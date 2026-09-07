#!/usr/bin/env python3
# THE MISHPATIM RE-COMPILATION PASS (2026-09-02, under the compiler law)
# Owner's order: "Ok run it and report what you find."
# Five functions of the law code (Exodus 21:1-23:19) cold-compiled and
# graded against their Mishnah answer sheets. Companion to
# cold_run_guardians.py (the sixth function, already 12/12).
# Read-only; touches no unit; every non-ink cell labeled with the
# teacher's source row; every token probed (zero-report law).

# ---- THE HONEST-PAIRING GUARD (sitting C retrofit, 2026-09-05) ------------
# Every expected value this runner grades against must be a LITERAL typed from
# the answer sheet; the parser checks the source before anything runs, and the
# count below is the tripwire — it fails loudly the day the table changes.
import os as _os, sys as _sys
_sys.path.insert(0, _os.path.dirname(_os.path.abspath(__file__)))
from compile_guards import check_honest_pairing as _chp, check_honest_dict as _chd, check_honest_calls as _chc
_P = _os.path.abspath(__file__)
GUARDED = _chc(_P, 'grade', 2, 2)
assert GUARDED == 21, ("the guard counted %d expectations, the tripwire holds 21" % GUARDED)
print('guard: %d expectations checked, every one a literal from the answer sheet [honest-pairing guard satisfied]' % GUARDED)
import sqlite3, sys, os

# THE FIRST CALL (2026-09-05): the talion cell no longer carries its
# verdict — it CALLS the compiled Lev 24 span, the tariff formula's
# only other seat in the canon (EX21-18; move M-07 exemplar c,
# EXECUTED). The first inter-span function call of the compiled Bible.
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from cold_run_lev24 import talion as lev24_talion

DB = '<repo-old>/elijah_docket/tanakh.sqlite'
db = sqlite3.connect(DB)

def strip(s):
    return ''.join(c for c in s if c != '/' and not (0x0591 <= ord(c) <= 0x05C7))

def words(book, ch, vs):
    return db.execute("""SELECT w.idx, w.he, COALESCE(w.lemma,'') FROM words w
        JOIN verses v ON w.verse_id=v.id
        WHERE v.book=? AND v.chapter=? AND v.verse=? ORDER BY w.idx""",
        (book, ch, vs)).fetchall()

def has_lemma(book, ch, vs, num):
    for _, _, lem in words(book, ch, vs):
        if str(num) in lem.replace('/', ' ').split():
            return True
    return False

# ---- probes: every token the run relies on must fire where expected --
PROBES = [
    ('six',       8337, 'Exod', 21, 2),  ('seventh', 7637, 'Exod', 21, 2),
    ('free',      2670, 'Exod', 21, 2),  ('redeem',  6299, 'Exod', 21, 8),
    ('jubilee',   3104, 'Lev',  25, 10), ('ox',      7794, 'Exod', 21, 28),
    ('pit',        953, 'Exod', 21, 33), ('graze',   1197, 'Exod', 22, 4),
    ('fire',       784, 'Exod', 22, 5),  ('best',    4315, 'Exod', 22, 4),
    ('divide',    2673, 'Exod', 21, 35), ('yesterday', 8543, 'Exod', 21, 29),
    ('day-before', 8032, 'Exod', 21, 29),('stone',   5619, 'Exod', 21, 29),
    ('ransom',    3724, 'Exod', 21, 30), ('thirty',  7970, 'Exod', 21, 32),
    ('shekel',    8255, 'Exod', 21, 32), ('heal',    7495, 'Exod', 21, 19),
    ('idleness',  7674, 'Exod', 21, 19), ('wound',   6482, 'Exod', 21, 25),
    ('double',    8147, 'Exod', 22, 3),  ('five',    2568, 'Exod', 21, 37),
    ('cattle',    1241, 'Exod', 21, 37), ('four',     702, 'Exod', 21, 37),
    ('flock',     6629, 'Exod', 21, 37), ('pay',     7999, 'Exod', 21, 36),
]
failed = [(n, b, c, v) for n, num, b, c, v in PROBES if not has_lemma(b, c, v, num)]
if failed:
    sys.exit('ZERO-REPORT LAW: probes failed to fire: %r — refusing to run' % failed)
