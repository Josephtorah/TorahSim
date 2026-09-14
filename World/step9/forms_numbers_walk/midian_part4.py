

# ---- THE WRAP — the daemon, the scene, the narrative ------------------------------------------------------
def law_midian(event, world):
    """Num 31:1-54 (cold_run_midian.py F1-F7). given_at Num 31:21; installed_by boot — THE THIRD RELAYED FORM (a statute in the PRIEST'S
    voice citing the LORD's command to Moses; the class named in the registry, the second pass decides). THIRTEEN TAPE LINES: the vengeance
    commanded (a DEBIT on Moses), the muster counted and the trumpets' debit CLOSED BY VALUE (a run by carrying), the war's receipt closing
    the two vengeance debits and writing NOTHING, the kings and Balaam slain, the captives / the spoil / the cities, Moses' wrath and THE
    SENTENCE (a debit OPEN forever — no narrated run), the purification's status and SIX TIMERS (chukat's dues on the men and on the
    captives), Eleazar's statute, the division's THREE DEBITS and their three receipts, the sixteen counted statuses on four thing parties,
    the two transfers, the officers' gold as the ransom at a count. The exam's six case kinds dispatch to the cells with LITERAL effects per
    kind (2b's form — an unnamed effect is a KeyError)."""
    k, src = event['kind'], event['case_source']
    E_ = lambda eff, s, cp=None, amount=None, due=None, law='', value=None: {'effect': eff, 'subject': s, 'counterparty': cp, 'amount': amount, 'due': due, 'value': value if value is not None else True, 'source_law': law, 'case_source': src}
    day = event.get('day', world.clock.day)      # THE SEQUENTIAL RUN: the event's own day
    # ---- the thirteen lines (page_order at the counter's day, no marker in the chapter) ----
    if k == 'midian_vengeance_commanded':
        return [E_('commanded', 'moses', value='avenge_the_midianites', law='F1 [INK 31:1-2 "avenge the vengeance of the children of Israel from THE MIDIANITES; afterward you shall be gathered to your people" — the debit on Moses beside the Balak runner\'s harass_the_midianites (25:17: the command and its run share the word); closed by value at 31:7\'s receipt]')]
    if k == 'midian_army_mustered':
        world.close('moses', 'commanded', 'Num 31:6 — the trumpets of the alarm in Phinehas\'s hand: 10:2\'s making implied by the run and never narrated — A RUN BY CARRYING; no sounding narrated, nothing written for the alarm (10:9\'s war clause the reference, BH.trumpets by CALL)', value='the_trumpets')
        return [E_('counted', 'the-men-of-war', value=MUSTER, law='F1 [INK 31:4-5 "a thousand to a tribe, a thousand to a tribe ... twelve thousand armed for the army" — 1,000 x 12 the ink\'s own product (the row muster_count: R. Yishmael\'s 24,000 recorded); Levi in (the row levi_in_the_muster); "delivered" (the row delivered_how); 31:6 Phinehas the priest anointed for war with the holy vessels (the row holy_vessels) and the trumpets]')]
    if k == 'midian_warred':
        world.close('israel', 'commanded', 'Num 31:7 — and they warred against Midian AS THE LORD COMMANDED MOSES: the receipt closes the Balak runner\'s harass_the_midianites (25:17) BY VALUE — the debit "OPEN to 31:7" in its own note', value='harass_the_midianites')
        world.close('moses', 'commanded', 'Num 31:7 — and they warred against Midian as the LORD commanded Moses: the receipt closes 31:2\'s avenge_the_midianites BY VALUE', value='avenge_the_midianites')
        return []                                                              # NO WRITE — the closes are the line's work (the register gate's 31:7 turns CLOSE)
    if k == 'kings_and_balaam_slain':
        return [E_('slain', 'the-kings-of-midian', cp='israel', value='%s — the five kings of Midian (31:8), Zur among them (Cozbi\'s father, 25:15; BK.DATA[cozbi_and_zur] = %s); Joshua 13:21 the RUN_CITATION' % (' '.join(KINGS_NAMES), DATA['cozbi_and_zur']['value']), law='F2 [INK 31:8 "and the kings of Midian they killed with their slain: Evi, Rekem, Zur, Hur and Reba, the five kings of Midian" — the parser\'s [5]; one party on the ledger]'),
                E_('slain', 'balaam', cp='israel', value=DATA['balaam_death']['value'], law='F2 [INK 31:8 "and Balaam son of Beor they killed with the sword" — BK.DATA[balaam_death] READ by CALL: come for his wages (Sanhedrin 106a:16), the four court modes recorded (106b:1); the ass\'s sword clause (22:29) a crown, no entry of its own]')]
    if k == 'captives_and_spoil_taken':
        return [E_('taken_captive', 'the-captives-of-midian', cp='israel', value='the women of Midian and their little ones (31:9)', law='F2 [INK 31:9 "and the children of Israel took captive the women of Midian and their little ones" — Lot\'s effect (Genesis 14); the sentence of 31:17-18 falls on this party]'),
                E_('spoil_taken', 'israel', cp='the-midianites', value='all their cattle, all their flocks and all their goods (31:9)', law='F2 [INK 31:9 "and all their cattle, and all their flocks, and all their goods they took as spoil" — Shechem\'s effect (Genesis 34); 31:11-12 the prey and the spoil brought to Moses at the plains of Moab]'),
                E_('burned_in_fire', 'the-midianites', value='all their cities in their dwellings and all their castles (31:10)', law='F2 [INK 31:10 "and all their cities in their dwellings and all their castles they burned with fire" — the row castles_reading (Onkelos\' houses of worship); the Midianites a counterparty until now, written on here]')]
    if k == 'moses_wroth_at_the_officers':
        return [E_('mark_of_anger', 'moses', cp='the-officers-of-the-host', value='and Moses was wroth with the officers of the host (31:14) — ANGER BEGETS ERROR: the statute in Eleazar\'s mouth at 31:21 (Sifrei 157:9; Pesachim 66b:7)', law='F3 [INK 31:14 — the wrath-verb with Moses as subject at three Torah seats (the row anger_seats); MOVE Sifrei 157:9 "in the name of its sayer" (Megillah 15a:20)]'),
                E_('commanded', 'the-officers-of-the-host', value='the_sentence_on_the_captives', law='F3 [INK 31:17-18 "now kill every male among the little ones, and every woman who has known a man by lying with a male kill; and all the little ones among the women who have not known a man by lying with a male keep alive for yourselves" — A COMMAND WITH NO NARRATED RUN: OPEN forever; 31:35 names the outcome ("the women who had not known a man", 32,000) and never the killing; the rows known_a_man_test, frontplate_test, proselyte_age, punish_by_inference]')]
    if k == 'warriors_purification_commanded':
        return [E_('sent_outside_the_camp', 'the-men-of-war', value='encamp outside the camp seven days (31:19) — the corpse-impure out of the Presence\'s camp alone (CK.corpse_tumah camps by CALL)', law='F4 [INK 31:19 "and you, encamp outside the camp seven days: whoever has killed a soul and whoever has touched a slain one" — Miriam\'s seven at 12:15 the phrase\'s other seat]'),
                E_('corpse_unclean_seven_days', 'the-men-of-war', amount=SEVEN, due=day + SEVEN, value='unclean seven days — whoever has killed a soul, whoever has touched a slain one (31:19); the sword like the slain (the row sword_like_slain)', law='F4 [INK 31:19; CK.corpse_tumah(seven_days) by CALL — the TIMER due day + 7, chukat\'s own due]'),
                E_('sprinkling_due_third_day', 'the-men-of-war', due=day + THIRD_DUE, value='purify yourselves on the third day (31:19)', law='F4 [INK 31:19 "on the third day and on the seventh day" — 19:12, 19:19\'s schedule; CK.corpse_tumah(schedule) by CALL — the TIMER due day + 3]'),
                E_('sprinkling_due_seventh_day', 'the-men-of-war', due=day + SEVENTH_DUE, value='purify yourselves on the seventh day; wash your garments on the seventh day and be clean, afterward come into the camp (31:19, 31:24)', law='F4 [INK 31:19, 31:24 — the row camp_entry_reading (Sifrei 158:3); CK.corpse_tumah(schedule) by CALL — the TIMER due day + 7]'),
                E_('corpse_unclean_seven_days', 'the-captives-of-midian', amount=SEVEN, due=day + SEVEN, value='you AND YOUR CAPTIVES (31:19) — the gentile\'s corpse defiles by touch and carrying, not by tent (the row tent_gentile; Yevamot 61a:5 the Midian war)', law='F4 [INK 31:19 "you and your captives" — CK.DATA[tent_gentile] READ by CALL; the TIMER due day + 7]'),
                E_('sprinkling_due_third_day', 'the-captives-of-midian', due=day + THIRD_DUE, value='the captives sprinkled on the third day (31:19)', law='F4 [INK 31:19 — CK.corpse_tumah(schedule) by CALL; the TIMER due day + 3]'),
                E_('sprinkling_due_seventh_day', 'the-captives-of-midian', due=day + SEVENTH_DUE, value='the captives sprinkled on the seventh day (31:19)', law='F4 [INK 31:19 — CK.corpse_tumah(schedule) by CALL; the TIMER due day + 7]')]
    if k == 'vessels_statute_spoken':
        return [E_('commanded', 'the-men-of-war', value='the_statute_of_the_vessels — Num 31:21-23', law='F5 [INK 31:21-23 "and Eleazar the priest said to the men of war who had gone to the battle: this is the statute of the Torah which the LORD commanded Moses — the gold, the silver, the bronze, the iron, the tin and the lead: everything that comes into the fire you shall pass through the fire and it shall be clean, only with the water of sprinkling it shall be purified; and everything that does not come into the fire you shall pass through water" — THE THIRD RELAYED FORM (installed_by boot, the class named); the rows kashering_modes, immersion_source; 31:20\'s four materials against Leviticus 11:32\'s (the edge shemini, a transfer taught)]')]
    if k == 'prey_division_commanded':
        return [E_('commanded', 'moses', value='divide_the_prey', law='F6 [INK 31:26-27 "take the sum of the prey of the captives, of man and of beast, you and Eleazar the priest and the heads of the fathers\' houses of the congregation; and halve the prey between those who took the war, who went out to the army, and all the congregation" — "lift the head" the census idiom (IS.shekel by CALL); the equal halves; closed by value at 31:31]'),
                E_('commanded', 'moses', value='the_tribute_to_the_priest', law='F6 [INK 31:28-29 "and levy a tribute to the LORD from the men of war who went out to the army: ONE SOUL OF FIVE HUNDRED, of the persons, the cattle, the donkeys and the flock; from their half you shall take it and give it to Eleazar the priest, the LORD\'s heave-offering" — THE RATE Fraction(1, 500), the parser\'s ratio class; the row tribute_rate_reading; closed by value at 31:41]'),
                E_('commanded', 'moses', value='the_levites_share', law='F6 [INK 31:30 "and from the half of the children of Israel you shall take ONE HELD OF FIFTY, of the persons, the cattle, the donkeys and the flock, of all the beasts, and give them to the Levites who keep the charge of the tabernacle of the LORD" — THE RATE Fraction(1, 50); 1:53\'s charge (BM.charges by CALL); the row levites_rate_reading (the terumah\'s average, a transfer taught); closed by value at 31:47]')]
    if k == 'prey_counted':
        world.close('moses', 'commanded', 'Num 31:31 — and Moses and Eleazar the priest did as the LORD commanded Moses: the count and the halving run (31:32-36)', value='divide_the_prey')
        return [E_('counted', 'the-prey', value=TOTALS[0], law='F6 [INK 31:32 "and the prey, the rest of the plunder which the people of the army took, was: sheep six hundred and seventy-five thousand" — the parser\'s 675,000; the thing party the ink\'s own noun (המלקוח "the prey", four seats)]'),
                E_('counted', 'the-prey', value=TOTALS[1], law='F6 [INK 31:33 "and cattle seventy-two thousand" — the parser\'s 72,000]'),
                E_('counted', 'the-prey', value=TOTALS[2], law='F6 [INK 31:34 "and donkeys sixty-one thousand" — the parser\'s 61,000]'),
                E_('counted', 'the-prey', value=TOTALS[3], law='F6 [INK 31:35 "and the persons, of the women who had not known a man by lying with a male, all the souls thirty-two thousand" — the parser\'s 32,000; the sentence\'s outcome described, its run never narrated; THE REGISTER GATE\'s count line 31:35 turns LEDGER by this status]')]
    if k == 'tribute_given':
        world.close('moses', 'commanded', 'Num 31:41 — and Moses gave the tribute, the LORD\'s heave-offering, to Eleazar the priest, as the LORD commanded Moses: the transfer run', value='the_tribute_to_the_priest')
        return [E_('counted', 'the-warriors-portion', value=WARRIORS[0], law='F6 [INK 31:36 "and the half, the portion of those who went out to the army, was: the number of the sheep three hundred and thirty-seven thousand five hundred" — the parser\'s 337,500 = 675,000 / 2 CHECK; the register gate\'s count line 31:36 LEDGER]'),
                E_('counted', 'the-warriors-portion', value=WARRIORS[1], law='F6 [INK 31:38 "and the cattle thirty-six thousand" — 72,000 / 2 CHECK]'),
                E_('counted', 'the-warriors-portion', value=WARRIORS[2], law='F6 [INK 31:39 "and the donkeys thirty thousand five hundred" — 61,000 / 2 CHECK]'),
                E_('counted', 'the-warriors-portion', value=WARRIORS[3], law='F6 [INK 31:40 "and the persons sixteen thousand" — 32,000 / 2 CHECK; the register gate\'s count line 31:40 LEDGER]'),
                E_('counted', 'the-tribute', value=TRIBUTE[0], law='F6 [INK 31:37 "and the tribute to the LORD of the sheep was six hundred and seventy-five" — 337,500 x 1/500 CHECK]'),
                E_('counted', 'the-tribute', value=TRIBUTE[1], law='F6 [INK 31:38 "and their tribute to the LORD seventy-two" — 36,000 x 1/500 CHECK]'),
                E_('counted', 'the-tribute', value=TRIBUTE[2], law='F6 [INK 31:39 "and their tribute to the LORD sixty-one" — 30,500 x 1/500 CHECK]'),
                E_('counted', 'the-tribute', value=TRIBUTE[3], law='F6 [INK 31:40 "and their tribute to the LORD thirty-two souls" — 16,000 x 1/500 CHECK; the tribute 840 heads in all]'),
                E_('heave_offering_given', 'eleazar', cp='the-tribute', amount=sum(TRIBUTE), value='the tribute, the LORD\'s heave-offering — 675 sheep, 72 cattle, 61 donkeys, 32 persons: 840 heads (31:37-41)', law='F6 [INK 31:41 "and Moses gave the tribute, the LORD\'s heave-offering, to Eleazar the priest, as the LORD commanded Moses" — the TRANSFER; "the LORD\'s heave-offering" the half-shekel\'s phrase (eleven seats); the row tribute_rate_reading (Menachot 77b:20: not for all generations)]')]
    if k == 'levites_portion_given':
        world.close('moses', 'commanded', 'Num 31:47 — and Moses took from the half of the children of Israel the held one of fifty, of man and of beast, and gave them to the Levites who keep the charge of the tabernacle of the LORD, as the LORD commanded Moses: the transfer run', value='the_levites_share')
        return [E_('counted', 'the-congregations-half', value=CONGREGATION[0], law='F6 [INK 31:43 "and the half of the congregation was: of the sheep three hundred and thirty-seven thousand five hundred" — = the warriors\' portion CHECK (מחצת העדה "the half of the congregation", one seat)]'),
                E_('counted', 'the-congregations-half', value=CONGREGATION[1], law='F6 [INK 31:44 "and cattle thirty-six thousand" — CHECK]'),
                E_('counted', 'the-congregations-half', value=CONGREGATION[2], law='F6 [INK 31:45 "and donkeys thirty thousand five hundred" — CHECK]'),
                E_('counted', 'the-congregations-half', value=CONGREGATION[3], law='F6 [INK 31:46 "and the persons sixteen thousand" — CHECK; the register gate\'s count line 31:46 LEDGER]'),
                E_('levites_portion_given', 'the-levites', cp='the-congregations-half', amount=sum(LEVITES), value='one held of fifty of the congregation\'s half — %d / %d / %d / %d = %d heads COMPUTED, UNWRITTEN (31:47); ten times the priest\'s 840' % (LEVITES + (sum(LEVITES),)), law='F6 [INK 31:47 "and Moses took from the half of the children of Israel the held one of fifty, of man and of beast, and gave them to the Levites who keep the charge of the tabernacle of the LORD, as the LORD commanded Moses" — the TRANSFER; THE SHARE STATED AS A RATE AND NEVER AS A NUMBER: the value the runner\'s arithmetic; the row levites_rate_reading (the terumah\'s average — Jerusalem Talmud Terumot 4:3:2)]')]
    if k == 'officers_gold_brought':
        return [E_('no_plague_at_counting', 'the-men-of-war', value='your servants have lifted the head of the men of war under our hand, and not one man of us is missing (31:49)', law='F7 [INK 31:48-49 — the officers of thousands and of hundreds (Jethro\'s grades, Exodus 18:21); "lift the head" Exodus 30:12\'s idiom; the shekel engine\'s clause (IS.shekel(plague_clause) by CALL); the row atonement_reading (the moral count, Yevamot 61a:4)]'),
                E_('atoned_forgiven', 'the-officers-of-the-host', cp='HEAVEN', value='we have brought the LORD\'s offering, every man what he found, vessels of gold — the armlet, the bracelet, the ring, the earring and the kumaz — to atone for our souls before the LORD (31:50): the ransom of Exodus 30 run at a count', law='F7 [INK 31:50 — "to atone for our souls" / Exodus 30:15-16\'s "to atone for your souls" (IS.shekel(atone_souls) by CALL); the rows ornaments_reading (Shabbat 64a:20-21) and atonement_reading (the eyes\' thoughts, Shabbat 64a:22-64b:2)]'),
                E_('memorial_before_the_lord', 'israel', value=GOLD, law='F7 [INK 31:52-54 "all the gold of the heave-offering which they offered to the LORD was sixteen thousand seven hundred and fifty shekels ... and Moses and Eleazar the priest took the gold ... and brought it into the tent of meeting, a memorial for the children of Israel before the LORD" — the parser\'s 16,750; Exodus 30:16\'s six words in another order; the LORD\'s offering to the tent, not the altar (Temurah 13a:14); 31:53 the private plunder outside the count]')]
    # ---- the exam's case kinds: each names LITERALLY every effect it can write (2b's form) ----
    if k == 'midian_war_case':
        fn = the_war if event.get('cell') == 'war' else the_vengeance
        v, e, _ = fn(dict(event, ask=event['ask']), DATA); L = '%s [%s]' % ('F2' if event.get('cell') == 'war' else 'F1', v); s_ = event['person']
        W = {'commanded': E_('commanded', s_, value=v, law=L), 'counted': E_('counted', s_, value=v, law=L), 'slain': E_('slain', s_, cp='israel', value=v, law=L), 'accepted': E_('accepted', s_, value=v, law=L), 'exempt': E_('exempt', s_, value=v, law=L)}
        return [W[x] for x in e if x != FX.NONE]
    if k == 'captive_sentence_case':
        v, e, _ = the_sentence(dict(event, ask=event['ask']), DATA); L = 'F3 [%s]' % v; s_ = event['person']
        W = {'commanded': E_('commanded', s_, value=v, law=L), 'mark_of_anger': E_('mark_of_anger', s_, cp='the-officers-of-the-host', value=v, law=L), 'accepted': E_('accepted', s_, value=v, law=L), 'exempt': E_('exempt', s_, value=v, law=L)}
        return [W[x] for x in e if x != FX.NONE]
    if k == 'warriors_purification_case':
        v, e, _ = the_purification(dict(event, ask=event['ask']), DATA); L = 'F4 [%s]' % v; s_ = event['person']
        W = {'sent_outside_the_camp': E_('sent_outside_the_camp', s_, value=v, law=L),
             'corpse_unclean_seven_days': E_('corpse_unclean_seven_days', s_, amount=SEVEN, due=day + SEVEN, value=v, law=L),               # the TIMERS: chukat's dues (the machine counts the days that pass)
             'sprinkling_due_third_day': E_('sprinkling_due_third_day', s_, due=day + THIRD_DUE, value=v, law=L), 'sprinkling_due_seventh_day': E_('sprinkling_due_seventh_day', s_, due=day + SEVENTH_DUE, value=v, law=L),
             'declared_pure': E_('declared_pure', s_, value=v, law=L), 'accepted': E_('accepted', s_, value=v, law=L), 'exempt': E_('exempt', s_, value=v, law=L)}
        return [W[x] for x in e if x != FX.NONE]
    if k == 'vessel_of_war_case':
        v, e, _ = the_vessels(dict(event, ask=event['ask']), DATA); L = 'F5 [%s]' % v; s_ = event['person']
        W = {'declared_pure': E_('declared_pure', s_, value=v, law=L), 'immersed': E_('immersed', s_, value=v, law=L), 'accepted': E_('accepted', s_, value=v, law=L), 'exempt': E_('exempt', s_, value=v, law=L)}
        return [W[x] for x in e if x != FX.NONE]
    if k == 'prey_division_case':
        v, e, _ = the_division(dict(event, ask=event['ask']), DATA); L = 'F6 [%s]' % v; s_ = event['person']
        W = {'counted': E_('counted', s_, value=v, law=L), 'heave_offering_given': E_('heave_offering_given', s_, cp='the-tribute', value=v, law=L), 'levites_portion_given': E_('levites_portion_given', s_, cp='the-congregations-half', value=v, law=L), 'accepted': E_('accepted', s_, value=v, law=L), 'exempt': E_('exempt', s_, value=v, law=L)}
        return [W[x] for x in e if x != FX.NONE]
    if k == 'officers_gold_case':
        v, e, _ = the_gold(dict(event, ask=event['ask']), DATA); L = 'F7 [%s]' % v; s_ = event['person']
        W = {'no_plague_at_counting': E_('no_plague_at_counting', s_, value=v, law=L), 'atoned_forgiven': E_('atoned_forgiven', s_, cp='HEAVEN', value=v, law=L), 'memorial_before_the_lord': E_('memorial_before_the_lord', s_, value=v, law=L), 'accepted': E_('accepted', s_, value=v, law=L), 'exempt': E_('exempt', s_, value=v, law=L)}
        return [W[x] for x in e if x != FX.NONE]
    return []


