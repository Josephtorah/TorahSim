#!/usr/bin/env python3
# THE VERIFIED-IMPORT CACHE (2026-09-19): the instruments and prints copied from the scratchpad into World/step9/forms_gates_cut_2026-09-19/ under
# cache_* names — the scratch ROOT line replaced by the portable header, the scratch path and the home path by markers; the third chain's folder whole.
import os, re, subprocess
ROOT = _ROOT
SP = os.path.dirname(os.path.abspath(__file__))
DST = f'{ROOT}/World/step9/forms_gates_cut_2026-09-19'; assert os.path.isdir(DST)
HDR = "import os as _os\n_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place\n"
PY = ['stmt_profile.py', 'w_diag.py', 'c2_diag.py', 'w_canon.py', 'name_diff.py', 'name_diff2.py', 'mutables_scan.py', 'write_cache_records.py', 'copy_cache_forms.py']
OUT = ['importtime.txt', 'nd_full.json', 'nd_cached.json', 'cache_probes_final.out', 'cache_records_check.out', 'cache_records_write.out']
home = os.path.expanduser('~'); n = 0
def scrub(t): return t.replace(SP, '<scratch>').replace(home, '<home>')
for f in PY:
    src = f'{SP}/{f}'
    if not os.path.exists(src): print('skip (absent)', f); continue
    t = open(src, encoding='utf-8').read()
    t2 = re.sub(r"(?:__import__\('subprocess'\)|subprocess|_sp)\.check_output\(\['git', ?'rev-parse', ?'--show-toplevel'\], text=True\)\.strip\(\)", "_ROOT", t)
    if t2 != t and '_ROOT = _os.path.normpath' not in t2: t2 = HDR + t2
    open(f'{DST}/cache_{f}', 'w', encoding='utf-8').write(scrub(t2)); n += 1
for f in OUT:
    src = f'{SP}/{f}'
    if not os.path.exists(src): print('skip (absent)', f); continue
    open(f'{DST}/cache_{f}', 'w', encoding='utf-8').write(scrub(open(src, encoding='utf-8', errors='ignore').read())); n += 1
g = f'{SP}/gates_cut_3'; os.makedirs(f'{DST}/gates_cut_3', exist_ok=True)
for f in sorted(os.listdir(g)):
    if f.endswith('.rc'): continue
    open(f'{DST}/gates_cut_3/{f}', 'w', encoding='utf-8').write(scrub(open(f'{g}/{f}', encoding='utf-8', errors='ignore').read())); n += 1
bad = [f for f in os.listdir(DST) if os.path.isfile(f'{DST}/{f}') and (SP in open(f'{DST}/{f}', encoding='utf-8', errors='ignore').read() or home in open(f'{DST}/{f}', encoding='utf-8', errors='ignore').read())]
assert not bad, bad
print('copied %d files into %s (no scratch path, no home path)' % (n, DST.replace(ROOT, '<repo>')))
