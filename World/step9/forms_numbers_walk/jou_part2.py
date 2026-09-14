

# ===== THE DATA CHANNEL — the parameter rows the ink leaves open (motion 2's recorded settings) =========
DATA = {
    'the_stations': {'value': STATIONS, 'settings': {'a_data_list': "THE FORTY-TWO AS A DATA ROW, NOT TAPE LINES (the design's decision on the measurements): a retelling never writes an act twice — sixteen camps stand on the ledger at their first tellings' own days; the chapter's lines land at (40, 6, 1) and a year-one camp cannot carry the record's day; the ink's own verb for the chapter is WROTE (33:2), whose value is the list", 'tape_lines': "the eighteen only-here stations as encamped_at statuses at (40, 6, 1) — REFUSED: false on the clock (no day of their own in the ink)"},
                     'source': "33:5-49 — the forty-two places cut from the verbs' after-tokens on the DB; each place's first telling by its lemma's seats; the tape's witness from the running world's markers and statuses (jou_compile_measure.out)"},
    'the_four_writings': {'value': ['Exod 24:4', 'Num 33:2', 'Deut 31:9', 'Deut 31:22'], 'settings': {'four': "'and Moses wrote' at four Torah seats — the covenant's words (Exodus 24:4), THE JOURNEYS (33:2), this Torah (Deuteronomy 31:9), this song (31:22); the tablets at Exodus 34:28 and Deuteronomy 10:4 the verb's other two seats (the LORD's writing)"},
                          'source': "33:2 'and Moses wrote' — the phrase's seats computed (WROTE)"},
    'the_morrow_of_the_passover': {'value': 'the_omer_then_the_produce', 'settings': {'the_omer_then_the_produce': "Joshua 5:11 'they ate of the produce of the land on the morrow of the Passover' — they brought the omer and only afterward ate (Kiddushin 37b:14-38a:1: the new crop's 'dwelling' is wherever you dwell)", 'the_manna_sufficed': "they did not need the new produce, for they still had manna (Kiddushin 38a:2) — the manna's end the morrow's meaning (38a:3-4: forty years less thirty days, the sixteenth of Iyar to the sixteenth of Nisan; Joshua 5:12 'the manna ceased on the morrow')"},
                                   'source': "33:3 'on the morrow of the Passover' and Joshua 5:11 — THE PHRASE'S TWO BIBLE SEATS (MORROW): the going out of Egypt and the land's bread on one date-word; Seder Olam Rabbah 10:2 the same reckoning"},
    'the_judgments_on_the_gods': {'value': 'recorded_at_33_4_alone', 'settings': {'recorded_at_33_4_alone': "Exodus 12:12 'on all the gods of Egypt I will execute judgments' THE SPEC (the future at 12:12 and Ezekiel 25:11 alone); Exodus narrates the firstborn struck (12:29) and never the gods; 'and on their gods the LORD executed judgments' (33:4) the perfect's ONE seat — the run recorded forty years on, in the itinerary; Onkelos 'on their idols'"},
                                  'source': "33:4 against Exodus 12:12 — the verb's forms computed (JUDG_PERF, JUDG_FUT, the noun's sixteen seats); NO entry on the tape before 33:4 carries the judgments (measured)"},
    'the_deuteronomy_order': {'value': 'the_retreat_of_seven_stations', 'settings': {'the_retreat_of_seven_stations': "Deuteronomy 10:6 'from Beeroth-bene-jaakan to Moserah; THERE Aaron died' against 33:30-31 (Moseroth then Bene-jaakan) and 33:37-38 (the death at Mount Hor): after Arad's attack they retreated seven stations to Moserah and the mourning was renewed there (Seder Olam Rabbah 9:2 — 'did Aaron die in Moserah? did he not die at Mount Hor? rather, from where Aaron died they retreated seven stations') — the chukat runner's row CK.DATA['moserah'] READ", 'the_ink_alone': "two orders in the ink, no rule between them — Deuteronomy's Beeroth-bene-jaakan and Gudgodah another lemma from 33:31-32's Bene-jaakan and Hor-haggidgad"},
                              'source': "33:30-38 against Deuteronomy 10:6-7 — MOSEROTH SEVEN CAMPS BEFORE MOUNT HOR BY INDEX (computed on the list): the shelf's seven = the ink's seven"},
    'arads_hearing': {'value': CK.DATA['arad_heard']['value'], 'settings': dict(CK.DATA['arad_heard']['settings'], **{'sihon_arad_canaan_one_person': "Rosh Hashanah 3a:3 — 'he is Sihon, he is Arad, he is Canaan': one person under three names (the foal, the kingdom, the real name Arad — or the wild ass, the kingdom, the real name Sihon): the hearer's identity DISPUTED; Taanit 9a's Amalek in disguise the registry row's other reading"}),
                      'source': "33:40 'and the Canaanite king of Arad heard' — 21:1's hearing without the war, the captives, the vow and Hormah, WITH 'in the land of Canaan'; CK's row READ by CALL (Rosh Hashanah 3a:1; Taanit 9a:10; Seder Olam Rabbah 9:2)"},
    'aarons_age': {'value': 123, 'settings': {'83_plus_40': "Aaron 83 at the speaking before Pharaoh (Exodus 7:7 — [80, 83]) + the era's fortieth year = 123 (33:39 — [123]); Moses 80 + 40 = 120 (Deuteronomy 34:7 — [120]): the brothers three years apart at both ends, THE INK'S OWN CHECKSUM; Kiddushin 38a:7 — 'a hundred and twenty years old THIS DAY': the years of the righteous completed to the day (Exodus 23:26)"},
                   'source': "33:39 by the same parser as Exodus 7:7 and Deuteronomy 34:7 (RETOLD); CK.AARON_AGE READ"},
    'the_death_date': {'value': AARON_DATE, 'settings': {'ordinal_reader': "33:38 'in the fortieth year … in the fifth month, on the first of the month' — the year and the month article-bearing ORDINALS [40, 5], the day [1]: THE TAPE'S OWN MARKER at 20:28 is built from this verse (cold_run_sequence.py); Deuteronomy 1:3's fortieth-year date is CARDINAL ([40, 11, 1] by the number reader): the two date forms have two readers", 'first_of_av_or_tammuz': "Seder Olam Rabbah 10:2 'Aaron on the first of Av' with the export's note of the French manuscripts' 'first of Tammuz' — a variant on the month the ink fixes as the fifth (OBSERVED, RESEARCH_LOG)"},
                       'source': "33:38 — the ordinals and the number computed (ORDS, INTS); CK.AARON_DATE READ; the marker at Num 20:28 on the tape (CZ5)"},
    'the_eras_stamps': {'value': ['Exod 19:1', 'Num 33:38', '1Kgs 6:1'], 'settings': {'three_stamps': "'of the going out of the children of Israel from the land of Egypt' at THREE Bible seats — Exodus 19:1 (the third month), Numbers 33:38 (the fortieth year), 1 Kings 6:1 (the 480th year — [480] with the ordinal [2] by the parser): the era's own dating form; Rosh Hashanah 2b:7-3a:13 reads the three in one chain to prove the New Year for the exodus count and the kings is Nisan (2b:9 — Av and the following Shevat both 'the fortieth year'; 2b:11 the verbal analogy 'the fortieth year' TAUGHT for Deuteronomy 1:3's bare date; 3a:5 Nisan and Iyar both 'the second year'; 3a:6 'the third month' without 'the second year')"},
                        'source': "33:38 — the phrase's three seats computed (STAMPS); the engine's Calendar with the exodus era's new year in the first month reproduces the chain (ERA_AV, ERA_SHEVAT, ERA_NISAN2, ERA_IYAR2)"},
    'the_camps_extent': {'value': 'three_parasangs', 'settings': {'three_parasangs': "'from Beth-jeshimoth to Abel-shittim' (33:49) — Rabba bar bar Chana in R. Yochanan's name: 'I saw that place, three parasangs by three' (twelve mil) — Eruvin 55b:15 (Rav Chisda's objection), Yoma 75b:14 (the baraita on relieving oneself behind the camp)"},
                         'source': "33:49 — the itinerary's ONE camp with two ends (Beth-jeshimoth one seat; Abel-shittim one seat of the full name); the shelf's measure a witness's"},
    'the_three_objects': {'value': ['figured_stones', 'molten_images', 'high_places'], 'settings': {'figured_stones': "Leviticus 26:1's word (the lemma's six Bible seats: Lev 26:1, Num 33:52, Ezek 8:12, Ps 73:7, Prov 18:11, 25:11) — the ban 'a figured stone you shall not install in your land to bow upon it': Ulla, bowing on a stone floor outside the Temple with outstretched arms and legs (Megillah 22b:11-13); THE CELL THAT COMPILES LEVITICUS 26:1 DOES NOT EXIST (measured) — journeys → tochacha OWED, the rows filed to the debt", 'molten_images': "the calf's word (Exodus 32:4, 32:8; Deuteronomy 9:12, 9:16) and the ban's — 'molten gods you shall not make for yourself' (Exodus 34:17; Leviticus 19:4 with the vav; Deuteronomy 27:15 the curse): ER.covenant('molten_two_seats') and HL.frame('molten_warnings') by CALL; aaron's molten_image_barred block on the tape (Exodus 32:4)", 'high_places': "Leviticus 26:30's curse in the same verb on the same object — 'I will DESTROY your high places' / 'their high places you shall DEMOLISH' (the verb's two Torah seats; the noun's five): the Canaanites' — ANOTHER SENSE than the private altar's eras (Mishnah Zevachim 14:4-8: Israel's own altars permitted and forbidden by era — the erection runner's high_places_banned block on the land); 'their high places' the consonants of 'at their death' (Leviticus 11:31-32, Numbers 6:7 — the morphology decides)"},
                          'source': "33:52 — the three objects' tokens and their seats computed; the other iconoclasm commands (Exodus 23:24, 34:13, Deuteronomy 7:5, 12:2-3) name altars, pillars, asherim and graven images — ER.covenant('demolition_grows') [3, 4, 5] by CALL: 33:52's three are its own list"},
    'the_lot_restated': {'value': 'plural_then_singular', 'settings': {'plural_then_singular': "33:54 restates 26:52-56 TO THE PEOPLE: 'you (plural) shall inherit … to the many you (PLURAL) shall give more … to the few you (SINGULAR) shall give less' — the number switches inside the verse (26:54 'to the many you shall give more' singular): computed on the morphology (MORPH_54); Onkelos makes both plural; C2.the_land('by_lot' / 'by_number_of_names') by CALL, C2.DATA['division_by'] = tribes READ; the OPEN divide_the_land debit (26:52-56) CITED, NOT REWRITTEN"},
                         'source': "33:54 against 26:52-56 — the shared clauses computed (BY_LOT_T, MANY, LOT_OUT, TRIBES_FATHERS); Bava Batra 117a:2-3, 117b:1 (left Egypt / entered / both), 122a:3 (the lot and the Urim) credited"},
    'negative_arm_outcome': {'value': 'thorns_in_your_eyes_and_pricks_in_your_sides', 'settings': {'thorns_in_your_eyes_and_pricks_in_your_sides': "33:55 'those you leave of them shall be thorns in your eyes and pricks in your sides, and they shall harass you on the land' — run back REVERSED by Joshua 23:13 ('a snare and a trap, a scourge in your sides and pricks in your eyes') and Judges 2:3 ('for sides, and their gods a snare'); 33:56 'as I thought to do to them, I will do to you' (Isaiah 14:24's phrase); Onkelos: bands taking up arms against you and camps surrounding you", 'sauls_amalek_and_haman': "Megillah 11a:13-14 — R. Levi and R. Chiyya open Esther from 33:55-56: Saul's failure to finish Amalek left Haman as the thorn; Purim's punishment 'as I thought to do to them' — the arm's runs on the shelf beyond Joshua and Judges", 'the_crossings_purpose': "Sotah 34a:5 — Joshua in the Jordan: 'know for what purpose you cross — to drive out the inhabitants (33:52); if not, the water will drown me and you': the debit's first run-reading with the negative arm as its condition"},
                             'source': "33:55-56 — the ink's three seats (THORNS, PRICKS, PRICKS_EYES, SIDES_JUDG, THOUGHT); NO verdict on the tape — the arm a DATA row; GR.DATA['negative_arm_outcome'] the chapter-32 arm beside it"},
}


