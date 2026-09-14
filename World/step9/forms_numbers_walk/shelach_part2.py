
# =====================================================================
# Motion 2 — THE DATA: the parameter rows (the tradition's own vocabulary; the running setting first)
# =====================================================================
DATA = {
    'hebron_visitor': {'value': 'Caleb alone', 'settings': {'Caleb alone': "Rava (Sotah 34b:7) — 'HE came to Hebron': Caleb separated from the counsel and prostrated himself on the graves of the forefathers", 'they came': "the plain plural of the verse's other verbs"}, 'source': "13:22 — the singular verb the ink's, the visitor the shelf's"},
    'hebron_before_zoan': {'value': 'seven times more fertile', 'settings': {'seven times more fertile': "Sotah 34b:11; Ketubot 112a:8 — 'built' cannot be literal: Canaan is Ham's youngest", 'seven years earlier': "the plain reading"}, 'source': "13:22 'built seven years before Zoan' — the parser's seven"},
    'cluster_bearers': {'value': 8, 'settings': {'8': "Sotah 34a:9 (the baraita continued) — the cluster on two poles, eight men; one the pomegranates, one the figs; Joshua and Caleb carried nothing", '4': "the first reading of 'on a pole between two' — two poles, four men (34a:9)"}, 'source': "13:23 — the parser's [1, 2]"},
    'cluster_weight': {'value': 480, 'settings': {'480': "Sotah 34a:9 — four hundred and eighty seah, from the bearers' count"}, 'source': "the shelf's arithmetic on the bearers"},
    'return_day': {'value': (2, 5, 9), 'settings': {'(2, 5, 9)': "Taanit 29a:5 — the baraita: sent on the twenty-ninth of Sivan, returned 'at the end of forty days' on the Ninth of Av; Mishnah Ta'anit 4:6 the decree's day; Sotah 35a:11 the eve; 29a:7 that night"}, 'source': "13:25 — the tape's reading-placed marker"},
    'tammuz_length': {'value': 29, 'settings': {'29': "the modeled alternation (calendar_parameters month_rounding) — the running setting: the forty-day timer fires at (2, 5, 10)", '30': "Abaye (Taanit 29a:6) — 'Tammuz of that year was made full', Lam 1:15: the fortieth day the ninth itself"}, 'source': "the calendar registry's row tammuz_length; CF2"},
    'the_ten_trials': {'value': 10, 'settings': {'10': "Arakhin 15a-b (R. Yehuda's list): two at the sea, two at the water, two at the manna, two at the quail, the calf, the spies; Pirkei Avot 5:4 the answer sheet"}, 'source': "14:22 'these ten times' — the parser's ten; the ledger's tested_the_lord count graded at CF6"},
    'congregation': {'value': 10, 'settings': {'10': "Mishnah Sanhedrin 1:6; Berakhot 21b:5; Megillah 23b:8; Sanhedrin 74b:3 — the twelve less Joshua and Caleb"}, 'source': "14:27 'this evil congregation'"},
    'deaths_ceased': {'value': (40, 5, 15), 'settings': {'(40, 5, 15)': "Bava Batra 121a:9 (Rav Nachman); Taanit 30b:12 (R. Yochanan) — the fifteenth of Av the day the dying in the wilderness ceased; Deut 2:16-17 the speech resumed"}, 'source': "the decree's timer due (40, 5, 9) six days before it"},
    'wilderness_share': {'value': 'no share', 'settings': {'no share': "R. Akiva (Mishnah Sanhedrin 10:3; Sanhedrin 110b:2) — 'in this wilderness they shall be consumed, and there they shall die'; Ps 95:11", 'a share': "R. Eliezer — Ps 50:5 'gather My pious to Me'; R. Yehoshua ben Korcha (Tosefta Sanhedrin 13:1)"}, 'source': "14:35"},
    'spies_share': {'value': 'no share', 'settings': {'no share': "Mishnah Sanhedrin 10:3; Sanhedrin 108a:2, 109b:10 — 'died' this world, 'by plague' the next"}, 'source': "14:37"},
    'spies_death_mode': {'value': 'the tongue to the navel', 'settings': {'the tongue to the navel': "R. Sheila of Kefar Temarta (Sotah 35a:13) — the tongue stretched to the navel, worms between", 'diphtheria': "Rav Nachman bar Yitzchak (35a:13)"}, 'source': "14:37 'by the plague before the LORD' — an unusual death (Reish Lakish)"},
    'count_from': {'value': 'the exodus', 'settings': {'the exodus': "Deut 2:14's thirty-eight from Kadesh-barnea to Zered — the forty includes the two years elapsed (40 − 38 = 2 = the era's year at the decree)", 'the decree': "the plain forty from 14:34's own day — (42, 5, 9)"}, 'source': "14:33-34 against Deut 2:14 (the retelling's ink)"},
    'hin_in_logs': {'value': 12, 'settings': {'12': "Mishnah Menachot 9:2 — the hin vessel twelve logs; the half six, the third four, the quarter three (R. Shimon: no hin vessel, the gradations)"}, 'source': "the table's fractions of the hin"},
    'libation_floors': {'value': [3, 4, 6], 'settings': {'[3, 4, 6]': "Mishnah Menachot 12:4, 13:5; Menachot 104a:10-11, 107a:11-12 — three, four, six logs and beyond, never one, two or five: the lamb's, the ram's, the bull's"}, 'source': "15:13 'all the home-born shall do these' with 28:14's 'shall be'"},
    'oil_donation': {'value': 'wine only', 'settings': {'wine only': "R. Akiva (Mishnah Menachot 12:5) — oil never comes alone with its obligation", 'oil too': "R. Tarfon; Rabbi three logs from 15:13 (Menachot 107a:17; Zevachim 91b:10), the Rabbis one log"}, 'source': "15:13"},
    'libations_from': {'value': 'the entry', 'settings': {'the entry': "Zevachim 111a:7 — 'when you come into the land': the libations began at the entry, on the great public altar; none in the wilderness", 'inheritance and settlement': "R. Yishmael (Kiddushin 37b:1) — where coming AND dwelling are written"}, 'source': "15:2 'when you come into the land of your dwellings' — the cell's own gate"},
    'altar_eras': {'value': 'wilderness forbidden; Gilgal permitted; Shiloh forbidden; Nov and Gibeon permitted; Jerusalem forbidden forever', 'settings': {'wilderness forbidden; Gilgal permitted; Shiloh forbidden; Nov and Gibeon permitted; Jerusalem forbidden forever': "Mishnah Zevachim 14:4-8 — the high places' eras; 14:10 the private altar's omissions"}, 'source': "the altar the libations are poured on (Zevachim 111a)"},
    'which_take_libations': {'value': 'all but the firstborn, the tithe, the Passover, the sin offering and the guilt offering; the leper\'s chatat and asham do', 'settings': {"all but the firstborn, the tithe, the Passover, the sin offering and the guilt offering; the leper's chatat and asham do": "Mishnah Menachot 9:6; Menachot 90b:6-91a:27 — the baraita on 15:3-5 (the vow, the gift, the festivals; the festival goats excluded at 15:8; the leper's three from 'the burnt offering or the sacrifice, for the one lamb')"}, 'source': "15:3-5, 15:8"},
    'lamb_and_ram_ages': {'value': 'lambs to a year; rams from thirteen months and a day', 'settings': {'lambs to a year; rams from thirteen months and a day': "Mishnah Parah 1:3 — day to day; the thirteen-month animal the palges, invalid as either; its libation a ram's (Chullin 23a:6)"}, 'source': "15:5-6, 15:11 'the one lamb', 'the one ram'"},
    'gentile_libations': {'value': 'the public pays', 'settings': {'the public pays': "Mishnah Shekalim 7:6 (R. Shimon's ordinance) — a gentile's olah from abroad without money for its libations: from the treasury; no independent libations for a gentile (Menachot 73b:14; Zevachim 45a:14; Temurah 3a:10)"}, 'source': "15:11, 15:13"},
    'convert_offering': {'value': 'a beast olah, or a bird pair both olot', 'settings': {'a beast olah, or a bird pair both olot': "Keritot 8b:18-9a:4 — as you entered the covenant (Exod 24:5); the bird burnt offering wholly for the LORD; Rabbi: circumcision, immersion, the sprinkling of blood; Mishnah Kinnim 1:1 vows all olot", 'a quarter-dinar today': "Keritot 9a:10 — set aside for the pair; R. Shimon annulled it"}, 'source': "15:14-16"},
    'convert_congregation': {'value': 'congregation', 'settings': {'congregation': "R. Yehuda (Kiddushin 73a:4) — 'as for the congregation, one statute for you and for the stranger'", 'not congregation': "R. Yosei — 'one statute' interrupts"}, 'source': "15:15"},
    'challah_measure': {'value': {'householder': Fraction(1, 24), 'baker': Fraction(1, 48)}, 'settings': {"{'householder': 1/24, 'baker': 1/48}": "Mishnah Challah 2:7 — one twenty-fourth for oneself or a banquet; one forty-eighth for the baker and the market; impure unwittingly 1/48, intentionally 1/24"}, 'source': "15:20 — no measure in the ink"},
    'challah_minimum': {'value': 'five quarters of a kav', 'settings': {'five quarters of a kav': "Mishnah Challah 2:6; Shabbat 15a:3; Tosefta Eduyot 1:1 — Shammai a kav, Hillel two, the Sages a kav and a half = the wilderness omer (Exod 16:36 'a tenth of the ephah'), recalculated five quarters (R. Yosei: and a bit more)"}, 'source': "15:20 'your dough' — the omer (Menachot 67a:6)"},
    'terumah_measure': {'value': {'generous': Fraction(1, 40), 'average': Fraction(1, 50), 'stingy': Fraction(1, 60)}, 'settings': {"{'generous': 1/40, 'average': 1/50, 'stingy': 1/60}": "Mishnah Terumot 4:3 (Beit Shammai 1/30) — the terumah's measure has no ink floor; 4:4 the messenger's average"}, 'source': "15:20 'as the terumah of the threshing floor' — Numbers 18's terumah, OWED to Korach's compile"},
    'outside_produce': {'value': 'in liable; out exempt', 'settings': {'in liable; out exempt': "Mishnah Challah 2:1 — R. Akiva: taken out exempt", 'in liable; out liable': "R. Eliezer"}, 'source': "15:18 'the land'"},
    'territories': {'value': 'the land to Chezib one; to the river and Amanah two; beyond two, the measures reversed', 'settings': {'the land to Chezib one; to the river and Amanah two; beyond two, the measures reversed': "Mishnah Challah 4:8 (Rabban Gamliel) — one for the fire, one for the priest; 4:7 Syria's two"}, 'source': "15:21 'throughout your generations' — outside the land by the rabbis' word"},
    'challah_today': {'value': 'rabbinic', 'settings': {'rabbinic': "Ketubot 25a:11; Niddah 47a:7 — 'when you come' = the coming of all of you; Ezra's return partial"}, 'source': "15:18-19"},
    'tribe_table': {'value': 'a bull and a goat (R. Meir)', 'settings': {'a bull and a goat (R. Meir)': "Mishnah Horayot 1:5 — the court's; carried in the chatat engine (court({'sin': 'idolatry'}))", 'twelve (R. Yehuda)': "each tribe a congregation — twelve bulls and twelve goats", 'thirteen (R. Shimon)': "the tribes and the court"}, 'source': "15:24 — the chatat engine's row by CALL"},
    'idolatry_principle': {'value': 'one sin offering', 'settings': {'one sin offering': "Mishnah Shabbat 7:1's analogue (Shabbat 68b-69a) — one who forgot the principle of idolatry brings one", 'prior knowledge required': "Munbaz (Shabbat 68b:6) — the unwitting juxtaposed to the intentional at 15:29-30"}, 'source': "15:22-31"},
    'karet_reading': {'value': 'this world and the next', 'settings': {'this world and the next': "R. Akiva (Sanhedrin 64b:21, 90b:18) — 'cut off' this world, 'shall be cut off' the World-to-Come", 'the language of men': "R. Yishmael (64b:22) — the doubling teaches nothing; 15:30's 'venikhreta' this world, 15:31's the next", 'before and after Yom Kippur': "Rabbi (Shevuot 13a:2) — the day does not atone for the high-handed"}, 'source': "15:31 'cut off, shall be cut off' — MIDDOT.md's governance row"},
    'despiser': {'value': 'who says the Torah is not from Heaven', 'settings': {'who says the Torah is not from Heaven': "Sanhedrin 99a:17 (the baraita)", 'the Epicurean': "99a:17 alternatively", 'who uncovers faces in the Torah': "Shevuot 13a:2 (Rabbi); Pirkei Avot 3:11 (R. Elazar of Modiin)", 'Manasseh': "Sanhedrin 99b:4 — the exemplar"}, 'source': "15:31 'despised the word of the LORD'"},
    'yoke': {'value': 'the yoke, the covenant, the faces', 'settings': {'the yoke, the covenant, the faces': "Shevuot 13a:2 — 'despised the word' = throws off the yoke, uncovers faces; 'breached His commandment' = circumcision; Pirkei Avot 3:11's five"}, 'source': "15:31"},
    'blasphemer_offering': {'value': 'none', 'settings': {'none': "the Rabbis (Mishnah Keritot 1:2; Keritot 2a:5, 7a:23) — 'one law for him who DOES': no act, no sin offering", 'an offering': "R. Akiva (Keritot 7b:1) — the karet written in the offering's passage"}, 'source': "15:29-30"},
    'blasphemer_identity': {'value': 'the curser of the Name', 'settings': {'the curser of the Name': "the Rabbis (Keritot 7b:6); Isi ben Yehuda (7b:4); Pesachim 93b:1 with Lev 24:15", 'the idolater': "R. Elazar ben Azarya (Keritot 7b:6); Sifrei 112:1"}, 'source': "15:30 'blasphemes the LORD'"},
    'owner_piggul': {'value': 'the performer only', 'settings': {'the performer only': "the mishna (Zevachim 47a)", 'the owner too': "R. Elazar son of R. Yosei (Zevachim 47a:3) — 'he who sacrifices shall sacrifice his offering'"}, 'source': "15:4"},
    'idolatry_goat_semikhah': {'value': 'no laying of hands', 'settings': {'no laying of hands': "Mishnah Menachot 9:7 — the communal offerings save the court's bull and the scapegoat", 'laying of hands': "R. Shimon (Menachot 92a:2) — the idolatry goat too"}, 'source': "15:24"},
    'anointed_idolatry_trigger': {'value': 'an erroneous ruling with an unwitting act', 'settings': {'an erroneous ruling with an unwitting act': "Mishnah Horayot 2:1-3 — the anointed like the court", 'an unwitting act alone': "Rabbi (Horayot 7b:19) — 'when he sins unwittingly'"}, 'source': "15:27-28"},
}
assert all('value' in r and 'settings' in r and 'source' in r for r in DATA.values())
print('DATA rows: %d' % len(DATA))


