#!/usr/bin/env python3
"""port_probes.py — THE LOOP's step 7 part (c) THE PORT fire-probes (2026-09-14; THE_LOOP.md "Step 7 THE LOOP THAT WAITS — part (c)
THE PORT: the design", decisions D16-D18), written BEFORE world_port.py and the stepper's hooks. Against the unchanged tree every probe
must FAIL; after the code every probe must PASS. The probe tape and daemons are step_probes' and live_probes'; every queue is written
into a temporary directory. Nine probes:
  P1 THE QUEUE READS AND REFUSES — two items load with their positions; an unregistered kind REFUSED at open; an unknown field REFUSED;
     a bad position REFUSED; a registered field the item lacks a printed warning, not a refusal
  P2 THE ONE DOOR — an item with no position enters at the first pause through World.submit: the daemon fires, event + write sealed in
     the session's segment and rows, the EVENT line prov.unit 'port:<queue>' and data.port {queue, id, label}
  P3 THE POSITION — an item at 'Exod 24:1' enters at the left edge: after the tape's fourth line and before its fifth in the sealed
     order; a session started past the item's verse REFUSES the queue at open
  P4 THE FORK — the prefix before the first input audited against the base; from the input on the report says forked, the ordinal and
     the item named; the sealed header carries base, fork, forked_by, queue
  P5 THE FUTURE CHANGES — an item that sets a timer at the first pause fires at the later marker: more lines than the base, no refusal
  P6 DETERMINISM — two sessions over one queue seal byte-identical segments and identical rows
  P7 THE END IS A PAUSE — an item positioned past the tape's last verse enters after the last tape line, before the seal
  P8 THE TEXT ALONE — a session with no queue seals the base's body byte for byte
  P9 THE ORDER — two items due at one pause and the tape line: item 1, item 2, then the line
Not run by the sweep; run by hand at the sitting and after any engine edit. Run: python3 World/step9/port_probes.py
"""
import os, sys, json, tempfile
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import yaml
import world_engine as WE
import events_layer as EV
import live_probes as LP
import step_probes as SP

results = []


def probe(name):
    def deco(fn):
        try:
            ok, note = fn()
        except BaseException as e:                   # the module or the construct is missing: a FAIL, named
            ok, note = False, '%s: %s' % (type(e).__name__, str(e)[:240])
        results.append((name, bool(ok), note))
        return fn
    return deco


def item(id_, at, kind='custody_three_days', subject='the-stranger', label='the probe item', **fields):
    ev = dict(kind=kind, subject=subject, case_source='%s — probe: %s' % (at or 'Exod 19:1', id_))
    ev.update(fields)
    return {'id': id_, 'at': at, 'label': label, 'event': ev}


def queue(d, items, name='probe'):
    p = os.path.join(d, name + '.yaml')
    with open(p, 'w', encoding='utf-8') as f:
        yaml.safe_dump({'items': items}, f, allow_unicode=True, sort_keys=False)
    return p


def session(d, q, **kw):
    import world_stepper as WS
    return WS.Stepper(tape_source=SP.SRC, world=SP.world(), out_dir=d, namespace={}, queue=q, **kw)


SRC_NAME = 'cold_run_sequence/port@probe'


def seg_lines(path):
    return [l for l in open(path, encoding='utf-8').read().split('\n') if l.strip()]


@probe('P1 the queue reads and refuses: positions loaded; an unregistered kind, an unknown field, a bad position refused; a missing registered field a warning')
def p1():
    import world_port as WP
    with tempfile.TemporaryDirectory() as d:
        port = WP.Port(queue(d, [item('a', None), item('b', 'Exod 24:1')]))
        loaded = [(it['id'], it['at']) for it in port.items]
        refusals = {}
        for name, items in (('kind', [item('x', None, kind='no_such_kind')]), ('field', [item('x', None, zzz_unknown=1)]), ('at', [item('x', 'not a verse')])):
            try:
                WP.Port(queue(d, items, name=name)); refusals[name] = None
            except SystemExit as e:
                refusals[name] = str(e)[:80]
        listed = EV.REGISTRY['custody_three_days'].get('fields') or []
        warned = port.warnings
    ok = (loaded == [('a', None), ('b', 'Exod 24:1')] and port.name == 'probe' and all(v and 'REFUSED' in v for v in refusals.values())
          and isinstance(warned, list) and (bool(listed) == bool(warned)))
    return ok, 'loaded %s; refusals %s; registered fields %s; warnings %d' % (loaded, {k: (v or 'NOT REFUSED') for k, v in refusals.items()}, listed, len(warned))


