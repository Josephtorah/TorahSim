#!/usr/bin/env python3
# THE DEUTERONOMY WALK sitting 8b — THE COMPILE OF CHAPTER 10 (2026-09-20): RUN B's scripts and prints copied from the scratchpad into
# World/step9/forms_deuteronomy_walk/ as the walk's forms — the scratch ROOT line (git rev-parse) replaced by the portable header (_ROOT from the file's own
# place), the scratch path by a marker, the home path by a marker; the recorder and the stitcher copied under their sitting's names; the chain's folder whole.
# (RUN A's and the docket's forms were copied at their own runs — copy_ch10_docket_forms.py.) copy_ch9b_forms.py's form.
import os, re, subprocess
ROOT = _ROOT
SP = os.path.dirname(os.path.abspath(__file__))
DST = f'{ROOT}/World/step9/forms_deuteronomy_walk'; os.makedirs(DST, exist_ok=True)
HDR = "import os as _os\n_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place\n"
PY = ['patch_probes_ch10.py', 'add_types_ch10.py', 'ch10_callees.py', 'patch_after_callees_ch10.py', 'derive_ch10_part1.py', 'ch10_part1.py', 'ch10_part2.py', 'ch10_part3.py', 'ch10_part4.py',
      'ch10_cases_gen.py', 'ch10_assemble.py', 'ch10_fastcheck.py', 'seq_record_ch10.py', 'derive_ch10_stitch.py', 'seq_stitch_ch10.py', 'patch_seq_literals_ch10.py', 'patch_da1_ch10.py', 'patch_tape2_ch10.py',
      'patch_nr_scan_ch10.py', 'patch_probes172_ch10.py', 'add_dispositions_ch10.py', 'patch_ink_cache_src_ch10.py', 'record_compaction_ch10b.py', 'write_ch10b_records.py', 'copy_ch10b_forms.py', 'extend_commit_msg_ch10b.py']   # RUN B
OUT = ['ch10b_probes_fail.out', 'add_types_ch10.out', 'ch10_callees.out', 'ch10_cases_gen.out', 'ch10_run1.out', 'seq_record_ch10.out', 'seq_stitch_ch10.out',
       'patch_seq_literals_ch10.out', 'ch10_tape1.out', 'ch10_tape2_first.out', 'ch10_tape2.out', 'ch10_tape3.out', 'ch10_checkpoint_check.out', 'ch10b_chain1.log', 'ch10b_chain2.log', 'ch10b_chain_SUMMARY_first.txt', 'ch10b_chain_dependency_first.out', 'ch10b_chain_probe_readback_first.out', 'add_dispositions_ch10.out', 'ch10b_chain_SUMMARY_second.txt', 'ch10b_chain_positions_second.out', 'ch10b_chain3.log', 'ch10b_records_check.out', 'ch10b_records_write.out', 'commit_msg_ch9b.txt']
GATES = 'gates_ch10b'   # the chain's folder — every step's print and the SUMMARY
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
        open(f'{DST}/gates_ch10b_{f}', 'w', encoding='utf-8').write(t); n += 1
# THE TRUNCATED SCRATCH PATH (read at this copier's first run): the chain's stamp print carries the scratchpad's path CUT at the summary's width, so the whole-path
# replace above misses it (7b's copier the same — its two copies in the folder carried it); every copied print is scrubbed again by prefix — the marker <scratch>
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
git = [f for f in PY if os.path.exists(f'{DST}/{f}') and re.search(r"check_output\(\['git', 'rev-parse'", open(f'{DST}/{f}', encoding='utf-8', errors='ignore').read())]   # no git root in a form copied THIS sitting
assert not git, git
print(f'copied {n} files into {DST}; the folder holds {len(files)} files')
