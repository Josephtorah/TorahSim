import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE DEUTERONOMY WALK sitting 18 — CHAPTERS 26-28's READING IN THE LEAN FORM (2026-09-26; the owner: "Continue" after sitting 17b's tail, no compaction between —
# THE LEAN PASS's ninth sitting, its fifth reading, the first on chapters WITHOUT A SPINE PISKA (the Sifrei on Deuteronomy heads on 26:1-15 — piskaot 297-303 — and
# then on 31:14; chapters 27 and 28 have NO piska of their own, only rows elsewhere citing them); no commit word said, the tree UNCOMMITTED since f730559 with
# sittings 15 through 17b riding): ch26_dump0.py, ch27_dump0.py AND ch28_dump0.py DERIVED from the forms' ch22_dump0.py by asserted substitutions, ONE PER CHAPTER
# (sitting 17's form derive_ch22_dump0.py): the chapter number, the file names, the register and prior-read greps, the drafts by glob, the claim prefixes, the heads
# window (290-310 — 296 on 25:17 before, 297-303 on chapter 26, 304 on 31:14 after), the kin chapters (26: the firstfruits Exodus 23:19 / 34:26 / Numbers 18:13 and the
# tithe's confession Numbers 18:21-32 / Deuteronomy 14:22-29 / 12:17-19 / 18:1-8; 27: the altar of unhewn stones Exodus 20:22-23, Gerizim and Ebal 11:29, the curses'
# kin Leviticus 18-20 / Exodus 22:20-21 / Leviticus 19:14 / Deuteronomy 19:14 / 24:17 / 22:30; 28: the blessings and curses Leviticus 26, Exodus 23:25-26 / 15:26 / 9:9,
# Deuteronomy 7:12-15 / 11:13-17 / 4:25-31); THE SPINE GUARDED for a chapter with no head (the union whole OUTSIDE; section I empty); NO portion edge inside 26-28
# (Ki Tavo 26:1-29:8 holds the three whole; 29:1-8 is sitting 19's) — the chapter the unit, CHAPTER NUMBERS. THE TWO DIVISIONS: the Hebrew's 28:69 is the English's
# 29:1 — A0 measures the Onkelos export against the DB; the Sifrei's English citations are read as they print. RUN FROM THE REPO ROOT.
import os, re, subprocess, ast
ROOT = _ROOT
SP = os.path.dirname(os.path.abspath(__file__))
src = open(f'{ROOT}/World/step9/forms_deuteronomy_walk/ch22_dump0.py', encoding='utf-8').read()
lines = src.split('\n')
assert lines[0] == 'import os as _os' and lines[1].startswith('_ROOT = '), lines[:2]
s0 = '\n'.join(lines[2:])
GIT = "ROOT = _ROOT"
ORD = {26: 'an eighteenth time', 27: 'a nineteenth time — NONE: no piska heads here', 28: 'a twentieth time — NONE: no piska heads here'}
PROPHETS = "'| ledgers with an Onkelos row of the Prophets (never read ahead — expected none):', sorted(f for f, t in LED.items() if re.search(r'^- Onkelos (?:Josh|Judg|1Sam|2Sam|1Kgs|2Kgs):', t, re.M)))"
KIN = {26: ("print('  ledgers with an Onkelos Exod 23 / Exod 34 / Num 18 / Lev 23 / Lev 27 / Deut 14 / Deut 12 / Deut 18 row (the kin\\'s reading — the firstfruits Exodus 23:19, 34:26 and Numbers 18:13 for 26:1-11; the tithe\\'s confession Numbers 18:21-32, Deuteronomy 14:22-29, 12:17-19 and 18:1-8 for 26:12-15; the covenant\\'s formula 26:16-19):', "
            "sorted(f for f, t in LED.items() if re.search(r'^- Onkelos (?:Exod (?:23|34)|Num 18|Lev (?:23|27)|Deut (?:14|12|18)):', t, re.M)), " + PROPHETS),
       27: ("print('  ledgers with an Onkelos Exod 20 / Exod 22 / Lev 18 / Lev 19 / Lev 20 / Deut 11 / Deut 19 / Deut 24 / Deut 22 / Deut 23 row (the kin\\'s reading — the altar of unhewn stones Exodus 20:22-23 for 27:5-6; Gerizim and Ebal 11:29 for 27:12-13; the curses\\' kin — the image Exodus 20:4 / Deuteronomy 4:16, the parents 21:18 / Leviticus 20:9, the landmark 19:14, the blind Leviticus 19:14, the stranger\\'s judgment Exodus 22:20-21 / 24:17, the father\\'s wife 23:1 / Leviticus 18:8, the beast Leviticus 18:23, the sister 18:9, the mother-in-law 20:14, the secret blow, the bribe 16:19 / Exodus 23:8 — for 27:15-26):', "
            "sorted(f for f, t in LED.items() if re.search(r'^- Onkelos (?:Exod (?:20|22)|Lev (?:18|19|20)|Deut (?:11|19|24|22|23)):', t, re.M)), " + PROPHETS),
       28: ("print('  ledgers with an Onkelos Lev 26 / Exod 23 / Exod 15 / Exod 9 / Deut 7 / Deut 11 / Deut 4 row (the kin\\'s reading — THE BLESSINGS AND THE CURSES Leviticus 26:3-45 for 28:1-68; the bread and the water and the barren Exodus 23:25-26 for 28:4-5; the diseases of Egypt Exodus 15:26 and the boils 9:9 for 28:27, 60; the rain and the heavens 11:13-17 and 7:12-15 for 28:12, 23-24; the scattering and the return 4:25-31 for 28:64):', "
            "sorted(f for f, t in LED.items() if re.search(r'^- Onkelos (?:Lev 26|Exod (?:23|15|9)|Deut (?:7|11|4)):', t, re.M)), " + PROPHETS)}
