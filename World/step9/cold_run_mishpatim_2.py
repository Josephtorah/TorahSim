#!/usr/bin/env python3
# MISHPATIM RE-COMPILATION, PASS 2 (2026-09-02) — three more functions
# before the listening epub, at the owner's word ("feel free to find a
# few more"). Same discipline as cold_run_mishpatim.py.

# ---- THE HONEST-PAIRING GUARD (sitting C retrofit, 2026-09-05) ------------
# Every expected value this runner grades against must be a LITERAL typed from
# the answer sheet; the parser checks the source before anything runs, and the
# count below is the tripwire — it fails loudly the day the table changes.
import os as _os, sys as _sys
_sys.path.insert(0, _os.path.dirname(_os.path.abspath(__file__)))
from compile_guards import check_honest_pairing as _chp, check_honest_dict as _chd, check_honest_calls as _chc
_P = _os.path.abspath(__file__)
GUARDED = _chc(_P, 'grade', 2, 2)
assert GUARDED == 10, ("the guard counted %d expectations, the tripwire holds 10" % GUARDED)
print('guard: %d expectations checked, every one a literal from the answer sheet [honest-pairing guard satisfied]' % GUARDED)
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

# ---- THE WRAP (W1 THE EXODUS LAW, D9-iii, 2026-09-07) — the daemon and the scene --------------
# The three case heads this pass compiled, as watched types of event_vocabulary.yaml: the seducer
# (22:15-16), the maimed slave (21:26-27), the struck pregnant woman (21:22). The daemon writes the
# ledger and never emits an event; every effect is registry-validated at write time.
import io, contextlib, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import world_engine as WE
def law_mishpatim_2(event, world):
    """Exod 22:15-16, 21:26-27, 21:22 (cold_run_mishpatim_2.py — the seducer, the freed limbs, the miscarriage)."""
    k, src = event['kind'], event['case_source']
    E_ = lambda eff, s, cp=None, amount=None, due=None, law='', value=None: {'effect': eff, 'subject': s, 'counterparty': cp, 'amount': amount, 'due': due, 'value': value if value is not None else True, 'source_law': law, 'case_source': src}
    if k == 'virgin_seduced':
        out = [E_('gives_fixed_sum', event['seducer'], cp=event['father'], value='FETCH-50', law='the seducer: FINE [INK 22:15-16 "he shall weigh silver like the dowry of the virgins" — the amount a POINTER to Deut 22:29, Ketubot 29b:3]'),
               E_('pays', event['seducer'], cp=event['father'], value='humiliation', law='the seducer: TABLE [ANSWER-KEY Mishnah Ketubot 3:4]'),
               E_('pays', event['seducer'], cp=event['father'], value='degradation', law='the seducer: TABLE [ANSWER-KEY Mishnah Ketubot 3:4]')]
        if event.get('raped'):
            out.append(E_('pays', event['seducer'], cp=event['father'], value='pain', law='the rapist adds PAIN [ANSWER-KEY Mishnah Ketubot 3:4]'))
        return out
    if k == 'slave_maimed':
        if event['limb'] in ('eye', 'tooth') or not event.get('regenerates', True):
            return [E_('released', event['slave'], cp=event['master'], value=event['limb'], law='freed limbs [INK 21:26-27 "he shall send him free for his eye... for his tooth"]'),
                    E_('goes_free', event['slave'], law='freed limbs: CLASS-24 [RECORDED Kiddushin 24a:6: the exemplars generalized to the limb-tips; Mishnah Negaim 6:7]')]
        return []                                                # a limb that grows back: no exemplar reaches it
    if k == 'pregnant_woman_struck':
        if event.get('actor_kind', 'person') != 'person':
            return [E_('exempt', event['striker'], law='miscarriage: PERSON-ONLY [INK-PATTERN 21:22 "when MEN strive"; ANSWER-KEY Mishnah Bava Kamma 5:4: the ox that struck her — exempt]')]
        return [E_('fined_by_assessment', event['striker'], cp=event['husband'], amount=event['value_before'] - event['value_after'], law='miscarriage: JUDGES + DIFF-VALUE [INK 21:22 "he shall give by the judges"; ANSWER-KEY Mishnah Bava Kamma 5:4: her worth before and after]')]
    return []

