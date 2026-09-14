

# ===== F4: THE MARCH AND THE ARK (Num 10:11-36) ==============================================================
def march(case, data):
    del P[:]
    ask = case['ask']
    if ask == 'date':
        ink('10:11', '"in the second year, in the second month, on the twentieth of the month" — ordinals %s, the day %s' % (DATE_ORD, DATE))
        move('Rosh Hashanah 3a:5; Taanit 29a:2', 'Nisan and Iyar in one year — the year does not turn in Iyar; the day-stack opens')
        return out('(2, 2, 20) — the twentieth of Iyar, year two; the year does not turn in Iyar', ['arrayed_by_banners'])
    if ask == 'order':
        v = BM.camp({'ask': 'march'}, BM.DATA)[0]
        ink('10:14-27', 'the twelve princes in the camp\'s order a third time — computed %s' % (ORDER_10 == ORDER_2))
        move('cold_run_bamidbar.camp(march) -> %r [IMPORT]' % (v,), 'the order at its home — Judah, Reuben, the tent, Ephraim, Dan')
        return out(v, ['arrayed_by_banners'])
    if ask == 'levites_places':
        ink('10:17, 10:21', '"the tabernacle was taken down, and the sons of Gershon and the sons of Merari journeyed, bearing the tabernacle"; "the Kohathites journeyed, bearing the sanctuary, and they set up the tabernacle before their coming"')
        return out('Gershon and Merari after Judah bearing the tabernacle; Kohath after Reuben bearing the sanctuary — set up before their coming', ['charge_kept'])
    if ask == 'ark_bearers':
        ink('10:21', '"the Kohathites journeyed, the bearers of the sanctuary" — two plurals'); move('Menachot 98b:3', 'two bearers each — four')
        return out('four bearers (two plurals)', ['charge_kept'])
    if ask == 'sanctuary_name':
        ink('10:21', '"the bearers of the SANCTUARY"'); move('Shevuot 16b:4 against Eruvin 2a:14', '10:21\'s "sanctuary" is the ark and the vessels; the Tabernacle is called Sanctuary from Exod 25:8-9')
        return out("10:21's sanctuary is the ark and the vessels; the Tabernacle's name from Exod 25:8", ['charge_kept'])
    if ask == 'princes_order':
        ink('2:3-31 = 7:12-83 = 10:14-27', 'the twelve in one order at three chapters — computed: %s' % (ORDER_10 == ORDER_2 == NAMES))
        return out('the camp\'s order a third time — 2 = 7 = 10', ['arrayed_by_banners'])
    if ask == 'three_days':
        ink('10:33', '"three days\' journey" twice — %s' % THREE_DAYS); move('Taanit 29a:3 (R. Chama b. Chanina); Shabbat 116a:3', 'that very day they turned from after the LORD — the first punishment; the three days on the tape a TIMER, its fire the reading-placed marker at 11:1')
        return out("three days' journey — the timer; that very day they turned (the first punishment)", ['journey_of_three_days'])
    if ask == 'spy_verb':
        ink('10:33', '"to spy out (latur) for them a resting place" — the spies\' verb of chapters 13-14 (eight seats)')
        return out("the ark's verb is the spies' verb — eight seats", ['journey_of_three_days'])
    if ask == 'clouds':
        dat('the row seven_clouds = %s' % data['seven_clouds']['value']); ink('10:34', '"the cloud of the LORD was over them by day"'); move('Sifrei Bamidbar 83:1', 'seven clouds — four sides, above, below, one before; thirteen, four, two the other counts')
        return out('seven clouds (Sifrei); 13 / 4 / 2 the other settings', ['arrayed_by_banners'])
    if ask == 'shekhinah_minimum':
        dat('the row shekhinah_minimum = %s' % data['shekhinah_minimum']['value']); ink('10:36', '"the myriads of the thousands of Israel" — no numeral on the ink (%s)' % N('Num', 10, 36))
        move('Bava Kamma 83a:7; Yevamot 64a', 'two myriads and two thousands — the plurals\' minimum: the Presence rests on no fewer')
        return out('22,000 — the plurals\' minimum (the shelf\'s datum; no numeral on the ink)', ['arrayed_by_banners'])
    if ask == 'eighty_five':
        ink('10:35-36', 'the section\'s letters computed: %d' % LETTERS_3536); move('Mishnah Yadayim 3:5; Shabbat 115b:4', 'a scroll with eighty-five letters defiles the hands; without them it is not rescued from a fire')
        return out('85 letters — the measure of a scroll (Mishnah Yadayim 3:5)', ['arrayed_by_banners'])
    if ask == 'signs':
        ink('10:34 / 10:36', 'the two inverted nuns as marks on the DB (sitting 3)'); move('Shabbat 115b-116a; Sifrei 84:1', 'Rebbi: a book in itself; R. Shimon b. Gamliel: to separate the two punishments, to be written in the portion of the flags')
        return out('a book in itself (Rebbi) / to separate the two punishments (R. Shimon b. Gamliel)', ['arrayed_by_banners'])
    if ask == 'hobab':
        ink('10:29-32', '"we are journeying... come with us"; "I will not go"; "leave us not, I pray... you shall be to us for eyes"'); move('Sifrei Bamidbar 78:3, 81:1; Judg 1:16, 4:11', 'the three readings of "we are journeying"; the answer not in the ink — the Kenites went')
        return out('asked, refused, asked again — the answer not in the ink (Judg 1:16)', ['plea_made'])
    if ask == 'jethro_at_sinai':
        dat('the row jethro_at_sinai = %s' % data['jethro_at_sinai']['value']); move('Zevachim 116a', 'before the giving (R. Yehoshua) / after (R. Elazar HaModai)')
        return out('before the giving (R. Yehoshua); after (R. Elazar HaModai)', ['plea_made'])
    if ask == 'day_stack':
        dat('the row spies_sent_day = %s' % data['spies_sent_day']['value'])
        move('Taanit 29a:2-5; Seder Olam Rabbah 8:2', '(2, 2, 20) the march; + 3 days = the twenty-third; the month of meat ends the twenty-second of Sivan; Hazeroth with the seven until the twenty-ninth; the spies sent that day')
        return out('the march (2, 2, 20); the three days to the twenty-third; Hazeroth on the twenty-second of Sivan; Paran on the twenty-ninth', ['arrayed_by_banners'])
    if ask == 'year_turns':
        move('Rosh Hashanah 3a:5', '40:17\'s "second year" and 10:11\'s "second year" — Nisan and Iyar in one year')
        return out('not in Iyar — Nisan and Iyar in one year', ['arrayed_by_banners'])
    if ask == 'cloud_and_trumpets':
        ink('9:23 and 10:2', '"by the word of the LORD they journeyed" AND the trumpets for the journeying'); move('Sifrei Bamidbar 72:1, 84:5', 'two verses both kept — the cloud\'s word and the priests\' blast')
        return out('both kept — the cloud and the trumpets', ['arrayed_by_banners'])
    return out('no verdict in span', [FX.NONE])


