
# =====================================================================
# Motion 1 — THE CODE FROM THE VERSES: five cells, every clause cited (INK), every parameter a DATA row, every callee a live CALL
# =====================================================================
# ===== F1: THE CALL (Num 22:1-20) ===========================================================================
def the_call(case, data):
    q = case['ask']; P.clear()
    if q == 'last_camp':
        ink('22:1', "'and camped in the plains of Moab across the Jordan of Jericho' — the book's last camp: nine datelines to 36:13, Moses climbs from them (Deut 34:1)")
        return out('the plains of Moab — the last camp; the book never moves again (22:1; 36:13; Deut 34:1)', ['encamped_at'])
    if q == 'midian_joined':
        ink('22:4, 22:7', "'Moab said to the elders of Midian' (one seat); 'the elders of Moab and the elders of Midian' — Midian enters at 22:4 and 22:7, vanishes, returns at 25:6-18"); move('Sanhedrin 105a:13', 'never at peace before — the two dogs and the wolf')
        return out('Midian joined Moab at 22:4 and 22:7 and returns with Cozbi (25:6-18) — the thread to chapter 31 (Sanhedrin 105a:13)', [FX.NONE])
    if q == 'curse_roots':
        ink('22:6-24:9', 'arar %d, qabab %d, zaam %d — twenty tokens, no curse spoken' % (len(ARAR), len(QABAB), len(ZAAM))); dat('the row curse_roots computed')
        return out('three curse-roots, twenty tokens (arar 7, qabab 10, zaam 3) — and no curse spoken (22:12; Deut 23:6)', [FX.NONE])
    if q == 'blessing_formula':
        ink('22:6, 24:9', "'whom you bless is blessed and whom you curse is cursed' / 'those who bless you are blessed, and those who curse you are cursed'"); move('Gen 12:3 by the primeval engine (CALL)', 'the promise ladder: %s' % ', '.join(PV_LADDER)); move('Gen 27:29 by the mamre engine (CALL)', "Isaac's clauses: %s — the curse first there" % ', '.join(MM_CLAUSES))
        return out("the patriarchs' formula — Gen 12:3 blesses first (the primeval engine's ladder), Gen 27:29 curses first (the mamre engine's clauses); 24:9 returns Isaac's reversed", [FX.NONE])
    if q == 'word_formula':
        ink('22:20, 22:35, 22:38, 23:12, 23:26, 24:13', 'the six seats: %s' % data['word_formula']['value'])
        return out("the word-formula at six seats — do (22:20, akh 'only'), speak (22:35, efes 'nothing but'), speak (22:38), keep (23:12), do (23:26), speak (24:13)", ['bound_to_the_word'])
    if q == 'restrictors':
        ink('22:20, 22:35, 23:13', "akh at 22:20; efes at 22:35 and 23:13 ('only its edge')"); move('THE NUMBERS WALK 4b — 13:5 the export operator', "the restrictor class: 'only' narrows the permission to the word")
        return out("the restrictors — akh 'only' (22:20), efes 'nothing but' (22:35), efes 'only its edge' (23:13): the permission narrowed to the word", ['bound_to_the_word'])
    if q == 'way_one_wishes':
        ink('22:12, 22:20', "'you shall not go with them' then 'rise, go with them'"); move('Makkot 10b:6; Sanhedrin 105a:15', 'in the way a man wishes to go he is led; impudence effective even toward Heaven')
        return out("led in the way he wishes — 'you shall not go' (22:12) then 'rise, go' (22:20): Makkot 10b; Isa 48:17; Prov 3:34", ['cursing_barred'])
    if q == 'cursing_barred':
        ink('22:12', "'you shall not curse the people, for it is blessed' — HEAVEN's block, never closed"); ink('Deut 23:6', 'the curse turned into a blessing — the run citation (%s)' % CURSE_TURNED)
        return out("cursing barred — 'you shall not curse the people, for it is blessed' (22:12): a block never closed; Deut 23:6 the run", ['cursing_barred'])
    if q == 'refuses_spelling':
        ink('22:13-14', "'the LORD refuses' (me'en) — Pharaoh's verb (Exod 7:14, 10:3), Edom's (20:21)"); move('Kiddushin 4a:8', "'Balaam refuses' and 'my yavam refuses' (Deut 25:7) both without a yod — the yod of 'ein' expounded")
        return out("'Balaam refuses' (22:14) written without a yod — Kiddushin 4a's ground for expounding the yod elsewhere; the refusal-verb Pharaoh's", ['refused'])
    if q == 'midian_elders_left':
        ink('22:7-8', "'the elders of Moab and the elders of Midian' at 22:7; 'the princes of Moab stayed' at 22:8 — Midian's elders gone"); move('Sanhedrin 105a:14', "'if he asks the LORD he will not join us'")
        return out("Midian's elders left between 22:7 and 22:8 — the ink's delta the shelf reads (Sanhedrin 105a:14)", [FX.NONE])
    if q == 'beno_form':
        ink('24:3, 24:15, 23:18', "'his son Beor' (beno) for 'son of' — the archaic construct three times"); move('Sanhedrin 105a:9', "R. Yochanan: his father was his son in prophecy")
        return out("'his son Beor' (24:3, 24:15) — the archaic construct the shelf reads as 'his son': Balaam greater than his father (Sanhedrin 105a:9)", [FX.NONE])
    if q == 'balaam_name':
        move('Sanhedrin 105a:7', "belo am (without a nation) / bila am (wore down the nation); Beor — be'ir (bestiality)"); move('Sanhedrin 105a:8', 'Beor = Cushan-Rishathaim = Laban the Aramean')
        return out("Balaam's name expounded — without a nation / wore down the nation; his father Beor read as Laban the Aramean (Sanhedrin 105a:7-8)", [FX.NONE])
    if q == 'prophet_then_diviner':
        ink('22:7', "'divinations in their hand'"); ink('Josh 13:22', "'Balaam the diviner'"); move('Sanhedrin 106a:17', 'first a prophet, at the end a diviner')
        return out("first a prophet, at the end a diviner (Josh 13:22 — Sanhedrin 106a:17); 'divinations in their hand' at 22:7 the noun's Torah four", [FX.NONE])
    if q == 'mimmul':
        ink('22:5', "'they dwell adjacent to me [mimmuli]'"); move('Chullin 19b:14', "'adjacent to' sees the thing and is not it — the slaughter's 'adjacent to its nape' read from Balak's word")
        return out("'adjacent to me' (22:5) — the slaughter law's 'adjacent to the nape' defined from Balak's message (Chullin 19b)", [FX.NONE])
    if q == 'gentile_prophecy_by_night':
        ink('22:9, 22:20', "'and God came to Balaam' — the clause's four Bible seats: Abimelech (Gen 20:3), Laban (31:24), Balaam twice, all by night"); dat('the row gentile_prophets = %s' % data['gentile_prophets']['value'])
        return out("'God came to' — three gentiles by night (Gen 20:3, 31:24; Num 22:9, 22:20), never an Israelite in that clause", [FX.NONE])
    if q == 'house_of_silver':
        ink('22:18, 24:13', 'the clause twice with its deltas: %s' % data['house_of_silver']['value'])
        return out("'his house full of silver and gold' at 22:18 (small or great; the LORD my God) and 24:13 (good or bad; from my own heart; no 'my God')", [FX.NONE])
    if q == 'honor_promised':
        ink('22:17, 24:11', "'I will surely honor you greatly' — revoked: 'the LORD has held you back from honor'")
        return out("the honor promised at 22:17 is revoked at 24:11 in its own words — the debit closed by the revocation", ['honor_owed'])
    if q == 'embassies':
        ink('22:5-6, 22:15-17', "two embassies — 'come, curse this people for me'; 'princes more and weightier'")
        return out("two embassies (22:5-6, 22:15-17) — Balak's pleas to Balaam; the second with the honor", ['plea_made', 'honor_owed'])
    return out('no verdict in span', [FX.NONE])


