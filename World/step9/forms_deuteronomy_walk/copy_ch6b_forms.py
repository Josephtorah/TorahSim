import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE DEUTERONOMY WALK sitting 4b — THE COMPILE OF CHAPTER 6 (2026-09-17): the sitting's scripts and prints copied from the scratchpad into
# World/step9/forms_deuteronomy_walk/ as the walk's forms — the scratch ROOT line (git rev-parse) replaced by the portable header (_ROOT from the
# file's own place), the scratch path by a marker; the recorder and the stitcher copied under their sitting's names; THE WHOLE-ROW instruments and
# their seven chunk prints ride with them (#192 addendum 1). copy_ch5b_forms.py's form.
import os, re, subprocess
ROOT = _ROOT
SP = os.path.dirname(os.path.abspath(__file__))
DST = f'{ROOT}/World/step9/forms_deuteronomy_walk'; os.makedirs(DST, exist_ok=True)
HDR = "import os as _os\n_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place\n"
PY = ['ch6_compile_recon.py', 'ch6_docket_scan.py', 'ch6_docket_rows.py', 'ch6_docket_common.py', 'ch6_docket_A.py', 'ch6_docket_B.py', 'ch6_docket_C.py',
      'ch6_docket_D.py', 'write_ch6_docket.py', 'write_ch6b_design.py', 'write_ch6b_run2.py', 'add_types_ch6.py', 'ch6_callees.py', 'ch6_part1.py',
      'ch6_part2.py', 'ch6_part3.py', 'ch6_part4.py', 'ch6_cases_gen.py', 'ch6_assemble.py', 'ch6_fastcheck.py', 'derive_form.py', 'seq_record_ch6.py',
      'seq_stitch_ch6.py', 'patch_seq_literals_ch6.py', 'add_pointers_ch6.py', 'write_ch6_run3.py', 'write_cp191.py', 'write_cp192.py', 'write_cp193.py',
      'write_whole_row_rule.py', 'write_whole_fix_1.py', 'write_whole_fix_2.py', 'write_whole_fix_3.py', 'whole_rows_d.py', 'whole_d_corrections.py',
      'retype_ch4_fifth.py', 'fix_probes_ch6b.py', 'write_ch6b_records.py', 'copy_ch6b_forms.py']
OUT = ['ch6_recon.out', 'ch6_scan.out', 'ch6_docket_dump.txt', 'ch6_callees.out', 'ch6_run1.out', 'seq_record_ch6.out', 'seq_stitch_ch6.out',
       'ch6_checkpoint_check.out', 'ch6_tape1.out', 'daemon_gate_ch6.out', 'dependency_gate_ch6.out', 'ch4_recheck.out',
       'whole_ch4_1.txt', 'whole_ch4_2.txt', 'whole_ch4_3.txt', 'whole_deu_1.txt', 'whole_deu_2.txt', 'whole_deu_3.txt', 'whole_deu_4.txt',
       'ch6b_records_check.out', 'ch6b_records_write.out', 'ch6b_chain.log', 'ch6b_chain2.log', 'ch6b_chain_SUMMARY_first.txt', 'ch6b_chain_probes_first.out']
GATES = 'ch6b_chain'   # the chain's folder — every step's print and the SUMMARY
home = os.path.expanduser('~')   # the records writer prints the memory folder's path (under the home) — scrubbed to the marker <home> in every copied print
n = 0
def port(src, dst):
    global n
    t = open(src, encoding='utf-8').read()
    t2 = re.sub(r"^ROOT = subprocess\.check_output\(\['git', 'rev-parse', '--show-toplevel'\], text=True\)\.strip\(\)$", "ROOT = _ROOT", t, flags=re.M)
    t2 = re.sub(r"^_ROOT = __import__\('subprocess'\)\.check_output\(\['git', 'rev-parse', '--show-toplevel'\], text=True\)\.strip\(\)$", "_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place", t2, flags=re.M)
    t2 = re.sub(r"^_ROOT = _sp\.check_output\(\['git', 'rev-parse', '--show-toplevel'\], text=True\)\.strip\(\)(.*)$", "_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place", t2, flags=re.M)
    if t2 != t and not t2.startswith('import os as _os'): t2 = HDR + t2
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
        open(f'{DST}/gates_ch6b_{f}', 'w', encoding='utf-8').write(t); n += 1
files = [f for f in os.listdir(DST) if os.path.isfile(f'{DST}/{f}')]   # a __pycache__ folder had appeared beside the forms (an import from the folder) — directories skipped, never read
bad = [f for f in files if SP in open(f'{DST}/{f}', encoding='utf-8', errors='ignore').read() or home in open(f'{DST}/{f}', encoding='utf-8', errors='ignore').read()]   # no scratch path, no home path in a copied form
assert not bad, bad
print(f'copied {n} files into {DST}; the folder holds {len(files)} files')
