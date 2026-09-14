#!/usr/bin/env python3
"""view_probes.py — THE LOOP's step 2 fire-probes for the FOUR VIEWS and the FOUR QUESTIONS (2026-09-09; THE_LOOP.md "Step 2 THE
INDEX — the remainder", decisions D7/D8), written BEFORE the index's source column, the engine's closed_day stamp, the view file
World/journal/run_views.sql and the ask-tool. Against the unchanged code every probe must FAIL; after the code every probe must
PASS. All six run in-process on a SMALL probe world over registered kinds — the journal probes' tape (markers forward, retrograde
and proleptic; a timer that fires, one cancelled, one pending; a retro-write) extended by the custody act (Joseph's
custody_three_days standing in), the output act (Marah's statute_set) that closes the docket's debit, and a law skipped under
from_event until the output installs it — so all EIGHT log classes, a close and a custody are on the segment. Six probes:
  V1 the index carries each row's SOURCE (the segment header's), and a closed entry carries closed_day beside closed_by
  V2 run_ledger's rows equal the write rows (run.write + run.retro_write); the closed entry shows its day and its closer
  V3 run_timers joins every fire and every cancel to exactly one set, and shows the pending one
  V4 run_clock lists the markers in seq order with all three classes (forward, retrograde, proleptic)
  V5 run_docket shows the declaration owed OPEN when sunk before the output, CLOSED at the output when sunk at the end
  V6 the four questions answer: the ledger at a day before and after the close; what stands open at a verse; who wrote this;
     what waits in custody — one row before the output, none after
Not run by the sweep; run by hand at the sitting and after any engine or journal edit. Run: python3 World/step9/view_probes.py
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


def _eff(effect, subject, event, **kw):
    d = {'effect': effect, 'subject': subject, 'counterparty': None, 'amount': None, 'due': None,
         'source_law': 'probe', 'case_source': event['case_source']}
    d.update(kw)
    return d


def law_probe(event, world):
    """the journal probes' daemon (a seven-day timer, an immediate status, a cancel) plus the custody act and the output act"""
    k = event['kind']
    day = event.get('day', world.clock.day)
    if k == 'installation_commanded':
        return [_eff('released', event['subject'], event, due=day + 7)]
    if k == 'people_answered':
        return [_eff('accepted', event['subject'], event)]
    if k == 'tablets_broken':
        world.cancel_timers(event['subject'], 'released', event['case_source'])
        return [_eff('accepted', event['subject'], event, value=False)]
    if k == 'custody_three_days':
        return [_eff('in_custody', event['subject'], event),
                _eff('declaration_owed', 'the-court', event, counterparty=event['subject'])]
    if k == 'statute_set':
        world.close('the-court', 'declaration_owed', event['case_source'])
        return [_eff('rule_installed', 'the-tabernacle', event, value='law_probe_late')]
    return []


def law_probe_late(event, world):
    """a law whose installing act never fires — skipped under from_event until the output's rule_installed names it"""
    if event['kind'] == 'people_answered':
        return [_eff('accepted', event['subject'], event, value='late')]
    return []


FIELDS = {'law_probe': {'given_at': 'Gen 1:1', 'installed_by': 'boot'},
          'law_probe_late': {'given_at': 'Exod 19:1', 'installed_by': 'entered_the_land'}}
REG = {'the-people': 'israel_people', 'the-court': 'the_court', 'the-tabernacle': 'the_tent_of_meeting'}
SOURCE = 'view_probes/probe'


def probe_world(upto=None):
    """the tape; `upto='custody'` stops after the custody act (the docket open)"""
    w = WE.World(era='probe', epoch='count', registry=REG, installation={'setting': 'from_event', 'fields': FIELDS})
    w.laws = [law_probe, law_probe_late]
    w.marker('Exod 19:1', 10, value='the third month')
    w.submit({'kind': 'installation_commanded', 'subject': 'the-people', 'case_source': 'Exod 19:5'})     # timer set: due 17
    w.marker('Exod 19:16', 12, value='the third day')
    w.submit({'kind': 'people_answered', 'subject': 'the-people', 'case_source': 'Exod 19:8'})            # write; the late law SKIPPED
    w.marker('Exod 24:1', 20, value='after')                                                               # the timer fires at 17
    w.submit({'kind': 'installation_commanded', 'subject': 'the-people', 'case_source': 'Exod 24:3'})     # a second timer: due 27
    w.submit({'kind': 'tablets_broken', 'subject': 'the-people', 'case_source': 'Exod 32:1'})             # cancels it
    w.marker('Exod 12:2', 5, value='this month')                                                           # RETROGRADE
    w.submit({'kind': 'installation_commanded', 'subject': 'the-people', 'case_source': 'Exod 12:3'})     # due 12 < now 20: RETRO-WRITE
    w.marker('Exod 40:17', 30, value='the tabernacle erected')                                             # forward: the stretch closes
    w.submit({'kind': 'custody_three_days', 'subject': 'the-blasphemer', 'case_source': 'Lev 24:12 — probe: the custody act'})  # the docket opens
    if upto == 'custody':
        return w
    w.marker('Lev 24:13', 33, value='the output')
    w.submit({'kind': 'statute_set', 'subject': 'moses', 'case_source': 'Lev 24:13 — probe: the output'})   # the docket closes at 33; rule_installed
    w.submit({'kind': 'people_answered', 'subject': 'the-people', 'case_source': 'Lev 24:14 — probe: after the output'})   # the late law FIRES
    w.submit({'kind': 'installation_commanded', 'subject': 'the-people', 'case_source': 'Lev 24:15 — probe: a pending timer'})   # due 40: PENDING
    w.marker('Gen 5:5', 40, value='all the days', proleptic=True)                                           # PROLEPTIC: the counter unmoved
    return w


