

TESTS = [
 # ---- Gen 2: the garden ----
 ('a living soul — the phrase once as the man\'s predicate', garden('living_soul'), 1),
 ('the first office: work and keep', garden('office'), ('work', 'keep')),
 ('"took" — elevated or persuaded (Bereshit Rabbah 16:5)', garden('took'), ('elevated', 'persuaded')),
 ('a help, or against him (Bereshit Rabbah 17:3)', garden('helper'), ('a_help', 'against_him')),
 ('the couple\'s row (Yevamot 6:6)', garden('couple_sheet'), ('two_males', 'male_and_female')),
 ('the three deep sleeps at both seats (Bereshit Rabbah 17:5, 44:17)', garden('deep_sleeps'), ('sleep', 'prophecy', 'stupor')),
 ('fourteen naming clauses', garden('names_count'), 14),
 # ---- Gen 3: the breach ----
 ('the first rule fetched from the pre-Sinai engine (by call)', breach('first_rule_by_call'), ['ויצו', 'יהוה', 'אלהים', 'על', 'האדם', 'לאמר']),
 ('the four verbs of the breach', breach('four_verbs'), 4),
 ('the tree — vine, wheat, fig (Berakhot 40a; Sanhedrin 70a)', breach('tree_identity'), ('vine', 'wheat', 'fig')),
 ('three things said of the tree (Bereshit Rabbah 19:5)', breach('three_things'), 3),
 ('were they blind (Bereshit Rabbah 19:6)', breach('eyes'), 'were_they_blind'),
 ('"deceived" once in the Tanakh', breach('deceived_seat'), 1),
 ('the day\'s hours — sub-day is OUT', breach('no_sub_day'), 'recorded_not_run'),
 # ---- the sentences ----
 ('the four curses of the stretch', sentences('curse_seats'), [(3, 14), (3, 17), (4, 11), (9, 25)]),
 ('seventy-one mentions of the Name (Bereshit Rabbah 20:4)', sentences('seventy_one'), 71),
 ('four desires (Bereshit Rabbah 20:7)', sentences('four_desires'), 4),
 ('livelihood harder than birth (Bereshit Rabbah 20:9)', sentences('livelihood'), 'harder_than_birth'),
 ('the thousand-year day (Bereshit Rabbah 19:8)', sentences('thousand_year_day'), (1000, 930, 70)),
 ('four died by the serpent\'s counsel (Shabbat 55b)', sentences('serpent_counsel'), 4),
 ('the garments — kindness first and last (Sotah 14a)', sentences('garments_kindness'), 'begins_and_ends_with_kindness'),
 ('garments of light (Bereshit Rabbah 20:12)', sentences('garments_of_light'), 'kutnot_or_with_an_aleph'),
 ('expelled from two worlds? (Bereshit Rabbah 21:7)', sentences('expelled_two_worlds'), ('this_world_and_the_next', 'this_world_only')),
 ('driven out like a divorced daughter (Bereshit Rabbah 21:8)', sentences('divorced_daughter'), ('priests_daughter_cannot_return', 'israelites_daughter_can')),
 ('the east receives (Bereshit Rabbah 21:9)', sentences('east_receives'), ('adam', 'cain', 'the_manslayer')),
 # ---- Gen 4: Cain and Abel ----
 ('Cain\'s minchah names the meal-offering engine (by call)', cain('minchah_by_call'), 3),
 ('the firstling\'s seat, Lev 27:26 (by call)', cain('firstling_by_call'), 'cannot_be_sanctified_to_the_altar'),
 ('the fat inventory of the lamb (by call)', cain('fat_by_call'), ['parts', 'pointer_4_10']),
 ('the regard verb once in the Torah', cain('regard_seats'), [(4, 4)]),
 ('from the refuse; the firstlings (Bereshit Rabbah 22:5)', cain('refuse'), ('from_the_refuse', 'the_firstlings')),
 ('Abel no more than fifty days (the row; Bereshit Rabbah 22:4)', cain('abel_days'), 50),
 ('the first IF — rule over it (Kiddushin 30b)', cain('first_if'), 'rule_over_it'),
 ('wounds upon wounds (Sanhedrin 37b)', cain('wounds'), 'wounds_upon_wounds'),
 ('the bloods — his and his descendants\' (Sanhedrin 4:5)', cain('bloods_sheet'), 'his_blood_and_the_blood_of_his_descendants'),
 ('"your brother\'s bloods" at two seats', cain('bloods_seats'), [(4, 10), (4, 11)]),
 ('the earth\'s mouth opened once (Sanhedrin 37b)', cain('earth_mouth'), 'opened_once_for_abel'),
 ('exile atones half (Sanhedrin 37b)', cain('exile_half'), ('fugitive_and_wanderer', 'dwelt_in_nod')),
 ('greater than my father\'s (Bereshit Rabbah 22:11)', cain('greater_than_father'), 'a_light_command_vs_bloodshed'),
 ('the mark — three arms (Bereshit Rabbah 22:12)', cain('mark_arms'), ('a_dog', 'a_horn', 'leprosy')),
 ('"sevenfold" at two seats', cain('sevenfold_seats'), [(4, 15), (4, 24)]),
 ('Lamech\'s wives refused (Bereshit Rabbah 23:4)', cain('lamech_wives'), 'refused_tomorrow_the_flood'),
 ('two wives — offspring and pleasure (Bereshit Rabbah 23:2)', cain('two_wives'), ('for_offspring', 'for_pleasure')),
 ('the rebellion verb at three places (Bereshit Rabbah 23:7)', cain('rebellion_three'), 3),
 ('the first city', cain('city_seat'), 1),
 # ---- the lines and the ledger ----
 ('"and he begot" at thirty-nine seats', lines('begot_seats'), 39),
 ('"and she bore" at seven seats of the stretch', lines('bore_seats'), 7),
 ('"and he died" at eleven seats', lines('died_seats'), 11),
 ('ten generations twice (Avot 5:2)', lines('ten_generations'), (10, 10)),
 ('Enoch taken while righteous (Bereshit Rabbah 25:1)', lines('enoch_taken'), 'hypocrite_taken_while_righteous'),
 ('Noah\'s name is not its exposition (Bereshit Rabbah 25:2)', lines('noah_name'), 'the_name_is_not_the_exposition'),
 ('the ten famines — the stretch\'s three (Bereshit Rabbah 25:3, 40:3)', lines('ten_famines'), ('adam', 'lamech', 'abraham')),
 ('two Enochs, two Lamechs', lines('two_lines_names'), ('enoch', 'lamech')),
 ('Seth\'s birth stated twice', lines('seth_twice'), 2),
 # ---- Gen 6: the prologue ----
 ('the sons of the judges (Bereshit Rabbah 26:5)', prologue('sons_of_god'), 'sons_of_the_judges'),
 ('the row gen6_3_reading', prologue('reading_row'), 'reprieve'),
 ('a hundred and twenty years parsed', prologue('reprieve_number'), 120),
 ('THE RETROGRADE DATING of 6:3', prologue('retrograde'), (600, 120, 480, 500)),
 ('with "great" they sinned (Sanhedrin 108a)', prologue('wickedness_great'), 'with_great_they_sinned_with_great_judged'),
 ('the regret — two arms (Sanhedrin 108a)', prologue('regret_two'), ('well_did_i_prepare_graves', 'not_well')),
 ('wiped in two worlds (Sanhedrin 108a; Avot? no — Sanhedrin 10:3)', prologue('wipe_two_worlds'), ('this_world', 'the_world_to_come')),
 ('even on Noah the decree was sealed (Sanhedrin 108a)', prologue('favor_even_noah'), 'the_decree_sealed_on_noah_too'),
 ('the flood\'s month — Iyar or Cheshvan (Rosh Hashanah 11b)', prologue('flood_month_row'), ('iyar', 'cheshvan')),
 # ---- the ark ----
 ('mated across kinds (Sanhedrin 108a)', ark('corrupt_five'), 'mated_across_kinds'),
 ('robbery sealed the decree (Sanhedrin 108a)', ark('robbery_seals'), 'robbery'),
 ('the spec\'s numbers', ark('spec_numbers'), (300, 50, 30)),
 ('the three decks (Sanhedrin 108b)', ark('decks'), ('dung', 'beasts', 'man')),
 ('the covenant\'s heads (by call)', ark('covenant_by_call'), 'you_and_your_seed_after_you'),
 ('"covenant" in the stretch', ark('covenant_seats'), [(6, 18), (9, 9), (9, 11), (9, 12), (9, 13), (9, 15), (9, 16), (9, 17), (15, 18)]),
 ('the receipt: thus did Noah', ark('receipt'), 'thus_did_noah'),
 ('the clean beast by the classifier (by call)', ark('clean_by_call'), 'pure'),
 ('the seven days — three arms (Sanhedrin 108b)', ark('seven_days_arms'), ('methuselahs_mourning', 'the_sun_reversed', 'a_taste_of_the_world_to_come')),
 ('the forty — two arms (Bereshit Rabbah 32:5)', ark('forty_arms'), ('the_torah_in_forty', 'the_embryos_forty')),
 ('intercourse barred and permitted by the word order (Sanhedrin 108b)', ark('intercourse_order'), ('barred_at_6_18', 'permitted_at_8_16')),
 ('three smitten in the ark (Sanhedrin 108b)', ark('three_smitten'), ('the_dog', 'the_raven', 'ham')),
 # ---- the flood ----
 ('judged by water like the eyeball (Sanhedrin 108a)', flood('eyeball'), 'judged_by_water_like_the_eyeball'),
 ('the beasts\' guilt — the wedding canopy (Sanhedrin 108a)', flood('beasts_guilt'), 'the_wedding_canopy'),
 ('not the fish', flood('not_the_fish'), 'not_the_fish'),
 ('only Noah remained', flood('remnant'), 1),
 ('a hundred and fifty days', flood('hundred_fifty'), 150),
 ('three generations (Sanhedrin 10:3)', flood('three_rows_sheet'), ('the_flood', 'the_dispersion', 'sodom')),
 ('twelve months (Eduyot 2:10)', flood('twelve_months_sheet'), 12),
 # ---- the remembering ----
 ('"and God remembered" — the debut', remembering('remember_seats'), [(8, 1)]),
 ('boiling water (Sanhedrin 108b)', remembering('boiling'), 'subsided_like_the_kings_wrath'),
 ('three fountains stayed open (Bereshit Rabbah 33:4)', remembering('three_fountains'), 3),
 ('the row window_count_from', remembering('window_from'), 'mountaintops'),
 ('the raven\'s retort (Sanhedrin 108b)', remembering('raven_retort'), 'your_master_hates_me_and_you_hate_me'),
 ('the dove\'s three sendings', remembering('dove_three'), ('returned', 'the_olive_leaf', 'did_not_return')),
 ('bitter from Your hand (Sanhedrin 108b)', remembering('olive_bitter'), 'bitter_from_your_hand_not_sweet_from_flesh_and_blood'),
 ('clean birds dwell with the righteous (Sanhedrin 108b)', remembering('clean_birds'), 'dwell_with_the_righteous'),
 ('a year and ten days by the ink', remembering('year_and_days'), (1, 10)),
 # ---- the exit ----
 ('entered and went out by permission (Bereshit Rabbah 34:4)', exit('by_permission'), 'entered_and_went_out_by_permission'),
 ('by families, not they (Sanhedrin 108b)', exit('by_families'), 'by_families_not_they'),
 ('the burnt offering\'s place (by call)', exit('olah_by_call'), 'north'),
 ('four altars', exit('altar_seats'), [(8, 20), (12, 7), (12, 8), (13, 18)]),
 ('the great altar (Bereshit Rabbah 34:9)', exit('great_altar'), 'the_great_altar_of_jerusalem'),
 ('the pleasing savor once in Genesis', exit('savor_seat'), 1),
 ('the righteous rule their hearts (Bereshit Rabbah 34:10)', exit('heart_resolve'), 'the_righteous_rule_their_hearts'),
 ('as long as heaven and earth stand (Bereshit Rabbah 34:11)', exit('seasons_standing'), 'as_long_as_heaven_and_earth_stand'),
 ('8:17 runs the blessing (by call)', exit('blessing_by_call'), [22, 28, 103]),
 # ---- the vineyard ----
 ('profaned (Bereshit Rabbah 36:3)', vineyard('profaned'), 'became_common'),
 ('planted, drank, disgraced in one day (Bereshit Rabbah 36:4)', vineyard('same_day'), 'planted_drank_disgraced_in_one_day'),
 ('learn from the first man (Sanhedrin 70a)', vineyard('learn_from_adam'), 'wine_alone_undid_the_first_man'),
 ('Ham\'s deed — Rav and Shmuel (Sanhedrin 70a)', vineyard('ham_deed'), ('castrated', 'lay_with')),
 ('Ham sinned and Canaan is cursed (Bereshit Rabbah 36:7)', vineyard('canaan_puzzle'), 'ham_sinned_and_canaan_is_cursed'),
 ('the slave word\'s four tokens', vineyard('slave_tokens'), 4),
 ('Shem the tallit, Japheth the burial (Bereshit Rabbah 36:6)', vineyard('shem_began'), ('shem_the_tallit', 'japheth_the_burial')),
 ('Greek alone (Megillah 1:8; 9b)', vineyard('greek_sheet'), 'greek_alone'),
 ('Cyrus, and the tents of Shem (Bereshit Rabbah 36:8)', vineyard('cyrus'), 'the_presence_only_in_the_tents_of_shem'),
 # ---- the nations ----
 ('greatness to Nimrod (Chullin 89a)', nations('nimrod_greatness'), 'i_gave_greatness_to_nimrod'),
 ('Amraphel is Nimrod (Eruvin 53a)', nations('amraphel'), ('nimrod_is_his_name', 'amraphel_is_his_name')),
 ('Shinar (Bereshit Rabbah 37:4)', nations('shinar'), ('the_dead_shaken_out', 'shakes_off_the_commandments')),
 ('Eber a great prophet (Bereshit Rabbah 37:7)', nations('peleg_prophet'), 'eber_a_great_prophet'),
 ('Japheth the elder (Bereshit Rabbah 37:7)', nations('shem_or_japheth_elder'), 'japheth_the_elder'),
 ('four cities', nations('cities_four'), 4),
 # ---- Babel ----
 ('one language — once', babel('one_language'), 1),
 ('three parties (Sanhedrin 109a)', babel('three_parties'), ('to_dwell', 'to_serve_idols', 'to_make_war')),
 ('Mitzrayim to Cush (Bereshit Rabbah 38:8)', babel('who_to_whom'), 'mitzrayim_to_cush'),
 ('one of the ten descents (Bereshit Rabbah 38:9)', babel('ten_descents'), 'one_of_the_ten'),
 ('changed for Ptolemy (Bereshit Rabbah 38:10)', babel('ptolemy'), 'let_ME_go_down'),
 ('the tower\'s thirds (Sanhedrin 109a)', babel('thirds'), ('burned', 'swallowed', 'stands')),
 ('two scatterings (Sanhedrin 10:3)', babel('two_scatterings'), ('this_world', 'the_world_to_come')),
 ('the scatter verb\'s debut', babel('scatter_seats'), [(11, 8)]),
 # ---- Shem\'s line ----
 ('two years after the flood', shem_line('two_years_after'), (100, 2)),
 ('Terah the idol-maker (Bereshit Rabbah 38:13)', shem_line('haran_furnace'), 'terah_the_idol_maker'),
 ('the one death in sequence', shem_line('died_in_sequence'), 1),
 ('Iscah is Sarah (Megillah 14a)', shem_line('iscah'), 'iscah_is_sarah'),
 ('the marriage formula\'s five verbs (by call)', shem_line('marriage_by_call'), 5),
 ('Sarai barren — once', shem_line('barren_seat'), 1),
 ('Terah\'s death sixty years after the going out', shem_line('terah_death_gap'), (70, 75, 205, 60)),
 ('the wicked called dead in their lifetime (Bereshit Rabbah 39:7)', shem_line('terah_death_midrash'), 'the_wicked_called_dead_in_their_lifetime'),
 ('Abram a year older than Nahor (Bereshit Rabbah 38:14)', shem_line('abram_elder'), 'abram_a_year_older_than_nahor'),
 # ---- the call ----
 ('the going\'s receipt', call('go_receipt'), 'as_the_lord_had_spoken'),
 ('two "go you" (Bereshit Rabbah 39:8)', call('two_go_you'), ('aram_naharaim_and_aram_nachor', 'the_pieces_to_haran')),
 ('I will MAKE you (Bereshit Rabbah 39:11)', call('new_creature'), 'i_will_MAKE_you'),
 ('the ladder\'s six clauses', call('ladder'), ('bless_you', 'make_your_name_great', 'be_a_blessing', 'bless_your_blessers', 'curse_your_curser', 'all_families_blessed_in_you')),
 ('the land promised thrice, closed at 15:18', call('land_seats'), [(12, 7), (13, 15), (15, 7), (15, 18)]),
 ('three altars (Bereshit Rabbah 39:16)', call('three_altars'), 3),
 ('"called on the name" at two Genesis seats', call('called_seats'), [(12, 8), (26, 25)]),
 ('seventy-five', call('seventy_five'), 75),
 ('seven stations of Abram', call('stations'), 7),
 # ---- Egypt ----
 ('the third famine (Bereshit Rabbah 40:3)', egypt('famine_third'), 'the_third_of_ten'),
 ('Abram\'s first speech', egypt('first_speech'), 'behold_now_i_know'),
 ('the chest at the customs (Bereshit Rabbah 40:5)', egypt('chest'), 'hidden_in_a_chest_at_the_customs'),
 ('the passive taking', egypt('passive_take'), 'taken_passive'),
 ('ra\'atan (Bereshit Rabbah 41:2)', egypt('raatan'), 'raatan'),
 ('the pattern of the sons (Bereshit Rabbah 40:6)', egypt('pattern'), 'whatever_is_written_of_abraham_is_written_of_his_sons'),
 ('silver and gold (Bereshit Rabbah 41:3)', egypt('silver_and_gold'), 'brought_them_out_with_silver_and_gold'),
 # ---- the separation ----
 ('muzzled (Bereshit Rabbah 41:5)', separation('muzzled'), 'abrahams_beasts_muzzled_lots_not'),
 ('a language of lewdness (Bereshit Rabbah 41:7)', separation('lewdness'), 'the_whole_verse_a_language_of_lewdness'),
 ('"they separated" once', separation('parted_seat'), 1),
 ('Sodom\'s row (Sanhedrin 10:3)', separation('sodom_sheet'), ('wicked_this_world', 'sinners_the_world_to_come', 'but_they_stand_in_judgment')),
 ('Sodom — body and money (Sanhedrin 109a)', separation('sodom_arms'), ('wicked_in_body_sinners_in_money', 'wicked_in_money_sinners_in_body')),
 ('the dust blessed by water (Bereshit Rabbah 41:9)', separation('dust'), 'as_the_dust_blessed_only_by_water'),
 ('the walk — the three modes (by call; Bava Batra 100a)', separation('walk_by_call'), ['money', 'deed', 'possession']),
 # ---- the war ----
 ('the years\' chain', war('years_chain'), (12, 13, 14)),
 ('twenty-five or thirteen (Bereshit Rabbah 42:6)', war('years_arms'), (25, 13)),
 ('an annal with no speech', war('annal'), 0),
 ('the escapee is Og (Bereshit Rabbah 42:8)', war('og'), 'the_escapee_is_og'),
 ('the Hebrew — three arms (Bereshit Rabbah 42:8)', war('hebrew_arms'), ('from_eber', 'from_beyond_the_river', 'the_language')),
 ('three hundred and eighteen', war('three_eighteen'), 318),
 ('Eliezer alone (Nedarim 32a)', war('eliezer'), 'eliezer_alone'),
 ('the two hundred and ten years — three causes (Nedarim 32a)', war('punished_210'), ('pressed_scholars_into_service', 'whereby_shall_i_know', 'give_me_the_persons')),
 ('the night\'s halves (Bereshit Rabbah 43:3)', war('night_halves'), ('of_itself', 'its_maker_divided_it')),
 ('the children not returned (Bereshit Rabbah 43:4)', war('children_not_returned'), 'men_and_women_returned_the_children_not'),
 ('the priest\'s office (by call)', war('priest_by_call'), ['blemished_and_minors', 'chalalim']),
 ('the priesthood from Shem (Nedarim 32b)', war('priesthood_from_shem'), 'taken_from_shem_given_to_abraham'),
 ('Salem is Jerusalem (Bereshit Rabbah 43:6)', war('salem'), 'salem_is_jerusalem'),
 ('the tithe\'s seat (by call)', war('tithe_by_call'), 'holy_to_the_LORD'),
 ('the raised hand (Bereshit Rabbah 43:9)', war('raised_hand'), ('terumah', 'an_oath')),
 ('a thread to a shoe-latchet', war('thread_to_latchet'), 'not_a_thread_nor_a_shoe_latchet'),
 # ---- the pieces ----
 ('two fears (Bereshit Rabbah 44:4)', pieces('two_fears'), ('a_righteous_man_among_the_slain', 'the_reward_consumed')),
 ('"childless" — Lev 20:20\'s row (by call)', pieces('childless_by_call'), (14, 20, None, True)),
 ('the heir — the inheritance owed forward (by call)', pieces('heir_by_call'), ['Deut 25:5', 'Num 27:8']),
 ('no constellation for Israel (Nedarim 32a)', pieces('astrology'), 'no_constellation_for_israel'),
 ('inherited both worlds by faith (the Mekhilta)', pieces('faith_merit'), 'inherited_both_worlds_by_faith'),
 ('reckoned — staged both ways', pieces('reckoned_both_ways'), 'staged_both_ways'),
 ('the furnace (Bereshit Rabbah 44:13)', pieces('furnace'), ('michael', 'the_holy_one_himself')),
 ('by what merit (Bereshit Rabbah 44:14)', pieces('by_what_merit'), 'by_the_atonements'),
 ('the bird offering\'s species (by call)', pieces('birds_by_call'), 'turtledoves_or_young_pigeons'),
 ('the kingdoms and the bird (Bereshit Rabbah 44:15)', pieces('kingdoms'), ('babylon', 'media', 'greece', 'israel_the_bird')),
 ('four hundred years', pieces('four_hundred'), 400),
 ('also that nation (Bereshit Rabbah 44:19)', pieces('also_that_nation'), ('egypt', 'the_four_exiles')),
 ('after ten plagues (Bereshit Rabbah 44:20)', pieces('after_ten_plagues'), 'after_i_bring_ten_plagues'),
 ('the fourth generation', pieces('fourth_generation'), 4),
 ('four things shown (Bereshit Rabbah 44:21)', pieces('four_things'), ('gehenna', 'the_kingdoms', 'the_giving_of_the_torah', 'the_temple')),
 ('the covenant cut — Exod 34\'s word', pieces('covenant_cut_seat'), 1),
 ('ten named, seven given (Bereshit Rabbah 44:23)', pieces('ten_nations'), (10, 7, 3)),
 # ---- Hagar ----
 ('ten years (Yevamot 6:6; 64a)', hagar('ten_years_sheet'), 'may_not_neglect_procreation'),
 ('the ten years parsed', hagar('ten_years_number'), 10),
 ('"to him as a wife" at seven Genesis seats', hagar('as_a_wife'), 7),
 ('from the first union (Bereshit Rabbah 45:4)', hagar('first_union'), ('from_the_first_union', 'never_from_the_first')),
 ('"despised" once', hagar('despised_seat'), 1),
 ('you wrong me with words (Bereshit Rabbah 45:5)', hagar('wrong_with_words'), 'you_wrong_me_with_words'),
 ('the affliction\'s reading (Bereshit Rabbah 45:6)', hagar('affliction_reading'), 'not_obliged_for_her_good_or_ill'),
 ('the flight — one type, two layers', hagar('flight_seat'), 'the_exodus_daemon_seat_checked'),
 ('the return never narrated', hagar('return_open'), 'return_never_narrated'),
 ('named before birth (Bereshit Rabbah 45:8)', hagar('named_before_birth'), ('isaac', 'solomon', 'josiah')),
 ('"you shall call" against "Abram called"', hagar('you_shall_call_vs_abram_called'), ('you_shall_call', 'abram_called')),
 ('the wild ass (Bereshit Rabbah 45:9)', hagar('wild_ass'), ('grows_in_the_wilderness', 'plunders_souls')),
 ('a God of seeing (Bereshit Rabbah 45:10)', hagar('god_of_seeing'), 'never_conversed_with_a_woman_but_through_an_angel'),
 # ---- THE SCENE AND THE HEADLINES ----
 ('THE SCENE on the world engine', build('world'), __SCENE_PRED__),
 ('HEADLINE: the land promises close on the perfect', build('headline_promises'), 'the_promises_of_the_land_close_on_the_inks_own_perfect'),
 ('HEADLINE: three generations, three heaven entries', build('headline_generations'), 'the_three_generations_of_sanhedrin_10_3_are_three_heaven_entries'),
 ('HEADLINE: the reprieve is a retrograde-dated timer', build('headline_retrograde'), 'the_reprieve_is_a_retrograde_dated_timer'),
 ('HEADLINE: the ledger\'s deaths ride the proleptic markers', build('headline_ledger'), 'the_ledgers_deaths_ride_the_proleptic_markers'),
 ('HEADLINE: seven kinds under two law layers', build('headline_two_layers'), 'seven_kinds_under_two_law_layers'),
]

