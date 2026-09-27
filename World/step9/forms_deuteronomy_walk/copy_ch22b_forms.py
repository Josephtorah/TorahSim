#!/usr/bin/env python3
# THE DEUTERONOMY WALK sitting 17b — CHAPTERS 22-25's COMPILE, LEAN (2026-09-26): the sitting's scripts and prints copied from the scratchpad into
# World/step9/forms_deuteronomy_walk/ as the walk's forms — the scratch ROOT line (git rev-parse) replaced by the portable header (_ROOT from the file's own
# place), the scratch path by a marker, the home path by a marker. copy_ch22_forms.py's form (files only at the post-check). RUN FROM THE REPO ROOT.
import os, re, subprocess
ROOT = _ROOT
SP = os.path.dirname(os.path.abspath(__file__))
DST = f'{ROOT}/World/step9/forms_deuteronomy_walk'; os.makedirs(DST, exist_ok=True)
HDR = "import os as _os\n_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place\n"
PY = ['ch22_exam_rows.py', 'ch22_compile_recon.py', 'ch22_callees.py', 'ch22_callees2.py', 'ch22_callees3.py', 'ch22_callees_keys.py', 'write_ch22b_design.py', 'patch_probes_ch22.py', 'write_ch22_exam.py', 'write_ch22b_point.py', 'copy_ch22b_forms.py',
      'add_types_ch22_a.py', 'add_types_ch22_b.py', 'derive_ch22_seq_tools.py', 'derive_ch22_shells.py', 'derive_ch22_part1.py', 'ch22_part1.py', 'ch22_part2.py', 'ch22_part3.py', 'ch22_part4.py', 'ch22_part5.py', 'ch22_part6.py', 'ch22_part7.py', 'ch22_fastcheck.py', 'ch22_askcheck.py', 'ch22_cases_gen.py', 'ch22_assemble.py', 'ch22_scan_census.py', 'patch_scans_ch22.py', 'patch_deps_ch22.py', 'write_ch22b_point2.py', 'write_ch22b_records.py', 'write_ch22b_commit_msg.py',
      'ch22_types_a1.py', 'ch22_types_a2.py', 'ch22_types_a3.py', 'ch22_types_a4.py', 'ch22_part2a.py', 'ch22_part2b.py', 'ch22_part3a.py', 'ch22_part3b.py', 'ch22_part4a.py', 'ch22_part4b.py', 'ch22_part5a.py', 'ch22_part5b.py', 'ch22_part6a.py', 'ch22_part6b.py', 'ch22_part6c.py', 'ch22_part6d.py', 'ch22_part6e.py', 'ch22_part7a.py', 'ch22_part7b.py', 'ch22_part7c.py', 'ch22_part8.py', 'ch22_callees_facts.py', 'patch_seq_literals_ch22.py', 'seq_record_ch22.py', 'seq_stitch_ch22.py']   # RUN B's parts as typed (the cells four to a part in halves, the readback in five blocks, the daemon in three), the facts, the tape tools
OUT = ['ch22_exam_rows.out', 'ch22_compile_recon.out', 'ch22_callees.out', 'ch22_callees2.out', 'ch22_callees3.out', 'ch22_callees_keys.out', 'ch22b_design_a.txt', 'ch22b_design_b.txt', 'ch22b_design_c.txt', 'ch22b_design_d.txt', 'ch22_probes_fail.out', 'ch22_exam.out', 'ch22_exam2.out', 'ch22b_point_check.out', 'ch22b_point_write.out', 'ch22b_timing.tsv', 'ch22b_forms.out',
       'add_types_ch22_a.out', 'add_types_ch22_b.out', 'ch22_fastcheck_run0.out', 'ch22_fastcheck_run1.out', 'ch22_fastcheck_run2.out', 'ch22_askcheck_run1.out', 'ch22_cases_gen.out', 'ch22_runner_run1.out', 'ch22_runner_run2.out', 'ch22_runner_lint.out', 'ch22b_dependency_first.out', 'ch22b_daemon_first.out', 'ch22_tape_run1.out', 'ch22_tape_run2.out', 'ch22_tape_run3.out', 'ch22_checkpoint_check.out', 'ch22_scan_census.out', 'ch22b_point2_check.out', 'ch22b_point2_write.out', 'ch22b_gates_SUMMARY.txt', 'ch22b_gates.log', 'ch22b_records_check.out', 'ch22b_records_write.out', 'commit_msg_ch22b.txt', 'ch22_tape_chain.sh', 'ch22_tape_wrap.sh', 'ch22_runner_chain.sh', 'ch22b_gates.sh', 'ch22b_gates_wrap.sh',
       'ch22_types_a_check.out', 'ch22_types_a.out', 'ch22_types_b_check.out', 'ch22_types_b.out', 'derive_ch22_part1.out', 'derive_ch22_part1_2.out', 'ch22_fastcheck_run3.out', 'ch22_fastcheck_run4.out', 'ch22_twin_expected.txt', 'ch22_scans_expected.txt', 'ch22_build_chain.sh', 'ch22_build_chain.log', 'ch22_runner_chain.log', 'seq_record_ch22.out', 'seq_stitch_ch22.out', 'patch_seq_literals_ch22.out', 'ch22_tape_wrap.log', 'ch22_scan_census2.out',
       'ch22_checkpoint_check2.out', 'ch22_checkpoint_check3.out', 'ch22_scan_census3.out', 'ch22b_dependency_after.out', 'ch22b_dependency_after2.out', 'ch22b_dependency_after3.out', 'patch_deps_ch22.out', 'patch_deps_ch22_2.out', 'patch_deps_ch22_3.out', 'patch_scans_ch22.out', 'seq_record_ch22_2.out', 'seq_stitch_ch22_2.out', 'derive_ch22_part1_3.out', 'ch22_tape_chain2.sh', 'ch22_tape_chain2.log', 'ch22b_home.out']   # RUN B's prints (the gates alone after each filing, the tape's third run's companions, the second recorder and stitcher prints)
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
