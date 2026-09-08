#!/usr/bin/env python3
# THE SIMULATOR SKELETON (2026-09-03, owner: "build the skeleton then
# compile the spans") — the five constructs of THE EFFECTS LAW's engine:
#
#   1. A CLOCK with named eras — the driver is time, not a row list.
#   2. ENTITY LEDGERS — persistent, MUTABLE state: people, animals,
#      property, the court docket, Heaven's docket. Entries open and
#      close; a ledger that ends OPEN can be the correct ending.
#   3. LAWS AS DAEMONS — every registered law fires UNASKED on every
#      event; the law never decides that anyone ACTS (agency absent):
#      obligations are computed, acts come from the text.
#   4. TIMERS — effects owed to the FUTURE (the six-year term, the
#      jubilee): the construct that makes this a simulator and not a
#      ledger.
#   5. THE DIFF ENGINE — at each checkpoint the computed ledger is
#      compared against what the text/answer sheet declares.
#
# METHOD LAWS HONORED: the event tape below replays the tradition's own
# RECORDED cases (Mishnah rows, the sugya's exemplars — method law 4),
# never invented history (law 6, as clarified 2026-09-03: computed
# CONSEQUENCES are the output; the fence forbids invented EVENTS — and
# these scenes are labeled TEST SCENES, each citing its recorded
# source). Effects come ONLY from effect_vocabulary.yaml via
# effects_layer (the registry discipline). Disputes fork (law 3).
#
# THE EFFECT INTERFACE this skeleton fixes (the contract every span
# compile targets from now on):
#   {effect:      registry id (validated),
#    subject:     entity whose ledger takes the entry,
#    counterparty: entity on the other side (or None),
#    amount:      the data channel (quantities are DATA, never code),
#    due:         a future year (timers) or None (immediate),
#    source_law:  the compiled function that fired,
#    case_source: the recorded case the event replays}
#
# Model layer; read-only over the corpus; touches no unit.

import bisect
import collections
import os
import re
import yaml
import effects_layer as FX
import events_layer as EV      # THE EVENT-TYPE REGISTRY (D9-i): an unregistered kind refuses the tape

# THE CLOCK SITTING (2026-09-07; CLOCK.md; the specification ARCHITECTURE/THE_CLOCK.md; the two-thread consensus
# A-H with round two's eight amendments): the DAY is the base unit and the YEAR is DERIVED by a Calendar over the
# THIRD REGISTRY, calendar_parameters.yaml — this module its only reader (the code/data law: the mechanism is
# ink, the quantities are the registry's rows with their channels and sources). No tick stream: calendar
# boundaries are TIMERS set by the daemons whose verses command the count; a PERIOD field (opt-in) re-arms a
# timer at its fire through the Calendar; a MARKER log class carries the text's own dates; an event between
# markers carries its BOUND; a RETROGRADE marker (Pesachim 6b:7 — no earlier and later in the Torah) leaves the
# counter unmoved and dates the event; a past due writes at submission (RETRO-WRITE).
_CAL_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'calendar_parameters.yaml')
with open(_CAL_PATH, encoding='utf-8') as _f:
    _CAL = yaml.safe_load(_f)
CAL_PARAMS, CAL_ERAS = _CAL['parameters'], _CAL['eras']
LIFE_READING = CAL_PARAMS['life_year_reading']['value']    # THE SEQUENTIAL RUN: 'completed' or 'ordinal' (OPEN-8), a data row

# THE FENCE'S DEPTH BOUND (D9-ii, 2026-09-07): a daemon CONSUMES events and WRITES
# the ledger; it never emits an event. Cascades run through LEDGER STATE (one
# daemon's write satisfies another's condition on a later event), never through
# a daemon submitting. So no event is ever submitted while another is being
# consumed: the cascade depth bound is 1, and a re-entry is a daemon emitting
# an event — reported loudly, naming the daemon, never truncated silently.
DEPTH_BOUND = 1


