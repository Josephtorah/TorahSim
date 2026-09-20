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
import functools
import os
import re
import yaml
import ink_cache; ink_cache.install()   # THE VERIFIED-IMPORT CACHE (2026-09-19): the cold_run_* modules load through it — see ink_cache.py
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
# O9 THE CLOCK'S OPEN ITEMS (2026-09-08; CLOCK.md section 12): the third registry's two further blocks — the DAY SLOTS (12e: the
# ink's own day-words in the calendar day's order from Gen 1:5, evening then morning; the Calendar reads them for slot_rank and
# crosses_day; nothing in the engine counts hours) and the COUNTER IDIOMS (12c: per subject class — people, kings, animals,
# trees, inclusive day counts, the jubilee's boundary year — DATA rows read by no code yet, visible in the parameters census)
CAL_SLOTS = list(_CAL.get('day_slots') or [])
CAL_IDIOMS = dict(_CAL.get('counter_idioms') or {})
LIFE_READING = CAL_PARAMS['life_year_reading']['value']    # THE SEQUENTIAL RUN: 'completed' or 'ordinal' (OPEN-8), a data row

# THE LOOP step 3 INSTALLATION (2026-09-09; World/step9/THE_LOOP.md "Step 3 INSTALLATION — the design"; the decisions D1-D6):
# THE FOURTH REGISTRY, installation_parameters.yaml — the two parameter rows (installation_setting: boot / from_event, the
# running value `boot` until the second pass after Deuteronomy, D2; case_output: the generations' rule / the provisional edict,
# Sanhedrin 80b:5) and the table of INSTALLING ACTS: the registered act kind that switches an institution on → the institution
# and the scene token the tent daemon writes `in_force` on. This module its only reader. A law is IN FORCE when it has been
# SPOKEN (the run's position in the text has reached its given_at) and its INSTITUTION STANDS (Chagigah 6b:2); every daemon's
# two fields live in daemon_dispositions.yaml and the daemon gate demands them; the dispatch gate is in World.submit, never
# at registration (CLOCK.md section 8).
_INST_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'installation_parameters.yaml')
with open(_INST_PATH, encoding='utf-8') as _f:
    _INST = yaml.safe_load(_f)
INSTALL_PARAMS, INSTALLING_ACTS = _INST['parameters'], _INST['installing_acts']
INSTALL_FIELDS = ('given_at', 'installed_by')
INSTALL_VALUES = ('boot', 'pending')       # the two non-act values: in force from creation; the installing act not yet on the tape (counted)
BOOK_ORDER = {'Gen': 1, 'Exod': 2, 'Lev': 3, 'Num': 4, 'Deut': 5}

# THE POPULATION TABLE (THE NUMBERS WALK sitting 8b, 2026-09-11; NUMBERS_WALK.md "Sitting 8b — THE POPULATION TABLE — THE DESIGN"; the
# speculation ARCHITECTURE/DATABASE_SPECULATION.md): THE FIFTH REGISTRY — population_schema.yaml names the tables, their columns (the
# ink's own words) and their grains (counted / named / delta) with the required and optional columns. World.row validates every row
# against it; the schema is data, never a constant in code. The table is engine STATE (World.tables), queried by daemons during the
# run (World.population) and journaled afterward as the log's own class ROW (run.row — the fifth view run_population reads it back).
_POP_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'population_schema.yaml')
with open(_POP_PATH, encoding='utf-8') as _f:
    POP_SCHEMA = yaml.safe_load(_f)['tables']
POP_STAMPS = ('written_by', 'day', 'year', 'table')


def verse_key(src):
    """THE VERSE REACHED's order key: the canonical position of a reference's first cited verse (Gen < Exod < Lev < Num < Deut;
    any other book after them in the parser's order); None when the string opens with no verse"""
    fv = first_verse(src)
    return (BOOK_ORDER.get(fv[0], 99), fv[1], fv[2]) if fv else None

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

    def elapsed(self, day):
        """O9 T3 (2026-09-08; CLOCK.md 12a): ELAPSED — the completed years since the epoch's first New Year, the LABEL LESS
        ONE at the year grain (the tradition's anno mundi is completed years: Avodah Zarah 9a:7-8's two thousand at Abraham's
        fifty-two); a derived RENDERING, never a second counter; the stub month's days read −1 by the same arithmetic"""
        return self.year(day) - 1

    def date(self, day):
        start, y, m, _ = self._month_at(day)
        return (y, m, day - start + 1)

    # -- O9 OPEN-5 (CLOCK.md 12e): the day's slots in the ink's order; the day stays the unit --
    def slot_rank(self, name):
        """the slot's rank in the calendar day (Gen 1:5: evening then morning — the day begins at evening), from the
        registry's day_slots block; an unknown slot refuses, naming the slots"""
        names = [r['name'] for r in CAL_SLOTS]
        if name not in names:
            raise SystemExit('CALENDAR: unknown slot %r (slots: %s)' % (name, ', '.join(names)))
        return names.index(name)

    def crosses_day(self, a, b):
        """slot b narrated after slot a lies on the NEXT calendar day when its rank is below a's (the night after the
        morning) — the stitcher's slot-regression report reads it; the counter moves by markers only"""
        return self.slot_rank(b) < self.slot_rank(a)

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

    def elapsed(self, day):
        """O9 T3: a calendar-year era's elapsed is its label less one; a LIFE era's is its age as it stands (completed years
        already — the correction of Gen 8:13)"""
        return self._age(day) if self.nym is None else self.year(day) - 1

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
    def elapsed(self):
        return self.calendar.elapsed(self.day) if self.epoch else None

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

    def elapsed_in(self, name):
        return self._era(name).elapsed(self.day)

    def date_in(self, name):
        return self._era(name).date(self.day)

    def day_in(self, name, y, m=1, dom=1, reading=None):
        return self._era(name).day_of(y, m, dom, reading)


