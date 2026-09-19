#!/usr/bin/env python3
import os as _os, subprocess as _sp
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
# THE DEUTERONOMY WALK sitting 6b — THE COMPILE OF CHAPTER 8, RUN B (2026-09-19): the sitting's scripts and prints copied from the scratchpad into
# World/step9/forms_deuteronomy_walk/ as the walk's forms — the scratch ROOT line (git rev-parse) replaced by the portable header (_ROOT from the
# file's own place), the scratch path by a marker, the home path by a marker; the recorder and the stitcher copied under their sitting's names; the
# docket's instruments were copied at the docket's own run (write_ch8_docket_records.py's step); RUN B's scripts and prints here. copy_ch7b_forms.py's form.
import os, re, subprocess
ROOT = _ROOT
SP = os.path.dirname(os.path.abspath(__file__))
DST = f'{ROOT}/World/step9/forms_deuteronomy_walk'; os.makedirs(DST, exist_ok=True)
HDR = "import os as _os\n_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place\n"
PY = ['derive_ch9_dump0.py', 'ch9_dump0.py', 'derive_ch9_measure1.py', 'ch9_measure1_sections.py', 'ch9_measure1.py', 'ch9_ink.py', 'ch9_ink_diag.py', 'ch9_rows_onkelos_a.py', 'ch9_rows_onkelos_b.py', 'ch9_rows_outside.py',
      'write_ch9_ledger.py', 'ch9_patch_overrides.py', 'write_ch9_manifest.py', 'seat_ch9.py', 'write_ch9_design.py', 'write_ch9_records.py', 'copy_ch9_forms.py']
OUT = ['ch9_dump0.out', 'ch9_measure1.out', 'ch9_onkelos.txt', 'ch9_sifrei_outside.txt', 'ch9_store_glosses.txt', 'ch9_ink_run1.out', 'ch9_ink_run2.out', 'ch9_ink_run3.out', 'ch9_manifest.out',
       'ch9_chain.log', 'ch9_ritual_deu_09_not_righteousness.out', 'ch9_vt_deu_09_not_righteousness.out', 'ch9_vc.out', 'ch9_labels.out', 'ch9_fold.out', 'ch9_fold_check1.out', 'ch9_bake.out', 'ch9_build.out', 'ch9_journal.out', 'ch9_register.out', 'ch9_large_letter.out', 'ch9_home.out', 'ch9_truth.out', 'ch9_gates_SUMMARY.txt', 'ch9_gates.log', 'ch9_records_check.out', 'ch9_records_write.out', 'ch9_chain.sh', 'ch9_fold.sh', 'ch9_gates.sh']
GATES = 'none'   # the reading's chain prints are named in OUT
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
        open(f'{DST}/gates_ch9_{f}', 'w', encoding='utf-8').write(t); n += 1
files = [f for f in os.listdir(DST) if os.path.isfile(f'{DST}/{f}')]   # directories skipped, never read
bad = [f for f in files if SP in open(f'{DST}/{f}', encoding='utf-8', errors='ignore').read() or home in open(f'{DST}/{f}', encoding='utf-8', errors='ignore').read()]   # no scratch path, no home path in a copied form
assert not bad, bad
git = [f for f in PY if os.path.exists(f'{DST}/{f}') and re.search(r"check_output\(\['git', 'rev-parse'", open(f'{DST}/{f}', encoding='utf-8', errors='ignore').read())]   # no git root in a form copied THIS sitting (the older forms' lines stand as they were)
assert not git, git
print(f'copied {n} files into {DST}; the folder holds {len(files)} files')
