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
    ('TIMER-FIRE', 'run.timer_fire'), ('TIMER-CANCEL', 'run.timer_cancel'), ('MARKER', 'run.marker'),
    ('SKIP', 'run.skip')])       # THE LOOP step 3 (2026-09-09): the eighth class — a daemon not called, its law not in force (the from_event setting)
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


def _append_log(seg, world, log, coerced):
    """the log's lines into a segment — the sink's one conversion (THE LOOP step 4 factors it out for the cursor's audit and append)"""
    reg = getattr(world, '_registry', None) or {}
    for cls, day, payload in log:
        kind = KINDS[cls]
        if cls == 'MARKER':
            subj, unit, ref = 'clock', 'marker', payload.get('verse')
        else:
            s = payload.get('subject')
            subj = reg.get(s, s) if s is not None else 'world'
            if cls == 'EVENT':
                unit = 'scenario' if payload.get('scenario') else 'tape'   # THE LOOP step 5 (2026-09-09): a labeled hypothetical is told from the text's act
            elif cls == 'SKIP':
                unit = payload.get('daemon')          # step 3: the daemon not called — "who was skipped" beside "who wrote this"
            else:
                unit = payload.get('written_by') or payload.get('source_law')
            ref = payload.get('case_source')
        seg.append(kind, subj, _jsonable(payload, coerced), {'unit': unit, 'ref': ref}, op=day)


def sink(world, source, out_dir=None):
    """write World.log as one L3 segment; returns (path, lines, coerced)"""
    seg = Segment(LAYER, source)
    coerced = collections.Counter()
    _append_log(seg, world, world.log, coerced)
    path = os.path.join(data_dir(out_dir), segment_name(source))
    seg.write(path)
    return path, len(seg.events), sum(coerced.values())


# ---- THE LOOP step 4 THE CURSOR and step 5 SCENARIOS (2026-09-09; THE_LOOP.md "Step 4 THE CURSOR — the design", "Step 5 SCENARIOS — the
# ---- design"; the probes cursor_probes.py written first): the audit, the append, the labeled hypothetical ----
BASE_SEGMENT = segment_name(RUNNING_WORLD) if False else 'L3_run_cold_run_sequence_seed_isaac.jsonl'   # the running world's base segment on disk


def cursor_segment(world, fork, verse, out_dir=None, base=None):
    """THE AUDIT AND THE APPEND (D9): the world's first `fork` log lines, converted, must be byte-identical to the base segment's
    first `fork` event lines (same events, same chains — the replay reproduces the run or the cursor is REFUSED); the lines AFTER
    the fork are written as a new segment L3_run_cursor_<verse>.jsonl whose chain CONTINUES from the base's chain at the fork and
    whose header names the base, the fork and the cursor verse. The base is never rewritten. Returns (path, appended lines)."""
    base = base or os.path.join(data_dir(out_dir), BASE_SEGMENT) if os.path.exists(os.path.join(data_dir(out_dir), BASE_SEGMENT)) else (base or os.path.join(data_dir(), BASE_SEGMENT))
    coerced = collections.Counter()
    audit = Segment(LAYER, RUNNING_WORLD)
    _append_log(audit, world, world.log[:fork], coerced)
    with open(base, encoding='utf-8') as f:
        base_lines = f.read().split('\n')
    mine = [canon(ev) for ev in audit.events]
    if mine != base_lines[1:fork + 1]:
        first = next((i for i, (a, b) in enumerate(zip(mine, base_lines[1:fork + 1])) if a != b), min(len(mine), len(base_lines) - 1))
        raise SystemExit('CURSOR REFUSED: the replayed prefix differs from the base segment %s at event %d of %d — the base or the engine has '
                         'moved; rerun the tape (cold_run_sequence.py), then resume' % (os.path.basename(base), first + 1, fork))
    start = audit.events[-1]['chain'] if audit.events else None
    seg = Segment(LAYER, 'cold_run_sequence/cursor@%s' % verse, start_chain=start,
                  header={'base': os.path.basename(base), 'fork': fork, 'cursor': verse})
    _append_log(seg, world, world.log[fork:], coerced)
    path = os.path.join(data_dir(out_dir), 'L3_run_cursor_%s.jsonl' % re.sub(r'[^A-Za-z0-9_.-]+', '_', verse))
    seg.write(path)
    return path, len(seg.events)


