import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE DEUTERONOMY WALK sitting 16 — CHAPTERS 19-21's READING IN THE LEAN FORM (2026-09-24; the owner: "Reread go" after the compaction at #212 — THE LEAN
# PASS's fifth sitting, the first on THREE chapters): ch19_dump0.py, ch20_dump0.py AND ch21_dump0.py DERIVED from the forms' ch17_dump0.py by asserted
# substitutions, ONE PER CHAPTER (the instrument measures one chapter; the sitting reads three — the split joins them; sitting 15's lesson 1): the chapter
# number, the file names, the register and prior-read greps, the drafts by glob, the claim prefixes, the heads window (177-223 — 178 on 18:20 before, 179 on
# 19:1, the heads of 22 after), the kin chapters (19: the cities of refuge Numbers 35 / Exodus 21 / 4:41-43, the landmark 27:17, the witnesses 17:6 / Numbers
# 35:30 / Exodus 23:1 / Leviticus 24; 20: the trumpets Numbers 10, the exemptions 24:5 / 28:30, Sihon 2-3 / Numbers 21 / 31, the seven nations 7 / 12 / Exodus
# 23 / 34; 21: the heifer Numbers 35:33 / Exodus 13:13, the captive Numbers 31 / 7:3 / Exodus 21:8, the firstborn Genesis 25 / 48 / 49, the rebellious son
# Exodus 21 / Leviticus 20 / 5:16 / 13:12, the hanged Numbers 25:4 / Genesis 40:19); SECTION I the SPINE computed from the heads, never typed; NO portion edge
# inside 19 or 20 (Shoftim 16:18-21:9), THE EDGE inside 21 at 21:9|21:10 (Ki Teitzei) — the chapter the unit, CHAPTER NUMBERS. RUN FROM THE REPO ROOT.
import os, re, subprocess, ast
ROOT = _ROOT
SP = os.path.dirname(os.path.abspath(__file__))
src = open(f'{ROOT}/World/step9/forms_deuteronomy_walk/ch17_dump0.py', encoding='utf-8').read()
lines = src.split('\n')
assert lines[0] == 'import os as _os' and lines[1].startswith('_ROOT = '), lines[:2]
s0 = '\n'.join(lines[2:])
GIT = "ROOT = _ROOT"
ORD = {19: 'an eleventh time', 20: 'a twelfth time', 21: 'a thirteenth time'}
PROPHETS = "'| ledgers with an Onkelos row of the Prophets (never read ahead — expected none):', sorted(f for f, t in LED.items() if re.search(r'^- Onkelos (?:Josh|Judg|1Sam|2Sam|1Kgs|2Kgs):', t, re.M)))"
KIN = {19: ("print('  ledgers with an Onkelos Num 35 / Exod 21 / Exod 23 / Exod 20 / Deut 4 / Deut 27 / Deut 17 / Lev 24 row (the kin\\'s reading — the cities of refuge Numbers 35:9-34, Exodus 21:12-14 and 4:41-43 for 19:1-13; the landmark 27:17 for 19:14; the witnesses 17:6 and Numbers 35:30, the false witness Exodus 23:1 and 20:13, the measure Leviticus 24:19-20 and Exodus 21:23-25 for 19:15-21):', "
            "sorted(f for f, t in LED.items() if re.search(r'^- Onkelos (?:Num 35|Exod (?:21|23|20)|Deut (?:4|27|17)|Lev 24):', t, re.M)), " + PROPHETS),
       20: ("print('  ledgers with an Onkelos Num 10 / Num 21 / Num 31 / Deut 24 / Deut 28 / Deut 7 / Deut 12 / Deut 2 / Deut 3 / Exod 23 / Exod 34 row (the kin\\'s reading — the trumpets Numbers 10:9 for 20:1-4; the exemptions, 24:5 and 28:30 for 20:5-9; the siege, Sihon 2:26-36, 3:1-7, Numbers 21:21-35 and 31:7-18 for 20:10-15; the seven nations 7:1-5, 7:16, 12:29-31, Exodus 23:31-33 and 34:11-16 for 20:16-18):', "
            "sorted(f for f, t in LED.items() if re.search(r'^- Onkelos (?:Num (?:10|21|31)|Deut (?:24|28|7|12|2|3)|Exod (?:23|34)):', t, re.M)), " + PROPHETS),
       21: ("print('  ledgers with an Onkelos Num 35 / Num 31 / Num 25 / Exod 13 / Exod 21 / Deut 19 / Deut 7 / Deut 5 / Deut 13 / Gen 25 / Gen 48 / Gen 49 / Gen 40 / Lev 20 row (the kin\\'s reading — the heifer and the land\\'s blood Numbers 35:33 and 19:10, the neck broken Exodus 13:13 for 21:1-9; the captive Numbers 31:9-18, 7:3 and Exodus 21:8 for 21:10-14; the firstborn\\'s double Genesis 25:31-34, 49:3-4 and 48:22 for 21:15-17; the rebellious son Exodus 21:15, 17, Leviticus 20:9, 5:16 and 13:12 for 21:18-21; the hanged Numbers 25:4 and Genesis 40:19 for 21:22-23):', "
            "sorted(f for f, t in LED.items() if re.search(r'^- Onkelos (?:Num (?:35|31|25)|Exod (?:13|21)|Deut (?:19|7|5|13)|Gen (?:25|48|49|40)|Lev 20):', t, re.M)), " + PROPHETS)}
