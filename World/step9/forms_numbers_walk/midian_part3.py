

# ===== F4: THE PURIFICATION (Num 31:19-20 with 31:24) =========================================================
def the_purification(case, data):
    del P[:]
    ask = case['ask']
    if ask == 'outside_the_camp':
        ink('31:19', '"and you, encamp outside the camp seven days" — %s (Miriam\'s seven at 12:15 the other seat); the parser\'s %s' % (OUTSIDE_SEVEN, INTS[19]))
        move('cold_run_chukat (CALL) — CK.corpse_tumah(camps) = %s' % CK_CAMPS[0], "the corpse-impure out of the Presence's camp alone (Kelim 1:8; 5:2)")
        return out("encamp outside the camp seven days (31:19) — the corpse-impure out of the Presence's camp alone (CK.corpse_tumah camps by CALL)", ['sent_outside_the_camp'])
    if ask == 'schedule':
        ink('31:19', '"whoever has killed a soul and whoever has touched a slain one, purify yourselves on the third day and on the seventh day, you and your captives" — %s; "you and your captives" %s; the ordinal reader\'s %s' % (THIRD_AND_SEVENTH, YOU_AND_YOUR_CAPTIVES, ORDINALS[19]))
        move('cold_run_chukat (CALL) — CK.corpse_tumah(schedule) = %s' % CK_SCHEDULE[0], "THE THREE TIMERS on the men of war and on the captives: corpse_unclean_seven_days due day + %d, sprinkling_due_third_day day + %d, sprinkling_due_seventh_day day + %d — chukat's own dues (the machine counts the days that pass)" % (SEVEN, THIRD_DUE, SEVENTH_DUE))
        return out("purify yourselves on the third day and on the seventh day, you and your captives (31:19) — the three timers, chukat's dues (day + 3, day + 7)", ['corpse_unclean_seven_days', 'sprinkling_due_third_day', 'sprinkling_due_seventh_day'])
    if ask == 'seven_days_floor':
        ink('31:24', '"and you shall wash your garments on the seventh day" — the seventh named for the wash'); dat('the row camp_entry_reading: %s (the seven_days_floor arm)' % data['camp_entry_reading']['value'])
        move('Bava Kamma 25b:13; cold_run_chukat (CALL) — CK.corpse_tumah(seven_days) = %s' % CK_SEVEN[0], "Rava: a Torah edict that what a corpse defiles stays impure no less than SEVEN DAYS — the vessels' seven the men's")
        return out("wash your garments on the seventh day (31:24) — what a corpse defiles stays impure no less than seven days (Bava Kamma 25b:13); CK seven_days by CALL", ['corpse_unclean_seven_days'])
    if ask == 'sword_like_slain':
        ink('31:19, 31:22', '"whoever has touched a slain one" beside the six metals — the warriors\' metal the seat (19:16\'s "slain by the sword"; Sifrei 158:3)')
        dat('the row sword_like_slain: %s (CK\'s row READ)' % data['sword_like_slain']['value'])
        move('cold_run_chukat (CALL) — CK.corpse_tumah(sword_like_slain) = %s' % CK_SWORD[0], "Nazir 53b:11; Pesachim 14b:1, 14b:5 — metal the one substance where the corpse's and the creeping animal's impurity differ; Chullin 3a:1 the knife")
        return out("a sword is like the slain — the metal takes the corpse's grade (Nazir 53b:11; Pesachim 14b:1, 14b:5; Chullin 3a:1) — the warriors' metal the seat", ['corpse_unclean_seven_days'])
    if ask == 'captives_sprinkled':
        ink('31:19', '"you AND YOUR CAPTIVES" — the captives sprinkled: the gentile\'s corpse defiles them by touch and carrying')
        dat('the row tent_gentile: %s (CK\'s row READ — its note names the Midian war)' % data['tent_gentile']['value'])
        move('cold_run_chukat (CALL) — CK.corpse_tumah(tent_gentile) = %s' % CK_TENT[0], "Yevamot 61a:1 (no tent — 'you are men'), 61a:5 (Ravina: excluded from the tent, not from touch and carrying — hence the Midian war's purification even per R. Shimon ben Yochai)")
        return out("the captives sprinkled — gentile corpses defile by touch and carrying, not by tent (Yevamot 61a:1, 61a:5): the Midian war the proof", ['sprinkling_due_third_day', 'sprinkling_due_seventh_day'])
    if ask == 'four_materials':
        ink('31:20', '"every garment, every vessel of skin, every work of goats, every vessel of wood you shall purify" — %s against Leviticus 11:32\'s %s ON THE DB: shared %s, sack there against goat-work here' % (NUM_MATERIALS, LEV_MATERIALS, SHARED_MATERIALS))
        move('Sifrei 157:8', "the freed-word identity of the two lists — what is said here is said there: the spun and woven, the vessels of skin and wood")
        return out("garment, vessel of skin, goat-work, vessel of wood (31:20) against Leviticus 11:32's wood, garment, skin, sack — three shared, sack there against goat-work here (computed on the DB)", ['accepted'])
    if ask == 'goat_work_reading':
        dat('the row goat_work_reading: %s' % data['goat_work_reading']['value'])
        move('Shabbat 64a:2-4, 64a:9; Chullin 25b:4; Sifrei 157:8', "spun and woven — the sack; reins and the belly band; the tails; horn and hoof in, birds' bones out")
        return out("spun and woven — the sack (Shabbat 64a:3; Sifrei 157:8); reins and the belly band (64a:4), the tails (64a:9), horn and hoof in, birds' bones out (Chullin 25b:4)", ['accepted'])
    if ask == 'the_transfer':
        move('Shabbat 64a:7-8, 64a:15; Bava Kamma 25b:6', "THE VERBAL ANALOGY 'garment and leather' between Leviticus 11:32 and Numbers 31:20 run both ways — as there only the spun and woven, so here; as here all work of goats, so there: THE TEACHER of the edge midian -> shemini (link: transfer); the free-word condition argued (64a:16-19)")
        return out("the verbal analogy garment / leather between Leviticus 11:32 and Numbers 31:20 run both ways (Shabbat 64a:7-8, 64a:15; Bava Kamma 25b:6) — the edge midian to shemini a TRANSFER taught; the free-word condition argued (64a:16-19)", ['accepted'])
    if ask == 'carcass_grade':
        move('cold_run_shemini (CALL) — SH.touch_effect(touch_carcass) = %s, (carry_carcass) = %s' % (SH_TOUCH[0], SH_CARRY[0]), "the carcass grade at Leviticus 11:24-25; THE LEVITICUS 11 RUNNER HAS NO VESSELS CELL — 11:32's list compared on the DB here, the cell OWED (COMPILE_DEBT)")
        return out("the carcass grade by call — touch impure until evening, carry wash and evening (Lev 11:24-25); the vessels' cell in shemini OWED", ['accepted'])
    if ask == 'camp_entry_reading':
        ink('31:24', '"and you shall wash your garments on the seventh day and be clean; and afterward you shall come into the camp" against 19:19\'s "and he shall be clean at evening"')
        dat('the row camp_entry_reading: %s' % data['camp_entry_reading']['value']); move('Sifrei 158:3', "the two-way likening — the camp after the wash, the purity at evening")
        return out("wash on the seventh day, be clean, then come into the camp (31:24) against 19:19's evening — Sifrei 158:3's two-way likening", ['declared_pure'])
    if ask == 'removes':
        move('cold_run_chukat (CALL) — CK.corpse_tumah(removes) = %s' % CK_REMOVES[0], "the vessel's toucher until evening (Nazir 54b:6; Mishnah Oholot 1:2-3) — the remove after the vessel is the evening's")
        return out("the vessel's toucher until evening (Nazir 54b:6; Oholot 1:2-3) — the removes by call", ['accepted'])
    if ask == 'receptacles':
        move('Mishnah Kelim 15:1', "vessels of wood, leather, bone or glass: flat clean, receptacles susceptible; broken clean; the forty-se'ah vessels clean")
        return out("vessels of wood and skin as receptacles (Mishnah Kelim 15:1) — the flat ones outside", ['accepted'])
    return out('no verdict in span', [FX.NONE])


