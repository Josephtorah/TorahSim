

# ===== F4: AARON'S DEATH RETOLD (Num 33:38-40) — the tape's own marker; no write =============================
def aarons_death_retold(case, data):
    del P[:]
    ask = case['ask']
    if ask == 'the_date':
        ink('33:38', '"in the fortieth year of the going out … in the fifth month, on the first of the month" — the ordinals %s and the day [%d] = %s; "in the fortieth year" %s; "in the fifth month" %s (the Torah\'s one)' % (ORDS[38], DAY_ONE, AARON_DATE, FORTIETH, FIFTH))
        move('cold_run_chukat (CALL) — CK.AARON_DATE = %s; CK.edom_and_hor(death_dates) = %s' % (CK.AARON_DATE, CK_DATES[0]), "the tape's marker at 20:28 is built from this verse (CZ5)")
        dat('the row the_death_date: %s' % (data['the_death_date']['value'],))
        return out("Aaron died on (40, 5, 1) (33:38) — the tape's marker at 20:28, built from this verse; the ordinal reader's year and month", ['accepted'])
    if ask == 'the_age':
        ink('33:39', '"a hundred and twenty-three years at his death" — [%d]; Exodus 7:7 [%d, %d]: %d + %d = %d; Moses %d + %d = %d (Deuteronomy 34:7 [%d]); "at his death" %s' % (AGE, MOSES_80, AARON_83, AARON_83, YEAR, AGE, MOSES_80, YEAR, MOSES_120, MOSES_120, AT_DEATH))
        move('cold_run_chukat (CALL) — CK.AARON_AGE = %s; CK.edom_and_hor(aaron_age) = %s' % (CK.AARON_AGE, CK_AGE[0]), "the chukat runner's age READ")
        dat('the row aarons_age: %s' % data['aarons_age']['value'])
        return out("Aaron 123 at his death (33:39) = Exodus 7:7's 83 + 40; Moses 120 = 80 + 40 — the brothers three years apart at both ends, the ink's checksum", ['accepted'])
    if ask == 'the_eras_stamps':
        ink('33:38', '"of the going out of the children of Israel from the land of Egypt" — %s: THE ERA\'S THREE STAMPS; 1 Kings 6:1 by the parser [%d] with the ordinal %s' % (STAMPS, KINGS_480, RETOLD[('1Kgs', 6, 1)][1]))
        move('Rosh Hashanah 2b:7, 3a:11', "R. Yochanan: kings' years from Nisan — 1 Kings 6:1 juxtaposes Solomon's reign to the going out; the baraita's chain 1 Kings 6:1, Numbers 33:38, Deuteronomy 1:3")
        dat('the row the_eras_stamps: %s' % data['the_eras_stamps']['value'])
        return out("the era's three stamps — Exodus 19:1, Numbers 33:38, 1 Kings 6:1 (the 480th year): the shelf's own chain of proof (Rosh Hashanah 2b:7, 3a:11)", ['accepted'])
    if ask == 'the_era_new_year':
        ink('33:38 / Deuteronomy 1:3', 'the fortieth year in Av %s and in Shevat %s — ONE year on the Calendar; the second year in Nisan %s and Iyar %s — one year' % (ERA_AV, ERA_SHEVAT, ERA_NISAN2, ERA_IYAR2))
        move('Rosh Hashanah 2b:9, 3a:5-6', "Av and the following Shevat both 'the fortieth year' — the exodus count's New Year is not Tishrei; Nisan and Iyar both 'the second year' — not Iyar; 'the third month' without 'the second year' — not Sivan")
        move('cold_run_beha (CALL) — BH.march(year_turns) = %s' % BH_YEAR[0], "the beha runner's own row")
        return out("the era's new year from the chapter's date — (40, 5, 1) and (40, 11, 1) in one year, (2, 1, 1) and (2, 2, 20) in one year on the Calendar: not Tishrei, not Iyar (Rosh Hashanah 2b:9, 3a:5)", ['accepted'])
    if ask == 'verbal_analogy':
        ink('33:38 / Deuteronomy 1:3', 'the ordinal date %s (the article-bearing year and month) against the cardinal date %s (the number reader\'s) — THE TWO DATE FORMS HAVE TWO READERS' % (AARON_DATE, SHEVAT_DATE))
        move('Rosh Hashanah 2b:10-11', "33:38's epoch EXPLICIT ('of the going out from the land of Egypt'), Deuteronomy 1:3's bare — the verbal analogy 'the fortieth year' / 'the fortieth year' (Rav Pappa's form): a TRANSFER TAUGHT, the teacher named")
        return out("the fortieth year / the fortieth year — Deuteronomy 1:3's bare date counted from the exodus by the verbal analogy with 33:38 (Rosh Hashanah 2b:11, taught); the two date readers meet", ['accepted'])
    if ask == 'by_the_mouth_kiss':
        ink('33:38', '"Aaron the priest went up Mount Hor BY THE MOUTH OF THE LORD and died there" — the phrase\'s seat at the death')
        move('Bava Batra 17a:3', 'Moses, Aaron and Miriam died by the mouth of the LORD (33:38; Deuteronomy 34:5) — the kiss, not the Angel of Death')
        move('cold_run_chukat (CALL) — CK.DATA[death_by_the_kiss] = %s' % CK.DATA['death_by_the_kiss']['value'], "the chukat runner's row: Miriam too, by 'there' / 'there'")
        return out("by the mouth of the LORD at the death (33:38) — the kiss (Bava Batra 17a:3); the chukat runner's row death_by_the_kiss by CALL", ['accepted'])
    if ask == 'moses_seventh_adar':
        move('Kiddushin 38a:5-7; Seder Olam Rabbah 10:2', "Moses died on the seventh of Adar — the tenth of Nisan (Joshua 4:19) less thirty-three days (thirty of mourning, three of preparation); born the same day ('this day', Deuteronomy 31:2): the years of the righteous completed to the day")
        move('cold_run_chukat (CALL) — CK.edom_and_hor(death_dates) = %s' % CK_DATES[0], "Aaron by the ink, Miriam and Moses by the shelf")
        ink('33:38-39', 'the Torah\'s one full death-date is Aaron\'s; Moses\' date the shelf\'s, computed BACKWARD from a run\'s marker')
        return out("Moses' seventh of Adar — computed backward from the tenth of Nisan (Kiddushin 38a:5-6); born and died the same day, a hundred and twenty exact (38a:7): Aaron's date the ink's, Moses' the shelf's", ['accepted'])
    if ask == 'arad':
        ink('33:40', '"and the Canaanite king of Arad heard" — %s / %s: 21:1\'s hearing WITHOUT the war, the captives, the vow and Hormah, WITH "in the land of Canaan"; placed right after the death' % (ARAD, HEARD))
        move('cold_run_chukat (CALL) — CK.edom_and_hor(arad_heard) = %s' % CK_ARAD[0], "what he heard: that Aaron died and the clouds departed (Rosh Hashanah 3a:1; Taanit 9a:10; Seder Olam Rabbah 9:2)")
        move('Rosh Hashanah 3a:3', "'he is Sihon, he is Arad, he is Canaan' — the hearer's identity disputed on the shelf")
        dat('the row arads_hearing: %s' % data['arads_hearing']['value'])
        return out("the Canaanite king of Arad heard (33:40) — 21:1's hearing alone, a run citation of the tape's line at (40, 5, 1); what he heard by CALL: that Aaron died and the clouds departed", ['accepted'])
    if ask == 'the_order':
        move('Rosh Hashanah 2b:13, 3a:2', "'after he had slain Sihon' (Deuteronomy 1:4) — Sihon alive at Aaron's death: Av before Shevat")
        ink('33:38-40', 'the tape\'s own order: the death at (40, 5, 1), Arad\'s hearing at (40, 5, 1), the departure from Hor at (40, 6, 1) — CK.D_AARON %d < CK.D_DEPART %d; Sihon smitten after; Moses\' oration past the Torah' % (CK.D_AARON, CK.D_DEPART))
        return out("the fortieth year's order — Aaron's death, Arad, the departure, Sihon: the tape's days in the shelf's order (Rosh Hashanah 2b:13)", ['accepted'])
    if ask == 'no_write':
        ink('33:38-40', 'the death and the hearing stand on the tape at 20:28 (garments_transferred_and_aaron_died, date %s, age %d) and 21:1 (arad_fought_and_took_captives): A RETELLING NEVER WRITES AN ACT TWICE — no line for 33:38-40, the checkpoints CZ5 and CZ6 read the tape' % (list(AARON_DATE), AGE))
        return out("no write for 33:38-40 — the death and the hearing are the tape's 20:28 and 21:1 lines, checkpointed, not rewritten", [FX.NONE])
    return out('no verdict in span', [FX.NONE])


