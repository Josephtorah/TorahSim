import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE DEUTERONOMY WALK sitting 8 — CHAPTER 10's READING, ONE RUN under THE TWO-RUN RULE (2026-09-19; the owner: "Go"): ch10_dump0.py DERIVED from the
# forms' ch9_dump0.py by asserted substitutions (derive_ch9_dump0.py's form): the chapter number, the file names, the register and prior-read greps, the kin
# chapters (Exodus 25, 34 and 37 — the ark and the second tablets, where chapter 10's retold acts have their first tellings; Numbers 3, 8, 18, 20, 33 the
# Levites, Aaron's death, the journeys), the drafts by glob; SECTION I stays dropped — no piska head on chapter 10 (the A print: 36 on 6:9, 37 on 11:10);
# the forms' portable header turned back to the git root for a scratch run.
import os, re, subprocess
ROOT = _ROOT
SP = os.path.dirname(os.path.abspath(__file__))
src = open(f'{ROOT}/World/step9/forms_deuteronomy_walk/ch9_dump0.py', encoding='utf-8').read()
lines = src.split('\n')
s = '\n'.join(lines[2:]) if lines[0] == 'import os as _os' else src
REPL = [
 ("ROOT = _ROOT", "ROOT = _ROOT"),
 ("# DEUTERONOMY CHAPTER 9, THE READING (THE DEUTERONOMY WALK sitting 7, 2026-09-19; the owner: \"do another section\"; ONE RUN under the two-run rule) — THE FIRST",
  "# DEUTERONOMY CHAPTER 10, THE READING (THE DEUTERONOMY WALK sitting 8, 2026-09-19; the owner: \"Go\"; ONE RUN under the two-run rule) — THE FIRST"),
 ("# Chapter 8's form (ch8_dump0.py) derived by asserted substitutions (derive_ch9_dump0.py); section I (the spine ON the chapter) stays dropped — no piska\n# head on chapter 9 either (the A print: 36 on 6:9, 37 on 11:10); the outside rows are the spine's whole contribution, as at chapters 4, 7 and 8.",
  "# Chapter 9's form (ch9_dump0.py) derived by asserted substitutions (derive_ch10_dump0.py); section I (the spine ON the chapter) stays dropped — no piska\n# head on chapter 10 either (the A print: 36 on 6:9, 37 on 11:10); the outside rows are the spine's whole contribution, as at chapters 4, 7, 8 and 9."),
 ("CH = 9\n", "CH = 10\n"),
 ("chapters 1-9:', [(c, len(onk_he[c - 1]), VC[c]) for c in range(1, 10)", "chapters 1-10:', [(c, len(onk_he[c - 1]), VC[c]) for c in range(1, 11)"),
 ("'| heads by chapter 1-9:', sorted(Counter(h[0] for h in heads.values() if h).items())[:9])", "'| heads by chapter 1-10:', sorted(Counter(h[0] for h in heads.values() if h).items())[:10])"),
 ("en_forms = re.compile(r'\\((?:Deut(?:eronomy)?\\.?|Dt\\.?|Devarim) ?(9):(\\d+)')", "en_forms = re.compile(r'\\((?:Deut(?:eronomy)?\\.?|Dt\\.?|Devarim) ?(10):(\\d+)')"),
 ("r'\\((?:Ibid|ibid)\\.? ?9:(\\d+)\\)'", "r'\\((?:Ibid|ibid)\\.? ?10:(\\d+)\\)'"),
 ("print('  EN \"ibid 9:n\" candidates:'", "print('  EN \"ibid 10:n\" candidates:'"),
 ("ch9_sifrei_outside.txt", "ch10_sifrei_outside.txt"),
 ("ch9_onkelos.txt", "ch10_onkelos.txt"),
 ("ch9_store_glosses.txt", "ch10_store_glosses.txt"),
 ("| {1, 29}):", "| {1, 22}):"),
 ("print('  dispositions naming Deut 9:', re.findall(r'^([^\\n]*Deut 9:[^\\n]*)$', RD, re.M)[:20])", "print('  dispositions naming Deut 10:', re.findall(r'^([^\\n]*Deut 10:[^\\n]*)$', RD, re.M)[:20])"),
 ("print('  REGISTER_INDEX lines on Deut 9:'); [print('   ', l[:220]) for l in RI.split('\\n') if re.search(r'Deut 9:', l)]", "print('  REGISTER_INDEX lines on Deut 10:'); [print('   ', l[:220]) for l in RI.split('\\n') if re.search(r'Deut 10:', l)]"),
 ("print('  ledgers with an Onkelos Deut 9 row:', sorted(f for f, t in LED.items() if re.search(r'^- Onkelos Deut 9:', t, re.M)))", "print('  ledgers with an Onkelos Deut 10 row:', sorted(f for f, t in LED.items() if re.search(r'^- Onkelos Deut 10:', t, re.M)))"),
 ("NAMING = sorted((f, len(re.findall(r'Deut(?:eronomy)? 9:\\d+', t)), sorted(set(re.findall(r'Deut(?:eronomy)? 9:\\d+(?:-\\d+)?', t)))[:14]) for f, t in LED.items() if re.search(r'Deut(?:eronomy)? 9:\\d+', t))\nprint('  ledgers NAMING a verse of Deut 9:'",
  "NAMING = sorted((f, len(re.findall(r'Deut(?:eronomy)? 10:\\d+', t)), sorted(set(re.findall(r'Deut(?:eronomy)? 10:\\d+(?:-\\d+)?', t)))[:14]) for f, t in LED.items() if re.search(r'Deut(?:eronomy)? 10:\\d+', t))\nprint('  ledgers NAMING a verse of Deut 10:'"),
 ("print('  ledgers with an Onkelos Exod 24 or 32 row (the kin\\'s reading — the forty days 24:12-18, the calf 32:1-35):', sorted(f for f, t in LED.items() if re.search(r'^- Onkelos Exod (24|32):', t, re.M)), '| Mekhilta rows on Exod 16/17 anywhere:', sum(len(re.findall(r'Mekhilta[^\\n]{0,40}(?:16|17):\\d+', t)) for t in LED.values()), '| ledgers with an Onkelos Num 11, 14, 20 or 21 row (the craving 11:4-9, the forty years 14:33-34, Meribah 20:1-13, the serpents 21:4-9):', sorted(f for f, t in LED.items() if re.search(r'^- Onkelos Num (11|14|20|21):', t, re.M)))",
  "print('  ledgers with an Onkelos Exod 25, 34 or 37 row (the kin\\'s reading — the ark 25:10-22, the second tablets 34:1-4 and 28-29, the ark made 37:1-9):', sorted(f for f, t in LED.items() if re.search(r'^- Onkelos Exod (25|34|37):', t, re.M)), '| Tanchuma rows on Exod 25/34/37 anywhere:', sum(len(re.findall(r'Tanchuma[^\\n]{0,40}(?:25|34|37):\\d+', t)) for t in LED.values()), '| ledgers with an Onkelos Num 3, 8, 18, 20 or 33 row (the Levites 3:5-13, 8:5-26, 18:20-24; Aaron\\'s death 20:22-29; the journeys 33:30-39):', sorted(f for f, t in LED.items() if re.search(r'^- Onkelos Num (3|8|18|20|33):', t, re.M)))"),
 ("glob.glob(f'{ROOT}/logic/units/deu_0[8-9]*.yaml')", "glob.glob(f'{ROOT}/logic/units/deu_09*.yaml') + glob.glob(f'{ROOT}/logic/units/deu_10*.yaml')"),
 ("    if uid.startswith('deu_09'): print(", "    if uid.startswith('deu_10'): print("),
 ("for p in ('DV09', 'DV09A', 'DV09B', 'DV08', 'DV10')})", "for p in ('DV10', 'DV10A', 'DV10B', 'DV09', 'DV11')})"),
 ("print('  existing manifests deu_09*:', sorted(os.path.basename(f) for f in glob.glob(f'{ROOT}/logic/oral_audit/manifests/deu_09*'))", "print('  existing manifests deu_10*:', sorted(os.path.basename(f) for f in glob.glob(f'{ROOT}/logic/oral_audit/manifests/deu_10*'))"),
 ("print('  overrides already for Deut.9:', re.findall(r'\"Deut\\.9\\.[^\"]+\": \"[^\"]+\"', OV)[:20], '| by_ref last Deut.8 line:', [l for l in OV.split('\\n') if l.startswith('  \"Deut.8.')][-1:])",
  "print('  overrides already for Deut.10:', re.findall(r'\"Deut\\.10\\.[^\"]+\": \"[^\"]+\"', OV)[:20], '| by_ref last Deut.9 line:', [l for l in OV.split('\\n') if l.startswith('  \"Deut.9.')][-1:])"),
]
for old, new in REPL:
    n = s.count(old); assert n >= 1, ('ABSENT', old[:90]); s = s.replace(old, new)
left = [m for m in re.findall(r'.{30}(?:ch9_|Deut 9:|Deut\.9\.|Exod \(24\|32\)).{30}', s.replace('ch9_dump0.py', ''))]
left += [m for m in re.findall(r'.{30}deu_09.{30}', s) if 'glob' not in m]
assert not left, left
open(f'{SP}/ch10_dump0.py', 'w', encoding='utf-8').write(s)
print('derived ch10_dump0.py', len(s), 'bytes;', len(REPL), 'substitutions')
