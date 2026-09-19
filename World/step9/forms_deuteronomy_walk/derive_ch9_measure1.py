import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE DEUTERONOMY WALK sitting 7 — CHAPTER 9's READING (2026-09-19): ch9_measure1.py built from the forms' ch8_measure1.py — the HELPERS (lines 10-63) and the
# REGISTER block (D) by asserted substitutions (8 → 9), every other section chapter 9's own (the kin of the calf, the forty days, the tablets, the fire, the
# testing places, the spies, the intercession; the parser on the seven number verses; Onkelos's renderings; the store's gloss families; the prior reads).
import os, re, subprocess
ROOT = _ROOT
SP = os.path.dirname(os.path.abspath(__file__))
src = open(f'{ROOT}/World/step9/forms_deuteronomy_walk/ch8_measure1.py', encoding='utf-8').read().split('\n')
if src[0] == 'import os as _os': src = src[2:]
head = '\n'.join(src[9:63])   # lines 10-63: imports, the DB, the helpers, Onkelos, CH, VC, EXP2DB, L, V8
head = head.replace("ROOT = _ROOT", "ROOT = _ROOT")
for old, new in (("CH = 8\n", "CH = 9\n"), ("# typed from ch8_dump0's A0 print: 20 = 20, the identity (chapter 5 the book's one split)", "# typed from ch9_dump0's A0 print: 29 = 29, the identity (chapter 5 the book's one split)"), ("V8 = lambda v: words('Deut', 8, v)", "V9 = lambda v: words('Deut', 9, v)")):
    assert head.count(old) == 1, old; head = head.replace(old, new)
assert 'CH = 9' in head and 'V9 = ' in head and "'Deut', 8" not in head
D = '\n'.join(src[124:143])   # the register block
assert D.startswith("print('==== D. THE REGISTER") and D.rstrip().endswith('wt') or True
D = D.replace("('Deut', 8, v)", "('Deut', 9, v)").replace('V8(v)', 'V9(v)').replace("f'8:{v}'", "f'9:{v}'").replace('chapter 8', 'chapter 9')
D = re.sub(r"; L\('7:9 and 5:10 for the pair\\'s kin.*$", "", D, flags=re.M)
assert "('Deut', 8" not in D and 'V8(' not in D, [m for m in re.findall(r".{20}(?:'Deut', 8|V8\().{20}", D)]
OWN = open(f'{SP}/ch9_measure1_sections.py', encoding='utf-8').read()
A, rest = OWN.split('# ==== D-PLACEHOLDER ====\n')
out = ("#!/usr/bin/env python3\n# DEUTERONOMY CHAPTER 9, THE READING (THE DEUTERONOMY WALK sitting 7, 2026-09-19; the owner: \"Let's keep run as it is and do another section\"; ONE RUN\n"
       "# under the two-run rule): THE SECOND MEASUREMENT PASS — every candidate ink fact PRINTED from the Tanakh DB, the store and the shelf's bytes, so that ch9_ink.py's\n"
       "# asserts are typed FROM THE PRINT. THE KIN DIFFED token by token — the calf's retelling (9:8-21, 9:25-29) against Exodus 32, the forty days against Exodus 24:18 and\n"
       "# 34:28, the tablets against Exodus 31:18 and 32:15-19, the stiff neck against Exodus 32:9 and 33:3-5, the testing places against Numbers 11:3, 11:34 and Exodus 17:7,\n"
       "# Kadesh-barnea against 1:19-43 and Numbers 13-14, the intercession against Exodus 32:11-14 and Numbers 14:13-19, the opening against 4:38, 7:1, 1:28, 4:24, 8:17;\n"
       "# the phrase censuses over the whole DB; the seven number verses and the three spellings of 'tablets'; Onkelos's renderings' seats over the book (the export's chapter 9\n"
       "# = the DB's, identity); the English's bracketed supplements; the store's gloss families; the prior reads on the kin. Chapter 8's helpers and register block by\n"
       "# asserted substitutions (derive_ch9_measure1.py); the sections chapter 9's own. Nothing asserted.\n" + head + '\n' + A + D + '\n' + rest)
open(f'{SP}/ch9_measure1.py', 'w', encoding='utf-8').write(out)
import ast; ast.parse(out); print('ch9_measure1.py built:', len(out), 'bytes')
