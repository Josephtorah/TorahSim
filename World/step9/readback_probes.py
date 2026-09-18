#!/usr/bin/env python3
"""readback_probes.py — THE READBACK'S FIRST FORM (THE LOOP step 6; THE DEUTERONOMY WALK sitting 1b, 2026-09-15; World/step9/DEUTERONOMY_WALK.md
"Sitting 1b" (R1)-(R6)): the probes written to FAIL before cold_run_opening_speech.py exists, PASS after the tape carries Deuteronomy 1-3.
  Q1 the runner exists and its DATA row the_readback carries rows graded by the six grades (VERBATIM / TURNED / SHORTENED / EXPANDED / SUPPLIED / DISAGREES)
  Q2 every row's tape entry is FOUND on the running world by kind and first verse (rows n = found n)
  Q3 a SUPPLIED debit is CLOSED BY A PRIOR RUN — the closer's verse stands EARLIER on the tape than the line that opened the debit
  Q4 the supplied lines are DATED by a retrograde stretch — the event carries `dated`, its day the marker's stated day, not the counter's
  Q5 the two DISAGREES rows are OPEN — no ledger entry written for either (2:29's Edom, 1:37's ground of the bar)
  Q6 the register gate's seats on the new tape — Deut 1:3 ACT, 1:19 CHAPTER, 1:41 CHAPTER (the gate's class for a receipt whose chapter holds a closed entry — read at the first run; the design said NONE), Deut 4:45 DAEMONS, Num 27:22 CLOSE
  THE DEUTERONOMY WALK 2b (2026-09-16; DEUTERONOMY_WALK.md "Sitting 2b" THE PROBES) — written to FAIL before cold_run_obey_horeb.py exists:
  Q7 the runner and its the_readback table: eleven rows (SHORTENED 3, EXPANDED 5, SUPPLIED 2, DISAGREES 1), the two SUPPLIED rows naming their first tellings Exod 20:1 and 31:18 (THE TAPE'S HOLE)
  Q8 the two supplied Horeb lines DATED by the retrograde markers at Deut 4:10 and 4:13 — (1, 3, 7) the giving, (1, 4, 17) the tablets; the tablets' day = the breaking marker's (Exod 32:19)
  Q9 the register seats after chapter 4 — Deut 4:5 ACT, Deut 4:45 DAEMONS with daemons 2; the refuge debit appoint_six_cities_of_refuge OPEN after the three cities' line (Makkot 2:4); cities_set_apart on Israel ONE
  (Q4 NARROWED at 2b to chapters 1-3's lines and markers — the probe tests 1b's form, not the tape's length)
  THE DEUTERONOMY WALK 3b (2026-09-16; DEUTERONOMY_WALK.md "Sitting 3b" THE PROBES) — written to FAIL before cold_run_covenant_at_horeb.py exists:
  Q10 the runner and its the_readback table: twenty-one rows — sixteen LAW rows (one per verse of the second copy, 5:6-21) each naming its cell or NO CELL (5:6 alone), five narrative rows; the grades VERBATIM 5 / VARIANT 5 / EXPANDED 5 / TURNED 4 / SUPPLIED 2 (VARIANT the laws' readback's own grade); no row OPEN
  Q11 the two SUPPLIED lines (the request, the answer) DATED (1, 3, 7) by the retrograde marker at Deut 5:23; the request naming its first telling Exodus 20:18-19 (THE TAPE'S SECOND HOLE); the charge's debit on Moses CLOSED BY THE PRIOR RUN — the closer's line earlier on the tape (Q3's form)
  Q13 chapter 6's table — THE READBACK'S THIRD FORM (a retelling inside a law): seven rows — the son's answer's five (6:21-25), the header's (6:1), the test's (6:16) — every row a law's, every row's tape entry FOUND on the running world by kind and first verse (Q2's form), the grades VERBATIM 3 / EXPANDED 3 / SHORTENED 1, no row OPEN
  Q14 the two lines of chapter 6 (shema_declared 6:4-9, testing_barred 6:16-19) on the speech's own day — NO marker in chapter 6, the markers 167; shema_commanded (a status) and test_barred (a block) on Israel ONE each, their sources Deut 6:4 / Deut 6:16
  Q15 THE RECEIPT WITHOUT THE NAME — the register gate's own finder lists no seat at Deut 6:25 (its form has no Name; measured at the design), the RUN_CITATION pointer 'Deut 6:25' on file; the daemon law_hear_o_israel registered
  Q12 the register seats after chapter 5 — Deut 5:12, 5:16, 5:32 CHAPTER (the receipts inside the code, run citations of the giving), 4:45 DAEMONS with daemons 2; THE CODE'S HOLE FILLED — other_gods_barred and coveting_barred on Israel ONE each, dated (1, 3, 7), written at the giving's line (source Deut 4:10)
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
    lines = [e for e in EV if re.match(r'Deut [123]:', str(e[2].get('case_source', '')))]   # THE DEUTERONOMY WALK 2b (2026-09-16): chapters 1-3 only (the probe tests 1b's form)
    dated = [e for e in lines if e[2].get('dated') is not None]
    mk = [l for l in W.log if l[0] == 'MARKER' and re.match(r'Deut [123]:', str(l[2].get('verse', ''))) and l[2].get('retrograde')]
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

def q7():
    import cold_run_obey_horeb as OH
    rows = OH.DATA['the_readback']['value']
    gs = collections.Counter(r['grade'] for r in rows)
    sup = [r for r in rows if r['grade'] == 'SUPPLIED']
    named = sum(1 for r in sup if 'Exod 20:1' in str(r.get('entry', '')) + str(r.get('why', ''))) + sum(1 for r in sup if 'Exod 31:18' in str(r.get('entry', '')) + str(r.get('why', '')))
    return len(rows) == 11 and gs == collections.Counter({'EXPANDED': 5, 'SHORTENED': 3, 'SUPPLIED': 2, 'DISAGREES': 1}) and named == 2, 'rows %d, grades %s, the first tellings named %d' % (len(rows), dict(gs), named)
def q8():
    tw = [e for e in EV if e[2]['kind'] == 'ten_words_declared']; tb = [e for e in EV if e[2]['kind'] == 'tablets_given']
    mk = {str(l[2].get('verse', '')): l for l in W.log if l[0] == 'MARKER'}
    d_tw = ex.date(tw[0][2]['dated']) if tw and tw[0][2].get('dated') is not None else None
    d_tb = ex.date(tb[0][2]['dated']) if tb and tb[0][2].get('dated') is not None else None
    same = bool(tb) and 'Exod 32:19' in mk and tb[0][2].get('dated') == mk['Exod 32:19'][1]
    ok = len(tw) == 1 and len(tb) == 1 and d_tw == (1, 3, 7) and d_tb == (1, 4, 17) and 'Deut 4:10' in mk and 'Deut 4:13' in mk and mk['Deut 4:10'][2].get('retrograde') and mk['Deut 4:13'][2].get('retrograde') and same
    return ok, 'ten_words_declared %d dated %s; tablets_given %d dated %s; the markers at Deut 4:10 / 4:13 %s / %s; the tablets\' day = the breaking\'s %s' % (len(tw), d_tw, len(tb), d_tb, 'Deut 4:10' in mk, 'Deut 4:13' in mk, same)
def q9():
    with contextlib.redirect_stdout(io.StringIO()):
        ink = RG.read_ink(); cr = RG.class_receipts(ink, W); cf = RG.class_footers(ink)
    isr = W.entities.get('israel_people')
    deb = [e for e in isr.ledger if e['effect'] == 'commanded' and e.get('value') == 'appoint_six_cities_of_refuge'] if isr else []
    csa = [e for e in isr.ledger if e['effect'] == 'cities_set_apart'] if isr else []
    got = (cr.get('Deut 4:5', {}).get('class'), cf.get('Deut 4:45', {}).get('class'), cf.get('Deut 4:45', {}).get('daemons'), len(deb), bool(deb) and deb[0].get('open'), len(csa))
    return got == ('ACT', 'DAEMONS', 2, 1, True, 1), 'got (4:5 class, 4:45 class, 4:45 daemons, the refuge debit, open, cities_set_apart) = %s' % (got,)
# ---- THE DEUTERONOMY WALK 3b (2026-09-16): the laws' readback on chapter 5 — written to FAIL before the runner exists ----
def q10():
    import cold_run_covenant_at_horeb as CH
    rows = CH.DATA['the_readback']['value']
    gs = collections.Counter(r['grade'] for r in rows)
    law = [r for r in rows if r.get('law')]
    nocell = [r['verses'] for r in law if r.get('cell') == 'NO CELL']
    named = sum(1 for r in law if r.get('cell') and r['cell'] != 'NO CELL')
    ok = len(rows) == 21 and len(law) == 16 and named == 15 and nocell == ['Deut 5:6'] and gs == collections.Counter({'VERBATIM': 5, 'VARIANT': 5, 'EXPANDED': 5, 'TURNED': 4, 'SUPPLIED': 2}) and not any(r['open'] for r in rows)
    return ok, 'rows %d (law %d, cells named %d, no cell %s), grades %s' % (len(rows), len(law), named, nocell, dict(gs))
def q11():
    mr = [e for e in EV if e[2]['kind'] == 'mediator_requested']; sh = [e for e in EV if e[2]['kind'] == 'stand_here_commanded']
    mk = {str(l[2].get('verse', '')): l for l in W.log if l[0] == 'MARKER'}
    d1 = ex.date(mr[0][2]['dated']) if mr and mr[0][2].get('dated') is not None else None
    d2 = ex.date(sh[0][2]['dated']) if sh and sh[0][2].get('dated') is not None else None
    first = 'Exod 20:18-19' in str(mr[0][2].get('first_telling', '')) if mr else False
    mo = W.entities.get('moses'); deb = [e for e in mo.ledger if e['effect'] == 'commanded' and e.get('value') == 'teach_the_commandment'] if mo else []
    ev_i = [(i, l[2]) for i, l in enumerate(W.log) if l[0] == 'EVENT']
    def at_verse(k): return min([i for i, e in ev_i if RG.contains(e.get('case_source'), k)], default=10 ** 9)   # the line whose source CONTAINS the verse (the frame's 1:1-5 holds the closer's 1:5); first_verse returns a (book, chapter, verse) tuple
    closer_earlier = bool(deb) and not deb[0].get('open') and at_verse(WE.first_verse(deb[0].get('closed_by'))) < at_verse(('Deut', 5, 28))
    ok = len(mr) == 1 and len(sh) == 1 and d1 == (1, 3, 7) and d2 == (1, 3, 7) and 'Deut 5:23' in mk and bool(mk['Deut 5:23'][2].get('retrograde')) and first and len(deb) == 1 and closer_earlier
    return ok, "mediator_requested %d dated %s (the first telling named %s); stand_here_commanded %d dated %s; the marker at Deut 5:23 %s; the charge's debit %d, closed by the prior run %s" % (len(mr), d1, first, len(sh), d2, 'Deut 5:23' in mk, len(deb), closer_earlier)
def q12():
    with contextlib.redirect_stdout(io.StringIO()):
        ink = RG.read_ink(); cr = RG.class_receipts(ink, W); cf = RG.class_footers(ink)
    isr = W.entities.get('israel_people')
    og = [e for e in isr.ledger if e['effect'] == 'other_gods_barred'] if isr else []; cv = [e for e in isr.ledger if e['effect'] == 'coveting_barred'] if isr else []
    got = (cr.get('Deut 5:12', {}).get('class'), cr.get('Deut 5:16', {}).get('class'), cr.get('Deut 5:32', {}).get('class'), cf.get('Deut 4:45', {}).get('daemons'), len(og), len(cv), ex.date(og[0]['dated']) if og and og[0].get('dated') is not None else None, str(og[0].get('case_source', ''))[:9] if og else None)
    return got == ('CHAPTER', 'CHAPTER', 'CHAPTER', 2, 1, 1, (1, 3, 7), 'Deut 4:10'), "got (5:12, 5:16, 5:32 classes, 4:45 daemons, other_gods_barred, coveting_barred, the blocks' day, source) = %s" % (got,)

# ---- THE DEUTERONOMY WALK 4b (2026-09-17): the readback's third form on chapter 6 — written to FAIL before the runner exists ----
def q13():
    import cold_run_hear_o_israel as HO
    rows = HO.DATA['the_readback']['value']
    gs = collections.Counter(r['grade'] for r in rows)
    found = sum(1 for r in rows if any(e[2]['kind'] == r['tape_kind'] and WE.first_verse(e[2].get('case_source')) == WE.first_verse(r['tape_verse']) for e in EV))   # FOUND ON THE RUNNING WORLD (Q2's form; the tape's CO4) — RUN 4's retype: the rows carry no 'found' key
    law = sum(1 for r in rows if r.get('law'))
    ok = len(rows) == 7 and found == 7 and law == 7 and gs == collections.Counter({'VERBATIM': 3, 'EXPANDED': 3, 'SHORTENED': 1}) and not any(r.get('open') for r in rows)
    return ok, 'rows %d (found on the running world %d, every row a law\'s %d), grades %s, open %d' % (len(rows), found, law, dict(gs), sum(1 for r in rows if r.get('open')))
def q14():
    sd = [e for e in EV if e[2]['kind'] == 'shema_declared']; tb = [e for e in EV if e[2]['kind'] == 'testing_barred']
    mk = {str(l[2].get('verse', '')): l for l in W.log if l[0] == 'MARKER'}
    nm = len([l for l in W.log if l[0] == 'MARKER'])
    isr = W.entities.get('israel_people')
    sc = [e for e in isr.ledger if e['effect'] == 'shema_commanded'] if isr else []; tbd = [e for e in isr.ledger if e['effect'] == 'test_barred'] if isr else []
    got = (len(sd), len(tb), any(k.startswith('Deut 6:') for k in mk), nm, len(sc), len(tbd), str(sc[0].get('case_source', ''))[:8] if sc else None, str(tbd[0].get('case_source', ''))[:9] if tbd else None)
    return got == (1, 1, False, 167, 1, 1, 'Deut 6:4', 'Deut 6:16'), 'got (shema_declared, testing_barred, a chapter-6 marker, markers, shema_commanded, test_barred, their sources) = %s' % (got,)
def q15():
    import yaml as _y
    with contextlib.redirect_stdout(io.StringIO()):
        ink = RG.read_ink(); cr = RG.class_receipts(ink, W)
    dep = _y.safe_load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'dependency_dispositions.yaml'), encoding='utf-8'))
    ptr = [p for p in dep['pointers'] if p.get('verse') == 'Deut 6:25' and p.get('disposition') == 'RUN_CITATION']
    dd = _y.safe_load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'daemon_dispositions.yaml'), encoding='utf-8'))
    got = ('Deut 6:25' in cr, len(ptr), 'law_hear_o_israel' in dd['daemons'], dd['daemons'].get('law_hear_o_israel', {}).get('given_at'))
    return got == (False, 1, True, 'Deut 6:4'), "got (the gate sees 6:25, the pointer rows, the daemon registered, given_at) = %s" % (got,)

# ---- THE DEUTERONOMY WALK 5b (2026-09-18): the readback on the kin — chapter 7's laws re-declared for the land, graded against the kin's cells by CALL and
# the tape's lines by kind and verse; written to FAIL before the runner exists (the design's Q16-Q18) ----
def q16():
    import cold_run_seven_nations as SN
    tbl = SN.DATA['the_readback']; rows = tbl['value']; holes = tbl.get('holes') or []
    gs = collections.Counter(r['grade'] for r in rows)
    on_tape = sum(1 for r in rows if r.get('tape_kind') and any(e[2]['kind'] == r['tape_kind'] and WE.first_verse(e[2].get('case_source')) == WE.first_verse(r['tape_verse']) for e in EV))
    by_call = sum(1 for r in rows if r.get('cell') and r.get('cell_found'))
    ok = len(rows) == 21 and on_tape + by_call == 21 and gs == collections.Counter({'VERBATIM': 4, 'VARIANT': 5, 'EXPANDED': 8, 'TURNED': 3, 'SHORTENED': 1}) and len(holes) == 4 and not any(r.get('open') for r in rows)
    return ok, 'rows %d (found on the tape %d, in the kin\'s cells by CALL %d), grades %s, the code\'s holes %d, open %d' % (len(rows), on_tape, by_call, dict(gs), len(holes), sum(1 for r in rows if r.get('open')))
def q17():
    nd = [e for e in EV if e[2]['kind'] == 'nations_devoted']; hb = [e for e in EV if e[2]['kind'] == 'hearing_blessed']; ab = [e for e in EV if e[2]['kind'] == 'abomination_barred']
    mk = {str(l[2].get('verse', '')): l for l in W.log if l[0] == 'MARKER'}; nm = len([l for l in W.log if l[0] == 'MARKER'])
    isr = W.entities.get('israel_people')
    def L(eff): return [e for e in isr.ledger if e['effect'] == eff] if isr else []
    cmd = [e for e in L('commanded') if e.get('value') == 'devote_the_seven_nations']; hab = L('house_abomination_barred')
    got = (len(nd), len(hb), len(ab), any(k.startswith('Deut 7:') for k in mk), nm, len(cmd), len(L('covenant_barred')), len(L('favor_barred')), len(L('intermarriage_barred')), len(L('blessings_for_hearing')), len(L('pity_barred')), len(hab), str(cmd[0].get('case_source', ''))[:8] if cmd else None, str(hab[0].get('case_source', ''))[:9] if hab else None)
    return got == (1, 1, 1, False, 167, 1, 1, 1, 1, 1, 1, 1, 'Deut 7:1', 'Deut 7:25'), 'got (nations_devoted, hearing_blessed, abomination_barred, a chapter-7 marker, markers, the ban\'s debit, covenant_barred, favor_barred, intermarriage_barred, blessing_promised, pity_barred, house_abomination_barred, their sources) = %s' % (got,)
def q18():
    import yaml as _y
    isr = W.entities.get('israel_people')
    def L(eff): return [e for e in isr.ledger if e['effect'] == eff] if isr else []
    dsp = [e for e in L('commanded') if str(e.get('value', '')).startswith('dispossess') or e.get('value') == 'destroy_their_images']
    land = W.entities.get('the-land'); hp = [e for e in land.ledger if e['effect'] == 'high_places_banned'] if land else []
    dd = _y.safe_load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'daemon_dispositions.yaml'), encoding='utf-8'))
    d = dd['daemons'].get('law_seven_nations', {})
    got = (len(L('other_gods_barred')), len(L('coveting_barred')), len(L('treasured_people')), len(dsp), bool(hp), 'law_seven_nations' in dd['daemons'], d.get('given_at'), d.get('installed_by'))
    return got == (1, 1, 1, 2, True, True, 'Deut 7:1', 'boot'), 'got (other_gods_barred, coveting_barred, treasured_people, the dispossession\'s debits, high_places_banned present, the daemon registered, given_at, installed_by) = %s' % (got,)

print('READBACK PROBES (THE LOOP step 6, the first form)')
for n, f in (('Q1 the table', q1), ('Q2 found', q2), ('Q3 the close by a prior run', q3), ('Q4 the retrograde dating', q4), ('Q5 the open disagreements', q5), ('Q6 the register seats', q6), ('Q7 chapter 4\'s table', q7), ('Q8 the Horeb lines dated', q8), ('Q9 the seats and the debit after chapter 4', q9), ("Q10 chapter 5's table — the laws' readback", q10), ('Q11 the request and the answer dated; the charge closed by the prior run', q11), ('Q12 the seats after chapter 5; the code\'s hole filled', q12), ('Q13 chapter 6\'s table — the readback\'s third form', q13), ('Q14 the two lines on the speech\'s day, no marker', q14), ('Q15 the receipt without the Name; the pointer; the daemon', q15), ('Q16 chapter 7\'s table — the readback on the kin', q16), ('Q17 the three lines on the speech\'s day, no marker; the seven writes', q17), ('Q18 the kin stands; the daemon', q18)):
    probe(n, f)
n_ok = sum(1 for _, ok in R if ok)
print('readback_probes: %d/%d' % (n_ok, len(R)))
sys.exit(0 if n_ok == len(R) else 1)
