#!/usr/bin/env python3
# THE DEUTERONOMY WALK 19b (2026-09-27): THE SPEC MODULE — the compile's names fixed ONCE at the design and read by every later script (the design writer, the
# probe patch, the exam writer, the types, the runner's parts, the checkpoints): the runner, the daemon, the span, the twenty own-day lines with their kinds, forms and
# fields, the fifty-nine NEW effects with their ops and their subjects, the nine REUSES, the ONE MARKER (Moses' last day), the kin's references with their counts as the
# recon and the callees read them, the parameters, the edges, the Mishnah and Tosefta rows. Nothing here is a verdict — the verdicts are the runner's cells'.
# ch26b_spec.py's form over chapters 29-31. RUN FROM THE REPO ROOT with PYTHONPATH the scratchpad.
RUNNER = 'covenant_return_charge'            # the 76th runner: the covenant in Moab (29), the return and the choice (30), the charge, the hakhel, the tent, the song and the book (31)
DAEMON = 'law_covenant_return_charge'        # the 81st daemon; I5 80 -> 81
GIVEN_AT = 'Deut 29:1'; INSTALLED_BY = 'boot'
SPAN = [['Deut', 29, 1, 28], ['Deut', 30, 1, 20], ['Deut', 31, 1, 30]]
UNITS = {'deu_29_moab_covenant': 'DV29', 'deu_30_teshuvah_choice': 'DV30', 'deu_31_charge_torah': 'DV31'}
CORPUS = ('deu_29_moab_covenant (STEP_Dt_29_1 through STEP_Dt_29_28; claims DV29-01 through DV29-05), deu_30_teshuvah_choice (STEP_Dt_30_1 through STEP_Dt_30_20; claims DV30-01 through DV30-04) and '
          'deu_31_charge_torah (STEP_Dt_31_1 through STEP_Dt_31_30; claims DV31-01 through DV31-06)')
