#!/usr/bin/env python3
# THE DEUTERONOMY WALK 20b (2026-09-28): THE SPEC MODULE — the compile's names fixed ONCE at the design and read by every later script (the design writer, the
# probe patch, the exam writer, the types, the runner's parts, the checkpoints): the runner, the daemon, the span, the sixteen own-day lines with their kinds, forms and
# fields, the forty-two NEW effects with their ops and their subjects, the three REUSES, NO MARKER (the song stands on 19b's marker — Moses' last day (40, 12, 7)), the
# kin's references with their counts as the recon and the callees read them, the parameters (the answer sheet's rows), the DATA rows (the parser's two guards among them),
# the edges, the Mishnah and Tosefta rows. Nothing here is a verdict — the verdicts are the runner's cells'. ch29b_spec.py's form over chapter 32. RUN FROM THE REPO ROOT with PYTHONPATH the scratchpad.
RUNNER = 'song_charge_nebo'                  # the 77th runner: the song (32:1-43), the charge after it (32:44-47), the summons to Nebo (32:48-52)
DAEMON = 'law_song_charge_nebo'              # the 82nd daemon; I5 81 -> 82
GIVEN_AT = 'Deut 32:1'; INSTALLED_BY = 'boot'
SPAN = [['Deut', 32, 1, 52]]
UNITS = {'deu_32_haazinu': 'DV32', 'deu_32_song_aftermath': 'DV32A'}
CORPUS = ('deu_32_haazinu (STEP_Dt_32_1 through STEP_Dt_32_43; claims DV32-01 through DV32-12) and deu_32_song_aftermath (STEP_Dt_32_44 through STEP_Dt_32_52; claims DV32A-01 through DV32A-04)')
S, B, H = 'status', 'block', 'heaven'
I, MO, YE = 'israel_people', 'moses', 'yehoshua'
# THE LINES: (kind, first verse, verse range, claim, cell, form, fields, [(effect, op, subject)], [(reuse effect, verse, subject)]) — ONE PER CLAIM (18b's form): the song's
# twelve stanzas SPEECHES (Moses' witness-song; from 32:20 the LORD's words inside it), the frame an ACT (Moses and Hoshea speak the song), a STATUTE (the charge) and two
# SPEECHES of the LORD to Moses (the summons, the reason); every line at Moses' last day (40, 12, 7) after 19b's marker — NO MARKER HERE (32:48's 'selfsame day' is that day)
LINES = [
 ('song_witnesses_called_declared', 'Deut 32:1', '32:1-4', 'DV32-01', 'F1', 'speech', ['give_ear_o_heavens_and_let_the_earth_hear', 'my_doctrine_as_the_rain_my_speech_as_the_dew', 'i_will_proclaim_the_name_of_the_lord_ascribe_greatness', 'the_rock_his_work_is_perfect_all_his_ways_justice'],
  [('doctrine_as_rain_and_dew_likened', S, I), ('name_of_the_lord_proclaimed_greatness_ascribed', S, I), ('the_rock_perfect_and_just_declared', S, I)], [('heaven_and_earth_witness', 'Deut 32:1', I)]),
 ('song_crooked_generation_declared', 'Deut 32:5', '32:5-6', 'DV32-02', 'F2', 'speech', ['is_corruption_his_no_his_childrens_is_the_blemish', 'a_perverse_and_crooked_generation', 'do_you_thus_requite_the_lord_o_foolish_people_and_unwise', 'is_he_not_your_father_who_acquired_you_he_made_you_and_established_you'],
  [('generation_crooked_not_his_children', S, I), ('father_who_acquired_you_requited', S, I)], []),
 ('song_nations_divided_lords_portion_declared', 'Deut 32:7', '32:7-9', 'DV32-03', 'F3', 'speech', ['remember_the_days_of_old_ask_your_father_and_your_elders', 'when_the_most_high_gave_the_nations_their_inheritance_and_separated_the_sons_of_man', 'he_set_the_borders_of_the_peoples_by_the_number_of_the_children_of_israel', 'the_lords_portion_is_his_people_jacob_the_lot_of_his_inheritance'],
  [('days_of_old_remember_commanded', S, I), ('nations_bounds_set_by_number_of_israel', S, I), ('lords_portion_his_people_jacob', S, I)], []),
 ('song_found_in_the_desert_declared', 'Deut 32:10', '32:10-12', 'DV32-04', 'F4', 'speech', ['he_found_him_in_a_desert_land_and_in_the_howling_waste', 'he_compassed_him_cared_for_him_kept_him_as_the_apple_of_his_eye', 'as_an_eagle_stirs_up_her_nest_hovers_spreads_her_wings_takes_and_bears', 'the_lord_alone_led_him_and_no_strange_god_with_him'],
  [('found_in_the_desert_encircled_and_kept', S, I), ('apple_of_his_eye_kept', S, I), ('as_an_eagle_stirring_its_nest_borne', S, I), ('the_lord_alone_led_no_foreign_god', S, I)], []),
 ('song_heights_honey_rock_declared', 'Deut 32:13', '32:13-14', 'DV32-05', 'F5', 'speech', ['he_made_him_ride_on_the_high_places_of_the_earth_and_eat_the_fruitage_of_the_field', 'honey_out_of_the_crag_and_oil_out_of_the_flinty_rock', 'curd_of_kine_milk_of_sheep_fat_of_lambs_rams_of_bashan_and_he_goats', 'the_kidney_fat_of_wheat_and_the_blood_of_the_grape_you_drank'],
  [('heights_of_the_land_ridden_honey_from_the_rock', S, I), ('feast_of_curd_milk_fat_and_wine_given', S, I)], []),
 ('song_jeshurun_fat_kicked_declared', 'Deut 32:15', '32:15-18', 'DV32-06', 'F6', 'speech', ['jeshurun_grew_fat_and_kicked_you_grew_fat_thick_and_gross', 'he_forsook_god_who_made_him_and_contemned_the_rock_of_his_salvation', 'they_roused_him_to_jealousy_with_strange_gods_and_provoked_him_with_abominations', 'they_sacrificed_to_demons_no_gods_new_ones_that_came_up_of_late', 'of_the_rock_that_begot_you_you_were_unmindful_and_forgot_god_who_bore_you'],
  [('jeshurun_fat_kicked_forsook_god', S, I), ('demons_and_new_gods_sacrificed', S, I), ('rock_that_begot_you_forgotten', S, I)], []),
 ('song_face_hidden_foolish_nation_declared', 'Deut 32:19', '32:19-22', 'DV32-07', 'F7', 'speech', ['the_lord_saw_and_spurned_from_the_provoking_of_his_sons_and_daughters', 'i_will_hide_my_face_from_them_i_will_see_what_their_end_shall_be', 'i_will_rouse_them_to_jealousy_with_a_no_people_with_a_vile_nation_provoke_them', 'a_fire_is_kindled_in_my_nostril_and_burns_to_the_depths_of_sheol'],
  [('jealousy_by_no_people_foolish_nation', H, I), ('fire_kindled_to_the_lowest_sheol', H, I)], [('face_hidden_and_forsaken_foretold', 'Deut 32:20', I)]),
 ('song_evils_heaped_declared', 'Deut 32:23', '32:23-25', 'DV32-08', 'F8', 'speech', ['i_will_heap_evils_upon_them_i_will_spend_my_arrows_upon_them', 'the_wasting_of_hunger_the_devouring_of_the_fiery_bolt_and_bitter_destruction', 'the_teeth_of_beasts_and_the_venom_of_crawling_things_of_the_dust', 'without_the_sword_shall_bereave_and_in_the_chambers_terror'],
  [('evils_heaped_arrows_spent', H, I), ('hunger_beasts_serpents_sword_terror_sent', H, I)], []),
 ('song_enemys_boast_declared', 'Deut 32:26', '32:26-28', 'DV32-09', 'F9', 'speech', ['i_said_i_would_make_an_end_of_them_and_make_their_memory_cease', 'were_it_not_that_i_dreaded_the_enemys_provocation_lest_they_say_our_hand_is_exalted', 'for_they_are_a_nation_void_of_counsel_and_there_is_no_understanding_in_them'],
  [('blotting_out_stayed_by_the_enemys_boast', H, I), ('nation_void_of_counsel', S, I)], []),
 ('song_one_chasing_a_thousand_declared', 'Deut 32:29', '32:29-33', 'DV32-10', 'F10', 'speech', ['if_they_were_wise_they_would_understand_this_and_discern_their_latter_end', 'how_should_one_chase_a_thousand_and_two_put_ten_thousand_to_flight', 'except_their_rock_had_sold_them_and_the_lord_had_delivered_them_up', 'their_rock_is_not_as_our_rock_and_our_enemies_are_judges', 'their_vine_is_of_the_vine_of_sodom_grapes_of_gall_and_bitter_clusters', 'their_wine_is_the_venom_of_serpents_and_the_cruel_poison_of_asps'],
  [('one_chasing_a_thousand_rock_sold_them', S, I), ('vine_of_sodom_gall_grapes', S, I)], []),
 ('song_vengeance_in_store_declared', 'Deut 32:34', '32:34-38', 'DV32-11', 'F11', 'speech', ['is_not_this_laid_up_in_store_with_me_sealed_up_in_my_treasuries', 'vengeance_is_mine_and_recompense_at_the_time_their_foot_shall_slip', 'the_lord_will_judge_his_people_and_repent_himself_for_his_servants', 'where_are_their_gods_the_rock_in_whom_they_trusted_let_them_rise_up_and_help_you'],
  [('vengeance_laid_up_in_store_sealed', H, I), ('lord_judges_his_people_repents_himself', H, I), ('where_are_their_gods_asked', S, I)], []),
 ('song_i_am_he_declared', 'Deut 32:39', '32:39-43', 'DV32-12', 'F12', 'speech', ['see_now_that_i_even_i_am_he_and_there_is_no_god_with_me', 'i_kill_and_i_make_alive_i_have_wounded_and_i_heal_and_none_delivers_out_of_my_hand', 'i_lift_up_my_hand_to_heaven_and_say_as_i_live_forever', 'if_i_whet_my_glittering_sword_i_will_render_vengeance_to_my_adversaries', 'sing_aloud_o_nations_of_his_people_he_avenges_the_blood_of_his_servants_and_makes_expiation_for_the_land_of_his_people'],
  [('i_i_am_he_no_god_beside_me', S, I), ('i_kill_and_make_alive_none_delivers', S, I), ('hand_lifted_to_heaven_live_forever_sworn', S, I), ('sword_whetted_vengeance_rendered', H, I), ('nations_sing_with_his_people_land_atones', H, I)], []),
 ('song_spoken_by_moses_and_hoshea', 'Deut 32:44', '32:44-45', 'DV32A-01', 'F13', 'act', ['moses_came_and_spoke_all_the_words_of_this_song_in_the_ears_of_the_people', 'he_and_hoshea_the_son_of_nun', 'moses_made_an_end_of_speaking_all_these_words_to_all_israel'],
  [('song_spoken_in_the_ears_of_the_people', S, I), ('hoshea_speaks_the_song_beside_moses', S, YE)], []),
 ('set_your_heart_no_empty_matter_declared', 'Deut 32:46', '32:46-47', 'DV32A-02', 'F14', 'statute', ['set_your_heart_to_all_the_words_which_i_testify_against_you_this_day', 'that_you_may_command_your_children_to_observe_to_do_all_the_words_of_this_law', 'for_it_is_no_vain_thing_for_you_because_it_is_your_life', 'through_this_thing_you_shall_prolong_your_days_on_the_land_which_you_cross_the_jordan_to_possess'],
  [('set_your_heart_to_these_words_commanded', S, I), ('it_is_your_life_no_empty_matter', S, I)], [('length_of_days_on_the_land_promised', 'Deut 32:47', I)]),
 ('nebo_summons_die_as_aaron', 'Deut 32:48', '32:48-50', 'DV32A-03', 'F15', 'speech', ['the_lord_spoke_to_moses_that_selfsame_day', 'go_up_into_this_mountain_of_abarim_mount_nebo_and_behold_the_land_of_canaan', 'die_in_the_mount_where_you_go_up_and_be_gathered_to_your_people', 'as_aaron_your_brother_died_in_mount_hor_and_was_gathered_to_his_people'],
  [('go_up_to_nebo_see_the_land_commanded', S, MO), ('die_in_the_mountain_gathered_to_your_people_commanded', S, MO), ('as_aaron_died_in_hor_and_was_gathered', S, MO)], []),
 ('meribah_trespass_not_go_there_declared', 'Deut 32:51', '32:51-52', 'DV32A-04', 'F16', 'speech', ['because_you_trespassed_against_me_at_the_waters_of_meribath_kadesh_in_the_wilderness_of_zin', 'because_you_did_not_sanctify_me_in_the_midst_of_the_children_of_israel', 'you_shall_see_the_land_before_you_but_there_you_shall_not_go'],
  [('trespassed_at_meribath_kadesh_not_sanctified', S, MO), ('see_the_land_from_afar_not_go_there', H, MO)], []),
]
KINDS = [l[0] for l in LINES]
NEW_E = [(e, op, sub) for l in LINES for e, op, sub in l[7]]
NEW_EFFECTS = [e for e, _, _ in NEW_E]
REUSES = [(e, v, sub, l[0]) for l in LINES for e, v, sub in l[8]]      # (effect, verse, subject, line kind) — a reuse is a further entry on the named ledger
CELLS = {'F1': 'the_witnesses_and_the_rock', 'F2': 'the_crooked_generation', 'F3': 'the_nations_divided_and_the_portion', 'F4': 'the_desert_and_the_eagle', 'F5': 'the_heights_and_the_feast', 'F6': 'jeshurun_fat_and_the_demons',
         'F7': 'the_hidden_face_and_the_fire', 'F8': 'the_evils_heaped', 'F9': 'the_enemys_boast', 'F10': 'the_joined_thousand_and_the_vine_of_sodom', 'F11': 'the_cup_in_store_and_the_vengeance', 'F12': 'i_am_he_and_the_land_atones',
         'F13': 'the_song_spoken_with_hoshea', 'F14': 'the_charge_after_the_song', 'F15': 'the_summons_to_nebo', 'F16': 'meribah_and_the_seeing'}
