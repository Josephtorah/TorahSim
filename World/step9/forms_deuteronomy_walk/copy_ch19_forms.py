#!/usr/bin/env python3
# THE DEUTERONOMY WALK sitting 16 — CHAPTERS 19-21's READING, LEAN (2026-09-24): the sitting's scripts and prints copied from the scratchpad into
# World/step9/forms_deuteronomy_walk/ as the walk's forms — the scratch ROOT line (git rev-parse) replaced by the portable header (_ROOT from the file's own
# place), the scratch path by a marker, the home path by a marker. copy_ch17_forms.py's form (files only at the post-check). RUN FROM THE REPO ROOT.
import os, re, subprocess
ROOT = _ROOT
SP = os.path.dirname(os.path.abspath(__file__))
DST = f'{ROOT}/World/step9/forms_deuteronomy_walk'; os.makedirs(DST, exist_ok=True)
HDR = "import os as _os\n_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place\n"
PY = ['derive_ch19_dump0.py', 'ch19_dump0.py', 'ch20_dump0.py', 'ch21_dump0.py', 'split_ch19_spine.py', 'ch19_ink_head.py', 'ch19_ink_body.py', 'derive_ch19_ink.py', 'ch19_ink.py', 'ch19_measure_lean.py', 'assert_driver.py',
      'ch19_rows_sifrei_179_183.py', 'ch19_rows_sifrei_184_188.py', 'ch19_rows_sifrei_189_190.py', 'ch19_rows_sifrei_191_197.py', 'ch19_rows_sifrei_198_204.py', 'ch19_rows_sifrei_205_210.py', 'ch19_rows_sifrei_211_215.py', 'ch19_rows_sifrei_216_218.py', 'ch19_rows_sifrei_219_221.py', 'ch19_rows_onkelos_19.py', 'ch19_rows_onkelos_20.py', 'ch19_rows_onkelos_21.py', 'ch19_rows_outside.py', 'ch19_rows_check_a.py', 'ch19_rows_check_b.py',
      'write_ch19_ledger.py', 'write_ch19_design.py', 'write_ch19_point.py', 'write_ch19_point2.py', 'derive_ch19_seat.py', 'seat_ch19.py', 'write_ch19_manifest.py', 'ch19_patch_probe.py', 'ch19_patch_overrides.py', 'write_ch19_records.py', 'write_ch19_commit_msg.py', 'copy_ch19_forms.py']
OUT = ['ch19_dump0.out', 'ch20_dump0.out', 'ch21_dump0.out', 'ch19_split.out', 'ch19_measure_lean.out', 'ch19_onkelos.txt', 'ch20_onkelos.txt', 'ch21_onkelos.txt', 'ch19_sifrei_outside.txt', 'ch20_sifrei_outside.txt', 'ch21_sifrei_outside.txt', 'ch19_sifrei_spine.txt', 'ch20_sifrei_spine.txt', 'ch21_sifrei_spine.txt', 'ch19_outside_rows.txt', 'ch19_store_glosses.txt', 'ch20_store_glosses.txt', 'ch21_store_glosses.txt', 'ch19_ink_run1.out', 'ch19_ink_run2.out', 'ch19_ink_run3.out', 'ch19_rows_check_a.out', 'ch19_rows_check_a2.out', 'ch19_rows_check_b.out', 'ch19_rows_check_b2.out', 'ch19_point_check.out', 'ch19_point_check2.out', 'ch19_point_write.out',
       'write_ch19_ledger.out', 'ch19_patch_probe.out', 'ch19_patch.out', 'ch19_manifest.out', 'ch19_vc.out', 'ch19_labels.out',
       'ch19_chain.log', 'ch19_ritual_deu_19_miklat_witness.out', 'ch19_ritual_deu_20_war_rules.out', 'ch19_ritual_deu_21_eglah_family.out', 'ch19_vt_deu_19_miklat_witness.out', 'ch19_vt_deu_20_war_rules.out', 'ch19_vt_deu_21_eglah_family.out', 'ch19_fold.out', 'ch19_fold_check1.out', 'ch19_bake.out', 'ch19_build.out', 'ch19_journal.out', 'ch19_register.out', 'ch19_large_letter.out', 'ch19_home.out', 'ch19_truth.out', 'ch19_gates_SUMMARY.txt', 'ch19_gates.log', 'ch19_gates.DONE', 'ch19_records_write.out',
       'ch19_chain.sh', 'ch19_fold.sh', 'ch19_gates.sh', 'ch19_gates_wrap.sh', 'ch19_timing.tsv', 'commit_msg_ch19.txt'] + [f'ch19_spine_p{p}.txt' for p in range(179, 222)]
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
