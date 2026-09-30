#!/usr/bin/env python3
# THE DEUTERONOMY WALK 21b (2026-09-29): THE SPEC MODULE — the compile's names fixed ONCE at the design and read by every later script (the design writer, the
# probe patch, the exam writer, the types, the runner's parts, the checkpoints): the runner, the daemon, the span, the eleven own-day lines with their kinds, forms and
# fields, the twenty-eight NEW effects with their ops and their subjects (Israel's ledger and THE TRIBES' OWN — the sons' entities Genesis 49's testament wrote on), NO REUSE,
# NO MARKER (the blessing stands on 19b's marker — Moses' last day (40, 12, 7)), the kin's references with their counts as the callees read them, the parameters (the answer
# sheet's rows), the DATA rows (the parser's false seven among them), the edges, the Mishnah and Tosefta rows with the regex's misreads and the export's holes named.
# Nothing here is a verdict — the verdicts are the runner's cells'. ch32b_spec.py's form over chapter 33. RUN FROM THE REPO ROOT with PYTHONPATH the scratchpad.
RUNNER = 'blessing_of_moses'                 # the 78th runner: the blessing (33:1-29) — the frame, the prologue, the eleven tribes' blessings, the coda
DAEMON = 'law_blessing_of_moses'             # the 83rd daemon; I5 82 -> 83
GIVEN_AT = 'Deut 33:1'; INSTALLED_BY = 'boot'
SPAN = [['Deut', 33, 1, 29]]
UNITS = {'deu_33_ve_zot': 'DV33'}
CORPUS = 'deu_33_ve_zot (STEP_Dt_33_1 through STEP_Dt_33_29; claims DV33-01 through DV33-11)'
S, B, H = 'status', 'block', 'heaven'
I, MO = 'israel_people', 'moses'
RE_, JU, LV, BN, JO, ZB, IS, GD, DN, NP, AS = 'reuben', 'judah', 'levi', 'benjamin', 'joseph', 'zebulun', 'issachar', 'gad', 'dan_son', 'naphtali', 'asher'
# THE LINES: (kind, first verse, verse range, claim, cell, form, fields, [(effect, op, subject)], [(reuse effect, verse, subject)]) — ONE PER CLAIM (18b's form): the frame an
# ACT (Moses blessed Israel before his death — 33:1 with the theophany's opening 33:2), the prologue and the ten blessings SPEECHES (Moses' words; Simeon named nowhere, no
# write), the coda two speeches; every line at Moses' last day (40, 12, 7) after 19b's marker — NO MARKER HERE ('before his death' the frame's own word)
LINES = [
 ('moses_blessed_israel_before_his_death', 'Deut 33:1', '33:1-2', 'DV33-01', 'F1', 'act', ['and_this_is_the_blessing_which_moses_the_man_of_god_blessed_the_children_of_israel_before_his_death', 'the_lord_came_from_sinai_and_rose_from_seir_unto_them_he_shone_from_mount_paran', 'he_came_from_the_myriads_of_holy_ones_at_his_right_hand_a_fiery_law_unto_them'],
  [('blessing_given_before_moses_death', S, I), ('the_lord_came_from_sinai_seir_paran_declared', S, I), ('fiery_law_from_his_right_hand_declared', S, I)], []),
 ('blessing_prologue_law_and_king_declared', 'Deut 33:3', '33:3-5', 'DV33-02', 'F2', 'speech', ['he_loves_the_peoples_all_his_holy_ones_are_in_your_hand_they_sat_down_at_your_feet_receiving_of_your_words', 'moses_commanded_us_a_law_the_inheritance_of_the_congregation_of_jacob', 'there_was_a_king_in_jeshurun_when_the_heads_of_the_people_gathered_the_tribes_of_israel_together'],
  [('lover_of_the_peoples_holy_ones_in_his_hand_declared', S, I), ('law_commanded_the_inheritance_of_jacob_declared', S, I), ('king_in_jeshurun_when_the_heads_gathered_declared', S, I)], []),
 ('blessing_reuben_and_judah_declared', 'Deut 33:6', '33:6-7', 'DV33-03', 'F3', 'speech', ['let_reuben_live_and_not_die_and_let_his_men_be_a_number', 'hear_lord_the_voice_of_judah_and_bring_him_to_his_people', 'his_hands_shall_contend_for_him_and_you_shall_be_a_help_against_his_adversaries'],
  [('reuben_to_live_and_not_die_blessed', S, RE_), ('judahs_voice_heard_brought_to_his_people_blessed', S, JU)], []),
 ('blessing_levi_declared', 'Deut 33:8', '33:8-11', 'DV33-04', 'F4', 'speech', ['your_thummim_and_your_urim_be_with_your_pious_man_whom_you_proved_at_massah_and_strove_with_at_the_waters_of_meribah', 'who_said_of_his_father_and_his_mother_i_have_not_seen_him_nor_acknowledged_his_brethren_nor_knew_his_sons_for_they_kept_your_word_and_observed_your_covenant', 'they_shall_teach_jacob_your_ordinances_and_israel_your_law_they_shall_put_incense_in_your_nostrils_and_whole_offering_on_your_altar', 'bless_lord_his_substance_and_accept_the_work_of_his_hands_smite_the_loins_of_those_who_rise_against_him_that_they_rise_not_again'],
  [('levi_thummim_and_urim_proved_at_massah_blessed', S, LV), ('levi_father_and_mother_unseen_covenant_kept', S, LV), ('levi_teaches_jacob_incense_and_whole_offering', S, LV), ('levi_substance_blessed_loins_of_his_foes_smitten', S, LV)], []),
 ('blessing_benjamin_declared', 'Deut 33:12', '33:12', 'DV33-05', 'F5', 'speech', ['the_beloved_of_the_lord_shall_dwell_in_safety_by_him', 'he_covers_him_all_the_day_and_he_dwells_between_his_shoulders'],
  [('benjamin_beloved_dwells_in_safety_between_his_shoulders_blessed', S, BN)], []),
 ('blessing_joseph_declared', 'Deut 33:13', '33:13-17', 'DV33-06', 'F6', 'speech', ['blessed_of_the_lord_be_his_land_for_the_precious_things_of_heaven_for_the_dew_and_for_the_deep_that_couches_beneath', 'for_the_precious_things_of_the_fruits_of_the_sun_and_of_the_yield_of_the_moons_the_top_of_the_ancient_mountains_and_the_everlasting_hills', 'the_precious_things_of_the_earth_and_its_fulness_and_the_favor_of_him_that_dwelt_in_the_bush_on_the_head_of_joseph_and_on_the_crown_of_him_separate_from_his_brethren', 'his_firstling_bullock_majesty_is_his_and_his_horns_the_horns_of_the_wild_ox_the_ten_thousands_of_ephraim_and_the_thousands_of_manasseh'],
  [('joseph_land_blessed_with_the_precious_things', S, JO), ('joseph_the_bush_dweller_favor_on_the_crown_separate_from_his_brethren', S, JO), ('joseph_firstling_ox_horns_ephraim_myriads_manasseh_thousands', S, JO)], []),
 ('blessing_zebulun_and_issachar_declared', 'Deut 33:18', '33:18-19', 'DV33-07', 'F7', 'speech', ['rejoice_zebulun_in_your_going_out_and_issachar_in_your_tents', 'they_shall_call_peoples_to_the_mountain_there_they_shall_offer_sacrifices_of_righteousness', 'for_they_shall_suck_the_abundance_of_the_seas_and_the_hidden_treasures_of_the_sand'],
  [('zebulun_going_out_issachar_in_tents_blessed', S, ZB), ('peoples_called_to_the_mountain_sacrifices_of_righteousness', S, IS)], []),
 ('blessing_gad_declared', 'Deut 33:20', '33:20-21', 'DV33-08', 'F8', 'speech', ['blessed_be_he_that_enlarges_gad_he_dwells_as_a_lioness_and_tears_the_arm_yea_the_crown_of_the_head', 'he_chose_a_first_part_for_himself_for_there_a_portion_of_a_ruler_was_reserved', 'he_came_with_the_heads_of_the_people_he_executed_the_righteousness_of_the_lord_and_his_ordinances_with_israel'],
  [('gad_enlarged_lioness_first_part_lawgivers_portion_blessed', S, GD), ('gad_came_with_the_heads_righteousness_of_the_lord_executed', S, GD)], []),
 ('blessing_dan_naphtali_asher_declared', 'Deut 33:22', '33:22-25', 'DV33-09', 'F9', 'speech', ['dan_is_a_lions_whelp_that_leaps_forth_from_bashan', 'naphtali_sated_with_favor_and_full_of_the_blessing_of_the_lord_possess_the_sea_and_the_south', 'blessed_be_asher_above_sons_let_him_be_the_favored_of_his_brethren_and_let_him_dip_his_foot_in_oil', 'iron_and_brass_shall_be_your_bars_and_as_your_days_so_shall_your_strength_be'],
  [('dan_lions_whelp_leaps_from_bashan_blessed', S, DN), ('naphtali_sated_with_favor_sea_and_south_blessed', S, NP), ('asher_blessed_above_sons_foot_dipped_in_oil', S, AS), ('iron_and_brass_bars_strength_as_your_days_blessed', S, AS)], []),
 ('blessing_rider_of_the_heaven_declared', 'Deut 33:26', '33:26-27', 'DV33-10', 'F10', 'speech', ['there_is_none_like_the_god_of_jeshurun_who_rides_upon_the_heaven_as_your_help_and_in_his_excellency_on_the_skies', 'the_eternal_god_is_a_dwelling_place_and_underneath_are_the_everlasting_arms', 'he_drove_out_the_enemy_from_before_you_and_said_destroy'],
  [('none_like_the_god_of_jeshurun_rider_of_the_heaven_declared', S, I), ('eternal_god_dwelling_everlasting_arms_enemy_driven_out_declared', S, I)], []),
 ('blessing_israel_dwells_alone_declared', 'Deut 33:28', '33:28-29', 'DV33-11', 'F11', 'speech', ['israel_dwells_in_safety_the_fountain_of_jacob_alone_in_a_land_of_corn_and_wine_yea_his_heavens_drop_down_dew', 'happy_are_you_o_israel_who_is_like_you_a_people_saved_by_the_lord_the_shield_of_your_help_and_the_sword_of_your_excellency', 'your_enemies_shall_dwindle_away_before_you_and_you_shall_tread_upon_their_high_places'],
  [('israel_dwells_in_safety_alone_fountain_of_jacob_declared', S, I), ('happy_are_you_israel_shield_and_sword_high_places_trodden_declared', S, I)], []),
]
KINDS = [l[0] for l in LINES]
NEW_E = [(e, op, sub) for l in LINES for e, op, sub in l[7]]
NEW_EFFECTS = [e for e, _, _ in NEW_E]
REUSES = [(e, v, sub, l[0]) for l in LINES for e, v, sub in l[8]]      # NONE — no effect's own forward seat lies in the chapter (20b had three)
CELLS = {'F1': 'the_man_of_god_and_the_theophany', 'F2': 'the_prologue_law_and_king', 'F3': 'the_reuben_and_judah', 'F4': 'the_levi', 'F5': 'the_beloved_between_his_shoulders', 'F6': 'the_joseph',
         'F7': 'the_zebulun_and_issachar', 'F8': 'the_gad_lioness_and_the_lawgivers_portion', 'F9': 'the_dan_naphtali_and_asher', 'F10': 'the_rider_of_the_heaven', 'F11': 'the_israel_dwells_alone'}