# ---- construct 1: the clock, the calendar over the third registry ----
class Calendar:
    """THE CALENDAR FUNCTION (CLOCK.md section 2) — an engine construct, because the period re-arm fires inside
    advance() and the engine cannot import a runner. Lays the months out from the world's EPOCH ROW: the
    received month rounded to thirty and twenty-nine alternating (Rosh Hashanah 25a:10, the day grain's
    rounding), the year turning at the era's new-year month (Mishnah Rosh Hashanah 1:1 — a data row), the
    thirteenth month by the season ground alone (Sanhedrin 13a:4's recorded threshold over a MODELED solar
    year and equinox — OPEN-2, labeled). Keys: day, week, month, year, sabbatical, jubilee (Lev 25:4, 25:8,
    25:10 — the ink's counts; the count-start offset and the fiftieth's place in the cycle are data rows), and
    from O5 (2026-09-07) the FESTIVAL KEYS of the row festival_dates — Leviticus 23's own dates, a scene walking
    to a festival by next(key), a festival's recurrence a period timer keyed by it (CLOCK.md section 10)."""
    KEYS = ('day', 'week', 'month', 'year', 'sabbatical', 'jubilee')

    def __init__(self, epoch=None):
        P = CAL_PARAMS
        self.epoch = epoch
        self.era = CAL_ERAS[epoch] if epoch else None
        if epoch and epoch not in CAL_ERAS:
            raise SystemExit('CALENDAR: epoch %r is not a row of calendar_parameters.yaml eras' % epoch)
        self.nym = self.era['new_year_month'] if self.era else None
        self.leap_len = P['intercalated_month']['value']['length']
        self.threshold = P['intercalation_threshold_days']['value']
        self.solar = P['solar_year_days']['value']
        self.eq0 = P['equinox_offset_days']['value']
        self.sab, self.cyc, self.jub = P['sabbatical_years']['value'], P['cycle_years']['value'], P['jubilee_year']['value']
        self.offset = P['count_start_offset_years']['value']
        self.fiftieth = P['fiftieth_in_cycle']['value']
        # O5 THE MOADIM RE-TYPE (2026-09-07; CLOCK.md section 10): the FESTIVAL KEYS from Lev 23's own dates — the row
        # festival_dates (ink: {month, day}, {from, plus} on the named key, or {key: week}) and omer_day (received)
        self.festivals = dict((P.get('festival_dates') or {}).get('value') or {})
        if 'omer_day' in P:
            self.festivals['omer'] = P['omer_day']['value']
        self.keys = self.KEYS + tuple(k for k in self.festivals if k not in self.KEYS)
        self._months = []          # (start_day, year, month_no, length), laid out lazily from the epoch
        self._starts = []
        # O1 (2026-09-07; SEQUENTIAL_RUN.md section 12 e): the era row's `day_one_offset` — the days BEFORE the first
        # new-year month's first day (the creation era: 'day one' = the twenty-fifth of Elul, the sixth day = the first
        # of Tishrei — Vayikra Rabbah 29:1). A STUB MONTH is laid first: the preceding month of year 0, its start
        # negative so that day 0 is its (length − offset + 1)th day; the world's first year begins at day `offset`.
        self.day_one_offset = int((self.era or {}).get('day_one_offset') or 0)
        self.first_year_start = self.day_one_offset if (self.era and self.nym) else 0
        if self.era and self.nym:
            k = self.day_one_offset
            if k:
                pm = 12 if self.nym == 1 else self.nym - 1
                pl = self._plain_len(pm)
                self._months.append((k - pl, 0, pm, pl)); self._starts.append(k - pl)
            self._months.append((k, 1, self.nym, self._plain_len(self.nym)))
            self._starts.append(k)

    @staticmethod
    def _plain_len(m):
        return 30 if m % 2 == 1 else 29                      # the first month thirty, the second twenty-nine ...

    def _need(self):
        if not self._months:
            raise SystemExit('CALENDAR: the world declares no epoch — a derived year or a calendar key needs one '
                             '(World(era=..., epoch=<a row of calendar_parameters.yaml eras>))')

    def _lay_next(self):
        start, year, m, length = self._months[-1]
        nxt_start = start + length
        if m == 12:
            # the season ground (Sanhedrin 13a:4): project the next seventh month's first day without a leap
            # month — the months 1..6 = 177 days — and ask where the autumn equinox falls in it
            T = nxt_start + sum(self._plain_len(k) for k in range(1, 7))
            k = round((T - self.eq0) / self.solar)
            E = self.eq0 + k * self.solar
            dom = int(E - T) + 1
            if dom >= self.threshold:
                self._months.append((nxt_start, year, 13, self.leap_len)); self._starts.append(nxt_start)
                return
        nm = 1 if m in (12, 13) else m + 1
        ny = year + 1 if nm == self.nym else year
        self._months.append((nxt_start, ny, nm, self._plain_len(nm))); self._starts.append(nxt_start)

    def _extend_to_day(self, day):
        self._need()
        while self._months[-1][0] + self._months[-1][3] <= day:
            self._lay_next()

    def _extend_to_year(self, y):
        self._need()
        while self._months[-1][1] <= y:
            self._lay_next()

    def _month_at(self, day):
        self._extend_to_day(day)
        return self._months[bisect.bisect_right(self._starts, day) - 1]

    def year(self, day):
        return self._month_at(day)[1]

    def date(self, day):
        start, y, m, _ = self._month_at(day)
        return (y, m, day - start + 1)

    def day_of(self, y, m=None, dom=1):
        """the day of (year, month, day-of-month) in the epoch; month defaults to the era's new-year month"""
        self._extend_to_year(y)
        m = self.nym if m is None else m
        for start, yy, mm, length in self._months:
            if yy == y and mm == m:
                return start + min(dom, length) - 1
        if m == 13:                                          # no thirteenth month that year: the twelfth
            return self.day_of(y, 12, dom)
        raise SystemExit('CALENDAR: no month %r in year %r of the %s epoch' % (m, y, self.epoch))

    def position(self, y):
        """the count-year's place in the sabbatical/jubilee period, or None before the count began"""
        n = y - 1 - self.offset
        if n < 0:
            return None
        if self.fiftieth == 'not_counted':                   # the Sages (Rosh Hashanah 9a:1): fifty years to the period
            return n % self.jub + 1
        return n % self.cyc + 1                              # Rabbi Yehuda: the fiftieth counts for both (Arakhin 12b:4)

    def _is(self, key, y):
        p = self.position(y)
        if p is None:
            return False
        if key == 'sabbatical':
            return p % self.sab == 0 and p <= self.cyc
        n = y - 1 - self.offset
        return p == self.jub if self.fiftieth == 'not_counted' else (n > 0 and n % self.cyc == 0)

    def festival_day(self, y, key):
        """O5: the day of a festival key in year y — a {month, day} row by day_of, a {from, plus} row by the named key's
        day plus the ink's own count (the fiftieth from the omer, the eighth from the first)"""
        row = self.festivals[key]
        if 'key' in row:
            raise SystemExit('CALENDAR: %r is the %r key, not a date' % (key, row['key']))
        if 'from' in row:
            return self.festival_day(y, row['from']) + int(row['plus'])
        return self.day_of(y, int(row['month']), int(row['day']))

    def next(self, day, key):
        """the first boundary of `key` strictly after `day`"""
        if key == 'day':
            return day + 1
        if key == 'week':
            return day + 7
        if key in self.festivals:                             # O5: a festival key — this year's occurrence if still ahead, else the next year's
            row = self.festivals[key]
            if 'key' in row:
                return self.next(day, row['key'])
            self._extend_to_day(day)
            y = max(self.year(day), 1)
            d = self.festival_day(y, key)
            while d <= day:
                y += 1
                d = self.festival_day(y, key)
            return d
        if key not in self.KEYS:
            raise SystemExit('CALENDAR: unknown key %r (keys: %s)' % (key, ', '.join(self.keys)))
        self._extend_to_day(day)
        i = bisect.bisect_right(self._starts, day)
        while True:
            while i >= len(self._months):
                self._lay_next()
            start, y, m, _ = self._months[i]
            if key == 'month' or (m == self.nym and (key == 'year' or self._is(key, y))):
                return start
            i += 1

    def add(self, day, n, key):
        """n units of `key` later — the same date (a calendar key moves under intercalation)"""
        if key == 'day':
            return day + n
        if key == 'week':
            return day + 7 * n
        y, m, dom = self.date(day)
        if key == 'year':
            return self.day_of(y + n, m, dom)
        if key == 'month':
            d = day
            for _ in range(n):
                d = self.next(d, 'month')
            start, yy, mm, length = self._month_at(d)
            return start + min(dom, length) - 1
        raise SystemExit('CALENDAR: add() takes day, week, month, or year, not %r' % key)


