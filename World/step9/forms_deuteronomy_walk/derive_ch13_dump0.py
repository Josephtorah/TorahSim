import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE DEUTERONOMY WALK sitting 11 — CHAPTER 13's READING, ONE RUN + ITS TAIL under THE COST RULES A-B-C (2026-09-21; the owner: "Go" after the reread that
# followed 10b's compaction): ch13_dump0.py DERIVED from the forms' ch12_dump0.py by asserted substitutions (derive_ch12_dump0.py's form): the chapter number,
# the file names, the register and prior-read greps, the kin chapters (Exodus 22:19 the sacrifice to other gods, Exodus 32 the calf's "these are your gods",
# Leviticus 20:2 and 24:14-16 the stoning by the people and the witnesses, Leviticus 27:28-29 the devoted thing, Numbers 15:30-31 the high hand, chapter 4's
# signs and wonders and chapter 7's ban and the devoted thing, Genesis 22:1 and chapter 8's "tests you", Numbers 25:4 and Joshua 7's "fierce anger"), the
# drafts by glob; SECTION I in chapter 6's form as at chapter 12 — the SPINE computed from the heads, never typed; NO PORTION EDGE inside the chapter (Re'eh
# 11:26-16:17 holds it whole); the chapter NINETEEN verses in the DB's numbering (sitting 10's ink: the English's 12:32 is the Hebrew's 13:1 — the English's
# chapter 13 runs 1-18 where the DB's runs 1-19: A0's alignment measures the offset, never a typed table).
import os, re, subprocess
ROOT = _ROOT
SP = os.path.dirname(os.path.abspath(__file__))
src = open(f'{ROOT}/World/step9/forms_deuteronomy_walk/ch12_dump0.py', encoding='utf-8').read()
lines = src.split('\n')
s = '\n'.join(lines[2:]) if lines[0] == 'import os as _os' else src
REPL = [
 ("ROOT = _ROOT", "ROOT = _ROOT"),
 ("# DEUTERONOMY CHAPTER 12, THE READING (THE DEUTERONOMY WALK sitting 10, 2026-09-20; the owner: \"Monitor how long each step takes and report when the chapter is done\"; ONE RUN + ITS TAIL under the cost rules) — THE FIRST",
  "# DEUTERONOMY CHAPTER 13, THE READING (THE DEUTERONOMY WALK sitting 11, 2026-09-21; the owner: \"Go\" after the reread that followed 10b's compaction; ONE RUN + ITS TAIL under the cost rules) — THE FIRST"),
 ("# Chapter 11's form (ch11_dump0.py) derived by asserted substitutions (derive_ch12_dump0.py); SECTION I in chapter 6's form — THE SPINE IS ON THE CHAPTER\n# (sitting 9's print: 59 heads on 12:1): the SPINE computed from the heads, the outside rows the union less the spine's own piskaot; NO portion edge inside\n# the chapter (Re'eh 11:26-16:17 holds it whole — the chapter the unit, per the ruling CHAPTER NUMBERS); THIRTY-ONE verses in the DB's numbering.",
  "# Chapter 12's form (ch12_dump0.py) derived by asserted substitutions (derive_ch13_dump0.py); SECTION I in chapter 6's form — THE SPINE IS ON THE CHAPTER\n# (sitting 10's print: 82 heads on 13:1): the SPINE computed from the heads, the outside rows the union less the spine's own piskaot; NO portion edge inside\n# the chapter (Re'eh 11:26-16:17 holds it whole — the chapter the unit, per the ruling CHAPTER NUMBERS); NINETEEN verses in the DB's numbering (the English's\n# 12:32 the DB's 13:1 — the export's chapter 13 against the DB's measured at A0, never typed)."),
 ("CH = 12\n", "CH = 13\n"),
 ("chapters 1-12:', [(c, len(onk_he[c - 1]), VC[c]) for c in range(1, 13)", "chapters 1-13:', [(c, len(onk_he[c - 1]), VC[c]) for c in range(1, 14)"),
 ("print('  heads 58-90 (HE first citation | rows | EN first quote):')\nfor p in range(58, 91):", "print('  heads 80-100 (HE first citation | rows | EN first quote):')\nfor p in range(80, 101):"),
 ("'| heads by chapter 1-12:', sorted(Counter(h[0] for h in heads.values() if h).items())[:12])", "'| heads by chapter 1-13:', sorted(Counter(h[0] for h in heads.values() if h).items())[:13])"),
 ("en_forms = re.compile(r'\\((?:Deut(?:eronomy)?\\.?|Dt\\.?|Devarim) ?(12):(\\d+)')", "en_forms = re.compile(r'\\((?:Deut(?:eronomy)?\\.?|Dt\\.?|Devarim) ?(13):(\\d+)')"),
 ("ibid = [(p, r+1, m.group(0), clean(row)[max(0, m.start()-120):m.start()]) for p in range(1, len(en)+1) for r, row in enumerate(en[p-1]) for m in re.finditer(r'\\((?:Ibid|ibid)\\.? ?12:(\\d+)\\)', clean(row))]",
  "en_1232 = [(p, r+1) for p in range(1, len(en)+1) for r, row in enumerate(en[p-1]) if re.search(r'\\((?:Deut(?:eronomy)?\\.?|Dt\\.?|Devarim) ?12:32', clean(row))]\nprint('  EN rows citing Deut 12:32 (the ENGLISH\\'S number for the DB\\'s 13:1 — the union takes them as 13:1):', len(en_1232), en_1232)\noutside_en += [(p, r, 1) for p, r in en_1232 if (p, r, 1) not in outside_en]\nibid = [(p, r+1, m.group(0), clean(row)[max(0, m.start()-120):m.start()]) for p in range(1, len(en)+1) for r, row in enumerate(en[p-1]) for m in re.finditer(r'\\((?:Ibid|ibid)\\.? ?13:(\\d+)\\)', clean(row))]"),
 ("print('  EN \"ibid 12:n\" candidates:'", "print('  EN \"ibid 13:n\" candidates:'"),
 ("ch12_sifrei_outside.txt", "ch13_sifrei_outside.txt"),
 ("ch12_onkelos.txt", "ch13_onkelos.txt"),
 ("ch12_store_glosses.txt", "ch13_store_glosses.txt"),
 ("ch12_sifrei_spine.txt", "ch13_sifrei_spine.txt"),
 ("| {1, 31}):", "| {1, 19}):"),
 ("print('  dispositions naming Deut 12:', re.findall(r'^([^\\n]*Deut 12:[^\\n]*)$', RD, re.M)[:20])", "print('  dispositions naming Deut 13:', re.findall(r'^([^\\n]*Deut 13:[^\\n]*)$', RD, re.M)[:20])"),
 ("print('  REGISTER_INDEX lines on Deut 12:'); [print('   ', l[:220]) for l in RI.split('\\n') if re.search(r'Deut 12:', l)]", "print('  REGISTER_INDEX lines on Deut 13:'); [print('   ', l[:220]) for l in RI.split('\\n') if re.search(r'Deut 13:', l)]"),
 ("print('  ledgers with an Onkelos Deut 12 row:', sorted(f for f, t in LED.items() if re.search(r'^- Onkelos Deut 12:', t, re.M)))", "print('  ledgers with an Onkelos Deut 13 row:', sorted(f for f, t in LED.items() if re.search(r'^- Onkelos Deut 13:', t, re.M)))"),
 ("NAMING = sorted((f, len(re.findall(r'Deut(?:eronomy)? 12:\\d+', t)), sorted(set(re.findall(r'Deut(?:eronomy)? 12:\\d+(?:-\\d+)?', t)))[:14]) for f, t in LED.items() if re.search(r'Deut(?:eronomy)? 12:\\d+', t))\nprint('  ledgers NAMING a verse of Deut 12:'",
  "NAMING = sorted((f, len(re.findall(r'Deut(?:eronomy)? 13:\\d+', t)), sorted(set(re.findall(r'Deut(?:eronomy)? 13:\\d+(?:-\\d+)?', t)))[:14]) for f, t in LED.items() if re.search(r'Deut(?:eronomy)? 13:\\d+', t))\nprint('  ledgers NAMING a verse of Deut 13:'"),
 ("print('  ledgers with an Onkelos Lev 17 row (the kin\\'s reading — the slaughter at the tent\\'s door and the blood 17:1-16 for 12:15-16 and 12:20-25):', sorted(f for f, t in LED.items() if re.search(r'^- Onkelos Lev 17:', t, re.M)), '| Sifra rows on Lev 17 anywhere:', sum(len(re.findall(r'Sifra[^\\n]{0,60}(?:Acharei|17)', t)) for t in LED.values()), '| ledgers with an Onkelos Exod 20 row (the altar in every place 20:21 for 12:5-14) or a Num 18 row (the tithe and the firstling 18:8-32 for 12:6, 12:17):', sorted(f for f, t in LED.items() if re.search(r'^- Onkelos (?:Exod 20|Num 18):', t, re.M)), '| ledgers with an Onkelos Deut 7 row (the shrines destroyed 7:5, 7:25 — 12:2-3\\'s kin) or a Lev 18/20 row (the children to Molech 18:21, 20:2-5 — 12:31\\'s kin):', sorted(f for f, t in LED.items() if re.search(r'^- Onkelos (?:Deut 7|Lev 18|Lev 20):', t, re.M)))",
  "print('  ledgers with an Onkelos Exod 22 row (the kin\\'s reading — the sacrifice to other gods 22:19 for 13:2-12) or an Exod 32 row (the calf\\'s \"these are your gods\" for 13:3, 13:7, 13:14):', sorted(f for f, t in LED.items() if re.search(r'^- Onkelos Exod (?:22|32):', t, re.M)), '| ledgers with an Onkelos Lev 20 or Lev 24 row (the stoning by the people 20:2 and by the witnesses 24:14-16 for 13:10-11) or a Lev 27 row (the devoted thing 27:28-29 for 13:16-18):', sorted(f for f, t in LED.items() if re.search(r'^- Onkelos Lev (?:20|24|27):', t, re.M)), '| ledgers with an Onkelos Num 15 row (the high hand 15:30-31) or a Num 25 row (the fierce anger 25:4 for 13:18) or a Deut 4 / Deut 7 / Deut 8 row (the signs and wonders 4:34, the ban and the devoted thing 7:2, 7:25-26, the testing 8:2, 8:16 — 13:2-4\\'s and 13:16-18\\'s kin):', sorted(f for f, t in LED.items() if re.search(r'^- Onkelos (?:Num 15|Num 25|Deut 4|Deut 7|Deut 8):', t, re.M)), '| ledgers with an Onkelos Gen 22 row (the test 22:1 for 13:4):', sorted(f for f, t in LED.items() if re.search(r'^- Onkelos Gen 22:', t, re.M)))"),
 ("glob.glob(f'{ROOT}/logic/units/deu_11*.yaml') + glob.glob(f'{ROOT}/logic/units/deu_12*.yaml')", "glob.glob(f'{ROOT}/logic/units/deu_12*.yaml') + glob.glob(f'{ROOT}/logic/units/deu_13*.yaml')"),
 ("    if uid.startswith('deu_12'): print(", "    if uid.startswith('deu_13'): print("),
 ("for p in ('DV12', 'DV12A', 'DV12B', 'DV11', 'DV13')})", "for p in ('DV13', 'DV13A', 'DV13B', 'DV12', 'DV14')})"),
 ("print('  existing manifests deu_12*:', sorted(os.path.basename(f) for f in glob.glob(f'{ROOT}/logic/oral_audit/manifests/deu_12*'))", "print('  existing manifests deu_13*:', sorted(os.path.basename(f) for f in glob.glob(f'{ROOT}/logic/oral_audit/manifests/deu_13*'))"),
 ("print('  overrides already for Deut.12:', re.findall(r'\"Deut\\.12\\.[^\"]+\": \"[^\"]+\"', OV)[:20], '| by_ref last Deut.11 line:', [l for l in OV.split('\\n') if l.startswith('  \"Deut.11.')][-1:])",
  "print('  overrides already for Deut.13:', re.findall(r'\"Deut\\.13\\.[^\"]+\": \"[^\"]+\"', OV)[:20], '| by_ref last Deut.12 line:', [l for l in OV.split('\\n') if l.startswith('  \"Deut.12.')][-1:])"),
]
for old, new in REPL:
    n = s.count(old); assert n >= 1, ('ABSENT', old[:90]); s = s.replace(old, new)
left = [m for m in re.findall(r'.{30}(?:ch12_|Deut 12:|Deut\.12\.|Lev 17|Exod 20|Num 18|Lev 18).{30}', s.replace('ch12_dump0.py', '').replace('Deut 12:32', ''))]
left += [m for m in re.findall(r'.{30}deu_12.{30}', s) if 'glob' not in m]
assert not left, left
open(f'{SP}/ch13_dump0.py', 'w', encoding='utf-8').write(s)
import ast; ast.parse(s)
print('derived ch13_dump0.py', len(s), 'bytes;', len(REPL), 'substitutions; section I in chapter 6\'s form; no portion edge; the English\'s 12:32 folded into the union as 13:1')