# ===== F5: TABERAH, THE LUST AND THE QUAIL (Num 11:1-15, 11:31-35) ==========================================
def taberah_and_quail(case, data):
    del P[:]
    ask = case['ask']
    if ask == 'the_people':
        ink('11:1', '"the people were as murmurers"'); move('Sifrei Bamidbar 85:1', '"the people" everywhere the wicked, "My people" the upright — a lexical rule with proof-seats')
        return out("'the people' the wicked, 'My people' the upright", ['fire_sank'])
    if ask == 'fire_at_edge':
        dat('the row fire_at_the_edge = %s' % data['fire_at_the_edge']['value']); ink('11:1', '"consumed at the edge of the camp"'); move('Sifrei 85:1 (R. Shimon b. Menassia the other arm)', 'the proselytes cast to the edge / the officers')
        return out('the proselytes at the edge (Sifrei); the officers (R. Shimon b. Menassia)', ['fire_sank'])
    if ask == 'fire_sank':
        ink('11:2', '"Moses prayed to the LORD, and the fire sank"'); move('Berakhot 32a:5', '"to the LORD" read "onto the LORD" — Moses spoke impertinently (R. Elazar)')
        return out("sank at Moses' prayer", ['fire_sank'])
    if ask == 'taberah_name':
        ink('11:3', '"he called the name of that place Taberah, for the fire of the LORD burned among them"'); move('Sifrei 86:1; Deut 9:22', 'the name by the event — "because"')
        return out('named by the event — Taberah (Deut 9:22)', ['fire_sank'])
    if ask == 'rabble':
        ink('11:4', '"the rabble that was among them lusted a lust"'); move('Onkelos 11:4; Exod 12:38', 'the mixed multitude')
        return out('the mixed multitude', ['lusted'])
    if ask == 'five_foods':
        dat('the row five_foods = %s' % data['five_foods']['value']); ink('11:5', 'the cucumbers, the melons, the leeks, the onions, the garlic — one seat each'); move('Yoma 75a:10', 'the manna gave every taste but these five (one arm); every taste and texture but these five\'s texture (the other)')
        return out('the manna tasted like all but these five (R. Ami / R. Asi)', ['lusted'])
    if ask == 'fish_for_nothing':
        dat('the row fish_for_nothing = %s' % data['fish_for_nothing']['value']); move('Yoma 75a:6 (Rav / Shmuel)', '"for nothing" — the forbidden relations; "which we ate" — fish')
        return out("the forbidden relations ('for nothing'); fish ('which we ate')", ['lusted'])
    if ask == 'families_weeping':
        ink('11:10', '"weeping by its families"'); move('Yoma 75a:9; Shabbat 130a:13', 'over the forbidden relations newly barred — a mitzvah accepted with contention')
        return out('the forbidden relations', ['lusted'])
    if ask == 'manna_taste':
        ink('11:8 with Exod 16:31', '"the taste of a cake baked with oil" / "wafers in honey" — two seats'); move('Yoma 75b:5 (R. Yosei b. R. Chanina)', 'bread for the youth, oil for the elderly, honey for the children')
        return out('by age — bread, oil, honey', ['lusted'])
    if ask == 'manna_fell':
        move('Yoma 75a:16', '11:9 "fell on it", Exod 16:4 "go out and gather", 11:8 "went about" — by rank: at the door, outside the camp, far off')
        return out('by rank — the righteous at their doors, the average outside the camp, the wicked far off', ['lusted'])
    if ask == 'manna_form':
        move('Yoma 75a:17', '"bread", "cakes", "ground it" — baked, cakes, raw by rank')
        return out('by rank — baked, cakes, raw', ['lusted'])
    if ask == 'dew':
        move('Yoma 75b:9', 'Exod 16:14 over it, 11:9 under it — dew above and below')
        return out('dew above and dew below', ['lusted'])
    if ask == 'manna_taste_word':
        dat('the row manna_taste_word = %s' % data['manna_taste_word']['value']); move('Yoma 75a:20', 'shad = breast (R. Abbahu) / shed = demon')
        return out('breast (R. Abbahu) / demon', ['lusted'])
    if ask == 'day_ladder':
        ink('11:19-20', '"not one day, nor two days, nor five days, nor ten days, nor twenty days — until a month of days" — the parser: %s' % DAY_LADDER)
        return out('1, 2, 5, 10, 20 — then a month', ['flesh_for_a_month'])
    if ask == 'month_of_days':
        dat('the row month_of_days = %s' % data['month_of_days']['value']); move('Chagigah 17b:7; Megillah 5a:11', 'a month of DAYS — thirty, counted by days, no hours')
        return out('thirty days, counted by days, no hours', ['flesh_for_a_month'])
    if ask == 'six_hundred_thousand':
        ink('11:21', '"six hundred thousand on foot" — %s; the exodus\' "about" dropped' % SIX_HUNDRED)
        return out('600000 on foot', ['lusted'])
    if ask == 'shortened_hand':
        ink('11:23', '"is the hand of the LORD shortened?" — with Isa 50:2, 59:1'); move('Onkelos 11:23', '"the Word held back"')
        return out('not shortened — three seats', ['flesh_for_a_month'])
    if ask == 'nursing_father':
        ink('11:12', '"as a nursing-father carries the sucking child"'); move('Sanhedrin 8a:6', 'the judge bears the community\'s burden to this degree')
        return out("the judge's burden measured by Moses' clause", ['lusted'])
    if ask == 'wilderness_meat':
        dat('the row wilderness_meat = %s' % data['wilderness_meat']['value']); move('Chullin 17a:6', 'R. Yishmael: the meat of stabbing forbidden — "slaughtered" literal; R. Akiva: their stabbing was their slaughter')
        return out('slaughter (R. Yishmael); stabbing (R. Akiva)', ['lusted'])
    if ask == 'quail_height':
        ink('11:31', '"about two cubits above the face of the earth" — the dual: %s' % TWO_CUBITS); move('Yoma 75b; Arakhin 15b:3', 'the second quail among the ten trials')
        return out('2 cubits', ['lusted'])
    if ask == 'quail_slaughter':
        ink('11:32', '"gathered the quail"'); move('Chullin 27b:8-9', 'the fish\'s "gathering" is written beside the flocks\' slaughter — birds\' is not: birds need slaughter')
        return out("birds need slaughter — the quail's 'gathered' no exemption", ['lusted'])
    if ask == 'ten_homers':
        ink('11:32', '"he who gathered least gathered ten homers" — %s (Joseph\'s "ten asses" by consonants)' % TEN_HOMERS)
        return out('10 homers the least', ['lusted'])
    if ask == 'meat_between_teeth':
        ink('11:33', '"while the meat was yet between their teeth"'); move('Chullin 105a:8 (Rav Chisda)', 'meat between the teeth is still meat — no cheese until removed')
        return out('still meat — no cheese until removed', ['lusted'])
    if ask == 'two_timers':
        ink('11:33 against 11:19-20', '"between their teeth, before it was chewed" / "a whole month"'); move('Yoma 75b:2; Sifrei Bamidbar 94:1', 'the average died at once, the wicked after a month — one plague, two timers')
        return out('the average at once (11:33), the wicked after a month (11:20) — one plague, two timers', ['put_to_death'])
    if ask == 'graves':
        ink('11:34', '"Kibroth-hattaavah, for there they buried the people that lusted" — plene here, defective at 33:16 and Deut 9:22'); move('Sifrei 98:1', 'the name by the event')
        return out('Kibroth-hattaavah — the graves of lust', ['buried'])
    if ask == 'trials':
        move('Arakhin 15b:3; Pirkei Avot 5:4', 'the quail the second quail-trial among the ten — "these ten times" (Num 14:22)')
        return out('the quail among the ten trials', ['lusted'])
    if ask == 'three_gifts':
        move('Taanit 9a', 'the well by Miriam, the cloud by Aaron, the manna by Moses')
        return out('the well, the cloud, the manna — three gifts by three shepherds', ['lusted'])
    if ask == 'spread_or_slaughtered':
        dat('the row spread_or_slaughtered = %s' % data['spread_or_slaughtered']['value']); move('Yoma 75b:3', 'Reish Lakish: read "slaughtered"; R. Yehoshua b. Korcha: birds needing slaughter; Rebbi: Psalm 78:27')
        return out("spread (the ink); 'slaughtered' by Reish Lakish's re-reading", ['lusted'])
    return out('no verdict in span', [FX.NONE])


