import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE DEUTERONOMY WALK sitting 17 — CHAPTERS 22-25's READING IN THE LEAN FORM (2026-09-25; the owner: "Reread and go" after the compaction at #216 — THE LEAN
# PASS's seventh sitting, the first on FOUR chapters; no commit word said, the tree UNCOMMITTED since f730559 with sittings 15, 15b, 16 and 16b riding):
# ch22_dump0.py, ch23_dump0.py, ch24_dump0.py AND ch25_dump0.py DERIVED from the forms' ch17_dump0.py by asserted substitutions, ONE PER CHAPTER (the instrument
# measures one chapter; the sitting reads four — the split joins them; sitting 15's lesson 1, sitting 16's form derive_ch19_dump0.py): the chapter number, the
# file names, the register and prior-read greps, the drafts by glob, the claim prefixes, the heads window (220-300 — 221 on 21:22 before, 222 on 22:1, the heads
# of 26 after), the kin chapters (22: the lost ox and the fallen ass Exodus 23:4-5, the mixtures Leviticus 19:19, the tassels Numbers 15:38, the adulterer
# Leviticus 20:10, the seducer Exodus 22:15-16, the father's wife Leviticus 18:8 / 20:11 / 27:20; 23: the excluded Leviticus 21:20, Balaam Numbers 22-24 and the
# kin nations 2, the camp Numbers 5 / Leviticus 15, the harlot Leviticus 19:29, the interest Exodus 22:24 / Leviticus 25:36, the vows Numbers 30 / Leviticus 27;
# 24: the divorced Leviticus 21:7, the newlywed 20:7, the pledge Exodus 22:25-26, the kidnapper Exodus 21:16, the leprosy Leviticus 13-14 / Miriam Numbers 12,
# the hireling Leviticus 19:13, the stranger's justice Exodus 22:20 / Leviticus 19:33 / 10:18, the sheaf Leviticus 19:9 / 23:22; 25: the levirate Genesis 38,
# the pity formula 19:13 / 19:21 / 7:16 / 13:9, the weights Leviticus 19:35-36, Amalek Exodus 17:8-16 / Numbers 24:20); SECTION I the SPINE computed from the
# heads, never typed; NO portion edge inside 22-25 (Ki Teitzei 21:10-25:19 holds the four whole; Ki Tavo opens at 26:1, a chapter edge) — the chapter the unit,
# CHAPTER NUMBERS. THE TWO DIVISIONS: the English's numbering of chapters 22-23 differs from the Hebrew's by one verse at their edge (the English's 22:30 is the
# Hebrew's 23:1) — A0 measures the export against the DB; the English citations are read as they print. RUN FROM THE REPO ROOT.
import os, re, subprocess, ast
ROOT = _ROOT
SP = os.path.dirname(os.path.abspath(__file__))
src = open(f'{ROOT}/World/step9/forms_deuteronomy_walk/ch17_dump0.py', encoding='utf-8').read()
lines = src.split('\n')
assert lines[0] == 'import os as _os' and lines[1].startswith('_ROOT = '), lines[:2]
s0 = '\n'.join(lines[2:])
GIT = "ROOT = _ROOT"
ORD = {22: 'a fourteenth time', 23: 'a fifteenth time', 24: 'a sixteenth time', 25: 'a seventeenth time'}
PROPHETS = "'| ledgers with an Onkelos row of the Prophets (never read ahead — expected none):', sorted(f for f, t in LED.items() if re.search(r'^- Onkelos (?:Josh|Judg|1Sam|2Sam|1Kgs|2Kgs):', t, re.M)))"
KIN = {22: ("print('  ledgers with an Onkelos Exod 23 / Exod 22 / Lev 19 / Lev 18 / Lev 20 / Num 15 / Deut 27 / Deut 24 row (the kin\\'s reading — the lost ox and the fallen ass Exodus 23:4-5 for 22:1-4; the mixtures Leviticus 19:19 and the tassels Numbers 15:38 for 22:9-12; the adulterer Leviticus 20:10 and 18:20 for 22:22; the seducer Exodus 22:15-16 for 22:28-29; the father\\'s wife Leviticus 18:8 and 20:11 for 23:1, the English\\'s 22:30; the curses 27:20-23):', "
            "sorted(f for f, t in LED.items() if re.search(r'^- Onkelos (?:Exod (?:23|22)|Lev (?:19|18|20)|Num 15|Deut (?:27|24)):', t, re.M)), " + PROPHETS),
       23: ("print('  ledgers with an Onkelos Lev 21 / Lev 15 / Lev 19 / Lev 25 / Lev 27 / Num 22 / Num 23 / Num 24 / Num 5 / Num 30 / Deut 2 / Exod 22 / Gen 19 row (the kin\\'s reading — the crushed Leviticus 21:20 for 23:2; Balaam Numbers 22-24, Lot Genesis 19 and the kin nations 2:4-29 for 23:4-9; the camp Numbers 5:1-4 and Leviticus 15:16 for 23:10-15; the harlot Leviticus 19:29 for 23:18-19; the interest Exodus 22:24 and Leviticus 25:36-37 for 23:20-21; the vows Numbers 30 and Leviticus 27 for 23:22-24):', "
            "sorted(f for f, t in LED.items() if re.search(r'^- Onkelos (?:Lev (?:21|15|19|25|27)|Num (?:22|23|24|5|30)|Deut 2|Exod 22|Gen 19):', t, re.M)), " + PROPHETS),
       24: ("print('  ledgers with an Onkelos Exod 21 / Exod 22 / Lev 13 / Lev 14 / Lev 19 / Lev 21 / Lev 23 / Num 12 / Deut 20 / Deut 10 / Deut 22 row (the kin\\'s reading — the divorced Leviticus 21:7 for 24:1-4; the newlywed 20:7 for 24:5; the pledge Exodus 22:25-26 for 24:6, 10-13, 17; the kidnapper Exodus 21:16 for 24:7; the leprosy Leviticus 13-14 and Miriam Numbers 12 for 24:8-9; the hireling Leviticus 19:13 for 24:14-15; the stranger\\'s justice Exodus 22:20-23, Leviticus 19:33-34 and 10:18-19 for 24:17-18; the sheaf Leviticus 19:9-10 and 23:22 for 24:19-22):', "
            "sorted(f for f, t in LED.items() if re.search(r'^- Onkelos (?:Exod (?:21|22)|Lev (?:13|14|19|21|23)|Num 12|Deut (?:20|10|22)):', t, re.M)), " + PROPHETS),
       25: ("print('  ledgers with an Onkelos Gen 38 / Lev 19 / Exod 17 / Num 24 / Deut 19 / Deut 7 / Deut 13 row (the kin\\'s reading — the levirate Genesis 38:8-10 for 25:5-10; the pity formula 19:13, 19:21, 7:16 and 13:9 for 25:12; the weights Leviticus 19:35-36 for 25:13-16; Amalek Exodus 17:8-16 and Numbers 24:20 for 25:17-19):', "
            "sorted(f for f, t in LED.items() if re.search(r'^- Onkelos (?:Gen 38|Lev 19|Exod 17|Num 24|Deut (?:19|7|13)):', t, re.M)), " + PROPHETS)}
