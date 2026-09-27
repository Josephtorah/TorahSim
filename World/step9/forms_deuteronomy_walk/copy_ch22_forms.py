#!/usr/bin/env python3
# THE DEUTERONOMY WALK sitting 17 — CHAPTERS 22-25's READING, LEAN (2026-09-25): the sitting's scripts and prints copied from the scratchpad into
# World/step9/forms_deuteronomy_walk/ as the walk's forms — the scratch ROOT line (git rev-parse) replaced by the portable header (_ROOT from the file's own
# place), the scratch path by a marker, the home path by a marker. copy_ch19_forms.py's form (files only at the post-check). RUN FROM THE REPO ROOT.
import os, re, subprocess
ROOT = _ROOT
SP = os.path.dirname(os.path.abspath(__file__))
DST = f'{ROOT}/World/step9/forms_deuteronomy_walk'; os.makedirs(DST, exist_ok=True)
HDR = "import os as _os\n_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place\n"
PY = ['derive_ch22_dump0.py', 'ch22_dump0.py', 'ch23_dump0.py', 'ch24_dump0.py', 'ch25_dump0.py', 'split_ch22_spine.py', 'ch22_ink_head.py', 'ch22_ink_body.py', 'derive_ch22_ink.py', 'ch22_ink.py', 'ch22_measure_lean.py',
      'ch22_rows_sifrei_222_226.py', 'ch22_rows_sifrei_227_230.py', 'ch22_rows_sifrei_231_236.py', 'ch22_rows_sifrei_237_241.py', 'ch22_rows_sifrei_242_245.py', 'ch22_rows_onkelos_22.py', 'ch22_rows_outside.py', 'ch22_rows_check_a.py',
      'ch22_rows_sifrei_246_253.py', 'ch22_rows_sifrei_254_261.py', 'ch22_rows_sifrei_262_267.py', 'ch22_rows_sifrei_268_270.py', 'ch22_rows_sifrei_271_277.py', 'ch22_rows_sifrei_278_285.py', 'ch22_rows_onkelos_23.py', 'ch22_rows_onkelos_24.py', 'ch22_rows_check_b.py',
      'ch22_rows_sifrei_286_287.py', 'ch22_rows_sifrei_288_291.py', 'ch22_rows_sifrei_292_296.py', 'ch22_rows_onkelos_25.py', 'ch22_rows_check_c.py',
      'write_ch22_ledger.py', 'write_ch22_point.py', 'write_ch22_point2.py', 'write_ch22_point3.py', 'derive_ch22_seat.py', 'seat_ch22.py', 'write_ch22_manifest.py', 'ch22_patch_probe.py', 'ch22_patch_overrides.py', 'write_ch22_records.py', 'write_ch22_commit_msg.py', 'copy_ch22_forms.py']
OUT = ['ch22_ledger.out', 'ch22_ledger2.out', 'ch22_seat_derive.out', 'ch22_records_check.out', 'ch22_commit_msg.out', 'ch22_point3_note.out', 'ch22_vc.sh', 'ch22_dump0.out', 'ch23_dump0.out', 'ch24_dump0.out', 'ch25_dump0.out', 'ch22_split.out', 'ch22_measure_lean.out', 'ch22_onkelos.txt', 'ch23_onkelos.txt', 'ch24_onkelos.txt', 'ch25_onkelos.txt', 'ch22_sifrei_outside.txt', 'ch23_sifrei_outside.txt', 'ch24_sifrei_outside.txt', 'ch25_sifrei_outside.txt', 'ch22_sifrei_spine.txt', 'ch23_sifrei_spine.txt', 'ch24_sifrei_spine.txt', 'ch25_sifrei_spine.txt', 'ch22_outside_rows.txt', 'ch22_store_glosses.txt', 'ch23_store_glosses.txt', 'ch24_store_glosses.txt', 'ch25_store_glosses.txt',
       'ch22_ink_run1.out', 'ch22_ink_run2.out', 'ch22_rows_check_a.out', 'ch22_rows_check_a2.out', 'ch22_rows_check_b.out', 'ch22_rows_check_b2.out', 'ch22_rows_check_c.out', 'ch22_rows_check_c2.out', 'ch22_point_check.out', 'ch22_point_write.out', 'ch22_point2_check.out', 'ch22_point2_write.out', 'ch22_point3_check.out', 'ch22_point3_write.out', 'ch22_design_part1.txt', 'ch22_design_part2.txt',
       'write_ch22_ledger.out', 'ch22_patch_probe.out', 'ch22_patch.out', 'ch22_manifest.out', 'ch22_vc.out', 'ch22_labels.out',
       'ch22_chain.log', 'ch22_ritual_deu_22_return_sex_laws.out', 'ch22_ritual_deu_23_qahal_purity_vows.out', 'ch22_ritual_deu_24_divorce_poor.out', 'ch22_ritual_deu_25_courts_yibbum.out', 'ch22_vt_deu_22_return_sex_laws.out', 'ch22_vt_deu_23_qahal_purity_vows.out', 'ch22_vt_deu_24_divorce_poor.out', 'ch22_vt_deu_25_courts_yibbum.out', 'ch22_fold.out', 'ch22_fold_check1.out', 'ch22_bake.out', 'ch22_build.out', 'ch22_journal.out', 'ch22_register.out', 'ch22_large_letter.out', 'ch22_home.out', 'ch22_truth.out', 'ch22_gates_SUMMARY.txt', 'ch22_gates.log', 'ch22_gates.DONE', 'ch22_records_write.out',
       'ch22_chain.sh', 'ch22_fold.sh', 'ch22_gates.sh', 'ch22_gates_wrap.sh', 'ch22_timing.tsv', 'commit_msg_ch22.txt'] + [f'ch22_spine_p{p}.txt' for p in range(222, 297)]
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
