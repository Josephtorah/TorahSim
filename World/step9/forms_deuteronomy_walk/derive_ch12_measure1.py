import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE DEUTERONOMY WALK sitting 10 — CHAPTER 12's READING (2026-09-20): ch12_measure1.py built from the forms' ch11_measure1.py — the HELPERS (from the import line
# to the V11 lambda) and the REGISTER block (D) by asserted substitutions (11 → 12), every other section chapter 12's own (the kin FOUND BY COMPUTATION over the
# whole Bible and the law kin named; the phrase censuses of the place, the slaughter, the blood, the tithe, the Levite, the abomination; the parser on the
# chapter's one number verse and its starred tithe; Onkelos's Shekhinah, errors, permission, fitness; the English's brackets; the store's gloss families; the
# prior reads and the register's finder). derive_ch11_measure1.py's form, the blocks found by content, never by line number.
import os, re, subprocess
ROOT = _ROOT
SP = os.path.dirname(os.path.abspath(__file__))
src = open(f'{ROOT}/World/step9/forms_deuteronomy_walk/ch11_measure1.py', encoding='utf-8').read()
i = src.index('import json, os, re, html, sqlite3'); j = src.index("V11 = lambda v: words('Deut', 11, v)"); j = src.index('\n', j) + 1
head = src[i:j]
GIT = "ROOT = _ROOT"
assert head.count('ROOT = _ROOT') == 1, 'the forms copy carries the portable ROOT line once'; head = head.replace('ROOT = _ROOT', GIT)   # the forms' portable header turned back to the git root for a scratch run
for old, new in (("CH = 11\n", "CH = 12\n"), ("# typed from ch11_dump0's A0 print: 32 = 32, the identity, cost 18 (chapter 5 the book's one split)", "# typed from ch12_dump0's A0 print: 31 = 31, the identity, cost 26 (chapter 5 the book's one split)"), ("V11 = lambda v: words('Deut', 11, v)", "V12 = lambda v: words('Deut', 12, v)")):
    assert head.count(old) == 1, old; head = head.replace(old, new)
assert 'CH = 12' in head and 'V12 = ' in head and "'Deut', 11" not in head and '_ROOT' not in head
di = src.index("print('==== D. THE REGISTER"); dj = src.index("print('==== E. ONKELOS")
D = src[di:dj]
D = D.replace("('Deut', 11, v)", "('Deut', 12, v)").replace('V11(v)', 'V12(v)').replace("f'11:{v}'", "f'12:{v}'").replace('chapter 11', 'chapter 12')
assert "('Deut', 11" not in D and 'V11(' not in D and 'chapter 11' not in D, [m for m in re.findall(r".{20}(?:'Deut', 11|V11\(|chapter 11).{20}", D)]
OWN = open(f'{SP}/ch12_measure1_sections.py', encoding='utf-8').read()
A, rest = OWN.split('# ==== D-PLACEHOLDER ====\n')
out = ("#!/usr/bin/env python3\n# DEUTERONOMY CHAPTER 12, THE READING (THE DEUTERONOMY WALK sitting 10, 2026-09-20; the owner: \"Monitor how long each step takes and report when the\n"
       "# chapter is done\"; ONE RUN + ITS TAIL under the cost rules A-B-C): THE SECOND MEASUREMENT PASS — every candidate ink fact PRINTED from the Tanakh DB, the\n"
       "# store and the shelf's bytes, so that ch12_ink.py's asserts are typed FROM THE PRINT. THE KIN FOUND BY COMPUTATION (every verse against the whole Bible by\n"
       "# shared tokens, the closest re-scored in order) beside THE LAW KIN NAMED (Leviticus 17's slaughter and blood, Exodus 20:21's altar, Numbers 18's dues,\n"
       "# 7:5's demolition, Molech, the rest and the inheritance, the Levite's portion, the desire of the soul); the phrase censuses over the whole DB; the parser on\n"
       "# the chapter's one number verse (12:14 'in one of your tribes') and its starred tithe (12:17); Onkelos's renderings' seats over the book; the English's\n"
       "# bracketed supplements; the store's gloss families over the whole store; the prior reads on the kin; the register's finder on the chapter. Chapter 11's\n"
       "# helpers and register block by asserted substitutions (derive_ch12_measure1.py); the sections chapter 12's own. Nothing asserted.\n" + head + '\n' + A + D + '\n' + rest)
open(f'{SP}/ch12_measure1.py', 'w', encoding='utf-8').write(out)
import ast; ast.parse(out); print('ch12_measure1.py built:', len(out), 'bytes')
