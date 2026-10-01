import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE DEUTERONOMY WALK 22b (2026-09-30): THE SPEC MODULE — the compile's names fixed ONCE at the design and read by every later script (the design writer, the probe patch,
# the exam writer, the types, the runner's parts, the checkpoints): the runner, the daemon, the span, the SIX own-day lines with their kinds, forms and fields (one per claim —
# 21b's form), the TWELVE NEW effects with their ops and subjects (moses, israel_people, yehoshua) and THE THREE REUSES (an effect's own forward seat lies in the chapter — the
# song's denial 32:52 -> 34:4, the gathering 32:50 -> 34:5, Aaron's thirty days Numbers 20:29 -> 34:8), NO MARKER (the death falls on 19b's marker's day (40, 12, 7); the thirty
# days a DURATION — the counter UNMOVED by this design's ruling), the kin's references with their counts COMPUTED on the one database at the spec's own main (printed, then read),
# the parameters (the answer sheet's rows), the DATA rows, the edges, the Mishnah and Tosefta rows the ledger cites (the regex's one misread named). Nothing here is a verdict —
# the verdicts are the runner's cells'. ch33b_spec.py's form over chapter 34. RUN FROM THE REPO ROOT with PYTHONPATH the scratchpad.
RUNNER = 'moses_death'                    # the 79th runner: the death of Moses (34:1-12) — the ascent, the oath, the death and the burial, the years and the thirty days, Joshua, the prophet
DAEMON = 'law_moses_death'                # the 84th daemon; I5 83 -> 84
GIVEN_AT = 'Deut 34:1'; INSTALLED_BY = 'boot'
SPAN = [['Deut', 34, 1, 12]]
UNITS = {'deu_34_moses_death': 'DV34'}
CORPUS = 'deu_34_moses_death (STEP_Dt_34_1 through STEP_Dt_34_12; claims DV34-01 through DV34-06)'
S, B, H = 'status', 'block', 'heaven'
I, MO, GOD, YE = 'israel_people', 'moses', 'god', 'yehoshua'
# THE LINES: (kind, first verse, verse range, claim, cell, form, fields, [(effect, op, subject)], [(reuse effect, verse, subject)]) — ONE PER CLAIM (21b's form): five ACTS of the
# narrator (the ascent, the death and the burial, the years and the weeping, Joshua and the receipt, the epilogue — 34:10's "there arose not" a narrative past) and ONE SPEECH of the
# LORD (the oath and the denial, 34:4 — the subject god, 20b's form for the LORD's speeches); every line at Moses' last day (40, 12, 7) — NO MARKER
LINES = [
 ('moses_went_up_to_nebo_and_saw_the_land', 'Deut 34:1', '34:1-3', 'DV34-01', 'F1', 'act', ['and_moses_went_up_from_the_plains_of_moab_to_mount_nebo_the_top_of_pisgah_over_against_jericho', 'the_lord_showed_him_all_the_land_gilead_to_dan_naphtali_ephraim_and_manasseh_judah_to_the_hinder_sea', 'the_south_and_the_plain_the_valley_of_jericho_the_city_of_palms_to_zoar'],
  [('moses_went_up_to_nebo_as_commanded', S, MO), ('the_whole_land_shown_to_moses_gilead_to_zoar', S, MO)], []),
 ('oath_land_shown_not_crossed_declared', 'Deut 34:4', '34:4', 'DV34-02', 'F2', 'speech', ['this_is_the_land_which_i_swore_to_abraham_to_isaac_and_to_jacob_saying_to_your_seed_i_will_give_it', 'i_have_caused_you_to_see_it_with_your_eyes_but_you_shall_not_cross_over_there'],
  [('land_sworn_to_the_fathers_shown_at_the_end_declared', S, MO)], [('see_the_land_from_afar_not_go_there', 'Deut 34:4', MO)]),
 ('moses_died_and_was_buried', 'Deut 34:5', '34:5-6', 'DV34-03', 'F3', 'act', ['moses_the_servant_of_the_lord_died_there_in_the_land_of_moab_by_the_mouth_of_the_lord', 'he_buried_him_in_the_valley_in_the_land_of_moab_over_against_beth_peor', 'no_man_knows_his_grave_to_this_day'],
  [('moses_died_by_the_mouth_of_the_lord', S, MO), ('buried_by_the_lord_grave_unknown', S, MO), ('three_gifts_merits_withdrawn_at_the_third_death', S, I)], [('gathered_to_his_people', 'Deut 34:5', MO)]),
 ('moses_hundred_and_twenty_israel_wept_thirty_days', 'Deut 34:7', '34:7-8', 'DV34-04', 'F4', 'act', ['moses_was_a_hundred_and_twenty_years_old_when_he_died_his_eye_not_dim_nor_his_natural_force_abated', 'the_children_of_israel_wept_for_moses_in_the_plains_of_moab_thirty_days', 'the_days_of_weeping_in_the_mourning_for_moses_were_ended'],
  [('died_at_a_hundred_and_twenty_eye_undimmed', S, MO), ('days_of_weeping_for_moses_ended', S, I)], [('mourned_thirty_days', 'Deut 34:8', I)]),
 ('joshua_full_of_the_spirit_israel_hearkened', 'Deut 34:9', '34:9', 'DV34-05', 'F5', 'act', ['joshua_the_son_of_nun_was_full_of_the_spirit_of_wisdom_for_moses_had_laid_his_hands_upon_him', 'the_children_of_israel_hearkened_to_him_and_did_as_the_lord_commanded_moses'],
  [('spirit_of_wisdom_by_the_hands_laid', S, YE), ('israel_hearkened_to_joshua_as_the_lord_commanded_moses', S, I)], []),
 ('no_prophet_like_moses_declared', 'Deut 34:10', '34:10-12', 'DV34-06', 'F6', 'act', ['there_arose_not_a_prophet_since_in_israel_like_moses_whom_the_lord_knew_face_to_face', 'all_the_signs_and_wonders_the_lord_sent_him_to_do_in_the_land_of_egypt_to_pharaoh_his_servants_and_his_land', 'the_mighty_hand_and_the_great_terror_which_moses_wrought_in_the_sight_of_all_israel'],
  [('no_prophet_like_moses_face_to_face_declared', S, I), ('signs_mighty_hand_great_terror_in_the_sight_of_all_israel_declared', S, I)], []),
]
KINDS = [l[0] for l in LINES]
NEW_E = [(e, op, sub) for l in LINES for e, op, sub in l[7]]
NEW_EFFECTS = [e for e, _, _ in NEW_E]
REUSES = [(e, v, sub, l[0]) for l in LINES for e, v, sub in l[8]]      # THREE — the song's denial (32:52), the gathering (32:50 — Aaron's word), Aaron's thirty days (Numbers 20:29)
CELLS = {'F1': 'the_ascent_and_the_land_shown', 'F2': 'the_oath_and_the_denial', 'F3': 'the_death_and_the_burial', 'F4': 'the_years_and_the_thirty_days', 'F5': 'joshua_and_the_receipt', 'F6': 'the_prophet_the_signs_and_the_terror'}
# NO MARKER — the death on 19b's marker's day (40, 12, 7): the seventh of Adar (Tosefta Sotah 11:3 read at 19b; the_death_date_of_moses the calendar's parameter); THE THIRTY DAYS
# OF WEEPING A DURATION — THE DESIGN'S RULING: the counter does NOT move (a marker is the ink's own date statement; a duration is an act's length; the tape's counter walks at the
# next book's first marker — Joshua's tape, cited never read; the tradition's arithmetic Adar 7 to Nisan 7 a DATA row, Kiddushin 38a cited never read); markers 173 UNMOVED
MARKER = None
DAY = (40, 12, 7)
GUARDS = {'the_two_numbers': "34:7's 120 (31:2's number restated on the marker's day — no second marker) and 34:8's 30 (Aaron's thirty, Numbers 20:29 — a DURATION on the weeping's line, no timer, the counter unmoved): the parser's two hits DATA rows, no count in the world"}
KIN = ('go_up_to_nebo_see_the_land_commanded', 'die_in_the_mountain_gathered_to_your_people_commanded', 'as_aaron_died_in_hor_and_was_gathered', 'see_the_land_from_afar_not_go_there', 'barred_from_the_land', 'gathered_to_his_people',
       'mourned_thirty_days', 'garments_transferred', 'invested_office', 'joshua_commissioned_to_bring_israel_in', 'joshua_charged_to_bring_israel_in', 'lord_with_joshua_promised', 'moses_to_sleep_with_the_fathers',
       'corruption_after_moses_death_foretold', 'prophet_like_moses_promised', 'face_radiant', 'signs_in_hand', 'manna_provided', 'well_given', 'camp_moves_by_the_cloud', 'bones_oath', 'buried', 'wept', 'blessing_given_before_moses_death')
