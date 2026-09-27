import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE DEUTERONOMY WALK 15b (LEAN): THE ONE STALE LITERAL RETYPED FROM THE TAPE'S PRINT (14b's DD4 twin — the grep decided): the tape's DE4 (chapter 13's holes)
# scans israel_people's effect NAMES by substring ('false_prophet', …) and read this sitting's false_prophet_fear_barred (18:22) — a later chapter's write moved
# the tape's own scan; the name excluded with the sitting's note; the checkpoint's text amended; nothing else moves. patch_tape_dd4_ch16.py's form. RUN FROM THE REPO ROOT.
import subprocess, py_compile
ROOT = _ROOT
P = ROOT + '/World/step9/cold_run_sequence.py'; s = open(P, encoding='utf-8').read()
old = "    holes_se = sorted({e['effect'] for e in LG('israel') if any(t in e['effect'] for t in ('false_prophet', 'tested_by', 'hears_and_fears', 'condemned_city', 'devoted_thing'))})\n"
assert s.count(old) == 1, s.count(old)
new = "    holes_se = sorted({e['effect'] for e in LG('israel') if any(t in e['effect'] for t in ('false_prophet', 'tested_by', 'hears_and_fears', 'condemned_city', 'devoted_thing')) and e['effect'] not in ('false_prophet_fear_barred',)})   # THE DEUTERONOMY WALK 15b (2026-09-24; LEAN): 18:22's false_prophet_fear_barred excluded — the substring 'false_prophet' matched a later chapter's name once the tape's first run wrote it (the tape's own scan moved by a later chapter's write — 14b's DD4 twin; the extended scan census missed this tuple form and was widened to it)\n"
s = s.replace(old, new)
old2 = "cp('DE4 THE HOLES — the effects naming the false prophet\\'s hearing, the LORD\\'s testing, Israel\\'s hearing and fearing, the condemned city\\'s inquiry or the devoted thing\\'s cleaving on israel_people are this sitting\\'s FIVE ALONE"
assert s.count(old2) == 1, s.count(old2)
s = s.replace(old2, "cp('DE4 THE HOLES — the effects naming the false prophet\\'s hearing, the LORD\\'s testing, Israel\\'s hearing and fearing, the condemned city\\'s inquiry or the devoted thing\\'s cleaving on israel_people are this sitting\\'s FIVE ALONE (THE DEUTERONOMY WALK 15b: 18:22\\'s false_prophet_fear_barred excluded from the substring scan — a later chapter\\'s name)")
open(P, 'w', encoding='utf-8').write(s); py_compile.compile(P, doraise=True)
print('DE4 retyped: false_prophet_fear_barred excluded from the tape\'s own substring scan, the text amended; the file compiles')
