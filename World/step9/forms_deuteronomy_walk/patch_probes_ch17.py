import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE DEUTERONOMY WALK 15b (2026-09-24): readback_probes.py Q44 written to FAIL before cold_run_courts_prophet.py exists (the design's THE PROBES paragraph — the
# FIRST step, before the types: 7b's lesson 2; ONE probe in the lean form): the EIGHT OWN-DAY lines after the tape's last Deuteronomy 16 line on the counter's day
# (40, 11, 1), no dated field, NO marker at any Deut 17 or 18 verse (markers 172 UNMOVED); their writes — the thirty-seven NEW ONE each on israel_people with their
# lines' first verses; the twenty blocks; the two heaven entries; the daemon registered; the readback's forty-two rows one per verse in order, no pointer, no state, no
# open, no stretch row. Idempotent. patch_probes_ch16.py's form. RUN FROM THE REPO ROOT.
import subprocess, os
ROOT = _ROOT
P = ROOT + '/World/step9/readback_probes.py'
s = open(P, encoding='utf-8').read()
assert 'def q44():' not in s, 'already patched'
def rep(old, new):
    global s
    assert s.count(old) == 1, (s.count(old), old[:90]); s = s.replace(old, new)
W = 'THE DEUTERONOMY WALK 15b (2026-09-24)'
Q44 = '''
def q44():
    import yaml as _y, cold_run_courts_prophet as CP
    def ENT(*names):
        for n_ in names:
            if n_ in W.entities: return W.entities[n_]
        return None
    def L(ent, eff):
        e_ = ENT(*ent) if isinstance(ent, tuple) else ENT(ent); return [e for e in e_.ledger if e['effect'] == eff] if e_ else []
    def nall(eff): return sum(1 for ent in W.entities.values() for e in ent.ledger if e['effect'] == eff)
    OWN = ('blemished_sacrifice_barred', 'idolater_trial_declared', 'high_court_declared', 'king_law_declared', 'priests_dues_declared', 'levite_at_the_place_declared', 'diviners_barred', 'prophet_law_declared')
    own = [e for e in EV if e[2]['kind'] in OWN]
    idx = {id(l): i for i, l in enumerate(W.log)}
    i_last16 = max([i for i, l in enumerate(W.log) if l[0] == 'EVENT' and str(l[2].get('case_source', '')).startswith('Deut 16:')] or [-1])
    after = bool(own) and all(idx[id(e)] > i_last16 for e in own)
    mk17 = [l for l in W.log if l[0] == 'MARKER' and str(l[2].get('verse', '')).startswith(('Deut 17:', 'Deut 18:'))]; nm = len([l for l in W.log if l[0] == 'MARKER'])
    days = sorted({ex.date(e[1]) for e in own}); dated = sum(1 for e in own if e[2].get('dated') is not None)
    W37 = [('blemished_offering_barred', 'Deut 17:1'), ('idolater_inquiry_required', 'Deut 17:2'), ('two_witnesses_required', 'Deut 17:2'), ('one_witness_barred', 'Deut 17:2'), ('witnesses_hand_first_commanded', 'Deut 17:2'), ('high_court_at_the_place_commanded', 'Deut 17:8'), ('sentence_binding_commanded', 'Deut 17:8'), ('turning_from_the_word_barred', 'Deut 17:8'), ('king_from_the_brothers_commanded', 'Deut 17:14'), ('foreign_king_barred', 'Deut 17:14'), ('horses_multiplying_barred', 'Deut 17:14'), ('return_to_egypt_barred', 'Deut 17:14'), ('wives_multiplying_barred', 'Deut 17:14'), ('silver_and_gold_multiplying_barred', 'Deut 17:14'), ('law_copy_commanded', 'Deut 17:14'), ('heart_lifting_barred', 'Deut 17:14'), ('shoulder_cheeks_maw_owed', 'Deut 18:1'), ('first_fleece_owed', 'Deut 18:1'), ('priests_standing_chosen', 'Deut 18:1'), ('levite_service_at_the_place_permitted', 'Deut 18:6'), ('equal_portions_commanded', 'Deut 18:6'), ('abominations_learning_barred', 'Deut 18:9'), ('passing_through_fire_barred', 'Deut 18:9'), ('diviner_barred', 'Deut 18:9'), ('soothsayer_barred', 'Deut 18:9'), ('augur_barred', 'Deut 18:9'), ('sorcerer_barred', 'Deut 18:9'), ('charmer_barred', 'Deut 18:9'), ('ghost_consulting_barred', 'Deut 18:9'), ('familiar_spirit_barred', 'Deut 18:9'), ('necromancer_barred', 'Deut 18:9'), ('wholeness_commanded', 'Deut 18:9'), ('prophet_like_moses_promised', 'Deut 18:15'), ('prophet_hearkening_commanded', 'Deut 18:15'), ('word_required_of_the_hearer', 'Deut 18:15'), ('false_word_test_declared', 'Deut 18:15'), ('false_prophet_fear_barred', 'Deut 18:15')]
    BLOCKS = ('blemished_offering_barred', 'one_witness_barred', 'turning_from_the_word_barred', 'foreign_king_barred', 'horses_multiplying_barred', 'return_to_egypt_barred', 'wives_multiplying_barred', 'silver_and_gold_multiplying_barred', 'heart_lifting_barred', 'abominations_learning_barred', 'passing_through_fire_barred', 'diviner_barred', 'soothsayer_barred', 'augur_barred', 'sorcerer_barred', 'charmer_barred', 'ghost_consulting_barred', 'familiar_spirit_barred', 'necromancer_barred', 'false_prophet_fear_barred')
    FV = lambda t_: '%s %d:%d' % t_ if isinstance(t_, tuple) else str(t_)   # WE.first_verse returns a (book, chapter, verse) tuple — formatted to the literal's 'Deut 17:1' (10b's Q32 form)
    w37 = tuple((len(L('israel_people', eff)), FV(WE.first_verse(str(L('israel_people', eff)[0].get('case_source', '')))) if L('israel_people', eff) else None) for eff, _ in W37)
    blocks = sum(1 for eff in BLOCKS for e in L('israel_people', eff) if e.get('op') == 'block')
    heaven = sum(1 for eff in ('prophet_like_moses_promised', 'word_required_of_the_hearer') for e in L('israel_people', eff) if e.get('op') == 'heaven')
    kin = (nall('israel_hears_and_fears'), nall('false_prophet_hearing_barred'), nall('inheritance_barred'), nall('kings_promised'), nall('prophet_declared'), nall('wholeness_owed'), nall('courts_established'), nall('judges_charged'), nall('bribe_barred'), nall('stoned'), nall('put_to_death'), nall('evil_purged_from_the_midst'))
    rows = CP.DATA['the_readback']['value']
    rb = (len(rows), [r['verses'] for r in rows] == ['Deut 17:%d' % v for v in range(1, 21)] + ['Deut 18:%d' % v for v in range(1, 23)], any(r.get('pointer') for r in rows), any(r.get('state') for r in rows), any(r.get('open') for r in rows), any(r.get('stretch') for r in rows))
    dd = _y.safe_load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'daemon_dispositions.yaml'), encoding='utf-8'))
    d = dd['daemons'].get('law_courts_prophet', {})
    got = ([e[2]['kind'] for e in own], after, len(mk17), nm, days, dated, w37, blocks, heaven, kin, rb, 'law_courts_prophet' in dd['daemons'], d.get('given_at'), d.get('installed_by'))
    return got == (list(OWN), True, 0, 172, [(40, 11, 1)], 0, tuple((1, v_) for _, v_ in W37), 20, 2, (1, 1, 2, 1, 1, 1, 1, 1, 1, 2, 7, 0), (42, True, False, False, False, False), True, 'Deut 17:1', 'boot'), 'got (the eight own-day lines in the ink\\'s order, all after the tape\\'s last Deuteronomy 16 line, markers at Deut 17-18 (none), markers, their day, dated fields (none), the thirty-seven NEW writes on israel_people with their lines\\' first verses, the twenty blocks, the two heaven entries, the kin\\'s counts unmoved (hears-and-fears, false prophet, inheritance, kings, prophet, wholeness, courts, judges, bribe, stoned, put to death, purged — as the recon read them), the readback (rows, one per verse in order, pointer, state, open, stretch), the daemon registered, given_at, installed_by) = %s' % (got,)
'''
rep("\nprint('READBACK PROBES (THE LOOP step 6, the first form)')", Q44 + "\nprint('READBACK PROBES (THE LOOP step 6, the first form)')")
rep("('Q43 chapter 16\\'s five own-day lines, their sixteen writes (the bribe\\'s first), the nine blocks, the readback\\'s twenty-two rows, the daemon — LEAN', q43)", "('Q43 chapter 16\\'s five own-day lines, their sixteen writes (the bribe\\'s first), the nine blocks, the readback\\'s twenty-two rows, the daemon — LEAN', q43), ('Q44 chapters 17-18\\'s eight own-day lines, their thirty-seven writes, the twenty blocks and the two heaven entries, the kin unmoved, the readback\\'s forty-two rows, the daemon — LEAN', q44)")
rep('  THE DEUTERONOMY WALK 14b (2026-09-23) (DEUTERONOMY_WALK.md "Sitting 14b" THE PROBES; THE LEAN PASS)', "  %s (DEUTERONOMY_WALK.md \"Sitting 15b\" THE PROBES; THE LEAN PASS) — written to FAIL before cold_run_courts_prophet.py exists: Q44 the EIGHT OWN-DAY lines blemished_sacrifice_barred (17:1), idolater_trial_declared (17:2-7), high_court_declared (17:8-13), king_law_declared (17:14-20), priests_dues_declared (18:1-5), levite_at_the_place_declared (18:6-8), diviners_barred (18:9-14) and prophet_law_declared (18:15-22) after the tape's last Deuteronomy 16 line on the counter's day (40, 11, 1), no dated field, NO marker at any Deut 17 or 18 verse (markers 172 UNMOVED); their writes — the thirty-seven NEW ONE each on israel_people (fifteen STATUSES, twenty BLOCKS, two HEAVEN entries); the kin's counts UNMOVED (no second write of hears-and-fears, the false prophet's block, the inheritance, the kings promised, the prophet declared, the wholeness owed, the courts, the judges, the bribe; stoned 2, put to death 7, purged 0 — the references); the readback's forty-two rows one per verse in order with no pointer, state, open or stretch row; the daemon law_courts_prophet registered, given_at Deut 17:1, installed_by boot (ONE probe — the lean form)\n  THE DEUTERONOMY WALK 14b (2026-09-23) (DEUTERONOMY_WALK.md \"Sitting 14b\" THE PROBES; THE LEAN PASS)" % W)
open(P, 'w', encoding='utf-8').write(s)
import py_compile; py_compile.compile(P, doraise=True)
print('patched: Q44 written (to FAIL until the runner and the tape carry chapters 17-18); the file compiles')
