import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE DEUTERONOMY WALK sitting 13 — CHAPTER 15's READING (2026-09-22): ch15_measure1.py built from the forms' ch14_measure1.py — the HELPERS (from the import line
# to the V14 lambda) and the REGISTER block (D) by asserted substitutions (14 → 15), every other section chapter 15's own (the kin FOUND BY COMPUTATION over the
# whole Bible and the law kin named; THE TWIN LAWS diffed verse by verse — Exodus 21:2-6 against 15:12-17, Exodus 23:10-11 and Leviticus 25 against 15:1-2,
# chapter 12's clauses against 15:20-23, 5:15 and 24:18 against 15:15, 28:12 against 15:6, 24:15 against 15:9, 17:1 against 15:21, 31:10 and Jeremiah 34:14
# against 15:1; the phrase censuses of the release, the creditor, the foreigner, the needy, the blessing's receipt, the hand opened and shut, the base thought
# and the seventh year, the cry, the Hebrew slave and the Hebrew woman, "empty", the gift from the flock, the floor and the press, the slave remembered, the awl
# and the door, the double hire, the firstling sanctified, not worked nor shorn, year by year, the blemish, the gazelle and the hart, the blood as water; the
# parser on the chapter's number verses 15:1, 7, 9, 12, 18 and the starred "years" tokens; Onkelos's renderings; the English's brackets; the store's gloss
# families; the prior reads and the register's finder). derive_ch14_measure1.py's form, the blocks found by content, never by line number. The sections in TWO
# files (ch15_measure1_sections_a.py the kin and the censuses; _b.py the parser, Onkelos, the brackets, the glosses, the prior reads) joined at the D placeholder
# in _b. RUN FROM THE REPO ROOT.
import os, re, subprocess
ROOT = _ROOT
SP = os.path.dirname(os.path.abspath(__file__))
src = open(f'{ROOT}/World/step9/forms_deuteronomy_walk/ch14_measure1.py', encoding='utf-8').read()
i = src.index('import json, os, re, html, sqlite3'); j = src.index("V14 = lambda v: words('Deut', 14, v)"); j = src.index('\n', j) + 1
head = src[i:j]
GIT = "ROOT = _ROOT"
assert head.count('ROOT = _ROOT') == 1, 'the forms copy carries the portable ROOT line once'; head = head.replace('ROOT = _ROOT', GIT)   # the forms' portable header turned back to the git root for a scratch run
for old, new in (("CH = 14\n", "CH = 15\n"), ("# typed from ch14_dump0's A0 print: 29 = 29, the identity, cost 17 (chapter 5 the book's one split)", "# typed from ch15_dump0's A0 print: 23 = 23, the identity, cost 20 (chapter 5 the book's one split)"), ("V14 = lambda v: words('Deut', 14, v)", "V15 = lambda v: words('Deut', 15, v)")):
    assert head.count(old) == 1, old; head = head.replace(old, new)
assert 'CH = 15' in head and 'V15 = ' in head and "'Deut', 14" not in head and '_ROOT' not in head and 'subprocess' in head.split('\n')[0]
di = src.index("print('==== D. THE REGISTER"); dj = src.index("print('==== E. ONKELOS")
D = src[di:dj]
D = D.replace("('Deut', 14, v)", "('Deut', 15, v)").replace('V14(v)', 'V15(v)').replace("f'14:{v}'", "f'15:{v}'").replace('chapter 14', 'chapter 15')
assert "('Deut', 14" not in D and 'V14(' not in D and 'chapter 14' not in D and '14:' not in D, [m for m in re.findall(r".{20}(?:'Deut', 14|V14\(|chapter 14|14:).{20}", D)]
A = open(f'{SP}/ch15_measure1_sections_a.py', encoding='utf-8').read()
B = open(f'{SP}/ch15_measure1_sections_b.py', encoding='utf-8').read()
Bc, rest = B.split('# ==== D-PLACEHOLDER ====\n')
out = ("#!/usr/bin/env python3\n# DEUTERONOMY CHAPTER 15, THE READING (THE DEUTERONOMY WALK sitting 13, 2026-09-22; the owner: \"Go\" after the compaction at #205 addendum 5; TWO RUNS +\n"
       "# THE TAIL under the cost rules A-B-C — the #204 NOTE): THE SECOND MEASUREMENT PASS — every candidate ink fact PRINTED from the Tanakh DB, the store and the\n"
       "# shelf's bytes, so that ch15_ink.py's asserts are typed FROM THE PRINT. THE KIN FOUND BY COMPUTATION (every verse against the whole Bible by shared tokens,\n"
       "# the closest re-scored in order) beside THE LAW KIN NAMED and THE TWIN LAWS diffed (Exodus 21:2-6 at 15:12-17; Exodus 23:10-11 and Leviticus 25:1-7,\n"
       "# 25:35-46 at 15:1-11; Exodus 13:2, 13:12, 22:29, 34:19, Leviticus 27:26 and Numbers 18:17 at 15:19; Leviticus 22:20-25 and 17:1 at 15:21; chapter 12's\n"
       "# 12:15-16, 12:22-24 at 15:22-23; 5:15 and 24:18 at 15:15; 28:12 at 15:6; 24:15 at 15:9; 31:10 and Jeremiah 34:14 at 15:1); the phrase censuses over the\n"
       "# whole DB; the parser on the chapter's number verses (15:1 'seven years', 15:9 'the seventh', 15:12 and 15:18 'six years', 15:7 'one of your brothers') and\n"
       "# the starred 'years' tokens; Onkelos's renderings' seats over the book; the English's bracketed supplements; the store's gloss families; the prior reads\n"
       "# on the kin; the register's finder on the chapter (15:6's 'as He spoke to you' a candidate receipt shape). Chapter 14's helpers and register block by\n"
       "# asserted substitutions (derive_ch15_measure1.py); the sections chapter 15's own. Nothing asserted.\n" + head + '\n' + A + Bc + D + '\n' + rest)
open(f'{SP}/ch15_measure1.py', 'w', encoding='utf-8').write(out)
import ast; ast.parse(out); print('ch15_measure1.py built:', len(out), 'bytes; sections a', len(A), 'b', len(B))