# NO MARKER — the song and its frame stand on 19b's marker at 31:1 (Moses' last day (40, 12, 7): the year the ink's, the day the answer sheet's — Tosefta Sotah 11:3); 32:48's
# 'that selfsame day' names that day (337:1's three seats — the flood's boarding Genesis 7:13, the exodus Exodus 12:41/51, the summons); the counter does not move; markers 173 UNMOVED
MARKER = None
DAY = (40, 12, 7)
# THE PARSER'S TWO GUARDS (the reading's lessons 8 — the spine's own arithmetic the oracle): DATA rows of the runner, no ledger write
GUARDS = {'the_false_eight': "32:15 'you grew fat' (shamanta) read by the parser as the number eight — a verb, not a count: Onkelos 'you prospered' (atzlach), the Sifrei 318:4-5's dated reading (the fat of the generation before the exile) — FALSE, no write",
          'the_joined_thousand': "32:30 'one chase a thousand, two put ten thousand to flight' read by the parser as [1, 1002] — the thousand and the two joined, the ten thousand uncounted: the Sifrei 322:10 reads the four numbers aloud (one, a thousand, two, ten thousand) and 322:12 the proverb's arithmetic; Leviticus 26:8's five and a hundred the tape's kin — a proverb, not a count in the world; no write"}
