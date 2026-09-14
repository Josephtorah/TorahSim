

# ---- THE WRAP — the daemon, the scene, the narrative ------------------------------------------------------
def law_chukat(event, world):
    """Num 19:1-21:35 (cold_run_chukat.py F1-F6). installed_by boot — the heifer's statute spoken at 19:1 with no installing act on the
    tape (the standing setting); the lines of chapters 20-21 are acts in the fortieth year. ONE timer: the thirty days' weeping (20:29,
    due the day + 30 = (40, 6, 1) on the tape). SIX closes, all the daemon's own (THE TENT sitting 1: a daemon's close is not a tape
    line): the rock's debit (20:11), the ascent's (20:27), Aaron's block (20:28), the cherem (21:3), the turn-back of 14:25 (21:4 —
    law_shelach's entry, closed here on the tape; on this runner's own world the close finds no entry and returns False), the pole's
    (21:9). The exam's six case kinds dispatch to the cells with LITERAL effects per kind (2b's form — an unnamed effect is a KeyError)."""
    k, src = event['kind'], event['case_source']
    E_ = lambda eff, s, cp=None, amount=None, due=None, law='', value=None: {'effect': eff, 'subject': s, 'counterparty': cp, 'amount': amount, 'due': due, 'value': value if value is not None else True, 'source_law': law, 'case_source': src}
    C_ = lambda ev: {f: ev[f] for f in ('ask', 'burden', 'passed', 'third', 'seventh', 'intent', 'covered') if f in ev}   # the case's own fields to the cell (no field named kind or day)
    day = event.get('day', world.clock.day)      # THE SEQUENTIAL RUN: the event's own day
    # ---- chapter 19: the statute (one line, page_order at the running counter) ----
    if k == 'heifer_statute_given':
        return [E_('commanded', 'israel', value='the_red_heifer', law='F1 [INK 19:1-10 "speak to the children of Israel that they take to you a red heifer, whole, in which there is no blemish, upon which never came a yoke; and you shall give it to Eleazar the priest" — the debit on Israel; OPEN on this tape: the ink never narrates the first burning (the row nine_heifers — Parah 3:5 the shelf\'s run)]')]
    # ---- chapter 20: Kadesh (the first marker), Meribah, Edom, Mount Hor ----
    if k == 'miriam_died_at_kadesh':
        return [E_('buried', 'miriam', value='and Miriam died there and was buried there (20:1) — Kadesh in the wilderness of Zin; the tenth of Nisan by the shelf (the row miriam_death_day), the arrival\'s day on the tape (CM5\'s nine days)', law='F3 [INK 20:1; Moed Katan 28a:2; Seder Olam 10:2]'),
                E_('encamped_at', 'israel', value='Kadesh, the wilderness of Zin — in the first month (20:1; the ordinal reader\'s [1]; Seder Olam 9:2: the new moon of Nisan of the fortieth year, the well removed)', law='F3 [INK 20:1; Seder Olam 9:2]')]
    if k == 'congregation_strove_for_water':
        return [E_('gathered_against', 'israel', cp='moses-and-aaron', value='there was no water for the congregation; they gathered against Moses and against Aaron; the people strove with Moses: would that we had expired... why have you brought us up from Egypt (20:2-5) — the first Meribah\'s clauses at the second (Exod 17:2-3, computed)', law='F3 [INK 20:2-5; Exod 17:2-3]')]
    if k == 'moses_and_aaron_fell_and_the_glory':
        return [E_('glory_appeared', 'the-tabernacle', cp='HEAVEN', value='Moses and Aaron came from before the assembly to the entrance of the tent of meeting and fell on their faces, and the glory of the LORD appeared to them (20:6) — the formula\'s fifth seat (Lev 9:23; Num 14:10, 16:19, 17:7)', law='F3 [INK 20:6]')]
    if k == 'rock_commanded':
        return [E_('commanded', 'moses', value='the_rock', law='F3 [INK 20:7-8 "take the staff and assemble the congregation, you and Aaron your brother, and SPEAK to the rock before their eyes, and it shall give its water" — the debit on Moses: the spec\'s verb SPEAK; CLOSED by 20:11\'s strike, the run\'s verb (CM6)]')]
    if k == 'staff_taken_from_before_the_lord':
        return []                                  # the object row read (20:9): "the staff from before the LORD" — Aaron's kept staff (17:25); the words are the line's value
    if k == 'rock_struck_twice':
        world.close('moses', 'commanded', 'Num 20:11 — and Moses lifted his hand and STRUCK the rock with his staff TWICE (the parser\'s [2]) — the run\'s verb against the spec\'s SPEAK (CM6)', value='the_rock')
        return [E_('water_from_the_rock', 'israel', amount=TWICE[0], value='hear now, you rebels: shall we bring you water out of this rock? (20:10); much water came out and the congregation drank, and their cattle (20:11) — struck twice', law='F3 [INK 20:10-11 — rule (19) the dual "twice"; Menachot 76b:13 the cattle]')]
    if k == 'sentence_at_meribah':
        return [E_('barred_from_the_land', 'moses', cp='HEAVEN', value='because you did not believe in Me, to sanctify Me before the eyes of the children of Israel, therefore you shall not bring this assembly into the land which I have given them (20:12) — OPEN: its close at Deut 34', law='F3 [INK 20:12-13; Shabbat 55b:2; Yoma 87a:3]'),
                E_('barred_from_the_land', 'aaron', cp='HEAVEN', value='the same sentence — the frame to Moses AND Aaron (20:12); restated at 20:24; CLOSED by 20:28', law='F3 [INK 20:12, 20:24]')]
    if k == 'messengers_sent_to_edom':
        return [E_('plea_made', 'israel', cp='edom', value='thus says your brother Israel: you know all the hardship... the Egyptians did evil to us and we cried to the LORD... let us pass through your land; we will not pass through field or vineyard nor drink well water; by the king\'s highway (20:14-17) — the firstfruits declaration\'s clauses (Deut 26:6-7, computed)', law='F4 [INK 20:14-17; Deut 26:6-7]')]
    if k == 'edom_refused':
        return [E_('refused', 'edom', cp='israel', value='you shall not pass through me, lest I come out against you with the sword (20:18)', law='F4 [INK 20:18]')]
    if k == 'israel_pleaded_the_highway':
        return [E_('plea_made', 'israel', cp='edom', value='we will go up by the highway; if we drink your water, I and my cattle, I will pay its price; only on foot, nothing more (20:19)', law='F4 [INK 20:19]')]
    if k == 'edom_came_out_against':
        return [E_('refused', 'edom', cp='israel', value='you shall not pass; and Edom came out against him with much people and with a strong hand; and Israel turned away from him (20:20-21) — the row edom_passage: Deut 2:28-29\'s purchase the other arm', law='F4 [INK 20:20-21; Deut 2:4-8, 2:28-29]')]
    if k == 'journeyed_to_mount_hor':
        return [E_('encamped_at', 'israel', value='Mount Hor, by the border of the land of Edom (20:22-23) — from Kadesh, all the congregation; three months at Kadesh by the shelf (Seder Olam 9:2 — the second marker)', law='F4 [INK 20:22; Seder Olam 9:2]')]
    if k == 'aarons_gathering_decreed':
        return [E_('commanded', 'moses', value='bring_aaron_up_mount_hor', law='F4 [INK 20:23-26 "Aaron shall be gathered to his people... because you rebelled against My word at the waters of Meribah; take Aaron and Eleazar his son and bring them up Mount Hor; strip Aaron of his garments and put them on Eleazar his son; and Aaron shall be gathered and die there" — the debit on Moses; CLOSED by 20:27]')]
    if k == 'aaron_brought_up_mount_hor':
        world.close('moses', 'commanded', 'Num 20:27 — and Moses did as the LORD commanded, and they went up Mount Hor before the eyes of all the congregation', value='bring_aaron_up_mount_hor')
        return []
    if k == 'garments_transferred_and_aaron_died':
        world.close('aaron', 'barred_from_the_land', 'Num 20:28 — and Aaron died there on the top of the mountain: the block run to its end (33:38 the date, 33:39 the age)')
        return [E_('garments_transferred', 'aaron', cp='eleazar', value='Moses stripped Aaron of his garments and put them on Eleazar his son (20:28) — Exod 29:29-30\'s spec RUN; the vestments engine\'s cell: %s' % VS_SUBSTITUTE, law='F4 [INK 20:26, 20:28; Exod 29:29-30]'),
                E_('invested_office', 'eleazar', value='the office with the garments (20:28) — the many-garmented priest (Horayot 12a); the priesthood engine\'s hour: %s' % PR_HOUR, law='F4 [INK 20:28; Exod 29:29-30; the priesthood engine\'s row one_hour]'),
                E_('gathered_to_his_people', 'aaron', cp='HEAVEN', value='and Aaron died there on the top of the mountain (20:28) — in the fortieth year, the fifth month, the first of the month, aged a hundred and twenty-three (33:38-39: the parser\'s %s, %s)' % (AARON_DATE, AARON_AGE), law='F4 [INK 20:28; 33:38-39; Seder Olam 10:2]')]
    if k == 'aaron_mourned_thirty_days':
        return [E_('mourned_thirty_days', 'israel', due=day + DAYS30[0], value='and all the congregation saw that Aaron had expired, and they wept for Aaron thirty days, all the house of Israel (20:29) — the men and the women; the TIMER due the thirtieth day: (40, 6, 1) on the tape (CM4)', law='F4 [INK 20:29 — the parser\'s [30]; Deut 34:8 Moses\' thirty]')]
    # ---- chapter 21: Arad during the mourning, the serpents, the stations, the well, the two kings ----
    if k == 'arad_fought_and_took_captives':
        return [E_('taken_captive', 'israel', cp='the-king-of-arad', value='the Canaanite king of Arad, who dwelt in the Negev, heard that Israel came by the way of Atharim; he fought against Israel and took some of them captive (21:1) — during the mourning (Rosh Hashanah 3a: he heard that Aaron died); the shelf\'s one maidservant (the row captive_count)', law='F5 [INK 21:1; 33:40; Rosh Hashanah 3a:1; Gittin 38a:4]')]
    if k == 'israel_vowed_the_cherem':
        return [E_('cherem_vowed', 'israel', cp='HEAVEN', value='if You will indeed give this people into my hand, I will devote their cities (21:2) — the conditional vow (Gen 28:20; Judg 11:30); CLOSED by 21:3', law='F5 [INK 21:2; Eruvin 64b:3]')]
    if k == 'canaanites_devoted_hormah_named':
        world.close('israel', 'cherem_vowed', 'Num 21:3 — and the LORD heard the voice of Israel and gave the Canaanite, and he devoted them and their cities')
        return [E_('destroyed', 'the-king-of-arad', cp='israel', value='he devoted them and their cities (21:3) — Onkelos DESTROYED; the temurah engine\'s devotion: %s' % TM_DEVOTE, law='F5 [INK 21:3; Lev 27:28-29]'),
                E_('hormah_named', 'hormah', value='and he called the name of the place Hormah (21:3) — the proleptic name of 14:45 closed (CF9); Judg 1:17 the second naming', law='F5 [INK 21:3; 14:45]')]
    if k == 'journeyed_by_the_red_sea_way':
        world.close('israel', 'commanded', 'Num 21:4 — and they journeyed from Mount Hor by the way of the Red Sea to go around the land of Edom: 14:25\'s "turn and journey by the way of the Red Sea" RUN (CF8)', value='the_turn_back')
        return [E_('encamped_at', 'israel', value='from Mount Hor by the way of the Red Sea, to go around the land of Edom; and the soul of the people was shortened on the way (21:4) — after the thirty days (the fourth marker: Aaron\'s death + 30)', law='F5 [INK 21:4; 14:25; Deut 2:1]')]
    if k == 'people_spoke_against_god_and_moses':
        return [E_('spoke_against_god_and_moses', 'israel', value='why have you brought us up from Egypt to die in the wilderness? there is no bread and no water, and our soul loathes the light bread (21:5) — the manna (the row manna_absorbed)', law='F5 [INK 21:5; Sanhedrin 110a:10; Yoma 75a]')]
    if k == 'fiery_serpents_sent':
        return [E_('serpents_sent', 'israel', cp='HEAVEN', value='the LORD sent among the people the fiery serpents, and they bit the people, and many people of Israel died (21:6) — the burn-word the heifer\'s (19:5), the bite usury\'s (Deut 23:20)', law='F5 [INK 21:6]')]
    if k == 'people_confessed_and_moses_prayed':
        return [E_('confessed', 'israel', value='we have sinned, for we spoke against the LORD and against you; pray to the LORD that He remove the serpent from us (21:7) — the serpent singular', law='F5 [INK 21:7]'),
                E_('plea_made', 'moses', cp='HEAVEN', value='and Moses prayed for the people (21:7)', law='F5 [INK 21:7]')]
    if k == 'pole_commanded':
        return [E_('commanded', 'moses', value='the_serpent_on_a_pole', law='F5 [INK 21:8 "make YOU a fiery one and set it on a pole; and everyone bitten who sees it shall live" — the debit on Moses; CLOSED by 21:9]')]
    if k == 'copper_serpent_made':
        world.close('moses', 'commanded', 'Num 21:9 — and Moses made a serpent of copper and set it on the pole', value='the_serpent_on_a_pole')
        return [E_('set_on_the_pole', 'the-copper-serpent', value='a serpent of copper on the pole (21:9) — from Moses\' own (Avodah Zarah 44a); its run ends at 2 Kgs 18:4, Nehushtan (the row nehushtan)', law='F5 [INK 21:9; 2 Kgs 18:4]'),
                E_('healed', 'israel', cp='HEAVEN', value='if the serpent bit a man and he looked at the copper serpent, he lived (21:9) — the heart subjected to Heaven (Mishnah Rosh Hashanah 3:8; the row serpent_kills_or_heals)', law='F5 [INK 21:9; Mishnah Rosh Hashanah 3:8]')]
    if k == 'journeyed_oboth_to_arnon':
        return [E_('encamped_at', 'israel', value='Oboth; Iye-abarim in the wilderness before Moab toward the sunrise; the brook Zered; beyond Arnon in the wilderness at the Amorite\'s border (21:10-13) — the Zered after the thirty-eight years (Deut 2:14 — [38])', law='F6 [INK 21:10-13; Deut 2:13-14]')]
    if k == 'book_of_the_wars_cited':
        return []                                  # the citation the value (21:14-15): "therefore it is said in the Book of the Wars of the LORD: Vaheb in Suphah and the brooks of Arnon"
    if k == 'well_given_at_beer':
        return [E_('well_given', 'israel', cp='HEAVEN', value='Beer — the well of which the LORD said to Moses: assemble the people and I will give them water; then sang Israel this song: rise up, O well (21:16-18) — the second "then sang" (Exod 15:1, computed); the lawgiver\'s word (Gen 49:10)', law='F6 [INK 21:16-18; Exod 15:1; Gen 49:10]')]
    if k == 'journeyed_to_pisgah':
        return [E_('encamped_at', 'israel', value='from the wilderness Mattanah, Nahaliel, Bamoth, the valley in the field of Moab, the top of Pisgah looking over the wasteland (21:18-20)', law='F6 [INK 21:19-20]')]
    if k == 'messengers_sent_to_sihon':
        return [E_('plea_made', 'israel', cp='sihon', value='let me pass through your land; we will not turn into field or vineyard, nor drink well water; by the king\'s highway until we pass your border (21:21-22) — thirteen tokens shared with the Edom letter (computed)', law='F6 [INK 21:21-22; 20:17]')]
    if k == 'sihon_came_out_and_fought':
        return [E_('refused', 'sihon', cp='israel', value='Sihon did not let Israel pass through his border; he gathered all his people and came out against Israel to the wilderness, to Jahaz, and fought against Israel (21:23) — hardened (Deut 2:30)', law='F6 [INK 21:23; Deut 2:30]')]
    if k == 'sihon_smitten_land_possessed':
        return [E_('kings_smitten', 'sihon', cp='israel', value='Israel smote him with the edge of the sword (21:24)', law='F6 [INK 21:24]'),
                E_('land_possessed', 'israel', value='his land from Arnon to Jabbok, as far as the sons of Ammon — for the border of the sons of Ammon was strong; all these cities, Heshbon and all its daughters (21:24-25)', law='F6 [INK 21:24-25; Deut 2:19, 2:37]')]
    if k == 'heshbon_and_the_parable':
        return []                                  # the history and the parable the value (21:26-30): Sihon's war on Moab's former king; the parable-tellers' song (Jer 48:45-46 quotes it)
    if k == 'israel_dwelt_and_jazer_taken':
        return [E_('land_possessed', 'israel', value='Israel dwelt in the land of the Amorite; Moses sent to spy out Jazer, and they took its daughters and dispossessed the Amorite there (21:31-32) — Caleb\'s spy-verb (Josh 14:7)', law='F6 [INK 21:31-32; Josh 14:7]')]
    if k == 'og_came_out_and_fear_not':
        return [E_('fear_not_promised', 'moses', cp='HEAVEN', value='do not fear him, for into your hand I have given him and all his people and his land; you shall do to him as you did to Sihon (21:34) — Og came out to Edrei (21:33)', law='F6 [INK 21:33-34; Deut 3:1-2]')]
    if k == 'og_smitten':
        return [E_('kings_smitten', 'og', cp='israel', value='they smote him and his sons and all his people until no survivor was left to him (21:35) — Joshua\'s refrain born (Josh 8:22, 10:33; computed)', law='F6 [INK 21:35; Deut 3:3]'),
                E_('land_possessed', 'israel', value='and they possessed his land (21:35) — Bashan; the land east of the Jordan whole: Sihon\'s, the Amorite\'s and Jazer, Og\'s (CM10)', law='F6 [INK 21:35; Deut 3:1-11]')]
    # ---- the exam's case kinds: each names LITERALLY every effect it can write (2b's form — an unnamed effect is a KeyError to read) ----
    if k == 'heifer_case':
        v, e, _ = heifer_rite(C_(event), DATA); L = 'F1 [%s]' % v; s_ = event['person']
        W = {'accepted': E_('accepted', s_, value=v, law=L), 'disqualified': E_('disqualified', s_, value=v, law=L), 'exempt': E_('exempt', s_, value=v, law=L), 'impure_until_evening': E_('impure_until_evening', s_, value=v, law=L),
             'ashes_kept_for_niddah_water': E_('ashes_kept_for_niddah_water', s_, value=v, law=L), 'sprinkled_seven': E_('sprinkled_seven', s_, amount=SEVEN[0], value=v, law=L), 'pays': E_('pays', s_, cp='the-priest', value=v, law=L)}
        return [W[x] for x in e if x != FX.NONE]
    if k == 'corpse_tumah_case':
        v, e, _ = corpse_tumah(C_(event), DATA); L = 'F2 [%s]' % v; s_ = event['person']
        W = {'accepted': E_('accepted', s_, value=v, law=L), 'disqualified': E_('disqualified', s_, value=v, law=L), 'exempt': E_('exempt', s_, value=v, law=L),
             'corpse_unclean_seven_days': E_('corpse_unclean_seven_days', s_, amount=SEVENS[0][0], due=day + SEVENS[0][0], value=v, law=L),               # the TIMERS: the machine counts the days that pass (3b's inclusive-count lesson recorded, never absorbed)
             'sprinkling_due_third_day': E_('sprinkling_due_third_day', s_, due=day + SCHEDULE[0], value=v, law=L), 'sprinkling_due_seventh_day': E_('sprinkling_due_seventh_day', s_, due=day + SCHEDULE[1], value=v, law=L),
             'not_purified': E_('not_purified', s_, value=v, law=L), 'declared_pure': E_('declared_pure', s_, value=v, law=L), 'impure_until_evening': E_('impure_until_evening', s_, value=v, law=L), 'tent_unclean': E_('tent_unclean', s_, value=v, law=L),
             'open_vessel_unclean': E_('open_vessel_unclean', s_, value=v, law=L), 'karet_cut_off': E_('karet_cut_off', s_, cp='HEAVEN', value=v, law=L), 'sent_outside_the_camp': E_('sent_outside_the_camp', s_, value=v, law=L),
             'washes_and_bathes': E_('washes_and_bathes', s_, value=v, law=L), 'lashes': E_('lashes', s_, value=v, law=L)}
        return [W[x] for x in e if x != FX.NONE]
    if k == 'meribah_case':
        v, e, _ = meribah(C_(event), DATA); L = 'F3 [%s]' % v; s_ = event['person']
        W = {'accepted': E_('accepted', s_, value=v, law=L), 'exempt': E_('exempt', s_, value=v, law=L), 'water_from_the_rock': E_('water_from_the_rock', s_, value=v, law=L), 'barred_from_the_land': E_('barred_from_the_land', s_, cp='HEAVEN', value=v, law=L),
             'buried': E_('buried', s_, value=v, law=L), 'gathered_against': E_('gathered_against', s_, cp='moses-and-aaron', value=v, law=L)}
        return [W[x] for x in e if x != FX.NONE]
    if k == 'edom_hor_case':
        v, e, _ = edom_and_hor(C_(event), DATA); L = 'F4 [%s]' % v; s_ = event['person']
        W = {'accepted': E_('accepted', s_, value=v, law=L), 'exempt': E_('exempt', s_, value=v, law=L), 'refused': E_('refused', s_, value=v, law=L), 'garments_transferred': E_('garments_transferred', s_, cp='eleazar', value=v, law=L),
             'invested_office': E_('invested_office', s_, value=v, law=L), 'gathered_to_his_people': E_('gathered_to_his_people', s_, cp='HEAVEN', value=v, law=L), 'plea_made': E_('plea_made', s_, value=v, law=L)}
        return [W[x] for x in e if x != FX.NONE]
    if k == 'arad_serpent_case':
        v, e, _ = arad_and_the_serpent(C_(event), DATA); L = 'F5 [%s]' % v; s_ = event['person']
        W = {'accepted': E_('accepted', s_, value=v, law=L), 'exempt': E_('exempt', s_, value=v, law=L), 'taken_captive': E_('taken_captive', s_, cp='the-king-of-arad', value=v, law=L), 'cherem_vowed': E_('cherem_vowed', s_, cp='HEAVEN', value=v, law=L),
             'destroyed': E_('destroyed', s_, value=v, law=L), 'hormah_named': E_('hormah_named', s_, value=v, law=L), 'serpents_sent': E_('serpents_sent', s_, cp='HEAVEN', value=v, law=L), 'healed': E_('healed', s_, cp='HEAVEN', value=v, law=L),
             'set_on_the_pole': E_('set_on_the_pole', s_, value=v, law=L), 'confessed': E_('confessed', s_, value=v, law=L)}
        return [W[x] for x in e if x != FX.NONE]
    if k == 'well_kings_case':
        v, e, _ = well_and_kings(C_(event), DATA); L = 'F6 [%s]' % v; s_ = event['person']
        W = {'accepted': E_('accepted', s_, value=v, law=L), 'exempt': E_('exempt', s_, value=v, law=L), 'well_given': E_('well_given', s_, cp='HEAVEN', value=v, law=L), 'land_possessed': E_('land_possessed', s_, value=v, law=L),
             'kings_smitten': E_('kings_smitten', s_, value=v, law=L), 'fear_not_promised': E_('fear_not_promised', s_, cp='HEAVEN', value=v, law=L), 'refused': E_('refused', s_, value=v, law=L)}
        return [W[x] for x in e if x != FX.NONE]
    return []


