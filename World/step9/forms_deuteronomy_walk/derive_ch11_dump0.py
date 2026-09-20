import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE DEUTERONOMY WALK sitting 9 — CHAPTER 11's READING, ONE RUN under THE TWO-RUN RULE (2026-09-20; the owner: "Go" after the reread that followed 8b's
# compaction — not a commit word, the commit still pending): ch11_dump0.py DERIVED from the forms' ch10_dump0.py by asserted substitutions
# (derive_ch10_dump0.py's form): the chapter number, the file names, the register and prior-read greps, the kin chapters (Exodus 14 the sea for 11:4, Exodus 23
# the dread and the borders for 11:24-25, Numbers 16 Dathan and Abiram for 11:6, Genesis 15 the borders' oath, Deuteronomy 6 the Shema's first paragraph
# beside 11:13-21's second), the drafts by glob; SECTION I RETURNS in chapter 6's form (ch6_dump0.py's) — THE SPINE IS ON THE CHAPTER for the first time
# since chapter 6 (sitting 8's A print: 37-38 head on 11:10, 39 on 11:11; twenty-one heads in chapter 11): the SPINE computed from the heads, never typed,
# the outside rows the union less the spine's own piskaot; the forms' portable header turned back to the git root for a scratch run.
import os, re, subprocess
ROOT = _ROOT
SP = os.path.dirname(os.path.abspath(__file__))
src = open(f'{ROOT}/World/step9/forms_deuteronomy_walk/ch10_dump0.py', encoding='utf-8').read()
lines = src.split('\n')
s = '\n'.join(lines[2:]) if lines[0] == 'import os as _os' else src
REPL = [
 ("ROOT = _ROOT", "ROOT = _ROOT"),
 ("# DEUTERONOMY CHAPTER 10, THE READING (THE DEUTERONOMY WALK sitting 8, 2026-09-19; the owner: \"Go\"; ONE RUN under the two-run rule) — THE FIRST",
  "# DEUTERONOMY CHAPTER 11, THE READING (THE DEUTERONOMY WALK sitting 9, 2026-09-20; the owner: \"Go\"; ONE RUN under the two-run rule) — THE FIRST"),
 ("# Chapter 9's form (ch9_dump0.py) derived by asserted substitutions (derive_ch10_dump0.py); section I (the spine ON the chapter) stays dropped — no piska\n# head on chapter 10 either (the A print: 36 on 6:9, 37 on 11:10); the outside rows are the spine's whole contribution, as at chapters 4, 7, 8 and 9.",
  "# Chapter 10's form (ch10_dump0.py) derived by asserted substitutions (derive_ch11_dump0.py); SECTION I RETURNS in chapter 6's form — THE SPINE IS ON THE\n# CHAPTER (sitting 8's A print: 37-38 on 11:10, 39 on 11:11; twenty-one heads in chapter 11): the SPINE computed from the heads, the outside rows the union\n# less the spine's own piskaot; the portion's edge inside the chapter (Ekev to 11:25, Re'eh from 11:26 — the chapter the unit, per the ruling CHAPTER NUMBERS)."),
 ("CH = 10\n", "CH = 11\n"),
 ("chapters 1-10:', [(c, len(onk_he[c - 1]), VC[c]) for c in range(1, 11)", "chapters 1-11:', [(c, len(onk_he[c - 1]), VC[c]) for c in range(1, 12)"),
 ("print('  heads 34-39 (HE first citation | rows | EN first quote):')\nfor p in range(34, 40):", "print('  heads 36-59 (HE first citation | rows | EN first quote):')\nfor p in range(36, 60):"),
 ("'| heads by chapter 1-10:', sorted(Counter(h[0] for h in heads.values() if h).items())[:10])", "'| heads by chapter 1-11:', sorted(Counter(h[0] for h in heads.values() if h).items())[:11])"),
 ("en_forms = re.compile(r'\\((?:Deut(?:eronomy)?\\.?|Dt\\.?|Devarim) ?(10):(\\d+)')", "en_forms = re.compile(r'\\((?:Deut(?:eronomy)?\\.?|Dt\\.?|Devarim) ?(11):(\\d+)')"),
 ("r'\\((?:Ibid|ibid)\\.? ?10:(\\d+)\\)'", "r'\\((?:Ibid|ibid)\\.? ?11:(\\d+)\\)'"),
 ("print('  EN \"ibid 10:n\" candidates:'", "print('  EN \"ibid 11:n\" candidates:'"),
 ("allrows = sorted(set((p, r) for p, r, _ in outside_he) | set((p, r) for p, r, _ in outside_en))\nprint('  the union of rows (both files):', len(allrows), allrows)\n",
  "allrows = sorted(set((p, r) for p, r, _ in outside_he) | set((p, r) for p, r, _ in outside_en))\nprint('  the union of rows (both files):', len(allrows), allrows)\n"
  "SPINE = sorted(p for p, h in heads.items() if h and h[0] == CH)   # COMPUTED from the heads, never typed (chapter 6 typed its six from the print)\n"
  "OUTSIDE = [(p, r) for p, r in allrows if p not in SPINE]\n"
  "print('  the rows OUTSIDE the spine piskaot (the union less the on-chapter piskaot', SPINE[0], '-', SPINE[-1], '):', len(OUTSIDE), OUTSIDE, '| in-spine rows of the union:', len(allrows) - len(OUTSIDE))\n"),
 ("    for p, r in allrows:\n        f.write(f'\\n## Sifrei", "    for p, r in OUTSIDE:\n        f.write(f'\\n## Sifrei"),
 ("ch10_sifrei_outside.txt", "ch11_sifrei_outside.txt"),
 ("ch10_onkelos.txt", "ch11_onkelos.txt"),
 ("ch10_store_glosses.txt", "ch11_store_glosses.txt"),
 ("| {1, 22}):", "| {1, 32}):"),
 ("print('  dispositions naming Deut 10:', re.findall(r'^([^\\n]*Deut 10:[^\\n]*)$', RD, re.M)[:20])", "print('  dispositions naming Deut 11:', re.findall(r'^([^\\n]*Deut 11:[^\\n]*)$', RD, re.M)[:20])"),
 ("print('  REGISTER_INDEX lines on Deut 10:'); [print('   ', l[:220]) for l in RI.split('\\n') if re.search(r'Deut 10:', l)]", "print('  REGISTER_INDEX lines on Deut 11:'); [print('   ', l[:220]) for l in RI.split('\\n') if re.search(r'Deut 11:', l)]"),
 ("print('  ledgers with an Onkelos Deut 10 row:', sorted(f for f, t in LED.items() if re.search(r'^- Onkelos Deut 10:', t, re.M)))", "print('  ledgers with an Onkelos Deut 11 row:', sorted(f for f, t in LED.items() if re.search(r'^- Onkelos Deut 11:', t, re.M)))"),
 ("NAMING = sorted((f, len(re.findall(r'Deut(?:eronomy)? 10:\\d+', t)), sorted(set(re.findall(r'Deut(?:eronomy)? 10:\\d+(?:-\\d+)?', t)))[:14]) for f, t in LED.items() if re.search(r'Deut(?:eronomy)? 10:\\d+', t))\nprint('  ledgers NAMING a verse of Deut 10:'",
  "NAMING = sorted((f, len(re.findall(r'Deut(?:eronomy)? 11:\\d+', t)), sorted(set(re.findall(r'Deut(?:eronomy)? 11:\\d+(?:-\\d+)?', t)))[:14]) for f, t in LED.items() if re.search(r'Deut(?:eronomy)? 11:\\d+', t))\nprint('  ledgers NAMING a verse of Deut 11:'"),
 ("print('  ledgers with an Onkelos Exod 25, 34 or 37 row (the kin\\'s reading — the ark 25:10-22, the second tablets 34:1-4 and 28-29, the ark made 37:1-9):', sorted(f for f, t in LED.items() if re.search(r'^- Onkelos Exod (25|34|37):', t, re.M)), '| Tanchuma rows on Exod 25/34/37 anywhere:', sum(len(re.findall(r'Tanchuma[^\\n]{0,40}(?:25|34|37):\\d+', t)) for t in LED.values()), '| ledgers with an Onkelos Num 3, 8, 18, 20 or 33 row (the Levites 3:5-13, 8:5-26, 18:20-24; Aaron\\'s death 20:22-29; the journeys 33:30-39):', sorted(f for f, t in LED.items() if re.search(r'^- Onkelos Num (3|8|18|20|33):', t, re.M)))",
  "print('  ledgers with an Onkelos Exod 14 or 23 row (the kin\\'s reading — the sea 14:21-31 for 11:4, the dread and the borders 23:27-31 for 11:24-25):', sorted(f for f, t in LED.items() if re.search(r'^- Onkelos Exod (14|23):', t, re.M)), '| Mekhilta rows on Exod 14/23 anywhere:', sum(len(re.findall(r'Mekhilta[^\\n]{0,40}(?:14|23):\\d+', t)) for t in LED.values()), '| ledgers with an Onkelos Num 16 row (Dathan and Abiram 16:25-34 for 11:6) or a Gen 15 row (the borders sworn 15:18 for 11:24):', sorted(f for f, t in LED.items() if re.search(r'^- Onkelos (?:Num 16|Gen 15):', t, re.M)), '| ledgers with an Onkelos Deut 6 row (the Shema\\'s first paragraph — 11:13-21 its second):', sorted(f for f, t in LED.items() if re.search(r'^- Onkelos Deut 6:', t, re.M)))"),
 ("glob.glob(f'{ROOT}/logic/units/deu_09*.yaml') + glob.glob(f'{ROOT}/logic/units/deu_10*.yaml')", "glob.glob(f'{ROOT}/logic/units/deu_10*.yaml') + glob.glob(f'{ROOT}/logic/units/deu_11*.yaml')"),
 ("    if uid.startswith('deu_10'): print(", "    if uid.startswith('deu_11'): print("),
 ("for p in ('DV10', 'DV10A', 'DV10B', 'DV09', 'DV11')})", "for p in ('DV11', 'DV11A', 'DV11B', 'DV10', 'DV12')})"),
 ("print('  existing manifests deu_10*:', sorted(os.path.basename(f) for f in glob.glob(f'{ROOT}/logic/oral_audit/manifests/deu_10*'))", "print('  existing manifests deu_11*:', sorted(os.path.basename(f) for f in glob.glob(f'{ROOT}/logic/oral_audit/manifests/deu_11*'))"),
 ("print('  overrides already for Deut.10:', re.findall(r'\"Deut\\.10\\.[^\"]+\": \"[^\"]+\"', OV)[:20], '| by_ref last Deut.9 line:', [l for l in OV.split('\\n') if l.startswith('  \"Deut.9.')][-1:])",
  "print('  overrides already for Deut.11:', re.findall(r'\"Deut\\.11\\.[^\"]+\": \"[^\"]+\"', OV)[:20], '| by_ref last Deut.10 line:', [l for l in OV.split('\\n') if l.startswith('  \"Deut.10.')][-1:])"),
]
for old, new in REPL:
    n = s.count(old); assert n >= 1, ('ABSENT', old[:90]); s = s.replace(old, new)