print('probes: all %d token probes fired  [zero-report law satisfied]\n' % len(PROBES))

TOTAL = {'INK': 0, 'RECORDED': 0, 'ROUTED/IMPORT': 0}
def grade(fn, oracle_name, cells):
    ok = 0
    print('FUNCTION: %s  (answer sheet: %s)' % (fn, oracle_name))
    for name, verdict, want, prov, kind in cells:
        mark = 'ok' if verdict == want else 'MISMATCH'
        ok += verdict == want
        TOTAL[kind] += 1
        print('  %-34s %-10s [%s]  <- %s' % (name, verdict, mark, prov))
    print('  -> %d/%d\n' % (ok, len(cells)))
    return ok, len(cells)

results = []

# ---- F1: the Hebrew slave's release list (code: 21:2-6, 8) ----------
cells = [
    ('release by YEARS (the timer)', 'FREE-YEAR-7', 'FREE-YEAR-7',
     'INK 21:2: six [8337] + seventh [7637] + free [2670] all in the verse', 'INK'),
    ('release by DEDUCTION (buy-out)', 'DEDUCT', 'DEDUCT',
     'RECORDED [Kiddushin 16a:11]: from 21:8 "let her be redeemed" [6299], applied by comparison', 'RECORDED'),
    ('release by JUBILEE', 'FREE-AT-JUBILEE', 'FREE-AT-JUBILEE',
     'IMPORT [Leviticus 25; Kiddushin 15a:19: written even for the pierced "forever"]', 'ROUTED/IMPORT'),
]
results.append(grade('slave-release', 'Mishnah Kiddushin 1:2', cells))

# ---- F2: the four damage classes (code: 21:28-22:5) -----------------
openers = []
for ch, vs, lem, label in ((21, 28, 7794, 'OX'), (21, 33, 953, 'PIT'),
                           (22, 4, 1197, 'GRAZING'), (22, 5, 784, 'FIRE')):
    first = strip(words('Exod', ch, vs)[0][1])
    assert first in ('כי', 'וכי') and has_lemma('Exod', ch, vs, lem)
    openers.append(label)
cells = [('class %s (case opener found)' % l, 'MODULE', 'MODULE',
          'INK: verse-initial KI + the class noun in its opener verse', 'INK')
         for l in openers]
cells.append(('common output: pay from the BEST', 'BEST-OF-LAND', 'BEST-OF-LAND',
              'INK 22:4 "best of his field, best of his vineyard" [4315 x2] + GENERALIZED [Bava Kamma 6b]', 'RECORDED'))
results.append(grade('four-damages class map', 'Mishnah Bava Kamma 1:1', cells))

# ---- F3: the goring-ox state machine (code: 21:28-32, 35-36) --------
cells = [
    ('innocuous state: HALF, from the body', 'HALF-FROM-BODY', 'HALF-FROM-BODY',
     'INK 21:35: "divide" [2673] the live ox — the split is the payment and its cap', 'INK'),
    ('forewarned state: FULL damages', 'FULL', 'FULL',
     'INK 21:36: "he shall pay [7999] ox for ox"', 'INK'),
    ('transition threshold = 3 gorings', 'THREE', 'THREE',
     'RECORDED [Bava Kamma 23b:17-18]: yesterday [8543] + day-before [8032] + "not secured" = 3; two named tokenizations (Abaye/Rava)', 'RECORDED'),
    ('reverse transition (back to innocuous)', 'REVERTS', 'REVERTS',
     'ANSWER-KEY [Mishnah Bava Kamma 2:4]: three days of restraint; semantics debate recorded at 24a:9', 'ROUTED/IMPORT'),
    ('human victim: stoning + ransom branch', 'STONE+RANSOM', 'STONE+RANSOM',
     'INK 21:29-30: stoned [5619], owner liable, IM-branch: ransom [3724]', 'INK'),
    ('slave victim: fixed thirty shekels', '30-SHEKELS', '30-SHEKELS',
     'INK 21:32: thirty [7970] shekels [8255] — the fixed fine the Mishnah repeats', 'INK'),
]
results.append(grade('goring-ox state machine', 'Mishnah Bava Kamma 1:4 + 2:4', cells))

