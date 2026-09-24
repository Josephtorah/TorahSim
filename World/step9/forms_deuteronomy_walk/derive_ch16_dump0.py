import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE DEUTERONOMY WALK sitting 14 — CHAPTER 16's READING IN THE LEAN FORM (2026-09-23; the owner: "Reread and go" after the compaction at #208 — THE LEAN PASS's
# first sitting: one reading window + one compile window + a short tail): ch16_dump0.py DERIVED from the forms' ch15_dump0.py by asserted substitutions
# (derive_ch15_dump0.py's form): the chapter number, the file names, the register and prior-read greps, the kin chapters (Exodus 12-13 the Passover and the
# month of Aviv, Exodus 23:14-19 and 34:18-26 the three pilgrimages, Leviticus 23 the appointed times, Numbers 9 and 28-29; Exodus 18, 23:1-8, Leviticus 19:15
# and Deuteronomy 1:9-18 the judges and the bribe; Exodus 34:13, Leviticus 26:1, Deuteronomy 7:5 and 12:3 the asherah and the pillar), the drafts by glob;
# SECTION I in chapter 6's form — the SPINE computed from the heads, never typed; the last on-chapter piska's tail, if it runs into 17:1, LEFT for chapter 17
# (sitting 11's lesson 1); A PORTION EDGE INSIDE THE CHAPTER (Re'eh ends at 16:17, Shoftim opens at 16:18 — the chapter the unit regardless, per the ruling
# CHAPTER NUMBERS); the verse count measured at A0, never typed. RUN FROM THE REPO ROOT.
import os, re, subprocess
ROOT = _ROOT
SP = os.path.dirname(os.path.abspath(__file__))
src = open(f'{ROOT}/World/step9/forms_deuteronomy_walk/ch15_dump0.py', encoding='utf-8').read()
lines = src.split('\n')
assert lines[0] == 'import os as _os' and lines[1].startswith('_ROOT = '), lines[:2]
s = '\n'.join(lines[2:])
GIT = "ROOT = _ROOT"
REPL = [
 ("ROOT = _ROOT", GIT),
 ("# DEUTERONOMY CHAPTER 15, THE READING (THE DEUTERONOMY WALK sitting 13, 2026-09-22; the owner: \"Go\" after the compaction at #205 addendum 5; TWO RUNS + THE TAIL under the cost rules — the #204 NOTE) — THE FIRST",
  "# DEUTERONOMY CHAPTER 16, THE READING IN THE LEAN FORM (THE DEUTERONOMY WALK sitting 14, 2026-09-23; the owner: \"Reread and go\" after the compaction at #208 — THE LEAN PASS's first sitting) — THE FIRST"),
 ("# Chapter 14's form (ch14_dump0.py) derived by asserted substitutions (derive_ch15_dump0.py); SECTION I in chapter 6's form — THE SPINE IS ON THE CHAPTER\n# (sitting 12's print: 111 heads on 15:1; the last on-chapter piska's tail, if it runs into 16:1, LEFT for chapter 16 — sitting 11's lesson 1): the SPINE\n# computed from the heads, the outside rows the union less the spine's own piskaot; NO portion edge inside the chapter (Re'eh 11:26-16:17 holds it whole — the\n# chapter the unit, per the ruling CHAPTER NUMBERS); the verse count in the DB's numbering measured at A0 (the export's chapter 15 against the DB's), never typed.",
  "# Chapter 15's form (the forms' dump of chapter 15) derived by asserted substitutions (derive_ch16_dump0.py); SECTION I in chapter 6's form — THE SPINE IS ON THE CHAPTER\n# (sitting 13's print: 127 heads on 16:1; the last on-chapter piska's tail, if it runs into 17:1, LEFT for chapter 17 — sitting 11's lesson 1): the SPINE\n# computed from the heads, the outside rows the union less the spine's own piskaot; A PORTION EDGE INSIDE THE CHAPTER (Re'eh ends at 16:17, Shoftim opens at\n# 16:18 — the chapter the unit regardless, per the ruling CHAPTER NUMBERS); the verse count in the DB's numbering measured at A0 (the export's chapter 16 against the DB's), never typed."),
 ("CH = 15\n", "CH = 16\n"),
 ("chapters 1-15:', [(c, len(onk_he[c - 1]), VC[c]) for c in range(1, 16)", "chapters 1-16:', [(c, len(onk_he[c - 1]), VC[c]) for c in range(1, 17)"),
 ("print('  heads 108-130 (HE first citation | rows | EN first quote):')\nfor p in range(108, 131):", "print('  heads 124-150 (HE first citation | rows | EN first quote):')\nfor p in range(124, 151):"),
 ("'| heads by chapter 1-15:', sorted(Counter(h[0] for h in heads.values() if h).items())[:15])", "'| heads by chapter 1-16:', sorted(Counter(h[0] for h in heads.values() if h).items())[:16])"),
 (r"""en_forms = re.compile(r'\((?:Deut(?:eronomy)?\.?|Dt\.?|Devarim) ?(15):(\d+)')""", r"""en_forms = re.compile(r'\((?:Deut(?:eronomy)?\.?|Dt\.?|Devarim) ?(16):(\d+)')"""),
 ("# (no fold of the English's numbering this chapter either — the English's chapter 15 counts as the Hebrew's; A0 measures it)\n",
  "# (no fold of the English's numbering this chapter either — the English's chapter 16 counts as the Hebrew's; A0 measures it)\n"),
 (r"""re.finditer(r'\((?:Ibid|ibid)\.? ?15:(\d+)\)', clean(row))]""", r"""re.finditer(r'\((?:Ibid|ibid)\.? ?16:(\d+)\)', clean(row))]"""),
 ("print('  EN \"ibid 15:n\" candidates:'", "print('  EN \"ibid 16:n\" candidates:'"),
 ("ch15_sifrei_outside.txt", "ch16_sifrei_outside.txt"),
 ("ch15_onkelos.txt", "ch16_onkelos.txt"),
 ("ch15_store_glosses.txt", "ch16_store_glosses.txt"),
 ("ch15_sifrei_spine.txt", "ch16_sifrei_spine.txt"),
 ("print('  dispositions naming Deut 15:', re.findall(r'^([^\\n]*Deut 15:[^\\n]*)$', RD, re.M)[:20])", "print('  dispositions naming Deut 16:', re.findall(r'^([^\\n]*Deut 16:[^\\n]*)$', RD, re.M)[:20])"),
 ("print('  REGISTER_INDEX lines on Deut 15:'); [print('   ', l[:220]) for l in RI.split('\\n') if re.search(r'Deut 15:', l)]", "print('  REGISTER_INDEX lines on Deut 16:'); [print('   ', l[:220]) for l in RI.split('\\n') if re.search(r'Deut 16:', l)]"),
 ("print('  ledgers with an Onkelos Deut 15 row:', sorted(f for f, t in LED.items() if re.search(r'^- Onkelos Deut 15:', t, re.M)))", "print('  ledgers with an Onkelos Deut 16 row:', sorted(f for f, t in LED.items() if re.search(r'^- Onkelos Deut 16:', t, re.M)))"),
 ("NAMING = sorted((f, len(re.findall(r'Deut(?:eronomy)? 15:\\d+', t)), sorted(set(re.findall(r'Deut(?:eronomy)? 15:\\d+(?:-\\d+)?', t)))[:14]) for f, t in LED.items() if re.search(r'Deut(?:eronomy)? 15:\\d+', t))\nprint('  ledgers NAMING a verse of Deut 15:'",
  "NAMING = sorted((f, len(re.findall(r'Deut(?:eronomy)? 16:\\d+', t)), sorted(set(re.findall(r'Deut(?:eronomy)? 16:\\d+(?:-\\d+)?', t)))[:14]) for f, t in LED.items() if re.search(r'Deut(?:eronomy)? 16:\\d+', t))\nprint('  ledgers NAMING a verse of Deut 16:'"),
 ("glob.glob(f'{ROOT}/logic/units/deu_14*.yaml') + glob.glob(f'{ROOT}/logic/units/deu_15*.yaml')", "glob.glob(f'{ROOT}/logic/units/deu_15*.yaml') + glob.glob(f'{ROOT}/logic/units/deu_16*.yaml')"),
 ("    if uid.startswith('deu_15'): print(", "    if uid.startswith('deu_16'): print("),
 ("for p in ('DV15', 'DV15A', 'DV15B', 'DV14', 'DV16')})", "for p in ('DV16', 'DV16A', 'DV16B', 'DV15', 'DV17')})"),
 ("print('  existing manifests deu_15*:', sorted(os.path.basename(f) for f in glob.glob(f'{ROOT}/logic/oral_audit/manifests/deu_15*'))", "print('  existing manifests deu_16*:', sorted(os.path.basename(f) for f in glob.glob(f'{ROOT}/logic/oral_audit/manifests/deu_16*'))"),
 ("print('  overrides already for Deut.15:', re.findall(r'\"Deut\\.15\\.[^\"]+\": \"[^\"]+\"', OV)[:20], '| by_ref last Deut.14 line:', [l for l in OV.split('\\n') if l.startswith('  \"Deut.14.')][-1:])",
  "print('  overrides already for Deut.16:', re.findall(r'\"Deut\\.16\\.[^\"]+\": \"[^\"]+\"', OV)[:20], '| by_ref last Deut.15 line:', [l for l in OV.split('\\n') if l.startswith('  \"Deut.15.')][-1:])"),
 ("'(the spine on the chapter a seventh time), whole')", "'(the spine on the chapter an eighth time), whole')"),
 ("print('  NO portion edge inside the chapter (Re\\'eh 11:26-16:17 holds it whole) — the heads by verse, and the verses of the chapter with no head:'",
  "print('  THE PORTION EDGE inside the chapter (Re\\'eh ends at 16:17, Shoftim opens at 16:18) — the heads by verse, and the verses of the chapter with no head:'"),
]
CNT = {'ch15_sifrei_outside.txt': 2, 'ch15_onkelos.txt': 2, 'ch15_store_glosses.txt': 2, 'ch15_sifrei_spine.txt': 2}   # the four file names each opened and sized (the second derive's lesson: the count asserted per row, read from the print)
for old, new in REPL:
    c = s.count(old); assert c == CNT.get(old, 1), (c, old[:90]); s = s.replace(old, new)
