import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE DEUTERONOMY WALK 14b (LEAN): the place-name callee's hole scan (PLACE_SCAN — the effects naming the place, the gates … on Israel, its own seven excluded) found
# chapter 16's passover_at_the_place_commanded and weeks_at_the_place_commanded once the tape's first run had written them into the one database (the third tape run
# stopped at its import); the scan census (ch16_scan_census.py) showed this the one remaining seat. Chapter 16's names excluded with the sitting's note; nothing else moves. RUN FROM THE REPO ROOT.
import subprocess, re
ROOT = _ROOT
P = ROOT + '/World/step9/cold_run_place_name.py'
s = open(P, encoding='utf-8').read()
m = re.search(r"^_ps = ledger_scan\('israel_people', PLACE_WORDS\); PLACE_SCAN = None if _ps is None else \[e for e in _ps if e not in OWN7\]   # this sitting's own seven excluded once the fold carries them", s, re.M)
assert m, 'the PLACE_SCAN statement (its form read at the grep)'
new = "_ps = ledger_scan('israel_people', PLACE_WORDS); PLACE_SCAN = None if _ps is None else [e for e in _ps if e not in OWN7 and e not in CH16_AT_THE_PLACE]   # THE DEUTERONOMY WALK 14b (2026-09-23; LEAN): chapter 16's own statuses at the place (passover_at_the_place_commanded, weeks_at_the_place_commanded, booths_at_the_place_commanded) and its gates' bar excluded — a later chapter's writes moved this scan's ground once the tape's first run put them in the one database (the same lesson at the second-tablets callee's two seats)"
s = s[:m.start()] + "CH16_AT_THE_PLACE = ('passover_at_the_place_commanded', 'weeks_at_the_place_commanded', 'booths_at_the_place_commanded', 'passover_in_the_gates_barred')   # THE DEUTERONOMY WALK 14b (2026-09-23): chapter 16's names carrying the place and the gates\n" + new + s[m.end():]
open(P, 'w', encoding='utf-8').write(s)
import py_compile; py_compile.compile(P, doraise=True); print('place_name: chapter 16\'s four names excluded from PLACE_SCAN; the file compiles')
