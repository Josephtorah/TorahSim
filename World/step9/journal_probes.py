#!/usr/bin/env python3
"""journal_probes.py — THE LOOP's step 1 fire-probes (2026-09-09; THE_LOOP.md "Step 1 THE SINK — the design"), written BEFORE
the sink module and the engine's one additive line (the writer stamp). Against the unchanged engine every probe must FAIL; after
the code every probe must PASS. All six run in-process on a SMALL probe world (a probe daemon, a registry map, a marker, a timer
that fires, a cancel, a retrograde stretch) so the file runs in a second. Six probes:
  J1 a run writes a SEGMENT whose line count equals the world's log length (one journal event per log line; the header apart)
  J2 the chain VERIFIES, and a line mutated in place is DETECTED (worldledger's own verify)
  J3 every kind the sink writes is in the REGISTER (World/journal/registers/event_kinds.yaml) — the register's own rule
  J4 the subject is the REGISTRY id — a scene token mapped by the registry writes its registry name, never the token
  J5 two sinks of one world are BYTE-IDENTICAL (no timestamps, canonical JSON, the log's order)
  J6 (step 2's first gate) the INDEX rebuilt from the segment counts each kind exactly as the log does, and answers
     "who wrote this" (prov.unit = the daemon that wrote the entry) and "what is written on this subject"
Not run by the sweep; run by hand at the sitting and after any engine edit. Run: python3 World/step9/journal_probes.py
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
            ok, note = False, '%s: %s' % (type(e).__name__, str(e)[:160])
        results.append((name, bool(ok), note))
        return fn
    return deco


def law_probe(event, world):
    """the probe daemon: a seven-day timer on an installation, an immediate status on an answer, a cancel on the breaking
    (registered kinds only — the tape's registry refuses a probe-only type, so the breaking stands in for a refusal)"""
    if event['kind'] == 'installation_commanded':
        day = event.get('day', world.clock.day)
        return [{'effect': 'released', 'subject': event['subject'], 'counterparty': None, 'amount': None, 'due': day + 7,
                 'source_law': 'probe', 'case_source': event['case_source']}]
    if event['kind'] == 'people_answered':
        return [{'effect': 'accepted', 'subject': event['subject'], 'counterparty': None, 'amount': None, 'due': None,
                 'source_law': 'probe', 'case_source': event['case_source']}]
    if event['kind'] == 'tablets_broken':
        world.cancel_timers(event['subject'], 'released', event['case_source'])
        return [{'effect': 'accepted', 'subject': event['subject'], 'counterparty': None, 'amount': None, 'due': None,
                 'value': False, 'case_source': event['case_source']}]     # no source_law: the writer must come from the engine
    return []


def probe_world():
    """a small world exercising the seven engine log classes: EVENT, WRITE, TIMER-SET, TIMER-FIRE, TIMER-CANCEL, MARKER, RETRO-WRITE (the
    eighth, SKIP, is installation_probes.py's; the ninth, ROW, population_probes.py's — THE NUMBERS WALK 8b, 2026-09-11)"""
    w = WE.World(era='probe', epoch='count', registry={'the-people': 'israel_people'})
    w.laws = [law_probe]
    w.marker('Exod 19:1', 10, value='the third month')
    w.submit({'kind': 'installation_commanded', 'subject': 'the-people', 'case_source': 'Exod 19:5'})     # timer set: day 17
    w.marker('Exod 19:16', 12, value='the third day')
    w.submit({'kind': 'people_answered', 'subject': 'the-people', 'case_source': 'Exod 19:8'})            # write now
    w.marker('Exod 24:1', 20, value='after')                                                               # the timer fires at 17
    w.submit({'kind': 'installation_commanded', 'subject': 'the-people', 'case_source': 'Exod 24:3'})     # a second timer: 27
    w.submit({'kind': 'tablets_broken', 'subject': 'the-people', 'case_source': 'Exod 32:1'})             # cancels it
    w.marker('Exod 12:2', 5, value='this month')                                                           # RETROGRADE: earlier than the counter
    w.submit({'kind': 'installation_commanded', 'subject': 'the-people', 'case_source': 'Exod 12:3'})     # due 12 < now 20: RETRO-WRITE
    return w


def sink_to(w, d, name='probe'):
    import world_journal as WJ
    return WJ.sink(w, source='journal_probes/%s' % name, out_dir=d)


@probe('J1 a run writes a segment with one journal event per log line')
def j1():
    w = probe_world()
    classes = collections.Counter(l[0] for l in w.log)
    with tempfile.TemporaryDirectory() as d:
        path, n, coerced = sink_to(w, d)
        lines = open(path, encoding='utf-8').read().splitlines()
    ok = os.path.basename(path).startswith('L3_') and n == len(w.log) and len(lines) == len(w.log) + 1 and coerced == 0
    return ok, 'log %d lines in classes %s; segment %d events + header, coerced %d' % (len(w.log), dict(classes), n, coerced)


@probe('J2 the chain verifies, and a line mutated in place is detected')
def j2():
    import world_journal as WJ
    w = probe_world()
    with tempfile.TemporaryDirectory() as d:
        path, n, _ = sink_to(w, d)
        clean = WJ.verify(path)
        lines = open(path, encoding='utf-8').read().split('\n')
        ev = json.loads(lines[3]); ev['data']['case_source'] = 'Exod 99:99'          # mutate one line in place, chain field kept
        lines[3] = json.dumps(ev, sort_keys=True, ensure_ascii=False, separators=(',', ':'))
        open(path, 'w', encoding='utf-8').write('\n'.join(lines))
        tampered = WJ.verify(path)
    return clean is True and tampered is False, 'clean verify %r; after an in-place mutation of line 3 verify %r' % (clean, tampered)


@probe('J3 every kind the sink writes is in the register')
def j3():
    import yaml, world_journal as WJ
    reg = yaml.safe_load(open(os.path.join(HERE, '..', 'journal', 'registers', 'event_kinds.yaml'), encoding='utf-8'))
    ids = {k['id'] for k in reg['kinds']}
    w = probe_world()
    with tempfile.TemporaryDirectory() as d:
        path, n, _ = sink_to(w, d)
        kinds = collections.Counter(json.loads(l)['kind'] for l in open(path, encoding='utf-8').read().splitlines()[1:])
    missing = sorted(k for k in kinds if k not in ids)
    # THE LOOP step 3 (2026-09-09): the sink's eighth class, run.skip, is exercised by installation_probes.py I1 (a from_event world sunk
    # and indexed); this probe world has no installation, so the seven engine classes it exercises are KINDS less run.skip — and every
    # class the sink can write, the eighth included, must be in the register
    seven = set(WJ.KINDS.values()) - {'run.skip', 'run.row', 'run.close'}   # THE NUMBERS WALK 8b (2026-09-11): the ninth class run.row (a population-table row) is exercised by population_probes.py P6 — this probe world writes no row; THE LOOP step 1's amendment (2026-09-12): the tenth class run.close (a ledger entry's close as its own line) is exercised by J7 below — this probe world closes nothing
    unregistered_kinds = sorted(k for k in WJ.KINDS.values() if k not in ids)
    return not missing and not unregistered_kinds and len(kinds) == 7 and set(kinds) == seven, 'kinds written %s; unregistered %s; sink classes %d (all registered: %s)' % (
        dict(kinds), missing or 'none', len(WJ.KINDS), not unregistered_kinds)


@probe('J4 the subject is the registry id, never the scene token')
def j4():
    w = probe_world()
    with tempfile.TemporaryDirectory() as d:
        path, n, _ = sink_to(w, d)
        evs = [json.loads(l) for l in open(path, encoding='utf-8').read().splitlines()[1:]]
    subs = collections.Counter(e['subj'] for e in evs)
    return 'the-people' not in subs and subs.get('israel_people', 0) >= 8 and subs.get('clock', 0) == 4, 'subjects %s' % dict(subs)


@probe('J5 two sinks of one world are byte-identical')
def j5():
    w = probe_world()
    with tempfile.TemporaryDirectory() as d1, tempfile.TemporaryDirectory() as d2:
        p1, n1, _ = sink_to(w, d1); p2, n2, _ = sink_to(w, d2)
        b1 = open(p1, 'rb').read(); b2 = open(p2, 'rb').read()
    return b1 == b2 and n1 == n2 and b'"ts"' not in b1 and b'timestamp' not in b1, '%d bytes each, identical %r, no timestamp field' % (len(b1), b1 == b2)


@probe('J6 the index counts each kind as the log does and answers who wrote this / what is on this subject')
def j6():
    import world_journal as WJ
    w = probe_world()
    log_counts = collections.Counter(WJ.KINDS[l[0]] for l in w.log)
    with tempfile.TemporaryDirectory() as d:
        path, n, _ = sink_to(w, d)
        db = os.path.join(d, 'probe.sqlite')
        WJ.index(db, [path])
        idx = WJ.counts(db)
        c = sqlite3.connect(db)
        writers = dict(c.execute("SELECT unit, COUNT(*) FROM events WHERE kind IN ('run.write','run.retro_write') GROUP BY unit").fetchall())
        on_subject = c.execute("SELECT COUNT(*) FROM events WHERE subj='israel_people' AND kind LIKE 'run.%'").fetchone()[0]
        c.close()
    ok = idx == dict(log_counts) and writers.get('law_probe', 0) == 4 and None not in writers and on_subject >= 8
    return ok, 'index %s vs log %s; writers %s; lines on israel_people %d' % (idx, dict(log_counts), writers, on_subject)



# ---- THE LOOP step 1's amendment — THE CLOSE LINE (2026-09-12; THE_LOOP.md "Step 1's amendment — THE CLOSE LINE"; the owner: "I accept
# ---- your recommendation"): the tenth class, written to FAIL on the engine that logs the ledger entry itself ----
def law_probe_close(event, world):
    """a debt opened at the custody act and paid at the output (view_probes' pair of kinds; registered effects only)"""
    if event['kind'] == 'custody_three_days':
        return [{'effect': 'declaration_owed', 'subject': 'the-court', 'counterparty': event['subject'], 'amount': None, 'due': None,
                 'source_law': 'probe', 'case_source': event['case_source']}]
    if event['kind'] == 'statute_set':
        world.close('the-court', 'declaration_owed', event['case_source'])
        return [{'effect': 'rule_installed', 'subject': 'the-tabernacle', 'counterparty': None, 'amount': None, 'due': None,
                 'value': 'law_probe_close', 'source_law': 'probe', 'case_source': event['case_source']}]
    return []


@probe('J7 a close is its own line: the write line a snapshot with no closer, the close line naming the entry, the earlier sink a byte-identical prefix of the later, the index counting run.close and the ledger view joining the two')
def j7():
    import world_journal as WJ
    w = WE.World(era='probe', epoch='count', registry={'the-court': 'the_court'})
    w.laws = [law_probe_close]
    w.marker('Lev 24:12', 30, value='the custody')
    w.submit({'kind': 'custody_three_days', 'subject': 'the-blasphemer', 'case_source': 'Lev 24:12 — probe: the custody act'})   # the debt opens at 30
    w.marker('Lev 24:13', 33, value='the output')                                                                                # the forward marker CLOSES the event's bound — the first sink stands at a marker, as the cursor's bound rule (sitting 1b) requires; a sink inside an open bound differs on the shared bound list by design (THE_LOOP.md, the amendment's item 2 — the first form of this probe fell on exactly that, 2026-09-12)
    with tempfile.TemporaryDirectory() as d:
        p1, n1, _ = WJ.sink(w, source='journal_probes/close', out_dir=d)
        before = open(p1, encoding='utf-8').read().split('\n')
        w.submit({'kind': 'statute_set', 'subject': 'moses', 'case_source': 'Lev 24:13 — probe: the output'})                    # the debt is paid at 33
        p2, n2, _ = WJ.sink(w, source='journal_probes/close', out_dir=d)
        after = open(p2, encoding='utf-8').read().split('\n')
        evs = [json.loads(l) for l in after[1:] if l.strip()]
        db = os.path.join(d, 'probe.sqlite')
        WJ.index(db, [p2]); WJ.views(db)
        idx = WJ.counts(db)
        c = sqlite3.connect(db)
        led = c.execute("select open, day_closed, closed_by from run_ledger where effect = 'declaration_owed'").fetchall()
        c.close()
    writes = [e for e in evs if e['kind'] == 'run.write' and e['data'].get('effect') == 'declaration_owed']
    closes = [e for e in evs if e['kind'] == 'run.close']
    wd = writes[0]['data'] if writes else {}
    entry = w.entities['the_court'].ledger[0]
    prefix = after[1:n1 + 1] == before[1:n1 + 1]
    ok = (len(writes) == 1 and 'closed_by' not in wd and 'closed_day' not in wd and wd.get('open') is True and 'seq' in wd
          and len(closes) == 1 and closes[0]['data'].get('entry_seq') == wd.get('seq') and closes[0]['op'] == 33 and closes[0]['subj'] == 'the_court'
          and str(closes[0]['data'].get('note', '')).startswith('Lev 24:13') and closes[0]['prov'].get('unit') == 'law_probe_close'
          and prefix and n2 == n1 + 3 and idx.get('run.close') == 1
          and led == [(0, 33, 'Lev 24:13 — probe: the output')]
          and entry.get('open') is False and entry.get('closed_day') == 33)
    return ok, 'write line data keys %s; close lines %d %s; prefix identical %r (%d then %d lines); index run.close %r; the view %s; the ledger entry open %r closed_day %r' % (
        sorted(wd), len(closes), [(e['op'], e['subj'], e['data'].get('entry_seq'), e['prov'].get('unit')) for e in closes], prefix, n1, n2, idx.get('run.close'), led, entry.get('open'), entry.get('closed_day'))

if __name__ == '__main__':
    ok = sum(1 for _, o, _ in results if o)
    for name, o, note in results:
        print('%s %s\n     %s' % ('PASS' if o else 'FAIL', name, note))
    print('\n%d/%d probes' % (ok, len(results)))
    sys.exit(0 if ok == len(results) else 1)
