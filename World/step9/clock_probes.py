#!/usr/bin/env python3
"""clock_probes.py — THE CLOCK SITTING's fire-probes (2026-09-07), written BEFORE the engine code (the W1/LR1
lesson: a gate that never fails proves nothing). Each probe asserts a construct of CLOCK.md; run against the
unchanged engine every probe must FAIL; after the engine code every probe must PASS. Twelve probes:
  1. the day counter and the derived year through an epoch (B)
  2. year is None with no epoch declared (round two, 6)
  3. a calendar-key period re-arms and logs the TIMER-SET chain (G)
  4. an integer period re-arms in days (G)
  5. a recurrence ends by cancel_timers on a text event, never by count (G)
  6. the bound stamped at submit, closed by the next marker, inherited by the timer and its fire (C)
  7. the derived year at an intercalated boundary — a thirteen-month year under the modeled season ground (D, E)
  8. the retrograde marker — logged, counter unmoved, `dated` carried, a past due written at submission (C)
  9. the jubilee fork's three conditions on the proclamation act (F as amended)
 10. after(6, 'year') lands on the same date six years on (B)
 11. the flood's 150 days against the received month — OPEN-4, expected to DIVERGE and say so (H)
 12. the close pairing — the tamid offered closes yesterday's open debit (G)
Then THE PARAMETERS CENSUS: calendar_parameters.yaml's rows by channel, the UNEXERCISED rows named (the
zero-report law). Not run by the sweep; run by hand at the sitting and after any engine edit.
Run: python3 World/step9/clock_probes.py
"""
import contextlib, io, os, sys, traceback
import yaml
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import world_engine as WE

results = []


def probe(name):
    def deco(fn):
        try:
            ok, note = fn()
        except BaseException as e:                   # the old engine lacks the construct (or a registry refuses): a FAIL, named
            ok, note = False, '%s: %s' % (type(e).__name__, str(e)[:120])
        results.append((name, bool(ok), note))
        return fn
    return deco


def quiet_import(mod):
    with contextlib.redirect_stdout(io.StringIO()):
        return __import__(mod)


@probe('1 the day counter; the year derived through the count epoch')
def p1():
    w = WE.World(era='probe', epoch='count')
    a = (w.clock.day, w.clock.year, w.clock.date)
    w.advance(w.clock.at_year(3))
    b = (w.clock.year, w.clock.date, w.clock.day > 700)
    return a == (0, 1, (1, 7, 1)) and b == (3, (3, 7, 1), True), 'start %r; at year 3: %r' % (a, b)


@probe('2 no epoch: the year is None, the day counts')
def p2():
    w = WE.World(era='probe')
    w.advance(5)
    return w.clock.day == 5 and w.clock.year is None, 'day %r year %r' % (w.clock.day, w.clock.year)


@probe('3 a calendar-key period re-arms; the chain logged with rearmed_from')
def p3():
    w = WE.World(era='probe', epoch='count')
    w._write({'effect': 'sabbath_of_the_land', 'subject': 'the-land', 'counterparty': None, 'amount': None,
              'due': w.clock.at_year(7), 'period': 'sabbatical', 'source_law': 'probe', 'case_source': 'probe'})
    w.advance(w.clock.at_year(15))
    fires = [l for l in w.log if l[0] == 'TIMER-FIRE']
    rearms = [l for l in w.log if l[0] == 'TIMER-SET' and l[2].get('rearmed_from') is not None]
    years = [w.clock.calendar.year(l[1]) for l in fires]
    pending = [w.clock.calendar.year(t[0]) for t in w.timers]
    return (years == [7, 14] and len(rearms) == 2 and pending == [21],
            'fired in years %r; re-arms %d; pending at %r' % (years, len(rearms), pending))


@probe('4 an integer period re-arms in days')
def p4():
    w = WE.World(era='probe')
    w._write({'effect': 'tamid_owed', 'subject': 'the-altar', 'counterparty': None, 'amount': None,
              'due': 1, 'period': 1, 'source_law': 'probe', 'case_source': 'probe'})
    w.advance(5)
    fires = [l[1] for l in w.log if l[0] == 'TIMER-FIRE']
    return fires == [1, 2, 3, 4, 5] and len(w.timers) == 1, 'fired on days %r; pending %d' % (fires, len(w.timers))


