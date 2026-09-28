import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE DEUTERONOMY WALK sitting 19 — CHAPTERS 29-31's READING IN THE LEAN FORM (2026-09-27; the owner: "Continue" after sitting 18b's tail, no compaction between,
# /context 387k at the open — THE LEAN PASS's eleventh sitting, its sixth reading, the second on chapters WITHOUT A SPINE PISKA (the Sifrei on Deuteronomy is silent
# from 26:16 to 31:13 — chapters 29 and 30 have NO piska of their own; chapter 31 has ONE head, 304 on 31:14, and 305 beside it before 306 opens chapter 32); no commit
# word said, the tree UNCOMMITTED since 68191ea with sitting 18b riding): ch29_dump0.py, ch30_dump0.py AND ch31_dump0.py DERIVED from the forms' ch22_dump0.py by asserted
# substitutions, ONE PER CHAPTER (sitting 18's form derive_ch26_dump0.py): the chapter number, the file names, the register and prior-read greps, the drafts by glob, the
# claim prefixes, the heads window (295-320 — 303 on 26:15 before, 304 on 31:14, 306 on 32:1 after), the kin chapters (29: the covenant at Horeb and Moab, the forty
# years' garments, Sihon and Og, Sodom, the exile 4:25-31 / Leviticus 26; 30: the return and the gathering Leviticus 26:40-45 / 4:29-31, the circumcised heart 10:16,
# the commandment near 6:6-7 / 11:18, life and death 11:26-28; 31: Moses' hundred and twenty years and Joshua's commission Numbers 27:12-23 / 3:21-28 / 34:7-9, the reading
# at the release year's Sukkot 15:1 / 16:13-15 / 17:18-19, the ark and the Levites 10:1-5, the Tent and the pillar Exodus 33:9-10); THE SPINE GUARDED for a chapter with
# no head (the union whole OUTSIDE; section I empty); THE PORTION EDGES: Ki Tavo ends at 29:8 and Nitzavim opens at 29:9 INSIDE chapter 29; Nitzavim ends with chapter 30;
# Vayelech is chapter 31 whole — the chapter the unit, CHAPTER NUMBERS. THE TWO DIVISIONS: the Hebrew's 28:69 is the English's 29:1, so the English's chapter 29 runs one
# verse ahead of the Hebrew's (29:1-29 against 29:1-28) — A0 measures the Onkelos export against the DB; the Sifrei's English citations are read as they print. RUN FROM THE REPO ROOT.
import os, re, subprocess, ast
ROOT = _ROOT
SP = os.path.dirname(os.path.abspath(__file__))
src = open(f'{ROOT}/World/step9/forms_deuteronomy_walk/ch22_dump0.py', encoding='utf-8').read()
lines = src.split('\n')
assert lines[0] == 'import os as _os' and lines[1].startswith('_ROOT = '), lines[:2]
s0 = '\n'.join(lines[2:])
GIT = "import subprocess; ROOT = _ROOT"   # the scratch form: the forms copy of the derive carried the copier's portable line (ROOT = _ROOT) — the git root restored for the scratchpad (RUN FROM THE REPO ROOT)
ORD = {29: 'a twenty-first time — NONE: no piska heads here', 30: 'a twenty-second time — NONE: no piska heads here', 31: 'a twenty-third time — ONE head, 304 on 31:14'}
PROPHETS = "'| ledgers with an Onkelos row of the Prophets (never read ahead — expected none):', sorted(f for f, t in LED.items() if re.search(r'^- Onkelos (?:Josh|Judg|1Sam|2Sam|1Kgs|2Kgs):', t, re.M)))"
KIN = {29: ("print('  ledgers with an Onkelos Exod 19 / Exod 24 / Lev 26 / Gen 19 / Deut 2 / Deut 3 / Deut 4 / Deut 5 / Deut 8 / Deut 28 row (the kin\\'s reading — the covenant at Horeb Exodus 19-24 and 5:2-3 beside the covenant in Moab 29:9-14; the forty years\\' garments and the kings Sihon and Og 8:2-4 and 2:24-3:11 for 29:4-7; Sodom and Gomorrah Genesis 19 for 29:22; the exile and the return 4:25-31 and Leviticus 26 for 29:21-27):', "
            "sorted(f for f, t in LED.items() if re.search(r'^- Onkelos (?:Exod (?:19|24)|Lev 26|Gen 19|Deut (?:2|3|4|5|8|28)):', t, re.M)), " + PROPHETS),
       30: ("print('  ledgers with an Onkelos Lev 26 / Deut 4 / Deut 6 / Deut 10 / Deut 11 / Deut 28 row (the kin\\'s reading — the return and the gathering Leviticus 26:40-45 and 4:29-31 for 30:1-10; the circumcised heart 10:16 for 30:6; the commandment near, in your mouth and in your heart 6:6-7 and 11:18 for 30:11-14; life and death, the blessing and the curse 11:26-28 and chapter 28 for 30:15-20):', "
            "sorted(f for f, t in LED.items() if re.search(r'^- Onkelos (?:Lev 26|Deut (?:4|6|10|11|28)):', t, re.M)), " + PROPHETS),
       31: ("print('  ledgers with an Onkelos Num 27 / Exod 33 / Deut 1 / Deut 3 / Deut 10 / Deut 15 / Deut 16 / Deut 17 / Deut 34 row (the kin\\'s reading — Moses\\' hundred and twenty years and Joshua\\'s commission Numbers 27:12-23, 3:21-28 and 34:7-9 for 31:1-8 and 31:14-23; the reading of the law at the release year\\'s Sukkot 15:1, 16:13-15 and 17:18-19 for 31:9-13; the ark and the Levites 10:1-5 for 31:9 and 31:25-26; the Tent and the pillar of cloud Exodus 33:9-10 for 31:14-15):', "
            "sorted(f for f, t in LED.items() if re.search(r'^- Onkelos (?:Num 27|Exod 33|Deut (?:1|3|10|15|16|17|34)):', t, re.M)), " + PROPHETS)}