EDGE = {19: "print('  NO portion edge inside the chapter (Shoftim 16:18-21:9 holds it whole) — the heads by verse, and the verses of the chapter with no head:', sorted({heads[p][1] for p in SPINE}), [v for v in range(1, VC[CH] + 1) if v not in {heads[p][1] for p in SPINE}])",
        20: "print('  NO portion edge inside the chapter (Shoftim 16:18-21:9 holds it whole) — the heads by verse, and the verses of the chapter with no head:', sorted({heads[p][1] for p in SPINE}), [v for v in range(1, VC[CH] + 1) if v not in {heads[p][1] for p in SPINE}])",
        21: "print('  THE PORTION EDGE inside the chapter at 21:9|21:10 (Shoftim ends at 21:9, Ki Teitzei opens at 21:10 — the chapter the unit, CHAPTER NUMBERS) — the heads by verse, the verses with no head, and the heads on 21:9 and 21:10:', sorted({heads[p][1] for p in SPINE}), [v for v in range(1, VC[CH] + 1) if v not in {heads[p][1] for p in SPINE}], [(p, heads[p]) for p in SPINE if heads[p][1] in (9, 10)])"}
for CH in (19, 20, 21):
    s = s0
    def sub(old, new, n=1):
        global s
        c = s.count(old); assert c == n, (CH, c, n, old[:80]); s = s.replace(old, new)
    sub("ROOT = _ROOT", GIT)
    i = s.index('# DEUTERONOMY CHAPTER 17 — ONE OF THE TWO CHAPTERS'); j = s.index('import json, re, html')
    HDR = (f"# DEUTERONOMY CHAPTER {CH} — ONE OF THE THREE CHAPTERS OF SITTING 16 (19-21), THE READING IN THE LEAN FORM (THE DEUTERONOMY WALK sitting 16, 2026-09-24; the owner:\n"
           f"# \"Reread go\" after the compaction at #212 — THE LEAN PASS's fifth sitting, the first on three chapters) — THE FIRST MEASUREMENT PASS for chapter {CH}, nothing\n"
           f"# typed: (A0) THE TWO DIVISIONS — the export's chapter aligned to the DB's by the monotone alignment over token and negation counts, never by a typed table;\n"
           f"# (A) the shelf BY POSITION (the Sifrei on Deuteronomy's heads 177-223; the whole export scanned in both files for rows citing chapter {CH}); (B) the Onkelos dump\n"
           f"# per DB verse; (C) THE PARSER on every verse; (D) the case tokens, the frames and the register; (E) the register gate; (F) the prior reads; (G) the drafts;\n"
           f"# (H) the store's glosses; (I) THE SPINE ON THE CHAPTER computed from the heads (the outside rows the union less the spine's own piskaot; the other chapters'\n"
           f"# spine rows citing this one fall among them here and are joined at the split). Chapter 17's form (the forms' ch17_dump0.py) derived by asserted\n"
           f"# substitutions (derive_ch19_dump0.py — one derive, three dumps); the portion edge: none inside 19 or 20 (Shoftim 16:18-21:9), inside 21 at 21:9|21:10\n"
           f"# (Ki Teitzei) — the chapter the unit, CHAPTER NUMBERS; the verse count in the DB's numbering measured at A0, never typed.\n")
    s = s[:i] + HDR + s[j:]
    sub("CH = 17\n", f"CH = {CH}\n")
    sub("chapters 1-18:', [(c, len(onk_he[c - 1]), VC[c]) for c in range(1, 19)", "chapters 1-21:', [(c, len(onk_he[c - 1]), VC[c]) for c in range(1, 22)")
    sub("print('  heads 145-181 (HE first citation | rows | EN first quote):')\nfor p in range(145, 182):", "print('  heads 177-223 (HE first citation | rows | EN first quote):')\nfor p in range(177, 224):")
    sub("'| heads by chapter 1-18:', sorted(Counter(h[0] for h in heads.values() if h).items())[:18])", "'| heads by chapter 1-21:', sorted(Counter(h[0] for h in heads.values() if h).items())[:21])")
    sub(r"""en_forms = re.compile(r'\((?:Deut(?:eronomy)?\.?|Dt\.?|Devarim) ?(17):(\d+)')""", r"""en_forms = re.compile(r'\((?:Deut(?:eronomy)?\.?|Dt\.?|Devarim) ?(%d):(\d+)')""" % CH)
    sub("# (no fold of the English's numbering this chapter either — the English's chapter 17 counts as the Hebrew's; A0 measures it)\n", f"# (no fold of the English's numbering this chapter either — the English's chapter {CH} counts as the Hebrew's; A0 measures it)\n")
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
    chk = s.replace("the forms' ch17_dump0.py", '').replace("Chapter 17's form", '').replace(f"deu_{CH - 1}*.yaml", '').replace(f"'DV{CH - 1}'", '').replace(f"'DV{CH + 1}'", '').replace('Deut 17 / Lev 24', '')   # chapter 19's kin names 17:6 — its own reference
    left = re.findall(r'.{40}(?:ch17_|Deut 17|_ROOT|chapter 17|Deut\\\.17|deu_17|DV17|145|181|1-18).{40}', chk)
    assert not left, left
    ast.parse(s); open(f'{SP}/ch{CH}_dump0.py', 'w', encoding='utf-8').write(s); print(f'ch{CH}_dump0.py derived:', len(s), 'bytes')