# NO MARKER — the blessing stands on 19b's marker at 31:1 (Moses' last day (40, 12, 7): the year the ink's, the day the answer sheet's — Tosefta Sotah 11:3); 33:1's 'before his
# death' names that day; the counter does not move; markers 173 UNMOVED
MARKER = None
DAY = (40, 12, 7)
# THE PARSER'S FALSE SEVEN (the reading's measure — MARKED, not counted): a DATA row of the runner, no guard, no ledger write
GUARDS = {'the_false_seven': "33:23 'sated' (seva — Naphtali sated with favor) carries seven's consonants; the parser's own list MARKS it with the star and counts nothing — a homograph, no number in the chapter (the myriads of 33:2 and 33:17 and Manasseh's thousands construct plurals unread, Reuben's 'number' a noun): a DATA row, no write"}
# THE KIN'S COUNTS as the callees read them (ch33_callees.out THE NEAR NAMES) — the references UNMOVED after the run; no reuse moves any
KIN_UNMOVED = {'barred_from_the_land': 2, 'gathered_to_his_people': 5, 'go_up_to_nebo_see_the_land_commanded': 1, 'die_in_the_mountain_gathered_to_your_people_commanded': 1, 'as_aaron_died_in_hor_and_was_gathered': 1,
               'see_the_land_from_afar_not_go_there': 1, 'heaven_and_earth_witness': 5, 'blessing_and_curse_set': 2, 'blessings_for_hearing': 3, 'blessed_with_dew_and_fat': 1, 'blessed_the_people': 2, 'counted': 22,
               'hand_opening_commanded': 1, 'equal_portions_commanded': 1, 'levites_portion_given': 1, 'inheritance_barred': 2, 'book_of_the_law_beside_the_ark_commanded': 1, 'descended_on_the_mountain': 1,
               'doctrine_as_rain_and_dew_likened': 1, 'heavens_good_treasure_opened': 1, 'high_court_at_the_place_commanded': 1, 'high_places_banned': 3, 'incense_continual': 2, 'kings_smitten': 3, 'land_possessed': 6,
               'lords_portion_his_people_jacob': 1, 'nations_dispossessed_as_sihon_and_og_promised': 1, 'oral_law_unwritten': 3, 'presence_dwells': 1, 'shield_promised': 1, 'six_tribes_on_ebal_for_the_curse': 1,
               'six_tribes_on_gerizim_to_bless': 1, 'substituted_for_the_firstborn': 1, 'torah_through_moses': 1, 'work_of_the_hand_blessed': 2, 'storehouses_blessed': 1, 'firstling_sanctification_commanded': 1,
               'grave_marked': 1, 'judah_sent_ahead': 1, 'portion_added': 1, 'levite_forsaking_barred': 2, 'levites_loud_voice_commanded': 1, 'the_lord_alone_led_no_foreign_god': 1, 'song_sung': 1,
               'no_share_in_the_world_to_come': 3, 'slain_by_sword': 2, 'priestly_dues_granted': 1}
