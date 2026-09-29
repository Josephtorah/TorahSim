import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
"""patch_sweep_timeout_ch32b.py — THE DEUTERONOMY WALK 20b's tail (2026-09-29): THE SWEEP'S PER-RUNNER LIMIT RAISED. run_cold_all.py bounded one runner's run at
900 s (set at the gates cut, 2026-09-19); the chain's third pass at 20b fell there on the song's runner alone (rc=124, 75/76 green): under INK_CACHE=0 a runner's
time is its callees' FULL loads — covenant_return_charge 790.9 s, firstfruits_ebal_curses 596.5 s, persons_poor_court 417.3 s, the song's forty-two callees past
900. The limit becomes --timeout N (the default 2400 s), a dated comment; nothing the tape, the probes or the sweep's stamp read moves. --check prints only."""
import re, sys, subprocess, py_compile
ROOT = _ROOT
P = f'{ROOT}/World/step9/run_cold_all.py'; CHECK = '--check' in sys.argv
s = open(P, encoding='utf-8').read()
OLD1 = "text=True, timeout=900, env=dict(os.environ, INK_CACHE='0'))"; assert s.count(OLD1) == 1
s2 = s.replace(OLD1, "text=True, timeout=TIMEOUT, env=dict(os.environ, INK_CACHE='0'))")
OLD2 = "JOBS = int(argv_value('--jobs', str(min(8, max(1, (os.cpu_count() or 2) // 2)))))\n"; assert s2.count(OLD2) == 1
s2 = s2.replace(OLD2, OLD2 + "TIMEOUT = int(argv_value('--timeout', '2400'))   # THE DEUTERONOMY WALK 20b (2026-09-29): one runner's bound — 900 s from the gates cut until the song's runner (forty-two callees) ran past it under INK_CACHE=0 at 20b's third pass (rc=124; covenant_return_charge 790.9 s, firstfruits_ebal_curses 596.5 s beside it): a runner's sweep time is its callees' full loads\n")
OLD3 = "runners out (the chain skips cold_run_sequence.py, whose full run is the chain's own first step)."; assert s2.count(OLD3) == 1
s2 = s2.replace(OLD3, OLD3 + " --timeout N (default 2400 s; 900 until 2026-09-29) bounds one runner's run — the song's\nrunner with forty-two callees ran past 900 s under INK_CACHE=0 at sitting 20b's third pass: a runner's sweep time is its callees' full loads.")
compile(s2, P, 'exec')
if CHECK: print('the sweep limit 900 -> 2400 (--timeout N); three edits | CHECK ONLY')
else:
    open(P, 'w', encoding='utf-8').write(s2); py_compile.compile(P, doraise=True); print('the sweep limit 900 -> 2400 (--timeout N); three edits | WRITTEN')
