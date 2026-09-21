import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE DEUTERONOMY WALK sitting 10 — CHAPTER 12's READING, ONE RUN + ITS TAIL under THE COST RULES A-B-C (2026-09-20; the owner: "Monitor how long each step
# takes and report when the chapter is done" — the first sitting under the rules): ch12_dump0.py DERIVED from the forms' ch11_dump0.py by asserted substitutions
# (derive_ch11_dump0.py's form): the chapter number, the file names, the register and prior-read greps, the kin chapters (Leviticus 17 the slaughter at the tent
# and the blood for 12:15-16 and 12:20-25, Exodus 20 the altar in every place for 12:5-14, Numbers 18 the tithe and the firstling for 12:6 and 12:17, Deuteronomy 7
# the shrines destroyed for 12:2-3), the drafts by glob; SECTION I in chapter 6's form as at chapter 11 — the SPINE computed from the heads, never typed; NO PORTION
# EDGE inside the chapter (Re'eh 11:26-16:17 holds it whole); the chapter THIRTY-ONE verses in the DB's numbering (chapter 11's ink: the English's 12:32 is the
# Hebrew's 13:1).
import os, re, subprocess
ROOT = _ROOT
SP = os.path.dirname(os.path.abspath(__file__))
src = open(f'{ROOT}/World/step9/forms_deuteronomy_walk/ch11_dump0.py', encoding='utf-8').read()
lines = src.split('\n')
s = '\n'.join(lines[2:]) if lines[0] == 'import os as _os' else src
REPL = [
 ("ROOT = _ROOT", "ROOT = _ROOT"),
 ("# DEUTERONOMY CHAPTER 11, THE READING (THE DEUTERONOMY WALK sitting 9, 2026-09-20; the owner: \"Go\"; ONE RUN under the two-run rule) — THE FIRST",
  "# DEUTERONOMY CHAPTER 12, THE READING (THE DEUTERONOMY WALK sitting 10, 2026-09-20; the owner: \"Monitor how long each step takes and report when the chapter is done\"; ONE RUN + ITS TAIL under the cost rules) — THE FIRST"),
 ("# Chapter 10's form (ch10_dump0.py) derived by asserted substitutions (derive_ch11_dump0.py); SECTION I RETURNS in chapter 6's form — THE SPINE IS ON THE\n# CHAPTER (sitting 8's A print: 37-38 on 11:10, 39 on 11:11; twenty-one heads in chapter 11): the SPINE computed from the heads, the outside rows the union\n# less the spine's own piskaot; the portion's edge inside the chapter (Ekev to 11:25, Re'eh from 11:26 — the chapter the unit, per the ruling CHAPTER NUMBERS).",
  "# Chapter 11's form (ch11_dump0.py) derived by asserted substitutions (derive_ch12_dump0.py); SECTION I in chapter 6's form — THE SPINE IS ON THE CHAPTER\n# (sitting 9's print: 59 heads on 12:1): the SPINE computed from the heads, the outside rows the union less the spine's own piskaot; NO portion edge inside\n# the chapter (Re'eh 11:26-16:17 holds it whole — the chapter the unit, per the ruling CHAPTER NUMBERS); THIRTY-ONE verses in the DB's numbering."),
 ("CH = 11\n", "CH = 12\n"),
 ("chapters 1-11:', [(c, len(onk_he[c - 1]), VC[c]) for c in range(1, 12)", "chapters 1-12:', [(c, len(onk_he[c - 1]), VC[c]) for c in range(1, 13)"),
 ("print('  heads 36-59 (HE first citation | rows | EN first quote):')\nfor p in range(36, 60):", "print('  heads 58-90 (HE first citation | rows | EN first quote):')\nfor p in range(58, 91):"),
 ("'| heads by chapter 1-11:', sorted(Counter(h[0] for h in heads.values() if h).items())[:11])", "'| heads by chapter 1-12:', sorted(Counter(h[0] for h in heads.values() if h).items())[:12])"),
 ("en_forms = re.compile(r'\\((?:Deut(?:eronomy)?\\.?|Dt\\.?|Devarim) ?(11):(\\d+)')", "en_forms = re.compile(r'\\((?:Deut(?:eronomy)?\\.?|Dt\\.?|Devarim) ?(12):(\\d+)')"),
 ("r'\\((?:Ibid|ibid)\\.? ?11:(\\d+)\\)'", "r'\\((?:Ibid|ibid)\\.? ?12:(\\d+)\\)'"),
 ("print('  EN \"ibid 11:n\" candidates:'", "print('  EN \"ibid 12:n\" candidates:'"),
 ("ch11_sifrei_outside.txt", "ch12_sifrei_outside.txt"),
 ("ch11_onkelos.txt", "ch12_onkelos.txt"),
 ("ch11_store_glosses.txt", "ch12_store_glosses.txt"),
 ("ch11_sifrei_spine.txt", "ch12_sifrei_spine.txt"),
 ("| {1, 32}):", "| {1, 31}):"),
 ("print('  dispositions naming Deut 11:', re.findall(r'^([^\\n]*Deut 11:[^\\n]*)$', RD, re.M)[:20])", "print('  dispositions naming Deut 12:', re.findall(r'^([^\\n]*Deut 12:[^\\n]*)$', RD, re.M)[:20])"),
 ("print('  REGISTER_INDEX lines on Deut 11:'); [print('   ', l[:220]) for l in RI.split('\\n') if re.search(r'Deut 11:', l)]", "print('  REGISTER_INDEX lines on Deut 12:'); [print('   ', l[:220]) for l in RI.split('\\n') if re.search(r'Deut 12:', l)]"),
 ("print('  ledgers with an Onkelos Deut 11 row:', sorted(f for f, t in LED.items() if re.search(r'^- Onkelos Deut 11:', t, re.M)))", "print('  ledgers with an Onkelos Deut 12 row:', sorted(f for f, t in LED.items() if re.search(r'^- Onkelos Deut 12:', t, re.M)))"),
 ("NAMING = sorted((f, len(re.findall(r'Deut(?:eronomy)? 11:\\d+', t)), sorted(set(re.findall(r'Deut(?:eronomy)? 11:\\d+(?:-\\d+)?', t)))[:14]) for f, t in LED.items() if re.search(r'Deut(?:eronomy)? 11:\\d+', t))\nprint('  ledgers NAMING a verse of Deut 11:'",
  "NAMING = sorted((f, len(re.findall(r'Deut(?:eronomy)? 12:\\d+', t)), sorted(set(re.findall(r'Deut(?:eronomy)? 12:\\d+(?:-\\d+)?', t)))[:14]) for f, t in LED.items() if re.search(r'Deut(?:eronomy)? 12:\\d+', t))\nprint('  ledgers NAMING a verse of Deut 12:'"),
 ("print('  ledgers with an Onkelos Exod 14 or 23 row (the kin\\'s reading — the sea 14:21-31 for 11:4, the dread and the borders 23:27-31 for 11:24-25):', sorted(f for f, t in LED.items() if re.search(r'^- Onkelos Exod (14|23):', t, re.M)), '| Mekhilta rows on Exod 14/23 anywhere:', sum(len(re.findall(r'Mekhilta[^\\n]{0,40}(?:14|23):\\d+', t)) for t in LED.values()), '| ledgers with an Onkelos Num 16 row (Dathan and Abiram 16:25-34 for 11:6) or a Gen 15 row (the borders sworn 15:18 for 11:24):', sorted(f for f, t in LED.items() if re.search(r'^- Onkelos (?:Num 16|Gen 15):', t, re.M)), '| ledgers with an Onkelos Deut 6 row (the Shema\\'s first paragraph — 11:13-21 its second):', sorted(f for f, t in LED.items() if re.search(r'^- Onkelos Deut 6:', t, re.M)))",
  "print('  ledgers with an Onkelos Lev 17 row (the kin\\'s reading — the slaughter at the tent\\'s door and the blood 17:1-16 for 12:15-16 and 12:20-25):', sorted(f for f, t in LED.items() if re.search(r'^- Onkelos Lev 17:', t, re.M)), '| Sifra rows on Lev 17 anywhere:', sum(len(re.findall(r'Sifra[^\\n]{0,60}(?:Acharei|17)', t)) for t in LED.values()), '| ledgers with an Onkelos Exod 20 row (the altar in every place 20:21 for 12:5-14) or a Num 18 row (the tithe and the firstling 18:8-32 for 12:6, 12:17):', sorted(f for f, t in LED.items() if re.search(r'^- Onkelos (?:Exod 20|Num 18):', t, re.M)), '| ledgers with an Onkelos Deut 7 row (the shrines destroyed 7:5, 7:25 — 12:2-3\\'s kin) or a Lev 18/20 row (the children to Molech 18:21, 20:2-5 — 12:31\\'s kin):', sorted(f for f, t in LED.items() if re.search(r'^- Onkelos (?:Deut 7|Lev 18|Lev 20):', t, re.M)))"),
 ("glob.glob(f'{ROOT}/logic/units/deu_10*.yaml') + glob.glob(f'{ROOT}/logic/units/deu_11*.yaml')", "glob.glob(f'{ROOT}/logic/units/deu_11*.yaml') + glob.glob(f'{ROOT}/logic/units/deu_12*.yaml')"),
 ("    if uid.startswith('deu_11'): print(", "    if uid.startswith('deu_12'): print("),
 ("for p in ('DV11', 'DV11A', 'DV11B', 'DV10', 'DV12')})", "for p in ('DV12', 'DV12A', 'DV12B', 'DV11', 'DV13')})"),
 ("print('  existing manifests deu_11*:', sorted(os.path.basename(f) for f in glob.glob(f'{ROOT}/logic/oral_audit/manifests/deu_11*'))", "print('  existing manifests deu_12*:', sorted(os.path.basename(f) for f in glob.glob(f'{ROOT}/logic/oral_audit/manifests/deu_12*'))"),
 ("print('  overrides already for Deut.11:', re.findall(r'\"Deut\\.11\\.[^\"]+\": \"[^\"]+\"', OV)[:20], '| by_ref last Deut.10 line:', [l for l in OV.split('\\n') if l.startswith('  \"Deut.10.')][-1:])",
  "print('  overrides already for Deut.12:', re.findall(r'\"Deut\\.12\\.[^\"]+\": \"[^\"]+\"', OV)[:20], '| by_ref last Deut.11 line:', [l for l in OV.split('\\n') if l.startswith('  \"Deut.11.')][-1:])"),
 ("print('  the portion edge inside the chapter: Ekev ends at 11:25, Re\\'eh opens at 11:26 — the heads at or after verse 26:', [(p, heads[p]) for p in SPINE if heads[p][1] >= 26])",
  "print('  NO portion edge inside the chapter (Re\\'eh 11:26-16:17 holds it whole) — the heads by verse, and the verses of the chapter with no head:', sorted({heads[p][1] for p in SPINE}), [v for v in range(1, VC[CH] + 1) if v not in {heads[p][1] for p in SPINE}])"),
]
for old, new in REPL:
    n = s.count(old); assert n >= 1, ('ABSENT', old[:90]); s = s.replace(old, new)
left = [m for m in re.findall(r'.{30}(?:ch11_|Deut 11:|Deut\.11\.|Exod \(14\|23\)|Num 16|Gen 15).{30}', s.replace('ch11_dump0.py', ''))]
left += [m for m in re.findall(r'.{30}deu_11.{30}', s) if 'glob' not in m]
assert not left, left
open(f'{SP}/ch12_dump0.py', 'w', encoding='utf-8').write(s)
import ast; ast.parse(s)
print('derived ch12_dump0.py', len(s), 'bytes;', len(REPL), 'substitutions; section I in chapter 6\'s form; no portion edge')