REUSE_BEFORE = {}
import collections as _c
_rc = _c.Counter(e for e, _, _, _ in REUSES)
REUSE_AFTER = {e: REUSE_BEFORE[e] + _rc[e] for e in REUSE_BEFORE}
# THE EDGES from the runner — every one REFERENCE (the ink names the kin's institution or event, or the kin's cell names THIS chapter's verse forward); the registration edge and the census's FALSE and VIA edges filed at RUN B from the gate's print
EDGES = ['song_charge_nebo', 'covenant_return_charge', 'gad_reuben', 'joseph', 'family', 'chukat', 'exodus_story', 'erection', 'second_tablets', 'incense_shekel', 'balak', 'opening_speech', 'refuge_war_family', 'courts_prophet',
         'festivals_judges', 'good_land', 'blessing_and_curse', 'release_firstborn', 'persons_poor_court', 'bamidbar', 'naso', 'korach', 'vestments', 'priesthood', 'zelophehad', 'second_census', 'borders', 'place_name',
         'obey_horeb', 'seven_nations', 'hear_o_israel', 'moadim', 'offerings', 'firstfruits_ebal_curses', 'shelach', 'journeys', 'midian', 'mamre', 'pre_sinai']
POINTERS_PREDICTED = [('Deut 33:21', "for there a portion of a ruler was reserved — MOSES' GRAVE in Gad's portion (Onkelos 33:21; the Sifrei 355:6 with the twilight creations): the tape's own entry AHEAD at 34:6 — FORWARD, the death's sitting's; gad_reuben's DATA moses_grave by CALL (Reuben's Nebo, Gad's field — Sotah 13b)"),
                      ('Deut 33:8', "whom You proved at Massah and strove with at the waters of Meribah — the tape's own entries at Exodus 17:7 and Numbers 20:13 (exodus_story.trials, chukat.meribah by CALL): RUN_CITATION"),
                      ('Deut 33:9', "who said of his father and his mother I have not seen him — the calf's sword on the kin, Exodus 32:26-29 on the tape (erection.calf by CALL; slain_by_sword on the three thousand): RUN_CITATION"),
                      ('Deut 33:16', "the favor of Him that dwelt in the bush — Exodus 3:2-4 on the tape (exodus_story by CALL — appeared_in_the_bush the kind): RUN_CITATION"),
                      ('Deut 33:17', "the ten thousands of Ephraim and the thousands of Manasseh — Genesis 48:19's blessing on the tape (joseph by CALL — younger_set_first, adopted_as_sons on the sons' ledgers): RUN_CITATION"),
                      ('Deut 33:5', "there was a king in Jeshurun when the heads of the people gathered — 20b's owed pointer row (346:2 read at chapter 32 for 32:3's teaching) PAID here in its own piska: a POINTER ROW of the readback, grade R"),
                      ('Deut 33:28', "Israel dwells in safety alone, the fountain of Jacob — 20b's owed pointer row (356:5 and 356:8 read at chapter 32 for 32:12's and 32:2's teaching) PAID here: a POINTER ROW of the readback, grade R")]
