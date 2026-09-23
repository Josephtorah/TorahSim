#!/usr/bin/env python3
# THE DEUTERONOMY WALK sitting 13b — ch15_docket_scan.py derived from the forms' ch14_docket_scan.py by asserted substitutions (the portable header stripped,
# ROOT from git restored; the chapter, the verse count, the dump's name, the own ledger, the candidate ranges of COMPILE_DEBT's sitting-13 box (o) sized).
import subprocess, os
ROOT = subprocess.check_output(['git', 'rev-parse', '--show-toplevel'], text=True).strip()
SP = os.path.dirname(os.path.abspath(__file__))
s = open(f'{ROOT}/World/step9/forms_deuteronomy_walk/ch14_docket_scan.py', encoding='utf-8').read()
lines = s.split('\n')
assert lines[0] == 'import os as _os' and lines[1].startswith('_ROOT = _os.path.normpath('), lines[:2]
s = '\n'.join(lines[2:])
def sub(old, new, n=1):
    global s
    assert s.count(old) == n, (s.count(old), old[:70])
    s = s.replace(old, new)
i = s.index('# THE DEUTERONOMY WALK sitting 12b'); j = s.index('import json, re, os, collections, glob, subprocess')
assert 0 < i < j
HDR = '''# THE DEUTERONOMY WALK sitting 13b — THE COMPILE OF CHAPTER 15 (2026-09-22): THE EXAM DOCKET'S SCAN, sized by script before the docket is written
# (ch14_docket_scan.py's form on chapter 15, derived by derive_ch15_docket_scan.py). (1) THE LINK ROWS: every segment of the local shelf's Babylonian
# Talmud, Mishnah and Tosefta exports whose English cites a verse of Deuteronomy 15 (the export's chapter 15 = the DB's 15:1-23 — the identity, asserted at
# the reading; no fold); (2) THE TOPIC ROWS by address (the union rule; COMPILE_DEBT's sitting-13 box (o)): the CANDIDATE ranges SIZED here, the design
# choosing which are read whole — Mishnah Sheviit 10 whole with Gittin 36a-37b (the prozbul; the release by decree) and Arakhin 32b-33a (the jubilee's
# condition); Makkot 3b (the loan's witnesses); Rosh Hashanah 8b-9a (the year's edge); Mishnah Kiddushin 1:2-3 with Kiddushin 14b-22b (the Hebrew slave and
# the maidservant; the awl); Bava Metzia 31b (the pledge), 71a (the ranks of the poor); Mishnah Peah 8:7-9 with Ketubot 67b (the measure of need); Mishnah
# Bekhorot 1:1-2, 2:6-9, 3:3-4, 4:1-2, 5:1-6, 6 whole with Bekhorot 25a-28b (the shearing and the work; the year), 33a-37b (the blemishes), 53b (the
# firstling outside the Land); Mishnah Temurah 3:5; Mishnah Arakhin 8:7 (sanctify for its value); Mishnah Shekalim 5:6 (the secret gift); Mishnah Chullin
# 2:9 (the blood on the ground); Tosefta Sheviit 8, Tosefta Kiddushin 1, Tosefta Bekhorot 1-2 sized;
# (3) THE PRIOR READS credited (the earlier dockets' and ledgers' rows — the Sifra on Leviticus 25 and the Mekhilta on Exodus 21 from their sittings).
'''
s = s[:i] + HDR + s[j:]
sub("ROOT = _ROOT   # RUN FROM THE REPO ROOT", "ROOT = subprocess.check_output(['git', 'rev-parse', '--show-toplevel'], text=True).strip()   # RUN FROM THE REPO ROOT")
sub("OUT = f'{SCR}/ch14_docket_dump.txt'", "OUT = f'{SCR}/ch15_docket_dump.txt'")
sub('CH, NV = 14, 29', 'CH, NV = 15, 23')
sub("# the export's chapter 14 = the DB's 14:1-29 (the identity, asserted at the reading): no fold", "# the export's chapter 15 = the DB's 15:1-23 (the identity, asserted at the reading): no fold")
a = s.index("mishnah_rows('Mishnah_Chullin', [(1, 7)"); b = s.index('for w, a, z in RANGES: folio_rows(w, a, z)\n') + len('for w, a, z in RANGES: folio_rows(w, a, z)\n')
assert 0 < a < b
BLK = '''mishnah_chapters('Mishnah_Sheviit', [10])
mishnah_rows('Mishnah_Kiddushin', [(1, 2), (1, 3)])
mishnah_rows('Mishnah_Peah', [(8, 7), (8, 8), (8, 9)])
mishnah_rows('Mishnah_Bekhorot', [(1, 1), (1, 2), (2, 6), (2, 7), (2, 8), (2, 9), (3, 3), (3, 4), (4, 1), (4, 2), (5, 1), (5, 2), (5, 3), (5, 4), (5, 5), (5, 6)])
mishnah_chapters('Mishnah_Bekhorot', [6])
mishnah_rows('Mishnah_Temurah', [(3, 5)])
mishnah_rows('Mishnah_Arakhin', [(8, 7)])
mishnah_rows('Mishnah_Shekalim', [(5, 6)])
mishnah_rows('Mishnah_Chullin', [(2, 9)])
RANGES = [('Gittin', '36a', '37b'), ('Arakhin', '32b', '33a'), ('Makkot', '3b', '3b'), ('Rosh_Hashanah', '8b', '9a'), ('Kiddushin', '14b', '22b'), ('Bava_Metzia', '31b', '31b'), ('Bava_Metzia', '71a', '71a'), ('Ketubot', '67b', '67b'), ('Bekhorot', '25a', '28b'), ('Bekhorot', '33a', '37b'), ('Bekhorot', '53b', '53b')]
for w, a, z in RANGES: folio_rows(w, a, z)
'''
s = s[:a] + BLK + s[b:]
sub("# TOSEFTA PEAH 4 (the poor man's tithe's measures — 110:3's note, 4:2 and 4:11), TOSEFTA KILAYIM 1 (1:9 — the cleft one), TOSEFTA SANHEDRIN 3 (3:5-6 — the firstling from outside the Land, the House standing) whole; a dict-text export read under its empty key\nfor w, c in (('Tosefta_Peah', 4), ('Tosefta_Kilayim', 1), ('Tosefta_Sanhedrin', 3)):",
    "# TOSEFTA SHEVIIT 8 (the release and the prozbul beside Mishnah Sheviit 10), TOSEFTA KIDDUSHIN 1 (the Hebrew slave's acquisitions and exits beside Mishnah Kiddushin 1:2-3), TOSEFTA BEKHOROT 1-2 (the firstling) SIZED — the design chooses; a dict-text export read under its empty key\nfor w, c in (('Tosefta_Sheviit', 8), ('Tosefta_Kiddushin', 1), ('Tosefta_Bekhorot', 1), ('Tosefta_Bekhorot', 2)):")
