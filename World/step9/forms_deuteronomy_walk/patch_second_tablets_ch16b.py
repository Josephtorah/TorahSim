import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE DEUTERONOMY WALK 14b (LEAN): the second-tablets callee's SECOND scan seat widened — LAW_SCAN (the laws on Israel by pattern, its own names excluded) found
# bribe_barred after the tape's first run had written chapter 16's lines into the one database (the tape's second run stopped at the import); the first seat
# (BRIBE_SCAN) was widened at the design — the same lesson at its second seat. The value excluded with the sitting's note; nothing else moves. RUN FROM THE REPO ROOT.
import subprocess, re
ROOT = _ROOT
P = ROOT + '/World/step9/cold_run_second_tablets.py'
s = open(P, encoding='utf-8').read()
old = "LAW_SCAN = None if _law is None else [e for e in _law if e not in ('cleaving_commanded', 'stiffening_barred', 'heart_circumcision_commanded', 'fear_of_heaven_asked', "
assert s.count(old) == 1, s.count(old)
new = "LAW_SCAN = None if _law is None else [e for e in _law if e not in ('bribe_barred', 'cleaving_commanded', 'stiffening_barred', 'heart_circumcision_commanded', 'fear_of_heaven_asked', "
s = s.replace(old, new)
# the note beside the assert
old2 = "assert LAW_SCAN in ([], None), LAW_SCAN   # nothing written on Israel for the cleaving, the heart, the neck, the bribe or the fear of Heaven before this sitting (the code's holes)"
assert s.count(old2) == 1, s.count(old2)
s = s.replace(old2, old2 + "; THE DEUTERONOMY WALK 14b (2026-09-23): bribe_barred excluded from this scan too — Deut 16:19 writes the block's FIRST entry on israel_people (the tape's first run put it in the one database; the second run's import found it here — the same lesson at the callee's second seat)")
open(P, 'w', encoding='utf-8').write(s)
import py_compile; py_compile.compile(P, doraise=True); print('second_tablets: bribe_barred excluded from LAW_SCAN (the second seat); the file compiles')
