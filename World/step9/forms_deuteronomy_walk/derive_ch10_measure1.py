import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE DEUTERONOMY WALK sitting 8 — CHAPTER 10's READING (2026-09-19): ch10_measure1.py built from the forms' ch9_measure1.py — the HELPERS (from the import line to
# the V9 lambda) and the REGISTER block (D) by asserted substitutions (9 → 10), every other section chapter 10's own (the kin of the second tablets, the ark, the
# stations and Aaron's death, the Levites, the fear and the love, the stranger, the seventy; the parser on the five number verses; Onkelos's renderings; the store's
# gloss families; the prior reads). derive_ch9_measure1.py's form, the blocks found by content, never by line number.
import os, re, subprocess
ROOT = _ROOT
SP = os.path.dirname(os.path.abspath(__file__))
src = open(f'{ROOT}/World/step9/forms_deuteronomy_walk/ch9_measure1.py', encoding='utf-8').read()
i = src.index('import json, os, re, html, sqlite3'); j = src.index("V9 = lambda v: words('Deut', 9, v)"); j = src.index('\n', j) + 1
head = src[i:j]
for old, new in (("ROOT = _ROOT", "ROOT = _ROOT"), ("CH = 9\n", "CH = 10\n"), ("# typed from ch9_dump0's A0 print: 29 = 29, the identity (chapter 5 the book's one split)", "# typed from ch10_dump0's A0 print: 22 = 22, the identity, cost 14 (chapter 5 the book's one split)"), ("V9 = lambda v: words('Deut', 9, v)", "V10 = lambda v: words('Deut', 10, v)")):
    assert head.count(old) == 1, old; head = head.replace(old, new)
assert 'CH = 10' in head and 'V10 = ' in head and "'Deut', 9" not in head and '_ROOT' not in head
di = src.index("print('==== D. THE REGISTER"); dj = src.index("print('==== E. ONKELOS chapter 9")
D = src[di:dj]
D = D.replace("('Deut', 9, v)", "('Deut', 10, v)").replace('V9(v)', 'V10(v)').replace("f'9:{v}'", "f'10:{v}'").replace('chapter 9', 'chapter 10')
assert "('Deut', 9" not in D and 'V9(' not in D and 'chapter 9' not in D, [m for m in re.findall(r".{20}(?:'Deut', 9|V9\(|chapter 9).{20}", D)]
OWN = open(f'{SP}/ch10_measure1_sections.py', encoding='utf-8').read()
A, rest = OWN.split('# ==== D-PLACEHOLDER ====\n')
out = ("#!/usr/bin/env python3\n# DEUTERONOMY CHAPTER 10, THE READING (THE DEUTERONOMY WALK sitting 8, 2026-09-19; the owner: \"Go\"; ONE RUN under the two-run rule): THE SECOND\n"
       "# MEASUREMENT PASS — every candidate ink fact PRINTED from the Tanakh DB, the store and the shelf's bytes, so that ch10_ink.py's asserts are typed FROM THE PRINT.\n"
       "# THE KIN DIFFED token by token — the second tablets and the ark (10:1-5) against Exodus 34:1-4, 34:28-29, 25:10-21, 37:1, 40:20 and 9:9-17, the stations and\n"
       "# Aaron's death (10:6-7) against Numbers 33:30-39 and 20:22-29, the Levites (10:8-9) against Numbers 3, 8, 16, 18 and 18:1-7, the third forty (10:10-11) against\n"
       "# 9:18-25 and Exodus 32:34-33:2, the demand (10:12-13) against 6:5, 6:13, 11:13, 11:22 and Micah 6:8, the heavens and the choosing (10:14-15) against 1 Kings 8:27 and\n"
       "# 4:37, 7:6-8, the heart's foreskin and the stiff neck (10:16) against 30:6, Leviticus 26:41, Jeremiah 4:4 and the calf's six seats, the attributes and the bribe (10:17-19)\n"
       "# against Psalm 136, Nehemiah 9:32, 16:19, Exodus 23:8, 22:20-23, Leviticus 19:33-34, the four clauses (10:20) against 6:13, the seventy and the stars (10:22) against\n"
       "# Genesis 46:27, Exodus 1:5, 1:10 and 28:62; the phrase censuses over the whole DB; the five number verses and the ordinal; Onkelos's renderings' seats over the book\n"
       "# (the export's chapter 10 = the DB's, identity); the English's bracketed supplements; the store's gloss families; the prior reads on the kin. Chapter 9's helpers and\n"
       "# register block by asserted substitutions (derive_ch10_measure1.py); the sections chapter 10's own. Nothing asserted.\n" + head + '\n' + A + D + '\n' + rest)
open(f'{SP}/ch10_measure1.py', 'w', encoding='utf-8').write(out)
import ast; ast.parse(out); print('ch10_measure1.py built:', len(out), 'bytes')
