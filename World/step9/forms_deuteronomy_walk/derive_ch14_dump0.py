import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE DEUTERONOMY WALK sitting 12 — CHAPTER 14's READING, ONE RUN + ITS TAIL under THE COST RULES A-B-C (2026-09-21; the owner: "Go" after 11b's tail — the
# commit still on his word): ch14_dump0.py DERIVED from the forms' ch13_dump0.py by asserted substitutions (derive_ch13_dump0.py's form): the chapter number,
# the file names, the register and prior-read greps, the kin chapters (Leviticus 11 the clean and the unclean, Leviticus 19:27-28 and 21:5 the cuts and the
# baldness, Leviticus 17:15 and 22:8 the carcass and the torn, Exodus 22:30 / 23:19 / 34:26 the torn flesh and the kid in its mother's milk, Exodus 19:5-6 and
# chapter 7's holy people, Numbers 18 and Leviticus 27 the tithe, chapter 12's tithe at the place and the Levite, Genesis 7's clean beasts), the drafts by glob;
# SECTION I in chapter 6's form — the SPINE computed from the heads, never typed; PISKA 96's ROWS 9-12 ARE 14:1's (sitting 11's lesson 1) — outside the
# on-chapter piskaot, found by the union of both files' citations (96:10 cites Amos 9:6 alone — folded by the consonant rule at the split, as 88 was at 13);
# NO PORTION EDGE inside the chapter (Re'eh 11:26-16:17 holds it whole); the chapter TWENTY-NINE verses in the DB's numbering (the English's chapter 14 counts
# as the Hebrew's — A0 measures it, never a typed table; chapter 13's 12:32 fold is not this chapter's). RUN FROM THE REPO ROOT.
import os, re, subprocess
ROOT = _ROOT
SP = os.path.dirname(os.path.abspath(__file__))
src = open(f'{ROOT}/World/step9/forms_deuteronomy_walk/ch13_dump0.py', encoding='utf-8').read()
lines = src.split('\n')
s = '\n'.join(lines[2:]) if lines[0] == 'import os as _os' else src
GIT = "ROOT = _ROOT"
REPL = [
 ("ROOT = _ROOT", GIT),
 ("# DEUTERONOMY CHAPTER 13, THE READING (THE DEUTERONOMY WALK sitting 11, 2026-09-21; the owner: \"Go\" after the reread that followed 10b's compaction; ONE RUN + ITS TAIL under the cost rules) — THE FIRST",
  "# DEUTERONOMY CHAPTER 14, THE READING (THE DEUTERONOMY WALK sitting 12, 2026-09-21; the owner: \"Go\" after 11b's tail; ONE RUN + ITS TAIL under the cost rules) — THE FIRST"),
 ("# Chapter 12's form (ch12_dump0.py) derived by asserted substitutions (derive_ch13_dump0.py); SECTION I in chapter 6's form — THE SPINE IS ON THE CHAPTER\n# (sitting 10's print: 82 heads on 13:1): the SPINE computed from the heads, the outside rows the union less the spine's own piskaot; NO portion edge inside\n# the chapter (Re'eh 11:26-16:17 holds it whole — the chapter the unit, per the ruling CHAPTER NUMBERS); NINETEEN verses in the DB's numbering (the English's\n# 12:32 the DB's 13:1 — the export's chapter 13 against the DB's measured at A0, never typed).",
  "# Chapter 13's form (ch13_dump0.py) derived by asserted substitutions (derive_ch14_dump0.py); SECTION I in chapter 6's form — THE SPINE IS ON THE CHAPTER\n# (sitting 11's print: 97 heads on 14:2; PISKA 96's ROWS 9-12 ARE 14:1's — outside the on-chapter piskaot, found by the union, folded at the split): the SPINE\n# computed from the heads, the outside rows the union less the spine's own piskaot; NO portion edge inside the chapter (Re'eh 11:26-16:17 holds it whole — the\n# chapter the unit, per the ruling CHAPTER NUMBERS); TWENTY-NINE verses in the DB's numbering (the export's chapter 14 against the DB's measured at A0, never typed)."),
 ("CH = 13\n", "CH = 14\n"),
 ("chapters 1-13:', [(c, len(onk_he[c - 1]), VC[c]) for c in range(1, 14)", "chapters 1-14:', [(c, len(onk_he[c - 1]), VC[c]) for c in range(1, 15)"),
 ("print('  heads 80-100 (HE first citation | rows | EN first quote):')\nfor p in range(80, 101):", "print('  heads 94-116 (HE first citation | rows | EN first quote):')\nfor p in range(94, 117):"),
 ("'| heads by chapter 1-13:', sorted(Counter(h[0] for h in heads.values() if h).items())[:13])", "'| heads by chapter 1-14:', sorted(Counter(h[0] for h in heads.values() if h).items())[:14])"),
 (r"""en_forms = re.compile(r'\((?:Deut(?:eronomy)?\.?|Dt\.?|Devarim) ?(13):(\d+)')""", r"""en_forms = re.compile(r'\((?:Deut(?:eronomy)?\.?|Dt\.?|Devarim) ?(14):(\d+)')"""),
 (r"""en_1232 = [(p, r+1) for p in range(1, len(en)+1) for r, row in enumerate(en[p-1]) if re.search(r'\((?:Deut(?:eronomy)?\.?|Dt\.?|Devarim) ?12:32', clean(row))]
print('  EN rows citing Deut 12:32 (the ENGLISH\'S number for the DB\'s 13:1 — the union takes them as 13:1):', len(en_1232), en_1232)
outside_en += [(p, r, 1) for p, r in en_1232 if (p, r, 1) not in outside_en]
""", "# (chapter 13's fold of the English's 12:32 into 13:1 is not chapter 14's — the English's chapter 14 counts as the Hebrew's; A0 measures it)\n"),
 (r"""re.finditer(r'\((?:Ibid|ibid)\.? ?13:(\d+)\)', clean(row))]""", r"""re.finditer(r'\((?:Ibid|ibid)\.? ?14:(\d+)\)', clean(row))]"""),
 ("print('  EN \"ibid 13:n\" candidates:'", "print('  EN \"ibid 14:n\" candidates:'"),
 ("ch13_sifrei_outside.txt", "ch14_sifrei_outside.txt"),
 ("ch13_onkelos.txt", "ch14_onkelos.txt"),
 ("ch13_store_glosses.txt", "ch14_store_glosses.txt"),
 ("ch13_sifrei_spine.txt", "ch14_sifrei_spine.txt"),
 ("| {1, 19}):", "| {1, 29}):"),
 ("print('  dispositions naming Deut 13:', re.findall(r'^([^\\n]*Deut 13:[^\\n]*)$', RD, re.M)[:20])", "print('  dispositions naming Deut 14:', re.findall(r'^([^\\n]*Deut 14:[^\\n]*)$', RD, re.M)[:20])"),
 ("print('  REGISTER_INDEX lines on Deut 13:'); [print('   ', l[:220]) for l in RI.split('\\n') if re.search(r'Deut 13:', l)]", "print('  REGISTER_INDEX lines on Deut 14:'); [print('   ', l[:220]) for l in RI.split('\\n') if re.search(r'Deut 14:', l)]"),
 ("print('  ledgers with an Onkelos Deut 13 row:', sorted(f for f, t in LED.items() if re.search(r'^- Onkelos Deut 13:', t, re.M)))", "print('  ledgers with an Onkelos Deut 14 row:', sorted(f for f, t in LED.items() if re.search(r'^- Onkelos Deut 14:', t, re.M)))"),
 ("NAMING = sorted((f, len(re.findall(r'Deut(?:eronomy)? 13:\\d+', t)), sorted(set(re.findall(r'Deut(?:eronomy)? 13:\\d+(?:-\\d+)?', t)))[:14]) for f, t in LED.items() if re.search(r'Deut(?:eronomy)? 13:\\d+', t))\nprint('  ledgers NAMING a verse of Deut 13:'",
  "NAMING = sorted((f, len(re.findall(r'Deut(?:eronomy)? 14:\\d+', t)), sorted(set(re.findall(r'Deut(?:eronomy)? 14:\\d+(?:-\\d+)?', t)))[:14]) for f, t in LED.items() if re.search(r'Deut(?:eronomy)? 14:\\d+', t))\nprint('  ledgers NAMING a verse of Deut 14:'"),
 ("print('  ledgers with an Onkelos Exod 22 row (the kin\\'s reading — the sacrifice to other gods 22:19 for 13:2-12) or an Exod 32 row (the calf\\'s \"these are your gods\" for 13:3, 13:7, 13:14):', sorted(f for f, t in LED.items() if re.search(r'^- Onkelos Exod (?:22|32):', t, re.M)), '| ledgers with an Onkelos Lev 20 or Lev 24 row (the stoning by the people 20:2 and by the witnesses 24:14-16 for 13:10-11) or a Lev 27 row (the devoted thing 27:28-29 for 13:16-18):', sorted(f for f, t in LED.items() if re.search(r'^- Onkelos Lev (?:20|24|27):', t, re.M)), '| ledgers with an Onkelos Num 15 row (the high hand 15:30-31) or a Num 25 row (the fierce anger 25:4 for 13:18) or a Deut 4 / Deut 7 / Deut 8 row (the signs and wonders 4:34, the ban and the devoted thing 7:2, 7:25-26, the testing 8:2, 8:16 — 13:2-4\\'s and 13:16-18\\'s kin):', sorted(f for f, t in LED.items() if re.search(r'^- Onkelos (?:Num 15|Num 25|Deut 4|Deut 7|Deut 8):', t, re.M)), '| ledgers with an Onkelos Gen 22 row (the test 22:1 for 13:4):', sorted(f for f, t in LED.items() if re.search(r'^- Onkelos Gen 22:', t, re.M)))",
  "print('  ledgers with an Onkelos Lev 11 row (the kin\\'s reading — the clean and the unclean animals 11:1-47 for 14:3-21) or a Lev 19 / Lev 21 row (the cuts for the dead 19:27-28 and the priests\\' baldness 21:5 for 14:1) or a Lev 17 / Lev 22 row (the carcass and the torn 17:15, 22:8 for 14:21):', sorted(f for f, t in LED.items() if re.search(r'^- Onkelos Lev (?:11|17|19|21|22):', t, re.M)), '| ledgers with an Onkelos Exod 22 / Exod 23 / Exod 34 row (the torn flesh 22:30, the kid in its mother\\'s milk 23:19 and 34:26 for 14:21) or an Exod 19 row (the treasured people 19:5-6 for 14:2):', sorted(f for f, t in LED.items() if re.search(r'^- Onkelos Exod (?:19|22|23|34):', t, re.M)), '| ledgers with an Onkelos Num 18 row (the tithe to the Levites 18:21-32 for 14:22-29) or a Lev 27 row (the tithe holy to the LORD 27:30-33) or a Deut 7 / Deut 12 row (the holy people 7:6 for 14:2; the tithe eaten at the place and the Levite 12:6, 12:17-19 for 14:22-27):', sorted(f for f, t in LED.items() if re.search(r'^- Onkelos (?:Num 18|Lev 27|Deut 7|Deut 12):', t, re.M)), '| ledgers with an Onkelos Gen 7 row (the clean beasts 7:2 for 14:4):', sorted(f for f, t in LED.items() if re.search(r'^- Onkelos Gen 7:', t, re.M)))"),
 ("glob.glob(f'{ROOT}/logic/units/deu_12*.yaml') + glob.glob(f'{ROOT}/logic/units/deu_13*.yaml')", "glob.glob(f'{ROOT}/logic/units/deu_13*.yaml') + glob.glob(f'{ROOT}/logic/units/deu_14*.yaml')"),
 ("    if uid.startswith('deu_13'): print(", "    if uid.startswith('deu_14'): print("),
 ("for p in ('DV13', 'DV13A', 'DV13B', 'DV12', 'DV14')})", "for p in ('DV14', 'DV14A', 'DV14B', 'DV13', 'DV15')})"),
 ("print('  existing manifests deu_13*:', sorted(os.path.basename(f) for f in glob.glob(f'{ROOT}/logic/oral_audit/manifests/deu_13*'))", "print('  existing manifests deu_14*:', sorted(os.path.basename(f) for f in glob.glob(f'{ROOT}/logic/oral_audit/manifests/deu_14*'))"),
 ("print('  overrides already for Deut.13:', re.findall(r'\"Deut\\.13\\.[^\"]+\": \"[^\"]+\"', OV)[:20], '| by_ref last Deut.12 line:', [l for l in OV.split('\\n') if l.startswith('  \"Deut.12.')][-1:])",
  "print('  overrides already for Deut.14:', re.findall(r'\"Deut\\.14\\.[^\"]+\": \"[^\"]+\"', OV)[:20], '| by_ref last Deut.13 line:', [l for l in OV.split('\\n') if l.startswith('  \"Deut.13.')][-1:])"),
]
for old, new in REPL:
    n = s.count(old); assert n >= 1, ('ABSENT', old[:90]); s = s.replace(old, new)
left = [m for m in re.findall(r'.{30}(?:ch13_|Deut 13:|Deut\.13\.|Exod \(\?:22\|32\)|Lev \(\?:20|Num 15|Gen 22|12:32|_ROOT).{30}', s.replace('ch13_dump0.py', '').replace("# (chapter 13's fold of the English's 12:32 into 13:1 is not chapter 14's", ''))]   # the derive's own comment line excluded from its guard
left += [m for m in re.findall(r'.{30}deu_13.{30}', s) if 'glob' not in m]
assert not left, left
assert s.count(GIT) == 1 and 'CH = 14' in s
open(f'{SP}/ch14_dump0.py', 'w', encoding='utf-8').write(s)
import ast; ast.parse(s)
print('derived ch14_dump0.py', len(s), 'bytes;', len(REPL), 'substitutions; section I in chapter 6\'s form; no portion edge; piska 96:9-12 to the union (outside the spine piskaot), folded at the split')
