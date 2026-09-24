#!/usr/bin/env python3
# THE DEUTERONOMY WALK sitting 14 — CHAPTER 16's READING, LEAN (2026-09-23): the sitting's scripts and prints copied from the scratchpad into
# World/step9/forms_deuteronomy_walk/ as the walk's forms — the scratch ROOT line (git rev-parse) replaced by the portable header (_ROOT from the file's own
# place), the scratch path by a marker, the home path by a marker. copy_ch15_forms.py's form. RUN FROM THE REPO ROOT.
import os, re, subprocess
ROOT = _ROOT
SP = os.path.dirname(os.path.abspath(__file__))
DST = f'{ROOT}/World/step9/forms_deuteronomy_walk'; os.makedirs(DST, exist_ok=True)
HDR = "import os as _os\n_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place\n"
PY = ['derive_ch16_dump0.py', 'ch16_dump0.py', 'derive_ch16_split.py', 'split_ch16_spine.py', 'ch16_ink_head.py', 'ch16_ink_body.py', 'derive_ch16_ink.py', 'ch16_ink.py', 'ch16_measure_lean.py', 'assert_driver.py',
      'ch16_rows_sifrei_127_131.py', 'ch16_rows_sifrei_132_136.py', 'ch16_rows_sifrei_137_142.py', 'ch16_rows_sifrei_143_146.py', 'ch16_rows_onkelos_a.py', 'ch16_rows_onkelos_b.py', 'ch16_rows_outside.py', 'ch16_rows_check_a.py', 'ch16_rows_check_b.py',
      'write_ch16_ledger.py', 'write_ch16_design.py', 'derive_ch16_seat.py', 'seat_ch16.py', 'derive_ch16_shells.py', 'write_ch16_manifest.py', 'ch16_patch_probe.py', 'ch16_patch_overrides.py', 'write_ch16_records.py', 'write_ch16_commit_msg.py', 'copy_ch16_forms.py']
OUT = ['ch16_dump0.out', 'ch16_measure_lean.out', 'ch16_onkelos.txt', 'ch16_sifrei_outside.txt', 'ch16_sifrei_spine.txt', 'ch16_outside_rows.txt', 'ch16_store_glosses.txt', 'ch16_ink_run1.out', 'ch16_ink_run2.out', 'ch16_rows_check_a.out', 'ch16_rows_check_a2.out', 'ch16_rows_check_b.out', 'ch16_rows_check_b2.out', 'ch16_rows_check_b3.out',
       'write_ch16_ledger.out', 'write_ch16_ledger2.out', 'write_ch16_ledger3.out', 'ch16_patch_probe.out', 'ch16_patch.out', 'ch16_manifest.out', 'ch16_vc.out', 'ch16_labels.out',
       'ch16_chain.log', 'ch16_ritual_deu_16_festivals_judges.out', 'ch16_vt_deu_16_festivals_judges.out', 'ch16_fold.out', 'ch16_fold_check1.out', 'ch16_bake.out', 'ch16_build.out', 'ch16_journal.out', 'ch16_register.out', 'ch16_large_letter.out', 'ch16_home.out', 'ch16_truth.out', 'ch16_gates_SUMMARY.txt', 'ch16_gates.log', 'ch16_records_write.out',
       'ch16_chain.sh', 'ch16_fold.sh', 'ch16_gates.sh', 'tstep.sh', 'ch16_timing.tsv', 'commit_msg_ch16.txt'] + [f'ch16_spine_p{p}.txt' for p in range(127, 147)]
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
