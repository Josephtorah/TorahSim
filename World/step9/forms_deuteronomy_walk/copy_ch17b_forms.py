import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE DEUTERONOMY WALK 15b (LEAN): the sitting's forms copied into World/step9/forms_deuteronomy_walk/ — the python files with the portable _ROOT header prepended
# (the scratch ROOT-from-git line replaced), the shells and the prints as they are; no scratch path and no home path in any copy (asserted). copy_ch16b_forms.py's form. RUN FROM THE REPO ROOT.
import os, re, subprocess, glob
ROOT = _ROOT
SP = os.path.dirname(os.path.abspath(__file__))
FD = f'{ROOT}/World/step9/forms_deuteronomy_walk'
HOME = os.path.expanduser('~')
PY = ['ch17_compile_recon.py', 'write_ch17b_design.py', 'ch17_callees.py', 'ch17_callees_facts.py', 'patch_probes_ch17.py', 'add_types_ch17_a.py', 'add_types_ch17_b.py', 'write_ch17_exam.py', 'derive_ch17_seq_tools.py', 'derive_ch17_shells.py', 'derive_ch17_part1.py', 'ch17_part1.py', 'ch17_part2.py', 'ch17_part3.py', 'ch17_part4.py', 'ch17_part5.py', 'ch17_assemble.py', 'ch17_fastcheck.py', 'ch17_askcheck.py', 'ch17_cases_gen.py', 'seq_record_ch17.py', 'seq_stitch_ch17.py', 'patch_seq_literals_ch17.py', 'ch17_scan_census.py', 'patch_scans_ch17.py', 'patch_deps_ch17.py', 'patch_tape_de4_ch17.py', 'patch_deps_ch17b.py', 'patch_probes_q_ch17.py', 'write_ch17b_point.py', 'write_ch17b_records.py', 'copy_ch17b_forms.py', 'write_ch17b_commit_msg.py']
SH = ['ch17_runner_chain.sh', 'ch17_tape_chain.sh', 'ch17_build_chain.sh', 'ch17_build_wrap.sh', 'ch17_tape_wrap.sh', 'ch17_tape2_wrap.sh', 'ch17_tape3_wrap.sh', 'ch17b_gates.sh']
OUT = ['ch17_compile_recon.out', 'ch17_callees.out', 'ch17_probes_fail.out', 'add_types_ch17_a.out', 'add_types_ch17_b.out', 'ch17_fastcheck_run0.out', 'ch17_fastcheck_run1.out', 'ch17_askcheck_run1.out', 'ch17_cases_gen.out', 'ch17_runner_run1.out', 'ch17_runner_run2.out', 'ch17_runner_run3.out', 'ch17_build_chain.log', 'ch17_tape_wrap.log', 'ch17_tape2_wrap.log', 'seq_record_ch17.out', 'seq_stitch_ch17.out', 'patch_seq_literals_ch17.out', 'ch17_tape_run1.out', 'ch17_tape_run2.out', 'ch17_tape_run3.out', 'ch17_tape3_wrap.log', 'ch17_checkpoint_check.out', 'ch17_checkpoint_check2.out', 'ch17_checkpoint_check3.out', 'ch17_scan_census.out', 'ch17_scan_census2.out', 'ch17_scan_census3.out', 'ch17b_dependency_first.out', 'ch17b_dependency_after.out', 'ch17b_dependency_after2.out', 'ch17b_daemon_first.out', 'ch17b_daemon_after.out', 'ch17b_gates.log', 'ch17b_gates_SUMMARY.txt', 'ch17b_timing.tsv', 'ch17b_point_check.out', 'ch17b_point_write.out', 'ch17b_records_check.out', 'ch17b_records_write.out', 'commit_msg_ch17b.txt']
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
for f in sorted(glob.glob(f'{SP}/ch17b_gates/*')):
    text = open(f, encoding='utf-8', errors='replace').read().replace(SP, '<scratch>').replace(ROOT, '<repo>').replace(HOME, '<home>')
    open(f'{FD}/gates_ch17b_{os.path.basename(f)}', 'w', encoding='utf-8').write(text); n += 1
print('forms copied: %d | skipped (absent): %s | the folder holds %d files; no scratch or home path in any' % (n, skipped, len(os.listdir(FD))))
bad = [p for p in glob.glob(f'{FD}/*') if os.path.isfile(p) and os.path.getsize(p) < 2_000_000 and (SP in open(p, encoding='utf-8', errors='replace').read() or HOME in open(p, encoding='utf-8', errors='replace').read())]
assert not bad, bad
