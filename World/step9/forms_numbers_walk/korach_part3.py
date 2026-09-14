
# ===== F3: THE WATCH (Num 18:1-7) ==========================================================================
def the_watch(case, data):
    del P[:]
    ask = case['ask']
    if ask == 'iniquity_of_the_sanctuary':
        ink('18:1', '"you and your sons and your father\'s house with you shall bear the iniquity of the sanctuary" — the LORD to Aaron alone (five Torah seats, three here)'); move('Sifrei Bamidbar 116:1 (R. Yoshiyah)', "the priests' mishandled offerings"); move('CALLED cold_run_tzav.dues_machine(eli_violation) -> %r [IMPORT, live call]' % TZ_ELI, "Eli's sons the recorded violation (1 Sam 2:15-17 — the Sifrei's own citation on 18:1)")
        return out("the priests' mishandled offerings (Sifrei 116:1 — R. Yoshiyah); Eli's sons the recorded violation (tzav CALLED)", [FX.NONE])
    if ask == 'iniquity_of_the_priesthood':
        ink('18:1', '"you and your sons with you shall bear the iniquity of your priesthood"'); move('Sifrei Bamidbar 116:1', 'keeping strangers out')
        return out('keeping strangers out (Sifrei 116:1)', [FX.NONE])
    if ask == 'song':
        ink('18:2-3', '"your brothers the tribe of Levi... joined to you and serve you" — Leah\'s verb at Levi\'s naming (Gen 29:34); "neither they nor you"'); move('Arakhin 11b:2 (R. Yonatan)', 'the Levites equated with the priests for a service pertaining to the altar — the song'); move('Sifrei Bamidbar 116:1', '"with you" = the Levites\' song')
        return out("the Levites' altar-service is the song — neither they nor you (Arakhin 11b; Sifrei 116:1)", ['watch_owed'])
    if ask == 'fence':
        ink('18:3', '"only to the vessels of the holy and to the altar they shall not come near, that they die not, BOTH THEY AND YOU"'); move('Sifrei Bamidbar 116:1', "the two-way fence — the priests inside, the Levites outside; treasurers and trustees"); move('Arakhin 11b', "the priests not the Levites' work, the Levites not the priests'")
        return out("both they and you — the priests not the Levites' work, the Levites not the priests' (18:3; Sifrei 116:1; Arakhin 11b)", ['watch_owed'])
    if ask == 'watch_stories':
        ink('18:2', '"that they may accompany you and serve you"'); ink('18:4', '"and keep the watch of the tent of meeting"'); move('Tamid 26b:3-4', 'the priests keep watch ABOVE, the Levites BELOW'); move('Mishnah Middot 1:5, 1:9', 'the Gate of the Sparks; the priest locks within while the Levite sleeps outside')
        return out('the priests above, the Levites below (Tamid 26b; Mishnah Middot 1:5); the priest locks within, the Levite sleeps outside (Middot 1:9)', ['watch_owed'])
    if ask == 'watch_places':
        ink('18:4-5', '"keep the watch of the tent of meeting... the watch of the holy and the watch of the altar" — the watch-word six times'); dat('the row watch_places = %s' % data['watch_places']['value']); move('Mishnah Middot 1:1-2; Mishnah Tamid 1:1', 'three and twenty-one; the sleeping watchman beaten, his clothes burned')
        return out('3 and 21 — the priests in three places, the Levites in twenty-one (Mishnah Middot 1:1; Tamid 1:1); the sleeping watchman beaten (Middot 1:2)', ['watch_owed'])
    if ask == 'stranger_warning':
        ink('18:4', '"and a stranger shall not come near to you" — the warning, one seat'); ink('1:51, 3:10, 3:38, 18:7', '"the stranger who comes near shall be put to death" — the punishment at four seats'); move('Zevachim 16a:5', 'the non-priest barred from the rites is derived from 18:4'); move('Sifrei Bamidbar 116:1', 'the warning and the punishment')
        return out('18:4 the warning — a stranger shall not come near to you (Zevachim 16a; Sifrei 116:1)', ['stranger_barred'])
    if ask == 'stranger_death':
        ink('18:7', '"and the stranger who comes near shall be put to death" — the formula\'s fourth seat'); dat('the row zar_who_served is BAMIDBAR\'S (1:51\'s clause), read by CALL: %s — %s' % (ZAR['value'], ZAR['source'][:90])); move('Mishnah Sanhedrin 9:6; Sanhedrin 83b:4, 84a:13', 'the Rabbis: death at the hand of Heaven; R. Akiva: strangulation; R. Yishmael\'s "shall die" / "shall be put to death"'); move('Sifrei Bamidbar 116:2', 'only for a service, even in purity — the fork on "shall be put to death"')
        return out("death by Heaven — the Rabbis; R. Akiva: strangulation (Mishnah Sanhedrin 9:6; Sanhedrin 83b, 84a) — Bamidbar's row zar_who_served by CALL: %s" % ZAR['value'], ['death_by_heaven'])
    if ask == 'stranger_death_scope':
        ink('18:7', '"for every matter of the altar and within the veil, and you shall serve; a service of GIFT"'); move('Yoma 24a:7 (Rav)', 'a service of giving, not removal; a complete service'); move('Yoma 24b:1', 'within the veil the giving services only; outside any service'); move('Yoma 27a:1', 'slaughter by a non-priest valid — Lev 1:5'); move('Sifrei Bamidbar 116:2', 'only for a service, even in purity')
        return out('a service of giving and complete — not removal, not slaughter; within the veil the giving services (Yoma 24a-b, 27a); only for a service, even in purity (Sifrei 116:2)', [FX.NONE])
    if ask == 'no_more_wrath':
        ink('18:5 / 1:53', 'the clause computed: 1:53 %s; 18:5 %s — added %s, dropped %s' % (' '.join(WRATH_153), ' '.join(WRATH_185), WRATH_ADDED, WRATH_DROPPED)); move('Sifrei Bamidbar 116:1', 'four "no more"s, each paid by a prior event — the calf, the murmur, the spies, Korach (M-23 exemplar 15)')
        return out("18:5 = 1:53's clause with one token added — no MORE wrath (computed); the four no-mores each paid by a prior event (Sifrei 116:1)", ['watch_owed'])
    if ask == 'given_to_the_lord':
        ink('18:6', '"to you a GIFT, given to the LORD" — the third form of the Levites given (3:9, 8:16)'); move('Sifrei Bamidbar 116:2', 'to the LORD, not to the priests')
        return out('a gift, given to the LORD (18:6) — to the LORD, not to the priests (Sifrei 116:2); the third form (3:9, 8:16)', [FX.NONE])
    if ask == 'service_of_gift':
        ink('18:7', '"a service of gift I give your priesthood"'); move('Pesachim 73a:1; Sifrei Bamidbar 116:2 (R. Tarfon)', 'the eating of terumah in the provinces made like the Temple\'s service'); move('Mishnah Yoma 2:1-2', 'the lots — service by lot as the blood is by lot (Sifrei 116:2)')
        return out('a service of gift — the lots (Mishnah Yoma 2:1-2: four lotteries); eating terumah in the provinces equated (Pesachim 73a; Sifrei 116:2)', [FX.NONE])
    if ask == 'lots':
        dat('the row lots = %s' % data['lots']['value']); move('Mishnah Yoma 2:1-7; Mishnah Tamid 1:2', 'the ashes, the thirteen, the incense, the limbs; nine to twelve priests; the ram eleven, the bull twenty-four')
        return out('four lotteries — the ashes, the thirteen, the incense, the limbs (Mishnah Yoma 2:1-4); nine to twelve priests (2:5); the ram eleven, the bull twenty-four (2:6-7)', [FX.NONE])
    if ask == 'genealogy_chamber':
        ink('18:7', '"and within the veil"'); dat('the row genealogy_chamber = %s' % data['genealogy_chamber']['value']); move('Sifrei Bamidbar 116:2; Mishnah Middot 5:4', 'the chamber where the priesthood\'s genealogy was judged — black and white')
        return out('within the veil — the chamber of hewn stone judges the priesthood: black and white (Mishnah Middot 5:4; Sifrei 116:2)', [FX.NONE])
    if ask == 'washing_hands':
        move('Sifrei Bamidbar 116:2', 'the washing of the hands scriptural — "and you shall serve"'); move('Chullin 106a-107a', 'the hands washed')
        return out('the washing of the hands scriptural (Sifrei 116:2; Chullin 106a)', [FX.NONE])
    if ask == 'why_reiterate':
        ink('18:1', 'the demarcation reiterated after 1:51, 3:10, 3:38'); move('Sifrei Bamidbar 116:1 (Rebbi)', 'because Korach came, Scripture reiterated the exhortation — the census of the demarcation verses')
        return out('because Korach came, Scripture reiterated the exhortation (Sifrei 116:1 — Rebbi)', [FX.NONE])
    return out('no verdict in span', [FX.NONE])


