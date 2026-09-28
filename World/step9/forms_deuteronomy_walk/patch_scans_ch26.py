import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
# THE DEUTERONOMY WALK 18b (2026-09-26; LEAN) — RUN B: THE IMPORT-TIME HOLE SCANS WIDENED BY NAME for the ninety-one new rows the fold carries after the tape's first run
# (the scan census's section A intersected with the spec's NEW_EFFECTS; the runner's fourth graded run tripped at IMPORT on not_righteousness's STIFF_SCAN — fixed apart, CH28_NECK):
# blessing_and_curse RAIN_SCAN (the values naming the rain, Gerizim and Ebal: 28:12's treasure, 28:24's dust, 27:12-13's six and six), persons_poor_court HOLE_SCAN
# (27:20's father's wife, 28:31's ox and ass), second_tablets LAW_SCAN (27:25's bribe, 28:21's cleaving pestilence, 28:48's yoke on the neck). 16b's CH19_* form: a
# named tuple beside the scan and `e not in CH28_*` inside its comprehension. 17b's lesson applied: census before the run — here read after the first run tripped.
import re, subprocess, ast
ROOT = _ROOT
M = 'THE DEUTERONOMY WALK 18b (2026-09-26; LEAN)'
JOBS = [
 ('blessing_and_curse', 'RAIN_SCAN', 'CH28_RAIN', ('heavens_good_treasure_opened', 'rain_turned_to_dust', 'six_tribes_on_ebal_for_the_curse', 'six_tribes_on_gerizim_to_bless'), "chapters 27-28's names whose values name the rain, Gerizim or Ebal (28:12's good treasure giving the rain; 28:24's rain turned to dust; 27:12-13's six tribes on each mountain) — the words, not the law of 11:13-17"),
 ('persons_poor_court', 'HOLE_SCAN', 'CH28_HOLES_PP', ('fathers_wife_lier_cursed', 'ox_ass_flock_taken'), "chapters 27-28's names carrying this runner's heads (27:20's curse on the lier with his father's wife — 23:1's law cursed; 28:31's ox, ass and flock taken — 22:1-4's beasts lost by the curse)"),
 ('second_tablets', 'LAW_SCAN', 'CH28_LAW_ST', ('bribe_for_blood_taker_cursed', 'iron_yoke_on_neck', 'pestilence_cleaving'), "chapters 27-28's names carrying the words (27:25's bribe to slay cursed; 28:21's pestilence cleaving; 28:48's yoke of iron on the neck) — the curses, not chapter 10's laws"),
]
for runner, scan, ch, names, why in JOBS:
    F = f'{ROOT}/World/step9/cold_run_{runner}.py'; L = open(F, encoding='utf-8').read().split('\n')
    RX = re.compile(scan + r' = None if \w+ is None else \[e for e in \w+ if [^\]]*\]')
    k = [i for i, l in enumerate(L) if RX.search(l)]; assert len(k) == 1, (runner, scan, k)
    l = L[k[0]]; m = RX.search(l); assert ch not in l and l.count(m.group(0)) == 1
    L[k[0]] = l[:m.end() - 1] + ' and e not in ' + ch + ']' + l[m.end():] + '   # ' + M + ': ' + ch + ' excluded (the fold carried the ninety-one after the tape\'s first run; the scan census\'s section A)'
    L.insert(k[0], '%s = %r   # %s: %s' % (ch, names, M, why))
    src = '\n'.join(L); ast.parse(src); open(F, 'w', encoding='utf-8').write(src)
    print(runner, ':', L[k[0]][:200]); print('   ', L[k[0] + 1][:260])
print('SCANS WIDENED', len(JOBS))