# ===== F5: THE COMMAND (Num 33:50-56) — the divine voice; two debits open by design; the lot cited; the negative arm as data ====
def the_command(case, data):
    del P[:]
    ask = case['ask']
    if ask == 'the_frame':
        ink('33:50', '"and the LORD spoke to Moses in the plains of Moab by the Jordan at Jericho, saying" — %s (35:1 the frame\'s second seat; 26:3 Moses and Eleazar\'s); THE ONE DIVINE FRAME of the chapter (FRAME_VERBS %s)' % (SPOKE_PLAINS, FRAME_VERBS))
        dat('installed_by BOOT with the class named — a law in the divine voice spoken in the plains of Moab; the second pass (D2) decides')
        return out("and the LORD spoke to Moses in the plains of Moab (33:50) — the chapter's one divine frame after forty-nine verses without one; 35:1 the second seat", ['accepted'])
    if ask == 'when_you_pass':
        ink('33:51', '"when you pass over the Jordan into the land of Canaan" — %d seats of the clause (33:51, 35:10, Deuteronomy 11:31 among them); "into the land of Canaan" Leviticus 14:34\'s form' % len(PASS_OVER))
        return out("when you pass over the Jordan into the land of Canaan (33:51) — the law's trigger; 35:10 and Deuteronomy 11:31 the clause's kin", ['accepted'])
    if ask == 'drive_out':
        ink('33:52-53', '"you shall drive out all the inhabitants of the land from before you" (one seat) … "and you shall dispossess the land and dwell in it" %s — the same root at both; "the inhabitants of the land" %s in the Torah (Exodus 23:31\'s promise "I will drive them out" the command\'s kin)' % (DISPOSSESS_DWELL, INHAB_T))
        move('Sotah 34a:5', "Joshua in the Jordan: 'know for what purpose you cross — to drive out the inhabitants (33:52); if not, the water will drown me and you' — the debit's first run-reading")
        return out("drive out all the inhabitants of the land (33:52-53) — a DEBIT on Israel OPEN BY DESIGN: its runs Joshua's; the crossing's purpose at the Jordan (Sotah 34a:5)", ['commanded'])
    if ask == 'figured_stones':
        ink('33:52', '"destroy all their figured stones" — %s; Leviticus 26:1\'s word %s; the lemma\'s seats %s' % (FIGURED, FIG_LEV, FIG_LEMMA))
        move('Megillah 22b:11-13', "the baraita on Leviticus 26:1 — bowing on a stone floor forbidden outside the Temple (Ulla), with outstretched arms and legs (22b:13)")
        dat('the row the_three_objects[figured_stones]: THE CELL THAT COMPILES LEVITICUS 26:1 DOES NOT EXIST — journeys → tochacha OWED; the rows filed to the debt')
        return out("their figured stones (33:52) — Leviticus 26:1's word at its ban's seat, uncompiled: the edge owed, Megillah 22b:11-13's rows filed to the debt", ['commanded'])
    if ask == 'molten_images':
        ink('33:52', '"all their molten images you shall destroy" — %s (one seat); the calf\'s word at %s in the Torah (the lemma at %d seats)' % (MOLTEN_IMG, MOLTEN_T, len(MOLTEN_LEMMA_T)))
        move('cold_run_erection (CALL) — ER.covenant(molten_two_seats) = %s; ER.calf(molten_calf) = %d seats' % (ER_MOLTEN['v'], ER_CALF['v']), "the ban on MAKING (Exodus 34:17; Leviticus 19:4) and the calf; aaron's molten_image_barred block on the tape")
        move('cold_run_holiness (CALL) — HL.frame(molten_warnings) = %s' % HL_MOLTEN['v'], "Leviticus 19:4's two warnings, R. Yosei's third")
        return out("their molten images (33:52) — the calf's word; the ban on making at Exodus 34:17 and Leviticus 19:4 by CALL (the erection and holiness runners)", ['commanded'])
    if ask == 'high_places':
        ink('33:52', '"all their high places you shall demolish" — "their high places" %s (the consonants of "at their death", Leviticus 11:31-32, Numbers 6:7 — the morphology decides); the noun\'s Torah seats %s; "demolish" %s; Leviticus 26:30 "I will destroy your high places" %s / %s' % (HIGH, HIGH_LEMMA_T, DEMOLISH, YOUR_HIGH, I_DESTROY))
        move('Mishnah Zevachim 14:4-8', "the private altars' eras — Israel's own altars permitted and forbidden by era (the erection runner's high_places_banned block on the land): ANOTHER SENSE than the Canaanites' high places to demolish")
        return out("their high places (33:52) — Leviticus 26:30's curse in the same verb on the same object: the spec/curse pair; the private altar's eras (Mishnah Zevachim 14:4-8) another sense", ['commanded'])
    if ask == 'three_objects_own':
        move('cold_run_erection (CALL) — ER.covenant(demolition_grows) = %s' % ER_GROWS['v'], "the other iconoclasm commands' lists grow — Exodus 34:13 three, Deuteronomy 7:5 four, 12:3 five: altars, pillars, asherim, graven images")
        ink('33:52', 'the figured stone, the molten image, the high place — none of them in Exodus 23:24, 34:13, Deuteronomy 7:5, 12:2-3\'s lists: 33:52\'s three are the chapter\'s own')
        dat('the row the_three_objects: %s' % data['the_three_objects']['value'])
        return out("the three objects (33:52) are the chapter's own — the other iconoclasm lists (three, four, five by CALL) name altars, pillars, asherim and graven images", ['accepted'])
    if ask == 'possess_and_dwell':
        ink('33:53', '"and you shall dispossess the land and dwell in it, for to you I have given the land to possess it" — %s / %s (each one seat); "dwell in it" Deuteronomy 11:31\'s, "to possess it" Leviticus 20:24\'s' % (DISPOSSESS_DWELL, GIVEN))
        move('cold_run_second_census (CALL) — C2.the_land(possession_before_assignment) = %s' % C2_HELD[0], "the land held before assignment (Bava Batra 119a:1, 119a:5); ZL's row 'held' — the fifth expression's 'heritage' (Exodus 6:8, OPEN on Israel) read in the perfect here")
        return out("possess the land and dwell in it, for to you I have given it (33:53) — the promise's gift read in the perfect; held before assignment by CALL; no second entry", ['accepted'])
    if ask == 'the_lot_restated':
        ink('33:54', '33:54 RESTATES 26:52-56 — "by lot" %s, "to the many you shall give more" %s, "to whom the lot goes out" %s, "by the tribes of your fathers" %s; THE NUMBER SWITCHES: %s (26:54 %s singular; 33:54 %s plural, %s singular)' % (BY_LOT_T, MANY, LOT_OUT, TRIBES_FATHERS, MORPH_54, words(26, 54)[:2], words(33, 54)[5:7], words(33, 54)[9:11]))
        move('cold_run_second_census (CALL) — C2.the_land(by_lot) = %s; (by_number_of_names) = %s; C2.DATA[division_by] = %s' % (C2_LOT[0], C2_NAMES[0], C2.DATA['division_by']['value']), "the lot's cell — its effect commanded the debit OPEN since 26:52-56: CITED, NOT REWRITTEN (CZ7)")
        dat('the row the_lot_restated: %s' % data['the_lot_restated']['value'])
        return out("the lot restated to the people (33:54) — 26:52-56 word for word with the verb's number switching inside the verse; the open debit cited by CALL, not rewritten", ['accepted'])
    if ask == 'negative_arm':
        ink('33:55-56', '"thorns in your eyes and pricks in your sides" %s / %s — run back REVERSED at Joshua 23:13 %s, Judges 2:3 %s; "leave over" the Passover\'s verb %s; "harass" %s (25:18\'s word); "as I thought" %s (Isaiah 14:24)' % (THORNS, PRICKS, PRICKS_EYES, SIDES_JUDG, LEAVE_OVER, HARASS, THOUGHT))
        move('Megillah 11a:13-14', "Saul's Amalek left Haman as the thorn; Purim's punishment 'as I thought to do to them'")
        dat('the row negative_arm_outcome: %s — NO verdict on the tape' % data['negative_arm_outcome']['value'])
        return out("the negative arm (33:55-56) — thorns in your eyes and pricks in your sides, run back reversed by Joshua 23:13 and Judges 2:3; Saul's Amalek and Haman on the shelf (Megillah 11a); a data row, no verdict on the tape", ['accepted'])
    if ask == 'the_lot_arms':
        move('cold_run_second_census (CALL) — C2.the_land(land_divided_among) = %s; (lots_mouth) = %s' % (C2_AMONG[0], C2_MOUTH[0]), "left Egypt / entered / both (Bava Batra 117a:2-3, 117b:1); the lot and the Urim (122a:3-4)")
        ink('33:54', '"by the tribes of your fathers you shall inherit" — 26:55\'s "by the names of the tribes of their fathers" restated: the arms are the second census\'s rows')
        return out("the lot's arms — divided among those who left Egypt (the running setting), those who entered, or both; by lot and by the Urim: the second census's rows by CALL", ['accepted'])
    if ask == 'private_altar_eras':
        move('Mishnah Zevachim 14:4-8', "until the tabernacle stood private altars were permitted; forbidden; Gilgal permitted; Shiloh forbidden; Nob and Gibeon permitted; Jerusalem forbidden forever")
        ink('33:52', '"their high places" the Canaanites\' — the eras\' high places Israel\'s own private altars: NOT this chapter\'s; the gemara 112b-119b cut at the docket as the erection runner\'s')
        return out("the private altar's eras (Mishnah Zevachim 14:4-8) — Israel's own altars by era, the erection runner's block: not this chapter's high places", ['exempt'])
    return out('no verdict in span', [FX.NONE])
