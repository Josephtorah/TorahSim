import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE DEUTERONOMY WALK sitting 20 — CHAPTER 32's READING IN THE LEAN FORM (2026-09-27; the owner: "Continue" after sitting 19b's tail and the push c4b14ce, no compaction
# between, /context 332k at the open — THE LEAN PASS's thirteenth sitting, its seventh reading, THE SONG: the Sifrei's spine returns in force at 306 on 32:1 after its silence
# from 26:16 to 31:13): ch32_dump0.py DERIVED from the forms' ch22_dump0.py by asserted substitutions (sitting 19's form derive_ch29_dump0.py, one chapter): the chapter number,
# the file names, the register and prior-read greps, the drafts by glob (deu_32_haazinu and deu_32_song_aftermath the two drafts on file), the claim prefixes, the heads window
# (300-345 — 305 on 31:14's neighbour before, 306 on 32:1, the song's piskaot, 342 on 33:1 after), the kin chapters (the song at the sea Exodus 15; the eagle's wings Exodus 19:4;
# the nations divided Genesis 11; Jacob's poem Genesis 49; the vengeance Leviticus 26 and chapter 28; the rock and Meribah Numbers 20; the mountain Numbers 27:12 with 3:27 and 34;
# the witnesses 4:26 and 31:28; the satiety 8:12-14 and 31:20); THE SPINE GUARDED as before (a chapter with heads keeps its spine; the guards are harmless); THE PORTION EDGE:
# Haazinu is chapter 32 whole (Vezot Habrachah opens at 33:1) — the chapter the unit, CHAPTER NUMBERS. THE TWO DIVISIONS: A0 measures the Onkelos export against the DB
# (chapters 30-34 align; the Hebrew's 28:69 = the English's 29:1 moved chapter 29 alone). RUN FROM THE REPO ROOT.
import os, re, subprocess, ast
ROOT = _ROOT
SP = os.path.dirname(os.path.abspath(__file__))
src = open(f'{ROOT}/World/step9/forms_deuteronomy_walk/ch22_dump0.py', encoding='utf-8').read()
lines = src.split('\n')
assert lines[0] == 'import os as _os' and lines[1].startswith('_ROOT = '), lines[:2]
s0 = '\n'.join(lines[2:])
GIT = "import subprocess; ROOT = _ROOT"
PROPHETS = "'| ledgers with an Onkelos row of the Prophets (never read ahead — expected none):', sorted(f for f, t in LED.items() if re.search(r'^- Onkelos (?:Josh|Judg|1Sam|2Sam|1Kgs|2Kgs):', t, re.M)))"
CH = 32
ORD = 'a twenty-fourth time — THE SONG: 306 on 32:1 onward, the spine returned in force'
KIN = ("print('  ledgers with an Onkelos Exod 15 / Exod 19 / Gen 11 / Gen 49 / Lev 26 / Num 20 / Num 27 / Deut 3 / Deut 4 / Deut 8 / Deut 28 / Deut 31 / Deut 34 row (the kin\\'s reading — the song at the sea Exodus 15 for the song\\'s form; the eagle\\'s wings 19:4 for 32:11; the nations divided Genesis 11 for 32:8; Jacob\\'s poem Genesis 49 for 32:14; the vengeance Leviticus 26 and chapter 28 for 32:19-42; the rock at Meribah Numbers 20 and the mountain Numbers 27:12 with 3:27 and 34:1-4 for 32:48-52; the witnesses 4:26 and 31:28 for 32:1; satiety 8:12-14 and 31:20 for 32:15):', "
       "sorted(f for f, t in LED.items() if re.search(r'^- Onkelos (?:Exod (?:15|19)|Gen (?:11|49)|Lev 26|Num (?:20|27)|Deut (?:3|4|8|28|31|34)):', t, re.M)), " + PROPHETS)
EDGE = "print('  NO portion edge inside the chapter (Haazinu 32:1-52 is the chapter whole; Vezot Habrachah opens at 33:1) — THE SPINE RETURNS IN FORCE: the Sifrei\\'s heads on chapter 32 by verse (306 on 32:1 onward), and the verses without a head:', sorted({heads[p][1] for p in SPINE}), [v for v in range(1, VC[CH] + 1) if v not in {heads[p][1] for p in SPINE}])"
s = s0
def sub(old, new, n=1):
    global s
    c = s.count(old); assert c == n, (CH, c, n, old[:80]); s = s.replace(old, new)