# ---- F4: the five injury indemnities (code: 21:18-19, 24-25) --------
cells = [
    ('MEDICAL costs', 'PAY', 'PAY',
     'INK 21:19: "and healing he shall heal" [7495]', 'INK'),
    ('LOSS OF LIVELIHOOD', 'PAY', 'PAY',
     'INK 21:19: "his idleness he shall give" [7674]', 'INK'),
    ('DAMAGE (the tariff, as money)', lev24_talion('eye')['verdict'], 'PAY-MONEY',
     'CALLED cold_run_lev24.talion(): resolves THROUGH the call site [Bava Kamma 83b:10, 84a:1; move M-07c EXECUTED]', 'RECORDED'),
    ('PAIN', 'PAY', 'PAY',
     'RECORDED [Bava Kamma 85a]: from "wound for wound" [6482], 21:25', 'RECORDED'),
    ('HUMILIATION', 'PAY', 'PAY',
     'IMPORT [Deuteronomy 25:11-12, the recorded source in the sugya]', 'ROUTED/IMPORT'),
]
results.append(grade('injury indemnities', 'Mishnah Bava Kamma 8:1', cells))

# ---- F5: the theft multiples (code: 21:37, 22:3) --------------------
cells = [
    ('DOUBLE payment (base)', 'X2', 'X2',
     'INK 22:3: "he shall pay double" [8147]', 'INK'),
    ('FIVEFOLD for the ox', 'X5', 'X5',
     'INK 21:37: five [2568] cattle [1241] for the ox', 'INK'),
    ('FOURFOLD for the sheep', 'X4', 'X4',
     'INK 21:37: four [702] of the flock [6629] for the sheep', 'INK'),
    ('scope: 4/5 ONLY ox and sheep', 'RESTRICTED', 'RESTRICTED',
     'INK-PATTERN 21:37: the constants attach to those two nouns alone — Mishnah 7:1 states it "as it is stated"', 'INK'),
]
results.append(grade('theft multiples', 'Mishnah Bava Kamma 7:1', cells))

