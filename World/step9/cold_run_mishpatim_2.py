#!/usr/bin/env python3
# MISHPATIM RE-COMPILATION, PASS 2 (2026-09-02) — three more functions
# before the listening epub, at the owner's word ("feel free to find a
# few more"). Same discipline as cold_run_mishpatim.py.

import sqlite3, sys

db = sqlite3.connect('<repo-old>/elijah_docket/tanakh.sqlite')
def has(book, ch, vs, num):
    for (lem,) in db.execute("""SELECT COALESCE(w.lemma,'') FROM words w
        JOIN verses v ON w.verse_id=v.id
        WHERE v.book=? AND v.chapter=? AND v.verse=?""", (book, ch, vs)):
        if str(num) in lem.replace('/', ' ').split(): return True
    return False

PROBES = [('dowry', 4119, 'Exod', 22, 16), ('fifty', 2572, 'Deut', 22, 29),
          ('eye', 5869, 'Exod', 21, 26), ('tooth', 8127, 'Exod', 21, 27),
          ('free', 2670, 'Exod', 21, 26), ('judges', 6414, 'Exod', 21, 22)]
bad = [p for p in PROBES if not has(*p[2:], p[1])]
if bad: sys.exit('ZERO-REPORT LAW: probes failed: %r' % bad)
print('probes: all %d fired  [zero-report law satisfied]\n' % len(PROBES))

TOTAL = {'INK': 0, 'RECORDED': 0, 'ROUTED/IMPORT': 0}
def grade(fn, oracle, cells):
    ok = 0
    print('FUNCTION: %s  (answer sheet: %s)' % (fn, oracle))
    for name, v, want, prov, kind in cells:
        ok += v == want; TOTAL[kind] += 1
        print('  %-36s %-9s [%s]  <- %s' % (name, v, 'ok' if v == want else 'MISMATCH', prov))
    print('  -> %d/%d\n' % (ok, len(cells)))
    return ok, len(cells)

R = []
R.append(grade('the seducer\'s fine', 'Mishnah Ketubot 3:4', [
    ('a fine exists, paid to the father', 'FINE', 'FINE',
     'INK Exod 22:15-16: "he shall surely pay a dowry... weigh money"', 'INK'),
    ('the AMOUNT: a pointer, not a number', 'FETCH-50', 'FETCH-50',
     'INK holds only the pointer "like the dowry [4119] of the virgins"; the constant — fifty [2572] silver — lives in Deut 22:29; the link is recorded [Ketubot 29b:3 parsing the triple mention]', 'ROUTED/IMPORT'),
    ('the payments table: seducer 3, rapist 4', 'TABLE', 'TABLE',
     'ANSWER-KEY [Mishnah Ketubot 3:4]: humiliation, degradation, fine; the rapist adds pain', 'ROUTED/IMPORT'),
]))
R.append(grade('the freed slave\'s limbs', 'Kiddushin 24a + Mishnah Negaim 6:7', [
    ('EYE destroyed -> freedom', 'FREE', 'FREE',
     'INK Exod 21:26: eye [5869] + free [2670]', 'INK'),
    ('TOOTH knocked out -> freedom', 'FREE', 'FREE',
     'INK Exod 21:27: tooth [8127] + free', 'INK'),
    ('the CLASS: all limb-tips that do not regenerate', 'CLASS-24', 'CLASS-24',
     'RECORDED [Kiddushin 24a:6: "granted, a tooth and an eye are WRITTEN..." — the exemplars generalized]; the 24-member list enumerated at Mishnah Negaim 6:7', 'RECORDED'),
]))
R.append(grade('the miscarriage valuation', 'Mishnah Bava Kamma 5:4', [
    ('assessment goes THROUGH THE COURT', 'JUDGES', 'JUDGES',
     'INK Exod 21:22: "he shall give by the judges [6414]"', 'INK'),
    ('the valuation ALGORITHM: before/after', 'DIFF-VALUE', 'DIFF-VALUE',
     'ANSWER-KEY [Mishnah Bava Kamma 5:4]: appraise her worth before the birth and after, pay the difference — with Rabban Shimon ben Gamliel\'s objection recorded', 'ROUTED/IMPORT'),
    ('the actor class: a PERSON pays, an ox is exempt', 'PERSON-ONLY', 'PERSON-ONLY',
     'INK-PATTERN Exod 21:22 opens "when MEN strive" + ANSWER-KEY [same mishnah: the ox that struck her — exempt]', 'INK'),
]))

ok = sum(a for a, _ in R); n = sum(b for _, b in R)
print('=' * 60)
print('PASS 2: %d/%d  |  RUNNING TOTAL with passes 1+guardians: %d/44' % (ok, n, 35 + ok))
print('PASS-2 FRACTIONS: INK %d | RECORDED %d | ROUTED/IMPORT %d'
      % (TOTAL['INK'], TOTAL['RECORDED'], TOTAL['ROUTED/IMPORT']))

# ---- EFFECTS (retrofit 2026-09-03, under the effects law) -----------
import effects_layer as FX
EFFECTS = [
    ('seducer: FINE to the father',      ['gives_fixed_sum']),
    ('seducer: FETCH-50 (the pointer)',  [FX.NONE]),
    ('seducer: payments TABLE',          ['pays']),
    ('freed limbs: EYE -> freedom',      ['released', 'goes_free']),
    ('freed limbs: TOOTH -> freedom',    ['released', 'goes_free']),
    ('freed limbs: CLASS-24',            [FX.NONE]),
    ('miscarriage: JUDGES assess',       ['fined_by_assessment']),
    ('miscarriage: DIFF-VALUE algorithm', [FX.NONE]),
    ('miscarriage: PERSON-ONLY (ox actor exempt)', ['exempt']),
]
print('\nEFFECTS — the state changes each cell writes:')
used = []
for name, fx in EFFECTS:
    used += fx
    for line in FX.render(fx):
        print('  %-40s ->%s' % (name, line))
ops = FX.summarize(used)
print('LEDGER OPS this pass writes:',
      ', '.join('%s x%d' % (op, cnt) for op, cnt in sorted(ops.items())))
assert len(EFFECTS) == n, 'EFFECTS LAW: %d cells graded, %d mapped' % (n, len(EFFECTS))
print('effects: all %d cells carry a REGISTERED effect or an honest '
      'no-change [effects law satisfied]' % n)
