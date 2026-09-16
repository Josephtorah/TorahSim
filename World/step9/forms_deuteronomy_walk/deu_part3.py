
# ===== F0: THE COMMISSION (Num 27:12-23 — the callee) ======================================================
def the_commission(case, data):
    del P[:]
    ask = case['ask']
    if ask == 'the_mountain':
        ink('Num 27:12', '"go up to this mountain of Abarim and see the land" — "the mountain of Abarim" %s (27:12; 33:47-48; Deuteronomy 32:49 with Nebo named); "and see the land" %s; "Mount Nebo, the top of Pisgah" %s' % (ABARIM_MOUNTAIN, SEE_THE_LAND, NEBO_PISGAH))
        dat('the row the_commission: one mountain, three names — %s' % data['the_commission']['value']['mountain_names'])
        return out("the mountain of Abarim (27:12) — Nebo and Pisgah its other names (34:1 one mountain): Deuteronomy 3:27's Pisgah the retelling of this command, READ BACK", ['accepted'])
    if ask == 'the_sentence_cited':
        ink('Num 27:14', '"as you rebelled against My word in the wilderness of Zin … the waters of Meribah of Kadesh" — %s (27:14; Deuteronomy 32:51): an INTERNAL pointer to 20:12\'s sentence' % MERIBAH_KADESH)
        move('cold_run_chukat (CALL) — CK.meribah(sentence) = %s' % CK_SENTENCE[0][:70], "the barred_from_the_land entry on Moses OPEN since (40, 1, 1) — read, not rewritten; Aaron's closed at 20:28")
        return out("Meribah cited (27:14) — 20:12's sentence pointed to, the barred entry on Moses OPEN read (CK by CALL); no second write", ['accepted'])
    if ask == 'the_shepherd':
        ink('Num 27:15-17', '"let the LORD, the God of the spirits of all flesh, appoint a man over the congregation … that the congregation of the LORD be not as sheep which have no shepherd" — "the God of the spirits of all flesh" %s (16:22 Korach\'s day and here); "go out … come in" %s; "as sheep without a shepherd" %s' % (SPIRITS_ALL_FLESH, GO_OUT_COME_IN, SHEEP_NO_SHEPHERD))
        move('Sanhedrin 17a:10 (credited at THE TENT); Sifrei Bamidbar 138', "Eldad and Medad's prophecy — Moses will die and Joshua will bring Israel in; the successor asked before he is named")
        return out("a shepherd asked (27:15-17) — plea_made on Moses: the successor asked before he is named; 16:22's phrase at its second seat", ['plea_made'])
    if ask == 'the_hand_laid':
        ink('Num 27:18, 23', '"lay your HAND upon him" (27:18) — %s; "and he laid his HANDS upon him" (27:23) — %s: one commanded, two laid; "a man in whom is spirit" %s' % (HAND_SG, HANDS_PL, MAN_WITH_SPIRIT))
        move('Sifrei Bamidbar 141 (credited at THE TENT); Sanhedrin 13b-14a the ordination', "one hand commanded, two hands laid — with a generous eye; the ordination's form for the generations")
        dat('the row the_commission: hands %s' % (data['the_commission']['value']['hands'],))
        return out("the hand laid (27:18, 23) — one hand commanded, two laid (the Sifrei 141): invested_office on Joshua, the ordination's form", ['invested_office'])
    if ask == 'the_honor':
        ink('Num 27:20', '"and you shall put of your honor upon him" — %s one seat' % OF_YOUR_HONOR)
        move('Bava Batra 75a:8', "of your honor and not all your honor — the elders of that generation said: Moses' face as the sun, Joshua's as the moon")
        dat('the row the_commission: the_honor')
        return out("of your honor (27:20) — not all of it: the sun and the moon (Bava Batra 75a:8) — DATA", ['accepted'])
    if ask == 'the_urim':
        ink('Num 27:21', '"he shall stand before Eleazar the priest, who shall inquire for him by the judgment of the Urim" — %s one seat; "at his word they shall go out and come in" %s; "before Eleazar the priest" %s' % (JUDGMENT_URIM, AT_HIS_WORD, BEFORE_ELEAZAR))
        move('cold_run_second_census (CALL) — C2.DATA[urim_judgment] = %s' % C2.DATA['urim_judgment']['value'], "a prophet's decree may be retracted, the Urim's not (Yoma 73b:3); the lot's mouth is the Urim's (Bava Batra 122a:3)")
        return out("the judgment of the Urim (27:21) — final (C2 by CALL: Yoma 73b:3); Joshua under Eleazar's inquiry, not Moses' face to face", ['accepted'])
    if ask == 'the_receipt':
        ink('Num 27:22-23', '"and Moses did as the LORD commanded him" — %s one seat; "as the LORD spoke by the hand of Moses" — "by the hand of Moses" %d Bible seats: THE RECEIPT, the spec/run pair\'s form (CB8\'s)' % (DID_AS_COMMANDED, len(BY_HAND_MOSES)))
        dat('the commission\'s debit on Moses CLOSED by its run (closed_by "Num 27:22-23") — the register seat Num 27:22 CLOSE')
        return out("the receipt (27:22-23) — 'as the LORD commanded him': the commission's debit closed by its run, the register seat Num 27:22 CLOSE", ['accepted'])
    if ask == 'the_debit':
        ink('Num 27:12-13', '"see the land … and when you have seen it, you also shall be gathered" — "as Aaron your brother was gathered" %s' % GATHERED_AS_AARON)
        dat('commanded on moses valued see_the_land_from_abarim — OPEN BY DESIGN to Deuteronomy 34:1-4 (this book\'s own end); 3:27 its retelling READ BACK, no second write')
        return out("the debit (27:12) — see the land from Abarim: commanded on Moses, OPEN to Deuteronomy 34:1-4; 3:27 reads it back with Pisgah", ['commanded'])
    return out('no verdict in span', [FX.NONE])


# ===== F1: THE FRAME (Deut 1:1-5) ===========================================================================
def the_frame(case, data):
    del P[:]
    ask = case['ask']
    if ask == 'the_words':
        ink('1:1', '"these are the words which Moses spoke to all Israel beyond the Jordan …" — "these are the words" %s; the verse %d tokens, the eleven names of places' % (THESE_WORDS, len(words(1, 1))))
        move('Sifrei Devarim 1; Onkelos 1:1', "the places as the rebuke's sins — Onkelos writes them INTO the verse (thirty-three tokens for twenty-two)")
        move('Berakhot 32a:7; Sanhedrin 102a:14', "'and Di-zahab' — the school of R. Yannai: no such place; the gold lavished until they said 'enough' made the calf")
        dat('the row the_frame: %s' % data['the_frame']['value']['places'])
        return out("the words (1:1) — the eleven places the rebuke's sins (the Sifrei 1; Onkelos writes them in); Di-zahab the calf's gold (Berakhot 32a:7): the frame's DATA", ['accepted'])
    if ask == 'the_date':
        ink('1:3', '"in the fortieth year, in the eleventh month, on the first of the month" — the NUMBER reader %s; "in the fortieth year" %s ONE seat (33:38 says "of the going out"); "in the eleventh month" %s' % (SPEECH_DATE, FORTIETH_YEAR, ELEVENTH_MONTH))
        move('cold_run_journeys (CALL) — JO.aarons_death_retold(verbal_analogy) = %s' % JO_ANALOGY[0][:90], "Rosh Hashanah 2b:11 — 'the fortieth year' / 'the fortieth year': the bare date the exodus's; THE TRANSFER TAUGHT; the era's new year Nisan (JO the_era_new_year)")
        dat('the row the_date: %s — one clock, two readers; the marker at the tape position Deut 1:1' % data['the_date']['value'])
        return out("the date (1:3) — [40, 11, 1] by the number reader; the era the exodus's by the taught verbal analogy with 33:38 (Rosh Hashanah 2b:11; JO by CALL): the FORWARD marker at Deut 1:1", ['accepted'])
    if ask == 'the_receipt_of_the_rules':
        ink('1:3', '"Moses spoke to the children of Israel according to all that the LORD had commanded him to them" — "according to all that the LORD commanded him" %s (Exodus 40:16 the erection\'s receipt and this); the second form %s' % (ACCORDING_ALL_HIM, ACCORDING_ALL))
        move('Sifrei Devarim 2:8', "'according to all that the LORD commanded him' — the hermeneutic rules themselves: the receipt of the whole book's rules")
        dat('the register seat Deut 1:3 declared ACT — the speech line\'s write (torah_expounded) carries its source; the run of every relayed command, closing nothing by itself')
        return out("the receipt of the rules (1:3) — 'according to all' the hermeneutic rules (the Sifrei 2:8): the register seat ACT, the frame the readback checkpoint reads", ['accepted'])
    if ask == 'the_eleven_days':
        ink('1:2', '"eleven days from Horeb by the way of Mount Seir to Kadesh-barnea" — %s; the parser [%d]' % (ELEVEN_HOREB, ELEVEN_DAYS))
        move('Sifrei Devarim 2:1-3', "eleven days' journey done in three — the Presence hastened them; the rebuke's measure")
        return out("eleven days (1:2) — [11] by the parser; the journey hastened (the Sifrei 2:1-3): the rebuke's measure", ['accepted'])
    if ask == 'after_sihon':
        ink('1:4', '"after he had smitten Sihon king of the Amorites … and Og king of Bashan" — %s one seat; "Og king of Bashan" %d Bible seats' % (AFTER_SIHON, len(OG_BASHAN)))
        move('cold_run_journeys (CALL) — JO.aarons_death_retold(the_order) = %s' % JO_ORDER[0][:80], "Rosh Hashanah 2b:13, 3a:12 — Aaron's death before the speech by 'after he had smitten Sihon'; the fortieth year's order on the tape")
        return out("after Sihon (1:4) — the order of the fortieth year: Aaron's death, Arad, the departure, Sihon, the speech (JO by CALL; Rosh Hashanah 2b:13)", ['accepted'])
    if ask == 'began_to_expound':
        ink('1:5', '"beyond the Jordan, in the land of Moab, Moses undertook to expound this Torah" — %s one seat; the expound-root\'s Torah seats %s' % (EXPOUND, EXPOUND_LEMMA))
        move('Sotah 35b:6; Zevachim 115b:17; Mishnah Sotah 7:8', "'expound' with 27:8's 'clearly' — the seventy languages; R. Akiva: the third teaching in the plains of Moab; the king reads from 'these are the words'")
        return out("began to expound (1:5) — the expound-root's two Torah seats (27:8's 'clearly' the other); the third teaching (Zevachim 115b:17); the king's reading (Sotah 7:8)", ['accepted'])
    if ask == 'the_write':
        ink('1:1-5', 'the frame — the book\'s one act of its own day')
        dat('torah_expounded on israel_people — a STATUS dated (40, 11, 1) by the forward marker; everything after it in chapters 1-3 read back or supplied at its own time (R6)')
        return out("the write (1:1-5) — torah_expounded on Israel at (40, 11, 1): the book's one act of its own day", ['torah_expounded'])
    return out('no verdict in span', [FX.NONE])


