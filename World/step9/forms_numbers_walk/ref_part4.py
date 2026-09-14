# ===== F4: THE MANSLAYER (Num 35:22-28) =====================================================================
def the_manslayer(case, data):
    del P[:]
    ask = case['ask']
    if ask == 'suddenly':
        ink('35:22', '"and if suddenly, without enmity, he thrust him or threw at him any instrument without lying-in-wait" — "suddenly" %s (the nazirite\'s word — the two Bible seats both this book\'s); "without enmity" %s, "without lying-in-wait" %s' % (SUDDENLY, WITHOUT_ENMITY, WITHOUT_LYING))
        move('Makkot 7b:6 (the baraita); Keritot 9a:19', "'suddenly' excludes the corner; 'without enmity' the enemy; 'he thrust him' includes the shove; 'or cast upon him' the downward-for-upward; 'without lying in wait' the stone thrown aside; 'unexpectedly' = unwitting as the nazirite's")
        return out("suddenly (35:22) — the nazirite's word (6:9, the naso runner's seat); the baraita's five marks read word by word (Makkot 7b:6)", ['flees_to_refuge'])
    if ask == 'without_seeing':
        ink('35:23', '"or with any stone whereby he may die, without seeing" — %s one seat; "whereby he may die" %s' % (WITHOUT_SEEING, WHEREBY_F))
        move('Makkot 9b:5-8; Bava Kamma 86b:17-19; Nedarim 87b:5', "R. Yehuda excludes the blind, R. Meir includes (a restriction after a restriction)")
        dat('the row the_blind_killer: %s' % data['the_blind_killer']['value'])
        return out("without seeing (35:23) — the blind killer disputed (R. Yehuda exempt, R. Meir exiled): a data row", ['flees_to_refuge'])
    if ask == 'the_downward_motion':
        ink('35:23', '"and he dropped it on him and he died" — %s one seat; the narrative verbs inside the cases %s' % (DROPPED, NARR))
        move('cold_run_mishpatim_3 (CALL) — M3.killer(refuge_by_descent) = %s' % M3_DESCENT['v'], "Shmuel from 35:23: exile only for a downward motion (Makkot 7b:2) — Mishnah Makkot 2:1's rows at their second seat; the butcher and the rung (7b:8-16)")
        return out("the downward motion (35:23 'and he dropped it') — descent exiles, ascent does not (Mishnah Makkot 2:1 by CALL; Makkot 7b:2)", ['flees_to_refuge'])
    if ask == 'not_his_enemy':
        ink('35:23', '"and he was not his enemy nor sought his harm" — %s one seat' % NOT_ENEMY)
        move('Sanhedrin 29a:6; Mishnah Sanhedrin 3:5; Makkot 9b:9-13 (R. Shimon)', "'not his enemy' testifies, 'nor sought his harm' judges; the enemy not exiled (R. Yosei: executed as forewarned; R. Shimon: by the circumstances)")
        return out("not his enemy (35:23) — the hater of three days off the witness stand and the bench (Sanhedrin 29a:6); the enemy's exile by the circumstances (R. Shimon)", ['accepted'])
    if ask == 'the_congregation_judges':
        ink('35:24', '"and the congregation shall judge between the smiter and the avenger of blood on these judgments" — %s one seat; "these judgments" %s; the congregation-token %s (12, 24, 25, 25)' % (CONG_JUDGE, THESE_JUDG, CONG_TOKENS))
        move('Mishnah Sanhedrin 1:6; Sanhedrin 2a:14-2b:1; Sifrei 160:8', "ten and ten and three — the court of TWENTY-THREE from the two congregations")
        dat('the row the_court_of_twenty_three: %d' % data['the_court_of_twenty_three']['value'])
        return out("the congregation judges (35:24) — the court of twenty-three built from the congregation-tokens (the Sifrei 160:8; Mishnah Sanhedrin 1:6): a data row", ['accepted'])
    if ask == 'the_deliverance':
        ink('35:25', '"and the congregation shall deliver the manslayer from the hand of the avenger of blood and return him to his city of refuge where he fled, and he shall dwell in it until the death of the high priest" — %s one seat; Onkelos renders "deliver" with the refuge-root' % CONG_DELIVER)
        move('Makkot 10b:14; 9b:17', "the court's three verbs — the murderer executed, the free freed ('deliver'), the exiled RESTORED ('return him')")
        return out("the deliverance (35:25) — the court returns him: flees_to_refuge (Exodus 21:13's effect at its second seat) and dwells_in_refuge, the term's open entry", ['flees_to_refuge', 'dwells_in_refuge'])
    if ask == 'the_term':
        ink('35:25, 28, 32', '"until the death of the high priest" %s; "the high priest" DEFECTIVE only here %s (three tokens %s; plene %d seats, Joshua 20:6 among them); "who was anointed with the holy oil" %s; "until the death of the priest" %s (35:32 bare)' % (UNTIL_DEATH_HP, HP_DEF, HP_DEF_TOK, len(HP_PLENE), ANOINTED, UNTIL_DEATH_PRIEST))
        move('cold_run_chukat (CALL) — CK.edom_and_hor(succession) = %s' % CK_SUCC[0], "THE OFFICE'S HOLDER: Eleazar since (40, 5, 1); his death Joshua 24:33 (computed: %s) — OUTSIDE THE TORAH" % ELEAZAR_DIED)
        move('cold_run_priesthood (CALL) — PH.family(nezer) = %s' % PH_NEZER['v'], "Leviticus 21:10-12's anointed and many-garmented — the definition; Makkot 11a:12's three high priests from the three seats of the death clause")
        dat('the row the_three_high_priests: %s; the row the_terms_rows: %s — THE DESIGN\'S DECISION (e): an open BODY entry closed by the death ACT, no day-timer' % (data['the_three_high_priests']['value'], data['the_terms_rows']['value']))
        return out("the term (35:25, 28, 32) — until the death of the high priest (defective only here): an open entry on the manslayer closed by the office-holder's death act; the holder Eleazar by CALL, his death outside the Torah; the three high priests as data", ['dwells_in_refuge'])
    if ask == 'the_border':
        ink('35:26-27', '"and if going out he goes out beyond the border of his city of refuge … and the avenger finds him outside the border … and the avenger slays the manslayer — he has no blood": "going out he goes out" %s (Jacob\'s at Genesis 27:30), "the border of his city of refuge" %s, "he has no blood" %s (the burglar\'s "he has no bloods" %s — the singular here); "and he slays" the consecutive perfect' % (GOING_OUT, BORDER_REFUGE, NO_BLOOD, NO_BLOODS))
        move('cold_run_mishpatim_3 (CALL) — M3.burglar(judged_by_his_end) = %s' % M3_END['v'], "Exodus 22:1's 'no blood' at its second seat — the effect has_blood reused: the avenger clear")
        move('Makkot 12a:8-15', "R. Yosei HaGelili a mitzva, R. Akiva a license (the verb's mood); the doubled verb — deliberate or unwitting exit; Abaye: the end not severer than the beginning")
        dat('the row the_border_rows: %s' % data['the_border_rows']['value'])
        return out("the border (35:26-27) — outside the border the avenger has no blood: the burglar's clause reused (has_blood no_blood by CALL); the doubled infinitive and the mood disputed (Makkot 12a)", ['has_blood', 'exempt'])
    if ask == 'the_return':
        ink('35:28', '"for in his city of refuge he shall dwell until the death of the high priest, and after the death of the high priest the manslayer shall return to the land of his possession" — "the land of his possession" %s one seat; "he shall return" the simple stem %s' % (LAND_POSS, RETURN_STEM))
        move('Sifrei 161:5; Makkot 13a:4-6; 11b:12', "'he will return', not 'bring back' — the stem read; to his land, not his fathers' honor (R. Yehuda) or even to it (R. Meir); his bones after the death")
        return out("the return (35:28) — after the death of the high priest to the land of his possession: returns_to_his_possession written at the term's close; the stem read (Sifrei 161:5)", ['returns_to_his_possession'])
    if ask == 'the_uncertainty':
        ink('35:22-23', 'the marks of the unwitting — suddenly, without enmity, without lying-in-wait, without seeing, not his enemy: a killing the ink names neither way')
        move('Sifrei 160:8 (Issi ben Akiva); Makkot 7b:4 (Rava)', "a two-way uncertainty — neither death nor exile; 'the one who says it is permitted' neither executed nor exiled")
        dat('the row the_uncertainty: %s — the TEIKU form (the vows\' precedent)' % data['the_uncertainty']['value'])
        return out("unresolved", ['exempt'])
    if ask == 'father_and_son':
        move('cold_run_mishpatim_3 (CALL) — M3.killer(father_and_son) = %s; M3.killer(guile_excludes) = %s' % (M3_FATHER['v'], M3_GUILE['v']), "Mishnah Makkot 2:3 — each exiles for the other; the office's exemptions (the father, the teacher, the court's agent — Mishnah 2:2; Makkot 8a:6, 8b:8-14)")
        return out("the father and the son (Mishnah Makkot 2:3 by CALL) — each exiles for the other; the office's exemptions (Abba Shaul) by CALL", ['flees_to_refuge'])
    if ask == 'the_levite_exiled':
        move('Mishnah Makkot 2:7; Makkot 12b:9; Zevachim 117a:7', "a Levite from district to district; the exile who killed in his city to another neighborhood ('for in HIS city of refuge', 35:28)")
        dat('the row the_exiles_rows: the_levite_exiled')
        return out("the Levite exiled (Makkot 12b:9) — from district to district; the exile who killed again to another neighborhood: a data row", ['flees_to_refuge'])
    if ask == 'the_honor':
        move('Mishnah Makkot 2:8; 2:5; Makkot 10a:10, 10b:1', "'I am a murderer'; the roads and the signs; the teacher exiled with the student")
        dat('the row the_exiles_rows: the_honor / the_roads / the_teacher')
        return out("the exile's honor, roads and teacher (Mishnah Makkot 2:5, 2:8; Makkot 10a-10b) — the shelf's rows as data", ['accepted'])
    return out('no verdict in span', [FX.NONE])


