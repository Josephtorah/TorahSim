#!/usr/bin/env python3
import os as _os, subprocess as _sp
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
# THE DEUTERONOMY WALK sitting 5b — THE COMPILE OF CHAPTER 7 (2026-09-18): the sitting's scripts and prints copied from the scratchpad into
# World/step9/forms_deuteronomy_walk/ as the walk's forms — the scratch ROOT line (git rev-parse) replaced by the portable header (_ROOT from the
# file's own place), the scratch path by a marker, the home path by a marker; the recorder and the stitcher copied under their sitting's names; the
# docket's four parts (read whole from the start — no overlay) and the four row prints ride with them. copy_ch6b_forms.py's form.
import os, re, subprocess
ROOT = _ROOT
SP = os.path.dirname(os.path.abspath(__file__))
DST = f'{ROOT}/World/step9/forms_deuteronomy_walk'; os.makedirs(DST, exist_ok=True)
HDR = "import os as _os\n_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place\n"
PY = ['ch7_compile_recon.py', 'ch7_docket_scan.py', 'ch7_docket_rows.py', 'ch7_docket_common.py', 'ch7_docket_A.py', 'ch7_docket_B.py', 'ch7_docket_C.py',
      'ch7_docket_D.py', 'write_ch7_docket.py', 'close_ch7_run2.py', 'write_ch7b_design.py', 'add_types_ch7.py', 'ch7_callees.py', 'ch7_part1.py', 'ch7_part2.py',
      'ch7_part3.py', 'ch7_part3b.py', 'ch7_part4.py', 'ch7_cases_gen.py', 'ch7_assemble.py', 'ch7_fastcheck.py', 'seq_record_ch7.py', 'seq_stitch_ch7.py',
      'patch_seq_literals_ch7.py', 'add_pointers_ch7.py', 'write_ch7b_records.py', 'copy_ch7b_forms.py']
OUT = ['ch7_recon.out', 'ch7_scan.out', 'ch7_docket_dump.txt', 'ch7_rows_A.txt', 'ch7_rows_B.txt', 'ch7_rows_C.txt', 'ch7_rows_D.txt', 'ch7_docket_write.out',
       'ch7b_probes_fail.out', 'ch7_callees.out', 'ch7_fastcheck1.out', 'ch7_cases_gen.out', 'ch7_run1.out', 'seq_record_ch7.out', 'seq_stitch_ch7.out',
       'patch_seq_literals_ch7.out', 'ch7_tape1.out', 'ch7_tape2.out', 'ch7_checkpoint_check.out', 'ch7b_probes_run3.out', 'ch7b_chain.log',
       'ch7b_records_check.out', 'ch7b_records_write.out', 'add_pointers_ch7.out', 'ch7b_chain2.log', 'ch7b_chain_SUMMARY_first.txt', 'ch7b_chain_dependency_first.out']
GATES = 'gates_ch7b'   # the chain's folder — every step's print and the SUMMARY
home = os.path.expanduser('~')   # the records writer prints the memory folder's path (under the home) — scrubbed to the marker <home> in every copied print
n = 0
def port(src, dst):
    global n
    t = open(src, encoding='utf-8').read()
    t2 = re.sub(r"^ROOT = subprocess\.check_output\(\['git', 'rev-parse', '--show-toplevel'\], text=True\)\.strip\(\)$", "ROOT = _ROOT", t, flags=re.M)
    t2 = re.sub(r"^_ROOT = __import__\('subprocess'\)\.check_output\(\['git', 'rev-parse', '--show-toplevel'\], text=True\)\.strip\(\)(.*)$", "_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place", t2, flags=re.M)
    t2 = re.sub(r"^_ROOT = _sp\.check_output\(\['git', 'rev-parse', '--show-toplevel'\], text=True\)\.strip\(\)(.*)$", "_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place", t2, flags=re.M)
    # any remaining git-root call inside a longer line (a scratch script's 'SP = …; ROOT = subprocess.check_output(…)' form) becomes the portable root
    t2 = re.sub(r"(?:__import__\('subprocess'\)|subprocess|_sp)\.check_output\(\['git', 'rev-parse', '--show-toplevel'\], text=True\)\.strip\(\)", "_ROOT", t2)
    if t2 != t and '_ROOT = _os.path.normpath' not in t2: t2 = HDR + t2
    t2 = t2.replace(SP, '<scratch>').replace(home, '<home>')
    open(dst, 'w', encoding='utf-8').write(t2); n += 1
for f in PY:
    src = f'{SP}/{f}'
    if not os.path.exists(src): print('skip (absent)', f); continue
    port(src, f'{DST}/{f}')
for f in OUT:
    if os.path.exists(f'{SP}/{f}'):
        t = open(f'{SP}/{f}', encoding='utf-8', errors='ignore').read().replace(SP, '<scratch>').replace(home, '<home>')
        open(f'{DST}/{f}', 'w', encoding='utf-8').write(t); n += 1
    else: print('skip (absent)', f)
g = f'{SP}/{GATES}'
if os.path.isdir(g):
    for f in sorted(os.listdir(g)):
        t = open(f'{g}/{f}', encoding='utf-8', errors='ignore').read().replace(SP, '<scratch>').replace(home, '<home>')
        open(f'{DST}/gates_ch7b_{f}', 'w', encoding='utf-8').write(t); n += 1
files = [f for f in os.listdir(DST) if os.path.isfile(f'{DST}/{f}')]   # directories skipped, never read
bad = [f for f in files if SP in open(f'{DST}/{f}', encoding='utf-8', errors='ignore').read() or home in open(f'{DST}/{f}', encoding='utf-8', errors='ignore').read()]   # no scratch path, no home path in a copied form
assert not bad, bad
git = [f for f in PY if os.path.exists(f'{DST}/{f}') and re.search(r"check_output\(\['git', 'rev-parse'", open(f'{DST}/{f}', encoding='utf-8', errors='ignore').read())]   # no git root in a form copied THIS sitting (the older forms' lines stand as they were)
assert not git, git
print(f'copied {n} files into {DST}; the folder holds {len(files)} files')