def scenario(world, event, label):
    """step 5: a registered CASE event submitted on a live world as a labeled hypothetical — the journal's EVENT line carries prov.unit
    'scenario' and the label in its data; returns the daemons' fire count"""
    ev = dict(event)
    ev['scenario'] = label
    return world.submit(ev)


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
    """step 2: the index rebuilt from every segment on disk (drop-and-rebuild), the four run views created over it; returns
    (db, rows, segments)"""
    d = data_dir(out_dir)
    paths = segments(d)
    db = os.path.join(d, 'world.sqlite')
    n = index_sqlite(db, paths)
    views(db)
    return db, n, len(paths)


# ---- THE LOOP step 2's remainder (2026-09-09; THE_LOOP.md "Step 2 THE INDEX — the remainder", D7/D8): the four views, their gate,
# ---- the four questions ----
VIEWS_SQL = os.path.join(JOURNAL, 'run_views.sql')
RUNNING_WORLD = 'cold_run_sequence/seed_isaac'      # the running setting's segment — the ask-tool's default world (--world overrides)
OPEN_OPS = ('debit', 'heaven', 'body')               # the ledger ops whose entries open and close (World._write's own rule)
_VERSE_HEAD = re.compile(r'^\s*(\d?\s?[A-Za-z]+)\s+(\d+):(\d+)')


def views(db_path):
    """create the four run views over the events table from World/journal/run_views.sql (drop-and-create)"""
    sql = open(VIEWS_SQL, encoding='utf-8').read()
    c = sqlite3.connect(db_path)
    try:
        c.executescript(sql)
        c.commit()
    finally:
        c.close()


def view_counts(db_path):
    """per source: the events table's own counts beside each view's — the gate derives every expected count from the table"""
    c = sqlite3.connect(db_path)
    try:
        out = collections.OrderedDict()
        for (src,) in c.execute("select distinct source from events where layer = 'L3' order by source"):
            k = dict(c.execute("select kind, count(*) from events where source = ? group by kind", (src,)).fetchall())
            v = {'writes': k.get('run.write', 0) + k.get('run.retro_write', 0), 'sets': k.get('run.timer_set', 0),
                 'fires': k.get('run.timer_fire', 0), 'cancels': k.get('run.timer_cancel', 0), 'markers': k.get('run.marker', 0),
                 'skips': k.get('run.skip', 0)}
            v['ledger'] = c.execute("select count(*) from run_ledger where source = ?", (src,)).fetchone()[0]
            v['timers'] = c.execute("select count(*) from run_timers where source = ?", (src,)).fetchone()[0]
            by = dict(c.execute("select outcome, count(*) from run_timers where source = ? group by outcome", (src,)).fetchall())
            v['fired'], v['cancelled'], v['pending'] = by.get('fired', 0), by.get('cancelled', 0), by.get('pending', 0)
            v['clock'] = c.execute("select count(*) from run_clock where source = ?", (src,)).fetchone()[0]
            v['docket'] = c.execute("select count(*) from run_docket where source = ?", (src,)).fetchone()[0]
            v['docket_open'] = c.execute("select count(*) from run_docket where source = ? and open = 1", (src,)).fetchone()[0]
            v['docket_from_ledger'] = c.execute("select count(*) from run_ledger where source = ? and effect = 'declaration_owed'", (src,)).fetchone()[0]
            out[src] = v
        return out
    finally:
        c.close()


