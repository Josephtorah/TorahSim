#!/usr/bin/env python3
"""live_probes.py — THE LOOP's step 7 part (a) WRITE AS YOU GO fire-probes (2026-09-14; THE_LOOP.md "Step 7 THE LOOP THAT WAITS —
part (a) WRITE AS YOU GO: the design"), written BEFORE the engine's hook and the live sink. Against the unchanged engine every
probe must FAIL; after the code every probe must PASS. All seven run in-process on a SMALL probe world (two probe daemons over
registered kinds and effects: a seven-day timer, a debit opened at the custody act and closed at the output) journaling into a
temporary directory, so the file runs in a second. Seven probes:
  L1 THE BODY FILE IS LIVE — after each of three blocks (a marker; a submit that writes the debit; the submit whose daemon closes
     it) the body file <segment>.live holds exactly the lines sealed so far and its chain verifies from genesis
  L2 THE INDEX IS LIVE — at the same three points the events rows of the source equal the lines so far, and run_ledger shows the
     debit OPEN after the second block and CLOSED after the third (the ask tool's answer between blocks)
  L3 THE SEAL'S FORM — a sealed EVENT line carries fired_by complete and its bound [x, null]; the marker line that closes the bound
     follows with the right edge as its day; a timer fired inside a later marker's walk carries its bound already closed
  L4 THE SEAL AND THE AUDIT — seal() writes the segment (header + the same bytes), removes the body file, verify() passes, and the
     audit passes: lines = the log; the fresh conversion equal on every field but the bound's right edge (the count of lines whose
     bound closed after their seal printed); the index rebuilt from the sealed segment equal to the live rows
  L5 DETERMINISM THROUGH THE LIVE PATH — two live runs of one probe world in two directories are byte-identical, segment and rows
  L6 THE CRASH-SAFE TRACE — a refusal raised inside a daemon mid-block leaves the lines sealed before it on disk, the body file's
     prefix verifying
  L7 THE EXAM WORLDS PAY NOTHING — a World with no journal attached logs as before: the attribute None, no file, no row
Not run by the sweep; run by hand at the sitting and after any engine edit. Run: python3 World/step9/live_probes.py
"""
import os, sys, json, sqlite3, tempfile, collections
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import world_engine as WE

results = []


def probe(name):
    def deco(fn):
        try:
            ok, note = fn()
        except BaseException as e:                   # the old engine lacks the construct: a FAIL, named
            ok, note = False, '%s: %s' % (type(e).__name__, str(e)[:200])
        results.append((name, bool(ok), note))
        return fn
    return deco


def law_timer(event, world):
    """the timer daemon: a seven-day timer on an installation (registered kinds and effects only)"""
    if event['kind'] == 'installation_commanded':
        day = event.get('day', world.clock.day)
        return [{'effect': 'released', 'subject': event['subject'], 'counterparty': None, 'amount': None, 'due': day + 7,
                 'source_law': 'probe', 'case_source': event['case_source']}]
    return []


def law_debit(event, world):
    """the debit daemon: a declaration owed at the custody act, closed at the output (journal_probes' J7 pair)"""
    if event['kind'] == 'custody_three_days':
        return [{'effect': 'declaration_owed', 'subject': 'the-court', 'counterparty': event['subject'], 'amount': None, 'due': None,
                 'source_law': 'probe', 'case_source': event['case_source']}]
    if event['kind'] == 'statute_set':
        world.close('the-court', 'declaration_owed', event['case_source'])
        return [{'effect': 'rule_installed', 'subject': 'the-tabernacle', 'counterparty': None, 'amount': None, 'due': None,
                 'value': 'law_debit', 'source_law': 'probe', 'case_source': event['case_source']}]
    return []


def law_refuse(event, world):
    """the refusing daemon: a gate's honest fire mid-block (L6)"""
    if event['kind'] == 'tablets_broken':
        raise SystemExit('PROBE: a refusal raised inside a daemon while consuming %s' % event['kind'])
    return []


SOURCE = 'live_probes/world'
REG = {'the-court': 'the_court', 'the-people': 'israel_people'}


def new_world(laws):
    w = WE.World(era='probe', epoch='count', registry=REG)
    w.laws = laws
    return w


def body_lines(d):
    p = os.path.join(d, 'L3_run_live_probes_world.jsonl.live')
    if not os.path.exists(p):
        return None, p
    return [l for l in open(p, encoding='utf-8').read().split('\n') if l.strip()], p


def live_rows(d, source=SOURCE):
    db = os.path.join(d, 'world.sqlite')
    if not os.path.exists(db):
        return None
    c = sqlite3.connect(db)
    try:
        return c.execute("select seq, op, layer, kind, subj, data, unit, ref, chain, source from events where source = ? order by seq", (source,)).fetchall()
    finally:
        c.close()