_SEAT = re.compile(r'^\s*(Gen|Exod|Lev|Num|Deut|1 Sam|2 Sam|1 Kgs|2 Kgs|1 Chr|2 Chr|Neh|Josh|Judg|Ruth|Isa|Jer|Ezek|Ps|Prov|Job|Song|Eccl|Lam|Esth|Dan|Ezra|Mal)\s+(\d+):')


_VERSE = re.compile(r'^\s*(Gen|Exod|Lev|Num|Deut|1 Sam|2 Sam|1 Kgs|2 Kgs|1 Chr|2 Chr|Neh|Josh|Judg|Ruth|Isa|Jer|Ezek|Ps|Prov|Job|Song|Eccl|Lam|Esth|Dan|Ezra|Mal)\s+(\d+):(\d+)')


def first_verse(src):
    """O9 T2 (2026-09-08; CLOCK.md 12b): the (book, chapter, verse) an event's source opens with — the placement stamp compares
    it to the last marker's verse (the marker names the position it sits at)"""
    m = _VERSE.match(src or '')
    return (m.group(1), int(m.group(2)), int(m.group(3))) if m else None


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


class CursorReached(Exception):
    """THE LOOP step 4 THE CURSOR (2026-09-09; THE_LOOP.md 'Step 4 THE CURSOR — the design'): raised by submit() and marker() when a
    line names a verse AT OR AFTER World.stop_before — the tape replayed to a position in the text and stopped at its left edge"""


def _sealed(fn):
    """THE LOOP step 7 (a) WRITE AS YOU GO (2026-09-14; THE_LOOP.md "Step 7 ... part (a)", decision D14 THE SEAL): an entry point of
    the engine is a BLOCK — when the outermost call returns (depth 0; in a finally, so a refusal raised mid-block still seals the lines
    logged before it) the attached journal seals the log's new lines: on disk and in the index at once. A world with no journal
    (the exam worlds, D9) pays nothing. Nothing here reads or writes the world: the hook observes the log and decides nothing."""
    @functools.wraps(fn)
    def sealed(self, *a, **k):
        try:
            return fn(self, *a, **k)
        finally:
            j = getattr(self, 'journal', None)
            if j is not None and self._depth == 0:
                j.flush()
    return sealed