REUSE_NAMES = sorted({e for e, _, _, _ in REUSES})
import collections as _c, os as _os, sqlite3 as _sq, subprocess as _sp
_ROOT = _ROOT
def kin_counts():
    """the references' counts in ONE full run of the tape on the one database (the largest source — count_scan's form): computed, printed at the spec's main, read by the design, the probe and the runner"""
    db = f'{_ROOT}/World/journal/data/world.sqlite'
    c_ = _sq.connect('file:%s?mode=ro' % db, uri=True)
    src = c_.execute("SELECT source FROM run_ledger GROUP BY source ORDER BY COUNT(*) DESC, source LIMIT 1").fetchone()[0]
    return {k: c_.execute("SELECT COUNT(*) FROM run_ledger WHERE effect=? AND source=?", (k, src)).fetchone()[0] for k in KIN}
KIN_BEFORE = kin_counts()
_rc = _c.Counter(e for e, _, _, _ in REUSES)
KIN_AFTER = {k: KIN_BEFORE[k] + _rc.get(k, 0) for k in KIN}        # the three reuses move three counts by one each; the rest UNMOVED
REUSE_BEFORE = {e: KIN_BEFORE[e] for e in REUSE_NAMES}; REUSE_AFTER = {e: KIN_AFTER[e] for e in REUSE_NAMES}
EDGES = ['song_charge_nebo', 'covenant_return_charge', 'blessing_of_moses', 'gad_reuben', 'chukat', 'journeys', 'second_tablets', 'zelophehad', 'opening_speech', 'beha', 'naso', 'courts_prophet', 'erection', 'exodus_story', 'joseph', 'family', 'mamre', 'hear_o_israel', 'obey_horeb', 'shelach']
POINTERS_PREDICTED = [('Deut 34:4', "the two denials — 32:52's 'you shall not come there' (see_the_land_from_afar_not_go_there on moses, song_charge_nebo's line) and 34:4's 'you shall not cross over there': THE SONG'S OWED POINTER PAID — a REUSE of the effect at its own forward seat and a POINTER ROW of the readback, grade R (341:1 and 357:27 read them word for word as king and commoner, living and dead)"),
                      ('Deut 34:5', "32:50's 'die in the mountain and be gathered as Aaron died' (die_in_the_mountain_gathered_to_your_people_commanded, as_aaron_died_in_hor_and_was_gathered on moses): THE SONG'S OWED POINTER PAID — the death in Aaron's words (by the mouth of the LORD, when he died, thirty days — Numbers 20:29, 33:38-39 the RUN CITATIONS by CALL to chukat and journeys) though 34:5 shares no token with 32:50: a REUSE of gathered_to_his_people on moses and a POINTER ROW, grade R"),
                      ('Deut 34:6', "33:21's lawgiver's portion — MOSES' GRAVE IN GAD'S PORTION (Onkelos 33:21; 355:6 and 357:31; Tosefta Sotah 4:4's four mil; gad_reuben's DATA moses_grave by CALL — Reuben's Nebo, Gad's field): THE BLESSING'S OWED POINTER PAID — a POINTER ROW, grade R; 'no man knows his grave' a status on moses"),
                      ('Deut 34:9', "'as the LORD commanded Moses' — THE RECEIPT: Numbers 27:18-23 on the tape (invested_office on yehoshua — the hands laid; zelophehad and opening_speech by CALL) and 31:7, 31:23 (joshua_charged_to_bring_israel_in, joshua_commissioned_to_bring_israel_in — covenant_return_charge by CALL): a RUN CITATION; the register's seat RE-DECLARED (class NONE for a book unread -> the class the gate computes, read from its print)"),
                      ('Deut 34:1', "32:49's 'go up to this mountain of Abarim, Mount Nebo … over against Jericho' (go_up_to_nebo_see_the_land_commanded on moses): the command obeyed word for word — a RUN CITATION by CALL to song_charge_nebo; 3:27's Pisgah (opening_speech.the_plea)")]