# ===== F1: THE HEADING AND THE WRITING (Num 33:1-2) ===========================================================
def the_heading_and_the_writing(case, data):
    del P[:]
    ask = case['ask']
    if ask == 'heading':
        ink('33:1', '"these are the journeys of the children of Israel" — %s (10:28 the same four words: "these are the journeys of the children of Israel by their hosts, and they journeyed"); %d verse-initial "these" headings in the Torah' % (HEAD, len(HEADINGS)))
        return out("these are the journeys of the children of Israel (33:1) — 10:28's four words; sixty-three headings in the Torah", ['accepted'])
    if ask == 'by_their_hosts':
        ink('33:1', '"by their hosts" — %d seats, every one in Numbers (%s … %s)' % (len(HOSTS), HOSTS[0], HOSTS[-1]))
        return out("by their hosts (33:1) — sixteen seats, all in Numbers", ['accepted'])
    if ask == 'by_the_hand':
        ink('33:1', '"by the hand of Moses and Aaron" — %s: the phrase\'s two Bible seats; Psalm 77:21 "You led Your people like a flock by the hand of Moses and Aaron" OBSERVED, no link' % HAND)
        return out("by the hand of Moses and Aaron (33:1) — Psalm 77:21 the phrase's other seat, observed", ['accepted'])
    if ask == 'moses_wrote':
        ink('33:2', '"and Moses wrote" — %s: THE FOUR WRITINGS (the covenant\'s words, the journeys, this Torah, this song); the tablets Exodus 34:28 and Deuteronomy 10:4 the verb\'s other two' % WROTE)
        dat('the row the_four_writings: %s' % data['the_four_writings']['value'])
        return out("and Moses wrote (33:2) — the four writings: Exodus 24:4, Numbers 33:2, Deuteronomy 31:9, 31:22", ['journeys_recorded'])
    if ask == 'by_the_mouth':
        ink('33:2, 38', '"by the mouth of the LORD" — %d Bible seats, %d in the Torah, %d in Numbers; Moses WROTE by it (33:2) and Aaron WENT UP by it (33:38); Onkelos "by the WORD of the LORD" at both' % (len(MOUTH), len(MOUTH_T), len(MOUTH_N)))
        move('Bava Batra 17a:3', 'six over whom the Angel of Death had no sway — Moses, Aaron and Miriam died BY THE MOUTH OF THE LORD (33:38; Deuteronomy 34:5): the kiss')
        move('cold_run_chukat (CALL) — CK.meribah(death_by_the_kiss) = %s' % CK_KISS[0], "the chukat runner's row death_by_the_kiss READ")
        return out("by the mouth of the LORD — twenty-one Bible seats; Moses wrote by it (33:2), Aaron went up by it (33:38), and died by it on the shelf (Bava Batra 17a:3)", ['accepted'])
    if ask == 'the_chiasm':
        ink('33:2', '"their goings out by their journeys … their journeys by their goings out" — %s / %s; "their goings out" %s (Jeremiah 50:7 the other seat); "by their journeys" %s (the cloud\'s stages at Exodus 17:1, Numbers 10:6, 10:12)' % (words(33, 2)[3:5], words(33, 2)[9:11], GOINGS, JOURNEYS_L))
        return out("their goings out by their journeys, their journeys by their goings out (33:2) — the chiasm; 'their goings out' two Bible seats, 'by their journeys' four", ['accepted'])
    if ask == 'the_list':
        ink('33:2, 5-49', 'the writing\'s VALUE — %d places: %s … %s; %d named nowhere else; %d with a first telling outside the chapter; %d with a witness on the tape' % (len(STATIONS), STATIONS[0]['en'], STATIONS[-1]['en'], sum(1 for s in STATIONS if s['only_here']), sum(1 for s in STATIONS if s['first_telling']), sum(1 for s in STATIONS if s['witness'] != '-')))
        dat('the row the_stations: a DATA LIST, not tape lines — a retelling never writes a camp twice; the record\'s day the writing\'s')
        return out("the journeys recorded — forty-two places as the writing's value: Rameses and forty-one camps, eighteen named nowhere else, eighteen with a first telling, seventeen with a witness on the tape", ['journeys_recorded'])
    return out('no verdict in span', [FX.NONE])


