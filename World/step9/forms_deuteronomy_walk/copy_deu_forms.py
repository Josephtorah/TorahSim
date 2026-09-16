import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE DEUTERONOMY WALK sitting 1 (2026-09-15): the sitting's scripts copied from the scratchpad into World/step9/forms_deuteronomy_walk/ as the
# walk's forms — the scratch ROOT line (git rev-parse) replaced by the portable header (_ROOT from the file's own place), the chain's SP by a
# marker. Sitting 15's form (the copy step of write_ref_records.py), lifted into its own script.
import os, re, subprocess, shutil
ROOT = _ROOT
SP = os.path.dirname(os.path.abspath(__file__))
DST = f'{ROOT}/World/step9/forms_deuteronomy_walk'; os.makedirs(DST, exist_ok=True)
HDR = "import os as _os\n_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place\n"
PY = ['deu_dump0.py', 'deu_parser0.py', 'deu_measure0.py', 'deu_measure1.py', 'deu_measure2.py', 'deu_ink.py', 'assert_driver.py', 'deu_legs.py', 'deu_rows_onkelos_a.py', 'deu_rows_onkelos_b.py', 'deu_rows_onkelos_c.py', 'deu_rows_sifrei_a.py', 'deu_rows_sifrei_b.py', 'deu_rows_sifrei_c.py', 'deu_rows_sifrei_d.py', 'write_deu_ledger.py', 'patch_overrides_deu.py', 'write_deu_manifest.py', 'seat_deu.py', 'copy_deu_forms.py', 'write_deu_records.py']
n = 0
for f in PY:
    src = f'{SP}/{f}'
    if not os.path.exists(src): print('skip (absent)', f); continue
    t = open(src, encoding='utf-8').read()
    t2 = re.sub(r"^ROOT = subprocess\.check_output\(\['git', 'rev-parse', '--show-toplevel'\], text=True\)\.strip\(\)$", "ROOT = _ROOT", t, flags=re.M)
    if t2 != t: t2 = HDR + t2
    open(f'{DST}/{f}', 'w', encoding='utf-8').write(t2); n += 1
sh = open(f'{SP}/deu_chain.sh', encoding='utf-8').read().replace(SP, '<scratch>').replace('git -C /Users/Shared/TorahSim rev-parse --show-toplevel', 'cd "$(dirname "$0")" && git rev-parse --show-toplevel')
open(f'{DST}/deu_chain.sh', 'w', encoding='utf-8').write(sh); n += 1
for f in ('legs1.txt', 'legs2.txt', 'legs3.txt', 'legs4.txt', 'legs5.txt'):
    if os.path.exists(f'{SP}/{f}'): shutil.copy(f'{SP}/{f}', f'{DST}/{f}'); n += 1
bad = [f for f in os.listdir(DST) if SP in open(f'{DST}/{f}', encoding='utf-8', errors='ignore').read() or os.path.expanduser('~') in open(f'{DST}/{f}', encoding='utf-8', errors='ignore').read()]   # no scratch path, no home path in a copied form
assert not bad, bad
print(f'copied {n} files into {DST}')