@probe('5 a recurrence ends on cancel_timers (a text event), never on a count')
def p5():
    w = WE.World(era='probe')
    w._write({'effect': 'tamid_owed', 'subject': 'the-altar', 'counterparty': None, 'amount': None,
              'due': 1, 'period': 1, 'source_law': 'probe', 'case_source': 'probe'})
    w.advance(3)
    cut = w.cancel_timers('the-altar', 'tamid_owed', 'the tamid taken away [Mishnah Taanit 4:6; Dan 8:11] — probe')
    w.advance(10)
    fires = [l[1] for l in w.log if l[0] == 'TIMER-FIRE']
    return cut == 1 and fires == [1, 2, 3] and not w.timers, 'cut %d; fired %r; pending %d' % (cut, fires, len(w.timers))


def law_probe_timer(event, world):
    if event['kind'] == 'tamid_offered':
        return [{'effect': 'tamid_owed', 'subject': 'the-altar', 'counterparty': None, 'amount': None,
                 'due': world.clock.day + 5, 'source_law': 'probe', 'case_source': event['case_source']}]
    return []


@probe('6 the bound: stamped [last marker, open] at submit, closed by the next marker, on the timer and its fire')
def p6():
    w = WE.World(era='probe'); w.laws = [law_probe_timer]
    w.marker('Exod 40:17', 10)
    ev = {'kind': 'tamid_offered', 'subject': 'the-lamb', 'case_source': 'probe'}
    w.submit(ev)
    open_bound = list(ev['bound'])
    w.marker('Num 1:1', 40)                                   # walks to 40: the timer fires at 15 on the way
    fire = [l for l in w.log if l[0] == 'TIMER-FIRE'][0][2]
    setl = [l for l in w.log if l[0] == 'TIMER-SET'][0][2]
    return (open_bound == [10, None] and ev['bound'] == [10, 40] and setl['bound'] == [10, 40] and fire['bound'] == [10, 40],
            'at submit %r; after the marker %r; timer %r; fire %r' % (open_bound, ev['bound'], setl.get('bound'), fire.get('bound')))


@probe('7 an intercalated year exists under the modeled season ground; the year still turns at the new-year month')
def p7():
    w = WE.World(era='probe', epoch='count')
    cal = w.clock.calendar
    leap = [y for y in range(1, 50) if cal.day_of(y + 1) - cal.day_of(y) == 384]
    plain = [y for y in range(1, 50) if cal.day_of(y + 1) - cal.day_of(y) == 354]
    y = leap[0] if leap else None
    ok = bool(leap) and len(leap) + len(plain) == 49 and cal.year(cal.day_of(y + 1)) == y + 1 and cal.year(cal.day_of(y + 1) - 1) == y \
        and cal.date(cal.day_of(y + 1) - 1)[1] == 6
    return ok, 'thirteen-month years in the first forty-nine: %r; twelve-month: %d' % (leap, len(plain))


def law_probe_dated(event, world):
    if event['kind'] == 'tamid_offered':
        base = event.get('dated', world.clock.day)
        return [{'effect': 'tamid_owed', 'subject': 'the-altar', 'counterparty': None, 'amount': None,
                 'due': base + 10, 'source_law': 'probe', 'case_source': event['case_source']}]
    return []