# ===== F2: THE OFFICERS AND THE JUDGES (Deut 1:6-18) ========================================================
def the_officers_and_the_judges(case, data):
    del P[:]
    ask = case['ask']
    if ask == 'the_horeb_command':
        ink('1:6-8', '"you have dwelt long enough in this mountain; turn and take your journey … go in and possess" — "enough for you" %s (the plural\'s eight seats: Horeb, Seir, the tribes, Korach\'s two); "turn and journey" %s (14:25\'s pair); "go in and possess" %s' % (ENOUGH_PL, TURN_JOURNEY, GO_POSSESS))
        move('cold_run_erection (CALL) — ER.presence(horev_plene) = %s; cold_run_beha (CALL) — BH.march(date) = %s' % (ER_HOREB['v'], BH_DATE[0][:40]), "Exodus 33:1's 'depart, go up hence' the command's kin; 10:11's (2, 2, 20) the departure's day — the retrograde marker at 1:6")
        dat('the row the_horeb_command: %s — the supplied debit journey_to_the_mountain_of_the_amorite CLOSED at once by the prior run Num 12:16' % data['the_horeb_command']['value']['closed_by'])
        return out("the Horeb command (1:6-8) — told only here: commanded on Israel dated (2, 2, 20), CLOSED by the prior run Num 12:16 (the arrival in Paran); 'go in and possess' a reference to the land granted (Genesis 15:18)", ['commanded'])
    if ask == 'the_regions':
        ink('1:7', '"the hill country of the Amorites … the Arabah, the hill country, the lowland, the Negev, the seashore, the land of the Canaanites and Lebanon, as far as the great river, the river Euphrates"')
        move('Bava Kamma 81b:6; Shevuot 47b:6; cold_run_borders (CALL) — BO.DATA[the_promised_extents] = %s' % BO.DATA['the_promised_extents']['value'], "every tribe's portion held some of each kind (Joshua's ten conditions); the Euphrates called great because near the land; the four promised extents observed")
        dat('the row the_horeb_command: regions %s' % data['the_horeb_command']['value']['regions'])
        return out("the regions (1:7) — the seven kinds every tribe's portion held (Bava Kamma 81b:6); the Euphrates great by nearness (Shevuot 47b:6); the promised extents by CALL: DATA", ['accepted'])
    if ask == 'the_burden':
        ink('1:9-12', '"I am not able to bear you myself alone … how can I myself alone bear your cumbrance and your burden and your strife" — "your burden" %s one seat; 11:14\'s "I alone" the same word' % YOUR_BURDEN)
        move('cold_run_beha (CALL) — BH.seventy_elders(sanhedrin) = %s' % BH_SANH[0], "11:14's burden and 11:16's seventy — the seventy-one with Moses over them (Sanhedrin 2a:13; 16b:18); 'they shall bear the burden of the people WITH you' (11:17) — like you (17a:3)")
        return out("the burden (1:9-12) — 11:14's 'I alone' retold; the seventy with Moses the seventy-one (BH by CALL; Sanhedrin 16b:18, 17a:3)", ['accepted'])
    if ask == 'the_blessing':
        ink('1:11', '"may the LORD, the God of your fathers, add to you a thousand times" — %s one seat; the parser [%d]' % (THOUSAND_TIMES, THOUSAND_FOLD))
        move('Sifrei Devarim 11:1; Rosh Hashanah 28b:10', "Moses' own blessing beside God's (which has no bound); a priest may not add this blessing of his own to the priestly blessing")
        dat('the row the_officers_table: the_blessing')
        return out("the blessing (1:11) — [1000]: Moses' own beside God's (the Sifrei 11:1); a priest may not add it (Rosh Hashanah 28b:10): DATA", ['accepted'])
    if ask == 'the_qualities':
        ink('1:13, 15', '"wise and discerning and known" %s ONE seat; "wise and known" %s ONE seat — the discerning not found' % (WISE_DISC_KNOWN, WISE_KNOWN))
        move('Sifrei Devarim 15:2; Eruvin 100b:18; Nedarim 20b:10; Sanhedrin 17a:21-22', "seven sought, three found; the generation's sons; the Great Sanhedrin's men of stature and seventy languages; the creeping thing rendered pure")
        dat('the row the_seven_qualities: asked %d, found %d' % (data['the_seven_qualities']['value']['asked'], data['the_seven_qualities']['value']['found']))
        return out("the qualities (1:13, 15) — seven asked, three found (the Sifrei 15:2): the discerning not found (Eruvin 100b:18); Jethro's four by CALL: a DATA checklist", ['accepted'])
    if ask == 'the_grains':
        ink('1:15', '"captains of thousands, captains of hundreds, captains of fifties and captains of tens, and officers for your tribes" — the parser %s with "thousands" a NOUN; "captains of thousands" %s (Exodus 18:21, 25 and the kings\' seats); "and officers for your tribes" %s' % (GRAINS, CAPT_THOUSANDS, OFFICERS_TRIBES))
        move('cold_run_exodus_story (CALL) — ES.jethro(denominations) = %s' % ES_DENOM['v'], "the four grains of 18:21 — the appointment a REFERENCE to judges_appointed (Exodus 18:25), TURNED")
        dat('the row the_officers_table: grains %s' % data['the_officers_table']['value']['grains'])
        return out("the grains (1:15) — [100, 50, 10] with the plural 'thousands' a noun: the four grains of Exodus 18:21 by CALL; the appointment read back, TURNED", ['accepted'])
    if ask == 'the_count':
        move('cold_run_exodus_story (CALL) — ES.jethro(judges) = %d; cold_run_bamidbar (CALL) — CB.census(total) = %s' % (ES_JUDGES['v'], CB_TOTAL[0]), "78,600 on the round six hundred thousand (Sanhedrin 18a:3); 79,064 on the exact 603,550 by integer division at every grain (the Sifrei 15:4's rounding rule)")
        move('cold_run_balak (CALL) — BK.peor(judges_count) = %s' % BK_JUDGES[0][:60], "the Jerusalem Talmud Sanhedrin 10:2's arithmetic — each executing two = 157,200")
        dat('the row the_officers_table: round %d, exact %d' % (data['the_officers_table']['value']['count_round'], data['the_officers_table']['value']['count_exact']))
        return out("the count — 78,600 on the round six hundred thousand (ES by CALL; Sanhedrin 18a), 79,064 on the census's exact 603,550 by integer division (CB by CALL; the Sifrei 15:4's rounding rule): two settings", ['accepted'])
    if ask == 'the_officers':
        ink('1:15', '"and officers for your tribes" — %s one seat; "and officers" %s — Deuteronomy 16:18 the second seat' % (OFFICERS_TRIBES, AND_OFFICERS))
        move('Sifrei Devarim 15:5; Sanhedrin 16b:9-10; 2 Chronicles 19:11', "the officers with the strap — the Levites; 'judges and officers in all your gates for your tribes' (16:18): judges for Israel, for every tribe, for every city — THE OFFICERS' TABLE's other seat")
        return out("the officers (1:15) — the strap (the Sifrei 15:5; 2 Chronicles 19:11); Deuteronomy 16:18's second seat — every tribe, every city (Sanhedrin 16b:9-10)", ['accepted'])
    if ask == 'the_charge':
        ink('1:16-17', 'the six clauses — "hear between your brothers" %s, "judge righteously" %s, "no faces in judgment" %s, "the small as the great" %s, "not afraid of any man" %s, "the judgment is God\'s" %s, "the hard matter" %s: each ONE seat' % (HEAR_BROTHERS, JUDGE_RIGHT, NO_FACES, SMALL_GREAT, NOT_AFRAID, JUDGMENT_GODS, HARD_MATTER))
        dat('judges_charged on the-court — the six clauses %s, dated (1, 2, 16) by the court\'s founding day read off Israel\'s ledger (the retrograde marker at 1:9); THE LAW of the span in Moses\' voice with no divine frame' % data['the_judges_charge']['value'])
        return out("the charge (1:16-17) — the six clauses each one seat: judges_charged on the court, dated at the court's founding (1, 2, 16); the law in Moses' voice, the vows' class", ['judges_charged'])
    if ask == 'hear':
        ink('1:16', '"and I charged your judges at that time, saying: hear between your brothers" — "hear" the infinitive absolute')
        move('Sanhedrin 7b:14 (R. Chanina)', "a judge may not hear one litigant before the other comes; 'charged' — with alacrity, the rod and the strap (7b:14-15)")
        return out("hear (1:16) — not one litigant without the other (Sanhedrin 7b:14); 'charged' with alacrity, the rod and the strap", ['accepted'])
    if ask == 'judge_righteously':
        ink('1:16', '"and judge righteously between a man and his brother and his stranger" — %s one seat' % JUDGE_RIGHT)
        move('Sanhedrin 7a:17 (R. Yonatan); Leviticus 19:15 by CALL — HO.conduct(judge_is_measurer) = %s' % HO_MEASURER['v'], "the true judgment truly makes the Presence rest in Israel; 'in righteousness you shall judge' the holiness engine's clause")
        return out("judge righteously (1:16) — the true judgment truly makes the Presence rest (Sanhedrin 7a:17); Leviticus 19:15's 'in righteousness' by CALL", ['accepted'])
    if ask == 'no_faces':
        ink('1:17', '"you shall not respect persons in judgment" — %s one seat; "respect persons" (takiru) %s' % (NO_FACES, RESPECT_FACES))
        move('Sanhedrin 7b:18 (R. Yehuda / R. Elazar); Sifrei Devarim 17:1', "do not befriend the litigant / do not estrange him — a DISPUTE row; the appointer addressed")
        move('Mishnah Sanhedrin 3:4-5; Sanhedrin 27b:10-29a:12; Numbers 35:23 by CALL — RF.DATA[the_court_of_twenty_three]', "the kin and the haters off the bench — 'not his enemy nor seeking his harm': the witness disputed, the JUDGE agreed (29a:11)")
        return out("no faces (1:17) — befriend / estrange disputed (Sanhedrin 7b:18); the kin and the haters off the bench (Mishnah Sanhedrin 3:4-5; 29a:11): the DATA row no_faces", ['accepted'])
    if ask == 'small_and_great':
        ink('1:17', '"you shall hear the small and the great alike" — %s one seat' % SMALL_GREAT)
        move('Sanhedrin 8a:2 (Reish Lakish); 8a:4-5', "the judgment of one peruta as dear as of a hundred maneh; the case that came first heard first")
        return out("the small and the great (1:17) — the peruta as the hundred maneh (Sanhedrin 8a:2); the order of hearing (8a:4-5)", ['accepted'])
    if ask == 'no_fear':
        ink('1:17', '"you shall not be afraid of the face of any man" — %s one seat; "afraid" (taguru) the gather-root' % NOT_AFRAID)
        move('Sanhedrin 7a:16; 6b:12 (Reish Lakish); 6b:13 (R. Yehoshua ben Korcha); Sifrei Devarim 17:4', "a term for gathering in — a judge may not hold back his words; refusal before hearing, not after; the student who sees merit for the poor not silent")
        return out("no fear (1:17) — a term for gathering in (Sanhedrin 7a:16); the refusal before hearing only (6b:12; the Sifrei 17:4); the student not silent (6b:13)", ['accepted'])
    if ask == 'the_judgment_is_gods':
        ink('1:17', '"for the judgment is God\'s" — %s one seat' % JUDGMENT_GODS)
        move('Sanhedrin 6b:3; 7a:18; 6b:14; the Rambam\'s introduction 15:58', "let the judgment pierce the mountain (Moses) against Aaron the pursuer of peace; the judge who takes from one and gives to the other — the Holy One takes his life; the judges know before Whom")
        return out("the judgment is God's (1:17) — pierce the mountain (Sanhedrin 6b:3); the unlawful judge's life (7a:18); before Whom (6b:14)", ['accepted'])
    if ask == 'the_hard_matter':
        ink('1:17', '"and the cause that is too hard for you, you shall bring to me and I will hear it" — %s, %s one seat each' % (HARD_MATTER, BRING_TO_ME))
        move('cold_run_exodus_story (CALL) — ES.jethro(hard_cases) = %s; cold_run_zelophehad (CALL) — ZL.the_daughters(halt) = %s' % (ES_HARD['v'], ZL_HALT[0][:60]), "Exodus 18:26's hard_cases_to_moses the standing status; the Sifrei 17:7 — Zelophehad's daughters, THE TENT: the third form, carried in by Moses")
        return out("the hard matter (1:17) — Exodus 18:26's status read (ES by CALL); Zelophehad's daughters the case (the Sifrei 17:7; ZL by CALL — the third form)", ['accepted'])
    if ask == 'the_stranger':
        ink('1:16', '"between a man and his brother and his stranger" — "his stranger" the convert')
        move('Yevamot 47a:7 (R. Yehuda)', "a convert converts only before a court — 'and his stranger' with 'judge righteously'; his opponent's plea heard")
        return out("the stranger (1:16) — a convert before a court (Yevamot 47a:7)", ['accepted'])
    if ask == 'a_man_excludes_the_minor':
        ink('1:16', '"between a MAN and his brother"')
        move('Sifrei Devarim 16:6', "'a man' — the minor excluded from the litigants")
        return out("a man excludes the minor (1:16 — the Sifrei 16:6)", ['accepted'])
    if ask == 'the_gentile_litigant':
        ink('1:16', '"and his stranger" — the gentile litigant on the shelf')
        dat('the row the_gentile_litigant: %s — R. Ishmael\'s two rulings against Rabban Shimon ben Gamliel (the Sifrei 16:4)' % data['the_gentile_litigant']['value'])
        return out("the gentile litigant — R. Ishmael's two rulings against Rabban Shimon ben Gamliel's one (the Sifrei 16:4): DATA", ['accepted'])
    if ask == 'the_appointer':
        ink('1:17', '"you shall not respect persons" — addressed to the one who appoints judges')
        move('Sifrei Devarim 17:1', "'you shall not respect persons in judgment' — to the appointer: appoint no judge for his face; Sanhedrin 7b:16-17 the judge appointed for money")
        return out("the appointer (1:17) — the clause addressed to the one who appoints (the Sifrei 17:1): DATA", ['accepted'])
    if ask == 'the_compromise':
        ink('1:17', '"for the judgment is God\'s" — the compromise\'s clause on the shelf')
        dat('the row the_compromise: %s — R. Yehoshua ben Korcha a mitzva, R. Eliezer son of R. Yosei HaGelili forbidden once heard, R. Shimon ben Menasya before the verdict leans; "justice, justice" one for judgment, one for compromise (Sanhedrin 6b:1-15; 32b:4-6)' % data['the_compromise']['value'])
        return out("the compromise — three settings on 1:17's clause (Sanhedrin 6b:1-15; 32b:4-6): TWO VERDICT TABLES as DATA", ['accepted'])
    if ask == 'the_al_tikrei':
        ink('1:13', '"and I will set them as your heads" (ואשימם)')
        move('Sifrei Devarim 13:6', "'I will set them' read 'their guilt' (ashmam) on your heads — THE REVOCALIZATION (MOVE_CATALOG's move): the appointer bears the judges' guilt")
        return out("the al tikrei (1:13) — 'I will set them' read 'their guilt on your heads' (the Sifrei 13:6): the revocalization move", ['accepted'])
    if ask == 'be_deliberate':
        move('Pirkei Avot 1:1; Sifrei Devarim 16:1; cold_run_erection (CALL) — ER.presence(sheet_avot_1_1) = %s' % ER_AVOT['v'], "'be deliberate in judgment' — the Sifrei cites the Mishnah as the verse's reading; the chain from Moses to Joshua the erection engine's row")
        return out("be deliberate (Avot 1:1) — the Sifrei 16:1 cites the Mishnah as 1:16's reading; the chain by CALL", ['accepted'])
    if ask == 'money_and_capital':
        move('Mishnah Sanhedrin 4:1; Sanhedrin 32a:1-10; cold_run_ordinances (CALL) — OR.courts(one_vs_two) = %s, (asymmetry) = %s, (twenty_three) = %d' % (OR_ONE_TWO['v'], OR_ASYM['v'], OR_23['v']), "'one manner of law' (Leviticus 24:22); the ten differences — three against twenty-three, one against two, reversal, who may argue, day and night, the same day or the morrow, from the side (1:17's 'the small and the great' the eighth's ground), the fit of lineage; the Sifrei 18:1")
        return out("money and capital (Mishnah Sanhedrin 4:1) — the ten differences (Sanhedrin 32a; the Sifrei 18:1); the majority's asymmetry by CALL", ['accepted'])
    if ask == 'the_court_of_three':
        move('Mishnah Sanhedrin 1:1-3, 3:1-3; Sanhedrin 2a-2b, 23a-26b; cold_run_exodus_story (CALL) — ES.jethro(sanhedrin_sizes) = %s' % (ES_SIZES['v'],), "money cases by three; the litigants' choice — this one chooses one, that one chooses one, the two choose a third (R. Zeira: so the judgment goes out true); the disqualified by conduct — the dice-player, the lender at interest, the pigeon-flyer, the Sabbatical merchant; the proclamation")
        return out("the court of three (Mishnah Sanhedrin 1:1, 3:1-3) — the litigants' choice, the third by the two (Sanhedrin 23a:12); the disqualified by conduct (24b-26b); the sizes by CALL", ['accepted'])
    if ask == 'the_perverting_judge':
        move('cold_run_holiness (CALL) — HO.conduct(five_effects) = %s' % HO_FIVE['v'], "Leviticus 19:15's 'do no wrong in judgment' — the judge who perverts defiles the land, profanes the Name, removes the Presence, fells by the sword, exiles (the Sifra); Sanhedrin 7a:17-18 the Presence removed, the life taken")
        return out("the perverting judge — the five effects (HO by CALL; Sanhedrin 7a:17-18): judgment_perverted", ['judgment_perverted'])
    if ask == 'the_refusal_before_hearing':
        move('Sanhedrin 6b:12 (Reish Lakish); 6b:11 (R. Shimon ben Menasya)', "before hearing the litigants' statements, or after hearing but before knowing where the judgment leans, a judge may refuse to judge — 'you shall not be afraid' (1:17) binds him only after")
        return out("the refusal before hearing — permitted, not yet bound by 'you shall not be afraid' (Sanhedrin 6b:12): exempt", ['exempt'])
    if ask == 'all_the_things':
        ink('1:18', '"and I commanded you at that time all the things that you should do"')
        move('Sanhedrin 8a:6 (credited at Beha\'alotcha)', "'I charged your judges' (1:16) and 'I commanded you' (1:18) — the judges warned to bear the community, the community warned to bear the judges' burden")
        return out("all the things (1:18) — the community warned as the judges were (Sanhedrin 8a:6)", ['accepted'])
    return out('no verdict in span', [FX.NONE])


