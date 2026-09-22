import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE DEUTERONOMY WALK sitting 12 — CHAPTER 14's READING (2026-09-21): ch14_measure1.py built from the forms' ch13_measure1.py — the HELPERS (from the import line
# to the V13 lambda) and the REGISTER block (D) by asserted substitutions (13 → 14), every other section chapter 14's own (the kin FOUND BY COMPUTATION over the
# whole Bible and the law kin named; THE TWIN CHAPTER Leviticus 11 diffed verse by verse; the phrase censuses of the children and the cuts, the holy people, the
# abomination, the ten beasts, the two signs and the four exceptions, the water, the birds and the ra'ah/da'ah letter, the swarming fowl, the carcass and the
# sojourner, the kid in its mother's milk, the tithe and its place, the way and the money, the Levite's portion, the third year and the three; the parser on
# the chapter's number verses 14:6 and 14:28 and the starred tithe tokens; Onkelos's renderings — "flesh with milk", "beloved", the Shekhinah at the place; the
# English's brackets; the store's gloss families; the prior reads and the register's finder). derive_ch13_measure1.py's form, the blocks found by content, never
# by line number. RUN FROM THE REPO ROOT.
import os, re, subprocess
ROOT = _ROOT
SP = os.path.dirname(os.path.abspath(__file__))
src = open(f'{ROOT}/World/step9/forms_deuteronomy_walk/ch13_measure1.py', encoding='utf-8').read()
i = src.index('import json, os, re, html, sqlite3'); j = src.index("V13 = lambda v: words('Deut', 13, v)"); j = src.index('\n', j) + 1
head = src[i:j]
GIT = "ROOT = _ROOT"
assert head.count('ROOT = _ROOT') == 1, 'the forms copy carries the portable ROOT line once'; head = head.replace('ROOT = _ROOT', GIT)   # the forms' portable header turned back to the git root for a scratch run
for old, new in (("CH = 13\n", "CH = 14\n"), ("# typed from ch13_dump0's A0 print: 19 = 19, the identity, cost 10 (chapter 5 the book's one split)", "# typed from ch14_dump0's A0 print: 29 = 29, the identity, cost 17 (chapter 5 the book's one split)"), ("V13 = lambda v: words('Deut', 13, v)", "V14 = lambda v: words('Deut', 14, v)")):
    assert head.count(old) == 1, old; head = head.replace(old, new)
assert 'CH = 14' in head and 'V14 = ' in head and "'Deut', 13" not in head and '_ROOT' not in head and 'subprocess' in head.split('\n')[0]
di = src.index("print('==== D. THE REGISTER"); dj = src.index("print('==== E. ONKELOS")
D = src[di:dj]
D = D.replace("('Deut', 13, v)", "('Deut', 14, v)").replace('V13(v)', 'V14(v)').replace("f'13:{v}'", "f'14:{v}'").replace('chapter 13', 'chapter 14').replace("('Deut', 13, 16)", "('Deut', 14, 21)").replace('13:16', '14:21 (no ketiv this chapter — the line kept as the form)')
assert "('Deut', 13" not in D and 'V13(' not in D and 'chapter 13' not in D, [m for m in re.findall(r".{20}(?:'Deut', 13|V13\(|chapter 13).{20}", D)]
OWN = open(f'{SP}/ch14_measure1_sections.py', encoding='utf-8').read()
A, rest = OWN.split('# ==== D-PLACEHOLDER ====\n')
out = ("#!/usr/bin/env python3\n# DEUTERONOMY CHAPTER 14, THE READING (THE DEUTERONOMY WALK sitting 12, 2026-09-21; the owner: \"Go\" after 11b's tail; ONE RUN + ITS TAIL under\n"
       "# the cost rules A-B-C): THE SECOND MEASUREMENT PASS — every candidate ink fact PRINTED from the Tanakh DB, the store and the shelf's bytes, so that\n"
       "# ch14_ink.py's asserts are typed FROM THE PRINT. THE KIN FOUND BY COMPUTATION (every verse against the whole Bible by shared tokens, the closest re-scored\n"
       "# in order) beside THE LAW KIN NAMED and THE TWIN CHAPTER (Leviticus 11 against 14:3-21 verse by verse; Exodus 22:30, 23:19, 34:26 and Leviticus 17:15,\n"
       "# 19:28, 21:5, 27:30 and Numbers 18:21 at 14:1, 14:21, 14:22; chapter 12's place, desire, far-place and Levite formulas at 14:23-27; 26:12 and 24:19 at\n"
       "# 14:28-29); the phrase censuses over the whole DB; the parser on the chapter's number verses (14:6 'two hoofs', 14:28 'three years') and the starred\n"
       "# tithe tokens; Onkelos's renderings' seats over the book; the English's bracketed supplements; the store's gloss families (no ketiv this chapter); the\n"
       "# prior reads on the kin; the register's finder on the chapter. Chapter 13's helpers and register block by asserted substitutions (derive_ch14_measure1.py);\n"
       "# the sections chapter 14's own. Nothing asserted.\n" + head + '\n' + A + D + '\n' + rest)
open(f'{SP}/ch14_measure1.py', 'w', encoding='utf-8').write(out)
import ast; ast.parse(out); print('ch14_measure1.py built:', len(out), 'bytes')
