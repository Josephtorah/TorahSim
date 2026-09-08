#!/usr/bin/env python3
"""sequence_probes.py — THE SEQUENTIAL RUN's fire-probes (2026-09-07; SEQUENTIAL_RUN.md section 7), written BEFORE the
engine extension (the W1/LR1 lesson: a gate that never fails proves nothing). Against the unchanged engine every probe
must FAIL; after the engine code every probe must PASS. Four probes:
  P1 an era SET BY A MARKER, its year counting new-year boundaries (the exodus era: Rosh Hashanah 3a:5)
  P2 year_in across an INTERCALATED boundary — one increment per Nisan whatever the month count
  P3 a LIFE era: 'the 600th year' under the completed and the ordinal readings; day_in finds the first 17th of the
     second ordinal month inside the life-year (Gen 7:11)
  P4 on a stitched stretch: the PROLEPTIC marker's log class; THE DATED DAY IS THE EVENT'S DAY inside a retrograde
     stretch; the registry map merging two tokens on one ledger; a checkpoint against an inherited bound
Not run by the sweep; run by hand at the sitting and after any engine edit. Run: python3 World/step9/sequence_probes.py
"""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import world_engine as WE

results = []


def probe(name):
    def deco(fn):
        try:
            ok, note = fn()
        except BaseException as e:                   # the old engine lacks the construct (or a registry refuses): a FAIL, named
            ok, note = False, '%s: %s' % (type(e).__name__, str(e)[:140])
        results.append((name, bool(ok), note))
        return fn
    return deco


def law_probe_dated(event, world):
    """a probe daemon in the day-grain runners' idiom: the due from the EVENT's day, falling back to the clock"""
    if event['kind'] == 'installation_commanded':
        day = event.get('day', world.clock.day)
        return [{'effect': 'released', 'subject': event['subject'], 'counterparty': None, 'amount': None, 'due': day + 7,
                 'source_law': 'probe', 'case_source': event['case_source']}]
    if event['kind'] == 'people_answered':
        return [{'effect': 'accepted', 'subject': event['subject'], 'counterparty': None, 'amount': None, 'due': None,
                 'source_law': 'probe', 'case_source': event['case_source']}]
    return []


@probe('P1 an era set by a marker: year_in counts the new-year boundaries (Rosh Hashanah 3a:5)')
def p1():
    w = WE.World(era='probe', epoch='count')
    nisan3 = w.clock.calendar.day_of(3, 1, 1)                          # the first of Nisan in count-year 3
    w.marker('Exod 12:2', nisan3, value='this month is for you the head of months', era='exodus', new_year_month=1)
    a = (w.clock.year_in('exodus'), w.clock.date_in('exodus'))
    w.advance(w.clock.day_in('exodus', 2, 1, 1))                       # Exod 40:17: the first month of the second year
    b = (w.clock.year_in('exodus'), w.clock.date_in('exodus'), w.clock.calendar.date(w.clock.day))
    w.advance(w.clock.day_in('exodus', 2, 2, 20))                      # Num 10:11: the second month of the second year
    c = (w.clock.year_in('exodus'), w.clock.date_in('exodus'), w.clock.year)
    return (a == (1, (1, 1, 1)) and b[:2] == (2, (2, 1, 1)) and b[2] == (4, 1, 1) and c[:2] == (2, (2, 2, 20)) and c[2] == 4,
            'at the marker %r; at 40:17 %r; at Num 10:11 %r' % (a, b, c))


@probe('P2 year_in across an intercalated boundary: one increment per Nisan')
def p2():
    w = WE.World(era='probe', epoch='count')
    w.marker('Exod 12:2', w.clock.calendar.day_of(2, 1, 1), era='exodus', new_year_month=1)
    years, lens = [], []
    for y in range(2, 40):
        d = w.clock.calendar.day_of(y, 1, 1)
        w.advance(d)
        years.append(w.clock.year_in('exodus'))
        lens.append(w.clock.calendar.day_of(y + 1, 1, 1) - d)
    steps = [b - a for a, b in zip(years, years[1:])]
    return (all(s == 1 for s in steps) and years[0] == 1 and any(l > 380 for l in lens) and any(l < 360 for l in lens),
            'years %s...; year lengths seen %s' % (years[:6], sorted(set(lens))))