EDGE = {26: "print('  NO portion edge inside the chapter (Ki Tavo 26:1-29:8 holds it whole; Ki Teitzei ends at 25:19, a chapter edge) — the heads by verse, and the verses of the chapter with no head (the Sifrei stops at 26:15 — 26:16-19 headless, the covenant formula):', sorted({heads[p][1] for p in SPINE}), [v for v in range(1, VC[CH] + 1) if v not in {heads[p][1] for p in SPINE}])",
        27: "print('  NO portion edge inside the chapter (Ki Tavo 26:1-29:8 holds it whole) — NO SPINE PISKA HEADS IN CHAPTER 27 (the Sifrei runs 303 on 26:15 to 304 on 31:14): the heads by verse (none) and every verse without a head:', sorted({heads[p][1] for p in SPINE}), [v for v in range(1, VC[CH] + 1) if v not in {heads[p][1] for p in SPINE}])",
        28: "print('  NO portion edge inside the chapter (Ki Tavo 26:1-29:8 holds it whole; the Hebrew\\'s 28:69 is the English\\'s 29:1 — A0 measured the export) — NO SPINE PISKA HEADS IN CHAPTER 28: the heads by verse (none) and every verse without a head:', sorted({heads[p][1] for p in SPINE}), [v for v in range(1, VC[CH] + 1) if v not in {heads[p][1] for p in SPINE}])"}