EDGE = {29: "print('  THE PORTION EDGE INSIDE THE CHAPTER — Ki Tavo ends at 29:8 and Nitzavim opens at 29:9 (the chapter the unit, CHAPTER NUMBERS) — NO SPINE PISKA HEADS IN CHAPTER 29 (the Sifrei runs 303 on 26:15 to 304 on 31:14): the heads by verse (none) and every verse without a head:', sorted({heads[p][1] for p in SPINE}), [v for v in range(1, VC[CH] + 1) if v not in {heads[p][1] for p in SPINE}])",
        30: "print('  NO portion edge inside the chapter (Nitzavim 29:9-30:20 ends with the chapter; Vayelech opens at 31:1, a chapter edge) — NO SPINE PISKA HEADS IN CHAPTER 30: the heads by verse (none) and every verse without a head:', sorted({heads[p][1] for p in SPINE}), [v for v in range(1, VC[CH] + 1) if v not in {heads[p][1] for p in SPINE}])",
        31: "print('  NO portion edge inside the chapter (Vayelech 31:1-30 is the chapter whole; Haazinu opens at 32:1) — the Sifrei returns at 31:14 (304; 305 beside it; 306 on 32:1): the heads by verse and the verses without a head (31:1-13 the charge, the reading and the ark — headless):', sorted({heads[p][1] for p in SPINE}), [v for v in range(1, VC[CH] + 1) if v not in {heads[p][1] for p in SPINE}])"}