@probe('8 the retrograde marker: logged, the counter unmoved, dated carried, a past due written at submission')
def p8():
    w = WE.World(era='probe'); w.laws = [law_probe_dated]
    w.advance(50)
    w.marker('Num 9:1', 30)
    mk = [l for l in w.log if l[0] == 'MARKER'][-1]
    ev = {'kind': 'tamid_offered', 'subject': 'the-lamb', 'case_source': 'probe'}
    w.submit(ev)
    retro = [l for l in w.log if l[0] == 'RETRO-WRITE']
    entry = w.entity('the-altar').ledger[-1]
    return (mk[2].get('retrograde') is True and mk[2].get('stated') == 30 and w.clock.day == 50 and ev.get('dated') == 30
            and 'bound' not in ev and len(retro) == 1 and entry['day'] == 50 and entry.get('dated') == 30 and not w.timers,
            'marker %r; day %d; dated %r; retro-writes %d; entry day %r dated %r' % (mk[2], w.clock.day, ev.get('dated'), len(retro), entry.get('day'), entry.get('dated')))


@probe('9 the jubilee fork: the horn, the servants, all the inhabitants — on the proclamation act')
def p9():
    Y = quiet_import('cold_run_yovel'); T = quiet_import('cold_run_tochacha')
    def world(exiled):
        w = WE.World(era='probe', epoch='count'); w.laws = [Y.law_yovel, T.law_tochacha, WE.law_slave_term]
        w.submit({'kind': 'entered_the_land', 'subject': 'israel', 'people': 'israel', 'land': 'the-land', 'case_source': 'Lev 25:2 — probe'})
        w.advance(w.clock.at_year(40))
        w.submit({'kind': 'field_sold', 'subject': 'field-1', 'seller': 'the-seller', 'buyer': 'the-buyer', 'field': 'field-1', 'price': 100,
                  'years_to_jubilee': 10, 'case_source': 'Lev 25:28 — probe'})
        if exiled:
            w.submit({'kind': 'people_exiled', 'subject': 'israel', 'people': 'israel', 'land': 'the-land', 'case_source': 'Arakhin 32b:16 — probe'})
        w.advance(w.clock.calendar.day_of(50, 7, 10))
        return w
    def vals(w):
        return [e['value'] for e in w.entity('the-land').ledger if e['effect'] == 'jubilee_release' and e['day'] == w.clock.day]
    wa = world(False); wa.submit({'kind': 'jubilee_proclaimed', 'subject': 'the-land', 'proclaimer': 'the-court', 'land': 'the-land', 'horn_sounded': False, 'servants_sent_free': True, 'case_source': 'Sifra Behar Chapter 2 4 — probe'})
    wb = world(False); wb.submit({'kind': 'jubilee_proclaimed', 'subject': 'the-land', 'proclaimer': 'the-court', 'land': 'the-land', 'horn_sounded': True, 'servants_sent_free': False, 'case_source': 'Sifra Behar Chapter 2 4 — probe'})
    wc = world(True); wc.submit({'kind': 'jubilee_proclaimed', 'subject': 'the-land', 'proclaimer': 'the-court', 'land': 'the-land', 'horn_sounded': True, 'servants_sent_free': True, 'case_source': 'Arakhin 32b:16 — probe'})
    wd = world(False); wd.submit({'kind': 'jubilee_proclaimed', 'subject': 'the-land', 'proclaimer': 'the-court', 'land': 'the-land', 'horn_sounded': True, 'servants_sent_free': True, 'case_source': 'Lev 25:9-10 — probe'})
    va, vb, vc, vd = vals(wa), vals(wb), vals(wc), vals(wd)
    ret_d = [e for e in wd.entity('field-1').ledger if e['effect'] == 'returns_to_holding']
    ret_c = [e for e in wc.entity('field-1').ledger if e['effect'] == 'returns_to_holding']
    ent = [e for e in wd.entity('field-1').ledger if e['effect'] == 'goes_out_in_the_jubilee']
    s = lambda v: ' | '.join(map(str, v))
    ok = (len(va) == 2 and any('Rabbi Yehuda' in str(x) and 'jubilee' in str(x) and 'no jubilee' not in str(x) for x in va) and any('Rabbi Yose' in str(x) and 'no jubilee' in str(x) for x in va)
          and len(vb) == 2 and any('Rabbi Yose' in str(x) and 'no jubilee' not in str(x) for x in vb) and any('Rabbi Yehuda' in str(x) and 'no jubilee' in str(x) for x in vb)
          and len(vc) == 1 and 'no jubilee' in str(vc[0]) and 'inhabitants' in str(vc[0]) and not ret_c
          and len(vd) == 1 and 'no jubilee' not in str(vd[0]) and len(ret_d) == 1 and len(ent) == 1)
    return ok, 'no horn: %s || no servants: %s || exiled: %s (returns %d) || all held: %s (returns %d, entitlement %d)' % (s(va), s(vb), s(vc), len(ret_c), s(vd), len(ret_d), len(ent))


