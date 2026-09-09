#!/usr/bin/env python3
"""world_journal.py — THE LOOP, step 1 THE SINK (owner-ruled PERMANENT 2026-09-09; the design: World/step9/THE_LOOP.md,
"Step 1 THE SINK — the design"; the probes: journal_probes.py, written first and run to fail).

The law engine's run log (World.log — seven classes: EVENT, WRITE, RETRO-WRITE, TIMER-SET, TIMER-FIRE, TIMER-CANCEL, MARKER)
written as ONE journal segment per world per run in the August envelope {s, op, layer, kind, subj, data, prov, chain}
(World/journal/worldledger.py — the envelope has one home; imported, never copied):
  s     the line's ordinal in the run            op    the clock day the line was logged at
  layer L3 (a run of the law engine)             kind  run.<class> — registered in World/journal/registers/event_kinds.yaml
  subj  the REGISTRY entity id (the payload's subject through World._registry; `clock` for a marker; `world` if none)
  data  the payload as it stands at the run's end, canonical JSON; a non-JSON leaf coerced to a string and COUNTED
  prov  {unit: the writing daemon (written_by, else source_law) / `tape` / `marker`, ref: the verse}
  chain sha256(previous + canon(event))[:16] from `genesis`
No timestamps. The segment lives in World/journal/data/ (derived, gitignored) or WORLD_JOURNAL_DIR when set.
The index (step 2, minimal): `--reindex` rebuilds World/journal/data/world.sqlite from EVERY segment on disk (L0, L1, L2, L3_*)
by worldledger.index_sqlite — drop-and-rebuild, never written directly. The gate: `--gate` runs the sequence runner twice in
two processes and demands byte-identical segments, verified chains, and an index whose counts equal the RUN tuple printed.
Run: python3 World/step9/world_journal.py --gate | --reindex | --verify <segment>
"""
import os, re, sys, glob, json, sqlite3, subprocess, tempfile, collections
HERE = os.path.dirname(os.path.abspath(__file__))
JOURNAL = os.path.normpath(os.path.join(HERE, '..', 'journal'))
sys.path.insert(0, JOURNAL)
from worldledger import Segment, index_sqlite, canon          # the August envelope, the chain, the index

KINDS = collections.OrderedDict([
    ('EVENT', 'run.event'), ('WRITE', 'run.write'), ('RETRO-WRITE', 'run.retro_write'), ('TIMER-SET', 'run.timer_set'),
    ('TIMER-FIRE', 'run.timer_fire'), ('TIMER-CANCEL', 'run.timer_cancel'), ('MARKER', 'run.marker')])
LAYER = 'L3'


def data_dir(out_dir=None):
    d = out_dir or os.environ.get('WORLD_JOURNAL_DIR') or os.path.join(JOURNAL, 'data')
    os.makedirs(d, exist_ok=True)
    return d


def _jsonable(x, coerced):
    """a JSON-safe copy of a payload; an unknown leaf becomes its string and is counted (the count must be zero on the tape)"""
    if isinstance(x, dict):
        return {str(k): _jsonable(v, coerced) for k, v in x.items()}
    if isinstance(x, (list, tuple)):
        return [_jsonable(v, coerced) for v in x]
    if x is None or isinstance(x, (str, int, float, bool)):
        return x
    coerced[type(x).__name__] += 1
    return str(x)


def segment_name(source):
    return 'L3_run_%s.jsonl' % re.sub(r'[^A-Za-z0-9_.-]+', '_', source)


def sink(world, source, out_dir=None):
    """write World.log as one L3 segment; returns (path, lines, coerced)"""
    seg = Segment(LAYER, source)
    reg = getattr(world, '_registry', None) or {}
    coerced = collections.Counter()
    for cls, day, payload in world.log:
        kind = KINDS[cls]
        if cls == 'MARKER':
            subj, unit, ref = 'clock', 'marker', payload.get('verse')
        else:
            s = payload.get('subject')
            subj = reg.get(s, s) if s is not None else 'world'
            if cls == 'EVENT':
                unit = 'tape'
            else:
                unit = payload.get('written_by') or payload.get('source_law')
            ref = payload.get('case_source')
        seg.append(kind, subj, _jsonable(payload, coerced), {'unit': unit, 'ref': ref}, op=day)
    path = os.path.join(data_dir(out_dir), segment_name(source))
    seg.write(path)
    return path, len(seg.events), sum(coerced.values())


def verify(path):
    return Segment.verify(path)


def index(db_path, paths):
    return index_sqlite(db_path, paths)


def counts(db_path):
    """{kind: n} over the run kinds in the index"""
    c = sqlite3.connect(db_path)
    rows = c.execute("SELECT kind, COUNT(*) FROM events WHERE kind LIKE 'run.%' GROUP BY kind").fetchall()
    c.close()
    return dict(rows)