LINES = [
    ('Num 31:1-2 — and the LORD spoke to Moses, saying: avenge the vengeance of the children of Israel from the Midianites; afterward you shall be gathered to your people', 'moses'),
    ('Num 31:3-6 — and Moses spoke to the people: arm men from among you for the army ... a thousand to a tribe ... and there were delivered from the thousands of Israel a thousand to a tribe, twelve thousand armed for the army; and Moses sent them, and Phinehas son of Eleazar the priest, with the holy vessels and the trumpets of the alarm in his hand', 'israel'),
    ('Num 31:7 — and they warred against Midian as the LORD commanded Moses, and they killed every male', 'israel'),
    ('Num 31:8 — and the kings of Midian they killed with their slain: Evi, Rekem, Zur, Hur and Reba, the five kings of Midian; and Balaam son of Beor they killed with the sword', 'israel'),
    ('Num 31:9-12 — and the children of Israel took captive the women of Midian and their little ones, and all their cattle, and all their flocks, and all their goods they took as spoil; and all their cities in their dwellings and all their castles they burned with fire; and they brought the captives, the prey and the spoil to Moses and to Eleazar the priest and to the congregation, at the plains of Moab by the Jordan at Jericho', 'israel'),
    ('Num 31:13-18 — and Moses was wroth with the officers of the host ... have you kept every female alive? ... now kill every male among the little ones, and every woman who has known a man by lying with a male kill; and all the little ones among the women who have not known a man by lying with a male keep alive for yourselves', 'moses'),
    ('Num 31:19-20 — and you, encamp outside the camp seven days: whoever has killed a soul and whoever has touched a slain one, purify yourselves on the third day and on the seventh day, you and your captives; and every garment, every vessel of skin, every work of goats and every vessel of wood you shall purify', 'moses'),
    ('Num 31:21-24 — and Eleazar the priest said to the men of war who had gone to the battle: this is the statute of the Torah which the LORD commanded Moses: the gold, the silver, the bronze, the iron, the tin and the lead — everything that comes into the fire you shall pass through the fire and it shall be clean, only with the water of sprinkling it shall be purified; and everything that does not come into the fire you shall pass through water; and wash your garments on the seventh day and be clean, and afterward come into the camp', 'eleazar'),
    ('Num 31:25-30 — and the LORD spoke to Moses: take the sum of the prey of the captives ... and halve the prey between those who took the war and all the congregation; and levy a tribute to the LORD from the men of war: one soul of five hundred ... and give it to Eleazar the priest, the heave-offering of the LORD; and from the half of the children of Israel take one held of fifty ... and give them to the Levites who keep the charge of the tabernacle of the LORD', 'moses'),
    ('Num 31:31-35 — and Moses and Eleazar the priest did as the LORD commanded Moses; and the prey, the rest of the plunder, was: sheep six hundred and seventy-five thousand, cattle seventy-two thousand, donkeys sixty-one thousand, and the persons, of the women who had not known a man, thirty-two thousand', 'moses'),
    ('Num 31:36-41 — and the half, the portion of those who went out to the army, was: sheep three hundred and thirty-seven thousand five hundred, and the tribute to the LORD six hundred and seventy-five; cattle thirty-six thousand, their tribute seventy-two; donkeys thirty thousand five hundred, their tribute sixty-one; persons sixteen thousand, their tribute thirty-two souls; and Moses gave the tribute, the heave-offering of the LORD, to Eleazar the priest, as the LORD commanded Moses', 'moses'),
    ('Num 31:42-47 — and from the half of the children of Israel, which Moses halved from the men of the army: the half of the congregation was sheep three hundred and thirty-seven thousand five hundred, cattle thirty-six thousand, donkeys thirty thousand five hundred, persons sixteen thousand; and Moses took from the half of the children of Israel the held one of fifty, of man and of beast, and gave them to the Levites who keep the charge of the tabernacle of the LORD, as the LORD commanded Moses', 'moses'),
    ('Num 31:48-54 — and the officers over the thousands of the army came near to Moses: your servants have lifted the head of the men of war under our hand, and not one man of us is missing; and we have brought the offering of the LORD, every man what he found, vessels of gold — the armlet, the bracelet, the ring, the earring and the kumaz — to atone for our souls before the LORD; and all the gold of the heave-offering was sixteen thousand seven hundred and fifty shekels; the men of the host had taken spoil every man for himself; and Moses and Eleazar the priest took the gold and brought it into the tent of meeting, a memorial for the children of Israel before the LORD', 'the-officers-of-the-host'),
]
CLOSES = 'six — the trumpets (31:6, by carrying), the two vengeance debits (31:7), the division (31:31), the tribute (31:41), the Levites\' share (31:47); the sentence on the captives OPEN forever'


