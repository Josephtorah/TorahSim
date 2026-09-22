import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE DEUTERONOMY WALK sitting 11b — THE COMPILE OF CHAPTER 13: ch13_docket_scan.py DERIVED from the 10b form (the scratchpad's ch12_docket_scan.py) by asserted
# line-based substitutions — the scanner copied whole; the chapter, its verse count, the Mishnah rows, the folio ranges, the whole chapters of the Tosefta and the
# Sifrei on Numbers, and the own ledger's name alone typed; ONE new line — the English numbering's 12:32 folded to the DB's 13:1 (the header). derive_ch12_docket_scan.py's form.
import subprocess, os, re
ROOT = _ROOT
SP = os.path.dirname(os.path.abspath(__file__))
src = open(f'{SP}/ch12_docket_scan.py', encoding='utf-8').read()
lines = src.split('\n')
if lines[0].startswith('import os as _os'): lines = lines[2:]
def find_line(prefix):
    idx = [i for i, l in enumerate(lines) if l.startswith(prefix)]
    assert len(idx) == 1, ('prefix not unique/absent', prefix[:60], idx); return idx[0]
def rep_line(prefix, new): lines[find_line(prefix)] = new
def rep_block(prefix_first, suffix_last, new):
    i = find_line(prefix_first); js = [k for k in range(i, len(lines)) if lines[k].rstrip().endswith(suffix_last)]
    assert js, ('suffix absent', suffix_last[:60]); lines[i:js[0] + 1] = new
rep_block("# THE DEUTERONOMY WALK sitting 10b — THE COMPILE OF CHAPTER 12 (2026-09-20): THE EXAM DOCKET'S SCAN", "(3) THE PRIOR READS credited (the earlier dockets' and ledgers' rows).", [
"# THE DEUTERONOMY WALK sitting 11b — THE COMPILE OF CHAPTER 13 (2026-09-21): THE EXAM DOCKET'S SCAN, sized by script before the docket is written",
"# (ch12_docket_scan.py's form on chapter 13, derived by derive_ch13_docket_scan.py). (1) THE LINK ROWS: every segment of the local shelf's Babylonian",
"# Talmud, Mishnah and Tosefta exports whose English cites a verse of Deuteronomy 13 (the export's chapter 13 = the DB's 13:1-19 — the identity, asserted at",
"# the reading; the English numbering's 12:32 is the DB's 13:1 — a citation of 12:32 is FOLDED to 13:1 here, the header); (2) THE TOPIC ROWS by address (the",
"# union rule; COMPILE_DEBT's sitting-11 box (l)): the CANDIDATE ranges SIZED here, the design choosing which are read whole — Mishnah Sanhedrin 7:10 with",
"# Sanhedrin 67a (the inciter — the concealed witnesses), 7:6 (the honors of an idol), 10:4-6 with Sanhedrin 111b-113b (the condemned city), 11:1 and 11:5-6 with",
"# Sanhedrin 89a-90a (the false prophet strangled; the sign), 5:1-2 with Sanhedrin 40a-41a (the seven inquiries and the probes), 1:5 (one city), 11:4 (the",
"# festival's execution), 4:1 (the verdict returned), Sanhedrin 88b (the rebellious elder and the not-adding); Mishnah Makkot 1:4-6 (the plotting witness);",
"# Mishnah Zevachim 8:10 with Zevachim 80a-81b (the mixed bloods); Mishnah Sukkah 3:4 with Sukkah 34b and Menachot 41b-42a (the four species; the fringes); Rosh",
"# Hashanah 28b and Eruvin 96a (the priests' blessing not added to); Mishnah Avodah Zarah 3:9 with Avodah Zarah 49b-50a (the benefit to the Salt Sea); Bava",
"# Metzia 59b (the prophet's sign not decisive) and Yevamot 90b (the prophet's temporary uprooting); Shabbat 151b (the mercy two-armed); Avot 2:1, 3:9, 3:14;",
"# Tosefta Sanhedrin 11, 12 and 14, Tosefta Zevachim 8, Tosefta Bava Kamma 9 and the Sifrei on Numbers 103, 113, 114 whole; (3) THE PRIOR READS credited (the",
"# earlier dockets' and ledgers' rows)."])
rep_line("OUT = f'{SCR}/ch12_docket_dump.txt'", "OUT = f'{SCR}/ch13_docket_dump.txt'")
rep_line("CH, NV = 12, 31", "CH, NV = 13, 19")
rep_line("            if c != CH: continue", "            if c == 12 and a == 32: c, a, z = 13, 1, 1   # THE ENGLISH NUMBERING'S 12:32 IS THE DB'S 13:1 (the header) — folded in\n            if c != CH: continue")
rep_block("mishnah_rows('Mishnah_Zevachim'", "mishnah_rows('Pirkei_Avot', [(2, 1)])", [
"mishnah_rows('Mishnah_Sanhedrin', [(1, 5), (4, 1), (5, 1), (5, 2), (7, 6), (7, 10), (10, 4), (10, 5), (10, 6), (11, 1), (11, 4), (11, 5), (11, 6)])",
"mishnah_rows('Mishnah_Makkot', [(1, 4), (1, 5), (1, 6)])", "mishnah_rows('Mishnah_Zevachim', [(8, 10)])", "mishnah_rows('Mishnah_Sukkah', [(3, 4)])", "mishnah_rows('Mishnah_Avodah_Zarah', [(3, 9)])", "mishnah_rows('Pirkei_Avot', [(2, 1), (3, 9), (3, 14)])"])
rep_block("RANGES = [", "('Pesachim', '8b', '8b')]", [
"RANGES = [('Sanhedrin', '67a', '67a'), ('Sanhedrin', '88b', '88b'), ('Sanhedrin', '89a', '90a'), ('Sanhedrin', '40a', '41a'), ('Sanhedrin', '111b', '113b'), ('Zevachim', '80a', '81b'), ('Sukkah', '34b', '34b'), ('Menachot', '41b', '42a'),",
"          ('Rosh_Hashanah', '28b', '28b'), ('Eruvin', '96a', '96a'), ('Avodah_Zarah', '49b', '50a'), ('Bava_Metzia', '59b', '59b'), ('Yevamot', '90b', '90b'), ('Shabbat', '151b', '151b')]"])
rep_block("# TOSEFTA ZEVACHIM 4 (78:1-2", "for w, c in (('Tosefta_Zevachim', 4), ('Tosefta_Shekalim', 2), ('Tosefta_Menachot', 9), ('Seder_Olam_Rabbah', 11)):", [
"# TOSEFTA SANHEDRIN 11 (the festival's execution — 91:2's note), 12 (the honors), 14 (the condemned city — 93:3, 94:6's notes), TOSEFTA ZEVACHIM 8 (the mixed bloods — 82:3's note), TOSEFTA BAVA KAMMA 9 (the mercy — 96:4) and THE SIFREI ON NUMBERS 103, 113, 114 (the English's parallels) whole; a dict-text export read under its empty key",
"for w, c in (('Tosefta_Sanhedrin', 11), ('Tosefta_Sanhedrin', 12), ('Tosefta_Sanhedrin', 14), ('Tosefta_Zevachim', 8), ('Tosefta_Bava_Kamma', 9), ('Sifrei_Bamidbar', 103), ('Sifrei_Bamidbar', 113), ('Sifrei_Bamidbar', 114)):"])
rep_line("for wname in ('Tosefta_Zevachim', 'Tosefta_Shekalim'", "for wname in ('Tosefta_Sanhedrin', 'Tosefta_Zevachim', 'Tosefta_Bava_Kamma', 'Sifrei_Bamidbar', 'Mishnah_Sukkah', 'Pirkei_Avot', 'Bava_Metzia', 'Eruvin', 'Rosh_Hashanah', 'Shabbat', 'Yevamot', 'Menachot'):")
rep_line("    rows = T[c - 1]; rows = rows if isinstance(rows, list) else [rows]", "    if c - 1 >= len(T): print('CHAPTER PAST THE END OF THE EXPORT: %s %d (the export holds %d top-level entries)' % (w, c, len(T))); continue\n    rows = T[c - 1]; rows = rows if isinstance(rows, list) else [rows]")
rep_line("own = {'deu_12_reeh_2026-09-20.md'}", "own = {'deu_13_reeh_2026-09-21.md'}")
out = '\n'.join(lines)
assert 'ch12' not in out.replace('ch12_docket_scan.py', '') and 'Zevachim 14' not in out and 'Chullin' not in out and 'Seder Olam' not in out and 'Pesachim' not in out, [l[:80] for l in out.split('\n') if 'ch12' in l or 'Chullin' in l or 'Pesachim' in l]
open(f'{SP}/ch13_docket_scan.py', 'w', encoding='utf-8').write(out)
print('written', f'{SP}/ch13_docket_scan.py', len(out), 'bytes')