# ===== F5: THE VESSELS — ELEAZAR'S STATUTE (Num 31:21-23) =====================================================
def the_vessels(case, data):
    del P[:]
    ask = case['ask']
    if ask == 'statute_head':
        ink('31:21', '"and Eleazar the priest said to the men of war who had gone to the battle: this is the statute of the Torah which the LORD commanded Moses" — %s (19:2 the heifer\'s head); the frame verbs %s: the priest\'s voice citing Moses' % (STATUTE_HEAD, FRAME_VERBS[3]))
        return out("this is the statute of the Torah (31:21) — 19:2's head, Eleazar speaking it: the third relayed form", ['commanded'])
    if ask == 'eleazar_before_his_teacher':
        move('Eruvin 63a:24', "R. Eliezer: who rules before his teacher is lowered — Eleazar's 'this is the statute' spoken in Moses' presence, though he said 'commanded to my father's brother, not to me'; Pesachim 66b:7 the same pair from the anger's side")
        return out("Eleazar lowered for ruling before his teacher (Eruvin 63a:24) — the relay a fault on the shelf; the installed_by class's witness", ['accepted'])
    if ask == 'installed_by':
        ink('31:21', 'no divine frame on the statute — Eleazar cites "which the LORD commanded Moses"; the chapter\'s frames %s' % [f[:2] for f in FRAME_VERBS])
        move('THE LOOP step 3 (installation_parameters.yaml); Menachot 77b:20', "BOOT with the class named — THE THIRD RELAYED FORM (the priest's voice citing Moses; 30:2's relay in Moses' voice; 36:6's relayed output); the installing acts erect institutions and the priest's relay erects none; the division's rates 'not for all generations' — the second pass (D2) decides")
        return out("installed_by boot — the priest's voice citing the LORD's command to Moses: the third relayed form, the class named; the second pass decides", ['accepted'])
    if ask == 'six_metals':
        ink('31:22', '"the gold, the silver, the bronze, the iron, the tin and the lead" — %s, every one with its article; the tin %s, the lead %s' % (METALS, TIN, LEAD))
        move('Shabbat 16b:2; Mishnah Kelim 11:1', "metal vessels impure BY TORAH LAW from this list; recast they revert (the Sages' decree — CK.corpse_tumah(metal_vessels_decree) READ: %s)" % CK_METAL[0])
        return out("gold, silver, bronze, iron, tin, lead (31:22) — tin's one Torah seat, lead's two; metal vessels impure by Torah law (Shabbat 16b:2; Kelim 11:1)", ['accepted'])
    if ask == 'kashering':
        material, use = case.get('material', 'metal'), case.get('use', 'fire')
        ink('31:23', '"everything that comes into the fire you shall pass through the fire and it shall be clean, only with the water of sprinkling it shall be purified; and everything that does not come into the fire you shall pass through water" — %s / %s: the ink\'s TWO branches' % (PASS_THROUGH_FIRE, WATER_OF_SPRINKLING))
        if material == 'earthenware':
            move('Pesachim 30b:8, 30b:2', "Ameimar: earthenware NEVER leaves its defective state — 'the Torah testified: broken' (Leviticus 6:21); the six metals the rule's whole class")
            return out("earthenware never purged — the Torah testified: broken (Leviticus 6:21; Pesachim 30b:8); the six metals the rule's whole class", ['exempt'])
        if use == 'fire':
            dat('the row immersion_source: %s' % data['immersion_source']['value'])
            return out("what comes into the fire — through the fire, and with the water of sprinkling purified (31:23): the first branch; the immersion added by the shelf", ['declared_pure', 'immersed'])
        return out("what does not come into the fire — through water (31:23): the second branch", ['immersed'])
    if ask == 'kashering_modes':
        dat('the row kashering_modes: %s' % data['kashering_modes']['value'])
        move('Mishnah Avodah Zarah 5:12 (= 75b:6); Avodah Zarah 75b:17, 76a:17, 76b:1-2; Pesachim 30b:5-6', "whiten the spit and the grill, boil the pot and the kettle, polish the knife — and immerse all; the baraita's four uses; as it absorbs so it emits")
        return out("whiten the spit and the grill, boil the pot and the kettle, polish the knife — and immerse all (Mishnah Avodah Zarah 5:12; the baraita's four uses, 75b:17)", ['immersed'])
    if ask == 'immersion_source':
        dat('the row immersion_source: %s' % data['immersion_source']['value'])
        move('Avodah Zarah 75b:7-11; Sifrei 158:2', "Rava: 'and it shall be pure' adds immersion in forty se'ah; Bar Kappara: 'nevertheless' excludes the third and seventh day's sprinkling — the water of niddah the menstruant's; the Sifrei's a-fortiori beside")
        return out("'and it shall be pure' adds immersion in forty se'ah (Rava, Avodah Zarah 75b:7); 'nevertheless' excludes the third and seventh day's sprinkling (Bar Kappara, 75b:8); the Sifrei 158:2's a-fortiori beside", ['immersed'])
    if ask == 'water_of_sprinkling':
        ink('31:23', '"only with the water of sprinkling it shall be purified" — %s here; the purify-verb\'s seats %s, all in 19 and 31' % (WATER_OF_SPRINKLING, PURIFY_3))
        move('cold_run_chukat (CALL) — CK.corpse_tumah(metal_vessels_decree) = %s' % CK_METAL[0], "the heifer's water by call; the shelf splits the phrase's sense — the menstruant's immersion water (Avodah Zarah 75b:9)")
        return out("the water of niddah — four Torah seats all in 19 and 31; the heifer's water by call: metal vessels keep their impurity until the sprinkling (Shabbat 16b); the shelf splits its sense (75b:9)", ['accepted'])
    if ask == 'same_day_pot':
        dat('the row kashering_modes (the same_day_pot arm): %s' % data['kashering_modes']['settings']['same_day_pot'][:60])
        move('Avodah Zarah 75b:21-76a:2; Pesachim 44b:15', "the Torah forbids only a pot used that same day; the rest a rabbinic fence")
        return out("the Torah forbids only a pot used that same day (Avodah Zarah 75b:21; Pesachim 44b:15); the rest a fence", ['accepted'])
    if ask == 'taste_as_substance':
        move('Nazir 37b:1; Pesachim 44b:13-16; Avodah Zarah 67b:6', "R. Akiva derives THE TASTE AS THE SUBSTANCE from the vessels of Midian; the Rabbis: the purging a NOVELTY — a taste that taints forbidden here alone; R. Meir's detriment principle on the same verses")
        return out("the taste as the substance from the vessels of Midian (R. Akiva — Nazir 37b:1; Pesachim 44b:13); the Rabbis: the purging a NOVELTY (44b:14)", ['accepted'])
    if ask == 'immersion_scope':
        dat('the row immersion_source (the scope arm): %s' % data['immersion_source']['settings']['scope'])
        move('Avodah Zarah 75b:12-15', "metal utensils alone; purchased as the captured were, not borrowed; even new; glass as metal; meal utensils")
        return out("metal utensils (75b:14), purchased as the captured (75b:13), even new (75b:12), glass as metal (75b:15) — the immersion's scope the passage's own", ['immersed'])
    if ask == 'as_it_absorbs':
        move('Avodah Zarah 76a:17, 76b:1; Pesachim 30b:6', "AS IT ABSORBS SO IT EMITS — Rava on Rav Akavya's cauldron; the measures: until the outer layer sheds, a kettle in a kettle")
        return out("as it absorbs so it emits (Avodah Zarah 76b:1; Pesachim 30b:6); the measures — until the outer layer sheds, a kettle in a kettle (76a:17)", ['accepted'])
    if ask == 'the_line':
        ink('31:21-24', "ONE line on the tape for the statute — Eleazar's speech at the counter's day, no marker; commanded on the men of war")
        return out("commanded on the men of war valued the_statute_of_the_vessels — the walk's form for a statute line (10b's commanded on israel)", ['commanded'])
    return out('no verdict in span', [FX.NONE])


