#!/usr/bin/env python3
# THE DEUTERONOMY WALK sitting 3 — CHAPTER 5 (2026-09-16): the sitting's scripts and prints copied from the scratchpad into
# World/step9/forms_deuteronomy_walk/ as the walk's forms — the scratch ROOT line (git rev-parse) replaced by the portable header (_ROOT from the
# file's own place), the chain's SP by a marker. Sitting 2's form (copy_ch4_forms.py).
import os, re, subprocess, shutil
ROOT = subprocess.check_output(['git', 'rev-parse', '--show-toplevel'], text=True).strip()
SP = os.path.dirname(os.path.abspath(__file__))
DST = f'{ROOT}/World/step9/forms_deuteronomy_walk'; os.makedirs(DST, exist_ok=True)
HDR = "import os as _os\n_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place\n"
PY = ['ch5_dump0.py', 'ch5_measure1.py', 'ch5_ink.py', 'ch5_rows_onkelos_a.py', 'ch5_rows_onkelos_b.py', 'ch5_rows_sifrei.py', 'write_ch5_ledger.py', 'ch5_patch_overrides.py', 'write_ch5_manifest.py', 'seat_ch5.py', 'copy_ch5_forms.py', 'write_ch5_records.py']
OUT = ['ch5_dump0.out', 'ch5_measure1.out', 'ch5_sifrei_outside.txt', 'ch5_legs.txt', 'ch5_chain.log', 'ch5_ritual_deu_05_decalogue.out', 'ch5_vt_deu_05_decalogue.out', 'ch5_close.out']
n = 0
for f in PY:
    src = f'{SP}/{f}'
    if not os.path.exists(src): print('skip (absent)', f); continue
    t = open(src, encoding='utf-8').read()
    t2 = re.sub(r"^ROOT = subprocess\.check_output\(\['git', 'rev-parse', '--show-toplevel'\], text=True\)\.strip\(\)$", "ROOT = subprocess.check_output(['git', 'rev-parse', '--show-toplevel'], text=True).strip()", t, flags=re.M)
    if t2 != t: t2 = HDR + t2
    open(f'{DST}/{f}', 'w', encoding='utf-8').write(t2); n += 1
sh = open(f'{SP}/ch5_chain.sh', encoding='utf-8').read().replace(SP, '<scratch>').replace('git -C /Users/Shared/TorahSim rev-parse --show-toplevel', 'cd "$(dirname "$0")" && git rev-parse --show-toplevel')
open(f'{DST}/ch5_chain.sh', 'w', encoding='utf-8').write(sh); n += 1
for f in OUT:
    if os.path.exists(f'{SP}/{f}'):
        t = open(f'{SP}/{f}', encoding='utf-8', errors='ignore').read().replace(SP, '<scratch>')
        open(f'{DST}/{f}', 'w', encoding='utf-8').write(t); n += 1
    else: print('skip (absent)', f)
bad = [f for f in os.listdir(DST) if SP in open(f'{DST}/{f}', encoding='utf-8', errors='ignore').read() or os.path.expanduser('~') in open(f'{DST}/{f}', encoding='utf-8', errors='ignore').read()]   # no scratch path, no home path in a copied form
assert not bad, bad
print(f'copied {n} files into {DST}; the folder holds {len(os.listdir(DST))} files')
