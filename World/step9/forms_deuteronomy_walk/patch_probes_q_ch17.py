import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE DEUTERONOMY WALK 15b (LEAN): ONE PROBE SEAT RETYPED FROM THE WIDENED SCAN CENSUS'S PRINT BEFORE THE CHAIN (ch17_scan_census3.out — readback_probes.py line 552,
# entity name, pattern 'false_prophet'): chapter 13's holes probe scans israel_people's effect NAMES by a tuple of substrings and would read this sitting's
# false_prophet_fear_barred (18:22) — 14b's Q33 twin, found by the census here rather than by the chain's first pass; the name excluded with the note; nothing else moves. RUN FROM THE REPO ROOT.
import subprocess, re, py_compile
ROOT = _ROOT
P = ROOT + '/World/step9/readback_probes.py'; s = open(P, encoding='utf-8').read()
old = "    holes = sorted({e['effect'] for e in (isr.ledger if isr else []) if any(t in e['effect'] for t in ('false_prophet', 'tested_by', 'hears_and_fears', 'condemned_city', 'devoted_thing'))})\n"
assert s.count(old) == 1, s.count(old)
i = s.index(old); q = re.findall(r'^def (q\d+)\(\):', s[:i], re.M)[-1]
new = "    holes = sorted({e['effect'] for e in (isr.ledger if isr else []) if any(t in e['effect'] for t in ('false_prophet', 'tested_by', 'hears_and_fears', 'condemned_city', 'devoted_thing')) and e['effect'] not in ('false_prophet_fear_barred',)})   # THE DEUTERONOMY WALK 15b (2026-09-24; LEAN): 18:22's false_prophet_fear_barred excluded — a later chapter's name under the substring 'false_prophet' (the widened scan census's print, retyped BEFORE the chain; the tape's DE4 the same seat)\n"
s = s.replace(old, new); open(P, 'w', encoding='utf-8').write(s); py_compile.compile(P, doraise=True)
print('readback_probes %s: false_prophet_fear_barred excluded from the chapter-13 holes scan; the file compiles' % q)
