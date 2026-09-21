#!/usr/bin/env python3
# sitting 10b — the docket's instruments copied into the forms folder (the scratchpad is not portable): every text file asserted free of a scratch or home
# path before it is written; the chunk prints and the unresolved prints left out (the dump holds their text). 9b's copy form (copy_ch11_docket_forms.py);
# rerun at D2's close with the D2 files added.
import os, shutil, subprocess, sys
ROOT = subprocess.check_output(['git', 'rev-parse', '--show-toplevel'], text=True).strip()
SP = os.path.dirname(os.path.abspath(__file__)); DST = f'{ROOT}/World/step9/forms_deuteronomy_walk'
FILES = ['derive_ch12_docket_tools.py', 'ch12_docket_common.py', 'ch12_docket_rows.py', 'ch12_docket_uncred.py', 'ch12_docket_uncred.out', 'ch12_credit_survey.py',
         'ch12_credit_survey.out', 'ch12_credit_carry.py', 'ch12_credit_carry.out', 'ch12_credited_rows.py', 'ch12_unres_split.py', 'ch12_docket_A.py', 'ch12_docket_B.py', 'ch12_docket_C.py',
         'ch12_d1_check.py', 'ch12_d1_check.out', 'write_ch12_d1_records.py', 'write_ch12_d2a_records.py', 'copy_ch12_docket_forms.py', 'ch12_docket_dump.txt',
         'ch12_docket_D.py', 'ch12_docket_E.py', 'ch12_docket_F.py', 'ch12_docket_G.py', 'ch12_d2_check.py', 'ch12_d2_check.out', 'ch12_d2b_check.out', 'ch12_docket_hdr.py', 'ch12_docket_crowns.py',
         'derive_ch12_docket_writer.py', 'write_ch12_docket.py', 'ch12_docket_write.out', 'write_ch12_docket_records.py']
BAD = ('/private' + '/tmp', '/Users/' + os.path.basename(os.path.expanduser('~')), os.path.expanduser('~'))   # the literals split so this file passes its own check
n = 0; skipped = []
for f in FILES:
    src = f'{SP}/{f}'
    if not os.path.exists(src): skipped.append(f); continue
    t = open(src, encoding='utf-8', errors='replace').read()
    hits = [b for b in BAD if b in t]
    if hits: skipped.append(f'{f} (holds {hits[0].replace(os.path.expanduser("~"), "<home>")})'); continue
    shutil.copyfile(src, f'{DST}/{f}'); n += 1
print('copied %d files into forms_deuteronomy_walk (%d there now); skipped: %s' % (n, len(os.listdir(DST)), skipped))
