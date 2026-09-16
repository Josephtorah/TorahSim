import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE DEUTERONOMY WALK sitting 2b — THE COMPILE OF CHAPTER 4 (2026-09-16): the sitting's scripts and prints copied from the scratchpad into
# World/step9/forms_deuteronomy_walk/ as the walk's forms — the scratch ROOT line (git rev-parse) replaced by the portable header (_ROOT from the
# file's own place), the chains' SP by a marker; the recorder and the stitcher copied under their sitting's names (1b's forms keep theirs).
# Sitting 2's form (copy_ch4_forms.py).
import os, re, subprocess
ROOT = _ROOT
SP = os.path.dirname(os.path.abspath(__file__))
DST = f'{ROOT}/World/step9/forms_deuteronomy_walk'; os.makedirs(DST, exist_ok=True)
HDR = "import os as _os\n_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place\n"
PY = ['ch4_compile_recon.py', 'ch4_docket_scan.py', 'ch4_docket_rows.py', 'ch4_docket_A.py', 'ch4_docket_B.py', 'ch4_docket_C.py', 'ch4_docket_D.py',
      'write_ch4_docket.py', 'add_types_ch4.py', 'patch_probes_ch4.py', 'ch4_part1.py', 'ch4_part2.py', 'ch4_part3.py', 'ch4_part4.py', 'ch4_cases_gen.py',
      'ch4_assemble.py', 'ch4_fastcheck.py', 'patch_seq_literals_ch4.py', 'declare_ch4_seat.py', 'write_ch4_design.py', 'write_ch4_state186.py',
      'write_ch4b_records.py', 'copy_ch4b_forms.py']
RENAME = {'seq_record.py': 'seq_record_ch4.py', 'seq_stitch.py': 'seq_stitch_ch4.py'}
OUT = ['ch4_recon_tail.txt', 'ch4_docket_dump.txt', 'ch4_docket_scan.out', 'ch4_cases_gen.out', 'ch4_run1.out', 'seq_record_ch4.out', 'seq_stitch_ch4.out',
       'patch_seq_literals_ch4.out', 'tape_run_ch4_1.out', 'tape_run_ch4_6.out', 'daemon_gate_ch4_fail.out', 'daemon_gate_ch4_2.out',
       'dependency_gate_ch4_fail.out', 'dependency_gate_ch4_4.out', 'census_probes_ch4.out', 'installation_probes_ch4.out', 'readback_probes_ch4.out',
       'register_probes_ch4.out', 'clock_probes_ch4.out', 'sequence_probes_ch4.out', 'view_probes_ch4.out', 'population_probes_ch4.out',
       'journal_probes_ch4.out', 'cursor_probes_ch4.out', 'checkpoint_probes_ch4.out', 'probes_ch4_chain.out', 'gates_ch4_chainB.out', 'sweep_ch4.out',
       'positions_ch4.out', 'journal_gate_ch4_final.out', 'ch4_chain2.log', 'ch4_chain3.log']
SH = ['ch4_chain2.sh', 'ch4_chain3.sh']
n = 0
def port(src, dst):
    global n
    t = open(src, encoding='utf-8').read()
    t2 = re.sub(r"^ROOT = subprocess\.check_output\(\['git', 'rev-parse', '--show-toplevel'\], text=True\)\.strip\(\)$", "ROOT = _ROOT", t, flags=re.M)
    if t2 != t: t2 = HDR + t2
    t2 = t2.replace(SP, '<scratch>')
    open(dst, 'w', encoding='utf-8').write(t2); n += 1
for f in PY + list(RENAME):
    src = f'{SP}/{f}'
    if not os.path.exists(src): print('skip (absent)', f); continue
    port(src, f'{DST}/{RENAME.get(f, f)}')
for f in SH:
    if not os.path.exists(f'{SP}/{f}'): print('skip (absent)', f); continue
    sh = open(f'{SP}/{f}', encoding='utf-8').read().replace(SP, '<scratch>').replace('git -C /Users/Shared/TorahSim rev-parse --show-toplevel', 'cd "$(dirname "$0")" && git rev-parse --show-toplevel')
    open(f'{DST}/{f}', 'w', encoding='utf-8').write(sh); n += 1
for f in OUT:
    if os.path.exists(f'{SP}/{f}'):
        t = open(f'{SP}/{f}', encoding='utf-8', errors='ignore').read().replace(SP, '<scratch>')
        open(f'{DST}/{f}', 'w', encoding='utf-8').write(t); n += 1
    else: print('skip (absent)', f)
home = os.path.expanduser('~')
bad = [f for f in os.listdir(DST) if SP in open(f'{DST}/{f}', encoding='utf-8', errors='ignore').read() or home in open(f'{DST}/{f}', encoding='utf-8', errors='ignore').read()]   # no scratch path, no home path in a copied form
assert not bad, bad
print(f'copied {n} files into {DST}; the folder holds {len(os.listdir(DST))} files')
