#!/usr/bin/env python3
# THE DEUTERONOMY WALK sitting 5 — CHAPTER 7's READING, RUN 1 (2026-09-17; the owner: "Go"): ch7_dump0.py DERIVED from the forms' ch6_dump0.py by
# asserted substitutions (the four-run rule's economy on our own text): the chapter number, the file names, the register and prior-read greps,
# the kin chapters (Exodus 23:20-33 and 34:11-16 — the angel's covenant clauses and the renewed covenant's, where chapter 7's ban, altars and
# marriages have their first tellings), the drafts by glob; SECTION I (the spine ON the chapter) DROPPED — no piska heads on chapter 7 (typed from
# chapter 6's A print: heads by chapter (6, 6), (11, 21)); the forms' portable header turned back to the git root for a scratch run.
import os, re, subprocess
ROOT = subprocess.check_output(['git', 'rev-parse', '--show-toplevel'], text=True).strip()
SP = os.path.dirname(os.path.abspath(__file__))
src = open(f'{ROOT}/World/step9/forms_deuteronomy_walk/ch6_dump0.py', encoding='utf-8').read()
lines = src.split('\n')
s = '\n'.join(lines[2:]) if lines[0] == 'import os as _os' else src   # the forms copy of ch6_dump0.py kept the git-root line (no portable header)
REPL = [
 ("ROOT = _ROOT", "ROOT = subprocess.check_output(['git', 'rev-parse', '--show-toplevel'], text=True).strip()"),
 ("# DEUTERONOMY CHAPTER 6, THE READING (THE DEUTERONOMY WALK sitting 4, 2026-09-17; the owner: \"ok lets start the next chapter\") — THE FIRST",
  "# DEUTERONOMY CHAPTER 7, THE READING (THE DEUTERONOMY WALK sitting 5, 2026-09-17; the owner: \"Go\") — THE FIRST"),
 ("# Chapter 4's form (ch4_dump0.py) edited for the chapter; the alignment section new.",
  "# Chapter 6's form (ch6_dump0.py) derived by asserted substitutions (derive_ch7_dump0.py); section I (the spine ON the chapter) dropped — no piska\n# heads on chapter 7 (chapter 6's A print: the heads by chapter (6, 6), (11, 21)); the outside rows are the spine's whole contribution, as at chapter 4."),
 ("CH = 6\n", "CH = 7\n"),
 ("print('  heads 28-34 (HE first citation | rows | EN first quote):')\nfor p in range(30, 38):", "print('  heads 34-39 (HE first citation | rows | EN first quote):')\nfor p in range(34, 40):"),
 ("en_forms = re.compile(r'\\((?:Deut(?:eronomy)?\\.?|Dt\\.?|Devarim) ?(6):(\\d+)')", "en_forms = re.compile(r'\\((?:Deut(?:eronomy)?\\.?|Dt\\.?|Devarim) ?(7):(\\d+)')"),
 ("r'\\((?:Ibid|ibid)\\.? ?5:(\\d+)\\)'", "r'\\((?:Ibid|ibid)\\.? ?7:(\\d+)\\)'"),
 ("print('  EN \"ibid 5:n\" candidates:'", "print('  EN \"ibid 7:n\" candidates:'"),
 ("ch6_sifrei_outside.txt", "ch7_sifrei_outside.txt"),
 ("ch6_onkelos.txt", "ch7_onkelos.txt"),
 ("ch6_store_glosses.txt", "ch7_store_glosses.txt"),
 ("| {1, 4, 20, 25}):", "| {1, 26}):"),
 ("print('  dispositions naming Deut 6:', re.findall(r'^([^\\n]*Deut 6:[^\\n]*)$', RD, re.M)[:20])", "print('  dispositions naming Deut 7:', re.findall(r'^([^\\n]*Deut 7:[^\\n]*)$', RD, re.M)[:20])"),
 ("print('  REGISTER_INDEX lines on Deut 6:'); [print('   ', l[:220]) for l in RI.split('\\n') if re.search(r'Deut 6:', l)]", "print('  REGISTER_INDEX lines on Deut 7:'); [print('   ', l[:220]) for l in RI.split('\\n') if re.search(r'Deut 7:', l)]"),
 ("print('  ledgers with an Onkelos Deut 6 row:', sorted(f for f, t in LED.items() if re.search(r'^- Onkelos Deut 6:', t, re.M)))", "print('  ledgers with an Onkelos Deut 7 row:', sorted(f for f, t in LED.items() if re.search(r'^- Onkelos Deut 7:', t, re.M)))"),
 ("NAMING = sorted((f, len(re.findall(r'Deut(?:eronomy)? 6:\\d+', t)), sorted(set(re.findall(r'Deut(?:eronomy)? 6:\\d+(?:-\\d+)?', t)))[:14]) for f, t in LED.items() if re.search(r'Deut(?:eronomy)? 6:\\d+', t))\nprint('  ledgers NAMING a verse of Deut 6:'",
  "NAMING = sorted((f, len(re.findall(r'Deut(?:eronomy)? 7:\\d+', t)), sorted(set(re.findall(r'Deut(?:eronomy)? 7:\\d+(?:-\\d+)?', t)))[:14]) for f, t in LED.items() if re.search(r'Deut(?:eronomy)? 7:\\d+', t))\nprint('  ledgers NAMING a verse of Deut 7:'"),
 ("print('  ledgers with an Onkelos Exod 13 row (the kin\\'s reading — the frontlets and the son\\'s question, Exodus 13:1-16):', sorted(f for f, t in LED.items() if re.search(r'^- Onkelos Exod 13:', t, re.M)), '| Mekhilta rows on Exod 13 anywhere:', sum(len(re.findall(r'Mekhilta[^\\n]{0,40}13:\\d+', t)) for t in LED.values()))",
  "print('  ledgers with an Onkelos Exod 23 or 34 row (the kin\\'s reading — the angel\\'s covenant clauses 23:20-33, the renewed covenant 34:11-16):', sorted(f for f, t in LED.items() if re.search(r'^- Onkelos Exod (23|34):', t, re.M)), '| Mekhilta rows on Exod 23/34 anywhere:', sum(len(re.findall(r'Mekhilta[^\\n]{0,40}(?:23|34):\\d+', t)) for t in LED.values()), '| ledgers with an Onkelos Num 33 row (33:50-56 the dispossession):', sorted(f for f, t in LED.items() if re.search(r'^- Onkelos Num 33:', t, re.M)))"),
 ("for uid in ('deu_05_decalogue', 'deu_06_shema', 'deu_07_nations_cherem'):", "for uid in sorted(os.path.basename(f)[:-5] for f in glob.glob(f'{ROOT}/logic/units/deu_0[6-8]*.yaml')):"),
 ("    if uid == 'deu_06_shema': print(", "    if uid.startswith('deu_07'): print("),
 ("for p in ('DV06A', 'DV05B', 'DV05', 'DV04B')})", "for p in ('DV07', 'DV07A', 'DV07B', 'DV06', 'DV08')})"),
 ("print('  existing manifests deu_06*:', sorted(os.path.basename(f) for f in glob.glob(f'{ROOT}/logic/oral_audit/manifests/deu_06*'))", "print('  existing manifests deu_07*:', sorted(os.path.basename(f) for f in glob.glob(f'{ROOT}/logic/oral_audit/manifests/deu_07*'))"),
 ("print('  overrides already for Deut.6:', re.findall(r'\"Deut\\.6\\.[^\"]+\": \"[^\"]+\"', OV)[:20], '| by_ref last Deut.5 line:', [l for l in OV.split('\\n') if l.startswith('  \"Deut.5.')][-1:])",
  "print('  overrides already for Deut.7:', re.findall(r'\"Deut\\.7\\.[^\"]+\": \"[^\"]+\"', OV)[:20], '| by_ref last Deut.6 line:', [l for l in OV.split('\\n') if l.startswith('  \"Deut.6.')][-1:])"),
]
for old, new in REPL:
    n = s.count(old); assert n >= 1 or old == 'ROOT = _ROOT', ('ABSENT', old[:90]); s = s.replace(old, new)
i = s.index("print('==== I. THE SPINE ON THE CHAPTER")
s = s[:i] + "print('==== I. THE SPINE ON THE CHAPTER — none: no piska head in chapter', CH, '(the heads by chapter above); the outside rows are the spine here')\nprint('  the heads whose chapter is', CH, ':', [(p, h) for p, h in heads.items() if h and h[0] == CH], '| the nearest heads:', {p: heads[p] for p in (36, 37)})\n"
assert 'ch6_' not in s.replace('ch6_dump0.py', '') and 'Deut 6:' not in s and "Deut.6." not in s.replace('"Deut.6.', ''), [m for m in re.findall(r'.{30}(?:ch6_|Deut 6:).{30}', s)]
open(f'{SP}/ch7_dump0.py', 'w', encoding='utf-8').write(s)
print('derived ch7_dump0.py', len(s), 'bytes;', len(REPL), 'substitutions; section I replaced')
