import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE DEUTERONOMY WALK 11b (2026-09-21): readback_probes.py Q34-Q36 written to FAIL before cold_run_seducers.py exists (the design's THE PROBES paragraph — RUN B's
# FIRST step, before the types: 7b's lesson 2; Q31-Q33's form). Q34 the runner and its the_readback table — THE FORMS ON FILE, NO NEW FORM: nineteen rows predicted
# from the design (one per verse; VERBATIM 3 / VARIANT 5 / EXPANDED 3 / SUPPLIED 8; seven on the tape by kind and first verse, SEVENTEEN in the kin's cells by CALL — five rows both, RETYPED from the fast checker's print (the design's ten); two
# with neither — 13:12 and 13:15 the formulas' first seats; EIGHT rows SUPPLIED AS LAWS: 13:4, 13:12, 13:15, 13:18 WITH THEIR WRITES (false_prophet_hearing_barred,
# israel_hears_and_fears, condemned_city_inquiry_required, devoted_thing_cleaving_barred), 13:2, 13:7, 13:13 the lines' own first seats, 13:6 the case's; the pointer
# row 13:18; no state row, no stretch, no hole, no open row, no retrograde row) — retyped ONCE from the runner's print if the census moves (4b's lesson); Q35 the FOUR
# OWN-DAY lines word_sealed (13:1), prophet_test_declared (13:2-6), inciter_law_declared (13:7-12) and condemned_city_law_declared (13:13-19) after the tape's last
# Deuteronomy 12 line, on the counter's day (40, 11, 1), no dated field, NO marker at any Deut 13 verse, markers 172 UNMOVED; their EIGHT writes — five NEW on
# israel_people ONE each (false_prophet_hearing_barred, devoted_thing_cleaving_barred BLOCKS; tested_by_the_lord, israel_hears_and_fears,
# condemned_city_inquiry_required STATUSES) and THREE REUSES TWO each (adding_barred 4:1's and 13:1's, cleaving_commanded 10:20's and 13:2's line, pity_barred 7:12's
# and 13:7's line — 8b's lesson: a reused effect is a second entry on the same ledger); the six blocks; the daemon registered; Q36 the kin standing (DE5's counts) and
# THE HOLES FILLED (DE4, DE6 — the five names on israel_people this sitting's alone; the case's two effects on no ledger of the tape; the runner's scans at import).
# THE GREP DECIDED (10b's lesson 1 — a boolean is not a count; here every seat IS a count): SEVEN seats hold the reuse counts ONE — the checkpoints CC3 (adding_barred),
# CQ6 (pity_barred), DB2 (cleaving_commanded) and DC6 (pity_barred, cleaving_commanded) in cold_run_sequence.py, retyped ONE -> TWO at patch_seq_literals_ch13.py
# BEFORE the tape; and the probes Q17 (pity_barred), Q27 (cleaving_commanded) and Q30 (pity_barred, cleaving_commanded) RETYPED HERE — they FAIL beside Q34-Q36 until
# the tape carries the chapter's lines (30/36 expected on this run). Idempotent. patch_probes_ch12.py's form. RUN FROM THE REPO ROOT.
import subprocess, os
ROOT = _ROOT
P = ROOT + '/World/step9/readback_probes.py'
s = open(P, encoding='utf-8').read()
assert 'def q34():' not in s, 'already patched'
def rep(old, new):
    global s
    assert s.count(old) == 1, (s.count(old), old[:90]); s = s.replace(old, new)
# ---- THE RETYPES (the grep decided; a count literal in a PROBE moves like one in a checkpoint — 7b's lesson) ----
rep("    return got == (1, 1, 1, False, 172, 1, 1, 1, 1, 1, 1, 1, 'Deut 7:1', 'Deut 7:25'), 'got (nations_devoted,",
    "    # THE DEUTERONOMY WALK 11b (2026-09-21): pity_barred ONE -> TWO on israel_people (13:9's second entry on the line inciter_law_declared — the REUSE; retyped BEFORE the tape, the grep decided; its first entry's source 7:12's unmoved)\n    return got == (1, 1, 1, False, 172, 1, 1, 1, 1, 1, 2, 1, 'Deut 7:1', 'Deut 7:25'), 'got (nations_devoted,")
rep("    return got == (list(OWN), True, [(40, 11, 1)], 0, ((1, 'Deut 10:1'), (1, 'Deut 10:1'), (1, 'Deut 10:1'), (1, 'Deut 10:1'), (1, 'Deut 10:2')), (1, 1, 1, (1, 2), 2, 1, 1, 1, 30, 1), True, 'Deut 10:1', 'boot')",
    "    # THE DEUTERONOMY WALK 11b (2026-09-21): cleaving_commanded ONE -> TWO on israel_people (13:5's second entry on the line prophet_test_declared — the REUSE; retyped BEFORE the tape, the grep decided; its first entry's source 10:20's unmoved)\n    return got == (list(OWN), True, [(40, 11, 1)], 0, ((1, 'Deut 10:1'), (1, 'Deut 10:1'), (1, 'Deut 10:1'), (1, 'Deut 10:1'), (2, 'Deut 10:2')), (1, 1, 1, (1, 2), 2, 1, 1, 1, 30, 1), True, 'Deut 10:1', 'boot')")
rep("    return got == ((1, 1, 1, 1, 1, 1, 1, 1, 1, 1), ['heavens_shut_for_turning', 'rain_in_its_season', 'yoke_of_the_commandments_accepted'], ['rain_in_its_season', 'restraint_failed', 'speech_restrained'], (10, 1, 1, 1, 1, False, 1))",
    "    # THE DEUTERONOMY WALK 11b (2026-09-21): pity_barred (the fourth) and cleaving_commanded (the sixth) ONE -> TWO on israel_people (13:9's and 13:5's second entries — the REUSES; retyped BEFORE the tape, the grep decided)\n    return got == ((1, 1, 1, 2, 1, 2, 1, 1, 1, 1), ['heavens_shut_for_turning', 'rain_in_its_season', 'yoke_of_the_commandments_accepted'], ['rain_in_its_season', 'restraint_failed', 'speech_restrained'], (10, 1, 1, 1, 1, False, 1))")
NEW = '''
# ---- THE DEUTERONOMY WALK 11b (2026-09-21): THE FORMS ON FILE, NO NEW FORM — chapter 13 is the header's seal (13:1), the prophet and the test (13:2-6), the inciter
# (13:7-12), the city heard of, the inquiry and the sword (13:13-16), the whole offering, the heap and the mercy (13:17-18) and the footer (13:19): T4 rows graded
# against the cells that compile their kin by CALL and T1 reference rows against the tape's lines by kind and first verse; EIGHT rows SUPPLIED AS LAWS (the code's
# four holes compiled at the chapter's own day — four with their writes, three the lines' own first seats, 13:6 the case's); the pointer 13:18 ('as He swore to your
# fathers' — the oath's AS_WHEN form); no state row, no stretch, no hole, no open row, no retrograde row; written to FAIL before the runner exists (the design's Q34-Q36) ----
def q34():
    import cold_run_seducers as SE
    tbl = SE.DATA['the_readback']; rows = tbl['value']; holes = tbl.get('holes') or []; opens = tbl.get('open_rows') or []
    gs = collections.Counter(r['grade'] for r in rows)
    on_tape = sum(1 for r in rows if r.get('tape_kind') and any(e[2]['kind'] == r['tape_kind'] and WE.first_verse(e[2].get('case_source')) == WE.first_verse(r['tape_verse']) for e in EV))
    by_call = sum(1 for r in rows if r.get('cell') and r.get('cell_found'))
    sup = [r for r in rows if r['grade'] == 'SUPPLIED']
    ptr = [r for r in rows if r.get('pointer')]
    ok = len(rows) == 19 and on_tape + by_call == 24 and gs == collections.Counter({'VERBATIM': 3, 'VARIANT': 5, 'EXPANDED': 3, 'SUPPLIED': 8}) and len(holes) == 0 and len(opens) == 0 and not any(r.get('open') for r in rows) and not any(r.get('stretch') for r in rows) and not any(r.get('state') for r in rows) and len(sup) == 8 and [r['verses'] for r in sup] == ['Deut 13:2', 'Deut 13:4', 'Deut 13:6', 'Deut 13:7', 'Deut 13:12', 'Deut 13:13', 'Deut 13:15', 'Deut 13:18'] and [r.get('write') for r in sup] == [None, 'false_prophet_hearing_barred', None, None, 'israel_hears_and_fears', None, 'condemned_city_inquiry_required', 'devoted_thing_cleaving_barred'] and [r['verses'] for r in ptr] == ['Deut 13:18']
    return ok, 'rows %d (found on the tape %d, in the kin\\'s cells by CALL %d), grades %s, the holes %d, the OPEN rows %d, open-flagged %d, stretch rows %d, state rows %d, the SUPPLIED rows %s with their writes %s, the pointer rows %s' % (len(rows), on_tape, by_call, dict(gs), len(holes), len(opens), sum(1 for r in rows if r.get('open')), sum(1 for r in rows if r.get('stretch')), sum(1 for r in rows if r.get('state')), [r['verses'] for r in sup], [r.get('write') for r in sup], [r['verses'] for r in ptr])
def q35():
    import yaml as _y
    def ENT(*names):
        for n_ in names:
            if n_ in W.entities: return W.entities[n_]
        return None
    def L(ent, eff):
        e_ = ENT(*ent) if isinstance(ent, tuple) else ENT(ent); return [e for e in e_.ledger if e['effect'] == eff] if e_ else []
    OWN = ('word_sealed', 'prophet_test_declared', 'inciter_law_declared', 'condemned_city_law_declared')
    own = [e for e in EV if e[2]['kind'] in OWN]
    idx = {id(l): i for i, l in enumerate(W.log)}
    i_last12 = max([i for i, l in enumerate(W.log) if l[0] == 'EVENT' and str(l[2].get('case_source', '')).startswith('Deut 12:')] or [-1])
    after = bool(own) and all(idx[id(e)] > i_last12 for e in own)
    mk13 = [l for l in W.log if l[0] == 'MARKER' and str(l[2].get('verse', '')).startswith('Deut 13:')]; nm = len([l for l in W.log if l[0] == 'MARKER'])
    days = sorted({ex.date(e[1]) for e in own}); dated = sum(1 for e in own if e[2].get('dated') is not None)
    W5 = [('false_prophet_hearing_barred', 'Deut 13:2'), ('tested_by_the_lord', 'Deut 13:2'), ('israel_hears_and_fears', 'Deut 13:7'), ('condemned_city_inquiry_required', 'Deut 13:13'), ('devoted_thing_cleaving_barred', 'Deut 13:13')]
    FV = lambda t_: '%s %d:%d' % t_ if isinstance(t_, tuple) else str(t_)   # WE.first_verse returns a (book, chapter, verse) tuple — formatted to the literal's 'Deut 13:2' (10b's Q32 form)
    w5 = tuple((len(L('israel_people', eff)), FV(WE.first_verse(str(L('israel_people', eff)[0].get('case_source', '')))) if L('israel_people', eff) else None) for eff, _ in W5)
    r3 = tuple((len(L('israel_people', eff)), [FV(WE.first_verse(str(e.get('case_source', '')))) for e in L('israel_people', eff)]) for eff in ('adding_barred', 'cleaving_commanded', 'pity_barred'))
    blocks = sum(1 for eff in ('adding_barred', 'false_prophet_hearing_barred', 'pity_barred', 'devoted_thing_cleaving_barred') for e in L('israel_people', eff) if e.get('op') == 'block')
    dd = _y.safe_load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'daemon_dispositions.yaml'), encoding='utf-8'))
    d = dd['daemons'].get('law_seducers', {})
    got = ([e[2]['kind'] for e in own], after, len(mk13), nm, days, dated, w5, r3, blocks, 'law_seducers' in dd['daemons'], d.get('given_at'), d.get('installed_by'))
    return got == (list(OWN), True, 0, 172, [(40, 11, 1)], 0, ((1, 'Deut 13:2'), (1, 'Deut 13:2'), (1, 'Deut 13:7'), (1, 'Deut 13:13'), (1, 'Deut 13:13')), ((2, ['Deut 4:1', 'Deut 13:1']), (2, ['Deut 10:20', 'Deut 13:2']), (2, ['Deut 7:12', 'Deut 13:7'])), 6, True, 'Deut 13:1', 'boot'), 'got (the four own-day lines in the ink\\'s order, all after the tape\\'s last Deuteronomy 12 line, markers at Deut 13 (none), markers, their day, dated fields (none), the five NEW writes on israel_people with their lines\\' first verses (false_prophet_hearing_barred, tested_by_the_lord, israel_hears_and_fears, condemned_city_inquiry_required, devoted_thing_cleaving_barred), THE THREE REUSES with their entries\\' first verses (adding_barred, cleaving_commanded, pity_barred — the first entries 4:1\\'s, 10:20\\'s, 7:12\\'s and the chapter\\'s second), the six blocks, the daemon registered, given_at, installed_by) = %s' % (got,)
def q36():
    import yaml as _y, cold_run_seducers as SE
    def ENT(*names):
        for n_ in names:
            if n_ in W.entities: return W.entities[n_]
        return None
    def L(ent, eff):
        e_ = ENT(*ent) if isinstance(ent, tuple) else ENT(ent); return [e for e in e_.ledger if e['effect'] == eff] if e_ else []
    def n(ent, eff): return len(L(ent, eff))
    def nall(eff): return sum(1 for ent in W.entities.values() for e in ent.ledger if e['effect'] == eff)
    isr = ENT('israel_people')
    ban = [e for e in (isr.ledger if isr else []) if e['effect'] == 'commanded' and e.get('value') == 'devote_the_seven_nations']
    open_debits = len([e for e in isr.ledger if e.get('op') == 'debit' and not e.get('closed_by')]) if isr else None
    cv = L('israel_people', 'cherem_vowed')
    kin = (n('israel_people', 'other_gods_barred'), n('israel_people', 'test_barred'), n('israel_people', 'house_abomination_barred'), len(ban), bool(ban) and not ban[0].get('closed_by'), len(cv), bool(cv) and bool(cv[0].get('closed_by')), n(('the_king_of_arad', 'the-king-of-arad'), 'destroyed'), n(('the_blasphemer', 'the-blasphemer'), 'stoned'), n(('the_wood_gatherer', 'the-wood-gatherer'), 'stoned'), open_debits)
    OWN5 = ('false_prophet_hearing_barred', 'tested_by_the_lord', 'israel_hears_and_fears', 'condemned_city_inquiry_required', 'devoted_thing_cleaving_barred')
    holes = sorted({e['effect'] for e in (isr.ledger if isr else []) if any(t in e['effect'] for t in ('false_prophet', 'tested_by', 'hears_and_fears', 'condemned_city', 'devoted_thing'))})
    fx = _y.safe_load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'effect_vocabulary.yaml'), encoding='utf-8'))['effects']
    vocab7 = all(k in fx for k in OWN5 + ('evil_purged_from_the_midst', 'city_devoted'))
    got = (kin, holes, vocab7, nall('evil_purged_from_the_midst'), nall('city_devoted'), SE.SEDUCERS_SCAN in ([], None), SE.REUSE_SCAN in ([['israel_people'], ['israel_people'], ['israel_people']], None))
    return got == ((1, 1, 1, 1, True, 1, True, 1, 1, 1, 10), sorted(OWN5), True, 0, 0, True, True), 'got (THE KIN STANDING (other_gods_barred, test_barred, house_abomination_barred on israel_people; the ban\\'s debit — count, OPEN; cherem_vowed — count, CLOSED by Num 21:3; destroyed on the king of Arad; stoned on the blasphemer and on the wood-gatherer; the open debits on israel_people), THE HOLES FILLED (the effects naming the false prophet\\'s hearing, the LORD\\'s testing, Israel\\'s hearing and fearing, the condemned city\\'s inquiry or the devoted thing\\'s cleaving on israel_people — this sitting\\'s five alone), the vocabulary holds the seven, the case\\'s two effects on no ledger of the tape (evil_purged_from_the_midst, city_devoted — written at the exam only), the one database scanned EMPTY of the five before this daemon\\'s lines, the three reused effects on israel_people alone before) = %s' % (got,)
'''
a = "\nprint('READBACK PROBES (THE LOOP step 6, the first form)')"
assert s.count(a) == 1
s = s.replace(a, NEW + a)
old = "('Q33 the kin stands; the holes filled; the eras table unmoved', q33)):"
assert s.count(old) == 1, s.count(old)
s = s.replace(old, "('Q33 the kin stands; the holes filled; the eras table unmoved', q33), ('Q34 chapter 13\\'s table — the forms on file, no new form', q34), ('Q35 the four own-day lines and their eight writes (three reuses); no marker; the daemon', q35), ('Q36 the kin stands; the holes filled; the case\\'s effects off the tape', q36)):")
old2 = "Run: python3 World/step9/readback_probes.py"
assert s.count(old2) == 1
s = s.replace(old2, "  THE DEUTERONOMY WALK 11b (2026-09-21; DEUTERONOMY_WALK.md \"Sitting 11b\" THE PROBES) — written to FAIL before cold_run_seducers.py exists:\n  Q34 chapter 13's table — THE FORMS ON FILE, NO NEW FORM (the header's seal 13:1, the prophet and the test 13:2-6, the inciter 13:7-12, the city heard of, the inquiry and the sword 13:13-16, the whole offering, the heap and the mercy 13:17-18, the footer 13:19): nineteen rows predicted from the design, one per verse (VERBATIM 3 / VARIANT 5 / EXPANDED 3 / SUPPLIED 8; seven on the tape by kind and first verse, ten in the kin's cells by CALL, two with neither — 13:12 and 13:15 the formulas' first seats; retyped once from the print if the census moves); EIGHT rows SUPPLIED AS LAWS — 13:4 false_prophet_hearing_barred (with tested_by_the_lord), 13:12 israel_hears_and_fears, 13:15 condemned_city_inquiry_required, 13:18 devoted_thing_cleaving_barred WITH THEIR WRITES (the code's holes, each a law's first seat), 13:2, 13:7, 13:13 the lines' own first seats, 13:6 the case's (put_to_death by the parameter, evil_purged_from_the_midst — THE PURGE FORMULA'S FIRST SEAT OF NINE); the pointer row 13:18 ('as He swore to your fathers' — the oath's AS_WHEN form, RUN_CITATION if the census demands); no state row, no stretch, no hole, no open row, no retrograde row\n  Q35 the FOUR OWN-DAY lines word_sealed (13:1), prophet_test_declared (13:2-6), inciter_law_declared (13:7-12) and condemned_city_law_declared (13:13-19) after the tape's last Deuteronomy 12 line on the counter's day (40, 11, 1), no dated field, NO marker at any Deut 13 verse (markers 172 UNMOVED); their EIGHT writes — five NEW on israel_people ONE each (two BLOCKS: false_prophet_hearing_barred, devoted_thing_cleaving_barred; three STATUSES: tested_by_the_lord, israel_hears_and_fears, condemned_city_inquiry_required) and THREE REUSES TWO each (adding_barred — 4:1's and 13:1's; cleaving_commanded — 10:20's and 13:5's on the line prophet_test_declared; pity_barred — 7:16's and 13:9's on the line inciter_law_declared: a second entry on the same ledger, 8b's lesson); the six blocks; the daemon law_seducers registered, given_at Deut 13:1, installed_by boot\n  Q36 the kin stands — other_gods_barred ONE, test_barred ONE, house_abomination_barred ONE on israel_people, the ban's debit ONE and OPEN, cherem_vowed ONE and CLOSED (Num 21:3), destroyed ONE on the king of Arad, stoned ONE on the blasphemer and ONE on the wood-gatherer, the open debits on israel_people 10 UNMOVED (no debit this chapter); THE HOLES FILLED — the effects naming the false prophet's hearing, the LORD's testing, Israel's hearing and fearing, the condemned city's inquiry or the devoted thing's cleaving on israel_people this sitting's five alone, the vocabulary holding the seven (the case's evil_purged_from_the_midst and city_devoted on no ledger of the tape — written at the exam only); the one database scanned EMPTY of the five before this daemon's lines and the three reused effects on israel_people alone before\n" + old2)
open(P, 'w', encoding='utf-8').write(s)
import py_compile; py_compile.compile(P, doraise=True)
print('patched readback_probes.py: Q34-Q36 added (written to FAIL); Q17, Q27, Q30 retyped ONE -> TWO for the three reuses (the grep decided: seven count seats — four checkpoints, three probes); compiles')
