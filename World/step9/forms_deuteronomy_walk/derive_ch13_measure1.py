import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE DEUTERONOMY WALK sitting 11 — CHAPTER 13's READING (2026-09-21): ch13_measure1.py built from the forms' ch12_measure1.py — the HELPERS (from the import line
# to the V12 lambda) and the REGISTER block (D) by asserted substitutions (12 → 13), every other section chapter 13's own (the kin FOUND BY COMPUTATION over the
# whole Bible and the law kin named; the phrase censuses of the seducer's formula, the testing, the six verbs, the purge, the inciters, the five prohibitions,
# the hand first, the stoning, the hearing and fearing, the inquiry, the sword and the ban, the whole offering and the heap, the fierce anger and the mercy;
# the parser on the chapter's one number verse; Onkelos's fear, acceptance, Word, errors; the English's brackets; the store's gloss families and the
# written/read pair at 13:16; the prior reads and the register's finder). derive_ch12_measure1.py's form, the blocks found by content, never by line number.
import os, re, subprocess
ROOT = _ROOT
SP = os.path.dirname(os.path.abspath(__file__))
src = open(f'{ROOT}/World/step9/forms_deuteronomy_walk/ch12_measure1.py', encoding='utf-8').read()
i = src.index('import json, os, re, html, sqlite3'); j = src.index("V12 = lambda v: words('Deut', 12, v)"); j = src.index('\n', j) + 1
head = src[i:j]
GIT = "ROOT = _ROOT"
assert head.count('ROOT = _ROOT') == 1, 'the forms copy carries the portable ROOT line once'; head = head.replace('ROOT = _ROOT', GIT)   # the forms' portable header turned back to the git root for a scratch run
for old, new in (("CH = 12\n", "CH = 13\n"), ("# typed from ch12_dump0's A0 print: 31 = 31, the identity, cost 26 (chapter 5 the book's one split)", "# typed from ch13_dump0's A0 print: 19 = 19, the identity, cost 10 (chapter 5 the book's one split)"), ("V12 = lambda v: words('Deut', 12, v)", "V13 = lambda v: words('Deut', 13, v)")):
    assert head.count(old) == 1, old; head = head.replace(old, new)
assert 'CH = 13' in head and 'V13 = ' in head and "'Deut', 12" not in head and '_ROOT' not in head
di = src.index("print('==== D. THE REGISTER"); dj = src.index("print('==== E. ONKELOS")
D = src[di:dj]
D = D.replace("('Deut', 12, v)", "('Deut', 13, v)").replace('V12(v)', 'V13(v)').replace("f'12:{v}'", "f'13:{v}'").replace('chapter 12', 'chapter 13')
assert "('Deut', 12" not in D and 'V12(' not in D and 'chapter 12' not in D, [m for m in re.findall(r".{20}(?:'Deut', 12|V12\(|chapter 12).{20}", D)]
OWN = open(f'{SP}/ch13_measure1_sections.py', encoding='utf-8').read()
A, rest = OWN.split('# ==== D-PLACEHOLDER ====\n')
out = ("#!/usr/bin/env python3\n# DEUTERONOMY CHAPTER 13, THE READING (THE DEUTERONOMY WALK sitting 11, 2026-09-21; the owner: \"Go\" after the reread that followed 10b's compaction;\n"
       "# ONE RUN + ITS TAIL under the cost rules A-B-C): THE SECOND MEASUREMENT PASS — every candidate ink fact PRINTED from the Tanakh DB, the store and the\n"
       "# shelf's bytes, so that ch13_ink.py's asserts are typed FROM THE PRINT. THE KIN FOUND BY COMPUTATION (every verse against the whole Bible by shared tokens,\n"
       "# the closest re-scored in order) beside THE LAW KIN NAMED (4:2's adding and diminishing, 18:20's false prophet, 17:2-7's idolater and the hand first, 8:2's\n"
       "# testing, 10:20's four verbs, 7:16's unpitying eye, the stoning at Leviticus 20 and 24, the ban at Leviticus 27 and Joshua 6-8, the fierce anger at Numbers\n"
       "# 25 and Joshua 7, the oath's formula); the phrase censuses over the whole DB; the parser on the chapter's one number verse (13:13 'in one of your cities');\n"
       "# Onkelos's renderings' seats over the book; the English's bracketed supplements; the store's gloss families and the written/read pair at 13:16; the prior\n"
       "# reads on the kin; the register's finder on the chapter. Chapter 12's helpers and register block by asserted substitutions (derive_ch13_measure1.py); the\n"
       "# sections chapter 13's own. Nothing asserted.\n" + head + '\n' + A + D + '\n' + rest)
open(f'{SP}/ch13_measure1.py', 'w', encoding='utf-8').write(out)
import ast; ast.parse(out); print('ch13_measure1.py built:', len(out), 'bytes')
