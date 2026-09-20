#!/usr/bin/env python3
# sitting 9b — RUN A's and the docket's instruments copied into the forms folder (the scratchpad is not portable): every text file asserted free of a
# scratch or home path before it is written; the ten chunk prints left out (the dump holds their text); the three patch scripts that name the scratch path
# by design left out by the check. 8b's copy form (copy_ch10_docket_forms.py).
import os, shutil, subprocess, sys
ROOT = subprocess.check_output(['git', 'rev-parse', '--show-toplevel'], text=True).strip()
SP = os.path.dirname(os.path.abspath(__file__)); DST = f'{ROOT}/World/step9/forms_deuteronomy_walk'
FILES = ['derive_ch11_recon.py', 'ch11_compile_recon.py', 'ch11_recon.out', 'derive_ch11_docket_scan.py', 'ch11_docket_scan.py', 'ch11_docket_scan.out',
         'ch11_docket_dump.txt', 'write_ch11b_design.py', 'ch11_docket_common.py', 'ch11_docket_rows.py', 'ch11_docket_uncred.py', 'ch11_credit_survey.py',
         'ch11_credit_carry.py', 'ch11_credited_rows.py', 'ch11_docket_A.py', 'ch11_docket_B.py', 'ch11_docket_C.py', 'ch11_docket_hdr.py', 'ch11_docket_crowns.py',
         'derive_ch11_docket_writer.py', 'write_ch11_docket.py', 'ch11_docket_write.out', 'write_ch11_docket_records.py', 'copy_ch11_docket_forms.py']
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
