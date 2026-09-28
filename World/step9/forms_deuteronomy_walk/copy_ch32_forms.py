# THE DEUTERONOMY WALK 20 (LEAN, 2026-09-27): the reading sitting's scripts and prints copied into World/step9/forms_deuteronomy_walk/ as the walk's forms — the
# scratch ROOT line (git rev-parse) replaced by the portable header (_ROOT from the file's own place), the scratch path by a marker, the home path by a marker.
# copy_ch29b_forms.py's form (files only at the post-check; the later runs' files skipped while absent). RUN FROM THE REPO ROOT.
import os, re, subprocess
ROOT = _ROOT
SP = os.path.dirname(os.path.abspath(__file__))
DST = f'{ROOT}/World/step9/forms_deuteronomy_walk'; os.makedirs(DST, exist_ok=True)
HDR = "import os as _os\n_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place\n"
PY = ['derive_ch32_dump0.py', 'ch32_dump0.py', 'split_ch32_spine.py', 'ch32_ink_head.py', 'ch32_ink_body.py', 'ch32_ink_body_b.py', 'derive_ch32_ink.py', 'ch32_ink.py', 'ch32_measure_lean.py', 'write_ch32_design.py', 'write_ch32_point.py', 'copy_ch32_forms.py', 'assert_driver.py', 'ch32_rows_onkelos.py', 'ch32_rows_outside.py', 'ch32_rows_p306.py', 'ch32_rows_p307_316.py', 'ch32_rows_p317_322.py', 'ch32_rows_p323_338.py', 'ch32_rows_p339_341.py', 'ch32_rows_check.py', 'write_ch32_ledger.py', 'write_ch32_manifest.py', 'derive_ch32_seat.py', 'seat_ch32.py', 'write_ch32_point2.py', 'write_ch32_point3.py', 'write_ch32_point4.py', 'write_ch32_chain_note.py', 'ch32_patch_probe.py', 'ch32_patch_overrides.py', 'write_ch32_records.py', 'write_ch32_commit_msg.py', 'ch32_gates_wrap.sh', 'ch32_chain.sh', 'ch32_fold.sh', 'ch32_gates.sh', 'ch32_vc.sh', 'ch32_exam_rows.py', 'derive_ch32_recon.py', 'ch32_compile_recon.py', 'write_ch32b_ready.py']   # RUN 2-4's and the tail's skipped while absent
OUT = ['ch32_dump0.out', 'ch32_split.out', 'ch32_measure_lean.out', 'ch32_onkelos.txt', 'ch32_sifrei_outside.txt', 'ch32_sifrei_spine.txt', 'ch32_outside_rows.txt', 'ch32_store_glosses.txt', 'ch32_ink_run1.out', 'ch32_ink_run2.out', 'ch32_ink_run3.out', 'ch32_design.txt', 'ch32_point_check.out', 'ch32_point_write.out', 'ch32_timing.tsv', 'ch32_forms.out', 'ch32_home.out', 'ch32_rows_check.out', 'ch32_point2_check.out', 'ch32_point2_write.out', 'ch32_rows_check_p307.out', 'ch32_rows_check3.out', 'ch32_rows_check4.out', 'ch32_point3_check.out', 'ch32_point3_write.out', 'ch32_point4_check.out', 'ch32_point4_write.out', 'ch32_ledger.out', 'ch32_manifest.out', 'ch32_gates_SUMMARY.txt', 'ch32_gates.log', 'ch32_gates.DONE', 'ch32_records_check.out', 'ch32_records_write.out', 'commit_msg_ch32.txt', 'ch32_seat_derive.out', 'ch32_chain_note.out', 'ch32_patch_probe.out', 'ch32_patch.out', 'ch32_commit_msg.out', 'ch32_vc.out', 'ch32_labels.out', 'tstep.sh', 'ch32_chain.log', 'ch32_vt_deu_32_haazinu.out', 'ch32_vt_deu_32_song_aftermath.out', 'ch32_ritual_deu_32_haazinu.out', 'ch32_ritual_deu_32_song_aftermath.out', 'ch32_fold.out', 'ch32_fold_check1.out', 'ch32_truth.out', 'ch32_bake.out', 'ch32_build.out', 'ch32_journal.out', 'ch32_register.out', 'ch32_large_letter.out', 'ch32_home_chain.out', 'ch32_gloss_list.out', 'ch32_exam_rows.out', 'ch32b_recon.out', 'ch32b_ready.out'] + [f'ch32_spine_p{p}.txt' for p in range(306, 342)]
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