STATE_ROWS = []
POINTER_ROWS = ['Deut 34:4', 'Deut 34:5', 'Deut 34:6']     # the song's two and the blessing's one PAID — grade R
CAL_NEW = []                                              # no new clock key — the death date 19b's; the thirty days a duration, the counter unmoved
DATA_ROWS = ['the_two_numbers', 'the_readback', 'the_three_gifts_third_event', 'the_thirty_days_a_duration', 'the_land_shown_as_the_future', 'who_wrote_and_moses_died_there', 'the_grave_in_gads_portion_paid', 'the_oath_is_exodus_33_1',
             'the_death_in_aarons_words', 'the_homograph_of_the_name', 'the_eighteen_ledgers_pointers', 'the_seat_rule_by_row', 'the_receipt_re_declared', 'the_books_edge', 'onkelos_and_the_sifrei_one_teaching', 'the_pointers_paid']
PARAMS = ['the_nazirites_term', 'the_chain_of_transmission', 'the_world_to_come_share', 'joseph_bones_merited', 'the_burial_by_the_place', 'the_four_mil', 'the_death_date_of_moses', 'the_prophets_bound', 'measure_for_measure']
MISHNAH = [('Avot', 1, 1), ('Nazir', 1, 3), ('Sanhedrin', 10, 1), ('Sotah', 1, 7), ('Sotah', 1, 9)]
MISHNAH_EXCLUDED = [('Sotah', 4, 4)]        # the regex's one misread — "the Tosefta's Sotah 4:4" and "(Sotah 4:4 — the testing shelf's row)" name the TOSEFTA's row; the Mishnah's Sotah 4:4 is another row, read whole and EXCLUDED
TOSEFTA = [('Tosefta Sotah', 4, 4)]
TOSEFTA_OWED = []
TALMUD_OWED = ["Bava Batra 15a (who wrote 'and Moses died there' — 357:28's dispute)", "Sotah 13b (Moses' grave and the four mil — 357:31; gad_reuben's DATA names 13b:20)", "Shabbat 87a (the tablets broken approved — 357:44)", "Menachot 30a (the last eight verses — 357:28)", "Kiddushin 38a (the manna in store to the sixteenth of Nisan — the three gifts' third event; the seventh of Adar)"]
PROPHETS_CITED = ['Joshua 1:1', 'Joshua 1:11', 'Joshua 4:14', 'Joshua 4:19', 'Joshua 5:12', 'Judges 6:22', 'Jeremiah 32:20', 'Isaiah 11:2', 'Isaiah 15:5', 'Ezekiel 20:35', '2 Chronicles 28:15', '2 Kings 21:26']
def counts():
    ops = _c.Counter(op for _, op, _ in NEW_E); subs = _c.Counter(sub for _, _, sub in NEW_E); rsubs = _c.Counter(sub for _, _, sub, _ in REUSES); forms = _c.Counter(l[5] for l in LINES)
    return {'lines': len(LINES), 'new_effects': len(NEW_EFFECTS), 'distinct': len(set(NEW_EFFECTS)), 'ops': dict(ops), 'reuses': len(REUSES), 'writes': len(NEW_EFFECTS) + len(REUSES), 'edges': len(EDGES), 'params': len(PARAMS),
            'mishnah': len(MISHNAH), 'tosefta': len(TOSEFTA), 'per_line': [(l[1], len(l[7]) + len(l[8])) for l in LINES], 'cells': len(CELLS), 'subjects_new': dict(subs), 'subjects_reuse': dict(rsubs), 'forms': dict(forms),
            'writes_by_subject': dict(subs + rsubs), 'fields': sum(len(l[6]) for l in LINES), 'data_rows': len(DATA_ROWS), 'kin': len(KIN), 'guards': len(GUARDS)}
