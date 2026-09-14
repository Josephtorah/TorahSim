
# =====================================================================
# Motion 1 — THE FUNCTION, compiled from the ink (F1-F5)
# =====================================================================
# ===== F1: THE REBELLION (Num 16:1-35) =====================================================================
def rebellion(case, data):
    del P[:]
    ask = case['ask']
    if ask == 'took':
        ink('16:1', '"and Korach TOOK" — no object; the genealogy stops at Levi where 1 Chr 6:23 runs it to Israel'); move('Onkelos Num 16:1', 'divided himself'); move('Sanhedrin 109b:13 (Reish Lakish)', 'he took a bad acquisition for himself')
        return out('took — no object; Onkelos: divided himself; a bad acquisition (Sanhedrin 109b)', [FX.NONE])
    if ask == 'two_hundred_fifty':
        ink('16:2, 16:17, 16:35', 'the parser at three seats: %s — 16:35 "THE fifty and two hundred", the definite numeral at the head of a compound, taught at 5b' % C250)
        return out('250 — the parser at 16:2, 16:17 and 16:35 (the definite numeral at the head of a compound)', [FX.NONE])
    if ask == 'too_much_returned':
        ink('16:3', '"too much for you" (rav lakhem)'); ink('16:7', 'returned to the Levites — "too much for you, sons of Levi"'); move('Sotah 13b:13 (R. Levi)', 'proclaimed with "rav", so it was proclaimed to him with "rav" — Deut 3:26 "let it suffice for you"')
        return out('too much for you (16:3) returned at 16:7; proclaimed to Moses at Deut 3:26 (Sotah 13b)', [FX.NONE])
    if ask == 'congregation_ten':
        ink('16:21', '"separate yourselves from AMONG this congregation"'); move('Berakhot 21b:5; Megillah 23b:7; Sanhedrin 74b:3', '"among" / "among" with the sanctification of the Name; "congregation" / "congregation" with the spies (14:27): a congregation is ten')
        return out('10 — among / among with the sanctification of the Name; congregation / congregation with the spies (Berakhot 21b; Megillah 23b; Sanhedrin 74b)', [FX.NONE])
    if ask == 'summons_procedure':
        ink('16:12', '"and Moses sent to call Dathan and Abiram"'); ink('16:16', '"be you and all your congregation before the LORD, you and they and Aaron, tomorrow"'); ink('16:14', '"will you put out the eyes of these men" — the report'); move('Moed Katan 16a:3-5 (Rava)', "the court's agent; the defendant in person; before a great man; both parties named; a date set; the agent's report not slander")
        return out('the agent sent (16:12); in person (16:16); before a great man; both parties named; a date set — tomorrow; the report of disrespect permitted (Moed Katan 16a)', [FX.NONE])
    if ask == 'test':
        ink('16:5', '"in the morning the LORD will make known who is His and who is holy"'); ink('16:7, 16:16', '"tomorrow" twice — the one-day timer censers_test_awaited'); move('Sanhedrin 110a', 'as the boundary between morning and evening was fixed at creation, so Aaron')
        return out('in the morning the LORD will make known (16:5) — the boundary fixed at creation (Sanhedrin 110a); the censers tomorrow (16:7, 16:16) — the one-day timer', [FX.NONE])
    if ask == 'oath':
        ink('16:15', '"it was hot to Moses, very... do not turn to their offering; not ONE ass have I taken" — %s; the Cain echo (Gen 4:5 "it was hot to Cain, very"; "to Cain and his offering He did not turn")' % ONE_ONE); move('Nedarim 38a:11-13', "Rava: Samuel's greater — 'whose ox, whose ass' (1 Sam 12:3) even with consent"); move('Megillah 9b:1', "the translators' 'one item of value'")
        return out("not one ass (16:15) — Samuel's whose ox, whose ass (1 Sam 12:3; Nedarim 38a); the Cain echo (Gen 4:5)", [FX.NONE])
    if ask == 'oath_warning_formula':
        ink('16:26', '"turn aside, I pray, from the tents of these wicked men and touch nothing of theirs, lest you be swept away" — Sodom\'s verbs (Gen 19:2, 18:23)'); move('Shevuot 39a:7', 'the bystanders recite it when an oath is administered; the oath on the court\'s understanding (the oaths engine\'s seat)')
        return out('16:26 recited at the oath — depart from the tents of these wicked men (Shevuot 39a)', [FX.NONE])
    if ask == 'new_creation':
        ink('16:30', '"if the LORD creates a creation and the ground opens its mouth" — the noun\'s one seat'); dat('the row earth_mouth = %s' % data['earth_mouth']['value']); move('Mishnah Avot 5:6; Pesachim 54a', 'the mouth of the earth created at the twilight of the sixth day'); move('Sanhedrin 110a:16; Nedarim 39b:3 (Rava)', 'nothing new under the sun — the opening brought near')
        return out("the mouth of the earth created at the twilight of the sixth day (Avot 5:6); if not, create it now — Gehenna's opening brought near (Sanhedrin 110a:16; Nedarim 39b)", [FX.NONE])
    if ask == 'death_mode':
        ink('16:32', '"every person who belonged TO Korach" — Korach not named (computed: %s)' % ('לקרח' in SWALLOWED_NAMES)); ink('26:10', '"and swallowed them with Korach" — the retelling adds him (computed: %s)' % ADDS_KORACH); dat('the row korach_death_mode = %s: %s' % (data['korach_death_mode']['value'], data['korach_death_mode']['settings']['open'][:80]))
        move('Sanhedrin 110a:13 (R. Yochanan)', 'neither swallowed nor burned — he died in the plague'); move('Sanhedrin 110a:14 (the baraita, the outside teaching)', 'both burned and swallowed')
        return out('OPEN — 16:32 names the men who belonged to Korach, not Korach; 26:10 adds and Korach; R. Yochanan: the plague; the baraita: burned and swallowed (Sanhedrin 110a)', ['put_to_death'])
    if ask == 'share':
        ink('16:33', '"the earth covered them and they perished from among the assembly"'); dat('the row korach_share = %s' % data['korach_share']['value']); move('Mishnah Sanhedrin 10:3; Sanhedrin 108a:4, 109b:11', 'R. Akiva: no share, no rising; R. Eliezer: "the LORD kills and makes alive"'); move('Sanhedrin 109b:12; Tosefta Sanhedrin 13:9', 'R. Yehuda ben Beteira: a lost item sought and found')
        return out('R. Akiva: no share and no rising; R. Eliezer: the LORD kills and makes alive (Mishnah Sanhedrin 10:3); R. Yehuda ben Beteira: a lost item sought (Sanhedrin 109b)', [FX.NONE])
    if ask == 'sons_of_korach':
        ink('26:11', '"and the sons of Korach did not die"'); dat('the row sons_of_korach = %s' % data['sons_of_korach']['value']); move('Sanhedrin 110a', 'a place was fortified for them in Gehenna')
        return out('the sons of Korach did not die (26:11) — a place fortified for them (Sanhedrin 110a); the eleven Psalm headings', [FX.NONE])
    if ask == 'exclusion_by_sin':
        ink('16:32-33', 'the swallowed perished from among the assembly'); move('CALLED cold_run_zelophehad.inheritance_order(excluded) -> %r [IMPORT, live call]' % ZL_EXCL, "Bava Batra 118b: the spies, the protesters (Korach's two hundred fifty) and Korach's congregation took no portion")
        return out(ZL_EXCL, ['exempt'])
    if ask == 'not_for_heaven':
        dat('the row dispute_not_for_heaven = %s' % data['dispute_not_for_heaven']['value']); move('Mishnah Avot 5:17', "a dispute not for Heaven's sake will not endure — Korach and all his congregation")
        return out("a dispute not for Heaven's sake — Korach and all his congregation (Avot 5:17)", [FX.NONE])
    if ask == 'earth_mouth_cain':
        ink('16:30-32', '"the ground opens its mouth" / "the earth opened its mouth" — Cain\'s ground (Gen 4:11), Deut 11:6'); move('Sanhedrin 37b:11 (Rav Yehuda son of R. Chiyya)', "the earth's mouth opened for Abel's blood and again for Korach — for a deleterious purpose")
        return out('the ground opened its mouth for Abel\'s blood and for Korach — for a deleterious purpose (Sanhedrin 37b); Gen 4:11, Deut 11:6', [FX.NONE])
    if ask == 'swallowed':
        ink('16:31-33', '"the ground under them split... the earth opened its mouth and swallowed them and their houses... they went down alive to Sheol"'); ink('Deut 11:6; Ps 106:17', 'the retellings name Dathan and Abiram alone')
        return out('Dathan and Abiram and their households swallowed alive (16:31-33); Deut 11:6, Ps 106:17 name them alone', ['put_to_death'])
    if ask == 'fire':
        ink('16:35', '"fire went out from WITH the LORD and consumed the two hundred and fifty men" — %d; Leviticus\' "from before" (9:24, 10:2)' % C250[2]); move('Sanhedrin 52a:10-12', "the souls burned, the bodies intact — 'sinned against their souls' (17:3)")
        return out('fire from with the LORD consumed the 250 (16:35) — the souls burned, the bodies intact (Sanhedrin 52a); Lev 9:24, 10:2 from before', ['put_to_death'])
    if ask == 'wives':
        dat('the row wives = %s' % data['wives']['value']); move('Sanhedrin 109b:15-16 (Rav)', "On's wife: the wine, the tent's entrance — spared"); move('Sanhedrin 110a', "Korach's wife incited him")
        return out("On's wife saved him — the wine and the tent's entrance; Korach's wife incited (Sanhedrin 109b-110a)", [FX.NONE])
    if ask == 'names':
        ink('16:1, 18:12', 'Izhar = fresh oil — one pointed word (the reading\'s crown; the triad %s at 18:12)' % TRIAD); move('Sanhedrin 109b:13-15', 'the names expounded: a void, the afternoon heat, blunted teeth, an escort; Dathan the precepts, Abiram braced, On in mourning')
        return out("Korach a void; Izhar the afternoon heat; Dathan the precepts; Abiram braced; On in mourning (Sanhedrin 109b) — the names' lore; Izhar = fresh oil the ink's pointed word (18:12)", [FX.NONE])
    if ask == 'visiting_the_sick':
        ink('16:29', '"and the visitation of all men is visited on them"'); move('Nedarim 39b:2 (Reish Lakish; Rava)', 'visiting the sick alluded')
        return out('alluded from the visitation of all men (16:29 — Nedarim 39b)', [FX.NONE])
    if ask == 'elect':
        ink('16:2', '"princes of the congregation, called to the assembly, men of name" — 1:16\'s "called of the congregation" returning at 26:9'); move('Sanhedrin 110a:4', 'the elect who intercalate the years; men of renown')
        return out('the elect of the assembly = those who intercalate; men of renown (Sanhedrin 110a:4)', [FX.NONE])
    if ask == 'what_moses_heard':
        ink('16:4', '"and Moses heard and fell on his face" — alone on his face (singular); 16:22 and 17:10 the two'); move('Sanhedrin 110a:5', 'suspected of adultery — Ps 106:16; Exod 33:7')
        return out('suspected of adultery — Ps 106:16 (Sanhedrin 110a:5)', [FX.NONE])
    return out('no verdict in span', [FX.NONE])


