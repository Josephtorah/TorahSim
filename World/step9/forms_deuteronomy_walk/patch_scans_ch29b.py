import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE DEUTERONOMY WALK 19b (2026-09-27; LEAN) — RUN B, THE SECOND SCAN PATCH: good_land's GARMENT_SCAN — the fast checker's third pass tripped AT IMPORT (the first row covenant_words_keeping_commanded's value named 'the garment'; the scan census's section A had not listed good_land's scan — a lesson: the census's list of runner scans is incomplete, the fast checker the second reader). THE IMPORT-TIME HOLE SCANS WIDENED BY NAME for the row the fold carries after the tape's first run whose VALUE named the
# stiff neck (the scan census's section A: not_righteousness STIFF_SCAN and second_tablets LAW_SCAN both name book_a_witness_against_israel — 31:26-27's 'a witness against you …
# your stiff neck'); the value REWORDED in the daemon at the second pass (the tape's CU7 and DA6 read the running world) and the name EXCLUDED here so the fold's first rows never
# trip the import (18b's lesson 1: the runner's fourth graded run tripped at IMPORT on this very scan). 16b's CH19_* form: a named tuple beside the scan and `e not in CH31_*`
# inside its comprehension. 18b's patch_scans_ch26.py the form. RUN FROM THE REPO ROOT.
import re, subprocess, ast
ROOT = _ROOT
M = 'THE DEUTERONOMY WALK 19b (2026-09-27; LEAN)'
JOBS = [
 ('good_land', 'GARMENT_SCAN', 'CH31_GARMENT', ('covenant_words_keeping_commanded',), "chapter 29's name whose first value named the garment (29:8's keep the words of this covenant — the recital's retelling of 29:4's garments; the value reworded at 19b's second pass) — the covenant's command, not 8:4's state"),
]
for runner, scan, ch, names, why in JOBS:
    F = f'{ROOT}/World/step9/cold_run_{runner}.py'; L = open(F, encoding='utf-8').read().split('\n')
    RX = re.compile(scan + r' = None if \w+ is None else \[e for e in \w+ if [^\]]*\]')
    k = [i for i, l in enumerate(L) if RX.search(l)]; assert len(k) == 1, (runner, scan, k)
    l = L[k[0]]; m = RX.search(l); assert ch not in l and l.count(m.group(0)) == 1
    L[k[0]] = l[:m.end() - 1] + ' and e not in ' + ch + ']' + l[m.end():] + '   # ' + M + ': ' + ch + ' excluded (the fold carried the fifty-nine after the tape\'s first run; the scan census\'s section A)'
    L.insert(k[0], '%s = %r   # %s: %s' % (ch, names, M, why))
    src = '\n'.join(L); ast.parse(src); open(F, 'w', encoding='utf-8').write(src)
    print(runner, ':', L[k[0]][:200]); print('   ', L[k[0] + 1][:260])
print('SCANS WIDENED', len(JOBS))
