#!/usr/bin/env python3
# THE DEUTERONOMY WALK sitting 16b — CHAPTERS 19-21's COMPILE, LEAN (2026-09-25): the sitting's scripts and prints copied from the scratchpad into
# World/step9/forms_deuteronomy_walk/ as the walk's forms — the scratch ROOT line (git rev-parse) replaced by the portable header, the scratch path and the home
# path by markers. copy_ch19_forms.py's form (idempotent; run again at every clean point). RUN FROM THE REPO ROOT.
import os, re, subprocess
ROOT = _ROOT
SP = os.path.dirname(os.path.abspath(__file__))
DST = f'{ROOT}/World/step9/forms_deuteronomy_walk'; os.makedirs(DST, exist_ok=True)
HDR = "import os as _os\n_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place\n"
PY = ['derive_ch19_recon.py', 'ch19_compile_recon.py', 'ch19_exam_rows.py', 'write_ch19b_design.py', 'ch19_callees.py', 'patch_probes_ch19.py', 'write_ch19_exam.py', 'ch19_types_a1.py', 'ch19_types_a2.py', 'ch19_types_a3.py', 'add_types_ch19_a.py', 'add_types_ch19_b.py', 'write_ch19b_point.py', 'copy_ch19b_forms.py',
      'derive_ch19_seq_tools.py', 'derive_ch19_shells.py', 'seq_record_ch19.py', 'seq_stitch_ch19.py', 'derive_ch19_part1.py', 'ch19_callees_facts.py', 'ch19_part1.py', 'ch19_part5a.py', 'ch19_part5b.py', 'ch19_part5c.py', 'ch19_part5d.py', 'ch19_part5e.py', 'ch19_part5f.py', 'ch19_part2.py', 'ch19_part3.py', 'ch19_part4.py', 'ch19_part5.py', 'ch19_part6.py', 'ch19_assemble.py', 'ch19_fastcheck.py', 'ch19_askcheck.py', 'ch19_cases_gen.py', 'ch19_scan_census.py', 'patch_seq_literals_ch19.py', 'patch_scans_ch19.py', 'patch_refuge_row_ch19.py', 'patch_deps_ch19.py', 'write_ch19b_point2.py', 'write_ch19b_records.py', 'write_ch19b_commit_msg.py']
OUT = ['ch19_compile_recon.out', 'ch19_exam_rows.out', 'ch19b_design_a.txt', 'ch19b_design_b.txt', 'ch19b_design_c.txt', 'ch19_callees.out', 'ch19_probes_fail.out', 'add_types_ch19_a.out', 'add_types_ch19_b.out', 'ch19b_point_check.out', 'ch19b_point_write.out', 'ch19b_timing.tsv',
       'ch19_fastcheck_run0.out', 'ch19_fastcheck_run1.out', 'ch19_fastcheck_run2.out', 'ch19_runner_lint.out', 'ch19_scan_census3.out', 'ch19b_dependency_after2.out', 'ch19b_register_after.out', 'ch19b_gates_SUMMARY_pass1.txt', 'ch19b_gates_pass1.log', 'ch19b_point2_check.out', 'ch19b_point2_write.out', 'ch19b_forms2.out', 'ch19b_home2.out', 'ch19_tape_wrap.log', 'ch19_runner_chain.log', 'ch19_tape_wrap.log', 'ch19b_dependency_after.out', 'ch19_askcheck_run1.out', 'ch19_cases_gen.out', 'ch19_runner_run1.out', 'ch19_runner_run2.out', 'ch19_runner_run3.out', 'ch19b_dependency_first.out', 'ch19b_daemon_first.out', 'seq_record_ch19.out', 'seq_stitch_ch19.out', 'patch_seq_literals_ch19.out', 'ch19_tape_run1.out', 'ch19_tape_run2.out', 'ch19_tape_run3.out', 'ch19_checkpoint_check.out', 'ch19_checkpoint_check2.out', 'ch19_scan_census.out', 'ch19_scan_census2.out', 'ch19_runner_chain.sh', 'ch19_tape_chain.sh', 'ch19_tape_wrap.sh', 'ch19b_gates.sh', 'ch19b_gates_SUMMARY.txt', 'ch19b_gates.log', 'ch19b_point2_check.out', 'ch19b_point2_write.out', 'ch19b_records_check.out', 'ch19b_records_write.out', 'commit_msg_ch19b.txt']
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
    if not os.path.exists(src): continue
    port(src, f'{DST}/{f}')
for f in OUT:
    if os.path.exists(f'{SP}/{f}'):
        t = open(f'{SP}/{f}', encoding='utf-8', errors='ignore').read().replace(SP, '<scratch>').replace(home, '<home>')
        open(f'{DST}/{f}', 'w', encoding='utf-8').write(t); n += 1
files = [f for f in os.listdir(DST) if os.path.isfile(f'{DST}/{f}')]
bad = [f for f in files if SP in open(f'{DST}/{f}', encoding='utf-8', errors='ignore').read() or home in open(f'{DST}/{f}', encoding='utf-8', errors='ignore').read()]
assert not bad, bad
print('forms copied:', n, '| the folder holds', len(files), 'files; no scratch or home path in any')
