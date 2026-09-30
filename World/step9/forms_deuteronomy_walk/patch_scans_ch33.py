import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE DEUTERONOMY WALK 21b (2026-09-29; LEAN) — RUN B, THE SCAN PATCH: blessing_and_curse's RAIN_SCAN — THE SCAN CENSUS's section A (ch33_scan_census.out) read after the tape's first
# run: the one runner whose import-time hole scan names one of this sitting's twenty-eight — the_lord_came_from_sinai_seir_paran_declared (33:2 'He shone from mount PARAN'): the scan's
# rain\w* reads the letters r-a-n inside PARAN — a homograph of letters, no rain in the name (33:28's dew a different word, unmatched); the name EXCLUDED here so the fold's row never
# trips the import (18b's lesson 1; 20b's patch_scans_ch32.py the form: a named tuple beside the scan and `e not in CH33_*` inside its comprehension). RUN FROM THE REPO ROOT.
import re, subprocess, ast
ROOT = _ROOT
M = 'THE DEUTERONOMY WALK 21b (2026-09-29; LEAN)'
JOBS = [
 ('blessing_and_curse', 'RAIN_SCAN', 'CH33_RAIN', ('the_lord_came_from_sinai_seir_paran_declared',), "chapter 33's name whose letters spell the rain — mount PARAN (33:2 'He shone from mount Paran', the theophany's third mountain) inside the effect's name: the scan's rain\\w* reads the letters r-a-n in 'paran', a homograph of letters, no rain (33:28's dew a different word) — the scan census's section A after the tape's first run"),
]
for runner, scan, ch, names, why in JOBS:
    F = f'{ROOT}/World/step9/cold_run_{runner}.py'; L = open(F, encoding='utf-8').read().split('\n')
    RX = re.compile(scan + r' = None if \w+ is None else \[e for e in \w+ if [^\]]*\]')
    k = [i for i, l in enumerate(L) if RX.search(l)]; assert len(k) == 1, (runner, scan, k)
    l = L[k[0]]; m = RX.search(l); assert ch not in l and l.count(m.group(0)) == 1
    L[k[0]] = l[:m.end() - 1] + ' and e not in ' + ch + ']' + l[m.end():] + '   # ' + M + ': ' + ch + ' excluded (the fold carries the twenty-eight after the tape\'s first run; the scan census\'s section A)'
    L.insert(k[0], '%s = %r   # %s: %s' % (ch, names, M, why))
    src = '\n'.join(L); ast.parse(src); open(F, 'w', encoding='utf-8').write(src)
    print(runner, ':', L[k[0]][:220]); print('   ', L[k[0] + 1][:300])
print('SCANS WIDENED', len(JOBS))