for CH in (29, 30, 31):
    s = s0
    def sub(old, new, n=1):
        global s
        c = s.count(old); assert c == n, (CH, c, n, old[:80]); s = s.replace(old, new)
    sub("ROOT = _ROOT", GIT)
    i = s.index('# DEUTERONOMY CHAPTER 22 — ONE OF THE FOUR CHAPTERS'); j = s.index('import json, re, html')
    HDR = (f"# DEUTERONOMY CHAPTER {CH} — ONE OF THE THREE CHAPTERS OF SITTING 19 (29-31), THE READING IN THE LEAN FORM (THE DEUTERONOMY WALK sitting 19, 2026-09-27; the owner:\n"
           f"# \"Continue\" after sitting 18b's tail — THE LEAN PASS's eleventh sitting, the second on chapters without a spine piska) — THE FIRST MEASUREMENT PASS for chapter {CH},\n"
           f"# nothing typed: (A0) THE TWO DIVISIONS — the export's chapter aligned to the DB's by the monotone alignment over token and negation counts, never by a typed\n"
           f"# table (the Hebrew's 28:69 is the English's 29:1 — A0 measures the Onkelos export); (A) the shelf BY POSITION (the Sifrei on Deuteronomy's heads 295-320; the\n"
           f"# whole export scanned in both files for rows citing chapter {CH}); (B) the Onkelos dump per DB verse; (C) THE PARSER on every verse; (D) the case tokens, the\n"
           f"# frames and the register; (E) the register gate; (F) the prior reads; (G) the drafts; (H) the store's glosses; (I) THE SPINE ON THE CHAPTER computed from the\n"
           f"# heads — GUARDED: a chapter with no head has an empty spine and the union whole OUTSIDE (chapters 29 and 30; chapter 31 has 304 on 31:14 and 305 beside it).\n"
           f"# Chapter 22's form (the forms' ch22_dump0.py) derived by asserted substitutions (derive_ch29_dump0.py — one derive, three dumps); the portion edges: Ki Tavo\n"
           f"# ends at 29:8 INSIDE chapter 29, Nitzavim ends with 30, Vayelech is 31 whole — the chapter the unit, CHAPTER NUMBERS; the verse count in the DB's numbering measured at A0, never typed.\n")
    s = s[:i] + HDR + s[j:]
    sub("CH = 22\n", f"CH = {CH}\n")
    sub("chapters 1-25:', [(c, len(onk_he[c - 1]), VC[c]) for c in range(1, 26)", "chapters 1-31:', [(c, len(onk_he[c - 1]), VC[c]) for c in range(1, 32)")
    sub("print('  heads 220-300 (HE first citation | rows | EN first quote):')\nfor p in range(220, 301):", "print('  heads 295-320 (HE first citation | rows | EN first quote):')\nfor p in range(295, 321):")
    sub("'| heads by chapter 1-25:', sorted(Counter(h[0] for h in heads.values() if h).items())[:25])", "'| heads by chapter 1-31:', sorted(Counter(h[0] for h in heads.values() if h).items())[:31])")
    sub(r"""en_forms = re.compile(r'\((?:Deut(?:eronomy)?\.?|Dt\.?|Devarim) ?(22):(\d+)')""", r"""en_forms = re.compile(r'\((?:Deut(?:eronomy)?\.?|Dt\.?|Devarim) ?(%d):(\d+)')""" % CH)
    sub("# (the English's numbering: chapters 22-23 differ from the Hebrew's by one verse at their edge — the English's 22:30 is the Hebrew's 23:1; the English citations of chapter 22 are read as they print; A0 measures the export)\n", f"# (the English's numbering: the Hebrew's 28:69 is the English's 29:1, so the English's chapter 29 runs one verse ahead — the English citations of chapter {CH} are read as they print; A0 measures the Onkelos export against the DB)\n")
    sub(r"""re.finditer(r'\((?:Ibid|ibid)\.? ?22:(\d+)\)', clean(row))]""", r"""re.finditer(r'\((?:Ibid|ibid)\.? ?%d:(\d+)\)', clean(row))]""" % CH)
    sub("print('  EN \"ibid 22:n\" candidates:'", f"print('  EN \"ibid {CH}:n\" candidates:'")
    for fn in ('ch22_sifrei_outside.txt', 'ch22_onkelos.txt', 'ch22_store_glosses.txt', 'ch22_sifrei_spine.txt'): sub(fn, fn.replace('ch22_', f'ch{CH}_'), 2)
    sub("Deut 22:", f"Deut {CH}:", 6)
    sub("Deut(?:eronomy)? 22:", f"Deut(?:eronomy)? {CH}:", 3)
    sub("Onkelos Deut 22 row", f"Onkelos Deut {CH} row")
    sub("glob.glob(f'{ROOT}/logic/units/deu_21*.yaml') + glob.glob(f'{ROOT}/logic/units/deu_22*.yaml')", f"glob.glob(f'{{ROOT}}/logic/units/deu_{CH - 1}*.yaml') + glob.glob(f'{{ROOT}}/logic/units/deu_{CH}*.yaml')")
    sub("    if uid.startswith('deu_22'): print(", f"    if uid.startswith('deu_{CH}'): print(")
    sub("for p in ('DV22', 'DV22A', 'DV22B', 'DV21', 'DV23')})", f"for p in ('DV{CH}', 'DV{CH}A', 'DV{CH}B', 'DV{CH - 1}', 'DV{CH + 1}')}})")
    sub("existing manifests deu_22*:', sorted(os.path.basename(f) for f in glob.glob(f'{ROOT}/logic/oral_audit/manifests/deu_22*'))", f"existing manifests deu_{CH}*:', sorted(os.path.basename(f) for f in glob.glob(f'{{ROOT}}/logic/oral_audit/manifests/deu_{CH}*'))")
    sub("overrides already for Deut.22:", f"overrides already for Deut.{CH}:"); sub('Deut\\.22\\.', f'Deut\\.{CH}\\.'); sub("by_ref last Deut.21 line:", f"by_ref last Deut.{CH - 1} line:"); sub("l.startswith('  \"Deut.21.')", f"l.startswith('  \"Deut.{CH - 1}.')")
    sub("(the spine on the chapter a fourteenth time), whole')", f"(the spine on the chapter {ORD[CH]}), whole')")
    # THE SPINE GUARDED — a chapter with no piska head (27, 28)
    sub("SPINE[0], '-', SPINE[-1], '):'", "(SPINE or ['none'])[0], '-', (SPINE or ['none'])[-1], '):'")
    sub("'| contiguous?', SPINE == list(range(SPINE[0], SPINE[-1] + 1))", "'| contiguous?', (not SPINE or SPINE == list(range(SPINE[0], SPINE[-1] + 1)))")
    sub("{p: heads[p] for p in (SPINE[0] - 1, SPINE[-1] + 1)})", "{p: heads[p] for p in ((SPINE[0] - 1, SPINE[-1] + 1) if SPINE else ())})")
    i = s.index("print('  NO portion edge inside the chapter"); j = s.index('\n', i)
    s = s[:i] + EDGE[CH] + s[j:]
    i = s.index("print('  ledgers with an Onkelos Exod 23 / Exod 22"); j = s.index('\n', i)
    s = s[:i] + KIN[CH] + s[j:]
    chk = s.replace("the forms' ch22_dump0.py", '').replace("Chapter 22's form", '').replace(f"'DV{CH - 1}'", '').replace(f"'DV{CH + 1}'", '').replace('22:30', '').replace('Deut 22', '') if CH in (29, 30) else s.replace("the forms' ch22_dump0.py", '').replace("Chapter 22's form", '').replace(f"'DV{CH - 1}'", '').replace(f"'DV{CH + 1}'", '')
    left = re.findall(r'.{40}(?:ch22_|Deut 22|chapter 22|Deut\\\.22|deu_22|DV22|heads 220|range\(220|1-25|Ki Teitzei 21:10).{40}', chk)
    assert not left, left
    ast.parse(s); open(f'{SP}/ch{CH}_dump0.py', 'w', encoding='utf-8').write(s); print(f'ch{CH}_dump0.py derived:', len(s), 'bytes')
