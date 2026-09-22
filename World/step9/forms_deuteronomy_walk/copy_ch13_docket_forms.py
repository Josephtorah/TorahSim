#!/usr/bin/env python3
# sitting 11b — the docket's instruments copied into the forms folder (the scratchpad is not portable): every text file asserted free of a scratch or home
# path before it is written; the chunk prints and the unresolved print left out (the dump holds their text). 10b's copy form (copy_ch12_docket_forms.py).
import os, shutil, subprocess, sys
ROOT = subprocess.check_output(['git', 'rev-parse', '--show-toplevel'], text=True).strip()
SP = os.path.dirname(os.path.abspath(__file__)); DST = f'{ROOT}/World/step9/forms_deuteronomy_walk'
FILES = ['derive_ch13_docket_tools.py', 'ch13_docket_common.py', 'ch13_docket_rows.py', 'ch13_docket_uncred.py', 'ch13_docket_uncred.out', 'ch13_credit_survey.py',
         'ch13_credit_survey.out', 'ch13_credit_carry.py', 'ch13_credit_carry.out', 'ch13_credited_rows.py', 'ch13_docket_U.py', 'ch13_docket_A.py', 'ch13_docket_B.py',
         'ch13_docket_C.py', 'ch13_docket_D.py', 'ch13_d1_check.py', 'ch13_d1_check.out', 'ch13_docket_hdr.py', 'ch13_docket_crowns.py', 'derive_ch13_docket_writer.py',
         'write_ch13_docket.py', 'ch13_docket_write.out', 'write_ch13_docket_records.py', 'copy_ch13_docket_forms.py', 'ch13_docket_dump.txt']
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