def scene():
    """THE SCENE — the exam's rows replayed on the world engine (the exodus epoch): the exam's persons through the six case kinds, the
    clock advanced seven days to fire the purification's timers."""
    with contextlib.redirect_stdout(io.StringIO()):
        w = WE.World(era='Num 31:1-54: Mishnah Avodah Zarah 5:12, Kelim 11:1, Terumot 4:3 and the sugyot on the engine (the exodus epoch)', epoch='exodus')
        w.laws = [law_midian]
        w.advance(w.clock.day_in('exodus', 40, 6, 1))
        # ---- the exam's persons through the six case kinds (LITERAL submits — the daemon gate parses no loop) ----
        w.submit({'kind': 'midian_war_case', 'subject': 'the-muster', 'person': 'the-muster', 'ask': 'muster', 'case_source': 'Num 31:4-5 — the exam\'s row muster'})
        w.submit({'kind': 'midian_war_case', 'subject': 'the-moab-question', 'person': 'the-moab-question', 'ask': 'moab_spared', 'case_source': 'Bava Kamma 38a:16 — the exam\'s row moab_spared'})
        w.submit({'kind': 'midian_war_case', 'subject': 'the-anointed-priest', 'person': 'the-anointed-priest', 'ask': 'phinehas_anointed_for_war', 'case_source': 'Sotah 43a:1 — the exam\'s row phinehas_anointed_for_war'})
        w.submit({'kind': 'midian_war_case', 'subject': 'the-five-kings-slain', 'person': 'the-five-kings-slain', 'cell': 'war', 'ask': 'five_kings', 'case_source': 'Num 31:8 — the exam\'s row five_kings'})
        w.submit({'kind': 'midian_war_case', 'subject': 'the-diviner', 'person': 'the-diviner', 'cell': 'war', 'ask': 'balaam', 'case_source': 'Sanhedrin 106a:16 — the exam\'s row balaam'})
        w.submit({'kind': 'captive_sentence_case', 'subject': 'the-wrath', 'person': 'the-wrath', 'ask': 'moses_wrath', 'case_source': 'Pesachim 66b:7 — the exam\'s row moses_wrath'})
        w.submit({'kind': 'captive_sentence_case', 'subject': 'the-sentence', 'person': 'the-sentence', 'ask': 'the_sentence', 'case_source': 'Num 31:17-18 — the exam\'s row the_sentence'})
        w.submit({'kind': 'captive_sentence_case', 'subject': 'the-convert-under-three', 'person': 'the-convert-under-three', 'ask': 'proselyte_age', 'case_source': 'Yevamot 60b:6 — the exam\'s row proselyte_age'})
        w.submit({'kind': 'captive_sentence_case', 'subject': 'the-inference', 'person': 'the-inference', 'ask': 'punish_by_inference', 'case_source': 'Makkot 5b:11 — the exam\'s row punish_by_inference'})
        w.submit({'kind': 'warriors_purification_case', 'subject': 'the-toucher', 'person': 'the-toucher', 'ask': 'schedule', 'case_source': 'Num 31:19 — the exam\'s row schedule'})
        w.submit({'kind': 'warriors_purification_case', 'subject': 'the-sworded', 'person': 'the-sworded', 'ask': 'sword_like_slain', 'case_source': 'Nazir 53b:11 — the exam\'s row sword_like_slain'})
        w.submit({'kind': 'warriors_purification_case', 'subject': 'the-captive-sprinkled', 'person': 'the-captive-sprinkled', 'ask': 'captives_sprinkled', 'case_source': 'Yevamot 61a:5 — the exam\'s row captives_sprinkled'})
        w.submit({'kind': 'warriors_purification_case', 'subject': 'the-four-materials', 'person': 'the-four-materials', 'ask': 'four_materials', 'case_source': 'Shabbat 64a:7 — the exam\'s row four_materials'})
        w.submit({'kind': 'warriors_purification_case', 'subject': 'the-camp-entrant', 'person': 'the-camp-entrant', 'ask': 'camp_entry_reading', 'case_source': 'Sifrei 158:3 — the exam\'s row camp_entry_reading'})
        w.submit({'kind': 'vessel_of_war_case', 'subject': 'the-spit', 'person': 'the-spit', 'ask': 'kashering', 'material': 'metal', 'use': 'fire', 'case_source': 'Mishnah Avodah Zarah 5:12 — the exam\'s row kashering (the spit)'})
        w.submit({'kind': 'vessel_of_war_case', 'subject': 'the-cup', 'person': 'the-cup', 'ask': 'kashering', 'material': 'metal', 'use': 'cold', 'case_source': 'Avodah Zarah 75b:17 — the exam\'s row kashering (the cup)'})
        w.submit({'kind': 'vessel_of_war_case', 'subject': 'the-earthen-pot', 'person': 'the-earthen-pot', 'ask': 'kashering', 'material': 'earthenware', 'case_source': 'Pesachim 30b:8 — the exam\'s row kashering (earthenware)'})
        w.submit({'kind': 'vessel_of_war_case', 'subject': 'the-immersion', 'person': 'the-immersion', 'ask': 'immersion_source', 'case_source': 'Avodah Zarah 75b:7 — the exam\'s row immersion_source'})
        w.submit({'kind': 'prey_division_case', 'subject': 'the-tribute-rate', 'person': 'the-tribute-rate', 'ask': 'tribute_rate', 'case_source': 'Num 31:28 — the exam\'s row tribute_rate'})
        w.submit({'kind': 'prey_division_case', 'subject': 'the-levites-rate', 'person': 'the-levites-rate', 'ask': 'levites_rate', 'case_source': 'Jerusalem Talmud Terumot 4:3:2 — the exam\'s row levites_rate'})
        w.submit({'kind': 'prey_division_case', 'subject': 'the-tribute-check', 'person': 'the-tribute-check', 'ask': 'the_tribute_check', 'case_source': 'Num 31:37-41 — the exam\'s row the_tribute_check'})
        w.submit({'kind': 'prey_division_case', 'subject': 'the-private-plunder', 'person': 'the-private-plunder', 'ask': 'private_plunder', 'case_source': 'Num 31:53 — the exam\'s row private_plunder'})
        w.submit({'kind': 'officers_gold_case', 'subject': 'the-count', 'person': 'the-count', 'ask': 'the_count', 'case_source': 'Num 31:49 — the exam\'s row the_count'})
        w.submit({'kind': 'officers_gold_case', 'subject': 'the-ransom', 'person': 'the-ransom', 'ask': 'ransom_at_a_count', 'case_source': 'Num 31:50 — the exam\'s row ransom_at_a_count'})
        w.submit({'kind': 'officers_gold_case', 'subject': 'the-memorial', 'person': 'the-memorial', 'ask': 'memorial', 'case_source': 'Temurah 13a:14 — the exam\'s row memorial'})
        w.submit({'kind': 'officers_gold_case', 'subject': 'the-ornaments', 'person': 'the-ornaments', 'ask': 'ornaments', 'case_source': 'Shabbat 64a:20 — the exam\'s row ornaments'})
        w.advance(w.clock.day + 7)                                             # THE SEVENTH DAY: the purification's timers fire (the third at + 3, the seventh at + 7)
    n = lambda eid, eff: len([e for e in w.entity(eid).ledger if e['effect'] == eff])
    is_open = lambda eid, eff: int(any(e['effect'] == eff and e.get('open') for e in w.entity(eid).ledger))
    tset = len([l for l in w.log if l[0] == 'TIMER-SET']); tfire = len([l for l in w.log if l[0] == 'TIMER-FIRE']); tcan = len([l for l in w.log if l[0] == 'TIMER-CANCEL'])
    return ((n('the-muster', 'counted'), n('the-moab-question', 'commanded'), n('the-anointed-priest', 'accepted'), n('the-five-kings-slain', 'slain'), n('the-diviner', 'slain'),
             n('the-wrath', 'mark_of_anger'), n('the-sentence', 'commanded'), is_open('the-sentence', 'commanded'), n('the-convert-under-three', 'accepted'), n('the-inference', 'accepted'),
             n('the-toucher', 'sprinkling_due_third_day'), n('the-toucher', 'sprinkling_due_seventh_day'), n('the-toucher', 'corpse_unclean_seven_days'), n('the-sworded', 'corpse_unclean_seven_days'), n('the-captive-sprinkled', 'sprinkling_due_seventh_day'), n('the-four-materials', 'accepted'), n('the-camp-entrant', 'declared_pure'),
             n('the-spit', 'declared_pure'), n('the-spit', 'immersed'), n('the-cup', 'immersed'), n('the-cup', 'declared_pure'), n('the-earthen-pot', 'exempt'), n('the-immersion', 'immersed'),
             n('the-tribute-rate', 'heave_offering_given'), n('the-levites-rate', 'levites_portion_given'), n('the-tribute-check', 'counted'), n('the-tribute-check', 'heave_offering_given'), n('the-private-plunder', 'accepted'),
             n('the-count', 'no_plague_at_counting'), n('the-ransom', 'no_plague_at_counting'), n('the-ransom', 'atoned_forgiven'), n('the-memorial', 'memorial_before_the_lord'), n('the-ornaments', 'accepted')),
            (tset, tfire, tcan, len(w.timers)),
            len(w.entities)), w