class Era:
    """THE SEQUENTIAL RUN (2026-09-07; SEQUENTIAL_RUN.md section 2): an era is a VIEW on the one month table — an
    epoch day and a new-year month. Its year turns at the first day of its new-year month after the epoch; its months
    are counted ORDINALLY from the year's first month (before Exod 12:2 names month one, Gen 7:11's 'second month'
    counts from the creation era's first month — Rosh Hashanah 11b:6-7's two arms from one parameter; after it the
    exodus era counts from Nisan — Rosh Hashanah 3a:5). A LIFE era (new_year_month None) TURNS AT THE NEW YEAR (Gen
    8:13 — the sitting's correction): its year is the AGE as the calendar years' difference, and 'the Nth year of X's
    life' names age N under the running reading (the row life_year_reading; the ordinal reading names age N-1). An era
    is SET BY A MARKER, never by a literal day. The world's OWN era opens at the calendar's first new-year start (day 0,
    or the era row's day_one_offset — O1, 2026-09-07); the days before it read the calendar's year 0."""
    def __init__(self, cal, epoch_day, new_year_month, name=''):
        self.cal, self.epoch, self.nym, self.name = cal, epoch_day, new_year_month, name

    def _before_epoch(self, day):
        """a day before the era's epoch: the world's own era reads the calendar's stub (year 0); any other era refuses"""
        if self.name != self.cal.epoch and self.name != 'base':
            raise SystemExit('ERA %s: day %d falls before the era\'s epoch (day %d)' % (self.name, day, self.epoch))
        start, yy, mm, length = self.cal._month_at(day)
        return (yy, (mm - self.nym) % 12 + 1, day - start + 1)

    # -- a calendar-year era --
    def _year_starts(self, upto):
        self.cal._extend_to_day(upto)
        return [self.epoch] + [s for s, y, m, l in self.cal._months if self.epoch < s <= upto and m == self.nym]

    def _nth_year_start(self, y):
        starts = [self.epoch]
        i = bisect.bisect_right(self.cal._starts, self.epoch)
        while len(starts) < y:
            while i >= len(self.cal._months):
                self.cal._lay_next()
            s, yy, m, l = self.cal._months[i]
            if m == self.nym:
                starts.append(s)
            i += 1
        return starts[y - 1]

    # -- a life era: the life-year TURNS AT THE NEW YEAR (Gen 7:11 -> 8:13 -> 8:14: the 601st year's first month
    #    follows the 600th year's second month by ten and a half months — the ink's own interval), so the age is the
    #    calendar year's difference: completed years at the year grain --
    def _born_year(self):
        return self.cal.year(self.epoch)

    def _age(self, day):
        return self.cal.year(day) - self._born_year()

    def _base(self):
        return Era(self.cal, self.cal.first_year_start, self.cal.nym, 'base')

    def _ordinal_in_world_year(self, start):
        """the ordinal of the month beginning at `start` within the WORLD era's year (the calendar's own new-year month)"""
        yy = self.cal._month_at(start)[1]
        return 1 + sum(1 for s, y, m, l in self.cal._months if y == yy and s < start)

    def year(self, day):
        if self.nym is None:
            return self._age(day)
        if day < self.epoch:
            return self._before_epoch(day)[0]
        return len(self._year_starts(day))

    def date(self, day):
        """(year, ordinal month, day of month) — for a life era: (age, the world's ordinal month, day of month)"""
        start, yy, mm, length = self.cal._month_at(day)
        if self.nym is None:
            return (self._age(day), self._ordinal_in_world_year(start), day - start + 1)
        if day < self.epoch:
            return self._before_epoch(day)
        ys = self._year_starts(day)
        ystart = ys[-1]
        ordinal = 1 + sum(1 for s, y, m, l in self.cal._months if ystart < s <= day)
        return (len(ys), ordinal, day - start + 1)

    def day_of(self, y, m=1, dom=1, reading=None):
        """the day of (year y, ordinal month m, day dom) in this era; a life era finds the first such WORLD date inside the
        life-year the ink names (Gen 7:11 'the six hundredth year... the second month, the seventeenth')"""
        if self.nym is None:
            age = y if (reading or LIFE_READING) == 'completed' else y - 1     # 'the Nth year of X's life' = the calendar year in which X's completed age is N (the running reading)
            d = self._base().day_of(self._born_year() + age, m, dom)
            if d < self.epoch:
                raise SystemExit('ERA %s: (year %r, month %r, day %r) falls before the birth' % (self.name, y, m, dom))
            return d
        ystart = self._nth_year_start(y)
        i = bisect.bisect_right(self.cal._starts, ystart) - 1
        for _ in range(m - 1):
            i += 1
            while i >= len(self.cal._months):
                self.cal._lay_next()
        start, yy, mm, length = self.cal._months[i]
        return start + min(dom, length) - 1


class Clock:
    """the counter is the DAY; the year is DERIVED through the world's epoch (None where none is declared); ERAS are
    views set by markers (THE SEQUENTIAL RUN) — the world's own era is the epoch row's, at day 0"""
    def __init__(self, era, day=0, epoch=None):
        self.era, self.day, self.epoch = era, day, epoch
        self.calendar = Calendar(epoch)
        self.eras = {}
        if epoch:
            self.eras[epoch] = Era(self.calendar, self.calendar.first_year_start, self.calendar.nym, epoch)   # O1: the world's own era opens at the first new-year start (day_one_offset)

    @property
    def year(self):
        return self.calendar.year(self.day) if self.epoch else None

    @property
    def date(self):
        return self.calendar.date(self.day) if self.epoch else None

    @property
    def weekday(self):
        """O8 S1 (2026-09-08; NARRATIVE_GAPS.md convention 17): the WEEKDAY from the creation count — day 0 is 'day one'
        (Gen 1:5), day 6 the first Sabbath (2:2-3); 1 = the first day of the week ... 7 = the Sabbath. An engine
        derivation under the creation epoch alone (no other epoch row anchors a week); the shelf's weekday rows
        (Shabbat 87b:2-5) are graded AGAINST it by the sequence runner's checkpoints, never read into it."""
        return (self.day % 7) + 1 if self.epoch == 'creation' else None

    def at_year(self, y):
        return self.calendar.day_of(y)

    def after(self, n, key='day'):
        return self.calendar.add(self.day, n, key)

    def next(self, key):
        return self.calendar.next(self.day, key)

    # -- THE SEQUENTIAL RUN: eras as counters set by markers --
    def set_era(self, name, epoch_day, new_year_month=None):
        self.eras[name] = Era(self.calendar, epoch_day, new_year_month, name)
        return self.eras[name]

    def _era(self, name):
        if name not in self.eras:
            raise SystemExit('CLOCK: no era %r set — an era is set by a marker (world.marker(..., era=%r, new_year_month=...)), never by a literal day' % (name, name))
        return self.eras[name]

    def year_in(self, name):
        return self._era(name).year(self.day)

    def date_in(self, name):
        return self._era(name).date(self.day)

    def day_in(self, name, y, m=1, dom=1, reading=None):
        return self._era(name).day_of(y, m, dom, reading)


