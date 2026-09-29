import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE DEUTERONOMY WALK 20b (2026-09-28; LEAN) — RUN B, THE SCAN PATCH: blessing_and_curse's RAIN_SCAN — THE SCAN CENSUS's section A (ch32_scan_census.out) read after the tape's first
# run: the one runner whose import-time hole scan names one of this sitting's forty-two — doctrine_as_rain_and_dew_likened (32:2 'my doctrine shall drop as the rain' — the four
# rains words of Torah) matches RAIN_WORDS's rain\w*; the name EXCLUDED here so the fold's row never trips the import (18b's lesson 1; 19b's patch_scans_ch29.py the form: a named
# tuple beside the scan and `e not in CH32_*` inside its comprehension); the sequence's DC4 retyped beside it (patch_tape_retypes_ch32.py). RUN FROM THE REPO ROOT.
import re, subprocess, ast
ROOT = _ROOT
M = 'THE DEUTERONOMY WALK 20b (2026-09-28; LEAN)'
JOBS = [
 ('blessing_and_curse', 'RAIN_SCAN', 'CH32_RAIN', ('doctrine_as_rain_and_dew_likened',), "chapter 32's name whose value names the rain (32:2 'my doctrine shall drop as the rain, my speech distil as the dew' — the song's likening, the Sifrei 306:16-35's four rains words of Torah; the rains' dates the runner's own DATA by CALL) — the song's doctrine, not 11:14's rain: the scan census's section A after the tape's first run"),
]
for runner, scan, ch, names, why in JOBS:
    F = f'{ROOT}/World/step9/cold_run_{runner}.py'; L = open(F, encoding='utf-8').read().split('\n')
    RX = re.compile(scan + r' = None if \w+ is None else \[e for e in \w+ if [^\]]*\]')
    k = [i for i, l in enumerate(L) if RX.search(l)]; assert len(k) == 1, (runner, scan, k)
    l = L[k[0]]; m = RX.search(l); assert ch not in l and l.count(m.group(0)) == 1
    L[k[0]] = l[:m.end() - 1] + ' and e not in ' + ch + ']' + l[m.end():] + '   # ' + M + ': ' + ch + ' excluded (the fold carried the forty-two after the tape\'s first run; the scan census\'s section A)'
    L.insert(k[0], '%s = %r   # %s: %s' % (ch, names, M, why))
    src = '\n'.join(L); ast.parse(src); open(F, 'w', encoding='utf-8').write(src)
    print(runner, ':', L[k[0]][:200]); print('   ', L[k[0] + 1][:260])
print('SCANS WIDENED', len(JOBS))