@probe('P2 the one door: an unpositioned item enters at the first pause; event + write sealed; prov.unit port:<queue>; data.port {queue, id, label}')
def p2():
    with tempfile.TemporaryDirectory() as d:
        st = session(d, queue(d, [item('q1', None, label='the first input')]))
        r = st.step('call')
        rows = LP.live_rows(d, SRC_NAME)
        path, n, _ = st.close()
        evs = [json.loads(l) for l in seg_lines(path)[1:]]
    e0 = evs[0] if evs else {}
    ok = (r['inputs'] == ['q1'] and r['sealed'] == 3 and len(rows) == 3 and e0.get('kind') == 'run.event' and e0['prov'].get('unit') == 'port:probe'
          and e0['data'].get('port') == {'queue': 'probe', 'id': 'q1', 'label': 'the first input'} and evs[1]['kind'] == 'run.write' and evs[2]['kind'] == 'run.marker'
          and e0['subj'] == 'the-stranger')
    return ok, 'inputs %s, sealed %d, rows %d; first line %s prov %s port %s; then %s' % (r.get('inputs'), r.get('sealed'), len(rows or []), e0.get('kind'), e0.get('prov'), e0.get('data', {}).get('port'), [e['kind'] for e in evs[1:3]])


@probe('P3 the position: an item at Exod 24:1 enters at the left edge, after the fourth line and before the fifth; a session past it refuses the queue')
def p3():
    with tempfile.TemporaryDirectory() as d:
        q = queue(d, [item('q1', 'Exod 24:1')])
        st = session(d, q)
        rs = [st.step('call') for _ in range(6)]
        path, n, _ = st.close()
        evs = [json.loads(l) for l in seg_lines(path)[1:]]
        refused = None
        try:
            session(d, q, from_verse='Lev 24:13')
        except SystemExit as e:
            refused = str(e)[:100]
    kinds = [e['kind'] for e in evs]
    ok = (rs[4]['inputs'] == ['q1'] and rs[3]['inputs'] == [] and kinds[5] == 'run.marker' and kinds[6] == 'run.event' and evs[6]['prov']['unit'] == 'port:probe'
          and kinds[7] == 'run.write' and kinds[8] == 'run.timer_fire' and n == 14 and refused is not None and 'REFUSED' in refused)
    return ok, 'inputs per step %s; kinds %s; n %d; the later session: %s' % ([r['inputs'] for r in rs], kinds, n, refused or 'NOT REFUSED')


@probe('P4 the fork: audited before the first input; forked at its ordinal after; the header names base, fork, forked_by, queue')
def p4():
    import world_journal as WJ, world_stepper as WS
    with tempfile.TemporaryDirectory() as d1, tempfile.TemporaryDirectory() as d2:
        w = SP.world(); WJ.attach(w, 'probe/base', out_dir=d1)
        ns = {}; exec(SP.SRC, ns); ns['tape'](w, {}, {})
        base, _, _ = WJ.sink(w, 'probe/base', out_dir=d1)
        st = WS.Stepper(tape_source=SP.SRC, world=SP.world(), out_dir=d2, namespace={}, queue=queue(d2, [item('q1', 'Exod 24:1')]), base=base)
        rs = [st.step('call') for _ in range(6)]
        path, n, _ = st.close()
        head = json.loads(seg_lines(path)[0])
    ok = ([r['audited'] for r in rs[:4]] == [True] * 4 and rs[4]['fork'] == 7 and rs[4]['forked_by'] == 'q1' and rs[4]['audited'] is None
          and head.get('base') == os.path.basename(base) and head.get('fork') == 7 and head.get('forked_by') == 'q1' and head.get('queue') == 'probe')
    return ok, 'audited %s; fork %s by %s; header %s' % ([r['audited'] for r in rs], rs[4].get('fork'), rs[4].get('forked_by'), {k: head.get(k) for k in ('base', 'fork', 'forked_by', 'queue')})