# THE KIN'S COUNTS as the callees read them (ch32_callees.out THE NEAR NAMES) — the references UNMOVED after the run; the reuses MOVED by their entries
KIN_UNMOVED = {'barred_from_the_land': 2, 'gathered_to_his_people': 5, 'became_the_lords_people_this_day': 2, 'lord_declared_israel_treasure_people': 1, 'treasured_people': 1, 'other_gods_barred': 1, 'manna_provided': 1,
               'water_from_the_rock': 2, 'eagle_nation_devours': 1, 'few_in_number_left': 1, 'scattered_among_all_peoples': 1, 'serving_wood_and_stone_among_nations': 1, 'sold_and_none_buys': 1, 'sons_flesh_eaten_in_siege': 1,
               'pestilence_cleaving': 1, 'sword_blight_mildew_sent': 1, 'trembling_heart_no_rest': 1, 'plagues_made_wonderful': 1, 'innocent_blood_atoned': 1, 'two_witnesses_required': 1, 'two_or_three_witnesses_required': 1,
               'one_witness_barred': 1, 'witnesses_inquiry_commanded': 1, 'plotting_witness_talion_commanded': 1, 'song_sung': 1, 'song_writing_commanded': 1, 'song_taught_and_put_in_mouths_commanded': 1,
               'song_a_witness_against_israel': 1, 'song_written_and_taught_by_moses': 1, 'song_spoken_to_the_assembly_to_its_end': 1, 'book_a_witness_against_israel': 1, 'future_whoring_after_foreign_gods_foretold': 1,
               'covenant_breaking_foretold': 1, 'evils_and_troubles_befall_foretold': 1, 'corruption_after_moses_death_foretold': 1, 'moses_to_sleep_with_the_fathers': 1, 'moses_days_approach_to_die': 1,
               'joshua_commissioned_to_bring_israel_in': 1, 'land_brimstone_salt_like_sodom': 1, 'hidden_things_the_lords': 1, 'shema_commanded': 1, 'hakhel_children_hear_and_learn_commanded': 1, 'serpents_sent': 1,
               'healed': 2, 'atoned_forgiven': 7, 'sevenfold_vengeance': 1, 'blood_required': 1, 'scattered': 1, 'building_ceased': 1, 'no_share_in_the_world_to_come': 3, 'only_noah_remained': 1, 'famine': 3,
               'rain_in_its_season': 2, 'heavens_good_treasure_opened': 1, 'curses_of_the_book_on_the_idolater': 1, 'hidden_idolater_unpardoned': 1, 'heart_turning_to_other_gods_barred': 1, 'enemies_flee_seven_ways': 1,
               'smitten_before_enemies_seven_ways': 1, 'nations_dispossessed_as_sihon_and_og_promised': 1, 'holy_people_promised': 1, 'established_holy_people': 1}
