

# ===== F5: THE ACCEPTANCE AND THE CHARGE (Num 32:25-32) ======================================================
def the_acceptance_and_the_charge(case, data):
    del P[:]
    ask = case['ask']
    if ask == 'servants_will_do':
        ink('32:25, 27', '"your servants will do as my lord commands" — %s (one seat); "my lord" in Numbers at %s (11:28 Joshua\'s, 12:11 Aaron\'s, 14:17 to God, 36:2 the Gileadite heads\')' % (SERVANTS_WILL_DO, MY_LORD_NUM))
        return out("your servants will do as my lord commands (32:25) — 'my lord' for Moses at 32:25, 27 (Joshua's 11:28, Aaron's 12:11, the Gileadite heads' 36:2)", ['accepted'])
    if ask == 'the_order_reversed':
        ink('32:26-27', '"our little ones, our wives, our cattle and all our beasts shall be there in the cities of Gilead; and your servants will pass over, every armed one for war before the LORD" — Moses\' order held (the children first); "before the LORD for the war" %s' % BEFORE_LORD_FOR_WAR)
        return out("our little ones, our wives, our cattle and all our beasts (32:26) — Moses' order held; the retellings 'your wives, your little ones, your cattle' (Deuteronomy 3:19, Joshua 1:14)", ['accepted'])
    if ask == 'the_commission':
        ink('32:28', '"and Moses commanded concerning them Eleazar the priest, and Joshua son of Nun, and the heads of the fathers of the tribes of the children of Israel" — %s; Joshua 14:1\'s form %s WORD FOR WORD; Joshua 21:1\'s third form %s' % (TRIAD_32, TRIAD_JOSH, TRIAD_JOSH21))
        move('Bava Batra 122a:4 (credited)', "Eleazar dressed with the Urim, Joshua and all Israel before him at the lottery — the commission at its run outside the Torah")
        return out("Eleazar the priest, Joshua son of Nun and the heads of the fathers of the tribes (32:28) — Joshua 14:1's dividers word for word, 21:1 the third form; Bava Batra 122a:4's lottery", ['commanded'])
    if ask == 'second_doubling':
        ink('32:29-30', '"if the sons of Gad and the sons of Reuben pass over the Jordan with you ... you shall give them the land of Gilead for a possession; and if they do not pass over armed with you, they shall take possessions among you in the land of Canaan" — "the land is subdued before you" %s; "the land of Gilead" %s; the exam\'s proof verses (cited five and four times)' % (SUBDUED_BEFORE_YOU, LAND_OF_GILEAD_ART))
        return out("if they pass over — give them Gilead; if not — they take possessions among you in Canaan (32:29-30): the second doubling, the exam's proof verses; the commission's debit open to Joshua 22", ['commanded'])
    if ask == 'the_lords_word':
        ink('32:31', '"that which the LORD has spoken to your servants, so will we do" — the parties call MOSES\' stipulation the LORD\'s word; Joshua 22:9 "by the commandment of the LORD by the hand of Moses"; no divine frame in the chapter (FRAME_VERBS %s)' % [v for v, _, _ in FRAME_VERBS])
        move('cold_run_vows (CALL) — VW.the_man(frame) = %s' % VW_FRAME[0], "30:2's class — a law relayed in Moses' voice; the installed_by class named in the registry (the second pass's D2)")
        return out("that which the LORD has spoken to your servants, so will we do (32:31) — Moses' stipulation called the LORD's word; Joshua 22:9 'by the commandment of the LORD by the hand of Moses': a law in Moses' voice with no divine frame", ['accepted'])
    if ask == 'we_short':
        ink('32:32', '"WE will pass over armed before the LORD to the land of Canaan, and the possession of our inheritance with us across the Jordan" — "we" in its short form at %s; "the possession of our inheritance" %s against the daughters\' "a possession of an inheritance" %s' % (WE_SHORT, POSSESSION_OF_OUR, POSSESSION_OF))
        return out("'we' in its short form (32:32) — three Bible seats (Genesis 42:11, Lamentations 3:42); 'the possession of our inheritance' the daughters' construct (27:7)", ['accepted'])
    return out('no verdict in span', [FX.NONE])