@probe('P3 a life era: the 600th year under two readings; the flood date inside the life-year (Gen 7:11)')
def p3():
    w = WE.World(era='probe', epoch='count')
    birth = w.clock.calendar.day_of(5, 7, 6)                           # 6 Tishrei of year 5
    w.marker('Gen 5:28', birth, value='Lamech 182: Noah born', era='life:noach', new_year_month=None)
    d_completed = w.clock.day_in('life:noach', 600, 2, 17)             # the running reading: age 600
    d_ordinal = w.clock.day_in('life:noach', 600, 2, 17, reading='ordinal')
    d_601 = w.clock.day_in('life:noach', 601, 1, 1)                    # Gen 8:13: the 601st year, the first month, the first — the NEXT New Year
    w.advance(d_completed)
    a = (w.clock.calendar.date(d_completed), w.clock.calendar.date(d_ordinal), w.clock.year_in('life:noach'), w.clock.date_in('life:noach'), w.clock.calendar.date(d_601))
    return (a[0] == (605, 8, 17) and a[1] == (604, 8, 17) and a[2] == 600 and a[3][0] == 600 and a[4] == (606, 7, 1),
            'completed %r; ordinal %r; year_in %r; date_in %r; the 601st year\'s first day %r' % a)


@probe('P4 the proleptic marker; the dated day is the event\'s day; the registry map; the inherited bound')
def p4():
    w = WE.World(era='probe', epoch='count', registry={'the-people': 'israel_people', 'israel': 'israel_people'})
    w.laws = [law_probe_dated]
    w.advance(100)
    w.marker('Lev 8:2', 93, value='the twenty-third of Adar')          # retrograde: earlier than the counter
    ev = {'kind': 'installation_commanded', 'subject': 'aaron-and-sons', 'components': [], 'case_source': 'probe'}
    w.submit(ev)
    dated_ok = ev.get('day') == 93 and ev.get('dated') == 93
    writes = [l for l in w.log if l[0] in ('WRITE', 'RETRO-WRITE') and l[2]['effect'] == 'released']
    immediate = len(writes) == 1 and not [t for t in w.timers if t[1]['effect'] == 'released']   # due 100 = now: written at once
    w.marker('Gen 5:5', 500, value='Adam 930', proleptic=True)
    m = [l for l in w.log if l[0] == 'MARKER'][-1]
    prol_ok = m[2].get('proleptic') is True and m[2].get('stated') == 500 and w.clock.day == 100
    w.marker('Gen 21:5', 200)
    e1 = {'kind': 'people_answered', 'subject': 'the-people', 'people': 'the-people', 'book_read': False, 'case_source': 'probe'}
    e2 = {'kind': 'people_answered', 'subject': 'israel', 'people': 'israel', 'book_read': True, 'case_source': 'probe'}
    w.submit(e1); w.submit(e2)
    merged = w.entity('israel') is w.entity('the-people') and len(w.entity('the-people').ledger) == 2 and 'israel_people' in w.entities and 'israel' not in w.entities
    w.marker('Gen 25:20', 300)
    bound_ok = e1.get('bound') == [200, 300] and w.checkpoint('probe: the purchase within its bound', None, 250, bound=e1['bound'])
    return (dated_ok and immediate and prol_ok and merged and bound_ok,
            'dated %s immediate %s proleptic %s merged %s bound %s' % (dated_ok, immediate, prol_ok, merged, bound_ok))


if __name__ == '__main__':
    n_ok = sum(1 for _, ok, _ in results if ok)
    for name, ok, note in results:
        print('%s  %s\n      %s' % ('PASS' if ok else 'FAIL', name, note))
    print('\nsequence_probes: %d/%d probes pass' % (n_ok, len(results)))
    sys.exit(0 if n_ok == len(results) else 1)