REUSE_BEFORE = {'heaven_and_earth_witness': 4, 'face_hidden_and_forsaken_foretold': 1, 'length_of_days_on_the_land_promised': 1}
import collections as _c
_rc = _c.Counter(e for e, _, _, _ in REUSES)
REUSE_AFTER = {e: REUSE_BEFORE[e] + _rc[e] for e in REUSE_BEFORE}
# THE EDGES from the runner — every one REFERENCE (the ink names the kin's institution or event, or the kin's cell names THIS chapter's verse forward); the registration edge and the census's FALSE and VIA edges filed at RUN B from the gate's print
EDGES = ['obey_horeb', 'covenant_return_charge', 'good_land', 'exodus_story', 'refuge_war_family', 'persons_poor_court', 'courts_prophet', 'refuge', 'ordinances', 'chukat', 'opening_speech', 'journeys', 'second_tablets', 'primeval',
         'pre_sinai', 'mamre', 'family', 'balak', 'beha', 'shelach', 'not_righteousness', 'seven_nations', 'hear_o_israel', 'blessing_and_curse', 'firstfruits_ebal_curses', 'tochacha', 'seducers', 'decalogue', 'covenant_at_horeb',
         'naso', 'incense_shekel', 'festivals_judges', 'holiness', 'vows', 'food_tithe', 'gad_reuben', 'borders', 'erection', 'sanctions', 'vayikra5', 'moadim', 'mekoshesh']
