import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE DEUTERONOMY WALK 7b (2026-09-19): THREE OLDER READBACK PROBES MOVED at the first chain (gates_ch9b/probe_readback.out: 21/24 — Q22-Q24 PASS, Q14, Q17 and
# Q20 FAIL): each older chapter's "no marker" probe (4b's Q14, 5b's Q17, 6b's Q20) holds the tape's marker COUNT as a literal (167) beside its "no chapter-N
# marker" test — a count literal in a PROBE, the same class as the sequence file's nine (retyped at the literals patch) and CA1's list (retyped at the tape):
# retyped here from the print, 167 -> 169, the docstring noted. patch_cc7_ch8.py's form.
import subprocess
ROOT = _ROOT
P = ROOT + '/World/step9/readback_probes.py'
s = open(P, encoding='utf-8').read()
assert s.count('False, 167,') == 3, s.count('False, 167,')   # Q14, Q17, Q20's expected tuples
s = s.replace('False, 167,', 'False, 169,')
old = "Run: python3 World/step9/readback_probes.py"
assert s.count(old) == 1
s = s.replace(old, "  (Q14, Q17 and Q20's marker count 167 -> 169 at THE DEUTERONOMY WALK 7b, 2026-09-19 — the two markers at Deut 9:20 and 9:21; a count literal in a probe moves like one in a checkpoint: retyped from the chain's print)\n" + old)
open(P, 'w', encoding='utf-8').write(s)
import py_compile; py_compile.compile(P, doraise=True)
print('readback_probes.py: Q14, Q17, Q20 retyped 167 -> 169; compiles')
