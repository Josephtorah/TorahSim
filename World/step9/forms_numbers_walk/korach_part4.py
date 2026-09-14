
# ===== F5: THE TITHE (Num 18:20-32) ========================================================================
def the_tithe(case, data):
    del P[:]
    ask = case['ask']
    if ask == 'no_inheritance':
        ink('18:20', '"in their land you shall not inherit, and you shall have no portion among them; I am your portion and your inheritance"'); move('Onkelos Num 18:20', 'the gifts I have given you, they are your portion'); ink('18:23-24', '"among the children of Israel they shall inherit no inheritance" twice'); ink('Deut 10:9, 18:2; Josh 13:14; Ezek 44:28', 'the runs')
        return out('in their land you shall not inherit — I am your portion (18:20; Onkelos: the gifts I have given you); the Levites no inheritance (18:23-24); Deut 10:9, 18:2, Josh 13:14, Ezek 44:28', ['inheritance_barred'])
    if ask == 'exclusion_table':
        dat('the row exclusion_table = %s' % data['exclusion_table']['value']); move('Sifrei Bamidbar 119:1', 'the set carved from 26:53 by four clauses'); move('Mishnah Ma\'aser Sheni 5:14', 'R. Meir: priests and Levites do not confess; R. Yosei: the Levitical cities'); move('CALLED cold_run_zelophehad.inheritance_order(excluded) -> %r' % ZL_EXCL, 'the exclusion by sin beside')
        return out("priests (18:20), Levites (18:23), bondsmen and proselytes (26:55), the two of uncertain sex (26:54) — Sifrei 119:1; R. Meir: priests and Levites do not confess (Mishnah Ma'aser Sheni 5:14)", ['inheritance_barred'])
    if ask == 'tithe_to_levites':
        ink('18:21', '"all the tithe in Israel for an inheritance IN EXCHANGE for their service" — "in exchange" the Torah\'s two seats (18:21, 18:31)'); dat('the row levite_wage_condition = %s' % data['levite_wage_condition']['value']); move('Sifrei Bamidbar 119:5, 122:1', 'if he serves he takes; a Levite who refused one service has no portion')
        return out('all the tithe in Israel — in exchange for their service (18:21): the Levite serves, the Levite takes; a Levite who refused one service has no portion (Sifrei 119:5, 122:1)', ['tithe_granted'])
    if ask == 'tithe_recipient':
        dat('the row tithe_recipient = %s' % data['tithe_recipient']['value']); move('Yevamot 86b:1-2', 'R. Akiva: the Levites; R. Eliezer: the priests too'); move('Yevamot 86a-b', "Ezra's penalty")
        return out("the Levite (18:21, 18:26 — R. Akiva); the priest too — Ezra's penalty / the priests called Levites (R. Eliezer; Yevamot 86a-b)", ['tithe_granted'])
    if ask == 'third_year':
        move('Rosh Hashanah 12b:3', 'the first tithe juxtaposed to an inheritance — no interruption in the third year'); move('Sifrei Bamidbar 119:5', 'the tithe an inheritance — does not change its place')
        return out('the first tithe every year — juxtaposed to an inheritance (Rosh Hashanah 12b; Sifrei 119:5)', [FX.NONE])
    if ask == 'tithe_to_foreigners':
        move('Yevamot 86a:2', 'R. Meir: the tithe called terumah — forbidden to non-Levites; the Rabbis permit')
        return out('R. Meir: forbidden to non-Levites as terumah; the Rabbis permit (Yevamot 86a)', [FX.NONE])
    if ask == 'levite_he':
        ink('18:23', '"and the Levite, HE shall serve" — one seat'); move('Sifrei Bamidbar 119:5', 'perforce; in sabbatical and jubilee years; no priest in his stead — R. Nathan\'s a-fortiori refused')
        return out('the Levite — he: perforce, in sabbatical and jubilee years, no priest in his stead (Sifrei 119:5)', [FX.NONE])
    if ask == 'tithe_of_the_tithe':
        ink('18:26', '"you shall lift from it a terumah of the LORD, a tithe from the tithe" — one seat; Neh 10:39 the run'); dat('the arithmetic: %s x %s = %s' % (Fraction(1, 10), Fraction(1, 10), TITHE_OF_TITHE)); move('Menachot 54b:11; Beitzah 13b:3', 'one-tenth of the first tithe')
        return out('1/100 — a tenth of the tenth (18:26; Menachot 54b; Neh 10:39)', ['terumah_of_the_tithe_owed'])
    if ask == 'from_it':
        ink('18:26', '"from IT"'); move('Sifrei Bamidbar 120:1', 'kind for its kind, rooted for rooted, new for new, not across the border (Lev 27:30)'); move('Mishnah Terumot 1:5, 1:8-10; Mishnah Ma\'aser Sheni 5:11', 'the answer sheet\'s row — not the tithed tithe, not the exempt for the liable, not plucked for attached, not new for old, not the land\'s for outside')
        return out('from it — kind for its kind, rooted for rooted, new for new, not across the border (Sifrei 120:1; Mishnah Terumot 1:5); not the tithed tithe, not the exempt for the liable', [FX.NONE])
    if ask == 'mourner':
        move('Sifrei Bamidbar 120:1', '"from it" free (mufneh) for the mourner — the tithe and the paschal lamb'); move('Pesachim 36a; Yevamot 73b-74a; Mishnah Ma\'aser Sheni 5:12', '"not in my mourning"')
        return out("from it free for the mourner — the tithe and the paschal lamb (Sifrei 120:1; Pesachim 36a; Yevamot 73b); Mishnah Ma'aser Sheni 5:12", [FX.NONE])
    if ask == 'levite_preceded':
        ink('18:26', '"a tenth part of the tithe" — I said to you the tithe\'s terumah'); ink('18:29', '"from ALL that is given you" — the great terumah from the tithe too'); move('Berakhot 47a:15-47b:1; Beitzah 13b:6-7; Eruvin 31b:4-5; Pesachim 35b:6-7; Shabbat 127b:17-18 (R. Abbahu / Reish Lakish; Abaye to Rav Pappa)', 'on the stalks exempt from the great terumah; after the pile liable')
        return out("on the stalks — the tithe's terumah only; after the pile — the great terumah too (Berakhot 47a-b; Beitzah 13b; Eruvin 31b; Pesachim 35b; Shabbat 127b)", ['due_to_priest'])
    if ask == 'estimate':
        ink('18:27', '"and YOUR terumah shall be reckoned to you" — the plural'); move('Beitzah 13b:3; Bekhorot 58b:11, 59a:1; Menachot 54b:11 (Abba Elazar ben Gomel)', 'two terumot — by estimate and by thought; the tithes too (18:24\'s "terumah"), the animal tithe'); move('Sifrei Bamidbar 121:1', 'by estimate and by thought'); move('Mishnah Terumot 1:7, 4:6', 'never by measure; counting, measuring, weighing ranked')
        return out("by estimate and by thought — your terumah plural, two terumot (Abba Elazar ben Gomel: Beitzah 13b; Bekhorot 58b-59a; Sifrei 121:1); never by measure (Mishnah Terumot 1:7); the tithes too (18:24's terumah)", [FX.NONE])
    if ask == 'who_separates_tithe_terumah':
        move('Gittin 30b:13 (Abba Elazar ben Gamla)', 'the homeowner may separate the tithe\'s terumah from the Levite\'s tithe')
        return out('the Levite, and the owner too (Gittin 30b)', [FX.NONE])
    if ask == 'thresholds':
        ink('18:27, 18:30', '"as the grain of the threshing floor and as the fullness of the winepress" — the floor-word at %s' % [s for s in FLOOR_SEATS if s.startswith('Num')]); dat('the row tithe_thresholds = %s' % data['tithe_thresholds']['value']); move('Sifrei Bamidbar 121:1', 'from what is processed — the pile evened, the wine skimmed, the oil dripped'); move('Mishnah Ma\'aserot 1:5-8; Bava Metzia 88b:7; Mishnah Terumot 1:10', 'the answer sheet\'s thresholds; grain at the granary, olives and grapes at the house; the processed for the processed')
        return out("the pile evened, the wine skimmed, the oil dripped (Sifrei 121:1; Mishnah Ma'aserot 1:6-7); grain at the granary, olives and grapes at the house (Bava Metzia 88b); the processed for the processed (Terumot 1:10)", [FX.NONE])
    if ask == 'terumah_measure':
        ink('18:12, 18:29', '"the best of the oil..." / "from all its best" — NO MEASURE IN THE INK'); ink('15:20', '"as the terumah of the threshing floor" — the challah cell\'s pointer PAID at this cell'); dat('the row terumah_measure = %s (this runner\'s own; Shelach\'s copy the placeholder)' % data['terumah_measure']['value']); move('CALLED cold_run_naso.restitution(terumah_measure) -> %r [IMPORT, live call]' % NS_TM, 'the floor — Mishnah Terumot 4:5')
        return out('1/40, 1/50, 1/60 (Beit Shammai 1/30 — Mishnah Terumot 4:3); the floor: some must remain common (4:5 — naso\'s cell CALLED)', ['due_to_priest'])
    if ask == 'kind_for_kind':
        ink('18:12', '"the best of the oil, the best of the wine and the grain, THEIR first part"'); move('Mishnah Terumot 2:4; Bekhorot 53b:17, 54b:2; Temurah 5a:11', 'not one kind for another — not terumah; each type its own first')
        return out('not one kind for another — not terumah (Mishnah Terumot 2:4; Bekhorot 53b); the first part of them — each type its own (Bekhorot 54b; Temurah 5a)', [FX.NONE])
    if ask == 'the_best':
        ink('18:29-30, 18:32', '"from all its best, its hallowed part" / "when you lift its best" — Onkelos "its beauty"'); move('Sifrei Bamidbar 122:1', 'a warning to take only from the choicest'); move('Mishnah Terumot 2:4, 2:6', 'where a priest is, the best; where none, what lasts; the superior for the inferior, not the reverse')
        return out('from all its best (18:29-30, 18:32) — where a priest is, the best; where none, what lasts; the superior for the inferior, not the reverse (Mishnah Terumot 2:4, 2:6); a warning to take the choicest (Sifrei 122:1)', [FX.NONE])
    if ask == 'inferior_for_superior':
        ink('18:32', '"and you shall bear no sin by reason of it, when you lift its best from it" — a sin, so an effect'); move('Bava Batra 84b:2, 143a:6; Bava Metzia 56a:5; Kiddushin 46b:13; Temurah 5a:9 (R. Ilai)', 'valid terumah, a transgression that takes effect'); move('Yevamot 89b:2; Mishnah Terumot 2:2', 'the impure for the pure likewise — valid by Torah law, penalized')
        return out('valid terumah, a transgression that takes effect — you shall bear no sin (18:32; R. Ilai: Bava Batra 84b, 143a; Bava Metzia 56a; Kiddushin 46b; Temurah 5a); the impure for the pure likewise, penalized (Yevamot 89b; Terumot 2:2)', ['due_to_priest'])
    if ask == 'impure_for_pure':
        move('Mishnah Terumot 2:2; Yevamot 89b:2', 'not impure for pure — unwitting valid, intentional nothing; the Levite\'s unclean tithe likewise; R. Yehuda: if he knew, even in error nothing')
        return out('not impure for pure — unwitting valid, intentional nothing (Mishnah Terumot 2:2); terumah by Torah law, the Sages penalized (Yevamot 89b)', [FX.NONE])
    if ask == 'one_in_a_hundred':
        move('Sifrei Bamidbar 121:1', 'neutralized in a hundred and one — the last rendered clause before the translator stops'); move('CALLED cold_run_holiness_b.orlah(ratio)[the_priestly_gifts] -> %r [IMPORT, live call]' % HB_101, 'Mishnah Orlah 2:1'); move('Mishnah Terumot 4:7-13; Mishnah Challah 1:9', 'R. Eliezer 101; R. Yehoshua a hundred and more; the mixtures by kind')
        return out('neutralized in a hundred and one (Sifrei 121:1; Mishnah Terumot 4:7; Challah 1:9) — holiness_b CALLED: 101', [FX.NONE])
    if ask == 'what_remains_common':
        ink('18:30', '"it shall be reckoned to the Levites as the produce of the threshing floor and the produce of the winepress"'); move('Sifrei Bamidbar 122:1', 'what remains is common, as the floor\'s grain after terumah')
        return out("what remains is common, as the floor's grain after terumah (18:30; Sifrei 122:1)", [FX.NONE])
    if ask == 'every_place':
        ink('18:31', '"and you may eat it in EVERY PLACE" — Deut 12:13\'s ban the Torah twin'); dat('the row every_place = %s' % data['every_place']['value']); move('Sifrei Bamidbar 122:1', 'even a cemetery — the a-fortiori from terumah refused'); move('Yevamot 86b:2', 'R. Akiva: excludes the priest; R. Eliezer: any city')
        return out("in every place — even a cemetery (Sifrei 122:1; Yevamot 86b — R. Akiva: excludes the priest); Deut 12:13's ban the Torah twin", [FX.NONE])
    if ask == 'household_deputes':
        ink('18:31', '"you and your household"'); move('Yevamot 86a:9; Sifrei Bamidbar 122:1', 'the Israelite wife of a Levite may depute the separation')
        return out('you and your household — the Israelite wife of a Levite may depute the separation (18:31; Yevamot 86a; Sifrei 122:1)', [FX.NONE])
    if ask == 'wage':
        ink('18:31', '"for it is your WAGE in exchange for your service" — the wage-word\'s consonants the Nazirite\'s strong drink (6:3)'); move('Bekhorot 26b:18-19', 'terumah or tithe not given as wages to the assisting priests, Levites or poor — desecrated, "that you shall not die"')
        return out('it is your wage in exchange for your service (18:31); terumah or tithe not given as wages to the assisting priests, Levites or poor (Bekhorot 26b)', ['tithe_granted'])
    if ask == 'as_wages':
        move('Bekhorot 26b:18-19', 'forbidden, desecrated — the second verse adds the death')
        return out('forbidden, desecrated — that you shall not die (Bekhorot 26b)', [FX.NONE])
    if ask == 'agent':
        ink('18:28', '"so YOU ALSO shall lift the terumah of the LORD"'); move('Bava Metzia 22a:8; Kiddushin 41b:1; Mishnah Terumot 4:4', '"also" includes an agent, with the owner\'s knowledge; by the owner\'s mind, else 1/50'); move('Gittin 52a:3', '"you" — not partners, sharecroppers, stewards'); move('Bava Metzia 71b:10-12; Gittin 23b:4', 'members of the covenant — a gentile no')
        return out('you also — an agent, with the owner\'s knowledge; by the owner\'s mind, else 1/50; not partners, sharecroppers, stewards; a gentile no (Bava Metzia 22a, 71b; Kiddushin 41b; Gittin 23b, 52a; Mishnah Terumot 4:4)', [FX.NONE])
    if ask == 'agent_gentile':
        move('Bava Metzia 71b:10-12; Gittin 23b:4', 'as the appointers are members of the covenant so the agents')
        return out('a gentile cannot separate terumah even as an agent — members of the covenant (Bava Metzia 71b; Gittin 23b)', [FX.NONE])
    if ask == 'who_separates':
        move('Mishnah Terumot 1:1-3, 1:6', 'the five excluded; the five valid after the fact; the minor disputed')
        return out('not the deaf-mute, the imbecile, the minor, from what is not his, a gentile (Mishnah Terumot 1:1); the mute, the drunk, the naked, the blind — valid after the fact (1:6)', [FX.NONE])
    if ask == 'partners':
        ink('18:28', '"ALL YOUR tithes" — plural'); move('Chullin 136a:2', 'partners obligated; a gentile\'s partnership exempt')
        return out('partners liable — all your tithes (Chullin 136a); with a gentile exempt', [FX.NONE])
    if ask == 'gentile_tithe':
        ink('18:24, 18:26', '"the tithe of the children of Israel" / "from the children of Israel"'); move('Temurah 3a:9; Zevachim 45a:10', 'not gentiles\''); move('Bekhorot 11b:9 (R. Yehoshua ben Levi)', 'bought from a gentile in smoothed piles — exempt from the tithe\'s terumah')
        return out("the tithe of the children of Israel — not gentiles' (Temurah 3a; Zevachim 45a); bought from a gentile in piles — exempt from the tithe's terumah (Bekhorot 11b)", [FX.NONE])
    if ask == 'bought_from_gentile':
        move('Bekhorot 11b:9', '"from the children of Israel" — the gentile\'s piles exempt')
        return out("bought from a gentile in smoothed piles — exempt from the tithe's terumah (Bekhorot 11b)", [FX.NONE])
    if ask == 'wrong_order':
        ink('18:29', '"of all your tithes"'); move('Temurah 4b:3 (R. Avin)', 'tithed in the wrong order — rectified by the positive command, no lashes')
        return out('tithed in the wrong order — valid, rectified by the positive command, no lashes (Temurah 4b)', [FX.NONE])
    if ask == 'israelite_benefit_from_terumah':
        ink('18:27', '"YOUR terumah"'); move('Pesachim 23a:4 (Rav Pappa; Chizkiya)', 'an Israelite may benefit from terumah')
        return out('your terumah — an Israelite may benefit (Pesachim 23a)', [FX.NONE])
    if ask == 'tithe_terumah_betrothal':
        move('Kiddushin 53a:12', 'no "to the LORD" written of the tithe\'s terumah — betrothal with it valid')
        return out("betrothal with the tithe's terumah valid — no to the LORD written of it (Kiddushin 53a)", [FX.NONE])
    if ask == 'liable_produce':
        move('Mishnah Ma\'aserot 1:1-4', 'food, guarded, grown from the land; the ripening signs')
        return out("food, guarded, grown from the land (Mishnah Ma'aserot 1:1); the ripening signs (1:2-4)", [FX.NONE])
    if ask == 'removal':
        move('Mishnah Ma\'aser Sheni 5:6, 5:9', 'the removal on Passover eve of the fourth and seventh years — the first tithe to the Levite; Rabban Gamliel\'s ship')
        return out("the removal on Passover eve of the fourth and seventh years — the first tithe to the Levite (Mishnah Ma'aser Sheni 5:6); the recipients by office: Joshua the Levite, Elazar ben Azariah the priest (5:9)", [FX.NONE])
    if ask == 'recipients':
        move('Mishnah Ma\'aser Sheni 5:9', 'the tithe to Joshua the Levite; the poor\'s to Akiva; the tithe\'s terumah to Elazar ben Azariah the priest')
        return out("the Levite, the priest (the tithe's terumah), the poor — Rabban Gamliel's ship (Mishnah Ma'aser Sheni 5:9)", [FX.NONE])
    if ask == 'confession':
        move('Mishnah Ma\'aser Sheni 5:10-11', '"given to the Levite" = the first tithe; "also given" = terumah and the tithe\'s terumah; the exclusions on the confession\'s tongue')
        return out("given to the Levite = the first tithe; also given = terumah and the tithe's terumah (Mishnah Ma'aser Sheni 5:10-11); Deut 26's run", [FX.NONE])
    if ask == 'you_shall_not_die':
        ink('18:32', '"the holy things of the children of Israel you shall not profane, and you shall not die" — the priests\' words (Lev 8:35, 10:6-9; Joseph\'s Gen 42:20)'); move('Sifrei Bamidbar 122:1', 'the warning to Levites and Israelites both')
        return out("you shall not profane... and you shall not die (18:32) — the warning to Levites and Israelites both (Sifrei 122:1); the priests' words (Lev 8:35, 10:6-9)", [FX.NONE])
    if ask == 'so_you_too':
        ink('18:28', '"so YOU TOO shall lift"'); move('Sifrei Bamidbar 121:1', 'the priests separate too (or the Levites from their own — Yishmael\'s a-fortiori from challah); the three a-fortioris')
        return out('so you too — the priests separate too (Sifrei 121:1); the three a-fortioris', [FX.NONE])
    if ask == 'terumah_status':
        move('Mishnah Challah 1:9', 'challah and terumah alike — death and a fifth, forbidden to non-priests, the priest\'s property, nullified in a hundred and one, the hands, sunset, from the near and finished'); move('CALLED cold_run_priesthood.holy_food(stranger) -> %r [IMPORT, live call]' % PR_STRANGER, 'Lev 22:10\'s stranger')
        return out("death and a fifth, forbidden to non-priests, the priest's property, nullified in a hundred and one, the hands, sunset, from the near and finished (Mishnah Challah 1:9)", ['due_to_priest'])
    if ask == 'pointer_paid':
        ink('15:20 / 18:27, 18:30', 'the floor-word\'s seats %s — "as the terumah of the threshing floor" pointed forward at 15:20 and is paid at 18:27\'s "reckoned as the grain of the threshing floor" (computed)' % [s for s in FLOOR_SEATS if s.startswith('Num')])
        return out("15:20's as the terumah of the threshing floor is paid at 18:27's reckoned as the grain of the threshing floor (computed on the floor-word); the challah cell's as_terumah CALLS this cell", [FX.NONE])
    return out('no verdict in span', [FX.NONE])


