#!/usr/bin/env python3
"""portable_probes.py — THE PORTABLE REPO fire-probes (2026-09-15; reviews/PORTABLE_repo_2026-09-15.md, decisions P1-P5), written BEFORE the
pass. Against the unchanged tree T1, T3, T4, T5 must FAIL; after the pass every probe must PASS. Five probes:
  T1 NO ABSOLUTE PATH — no tracked .py, .sh or .json under the repo carries the literal '<repo-old>' (ARCHITECTURE/ is the
     design thread's, read never edited — its carriers are counted apart and named, a debt handed to that thread)
  T2 EVERY TRACKED .py COMPILES
  T3 THE CLONE AT ANOTHER PATH — the tracked tree copied to a temporary folder (the store with it, the snapshot store copied as the
     fetch would bring it, the shelf symlinked, no derived data)
     and run THERE: cold_run_bamidbar.py green; World/build_world.py builds the one database from nothing and reconciles ALL GREEN;
     the tape 10/10; world_board.py --gate GREEN; checkpoint_positions.py --check GREEN
  T4 THE MANIFEST IS THE CHECK — Data/fetch_shelf.py --check: every file of the shelf matches its size and hash, none missing
  T5 THE FETCH IS REAL — Data/fetch_shelf.py --sample 2: two files fetched from Sefaria's export match their hashes
Not run by the sweep; run by hand at the sitting. Run: python3 World/step9/portable_probes.py [--quick]   (--quick skips T3 and T5)
"""
import os, sys, re, subprocess, tempfile, shutil, py_compile
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.normpath(os.path.join(HERE, '..', '..'))
OLD = '<repo-old>'
QUICK = '--quick' in sys.argv
results = []


def probe(name):
    def deco(fn):
        try:
            ok, note = fn()
        except BaseException as e:
            ok, note = False, '%s: %s' % (type(e).__name__, str(e)[:240])
        results.append((name, bool(ok), note))
        return fn
    return deco


def tracked():
    out = subprocess.run(['git', 'ls-files'], capture_output=True, text=True, cwd=ROOT).stdout
    return [l for l in out.split('\n') if l.strip()]


@probe("T1 no absolute path: no tracked .py, .sh or .json carries the literal old path")
def t1():
    bad, theirs = [], []
    TOOLS = ('World/step9/portable_probes.py', 'logic/solo_tools/portable_pass.py')   # the two whose job is to name the old path
    for f in tracked():
        if f.endswith(('.py', '.sh', '.json')) and f not in TOOLS:
            try:
                if OLD in open(os.path.join(ROOT, f), encoding='utf-8', errors='replace').read():
                    (theirs if f.startswith('ARCHITECTURE/') else bad).append(f)
            except IsADirectoryError:
                pass
    return not bad, '%d tracked code files carry the old path: %s; ARCHITECTURE/ (the design thread\'s) %d: %s' % (len(bad), bad[:6], len(theirs), theirs[:4])


@probe('T2 every tracked .py compiles')
def t2():
    bad = []
    for f in tracked():
        if f.endswith('.py'):
            try:
                compile(open(os.path.join(ROOT, f), encoding='utf-8', errors='replace').read(), f, 'exec')
            except Exception as e:
                bad.append('%s: %s' % (f, str(e)[:80]))
    return not bad, '%d files fail to compile: %s' % (len(bad), bad[:4])


def run_at(cwd, args, timeout=900):
    r = subprocess.run([sys.executable] + args, cwd=cwd, capture_output=True, text=True, timeout=timeout)
    tail = (r.stdout.strip().split('\n') or [''])[-1][:160]
    return r.returncode, tail, r.stdout + r.stderr


@probe('T3 the clone at another path: the tracked tree copied elsewhere, the store with it, the shelf symlinked; a runner, the builder, the tape, two gates run there')
def t3():
    if QUICK:
        return False, 'skipped under --quick (a FAIL by design: the clone is the proof)'
    d = tempfile.mkdtemp(prefix='torahsim_clone_')
    try:
        files = tracked()
        for f in files:
            src = os.path.join(ROOT, f)
            if os.path.isdir(src):
                continue
            dst = os.path.join(d, f)
            os.makedirs(os.path.dirname(dst), exist_ok=True)
            shutil.copy2(src, dst)
        store = os.path.join(d, 'Data', 'tanakh.sqlite')
        if not os.path.exists(store):
            return False, 'the clone has no Data/tanakh.sqlite — the store is not tracked (P2 not done)'
        for name in ('torah_grok.SNAPSHOT-main-51801ca.sqlite',):   # the stores too large for git — what `fetch_shelf.py --stores` brings a clone (P2 amended: the release asset), provided here from the repo
            src = os.path.join(ROOT, name)
            if not os.path.exists(src):
                return False, 'the snapshot store %s is not on this machine' % name
            shutil.copy2(src, os.path.join(d, name))
        shelf = os.path.join(d, 'Data', 'sefaria_export')
        shutil.rmtree(shelf, ignore_errors=True)
        os.symlink(os.path.join(ROOT, 'Data', 'sefaria_export'), shelf)
        steps = [('a runner', ['World/step9/cold_run_bamidbar.py'], lambda t, o: 'MISS' not in o.split('THE GRADE')[-1] if 'THE GRADE' in o else 'FAIL' not in t),
                 ('the builder', ['World/build_world.py'], lambda t, o: 'ALL GREEN' in o),
                 ('the tape', ['World/step9/cold_run_sequence.py'], lambda t, o: '10/10 checkpoints' in o),
                 ("the board's gate", ['World/step9/world_board.py', '--gate'], lambda t, o: 'GREEN' in t),
                 ("the positions' gate", ['World/step9/checkpoint_positions.py', '--check'], lambda t, o: 'GREEN' in t)]
        notes = []
        for name, args, okf in steps:
            code, tail, out = run_at(d, args)
            ok = code == 0 and okf(tail, out)
            notes.append('%s %s' % (name, 'ok' if ok else 'FAILED (%s)' % (tail or out.strip().split('\n')[-1][:120])))
            if not ok:
                return False, 'at %s: %s' % (d, '; '.join(notes))
        return True, 'at %s: %s' % (d, '; '.join(notes))
    finally:
        shutil.rmtree(d, ignore_errors=True)


@probe("T4 the manifest is the check: Data/fetch_shelf.py --check finds every file of the shelf matching, none missing")
def t4():
    code, tail, out = run_at(ROOT, ['Data/fetch_shelf.py', '--check'], timeout=1800)
    return code == 0 and 'GREEN' in tail, tail or out.strip().split('\n')[-1][:160]


@probe("T5 the fetch is real: Data/fetch_shelf.py --sample 2 fetches two files from Sefaria's export matching their hashes")
def t5():
    if QUICK:
        return False, 'skipped under --quick'
    code, tail, out = run_at(ROOT, ['Data/fetch_shelf.py', '--sample', '2'], timeout=600)
    return code == 0 and 'GREEN' in tail, tail or out.strip().split('\n')[-1][:160]


if __name__ == '__main__':
    ok = sum(1 for _, o, _ in results if o)
    print('THE PORTABLE REPO: the fire-probes%s' % (' (--quick)' if QUICK else ''))
    for name, o, note in results:
        print('  %s  %s\n        %s' % ('PASS' if o else 'FAIL', name, note))
    print('%d/%d probes' % (ok, len(results)))
    sys.exit(0 if ok == len(results) else 1)