for CH in (26, 27, 28):
    s = s0
    def sub(old, new, n=1):
        global s
        c = s.count(old); assert c == n, (CH, c, n, old[:80]); s = s.replace(old, new)
    sub("ROOT = _ROOT", GIT)
    i = s.index('# DEUTERONOMY CHAPTER 22 — ONE OF THE FOUR CHAPTERS'); j = s.index('import json, re, html')
    HDR = (f"# DEUTERONOMY CHAPTER {CH} — ONE OF THE THREE CHAPTERS OF SITTING 18 (26-28), THE READING IN THE LEAN FORM (THE DEUTERONOMY WALK sitting 18, 2026-09-26; the owner:\n"
           f"# \"Continue\" after sitting 17b's tail — THE LEAN PASS's ninth sitting, the first on chapters without a spine piska) — THE FIRST MEASUREMENT PASS for chapter {CH},\n"
           f"# nothing typed: (A0) THE TWO DIVISIONS — the export's chapter aligned to the DB's by the monotone alignment over token and negation counts, never by a typed\n"
           f"# table (the Hebrew's 28:69 is the English's 29:1 — A0 measures the Onkelos export); (A) the shelf BY POSITION (the Sifrei on Deuteronomy's heads 290-310; the\n"
           f"# whole export scanned in both files for rows citing chapter {CH}); (B) the Onkelos dump per DB verse; (C) THE PARSER on every verse; (D) the case tokens, the\n"
           f"# frames and the register; (E) the register gate; (F) the prior reads; (G) the drafts; (H) the store's glosses; (I) THE SPINE ON THE CHAPTER computed from the\n"
           f"# heads — GUARDED: a chapter with no head has an empty spine and the union whole OUTSIDE (chapters 27 and 28; the Sifrei runs 303 on 26:15 to 304 on 31:14).\n"
           f"# Chapter 22's form (the forms' ch22_dump0.py) derived by asserted substitutions (derive_ch26_dump0.py — one derive, three dumps); the portion edge: NONE\n"
           f"# inside 26-28 (Ki Tavo 26:1-29:8 holds the three whole) — the chapter the unit, CHAPTER NUMBERS; the verse count in the DB's numbering measured at A0, never typed.\n")
    s = s[:i] + HDR + s[j:]
    sub("CH = 22\n", f"CH = {CH}\n")
    sub("chapters 1-25:', [(c, len(onk_he[c - 1]), VC[c]) for c in range(1, 26)", "chapters 1-28:', [(c, len(onk_he[c - 1]), VC[c]) for c in range(1, 29)")
    sub("print('  heads 220-300 (HE first citation | rows | EN first quote):')\nfor p in range(220, 301):", "print('  heads 290-310 (HE first citation | rows | EN first quote):')\nfor p in range(290, 311):")
    sub("'| heads by chapter 1-25:', sorted(Counter(h[0] for h in heads.values() if h).items())[:25])", "'| heads by chapter 1-28:', sorted(Counter(h[0] for h in heads.values() if h).items())[:28])")
    sub(r"""en_forms = re.compile(r'\((?:Deut(?:eronomy)?\.?|Dt\.?|Devarim) ?(22):(\d+)')""", r"""en_forms = re.compile(r'\((?:Deut(?:eronomy)?\.?|Dt\.?|Devarim) ?(%d):(\d+)')""" % CH)
    sub("# (the English's numbering: chapters 22-23 differ from the Hebrew's by one verse at their edge — the English's 22:30 is the Hebrew's 23:1; the English citations of chapter 22 are read as they print; A0 measures the export)\n", f"# (the English's numbering: the Hebrew's 28:69 is the English's 29:1 — the English citations of chapter {CH} are read as they print; A0 measures the Onkelos export against the DB)\n")
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
    chk = s.replace("the forms' ch22_dump0.py", '').replace("Chapter 22's form", '').replace(f"'DV{CH - 1}'", '').replace(f"'DV{CH + 1}'", '').replace('22:30', '').replace('Deut 22', '') if CH == 27 else s.replace("the forms' ch22_dump0.py", '').replace("Chapter 22's form", '').replace(f"'DV{CH - 1}'", '').replace(f"'DV{CH + 1}'", '')
    left = re.findall(r'.{40}(?:ch22_|Deut 22|chapter 22|Deut\\\.22|deu_22|DV22|heads 220|range\(220|1-25|Ki Teitzei 21:10).{40}', chk)
    assert not left, left
    ast.parse(s); open(f'{SP}/ch{CH}_dump0.py', 'w', encoding='utf-8').write(s); print(f'ch{CH}_dump0.py derived:', len(s), 'bytes')
