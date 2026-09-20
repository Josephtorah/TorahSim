#!/usr/bin/env python3
# sitting 8b — RUN A's and the docket's instruments copied into the forms folder (the scratchpad is not portable): every text file asserted free of a
# scratch or home path before it is written; the six row prints left out (the dump holds their text). 7b's copy form.
import os, shutil, subprocess, sys
ROOT = subprocess.check_output(['git', 'rev-parse', '--show-toplevel'], text=True).strip()
SP = os.path.dirname(os.path.abspath(__file__)); DST = f'{ROOT}/World/step9/forms_deuteronomy_walk'
FILES = ['derive_ch10_recon.py', 'ch10_compile_recon.py', 'ch10_recon.out', 'ch10_measure2.py', 'ch10_measure2.out', 'ch10_measure3.py', 'derive_ch10_docket_scan.py',
         'ch10_docket_scan.py', 'ch10_docket_scan.out', 'ch10_docket_dump.txt', 'ch10_docket_rows.py', 'ch10_docket_common.py', 'ch10_docket_A.py', 'ch10_docket_B.py',
         'ch10_docket_C.py', 'write_ch10_docket.py', 'ch10_docket_write.out', 'write_ch10b_design.py', 'write_ch10_docket_records.py', 'copy_ch10_docket_forms.py']
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
