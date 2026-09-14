# ===== F3: MOSES' RESTATEMENT (Num 34:13-15) — the relay; the nine and a half a run citation; no write ==========
def moses_restatement(case, data):
    del P[:]
    ask = case['ask']
    if ask == 'the_relay':
        ink('34:13', '"and Moses commanded the children of Israel, saying" — %s: the phrase\'s TWO Torah seats; 36:5\'s is the installing act command_relayed (THE TENT sitting 4)' % RELAY)
        dat('the row the_relay_form: %s — law_borders installed_by BOOT with the class named; whether a relay in this form installs is the second pass\'s D2 question' % data['the_relay_form']['value'])
        return out("and Moses commanded the children of Israel (34:13) — the relay of 34:1-12 in the form 36:5's installing act took: the D2 question of the second pass, the class named", ['accepted'])
    if ask == 'the_nine_and_a_half':
        ink('34:13, 15', 'the parser [%d] at 34:13 and [%d] at 34:15 (the construct "two of", the caret) with the two halves = %d; "to the nine tribes and the half tribe" %s (Joshua 14:2 the other seat); "nine" in the construct %s — every one the nine tribes; "the two tribes and the half tribe" %s' % (NINE, TWO, NINE + TWO + 1, NINE_HALF, NINE_CONSTRUCT, TWO_HALF))
        dat('the row the_nine_and_a_half: %s' % data['the_nine_and_a_half']['value'])
        return out("the nine tribes and the half tribe, the two tribes and the half tribe (34:13, 34:15) — [9] and [2] with the two halves = twelve; 'nine' in the construct three Bible seats, all the nine tribes", ['accepted'])
    if ask == 'one_tribe_noun':
        ink('34:13-28', 'the staff-word %d times in the chapter, the other tribe-word NEVER; 32:33 gave "the half tribe of Manasseh" with the other word (the neighbour); Joshua 13:7 says the nine with the other word %s' % (len(MATTEH), NINE_HALF_OTHER))
        return out("one tribe-noun — the staff-word eighteen times in the chapter and the other never; 32:33's the neighbour; Joshua 13:7 says the nine with the other word", ['accepted'])
    if ask == 'the_grant_read':
        ink('34:14-15', '"the two tribes and the half tribe HAVE TAKEN THEIR INHERITANCE beyond the Jordan at Jericho" — "took their inheritance" %s (always the two and a half); "beyond the Jordan at Jericho" %s' % (TOOK, BEYOND))
        move('cold_run_gad_reuben (CALL) — GR.the_grant(three_parties) = %s' % GR_THREE[0][:90], "32:33's three transfers on the tape (holding_given on the sons of Gad, the sons of Reuben, the half tribe of Manasseh) — A RUN CITATION: the line writes nothing (CW4 reads the ledger)")
        move('cold_run_gad_reuben (CALL) — GR.the_grant(not_by_lot) = %s' % GR_NOTLOT[0][:70], "the east by Moses' word, not by the lot of 26:55")
        return out("the two and a half have taken their inheritance (34:14-15) — a run citation of 32:33's three transfers on the tape; the line writes nothing", ['accepted'])
    if ask == 'the_count':
        move('cold_run_gad_reuben (CALL) — GR.the_grant(the_count) = %s' % GR_COUNT[0][:80], "43,730 + 40,500 + 52,700 ÷ 2 = 110,580 from the second census")
        ink('34:14', '43730 + 40500 + 52700 // 2 = %d' % COUNT_TWO_HALF)
        dat('the row the_nine_and_a_half: count_two_and_a_half = %d' % data['the_nine_and_a_half']['value']['count_two_and_a_half'])
        return out("the two and a half's count — 110,580 by CALL (43,730 + 40,500 + 52,700 ÷ 2 from the second census)", ['accepted'])
    if ask == 'the_pair':
        ink('34:14', '"the tribe of the sons of the Reubenite … the tribe of the sons of the Gadite" — the gentilics %s / %s: THE PAIR\'S FIRST SEAT; the Gadite\'s token also "the kid" (Genesis 38:23, Judges 14:6) — a homograph by token' % (REUBENITE, GADITE))
        return out("the Reubenite and the Gadite (34:14) — the pair's first seat; the Gadite's token is also 'the kid' at Genesis 38:23 and Judges 14:6", ['accepted'])
    if ask == 'joshuas_receipt':
        ink('34:13 / Joshua 14:2', 'Joshua 14:2 %s quotes 34:13\'s %s under "as the LORD commanded by the hand of Moses" %s (Joshua 21:8 the form\'s other seat); NO receipt in the chapter — "as the LORD commanded Moses" in Numbers %d seats, none in 34' % (words(14, 2, 'Josh')[-4:], words(34, 13)[16:20], RECEIPT_HAND, len(RECEIPT_NUM)))
        return out("Joshua 14:2's receipt — 'as the LORD commanded by the hand of Moses, to the nine tribes and the half tribe' quotes 34:13 outside the Torah; no receipt in the chapter", ['accepted'])
    if ask == 'the_lot_by_call':
        ink('34:13', '"this is the land which you shall INHERIT BY LOT" — "by lot" in the Torah %s; the reflexive stem %s (Ezekiel 47:13 the same)' % (BY_LOT_T, INHERIT_HIT))
        move('cold_run_second_census (CALL) — C2.the_land(by_lot) = %s; C2.DATA[division_by] = %s' % (C2_LOT[0], C2.DATA['division_by']['value']), "the OPEN divide_the_land debit (26:52-56) CITED, not rewritten — VIA second_census as at 32:18 and 33:54")
        move('cold_run_journeys (CALL) — JO.the_command(the_lot_restated) = %s' % JO_LOT[0][:80], "33:54's restatement the same way")
        return out("you shall inherit by lot (34:13) — 26:52-56's lot by CALL, the open debit cited a third time (32:18, 33:54, here), not rewritten", ['accepted'])
    return out('no verdict in span', [FX.NONE])


