#!/usr/bin/env python3
# THE DEUTERONOMY WALK 18b (2026-09-26): THE SPEC MODULE — the compile's names fixed ONCE at the design and read by every later script (the design writer, the
# probe patch, the exam writer, the types, the runner's parts, the checkpoints): the runner, the daemon, the span, the twenty-one own-day lines with their kinds and
# fields, the ninety-one NEW effects with their ops, the five REUSES, the kin's references with their counts as the recon and the callees read them, the parameters,
# the edges, the Mishnah rows. Nothing here is a verdict — the verdicts are the runner's cells'. RUN FROM THE REPO ROOT with PYTHONPATH the scratchpad.
RUNNER = 'firstfruits_ebal_curses'            # the 75th runner: the first fruits (26), Ebal's ceremony (27), the blessings and the curses (28)
DAEMON = 'law_firstfruits_ebal_curses'        # the 80th daemon; I5 79 -> 80
GIVEN_AT = 'Deut 26:1'; INSTALLED_BY = 'boot'
SPAN = [['Deut', 26, 1, 19], ['Deut', 27, 1, 26], ['Deut', 28, 1, 69]]
UNITS = {'deu_26_bikkurim_close': 'DV26', 'deu_27_ebal_curses': 'DV27', 'deu_28_blessings': 'DV28A', 'deu_28_curses_a': 'DV28B', 'deu_28_curses_b': 'DV28C'}
CORPUS = ('deu_26_bikkurim_close (STEP_Dt_26_1 through STEP_Dt_26_19; claims DV26-01 through DV26-03), deu_27_ebal_curses (STEP_Dt_27_1 through STEP_Dt_27_26; claims DV27-01 through DV27-04), '
          'deu_28_blessings (STEP_Dt_28_1 through STEP_Dt_28_14; claims DV28A-01 through DV28A-04), deu_28_curses_a (STEP_Dt_28_15 through STEP_Dt_28_44; claims DV28B-01 through DV28B-05) and '
          'deu_28_curses_b (STEP_Dt_28_45 through STEP_Dt_28_69; claims DV28C-01 through DV28C-05)')
