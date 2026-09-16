
# ---- THE WRAP — the daemon, the scene, the narrative ------------------------------------------------------
CELL_TAG = {'commission': 'F0', 'frame': 'F1', 'judges': 'F2', 'spies': 'F3', 'bypass': 'F4', 'sihon_og': 'F5', 'east': 'F6', 'plea': 'F7'}
CELL_FN = {'commission': the_commission, 'frame': the_frame, 'spies': the_spies_read_back, 'bypass': the_bypass, 'sihon_og': sihon_and_og, 'east': the_east_and_the_charges, 'plea': the_plea}

def _closed_by_prior_run(world, event, eff, closer):
    """THE CLOSE BY A PRIOR RUN (THE READBACK'S FIRST FORM, R3): a supplied debit is OPENED AND CLOSED IN ONE BLOCK — the engine writes a daemon's
    effects after the daemon returns, so the daemon writes this one itself, stamped as the engine would stamp it (the event's date, the writer),
    and closes it at once with the tape's EARLIER line as the closer (closed_by naming the run's verse): the ledger's own record that the command
    came to the reader after its execution. The recorder never records a daemon's close as a tape line (the close is the daemon's own write)."""
    for key in ('bound', 'dated'):
        if key in event:
            eff.setdefault(key, event[key])
    eff.setdefault('written_by', 'law_opening_speech')
    world._write(eff)
    world.close(eff['subject'], eff['effect'], closer, value=eff['value'])

def law_opening_speech(event, world):
    """Deut 1:1-3:29 with Num 27:12-23 (cold_run_opening_speech.py F0-F7). given_at Deut 1:16; installed_by boot — A LAW IN MOSES' VOICE WITH NO
    DIVINE FRAME (the vows' class; the class named in the registry, the second pass decides). SIXTEEN TAPE LINES: the commission's four (Num
    27:12-23 — a debit on Moses OPEN to Deuteronomy 34, the shepherd's plea, the commission's debit and its CLOSE by its run); the frame (the book's
    one act of its own day — torah_expounded on Israel); the eleven acts told only in the retelling, each written ONCE at its own time by a
    retrograde marker — four supplied debits CLOSED AT ONCE BY A PRIOR RUN, the judges' charge (THE LAW — a status on the court), the three bars
    and grants, the two bans, Joshua's promise, the plea with its refusal. The exam's two case kinds dispatch to the cells in EXPLICIT branches with
    LITERAL effects per kind (2b's form — an unnamed effect is a KeyError)."""
    k, src = event['kind'], event['case_source']
    E_ = lambda eff, s, cp=None, amount=None, due=None, law='', value=None: {'effect': eff, 'subject': s, 'counterparty': cp, 'amount': amount, 'due': due, 'value': value if value is not None else True, 'source_law': law, 'case_source': src}
    # ---- F0: the commission (Num 27:12-23 — page_order at the daughters' day) ----
    if k == 'moses_told_to_ascend_abarim':
        return [E_('commanded', 'moses', value='see_the_land_from_abarim', law='F0 [INK 27:12 "go up to this mountain of Abarim and see the land" — the debit OPEN BY DESIGN to Deuteronomy 34:1-4 (this book\'s own end); 27:14\'s Meribah an INTERNAL pointer to 20:12\'s sentence, the barred entry read; Deuteronomy 3:27 the retelling READ BACK]')]
    if k == 'a_shepherd_asked':
        return [E_('plea_made', 'moses', value='let the LORD, the God of the spirits of all flesh, appoint a man over the congregation, who may go out before them and come in before them, that the congregation of the LORD be not as sheep without a shepherd (27:16-17)', law='F0 [INK 27:15-17 — the successor asked before he is named; 16:22\'s phrase at its second seat; Sanhedrin 17a:10 Eldad and Medad\'s prophecy]')]
    if k == 'joshua_commission_commanded':
        return [E_('commanded', 'moses', value='commission_joshua_before_eleazar', law='F0 [INK 27:18-21 "take you Joshua … lay your hand upon him; set him before Eleazar the priest … put of your honor upon him … by the judgment of the Urim" — one hand commanded (the Sifrei 141); the Urim final (C2 by CALL); the debit CLOSED by the next line\'s run]')]
    if k == 'joshua_commissioned':
        world.close('moses', 'commanded', 'Num 27:22-23 — and Moses did as the LORD commanded him; he took Joshua and set him before Eleazar the priest and before all the congregation, and laid his hands upon him and commanded him, as the LORD spoke by the hand of Moses: THE COMMISSION\'S DEBIT CLOSED BY ITS RUN (the receipt "as the LORD commanded" — the spec/run pair\'s form); the register seat Num 27:22 CLOSE', value='commission_joshua_before_eleazar')
        return [E_('invested_office', 'joshua', value='the hand laid — two hands for the one commanded (27:23; the Sifrei 141); some of Moses\' honor (27:20 — the sun and the moon, Bava Batra 75a:8); before Eleazar the priest by the judgment of the Urim (27:21)', law='F0 [INK 27:22-23 "and he laid his hands upon him and commanded him, as the LORD spoke by the hand of Moses" — Joshua invested; Deuteronomy 3:28 "command Joshua" the commissioning READ BACK (Kiddushin 29a:14)]')]
    # ---- F1: the frame — the book's one act of its own day (text_constrained at the marker's verse) ----
    if k == 'speech_opened':
        return [E_('torah_expounded', 'israel', value={'words': 'these are the words which Moses spoke to all Israel beyond the Jordan (1:1) — the eleven places the rebuke\'s sins (the Sifrei 1; Onkelos)', 'date': (40, 11, 1), 'receipt': 'according to all that the LORD commanded him (1:3) — the hermeneutic rules (the Sifrei 2:8)', 'after': 'after he had smitten Sihon and Og (1:4) — the fortieth year\'s order (Rosh Hashanah 2b:13)'}, law='F1 [INK 1:5 "Moses undertook to expound this Torah" — the frame: a STATUS on Israel dated (40, 11, 1) by 1:3\'s number reader, the era the exodus\'s by the taught verbal analogy with 33:38 (Rosh Hashanah 2b:11; JO by CALL); everything after it in chapters 1-3 read back or supplied at its own time (R6); the register seat Deut 1:3 ACT]')]
    # ---- F2: the Horeb command (supplied, dated (2, 2, 20)) and the judges' charge (THE LAW, dated (1, 2, 16)) ----
    if k == 'horeb_departure_commanded':
        _closed_by_prior_run(world, event, E_('commanded', 'israel', value='journey_to_the_mountain_of_the_amorite', law='F2 [INK 1:6-8 "you have dwelt long enough in this mountain; turn and take your journey and go to the hill country of the Amorites … go in and possess the land" — TOLD ONLY IN THE RETELLING (Exodus 33:1 the command\'s kin): written once, dated (2, 2, 20) by the retrograde marker at 1:6, CLOSED AT ONCE BY THE PRIOR RUN — the arrival in Paran; "go in and possess" a REFERENCE to land_granted (Genesis 15:18) and the OPEN dispossess debit (33:50-56)]'),
                             'Num 12:16 — and afterward the people journeyed from Hazeroth and encamped in the wilderness of Paran: THE CLOSE BY A PRIOR RUN (R3) — the departure from Horeb commanded at Deuteronomy 1:6-8 ran at Numbers 10:11-12:16, the tape\'s earlier line; the command came to the reader after its execution')
        return []
    if k == 'judges_charged':
        return [E_('judges_charged', 'the-court', value=['hear between your brothers', 'judge righteously between a man and his brother and his stranger', 'no faces in judgment', 'the small as the great', 'fear no man, for the judgment is God\'s', 'the hard matter to me'], law='F2 [INK 1:16-17 "and I charged your judges at that time, saying: hear between your brothers, and judge righteously between a man and his brother and the stranger with him; you shall not respect persons in judgment; you shall hear the small and the great alike; you shall not be afraid of the face of any man, for the judgment is God\'s; and the cause that is too hard for you, you shall bring to me" — THE LAW OF THE SPAN in Moses\' voice with no divine frame: ONE STATUS on the court, the six clauses, dated (1, 2, 16) by the court\'s founding day read off Israel\'s ledger (the retrograde marker at 1:9); the appointment (1:9-15) a REFERENCE to judges_appointed (Exodus 18:25 — TURNED); the clauses\' arms the exam\'s rows (Sanhedrin 7b:14-8a:6; 6b; Mishnah Sanhedrin 1, 3, 4; Avot 1:1)]')]
    # ---- F4: the bypass — the supplied acts dated (40, 6, 1) by the retrograde marker at 2:2 ----
    if k == 'turn_northward_commanded':
        _closed_by_prior_run(world, event, E_('commanded', 'israel', value='turn_northward', law='F4 [INK 2:2-3 "you have compassed this mountain long enough; turn you northward" — TOLD ONLY HERE: written once, dated (40, 6, 1) by the retrograde marker at 2:2 (the departure from Mount Hor), CLOSED AT ONCE BY THE PRIOR RUN — the march past Moab (21:10-13)]'),
                             'Num 21:10-13 — and the children of Israel journeyed and camped at Oboth; and from Oboth at Iye-abarim in the wilderness before Moab toward the sunrise; and from there at the brook Zered; and from there beyond the Arnon: THE CLOSE BY A PRIOR RUN (R3) — the turn northward commanded at Deuteronomy 2:2-3 ran at Numbers 21:10-13, the tape\'s earlier line')
        return [E_('contending_barred', 'edom', value='do not contend with them; not so much as for the sole of the foot to tread on (2:5) — your brothers the sons of Esau who dwell in Seir (2:4, 2:8)', law='F4 [INK 2:4-5 "do not contend with them, for I will not give you of their land" — the BLOCK on Edom told only here; the bar\'s reach: battle and harassing alike (Edom "your brothers" — Deuteronomy 23:8 forward); Bava Kamma 38a:16 Moses\' a fortiori from Midian needed the bar]'),
                E_('land_granted', 'edom', value='mount_seir', law='F4 [INK 2:5 "because I have given Mount Seir to Esau for a possession" — the grant told here: Genesis 36:8\'s dwelling in Seir (JS by CALL) the standing status; Kiddushin 18a:2 — a gentile inherits by Torah law from this verse; Bereshit Rabbah 44:23 the Kenite kept for Edom (PR by CALL)]')]
    if k == 'moab_spared_commanded':
        return [E_('contending_barred', 'the-moabites', value='do not harass Moab nor contend with them in battle (2:9) — battle forbidden, harassing not (Horayot 10b:19; Nazir 23b:11)', law='F4 [INK 2:9 "do not harass Moab nor contend with them in battle, for I will not give you of his land" — the BLOCK on the Moabites told only here; the bar the a fortiori from Midian needed (Bava Kamma 38a:16 — BK by CALL); the reward of the elder daughter\'s euphemism (Horayot 10b:19)]'),
                E_('land_granted', 'the-moabites', value='ar', law='F4 [INK 2:9 "because I have given Ar to the children of Lot for a possession" — the grant told here: Lot\'s elder daughter\'s people (Genesis 19:37 — MM by CALL); Moab\'s land purified through Sihon (Chullin 60b:13 — CK.DATA by CALL)]')]
    if k == 'zered_crossing_commanded':
        _closed_by_prior_run(world, event, E_('commanded', 'israel', value='cross_the_brook_zered', law='F4 [INK 2:13 "now rise up and get you over the brook Zered; and we went over the brook Zered" — TOLD ONLY HERE: written once, dated (40, 6, 1), CLOSED AT ONCE BY THE PRIOR RUN — the camp at the brook Zered (21:12, inside the four camps\' line); 2:14\'s thirty-eight years from Kadesh-barnea against the tape\'s years (CA2)]'),
                             'Num 21:10-13 — and from there they journeyed and camped at the brook Zered (21:12): THE CLOSE BY A PRIOR RUN (R3) — the crossing of the Zered commanded at Deuteronomy 2:13 ran at Numbers 21:12, inside the tape\'s earlier line of the four camps (21:10-13); the thirty-eight years (2:14) the tape\'s own years from the spies\' return')
        return []
    if k == 'ammon_spared_commanded':
        return [E_('contending_barred', 'the-sons-of-ammon', value='do not harass them nor contend with them (2:19) — not even harassed (Bava Kamma 38b:6; Horayot 11a:1; Nazir 23b:12)', law='F4 [INK 2:19 "when you come near over against the children of Ammon, do not harass them nor contend with them, for I will not give you of the land of the children of Ammon" — the BLOCK on the sons of Ammon told only here — the one NEW written-on party (Genesis 19:38\'s people); Ammon\'s border strong at 21:24, commanded off-limits here (CK.DATA by CALL); the reward of the younger daughter\'s euphemism]'),
                E_('land_granted', 'the-sons-of-ammon', value='the land of the sons of Ammon', law='F4 [INK 2:19 "because I have given it to the children of Lot for a possession" — the grant told here: Lot\'s younger daughter\'s people (Genesis 19:38 — MM by CALL)]')]
    if k == 'sihon_war_commanded':
        _closed_by_prior_run(world, event, E_('commanded', 'israel', value='begin_to_possess_sihons_land', law='F4 [INK 2:24-25 "rise up, take your journey, and pass over the valley of Arnon; behold, I have given into your hand Sihon … begin to possess it, and contend with him in battle; this day will I begin to put the dread of you" (2:31 "begin to possess, that you may inherit his land") — TOLD ONLY HERE (21:21 says Israel sent messengers, no command): written once, dated (40, 6, 1), CLOSED AT ONCE BY THE PRIOR RUN — the smiting and possession (21:24-25); the dread DATA (Avodah Zarah 25a:7-9; Taanit 20a:6-8 — the sun for Moses)]'),
                             'Num 21:24-25 — and Israel smote him with the edge of the sword and possessed his land from the Arnon to the Jabbok, as far as the sons of Ammon; and Israel took all these cities and dwelt in all the cities of the Amorite: THE CLOSE BY A PRIOR RUN (R3) — the war on Sihon commanded at Deuteronomy 2:24-25 ran at Numbers 21:24-25, the tape\'s earlier line')
        return []
    # ---- F5: the bans told only in the retelling (supplied acts on the Amorite) ----
    if k == 'sihons_cities_devoted':
        return [E_('destroyed', 'the-amorite', cp='israel', value='every city of Sihon\'s — the men, the women and the little ones; none left; the cattle and the spoil taken (2:34-35)', law='F5 [INK 2:34-35 "and we took all his cities at that time, and utterly destroyed every city, the men and the women and the little ones; we left none remaining; only the cattle we took for a prey" — THE BAN TOLD ONLY HERE (21:24-25 say smote and possessed): the body effect the king of Arad\'s line wrote at 21:3, on the Amorite; Genesis 15:16\'s amorite_not_full status READ beside it (PR by CALL — a printed line, no verdict); Deuteronomy 20:16-17\'s law FORWARD]')]
    if k == 'ogs_cities_devoted':
        return [E_('destroyed', 'the-amorite', cp='israel', value='every city of Og\'s sixty — the men, the women and the little ones; the cattle and the spoil taken (3:6-7)', law='F5 [INK 3:6-7 "and we utterly destroyed them, as we did to Sihon king of Heshbon, utterly destroying every city, the men and the women and the little ones; but all the cattle and the spoil of the cities we took" — THE SECOND BAN TOLD ONLY HERE (21:35 says smote and possessed); the sixty cities of Argob (3:4-5 — [60]; Arakhin 32b:6 the walled cities from Joshua\'s days)]')]
    # ---- F6: Joshua's promise (supplied) ----
    if k == 'joshua_encouraged':
        return [E_('fear_not_promised', 'joshua', value='your eyes have seen all that the LORD your God has done to these two kings; so shall the LORD do to all the kingdoms; you shall not fear them, for the LORD your God, He fights for you (3:21-22)', law='F6 [INK 3:21-22 "and I commanded Joshua at that time, saying: your eyes have seen … you shall not fear them" — TOLD ONLY HERE: HEAVEN\'s promise on Joshua, 21:34\'s effect ("fear him not", on Moses) at its second party; Joshua 1:6 and Ai\'s run outside the Torah (the Sifrei 29:8-9 the condition Joshua broke — DATA); Joshua written plene here alone in the Torah]')]
    # ---- F7: the plea with its refusal (supplied) ----
    if k == 'moses_besought':
        return [E_('plea_made', 'moses', value='let me go over, I pray, and see the good land beyond the Jordan, that goodly hill country and Lebanon (3:25) — REFUSED: let it suffice you; speak no more to Me of this matter (3:26); the LORD was wroth with me for your sakes and did not hear me', law='F7 [INK 3:23-26 "and I besought the LORD at that time … O Lord GOD, You have begun to show Your servant Your greatness … let me go over … but the LORD was wroth with me for your sakes" — TOLD ONLY HERE: the plea AND its answer in the value as Hobab\'s row carries the refusal (BH by CALL); the barred_from_the_land entry on Moses OPEN, READ — no new heaven write; praise before the request (Berakhot 32a:32); "let it suffice you" measure for measure (Sotah 13b:13); Lebanon the Temple (Gittin 56b:1)]')]
    # ---- the exam's case kinds: EXPLICIT branches per kind (the daemon gate parses explicit branches only), each naming LITERALLY every effect it can write (2b's form — an unnamed effect is a KeyError) ----
    if k == 'judges_case':
        v, e, _ = the_officers_and_the_judges({'ask': event['ask']}, DATA); L = 'F2 [%s]' % event['ask']; s_ = event['person']
        W = {'accepted': E_('accepted', s_, value=v, law=L), 'exempt': E_('exempt', s_, value=v, law=L), 'judgment_perverted': E_('judgment_perverted', s_, value=v, law=L)}
        return [W[x] for x in e if x != FX.NONE]
    if k == 'speech_case':
        v, e, _ = CELL_FN[event['cell']]({'ask': event['ask']}, DATA); L = '%s [%s]' % (CELL_TAG[event['cell']], event['ask']); s_ = event['person']
        W = {'accepted': E_('accepted', s_, value=v, law=L), 'exempt': E_('exempt', s_, value=v, law=L)}
        return [W[x] for x in e if x != FX.NONE]
    return []