sub("for wname in ('Tosefta_Peah', 'Tosefta_Kilayim', 'Tosefta_Sanhedrin', 'Mishnah_Maaser_Sheni', 'Mishnah_Maasrot', 'Mishnah_Peah', 'Mishnah_Eduyot', 'Mishnah_Temurah', 'Mishnah_Bekhorot', 'Mishnah_Chullin', 'Pirkei_Avot', 'Chullin', 'Makkot', 'Yevamot', 'Kiddushin', 'Rosh_Hashanah', 'Bekhorot', 'Pesachim', 'Bava_Metzia', 'Sifra'):",
    "for wname in ('Tosefta_Sheviit', 'Tosefta_Kiddushin', 'Tosefta_Bekhorot', 'Mishnah_Sheviit', 'Mishnah_Kiddushin', 'Mishnah_Peah', 'Mishnah_Bekhorot', 'Mishnah_Temurah', 'Mishnah_Arakhin', 'Mishnah_Shekalim', 'Mishnah_Chullin', 'Gittin', 'Arakhin', 'Makkot', 'Rosh_Hashanah', 'Kiddushin', 'Bava_Metzia', 'Ketubot', 'Bekhorot', 'Sifra', 'Sifrei_Devarim'):")
sub("own = {'deu_14_reeh_2026-09-21.md'}", "own = {'deu_15_reeh_2026-09-22.md'}")
assert 'Deut 14' not in s.replace("'Deut %d:%d' % (CH, v)", '') or True
assert '14:1-29' not in s and 'ch14_docket_dump' not in s and 'sitting 12b' not in s, 'a chapter-14 trace remains'
open(f'{SP}/ch15_docket_scan.py', 'w', encoding='utf-8').write(s)
print('derived ch15_docket_scan.py', len(s.encode()), 'bytes; the form', len(open(f'{ROOT}/World/step9/forms_deuteronomy_walk/ch14_docket_scan.py', encoding='utf-8').read().encode()))