# ===== F4: THE DIVIDERS (Num 34:16-18) — the standing party named; the doubling; the court that owes ===========
def the_dividers(case, data):
    del P[:]
    ask = case['ask']
    if ask == 'the_names_form':
        ink('34:17, 19', '"these are the names of the men" — %s: the spies\' roster (13:16) and this; 34:19 with the conjunction %s' % (NAMES_MEN, words(34, 19)[:3]))
        return out("these are the names of the men (34:17, 34:19) — the rosters' heading, 13:16's and this", ['dividers_named'])
    if ask == 'the_triad':
        ink('34:17', '"Eleazar the priest and Joshua son of Nun" as one phrase — %s: this and Joshua\'s two runs (14:1, 19:51)' % TRIAD)
        move('cold_run_gad_reuben (CALL) — GR.the_acceptance_and_the_charge(the_commission) = %s' % GR_COMM[0][:90], "32:28's charge to the same triad — the dividers of the land written on already (the Gilead charge OPEN)")
        move('Bava Batra 122a:4-6 (credited)', "the lottery's picture — Eleazar with the Urim, Joshua and all Israel before him, two receptacles: THE DIVIDERS AT WORK")
        return out("Eleazar the priest and Joshua son of Nun (34:17) — the triad's three Bible seats: this and Joshua 14:1, 19:51; 32:28's charge by CALL; the lottery's picture on the shelf", ['dividers_named'])
    if ask == 'the_three_stems':
        ink('34:13, 17-18, 29', 'the one root in three stems — the reflexive 34:13 (%s), the plain 34:17-18 (%s; "to divide the land" %s), the INTENSIVE 34:29 (its other three seats Joshua\'s runs %s, %s); one skin "to divide" / "to the brook" %s — the points decide; THE OBJECT SWITCHES: the land at 34:17 %s, the people at 34:29 %s' % (INHERIT_HIT, INHERIT_QAL, TO_DIVIDE_LAND, PIEL_MOSES, PIEL_RUNS, TO_DIVIDE, words(34, 17)[4:8], words(34, 29)[4:8]))
        return out("the one root in three stems — the reflexive (34:13), the plain (34:17-18), the intensive (34:29) whose other three seats are Joshua's runs; the object switching from the land to the people", ['accepted'])
    if ask == 'the_distributive':
        ink('34:18', '"one prince, one prince from a tribe" %s — the parser [%d, %d]; the pair\'s bare form %s; "one man, one man" %s; the kin by the same parser %s' % (DOUBLING, ONE_ONE[0], ONE_ONE[1], ONE_PRINCE_PAIR, ONE_MAN_PAIR, {('%s %d:%d' % k): v for k, v in KIN.items()}))
        move('cold_run_shelach (CALL) — SL.spies(one_per_tribe) = %s' % SL_ONE[0], "13:2's doubling")
        move('cold_run_naso (CALL) — NS.dedication(per_day) = %s' % NS_PER_DAY[0][:60], "7:11's doubling")
        move('cold_run_korach (CALL) — KR.plague_and_staffs(staffs_count) = %s' % KR_STAFFS[0][:70], "17:21's doubling with the twelve")
        dat('the row the_distributive_doubling: %s' % data['the_distributive_doubling']['value'])
        return out("one prince, one prince from a tribe (34:18) — the distributive doubling read [1, 1]: the spies, the dedication and the rods by CALL; Joshua's stones and embassy the runs", ['dividers_named'])
    if ask == 'the_court_that_owes':
        move('cold_run_zelophehad (CALL) — ZL.the_daughters(the_run) = %s' % ZL_RUN[0][:80], "the daughters' holding owed at 27:7 paid at Joshua 17:4 'before Eleazar the priest and before Joshua' — the dividers the court that owes it (the zelophehad runner's token table reads 34:17 so)")
        move('cold_run_shelach (CALL) — SL.decree(caleb_entitlement) = %s' % SL_CALEB[0][:70], "Caleb's Hebron paid at Joshua 14:13 before the same court")
        ink('34:17', 'Caleb\'s holding_owed OPEN on the tape since 14:24 and the daughters\' since 27:4 — both paid before the dividers outside the Torah (CW7)')
        return out("the court that owes — the daughters' holding (paid at Joshua 17:4 before Eleazar and Joshua) and Caleb's Hebron (Joshua 14:13): the dividers the payers, by CALL", ['accepted'])
    if ask == 'only_excludes':
        move('cold_run_second_census (CALL) — C2.the_land(only_excludes) = %s' % C2_ONLY[0], "'only by lot' excludes Joshua and Caleb — not by the lot they administer (Bava Batra 122a:12)")
        return out("'only' excludes Joshua and Caleb (Bava Batra 122a:12) — the two dividers' own portions not by the lot they administer: by CALL", ['exempt'])
    if ask == 'the_princes_as_agents':
        move('Kiddushin 42a:6', "Rav Giddel: the law of agency from 34:18 — refused, since minors have no agency and the princes divided for them")
        move('Kiddushin 42a:8', "Rava bar Rav Huna: the court appoints a steward for orphans who come to divide, to their disadvantage and to their benefit — from 34:18")
        dat('the row the_princes_as_agents: %s' % data['the_princes_as_agents']['value'])
        return out("the princes as agents or stewards (Kiddushin 42a:6-8 on 34:18) — agency asked and refused, the court's steward for orphans the verse's teaching: a data row", ['accepted'])
    if ask == 'the_seventy_one':
        move('Sanhedrin 16a:2', "Ulla: the first division by seventy-one elders — a tribes' border dispute before the Great Sanhedrin")
        move('Sanhedrin 16a:3', "refused: the first division needed the lots, the Urim and all Israel")
        dat('the row the_seventy_one: %s' % data['the_seventy_one']['value'])
        return out("the seventy-one at the first division (Sanhedrin 16a:2-3) — Ulla's likeness refused: the lots, the Urim and all Israel; the ink's dividers twelve by name: a data row", ['accepted'])
    if ask == 'the_debit':
        ink('34:29', '"these are they whom the LORD commanded to divide to the children of Israel in the land of Canaan" — the closer %s; the debit on the dividers OPEN BY DESIGN to Joshua 14:1 and 19:51' % CLOSER)
        return out("the dividers commanded (34:29) — a debit to divide the inheritance to the children of Israel in Canaan, OPEN BY DESIGN to Joshua 14:1 and 19:51", ['commanded'])
    return out('no verdict in span', [FX.NONE])


