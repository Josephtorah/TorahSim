#!/usr/bin/env python3
"""step_probes.py — THE LOOP's step 7 part (b) THE STEPPER fire-probes (2026-09-14; THE_LOOP.md "Step 7 THE LOOP THAT WAITS — part (b)
THE STEPPER: the design", decision D15 THE TAPE AS A GENERATOR), written BEFORE world_stepper.py. Against the unchanged tree every probe
must FAIL (the module does not exist); after the code every probe must PASS. The probe tape is a SOURCE TEXT of six lines over
live_probes' two daemons, transformed exactly as the real tape is; every session journals into a temporary directory. Nine probes:
  S1 THE GENERATOR — transform(source) yields once per engine-call line, BEFORE the call, with the call's verse; the yields equal the calls
     (6); one next() runs exactly one call
  S2 STEP BY CALL — six steps seal 1, 2, 2, 1, 3, 3 lines; at every pause the body file and the live rows hold exactly the lines so far; the
     seventh step reports the end; the segment sealed, the audit ok
  S3 THE GRAINS — by 'verse' the two calls at Exod 19:5 are one step; by 'marker' the calls through each marker are one step; by 'day' a step
     ends when the clock moved; by the verse address 'Exod 24:1' the stepper stops at the LEFT EDGE, nothing of it run
  S4 FROM A VERSE — Stepper(from_verse='Exod 24:1') replays to the left edge with no pause; the position, six lines sealed, the debit OPEN in
     the live database under the stepper's source
  S5 THE AUDIT — a base written by a straight run of the same tape through the live sink; the stepper with that base reports every step
     audited; a stepper over a CHANGED tape is REFUSED at the step where they diverge, the ordinal named
  S6 THE EARLY CLOSE — close() after two steps seals a partial segment of three lines, the audit ok, the body gone, the base untouched
  S7 THE STATE FROM THE DATABASE — the report's clock, position, next verse, entities, open entries, pending timers; `ledger the_court` from
     the live database OPEN after the third line and CLOSED (day 20) after the sixth
  S8 THE REAL TAPE'S CONTRACT — the transform of cold_run_sequence's own tape section (read as text, never imported) compiles and yields
     exactly 1,507 times (1,279 submits + 157 markers + 71 closes)
  S9 EVERY CALL YIELDS A VERSE — no None over the real tape (added after the first sessions' miss: double-quoted sources)
Not run by the sweep; run by hand at the sitting and after any engine edit. Run: python3 World/step9/step_probes.py
"""
import os, sys, json, sqlite3, tempfile
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import world_engine as WE
import live_probes as LP                      # the two probe daemons and the registry map

results = []


def probe(name):
    def deco(fn):
        try:
            ok, note = fn()
        except BaseException as e:                   # the module or the construct is missing: a FAIL, named
            ok, note = False, '%s: %s' % (type(e).__name__, str(e)[:220])
        results.append((name, bool(ok), note))
        return fn
    return deco


SRC = '''def tape(w, M, P):
    w.marker('Exod 19:1', 10, value='the third month')
    w.submit({'kind': 'installation_commanded', 'subject': 'the-people', 'case_source': 'Exod 19:5'})
    w.submit({'kind': 'custody_three_days', 'subject': 'the-blasphemer', 'case_source': 'Exod 19:5 — probe: the custody act'})
    w.marker('Exod 19:16', 12, value='the third day')
    w.marker('Exod 24:1', 20, value='after')
    w.submit({'kind': 'statute_set', 'subject': 'moses', 'case_source': 'Lev 24:13 — probe: the output'})
'''
SOURCE = 'cold_run_sequence/stepper'
LINES_PER_CALL = [1, 2, 2, 1, 3, 3]           # marker; event + timer set; event + the debit; marker; the fire + its write + marker; event + close + write


def world():
    w = WE.World(era='probe', epoch='count', registry=LP.REG)
    w.laws = [LP.law_timer, LP.law_debit]
    return w


def stepper(d, **kw):
    import world_stepper as WS
    return WS.Stepper(tape_source=SRC, world=world(), out_dir=d, namespace={}, **kw)


def body_and_rows(d):
    p = os.path.join(d, 'L3_run_cold_run_sequence_stepper.jsonl.live')
    lines = [l for l in open(p, encoding='utf-8').read().split('\n') if l.strip()] if os.path.exists(p) else None
    return lines, LP.live_rows(d, SOURCE)


@probe('S1 the generator: one yield per engine-call line, before the call, with its verse; a next() runs exactly one call')
def s1():
    import world_stepper as WS
    src, n = WS.transform(SRC)
    ns = {}
    exec(src, ns)
    w = world()
    g = ns['tape'](w, {}, {})
    first = next(g)                                  # yields the first call's verse, runs nothing
    n0 = len(w.log)
    second = next(g)                                 # runs the marker, yields the next call's verse
    n1 = len(w.log)
    third = next(g)                                  # runs the submit (event + timer set)
    n2 = len(w.log)
    ok = (n == 6 and src.count('yield') == 6 and first[0] == 'Exod 19:1' and n0 == 0 and second[0] == 'Exod 19:5' and n1 == 1
          and third[0] == 'Exod 19:5' and n2 == 3 and first[1] == 2)
    return ok, 'yields %d; first %r (log %d), after one next %r (log %d), after two %r (log %d)' % (n, first, n0, second, n1, third, n2)


