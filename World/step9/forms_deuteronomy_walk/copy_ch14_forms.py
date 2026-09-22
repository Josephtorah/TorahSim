#!/usr/bin/env python3
# THE DEUTERONOMY WALK sitting 12 — CHAPTER 14's READING (2026-09-21): the sitting's scripts and prints copied from the scratchpad into
# World/step9/forms_deuteronomy_walk/ as the walk's forms — the scratch ROOT line (git rev-parse) replaced by the portable header (_ROOT from the file's own
# place), the scratch path by a marker, the home path by a marker; the assert driver, the ink's parts, the timer and its table with them.
# copy_ch13_forms.py's form (the header prepended whenever the copied text names _ROOT — the form's own copy lacked it). RUN FROM THE REPO ROOT.
import os, re, subprocess
ROOT = _ROOT
SP = os.path.dirname(os.path.abspath(__file__))
DST = f'{ROOT}/World/step9/forms_deuteronomy_walk'; os.makedirs(DST, exist_ok=True)
HDR = "import os as _os\n_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place\n"
PY = ['derive_ch14_dump0.py', 'ch14_dump0.py', 'derive_ch14_measure1.py', 'ch14_measure1_sections.py', 'ch14_measure1.py', 'split_ch14_spine.py', 'ch14_ink_head.py', 'ch14_ink_body.py', 'ch14_ink_body_b.py', 'ch14_ink_body_c.py', 'derive_ch14_ink.py', 'ch14_ink.py', 'assert_driver.py',
      'ch14_rows_sifrei_96_103.py', 'ch14_rows_sifrei_104_110.py', 'ch14_rows_onkelos_a.py', 'ch14_rows_onkelos_b.py', 'ch14_rows_outside.py',
      'write_ch14_ledger.py', 'write_ch14_design.py', 'write_ch14_cleanpoint.py', 'derive_ch14_patch.py', 'ch14_patch_overrides.py', 'write_ch14_manifest.py', 'seat_ch14.py', 'derive_ch14_shells.py', 'write_ch14_records.py', 'copy_ch14_forms.py']
OUT = ['ch14_dump0.out', 'ch14_measure1.out', 'ch14_onkelos.txt', 'ch14_sifrei_outside.txt', 'ch14_sifrei_spine.txt', 'ch14_outside_rows.txt', 'ch14_store_glosses.txt', 'ch14_ink_run1.out', 'ch14_ink_run2.out', 'ch14_ink_run3.out', 'ch14_ink_run4.out', 'ch14_ink_run5.out', 'ch14_ink_run6.out', 'write_ch14_ledger.out', 'ch14_patch.out', 'ch14_manifest.out', 'ch14_vc.out', 'ch14_labels.out',
       'ch14_chain.log', 'ch14_ritual_deu_14_food_tithe.out', 'ch14_vt_deu_14_food_tithe.out', 'ch14_fold.out', 'ch14_fold_check1.out', 'ch14_bake.out', 'ch14_build.out', 'ch14_journal.out', 'ch14_register.out', 'ch14_large_letter.out', 'ch14_home.out', 'ch14_truth.out', 'ch14_gates_SUMMARY.txt', 'ch14_gates.log', 'ch14_records_check.out', 'ch14_records_write.out',
       'ch14_chain.sh', 'ch14_fold.sh', 'ch14_gates.sh', 'tstep.sh', 'ch14_timing.tsv', 'commit_msg_ch14.txt'] + [f'ch14_spine_p{p}.txt' for p in range(96, 111)]
home = os.path.expanduser('~')   # the records writer prints the memory folder's path (under the home) — scrubbed to the marker <home> in every copied print
n = 0
def port(src, dst):
    global n
    t = open(src, encoding='utf-8').read()
    t2 = re.sub(r"^ROOT = subprocess\.check_output\(\['git', 'rev-parse', '--show-toplevel'\], text=True\)\.strip\(\)$", "ROOT = _ROOT", t, flags=re.M)
    t2 = re.sub(r"(?:__import__\('subprocess'\)|subprocess|_sp)\.check_output\(\['git', 'rev-parse', '--show-toplevel'\], text=True\)\.strip\(\)", "_ROOT", t2)
    if '_ROOT' in t2 and '_ROOT = _os.path.normpath' not in t2: t2 = HDR + t2
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
files = [f for f in os.listdir(DST) if os.path.isfile(f'{DST}/{f}')]
bad = [f for f in files if SP in open(f'{DST}/{f}', encoding='utf-8', errors='ignore').read() or home in open(f'{DST}/{f}', encoding='utf-8', errors='ignore').read()]
assert not bad, bad
git = [f for f in PY if os.path.exists(f'{DST}/{f}') and re.search(r"check_output\(\['git', 'rev-parse'", open(f'{DST}/{f}', encoding='utf-8', errors='ignore').read())]
assert not git, git
noroot = [f for f in PY if os.path.exists(f'{DST}/{f}') and 'ROOT = _ROOT' in open(f'{DST}/{f}', encoding='utf-8').read() and '_ROOT = _os.path.normpath' not in open(f'{DST}/{f}', encoding='utf-8').read()]
assert not noroot, noroot
print(f'copied {n} files into {DST}; the folder holds {len(files)} files')