STATE_ROWS = []                    # no condition state in the blessing (33:29's enemies a declared future inside a blessing, no two-armed condition)
POINTER_ROWS = ['Deut 33:5', 'Deut 33:28']   # 20b's owed pointers PAID — the piskaot 346 and 356 read here in their own chapter
CAL_NEW = []                       # no clock word in the blessing; the festivals' times at 33:18 Onkelos's, the registry's parameters unmoved
DATA_ROWS = ['the_false_seven', 'the_readback', 'moses_grave_ahead', 'the_sanctuarys_tribe', 'the_three_scrolls_in_the_court', 'the_two_torahs', 'the_twilight_creations', 'the_eighteen_blessings', 'simeon_under_judah',
             'the_three_parts_of_the_blessing', 'the_tribes_order', 'the_seat_rule_by_row', 'onkelos_and_the_sifrei_one_teaching', 'the_torah_offered_and_refused', 'the_pointers_ahead']
PARAMS = ['the_chain_of_transmission', 'the_shekhinah_among_ten', 'the_twilight_creations', 'the_goring_ox_of_a_gentile', 'the_eighteen_blessings', 'sacrifices_without_a_temple', 'those_lacking_atonement', 'the_oil_of_tekoa',
          'the_new_moons_witnesses', 'the_world_to_come_share', 'the_first_of_adar_proclamations', 'the_seventy_tongues_on_ebal', 'the_seven_commandments_of_the_nations', 'the_challah_measure', 'the_sanctuarys_tribe',
          'the_three_scrolls_in_the_court']
