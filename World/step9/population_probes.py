#!/usr/bin/env python3
"""population_probes.py — THE POPULATION TABLE's fire-probes (THE NUMBERS WALK sitting 8b, 2026-09-11; the design in
World/step9/NUMBERS_WALK.md "Sitting 8b"; the speculation ARCHITECTURE/DATABASE_SPECULATION.md), written BEFORE the engine's table,
the schema registry, the journal's ninth class, the fifth view and the fifth question. Against the unchanged code every probe must
FAIL; after the code every probe must PASS. Nine probes on a SMALL world over registered kinds (a probe-only kind is refused by the
registry — the journal's lesson): the first census's event (census_taken, the twelve counts as the ink writes them), the daughters'
plea (daughters_approached — a person the ink names), a second census_taken with other counts (the deltas the table computes from
its own rows). The table's law: a row is written by a DAEMON consuming an event, never by hand; a row is validated against
World/step9/population_schema.yaml (the fifth registry — the columns the ink's own words); a row is not a ledger entry (no op, no
open, no close) and moves no count of the RUN tuple; it is the log's own class ROW, journaled as run.row, read back by the fifth view
run_population and the fifth question `population`.
  P1 a daemon writes counted rows on a census event: the table holds them with the schema's columns, written_by the daemon, the day
     the clock's, and a ROW line per row on the log
  P2 a row written by hand — outside a daemon's call — is REFUSED (never by hand)
  P3 a row with an unknown grain, a missing required column, or an unknown column is REFUSED — three refusals
  P4 the query: population(tribe=...) / population(grain='named') / population(as_of=...) return the rows and nothing else
  P5 the daemon reads its own rows: at the second census it writes DELTA rows computed from the table (declared numbers, the
     remainder labeled unexplained) — the table is the daemon's instrument
  P6 the journal: KINDS carries ROW -> run.row, the register carries run.row, the sink writes one run.row line per row with subj the
     registry id (a named row's person) or the tribe's name (a counted row), unit the daemon, ref the verse
  P7 the fifth view run_population: one row per run.row with the columns extracted; the views gate carries the population check
     and passes on the probe world
  P8 the fifth question `population [tribe]`: every row, then one tribe's rows in seq order
  P9 the RUN counts do not move: the world's writes / timers / entities are what the ledger effects alone make — the rows add none
Not run by the sweep; run by hand at the sitting and after any engine or journal edit. Run: python3 World/step9/population_probes.py
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
        except BaseException as e:                   # the old code lacks the construct: a FAIL, named
            ok, note = False, '%s: %s' % (type(e).__name__, str(e)[:200])
        results.append((name, bool(ok), note))
        return fn
    return deco


COUNTS_1 = {'reuben': 46500, 'simeon': 59300, 'gad': 45650}
COUNTS_2 = {'reuben': 43730, 'simeon': 22200, 'gad': 40500}


def law_probe_rows(event, world):
    """the probe daemon: counted rows at a census, a named row at the plea, delta rows at the second census from the table's own rows"""
    k, src = event['kind'], event['case_source']
    if k == 'census_taken':
        prior = world.population(grain='counted', family=None)
        for t, n in event['counts'].items():
            world.row('population', {'grain': 'counted', 'as_of': src.split(' — ')[0], 'subject': t, 'tribe': t, 'family': None, 'count': n, 'source': src})
        if prior:
            by = {r['tribe']: r for r in prior}
            for t, n in event['counts'].items():
                if t in by:
                    d = n - by[t]['count']
                    explained = [{'source': 'Num 25:9', 'count': 24000, 'tribe_by': 'the shelf'}] if t == 'simeon' else []
                    world.row('population', {'grain': 'delta', 'as_of': src.split(' — ')[0], 'subject': t, 'tribe': t, 'from_verse': by[t]['as_of'], 'to_verse': src.split(' — ')[0],
                                             'delta': d, 'explained': explained, 'unexplained': d + sum(x['count'] for x in explained), 'source': src})
        return []
    if k == 'daughters_approached':
        for p in event.get('persons') or [event['subject']]:
            world.row('population', {'grain': 'named', 'as_of': src.split(' — ')[0], 'subject': p, 'person': p, 'tribe': 'manasseh', 'family': 'the Hepherite', 'father': 'zelophehad', 'status': 'no sons, only daughters', 'source': src})
        return []
    return []


REG = {'the-people': 'israel_people', 'the-daughters-of-zelophehad': 'the_daughters_of_zelophehad'}
SOURCE = 'population_probes/probe'


def probe_world():
    w = WE.World(era='probe', epoch='count', registry=REG)
    w.laws = [law_probe_rows]
    w.marker('Num 1:1', 10, value='the first census')
    w.submit({'kind': 'census_taken', 'subject': 'the-people', 'counts': dict(COUNTS_1), 'total': sum(COUNTS_1.values()), 'case_source': 'Num 1:17-19 — probe: the first census'})
    w.marker('Num 25:19', 20, value='after the plague')
    w.submit({'kind': 'daughters_approached', 'subject': 'the-daughters-of-zelophehad', 'persons': ['the-daughters-of-zelophehad'], 'case_source': 'Num 26:33 — probe: the daughters named on the roll'})
    w.submit({'kind': 'census_taken', 'subject': 'the-people', 'counts': dict(COUNTS_2), 'total': sum(COUNTS_2.values()), 'case_source': 'Num 26:1-51 — probe: the second census'})
    return w