S, B, H = 'status', 'block', 'heaven'
# THE LINES: (kind, first verse, verse range, claim, cell, fields, [(effect, op)], [reuses])
LINES = [
 ('first_fruits_declared', 'Deut 26:1', '26:1-11', 'DV26-01', 'F1', ['when_you_come_into_the_land_and_dwell_in_it', 'the_first_of_all_the_fruit_in_a_basket_to_the_place', 'i_declare_this_day_to_the_priest', 'the_recital_a_wandering_aramean', 'set_it_down_bow_and_rejoice_with_the_levite_and_the_stranger'],
  [('first_fruits_basket_commanded', S), ('first_fruits_declaration_commanded', S), ('first_fruits_recital_commanded', S), ('first_fruits_set_before_altar_commanded', S)], [('rejoicing_before_the_lord_commanded', 'Deut 26:11')]),
 ('tithe_confession_declared', 'Deut 26:12', '26:12-15', 'DV26-02', 'F2', ['when_you_have_finished_tithing_in_the_third_year', 'given_to_the_levite_the_stranger_the_orphan_and_the_widow', 'i_have_removed_the_holy_from_the_house', 'not_in_mourning_not_in_uncleanness_not_for_the_dead', 'look_down_and_bless'],
  [('tithe_removal_commanded', S), ('tithe_confession_commanded', S), ('tithe_in_mourning_barred', B), ('tithe_in_uncleanness_barred', B), ('tithe_for_the_dead_barred', B)], [('poor_tithe_owed', 'Deut 26:12')]),
 ('covenant_formula_declared', 'Deut 26:16', '26:16-19', 'DV26-03', 'F3', ['this_day_the_lord_commands_you_to_do_these_statutes', 'the_lord_you_have_declared_this_day_to_be_your_god', 'the_lord_has_declared_you_this_day_his_treasured_people', 'high_above_all_nations_a_holy_people_as_he_spoke'],
  [('statutes_this_day_commanded', S), ('israel_declared_the_lord_god', S), ('lord_declared_israel_treasure_people', S), ('high_above_all_nations_promised', H), ('holy_people_promised', H)], []),
 ('stones_altar_declared', 'Deut 27:1', '27:1-8', 'DV27-01', 'F4', ['moses_and_the_elders_keep_all_the_commandment', 'great_stones_plastered_on_the_day_you_cross', 'all_the_words_of_this_law_written_on_them', 'an_altar_of_whole_stones_on_ebal_no_iron', 'burnt_and_peace_offerings_eat_and_rejoice_very_plainly'],
  [('great_stones_commanded', S), ('stones_plastered_written_commanded', S), ('whole_stones_altar_commanded', S), ('iron_on_altar_barred', B), ('ebal_offerings_commanded', S), ('law_written_very_plainly_commanded', S)], [('rejoicing_before_the_lord_commanded', 'Deut 27:7')]),
 ('people_this_day_declared', 'Deut 27:9', '27:9-10', 'DV27-02', 'F5', ['moses_and_the_priests_the_levites_be_silent_and_hear', 'this_day_you_have_become_a_people_to_the_lord', 'hearken_to_his_voice_and_do_his_commandments'],
  [('became_the_lords_people_this_day', S), ('hearken_and_do_commanded', S)], []),
 ('gerizim_ebal_tribes_declared', 'Deut 27:11', '27:11-13', 'DV27-03', 'F6', ['moses_commanded_the_people_that_day', 'these_shall_stand_to_bless_on_gerizim_the_six', 'these_shall_stand_for_the_curse_on_ebal_the_six'],
  [('six_tribes_on_gerizim_to_bless', S), ('six_tribes_on_ebal_for_the_curse', S)], []),
 ('twelve_curses_declared', 'Deut 27:14', '27:14-26', 'DV27-04', 'F7', ['the_levites_answer_every_man_of_israel_with_a_loud_voice', 'cursed_the_man_the_twelve', 'and_all_the_people_shall_say_amen'],
  [('levites_loud_voice_commanded', S), ('image_maker_cursed', S), ('parent_dishonorer_cursed', S), ('landmark_mover_cursed', S), ('blind_misleader_cursed', S), ('judgment_perverter_cursed', S), ('fathers_wife_lier_cursed', S), ('beast_lier_cursed', S), ('sister_lier_cursed', S), ('mother_in_law_lier_cursed', S), ('secret_smiter_cursed', S), ('bribe_for_blood_taker_cursed', S), ('law_non_upholder_cursed', S), ('amen_answered_commanded', S)], []),
 ('blessings_condition_declared', 'Deut 28:1', '28:1-6', 'DV28A-01', 'F8', ['if_you_diligently_hearken_all_these_blessings', 'blessed_in_the_city_and_in_the_field', 'blessed_the_fruit_of_womb_ground_and_beast', 'blessed_your_basket_and_your_kneading_trough', 'blessed_coming_in_and_going_out'],
  [('blessed_in_city_and_field', H), ('blessed_fruit_of_womb_ground_beast', H), ('blessed_basket_and_trough', H), ('blessed_coming_in_and_going_out', H)], [('blessings_for_hearing', 'Deut 28:1')]),
 ('enemies_storehouses_blessing_declared', 'Deut 28:7', '28:7-8', 'DV28A-02', 'F8', ['your_enemies_come_one_way_and_flee_seven', 'the_blessing_in_your_storehouses'],
  [('enemies_flee_seven_ways', H), ('storehouses_blessed', H)], []),
 ('holy_people_fear_declared', 'Deut 28:9', '28:9-10', 'DV28A-03', 'F8', ['established_a_holy_people_if_you_keep_and_walk', 'all_the_peoples_shall_see_the_name_on_you_and_fear'],
  [('established_holy_people', H), ('peoples_fear_israel', H)], []),
 ('heavens_treasure_lending_declared', 'Deut 28:11', '28:11-14', 'DV28A-04', 'F8', ['plenteous_in_goods_womb_beast_and_ground', 'the_heavens_his_good_treasure_opened_rain_in_its_season', 'you_shall_lend_and_not_borrow', 'the_head_and_not_the_tail', 'turn_not_aside_right_or_left'],
  [('heavens_good_treasure_opened', H), ('lend_not_borrow', H), ('head_not_tail', H), ('turning_aside_barred', B)], [('rain_in_its_season', 'Deut 28:12')]),
 ('curses_condition_declared', 'Deut 28:15', '28:15-19', 'DV28B-01', 'F9', ['if_you_will_not_hearken_all_these_curses', 'cursed_in_the_city_and_in_the_field', 'cursed_your_basket_and_your_kneading_trough', 'cursed_the_fruit_of_womb_ground_and_beast', 'cursed_coming_in_and_going_out'],
  [('curses_for_not_hearkening', H), ('cursed_in_city_and_field', H), ('cursed_basket_and_trough', H), ('cursed_fruit_of_womb_ground_beast', H), ('cursed_coming_in_and_going_out', H)], []),
 ('curse_diseases_brass_declared', 'Deut 28:20', '28:20-24', 'DV28B-02', 'F9', ['the_curse_the_confusion_and_the_rebuke', 'pestilence_consumption_fever_inflammation', 'sword_blight_and_mildew', 'heavens_brass_earth_iron_rain_dust'],
  [('curse_confusion_rebuke_sent', H), ('pestilence_cleaving', H), ('consumption_fever_inflammation_sent', H), ('sword_blight_mildew_sent', H), ('heavens_brass_earth_iron', H), ('rain_turned_to_dust', H)], []),
 ('defeat_carcass_boil_madness_declared', 'Deut 28:25', '28:25-29', 'DV28B-03', 'F9', ['smitten_before_your_enemies_one_way_out_seven_fleeing', 'your_carcass_food_for_the_birds', 'the_boil_of_egypt_hemorrhoids_scab_and_itch', 'madness_blindness_and_astonishment_of_heart'],
  [('smitten_before_enemies_seven_ways', H), ('carcass_food_for_birds', H), ('boil_of_egypt_hemorrhoids_scab_itch', H), ('madness_blindness_astonishment', H)], []),
 ('wife_house_vineyard_king_taken_declared', 'Deut 28:30', '28:30-37', 'DV28B-04', 'F9', ['a_wife_a_house_a_vineyard_another_takes', 'your_ox_your_ass_your_flock_taken', 'sons_and_daughters_to_another_people', 'the_fruit_of_your_ground_eaten_by_a_people_you_know_not', 'sore_boils_from_sole_to_crown', 'carried_with_your_king_to_serve_wood_and_stone', 'an_astonishment_a_proverb_and_a_byword'],
  [('wife_house_vineyard_taken', H), ('ox_ass_flock_taken', H), ('sons_daughters_given_to_another_people', H), ('fruit_eaten_by_unknown_nation', H), ('sore_boils_sole_to_crown', H), ('exiled_with_king_to_serve_wood_and_stone', H), ('astonishment_proverb_byword', H)], []),
 ('harvests_failed_stranger_head_declared', 'Deut 28:38', '28:38-44', 'DV28B-05', 'F9', ['seed_vines_and_olives_lost_to_locust_worm_and_dropping', 'sons_and_daughters_into_captivity', 'the_stranger_rises_the_head_and_you_the_tail_he_lends_to_you'],
  [('seed_vines_olives_lost', H), ('sons_daughters_into_captivity', H), ('stranger_head_israel_tail', H)], []),
 ('curses_pursue_iron_yoke_declared', 'Deut 28:45', '28:45-48', 'DV28C-01', 'F10', ['all_these_curses_pursue_you_until_you_are_destroyed', 'because_you_served_not_with_joy', 'serve_your_enemies_in_hunger_thirst_nakedness_and_want_an_iron_yoke'],
  [('curses_pursue_until_destroyed', H), ('iron_yoke_on_neck', H), ('enemies_served_in_want', H)], []),
 ('eagle_nation_siege_declared', 'Deut 28:49', '28:49-52', 'DV28C-02', 'F10', ['a_nation_from_the_end_of_the_earth_as_the_eagle_flies', 'it_eats_the_fruit_of_your_beast_and_your_ground', 'besieges_you_in_all_your_gates_until_the_high_walls_fall'],
  [('eagle_nation_devours', H), ('siege_in_all_gates_walls_fall', H)], []),
 ('sons_flesh_siege_declared', 'Deut 28:53', '28:53-57', 'DV28C-03', 'F10', ['you_eat_the_fruit_of_your_own_womb_in_the_siege_and_the_distress', 'the_tender_man_and_the_delicate_woman_grudge_their_children'],
  [('sons_flesh_eaten_in_siege', H)], []),
 ('plagues_scattered_declared', 'Deut 28:58', '28:58-64', 'DV28C-04', 'F10', ['if_you_keep_not_all_the_words_of_this_law_written_in_this_book', 'plagues_made_wonderful_the_diseases_of_egypt_returned', 'left_few_in_number_as_he_rejoiced_so_he_rejoices_to_destroy', 'scattered_among_all_peoples_to_serve_wood_and_stone'],
  [('plagues_made_wonderful', H), ('diseases_of_egypt_returned', H), ('few_in_number_left', H), ('scattered_among_all_peoples', H), ('serving_wood_and_stone_among_nations', H)], []),
 ('trembling_ships_covenant_declared', 'Deut 28:65', '28:65-69', 'DV28C-05', 'F10', ['no_rest_for_the_sole_of_your_foot_a_trembling_heart', 'your_life_hangs_in_doubt_morning_and_evening', 'back_to_egypt_in_ships_sold_and_none_buys', 'these_are_the_words_of_the_covenant_in_the_land_of_moab_besides_horeb'],
  [('trembling_heart_no_rest', H), ('life_hanging_in_doubt', H), ('returned_to_egypt_in_ships', H), ('sold_and_none_buys', H), ('covenant_words_in_moab_declared', S)], []),
]
KINDS = [l[0] for l in LINES]
NEW_E = [(e, op) for l in LINES for e, op in l[6]]
NEW_EFFECTS = [e for e, _ in NEW_E]
REUSES = [(e, v, l[0]) for l in LINES for e, v in l[7]]           # (effect, verse, line kind) — a reuse is a SECOND (third, fourth) entry on israel_people
CELLS = {'F1': 'the_first_fruits', 'F2': 'the_removal_and_the_confession', 'F3': 'the_covenant_formula', 'F4': 'the_stones_and_the_altar', 'F5': 'the_people_this_day', 'F6': 'the_six_and_the_six',
         'F7': 'the_twelve_curses', 'F8': 'the_blessings', 'F9': 'the_curses_of_the_house_and_the_field', 'F10': 'the_curses_of_the_siege_and_the_exile'}