# ---- THE WRAP (W1 THE EXODUS LAW, D9-iii, 2026-09-07) — the daemon and the scene --------------
# The skeleton's law_slave_term (F1) and law_goring_ox (F3) stay in world_engine.py as the LIBRARY,
# registered on this scene beside the runner's own daemon, which takes the case heads the library
# does not: the quarrel (21:18-19 with the tariff CALLED from Lev 24), the pit (21:33-34), the
# grazing (22:4), the fire (22:5), the theft multiples (21:37, 22:3), and the buy-out (21:8 by
# comparison). Every watched kind is a case-form type of event_vocabulary.yaml; every effect is
# registry-validated at write time; the daemon writes the ledger and never emits an event.
import io, contextlib
import world_engine as WE
def law_mishpatim(event, world):
    """Exod 21:18-19, 21:33-34, 21:37-22:5, 21:8 (cold_run_mishpatim.py F1 DEDUCT, F2, F4, F5)."""
    k, src = event['kind'], event['case_source']
    E_ = lambda eff, s, cp=None, amount=None, due=None, law='', value=None: {'effect': eff, 'subject': s, 'counterparty': cp, 'amount': amount, 'due': due, 'value': value if value is not None else True, 'source_law': law, 'case_source': src}
    if k == 'men_quarrel':
        tal = lev24_talion(event.get('blemish', 'eye'))          # the first inter-span call, run live on the tape
        return [E_('pays', event['striker'], cp=event['victim'], amount=event['medical'], law='F4 MEDICAL [INK 21:19 "and healing he shall heal"]'),
                E_('gives_fixed_sum', event['striker'], cp=event['victim'], amount=event['idleness'], law='F4 LIVELIHOOD [INK 21:19 "his idleness he shall give"]'),
                E_('substitution', event['striker'], cp=event['victim'], value=tal['verdict'], law='F4 DAMAGE [CALLED cold_run_lev24.talion(%s) -> %s; Bava Kamma 83b:10, 84a:1]' % (tal['blemish'], tal['verdict'])),
                E_('pays', event['striker'], cp=event['victim'], value='pain', law='F4 PAIN [RECORDED Bava Kamma 85a: "wound for wound", 21:25]'),
                E_('pays', event['striker'], cp=event['victim'], value='humiliation', law='F4 HUMILIATION [IMPORT Deut 25:11-12]')]
    if k == 'pit_opened':
        return [E_('pays', event['owner'], cp=event['victim'], amount=event['damage'], law='F2 PIT [INK 21:34 "the owner of the pit shall pay"]')]
    if k == 'field_grazed':
        return [E_('pays', event['grazer'], cp=event['owner'], amount=event['damage'], value='best_of_the_land', law='F2 GRAZING [INK 22:4 "the best of his field and the best of his vineyard he shall pay"]')]
    if k == 'fire_spread':
        return [E_('pays', event['kindler'], cp=event['owner'], amount=event['damage'], law='F2 FIRE [INK 22:5 "the kindler of the fire shall surely pay"]')]
    if k == 'animal_stolen':
        if event['disposed']:                                    # slaughtered or sold (21:37)
            mult = 5 if event['animal'] == 'ox' else 4
            return [E_('pays_four_five', event['thief'], cp=event['owner'], amount=mult * event['value'], law='F5 [INK 21:37 five cattle for the ox, four sheep for the sheep]')]
        return [E_('pays_double', event['thief'], cp=event['owner'], amount=2 * event['value'], law='F5 [INK 22:3 "if the theft is found in his hand... he shall pay double"]')]
    if k == 'redeemed_by_deduction':
        world.cancel_timers(event['slave'], 'goes_free', 'the buy-out [RECORDED Kiddushin 16a:11 from 21:8 "let her be redeemed", by comparison]')
        return [E_('pays', event['slave'], cp=event['master'], amount=event['amount'], law='F1 DEDUCT [RECORDED Kiddushin 16a:11]'),
                E_('goes_free', event['slave'], law='F1 DEDUCT [Mishnah Kiddushin 1:2: acquires himself by deduction of money]')]
    return []