def build(w, d):
    """sink the world, index the segment, create the views; returns the db path"""
    import world_journal as WJ
    path, n, coerced = WJ.sink(w, source=SOURCE, out_dir=d)
    db = os.path.join(d, 'probe.sqlite')
    WJ.index(db, [path])
    WJ.views(db)
    return db


def q(db, sql, *args):
    c = sqlite3.connect(db)
    try:
        return c.execute(sql, args).fetchall()
    finally:
        c.close()


@probe('V1 the index carries each row\'s source; the write row carries NO closer (a snapshot at write), the close row carries the day and the closer, and the ledger view joins them')
def v1():
    # THE LOOP step 1's amendment — THE CLOSE LINE (2026-09-12; THE_LOOP.md): RETYPED from "a closed entry carries closed_day beside closed_by"
    # (the write line held the ledger entry itself) to the new invariant — written to FAIL on the engine that logs the entry by reference
    w = probe_world()
    court = w.entities[REG['the-court']]
    owed = [e for e in court.ledger if e['effect'] == 'declaration_owed']
    with tempfile.TemporaryDirectory() as d:
        db = build(w, d)
        srcs = q(db, 'select distinct source from events')
        n = q(db, 'select count(*) from events where source = ?', SOURCE)[0][0]
        wrow = q(db, "select data from events where source = ? and kind = 'run.write' and json_extract(data, '$.effect') = 'declaration_owed'", SOURCE)
        crow = q(db, "select op, subj, json_extract(data, '$.note'), json_extract(data, '$.entry_seq'), unit from events where source = ? and kind = 'run.close'", SOURCE)
        vrow = q(db, "select open, day_closed, closed_by from run_ledger where source = ? and effect = 'declaration_owed'", SOURCE)
    wd = json.loads(wrow[0][0]) if wrow else {}
    ok = (srcs == [(SOURCE,)] and n == len(w.log) and len(owed) == 1 and owed[0].get('closed_day') == 33 and owed[0].get('open') is False
          and 'closed_by' not in wd and 'closed_day' not in wd and wd.get('open') is True
          and len(crow) == 1 and crow[0][0] == 33 and crow[0][1] == 'the_court' and str(crow[0][2]).startswith('Lev 24:13') and crow[0][3] == wd.get('seq') and crow[0][4] == 'law_probe'
          and vrow == [(0, 33, 'Lev 24:13 — probe: the output')])
    return ok, 'sources %s; rows with the source %d of %d log lines; the ledger entry closed_day %r open %r; the write row keys %s; the close rows %s; the view %s' % (
        srcs, n, len(w.log), owed[0].get('closed_day') if owed else None, owed[0].get('open') if owed else None, sorted(wd), crow, vrow)


@probe('V2 run_ledger\'s rows equal the write rows; the closed entry shows its day and its closer')
def v2():
    w = probe_world()
    writes = sum(1 for l in w.log if l[0] in ('WRITE', 'RETRO-WRITE'))
    with tempfile.TemporaryDirectory() as d:
        db = build(w, d)
        n = q(db, 'select count(*) from run_ledger where source = ?', SOURCE)[0][0]
        row = q(db, 'select entity, effect, ledger_op, day_written, open, day_closed, closed_by, written_by, counterparty from run_ledger where effect = ?', 'declaration_owed')
        retro = q(db, 'select count(*) from run_ledger where kind = ?', 'run.retro_write')[0][0]
    ok = n == writes and len(row) == 1 and row[0][0] == 'the_court' and row[0][2] == 'debit' and row[0][3] == 30 and row[0][4] == 0 \
        and row[0][5] == 33 and str(row[0][6]).startswith('Lev 24:13') and row[0][7] == 'law_probe' and row[0][8] == 'the-blasphemer' and retro == 1
    return ok, 'ledger rows %d = write lines %d; the docket row %s; retro-write rows %d' % (n, writes, row, retro)