POINTERS_PREDICTED = [('Deut 32:50', "as Aaron your brother died in Mount Hor and was gathered to his people — the tape's own entries at Numbers 20:28 and 33:38 (chukat.edom_and_hor, journeys.aarons_death_retold by CALL): RUN_CITATION")]
STATE_ROWS = ['Deut 32:30']        # the condition's two arms (323:5 — the Torah done, one chases a thousand; undone, the reversal; Leviticus 26:8 the promise's seat)
POINTER_ROWS = []                  # no owed pointer paid here; 32:50's run citation a reference row
CAL_NEW = []                       # no clock word in the song; the selfsame day the marker's
DATA_ROWS = ['the_false_eight', 'the_joined_thousand', 'the_witnesses_chain_fifth_seat', 'the_rule_of_war_and_famine', 'the_name_profaned_at_once', 'the_things_without_measure', 'the_mountains_by_a_hair', 'the_seven_commandments_of_the_nations',
             'the_camps_twelve_mil', 'the_song_spoken_twice', 'the_selfsame_day_seats', 'aarons_death_the_receipt', 'moses_death_ahead', 'the_response_to_the_name', 'the_measure_for_measure', 'the_no_ransom', 'the_readback']
PARAMS = ['the_things_without_measure', 'the_mountains_by_a_hair', 'the_response_to_the_name', 'the_shemas_evening_time', 'the_witnesses_examinations', 'the_enemy_disqualified', 'the_measure_for_measure', 'the_clusters_ceased',
          'the_seven_commandments_of_the_nations', 'the_camps_twelve_mil', 'the_fruit_of_deeds', 'the_ten_utterances', 'the_twilight_creations', 'the_five_acquisitions', 'the_shekhinah_among_ten', 'the_place_of_torah',
          'the_idols_treatment', 'the_burned_and_the_beheaded', 'the_storekeepers_ledger', 'the_vows_substitutes', 'the_peah_from_the_beginning', 'the_striped_field', 'the_seed_bed', 'the_rule_of_war_and_famine', 'the_name_profaned_at_once']