LINES = [
    ('Num 27:12-14 — and the LORD said to Moses: go up to this mountain of Abarim and see the land which I have given to the children of Israel; and when you have seen it, you also shall be gathered to your people, as Aaron your brother was gathered; because you rebelled against My word in the wilderness of Zin, in the strife of the congregation, to sanctify Me at the waters before their eyes — these are the waters of Meribah of Kadesh in the wilderness of Zin', 'moses_told_to_ascend_abarim'),
    ('Num 27:15-17 — and Moses spoke to the LORD, saying: let the LORD, the God of the spirits of all flesh, appoint a man over the congregation, who may go out before them and who may come in before them, and who may lead them out and who may bring them in, that the congregation of the LORD be not as sheep which have no shepherd', 'a_shepherd_asked'),
    ('Num 27:18-21 — and the LORD said to Moses: take you Joshua the son of Nun, a man in whom is spirit, and lay your hand upon him; and set him before Eleazar the priest and before all the congregation, and command him in their sight; and you shall put of your honor upon him, that all the congregation of the children of Israel may hear; and he shall stand before Eleazar the priest, who shall inquire for him by the judgment of the Urim before the LORD; at his word shall they go out and at his word shall they come in', 'joshua_commission_commanded'),
    ('Num 27:22-23 — and Moses did as the LORD commanded him; and he took Joshua and set him before Eleazar the priest and before all the congregation; and he laid his hands upon him and commanded him, as the LORD spoke by the hand of Moses', 'joshua_commissioned'),
    ('Deut 1:1-5 — these are the words which Moses spoke to all Israel beyond the Jordan, in the wilderness, in the Arabah over against Suph, between Paran and Tophel and Laban and Hazeroth and Di-zahab; eleven days from Horeb by the way of Mount Seir to Kadesh-barnea; and it came to pass in the fortieth year, in the eleventh month, on the first of the month, that Moses spoke to the children of Israel according to all that the LORD had commanded him to them; after he had smitten Sihon king of the Amorites who dwelt in Heshbon, and Og king of Bashan who dwelt in Ashtaroth, at Edrei; beyond the Jordan, in the land of Moab, Moses undertook to expound this Torah, saying', 'speech_opened'),
    ('Deut 1:6-8 — the LORD our God spoke to us in Horeb, saying: you have dwelt long enough in this mountain; turn and take your journey and go to the hill country of the Amorites and to all the places near it, in the Arabah, in the hill country, in the lowland, in the Negev and by the seashore, the land of the Canaanites and Lebanon, as far as the great river, the river Euphrates; behold, I have set the land before you: go in and possess the land which the LORD swore to your fathers, to Abraham, to Isaac and to Jacob, to give to them and to their seed after them', 'horeb_departure_commanded'),
    ('Deut 1:16-18 — and I charged your judges at that time, saying: hear the causes between your brothers, and judge righteously between a man and his brother and the stranger with him; you shall not respect persons in judgment; you shall hear the small and the great alike; you shall not be afraid of the face of any man, for the judgment is God\'s; and the cause that is too hard for you, you shall bring to me and I will hear it; and I commanded you at that time all the things that you should do', 'judges_charged'),
    ('Deut 2:2-7 — and the LORD spoke to me, saying: you have compassed this mountain long enough; turn you northward; and command the people, saying: you are to pass through the border of your brothers the children of Esau, who dwell in Seir, and they will be afraid of you; take good heed to yourselves therefore; do not contend with them, for I will not give you of their land, no, not so much as for the sole of the foot to tread on, because I have given Mount Seir to Esau for a possession; you shall buy food of them for money, that you may eat, and water for money, that you may drink; for the LORD your God has blessed you in all the work of your hand; these forty years the LORD your God has been with you; you have lacked nothing', 'turn_northward_commanded'),
    ('Deut 2:9 — and the LORD said to me: do not harass Moab nor contend with them in battle, for I will not give you of his land for a possession, because I have given Ar to the children of Lot for a possession', 'moab_spared_commanded'),
    ('Deut 2:13 — now rise up and get you over the brook Zered; and we went over the brook Zered', 'zered_crossing_commanded'),
    ('Deut 2:17-19 — and the LORD spoke to me, saying: you are this day to pass over Ar, the border of Moab; and when you come near over against the children of Ammon, do not harass them nor contend with them, for I will not give you of the land of the children of Ammon for a possession, because I have given it to the children of Lot for a possession', 'ammon_spared_commanded'),
    ('Deut 2:24-25 — rise up, take your journey, and pass over the valley of Arnon; behold, I have given into your hand Sihon the Amorite, king of Heshbon, and his land; begin to possess it, and contend with him in battle; this day will I begin to put the dread of you and the fear of you upon the peoples that are under the whole heaven, who, when they hear the report of you, shall tremble and be in anguish because of you (2:31: the LORD said to me: behold, I have begun to deliver up Sihon and his land before you; begin to possess, that you may inherit his land)', 'sihon_war_commanded'),
    ('Deut 2:34-35 — and we took all his cities at that time, and utterly destroyed every city, the men and the women and the little ones; we left none remaining; only the cattle we took for a prey to ourselves, with the spoil of the cities which we had taken', 'sihons_cities_devoted'),
    ('Deut 3:6-7 — and we utterly destroyed them, as we did to Sihon king of Heshbon, utterly destroying every city, the men and the women and the little ones; but all the cattle and the spoil of the cities we took for a prey to ourselves', 'ogs_cities_devoted'),
    ('Deut 3:21-22 — and I commanded Joshua at that time, saying: your eyes have seen all that the LORD your God has done to these two kings; so shall the LORD do to all the kingdoms to which you go over; you shall not fear them, for the LORD your God, He it is who fights for you', 'joshua_encouraged'),
    ('Deut 3:23-26 — and I besought the LORD at that time, saying: O Lord GOD, You have begun to show Your servant Your greatness and Your strong hand; for what god is there in heaven or on earth that can do according to Your works and according to Your mighty acts; let me go over, I pray, and see the good land that is beyond the Jordan, that goodly hill country and Lebanon; but the LORD was wroth with me for your sakes and did not hear me; and the LORD said to me: let it suffice you; speak no more to Me of this matter', 'moses_besought'),
]
CLOSES = "five, none a tape line: the commission's debit on Moses CLOSED BY ITS RUN inside the daemon (27:22-23 — the register seat Num 27:22 CLOSE); the four supplied debits on Israel CLOSED AT ONCE BY A PRIOR RUN inside the daemon (Num 12:16; 21:10-13; 21:10-13; 21:24-25 — the tape's earlier lines); see_the_land_from_abarim OPEN to Deuteronomy 34:1-4; the two DISAGREES rows OPEN"

