import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE DEUTERONOMY WALK sitting 13b — THE COMPILE OF CHAPTER 15: THE TAPE'S FIRST RUN 9/10 — CU5 (8b's THE KIN STANDS) counts blessings_for_hearing through the
# helper _n_gl('blessings_for_hearing'); chapter 15's reuse (15:5, source beginning "Deut 15:1") made it TWO; the design's grep found four count seats (CQ6, DC6,
# DD2, DF5) and not this fifth. A MISS IS EVIDENCE, NEVER A RETYPE — read from the tape's print, retyped here with the old text asserted present exactly once.
# 12b's form (the DD2 retype at 10b). RUN FROM THE REPO ROOT.
import subprocess, re, os
ROOT = _ROOT
SP = os.path.dirname(os.path.abspath(__file__))
SEQ = ROOT + '/World/step9/cold_run_sequence.py'
run1 = open(SP + '/ch15_tape_run1.out', encoding='utf-8').read()
cu5 = [l for l in run1.splitlines() if 'CHECKPOINT CU5 ' in l]; assert len(cu5) == 1 and cu5[0].endswith(' DIVERGE'), cu5
assert re.search(r'^9/10 checkpoints$', run1, re.M) and 'DIFF' not in run1
got = re.search(r"^\s+got\s+(\[.*\])\s*$", run1, re.M).group(1); want = re.search(r"^\s+want\s+(\[.*\])\s*$", run1, re.M).group(1)   # "got" is followed by TWO spaces in the print (aligned with "want ")
import ast; g = ast.literal_eval(got); wnt = ast.literal_eval(want)
diff = [(a, b) for a, b in zip(g, wnt) if a != b]; assert diff == [('CU5 DIVERGE', 'CU5 MATCH')] and len(g) == len(wnt) == 316, (diff, len(g), len(wnt))
s = open(SEQ, encoding='utf-8').read()
OLD = "blessings_for_hearing ONE UNMOVED; treasured_people ONE UNMOVED', (1, 2, 1, 1, 1, 1, 1, 1), (_n_gl('manna_provided')"
NEW = ("blessings_for_hearing TWO since THE DEUTERONOMY WALK 13b (2026-09-23 — the reuse at 15:5, source beginning \"Deut 15:1\"; the tape\\'s first run 9/10 with this seat "
       "the miss: the design\\'s grep found four count seats and not this fifth, the name inside the helper\\'s call _n_gl(...) — RETYPED FROM THE TAPE\\'S PRINT); "
       "treasured_people ONE UNMOVED', (1, 2, 1, 1, 1, 1, 2, 1), (_n_gl('manna_provided')")   # the apostrophes ESCAPED — the seat is a single-quoted string (the first patch left them bare: a SyntaxError on the second run)
assert s.count(OLD) == 1, s.count(OLD)
s = s.replace(OLD, NEW); assert s.count(NEW) == 1
open(SEQ, 'w', encoding='utf-8').write(s)
print('patched: CU5 the seventh seat 1 -> 2 (blessings_for_hearing TWO), read from ch15_tape_run1.out (9/10; the one DIFF CU5 DIVERGE vs MATCH)')