# ===== F5: THE STATUTE (Num 35:29-34) =======================================================================
def the_statute(case, data):
    del P[:]
    ask = case['ask']
    if ask == 'a_statute_of_judgment':
        ink('35:29', '"and these shall be to you a statute of judgment for your generations in all your dwellings" — "a statute of judgment" %s (THE DAUGHTERS\' PHRASE, the two Bible seats; Onkelos "a decree of judgment" at both); "for your generations in all your dwellings" %s — LEVITICUS 3:17\'S, THE BLOOD BAN\'S formula' % (STATUTE_JUDG, GENERATIONS))
        move('cold_run_zelophehad (CALL) — ZL.inheritance_order(source_of_rule) = %s' % ZL_SRC[0], "27:11's 'a statute of judgment' — the daughters' output; this chapter's statute the second")
        move('Makkot 7a:3, 7a:7; Sanhedrin 35b:10; Yevamot 6b:10', "in all your dwellings — the Sanhedrin in the land and outside it; no execution on the Sabbath")
        return out("a statute of judgment (35:29) — the daughters' phrase (27:11 by CALL); 'in all your dwellings' the blood ban's formula: the Sanhedrin everywhere (Makkot 7a:7), never on the Sabbath", ['accepted'])
    if ask == 'the_witnesses':
        ink('35:30', '"whoever smites a soul, by the mouth of witnesses the murderer shall be slain; and one witness shall not testify against a soul to die" — "by the mouth of witnesses" %s the bare plural; "one witness" %s (the bare consonants עד inside the chapter are all "until" — the lemmas %s at 12, 25, 28, 32; the witness at 30 wears the vav, ועד "and a witness"); "shall not testify" %s — THE NINTH COMMANDMENT\'S VERB beside the sixth\'s root in one verse' % (MOUTH_WIT, ONE_WITNESS, UNTIL_LEMMAS, NOT_TESTIFY))
        move('Sifrei 161:1; Sanhedrin 33b:15; Mishnah Shevuot 4:1', "witness means two unless 'one' is written — the prototype; the one witness may answer to acquit (R. Yosei son of R. Yehuda); the oath of testimony")
        move('cold_run_lev24 (CALL) — L24.talion(kill) = %s' % L24_KILL['verdict'], "24:17's 'whoever strikes any soul' and 35:30's 'whoever smites a soul' both needed (Sanhedrin 84b:6)")
        dat('the row the_one_witness: %s' % data['the_one_witness']['value'])
        return out("the witnesses (35:30) — two by the prototype (the Sifrei 161:1); one witness not to convict, but to acquit (Sanhedrin 33b:15); the ninth commandment's verb; a data row", ['accepted'])
    if ask == 'no_ransom':
        ink('35:31', '"and you shall not take ransom for the life of a murderer who is wicked to die, for he shall surely die" — %s the two refusals; the ransom-noun\'s Torah seats by lemma %s (THE GORING OX\'S 21:30, THE HALF-SHEKEL\'S 30:12, this chapter\'s two; Genesis 6:14\'s "pitch" the lemma\'s homograph), by token %s; "wicked to die" %s' % (NO_RANSOM, RANSOM_LEMMA_T, RANSOM_TOK_T, WICKED_DIE))
        move('cold_run_mishpatim (CALL) — M1.has_lemma(Exod 21:30, 3724) = %s; the ox row %s' % (M1_RANSOM_SEAT, M1_RANSOM_ROW), "the goring ox's ransom — the noun refused here; Sanhedrin 15b:4-5: where ransom is written there is no death")
        move('Ketubot 37b:3-4, 37b:12; Bava Kamma 40a:5-12', "no money to exempt from death (the intentional); Heaven's death commuted to money — the ox's owner; the court's never")
        move('cold_run_lev24 (CALL) — L24.talion(kill) = %s' % L24_KILL['verdict'], "'no ransom for the LIFE' — but for limbs: the talion's money (Bava Kamma 83b:9-19)")
        dat('the row the_ransom_rows: %s' % data['the_ransom_rows']['value'])
        return out("no_ransom_the_death_stands", ['put_to_death'])
    if ask == 'no_ransom_for_the_fugitive':
        ink('35:32', '"and you shall not take ransom for him who fled to his city of refuge, to return to dwell in the land until the death of the priest" — the second refusal; "the priest" bare')
        move('Ketubot 37b:3-4; Makkot 11a:13; Bava Kamma 28a:11', "no money to exempt from exile (the unwitting); R. Yehuda: the war-anointed priest from the bare 'priest'; the verse lent to the Hebrew slave's eviction")
        return out("no_ransom_the_exile_stands", ['flees_to_refuge'])
    if ask == 'the_land_polluted':
        ink('35:33', '"and you shall not pollute the land in which you are, for the blood, it pollutes the land, and for the land no atonement can be made for the blood shed in it except by the blood of him who shed it" — "you shall not pollute" %s: THE POLLUTE-ROOT\'S ONLY TORAH SEAT (%d Bible verses, Psalm 106:38 among them); "no atonement" %s the passive %s — the ransom\'s root a third time; "except by the blood of him who shed it" %s' % (POLLUTE, len(POLLUTE_LEMMA_B), NO_ATONE, ATONE_STEM, EXCEPT_BLOOD))
        move('Arakhin 16a:22; Zevachim 88b:13; Mishnah Sotah 9:7; Sotah 47b:2; Shabbat 33a:4', "no atonement for the community until he dies; the heifer broken and then the killer found — he dies; for bloodshed the Presence departs")
        dat('the row the_lands_atonement: %s' % data['the_lands_atonement']['value'])
        return out("the land polluted (35:33) — the pollute-root's only Torah seat: a status on the land while the shedder stands; atoned only by his blood; the heifer's other passive Deuteronomy 21's (forward)", ['land_polluted_by_blood'])
    if ask == 'the_shedders_blood':
        ink('35:33', '"except by the blood of him who shed it" — Genesis 9:6\'s "who sheds the blood of man, by man shall his blood be shed" (%s)' % GEN9_6[:6])
        move('cold_run_primeval (CALL) — PR.cain(bloods_seats) = %s; PR.cain(exile_half) = %s; PR.sentences(east_receives) = %s' % (PR_BLOODS['v'], PR_HALF['v'], PR_EAST['v']), "the bloods of Abel; Cain's exile atoning HALF (Sanhedrin 37b:12); the manslayer's direction the east (Bereshit Rabbah 21:9); the blood_required HEAVEN entry on Noah since 9:5")
        return out("the shedder's blood (35:33) — Genesis 9:6's clause run as law (the primeval runner by CALL): Cain's exile the half-atonement, the murderer's blood the whole", ['put_to_death'])
    if ask == 'not_defile':
        ink('35:34', '"and you shall not defile the land in which you dwell" — %s one seat; Leviticus 18:25\'s "and the land was defiled … and the land vomited" (%s)' % (NOT_DEFILE, [w for w in LEV18_25 if w in ('ותטמא', 'ותקא')]))
        move('cold_run_sanctions (CALL) — SA.frame(land) = %s' % SA_VOMIT['v'], "18:25, 28; 20:22 — the land that vomits its inhabitants; Shevuot 7b:7: bloodshed an impurity by 35:34 beside the unions and Molech")
        return out("you shall not defile the land (35:34) — Leviticus 18:25-28's land that vomits (the sanctions runner by CALL); bloodshed an impurity (Shevuot 7b:7)", ['accepted'])
    if ask == 'in_whose_midst_i_dwell':
        ink('35:34', '"in whose midst I dwell, for I the LORD dwell in the midst of the children of Israel" — %s, %s, %s one seat each; THE BOOK\'S INCLUSIO: the phrase at %s (5:3\'s camp and 35:34\'s land — computed); 5:3 ends %s' % (MIDST_DWELL, I_DWELL_MIDST, FOR_I_LORD, sorted(set(INCLUSIO)), NUM5_3[-5:]))
        move('cold_run_naso (CALL) — NS.camp_purity(three_camps) = %s; (classes) = %s' % (NS_CAMPS[0], NS_CLASSES[0]), "5:3's camp guarded by the send-out — the Presence in the camp; here the Presence in the land guarded by the blood's ban")
        move('Shabbat 33a:4; Yoma 85a:14; Shevuot 7b:7; Megillah 29a:4', "the Presence departs for bloodshed; R. Yishmael reads it at the burglar's seat; an impurity; the Presence that goes with Israel into exile")
        dat('the row the_presence_rows: %s — presence_dwells OPEN on the people since Exodus 40:34, read at the checkpoint, no new write' % data['the_presence_rows']['value'])
        return out("in whose midst I dwell (35:34) — the book's inclusio with 5:3 (the naso runner by CALL): the Presence in the camp and in the land, each guarded by a ban; the open promise read, not rewritten", ['accepted'])
    if ask == 'the_closer':
        ink('36:1', 'the next chapter opens on the heads of Gilead (36:1, frozen at THE TENT) — 35:34 the last verse of the last law-chapter; 36:13 the book\'s footer with the place-stamp %s' % STAMP)
        move('Sifrei 161:5 (the Hebrew colophon)', "'the book of Numbers is completed; blessed is the man who trusts in the LORD' — the shelf's own close, dropped by the English")
        return out("the closer — 35:34 the last verse of the last law-chapter; 36:13 the footer; the Sifrei's colophon on 161:5", ['accepted'])
    return out('no verdict in span', [FX.NONE])