NOEDGE = "print('  NO portion edge inside the chapter (Ki Teitzei 21:10-25:19 holds it whole) — the heads by verse, and the verses of the chapter with no head:', sorted({heads[p][1] for p in SPINE}), [v for v in range(1, VC[CH] + 1) if v not in {heads[p][1] for p in SPINE}])"
EDGE = {22: NOEDGE, 23: NOEDGE, 24: NOEDGE,
        25: "print('  NO portion edge inside the chapter — Ki Teitzei ends at 25:19, the chapter\\'s last verse, and Ki Tavo opens at 26:1 (a chapter edge; the chapter the unit, CHAPTER NUMBERS) — the heads by verse, the verses with no head, and the heads on 25:17-19:', sorted({heads[p][1] for p in SPINE}), [v for v in range(1, VC[CH] + 1) if v not in {heads[p][1] for p in SPINE}], [(p, heads[p]) for p in SPINE if heads[p][1] in (17, 18, 19)])"}
for CH in (22, 23, 24, 25):
    s = s0
    def sub(old, new, n=1):
        global s
        c = s.count(old); assert c == n, (CH, c, n, old[:80]); s = s.replace(old, new)
    sub("ROOT = _ROOT", GIT)
    i = s.index('# DEUTERONOMY CHAPTER 17 — ONE OF THE TWO CHAPTERS'); j = s.index('import json, re, html')
    HDR = (f"# DEUTERONOMY CHAPTER {CH} — ONE OF THE FOUR CHAPTERS OF SITTING 17 (22-25), THE READING IN THE LEAN FORM (THE DEUTERONOMY WALK sitting 17, 2026-09-25; the owner:\n"
           f"# \"Reread and go\" after the compaction at #216 — THE LEAN PASS's seventh sitting, the first on four chapters) — THE FIRST MEASUREMENT PASS for chapter {CH}, nothing\n"
           f"# typed: (A0) THE TWO DIVISIONS — the export's chapter aligned to the DB's by the monotone alignment over token and negation counts, never by a typed table (the\n"
           f"# English's numbering of chapters 22-23 differs from the Hebrew's by one verse at their edge — the English's 22:30 is the Hebrew's 23:1 — and A0 measures it);\n"
           f"# (A) the shelf BY POSITION (the Sifrei on Deuteronomy's heads 220-300; the whole export scanned in both files for rows citing chapter {CH}); (B) the Onkelos dump\n"
           f"# per DB verse; (C) THE PARSER on every verse; (D) the case tokens, the frames and the register; (E) the register gate; (F) the prior reads; (G) the drafts;\n"
           f"# (H) the store's glosses; (I) THE SPINE ON THE CHAPTER computed from the heads (the outside rows the union less the spine's own piskaot; the other chapters'\n"
           f"# spine rows citing this one fall among them here and are joined at the split). Chapter 17's form (the forms' ch17_dump0.py) derived by asserted\n"
           f"# substitutions (derive_ch22_dump0.py — one derive, four dumps); the portion edge: NONE inside 22-25 (Ki Teitzei 21:10-25:19 holds the four whole; Ki Tavo\n"
           f"# opens at 26:1, a chapter edge) — the chapter the unit, CHAPTER NUMBERS; the verse count in the DB's numbering measured at A0, never typed.\n")
    s = s[:i] + HDR + s[j:]
    sub("CH = 17\n", f"CH = {CH}\n")
    sub("chapters 1-18:', [(c, len(onk_he[c - 1]), VC[c]) for c in range(1, 19)", "chapters 1-25:', [(c, len(onk_he[c - 1]), VC[c]) for c in range(1, 26)")
    sub("print('  heads 145-181 (HE first citation | rows | EN first quote):')\nfor p in range(145, 182):", "print('  heads 220-300 (HE first citation | rows | EN first quote):')\nfor p in range(220, 301):")
    sub("'| heads by chapter 1-18:', sorted(Counter(h[0] for h in heads.values() if h).items())[:18])", "'| heads by chapter 1-25:', sorted(Counter(h[0] for h in heads.values() if h).items())[:25])")
    sub(r"""en_forms = re.compile(r'\((?:Deut(?:eronomy)?\.?|Dt\.?|Devarim) ?(17):(\d+)')""", r"""en_forms = re.compile(r'\((?:Deut(?:eronomy)?\.?|Dt\.?|Devarim) ?(%d):(\d+)')""" % CH)
    sub("# (no fold of the English's numbering this chapter either — the English's chapter 17 counts as the Hebrew's; A0 measures it)\n", f"# (the English's numbering: chapters 22-23 differ from the Hebrew's by one verse at their edge — the English's 22:30 is the Hebrew's 23:1; the English citations of chapter {CH} are read as they print; A0 measures the export)\n")
    sub(r"""re.finditer(r'\((?:Ibid|ibid)\.? ?17:(\d+)\)', clean(row))]""", r"""re.finditer(r'\((?:Ibid|ibid)\.? ?%d:(\d+)\)', clean(row))]""" % CH)
    sub("print('  EN \"ibid 17:n\" candidates:'", f"print('  EN \"ibid {CH}:n\" candidates:'")
    for fn in ('ch17_sifrei_outside.txt', 'ch17_onkelos.txt', 'ch17_store_glosses.txt', 'ch17_sifrei_spine.txt'): sub(fn, fn.replace('ch17_', f'ch{CH}_'), 2)
    sub("Deut 17:", f"Deut {CH}:", 6)   # the register's two prints and two regexes, the Onkelos-row regex, NAMING's print — the count as sitting 15's derive read it
    sub("Deut(?:eronomy)? 17:", f"Deut(?:eronomy)? {CH}:", 3)   # NAMING's three regexes
    sub("Onkelos Deut 17 row", f"Onkelos Deut {CH} row")
    sub("glob.glob(f'{ROOT}/logic/units/deu_16*.yaml') + glob.glob(f'{ROOT}/logic/units/deu_17*.yaml')", f"glob.glob(f'{{ROOT}}/logic/units/deu_{CH - 1}*.yaml') + glob.glob(f'{{ROOT}}/logic/units/deu_{CH}*.yaml')")
    sub("    if uid.startswith('deu_17'): print(", f"    if uid.startswith('deu_{CH}'): print(")
    sub("for p in ('DV17', 'DV17A', 'DV17B', 'DV16', 'DV18')})", f"for p in ('DV{CH}', 'DV{CH}A', 'DV{CH}B', 'DV{CH - 1}', 'DV{CH + 1}')}})")
    sub("existing manifests deu_17*:', sorted(os.path.basename(f) for f in glob.glob(f'{ROOT}/logic/oral_audit/manifests/deu_17*'))", f"existing manifests deu_{CH}*:', sorted(os.path.basename(f) for f in glob.glob(f'{{ROOT}}/logic/oral_audit/manifests/deu_{CH}*'))")
    sub("overrides already for Deut.17:", f"overrides already for Deut.{CH}:"); sub('Deut\\.17\\.', f'Deut\\.{CH}\\.'); sub("by_ref last Deut.16 line:", f"by_ref last Deut.{CH - 1} line:"); sub("l.startswith('  \"Deut.16.')", f"l.startswith('  \"Deut.{CH - 1}.')")
    sub("(the spine on the chapter a ninth time), whole')", f"(the spine on the chapter {ORD[CH]}), whole')")
    i = s.index("print('  NO portion edge inside the chapter"); j = s.index('\n', i)
    s = s[:i] + EDGE[CH] + s[j:]
    i = s.index("print('  ledgers with an Onkelos Lev 22 / Deut 15"); j = s.index('\n', i)
    s = s[:i] + KIN[CH] + s[j:]
    chk = s.replace("the forms' ch17_dump0.py", '').replace("Chapter 17's form", '').replace(f"'DV{CH - 1}'", '').replace(f"'DV{CH + 1}'", '')
    left = re.findall(r'.{40}(?:ch17_|Deut 17|_ROOT|chapter 17|Deut\\\.17|deu_17|DV17|145|181|1-18).{40}', chk)
    assert not left, left
    ast.parse(s); open(f'{SP}/ch{CH}_dump0.py', 'w', encoding='utf-8').write(s); print(f'ch{CH}_dump0.py derived:', len(s), 'bytes')
