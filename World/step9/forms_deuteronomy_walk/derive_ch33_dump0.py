import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE DEUTERONOMY WALK sitting 21 — CHAPTER 33's READING IN THE LEAN FORM (2026-09-29; the owner: "Reread and go" after the compaction that followed sitting 20b's
# push 472d2a3 — THE LEAN PASS's fifteenth sitting, its eighth reading, THE BLESSING: the Sifrei's spine in force at 342 on 33:1 through 356 on 33:27; 357 is chapter 34's):
# ch33_dump0.py DERIVED from the forms' ch32_dump0.py by asserted substitutions (sitting 20's form derive_ch32_dump0.py, one chapter): the chapter number, the file names,
# the register and prior-read greps, the drafts by glob (deu_33_ve_zot the one draft on file), the claim prefixes, the heads window (335-357 — the export's end; 341 on 32:52
# before, 342 on 33:1, the blessing's piskaot, 357 on 34:1 after), the kin chapters (Jacob's blessing Genesis 49 and Joseph's sons Genesis 48; Isaac's dew Genesis 27:28;
# Reuben's deed Genesis 35:22; Sinai's coming Exodus 19; Massah Exodus 17:7; the Urim and Thummim Exodus 28:30 and Numbers 27:21; Levi's sword Exodus 32:26-29 and Phinehas
# Numbers 25; the camp's order Numbers 1-2; Gad's portion Numbers 32; the Levites' charge 10:8; the tribes on the mountains 27:12-13; the song 32); THE HEAD REGEX TOLERATES
# A COMMA after the chapter's letters — 342's head is printed with one, the export's one comma head, read as headless by sitting 20's instrument (its print: "342 head None");
# THE SPINE GUARDED as before. THE PORTION EDGE: Vezot Habrachah is 33:1-34:12 — chapter 33 the unit, CHAPTER NUMBERS (34 the next sitting). RUN FROM THE REPO ROOT.
import os, re, subprocess, ast
ROOT = _ROOT
SP = os.path.dirname(os.path.abspath(__file__))
src = open(f'{ROOT}/World/step9/forms_deuteronomy_walk/ch32_dump0.py', encoding='utf-8').read()
lines = src.split('\n')
assert lines[0] == 'import os as _os' and lines[1].startswith('_ROOT = '), lines[:2]
s0 = '\n'.join(lines[2:])
GIT = "import subprocess; ROOT = _ROOT"
PROPHETS = "'| ledgers with an Onkelos row of the Prophets (never read ahead — expected none):', sorted(f for f, t in LED.items() if re.search(r'^- Onkelos (?:Josh|Judg|1Sam|2Sam|1Kgs|2Kgs):', t, re.M)))"
CH = 33
ORD = "a twenty-fifth time — THE BLESSING: 342 on 33:1 onward, the comma in the head of 342 tolerated"   # no apostrophe inside the single-quoted print
KIN = ("print('  ledgers with an Onkelos Gen 27 / Gen 35 / Gen 48 / Gen 49 / Exod 17 / Exod 19 / Exod 28 / Exod 32 / Num 1 / Num 2 / Num 25 / Num 27 / Num 32 / Deut 10 / Deut 27 / Deut 32 row (the kin\\'s reading — Jacob\\'s blessing Genesis 49 and Joseph\\'s sons Genesis 48 for the tribes\\' order and words; Isaac\\'s dew Genesis 27:28 for 33:28; Reuben\\'s deed Genesis 35:22 for 33:6; Sinai\\'s coming Exodus 19 for 33:2; Massah Exodus 17:7 for 33:8; the Urim and Thummim Exodus 28:30 and Numbers 27:21 for 33:8; Levi\\'s sword Exodus 32:26-29 and Phinehas Numbers 25 for 33:9; the camp\\'s order Numbers 1-2 for the tribes named; Gad\\'s portion Numbers 32 for 33:20-21; the Levites\\' charge 10:8 for 33:10; the tribes on the mountains 27:12-13; the song 32 for Jeshurun, the dew and the high places):', "
       "sorted(f for f, t in LED.items() if re.search(r'^- Onkelos (?:Gen (?:27|35|48|49)|Exod (?:17|19|28|32)|Num (?:1|2|25|27|32)|Deut (?:10|27|32)):', t, re.M)), " + PROPHETS)