# ===== F5: THE ROSTER (Num 34:19-29) — the twelve as rows; the order matching none ==========================
def the_roster(case, data):
    del P[:]
    ask = case['ask']
    if ask == 'the_roster':
        ink('34:19-28', 'the ten by tribe — %s; the fathers %s; the title at %s; "the children of" absent at %s; the conjunction absent at %s' % ([r['tribe'] for r in ROSTER], [r['father'] for r in ROSTER], [r['tribe'] for r in ROSTER if r['title']], [r['tribe'] for r in ROSTER if not r['sons_of']], [r['tribe'] for r in ROSTER if not r['conjunction']]))
        dat('the row the_roster: the twelve — Eleazar, Joshua and the ten; the population table\'s named rows (as_of Num 34:17-29)')
        return out("the roster (34:19-28) — ten princes by tribe with their fathers; the title at seven rows, dropped at Judah's, Simeon's and Benjamin's; the twelve enter the population table", ['dividers_named'])
    if ask == 'calebs_five_words':
        ink('34:19 / 13:6', '34:19\'s five %s = 13:6\'s %s — the spy\'s line at the dividers\'; "Caleb son of Jephunneh" %s' % (words(34, 19)[3:8], words(13, 6), CALEB_JEPH))
        move('cold_run_shelach (CALL) — SL.spies(joshua_caleb_equal) = %s' % SL_EQUAL[0], "Caleb first at 13:6")
        return out("Caleb's five words (34:19 = 13:6) — the spy's line repeated at the dividers'; Caleb son of Jephunneh eight Torah seats", ['accepted'])
    if ask == 'the_survivors':
        move('cold_run_shelach (CALL) — SL.decree(exceptions) = %s; SL.decree(spies_portions) = %s' % (SL_EXC[0], SL_PORTIONS[0][:60]), "the two survivors of the spies' roster")
        ink('34:17, 19', 'Joshua son of Nun (34:17; 13:8 "Hoshea son of Nun") and Caleb — the ONLY persons of chapter 13\'s roster here; the spies\' tribes %s' % SL.SPY_TRIBES)
        return out("the two survivors — Joshua and Caleb the only persons of the spies' roster among the dividers; the exceptions of 14:24, 14:30 by CALL", ['accepted'])
    if ask == 'no_prince_of_chapter_one':
        move('cold_run_naso (CALL) — NS.NAMES = %s' % NS.NAMES, "the twelve princes of 1:5-15 (the dedication's twelve)")
        move('cold_run_bamidbar (CALL) — CB.census(orders) = %s' % CB_ORDERS[0], "the roll's orders")
        ink('34:19-28', 'NONE of the twelve among the ten; one father\'s name shared — Ammihud %s (Ephraim\'s Elishama 1:10; Simeon\'s Shemuel; Naphtali\'s Pedahel)' % FATHER_SEATS['עמיהוד'])
        return out("no prince of chapter 1 among the ten (by CALL); Ammihud the one father's name shared — three tribes' fathers' name (1:10; 34:20; 34:28)", ['accepted'])
    if ask == 'only_here':
        ink('34:19-28', 'nowhere else BY TOKEN %s (eight — Hanniel among them, his namesake at 1 Chronicles 7:39 spelled otherwise); BY LEMMA %s (ten — Ephod the vestment\'s consonants at Exodus 28:15, 39:8; Chislon Joshua 15:10\'s Chesalon; Shelomi "my peace-offerings"; Hanniel out); Shemuel %d verses by lemma, this the first; Kemuel %s; Elizaphan %s; Paltiel %s; Bukki %s' % (ONLY_HERE_TOKEN, ONLY_HERE_LEMMA, len(PRINCE_SEATS['שמואל']), PRINCE_SEATS['קמואל'], PRINCE_SEATS['אליצפן'], PRINCE_SEATS['פלטיאל'], PRINCE_SEATS['בקי']))
        dat('the reading\'s "eight names only here" was a MIXED measure — filed at the compile (the ledger\'s CORRECTIONS block)')
        return out("the names nowhere else — eight by token (Hanniel among them), ten by lemma (Ephod, Chislon, Shelomi homographs by token; Hanniel's lemma shared); Shemuel the prophet's name's first seat; seven of the ten carry God's name, none of the fathers", ['accepted'])
    if ask == 'the_order':
        ink('34:19-28', 'the order %s against sixteen lists — matching %s; Manasseh before Ephraim in %s; Zebulun before Issachar in %s; the four northern in Joshua\'s lot order %s' % (ROSTER_ORDER, MATCHES or 'none', MAN_BEFORE_EPH, ZEB_BEFORE_ISS, LOTS_19))
        dat('the row the_roster_order: matching none — the cause unnamed, the declared shelf silent')
        return out("the order matches no other roster (sixteen lists) — Manasseh before Ephraim as the second census and Genesis 46 in the Torah, Zebulun before Issachar as the two blessings, the four northern in Joshua's lot order", ['accepted'])
    if ask == 'the_closer':
        ink('34:29', '"these are they whom the LORD commanded" %s — the closer without a noun, one seat; no receipt "as the LORD commanded Moses" in the chapter (Numbers\' %d seats); the receipt Joshua 14:2\'s' % (CLOSER, len(RECEIPT_NUM)))
        return out("the closer (34:29) — 'these are they whom the LORD commanded to divide', one seat; no receipt in the chapter — Joshua 14:2's is outside the Torah", ['commanded'])
    if ask == 'the_rows':
        ink('34:17-28', 'TWELVE NAMED ROWS — Eleazar (levi, "the priest"), Joshua (ephraim by 13:8, "son of Nun"), and the ten by tribe with their fathers and the title\'s clause; as_of Num 34:17-29 — the register gate\'s Num 34 seat PAID')
        dat('the population table\'s named grain (8b): the persons the roll names enter the table — the first register reached since the table was built')
        return out("the twelve named rows — the roll's persons enter the population table (grain named, as of Num 34:17-29): the register gate's seat paid", ['dividers_named'])
    return out('no verdict in span', [FX.NONE])


# ---- THE WRAP — the daemon, the scene, the narrative ------------------------------------------------------
PRINCE_TOKENS = {'כלב': 'caleb', 'שמואל': 'shemuel-ben-ammihud', 'אלידד': 'elidad-ben-chislon', 'בקי': 'bukki-ben-jogli', 'חניאל': 'hanniel-ben-ephod', 'קמואל': 'kemuel-ben-shiphtan', 'אליצפן': 'elizaphan-ben-parnach', 'פלטיאל': 'paltiel-ben-azzan', 'אחיהוד': 'ahihud-ben-shelomi', 'פדהאל': 'pedahel-ben-ammihud'}   # the rows' subjects — the registry's id where one exists (caleb; eleazar and joshua through the map), the naso runner's name-ben-father form for the rest
NAMED_ROWS = [('eleazar', 'אלעזר', 'levi', None, 'the priest (34:17)', 17), ('joshua', 'יהושע', JOSHUA_TRIBE, 'נון', 'son of Nun (34:17; the tribe by 13:8)', 17)] + \
             [(PRINCE_TOKENS[r['prince']], r['prince'], r['tribe'], r['father'], ('prince (34:%d)' % r['verse']) if r['title'] else ('named without the title (34:%d)' % r['verse']), r['verse']) for r in ROSTER]
assert len(NAMED_ROWS) == 12 and NAMED_ROWS[2][0] == 'caleb' and NAMED_ROWS[1][2] == 'ephraim', NAMED_ROWS[:3]

