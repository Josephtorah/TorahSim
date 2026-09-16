#!/usr/bin/env python3
"""readback_probes.py — THE READBACK'S FIRST FORM (THE LOOP step 6; THE DEUTERONOMY WALK sitting 1b, 2026-09-15; World/step9/DEUTERONOMY_WALK.md
"Sitting 1b" (R1)-(R6)): the probes written to FAIL before cold_run_opening_speech.py exists, PASS after the tape carries Deuteronomy 1-3.
  Q1 the runner exists and its DATA row the_readback carries rows graded by the six grades (VERBATIM / TURNED / SHORTENED / EXPANDED / SUPPLIED / DISAGREES)
  Q2 every row's tape entry is FOUND on the running world by kind and first verse (rows n = found n)
  Q3 a SUPPLIED debit is CLOSED BY A PRIOR RUN — the closer's verse stands EARLIER on the tape than the line that opened the debit
  Q4 the supplied lines are DATED by a retrograde stretch — the event carries `dated`, its day the marker's stated day, not the counter's
  Q5 the two DISAGREES rows are OPEN — no ledger entry written for either (2:29's Edom, 1:37's ground of the bar)
  Q6 the register gate's seats on the new tape — Deut 1:3 ACT, 1:19 CHAPTER, 1:41 CHAPTER (the gate's class for a receipt whose chapter holds a closed entry — read at the first run; the design said NONE), Deut 4:45 DAEMONS, Num 27:22 CLOSE
Run: python3 World/step9/readback_probes.py   (the running world replays the tape: ~3 minutes)
"""
import os, sys, io, re, contextlib, collections
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
R = []
def probe(name, f):
    try:
        ok, why = f()
    except BaseException as e:            # a probe harness catches BaseException — a missing runner is a FAIL named, never a crash
        ok, why = False, '%s: %s' % (type(e).__name__, str(e)[:160])
    R.append((name, ok)); print('  %-4s %s — %s' % ('PASS' if ok else 'FAIL', name, why))

with contextlib.redirect_stdout(io.StringIO()):
    import world_engine as WE
    import register_census as RG
    W = RG.running_world()
ex = W.clock.eras['exodus']
EV = [l for l in W.log if l[0] == 'EVENT']
GRADES = ('VERBATIM', 'TURNED', 'SHORTENED', 'EXPANDED', 'SUPPLIED', 'DISAGREES')

def q1():
    import cold_run_opening_speech as OS
    rows = OS.DATA['the_readback']['value']
    gs = collections.Counter(r['grade'] for r in rows)
    return all(g in GRADES for g in gs) and len(gs) == 6 and len(rows) >= 20, 'rows %d, grades %s' % (len(rows), dict(gs))
def q2():
    import cold_run_opening_speech as OS
    rows = OS.DATA['the_readback']['value']
    found = 0
    for r in rows:
        if r['grade'] in ('SUPPLIED', 'DISAGREES') and not r.get('tape_kind'):
            found += 1; continue
        hit = [e for e in EV if e[2]['kind'] == r['tape_kind'] and WE.first_verse(e[2].get('case_source')) == WE.first_verse(r['tape_verse'])]
        found += bool(hit)
    return found == len(rows), 'rows %d, found on the running world %d' % (len(rows), found)
def q3():
    isr = W.entities.get('israel_people')
    sup = [e for e in isr.ledger if e['effect'] == 'commanded' and e.get('value') in ('journey_to_the_mountain_of_the_amorite', 'turn_northward', 'cross_the_brook_zered', 'begin_to_possess_sihons_land')]
    pos = {}
    for i, l in enumerate(W.log):
        if l[0] == 'EVENT':
            k = WE.first_verse(l[2].get('case_source'))
            if k and k not in pos: pos[k] = i
    ok = len(sup) == 4 and all(not e.get('open') for e in sup)
    order = []
    for e in sup:
        opener = WE.first_verse(e.get('case_source')); closer = WE.first_verse(str(e.get('closed_by', '')))
        order.append(opener in pos and closer in pos and pos[closer] < pos[opener])
    return ok and all(order) and len(order) == 4, 'supplied debits %d, closed %d, closer earlier on the tape %s' % (len(sup), sum(1 for e in sup if not e.get('open')), order)
def q4():
    lines = [e for e in EV if str(e[2].get('case_source', '')).startswith('Deut ')]
    dated = [e for e in lines if e[2].get('dated') is not None]
    mk = [l for l in W.log if l[0] == 'MARKER' and str(l[2].get('verse', '')).startswith('Deut ') and l[2].get('retrograde')]
    stated = {l[2]['stated'] for l in mk}
    return len(lines) == 12 and len(dated) == 11 and len(mk) == 3 and all(e[2]['dated'] in stated for e in dated), 'Deuteronomy lines %d, dated %d, retrograde markers %d, stated days %s' % (len(lines), len(dated), len(mk), sorted(ex.date(d) for d in stated))
def q5():
    import cold_run_opening_speech as OS
    rows = [r for r in OS.DATA['the_readback']['value'] if r['grade'] == 'DISAGREES']
    hits = [(ent.eid, e['effect']) for ent in W.entities.values() for e in ent.ledger if any(v in str(e.get('case_source', '')) for v in ('Deut 2:29', 'Deut 1:37'))]
    return len(rows) == 2 and not hits and all(r.get('open') for r in rows), 'DISAGREES rows %d (open %s), ledger entries citing them %d' % (len(rows), [r.get('open') for r in rows], len(hits))
def q6():
    with contextlib.redirect_stdout(io.StringIO()):
        ink = RG.read_ink(); cr = RG.class_receipts(ink, W); cf = RG.class_footers(ink)
    got = {k: cr[k]['class'] for k in ('Deut 1:3', 'Deut 1:19', 'Deut 1:41', 'Num 27:22') if k in cr}
    got['Deut 4:45'] = cf.get('Deut 4:45', {}).get('class')
    want = {'Deut 1:3': 'ACT', 'Deut 1:19': 'CHAPTER', 'Deut 1:41': 'CHAPTER', 'Num 27:22': 'CLOSE', 'Deut 4:45': 'DAEMONS'}   # 1:19 and 1:41 CHAPTER, not NONE — the gate's own class for a receipt whose chapter holds a closed entry (the Horeb debit at 1:6-8, closed by the prior run): read at the first tape run (2026-09-15), the design's NONE retyped; the receipts run citations still (R5)
    return got == want, 'got %s' % got

print('READBACK PROBES (THE LOOP step 6, the first form)')
for n, f in (('Q1 the table', q1), ('Q2 found', q2), ('Q3 the close by a prior run', q3), ('Q4 the retrograde dating', q4), ('Q5 the open disagreements', q5), ('Q6 the register seats', q6)):
    probe(n, f)
n_ok = sum(1 for _, ok in R if ok)
print('readback_probes: %d/%d' % (n_ok, len(R)))
sys.exit(0 if n_ok == len(R) else 1)