# THE KIN'S COUNTS as the recon (section H) and the callees (THE NEAR NAMES) read them — the references UNMOVED after the run; the reuses MOVED by their entries
KIN_UNMOVED = {'gerizim_ebal_ceremony_owed': 1, 'blessing_and_curse_set': 1, 'heavens_shut_for_turning': 1, 'treasured_people': 1, 'second_tithe_owed': 1, 'levite_forsaking_barred': 2, 'three_pilgrimages_commanded': 1,
               'work_of_the_hand_blessed': 2, 'bribe_barred': 1, 'landmark_removal_barred': 1, 'stranger_orphan_justice_commanded': 1, 'fathers_wife_barred': 1, 'return_to_egypt_barred': 1, 'horses_multiplying_barred': 1,
               'heaven_and_earth_witness': 2, 'forgetting_barred': 1, 'house_abomination_barred': 1, 'israel_hears_and_fears': 1, 'shema_commanded': 1, 'covenant_cut': 3, 'covenant_declared': 1, 'entered_the_covenant': 3,
               'seed_as_stars': 3, 'enslaved': 2, 'cry_heard': 2, 'plague_struck': 13, 'molten_image_barred': 1, 'yoke_of_the_commandments_accepted': 1, 'bless_after_eating_commanded': 1, 'first_fleece_owed': 1,
               'scattered_among_nations': 0, 'land_desolate': 0, 'chastised_sevenfold': 0, 'sabbath_debt': 0, 'put_to_death': 7, 'stoned': 2, 'terumah_of_the_tithe_owed': 1, 'tithe_granted': 1, 'confessed': 3, 'altar_built': 8}