# the exam's persons through the two case kinds: (kind, person, cell, ask, the shelf's citation)
PERSONS = [
    ('judges_case', 'the-hearer', 'judges', 'hear', 'Sanhedrin 7b:14 — the exam\'s row hear'),
    ('judges_case', 'the-righteous-judge', 'judges', 'judge_righteously', 'Sanhedrin 7a:17 — the exam\'s row judge_righteously'),
    ('judges_case', 'the-befriended', 'judges', 'no_faces', 'Sanhedrin 7b:18; Mishnah Sanhedrin 3:4-5 — the exam\'s row no_faces'),
    ('judges_case', 'the-peruta', 'judges', 'small_and_great', 'Sanhedrin 8a:2 — the exam\'s row small_and_great'),
    ('judges_case', 'the-gatherer-of-words', 'judges', 'no_fear', 'Sanhedrin 7a:16 — the exam\'s row no_fear'),
    ('judges_case', 'the-mountain-piercer', 'judges', 'the_judgment_is_gods', 'Sanhedrin 6b:3 — the exam\'s row the_judgment_is_gods'),
    ('judges_case', 'the-hard-matter', 'judges', 'the_hard_matter', 'Sifrei Devarim 17:7 — the exam\'s row the_hard_matter'),
    ('judges_case', 'the-convert', 'judges', 'the_stranger', 'Yevamot 47a:7 — the exam\'s row the_stranger'),
    ('judges_case', 'the-mediator', 'judges', 'the_compromise', 'Sanhedrin 6b:1-15 — the exam\'s row the_compromise'),
    ('judges_case', 'the-refuser-before-hearing', 'judges', 'the_refusal_before_hearing', 'Sanhedrin 6b:12 — the exam\'s row the_refusal_before_hearing'),
    ('judges_case', 'the-perverter', 'judges', 'the_perverting_judge', 'Sifra Kedoshim 4:1; Sanhedrin 7a:18 — the exam\'s row the_perverting_judge'),
    ('judges_case', 'the-money-court', 'judges', 'money_and_capital', 'Mishnah Sanhedrin 4:1 — the exam\'s row money_and_capital'),
    ('judges_case', 'the-three', 'judges', 'the_court_of_three', 'Mishnah Sanhedrin 1:1, 3:1 — the exam\'s row the_court_of_three'),
    ('judges_case', 'the-deliberate', 'judges', 'be_deliberate', 'Pirkei Avot 1:1 — the exam\'s row be_deliberate'),
    ('judges_case', 'the-counted-officers', 'judges', 'the_count', 'Sanhedrin 18a:3 — the exam\'s row the_count'),
    ('judges_case', 'the-seven-sought', 'judges', 'the_qualities', 'Sifrei Devarim 15:2; Eruvin 100b:18 — the exam\'s row the_qualities'),
    ('speech_case', 'the-dated-speech', 'frame', 'the_date', 'Rosh Hashanah 2b:11 — the exam\'s row the_date'),
    ('speech_case', 'the-received-rules', 'frame', 'the_receipt_of_the_rules', 'Sifrei Devarim 2:8 — the exam\'s row the_receipt_of_the_rules'),
    ('speech_case', 'the-askers', 'spies', 'the_asking', 'Sotah 34b:3 — the exam\'s row the_asking'),
    ('speech_case', 'the-little-ones', 'spies', 'the_little_ones', 'Numbers 14:31 — the exam\'s row the_little_ones'),
    ('speech_case', 'the-excepted', 'spies', 'the_exceptions', 'Numbers 14:24, 30 — the exam\'s row the_exceptions'),
    ('speech_case', 'the-harasser-of-moab', 'bypass', 'harassing_permitted', 'Horayot 10b:19 — the exam\'s row harassing_permitted'),
    ('speech_case', 'the-buyer-from-esau', 'bypass', 'forty_years_lacking_nothing', 'Exodus 16:35 — the exam\'s row forty_years_lacking_nothing'),
    ('speech_case', 'the-thirty-eight', 'bypass', 'the_men_of_war_consumed', 'Taanit 30b:12 — the exam\'s row the_men_of_war_consumed'),
    ('speech_case', 'the-messengers', 'sihon_og', 'the_messengers', 'Numbers 21:22 — the exam\'s row the_messengers'),
    ('speech_case', 'the-sixty', 'sihon_og', 'the_sixty_cities', 'Arakhin 32b:6 — the exam\'s row the_sixty_cities'),
    ('speech_case', 'the-bed', 'sihon_og', 'ogs_bed', 'Mishnah Kelim 17:9 — the exam\'s row ogs_bed'),
    ('speech_case', 'the-divided-east', 'east', 'the_division', 'Numbers 32:33 — the exam\'s row the_division'),
    ('speech_case', 'the-armed', 'east', 'the_charge_to_the_tribes', 'Joshua 1:15 — the exam\'s row the_charge_to_the_tribes'),
    ('speech_case', 'the-named-lord', 'plea', 'the_names', 'Sifrei Devarim 27:4 — the exam\'s row the_names'),
    ('speech_case', 'the-temple-mountain', 'plea', 'lebanon', 'Gittin 56b:1 — the exam\'s row lebanon'),
    ('speech_case', 'the-urim', 'commission', 'the_urim', 'Yoma 73b:3 — the exam\'s row the_urim'),
    ('speech_case', 'the-honored', 'commission', 'the_honor', 'Bava Batra 75a:8 — the exam\'s row the_honor'),
]

