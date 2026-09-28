# THE DEUTERONOMY WALK 19 (LEAN, 2026-09-27): the sitting's scratch forms and prints copied into World/step9/forms_deuteronomy_walk/ — the scratch ROOT line (git rev-parse) replaced by the portable header (_ROOT from the file's own place), the scratch path by a marker, the home path by a marker. copy_ch26_forms.py's form (files only). RUN FROM THE REPO ROOT.
# scratch ROOT line (git rev-parse) replaced by the portable header (_ROOT from the file's own place), the scratch path by a marker, the home path by a marker.
# copy_ch22_forms.py's form (files only at the post-check). RUN FROM THE REPO ROOT.
import os, re, subprocess
ROOT = _ROOT
SP = os.path.dirname(os.path.abspath(__file__))
DST = f'{ROOT}/World/step9/forms_deuteronomy_walk'; os.makedirs(DST, exist_ok=True)
HDR = "import os as _os\n_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place\n"
PY = ['derive_ch29_dump0.py', 'ch29_dump0.py', 'ch30_dump0.py', 'ch31_dump0.py', 'split_ch29_spine.py', 'ch29_ink_head.py', 'ch29_ink_body.py', 'ch29_ink_body_b.py', 'derive_ch29_ink.py', 'ch29_ink.py', 'ch29_measure_lean.py', 'write_ch29_design.py', 'write_ch29_point.py', 'copy_ch29_forms.py', 'assert_driver.py', 'ch29_rows_onkelos_29.py', 'ch29_rows_onkelos_30.py', 'ch29_rows_onkelos_31_a.py', 'ch29_rows_onkelos_31_b.py', 'ch29_rows_sifrei_304_305.py', 'ch29_rows_outside.py', 'ch29_rows_check.py', 'write_ch29_ledger.py', 'write_ch29_manifest.py', 'derive_ch29_seat.py', 'seat_ch29.py', 'write_ch29_point2.py', 'write_ch29_chain_note.py', 'ch29_patch_probe.py', 'ch29_patch_overrides.py', 'write_ch29_records.py', 'write_ch29_commit_msg.py']   # RUN 2's and the tail's skipped while absent
OUT = ['ch29_dump0.out', 'ch30_dump0.out', 'ch31_dump0.out', 'ch29_split.out', 'ch29_measure_lean.out', 'ch29_onkelos.txt', 'ch30_onkelos.txt', 'ch31_onkelos.txt', 'ch29_sifrei_outside.txt', 'ch30_sifrei_outside.txt', 'ch31_sifrei_outside.txt', 'ch31_sifrei_spine.txt', 'ch29_spine_p304.txt', 'ch29_spine_p305.txt', 'ch29_outside_rows.txt', 'ch29_store_glosses.txt', 'ch30_store_glosses.txt', 'ch31_store_glosses.txt', 'ch29_ink_run1.out', 'ch29_ink_run2.out', 'ch29_ink_run3.out', 'ch29_design.txt', 'ch29_point_check.out', 'ch29_point_write.out', 'ch29_timing.tsv', 'ch29_forms.out', 'ch29_rows_check.out', 'ch29_point2_check.out', 'ch29_point2_write.out', 'ch29_ledger.out', 'ch29_manifest.out', 'ch29_gates_SUMMARY.txt', 'ch29_records_check.out', 'ch29_records_write.out', 'commit_msg_ch29.txt', 'ch29_seat_derive.out', 'ch29_fold_check1.out', 'ch29_truth.out', 'ch29_bake.out', 'ch29_build.out', 'ch29_journal.out', 'ch29_register.out', 'ch29_large_letter.out', 'ch29_home.out', 'ch29_chain.log', 'ch29_gates.log', 'ch29_fold.out', 'ch29_vc.out', 'ch29_labels.out', 'ch29_patch_probe.out', 'ch29_patch.out', 'ch29_commit_msg.out', 'ch29_chain_note.out', 'ch29_gates.DONE', 'ch29_chain.sh', 'ch29_fold.sh', 'ch29_gates.sh', 'ch29_gates_wrap.sh', 'ch29_vc.sh', 'onkview.py', 'tstep.sh'] + [f'ch29_vt_{u}.out' for u in ('deu_29_moab_covenant', 'deu_30_teshuvah_choice', 'deu_31_charge_torah')] + [f'ch29_ritual_{u}.out' for u in ('deu_29_moab_covenant', 'deu_30_teshuvah_choice', 'deu_31_charge_torah')]
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