# ===== F6: THE GRANT (Num 32:33) =============================================================================
def the_grant(case, data):
    del P[:]
    ask = case['ask']
    if ask == 'three_parties':
        ink('32:33', '"and Moses gave to them — to the sons of Gad and to the sons of Reuben and to half the tribe of Manasseh son of Joseph" — three grantees; "half the tribe of Manasseh" first named here (the phrase\'s seats include %s)' % ('Num 34:14' if 'Num 34:14' in HALF_MANASSEH else HALF_MANASSEH[:3]))
        return out("to the sons of Gad, to the sons of Reuben and to half the tribe of Manasseh (32:33) — three transfers; half Manasseh first named at the grant", ['holding_given'])
    if ask == 'two_kingdoms':
        ink('32:33', '"the kingdom of Sihon king of the Amorite" %s (one seat) "and the kingdom of Og king of Bashan" %s — "the land with its cities in the borders, the cities of the land round about"' % (KINGDOM_SIHON, KINGDOM_OG))
        move('cold_run_chukat (CALL) — CK.well_and_kings(land_east) = %s' % CK_EAST[0], "the chukat runner's land_possessed on israel_people at 21:24-25, 21:31-32, 21:35 — THE GRANT'S SOURCE ON THE LEDGER; CK.well_and_kings(deut3_delta) = %s; (og_lore) = %s" % (CK_DELTA[0], CK_OG[0]))
        return out("the kingdom of Sihon king of the Amorite (one seat) and the kingdom of Og king of Bashan (Deuteronomy 3's and this) — the chukat runner's land possessed at 21:24-35 by CALL: the grant's source", ['holding_given'])
    if ask == 'half_manassehs_stipulation':
        ink('32:33', 'no stipulation spoken to half Manasseh in the chapter (32:20-32 address the two tribes alone — COMPOUND %s)' % COMPOUND)
        dat('the row half_manassehs_stipulation: %s' % data['half_manassehs_stipulation']['value']); move('Bava Batra 118b:8 (credited)', "'ten parts fell to Manasseh, beside the land of Gilead and Bashan beyond the Jordan' (Joshua 17:5-6) — the shelf's line between the tribe's ten parts and its east")
        return out("no stipulation spoken to half Manasseh in the chapter; Deuteronomy 3:18-20, Joshua 1:12-15, 4:12 extend the crossing to the three; Joshua 17:5-6 'beside the land of Gilead and Bashan' (Bava Batra 118b:8)", ['accepted'])
    if ask == 'the_count':
        ink('26:7, 18, 34; Joshua 4:13; 1 Chronicles 5:18', 'the two and a half — %d + %d + %d / 2 = %d; Joshua 4:13 "about forty thousand armed" [%d]; 1 Chronicles 5:18 "that went out to war" [%d]' % (C2.C26['reuben'], C2.C26['gad'], C2.C26['manasseh'], TWO_AND_A_HALF, FORTY_THOUSAND, CHRONICLES_COUNT))
        move('cold_run_second_census (CALL) — C2.the_roll(total) = %s' % C2_TOTAL[0], "the counts the second census's own rows (the population table on the tape — the checkpoint CG5 reads them)")
        dat('the row the_forty_thousand: %s' % data['the_forty_thousand']['value'])
        return out("the two and a half's count — 43,730 + 40,500 + 52,700 ÷ 2 = 110,580 from the second census by CALL; Joshua 4:13's about forty thousand; 1 Chronicles 5:18's 44,760", ['accepted'])
    if ask == 'land_held':
        move('cold_run_second_census (CALL) — C2.the_land(possession_before_assignment) = %s' % C2_HELD[0], "Rabba: Eretz Yisrael held before assignment (Bava Batra 119a:1, 119a:5 — credited) — the standing 'a possession' carries at 32:5, 22, 29, 32 (%s)" % FOR_A_POSSESSION[-3:])
        dat('the row the_land_east_status: %s' % data['the_land_east_status']['value'])
        return out("in possession before assignment — the rows are holdings before the lot (C2 by CALL; Bava Batra 119a:1, 119a:5): the standing 'a possession' carries", ['holding_given'])
    if ask == 'not_by_lot':
        move('cold_run_second_census (CALL) — C2.the_land(by_lot) = %s; (thirteen_tribes) = %s' % (C2_LOT[0], C2_THIRTEEN[0]), "26:55's lot is Canaan's; the east by Moses' word (32:33) — israel_people's OPEN commanded divide_the_land is not this chapter's run")
        return out("the east by Moses' word, not by lot — 26:55's lot is Canaan's (C2 by CALL: the place by lot, Joshua 14-19 the run); the OPEN divide_the_land not this chapter's run", ['accepted'])
    if ask == 'bequeath_not_inherit':
        move('cold_run_second_census (CALL) — C2.the_land(morasha) = %s' % C2_MORASHA[0], "Bava Batra 119b:3-4 (credited): Exodus 6:8's 'heritage' — the exodus generation bequeath and do not inherit; 'You will bring THEM in' (Exodus 15:17)")
        return out("the exodus generation bequeath and do not inherit (Bava Batra 119b:3-4; C2 morasha by CALL) — the doomed set's title to the land", ['accepted'])
    return out('no verdict in span', [FX.NONE])


