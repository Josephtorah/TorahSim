#!/usr/bin/env python3
# THE DEUTERONOMY WALK 13b (2026-09-23) — RUN B's and THE TAIL's instruments and prints copied into World/step9/forms_deuteronomy_walk/ as the walk's forms — the
# scratch ROOT line (git rev-parse) replaced by the portable header (_ROOT from the file's own place), the scratch path by a marker, the home path by a marker; the
# recorder and the stitcher copied under their sitting's names; the chain's folder whole. (RUN A's and the docket's forms were copied at their runs.)
# copy_ch14b_forms.py's form. RUN FROM THE REPO ROOT.
import os, re, subprocess
ROOT = _ROOT
SP = os.path.dirname(os.path.abspath(__file__))
DST = f'{ROOT}/World/step9/forms_deuteronomy_walk'; os.makedirs(DST, exist_ok=True)
HDR = "import os as _os\n_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place\n"
PY = ['ch15_callees.py', 'patch_probes_ch15.py', 'add_types_ch15_p1.py', 'add_types_ch15_p2.py', 'add_types_ch15_p3.py', 'add_types_ch15.py', 'ch15_callees_facts.py', 'derive_ch15_part1.py', 'ch15_part1.py', 'ch15_part2a.py', 'ch15_part2b.py', 'ch15_part2.py',
      'ch15_part3a.py', 'ch15_part3b.py', 'ch15_part3c.py', 'ch15_part3d.py', 'ch15_part3.py', 'ch15_part4a.py', 'ch15_part4b.py', 'ch15_part4c.py', 'ch15_part4.py', 'ch15_part5.py', 'ch15_scene_gen.py', 'ch15_cases_gen.py', 'ch15_assemble.py', 'ch15_fastcheck.py', 'ch15_askcheck.py', 'derive_ch15_shells.py',
      'derive_ch15_seq_tools.py', 'seq_record_ch15.py', 'seq_stitch_ch15.py', 'patch_seq_literals_ch15.py', 'write_ch15b_runb_point.py', 'write_ch15b_records.py', 'copy_ch15b_forms.py', 'extend_commit_msg_ch15b.py',
      'ch15_runner_chain.sh', 'ch15_tape_chain.sh', 'patch_tape_cu5_ch15.py', 'ch15_tape_chain2.sh', 'ch15_tape_chain3.sh', 'patch_reuse_scan_ch15.py', 'ch15_tape_chain4.sh', 'ch15_probes_types_chain.sh', 'ch15_types_fastcheck_chain.sh', 'ch15_fastcheck_chain1.sh', 'ch15_fastcheck_chain2.sh', 'patch_tail_ch15b.py', 'patch_tape_dg7_ch15.py', 'write_ch15b_commit_msg.py', 'write_ch15b_chain_story.py', 'write_ch15b_records_A.py', 'write_ch15b_records_B.py', 'write_ch15b_records_C.py', 'write_ch15b_records.py', 'write_ch15b_runb_point.py', 'copy_ch15b_forms.py', 'tstep.sh']   # RUN B and the tail (the absent ones skipped by name)