EDGE = "print('  THE PORTION EDGE: Vezot Habrachah is 33:1-34:12 — chapter 33 the unit, CHAPTER NUMBERS (34 the next sitting; 357 on 34:1 its piska) — THE SPINE IN FORCE: the Sifrei\\'s heads on chapter 33 by verse (342 on 33:1 onward), and the verses without a head:', sorted({heads[p][1] for p in SPINE}), [v for v in range(1, VC[CH] + 1) if v not in {heads[p][1] for p in SPINE}])"
s = s0
def sub(old, new, n=1):
    global s
    c = s.count(old); assert c == n, (CH, c, n, old[:80]); s = s.replace(old, new)
sub("import subprocess; ROOT = _ROOT", GIT)   # the copier's portable line (the forms' copy) back to the scratch form
i = s.index('# DEUTERONOMY CHAPTER 32 — THE SONG'); j = s.index('import json, re, html')
HDR = (f"# DEUTERONOMY CHAPTER {CH} — THE BLESSING, THE ONE CHAPTER OF SITTING 21, THE READING IN THE LEAN FORM (THE DEUTERONOMY WALK sitting 21, 2026-09-29; the owner:\n"
       f"# \"Reread and go\" after the compaction that followed sitting 20b's push 472d2a3 — THE LEAN PASS's fifteenth sitting, its eighth reading; the Sifrei's spine in force at 342 on 33:1) —\n"
       f"# THE FIRST MEASUREMENT PASS for chapter {CH}, nothing typed: (A0) THE TWO DIVISIONS — the export's chapter aligned to the DB's by the monotone alignment over token and\n"
       f"# negation counts, never by a typed table; (A) the shelf BY POSITION (the Sifrei on Deuteronomy's heads 335-357, the export's end; the whole export scanned in both files for rows\n"
       f"# citing chapter {CH}; THE HEAD REGEX TOLERATES A COMMA after the chapter's letters — 342's head is printed with one, the export's one comma head, read as headless by sitting 20's\n"
       f"# instrument); (B) the Onkelos dump per DB verse; (C) THE PARSER on every verse; (D) the case tokens, the frames and the register; (E) the register gate; (F) the prior\n"
       f"# reads; (G) the drafts (one on file — deu_33_ve_zot, 33:1-29); (H) the store's glosses; (I) THE SPINE ON THE CHAPTER computed from the heads (guarded as sitting 19 left\n"
       f"# it). Sitting 20's form (the forms' ch32_dump0.py) derived by asserted substitutions (derive_ch33_dump0.py); the portion edge: Vezot Habrachah is 33:1-34:12 — chapter 33\n"
       f"# the unit, CHAPTER NUMBERS (34 the next sitting); the verse count in the DB's numbering measured at A0, never typed.\n")