# ===== F3: THE SPIES READ BACK (Deut 1:19-46) ===============================================================
def the_spies_read_back(case, data):
    del P[:]
    ask = case['ask']
    if ask == 'the_asking':
        ink('1:22', '"you came near to me, all of you, and said: let us send men before us, that they may search the land for us" — %s, %s one seat each' % (LET_US_SEND, SEARCH_FOR_US))
        move('cold_run_shelach (CALL) — SL.spies(send_for_yourself) = %s' % SL_SEND[0][:70], "Sotah 34b:3 — 'send for yourself' at Moses' discretion; the people asked; 34b:4 'that they may search' with the moon's embarrassment")
        dat('the row the_spies_asked: %s' % data['the_spies_asked']['value'])
        return out("the asking (1:22) — the people's, against 13:2's 'send for yourself' (Sotah 34b:3; SL by CALL): the two tellings reconciled on the shelf — the readback row TURNED", ['accepted'])
    if ask == 'the_twelve':
        ink('1:23', '"I took twelve men of you, one man for a tribe" — the parser %s; "twelve men" %s; "one man for a tribe" %s' % (TWELVE_ONE, TWELVE_MEN, ONE_PER_TRIBE))
        move('cold_run_shelach (CALL) — SL.spies(one_per_tribe)', "13:2's one man per tribe, princes; Levi absent; Joshua's crossing the phrases' other seats")
        return out("the twelve (1:23) — [12, 1]: one per tribe by CALL; Joshua 4:2 and 3:12 the phrases' other seats", ['accepted'])
    if ask == 'the_valley':
        ink('1:24', '"they came to the valley of Eshcol and spied it out" — %s (13:23 and this); "spied" the spy-root\'s piel %s — Caleb\'s verb, not 13:2\'s tour' % (ESHCOL, SPY_ROOT))
        move('cold_run_shelach (CALL) — SL.spies(eshcol) = %s; cold_run_chukat (CALL) — CK.DATA[spy_verb] = %s' % (SL_ESHCOL[0], CK.DATA['spy_verb']['value']), "named after the cluster (13:24); the spy-verb Caleb's (Joshua 14:7) at Jazer (21:32)")
        return out("the valley (1:24) — Eshcol named after the cluster (SL by CALL); 'spied' the piel — Caleb's verb (Joshua 14:7; CK.DATA spy_verb by CALL)", ['accepted'])
    if ask == 'good_is_the_land':
        ink('1:25', '"they brought us word and said: good is the land which the LORD our God gives us" — %s: this and Numbers 14:7 — JOSHUA AND CALEB\'S words' % GOOD_LAND_IS)
        move('Sifrei Devarim 23:3; Sotah 35a:2', "the spies' own words 'good is the land' — 14:7's in their mouths; 13:27's 'however' dropped: the lie with a grain of truth")
        return out("good is the land (1:25) — 14:7's words, Joshua and Caleb's (the Sifrei 23:3); the retelling keeps the truth, drops 13:27's 'however' (Sotah 35a:2): SHORTENED", ['accepted'])
    if ask == 'the_murmuring':
        ink('1:27-28', '"you murmured in your tents … the LORD hates us … our brothers have melted our heart, saying: a people greater and taller than we, cities great and fortified to heaven, the sons of the Anakim" — %s, %s, %s, %s one seat each; "the sons of the Anakim" %s' % (MURMURED_TENTS, HATES_US, MELTED_HEART, GREATER_TALLER, SONS_ANAKIM))
        move('Shevuot 47b:5 (credited); cold_run_shelach (CALL) — SL.spies(stronger_than) = %s' % SL_STRONGER[0][:60], "'you murmured' as two words — you explored and disparaged; 13:31's 'stronger than us' read 'than Him' — the retelling keeps the plain sense; the Sifrei 25:4's hyperbole 'to heaven'")
        return out("the murmuring (1:27-28) — two words (Shevuot 47b:5); the spies' words in the people's mouths, 'greater and taller than we' the plain sense of 13:31 (Sotah 35a:7): TURNED", ['accepted'])
    if ask == 'the_carrying':
        ink('1:31', '"the LORD your God carried you, as a man carries his son" — %s one seat' % CARRIES_SON)
        move('Sifrei Devarim 314:2 (by position, forward); Exodus 19:4', "'as on eagles' wings' — the eagle's carrying; the son carried")
        return out("the carrying (1:31) — as a man carries his son: Exodus 19:4's eagle the kin", ['accepted'])
    if ask == 'the_pillar':
        ink('1:33', '"who goes before you in the way … in fire by night and in the cloud by day" — %s, %s one seat each' % (FIRE_NIGHT, CLOUD_DAY))
        move('Exodus 13:21 by REFERENCE (the exodus story\'s pillar_set line, no cell)', "the pillar of cloud by day and of fire by night — the tape's line at Exodus 13:21-22; the pesach runner's by_day ask the token's seat")
        return out("the pillar (1:33) — Exodus 13:21's by REFERENCE: the tape's pillar_set line, read", ['accepted'])
    if ask == 'the_oath':
        ink('1:34-36', '"the LORD heard the voice of your words and was angry and SWORE: not one of these men, this evil generation, shall see the good land … save Caleb son of Jephunneh, he shall see it … because he wholly followed the LORD" — %s, %s, %s; "he wholly followed the LORD" %s (Joshua 14:14 the payment\'s seat)' % (EVIL_GENERATION, SAVE_CALEB, THE_GOOD_LAND[:3], WHOLLY_FOLLOWED))
        move('cold_run_gad_reuben (CALL) — GR.DATA[the_oath_supplied] = %s; cold_run_shelach (CALL) — SL.decree(exceptions) = %s; SL.decree(caleb_entitlement) = %s' % (GR.DATA['the_oath_supplied']['value'], SL_EXC[0], SL_CALEB[0][:40]), "the oath's verb supplied by the retelling (32:10 the first); Caleb's holding_owed OPEN — paid at Joshua 14:13-14 outside the Torah")
        return out("the oath (1:34-36) — the verb 'swore' supplied (GR.DATA by CALL); sentence_pronounced read; Caleb's holding_owed OPEN read (SL by CALL): SHORTENED", ['accepted'])
    if ask == 'the_exceptions':
        move('cold_run_shelach (CALL) — SL.decree(exceptions) = %s' % SL_EXC[0], "Caleb and Joshua (14:24, 14:30) and the children brought in (14:31) — exempt from the oath; 1:36, 1:38, 1:39 retell the three")
        return out("the exceptions — Caleb, Joshua, the children (SL by CALL): exempt from the oath", ['exempt'])
    if ask == 'the_bars_ground':
        ink('1:37', '"the LORD was angry with me for your sakes, saying: you also shall not go in there" — %s, %s one seat each' % (ANGRY_FOR_YOU, NOT_GO_IN))
        move('cold_run_chukat (CALL) — CK.meribah(sentence) = %s' % CK_SENTENCE[0][:60], "20:12's 'because you did not believe in Me' — the tape's one entry; Psalm 106:32's 'for their sakes' outside the Torah, read, not run")
        dat('the row the_bars_ground: %s — no teacher joins the two grounds: an OPEN row (R4)' % data['the_bars_ground']['value'])
        return out("the bar's ground (1:37) — 'for your sakes' against 20:12's 'because you did not believe': DISAGREES, an OPEN row; the tape's one entry stands", ['accepted'])
    if ask == 'joshua_shall_go_in':
        ink('1:38', '"Joshua son of Nun who stands before you, he shall go in there; strengthen him, for he shall cause Israel to inherit it" — %s, %s one seat each: the effect\'s FIRST seat (3:28 the second)' % (HE_SHALL_GO, CAUSE_ISRAEL_INHERIT))
        move('cold_run_gad_reuben (CALL) — GR.the_rebuke(joshua_nothing_owed)', "Joshua excepted (14:30) and nothing owed him in the ink — Sotah 35a:4; Timnath-serah by the LORD's word")
        return out("Joshua shall go in (1:38) — 14:30's exception EXPANDED with the inheriting (the effect's first seat; 3:28 and Joshua 1:6 after)", ['accepted'])
    if ask == 'the_little_ones':
        ink('1:39', '"your little ones who you said would be a prey" — %s: 14:31 VERBATIM (the shared prefix %d tokens computed); "good and evil" %s — Eden\'s four seats and this' % (LITTLE_ONES_PREY, VERBATIM_PREFIX, GOOD_EVIL))
        move('Sifrei Devarim 25 (by position); Genesis 2:9, 17; 3:5, 22', "the children who know not good and evil — Eden's phrase; the exception's ground")
        return out("the little ones (1:39) — 14:31 VERBATIM for five tokens, then the children who know not good and evil added (Eden's four seats)", ['accepted'])
    if ask == 'the_turn_back':
        ink('1:40', '"and you, turn and take your journey into the wilderness by the way of the Red Sea" — "the way of the Red Sea" %s: the command (14:25), its run (21:4), both retold (1:40, 2:1)' % RED_SEA_WAY)
        move('cold_run_shelach (CALL) — SL.decree(turn_back) = %s' % SL_TURN[0][:70], "14:25's debit CLOSED at 21:4 (CF8) — read at the checkpoint, not rewritten")
        return out("the turn back (1:40) — 14:25 retold with 'tomorrow' dropped; the debit's close at 21:4 read (SL by CALL): TURNED", ['accepted'])
    if ask == 'the_presumption':
        ink('1:41-44', '"we have sinned … we will go up and fight, according to all that the LORD our God commanded us … you were presumptuous and went up … the Amorite chased you as bees do and beat you down in Seir to Hormah" — %s, %s, %s, %s, %s' % (WE_HAVE_SINNED[:2], GO_UP_FIGHT, PRESUMPTUOUS, AS_BEES, TO_HORMAH))
        move('cold_run_shelach (CALL) — SL.decree(presumption) = %s; SL.decree(hormah) = %s' % (SL_PRESUME[0][:50], SL_HORMAH[0][:50]), "presumed — the ark and Moses stayed; Hormah the proleptic name")
        dat('the receipt "as the LORD commanded us" in the PEOPLE\'S mouth refused by 1:42-43 — a RUN CITATION (R5): the register seat Deut 1:41 NONE')
        return out("the presumption (1:41-44) — presumed_to_go_up and defeated read back; 'as bees do', 'in Seir' EXPANDED; the receipt in the people's mouth a run citation (1:41 NONE)", ['accepted'])
    if ask == 'the_weeping':
        ink('1:45', '"you returned and wept before the LORD; the LORD did not hear your voice nor give ear" — %s, %s one seat each; 3:26\'s "did not hear me" the same phrase' % (WEPT_BEFORE, NOT_HEAR_VOICE))
        move('cold_run_shelach (CALL) — SL.decree(that_night) = %s' % SL_NIGHT[0][:60], "14:1's weeping the night of the Ninth of Av — a weeping for generations; the second weeping told only here, unheard")
        return out("the weeping (1:45) — a second weeping told only here, unheard (1:45 and 3:26 one phrase); 14:1's wept read: EXPANDED, no write", ['accepted'])
    if ask == 'many_days_at_kadesh':
        ink('1:46', '"you abode in Kadesh many days, according to the days that you abode" — %s one seat' % KADESH_DAYS)
        move('Seder Olam Rabbah 8 (the shelf\'s export); Sifrei Devarim 28:1', "nineteen years at Kadesh, nineteen wandering — the days as the days: DATA")
        return out("many days at Kadesh (1:46) — Seder Olam 8's nineteen years: DATA, no day moved", ['accepted'])
    if ask == 'the_readback_table':
        dat('the row the_readback: %d rows — %s' % (len(data['the_readback']['value']), dict(RB_GRADES)))
        return out("the readback table — forty-two reference rows graded; the two DISAGREES rows open; every retold act's entry found on the running world (CA4)", ['accepted'])
    return out('no verdict in span', [FX.NONE])