def views_gate(db_path):
    """every view's row count equals what the events table says it must be, on every source: (ok, lines)"""
    ok, lines = True, []
    for src, v in view_counts(db_path).items():
        checks = [('ledger', v['ledger'], v['writes']), ('timers', v['timers'], v['sets']), ('fired', v['fired'], v['fires']),
                  ('cancelled', v['cancelled'], v['cancels']), ('clock', v['clock'], v['markers']), ('docket', v['docket'], v['docket_from_ledger'])]
        bad = [(n, got, want) for n, got, want in checks if got != want]
        ok = ok and not bad
        lines.append('  %-44s ledger %5d = writes %5d | timers %4d = sets %4d (fired %d = fires %d, cancelled %d = cancels %d, pending %d) | clock %4d = markers %4d | docket %d (open %d) | skips %d  %s'
                     % (src, v['ledger'], v['writes'], v['timers'], v['sets'], v['fired'], v['fires'], v['cancelled'], v['cancels'], v['pending'],
                        v['clock'], v['markers'], v['docket'], v['docket_open'], v['skips'], 'MATCH' if not bad else 'DIVERGE %s' % bad))
    if not lines:
        ok, lines = False, ['  no L3 source in the index — ZERO-REPORT']
    return ok, lines


def _rows(c, sql, args=()):
    c.row_factory = sqlite3.Row
    return [dict(r) for r in c.execute(sql, args).fetchall()]


def _state(r, day):
    """an entry's state as of a day: open-capable ops are open until their day_closed is at or before the day; others are written"""
    if r['ledger_op'] not in OPEN_OPS:
        return 'written'
    dc = r['day_closed']
    return 'closed' if (dc is not None and (day is None or dc <= day)) else 'open'


def _verse_day(c, source, verse):
    """the day a verse sits at in a run: the first marker or event whose ref opens with the verse (not a longer verse number)"""
    m = _VERSE_HEAD.match(verse or '')
    if not m:
        raise SystemExit('ASK: %r is not a verse' % verse)
    head = '%s %s:%s' % (m.group(1), m.group(2), m.group(3))
    pat = re.compile(r'^\s*' + re.escape(head) + r'(?!\d)')
    days = [op for op, ref in c.execute("select op, ref from events where source = ? and kind in ('run.marker', 'run.event') and ref like ? order by seq",
                                        (source, head + '%')) if pat.match(ref or '')]
    if not days:
        raise SystemExit('ASK: no marker or event at %s in %s' % (head, source))
    return days[0]


def ask(db_path, question, *args, source=None):
    """THE FOUR QUESTIONS over the views — 'ledger' <entity> [<day>]; 'open' <verse>; 'who' <entity> <effect>; 'custody';
    each a list of dict rows; the world is `source` (the running setting's world by default)"""
    source = source or RUNNING_WORLD
    c = sqlite3.connect(db_path)
    try:
        if not c.execute("select 1 from events where source = ? limit 1", (source,)).fetchone():
            raise SystemExit('ASK: no rows for the world %r in %s (the worlds: %s)' % (source, db_path, ', '.join(
                s for (s,) in c.execute("select distinct source from events where layer = 'L3'"))))
        if question == 'ledger':
            entity, day = args[0], (int(args[1]) if len(args) > 1 and args[1] is not None else None)
            rows = _rows(c, "select * from run_ledger where source = ? and entity = ? and (? is null or day_written <= ?) order by seq",
                         (source, entity, day, day))
            for r in rows:
                r['state'] = _state(r, day)
            return rows
        if question == 'open':
            day = _verse_day(c, source, args[0])
            rows = _rows(c, "select * from run_ledger where source = ? and ledger_op in (?,?,?) and day_written <= ? and (day_closed is null or day_closed > ?) order by entity, seq",
                         (source, OPEN_OPS[0], OPEN_OPS[1], OPEN_OPS[2], day, day))
            for r in rows:
                r['state'], r['as_of_day'] = 'open', day
            return rows
        if question == 'who':
            entity, effect = args[0], args[1]
            rows = _rows(c, "select entity, effect, written_by, verse, day_written as day, value, kind from run_ledger where source = ? and entity = ? and effect = ? order by seq",
                         (source, entity, effect))
            return rows
        if question == 'custody':
            return _rows(c, "select * from run_docket where source = ? and open = 1 order by seq", (source,))
        raise SystemExit('ASK: the questions are ledger <entity> [<day>], open <verse>, who <entity> <effect>, custody')
    finally:
        c.close()