REUSE_BEFORE = {'rejoicing_before_the_lord_commanded': 2, 'poor_tithe_owed': 1, 'blessings_for_hearing': 2, 'rain_in_its_season': 1}
REUSE_AFTER = {'rejoicing_before_the_lord_commanded': 4, 'poor_tithe_owed': 2, 'blessings_for_hearing': 3, 'rain_in_its_season': 2}
# THE EDGES from the runner — every one REFERENCE (the ink names the kin's institution, or the kin's cell names THIS chapter's verse forward); the registration edge and the census's FALSE edges filed at RUN B from the gate's print
EDGES = ['food_tithe', 'release_firstborn', 'blessing_and_curse', 'seven_nations', 'place_name', 'festivals_judges', 'persons_poor_court', 'refuge_war_family', 'sanctions', 'mishpatim_3', 'holiness', 'second_tablets',
         'courts_prophet', 'obey_horeb', 'good_land', 'covenant_at_horeb', 'hear_o_israel', 'decalogue', 'ordinances', 'exodus_story', 'korach', 'calendar', 'chukat', 'tochacha', 'naso', 'joseph', 'primeval', 'seducers',
         'borders', 'priesthood', 'chatat', 'opening_speech', 'journeys', 'sanctuary_build']
POINTER_PAID = {'verse': 'Deut 15:6', 'runner': 'release_firstborn', 'from': ('OWED', 'hypothesis'), 'to': ('REVERSE', 'reference'), 'taught_by': 'the Sifrei on Deuteronomy 116:1 (read whole at sittings 13 and 18)'}
POINTERS_PREDICTED = [('Deut 26:18', 'as He spoke to you — Exodus 19:5-6 the treasure (RUN_CITATION)'), ('Deut 26:19', 'as He spoke — 7:6 and 14:2 the holy people (RUN_CITATION)'), ('Deut 27:3', 'as the LORD God of your fathers spoke to you — 6:3 (RUN_CITATION)'),
                      ('Deut 28:9', 'as He swore to you — the oath to the fathers (RUN_CITATION)'), ('Deut 28:68', 'by the way of which I said to you — 17:16 (RUN_CITATION)')]
