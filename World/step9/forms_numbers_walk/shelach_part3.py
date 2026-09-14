
# ===== F3: THE LIBATIONS (Num 15:1-13) ======================================================================
NO_LIBATIONS = ('firstborn', 'tithe', 'pesach', 'chatat', 'asham', 'festival_goat', 'bird_olah', 'meal_offering')
def libations(case, data):
    del P[:]
    ask = case['ask']
    if ask == 'table':
        ink('15:4-10', 'the table computed from the ink: %s (flour in tenths, oil and wine in hin)' % {k: tuple(str(x) for x in v) for k, v in TABLE.items()})
        return out('lamb 1/10 + 1/4 + 1/4; ram 2/10 + 1/3 + 1/3; bull 3/10 + 1/2 + 1/2 — computed from 15:4-10', [FX.NONE])
    if ask == 'table_seats':
        ink('Exod 29:40; Lev 23:13; Num 28:5-7, 28:14', 'the same rows at every seat: the tamid %s, the daily %s, the new moon %s; the omer\'s lamb %s — its flour doubled' % (TAMID_ROW, DAILY_ROW, MONTH_ROW, OMER_ROW)); move('Mishnah Menachot 9:4', 'the omer\'s lamb: doubled flour, oil and wine not doubled')
        return out("the lamb's quarter-hin at Exod 29:40, Lev 23:13, Num 28:5-7; 28:14 the three rows; the omer's flour doubled (two tenths — Mishnah Menachot 9:4)", [FX.NONE])
    if ask == 'logs':
        dat('the row hin_in_logs = %s' % data['hin_in_logs']['value']); ink('15:4-10', 'the fractions in logs: %s' % LOGS)
        return out('lamb 3, ram 4, bull 6 — the hin twelve logs (Mishnah Menachot 9:2)', [FX.NONE])
    if ask == 'mixing':
        ink('15:4-10', 'oil logs per tenth of flour: %s' % {k: str(v) for k, v in RATIO.items()}); move('Mishnah Menachot 9:4', 'bulls\' with rams\' — the same ratio; lambs\' with lambs\'; not lambs\' with bulls\' or rams\'')
        a, b = case.get('pair', ('bull', 'ram'))
        return out('may mix — the same ratio' if RATIO[a] == RATIO[b] else 'may not mix — the ratios differ', ['accepted'] if RATIO[a] == RATIO[b] else ['disqualified'])
    if ask == 'sukkot_sabbath':
        ink('15:4-10 with 29:12-16, 28:3, 28:9', 'thirteen bulls at %d, two rams at %d, fourteen lambs at %d, the two daily and the two Sabbath lambs = %d' % (TABLE['bull'][0], TABLE['ram'][0], TABLE['lamb'][0], SUKKOT_SABBATH)); move('Mishnah Menachot 12:4', 'sixty-one tenths — the community\'s most in a day')
        return out('61 tenths — 13 bulls x 3 + 2 rams x 2 + 14 lambs + 2 daily + 2 Sabbath lambs (Mishnah Menachot 12:4)', [FX.NONE])
    if ask == 'which_offerings':
        ink('15:3', '"a burnt offering or a sacrifice, for a vow or a gift or at your festivals"'); ink('15:8', '"a young bull for a burnt offering" — the festival goats excluded'); ink('15:5', '"with the burnt offering or for the sacrifice, for the one lamb" — the leper\'s three'); dat('the row which_take_libations')
        return out("all but the firstborn, the tithe, the Passover, the sin offering, the guilt offering; the leper's chatat and asham do (Mishnah Menachot 9:6; 15:5)", [FX.NONE])
    if ask == 'takes':
        kind = case['offering']
        if case.get('where') == 'wilderness':
            ink('15:2', '"when you come into the land of your dwellings" — the cell\'s own gate'); dat('the row libations_from = %s' % data['libations_from']['value'])
            return out('not yet — before the entry (15:2)', ['exempt'])
        if kind in ('leper_chatat', 'leper_asham'):
            ink('15:5', '"or for the sacrifice" — the leper\'s sin offering and guilt offering included (Menachot 91a:27)')
            return out('libations — the leper\'s (15:5)', ['libation_owed'])
        if kind in NO_LIBATIONS:
            ink('15:3, 15:8', 'a burnt offering or a sacrifice of a vow or a gift — not the %s' % kind); move('Mishnah Menachot 9:6; Menachot 90b:6-10', 'the list')
            return out('no libations', ['exempt'])
        ink('15:3-10', 'the table applies — %s' % kind)
        return out('libations', ['libation_owed'])
    if ask == 'donated':
        dat('the row libation_floors = %s' % data['libation_floors']['value']); ink('15:13', '"all the home-born shall do these" — libations alone; 28:14 "shall be" adds'); move('Mishnah Menachot 12:4, 13:5; Menachot 104a:10-11', 'three, four, six logs and beyond; never one, two or five')
        n = case.get('logs')
        if n is None:
            return out("not less than three logs — the lamb's; 3, 4, 6 and beyond, never 1, 2, 5 (Mishnah Menachot 12:4, 13:5; Menachot 104a)", [FX.NONE])
        ok = n >= 3 and n != 5
        return out('a valid libation of %d logs' % n if ok else 'no such libation — %d logs' % n, ['accepted'] if ok else ['disqualified'])
    if ask == 'donated_oil':
        dat('the row oil_donation = %s' % data['oil_donation']['value'])
        return out('wine yes; oil — R. Akiva no, R. Tarfon yes; Rabbi three logs (Mishnah Menachot 12:5; 107a:17)', [FX.NONE])
    if ask == 'donated_wine_disposal':
        ink('15:10', '"half a hin of wine, an offering made by fire"'); move('Zevachim 91b:12 (Shmuel)', 'sprinkled on the altar\'s fire; partial extinguishing is no extinguishing')
        return out("on the altar's fire — an offering made by fire (Shmuel, Zevachim 91b)", ['accepted'])
    if ask == 'gentile':
        ink('15:13', '"the home-born" — a Jew brings libations alone'); ink('15:11', '"so shall it be done for the one bull" — every olah requires them'); dat('the row gentile_libations = %s' % data['gentile_libations']['value']); move('Menachot 73b:14; Zevachim 45a:14; Temurah 3a:10; Mishnah Shekalim 7:6', 'no independent libations for a gentile; his olah\'s required, the public pays')
        return out("no independent libations; his olah's required (15:11, 15:13); the public pays if he sent none (Mishnah Shekalim 7:6)", ['libation_owed'])
    if ask == 'found_animal':
        move('Mishnah Shekalim 7:5', 'the found animal\'s libations from public funds — the court\'s ordinance')
        return out('from public funds (Mishnah Shekalim 7:5)', ['libation_owed'])
    if ask == 'heir':
        move('Mishnah Menachot 9:7', 'the heir places hands and brings the libations')
        return out('the heir brings the libations (Mishnah Menachot 9:7)', ['libation_owed'])
    if ask == 'so':
        ink('15:11', '"SO shall it be done" — the exact measure'); move('Menachot 27a:7-8', 'the wine\'s minority prevents the majority; the log of oil likewise')
        return out('the exact measure indispensable — "so" (Menachot 27a)', ['disqualified'])
    if ask == 'calf':
        ink('15:11', '"for the ONE bull" — the definite one (the parser\'s %s)' % ONE_OX_RAM); move('Menachot 91b:20', 'one law for all bulls, the calf included')
        return out('as a bull — "for the one bull" (Menachot 91b:20)', ['libation_owed'])
    if ask == 'palges':
        ink('15:6', '"or for a ram"'); dat('the row lamb_and_ram_ages = %s' % data['lamb_and_ram_ages']['value']); move('Chullin 23a:6 (R. Yochanan); Mishnah Parah 1:3', 'the thirteen-month animal — a ram\'s libations, not counted')
        return out("the ram's libations, not counted — the thirteen-month animal (Mishnah Parah 1:3; Chullin 23a)", ['libation_owed'])
    if ask == 'ages':
        dat('the row lamb_and_ram_ages = %s' % data['lamb_and_ram_ages']['value'])
        return out('lambs to a year, rams from thirteen months and a day (Mishnah Parah 1:3)', [FX.NONE])
    if ask == 'the_one':
        ink('15:5, 15:11', '"for the one lamb", "for the one bull", "for the one ram" — THE DEFINITE ONE read by the parser (%s, %s)' % (LAMB_B, ONE_OX_RAM)); move('Menachot 91b:9 (R. Natan); 91b:20', 'the woman\'s olah; the tithe\'s eleventh; the calf')
        return out("the definite one read — the woman's olah, the tithe's eleventh (Menachot 91b:9); the calf (91b:20)", [FX.NONE])
    if ask == 'aarons_ram':
        ink('15:6-7', '"or for a ram" beside 28:12'); move('Menachot 91b:12 (Rav Sheshet)', 'the ram of Aaron included')
        return out('libations — "or for a ram" (Rav Sheshet)', ['libation_owed'])
    if ask == 'each_animal':
        ink('15:11-12', '"so shall be done for each... according to their number" — separate libations per animal'); move('Menachot 91a:18-24', 'even consecrated together')
        return out('separate libations per animal, even consecrated together (15:11-12)', ['libation_owed'])
    if ask == 'tenths_integral':
        ink('15:4-9', 'the tenth the unit noun — one, two, three tenths (the parser\'s %s, %s, %s)' % (LAMB_A[0], RAM_A[0], BULL_A[0])); move('Mishnah Menachot 12:3', 'no partial tenths')
        return out('no partial tenths — half a tenth brings a whole; a tenth and a half brings two (Mishnah Menachot 12:3)', [FX.NONE])
    if ask == 'with_price':
        move('Mishnah Menachot 13:8', 'the libations inside the vow\'s price')
        return out("the libations inside the vow's price — a bull 100 dinars, a calf 5 sela, a ram 2, a lamb 1 (Mishnah Menachot 13:8)", [FX.NONE])
    if ask == 'from_when':
        ink('15:2', '"when you come into the land of your dwellings"'); dat('the row libations_from = %s' % data['libations_from']['value'])
        return out('the entry (Zevachim 111a); after inheritance and settlement (R. Yishmael, Kiddushin 37b) — none in the wilderness on both', [FX.NONE])
    if ask == 'altar_eras':
        dat('the row altar_eras = %s' % data['altar_eras']['value'])
        return out('the wilderness / Gilgal / Shiloh / Nov and Gibeon / Jerusalem — forbidden, permitted, forbidden, permitted, forbidden forever (Mishnah Zevachim 14:4-8)', [FX.NONE])
    if ask == 'private_altar':
        move('Mishnah Zevachim 14:10; Zevachim 111a-b', 'the high place\'s omissions; the intents equal')
        return out('no laying of hands, no north, no blood around, no waving; the intents equal (Mishnah Zevachim 14:10)', [FX.NONE])
    if ask == 'ezekiel':
        ink('15:6, 15:9', 'the ram two tenths, the bull three — against Ezek 46:7\'s "an ephah for the bull and an ephah for the ram"'); move('Menachot 45a:21 (R. Shimon)', 'the ink\'s rows hold; Ezekiel\'s reconciled')
        return out("the bull's three tenths and the ram's two against Ezekiel 46:7's ephah each (R. Shimon, Menachot 45a)", [FX.NONE])
    if ask == 'or_against_and':
        ink('15:3', '"from the herd OR from the flock" — Lev 1:2 "from the herd AND from the flock"')
        return out('"from the herd OR from the flock" against Lev 1:2\'s AND (computed)', [FX.NONE])
    if ask == 'oil_only':
        v = MN.adjuncts('libation')['v']; ink('15:4', '"a meal offering... mixed with oil" — no frankincense named'); dat('the minchah engine CALLED: adjuncts(libation) -> %s' % v)
        return out('%s — the libation meal offering: oil, no frankincense (the minchah engine CALLED)' % v, [FX.NONE])
    if ask == 'olah_table':
        t = OF.dispatch('olah:herd'); ink('15:3, 15:8, 15:24', '"a burnt offering" — Lev 1\'s own table by name'); dat('the offerings engine CALLED: dispatch(olah) -> %s' % {k: c['v'] for k, c in t.items()})
        return out('%s; %s; %s; %s (the offerings engine CALLED)' % (t['place']['v'], t['applications']['v'], t['procedure']['v'], t['disposition']['v']), [FX.NONE])
    if ask == 'owner_piggul':
        ink('15:4', '"he who sacrifices shall sacrifice his offering" — the owner named a sacrificer'); dat('the row owner_piggul = %s' % data['owner_piggul']['value'])
        return out('the owner can render piggul — "he who sacrifices" (R. Elazar son of R. Yosei); the performer only (the mishna)', [FX.NONE])
    raise KeyError(ask)


