# THE DEUTERONOMY WALK 22 (LEAN, 2026-09-30): the reading sitting's scripts and prints copied into World/step9/forms_deuteronomy_walk/ as the walk's forms — the
# scratch ROOT line (git rev-parse) replaced by the portable header (_ROOT from the file's own place), the scratch path by a marker, the home path by a marker.
# copy_ch33_forms.py's form (files only at the post-check; the tail's files skipped while absent). RUN FROM THE REPO ROOT.
import os, re, subprocess
ROOT = _ROOT
SP = os.path.dirname(os.path.abspath(__file__))
DST = f'{ROOT}/World/step9/forms_deuteronomy_walk'; os.makedirs(DST, exist_ok=True)
HDR = "import os as _os\n_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place\n"
PY = ['derive_ch34_dump0.py', 'ch34_dump0.py', 'ch34_split.py', 'ch34_ink_head.py', 'ch34_ink_body.py', 'ch34_ink_body_b.py', 'derive_ch34_ink.py', 'ch34_ink.py', 'ch34_measure_lean.py', 'write_ch34_design.py', 'write_ch34_point.py', 'copy_ch34_forms.py', 'assert_driver.py', 'ch34_rows_onkelos.py', 'ch34_rows_outside.py', 'ch34_rows_p357.py', 'ch34_rows_check.py', 'write_ch34_ledger.py', 'write_ch34_manifest.py', 'seat_ch34.py', 'ch34_gates_wrap.sh', 'ch34_chain.sh', 'ch34_fold.sh', 'ch34_gates.sh', 'ch34_vc.sh',
      'ch34_gloss_list.py', 'ch34_patch_probe.py', 'ch34_patch_overrides.py', 'write_ch34_records.py', 'write_ch34_commit_msg.py', 'ch34_tail_facts.py', 'ch34_tail_records.sh']
OUT = ['ch34_dump0.out', 'ch34_split.out', 'ch34_measure_lean.out', 'ch34_onkelos.txt', 'ch34_sifrei_outside.txt', 'ch34_sifrei_spine.txt', 'ch34_spine_p357.txt', 'ch34_store_glosses.txt', 'ch34_ink_run1.out', 'ch34_ink_run2.out', 'ch34_ink_run3.out', 'ch34_ink_run4.out', 'ch34_design.txt', 'ch34_rows_check.out', 'ch34_ledger.out', 'ch34_manifest.out', 'ch34_timing.tsv', 'ch34_chain.log', 'ch34_vt_deu_34_moses_death.out', 'ch34_ritual_deu_34_moses_death.out', 'ch34_fold.out', 'ch34_fold_check1.out', 'ch34_truth.out', 'ch34_bake.out', 'ch34_build.out', 'ch34_journal.out', 'ch34_register.out', 'ch34_large_letter.out', 'ch34_home_chain.out', 'ch34_gates_SUMMARY.txt', 'ch34_gates.log', 'ch34_gates.DONE', 'ch34_gates_wrapper.log', 'ch34_point_check.out', 'ch34_point_write.out', 'ch34_forms.out', 'ch34_home.out', 'tstep.sh',
       'ch34_vc.out', 'ch34_labels.out', 'ch34_gloss_list.out', 'ch34_patch_probe.out', 'ch34_patch.out', 'ch34_asbuilt.txt', 'ch34_facts.out', 'ch34_records_check.out', 'ch34_records_write.out', 'ch34_commit_msg.out', 'commit_msg_ch34.txt', 'ch34_forms2.out', 'ch34_home2.out']
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
print('forms copied:', n, '| skipped (absent, the tail\'s):', len(skipped), skipped, '| the folder holds', len(files), 'files; no scratch or home path in any')
