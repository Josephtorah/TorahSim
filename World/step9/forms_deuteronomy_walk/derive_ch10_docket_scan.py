#!/usr/bin/env python3
# sitting 8b: ch10_docket_scan.py derived from the 7b form (ch9_docket_scan.py) by asserted substitutions — the chapter, the ranges, the Mishnah rows, the midrashim.
import subprocess, os, re
ROOT = subprocess.check_output(['git', 'rev-parse', '--show-toplevel'], text=True).strip()
SP = os.path.dirname(os.path.abspath(__file__))
src = open(f'{ROOT}/World/step9/forms_deuteronomy_walk/ch9_docket_scan.py', encoding='utf-8').read()
def rep_block(s, first, last, new):
    assert s.count(first) == 1, ('first', first[:70], s.count(first)); i = s.index(first)
    assert s.count(last) == 1, ('last', last[:70], s.count(last)); j = s.index(last, i) + len(last)
    return s[:i] + new + s[j:]
def rep(s, old, new, n=1):
    assert s.count(old) == n, ('rep', old[:70], s.count(old)); return s.replace(old, new)
lines = src.split('\n'); assert lines[0].startswith('import os as _os') and lines[1].startswith('_ROOT ='); src = '\n'.join(lines[2:])
src = rep(src, "ROOT = _ROOT", "ROOT = subprocess.check_output(['git', 'rev-parse', '--show-toplevel'], text=True).strip()   # RUN FROM THE REPO ROOT")
src = rep_block(src, "# THE DEUTERONOMY WALK sitting 7b — THE COMPILE OF CHAPTER 9", "credited (the Numbers walk's and the earlier dockets' Berakhot rows among them).",
"""# THE DEUTERONOMY WALK sitting 8b — THE COMPILE OF CHAPTER 10 (2026-09-20): THE EXAM DOCKET'S SCAN, sized by script before the docket is written
# (ch9_docket_scan.py's form on chapter 10, derived by derive_ch10_docket_scan.py). (1) THE LINK ROWS: every segment of the local shelf's Babylonian
# Talmud, Mishnah and Tosefta exports whose English cites a verse of Deuteronomy 10 (the export's chapter 10 = the DB's — the identity, asserted at the
# reading); (2) THE TOPIC ROWS by address (the union rule; COMPILE_DEBT's sitting-8 box (n)): the CANDIDATE ranges SIZED here, the design choosing which
# are read whole — Bava Batra 14a-b, Menachot 99a-b, Berakhot 8b (the ark and the fragments); Mishnah Shekalim 6:1-2 (the ark hidden); Berakhot 33b,
# Menachot 43b, Shabbat 31b, Sotah 14a (the demand and the ways); Yoma 69b, Megillah 25a, Berakhot 20b, Niddah 70b, Mishnah Berakhot 9:5 (the
# attributes, the face); Ketubot 105a-b (the bribe); Bava Metzia 59b, Yevamot 47a-b (the stranger); Ketubot 111b (cleave); Shevuot 35b, Temurah 3b-4a,
# Sanhedrin 56a (the Name, the oath); Bava Batra 123a-b (the seventy); Rosh Hashanah 3a, Ta'anit 9a, Seder Olam 6 and 9-10 (Aaron and the forty);
# Mishnah Sotah 7:6 (the blessing in the Name); (3) THE PRIOR READS credited (the Numbers walk's, the erection's and the earlier dockets' rows among them).""")
src = rep(src, "OUT = f'{SCR}/ch9_docket_dump.txt'", "OUT = f'{SCR}/ch10_docket_dump.txt'")
src = rep(src, "CH, NV = 9, 29", "CH, NV = 10, 22")
src = rep_block(src, "mishnah_chapters('Mishnah_Avodah_Zarah', [3])", "mishnah_rows('Mishnah_Yoma', [(8, 8), (8, 9)])",
"mishnah_rows('Mishnah_Shekalim', [(6, 1), (6, 2)])\nmishnah_rows('Mishnah_Sotah', [(7, 6)])\nmishnah_rows('Mishnah_Berakhot', [(9, 5)])")
src = rep_block(src, "RANGES = [('Taanit', '26a', '26a')", "('Yoma', '86b', '86b')]",
"""RANGES = [('Bava_Batra', '14a', '14b'), ('Menachot', '99a', '99b'), ('Berakhot', '8b', '8b'), ('Berakhot', '33b', '33b'), ('Menachot', '43b', '43b'), ('Shabbat', '31b', '31b'), ('Sotah', '14a', '14a'),
          ('Yoma', '69b', '69b'), ('Megillah', '25a', '25a'), ('Berakhot', '20b', '20b'), ('Niddah', '70b', '70b'), ('Ketubot', '105a', '105b'), ('Bava_Metzia', '59b', '59b'), ('Yevamot', '47a', '47b'),
          ('Ketubot', '111b', '111b'), ('Shevuot', '35b', '35b'), ('Temurah', '3b', '4a'), ('Sanhedrin', '56a', '56a'), ('Bava_Batra', '123a', '123b'), ('Rosh_Hashanah', '3a', '3a'), ('Taanit', '9a', '9a')]""")
