#!/usr/bin/env python3
# THE DEUTERONOMY WALK sitting 9b — THE COMPILE OF CHAPTER 11: ch11_docket_scan.py DERIVED from the 8b form (ch10_docket_scan.py in the forms folder) by
# asserted line-based substitutions — the scanner copied whole; the chapter, its verse count, the Mishnah rows, the folio ranges, the Tosefta chapters and
# the own ledger's name alone typed.
import subprocess, os, re
ROOT = subprocess.check_output(['git', 'rev-parse', '--show-toplevel'], text=True).strip()
SP = os.path.dirname(os.path.abspath(__file__))
src = open(f'{ROOT}/World/step9/forms_deuteronomy_walk/ch10_docket_scan.py', encoding='utf-8').read()
lines = src.split('\n')
if lines[0].startswith('import os as _os'): lines = lines[2:]
def find_line(prefix):
    idx = [i for i, l in enumerate(lines) if l.startswith(prefix)]
    assert len(idx) == 1, ('prefix not unique/absent', prefix[:60], idx); return idx[0]
def rep_line(prefix, new): lines[find_line(prefix)] = new
def rep_block(prefix_first, suffix_last, new):
    i = find_line(prefix_first); js = [k for k in range(i, len(lines)) if lines[k].rstrip().endswith(suffix_last)]
    assert js, ('suffix absent', suffix_last[:60]); lines[i:js[0] + 1] = new
def sub_in_line(prefix, old, new, n=1):
    i = find_line(prefix); assert lines[i].count(old) == n, (prefix[:40], old, lines[i].count(old)); lines[i] = lines[i].replace(old, new)
if any(l.startswith('ROOT = _ROOT') for l in lines): rep_line('ROOT = _ROOT', "ROOT = subprocess.check_output(['git', 'rev-parse', '--show-toplevel'], text=True).strip()   # RUN FROM THE REPO ROOT")
rep_block("# THE DEUTERONOMY WALK sitting 8b — THE COMPILE OF CHAPTER 10 (2026-09-20): THE EXAM DOCKET'S SCAN", "the earlier dockets' rows among them).", [
"# THE DEUTERONOMY WALK sitting 9b — THE COMPILE OF CHAPTER 11 (2026-09-20): THE EXAM DOCKET'S SCAN, sized by script before the docket is written",
"# (ch10_docket_scan.py's form on chapter 11, derived by derive_ch11_docket_scan.py). (1) THE LINK ROWS: every segment of the local shelf's Babylonian",
"# Talmud, Mishnah and Tosefta exports whose English cites a verse of Deuteronomy 11 (the export's chapter 11 = the DB's — the identity, asserted at the",
"# reading); (2) THE TOPIC ROWS by address (the union rule; COMPILE_DEBT's sitting-9 box (n)): the CANDIDATE ranges SIZED here, the design choosing which",
"# are read whole — Mishnah Berakhot 2:2 and Berakhot 13a-16a (the paragraphs' order); Menachot 34a-37b and Kiddushin 29a-30b (credited from 4b's docket);",
"# Kiddushin 36b-37a (the land-bound) and 40b (study and deed); Ta'anit 2a-3a and 7a-10a with Mishnah Ta'anit 1:1-3 and Berakhot 33a (the rain); Rosh",
"# Hashanah 16a-17b with Mishnah Rosh Hashanah 1:2 (the year judged); Gittin 8a with Mishnah Sheviit 6:1 (the borders); Pesachim 8b (the pilgrimage guarded);",
"# Sotah 32a-37b with Mishnah Sotah 7:2-5 (the ceremony; Gerizim and Ebal; idolatry); Ketubot 110b-111a (the dwelling); Sanhedrin 90b (the resurrection);",
"# Sukkah 52a (the inclination — credited from 8b); Mishnah Kiddushin 1:7, 1:9 and Menachot 3:7 (sons; the land-bound; the four compartments); Tosefta Sotah 8",
"# and Tosefta Sheviit 4 (the ceremony's form; the baraita of the borders); (3) THE PRIOR READS credited (the earlier dockets' and ledgers' rows)."])
rep_line("OUT = f'{SCR}/ch10_docket_dump.txt'", "OUT = f'{SCR}/ch11_docket_dump.txt'")
rep_line("CH, NV = 10, 22", "CH, NV = 11, 32")
rep_block("mishnah_rows('Mishnah_Shekalim'", "mishnah_rows('Mishnah_Berakhot', [(9, 5)])", [
"mishnah_rows('Mishnah_Berakhot', [(2, 2)])", "mishnah_rows('Mishnah_Sheviit', [(6, 1)])", "mishnah_rows('Mishnah_Rosh_Hashanah', [(1, 2)])", "mishnah_rows('Mishnah_Taanit', [(1, 1), (1, 2), (1, 3)])",
"mishnah_rows('Mishnah_Sotah', [(7, 2), (7, 3), (7, 4), (7, 5)])", "mishnah_rows('Mishnah_Kiddushin', [(1, 7), (1, 9)])", "mishnah_rows('Mishnah_Menachot', [(3, 7)])"])
rep_block("RANGES = [", "('Taanit', '9a', '9a')]", [
"RANGES = [('Berakhot', '13a', '16a'), ('Menachot', '34a', '37b'), ('Kiddushin', '29a', '30b'), ('Kiddushin', '36b', '37a'), ('Kiddushin', '40b', '40b'), ('Taanit', '2a', '3a'), ('Taanit', '7a', '10a'), ('Berakhot', '33a', '33a'),",
"          ('Rosh_Hashanah', '16a', '17b'), ('Gittin', '8a', '8a'), ('Pesachim', '8b', '8b'), ('Sotah', '32a', '37b'), ('Ketubot', '110b', '111a'), ('Sanhedrin', '90b', '90b'), ('Sukkah', '52a', '52a')]"])
rep_block("# SEDER OLAM RABBAH 6, 9, 10", "for w, c in (('Seder_Olam_Rabbah', 6), ('Seder_Olam_Rabbah', 9), ('Seder_Olam_Rabbah', 10), ('Tosefta_Sotah', 7)):", [
"# TOSEFTA SOTAH 8 (the ceremony's form — 55:2's likening) and TOSEFTA SHEVIIT 4 (the baraita of the borders — 51:3's names) whole; a dict-text export read under its empty key",
"for w, c in (('Tosefta_Sotah', 8), ('Tosefta_Sheviit', 4)):"])
rep_line("for wname in ('Tosefta_Sotah', 'Seder_Olam_Rabbah'", "for wname in ('Tosefta_Sotah', 'Tosefta_Sheviit', 'Tosefta_Berakhot', 'Tosefta_Taanit', 'Tosefta_Kiddushin'):")
rep_line("own = {'deu_10_ekev_2026-09-19.md'}", "own = {'deu_11_ekev_reeh_2026-09-20.md'}")
out = '\n'.join(lines)
assert 'ch10' not in out.replace('ch10_docket_scan.py', '') and 'Shekalim' not in out and 'Seder' not in out.replace('a dict-text', ''), [l[:80] for l in out.split('\n') if 'ch10' in l or 'Shekalim' in l or 'Seder' in l]
open(f'{SP}/ch11_docket_scan.py', 'w', encoding='utf-8').write(out)
print('written', f'{SP}/ch11_docket_scan.py', len(out), 'bytes')