# ===== F4: THE STRANGER (Num 15:14-16) ======================================================================
def stranger(case, data):
    del P[:]
    ask = case['ask']
    if ask == 'convert_offering':
        ink('15:14', '"as you do, so shall he do" — as at the covenant\'s entry (Exod 24:5)'); ink('15:14', '"an offering made by fire, a pleasing aroma" — wholly for the LORD: a bird olah'); dat('the row convert_offering = %s' % data['convert_offering']['value']); move('Keritot 8b:18-9a:3; Mishnah Kinnim 1:1', 'a beast olah, or a bird pair both olot')
        return out("an olah (a beast) or a bird pair, both olot — as at the covenant's entry (Keritot 8b-9a; Mishnah Kinnim 1:1)", ['accepted'])
    if ask == 'entry':
        ink('15:15', '"as you are, so shall the stranger be"'); move('Keritot 9a:4 (Rabbi)', 'as your fathers — circumcision, immersion, the sprinkling of blood')
        return out('circumcision, immersion, the sprinkling of blood — as your fathers (Rabbi, Keritot 9a:4)', [FX.NONE])
    if ask == 'no_temple':
        ink('15:14', '"throughout your generations"'); move('Keritot 9a:10 (Rav Acha bar Yaakov)', 'converts accepted without a Temple — the offering waits')
        return out('accepted — "throughout your generations" (Rav Acha bar Yaakov)', ['accepted'])
    if ask == 'court':
        ink('15:16', '"one JUDGMENT for you and for the stranger"'); move('Yevamot 46b:16 (R. Yochanan)', 'a court of three')
        return out('3 — "one judgment" (R. Yochanan, Yevamot 46b)', [FX.NONE])
    if ask == 'one_law':
        f = [w for v in (15, 16, 29) for w in verse_text(15, v).split() if w in ('אחת', 'אחד')]
        ink('15:15-16, 15:29', '"one statute", "one Torah", "one judgment", "one Torah" — the formulas computed: %d' % len(f))
        return out('one statute, one Torah, one judgment — the formulas computed (15:15-16, 15:29)', [FX.NONE])
    if ask == 'congregation':
        dat('the row convert_congregation = %s' % data['convert_congregation']['value'])
        return out('converts are congregation (R. Yehuda); not (R. Yosei) — Kiddushin 73a', [FX.NONE])
    if ask == 'meal_offering':
        ink('15:14', '"as you do" — offerings whose blood is sprinkled'); move('Keritot 9a:2', 'a meal offering does not discharge the convert')
        return out('a meal offering does not discharge — the blood sprinkled (Keritot 9a:2)', ['disqualified'])
    if ask == 'quarter_dinar':
        dat('the row convert_offering — the quarter-dinar arm'); move('Keritot 9a:10', 'set aside for the pair; R. Shimon annulled it')
        return out('a quarter-dinar set aside for the pair — R. Shimon annulled it (Keritot 9a)', [FX.NONE])
    raise KeyError(ask)