# ===== F6: THE SEVENTY AND THE TWO (Num 11:16-30) ===========================================================
def seventy_elders(case, data):
    del P[:]
    ask = case['ask']
    if ask == 'sanhedrin':
        dat('the row sanhedrin_size = %s' % data['sanhedrin_size']['value']); ink('11:16', '"seventy men of the elders" — %s' % SEVENTY); move('Mishnah Sanhedrin 1:6; Sanhedrin 2a:13, 17a:1-2', 'seventy-one with Moses (the Sages); seventy (R. Yehuda)')
        return out('71 (the Sages); 70 (R. Yehuda)', ['appointed_to_serve'])
    if ask == 'lots':
        dat('the row lots_mechanism = %s; Bamidbar\'s the_lots = %s' % (data['lots_mechanism']['value'], BM.DATA['the_lots']['value']))
        ink('11:26', '"among the written"'); move('cold_run_bamidbar.DATA[the_lots] [IMPORT]; Sanhedrin 17a:4-5', 'seventy-two ballots, seventy by lot from a box — the 273\'s mechanism')
        return out('72 ballots, 70 by lot — the box of the 273', ['appointed_to_serve'])
    if ask == 'with_you':
        ink('11:16-17', '"they shall stand there WITH YOU"; "bear the burden WITH YOU"'); move('Horayot 4b:14; Kiddushin 76b:6; Sanhedrin 36b:4, 36b:10, 17a:1-2', 'four readings — counted with them; fit to rule; whole in body; of fit lineage')
        return out('counted with them / fit to rule / whole in body / of fit lineage', ['appointed_to_serve'])
    if ask == 'elder_means':
        ink('11:16', '"whom you know to be the elders of the people"'); move('Kiddushin 32b:8 (R. Yosei HaGelili)', 'an elder is a sage — one who has acquired wisdom')
        return out('a sage — not merely the aged', ['appointed_to_serve'])
    if ask == 'count_when':
        move('Sanhedrin 3b:16', 'from the time of gathering there must be seventy')
        return out('at the gathering', ['appointed_to_serve'])
    if ask == 'spirit':
        ink('11:17, 11:25', '"I will set apart of the spirit that is on you"'); move('Sifrei Bamidbar 93:1; Onkelos 11:17', 'Moses\' lamp undiminished — "make greater"')
        return out("set apart — Moses' spirit undiminished", ['spirit_rested'])
    if ask == 'continued':
        dat('the row continued = %s' % data['continued']['value']); ink('11:25 / 11:27', '"they prophesied and did not continue" / "are prophesying" — the participle'); move('Sanhedrin 17a:12-13; Onkelos 11:25 "did not cease"', 'the seventy stopped, Eldad and Medad did not — the spine\'s two arms settled by the participle')
        return out('the seventy stopped, the two did not', ['spirit_rested'])
    if ask == 'eldad_medad_prophecy':
        dat('the row eldad_medad_prophecy = %s' % data['eldad_medad_prophecy']['value']); move('Sanhedrin 17a:10', 'Moses dies and Joshua brings them in / the quail / Gog and Magog')
        return out('Moses dies and Joshua brings them in; the quail; Gog and Magog — three settings', ['spirit_rested'])
    if ask == 'restrain_them':
        dat('the row restrain_them = %s' % data['restrain_them']['value']); ink('11:28', '"my lord Moses, restrain them"'); move('Sifrei 96:1; Sanhedrin 17a:14', 'lay the public burden on them / imprison them')
        return out('lay the public burden on them (Sifrei); imprison them (Sanhedrin 17a)', ['spirit_rested'])
    if ask == 'joshua_childless':
        move('Eruvin 63a:26 (R. Levi)', 'whoever answers before his teacher goes childless — Joshua')
        return out('answered before his teacher — childless', ['spirit_rested'])
    if ask == 'descents':
        dat('the row descents = %s' % data['descents']['value']); ink('11:17, 11:25, 12:5', '"I will come down"; "the LORD came down" — eleven going-down tokens in the Torah (the reading)'); move('Sifrei Bamidbar 93:1', '"ten descents are written" — the shelf\'s count, the list not on this shelf')
        return out("eleven on the ink against the Sifrei's ten — DIVERGE by one, open", ['spirit_rested'])
    if ask == 'would_that':
        ink('11:29', '"would that all the LORD\'s people were prophets"'); move('Sanhedrin 17a:15', 'fits the two other readings of their prophecy')
        return out("would that all the LORD's people were prophets", ['spirit_rested'])
    return out('no verdict in span', [FX.NONE])