# ---- THE WRAP — the daemon, the scene, the narrative ------------------------------------------------------
def law_refuge(event, world):
    """Num 35:1-34 (cold_run_refuge.py F1-F5). given_at Num 35:1; installed_by boot — A LAW IN THE DIVINE VOICE IN THE PLAINS OF MOAB (35:1's
    frame with the place-stamp, 33:50's class; 35:9 bare; the class named in the registry, the second pass decides). TWO TAPE LINES: the Levite
    cities commanded (35:1-8) — ONE debit on the people (give_the_levites_cities_and_pasture_lands, counterparty the Levites, OPEN by design to
    Joshua 21); the refuge law given (35:9-34) — ONE debit on the people (appoint_six_cities_of_refuge, OPEN by design to Deuteronomy 4:41 and
    Joshua 20:7-8). The exam's three case kinds dispatch to the cells in EXPLICIT branches with LITERAL effects per kind (2b's form — an unnamed effect is a KeyError);
    THE OFFICE-HOLDER'S DEATH (high_priest_died) CLOSES every open dwells_in_refuge entry by value and writes returns_to_his_possession —
    the term's closer, an act (outside the Torah on the tape)."""
    k, src = event['kind'], event['case_source']
    E_ = lambda eff, s, cp=None, amount=None, due=None, law='', value=None: {'effect': eff, 'subject': s, 'counterparty': cp, 'amount': amount, 'due': due, 'value': value if value is not None else True, 'source_law': law, 'case_source': src}
    day = event.get('day', world.clock.day)      # THE SEQUENTIAL RUN: the event's own day
    # ---- the two lines (page_order at the counter's day, no marker in the chapter) ----
    if k == 'levite_cities_commanded':
        return [E_('commanded', 'israel', cp='the-levites', value='give_the_levites_cities_and_pasture_lands', law='F1 [INK 35:2 "command the children of Israel that they give to the Levites … cities to dwell in" … 35:7 "forty-eight cities" — the debit OPEN BY DESIGN to Joshua 21:1-42 (21:2 the request quoting the spec; 21:41 the tally; the four lots 13 + 10 + 13 + 12): THE READBACK\'s]')]
    if k == 'refuge_law_given':
        return [E_('commanded', 'israel', value='appoint_six_cities_of_refuge', law='F2 [INK 35:11 "you shall appoint for yourselves cities" … 35:14 "three cities beyond the Jordan and three in the land of Canaan" — the debit OPEN BY DESIGN to Deuteronomy 4:41-43 (Moses\' three) and Joshua 20:7-8 (the six): THE READBACK\'s]')]
    # ---- the term's closer: the office-holder's death — the daemon's own close of every open dwells_in_refuge, by value ----
    if k == 'high_priest_died':
        outp = []
        holder = event.get('priest', 'eleazar')
        for ent in list(world.entities.values()):
            for e in ent.ledger:
                if e['effect'] == 'dwells_in_refuge' and e.get('open') and e.get('value') == holder:
                    world.close(ent.eid, 'dwells_in_refuge', '%s — the death of the high priest %s closes the term (35:25, 28)' % (src, holder), value=holder)
                    outp.append(E_('returns_to_his_possession', ent.eid, value='the land of his possession (35:28)', law='F4 [INK 35:28 "and after the death of the high priest the manslayer shall return to the land of his possession" — the term closed by the act, not by a day: the design\'s decision (e)]'))
        return outp
    # ---- the exam's case kinds: EXPLICIT branches per kind (the daemon gate parses explicit branches only — the shared tuple form was refused
    #      on the first gate run, 2026-09-13), each naming LITERALLY every effect it can write (2b's form — an unnamed effect is a KeyError) ----
    if k == 'levite_cities_case':
        v, e, _ = the_levite_cities({'ask': event['ask']}, DATA); L = 'F1 [%s]' % event['ask']; s_ = event['person']
        W = {'accepted': E_('accepted', s_, value=v, law=L), 'commanded': E_('commanded', s_, cp='the-levites', value=v, law=L)}
        return [W[x] for x in e if x != FX.NONE]
    if k == 'killer_case':
        fn = {'law': the_refuge_law, 'murderer': the_murderer}.get(event.get('cell'), the_manslayer)
        v, e, _ = fn({'ask': event['ask']}, DATA); L = '%s [%s]' % ({'law': 'F2', 'murderer': 'F3'}.get(event.get('cell'), 'F4'), event['ask']); s_ = event['person']
        W = {'accepted': E_('accepted', s_, value=v, law=L), 'commanded': E_('commanded', s_, value=v, law=L), 'exempt': E_('exempt', s_, value=v, law=L),
             'put_to_death': E_('put_to_death', s_, value=v, law=L), 'flees_to_refuge': E_('flees_to_refuge', s_, value=v, law=L),
             'dwells_in_refuge': E_('dwells_in_refuge', s_, value=event.get('priest', 'eleazar'), law=L), 'has_blood': E_('has_blood', s_, value='no_blood', law=L),
             'returns_to_his_possession': E_('returns_to_his_possession', s_, value=v, law=L)}
        return [W[x] for x in e if x != FX.NONE]
    if k == 'refuge_statute_case':
        v, e, _ = the_statute({'ask': event['ask']}, DATA); L = 'F5 [%s]' % event['ask']; s_ = event['person']
        W = {'accepted': E_('accepted', s_, value=v, law=L), 'put_to_death': E_('put_to_death', s_, value=v, law=L), 'flees_to_refuge': E_('flees_to_refuge', s_, value=v, law=L),
             'land_polluted_by_blood': E_('land_polluted_by_blood', 'the-land-of-canaan', cp=s_, value=v, law=L)}
        return [W[x] for x in e if x != FX.NONE]
    return []