S, B, H = 'status', 'block', 'heaven'
I, MO, YE, LV, TE = 'israel_people', 'moses', 'yehoshua', 'the_levites', 'the_tent_of_meeting'
# THE LINES: (kind, first verse, verse range, claim, cell, form, fields, [(effect, op, subject)], [(reuse effect, verse, subject)])
LINES = [
 ('moab_recital_declared', 'Deut 29:1', '29:1-8', 'DV29-01', 'F1', 'statute', ['you_have_seen_all_the_lord_did_in_egypt', 'no_heart_to_know_until_this_day', 'forty_years_garments_and_sandals_not_worn', 'sihon_and_og_smitten_and_their_land_given', 'keep_the_words_of_this_covenant'],
  [('covenant_words_keeping_commanded', S, I)], []),
 ('covenant_oath_entered_declared', 'Deut 29:9', '29:9-14', 'DV29-02', 'F2', 'statute', ['standing_this_day_all_of_you_before_the_lord', 'from_the_hewer_of_wood_to_the_drawer_of_water', 'to_enter_the_covenant_and_the_oath', 'established_this_day_as_his_people_as_he_swore', 'with_him_who_stands_here_and_him_who_is_not'],
  [('standing_before_the_lord_this_day', S, I), ('covenant_oath_sworn_this_day', S, I), ('covenant_with_those_not_here', S, I)], [('entered_the_covenant', 'Deut 29:11', I), ('became_the_lords_people_this_day', 'Deut 29:12', I)]),
 ('hidden_idolater_curse_declared', 'Deut 29:15', '29:15-20', 'DV29-03', 'F3', 'statute', ['lest_a_heart_turn_to_serve_the_nations_gods', 'a_root_bearing_gall_and_wormwood', 'he_blesses_himself_in_his_heart_in_stubbornness', 'the_lord_will_not_pardon_his_anger_smokes', 'the_curse_written_in_this_book_lies_on_him', 'blotted_out_and_separated_for_evil'],
  [('heart_turning_to_other_gods_barred', B, I), ('stubborn_self_blessing_barred', B, I), ('hidden_idolater_unpardoned', H, I), ('curses_of_the_book_on_the_idolater', H, I), ('name_blotted_from_under_heaven', H, I), ('separated_for_evil_from_all_tribes', H, I)], []),
 ('land_desolation_answer_declared', 'Deut 29:21', '29:21-27', 'DV29-04', 'F4', 'statute', ['the_later_generation_and_the_foreigner_see_the_plagues', 'brimstone_and_salt_like_sodom_and_gomorrah', 'the_nations_ask_why_the_lord_did_thus', 'because_they_forsook_the_covenant_and_served_other_gods', 'uprooted_and_cast_into_another_land_as_this_day'],
  [('land_brimstone_salt_like_sodom', H, I), ('nations_question_answered_covenant_forsaken', H, I), ('uprooted_and_cast_into_another_land', H, I)], []),
 ('hidden_and_revealed_declared', 'Deut 29:28', '29:28', 'DV29-05', 'F5', 'statute', ['the_hidden_things_are_the_lord_our_gods', 'the_revealed_are_ours_and_our_childrens_forever', 'to_do_all_the_words_of_this_law'],
  [('hidden_things_the_lords', S, I), ('revealed_things_ours_to_do', S, I)], []),
 ('return_and_gathering_declared', 'Deut 30:1', '30:1-5', 'DV30-01', 'F6', 'statute', ['when_all_these_things_come_and_you_take_it_to_heart', 'return_to_the_lord_and_hearken_with_all_your_heart', 'the_lord_returns_your_captivity_and_has_compassion', 'gathered_from_all_the_peoples_even_from_the_end_of_heaven', 'brought_into_the_fathers_land_and_multiplied_above_them'],
  [('return_to_the_lord_the_condition', S, I), ('captivity_returned_on_return', H, I), ('gathered_from_all_the_peoples', H, I), ('gathered_from_the_end_of_heaven', H, I), ('brought_into_the_fathers_land_again', H, I), ('multiplied_above_the_fathers', H, I)], []),
 ('heart_circumcised_declared', 'Deut 30:6', '30:6-10', 'DV30-02', 'F7', 'statute', ['the_lord_circumcises_your_heart_to_love_him', 'the_curses_put_on_your_enemies_who_pursued_you', 'you_return_and_hearken_and_do_all_his_commandments', 'abounding_in_the_fruit_of_body_cattle_and_ground', 'rejoicing_over_you_as_he_rejoiced_over_your_fathers'],
  [('heart_circumcised_by_the_lord', H, I), ('curses_put_on_the_enemies', H, I), ('return_and_hearken_and_do_commanded', S, I), ('abounding_in_fruit_of_body_cattle_ground', H, I), ('rejoiced_over_as_over_the_fathers', H, I)], []),
 ('commandment_near_declared', 'Deut 30:11', '30:11-14', 'DV30-03', 'F8', 'statute', ['the_commandment_not_too_hard_nor_far', 'not_in_heaven_nor_beyond_the_sea', 'in_your_mouth_and_in_your_heart_to_do_it'],
  [('commandment_not_too_hard_nor_far', S, I), ('commandment_not_in_heaven_nor_beyond_the_sea', S, I), ('commandment_in_mouth_and_heart_to_do', S, I)], []),
 ('life_and_death_choice_declared', 'Deut 30:15', '30:15-20', 'DV30-04', 'F9', 'statute', ['see_i_set_before_you_life_and_good_death_and_evil', 'if_you_love_and_walk_and_keep_you_live_and_multiply', 'if_your_heart_turns_you_perish_and_not_prolong_days', 'heaven_and_earth_called_to_witness_this_day', 'choose_life_love_hearken_and_cleave_the_length_of_days'],
  [('life_and_death_set_before_israel', S, I), ('choose_life_commanded', S, I), ('living_and_multiplying_for_hearkening', H, I), ('perishing_for_turning_away', H, I), ('length_of_days_on_the_land_promised', H, I)], [('heaven_and_earth_witness', 'Deut 30:19', I), ('blessing_and_curse_set', 'Deut 30:19', I), ('cleaving_commanded', 'Deut 30:20', I)]),
 ('crossing_charge_declared', 'Deut 31:1', '31:1-6', 'DV31-01', 'F10', 'statute', ['moses_went_and_spoke_these_words_to_all_israel', 'a_hundred_and_twenty_years_old_this_day', 'i_can_no_more_go_out_and_come_in_you_shall_not_cross', 'the_lord_your_god_crosses_before_you_and_joshua', 'as_he_did_to_sihon_and_og_so_to_the_nations', 'be_strong_and_of_good_courage_fear_not_he_will_not_forsake_you'],
  [('joshua_to_cross_before_israel', S, I), ('nations_dispossessed_as_sihon_and_og_promised', H, I), ('be_strong_and_courageous_commanded', S, I)], [('fear_not_promised', 'Deut 31:6', I)]),
 ('joshua_charged_before_israel', 'Deut 31:7', '31:7-8', 'DV31-01', 'F10', 'act', ['moses_called_joshua_in_the_sight_of_all_israel', 'be_strong_you_shall_go_with_this_people_into_the_land', 'the_lord_goes_before_you_he_will_not_fail_you'],
  [('joshua_charged_to_bring_israel_in', S, YE)], [('fear_not_promised', 'Deut 31:8', YE)]),
 ('law_written_given', 'Deut 31:9', '31:9', 'DV31-02', 'F11', 'act', ['moses_wrote_this_law', 'gave_it_to_the_priests_the_sons_of_levi_who_carry_the_ark', 'and_to_all_the_elders_of_israel'],
  [('law_written_and_given_to_priests_and_elders', S, I)], []),
 ('hakhel_reading_declared', 'Deut 31:10', '31:10-13', 'DV31-02', 'F11', 'statute', ['at_the_end_of_seven_years_at_the_release_years_set_time_at_the_feast_of_booths', 'when_all_israel_comes_to_appear_at_the_place_read_this_law', 'assemble_the_people_men_women_children_and_the_stranger', 'that_they_hear_and_learn_and_fear_and_do', 'their_children_who_have_not_known_all_the_days_on_the_land'],
  [('hakhel_reading_commanded', S, I), ('hakhel_assembly_of_all_commanded', S, I), ('hakhel_children_hear_and_learn_commanded', S, I)], []),
 ('tent_summons_cloud_appeared', 'Deut 31:14', '31:14-15', 'DV31-03', 'F12', 'act', ['your_days_approach_to_die', 'call_joshua_and_present_yourselves_in_the_tent_that_i_may_commission_him', 'moses_and_joshua_went_and_presented_themselves', 'the_lord_appeared_in_the_pillar_of_cloud_at_the_tent_door'],
  [('moses_days_approach_to_die', S, MO)], [('glory_appeared', 'Deut 31:15', TE)]),
 ('apostasy_and_hidden_face_foretold', 'Deut 31:16', '31:16-18', 'DV31-04', 'F13', 'speech', ['you_shall_sleep_with_your_fathers', 'this_people_will_rise_and_whore_after_the_gods_of_the_land', 'they_will_forsake_me_and_break_my_covenant', 'my_anger_kindled_i_will_forsake_them_and_hide_my_face', 'many_evils_and_troubles_is_it_not_because_our_god_is_not_among_us', 'i_will_surely_hide_my_face_for_the_evil_they_did'],
  [('moses_to_sleep_with_the_fathers', S, MO), ('future_whoring_after_foreign_gods_foretold', H, I), ('covenant_breaking_foretold', H, I), ('face_hidden_and_forsaken_foretold', H, I), ('evils_and_troubles_befall_foretold', H, I)], []),
 ('song_witness_commanded', 'Deut 31:19', '31:19-21', 'DV31-05', 'F14', 'speech', ['write_this_song_and_teach_it_put_it_in_their_mouths', 'that_this_song_be_a_witness_for_me', 'when_they_eat_and_are_sated_and_grow_fat_and_turn', 'the_song_testifies_and_is_not_forgotten_from_their_seeds_mouth', 'i_know_their_inclination_before_i_bring_them_in'],
  [('song_writing_commanded', S, I), ('song_taught_and_put_in_mouths_commanded', S, I), ('song_a_witness_against_israel', S, I)], []),
 ('song_written_taught', 'Deut 31:22', '31:22', 'DV31-05', 'F14', 'act', ['moses_wrote_this_song_that_day', 'and_taught_it_to_the_children_of_israel'],
  [('song_written_and_taught_by_moses', S, I)], []),
 ('joshua_commissioned_at_tent', 'Deut 31:23', '31:23', 'DV31-05', 'F12', 'speech', ['he_commissioned_joshua_be_strong_and_of_good_courage', 'you_shall_bring_the_children_of_israel_into_the_land_i_swore', 'i_will_be_with_you'],
  [('joshua_commissioned_to_bring_israel_in', S, YE), ('lord_with_joshua_promised', H, YE)], []),
 ('book_beside_the_ark_declared', 'Deut 31:24', '31:24-27', 'DV31-06', 'F15', 'statute', ['when_moses_finished_writing_the_words_of_this_law_to_their_end', 'he_commanded_the_levites_who_carry_the_ark', 'take_this_book_and_put_it_beside_the_ark_a_witness_against_you', 'i_know_your_rebellion_and_your_stiff_neck', 'how_much_more_after_my_death'],
  [('book_of_the_law_beside_the_ark_commanded', S, LV), ('book_a_witness_against_israel', S, I)], []),
 ('assembly_and_song_spoken_declared', 'Deut 31:28', '31:28-30', 'DV31-06', 'F15', 'statute', ['assemble_to_me_all_the_elders_of_your_tribes_and_your_officers', 'that_i_speak_these_words_and_call_heaven_and_earth_to_witness', 'after_my_death_you_will_corrupt_and_turn_evil_will_befall_you', 'moses_spoke_the_words_of_this_song_in_the_ears_of_all_the_assembly_to_their_end'],
  [('elders_and_officers_assembled_commanded', S, I), ('corruption_after_moses_death_foretold', H, I), ('song_spoken_to_the_assembly_to_its_end', S, I)], [('heaven_and_earth_witness', 'Deut 31:28', I)]),
]
KINDS = [l[0] for l in LINES]
NEW_E = [(e, op, sub) for l in LINES for e, op, sub in l[7]]
NEW_EFFECTS = [e for e, _, _ in NEW_E]
REUSES = [(e, v, sub, l[0]) for l in LINES for e, v, sub in l[8]]      # (effect, verse, subject, line kind) — a reuse is a further entry on the named ledger
CELLS = {'F1': 'the_moab_recital', 'F2': 'the_covenant_and_the_oath', 'F3': 'the_individuals_curse', 'F4': 'the_lands_desolation', 'F5': 'the_hidden_and_the_revealed', 'F6': 'the_return_and_the_gathering', 'F7': 'the_heart_circumcised',
         'F8': 'the_commandment_near', 'F9': 'life_and_death', 'F10': 'the_charge_and_the_crossing', 'F11': 'the_law_written_and_the_hakhel', 'F12': 'the_tent_and_the_commission', 'F13': 'the_apostasy_foretold', 'F14': 'the_song_commanded', 'F15': 'the_book_beside_the_ark_and_the_assembly'}