MISHNAH = [('Avodah Zarah', 3, 4), ('Avot', 3, 6), ('Avot', 5, 1), ('Avot', 5, 6), ('Avot', 6, 9), ('Avot', 6, 10), ('Berakhot', 1, 1), ('Berakhot', 2, 2), ('Berakhot', 7, 1), ('Berakhot', 8, 8), ('Chagigah', 1, 8), ('Kilayim', 3, 2),
           ('Nedarim', 1, 2), ('Peah', 1, 1), ('Peah', 3, 2), ('Sanhedrin', 3, 5), ('Sanhedrin', 5, 2), ('Sanhedrin', 9, 1), ('Shevuot', 7, 5), ('Sotah', 1, 7), ('Sotah', 9, 9)]
# CORRECTED FROM THE EXAM WRITER'S PRINT (RUN A): Mishnah Peah 1:3 was counted at the first print by the regex reading 'Peah 1:3' INSIDE 'Tosefta Peah 1:3' (324:2) — not cited by the ledger; read whole at the design and EXCLUDED (the exam file's EXCL row); 22 -> 21 Mishnah rows — a departure from the design as written, recorded for the AS BUILT
MISHNAH_EXCLUDED = [('Peah', 1, 3)]
TOSEFTA = [('Tosefta Arakhin', 1, 4), ('Tosefta Avodah Zarah', 9, 4), ('Tosefta Peah', 1, 1), ('Tosefta Peah', 1, 2), ('Tosefta Peah', 1, 3)]
RENUMBER = {('Tosefta Arakhin', 1, 10): ('Tosefta Arakhin', 1, 4), ('Tosefta Avodah Zarah', 8, 4): ('Tosefta Avodah Zarah', 9, 4)}   # the ledger's (the translator's) paragraph -> the export's (found by the rows' own words)
TOSEFTA_NOTE = ("the ledger names 'Tosefta Arakhin 1:10' (313:9 — the camp's twelve mil) and 'Tosefta Avodah Zarah 8:4' (322:11 — the nations' seven commandments), the translator's paragraph numbers; the export's chapter 1 of Arakhin "
                "has six paragraphs and the twelve mil stand in 1:4 (the chapter read whole to find it), the seven commandments in Avodah Zarah 9:4 (found by the words 'seven commandments' over the whole tractate — chapter 8 of the export "
                "holds the hired worker and the libation wine); 'Tosefta Peah 1:1' (336:1) and '1:3' (324:2) as cited, 1:2 the paragraph between them read whole with them — 19b's lesson: the translator's paragraph number differs from the export's")
