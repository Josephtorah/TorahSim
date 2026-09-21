#!/usr/bin/env python3
# THE DEUTERONOMY WALK sitting 11 — CHAPTER 13's READING (2026-09-21): the sitting's scripts and prints copied from the scratchpad into
# World/step9/forms_deuteronomy_walk/ as the walk's forms — the scratch ROOT line (git rev-parse) replaced by the portable header (_ROOT from the file's own
# place), the scratch path by a marker, the home path by a marker; the assert driver, the ink's parts, the timer and its table with them.
# copy_ch12_forms.py's form.
import os, re, subprocess
ROOT = _ROOT
SP = os.path.dirname(os.path.abspath(__file__))
DST = f'{ROOT}/World/step9/forms_deuteronomy_walk'; os.makedirs(DST, exist_ok=True)
HDR = "import os as _os\n_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place\n"
PY = ['derive_ch13_dump0.py', 'ch13_dump0.py', 'derive_ch13_measure1.py', 'ch13_measure1_sections.py', 'ch13_measure1.py', 'split_ch13_spine.py', 'ch13_ink_head.py', 'ch13_ink_body.py', 'ch13_ink_body_b.py', 'ch13_ink_body_c.py', 'derive_ch13_ink.py', 'ch13_ink.py', 'assert_driver.py',
      'ch13_rows_sifrei_82_86.py', 'ch13_rows_sifrei_87_92.py', 'ch13_rows_sifrei_93_96.py', 'ch13_rows_onkelos.py', 'ch13_rows_outside.py',
      'write_ch13_ledger.py', 'write_ch13_design.py', 'write_ch13_cleanpoint.py', 'derive_ch13_patch.py', 'ch13_patch_overrides.py', 'write_ch13_manifest.py', 'seat_ch13.py', 'derive_ch13_shells.py', 'write_ch13_records.py', 'copy_ch13_forms.py']
OUT = ['ch13_dump0.out', 'ch13_measure1.out', 'ch13_onkelos.txt', 'ch13_sifrei_outside.txt', 'ch13_sifrei_spine.txt', 'ch13_outside_rows.txt', 'ch13_store_glosses.txt', 'ch13_ink_run1.out', 'ch13_ink_run2.out', 'ch13_ink_run3.out', 'write_ch13_ledger.out', 'ch13_manifest.out', 'ch13_vc.out', 'ch13_labels.out',
       'ch13_chain.log', 'ch13_ritual_deu_13_seducers.out', 'ch13_vt_deu_13_seducers.out', 'ch13_fold.out', 'ch13_fold_check1.out', 'ch13_bake.out', 'ch13_build.out', 'ch13_journal.out', 'ch13_register.out', 'ch13_large_letter.out', 'ch13_home.out', 'ch13_truth.out', 'ch13_gates_SUMMARY.txt', 'ch13_gates.log', 'ch13_records_check.out', 'ch13_records_write.out',
       'ch13_chain.sh', 'ch13_fold.sh', 'ch13_gates.sh', 'tstep.sh', 'ch13_timing.tsv', 'commit_msg_ch13.txt']
home = os.path.expanduser('~')   # the records writer prints the memory folder's path (under the home) — scrubbed to the marker <home> in every copied print
n = 0
def port(src, dst):
    global n
    t = open(src, encoding='utf-8').read()
    t2 = re.sub(r"^ROOT = subprocess\.check_output\(\['git', 'rev-parse', '--show-toplevel'\], text=True\)\.strip\(\)$", "ROOT = _ROOT", t, flags=re.M)
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
files = [f for f in os.listdir(DST) if os.path.isfile(f'{DST}/{f}')]
bad = [f for f in files if SP in open(f'{DST}/{f}', encoding='utf-8', errors='ignore').read() or home in open(f'{DST}/{f}', encoding='utf-8', errors='ignore').read()]
assert not bad, bad
git = [f for f in PY if os.path.exists(f'{DST}/{f}') and re.search(r"check_output\(\['git', 'rev-parse'", open(f'{DST}/{f}', encoding='utf-8', errors='ignore').read())]
assert not git, git
print(f'copied {n} files into {DST}; the folder holds {len(files)} files')
