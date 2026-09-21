#!/usr/bin/env python3
# THE DEUTERONOMY WALK sitting 10 — CHAPTER 12's READING (2026-09-20): the sitting's scripts and prints copied from the scratchpad into
# World/step9/forms_deuteronomy_walk/ as the walk's forms — the scratch ROOT line (git rev-parse) replaced by the portable header (_ROOT from the file's own
# place), the scratch path by a marker, the home path by a marker; the assert driver, the ink's parts, the timer and its table with them.
# copy_ch11_forms.py's form.
import os, re, subprocess
ROOT = _ROOT
SP = os.path.dirname(os.path.abspath(__file__))
DST = f'{ROOT}/World/step9/forms_deuteronomy_walk'; os.makedirs(DST, exist_ok=True)
HDR = "import os as _os\n_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place\n"
PY = ['derive_ch12_dump0.py', 'ch12_dump0.py', 'derive_ch12_measure1.py', 'ch12_measure1_sections.py', 'ch12_measure1.py', 'split_ch12_spine.py', 'ch12_ink_head.py', 'ch12_ink_body.py', 'ch12_ink_body_b.py', 'ch12_ink_body_c.py', 'derive_ch12_ink.py', 'ch12_ink.py', 'ch12_ink_diag.py', 'patch_ink_ch12.py', 'assert_driver.py',
      'ch12_rows_onkelos_a.py', 'ch12_rows_onkelos_b.py', 'ch12_rows_sifrei_59_62.py', 'ch12_rows_sifrei_63_67.py', 'ch12_rows_sifrei_68_71.py', 'ch12_rows_sifrei_72_74.py', 'ch12_rows_sifrei_75_76.py', 'ch12_rows_sifrei_77_81.py', 'ch12_rows_outside.py', 'patch_rows_ch12.py',
      'write_ch12_ledger.py', 'write_ch12_design.py', 'write_ch12_cleanpoint.py', 'derive_ch12_patch.py', 'ch12_patch_overrides.py', 'write_ch12_manifest.py', 'seat_ch12.py', 'derive_ch12_shells.py', 'write_ch12_records.py', 'copy_ch12_forms.py']
OUT = ['ch12_dump0.out', 'ch12_measure1.out', 'ch12_onkelos.txt', 'ch12_sifrei_outside.txt', 'ch12_sifrei_spine.txt', 'ch12_outside_rows.txt', 'ch12_store_glosses.txt', 'ch12_ink_run1.out', 'ch12_ink_run2.out', 'ch12_ink_run3.out', 'write_ch12_ledger.out', 'ch12_manifest.out', 'ch12_vc.out', 'ch12_labels.out',
       'ch12_chain.log', 'ch12_ritual_deu_12_place_name.out', 'ch12_vt_deu_12_place_name.out', 'ch12_fold.out', 'ch12_fold_check1.out', 'ch12_bake.out', 'ch12_build.out', 'ch12_journal.out', 'ch12_register.out', 'ch12_large_letter.out', 'ch12_home.out', 'ch12_truth.out', 'ch12_gates_SUMMARY.txt', 'ch12_gates.log', 'ch12_records_check.out', 'ch12_records_write.out',
       'ch12_chain.sh', 'ch12_fold.sh', 'ch12_gates.sh', 'tstep.sh', 'ch12_timing.tsv', 'commit_msg_ch12.txt']
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