# =====================================================================
# Motion 1 — THE FUNCTION, compiled from the ink (F1-F7)
# =====================================================================
# ===== F1: THE SPIES (Num 13:1-33) ==========================================================================
def spies(case, data):
    del P[:]
    ask = case['ask']
    if ask == 'send_for_yourself':
        ink('13:2', '"send FOR YOURSELF men" — the sending Moses\' own; Deut 1:22-23 the people\'s asking, "good in my eyes"'); move('Sotah 34b:3 (Reish Lakish)', 'at your discretion, not a divine command')
        return out("at Moses' discretion — 'for yourself' (Reish Lakish); the people's asking (Deut 1:22)", [FX.NONE])
    if ask == 'one_per_tribe':
        ink('13:2', '"one man, one man for his fathers\' tribe... every one a prince" — the parser\'s [1, 1] the distributive'); ink('13:4-15', 'twelve tribe-lines computed: %s; Levi absent' % SPY_TRIBES)
        return out('12 — one man per tribe, princes; Levi absent', [FX.NONE])
    if ask == 'fourth_order':
        ink('13:4-15', 'the tribes in the spies\' order: %s — a fourth order of the twelve (1:5-15, 2:3-31, 7:12-83 the others); Joseph named over Manasseh at 13:11' % SPY_TRIBES)
        return out('a fourth order of the twelve — Reuben, Simeon, Judah, Issachar, Ephraim, Benjamin, Zebulun, Manasseh under Joseph, Dan, Asher, Naphtali, Gad', [FX.NONE])
    if ask == 'joshua_name':
        ink('13:16', '"and Moses called Hoshea son of Nun Joshua" — the new name at %d seats BEFORE this verse (%s); Hoshea again at Deut 32:44' % (len(JOSHUA_BEFORE), ', '.join('%s %d:%d' % s for s in JOSHUA_BEFORE)))
        move('Sotah 34b:8', 'the name a prayer — the LORD will save you from the spies\' counsel'); move('Tosefta Berakhot 1:15', 'Hoshea again in his praise: the same man before and after')
        return out('Hoshea to Joshua at 13:16 — the new name at 8 seats before it, the old at Deut 32:44 (the same man)', [FX.NONE])
    if ask == 'questionnaire':
        ink('13:18-20', 'the seven interrogatives computed: %s — strong or weak, few or many, good or bad, camps or fortresses, fat or lean, trees or none' % QUESTIONS)
        return out('7 questions — strong or weak, few or many, good or bad, camps or fortresses, fat or lean, trees or none; and the fruit', [FX.NONE])
    if ask == 'report_answers':
        ink('13:27-29', 'the report answers the questionnaire: fat (milk and honey, the fruit), strong (the people fierce, the Anak), fortified (the cities great), the map (Amalek south; the Hittite, Jebusite, Amorite in the mountain; the Canaanite by the sea and the Jordan)')
        return out('the report answers: fat; strong; fortified; the Anak; the map — Amalek south, the mountain peoples, the Canaanite by the sea and the Jordan', [FX.NONE])
    if ask == 'hebron_visitor':
        ink('13:22', '"they went up by the south, and HE came to Hebron" — the singular verb between plurals'); dat('the row hebron_visitor = %s' % data['hebron_visitor']['value'])
        return out("Caleb alone at the graves (Rava, Sotah 34b:7) — the singular verb the ink's", [FX.NONE])
    if ask == 'hebron_zoan':
        ink('13:22', '"Hebron was built seven years before Zoan of Egypt" — the parser\'s %s' % SEVEN); dat('the row hebron_before_zoan = %s' % data['hebron_before_zoan']['value']); move('Sotah 34b:11; Ketubot 112a:8', 'Canaan Ham\'s youngest — seven times more fertile')
        return out('7 — built seven years before Zoan: sevenfold fertility (Sotah 34b:11; Ketubot 112a)', [FX.NONE])
    if ask == 'cluster':
        ink('13:23', '"they carried it on a pole between two" — the parser\'s %s (the dual)' % POLE); dat('the rows cluster_bearers = %s, cluster_weight = %s' % (data['cluster_bearers']['value'], data['cluster_weight']['value']))
        return out('on a pole between two — two poles, eight bearers (Sotah 34a); 480 seah', [FX.NONE])
    if ask == 'eshcol':
        ink('13:24', '"that place he called the wadi of Eshcol because of the cluster" — named after its use; Deut 1:24')
        return out('named after the cluster (13:24); Deut 1:24', [FX.NONE])
    if ask == 'forty_days':
        ink('13:25', '"at the end of forty days" — %s; 14:34 a day for a year' % FORTY)
        return out('40 days (13:25) — the timer; a day for a year (14:34)', [FX.NONE])
    if ask == 'going_like_coming':
        ink('13:25-26', '"and they went and came"'); move('Sotah 35a:1 (R. Shimon ben Yochai)', 'the going likened to the coming — with wicked counsel')
        return out('the going with wicked counsel like the coming (R. Shimon ben Yochai, Sotah 35a:1)', [FX.NONE])
    if ask == 'report_form':
        ink('13:27-28', 'the praise first ("flowing with milk and honey"), then "but the people are strong"'); move('Sotah 35a:2 (R. Meir)', 'a slander that does not begin with truth does not stand')
        return out('truth first, then the slander — a slander that does not begin with truth does not stand (R. Meir)', ['evil_report_spread'])
    if ask == 'caleb_hushed':
        ink('13:30', '"and Caleb hushed the people toward Moses" — "we shall surely go up", two doubled infinitives'); move('Sotah 35a:3-6 (Rabba)', 'persuaded them — the ruse: is this the only thing the son of Amram did to us?')
        return out('persuaded them (Rabba) — the ruse: is this the only thing the son of Amram did?', ['plea_made'])
    if ask == 'stronger_than':
        ink('13:31', '"for they are stronger than us" — the same letters read "than Him"'); move('Sotah 35a:7; Arakhin 15a:12 (R. Chanina bar Pappa)', 'the revocalization — heresy: the Owner cannot remove His vessels (M-16\'s class)')
        return out("stronger than us, read stronger than Him — heresy (R. Chanina bar Pappa; M-16's class)", [FX.NONE])
    if ask == 'punished_for':
        ink('14:37', '"those who brought out the evil report of the land died" — the report named, not the blasphemy'); move('Arakhin 15a:13 (Rabba / Reish Lakish)', 'punished for the evil report')
        return out('the evil report (14:37), not the blasphemy — Rabba / Reish Lakish', [FX.NONE])
    if ask == 'slander_sealed':
        ink('14:22', '"tried Me these ten times" — the sentence at the spies\' speech'); move('Arakhin 15a:6; Mishnah Arakhin 3:5', 'the sentence sealed by the malicious speech — speech severer than deeds')
        return out('the sentence sealed by the evil report — speech severer than deeds (Mishnah Arakhin 3:5)', ['evil_report_spread'])
    if ask == 'consumes_inhabitants':
        ink('13:32', '"a land that eats its inhabitants"'); move('Sotah 35a:8 (Rava)', 'the deaths for their own good — the mourning hid them; Job\'s eulogy (some say)')
        return out("the deaths for their good — the mourning that hid them (Rava); Job's eulogy (some say)", [FX.NONE])
    if ask == 'grasshoppers':
        ink('13:33', '"we were in our own eyes as grasshoppers, and so we were in their eyes"'); move('Sotah 35a:9 (Rav Mesharshiyya)', 'liars — in their eyes unknowable')
        return out('liars — "in their eyes" unknowable (Rav Mesharshiyya)', [FX.NONE])
    if ask == 'job':
        ink('13:20', '"whether there are trees (eitz) in it"'); move('Bava Batra 15a:14 (Rava)', 'Job (Utz) in the spies\' days')
        return out("Job in the spies' days — trees / Utz (Rava, Bava Batra 15a)", [FX.NONE])
    if ask == 'joshua_caleb_equal':
        ink('13:6, 13:8', 'Caleb named first (Judah), Joshua after (Ephraim) — the list\'s order'); move('Tosefta Keritot 4:7 (R. Shimon)', 'Joshua preceded Caleb everywhere but here — equal')
        return out('equal — Caleb first at 13:6, Joshua at 13:8 (Tosefta Keritot 4:7)', [FX.NONE])
    if ask == 'named_after_deeds':
        ink('13:13-14', 'Sethur son of Michael; Nahbi son of Vophsi'); move('Sotah 34b:5-6 (R. Yitzchak; R. Yochanan)', 'named after their deeds — hid, weakened; concealed, stomped')
        return out('Sethur son of Michael — hid the acts, weakened Him; Nahbi son of Vophsi (R. Yitzchak; R. Yochanan)', [FX.NONE])
    if ask == 'giants':
        ink('13:22', 'Ahiman, Sheshai and Talmai, the children of Anak — Sheshai a name, not the ordinal (the parser\'s %s)' % SHESHAI); move('Sotah 34b:9-10; Yoma 10a:6', 'the skilled, the pits, the furrows; the sun a necklace')
        return out('Ahiman the skilled, Sheshai the pits, Talmai the furrows; the sun a necklace (Sotah 34b:9-10; Yoma 10a)', [FX.NONE])
    raise KeyError(ask)


