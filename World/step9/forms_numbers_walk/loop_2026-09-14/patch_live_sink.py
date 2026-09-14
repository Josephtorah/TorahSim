#!/usr/bin/env python3
"""patch_live_sink.py — THE LOOP step 7 (a) WRITE AS YOU GO: the code, in three files, on the design of THE_LOOP.md (2026-09-14).
Every replacement asserted unique; idempotent (a second run finds the new text and skips)."""
import sys

def patch(path, pairs):
    t = open(path, encoding='utf-8').read(); done = 0
    for old, new in pairs:
        n = t.count(old)
        if n == 0 and new in t:
            continue
        assert n == 1, (path, n, old[:70]); t = t.replace(old, new); done += 1
    open(path, 'w', encoding='utf-8').write(t)
    print('%s: %d replacement(s)' % (path, done))

# ---- 1. worldledger.py: the index's row has one home ----
patch('<repo-old>/World/journal/worldledger.py', [
    ('''def index_sqlite(db_path, segment_paths):''',
     '''def row_of(ev, source):
    """the index's row for one envelope event — ONE home for the row's shape (THE LOOP step 7 (a) WRITE AS YOU GO, 2026-09-14:
    the live sink writes the same row the rebuild makes, and the rebuild must reproduce it)"""
    return (ev["s"], ev["op"], ev["layer"], ev["kind"], ev["subj"], canon(ev["data"]),
            ev["prov"].get("unit"), ev["prov"].get("ref"), ev["chain"], source)


def index_sqlite(db_path, segment_paths):'''),
    ('''                c.execute("INSERT INTO events VALUES (?,?,?,?,?,?,?,?,?,?)",
                          (ev["s"], ev["op"], ev["layer"], ev["kind"],
                           ev["subj"], canon(ev["data"]),
                           ev["prov"].get("unit"), ev["prov"].get("ref"),
                           ev["chain"], source))''',
     '''                c.execute("INSERT INTO events VALUES (?,?,?,?,?,?,?,?,?,?)", row_of(ev, source))'''),
])

# ---- 2. world_engine.py: the hook — one attribute, one decorator, six decorations ----
patch('<repo-old>/World/step9/world_engine.py', [
    ('import collections\n', 'import collections\nimport functools\n'),
    ('''class World:
    def __init__(self, era, epoch=None, registry=None, installation=None):''',
     '''def _sealed(fn):
    """THE LOOP step 7 (a) WRITE AS YOU GO (2026-09-14; THE_LOOP.md "Step 7 ... part (a)", decision D14 THE SEAL): an entry point of
    the engine is a BLOCK — when the outermost call returns (depth 0; in a finally, so a refusal raised mid-block still seals the lines
    logged before it) the attached journal seals the log's new lines: on disk and in the index at once. A world with no journal
    (the exam worlds, D9) pays nothing. Nothing here reads or writes the world: the hook observes the log and decides nothing."""
    @functools.wraps(fn)
    def sealed(self, *a, **k):
        try:
            return fn(self, *a, **k)
        finally:
            j = getattr(self, 'journal', None)
            if j is not None and self._depth == 0:
                j.flush()
    return sealed


class World:
    def __init__(self, era, epoch=None, registry=None, installation=None):'''),
    ('''        self.log = []
        self._entry_seq = 0''',
     '''        self.log = []
        self.journal = None      # THE LOOP step 7 (a) WRITE AS YOU GO (2026-09-14): the attached live sink (world_journal.attach), sealing the log's lines at the end of every block; None on every world that journals nothing
        self._entry_seq = 0'''),
    ('''    def submit(self, event):
        EV.validate([event['kind']])''',
     '''    @_sealed
    def submit(self, event):
        EV.validate([event['kind']])'''),
    ('''    def close(self, eid, effect, note, value=None):
        """an entry closes''',
     '''    @_sealed
    def close(self, eid, effect, note, value=None):
        """an entry closes'''),
    ('''    def row(self, table, row):
        """a daemon writes a ROW''',
     '''    @_sealed
    def row(self, table, row):
        """a daemon writes a ROW'''),
    ('''    def cancel_timers(self, subject, effect, note):
        """a later TEXT event''',
     '''    @_sealed
    def cancel_timers(self, subject, effect, note):
        """a later TEXT event'''),
    ('''    def marker(self, verse, day, value=None, era=None, new_year_month=None, proleptic=False, placement='text_constrained'):
        """THE MARKER''',
     '''    @_sealed
    def marker(self, verse, day, value=None, era=None, new_year_month=None, proleptic=False, placement='text_constrained'):
        """THE MARKER'''),
    ('''    def advance(self, to_day):
        if to_day > self.clock.day:''',
     '''    @_sealed
    def advance(self, to_day):
        if to_day > self.clock.day:'''),
])