class World:
    def __init__(self, era, epoch=None, registry=None, installation=None):
        self.clock = Clock(era, epoch=epoch)
        self.entities = {}
        self.stop_before = None           # THE LOOP step 4: a verse key; a line at or after it raises CursorReached (the cursor's left edge)
        # THE LOOP step 3 INSTALLATION (2026-09-09): a world OPTS IN with `installation` (D1 — the sequence runner's four worlds;
        # the 38 exam worlds pass nothing: no field read, no line logged, no write); the fields per daemon, the setting, the counts
        self.installation = None          # {'setting', 'fields': {daemon: {given_at, installed_by}}, 'skipped', 'would_skip'}
        self._verse_reached = None        # THE VERSE REACHED: the canonical max over every marker's verse and every event's first cited verse
        # THE SEQUENTIAL RUN (2026-09-07): THE ONE WHO-IS-WHO AT THE ENGINE — a scene token resolves to the registry's
        # entity id (logic/corpus/entity_registry.yaml's members with units [step9-scenes]); the daemons keep their
        # names, the ledgers merge. A world with no map behaves as before.
        self._registry = dict(registry or {})
        self.laws = []        # the daemon registry
        self.timers = []      # (fire_day, effect_dict) — a timer with a `period` re-arms at its fire
        self.log = []
        self.journal = None      # THE LOOP step 7 (a) WRITE AS YOU GO (2026-09-14): the attached live sink (world_journal.attach), sealing the log's lines at the end of every block; None on every world that journals nothing
        self._entry_seq = 0      # THE LOOP step 1's amendment THE CLOSE LINE (2026-09-12): every ledger entry's own ordinal, stamped at write — the write line carries it, the close line names it
        # THE CLOCK SITTING (2026-09-07): the bound and the marker (CLOCK.md section 4)
        self._last_marker = 0        # the last forward marker's day — every later event's bound opens here
        self._open_bounds = []       # the bound lists still open, SHARED by the event, its effects, timers, fires
        self._dated = None           # a retrograde stretch's stated day (Pesachim 6b:7), until the clock moves
        self._placement = (None, None)   # O9 T2: the last non-proleptic marker's (class, first verse) — the placement stamp's source
        # D9-ii: every daemon's WATCH COVERAGE — events seen, events it fired on,
        # the kinds it fired on — printed by coverage(); the zero-report law's
        # instrument for the simulator (a daemon that never fires is visible)
        self.watch = collections.OrderedDict()
        self._depth = 0
        self._consuming = None
        # THE POPULATION TABLE (THE NUMBERS WALK 8b, 2026-09-11): the tables of the fifth registry, each a list of rows written by daemons
        # (World.row) — not the ledger: no op, no open, no close; a row moves no count of the RUN tuple and is the log's own class ROW
        self.tables = {t: [] for t in POP_SCHEMA}
        if installation is not None:
            self.install(installation)

    def entity(self, eid, kind='person'):
        eid = self._registry.get(eid, eid)
        if eid not in self.entities:
            self.entities[eid] = Entity(eid, kind)
        return self.entities[eid]

    # -- THE LOOP step 3: installation (2026-09-09; THE_LOOP.md "Step 3 INSTALLATION — the design", D1-D6) --
    def install(self, installation):
        """opt this world into installation. `installation` is a setting name ('boot' | 'from_event') or a dict {'setting': ...,
        'fields': {daemon: {'given_at', 'installed_by'}}}; True takes the fourth registry's running setting. Without fields the two
        fields are read for every daemon declared in daemon_dispositions.yaml; a daemon without both, or naming an act that is not
        an installing act, is refused at once (the daemon gate refuses the same before any sweep)."""
        if isinstance(installation, dict):
            setting, fields = installation.get('setting'), installation.get('fields')
        else:
            setting, fields = (None if installation is True else installation), None
        setting = setting or INSTALL_PARAMS['installation_setting']['value']
        if setting not in INSTALL_PARAMS['installation_setting']['settings']:
            raise SystemExit('INSTALLATION: setting %r is not a recorded setting of installation_setting (%s)'
                             % (setting, ', '.join(INSTALL_PARAMS['installation_setting']['settings'])))
        if fields is None:
            with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'daemon_dispositions.yaml'), encoding='utf-8') as f:
                decl = yaml.safe_load(f)['daemons']
            fields = {n: {k: d.get(k) for k in INSTALL_FIELDS} for n, d in decl.items()}
        for n, d in fields.items():
            missing = [k for k in INSTALL_FIELDS if not d.get(k)]
            if missing:
                raise SystemExit('INSTALLATION: daemon %s declares no %s — every daemon carries both fields (THE_LOOP.md step 3)' % (n, ' / '.join(missing)))
            if d['installed_by'] not in INSTALL_VALUES and d['installed_by'] not in INSTALLING_ACTS:
                raise SystemExit('INSTALLATION: daemon %s installed_by %r is neither boot, pending, nor an installing act of installation_parameters.yaml' % (n, d['installed_by']))
            if verse_key(d['given_at']) is None:
                raise SystemExit('INSTALLATION: daemon %s given_at %r is not a verse' % (n, d['given_at']))
        self.installation = {'setting': setting, 'fields': fields, 'skipped': 0, 'would_skip': 0}
        return self.installation

    def installation_report(self):
        """the setting; the registered daemons by value (boot / by an act / pending, the pending named); skipped and would-skip"""
        I = self.installation
        if I is None:
            return None
        names = [getattr(l, '__name__', repr(l)) for l in self.laws]
        by = collections.Counter(I['fields'][n]['installed_by'] for n in names if n in I['fields'])
        return {'setting': I['setting'], 'registered': len(names), 'boot': by.get('boot', 0),
                'by_act': sum(v for k, v in by.items() if k not in INSTALL_VALUES), 'by_value': dict(by),
                'pending': sorted(n for n in names if I['fields'].get(n, {}).get('installed_by') == 'pending'),
                'skipped': I['skipped'], 'would_skip': I['would_skip']}

    def _reach(self, src):
        k = verse_key(src)
        if k is not None and (self._verse_reached is None or k > self._verse_reached):
            self._verse_reached = k

    def not_in_force(self, name, event):
        """the question asked before a daemon is called: None when in force, else (why, needs) — not_given when the run's position
        in the text has not reached the law's given_at; not_in_force when the act's institution carries no in_force entry for that
        act AND no institution carries a rule_installed entry naming this daemon (installation BY A CASE EVENT, D5/D6). boot and
        pending are always in force (pending behaves as boot and is counted as debt, D2)."""
        f = self.installation['fields'].get(name)
        if f is None:
            raise SystemExit('INSTALLATION: daemon %s is registered on an installation world but declares no fields' % name)
        by = f['installed_by']
        if by in INSTALL_VALUES:
            return None
        g = verse_key(f['given_at'])
        if self._verse_reached is None or g > self._verse_reached:
            return ('not_given', f['given_at'])
        row = INSTALLING_ACTS[by]
        ent = self.entities.get(self._registry.get(row['entity'], row['entity']))
        if ent is not None and any(e['effect'] == 'in_force' and e.get('value') == by for e in ent.ledger):
            return None
        for r in INSTALLING_ACTS.values():
            ent = self.entities.get(self._registry.get(r['entity'], r['entity']))
            if ent is not None and any(e['effect'] == 'rule_installed' and e.get('value') == name for e in ent.ledger):
                return None
        return ('not_in_force', by)

    def skips(self):
        """every daemon's skipped count under the from_event setting (zero everywhere under boot)"""
        return collections.OrderedDict((n, w.get('skipped', 0)) for n, w in self.watch.items())

    # -- construct 3: dispatch — every law fires, unasked -------------
    @_sealed
    def submit(self, event):
        EV.validate([event['kind']])                  # the tape carries registered types only
        if self.stop_before is not None:              # THE LOOP step 4: the cursor — a line at or after the verse is the future
            k = verse_key(event.get('case_source'))
            if k is not None and k >= self.stop_before:
                raise CursorReached(event.get('case_source'))
        if self._depth >= DEPTH_BOUND:
            raise SystemExit('THE FENCE: World.submit re-entered at depth %d (bound %d) while %s was consuming an event — '
                             'a daemon emitted an event %r; daemons write the ledger, cascades run through ledger state'
                             % (self._depth + 1, DEPTH_BOUND, self._consuming, event.get('kind')))
        self._depth += 1
        try:
            if self._dated is not None:                      # inside a retrograde stretch: the text's own date, no bound
                event['dated'] = self._dated
                event.setdefault('day', self._dated)         # THE DATED DAY IS THE EVENT'S DAY (SEQUENTIAL_RUN.md section 2): a daemon that reads the event's day reads the text's date
                event['placement'] = self._placement[0] or 'text_constrained'    # O9 T2: the stretch is placed as one, by its marker's class
            else:                                            # between markers: the bound [the last marker, open]
                b = [self._last_marker, None]
                event['bound'] = b
                self._open_bounds.append(b)
                # O9 T2 (CLOCK.md 12b): THE PLACEMENT CLASS beside the bound — the marker's class on the event at the marker's own
                # verse; every other event between markers is page_order (the counter's: an unlabeled prior no longer unlabeled)
                cls, at = self._placement
                event['placement'] = cls if (cls and at is not None and first_verse(event.get('case_source')) == at) else 'page_order'
            self._reach(event.get('case_source'))     # THE LOOP step 3: the verse reached — the given_at check's position in the text
            event['fired_by'] = []                     # THE LOOP step 3: THE CONSUMERS STAMPED — the journal's EVENT line names the daemons that fired on it
            self.log.append(('EVENT', self.clock.day, event))
            fired = 0
            for law in self.laws:
                name = getattr(law, '__name__', repr(law))
                w = self.watch.setdefault(name, {'seen': 0, 'fired': 0, 'kinds': set(), 'skipped': 0})
                if self.installation is not None:      # THE LOOP step 3 INSTALLATION (2026-09-09): THE DISPATCH GATE — at the call, never at registration
                    why = self.not_in_force(name, event)
                    if why is not None:
                        if self.installation['setting'] == 'from_event':
                            self.log.append(('SKIP', self.clock.day, {'daemon': name, 'kind': event['kind'], 'subject': event.get('subject'),
                                                                      'case_source': event.get('case_source'), 'why': why[0], 'needs': why[1]}))
                            w['skipped'] += 1
                            self.installation['skipped'] += 1
                            continue
                        self.installation['would_skip'] += 1    # the boot setting (D2): nothing skipped, nothing logged — counted for the deferred decision
                w['seen'] += 1
                self._consuming = name
                effs = law(event, self) or []
                self._consuming = None
                if effs:
                    w['fired'] += 1
                    w['kinds'].add(event['kind'])
                    event['fired_by'].append(name)
                for eff in effs:
                    fired += 1
                    for key in ('bound', 'dated'):           # the engine copies the event's bound/date onto its effects
                        if key in event:
                            eff.setdefault(key, event[key])
                    eff.setdefault('written_by', name)       # THE LOOP step 1 (2026-09-09): the writing daemon stamped — the journal's "who wrote this" (prov.unit)
                    self._write(eff)
            return fired
        finally:
            self._depth -= 1

    def coverage(self):
        """every daemon's watch coverage: {daemon: (events seen, events fired on, kinds fired on)}"""
        return collections.OrderedDict((n, (w['seen'], w['fired'], sorted(w['kinds']))) for n, w in self.watch.items())

    def print_coverage(self):
        for n, (seen, fired, kinds) in self.coverage().items():
            sk = self.watch[n].get('skipped', 0)
            print('  WATCH %-22s seen %3d  fired %3d  on: %s%s' % (n, seen, fired, ', '.join(kinds) or '(never fired)', ('  skipped %d' % sk) if sk else ''))

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
        entry['seq'] = self._entry_seq                 # THE CLOSE LINE (2026-09-12): the entry's run-local name (the world's write counter, retro-writes and fires included)
        self._entry_seq += 1
        ent.ledger.append(entry)
        if op == 'status':
            ent.status[eff['effect']] = eff.get('value', True)
        # THE LOOP step 1's amendment THE CLOSE LINE (2026-09-12; THE_LOOP.md): the log holds a SNAPSHOT of the entry at write time — a later
        # close writes into the ledger entry, never into this line (the shallow copy keeps the event's shared bound list, as step 1 designed)
        if eff.get('due') is not None and eff['due'] < now:   # a due already past (a retrograde stretch): written now, named
            self.log.append(('RETRO-WRITE', now, dict(entry)))
        else:
            self.log.append(('WRITE', now, dict(entry)))

    @_sealed
    def close(self, eid, effect, note, value=None):
        """an entry closes when the text records the closing act; with `value` the entry whose value matches closes
        (O8 S1, 2026-09-08: the frogs' removal closes the FROGS' plague entry, not the first open plague — probe 18)"""
        ent = self.entity(eid)
        for e in ent.ledger:
            if e['effect'] == effect and e.get('open') and (value is None or e.get('value') == value):
                e['open'] = False
                e['closed_by'] = note
                e['closed_day'] = self.clock.day      # THE LOOP step 2's remainder (2026-09-09): the day it closed, beside the closer — the ledger view's day_closed
                # THE LOOP step 1's amendment THE CLOSE LINE (2026-09-12; THE_LOOP.md; the owner's word on the cursor's audit): the close is a LINE OF
                # ITS OWN — the tenth log class — naming the entry by its seq; the ledger entry above keeps the fields the daemons and checkpoints read
                self.log.append(('CLOSE', self.clock.day, {'subject': ent.eid, 'effect': effect, 'entry_seq': e.get('seq'), 'value': e.get('value'),
                                                           'note': note, 'written_day': e.get('day'), 'written_by': e.get('written_by'),
                                                           'closed_by_daemon': self._consuming, 'case_source': e.get('case_source')}))
                return True
        return False

    # -- THE POPULATION TABLE (THE NUMBERS WALK 8b, 2026-09-11; NUMBERS_WALK.md "Sitting 8b"): the rows and the query --------------
    @_sealed
    def row(self, table, row):
        """a daemon writes a ROW of a table of the fifth registry (population_schema.yaml) while consuming an event — NEVER BY HAND:
        a call with no daemon consuming (self._consuming unset) is refused. The row is validated against the schema (a known table; a
        known grain; every required column present; no unknown column), stamped written_by / day / year / table, appended to the table
        and logged as the class ROW (journaled as run.row). A row is not a ledger entry — no op, no open, no close, no counterparty — and
        moves no count of the RUN tuple; the daemons read the table back through population(). Returns the stamped row."""
        if self._consuming is None:
            raise SystemExit('THE POPULATION TABLE: a row of %r is written by a daemon consuming an event, never by hand (population_schema.yaml law 1)' % table)
        if table not in POP_SCHEMA:
            raise SystemExit('THE POPULATION TABLE: %r is not a table of population_schema.yaml (the tables: %s)' % (table, ', '.join(POP_SCHEMA)))
        sch = POP_SCHEMA[table]
        grain = row.get('grain')
        if grain not in sch['grains']:
            raise SystemExit('THE POPULATION TABLE: grain %r is not a grain of %s (the grains: %s)' % (grain, table, ', '.join(sch['grains'])))
        g = sch['grains'][grain]
        missing = [c for c in g['required'] if c not in row]
        if missing:
            raise SystemExit('THE POPULATION TABLE: a %s row of %s lacks its required column(s) %s' % (grain, table, ', '.join(missing)))
        unknown = [c for c in row if c not in g['required'] and c not in g.get('optional', ()) and c not in POP_STAMPS]
        if unknown:
            raise SystemExit('THE POPULATION TABLE: a %s row of %s carries unknown column(s) %s — the schema is the fifth registry, amended before use' % (grain, table, ', '.join(unknown)))
        entry = dict(row, written_by=self._consuming, day=self.clock.day, year=self.clock.year, table=table)
        self.tables[table].append(entry)
        self.log.append(('ROW', self.clock.day, entry))
        return entry

    def population(self, table='population', **where):
        """the rows of a table matching every given column by equality (a value of None matches a None column) — the daemons' instrument
        (the census daemon reads its own chapter-1 rows to declare the deltas at chapter 26); a missing column never matches"""
        rows = self.tables.get(table, [])
        return [r for r in rows if all(k in r and r[k] == v for k, v in where.items())]

    @_sealed
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

    @_sealed
    def marker(self, verse, day, value=None, era=None, new_year_month=None, proleptic=False, placement='text_constrained'):
        """THE MARKER (CLOCK.md section 4): the text's own date stamp sets the clock. A marker at or after the
        counter walks advance(day) and CLOSES every open bound at it; a marker EARLIER than the counter is
        RETROGRADE (Pesachim 6b:7 — 'there is no earlier and later in the Torah'; Num 9:1 after 1:1): logged,
        the counter unmoved, the following events dated by the text until the clock next moves.
        THE SEQUENTIAL RUN (SEQUENTIAL_RUN.md section 2): `era` names an era whose EPOCH this marker sets at `day`
        (Exod 12:2 sets the exodus era; a begetting sets life:<entity>); `proleptic` is the third class — a paragraph's
        CLOSING TOTAL ('all the days of X were N years, and he died'), logged at its computed day with the counter
        unmoved and no dated stretch opened: the text's summary of a life, not a clock stamp for the next verse.
        O9 T2 (2026-09-08; CLOCK.md 12b): `placement` is the marker's CLASS — text_constrained (the ink's own stamp or
        arithmetic, the default) or reading_placed (a shelf reading fixing a date where the ink is silent at that grain);
        submit() stamps it on the event at the marker's verse (the marker names the position it sits at) and on every event
        of a retrograde stretch; a proleptic marker carries none."""
        if self.stop_before is not None and verse_key(verse) is not None and verse_key(verse) >= self.stop_before:
            # THE NUMBERS WALK 1b (2026-09-09; NUMBERS_WALK.md "Sitting 1b" as built): a FORWARD marker at the cursor CLOSES the bounds behind
            # it as the full run would — the right edge is its own day, known here — before the world stops; else the replayed prefix
            # differs from the base by every event of the last open bound (found when 1:1's bound, closed by 27:1 in the run, stayed open
            # at the 27:1 cursor: the bamidbar lines refused). A retrograde or proleptic marker closes nothing in the run either.
            if not proleptic and day >= self.clock.day:
                for b in self._open_bounds:
                    b[1] = day
                self._open_bounds = []
            raise CursorReached(verse)                       # THE LOOP step 4: a marker AT the cursor verse belongs to its future
        if era is not None:
            self.clock.set_era(era, day, new_year_month)
        self._reach(verse)                                   # THE LOOP step 3: a marker names the position in the text it sits at
        if placement not in ('text_constrained', 'reading_placed'):
            raise SystemExit('MARKER %s: placement %r is not text_constrained or reading_placed' % (verse, placement))
        if proleptic:
            self.log.append(('MARKER', self.clock.day, {'verse': verse, 'value': value, 'retrograde': False, 'proleptic': True, 'stated': day}))
            return day
        self._placement = (placement, first_verse(verse))
        if day < self.clock.day:
            self.log.append(('MARKER', self.clock.day, {'verse': verse, 'value': value, 'retrograde': True, 'stated': day, 'placement': placement}))
            self._dated = day
            return day
        self._dated = None
        self.advance(day)
        for b in self._open_bounds:
            b[1] = day
        self._open_bounds = []
        self._last_marker = day
        self.log.append(('MARKER', day, {'verse': verse, 'value': value, 'retrograde': False, 'placement': placement}))
        return day

    # -- construct 4: time advances; due timers fire; a period re-arms --
    @_sealed
    def advance(self, to_day):
        if to_day > self.clock.day:
            self._dated = None                               # the clock moves: the retrograde stretch is over
        while self.clock.day < to_day:
            self.clock.day += 1
            now = self.clock.day
            due = [t for t in self.timers if t[0] == now]
            self.timers = [t for t in self.timers if t[0] != now]
            # O9 OPEN-5 (CLOCK.md 12e): the fires within ONE day's walk are ORDERED by the timer's opt-in `boundary` — the calendar's
            # (absent: the evening, Gen 1:5 — Chullin 83a:15) first, consecrated things' ('morning' — Chullin 83a:16, the night follows
            # the day: the eating windows' "until morning") after; a stable sort keeps the set order within a class; the due never moves
            due.sort(key=lambda t: 0 if t[1].get('boundary', 'evening') == 'evening' else 1)
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