def build(w, d):
    import world_journal as WJ
    path, n, coerced = WJ.sink(w, source=SOURCE, out_dir=d)
    db = os.path.join(d, 'probe.sqlite')
    WJ.index(db, [path])
    WJ.views(db)
    return db, path


def q(db, sql, *args):
    c = sqlite3.connect(db)
    try:
        return c.execute(sql, args).fetchall()
    finally:
        c.close()


@probe('P1 a daemon writes counted rows on a census event — the table, the columns, the writer, the day, a ROW line per row')
def p1():
    w = probe_world()
    rows = [r for r in w.tables['population'] if r['grain'] == 'counted']
    lines = [l for l in w.log if l[0] == 'ROW']
    first = rows[0] if rows else {}
    ok = len(rows) == 6 and all(r['written_by'] == 'law_probe_rows' for r in rows) and [r['day'] for r in rows[:3]] == [10, 10, 10] and [r['day'] for r in rows[3:]] == [20, 20, 20] \
        and first.get('tribe') == 'reuben' and first.get('count') == 46500 and first.get('as_of') == 'Num 1:17-19' and len(lines) == len(w.tables['population'])
    return ok, 'counted rows %d (written_by %s; days %s); ROW lines %d of %d rows; the first %s' % (len(rows), sorted({r.get('written_by') for r in rows}), [r['day'] for r in rows], len(lines), len(w.tables['population']), {k: first.get(k) for k in ('grain', 'as_of', 'tribe', 'count')})


@probe('P2 a row written by hand — outside a daemon\'s call — is REFUSED')
def p2():
    w = probe_world()
    try:
        w.row('population', {'grain': 'counted', 'as_of': 'Num 1:1', 'subject': 'dan', 'tribe': 'dan', 'family': None, 'count': 62700, 'source': 'Num 1:39 — by hand'})
        return False, 'the hand-written row was accepted'
    except SystemExit as e:
        return 'never by hand' in str(e) or 'daemon' in str(e), 'refused: %s' % str(e)[:160]


@probe('P3 an unknown grain, a missing required column, an unknown column — three refusals')
def p3():
    notes = []
    for bad in ({'grain': 'tally', 'as_of': 'Num 1:1', 'subject': 'dan', 'tribe': 'dan', 'family': None, 'count': 1, 'source': 'x'},
                {'grain': 'counted', 'as_of': 'Num 1:1', 'subject': 'dan', 'tribe': 'dan', 'family': None, 'source': 'x'},
                {'grain': 'counted', 'as_of': 'Num 1:1', 'subject': 'dan', 'tribe': 'dan', 'family': None, 'count': 1, 'source': 'x', 'colour': 'blue'}):
        w = WE.World(era='probe', epoch='count', registry=REG)
        def law_bad(event, world, bad=bad):
            world.row('population', bad); return []
        w.laws = [law_bad]
        try:
            w.submit({'kind': 'census_taken', 'subject': 'the-people', 'counts': {}, 'total': 0, 'case_source': 'Num 1:17 — probe'})
            notes.append('ACCEPTED')
        except SystemExit as e:
            notes.append('refused: ' + str(e)[:80])
    return all(n.startswith('refused') for n in notes) and len(notes) == 3, ' | '.join(notes)


@probe('P4 the query: by tribe, by grain, by as_of — the rows and nothing else')
def p4():
    w = probe_world()
    a = w.population(tribe='simeon'); b = w.population(grain='named'); c = w.population(as_of='Num 26:1-51'); d = w.population(grain='counted', as_of='Num 1:17-19')
    ok = [r['grain'] for r in a] == ['counted', 'counted', 'delta'] and len(b) == 1 and b[0]['person'] == 'the-daughters-of-zelophehad' and b[0]['status'] == 'no sons, only daughters' \
        and len(c) == 6 and len(d) == 3 and w.population(tribe='levi') == []
    return ok, 'simeon %s; named %d; as_of 26 %d; counted at 1 %d; levi %d' % ([r['grain'] for r in a], len(b), len(c), len(d), len(w.population(tribe='levi')))


@probe('P5 the daemon reads its own rows: delta rows computed from the table — declared, the remainder labeled')
def p5():
    w = probe_world()
    d = {r['tribe']: r for r in w.population(grain='delta')}
    ok = set(d) == {'reuben', 'simeon', 'gad'} and d['simeon']['delta'] == -37100 and d['simeon']['unexplained'] == -13100 and d['simeon']['explained'][0]['count'] == 24000 \
        and d['reuben']['delta'] == -2770 and d['reuben']['unexplained'] == -2770 and d['reuben']['explained'] == [] and d['simeon']['from_verse'] == 'Num 1:17-19' and d['simeon']['to_verse'] == 'Num 26:1-51'
    return ok, 'deltas %s' % {t: (r['delta'], r['unexplained'], len(r['explained'])) for t, r in d.items()}