def law_borders(event, world):
    """Num 34:1-29 (cold_run_borders.py F1-F5). given_at Num 34:1; installed_by boot — A LAW IN THE DIVINE VOICE relayed at 34:13 in 36:5's
    form (the class named in the registry, the second pass decides). THREE TAPE LINES: the borders commanded (34:1-12) — ONE status on the
    land of Canaan valued the four sides; Moses' restatement (34:13-15) — NO write (the grant read, the lot cited); the dividers named
    (34:16-29) — a status and a debit on the dividers of the land (the party 32:28 charged) and TWELVE named rows in the population table.
    The exam's two case kinds dispatch to the cells with LITERAL effects per kind (2b's form — an unnamed effect is a KeyError)."""
    k, src = event['kind'], event['case_source']
    E_ = lambda eff, s, cp=None, amount=None, due=None, law='', value=None: {'effect': eff, 'subject': s, 'counterparty': cp, 'amount': amount, 'due': due, 'value': value if value is not None else True, 'source_law': law, 'case_source': src}
    day = event.get('day', world.clock.day)      # THE SEQUENTIAL RUN: the event's own day
    # ---- the three lines (page_order at the counter's day, no marker in the chapter) ----
    if k == 'borders_commanded':
        return [E_('borders_declared', 'the-land-of-canaan', value=SIDES_EN, law='F2 [INK 34:2 "this is the land that shall fall to you as an inheritance, the land of Canaan BY ITS BORDERS" … 34:12 "this shall be your land by its borders round about" — ONE STATUS ON THE LAND: the four sides in the ink\'s order with their named points (the DATA row the_four_sides, twenty-seven proper-name tokens; Joshua 15:1-4 Judah\'s run of the south; Ezekiel 47 the kin in another order; the second Mount Hor the chukat runner\'s row); nothing on the people — the lot\'s debit of 26:52-56 OPEN, cited (CW3); the shelf: the sea within the border or the islands by the string (Gittin 8a:4-7), one border round about (Bekhorot 55a:10), the Jordan Canaan\'s (55a:14)]')]
    if k == 'moses_commanded_the_nine_and_a_half':
        return []                                                                                        # THE EMPTY WATCH: the relay writes nothing — the grant's three transfers and the lot's open debit are read at the checkpoints (CW3, CW4); Joshua 14:2's receipt outside the Torah
    if k == 'dividers_named':
        for subj, person, tribe, father, status, v in NAMED_ROWS:
            world.row('population', {'grain': 'named', 'as_of': 'Num 34:17-29', 'subject': subj, 'person': person, 'tribe': tribe, 'father': father, 'status': status, 'source': src, 'note': 'Num 34:%d' % v})   # the father column always present (None for Eleazar — 34:17 names no father; the second census runner's rows carry the column the same way): the tape's first run read a KeyError on the view                                                                # THE ROLL'S PERSONS ENTER THE TABLE (8b's law) — the register gate's Num 34 seat PAID
        return [E_('dividers_named', 'the-dividers-of-the-land', value='Eleazar the priest, Joshua son of Nun, and one prince from a tribe — Judah Caleb son of Jephunneh, Simeon Shemuel son of Ammihud, Benjamin Elidad son of Chislon, Dan Bukki son of Jogli, Manasseh Hanniel son of Ephod, Ephraim Kemuel son of Shiphtan, Zebulun Elizaphan son of Parnach, Issachar Paltiel son of Azzan, Asher Ahihud son of Shelomi, Naphtali Pedahel son of Ammihud (34:17-28)', law='F4 [INK 34:17 "these are the names of the men who shall divide the land for you: Eleazar the priest and Joshua son of Nun" — the party 32:28 charged as a body (its Gilead charge OPEN beside this write) gets its roster; 34:18 "one prince, one prince from a tribe" the distributive doubling; the triad\'s three Bible seats (34:17; Joshua 14:1, 19:51); the twelve rows in the population table (grain named, as_of Num 34:17-29)]'),
                E_('commanded', 'the-dividers-of-the-land', value='divide_the_inheritance_to_the_children_of_israel_in_canaan', law='F4 [INK 34:29 "these are they whom the LORD commanded to divide to the children of Israel in the land of Canaan" — the DEBIT on the dividers OPEN BY DESIGN: its runs Joshua 14:1 ("which Eleazar the priest and Joshua son of Nun … divided"), 17:14 (Joseph\'s claim answered), 19:51 (the lot before the LORD at Shiloh) — outside the Torah, THE READBACK\'s; the intensive stem\'s other three seats those runs; "only" excludes the two dividers\' own portions (Bava Batra 122a:12)]')]
    # ---- the exam's case kinds: each names LITERALLY every effect it can write (2b's form) ----
    if k == 'borders_case':
        fn = {'heading': the_land_and_its_fall}.get(event.get('cell'), the_four_sides)
        v, e, _ = fn(dict(event, ask=event['ask']), DATA); L = '%s [%s]' % ({'heading': 'F1'}.get(event.get('cell'), 'F2'), v); s_ = event['person']
        W = {'borders_declared': E_('borders_declared', s_, value=v, law=L), 'accepted': E_('accepted', s_, value=v, law=L), 'exempt': E_('exempt', s_, value=v, law=L)}
        return [W[x] for x in e if x != FX.NONE]
    if k == 'dividers_case':
        fn = {'restatement': moses_restatement, 'dividers': the_dividers}.get(event.get('cell'), the_roster)
        v, e, _ = fn(dict(event, ask=event['ask']), DATA); L = '%s [%s]' % ({'restatement': 'F3', 'dividers': 'F4'}.get(event.get('cell'), 'F5'), v); s_ = event['person']
        W = {'commanded': E_('commanded', s_, value=v, law=L), 'dividers_named': E_('dividers_named', s_, value=v, law=L), 'accepted': E_('accepted', s_, value=v, law=L), 'exempt': E_('exempt', s_, value=v, law=L)}
        return [W[x] for x in e if x != FX.NONE]
    return []


LINES = [
    ('Num 34:1-12 — and the LORD spoke to Moses, saying: command the children of Israel and say to them: when you are coming into the land Canaan, this is the land that shall fall to you as an inheritance, the land of Canaan by its borders; and your south side shall be from the wilderness of Zin on the hands of Edom, and your south border shall be from the end of the Salt Sea eastward; and the border shall turn for you south of the ascent of Akrabbim and pass to Zin, and its goings-out shall be south of Kadesh-barnea, and it shall go out to Hazar-addar and pass to Azmon; and the border shall turn from Azmon to the brook of Egypt, and its goings-out shall be at the sea; and the west border: you shall have the great sea and its border, this shall be your west border; and this shall be your north border: from the great sea you shall mark out for yourselves Mount Hor; from Mount Hor you shall mark out to Lebo-hamath, and the goings-out of the border shall be to Zedad; and the border shall go out to Ziphron, and its goings-out shall be Hazar-enan, this shall be your north border; and you shall mark out for yourselves the east border from Hazar-enan to Shepham; and the border shall go down from Shepham to Riblah east of Ain, and the border shall go down and reach the shoulder of the sea of Chinnereth eastward; and the border shall go down to the Jordan, and its goings-out shall be the Salt Sea; this shall be your land by its borders round about', 'israel'),
    ('Num 34:13-15 — and Moses commanded the children of Israel, saying: this is the land which you shall inherit by lot, which the LORD commanded to give to the nine tribes and the half tribe; for the tribe of the sons of the Reubenite by their fathers\' house and the tribe of the sons of the Gadite by their fathers\' house and the half tribe of Manasseh have taken their inheritance; the two tribes and the half tribe have taken their inheritance beyond the Jordan at Jericho, eastward toward the sunrise', 'moses'),
    ('Num 34:16-29 — and the LORD spoke to Moses, saying: these are the names of the men who shall divide the land for you: Eleazar the priest and Joshua son of Nun; and one prince, one prince from a tribe you shall take to divide the land; and these are the names of the men: for the tribe of Judah, Caleb son of Jephunneh; and for the tribe of the sons of Simeon, Shemuel son of Ammihud; for the tribe of Benjamin, Elidad son of Chislon; and for the tribe of the sons of Dan a prince, Bukki son of Jogli; for the sons of Joseph: for the tribe of the sons of Manasseh a prince, Hanniel son of Ephod; and for the tribe of the sons of Ephraim a prince, Kemuel son of Shiphtan; and for the tribe of the sons of Zebulun a prince, Elizaphan son of Parnach; and for the tribe of the sons of Issachar a prince, Paltiel son of Azzan; and for the tribe of the sons of Asher a prince, Ahihud son of Shelomi; and for the tribe of the sons of Naphtali a prince, Pedahel son of Ammihud; these are they whom the LORD commanded to divide to the children of Israel in the land of Canaan', 'israel'),
]
CLOSES = 'none — Caleb\'s holding_owed (14:24) and the daughters\' (27:4) are paid before the dividers OUTSIDE THE TORAH (Joshua 14:13, 17:4); the lot\'s debit (26:52-56) stays open, cited; the dividers\' Gilead charge (32:28-30) stays open beside the new debit'


