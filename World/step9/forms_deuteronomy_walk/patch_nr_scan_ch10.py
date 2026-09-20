import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE DEUTERONOMY WALK 8b (2026-09-20): AN OLDER RUNNER'S HOLE-GROUND SCAN BROKEN BY A LATER SITTING'S WRITE — the tape's second run fell at IMPORT (ch10_tape2's first
# attempt): cold_run_not_righteousness.py scans the one database at import for stiff / neck / nape on Israel and asserts the scan EMPTY (7b's decision 2 — the stiff
# neck a STATE in the first telling, no write), and the tape's first run of this sitting sealed stiffening_barred on israel_people into the one database ('your neck
# you shall not stiffen any more', 10:16 — THE COMMAND, a block: the chapter's one prohibition), whose value names the neck. The state's ground stands as of 7b's own
# sitting: the scan now EXCLUDES the later sitting's effect once the fold carries it (7b's own lesson 10 on the peril's scan, applied to an older runner by the sitting
# that wrote after it); the sequence file's DA6 (the same scan on the running world) excludes it too. Idempotent.
import subprocess
ROOT = _ROOT
P = ROOT + '/World/step9/cold_run_not_righteousness.py'
s = open(P, encoding='utf-8').read()
old = "STIFF_SCAN = ledger_scan('israel_people', STIFF_WORDS)\n"
if s.count(old) == 1:
    s = s.replace(old, "_stiff = ledger_scan('israel_people', STIFF_WORDS)\nSTIFF_SCAN = None if _stiff is None else [e for e in _stiff if e != 'stiffening_barred']   # THE DEUTERONOMY WALK 8b (2026-09-20): chapter 10's own write EXCLUDED once the fold carries it — 'your neck you shall not stiffen any more' (10:16) the COMMAND, a block on Israel, its value naming the neck; the STATE of Exodus 32:9 still on no entry: the ground of 7b's decision 2 stands as of its own sitting (the peril's form, 7b's lesson 10, applied to an older runner by the sitting that wrote after it)\n")
    open(P, 'w', encoding='utf-8').write(s)
assert "STIFF_SCAN = None if _stiff is None else [e for e in _stiff if e != 'stiffening_barred']" in open(P, encoding='utf-8').read()
import py_compile; py_compile.compile(P, doraise=True)
P2 = ROOT + '/World/step9/cold_run_sequence.py'
s = open(P2, encoding='utf-8').read()
old2 = "    st_nr = sorted({e['effect'] for e in LG('israel') if re.search(cold_run_not_righteousness.STIFF_WORDS, '%s %s' % (e['effect'], e.get('value', '')), re.I)})\n"
if s.count(old2) == 1:
    s = s.replace(old2, "    st_nr = sorted({e['effect'] for e in LG('israel') if e['effect'] != 'stiffening_barred' and re.search(cold_run_not_righteousness.STIFF_WORDS, '%s %s' % (e['effect'], e.get('value', '')), re.I)})   # THE DEUTERONOMY WALK 8b (2026-09-20): chapter 10's stiffening_barred (the command on the neck) excluded — the state's ground stands as of 7b\n")
    open(P2, 'w', encoding='utf-8').write(s)
assert "if e['effect'] != 'stiffening_barred' and re.search(cold_run_not_righteousness.STIFF_WORDS" in open(P2, encoding='utf-8').read()
py_compile.compile(P2, doraise=True)
print('patched: cold_run_not_righteousness.py STIFF_SCAN excludes stiffening_barred; DA6 the same; both compile')