# ===== F5: THE CHALLAH (Num 15:17-21) =======================================================================
FIVE_SPECIES = ('wheat', 'barley', 'spelt', 'oats', 'rye')
def challah(case, data):
    del P[:]
    ask = case['ask']
    if ask == 'species':
        ink('15:19', '"the bread of the land"'); move('Menachot 70b:2 (Reish Lakish); Mishnah Challah 1:1', '"bread" / "bread" with matza — the five grains')
        grain = case.get('grain')
        if grain is None:
            return out('5 — wheat, barley, spelt, oats, rye (Mishnah Challah 1:1; "bread"/"bread", Menachot 70b)', [FX.NONE])
        return out('liable — one of the five' if grain in FIVE_SPECIES else 'exempt — not of the five (rice, millet, pulse)', ['accepted'] if grain in FIVE_SPECIES else ['exempt'])
    if ask == 'entry_gate':
        ink('15:18', '"UPON YOUR COMING to the land" — varied from "when you come" (M-23 exemplar 12)'); move('Sifrei Bamidbar 110:1 (R. Yishmael)', 'liable from the entry itself, unlike the land-laws that wait for settlement')
        return out('from the entry itself — "upon your coming" varied (Sifrei 110:1; R. Yishmael)', [FX.NONE])
    if ask == 'all_of_you':
        ink('15:18', '"upon your coming" — all of you'); dat('the row challah_today = %s' % data['challah_today']['value']); move('Ketubot 25a:11; Niddah 47a:7', 'not two or three spies; Ezra\'s return partial')
        return out('all of you, not two or three spies — challah today rabbinic (Ketubot 25a; Niddah 47a)', [FX.NONE])
    if ask == 'minimum':
        ink('15:20', '"your dough" — the wilderness measure (Menachot 67a:6): the omer, a tenth of the ephah (Exod 16:36 — the parser\'s fraction)'); dat('the row challah_minimum = %s' % data['challah_minimum']['value'])
        return out('five quarters of flour — the wilderness omer, a tenth of the ephah (Mishnah Challah 2:6; Shabbat 15a; Tosefta Eduyot 1:1; Exod 16:36)', [FX.NONE])
    if ask == 'measure':
        who = case.get('who', 'householder'); impure = case.get('impure')
        dat('the row challah_measure = %s' % data['challah_measure']['value']); ink('15:20', 'no measure in the ink — the data channel\'s')
        m = Fraction(1, 24) if (impure == 'intentional' or (who == 'householder' and impure is None)) else Fraction(1, 48)
        return out(str(m), ['due_to_priest'])
    if ask == 'as_terumah':
        ink('15:20', '"as the terumah of the threshing floor so shall you lift it" — Numbers 18\'s terumah'); dat('the row terumah_measure = %s (OWED to Korach\'s compile)' % data['terumah_measure']['value']); move('Mishnah Challah 1:9', 'the terumah\'s laws on the challah')
        return out("the terumah's laws — death and a fifth, the priest's, 101 (Mishnah Challah 1:9); its measure 1/40, 1/50, 1/60 (Terumot 4:3) OWED to Numbers 18", ['due_to_priest'])
    if ask == 'owner':
        ink('15:20-21', '"your dough" twice'); move('Menachot 67a:6; Pesachim 38a:3', 'yours — not a gentile\'s, not consecrated')
        owner = case.get('owner', 'israelite')
        return out('yours — not a gentile\'s, not consecrated (Menachot 67a; Pesachim 38a)' if owner == 'israelite' else 'exempt — not your dough', ['accepted'] if owner == 'israelite' else ['exempt'])
    if ask == 'partners':
        ink('15:20', '"your dough" — the plural'); move('Chullin 135b:9 (R. Ilai concedes)', 'joint owners obligated')
        return out('liable — "your dough" plural (Chullin 135b)', ['accepted'])
    if ask == 'from_flour':
        ink('15:20', '"of your DOUGH"'); move('Kiddushin 46b:4; Mishnah Challah 2:5', 'from flour not challah; stolen in the priest\'s hand')
        return out("not challah — stolen in the priest's hand (Mishnah Challah 2:5)", ['disqualified'])
    if ask == 'outside_produce':
        dat('the row outside_produce = %s' % data['outside_produce']['value'])
        d = case.get('direction', 'in')
        return out('liable — brought into the land (Mishnah Challah 2:1)' if d == 'in' else 'R. Eliezer liable, R. Akiva exempt — taken out (Mishnah Challah 2:1)', ['accepted'] if d == 'in' else [FX.NONE])
    if ask == 'territories':
        ink('15:21', '"throughout your generations"'); dat('the row territories = %s' % data['territories']['value'])
        return out('three — to Chezib one; to the river two; beyond two, the measures reversed (Mishnah Challah 4:8)', [FX.NONE])
    if ask == 'sabbatical':
        ink('15:21', '"throughout your generations"'); move('Bekhorot 12b:11', 'sabbatical-year dough liable')
        return out('liable — throughout your generations (Bekhorot 12b)', ['accepted'])
    if ask == 'when_liable':
        move('Mishnah Challah 3:1-3', 'the rolling of wheat, the solid mass of barley; death by Heaven after')
        return out('the rolling (wheat) / the solid mass (barley); death by Heaven after (Mishnah Challah 3:1)', [FX.NONE])
    if ask == 'mixture':
        move('Mishnah Challah 3:7, 3:10; Zevachim 78a:7', 'wheat with rice — the taste of grain')
        return out('the taste of grain (Mishnah Challah 3:7, 3:10; Zevachim 78a)', [FX.NONE])
    if ask == 'joining':
        move('Mishnah Challah 2:4, 4:1-3', 'stuck together, one owner, one species; the basket (R. Eliezer)')
        return out('stuck together, one owner, one species; the basket (R. Eliezer) (Mishnah Challah 2:4, 4:1-3)', [FX.NONE])
    if ask == 'joining_species':
        move('Mishnah Challah 4:2', 'wheat with spelt only; barley with all but wheat')
        return out('wheat with spelt only; barley with all but wheat (Mishnah Challah 4:2)', [FX.NONE])
    if ask == 'gentile_dough':
        move('Mishnah Challah 3:5', 'a gentile\'s flour exempt; a gift before the rolling liable')
        return out("exempt — a gentile's; a gift before the rolling liable (Mishnah Challah 3:5)", ['exempt'])
    if ask == 'convert_dough':
        ink('15:14-16', 'one law for the stranger — at the dough'); move('Mishnah Challah 3:6', 'before conversion exempt, after liable, in doubt liable without the fifth')
        return out('before conversion exempt, after liable, in doubt liable without the fifth (Mishnah Challah 3:6)', [FX.NONE])
    if ask == 'dogs_dough':
        move('Mishnah Challah 1:8', 'if shepherds eat it')
        return out('liable if shepherds eat it (Mishnah Challah 1:8)', [FX.NONE])
    if ask == 'market':
        move('Mishnah Challah 1:6', 'the thanksgiving loaves for the market liable, for oneself exempt')
        return out('for the market liable, for oneself exempt — the thanksgiving loaves (Mishnah Challah 1:6)', [FX.NONE])
    if ask == 'liable_not_tithed':
        move('Mishnah Challah 1:3', 'gleanings, the forgotten sheaf, peah, ownerless, the first tithe, redeemed second tithe, the omer\'s remainder, grain under a third')
        return out("liable to challah, exempt from tithes — gleanings, the forgotten sheaf, peah, ownerless produce, the first tithe, redeemed second tithe, the omer's remainder (Mishnah Challah 1:3)", [FX.NONE])
    if ask == 'exempt_list':
        move('Mishnah Challah 1:4', 'rice, millet, poppy, sesame, pulse, under five quarters, sponge-cakes, honey-cakes, dumplings, a pan-cake, medumma')
        return out('exempt from challah — rice, millet, poppy, sesame, pulse, under five quarters, sponge-cakes, honey-cakes, dumplings, a pan-cake, medumma (Mishnah Challah 1:4)', ['exempt'])
    if ask == 'demai':
        move('Mishnah Challah 4:6', 'challah for demai from clean dough not near')
        return out('permitted from clean dough not near (Mishnah Challah 4:6)', [FX.NONE])
    if ask == 'clean_for_unclean':
        move('Mishnah Challah 2:8', 'R. Eliezer permits with the egg-size bridge; the sages forbid')
        return out('R. Eliezer permits (the egg bridge); the sages forbid (Mishnah Challah 2:8)', [FX.NONE])
    if ask == 'dough_word':
        ink('15:20-21', 'the dough-word twice here — %d spellings in the Tanakh: %s' % (len(DOUGH), DOUGH))
        return out('the dough-word four spellings in the Tanakh — two here, Ezekiel 44:30, Nehemiah 10:38 (computed)', [FX.NONE])
    raise KeyError(ask)


