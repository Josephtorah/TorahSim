#!/usr/bin/env python3
"""run_cold_all.py — run EVERY cold-compiled runner in this directory and
report one line each (REVIEW_LEV1-8 item K, 2026-09-05, sitting A).

"Cold runners clean" used to come from an ad-hoc shell line; this makes
the green reproducible. Each cold_run_*.py runs as its own process from
this directory; a runner passes when it exits 0 AND prints a MATRIX
line whose two numbers agree (n/n). The list is discovered by glob, so
a new compile joins the sweep the day it lands. Coverage line printed
first (a report of zero is worth only the coverage line above it).

Run: python3 World/step9/run_cold_all.py   (from anywhere)
Exit 1 if any runner fails; the failing runner's tail is printed.
"""
import glob, os, re, subprocess, sys, time

HERE = os.path.dirname(os.path.abspath(__file__))
runners = sorted(glob.glob(os.path.join(HERE, 'cold_run_*.py')))
print('run_cold_all: %d runners discovered in %s' % (len(runners), HERE))
if not runners:
    sys.exit('no cold_run_*.py found — refusing to report a clean sweep of nothing')

# Every runner exits non-zero on a miss (its own sys.exit), so rc is the
# verdict; the score line is read for the report and, where present,
# must agree with itself (n/n). Score-line forms across the runners:
# "MATRIX: 40/40 cells", "18/18 cells", "24/24 checkpoints", "n/n match".
SCORE = re.compile(r'(\d+)\s*/\s*(\d+)\s*(?:cells|checkpoints|match|test)')
results = []
for path in runners:
    name = os.path.basename(path)
    t0 = time.time()
    try:
        r = subprocess.run([sys.executable, path], cwd=HERE, capture_output=True,
                           text=True, timeout=600)
        out = r.stdout + r.stderr
        rc = r.returncode
    except subprocess.TimeoutExpired:
        out, rc = 'TIMEOUT', 124
    m = SCORE.findall(out)
    score = m[-1] if m else None   # the last score line is the runner's total
    ok = rc == 0 and (score is None or score[0] == score[1])
    results.append((name, ok, rc, score, out, time.time() - t0))
    print('%s  %-28s rc=%d  score=%s  %.1fs' % (
        'PASS' if ok else 'FAIL', name, rc,
        ('%s/%s' % score) if score else 'rc-only (no score line printed)',
        time.time() - t0))

fails = [x for x in results if not x[1]]
cells = sum(int(x[3][0]) for x in results if x[3])
print()
print('run_cold_all: %d/%d runners green, %d graded cells in all' % (
    len(results) - len(fails), len(results), cells))
for name, ok, rc, matrix, out, dt in fails:
    print('\n---- %s (rc=%d) tail ----' % (name, rc))
    print('\n'.join(out.splitlines()[-25:]))
sys.exit(1 if fails else 0)
