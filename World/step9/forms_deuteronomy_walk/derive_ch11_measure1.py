import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE DEUTERONOMY WALK sitting 9 — CHAPTER 11's READING (2026-09-20): ch11_measure1.py built from the forms' ch10_measure1.py — the HELPERS (from the import line to
# the V10 lambda) and the REGISTER block (D) by asserted substitutions (10 → 11), every other section chapter 11's own (the kin of the discipline seen — Egypt, the
# sea, the wilderness, Dathan and Abiram; the land not like Egypt; the second paragraph of the Shema — the rain, the anger, the tefillin, the teaching, the mezuzah;
# the borders and the dread; the blessing and the curse, Gerizim and Ebal, Gilgal and the terebinths of Moreh; the frame; the parser on a chapter with NO number
# verse; Onkelos's renderings over the book; the English's brackets; the store's gloss families over the whole store; the prior reads). derive_ch10_measure1.py's
# form, the blocks found by content, never by line number.
import os, re, subprocess
ROOT = _ROOT
SP = os.path.dirname(os.path.abspath(__file__))
src = open(f'{ROOT}/World/step9/forms_deuteronomy_walk/ch10_measure1.py', encoding='utf-8').read()
i = src.index('import json, os, re, html, sqlite3'); j = src.index("V10 = lambda v: words('Deut', 10, v)"); j = src.index('\n', j) + 1
head = src[i:j]
for old, new in (("ROOT = _ROOT", "ROOT = _ROOT"), ("CH = 10\n", "CH = 11\n"), ("# typed from ch10_dump0's A0 print: 22 = 22, the identity, cost 14 (chapter 5 the book's one split)", "# typed from ch11_dump0's A0 print: 32 = 32, the identity, cost 18 (chapter 5 the book's one split)"), ("V10 = lambda v: words('Deut', 10, v)", "V11 = lambda v: words('Deut', 11, v)")):
    assert head.count(old) == 1, old; head = head.replace(old, new)
assert 'CH = 11' in head and 'V11 = ' in head and "'Deut', 10" not in head and '_ROOT' not in head
di = src.index("print('==== D. THE REGISTER"); dj = src.index("print('==== E. ONKELOS chapter 10")
D = src[di:dj]
D = D.replace("('Deut', 10, v)", "('Deut', 11, v)").replace('V10(v)', 'V11(v)').replace("f'10:{v}'", "f'11:{v}'").replace('chapter 10', 'chapter 11')
assert "('Deut', 10" not in D and 'V10(' not in D and 'chapter 10' not in D, [m for m in re.findall(r".{20}(?:'Deut', 10|V10\(|chapter 10).{20}", D)]
OWN = open(f'{SP}/ch11_measure1_sections.py', encoding='utf-8').read()
A, rest = OWN.split('# ==== D-PLACEHOLDER ====\n')
out = ("#!/usr/bin/env python3\n# DEUTERONOMY CHAPTER 11, THE READING (THE DEUTERONOMY WALK sitting 9, 2026-09-20; the owner: \"Go\"; ONE RUN under the two-run rule): THE SECOND\n"
       "# MEASUREMENT PASS — every candidate ink fact PRINTED from the Tanakh DB, the store and the shelf's bytes, so that ch11_ink.py's asserts are typed FROM THE PRINT.\n"
       "# THE KIN DIFFED token by token — the discipline seen (11:1-7) against 6:5, Genesis 26:5, the formula of the hand and the arm, Exodus 14-15's sea, Numbers 16's\n"
       "# swallowing and the flood's 'living thing'; the land not like Egypt (11:8-12) against 8:7-10, Genesis 13:10, Leviticus 26:4; THE SECOND PARAGRAPH OF THE SHEMA\n"
       "# (11:13-21) against 6:5-9, 28:1, Exodus 13:9-16, Leviticus 26:19-20, Joshua 23:16; the borders and the dread (11:22-25) against Joshua 1:3-5, Genesis 15:18,\n"
       "# Exodus 23:27-31, 1:7, 34:2, 7:24, 2:25; the blessing and the curse (11:26-32) against 30:15-19, 27:12-13, Joshua 8:30-35, Genesis 12:6, 27:12, 12:1; the phrase\n"
       "# censuses over the whole DB; the parser on a chapter WITHOUT A NUMBER VERSE; Onkelos's renderings' seats over the book (the export's chapter 11 = the DB's,\n"
       "# identity); the English's bracketed supplements; the store's gloss families over the whole store; the prior reads on the kin. Chapter 10's helpers and\n"
       "# register block by asserted substitutions (derive_ch11_measure1.py); the sections chapter 11's own. Nothing asserted.\n" + head + '\n' + A + D + '\n' + rest)
open(f'{SP}/ch11_measure1.py', 'w', encoding='utf-8').write(out)
import ast; ast.parse(out); print('ch11_measure1.py built:', len(out), 'bytes')
