import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE DEUTERONOMY WALK 6b (2026-09-19): ONE OLDER CHECKPOINT RETYPED FROM THE PRINT (ch8_tape1.out — 9/10, the one miss the VERDICTS list: CC7 DIVERGE) —
# chapter 4's CC7 holds the CURRENT COUNT of heaven_and_earth_witness on Israel as a literal (1); the chapter-8 line perishing_testified REUSES the effect
# at 8:19 (CU6 counts TWO, the 4:26 entry unmoved) — the literal moved by design (5b's lesson: a write that moves an older count retypes that count from
# the print; the design said 'no retype expected' — wrong on this one, the reuse is a second entry on the same ledger). The declared tuple 1 -> 2, its
# note dated; nothing else touched.
import subprocess, py_compile
ROOT = _ROOT
P = ROOT + '/World/step9/cold_run_sequence.py'
s = open(P, encoding='utf-8').read()
old = "cp('CC7 THE WITNESSES AND THE CASE — heaven_and_earth_witness on israel_people ONE dated (40, 11, 1), source beginning \"Deut 4:25\"; no timer set by the sitting\\'s lines (the end of days a prophecy); the tochacha\\'s scattered_among_nations registered and NOT written on the tape (no exile)', (1, (40, 11, 1), 'Deut 4:2', 0, True, 0),"
new = "cp('CC7 THE WITNESSES AND THE CASE — heaven_and_earth_witness on israel_people TWO (ONE at 2b; 2 since THE DEUTERONOMY WALK 6b, 2026-09-19 — chapter 8\\'s perishing_testified REUSES the effect at 8:19, CU6; the first entry 4:25\\'s unmoved, dated (40, 11, 1), source beginning \"Deut 4:25\" — retyped from the print, 5b\\'s lesson); no timer set by the sitting\\'s lines (the end of days a prophecy); the tochacha\\'s scattered_among_nations registered and NOT written on the tape (no exile)', (2, (40, 11, 1), 'Deut 4:2', 0, True, 0),"
assert s.count(old) == 1, s.count(old)
s = s.replace(old, new); open(P, 'w', encoding='utf-8').write(s); py_compile.compile(P, doraise=True)
print('CC7 retyped: heaven_and_earth_witness 1 -> 2 (the reuse at 8:19); compiles')