# ===== F4: THE BYPASS (Deut 2:1-25) =========================================================================
def the_bypass(case, data):
    del P[:]
    ask = case['ask']
    if ask == 'the_turn':
        ink('2:1-3', '"we turned and journeyed by the way of the Red Sea … we compassed Mount Seir many days; the LORD said to me: you have compassed this mountain long enough; turn you northward" — %s, %s, %s one seat each' % (COMPASSED_SEIR, LONG_ENOUGH_MOUNTAIN, TURN_NORTH))
        move('cold_run_chukat (CALL) — CK.edom_and_hor(death_dates) = %s' % CK_DATES[0][:50], "the departure from Mount Hor (40, 6, 1) — the retrograde marker's day at 2:2; the turn's debit CLOSED at once by the prior run Num 21:10-13 (the march past Moab)")
        dat('commanded on israel_people turn_northward — dated (40, 6, 1), closed by "Num 21:10-13"')
        return out("the turn (2:1-3) — told only here: commanded on Israel dated (40, 6, 1), CLOSED by the prior run Num 21:10-13; 'enough' the plural's second seat in the speech", ['commanded'])
    if ask == 'esau':
        ink('2:4-8', '"your brothers the sons of Esau who dwell in Seir … do not contend with them … not so much as for the sole of the foot … I have given Mount Seir to Esau for a possession; food you shall buy of them for money" — %s, %s, %s, %s, %s' % (BROTHERS_ESAU, NOT_CONTEND, FOOT_BREADTH, SEIR_TO_ESAU, BUY_FOOD))
        move('cold_run_joseph (CALL) — JS.edom(parted_for_room) = %s; Kiddushin 18a:2; Bava Kamma 38a:16' % JS_SEIR['v'], "Esau dwelt in Mount Seir (Genesis 36:8) — the grant standing; a gentile inherits by Torah law from this verse; the a fortiori from Midian needed the bar")
        dat('the row the_bypass_commands: edom %s' % (data['the_bypass_commands']['value']['edom'],))
        return out("Esau (2:4-8) — contending_barred and land_granted (Mount Seir) on Edom: the bar and the grant told only here (Kiddushin 18a:2; JS by CALL); the purchase a permission", ['contending_barred', 'land_granted'])
    if ask == 'forty_years_lacking_nothing':
        ink('2:7', '"these forty years the LORD your God has been with you; you have lacked nothing" — %s, %s; the parser [%d]' % (FORTY_YEARS_THESE, LACKED_NOTHING, FORTY))
        move('cold_run_exodus_story (CALL) — ES.manna(forty_years) = %d' % ES_MANNA['v'], "'the sons of Israel ate the manna forty years' (Exodus 16:35) — the provision's span by CALL")
        return out("forty years lacking nothing (2:7) — [40]: the manna's forty years (ES by CALL; Exodus 16:35)", ['accepted'])
    if ask == 'the_route':
        ink('2:8', '"we passed by our brothers the sons of Esau … from the way of the Arabah, from Elath and from Ezion-geber; we turned and passed by the way of the wilderness of Moab" — against 21:4\'s "by the way of the Red Sea"')
        move('Onkelos 2:8; cold_run_journeys (CALL) — JO.the_stations', "the route named by its stations — the Arabah, Elath, Ezion-geber (33:35-36 the itinerary's seat), the wilderness of Moab (21:11)")
        return out("the route (2:8) — Elath and Ezion-geber, the way of Moab's wilderness: the itinerary's stations by CALL; 21:4's Red Sea way the same road", ['accepted'])
    if ask == 'moab':
        ink('2:9', '"do not harass Moab nor contend with them in battle, for I will not give you of his land for a possession, because I have given Ar to the children of Lot" — %s one seat; "Ar" %s' % (HARASS_MOAB, AR_SEATS[:4]))
        move('cold_run_balak (CALL) — BK.phinehas_and_midian(midian_not_moab) = %s; cold_run_mamre (CALL) — MM.sodom(two_peoples_named) = %s; cold_run_chukat (CALL) — CK.DATA[sihon_purified] = %s' % (BK_MIDIAN[0][:50], MM_TWO['v'], CK.DATA['sihon_purified']['value']), "Moses' a fortiori from Midian needed the bar (Bava Kamma 38a:16); Moab Lot's elder daughter's; Moab's land purified through Sihon (Chullin 60b:13)")
        dat('the row the_bypass_commands: moab %s' % (data['the_bypass_commands']['value']['moab'],))
        return out("Moab (2:9) — contending_barred and land_granted (Ar) on the Moabites: the bar the a fortiori needed (Bava Kamma 38a:16; BK by CALL); Lot's elder daughter's people (MM by CALL)", ['contending_barred', 'land_granted'])
    if ask == 'harassing_permitted':
        move('Horayot 10b:19 (R. Yochanan); Nazir 23b:11', "'do not contend with Moab IN BATTLE' — battle forbidden, harassing not: the reward of the elder daughter's euphemism; Ammon not even harassed (11a:1)")
        dat('the row the_bypass_commands: the_difference — a PARAMETER of the block\'s reach')
        return out("harassing Moab — permitted, battle forbidden (Horayot 10b:19): exempt from the bar's reach; Ammon's bar reaches further", ['exempt'])
    if ask == 'the_emim':
        ink('2:10-12', '"the Emim dwelt there before … Rephaim … Anakim; the Horites dwelt in Seir before, and the sons of Esau dispossessed them … as Israel did to the land of his possession" — %s, %s (%d seats), %s (%d), %s one seat' % (EMIM, 'Rephaim', len(REPHAIM), 'Horites', len(HORITES), AS_ISRAEL_DID))
        move('cold_run_primeval (CALL) — PR.war(og) = %s; cold_run_joseph (CALL) — JS.edom (the Horites of 36:20); Chullin 60b:11' % PR_OG['v'], "Genesis 14:5-6's Rephaim, Emim and Horites at their first seats; the verses fit to be burned that are the Torah's body")
        dat('the row the_dispossessions: %s' % data['the_dispossessions']['value'])
        return out("the Emim and the Horites (2:10-12) — Genesis 14:5-6's peoples (PR and JS by CALL); 'as Israel did' the ink's pattern of title: the dispossessions DATA", ['accepted'])
    if ask == 'the_zered':
        ink('2:13-14', '"rise up and get you over the brook Zered; and we went over the brook Zered; the days from Kadesh-barnea until we crossed the brook Zered — thirty-eight years, until all the generation of the men of war was consumed" — %s, %s; the parser [%d]' % (ZERED, THIRTY_EIGHT_YEARS, THIRTY_EIGHT))
        move('cold_run_chukat (CALL) — CK.well_and_kings(zered_date) = %s; cold_run_shelach (CALL) — SL.decree(count_from) = %s' % (CK_ZERED[0][:60], SL_FROM[0][:40]), "the Zered crossed after the thirty-eight years; 40 − 38 = 2 the era's year at the decree")
        dat('the row the_thirty_eight: %s — the supplied crossing CLOSED by the prior run Num 21:10-13 (21:12 the camp at Zered)' % data['the_thirty_eight']['value'])
        return out("the Zered (2:13-14) — told only here: commanded on Israel cross_the_brook_zered, CLOSED by the prior run Num 21:10-13; [38] against the tape's years (the spies' return to the departure from Mount Hor)", ['commanded'])
    if ask == 'the_men_of_war_consumed':
        ink('2:14-16', '"until all the generation of the men of war was consumed … the hand of the LORD was against them to discomfit them … when all the men of war were consumed and dead" — %s, %s, %s' % (GENERATION_CONSUMED, HAND_AGAINST, DISCOMFIT))
        move('cold_run_shelach (CALL) — SL.decree(deaths_ceased) = %s; SL.decree(due) = %s' % (SL_CEASED[0][:60], SL_DUE[0][:40]), "the carcasses timer fired at (40, 5, 9); the dying ceased the fifteenth of Av (Bava Batra 121a:9; Taanit 30b:12)")
        return out("the men of war consumed (2:14-16) — the decree's timer FIRED at (40, 5, 9) read; the dying ceased (40, 5, 15) by CALL (Taanit 30b:12)", ['accepted'])
    if ask == 'the_speech_resumed':
        ink('2:17', '"and the LORD SPOKE to me, saying" — %s: the Bible\'s ONE seat (the six "said to me" %s)' % (SPOKE_TO_ME, SAID_TO_ME))
        move('Bava Batra 121b:1 (credited); Taanit 30b:12', "the speech resumed only after the last of that generation — the fifteenth of Av")
        return out("the speech resumed (2:17) — 'SPOKE to me' the Bible's one seat: only after the last of that generation (Bava Batra 121b:1)", ['accepted'])
    if ask == 'ammon':
        ink('2:17-19', '"when you come near over against the children of Ammon, do not harass them nor contend with them, for I will not give you of the land of the children of Ammon" — "the sons of Ammon" %d Bible seats; "the land of the sons of Ammon" %s' % (len(SONS_OF_AMMON), LAND_AMMON))
        move('Bava Kamma 38b:6; Horayot 11a:1; Nazir 23b:12; cold_run_chukat (CALL) — CK.DATA[ammon_border] = %s' % CK.DATA['ammon_border']['value'], "Ammon not even harassed — the younger daughter's reward; 21:24's border STRONG, here commanded off-limits")
        dat('the row the_bypass_commands: ammon %s — the-sons-of-ammon the one NEW written-on party' % (data['the_bypass_commands']['value']['ammon'],))
        return out("Ammon (2:17-19) — contending_barred and land_granted on the sons of Ammon: not even harassed (Bava Kamma 38b:6); 21:24's strong border the bar's reason (CK.DATA by CALL); the one new party", ['contending_barred', 'land_granted'])
    if ask == 'the_avvim':
        ink('2:20-23', '"the Zamzummim … the Avvim who dwelt in villages as far as Gaza, the Caphtorim who came out of Caphtor destroyed them" — %s, %s (Genesis 10:14)' % (ZAMZUMMIM, CAPHTORIM))
        move('Chullin 60b:11 (credited); Genesis 10:14 by CALL (PR.nations)', "Reish Lakish's verses fit to be burned that are the Torah's body — the Avvim's dispossession the title's pattern")
        return out("the Avvim (2:20-23) — the Caphtorim's dispossession, Genesis 10:14's people (Chullin 60b:11): the dispossessions DATA", ['accepted'])
    if ask == 'sihon_commanded':
        ink('2:24-25', '"rise up, take your journey, and pass over the valley of Arnon; behold, I have given into your hand Sihon … begin to possess it, and contend with him in battle; this day will I begin to put the dread of you" — %s, %s, %s, %s' % (RISE_ARNON, BEGIN_POSSESS, BEGIN_DREAD, WHOLE_HEAVEN[:3]))
        move('Avodah Zarah 25a:7-9; Taanit 20a:6-8', "the sun stood still for Moses — 'I will begin' / 'I will begin' (Joshua 3:7), 'put' / 'put' (Joshua 10:12), the verse itself: DATA")
        dat('commanded on israel_people begin_to_possess_sihons_land — dated (40, 6, 1), closed by "Num 21:24-25" (the smiting and possession)')
        return out("Sihon commanded (2:24-25) — told only here: commanded on Israel, CLOSED by the prior run Num 21:24-25; the dread's row the sun for Moses (Avodah Zarah 25a; Taanit 20a): DATA", ['commanded'])
    return out('no verdict in span', [FX.NONE])