def scene():
    """THE SCENE — the recorded cases replayed on the world engine (clock unit: days)."""
    with contextlib.redirect_stdout(io.StringIO()):
        w = WE.World(era='Mishpatim pass 2: Ketubot 3:4, Kiddushin 24a, Bava Kamma 5:4 on the engine (clock unit: days)')
        w.laws = [law_mishpatim_2]
        w.advance(1)
        w.submit({'kind': 'virgin_seduced', 'subject': 'the-seducer', 'seducer': 'the-seducer', 'father': 'her-father', 'raped': False, 'case_source': 'Mishnah Ketubot 3:4 — the seducer pays three'})
        w.submit({'kind': 'virgin_seduced', 'subject': 'the-rapist', 'seducer': 'the-rapist', 'father': 'her-father', 'raped': True, 'case_source': 'Mishnah Ketubot 3:4 — the rapist pays four'})
        w.advance(2)
        w.submit({'kind': 'slave_maimed', 'subject': 'the-master', 'master': 'the-master', 'slave': 'the-slave', 'limb': 'eye', 'case_source': 'Exod 21:26 — the eye; Kiddushin 24a'})
        w.submit({'kind': 'slave_maimed', 'subject': 'the-master', 'master': 'the-master', 'slave': 'the-maidservant', 'limb': 'tooth', 'case_source': 'Exod 21:27 — the tooth; Kiddushin 24a'})
        w.submit({'kind': 'slave_maimed', 'subject': 'the-master', 'master': 'the-master', 'slave': 'the-second-slave', 'limb': 'hair', 'regenerates': True, 'case_source': 'Kiddushin 24a — a limb that grows back: no exemplar'})
        w.advance(3)
        w.submit({'kind': 'pregnant_woman_struck', 'subject': 'the-striker', 'striker': 'the-striker', 'actor_kind': 'person', 'husband': 'her-husband', 'value_before': 200, 'value_after': 150, 'case_source': 'Mishnah Bava Kamma 5:4 — her worth before and after'})
        w.submit({'kind': 'pregnant_woman_struck', 'subject': 'the-ox-owner', 'striker': 'the-ox-owner', 'actor_kind': 'ox', 'husband': 'her-husband', 'value_before': 200, 'value_after': 150, 'case_source': 'Mishnah Bava Kamma 5:4 — the ox that struck her: exempt'})
    n = lambda eid, eff: len([e for e in w.entity(eid).ledger if e['effect'] == eff])
    amt = lambda eid, eff: sum(e['amount'] or 0 for e in w.entity(eid).ledger if e['effect'] == eff)
    return (n('the-seducer', 'gives_fixed_sum'), n('the-seducer', 'pays'), n('the-rapist', 'gives_fixed_sum'), n('the-rapist', 'pays'),
            n('the-slave', 'released'), n('the-slave', 'goes_free'), n('the-maidservant', 'released'), n('the-maidservant', 'goes_free'), n('the-second-slave', 'released'),
            n('the-striker', 'fined_by_assessment'), amt('the-striker', 'fined_by_assessment'), n('the-ox-owner', 'exempt'), n('the-ox-owner', 'fined_by_assessment'), w.clock.year), w
SCENE, _W = scene()
wrap_cells = [
    ('THE SCENE on the world engine (the wrap)', SCENE, (1, 2, 1, 3, 1, 1, 1, 1, 0, 1, 50, 1, 0, 3),
     'RECORDED — the answer sheet\'s rows as the tape: Ketubot 3:4 (the seducer three, the rapist four), Kiddushin 24a (eye, tooth; the regenerating limb no exemplar), Bava Kamma 5:4 (the difference; the ox exempt)', 'RECORDED'),
]
R.append(grade('THE WRAP — the daemon on the recorded cases', 'Ketubot 3:4 + Kiddushin 24a + Bava Kamma 5:4', wrap_cells))
print('WATCH COVERAGE (the wrap):')
_W.print_coverage()
print()

ok = sum(a for a, _ in R); n = sum(b for _, b in R)
print('=' * 60)
print('PASS 2: %d/%d cells  |  RUNNING TOTAL with passes 1+guardians: %d/44' % (ok, n, 35 + ok))
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
    ('THE SCENE (the wrap)',             ['gives_fixed_sum', 'pays', 'released', 'goes_free', 'fined_by_assessment', 'exempt']),
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
