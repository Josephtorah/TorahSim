#!/usr/bin/env python3
# THE DEUTERONOMY WALK sitting 13 — CHAPTER 15's READING (2026-09-22): the sitting's scripts and prints copied from the scratchpad into
# World/step9/forms_deuteronomy_walk/ as the walk's forms — the scratch ROOT line (git rev-parse) replaced by the portable header (_ROOT from the file's own
# place), the scratch path by a marker, the home path by a marker; the assert driver, the ink's four parts, the eight row files and their two checks, the
# three clean-point writers, the probe, the timer and its table with them. copy_ch14_forms.py's form (the header prepended whenever the copied text names
# _ROOT). RUN FROM THE REPO ROOT.
import os, re, subprocess
ROOT = _ROOT
SP = os.path.dirname(os.path.abspath(__file__))
DST = f'{ROOT}/World/step9/forms_deuteronomy_walk'; os.makedirs(DST, exist_ok=True)
HDR = "import os as _os\n_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place\n"
PY = ['derive_ch15_dump0.py', 'ch15_dump0.py', 'derive_ch15_measure1.py', 'ch15_measure1_sections_a.py', 'ch15_measure1_sections_b.py', 'ch15_measure1.py', 'split_ch15_spine.py', 'ch15_ink_head.py', 'ch15_ink_body.py', 'ch15_ink_body_b.py', 'ch15_ink_body_c.py', 'ch15_ink_body_d.py', 'derive_ch15_ink.py', 'ch15_ink.py', 'assert_driver.py',
      'ch15_rows_sifrei_111_116.py', 'ch15_rows_sifrei_117_118.py', 'ch15_rows_sifrei_119_123.py', 'ch15_rows_sifrei_124_126.py', 'ch15_rows_onkelos_a.py', 'ch15_rows_onkelos_b.py', 'ch15_rows_outside_a.py', 'ch15_rows_outside_b.py', 'ch15_rows_check_a.py', 'ch15_rows_check_b.py',
      'write_ch15_ledger.py', 'write_ch15_design.py', 'write_ch15_cleanpoint.py', 'write_ch15_cleanpoint_b1.py', 'write_ch15_cleanpoint_b2.py', 'derive_ch15_patch.py', 'ch15_patch_overrides.py', 'ch15_manifest_probe.py', 'write_ch15_manifest.py', 'seat_ch15.py', 'derive_ch15_shells.py', 'write_ch15_records.py', 'copy_ch15_forms.py']
OUT = ['ch15_dump0.out', 'ch15_measure1.out', 'ch15_onkelos.txt', 'ch15_sifrei_outside.txt', 'ch15_sifrei_spine.txt', 'ch15_outside_rows.txt', 'ch15_store_glosses.txt', 'ch15_ink_run1.out', 'ch15_ink_run2.out', 'ch15_ink_run3.out', 'ch15_ink_run4.out', 'ch15_rows_check_a.out', 'ch15_rows_check_a2.out', 'ch15_rows_check_b.out', 'ch15_rows_check_b2.out',
       'write_ch15_ledger.out', 'write_ch15_ledger2.out', 'write_ch15_ledger3.out', 'ch15_patch.out', 'ch15_manifest.out', 'ch15_vc.out', 'ch15_labels.out',
       'ch15_chain.log', 'ch15_ritual_deu_15_release_firstborn.out', 'ch15_vt_deu_15_release_firstborn.out', 'ch15_fold.out', 'ch15_fold_check1.out', 'ch15_bake.out', 'ch15_build.out', 'ch15_journal.out', 'ch15_register.out', 'ch15_large_letter.out', 'ch15_home.out', 'ch15_truth.out', 'ch15_gates_SUMMARY.txt', 'ch15_gates.log', 'ch15_records_check.out', 'ch15_records_write.out',
       'ch15_chain.sh', 'ch15_fold.sh', 'ch15_gates.sh', 'tstep.sh', 'ch15_timing.tsv', 'commit_msg_ch15.txt'] + [f'ch15_spine_p{p}.txt' for p in range(111, 127)]
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
