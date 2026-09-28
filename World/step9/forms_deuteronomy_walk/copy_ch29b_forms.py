# THE DEUTERONOMY WALK 19b (LEAN, 2026-09-27): the compile sitting's scripts and prints copied into World/step9/forms_deuteronomy_walk/ as the walk's forms — the
# scratch ROOT line (git rev-parse) replaced by the portable header (_ROOT from the file's own place), the scratch path by a marker, the home path by a marker.
# copy_ch26b_forms.py's form (files only at the post-check; the later runs' files skipped while absent). RUN FROM THE REPO ROOT.
import os, re, subprocess
ROOT = _ROOT
SP = os.path.dirname(os.path.abspath(__file__))
DST = f'{ROOT}/World/step9/forms_deuteronomy_walk'; os.makedirs(DST, exist_ok=True)
HDR = "import os as _os\n_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place\n"
PY = ['ch29_exam_rows.py', 'ch29_compile_recon.py', 'ch29_callees.py', 'ch29b_spec.py', 'ch29b_design_part1.py', 'ch29b_design_part2.py', 'ch29b_design_part3.py', 'write_ch29b_design.py', 'patch_probes_ch29.py', 'write_ch29_exam.py', 'write_ch29b_point.py', 'copy_ch29b_forms.py', 'ch29b_callees2.py', 'ch29a_p1.py', 'ch29a_p2.py', 'ch29a_p3.py', 'ch29a_p4.py', 'ch29a_p5a.py', 'ch29a_p5b.py', 'ch29a_p5c.py', 'ch29a_p6.py', 'ch29_runner_chain.sh', 'ch29_tape_chain.sh', 'ch29_tape_wrap.sh', 'add_types_ch29_a.py', 'add_types_ch29_b.py', 'derive_ch29_seq_tools.py', 'derive_ch29_shells.py', 'ch29_callees_facts.py', 'derive_ch29_part1.py', 'ch29_part1.py', 'ch29_part2.py', 'ch29_part3.py', 'ch29_part4.py', 'ch29_part5.py', 'ch29_part6.py', 'ch29_part7.py', 'ch29_cases_gen.py', 'ch29_assemble.py', 'ch29_fastcheck.py', 'ch29_askcheck.py', 'ch29_scan_census.py', 'seq_record_ch29.py', 'seq_stitch_ch29.py', 'patch_seq_literals_ch29.py', 'patch_deps_ch29.py', 'patch_probes_retypes_ch29.py', 'patch_tape_retypes_ch29.py', 'patch_scans_ch29.py', 'patch_scans_ch29b.py', 'ch29_second_pass.sh', 'ch29_pass2_wrap.sh', 'ch29_third_pass.sh', 'patch_tape_retypes_ch29b.py', 'ch29_tape_verdict.py', 'write_ch29b_point2.py', 'write_ch29b_records.py', 'write_ch29b_commit_msg.py', 'ch29b_gates.sh', 'ch29b_after_chain.sh', 'patch_probes_retypes_ch29b.py', 'patch_probe_q47_ch29b.py', 'ch29b_gates2.sh', 'ch29b_tail_facts.py', 'ch29b_gates3.sh']   # RUN B's and the tail's skipped while absent
OUT = ['ch29_exam_rows.out', 'ch29b_recon.out', 'ch29_callees.out', 'ch29_callees_filtered.txt', 'ch29b_spec.out', 'ch29b_design_check.out', 'ch29b_design_write.out', 'ch29b_design_assembled.md', 'ch29b_probes_patch.out', 'ch29b_probes_fail.out', 'ch29b_exam.out', 'ch29b_point_check.out', 'ch29b_point_write.out', 'ch29b_timing.tsv', 'ch29b_forms.out', 'ch29b_home.out', 'ch29b_types_a.out', 'ch29b_types_b.out', 'ch29b_callees2.out', 'ch29b_types_a_check.out', 'ch29b_types_b_check.out', 'derive_ch29_part1.out', 'derive_ch29_part1_2.out', 'derive_ch29_part1_3.out', 'ch29_fastcheck_run0.out', 'ch29_fastcheck_run1.out', 'ch29_fastcheck_run2.out', 'ch29_fastcheck_run3.out', 'ch29_fastcheck_run4.out', 'ch29_askcheck.out', 'ch29_cases_gen.out', 'ch29_runner_chain.out', 'ch29_runner_run1.out', 'ch29_runner_run2.out', 'ch29_runner_run3.out', 'ch29_tape_wrap.out', 'ch29b_dependency_first.out', 'ch29b_dependency_after.out', 'ch29b_daemon_first.out', 'seq_record_ch29.out', 'seq_stitch_ch29.out', 'patch_seq_literals_ch29.out', 'ch29_tape_run1.out', 'ch29_tape_run2.out', 'ch29_tape_run3.out', 'ch29_checkpoint_check.out', 'ch29_checkpoint_check2.out', 'ch29_scan_census.out', 'ch29_twin_expected.txt', 'ch29_scans_expected.txt', 'ch29_tokn_expected.txt', 'ch29_name_bare_expected.txt', 'patch_probes_retypes_ch29.out', 'patch_tape_retypes_ch29.out', 'patch_scans_ch29.out', 'patch_scans_ch29b.out', 'ch29_fastcheck_run5.out', 'ch29_fastcheck_run6.out', 'ch29_fastcheck_run7.out', 'ch29_fastcheck_run8.out', 'ch29_askcheck2.out', 'derive_ch29_part1_4.out', 'derive_ch29_part1_5.out', 'derive_ch29_part1_6.out', 'ch29_second_pass.out', 'ch29_pass2_wrap.out', 'ch29_fastcheck_run9.out', 'ch29_askcheck3.out', 'ch29_third_pass.out', 'ch29_runner_run4.out', 'ch29b_dependency_after2.out', 'ch29_checkpoint_check3.out', 'patch_tape_retypes_ch29b.out', 'derive_ch29_part1_7.out', 'patch_deps_ch29.out', 'ch29b_gates_SUMMARY.txt', 'ch29b_gates.log', 'ch29b_point2_check.out', 'ch29b_point2_write.out', 'ch29b_records_check.out', 'ch29b_records_write.out', 'ch29b_commit_msg.out', 'commit_msg_ch29b.txt', 'ch29b_asbuilt.txt', 'ch29b_probes_retypes_check.out', 'ch29b_probes_retypes.out', 'ch29b_probe_q47.out', 'ch29b_gates2_SUMMARY.txt', 'ch29b_gates2.log', 'ch29b_gates2_killed_probe_readback.out', 'ch29b_tail_facts.out', 'ch29b_gates2_part1_SUMMARY.txt', 'ch29b_gates3_positions.out', 'ch29b_gates3_SUMMARY.txt', 'ch29b_gates3.log']
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