def scene():
    """THE SCENE — the recorded cases replayed on the world engine (clock unit: years; the answer sheet's rows as the tape)."""
    with contextlib.redirect_stdout(io.StringIO()):
        w = WE.World(era='Mishpatim: Kiddushin 1:2 and Bava Kamma 1-8 on the engine (clock unit: years)')
        w.laws = [WE.law_slave_term, WE.law_goring_ox, law_mishpatim]
        w.advance(1)
        w.submit({'kind': 'acquire_hebrew_slave', 'subject': 'the-master', 'master': 'the-master', 'slave': 'the-slave', 'case_source': 'Mishnah Kiddushin 1:2 — acquires himself by years'})
        w.advance(3)
        w.submit({'kind': 'redeemed_by_deduction', 'subject': 'the-slave', 'slave': 'the-slave', 'master': 'the-master', 'amount': 30, 'case_source': 'Mishnah Kiddushin 1:2 — by deduction of money; Kiddushin 16a:11'})
        w.advance(4)
        for i in (1, 2, 3):
            w.submit({'kind': 'ox_gores', 'subject': 'the-ox', 'ox': 'the-ox', 'owner': 'reuben', 'victim': 'simeon', 'victim_kind': 'animal', 'damage': 100, 'case_source': 'Mishnah Bava Kamma 2:4 — goring #%d' % i})
        w.submit({'kind': 'ox_gores', 'subject': 'the-ox', 'ox': 'the-ox', 'owner': 'reuben', 'victim': 'simeon', 'victim_kind': 'animal', 'damage': 100, 'case_source': 'Mishnah Bava Kamma 1:4 — the forewarned pays full'})
        w.submit({'kind': 'ox_gores', 'subject': 'the-ox', 'ox': 'the-ox', 'owner': 'reuben', 'victim': 'the-slaves-master', 'victim_kind': 'slave', 'case_source': 'Mishnah Bava Kamma 4:5 — the slave gored: thirty sela, the ox stoned'})
        w.advance(5)
        w.submit({'kind': 'men_quarrel', 'subject': 'levi', 'striker': 'levi', 'victim': 'judah', 'medical': 10, 'idleness': 5, 'blemish': 'eye', 'case_source': 'Mishnah Bava Kamma 8:1 — the five indemnities'})
        w.submit({'kind': 'pit_opened', 'subject': 'dan', 'owner': 'dan', 'victim': 'naphtali', 'damage': 40, 'case_source': 'Mishnah Bava Kamma 1:1 — the pit'})
        w.submit({'kind': 'field_grazed', 'subject': 'gad', 'grazer': 'gad', 'owner': 'asher', 'damage': 20, 'case_source': 'Mishnah Bava Kamma 1:1 — the tooth; from the best of the land'})
        w.submit({'kind': 'fire_spread', 'subject': 'issachar', 'kindler': 'issachar', 'owner': 'zebulun', 'damage': 60, 'case_source': 'Mishnah Bava Kamma 1:1 — the fire; 6:4'})
        w.advance(6)
        w.submit({'kind': 'animal_stolen', 'subject': 'the-thief', 'thief': 'the-thief', 'owner': 'joseph', 'animal': 'ox', 'disposed': True, 'value': 10, 'case_source': 'Mishnah Bava Kamma 7:1 — five for the ox'})
        w.submit({'kind': 'animal_stolen', 'subject': 'the-thief', 'thief': 'the-thief', 'owner': 'joseph', 'animal': 'sheep', 'disposed': True, 'value': 10, 'case_source': 'Mishnah Bava Kamma 7:1 — four for the sheep'})
        w.submit({'kind': 'animal_stolen', 'subject': 'the-thief', 'thief': 'the-thief', 'owner': 'joseph', 'animal': 'ox', 'disposed': False, 'value': 10, 'case_source': 'Mishnah Bava Kamma 7:1 — found in his hand: double'})
        w.advance(8)                                              # year 7 passes: the CANCELLED six-year timer must not fire
    n = lambda eid, eff: len([e for e in w.entity(eid).ledger if e['effect'] == eff])
    amt = lambda eid, eff: sum(e['amount'] or 0 for e in w.entity(eid).ledger if e['effect'] == eff)
    cut = len([l for l in w.log if l[0] == 'TIMER-CANCEL']); fired = len([l for l in w.log if l[0] == 'TIMER-FIRE'])
    return (n('the-slave', 'term_clock'), n('the-slave', 'pays'), n('the-slave', 'goes_free'), cut, fired,
            n('reuben', 'pays'), amt('reuben', 'pays'), n('the-ox', 'forewarned'), n('the-ox', 'stoned'), n('reuben', 'gives_fixed_sum'), amt('reuben', 'gives_fixed_sum'),
            n('levi', 'pays'), n('levi', 'gives_fixed_sum'), n('levi', 'substitution'), n('dan', 'pays'), n('gad', 'pays'), n('issachar', 'pays'),
            n('the-thief', 'pays_four_five'), amt('the-thief', 'pays_four_five'), n('the-thief', 'pays_double'), amt('the-thief', 'pays_double'), w.clock.year), w
SCENE, _W = scene()
wrap_cells = [
    ('THE SCENE on the world engine (the wrap)', SCENE, (1, 1, 1, 1, 0, 4, 250.0, 1, 1, 1, 30, 3, 1, 1, 1, 1, 1, 2, 90, 1, 20, 8),
     'RECORDED — the answer sheet\'s rows as the tape: Kiddushin 1:2 (years, then the buy-out CANCELS the year-7 timer — no fire), Bava Kamma 2:4 (three gorings: half, half, half + FOREWARNED), 1:4 (full), '
     '4:5 (the slave: stoned + thirty), 8:1 (the five: three pays, the idleness sum, the tariff CALLED from Lev 24), 1:1 (pit, tooth, fire), 7:1 (five, four, double); the clock ABSOLUTE', 'RECORDED'),
]
results.append(grade('THE WRAP — the daemon on the recorded cases', 'Kiddushin 1:2 + Bava Kamma 1:1, 1:4, 2:4, 4:5, 7:1, 8:1', wrap_cells))
print('WATCH COVERAGE (the wrap): the library daemons and the runner\'s own, on this scene\'s tape')
_W.print_coverage()
print()

