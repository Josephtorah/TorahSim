import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE DEUTERONOMY WALK 16b (2026-09-25): readback_probes.py Q45 written to FAIL before cold_run_refuge_war_family.py exists (the design's THE PROBES paragraph — the
# FIRST step after the design: 7b's lesson 2; ONE probe in the lean form): the THIRTEEN OWN-DAY lines after the tape's last Deuteronomy 18 line on the counter's day
# (40, 11, 1), no dated field, NO marker at any Deut 19, 20 or 21 verse (markers 172 UNMOVED); their writes — the forty-five NEW ONE each on israel_people with their
# lines' first verses; the ten blocks; the one heaven entry; the daemon registered; the readback's sixty-four rows one per verse in order, no pointer, no state, no
# open, no stretch row. Idempotent. patch_probes_ch17.py's form. RUN FROM THE REPO ROOT.
import subprocess, os
ROOT = _ROOT
P = ROOT + '/World/step9/readback_probes.py'
s = open(P, encoding='utf-8').read()
assert 'def q45():' not in s, 'already patched'
def rep(old, new):
    global s
    assert s.count(old) == 1, (s.count(old), old[:90]); s = s.replace(old, new)
W = 'THE DEUTERONOMY WALK 16b (2026-09-25)'
Q45 = '''
def q45():
    import yaml as _y, cold_run_refuge_war_family as RW
    def ENT(*names):
        for n_ in names:
            if n_ in W.entities: return W.entities[n_]
        return None
    def L(ent, eff):
        e_ = ENT(*ent) if isinstance(ent, tuple) else ENT(ent); return [e for e in e_.ledger if e['effect'] == eff] if e_ else []
    def nall(eff): return sum(1 for ent in W.entities.values() for e in ent.ledger if e['effect'] == eff)
    OWN = ('refuge_cities_declared', 'manslayer_and_murderer_declared', 'landmark_declared', 'witnesses_law_declared', 'war_speech_declared', 'siege_law_declared', 'seven_nations_herem_declared', 'siege_trees_declared', 'heifer_rite_declared', 'captive_wife_declared', 'firstborn_portion_declared', 'rebellious_son_declared', 'hanged_burial_declared')
    own = [e for e in EV if e[2]['kind'] in OWN]
    idx = {id(l): i for i, l in enumerate(W.log)}
    i_last18 = max([i for i, l in enumerate(W.log) if l[0] == 'EVENT' and str(l[2].get('case_source', '')).startswith('Deut 18:')] or [-1])
    after = bool(own) and all(idx[id(e)] > i_last18 for e in own)
    mk19 = [l for l in W.log if l[0] == 'MARKER' and str(l[2].get('verse', '')).startswith(('Deut 19:', 'Deut 20:', 'Deut 21:'))]; nm = len([l for l in W.log if l[0] == 'MARKER'])
    days = sorted({ex.date(e[1]) for e in own}); dated = sum(1 for e in own if e[2].get('dated') is not None)
    W45 = [('three_cities_separated_commanded', 'Deut 19:1'), ('way_prepared_commanded', 'Deut 19:1'), ('land_divided_in_three_commanded', 'Deut 19:1'), ('three_more_cities_conditioned', 'Deut 19:1'), ('manslayer_flight_permitted', 'Deut 19:4'), ('murderer_extradition_commanded', 'Deut 19:4'), ('murderer_pity_barred', 'Deut 19:4'), ('innocent_blood_purge_commanded', 'Deut 19:4'), ('landmark_removal_barred', 'Deut 19:14'), ('two_or_three_witnesses_required', 'Deut 19:15'), ('witnesses_inquiry_commanded', 'Deut 19:15'), ('plotting_witness_talion_commanded', 'Deut 19:15'), ('talion_pity_barred', 'Deut 19:15'), ('war_fear_barred', 'Deut 20:1'), ('priest_war_speech_commanded', 'Deut 20:1'), ('officers_exemptions_commanded', 'Deut 20:1'), ('fearful_exemption_commanded', 'Deut 20:1'), ('captains_appointed_commanded', 'Deut 20:1'), ('peace_call_commanded', 'Deut 20:10'), ('tribute_service_commanded', 'Deut 20:10'), ('siege_males_smitten_commanded', 'Deut 20:10'), ('spoil_permitted', 'Deut 20:10'), ('far_cities_scope_declared', 'Deut 20:10'), ('nothing_alive_left_commanded', 'Deut 20:16'), ('abominations_teaching_barred', 'Deut 20:16'), ('fruit_tree_cutting_barred', 'Deut 20:19'), ('siege_works_permitted', 'Deut 20:19'), ('slain_found_measuring_commanded', 'Deut 21:1'), ('heifer_neck_broken_commanded', 'Deut 21:1'), ('priests_approach_commanded', 'Deut 21:1'), ('elders_hands_washed_commanded', 'Deut 21:1'), ('elders_declaration_commanded', 'Deut 21:1'), ('innocent_blood_atoned', 'Deut 21:1'), ('captive_wife_permitted', 'Deut 21:10'), ('captive_mourning_month_commanded', 'Deut 21:10'), ('captive_sale_barred', 'Deut 21:10'), ('captive_release_commanded', 'Deut 21:10'), ('firstborn_double_portion_commanded', 'Deut 21:15'), ('firstborn_right_transfer_barred', 'Deut 21:15'), ('rebellious_son_seized_commanded', 'Deut 21:18'), ('rebellious_son_stoning_commanded', 'Deut 21:18'), ('hanging_after_death_commanded', 'Deut 21:22'), ('corpse_overnight_barred', 'Deut 21:22'), ('same_day_burial_commanded', 'Deut 21:22'), ('land_defilement_barred', 'Deut 21:22')]
    BLOCKS = ('murderer_pity_barred', 'landmark_removal_barred', 'talion_pity_barred', 'war_fear_barred', 'abominations_teaching_barred', 'fruit_tree_cutting_barred', 'captive_sale_barred', 'firstborn_right_transfer_barred', 'corpse_overnight_barred', 'land_defilement_barred')
    FV = lambda t_: '%s %d:%d' % t_ if isinstance(t_, tuple) else str(t_)   # WE.first_verse returns a (book, chapter, verse) tuple — formatted to the literal's 'Deut 19:1' (10b's Q32 form)
    w45 = tuple((len(L('israel_people', eff)), FV(WE.first_verse(str(L('israel_people', eff)[0].get('case_source', '')))) if L('israel_people', eff) else None) for eff, _ in W45)
    blocks = sum(1 for eff in BLOCKS for e in L('israel_people', eff) if e.get('op') == 'block')
    heaven = sum(1 for e in L('israel_people', 'innocent_blood_atoned') if e.get('op') == 'heaven')
    kin = (nall('cities_set_apart'), nall('pity_barred'), nall('israel_hears_and_fears'), nall('one_witness_barred'), nall('two_witnesses_required'), nall('witnesses_hand_first_commanded'), nall('abominations_learning_barred'), nall('fear_not_promised'), nall('taken_captive'), nall('spoil_taken'), nall('boundary_witnessed'), nall('hanged'), nall('buried'), nall('atoned_forgiven'), nall('blood_required'), nall('firstborn_by_the_head'), nall('hated'), nall('stoned'), nall('put_to_death'), nall('evil_purged_from_the_midst'))
    rows = RW.DATA['the_readback']['value']
    rb = (len(rows), [r['verses'] for r in rows] == ['Deut 19:%d' % v for v in range(1, 22)] + ['Deut 20:%d' % v for v in range(1, 21)] + ['Deut 21:%d' % v for v in range(1, 24)], any(r.get('pointer') for r in rows), any(r.get('state') for r in rows), any(r.get('open') for r in rows), any(r.get('stretch') for r in rows))
    dd = _y.safe_load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'daemon_dispositions.yaml'), encoding='utf-8'))
    d = dd['daemons'].get('law_refuge_war_family', {})
    got = ([e[2]['kind'] for e in own], after, len(mk19), nm, days, dated, w45, blocks, heaven, kin, rb, 'law_refuge_war_family' in dd['daemons'], d.get('given_at'), d.get('installed_by'))
    return got == (list(OWN), True, 0, 172, [(40, 11, 1)], 0, tuple((1, v_) for _, v_ in W45), 10, 1, (1, 2, 1, 1, 1, 1, 1, 4, 3, 2, 1, 1, 9, 7, 1, 2, 3, 2, 7, 0), (64, True, False, False, False, False), True, 'Deut 19:1', 'boot'), 'got (the thirteen own-day lines in the ink\\'s order, all after the tape\\'s last Deuteronomy 18 line, markers at Deut 19-21 (none), markers, their day, dated fields (none), the forty-five NEW writes on israel_people with their lines\\' first verses, the ten blocks, the one heaven entry, the kin\\'s counts unmoved (the cities set apart, pity, hears-and-fears, one witness, two witnesses, the witnesses\\' hand, the learning, fear not, captive, spoil, the boundary, hanged, buried, atoned, blood required, the firstborn by the head, hated, stoned, put to death, purged — as the recon read them), the readback (rows, one per verse in order, pointer, state, open, stretch), the daemon registered, given_at, installed_by) = %s' % (got,)
'''
rep("\nprint('READBACK PROBES (THE LOOP step 6, the first form)')", Q45 + "\nprint('READBACK PROBES (THE LOOP step 6, the first form)')")
rep("the readback\\'s forty-two rows, the daemon — LEAN', q44)", "the readback\\'s forty-two rows, the daemon — LEAN', q44), ('Q45 chapters 19-21\\'s thirteen own-day lines, their forty-five writes, the ten blocks and the one heaven entry, the kin unmoved, the readback\\'s sixty-four rows, the daemon — LEAN', q45)")
rep('  THE DEUTERONOMY WALK 15b (2026-09-24) (DEUTERONOMY_WALK.md "Sitting 15b" THE PROBES; THE LEAN PASS)', "  %s (DEUTERONOMY_WALK.md \"Sitting 16b\" THE PROBES; THE LEAN PASS) — written to FAIL before cold_run_refuge_war_family.py exists: Q45 the THIRTEEN OWN-DAY lines refuge_cities_declared (19:1-3, 7-10), manslayer_and_murderer_declared (19:4-6, 11-13), landmark_declared (19:14), witnesses_law_declared (19:15-21), war_speech_declared (20:1-9), siege_law_declared (20:10-15), seven_nations_herem_declared (20:16-18), siege_trees_declared (20:19-20), heifer_rite_declared (21:1-9), captive_wife_declared (21:10-14), firstborn_portion_declared (21:15-17), rebellious_son_declared (21:18-21) and hanged_burial_declared (21:22-23) after the tape's last Deuteronomy 18 line on the counter's day (40, 11, 1), no dated field, NO marker at any Deut 19, 20 or 21 verse (markers 172 UNMOVED); their writes — the forty-five NEW ONE each on israel_people (thirty-four STATUSES, ten BLOCKS, one HEAVEN entry); the kin's counts UNMOVED (the references — no second write); the readback's sixty-four rows one per verse in order with no pointer, state, open or stretch row; the daemon law_refuge_war_family registered, given_at Deut 19:1, installed_by boot (ONE probe — the lean form)\n  THE DEUTERONOMY WALK 15b (2026-09-24) (DEUTERONOMY_WALK.md \"Sitting 15b\" THE PROBES; THE LEAN PASS)" % W)
open(P, 'w', encoding='utf-8').write(s)
import py_compile; py_compile.compile(P, doraise=True)
print('patched: Q45 written (to FAIL until the runner and the tape carry chapters 19-21); the file compiles')