# ---- 3. world_journal.py: the live sink, the seal, the audit; the cursor's audit under the seal; the gate's live check ----
NEW_SINK = '''def sink(world, source, out_dir=None):
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
                self.f.write(canon(ev) + '\\n')
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
            print('  THE SEAL %s: %d lines sealed %s in %d blocks; chain %s; the fresh conversion %s on every field but the bound\\'s right edge (closed after the seal: %d); the rebuilt index %s the live rows'
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
'''
OLD_SINK = '''def sink(world, source, out_dir=None):
    """write World.log as one L3 segment; returns (path, lines, coerced)"""
    seg = Segment(LAYER, source)
    coerced = collections.Counter()
    _append_log(seg, world, world.log, coerced)
    path = os.path.join(data_dir(out_dir), segment_name(source))
    seg.write(path)
    return path, len(seg.events), sum(coerced.values())
'''
patch('<repo-old>/World/step9/world_journal.py', [
    ('import os, re, sys, glob, json, sqlite3, subprocess, tempfile, collections\n',
     'import os, re, sys, glob, json, sqlite3, subprocess, tempfile, collections, hashlib\n'),
    ('from worldledger import Segment, index_sqlite, canon          # the August envelope, the chain, the index\n',
     'from worldledger import Segment, index_sqlite, canon, row_of  # the August envelope, the chain, the index, the index\'s row\n'),
    ('''Run: python3 World/step9/world_journal.py --gate | --reindex | --verify <segment>
"""''',
     '''SINCE STEP 7 (a) WRITE AS YOU GO (2026-09-14; THE_LOOP.md "Step 7 THE LOOP THAT WAITS — part (a)", decision D14 THE SEAL): a world with a
live sink attached (attach) writes every line to the segment's body file and into the one database AT THE END OF ITS BLOCK — the engine's
outermost call returning; the seal writes the header and runs THE AUDIT (the chain, the count, an independent conversion equal on every
field but the bound's right edge, the rebuilt index equal to the live rows). The database is the state between blocks; --gate proves it.
Run: python3 World/step9/world_journal.py --gate | --reindex | --verify <segment>
"""'''),
    (OLD_SINK, NEW_SINK),
    ('''    coerced = collections.Counter()
    audit = Segment(LAYER, RUNNING_WORLD)
    _append_log(audit, world, world.log[:fork], coerced)
    with open(base, encoding='utf-8') as f:
        base_lines = f.read().split('\\n')
    mine = [canon(ev) for ev in audit.events]''',
     '''    coerced = collections.Counter()
    j = getattr(world, 'journal', None)
    if j is not None and j.memory_only:               # THE LOOP step 7 (a) (2026-09-14; D14 THE SEAL): the replay's lines were sealed at their blocks by the cursor's in-memory sink — the rule the base was written under
        sealed = j.seg.events[:fork]
    else:                                              # a world that replayed with no sink attached: the late conversion, the bounds as they stand
        audit_seg = Segment(LAYER, RUNNING_WORLD)
        _append_log(audit_seg, world, world.log[:fork], coerced)
        sealed = audit_seg.events
    with open(base, encoding='utf-8') as f:
        base_lines = f.read().split('\\n')
    mine = [canon(ev) for ev in sealed]'''),
    ('''    start = audit.events[-1]['chain'] if audit.events else None
    seg = Segment(LAYER, 'cold_run_sequence/cursor@%s' % verse, start_chain=start,''',
     '''    start = sealed[-1]['chain'] if sealed else None
    seg = Segment(LAYER, 'cold_run_sequence/cursor@%s' % verse, start_chain=start,           # the appended lines: converted at the write (late; part (b) makes the cursor's own lines live)'''),
    ('''        db, n, k = reindex(t1)
        got = {kind: c for kind, c in counts(db).items()}''',
     '''        # THE LOOP step 7 (a) WRITE AS YOU GO (2026-09-14): the LIVE rows of every L3 source, read BEFORE the rebuild — the two processes'
        # rows identical, and the rebuilt index equal to the live rows on every source (the audit, once more, from outside the run)
        live1 = {s: rows_of(os.path.join(t1, 'world.sqlite'), s) for s in l3_sources(t1)}
        live2 = {s: rows_of(os.path.join(t2, 'world.sqlite'), s) for s in l3_sources(t2)}
        db, n, k = reindex(t1)
        rebuilt = {s: rows_of(db, s) for s in live1}
        live_ok = bool(live1) and live1 == live2 and rebuilt == live1
        print('  THE LIVE INDEX (step 7 a): %d sources, %d rows written line by line at their blocks; the two processes\\' rows %s; the rebuilt index %s the live rows'
              % (len(live1), sum(len(r) for r in live1.values()), 'IDENTICAL' if live1 == live2 else 'DIFFER', 'EQUALS' if rebuilt == live1 else 'DIFFERS FROM'))
        ok = ok and live_ok
        got = {kind: c for kind, c in counts(db).items()}'''),
])