# ===== F6: THE DIVISION (Num 31:25-47) ========================================================================
def the_division(case, data):
    del P[:]
    ask = case['ask']
    if ask == 'lift_the_head':
        ink('31:26', '"take the sum of the prey of the captives, of man and of beast, you and Eleazar the priest and the heads of the fathers\' houses of the congregation" — %s the singular imperative, one seat; Exodus 30:12\'s %s' % (LIFT_THE_HEAD, WHEN_YOU_LIFT))
        move('cold_run_incense_shekel (CALL) — IS.shekel(lift_head) = %s' % IS_LIFT, "the census idiom's seats named there — a REFERENCE by the shared words")
        return out("take the sum of the prey (31:26) — 'lift the head', the census idiom (Exod 30:12 by call), the singular imperative one seat", ['accepted'])
    if ask == 'halve':
        ink('31:27', '"and halve the prey between those who took the war, who went out to the army, and all the congregation" — the equal halves; the halving computed: %s // 2 = %s' % (TOTALS, WARRIORS))
        move('1 Samuel 30:24-25; Joshua 22:8 (OBSERVED)', "David's statute at Ziklag — 'as his share who goes down to the battle, so his share who stays by the baggage'; Joshua's 'divide the spoil with your brothers' — NO ROW OF THE DECLARED SHELF LINKS them to 31:27 (the docket found none): observed, not linked (THE LINK REVIEW LAW)")
        return out("halve the prey between those who took the war and all the congregation (31:27) — the equal halves; David's statute (1 Samuel 30:24-25) OBSERVED, no link on the declared shelf", ['accepted'])
    if ask == 'tribute_rate':
        ink('31:28-29', '"and levy a tribute to the LORD from the men of war who went out to the army: one soul of five hundred, of the persons, the cattle, the donkeys and the flock; from their half you shall take it and give it to Eleazar the priest, the LORD\'s heave-offering" — %s; THE RATE %s the parser\'s read (the one marked, the denominator starred); the tribute-word %s; "the LORD\'s heave-offering" %d seats' % (ONE_OF_FIVE_HUNDRED, TRIBUTE_RATE, TRIBUTE_TOKENS, len(HEAVE_OFFERING)))
        dat('the row tribute_rate_reading: %s' % data['tribute_rate_reading']['value']); move('Menachot 77b:20; Yoma 24a:5', "not one of ten and not for all generations; asked as a measure for the ash removal")
        return out("one soul of five hundred (31:28) — the rate Fraction(1, 500), the parser's read; not one of ten and not for all generations (Menachot 77b:20); asked as a measure (Yoma 24a:5)", ['heave_offering_given'])
    if ask == 'levites_rate':
        ink('31:30', '"and from the half of the children of Israel you shall take one held of fifty, of the persons, the cattle, the donkeys and the flock, of all the beasts, and give them to the Levites who keep the charge of the tabernacle of the LORD" — %s; THE RATE %s' % (ONE_HELD_OF_FIFTY, LEVITE_RATE))
        dat('the row levites_rate_reading: %s' % data['levites_rate_reading']['value']); move('Jerusalem Talmud Terumot 4:3:2; Mishnah Terumot 4:3', "R. Levi: 'all you take elsewhere shall be like this' — the terumah's average fiftieth FROM THIS VERSE: a TRANSFER taught")
        return out("one held of fifty (31:30) — Fraction(1, 50); the terumah's average rate (Mishnah Terumot 4:3; Jerusalem Talmud Terumot 4:3:2 — R. Levi from this verse): a TRANSFER taught", ['levites_portion_given'])
    if ask == 'levites_charge':
        ink('31:30, 31:47', '"the Levites who keep the charge of the tabernacle of the LORD" — %s; 1:53\'s charge' % KEEP_THE_CHARGE)
        move('cold_run_bamidbar (CALL) — BM.charges(houses_charges) = %s' % BM_CHARGES[0], "1:50-53's charge_kept on the Levites' ledger (the census daemon's) — a REFERENCE by the shared words")
        return out("to the Levites who keep the charge of the tabernacle of the LORD (31:30, 31:47) — 1:53's charge (BM.charges by call: gershon the woven, kohath the holy, merari the frame)", ['accepted'])
    if ask == 'three_debits':
        ink('31:26-30 / 31:31, 31:41, 31:47', 'ONE speech, THREE commands — the count and the halving (31:26-27), the tribute to the priest (31:28-29), the Levites\' share (31:30); THREE RECEIPTS "as the LORD commanded Moses" at %s' % [s for s in RECEIPT if s in ('Num 31:31', 'Num 31:41', 'Num 31:47')])
        return out("three commands in one speech — divide the prey, the tribute to the priest, the Levites' share — closed by value at 31:31, 31:41, 31:47", ['commanded'])
    if ask == 'the_count':
        ink('31:32-35', '"the prey, the rest of the plunder which the people of the army took: sheep %d, cattle %d, donkeys %d, persons %d" — the parser\'s numbers; every total a multiple of a thousand' % TOTALS)
        return out("the prey: 675,000 sheep, 72,000 cattle, 61,000 donkeys, 32,000 persons (31:32-35) — the parser's numbers, every total a multiple of a thousand", ['counted'])
    if ask == 'the_halving_check':
        ink('31:36, 31:43', '"the half, the portion of those who went out to the army" %s = "the half of the congregation" %s (%s one seat) = the totals halved — CHECK' % (WARRIORS, CONGREGATION, HALF_OF_THE_CONGREGATION))
        return out("the totals halved = the warriors' portion = the congregation's half: 337,500 / 36,000 / 30,500 / 16,000 (31:36-46) — CHECK", ['counted'])
    if ask == 'the_tribute_check':
        ink('31:37-41', '"the tribute to the LORD" %s = the warriors\' portion x %s — %d heads; "and Moses gave the tribute, the LORD\'s heave-offering, to Eleazar the priest, as the LORD commanded Moses" (31:41)' % (TRIBUTE, TRIBUTE_RATE, sum(TRIBUTE)))
        return out("the warriors' portion at one of five hundred = the tribute: 675 / 72 / 61 / 32 = 840 heads (31:37-40) — CHECK; given to Eleazar (31:41)", ['counted', 'heave_offering_given'])
    if ask == 'the_levites_share':
        ink('31:42-47', 'THE SHARE STATED AS A RATE AND NEVER AS A NUMBER — the congregation\'s half %s x %s = %s = %d heads COMPUTED, UNWRITTEN; ten times the priest\'s %d; "and Moses took ... the held one of fifty, of man and of beast, and gave them to the Levites" (31:47)' % (CONGREGATION, LEVITE_RATE, LEVITES, sum(LEVITES), sum(TRIBUTE)))
        return out("the congregation's half at one of fifty = 6,750 / 720 / 610 / 320 = 8,400 heads — COMPUTED, UNWRITTEN; ten times the priest's; given to the Levites (31:47)", ['levites_portion_given'])
    if ask == 'thing_parties':
        ink('31:32, 31:36, 31:37, 31:43', 'the ink\'s own nouns for the four counted things — the prey (המלקוח, %d seats), the portion of those who went out (חלק היצאים בצבא), the tribute (המכס), the half of the congregation (מחצת העדה)' % len(PREY_TOKENS))
        move('world_engine._write (ent.status[effect] = value)', "a counted STATUS overwrites — the sixteen values go on four thing parties, never on israel_people (601,730) or the Levites (23,000)")
        return out("the sixteen counted statuses on four thing parties — the prey, the warriors' portion, the tribute, the congregation's half — never on israel_people or the Levites (the status overwrite)", ['counted'])
    if ask == 'private_plunder':
        ink('31:53', '"the men of the host had taken spoil, every man for himself" — outside the count (the prey "the rest of the plunder", 31:32)')
        return out("the men of the host had taken spoil every man for himself (31:53) — outside the count", ['accepted'])
    if ask == 'register_gate':
        move('THE REGISTER GATE (register_census.py --strict)', "the four count lines (31:35, 31:36, 31:40, 31:46) LEDGER by the counted statuses on the thing parties; the four receipts (31:7, 31:31, 31:41, 31:47) CLOSE by the notes; 31:28's rate a MEASURE (register_probes R7 — a Fraction leaves the count census); the footer Num 36:13 DAEMONS by law_midian's given_at")
        return out("the four count lines LEDGER by the counted statuses; the four receipts CLOSE; the rate a MEASURE (R7); the footer's block DAEMONS", ['accepted'])
    if ask == 'terumah_measure':
        dat('the row levites_rate_reading (the no_torah_measure arm): %s' % data['levites_rate_reading']['settings']['no_torah_measure'][:80]); move('Jerusalem Talmud Terumot 4:3:8', "R. Yonatan one in a hundred, R. Yannai one in a thousand, R. Mana no measure")
        return out("the Torah's own measure of terumah none (Jerusalem Talmud Terumot 4:3:8) — the rates the shelf's settings, the ink's fiftieth a one-time instruction", ['accepted'])
    return out('no verdict in span', [FX.NONE])


