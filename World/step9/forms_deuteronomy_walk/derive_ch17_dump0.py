import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE DEUTERONOMY WALK sitting 15 — CHAPTERS 17-18's READING IN THE LEAN FORM (2026-09-24; the owner: "Reread and go" after the compaction at #210 — THE LEAN
# PASS's third sitting, the first on TWO chapters): ch17_dump0.py AND ch18_dump0.py DERIVED from the forms' ch16_dump0.py by asserted substitutions, ONE PER
# CHAPTER (the instrument measures one chapter; the sitting reads two — the split joins them): the chapter number, the file names, the register and
# prior-read greps, the drafts by glob, the claim prefixes, the heads window (145-181 — 146 on 16:22 before, 179 on 19:1 after), the kin chapters (17: the
# blemished offering Leviticus 22 and 15:21; the idolater's trial 13:7-12 and the two witnesses Numbers 35:30; the high court Exodus 18 and 1:9-18; the king —
# the Prophets' verses the run's cases, never rows; 18: the priests' portions Numbers 18 and Leviticus 7; the Levite 10:9, 12:12, 14:27-29; the diviners
# Leviticus 19:26-31, 20:6, 20:27, 12:31, Exodus 22:17; the prophet 5:20-28, Exodus 20:15-18, 13:2-6); SECTION I in chapter 6's form — the SPINE computed from
# the heads, never typed; NO portion edge inside either chapter (Shoftim 16:18-21:9 holds both whole); the verse counts measured at A0. RUN FROM THE REPO ROOT.
import os, re, subprocess, ast
ROOT = _ROOT
SP = os.path.dirname(os.path.abspath(__file__))
src = open(f'{ROOT}/World/step9/forms_deuteronomy_walk/ch16_dump0.py', encoding='utf-8').read()
lines = src.split('\n')
assert lines[0] == 'import os as _os' and lines[1].startswith('_ROOT = '), lines[:2]
s0 = '\n'.join(lines[2:])
GIT = "ROOT = _ROOT"
ORD = {17: 'a ninth time', 18: 'a tenth time'}
KIN = {17: ("print('  ledgers with an Onkelos Lev 22 / Deut 15 / Deut 13 / Num 35 / Exod 18 / Deut 1 row (the kin\\'s reading — the blemished offering Leviticus 22:17-25 and 15:21 for 17:1; the idolater\\'s trial 13:7-12 and the two witnesses Numbers 35:30 for 17:2-7; the high court Exodus 18:13-26 and 1:9-18 for 17:8-13; the king\\'s law — 1 Samuel 8 and 1 Kings 10-11 the run\\'s cases, never rows):', "
            "sorted(f for f, t in LED.items() if re.search(r'^- Onkelos (?:Lev 22|Deut (?:15|13|1)|Num 35|Exod 18):', t, re.M)), "
            "'| ledgers with an Onkelos row of the Prophets (never read ahead — expected none):', sorted(f for f, t in LED.items() if re.search(r'^- Onkelos (?:Josh|Judg|1Sam|2Sam|1Kgs|2Kgs):', t, re.M)))"),
       18: ("print('  ledgers with an Onkelos Num 18 / Lev 7 / Deut 10 / Deut 12 / Deut 14 row (the kin\\'s reading — the priests\\' portions Numbers 18:8-20 and Leviticus 7:28-34 for 18:1-5; the Levite without a portion 10:9, 12:12, 14:27-29 for 18:6-8):', "
            "sorted(f for f, t in LED.items() if re.search(r'^- Onkelos (?:Num 18|Lev 7|Deut (?:10|12|14)):', t, re.M)), "
            "'| ledgers with an Onkelos Lev 19 / Lev 20 / Exod 22 / Deut 12 row (the diviners — Leviticus 19:26-31, 20:6, 20:27, Exodus 22:17, 12:31 for 18:9-14):', sorted(f for f, t in LED.items() if re.search(r'^- Onkelos (?:Lev (?:19|20)|Exod 22|Deut 12):', t, re.M)), "
            "'| ledgers with an Onkelos Deut 5 / Exod 20 / Deut 13 row (the prophet like Moses — 5:20-28 and Exodus 20:15-18 the request at Horeb, 13:2-6 the false prophet for 18:15-22):', sorted(f for f, t in LED.items() if re.search(r'^- Onkelos (?:Deut (?:5|13)|Exod 20):', t, re.M)))")}