def segments(out_dir=None):
    d = data_dir(out_dir)
    return sorted(p for layer in ('L0', 'L1', 'L2', 'L3') for p in glob.glob(os.path.join(d, layer + '_*.jsonl')))


def reindex(out_dir=None):
    """step 2, minimal: the index rebuilt from every segment on disk (drop-and-rebuild); returns (db, rows, segments)"""
    d = data_dir(out_dir)
    paths = segments(d)
    db = os.path.join(d, 'world.sqlite')
    n = index_sqlite(db, paths)
    return db, n, len(paths)


def _run_sequence(td):
    env = dict(os.environ, WORLD_JOURNAL_DIR=td)
    r = subprocess.run([sys.executable, os.path.join(HERE, 'cold_run_sequence.py')], cwd=HERE, env=env,
                       capture_output=True, text=True)
    if r.returncode != 0:
        raise SystemExit('THE GATE: the sequence runner failed (exit %d)\n%s' % (r.returncode, r.stdout[-2000:] + r.stderr[-2000:]))
    return r.stdout


def _tuple_of(stdout):
    """the RUN tuple as the runner prints it: events, markers; timers set, fired, cancelled; retro-writes; writes"""
    ev = re.search(r'THE TAPE: (\d+) events, (\d+) markers', stdout)
    tm = re.search(r'timers: set (\d+), fired (\d+), cancelled (\d+); retro-writes (\d+); writes (\d+)', stdout)
    if not (ev and tm):
        raise SystemExit('THE GATE: the RUN tuple was not found in the runner\'s print')
    return {'run.event': int(ev.group(1)), 'run.marker': int(ev.group(2)), 'run.timer_set': int(tm.group(1)),
            'run.timer_fire': int(tm.group(2)), 'run.timer_cancel': int(tm.group(3)), 'run.retro_write': int(tm.group(4)),
            'run.write': int(tm.group(5))}


def gate():
    """two processes, two directories: byte-identical segments, verified chains, the index's counts = the RUN tuple"""
    with tempfile.TemporaryDirectory() as t1, tempfile.TemporaryDirectory() as t2:
        out1 = _run_sequence(t1)
        out2 = _run_sequence(t2)
        want = _tuple_of(out1)
        if want != _tuple_of(out2):
            raise SystemExit('THE GATE: the two runs printed different RUN tuples')
        running = re.search(r'JOURNAL the running setting: (\S+) ', out1)
        if not running:
            raise SystemExit('THE GATE: the runner printed no JOURNAL line for the running setting')
        seg1 = sorted(glob.glob(os.path.join(t1, 'L3_*.jsonl')))
        ok = True
        print('THE LOOP — STEP 1\'S GATE: the sequence runner twice, in two processes and two directories')
        for p1 in seg1:
            p2 = os.path.join(t2, os.path.basename(p1))
            b1, b2 = open(p1, 'rb').read(), open(p2, 'rb').read() if os.path.exists(p2) else None
            same = b1 == b2
            chain = verify(p1) and (b2 is not None and verify(p2))
            lines = b1.count(b'\n') - 1
            print('  %-52s %6d lines  bytes %s  chain %s' % (os.path.basename(p1), lines, 'IDENTICAL' if same else 'DIFFER', 'VERIFIED' if chain else 'BROKEN'))
            ok = ok and same and chain
        db, n, k = reindex(t1)
        got = {kind: c for kind, c in counts(db).items()}
        run_seg = os.path.basename(running.group(1))
        # the running world's own counts: index that segment alone
        db_run = os.path.join(t1, 'running.sqlite')
        index(db_run, [os.path.join(t1, run_seg)])
        got_run = counts(db_run)
        for kind in want:
            got_run.setdefault(kind, 0)
        match = got_run == want
        print('  the index over all %d segments: %d rows; the running world\'s counts %s' % (k, n, 'MATCH the RUN tuple' if match else 'DIVERGE from the RUN tuple'))
        if not match:
            print('    index %s\n    tuple %s' % (got_run, want))
        ok = ok and match
        print('GATE %s — %s' % ('GREEN' if ok else 'RED', 'the replay is the audit, the running world is the instrument' if ok else 'read the lines above'))
        return ok


if __name__ == '__main__':
    if '--gate' in sys.argv:
        sys.exit(0 if gate() else 1)
    if '--reindex' in sys.argv:
        db, n, k = reindex()
        print('reindexed %s: %d rows from %d segments' % (db, n, k))
    elif '--verify' in sys.argv:
        p = sys.argv[sys.argv.index('--verify') + 1]
        print('%s: chain %s' % (p, 'VERIFIED' if verify(p) else 'BROKEN'))
        sys.exit(0 if verify(p) else 1)
    else:
        print(__doc__)
