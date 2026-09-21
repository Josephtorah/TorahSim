import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE DEUTERONOMY WALK 10b (2026-09-21): readback_probes.py Q31-Q33 written to FAIL before cold_run_place_name.py exists (the design's THE PROBES
# paragraph — RUN B's FIRST step, before the types: 7b's lesson 2; Q28-Q30's form). Q31 the runner and its the_readback table — THE FORMS ON FILE, NO NEW
# FORM: thirty-one rows predicted from the design (one per verse; VERBATIM 6 / VARIANT 16 / EXPANDED 3 / SUPPLIED 6; eleven on the tape by kind and first
# verse, fourteen in the kin's cells by CALL; the state row 12:9 SUPPLIED with NO write (chapter 8's fifth form); the five law rows 12:4, 12:7, 12:17, 12:19,
# 12:30 SUPPLIED WITH THEIR WRITES (the code's holes — a law's first seat); the pointer row 12:20; no hole, no open row, no stretch, no retrograde row) —
# retyped ONCE from the runner's print if the census moves (4b's lesson); Q32 the FOUR OWN-DAY lines demolition_restated (12:1-4), place_chosen_declared
# (12:5-14), profane_slaughter_permitted (12:15-28) and nations_cut_off_warned (12:29-31) after the tape's last Deuteronomy 11 line, on the counter's day
# (40, 11, 1), no dated field, NO marker at any Deut 12 verse, markers 172 UNMOVED; their EIGHT writes — seven on israel_people ONE each (name_erasure_barred,
# holy_things_in_the_gates_barred, levite_forsaking_barred, foreign_rite_inquiry_barred BLOCKS; place_chosen_required, rejoicing_before_the_lord_commanded,
# profane_slaughter_permitted STATUSES) and high_places_banned TWO on the-land (the erection's at Exod 40:17 and the chapter's REUSE at the line
# place_chosen_declared, Deut 12:5 — 8b's lesson: a reused effect is a second entry on the same ledger); the daemon registered; Q33 the kin standing (DD5-DD6's
# counts) and THE HOLES FILLED (DD4 — the seven names on israel_people this sitting's alone; the eras table's six rows read by CALL, unmoved). THE GREP DECIDED:
# no literal counts high_places_banned ONE — Q18 (readback_probes.py) and CQ5 (cold_run_sequence.py) hold BOOLEANS (present / any) — NO RETYPE (the design
# predicted five seats; the grep found two, both booleans). Idempotent. patch_probes_ch11.py's form. RUN FROM THE REPO ROOT.
import subprocess, os
ROOT = _ROOT
P = ROOT + '/World/step9/readback_probes.py'
s = open(P, encoding='utf-8').read()
assert 'def q31():' not in s, 'already patched'
NEW = '''
# ---- THE DEUTERONOMY WALK 10b (2026-09-21): THE FORMS ON FILE, NO NEW FORM — chapter 12 is the header and the demolition (12:1-4), the place chosen (12:5-12), the
# burnt offerings only there (12:13-14), the profane slaughter, the blood and the gates (12:15-19), the border enlarged and the altar (12:20-28), the nations cut off
# and the abomination (12:29-31): T1 reference rows against the tape's lines by kind and first verse or the kin's cells by CALL; T5 the state row 12:9 SUPPLIED with
# NO write (chapter 8's form); T4 the laws' form with THE CODE'S FOUR HOLES compiled at the chapter's own day (the Name's erasure, the place's law with the rejoicing
# and the reuse of high_places_banned, the profane slaughter's release with the gates' bar and the Levite, the inquiry after the gods) — five law rows SUPPLIED WITH
# THEIR WRITES; the pointer 12:20; written to FAIL before the runner exists (the design's Q31-Q33) ----
def q31():
    import cold_run_place_name as PN
    tbl = PN.DATA['the_readback']; rows = tbl['value']; holes = tbl.get('holes') or []; opens = tbl.get('open_rows') or []
    gs = collections.Counter(r['grade'] for r in rows)
    on_tape = sum(1 for r in rows if r.get('tape_kind') and any(e[2]['kind'] == r['tape_kind'] and WE.first_verse(e[2].get('case_source')) == WE.first_verse(r['tape_verse']) for e in EV))
    by_call = sum(1 for r in rows if r.get('cell') and r.get('cell_found'))
    sup = [r for r in rows if r['grade'] == 'SUPPLIED']
    ptr = [r for r in rows if r.get('pointer')]
    ok = len(rows) == 31 and on_tape + by_call == 25 and gs == collections.Counter({'VERBATIM': 6, 'VARIANT': 16, 'EXPANDED': 3, 'SUPPLIED': 6}) and len(holes) == 0 and len(opens) == 0 and not any(r.get('open') for r in rows) and not any(r.get('stretch') for r in rows) and len(sup) == 6 and [r['verses'] for r in sup] == ['Deut 12:4', 'Deut 12:7', 'Deut 12:9', 'Deut 12:17', 'Deut 12:19', 'Deut 12:30'] and [r.get('write') for r in sup] == ['name_erasure_barred', 'rejoicing_before_the_lord_commanded', None, 'holy_things_in_the_gates_barred', 'levite_forsaking_barred', 'foreign_rite_inquiry_barred'] and [bool(r.get('state')) for r in sup] == [False, False, True, False, False, False] and [r['verses'] for r in ptr] == ['Deut 12:20']
    return ok, 'rows %d (found on the tape %d, in the kin\\'s cells by CALL %d), grades %s, the holes %d, the OPEN rows %d, open-flagged %d, stretch rows %d, the SUPPLIED rows %s with their writes %s (the state rows %s), the pointer rows %s' % (len(rows), on_tape, by_call, dict(gs), len(holes), len(opens), sum(1 for r in rows if r.get('open')), sum(1 for r in rows if r.get('stretch')), [r['verses'] for r in sup], [r.get('write') for r in sup], [bool(r.get('state')) for r in sup], [r['verses'] for r in ptr])
def q32():
    import yaml as _y
    def ENT(*names):
        for n_ in names:
            if n_ in W.entities: return W.entities[n_]
        return None
    def L(ent, eff):
        e_ = ENT(*ent) if isinstance(ent, tuple) else ENT(ent); return [e for e in e_.ledger if e['effect'] == eff] if e_ else []
    OWN = ('demolition_restated', 'place_chosen_declared', 'profane_slaughter_permitted', 'nations_cut_off_warned')
    own = [e for e in EV if e[2]['kind'] in OWN]
    idx = {id(l): i for i, l in enumerate(W.log)}
    i_last11 = max([i for i, l in enumerate(W.log) if l[0] == 'EVENT' and str(l[2].get('case_source', '')).startswith('Deut 11:')] or [-1])
    after = bool(own) and all(idx[id(e)] > i_last11 for e in own)
    mk12 = [l for l in W.log if l[0] == 'MARKER' and str(l[2].get('verse', '')).startswith('Deut 12:')]; nm = len([l for l in W.log if l[0] == 'MARKER'])
    days = sorted({ex.date(e[1]) for e in own}); dated = sum(1 for e in own if e[2].get('dated') is not None)
    W7 = [('name_erasure_barred', 'Deut 12:1'), ('place_chosen_required', 'Deut 12:5'), ('rejoicing_before_the_lord_commanded', 'Deut 12:5'), ('profane_slaughter_permitted', 'Deut 12:15'), ('holy_things_in_the_gates_barred', 'Deut 12:15'), ('levite_forsaking_barred', 'Deut 12:15'), ('foreign_rite_inquiry_barred', 'Deut 12:29')]
    w7 = tuple((len(L('israel_people', eff)), WE.first_verse(str(L('israel_people', eff)[0].get('case_source', ''))) if L('israel_people', eff) else None) for eff, _ in W7)
    hp = L(('the-land', 'the_land'), 'high_places_banned'); hp_src = [WE.first_verse(str(e.get('case_source', ''))) for e in hp]
    blocks = sum(1 for eff in ('name_erasure_barred', 'holy_things_in_the_gates_barred', 'levite_forsaking_barred', 'foreign_rite_inquiry_barred') for e in L('israel_people', eff) if e.get('op') == 'block')
    dd = _y.safe_load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'daemon_dispositions.yaml'), encoding='utf-8'))
    d = dd['daemons'].get('law_place_name', {})
    got = ([e[2]['kind'] for e in own], after, len(mk12), nm, days, dated, w7, (len(hp), hp_src), blocks, 'law_place_name' in dd['daemons'], d.get('given_at'), d.get('installed_by'))
    return got == (list(OWN), True, 0, 172, [(40, 11, 1)], 0, ((1, 'Deut 12:1'), (1, 'Deut 12:5'), (1, 'Deut 12:5'), (1, 'Deut 12:15'), (1, 'Deut 12:15'), (1, 'Deut 12:15'), (1, 'Deut 12:29')), (2, ['Exod 40:17', 'Deut 12:5']), 4, True, 'Deut 12:1', 'boot'), 'got (the four own-day lines in the ink\\'s order, all after the tape\\'s last Deuteronomy 11 line, markers at Deut 12 (none), markers, their day, dated fields (none), the seven writes on israel_people with their lines\\' first verses (name_erasure_barred, place_chosen_required, rejoicing_before_the_lord_commanded, profane_slaughter_permitted, holy_things_in_the_gates_barred, levite_forsaking_barred, foreign_rite_inquiry_barred), high_places_banned on the-land (count, the entries\\' first verses — the erection\\'s and the chapter\\'s REUSE), the four blocks, the daemon registered, given_at, installed_by) = %s' % (got,)
def q33():
    import yaml as _y, cold_run_place_name as PN
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
    kin = (n('israel_people', 'house_abomination_barred'), nall('molten_image_barred'), n(('the_levites', 'the-levites'), 'tithe_granted'), n(('the_levites', 'the-levites'), 'inheritance_barred'), n('israel_people', 'shema_commanded'), n('israel_people', 'blessing_and_curse_set'), len([e for e in EV if e[2]['kind'] == 'limb_barred']), len(ban), bool(ban) and not ban[0].get('closed_by'), open_debits)
    OWN7 = ('name_erasure_barred', 'place_chosen_required', 'rejoicing_before_the_lord_commanded', 'profane_slaughter_permitted', 'holy_things_in_the_gates_barred', 'levite_forsaking_barred', 'foreign_rite_inquiry_barred')
    holes = sorted({e['effect'] for e in (isr.ledger if isr else []) if any(t in e['effect'] for t in ('place_chosen', 'rejoicing_before', 'profane_slaughter', 'in_the_gates', 'levite_forsaking', 'name_erasure', 'foreign_rite'))})
    fx = _y.safe_load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'effect_vocabulary.yaml'), encoding='utf-8'))['effects']
    vocab7 = all(k in fx for k in OWN7)
    eras = PN.DATA['the_eras_table_unmoved']['value']
    got = (kin, holes, vocab7, eras.get('n_rows'), eras.get('the_platform_agrees'), eras.get('the_journeys_agree'), PN.PLACE_SCAN in ([], None), PN.HPB_SCAN in (['the-land'], None))
    return got == ((1, 1, 1, 1, 1, 1, 1, 1, True, 10), sorted(OWN7), True, 6, True, True, True, True), 'got (THE KIN STANDING (house_abomination_barred on israel_people, molten_image_barred anywhere, tithe_granted and inheritance_barred on the Levites, shema_commanded, blessing_and_curse_set on israel_people; limb_barred\\'s line; the ban\\'s debit — count, OPEN; the open debits on israel_people), THE HOLES FILLED (the effects naming the place, the rejoicing, the profane slaughter, the gates, the Levite, the Name\\'s erasure or the inquiry on israel_people — this sitting\\'s seven alone), the vocabulary holds the seven, THE ERAS TABLE UNMOVED (six rows by CALL; the platform and the journeys agreeing), the one database scanned EMPTY of the seven before this daemon\\'s lines, high_places_banned on the-land alone before) = %s' % (got,)
'''
a = "\nprint('READBACK PROBES (THE LOOP step 6, the first form)')"
assert s.count(a) == 1
s = s.replace(a, NEW + a)
old = "('Q30 the kin stands; the rain\\'s hole filled', q30)):"
assert s.count(old) == 1, s.count(old)
s = s.replace(old, "('Q30 the kin stands; the rain\\'s hole filled', q30), ('Q31 chapter 12\\'s table — the forms on file, no new form', q31), ('Q32 the four own-day lines and their eight writes (the reuse); no marker; the daemon', q32), ('Q33 the kin stands; the holes filled; the eras table unmoved', q33)):")
old2 = "Run: python3 World/step9/readback_probes.py"
assert s.count(old2) == 1
s = s.replace(old2, "  THE DEUTERONOMY WALK 10b (2026-09-21; DEUTERONOMY_WALK.md \"Sitting 10b\" THE PROBES) — written to FAIL before cold_run_place_name.py exists:\n  Q31 chapter 12's table — THE FORMS ON FILE, NO NEW FORM (the header and the demolition 12:1-4, the place chosen 12:5-12, the burnt offerings only there 12:13-14, the profane slaughter, the blood and the gates 12:15-19, the border enlarged and the altar 12:20-28, the nations cut off and the abomination 12:29-31): thirty-one rows predicted from the design, one per verse (VERBATIM 6 / VARIANT 16 / EXPANDED 3 / SUPPLIED 6; eleven on the tape by kind and first verse, fourteen in the kin's cells by CALL — retyped once from the print if the census moves); the state row 12:9 SUPPLIED with NO write (chapter 8's fifth form); FIVE LAW ROWS SUPPLIED WITH THEIR WRITES — 12:4 name_erasure_barred, 12:7 rejoicing_before_the_lord_commanded, 12:17 holy_things_in_the_gates_barred, 12:19 levite_forsaking_barred, 12:30 foreign_rite_inquiry_barred (the code's holes, each a law's first seat); the pointer row 12:20 (Exodus 34:24's 'I will enlarge your border' by two teachers on the callee — the Sifrei 75:2); no hole, no open row, no stretch, no retrograde row\n  Q32 the FOUR OWN-DAY lines demolition_restated (12:1-4), place_chosen_declared (12:5-14), profane_slaughter_permitted (12:15-28) and nations_cut_off_warned (12:29-31) after the tape's last Deuteronomy 11 line on the counter's day (40, 11, 1), no dated field, NO marker at any Deut 12 verse (markers 172 UNMOVED); their EIGHT writes — seven on israel_people ONE each (four BLOCKS: name_erasure_barred, holy_things_in_the_gates_barred, levite_forsaking_barred, foreign_rite_inquiry_barred; three STATUSES: place_chosen_required, rejoicing_before_the_lord_commanded, profane_slaughter_permitted — the last conditional on the entry) and high_places_banned TWO on the-land (the erection's entry at Exod 40:17 and the chapter's REUSE at place_chosen_declared, Deut 12:5 — a second entry on the same ledger, 8b's lesson); the daemon law_place_name registered, given_at Deut 12:1, installed_by boot\n  Q33 the kin stands — house_abomination_barred ONE on israel_people, molten_image_barred ONE, tithe_granted ONE and inheritance_barred ONE on the Levites, shema_commanded ONE, blessing_and_curse_set ONE, limb_barred's line ONE, the ban's debit ONE and OPEN, the open debits on israel_people 10 UNMOVED (no second demolition debit); THE HOLES FILLED — the effects naming the place, the rejoicing, the profane slaughter, the gates, the Levite, the Name's erasure or the inquiry on israel_people this sitting's seven alone, the vocabulary holding them; THE ERAS TABLE UNMOVED — shemini_day.eras('table') six rows by CALL, sanctions.platform('eras') and journeys.the_command('private_altar_eras') agreeing; the one database scanned EMPTY of the seven before this daemon's lines and high_places_banned on the-land alone\n" + old2)
open(P, 'w', encoding='utf-8').write(s)
import py_compile; py_compile.compile(P, doraise=True)
print('patched readback_probes.py: Q31-Q33 added (written to FAIL); compiles')