_SEAT = re.compile(r'^\s*(Gen|Exod|Lev|Num|Deut|1 Sam|2 Sam|1 Kgs|2 Kgs|1 Chr|2 Chr|Neh|Josh|Judg|Ruth|Isa|Jer|Ezek|Ps|Prov|Job|Song|Eccl|Lam|Esth|Dan|Ezra|Mal)\s+(\d+):')


def seat(src):
    """O2 THE ALIASES (2026-09-07; SEQUENTIAL_RUN.md section 13): the (book, chapter) of an event's FIRST cited verse — the
    scope a daemon reads to consume an act within its own span or a recorded run, never a string typed into a verdict;
    None when the source opens with a tractate or a Mishnah (a case row)"""
    m = _SEAT.match(src or '')
    return (m.group(1), int(m.group(2))) if m else None


# ---- construct 2: entities with mutable ledgers ---------------------
class Entity:
    def __init__(self, eid, kind):
        self.eid, self.kind = eid, kind
        self.status = {}      # persistent flags (slave, forewarned...)
        self.ledger = []      # entries written by verdicts

    def open_entries(self):
        return [e for e in self.ledger if e.get('open')]


class World:
    def __init__(self, era, epoch=None, registry=None):
        self.clock = Clock(era, epoch=epoch)
        self.entities = {}
        # THE SEQUENTIAL RUN (2026-09-07): THE ONE WHO-IS-WHO AT THE ENGINE — a scene token resolves to the registry's
        # entity id (logic/corpus/entity_registry.yaml's members with units [step9-scenes]); the daemons keep their
        # names, the ledgers merge. A world with no map behaves as before.
        self._registry = dict(registry or {})
        self.laws = []        # the daemon registry
        self.timers = []      # (fire_day, effect_dict) — a timer with a `period` re-arms at its fire
        self.log = []
        # THE CLOCK SITTING (2026-09-07): the bound and the marker (CLOCK.md section 4)
        self._last_marker = 0        # the last forward marker's day — every later event's bound opens here
        self._open_bounds = []       # the bound lists still open, SHARED by the event, its effects, timers, fires
        self._dated = None           # a retrograde stretch's stated day (Pesachim 6b:7), until the clock moves
        # D9-ii: every daemon's WATCH COVERAGE — events seen, events it fired on,
        # the kinds it fired on — printed by coverage(); the zero-report law's
        # instrument for the simulator (a daemon that never fires is visible)
        self.watch = collections.OrderedDict()
        self._depth = 0
        self._consuming = None

    def entity(self, eid, kind='person'):
        eid = self._registry.get(eid, eid)
        if eid not in self.entities:
            self.entities[eid] = Entity(eid, kind)
        return self.entities[eid]

    # -- construct 3: dispatch — every law fires, unasked -------------
    def submit(self, event):
        EV.validate([event['kind']])                  # the tape carries registered types only
        if self._depth >= DEPTH_BOUND:
            raise SystemExit('THE FENCE: World.submit re-entered at depth %d (bound %d) while %s was consuming an event — '
                             'a daemon emitted an event %r; daemons write the ledger, cascades run through ledger state'
                             % (self._depth + 1, DEPTH_BOUND, self._consuming, event.get('kind')))
        self._depth += 1
        try:
            if self._dated is not None:                      # inside a retrograde stretch: the text's own date, no bound
                event['dated'] = self._dated
                event.setdefault('day', self._dated)         # THE DATED DAY IS THE EVENT'S DAY (SEQUENTIAL_RUN.md section 2): a daemon that reads the event's day reads the text's date
            else:                                            # between markers: the bound [the last marker, open]
                b = [self._last_marker, None]
                event['bound'] = b
                self._open_bounds.append(b)
            self.log.append(('EVENT', self.clock.day, event))
            fired = 0
            for law in self.laws:
                name = getattr(law, '__name__', repr(law))
                w = self.watch.setdefault(name, {'seen': 0, 'fired': 0, 'kinds': set()})
                w['seen'] += 1
                self._consuming = name
                effs = law(event, self) or []
                self._consuming = None
                if effs:
                    w['fired'] += 1
                    w['kinds'].add(event['kind'])
                for eff in effs:
                    fired += 1
                    for key in ('bound', 'dated'):           # the engine copies the event's bound/date onto its effects
                        if key in event:
                            eff.setdefault(key, event[key])
                    self._write(eff)
            return fired
        finally:
            self._depth -= 1

    def coverage(self):
        """every daemon's watch coverage: {daemon: (events seen, events fired on, kinds fired on)}"""
        return collections.OrderedDict((n, (w['seen'], w['fired'], sorted(w['kinds']))) for n, w in self.watch.items())

    def print_coverage(self):
        for n, (seen, fired, kinds) in self.coverage().items():
            print('  WATCH %-22s seen %3d  fired %3d  on: %s' % (n, seen, fired, ', '.join(kinds) or '(never fired)'))

    def _write(self, eff):
        FX.validate([eff['effect']])
        now = self.clock.day
        if eff.get('due') is not None and eff['due'] > now:
            self.timers.append((eff['due'], eff))     # construct 4
            self.log.append(('TIMER-SET', now, eff))
            return
        ent = self.entity(eff['subject'])
        op = FX.REGISTRY[eff['effect']]['ledger_op']
        entry = dict(eff, op=op, day=now, year=self.clock.year,
                     open=(op in ('debit', 'heaven', 'body')))
        ent.ledger.append(entry)
        if op == 'status':
            ent.status[eff['effect']] = eff.get('value', True)
        if eff.get('due') is not None and eff['due'] < now:   # a due already past (a retrograde stretch): written now, named
            self.log.append(('RETRO-WRITE', now, entry))
        else:
            self.log.append(('WRITE', now, entry))

    def close(self, eid, effect, note, value=None):
        """an entry closes when the text records the closing act; with `value` the entry whose value matches closes
        (O8 S1, 2026-09-08: the frogs' removal closes the FROGS' plague entry, not the first open plague — probe 18)"""
        for e in self.entity(eid).ledger:
            if e['effect'] == effect and e.get('open') and (value is None or e.get('value') == value):
                e['open'] = False
                e['closed_by'] = note
                return True
        return False

    def cancel_timers(self, subject, effect, note):
        """a later TEXT event voids a pending timer (the pierced slave's
        'forever' voids his six-year exit — Exod 21:5-6): the interface
        gap the skeleton's first spin exposed"""
        kept, cut = [], 0
        subject = self._registry.get(subject, subject)
        for day, eff in self.timers:
            if self._registry.get(eff['subject'], eff['subject']) == subject and eff['effect'] == effect:
                cut += 1
                self.log.append(('TIMER-CANCEL', self.clock.day,
                                 dict(eff, cancelled_by=note)))
            else:
                kept.append((day, eff))
        self.timers = kept
        return cut

    def marker(self, verse, day, value=None, era=None, new_year_month=None, proleptic=False):
        """THE MARKER (CLOCK.md section 4): the text's own date stamp sets the clock. A marker at or after the
        counter walks advance(day) and CLOSES every open bound at it; a marker EARLIER than the counter is
        RETROGRADE (Pesachim 6b:7 — 'there is no earlier and later in the Torah'; Num 9:1 after 1:1): logged,
        the counter unmoved, the following events dated by the text until the clock next moves.
        THE SEQUENTIAL RUN (SEQUENTIAL_RUN.md section 2): `era` names an era whose EPOCH this marker sets at `day`
        (Exod 12:2 sets the exodus era; a begetting sets life:<entity>); `proleptic` is the third class — a paragraph's
        CLOSING TOTAL ('all the days of X were N years, and he died'), logged at its computed day with the counter
        unmoved and no dated stretch opened: the text's summary of a life, not a clock stamp for the next verse."""
        if era is not None:
            self.clock.set_era(era, day, new_year_month)
        if proleptic:
            self.log.append(('MARKER', self.clock.day, {'verse': verse, 'value': value, 'retrograde': False, 'proleptic': True, 'stated': day}))
            return day
        if day < self.clock.day:
            self.log.append(('MARKER', self.clock.day, {'verse': verse, 'value': value, 'retrograde': True, 'stated': day}))
            self._dated = day
            return day
        self._dated = None
        self.advance(day)
        for b in self._open_bounds:
            b[1] = day
        self._open_bounds = []
        self._last_marker = day
        self.log.append(('MARKER', day, {'verse': verse, 'value': value, 'retrograde': False}))
        return day

    # -- construct 4: time advances; due timers fire; a period re-arms --
    def advance(self, to_day):
        if to_day > self.clock.day:
            self._dated = None                               # the clock moves: the retrograde stretch is over
        while self.clock.day < to_day:
            self.clock.day += 1
            now = self.clock.day
            due = [t for t in self.timers if t[0] == now]
            self.timers = [t for t in self.timers if t[0] != now]
            for _, eff in due:
                fired = dict(eff, due=None)
                self.log.append(('TIMER-FIRE', now, fired))
                self._write(fired)
                p = eff.get('period')
                if p is not None:                            # THE PERIOD FIELD (consensus G): re-armed through the Calendar
                    nxt = now + p if isinstance(p, int) else self.clock.calendar.next(now, p)
                    re = dict(eff, due=nxt, rearmed_from=now)
                    self.timers.append((nxt, re))
                    self.log.append(('TIMER-SET', now, re))

    # -- construct 5: the diff engine ----------------------------------
    def checkpoint(self, name, declared, computed, bound=None):
        """declared against computed; with a BOUND, the computed day is tested against the interval the text
        dates the originating event within (an open bound is tested to now, and says so)"""
        if bound is not None:
            lo, hi = bound[0], (bound[1] if bound[1] is not None else self.clock.day)
            ok = lo <= computed <= hi
            print('  CHECKPOINT %-34s %s  within [%s, %s]%s' % (name, 'MATCH' if ok else 'DIVERGE', lo, hi,
                                                                '' if bound[1] is not None else ' (open bound: tested to now)'))
            if not ok:
                print('    computed: %s' % (computed,))
            return ok
        ok = declared == computed
        print('  CHECKPOINT %-34s %s' % (name, 'MATCH' if ok else 'DIVERGE'))
        if not ok:
            print('    declared: %s' % (declared,))
            print('    computed: %s' % (computed,))
        return ok