# THE TENT sitting 4 (2026-09-09): THE INSTANCE'S VERDICTS from the ink's own word, per case — the entry's shape beyond effect/subject/value
# (the counterparty, the due, the source), built at the write; keyed by the installed law where the tape's line names no verdict (the first seat)
CASE_VERDICTS = {
    'second_passover_due': lambda world: {'counterparty': 'HEAVEN', 'due': due_of_passover_sheni(world),
                                          'source_law': 'THE TENT DAEMON — the instance\'s verdict from the ink\'s own word [INK Num 9:10-11: he shall keep a '
                                          'Passover to the LORD in the second month] — written only where the code had not decided (the from_event setting)'},
    'holding_owed': lambda world: {'counterparty': 'the-court', 'due': None,
                                   'source_law': 'THE TENT DAEMON — the instance\'s verdict from the ink\'s own word [INK Num 27:7: given shall be given to them a '
                                   'holding of inheritance among their father\'s brothers; the giving Josh 17:4] — written only where the code had not decided'},
    'marries_within_tribe': lambda world: {'counterparty': None, 'due': None,
                                           'source_law': 'THE TENT DAEMON — the second output\'s verdict from the ink\'s own word [INK Num 36:6: to whom is good in '
                                           'their eyes they shall be wives, only to the family of the tribe of their father] — written only where the code had not decided'},
}
CASE_VERDICTS_BY_LAW = {'law_pesach_sheni': 'second_passover_due'}   # the first seat's tape line carries no verdict field: keyed by the installed law