@probe('P6 the journal: KINDS carries ROW, the register carries run.row, the sink writes run.row lines with subj / unit / ref')
def p6():
    import yaml, world_journal as WJ
    reg = yaml.safe_load(open(os.path.join(HERE, '..', 'journal', 'registers', 'event_kinds.yaml'), encoding='utf-8'))
    ids = {k['id'] for k in reg['kinds']}
    w = probe_world()
    with tempfile.TemporaryDirectory() as d:
        db, path = build(w, d)
        evs = [json.loads(l) for l in open(path, encoding='utf-8').read().splitlines()[1:]]
    rows = [e for e in evs if e['kind'] == 'run.row']
    named = [e for e in rows if e['data'].get('grain') == 'named']
    ok = WJ.KINDS.get('ROW') == 'run.row' and 'run.row' in ids and len(rows) == len(w.tables['population']) and rows[0]['subj'] == 'reuben' and rows[0]['prov']['unit'] == 'law_probe_rows' \
        and rows[0]['prov']['ref'].startswith('Num 1:17-19') and len(named) == 1 and named[0]['subj'] == 'the_daughters_of_zelophehad'
    return ok, 'KINDS ROW -> %s; registered %s; run.row lines %d of %d rows; first subj %s unit %s ref %s; the named row\'s subj %s' % (
        WJ.KINDS.get('ROW'), 'run.row' in ids, len(rows), len(w.tables['population']), rows[0]['subj'] if rows else None, rows[0]['prov']['unit'] if rows else None, (rows[0]['prov']['ref'] or '')[:12] if rows else None, named[0]['subj'] if named else None)


@probe('P7 the fifth view run_population: one row per run.row with the columns extracted; the views gate carries the population check')
def p7():
    import world_journal as WJ
    w = probe_world()
    with tempfile.TemporaryDirectory() as d:
        db, path = build(w, d)
        rows = q(db, 'select grain, as_of, tribe, family, person, count, delta, written_by, verse from run_population where source = ? order by seq', SOURCE)
        n_row = q(db, "select count(*) from events where kind = 'run.row'")[0][0]
        ok_gate, lines = WJ.views_gate(db)
        vc = WJ.view_counts(db)[SOURCE]
    ok = len(rows) == n_row == len(w.tables['population']) and rows[0][:3] == ('counted', 'Num 1:17-19', 'reuben') and rows[0][5] == 46500 and rows[3][0] == 'named' and rows[3][4] == 'the-daughters-of-zelophehad' \
        and any(r[0] == 'delta' and r[2] == 'simeon' and r[6] == -37100 for r in rows) and ok_gate and vc.get('population') == n_row
    return ok, 'view rows %d = run.row %d = table %d; gate %s (population %s); first %s' % (len(rows), n_row, len(w.tables['population']), ok_gate, vc.get('population'), rows[0] if rows else None)


@probe('P8 the fifth question `population [tribe]`: every row, then one tribe\'s in seq order')
def p8():
    import world_journal as WJ
    w = probe_world()
    with tempfile.TemporaryDirectory() as d:
        db, path = build(w, d)
        allr = WJ.ask(db, 'population', source=SOURCE)
        sim = WJ.ask(db, 'population', 'simeon', source=SOURCE)
    ok = len(allr) == len(w.tables['population']) and [r['grain'] for r in sim] == ['counted', 'counted', 'delta'] and sim[0]['count'] == 59300 and sim[1]['count'] == 22200 and sim[2]['delta'] == -37100 \
        and all(r['seq'] <= s['seq'] for r, s in zip(sim, sim[1:]))
    return ok, 'all %d; simeon %s' % (len(allr), [(r['grain'], r.get('count'), r.get('delta')) for r in sim])


@probe('P9 the RUN counts do not move: the rows are no writes, no timers, no entities')
def p9():
    w = probe_world()
    writes = [l for l in w.log if l[0] in ('WRITE', 'RETRO-WRITE')]; tset = [l for l in w.log if l[0] == 'TIMER-SET']
    ok = len(w.tables['population']) == 10 and writes == [] and tset == [] and len(w.entities) == 0 and sum(1 for l in w.log if l[0] == 'EVENT') == 3
    return ok, 'rows %d; writes %d; timers set %d; entities %d; events %d' % (len(w.tables['population']), len(writes), len(tset), len(w.entities), sum(1 for l in w.log if l[0] == 'EVENT'))


if __name__ == '__main__':
    n = sum(1 for _, ok, _ in results if ok)
    for name, ok, note in results:
        print('%s %s\n      %s' % ('PASS' if ok else 'FAIL', name, note))
    print('\n%d/%d population probes' % (n, len(results)))