def scene():
    """THE SCENE — the exam's rows replayed on the world engine (the exodus epoch): the exam's persons through the two case kinds."""
    with contextlib.redirect_stdout(io.StringIO()):
        w = WE.World(era='Num 34:1-29: the borders on the shelf — Gittin, Bekhorot, Kiddushin, Sanhedrin, Bava Batra, Sheviit on the engine (the exodus epoch)', epoch='exodus')
        w.laws = [law_borders]
        w.advance(w.clock.day_in('exodus', 40, 6, 1))
        # ---- the exam's persons through the two case kinds (LITERAL submits — the daemon gate parses no loop) ----
        w.submit({'kind': 'borders_case', 'subject': 'the-title-claim', 'person': 'the-title-claim', 'cell': 'heading', 'ask': 'the_land_canaan', 'case_source': 'Sanhedrin 91a:6 — the exam\'s row the_land_canaan'})
        w.submit({'kind': 'borders_case', 'subject': 'the-land-bound-rule', 'person': 'the-land-bound-rule', 'cell': 'heading', 'ask': 'the_land_bound_rule', 'case_source': 'Mishnah Kiddushin 1:9 (36b:8) — the exam\'s row the_land_bound_rule'})
        w.submit({'kind': 'borders_case', 'subject': 'the-one-border', 'person': 'the-one-border', 'cell': 'heading', 'ask': 'by_its_borders', 'case_source': 'Bekhorot 55a:10 — the exam\'s row by_its_borders'})
        w.submit({'kind': 'borders_case', 'subject': 'the-sea-within', 'person': 'the-sea-within', 'cell': 'sides', 'ask': 'the_sea_as_border', 'case_source': 'Gittin 8a:5 — the exam\'s row the_sea_as_border'})
        w.submit({'kind': 'borders_case', 'subject': 'the-islands', 'person': 'the-islands', 'cell': 'sides', 'ask': 'the_west', 'case_source': 'Gittin 8a:4-7 — the exam\'s row the_west'})
        w.submit({'kind': 'borders_case', 'subject': 'the-jordan-canaans', 'person': 'the-jordan-canaans', 'cell': 'sides', 'ask': 'the_jordan_as_border', 'case_source': 'Bekhorot 55a:14 — the exam\'s row the_jordan_as_border'})
        w.submit({'kind': 'borders_case', 'subject': 'the-three-lands', 'person': 'the-three-lands', 'cell': 'sides', 'ask': 'the_three_lands', 'case_source': 'Mishnah Sheviit 6:1; Gittin 1:2 — the exam\'s row the_three_lands'})
        w.submit({'kind': 'borders_case', 'subject': 'the-ginnosar', 'person': 'the-ginnosar', 'cell': 'sides', 'ask': 'chinnereth', 'case_source': 'Bava Batra 122a:6 — the exam\'s row chinnereth'})
        w.submit({'kind': 'dividers_case', 'subject': 'the-nine-and-a-half', 'person': 'the-nine-and-a-half', 'cell': 'restatement', 'ask': 'the_grant_read', 'case_source': 'Bekhorot 55a:14 — the exam\'s row the_grant_read'})
        w.submit({'kind': 'dividers_case', 'subject': 'the-relay', 'person': 'the-relay', 'cell': 'restatement', 'ask': 'the_relay', 'case_source': 'Num 36:5 (command_relayed) — the exam\'s row the_relay'})
        w.submit({'kind': 'dividers_case', 'subject': 'the-agent', 'person': 'the-agent', 'cell': 'dividers', 'ask': 'the_princes_as_agents', 'case_source': 'Kiddushin 42a:6 — the exam\'s row the_princes_as_agents'})
        w.submit({'kind': 'dividers_case', 'subject': 'the-lottery', 'person': 'the-lottery', 'cell': 'dividers', 'ask': 'the_triad', 'case_source': 'Bava Batra 122a:4 — the exam\'s row the_triad'})
        w.submit({'kind': 'dividers_case', 'subject': 'the-only-excludes', 'person': 'the-only-excludes', 'cell': 'dividers', 'ask': 'only_excludes', 'case_source': 'Bava Batra 122a:12 — the exam\'s row only_excludes'})
        w.submit({'kind': 'dividers_case', 'subject': 'the-seventy-one', 'person': 'the-seventy-one', 'cell': 'dividers', 'ask': 'the_seventy_one', 'case_source': 'Sanhedrin 16a:2 — the exam\'s row the_seventy_one'})
        w.submit({'kind': 'dividers_case', 'subject': 'the-court-that-owes', 'person': 'the-court-that-owes', 'cell': 'dividers', 'ask': 'the_court_that_owes', 'case_source': 'Bava Batra 118b:8 — the exam\'s row the_court_that_owes'})
        w.submit({'kind': 'dividers_case', 'subject': 'the-debit', 'person': 'the-debit', 'cell': 'dividers', 'ask': 'the_debit', 'case_source': 'Num 34:29 — the exam\'s row the_debit'})
        w.submit({'kind': 'dividers_case', 'subject': 'the-survivors', 'person': 'the-survivors', 'cell': 'roster', 'ask': 'the_survivors', 'case_source': 'Bava Batra 117b:2 — the exam\'s row the_survivors'})
        w.submit({'kind': 'dividers_case', 'subject': 'the-order', 'person': 'the-order', 'cell': 'roster', 'ask': 'the_order', 'case_source': 'Num 34:19-28 — the exam\'s row the_order'})
    n = lambda eid, eff: len([e for e in w.entity(eid).ledger if e['effect'] == eff])
    tset = len([l for l in w.log if l[0] == 'TIMER-SET']); tfire = len([l for l in w.log if l[0] == 'TIMER-FIRE']); tcan = len([l for l in w.log if l[0] == 'TIMER-CANCEL'])
    return ((n('the-title-claim', 'accepted'), n('the-land-bound-rule', 'accepted'), n('the-one-border', 'borders_declared'), n('the-sea-within', 'accepted'), n('the-islands', 'borders_declared'), n('the-jordan-canaans', 'accepted'), n('the-three-lands', 'accepted'), n('the-ginnosar', 'accepted'),
             n('the-nine-and-a-half', 'accepted'), n('the-relay', 'accepted'), n('the-agent', 'accepted'), n('the-lottery', 'dividers_named'), n('the-only-excludes', 'exempt'), n('the-seventy-one', 'accepted'), n('the-court-that-owes', 'accepted'), n('the-debit', 'commanded'), n('the-survivors', 'accepted'), n('the-order', 'accepted')),
            (tset, tfire, tcan, len(w.timers)),
            len(w.entities)), w
SCENE, _W = scene()
# THE PREDICTION (typed before the first run, NUMBERS_WALK.md "Sitting 14b"): every exam person written once — eighteen ones; no timer in the
# chapter (set 0, fired 0, cancelled 0, pending 0). ENTITIES: the exam's 18 persons alone (an entity is a written-on party; no counterparty written on).
SCENE_PREDICTED = ((1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1), (0, 0, 0, 0), 18)
assert SCENE == SCENE_PREDICTED, ('THE NUMBERS WALK: the scene moved from its prediction', SCENE, SCENE_PREDICTED)