# =====================================================================
# THE LAW LIBRARY — the three compiled functions wrapped as daemons.
# Each daemon cites the cold run that compiled it; verdict logic is the
# compiled logic; every effect is registry-validated at write time.
# =====================================================================

def law_slave_term(event, world):
    """Exod 21:2-6 (cold_run_mishpatim.py F1). The term clock. THE CLOCK SITTING (2026-09-07): the six years
    are a calendar due (the same date six years on), the pierced servant's jubilee a due the Calendar computes
    (the year no longer passed inside the event), and the proclamation CANCELS each freed servant's pending
    term (THE PENDING TERM, REPORT_WRAP_W5.md finding 1) — deferring the release itself to the land's
    `jubilee_holds` verdict where a jubilee daemon registered before it has written one."""
    if event['kind'] == 'acquire_hebrew_slave':
        s = event['slave']
        world.entity(s).status['hebrew_slave'] = True
        return [
            {'effect': 'term_clock', 'subject': s,
             'counterparty': event['master'], 'amount': 6,
             'due': None, 'source_law': 'F1 slave-release [INK 21:2]',
             'case_source': event['case_source']},
            {'effect': 'goes_free', 'subject': s, 'counterparty': None,
             'amount': None, 'due': world.clock.after(6, 'year'),
             'source_law': 'F1 FREE-YEAR-7 [INK 21:2: six + seventh + free — the same date six years on]',
             'case_source': event['case_source']},
        ]
    if event['kind'] == 'slave_pierced':
        # Exod 21:5-6 "forever" — the piercing VOIDS the six-year exit
        # (the slave's recorded declaration is a text event; the law
        # only recomputes the consequences), yet the jubilee overrides
        s = event['slave']
        world.entity(s).status['pierced_forever'] = True
        world.cancel_timers(s, 'goes_free',
                            'the piercing [INK Exod 21:5-6 "I love my '
                            'master... he shall serve him forever"]')
        return [
            {'effect': 'jubilee_release', 'subject': s, 'counterparty': None,
             'amount': None, 'due': world.clock.next('jubilee'),
             'source_law': 'F1 FREE-AT-JUBILEE [IMPORT Lev 25; Kiddushin '
                           '15a:19: written even for the pierced "forever" — the due the Calendar computes]',
             'case_source': event['case_source']},
        ]
    if event['kind'] == 'jubilee_proclaimed':
        # the institutional flag flips on a text event, era-wide; where a jubilee daemon (law_yovel) has
        # written the land's verdict first, that verdict rules: no arm holding = no release, the term kept
        holds = world.entity(event.get('land', 'the-land')).status.get('jubilee_holds')
        if isinstance(holds, str) and holds.startswith('no jubilee'):
            return []                                        # no arm holds (the verdict named on the land): the servants serve on
        out = []
        for ent in world.entities.values():
            if ent.status.get('hebrew_slave'):
                world.cancel_timers(ent.eid, 'goes_free',
                                    'the jubilee [Lev 25:10 liberty proclaimed; Kiddushin 15a:19] — THE PENDING TERM cut')
                out.append(
                    {'effect': 'goes_free', 'subject': ent.eid,
                     'counterparty': None, 'amount': None, 'due': None,
                     'value': holds if holds is not None else True,
                     'source_law': 'F1 FREE-AT-JUBILEE',
                     'case_source': event['case_source']})
        return out
    return []


