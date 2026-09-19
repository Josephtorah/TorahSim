import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE DEUTERONOMY WALK sitting 7 — CHAPTER 9's READING, ONE RUN under THE TWO-RUN RULE (2026-09-19; the owner: "Let's keep run as it is and do another
# section"): ch9_dump0.py DERIVED from the forms' ch8_dump0.py by asserted substitutions (derive_ch8_dump0.py's form): the chapter number, the file
# names, the register and prior-read greps, the kin chapters (Exodus 24 and 32 — the forty days and the calf, where chapter 9's retold acts have their
# first tellings; Numbers 11, 13-14 the fire, the craving, the spies), the drafts by glob; SECTION I stays dropped — no piska head on chapter 9 (the A
# print: 36 on 6:9, 37 on 11:10); the forms' portable header (if any) turned back to the git root for a scratch run.
import os, re, subprocess
ROOT = _ROOT
SP = os.path.dirname(os.path.abspath(__file__))
src = open(f'{ROOT}/World/step9/forms_deuteronomy_walk/ch8_dump0.py', encoding='utf-8').read()
lines = src.split('\n')
s = '\n'.join(lines[2:]) if lines[0] == 'import os as _os' else src
REPL = [
 ("ROOT = _ROOT", "ROOT = _ROOT"),
 ("# DEUTERONOMY CHAPTER 8, THE READING (THE DEUTERONOMY WALK sitting 6, 2026-09-18; the owner: \"Go\"; ONE RUN under the two-run rule) — THE FIRST",
  "# DEUTERONOMY CHAPTER 9, THE READING (THE DEUTERONOMY WALK sitting 7, 2026-09-19; the owner: \"do another section\"; ONE RUN under the two-run rule) — THE FIRST"),
 ("# Chapter 7's form (ch7_dump0.py) derived by asserted substitutions (derive_ch8_dump0.py); section I (the spine ON the chapter) stays dropped — no piska\n# head on chapter 8 either (chapter 7's A print: 36 on 6:9, 37 on 11:10); the outside rows are the spine's whole contribution, as at chapters 4 and 7.",
  "# Chapter 8's form (ch8_dump0.py) derived by asserted substitutions (derive_ch9_dump0.py); section I (the spine ON the chapter) stays dropped — no piska\n# head on chapter 9 either (the A print: 36 on 6:9, 37 on 11:10); the outside rows are the spine's whole contribution, as at chapters 4, 7 and 8."),
 ("CH = 8\n", "CH = 9\n"),
 ("chapters 1-8:', [(c, len(onk_he[c - 1]), VC[c]) for c in range(1, 9)", "chapters 1-9:', [(c, len(onk_he[c - 1]), VC[c]) for c in range(1, 10)"),
 ("'| heads by chapter 1-8:', sorted(Counter(h[0] for h in heads.values() if h).items())[:8])", "'| heads by chapter 1-9:', sorted(Counter(h[0] for h in heads.values() if h).items())[:9])"),
 ("en_forms = re.compile(r'\\((?:Deut(?:eronomy)?\\.?|Dt\\.?|Devarim) ?(8):(\\d+)')", "en_forms = re.compile(r'\\((?:Deut(?:eronomy)?\\.?|Dt\\.?|Devarim) ?(9):(\\d+)')"),
 ("r'\\((?:Ibid|ibid)\\.? ?8:(\\d+)\\)'", "r'\\((?:Ibid|ibid)\\.? ?9:(\\d+)\\)'"),
 ("print('  EN \"ibid 8:n\" candidates:'", "print('  EN \"ibid 9:n\" candidates:'"),
 ("ch8_sifrei_outside.txt", "ch9_sifrei_outside.txt"),
 ("ch8_onkelos.txt", "ch9_onkelos.txt"),
 ("ch8_store_glosses.txt", "ch9_store_glosses.txt"),
 ("| {1, 20}):", "| {1, 29}):"),
 ("print('  dispositions naming Deut 8:', re.findall(r'^([^\\n]*Deut 8:[^\\n]*)$', RD, re.M)[:20])", "print('  dispositions naming Deut 9:', re.findall(r'^([^\\n]*Deut 9:[^\\n]*)$', RD, re.M)[:20])"),
 ("print('  REGISTER_INDEX lines on Deut 8:'); [print('   ', l[:220]) for l in RI.split('\\n') if re.search(r'Deut 8:', l)]", "print('  REGISTER_INDEX lines on Deut 9:'); [print('   ', l[:220]) for l in RI.split('\\n') if re.search(r'Deut 9:', l)]"),
 ("print('  ledgers with an Onkelos Deut 8 row:', sorted(f for f, t in LED.items() if re.search(r'^- Onkelos Deut 8:', t, re.M)))", "print('  ledgers with an Onkelos Deut 9 row:', sorted(f for f, t in LED.items() if re.search(r'^- Onkelos Deut 9:', t, re.M)))"),
 ("NAMING = sorted((f, len(re.findall(r'Deut(?:eronomy)? 8:\\d+', t)), sorted(set(re.findall(r'Deut(?:eronomy)? 8:\\d+(?:-\\d+)?', t)))[:14]) for f, t in LED.items() if re.search(r'Deut(?:eronomy)? 8:\\d+', t))\nprint('  ledgers NAMING a verse of Deut 8:'",
  "NAMING = sorted((f, len(re.findall(r'Deut(?:eronomy)? 9:\\d+', t)), sorted(set(re.findall(r'Deut(?:eronomy)? 9:\\d+(?:-\\d+)?', t)))[:14]) for f, t in LED.items() if re.search(r'Deut(?:eronomy)? 9:\\d+', t))\nprint('  ledgers NAMING a verse of Deut 9:'"),
 ("print('  ledgers with an Onkelos Exod 16 or 17 row (the kin\\'s reading — the manna 16:1-36, the water from the rock 17:1-7):', sorted(f for f, t in LED.items() if re.search(r'^- Onkelos Exod (16|17):', t, re.M)),",
  "print('  ledgers with an Onkelos Exod 24 or 32 row (the kin\\'s reading — the forty days 24:12-18, the calf 32:1-35):', sorted(f for f, t in LED.items() if re.search(r'^- Onkelos Exod (24|32):', t, re.M)),"),
 ("glob.glob(f'{ROOT}/logic/units/deu_0[7-9]*.yaml')", "glob.glob(f'{ROOT}/logic/units/deu_0[8-9]*.yaml')"),
 ("    if uid.startswith('deu_08'): print(", "    if uid.startswith('deu_09'): print("),
 ("for p in ('DV08', 'DV08A', 'DV08B', 'DV07', 'DV09')})", "for p in ('DV09', 'DV09A', 'DV09B', 'DV08', 'DV10')})"),
 ("print('  existing manifests deu_08*:', sorted(os.path.basename(f) for f in glob.glob(f'{ROOT}/logic/oral_audit/manifests/deu_08*'))", "print('  existing manifests deu_09*:', sorted(os.path.basename(f) for f in glob.glob(f'{ROOT}/logic/oral_audit/manifests/deu_09*'))"),
 ("print('  overrides already for Deut.8:', re.findall(r'\"Deut\\.8\\.[^\"]+\": \"[^\"]+\"', OV)[:20], '| by_ref last Deut.7 line:', [l for l in OV.split('\\n') if l.startswith('  \"Deut.7.')][-1:])",
  "print('  overrides already for Deut.9:', re.findall(r'\"Deut\\.9\\.[^\"]+\": \"[^\"]+\"', OV)[:20], '| by_ref last Deut.8 line:', [l for l in OV.split('\\n') if l.startswith('  \"Deut.8.')][-1:])"),
]
for old, new in REPL:
    n = s.count(old); assert n >= 1 or old == 'ROOT = _ROOT', ('ABSENT', old[:90]); s = s.replace(old, new)
left = [m for m in re.findall(r'.{30}(?:ch8_|Deut 8:|Deut\.8\.|deu_08|Exod \(16\|17\)).{30}', s.replace('ch8_dump0.py', ''))]
assert not left, left
open(f'{SP}/ch9_dump0.py', 'w', encoding='utf-8').write(s)
print('derived ch9_dump0.py', len(s), 'bytes;', len(REPL), 'substitutions')
