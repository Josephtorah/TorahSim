#!/usr/bin/env python3
"""world_journal.py — THE LOOP, step 1 THE SINK (owner-ruled PERMANENT 2026-09-09; the design: World/step9/THE_LOOP.md,
"Step 1 THE SINK — the design"; the probes: journal_probes.py, written first and run to fail).

The law engine's run log (World.log — seven classes: EVENT, WRITE, RETRO-WRITE, TIMER-SET, TIMER-FIRE, TIMER-CANCEL, MARKER; the eighth
SKIP since THE LOOP step 3; the ninth ROW — a population-table row — since THE NUMBERS WALK 8b, 2026-09-11; the tenth CLOSE — a ledger
entry's close as its own line, the write line a SNAPSHOT at write time — since step 1's amendment THE CLOSE LINE, 2026-09-12)
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
SINCE STEP 7 (a) WRITE AS YOU GO (2026-09-14; THE_LOOP.md "Step 7 THE LOOP THAT WAITS — part (a)", decision D14 THE SEAL): a world with a
live sink attached (attach) writes every line to the segment's body file and into the one database AT THE END OF ITS BLOCK — the engine's
outermost call returning; the seal writes the header and runs THE AUDIT (the chain, the count, an independent conversion equal on every
field but the bound's right edge, the rebuilt index equal to the live rows). The database is the state between blocks; --gate proves it.
Run: python3 World/step9/world_journal.py --gate | --reindex | --verify <segment> | --stamp <file> | --unmoved <file>   (THE GATES CUT 2026-09-19: the two gate runs concurrent; the stamp and the unmoved check the second gate's cheap form)
"""
import os, re, sys, glob, json, sqlite3, subprocess, tempfile, collections, hashlib
HERE = os.path.dirname(os.path.abspath(__file__))
JOURNAL = os.path.normpath(os.path.join(HERE, '..', 'journal'))
sys.path.insert(0, JOURNAL)
from worldledger import Segment, index_sqlite, canon, row_of  # the August envelope, the chain, the index, the index's row

KINDS = collections.OrderedDict([
    ('EVENT', 'run.event'), ('WRITE', 'run.write'), ('RETRO-WRITE', 'run.retro_write'), ('TIMER-SET', 'run.timer_set'),
    ('TIMER-FIRE', 'run.timer_fire'), ('TIMER-CANCEL', 'run.timer_cancel'), ('MARKER', 'run.marker'),
    ('SKIP', 'run.skip'),        # THE LOOP step 3 (2026-09-09): the eighth class — a daemon not called, its law not in force (the from_event setting)
    ('ROW', 'run.row'),          # THE NUMBERS WALK 8b (2026-09-11): the ninth class — a row of the POPULATION TABLE written by a daemon (World.row; population_schema.yaml)
    ('CLOSE', 'run.close')])     # THE LOOP step 1's amendment THE CLOSE LINE (2026-09-12): the tenth class — a ledger entry's close as its own line (World.close); the write line a snapshot since
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
        elif cls == 'CLOSE':                           # THE CLOSE LINE (2026-09-12): the entity through the registry, the closing daemon (else the scene's own hand: tape), the closer's note as the ref (it opens with the closing verse)
            s = payload.get('subject')
            subj, unit, ref = (reg.get(s, s) if s is not None else 'world'), payload.get('closed_by_daemon') or 'tape', payload.get('note')
        elif cls == 'ROW':                             # THE NUMBERS WALK 8b (2026-09-11): a table row — its subject through the registry (a named row's person, a counted row's tribe name), the writing daemon, the verse it was written from
            s = payload.get('subject')
            subj, unit, ref = (reg.get(s, s) if s is not None else 'world'), payload.get('written_by'), payload.get('source')
        else:
            s = payload.get('subject')
            subj = reg.get(s, s) if s is not None else 'world'
            if cls == 'EVENT':
                unit = ('scenario' if payload.get('scenario') else                                                        # THE LOOP step 5 (2026-09-09): a labeled hypothetical is told from the text's act
                        'port:%s' % payload['port'].get('queue') if isinstance(payload.get('port'), dict) else 'tape')   # THE LOOP step 7 (c) (2026-09-14): an input through the port names its queue
            elif cls == 'SKIP':
                unit = payload.get('daemon')          # step 3: the daemon not called — "who was skipped" beside "who wrote this"
            else:
                unit = payload.get('written_by') or payload.get('source_law')
            ref = payload.get('case_source')
        seg.append(kind, subj, _jsonable(payload, coerced), {'unit': unit, 'ref': ref}, op=day)