# THE MARKER — the one date the chapters set: Moses' last day (31:2 'a hundred and twenty years old THIS DAY'; the year the ink's — Exodus 7:7's eighty at the exodus plus the forty; the month and the day the answer sheet's — the 7th of Adar, Tosefta Sotah 11:3 computing backward from Joshua 4:19; Seder Olam 10:2 as chukat's cell holds it)
MARKER = {'verse': 'Deut 31:2', 'day': (40, 12, 7), 'ink': [120], 'era': 'exodus', 'class': 'F (the day supplied by a PARAMETER — the stitcher\'s class read from its print)', 'parameter': 'the_death_date_of_moses',
          'value': "a hundred and twenty years old this day (31:2) — Moses' last day: the year the ink's (Exodus 7:7's eighty at the exodus + forty), the month and the day the answer sheet's (the 7th of Adar — Tosefta Sotah 11:3); the counter's day moves from 1:3's (40, 11, 1) for the first time in the book"}
DAY_BEFORE, DAY_AFTER = (40, 11, 1), (40, 12, 7)
LINES_BEFORE = [l[0] for l in LINES if l[1].startswith(('Deut 29:', 'Deut 30:'))]; LINES_AFTER = [l[0] for l in LINES if l[1].startswith('Deut 31:')]
# THE KIN'S COUNTS as the recon (section H) and the callees (THE NEAR NAMES) read them — the references UNMOVED after the run; the reuses MOVED by their entries
KIN_UNMOVED = {'other_gods_barred': 1, 'covenant_cut': 3, 'covenant_declared': 1, 'covenant_words_in_moab_declared': 1, 'confessed': 3, 'scattered_among_nations': 0, 'scattered_among_all_peoples': 1, 'land_desolate': 0, 'return_to_egypt_barred': 1,
               'debt_release_owed': 1, 'three_pilgrimages_commanded': 1, 'appearance_owed': 0, 'booths_at_the_place_commanded': 1, 'law_copy_commanded': 1, 'king_from_the_brothers_commanded': 1, 'heart_circumcision_commanded': 1, 'stiffening_barred': 1,
               'shema_commanded': 1, 'forgetting_barred': 1, 'israel_hears_and_fears': 1, 'song_sung': 1, 'love_owed': 1, 'blotted_from_the_book': 1, 'whored_after': 1, 'reprieve_of_a_hundred_and_twenty': 1, 'pillar_leads': 1, 'camp_moves_by_the_cloud': 2,
               'fragments_in_the_ark': 1, 'tablets_delivered': 4, 'oath_sworn': 5, 'return_promised': 1, 'high_above_all_nations_promised': 1, 'blessings_for_hearing': 3, 'curses_for_not_hearkening': 1, 'few_in_number_left': 1,
               'serving_wood_and_stone_among_nations': 1, 'exiled_with_king_to_serve_wood_and_stone': 1, 'plague_struck': 13, 'seed_as_stars': 3, 'witness_declared': 1, 'covenant_remembered': 1, 'great_nation_promised': 3, 'barred_from_the_land': 2}   # barred_from_the_land 2 ON THE WORLD (Moses' AND Aaron's — Numbers 20:12; the recon read Moses' ledger alone: RETYPED FROM THE PRINT at RUN B's first fast check — count_scan counts the world's entries of the effect)