@probe('S2 step by call: 1, 2, 2, 1, 3, 3 lines; the body and the rows current at every pause; the seventh step the end; sealed, audited')
def s2():
    with tempfile.TemporaryDirectory() as d:
        st = stepper(d)
        per, current = [], []
        for _ in range(6):
            r = st.step('call')
            per.append(r['sealed'])
            lines, rows = body_and_rows(d)
            current.append((len(lines) if lines else 0, len(rows) if rows else 0, r['sealed_total']))
        r7 = st.step('call')
        path, n, coerced = st.close()
        a = st.sink.audit
        seg = [l for l in open(path, encoding='utf-8').read().split('\n') if l.strip()]
    ok = (per == LINES_PER_CALL and all(a_ == b_ == c_ for a_, b_, c_ in current) and current[-1][0] == 12 and r7['done'] and r7['sealed'] == 0
          and n == 12 and a.get('ok') and len(seg) == 13)
    return ok, 'lines per step %s; (body, rows, total) at each pause %s; step 7 done %r; sealed %d, audit ok %r' % (per, current, r7.get('done'), n, a.get('ok'))


@probe('S3 the grains: verse, marker, day, and a verse address at the left edge')
def s3():
    out = {}
    with tempfile.TemporaryDirectory() as d:
        st = stepper(d); st.step('call'); r = st.step('verse'); out['verse'] = (r['sealed'], r['next_verse'], [v for v, i in r['ran']]); st.close()
    with tempfile.TemporaryDirectory() as d:
        st = stepper(d); out['marker'] = [(st.step('marker')['sealed']) for _ in range(4)]; st.close()
    with tempfile.TemporaryDirectory() as d:
        st = stepper(d); rs = [st.step('day') for _ in range(4)]; out['day'] = [(r['sealed'], r['day']) for r in rs]; st.close()
    with tempfile.TemporaryDirectory() as d:
        st = stepper(d); r = st.step('Exod 24:1'); out['edge'] = (r['sealed'], r['day'], r['next_verse'], r['verse_reached'], len(r['ran'])); st.close()
    ok = (out['verse'] == (4, 'Exod 19:16', ['Exod 19:5', 'Exod 19:5'])
          and out['marker'] == [1, 5, 3, 3]
          and out['day'] == [(1, 10), (5, 12), (3, 20), (3, 20)]
          and out['edge'] == (6, 12, 'Exod 24:1', ('Exod', 19, 16), 4))
    return ok, '%s' % out


@probe('S4 from a verse: the replay to the left edge with no pause; the position; the debit open in the live database')
def s4():
    import world_journal as WJ
    with tempfile.TemporaryDirectory() as d:
        st = stepper(d, from_verse='Exod 24:1')
        r = st.report
        rows = WJ.ask(os.path.join(d, 'world.sqlite'), 'ledger', 'the_court', source=SOURCE)
        st.close()
    ok = (r['steps'] == 0 and r['sealed_total'] == 6 and r['next_verse'] == 'Exod 24:1' and r['day'] == 12 and r['verse_reached'] == ('Exod', 19, 16)
          and len(rows) == 1 and rows[0]['open'] == 1 and rows[0]['state'] == 'open')
    return ok, 'steps %s, sealed %s, next %s, day %s, reached %s; the court\'s ledger from the database %s' % (
        r.get('steps'), r.get('sealed_total'), r.get('next_verse'), r.get('day'), r.get('verse_reached'), [(x['effect'], x['open'], x['state']) for x in rows])


@probe('S5 the audit: every step audited against a base of the same tape; a changed tape refused at the diverging ordinal')
def s5():
    import world_journal as WJ, world_stepper as WS
    with tempfile.TemporaryDirectory() as d1, tempfile.TemporaryDirectory() as d2, tempfile.TemporaryDirectory() as d3:
        w = world()
        WJ.attach(w, 'probe/base', out_dir=d1)
        ns = {}; exec(SRC, ns); ns['tape'](w, {}, {})
        base, n, _ = WJ.sink(w, 'probe/base', out_dir=d1)
        st = WS.Stepper(tape_source=SRC, world=world(), out_dir=d2, namespace={}, base=base)
        audited = [st.step('call')['audited'] for _ in range(6)]
        st.close()
        changed = SRC.replace("'subject': 'the-blasphemer'", "'subject': 'the-stranger'")
        st2 = WS.Stepper(tape_source=changed, world=world(), out_dir=d3, namespace={}, base=base)
        st2.step('call'); st2.step('call')
        refused = None
        try:
            st2.step('call')
        except SystemExit as e:
            refused = str(e)
    ok = audited == [True] * 6 and refused is not None and 'REFUSED' in refused and 'ordinal 4' in refused
    return ok, 'audited %s; the changed tape: %s' % (audited, (refused or 'NOT REFUSED')[:140])