LINES = [
    ('Num 35:1-8 — and the LORD spoke to Moses in the plains of Moab by the Jordan at Jericho, saying: command the children of Israel that they give to the Levites from the inheritance of their possession cities to dwell in, and pasture-land for the cities round about them you shall give to the Levites; and the cities shall be theirs to dwell in and their pasture-lands for their beasts and their substance and all their living; and the pasture-lands of the cities that you shall give to the Levites: from the wall of the city outward a thousand cubits round about; and you shall measure from outside the city the east side two thousand by the cubit, and the south side two thousand by the cubit, and the west side two thousand by the cubit, and the north side two thousand by the cubit, and the city in the midst — this shall be to them the pasture-lands of the cities; and the cities that you shall give to the Levites: the six cities of refuge which you shall give for the manslayer to flee there, and beside them you shall give forty-two cities; all the cities that you shall give to the Levites: forty-eight cities, them and their pasture-lands; and the cities that you shall give from the possession of the children of Israel — from the many you shall take more and from the few you shall take less; each according to his inheritance that they inherit shall give of his cities to the Levites', 'levite_cities_commanded'),
    ('Num 35:9-34 — and the LORD spoke to Moses, saying: speak to the children of Israel and say to them: when you are crossing the Jordan to the land of Canaan, you shall appoint for yourselves cities, cities of refuge they shall be for you, and a manslayer shall flee there who smites a soul unwittingly; and the cities shall be for you a refuge from the avenger, and the manslayer shall not die until he stands before the congregation for judgment; and the cities that you shall give: six cities of refuge they shall be for you; three cities you shall give beyond the Jordan and three cities you shall give in the land of Canaan, cities of refuge they shall be; for the children of Israel and for the stranger and for the sojourner among them these six cities shall be for refuge, to flee there whoever smites a soul unwittingly; and if with an instrument of iron he struck him and he died, he is a murderer, the murderer shall surely die … the avenger of blood himself shall put the murderer to death … and if suddenly without enmity … the congregation shall judge … and deliver … and return him to his city of refuge … and he shall dwell in it until the death of the high priest … a statute of judgment for your generations in all your dwellings … by the mouth of witnesses … one witness shall not testify … you shall not take ransom … the blood, it pollutes the land … in whose midst I dwell, for I the LORD dwell in the midst of the children of Israel', 'refuge_law_given'),
]
CLOSES = 'none — the Levite cities\' debit closes at Joshua 21 and the appointment\'s at Joshua 20 OUTSIDE THE TORAH (Deuteronomy 4:41\'s three inside it, forward); no manslayer stands on the tape; the term\'s closer (the high priest\'s death) Joshua 24:33'


