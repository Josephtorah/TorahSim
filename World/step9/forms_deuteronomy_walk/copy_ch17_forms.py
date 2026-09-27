#!/usr/bin/env python3
# THE DEUTERONOMY WALK sitting 15 — CHAPTERS 17-18's READING, LEAN (2026-09-24): the sitting's scripts and prints copied from the scratchpad into
# World/step9/forms_deuteronomy_walk/ as the walk's forms — the scratch ROOT line (git rev-parse) replaced by the portable header (_ROOT from the file's own
# place), the scratch path by a marker, the home path by a marker. copy_ch16_forms.py's form (files only at the post-check). RUN FROM THE REPO ROOT.
import os, re, subprocess
ROOT = _ROOT
SP = os.path.dirname(os.path.abspath(__file__))
DST = f'{ROOT}/World/step9/forms_deuteronomy_walk'; os.makedirs(DST, exist_ok=True)
HDR = "import os as _os\n_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place\n"
PY = ['trim_records_ch17.py', 'derive_ch17_dump0.py', 'ch17_dump0.py', 'ch18_dump0.py', 'split_ch17_spine.py', 'ch17_ink_head.py', 'ch17_ink_body.py', 'derive_ch17_ink.py', 'ch17_ink.py', 'ch17_measure_lean.py', 'assert_driver.py',
      'ch17_rows_sifrei_147_149.py', 'ch17_rows_sifrei_150_152.py', 'ch17_rows_sifrei_153_156.py', 'ch17_rows_sifrei_157_162.py', 'ch17_rows_sifrei_163_166.py', 'ch17_rows_sifrei_167_171.py', 'ch17_rows_sifrei_172_178.py', 'ch17_rows_onkelos_17.py', 'ch17_rows_onkelos_18.py', 'ch17_rows_outside.py', 'ch17_rows_check_a.py', 'ch17_rows_check_b.py',
      'write_ch17_ledger.py', 'write_ch17_design.py', 'derive_ch17_seat.py', 'seat_ch17.py', 'write_ch17_manifest.py', 'ch17_patch_probe.py', 'ch17_patch_overrides.py', 'write_ch17_records.py', 'write_ch17_commit_msg.py', 'copy_ch17_forms.py']
OUT = ['ch17_dump0.out', 'ch18_dump0.out', 'ch17_measure_lean.out', 'ch17_measure_compact.out', 'ch17_onkelos.txt', 'ch18_onkelos.txt', 'ch17_sifrei_outside.txt', 'ch18_sifrei_outside.txt', 'ch17_sifrei_spine.txt', 'ch18_sifrei_spine.txt', 'ch17_outside_rows.txt', 'ch17_store_glosses.txt', 'ch18_store_glosses.txt', 'ch17_ink_run1.out', 'ch17_ink_run2.out', 'ch17_rows_check_a.out', 'ch17_rows_check_a2.out', 'ch17_rows_check_b.out',
       'write_ch17_ledger.out', 'write_ch17_ledger2.out', 'ch17_patch_probe.out', 'ch17_patch.out', 'ch17_manifest.out', 'ch17_vc.out', 'ch17_labels.out',
       'ch17_chain.log', 'ch17_ritual_deu_17_courts_king.out', 'ch17_ritual_deu_18_levi_prophet.out', 'ch17_vt_deu_17_courts_king.out', 'ch17_vt_deu_18_levi_prophet.out', 'ch17_fold.out', 'ch17_fold_check1.out', 'ch17_bake.out', 'ch17_build.out', 'ch17_journal.out', 'ch17_register.out', 'ch17_large_letter.out', 'ch17_home.out', 'ch17_truth.out', 'ch17_gates_SUMMARY.txt', 'ch17_gates.log', 'ch17_records_write.out',
       'ch17_chain.sh', 'ch17_fold.sh', 'ch17_gates.sh', 'tstep.sh', 'ch17_timing.tsv', 'commit_msg_ch17.txt'] + [f'ch17_spine_p{p}.txt' for p in range(147, 179)]
home = os.path.expanduser('~')
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
print('forms copied:', n, '| the folder holds', len(files), 'files; no scratch or home path in any')