# ===== F2: THE DEPARTURE (Num 33:3-4) — the tape's own date; the run of Exodus 12:12 recorded here alone ========
def the_departure(case, data):
    del P[:]
    ask = case['ask']
    if ask == 'the_date':
        ink('33:3', '"from Rameses in the first month, on the fifteenth day of the first month" — [%d] with the ordinals %s = %s; the full phrase %s (one seat); "from Rameses" %s' % (FIFTEEN, ORDS[3], DEPARTURE_DATE, FIFTEENTH, FROM_RAMESES))
        move('the Calendar (the exodus era registered at Exodus 12:2)', 'day_in(1, 1, 15) reads back %s — the tape\'s exodus marker at Exodus 12:29 and 12:41 (CZ3)' % (_EX.date(_WC.clock.day_in('exodus', 1, 1, 15)),))
        return out("the fifteenth day of the first month (33:3) = (1, 1, 15) — the tape's exodus marker; a retelling's date is a checkpoint, never a second marker", ['accepted'])
    if ask == 'the_morrow':
        ink('33:3', '"on the morrow of the Passover" — %s: the phrase\'s two Bible seats, the going out of Egypt and the land\'s bread (Joshua 5:11); the Passover\'s lemma at %s' % (MORROW, PASSOVER_LEMMA))
        move('Kiddushin 37b:14-38a:2', "the new crop's 'dwelling' wherever you dwell — they ate on the morrow after the omer (38a:1); or the manna sufficed (38a:2)")
        dat('the row the_morrow_of_the_passover: %s' % data['the_morrow_of_the_passover']['value'])
        return out("on the morrow of the Passover — 33:3 and Joshua 5:11 the phrase's two seats: the run's two ends on one date-word; the omer's arm and the manna's", ['accepted'])
    if ask == 'left_by_day':
        ink('33:3', '"on the morrow of the Passover the children of Israel went out with a high hand in the sight of all Egypt" — "in the sight of all Egypt" %s (one seat)' % SIGHT)
        move('Berakhot 9a:25', 'R. Abba: redeemed at evening (Deuteronomy 16:1), LEFT BY DAY — 33:3 the proof')
        move('cold_run_exodus_story (CALL) — ES.night(by_day) = %s' % ES_DAY['v'], "'on that very day' (12:51): they went out by day only (Mekhilta)")
        return out("left by day (33:3) — redeemed at evening, went out by day (Berakhot 9a:25); the exodus story's by_day by CALL", ['accepted'])
    if ask == 'high_hand':
        ink('33:3', '"with a high hand" — %s: three Torah seats (Exodus 14:8 the same going out; 15:30 the Sifrei 112:2\'s verse; here); Onkelos "with bared head" at 15:30 and 33:3 alone' % HIGH_HAND)
        move('cold_run_shelach (CALL) — SL.high_hand(high_hand_posture) = %s' % SL_HIGH[0], 'the callee names this chapter\'s verse')
        return out("with a high hand (33:3) — Exodus 14:8's posture at the same going out, 15:30's the high-hand sinner's; the shelach runner names 33:3", ['accepted'])
    if ask == 'the_burial':
        ink('33:4', '"and Egypt was burying those whom the LORD had struck among them, every firstborn" — "was burying" %s (the participle\'s two seats); "every firstborn" %d seats' % (BURYING, len(EVERY_FB)))
        move('cold_run_exodus_story (CALL) — ES.plagues(ten) = %d, (removed) = %d; ES.PLAGUES[-1] = %s; the removed %s' % (ES_TEN['v'], ES_REM['v'], ES.PLAGUES[-1], sorted(ES.REMOVED)), 'ten struck, four removed by a narrated removal — the firstborn\'s has none: A BURIAL IS NOT A REMOVAL, the entry stays OPEN (CZ4)')
        move('cold_run_pesach (CALL) — PS.firstborn(human) = %s' % PS_FB[0], "the Passover's firstborn cell live")
        return out("Egypt was burying every firstborn (33:4) — the plague's aftermath: the firstborn's plague_struck entry stays open, a burial is no removal (ten struck, four removed)", ['accepted'])
    if ask == 'the_gods_judged':
        ink('33:4', '"and on their gods the LORD executed judgments" — the perfect %s (ONE Bible seat); the future "I will execute judgments" %s (Exodus 12:12 THE SPEC, Ezekiel 25:11); the noun\'s %d seats' % (JUDG_PERF, JUDG_FUT, len(JUDG_LEMMA)))
        dat('the row the_judgments_on_the_gods: %s — Exodus narrates the firstborn and never the gods; NO entry on the tape before 33:4 carries the judgments (measured): the act\'s FIRST telling, forty years on' % data['the_judgments_on_the_gods']['value'])
        return out("on their gods the LORD executed judgments (33:4) — the run of Exodus 12:12 recorded here alone: a status on Egypt written forty years on, the act's first telling", ['judgments_executed_on_their_gods'])
    if ask == 'the_manna':
        move('Kiddushin 38a:3-4', 'the manna forty years less thirty days — from the sixteenth of Iyar of the first year to the sixteenth of Nisan of the fortieth; the cakes taken out on the fifteenth of Nisan tasted of manna thirty days')
        move('cold_run_exodus_story (CALL) — ES.manna(forty_years) = %d' % ES.manna('forty_years')['v'], "'until they came to an inhabited land' (Exodus 16:35) — the provision's span past the three books")
        ink('33:3', 'the Calendar: the manna\'s first morning %s = the tape\'s marker at Exodus 16:13; the cakes\' day %s = the exodus marker' % (_EX.date(_WC.clock.day_in('exodus', 1, 2, 16)), DEPARTURE_DATE))
        return out("the manna forty years less thirty days (Kiddushin 38a:3-4) — from (1, 2, 16), the tape's marker at Exodus 16:13, to the sixteenth of Nisan; the cakes of 33:3's fifteenth thirty days", ['accepted'])
    return out('no verdict in span', [FX.NONE])


