# THE DEUTERONOMY WALK 21 (LEAN, 2026-09-29): the reading sitting's scripts and prints copied into World/step9/forms_deuteronomy_walk/ as the walk's forms — the
# scratch ROOT line (git rev-parse) replaced by the portable header (_ROOT from the file's own place), the scratch path by a marker, the home path by a marker.
# copy_ch32_forms.py's form (files only at the post-check; the later runs' files skipped while absent). RUN FROM THE REPO ROOT.
import os, re, subprocess
ROOT = _ROOT
SP = os.path.dirname(os.path.abspath(__file__))
DST = f'{ROOT}/World/step9/forms_deuteronomy_walk'; os.makedirs(DST, exist_ok=True)
HDR = "import os as _os\n_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place\n"
PY = ['derive_ch33_dump0.py', 'ch33_dump0.py', 'split_ch33_spine.py', 'ch33_ink_head.py', 'ch33_ink_body.py', 'ch33_ink_body_b.py', 'derive_ch33_ink.py', 'ch33_ink.py', 'ch33_measure_lean.py', 'write_ch33_design.py', 'write_ch33_point.py', 'copy_ch33_forms.py', 'assert_driver.py', 'ch33_rows_onkelos.py', 'ch33_rows_outside.py', 'ch33_rows_p342_347.py', 'ch33_rows_p348_354.py', 'ch33_rows_p355_356.py', 'ch33_rows_check.py', 'write_ch33_ledger.py', 'write_ch33_manifest.py', 'derive_ch33_seat.py', 'seat_ch33.py', 'write_ch33_point2.py', 'write_ch33_point3.py', 'write_ch33_point4.py', 'write_ch33_chain_note.py', 'ch33_patch_probe.py', 'ch33_patch_overrides.py', 'write_ch33_records.py', 'write_ch33_commit_msg.py', 'ch33_gates_wrap.sh', 'ch33_chain.sh', 'ch33_fold.sh', 'ch33_gates.sh', 'ch33_vc.sh', 'write_ch33_exam.py', 'ch33_gloss_list.py']
OUT = ['ch33_dump0.out', 'derive_ch33_dump0.out', 'ch33_split.out', 'ch33_measure_lean.out', 'ch33_onkelos.txt', 'ch33_sifrei_outside.txt', 'ch33_sifrei_spine.txt', 'ch33_outside_rows.txt', 'ch33_store_glosses.txt', 'derive_ch33_ink.out', 'derive_ch33_ink2.out', 'derive_ch33_ink3.out', 'ch33_ink_run1.out', 'ch33_ink_run2.out', 'ch33_ink_run3.out', 'ch33_design.txt', 'ch33_design.out', 'ch33_point_check.out', 'ch33_point_write.out', 'ch33_timing.tsv', 'ch33_forms.out', 'ch33_home.out', 'ch33_rows_check.out', 'ch33_rows_check2.out', 'ch33_rows_check3.out', 'ch33_point2_check.out', 'ch33_point2_write.out', 'ch33_point3_check.out', 'ch33_point3_write.out', 'ch33_point4_check.out', 'ch33_point4_write.out', 'ch33_gates_wrapper.log', 'ch33_rows_check3.out', 'ch33_ledger.out', 'ch33_manifest.out', 'ch33_gates_SUMMARY.txt', 'ch33_gates.log', 'ch33_gates.DONE', 'ch33_records_check.out', 'ch33_records_write.out', 'commit_msg_ch33.txt', 'ch33_seat_derive.out', 'ch33_chain_note.out', 'ch33_patch_probe.out', 'ch33_patch.out', 'ch33_commit_msg.out', 'ch33_vc.out', 'ch33_labels.out', 'tstep.sh', 'ch33_chain.log', 'ch33_vt_deu_33_ve_zot.out', 'ch33_ritual_deu_33_ve_zot.out', 'ch33_fold.out', 'ch33_fold_check1.out', 'ch33_truth.out', 'ch33_bake.out', 'ch33_build.out', 'ch33_journal.out', 'ch33_register.out', 'ch33_large_letter.out', 'ch33_home_chain.out', 'ch33_gloss_list.out'] + ['ch33_spine_p%d.txt' % p for p in range(342, 357)]
# RUN B's forms and outs (21b — the types, the tape tools, the shells, the runner's parts, the chains, the gates, the point)
PY += ['add_types_ch33_a.py', 'add_types_ch33_b.py', 'derive_ch33_seq_tools.py', 'derive_ch33_shells.py', 'seq_record_ch33.py', 'seq_stitch_ch33.py', 'ch33_assemble.py', 'ch33_fastcheck.py', 'ch33_askcheck.py', 'ch33_cases_gen.py', 'ch33_runner_chain.sh', 'ch33_tape_chain.sh', 'ch33_tape_wrap.sh', 'ch33b_gates.sh', 'ch33_scan_census.py', 'ch33_callees_facts.py', 'derive_ch33_part1.py', 'parse_ch33_fastcheck.py', 'ch33_fact_asserts.py', 'ch33_part1.py', 'ch33_part2.py', 'ch33_part3.py', 'ch33_part4.py', 'ch33_part5.py', 'ch33_part6.py', 'ch33_part7.py', 'ch33_fastcheck_wrap.sh', 'ch33_fastcheck_wrap1.sh', 'patch_seq_literals_ch33.py', 'patch_deps_ch33.py', 'write_ch33b_point2.py', 'ch33_askcheck_wrap.sh', 'ch33_runner_wrap.sh']
OUT += ['ch33b_types_a_check.out', 'ch33b_types_a.out', 'ch33b_types_b_check.out', 'ch33b_types_b.out', 'ch33b_seq_tools.out', 'ch33b_shells.out', 'derive_ch33_part1.out', 'derive_ch33_part1_2.out', 'derive_ch33_part1_3.out', 'ch33_fastcheck_run0.out', 'ch33_fastcheck_run1.out', 'ch33_fastcheck_run2.out', 'ch33b_parse0.out', 'ch33b_parse1.out', 'ch33_tokn_expected.txt', 'ch33_name_bare_expected.txt', 'ch33_neg_expected.txt', 'ch33_twin_expected.txt', 'ch33_scans_expected.txt', 'ch33_askcheck_run1.out', 'ch33_cases_gen.out', 'ch33_runner_run1.out', 'ch33_runner_run2.out', 'ch33_runner_run3.out', 'ch33_runner_chain.out', 'ch33_tape_wrap.log', 'ch33b_dependency_first.out', 'ch33b_dependency_after.out', 'ch33b_daemon_first.out', 'seq_record_ch33.out', 'seq_stitch_ch33.out', 'patch_seq_literals_ch33.out', 'ch33_tape_run1.out', 'ch33_tape_run2.out', 'ch33_checkpoint_check.out', 'ch33_checkpoint_check2.out', 'ch33_scan_census.out', 'patch_deps_ch33.out', 'patch_deps_ch33_reg.out', 'ch33_fastcheck_wrapper.log', 'ch33_fastcheck_wrapper1.log', 'ch33b_timing.tsv', 'ch33b_point2_check.out', 'ch33b_point2_write.out', 'ch33b_home2.out', 'ch33b_gates.log']
# RUN A's forms (21b — the spec, the recon, the design, the probe, the exam; missed at RUN A's copy) and RUN B's stragglers, and THE TAIL's forms (the wrapper, the facts, the template, the writers)
PY += ['ch33b_spec.py', 'ch33b_recon_wrap.sh', 'ch33b_design_part1.py', 'ch33b_design_part2.py', 'ch33b_design_part3.py', 'write_ch33b_design.py', 'write_ch33b_point.py', 'ch33_exam_rows.py', 'patch_probes_ch33.py', 'ch33_ink_gloss_table.py', 'derive_ch33_ink_blocks.py',
       'patch_scans_ch33.py', 'ch33_ask_runner_wrap.sh', 'ch33_fastcheck_wrap2.sh', 'ch33_tape2_chain.sh', 'ch33_scan_census.py',
       'ch33b_tail_chain.sh', 'ch33b_tail_facts.py', 'write_ch33b_records.py', 'write_ch33b_commit_msg.py', 'ch33b_k1_diag.py', 'patch_k1_probe_ch33b.py', 'ch33b_tail_chain2.sh', 'ch33b_tail_records.sh']