# ===== F6: THE ERROR (Num 15:22-29) =========================================================================
def error(case, data):
    del P[:]
    ask = case['ask']
    if ask == 'which_sin':
        ink('15:22', '"all these commandments" — the one commandment equal to them all'); move('Horayot 8a:20 (Rava / R. Yehoshua ben Levi); Sifrei Bamidbar 111:1', 'idolatry')
        return out('idolatry — "all these commandments" the one equal to all (Horayot 8a:20; Sifrei 111:1)', [FX.NONE])
    if ask == 'delta':
        d = (('העדה' in verse_text(15, 24), 'הקהל' in verse_text(4, 13, 'Lev')), ('לעלה' in verse_text(15, 24), 'לחטאת' in verse_text(4, 14, 'Lev')), ('ושעיר' in verse_text(15, 24), 'שעיר' not in verse_text(4, 14, 'Lev')))
        ink('15:24 against Lev 4:13-14', 'the three deltas on the ink: the congregation for the assembly %s; a burnt offering for the sin offering %s; a goat added %s' % d); move('Sifrei Bamidbar 111:1', 'the passage is idolatry\'s by the deltas')
        return out('three deltas against Lev 4:13-14 — the congregation for the assembly, a burnt offering for the sin offering, a goat added (computed on the ink)', [FX.NONE])
    if ask == 'communal':
        c = CH.court({'sin': 'idolatry'}); ink('15:24', '"one young bull for a burnt offering... one he-goat for a sin offering"'); dat('the chatat engine CALLED: court(idolatry) -> %s' % c['v'])
        return out('%s — a bull for a burnt offering and a goat for a sin offering (the chatat engine CALLED)' % c['v'], ['accepted'])
    if ask in ('individual', 'anointed', 'leader'):
        tier = {'individual': 'commoner', 'anointed': 'anointed', 'leader': 'leader'}[ask]
        c = CH.rank(tier, sin='idolatry'); ink('15:27', '"one soul... a she-goat of its first year"'); move('Mishnah Horayot 2:6; Horayot 7b:21, 8a:12', 'the individual, the king and the anointed all "one soul"'); dat('the chatat engine CALLED: rank(%s, idolatry) -> %s' % (tier, c['v']))
        return out('%s — "one soul" (Mishnah Horayot 2:6; the chatat engine CALLED)' % c['v'], ['accepted'])
    if ask == 'tribe_table':
        dat('the row tribe_table = %s' % data['tribe_table']['value']); move('Mishnah Horayot 1:5', 'R. Meir / R. Yehuda / R. Shimon — carried in the chatat engine')
        return out('R. Meir a bull and a goat; R. Yehuda twelve; R. Shimon thirteen (Mishnah Horayot 1:5 — the chatat engine carries the arms)', [FX.NONE])
    if ask == 'order':
        ink('15:24', '"for a sin offering" WITHOUT the aleph (%d in the Bible); "according to the ordinance"' % ONCE['לחטת']); move('Horayot 13a:4 (Rava bar Mari; Rava); Zevachim 90b:6 (Ravina)', 'the bull precedes the goat')
        return out('the bull then the goat — "for a sin offering" without its aleph; "according to the ordinance" (Horayot 13a; Zevachim 90b)', ['accepted'])
    if ask == 'aleph':
        ink('15:24', 'the aleph-less sin offering — once in the Bible (computed %d)' % ONCE['לחטת'])
        return out('once in the Bible — the sin offering without the aleph at 15:24 (computed)', [FX.NONE])
    if ask == 'goat_portions':
        ink('15:25', '"their sin offering... for their error"'); move('Zevachim 41a:8', 'the idolatry goats\' portions burned like the communal bull\'s')
        return out('burned like the communal bull\'s — "their sin offering... for their error" (Zevachim 41a)', ['accepted'])
    if ask == 'majority_manner':
        ink('15:26', '"for all the people it was unwitting"'); move('Horayot 2a:19 (Rava)', 'all unwitting in one manner')
        return out('all unwitting in one manner (Rava, Horayot 2a)', [FX.NONE])
    if ask == 'eyes':
        ink('15:24', '"from the eyes of the congregation" — the court'); move('Horayot 5a-8a; Taanit 24a:12', 'the leaders the eyes; "from the eyes" / "from the eyes" with Lev 4:13')
        return out('"from the eyes of the congregation" = the court; the leaders the eyes (Horayot; Taanit 24a)', [FX.NONE])
    if ask == 'partial':
        c = CH.court({'sin': 'idolatry', 'ruling': 'whole'}); move('Mishnah Horayot 1:3, 2:2', 'the whole essence abolished exempt; a part nullified liable — "one who bows without sacrificing is exempt"'); dat('the chatat engine CALLED: court(whole) -> %s' % c['v'])
        return out('%s — the whole essence abolished; a part nullified liable (Mishnah Horayot 1:3)' % c['v'], ['exempt'])
    if ask == 'reliance':
        c = CH.reliance({'knew_error': case.get('knew_error', False)}); move('Mishnah Horayot 1:1', 'the individual who relied on the court exempt; one who knew liable'); dat('the chatat engine CALLED: reliance -> %s' % c['v'])
        return out(c['v'], ['atoned_forgiven'] if c['v'] == 'liable' else ['exempt'])
    if ask == 'priest_own':
        ink('15:28', '"the priest shall atone for the soul that sins unwittingly"'); move('Menachot 74a:7, 109a:20 (Rav Nachman)', 'a priest atones through his own rite')
        return out('a priest atones through his own rite (Menachot 74a; 109a)', ['accepted'])
    if ask == 'idolatry_principle':
        dat('the row idolatry_principle = %s' % data['idolatry_principle']['value']); move('Mishnah Shabbat 7:1; Shabbat 68b-69a', 'the forgetter of the principle — one offering; Munbaz: prior knowledge')
        return out("one sin offering for the forgetter of the principle (Mishnah Shabbat 7:1's analogue); prior knowledge for both (Munbaz)", [FX.NONE])
    if ask == 'semikhah':
        dat('the row idolatry_goat_semikhah = %s' % data['idolatry_goat_semikhah']['value'])
        return out("the court's bull and the scapegoat; R. Shimon adds the idolatry goat (Mishnah Menachot 9:7)", [FX.NONE])
    if ask == 'class':
        c = CH.domain({'intent': 'intentional'}); ink('15:29-30', '"one Torah for the one who acts unwittingly... with a high hand... cut off"'); move('Horayot 8a:14 (R. Yehoshua ben Levi); Keritot 3a:20; Shabbat 69a:1', 'the whole Torah juxtaposed to idolatry — intentional karet, unwitting sin offering'); dat('the chatat engine CALLED: domain(intentional) -> %s' % c['v'])
        return out('%s — the whole Torah juxtaposed to idolatry: intentional karet, unwitting sin offering (Horayot 8a:14; Keritot 3a:20)' % c['v'], [FX.NONE])
    if ask == 'stranger_included':
        ink('15:26', '"and to the stranger who sojourns among them"')
        return out('the stranger forgiven with them (15:26)', ['atoned_forgiven'])
    if ask == 'thrice_unwitting':
        ink('15:27-29', '"in error" %d times — thrice fenced' % IN_ERROR)
        return out('"in error" thrice at 15:27-29 (computed)', [FX.NONE])
    raise KeyError(ask)