# ===== F7: MIRIAM (Num 12:1-16) =============================================================================
def miriam(case, data):
    del P[:]
    ask = case['ask']
    if ask == 'who_first':
        ink('12:1', '"and Miriam SPOKE, and Aaron" — the feminine singular verb before two subjects: %s' % MIRIAM_FIRST); move('Sifrei Bamidbar 99:1', 'Miriam spoke first — the grammar')
        return out('Miriam first — the feminine singular verb', ['evil_speech_spoken'])
    if ask == 'dibbur':
        move('Sifrei Bamidbar 99:1', 'dibbur harsh, amirah imploring — a lexical rule with proof-seats')
        return out('harsh speech (dibbur)', ['evil_speech_spoken'])
    if ask == 'cushite':
        ink('12:1', '"the Cushite woman... a Cushite woman" — with the article, then without'); move('Moed Katan 16b:19; Sifrei 99:1', 'Zipporah is her name — distinguished by her deeds; beautiful')
        return out('distinguished by her deeds (Zipporah) — beautiful', ['evil_speech_spoken'])
    if ask == 'separation':
        ink('12:8', '"mouth to mouth I speak with him"'); move('Shabbat 87a:4', 'Moses separated from his wife by his own a-fortiori and God agreed — one of three things')
        return out("Moses' own a-fortiori, agreed to by God", ['evil_speech_spoken'])
    if ask == 'suddenly':
        ink('12:4', '"the LORD spoke suddenly" — three Torah seats with 6:9\'s'); move('Keritot 9a:19', '"suddenly" = beyond one\'s control')
        return out('beyond control — the three seats', ['evil_speech_spoken'])
    if ask == 'summons':
        ink('12:5', '"and He called Aaron and Miriam, and the two of them came out" — the order reversed; %s' % N('Num', 12, 5))
        return out('Aaron and Miriam — the summons reversed; the two came out', ['evil_speech_spoken'])
    if ask == 'dreams':
        ink('12:6-8', '"in a vision... in a dream"; "mouth to mouth, and not in riddles"'); move('Yevamot 49b; Berakhot 55b:14', 'the prophets through a dim glass, Moses through a clear one; a good dream not false')
        return out('the prophets in dreams; Moses mouth to mouth, not in riddles', ['evil_speech_spoken'])
    if ask == 'likeness':
        ink('12:8', '"the likeness of the LORD he beholds" — the word\'s eight Torah seats computed: %d (seven bans, one beholding)' % len(LIKENESS)); move('Berakhot 7a:32', 'the reward of the hidden face at the bush')
        return out('seven bans on making one, one beholding (12:8)', ['evil_speech_spoken'])
    if ask == 'aaron_struck':
        dat('the row aaron_struck = %s' % data['aaron_struck']['value']); ink('12:9-10', '"His anger burned against THEM"; "Aaron turned"'); move('Shabbat 97a:2-3', 'R. Akiva: Aaron too; R. Yehuda b. Beteira: either way you will answer for it')
        return out('not struck (R. Yehuda b. Beteira); struck and healed (R. Akiva)', ['stricken_with_leprosy'])
    if ask == 'as_snow':
        ink('12:10', '"leprous as snow" — Moses\' hand (Exod 4:6), Miriam, Gehazi (2 Kgs 5:27)')
        return out("Moses' hand, Miriam, Gehazi — leprous as snow", ['stricken_with_leprosy'])
    if ask == 'who_declared':
        dat('the row who_declared_miriam = %s' % data['who_declared_miriam']['value']); move('Zevachim 101b:19-102a; Mishnah Negaim 2:5, 3:1', 'not Moses the non-priest, not Aaron her kin — the Holy One Himself (or Moses as a priest in the installation week)')
        return out('the Holy One Himself; Moses as a priest in the installation week (Rav); not Aaron her kin', ['stricken_with_leprosy'])
    if ask == 'kin_rule':
        move('Mishnah Negaim 2:5 (R. Meir); 3:1', 'not his own, not his relatives\'; only a priest declares')
        return out("not his own, not his relatives' (R. Meir); only a priest declares", ['stricken_with_leprosy'])
    if ask == 'short_prayer':
        dat('the row short_prayer_bounds = %s' % data['short_prayer_bounds']['value']); ink('12:13', '"God, heal her, please" — %d words, %d letters, two "please"' % (len(PRAYER), sum(len(w) for w in PRAYER)))
        move('Berakhot 34a:12; Mishnah Berakhot 5:5', 'no briefer than Moses; fluency the sign of acceptance')
        return out('five words, the floor; forty days the ceiling; fluency the sign', ['healed'])
    if ask == 'dayo':
        dat('the row dayo = %s' % data['dayo']['value']); ink('12:14', '"if her father had but spit in her face, would she not be ashamed seven days?" — %s' % SEVEN_SEVEN)
        move('Bava Kamma 25a:3, 25a:8; Bava Batra 111a:5; Zevachim 69b:6; Mishnah Bava Kamma 2:5', 'fourteen by the a-fortiori; DAYO — seven: Torah law, general (12:15\'s second verse)')
        return out('7 of 14 — dayo is Torah law', ['confined_seven_days'])
    if ask == 'admonition_days':
        move('Moed Katan 16a:20', 'admonition no less than seven days — an allusion from Miriam')
        return out('seven days — admonition', ['confined_seven_days'])
    if ask == 'quarantine':
        d = NG.days(1)
        ink('12:14-15', '"let her be shut out of the camp seven days" — the leper\'s verb; %s' % SEVEN); move('cold_run_negaim.days(1) -> %r [IMPORT]; Lev 13:4' % (d,), 'the leper\'s week — the negaim engine\'s confinement')
        return out('shut out seven days — the leper\'s week (7)', ['confined_seven_days'])
    if ask == 'grade':
        v = NG.standing_verdict('skin')
        ink('12:10', '"leprous as snow" — the confirmed grade'); move('Yevamot 103b:16; cold_run_negaim.standing_verdict(skin) -> %r [IMPORT]' % (v,), 'the CONFIRMED leper is as one dead — not the quarantined')
        return out('confirmed — as one dead (the confirmed leper only)', ['stricken_with_leprosy'])
    if ask == 'as_one_dead':
        ink('12:12', '"let her not be as one dead"'); move('Nedarim 64b:6; Avodah Zarah 5a:19; Chullin 7b:12; Sanhedrin 47a:10', 'four are as dead — the pauper, the leper, the blind, the childless')
        return out('the leper among the four as dead', ['stricken_with_leprosy'])
    if ask == 'measure_for_measure':
        ink('12:15', '"the people did not journey until Miriam was gathered in"'); move('Mishnah Sotah 1:7, 1:9; Sotah 9b:8', 'an hour at the Nile — seven days\' halt')
        return out("an hour at the Nile, seven days' halt — measure for measure", ['journey_halted'])
    if ask == 'halt':
        ink('12:15-16', '"the people did not journey until Miriam was gathered in; and afterward the people journeyed"')
        return out('the halt until she was gathered; then Paran', ['journey_halted'])
    if ask == 'leper_shaves_on_festival':
        move('Mishnah Moed Katan 3:1; Moed Katan 7b', 'the leper rising to purity shaves on the intermediate days; the leper as one dead')
        return out('the leper shaves on the intermediate days', ['healed'])
    if ask == 'humble':
        ink('12:3', '"the man Moses was very humble" — written without the yod, read with it (the pair)'); move('Nedarim 38a:9; Chullin 89a', 'Moses humble, wise, wealthy')
        return out("humble — written without the yod, read with it", ['evil_speech_spoken'])
    if ask == 'article_blocks_identity':
        ink('12:3 / 27:18', '"THE man Moses" / "a man in whom is spirit"'); move('Yoma 76a:1', '"man" / "man" reads Joshua — "the man" no match: the article blocks the identity')
        return out("'the man' no match for 'man' — the article blocks the identity", ['evil_speech_spoken'])
    if ask == 'foolish':
        ink('12:11', '"we have done foolishly and we have sinned"'); move('Berakhot 63b:12; Makkot 10a:20; Taanit 7a:11', 'no\'alnu = foolish, then sinned')
        return out('foolish, then sinned', ['evil_speech_spoken'])
    if ask == 'remember_miriam':
        move('Deut 24:9; Arakhin 15a-16b', '"remember what the LORD your God did to Miriam" — the paradigm of evil speech')
        return out('the paradigm of evil speech (Deut 24:9)', ['evil_speech_spoken'])
    if ask == 'days':
        ink('12:15', '"shut out of the camp seven days" — %s' % SEVEN)
        return out('7 days', ['confined_seven_days'])
    return out('no verdict in span', [FX.NONE])
