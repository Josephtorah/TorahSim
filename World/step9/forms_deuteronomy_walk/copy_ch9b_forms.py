#!/usr/bin/env python3
# THE DEUTERONOMY WALK sitting 7b — THE COMPILE OF CHAPTER 9 (2026-09-19): RUN A's, THE DOCKET's and RUN B's scripts and prints copied from the scratchpad into
# World/step9/forms_deuteronomy_walk/ as the walk's forms — the scratch ROOT line (git rev-parse) replaced by the portable header (_ROOT from the file's own
# place), the scratch path by a marker, the home path by a marker; the recorder and the stitcher copied under their sitting's names; the docket's whole-row
# prints (ch9_rows_A-C.txt) and its dump with them. copy_ch8b_forms.py's form.
import os, re, subprocess
ROOT = _ROOT
SP = os.path.dirname(os.path.abspath(__file__))
DST = f'{ROOT}/World/step9/forms_deuteronomy_walk'; os.makedirs(DST, exist_ok=True)
HDR = "import os as _os\n_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place\n"
PY = ['ch9_compile_recon.py', 'ch9_docket_scan.py', 'write_ch9b_design.py',   # RUN A
      'ch9_docket_common.py', 'ch9_docket_rows.py', 'ch9_docket_A.py', 'ch9_docket_B.py', 'ch9_docket_C.py', 'write_ch9_docket.py', 'write_ch9_docket_records.py',   # the docket's own run
      'patch_probes_ch9.py', 'ch9_callees.py', 'add_types_ch9.py', 'ch9_part1.py', 'ch9_part2.py', 'ch9_part3.py', 'ch9_part4.py', 'ch9_cases_gen.py', 'ch9_assemble.py',
      'ch9_fastcheck.py', 'seq_record_ch9.py', 'seq_stitch_ch9.py', 'patch_seq_literals_ch9.py', 'patch_ca1_ch9.py', 'patch_probes167_ch9.py', 'patch_ink_cache_key_ch9.py',
      'add_dispositions_ch9.py', 'write_ch9b_records.py', 'copy_ch9b_forms.py']   # RUN B
OUT = ['ch9_recon.out', 'ch9_scan.out', 'ch9_docket_dump.txt', 'ch9_rows_A.txt', 'ch9_rows_B.txt', 'ch9_rows_C.txt', 'ch9_docket_write.out', 'ch9_docket_lawrows.txt',
       'ch9b_probes_fail.out', 'ch9_callees.out', 'add_types_ch9.out', 'ch9_fastcheck1.out', 'ch9_fastcheck2.out', 'ch9_cases_gen.out', 'ch9_run1.out', 'seq_record_ch9.out', 'seq_stitch_ch9.out',
       'patch_seq_literals_ch9.out', 'ch9_tape1.out', 'ch9_tape2.out', 'ch9_checkpoint_check.out', 'ch9b_chain.log', 'ch9b_chain2.log', 'add_dispositions_ch9.out',
       'ch9b_records_check.out', 'ch9b_records_write.out', 'ch9b_chain_SUMMARY_first.txt', 'ch9b_chain_dependency_first.out', 'ch9b_chain_probe_readback_first.out', 'ch9b_chain_probe_ink_cache_first.out', 'ch9b_chain_SUMMARY_second.txt', 'ch9b_chain_probe_readback_second.out', 'ch9b_chain_probe_ink_cache_second.out', 'ch9b_chain_dependency_second.out', 'ch9b_chain3.log', 'ch9b_chain_SUMMARY_third.txt', 'ch9b_chain4.log', 'ch9b_chain5.log', 'commit_msg_ch9b.txt']
GATES = 'gates_ch9b'   # the chain's folder — every step's print (the third pass's to the register gate, the fourth's from the positions table) and the SUMMARY
home = os.path.expanduser('~')   # the records writer prints the memory folder's path (under the home) — scrubbed to the marker <home> in every copied print
n = 0
def port(src, dst):
    global n
    t = open(src, encoding='utf-8').read()
    t2 = re.sub(r"^ROOT = subprocess\.check_output\(\['git', 'rev-parse', '--show-toplevel'\], text=True\)\.strip\(\)$", "ROOT = _ROOT", t, flags=re.M)
    t2 = re.sub(r"^_ROOT = __import__\('subprocess'\)\.check_output\(\['git', 'rev-parse', '--show-toplevel'\], text=True\)\.strip\(\)(.*)$", "_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place", t2, flags=re.M)
    t2 = re.sub(r"^_ROOT = _sp\.check_output\(\['git', 'rev-parse', '--show-toplevel'\], text=True\)\.strip\(\)(.*)$", "_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place", t2, flags=re.M)
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
        t = open(f'{g}/{f}', encoding='utf-8', errors='ignore').read().replace(SP, '<scratch>').replace(home, '<home>')
        open(f'{DST}/gates_ch9b_{f}', 'w', encoding='utf-8').write(t); n += 1
files = [f for f in os.listdir(DST) if os.path.isfile(f'{DST}/{f}')]   # directories skipped, never read
bad = [f for f in files if SP in open(f'{DST}/{f}', encoding='utf-8', errors='ignore').read() or home in open(f'{DST}/{f}', encoding='utf-8', errors='ignore').read()]   # no scratch path, no home path in a copied form
assert not bad, bad
git = [f for f in PY if os.path.exists(f'{DST}/{f}') and re.search(r"check_output\(\['git', 'rev-parse'", open(f'{DST}/{f}', encoding='utf-8', errors='ignore').read())]   # no git root in a form copied THIS sitting
assert not git, git
print(f'copied {n} files into {DST}; the folder holds {len(files)} files')