MISHNAH = [('Avot', 1, 1), ('Avot', 3, 6), ('Avot', 5, 6), ('Bava Kamma', 4, 3), ('Berakhot', 4, 3), ('Eduyot', 8, 6), ('Keritot', 2, 1), ('Menachot', 8, 3), ('Rosh Hashanah', 2, 8), ('Rosh Hashanah', 2, 9), ('Sanhedrin', 10, 1),
           ('Shekalim', 1, 1), ('Sotah', 7, 5)]
RANGE_EXTRA = [('Rosh Hashanah', 2, 9)]        # cited as '2:8-9' — the regex reads 2:8; the second row read whole with it
MISHNAH_EXCLUDED = [('Eduyot', 1, 1), ('Chagigah', 2, 6), ('Sheviit', 6, 1), ('Taanit', 4, 2)]   # the regex's misreads: 'the Tosefta's Eduyot 1:1' and 'Chagigah 2:6'; 'the Jerusalem Talmud's Sheviit 6:1' and 'Taanit 4:2' — read whole and EXCLUDED
NOROW = [('Avodah Zarah', 8, 4), ('Eruvin', 8, 23), ('Sotah', 11, 11)]   # the Tosefta's paragraphs wearing the Mishnah's names — NO SUCH ROW in the Mishnah export
TOSEFTA = [('Tosefta Avodah Zarah', 9, 4), ('Tosefta Eduyot', 1, 1)]
RENUMBER = {('Tosefta Avodah Zarah', 8, 4): ('Tosefta Avodah Zarah', 9, 4)}   # the ledger's (the translator's) paragraph -> the export's (20b's find by the rows' own words)
TOSEFTA_NOTE = ("the ledger names 'Tosefta Avodah Zarah 8:4' at 343:6 (the nations' seven commandments), the translator's paragraph number — the export's 9:4, found at 20b by the words 'seven commandments'; "
                "'Tosefta Eduyot 1:1' at 48:9 as cited (the export's chapter 1 has thirteen rows, the first the sages at Yavneh); the Tosefta's Sotah 11:11 at 352:11, Eruvin 8:23 at 355:6 and Chagigah 2:6 at 343:14 "
                "NOT in the export by those numbers (Sotah's chapter 11 has nine rows, Eruvin's chapter 8 seventeen, Chagigah's chapter 2 seven) nor by their words — OWED; Tosefta Sotah 4:4 found beside 355:6 on 34:6, LEFT for 34's sitting")