def scene():
    """THE SCENE — the exam's rows replayed on the world engine (the exodus epoch): the exam's persons through the two case kinds — the judges'
    charge clause by clause, the courts, the frame, the spies, the bypass, Sihon and Og, the east, the plea, the commission."""
    with contextlib.redirect_stdout(io.StringIO()):
        w = WE.World(era='Deut 1:1-3:29 with Num 27:12-23: the opening speech on the shelf — Sanhedrin, Rosh Hashanah, Sotah, Bava Kamma, Horayot, Kiddushin, Arakhin, Gittin on the engine (the exodus epoch)', epoch='exodus')
        w.laws = [law_opening_speech]
        w.advance(w.clock.day_in('exodus', 40, 11, 1))
        # THE DAEMON GATE READS LITERAL SUBMITS ONLY (the refuge runner's lesson, 2026-09-13) — the thirty-three persons typed out from PERSONS
        w.submit({'kind': 'judges_case', 'subject': 'the-hearer', 'person': 'the-hearer', 'cell': 'judges', 'ask': 'hear', 'case_source': "Sanhedrin 7b:14 — the exam's row hear"})
        w.submit({'kind': 'judges_case', 'subject': 'the-righteous-judge', 'person': 'the-righteous-judge', 'cell': 'judges', 'ask': 'judge_righteously', 'case_source': "Sanhedrin 7a:17 — the exam's row judge_righteously"})
        w.submit({'kind': 'judges_case', 'subject': 'the-befriended', 'person': 'the-befriended', 'cell': 'judges', 'ask': 'no_faces', 'case_source': "Sanhedrin 7b:18; Mishnah Sanhedrin 3:4-5 — the exam's row no_faces"})
        w.submit({'kind': 'judges_case', 'subject': 'the-peruta', 'person': 'the-peruta', 'cell': 'judges', 'ask': 'small_and_great', 'case_source': "Sanhedrin 8a:2 — the exam's row small_and_great"})
        w.submit({'kind': 'judges_case', 'subject': 'the-gatherer-of-words', 'person': 'the-gatherer-of-words', 'cell': 'judges', 'ask': 'no_fear', 'case_source': "Sanhedrin 7a:16 — the exam's row no_fear"})
        w.submit({'kind': 'judges_case', 'subject': 'the-mountain-piercer', 'person': 'the-mountain-piercer', 'cell': 'judges', 'ask': 'the_judgment_is_gods', 'case_source': "Sanhedrin 6b:3 — the exam's row the_judgment_is_gods"})
        w.submit({'kind': 'judges_case', 'subject': 'the-hard-matter', 'person': 'the-hard-matter', 'cell': 'judges', 'ask': 'the_hard_matter', 'case_source': "Sifrei Devarim 17:7 — the exam's row the_hard_matter"})
        w.submit({'kind': 'judges_case', 'subject': 'the-convert', 'person': 'the-convert', 'cell': 'judges', 'ask': 'the_stranger', 'case_source': "Yevamot 47a:7 — the exam's row the_stranger"})
        w.submit({'kind': 'judges_case', 'subject': 'the-mediator', 'person': 'the-mediator', 'cell': 'judges', 'ask': 'the_compromise', 'case_source': "Sanhedrin 6b:1-15 — the exam's row the_compromise"})
        w.submit({'kind': 'judges_case', 'subject': 'the-refuser-before-hearing', 'person': 'the-refuser-before-hearing', 'cell': 'judges', 'ask': 'the_refusal_before_hearing', 'case_source': "Sanhedrin 6b:12 — the exam's row the_refusal_before_hearing"})
        w.submit({'kind': 'judges_case', 'subject': 'the-perverter', 'person': 'the-perverter', 'cell': 'judges', 'ask': 'the_perverting_judge', 'case_source': "Sifra Kedoshim 4:1; Sanhedrin 7a:18 — the exam's row the_perverting_judge"})
        w.submit({'kind': 'judges_case', 'subject': 'the-money-court', 'person': 'the-money-court', 'cell': 'judges', 'ask': 'money_and_capital', 'case_source': "Mishnah Sanhedrin 4:1 — the exam's row money_and_capital"})
        w.submit({'kind': 'judges_case', 'subject': 'the-three', 'person': 'the-three', 'cell': 'judges', 'ask': 'the_court_of_three', 'case_source': "Mishnah Sanhedrin 1:1, 3:1 — the exam's row the_court_of_three"})
        w.submit({'kind': 'judges_case', 'subject': 'the-deliberate', 'person': 'the-deliberate', 'cell': 'judges', 'ask': 'be_deliberate', 'case_source': "Pirkei Avot 1:1 — the exam's row be_deliberate"})
        w.submit({'kind': 'judges_case', 'subject': 'the-counted-officers', 'person': 'the-counted-officers', 'cell': 'judges', 'ask': 'the_count', 'case_source': "Sanhedrin 18a:3 — the exam's row the_count"})
        w.submit({'kind': 'judges_case', 'subject': 'the-seven-sought', 'person': 'the-seven-sought', 'cell': 'judges', 'ask': 'the_qualities', 'case_source': "Sifrei Devarim 15:2; Eruvin 100b:18 — the exam's row the_qualities"})
        w.submit({'kind': 'speech_case', 'subject': 'the-dated-speech', 'person': 'the-dated-speech', 'cell': 'frame', 'ask': 'the_date', 'case_source': "Rosh Hashanah 2b:11 — the exam's row the_date"})
        w.submit({'kind': 'speech_case', 'subject': 'the-received-rules', 'person': 'the-received-rules', 'cell': 'frame', 'ask': 'the_receipt_of_the_rules', 'case_source': "Sifrei Devarim 2:8 — the exam's row the_receipt_of_the_rules"})
        w.submit({'kind': 'speech_case', 'subject': 'the-askers', 'person': 'the-askers', 'cell': 'spies', 'ask': 'the_asking', 'case_source': "Sotah 34b:3 — the exam's row the_asking"})
        w.submit({'kind': 'speech_case', 'subject': 'the-little-ones', 'person': 'the-little-ones', 'cell': 'spies', 'ask': 'the_little_ones', 'case_source': "Numbers 14:31 — the exam's row the_little_ones"})
        w.submit({'kind': 'speech_case', 'subject': 'the-excepted', 'person': 'the-excepted', 'cell': 'spies', 'ask': 'the_exceptions', 'case_source': "Numbers 14:24, 30 — the exam's row the_exceptions"})
        w.submit({'kind': 'speech_case', 'subject': 'the-harasser-of-moab', 'person': 'the-harasser-of-moab', 'cell': 'bypass', 'ask': 'harassing_permitted', 'case_source': "Horayot 10b:19 — the exam's row harassing_permitted"})
        w.submit({'kind': 'speech_case', 'subject': 'the-buyer-from-esau', 'person': 'the-buyer-from-esau', 'cell': 'bypass', 'ask': 'forty_years_lacking_nothing', 'case_source': "Exodus 16:35 — the exam's row forty_years_lacking_nothing"})
        w.submit({'kind': 'speech_case', 'subject': 'the-thirty-eight', 'person': 'the-thirty-eight', 'cell': 'bypass', 'ask': 'the_men_of_war_consumed', 'case_source': "Taanit 30b:12 — the exam's row the_men_of_war_consumed"})
        w.submit({'kind': 'speech_case', 'subject': 'the-messengers', 'person': 'the-messengers', 'cell': 'sihon_og', 'ask': 'the_messengers', 'case_source': "Numbers 21:22 — the exam's row the_messengers"})
        w.submit({'kind': 'speech_case', 'subject': 'the-sixty', 'person': 'the-sixty', 'cell': 'sihon_og', 'ask': 'the_sixty_cities', 'case_source': "Arakhin 32b:6 — the exam's row the_sixty_cities"})
        w.submit({'kind': 'speech_case', 'subject': 'the-bed', 'person': 'the-bed', 'cell': 'sihon_og', 'ask': 'ogs_bed', 'case_source': "Mishnah Kelim 17:9 — the exam's row ogs_bed"})
        w.submit({'kind': 'speech_case', 'subject': 'the-divided-east', 'person': 'the-divided-east', 'cell': 'east', 'ask': 'the_division', 'case_source': "Numbers 32:33 — the exam's row the_division"})
        w.submit({'kind': 'speech_case', 'subject': 'the-armed', 'person': 'the-armed', 'cell': 'east', 'ask': 'the_charge_to_the_tribes', 'case_source': "Joshua 1:15 — the exam's row the_charge_to_the_tribes"})
        w.submit({'kind': 'speech_case', 'subject': 'the-named-lord', 'person': 'the-named-lord', 'cell': 'plea', 'ask': 'the_names', 'case_source': "Sifrei Devarim 27:4 — the exam's row the_names"})
        w.submit({'kind': 'speech_case', 'subject': 'the-temple-mountain', 'person': 'the-temple-mountain', 'cell': 'plea', 'ask': 'lebanon', 'case_source': "Gittin 56b:1 — the exam's row lebanon"})
        w.submit({'kind': 'speech_case', 'subject': 'the-urim', 'person': 'the-urim', 'cell': 'commission', 'ask': 'the_urim', 'case_source': "Yoma 73b:3 — the exam's row the_urim"})
        w.submit({'kind': 'speech_case', 'subject': 'the-honored', 'person': 'the-honored', 'cell': 'commission', 'ask': 'the_honor', 'case_source': "Bava Batra 75a:8 — the exam's row the_honor"})
    n = lambda eid, eff: len([e for e in w.entity(eid).ledger if e['effect'] == eff])
    tset = len([l for l in w.log if l[0] == 'TIMER-SET']); tfire = len([l for l in w.log if l[0] == 'TIMER-FIRE']); tcan = len([l for l in w.log if l[0] == 'TIMER-CANCEL'])
    closes = len([e for ent in w.entities.values() for e in ent.ledger if e.get('closed_by')])
    return (tuple(n(p, 'accepted') + n(p, 'exempt') + n(p, 'judgment_perverted') for _, p, _, _, _ in PERSONS), (n('the-perverter', 'judgment_perverted'), n('the-refuser-before-hearing', 'exempt'), n('the-excepted', 'exempt'), n('the-harasser-of-moab', 'exempt')), (tset, tfire, tcan, len(w.timers)), len(w.entities), closes), w