for CH in (17, 18):
    s = s0
    def sub(old, new, n=1):
        global s
        c = s.count(old); assert c == n, (CH, c, n, old[:80]); s = s.replace(old, new)
    sub("ROOT = _ROOT", GIT)
    i = s.index('# DEUTERONOMY CHAPTER 16, THE READING IN THE LEAN FORM'); j = s.index('import json, re, html')
    HDR = (f"# DEUTERONOMY CHAPTER {CH} — ONE OF THE TWO CHAPTERS OF SITTING 15 (17-18), THE READING IN THE LEAN FORM (THE DEUTERONOMY WALK sitting 15, 2026-09-24; the owner:\n"
           f"# \"Reread and go\" after the compaction at #210 — THE LEAN PASS's third sitting, the first on two chapters) — THE FIRST MEASUREMENT PASS for chapter {CH}, nothing\n"
           f"# typed: (A0) THE TWO DIVISIONS — the export's chapter aligned to the DB's by the monotone alignment over token and negation counts, never by a typed table;\n"
           f"# (A) the shelf BY POSITION (the Sifrei on Deuteronomy's heads 145-181; the whole export scanned in both files for rows citing chapter {CH}); (B) the Onkelos dump\n"
           f"# per DB verse; (C) THE PARSER on every verse; (D) the case tokens, the frames and the register; (E) the register gate; (F) the prior reads; (G) the drafts;\n"
           f"# (H) the store's glosses; (I) THE SPINE ON THE CHAPTER computed from the heads (the outside rows the union less the spine's own piskaot; the other chapter's\n"
           f"# spine rows citing this one fall among them here and are joined at the split). Chapter 16's form (the forms' ch16_dump0.py) derived by asserted\n"
           f"# substitutions (derive_ch17_dump0.py — one derive, two dumps); NO portion edge inside the chapter (Shoftim 16:18-21:9 holds 17 and 18 whole — the chapter\n"
           f"# the unit, CHAPTER NUMBERS); the verse count in the DB's numbering measured at A0, never typed.\n")
    s = s[:i] + HDR + s[j:]
    sub("CH = 16\n", f"CH = {CH}\n")
    sub("chapters 1-16:', [(c, len(onk_he[c - 1]), VC[c]) for c in range(1, 17)", "chapters 1-18:', [(c, len(onk_he[c - 1]), VC[c]) for c in range(1, 19)")
    sub("print('  heads 124-150 (HE first citation | rows | EN first quote):')\nfor p in range(124, 151):", "print('  heads 145-181 (HE first citation | rows | EN first quote):')\nfor p in range(145, 182):")
    sub("'| heads by chapter 1-16:', sorted(Counter(h[0] for h in heads.values() if h).items())[:16])", "'| heads by chapter 1-18:', sorted(Counter(h[0] for h in heads.values() if h).items())[:18])")
    sub(r"""en_forms = re.compile(r'\((?:Deut(?:eronomy)?\.?|Dt\.?|Devarim) ?(16):(\d+)')""", r"""en_forms = re.compile(r'\((?:Deut(?:eronomy)?\.?|Dt\.?|Devarim) ?(%d):(\d+)')""" % CH)
    sub("# (no fold of the English's numbering this chapter either — the English's chapter 16 counts as the Hebrew's; A0 measures it)\n", f"# (no fold of the English's numbering this chapter either — the English's chapter {CH} counts as the Hebrew's; A0 measures it)\n")
    sub(r"""re.finditer(r'\((?:Ibid|ibid)\.? ?16:(\d+)\)', clean(row))]""", r"""re.finditer(r'\((?:Ibid|ibid)\.? ?%d:(\d+)\)', clean(row))]""" % CH)
    sub("print('  EN \"ibid 16:n\" candidates:'", f"print('  EN \"ibid {CH}:n\" candidates:'")
    for fn in ('ch16_sifrei_outside.txt', 'ch16_onkelos.txt', 'ch16_store_glosses.txt', 'ch16_sifrei_spine.txt'): sub(fn, fn.replace('ch16_', f'ch{CH}_'), 2)
    sub("Deut 16:", f"Deut {CH}:", 6)   # the register's two prints and two regexes, the Onkelos-row regex, NAMING's print — the count READ FROM THE PRINT (9 typed, 6 counted)
    sub("Deut(?:eronomy)? 16:", f"Deut(?:eronomy)? {CH}:", 3)   # NAMING's three regexes
    sub("Onkelos Deut 16 row", f"Onkelos Deut {CH} row")
    sub("glob.glob(f'{ROOT}/logic/units/deu_15*.yaml') + glob.glob(f'{ROOT}/logic/units/deu_16*.yaml')", f"glob.glob(f'{{ROOT}}/logic/units/deu_{CH - 1}*.yaml') + glob.glob(f'{{ROOT}}/logic/units/deu_{CH}*.yaml')")
    sub("    if uid.startswith('deu_16'): print(", f"    if uid.startswith('deu_{CH}'): print(")
    sub("for p in ('DV16', 'DV16A', 'DV16B', 'DV15', 'DV17')})", f"for p in ('DV{CH}', 'DV{CH}A', 'DV{CH}B', 'DV{CH - 1}', 'DV{CH + 1}')}})")
    sub("existing manifests deu_16*:', sorted(os.path.basename(f) for f in glob.glob(f'{ROOT}/logic/oral_audit/manifests/deu_16*'))", f"existing manifests deu_{CH}*:', sorted(os.path.basename(f) for f in glob.glob(f'{{ROOT}}/logic/oral_audit/manifests/deu_{CH}*'))")
    sub("overrides already for Deut.16:", f"overrides already for Deut.{CH}:"); sub('Deut\\.16\\.', f'Deut\\.{CH}\\.'); sub("by_ref last Deut.15 line:", f"by_ref last Deut.{CH - 1} line:"); sub("l.startswith('  \"Deut.15.')", f"l.startswith('  \"Deut.{CH - 1}.')")
    sub("(the spine on the chapter an eighth time), whole')", f"(the spine on the chapter {ORD[CH]}), whole')")
    i = s.index("print('  THE PORTION EDGE inside the chapter"); j = s.index('\n', i)
    s = s[:i] + "print('  NO portion edge inside the chapter (Shoftim 16:18-21:9 holds it whole) — the heads by verse, and the verses of the chapter with no head:', sorted({heads[p][1] for p in SPINE}), [v for v in range(1, VC[CH] + 1) if v not in {heads[p][1] for p in SPINE}])" + s[j:]
    i = s.index("print('  ledgers with an Onkelos Exod 12 / Exod 13"); j = s.index('\n', i)
    s = s[:i] + KIN[CH] + s[j:]
    left = re.findall(r'.{40}(?:ch16_|Deut 16|_ROOT|chapter 16|Deut\\\.16|deu_16|DV16).{40}', s.replace("the forms' ch16_dump0.py", '').replace("Chapter 16's form", '').replace(f"deu_{CH - 1}*.yaml", '').replace(f"'DV{CH - 1}'", ''))   # the prior chapter's draft glob and claim prefix are chapter 17's own references to 16
    assert not left, left
    ast.parse(s); open(f'{SP}/ch{CH}_dump0.py', 'w', encoding='utf-8').write(s); print(f'ch{CH}_dump0.py derived:', len(s), 'bytes')