# ---- 4. cold_run_sequence.py: attach before the tape, three worlds; the closing rebuild replaced by the live report ----
patch('<repo-old>/World/step9/cold_run_sequence.py', [
    ('''    assert w.laws, 'ZERO-REPORT: empty law library'
    M = {}
    del _INK_CHECKS[:]                                   # the re-checks counted per world (the first O1 run read 207 = three worlds x 69)''',
     '''    assert w.laws, 'ZERO-REPORT: empty law library'
    WJ.attach(w, 'cold_run_sequence/%s' % setting)       # THE LOOP step 7 (a) WRITE AS YOU GO (2026-09-14; D14 THE SEAL): every line on disk and in the index at the end of its block
    M = {}
    del _INK_CHECKS[:]                                   # the re-checks counted per world (the first O1 run read 207 = three worlds x 69)'''),
    ('''    w.stop_before = WE.verse_key(verse)
    if w.stop_before is None:
        raise SystemExit('CURSOR: %r is not a verse' % verse)
    M = {}''',
     '''    w.stop_before = WE.verse_key(verse)
    if w.stop_before is None:
        raise SystemExit('CURSOR: %r is not a verse' % verse)
    WJ.attach(w, WJ.RUNNING_WORLD, memory_only=True)     # THE LOOP step 7 (a) (2026-09-14): the replay's lines sealed at their blocks in memory — the audit compares them to the base
    M = {}'''),
    ('''    w.laws = daemons()
    del _INK_CHECKS[:]
    ns['tape_rest'](w, {}, dict(PARAMS))''',
     '''    w.laws = daemons()
    WJ.attach(w, 'cold_run_sequence/rest')               # THE LOOP step 7 (a) (2026-09-14): THE REST's lines live too
    del _INK_CHECKS[:]
    ns['tape_rest'](w, {}, dict(PARAMS))'''),
    ('''    db, rows, segs = WJ.reindex()                            # THE LOOP step 2 (minimal): the index rebuilt from every segment on disk
    print('JOURNAL INDEX: %s — %d rows from %d segments (drop-and-rebuild; never written directly)' % (db, rows, segs))''',
     '''    print('JOURNAL INDEX (live): %s' % WJ.live_report())    # THE LOOP step 7 (a) WRITE AS YOU GO (2026-09-14): the database IS the state — every world's rows were written line by line as its blocks sealed and audited against a rebuild at its seal; the closing rebuild of step 2 is retired (--reindex by hand)'''),
])
print('done')