def ledger_row(d, effect='declaration_owed', source=SOURCE):
    db = os.path.join(d, 'world.sqlite')
    c = sqlite3.connect(db)
    try:
        return c.execute("select open, day_closed from run_ledger where source = ? and effect = ?", (source, effect)).fetchall()
    finally:
        c.close()


def blocks(w, d, watch):
    """the probe world's six blocks; `watch(label)` is called after the blocks named in the probes (the three points and the end)"""
    import world_journal as WJ
    sink = WJ.attach(w, SOURCE, out_dir=d)
    w.marker('Exod 19:1', 10, value='the third month')                                                          # block 1: MARKER
    watch('m1')
    w.submit({'kind': 'installation_commanded', 'subject': 'the-people', 'case_source': 'Exod 19:5'})          # block 2: EVENT, TIMER-SET (due 17), bound [10, null]
    w.marker('Exod 19:16', 12, value='the third day')                                                           # block 3: MARKER (closes [10, 12])
    w.submit({'kind': 'custody_three_days', 'subject': 'the-blasphemer', 'case_source': 'Lev 24:12 — probe: the custody act'})   # block 4: EVENT, WRITE (the debit open), bound [12, null]
    watch('s2')
    w.marker('Exod 24:1', 20, value='after')                                                                    # block 5: TIMER-FIRE + WRITE (sealed inside the walk, bound [10, 12] closed), MARKER
    w.submit({'kind': 'statute_set', 'subject': 'moses', 'case_source': 'Lev 24:13 — probe: the output'})     # block 6: EVENT, CLOSE, WRITE, bound [20, null]
    watch('s3')
    return sink


EXPECT = {'m1': 1, 's2': 6, 's3': 12}      # the lines sealed after each watched block: 1; 1+2+1+2; +3 (the fire's two and the marker) +3


@probe('L1 the body file is live: after each of three blocks it holds exactly the lines sealed so far and its chain verifies')
def l1():
    import world_journal as WJ
    w = new_world([law_timer, law_debit])
    seen = {}
    with tempfile.TemporaryDirectory() as d:
        def watch(label):
            lines, p = body_lines(d)
            seen[label] = (None if lines is None else len(lines), None if lines is None else WJ.verify_body(p))
        blocks(w, d, watch)
    ok = all(seen.get(k) == (n, True) for k, n in EXPECT.items())
    return ok, 'lines and chain after each block %s (expected %s)' % (seen, EXPECT)


@probe('L2 the index is live: the rows equal the lines at each point; the debit OPEN after the custody act and CLOSED after the output')
def l2():
    w = new_world([law_timer, law_debit])
    seen = {}
    with tempfile.TemporaryDirectory() as d:
        def watch(label):
            rows = live_rows(d)
            seen[label] = (None if rows is None else len(rows), ledger_row(d) if rows is not None and label != 'm1' else None)
        blocks(w, d, watch)
    ok = (seen.get('m1', (None,))[0] == 1 and seen.get('s2') == (6, [(1, None)]) and seen.get('s3') == (12, [(0, 20)]))
    return ok, 'rows and the debit row after each block %s' % seen


@probe('L3 the seal\'s form: fired_by complete, the bound [x, null] at the seal, the closing marker after it, a fire inside a later walk with its bound closed')
def l3():
    w = new_world([law_timer, law_debit])
    got = {}
    with tempfile.TemporaryDirectory() as d:
        def watch(label):
            if label == 's3':
                lines, p = body_lines(d)
                got['lines'] = [json.loads(l) for l in lines]
        blocks(w, d, watch)
    ev = got.get('lines', [])
    e1 = ev[1] if len(ev) > 1 else {}          # block 2's EVENT
    e4 = ev[4] if len(ev) > 4 else {}          # block 4's EVENT
    m5 = ev[8] if len(ev) > 8 else {}          # block 5's MARKER (after the fire's two lines)
    f5 = ev[6] if len(ev) > 6 else {}          # block 5's TIMER-FIRE
    ok = (e1.get('kind') == 'run.event' and e1['data'].get('fired_by') == ['law_timer'] and e1['data'].get('bound') == [10, None]
          and e4.get('kind') == 'run.event' and e4['data'].get('fired_by') == ['law_debit'] and e4['data'].get('bound') == [12, None]
          and f5.get('kind') == 'run.timer_fire' and f5['data'].get('bound') == [10, 12]
          and m5.get('kind') == 'run.marker' and m5.get('op') == 20)
    return ok, 'event 2 fired_by %r bound %r; event 5 fired_by %r bound %r; fire bound %r; marker op %r' % (
        e1.get('data', {}).get('fired_by'), e1.get('data', {}).get('bound'), e4.get('data', {}).get('fired_by'), e4.get('data', {}).get('bound'),
        f5.get('data', {}).get('bound'), m5.get('op'))


