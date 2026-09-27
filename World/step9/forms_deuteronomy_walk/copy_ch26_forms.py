#!/usr/bin/env python3
# THE DEUTERONOMY WALK 18 (LEAN, 2026-09-26): the sitting's scripts, prints, dumps and typed rows copied into World/step9/forms_deuteronomy_walk/ as the walk's forms — the
# scratch ROOT line (git rev-parse) replaced by the portable header (_ROOT from the file's own place), the scratch path by a marker, the home path by a marker.
# copy_ch22_forms.py's form (files only at the post-check). RUN FROM THE REPO ROOT.
import os, re, subprocess
ROOT = _ROOT
SP = os.path.dirname(os.path.abspath(__file__))
DST = f'{ROOT}/World/step9/forms_deuteronomy_walk'; os.makedirs(DST, exist_ok=True)
HDR = "import os as _os\n_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place\n"
PY = ['derive_ch26_dump0.py', 'ch26_dump0.py', 'ch27_dump0.py', 'ch28_dump0.py', 'split_ch26_spine.py', 'ch26_ink_head.py', 'ch26_ink_body.py', 'derive_ch26_ink.py', 'ch26_ink.py', 'ch26_measure_lean.py', 'write_ch26_design.py',
      'ch26_rows_sifrei_297_300.py', 'ch26_rows_sifrei_301_a.py', 'ch26_rows_sifrei_301_b.py', 'ch26_rows_sifrei_302_303.py', 'ch26_rows_onkelos_26.py', 'ch26_rows_check_a.py', 'write_ch26_point.py', 'copy_ch26_forms.py',
      'ch26_rows_outside.py', 'ch26_rows_onkelos_27.py', 'ch26_rows_onkelos_28_a.py', 'ch26_rows_onkelos_28_b.py', 'ch26_rows_onkelos_28_c.py', 'ch26_rows_check_b.py', 'write_ch26_ledger.py', 'write_ch26_manifest.py', 'derive_ch26_seat.py', 'seat_ch26.py', 'write_ch26_point2.py', 'ch26_patch_probe.py', 'ch26_patch_overrides.py', 'write_ch26_records.py', 'write_ch26_commit_msg.py']   # RUN 2's and the tail's skipped while absent
OUT = ['ch26_dump0.out', 'ch27_dump0.out', 'ch28_dump0.out', 'ch26_split.out', 'ch26_measure_lean.out', 'ch26_onkelos.txt', 'ch27_onkelos.txt', 'ch28_onkelos.txt', 'ch26_sifrei_outside.txt', 'ch27_sifrei_outside.txt', 'ch28_sifrei_outside.txt', 'ch26_sifrei_spine.txt', 'ch26_outside_rows.txt', 'ch26_store_glosses.txt', 'ch27_store_glosses.txt', 'ch28_store_glosses.txt',
       'ch26_ink_run1.out', 'ch26_ink_run2.out', 'ch26_rows_check_a.out', 'ch26_design.txt', 'ch26_point_check.out', 'ch26_point_write.out', 'ch26_timing.tsv', 'ch26_forms.out',
       'ch26_rows_check_b.out', 'ch26_point2_check.out', 'ch26_point2_write.out', 'ch26_ledger.out', 'ch26_manifest.out', 'ch26_fold_check1.out', 'ch26_truth.out', 'ch26_bake.out', 'ch26_build.out', 'ch26_journal.out', 'ch26_register.out', 'ch26_large_letter.out', 'ch26_home.out', 'ch26_seat_derive.out', 'ch26_chain.log', 'ch26_gates.log', 'ch26_gates_SUMMARY.txt', 'ch26_fold.out', 'ch26_vc.out', 'ch26_labels.out', 'ch26_patch_probe.out', 'ch26_patch.out', 'ch26_records_check.out', 'ch26_records_write.out', 'ch26_commit_msg.out', 'commit_msg_ch26.txt', 'ch26_chain.sh', 'ch26_fold.sh', 'ch26_gates.sh', 'ch26_gates_wrap.sh', 'ch26_vc.sh'] + [f'ch26_spine_p{p}.txt' for p in range(297, 304)]
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
skipped = []
for f in PY:
    src = f'{SP}/{f}'
    if not os.path.exists(src): skipped.append(f); continue
    port(src, f'{DST}/{f}')
for f in OUT:
    if os.path.exists(f'{SP}/{f}'):
        t = open(f'{SP}/{f}', encoding='utf-8', errors='ignore').read().replace(SP, '<scratch>').replace(home, '<home>')
        open(f'{DST}/{f}', 'w', encoding='utf-8').write(t); n += 1
    else: skipped.append(f)
files = [f for f in os.listdir(DST) if os.path.isfile(f'{DST}/{f}')]
bad = [f for f in files if SP in open(f'{DST}/{f}', encoding='utf-8', errors='ignore').read() or home in open(f'{DST}/{f}', encoding='utf-8', errors='ignore').read()]
assert not bad, bad
print('forms copied:', n, '| skipped (absent, later runs\'):', len(skipped), '| the folder holds', len(files), 'files; no scratch or home path in any')