# THE KIN LINE (section F) retyped whole for chapter 16 — found by its head and its tail
i = s.index("print('  ledgers with an Onkelos Exod 21 / Exod 22 / Exod 23 row (the kin\\'s reading"); j = s.index('\n', i)
KIN = ("print('  ledgers with an Onkelos Exod 12 / Exod 13 / Exod 23 / Exod 34 / Lev 23 / Num 9 / Num 28 / Num 29 row (the kin\\'s reading — the Passover 12:1-28, 12:43-50, the unleavened bread and the month of Aviv 13:3-10, the three pilgrimages 23:14-19 and 34:18-26, the appointed times Leviticus 23, the second Passover Numbers 9, the offerings 28-29 for 16:1-17):', sorted(f for f, t in LED.items() if re.search(r'^- Onkelos (?:Exod (?:12|13|23|34)|Lev 23|Num (?:9|28|29)):', t, re.M)), "
       "'| ledgers with an Onkelos Exod 18 / Exod 23 / Lev 19 / Deut 1 row (the judges and the bribe — Exodus 18:13-26, 23:1-8, Leviticus 19:15, Deuteronomy 1:9-18 for 16:18-20):', sorted(f for f, t in LED.items() if re.search(r'^- Onkelos (?:Exod (?:18|23)|Lev 19|Deut 1):', t, re.M)), "
       "'| ledgers with an Onkelos Exod 34 / Lev 26 / Deut 7 / Deut 12 row (the asherah and the pillar — Exodus 34:13, Leviticus 26:1, Deuteronomy 7:5, 12:3 for 16:21-22):', sorted(f for f, t in LED.items() if re.search(r'^- Onkelos (?:Exod 34|Lev 26|Deut (?:7|12)):', t, re.M)))")
s = s[:i] + KIN + s[j:]
assert 'ch15_' not in s.replace("the forms' dump of chapter 15", '') and 'Deut 15' not in s and '_ROOT' not in s and 'chapter 15' not in s.replace("Chapter 15's form", '').replace('the forms\' dump of chapter 15', '') and 'Deut\\.15' not in s.replace('Deut\\.15.', ''), [m for m in re.findall(r'.{40}(?:ch15_|Deut 15|_ROOT|chapter 15).{40}', s)]
open(f'{SP}/ch16_dump0.py', 'w', encoding='utf-8').write(s)
import ast; ast.parse(s); print('ch16_dump0.py derived:', len(s), 'bytes;', len(REPL), 'substitutions + the kin line')