src = rep(src, "# THE MIDRASHIM NAMED IN THE BOX (Vayikra Rabbah 10:5 — Aaron's sons; Devarim Rabbah 2:1 — the ten names of prayer): sized if the export holds them",
          "# THE MIDRASHIM AND THE TOSEFTA NAMED IN THE BOX (Seder Olam Rabbah 6, 9, 10 — the forties, Aaron's death and the retreat; Tosefta Sotah 7:18 — the two arks): sized if the export holds them")
src = rep(src, "for w, c, m in (('Vayikra_Rabbah', 10, 5), ('Devarim_Rabbah', 2, 1), ('Seder_Olam_Rabbah', 6, 0)):", "for w, c, m in (('Seder_Olam_Rabbah', 6, 0), ('Seder_Olam_Rabbah', 9, 0), ('Seder_Olam_Rabbah', 10, 0), ('Tosefta_Sotah', 7, 18), ('Tosefta_Sotah_(Lieberman)', 7, 18)):")
src = rep_block(src, "# THE AMUDIM OF Shabbat 86b-89b SIZED ONE BY ONE", "print('BERAKHOT 32a-32b BY AMUD: %s' % [('%d%s' % (i // 2 + 1, 'ab'[i % 2]), len(TY[i])) for i in range(idx('32a'), idx('32b') + 1)])",
"""# THE RANGES BY AMUD (segments; the first 90 characters of each amud's first row — the design chooses; the rest enumerated outside declared scope)
for wname, a, z in RANGES:
    TB = json.load(open(os.path.join(R, wname, 'en.json'), encoding='utf-8'))['text']
    for i in range(idx(a), idx(z) + 1):
        print('   %-14s %4s %3d  %s' % (wname, '%d%s' % (i // 2 + 1, 'ab'[i % 2]), len(TB[i]), strip(TB[i][0])[:90].replace('\\n', ' ') if TB[i] else ''))
for wname in ('Tosefta_Sotah', 'Seder_Olam_Rabbah', 'Yerushalmi_Shekalim', 'Jerusalem_Talmud_Shekalim'):
    print('  export has %s: %s' % (wname, os.path.exists(os.path.join(R, wname, 'en.json'))))""")
src = rep(src, "own = {'deu_09_ekev_2026-09-19.md'}", "own = {'deu_10_ekev_2026-09-19.md'}")
open(f'{SP}/ch10_docket_scan.py', 'w', encoding='utf-8').write(src)
print('written', len(src), 'bytes; ch9 mentions left:', len(re.findall(r'ch9|Deut 9\\b|chapter 9', src)))
