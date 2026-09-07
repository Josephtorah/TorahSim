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

import collections
import effects_layer as FX
import events_layer as EV      # THE EVENT-TYPE REGISTRY (D9-i): an unregistered kind refuses the tape

# THE FENCE'S DEPTH BOUND (D9-ii, 2026-09-07): a daemon CONSUMES events and WRITES
# the ledger; it never emits an event. Cascades run through LEDGER STATE (one
# daemon's write satisfies another's condition on a later event), never through
# a daemon submitting. So no event is ever submitted while another is being
# consumed: the cascade depth bound is 1, and a re-entry is a daemon emitting
# an event — reported loudly, naming the daemon, never truncated silently.
DEPTH_BOUND = 1


# ---- construct 1: the clock -----------------------------------------
class Clock:
    def __init__(self, era, year=0):
        self.era, self.year = era, year


# ---- construct 2: entities with mutable ledgers ---------------------
class Entity:
    def __init__(self, eid, kind):
        self.eid, self.kind = eid, kind
        self.status = {}      # persistent flags (slave, forewarned...)
        self.ledger = []      # entries written by verdicts

    def open_entries(self):
        return [e for e in self.ledger if e.get('open')]


class World:
    def __init__(self, era):
        self.clock = Clock(era)
        self.entities = {}
        self.laws = []        # the daemon registry
        self.timers = []      # (fire_year, effect_dict)
        self.log = []
        # D9-ii: every daemon's WATCH COVERAGE — events seen, events it fired on,
        # the kinds it fired on — printed by coverage(); the zero-report law's
        # instrument for the simulator (a daemon that never fires is visible)
        self.watch = collections.OrderedDict()
        self._depth = 0
        self._consuming = None

    def entity(self, eid, kind='person'):
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
            self.log.append(('EVENT', self.clock.year, event))
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
        if eff.get('due') is not None and eff['due'] > self.clock.year:
            self.timers.append((eff['due'], eff))     # construct 4
            self.log.append(('TIMER-SET', self.clock.year, eff))
            return
        ent = self.entity(eff['subject'])
        op = FX.REGISTRY[eff['effect']]['ledger_op']
        entry = dict(eff, op=op, year=self.clock.year,
                     open=(op in ('debit', 'heaven', 'body')))
        ent.ledger.append(entry)
        if op == 'status':
            ent.status[eff['effect']] = eff.get('value', True)
        self.log.append(('WRITE', self.clock.year, entry))

    def close(self, eid, effect, note):
        """an entry closes when the text records the closing act"""
        for e in self.entity(eid).ledger:
            if e['effect'] == effect and e.get('open'):
                e['open'] = False
                e['closed_by'] = note
                return True
        return False

    def cancel_timers(self, subject, effect, note):
        """a later TEXT event voids a pending timer (the pierced slave's
        'forever' voids his six-year exit — Exod 21:5-6): the interface
        gap the skeleton's first spin exposed"""
        kept, cut = [], 0
        for yr, eff in self.timers:
            if eff['subject'] == subject and eff['effect'] == effect:
                cut += 1
                self.log.append(('TIMER-CANCEL', self.clock.year,
                                 dict(eff, cancelled_by=note)))
            else:
                kept.append((yr, eff))
        self.timers = kept
        return cut

    # -- construct 4: time advances; due timers fire -------------------
    def advance(self, to_year):
        while self.clock.year < to_year:
            self.clock.year += 1
            due = [t for t in self.timers if t[0] == self.clock.year]
            self.timers = [t for t in self.timers if t[0] != self.clock.year]
            for _, eff in due:
                eff = dict(eff, due=None)
                self.log.append(('TIMER-FIRE', self.clock.year, eff))
                self._write(eff)

    # -- construct 5: the diff engine ----------------------------------
    def checkpoint(self, name, declared, computed):
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
    """Exod 21:2-6 (cold_run_mishpatim.py F1). The term clock."""
    if event['kind'] == 'acquire_hebrew_slave':
        s = event['slave']
        world.entity(s).status['hebrew_slave'] = True
        return [
            {'effect': 'term_clock', 'subject': s,
             'counterparty': event['master'], 'amount': 6,
             'due': None, 'source_law': 'F1 slave-release [INK 21:2]',
             'case_source': event['case_source']},
            {'effect': 'goes_free', 'subject': s, 'counterparty': None,
             'amount': None, 'due': world.clock.year + 6,
             'source_law': 'F1 FREE-YEAR-7 [INK 21:2: six + seventh + free]',
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
             'amount': None, 'due': event['jubilee_year'],
             'source_law': 'F1 FREE-AT-JUBILEE [IMPORT Lev 25; Kiddushin '
                           '15a:19: written even for the pierced "forever"]',
             'case_source': event['case_source']},
        ]
    if event['kind'] == 'jubilee_proclaimed':
        # the institutional flag flips on a text event, era-wide
        out = []
        for ent in world.entities.values():
            if ent.status.get('hebrew_slave'):
                out.append(
                    {'effect': 'goes_free', 'subject': ent.eid,
                     'counterparty': None, 'amount': None, 'due': None,
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
             'amount': None, 'due': world.clock.year + 7,
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
    w = World(era='test-scenes (recorded cases)')
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
    w.advance(5)
    mid = w.entity('the-slave').status.get('hebrew_slave') and \
        not any(e['effect'] == 'goes_free'
                for e in w.entity('the-slave').ledger)
    w.advance(6)
    freed = any(e['effect'] == 'goes_free'
                for e in w.entity('the-slave').ledger)
    results.append(w.checkpoint(
        'year 5: still serving; year 6+: free',
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
              'jubilee_year': 12,
              'case_source': 'Kiddushin 15a:19 on Exod 21:6 + Lev 25:10'})
    w.advance(12)
    freed2 = [e for e in w.entity('the-pierced').ledger
              if e['effect'] == 'jubilee_release']
    six_yr_freed = [e for e in w.entity('the-pierced').ledger
                    if e['effect'] == 'goes_free']
    cancels = len([l for l in w.log if l[0] == 'TIMER-CANCEL'])
    results.append(w.checkpoint(
        'six-year exit VOIDED; jubilee fires at 12',
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
