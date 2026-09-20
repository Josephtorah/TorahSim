import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE DEUTERONOMY WALK 8b (2026-09-20): THE ELEVENTH STALE LITERAL — the tape's first run (ch10_tape1.out) 9/10 with ONE miss: DA1 DIVERGE, 7b's LINES
# checkpoint holding 'markers 169' in its tuple in a form the ten retypes did not cover ("[(40, 11, 1)], 169, (40, 11, 1))" — 7b's own literal, typed
# after the nine older ones were retyped and so outside their patterns); retyped from the print to 172, its text extended. A miss is evidence: read, then
# retyped once (5b's, 6b's and 7b's lesson on a stale literal — every line of a literal covered, and the newest sitting's own literal joins the list).
import subprocess
ROOT = _ROOT
P = ROOT + '/World/step9/cold_run_sequence.py'
s = open(P, encoding='utf-8').read()
old = "True, [(40, 11, 1)], 169, (40, 11, 1)), (len(ev_nr)"
assert s.count(old) == 1, s.count(old)
s = s.replace(old, "True, [(40, 11, 1)], 172, (40, 11, 1)), (len(ev_nr)")
old2 = "the FORWARD marker at Deut 9:21 at (40, 11, 1); markers 167 -> 169; the counter ends at (40, 11, 1) unmoved'"
assert s.count(old2) == 1, s.count(old2)
s = s.replace(old2, "the FORWARD marker at Deut 9:21 at (40, 11, 1); markers 167 -> 169 (169 -> 172 since THE DEUTERONOMY WALK 8b, 2026-09-20 — the three markers at Deut 10:2, 10:6 and 10:12); the counter ends at (40, 11, 1) unmoved'")
open(P, 'w', encoding='utf-8').write(s)
import py_compile; py_compile.compile(P, doraise=True)
print('DA1 retyped 169 -> 172 (the eleventh stale literal — read at the tape\'s first run); compiles')
