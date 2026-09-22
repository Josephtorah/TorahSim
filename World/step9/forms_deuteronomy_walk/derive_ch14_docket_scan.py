import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE DEUTERONOMY WALK sitting 12b — THE COMPILE OF CHAPTER 14: ch14_docket_scan.py DERIVED from the 11b form (the forms folder's ch13_docket_scan.py — its portable
# header stripped, ROOT from git restored) by asserted line-based substitutions — the scanner copied whole; the chapter, its verse count, the Mishnah rows, the
# folio ranges, the whole chapters of the Tosefta and the own ledger's name alone typed; chapter 13's one folded line (the English 12:32 = the DB's 13:1) REMOVED —
# the export's chapter 14 is the DB's 14:1-29 (the identity, asserted at the reading). derive_ch13_docket_scan.py's form. RUN FROM THE REPO ROOT.
import subprocess, os, re
ROOT = _ROOT
SP = os.path.dirname(os.path.abspath(__file__))
src = open(f'{ROOT}/World/step9/forms_deuteronomy_walk/ch13_docket_scan.py', encoding='utf-8').read()
lines = src.split('\n')
if lines[0].startswith('import os as _os'): lines = lines[2:]
def find_line(prefix):
    idx = [i for i, l in enumerate(lines) if l.startswith(prefix)]
    assert len(idx) == 1, ('prefix not unique/absent', prefix[:60], idx); return idx[0]
def rep_line(prefix, new): lines[find_line(prefix)] = new
def rep_block(prefix_first, suffix_last, new):
    i = find_line(prefix_first); js = [k for k in range(i, len(lines)) if lines[k].rstrip().endswith(suffix_last)]
    assert js, ('suffix absent', suffix_last[:60]); lines[i:js[0] + 1] = new
def R(s): return s.strip('\n').split('\n')
rep_block("# THE DEUTERONOMY WALK sitting 11b — THE COMPILE OF CHAPTER 13 (2026-09-21): THE EXAM DOCKET'S SCAN", "earlier dockets' and ledgers' rows).", R(r'''
# THE DEUTERONOMY WALK sitting 12b — THE COMPILE OF CHAPTER 14 (2026-09-21): THE EXAM DOCKET'S SCAN, sized by script before the docket is written
# (ch13_docket_scan.py's form on chapter 14, derived by derive_ch14_docket_scan.py). (1) THE LINK ROWS: every segment of the local shelf's Babylonian
# Talmud, Mishnah and Tosefta exports whose English cites a verse of Deuteronomy 14 (the export's chapter 14 = the DB's 14:1-29 — the identity, asserted at
# the reading; no fold); (2) THE TOPIC ROWS by address (the union rule; COMPILE_DEBT's sitting-12 box (o)): the CANDIDATE ranges SIZED here, the design
# choosing which are read whole — Mishnah Chullin 3:6-7 with Chullin 59a-66b (the signs of the beasts, the fish and the birds; the four; the locusts), 8:1-4 with
# Chullin 113a-116b (the kid — meat in milk), 4:4 with Chullin 72b-73a (the torn; the fetus), 1:7 (the containers), Chullin 68a-69a (the afterbirth), 77a, 80a;
# Mishnah Makkot 3:5-6 with Makkot 20a-21a (the baldness and the cuttings — the lashes); Yevamot 13b-14a (no factions), 47b (the convert), 86a-b (the tithe to
# the Levite); Kiddushin 36a (sons of the LORD), 54b (the second tithe Heaven's); Mishnah Maaser Sheni 1-5 (the second tithe whole); Mishnah Maasrot 1:1, 1:3,
# 2:4, 4:5-6 (the liabilities); Rosh Hashanah 12a-13a (the tithe's year); Bekhorot 34a-35a (the firstling's blemish), 53b (the cattle tithe) with Mishnah
# Bekhorot 9; Mishnah Temurah 6:1 (the altar's disqualified); Mishnah Eduyot 3:2 (the money's form); Mishnah Zevachim 5:8 (the wall); Pesachim 21b (the carcass's
# benefit), 50b-51a (the custom's bar); Bava Metzia 88a (the liability by the courtyard); Mishnah Peah 8:5-9 (the poor man's tithe's measures) with Tosefta
# Peah 4; Tosefta Kilayim 1; Tosefta Sanhedrin 3 (the House standing; the firstling from outside the Land); Avot 3:9, 3:14 (a holy people; sons of the LORD);
# (3) THE PRIOR READS credited (the earlier dockets' and ledgers' rows — the Sifra on Leviticus 11, 19 and 27 from their sittings).
'''))
rep_line("ROOT = _ROOT   # RUN FROM THE REPO ROOT", "ROOT = _ROOT   # RUN FROM THE REPO ROOT")
rep_line("OUT = f'{SCR}/ch13_docket_dump.txt'", "OUT = f'{SCR}/ch14_docket_dump.txt'")
rep_line("CH, NV = 13, 19", "CH, NV = 14, 29")
rep_line("            if c == 12 and a == 32: c, a, z = 13, 1, 1", "            # the export's chapter 14 = the DB's 14:1-29 (the identity, asserted at the reading): no fold")
rep_block("mishnah_rows('Mishnah_Sanhedrin'", "mishnah_rows('Pirkei_Avot', [(2, 1), (3, 9), (3, 14)])", R(r'''
mishnah_rows('Mishnah_Chullin', [(1, 7), (3, 6), (3, 7), (4, 4), (8, 1), (8, 2), (8, 3), (8, 4)])
mishnah_rows('Mishnah_Makkot', [(3, 5), (3, 6)])
mishnah_chapters('Mishnah_Maaser_Sheni', [1, 2, 3, 4, 5])
mishnah_rows('Mishnah_Maasrot', [(1, 1), (1, 3), (2, 4), (4, 5), (4, 6)])
mishnah_rows('Mishnah_Temurah', [(6, 1)])
mishnah_rows('Mishnah_Eduyot', [(3, 2)])
mishnah_rows('Mishnah_Zevachim', [(5, 8)])
mishnah_rows('Mishnah_Peah', [(8, 5), (8, 6), (8, 7), (8, 8), (8, 9)])
mishnah_chapters('Mishnah_Bekhorot', [9])
mishnah_rows('Pirkei_Avot', [(3, 9), (3, 14)])
'''))
rep_block("RANGES = [('Sanhedrin', '67a', '67a')", "('Shabbat', '151b', '151b')]", R(r'''
RANGES = [('Chullin', '59a', '66b'), ('Chullin', '68a', '69a'), ('Chullin', '72b', '73a'), ('Chullin', '77a', '77a'), ('Chullin', '80a', '80a'), ('Chullin', '113a', '116b'), ('Makkot', '20a', '21a'), ('Yevamot', '13b', '14a'), ('Yevamot', '47b', '47b'), ('Yevamot', '86a', '86b'),
          ('Kiddushin', '36a', '36a'), ('Kiddushin', '54b', '54b'), ('Rosh_Hashanah', '12a', '13a'), ('Bekhorot', '34a', '35a'), ('Bekhorot', '53b', '53b'), ('Pesachim', '21b', '21b'), ('Pesachim', '50b', '51a'), ('Bava_Metzia', '88a', '88a')]
'''))
rep_line("# TOSEFTA SANHEDRIN 11", "# TOSEFTA PEAH 4 (the poor man's tithe's measures — 110:3's note, 4:2 and 4:11), TOSEFTA KILAYIM 1 (1:9 — the cleft one), TOSEFTA SANHEDRIN 3 (3:5-6 — the firstling from outside the Land, the House standing) whole; a dict-text export read under its empty key")
rep_line("for w, c in (('Tosefta_Sanhedrin', 11)", "for w, c in (('Tosefta_Peah', 4), ('Tosefta_Kilayim', 1), ('Tosefta_Sanhedrin', 3)):")
rep_line("for wname in ('Tosefta_Sanhedrin', 'Tosefta_Zevachim'", "for wname in ('Tosefta_Peah', 'Tosefta_Kilayim', 'Tosefta_Sanhedrin', 'Mishnah_Maaser_Sheni', 'Mishnah_Maasrot', 'Mishnah_Peah', 'Mishnah_Eduyot', 'Mishnah_Temurah', 'Mishnah_Bekhorot', 'Mishnah_Chullin', 'Pirkei_Avot', 'Chullin', 'Makkot', 'Yevamot', 'Kiddushin', 'Rosh_Hashanah', 'Bekhorot', 'Pesachim', 'Bava_Metzia', 'Sifra'):")
rep_line("own = {'deu_13_reeh_2026-09-21.md'}", "own = {'deu_14_reeh_2026-09-21.md'}")
out = '\n'.join(lines)
bad = [l[:100] for l in out.split('\n') if re.search(r'ch13|sitting 11b|Sanhedrin 67a|12:32|deu_13|Deut 13', l.replace('ch13_docket_scan.py', ''))]
assert not bad, bad
assert '_ROOT' not in out and 'rev-parse' in out and 'CH, NV = 14, 29' in out
open(f'{SP}/ch14_docket_scan.py', 'w', encoding='utf-8').write(out)
print('written', f'{SP}/ch14_docket_scan.py', len(out), 'bytes')
