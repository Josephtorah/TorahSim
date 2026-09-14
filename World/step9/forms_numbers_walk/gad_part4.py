

# ---- THE WRAP — the daemon, the scene, the narrative ------------------------------------------------------
def law_gad_reuben(event, world):
    """Num 32:1-42 (cold_run_gad_reuben.py F1-F8). given_at Num 32:20; installed_by boot — A STIPULATION IN MOSES' VOICE WITH NO DIVINE
    FRAME (30:2's class; the class named in the registry, the second pass decides). TWELVE TAPE LINES: the request a plea on the ink's
    compound party; the rebuke, the offer, the acceptances and the answer NO WRITE (the oath retold is read against chapter 14's ledger);
    THE CONDITION two DEBITS on the compound party — to cross armed before the LORD until the land is subdued (OPEN BY DESIGN: the release
    Joshua 22:1-9 outside the Torah) and to build cities and folds (CLOSED by value at 32:34-38); the commission's debit OPEN; the grant
    THREE TRANSFERS from Israel's possession by conquest; the cities as statuses; Machir's sons, Jair and Nobah as the land possessed. The
    exam's four case kinds dispatch to the cells with LITERAL effects per kind (2b's form — an unnamed effect is a KeyError)."""
    k, src = event['kind'], event['case_source']
    E_ = lambda eff, s, cp=None, amount=None, due=None, law='', value=None: {'effect': eff, 'subject': s, 'counterparty': cp, 'amount': amount, 'due': due, 'value': value if value is not None else True, 'source_law': law, 'case_source': src}
    day = event.get('day', world.clock.day)      # THE SEQUENTIAL RUN: the event's own day
    # ---- the twelve lines (page_order at the counter's day, no marker in the chapter) ----
    if k == 'land_requested':
        return [E_('plea_made', 'the-sons-of-gad-and-reuben', value='let this land be given to your servants for a possession; do not bring us over the Jordan (32:5)', law='F1 [INK 32:1-5 "and the sons of Gad and the sons of Reuben came and spoke to Moses and to Eleazar the priest and to the princes of the congregation" — 27:2\'s triad WITHOUT the halt; the nine cities; "a possession" Genesis 47:11\'s word; the STATUS a spoken request writes on the one asked (Hobab\'s form); the row the_order_of_the_offer]')]
    if k == 'moses_rebuked_the_tribes':
        return []                                                              # NO WRITE — the oath retold (32:8-13) is read against the shelach daemon's ledger (CG3): sentence_pronounced, the forty years' fire, caleb's holding_owed
    if k == 'tribes_offered_to_arm':
        return []                                                              # NO WRITE — the undertaking is bound at the condition's line by the utterance rule (32:24)
    if k == 'condition_stipulated':
        return [E_('commanded', 'the-sons-of-gad-and-reuben', value='cross_armed_before_the_lord_until_the_land_is_subdued', law='F4 [INK 32:20-23 "if you arm yourselves before the LORD for the war, and every armed one of you passes over the Jordan before the LORD until he has dispossessed his enemies from before him, and the land is subdued before the LORD, and afterward you return — you shall be clear before the LORD and before Israel, and this land shall be yours for a possession before the LORD; and if you do not do so, behold, you have sinned against the LORD, and know your sin which will find you" — THE DOUBLED CONDITION (Mishnah Kiddushin 3:4; the rows doubled_condition, the_conditions_four_limbs, negative_arm_outcome, the_clearance); bound by 32:24\'s "that which has gone out of your mouth you shall do" = 30:3 (VW.the_man(all_that_proceeds) by CALL — its own effect commanded); OPEN BY DESIGN: the run is JOSHUA 22:1-9 ("you have kept all that Moses the servant of the LORD commanded you ... now turn and go to your tents", 22:2-4) — outside the Torah, the Jabesh-gilead class (the captives\' sentence 31:17, Caleb\'s Hebron 14:24)]'),
                E_('commanded', 'the-sons-of-gad-and-reuben', value='build_cities_and_folds', law='F4 [INK 32:24 "build for yourselves cities for your little ones and folds for your sheep" — Moses\' order (the children first); CLOSED BY VALUE at 32:34-38, the chapter\'s one Torah-closed debit]')]
    if k == 'tribes_accepted_the_condition':
        return []                                                              # NO WRITE — the seal on the parties' side (32:25-27); the debit stands from 32:20-24
    if k == 'commission_charged':
        return [E_('commanded', 'the-dividers-of-the-land', value='give_them_gilead_if_they_cross', law='F5 [INK 32:28-30 "and Moses commanded concerning them Eleazar the priest, and Joshua son of Nun, and the heads of the fathers of the tribes of the children of Israel: if the sons of Gad and the sons of Reuben pass over the Jordan with you, every armed one for war before the LORD, and the land is subdued before you, you shall give them the land of Gilead for a possession; and if they do not pass over armed with you, they shall take possessions among you in the land of Canaan" — THE SECOND DOUBLING (the exam\'s proof verses); the triad Joshua 14:1\'s dividers word for word; OPEN BY DESIGN: the run Joshua 1:12-18 (Joshua\'s charge) and 22:1-9 (the release), outside the Torah; Bava Batra 122a:4\'s lottery]')]
    if k == 'tribes_answered_so_will_we_do':
        return []                                                              # NO WRITE — "that which the LORD has spoken to your servants, so will we do" (32:31-32): Moses' stipulation called the LORD's word (the installed_by class's witness)
    if k == 'land_granted_east':
        rows = {r['tribe']: r['count'] for r in world.population(grain='counted', family=None) if r.get('as_of') == 'Num 26:5-51' and r.get('tribe') in ('reuben', 'gad', 'manasseh')}
        count = (rows['reuben'] + rows['gad'] + rows['manasseh'] // 2) if len(rows) == 3 else TWO_AND_A_HALF      # THE TABLE IS THE INSTRUMENT on the tape; the runner's own world has no rows — C2's counts by CALL
        assert count == TWO_AND_A_HALF, (rows, TWO_AND_A_HALF)
        val = lambda who: 'the kingdom of Sihon king of the Amorite and the kingdom of Og king of Bashan, the land with its cities in the borders (32:33) — %s; the land possessed at 21:24-25, 21:31-32, 21:35 (CK.well_and_kings(land_east) by CALL); the two and a half %d counted (26:7, 18, 34%s) against Joshua 4:13\'s %d and 1 Chronicles 5:18\'s %d' % (who, count, ' — the population table\'s rows' if len(rows) == 3 else '', FORTY_THOUSAND, CHRONICLES_COUNT)
        L = 'F6 [INK 32:33 "and Moses gave to them — to the sons of Gad and to the sons of Reuben and to half the tribe of Manasseh son of Joseph — the kingdom of Sihon king of the Amorite and the kingdom of Og king of Bashan" — the TRANSFER from Israel\'s possession by conquest (the chukat runner\'s land_possessed READ off the ledger); "on condition" is "from now" (Gittin 75b:2): the grant takes effect at once under the condition; the rows half_manassehs_stipulation, the_forty_thousand, the_land_east_status]'
        return [E_('holding_given', 'the-sons-of-gad', cp='israel', value=val('to the sons of Gad'), law=L),
                E_('holding_given', 'the-sons-of-reuben', cp='israel', value=val('to the sons of Reuben'), law=L),
                E_('holding_given', 'the-half-tribe-of-manasseh', cp='israel', value=val('to half the tribe of Manasseh son of Joseph — first named at the grant, no stipulation spoken to it (the row half_manassehs_stipulation)'), law=L)]
    if k == 'cities_built_east':
        world.close('the-sons-of-gad-and-reuben', 'commanded', 'Num 32:34-38 — and the sons of Gad built ... and the sons of Reuben built: the run of 32:24\'s "build for yourselves cities for your little ones and folds for your sheep" — the build debit CLOSED BY VALUE (the chapter\'s one Torah-closed debit)', value='build_cities_and_folds')
        return [E_('cities_built', 'the-sons-of-gad', value='%s — Dibon, Ataroth, Aroer, Atroth-shophan, Jazer, Jogbehah, Beth-nimrah, Beth-haran: fortified cities and folds for sheep (32:34-36)' % ' / '.join(GAD_CITIES), law='F7 [INK 32:34-36 — Gad\'s EIGHT from the tokens; four of the nine asked at 32:3 (Ataroth, Dibon, Jazer, Nimrah as Beth-nimrah); Dibon Gad the itinerary\'s witness (33:45-46); Dibon in Reuben\'s list at Joshua 13:17 (the row the_two_crossed_cities)]'),
                E_('cities_built', 'the-sons-of-reuben', value='%s — Heshbon, Elealeh, Kiriathaim, Nebo, Baal-meon (their names being changed) and Sibmah; and they called by names the names of the cities which they built (32:37-38)' % ' / '.join(REUBEN_CITIES), law='F7 [INK 32:37-38 — Reuben\'s SIX from the tokens; five of the nine asked (Heshbon, Elealeh, Sebam as Sibmah, Nebo, Beon as Baal-meon); "their names being changed" one seat; Nebo Moses\' grave (Sotah 13b:20; Onkelos 32:3 — the row moses_grave); Heshbon on Gad\'s border at Joshua 13:26]')]
    if k == 'gilead_taken_by_machir':
        return [E_('land_possessed', 'the-sons-of-machir', cp='the-amorite', value='Gilead taken and the Amorite who was in it dispossessed (32:39) — 21:32\'s verb; the sons of Machir son of Manasseh Genesis 50:23\'s collective, born on Joseph\'s knees', law='F8 [INK 32:39 "and the sons of Machir son of Manasseh went to Gilead and took it, and dispossessed the Amorite who was in it" — the phrase\'s two Torah seats; the conquest\'s effect (the chukat runner\'s) at its fourth seat; the row jair_and_machir_survived (Bava Batra 121b:9)]'),
                E_('holding_given', 'the-sons-of-machir', cp='moses', value='Gilead (32:40) — given by Moses to Machir son of Manasseh, the clan under the ancestor\'s name (26:29; Joshua 17:1; Deuteronomy 3:15); "and he dwelt in it"', law='F8 [INK 32:40 "and Moses gave Gilead to Machir son of Manasseh, and he dwelt in it" — the TRANSFER; Machir the clan (26:29 "Machir begot Gilead")]')]
    if k == 'villages_taken_by_jair':
        return [E_('land_possessed', 'jair', value='their villages taken and called Havvoth-jair (32:41) — the naming inside the value; six seats (Deuteronomy 3:14, Joshua 13:30, Judges 10:4, 1 Kings 4:13, 1 Chronicles 2:23)', law='F8 [INK 32:41 "and Jair son of Manasseh went and took their villages, and called them Havvoth-jair" — "went and took" at 32:41-42 alone; the rows jairs_lineage (1 Chronicles 2:21-22\'s Hezron) and jair_and_machir_survived (Bava Batra 121b:10 — "about thirty-six" at Ai read as Jair); the homograph traps in the registry]')]
    if k == 'kenath_taken_by_nobah':
        return [E_('land_possessed', 'nobah', value='Kenath and its daughters taken and called Nobah after his own name (32:42) — the naming inside the value; Kenath 1 Chronicles 2:23', law='F8 [INK 32:42 "and Nobah went and took Kenath and its daughters, and called it Nobah after his own name" — "its daughters" the villages (21:25, 21:32); Nobah and Jogbehah together at Judges 8:11 on Gideon\'s route against Midian (the place Nobah the trap)]')]
    # ---- the exam's case kinds: each names LITERALLY every effect it can write (2b's form) ----
    if k == 'stipulation_case':
        fn = the_acceptance_and_the_charge if event.get('cell') == 'charge' else the_condition
        v, e, _ = fn(dict(event, ask=event['ask']), DATA); L = '%s [%s]' % ('F5' if event.get('cell') == 'charge' else 'F4', v); s_ = event['person']
        W = {'commanded': E_('commanded', s_, value=v, law=L), 'holding_given': E_('holding_given', s_, cp='israel', value=v, law=L), 'accepted': E_('accepted', s_, value=v, law=L), 'exempt': E_('exempt', s_, value=v, law=L)}
        return [W[x] for x in e if x != FX.NONE]
    if k == 'clearance_case':
        v, e, _ = the_condition(dict(event, ask=event['ask']), DATA); L = 'F4 [%s]' % v; s_ = event['person']
        W = {'clear_before_the_lord_and_israel': E_('clear_before_the_lord_and_israel', s_, value=v, law=L), 'accepted': E_('accepted', s_, value=v, law=L), 'exempt': E_('exempt', s_, value=v, law=L)}
        return [W[x] for x in e if x != FX.NONE]
    if k == 'oath_retold_case':
        v, e, _ = the_rebuke(dict(event, ask=event['ask']), DATA); L = 'F2 [%s]' % v; s_ = event['person']
        W = {'exempt': E_('exempt', s_, value=v, law=L), 'holding_owed': E_('holding_owed', s_, cp='the-court', value=v, law=L), 'accepted': E_('accepted', s_, value=v, law=L)}
        return [W[x] for x in e if x != FX.NONE]
    if k == 'land_east_case':
        fn = {'cities': the_cities, 'machir': machir_jair_nobah, 'request': the_request}.get(event.get('cell'), the_grant)
        v, e, _ = fn(dict(event, ask=event['ask']), DATA); L = '%s [%s]' % ({'cities': 'F7', 'machir': 'F8', 'request': 'F1'}.get(event.get('cell'), 'F6'), v); s_ = event['person']
        W = {'holding_given': E_('holding_given', s_, cp='israel', value=v, law=L), 'land_possessed': E_('land_possessed', s_, cp='the-amorite', value=v, law=L), 'cities_built': E_('cities_built', s_, value=v, law=L), 'plea_made': E_('plea_made', s_, value=v, law=L), 'accepted': E_('accepted', s_, value=v, law=L), 'exempt': E_('exempt', s_, value=v, law=L)}
        return [W[x] for x in e if x != FX.NONE]
    return []


LINES = [
    ('Num 32:1-5 — and the sons of Reuben and the sons of Gad had much cattle, very numerous, and they saw the land of Jazer and the land of Gilead, and behold, the place was a place for cattle; and the sons of Gad and the sons of Reuben came and spoke to Moses and to Eleazar the priest and to the princes of the congregation: Ataroth and Dibon and Jazer and Nimrah and Heshbon and Elealeh and Sebam and Nebo and Beon, the land which the LORD smote before the congregation of Israel, is a land for cattle, and your servants have cattle; if we have found favour in your eyes, let this land be given to your servants for a possession; do not bring us over the Jordan', 'the-sons-of-gad-and-reuben'),
    ('Num 32:6-15 — and Moses said to the sons of Gad and to the sons of Reuben: shall your brothers go to war and you sit here? why do you discourage the heart of the children of Israel ... so did your fathers when I sent them from Kadesh-barnea to see the land ... and the anger of the LORD burned on that day and he swore, saying: surely none of the men who came up from Egypt, from twenty years old and upward, shall see the land which I swore to Abraham, to Isaac and to Jacob ... save Caleb son of Jephunneh the Kenizzite and Joshua son of Nun ... and he made them wander in the wilderness forty years, until all the generation that did evil in the eyes of the LORD was consumed; and behold, you have risen in your fathers\' stead, a brood of sinful men ... and you will destroy all this people', 'moses'),
    ('Num 32:16-19 — and they drew near to him and said: folds for our cattle we will build here, and cities for our little ones; and we will arm ourselves, hastening, before the children of Israel until we have brought them to their place ... we will not return to our houses until the children of Israel have inherited every man his inheritance; for we will not inherit with them across the Jordan and beyond, because our inheritance has come to us on this side of the Jordan eastward', 'the-sons-of-gad-and-reuben'),
    ('Num 32:20-24 — and Moses said to them: if you do this thing, if you arm yourselves before the LORD for the war, and every armed one of you passes over the Jordan before the LORD until he has dispossessed his enemies from before him, and the land is subdued before the LORD, and afterward you return — you shall be clear before the LORD and before Israel, and this land shall be yours for a possession before the LORD; and if you do not do so, behold, you have sinned against the LORD, and know your sin which will find you; build for yourselves cities for your little ones and folds for your sheep, and that which has gone out of your mouth you shall do', 'moses'),
    ('Num 32:25-27 — and the sons of Gad and the sons of Reuben spoke to Moses, saying: your servants will do as my lord commands; our little ones, our wives, our cattle and all our beasts shall be there in the cities of Gilead; and your servants will pass over, every armed one for war before the LORD, to the war, as my lord says', 'the-sons-of-gad-and-reuben'),
    ('Num 32:28-30 — and Moses commanded concerning them Eleazar the priest, and Joshua son of Nun, and the heads of the fathers of the tribes of the children of Israel; and Moses said to them: if the sons of Gad and the sons of Reuben pass over the Jordan with you, every armed one for war before the LORD, and the land is subdued before you, you shall give them the land of Gilead for a possession; and if they do not pass over armed with you, they shall take possessions among you in the land of Canaan', 'moses'),
    ('Num 32:31-32 — and the sons of Gad and the sons of Reuben answered, saying: that which the LORD has spoken to your servants, so will we do; we will pass over armed before the LORD to the land of Canaan, and the possession of our inheritance with us across the Jordan', 'the-sons-of-gad-and-reuben'),
    ('Num 32:33 — and Moses gave to them — to the sons of Gad and to the sons of Reuben and to half the tribe of Manasseh son of Joseph — the kingdom of Sihon king of the Amorite and the kingdom of Og king of Bashan, the land with its cities in the borders, the cities of the land round about', 'moses'),
    ('Num 32:34-38 — and the sons of Gad built Dibon and Ataroth and Aroer, and Atroth-shophan and Jazer and Jogbehah, and Beth-nimrah and Beth-haran, fortified cities and folds for sheep; and the sons of Reuben built Heshbon and Elealeh and Kiriathaim, and Nebo and Baal-meon (their names being changed) and Sibmah, and they called by names the names of the cities which they built', 'the-sons-of-gad-and-reuben'),
    ('Num 32:39-40 — and the sons of Machir son of Manasseh went to Gilead and took it, and dispossessed the Amorite who was in it; and Moses gave Gilead to Machir son of Manasseh, and he dwelt in it', 'the-sons-of-machir'),
    ('Num 32:41 — and Jair son of Manasseh went and took their villages, and called them Havvoth-jair', 'jair'),
    ('Num 32:42 — and Nobah went and took Kenath and its daughters, and called it Nobah after his own name', 'nobah'),
]
CLOSES = 'one — the build debit (32:24) at 32:34-38; the stipulation (32:20-24) and the commission\'s charge (32:28-30) OPEN BY DESIGN to Joshua 22:1-9'


def scene():
    """THE SCENE — the exam's rows replayed on the world engine (the exodus epoch): the exam's persons through the four case kinds."""
    with contextlib.redirect_stdout(io.StringIO()):
        w = WE.World(era='Num 32:1-42: Mishnah Kiddushin 3:4, Shekalim 3:2 and the sugyot on the engine (the exodus epoch)', epoch='exodus')
        w.laws = [law_gad_reuben]
        w.advance(w.clock.day_in('exodus', 40, 6, 1))
        # ---- the exam's persons through the four case kinds (LITERAL submits — the daemon gate parses no loop) ----
        w.submit({'kind': 'stipulation_case', 'subject': 'the-undoubled-condition', 'person': 'the-undoubled-condition', 'ask': 'doubled_condition', 'case_source': 'Mishnah Kiddushin 3:4 — the exam\'s row doubled_condition'})
        w.submit({'kind': 'stipulation_case', 'subject': 'the-order-limb', 'person': 'the-order-limb', 'ask': 'four_limbs', 'case_source': 'Gittin 75a:11 — the exam\'s row four_limbs'})
        w.submit({'kind': 'stipulation_case', 'subject': 'the-negative-arm', 'person': 'the-negative-arm', 'ask': 'negative_arm_outcome', 'case_source': 'Kiddushin 61b:2 — the exam\'s row negative_arm_outcome'})
        w.submit({'kind': 'stipulation_case', 'subject': 'the-gift-from-now', 'person': 'the-gift-from-now', 'ask': 'from_now', 'case_source': 'Gittin 75b:2 — the exam\'s row from_now'})
        w.submit({'kind': 'stipulation_case', 'subject': 'the-counter-torah', 'person': 'the-counter-torah', 'ask': 'condition_counter_to_torah', 'case_source': 'Bava Metzia 94a:2 — the exam\'s row condition_counter_to_torah'})
        w.submit({'kind': 'stipulation_case', 'subject': 'the-impossible-condition', 'person': 'the-impossible-condition', 'ask': 'impossible_condition', 'case_source': 'Bava Metzia 94a:14 — the exam\'s row impossible_condition'})
        w.submit({'kind': 'stipulation_case', 'subject': 'the-bill-undoubled', 'person': 'the-bill-undoubled', 'ask': 'undoubled_on_a_bill', 'case_source': 'Gittin 75a:10 — the exam\'s row undoubled_on_a_bill'})
        w.submit({'kind': 'stipulation_case', 'subject': 'the-scope', 'person': 'the-scope', 'ask': 'the_scope', 'case_source': 'Shevuot 36a:27 — the exam\'s row the_scope'})
        w.submit({'kind': 'stipulation_case', 'subject': 'the-second-doubling', 'person': 'the-second-doubling', 'cell': 'charge', 'ask': 'second_doubling', 'case_source': 'Num 32:29-30 — the exam\'s row second_doubling'})
        w.submit({'kind': 'clearance_case', 'subject': 'the-clerk', 'person': 'the-clerk', 'ask': 'clerk', 'case_source': 'Mishnah Shekalim 3:2 — the exam\'s row clerk'})
        w.submit({'kind': 'clearance_case', 'subject': 'the-bakers', 'person': 'the-bakers', 'ask': 'bakers', 'case_source': 'Yoma 38a:9 — the exam\'s row bakers'})
        w.submit({'kind': 'clearance_case', 'subject': 'the-perfumers', 'person': 'the-perfumers', 'ask': 'perfumers', 'case_source': 'Yoma 38a:12 — the exam\'s row perfumers'})
        w.submit({'kind': 'clearance_case', 'subject': 'the-collectors', 'person': 'the-collectors', 'ask': 'collectors', 'case_source': 'Pesachim 13a:13-14 — the exam\'s row collectors'})
        w.submit({'kind': 'oath_retold_case', 'subject': 'the-two-of-six-hundred-thousand', 'person': 'the-two-of-six-hundred-thousand', 'ask': 'two_of_six_hundred_thousand', 'case_source': 'Sanhedrin 111a:6 — the exam\'s row two_of_six_hundred_thousand'})
        w.submit({'kind': 'oath_retold_case', 'subject': 'the-exceptions', 'person': 'the-exceptions', 'ask': 'the_exceptions', 'case_source': 'Num 32:12 — the exam\'s row the_exceptions'})
        w.submit({'kind': 'oath_retold_case', 'subject': 'calebs-hebron', 'person': 'calebs-hebron', 'ask': 'calebs_hebron', 'case_source': 'Sotah 34b:7 — the exam\'s row calebs_hebron'})
        w.submit({'kind': 'oath_retold_case', 'subject': 'the-set', 'person': 'the-set', 'ask': 'the_set', 'case_source': 'Num 32:11 — the exam\'s row the_set'})
        w.submit({'kind': 'oath_retold_case', 'subject': 'the-deaths-ceased', 'person': 'the-deaths-ceased', 'ask': 'generation_consumed', 'case_source': 'Bava Batra 121a:9 — the exam\'s row generation_consumed'})
        w.submit({'kind': 'oath_retold_case', 'subject': 'joshua-nothing-owed', 'person': 'joshua-nothing-owed', 'ask': 'joshua_nothing_owed', 'case_source': 'Sotah 35a:4 — the exam\'s row joshua_nothing_owed'})
        w.submit({'kind': 'land_east_case', 'subject': 'the-three-grantees', 'person': 'the-three-grantees', 'ask': 'three_parties', 'case_source': 'Num 32:33 — the exam\'s row three_parties'})
        w.submit({'kind': 'land_east_case', 'subject': 'the-land-held', 'person': 'the-land-held', 'ask': 'land_held', 'case_source': 'Bava Batra 119a:1 — the exam\'s row land_held'})
        w.submit({'kind': 'land_east_case', 'subject': 'the-not-by-lot', 'person': 'the-not-by-lot', 'ask': 'not_by_lot', 'case_source': 'Num 26:55 — the exam\'s row not_by_lot'})
        w.submit({'kind': 'land_east_case', 'subject': 'the-count', 'person': 'the-count', 'ask': 'the_count', 'case_source': 'Josh 4:13 — the exam\'s row the_count'})
        w.submit({'kind': 'land_east_case', 'subject': 'the-survivors', 'person': 'the-survivors', 'cell': 'machir', 'ask': 'survivors', 'case_source': 'Bava Batra 121b:9 — the exam\'s row survivors'})
        w.submit({'kind': 'land_east_case', 'subject': 'the-moses-grave', 'person': 'the-moses-grave', 'cell': 'cities', 'ask': 'moses_grave', 'case_source': 'Sotah 13b:20 — the exam\'s row moses_grave'})
        w.submit({'kind': 'land_east_case', 'subject': 'the-gads-eight', 'person': 'the-gads-eight', 'cell': 'cities', 'ask': 'gads_eight', 'case_source': 'Num 32:34-36 — the exam\'s row gads_eight'})
    n = lambda eid, eff: len([e for e in w.entity(eid).ledger if e['effect'] == eff])
    tset = len([l for l in w.log if l[0] == 'TIMER-SET']); tfire = len([l for l in w.log if l[0] == 'TIMER-FIRE']); tcan = len([l for l in w.log if l[0] == 'TIMER-CANCEL'])
    return ((n('the-undoubled-condition', 'commanded'), n('the-order-limb', 'commanded'), n('the-negative-arm', 'accepted'), n('the-gift-from-now', 'holding_given'), n('the-counter-torah', 'exempt'), n('the-impossible-condition', 'exempt'), n('the-bill-undoubled', 'exempt'), n('the-scope', 'accepted'), n('the-second-doubling', 'commanded'),
             n('the-clerk', 'clear_before_the_lord_and_israel'), n('the-bakers', 'clear_before_the_lord_and_israel'), n('the-perfumers', 'clear_before_the_lord_and_israel'), n('the-collectors', 'clear_before_the_lord_and_israel'),
             n('the-two-of-six-hundred-thousand', 'exempt'), n('the-exceptions', 'exempt'), n('calebs-hebron', 'holding_owed'), n('the-set', 'accepted'), n('the-deaths-ceased', 'accepted'), n('joshua-nothing-owed', 'exempt'),
             n('the-three-grantees', 'holding_given'), n('the-land-held', 'holding_given'), n('the-not-by-lot', 'accepted'), n('the-count', 'accepted'), n('the-survivors', 'accepted'), n('the-moses-grave', 'accepted'), n('the-gads-eight', 'cities_built')),
            (tset, tfire, tcan, len(w.timers)),
            len(w.entities)), w
SCENE, _W = scene()
# THE PREDICTION (typed before the first run, NUMBERS_WALK.md "Sitting 12b"): every exam person written once per effect — twenty-six ones; no timer in the
# chapter (set 0, fired 0, cancelled 0, pending 0). ENTITIES: the exam's 26 persons + the counterparties israel (the holding_given rows) and the-court
# (Caleb's holding_owed) and the-amorite (none in the scene — no land_possessed row asked) = 28.
SCENE_PREDICTED = ((1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1), (0, 0, 0, 0), 26)   # the 28 typed first counted the counterparties israel and the-court: an entity is a written-on party (the narrative's evidence, the same run) — 26
assert SCENE == SCENE_PREDICTED, ('THE NUMBERS WALK: the scene moved from its prediction', SCENE, SCENE_PREDICTED)


def narrative():
    """THE NUMBERS WALK 12b (2026-09-12): the chapter's own acts AS HISTORY — the TWELVE lines of 32:1-42 at the counter's day (40, 6, 1),
    page-order after Midian's thirteen (31:1-54), on a world with this runner's daemon: 13 writes, no timer, no marker, eleven entities, one
    close found on this world (the build debit at 32:34-38). Recorded by the sequential run's recorder and stitched onto the tape. Not a graded
    cell: the tuple below is a tripwire typed from the design; the sequence world's RUN tuple and CG1-CG9 grade the tape."""
    with contextlib.redirect_stdout(io.StringIO()):
        w = WE.World(era='Num 32:1-42: Gad and Reuben on the tape — the request, the oath retold, the condition, the commission, the grant, the cities, Machir, Jair and Nobah (the exodus epoch)', epoch='exodus')
        w.laws = [law_gad_reuben]
        w.advance(w.clock.day_in('exodus', 40, 6, 1))
        # THE DAEMON GATE READS LITERAL SUBMITS ONLY — the twelve lines typed out
        w.submit({'kind': 'land_requested', 'subject': 'the-sons-of-gad-and-reuben', 'to': 'moses', 'cities': NINE, 'request': 'for a possession; do not bring us over the Jordan', 'case_source': LINES[0][0]})
        w.submit({'kind': 'moses_rebuked_the_tribes', 'subject': 'moses', 'to': 'the-sons-of-gad-and-reuben', 'oath': 'he swore (32:10) — chapter 14\'s "as I live"', 'set': TWENTY, 'exceptions': ['caleb', 'joshua'], 'years': FORTY, 'case_source': LINES[1][0]})
        w.submit({'kind': 'tribes_offered_to_arm', 'subject': 'the-sons-of-gad-and-reuben', 'folds': 'for our cattle', 'cities': 'for our little ones', 'arm': 'before the children of Israel', 'until_when': 'every man has inherited', 'case_source': LINES[2][0]})
        w.submit({'kind': 'condition_stipulated', 'subject': 'moses', 'to': 'the-sons-of-gad-and-reuben', 'positive_arm': 'cross armed before the LORD until the land is subdued — clear, and the land yours for a possession', 'negative_arm': 'your sin will find you', 'clearance': 'before the LORD and before Israel', 'utterance_rule': '32:24 = 30:3', 'build': 'cities for your little ones and folds for your sheep', 'case_source': LINES[3][0]})
        w.submit({'kind': 'tribes_accepted_the_condition', 'subject': 'the-sons-of-gad-and-reuben', 'to': 'moses', 'order': 'our little ones, our wives, our cattle', 'case_source': LINES[4][0]})
        w.submit({'kind': 'commission_charged', 'subject': 'moses', 'to': 'the-dividers-of-the-land', 'positive_arm': 'give them the land of Gilead for a possession', 'negative_arm': 'they take possessions among you in Canaan', 'case_source': LINES[5][0]})
        w.submit({'kind': 'tribes_answered_so_will_we_do', 'subject': 'the-sons-of-gad-and-reuben', 'to': 'moses', 'the_lords_word': 'that which the LORD has spoken to your servants', 'case_source': LINES[6][0]})
        w.submit({'kind': 'land_granted_east', 'subject': 'moses', 'to': ['the-sons-of-gad', 'the-sons-of-reuben', 'the-half-tribe-of-manasseh'], 'kingdoms': ['סיחן', 'עוג'], 'count': TWO_AND_A_HALF, 'case_source': LINES[7][0]})
        w.submit({'kind': 'cities_built_east', 'subject': 'the-sons-of-gad-and-reuben', 'gad': GAD_CITIES, 'reuben': REUBEN_CITIES, 'renamed': ['נבו', 'בעל מעון'], 'case_source': LINES[8][0]})
        w.submit({'kind': 'gilead_taken_by_machir', 'subject': 'the-sons-of-machir', 'took': 'Gilead', 'dispossessed': 'the-amorite', 'given': 'by Moses to Machir son of Manasseh', 'case_source': LINES[9][0]})
        w.submit({'kind': 'villages_taken_by_jair', 'subject': 'jair', 'took': 'their villages', 'named': 'Havvoth-jair', 'case_source': LINES[10][0]})
        w.submit({'kind': 'kenath_taken_by_nobah', 'subject': 'nobah', 'took': 'Kenath and its daughters', 'named': 'Nobah', 'case_source': LINES[11][0]})
    writes = len([l for l in w.log if l[0] == 'WRITE'])
    closes = len([e for ent in w.entities.values() for e in ent.ledger if e.get('closed_by')])
    return (writes, len([l for l in w.log if l[0] == 'TIMER-SET']), len(w.entities), w.clock.eras['exodus'].date(w.clock.day)[1:], closes), w


NARRATIVE, _WN = narrative()
NARRATIVE_PREDICTED = (13, 0, 8, (6, 1), 1)   # NUMBERS_WALK.md "Sitting 12b": 13 writes (L1 1, L2 0, L3 0, L4 2, L5 0, L6 1, L7 0, L8 3, L9 2, L10 2, L11 1, L12 1), no timer, EIGHT entities — the WRITTEN-ON parties alone (the compound party, the dividers, the three grantees, the sons of Machir, jair, nobah): the design's eleven had counted moses (a speech subject with no write here) and the counterparties israel and the-amorite — AN ENTITY IS A WRITTEN-ON PARTY, the first run's evidence (retyped); the date (6, 1) of the fortieth year, one close found on this world (the build debit)
assert NARRATIVE == NARRATIVE_PREDICTED, ('THE NUMBERS WALK: Gad and Reuben\'s narrative moved from its prediction', NARRATIVE, NARRATIVE_PREDICTED)


# =====================================================================
# Motion 2 — THE TEST DATA: the answer sheet's rows (the docket's LAW rows).
# =====================================================================
CASES = [
    # F1 — the request
    ('Num 32:1-2 — the parties: the ink\'s compound at six seats', lambda: the_request({'ask': 'the_parties'}, DATA), "the sons of Gad and the sons of Reuben — the ink's compound at six seats (32:2, 6, 25, 29, 31, 33), Gad first; Reuben first at 32:1 alone"),
    ('Num 32:1 / Bekhorot 4b:7 — much cattle', lambda: the_request({'ask': 'much_cattle'}, DATA), "much cattle, very numerous (32:1) — a place for cattle at its one seat; the land of Jazer one seat; Bekhorot 4b:7's premise"),
    ('Num 32:2 / 27:2 — the triad without the halt', lambda: the_request({'ask': 'the_triad'}, DATA), "to Moses, to Eleazar the priest and to the princes of the congregation (32:2) — 27:2's triad without the halt: no case brought before the LORD"),
    ('Num 32:3 / Berakhot 8b:1 — the nine cities', lambda: the_request({'ask': 'the_nine'}, DATA), "nine cities asked (32:3) — Ataroth, Dibon, Jazer, Nimrah, Heshbon, Elealeh, Sebam, Nebo, Beon; Onkelos renders them by Aramaic names (Berakhot 8b:1's premise against the store)"),
    ('Num 32:4-5 — the request', lambda: the_request({'ask': 'the_request'}, DATA), "let this land be given to your servants for a possession; do not bring us over the Jordan (32:5) — the plea's two clauses; 'a possession' Joseph's word (Genesis 47:11)"),
    ('Num 32:16 / 32:24 — the cattle before the children', lambda: the_request({'ask': 'order_of_the_offer'}, DATA), "the cattle before the children (32:16) reversed by Moses (32:24) — the ink's two orders; no row of the declared spine"),
    # F2 — the rebuke and the oath retold
    ('Num 32:6 / Judges 5:16 — shall your brothers go to war', lambda: the_rebuke({'ask': 'brothers_to_war'}, DATA), "shall your brothers go to war and you sit here? (32:6) — one seat; Deborah's question on Reuben (Judges 5:16) observed"),
    ('Num 32:7 / 30:6-12 — the hinder-root', lambda: the_rebuke({'ask': 'hinder_root'}, DATA), "why do you discourage the heart (32:7) — the vows' verb: six Torah tokens all in chapters 30 and 32; 14:34's 'my alienation' the noun"),
    ('Num 32:8 / Sotah 34b:3 — the spies\' verb; when I sent them', lambda: the_rebuke({'ask': 'the_spies_verb'}, DATA), "'to see the land' (32:8) — the spies' verb at each telling: 13:2's 'tour', Deuteronomy 1:22's 'search', 1:24's 'scout'; 'when I sent them' Moses' own first person (Sotah 34b:3's 'send you')"),
    ('Num 32:10 / 14:21, 28 — the oath supplied', lambda: the_rebuke({'ask': 'the_oath_supplied'}, DATA), "'and he swore, saying' (32:10) — chapter 14 says 'as I live' (14:21, 28); Deuteronomy 1:34 supplies the verb too: the oath retold with the verb supplied"),
    ('Num 32:11 / 14:29 by CALL — the set', lambda: the_rebuke({'ask': 'the_set'}, DATA), "from twenty years old and upward (32:11) — the census formula's twenty-three seats; the doomed set 603,550 by CALL (SL.decree set)"),
    ('Num 32:12 / 14:24, 30 by CALL — the exceptions', lambda: the_rebuke({'ask': 'the_exceptions'}, DATA), "save Caleb son of Jephunneh the Kenizzite and Joshua son of Nun (32:12) — SL.decree exceptions by CALL: Caleb and Joshua (14:24, 14:30); 'followed the LORD fully' Caleb's phrase"),
    ('Num 32:12 / Genesis 15:19 — the Kenizzite', lambda: the_rebuke({'ask': 'caleb_the_kenizzite'}, DATA), "the Kenizzite (32:12) — Genesis 15:19's nation as Caleb's gentilic (Joshua 14:6, 14); Othniel son of Kenaz; no docket row — the ink's arm"),
    ('Sotah 34b:7-8; Bava Batra 122a:12 — Caleb\'s Hebron', lambda: the_rebuke({'ask': 'calebs_hebron'}, DATA), "Caleb's Hebron — holding_owed (14:24 'the land where he went'), paid at Joshua 14:13-14 outside the Torah; Sotah 34b:7 the graves; 'another spirit' a change over time (34b:8)"),
    ('Sotah 35a:4; Bava Batra 122a:12 — Joshua, nothing owed', lambda: the_rebuke({'ask': 'joshua_nothing_owed'}, DATA), "Joshua excepted (32:12) and nothing owed him in the ink — Sotah 35a:4 'a severed head, no children'; Timnath-serah by the LORD's word (Joshua 19:50; Bava Batra 122a:12)"),
    ('Num 32:13 / 14:33-34; Deut 2:14 — forty years', lambda: the_rebuke({'ask': 'forty_years'}, DATA), "forty years (32:13) — the parser's [40] = SL.FORTY_YEARS; the timer fired at (40, 5, 9) on the tape; Deuteronomy 2:14's thirty-eight from Kadesh"),
    ('Num 32:13 / Bava Batra 121a:9 — the generation consumed', lambda: the_rebuke({'ask': 'generation_consumed'}, DATA), "until all the generation was consumed (32:13) — Deuteronomy 2:14's phrase; the deaths ceased on the fifteenth of Av (SL.decree deaths_ceased by CALL; Bava Batra 121a:9)"),
    ('Num 32:13 — he made them wander', lambda: the_rebuke({'ask': 'made_them_wander'}, DATA), "he made them wander in the wilderness (32:13) — the causative's one Torah seat"),
    ('Num 32:13 — the Kings\' formula at its first seat', lambda: the_rebuke({'ask': 'evil_formula'}, DATA), "who did evil in the eyes of the LORD (32:13) — the Judges' and Kings' formula, fifty-three seats, at its first seat in the Bible's order"),
    ('Num 32:14 / Genesis 13:13; 25:4 — a brood of sinful men', lambda: the_rebuke({'ask': 'brood'}, DATA), "a brood of sinful men (32:14) — 'brood' a hapax, 'sinners' Sodom's word (Genesis 13:13); 'to add yet to the fierce anger of the LORD' Peor's phrase (25:4)"),
    ('Num 32:15 — the threat, no write', lambda: the_rebuke({'ask': 'the_threat'}, DATA), "'he will yet again leave them in the wilderness and you will destroy all this people' (32:15) — a conditional threat in Moses' mouth: no write"),
    ('Sanhedrin 111a:6; Bava Batra 121b:8, 121b:11 — two of six hundred thousand', lambda: the_rebuke({'ask': 'two_of_six_hundred_thousand'}, DATA), "two of six hundred thousand entered — Caleb and Joshua (Rav Simai, Sanhedrin 111a:6); the decree not on Levi (Bava Batra 121b:8) nor under twenty or over sixty (121b:11)"),
    ('Sanhedrin 111a:12-13 — slow to anger; the pardon', lambda: the_rebuke({'ask': 'slow_to_anger'}, DATA), "'the LORD's anger burned' (32:10, 13) — the pardon of 14:20 preceded it (SL.decree pardon by CALL); slow to anger at the spies' sin (Sanhedrin 111a:12-13)"),
    # F3 — the offer
    ('Num 32:16 — folds and cities', lambda: the_offer({'ask': 'folds_and_cities'}, DATA), "folds for our cattle and cities for our little ones (32:16) — the offer's order; the cattle first"),
    ('Num 32:17 — we will arm ourselves (seven tokens)', lambda: the_offer({'ask': 'we_will_arm'}, DATA), "and we will arm ourselves, hastening, before the children of Israel (32:17) — the arm-root's seven tokens in the chapter"),
    ('Num 32:18 / Deut 3:20; Josh 1:15, 22:4 — we will not return', lambda: the_offer({'ask': 'not_return'}, DATA), "we will not return to our houses until the children of Israel have inherited every man his inheritance (32:18) — one seat; the retellings 'until the LORD gives rest' (Deuteronomy 3:20, Joshua 1:15); the release Joshua 22:4"),
    ('Josh 1:14, 4:12-13 — Joshua\'s armed in the consonants of fifty', lambda: the_offer({'ask': 'joshuas_armed'}, DATA), "Joshua's 'armed' in the consonants of 'fifty' (Joshua 1:14, 4:12 chamushim) — told by the u-vowel and the doubling dot; 4:13's chalutsei the chapter's word"),
    ('Num 32:19 — east of the Jordan', lambda: the_offer({'ask': 'east_of_jordan'}, DATA), "our inheritance has come to us on this side of the Jordan eastward (32:19) — the offer's ground"),
    # F4 — the condition
    ('Num 32:20-22 — the positive arm', lambda: the_condition({'ask': 'positive_arm'}, DATA), "if you arm yourselves before the LORD for the war and every armed one passes over the Jordan until the land is subdued, and afterward you return — clear, and this land yours for a possession (32:20-22): the positive arm; 'before the LORD' seven tokens"),
    ('Num 32:23 / Genesis 44:16 — the negative arm', lambda: the_condition({'ask': 'negative_arm'}, DATA), "and if you do not do so, you have sinned against the LORD, and know your sin which will find you (32:23) — the negative arm; Judah's idiom (Genesis 44:16)"),
    ('Mishnah Kiddushin 3:4 — the doubled condition', lambda: the_condition({'ask': 'doubled_condition'}, DATA), "the doubled condition — R. Meir: every condition not doubled like Gad and Reuben's is none; R. Chanina ben Gamliel: the doubling was needed there for its own sake (Mishnah Kiddushin 3:4)"),
    ('Gittin 75a:11-75b:6; Bava Metzia 94a — the law of all conditions', lambda: the_condition({'ask': 'four_limbs'}, DATA), "the law of all conditions from this chapter (Gittin 75a:11): doubled; the condition before the act (75a:12; Bava Metzia 94a:3); the positive before the negative (Gittin 75b:6); the condition's matter and the act's distinct (75a:14); a condition that can be fulfilled — the ruling as R. Yehuda ben Teima (Bava Metzia 94a:14)"),
    ('Kiddushin 61b:2, 61b:5-8 — the negative arm\'s outcome', lambda: the_condition({'ask': 'negative_arm_outcome'}, DATA), "'they shall take possessions among you in the land of Canaan' (32:30) — Gilead shared or Canaan only; without the doubling no portion anywhere or Gilead anyway (Kiddushin 61b:2, 61b:5-8)"),
    ('Gittin 75b:2 — on condition is from now', lambda: the_condition({'ask': 'from_now'}, DATA), "'on condition' is 'from now' (Rav Huna in Rav's name, Gittin 75b:2) — the grant of 32:33 takes effect at once under the condition; the transfer written at the grant, the debit open beside it"),
    ('Num 32:22 / Shekalim 3:2; Yoma 38a; Pesachim 13a — the clearance', lambda: the_condition({'ask': 'the_clearance'}, DATA), "clear before the LORD and before Israel (32:22) — one seat; a person must appear justified before people as before the Omnipresent (Mishnah Shekalim 3:2; Yoma 38a:9, 38a:12; Pesachim 13a:13-14); 1 Chronicles 22:18 the double in Chronicles' ink"),
    ('Mishnah Shekalim 3:2 — the clerk', lambda: the_condition({'ask': 'clerk'}, DATA), "Mishnah Shekalim 3:2 — clear before the LORD and before Israel (32:22): the one who collects from the treasury chamber enters with no cuffed garment, shoe, sandal, phylacteries or amulet — lest he become poor or rich and be suspected"),
    ('Yoma 38a:9 — the bakers', lambda: the_condition({'ask': 'bakers'}, DATA), "Yoma 38a:9 — clear before the LORD and before Israel (32:22): the House of Garmu's descendants never held refined bread — so that people would not say they are sustained from the showbread's technique"),
    ('Yoma 38a:12 — the perfumers', lambda: the_condition({'ask': 'perfumers'}, DATA), "Yoma 38a:12 — clear before the LORD and before Israel (32:22): the House of Avtinas's brides never perfumed; a wife from elsewhere STIPULATED not to — a condition on a marriage at the rule's own seat"),
    ('Pesachim 13a:13-14 — the collectors', lambda: the_condition({'ask': 'collectors'}, DATA), "Pesachim 13a:13-14 — clear before the LORD and before Israel (32:22): the charity collectors sell to others and change money with others, not with their own coins"),
    ('Num 32:24 / 30:3 by CALL — the utterance rule\'s second seat', lambda: the_condition({'ask': 'utterance_rule'}, DATA), "that which has gone out of your mouth you shall do (32:24) — 30:3's 'all that goes out of his mouth he shall do', the phrase's two seats; the vows' cell by CALL: the vow's fulfilment — a positive duty, a prohibition, and the court's compulsion"),
    ('Num 32:24 / 30:3; Judges 11:36 — the lemma pair', lambda: the_condition({'ask': 'the_lemma_pair'}, DATA), "'goes out' + 'mouth' adjacent at nine seats — Numbers 30:3 and 32:24 the Torah's two, Judges 11:36 Jephthah's daughter among the seven outside"),
    ('Num 32:24 — the build command', lambda: the_condition({'ask': 'the_build_command'}, DATA), "build for yourselves cities for your little ones and folds for your sheep (32:24) — Moses' order reversed: the children first; the run at 32:34-38 closes it"),
    ('Num 32:21-22 / Sotah 3a:8-9 — the verb of the future', lambda: the_condition({'ask': 'the_verb_future'}, DATA), "'and every armed one of you will pass over' (32:21) read of the future — 'the land subdued... and you return afterward' fixes it (Sotah 3a:8-9)"),
    ('Mishnah Bava Metzia 94a:2 — a condition counter to the Torah', lambda: the_condition({'ask': 'condition_counter_to_torah'}, DATA), "a condition counter to the Torah on a non-monetary matter is void; in monetary matters the parties may agree (Mishnah Bava Metzia 94a:2)"),
    ('Bava Metzia 94a:11-14 — an impossible condition', lambda: the_condition({'ask': 'impossible_condition'}, DATA), "a condition that cannot be fulfilled — the act stands and the condition is void, the ruling as R. Yehuda ben Teima (Bava Metzia 94a:11-14); the Rabbis: binding"),
    ('Gittin 75a:10, 75a:13 — an undoubled condition on a bill', lambda: the_condition({'ask': 'undoubled_on_a_bill'}, DATA), "an undoubled condition on a bill of divorce — no condition according to R. Meir, the act stands (Gittin 75a:10); the action preceding the condition the same (75a:13)"),
    ('Shevuot 36a:27, 36a:29 — the rule\'s scope', lambda: the_condition({'ask': 'the_scope'}, DATA), "R. Meir refuses the inference in monetary matters only (Shevuot 36a:27) — or everywhere (36a:29; the sotah's spelling): the rule's scope, both readings"),
    ('Onkelos 32:20-32 — before the people of the LORD', lambda: the_condition({'ask': 'onkelos_buffer'}, DATA), "'before the people of the LORD' at the six martial seats of Onkelos Numbers, all this chapter's (32:20, 21, 22, 27, 29, 32); the three legal seats kept — the reading's claim MT32A-06"),
    # F5 — the acceptance and the charge
    ('Num 32:25, 27 — my lord', lambda: the_acceptance_and_the_charge({'ask': 'servants_will_do'}, DATA), "your servants will do as my lord commands (32:25) — 'my lord' for Moses at 32:25, 27 (Joshua's 11:28, Aaron's 12:11, the Gileadite heads' 36:2)"),
    ('Num 32:26 / Deut 3:19; Josh 1:14 — the order held', lambda: the_acceptance_and_the_charge({'ask': 'the_order_reversed'}, DATA), "our little ones, our wives, our cattle and all our beasts (32:26) — Moses' order held; the retellings 'your wives, your little ones, your cattle' (Deuteronomy 3:19, Joshua 1:14)"),
    ('Num 32:28 / Josh 14:1, 21:1; Bava Batra 122a:4 — the commission', lambda: the_acceptance_and_the_charge({'ask': 'the_commission'}, DATA), "Eleazar the priest, Joshua son of Nun and the heads of the fathers of the tribes (32:28) — Joshua 14:1's dividers word for word, 21:1 the third form; Bava Batra 122a:4's lottery"),
    ('Num 32:29-30 — the second doubling', lambda: the_acceptance_and_the_charge({'ask': 'second_doubling'}, DATA), "if they pass over — give them Gilead; if not — they take possessions among you in Canaan (32:29-30): the second doubling, the exam's proof verses; the commission's debit open to Joshua 22"),
    ('Num 32:31 / Josh 22:9 — the LORD\'s word', lambda: the_acceptance_and_the_charge({'ask': 'the_lords_word'}, DATA), "that which the LORD has spoken to your servants, so will we do (32:31) — Moses' stipulation called the LORD's word; Joshua 22:9 'by the commandment of the LORD by the hand of Moses': a law in Moses' voice with no divine frame"),
    ('Num 32:32 / 27:7 — we, the possession of our inheritance', lambda: the_acceptance_and_the_charge({'ask': 'we_short'}, DATA), "'we' in its short form (32:32) — three Bible seats (Genesis 42:11, Lamentations 3:42); 'the possession of our inheritance' the daughters' construct (27:7)"),
    # F6 — the grant
    ('Num 32:33 — the three parties', lambda: the_grant({'ask': 'three_parties'}, DATA), "to the sons of Gad, to the sons of Reuben and to half the tribe of Manasseh (32:33) — three transfers; half Manasseh first named at the grant"),
    ('Num 32:33 / 21:24-35 by CALL — the two kingdoms', lambda: the_grant({'ask': 'two_kingdoms'}, DATA), "the kingdom of Sihon king of the Amorite (one seat) and the kingdom of Og king of Bashan (Deuteronomy 3's and this) — the chukat runner's land possessed at 21:24-35 by CALL: the grant's source"),
    ('Deut 3:18-20; Josh 1:12-15; Bava Batra 118b:8 — half Manasseh\'s stipulation', lambda: the_grant({'ask': 'half_manassehs_stipulation'}, DATA), "no stipulation spoken to half Manasseh in the chapter; Deuteronomy 3:18-20, Joshua 1:12-15, 4:12 extend the crossing to the three; Joshua 17:5-6 'beside the land of Gilead and Bashan' (Bava Batra 118b:8)"),
    ('Num 26:7, 18, 34 by CALL; Josh 4:13; 1 Chr 5:18 — the two and a half\'s count', lambda: the_grant({'ask': 'the_count'}, DATA), "the two and a half's count — 43,730 + 40,500 + 52,700 ÷ 2 = 110,580 from the second census by CALL; Joshua 4:13's about forty thousand; 1 Chronicles 5:18's 44,760"),
    ('Bava Batra 119a:1, 119a:5 by CALL — the land held', lambda: the_grant({'ask': 'land_held'}, DATA), "in possession before assignment — the rows are holdings before the lot (C2 by CALL; Bava Batra 119a:1, 119a:5): the standing 'a possession' carries"),
    ('Num 26:55 by CALL — not by lot', lambda: the_grant({'ask': 'not_by_lot'}, DATA), "the east by Moses' word, not by lot — 26:55's lot is Canaan's (C2 by CALL: the place by lot, Joshua 14-19 the run); the OPEN divide_the_land not this chapter's run"),
    ('Bava Batra 119b:3-4 by CALL — bequeath and not inherit', lambda: the_grant({'ask': 'bequeath_not_inherit'}, DATA), "the exodus generation bequeath and do not inherit (Bava Batra 119b:3-4; C2 morasha by CALL) — the doomed set's title to the land"),
    # F7 — the cities
    ('Num 32:34-36 — Gad\'s eight', lambda: the_cities({'ask': 'gads_eight'}, DATA), "Dibon, Ataroth, Aroer, Atroth-shophan, Jazer, Jogbehah, Beth-nimrah, Beth-haran — Gad's eight (32:34-36), fortified cities and folds for sheep"),
    ('Num 32:37-38 — Reuben\'s six', lambda: the_cities({'ask': 'reubens_six'}, DATA), "Heshbon, Elealeh, Kiriathaim, Nebo, Baal-meon and Sibmah — Reuben's six (32:37-38); 'their names being changed' one seat"),
    ('Num 32:3 / 32:34-38 — the nine split four and five', lambda: the_cities({'ask': 'the_split'}, DATA), "the nine asked split four and five — Gad's Ataroth, Dibon, Jazer, Nimrah (as Beth-nimrah); Reuben's Heshbon, Elealeh, Sebam (as Sibmah), Nebo, Beon (as Baal-meon)"),
    ('Num 33:45-46 — Dibon Gad', lambda: the_cities({'ask': 'dibon_gad'}, DATA), "Dibon Gad (33:45-46) — the itinerary's own witness to the city's tribe, the next chapter's"),
    ('Josh 13:17, 13:26, 13:20 — the two crossed cities', lambda: the_cities({'ask': 'two_crossed'}, DATA), "Dibon and Heshbon in Reuben's list at Joshua 13:17, Heshbon on Gad's border at 13:26 — the two crossed between the tribes; Beth-peor Reuben's (13:20)"),
    ('Sotah 13b:20; Onkelos 32:3 — Moses\' grave', lambda: the_cities({'ask': 'moses_grave'}, DATA), "Nebo Reuben's (32:37-38) — Moses died in Reuben's portion (Sotah 13b:20); Onkelos 'Nebo, the burial place of Moses' at 32:3; the Sifrei 106:1's Gad the other arm"),
    ('Num 32:34-38 / 32:24 — the build debit closed', lambda: the_cities({'ask': 'the_build_closed'}, DATA), "the cities built (32:34-38) — the run of 32:24's 'build for yourselves cities': the build debit closed by value, the chapter's one Torah-closed debit"),
    # F8 — Machir, Jair and Nobah
    ('Num 32:39 / Genesis 50:23; 21:32 — the sons of Machir', lambda: machir_jair_nobah({'ask': 'sons_of_machir'}, DATA), "the sons of Machir son of Manasseh (32:39) — Genesis 50:23's collective, born on Joseph's knees; Gilead taken, the Amorite dispossessed (21:32's verb)"),
    ('Num 32:40 / 26:29; Josh 17:1 — Gilead given to Machir', lambda: machir_jair_nobah({'ask': 'gilead_given'}, DATA), "Moses gave Gilead to Machir son of Manasseh (32:40) — the clan under the ancestor's name (26:29; Joshua 17:1 the man of war; Deuteronomy 3:15)"),
    ('Num 32:41 — Jair and Havvoth-jair', lambda: machir_jair_nobah({'ask': 'jair'}, DATA), "Jair son of Manasseh took their villages and called them Havvoth-jair (32:41) — six seats; 'went and took' at 32:41-42 alone"),
    ('Num 32:41 / 1 Chr 2:21-22; Judges 10:4 — Jair\'s two lineages', lambda: machir_jair_nobah({'ask': 'jairs_lineage'}, DATA), "Jair son of Manasseh (32:41; Deuteronomy 3:14; 1 Kings 4:13) against 1 Chronicles 2:21-22's Hezron's grandson by Machir's daughter, twenty-three cities — the ink's two accounts; the judge Jair's thirty (Judges 10:4)"),
    ('Bava Batra 121b:9-11 — Jair and Machir the survivors', lambda: machir_jair_nobah({'ask': 'survivors'}, DATA), "Jair and Machir born in Jacob's days and did not die until the entry — 'about thirty-six' at Ai read as Jair alone (Bava Batra 121b:9-10); already old at the decree (121b:11)"),
    ('Num 32:42 / Judges 8:11; 1 Chr 2:23 — Nobah', lambda: machir_jair_nobah({'ask': 'nobah'}, DATA), "Nobah took Kenath and its daughters and called it Nobah after his own name (32:42) — Nobah and Jogbehah together at Judges 8:11 on Gideon's route; Kenath's other seat 1 Chronicles 2:23"),
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
    print('THE INK: integers %s; ordinals none; starred none; marked none; the frame verbs %s (no divine frame)' % (sorted(INTS.items()), FRAME_VERBS))
    print('THE ARITHMETIC: the two and a half %d = %d + %d + %d / 2; Joshua 4:13\'s %d; 1 Chronicles 5:18\'s %d; the arm-root %d tokens; "before the LORD" %d tokens' % (TWO_AND_A_HALF, C2.C26['reuben'], C2.C26['gad'], C2.C26['manasseh'], FORTY_THOUSAND, CHRONICLES_COUNT, len(ARM_TOKENS), len(BEFORE_THE_LORD_32)))
    print('THE SCENE on the bench: %s; the timers (set, fired, cancelled, pending) %s; entities %d' % SCENE)
    print('THE NARRATIVE: %s' % (NARRATIVE,))
    print('THE PARAMETER ROWS: ' + '; '.join('%s = %s' % (k, DATA[k]['value']) for k in DATA) + ' (the other settings recorded in DATA)')
    if ok == len(CASES):
        print('\nTHE COMPILE OF GAD AND REUBEN: the answer sheet REPRODUCED — %d/%d' % (ok, len(CASES)))
    sys.exit(0 if ok == len(CASES) else 1)