def narrative():
    """THE NUMBERS WALK 14b (2026-09-13): the chapter's own acts AS HISTORY — the THREE lines of 34:1-29 at the counter's day (40, 6, 1),
    page-order after the journeys' three (33:1-56), on a world with this runner's daemon: 3 writes, no timer, no marker, two entities
    (the land of Canaan and the dividers of the land — moses and israel subjects with no write), no close, TWELVE population rows.
    Recorded by the sequential run's recorder and stitched onto the tape. Not a graded cell: the tuple below is a tripwire typed from the
    design; the sequence world's RUN tuple and CW1-CW9 grade the tape."""
    with contextlib.redirect_stdout(io.StringIO()):
        w = WE.World(era='Num 34:1-29: the borders on the tape — the four sides on the land, the relay, the dividers named (the exodus epoch)', epoch='exodus')
        w.laws = [law_borders]
        w.advance(w.clock.day_in('exodus', 40, 6, 1))
        # THE DAEMON GATE READS LITERAL SUBMITS ONLY — the three lines typed out
        w.submit({'kind': 'borders_commanded', 'subject': 'israel', 'sides': ['south', 'west', 'north', 'east'], 'points': 27, 'first': 'the wilderness of Zin', 'last': 'the Salt Sea', 'by_its_borders': True, 'case_source': LINES[0][0]})
        w.submit({'kind': 'moses_commanded_the_nine_and_a_half', 'subject': 'moses', 'to': 'israel', 'nine': 9, 'two': 2, 'halves': 2, 'by_lot': True, 'case_source': LINES[1][0]})
        w.submit({'kind': 'dividers_named', 'subject': 'israel', 'dividers': ['eleazar', 'joshua', 'caleb', 'shemuel-ben-ammihud', 'elidad-ben-chislon', 'bukki-ben-jogli', 'hanniel-ben-ephod', 'kemuel-ben-shiphtan', 'elizaphan-ben-parnach', 'paltiel-ben-azzan', 'ahihud-ben-shelomi', 'pedahel-ben-ammihud'], 'per_tribe': 1, 'case_source': LINES[2][0]})
    writes = len([l for l in w.log if l[0] == 'WRITE'])
    closes = len([e for ent in w.entities.values() for e in ent.ledger if e.get('closed_by')])
    rows = len([l for l in w.log if l[0] == 'ROW'])
    return (writes, len([l for l in w.log if l[0] == 'TIMER-SET']), len(w.entities), w.clock.eras['exodus'].date(w.clock.day)[1:], closes, rows, len(w.tables['population'])), w


NARRATIVE, _WN = narrative()
NARRATIVE_PREDICTED = (3, 0, 2, (6, 1), 0, 12, 12)   # NUMBERS_WALK.md "Sitting 14b": 3 writes (L1 1, L2 0, L3 2), no timer, TWO entities (the land of Canaan, the dividers of the land — the written-on parties; moses and israel subjects with no write), the counter's day (6, 1), no close, TWELVE rows = twelve ROW lines
assert NARRATIVE == NARRATIVE_PREDICTED, ('THE NUMBERS WALK: the borders\' narrative moved from its prediction', NARRATIVE, NARRATIVE_PREDICTED)
assert all(r['written_by'] == 'law_borders' and r['grain'] == 'named' and r['as_of'] == 'Num 34:17-29' for r in _WN.tables['population']) and [r['subject'] for r in _WN.tables['population']][:3] == ['eleazar', 'joshua', 'caleb'], _WN.tables['population'][:3]