# ===== F2: THE DECREE (Num 14:1-45) =========================================================================
def decree(case, data):
    del P[:]
    ask = case['ask']
    if ask == 'that_night':
        ink('14:1', '"and the people wept that night"'); dat('the row return_day = %s' % (data['return_day']['value'],)); move('Taanit 29a:7; Sotah 35a:11; Sanhedrin 104b:4', 'the night of the Ninth of Av — a weeping for generations; Mishnah Ta\'anit 4:6 the decree\'s day')
        return out("the night of the Ninth of Av — a weeping for generations (Taanit 29a:7; Sotah 35a:11; Sanhedrin 104b:4); Mishnah Ta'anit 4:6", ['wept'])
    if ask == 'ten_trials':
        ink('14:22', '"tried Me these ten times" — the parser\'s %s' % TEN); dat('the row the_ten_trials = %s' % data['the_ten_trials']['value']); move('Arakhin 15a-b; Pirkei Avot 5:4', 'the ten trials — the spies the tenth')
        return out("10 — 'these ten times' (14:22; Pirkei Avot 5:4); the ledger's count graded at CF6", [FX.NONE])
    if ask == 'now_ten':
        ink('14:22', '"NOW ten times" — the extra word'); move('Arakhin 15a:10 (Reish Lakish)', 'sealed for THIS sin')
        return out('sealed for THIS sin — "now" (Reish Lakish, Arakhin 15a:10)', [FX.NONE])
    if ask == 'congregation':
        ink('14:27', '"this evil congregation" — twelve spies less Joshua and Caleb = %d' % (len(TRIBE_LINES) - 2)); dat('the row congregation = %s' % data['congregation']['value']); move('Mishnah Sanhedrin 1:6; Berakhot 21b:5; Megillah 23b:8; Sanhedrin 74b:3', 'a congregation is ten')
        return out('10 — the twelve less Joshua and Caleb (Mishnah Sanhedrin 1:6; Berakhot 21b; Megillah 23b; Sanhedrin 74b)', [FX.NONE])
    if ask == 'set':
        ink('14:29', '"all your counted by all your number, from twenty years old and upward" — the census formula (the parser\'s %s)' % TWENTY); move('Bava Batra 121b:8 (Rav Hamnuna)', 'Levi outside — counted from thirty'); dat('Bamidbar\'s total CALLED: %d' % BM.TOTAL)
        return out('%d — the census set by CALL: from twenty and upward, all your counted; Levi outside (Bava Batra 121b:8); not over sixty (121b:11)' % BM.TOTAL, ['sentence_pronounced'])
    if ask == 'set_edges':
        ink('14:29', '"and upward" — the valuations\' "and upward" (Lev 27:7)'); move('Bava Batra 121b:11 (Rav Acha bar Yaakov)', 'the verbal analogy: over sixty outside as under twenty — Yair son of Manasseh; 121b:8 Rav Hamnuna: Levi from thirty')
        return out('under twenty and over sixty outside — "and upward" / "and upward" with the valuations (Rav Acha bar Yaakov); Levi from thirty (Rav Hamnuna)', [FX.NONE])
    if ask == 'exceptions':
        ink('14:24, 14:30', '"save Caleb son of Jephunneh and Joshua son of Nun"'); ink('14:31', '"your little ones... I will bring in"')
        return out('Caleb and Joshua (14:24, 14:30); the children brought in (14:31)', ['exempt'])
    if ask == 'day_for_year':
        ink('14:34', '"forty days, a day for a year, a day for a year... forty years" — the parser\'s %s; Ezek 4:6 verbatim' % DAY_YEAR)
        return out('[40, 40] — forty days, a day for a year, a day for a year (14:34; Ezek 4:6 verbatim)', [FX.NONE])
    if ask == 'count_from':
        ink('14:33-34', 'forty years — %s; Deut 2:14 thirty-eight from Kadesh-barnea to Zered' % FORTY_YEARS); dat('the row count_from = %s' % data['count_from']['value']); ink('the Calendar', 'the era\'s year at the decree = %d; 40 − 38 = %d' % (_EX.year(RETURN_DAY), 40 - 38))
        return out("40 - 38 = 2 — the era's year at the decree: the forty from the exodus (Deut 2:14's thirty-eight from Kadesh)", [FX.NONE])
    if ask == 'due':
        ink('the Calendar', 'the decree\'s day (2, 5, 9) + 38 years = %s' % (_EX.date(DUE_38),)); dat('the row deaths_ceased = %s' % (data['deaths_ceased']['value'],))
        return out('(40, 5, 9) — the ninth of Av of the fortieth year, by the Calendar; PENDING on the tape (CF3)', ['carcasses_fall_in_the_wilderness'])
    if ask == 'deaths_ceased':
        dat('the row deaths_ceased = %s' % (data['deaths_ceased']['value'],)); move('Bava Batra 121a:9 (Rav Nachman); Taanit 30b:12 (R. Yochanan)', 'the fifteenth of Av — the dying ceased; Deut 2:16-17 the speech resumed')
        return out('the fifteenth of Av of the fortieth year — the dying ceased; the speech resumed (Bava Batra 121a:9; Taanit 30b:12; Deut 2:16-17)', [FX.NONE])
    if ask == 'wilderness_share':
        ink('14:35', '"in this wilderness they shall be consumed, and there they shall die" — the four seats of "this wilderness": %s' % THIS_WILDERNESS); dat('the row wilderness_share = %s' % data['wilderness_share']['value'])
        return out('no share (R. Akiva — "there they shall die"); a share (R. Eliezer — Ps 50:5)', [FX.NONE])
    if ask == 'spies_share':
        ink('14:37', '"died... by plague"'); dat('the row spies_share = %s' % data['spies_share']['value'])
        return out('no share — "died... by plague" (Mishnah Sanhedrin 10:3)', [FX.NONE])
    if ask == 'spies_death_mode':
        ink('14:37', '"died by the plague before the LORD" — an unusual death'); dat('the row spies_death_mode = %s' % data['spies_death_mode']['value'])
        return out('the tongue to the navel with worms (R. Sheila); diphtheria (Rav Nachman bar Yitzchak)', ['put_to_death'])
    if ask == 'spies_portions':
        ink('14:38', '"Joshua and Caleb LIVED of those men" — 26:65 already says they survived'); move('Bava Batra 118b:3 (Ulla)', 'lived IN the ten\'s portions of the land')
        return out("Joshua and Caleb lived in the ten's portions — 'lived' (Ulla, Bava Batra 118b)", [FX.NONE])
    if ask == 'pardon':
        ink('14:20', '"I have pardoned according to your word" — once in the Bible (%d)' % ONCE['סלחתי']); move('Berakhot 32a:29 (R. Yochanan; the school of R. Yishmael)', 'God conceded to Moses; according to your word — so it will be')
        return out('"I have pardoned according to your word" — God conceded (R. Yochanan); so it will be (the school of R. Yishmael)', ['pardoned'])
    if ask == 'plea':
        ink('14:17-18', '"as You have spoken, saying: the LORD, long of anger" — the attributes quoted back'); move('Sanhedrin 111b:1', 'long of anger even for the wicked — as You said')
        return out('the attributes quoted back — "as You have spoken": long of anger even for the wicked (Sanhedrin 111b:1)', [FX.NONE])
    if ask == 'attributes_deleted':
        ink('14:18 against Exod 34:6-7', 'a subsequence — %d words of %d kept, %d dropped, none added; Onkelos restores "and sins" from its own Exod 34:7' % (len(N18), len(E34), len(E34) - len(N18)))
        return out('a subsequence of Exod 34:6-7 — eleven words dropped, none added; Onkelos restores "and sins"', [FX.NONE])
    if ask == 'offer_second_seat':
        ink('14:12', '"I will make of you a greater nation" — Exod 32:10 the first seat, Deut 9:14 the retelling (M-23)')
        return out("the offer's second seat — Exod 32:10 / Num 14:12 / Deut 9:14 (M-23)", [FX.NONE])
    if ask == 'egypt_will_hear':
        ink('14:13', '"then Egypt will hear" — Exod 32:12 "why should Egypt say" at the calf')
        return out("Moses' Egypt argument at both intercessions (Exod 32:12; Num 14:13)", [FX.NONE])
    if ask == 'ability':
        ink('14:16', '"from lack of the ABILITY of the LORD" — the feminine noun'); move('Berakhot 32a:27', 'yekholet, not yakhol — the nations\' saying')
        return out('the ability — yekholet, the feminine noun (Berakhot 32a:27)', [FX.NONE])
    if ask == 'as_i_live':
        ink('14:21', '"as I live, and all the earth shall be filled with the glory of the LORD"'); move('Berakhot 32a:31 (Rava / Rav Yitzchak)', 'you have given Me life with your words')
        return out('"you have given Me life with your words" (Rava / Rav Yitzchak)', [FX.NONE])
    if ask == 'upon_children':
        ink('14:18', '"visiting the iniquity of the fathers upon the children"'); move('Berakhot 7a; Sanhedrin 27b', 'when they hold their fathers\' deeds')
        return out("when they hold their fathers' deeds (Berakhot 7a; Sanhedrin 27b)", [FX.NONE])
    if ask == 'caleb_entitlement':
        ink('14:24', '"him I will bring into the land where he went, and his seed shall possess it"'); ink('Josh 14:6-14', 'forty years, forty-five, eighty-five; "Moses swore that day" — the oath Numbers never wrote; Hebron given')
        return out('holding_owed — Hebron; PAID at Josh 14:13-14 (forty-five years; eighty-five; Moses swore that day)', ['holding_owed'])
    if ask == 'turn_back':
        ink('14:25', '"tomorrow turn and journey into the wilderness by the way of the Red Sea" — the run Num 21:4 by the same phrase; Deut 2:1')
        return out('tomorrow turn — by the way of the Red Sea: OPEN, its run Num 21:4 / Deut 2:1', ['commanded'])
    if ask == 'presumption':
        ink('14:44', '"they presumed to go up... the ark and Moses did not depart"'); move('Shabbat 97a:1 (R. Yehuda ben Beteira)', 'Zelophehad among them — the daughters\' father')
        return out('presumed — the ark and Moses stayed; Zelophehad among them (R. Yehuda ben Beteira, Shabbat 97a)', ['presumed_to_go_up'])
    if ask == 'hormah':
        ink('14:45', '"beat them down to Hormah" — the name at 21:3 ("and he called the name of the place Hormah"), six chapters later; Judg 1:17 the second naming')
        return out('Hormah — named at 21:3, used at 14:45: THE PROLEPTIC NAME (the registry row carries both); Judg 1:17', ['defeated'])
    if ask == 'fell_and_rent':
        ink('14:5-6', '"Moses and Aaron fell on their faces"; "Joshua and Caleb... rent their garments"'); move('Taanit 14b:13 (R. Elazar)', 'the worthy fall on their faces; their students rend')
        return out('Moses and Aaron fell on their faces; Joshua and Caleb rent garments (Taanit 14b)', [FX.NONE])
    if ask == 'stones_upward':
        ink('14:10', '"to stone them with stones; and the glory of the LORD appeared"'); move('Sotah 35a:12 (R. Chiyya bar Abba)', 'the stones thrown upward, as at God')
        return out('stones thrown upward, as at God (R. Chiyya bar Abba)', [FX.NONE])
    if ask == 'ninth_of_av_reading':
        ink('14:11 / 14:27', '"how long will this people provoke Me" / "this evil congregation"'); move('Megillah 31b:2', 'the Ninth of Av\'s Torah reading — R. Natan bar Yosef; Abaye: today Deut 4:25')
        return out('the Ninth of Av\'s Torah reading — "how long will this people provoke Me" (R. Natan bar Yosef); today Deut 4:25 (Abaye)', [FX.NONE])
    if ask == 'joshua_childless':
        ink('14:6', '"Joshua son of Nun" — 1 Chr 7:27 "Nun his son, Joshua his son", no children named'); move('Pesachim 119b:6', 'no son')
        return out('no son — "Joshua son of Nun" and 1 Chr 7:27 (Pesachim 119b)', [FX.NONE])
    raise KeyError(ask)