CAL_NEW = ['the_first_fruits_window', 'the_confessions_hour']
PARAMS = ['the_first_fruits_window', 'the_species', 'the_bringers_and_the_reciters', 'the_setting_aside', 'the_replacement', 'the_baskets', 'the_temple_condition', 'the_removal_date', 'the_confessions_hour', 'the_confessions_clauses',
          'the_order_of_the_tithes', 'the_confessors', 'the_measures_at_the_floor', 'the_things_without_measure', 'the_tongue', 'the_ceremonys_form', 'the_seventy_languages', 'the_curses_scope', 'the_labors_third_state']
MISHNAH = [('Bikkurim', 1, 1), ('Bikkurim', 1, 2), ('Bikkurim', 1, 3), ('Bikkurim', 1, 4), ('Bikkurim', 1, 5), ('Bikkurim', 1, 6), ('Bikkurim', 1, 8), ('Bikkurim', 1, 10), ('Bikkurim', 2, 4), ('Bikkurim', 3, 1), ('Bikkurim', 3, 4), ('Bikkurim', 3, 7), ('Bikkurim', 3, 8),
           ('Maaser Sheni', 5, 6), ('Maaser Sheni', 5, 10), ('Maaser Sheni', 5, 11), ('Maaser Sheni', 5, 12), ('Maaser Sheni', 5, 13), ('Maaser Sheni', 5, 14), ('Peah', 1, 1), ('Peah', 4, 11), ('Peah', 8, 5), ('Sotah', 7, 1), ('Sotah', 7, 2), ('Sotah', 7, 5), ('Terumot', 11, 3)]
MISHNAH_EXCLUDED = [('Yevamot', 12, 3, "cited by 291:7 alone — the EXCLUDED row (25:9's own words, the English's misprint 'Dt.27:9'): read whole, 17b's exam holds it (F14 the levirate), NOT a case here")]
NOT_MISHNAH = [('Shekalim', 3, 24, 'Tosefta Shekalim 3:24 — no Temple, no first fruits: the daemon\'s own guard (the_temple_condition); no Mishnah row of that number (chapter 3 has four)')]
def counts():
    import collections
    ops = collections.Counter(op for _, op in NEW_E)
    return {'lines': len(LINES), 'new_effects': len(NEW_EFFECTS), 'distinct': len(set(NEW_EFFECTS)), 'ops': dict(ops), 'reuses': len(REUSES), 'writes': len(NEW_EFFECTS) + len(REUSES), 'edges': len(EDGES), 'params': len(PARAMS),
            'mishnah': len(MISHNAH), 'per_line': [(l[1], len(l[6]) + len(l[7])) for l in LINES], 'cells': len(CELLS)}
if __name__ == '__main__':
    c = counts(); print(c)
    assert c['new_effects'] == c['distinct'], 'a name twice'
    assert len(set(KINDS)) == len(KINDS)
    print('FIRST VERSES', [l[1] for l in LINES]); print('WRITES PER LINE (new + reuse)', c['per_line'])
    print('SPEC OK')
