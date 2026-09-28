#!/usr/bin/env python3
# THE DEUTERONOMY WALK 18b (LEAN, 2026-09-26): the compile sitting's scripts and prints copied into World/step9/forms_deuteronomy_walk/ as the walk's forms — the
# scratch ROOT line (git rev-parse) replaced by the portable header (_ROOT from the file's own place), the scratch path by a marker, the home path by a marker.
# copy_ch26_forms.py's form (files only at the post-check; the later runs' files skipped while absent). RUN FROM THE REPO ROOT.
import os, re, subprocess
ROOT = _ROOT
SP = os.path.dirname(os.path.abspath(__file__))
DST = f'{ROOT}/World/step9/forms_deuteronomy_walk'; os.makedirs(DST, exist_ok=True)
HDR = "import os as _os\n_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place\n"
PY = ['ch26b_gates2.sh', 'ch26b_fourth_chain.sh', 'ch26b_third_chain.sh', 'patch_kin_ch26.py', 'patch_scans_ch26.py', 'patch_deps_ch26.py', 'patch_tape_retypes_ch26.py', 'patch_probes_retypes_ch26.py', 'ch26b_after_chain.sh', 'ch26b_second_chain.sh', 'ch26_tape_verdict.py', 'ch26_exam_rows.py', 'ch26_compile_recon.py', 'ch26_callees.py', 'ch26b_spec.py', 'ch26b_design_part1.py', 'ch26b_design_part2.py', 'ch26b_design_part3.py', 'write_ch26b_design.py', 'patch_probes_ch26.py', 'write_ch26_exam.py', 'write_ch26b_point.py', 'copy_ch26b_forms.py', 'ch26a_p1.py', 'ch26a_p2.py', 'ch26a_p3.py', 'ch26a_p4.py', 'ch26a_p5.py', 'add_types_ch26_a.py', 'add_types_ch26_b.py', 'derive_ch26_seq_tools.py', 'derive_ch26_shells.py', 'ch26b_callees2.py', 'ch26b_callees3.py', 'ch26_callees_facts.py', 'derive_ch26_part1.py', 'ch26_part1.py', 'ch26_part2.py', 'ch26_part3.py', 'ch26_part4.py', 'ch26_part5.py', 'ch26_part6.py', 'ch26_part7.py', 'ch26_cases_gen.py', 'ch26_assemble.py', 'ch26_fastcheck.py', 'ch26_askcheck.py', 'ch26_scan_census.py', 'seq_record_ch26.py', 'seq_stitch_ch26.py', 'patch_seq_literals_ch26.py', 'write_ch26b_point2.py', 'write_ch26b_records.py', 'write_ch26b_commit_msg.py', 'patch_tail_ch26b.py']
OUT = ['ch26b_gates2_SUMMARY.txt', 'ch26b_asbuilt.txt', 'ch26b_fourth_chain_SUMMARY.txt', 'ch26_checkpoint_check4.out', 'ch26_tape_run4.out', 'ch26_runner_run6.out', 'patch_kin_ch26.out', 'ch26b_third_chain_SUMMARY.txt', 'ch26_checkpoint_check3.out', 'ch26_tape_run3.out', 'ch26_runner_run5.out', 'patch_scans_ch26.out', 'patch_deps_ch26.out', 'ch26b_dependency_after.out', 'ch26b_dependency_after2.out', 'ch26b_after_chain_SUMMARY.txt', 'ch26b_second_chain_SUMMARY.txt', 'ch26_runner_run3.out', 'ch26_runner_run4.out', 'ch26_checkpoint_check2.out', 'patch_tape_retypes_ch26.out', 'patch_probes_retypes_ch26.out', 'ch26_tape_run1_read3.txt', 'ch26_assemble_4.out', 'ch26_exam_rows.out', 'ch26_compile_recon.out', 'ch26_callees.out', 'ch26b_design_assembled.md', 'ch26b_probes_fail.out', 'ch26b_timing.tsv', 'ch26b_point_check.out', 'ch26b_point_write.out', 'ch26b_forms.out', 'ch26b_types_a_check.out', 'ch26b_types_a.out', 'ch26b_types_b_check.out', 'ch26b_types_b.out', 'ch26b_callees2.out', 'ch26b_facts_pick1.out', 'ch26b_facts_pick2.out', 'derive_ch26_part1.out', 'derive_ch26_part1_2.out', 'ch26_fastcheck_run0.out', 'ch26_fastcheck_run1.out', 'ch26_fastcheck_run2.out', 'ch26_fastcheck_run3.out', 'ch26_fastcheck_run4.out', 'ch26_askcheck.out', 'ch26_twin_expected.txt', 'ch26_scans_expected.txt', 'ch26_cases_gen.out', 'ch26_runner_run1.out', 'ch26_runner_run2.out', 'ch26b_dependency_first.out', 'ch26b_daemon_first.out', 'seq_record_ch26.out', 'seq_stitch_ch26.out', 'patch_seq_literals_ch26.out', 'ch26_tape_run1.out', 'ch26_tape_run2.out', 'ch26_checkpoint_check.out', 'ch26_scan_census.out', 'ch26_runner_chain.sh', 'ch26_tape_chain.sh', 'ch26_tape_wrap.sh', 'ch26b_gates.sh', 'ch26_runner_chain.out', 'ch26_tape_wrap.out', 'ch26b_gates.log', 'ch26b_gates_SUMMARY.txt', 'ch26b_point2_check.out', 'ch26b_point2_write.out', 'ch26b_records_check.out', 'ch26b_records_write.out', 'commit_msg_ch26b.txt', 'ch26b_commit_msg.out']
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
