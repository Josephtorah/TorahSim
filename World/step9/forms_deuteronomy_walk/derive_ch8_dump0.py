#!/usr/bin/env python3
# THE DEUTERONOMY WALK sitting 6 — CHAPTER 8's READING, ONE RUN under THE TWO-RUN RULE (2026-09-18; the owner: "Go"): ch8_dump0.py DERIVED from the
# forms' ch7_dump0.py by asserted substitutions (derive_ch7_dump0.py's form): the chapter number, the file names, the register and prior-read greps,
# the kin chapters (Exodus 16-17 the manna and the rock; Numbers 11, 14, 20, 21 the craving, the forty years, Meribah, the serpents — where chapter 8's
# retold acts have their first tellings), the drafts by glob; SECTION I stays dropped — no piska head on chapter 8 (chapter 7's A print: 36 on 6:9,
# 37 on 11:10); the forms' portable header (if any) turned back to the git root for a scratch run.
import os, re, subprocess
ROOT = subprocess.check_output(['git', 'rev-parse', '--show-toplevel'], text=True).strip()
SP = os.path.dirname(os.path.abspath(__file__))
src = open(f'{ROOT}/World/step9/forms_deuteronomy_walk/ch7_dump0.py', encoding='utf-8').read()
lines = src.split('\n')
s = '\n'.join(lines[2:]) if lines[0] == 'import os as _os' else src
REPL = [
 ("ROOT = _ROOT", "ROOT = subprocess.check_output(['git', 'rev-parse', '--show-toplevel'], text=True).strip()"),
 ("# DEUTERONOMY CHAPTER 7, THE READING (THE DEUTERONOMY WALK sitting 5, 2026-09-17; the owner: \"Go\") — THE FIRST",
  "# DEUTERONOMY CHAPTER 8, THE READING (THE DEUTERONOMY WALK sitting 6, 2026-09-18; the owner: \"Go\"; ONE RUN under the two-run rule) — THE FIRST"),
 ("# Chapter 6's form (ch6_dump0.py) derived by asserted substitutions (derive_ch7_dump0.py); section I (the spine ON the chapter) dropped — no piska\n# heads on chapter 7 (chapter 6's A print: the heads by chapter (6, 6), (11, 21)); the outside rows are the spine's whole contribution, as at chapter 4.",
  "# Chapter 7's form (ch7_dump0.py) derived by asserted substitutions (derive_ch8_dump0.py); section I (the spine ON the chapter) stays dropped — no piska\n# head on chapter 8 either (chapter 7's A print: 36 on 6:9, 37 on 11:10); the outside rows are the spine's whole contribution, as at chapters 4 and 7."),
 ("CH = 7\n", "CH = 8\n"),
 ("en_forms = re.compile(r'\\((?:Deut(?:eronomy)?\\.?|Dt\\.?|Devarim) ?(7):(\\d+)')", "en_forms = re.compile(r'\\((?:Deut(?:eronomy)?\\.?|Dt\\.?|Devarim) ?(8):(\\d+)')"),
 ("r'\\((?:Ibid|ibid)\\.? ?7:(\\d+)\\)'", "r'\\((?:Ibid|ibid)\\.? ?8:(\\d+)\\)'"),
 ("print('  EN \"ibid 7:n\" candidates:'", "print('  EN \"ibid 8:n\" candidates:'"),
 ("ch7_sifrei_outside.txt", "ch8_sifrei_outside.txt"),
 ("ch7_onkelos.txt", "ch8_onkelos.txt"),
 ("ch7_store_glosses.txt", "ch8_store_glosses.txt"),
 ("| {1, 26}):", "| {1, 20}):"),
 ("print('  dispositions naming Deut 7:', re.findall(r'^([^\\n]*Deut 7:[^\\n]*)$', RD, re.M)[:20])", "print('  dispositions naming Deut 8:', re.findall(r'^([^\\n]*Deut 8:[^\\n]*)$', RD, re.M)[:20])"),
 ("print('  REGISTER_INDEX lines on Deut 7:'); [print('   ', l[:220]) for l in RI.split('\\n') if re.search(r'Deut 7:', l)]", "print('  REGISTER_INDEX lines on Deut 8:'); [print('   ', l[:220]) for l in RI.split('\\n') if re.search(r'Deut 8:', l)]"),
 ("print('  ledgers with an Onkelos Deut 7 row:', sorted(f for f, t in LED.items() if re.search(r'^- Onkelos Deut 7:', t, re.M)))", "print('  ledgers with an Onkelos Deut 8 row:', sorted(f for f, t in LED.items() if re.search(r'^- Onkelos Deut 8:', t, re.M)))"),
 ("NAMING = sorted((f, len(re.findall(r'Deut(?:eronomy)? 7:\\d+', t)), sorted(set(re.findall(r'Deut(?:eronomy)? 7:\\d+(?:-\\d+)?', t)))[:14]) for f, t in LED.items() if re.search(r'Deut(?:eronomy)? 7:\\d+', t))\nprint('  ledgers NAMING a verse of Deut 7:'",
  "NAMING = sorted((f, len(re.findall(r'Deut(?:eronomy)? 8:\\d+', t)), sorted(set(re.findall(r'Deut(?:eronomy)? 8:\\d+(?:-\\d+)?', t)))[:14]) for f, t in LED.items() if re.search(r'Deut(?:eronomy)? 8:\\d+', t))\nprint('  ledgers NAMING a verse of Deut 8:'"),
 ("print('  ledgers with an Onkelos Exod 23 or 34 row (the kin\\'s reading — the angel\\'s covenant clauses 23:20-33, the renewed covenant 34:11-16):', sorted(f for f, t in LED.items() if re.search(r'^- Onkelos Exod (23|34):', t, re.M)), '| Mekhilta rows on Exod 23/34 anywhere:', sum(len(re.findall(r'Mekhilta[^\\n]{0,40}(?:23|34):\\d+', t)) for t in LED.values()), '| ledgers with an Onkelos Num 33 row (33:50-56 the dispossession):', sorted(f for f, t in LED.items() if re.search(r'^- Onkelos Num 33:', t, re.M)))",
  "print('  ledgers with an Onkelos Exod 16 or 17 row (the kin\\'s reading — the manna 16:1-36, the water from the rock 17:1-7):', sorted(f for f, t in LED.items() if re.search(r'^- Onkelos Exod (16|17):', t, re.M)), '| Mekhilta rows on Exod 16/17 anywhere:', sum(len(re.findall(r'Mekhilta[^\\n]{0,40}(?:16|17):\\d+', t)) for t in LED.values()), '| ledgers with an Onkelos Num 11, 14, 20 or 21 row (the craving 11:4-9, the forty years 14:33-34, Meribah 20:1-13, the serpents 21:4-9):', sorted(f for f, t in LED.items() if re.search(r'^- Onkelos Num (11|14|20|21):', t, re.M)))"),
 ("glob.glob(f'{ROOT}/logic/units/deu_0[6-8]*.yaml')", "glob.glob(f'{ROOT}/logic/units/deu_0[7-9]*.yaml')"),
 ("    if uid.startswith('deu_07'): print(", "    if uid.startswith('deu_08'): print("),
 ("for p in ('DV07', 'DV07A', 'DV07B', 'DV06', 'DV08')})", "for p in ('DV08', 'DV08A', 'DV08B', 'DV07', 'DV09')})"),
 ("print('  existing manifests deu_07*:', sorted(os.path.basename(f) for f in glob.glob(f'{ROOT}/logic/oral_audit/manifests/deu_07*'))", "print('  existing manifests deu_08*:', sorted(os.path.basename(f) for f in glob.glob(f'{ROOT}/logic/oral_audit/manifests/deu_08*'))"),
 ("print('  overrides already for Deut.7:', re.findall(r'\"Deut\\.7\\.[^\"]+\": \"[^\"]+\"', OV)[:20], '| by_ref last Deut.6 line:', [l for l in OV.split('\\n') if l.startswith('  \"Deut.6.')][-1:])",
  "print('  overrides already for Deut.8:', re.findall(r'\"Deut\\.8\\.[^\"]+\": \"[^\"]+\"', OV)[:20], '| by_ref last Deut.7 line:', [l for l in OV.split('\\n') if l.startswith('  \"Deut.7.')][-1:])"),
]
for old, new in REPL:
    n = s.count(old); assert n >= 1 or old == 'ROOT = _ROOT', ('ABSENT', old[:90]); s = s.replace(old, new)
assert 'ch7_' not in s.replace('ch7_dump0.py', '') and 'Deut 7:' not in s and "Deut.7." not in s.replace('"Deut.7.', ''), [m for m in re.findall(r'.{30}(?:ch7_|Deut 7:).{30}', s)]
open(f'{SP}/ch8_dump0.py', 'w', encoding='utf-8').write(s)
print('derived ch8_dump0.py', len(s), 'bytes;', len(REPL), 'substitutions')