# ===== F3: THE STATIONS (Num 33:5-37, 41-49) — the list against its first tellings, on the tokens ============
def the_stations(case, data):
    del P[:]
    ask = case['ask']
    if ask == 'forty_two':
        ink('33:3-49', '%d places = the forty-one departures\' places (Rameses told twice, 33:3 and 33:5) + the last camp; the departures\' from-tokens and the camps\' at-tokens the instrument' % len(PLACES_HE))
        return out("forty-two places (33:3-49) — Rameses and forty-one camps: the first departure and the last camp each told twice", ['accepted'])
    if ask == 'the_verbs':
        ink('33:3-49', '"journeyed" in %d verses (%s …), "camped" in %d (… %s); %d verses with both; 33:3 the journey alone (the date line), 33:49 the camp alone (the last camp\'s extent)' % (len(JOURNEYED), JOURNEYED[:3], len(CAMPED), CAMPED[-3:], len(set(JOURNEYED) & set(CAMPED))))
        return out("forty-two 'journeyed' and forty-two 'camped' — forty-one verses with both; 33:3 the journey alone, 33:49 the camp alone", ['accepted'])
    if ask == 'exodus_nine':
        move('cold_run_exodus_story (CALL) — ES.night(stations) = %d, its effects %s' % (ES_ST['v'], ES_ST['fx']), "the exodus story's nine encampments (Succoth, Etham, Pi-hahiroth, Shur, Marah, Elim, Sin, Rephidim, Sinai) — its why names Numbers 33's list as the run's citation")
        ink('33:5-15', 'the tape\'s witnesses among them: %s' % [(s['en'], s['witness']) for s in STATIONS[:12] if s['witness'] != '-'])
        return out("the exodus story's nine stations by CALL — Succoth to Sinai on the tape as statuses and markers; the itinerary's list their run citation", ['accepted'])
    if ask == 'etham_for_shur':
        ink('33:8', '"a way of three days in the wilderness of ETHAM" for Exodus 15:22\'s "wilderness of SHUR" — %s / %s (each one seat with its prefix); the bare pair "מדבר אתם" at %s is "speaking with them" — A HOMOGRAPH (the measure\'s find); "a way of three days" %s' % (words(33, 8)[11:13], SHUR, ETHAM_HOMOGRAPH, THREE_DAYS))
        move('cold_run_exodus_story (CALL) — ES.marah(three_days) = %d' % ES.marah('three_days')['v'], "the tape's marker at Shur (1, 1, 24)")
        return out("the wilderness of Etham (33:8) for Exodus 15:22's Shur — each one seat; 'a way of three days' six Torah seats; Exodus 34:33's 'speaking with them' a homograph", ['accepted'])
    if ask == 'one_word_added':
        ink('33:6', '33:6 %s IS Exodus 13:20 %s with ONE word added ("which")' % (words(33, 6), words(13, 20, 'Exod')))
        return out("33:6 is Exodus 13:20 with one word added — the itinerary retelling its first telling on the tokens", ['accepted'])
    if ask == 'elim':
        ink('33:9', '"twelve springs of water and seventy palm trees" — %s / %s: word for word with Exodus 15:27; the parser [%d, %d] at both' % (SPRINGS, PALMS, TWELVE, SEVENTY))
        return out("Elim's twelve springs and seventy palms (33:9) word for word with Exodus 15:27 — [12, 70] at both", ['accepted'])
    if ask == 'unnamed_in_exodus':
        ink('33:10-13', 'THE CAMP BY THE RED SEA (33:10 — "the Red Sea" %d Torah seats, the camp Exodus never names), DOPHKAH and ALUSH (33:12-13) — three stations between Elim and Rephidim that Exodus does not tell' % len(RED_SEA_T))
        return out("the Red Sea camp, Dophkah and Alush (33:10-13) — three stations Exodus never names", ['accepted'])
    if ask == 'kibroth_hazeroth':
        move('cold_run_beha (CALL) — BH.taberah_and_quail(graves) = %s; BH.march(day_stack) = %s' % (BH_GRAVES[0], BH_STACK[0]), "the naming 11:34 ('buried' on the tape); Hazeroth (2, 3, 22) and Paran (2, 3, 29) the tape's markers")
        ink('33:16-17', 'Kibroth-hattaavah and Hazeroth — 11:34-35\'s names; Onkelos "the graves of those who demanded" at all four seats')
        return out("Kibroth-hattaavah and Hazeroth (33:16-17) — chapter 11's graves and Hazeroth by CALL: the burial on the tape, the markers at (2, 3, 22) and (2, 3, 29)", ['accepted'])
    if ask == 'rithmah_paran':
        ink('33:18', '"Rithmah" %s — one seat: 12:16\'s "wilderness of Paran" under another name, the spies\' base (13:3 "from the wilderness of Paran", 13:26 "to Paran, to Kadesh"); Taberah no station' % RITHMAH)
        move('cold_run_shelach (CALL) — SL.spies(forty_days) = %s' % SL_FORTY[0], 'the forty days from the base; the tape\'s marker at 12:16 (2, 3, 29)')
        return out("Rithmah (33:18) — Paran under another name: the spies' base of 12:16, 13:3, 13:26; the tape's marker at (2, 3, 29)", ['accepted'])
    if ask == 'only_here':
        ink('33:10-46', '%d stations by lemma with no seat outside the chapter — %s; the eighteenth %s (a common noun, no proper-name lemma)' % (len(ONLY_HERE), ONLY_HERE, NO_LEMMA))
        return out("eighteen stations named nowhere else — seventeen by lemma (Dophkah to Almon-diblathaim) and the Red Sea camp", ['accepted'])
    if ask == 'common_word_names':
        ink('33:20, 26, 27', 'Libnah (the Judah city\'s lemma — Joshua 10:29 its first seat), Tahath (a Chronicles person\'s), Terah (Abraham\'s father\'s) — three names whose lemma\'s other seats are ANOTHER referent; Mount Shepher, Haradah, Tahath common words by consonants')
        return out("Libnah, Tahath, Terah (33:20, 26, 27) — three names whose lemma's other seats are another referent", ['accepted'])
    if ask == 'moseroth_seven':
        ink('33:30-38', 'Moseroth index %d, Mount Hor index %d — SEVEN CAMPS APART on the list; Deuteronomy 10:6 %s "there Aaron died", 10:7 %s' % (PLACES_EN.index('Moseroth'), PLACES_EN.index('Mount Hor'), words(10, 6, 'Deut')[3:9], words(10, 7, 'Deut')[:6]))
        move('Seder Olam Rabbah 9:2', "'did Aaron die in Moserah? did he not die at Mount Hor? rather, from where Aaron died they retreated seven stations until Moserah' — the shelf's seven = the ink's seven")
        move('cold_run_chukat (CALL) — CK.edom_and_hor(moserah) = %s; CK.DATA[moserah] = %s' % (CK_MOSERAH[0], CK.DATA['moserah']['value']), "the chukat runner's row READ")
        dat('the row the_deuteronomy_order: %s' % data['the_deuteronomy_order']['value'])
        return out("Moseroth seven camps before Mount Hor (33:30-37) — Deuteronomy 10:6's 'there Aaron died' at Moserah reconciled by the retreat of seven stations (Seder Olam Rabbah 9:2; the chukat runner's row)", ['accepted'])
    if ask == 'kadesh_hor':
        ink('33:36-37', '"in the wilderness of Zin, that is Kadesh" — the pair %s: Genesis 14:7 and here THE PLACE, Exodus 30:32, Leviticus 25:12, 27:30 "it is HOLY" — a homograph the reading\'s "five seats of the identity idiom" did not name (filed); "in the edge of the land of Edom" %s beside 20:23\'s "border" %s; "Mount Hor" bare at %s' % (THAT_IS_KADESH, EDGE_EDOM, BORDER_EDOM, HOR))
        move('cold_run_chukat (CALL) — CK.edom_and_hor(two_mount_hors) = %s' % CK_TWO[0], "Aaron's at Edom's border, the northern border's (34:7-8)")
        return out("Kadesh and Mount Hor (33:36-37) — 'that is Kadesh' with Genesis 14:7 (three of the pair's five seats read 'it is holy': a homograph); the edge of Edom one seat; two Mount Hors by CALL", ['accepted'])
    if ask == 'chapter_21':
        ink('33:41-47', 'Zalmonah and Punon named here alone (21:4 names no camp before Oboth); Oboth and Iye-abarim 21:10-11\'s; of 21:18-20\'s stations (Mattanah, Nahaliel, Bamoth, Pisgah) NOT ONE in the itinerary; Dibon-gad %s / %s; "the mountains of Abarim" %s beside 27:12\'s "the mountain of Abarim" %s' % (words(33, 45)[-2:], words(33, 46)[1:3], ABARIM_PL, ABARIM_SG))
        move('cold_run_gad_reuben (CALL) — GR.the_cities(dibon_gad) = %s' % GR_DIBON[0], "the Gad runner's own cell names 33:45-46")
        return out("the last stations against chapter 21 — Zalmonah and Punon only here; Oboth and Iye-abarim shared; 21:18-20's stations absent; Dibon Gad the Gad runner's own witness by CALL; the mountains of Abarim before Nebo", ['accepted'])
    if ask == 'the_last_camp':
        ink('33:48-49', '"the plains of Moab by the Jordan at Jericho" — "by the Jordan at Jericho" %s; "from Beth-jeshimoth to Abel-shittim" — Beth-jeshimoth %s, the full Abel-shittim one seat (%s the short name\'s)' % (JERICHO, BETH_J, SHITTIM))
        move('cold_run_balak (CALL) — BK.the_call(last_camp) = %s; BK.peor(shittim_name) = %s' % (BK_LAST[0], BK_SHITTIM[0]), "the last camp; Shittim's name")
        move('Eruvin 55b:15; Yoma 75b:14', "Rabba bar bar Chana: 'I saw that place — three parasangs by three'")
        dat('the row the_camps_extent: %s' % data['the_camps_extent']['value'])
        return out("the plains of Moab (33:48-49) — the last camp by CALL; from Beth-jeshimoth to Abel-shittim three parasangs on the shelf (Eruvin 55b:15; Yoma 75b:14)", ['accepted'])
    if ask == 'directional_ending':
        ink('33:46-47', '"Diblathaimah" %s — the directional ending on the station\'s name (Elimah at 33:9 the same form)' % DIBLATHAIMAH)
        move('Yevamot 13b:6', "R. Nechemya: a word needing a lamed at its head takes a heh at its end — 'Diblathaimah' among the examples")
        return out("Diblathaimah (33:46-47) — the directional ending on the station's name (Yevamot 13b:6's example)", ['accepted'])
    if ask == 'tape_matched':
        ink('33:5-49', 'the tape\'s camps the list names: %s; the tape\'s statuses the list does not name: %s' % (TAPE_CAMPS_MATCHED, TAPE_CAMPS_UNMATCHED))
        return out("the tape's camps against the list — twelve names matched (Succoth to the plains of Moab), five statuses not (Goshen, Shur, the Red Sea way, Mattanah to Pisgah, Shittim)", ['accepted'])
    return out('no verdict in span', [FX.NONE])