def _print_rows(rows):
    if not rows:
        print('  (no rows)'); return
    keys = [k for k in rows[0] if k not in ('source', 'kind')]
    for r in rows:
        print('  ' + ' | '.join('%s=%s' % (k, r[k]) for k in keys if r[k] is not None))


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
    tm = re.search(r'timers: set (\d+), fired (\d+), cancelled (\d+); retro-writes (\d+); writes (\d+); skipped (\d+)', stdout)
    if not (ev and tm):
        raise SystemExit('THE GATE: the RUN tuple was not found in the runner\'s print')
    return {'run.event': int(ev.group(1)), 'run.marker': int(ev.group(2)), 'run.timer_set': int(tm.group(1)),
            'run.timer_fire': int(tm.group(2)), 'run.timer_cancel': int(tm.group(3)), 'run.retro_write': int(tm.group(4)),
            'run.write': int(tm.group(5)), 'run.skip': int(tm.group(6))}      # step 3: the eighth class counted (0 under boot)


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
        # step 2's remainder (2026-09-09): the four views' counts derived from the events table's own, on every world
        vok, vlines = views_gate(db)
        print('  THE FOUR RUN VIEWS (run_ledger, run_timers, run_clock, run_docket) — every count against the table\'s:')
        print('\n'.join(vlines))
        ok = ok and vok
        print('GATE %s — %s' % ('GREEN' if ok else 'RED', 'the replay is the audit, the running world is the instrument' if ok else 'read the lines above'))
        return ok


if __name__ == '__main__':
    if '--gate' in sys.argv:
        sys.exit(0 if gate() else 1)
    if '--views' in sys.argv:                                  # step 2's remainder: the four views' counts against the table's, per world
        db = os.path.join(data_dir(), 'world.sqlite')
        views(db)
        ok, lines = views_gate(db)
        print('THE FOUR RUN VIEWS over %s (run_ledger, run_timers, run_clock, run_docket — World/journal/run_views.sql):' % db)
        print('\n'.join(lines))
        print('VIEWS GATE: %s' % ('every view count equals the events table\'s own on every world [gate satisfied]' if ok else 'DIVERGE — read the line'))
        sys.exit(0 if ok else 1)
    if '--ask' in sys.argv:                                    # step 2's remainder: the four questions
        i = sys.argv.index('--ask')
        rest = sys.argv[i + 1:]
        world = None
        if '--world' in rest:
            j = rest.index('--world'); world = rest[j + 1]; rest = rest[:j] + rest[j + 2:]
        db = os.path.join(data_dir(), 'world.sqlite')
        rows = ask(db, rest[0], *rest[1:], source=world)
        print('ASK %s %s — the world %s: %d rows' % (rest[0], ' '.join(rest[1:]), world or RUNNING_WORLD, len(rows)))
        _print_rows(rows)
        sys.exit(0)
    if '--reindex' in sys.argv:
        db, n, k = reindex()
        print('reindexed %s: %d rows from %d segments; the four views created' % (db, n, k))
    elif '--verify' in sys.argv:
        p = sys.argv[sys.argv.index('--verify') + 1]
        print('%s: chain %s' % (p, 'VERIFIED' if verify(p) else 'BROKEN'))
        sys.exit(0 if verify(p) else 1)
    else:
        print(__doc__)