s = s[:i] + HDR + s[j:]
sub("CH = 32\n", f"CH = {CH}\n")
sub("chapters 1-32:', [(c, len(onk_he[c - 1]), VC[c]) for c in range(1, 33)", "chapters 1-33:', [(c, len(onk_he[c - 1]), VC[c]) for c in range(1, 34)")
sub("print('  heads 300-345 (HE first citation | rows | EN first quote):')\nfor p in range(300, 346):", "print('  heads 335-357 (HE first citation | rows | EN first quote; the export ends at 357):')\nfor p in range(335, 358):")
sub("'| heads by chapter 1-32:', sorted(Counter(h[0] for h in heads.values() if h).items())[:32])", "'| heads by chapter 1-34:', sorted(Counter(h[0] for h in heads.values() if h).items())[:34])")
# THE HEAD REGEX: a comma tolerated after the chapter's letters (342's head — Deuteronomy 33:1 — the export's one comma head)
i = s.index("    m = re.match(r'\\("); j = s.index('\n', i); line = s[i:j]
assert line.count('+) ([') == 1 and line.count(',? ') == 0, line[:60]
s = s[:i] + line.replace('+) ([', '+),? ([') + "   # a comma after the chapter's letters tolerated: 342's head (Deuteronomy 33:1) is printed with one — the export's one comma head, headless to sitting 20's instrument" + s[j:]
sub(r"""en_forms = re.compile(r'\((?:Deut(?:eronomy)?\.?|Dt\.?|Devarim) ?(32):(\d+)')""", r"""en_forms = re.compile(r'\((?:Deut(?:eronomy)?\.?|Dt\.?|Devarim) ?(%d):(\d+)')""" % CH)
sub("the English citations of chapter 32 are read as they print", f"the English citations of chapter {CH} are read as they print")
sub(r"""re.finditer(r'\((?:Ibid|ibid)\.? ?32:(\d+)\)', clean(row))]""", r"""re.finditer(r'\((?:Ibid|ibid)\.? ?%d:(\d+)\)', clean(row))]""" % CH)
sub("print('  EN \"ibid 32:n\" candidates:'", f"print('  EN \"ibid {CH}:n\" candidates:'")
for fn in ('ch32_sifrei_outside.txt', 'ch32_onkelos.txt', 'ch32_store_glosses.txt', 'ch32_sifrei_spine.txt'): sub(fn, fn.replace('ch32_', f'ch{CH}_'), 2)
sub("Deut 32:", f"Deut {CH}:", 6)
sub("Deut(?:eronomy)? 32:", f"Deut(?:eronomy)? {CH}:", 3)
sub("Onkelos Deut 32 row", f"Onkelos Deut {CH} row")
sub("glob.glob(f'{ROOT}/logic/units/deu_31*.yaml') + glob.glob(f'{ROOT}/logic/units/deu_32*.yaml')", f"glob.glob(f'{{ROOT}}/logic/units/deu_{CH - 1}*.yaml') + glob.glob(f'{{ROOT}}/logic/units/deu_{CH}*.yaml')")
sub("    if uid.startswith('deu_32'): print(", f"    if uid.startswith('deu_{CH}'): print(")
sub("for p in ('DV32', 'DV32A', 'DV32B', 'DV31', 'DV33')})", f"for p in ('DV{CH}', 'DV{CH}A', 'DV{CH}B', 'DV{CH - 1}', 'DV{CH + 1}')}})")
sub("existing manifests deu_32*:', sorted(os.path.basename(f) for f in glob.glob(f'{ROOT}/logic/oral_audit/manifests/deu_32*'))", f"existing manifests deu_{CH}*:', sorted(os.path.basename(f) for f in glob.glob(f'{{ROOT}}/logic/oral_audit/manifests/deu_{CH}*'))")
sub("overrides already for Deut.32:", f"overrides already for Deut.{CH}:"); sub('Deut\\.32\\.', f'Deut\\.{CH}\\.'); sub("by_ref last Deut.31 line:", f"by_ref last Deut.{CH - 1} line:"); sub("l.startswith('  \"Deut.31.')", f"l.startswith('  \"Deut.{CH - 1}.')")
sub("(the spine on the chapter a twenty-fourth time — THE SONG: 306 on 32:1 onward, the spine returned in force), whole')", f"(the spine on the chapter {ORD}), whole')")
i = s.index("print('  NO portion edge inside the chapter"); j = s.index('\n', i); s = s[:i] + EDGE + s[j:]
i = s.index("print('  ledgers with an Onkelos Exod 15 / Exod 19"); j = s.index('\n', i); s = s[:i] + KIN + s[j:]
chk = s.replace("the forms' ch32_dump0.py", '').replace("Sitting 20's form", '').replace(f"'DV{CH - 1}'", '').replace(f"'DV{CH + 1}'", '').replace(f'deu_{CH - 1}*', '').replace(f'Deut.{CH - 1}', '').replace(f'Deut\\.{CH - 1}', '').replace('Deut 32 row', '').replace('the song 32', '')   # the kin line names the song's ledgers
left = re.findall(r'.{40}(?:ch32_|Deut 32|chapter 32|Deut\\\.32|deu_32|DV32|heads 300|range\(300|1-32|Haazinu|32:1-52|THE SONG|a twenty-fourth).{40}', chk)
assert not left, left
ast.parse(s); open(f'{SP}/ch{CH}_dump0.py', 'w', encoding='utf-8').write(s); print(f'ch{CH}_dump0.py derived:', len(s), 'bytes')