TALMUD_OWED = ['Avodah Zarah 18a (32:4 — the mourner\'s justification, the Rock whose work is perfect)', 'Bava Kamma 60b (321:9 — the rule of war and famine: the sword without, gather within)', 'Eruvin 54a-b (32:2 — the doctrine as rain, the order of teaching)',
               'Gittin 56b (the enemy\'s boast — "our hand is exalted")', 'Pesachim 68a and Sanhedrin 91b (32:39 — "I kill and I make alive", the resurrection)', 'Taanit 11a (32:4 — the Rock\'s judgment)', 'Yoma 86a (328:4 — the Name profaned punished at once)']
def counts():
    ops = _c.Counter(op for _, op, _ in NEW_E); subs = _c.Counter(sub for _, _, sub in NEW_E); rsubs = _c.Counter(sub for _, _, sub, _ in REUSES); forms = _c.Counter(l[5] for l in LINES)
    return {'lines': len(LINES), 'new_effects': len(NEW_EFFECTS), 'distinct': len(set(NEW_EFFECTS)), 'ops': dict(ops), 'reuses': len(REUSES), 'writes': len(NEW_EFFECTS) + len(REUSES), 'edges': len(EDGES), 'params': len(PARAMS),
            'mishnah': len(MISHNAH), 'tosefta': len(TOSEFTA), 'per_line': [(l[1], len(l[7]) + len(l[8])) for l in LINES], 'cells': len(CELLS), 'subjects_new': dict(subs), 'subjects_reuse': dict(rsubs), 'forms': dict(forms),
            'writes_by_subject': dict(subs + rsubs), 'fields': sum(len(l[6]) for l in LINES), 'data_rows': len(DATA_ROWS), 'kin': len(KIN_UNMOVED), 'guards': len(GUARDS)}
if __name__ == '__main__':
    import os, sys, yaml
    c = counts(); print(c)
    assert c['new_effects'] == c['distinct'], 'a name twice'
    assert len(set(KINDS)) == len(KINDS)
    assert set(REUSE_AFTER) == set(REUSE_BEFORE) and all(REUSE_AFTER[e] > REUSE_BEFORE[e] for e in REUSE_BEFORE)
    assert all(l[4] in CELLS for l in LINES) and len(set(l[4] for l in LINES)) == len(CELLS)
    assert set(RENUMBER.values()) <= set(TOSEFTA)
    ROOT = os.popen('git rev-parse --show-toplevel').read().strip(); S9 = ROOT + '/World/step9'
    fx = yaml.safe_load(open(S9 + '/effect_vocabulary.yaml', encoding='utf-8'))['effects']; ev = yaml.safe_load(open(S9 + '/event_vocabulary.yaml', encoding='utf-8'))['events']
    coll_e = [e for e in NEW_EFFECTS if e in fx]; coll_k = [k for k in KINDS if k in ev]
    print('COLLISIONS: effects present before', coll_e, '| kinds present before', coll_k)
    assert not coll_e and not coll_k, 'a new name already in a registry'
    assert all(e in fx for e in REUSE_BEFORE) and all(e in fx for e in KIN_UNMOVED), ('a reuse or kin name not in the registry', [e for e in list(REUSE_BEFORE) + list(KIN_UNMOVED) if e not in fx])
    print('FIRST VERSES', [l[1] for l in LINES]); print('WRITES PER LINE (new + reuse)', c['per_line']); print('REUSE_AFTER', REUSE_AFTER)
    print('SPEC OK')