# ===== F7: THE HIGH HAND (Num 15:30-31) =====================================================================
def high_hand(case, data):
    del P[:]
    ask = case['ask']
    if ask == 'class':
        c = CH.domain({'intent': case.get('intent', 'intentional')}); ink('15:30', '"with a high hand... cut off"'); move('Horayot 8a:14; Keritot 3a:20; Mishnah Keritot 1:2', 'the karet class'); dat('the chatat engine CALLED: domain -> %s' % c['v'])
        return out(c['v'], ['karet_cut_off'] if c['v'] == 'karet_no_offering' else ['atoned_forgiven'])
    if ask == 'blasphemer_offering':
        ink('15:29', '"one law for him who DOES unwittingly" — no act, no offering'); dat('the row blasphemer_offering = %s' % data['blasphemer_offering']['value'])
        return out('none — no act (the Rabbis, Mishnah Keritot 1:2); an offering (R. Akiva, Keritot 7b)', ['exempt'])
    if ask == 'blasphemer_identity':
        ink('15:30', '"blasphemes the LORD" — %d in the Bible' % ONCE['מגדף']); dat('the row blasphemer_identity = %s' % data['blasphemer_identity']['value'])
        return out('the curser of the Name (the Rabbis); the idolater (R. Elazar ben Azarya)', [FX.NONE])
    if ask == 'blasphemes_once':
        ink('15:30', 'the participle once in the Bible (computed %d)' % ONCE['מגדף'])
        return out('once in the Bible — blasphemes (computed)', [FX.NONE])
    if ask == 'despiser':
        ink('15:31', '"despised the word of the LORD"'); dat('the row despiser = %s' % data['despiser']['value']); move('Sanhedrin 99a:17; 99b:4', 'not from Heaven; the Epicurean; Manasseh')
        return out('who says the Torah is not from Heaven; the Epicurean (Sanhedrin 99a); Manasseh the exemplar (99b)', [FX.NONE])
    if ask == 'karet_reading':
        ink('15:31', '"cut off, shall be cut off" — the doubled infinitive'); dat('the row karet_reading = %s' % data['karet_reading']['value']); move('Sanhedrin 64b:21-22; 90b:18', 'R. Akiva two worlds; R. Yishmael the language of men — THE FORK (MIDDOT.md)')
        return out('R. Akiva: this world and the next; R. Yishmael: the language of men (Sanhedrin 64b; 90b) — the fork', [FX.NONE])
    if ask == 'yoke':
        ink('15:31', '"despised the word... breached His commandment... cut off, shall be cut off"'); dat('the row yoke = %s' % data['yoke']['value']); move('Shevuot 13a:2 (Rabbi); Pirkei Avot 3:11', 'the yoke, the faces, the covenant; before and after Yom Kippur')
        return out('throws off the yoke / uncovers faces in the Torah; the covenant of circumcision; before and after Yom Kippur (Shevuot 13a; Pirkei Avot 3:11)', ['karet_cut_off'])
    if ask == 'iniquity_in_him':
        ink('15:31', '"his iniquity is in him"'); move('Sanhedrin 90b:16; Yoma 36b:5; Keritot 25b:16', 'after death — the World-to-Come; iniquities = intentional')
        return out('after death — the World-to-Come alluded (Sanhedrin 90b); intentional sins (Yoma 36b)', [FX.NONE])
    if ask == 'census':
        c = CH.karet_census(); dat('the chatat engine CALLED: karet_census -> %s' % c['v']); move('Mishnah Keritot 1:1', 'the thirty-six — the blasphemer and the idolater among them')
        return out('%d — the karet cases (Mishnah Keritot 1:1; the chatat engine CALLED)' % c['v'], [FX.NONE])
    if ask == 'high_hand_posture':
        ink('15:30', '"with a high hand" — Exod 14:8, Num 33:3 the exodus\'s posture'); move('Onkelos 15:30', '"with uncovered head"')
        return out('the exodus\'s posture — "with a high hand" (Exod 14:8; Num 33:3)', [FX.NONE])
    if ask == 'filthy_place':
        move('Berakhot 24b:20 (Rav Adda bar Ahava)', 'reciting in a filthy place — "despised the word"')
        return out('reciting in a filthy place — despised (Rav Adda bar Ahava)', [FX.NONE])
    if ask == 'own_body':
        move('Shabbat 153b:13 (Rava)', 'liable only for an act with his own body — the juxtaposition to idolatry')
        return out("liable only for an act with his own body — the Sabbath's application (Shabbat 153b)", [FX.NONE])
    raise KeyError(ask)