def law_tent(event, world):
    """THE TENT DAEMON (THE LOOP step 3 INSTALLATION, 2026-09-09; decision D4; THE_LOOP.md "Step 3 INSTALLATION — the design") —
    the library's sixth, registered FIRST by the sequence runner so that an installing act switches on its laws INSIDE ITS OWN
    DISPATCH (Lev 25:2: the entry itself starts the count). It consumes the six INSTITUTION-ERECTING ACTS of the fourth registry,
    installation_parameters.yaml, and writes `in_force` on the act's institution — the value the act itself, matched by
    World.not_in_force against each daemon's installed_by. At Numbers' opening block it gains the custody branch (the ink's own
    custody act, "and they placed him in the guard" → in_custody on the person, declaration_owed on the court's docket, with the
    daemons that already wrote on the case's verse read off the ledger) and the output branch (the verse "by the mouth of the
    LORD" → rule_installed on the institution, the docket's debit closed), on the kinds registered with their witnesses then.
    A literal branch per kind — the daemon gate's parser reads branches; the entity comes from the registry's row."""
    k = event['kind']
    if k == 'judges_appointed':
        return [{'effect': 'in_force', 'subject': INSTALLING_ACTS['judges_appointed']['entity'], 'counterparty': None, 'amount': None, 'due': None,
                 'value': 'judges_appointed', 'source_law': 'THE TENT DAEMON — the_court installed by judges_appointed [INK Exod 18:25-26: '
                 'and they judged the people at all times]', 'case_source': event['case_source']}]
    if k == 'covenant_blood_thrown':
        return [{'effect': 'in_force', 'subject': INSTALLING_ACTS['covenant_blood_thrown']['entity'], 'counterparty': None, 'amount': None, 'due': None,
                 'value': 'covenant_blood_thrown', 'source_law': 'THE TENT DAEMON — the_covenant_at_sinai installed by covenant_blood_thrown '
                 '[INK Exod 24:8: the blood of the covenant which the LORD has cut with you upon all these words]', 'case_source': event['case_source']}]
    if k == 'erected':
        return [{'effect': 'in_force', 'subject': INSTALLING_ACTS['erected']['entity'], 'counterparty': None, 'amount': None, 'due': None,
                 'value': 'erected', 'source_law': 'THE TENT DAEMON — the_tent_of_meeting installed by erected [INK Exod 40:17: the tabernacle '
                 'was erected]', 'case_source': event['case_source']}]
    if k == 'called_from_the_tent':
        return [{'effect': 'in_force', 'subject': INSTALLING_ACTS['called_from_the_tent']['entity'], 'counterparty': None, 'amount': None, 'due': None,
                 'value': 'called_from_the_tent', 'source_law': 'THE TENT DAEMON — the_tent_of_meeting installed a second time by called_from_the_tent '
                 '[INK Lev 1:1: the LORD spoke to him from the tent of meeting — the detail pass opens, Chagigah 6b:1]', 'case_source': event['case_source']}]
    if k == 'milluim_blood_sprinkled':
        return [{'effect': 'in_force', 'subject': INSTALLING_ACTS['milluim_blood_sprinkled']['entity'], 'counterparty': None, 'amount': None, 'due': None,
                 'value': 'milluim_blood_sprinkled', 'source_law': 'THE TENT DAEMON — the_priesthood installed by milluim_blood_sprinkled [INK Lev 8:30; '
                 'Sifra, Tzav, Mekhilta DeMiluim I 34: consummated only at the blood sprinkling]', 'case_source': event['case_source']}]
    if k == 'entered_the_land':
        return [{'effect': 'in_force', 'subject': INSTALLING_ACTS['entered_the_land']['entity'], 'counterparty': None, 'amount': None, 'due': None,
                 'value': 'entered_the_land', 'source_law': 'THE TENT DAEMON — the_land_of_canaan installed by entered_the_land [INK Lev 25:2: when you '
                 'come into the land which I give you; Exod 23:23]', 'case_source': event['case_source']}]
    # ---- THE TENT's four cases (World/step9/THE_TENT.md; sitting 1 THE BLASPHEMER, 2026-09-09): the halt, the output, the execution ----
    if k == 'placed_in_custody':
        # THE HALT (Lev 24:12; Num 15:34): the person in the guard, the docket's declaration owed — OPEN until the output closes it — and,
        # read off the person's LEDGER, the daemons that already wrote on the case's verse (under the boot setting the code decided before
        # the halt; under from_event none had): the installation setting's own evidence, carried on the docket entry as covered_by
        person = event.get('person', event['subject'])
        ent = world.entities.get(world._registry.get(person, person))
        fv = first_verse(event.get('case_of')) if event.get('case_of') else None
        covered = sorted({e.get('written_by') for e in (ent.ledger if ent is not None else [])
                          if fv is not None and first_verse(e.get('case_source')) == fv and e.get('written_by') and e.get('written_by') != 'law_tent'})
        why = event.get('uncertainty', 'liable_at_all')
        return [{'effect': 'in_custody', 'subject': person, 'counterparty': None, 'amount': None, 'due': None, 'value': why,
                 'source_law': 'THE TENT DAEMON — the halt [INK Lev 24:12: and they placed him in the guard, to be declared to them by the mouth of '
                 'the LORD; Num 15:34; Sanhedrin 78b:4-7 the incarceration derived, the two uncertainties told apart]', 'case_source': event['case_source']},
                {'effect': 'declaration_owed', 'subject': 'the-court', 'counterparty': person, 'amount': None, 'due': None, 'value': why, 'covered_by': covered,
                 'source_law': 'THE TENT DAEMON — the docket [INK Lev 24:12 "to be declared to them"; Num 15:34 "it had not been declared"; covered_by = '
                 'the daemons that already wrote on the case verse — the installation setting\'s evidence]', 'case_source': event['case_source']}]
    if k == 'sentence_declared':
        # THE OUTPUT (Lev 24:13-14): the generations' rule installed on the tent in the case's name — under the parameter row case_output's
        # running setting only (the first tanna, Sanhedrin 80b:5; Rabbi Yehuda's provisional edict writes no rule) — the docket's debit
        # closed, and the instance's verdict from the ink's own word where the code has not already decided (the from_event setting)
        person = event.get('person', event['subject'])
        installs = event.get('installs')
        out = []
        if installs and INSTALL_PARAMS['case_output']['value'] == 'rule_for_the_generations':
            out.append({'effect': 'rule_installed', 'subject': INSTALLING_ACTS['sentence_declared']['entity'], 'counterparty': None, 'amount': None,
                        'due': None, 'value': installs, 'source_law': 'THE TENT DAEMON — the generations\' rule [INK Lev 24:15-22: the statute in the '
                        'case\'s name (Sanhedrin 8a:5; Sifrei Bamidbar 80:1, 114:1); the row case_output = rule_for_the_generations, the first tanna '
                        'at Sanhedrin 80b:5]', 'case_source': event['case_source']})
        world.close('the-court', 'declaration_owed', event['case_source'])
        ent = world.entities.get(world._registry.get(person, person))
        if event.get('sentence') == 'stoning' and not any(e['effect'] == 'stoned' for e in (ent.ledger if ent is not None else [])):
            out.append({'effect': 'stoned', 'subject': person, 'counterparty': None, 'amount': None, 'due': None, 'value': 'by the mouth of the LORD',
                        'source_law': 'THE TENT DAEMON — the instance\'s verdict from the ink\'s own word [INK Lev 24:14: let all the congregation stone '
                        'him] — written only where the code had not decided (Rabbi Yehuda\'s edict reading; the from_event setting)', 'case_source': event['case_source']})
        return out
    if k == 'stoned_as_commanded':
        # THE EXECUTION (Lev 24:23): the history's own act performs the sentence and ends the guard — the two BODY entries on the person
        # (stoned, in_custody) are CLOSED by the deed's verse (THE CLOSE PAIRING, CLOCK.md section 3); nothing new is written
        person = event.get('person', event['subject'])
        world.close(person, 'stoned', event['case_source'])
        world.close(person, 'in_custody', event['case_source'])
        world.close(person, 'put_to_death', event['case_source'])   # THE TENT sitting 3 (2026-09-09): the wood-gatherer's DEATH SENTENCE (law_sabbath's body entry at 15:32-33) performed by "and he died" (15:36) — found OPEN by the ask-tool after the first run; the blasphemer carries no such entry (close returns False)
        return []
    # ---- THE TENT sitting 2 (THE_TENT.md section 2; 2026-09-09): a STANDING case — the unclean men at the Passover (Num 9:6-14) ----
    if k == 'stood_to_hear':
        # THE HALT of a standing case (Num 9:8 "stand, and I will hear"; Onkelos: wait): no guard — the persons WAIT for the word (a body
        # entry, open until the output closes it) and the docket's declaration is owed; covered_by reads the persons' LEDGER and the PENDING
        # TIMERS (under boot the case law decided at 9:6-7 with a due to the second month — a timer, not a ledger line)
        persons = event.get('persons') or [event.get('person', event['subject'])]
        fv = first_verse(event.get('case_of')) if event.get('case_of') else None
        covered = set()
        for person in persons:
            ent = world.entities.get(world._registry.get(person, person))
            for e in (ent.ledger if ent is not None else []) + [t for _, t in world.timers if t.get('subject') == person]:
                if fv is not None and first_verse(e.get('case_source')) == fv and e.get('written_by') and e.get('written_by') != 'law_tent':
                    covered.add(e['written_by'])
        why = event.get('uncertainty', 'the_mode')
        out = [{'effect': 'waits_for_the_word', 'subject': p, 'counterparty': None, 'amount': None, 'due': None, 'value': why,
                'source_law': 'THE TENT DAEMON — the halt of a standing case [INK Num 9:8: stand, and I will hear what the LORD will command '
                'concerning you; Onkelos: wait; Sifrei Bamidbar 68:1: I have not heard — R. Chidka: the sprinkling was the question]',
                'case_source': event['case_source']} for p in persons]
        out.append({'effect': 'declaration_owed', 'subject': 'the-court', 'counterparty': persons[0] if len(persons) == 1 else persons, 'amount': None,
                    'due': None, 'value': why, 'covered_by': sorted(covered),
                    'source_law': 'THE TENT DAEMON — the docket [INK Num 9:8; covered_by = the daemons that already wrote on the case verse, the ledger '
                    'and the pending timers — the installation setting\'s evidence]', 'case_source': event['case_source']})
        return out
    if k == 'statute_declared':
        # THE OUTPUT, second form (Num 9:9-14): the statute itself — the generations' rule installed in the case's name (under case_output's
        # running setting), the docket's debit and the persons' wait CLOSED by the output's verse (THE CLOSE PAIRING at the design), and the
        # instance's verdict from the ink's own word — the second Passover's due — only where neither the ledger nor the pending timers carry it
        persons = event.get('persons') or [event.get('person', event['subject'])]
        installs = event.get('installs')
        out = []
        if installs and INSTALL_PARAMS['case_output']['value'] == 'rule_for_the_generations':
            out.append({'effect': 'rule_installed', 'subject': INSTALLING_ACTS['statute_declared']['entity'], 'counterparty': None, 'amount': None,
                        'due': None, 'value': installs, 'source_law': 'THE TENT DAEMON — the generations\' rule [INK Num 9:10-14: the statute in the '
                        'case\'s name, "of you or of your generations", "one statute shall be for you" (Sifrei Bamidbar 69:1: the rule wider than the '
                        'question; 114:1); the row case_output = rule_for_the_generations, the first tanna at Sanhedrin 80b:5]', 'case_source': event['case_source']})
        world.close('the-court', 'declaration_owed', event['case_source'])
        # THE TENT sitting 4 (2026-09-09): THE VERDICT TABLE — the instance's verdict from the ink's own word, keyed by the installed law (the
        # first seat's line names no verdict field: its row is the old path, byte-identical); written only where neither the ledger nor the
        # pending timers carry it (under boot the case law decided at the plea)
        verdict = event.get('verdict') or CASE_VERDICTS_BY_LAW.get(installs)
        for person in persons:
            world.close(person, 'waits_for_the_word', event['case_source'])
            ent = world.entities.get(world._registry.get(person, person))
            decided = any(e['effect'] == verdict for e in (ent.ledger if ent is not None else [])) or \
                any(t.get('effect') == verdict and t.get('subject') == person for _, t in world.timers)
            if verdict == 'second_passover_due' and not decided:
                sh = CASE_VERDICTS['second_passover_due'](world)
                out.append({'effect': 'second_passover_due', 'subject': person, 'counterparty': sh['counterparty'], 'amount': None, 'due': sh['due'],
                            'value': 'by the mouth of the LORD', 'source_law': sh['source_law'], 'case_source': event['case_source']})
            elif verdict == 'holding_owed' and not decided:
                sh = CASE_VERDICTS['holding_owed'](world)
                out.append({'effect': 'holding_owed', 'subject': person, 'counterparty': sh['counterparty'], 'amount': None, 'due': sh['due'],
                            'value': 'by the mouth of the LORD', 'source_law': sh['source_law'], 'case_source': event['case_source']})
        return out
    # ---- THE TENT sitting 4 (THE_TENT.md section 4; 2026-09-09): the daughters' halt — THE THIRD FORM — and the second output, RELAYED ----
    if k == 'judgment_brought_near':
        # THE HALT'S THIRD FORM (Num 27:5 "and Moses brought their judgment near before the LORD"): no guard, no wait — nothing in the ink
        # holds the persons, so NO body entry is written; the docket's declaration alone, covered_by read off the persons' ledger and the
        # pending timers (under boot the case law decided at the plea — holding_owed), the uncertainty THE SCOPE (Sifrei 133:4; Bava Batra 119a:6)
        persons = event.get('persons') or [event.get('person', event['subject'])]
        fv = first_verse(event.get('case_of')) if event.get('case_of') else None
        covered = set()
        for person in persons:
            ent = world.entities.get(world._registry.get(person, person))
            for e in (ent.ledger if ent is not None else []) + [t for _, t in world.timers if t.get('subject') == person]:
                if fv is not None and first_verse(e.get('case_source')) == fv and e.get('written_by') and e.get('written_by') != 'law_tent':
                    covered.add(e['written_by'])
        why = event.get('uncertainty', 'the_scope')
        return [{'effect': 'declaration_owed', 'subject': 'the-court', 'counterparty': persons[0] if len(persons) == 1 else persons, 'amount': None,
                 'due': None, 'value': why, 'covered_by': sorted(covered),
                 'source_law': 'THE TENT DAEMON — the halt\'s third form [INK Num 27:5: and Moses brought their judgment near before the LORD — the '
                 'offerings\' verb, no guard and no wait; Sifrei Bamidbar 133:4 / Bava Batra 119a:6: Moses knew daughters inherit, the question the FIT '
                 'against the HELD; Sanhedrin 8a:4: "I will hear it"; covered_by = the daemons that already wrote on the case verse — the installation '
                 'setting\'s evidence]', 'case_source': event['case_source']}]
    if k == 'command_relayed':
        # THE SECOND OUTPUT ON THE SAME CASE (Num 36:5-9 "and Moses commanded the children of Israel by the mouth of the LORD, saying"): relayed in
        # Moses' mouth — no divine frame; installs THE CELL law_zelophehad:tribe_transfer (a rule inside a case-born law: the statute amended with a
        # reach — "this is the thing", Bava Batra 120a:10); no docket was owed (the tribes' plea did not halt); the verdict only where the code had not
        persons = event.get('persons') or [event.get('person', event['subject'])]
        installs = event.get('installs')
        out = []
        if installs and INSTALL_PARAMS['case_output']['value'] == 'rule_for_the_generations':
            out.append({'effect': 'rule_installed', 'subject': INSTALLING_ACTS['command_relayed']['entity'], 'counterparty': None, 'amount': None,
                        'due': None, 'value': installs, 'source_law': 'THE TENT DAEMON — the second output\'s rule [INK Num 36:6-9: this is the thing '
                        'that the LORD commanded... an inheritance shall not go around from tribe to tribe; Bava Batra 120a:10 (Rava: this generation), '
                        '121a:7 (the fifteenth of Av: lapsed); the row case_output = rule_for_the_generations]', 'case_source': event['case_source']})
        verdict = event.get('verdict')
        for person in persons:
            ent = world.entities.get(world._registry.get(person, person))
            decided = any(e['effect'] == verdict for e in (ent.ledger if ent is not None else []))
            if verdict == 'marries_within_tribe' and not decided:
                sh = CASE_VERDICTS['marries_within_tribe'](world)
                out.append({'effect': 'marries_within_tribe', 'subject': person, 'counterparty': sh['counterparty'], 'amount': None, 'due': sh['due'],
                            'value': 'by the mouth of the LORD', 'source_law': sh['source_law'], 'case_source': event['case_source']})
        return out
    return []


def due_of_passover_sheni(world):
    """THE TENT sitting 2 (2026-09-09): the fourteenth of the second month through the Calendar — the row passover_sheni (Num 9:11), never a
    literal. The exodus ERA's date when the world carries it (the sequence world runs on the creation epoch and dates the exodus era from
    Exod 12:2's marker; an exam world declares epoch='exodus'); else the base calendar's festival key (a probe world)."""
    ex = world.clock.eras.get('exodus')
    row = CAL_PARAMS['festival_dates']['value']['passover_sheni']
    if ex is not None:
        y = ex.year(world.clock.day)
        d = ex.day_of(y, int(row['month']), int(row['day']))
        return d if d > world.clock.day else ex.day_of(y + 1, int(row['month']), int(row['day']))
    return world.clock.calendar.next(world.clock.day, 'passover_sheni')


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