# ===== F2: THE SHE-ASS AND THE ANGEL (Num 22:21-41) =======================================================
def the_ass_and_the_angel(case, data):
    q = case['ask']; P.clear()
    if q == 'saddling':
        ink('22:21-22', "'Balaam rose in the morning and saddled his she-ass' and 'his two young men with him' — Gen 22:3's verse (the parser's %s young men)" % TWO_YOUNG_MEN); move('Sanhedrin 105b:11', 'love and hatred upset the conduct of the great — Abraham and Balaam')
        return out("the Akedah's morning at Balaam's (22:21-22 = Gen 22:3): love and hatred upset the conduct of the great (Sanhedrin 105b:11)", [FX.NONE])
    if q == 'three_strikes':
        ink('22:23-27', 'the ass sees three times, Balaam strikes three times; 22:28 counts them: %s' % THREE[0])
        return out('struck three times (22:23, 22:25, 22:27) — the parser\'s 3 at 22:28 and 22:33, the plene three at 22:32', ['beaten'])
    if q == 'mouth_of_the_ass':
        ink('22:28', "'and the LORD opened the mouth of the she-ass' — the one seat"); move('Mishnah Avot 5:6', 'the mouth of the donkey the third of the ten things of twilight')
        return out('the mouth of the she-ass created at twilight — the third of the ten (Avot 5:6); opened at 22:28', ['mouth_opened'])
    if q == 'yarat':
        ink('22:32', "'the way is contrary [yarat] before me'"); move('Menachot 66b:6; Shabbat 105a:4', 'notarikon (an abbreviation reading): feared, saw, turned')
        return out("'yarat' (22:32) read as an abbreviation: the ass feared, saw, turned (Menachot 66b; Shabbat 105a)", ['adversary_in_the_way'])
    if q == 'eyes_uncovered':
        ink('22:31, 24:4, 24:16', "'the LORD uncovered Balaam's eyes' — his title afterward: 'fallen and with uncovered eyes'")
        return out("the eyes uncovered at 22:31 — Balaam's own title at 24:4 and 24:16", ['eyes_uncovered'])
    if q == 'confession':
        ink('22:34', "'I have sinned' — Pharaoh's confession (Exod 9:27, 10:16)")
        return out("'I have sinned' (22:34) — Pharaoh's confession at Balaam's mouth, the Torah's two gentile confessions", ['confessed'])
    if q == 'sword_spelling':
        ink('22:23, 22:31', "'his sword drawn' plene at the ass's seeing, defective at Balaam's")
        return out("'drawn' plene at 22:23 and defective at 22:31 — the ass's seeing and Balaam's, eight verses apart", [FX.NONE])
    if q == 'times_word':
        ink('22:28, 22:32, 22:33, 24:10', "'three TIMES' as regalim (feet) for the ass, pe'amim for the blessings — two times-words; the plene at 22:32 read %s" % PLENE)
        return out("two times-words — the ass's 'three feet' (regalim, 22:28, 22:32 plene, 22:33) and Balak's 'three times' (pe'amim, 24:10): the festivals' two words", [FX.NONE])
    if q == 'stands_stations':
        ink('22:41, 23:14, 23:28', 'the three stands: %s' % data['stands']['value']); ink('21:19-20', "Bamoth and Pisgah the well-song's last stations; 23:28 = 21:20's clause with Peor for Pisgah")
        return out("the three stands are chapter 21's last stations — Bamoth (22:41 = 21:19), Pisgah (23:14 = 21:20), Peor (23:28 = 21:20's clause): the third the god of 25:3", [FX.NONE])
    if q == 'adversary':
        ink('22:22, 22:32', "'as an adversary' — the satan-word's two Torah seats, both here")
        return out("the angel as an adversary (22:22, 22:32) — the satan-word's two Torah seats; God's anger the first of three", ['adversary_in_the_way', 'mark_of_anger'])
    if q == 'anger_mark':
        move('Zevachim 102a', "every anger leaves a mark"); ink('22:22, 24:10, 25:3', 'the three angers — the adversary, the honor revoked, the plague')
        return out("three angers, three marks — God's at Balaam (the adversary, 22:22), Balak's at Balaam (the honor revoked, 24:10), the LORD's at Israel (the plague, 25:3)", ['mark_of_anger'])
    if q == 'balaam_and_the_ass':
        dat('the row balaam_and_the_ass = %s' % data['balaam_and_the_ass']['value']); move('Sanhedrin 105a:17; Avodah Zarah 4b:2-3', "the ass's rebuke; the night service — the dispute")
        return out("a diviner by his member (Mar Zutra) / bestiality with his ass (Mar son of Ravina) — DISPUTE (Sanhedrin 105a:17)", [FX.NONE])
    if q == 'edge_of_the_people':
        ink('22:41, 23:13', "'he saw from there the edge of the people'; 'only its edge you will see'")
        return out("the edge of the people seen from Bamoth (22:41), 'only its edge' at 23:13 — the restrictor's third seat", [FX.NONE])
    return out('no verdict in span', [FX.NONE])