def scene():
    """THE SCENE — the exam's rows replayed on the world engine (the exodus epoch): the exam's persons through the three case kinds, and THE
    OFFICE-HOLDER'S DEATH closing the manslayers' open terms by value."""
    with contextlib.redirect_stdout(io.StringIO()):
        w = WE.World(era='Num 35:1-34: the refuge cities on the shelf — Makkot, Sanhedrin, Bava Kamma, Ketubot, Eruvin, Sotah, Arakhin on the engine (the exodus epoch)', epoch='exodus')
        w.laws = [law_refuge]
        w.advance(w.clock.day_in('exodus', 40, 6, 1))
        # ---- the exam's persons through the three case kinds (LITERAL submits — the daemon gate parses no loop) ----
        w.submit({'kind': 'levite_cities_case', 'subject': 'the-measure', 'person': 'the-measure', 'ask': 'the_two_thousand', 'case_source': 'Mishnah Sotah 5:3; Sotah 27b:8 — the exam\'s row the_two_thousand'})
        w.submit({'kind': 'levite_cities_case', 'subject': 'the-forty-eight', 'person': 'the-forty-eight', 'ask': 'six_and_forty_two', 'case_source': 'Makkot 10a:4 — the exam\'s row six_and_forty_two'})
        w.submit({'kind': 'levite_cities_case', 'subject': 'the-levites-gift', 'person': 'the-levites-gift', 'ask': 'the_debit', 'case_source': 'Josh 21:2 — the exam\'s row the_debit'})
        w.submit({'kind': 'levite_cities_case', 'subject': 'the-sides', 'person': 'the-sides', 'ask': 'the_four_sides', 'case_source': 'Num 2:3-25 — the exam\'s row the_four_sides'})
        w.submit({'kind': 'killer_case', 'subject': 'the-six', 'person': 'the-six', 'cell': 'law', 'ask': 'six_cities', 'case_source': 'Mishnah Makkot 2:4 — the exam\'s row six_cities'})
        w.submit({'kind': 'killer_case', 'subject': 'the-appointment', 'person': 'the-appointment', 'cell': 'law', 'ask': 'the_debit', 'case_source': 'Makkot 11a:1 — the exam\'s row the_debit'})
        w.submit({'kind': 'killer_case', 'subject': 'the-iron-striker', 'person': 'the-iron-striker', 'cell': 'murderer', 'ask': 'the_iron', 'case_source': 'Sanhedrin 76b:12 — the exam\'s row the_iron'})
        w.submit({'kind': 'killer_case', 'subject': 'the-stone-striker', 'person': 'the-stone-striker', 'cell': 'murderer', 'ask': 'the_stone_and_the_wood', 'case_source': 'Sanhedrin 76b:12 — the exam\'s row the_stone_and_the_wood'})
        w.submit({'kind': 'killer_case', 'subject': 'the-beheaded', 'person': 'the-beheaded', 'cell': 'murderer', 'ask': 'the_mode', 'case_source': 'Mishnah Sanhedrin 9:1 — the exam\'s row the_mode'})
        w.submit({'kind': 'killer_case', 'subject': 'the-hater', 'person': 'the-hater', 'cell': 'murderer', 'ask': 'the_intents', 'case_source': 'Mishnah Sanhedrin 9:2 — the exam\'s row the_intents'})
        w.submit({'kind': 'killer_case', 'subject': 'the-roller', 'person': 'the-roller', 'cell': 'manslayer', 'ask': 'the_downward_motion', 'case_source': 'Mishnah Makkot 2:1 — the exam\'s row the_downward_motion'})
        w.submit({'kind': 'killer_case', 'subject': 'the-sudden-thruster', 'person': 'the-sudden-thruster', 'cell': 'manslayer', 'ask': 'suddenly', 'case_source': 'Makkot 7b:6 — the exam\'s row suddenly'})
        w.submit({'kind': 'killer_case', 'subject': 'the-delivered', 'person': 'the-delivered', 'cell': 'manslayer', 'ask': 'the_deliverance', 'priest': 'eleazar', 'case_source': 'Makkot 10b:14 — the exam\'s row the_deliverance'})
        w.submit({'kind': 'killer_case', 'subject': 'the-exile-under-eleazar', 'person': 'the-exile-under-eleazar', 'cell': 'manslayer', 'ask': 'the_term', 'priest': 'eleazar', 'case_source': 'Makkot 11a:12 — the exam\'s row the_term'})
        w.submit({'kind': 'killer_case', 'subject': 'the-exile-under-phinehas', 'person': 'the-exile-under-phinehas', 'cell': 'manslayer', 'ask': 'the_term', 'priest': 'phinehas', 'case_source': 'Mishnah Makkot 2:6 — the exam\'s row the_term (the second high priest)'})
        w.submit({'kind': 'killer_case', 'subject': 'the-one-who-left', 'person': 'the-one-who-left', 'cell': 'manslayer', 'ask': 'the_border', 'case_source': 'Makkot 12a:8 — the exam\'s row the_border'})
        w.submit({'kind': 'killer_case', 'subject': 'the-uncertain', 'person': 'the-uncertain', 'cell': 'manslayer', 'ask': 'the_uncertainty', 'case_source': 'Sifrei Bamidbar 160:8 — the exam\'s row the_uncertainty'})
        w.submit({'kind': 'killer_case', 'subject': 'the-son-who-killed', 'person': 'the-son-who-killed', 'cell': 'manslayer', 'ask': 'father_and_son', 'case_source': 'Mishnah Makkot 2:3 — the exam\'s row father_and_son'})
        w.submit({'kind': 'refuge_statute_case', 'subject': 'the-twenty-three', 'person': 'the-twenty-three', 'ask': 'a_statute_of_judgment', 'case_source': 'Makkot 7a:7 — the exam\'s row a_statute_of_judgment'})
        w.submit({'kind': 'refuge_statute_case', 'subject': 'the-one-witness', 'person': 'the-one-witness', 'ask': 'the_witnesses', 'case_source': 'Sanhedrin 33b:15 — the exam\'s row the_witnesses'})
        w.submit({'kind': 'refuge_statute_case', 'subject': 'the-ransomer', 'person': 'the-ransomer', 'ask': 'no_ransom', 'case_source': 'Ketubot 37b:3 — the exam\'s row no_ransom'})
        w.submit({'kind': 'refuge_statute_case', 'subject': 'the-fugitive-ransomer', 'person': 'the-fugitive-ransomer', 'ask': 'no_ransom_for_the_fugitive', 'case_source': 'Ketubot 37b:4 — the exam\'s row no_ransom_for_the_fugitive'})
        w.submit({'kind': 'refuge_statute_case', 'subject': 'the-unexecuted-shedder', 'person': 'the-unexecuted-shedder', 'ask': 'the_land_polluted', 'case_source': 'Arakhin 16a:22 — the exam\'s row the_land_polluted'})
        w.submit({'kind': 'refuge_statute_case', 'subject': 'the-shedder', 'person': 'the-shedder', 'ask': 'the_shedders_blood', 'case_source': 'Gen 9:6 — the exam\'s row the_shedders_blood'})
        w.submit({'kind': 'refuge_statute_case', 'subject': 'the-camp-and-the-land', 'person': 'the-camp-and-the-land', 'ask': 'in_whose_midst_i_dwell', 'case_source': 'Shabbat 33a:4 — the exam\'s row in_whose_midst_i_dwell'})
        # ---- THE OFFICE-HOLDER'S DEATH: the act that closes the term — Eleazar's (Joshua 24:33, outside the Torah), then Phinehas's (the second high priest's) ----
        w.advance(w.clock.day + 7)
        w.submit({'kind': 'high_priest_died', 'subject': 'eleazar', 'priest': 'eleazar', 'office': 'the high priest', 'case_source': 'Josh 24:33 — and Eleazar son of Aaron died; the exam\'s act: the term closed by the death (Makkot 11a:12)'})
        w.submit({'kind': 'high_priest_died', 'subject': 'phinehas', 'priest': 'phinehas', 'office': 'the high priest', 'case_source': 'Mishnah Makkot 2:6 — the second high priest\'s death returns the one sentenced in his days'})
    n = lambda eid, eff: len([e for e in w.entity(eid).ledger if e['effect'] == eff])
    o = lambda eid, eff: len([e for e in w.entity(eid).ledger if e['effect'] == eff and e.get('open')])
    tset = len([l for l in w.log if l[0] == 'TIMER-SET']); tfire = len([l for l in w.log if l[0] == 'TIMER-FIRE']); tcan = len([l for l in w.log if l[0] == 'TIMER-CANCEL'])
    closes = len([e for ent in w.entities.values() for e in ent.ledger if e.get('closed_by')])
    return ((n('the-measure', 'accepted'), n('the-forty-eight', 'accepted'), n('the-levites-gift', 'commanded'), n('the-sides', 'accepted'),
             n('the-six', 'accepted'), n('the-appointment', 'commanded'), n('the-iron-striker', 'put_to_death'), n('the-stone-striker', 'put_to_death'), n('the-beheaded', 'put_to_death'), n('the-hater', 'put_to_death'),
             n('the-roller', 'flees_to_refuge'), n('the-sudden-thruster', 'flees_to_refuge'), n('the-delivered', 'flees_to_refuge'), n('the-delivered', 'dwells_in_refuge'), o('the-delivered', 'dwells_in_refuge'), n('the-delivered', 'returns_to_his_possession'),
             n('the-exile-under-eleazar', 'dwells_in_refuge'), o('the-exile-under-eleazar', 'dwells_in_refuge'), n('the-exile-under-eleazar', 'returns_to_his_possession'),
             n('the-exile-under-phinehas', 'dwells_in_refuge'), o('the-exile-under-phinehas', 'dwells_in_refuge'), n('the-exile-under-phinehas', 'returns_to_his_possession'),
             n('the-one-who-left', 'has_blood'), n('the-one-who-left', 'exempt'), n('the-uncertain', 'exempt'), n('the-son-who-killed', 'flees_to_refuge'),
             n('the-twenty-three', 'accepted'), n('the-one-witness', 'accepted'), n('the-ransomer', 'put_to_death'), n('the-fugitive-ransomer', 'flees_to_refuge'), n('the-land-of-canaan', 'land_polluted_by_blood'), n('the-shedder', 'put_to_death'), n('the-camp-and-the-land', 'accepted')),
            (tset, tfire, tcan, len(w.timers)), len(w.entities), closes), w
SCENE, _W = scene()
# THE PREDICTION (typed before the first run — the scratchpad's ref_scene_predict.py, run BEFORE this runner existed): every exam person written once per
# effect; the three manslayers' dwells_in_refuge SET at the sentence (the-delivered, the-exile-under-eleazar under Eleazar; the-exile-under-phinehas under
# Phinehas), CLOSED BY THE DEATH ACT (open 0 after) with returns_to_his_possession written at the close; no timer (set 0, fired 0, cancelled 0, pending 0);
# ENTITIES: predicted 26 (the exam's 25 persons + the-land-of-canaan) — THE FIRST GRADED RUN PRINTED 25, the model's miss read as evidence: the unexecuted
# shedder's row writes land_polluted_by_blood ON THE LAND with the shedder as COUNTERPARTY (the design's decision (i)), so he is never written on and the
# engine makes no entity for him — twenty-four written-on persons + the land = 25; RETYPED FROM THE PRINT; CLOSES 3 — the three terms closed by the two deaths.
SCENE_PREDICTED = ((1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1), (0, 0, 0, 0), 25, 3)
assert SCENE == SCENE_PREDICTED, ('THE NUMBERS WALK: the scene moved from its prediction', SCENE, SCENE_PREDICTED)