def law_goring_ox(event, world):
    """Exod 21:28-36 (cold_run_mishpatim.py F3). The state machine."""
    if event['kind'] != 'ox_gores':
        return []
    ox = world.entity(event['ox'], 'animal')
    gorings = ox.status.get('gorings', 0) + 1
    ox.status['gorings'] = gorings
    out = []
    if event.get('victim_kind') == 'human':
        out.append({'effect': 'stoned', 'subject': event['ox'],
                    'counterparty': None, 'amount': None, 'due': None,
                    'source_law': 'F3 STONE+RANSOM [INK 21:29-30]',
                    'case_source': event['case_source']})
        if ox.status.get('forewarned'):
            out.append({'effect': 'ransom_imposed',
                        'subject': event['owner'],
                        'counterparty': event['victim'], 'amount': None,
                        'due': None,
                        'source_law': 'F3 [INK 21:30 IM-branch]',
                        'case_source': event['case_source']})
        return out
    if event.get('victim_kind') == 'slave':
        # W1 (2026-09-07): Exod 21:32 "if the ox gores a slave or a maidservant:
        # thirty shekels of silver he shall give to his master, and the ox shall
        # be stoned" — the fixed sum the Mishnah repeats (Bava Kamma 4:5); the
        # victim party on the tape is the slave's master, who is paid
        out.append({'effect': 'stoned', 'subject': event['ox'],
                    'counterparty': None, 'amount': None, 'due': None,
                    'source_law': 'F3 30-SHEKELS [INK 21:32 "and the ox shall be stoned"]',
                    'case_source': event['case_source']})
        out.append({'effect': 'gives_fixed_sum', 'subject': event['owner'],
                    'counterparty': event['victim'], 'amount': 30, 'due': None,
                    'source_law': 'F3 30-SHEKELS [INK 21:32 thirty shekels to his master]',
                    'case_source': event['case_source']})
        return out
    if ox.status.get('forewarned'):
        out.append({'effect': 'pays', 'subject': event['owner'],
                    'counterparty': event['victim'],
                    'amount': event.get('damage'),
                    'due': None,
                    'source_law': 'F3 FULL [INK 21:36 "ox for ox"]',
                    'case_source': event['case_source']})
    else:
        out.append({'effect': 'pays', 'subject': event['owner'],
                    'counterparty': event['victim'],
                    'amount': (event.get('damage') or 0) / 2.0,
                    'due': None,
                    'source_law': 'F3 HALF-FROM-BODY [INK 21:35 "divide"]',
                    'case_source': event['case_source']})
    if gorings >= 3 and not ox.status.get('forewarned'):
        ox.status['forewarned'] = True
        out.append({'effect': 'forewarned', 'subject': event['ox'],
                    'counterparty': None, 'amount': None, 'due': None,
                    'source_law': 'F3 THREE [RECORDED Bava Kamma 23b:17-18]',
                    'case_source': event['case_source']})
    return out


GUARDIAN_MATRIX = {  # the compiled 12/12 matrix (cold_run_guardians.py)
    ('unpaid', 'accidents'): 'oath_imposed', ('unpaid', 'theft'): 'oath_imposed',
    ('unpaid', 'loss'): 'oath_imposed',
    ('paid', 'accidents'): 'oath_imposed', ('paid', 'theft'): 'pays',
    ('paid', 'loss'): 'pays',
    ('renter', 'accidents'): 'oath_imposed', ('renter', 'theft'): 'pays',
    ('renter', 'loss'): 'pays',
    ('borrower', 'accidents'): 'pays', ('borrower', 'theft'): 'pays',
    ('borrower', 'loss'): 'pays',
}


def law_guardians(event, world):
    """Exod 22:6-14 (cold_run_guardians.py). The four keepers."""
    if event['kind'] != 'bailment_claim':
        return []
    eff = GUARDIAN_MATRIX[(event['keeper_role'], event['happening'])]
    return [{'effect': eff, 'subject': event['keeper'],
             'counterparty': event['owner'],
             'amount': event.get('value') if eff == 'pays' else None,
             'due': None,
             'source_law': 'guardians 12/12 matrix [cold_run_guardians.py]',
             'case_source': event['case_source']}]


def law_deposit_oath(event, world):
    """Lev 5:20-26 (cold_run_vayikra5.py deposit_restitution)."""
    if event['kind'] != 'sworn_denial_admitted':
        return []
    base = event['value']
    out = [
        {'effect': ('restores' if event.get('object_exists') else 'pays'),
         'subject': event['claimant_against'],
         'counterparty': event['owner'], 'amount': base, 'due': None,
         'source_law': 'deposit_restitution [INK Lev 5:23 restitution FIRST]',
         'case_source': event['case_source']},
        {'effect': 'adds_fifth', 'subject': event['claimant_against'],
         'counterparty': event['owner'], 'amount': base / 4.0, 'due': None,
         'source_law': 'deposit_restitution [MOVE Sifra Section 13 8: '
                       'the added-quarter fifth]',
         'case_source': event['case_source']},
        {'effect': 'atoned_forgiven', 'subject': event['claimant_against'],
         'counterparty': 'HEAVEN', 'amount': None, 'due': None,
         'source_law': 'deposit_restitution [INK Lev 5:25-26 the ram, '
                       'and he shall be forgiven]',
         'case_source': event['case_source']},
    ]
    return out


