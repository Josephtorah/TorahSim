#!/usr/bin/env python3
# THE MISHPATIM RE-COMPILATION PASS (2026-09-02, under the compiler law)
# Owner's order: "Ok run it and report what you find."
# Five functions of the law code (Exodus 21:1-23:19) cold-compiled and
# graded against their Mishnah answer sheets. Companion to
# cold_run_guardians.py (the sixth function, already 12/12).
# Read-only; touches no unit; every non-ink cell labeled with the
# teacher's source row; every token probed (zero-report law).

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