def scene():
    """THE SCENE — the exam's rows replayed on the world engine (the exodus epoch): the yoked heifer, the tevul yom who burns, the gatherer,
    the trespasser, the seven sprinklings, the burner's garments; the toucher's third and seventh as TIMERS and the omitter's failure, the
    intentional enterer's karet, the high priest, the tent, the open vessel, the gentile, the carrier, the camp; the cattle at the rock,
    the sentence, the bier; the succession, Edom; the captive, the vow, the cherem, the bitten, Hormah; the well's song, the land east,
    Og, Sihon. A closing walk of seven days fires the timers (a timer's setting is not a write — 4b's lesson)."""
    with contextlib.redirect_stdout(io.StringIO()):
        w = WE.World(era='Num 19-21: Mishnah Parah, Oholot, Kelim, Mikvaot, Shevuot, Rosh Hashanah 3:8 and the Talmud\'s rows on the engine (the exodus epoch)', epoch='exodus')
        w.laws = [law_chukat]
        w.advance(w.clock.day_in('exodus', 2, 5, 9))
        d0 = w.clock.day
        w.submit({'kind': 'heifer_case', 'subject': 'the-yoked-heifer', 'person': 'the-yoked-heifer', 'ask': 'yoke', 'burden': 'sacks', 'case_source': 'Sotah 46a:11; Avodah Zarah 23a:6; Num 19:2 — a bundle of sacks placed on it'})
        w.submit({'kind': 'heifer_case', 'subject': 'the-tevul-yom-burner', 'person': 'the-tevul-yom-burner', 'ask': 'tvul_yom', 'case_source': 'Mishnah Parah 3:7; Yoma 43b:3; Num 19:19 — the burner defiled on purpose'})
        w.submit({'kind': 'heifer_case', 'subject': 'the-gatherer', 'person': 'the-gatherer', 'ask': 'gatherer', 'case_source': 'Yoma 43a:7; Yevamot 72b:16; Num 19:9 — a man who is pure shall gather'})
        w.submit({'kind': 'heifer_case', 'subject': 'the-trespasser', 'person': 'the-trespasser', 'ask': 'meilah', 'case_source': 'Menachot 51b:22; Mishnah Parah 4:4; Num 19:9 — it is a sin offering (the Lev 5 engine called)'})
        w.submit({'kind': 'heifer_case', 'subject': 'the-sprinkling-priest', 'person': 'the-sprinkling-priest', 'ask': 'sprinkling', 'case_source': 'Mishnah Parah 3:9; Menachot 27a:14; Num 19:4 — seven times toward the entrance'})
        w.submit({'kind': 'heifer_case', 'subject': 'the-burner', 'person': 'the-burner', 'ask': 'defiles_garments', 'case_source': 'Mishnah Parah 4:4, 8:3; Num 19:7-8 — the rite defiles its servants'})
        w.submit({'kind': 'corpse_tumah_case', 'subject': 'the-toucher', 'person': 'the-toucher', 'ask': 'schedule', 'third': True, 'seventh': True, 'case_source': 'Kiddushin 62a:4; Num 19:12 — the third and the seventh (the timers)'})
        w.submit({'kind': 'corpse_tumah_case', 'subject': 'the-omitter', 'person': 'the-omitter', 'ask': 'schedule', 'third': True, 'seventh': False, 'case_source': 'Sifrei Bamidbar 125; Num 19:12b — the seventh omitted'})
        w.submit({'kind': 'corpse_tumah_case', 'subject': 'the-enterer', 'person': 'the-enterer', 'ask': 'karet_entry', 'intent': 'intentional', 'case_source': 'Makkot 14b:6; Mishnah Keritot 1:1; Num 19:13, 19:20 — the impure who entered'})
        w.submit({'kind': 'corpse_tumah_case', 'subject': 'the-high-priest', 'person': 'the-high-priest', 'ask': 'high_priest_exempt', 'case_source': 'Horayot 9b:3; Mishnah Parah 12:4; Num 19:20 — from the midst of the congregation'})
        w.submit({'kind': 'corpse_tumah_case', 'subject': 'the-tent-dweller', 'person': 'the-tent-dweller', 'ask': 'tent', 'case_source': 'Mishnah Oholot 3:6; Num 19:14 — everyone who comes into the tent'})
        w.submit({'kind': 'corpse_tumah_case', 'subject': 'the-open-vessel', 'person': 'the-open-vessel', 'ask': 'open_vessel', 'covered': False, 'case_source': 'Mishnah Kelim 10:1; Chullin 25a:3; Num 19:15 — no cord-bound cover'})
        w.submit({'kind': 'corpse_tumah_case', 'subject': 'the-gentile', 'person': 'the-gentile', 'ask': 'gentile_no_tumah', 'case_source': 'Nazir 61b:1; Num 19:20 — cut off from the midst of the assembly'})
        w.submit({'kind': 'corpse_tumah_case', 'subject': 'the-carrier', 'person': 'the-carrier', 'ask': 'sprinkler_carrier', 'case_source': 'Yoma 14a:9; Mishnah Parah 12:5; Num 19:21 — he who sprinkles read as he who carries'})
        w.submit({'kind': 'corpse_tumah_case', 'subject': 'the-unclean-at-the-camp', 'person': 'the-unclean-at-the-camp', 'ask': 'camps', 'case_source': 'Mishnah Kelim 1:8; Num 5:2 — the corpse-impure at the chel (naso\'s paid edge)'})
        w.submit({'kind': 'meribah_case', 'subject': 'the-cattle', 'person': 'the-cattle', 'ask': 'cattle_water', 'case_source': 'Menachot 76b:13; Num 20:8 — and their cattle'})
        w.submit({'kind': 'meribah_case', 'subject': 'the-sentenced', 'person': 'the-sentenced', 'ask': 'died_for_sin', 'case_source': 'Shabbat 55b:2; Yoma 87a:3; Num 20:12 — had you believed'})
        w.submit({'kind': 'meribah_case', 'subject': 'the-bier', 'person': 'the-bier', 'ask': 'burial_near_death', 'case_source': 'Moed Katan 28a:2; Num 20:1 — died there and was buried there'})
        w.submit({'kind': 'edom_hor_case', 'subject': 'the-successor', 'person': 'the-successor', 'ask': 'succession', 'case_source': 'Horayot 12a; Num 20:28 — the garments to Eleazar (the vestments engine called)'})
        w.submit({'kind': 'edom_hor_case', 'subject': 'the-refuser', 'person': 'the-refuser', 'ask': 'edom_passage', 'case_source': 'Onkelos Num 20:18-21; Deut 2:28-29 — you shall not pass (the DISPUTE row)'})
        w.submit({'kind': 'arad_serpent_case', 'subject': 'the-captive', 'person': 'the-captive', 'ask': 'captive_acquired', 'case_source': 'Gittin 38a:4; Num 21:1 — took some of them captive'})
        w.submit({'kind': 'arad_serpent_case', 'subject': 'the-vower', 'person': 'the-vower', 'ask': 'vow_form', 'case_source': 'Eruvin 64b:3; Num 21:2 — if You will indeed give'})
        w.submit({'kind': 'arad_serpent_case', 'subject': 'the-devoted', 'person': 'the-devoted', 'ask': 'cherem_law', 'case_source': 'Lev 27:28-29 by the temurah engine; Num 21:3 — he devoted them'})
        w.submit({'kind': 'arad_serpent_case', 'subject': 'the-bitten', 'person': 'the-bitten', 'ask': 'serpent_heals', 'case_source': 'Mishnah Rosh Hashanah 3:8; Num 21:9 — he looked and lived'})
        w.submit({'kind': 'arad_serpent_case', 'subject': 'the-place-hormah', 'person': 'the-place-hormah', 'ask': 'hormah', 'case_source': 'Judg 1:17; Num 21:3 against 14:45 — the proleptic name (CF9)'})
        w.submit({'kind': 'well_kings_case', 'subject': 'the-singer', 'person': 'the-singer', 'ask': 'then_sang', 'case_source': 'Rosh Hashanah 31a:11; Num 21:17 — then sang Israel'})
        w.submit({'kind': 'well_kings_case', 'subject': 'the-east-land', 'person': 'the-east-land', 'ask': 'land_east', 'case_source': 'Chullin 60b:13; Num 21:24-35 — from Arnon to Jabbok, Jazer, Bashan'})
        w.submit({'kind': 'well_kings_case', 'subject': 'the-king-og', 'person': 'the-king-og', 'ask': 'og_lore', 'case_source': 'Niddah 61a:18; Berakhot 54b; Num 21:34 — do not fear him'})
        w.submit({'kind': 'well_kings_case', 'subject': 'the-king-sihon', 'person': 'the-king-sihon', 'ask': 'sihon_refused', 'case_source': 'Deut 2:30; Judg 11:20; Num 21:23 — Sihon did not let Israel pass'})
        w.advance(d0 + SEVENS[0][0])                          # the closing walk: the third day, the seventh day and the seven days fire
    n = lambda eid, eff: len([e for e in w.entity(eid).ledger if e['effect'] == eff])
    L = lambda kk: len([l for l in w.log if l[0] == kk])
    return (n('the-yoked-heifer', 'disqualified'), n('the-tevul-yom-burner', 'accepted'), n('the-gatherer', 'ashes_kept_for_niddah_water'), n('the-trespasser', 'pays'), n('the-sprinkling-priest', 'sprinkled_seven'), n('the-burner', 'impure_until_evening'),
            n('the-toucher', 'sprinkling_due_third_day'), n('the-toucher', 'sprinkling_due_seventh_day'), n('the-toucher', 'declared_pure'), n('the-omitter', 'sprinkling_due_third_day'), n('the-omitter', 'not_purified'),
            n('the-enterer', 'karet_cut_off'), n('the-enterer', 'lashes'), n('the-high-priest', 'exempt'), n('the-tent-dweller', 'tent_unclean'), n('the-tent-dweller', 'corpse_unclean_seven_days'), n('the-open-vessel', 'open_vessel_unclean'),
            n('the-gentile', 'exempt'), n('the-carrier', 'washes_and_bathes'), n('the-carrier', 'impure_until_evening'), n('the-unclean-at-the-camp', 'sent_outside_the_camp'),
            n('the-cattle', 'water_from_the_rock'), n('the-sentenced', 'barred_from_the_land'), n('the-bier', 'buried'),
            n('the-successor', 'garments_transferred'), n('the-successor', 'invested_office'), n('the-successor', 'gathered_to_his_people'), n('the-refuser', 'refused'),
            n('the-captive', 'taken_captive'), n('the-vower', 'cherem_vowed'), n('the-devoted', 'destroyed'), n('the-bitten', 'healed'), n('the-place-hormah', 'hormah_named'),
            n('the-singer', 'well_given'), n('the-east-land', 'land_possessed'), n('the-east-land', 'kings_smitten'), n('the-king-og', 'fear_not_promised'), n('the-king-sihon', 'refused'),
            L('TIMER-SET'), L('TIMER-FIRE'), len(w.entities)), w
