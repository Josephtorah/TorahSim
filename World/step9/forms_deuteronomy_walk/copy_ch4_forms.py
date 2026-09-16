import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE DEUTERONOMY WALK sitting 2 — CHAPTER 4 (2026-09-16): the sitting's scripts and prints copied from the scratchpad into
# World/step9/forms_deuteronomy_walk/ as the walk's forms — the scratch ROOT line (git rev-parse) replaced by the portable header (_ROOT from the
# file's own place), the chain's SP by a marker. Sitting 1's form (copy_deu_forms.py).
import os, re, subprocess, shutil
ROOT = _ROOT
SP = os.path.dirname(os.path.abspath(__file__))
DST = f'{ROOT}/World/step9/forms_deuteronomy_walk'; os.makedirs(DST, exist_ok=True)
HDR = "import os as _os\n_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place\n"
PY = ['ch4_dump0.py', 'ch4_measure1.py', 'ch4_measure2.py', 'ch4_ink.py', 'ch4_rows_onkelos_a.py', 'ch4_rows_onkelos_b.py', 'ch4_rows_sifrei.py', 'write_ch4_ledger.py', 'ch4_patch_overrides.py', 'write_ch4_manifest.py', 'seat_ch4.py', 'copy_ch4_forms.py', 'write_ch4_records.py']
OUT = ['ch4_dump0.out', 'ch4_measure1_b.out', 'ch4_measure2.out', 'ch4_sifrei_outside.txt', 'legs1.txt', 'ch4_chain.log', 'ch4_ritual_deu_04_obey_horeb.out', 'ch4_ritual_deu_04_refuge_east.out', 'ch4_vt_deu_04_obey_horeb.out', 'ch4_vt_deu_04_refuge_east.out', 'ch4_close.out']
n = 0
for f in PY:
    src = f'{SP}/{f}'
    if not os.path.exists(src): print('skip (absent)', f); continue
    t = open(src, encoding='utf-8').read()
    t2 = re.sub(r"^ROOT = subprocess\.check_output\(\['git', 'rev-parse', '--show-toplevel'\], text=True\)\.strip\(\)$", "ROOT = _ROOT", t, flags=re.M)
    if t2 != t: t2 = HDR + t2
    open(f'{DST}/{f}', 'w', encoding='utf-8').write(t2); n += 1
sh = open(f'{SP}/ch4_chain.sh', encoding='utf-8').read().replace(SP, '<scratch>').replace('git -C /Users/Shared/TorahSim rev-parse --show-toplevel', 'cd "$(dirname "$0")" && git rev-parse --show-toplevel')
open(f'{DST}/ch4_chain.sh', 'w', encoding='utf-8').write(sh); n += 1
for f in OUT:
    if os.path.exists(f'{SP}/{f}'):
        t = open(f'{SP}/{f}', encoding='utf-8', errors='ignore').read().replace(SP, '<scratch>')
        open(f'{DST}/{f}', 'w', encoding='utf-8').write(t); n += 1
    else: print('skip (absent)', f)
bad = [f for f in os.listdir(DST) if SP in open(f'{DST}/{f}', encoding='utf-8', errors='ignore').read() or os.path.expanduser('~') in open(f'{DST}/{f}', encoding='utf-8', errors='ignore').read()]   # no scratch path, no home path in a copied form
assert not bad, bad
print(f'copied {n} files into {DST}; the folder holds {len(os.listdir(DST))} files')