REUSE_BEFORE = {'entered_the_covenant': 3, 'became_the_lords_people_this_day': 1, 'heaven_and_earth_witness': 2, 'blessing_and_curse_set': 1, 'cleaving_commanded': 2, 'fear_not_promised': 4, 'glory_appeared': 6}
import collections as _c
_rc = _c.Counter(e for e, _, _, _ in REUSES)
REUSE_AFTER = {e: REUSE_BEFORE[e] + _rc[e] for e in REUSE_BEFORE}
# THE EDGES from the runner — every one REFERENCE (the ink names the kin's institution, or the kin's cell names THIS chapter's verse forward); the registration edge and the census's FALSE and VIA edges filed at RUN B from the gate's print
EDGES = ['opening_speech', 'gad_reuben', 'good_land', 'exodus_story', 'covenant_at_horeb', 'hear_o_israel', 'seven_nations', 'obey_horeb', 'second_tablets', 'not_righteousness', 'blessing_and_curse', 'seducers', 'food_tithe', 'release_firstborn',
         'festivals_judges', 'courts_prophet', 'firstfruits_ebal_curses', 'refuge_war_family', 'tochacha', 'yovel', 'calendar', 'moadim', 'musafim', 'mamre', 'primeval', 'family', 'erection', 'beha', 'chukat', 'journeys', 'vestments', 'shelach', 'place_name']