sub("ROOT = _ROOT", GIT)
i = s.index('# DEUTERONOMY CHAPTER 22 — ONE OF THE FOUR CHAPTERS'); j = s.index('import json, re, html')
HDR = (f"# DEUTERONOMY CHAPTER {CH} — THE SONG, THE ONE CHAPTER OF SITTING 20, THE READING IN THE LEAN FORM (THE DEUTERONOMY WALK sitting 20, 2026-09-27; the owner:\n"
       f"# \"Continue\" after sitting 19b's tail and the push — THE LEAN PASS's thirteenth sitting, its seventh reading; the Sifrei's spine returns in force at 306 on 32:1) —\n"
       f"# THE FIRST MEASUREMENT PASS for chapter {CH}, nothing typed: (A0) THE TWO DIVISIONS — the export's chapter aligned to the DB's by the monotone alignment over token and\n"
       f"# negation counts, never by a typed table; (A) the shelf BY POSITION (the Sifrei on Deuteronomy's heads 300-345; the whole export scanned in both files for rows citing\n"
       f"# chapter {CH}); (B) the Onkelos dump per DB verse; (C) THE PARSER on every verse; (D) the case tokens, the frames and the register; (E) the register gate; (F) the prior\n"
       f"# reads; (G) the drafts (two on file — deu_32_haazinu and deu_32_song_aftermath); (H) the store's glosses; (I) THE SPINE ON THE CHAPTER computed from the heads (guarded as\n"
       f"# sitting 19 left it). Chapter 22's form (the forms' ch22_dump0.py) derived by asserted substitutions (derive_ch32_dump0.py); the portion edge: Haazinu is chapter 32 whole\n"
       f"# (Vezot Habrachah opens at 33:1) — the chapter the unit, CHAPTER NUMBERS; the verse count in the DB's numbering measured at A0, never typed.\n")
s = s[:i] + HDR + s[j:]
sub("CH = 22\n", f"CH = {CH}\n")
sub("chapters 1-25:', [(c, len(onk_he[c - 1]), VC[c]) for c in range(1, 26)", "chapters 1-32:', [(c, len(onk_he[c - 1]), VC[c]) for c in range(1, 33)")
sub("print('  heads 220-300 (HE first citation | rows | EN first quote):')\nfor p in range(220, 301):", "print('  heads 300-345 (HE first citation | rows | EN first quote):')\nfor p in range(300, 346):")
sub("'| heads by chapter 1-25:', sorted(Counter(h[0] for h in heads.values() if h).items())[:25])", "'| heads by chapter 1-32:', sorted(Counter(h[0] for h in heads.values() if h).items())[:32])")
sub(r"""en_forms = re.compile(r'\((?:Deut(?:eronomy)?\.?|Dt\.?|Devarim) ?(22):(\d+)')""", r"""en_forms = re.compile(r'\((?:Deut(?:eronomy)?\.?|Dt\.?|Devarim) ?(%d):(\d+)')""" % CH)
sub("# (the English's numbering: chapters 22-23 differ from the Hebrew's by one verse at their edge — the English's 22:30 is the Hebrew's 23:1; the English citations of chapter 22 are read as they print; A0 measures the export)\n", f"# (the English's numbering: chapters 30-34 align with the Hebrew's — the Hebrew's 28:69 = the English's 29:1 moved chapter 29 alone; the English citations of chapter {CH} are read as they print; A0 measures the Onkelos export against the DB)\n")
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
sub("(the spine on the chapter a fourteenth time), whole')", f"(the spine on the chapter {ORD}), whole')")
sub("SPINE[0], '-', SPINE[-1], '):'", "(SPINE or ['none'])[0], '-', (SPINE or ['none'])[-1], '):'")
sub("'| contiguous?', SPINE == list(range(SPINE[0], SPINE[-1] + 1))", "'| contiguous?', (not SPINE or SPINE == list(range(SPINE[0], SPINE[-1] + 1)))")
sub("{p: heads[p] for p in (SPINE[0] - 1, SPINE[-1] + 1)})", "{p: heads[p] for p in ((SPINE[0] - 1, SPINE[-1] + 1) if SPINE else ())})")
i = s.index("print('  NO portion edge inside the chapter"); j = s.index('\n', i); s = s[:i] + EDGE + s[j:]
i = s.index("print('  ledgers with an Onkelos Exod 23 / Exod 22"); j = s.index('\n', i); s = s[:i] + KIN + s[j:]
chk = s.replace("the forms' ch22_dump0.py", '').replace("Chapter 22's form", '').replace(f"'DV{CH - 1}'", '').replace(f"'DV{CH + 1}'", '')
left = re.findall(r'.{40}(?:ch22_|Deut 22|chapter 22|Deut\\\.22|deu_22|DV22|heads 220|range\(220|1-25|Ki Teitzei 21:10|22:30).{40}', chk)
assert not left, left
ast.parse(s); open(f'{SP}/ch{CH}_dump0.py', 'w', encoding='utf-8').write(s); print(f'ch{CH}_dump0.py derived:', len(s), 'bytes')