# ===== F2: THE PLAGUE AND THE STAFFS (Num 17:1-28) =========================================================
def plague_and_staffs(case, data):
    del P[:]
    ask = case['ask']
    if ask == 'elevate_in_sanctity':
        ink('17:3-4', '"let them be made beaten plates, a covering for the altar, for they offered them before the LORD and they became holy" — the plate-word the gold thread\'s (Exod 39:3)'); move('Menachot 99a:11 (R. Acha bar Ya\'akov)', 'one elevates in sanctity — service vessels became the altar\'s own')
        return out("one elevates in sanctity — the censers, service vessels, became the altar's covering (Menachot 99a)", ['altar_plated'])
    if ask == 'burning_mode':
        ink('17:3', '"the censers of these sinners against their own souls"'); move('Sanhedrin 52a:10-12', 'burning / burning with Lev 21:9: the soul burned, the body intact')
        return out('the souls burned, the bodies intact (17:3 sinned against their souls; Sanhedrin 52a) — the capital burning\'s likeness', [FX.NONE])
    if ask == 'stranger_incense_ban':
        ink('17:5', '"a memorial... that no stranger who is not of Aaron\'s seed shall come near to burn incense before the LORD... as the LORD spoke by the hand of Moses TO HIM" — the output verse; the stranger defined "not of Aaron\'s seed" (Lev 21:21, 22:4 the seed)')
        return out("no stranger not of Aaron's seed to burn incense (17:5) — the output by the hand of Moses to him; rule installed on the priesthood", ['rule_installed'])
    if ask == 'maintaining_a_dispute':
        ink('16:25', '"and Moses rose and went to Dathan and Abiram"'); ink('17:5', '"that he be not as Korach and his congregation"'); dat('the row maintaining_a_dispute = %s' % data['maintaining_a_dispute']['value']); move('Sanhedrin 110a:6 (Reish Lakish; Rav)', 'one may not perpetuate a dispute — a prohibition; R. Ashi: leprosy')
        return out('one may not perpetuate a dispute — a prohibition from not to be as Korach (Rav; Reish Lakish on 16:25 — Sanhedrin 110a); R. Ashi: leprosy', [FX.NONE])
    if ask == 'incense_atones':
        ink('17:12', '"and he put the incense and atoned for the people" — atonement written of incense'); dat('the row incense_stays_plague = %s' % data['incense_stays_plague']['value']); move('Yoma 44a:5; Arakhin 16a:19; Zevachim 88b:10', 'incense atones — for slander: the private for the private')
        return out('incense atones — for slander: the private for the private (Yoma 44a; Arakhin 16a; Zevachim 88b)', ['atoned_forgiven'])
    if ask == 'angel_of_death':
        ink('17:13', '"and he stood between the dead and the living, and the plague was stayed"'); move('Shabbat 89a:2', 'the angel of death gave Moses the remedy — Ps 68:19')
        return out('the angel of death gave Moses the remedy (Shabbat 89a)', [FX.NONE])
    if ask == 'plague_count':
        ink('17:14', '"the dead in the plague were fourteen thousand and seven hundred, BESIDES the dead over the matter of Korach" — %d by the parser; the 250 and the households uncounted (Onkelos: the division of Korach)' % PLAGUE)
        return out("14,700 — besides the dead over the matter of Korach (17:14, the parser's)", ['plague_struck'])
    if ask == 'fire_from_the_altar':
        ink('17:11', '"put fire on it from OFF the altar and put incense" — the Day of Atonement\'s phrase (Lev 16:12) against Nadab\'s strange fire (Lev 10:1)')
        return out("from off the altar (17:11) — the Day of Atonement's phrase (Lev 16:12); against the strange fire (Lev 10:1)", [FX.NONE])
    if ask == 'staffs_count':
        ink('17:17-18', '"twelve staffs... Aaron\'s name on the staff of Levi" — %s' % STAFFS); ink('17:21', '"a staff for one prince, a staff for one prince... twelve staffs, and Aaron\'s staff among their staffs" — %s: Levi inside the twelve, Joseph one staff' % STAFFS_21)
        return out("12 — a staff for a father's house, Aaron's on Levi's, among their staffs (17:17-21 — the parser's [12], [1, 1, 12])", [FX.NONE])
    if ask == 'budded':
        ink('17:23', '"on the morrow... the staff of Aaron for the house of Levi had budded: it brought forth a bud and blossomed a BLOSSOM and ripened almonds" — the blossom the frontplate\'s word (Exod 28:36, 39:30, Lev 8:9); almonds once in the Bible; "ripened" Isaac weaned (Gen 21:8)')
        return out("a bud, a blossom (the frontplate's word), almonds (once; the menorah's cups) — on the morrow (17:23)", ['staff_budded'])
    if ask == 'staff_hidden':
        ink('17:25', '"return Aaron\'s staff before the testimony for a keeping, for a sign" — the manna jar\'s formula (Exod 16:34)'); dat('the row staff_hidden_with = %s' % data['staff_hidden_with']['value']); move('Horayot 12a:1-3; Keritot 5b:16-20; Yoma 52b:15', '"keepsake" / "keepsake" — sequestered with the ark, the jar and the oil')
        return out('hidden with the ark, the jar of manna and the anointing oil (Horayot 12a; Keritot 5b; Yoma 52b) — the keepsake / keepsake analogy', ['kept_for_a_sign'])
    if ask == 'three_deaths':
        ink('17:27', '"we expire, we perish, all of us perish" — the expire-verb Aaron\'s own at 20:29'); move('Onkelos Num 17:27', 'three deaths: the sword, the earth, the plague — cut from the shelf\'s bytes at the reading')
        return out('we expire, we perish, all of us perish (17:27) — Onkelos: the sword, the earth, the plague', [FX.NONE])
    if ask == 'levite_at_another_work':
        ink('18:3', '"only to the vessels of the holy and to the altar they shall not come near, that they die not, both they and you"'); dat('the row levite_at_another_work = %s' % data['levite_at_another_work']['value']); move('Arakhin 11b', "a Levite at the priests' work or another Levite's — death by Heaven")
        return out("a Levite at the priests' work or another Levite's — death by Heaven (Arakhin 11b)", ['death_by_heaven'])
    if ask == 'whoever_comes_near':
        ink('17:28', '"everyone who comes near, who comes near to the tabernacle of the LORD dies" — the doubled participle\'s one seat'); ink('18:7', '"the stranger who comes near shall be put to death"'); move('Sanhedrin 84a:13 (R. Yishmael)', '"shall die" / "shall be put to death" — death by Heaven')
        return out("whoever comes near dies (17:28) with 18:7's shall be put to death — R. Yishmael: death by Heaven (Sanhedrin 84a)", ['death_by_heaven'])
    return out('no verdict in span', [FX.NONE])