SCENE, _W = scene()
# THE PREDICTION (typed before the first run — the scratchpad's deu_scene_predict.py, run BEFORE this runner existed): every exam person written once;
# the perverter's judgment_perverted, the refuser's exempt, the excepted's exempt, Moab's harasser's exempt each ONE; no timer; ENTITIES the thirty-three persons; CLOSES 0.
SCENE_PREDICTED = ((1,) * 33, (1, 1, 1, 1), (0, 0, 0, 0), 33, 0)
assert SCENE == SCENE_PREDICTED, ('THE DEUTERONOMY WALK: the scene moved from its prediction', SCENE, SCENE_PREDICTED)


def narrative():
    """THE DEUTERONOMY WALK 1b (2026-09-15): the span's own acts AS HISTORY — the commission's four lines at the counter's day (40, 6, 1) after
    the daughters' four; the FORWARD marker at Deut 1:1 (40, 11, 1) and the frame's line; the RETROGRADE markers at 1:6 (2, 2, 20), 1:9 (the court's
    founding day) and 2:2 (40, 6, 1) with the eleven supplied lines dated by them — on a world with this runner's daemon: 20 writes (the sixteen
    lines' twenty effects — the four supplied debits written and closed by the daemon's own hand), no timer, EIGHT entities (Israel, Moses, the
    court, Edom, the Moabites, the sons of Ammon, the Amorite, Joshua), the counter at (11, 1), FIVE closes, no row. Recorded by the sequential run's
    recorder and stitched onto the tape (the markers the stitcher's rows). Not a graded cell: the tuple below is a tripwire typed from the design."""
    with contextlib.redirect_stdout(io.StringIO()):
        w = WE.World(era='Deut 1:1-3:29 with Num 27:12-23 on the tape — the commission, the frame, the acts told only in the retelling (the exodus epoch)', epoch='exodus')
        w.laws = [law_opening_speech]
        w.advance(w.clock.day_in('exodus', 40, 6, 1))
        # THE DAEMON GATE READS LITERAL SUBMITS ONLY — the sixteen lines typed out; no field named `until` or `due` (the stitcher re-bases those as scene-clock days)
        w.submit({'kind': 'moses_told_to_ascend_abarim', 'subject': 'moses', 'mountain': 'Abarim', 'land': 'the land given to the children of Israel', 'sentence': 'Meribah (20:12)', 'case_source': LINES[0][0]})
        w.submit({'kind': 'a_shepherd_asked', 'subject': 'moses', 'plea': 'a man over the congregation, that they be not as sheep without a shepherd', 'case_source': LINES[1][0]})
        w.submit({'kind': 'joshua_commission_commanded', 'subject': 'moses', 'successor': 'joshua', 'priest': 'eleazar', 'urim': 'the judgment of the Urim', 'case_source': LINES[2][0]})
        w.submit({'kind': 'joshua_commissioned', 'subject': 'joshua', 'hand': 'two hands laid for the one commanded', 'honor': 'some of Moses\' honor', 'receipt': 'as the LORD commanded him', 'case_source': LINES[3][0]})
        w.marker('Deut 1:1', w.clock.day_in('exodus', 40, 11, 1), value='the speech\'s date (1:3) — the number reader [40, 11, 1]; the FORWARD marker at the book\'s first verse')
        w.submit({'kind': 'speech_opened', 'subject': 'israel', 'places': 11, 'date': [40, 11, 1], 'after': 'Sihon and Og', 'case_source': LINES[4][0]})
        w.marker('Deut 1:6', w.clock.day_in('exodus', 2, 2, 20), value='the departure from Horeb told — dated at the march (10:11): RETROGRADE', placement='reading_placed')
        w.submit({'kind': 'horeb_departure_commanded', 'subject': 'israel', 'regions': 7, 'closed_by': 'Num 12:16', 'case_source': LINES[5][0]})
        w.marker('Deut 1:9', w.clock.day_in('exodus', 1, 2, 16), value='the judges charged — dated at the court\'s founding (Exodus 18:25-26): RETROGRADE', placement='reading_placed')
        w.submit({'kind': 'judges_charged', 'subject': 'the-court', 'clauses': 6, 'case_source': LINES[6][0]})
        w.marker('Deut 2:2', w.clock.day_in('exodus', 40, 6, 1), value='the bypass and the plea told — dated at the departure from Mount Hor (21:4): RETROGRADE', placement='reading_placed')
        w.submit({'kind': 'turn_northward_commanded', 'subject': 'israel', 'bar': 'edom', 'grant': 'mount_seir', 'purchase': 'food and water for money', 'closed_by': 'Num 21:10-13', 'case_source': LINES[7][0]})
        w.submit({'kind': 'moab_spared_commanded', 'subject': 'the-moabites', 'bar': 'battle', 'grant': 'ar', 'case_source': LINES[8][0]})
        w.submit({'kind': 'zered_crossing_commanded', 'subject': 'israel', 'closed_by': 'Num 21:10-13', 'case_source': LINES[9][0]})
        w.submit({'kind': 'ammon_spared_commanded', 'subject': 'the-sons-of-ammon', 'bar': 'harassing and battle', 'grant': 'the land of the sons of Ammon', 'case_source': LINES[10][0]})
        w.submit({'kind': 'sihon_war_commanded', 'subject': 'israel', 'dread': 'this day I will begin', 'closed_by': 'Num 21:24-25', 'case_source': LINES[11][0]})
        w.submit({'kind': 'sihons_cities_devoted', 'subject': 'the-amorite', 'cities': 'every city', 'spoil': 'the cattle and the spoil taken', 'case_source': LINES[12][0]})
        w.submit({'kind': 'ogs_cities_devoted', 'subject': 'the-amorite', 'cities': 60, 'spoil': 'the cattle and the spoil taken', 'case_source': LINES[13][0]})
        w.submit({'kind': 'joshua_encouraged', 'subject': 'joshua', 'seen': 'the two kings', 'promise': 'He fights for you', 'case_source': LINES[14][0]})
        w.submit({'kind': 'moses_besought', 'subject': 'moses', 'plea': 'let me go over and see the good land', 'answer': 'refused — let it suffice you', 'case_source': LINES[15][0]})
    writes = len([l for l in w.log if l[0] == 'WRITE'])
    closes = len([e for ent in w.entities.values() for e in ent.ledger if e.get('closed_by')])
    rows = len([l for l in w.log if l[0] == 'ROW'])
    dated = len([l for l in w.log if l[0] == 'EVENT' and l[2].get('dated') is not None])
    return (writes, len([l for l in w.log if l[0] == 'TIMER-SET']), len(w.entities), w.clock.eras['exodus'].date(w.clock.day)[1:], closes, rows, len(w.tables['population']), dated), w


NARRATIVE, _WN = narrative()
NARRATIVE_PREDICTED = (20, 0, 8, (11, 1), 5, 0, 0, 11)   # DEUTERONOMY_WALK.md "Sitting 1b": 20 writes (Num 27's four + the speech's sixteen — the daemon's watches summed), no timer, EIGHT entities, the counter's day (11, 1), FIVE closes (the commission's by its run; the four by a prior run), no row, ELEVEN dated lines (the retrograde stretches')
assert NARRATIVE == NARRATIVE_PREDICTED, ('THE DEUTERONOMY WALK: the opening speech\'s narrative moved from its prediction', NARRATIVE, NARRATIVE_PREDICTED)
_isr = _WN.entity('israel').ledger
assert [(e['value'], e.get('open'), str(e.get('closed_by', ''))[:12]) for e in _isr if e['effect'] == 'commanded'] == [('journey_to_the_mountain_of_the_amorite', False, 'Num 12:16 — '), ('turn_northward', False, 'Num 21:10-13'), ('cross_the_brook_zered', False, 'Num 21:10-13'), ('begin_to_possess_sihons_land', False, 'Num 21:24-25')], [(e['value'], e.get('open'), e.get('closed_by')) for e in _isr if e['effect'] == 'commanded']   # THE FOUR SUPPLIED DEBITS each CLOSED BY A PRIOR RUN, the closer's verse the tape's earlier line
assert [e['value'] for e in _WN.entity('moses').ledger if e['effect'] == 'commanded'] == ['see_the_land_from_abarim', 'commission_joshua_before_eleazar'] and [e.get('open') for e in _WN.entity('moses').ledger if e['effect'] == 'commanded'] == [True, False], _WN.entity('moses').ledger   # the ascent OPEN to Deuteronomy 34; the commission CLOSED by its run
assert [ex.date(l[2]['dated']) for l in _WN.log if l[0] == 'EVENT' and l[2].get('dated') is not None for ex in [_WN.clock.eras['exodus']]] == [(2, 2, 20), (1, 2, 16)] + [(40, 6, 1)] * 9, 'the eleven supplied lines dated by their markers'