def sink(world, source, out_dir=None):
    """write World.log as one L3 segment; returns (path, lines, coerced). SINCE STEP 7 (a) WRITE AS YOU GO (2026-09-14): a world with a
    live sink attached (attach) SEALS it — the lines were written at their blocks, the audit runs now; a world carrying the cursor's
    in-memory sink writes its sealed lines to out_dir; a world that ran with NO sink attaches one now and seals the whole log at once —
    THE LATE SEAL, the bounds as they stand at the seal (the probes' small worlds; said so in the audit)"""
    j = getattr(world, 'journal', None)
    if j is not None and j.memory_only and j.source == source:
        path = os.path.join(data_dir(out_dir), segment_name(source))
        j.seg.write(path)
        return path, len(j.seg.events), sum(j.coerced.values())
    if j is None or j.source != source:
        j = LiveSink(world, source, out_dir=out_dir, late=True)
    return j.seal(quiet=False)


# ---- THE LOOP step 7 THE LOOP THAT WAITS, part (a) WRITE AS YOU GO (2026-09-14; the owner: "ok go 1"; THE_LOOP.md "Step 7 ... part (a)":
# ---- the design, decision D14 THE SEAL; the probes live_probes.py written first, 0/7 on the unchanged engine) ----
# A JOURNAL LINE IS SEALED AT THE END OF ITS BLOCK (the outermost engine call returning at depth 0 — world_engine._sealed calls flush) and
# never changes after: written to the segment's BODY FILE (<segment>.live) and INSERTED into the one database's events table in the same
# act, committed per block. Its bound is written as it stood at the seal ([the last marker, null] inside an open bound); the right edge is
# the next forward marker line's day — a derived fact, never written back (as a ledger entry's close is its own line since THE CLOSE LINE).
# The seal of the run writes the header and the same bytes as the segment file and removes the body; THE AUDIT then proves the live path:
# the chain, the line count, an independent conversion equal on every field but the right edge (its count printed), the index rebuilt from
# the sealed segment equal to the live rows. The database IS the state between blocks; the rebuild is the audit, not the source.
def ensure_index(db_path, out_dir):
    """the one database's events table and the five views — built from every segment on disk when the table is absent (a fresh checkout);
    returns an open connection"""
    c = sqlite3.connect(db_path)
    has = c.execute("select 1 from sqlite_master where type = 'table' and name = 'events'").fetchone()
    c.close()
    if not has:
        index_sqlite(db_path, segments(out_dir))
    views(db_path)
    return sqlite3.connect(db_path)


def rows_of(db_path, source):
    """the index's rows of one source in the run's order, every column — the live rows and the rebuilt rows compared on these"""
    c = sqlite3.connect(db_path)
    try:
        return c.execute("select seq, op, layer, kind, subj, data, unit, ref, chain, source from events where source = ? order by seq", (source,)).fetchall()
    finally:
        c.close()


def l3_sources(out_dir):
    """the sources of the L3 segments on disk, read from their headers"""
    out = []
    for p in sorted(glob.glob(os.path.join(out_dir, 'L3_*.jsonl'))):
        with open(p, encoding='utf-8') as f:
            out.append(json.loads(f.readline()).get('source'))
    return out


def verify_body(path, start='genesis'):
    """a headerless body file's chain recomputed from `start`: True iff no line was mutated in place (the crash-safe trace's check)"""
    chain = start
    with open(path, encoding='utf-8') as f:
        for line in f:
            if not line.strip():
                continue
            ev = json.loads(line)
            claimed = ev.pop('chain')
            chain = hashlib.sha256((chain + canon(ev)).encode('utf-8')).hexdigest()[:16]
            if chain != claimed:
                return False
    return True