def narrative():
    """THE NUMBERS WALK 15b (2026-09-13): the chapter's own acts AS HISTORY — the TWO lines of 35:1-34 at the counter's day (40, 6, 1), page-order
    after the borders' three (34:1-29) and before the tribes' plea (36:1-4), on a world with this runner's daemon: 2 writes, no timer, no marker,
    ONE entity (israel_people — the written-on party; the Levites a counterparty), no close, no row. Recorded by the sequential run's recorder and
    stitched onto the tape. Not a graded cell: the tuple below is a tripwire typed from the design; the sequence world's RUN tuple and CR1-CR9 grade
    the tape."""
    with contextlib.redirect_stdout(io.StringIO()):
        w = WE.World(era='Num 35:1-34: the refuge cities on the tape — the Levite cities commanded, the refuge law given (the exodus epoch)', epoch='exodus')
        w.laws = [law_refuge]
        w.advance(w.clock.day_in('exodus', 40, 6, 1))
        # THE DAEMON GATE READS LITERAL SUBMITS ONLY — the two lines typed out (the term's field named `term`, never `until`: the stitcher re-bases an `until` as a scene-clock day — the first stitch fell on the string, 2026-09-13)
        w.submit({'kind': 'levite_cities_commanded', 'subject': 'israel', 'cities': 48, 'refuge': 6, 'others': 42, 'thousand': 1000, 'two_thousand': 2000, 'sides': ['east', 'south', 'west', 'north'], 'case_source': LINES[0][0]})
        w.submit({'kind': 'refuge_law_given', 'subject': 'israel', 'six': 6, 'beyond_the_jordan': 3, 'in_canaan': 3, 'term': 'the death of the high priest', 'witnesses': 'plural', 'ransom': False, 'case_source': LINES[1][0]})
    writes = len([l for l in w.log if l[0] == 'WRITE'])
    closes = len([e for ent in w.entities.values() for e in ent.ledger if e.get('closed_by')])
    rows = len([l for l in w.log if l[0] == 'ROW'])
    return (writes, len([l for l in w.log if l[0] == 'TIMER-SET']), len(w.entities), w.clock.eras['exodus'].date(w.clock.day)[1:], closes, rows, len(w.tables['population'])), w


NARRATIVE, _WN = narrative()
NARRATIVE_PREDICTED = (2, 0, 1, (6, 1), 0, 0, 0)   # NUMBERS_WALK.md "Sitting 15b": 2 writes (L1 1, L2 1), no timer, ONE entity (israel_people — the written-on party; the Levites the counterparty, no entity), the counter's day (6, 1), no close, no row
assert NARRATIVE == NARRATIVE_PREDICTED, ('THE NUMBERS WALK: the refuge cities\' narrative moved from its prediction', NARRATIVE, NARRATIVE_PREDICTED)
assert [e['value'] for e in _WN.entity('israel').ledger if e['effect'] == 'commanded'] == ['give_the_levites_cities_and_pasture_lands', 'appoint_six_cities_of_refuge'] and all(e.get('open') for e in _WN.entity('israel').ledger if e['effect'] == 'commanded'), _WN.entity('israel').ledger