SCENE, _W = scene()
# THE PREDICTION (typed before the first run, NUMBERS_WALK.md "Sitting 11b"): every exam person written once per effect — the cup's 'declared_pure' the one zero (the
# second branch writes immersed alone); the sentence's debit OPEN; TIMERS: set 6 (the toucher's three, the sworded's one, the captive's two), fired 6 at the seventh day,
# cancelled 0, pending 0. ENTITIES: the exam's 26 persons.
SCENE_PREDICTED = ((1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1), (6, 6, 0, 0), 26)


def narrative():
    """THE NUMBERS WALK 11b (2026-09-12): the portion's own acts AS HISTORY — the THIRTEEN lines of 31:1-54 at the counter's day (40, 6, 1),
    page-order after the vows' line (30:2-17), on a world with this runner's daemon: 35 writes, six timers set (none fired — the tape ends
    at the counter's day), no marker, fourteen entities, four closes found on this world (the trumpets' and the Balak debit's entries live on
    the sequence world alone). Recorded by the sequential run's recorder and stitched onto the tape. Not a graded cell: the tuple below is
    a tripwire typed from the design; the sequence world's RUN tuple and CX1-CX9 grade the tape."""
    with contextlib.redirect_stdout(io.StringIO()):
        w = WE.World(era='Num 31:1-54: the war of Midian on the tape — the vengeance, the war, the sentence, the purification, the statute, the division, the gold (the exodus epoch)', epoch='exodus')
        w.laws = [law_midian]
        w.advance(w.clock.day_in('exodus', 40, 6, 1))
        # THE DAEMON GATE READS LITERAL SUBMITS ONLY — the thirteen lines typed out
        w.submit({'kind': 'midian_vengeance_commanded', 'subject': 'moses', 'to': 'moses', 'close': 'Num 31:7 — by value', 'case_source': LINES[0][0]})
        w.submit({'kind': 'midian_army_mustered', 'subject': 'israel', 'count': MUSTER, 'with': 'pinchas', 'close': 'the trumpets (10:2) closed by value — a run by carrying', 'case_source': LINES[1][0]})
        w.submit({'kind': 'midian_warred', 'subject': 'israel', 'against': 'the-midianites', 'close': 'harass_the_midianites (25:17) and avenge_the_midianites (31:2) closed by value — no write', 'case_source': LINES[2][0]})
        w.submit({'kind': 'kings_and_balaam_slain', 'subject': 'israel', 'kings': KINGS_NAMES, 'diviner': 'balaam', 'case_source': LINES[3][0]})
        w.submit({'kind': 'captives_and_spoil_taken', 'subject': 'israel', 'to': 'moses', 'at': 'the plains of Moab by the Jordan at Jericho', 'case_source': LINES[4][0]})
        w.submit({'kind': 'moses_wroth_at_the_officers', 'subject': 'moses', 'to': 'the-officers-of-the-host', 'close': 'the sentence OPEN forever — no narrated run', 'case_source': LINES[5][0]})
        w.submit({'kind': 'warriors_purification_commanded', 'subject': 'moses', 'to': 'the-men-of-war', 'captives': 'the-captives-of-midian', 'schedule': [THIRD_DUE, SEVENTH_DUE], 'case_source': LINES[6][0]})
        w.submit({'kind': 'vessels_statute_spoken', 'subject': 'eleazar', 'to': 'the-men-of-war', 'metals': METALS, 'case_source': LINES[7][0]})
        w.submit({'kind': 'prey_division_commanded', 'subject': 'moses', 'rates': [str(TRIBUTE_RATE), str(LEVITE_RATE)], 'close': '31:31, 31:41, 31:47 — by value', 'case_source': LINES[8][0]})
        w.submit({'kind': 'prey_counted', 'subject': 'moses', 'with': 'eleazar', 'totals': list(TOTALS), 'case_source': LINES[9][0]})
        w.submit({'kind': 'tribute_given', 'subject': 'moses', 'to': 'eleazar', 'portion': list(WARRIORS), 'tribute': list(TRIBUTE), 'case_source': LINES[10][0]})
        w.submit({'kind': 'levites_portion_given', 'subject': 'moses', 'to': 'the-levites', 'half': list(CONGREGATION), 'share': list(LEVITES), 'case_source': LINES[11][0]})
        w.submit({'kind': 'officers_gold_brought', 'subject': 'the-officers-of-the-host', 'to': 'moses', 'gold': GOLD, 'ornaments': ORNAMENTS, 'case_source': LINES[12][0]})
    writes = len([l for l in w.log if l[0] == 'WRITE'])
    closes = len([e for ent in w.entities.values() for e in ent.ledger if e.get('closed_by')])
    return (writes, len([l for l in w.log if l[0] == 'TIMER-SET']), len(w.entities), w.clock.eras['exodus'].date(w.clock.day)[1:], closes), w


NARRATIVE, _WN = narrative()
NARRATIVE_PREDICTED = (35, 6, 14, (6, 1), 4)   # NUMBERS_WALK.md "Sitting 11b": 35 writes (L1 1, L2 1, L3 0, L4 2, L5 3, L6 2, L7 1, L8 1, L9 3, L10 4, L11 9, L12 5, L13 3), six timers set, fourteen entities, the date (6, 1) of the fortieth year, four closes found on this world (avenge, divide, tribute, share — the trumpets' and the Balak entries live on the tape)
assert NARRATIVE == NARRATIVE_PREDICTED, ('THE NUMBERS WALK: the war of Midian\'s narrative moved from its prediction', NARRATIVE, NARRATIVE_PREDICTED)
