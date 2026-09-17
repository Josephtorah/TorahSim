import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE DEUTERONOMY WALK sitting 3b — THE COMPILE OF CHAPTER 5 (2026-09-16): the sitting's scripts and prints copied from the scratchpad into
# World/step9/forms_deuteronomy_walk/ as the walk's forms — the scratch ROOT line (git rev-parse) replaced by the portable header (_ROOT from the
# file's own place), the scratch path by a marker; the recorder and the stitcher copied under their sitting's names. copy_ch4b_forms.py's form.
import os, re, subprocess
ROOT = _ROOT
SP = os.path.dirname(os.path.abspath(__file__))
DST = f'{ROOT}/World/step9/forms_deuteronomy_walk'; os.makedirs(DST, exist_ok=True)
HDR = "import os as _os\n_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place\n"
PY = ['ch5_compile_recon.py', 'ch5_docket_scan.py', 'ch5_docket_rows.py', 'ch5_docket_A.py', 'ch5_docket_B.py', 'ch5_docket_C.py', 'ch5_docket_D.py',
      'write_ch5_docket.py', 'add_types_ch5.py', 'ch5_callees.py', 'ch5_part1.py', 'ch5_part2.py', 'ch5_part3.py', 'ch5_part4.py', 'ch5_cases_gen.py',
      'ch5_assemble.py', 'ch5_fastcheck.py', 'patch_seq_literals_ch5.py', 'patch_rest_closes_ch5.py', 'declare_ch5_seats.py', 'add_pointers_ch5.py', 'write_ch5b_design.py',
      'write_ch5b_records.py', 'copy_ch5b_forms.py', 'seq_record_ch5.py', 'seq_stitch_ch5.py']
OUT = ['ch5_compile_recon.out', 'ch5_docket_dump.txt', 'ch5_docket_scan.out', 'ch5_callees.out', 'ch5_cases_gen.out', 'ch5_run1.out', 'seq_record_ch5.out',
       'seq_stitch_ch5.out', 'checkpoint_check_ch5.out', 'tape_run_ch5_1.out', 'tape_run_ch5_2.out', 'tape_run_ch5_3.out', 'readback_probes_ch5_fail.out', 'daemon_gate_ch5_fail.out', 'dependency_gate_ch5_fail.out',
       'daemon_gate_ch5_2.out', 'dependency_gate_ch5_2.out', 'gates_fail_ch5.log']
GATES = 'gates_ch5'   # the chain's folder — every step's print and the SUMMARY
n = 0
def port(src, dst):
    global n
    t = open(src, encoding='utf-8').read()
    t2 = re.sub(r"^ROOT = subprocess\.check_output\(\['git', 'rev-parse', '--show-toplevel'\], text=True\)\.strip\(\)$", "ROOT = _ROOT", t, flags=re.M)
    t2 = re.sub(r"^_ROOT = __import__\('subprocess'\)\.check_output\(\['git', 'rev-parse', '--show-toplevel'\], text=True\)\.strip\(\)$", "_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place", t2, flags=re.M)
    t2 = re.sub(r"^_ROOT = _sp\.check_output\(\['git', 'rev-parse', '--show-toplevel'\], text=True\)\.strip\(\)(.*)$", "_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place", t2, flags=re.M)
    if t2 != t and not t2.startswith('import os as _os'): t2 = HDR + t2
    t2 = t2.replace(SP, '<scratch>')
    open(dst, 'w', encoding='utf-8').write(t2); n += 1
for f in PY:
    src = f'{SP}/{f}'
    if not os.path.exists(src): print('skip (absent)', f); continue
    port(src, f'{DST}/{f}')
for f in OUT:
    if os.path.exists(f'{SP}/{f}'):
        t = open(f'{SP}/{f}', encoding='utf-8', errors='ignore').read().replace(SP, '<scratch>')
        open(f'{DST}/{f}', 'w', encoding='utf-8').write(t); n += 1
    else: print('skip (absent)', f)
g = f'{SP}/{GATES}'
if os.path.isdir(g):
    for f in sorted(os.listdir(g)):
        t = open(f'{g}/{f}', encoding='utf-8', errors='ignore').read().replace(SP, '<scratch>')
        open(f'{DST}/gates_ch5_{f}', 'w', encoding='utf-8').write(t); n += 1
home = os.path.expanduser('~')
bad = [f for f in os.listdir(DST) if SP in open(f'{DST}/{f}', encoding='utf-8', errors='ignore').read() or home in open(f'{DST}/{f}', encoding='utf-8', errors='ignore').read()]   # no scratch path, no home path in a copied form
assert not bad, bad
print(f'copied {n} files into {DST}; the folder holds {len(os.listdir(DST))} files')
