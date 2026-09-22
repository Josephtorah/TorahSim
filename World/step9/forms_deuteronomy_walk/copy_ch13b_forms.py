#!/usr/bin/env python3
# THE DEUTERONOMY WALK sitting 11b — THE COMPILE OF CHAPTER 13 (2026-09-21): RUN A's, RUN B's and the tail's scripts and prints copied from the scratchpad into
# World/step9/forms_deuteronomy_walk/ as the walk's forms — the scratch ROOT line (git rev-parse) replaced by the portable header (_ROOT from the file's own
# place), the scratch path by a marker, the home path by a marker; the recorder and the stitcher copied under their sitting's names; the chain's folder whole.
# (The docket's forms were copied at the docket run — copy_ch13_docket_forms.py.) copy_ch12b_forms.py's form. RUN FROM THE REPO ROOT.
import os, re, subprocess
ROOT = _ROOT
SP = os.path.dirname(os.path.abspath(__file__))
DST = f'{ROOT}/World/step9/forms_deuteronomy_walk'; os.makedirs(DST, exist_ok=True)
HDR = "import os as _os\n_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place\n"
PY = ['derive_ch13_recon.py', 'ch13_compile_recon.py', 'ch13_recon_excerpt.py', 'derive_ch13_docket_scan.py', 'ch13_docket_scan.py', 'write_ch13b_design.py', 'write_ch13b_cleanpoint.py',   # RUN A
      'patch_probes_ch13.py', 'add_types_ch13.py', 'ch13_callees.py', 'derive_ch13_part1.py', 'ch13_part1.py', 'ch13_part2.py', 'ch13_part3.py', 'ch13_part4.py', 'ch13_part5.py', 'ch13_scene_gen.py',
      'ch13_cases_gen.py', 'ch13_assemble.py', 'ch13_fastcheck.py', 'derive_ch13_seq_tools.py', 'seq_record_ch13.py', 'seq_stitch_ch13.py', 'patch_seq_literals_ch13.py',
      'write_ch13b_records.py', 'copy_ch13b_forms.py', 'extend_commit_msg_ch13b.py', 'ch13_runner_chain.sh', 'ch13_tape_chain.sh', 'patch_tail_ch13b.py', 'tstep.sh']   # RUN B and the tail (the absent ones skipped by name)
OUT = ['ch13_recon.out', 'ch13_recon.err', 'ch13_recon_excerpt.txt', 'ch13_docket_scan.out',   # RUN A's prints
       'ch13b_probes_fail.out', 'add_types_ch13.out', 'ch13_callees.out', 'ch13_fastcheck_run1.out', 'ch13_fastcheck_run2.out', 'ch13_cases_gen.out', 'ch13_runner_run1.out', 'ch13_runner_run2.out',
       'ch13_runner_chain.log', 'seq_record_ch13.out', 'seq_stitch_ch13.out', 'patch_seq_literals_ch13.out', 'ch13_tape_run1.out', 'ch13_tape_run2.out', 'ch13_checkpoint_check.out',
       'ch13_tape_chain.log', 'ch13b_chain1.log', 'ch13b_chain2.log', 'ch13b_chain3.log', 'ch13b_chain_SUMMARY_first.txt', 'ch13b_chain_SUMMARY_second.txt', 'ch13b_dependency_direct.out', 'patch_tail_ch13b.out', 'ch13b_positions_direct.log', 'ch13b_chain_story.txt', 'ch13b_records_check.out', 'ch13b_records_write.out', 'commit_msg_ch13b.txt', 'ch13_timing.tsv']
GATES = 'gates_ch13b'   # the chain's folder — every step's print and the SUMMARY
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
        open(f'{DST}/gates_ch13b_{f}', 'w', encoding='utf-8').write(t); n += 1
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