OUT += ['ch33b_spec.out', 'ch33b_recon.out', 'ch33b_recon_wrapper.log', 'ch33b_design_check.out', 'ch33b_design_write.out', 'ch33b_design_section.md', 'ch33b_probes_fail.out', 'ch33b_probes_patch.out', 'ch33b_exam.out', 'ch33_exam_rows.out', 'ch33b_point_check.out', 'ch33b_point_write.out', 'ch33b_forms.out', 'ch33b_home.out',
        'patch_scans_ch33.out', 'ch33_tape_wrap2.log', 'ch33b_point2_check2.out', 'ch33b_gates_wrapper.log', 'ch33b_gates_SUMMARY.txt', 'ch33b_gates.DONE',
        'ch33b_asbuilt.txt', 'ch33b_cache_clear.out', 'ch33b_tail_chain.log', 'ch33b_tail_chain.DONE', 'ch33b_gates2.log', 'ch33b_gates2_SUMMARY.txt', 'ch33b_facts_partial.out', 'ch33b_facts.out', 'ch33b_records_check.out', 'ch33b_records_write.out', 'ch33b_commit_msg.out', 'commit_msg_ch33b.txt', 'ch33b_forms3.out', 'ch33b_home3.out', 'ch33b_k1_diag.out', 'patch_k1_probe_ch33b.out', 'ch33b_tail_chain2.log', 'ch33b_tail_chain2.DONE', 'ch33b_gates3.log', 'ch33b_gates3_SUMMARY.txt']
