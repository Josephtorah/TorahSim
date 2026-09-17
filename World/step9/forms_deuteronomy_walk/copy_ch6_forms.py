#!/usr/bin/env python3
# THE DEUTERONOMY WALK sitting 4 — CHAPTER 6 (2026-09-17): the sitting's scripts and prints copied from the scratchpad into
# World/step9/forms_deuteronomy_walk/ as the walk's forms — the four runs' scripts (the dump, the measurement, the ink, the six row files, the
# ledger writer, the display patch, the manifest, the seat, the chain and the fold, the checkpoints, the records, this copy) and the prints (the
# chain log, the ritual, verify_text, the fold's checks, the gates re-run into files); the two large Sifrei dumps (the spine 100 KB, the outside
# rows 92 KB) NOT copied — reproducible by ch6_dump0.py from the export. Sitting 3's form (copy_ch5_forms.py): no scratch path, no home path
# in a copied form — asserted.
import os, re, subprocess
ROOT = subprocess.check_output(['git', 'rev-parse', '--show-toplevel'], text=True).strip()
SP = os.path.dirname(os.path.abspath(__file__))
DST = f'{ROOT}/World/step9/forms_deuteronomy_walk'; os.makedirs(DST, exist_ok=True)
PY = ['ch6_dump0.py', 'ch6_measure1.py', 'ch6_ink.py', 'ch6_rows_sifrei_31.py', 'ch6_rows_sifrei_32.py', 'ch6_rows_sifrei_33_36.py', 'ch6_rows_outside.py',
      'ch6_rows_onkelos_a.py', 'ch6_rows_onkelos_b.py', 'write_ch6_ledger.py', 'ch6_patch_overrides.py', 'write_ch6_manifest.py', 'seat_ch6.py',
      'write_ch6_design.py', 'write_large_letters.py', 'write_ch6_run2.py', 'write_ch6_run3.py', 'copy_ch6_forms.py', 'write_ch6_records.py']
SH = ['ch6_chain.sh', 'ch6_fold.sh']
OUT = ['ch6_dump0.out', 'ch6_measure1.out', 'ch6_onkelos.txt', 'ch6_store_glosses.txt', 'ch6_ink_run2.out', 'ch6_ink_run3.out', 'ch6_chain.log',
       'ch6_ritual_deu_06_shema.out', 'ch6_vt_deu_06_shema.out', 'ch6_fold_check1.out', 'ch6_bake.out', 'ch6_build.out', 'ch6_journal.out',
       'ch6_register.out', 'ch6_truth.out', 'ch6_records_check.out']
n = 0
for f in PY + SH:
    src = f'{SP}/{f}'
    if not os.path.exists(src): print('skip (absent)', f); continue
    t = open(src, encoding='utf-8').read().replace(SP, '<scratch>')
    open(f'{DST}/{f}', 'w', encoding='utf-8').write(t); n += 1
for f in OUT:
    if os.path.exists(f'{SP}/{f}'):
        t = open(f'{SP}/{f}', encoding='utf-8', errors='ignore').read().replace(SP, '<scratch>')
        open(f'{DST}/{f}', 'w', encoding='utf-8').write(t); n += 1
    else: print('skip (absent)', f)
HOME = os.path.expanduser('~')
bad = [f for f in os.listdir(DST) if os.path.isfile(f'{DST}/{f}') and (SP in open(f'{DST}/{f}', encoding='utf-8', errors='ignore').read() or HOME in open(f'{DST}/{f}', encoding='utf-8', errors='ignore').read())]
assert not bad, bad
print(f'copied {n} files into {DST}; the folder holds {len(os.listdir(DST))} entries')