SCENE, _W = scene()
SCENE_PREDICTED = (1, 1, 1, 1, 1, 1,
                   1, 1, 1, 1, 1,
                   1, 1, 1, 1, 1, 1,
                   1, 1, 1, 1,
                   1, 1, 1,
                   1, 1, 1, 1,
                   1, 1, 1, 1, 1,
                   1, 1, 1, 1, 1,
                   4, 4, 29)   # PREDICTED from the design BEFORE the first run: one effect per declared row — thirty-eight ledger counts of one; FOUR timers set and fired on the closing walk (the toucher's third and seventh, the omitter's third, the tent-dweller's seven days — the settings not writes, the fires the entries); twenty-nine entities (the subjects; HEAVEN, the priest, Eleazar and the king of Arad counterparties, not entities until written on)
assert SCENE == SCENE_PREDICTED, ('THE NUMBERS WALK: the Chukat scene moved from its prediction', SCENE, SCENE_PREDICTED)


def narrative():
    """THE NUMBERS WALK 6b (2026-09-11; NUMBERS_WALK.md "Sitting 6b"): the portion's own acts AS HISTORY — the thirty-seven lines of Num
    19:1-21:35 in the text's order on a world with this runner's daemon: chapter 19's statute at the running (2, 5, 9) (Seder Olam 8:2 —
    the laws of 1:1-19:22 in the second year); then the fortieth year by its four dates — (40, 1, 1) the arrival at Zin (Seder Olam 9:2's
    new moon of Nisan), (40, 4, 1) Mount Hor (three months at Kadesh), (40, 5, 1) Aaron's death (33:38 read whole by the taught parser),
    (40, 6, 1) the departure (Aaron's death + 20:29's thirty days — the mourning's timer fires on that walk, at its due). On the tape these
    four days are the stitcher's marker rows; here they are advances. The daughters' marker (27:1, the zelophehad runner) moved to
    day_in(40, 6, 1) this sitting — its own literal, reading-placed unchanged (the changelog line). Not a graded cell: the tuple below is a
    tripwire PREDICTED before the first run; the sequence world's RUN tuple grades the tape."""
    with contextlib.redirect_stdout(io.StringIO()):
        w = WE.World(era='Num 19-21: Chukat on the tape — the statute, Kadesh, Meribah, Edom, Mount Hor, Arad, the serpents, the well, the two kings (the exodus epoch)', epoch='exodus')
        w.laws = [law_chukat]
        w.advance(w.clock.day_in('exodus', 2, 5, 9))
        w.submit({'kind': 'heifer_statute_given', 'subject': 'israel', 'heifer': 'red, whole, no blemish, no yoke', 'to': 'eleazar', 'kit': ['cedar', 'hyssop', 'scarlet'], 'case_source': 'Num 19:1-22 — and the LORD spoke to Moses and to Aaron saying: this is the statute of the Torah that the LORD commanded, saying: speak to the children of Israel that they take to you a red heifer, whole, in which there is no blemish, upon which never came a yoke; and you shall give it to Eleazar the priest, and he shall bring it outside the camp and slaughter it before him... and it shall be for the congregation of the children of Israel for a keeping, for waters of niddah; it is a sin offering'})
        w.advance(w.clock.day_in('exodus', 40, 1, 1))     # THE FIRST MARKER on the tape: the arrival at Zin, the new moon of Nisan of the fortieth year
        w.submit({'kind': 'miriam_died_at_kadesh', 'subject': 'miriam', 'at': 'Kadesh, the wilderness of Zin', 'month': FIRST_MONTH[0], 'case_source': 'Num 20:1 — and the children of Israel, the whole congregation, came to the wilderness of Zin in the first month, and the people dwelt at Kadesh; and Miriam died there and was buried there'})
        w.submit({'kind': 'congregation_strove_for_water', 'subject': 'israel', 'words': 'would that we had expired; why have you brought us up from Egypt', 'case_source': 'Num 20:2-5 — and there was no water for the congregation, and they gathered against Moses and against Aaron; and the people strove with Moses and said: would that we had expired when our brothers expired before the LORD; why have you brought the assembly of the LORD into this wilderness... why have you brought us up from Egypt to bring us to this evil place'})
        w.submit({'kind': 'moses_and_aaron_fell_and_the_glory', 'subject': 'moses', 'at': 'the entrance of the tent of meeting', 'case_source': 'Num 20:6 — and Moses and Aaron came from before the assembly to the entrance of the tent of meeting and fell on their faces, and the glory of the LORD appeared to them'})
        w.submit({'kind': 'rock_commanded', 'subject': 'moses', 'verb': 'speak', 'take': 'the staff', 'case_source': 'Num 20:7-8 — and the LORD spoke to Moses saying: take the staff and assemble the congregation, you and Aaron your brother, and speak to the rock before their eyes, and it shall give its water; and you shall bring them water out of the rock and give drink to the congregation and their cattle'})
        w.submit({'kind': 'staff_taken_from_before_the_lord', 'subject': 'moses', 'object': 'the staff from before the LORD', 'case_source': 'Num 20:9 — and Moses took the staff from before the LORD as He commanded him'})
        w.submit({'kind': 'rock_struck_twice', 'subject': 'moses', 'verb': 'struck', 'count': TWICE[0], 'words': 'hear now, you rebels', 'case_source': 'Num 20:10-11 — and Moses and Aaron assembled the assembly before the rock, and he said to them: hear now, you rebels, shall we bring you water out of this rock? and Moses lifted his hand and struck the rock with his staff twice, and much water came out, and the congregation drank, and their cattle'})
        w.submit({'kind': 'sentence_at_meribah', 'subject': 'moses', 'to': ['moses', 'aaron'], 'case_source': 'Num 20:12-13 — and the LORD said to Moses and to Aaron: because you did not believe in Me, to sanctify Me before the eyes of the children of Israel, therefore you shall not bring this assembly into the land which I have given them; these are the waters of Meribah, where the children of Israel strove with the LORD, and He was sanctified in them'})
        w.submit({'kind': 'messengers_sent_to_edom', 'subject': 'israel', 'to': 'the king of Edom', 'words': 'thus says your brother Israel', 'case_source': "Num 20:14-17 — and Moses sent messengers from Kadesh to the king of Edom: thus says your brother Israel: you know all the hardship that has found us; our fathers went down to Egypt... and the Egyptians did evil to us and to our fathers, and we cried to the LORD and He heard our voice and sent a messenger and brought us out of Egypt; and behold, we are at Kadesh, a city at the edge of your border; let us pass, we pray, through your land; we will not pass through field or vineyard, nor drink water of a well; by the king's highway we will go, we will not turn right or left until we pass your border"})
        w.submit({'kind': 'edom_refused', 'subject': 'edom', 'words': 'you shall not pass through me', 'case_source': 'Num 20:18 — and Edom said to him: you shall not pass through me, lest I come out against you with the sword'})
        w.submit({'kind': 'israel_pleaded_the_highway', 'subject': 'israel', 'words': 'by the highway; only on foot', 'case_source': 'Num 20:19 — and the children of Israel said to him: we will go up by the highway, and if we drink your water, I and my cattle, I will give its price; only, nothing more, let me pass on foot'})
        w.submit({'kind': 'edom_came_out_against', 'subject': 'edom', 'with': 'much people and a strong hand', 'case_source': 'Num 20:20-21 — and he said: you shall not pass; and Edom came out against him with much people and with a strong hand; and Edom refused to let Israel pass through his border, and Israel turned away from him'})
        w.advance(w.clock.day_in('exodus', 40, 4, 1))     # THE SECOND MARKER: three months at Kadesh (Seder Olam 9:2), the journey to Mount Hor
        w.submit({'kind': 'journeyed_to_mount_hor', 'subject': 'israel', 'to': 'Mount Hor, by the border of the land of Edom', 'case_source': 'Num 20:22 — and they journeyed from Kadesh, and the children of Israel, the whole congregation, came to Mount Hor'})
        w.submit({'kind': 'aarons_gathering_decreed', 'subject': 'moses', 'words': 'Aaron shall be gathered to his people; because you rebelled at the waters of Meribah', 'case_source': 'Num 20:23-24 — and the LORD said to Moses and to Aaron at Mount Hor, by the border of the land of Edom, saying: Aaron shall be gathered to his people, for he shall not come into the land which I have given to the children of Israel, because you rebelled against My word at the waters of Meribah; take Aaron and Eleazar his son and bring them up Mount Hor'})
        w.submit({'kind': 'aaron_brought_up_mount_hor', 'subject': 'moses', 'with': ['aaron', 'eleazar'], 'case_source': 'Num 20:25-27 — take Aaron and Eleazar his son and bring them up Mount Hor; and strip Aaron of his garments and put them on Eleazar his son, and Aaron shall be gathered and die there; and Moses did as the LORD commanded, and they went up Mount Hor before the eyes of all the congregation'})
        w.advance(w.clock.day_in('exodus', *AARON_DATE))  # THE THIRD MARKER: 33:38 read whole — the fortieth year, the fifth month, the first of the month
        w.submit({'kind': 'garments_transferred_and_aaron_died', 'subject': 'aaron', 'to': 'eleazar', 'age': AARON_AGE[0], 'date': AARON_DATE, 'case_source': 'Num 20:28 — and Moses stripped Aaron of his garments and put them on Eleazar his son; and Aaron died there on the top of the mountain; and Moses and Eleazar came down from the mountain'})
        w.submit({'kind': 'aaron_mourned_thirty_days', 'subject': 'israel', 'days': DAYS30[0], 'who': 'all the house of Israel', 'case_source': 'Num 20:29 — and all the congregation saw that Aaron had expired, and they wept for Aaron thirty days, all the house of Israel'})
        w.submit({'kind': 'arad_fought_and_took_captives', 'subject': 'the-king-of-arad', 'heard': 'that Israel came by the way of Atharim', 'case_source': 'Num 21:1 — and the Canaanite, the king of Arad, who dwelt in the Negev, heard that Israel came by the way of Atharim; and he fought against Israel and took some of them captive'})
        w.submit({'kind': 'israel_vowed_the_cherem', 'subject': 'israel', 'vow': 'if You will indeed give this people into my hand, I will devote their cities', 'case_source': 'Num 21:2 — and Israel vowed a vow to the LORD and said: if You will indeed give this people into my hand, I will devote their cities'})
        w.submit({'kind': 'canaanites_devoted_hormah_named', 'subject': 'israel', 'named': 'Hormah', 'case_source': 'Num 21:3 — and the LORD heard the voice of Israel and gave the Canaanite, and he devoted them and their cities; and he called the name of the place Hormah'})
        w.advance(w.clock.day_in('exodus', 40, 6, 1))     # THE FOURTH MARKER: Aaron's death + the thirty days (the mourning fires on this walk, at its due)
        w.submit({'kind': 'journeyed_by_the_red_sea_way', 'subject': 'israel', 'from': 'Mount Hor', 'by': 'the way of the Red Sea, around the land of Edom', 'case_source': 'Num 21:4 — and they journeyed from Mount Hor by the way of the Red Sea, to go around the land of Edom; and the soul of the people was shortened on the way'})
        w.submit({'kind': 'people_spoke_against_god_and_moses', 'subject': 'israel', 'words': 'why have you brought us up from Egypt to die in the wilderness; our soul loathes the light bread', 'case_source': 'Num 21:5 — and the people spoke against God and against Moses: why have you brought us up from Egypt to die in the wilderness? for there is no bread and no water, and our soul loathes the light bread'})
        w.submit({'kind': 'fiery_serpents_sent', 'subject': 'israel', 'by': 'HEAVEN', 'case_source': 'Num 21:6 — and the LORD sent among the people the fiery serpents, and they bit the people, and many people of Israel died'})
        w.submit({'kind': 'people_confessed_and_moses_prayed', 'subject': 'israel', 'words': 'we have sinned, for we spoke against the LORD and against you', 'case_source': 'Num 21:7 — and the people came to Moses and said: we have sinned, for we spoke against the LORD and against you; pray to the LORD that He remove the serpent from us; and Moses prayed for the people'})
        w.submit({'kind': 'pole_commanded', 'subject': 'moses', 'make': 'a fiery one on a pole', 'case_source': 'Num 21:8 — and the LORD said to Moses: make you a fiery one and set it on a pole; and it shall be, everyone bitten who sees it shall live'})
        w.submit({'kind': 'copper_serpent_made', 'subject': 'moses', 'of': 'copper', 'case_source': 'Num 21:9 — and Moses made a serpent of copper and set it on the pole; and it was, if the serpent bit a man, and he looked at the copper serpent, he lived'})
        w.submit({'kind': 'journeyed_oboth_to_arnon', 'subject': 'israel', 'stations': ['Oboth', 'Iye-abarim', 'the brook Zered', 'beyond Arnon'], 'case_source': "Num 21:10-13 — and the children of Israel journeyed and camped at Oboth; and they journeyed from Oboth and camped at Iye-abarim, in the wilderness before Moab toward the sunrise; from there they journeyed and camped at the brook Zered; from there they journeyed and camped beyond Arnon, in the wilderness that comes out of the Amorite's border, for Arnon is Moab's border, between Moab and the Amorite"})
        w.submit({'kind': 'book_of_the_wars_cited', 'subject': 'israel', 'book': 'the Book of the Wars of the LORD', 'case_source': 'Num 21:14-15 — therefore it is said in the Book of the Wars of the LORD: Vaheb in Suphah and the brooks of Arnon, and the slope of the brooks that turns to the seat of Ar and leans on the border of Moab'})
        w.submit({'kind': 'well_given_at_beer', 'subject': 'israel', 'song': 'rise up, O well', 'case_source': 'Num 21:16-18 — and from there to Beer: that is the well of which the LORD said to Moses: assemble the people and I will give them water; then sang Israel this song: rise up, O well, answer it; the well the princes dug, the nobles of the people delved it, with the lawgiver, with their staffs'})
        w.submit({'kind': 'journeyed_to_pisgah', 'subject': 'israel', 'stations': ['Mattanah', 'Nahaliel', 'Bamoth', 'the valley in the field of Moab', 'the top of Pisgah'], 'case_source': 'Num 21:18-20 — and from the wilderness Mattanah; and from Mattanah Nahaliel; and from Nahaliel Bamoth; and from Bamoth the valley that is in the field of Moab, the top of Pisgah, which looks over the wasteland'})
        w.submit({'kind': 'messengers_sent_to_sihon', 'subject': 'israel', 'to': 'Sihon king of the Amorite', 'case_source': "Num 21:21-22 — and Israel sent messengers to Sihon king of the Amorite saying: let me pass through your land; we will not turn into field or vineyard, we will not drink water of a well; by the king's highway we will go until we pass your border"})
        w.submit({'kind': 'sihon_came_out_and_fought', 'subject': 'sihon', 'at': 'Jahaz', 'case_source': 'Num 21:23 — and Sihon did not let Israel pass through his border; and Sihon gathered all his people and came out against Israel to the wilderness, and came to Jahaz and fought against Israel'})
        w.submit({'kind': 'sihon_smitten_land_possessed', 'subject': 'israel', 'from': 'Arnon', 'to': 'Jabbok', 'case_source': "Num 21:24-25 — and Israel smote him with the edge of the sword and possessed his land from Arnon to Jabbok, as far as the sons of Ammon, for the border of the sons of Ammon was strong; and Israel took all these cities, and Israel dwelt in all the cities of the Amorite, in Heshbon and in all its daughters"})
        w.submit({'kind': 'heshbon_and_the_parable', 'subject': 'israel', 'tellers': 'the parable-tellers', 'case_source': 'Num 21:26-30 — for Heshbon was the city of Sihon king of the Amorite, who had fought against the former king of Moab and taken all his land from his hand as far as Arnon; therefore the parable-tellers say: come to Heshbon... woe to you, Moab; you are lost, people of Chemosh... and we shot them; Heshbon is lost as far as Dibon'})
        w.submit({'kind': 'israel_dwelt_and_jazer_taken', 'subject': 'israel', 'spied': 'Jazer', 'case_source': 'Num 21:31-32 — and Israel dwelt in the land of the Amorite; and Moses sent to spy out Jazer, and they took its daughters and dispossessed the Amorite that was there'})
        w.submit({'kind': 'og_came_out_and_fear_not', 'subject': 'og', 'at': 'Edrei', 'words': 'do not fear him', 'case_source': 'Num 21:33-34 — and they turned and went up by the way of Bashan; and Og king of Bashan came out against them, he and all his people, to battle at Edrei; and the LORD said to Moses: do not fear him, for into your hand I have given him and all his people and his land, and you shall do to him as you did to Sihon king of the Amorite who dwelt at Heshbon'})
        w.submit({'kind': 'og_smitten', 'subject': 'israel', 'survivor': False, 'case_source': 'Num 21:35 — and they smote him and his sons and all his people until no survivor was left to him, and they possessed his land'})
    n = lambda eid, eff: len([e for e in w.entity(eid).ledger if e['effect'] == eff])
    is_open = lambda eid, eff: [e.get('open') for e in w.entity(eid).ledger if e['effect'] == eff]
    L = lambda kk: len([l for l in w.log if l[0] == kk])
    ex = w.clock.eras['exodus']
    markers = [l for l in w.log if l[0] == 'MARKER']
    fires = [l for l in w.log if l[0] == 'TIMER-FIRE']
    return (n('israel', 'commanded'), is_open('israel', 'commanded'),
            n('miriam', 'buried'), n('israel', 'encamped_at'), n('israel', 'gathered_against'), n('the-tabernacle', 'glory_appeared'),
            n('moses', 'commanded'), is_open('moses', 'commanded'), n('israel', 'water_from_the_rock'),
            n('moses', 'barred_from_the_land'), is_open('moses', 'barred_from_the_land'), n('aaron', 'barred_from_the_land'), is_open('aaron', 'barred_from_the_land'),
            n('israel', 'plea_made'), n('edom', 'refused'),
            n('aaron', 'garments_transferred'), n('eleazar', 'invested_office'), n('aaron', 'gathered_to_his_people'), n('israel', 'mourned_thirty_days'),
            n('israel', 'taken_captive'), n('israel', 'cherem_vowed'), is_open('israel', 'cherem_vowed'), n('the-king-of-arad', 'destroyed'), n('hormah', 'hormah_named'),
            n('israel', 'spoke_against_god_and_moses'), n('israel', 'serpents_sent'), n('israel', 'confessed'), n('moses', 'plea_made'), n('the-copper-serpent', 'set_on_the_pole'), n('israel', 'healed'),
            n('israel', 'well_given'), n('sihon', 'refused'), n('sihon', 'kings_smitten'), n('og', 'kings_smitten'), n('israel', 'land_possessed'), n('moses', 'fear_not_promised'),
            L('TIMER-SET'), L('TIMER-FIRE'), [ex.date(f[1]) for f in fires], len(markers), L('EVENT'), L('WRITE'), len(w.entities)), w