def law_installation(event, world):
    """Lev 8 (cold_run_tzav.py F7, the Tzav round 2026-09-03). The
    installation transaction: ATOMIC over bullock + two rams + basket
    (Sifra, Tzav, Mekhilta DeMiluim I 19); the seven-day confinement
    timer (8:33); the commit at the blood sprinkling (DeMiluim I 34);
    the leftover clause (8:32)."""
    k = event['kind']
    day = event.get('day', world.clock.day)      # THE SEQUENTIAL RUN: the event's own day (the text's date inside a retrograde stretch — Lev 8 after Exod 40:17)
    if k == 'installation_commanded':
        required = {'bullock', 'ram_olah', 'ram_milluim', 'basket'}
        if not required.issubset(set(event['components'])):
            world.log.append(('ATOMIC-BLOCK', world.clock.year,
                              dict(event, missing=sorted(
                                  required - set(event['components'])))))
            return []          # no component, no sanctification
        subj = event['subject']
        return [
            {'effect': 'confined_seven_days', 'subject': subj,
             'counterparty': None, 'amount': 7, 'due': None,
             'source_law': 'F7 confinement [INK 8:33: you shall not '
                           'go out seven days]',
             'case_source': event['case_source']},
            {'effect': 'released', 'subject': subj, 'counterparty': None,
             'amount': None, 'due': day + 7,                     # THE CLOCK SITTING: the counter is the day; THE SEQUENTIAL RUN: the event's day
             'source_law': 'F7 completion [INK 8:33: until the day of '
                           'the filling of your installation days]',
             'case_source': event['case_source']},
        ]
    if k == 'milluim_blood_sprinkled':
        return [
            {'effect': 'invested_office', 'subject': event['subject'],
             'counterparty': None, 'amount': None, 'due': None,
             'source_law': 'F7 commit [Sifra, Tzav, Mekhilta DeMiluim '
                           'I 34: consummated only at the blood '
                           'sprinkling]',
             'case_source': event['case_source']},
        ]
    if k == 'milluim_leftover':
        return [
            {'effect': 'burn_remainder', 'subject': event['subject'],
             'counterparty': None, 'amount': None, 'due': None,
             'source_law': 'F7 leftover [INK 8:32: what remains you '
                           'shall burn in fire]',
             'case_source': event['case_source']},
        ]
    return []