class LiveSink:
    """the live sink of one world: attach(world, source) opens the body file and the live index, and the engine's blocks call flush()"""

    def __init__(self, world, source, out_dir=None, memory_only=False, late=False):
        self.world, self.source, self.memory_only, self.late = world, source, memory_only, late
        self.seg = Segment(LAYER, source)
        self.coerced = collections.Counter()
        self.n = 0                    # the log lines sealed so far
        self.blocks = 0               # the flushes that sealed at least one line
        self.audit = None
        if memory_only:               # the cursor's replay (step 4 under the seal): the lines sealed at their blocks, kept in memory — no file, no row
            self.dir = self.path = self.body = self.db = self.conn = self.f = None
        else:
            self.dir = data_dir(out_dir)
            self.path = os.path.join(self.dir, segment_name(source))
            self.body = self.path + '.live'
            self.f = open(self.body, 'w', encoding='utf-8')
            self.db = os.path.join(self.dir, 'world.sqlite')
            self.conn = ensure_index(self.db, self.dir)
            self.conn.execute("DELETE FROM events WHERE source = ?", (source,))     # this source's rows of an older run go; every other source stays
            self.conn.commit()
        world.journal = self

    def flush(self):
        """seal the log's new lines: converted (the one conversion), chained, appended to the body, inserted and committed"""
        log = self.world.log
        if self.n >= len(log):
            return 0
        start = len(self.seg.events)
        _append_log(self.seg, self.world, log[self.n:], self.coerced)
        new = self.seg.events[start:]
        self.n = len(log)
        self.blocks += 1
        if not self.memory_only:
            for ev in new:
                self.f.write(canon(ev) + '\n')
            self.f.flush()
            self.conn.executemany("INSERT INTO events VALUES (?,?,?,?,?,?,?,?,?,?)", [row_of(ev, self.source) for ev in new])
            self.conn.commit()
        return len(new)

    def seal(self, quiet=True):
        """the run's seal: the header and the same bytes written as the segment, the body removed, the connection closed, THE AUDIT run;
        the world detached (a later sink() attaches afresh). Returns (path, lines, coerced) — sink()'s own contract"""
        if self.memory_only:
            raise SystemExit('THE SEAL: an in-memory sink seals nothing — the cursor writes its appended segment through cursor_segment')
        self.flush()
        self.f.close()
        self.seg.write(self.path)
        os.remove(self.body)
        self.conn.close()
        self.world.journal = None
        self.audit = audit(self)
        if not quiet:
            a = self.audit
            print('  THE SEAL %s: %d lines sealed %s in %d blocks; chain %s; the fresh conversion %s on every field but the bound\'s right edge (closed after the seal: %d); the rebuilt index %s the live rows'
                  % (os.path.basename(self.path), a['lines'], 'LATE (the bounds as they stand)' if self.late else 'LIVE', self.blocks,
                     'VERIFIED' if a['chain'] else 'BROKEN', 'EQUAL' if a['fields_equal'] else 'UNEQUAL', a['right_edge_closed_after'],
                     'EQUALS' if a['index_equal'] else 'DIFFERS FROM'))
        if not self.audit['ok']:
            raise SystemExit('THE SEAL: the audit FAILED on %s — %s' % (self.path, self.audit))
        return self.path, len(self.seg.events), sum(self.coerced.values())


def attach(world, source, out_dir=None, memory_only=False):
    """attach a live sink to a world BEFORE its tape runs; the engine's blocks seal the lines from then on"""
    return LiveSink(world, source, out_dir=out_dir, memory_only=memory_only)


def _sans(ev):
    d = dict(ev); d.pop('chain', None)
    return d


