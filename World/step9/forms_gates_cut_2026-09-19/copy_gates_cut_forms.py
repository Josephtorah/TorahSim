#!/usr/bin/env python3
import os as _os, subprocess as _sp
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
# THE GATES CUT (2026-09-19): the cut's instruments and prints copied from the scratchpad into
# World/step9/forms_deuteronomy_walk/ as the walk's forms — the scratch ROOT line (git rev-parse) replaced by the portable header (_ROOT from the
# file's own place), the scratch path by a marker, the home path by a marker; the recorder and the stitcher copied under their sitting's names; the
# docket's instruments were copied at the docket's own run (write_ch8_docket_records.py's step); RUN B's scripts and prints here. copy_ch7b_forms.py's form.
import os, re, subprocess
ROOT = _ROOT
SP = os.path.dirname(os.path.abspath(__file__))
DST = f'{ROOT}/World/step9/forms_gates_cut_2026-09-19'; os.makedirs(DST, exist_ok=True)
HDR = "import os as _os\n_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place\n"
PY = ['snapshot_test.py', 'write_gates_cut_records.py', 'patch_writer_two_chains.py', 'copy_gates_cut_forms.py']
OUT = ['snapshot_test.out', 'gates_cut_1.log', 'gates_cut_1.start', 'gates_cut_2.log', 'gates_cut_2.start', 'gates_cut_records_check.out', 'gates_cut_records_write.out', 'journal_stamp_test.json', 'gates_chain_before.sh',
       'positions_incremental_test.out', 'positions_incremental_moved_test.out', 'positions_incremental_moved_test2.out', 'positions_workers_test.out']   # the struck form's own test prints — the evidence
GATES = 'gates_cut_1'   # the chain's folder — every step's print and the SUMMARY
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
for GATES in ('gates_cut_1', 'gates_cut_2'):   # both chains' folders — the first everything in full, the second the steady state
    g = f'{SP}/{GATES}'
    if os.path.isdir(g):
        for f in sorted(os.listdir(g)):
            t = open(f'{g}/{f}', encoding='utf-8', errors='ignore').read().replace(SP, '<scratch>').replace(home, '<home>')
            open(f'{DST}/{GATES}_{f}', 'w', encoding='utf-8').write(t); n += 1
files = [f for f in os.listdir(DST) if os.path.isfile(f'{DST}/{f}')]   # directories skipped, never read
bad = [f for f in files if SP in open(f'{DST}/{f}', encoding='utf-8', errors='ignore').read() or home in open(f'{DST}/{f}', encoding='utf-8', errors='ignore').read()]   # no scratch path, no home path in a copied form
assert not bad, bad
git = [f for f in PY if os.path.exists(f'{DST}/{f}') and re.search(r"check_output\(\['git', 'rev-parse'", open(f'{DST}/{f}', encoding='utf-8', errors='ignore').read())]   # no git root in a form copied THIS sitting (the older forms' lines stand as they were)
assert not git, git
print(f'copied {n} files into {DST}; the folder holds {len(files)} files')
