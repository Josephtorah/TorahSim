#!/usr/bin/env python3
# sitting 12b — the docket's instruments (two runs) copied into the forms folder (the scratchpad is not portable): every text file asserted free of a scratch or home
# path before it is written; the chunk prints and the unresolved print left out (the dump holds their text). 11b's copy form (copy_ch13_docket_forms.py).
import os, shutil, subprocess, sys
ROOT = subprocess.check_output(['git', 'rev-parse', '--show-toplevel'], text=True).strip()
SP = os.path.dirname(os.path.abspath(__file__)); DST = f'{ROOT}/World/step9/forms_deuteronomy_walk'
FILES = ['derive_ch14_docket_tools.py', 'ch14_docket_common.py', 'ch14_docket_rows.py', 'ch14_docket_uncred.py', 'ch14_docket_uncred.out', 'ch14_credit_survey.py',
         'ch14_credit_survey.out', 'ch14_credit_carry.py', 'ch14_credit_carry.out', 'ch14_credited_rows.py', 'ch14_docket_U.py', 'ch14_docket_A.py', 'ch14_docket_B.py',
         'ch14_docket_C.py', 'ch14_docket_D.py', 'ch14_docket_E.py', 'ch14_docket_F.py', 'ch14_docket_G.py', 'ch14_d1_check.py', 'ch14_d1_check.out', 'ch14_d2_check.out',
         'write_ch14_d1_cleanpoint.py', 'ch14_docket_hdr.py', 'ch14_docket_crowns.py', 'derive_ch14_docket_writer.py', 'write_ch14_docket.py', 'ch14_docket_write.out',
         'write_ch14_docket_records.py', 'copy_ch14_docket_forms.py', 'ch14_docket_dump.txt']
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