def audit(sink):
    """THE AUDIT of a sealed segment (the design's (i)-(iv)): the chain; the line count against the log; an INDEPENDENT conversion of the
    same log at the run's end equal on every field but the bound's right edge (the one named exception — its count returned); the index
    rebuilt from the sealed file equal to the live rows, row for row, every column"""
    w, path, source = sink.world, sink.path, sink.source
    chain = Segment.verify(path)
    fresh = Segment(LAYER, source)
    _append_log(fresh, w, w.log, collections.Counter())
    closed_after, bad = 0, 0
    for a, b in zip(sink.seg.events, fresh.events):
        a, b = _sans(a), _sans(b)
        if a == b:
            continue
        da, db_ = dict(a['data']), dict(b['data'])
        ba, bb = da.pop('bound', None), db_.pop('bound', None)
        rest = da == db_ and {k: v for k, v in a.items() if k != 'data'} == {k: v for k, v in b.items() if k != 'data'}
        if rest and isinstance(ba, list) and isinstance(bb, list) and len(ba) == 2 == len(bb) and ba[0] == bb[0] and ba[1] is None and bb[1] is not None:
            closed_after += 1
        else:
            bad += 1
    fields_equal = bad == 0 and len(sink.seg.events) == len(fresh.events)
    with tempfile.TemporaryDirectory() as td:
        tdb = os.path.join(td, 'audit.sqlite')
        index_sqlite(tdb, [path])
        rebuilt = rows_of(tdb, source)
    live = rows_of(sink.db, source)
    index_equal = rebuilt == live and len(live) == len(sink.seg.events)
    lines = len(sink.seg.events)
    ok = bool(chain) and lines == len(w.log) and fields_equal and index_equal
    return {'ok': ok, 'lines': lines, 'log': len(w.log), 'chain': bool(chain), 'fields_equal': fields_equal, 'unequal': bad,
            'right_edge_closed_after': closed_after, 'index_equal': index_equal, 'coerced': sum(sink.coerced.values()), 'late': sink.late}