@probe('L4 the seal and the audit: the segment written (header + the same bytes), the body file gone, verify() true, the audit passes')
def l4():
    import world_journal as WJ
    w = new_world([law_timer, law_debit])
    with tempfile.TemporaryDirectory() as d:
        sink = blocks(w, d, lambda label: None)
        body, bp = body_lines(d)
        path, n, coerced = sink.seal()
        gone = not os.path.exists(bp)
        seg = [l for l in open(path, encoding='utf-8').read().split('\n') if l.strip()]
        head = json.loads(seg[0])
        same = seg[1:] == body
        ver = WJ.verify(path)
        a = sink.audit
    ok = (gone and same and ver and n == 12 == len(w.log) and coerced == 0 and head.get('events') == 12
          and a.get('lines') == 12 and a.get('chain') is True and a.get('fields_equal') is True and a.get('right_edge_closed_after') == 4
          and a.get('index_equal') is True and a.get('ok') is True)
    return ok, 'body gone %r; same bytes %r; verify %r; n %d coerced %d; audit %s' % (gone, same, ver, n, coerced, a)


@probe('L5 determinism through the live path: two live runs in two directories are byte-identical, segments and rows')
def l5():
    outs = []
    for _ in range(2):
        w = new_world([law_timer, law_debit])
        with tempfile.TemporaryDirectory() as d:
            sink = blocks(w, d, lambda label: None)
            rows = live_rows(d)
            path, n, _ = sink.seal()
            outs.append((open(path, 'rb').read(), rows))
    ok = outs[0] == outs[1] and len(outs[0][0]) > 0 and outs[0][1] and len(outs[0][1]) == 12
    return ok, 'segments %d bytes each %s; rows %s %s' % (len(outs[0][0]), 'IDENTICAL' if outs[0][0] == outs[1][0] else 'DIFFER',
                                                         len(outs[0][1] or []), 'IDENTICAL' if outs[0][1] == outs[1][1] else 'DIFFER')


@probe('L6 the crash-safe trace: a refusal inside a daemon leaves the lines sealed before it on disk, the prefix verifying')
def l6():
    import world_journal as WJ
    w = new_world([law_timer, law_refuse])
    with tempfile.TemporaryDirectory() as d:
        WJ.attach(w, SOURCE, out_dir=d)
        w.marker('Exod 19:1', 10, value='the third month')
        w.submit({'kind': 'installation_commanded', 'subject': 'the-people', 'case_source': 'Exod 19:5'})
        w.marker('Exod 19:16', 12, value='the third day')
        refused = None
        try:
            w.submit({'kind': 'tablets_broken', 'subject': 'the-people', 'case_source': 'Exod 32:19'})
        except SystemExit as e:
            refused = str(e)
        lines, p = body_lines(d)
        ver = WJ.verify_body(p) if lines else None
        rows = live_rows(d)
    ok = (refused is not None and lines is not None and len(lines) == 5 == len(w.log) and ver is True and rows is not None and len(rows) == 5
          and json.loads(lines[-1])['kind'] == 'run.event' and json.loads(lines[-1])['data'].get('kind') == 'tablets_broken')
    return ok, 'refused %r; body lines %s of log %d; verify %r; rows %s' % ((refused or '')[:60], None if lines is None else len(lines), len(w.log), ver, None if rows is None else len(rows))


@probe('L7 the exam worlds pay nothing: a World with no journal logs as before — the attribute None, no file, no row')
def l7():
    w = new_world([law_timer])
    with tempfile.TemporaryDirectory() as d:
        os.environ['WORLD_JOURNAL_DIR'] = d
        try:
            w.marker('Exod 19:1', 10, value='the third month')
            w.submit({'kind': 'installation_commanded', 'subject': 'the-people', 'case_source': 'Exod 19:5'})
            w.marker('Exod 24:1', 20, value='after')
            files = os.listdir(d)
        finally:
            del os.environ['WORLD_JOURNAL_DIR']
    ok = hasattr(w, 'journal') and w.journal is None and len(w.log) == 6 and files == []
    return ok, 'journal attr %r; log %d lines; files in the data dir %s' % (getattr(w, 'journal', 'MISSING'), len(w.log), files)


if __name__ == '__main__':
    ok = sum(1 for _, o, _ in results if o)
    print('THE LOOP — STEP 7 (a) WRITE AS YOU GO: the fire-probes')
    for name, o, note in results:
        print('  %s  %s\n        %s' % ('PASS' if o else 'FAIL', name, note))
    print('%d/%d probes' % (ok, len(results)))
    sys.exit(0 if ok == len(results) else 1)