@probe('10 after(6, year) lands on the same date six years on')
def p10():
    w = WE.World(era='probe', epoch='count')
    w.advance(w.clock.at_year(1) + 40)
    d0 = w.clock.date; due = w.clock.after(6, 'year'); d1 = w.clock.calendar.date(due)
    return d1 == (d0[0] + 6, d0[1], d0[2]), '%r -> %r' % (d0, d1)


@probe('11 OPEN-4: the flood\'s 150 days (Gen 7:11 -> 8:4) against the received month — DIVERGE, said so')
def p11():
    w = WE.World(era='probe', epoch='count'); cal = w.clock.calendar
    computed = cal.day_of(3, 7, 17) - cal.day_of(2, 2, 17)          # the second month's 17th to the seventh month's 17th
    out = io.StringIO()
    with contextlib.redirect_stdout(out):
        ok = w.checkpoint('OPEN-4 the flood: 150 days by the text', 150, computed)
    return (not ok) and computed in (147, 148) and 'DIVERGE' in out.getvalue(), 'computed %d; checkpoint printed %r' % (computed, out.getvalue().strip().splitlines()[0])


@probe('12 the close pairing: the tamid offered closes yesterday\'s open debit')
def p12():
    E = quiet_import('cold_run_erection')
    w = WE.World(era='probe'); w.laws = [E.law_erection]
    w.advance(1)
    w.submit({'kind': 'tamid_offered', 'subject': 'the-lamb', 'case_source': 'Exod 29:38-42 — probe day 1'})
    w.advance(2)
    before = len([e for e in w.entity('the-altar').ledger if e['effect'] == 'tamid_owed' and e.get('open')])
    w.submit({'kind': 'tamid_offered', 'subject': 'the-lamb', 'case_source': 'Exod 29:38-42 — probe day 2'})
    after = [e for e in w.entity('the-altar').ledger if e['effect'] == 'tamid_owed']
    open_after = len([e for e in after if e.get('open')])
    return before == 1 and open_after == 0 and after[0].get('closed_by'), 'open before the second offering %d; open after %d; closed_by %r' % (before, open_after, after[0].get('closed_by') if after else None)


print('CLOCK PROBES (CLOCK.md sections 1-6; each must FAIL on the old engine and PASS on the new):')
for name, ok, note in results:
    print('  %s  %s\n        %s' % ('PASS' if ok else 'FAIL', name, note))
n = sum(ok for _, ok, _ in results)
print('clock probes: %d/%d pass' % (n, len(results)))

# ---- THE PARAMETERS CENSUS (coverage first; the unexercised rows named) --------------------------------
P = yaml.safe_load(open(os.path.join(HERE, 'calendar_parameters.yaml'), encoding='utf-8'))
by = {}
for k, r in P['parameters'].items():
    by.setdefault(r['channel'], []).append(k)
print('PARAMETERS CENSUS: %d rows — %s; eras %d' % (len(P['parameters']), ', '.join('%s %d' % (c, len(v)) for c, v in sorted(by.items())), len(P['eras'])))
unex = [k for k, r in P['parameters'].items() if not r.get('exercised_by')] + ['era:' + k for k, r in P['eras'].items() if not r.get('exercised_by')]
opens = [(k, r['open'].split(' — ')[0]) for k, r in P['parameters'].items() if r.get('open')]
print('  UNEXERCISED (visible, never counted as run): %s' % ', '.join(unex))
print('  OPEN: %s' % '; '.join('%s [%s]' % (k, o) for k, o in opens))
sys.exit(0 if n == len(results) else 1)