# SECTION I RETURNS — chapter 6's form (ch6_dump0.py), the SPINE computed above, the rows written whole to the spine file
i = s.index("print('==== I. THE SPINE ON THE CHAPTER — none")
s = s[:i] + r'''print('==== I. THE SPINE ON THE CHAPTER — the Sifrei piskaot whose head is in chapter', CH, '(the first on-chapter piskaot since chapter 6), whole')
print('  SPINE (computed from the heads):', SPINE, '| contiguous?', SPINE == list(range(SPINE[0], SPINE[-1] + 1)), '| the heads by verse:', [(p, heads[p][1]) for p in SPINE], '| the heads before and after:', {p: heads[p] for p in (SPINE[0] - 1, SPINE[-1] + 1)})
rows_ps = {p: (len(he[p - 1]), len(en[p - 1])) for p in SPINE}
print('  rows per piska (HE, EN):', rows_ps, '| total HE rows', sum(a for a, _ in rows_ps.values()), '| HE == EN everywhere?', all(a == b for a, b in rows_ps.values()))
with open(f'{SP}/ch11_sifrei_spine.txt', 'w', encoding='utf-8') as f:
    for p in SPINE:
        for r in range(len(he[p - 1])): f.write(f'--- {p}:{r + 1} (head {heads[p]})\nHE: {clean(he[p - 1][r])}\nEN: {clean(en[p - 1][r]) if r < len(en[p - 1]) else "(no EN row)"}\n')
print('  spine file bytes', os.path.getsize(f'{SP}/ch11_sifrei_spine.txt'), '| bytes per piska HE+EN:', {p: sum(len(clean(he[p - 1][r])) + (len(clean(en[p - 1][r])) if r < len(en[p - 1]) else 0) for r in range(len(he[p - 1]))) for p in SPINE})
print('  prior reads among the spine rows (any ledger):', [(f, p, r) for f, p, r in PRIOR if p in SPINE])
print('  the spine rows citing a verse of chapter', CH, 'in the Hebrew (p, r, the export verses):', [(p, r + 1, sorted({c[2] for c in he_cites(clean(he[p - 1][r])) if c[0] == 'דברים' and c[1] == CH})) for p in SPINE for r in range(len(he[p - 1])) if any(c[0] == 'דברים' and c[1] == CH for c in he_cites(clean(he[p - 1][r])))])
print('  the spine rows\' own Hebrew citations (book, chapter, verse) by row:', [(p, r + 1, he_cites(clean(he[p - 1][r]))) for p in SPINE for r in range(len(he[p - 1])) if he_cites(clean(he[p - 1][r]))])
print('  the spine rows\' English citations by row:', [(p, r + 1, re.findall(r'\(([A-Z][a-z]+\.? ?\d+:\d+(?:-\d+)?)\)', clean(en[p - 1][r]))) for p in SPINE for r in range(len(en[p - 1])) if re.findall(r'\(([A-Z][a-z]+\.? ?\d+:\d+(?:-\d+)?)\)', clean(en[p - 1][r]))])
print('  the spine rows with NO citation in either file:', [(p, r + 1) for p in SPINE for r in range(len(he[p - 1])) if not he_cites(clean(he[p - 1][r])) and not re.findall(r'\([A-Z][a-z]+\.? ?\d+:\d+', clean(en[p - 1][r]))])
print('  the portion edge inside the chapter: Ekev ends at 11:25, Re\'eh opens at 11:26 — the heads at or after verse 26:', [(p, heads[p]) for p in SPINE if heads[p][1] >= 26])
'''
left = [m for m in re.findall(r'.{30}(?:ch10_|Deut 10:|Deut\.10\.|Exod \(25\|34\|37\)).{30}', s.replace('ch10_dump0.py', ''))]
left += [m for m in re.findall(r'.{30}deu_10.{30}', s) if 'glob' not in m]
assert not left, left
open(f'{SP}/ch11_dump0.py', 'w', encoding='utf-8').write(s)
import ast; ast.parse(s)
print('derived ch11_dump0.py', len(s), 'bytes;', len(REPL), 'substitutions; section I in chapter 6\'s form')