# =====================================================================
# THE TEST TAPE — recorded cases only, each citing its source
# (method law 4: the tradition's own worked examples; law 6: these are
# TEST SCENES replaying recorded cases, never generated history).
# =====================================================================
def run():
    print('THE SIMULATOR SKELETON — first spin (2026-09-03)')
    print('era: TEST SCENES over the tradition\'s recorded cases\n')
    w = World(era='test-scenes (recorded cases; the count epoch — the day the base unit, the year derived)', epoch='count')
    w.laws = [law_slave_term, law_goring_ox, law_guardians,
              law_deposit_oath]
    assert w.laws, 'ZERO-REPORT: empty law library'
    results = []

    # SCENE 1 — the term clock (Mishnah Kiddushin 1:2: "acquires
    # himself by years"). Recorded case: the Hebrew slave's six years.
    print('SCENE 1 — the six-year term [Mishnah Kiddushin 1:2]')
    w.submit({'kind': 'acquire_hebrew_slave', 'slave': 'the-slave',
              'master': 'the-master',
              'case_source': 'Mishnah Kiddushin 1:2'})
    w.advance(w.clock.at_year(6))                # acquired in year 1: six years of service run to the same date in year 7
    mid = w.entity('the-slave').status.get('hebrew_slave') and \
        not any(e['effect'] == 'goes_free'
                for e in w.entity('the-slave').ledger)
    w.advance(w.clock.at_year(7))
    freed = any(e['effect'] == 'goes_free'
                for e in w.entity('the-slave').ledger)
    results.append(w.checkpoint(
        'year 6: still serving; year 7: free',
        (True, True), (bool(mid), bool(freed))))

    # SCENE 2 — the goring ox turns forewarned (Mishnah Bava Kamma 1:4
    # + 2:4 + the threshold at Bava Kamma 23b). Three recorded gorings.
    print('\nSCENE 2 — the ox state machine [Mishnah Bava Kamma 1:4, 2:4]')
    for n in (1, 2, 3):
        w.submit({'kind': 'ox_gores', 'ox': 'the-ox', 'owner': 'the-owner',
                  'victim': 'neighbor-%d' % n, 'damage': 100,
                  'case_source': 'Mishnah Bava Kamma 2:4 (goring #%d)' % n})
    w.submit({'kind': 'ox_gores', 'ox': 'the-ox', 'owner': 'the-owner',
              'victim': 'neighbor-4', 'damage': 100,
              'case_source': 'Mishnah Bava Kamma 1:4 (forewarned, full)'})
    owner = w.entity('the-owner')
    halves = [e['amount'] for e in owner.ledger
              if e['effect'] == 'pays' and e['amount'] == 50.0]
    fulls = [e['amount'] for e in owner.ledger
             if e['effect'] == 'pays' and e['amount'] == 100]
    flipped = w.entity('the-ox').status.get('forewarned', False)
    results.append(w.checkpoint(
        '3 half-payments, flip, then full',
        (3, True, 1), (len(halves), flipped, len(fulls))))

    # SCENE 3 — the keepers (Mishnah Shevuot 8:1's own table): the
    # unpaid keeper swears on theft; the paid keeper pays on theft.
    print('\nSCENE 3 — two keepers, one theft [Mishnah Shevuot 8:1]')
    w.submit({'kind': 'bailment_claim', 'keeper': 'keeper-unpaid',
              'keeper_role': 'unpaid', 'happening': 'theft',
              'owner': 'depositor', 'value': 200,
              'case_source': 'Mishnah Shevuot 8:1'})
    w.submit({'kind': 'bailment_claim', 'keeper': 'keeper-paid',
              'keeper_role': 'paid', 'happening': 'theft',
              'owner': 'depositor', 'value': 200,
              'case_source': 'Mishnah Shevuot 8:1'})
    got = (w.entity('keeper-unpaid').ledger[-1]['effect'],
           w.entity('keeper-paid').ledger[-1]['effect'])
    results.append(w.checkpoint(
        'unpaid swears; paid pays',
        ('oath_imposed', 'pays'), got))

    # SCENE 4 — the sworn deposit (Mishnah Bava Kamma 9:7 family, the
    # compiled Lev 5:20-26): restitution + fifth + Heaven's docket.
    print('\nSCENE 4 — the sworn deposit [Mishnah Bava Kamma 9:5/9:7]')
    w.submit({'kind': 'sworn_denial_admitted',
              'claimant_against': 'the-denier', 'owner': 'the-robbed',
              'value': 4.0, 'object_exists': False,
              'case_source': 'Mishnah Bava Kamma 9:5 (the four-value case '
                             'of Bava Metzia 54a)'})
    d = w.entity('the-denier')
    eff_seq = [e['effect'] for e in d.ledger]
    heaven_open = [e for e in d.ledger
                   if e['op'] == 'heaven' and e['open']]
    # the ram is BROUGHT in the recorded case — the text's act closes it
    w.close('the-denier', 'atoned_forgiven',
            'the ram brought [Lev 5:25, the recorded case]')
    results.append(w.checkpoint(
        'pay + fifth(1.00) + forgiven-closed',
        (['pays', 'adds_fifth', 'atoned_forgiven'], 1.0, 0),
        (eff_seq, [e['amount'] for e in d.ledger
                   if e['effect'] == 'adds_fifth'][0],
         len([e for e in d.ledger if e['op'] == 'heaven' and e['open']]))))

    # SCENE 5 — the pierced slave and the jubilee (Kiddushin 15a:19:
    # the jubilee frees even the pierced "forever"). Era-scale timer.
    print('\nSCENE 5 — "forever" meets the jubilee [Kiddushin 15a:19; '
          'Lev 25:10]')
    w.submit({'kind': 'acquire_hebrew_slave', 'slave': 'the-pierced',
              'master': 'the-master',
              'case_source': 'Mishnah Kiddushin 1:2'})
    w.submit({'kind': 'slave_pierced', 'slave': 'the-pierced',
              'case_source': 'Kiddushin 15a:19 on Exod 21:6 + Lev 25:10'})
    w.advance(w.clock.next('jubilee'))            # the Calendar's next jubilee: the fiftieth count-year's first day
    freed2 = [e for e in w.entity('the-pierced').ledger
              if e['effect'] == 'jubilee_release']
    six_yr_freed = [e for e in w.entity('the-pierced').ledger
                    if e['effect'] == 'goes_free']
    cancels = len([l for l in w.log if l[0] == 'TIMER-CANCEL'])
    results.append(w.checkpoint(
        'six-year exit VOIDED; jubilee fires at the fiftieth',
        (0, 1, 1), (len(six_yr_freed), len(freed2), cancels)))

    # SCENE 6 — the installation tape (Lev 8's OWN recorded narrative —
    # the tape is the ink itself: the atomic intake, the seven days at
    # the door, the commit at the sprinkling, the leftover burned).
    # A fresh world: this tape's clock unit is DAYS (the Clock is a
    # bare counter; the era label declares the unit honestly).
    print('\nSCENE 6 — the installation tape [Lev 8; Sifra, Tzav, '
          'Mekhilta DeMiluim I; cold_run_tzav.py F7]')
    wi = World(era='installation week (clock unit: days)')
    wi.laws = [law_installation]
    # the atomicity gate first: a defective intake sanctifies nothing
    fired_missing = wi.submit({'kind': 'installation_commanded',
                               'subject': 'aaron-and-sons',
                               'components': ['bullock', 'ram_olah',
                                              'ram_milluim'],
                               'case_source': 'Sifra, Tzav, Mekhilta '
                                              'DeMiluim I 19 (no basket '
                                              '— not sanctified)'})
    blocked = len([l for l in wi.log if l[0] == 'ATOMIC-BLOCK'])
    # the recorded intake (Lev 8:2 — all components taken)
    wi.submit({'kind': 'installation_commanded',
               'subject': 'aaron-and-sons',
               'components': ['bullock', 'ram_olah', 'ram_milluim',
                              'basket'],
               'case_source': 'Lev 8:2 (the take-list, audited against '
                              'Exod 29)'})
    wi.submit({'kind': 'milluim_blood_sprinkled',
               'subject': 'aaron-and-sons',
               'case_source': 'Lev 8:30 (the sprinkling; DeMiluim I 34 '
                              'the commit)'})
    wi.submit({'kind': 'milluim_leftover', 'subject': 'aaron-and-sons',
               'case_source': 'Lev 8:32'})
    wi.advance(7)              # the seven days pass; the release fires
    aas = wi.entity('aaron-and-sons')
    confined = [e for e in aas.ledger if e['effect'] == 'confined_seven_days']
    invested = [e for e in aas.ledger if e['effect'] == 'invested_office']
    released = [e for e in aas.ledger if e['effect'] == 'released']
    burned = [e for e in aas.ledger if e['effect'] == 'burn_remainder']
    results.append(w.checkpoint(
        'atomic-block; confined+invested+burned; release fires day 7',
        (1, 0, 1, 1, 1, 1),
        (blocked, fired_missing, len(confined), len(invested),
         len(burned), len(released))))

    # ---- the honest OPEN ledger --------------------------------------
    print('\nTHE OPEN LEDGER at end of tape (a ledger that ends OPEN '
          'can be the correct ending):')
    open_total = 0
    for ent in w.entities.values():
        for e in ent.open_entries():
            open_total += 1
            print('  OPEN  %-12s %-16s [%s] amount=%s  <- %s' %
                  (ent.eid, e['effect'], e['op'], e.get('amount'),
                   e['case_source']))
    print('  (%d entries stand open: the recorded cases state the '
          'obligation and record no payment event — the fence forbids '
          'inventing one)' % open_total)

    n_ok = sum(results)
    print('\nRESULT: %d/%d checkpoints MATCH.' % (n_ok, len(results)))
    ops = {}
    for _, _, entry in [l for l in w.log if l[0] == 'WRITE']:
        ops[entry['op']] = ops.get(entry['op'], 0) + 1
    print('LEDGER OPS written this run:',
          ', '.join('%s x%d' % kv for kv in sorted(ops.items())))
    timers_fired = len([l for l in w.log if l[0] == 'TIMER-FIRE'])
    print('TIMERS fired: %d (the six-year term; the jubilee)' % timers_fired)
    print('WATCH COVERAGE (D9-ii — every daemon prints what it saw and what it fired on):')
    w.print_coverage()
    wi.print_coverage()
    if n_ok == len(results):
        print('\nTHE SKELETON STANDS — the effect interface is fixed; '
              'span compiles now target this contract.')
    return n_ok == len(results)


if __name__ == '__main__':
    ok = run()
    raise SystemExit(0 if ok else 1)