@probe('P5 the future changes: an item setting a timer at the first pause fires at the later marker — more lines than the base, no refusal')
def p5():
    import world_journal as WJ, world_stepper as WS
    with tempfile.TemporaryDirectory() as d1, tempfile.TemporaryDirectory() as d2:
        w = SP.world(); WJ.attach(w, 'probe/base', out_dir=d1)
        ns = {}; exec(SP.SRC, ns); ns['tape'](w, {}, {})
        base, nb, _ = WJ.sink(w, 'probe/base', out_dir=d1)
        st = WS.Stepper(tape_source=SP.SRC, world=SP.world(), out_dir=d2, namespace={}, base=base,
                        queue=queue(d2, [item('t1', None, kind='installation_commanded', subject='the-people')]))
        r = st.run()
        path, n, _ = st.close()
        kinds = [json.loads(l)['kind'] for l in seg_lines(path)[1:]]
    # the fire's two lines come BEFORE the marker's own line — the walk fires inside the marker's call, its line logged after (part (a)'s L3);
    # the hand-typed index put the marker between them: corrected on the engine's own order after the first run, 2026-09-14
    ok = n == nb + 4 and kinds[:2] == ['run.event', 'run.timer_set'] and kinds[2:5] == ['run.timer_fire', 'run.write', 'run.marker'] and r['done'] and r['fork'] == 1
    return ok, 'base %d lines, the session %d; kinds %s; fork %s' % (nb, n, kinds, r.get('fork'))


@probe('P6 determinism: two sessions over one queue seal byte-identical segments and identical rows')
def p6():
    outs = []
    for _ in range(2):
        with tempfile.TemporaryDirectory() as d:
            st = session(d, queue(d, [item('q1', None), item('q2', 'Exod 24:1')]))
            st.run()
            rows = LP.live_rows(d, SRC_NAME)
            path, n, _ = st.close()
            outs.append((open(path, 'rb').read(), rows, n))
    ok = outs[0] == outs[1] and outs[0][2] == 16
    return ok, '%d lines each; segments %s; rows %s' % (outs[0][2], 'IDENTICAL' if outs[0][0] == outs[1][0] else 'DIFFER', 'IDENTICAL' if outs[0][1] == outs[1][1] else 'DIFFER')


@probe('P7 the end is a pause: an item positioned past the tape\'s last verse enters after the last line, before the seal')
def p7():
    with tempfile.TemporaryDirectory() as d:
        st = session(d, queue(d, [item('q_end', 'Lev 25:1')]))
        rs = [st.step('call') for _ in range(6)]
        path, n, _ = st.close()
        kinds = [json.loads(l)['kind'] for l in seg_lines(path)[1:]]
    ok = rs[5]['done'] and rs[5]['inputs'] == ['q_end'] and n == 14 and kinds[-2:] == ['run.event', 'run.write'] and all(r['inputs'] == [] for r in rs[:5])
    return ok, 'inputs per step %s; n %d; last kinds %s' % ([r['inputs'] for r in rs], n, kinds[-3:])


@probe('P8 the text alone: a session with no queue seals the base\'s body byte for byte')
def p8():
    import world_journal as WJ, world_stepper as WS
    with tempfile.TemporaryDirectory() as d1, tempfile.TemporaryDirectory() as d2:
        w = SP.world(); WJ.attach(w, 'probe/base', out_dir=d1)
        ns = {}; exec(SP.SRC, ns); ns['tape'](w, {}, {})
        base, nb, _ = WJ.sink(w, 'probe/base', out_dir=d1)
        st = WS.Stepper(tape_source=SP.SRC, world=SP.world(), out_dir=d2, namespace={}, base=base, queue=None)
        st.run(); path, n, _ = st.close()
        same = seg_lines(path)[1:] == seg_lines(base)[1:]
    return same and n == nb and st.port is None, 'bodies identical %s (%d lines); port %r' % (same, n, st.port)


@probe('P9 the order at one pause: item 1, item 2, then the tape line')
def p9():
    with tempfile.TemporaryDirectory() as d:
        st = session(d, queue(d, [item('q1', None, subject='the-stranger'), item('q2', None, subject='the-sojourner')]))
        r = st.step('call')
        path, n, _ = st.close()
        evs = [json.loads(l) for l in seg_lines(path)[1:]]
    kinds = [e['kind'] for e in evs[:5]]
    ok = (r['inputs'] == ['q1', 'q2'] and kinds == ['run.event', 'run.write', 'run.event', 'run.write', 'run.marker']
          and evs[0]['data']['port']['id'] == 'q1' and evs[2]['data']['port']['id'] == 'q2' and r['sealed'] == 5)
    return ok, 'inputs %s; kinds %s; ids %s' % (r.get('inputs'), kinds, [e['data'].get('port', {}).get('id') for e in evs[:3]])


if __name__ == '__main__':
    ok = sum(1 for _, o, _ in results if o)
    print('THE LOOP — STEP 7 (c) THE PORT: the fire-probes')
    for name, o, note in results:
        print('  %s  %s\n        %s' % ('PASS' if o else 'FAIL', name, note))
    print('%d/%d probes' % (ok, len(results)))
    sys.exit(0 if ok == len(results) else 1)