# ===== F7: THE OFFICERS' GOLD (Num 31:48-54) ==================================================================
def the_gold(case, data):
    del P[:]
    ask = case['ask']
    if ask == 'the_count':
        ink('31:48-49', '"the officers over the thousands of the army, the captains of thousands and the captains of hundreds, came near to Moses and said: your servants have lifted the head of the men of war under our hand, and not one man of us is missing" — %s; %s; Jethro\'s grades (Exodus 18:21, 25) the army\'s ranks' % (LIFTED_THE_HEAD, NONE_MISSING))
        move('cold_run_incense_shekel (CALL) — IS.shekel(plague_clause) = %s' % IS_PLAGUE['fx'], "the count taken with none missing — the shekel engine's clause: no plague at the counting")
        return out("the officers of thousands and of hundreds lifted the head of the men of war — not one man of us is missing (31:49): Jethro's grades the army's ranks; the count with none missing", ['no_plague_at_counting'])
    if ask == 'ransom_at_a_count':
        ink('31:49-50, 31:54', '"lift the head" %s / Exodus 30:12 %s; "to atone for our souls before the LORD" %s / "for your souls" %s; "a memorial ... before the LORD" %s / %s — EXODUS 30:12-16\'S OWN WORDS (computed)' % (LIFTED_THE_HEAD, WHEN_YOU_LIFT, ATONE_OUR_SOULS, ATONE_YOUR_SOULS, MEMORIAL, MEMORIAL_EXOD))
        move('cold_run_incense_shekel (CALL) — IS.shekel(lift_head) = %s, (atone_souls) = %s, (silver_of_atonements) = %s' % (IS_LIFT, IS_ATONE, IS_SILVER), "THE OFFICERS' GOLD RUNS THE RANSOM OF EXODUS 30 AT A COUNT — a REFERENCE by three shared phrases; the row trigger_parameter = %s" % data['trigger_parameter']['value'])
        return out("to atone for our souls before the LORD (31:50) — Exodus 30:12-16's own words (lift the head, atone for your souls, a memorial): the ransom of Exodus 30 run at a count; no plague at the counting", ['no_plague_at_counting', 'atoned_forgiven'])
    if ask == 'atonement_reading':
        dat('the row atonement_reading: %s (the eyes\' thoughts and the moral count recorded)' % data['atonement_reading']['value'])
        move('Shabbat 64a:22-64b:2; Yevamot 61a:4; Berakhot 24a:15', "'then why atonement?' — the thoughts of transgression; the eyes nourished from nakedness; R. Shimon: missing to transgression")
        return out("the ransom at a count (the ink) / the eyes' thoughts of transgression (Shabbat 64a:22-64b:2) — both arms; R. Shimon's moral count (Yevamot 61a:4)", ['atoned_forgiven'])
    if ask == 'ornaments':
        ink('31:50-51', '"every man what he found, vessels of gold: the armlet, the bracelet, the ring, the earring and the kumaz" — %s in the ink\'s order; "all vessels of workmanship" (31:51)' % ORNAMENTS)
        dat('the row ornaments_reading: %s' % data['ornaments_reading']['value']); move('Shabbat 64a:20-21, 60a:3, 63b:6, 63b:19', "agil the breast-mold, kumaz the womb-mold; the kumaz in Aramaic; vessels for impurity")
        return out("armlet, bracelet, ring, earring, kumaz (31:50) — agil the breast-mold, kumaz the womb-mold (Shabbat 64a:20-21); vessels for impurity (31:51 — Shabbat 60a:3, 63b:19)", ['accepted'])
    if ask == 'ornaments_impure':
        move('Shabbat 63b:6, 60a:3, 63b:19', "Rav Yosef: the bracelet impure — 31:50's ornaments beside 31:19's 'purify yourselves'; 'all vessels with which labor is done' (31:51) — a ring with a seal, a woven fabric of any size")
        return out("the bracelet impure — 31:50 beside 31:19 (Shabbat 63b:6); all vessels with which labor is done (31:51) the class's definition (60a:3, 63b:19)", ['accepted'])
    if ask == 'gold_weight':
        ink('31:52', '"all the gold of the heave-offering which they offered to the LORD was sixteen thousand seven hundred and fifty shekels, from the captains of thousands and from the captains of hundreds" — the parser\'s %d; %s one seat; the captains no number (census_probes G3); Onkelos\' selas' % (GOLD, GOLD_PHRASE))
        return out("sixteen thousand seven hundred and fifty shekels (31:52) — the parser's 16,750; the captains no number", ['memorial_before_the_lord'])
    if ask == 'memorial':
        ink('31:54', '"and Moses and Eleazar the priest took the gold from the captains of thousands and of hundreds and brought it into the tent of meeting, a memorial for the children of Israel before the LORD" — %s; Exodus 30:16\'s %s in another order; "the LORD\'s offering" (31:50) %s' % (MEMORIAL, MEMORIAL_EXOD, OFFERING_OF_THE_LORD))
        move('Temurah 13a:14', "'the LORD's offering', not 'an offering TO the LORD' — the tent, not the altar (the noun's form decides the destination)")
        return out("brought into the tent of meeting, a memorial for the children of Israel before the LORD (31:54) — Exodus 30:16's six words in another order; the LORD's offering, not an offering to the LORD: the tent, not the altar (Temurah 13a:14)", ['memorial_before_the_lord'])
    if ask == 'not_one_missing_reading':
        dat('the row atonement_reading (the moral_count arm): %s' % data['atonement_reading']['settings']['moral_count'][:70]); move('Yevamot 61a:4', "the Rabbis: the casualty count — no Jew fell, the corpses gentile; R. Shimon ben Yochai: missing to transgression")
        return out("the Rabbis: the casualty count — no Jew fell (the corpses gentile); R. Shimon ben Yochai: missing to transgression (Yevamot 61a:4)", ['accepted'])
    return out('no verdict in span', [FX.NONE])
