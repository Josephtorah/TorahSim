import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE DEUTERONOMY WALK 14b (2026-09-23): cold_run_second_tablets.py's BRIBE_SCAN assert widened — 16:19 writes bribe_barred's FIRST entry on israel_people; once the
# fold carries chapter 16's line, the callee's scan of the one database finds it (9b's lesson: the raw scan is the database's state at import; 13b's lesson: a later
# sitting's write moves an earlier scan's ground). The value asserted with the new arm, the note beside it; nothing else moves. RUN FROM THE REPO ROOT.
import subprocess
ROOT = _ROOT
P = ROOT + '/World/step9/cold_run_second_tablets.py'
s = open(P, encoding='utf-8').read()
old = "assert BRIBE_SCAN in ([], None), BRIBE_SCAN   # bribe_barred NEVER written (the ordinances' block on the judge at Exod 23:8 — 10:17 a declaration, no write)"
new = "assert BRIBE_SCAN in ([], None, ['israel_people']), BRIBE_SCAN   # bribe_barred NEVER written (the ordinances' block on the judge at Exod 23:8 — 10:17 a declaration, no write); THE DEUTERONOMY WALK 14b (2026-09-23): ['israel_people'] once the fold carries chapter 16's line judges_in_every_gate_commanded — Deut 16:19 writes the block's FIRST entry (the scan's ground moved by a later chapter; DB7's 'NEVER' retyped there)"
assert s.count(old) == 1, s.count(old)
s = s.replace(old, new); open(P, 'w', encoding='utf-8').write(s)
import py_compile; py_compile.compile(P, doraise=True); print('second_tablets: the bribe scan widened for 16:19\'s first entry; the file compiles')