# =====================================================================
# Motion 2 — THE TEST DATA: the answer sheet's rows (the docket's LAW rows).
# =====================================================================
CASES = [
    # F1 — the Levite cities
    ('Num 35:2 / Sifrei 1:2; 34:2 by CALL — the command', lambda: the_levite_cities({'ask': 'the_command'}, DATA), "command the children of Israel (35:2) — the five Torah seats, this the fifth (Sifrei 1:2's five); the borders runner's cell by CALL"),
    ('Num 35:2 / Josh 21:2 — cities to dwell in', lambda: the_levite_cities({'ask': 'cities_to_dwell_in'}, DATA), "cities to dwell in (35:2) — three Bible seats: this, Joshua 14:4, and Joshua 21:2 the run's request; the debit on the people OPEN to Joshua 21"),
    ('Num 35:2-7 / Lev 25:34; Arakhin 33b:15 — the pasture-land', lambda: the_levite_cities({'ask': 'the_pasture_land'}, DATA), "the pasture-land (35:2-7) — six Torah seats, Leviticus 25:34's unsellable field and this chapter's five; 69 Bible verses, 32 Joshua 21's; the lot unchangeable (Arakhin 33b:15)"),
    ('Num 35:3 / Nedarim 81a:7; Makkot 12a:5 — their beasts', lambda: the_levite_cities({'ask': 'their_beasts'}, DATA), "their beasts (35:3) — two Bible seats; Onkelos 'their needs of life'; for life, not burial (Makkot 12a:5)"),
    ('Num 35:4 / Eruvin 56b:6 — the thousand', lambda: the_levite_cities({'ask': 'the_thousand'}, DATA), "a thousand cubits (35:4) — the Bible's one seat; the parser [1000] with the cubit consumed; the open land (Eruvin 56b:6)"),
    ('Num 35:5 / Mishnah Sotah 5:3; Eruvin 51a:8; Arakhin 9:8 — the two thousand', lambda: the_levite_cities({'ask': 'the_two_thousand'}, DATA), "two thousand by the cubit (35:5) — four times, read [2000] each by rule 29 (the bare dual marked by the sheva under the lamed); the Sabbath limit's measure (R. Akiva) — a data row with three settings"),
    ('Num 35:5 / Num 2 by CALL — the four sides', lambda: the_levite_cities({'ask': 'the_four_sides'}, DATA), "the four sides (35:5) — east, south, west, north: THE CAMP'S ORDER (Numbers 2 by CALL), against the borders' and the court's; the Levite city laid out as the camp"),
    ('Num 35:5 / Eruvin 51a:13-14 — the city in the midst', lambda: the_levite_cities({'ask': 'the_city_in_the_midst'}, DATA), "and the city in the midst (35:5) — one seat; the square (Eruvin 51a:13-14)"),
    ('Num 35:6-7 / Josh 21:4-7, 41; Makkot 10a:4 — six and forty-two', lambda: the_levite_cities({'ask': 'six_and_forty_two'}, DATA), "six and forty-two (35:6-7) — [6, 42] and [48], the sum asserted; Joshua 21's four lots 13 + 10 + 13 + 12 = 48 by the parser, the tally reads it; the forty-two receive too (Makkot 10a:4)"),
    ('Num 35:8 / 26:54 by CALL — the rule', lambda: the_levite_cities({'ask': 'the_rule'}, DATA), "the proportional rule (35:8) — 26:54's rule at its third seat by CALL; 'you shall take less' plural here alone"),
    ('Num 18:20-24, 26:62 by CALL — no inheritance', lambda: the_levite_cities({'ask': 'no_inheritance'}, DATA), "the Levites have no inheritance (18:20-24; 26:62 by CALL) — the cities the people's gift 'from the inheritance of their possession' (35:2), the block standing"),
    ('Num 35:2-8 / Josh 21 — the debit', lambda: the_levite_cities({'ask': 'the_debit'}, DATA), "the debit (35:2-8) — 'you shall give' ten times: commanded on the people, counterparty the Levites, OPEN by design to Joshua 21"),
    # F2 — the refuge law
    ('Num 35:10 / 33:51 by CALL — when you cross', lambda: the_refuge_law({'ask': 'when_you_cross'}, DATA), "when you are crossing the Jordan (35:10) — 33:51's clause by CALL (Deuteronomy 11:31 the third); 'to Canaan-ward' the directional form's Torah last"),
    ('Num 35:11 / Sifrei 159:1 — appoint', lambda: the_refuge_law({'ask': 'appoint'}, DATA), "you shall appoint (35:11) — one seat; designation, not a meeting (Balaam's root FALSE by sense); after the inheritance (Sifrei 159:1)"),
    ('Num 35:11 / Exod 21:13 by CALL; Makkot 12b:8 — the place become cities', lambda: the_refuge_law({'ask': 'the_place_become_cities'}, DATA), "the place become cities — Exodus 21:13's 'he shall flee there' at its Numbers seat: the Levites' cities for the generations, the Levite camp for the hour (M3 by CALL)"),
    ('Num 35:13-15 / Deut 4:43; Josh 20:7-8; Mishnah Makkot 2:4 — six cities', lambda: the_refuge_law({'ask': 'six_cities'}, DATA), "six cities (35:13-15) — [6], [3, 3], [6]: three and three; the names Deuteronomy 4:43's and Joshua 20:7-8's, none here; not until all six (Makkot 2:4): a data row"),
    ('Num 35:15 / Makkot 9a — for whom', lambda: the_refuge_law({'ask': 'for_whom'}, DATA), "for whom (35:15) — Israel, the stranger and the sojourner against 35:12's 'for you': the sojourner for a sojourner only (Makkot 9a); Joshua 20:9 drops the sojourner"),
    ('Num 35:11, 15 / Num 15 by CALL — unwittingly', lambda: the_refuge_law({'ask': 'unwittingly'}, DATA), "unwittingly (35:11, 15) — the sin offering's word (thirteen seats; the shelach runner by CALL); Deuteronomy's 'without knowledge'; Joshua 20:3 both"),
    ('Num 35:12 / Makkot 12a:11; Onkelos 35:19, 21 — until he stands', lambda: the_refuge_law({'ask': 'until_he_stands'}, DATA), "until he stands before the congregation (35:12) — the court before the avenger's hand (Makkot 12a:11; Onkelos' clause at 19, 21); Joshua 20:6 quotes it"),
    ('Num 35:11-14 / Deut 4:41; Josh 20:7-8 — the debit', lambda: the_refuge_law({'ask': 'the_debit'}, DATA), "the debit (35:11-14) — appoint six cities: commanded on the people, OPEN by design to Deuteronomy 4:41 and Joshua 20:7-8"),
    # F3 — the murderer
    ('Num 35:16 / Sanhedrin 76b:12-13 — the iron', lambda: the_murderer({'ask': 'the_iron'}, DATA), "the iron (35:16) — no 'hand', no size clause: iron of any size kills (Sanhedrin 76b:12-13); the parameter's exemption stated by the shelf"),
    ('Num 35:17-18 / Sanhedrin 76b:12; Sifrei 160:3-5 — the stone and the wood', lambda: the_murderer({'ask': 'the_stone_and_the_wood'}, DATA), "the stone and the wood (35:17-18) — 'of the hand whereby he may die': the size a PARAMETER (Sanhedrin 76b:12; the Sifrei's induction from three)"),
    ('Num 35:16-18, 21 / Sanhedrin 15b:5 — he is a murderer', lambda: the_murderer({'ask': 'he_is_a_murderer'}, DATA), "he is a murderer (35:16-18, 21) — four seats; 'shall surely die' five times, the Torah's densest; one root for four agents, defective at every Numbers seat"),
    ('Mishnah Sanhedrin 9:1 by CALL; Ketubot 37b:7 — the mode', lambda: the_murderer({'ask': 'the_mode'}, DATA), "the mode — the sword (M3 by CALL; Sanhedrin 9:1), from the neck (Ketubot 37b:7); any mode when the sword cannot be done (the doubled verb)"),
    ('Num 35:19, 21 / Sanhedrin 45b:13; Makkot 12a — the avenger\'s hand', lambda: the_murderer({'ask': 'the_avengers_hand'}, DATA), "the avenger's hand (35:19, 21) — the avenger puts him to death after the court; none — the court appoints one (Sanhedrin 45b:13); a data row with its arms"),
    ('Num 35:20-21 / Sanhedrin 76b:15; Mishnah Sanhedrin 9:1 — the manners', lambda: the_murderer({'ask': 'the_manners'}, DATA), "the manners (35:20-21) — thrust, threw, struck with the hand; the confiner a murderer (Sanhedrin 76b:15); the causation line the shelf's (a data row)"),
    ('Num 35:20-22 / Mishnah Sanhedrin 9:2; Sanhedrin 41a by CALL — the intents', lambda: the_murderer({'ask': 'the_intents'}, DATA), "the intents (35:20-22) — hatred, lying-in-wait (Exodus 21:13's verb as a noun), enmity (the serpent's word) against their negations: the intent's table (Sanhedrin 9:2) a data row; the forewarning a parameter by CALL"),
    ('Num 35:21, 24 / Lev 24:17 by CALL — the smiter', lambda: the_murderer({'ask': 'the_smiter'}, DATA), "the smiter (35:21, 24) — the active participle at seven Torah seats, the smitten woman its passive homograph; Leviticus 24:17's smiter by CALL"),
    ('Num 35:16-23 — the case table', lambda: the_murderer({'ask': 'the_table'}, DATA), "the case table (35:16-23) — computed from the tokens: the instruments, the manners, the intents; the verdicts a murderer, a manslayer, neither"),
    # F4 — the manslayer
    ('Num 35:22 / Makkot 7b:6; Num 6:9 — suddenly', lambda: the_manslayer({'ask': 'suddenly'}, DATA), "suddenly (35:22) — the nazirite's word (6:9, the naso runner's seat); the baraita's five marks read word by word (Makkot 7b:6)"),
    ('Num 35:23 / Makkot 9b:5 — without seeing', lambda: the_manslayer({'ask': 'without_seeing'}, DATA), "without seeing (35:23) — the blind killer disputed (R. Yehuda exempt, R. Meir exiled): a data row"),
    ('Num 35:23 / Mishnah Makkot 2:1 by CALL; Makkot 7b:2 — the downward motion', lambda: the_manslayer({'ask': 'the_downward_motion'}, DATA), "the downward motion (35:23 'and he dropped it') — descent exiles, ascent does not (Mishnah Makkot 2:1 by CALL; Makkot 7b:2)"),
    ('Num 35:23 / Sanhedrin 29a:6 — not his enemy', lambda: the_manslayer({'ask': 'not_his_enemy'}, DATA), "not his enemy (35:23) — the hater of three days off the witness stand and the bench (Sanhedrin 29a:6); the enemy's exile by the circumstances (R. Shimon)"),
    ('Num 35:24 / Mishnah Sanhedrin 1:6; Sifrei 160:8 — the congregation judges', lambda: the_manslayer({'ask': 'the_congregation_judges'}, DATA), "the congregation judges (35:24) — the court of twenty-three built from the congregation-tokens (the Sifrei 160:8; Mishnah Sanhedrin 1:6): a data row"),
    ('Num 35:25 / Makkot 10b:14 — the deliverance', lambda: the_manslayer({'ask': 'the_deliverance'}, DATA), "the deliverance (35:25) — the court returns him: flees_to_refuge (Exodus 21:13's effect at its second seat) and dwells_in_refuge, the term's open entry"),
    ('Num 35:25, 28, 32 / 20:28 and Lev 21:10 by CALL; Makkot 11a:12 — the term', lambda: the_manslayer({'ask': 'the_term'}, DATA), "the term (35:25, 28, 32) — until the death of the high priest (defective only here): an open entry on the manslayer closed by the office-holder's death act; the holder Eleazar by CALL, his death outside the Torah; the three high priests as data"),
    ('Num 35:26-27 / Exod 22:1 by CALL; Makkot 12a:8-15 — the border', lambda: the_manslayer({'ask': 'the_border'}, DATA), "the border (35:26-27) — outside the border the avenger has no blood: the burglar's clause reused (has_blood no_blood by CALL); the doubled infinitive and the mood disputed (Makkot 12a)"),
    ('Num 35:28 / Sifrei 161:5; Makkot 13a:6 — the return', lambda: the_manslayer({'ask': 'the_return'}, DATA), "the return (35:28) — after the death of the high priest to the land of his possession: returns_to_his_possession written at the term's close; the stem read (Sifrei 161:5)"),
    ('Sifrei 160:8 (Issi ben Akiva); Makkot 7b:4 — the uncertainty', lambda: the_manslayer({'ask': 'the_uncertainty'}, DATA), "unresolved"),
    ('Mishnah Makkot 2:2-3 by CALL — the father and the son', lambda: the_manslayer({'ask': 'father_and_son'}, DATA), "the father and the son (Mishnah Makkot 2:3 by CALL) — each exiles for the other; the office's exemptions (Abba Shaul) by CALL"),
    ('Makkot 12b:9 — the Levite exiled', lambda: the_manslayer({'ask': 'the_levite_exiled'}, DATA), "the Levite exiled (Makkot 12b:9) — from district to district; the exile who killed again to another neighborhood: a data row"),
    ('Mishnah Makkot 2:5, 2:8; Makkot 10a-10b — the honor, the roads, the teacher', lambda: the_manslayer({'ask': 'the_honor'}, DATA), "the exile's honor, roads and teacher (Mishnah Makkot 2:5, 2:8; Makkot 10a-10b) — the shelf's rows as data"),
    # F5 — the statute
    ('Num 35:29 / 27:11 by CALL; Makkot 7a:7 — a statute of judgment', lambda: the_statute({'ask': 'a_statute_of_judgment'}, DATA), "a statute of judgment (35:29) — the daughters' phrase (27:11 by CALL); 'in all your dwellings' the blood ban's formula: the Sanhedrin everywhere (Makkot 7a:7), never on the Sabbath"),
    ('Num 35:30 / Sifrei 161:1; Sanhedrin 33b:15 — the witnesses', lambda: the_statute({'ask': 'the_witnesses'}, DATA), "the witnesses (35:30) — two by the prototype (the Sifrei 161:1); one witness not to convict, but to acquit (Sanhedrin 33b:15); the ninth commandment's verb; a data row"),
    ('Num 35:31 / Exod 21:30 by CALL; Ketubot 37b — no ransom', lambda: the_statute({'ask': 'no_ransom'}, DATA), "no_ransom_the_death_stands"),
    ('Num 35:32 / Ketubot 37b:4; Makkot 11a:13 — no ransom for the fugitive', lambda: the_statute({'ask': 'no_ransom_for_the_fugitive'}, DATA), "no_ransom_the_exile_stands"),
    ('Num 35:33 / Arakhin 16a:22; Mishnah Sotah 9:7 — the land polluted', lambda: the_statute({'ask': 'the_land_polluted'}, DATA), "the land polluted (35:33) — the pollute-root's only Torah seat: a status on the land while the shedder stands; atoned only by his blood; the heifer's other passive Deuteronomy 21's (forward)"),
    ('Num 35:33 / Gen 9:6 by CALL; Sanhedrin 37b:12 — the shedder\'s blood', lambda: the_statute({'ask': 'the_shedders_blood'}, DATA), "the shedder's blood (35:33) — Genesis 9:6's clause run as law (the primeval runner by CALL): Cain's exile the half-atonement, the murderer's blood the whole"),
    ('Num 35:34 / Lev 18:25-28 by CALL; Shevuot 7b:7 — not defile', lambda: the_statute({'ask': 'not_defile'}, DATA), "you shall not defile the land (35:34) — Leviticus 18:25-28's land that vomits (the sanctions runner by CALL); bloodshed an impurity (Shevuot 7b:7)"),
    ('Num 35:34 / 5:3 by CALL; Shabbat 33a:4 — in whose midst I dwell', lambda: the_statute({'ask': 'in_whose_midst_i_dwell'}, DATA), "in whose midst I dwell (35:34) — the book's inclusio with 5:3 (the naso runner by CALL): the Presence in the camp and in the land, each guarded by a ban; the open promise read, not rewritten"),
    ('Num 35:34 / 36:1, 36:13; Sifrei 161:5 — the closer', lambda: the_statute({'ask': 'the_closer'}, DATA), "the closer — 35:34 the last verse of the last law-chapter; 36:13 the footer; the Sifrei's colophon on 161:5"),
]