@probe('V3 run_timers joins every fire and every cancel to exactly one set, and shows the pending one')
def v3():
    w = probe_world()
    sets = sum(1 for l in w.log if l[0] == 'TIMER-SET'); fires = sum(1 for l in w.log if l[0] == 'TIMER-FIRE')
    cancels = sum(1 for l in w.log if l[0] == 'TIMER-CANCEL')
    with tempfile.TemporaryDirectory() as d:
        db = build(w, d)
        rows = q(db, 'select day_set, due, outcome, day_fired, day_cancelled, cancelled_by from run_timers where source = ? order by seq', SOURCE)
    by = collections.Counter(r[2] for r in rows)
    ok = len(rows) == sets == 3 and by['fired'] == fires == 1 and by['cancelled'] == cancels == 1 and by['pending'] == 1 \
        and [r[1] for r in rows] == [17, 27, 40] and rows[0][3] == 17 and rows[1][4] == 20 and str(rows[1][5]).startswith('Exod 32:1') and rows[2][3] is None
    return ok, 'timer rows %d (sets %d): %s; fires %d, cancels %d' % (len(rows), sets, rows, fires, cancels)


@probe('V4 run_clock lists the markers in seq order with all three classes')
def v4():
    w = probe_world()
    markers = [l for l in w.log if l[0] == 'MARKER']
    with tempfile.TemporaryDirectory() as d:
        db = build(w, d)
        rows = q(db, 'select seq, day, verse, class, stated from run_clock where source = ? order by seq', SOURCE)
    classes = [r[3] for r in rows]
    ok = len(rows) == len(markers) == 7 and [r[0] for r in rows] == sorted(r[0] for r in rows) \
        and classes == ['forward', 'forward', 'forward', 'retrograde', 'forward', 'forward', 'proleptic'] \
        and rows[3][2] == 'Exod 12:2' and rows[3][4] == 5 and rows[6][2] == 'Gen 5:5' and rows[6][4] == 40 and rows[6][1] == 33
    return ok, 'clock rows %d (markers %d): %s' % (len(rows), len(markers), rows)


@probe('V5 run_docket: the declaration owed OPEN before the output, CLOSED at the output')
def v5():
    with tempfile.TemporaryDirectory() as d:
        before = q(build(probe_world(upto='custody'), d), 'select entity, person, day_written, open, day_closed from run_docket')
    with tempfile.TemporaryDirectory() as d:
        after = q(build(probe_world(), d), 'select entity, person, day_written, open, day_closed, closed_by from run_docket')
    ok = before == [('the_court', 'the-blasphemer', 30, 1, None)] and len(after) == 1 and after[0][:5] == ('the_court', 'the-blasphemer', 30, 0, 33) \
        and str(after[0][5]).startswith('Lev 24:13')
    return ok, 'before the output %s; at the end %s' % (before, after)


@probe('V6 the four questions: the ledger at a day, what stands open at a verse, who wrote this, what waits in custody')
def v6():
    import world_journal as WJ
    with tempfile.TemporaryDirectory() as d:
        db = build(probe_world(), d)
        led31 = WJ.ask(db, 'ledger', 'the_court', 31, source=SOURCE)
        led33 = WJ.ask(db, 'ledger', 'the_court', 33, source=SOURCE)
        open12 = WJ.ask(db, 'open', 'Lev 24:12', source=SOURCE)
        open14 = WJ.ask(db, 'open', 'Lev 24:14', source=SOURCE)
        who = WJ.ask(db, 'who', 'the_court', 'declaration_owed', source=SOURCE)
        cust_after = WJ.ask(db, 'custody', source=SOURCE)
    with tempfile.TemporaryDirectory() as d:
        db = build(probe_world(upto='custody'), d)
        cust_before = WJ.ask(db, 'custody', source=SOURCE)
    state = lambda rows: [(r['effect'], r['state']) for r in rows]
    ok = state(led31) == [('declaration_owed', 'open')] and state(led33) == [('declaration_owed', 'closed')] \
        and any(r['entity'] == 'the_court' and r['effect'] == 'declaration_owed' for r in open12) \
        and not any(r['effect'] == 'declaration_owed' for r in open14) \
        and len(who) == 1 and who[0]['written_by'] == 'law_probe' and who[0]['day'] == 30 and str(who[0]['verse']).startswith('Lev 24:12') \
        and len(cust_before) == 1 and cust_before[0]['person'] == 'the-blasphemer' and cust_after == []
    return ok, 'ledger at 31 %s, at 33 %s; open at Lev 24:12 %d rows (the docket among them: %s), at Lev 24:14 the docket %s; who %s; custody before %d, after %d' % (
        state(led31), state(led33), len(open12), any(r['effect'] == 'declaration_owed' for r in open12),
        'closed' if not any(r['effect'] == 'declaration_owed' for r in open14) else 'OPEN', [(r['written_by'], r['day']) for r in who], len(cust_before), len(cust_after))


if __name__ == '__main__':
    n_ok = sum(1 for _, ok, _ in results if ok)
    for name, ok, note in results:
        print('  %s  %s\n        %s' % ('PASS' if ok else 'FAIL', name, note))
    print('VIEW PROBES: %d/%d' % (n_ok, len(results)))
    assert results, 'ZERO-REPORT: no probe ran'
    sys.exit(0 if n_ok == len(results) else 1)
