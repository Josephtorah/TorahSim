import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE DEUTERONOMY WALK 8b (2026-09-20): THREE OLDER READBACK PROBES HOLD THE MARKER COUNT AS A LITERAL — 4b's Q14, 5b's Q17 and 6b's Q20 ('no marker in this
# chapter' tested beside the tape's total): 24/27 at the chain's first pass (gates_ch10b/probe_readback.out), retyped 169 -> 172 from the print. 7b's lesson 12
# repeated ("a count literal in a PROBE moves like one in a checkpoint — grep the probes too before the chain"): the design's list named Q23 alone; the three
# older probes were retyped at 7b (patch_probes167_ch9.py) and their new literal joined the list unnoticed at this sitting's design. Idempotent.
import subprocess
ROOT = _ROOT
P = ROOT + '/World/step9/readback_probes.py'
s = open(P, encoding='utf-8').read()
def rep(old, new):
    global s
    assert s.count(old) == 1, (s.count(old), old[:80]); s = s.replace(old, new)
rep("return got == (1, 1, False, 169, 1, 1, 'Deut 6:4', 'Deut 6:16')", "return got == (1, 1, False, 172, 1, 1, 'Deut 6:4', 'Deut 6:16')")
rep("return got == (1, 1, 1, False, 169, 1, 1, 1, 1, 1, 1, 1, 'Deut 7:1', 'Deut 7:25')", "return got == (1, 1, 1, False, 172, 1, 1, 1, 1, 1, 1, 1, 'Deut 7:1', 'Deut 7:25')")
rep("return got == (1, 1, 1, False, 169, 1, 1, 2, 'Deut 8:7', 'Deut 8:11', 'Deut 8:19', 'Deut 4:25')", "return got == (1, 1, 1, False, 172, 1, 1, 2, 'Deut 8:7', 'Deut 8:11', 'Deut 8:19', 'Deut 4:25')")
rep("  (Q14, Q17 and Q20's marker count 167 -> 169 at THE DEUTERONOMY WALK 7b, 2026-09-19 — the two markers at Deut 9:20 and 9:21; a count literal in a probe moves like one in a checkpoint: retyped from the chain's print)",
    "  (Q14, Q17 and Q20's marker count 167 -> 169 at THE DEUTERONOMY WALK 7b, 2026-09-19 — the two markers at Deut 9:20 and 9:21; 169 -> 172 at THE DEUTERONOMY WALK 8b, 2026-09-20 — the three markers at Deut 10:2, 10:6 and 10:12; a count literal in a probe moves like one in a checkpoint: retyped from the chain's print each time)")
open(P, 'w', encoding='utf-8').write(s)
import py_compile; py_compile.compile(P, doraise=True)
print('Q14, Q17, Q20 retyped 169 -> 172 from the chain\'s print; compiles')
