import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE DEUTERONOMY WALK sitting 13 — CHAPTER 15's READING, TWO RUNS + THE TAIL under THE COST RULES A-B-C (2026-09-22; the owner: "Go" after the compaction
# at #205 addendum 5 — the #204 NOTE's rule: the measurements, the ink and the design one run to a clean point; the rows and the ledger a second, the clean
# point after the first half UNCONDITIONALLY; the tail the third): ch15_dump0.py DERIVED from the forms' ch14_dump0.py by asserted substitutions
# (derive_ch14_dump0.py's form): the chapter number, the file names, the register and prior-read greps, the kin chapters (Exodus 21:2-11 the Hebrew slave,
# Exodus 22:24-26 the lender and the pledge, Exodus 23:10-11 and Leviticus 25 the seventh year and the sold brother, Exodus 13 / 22:29 / 34:19-20, Leviticus 22
# and 27, Numbers 18:15-18 the firstling and the blemish, Deuteronomy 12's place and blood-poured clauses, 14:28-29's poor, 5:15's slave remembered, Genesis
# 4:4 Abel's firstlings), the drafts by glob; SECTION I in chapter 6's form — the SPINE computed from the heads, never typed; the last on-chapter piska's
# tail, if it runs into 16:1, LEFT for chapter 16 (sitting 11's lesson 1 — a piska's membership is decided on the consonants); NO PORTION EDGE inside the
# chapter (Re'eh 11:26-16:17 holds it whole); the verse count measured at A0 (the export's chapter 15 against the DB's), never typed. RUN FROM THE REPO ROOT.
import os, re, subprocess
ROOT = _ROOT
SP = os.path.dirname(os.path.abspath(__file__))
src = open(f'{ROOT}/World/step9/forms_deuteronomy_walk/ch14_dump0.py', encoding='utf-8').read()
lines = src.split('\n')
assert lines[0] == 'import os as _os' and lines[1].startswith('_ROOT = '), lines[:2]
s = '\n'.join(lines[2:])
GIT = "ROOT = _ROOT"
REPL = [
 ("ROOT = _ROOT", GIT),
 ("# DEUTERONOMY CHAPTER 14, THE READING (THE DEUTERONOMY WALK sitting 12, 2026-09-21; the owner: \"Go\" after 11b's tail; ONE RUN + ITS TAIL under the cost rules) — THE FIRST",
  "# DEUTERONOMY CHAPTER 15, THE READING (THE DEUTERONOMY WALK sitting 13, 2026-09-22; the owner: \"Go\" after the compaction at #205 addendum 5; TWO RUNS + THE TAIL under the cost rules — the #204 NOTE) — THE FIRST"),
 ("# Chapter 13's form (ch13_dump0.py) derived by asserted substitutions (derive_ch14_dump0.py); SECTION I in chapter 6's form — THE SPINE IS ON THE CHAPTER\n# (sitting 11's print: 97 heads on 14:2; PISKA 96's ROWS 9-12 ARE 14:1's — outside the on-chapter piskaot, found by the union, folded at the split): the SPINE\n# computed from the heads, the outside rows the union less the spine's own piskaot; NO portion edge inside the chapter (Re'eh 11:26-16:17 holds it whole — the\n# chapter the unit, per the ruling CHAPTER NUMBERS); TWENTY-NINE verses in the DB's numbering (the export's chapter 14 against the DB's measured at A0, never typed).",
  "# Chapter 14's form (ch14_dump0.py) derived by asserted substitutions (derive_ch15_dump0.py); SECTION I in chapter 6's form — THE SPINE IS ON THE CHAPTER\n# (sitting 12's print: 111 heads on 15:1; the last on-chapter piska's tail, if it runs into 16:1, LEFT for chapter 16 — sitting 11's lesson 1): the SPINE\n# computed from the heads, the outside rows the union less the spine's own piskaot; NO portion edge inside the chapter (Re'eh 11:26-16:17 holds it whole — the\n# chapter the unit, per the ruling CHAPTER NUMBERS); the verse count in the DB's numbering measured at A0 (the export's chapter 15 against the DB's), never typed."),
 ("CH = 14\n", "CH = 15\n"),
 ("chapters 1-14:', [(c, len(onk_he[c - 1]), VC[c]) for c in range(1, 15)", "chapters 1-15:', [(c, len(onk_he[c - 1]), VC[c]) for c in range(1, 16)"),
 ("print('  heads 94-116 (HE first citation | rows | EN first quote):')\nfor p in range(94, 117):", "print('  heads 108-130 (HE first citation | rows | EN first quote):')\nfor p in range(108, 131):"),
 ("'| heads by chapter 1-14:', sorted(Counter(h[0] for h in heads.values() if h).items())[:14])", "'| heads by chapter 1-15:', sorted(Counter(h[0] for h in heads.values() if h).items())[:15])"),
 (r"""en_forms = re.compile(r'\((?:Deut(?:eronomy)?\.?|Dt\.?|Devarim) ?(14):(\d+)')""", r"""en_forms = re.compile(r'\((?:Deut(?:eronomy)?\.?|Dt\.?|Devarim) ?(15):(\d+)')"""),
 ("# (chapter 13's fold of the English's 12:32 into 13:1 is not chapter 14's — the English's chapter 14 counts as the Hebrew's; A0 measures it)\n",
  "# (no fold of the English's numbering this chapter either — the English's chapter 15 counts as the Hebrew's; A0 measures it)\n"),
 (r"""re.finditer(r'\((?:Ibid|ibid)\.? ?14:(\d+)\)', clean(row))]""", r"""re.finditer(r'\((?:Ibid|ibid)\.? ?15:(\d+)\)', clean(row))]"""),
 ("print('  EN \"ibid 14:n\" candidates:'", "print('  EN \"ibid 15:n\" candidates:'"),
 ("ch14_sifrei_outside.txt", "ch15_sifrei_outside.txt"),
 ("ch14_onkelos.txt", "ch15_onkelos.txt"),
 ("ch14_store_glosses.txt", "ch15_store_glosses.txt"),
 ("ch14_sifrei_spine.txt", "ch15_sifrei_spine.txt"),
 ("| {1, 29}):", "| {1, VC[CH]}):"),
 ("print('  dispositions naming Deut 14:', re.findall(r'^([^\\n]*Deut 14:[^\\n]*)$', RD, re.M)[:20])", "print('  dispositions naming Deut 15:', re.findall(r'^([^\\n]*Deut 15:[^\\n]*)$', RD, re.M)[:20])"),
 ("print('  REGISTER_INDEX lines on Deut 14:'); [print('   ', l[:220]) for l in RI.split('\\n') if re.search(r'Deut 14:', l)]", "print('  REGISTER_INDEX lines on Deut 15:'); [print('   ', l[:220]) for l in RI.split('\\n') if re.search(r'Deut 15:', l)]"),
 ("print('  ledgers with an Onkelos Deut 14 row:', sorted(f for f, t in LED.items() if re.search(r'^- Onkelos Deut 14:', t, re.M)))", "print('  ledgers with an Onkelos Deut 15 row:', sorted(f for f, t in LED.items() if re.search(r'^- Onkelos Deut 15:', t, re.M)))"),
 ("NAMING = sorted((f, len(re.findall(r'Deut(?:eronomy)? 14:\\d+', t)), sorted(set(re.findall(r'Deut(?:eronomy)? 14:\\d+(?:-\\d+)?', t)))[:14]) for f, t in LED.items() if re.search(r'Deut(?:eronomy)? 14:\\d+', t))\nprint('  ledgers NAMING a verse of Deut 14:'",
  "NAMING = sorted((f, len(re.findall(r'Deut(?:eronomy)? 15:\\d+', t)), sorted(set(re.findall(r'Deut(?:eronomy)? 15:\\d+(?:-\\d+)?', t)))[:14]) for f, t in LED.items() if re.search(r'Deut(?:eronomy)? 15:\\d+', t))\nprint('  ledgers NAMING a verse of Deut 15:'"),
 ("print('  ledgers with an Onkelos Lev 11 row (the kin\\'s reading — the clean and the unclean animals 11:1-47 for 14:3-21) or a Lev 19 / Lev 21 row (the cuts for the dead 19:27-28 and the priests\\' baldness 21:5 for 14:1) or a Lev 17 / Lev 22 row (the carcass and the torn 17:15, 22:8 for 14:21):', sorted(f for f, t in LED.items() if re.search(r'^- Onkelos Lev (?:11|17|19|21|22):', t, re.M)), '| ledgers with an Onkelos Exod 22 / Exod 23 / Exod 34 row (the torn flesh 22:30, the kid in its mother\\'s milk 23:19 and 34:26 for 14:21) or an Exod 19 row (the treasured people 19:5-6 for 14:2):', sorted(f for f, t in LED.items() if re.search(r'^- Onkelos Exod (?:19|22|23|34):', t, re.M)), '| ledgers with an Onkelos Num 18 row (the tithe to the Levites 18:21-32 for 14:22-29) or a Lev 27 row (the tithe holy to the LORD 27:30-33) or a Deut 7 / Deut 12 row (the holy people 7:6 for 14:2; the tithe eaten at the place and the Levite 12:6, 12:17-19 for 14:22-27):', sorted(f for f, t in LED.items() if re.search(r'^- Onkelos (?:Num 18|Lev 27|Deut 7|Deut 12):', t, re.M)), '| ledgers with an Onkelos Gen 7 row (the clean beasts 7:2 for 14:4):', sorted(f for f, t in LED.items() if re.search(r'^- Onkelos Gen 7:', t, re.M)))",
  "print('  ledgers with an Onkelos Exod 21 / Exod 22 / Exod 23 row (the kin\\'s reading — the Hebrew slave 21:2-11 for 15:12-18, the lender and the pledge 22:24-26 for 15:7-11, the seventh year 23:10-11 for 15:1-11, the firstborn of the ox and the sheep 22:29 for 15:19) or a Lev 25 row (the sabbatical year 25:1-7, the poor brother 25:35-38, the sold brother 25:39-55 for 15:1-18):', sorted(f for f, t in LED.items() if re.search(r'^- Onkelos (?:Exod (?:21|22|23)|Lev 25):', t, re.M)), '| ledgers with an Onkelos Exod 13 / Exod 34 / Num 18 / Lev 27 / Lev 22 row (the firstling 13:2, 13:11-16, 34:19-20, Numbers 18:15-18, Leviticus 27:26; the blemish 22:17-25 and the seven days 22:27 for 15:19-23):', sorted(f for f, t in LED.items() if re.search(r'^- Onkelos (?:Exod (?:13|34)|Num 18|Lev (?:22|27)):', t, re.M)), '| ledgers with an Onkelos Deut 5 / Deut 12 / Deut 14 row (the slave remembered 5:15 for 15:15; the firstlings at the place 12:6, 12:17-18, the gazelle and the hart and the blood poured 12:15-16, 12:22-24 for 15:20-23; the poor at the gate 14:28-29 for 15:7-11):', sorted(f for f, t in LED.items() if re.search(r'^- Onkelos Deut (?:5|12|14):', t, re.M)), '| ledgers with an Onkelos Gen 4 row (Abel\\'s firstlings 4:4 for 15:19):', sorted(f for f, t in LED.items() if re.search(r'^- Onkelos Gen 4:', t, re.M)))"),
 ("glob.glob(f'{ROOT}/logic/units/deu_13*.yaml') + glob.glob(f'{ROOT}/logic/units/deu_14*.yaml')", "glob.glob(f'{ROOT}/logic/units/deu_14*.yaml') + glob.glob(f'{ROOT}/logic/units/deu_15*.yaml')"),
 ("    if uid.startswith('deu_14'): print(", "    if uid.startswith('deu_15'): print("),
 ("for p in ('DV14', 'DV14A', 'DV14B', 'DV13', 'DV15')})", "for p in ('DV15', 'DV15A', 'DV15B', 'DV14', 'DV16')})"),
 ("print('  existing manifests deu_14*:', sorted(os.path.basename(f) for f in glob.glob(f'{ROOT}/logic/oral_audit/manifests/deu_14*'))", "print('  existing manifests deu_15*:', sorted(os.path.basename(f) for f in glob.glob(f'{ROOT}/logic/oral_audit/manifests/deu_15*'))"),
 ("print('  overrides already for Deut.14:', re.findall(r'\"Deut\\.14\\.[^\"]+\": \"[^\"]+\"', OV)[:20], '| by_ref last Deut.13 line:', [l for l in OV.split('\\n') if l.startswith('  \"Deut.13.')][-1:])",
  "print('  overrides already for Deut.15:', re.findall(r'\"Deut\\.15\\.[^\"]+\": \"[^\"]+\"', OV)[:20], '| by_ref last Deut.14 line:', [l for l in OV.split('\\n') if l.startswith('  \"Deut.14.')][-1:])"),
 ("'(the first on-chapter piskaot since chapter 6), whole')", "'(the spine on the chapter a seventh time), whole')"),
]
for old, new in REPL:
    n = s.count(old); assert n >= 1, ('ABSENT', old[:90]); s = s.replace(old, new)   # the file names appear twice (the write and the size print) — 12's form
left = [m for m in re.findall(r'.{30}(?:ch14_|Deut 14:|Deut\.14\.|Lev \(\?:11|Exod \(\?:19|Gen 7:|_ROOT|range\(1, 15\)).{30}', s.replace('ch14_dump0.py', ''))]
left += [m for m in re.findall(r'.{30}deu_14.{30}', s) if 'glob' not in m]
left += [m for m in re.findall(r'.{30}chapter 14.{30}', s) if "Chapter 14's form" not in m]
assert not left, left
assert s.count(GIT) == 1 and 'CH = 15' in s and 'ch15_sifrei_spine.txt' in s and 'Deut 15:' in s
open(f'{SP}/ch15_dump0.py', 'w', encoding='utf-8').write(s)
import ast; ast.parse(s)
print('derived ch15_dump0.py', len(s), 'bytes;', len(REPL), 'substitutions; section I in chapter 6\'s form; no portion edge; the last piska\'s tail into 16:1 left for chapter 16 if any')