# ===== F5: SIHON AND OG (Deut 2:26-3:11) ====================================================================
def sihon_and_og(case, data):
    del P[:]
    ask = case['ask']
    if ask == 'the_messengers':
        ink('2:26-28', '"I sent messengers out of the wilderness of Kedemoth to Sihon king of Heshbon with words of peace: let me pass through your land; by the road, by the road I will go" — %s, %s, %s, %s; 2:27 %d tokens for 21:22\'s %d (computed: %d shared)' % (KEDEMOTH, WORDS_PEACE, ROAD_ROAD, NOT_TURN, len(MSG_DEUT), len(MSG_NUM), len(set(MSG_DEUT) & set(MSG_NUM))))
        move('Sifrei Devarim 199:5 (credited, forward); cold_run_chukat (CALL) — CK.edom_and_hor(two_messages)', "'words of peace' — the war's law of Deuteronomy 20:10 read here; the Edom and Sihon messages share thirteen tokens (computed at chukat)")
        return out("the messengers (2:26-28) — nine tokens for 21:22's seventeen: SHORTENED; Kedemoth and 'words of peace' told only here", ['accepted'])
    if ask == 'the_edom_disagreement':
        ink('2:29', '"as the sons of Esau who dwell in Seir did for me, and the Moabites who dwell in Ar" — %s, %s one seat each' % (ESAU_DID_FOR_ME, MOABITES_AR))
        move('cold_run_chukat (CALL) — CK.edom_and_hor(edom_passage) = %s' % CK_EDOM[0][:80], "the DISPUTE row holds both arms — 20:18-21's double refusal and 2:28-29's purchase; the Sifrei silent; Judges 11:17 outside the Torah: no link of our own")
        dat('the row the_edom_disagreement: %s — OPEN (R4)' % data['the_edom_disagreement']['value'])
        return out("the Edom disagreement (2:29) — 'as the sons of Esau did for me' against 20:18-21's refusal: DISAGREES, the chukat row's two arms (CK by CALL), an OPEN row", ['accepted'])
    if ask == 'the_hardening':
        ink('2:30', '"Sihon would not let us pass; for the LORD your God hardened his spirit and made his heart obstinate" — %s one seat' % HARDENED)
        move('cold_run_chukat (CALL) — CK.well_and_kings(sihon_refused) = %s; Exodus 4-14\'s hardening by REFERENCE' % CK_REFUSED[0][:50], "Pharaoh's two verbs at Sihon — the exodus story's hardening seats the kin; 21:23 says he did not let Israel pass")
        return out("the hardening (2:30) — told only here in Pharaoh's verbs (the exodus story by REFERENCE); sihon's refused read (CK by CALL): EXPANDED", ['accepted'])
    if ask == 'jahaz':
        ink('2:32-33', '"Sihon came out against us, he and all his people, to battle at Jahaz; the LORD our God delivered him before us and we smote him and his son and all his people" — %s; 2:32 %d tokens for 21:23\'s %d (computed: %d shared)' % (JAHAZ, len(JAHAZ_DEUT), len(JAHAZ_NUM), len(set(JAHAZ_DEUT) & set(JAHAZ_NUM))))
        return out("Jahaz (2:32-33) — eight tokens for 21:23's twenty: SHORTENED; 21:24's smiting the run", ['accepted'])
    if ask == 'the_written_and_read':
        ink('2:33', '"and we smote him and his SON and all his people" — written "his son" (the DB\'s eleven tokens), read "his sons" (the store\'s twelve); Onkelos plural')
        move('the reading\'s find (2026-09-15); Onkelos 2:33', "the written and the read — the store's mixed families a display sitting's; the DB's consonants the ink")
        return out("written 'his son', read 'his sons' (2:33) — the DB's eleven tokens against the store's twelve; Onkelos plural: the reading's find, DATA", ['accepted'])
    if ask == 'the_ban':
        ink('2:34-35; 3:6-7', '"we devoted every city — the men, the women and the little ones; we left none remaining; only the cattle we took" — %s (2:34 and 3:6 alone), %s, %s' % (DEVOTED_WE, EVERY_CITY_MEN, NONE_LEFT))
        move('cold_run_primeval (CALL) — PR.pieces(fourth_generation) = %s (fx %s)' % (PR_FOURTH['v'], PR_FOURTH['fx']), "'the iniquity of the Amorite is not yet full' (Genesis 15:16) — amorite_not_full on the Amorite READ beside the ban: a printed line, no verdict; Deuteronomy 20:16-17 FORWARD")
        dat('the row the_ban: %s — destroyed on the-amorite TWICE (the supplied acts sihons_cities_devoted, ogs_cities_devoted)' % data['the_ban']['value'])
        return out("the ban (2:34-35; 3:6-7) — told only in the retelling: destroyed on the Amorite twice (21:24-25, 21:35 say smote and possessed); 15:16's status read; the cherem law forward", ['destroyed'])
    if ask == 'aroer_to_gilead':
        ink('2:36-37', '"from Aroer on the edge of the valley of Arnon … to Gilead there was not a city too high for us; only to the land of the sons of Ammon you came not near" — %s, %s, %s' % (FROM_AROER, TOO_HIGH, LAND_AMMON[:3]))
        move('cold_run_chukat (CALL) — CK.well_and_kings(ammon_border) = %s' % CK_AMMON[0][:60], "21:24's border STRONG; here RESPECTED — the same border, the bar's reason")
        return out("Aroer to Gilead (2:36-37) — the border respected (2:37) against 21:24's strong (CK by CALL): EXPANDED", ['accepted'])
    if ask == 'og_turned':
        ink('3:1-3', '"we turned and went up the way to Bashan; Og came out against us … the LORD said to me: fear him not … as you did to Sihon" — %s, %s (3:2 = 21:34), %s; 3:1-3 %d tokens for 21:33-35\'s %d, %d shared, the shifts %s (computed)' % (EDREI, FEAR_HIM_NOT, AS_TO_SIHON, len(OG_D), len(OG_N), OG_SHARED, OG_SHIFT))
        move('cold_run_chukat (CALL) — CK.well_and_kings(deut3_delta) = %s' % CK_DELTA[0], "we for they, 'to me' for 'to Moses' — the chukat runner's own row")
        return out("Og turned (3:1-3) — 21:33-35 with the persons shifted (we for they; to me for to Moses): TURNED, the five shifts computed; fear_not_promised on Moses read", ['accepted'])
    if ask == 'the_sixty_cities':
        ink('3:4-5', '"sixty cities, all the region of Argob, the kingdom of Og in Bashan; all these cities fortified with high walls, gates and bars" — the parser [%d]; %s, %s, %s' % (SIXTY, SIXTY_CITIES, ARGOB, HIGH_WALLS))
        move('Arakhin 32b:6; Megillah 10a:10; Shevuot 16a:14; Arakhin 33b:22 (credited)', "the walled cities from Joshua's days many, the re-sanctified enumerated; 'walled' learned from 3:5 by the verbal analogy")
        dat('the row the_sixty_cities: %s' % data['the_sixty_cities']['value'])
        return out("the sixty cities (3:4-5) — [60], Argob's; the walled cities from Joshua's days (Arakhin 32b:6; Megillah 10a:10); Leviticus 25:29's 'walled' learned here: DATA", ['accepted'])
    if ask == 'ogs_bed':
        ink('3:11', '"only Og king of Bashan remained of the remnant of the Rephaim; behold his bedstead was a bedstead of iron … nine cubits its length and four cubits its breadth, by the cubit of a man" — the parser %s; %s, %s, %s, %s' % (BED, REMNANT_REPHAIM, IRON_BED, NINE_CUBITS, CUBIT_OF_MAN))
        move('Mishnah Kelim 17:9-10; Mishnah Eruvin 4:8; cold_run_chukat (CALL) — CK.DATA[og_lore] = %s; cold_run_primeval (CALL) — PR.war(og) = %s' % (CK.DATA['og_lore']['value'], PR_OG['v']), "the cubit of which they spoke the medium one; Og Sihon's brother of the Rephaim, the escapee")
        dat('the row ogs_bed: %s' % data['ogs_bed']['value'])
        return out("Og's bed (3:11) — [9, 4] by the cubit of a man (Kelim 17:9-10); the remnant of the Rephaim; Og's lore by CALL: DATA", ['accepted'])
    if ask == 'hermon':
        ink('3:8-9', '"from the valley of Arnon to Mount Hermon — the Sidonians call Hermon Sirion, and the Amorites call it Senir" — %s (%d seats), %s, %s' % ('Hermon', len(HERMON), SIRION, SENIR))
        move('Chullin 60b:14 (credited); Song 4:8', "every nation built a city on Hermon and named it after a mountain of the land — the verses fit to be burned")
        return out("Hermon (3:8-9) — Sirion and Senir, the nations' names (Chullin 60b:14; Song 4:8): EXPANDED", ['accepted'])
    return out('no verdict in span', [FX.NONE])


