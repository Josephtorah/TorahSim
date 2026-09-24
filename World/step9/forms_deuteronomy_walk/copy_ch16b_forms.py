import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE DEUTERONOMY WALK 14b (LEAN): the sitting's forms copied into World/step9/forms_deuteronomy_walk/ — the python files with the portable _ROOT header prepended
# (the scratch ROOT-from-git line replaced), the shells and the prints as they are; no scratch path and no home path in any copy (asserted). copy_ch16_forms.py's form. RUN FROM THE REPO ROOT.
import os, re, subprocess, glob
ROOT = _ROOT
SP = os.path.dirname(os.path.abspath(__file__))
FD = f'{ROOT}/World/step9/forms_deuteronomy_walk'
HOME = os.path.expanduser('~')
PY = ['ch16_compile_recon.py', 'write_ch16b_design.py', 'ch16_callees.py', 'ch16_callees2.py', 'ch16_callees_facts.py', 'patch_probes_ch16.py', 'add_types_ch16_a.py', 'add_types_ch16_b.py', 'write_ch16_exam.py', 'derive_ch16_seq_tools.py', 'derive_ch16_shells.py', 'derive_ch16_part1.py', 'ch16_part1.py', 'ch16_part2a.py', 'ch16_part2b.py', 'ch16_part2.py', 'ch16_part3.py', 'ch16_part5.py', 'ch16_assemble.py', 'ch16_fastcheck.py', 'ch16_askcheck.py', 'ch16_cases_gen.py', 'seq_record_ch16.py', 'seq_stitch_ch16.py', 'patch_seq_literals_ch16.py', 'patch_second_tablets_ch16.py', 'patch_second_tablets_ch16b.py', 'patch_place_name_ch16.py', 'patch_tape_dd4_ch16.py', 'ch16_scan_census.py', 'retype_writers_ch16b.py', 'retype_point_cap_ch16b.py', 'retype_tail_ch16b.py', 'patch_deps_ch16.py', 'patch_deps_ch16b.py', 'patch_probe_q33_ch16.py', 'write_ch16b_point.py', 'write_ch16b_records.py', 'write_ch16b_commit_msg.py', 'copy_ch16b_forms.py', 'show_anchors.py']
SH = ['ch16_runner_chain.sh', 'ch16_tape_chain.sh', 'ch16_build_chain.sh', 'ch16b_gates.sh']
OUT = ['ch16_compile_recon.out', 'ch16_callees.out', 'ch16_callees2.out', 'ch16_probes_fail.out', 'add_types_ch16_a.out', 'add_types_ch16_a2.out', 'add_types_ch16_a3.out', 'add_types_ch16_b.out', 'ch16_fastcheck_run0.out', 'ch16_fastcheck_run1.out', 'ch16_askcheck_run1.out', 'ch16_cases_gen.out', 'ch16_runner_run1.out', 'ch16_build_chain.log', 'seq_record_ch16.out', 'seq_stitch_ch16.out', 'patch_seq_literals_ch16.out', 'ch16_tape_run1.out', 'ch16_tape_run2.out', 'ch16_tape_run3.out', 'ch16_tape_run4.out', 'ch16_tape_run5.out', 'ch16_checkpoint_check.out', 'ch16_checkpoint_check2.out', 'ch16b_point_check.out', 'ch16b_point_write.out', 'ch16_tape_chain.log', 'ch16b_dependency_first.out', 'ch16b_daemon_first.out', 'ch16b_dependency_after.out', 'ch16b_dependency_after2.out', 'ch16b_gates_SUMMARY_first.txt', 'ch16b_gates_SUMMARY.txt', 'ch16b_gates.log', 'ch16b_timing.tsv', 'ch16b_records_check.out', 'ch16b_records_write.out', 'commit_msg_ch16b.txt']
HEADER = "import os as _os\n_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place\n"
GIT = "ROOT = _ROOT"
GIT2 = "_ROOT = _sp.check_output(['git', 'rev-parse', '--show-toplevel'], text=True).strip()"
n = 0; skipped = []
for name in PY + SH + OUT:
    src = f'{SP}/{name}'
    if not os.path.exists(src): skipped.append(name); continue
    text = open(src, encoding='utf-8', errors='replace').read()
    if name in PY:
        if GIT in text: text = HEADER + text.replace(GIT, 'ROOT = _ROOT')
        elif GIT2 in text: text = text.replace(GIT2, "_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place")
    if name in OUT or name in SH:
        text = text.replace(SP, '<scratch>').replace(ROOT, '<repo>')
    text = text.replace(SP, '<scratch>').replace(HOME, '<home>')
    assert SP not in text and HOME not in text, name
    open(f'{FD}/{name}', 'w', encoding='utf-8').write(text); n += 1
# the gates chain's own outputs (the step prints) copied under the sitting's prefix — the first pass's under gates_ch16b_first_
for f in sorted(glob.glob(f'{SP}/ch16b_gates_first/*')):
    text = open(f, encoding='utf-8', errors='replace').read().replace(SP, '<scratch>').replace(ROOT, '<repo>').replace(HOME, '<home>')
    open(f'{FD}/gates_ch16b_first_{os.path.basename(f)}', 'w', encoding='utf-8').write(text); n += 1
for f in sorted(glob.glob(f'{SP}/ch16b_gates/*')):
    text = open(f, encoding='utf-8', errors='replace').read().replace(SP, '<scratch>').replace(ROOT, '<repo>').replace(HOME, '<home>')
    open(f'{FD}/gates_ch16b_{os.path.basename(f)}', 'w', encoding='utf-8').write(text); n += 1
print('forms copied: %d | skipped (absent): %s | the folder holds %d files; no scratch or home path in any' % (n, skipped, len(os.listdir(FD))))
bad = [p for p in glob.glob(f'{FD}/*') if os.path.isfile(p) and os.path.getsize(p) < 2_000_000 and (SP in open(p, encoding='utf-8', errors='replace').read() or HOME in open(p, encoding='utf-8', errors='replace').read())]
assert not bad, bad