# ===== F4: THE GIFTS (Num 18:8-19) =========================================================================
def the_gifts(case, data):
    del P[:]
    ask = case['ask']
    if ask == 'with_joy':
        ink('18:8', '"and the LORD spoke to Aaron: and I, behold, I have given you" — the LORD to Aaron; 17:5\'s "to him" the frame through Moses'); move('Sifrei Bamidbar 117:1 (R. Yishmael; R. Nathan)', '"and I, behold" — with joy; "and I" willingly')
        return out("and I, behold — with joy (Sifrei 117:1); through Moses by 17:5's to him", [FX.NONE])
    if ask == 'covenant_reason':
        ink('18:8', 'the gifts written after the rebellion'); move('Sifrei Bamidbar 117:2', 'the covenant written, sealed and recorded because Korach contested — the king\'s retainer'); move('Sifrei Bamidbar 119:2 (R. Yishmael)', '"my cow\'s leg was broken for my good" — for Aaron\'s good did Korach come')
        return out("the covenant written because Korach contested — the king's retainer (Sifrei 117:2); for Aaron's good did Korach come (119:2)", [FX.NONE])
    if ask == 'eaten_in_greatness':
        ink('18:8', '"to you I have given them for ANOINTING"'); move('Onkelos Num 18:8', 'for GREATNESS — cut from the shelf\'s bytes at the reading'); move('Zevachim 91a:19', 'THE TALMUD CITES ONKELOS: eaten as kings eat, any manner'); move('Chullin 132b:14; Sotah 15a:5; Zevachim 28a:10', 'roasted with mustard; wine, oil and honey in the remainder; the tail\'s skin')
        return out('for anointing = for greatness — eaten as kings eat, roasted with mustard, any manner (Onkelos cited at Zevachim 91a; Chullin 132b; Sotah 15a)', ['due_to_priest'])
    if ask == 'twenty_four':
        L = data['the_twenty_four']['value']; n = len(L['sanctuary']) + len(L['borders']); assert n == 24, n
        ink('18:8-19', 'a generalization (18:8), the details (18:9-18), a covenant of salt (18:19)'); dat('the row the_twenty_four = twelve in the sanctuary + twelve in the borders = %d (computed on the list)' % n); move('Chullin 133b:11; Bava Kamma 110b; Sifrei Bamidbar 119:1-2', 'twenty-four gifts given to Aaron and his sons')
        return out('24 — twelve in the sanctuary, twelve in the borders (Sifrei 119:1-2; Chullin 133b; Bava Kamma 110b); a generalization, a detail and a covenant of salt', ['priestly_dues_granted'])
    if ask == 'most_holy_list':
        ink('18:9', '"every offering of theirs, every meal offering, every sin offering, every guilt offering" — the four "every"s (Sifrei 117:2\'s four lists)'); move('Menachot 73a:9; Zevachim 44b:4 (Levi\'s baraita, the outside teaching)', 'the omer\'s and the suspected wife\'s meal offerings, the bird olah\'s meat'); move('Menachot 58a:14', 'the leper\'s log included'); move('CALLED cold_run_chatat.domain(unwitting) -> %r; cold_run_minchah.adjuncts(sinner) -> %r; cold_run_vayikra5.pointers(asham_procedure) -> %r [IMPORT, live calls]' % (CH_SIN, MN_SINNER, str(V5_ASHAM)[:60]), 'the sin, meal and guilt offerings the engines\' own objects')
        return out("every offering, every meal offering, every sin offering, every guilt offering (18:9) — the four everys include the omer's, the suspected wife's, the bird olah's meat, the leper's log (Menachot 73a; Zevachim 44b)", ['due_to_priest'])
    if ask == 'from_the_fire':
        ink('18:9', '"this shall be yours of the most holy, from the fire"'); move('Sifrei Bamidbar 117:2', 'the most holy from the fire = the burnt offering\'s hide')
        return out("the olah's hide — the most holy from the fire (Sifrei 117:2)", ['due_to_priest'])
    if ask == 'returned':
        ink('18:9', '"which they RETURN to Me" — 5:8\'s restitution the pointer'); move('Sifrei Bamidbar 117:2; Bava Kamma 110a', 'the proselyte\'s theft')
        return out("which they return to Me — the proselyte's theft (5:8; Sifrei 117:2; Bava Kamma 110a)", ['due_to_priest'])
    if ask == 'most_holy_eating_place':
        ink('18:10', '"in the most holy place you shall eat it"'); move('Menachot 9a:1', 'the courtyard; inside the Sanctuary in certain instances'); move('Zevachim 63a:15 (R. Yochanan ben Beteira)', 'gentiles surrounding the courtyard — the priests eat inside')
        return out('in the most holy place — the courtyard; inside the Sanctuary when gentiles surround it (Zevachim 63a; Menachot 9a)', [FX.NONE])
    if ask == 'every_male':
        ink('18:10', '"every male shall eat it"'); move('Menachot 83a:2; Zevachim 97b:11', 'communal peace offerings eaten only by the priests\' males')
        return out("every male — communal peace offerings eaten by the priests' males (Menachot 83a; Zevachim 97b)", [FX.NONE])
    if ask == 'most_holy_portion_use':
        dat('the row most_holy_portion_use = %s' % data['most_holy_portion_use']['value']); move('Kiddushin 52b:16', 'R. Yehuda: betrothed with it; R. Yosei: consumption alone')
        return out('R. Yehuda: betrothed with it; R. Yosei: consumption alone (Kiddushin 52b)', [FX.NONE])
    if ask == 'impure_terumah_benefit':
        ink('18:8', '"the watch of My TERUMOT" — plural'); move('Shabbat 25a:2, 26a:5; Yevamot 74a:18 (Rav Nachman / Rabba bar Avuh)', 'two terumot — the impure burned with benefit beneath the dish, from the separation onward')
        return out('My terumot — two: the impure burned with benefit beneath the dish, from the separation onward (Shabbat 25a-26a; Yevamot 74a)', [FX.NONE])
    if ask == 'doubtful_terumah_watch':
        dat('the row doubtful_terumah_watch = %s' % data['doubtful_terumah_watch']['value']); move('Bekhorot 34a:6', 'R. Yehoshua: the pure only; R. Eliezer: the doubtful too')
        return out('R. Yehoshua: safeguard only the pure; R. Eliezer: the doubtful too (Bekhorot 34a)', [FX.NONE])
    if ask == 'breast_and_thigh':
        ink('18:11', '"the terumah of their gift, all the wave offerings of the children of Israel" — to your sons and daughters'); move('CALLED cold_run_tzav.dues_machine(breast_thigh) -> %r [IMPORT, live call]' % TZ_BT, 'Lev 7:30-34\'s breast and thigh')
        return out('breast and thigh to the priests after the smoking (tzav CALLED); the terumah of their gift, all the wave offerings (18:11)', ['due_to_priest'])
    if ask == 'household':
        ink('18:11, 18:13', '"every clean one in your house shall eat it" twice; "to your daughters"'); move('CALLED cold_run_priesthood.holy_food(household, who=wife) -> %r [IMPORT, live call]' % PR_HOUSE, 'Lev 22:11\'s household — the wife eats'); move('CALLED cold_run_priesthood.holy_food(daughter_to_stranger) -> %r' % PR_DAUGHTER, 'Lev 22:12-13\'s daughter')
        return out('every clean one in your house — the household (priesthood CALLED); to your daughters', ['terumah_fed'])
    if ask == 'betrothed_eats':
        ink('18:11, 18:13', '"every clean one in your house" TWICE — the betrothed daughter of an Israelite (Sifrei 117:2)'); dat('the row betrothed_eats = %s' % data['betrothed_eats']['value']); move('Sifrei Bamidbar 117:2 (R. Yochanan b. Bag Bag; R. Yehudah in Netzivim)', 'the a-fortiori: she eats; the Sages\' decree: not'); move('Mishnah Ketubot 5:2-3; Ketubot 57b-58a', 'the later court: not until she enters the canopy — the cup and the simpon')
        return out('the a-fortiori: she eats (R. Yochanan b. Bag Bag); THE DECREE: not until the canopy (Mishnah Ketubot 5:3 — the later court; Ketubot 57b-58a: the cup and the simpon) — the decree over the a-fortiori', ['stranger_barred'])
    if ask == 'the_best_triad':
        ink('18:12', '"all the best of the fresh oil, all the best of the wine and the grain, their first part" — the triad %s: oil, wine, grain — reversed against eleven grain-wine-oil seats; the first word Izhar\'s' % TRIAD); move('Bekhorot 53b:17, 54b:2; Temurah 5a:11', 'the best of this and of that separately — kind for kind; "their first part" each type its own')
        return out("the best of the oil, the wine and the grain (18:12) — Izhar's word; the triad reversed against eleven seats (computed); kind for kind: each type its first (Bekhorot 53b, 54b)", [FX.NONE])
    if ask == 'bikkurim':
        ink('18:13', '"the first fruits of all that is in their land, which they bring to the LORD, shall be yours; every clean one in your house shall eat it"'); move('Sifrei Bamidbar 117:2', 'holy while attached'); move('Chullin 136a:8; Menachot 84b:6, 84b:10', 'partners liable, outside the land exempt; roofs and ships; the household eats — the verse read as two'); move('CALLED cold_run_moadim.two_loaves() -> %r [IMPORT, live call]' % (str(MO_LOAVES)[:80],), 'the two loaves precede the first fruits (Menachot 84b:6)')
        return out('the first fruits of all — holy while attached (18:13; Sifrei 117:2); partners liable, outside the land exempt (Chullin 136a); roofs and ships (Menachot 84b); the household eats (84b:10)', ['due_to_priest'])
    if ask == 'devoted':
        ink('18:14', '"every devoted thing in Israel shall be yours" — one seat'); dat('the row devotion_default = %s; the four authorities: %s' % (data['devotion_default']['value'], data['devotion_default']['settings']['four_authorities'][:120])); move('CALLED cold_run_temurah.devote(unspecified_destination) -> %r [IMPORT, live call]' % TM_DEV, 'Lev 27:21 / 27:28 — the Sages / R. Yehuda b. Beteira'); move('Sifrei Bamidbar 117:3', 'gentiles\', women\'s and bondsmen\'s too; the four-way dispute')
        return out("every devoted thing in Israel — gentiles', women's, bondsmen's too (Sifrei 117:3); unspecified: %s (temurah CALLED) — the four-way dispute: R. Yossi HaGelili the priests, R. Yehudah b. Beteira Temple maintenance, R. Yehudah b. Bava the priests, R. Shimon Heaven" % TM_DEV, ['most_holy'])
    if ask == 'devoted_status':
        ink('18:14', '"shall be yours"'); move('CALLED cold_run_temurah.devote(priests_devotions) -> %r [IMPORT, live call]' % TM_DEV_PRIESTS, 'no redemption, given to the priests'); move('Arakhin 29a:1; Bekhorot 32a:25', 'in the owner\'s house consecrated (27:28); given to the priest common (18:14)'); move('Arakhin 28b:1', '"to the priest" / "to the priest" with 5:8 — the watch on duty')
        return out('in the owner\'s house consecrated; given to the priest common (Arakhin 29a; Bekhorot 32a); to the priest of the watch serving (Arakhin 28b)', ['due_to_priest'])
    if ask == 'devoted_to_whom':
        move('Arakhin 28b:1', 'a dedicated field to the priest of the watch serving — the verbal analogy "to the priest" (Lev 27:21) / "to the priest" (5:8, the proselyte\'s theft)')
        return out('to the priest of the watch serving in the Temple — to the priest / to the priest with 5:8 (Arakhin 28b)', ['due_to_priest'])
    if ask == 'devotion_by_priests':
        dat('the row devotion_by_priests = %s' % data['devotion_by_priests']['value']); move('Mishnah Arakhin 8:5; Arakhin 28a:12', 'R. Yehuda: neither; R. Shimon: priests not, Levites may')
        return out('R. Yehuda: priests and Levites may not; R. Shimon: priests not, Levites may (Mishnah Arakhin 8:5)', [FX.NONE])
    if ask == 'devote_firstborn':
        move('CALLED cold_run_temurah.devote(firstborn) -> %r [IMPORT, live call]' % TM_DEV_FB, 'Mishnah Arakhin 8:7: the firstborn, whole or blemished, may be devoted — assessed by the daughter\'s son; R. Yishmael\'s two verses')
        return out("the firstborn, whole or blemished, may be devoted — assessed by the daughter's son (Mishnah Arakhin 8:7; temurah CALLED: %s)" % TM_DEV_FB, [FX.NONE])
    if ask == 'opens_the_womb':
        ink('18:15', '"all that opens the womb of all flesh which they offer to the LORD, in man and in beast, shall be yours; yet redeem, you shall redeem the firstborn of man, and the firstborn of the unclean beast you shall redeem"'); move('Sifrei Bamidbar 118:1', '"which they offer" excludes the unclean animal, "and in beast" re-includes the blemished; what obtains with the man obtains with his beast — the Levites\' ass exempt'); move('Bekhorot 4a:6', 'the juxtaposition: the Levites\' donkeys exempt')
        return out("all that opens the womb — which they offer excludes the unclean animal, and in beast re-includes the blemished (Sifrei 118:1); the Levites' ass exempt", ['consecrated_firstborn'])
    if ask == 'redemption_rate':
        ink('18:16', '"by your valuation, five shekels of silver by the shekel of the sanctuary — it is twenty gerah" — %s' % REDEMPTION); move('CALLED cold_run_bamidbar.levites(rate) -> %r [IMPORT, live call]' % BM_RATE, '3:47\'s five, five shekels per skull — the same rate at the census')
        return out(BM_RATE, ['pays'])
    if ask == 'redemption_before_thirty':
        ink('18:16', '"from a month old you shall redeem"'); dat('the row firstborn_threshold is Bamidbar\'s threshold_edge, by CALL'); move('CALLED cold_run_bamidbar.levites(age, 31 days) -> %r [IMPORT, live call]' % BM_AGE, '"month" / "month" with 3:40 (Bekhorot 49a:6)'); move('Bava Kamma 11b:2-3; Menachot 37a:8', 'mauled within thirty days — no redemption ("yet")'); move('Mishnah Bekhorot 8:6; Shabbat 135b:13', 'the thirtieth day like the day before (R. Akiva: doubtful); a child alive thirty days no stillborn')
        return out('after thirty days — from a month old (18:16 / 3:40; Bekhorot 49a; Bamidbar CALLED: %s); mauled within thirty — no redemption (Bava Kamma 11b); the thirtieth day like the day before (Mishnah Bekhorot 8:6)' % BM_AGE, ['pays'])
    if ask == 'redemption_timing':
        dat('the row donkey_timing = %s' % data['donkey_timing']['value']); move('Bekhorot 12b:23, 13a:3; Sifrei Bamidbar 118:1', 'the son after thirty days; the ass immediately (the Rabbis) or after thirty (R. Eliezer)')
        return out('thirty days the son, at once the ass (Bekhorot 12b-13a; Sifrei 118:1 — immediately or after a month)', ['pays'])
    if ask == 'redemption_means':
        ink('18:16', '"by your valuation, five shekels of silver"'); dat('the row redemption_means = %s' % data['redemption_means']['value']); move('CALLED cold_run_bamidbar.levites(means, coins) -> %r [IMPORT, live call]' % BM_MEANS, 'Mishnah Bekhorot 8:8'); move('Sifrei Bamidbar 118:1; Bekhorot 51a:10; Shevuot 4b:6', 'general-particular-general: movable, not bondsmen, writs or land; Rebbi: writs only')
        return out('redeemed when in the priest\'s hand (Bamidbar CALLED); not with slaves, notes, land or consecrated items (Mishnah Bekhorot 8:8); movable, not writs (Sifrei 118:1 — Rebbi: writs only)', ['pays'])
    if ask == 'twenty_gerah_floor':
        ink('18:16', '"it is twenty gerah" — the seat among the shekel engine\'s five: %s' % IS_SEATS); move('CALLED cold_run_incense_shekel.shekel(twenty_gerah) -> %r [IMPORT, live call]' % IS_SEATS, 'the unit defined at Exod 30:13'); move('Bekhorot 50a:6; Sifrei Bamidbar 118:1', '"shall be" — may add (the Sages\' sixth); "the same is twenty" — never fewer'); move('CALLED cold_run_yovel.field_valuation(49)[shekel] -> %r [IMPORT, live call]' % YV_SHEKEL, 'Lev 27:25 "twenty gerah shall be the shekel" — "by your valuation" (18:16) the valuations\' word')
        return out('twenty gerah — more, not less (Sifrei 118:1; Bekhorot 50a); the seat among the shekel engine\'s five: Num 18:16', ['pays'])
    if ask == 'five_sela_coinage':
        move('Mishnah Bekhorot 8:7; Bekhorot 49b:10-11; Kiddushin 11b:7', 'the five sela in the Tyrian maneh; the sanctuary shekel twenty gera')
        return out('the five sela in the Tyrian maneh (Mishnah Bekhorot 8:7; Bekhorot 49b)', ['pays'])
    if ask == 'self_redemption':
        ink('18:15', '"REDEEM, YOU SHALL REDEEM" — the doubled infinitive\'s one seat'); move('Kiddushin 29a:15', 'the father redeems (Exod 34:20); if not, the son redeems himself'); move('Sifrei Bamidbar 118:1 (Kerem Beyavneh, R. Tarfon)', 'the doubled verb')
        return out('redeem, you shall redeem — the son redeems himself if the father did not (Kiddushin 29a; Sifrei 118:1 Kerem Beyavneh)', ['pays'])
    if ask == 'redemption_money_lost':
        ink('18:15', '"shall be yours" BEFORE "you shall redeem" — the verse order'); move('Mishnah Bekhorot 8:8; Bekhorot 51a:8, 51b:7-9', 'the father liable for the lost coins; redeemed only in the priest\'s hand')
        return out('the father liable — shall be yours before you shall redeem (Mishnah Bekhorot 8:8; Bekhorot 51a)', ['pays'])
    if ask == 'unclean_firstborn_scope':
        ink('18:15', '"the firstborn of the unclean beast you shall redeem"'); move('Sifrei Bamidbar 118:1; Bekhorot 5b:28 (R. Yosei HaGelili)', 'the ass alone — "the firstborn of a donkey" (Exod 13:13), not horses or camels; with a sheep'); move('CALLED cold_run_pesach.firstborn(donkey) -> %r [IMPORT, live call]' % PS_DONKEY, 'Exod 13:13\'s fork')
        return out('the ass alone (Sifrei 118:1; Bekhorot 5b) — redeem with a lamb, else break the neck (pesach CALLED)', ['redeem_or_break'])
    if ask == 'ass_redeem_or_break':
        move('CALLED cold_run_pesach.firstborn(donkey) -> %r [IMPORT, live call]' % PS_DONKEY, 'Mishnah Bekhorot 1:7: the redemption precedes the breaking')
        return out(PS_DONKEY, ['redeem_or_break'])
    if ask == 'levite_donkey':
        move('CALLED cold_run_bamidbar.levites(owner=priest, donkey) -> %r [IMPORT, live call]' % BM_OWNER, 'Mishnah Bekhorot 1:1\'s a-fortiori from 3:45; Bekhorot 4a:6\'s juxtaposition'); move('CALLED cold_run_bamidbar.levites(partner) -> %r' % BM_PARTNER, 'a gentile partner')
        return out(BM_OWNER, ['exempt'])
    if ask == 'donkey_doubt':
        move('Mishnah Bekhorot 1:3', 'the untried donkey bearing two males — one lamb; a male and a female — the burden of proof on the priest')
        return out('the burden of proof on the priest — a male and a female, the owner keeps the lamb; two males, one lamb (Mishnah Bekhorot 1:3)', [FX.NONE])
    if ask == 'redeeming_lamb':
        dat('the rows redeeming_lamb = %s; lamb_responsibility = %s' % (data['redeeming_lamb']['value'], data['lamb_responsibility']['value'])); move('Mishnah Bekhorot 1:4-6; Bekhorot 12b:18', 'any lamb; the exclusions; the designated lamb died')
        return out('any lamb — sheep or goat, any age, blemished; not a calf, a hybrid or a koy (Mishnah Bekhorot 1:4-5); the designated lamb died — R. Eliezer / the Rabbis (1:6)', [FX.NONE])
    if ask == 'clean_firstborn':
        ink('18:17', '"the firstborn of an ox, or the firstborn of a sheep, or the firstborn of a goat you shall not redeem — they are holy"'); move('Bekhorot 5b:10; Sifrei Bamidbar 118:1', 'an ox and its firstborn an ox; no hybrid'); move('CALLED cold_run_temurah.redeem(animal_tithe) -> %r [IMPORT, live call]' % TM_TITHE, 'Lev 27:33\'s "it shall not be redeemed" beside')
        return out('the firstborn of an ox, a sheep, a goat you shall not redeem — they are holy (18:17); an ox and its firstborn an ox (Bekhorot 5b); no hybrid (Sifrei 118:1)', ['consecrated'])
    if ask == 'firstborn_resembles':
        move('Bekhorot 7a:4, 12a:16, 6b:24; Bava Kamma 78a:6; Mishnah Bekhorot 1:2', 'the head and the majority of the body like the mother; resembling another species — no firstborn; the ass likewise')
        return out('the head and the majority of the body like the mother (Bekhorot 7a); resembling another species — no firstborn (Bekhorot 12a; Bava Kamma 78a)', [FX.NONE])
    if ask == 'firstborn_portions':
        ink('18:17', '"you shall sprinkle THEIR blood on the altar and make THEIR fat smoke"'); dat('the row one_spilling = %s' % data['one_spilling']['value']); move('Pesachim 64b:18; Zevachim 37a:8-9, 56b:12 (R. Yosei HaGelili / R. Yishmael)', 'the tithe and the Passover too — or from Deut 12:27'); move('Keritot 4a:12', 'the portions burned'); move('Sifrei Bamidbar 118:1', '"they are consecrated" — one spilling (Yoshiyah) / the fats (Yitzchak)')
        return out("their blood, their fat — the tithe and the Passover placed like the firstborn (R. Yosei HaGelili; Zevachim 37a, 56b; Pesachim 64b); R. Yishmael from Deut 12:27; the portions burned (Keritot 4a)", ['consecrated'])
    if ask == 'firstborn_blood_placement':
        move('Mishnah Zevachim 5:8; Zevachim 56b:12', 'lesser sanctity; slaughtered anywhere in the courtyard; the blood ONE PLACEMENT on the base')
        return out("one placement on the base — their blood, their fat: the tithe and the Passover too (R. Yosei HaGelili; Zevachim 56b; Mishnah Zevachim 5:8; Sifrei 118:1's one spilling)", ['consecrated'])
    if ask == 'firstborn_eating_window':
        ink('18:18', '"their flesh shall be yours, as the wave-breast and as the right thigh, it shall be yours" — "it shall be yours" twice'); move('CALLED cold_run_offerings.dispatch(shelamim) -> the peace offering\'s row (%s) [IMPORT, live call]' % ', '.join(sorted(OF_SHELAMIM)), 'the analogy\'s object'); move('Bekhorot 27b:7, 28a:2; Zevachim 57a:5-13; Temurah 21b:13; Mishnah Zevachim 5:8', 'two days and a night; the second "it shall be yours" the second day')
        return out('two days and a night — as the wave-breast and the right thigh (18:18; Bekhorot 27b; Zevachim 57a; Mishnah Zevachim 5:8) — the peace offering\'s row CALLED', ['due_to_priest'])
    if ask == 'firstborn_sale':
        move('Bava Kamma 13a:7; Bekhorot 31b:7, 32a:7; Temurah 5b:1, 8a:1; Zevachim 75b:8', '"you shall not redeem" — its sanctity never removed, yet sold: alive unblemished, blemished alive or slaughtered; the tithe neither')
        return out('not redeemed, but sold — alive unblemished, blemished alive or slaughtered; the tithe neither (Bava Kamma 13a; Bekhorot 31b; Temurah 5b, 8a)', [FX.NONE])
    if ask == 'firstborn_substitute':
        move('Temurah 21a:9; Zevachim 37b:3, 81b:7-8', '"THEY are holy" — they, not their substitutes')
        return out('they are holy — they, not their substitutes (Temurah 21a; Zevachim 37b)', [FX.NONE])
    if ask == 'firstborn_blood_mixed':
        move('Zevachim 81a:8; Temurah 5b:9', '"they are holy" — the blood mixed with others\' still sacrificed')
        return out("they are holy — the blood mixed with others' still sacrificed (Zevachim 81a; Temurah 5b)", [FX.NONE])
    if ask == 'firstborn_without_altar':
        move('Makkot 19a:9; Temurah 21a:22; Zevachim 60b:9', 'the flesh as the blood — eaten only while the altar stands; second tithe follows')
        return out('the flesh as the blood — eaten only while the altar stands (Makkot 19a; Temurah 21a; Zevachim 60b)', [FX.NONE])
    if ask == 'blemished_firstborn':
        move('Zevachim 37b:2', 'the blemished firstborn to the priest — "it shall be yours" repeated'); dat('the row raise_before_giving = %s' % data['raise_before_giving']['value']); move('Mishnah Bekhorot 4:1-5', 'raised thirty or fifty days; kept the year; the expert')
        return out('to the priest — it shall be yours repeated (Zevachim 37b); raised thirty or fifty days (Mishnah Bekhorot 4:1); kept the year (4:2); the expert (4:4-5)', ['due_to_priest'])
    if ask == 'blemished_keeping':
        move('Mishnah Bekhorot 4:2', 'a blemish within the year — the twelve months; after — thirty days')
        return out('a blemish within the year — kept the twelve months; after the year — thirty days (Mishnah Bekhorot 4:2)', [FX.NONE])
    if ask == 'blemish_expert':
        move('Mishnah Bekhorot 4:3-5', 'slaughtered then shown (R. Yehuda / R. Meir); a non-expert pays, the court\'s expert exempt (R. Tarfon\'s cow); a paid examiner disqualified unless like Ila')
        return out("the court's expert exempt, a non-expert pays (Mishnah Bekhorot 4:4); a paid examiner disqualified unless like Ila (4:5); shown after slaughter — R. Yehuda / R. Meir (4:3)", [FX.NONE])
    if ask == 'firstborn_eaters':
        dat('the row firstborn_eaters = %s' % data['firstborn_eaters']['value']); move('Bekhorot 32b:11, 33a:7', 'Beit Shammai / Beit Hillel')
        return out('Beit Shammai: priests only, not menstruating women; Beit Hillel: the blemished to any (Bekhorot 32b-33a)', [FX.NONE])
    if ask == 'raise_before_giving':
        dat('the row raise_before_giving = %s' % data['raise_before_giving']['value']); move('Mishnah Bekhorot 4:1; Bekhorot 26b:10', 'Exod 22:29 juxtaposed to 18:16\'s month')
        return out("30 days a small animal, 50 a large (Mishnah Bekhorot 4:1; Bekhorot 26b — Exod 22:29 juxtaposed to 18:16's month)", [FX.NONE])
    if ask == 'twins':
        move('Mishnah Bekhorot 8:3-5', 'twins — five sela after thirty days; one died — exempt; two wives — ten; the intermingled by certainty; the son redeems himself')
        return out('twins — five sela after thirty days; one died — exempt; two wives — ten; the intermingled by certainty (Mishnah Bekhorot 8:3-5)', ['pays'])
    if ask == 'firstborn_for_redemption':
        move('Mishnah Bekhorot 8:1-2', 'the four classes; R. Yosei HaGelili: opens a Jewish mother\'s womb; the caesarean — neither'); move('CALLED cold_run_pesach.firstborn(caesarean_animal) -> %r [IMPORT, live call]' % PS_CAESAREAN, 'the womb not opened')
        return out("opens a Jewish mother's womb (Mishnah Bekhorot 8:1); the caesarean — neither (8:2; pesach CALLED: %s)" % PS_CAESAREAN, [FX.NONE])
    if ask == 'suspect_firstborn':
        move('Mishnah Bekhorot 4:7, 4:10', 'no meat nor untanned hides from one suspect on firstborns; may neither judge nor testify on that matter')
        return out('no meat nor untanned hides from one suspect on firstborns (Mishnah Bekhorot 4:7); may neither judge nor testify on it (4:10)', [FX.NONE])
    if ask == 'suspect_principle':
        move('Mishnah Bekhorot 4:10', 'suspect on this not on that; suspect on either suspect on purities')
        return out('suspect on the sabbatical year not on tithes, nor the reverse; suspect on either — on purities; neither judge nor witness on that matter (Mishnah Bekhorot 4:10)', [FX.NONE])
    if ask == 'covenant_of_salt':
        ink('18:19', '"a covenant of salt forever it is before the LORD, for you and your seed with you" — the phrase\'s two seats in the Bible (computed): %s' % COVENANT_OF_SALT); move('Sifrei Bamidbar 119:5', 'Aaron\'s covenant greater than David\'s — for the wicked sons too'); move('Menachot 19b:14-20a:1; 21b:12', 'salting indispensable; from communal supplies'); move('Chullin 133b:11', 'the twenty-four eternal as salt')
        return out("a covenant of salt — Aaron's (18:19) and David's (2 Chr 13:5) alone; salting indispensable (Menachot 19b-20a); from communal supplies (Menachot 21b); Aaron's greater than David's (Sifrei 119:5)", ['covenant_of_salt'])
    if ask == 'salt_source':
        move('Menachot 21b:12', '"everlasting covenant" / "everlasting covenant" with the showbread (Lev 24:8) — from communal supplies')
        return out('the salt from communal supplies — everlasting covenant / everlasting covenant with the showbread (Menachot 21b)', [FX.NONE])
    if ask == 'gentile_consecrations':
        ink('18:8', '"of all the hallowed things of the CHILDREN OF ISRAEL"'); move('Temurah 3a:4', 'not gentiles\' — no misuse in their consecrations')
        return out("of all the hallowed things of the children of Israel — not gentiles': no misuse (Temurah 3a)", [FX.NONE])
    if ask == 'three_crowns':
        dat('the row three_crowns = %s' % data['three_crowns']['value']); move('Sifrei Bamidbar 119:4; Mishnah Avot 4:13', 'three crowns; the good name above them')
        return out('three crowns — Torah, priesthood, kingdom; the good name above them (Avot 4:13; Sifrei 119:4)', [FX.NONE])
    if ask == 'bikkurim_partners':
        move('Chullin 136a:8', '"in THEIR land" — partners liable; "your land" excludes outside')
        return out('first fruits from land in partnership — liable; outside the land exempt (Chullin 136a)', ['due_to_priest'])
    if ask == 'bikkurim_scope':
        move('Menachot 84b:6', '"the first fruits of ALL" — roofs, ruins, flowerpots, ships; the two loaves first')
        return out('the first fruits of all — roofs, ruins, flowerpots and ships; the two loaves precede (Menachot 84b)', ['due_to_priest'])
    if ask == 'bikkurim_eaters':
        move('Menachot 84b:9-10 (Rav Mesharshiyya)', 'the verse read as two: the meal offerings for males, the first fruits for the household')
        return out('the household eats the first fruits — the verse read as two (Menachot 84b:10)', ['terumah_fed'])
    return out('no verdict in span', [FX.NONE])