# ===== F6: THE EAST AND THE CHARGES (Deut 3:12-22) ==========================================================
def the_east_and_the_charges(case, data):
    del P[:]
    ask = case['ask']
    if ask == 'the_division':
        ink('3:12-13', '"from Aroer … and HALF the hill country of Gilead and its cities I gave to the Reubenite and the Gadite; the rest of Gilead and all Bashan … to the HALF tribe of Manasseh" — the halves %s by rule 30; %s, %s, %s; 3:12-13 %d tokens for 32:33\'s %d (computed)' % (HALVES, HALF_GILEAD, REUBENITE_GADITE[:3], HALF_MANASSEH, len(DIV_D), len(DIV_N)))
        move('cold_run_gad_reuben (CALL) — GR.the_grant(three_parties) = %s; cold_run_borders (CALL) — BO.moses_restatement(the_nine_and_a_half) = %s' % (GR_THREE[0][:60], BO_NINE[0][:50]), "the three holdings of 32:33 read; 34:13-15's halves the kin")
        return out("the division (3:12-13) — 32:33's three holdings read back, DIVIDED: half Gilead to the two, the rest and Bashan to the half tribe (thirty-six tokens for twenty-nine); the halves [1/2] by rule 30: EXPANDED", ['accepted'])
    if ask == 'jair':
        ink('3:14', '"Jair son of Manasseh took all the region of Argob to the border of the Geshurite and the Maacathite, and called them after his own name, Bashan-havvoth-jair, to this day" — %s, %s (%d seats), %s; %d tokens for 32:41\'s %d (computed)' % (JAIR_MANASSEH, 'Havvoth-jair', len(HAVVOTH_JAIR), GESHURITE, len(JAIR_D), len(JAIR_N)))
        move('cold_run_gad_reuben (CALL) — GR.machir_jair_nobah(jair) = %s' % GR_JAIR[0][:60], "32:41's taking read; 1 Kings 4:13 the kin; 'to this day' the retelling's")
        return out("Jair (3:14) — 32:41 read back, EXPANDED (twenty-three tokens for eleven): Argob, the Geshurite and the Maacathite, 'to this day' told only here", ['accepted'])
    if ask == 'machir':
        ink('3:15', '"and to Machir I gave Gilead" — %s one seat' % TO_MACHIR)
        move('cold_run_gad_reuben (CALL) — GR.machir_jair_nobah(gilead_given) = %s' % GR_GILEAD[0][:60], "32:40's 'Moses gave' in the first person — the clan under the ancestor's name")
        return out("Machir (3:15) — 32:40's 'Moses gave' in the first person: TURNED", ['accepted'])
    if ask == 'the_borders':
        ink('3:16-17', '"from Gilead to the valley of Arnon, the middle of the valley the border, to the river Jabbok, the border of the children of Ammon; the Arabah and the Jordan for a border, from Chinnereth to the sea of the Arabah, the Salt Sea, under the slopes of Pisgah eastward" — %s, %s (%d seats), %s, %s' % (MIDDLE_BROOK, 'the Jabbok', len(JABBOK), SALT_SEA_ARABAH, SLOPES_PISGAH))
        dat('the row the_easts_borders: %s — no write, the holdings stand' % data['the_easts_borders']['value'])
        return out("the east's borders (3:16-17) — told only here: the Arnon's middle, the Jabbok, Chinnereth to the Salt Sea under Pisgah — DATA, no write", ['accepted'])
    if ask == 'the_charge_to_the_tribes':
        ink('3:18-20', '"I commanded you at that time: the LORD your God has given you this land to possess; you shall pass over ARMED before your brothers … until the LORD gives rest to your brothers as to you … then you shall return every man to his possession" — %s, %s, %s (Joshua 1:15), %s' % (GIVEN_THIS_LAND, ARMED, UNTIL_REST, EACH_TO_POSSESSION))
        move('cold_run_gad_reuben (CALL) — GR.the_condition(positive_arm) = %s; GR.DATA[half_manassehs_stipulation] = %s; GR.the_offer(not_return) = %s' % (GR_POS[0][:50], GR.DATA['half_manassehs_stipulation']['value'], GR_RETURN[0][:50]), "the condition's debit OPEN read; half Manasseh included by the retelling; Joshua 22:4 the release outside the Torah")
        dat('the row the_armed_passage: %s' % data['the_armed_passage']['value'])
        return out("the charge to the tribes (3:18-20) — 32:20-24's condition in the first person with half Manasseh included: TURNED; the debit OPEN read (GR by CALL); 'until the LORD gives rest' Joshua 1:15's", ['accepted'])
    if ask == 'joshuas_charge':
        ink('3:21-22', '"and I commanded Joshua at that time: your eyes have seen all that the LORD your God has done to these two kings; so shall the LORD do to all the kingdoms; you shall not fear them, for the LORD your God, He fights for you" — %s, %s (PLENE, the Torah\'s one seat), %s, %s, %s, %s' % (COMMANDED_JOSHUA_TIME, JOSHUA_PLENE, EYES_SEEN, ALL_KINGDOMS, NOT_FEAR_THEM, HE_FIGHTS))
        move('Sifrei Devarim 29:8-9; Joshua 1:6; 23:3, 10', "the condition Joshua broke at Ai — the run against the spec outside the Torah; 'He fights for you' Joshua's own refrain")
        dat('the row joshuas_charge: %s' % data['joshuas_charge']['value']['promise'])
        return out("Joshua's charge (3:21-22) — told only here: fear_not_promised on Joshua (21:34's effect at its second party); Joshua plene; Ai's run outside the Torah (the Sifrei 29:8-9)", ['fear_not_promised'])
    return out('no verdict in span', [FX.NONE])