POINTERS_PREDICTED = [('Deut 29:12', 'as He spoke to you and as He swore to your fathers — the oath lines behind (RUN_CITATION)'), ('Deut 31:3', 'as the LORD has spoken — 3:28 the charge to Joshua behind on the tape (RUN_CITATION)'),
                      ('Deut 31:4', 'as He did to Sihon and to Og — the kings smitten, the tape\'s own lines (RUN_CITATION)'), ('Deut 29:22', 'like the overthrow of Sodom — a comparative (FALSE)'), ('Deut 30:9', 'as He rejoiced over your fathers — a comparative, 28:63\'s twin (FALSE)')]
POINTER_ROW_PAID = {'verse': 'Deut 31:10', 'owed_by': "sitting 15b's list (COMPILE_DEBT's lean box line (3): 'the pointer rows for 19:15, 28:14 and 31:10')", 'paid_by': "the line hakhel_reading_declared and the readback row 31:10 referencing law_copy_commanded (17:18-19) by CALL to courts_prophet.the_king('the_copy_of_the_law')"}
CAL_NEW = ['the_hakhel_time', 'the_death_date_of_moses']
PARAMS = ['the_hakhel_time', 'the_hakhels_reader', 'the_hakhels_text', 'the_hakhels_portions', 'the_hakhels_place', 'the_hakhels_blessings', 'the_four_classes', 'the_interpreter', 'the_blessing_on_bad_tidings', 'the_three_gifts_and_their_merits', 'the_death_date_of_moses', 'the_books_place', 'the_intercalated_month']
MISHNAH = [('Sotah', 7, 8), ('Berakhot', 9, 2), ('Avot', 1, 6)]
TOSEFTA = [('Tosefta Sotah', 11, 2), ('Tosefta Sotah', 11, 3), ('Tosefta Sotah', 11, 4), ('Tosefta Sotah', 11, 7), ('Tosefta Ketubot', 5, 8)]
TOSEFTA_NOTE = "the ledger names 'Tosefta Sotah 11:7' for Moses' hundred and twenty to the day and 'Tosefta Sotah 11' for the three gifts, 'Tosefta Ketubot 5' for Nakdimon's daughter: the export's paragraphs are 11:3 (the 7th of Adar), 11:4 (the well, the cloud and the manna by the three merits), 11:2 (the manna after Moses' death) and Ketubot 5:8 (the daughter gathering barley) — 11:7 (Rachel's tomb, Saul's seat) READ WHOLE and found NOT THE PARALLEL: the translator's paragraph number differs from the export's; the neighbours read whole and taken as the cases"
TALMUD_OWED = ['Bava Batra 14a-15a (the book beside the ark; the last eight verses)', 'Bava Metzia 59b (not in heaven)', 'Chagigah 3a (the four classes at the hakhel) and 5a-b (the hidden face)', 'Sanhedrin 43b (the dotted letters of 29:28) and 90b (31:16 and the resurrection)', 'Temurah 16a (the laws forgotten at Moses\' death)', 'Eruvin 54b (in their mouths — the order of teaching)', 'Sotah 41a-b (the hakhel\'s reading, the platform, the blessings)', 'Megillah 31b (the curses\' reading before the year\'s end)', 'Rosh Hashanah 8b, 12b and Arakhin 28b (the end of the seventh year; the count)']
def counts():
    ops = _c.Counter(op for _, op, _ in NEW_E); subs = _c.Counter(sub for _, _, sub in NEW_E); rsubs = _c.Counter(sub for _, _, sub, _ in REUSES); forms = _c.Counter(l[5] for l in LINES)
    return {'lines': len(LINES), 'new_effects': len(NEW_EFFECTS), 'distinct': len(set(NEW_EFFECTS)), 'ops': dict(ops), 'reuses': len(REUSES), 'writes': len(NEW_EFFECTS) + len(REUSES), 'edges': len(EDGES), 'params': len(PARAMS),
            'mishnah': len(MISHNAH), 'tosefta': len(TOSEFTA), 'per_line': [(l[1], len(l[7]) + len(l[8])) for l in LINES], 'cells': len(CELLS), 'subjects_new': dict(subs), 'subjects_reuse': dict(rsubs), 'forms': dict(forms),
            'writes_by_subject': dict(subs + rsubs), 'lines_before': len(LINES_BEFORE), 'lines_after': len(LINES_AFTER)}
if __name__ == '__main__':
    c = counts(); print(c)
    assert c['new_effects'] == c['distinct'], 'a name twice'
    assert len(set(KINDS)) == len(KINDS)
    assert set(REUSE_AFTER) == set(REUSE_BEFORE) and all(REUSE_AFTER[e] > REUSE_BEFORE[e] for e in REUSE_BEFORE)
    print('FIRST VERSES', [l[1] for l in LINES]); print('WRITES PER LINE (new + reuse)', c['per_line']); print('REUSE_AFTER', REUSE_AFTER)
    print('SPEC OK')