OUT = ['ch15_callees.out', 'ch15_callees_cut.txt', 'ch15b_probes_fail.out', 'patch_probes_ch15.out', 'add_types_ch15.out', 'ch15_probes_types_chain.log', 'ch15_types_fastcheck_chain.log', 'ch15_fastcheck_run0.out', 'ch15_fastcheck_run1.out', 'ch15_fastcheck_run2.out', 'ch15_fastcheck_chain1.log', 'ch15_fastcheck_chain2.log', 'ch15_askcheck_run1.out',
       'ch15_cases_gen.out', 'ch15_runner_run1.out', 'ch15_runner_run2.out', 'ch15_runner_chain.log', 'seq_record_ch15.out', 'seq_stitch_ch15.out', 'patch_seq_literals_ch15.out', 'ch15_tape_run1.out', 'ch15_tape_run2.out', 'ch15_tape_run3.out', 'ch15_runner_run3.out', 'ch15_checkpoint_check_run1.out', 'ch15_checkpoint_check.out', 'ch15_tape_chain.log', 'patch_tape_cu5_ch15.out', 'ch15_tape_chain2.log', 'ch15_tape_chain3.log', 'patch_reuse_scan_ch15.out', 'ch15_tape_chain4.log',
       'ch15b_chain1.log', 'ch15b_chain2.log', 'ch15b_chain3.log', 'ch15b_chain_SUMMARY_first.txt', 'ch15b_chain_SUMMARY_second.txt', 'ch15b_dependency_direct.out', 'patch_tail_ch15b.out', 'ch15b_positions_direct.log',
       'ch15b_chain_story.txt', 'ch15b_tape_story.txt', 'patch_tail_ch15b.out', 'ch15b_dependency_after.out', 'ch15b_chain_dependency_first.out', 'ch15b_chain_readback_first.out', 'ch15b_chain_summary_first.txt', 'patch_tape_dg7_ch15.out', 'ch15b_chain_tape_third.out', 'ch15b_chain_summary_fourth.txt', 'ch15b_positions_four.out', 'ch15b_records_check.out', 'ch15b_records_write.out', 'commit_msg_ch15b.txt', 'ch15b_timing.tsv']
GATES = 'gates_ch15b'   # the chain's folder — every step's print and the SUMMARY
home = os.path.expanduser('~')   # the records writer prints the memory folder's path (under the home) — scrubbed to the marker <home> in every copied print
n = 0
def port(src, dst):
    global n
    t = open(src, encoding='utf-8').read()
    t2 = re.sub(r"^ROOT = subprocess\.check_output\(\['git', 'rev-parse', '--show-toplevel'\], text=True\)\.strip\(\)$", "ROOT = _ROOT", t, flags=re.M)
    t2 = re.sub(r"^_ROOT = (?:__import__\('subprocess'\)|subprocess|_sp)\.check_output\(\['git', 'rev-parse', '--show-toplevel'\], text=True\)\.strip\(\)(.*)$", "_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place", t2, flags=re.M)
    t2 = re.sub(r"(?:__import__\('subprocess'\)|subprocess|_sp)\.check_output\(\['git', 'rev-parse', '--show-toplevel'\], text=True\)\.strip\(\)", "_ROOT", t2)
    if t2 != t and '_ROOT = _os.path.normpath' not in t2: t2 = HDR + t2
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
g = f'{SP}/{GATES}'
if os.path.isdir(g):
    for f in sorted(os.listdir(g)):
        if not os.path.isfile(f'{g}/{f}'): continue
        t = open(f'{g}/{f}', encoding='utf-8', errors='ignore').read().replace(SP, '<scratch>').replace(home, '<home>')
        open(f'{DST}/gates_ch15b_{f}', 'w', encoding='utf-8').write(t); n += 1
# THE TRUNCATED SCRATCH PATH (9b's copier's find): the chain's stamp print carries the scratchpad's path CUT at the summary's width — every copied print scrubbed again by prefix
SCR_RX = re.compile(r'/private' + r'/tmp/claude-501/[^\s)\]\'"]*')
for f in os.listdir(DST):
    q = f'{DST}/{f}'
    if not os.path.isfile(q): continue
    t = open(q, encoding='utf-8', errors='ignore').read()
    if SCR_RX.search(t): open(q, 'w', encoding='utf-8').write(SCR_RX.sub('<scratch>', t))
files = [f for f in os.listdir(DST) if os.path.isfile(f'{DST}/{f}')]   # directories skipped, never read
BAD = ('/private' + '/tmp', home)   # a copier's own literal split by concatenation — never the bare scratch path in the tree
bad = [f for f in files if any(b in open(f'{DST}/{f}', encoding='utf-8', errors='ignore').read() for b in BAD)]   # no scratch path, no home path in a copied form
assert not bad, bad
git = [f for f in PY if f.endswith('.py') and os.path.exists(f'{DST}/{f}') and re.search(r"check_output\(\['git', 'rev-parse'", open(f'{DST}/{f}', encoding='utf-8', errors='ignore').read())]   # no git root in a form copied THIS sitting
assert not git, git
print(f'copied {n} files into {DST}; the folder holds {len(files)} files')