# =====================================================================
# Motion 2 — THE TEST DATA: the answer sheet's rows (the docket's LAW rows and the cells' asks).
# =====================================================================
CASES = [
    # F0 — the_commission
    ('Num 27:12 — the_mountain', lambda: the_commission({'ask': 'the_mountain'}, DATA), "the mountain of Abarim (27:12) — Nebo and Pisgah its other names (34:1 one mountain): Deuteronomy 3:27's Pisgah the retelling of this command, READ BACK"),
    ('Num 27:14 — the_sentence_cited', lambda: the_commission({'ask': 'the_sentence_cited'}, DATA), "Meribah cited (27:14) — 20:12's sentence pointed to, the barred entry on Moses OPEN read (CK by CALL); no second write"),
    ('Num 27:15-17 — the_shepherd', lambda: the_commission({'ask': 'the_shepherd'}, DATA), "a shepherd asked (27:15-17) — plea_made on Moses: the successor asked before he is named; 16:22's phrase at its second seat"),
    ('Num 27:18, 23 — the_hand_laid', lambda: the_commission({'ask': 'the_hand_laid'}, DATA), "the hand laid (27:18, 23) — one hand commanded, two laid (the Sifrei 141): invested_office on Joshua, the ordination's form"),
    ('Num 27:20 — the_honor', lambda: the_commission({'ask': 'the_honor'}, DATA), 'of your honor (27:20) — not all of it: the sun and the moon (Bava Batra 75a:8) — DATA'),
    ('Num 27:21 — the_urim', lambda: the_commission({'ask': 'the_urim'}, DATA), "the judgment of the Urim (27:21) — final (C2 by CALL: Yoma 73b:3); Joshua under Eleazar's inquiry, not Moses' face to face"),
    ('Num 27:22-23 — the_receipt', lambda: the_commission({'ask': 'the_receipt'}, DATA), "the receipt (27:22-23) — 'as the LORD commanded him': the commission's debit closed by its run, the register seat Num 27:22 CLOSE"),
    ('Num 27:12-13 — the_debit', lambda: the_commission({'ask': 'the_debit'}, DATA), 'the debit (27:12) — see the land from Abarim: commanded on Moses, OPEN to Deuteronomy 34:1-4; 3:27 reads it back with Pisgah'),
    # F1 — the_frame
    ('Deut 1:1 — the_words', lambda: the_frame({'ask': 'the_words'}, DATA), "the words (1:1) — the eleven places the rebuke's sins (the Sifrei 1; Onkelos writes them in); Di-zahab the calf's gold (Berakhot 32a:7): the frame's DATA"),
    ('Deut 1:3 — the_date', lambda: the_frame({'ask': 'the_date'}, DATA), "the date (1:3) — [40, 11, 1] by the number reader; the era the exodus's by the taught verbal analogy with 33:38 (Rosh Hashanah 2b:11; JO by CALL): the FORWARD marker at Deut 1:1"),
    ('Deut 1:3 — the_receipt_of_the_rules', lambda: the_frame({'ask': 'the_receipt_of_the_rules'}, DATA), "the receipt of the rules (1:3) — 'according to all' the hermeneutic rules (the Sifrei 2:8): the register seat ACT, the frame the readback checkpoint reads"),
    ('Deut 1:2 — the_eleven_days', lambda: the_frame({'ask': 'the_eleven_days'}, DATA), "eleven days (1:2) — [11] by the parser; the journey hastened (the Sifrei 2:1-3): the rebuke's measure"),
    ('Deut 1:4 — after_sihon', lambda: the_frame({'ask': 'after_sihon'}, DATA), "after Sihon (1:4) — the order of the fortieth year: Aaron's death, Arad, the departure, Sihon, the speech (JO by CALL; Rosh Hashanah 2b:13)"),
    ('Deut 1:5 — began_to_expound', lambda: the_frame({'ask': 'began_to_expound'}, DATA), "began to expound (1:5) — the expound-root's two Torah seats (27:8's 'clearly' the other); the third teaching (Zevachim 115b:17); the king's reading (Sotah 7:8)"),
    ('Deut 1:1-5 — the_write', lambda: the_frame({'ask': 'the_write'}, DATA), "the write (1:1-5) — torah_expounded on Israel at (40, 11, 1): the book's one act of its own day"),
    # F2 — the_officers_and_the_judges
    ('Deut 1:6-8 — the_horeb_command', lambda: the_officers_and_the_judges({'ask': 'the_horeb_command'}, DATA), "the Horeb command (1:6-8) — told only here: commanded on Israel dated (2, 2, 20), CLOSED by the prior run Num 12:16 (the arrival in Paran); 'go in and possess' a reference to the land granted (Genesis 15:18)"),
    ('Deut 1:7 — the_regions', lambda: the_officers_and_the_judges({'ask': 'the_regions'}, DATA), "the regions (1:7) — the seven kinds every tribe's portion held (Bava Kamma 81b:6); the Euphrates great by nearness (Shevuot 47b:6); the promised extents by CALL: DATA"),
    ('Deut 1:9-12 — the_burden', lambda: the_officers_and_the_judges({'ask': 'the_burden'}, DATA), "the burden (1:9-12) — 11:14's 'I alone' retold; the seventy with Moses the seventy-one (BH by CALL; Sanhedrin 16b:18, 17a:3)"),
    ('Deut 1:11 — the_blessing', lambda: the_officers_and_the_judges({'ask': 'the_blessing'}, DATA), "the blessing (1:11) — [1000]: Moses' own beside God's (the Sifrei 11:1); a priest may not add it (Rosh Hashanah 28b:10): DATA"),
    ('Deut 1:13, 15 — the_qualities', lambda: the_officers_and_the_judges({'ask': 'the_qualities'}, DATA), "the qualities (1:13, 15) — seven asked, three found (the Sifrei 15:2): the discerning not found (Eruvin 100b:18); Jethro's four by CALL: a DATA checklist"),
    ('Deut 1:15 — the_grains', lambda: the_officers_and_the_judges({'ask': 'the_grains'}, DATA), "the grains (1:15) — [100, 50, 10] with the plural 'thousands' a noun: the four grains of Exodus 18:21 by CALL; the appointment read back, TURNED"),
    ('Deut the_count — the_count', lambda: the_officers_and_the_judges({'ask': 'the_count'}, DATA), "the count — 78,600 on the round six hundred thousand (ES by CALL; Sanhedrin 18a), 79,064 on the census's exact 603,550 by integer division (CB by CALL; the Sifrei 15:4's rounding rule): two settings"),
    ('Deut 1:15 — the_officers', lambda: the_officers_and_the_judges({'ask': 'the_officers'}, DATA), "the officers (1:15) — the strap (the Sifrei 15:5; 2 Chronicles 19:11); Deuteronomy 16:18's second seat — every tribe, every city (Sanhedrin 16b:9-10)"),
    ('Deut 1:16-17 — the_charge', lambda: the_officers_and_the_judges({'ask': 'the_charge'}, DATA), "the charge (1:16-17) — the six clauses each one seat: judges_charged on the court, dated at the court's founding (1, 2, 16); the law in Moses' voice, the vows' class"),
    ('Deut 1:16 — hear', lambda: the_officers_and_the_judges({'ask': 'hear'}, DATA), "hear (1:16) — not one litigant without the other (Sanhedrin 7b:14); 'charged' with alacrity, the rod and the strap"),
    ('Deut 1:16 — judge_righteously', lambda: the_officers_and_the_judges({'ask': 'judge_righteously'}, DATA), "judge righteously (1:16) — the true judgment truly makes the Presence rest (Sanhedrin 7a:17); Leviticus 19:15's 'in righteousness' by CALL"),
    ('Deut 1:17 — no_faces', lambda: the_officers_and_the_judges({'ask': 'no_faces'}, DATA), 'no faces (1:17) — befriend / estrange disputed (Sanhedrin 7b:18); the kin and the haters off the bench (Mishnah Sanhedrin 3:4-5; 29a:11): the DATA row no_faces'),
    ('Deut 1:17 — small_and_great', lambda: the_officers_and_the_judges({'ask': 'small_and_great'}, DATA), 'the small and the great (1:17) — the peruta as the hundred maneh (Sanhedrin 8a:2); the order of hearing (8a:4-5)'),
    ('Deut 1:17 — no_fear', lambda: the_officers_and_the_judges({'ask': 'no_fear'}, DATA), 'no fear (1:17) — a term for gathering in (Sanhedrin 7a:16); the refusal before hearing only (6b:12; the Sifrei 17:4); the student not silent (6b:13)'),
    ('Deut 1:17 — the_judgment_is_gods', lambda: the_officers_and_the_judges({'ask': 'the_judgment_is_gods'}, DATA), "the judgment is God's (1:17) — pierce the mountain (Sanhedrin 6b:3); the unlawful judge's life (7a:18); before Whom (6b:14)"),
    ('Deut 1:17 — the_hard_matter', lambda: the_officers_and_the_judges({'ask': 'the_hard_matter'}, DATA), "the hard matter (1:17) — Exodus 18:26's status read (ES by CALL); Zelophehad's daughters the case (the Sifrei 17:7; ZL by CALL — the third form)"),
    ('Deut 1:16 — the_stranger', lambda: the_officers_and_the_judges({'ask': 'the_stranger'}, DATA), 'the stranger (1:16) — a convert before a court (Yevamot 47a:7)'),
    ('Deut 1:16 — a_man_excludes_the_minor', lambda: the_officers_and_the_judges({'ask': 'a_man_excludes_the_minor'}, DATA), 'a man excludes the minor (1:16 — the Sifrei 16:6)'),
    ('Deut 1:16 — the_gentile_litigant', lambda: the_officers_and_the_judges({'ask': 'the_gentile_litigant'}, DATA), "the gentile litigant — R. Ishmael's two rulings against Rabban Shimon ben Gamliel's one (the Sifrei 16:4): DATA"),
    ('Deut 1:17 — the_appointer', lambda: the_officers_and_the_judges({'ask': 'the_appointer'}, DATA), 'the appointer (1:17) — the clause addressed to the one who appoints (the Sifrei 17:1): DATA'),
    ('Deut 1:17 — the_compromise', lambda: the_officers_and_the_judges({'ask': 'the_compromise'}, DATA), "the compromise — three settings on 1:17's clause (Sanhedrin 6b:1-15; 32b:4-6): TWO VERDICT TABLES as DATA"),
    ('Deut 1:13 — the_al_tikrei', lambda: the_officers_and_the_judges({'ask': 'the_al_tikrei'}, DATA), "the al tikrei (1:13) — 'I will set them' read 'their guilt on your heads' (the Sifrei 13:6): the revocalization move"),
    ('Deut be_deliberate — be_deliberate', lambda: the_officers_and_the_judges({'ask': 'be_deliberate'}, DATA), "be deliberate (Avot 1:1) — the Sifrei 16:1 cites the Mishnah as 1:16's reading; the chain by CALL"),
    ('Deut money_and_capital — money_and_capital', lambda: the_officers_and_the_judges({'ask': 'money_and_capital'}, DATA), "money and capital (Mishnah Sanhedrin 4:1) — the ten differences (Sanhedrin 32a; the Sifrei 18:1); the majority's asymmetry by CALL"),
    ('Deut the_court_of_three — the_court_of_three', lambda: the_officers_and_the_judges({'ask': 'the_court_of_three'}, DATA), "the court of three (Mishnah Sanhedrin 1:1, 3:1-3) — the litigants' choice, the third by the two (Sanhedrin 23a:12); the disqualified by conduct (24b-26b); the sizes by CALL"),
    ('Deut the_perverting_judge — the_perverting_judge', lambda: the_officers_and_the_judges({'ask': 'the_perverting_judge'}, DATA), 'the perverting judge — the five effects (HO by CALL; Sanhedrin 7a:17-18): judgment_perverted'),
    ('shelf: Sanhedrin 6b:12 (Reish Lakish); 6b:11 (R. Shimon ben Menasya — the_refusal_before_hearing', lambda: the_officers_and_the_judges({'ask': 'the_refusal_before_hearing'}, DATA), "the refusal before hearing — permitted, not yet bound by 'you shall not be afraid' (Sanhedrin 6b:12): exempt"),
    ('Deut 1:18 — all_the_things', lambda: the_officers_and_the_judges({'ask': 'all_the_things'}, DATA), 'all the things (1:18) — the community warned as the judges were (Sanhedrin 8a:6)'),
    # F3 — the_spies_read_back
    ('Deut 1:22 — the_asking', lambda: the_spies_read_back({'ask': 'the_asking'}, DATA), "the asking (1:22) — the people's, against 13:2's 'send for yourself' (Sotah 34b:3; SL by CALL): the two tellings reconciled on the shelf — the readback row TURNED"),
    ('Deut 1:23 — the_twelve', lambda: the_spies_read_back({'ask': 'the_twelve'}, DATA), "the twelve (1:23) — [12, 1]: one per tribe by CALL; Joshua 4:2 and 3:12 the phrases' other seats"),
    ('Deut 1:24 — the_valley', lambda: the_spies_read_back({'ask': 'the_valley'}, DATA), "the valley (1:24) — Eshcol named after the cluster (SL by CALL); 'spied' the piel — Caleb's verb (Joshua 14:7; CK.DATA spy_verb by CALL)"),
    ('Deut 1:25 — good_is_the_land', lambda: the_spies_read_back({'ask': 'good_is_the_land'}, DATA), "good is the land (1:25) — 14:7's words, Joshua and Caleb's (the Sifrei 23:3); the retelling keeps the truth, drops 13:27's 'however' (Sotah 35a:2): SHORTENED"),
    ('Deut 1:27-28 — the_murmuring', lambda: the_spies_read_back({'ask': 'the_murmuring'}, DATA), "the murmuring (1:27-28) — two words (Shevuot 47b:5); the spies' words in the people's mouths, 'greater and taller than we' the plain sense of 13:31 (Sotah 35a:7): TURNED"),
    ('Deut 1:31 — the_carrying', lambda: the_spies_read_back({'ask': 'the_carrying'}, DATA), "the carrying (1:31) — as a man carries his son: Exodus 19:4's eagle the kin"),
    ('Deut 1:33 — the_pillar', lambda: the_spies_read_back({'ask': 'the_pillar'}, DATA), "the pillar (1:33) — Exodus 13:21's by REFERENCE: the tape's pillar_set line, read"),
    ('Deut 1:34-36 — the_oath', lambda: the_spies_read_back({'ask': 'the_oath'}, DATA), "the oath (1:34-36) — the verb 'swore' supplied (GR.DATA by CALL); sentence_pronounced read; Caleb's holding_owed OPEN read (SL by CALL): SHORTENED"),
    ('Deut the_exceptions — the_exceptions', lambda: the_spies_read_back({'ask': 'the_exceptions'}, DATA), 'the exceptions — Caleb, Joshua, the children (SL by CALL): exempt from the oath'),
    ('Deut 1:37 — the_bars_ground', lambda: the_spies_read_back({'ask': 'the_bars_ground'}, DATA), "the bar's ground (1:37) — 'for your sakes' against 20:12's 'because you did not believe': DISAGREES, an OPEN row; the tape's one entry stands"),
    ('Deut 1:38 — joshua_shall_go_in', lambda: the_spies_read_back({'ask': 'joshua_shall_go_in'}, DATA), "Joshua shall go in (1:38) — 14:30's exception EXPANDED with the inheriting (the effect's first seat; 3:28 and Joshua 1:6 after)"),
    ('Deut 1:39 — the_little_ones', lambda: the_spies_read_back({'ask': 'the_little_ones'}, DATA), "the little ones (1:39) — 14:31 VERBATIM for five tokens, then the children who know not good and evil added (Eden's four seats)"),
    ('Deut 1:40 — the_turn_back', lambda: the_spies_read_back({'ask': 'the_turn_back'}, DATA), "the turn back (1:40) — 14:25 retold with 'tomorrow' dropped; the debit's close at 21:4 read (SL by CALL): TURNED"),
    ('Deut 1:41-44 — the_presumption', lambda: the_spies_read_back({'ask': 'the_presumption'}, DATA), "the presumption (1:41-44) — presumed_to_go_up and defeated read back; 'as bees do', 'in Seir' EXPANDED; the receipt in the people's mouth a run citation (1:41 NONE)"),
    ('Deut 1:45 — the_weeping', lambda: the_spies_read_back({'ask': 'the_weeping'}, DATA), "the weeping (1:45) — a second weeping told only here, unheard (1:45 and 3:26 one phrase); 14:1's wept read: EXPANDED, no write"),
    ('Deut 1:46 — many_days_at_kadesh', lambda: the_spies_read_back({'ask': 'many_days_at_kadesh'}, DATA), "many days at Kadesh (1:46) — Seder Olam 8's nineteen years: DATA, no day moved"),
    ('Deut the_readback_table — the_readback_table', lambda: the_spies_read_back({'ask': 'the_readback_table'}, DATA), "the readback table — forty-two reference rows graded; the two DISAGREES rows open; every retold act's entry found on the running world (CA4)"),
    # F4 — the_bypass
    ('Deut 2:1-3 — the_turn', lambda: the_bypass({'ask': 'the_turn'}, DATA), "the turn (2:1-3) — told only here: commanded on Israel dated (40, 6, 1), CLOSED by the prior run Num 21:10-13; 'enough' the plural's second seat in the speech"),
    ('Deut 2:4-8 — esau', lambda: the_bypass({'ask': 'esau'}, DATA), 'Esau (2:4-8) — contending_barred and land_granted (Mount Seir) on Edom: the bar and the grant told only here (Kiddushin 18a:2; JS by CALL); the purchase a permission'),
    ('Deut 2:7 — forty_years_lacking_nothing', lambda: the_bypass({'ask': 'forty_years_lacking_nothing'}, DATA), "forty years lacking nothing (2:7) — [40]: the manna's forty years (ES by CALL; Exodus 16:35)"),
    ('Deut 2:8 — the_route', lambda: the_bypass({'ask': 'the_route'}, DATA), "the route (2:8) — Elath and Ezion-geber, the way of Moab's wilderness: the itinerary's stations by CALL; 21:4's Red Sea way the same road"),
    ('Deut 2:9 — moab', lambda: the_bypass({'ask': 'moab'}, DATA), "Moab (2:9) — contending_barred and land_granted (Ar) on the Moabites: the bar the a fortiori needed (Bava Kamma 38a:16; BK by CALL); Lot's elder daughter's people (MM by CALL)"),
    ('shelf: Horayot 10b:19 (R. Yochanan); Nazir 23b:11 — harassing_permitted', lambda: the_bypass({'ask': 'harassing_permitted'}, DATA), "harassing Moab — permitted, battle forbidden (Horayot 10b:19): exempt from the bar's reach; Ammon's bar reaches further"),
    ('Deut 2:10-12 — the_emim', lambda: the_bypass({'ask': 'the_emim'}, DATA), "the Emim and the Horites (2:10-12) — Genesis 14:5-6's peoples (PR and JS by CALL); 'as Israel did' the ink's pattern of title: the dispossessions DATA"),
    ('Deut 2:13-14 — the_zered', lambda: the_bypass({'ask': 'the_zered'}, DATA), "the Zered (2:13-14) — told only here: commanded on Israel cross_the_brook_zered, CLOSED by the prior run Num 21:10-13; [38] against the tape's years (the spies' return to the departure from Mount Hor)"),
    ('Deut 2:14-16 — the_men_of_war_consumed', lambda: the_bypass({'ask': 'the_men_of_war_consumed'}, DATA), "the men of war consumed (2:14-16) — the decree's timer FIRED at (40, 5, 9) read; the dying ceased (40, 5, 15) by CALL (Taanit 30b:12)"),
    ('Deut 2:17 — the_speech_resumed', lambda: the_bypass({'ask': 'the_speech_resumed'}, DATA), "the speech resumed (2:17) — 'SPOKE to me' the Bible's one seat: only after the last of that generation (Bava Batra 121b:1)"),
    ('Deut 2:17-19 — ammon', lambda: the_bypass({'ask': 'ammon'}, DATA), "Ammon (2:17-19) — contending_barred and land_granted on the sons of Ammon: not even harassed (Bava Kamma 38b:6); 21:24's strong border the bar's reason (CK.DATA by CALL); the one new party"),
    ('Deut 2:20-23 — the_avvim', lambda: the_bypass({'ask': 'the_avvim'}, DATA), "the Avvim (2:20-23) — the Caphtorim's dispossession, Genesis 10:14's people (Chullin 60b:11): the dispossessions DATA"),
    ('Deut 2:24-25 — sihon_commanded', lambda: the_bypass({'ask': 'sihon_commanded'}, DATA), "Sihon commanded (2:24-25) — told only here: commanded on Israel, CLOSED by the prior run Num 21:24-25; the dread's row the sun for Moses (Avodah Zarah 25a; Taanit 20a): DATA"),
    # F5 — sihon_and_og
    ('Deut 2:26-28 — the_messengers', lambda: sihon_and_og({'ask': 'the_messengers'}, DATA), "the messengers (2:26-28) — nine tokens for 21:22's seventeen: SHORTENED; Kedemoth and 'words of peace' told only here"),
    ('Deut 2:29 — the_edom_disagreement', lambda: sihon_and_og({'ask': 'the_edom_disagreement'}, DATA), "the Edom disagreement (2:29) — 'as the sons of Esau did for me' against 20:18-21's refusal: DISAGREES, the chukat row's two arms (CK by CALL), an OPEN row"),
    ('Deut 2:30 — the_hardening', lambda: sihon_and_og({'ask': 'the_hardening'}, DATA), "the hardening (2:30) — told only here in Pharaoh's verbs (the exodus story by REFERENCE); sihon's refused read (CK by CALL): EXPANDED"),
    ('Deut 2:32-33 — jahaz', lambda: sihon_and_og({'ask': 'jahaz'}, DATA), "Jahaz (2:32-33) — eight tokens for 21:23's twenty: SHORTENED; 21:24's smiting the run"),
    ('Deut 2:33 — the_written_and_read', lambda: sihon_and_og({'ask': 'the_written_and_read'}, DATA), "written 'his son', read 'his sons' (2:33) — the DB's eleven tokens against the store's twelve; Onkelos plural: the reading's find, DATA"),
    ('Deut 2:34-35; 3:6-7 — the_ban', lambda: sihon_and_og({'ask': 'the_ban'}, DATA), "the ban (2:34-35; 3:6-7) — told only in the retelling: destroyed on the Amorite twice (21:24-25, 21:35 say smote and possessed); 15:16's status read; the cherem law forward"),
    ('Deut 2:36-37 — aroer_to_gilead', lambda: sihon_and_og({'ask': 'aroer_to_gilead'}, DATA), "Aroer to Gilead (2:36-37) — the border respected (2:37) against 21:24's strong (CK by CALL): EXPANDED"),
    ('Deut 3:1-3 — og_turned', lambda: sihon_and_og({'ask': 'og_turned'}, DATA), 'Og turned (3:1-3) — 21:33-35 with the persons shifted (we for they; to me for to Moses): TURNED, the five shifts computed; fear_not_promised on Moses read'),
    ('Deut 3:4-5 — the_sixty_cities', lambda: sihon_and_og({'ask': 'the_sixty_cities'}, DATA), "the sixty cities (3:4-5) — [60], Argob's; the walled cities from Joshua's days (Arakhin 32b:6; Megillah 10a:10); Leviticus 25:29's 'walled' learned here: DATA"),
    ('Deut 3:11 — ogs_bed', lambda: sihon_and_og({'ask': 'ogs_bed'}, DATA), "Og's bed (3:11) — [9, 4] by the cubit of a man (Kelim 17:9-10); the remnant of the Rephaim; Og's lore by CALL: DATA"),
    ('Deut 3:8-9 — hermon', lambda: sihon_and_og({'ask': 'hermon'}, DATA), "Hermon (3:8-9) — Sirion and Senir, the nations' names (Chullin 60b:14; Song 4:8): EXPANDED"),
    # F6 — the_east_and_the_charges
    ('Deut 3:12-13 — the_division', lambda: the_east_and_the_charges({'ask': 'the_division'}, DATA), "the division (3:12-13) — 32:33's three holdings read back, DIVIDED: half Gilead to the two, the rest and Bashan to the half tribe (thirty-six tokens for twenty-nine); the halves [1/2] by rule 30: EXPANDED"),
    ('Deut 3:14 — jair', lambda: the_east_and_the_charges({'ask': 'jair'}, DATA), "Jair (3:14) — 32:41 read back, EXPANDED (twenty-three tokens for eleven): Argob, the Geshurite and the Maacathite, 'to this day' told only here"),
    ('Deut 3:15 — machir', lambda: the_east_and_the_charges({'ask': 'machir'}, DATA), "Machir (3:15) — 32:40's 'Moses gave' in the first person: TURNED"),
    ('Deut 3:16-17 — the_borders', lambda: the_east_and_the_charges({'ask': 'the_borders'}, DATA), "the east's borders (3:16-17) — told only here: the Arnon's middle, the Jabbok, Chinnereth to the Salt Sea under Pisgah — DATA, no write"),
    ('Deut 3:18-20 — the_charge_to_the_tribes', lambda: the_east_and_the_charges({'ask': 'the_charge_to_the_tribes'}, DATA), "the charge to the tribes (3:18-20) — 32:20-24's condition in the first person with half Manasseh included: TURNED; the debit OPEN read (GR by CALL); 'until the LORD gives rest' Joshua 1:15's"),
    ('Deut 3:21-22 — joshuas_charge', lambda: the_east_and_the_charges({'ask': 'joshuas_charge'}, DATA), "Joshua's charge (3:21-22) — told only here: fear_not_promised on Joshua (21:34's effect at its second party); Joshua plene; Ai's run outside the Torah (the Sifrei 29:8-9)"),
    # F7 — the_plea
    ('Deut 3:23-26 — the_plea', lambda: the_plea({'ask': 'the_plea'}, DATA), 'the plea (3:23-26) — told only here: plea_made on Moses with the refusal in the value; the barred entry OPEN read; praise before the request (Berakhot 32a:32)'),
    ('Deut 3:24 — the_names', lambda: the_plea({'ask': 'the_names'}, DATA), "the names (3:24) — 'O Lord GOD' Abraham's and Moses'; 'Your greatness' the Sifrei 27:4's binyan av; 'Your strong hand' 1 Kings 8:42's: DATA"),
    ('Deut 3:25 — lebanon', lambda: the_plea({'ask': 'lebanon'}, DATA), "Lebanon (3:25) — the Temple (the Sifrei 6:2, 28:3; Gittin 56b:1); 1:7's Lebanon the region, this the house: DATA"),
    ('Deut 3:26 — the_refusal', lambda: the_plea({'ask': 'the_refusal'}, DATA), "the refusal (3:26) — 'let it suffice you' the singular's one seat, measure for measure for Korach's (Sotah 13b:13); 'did not hear' 1:45's phrase; the barred entry read"),
    ('Deut 3:27 — pisgah', lambda: the_plea({'ask': 'pisgah'}, DATA), "Pisgah (3:27) — 27:12's command read back with Pisgah for Abarim and the four directions in the third order: TURNED; the debit OPEN read"),
    ('Deut 3:28 — command_joshua', lambda: the_plea({'ask': 'command_joshua'}, DATA), "command Joshua (3:28) — the commission read back (Kiddushin 29a:14 — a galvanization for generations); 'he shall cause them to inherit' the effect's second seat: TURNED"),
    ('Deut 3:29 — beth_peor', lambda: the_plea({'ask': 'beth_peor'}, DATA), "Beth-peor (3:29) — the last camp by CALL (22:1; 36:13; Deuteronomy 34:1); 4:46 and 34:6 the valley's other seats: EXPANDED"),
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
    print('THE INK: integers %s; marked %s; the frames "said to me" %s, "spoke to me" %s; "at that time" %s; the case tokens %s' % (sorted(INTS.items()), MARKED, SAID_TO_ME, SPOKE_TO_ME, AT_THAT_TIME, CASE_KI))
    print('THE READBACK: %d rows — %s; the deltas: 1:39 prefix %d; 2:27 %d/%d; 2:32 %d/%d; 3:1-3 %d/%d shared %d shifts %d; 3:14 %d/%d; 3:12-13 %d/%d' % (len(READBACK), dict(RB_GRADES), VERBATIM_PREFIX, len(MSG_DEUT), len(MSG_NUM), len(JAHAZ_DEUT), len(JAHAZ_NUM), len(OG_D), len(OG_N), OG_SHARED, len(OG_SHIFT), len(JAIR_D), len(JAIR_N), len(DIV_D), len(DIV_N)))
    print('THE OFFICERS: the grains %s; the round %d; the exact %d of %d; the seven qualities asked %d found %d' % (DATA['the_officers_table']['value']['grains'], ES_JUDGES['v'], EXACT_COUNT, CENSUS_TOTAL, DATA['the_seven_qualities']['value']['asked'], DATA['the_seven_qualities']['value']['found']))
    print('THE SCENE on the bench: %s; the timers (set, fired, cancelled, pending) %s; entities %d; closes %d' % (SCENE[0], SCENE[2], SCENE[3], SCENE[4]))
    print('THE NARRATIVE: %s' % (NARRATIVE,))
    print('THE PARAMETER ROWS: ' + '; '.join('%s = %s' % (k, DATA[k]['value'] if k != 'the_readback' else '%d rows' % len(DATA[k]['value'])) for k in DATA) + ' (the other settings recorded in DATA)')
    if ok == len(CASES):
        print('\nTHE COMPILE OF THE OPENING SPEECH: the answer sheet REPRODUCED — %d/%d' % (ok, len(CASES)))
    sys.exit(0 if ok == len(CASES) else 1)