# the chain folders' step prints, copied under the folder's name (the folders themselves stay in the scratchpad)
SUB = [('ch33b_gates/probe_ink_cache.out', 'ch33b_gates_probe_ink_cache.out'), ('ch33b_gates/probes.out', 'ch33b_gates_probes.out'), ('ch33b_gates2/probe_ink_cache.out', 'ch33b_gates2_probe_ink_cache.out'), ('ch33b_gates2/probes.out', 'ch33b_gates2_probes.out'), ('ch33b_gates2/register.out', 'ch33b_gates2_register.out'), ('ch33b_gates2/positions.out', 'ch33b_gates2_positions.out'), ('ch33b_gates2/tape.out', 'ch33b_gates2_tape.out'), ('ch33b_gates2/checkpoint.out', 'ch33b_gates2_checkpoint.out'), ('ch33b_gates3/checkpoint.out', 'ch33b_gates3_checkpoint.out'), ('ch33b_gates3/sweep.out', 'ch33b_gates3_sweep.out')]
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
for src, dst in SUB:
    if os.path.exists(f'{SP}/{src}'):
        t = open(f'{SP}/{src}', encoding='utf-8', errors='ignore').read().replace(SP, '<scratch>').replace(home, '<home>')
        open(f'{DST}/{dst}', 'w', encoding='utf-8').write(t); n += 1
    else: skipped.append(src)
files = [f for f in os.listdir(DST) if os.path.isfile(f'{DST}/{f}')]
bad = [f for f in files if SP in open(f'{DST}/{f}', encoding='utf-8', errors='ignore').read() or home in open(f'{DST}/{f}', encoding='utf-8', errors='ignore').read()]
assert not bad, bad
print('forms copied:', n, '| skipped (absent, later runs\'):', len(skipped), '| the folder holds', len(files), 'files; no scratch or home path in any')
