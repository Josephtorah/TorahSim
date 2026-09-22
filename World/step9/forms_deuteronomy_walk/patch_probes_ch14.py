import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE DEUTERONOMY WALK 12b (2026-09-22): readback_probes.py Q37-Q39 written to FAIL before cold_run_food_tithe.py exists (the design's THE PROBES paragraph — RUN B's
# FIRST step, before the types: 7b's lesson 2; Q34-Q36's form). Q37 the runner and its the_readback table — THE FORMS ON FILE, NO NEW FORM: twenty-nine rows
# predicted from the design (one per verse; VERBATIM 6 / VARIANT 11 / EXPANDED 4 / SUPPLIED 8; ten on the tape by kind and first verse, twenty-nine in the kin's
# cells by CALL — every row has kin, 11b's lesson 8; RETYPED ONCE from the runner's print if the census moves, 4b's lesson); EIGHT rows SUPPLIED — 14:1, 14:3,
# 14:22, 14:28 AS LAWS WITH THEIR WRITES (cuttings_for_the_dead_barred, abomination_eating_barred, second_tithe_owed, poor_tithe_owed), 14:5 the ten named
# (Solomon's table the one kin), 14:11 and 14:20 the permission Leviticus lacks (the_birds_signs a parameter), 14:25 the money's first seat (the_moneys_form a
# parameter); 14:21 EXPANDED WITH ITS WRITE (carcass_eating_barred — the ban's seat named by the sanctions engine); no pointer row, no state row, no stretch, no
# hole, no open row, no retrograde row; Q38 the FIVE OWN-DAY lines sons_and_mourning_declared (14:1-2), food_law_declared (14:3-20), carcass_and_kid_declared
# (14:21), second_tithe_declared (14:22-27) and third_year_tithe_declared (14:28-29) after the tape's last Deuteronomy 13 line, on the counter's day (40, 11, 1),
# no dated field, NO marker at any Deut 14 verse, markers 172 UNMOVED; their SEVEN writes — five NEW on israel_people ONE each (three BLOCKS: cuttings_for_the_dead_barred,
# abomination_eating_barred, carcass_eating_barred; two STATUSES: second_tithe_owed, poor_tithe_owed) and TWO REUSES TWO each (rejoicing_before_the_lord_commanded —
# 12:5's line and 14:22's line, 14:26's seat; levite_forsaking_barred — 12:15's line and 14:22's line, 14:27's seat: a second entry on the same ledger, 8b's lesson);
# the five blocks (the three new and the Levite's two); the daemon registered; Q39 the kin standing (DF5's counts) and THE HOLES FILLED (DF4, DF6 — the five names on
# israel_people this sitting's alone; the runner's scans at import).
# THE GREP DECIDED (11b's lesson 1 — ONE grep over the sequence file AND the probes; every seat a COUNT): TWO seats hold the reuse counts ONE — the checkpoint DD2 in
# cold_run_sequence.py (the seven_pn tuple's third and sixth, and blocks_pn 4 -> 5) retyped at patch_seq_literals_ch14.py BEFORE the tape; and the probe Q32 (the w7
# tuple's third and sixth ONE -> TWO, the blocks 4 -> 5) RETYPED HERE — it FAILS beside Q37-Q39 until the tape carries the chapter's lines (35/39 expected on this
# run). Idempotent. patch_probes_ch13.py's form. RUN FROM THE REPO ROOT.
import subprocess, os
ROOT = _ROOT
P = ROOT + '/World/step9/readback_probes.py'
s = open(P, encoding='utf-8').read()
assert 'def q37():' not in s, 'already patched'
def rep(old, new):
    global s
    assert s.count(old) == 1, (s.count(old), old[:90]); s = s.replace(old, new)
# ---- THE RETYPE (the grep decided; a count literal in a PROBE moves like one in a checkpoint — 7b's lesson): Q32's w7 and blocks ----
rep("    return got == (list(OWN), True, 0, 172, [(40, 11, 1)], 0, ((1, 'Deut 12:1'), (1, 'Deut 12:5'), (1, 'Deut 12:5'), (1, 'Deut 12:15'), (1, 'Deut 12:15'), (1, 'Deut 12:15'), (1, 'Deut 12:29')), (3, ['Exod 40:17', 'Lev 9:24', 'Deut 12:5']), 4, True, 'Deut 12:1', 'boot'), 'got (the four own-day lines in the ink\\'s order, all after the tape\\'s last Deuteronomy 11 line",
    "    # THE DEUTERONOMY WALK 12b (2026-09-22): rejoicing_before_the_lord_commanded ONE -> TWO and levite_forsaking_barred ONE -> TWO on israel_people (14:26's and 14:27's second entries on the line second_tithe_declared — THE REUSES; retyped BEFORE the tape, the grep decided; the first entries' sources 12:5's and 12:15's unmoved); the blocks 4 -> 5 (the Levite's second entry a block)\n    return got == (list(OWN), True, 0, 172, [(40, 11, 1)], 0, ((1, 'Deut 12:1'), (1, 'Deut 12:5'), (2, 'Deut 12:5'), (1, 'Deut 12:15'), (1, 'Deut 12:15'), (2, 'Deut 12:15'), (1, 'Deut 12:29')), (3, ['Exod 40:17', 'Lev 9:24', 'Deut 12:5']), 5, True, 'Deut 12:1', 'boot'), 'got (the four own-day lines in the ink\\'s order, all after the tape\\'s last Deuteronomy 11 line")
NEW = '''
# ---- THE DEUTERONOMY WALK 12b (2026-09-22): THE FORMS ON FILE, NO NEW FORM — chapter 14 is the sons and the cuttings (14:1-2), the food law (14:3-20 — the
# beasts, the water, the birds: THE TWIN CHAPTER Leviticus 11 by CALL), the carcass and the kid (14:21), the second tithe with the far place, the money, the
# rejoicing and the Levite (14:22-27) and the third year's tithe (14:28-29): T4 rows graded against the cells that compile their kin by CALL (every row has kin)
# and T1 reference rows against the tape's lines by kind and first verse; EIGHT rows SUPPLIED (four AS LAWS WITH THEIR WRITES — the code's holes compiled at the
# chapter's own day; 14:5 the ten named; 14:11, 14:20 the permission Leviticus lacks; 14:25 the money's first seat) and 14:21 EXPANDED WITH ITS WRITE; no pointer,
# no state row, no stretch, no hole, no open row, no retrograde row; written to FAIL before the runner exists (the design's Q37-Q39) ----
def q37():
    import cold_run_food_tithe as FT
    tbl = FT.DATA['the_readback']; rows = tbl['value']; holes = tbl.get('holes') or []; opens = tbl.get('open_rows') or []
    gs = collections.Counter(r['grade'] for r in rows)
    on_tape = sum(1 for r in rows if r.get('tape_kind') and any(e[2]['kind'] == r['tape_kind'] and WE.first_verse(e[2].get('case_source')) == WE.first_verse(r['tape_verse']) for e in EV))
    by_call = sum(1 for r in rows if r.get('cell') and r.get('cell_found'))
    sup = [r for r in rows if r['grade'] == 'SUPPLIED']; wr = [r for r in rows if r.get('write')]
    ptr = [r for r in rows if r.get('pointer')]
    ok = len(rows) == 29 and on_tape == 10 and by_call == 29 and gs == collections.Counter({'VERBATIM': 6, 'VARIANT': 11, 'EXPANDED': 4, 'SUPPLIED': 8}) and len(holes) == 0 and len(opens) == 0 and not any(r.get('open') for r in rows) and not any(r.get('stretch') for r in rows) and not any(r.get('state') for r in rows) and [r['verses'] for r in sup] == ['Deut 14:1', 'Deut 14:3', 'Deut 14:5', 'Deut 14:11', 'Deut 14:20', 'Deut 14:22', 'Deut 14:25', 'Deut 14:28'] and [(r['verses'], r['write']) for r in wr] == [('Deut 14:1', 'cuttings_for_the_dead_barred'), ('Deut 14:3', 'abomination_eating_barred'), ('Deut 14:21', 'carcass_eating_barred'), ('Deut 14:22', 'second_tithe_owed'), ('Deut 14:28', 'poor_tithe_owed')] and ptr == []
    return ok, 'rows %d (found on the tape %d, in the kin\\'s cells by CALL %d), grades %s, the holes %d, the OPEN rows %d, open-flagged %d, stretch rows %d, state rows %d, the SUPPLIED rows %s, the rows with writes %s, the pointer rows %s' % (len(rows), on_tape, by_call, dict(gs), len(holes), len(opens), sum(1 for r in rows if r.get('open')), sum(1 for r in rows if r.get('stretch')), sum(1 for r in rows if r.get('state')), [r['verses'] for r in sup], [(r['verses'], r['write']) for r in wr], [r['verses'] for r in ptr])
def q38():
    import yaml as _y
    def ENT(*names):
        for n_ in names:
            if n_ in W.entities: return W.entities[n_]
        return None
    def L(ent, eff):
        e_ = ENT(*ent) if isinstance(ent, tuple) else ENT(ent); return [e for e in e_.ledger if e['effect'] == eff] if e_ else []
    OWN = ('sons_and_mourning_declared', 'food_law_declared', 'carcass_and_kid_declared', 'second_tithe_declared', 'third_year_tithe_declared')
    own = [e for e in EV if e[2]['kind'] in OWN]
    idx = {id(l): i for i, l in enumerate(W.log)}
    i_last13 = max([i for i, l in enumerate(W.log) if l[0] == 'EVENT' and str(l[2].get('case_source', '')).startswith('Deut 13:')] or [-1])
    after = bool(own) and all(idx[id(e)] > i_last13 for e in own)
    mk14 = [l for l in W.log if l[0] == 'MARKER' and str(l[2].get('verse', '')).startswith('Deut 14:')]; nm = len([l for l in W.log if l[0] == 'MARKER'])
    days = sorted({ex.date(e[1]) for e in own}); dated = sum(1 for e in own if e[2].get('dated') is not None)
    W5 = [('cuttings_for_the_dead_barred', 'Deut 14:1'), ('abomination_eating_barred', 'Deut 14:3'), ('carcass_eating_barred', 'Deut 14:21'), ('second_tithe_owed', 'Deut 14:22'), ('poor_tithe_owed', 'Deut 14:28')]
    FV = lambda t_: '%s %d:%d' % t_ if isinstance(t_, tuple) else str(t_)   # WE.first_verse returns a (book, chapter, verse) tuple — formatted to the literal's 'Deut 14:1' (10b's Q32 form)
    w5 = tuple((len(L('israel_people', eff)), FV(WE.first_verse(str(L('israel_people', eff)[0].get('case_source', '')))) if L('israel_people', eff) else None) for eff, _ in W5)
    r2 = tuple((len(L('israel_people', eff)), [FV(WE.first_verse(str(e.get('case_source', '')))) for e in L('israel_people', eff)]) for eff in ('rejoicing_before_the_lord_commanded', 'levite_forsaking_barred'))
    blocks = sum(1 for eff in ('cuttings_for_the_dead_barred', 'abomination_eating_barred', 'carcass_eating_barred', 'levite_forsaking_barred') for e in L('israel_people', eff) if e.get('op') == 'block')
    dd = _y.safe_load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'daemon_dispositions.yaml'), encoding='utf-8'))
    d = dd['daemons'].get('law_food_tithe', {})
    got = ([e[2]['kind'] for e in own], after, len(mk14), nm, days, dated, w5, r2, blocks, 'law_food_tithe' in dd['daemons'], d.get('given_at'), d.get('installed_by'))
    return got == (list(OWN), True, 0, 172, [(40, 11, 1)], 0, ((1, 'Deut 14:1'), (1, 'Deut 14:3'), (1, 'Deut 14:21'), (1, 'Deut 14:22'), (1, 'Deut 14:28')), ((2, ['Deut 12:5', 'Deut 14:22']), (2, ['Deut 12:15', 'Deut 14:22'])), 5, True, 'Deut 14:1', 'boot'), 'got (the five own-day lines in the ink\\'s order, all after the tape\\'s last Deuteronomy 13 line, markers at Deut 14 (none), markers, their day, dated fields (none), the five NEW writes on israel_people with their lines\\' first verses (cuttings_for_the_dead_barred, abomination_eating_barred, carcass_eating_barred, second_tithe_owed, poor_tithe_owed), THE TWO REUSES with their entries\\' first verses (rejoicing_before_the_lord_commanded, levite_forsaking_barred — the first entries 12:5\\'s and 12:15\\'s lines, the second the chapter\\'s line second_tithe_declared at 14:22), the five blocks, the daemon registered, given_at, installed_by) = %s' % (got,)
def q39():
    import yaml as _y, cold_run_food_tithe as FT
    def ENT(*names):
        for n_ in names:
            if n_ in W.entities: return W.entities[n_]
        return None
    def L(ent, eff):
        e_ = ENT(*ent) if isinstance(ent, tuple) else ENT(ent); return [e for e in e_.ledger if e['effect'] == eff] if e_ else []
    def n(ent, eff): return len(L(ent, eff))
    def nall(eff): return sum(1 for ent in W.entities.values() for e in ent.ledger if e['effect'] == eff)
    isr = ENT('israel_people')
    open_debits = len([e for e in isr.ledger if e.get('op') == 'debit' and not e.get('closed_by')]) if isr else None
    tv = [e for ent in W.entities.values() for e in ent.ledger if e['effect'] == 'tithe_vowed']
    kin = (nall('treasured_people'), n(('the_levites', 'the-levites'), 'tithe_granted'), n(('the_levites', 'the-levites'), 'inheritance_barred'), nall('tithe_given'), len(tv), bool(tv) and not tv[0].get('closed_by'), n('israel_people', 'holy_things_in_the_gates_barred'), n('israel_people', 'profane_slaughter_permitted'), n('israel_people', 'love_owed'), open_debits)
    OWN5 = ('cuttings_for_the_dead_barred', 'abomination_eating_barred', 'carcass_eating_barred', 'second_tithe_owed', 'poor_tithe_owed')
    holes = sorted({e['effect'] for e in (isr.ledger if isr else []) if any(t in e['effect'] for t in ('cuttings_for', 'abomination_eating', 'carcass_eating', 'second_tithe', 'poor_tithe'))})
    fx = _y.safe_load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'effect_vocabulary.yaml'), encoding='utf-8'))['effects']
    vocab5 = all(k in fx for k in OWN5)
    got = (kin, holes, vocab5, FT.FOOD_SCAN in ([], None), FT.REUSE_SCAN in ([['israel_people'], ['israel_people']], None))
    return got == ((1, 1, 1, 1, 1, True, 1, 1, 1, 10), sorted(OWN5), True, True, True), 'got (THE KIN STANDING (treasured_people anywhere — the heaven entry at Exod 19:5; tithe_granted and inheritance_barred on the Levites; tithe_given anywhere — Abram\\'s transfer; tithe_vowed — count, OPEN (Jacob\\'s debit); holy_things_in_the_gates_barred, profane_slaughter_permitted, love_owed on israel_people; the open debits on israel_people), THE HOLES FILLED (the effects naming the cuttings for the dead, the abomination\\'s eating, the carcass\\'s eating, the second tithe or the poor man\\'s tithe on israel_people — this sitting\\'s five alone), the vocabulary holds the five, the one database scanned EMPTY of the five before this daemon\\'s lines, the two reused effects on israel_people alone before) = %s' % (got,)
'''
a = "\nprint('READBACK PROBES (THE LOOP step 6, the first form)')"
assert s.count(a) == 1
s = s.replace(a, NEW + a)
old = "('Q36 the kin stands; the holes filled; the case\\'s effects off the tape', q36)):"
assert s.count(old) == 1, s.count(old)
s = s.replace(old, "('Q36 the kin stands; the holes filled; the case\\'s effects off the tape', q36), ('Q37 chapter 14\\'s table — the forms on file, no new form', q37), ('Q38 the five own-day lines and their seven writes (two reuses); no marker; the daemon', q38), ('Q39 the kin stands; the holes filled; the scans', q39)):")
old2 = "Run: python3 World/step9/readback_probes.py"
assert s.count(old2) == 1
s = s.replace(old2, "  THE DEUTERONOMY WALK 12b (2026-09-22; DEUTERONOMY_WALK.md \"Sitting 12b\" THE PROBES) — written to FAIL before cold_run_food_tithe.py exists:\n  Q37 chapter 14's table — THE FORMS ON FILE, NO NEW FORM (the sons and the cuttings 14:1-2, the food law 14:3-20 — the twin chapter Leviticus 11 by CALL, the carcass and the kid 14:21, the second tithe with the far place, the money, the rejoicing and the Levite 14:22-27, the third year's tithe 14:28-29): twenty-nine rows predicted from the design, one per verse (VERBATIM 6 / VARIANT 11 / EXPANDED 4 / SUPPLIED 8; ten on the tape by kind and first verse, twenty-nine in the kin's cells by CALL — every row has kin; retyped once from the print if the census moves); EIGHT rows SUPPLIED — 14:1 cuttings_for_the_dead_barred, 14:3 abomination_eating_barred, 14:22 second_tithe_owed, 14:28 poor_tithe_owed AS LAWS WITH THEIR WRITES (the code's holes, each a law's first seat), 14:5 the ten named (Solomon's table the one kin), 14:11 and 14:20 the permission Leviticus lacks (the_birds_signs a parameter), 14:25 the money's first seat (the_moneys_form a parameter); 14:21 EXPANDED WITH ITS WRITE carcass_eating_barred (the ban's seat named by the sanctions engine); no pointer row, no state row, no stretch, no hole, no open row, no retrograde row\n  Q38 the FIVE OWN-DAY lines sons_and_mourning_declared (14:1-2), food_law_declared (14:3-20), carcass_and_kid_declared (14:21), second_tithe_declared (14:22-27) and third_year_tithe_declared (14:28-29) after the tape's last Deuteronomy 13 line on the counter's day (40, 11, 1), no dated field, NO marker at any Deut 14 verse (markers 172 UNMOVED); their SEVEN writes — five NEW on israel_people ONE each (three BLOCKS: cuttings_for_the_dead_barred, abomination_eating_barred, carcass_eating_barred; two STATUSES: second_tithe_owed, poor_tithe_owed) and TWO REUSES TWO each (rejoicing_before_the_lord_commanded — 12:5's line and 14:26's seat on the line second_tithe_declared; levite_forsaking_barred — 12:15's line and 14:27's seat on the same line: a second entry on the same ledger, 8b's lesson); the five blocks; the daemon law_food_tithe registered, given_at Deut 14:1, installed_by boot\n  Q39 the kin stands — treasured_people ONE anywhere (the heaven entry at Exod 19:5), tithe_granted ONE and inheritance_barred ONE on the Levites, tithe_given ONE anywhere (Abram's transfer), tithe_vowed ONE and OPEN (Jacob's debit), holy_things_in_the_gates_barred ONE, profane_slaughter_permitted ONE, love_owed ONE on israel_people, the open debits on israel_people 10 UNMOVED (no debit this chapter); THE HOLES FILLED — the effects naming the cuttings for the dead, the abomination's eating, the carcass's eating, the second tithe or the poor man's tithe on israel_people this sitting's five alone, the vocabulary holding the five; the one database scanned EMPTY of the five before this daemon's lines and the two reused effects on israel_people alone before\n" + old2)
open(P, 'w', encoding='utf-8').write(s)
import py_compile; py_compile.compile(P, doraise=True)
print('patched readback_probes.py: Q37-Q39 added (written to FAIL); Q32 retyped ONE -> TWO for the two reuses and the blocks 4 -> 5 (the grep decided: two count seats — DD2 in the sequence file, Q32 in the probes); compiles')