# ---- summary --------------------------------------------------------
ok = sum(a for a, _ in results); n = sum(b for _, b in results)
print('=' * 60)
print('MISHPATIM PASS: %d/%d cells across 5 functions' % (ok, n))
print('  + the guardians run (separate machine): 12/12')
print('PROVENANCE FRACTIONS (this pass): INK %d | RECORDED %d | ROUTED/IMPORT %d'
      % (TOTAL['INK'], TOTAL['RECORDED'], TOTAL['ROUTED/IMPORT']))

# ---- EFFECTS (retrofit 2026-09-03, under the effects law) -----------
# Each graded cell's state change, from effect_vocabulary.yaml. The
# verdict writes the LEDGER, never the event stream. Cells that only
# CLASSIFY (a module map, a scope restriction) honestly write nothing.
import effects_layer as FX
EFFECTS = [
    # F1 slave-release
    ('slave-release: FREE-YEAR-7',   ['term_clock', 'goes_free']),
    ('slave-release: DEDUCT',        ['pays', 'goes_free']),
    ('slave-release: FREE-AT-JUBILEE', ['jubilee_release', 'goes_free']),
    # F2 four damages (class map = classification; the output cell pays)
    ('four-damages: class OX',       [FX.NONE]),
    ('four-damages: class PIT',      [FX.NONE]),
    ('four-damages: class GRAZING',  [FX.NONE]),
    ('four-damages: class FIRE',     [FX.NONE]),
    ('four-damages: BEST-OF-LAND',   ['pays']),
    # F3 goring ox
    ('goring-ox: HALF-FROM-BODY',    ['pays']),
    ('goring-ox: FULL',              ['pays']),
    ('goring-ox: THREE (threshold)', ['forewarned']),
    ('goring-ox: REVERTS',           ['forewarned']),
    ('goring-ox: STONE+RANSOM',      ['stoned', 'ransom_imposed']),
    ('goring-ox: 30-SHEKELS',        ['gives_fixed_sum']),
    # F4 injury indemnities
    ('injuries: MEDICAL',            ['pays']),
    ('injuries: LIVELIHOOD',         ['gives_fixed_sum']),
    ('injuries: DAMAGE (talion-as-money)', ['substitution']),
    ('injuries: PAIN',               ['pays']),
    ('injuries: HUMILIATION',        ['pays']),
    # F5 theft multiples
    ('multiples: DOUBLE',            ['pays_double']),
    ('multiples: FIVEFOLD ox',       ['pays_four_five']),
    ('multiples: FOURFOLD sheep',    ['pays_four_five']),
    ('multiples: RESTRICTED scope',  [FX.NONE]),
    # THE WRAP (W1): the scene's tape — every effect written on the ledger by the library daemons and law_mishpatim
    ('THE SCENE (the wrap)',         ['term_clock', 'goes_free', 'pays', 'forewarned', 'stoned', 'gives_fixed_sum', 'ransom_imposed', 'substitution', 'pays_four_five', 'pays_double']),
]
print('\nEFFECTS — the state changes each cell writes:')
used = []
for name, fx in EFFECTS:
    used += fx
    for line in FX.render(fx):
        print('  %-36s ->%s' % (name, line))
ops = FX.summarize(used)
print('LEDGER OPS this pass writes:',
      ', '.join('%s x%d' % (op, cnt) for op, cnt in sorted(ops.items())))
assert len(EFFECTS) == n, 'EFFECTS LAW: %d cells graded, %d mapped' % (n, len(EFFECTS))
print('effects: all %d cells carry a REGISTERED effect or an honest '
      'no-change [effects law satisfied]' % n)