TOSEFTA_OWED = ["Tosefta Sotah 11:11 (352:11 — R. Meir on the sanctuary's tribe; the translator's parallel, not located)", "Tosefta Eruvin 8:23 (355:6 — the twilight creations' parallel, not located)",
                "Tosefta Chagigah 2:6 (343:14 — the right hand's fiery law, the translator's parallel, not located)"]
TALMUD_OWED = ["Shabbat 55 (the ledger's one chapter-only citation — the folio without a page: Reuben's sin at 347:2)", "Sotah 13b-14a (Moses' grave and the four mil — gad_reuben's DATA names 13b:20; 355:6)",
               "Zevachim 118b (the sanctuary's tribe and Benjamin's strip — place_name's row names 118b:6-12; 352:10)", "Sanhedrin 91b-92a (the resurrection from the Torah — Reuben's life, 347:2 with Sanhedrin 10:1)",
               "Avodah Zarah 2b-3a (the Torah offered to the nations and refused — 343:6)", "the Jerusalem Talmud Taanit 4:2 (the three scrolls in the court — 356:1) and Sheviit 6:1 (the Girgashites who fled — 356:3)"]
def counts():
    ops = _c.Counter(op for _, op, _ in NEW_E); subs = _c.Counter(sub for _, _, sub in NEW_E); rsubs = _c.Counter(sub for _, _, sub, _ in REUSES); forms = _c.Counter(l[5] for l in LINES)
    return {'lines': len(LINES), 'new_effects': len(NEW_EFFECTS), 'distinct': len(set(NEW_EFFECTS)), 'ops': dict(ops), 'reuses': len(REUSES), 'writes': len(NEW_EFFECTS) + len(REUSES), 'edges': len(EDGES), 'params': len(PARAMS),
            'mishnah': len(MISHNAH), 'tosefta': len(TOSEFTA), 'per_line': [(l[1], len(l[7]) + len(l[8])) for l in LINES], 'cells': len(CELLS), 'subjects_new': dict(subs), 'subjects_reuse': dict(rsubs), 'forms': dict(forms),
            'writes_by_subject': dict(subs + rsubs), 'fields': sum(len(l[6]) for l in LINES), 'data_rows': len(DATA_ROWS), 'kin': len(KIN_UNMOVED), 'guards': len(GUARDS), 'tribes': len(set(s for _, _, s in NEW_E) - {I, MO})}
if __name__ == '__main__':
    import os, sys, yaml
    c = counts(); print(c)
    assert c['new_effects'] == c['distinct'], 'a name twice'
    assert len(set(KINDS)) == len(KINDS)
    assert set(REUSE_AFTER) == set(REUSE_BEFORE) and all(REUSE_AFTER[e] > REUSE_BEFORE[e] for e in REUSE_BEFORE)
    assert all(l[4] in CELLS for l in LINES) and len(set(l[4] for l in LINES)) == len(CELLS)
    assert set(RENUMBER.values()) <= set(TOSEFTA) and set(RANGE_EXTRA) <= set(MISHNAH)
    ROOT = os.popen('git rev-parse --show-toplevel').read().strip(); S9 = ROOT + '/World/step9'
    fx = yaml.safe_load(open(S9 + '/effect_vocabulary.yaml', encoding='utf-8'))['effects']; ev = yaml.safe_load(open(S9 + '/event_vocabulary.yaml', encoding='utf-8'))['events']
    coll_e = [e for e in NEW_EFFECTS if e in fx]; coll_k = [k for k in KINDS if k in ev]
    print('COLLISIONS: effects present before', coll_e, '| kinds present before', coll_k)
    assert not coll_e and not coll_k, 'a new name already in a registry'
    assert all(e in fx for e in REUSE_BEFORE) and all(e in fx for e in KIN_UNMOVED), ('a reuse or kin name not in the registry', [e for e in list(REUSE_BEFORE) + list(KIN_UNMOVED) if e not in fx])
    print('FIRST VERSES', [l[1] for l in LINES]); print('WRITES PER LINE (new + reuse)', c['per_line']); print('REUSE_AFTER', REUSE_AFTER); print('SUBJECTS', c['subjects_new'])
    print('SPEC OK')