# ===== F7: THE CITIES (Num 32:34-38) =========================================================================
def the_cities(case, data):
    del P[:]
    ask = case['ask']
    if ask == 'gads_eight':
        ink('32:34-36', '%s — Gad\'s EIGHT: %s; "fortified cities and folds for sheep"' % (GAD_BUILT, GAD_CITIES))
        return out("Dibon, Ataroth, Aroer, Atroth-shophan, Jazer, Jogbehah, Beth-nimrah, Beth-haran — Gad's eight (32:34-36), fortified cities and folds for sheep", ['cities_built'])
    if ask == 'reubens_six':
        ink('32:37-38', '%s — Reuben\'s SIX: %s; "their names being changed" %s (one seat); "and they called by names the names of the cities which they built"' % (REUBEN_BUILT, REUBEN_CITIES, NAMES_CHANGED))
        return out("Heshbon, Elealeh, Kiriathaim, Nebo, Baal-meon and Sibmah — Reuben's six (32:37-38); 'their names being changed' one seat", ['cities_built'])
    if ask == 'the_split':
        ink('32:3 against 32:34-38', 'the nine %s — Gad\'s four (Ataroth, Dibon, Jazer, Nimrah as Beth-nimrah), Reuben\'s five (Heshbon, Elealeh, Sebam as Sibmah, Nebo, Beon as Baal-meon): the reading\'s claim MT32A-09' % NINE)
        return out("the nine asked split four and five — Gad's Ataroth, Dibon, Jazer, Nimrah (as Beth-nimrah); Reuben's Heshbon, Elealeh, Sebam (as Sibmah), Nebo, Beon (as Baal-meon)", ['accepted'])
    if ask == 'dibon_gad':
        ink('33:45-46', '"and they camped at Dibon Gad; and they journeyed from Dibon Gad" — %s / %s: the itinerary\'s own witness, the next chapter\'s' % (words(33, 45)[-2:], words(33, 46)[1:3]))
        return out("Dibon Gad (33:45-46) — the itinerary's own witness to the city's tribe, the next chapter's", ['accepted'])
    if ask == 'two_crossed':
        ink('Joshua 13:17, 13:26, 13:20', 'Reuben\'s list: %s (Heshbon and Dibon both); Gad\'s border "from Heshbon" (13:26); Beth-peor Reuben\'s (13:20)' % ' '.join(words(13, 17, 'Josh')))
        dat('the row the_two_crossed_cities: %s' % data['the_two_crossed_cities']['value'])
        return out("Dibon and Heshbon in Reuben's list at Joshua 13:17, Heshbon on Gad's border at 13:26 — the two crossed between the tribes; Beth-peor Reuben's (13:20)", ['accepted'])
    if ask == 'moses_grave':
        ink('32:37-38', 'Nebo among Reuben\'s six')
        move('Sotah 13b:20', "R. Yehuda: Moses died in Reuben's portion — Nebo is Reuben's (32:37-38); Onkelos 32:3 'Nebo, the burial place of Moses' the same reading")
        dat('the row moses_grave: %s' % data['moses_grave']['value'])
        return out("Nebo Reuben's (32:37-38) — Moses died in Reuben's portion (Sotah 13b:20); Onkelos 'Nebo, the burial place of Moses' at 32:3; the Sifrei 106:1's Gad the other arm", ['accepted'])
    if ask == 'the_build_closed':
        ink('32:34-38 against 32:24', '"and the sons of Gad built ... and the sons of Reuben built" — the run of "build for yourselves cities for your little ones" (%s): the build debit CLOSED BY VALUE' % CITIES_YOUR)
        return out("the cities built (32:34-38) — the run of 32:24's 'build for yourselves cities': the build debit closed by value, the chapter's one Torah-closed debit", ['cities_built'])
    return out('no verdict in span', [FX.NONE])