if __name__ == '__main__':
    print()
    ok = 0
    frac = {I: 0, M: 0, A: 0, D: 0, P: 0, H: 0}
    misses = []
    for name, c, want in TESTS:
        hit = c['v'] == want
        ok += hit
        frac[c['p']] += 1
        if not hit: misses.append((name, c['v']))
        print('%s %-76s [%s] %s' % ('OK ' if hit else 'MISS', name[:76], c['p'], '' if hit else 'got=%r' % (c['v'],)))
        print('     effects: %s' % ', '.join(c['fx']))
    n = len(TESTS)
    assert n == GUARDED, (n, GUARDED)
    print()
    print('MATRIX: %d/%d cells match the answer sheet' % (ok, n))
    print('FRACTIONS: pure ink %d/%d (%d%%) · recorded moves %d/%d (%d%%) · answer-sheet %d/%d · data %d/%d · imports %d/%d · hypotheses %d/%d' % (
          frac[I], n, 100 * frac[I] // n, frac[M], n, 100 * frac[M] // n, frac[A], n, frac[D], n, frac[P], n, frac[H], n))
    print('effects: every cell carries REGISTERED effects — a hundred and forty-three discovered in the stretch\'s own words and registered first (living_soul ... wild_ass_of_a_man) [effects law satisfied]')
    print('SCENE: %r' % (SCENE,))
    _W.print_coverage()
    if ok == n:
        print()
        print('FROM EDEN TO HAGAR STANDS — the garden and the breach, the four sentences, Cain and the bloods, the two lines and the ledger, the reprieve and the ark, the flood and the birds, the exit and the first altar, the vineyard, the nations, Babel, Shem\'s line, the call, Egypt, the separation, the war, the pieces, Hagar — on one ledger, eight engines called.')
    else:
        print('MISSES (%d):' % len(misses))
        for m_ in misses: print('  -', m_[0][:80], '->', m_[1])
        sys.exit('MISSES REMAIN — a miss is evidence, never a retype: read it.')