NARRATIVE, _WN = narrative()
NARRATIVE_PREDICTED = (1, [True],
                       1, 5, 1, 1,
                       3, [False, False, False], 1,
                       1, [True], 1, [False],
                       3, 2,
                       1, 1, 1, 1,
                       1, 1, [False], 1, 1,
                       1, 1, 1, 1, 1, 1,
                       1, 1, 1, 1, 3, 1,
                       1, 1, [(40, 6, 1)], 0, 37, 42, 12)   # PREDICTED from the design BEFORE the first run (NUMBERS_WALK.md "Sitting 6b"): the heifer's debit OPEN; Miriam buried; Israel encamped five times (Kadesh, Mount Hor, the Red Sea way, Oboth-to-Arnon, Pisgah), the strife, the glory's fifth seat; Moses' three debits (the rock, the ascent, the pole) all CLOSED, the water struck out; Moses barred OPEN, Aaron barred CLOSED by 20:28; Israel's three pleas (Edom twice, Sihon), Edom's two refusals; the garments, Eleazar's office, Aaron gathered, the mourning's fire; the captives, the cherem CLOSED by 21:3, Arad devoted, Hormah named; the speaking against, the serpents, the confession, Moses' prayer, the serpent on the pole, the healing; the well; Sihon's refusal and death, Og's death, the land possessed three times, the fear-not; ONE timer set and fired at (40, 6, 1); no marker (advances here, markers on the tape); thirty-seven events; forty-two writes (forty-one at the lines + the mourning's fire — a timer's setting is not a write; CF3's carcasses are the tape's, not this world's); twelve entities (israel, miriam, the tabernacle, moses, aaron, edom, eleazar, the king of Arad, hormah, the copper serpent, sihon, og)
assert NARRATIVE == NARRATIVE_PREDICTED, ('THE NUMBERS WALK: Chukat\'s narrative moved from its prediction', NARRATIVE, NARRATIVE_PREDICTED)
