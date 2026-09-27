import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE DEUTERONOMY WALK 15b (LEAN): TWO CALLEES' HOLE SCANS WIDENED FROM THE SCAN CENSUS'S PRINT (ch17_scan_census.out, run after the tape's first run — 14b's lesson 2,
# the instrument used before the second run): (1) the seducers' SEDUCERS_SCAN (r'false_prophet\w*' on israel_people, its own five excluded) found this sitting's
# false_prophet_fear_barred — the tape's DE4 read it and DIVERGED (9/10) and the callee's import would fall; (2) the place-name callee's PLACE_SCAN (r'\w*the_place\w*'
# by the formula's words) found high_court_at_the_place_commanded. Each seat widened with the sitting's note; nothing else moves. patch_place_name_ch16.py's form. RUN FROM THE REPO ROOT.
import subprocess, re, py_compile
ROOT = _ROOT
W = 'THE DEUTERONOMY WALK 15b (2026-09-24; LEAN)'
# (1) seducers
P = ROOT + '/World/step9/cold_run_seducers.py'; s = open(P, encoding='utf-8').read()
old = "_ss = ledger_scan('israel_people', SEDUCER_WORDS); SEDUCERS_SCAN = None if _ss is None else [e for e in _ss if e not in OWN5]   # this sitting's own five excluded once the fold carries them"
assert s.count(old) == 1, s.count(old)
new = "CH17_FALSE_PROPHET = ('false_prophet_fear_barred',)   # %s: chapters 17-18's name carrying the false prophet (18:22's 'you shall not fear him')\n_ss = ledger_scan('israel_people', SEDUCER_WORDS); SEDUCERS_SCAN = None if _ss is None else [e for e in _ss if e not in OWN5 and e not in CH17_FALSE_PROPHET]   # %s: chapters 17-18's false_prophet_fear_barred excluded — a later chapter's write moved this scan's ground once the tape's first run put it in the one database (the scan census's print; the tape's DE4 read this scan and diverged 9/10 — the same lesson as 14b's place-name seat)" % (W, W)
s = s.replace(old, new); open(P, 'w', encoding='utf-8').write(s); py_compile.compile(P, doraise=True)
# (2) place_name
P2 = ROOT + '/World/step9/cold_run_place_name.py'; t = open(P2, encoding='utf-8').read()
old2 = "PLACE_SCAN = None if _ps is None else [e for e in _ps if e not in OWN7 and e not in CH16_AT_THE_PLACE]   # THE DEUTERONOMY WALK 14b (2026-09-23; LEAN):"
assert t.count(old2) == 1, t.count(old2)
new2 = "PLACE_SCAN = None if _ps is None else [e for e in _ps if e not in OWN7 and e not in CH16_AT_THE_PLACE and e not in CH17_AT_THE_PLACE]   # %s: chapters 17-18's high_court_at_the_place_commanded excluded too (the scan census's print — the third chapter to move this seat); 14b's note follows:   # THE DEUTERONOMY WALK 14b (2026-09-23; LEAN):" % W
t = t.replace(old2, new2)
old3 = "CH16_AT_THE_PLACE = ('passover_at_the_place_commanded', 'weeks_at_the_place_commanded', 'booths_at_the_place_commanded', 'passover_in_the_gates_barred')"
assert t.count(old3) == 1, t.count(old3)
t = t.replace(old3, old3 + "\nCH17_AT_THE_PLACE = ('high_court_at_the_place_commanded', 'levite_service_at_the_place_permitted')   # %s: chapters 17-18's names carrying the place (17:8's high court, 18:6-7's Levite at the place)" % W)
open(P2, 'w', encoding='utf-8').write(t); py_compile.compile(P2, doraise=True)
print('widened: seducers SEDUCERS_SCAN (false_prophet_fear_barred excluded), place_name PLACE_SCAN (high_court_at_the_place_commanded, levite_service_at_the_place_permitted excluded); both compile')