if __name__ == '__main__':
    ok = 0
    frac = {'INK': 0, 'MOVE': 0, 'DATA': 0, 'HYP': 0}
    used_effects = []
    print()
    for label, fn, want in CASES:
        got, effects, prov = fn()
        hit = got == want
        ok += hit
        kinds = [k for k, _ in prov]
        cls = 'HYP' if 'HYP' in kinds else ('INK' if all(k == 'INK' for k in kinds) else ('MOVE' if 'MOVE' in kinds else 'DATA'))
        frac[cls] += 1
        print('%s  [%s]  %s' % ('PASS' if hit else 'MISS', cls, label))
        if not hit:
            print('      expected: %s' % (want,))
            print('      got     : %s' % (got,))
        used_effects += effects
        for line in FX.render(effects):
            print('        ->%s' % line)
    print()
    print('WATCH COVERAGE (the wrap):')
    _W.print_coverage()
    print('MATRIX: %d/%d cells match the answer sheet' % (ok, len(CASES)))
    tot = len(CASES)
    print('FRACTIONS: pure ink %d/%d (%.0f%%) · named moves %d/%d (%.0f%%) · data %d/%d (%.0f%%) · hypotheses %d/%d (the H class, counted apart — never as compiled)' %
          (frac['INK'], tot, 100.0 * frac['INK'] / tot, frac['MOVE'], tot, 100.0 * frac['MOVE'] / tot, frac['DATA'], tot, 100.0 * frac['DATA'] / tot, frac['HYP'], tot))
    ops = FX.summarize(used_effects)
    print('LEDGER OPS this span writes:', ', '.join('%s x%d' % kv for kv in sorted(ops.items())))
    print('THE INK: integers %s; the dual marked %s; the unit noun %s; starred none; the frame verbs %s (two divine frames, the place-stamp at the first); the narrative verbs inside the cases %s; the case tokens %s' % (sorted(INTS.items()), TILDE, UNIT, FRAME_VERBS, NARR, CASE_TOKENS))
    print('THE MURDER-ROOT: %d tokens in the chapter (%d Torah verses, %d Bible); plene %s; the refuge-word %d Bible verses, Torah %s; "shall surely die" %d Torah seats, five here; the ransom-noun Torah %s; the pollute-root Torah %s' % (len(MURDER_TOK_35), len(MURDER_T), len(MURDER_B), MURDER_PLENE, len(REFUGE_B), len(REFUGE_T), len(SURELY_DIE_T), RANSOM_LEMMA_T, POLLUTE_LEMMA_T))
    print('THE TWIN SPECS: %s; THE INCLUSIO: %s; the six cities\' names by seat: %s' % (TWIN, sorted(set(INCLUSIO)), {k: len(v) for k, v in SIX_NAMES.items()}))
    print('THE SCENE on the bench: %s; the timers (set, fired, cancelled, pending) %s; entities %d; closes %d' % SCENE)
    print('THE NARRATIVE: %s' % (NARRATIVE,))
    print('THE PARAMETER ROWS: ' + '; '.join('%s = %s' % (k, DATA[k]['value']) for k in DATA) + ' (the other settings recorded in DATA)')
    if ok == len(CASES):
        print('\nTHE COMPILE OF THE REFUGE CITIES: the answer sheet REPRODUCED — %d/%d' % (ok, len(CASES)))
    sys.exit(0 if ok == len(CASES) else 1)