# ===== F3: THE THREE STANDS AND THE FOUR PARABLES (Num 23:1-24:25) ===========================================
def the_stands(case, data):
    q = case['ask']; P.clear()
    if q == 'forty_two_offerings':
        ink('23:1-2, 23:14, 23:29-30', 'seven altars three times, a bull and a ram on each — the parser\'s %s; %d altars, %d beasts' % (SEVENS[0], data['altars_total']['value'][0], data['altars_total']['value'][1])); move('Sanhedrin 105b:12; Nazir 23b:4', 'Ruth the reward of the forty-two')
        return out('twenty-one altars, forty-two beasts (7, 7, 7 × 3) — Ruth the reward (Sanhedrin 105b:12; Nazir 23b)', ['altars_built', 'offered_burnt_and_sacrifices'])
    if q == 'gentile_olah':
        dat('the row gentile_olah = %s' % data['gentile_olah']['value']); move('Zevachim 116a', "burnt offerings accepted from gentiles — Balak's and Jethro's")
        return out("Balak's burnt offerings accepted from a gentile (Zevachim 116a) — Jethro's row the exodus engine's", ['offered_burnt_and_sacrifices'])
    if q == 'most_high_knowledge':
        ink('24:16', "'and knows the knowledge of the Most High'"); move('Avodah Zarah 4b:1-4; Sanhedrin 105b:2-5; Berakhot 7a:8', "not God's thoughts (he did not know his animal's) — the moment of anger"); dat('the row moment_of_anger = %s' % data['moment_of_anger']['value'])
        return out("'knows the knowledge of the Most High' = fixes the moment of God's anger (one 58,888th of an hour) — Berakhot 7a; Avodah Zarah 4b", [FX.NONE])
    if q == 'no_anger_those_days':
        ink('23:8', "'how shall I curse whom El has not cursed'"); move('Avodah Zarah 4b:5; Berakhot 7a:13; Sanhedrin 105b:6-7', 'God was not angry all those days — Micah 6:5')
        return out("no anger in Balaam's days — 'how shall I curse whom El has not cursed' (23:8); Micah 6:5 'know the righteous acts'", ['oracle_blessed'])
    if q == 'moment_of_anger':
        dat('the row moment_of_anger: the measure Berakhot 7a:8, the hour Sanhedrin 105b:8, the cause 105b:10')
        return out("God's anger a moment daily — the first three hours, when the kings crown themselves to the sun and the rooster's crest whitens (Sanhedrin 105b:8-10)", [FX.NONE])
    if q == 'death_of_the_upright':
        ink('23:10, 24:14', "'let me die the death of the upright' / 'I go to my people'"); move('Sanhedrin 105a:12; Avodah Zarah 25a:1', "his own sign; the book of Yashar = Genesis, the book of the upright patriarchs")
        return out("'the death of the upright' — the patriarchs' (the book of Yashar, Avodah Zarah 25a); Balaam's sign for himself, 'I go to my people' the other arm (Sanhedrin 105a:12)", [FX.NONE])
    if q == 'balaam_share':
        dat('the row balaam_share = %s' % data['balaam_share']['value']); move('Mishnah Sanhedrin 10:2; Jerusalem Talmud Sanhedrin 10:2:1-2', 'the four commoners; all invented new sins')
        return out('no share in the world to come — Balaam among the four commoners (Mishnah Sanhedrin 10:2)', [FX.NONE])
    if q == 'gentile_share':
        dat('the row gentile_share = %s' % data['gentile_share']['value']); move('Sanhedrin 105a:10-11', "R. Yehoshua against R. Eliezer on Ps 9:18")
        return out("gentiles who fear God have a share — R. Yehoshua's, the mishnah's opinion (Sanhedrin 105a:11); Balaam alone excluded", [FX.NONE])
    if q == 'balaam_disciples':
        dat('the row balaam_disciples = %s' % (data['balaam_disciples']['value'],)); move('Pirkei Avot 5:19', "an evil eye, a haughty spirit, a limitless appetite")
        return out("Balaam's disciples — an evil eye, a haughty spirit, a limitless appetite — inherit Gehinnom (Avot 5:19)", [FX.NONE])
    if q == 'curses_turned':
        ink('24:5-7', "the clauses — tents, dwellings, streams, gardens, aloes, cedars, buckets, many waters, Agag, exalted"); move('Sanhedrin 105b:17-19', "R. Yochanan's table; R. Abba bar Kahana: all reverted but the synagogues — Deut 23:6 'the curse' singular")
        return out("each clause of 24:5-7 the curse he intended (Sanhedrin 105b:17-18); all reverted but the synagogues — Deut 23:6's singular 'curse' (105b:19)", ['oracle_blessed'])
    if q == 'reed_and_cedar':
        ink('24:6', "'as cedars beside the waters'"); move('Taanit 20a:15; Sanhedrin 105b:20-106a:2', "Ahijah's reed-curse better than Balaam's cedar-blessing")
        return out("the cedar-blessing worse than Ahijah's reed-curse — the reed bends and yields the quill; the cedar falls to the south wind (Taanit 20a; Sanhedrin 105b-106a)", [FX.NONE])
    if q == 'shema_candidate':
        ink('24:9', "'he couched, he lay down like a lion... who shall rouse him'"); move('Berakhot 12b:15-16', "the Sages sought to fix Balak's portion in the Shema for 24:9's lying down and rising; not for the Exodus mention")
        return out("Balak's portion nearly fixed in the Shema — for 24:9's 'lay down... rouse him' (Berakhot 12b:16), not for 23:22's Exodus (12b:15)", [FX.NONE])
    if q == 'tents_doors':
        ink('24:2', "'he saw Israel dwelling by its tribes'"); move('Bava Batra 60a:5', "the entrances not aligned — the privacy rule's source")
        return out("the tents' doors not aligned — 'dwelling by its tribes' (24:2) the source that one may not open an entrance opposite another's (Bava Batra 60a)", ['spirit_rested'])
    if q == 'tents_aloes':
        ink('24:5-6', "'your tents' (ohalekha) and 'like aloes' (ahalim) — one consonantal skin"); move('Berakhot 16a:1', 'tents juxtaposed to streams — read ohalim')
        return out("the tents and the aloes one skin (24:5-6) — Berakhot 16a reads the aloes as tents of Torah beside the purifying streams", [FX.NONE])
    if q == 'motzi_tense':
        ink('23:22', "'El who brought them out [motziam] of Egypt'"); move('Berakhot 38a:14', "Rava: motzi is past — the bread blessing's word argued from it")
        return out("'motzi' past tense from 23:22 — the bread blessing's 'who brings forth' argued from Balaam's verse (Berakhot 38a)", [FX.NONE])
    if q == 'blood_of_the_slain':
        ink('23:24', "'and drinks the blood of the slain'"); move('Chullin 35b:14; Keritot 22a:14; Niddah 19b:10, 55b:21', 'blood after death a liquid that renders susceptible; the spurting blood excluded; the wound\'s blood too')
        return out("'the blood of the slain' (23:24) — the blood that flows at death is the liquid that renders food susceptible; not the spurting blood; a wound's blood too (Chullin 35b; Keritot 22a; Niddah 19b, 55b)", [FX.NONE])
    if q == 'fourth_part':
        ink('23:10', "'the fourth part [rova] of Israel' — the quarter's consonants, Reba's, the bestiality-verb's (the reading BK23A-04)"); move('Niddah 31a:20', "R. Abbahu: God counts the couplings")
        return out("'the fourth part of Israel' read as the couplings God counts (Niddah 31a:20) — the homograph the reading told by the points", [FX.NONE])
    if q == 'opened_eye':
        ink('24:3', "'the man of the opened eye'"); move('Sanhedrin 105a:16; Niddah 31a:21', 'blind in one eye — the other blinded for objecting'); dat('the row balaam_blind = %s' % data['balaam_blind']['value'])
        return out("blind in one eye — 'the man of the opened eye' (24:3): Sanhedrin 105a:16; Niddah 31a:21 the reason", [FX.NONE])
    if q == 'shefi':
        ink('23:3', "'he went limping [shefi]' — the bare height, Onkelos 'alone'"); move('Sanhedrin 105a:16; Sotah 10a:9', 'lame in one leg; Samson in both')
        return out("lame in one leg — 'shefi' (23:3): Sanhedrin 105a:16 (the reading's 'bare height', Onkelos's 'alone')", [FX.NONE])
    if q == 'teruah_of_a_king':
        ink('23:21', "'the teruah of a king is among him' — the teruah-word's Torah seven; Onkelos the Shekhinah"); move('Rosh Hashanah 32b:11-15', "a Kingship verse of the Torah's three; with shofarot too (R. Yosei) / Kingship alone (R. Yehuda)"); dat('the row teruah_verse_class = %s' % data['teruah_verse_class']['value'])
        return out("23:21 one of the Torah's three Kingship verses (with Deut 33:5, Exod 15:18); recited with the shofarot too (R. Yosei) — DISPUTE (Rosh Hashanah 32b)", [FX.NONE])
    if q == 'no_divination':
        ink('23:23', "'no divination in Jacob and no sorcery in Israel' — the serpent's word in the diviner's mouth"); move('Nedarim 32a:12-13', 'the plain sense kept; one who does not divine is brought within the partition')
        return out("'no divination in Jacob' (23:23) — the plain sense kept against Rebbi's reading; the non-diviner brought within the partition (Nedarim 32a)", [FX.NONE])
    if q == 'dwells_alone':
        ink('23:9', "'a people that dwells alone and is not reckoned among the nations' — the leper's two words (Lev 13:46)"); move('Sanhedrin 39b:1', "where a verse says 'the nations', Israel is not included")
        return out("'not reckoned among the nations' (23:9) — the definition rule: 'the nations' excludes Israel (Sanhedrin 39b)", [FX.NONE])
    if q == 'kabbo_curse':
        ink('23:8', "'how shall I curse [ekkov] whom El has not cursed [kabbo]'"); move('Sanhedrin 56a:6, 92a:1; Sotah 41b:13', "nokev / kov = cursing — the blasphemer's verb and Proverbs' defined from Balaam's")
        return out("the qabab-root's definition seat — 'kabbo' = a curse (23:8): the blasphemer's 'nokev' read from it (Sanhedrin 56a; lev24's first call)", [FX.NONE])
    if q == 'eitan':
        ink('24:21', "'firm [eitan] is your dwelling, and your nest set in the sela' — Meribah's rock-word"); move('Rosh Hashanah 11a:8; Sotah 46b:1', 'eitan = mighty (the patriarchs as mountains) / hard / old')
        return out("'eitan' (24:21) = mighty (Rosh Hashanah 11a), hard as a rock or old (Sotah 46b) — the Kenite's nest in the sela, sitting 6's rock-word", [FX.NONE])
    if q == 'who_shall_live':
        ink('24:23', "'alas, who shall live when El appoints this'"); move('Sanhedrin 106a:5', "Reish Lakish: woe to him who lives in God's name; R. Yochanan: woe to the nation hindering the redemption")
        return out("'who shall live when El appoints this' (24:23) — two readings: the indulgent in God's name; the nation between the lion and the lioness (Sanhedrin 106a:5)", [FX.NONE])
    if q == 'kittim':
        ink('24:24', "'ships from the hand of Kittim... afflict Asshur and afflict Eber' — Daniel 11:30 quotes; Onkelos the Romans"); move('Sanhedrin 106a:6', "Rav: the Roman legion against Assyria — kill, then enslave")
        return out("Kittim's ships = the Roman legion (Sanhedrin 106a:6; Onkelos 'the Romans'); Daniel 11:30 the quotation", [FX.NONE])
    if q == 'counsel_inverted':
        ink('24:14', "'what this people will do to your people' — the reverse expected"); move('Sanhedrin 106a:7', 'he curses himself obliquely')
        return out("'what this people will do to your people' (24:14) — the inverted clause: Balaam curses himself obliquely (Sanhedrin 106a:7)", ['counsel_given'])
    if q == 'counsel':
        ink('24:14, 31:16, 25:18', "'come, I will counsel you' — 'in the matter of Peor' %d times, 'by the word of Balaam' at 31:16" % PEOR_MATTER); move('Sifrei Bamidbar 131:1', "R. Akiva's adjacency to 25:1 against Rebbi — the ink's own back-reference at 31:16")
        return out("the counsel (24:14) named as Peor's cause by the ink at 31:16 ('by the word of Balaam... in the matter of Peor'); the Sifrei's adjacency dispute beside it", ['counsel_given'])
    if q == 'star_reading':
        ink('24:17', "'a star steps forth from Jacob and a scepter rises from Israel' — Judah's scepter (Gen 49:10); Onkelos a KING and the MESSIAH"); dat('the row star_reading = %s' % data['star_reading']['value']); move('Jerusalem Talmud Taanit 4:5:13', "R. Akiva: Koziba out of Jacob — this is King Messiah; R. Yochanan ben Torta: grass will grow from your jaws")
        return out("the star applied to bar Koziba by R. Akiva and refused by R. Yochanan ben Torta (Jerusalem Talmud Taanit 4:5) — Onkelos's KING and MESSIAH the translation's text", [FX.NONE])
    if q == 'word_in_mouth_mode':
        ink('23:5, 23:16', "'the LORD put a word in Balaam's mouth' — Deut 18:18's prophet-clause"); dat('the row word_in_mouth_mode = %s' % data['word_in_mouth_mode']['value']); move('Sanhedrin 105b:16', 'an angel from his mouth / a hook in his mouth')
        return out("a word put in his mouth (23:5, 23:16) — an angel spoke from it (R. Elazar) / a hook held it (R. Yonatan): DISPUTE (Sanhedrin 105b:16)", ['word_put_in_mouth'])
    if q == 'judah_blessing':
        ink('24:9', "'he crouched, lay down like a lion and like a lioness — who will rouse him' = Gen 49:9 with two words exchanged (shakhav for ravatz, ari for aryeh)"); move("Gen 49:9 by the family engine (CALL)", "the lion's six names — %d of them here" % FM_LIONS)
        return out("Jacob's blessing of Judah in Balaam's mouth (24:9 = Gen 49:9 but two words) — the family engine's lion (two of the six names)", ['oracle_blessed'])
    if q == 'isaac_formula':
        ink('24:9', "'those who bless you are blessed, and those who curse you are cursed' — Gen 27:29 reversed (the curse first there)"); move('Gen 27:29 by the mamre engine (CALL)', "Isaac's six clauses, the last 'cursers_cursed'")
        return out("Isaac's formula reversed at 24:9 — Gen 27:29 curses first (the mamre engine's clauses), Balaam blesses first", ['oracle_blessed'])
    if q == 'promise_ladder':
        move('Gen 12:3 by the primeval engine (CALL)', "the ladder: %s" % ', '.join(PV_LADDER))
        return out("the promise ladder of Gen 12:2-3 — 'bless your blessers, curse your curser' — the formula's first seat (the primeval engine)", [FX.NONE])
    if q == 'one_letter':
        ink('23:22, 24:8', "'El brings THEM out of Egypt' / 'El brings HIM out' — one letter (a mem for a vav)")
        return out("23:22 -> 24:8 with one letter changed — 'brings them out' to 'brings him out'", [FX.NONE])
    if q == 'parables':
        ink('23:7, 23:18, 24:3, 24:15, 24:20, 24:21, 24:23', "'he took up his parable' seven times — 21:27's parable-tellers' word"); move('cold_run_chukat (CALL)', 'the parable-tellers: %s' % CK_TELLERS)
        return out("seven parables taken up — the parable-tellers' word of 21:27 (chukat's row PAID: Balaam and Beor the tellers, Chullin 60b)", ['oracle_blessed'])
    return out('no verdict in span', [FX.NONE])
