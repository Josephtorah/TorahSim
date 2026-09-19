#!/usr/bin/env python3
# THE DEUTERONOMY WALK sitting 6 — CHAPTER 8 (2026-09-18, the one run): the sitting's scripts and prints copied from the scratchpad into
# World/step9/forms_deuteronomy_walk/ as the walk's forms — the one run's scripts (the derivation, the dump, the measurement, the ink, the three row
# files, the ledger writer, the display patch, the manifest, the seat, the chain, the fold, the gates chain, the design, the records, this copy) and the
# prints (the dump, the measurement, the Onkelos dump, the outside rows, the store's glosses, the ink runs, the chain log, the ritual, verify_text, the
# claims' verifier, the labels census, the fold's checks, the gates and their summary). Sitting 5's form (copy_ch7_forms.py): no scratch path, no home
# path in a copied form — asserted.
import os, re, subprocess
ROOT = subprocess.check_output(['git', 'rev-parse', '--show-toplevel'], text=True).strip()
SP = os.path.dirname(os.path.abspath(__file__))
DST = f'{ROOT}/World/step9/forms_deuteronomy_walk'; os.makedirs(DST, exist_ok=True)
PY = ['derive_ch8_dump0.py', 'ch8_dump0.py', 'ch8_measure1.py', 'ch8_ink.py', 'ch8_rows_onkelos_a.py', 'ch8_rows_onkelos_b.py', 'ch8_rows_outside.py',
      'write_ch8_ledger.py', 'ch8_patch_overrides.py', 'write_ch8_manifest.py', 'seat_ch8.py', 'write_ch8_design.py', 'write_ch8_records.py', 'copy_ch8_forms.py']
SH = ['ch8_chain.sh', 'ch8_fold.sh', 'ch8_gates.sh']
OUT = ['ch8_dump0.out', 'ch8_measure1.out', 'ch8_onkelos.txt', 'ch8_sifrei_outside.txt', 'ch8_store_glosses.txt', 'ch8_ink_run1.out', 'ch8_ink_run2.out',
       'ch8_ink_run3.out', 'ch8_manifest.out', 'ch8_chain.log', 'ch8_ritual_deu_08_manna_humility.out', 'ch8_vt_deu_08_manna_humility.out', 'ch8_vc.out',
       'ch8_labels.out', 'ch8_fold.out', 'ch8_fold_check1.out', 'ch8_bake.out', 'ch8_build.out', 'ch8_journal.out', 'ch8_register.out', 'ch8_large_letter.out',
       'ch8_home.out', 'ch8_truth.out', 'ch8_gates_SUMMARY.txt', 'ch8_records_check.out']
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