# ===== F7: THE PLEA (Deut 3:23-29) ==========================================================================
def the_plea(case, data):
    del P[:]
    ask = case['ask']
    if ask == 'the_plea':
        ink('3:23-26', '"and I besought the LORD at that time … let me go over, I pray, and see the good land … but the LORD was wroth with me for your sakes and did not hear me: let it suffice you; speak no more to Me of this matter" — %s, %s, %s, %s, %s, %s' % (BESOUGHT, LET_ME_GO_OVER, WROTH_FOR_YOU, NOT_HEAR_ME, SUFFICE_YOU, SPEAK_NO_MORE))
        move('Berakhot 32a:32; Avodah Zarah 7b:18; Berakhot 30b:9; Sotah 13b:13 (credited); cold_run_beha (CALL) — BH.march(hobab) = %s' % BH_HOBAB[0][:40], "praise before the request; the pleading mode; 'let it suffice you' measure for measure; the refusal in the value as Hobab's row carries it")
        dat('plea_made on moses valued the plea AND its answer — %s; barred_from_the_land OPEN read, no new heaven write' % data['the_plea']['value']['answer'])
        return out("the plea (3:23-26) — told only here: plea_made on Moses with the refusal in the value; the barred entry OPEN read; praise before the request (Berakhot 32a:32)", ['plea_made'])
    if ask == 'the_names':
        ink('3:24', '"O Lord GOD, You have begun to show Your servant Your greatness and Your strong hand; what god is there in heaven or on earth" — %s, %s, %s (1 Kings 8:42 the other), %s; "O Lord GOD" %d Bible seats' % (BEGUN_SHOW, YOUR_GREATNESS, STRONG_HAND, WHAT_GOD, len(LORD_GOD)))
        move('Sifrei Devarim 27:4; Genesis 15:2, 15:8; 1 Kings 8:42', "'Your greatness' the binyan av; 'O Lord GOD' Abraham's two seats and Moses' two; 'Your strong hand' Solomon's prayer")
        return out("the names (3:24) — 'O Lord GOD' Abraham's and Moses'; 'Your greatness' the Sifrei 27:4's binyan av; 'Your strong hand' 1 Kings 8:42's: DATA", ['accepted'])
    if ask == 'lebanon':
        ink('3:25', '"let me go over and see the good land beyond the Jordan, that goodly hill country and Lebanon" — %s; "the good land" %d seats' % (GOOD_LAND_BEYOND, len(THE_GOOD_LAND)))
        move('Sifrei Devarim 6:2, 28:3; Gittin 56b:1; Onkelos 3:25', "Lebanon the Temple ('Lebanon shall fall by a mighty one', Isaiah 10:34); the good mountain Jerusalem — Onkelos writes the Temple in")
        return out("Lebanon (3:25) — the Temple (the Sifrei 6:2, 28:3; Gittin 56b:1); 1:7's Lebanon the region, this the house: DATA", ['accepted'])
    if ask == 'the_refusal':
        ink('3:26', '"the LORD was wroth with me for your sakes and did not hear me; the LORD said to me: let it suffice you; speak no more to Me of this matter" — "was wroth" %s (three Bible seats); "enough for you" singular %s (the plural %d seats)' % (WROTH, ENOUGH_SG, len(ENOUGH_PL)))
        move('Sotah 13b:13 (credited); cold_run_chukat (CALL) — CK.meribah(sentence)', "Moses rebuked with 'rav' (16:3, 7) and answered with 'rav' — measure for measure; the barred entry OPEN, its ground disputed (1:37)")
        return out("the refusal (3:26) — 'let it suffice you' the singular's one seat, measure for measure for Korach's (Sotah 13b:13); 'did not hear' 1:45's phrase; the barred entry read", ['accepted'])
    if ask == 'pisgah':
        ink('3:27', '"go up to the top of Pisgah and lift up your eyes westward and northward and southward and eastward, and see with your eyes; for you shall not go over this Jordan" — %s, %s, %s' % (TOP_PISGAH, FOUR_DIRECTIONS, NOT_CROSS_JORDAN))
        dat('the row the_four_directions: %s — three orders; the see_the_land debit on Moses OPEN (27:12) READ BACK, no second write' % data['the_four_directions']['value'])
        return out("Pisgah (3:27) — 27:12's command read back with Pisgah for Abarim and the four directions in the third order: TURNED; the debit OPEN read", ['accepted'])
    if ask == 'command_joshua':
        ink('3:28', '"command Joshua, and strengthen him and encourage him; for he shall go over before this people, and he shall cause them to inherit the land" — %s, %s, %s, %s; "be strong and of good courage" %d seats (Joshua 1:6 among them)' % (COMMAND_JOSHUA, STRENGTHEN, HE_SHALL_CROSS, CAUSE_THEM_INHERIT, len(BE_STRONG)))
        move('Kiddushin 29a:14 (credited)', "'command' a galvanization, immediate and for generations; the commissioning of 27:18-23 READ BACK")
        return out("command Joshua (3:28) — the commission read back (Kiddushin 29a:14 — a galvanization for generations); 'he shall cause them to inherit' the effect's second seat: TURNED", ['accepted'])
    if ask == 'beth_peor':
        ink('3:29', '"and we abode in the valley over against Beth-peor" — %s; "over against Beth-peor" %s (4:46 the speech\'s place; 34:6 Moses\' grave)' % (VALLEY_PEOR, AGAINST_PEOR))
        move('cold_run_balak (CALL) — BK.the_call(last_camp) = %s' % BK_LAST[0][:60], "the plains of Moab — the last camp; the book never moves again")
        return out("Beth-peor (3:29) — the last camp by CALL (22:1; 36:13; Deuteronomy 34:1); 4:46 and 34:6 the valley's other seats: EXPANDED", ['accepted'])
    return out('no verdict in span', [FX.NONE])
