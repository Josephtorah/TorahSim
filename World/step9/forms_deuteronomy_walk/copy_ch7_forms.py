#!/usr/bin/env python3
# THE DEUTERONOMY WALK sitting 5 — CHAPTER 7 (2026-09-18): the sitting's scripts and prints copied from the scratchpad into
# World/step9/forms_deuteronomy_walk/ as the walk's forms — the four runs' scripts (the derivation, the dump, the measurement, the ink, the three row
# files, the ledger writer, the display patch, the manifest, the seat, the chain and the fold, the checkpoints, the records, this copy) and the prints
# (the dump, the measurement, the Onkelos dump, the outside rows, the store's glosses, the ink runs, the chain log, the ritual, verify_text, the claims'
# verifier, the labels census, the fold's checks, the gates). Sitting 4's form (copy_ch6_forms.py; copy_ch6b_forms.py's home-path replace): no scratch
# path, no home path in a copied form — asserted.
import os, re, subprocess
ROOT = subprocess.check_output(['git', 'rev-parse', '--show-toplevel'], text=True).strip()
SP = os.path.dirname(os.path.abspath(__file__))
DST = f'{ROOT}/World/step9/forms_deuteronomy_walk'; os.makedirs(DST, exist_ok=True)
PY = ['derive_ch7_dump0.py', 'ch7_dump0.py', 'ch7_measure1.py', 'ch7_ink.py', 'ch7_rows_onkelos_a.py', 'ch7_rows_onkelos_b.py', 'ch7_rows_outside.py',
      'write_ch7_ledger.py', 'ch7_patch_overrides.py', 'write_ch7_manifest.py', 'seat_ch7.py', 'write_ch7_design.py', 'write_ch7_run2.py', 'write_ch7_run3.py',
      'write_ch7_records.py', 'copy_ch7_forms.py']
SH = ['ch7_chain.sh', 'ch7_fold.sh']
OUT = ['ch7_dump0.out', 'ch7_measure1.out', 'ch7_onkelos.txt', 'ch7_sifrei_outside.txt', 'ch7_store_glosses.txt', 'ch7_ink_run1.out', 'ch7_ink_run2.out',
       'ch7_ink_run3.out', 'ch7_chain.log', 'ch7_ritual_deu_07_nations_cherem.out', 'ch7_vt_deu_07_nations_cherem.out', 'ch7_vc.out', 'ch7_labels.out',
       'ch7_fold_check1.out', 'ch7_bake.out', 'ch7_build.out', 'ch7_journal.out', 'ch7_register.out', 'ch7_truth.out', 'ch7_records_check.out']
HOME = os.path.expanduser('~')
def scrub(t): return t.replace(SP, '<scratch>').replace(HOME, '<home>')
n = 0
for f in PY + SH:
    src = f'{SP}/{f}'
    if not os.path.exists(src): print('skip (absent)', f); continue
    open(f'{DST}/{f}', 'w', encoding='utf-8').write(scrub(open(src, encoding='utf-8').read())); n += 1
for f in OUT:
    if os.path.exists(f'{SP}/{f}'):
        open(f'{DST}/{f}', 'w', encoding='utf-8').write(scrub(open(f'{SP}/{f}', encoding='utf-8', errors='ignore').read())); n += 1
    else: print('skip (absent)', f)
bad = [f for f in os.listdir(DST) if os.path.isfile(f'{DST}/{f}') and (SP in open(f'{DST}/{f}', encoding='utf-8', errors='ignore').read() or HOME in open(f'{DST}/{f}', encoding='utf-8', errors='ignore').read())]
assert not bad, bad
print(f'copied {n} files into {DST}; the folder holds {len(os.listdir(DST))} entries')
