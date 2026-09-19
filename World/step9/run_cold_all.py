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
THE GATES CUT (2026-09-19; the owner: "Yes make that change. It's too long as it is" — the chain measured at ninety minutes, the sweep 2,007 s of it
sequential): the sweep runs its runners IN PARALLEL (--jobs N, default half the cores, at most 8 — each runner its own process, as before) and
INCREMENTALLY (--changed): the runners whose source moved since the last green sweep's STAMP (World/step9/sweep_stamp.json — every runner's hash and the
shared pieces' hashes, written only by a green sweep) plus every runner that IMPORTS them, transitively (the callers re-graded when a callee moves);
a shared piece moved (the engine, the effects layer, the guards, the journal, a registry) or no stamp = the FULL sweep. --skip name,name leaves named
runners out (the chain skips cold_run_sequence.py, whose full run is the chain's own first step). Nothing changed since the stamp = the stamp stands
(printed, exit 0; the stamp's date and count named). The dependency and daemon gates run first as before, whole.
"""
import glob, os, re, subprocess, sys, time, hashlib, json, concurrent.futures

HERE = os.path.dirname(os.path.abspath(__file__))
runners = sorted(glob.glob(os.path.join(HERE, 'cold_run_*.py')))
print('run_cold_all: %d runners discovered in %s' % (len(runners), HERE))

# THE DEPENDENCY GATE runs first (2026-09-06): every runner's span declared,
# every cross-reference the ink requires dispositioned, every CALL live. A
# runner that names another span's type without a disposition, or a call
# the dispositions file understates, fails the sweep before any cell runs.
gate = subprocess.run([sys.executable, os.path.join(HERE, 'dependency_census.py')],
                      cwd=HERE, capture_output=True, text=True)
print('\n'.join(l for l in gate.stdout.splitlines() if l.startswith('DEPENDENCY GATE')))
if gate.returncode != 0:
    print(gate.stdout[-3000:]); print(gate.stderr[-1000:])
    sys.exit('run_cold_all: THE DEPENDENCY GATE FAILED — no runner graded until every edge is dispositioned')
# THE DAEMON-EDGE GATE runs second (2026-09-07, D9-ii): every daemon declared
# with its watches equal to its parse, every watched and submitted event kind
# registered, every effect registered, every compiled function dispositioned
# (WRAPPED verified, OWED on the worklist), no daemon emitting an event.
dgate = subprocess.run([sys.executable, os.path.join(HERE, 'daemon_census.py')],
                       cwd=HERE, capture_output=True, text=True)
print('\n'.join(l for l in dgate.stdout.splitlines() if l.startswith('DAEMON GATE')))
if dgate.returncode != 0:
    print(dgate.stdout[-3000:]); print(dgate.stderr[-1000:])
    sys.exit('run_cold_all: THE DAEMON GATE FAILED — no runner graded until every daemon is declared and every function dispositioned')
if not runners:
    sys.exit('no cold_run_*.py found — refusing to report a clean sweep of nothing')

# ---- THE GATES CUT (2026-09-19): the selection (--changed against the stamp), the skips, the parallel run ----
STAMP = os.path.join(HERE, 'sweep_stamp.json')
SHARED = sorted(glob.glob(os.path.join(HERE, '*_vocabulary.yaml')) + glob.glob(os.path.join(HERE, '*_dispositions.yaml')) + glob.glob(os.path.join(HERE, 'calendar_parameters*.yaml')) + glob.glob(os.path.join(HERE, 'population_schema*.yaml'))
                + [os.path.join(HERE, f) for f in ('world_engine.py', 'effects_layer.py', 'compile_guards.py', 'world_journal.py')]
                + [os.path.normpath(os.path.join(HERE, '..', '..', 'logic', 'corpus', 'entity_registry.yaml'))])
SHARED = [p for p in SHARED if os.path.exists(p)]
def sha(p): return hashlib.sha256(open(p, 'rb').read()).hexdigest()
def importers_of(paths):
    """the reverse import graph: runner -> the runners that import it (the live edges: `import cold_run_X` / `from cold_run_X`)"""
    rev = {}
    for p in paths:
        src = open(p, encoding='utf-8', errors='ignore').read()
        for m in re.finditer(r'^\s*(?:import|from)\s+(cold_run_\w+)', src, re.M):
            rev.setdefault(m.group(1) + '.py', set()).add(os.path.basename(p))
    return rev
def argv_value(flag, default=None):
    if flag in sys.argv:
        i = sys.argv.index(flag); return sys.argv[i + 1] if i + 1 < len(sys.argv) else default
    return default
JOBS = int(argv_value('--jobs', str(min(8, max(1, (os.cpu_count() or 2) // 2)))))
SKIP = set(x for x in (argv_value('--skip', '') or '').split(',') if x)
mode = 'FULL'; selected = list(runners); reason = 'every runner'
stamp = json.load(open(STAMP, encoding='utf-8')) if os.path.exists(STAMP) else None
shared_now = {os.path.relpath(p, HERE): sha(p) for p in SHARED}
if '--changed' in sys.argv:
    if stamp is None:
        reason = 'no stamp at %s — the full sweep writes it' % STAMP
    else:
        shared_moved = sorted(k for k, v in shared_now.items() if stamp.get('shared', {}).get(k) != v)
        if shared_moved:
            reason = 'a shared piece moved since the stamp (%s): %s' % (stamp.get('when'), ', '.join(shared_moved[:6]))
        else:
            changed = sorted(os.path.basename(p) for p in runners if stamp.get('runners', {}).get(os.path.basename(p)) != sha(p))
            changed = [n for n in changed if n not in SKIP]   # a skipped runner is not in the stamp and never counts as moved
            rev = importers_of(runners); want = set(changed); frontier = list(changed)
            while frontier:
                x = frontier.pop()
                for caller in rev.get(x, ()):
                    if caller not in want: want.add(caller); frontier.append(caller)
            selected = [p for p in runners if os.path.basename(p) in want]; mode = 'CHANGED'
            reason = '%d runner(s) moved since the stamp (%s): %s; with their importers %d' % (len(changed), stamp.get('when'), ', '.join(changed[:8]), len(selected))
selected = [p for p in selected if os.path.basename(p) not in SKIP]
print('THE SWEEP %s (%s); jobs %d; skipped %s' % (mode, reason, JOBS, sorted(SKIP) or 'none'))
if not selected:
    print('run_cold_all: NOTHING TO GRADE — the stamp stands: %s runners green at %s (every source unmoved since)' % (len(stamp.get('runners', {})) if stamp else 0, stamp.get('when') if stamp else '?'))
    sys.exit(0)

# Every runner exits non-zero on a miss (its own sys.exit), so rc is the
# verdict; the score line is read for the report and, where present,
# must agree with itself (n/n). Score-line forms across the runners:
# "MATRIX: 40/40 cells", "18/18 cells", "24/24 checkpoints", "n/n match".
SCORE = re.compile(r'(\d+)\s*/\s*(\d+)\s*(?:cells|checkpoints|match|test)')
def run_one(path):
    name = os.path.basename(path)
    t0 = time.time()
    try:
        r = subprocess.run([sys.executable, path], cwd=HERE, capture_output=True,
                           text=True, timeout=900)
        out = r.stdout + r.stderr
        rc = r.returncode
    except subprocess.TimeoutExpired:
        out, rc = 'TIMEOUT', 124
    m = SCORE.findall(out)
    score = m[-1] if m else None   # the last score line is the runner's total
    ok = rc == 0 and (score is None or score[0] == score[1])
    return (name, ok, rc, score, out, time.time() - t0)
results = []
t_all = time.time()
with concurrent.futures.ThreadPoolExecutor(max_workers=JOBS) as pool:
    for name, ok, rc, score, out, dt in pool.map(run_one, selected):
        results.append((name, ok, rc, score, out, dt))
        print('%s  %-28s rc=%d  score=%s  %.1fs' % (
            'PASS' if ok else 'FAIL', name, rc,
            ('%s/%s' % score) if score else 'rc-only (no score line printed)', dt))

fails = [x for x in results if not x[1]]
cells = sum(int(x[3][0]) for x in results if x[3])
print()
print('run_cold_all: %d/%d runners green, %d graded cells in all (%s of %d; wall %.0f s, %d jobs)' % (
    len(results) - len(fails), len(results), cells, mode, len(runners), time.time() - t_all, JOBS))
for name, ok, rc, matrix, out, dt in fails:
    print('\n---- %s (rc=%d) tail ----' % (name, rc))
    print('\n'.join(out.splitlines()[-25:]))
if not fails:
    # THE STAMP — written by a green sweep only: the runners graded now carry their hashes, the rest keep the stamp's (unmoved by the selection's own test)
    new = {'when': time.strftime('%Y-%m-%d %H:%M'), 'mode': mode, 'jobs': JOBS, 'runners': dict((stamp or {}).get('runners', {})), 'shared': shared_now, 'graded': [x[0] for x in results]}
    for name, *_ in results: new['runners'][name] = sha(os.path.join(HERE, name))
    if mode == 'FULL':
        new['runners'] = {os.path.basename(p): sha(p) for p in runners if os.path.basename(p) not in SKIP} | {n: h for n, h in new['runners'].items() if n in SKIP}
    json.dump(new, open(STAMP, 'w', encoding='utf-8'), indent=0, sort_keys=True)
    print('the stamp written: %s (%d runners, %d shared pieces)' % (STAMP, len(new['runners']), len(new['shared'])))
sys.exit(1 if fails else 0)