# ===== F8: MACHIR, JAIR AND NOBAH (Num 32:39-42) =============================================================
def machir_jair_nobah(case, data):
    del P[:]
    ask = case['ask']
    if ask == 'sons_of_machir':
        ink('32:39', '"and the sons of Machir son of Manasseh went to Gilead and took it, and dispossessed the Amorite who was in it" — "the sons of Machir son of Manasseh" %s (Genesis 50:23\'s collective, born on Joseph\'s knees); "the Amorite who was in it" %s; the verb 21:32\'s' % (SONS_OF_MACHIR, AMORITE_IN_IT))
        move('cold_run_chukat (CALL) — CK.well_and_kings(spy_verb) = %s' % CK_SPY[0], "21:32's 'dispossessed the Amorite who was there' — the same verb at Jazer")
        return out("the sons of Machir son of Manasseh (32:39) — Genesis 50:23's collective, born on Joseph's knees; Gilead taken, the Amorite dispossessed (21:32's verb)", ['land_possessed'])
    if ask == 'gilead_given':
        ink('32:40', '"and Moses gave Gilead to Machir son of Manasseh, and he dwelt in it" — "Machir son of Manasseh" at %s; 26:29 "Machir begot Gilead" (C2.FAMILIES[manasseh][0] = %s)' % (MACHIR_SON, C2.FAMILIES['manasseh'][0]))
        return out("Moses gave Gilead to Machir son of Manasseh (32:40) — the clan under the ancestor's name (26:29; Joshua 17:1 the man of war; Deuteronomy 3:15)", ['holding_given'])
    if ask == 'jair':
        ink('32:41', '"and Jair son of Manasseh went and took their villages, and called them Havvoth-jair" — Havvoth-jair at %s (six seats); "went and took" at 32:41-42' % HAVVOTH)
        return out("Jair son of Manasseh took their villages and called them Havvoth-jair (32:41) — six seats; 'went and took' at 32:41-42 alone", ['land_possessed'])
    if ask == 'jairs_lineage':
        ink('32:41; 1 Chronicles 2:21-23', '"Jair son of Manasseh" at %s; 1 Chronicles 2:21 Hezron at [%d] took Machir\'s daughter, 2:22 Jair\'s [%d] cities, 2:23 [%d] cities; Judges 10:4 the judge\'s %s' % (JAIR_SON, RETOLD[('1Chr', 2, 21)][0], RETOLD[('1Chr', 2, 22)][0], RETOLD[('1Chr', 2, 23)][0], RETOLD[('Judg', 10, 4)]))
        dat('the row jairs_lineage: %s' % data['jairs_lineage']['value'])
        return out("Jair son of Manasseh (32:41; Deuteronomy 3:14; 1 Kings 4:13) against 1 Chronicles 2:21-22's Hezron's grandson by Machir's daughter, twenty-three cities — the ink's two accounts; the judge Jair's thirty (Judges 10:4)", ['accepted'])
    if ask == 'survivors':
        move('Bava Batra 121b:9-11 (credited)', "Jair and Machir born in Jacob's days and did not die until the entry; 'about thirty-six' at Ai (Joshua 7:5 — the parser's [%d]) read as Jair alone; already old at the decree (SL.decree(set_edges) = %s)" % (THIRTY_SIX, SL_EDGES[0]))
        dat('the row jair_and_machir_survived: %s' % data['jair_and_machir_survived']['value'])
        return out("Jair and Machir born in Jacob's days and did not die until the entry — 'about thirty-six' at Ai read as Jair alone (Bava Batra 121b:9-10); already old at the decree (121b:11)", ['accepted'])
    if ask == 'nobah':
        ink('32:42', '"and Nobah went and took Kenath and its daughters, and called it Nobah after his own name" — Nobah %s (one seat as a person); Kenath %s; "its daughters" in Numbers %s; Nobah and Jogbehah together at Judges 8:11 (the words %s)' % (NOBAH, KENATH, DAUGHTERS_NUM, [w for w in words(8, 11, 'Judg') if w in ('לנבח', 'ויגבהה')]))
        return out("Nobah took Kenath and its daughters and called it Nobah after his own name (32:42) — Nobah and Jogbehah together at Judges 8:11 on Gideon's route; Kenath's other seat 1 Chronicles 2:23", ['land_possessed'])
    return out('no verdict in span', [FX.NONE])