# ---- THE WRAP — the daemon, the scene, the narrative ------------------------------------------------------
def law_korach(event, world):
    """Num 16:1-18:32 (cold_run_korach.py F1-F5). installed_by boot — the rebellion's lines are acts, the grants spoken at their verses to
    Aaron and the Levites; the stranger's ban at 17:5 an OUTPUT (rule_installed on the priesthood). Two one-day timers on an undated stretch."""
    k, src = event['kind'], event['case_source']
    E_ = lambda eff, s, cp=None, amount=None, due=None, law='', value=None: {'effect': eff, 'subject': s, 'counterparty': cp, 'amount': amount, 'due': due, 'value': value if value is not None else True, 'source_law': law, 'case_source': src}
    day = event.get('day', world.clock.day)      # THE SEQUENTIAL RUN: the event's own day
    if k == 'korach_gathered_against':
        return [E_('gathered_against', 'korach', cp='moses-and-aaron', value='and Korach took... two hundred and fifty princes; gathered against Moses and against Aaron: too much for you (16:1-3)', law='F1 [INK 16:1-3; Sanhedrin 109b:13]'),
                E_('gathered_against', 'dathan', cp='moses-and-aaron', value='sons of Eliab, of Reuben — with Korach (16:1)', law='F1 [INK 16:1]'),
                E_('gathered_against', 'abiram', cp='moses-and-aaron', value='sons of Eliab, of Reuben — with Korach (16:1)', law='F1 [INK 16:1]')]
    if k == 'moses_set_the_test':
        return [E_('commanded', 'korach', value='the_censers', law='F1 [INK 16:6-7 "take for yourselves censers... tomorrow" — the debit on Korach; CLOSED by 16:18]'),
                E_('censers_test_awaited', 'korach', due=day + 1, value="tomorrow (16:7, 16:16) — the court's date set (Moed Katan 16a:4); the undated stretch's morrow", law='F1 [INK 16:7; Moed Katan 16a:4]')]
    if k == 'levites_rebuked':
        return []                                  # the words are the line's value (16:8-11)
    if k == 'censers_commanded':
        return []                                  # the command restated (16:16-17)
    if k == 'separation_commanded':
        return []                                  # the threat the value (16:20-21)
    if k == 'dathan_and_abiram_refused':
        return [E_('refused', 'dathan', cp='moses', value='we will not go up (16:12, 16:14) — the summons refused, the report of disrespect (Moed Katan 16a:5)', law='F1 [INK 16:12-14]'),
                E_('refused', 'abiram', cp='moses', value='we will not go up (16:12, 16:14)', law='F1 [INK 16:12-14]')]
    if k == 'moses_swore':
        return [E_('plea_made', 'moses', cp='HEAVEN', value="do not turn to their offering; not one ass have I taken (16:15) — the Cain echo; Samuel's run (1 Sam 12:3)", law='F1 [INK 16:15; Nedarim 38a]')]
    if k == 'censers_offered_at_the_tent':
        world.close('korach', 'commanded', 'Num 16:18 — and they took each his censer and put fire on them and put incense on them', value='the_censers')
        return [E_('glory_appeared', 'the-tabernacle', cp='HEAVEN', value='the glory of the LORD appeared to all the congregation at the entrance of the tent of meeting (16:19) — the formula\'s third seat (Lev 9:23, Num 14:10)', law='F1 [INK 16:19]')]
    if k == 'moses_and_aaron_pleaded':
        return [E_('plea_made', 'moses', cp='HEAVEN', value='O God, God of the spirits of all flesh, shall one man sin and You be wroth with all the congregation (16:22)', law='F1 [INK 16:22; Num 27:16]'),
                E_('plea_made', 'aaron', cp='HEAVEN', value='shall one man sin (16:22) — the two on their faces', law='F1 [INK 16:22]')]
    if k == 'get_up_commanded':
        return [E_('commanded', 'israel', value='get_up_from_the_dwelling', law='F1 [INK 16:24 "get up from around the dwelling of Korach, Dathan and Abiram" — the debit on Israel; CLOSED by 16:27]')]
    if k == 'congregation_withdrew':
        world.close('israel', 'commanded', 'Num 16:27 — and they got up from around the dwelling of Korach, Dathan and Abiram', value='get_up_from_the_dwelling')
        return []
    if k == 'creation_test_declared':
        return [E_('test_set', 'israel', cp='moses', value='by this you shall know: if these die the common death — the LORD has not sent me; if the LORD creates a creation and the ground opens its mouth — these men have scorned the LORD (16:28-30)', law='F1 [INK 16:28-30; Sanhedrin 110a:16; Mishnah Avot 5:6]')]
    if k == 'earth_swallowed':
        return [E_('put_to_death', 'dathan', cp='HEAVEN', value='swallowed alive with his household — the ground split, the earth opened its mouth (16:31-33); Deut 11:6, Ps 106:17', law='F1 [INK 16:31-33]'),
                E_('put_to_death', 'abiram', cp='HEAVEN', value='swallowed alive with his household (16:31-33)', law='F1 [INK 16:31-33]'),
                E_('put_to_death', 'korach', cp='HEAVEN', value='OPEN — the row korach_death_mode: 16:32 names the men who belonged to Korach, 26:10 adds and Korach; R. Yochanan the plague, the baraita burned and swallowed (Sanhedrin 110a:13-14)', law='F1 [INK 16:32 against 26:10; the DATA row korach_death_mode]')]
    if k == 'fire_consumed_the_two_hundred_fifty':
        return [E_('put_to_death', 'the-two-hundred-fifty', cp='HEAVEN', amount=C250[2], value='fire from with the LORD consumed the two hundred and fifty who offered the incense (16:35) — the souls burned, the bodies intact (Sanhedrin 52a)', law='F1 [INK 16:35 — the definite numeral read 250]')]
    if k == 'censers_beaten_into_plates':
        return [E_('altar_plated', 'the-altar', value="the copper censers beaten into plates, a covering for the altar — for they became holy; a sign, a memorial (17:3-5); one elevates in sanctity (Menachot 99a)", law='F2 [INK 17:2-5; Menachot 99a:11]'),
                E_('rule_installed', 'the-priesthood', value='law_korach:stranger_incense', law='F2 [INK 17:5 "that no stranger who is not of Aaron\'s seed shall come near to burn incense... as the LORD spoke by the hand of Moses to him" — the OUTPUT installing the ban; Sanhedrin 110a:6 the ban on maintaining a dispute]')]
    if k == 'congregation_murmured_you_killed':
        return [E_('gathered_against', 'israel', cp='moses-and-aaron', value='you have killed the people of the LORD (17:6); gathered against Moses and against Aaron (17:7)', law='F2 [INK 17:6-7]'),
                E_('glory_appeared', 'the-tabernacle', cp='HEAVEN', value='the cloud covered it and the glory of the LORD appeared (17:7) — the formula\'s fourth seat', law='F2 [INK 17:7]')]
    if k == 'plague_begun_and_stayed':
        return [E_('plague_struck', 'israel', cp='HEAVEN', amount=PLAGUE, value='the wrath has gone out, the plague has begun (17:11) — the dead 14,700 besides the dead over the matter of Korach (17:14)', law='F2 [INK 17:11-14 — the parser\'s 14,700]'),
                E_('atoned_forgiven', 'israel', value='Aaron put the incense and atoned for the people (17:12) — incense atones for slander (Yoma 44a; Arakhin 16a)', law='F2 [INK 17:12; Yoma 44a:5]'),
                E_('plague_removed', 'israel', value='he stood between the dead and the living, and the plague was stayed (17:13, 17:15)', law='F2 [INK 17:13, 17:15; Shabbat 89a:2]')]
    if k == 'staffs_commanded':
        return [E_('commanded', 'moses', value='the_staffs', law='F2 [INK 17:16-20 "take from them a staff, a staff for a father\'s house... twelve staffs... lay them before the testimony" — the debit on Moses; CLOSED by 17:22]')]
    if k == 'staffs_laid_and_budded':
        world.close('moses', 'commanded', 'Num 17:22 — and Moses laid the staffs before the LORD in the tent of the testimony', value='the_staffs')
        return [E_('staff_budding_awaited', 'aarons-staff', due=day + 1, value='laid before the LORD (17:22); on the morrow (17:23) — the undated stretch\'s morrow', law='F2 [INK 17:22-23]'),
                E_('staff_budded', 'aarons-staff', value='the staff of Aaron for the house of Levi budded: a bud, a blossom (the frontplate\'s word), almonds (17:23); twelve staffs with Levi among them (17:21)', law='F2 [INK 17:21-24; Exod 28:36]')]
    if k == 'aarons_staff_kept':
        return [E_('kept_for_a_sign', 'aarons-staff', value="returned before the testimony for a keeping, for a sign to the sons of rebellion (17:25) — beside the manna jar (Exod 16:34); hidden with the ark, the jar and the oil (Horayot 12a; Keritot 5b; Yoma 52b)", law='F2 [INK 17:25-26; Keritot 5b:20]')]
    if k == 'congregation_despaired':
        return [E_('plea_made', 'israel', cp='moses', value='we expire, we perish, all of us perish; everyone who comes near dies (17:27-28) — Onkelos: the sword, the earth, the plague', law='F2 [INK 17:27-28]')]
    if k == 'watch_given_to_aaron':
        return [E_('watch_owed', 'aaron', value="the watch of the holy and the watch of the altar (18:5); the priests within, the Levites without — both they and you (18:3); the stranger who comes near shall be put to death (18:7 — the row zar_who_served by CALL: %s); no more wrath (18:5 = 1:53 + one token)" % ZAR['value'], law='F3 [INK 18:1-7; Sifrei 116:1-2]'),
                E_('watch_owed', 'the-levites', value='joined to you and keep the watch of the tent of meeting for all the service of the tent (18:2-4); not to the vessels of the holy nor to the altar (18:3); the song (Arakhin 11b); the priests above, the Levites below (Tamid 26b)', law='F3 [INK 18:2-4; Arakhin 11b:2]')]
    if k == 'gifts_granted':
        return [E_('priestly_dues_granted', 'aaron', value='the watch of My terumot — the twenty-four gifts, twelve in the sanctuary and twelve in the borders (18:8-18; Chullin 133b; Sifrei 119:1-2); for greatness (Onkelos)', law='F4 [INK 18:8-18; the DATA row the_twenty_four]'),
                E_('covenant_of_salt', 'aaron', value="a covenant of salt forever before the LORD, for you and your seed with you (18:19) — Aaron's and David's (2 Chr 13:5)", law='F4 [INK 18:19; Sifrei 119:5]')]
    if k == 'portion_declared':
        return [E_('inheritance_barred', 'aaron', value='in their land you shall not inherit, and you shall have no portion among them; I am your portion and your inheritance (18:20)', law='F5 [INK 18:20; Sifrei 119:1]'),
                E_('inheritance_barred', 'the-levites', value='among the children of Israel they shall inherit no inheritance (18:23-24)', law='F5 [INK 18:23-24]'),
                E_('tithe_granted', 'the-levites', value='all the tithe in Israel for an inheritance in exchange for their service (18:21, 18:24) — if he serves he takes (Sifrei 119:5)', law='F5 [INK 18:21; the DATA rows tithe_recipient, levite_wage_condition]')]
    if k == 'tithe_of_the_tithe_commanded':
        return [E_('terumah_of_the_tithe_owed', 'the-levites', cp='aaron', value='a terumah of the LORD from the tithe — a tenth of the tenth (18:26) = 1/100; from all its best (18:29); reckoned as the grain of the threshing floor (18:27 — 15:20\'s pointer paid); to Aaron the priest (18:28)', law='F5 [INK 18:25-32; Menachot 54b:11]')]
    # ---- the exam's case kinds: each names LITERALLY every effect it can write (2b's form — an unnamed effect is a KeyError to read) ----
    if k == 'korach_case':
        v, e, _ = rebellion({'ask': event['ask']}, DATA); L = 'F1 [%s]' % v; s_ = event['person']
        W = {'accepted': E_('accepted', s_, value=v, law=L), 'disqualified': E_('disqualified', s_, value=v, law=L), 'exempt': E_('exempt', s_, value=v, law=L), 'put_to_death': E_('put_to_death', s_, cp='HEAVEN', value=v, law=L), 'plea_made': E_('plea_made', s_, value=v, law=L)}
        return [W[x] for x in e if x != FX.NONE]
    if k == 'plague_staff_case':
        v, e, _ = plague_and_staffs({'ask': event['ask']}, DATA); L = 'F2 [%s]' % v; s_ = event['person']
        W = {'accepted': E_('accepted', s_, value=v, law=L), 'disqualified': E_('disqualified', s_, value=v, law=L), 'exempt': E_('exempt', s_, value=v, law=L), 'atoned_forgiven': E_('atoned_forgiven', s_, value=v, law=L), 'death_by_heaven': E_('death_by_heaven', s_, cp='HEAVEN', value=v, law=L),
             'altar_plated': E_('altar_plated', s_, value=v, law=L), 'rule_installed': E_('rule_installed', s_, value=v, law=L), 'plague_struck': E_('plague_struck', s_, cp='HEAVEN', value=v, law=L), 'staff_budded': E_('staff_budded', s_, value=v, law=L), 'kept_for_a_sign': E_('kept_for_a_sign', s_, value=v, law=L)}
        return [W[x] for x in e if x != FX.NONE]
    if k == 'watch_case':
        v, e, _ = the_watch({'ask': event['ask']}, DATA); L = 'F3 [%s]' % v; s_ = event['person']
        W = {'accepted': E_('accepted', s_, value=v, law=L), 'disqualified': E_('disqualified', s_, value=v, law=L), 'exempt': E_('exempt', s_, value=v, law=L), 'death_by_heaven': E_('death_by_heaven', s_, cp='HEAVEN', value=v, law=L), 'put_to_death': E_('put_to_death', s_, cp='HEAVEN', value=v, law=L),
             'watch_owed': E_('watch_owed', s_, value=v, law=L), 'stranger_barred': E_('stranger_barred', s_, value=v, law=L)}
        return [W[x] for x in e if x != FX.NONE]
    if k == 'stranger_service_case':
        v, e, _ = the_watch({'ask': event['ask']}, DATA); L = 'F3 [%s]' % v; s_ = event['person']
        W = {'accepted': E_('accepted', s_, value=v, law=L), 'disqualified': E_('disqualified', s_, value=v, law=L), 'exempt': E_('exempt', s_, value=v, law=L), 'death_by_heaven': E_('death_by_heaven', s_, cp='HEAVEN', value=v, law=L), 'put_to_death': E_('put_to_death', s_, cp='HEAVEN', value=v, law=L),
             'watch_owed': E_('watch_owed', s_, value=v, law=L), 'stranger_barred': E_('stranger_barred', s_, value=v, law=L)}
        return [W[x] for x in e if x != FX.NONE]
    if k == 'priestly_gifts_case':
        v, e, _ = the_gifts({'ask': event['ask']}, DATA); L = 'F4 [%s]' % v; s_ = event['person']
        W = {'accepted': E_('accepted', s_, value=v, law=L), 'disqualified': E_('disqualified', s_, value=v, law=L), 'exempt': E_('exempt', s_, value=v, law=L), 'due_to_priest': E_('due_to_priest', s_, cp='the-priest', value=v, law=L), 'consecrated_firstborn': E_('consecrated_firstborn', s_, value=v, law=L),
             'redeem_or_break': E_('redeem_or_break', s_, value=v, law=L), 'pays': E_('pays', s_, cp='the-priest', value=v, law=L), 'most_holy': E_('most_holy', s_, value=v, law=L), 'terumah_fed': E_('terumah_fed', s_, value=v, law=L), 'stranger_barred': E_('stranger_barred', s_, value=v, law=L),
             'consecrated': E_('consecrated', s_, value=v, law=L), 'priestly_dues_granted': E_('priestly_dues_granted', s_, value=v, law=L), 'covenant_of_salt': E_('covenant_of_salt', s_, value=v, law=L)}
        return [W[x] for x in e if x != FX.NONE]
    if k == 'tithe_case':
        v, e, _ = the_tithe({'ask': event['ask']}, DATA); L = 'F5 [%s]' % v; s_ = event['person']
        W = {'accepted': E_('accepted', s_, value=v, law=L), 'disqualified': E_('disqualified', s_, value=v, law=L), 'exempt': E_('exempt', s_, value=v, law=L), 'due_to_priest': E_('due_to_priest', s_, cp='the-priest', value=v, law=L), 'pays': E_('pays', s_, cp='the-priest', value=v, law=L),
             'inheritance_barred': E_('inheritance_barred', s_, value=v, law=L), 'tithe_granted': E_('tithe_granted', s_, value=v, law=L), 'terumah_of_the_tithe_owed': E_('terumah_of_the_tithe_owed', s_, cp='the-priest', value=v, law=L)}
        return [W[x] for x in e if x != FX.NONE]
    return []