def live_report(out_dir=None):
    """the one database as the run leaves it: every L3 segment on disk against its rows — the database IS the state"""
    d = data_dir(out_dir)
    db = os.path.join(d, 'world.sqlite')
    parts, ok = [], True
    c = sqlite3.connect(db)
    try:
        total = c.execute("select count(*) from events").fetchone()[0]
        for p in sorted(glob.glob(os.path.join(d, 'L3_*.jsonl'))):
            with open(p, encoding='utf-8') as f:
                src = json.loads(f.readline()).get('source')
                lines = sum(1 for l in f if l.strip())
            rows = c.execute("select count(*) from events where source = ?", (src,)).fetchone()[0]
            ok = ok and rows == lines
            parts.append('%s %d rows = %d lines %s' % (src, rows, lines, 'MATCH' if rows == lines else 'DIVERGE'))
    finally:
        c.close()
    return '%s — %d rows; %s [%s]' % (db, total, '; '.join(parts), 'every source current' if ok else 'A SOURCE DIVERGES — reindex and read')


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
    j = getattr(world, 'journal', None)
    if j is not None and j.memory_only:               # THE LOOP step 7 (a) (2026-09-14; D14 THE SEAL): the replay's lines were sealed at their blocks by the cursor's in-memory sink — the rule the base was written under
        sealed = j.seg.events[:fork]
    else:                                              # a world that replayed with no sink attached: the late conversion, the bounds as they stand
        audit_seg = Segment(LAYER, RUNNING_WORLD)
        _append_log(audit_seg, world, world.log[:fork], coerced)
        sealed = audit_seg.events
    with open(base, encoding='utf-8') as f:
        base_lines = f.read().split('\n')
    mine = [canon(ev) for ev in sealed]
    if mine != base_lines[1:fork + 1]:
        first = next((i for i, (a, b) in enumerate(zip(mine, base_lines[1:fork + 1])) if a != b), min(len(mine), len(base_lines) - 1))
        raise SystemExit('CURSOR REFUSED: the replayed prefix differs from the base segment %s at event %d of %d — the base or the engine has '
                         'moved; rerun the tape (cold_run_sequence.py), then resume' % (os.path.basename(base), first + 1, fork))
    start = sealed[-1]['chain'] if sealed else None
    seg = Segment(LAYER, 'cold_run_sequence/cursor@%s' % verse, start_chain=start,           # the appended lines: converted at the write (late; part (b) makes the cursor's own lines live)
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
FOLD_VIEWS_SQL = os.path.join(JOURNAL, 'fold_views.sql')     # D7'S MERGE (2026-09-14): the reading's fourteen views over the fold rows
FOLD_SEGMENT = 'L1_fold.jsonl'
RUNNING_WORLD = 'cold_run_sequence/seed_isaac'      # the running setting's segment — the ask-tool's default world (--world overrides)
OPEN_OPS = ('debit', 'heaven', 'body')               # the ledger ops whose entries open and close (World._write's own rule)
_VERSE_HEAD = re.compile(r'^\s*(\d?\s?[A-Za-z]+)\s+(\d+):(\d+)')


def views(db_path):
    """create the four run views over the events table from World/journal/run_views.sql (drop-and-create)"""
    sql = open(VIEWS_SQL, encoding='utf-8').read()
    fold_sql = open(FOLD_VIEWS_SQL, encoding='utf-8').read() if os.path.exists(FOLD_VIEWS_SQL) else ''
    c = sqlite3.connect(db_path)
    try:
        c.executescript(sql)
        if fold_sql:
            c.executescript(fold_sql)                  # D7'S MERGE: the old tables as views, beside the run views
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
            v['rows'] = k.get('run.row', 0)             # THE NUMBERS WALK 8b (2026-09-11): the fifth view's count derived from the table's own run.row lines
            v['population'] = c.execute("select count(*) from run_population where source = ?", (src,)).fetchone()[0]
            # THE CLOSE LINE (2026-09-12): the ledger rows carrying a close = the run.close lines whose write lies in the same source; a close whose
            # write lies in another source (a cursor segment paying a base entry) is FOREIGN — counted and printed, never a per-source failure
            v['closes'] = k.get('run.close', 0)
            v['closed'] = c.execute("select count(*) from run_ledger where source = ? and day_closed is not null", (src,)).fetchone()[0]
            v['closes_local'] = c.execute("""select count(*) from events c where c.kind = 'run.close' and c.source = ? and exists (
                select 1 from events w where w.source = c.source and w.subj = c.subj and w.kind in ('run.write', 'run.retro_write')
                and json_extract(w.data, '$.seq') = json_extract(c.data, '$.entry_seq'))""", (src,)).fetchone()[0]
            v['closes_foreign'] = v['closes'] - v['closes_local']
            out[src] = v
        return out
    finally:
        c.close()


def views_gate(db_path):
    """every view's row count equals what the events table says it must be, on every source: (ok, lines)"""
    ok, lines = True, []
    for src, v in view_counts(db_path).items():
        checks = [('ledger', v['ledger'], v['writes']), ('timers', v['timers'], v['sets']), ('fired', v['fired'], v['fires']),
                  ('cancelled', v['cancelled'], v['cancels']), ('clock', v['clock'], v['markers']), ('docket', v['docket'], v['docket_from_ledger']),
                  ('population', v['population'], v['rows']),      # THE NUMBERS WALK 8b (2026-09-11): the fifth view's rows = the run.row lines
                  ('closed', v['closed'], v['closes_local'])]       # THE CLOSE LINE (2026-09-12): the ledger's closed rows = the source's own run.close lines
        bad = [(n, got, want) for n, got, want in checks if got != want]
        ok = ok and not bad
        lines.append('  %-44s ledger %5d = writes %5d | timers %4d = sets %4d (fired %d = fires %d, cancelled %d = cancels %d, pending %d) | clock %4d = markers %4d | docket %d (open %d) | population %d = rows %d | closed %d = closes %d (foreign %d) | skips %d  %s'
                     % (src, v['ledger'], v['writes'], v['timers'], v['sets'], v['fired'], v['fires'], v['cancelled'], v['cancels'], v['pending'],
                        v['clock'], v['markers'], v['docket'], v['docket_open'], v['population'], v['rows'], v['closed'], v['closes_local'], v['closes_foreign'], v['skips'], 'MATCH' if not bad else 'DIVERGE %s' % bad))
    if not lines:
        ok, lines = False, ['  no L3 source in the index — ZERO-REPORT']
    return ok, lines


def pinned_truth():
    """the tripwires logic/corpus/CORPUS_TRUTH.py pins (units, facts, demands, events, names, standing, open demands, the hash), read as literals"""
    p = os.path.normpath(os.path.join(HERE, '..', '..', 'logic', 'corpus', 'CORPUS_TRUTH.py'))
    t = open(p, encoding='utf-8').read()
    out = {k: int(v) for k, v in re.findall(r'assert len\(W\["(\w+)"\]\) == (\d+)', t)}
    m = re.search(r'assert len\(open_d\) == (\d+)', t)
    if m:
        out['open_demands'] = int(m.group(1))
    m = re.search(r"_state_hash\(W\) == '([0-9a-f]+)'", t)
    out['state_hash'] = m.group(1) if m else None
    return out


def fold_gate(db_path, out_dir=None):
    """D7'S MERGE (D21 b): the fold layer's header against CORPUS_TRUTH's pinned tripwires and against the index's own fold rows — no refold;
    a frozen unit moves the hash and the gate then says the layer is stale until World/build_world.py rebuilds it. Returns (ok, lines)."""
    d = data_dir(out_dir)
    seg = os.path.join(d, FOLD_SEGMENT)
    if not os.path.exists(seg):
        return False, ['  THE FOLD LAYER: no %s in %s — run python3 World/build_world.py' % (FOLD_SEGMENT, d)]
    with open(seg, encoding='utf-8') as f:
        head = json.loads(f.readline())
    pinned = pinned_truth()
    lines, ok = [], True
    for k in ('units', 'facts', 'demands', 'events', 'names', 'standing', 'open_demands'):
        same = head.get(k) == pinned.get(k)
        ok = ok and same
        lines.append('  THE FOLD LAYER %-13s header %6s  pinned %6s  %s' % (k, head.get(k), pinned.get(k), 'MATCH' if same else 'DIVERGE'))
    same = head.get('state_hash') == pinned.get('state_hash')
    ok = ok and same
    lines.append('  THE FOLD LAYER state hash    header %s  pinned %s  %s' % (head.get('state_hash'), pinned.get('state_hash'), 'MATCH' if same else 'STALE — run python3 World/build_world.py'))
    c = sqlite3.connect(db_path)
    try:
        rows = dict(c.execute("select kind, count(*) from events where kind like 'fold.%' group by kind").fetchall())
    finally:
        c.close()
    for k, kind in (('units', 'fold.unit'), ('facts', 'fold.fact'), ('events', 'fold.event'), ('demands', 'fold.demand'), ('mentions', 'fold.mention'),
                    ('names', 'fold.name'), ('standing', 'fold.standing'), ('tests', 'fold.test'), ('checkpoints', 'fold.checkpoint'), ('ledger', 'fold.ledger'), ('refs', 'fold.ref')):
        same = rows.get(kind, 0) == head.get(k)
        ok = ok and same
        if not same:
            lines.append('  THE FOLD LAYER %-13s index rows %6d  header %6s  DIVERGE' % (k, rows.get(kind, 0), head.get(k)))
    lines.append('  THE FOLD LAYER: %d kinds, %d rows in the index %s the header' % (len(rows), sum(rows.values()), 'MATCHING' if ok else 'DIVERGING FROM'))
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
        if question == 'population':                   # THE NUMBERS WALK 8b (2026-09-11): the fifth question — the population table's rows, all or one tribe's, in the run's order
            tribe = args[0] if args else None
            return _rows(c, "select * from run_population where source = ? and (? is null or tribe = ?) order by seq", (source, tribe, tribe))
        raise SystemExit('ASK: the questions are ledger <entity> [<day>], open <verse>, who <entity> <effect>, custody, population [<tribe>]')
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
    lc = re.search(r'log classes: (\{[^\n]*\})', stdout)              # THE NUMBERS WALK 8b (2026-09-11): the ninth class ROW read from the runner's own class census — the rows are no writes and enter no other count
    if not (ev and tm and lc):
        raise SystemExit('THE GATE: the RUN tuple was not found in the runner\'s print')
    import ast
    classes = ast.literal_eval(lc.group(1))
    return {'run.event': int(ev.group(1)), 'run.marker': int(ev.group(2)), 'run.timer_set': int(tm.group(1)),
            'run.timer_fire': int(tm.group(2)), 'run.timer_cancel': int(tm.group(3)), 'run.retro_write': int(tm.group(4)),
            'run.write': int(tm.group(5)), 'run.skip': int(tm.group(6)),      # step 3: the eighth class counted (0 under boot)
            'run.row': int(classes.get('ROW', 0)),                        # 8b: the ninth class — THE POPULATION TABLE's rows (0 on a world that writes none)
            'run.close': int(classes.get('CLOSE', 0))}                    # THE CLOSE LINE (2026-09-12): the tenth class — the closes performed, read from the runner's own class census


def sources_key():
    """THE GATES CUT (2026-09-19): the key of the running world's snapshot — a digest of every source the replay depends on (the runners, the engine,
    the effects layer, the guards, this file, the registries, the text store's size and stamp): a snapshot is served only under the same key"""
    import hashlib, glob
    h = hashlib.sha256()
    files = sorted(glob.glob(os.path.join(HERE, 'cold_run_*.py')) + glob.glob(os.path.join(HERE, '*_vocabulary.yaml')) + glob.glob(os.path.join(HERE, '*_dispositions.yaml'))
                   + glob.glob(os.path.join(HERE, 'calendar_parameters*.yaml')) + glob.glob(os.path.join(HERE, 'population_schema*.yaml'))
                   + [os.path.join(HERE, f) for f in ('world_engine.py', 'effects_layer.py', 'compile_guards.py', 'world_journal.py')]
                   + [os.path.normpath(os.path.join(HERE, '..', '..', 'logic', 'corpus', 'entity_registry.yaml'))])
    for p in files:
        if os.path.exists(p):
            h.update(os.path.basename(p).encode('utf-8')); h.update(open(p, 'rb').read())
    db = os.path.normpath(os.path.join(HERE, '..', '..', 'Data', 'tanakh.sqlite'))
    if os.path.exists(db):
        st = os.stat(db); h.update(('tanakh %d %d' % (st.st_size, int(st.st_mtime))).encode('utf-8'))
    return h.hexdigest()


def snapshot_paths(out_dir=None):
    d = data_dir(out_dir); return os.path.join(d, 'running_world.pickle'), os.path.join(d, 'running_world.json')


def save_snapshot(w, out_dir=None, key=None):
    """THE GATES CUT (2026-09-19): the running world saved after its replay — the daemons stripped (functions of the runners' modules; a reader
    of the world needs none and must not pay their import), the journal handle dropped; the sidecar carries the sources key. The replay costs
    two seconds; the import of sixty-three runners costs two minutes: the snapshot spares the readers the second."""
    import pickle, json, time
    snap, side = snapshot_paths(out_dir)
    laws, journal = w.laws, getattr(w, 'journal', None)
    w.laws = []; w.journal = None
    try:
        with open(snap + '.tmp', 'wb') as f: f.write(pickle.dumps(w, protocol=pickle.HIGHEST_PROTOCOL))
    finally:
        w.laws, w.journal = laws, journal
    with open(side + '.tmp', 'w', encoding='utf-8') as f:
        json.dump({'key': key or sources_key(), 'when': time.strftime('%Y-%m-%d %H:%M'), 'events': sum(1 for l in w.log if l[0] == 'EVENT'), 'entities': len(w.entities), 'log': len(w.log)}, f)
    os.replace(snap + '.tmp', snap); os.replace(side + '.tmp', side)   # atomic — two readers replaying at once never see a half-written snapshot
    return snap


def load_snapshot(out_dir=None, key=None):
    """the snapshot if its key is the current sources key, else None (the caller replays and saves)"""
    import pickle, json
    snap, side = snapshot_paths(out_dir)
    if not (os.path.exists(snap) and os.path.exists(side)): return None
    meta = json.load(open(side, encoding='utf-8'))
    if meta.get('key') != (key or sources_key()): return None
    import world_engine   # the classes the pickle names
    return pickle.load(open(snap, 'rb'))


def live_digest(out_dir=None):
    """THE GATES CUT (2026-09-19): a digest of the LIVE rows of every L3 source in the one database (the rows in their stored order) — what the chain
    stamps before the sweep and compares after: equal digests = the sweep moved nothing in the journal (the second gate's claim, proved in seconds)"""
    import hashlib
    dd = data_dir(out_dir); db = os.path.join(dd, 'world.sqlite')
    srcs = l3_sources(dd); h = hashlib.sha256()
    for s in srcs:
        h.update(s.encode('utf-8')); h.update(repr(rows_of(db, s)).encode('utf-8'))
    return h.hexdigest(), len(srcs)


def gate():
    """two processes, two directories: byte-identical segments, verified chains, the index's counts = the RUN tuple"""
    with tempfile.TemporaryDirectory() as t1, tempfile.TemporaryDirectory() as t2:
        # THE GATES CUT (2026-09-19): the two processes run CONCURRENTLY — two directories, two databases, no shared file; the proof (byte-identical
        # segments from two independent runs) is the same, the wall time half
        import concurrent.futures
        with concurrent.futures.ThreadPoolExecutor(max_workers=2) as pool:
            f1, f2 = pool.submit(_run_sequence, t1), pool.submit(_run_sequence, t2)
            out1, out2 = f1.result(), f2.result()
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
        # THE LOOP step 7 (a) WRITE AS YOU GO (2026-09-14): the LIVE rows of every L3 source, read BEFORE the rebuild — the two processes'
        # rows identical, and the rebuilt index equal to the live rows on every source (the audit, once more, from outside the run)
        live1 = {s: rows_of(os.path.join(t1, 'world.sqlite'), s) for s in l3_sources(t1)}
        live2 = {s: rows_of(os.path.join(t2, 'world.sqlite'), s) for s in l3_sources(t2)}
        db, n, k = reindex(t1)
        rebuilt = {s: rows_of(db, s) for s in live1}
        live_ok = bool(live1) and live1 == live2 and rebuilt == live1
        print('  THE LIVE INDEX (step 7 a): %d sources, %d rows written line by line at their blocks; the two processes\' rows %s; the rebuilt index %s the live rows'
              % (len(live1), sum(len(r) for r in live1.values()), 'IDENTICAL' if live1 == live2 else 'DIFFER', 'EQUALS' if rebuilt == live1 else 'DIFFERS FROM'))
        ok = ok and live_ok
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
        print('  THE FIVE RUN VIEWS (run_ledger, run_timers, run_clock, run_docket, run_population) — every count against the table\'s:')
        print('\n'.join(vlines))
        ok = ok and vok
        # D7'S MERGE (2026-09-14): the reading's layer in the ONE database (the data folder's index) against the pinned truth and its own rows
        fok, flines = fold_gate(os.path.join(data_dir(), 'world.sqlite'), data_dir())
        print('\n'.join(flines))
        ok = ok and fok
        print('GATE %s — %s' % ('GREEN' if ok else 'RED', 'the replay is the audit, the running world is the instrument' if ok else 'read the lines above'))
        return ok


if __name__ == '__main__':
    if '--stamp' in sys.argv:          # THE GATES CUT (2026-09-19): write the live rows' digest to a file (the chain, before the sweep)
        import json, time
        d, n = live_digest(); p = sys.argv[sys.argv.index('--stamp') + 1]
        json.dump({'digest': d, 'sources': n, 'when': time.strftime('%Y-%m-%d %H:%M')}, open(p, 'w', encoding='utf-8'))
        print('THE JOURNAL STAMPED: %d sources, digest %s… (%s)' % (n, d[:16], p)); sys.exit(0)
    if '--unmoved' in sys.argv:        # THE GATES CUT (2026-09-19): compare the live rows' digest with the stamp (the chain, after the sweep — the second gate's claim)
        import json
        p = sys.argv[sys.argv.index('--unmoved') + 1]; st = json.load(open(p, encoding='utf-8')); d, n = live_digest()
        same = d == st['digest'] and n == st['sources']
        print('THE JOURNAL %s: the live rows\' digest %s the stamp\'s (%d sources; stamped %s) — %s' % ('UNMOVED' if same else 'MOVED', 'equals' if same else 'DIFFERS FROM', n, st.get('when'), 'GATE GREEN — the sweep wrote nothing the journal keeps' if same else 'GATE RED — run the full gate'))
        sys.exit(0 if same else 1)
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