@probe('S6 the early close: a partial segment of three lines sealed, the audit ok, the body gone, the base untouched')
def s6():
    import world_journal as WJ
    with tempfile.TemporaryDirectory() as d:
        st = stepper(d)
        st.step('call'); st.step('call')
        path, n, coerced = st.close()
        body = os.path.join(d, 'L3_run_cold_run_sequence_stepper.jsonl.live')
        head = json.loads(open(path, encoding='utf-8').readline())
        a = st.sink.audit
        rows = LP.live_rows(d, SOURCE)
        ver = WJ.verify(path)
    ok = n == 3 and head.get('events') == 3 and a.get('ok') and not os.path.exists(body) and len(rows) == 3 and ver
    return ok, 'sealed %d lines, header events %s, audit ok %s, body gone %s, rows %d, verify %s' % (n, head.get('events'), a.get('ok'), not os.path.exists(body), len(rows or []), ver)


@probe('S7 the state from the database: the report\'s fields at a pause; the court\'s ledger open then closed, read through the views')
def s7():
    import world_journal as WJ
    with tempfile.TemporaryDirectory() as d:
        st = stepper(d)
        db = os.path.join(d, 'world.sqlite')
        for _ in range(3):
            r3 = st.step('call')
        open3 = WJ.ask(db, 'ledger', 'the_court', source=SOURCE)
        for _ in range(3):
            r6 = st.step('call')
        closed6 = WJ.ask(db, 'ledger', 'the_court', source=SOURCE)
        shown = st.show('open')
        st.close()
    ok = (r3['day'] == 10 and r3['verse_reached'] == ('Exod', 19, 5) and r3['next_verse'] == 'Exod 19:16' and r3['entities'] == 1      # the court alone: a timer's subject is not an entity until the fire writes it (THE TENT sitting 2's lesson) — corrected before the code, on the engine's own rule
          and r3['open_entries'] == 1 and r3['pending_timers'] == 1
          and open3 and open3[0]['open'] == 1 and open3[0]['day_closed'] is None
          and closed6 and closed6[0]['open'] == 0 and closed6[0]['day_closed'] == 20 and r6['open_entries'] == 0 and r6['pending_timers'] == 0
          and shown == [])
    return ok, 'after 3: day %s reached %s next %s entities %s open %s pending %s; the court open %s; after 6: closed %s, open %s pending %s; shown open at the end %s' % (
        r3.get('day'), r3.get('verse_reached'), r3.get('next_verse'), r3.get('entities'), r3.get('open_entries'), r3.get('pending_timers'),
        [(x['open'], x['day_closed']) for x in open3], [(x['open'], x['day_closed']) for x in closed6], r6.get('open_entries'), r6.get('pending_timers'), shown)


@probe('S8 the real tape\'s contract: the transform of the sequence runner\'s tape section compiles and yields exactly 1,507 times')
def s8():
    import world_stepper as WS
    text = open(os.path.join(HERE, 'cold_run_sequence.py'), encoding='utf-8').read()
    section = text.split('# ==== TAPE BEGIN', 1)[1].split('# ==== TAPE END ====', 1)[0].split('\n', 1)[1]
    src, n = WS.transform(section)
    compile(src, 'tape', 'exec')
    calls = section.count('w.submit(') + section.count('w.marker(') + section.count('w.close(')
    return n == calls == 1507, 'yields %d; calls counted %d (submit %d, marker %d, close %d)' % (n, calls, section.count('w.submit('), section.count('w.marker('), section.count('w.close('))


@probe('S9 every call of the real tape yields a verse — no None (the first sessions found double-quoted sources read as None; the probe added after the miss, 2026-09-14)')
def s9():
    import re, world_stepper as WS
    text = open(os.path.join(HERE, 'cold_run_sequence.py'), encoding='utf-8').read()
    section = text.split('# ==== TAPE BEGIN', 1)[1].split('# ==== TAPE END ====', 1)[0].split('\n', 1)[1]
    src, n = WS.transform(section)
    yielded = re.findall(r"yield \((None|'[^']*'|\"[^\"]*\"), (\d+)\);", src)
    nones = [i for v, i in yielded if v == 'None']
    books = {}
    for v, i in yielded:
        if v != 'None':
            books[v.strip('\'"').split(' ')[0]] = books.get(v.strip('\'"').split(' ')[0], 0) + 1
    return n == 1507 and len(yielded) == 1507 and not nones, 'yields %d, matched %d, None at lines %s; by book %s' % (n, len(yielded), nones[:8], books)


if __name__ == '__main__':
    ok = sum(1 for _, o, _ in results if o)
    print('THE LOOP — STEP 7 (b) THE STEPPER: the fire-probes')
    for name, o, note in results:
        print('  %s  %s\n        %s' % ('PASS' if o else 'FAIL', name, note))
    print('%d/%d probes' % (ok, len(results)))
    sys.exit(0 if ok == len(results) else 1)