# =====================================================================
# Motion 2 — THE TEST DATA: the answer sheet's rows (the docket's LAW rows).
# =====================================================================
CASES = [
    # F1 — the land and its fall
    ('Num 34:2 / Sifrei 1:2 — the command', lambda: the_land_and_its_fall({'ask': 'the_command'}, DATA), "command the children of Israel (34:2) — five Torah seats, the Sifrei's five; the one command without expense (Sifrei 1:2)"),
    ('Num 34:2 / 33:51 by CALL — when you come', lambda: the_land_and_its_fall({'ask': 'when_you_come'}, DATA), "when you are coming into the land Canaan (34:2) — the article on the land, none on the name; 33:51's entry clause by CALL"),
    ('Num 34:2 / Sanhedrin 91a:6 — the title claim', lambda: the_land_and_its_fall({'ask': 'the_land_canaan'}, DATA), "the land of Canaan (34:2) read as a title claim (Sanhedrin 91a:6) — the tape's answer canaan's status since Genesis 9:25"),
    ('Num 34:2, 13 / Deut 34:4 — this is the land', lambda: the_land_and_its_fall({'ask': 'this_is_the_land'}, DATA), "this is the land — 34:2 and 34:13, Deuteronomy 34:4 from Nebo, Joshua 13:2, Ezekiel 48:29"),
    ('Num 34:2 / 26:52-56 by CALL — shall fall', lambda: the_land_and_its_fall({'ask': 'shall_fall'}, DATA), "that shall fall to you as an inheritance (34:2) — the lot's verb at its one Torah seat with the inheritance; Onkelos 'be divided'; the lot's debit by CALL, cited"),
    ('Num 34:2 — as an inheritance', lambda: the_land_and_its_fall({'ask': 'as_an_inheritance'}, DATA), "as an inheritance (34:2) — three Torah seats: 26:53, 34:2, 36:2, all the land's"),
    ('Num 34:2, 12 / Josh 18:20, 19:49; Bekhorot 55a:10 — by its borders', lambda: the_land_and_its_fall({'ask': 'by_its_borders'}, DATA), "by its borders (34:2, 34:12) — the inclusio; Joshua 18:20 and 19:49 the closers; the border-word sixteen times: ONE STATUS ON THE LAND"),
    ('Num 34:1, 16 / 35:1 — the frames', lambda: the_land_and_its_fall({'ask': 'the_frame'}, DATA), "and the LORD spoke to Moses, saying (34:1, 34:16) — two divine frames with Moses' command between them; 35:1 adds the plains of Moab"),
    ('Mishnah Kiddushin 1:9; 37a:3-6 — the land-bound rule', lambda: the_land_and_its_fall({'ask': 'the_land_bound_rule'}, DATA), "the borders' legal reach — an obligation of the land inside the border, of the body everywhere (Mishnah Kiddushin 1:9; 37a:3-6): a data row, the classing Deuteronomy's"),
    # F2 — the four sides
    ('Num 34:3-5 — the south side', lambda: the_four_sides({'ask': 'the_south'}, DATA), "the south side (34:3-5) — from the wilderness of Zin on the hands of Edom to the brook of Egypt and the sea; eleven proper-name tokens; Joshua 15:1-4 Judah's run of it"),
    ('Num 34:6 / Gittin 8a:4-7 — the west border', lambda: the_four_sides({'ask': 'the_west'}, DATA), "the west border (34:6) — the great sea and its border: one word read two ways on the shelf (the sea itself, or the islands by the string — Gittin 8a:4-7)"),
    ('Num 34:7-9 — the north side', lambda: the_four_sides({'ask': 'the_north'}, DATA), "the north side (34:7-9) — from the great sea by Mount Hor and Lebo-hamath to Zedad, Ziphron and Hazar-enan; the border's own verb three Bible seats all here"),
    ('Num 34:10-12 — the east side', lambda: the_four_sides({'ask': 'the_east'}, DATA), "the east side (34:10-12) — from Hazar-enan by Shepham, Riblah east of Ain, the shoulder of the sea of Chinnereth and the Jordan to the Salt Sea: the loop closes"),
    ('Num 34:3, 12 / Bekhorot 55a:10 — the loop', lambda: the_four_sides({'ask': 'the_loop'}, DATA), "the loop (34:3, 34:12) — the Salt Sea at both ends, 'by its borders round about' the inclusio: all the land one border (Bekhorot 55a:10)"),
    ('Num 34:3-12 — the points (the data row)', lambda: the_four_sides({'ask': 'the_points'}, DATA), "the points (34:3-12) — twenty-seven proper-name tokens: south eleven, west none (the great sea alone), north eight, east eight; the data row the status's value"),
    ('Num 34:3-5 / Josh 15:1-4 — Judah\'s border', lambda: the_four_sides({'ask': 'judahs_border'}, DATA), "Judah's south border is the land's (Joshua 15:1-4) — twenty-nine of the forty-three tokens of 34:3-5 stand there; Hazar-addar split in two; Azmon plene; one 'to you' kept in the run"),
    ('Num 34:4, 5, 8, 9, 12 — the goings-out', lambda: the_four_sides({'ask': 'the_goings_out'}, DATA), "its goings-out — the outlet-word's five Torah seats all in this chapter (34:4, 5, 8, 9, 12); Joshua's borders say it again and again"),
    ('Num 34:4 / Josh 15:4 — the written singular', lambda: the_four_sides({'ask': 'the_written_singular'}, DATA), "the written singular read plural (34:4) — the chapter's one written-and-read pair; the DB writes the written form unpointed; Joshua 15:4 the same clause"),
    ('Num 34:7, 8, 10 / Prov 23:3 — the marking verb', lambda: the_four_sides({'ask': 'the_marking_verb'}, DATA), "you shall mark out (34:7, 8, 10) — the border's own verb, three Bible seats all here; Proverbs' 'desire' the homograph by the points"),
    ('Num 34:7-8 / 20:22 by CALL — the second Mount Hor', lambda: the_four_sides({'ask': 'the_second_mount_hor'}, DATA), "the second Mount Hor (34:7-8) — the name's twelve Torah seats, ten Aaron's and two the north border's; the chukat runner's row by CALL; Onkelos spells the two differently"),
    ('Num 34:6-7 — the great sea plene and defective', lambda: the_four_sides({'ask': 'the_great_sea'}, DATA), "the great sea plene at 34:6 and defective at 34:7 — the defective phrase's one seat"),
    ('Num 34:3-12 — the sea as the west', lambda: the_four_sides({'ask': 'the_sea_as_west'}, DATA), "the sea as the west — one token seven times in the sides (the west, the great sea, the Salt Sea, Chinnereth); Onkelos splits it"),
    ('Num 34:3 / Exod 27:9, 13 — the side-word', lambda: the_four_sides({'ask': 'the_side_word'}, DATA), "the side-word is the tabernacle's (34:3) — the court's south side Exodus 27:9 and its east side 27:13 carry it with the prefix; the bare token's five Torah seats include Leviticus's field-corner and beard-corner, homographs by sense; 'eastward toward the sunrise' (34:15) the court's east side"),
    ('Num 34:11 / 5:23 by CALL — the blotting verb', lambda: the_four_sides({'ask': 'the_blotting_verb'}, DATA), "and it shall reach (34:11) — the blotting verb's token (5:23; Deuteronomy 29:19; Isaiah 25:8): the border reaches, the priest blots — a homograph by sense, the sotah's cell by CALL"),
    ('Num 34:11 / Josh 13:27, 19:35; Bava Batra 122a:6 — Chinnereth', lambda: the_four_sides({'ask': 'chinnereth'}, DATA), "the sea of Chinnereth (34:11) — two seats of the phrase, seven of the name; Onkelos 'Gennesar' — the shelf's lottery names Naphtali's boundary by that word (Bava Batra 122a:6)"),
    ('Num 34:3, 8 / 13:21 by CALL — the spies walked it', lambda: the_four_sides({'ask': 'the_spies_walked_it'}, DATA), "the spies walked the border's length — 'from the wilderness of Zin' and 'Lebo-hamath' each at two seats: 13:21 and 34:3, 34:8"),
    ('Ezek 47:13-20 — the order', lambda: the_four_sides({'ask': 'ezekiels_order'}, DATA), "Ezekiel's order — north, east, south, west against the chapter's south, west, north, east; twenty-nine tokens shared; observed, no link"),
    ('Gen 15:18; Exod 23:31; Deut 1:7, 11:24; Josh 1:4 — the promised extents', lambda: the_four_sides({'ask': 'the_promised_extents'}, DATA), "the four promised extents (Genesis 15:18, Exodus 23:31, Deuteronomy 1:7, 11:24; Joshua 1:4) — no river, Euphrates, Lebanon or western sea in the chapter: another description, observed"),
    ('Gittin 8a:4-7 — the sea as a border', lambda: the_four_sides({'ask': 'the_sea_as_border'}, DATA), "the sea as a border, two ways (Gittin 8a:4-7 on 34:6) — the Rabbis' string over the islands between the ink's two corners, or Rabbi Yehuda's sea itself: a data row"),
    ('Bekhorot 55a:10, 14 — the Jordan as a border', lambda: the_four_sides({'ask': 'the_jordan_as_border'}, DATA), "the Jordan as a border, two ways (Bekhorot 55a:10 on 34:12; 55a:14 on 34:15) — one border round about, or the river Canaan's from 'at Jericho': a data row"),
    ('Mishnah Sheviit 6:1; Gittin 1:2 — the three lands', lambda: the_four_sides({'ask': 'the_three_lands'}, DATA), "the shelf's own border points — the three lands of Sheviit 6:1 inside 34's one border; the bills' Rekem the translation's Kadesh-barnea of 34:4 (Mishnah Gittin 1:2): a data row"),
    # F3 — Moses' restatement
    ('Num 34:13 / 36:5 — the relay', lambda: moses_restatement({'ask': 'the_relay'}, DATA), "and Moses commanded the children of Israel (34:13) — the relay of 34:1-12 in the form 36:5's installing act took: the D2 question of the second pass, the class named"),
    ('Num 34:13, 15 / Josh 13:7, 14:2 — the nine and a half', lambda: moses_restatement({'ask': 'the_nine_and_a_half'}, DATA), "the nine tribes and the half tribe, the two tribes and the half tribe (34:13, 34:15) — [9] and [2] with the two halves = twelve; 'nine' in the construct three Bible seats, all the nine tribes"),
    ('Num 34:13-28 / 32:33 — one tribe-noun', lambda: moses_restatement({'ask': 'one_tribe_noun'}, DATA), "one tribe-noun — the staff-word eighteen times in the chapter and the other never; 32:33's the neighbour; Joshua 13:7 says the nine with the other word"),
    ('Num 34:14-15 / 32:33 by CALL — the grant read', lambda: moses_restatement({'ask': 'the_grant_read'}, DATA), "the two and a half have taken their inheritance (34:14-15) — a run citation of 32:33's three transfers on the tape; the line writes nothing"),
    ('Num 26 by CALL — the count', lambda: moses_restatement({'ask': 'the_count'}, DATA), "the two and a half's count — 110,580 by CALL (43,730 + 40,500 + 52,700 ÷ 2 from the second census)"),
    ('Num 34:14 / Gen 38:23 — the pair', lambda: moses_restatement({'ask': 'the_pair'}, DATA), "the Reubenite and the Gadite (34:14) — the pair's first seat; the Gadite's token is also 'the kid' at Genesis 38:23 and Judges 14:6"),
    ('Num 34:13 / Josh 14:2, 21:8 — Joshua\'s receipt', lambda: moses_restatement({'ask': 'joshuas_receipt'}, DATA), "Joshua 14:2's receipt — 'as the LORD commanded by the hand of Moses, to the nine tribes and the half tribe' quotes 34:13 outside the Torah; no receipt in the chapter"),
    ('Num 34:13 / 26:52-56, 33:54 by CALL — the lot', lambda: moses_restatement({'ask': 'the_lot_by_call'}, DATA), "you shall inherit by lot (34:13) — 26:52-56's lot by CALL, the open debit cited a third time (32:18, 33:54, here), not rewritten"),
    # F4 — the dividers
    ('Num 34:17, 19 / 13:16 — the names form', lambda: the_dividers({'ask': 'the_names_form'}, DATA), "these are the names of the men (34:17, 34:19) — the rosters' heading, 13:16's and this"),
    ('Num 34:17 / 32:28 by CALL; Josh 14:1, 19:51 — the triad', lambda: the_dividers({'ask': 'the_triad'}, DATA), "Eleazar the priest and Joshua son of Nun (34:17) — the triad's three Bible seats: this and Joshua 14:1, 19:51; 32:28's charge by CALL; the lottery's picture on the shelf"),
    ('Num 34:13, 17-18, 29 / Josh 13:32 — the three stems', lambda: the_dividers({'ask': 'the_three_stems'}, DATA), "the one root in three stems — the reflexive (34:13), the plain (34:17-18), the intensive (34:29) whose other three seats are Joshua's runs; the object switching from the land to the people"),
    ('Num 34:18 / 13:2, 7:11, 17:21 by CALL — the distributive', lambda: the_dividers({'ask': 'the_distributive'}, DATA), "one prince, one prince from a tribe (34:18) — the distributive doubling read [1, 1]: the spies, the dedication and the rods by CALL; Joshua's stones and embassy the runs"),
    ('Josh 17:4, 14:13 by CALL — the court that owes', lambda: the_dividers({'ask': 'the_court_that_owes'}, DATA), "the court that owes — the daughters' holding (paid at Joshua 17:4 before Eleazar and Joshua) and Caleb's Hebron (Joshua 14:13): the dividers the payers, by CALL"),
    ('Bava Batra 122a:12 by CALL — only excludes', lambda: the_dividers({'ask': 'only_excludes'}, DATA), "'only' excludes Joshua and Caleb (Bava Batra 122a:12) — the two dividers' own portions not by the lot they administer: by CALL"),
    ('Kiddushin 42a:6-8 — the princes as agents', lambda: the_dividers({'ask': 'the_princes_as_agents'}, DATA), "the princes as agents or stewards (Kiddushin 42a:6-8 on 34:18) — agency asked and refused, the court's steward for orphans the verse's teaching: a data row"),
    ('Sanhedrin 16a:2-3 — the seventy-one', lambda: the_dividers({'ask': 'the_seventy_one'}, DATA), "the seventy-one at the first division (Sanhedrin 16a:2-3) — Ulla's likeness refused: the lots, the Urim and all Israel; the ink's dividers twelve by name: a data row"),
    ('Num 34:29 / Josh 14:1, 19:51 — the debit', lambda: the_dividers({'ask': 'the_debit'}, DATA), "the dividers commanded (34:29) — a debit to divide the inheritance to the children of Israel in Canaan, OPEN BY DESIGN to Joshua 14:1 and 19:51"),
    # F5 — the roster
    ('Num 34:19-28 — the roster', lambda: the_roster({'ask': 'the_roster'}, DATA), "the roster (34:19-28) — ten princes by tribe with their fathers; the title at seven rows, dropped at Judah's, Simeon's and Benjamin's; the twelve enter the population table"),
    ('Num 34:19 / 13:6 by CALL — Caleb\'s five words', lambda: the_roster({'ask': 'calebs_five_words'}, DATA), "Caleb's five words (34:19 = 13:6) — the spy's line repeated at the dividers'; Caleb son of Jephunneh eight Torah seats"),
    ('Num 14:24, 30 by CALL — the survivors', lambda: the_roster({'ask': 'the_survivors'}, DATA), "the two survivors — Joshua and Caleb the only persons of the spies' roster among the dividers; the exceptions of 14:24, 14:30 by CALL"),
    ('Num 1:5-15 by CALL — no prince of chapter 1', lambda: the_roster({'ask': 'no_prince_of_chapter_one'}, DATA), "no prince of chapter 1 among the ten (by CALL); Ammihud the one father's name shared — three tribes' fathers' name (1:10; 34:20; 34:28)"),
    ('Num 34:19-28 — the names nowhere else', lambda: the_roster({'ask': 'only_here'}, DATA), "the names nowhere else — eight by token (Hanniel among them), ten by lemma (Ephod, Chislon, Shelomi homographs by token; Hanniel's lemma shared); Shemuel the prophet's name's first seat; seven of the ten carry God's name, none of the fathers"),
    ('Num 34:19-28 against sixteen lists — the order', lambda: the_roster({'ask': 'the_order'}, DATA), "the order matches no other roster (sixteen lists) — Manasseh before Ephraim as the second census and Genesis 46 in the Torah, Zebulun before Issachar as the two blessings, the four northern in Joshua's lot order"),
    ('Num 34:29 — the closer', lambda: the_roster({'ask': 'the_closer'}, DATA), "the closer (34:29) — 'these are they whom the LORD commanded to divide', one seat; no receipt in the chapter — Joshua 14:2's is outside the Torah"),
    ('Num 34:17-28 — the twelve rows', lambda: the_roster({'ask': 'the_rows'}, DATA), "the twelve named rows — the roll's persons enter the population table (grain named, as of Num 34:17-29): the register gate's seat paid"),
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
    print('THE INK: integers %s; the caret %s; starred none; the frame verbs %s (two divine frames, Moses\' command between)' % (sorted(INTS.items()), CARET, FRAME_VERBS))
    print('THE SIDES: %d proper-name tokens (%s); the border-word %d in the chapter, %d in Numbers; %d "and it shall" verbs; "to you" %d; Judah\'s border shares %d of %d; Ezekiel shares %d tokens' % (len(NUM_POINTS), [len(SIDES[s]['points']) for s in SIDES], len(BORDER_TOKENS), BORDER_NUM, len(SHALL_BE), len(TO_YOU), len(SHARED_S), len(NUM_S), len(EZEK_SHARED)))
    print('THE ROSTER: %s; only here by token %d, by lemma %d; the order matches %s; Joshua\'s tribe %s' % ([(r['tribe'], r['prince'], r['father'], r['title']) for r in ROSTER], len(ONLY_HERE_TOKEN), len(ONLY_HERE_LEMMA), MATCHES or 'none', JOSHUA_TRIBE))
    print('THE SCENE on the bench: %s; the timers (set, fired, cancelled, pending) %s; entities %d' % SCENE)
    print('THE NARRATIVE: %s' % (NARRATIVE,))
    print('THE PARAMETER ROWS: ' + '; '.join('%s = %s' % (k, (DATA[k]['value'] if k not in ('the_four_sides', 'the_roster') else '%d rows (a data list)' % len(DATA[k]['value']))) for k in DATA) + ' (the other settings recorded in DATA)')
    if ok == len(CASES):
        print('\nTHE COMPILE OF THE BORDERS: the answer sheet REPRODUCED — %d/%d' % (ok, len(CASES)))
    sys.exit(0 if ok == len(CASES) else 1)