if __name__ == '__main__':
    import yaml
    c = counts(); print(c)
    assert c['new_effects'] == c['distinct'], 'a name twice'
    assert len(set(KINDS)) == len(KINDS) and all(l[4] in CELLS for l in LINES) and len(set(l[4] for l in LINES)) == len(CELLS)
    S9 = _ROOT + '/World/step9'
    fx = yaml.safe_load(open(S9 + '/effect_vocabulary.yaml', encoding='utf-8'))['effects']; ev = yaml.safe_load(open(S9 + '/event_vocabulary.yaml', encoding='utf-8'))['events']
    coll_e = [e for e in NEW_EFFECTS if e in fx]; coll_k = [k for k in KINDS if k in ev]
    print('COLLISIONS: effects present before', coll_e, '| kinds present before', coll_k)
    assert not coll_e and not coll_k, 'a new name already in a registry'
    assert all(e in fx for e in KIN), [e for e in KIN if e not in fx]
    print('KIN_BEFORE (computed on the one database, the largest source):', KIN_BEFORE); print('KIN_AFTER (the three reuses added):', KIN_AFTER); print('REUSE_BEFORE', REUSE_BEFORE, 'REUSE_AFTER', REUSE_AFTER)
    print('FIRST VERSES', [l[1] for l in LINES]); print('WRITES PER LINE (new + reuse)', c['per_line']); print('SUBJECTS', c['subjects_new'], c['subjects_reuse'])
    print('SPEC OK')
