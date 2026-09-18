
# ---- THE CALLEES' FACTS (every edge live at the cells that consume them; the values asserted from the callees' own prints — ch6_callees.out) ----
CH_NOG = CH.the_second_word({'ask': 'no_other_gods'}, CH.DATA); CH_VIS = CH.the_second_word({'ask': 'the_visiting'}, CH.DATA); CH_STAND = CH.the_answer_and_the_charge({'ask': 'stand_here_with_me'}, CH.DATA); CH_CHARGE = CH.the_answer_and_the_charge({'ask': 'the_charge'}, CH.DATA)
assert CH_NOG[1] == ['accepted'] and CH_NOG[0].startswith('no other gods before me (5:7)') and CH_VIS[1] == ['accepted'] and CH_STAND[1] == ['commanded'] and CH_CHARGE[1] == ['accepted'] and len(CH.READBACK) == 21 and dict(CH.RB_GRADES) == {'VERBATIM': 5, 'VARIANT': 5, 'EXPANDED': 5, 'TURNED': 4, 'SUPPLIED': 2}, (CH_NOG[:2], CH_STAND[1], len(CH.READBACK))
OH_TAKE = OH.horeb_retold({'ask': 'take_heed_lest_you_forget'}, OH.DATA); OH_FRAME = OH.the_cities_and_the_frame({'ask': 'the_second_frame'}, OH.DATA); OH_SEEK = OH.the_exile_case({'ask': 'seek_and_find'}, OH.DATA)
assert len(OH.FORGET) == 13 and 'Deut 6:12' in OH.FORGET and 'Deut 4:9' in OH.FORGET and OH_TAKE[1] == ['accepted'] and OH_FRAME[1] == ['accepted'] and OH_SEEK[0].startswith('seek and find (4:29)') and OH.DATA['the_creed']['value'] == ['Deut 4:35', 'Deut 4:39'] and len(OH.READBACK) == 11, (len(OH.FORGET), OH_TAKE[1], OH_SEEK[0][:30])
DC_VO = DC.vain_name({'ask': 'vain_oath'}, DC.DATA); DC_FF = DC.vain_name({'ask': 'false_future_oath'}, DC.DATA)
assert DC_VO[:2] == ('lashes', ['lashes']) and DC_FF[:2] == ('lashes', ['lashes']) and len(DC.CASES) == 13, (DC_VO[:2], DC_FF[:2])
ES_TEN = ES.trials('ten_list'); ES_SIX = ES.trials('count_by_exodus')
assert ES_TEN['v'] == ('two_at_the_sea', 'two_at_the_water', 'two_at_the_manna', 'two_at_the_quail', 'one_at_the_calf', 'one_at_paran') and ES_TEN['fx'] == ['tested_the_lord'] and ES_SIX['v'] == 6, (ES_TEN['v'], ES_SIX['v'])
PE_HUMAN = PE.firstborn({'kind': 'human'}, PE.DATA)
assert PE_HUMAN[0].startswith('redeem') and 'pays' in PE_HUMAN[1], PE_HUMAN[:2]
OS_WRITE = OS.the_frame({'ask': 'the_write'}, OS.DATA); OS_WORDS = OS.the_frame({'ask': 'the_words'}, OS.DATA)
assert OS_WRITE[1] == ['torah_expounded'] and OS_WORDS[1] == ['accepted'] and len(OS.READBACK) == 42, (OS_WRITE[1], OS_WORDS[1], len(OS.READBACK))
MA_TEST = MA.moriah('test_verb_seats'); MA_TEN = MA.moriah('ten_trials_sheet'); MA_FAM = MA.isaac_gerar('famine_ordinal')
assert MA_TEST['v'] == 1 and MA_TEST['fx'] == ['tried'] and MA_TEN['v'] == 10 and MA_FAM['v'] == 'the_second', (MA_TEST['v'], MA_TEN['v'], MA_FAM['v'])
JS_17 = JS.the_oath('seventeen_years'); JS_147 = JS.the_oath('hundred_forty_seven'); JS_KT = JS.the_oath('kindness_and_truth')
assert JS_17['v'] == 17 and JS_147['v'] == 147 and JS_KT['v'] == 'kindness_and_truth', (JS_17['v'], JS_147['v'], JS_KT['v'])
MK_CASE = MK.the_gatherer({'ask': 'the_case'}, MK.DATA)
assert MK_CASE[1] == ['warned_specifying_the_labor', 'put_to_death', 'in_custody', 'stoned'], MK_CASE[1]
ER_TORAH = ER.ascent('torah_mitzvah'); ER_BOOK = ER.blood_covenant('book_of_covenant')
assert ER_TORAH['v'] == 2 and ER_BOOK['v'] == 4 and ER_BOOK['fx'] == ['oral_law_unwritten'], (ER_TORAH['v'], ER_BOOK['v'], ER_BOOK['fx'])


# ===== THE WRAP (D9-iv): the daemon over the cells — the ledger written, no event emitted =====================
def law_hear_o_israel(event, world):
    """Deut 6:1-25 (cold_run_hear_o_israel.py F1-F6). given_at Deut 6:4 — THE SHEMA'S FIRST AND ONLY GIVING, the chapter's own line on the counter's
    day (40, 11, 1), NO marker; installed_by boot (the two Deuteronomy daemons' form). TWO TAPE LINES of its own: shema_declared (6:4-9 — the creed and
    the four duties: shema_commanded a STATUS on Israel) and testing_barred (6:16-19 — Massah the tape's named line, a run citation by name:
    test_barred a BLOCK on Israel). The exam's case kind dispatches to the cells in EXPLICIT branches with LITERAL effects per kind (an unnamed effect
    is a KeyError). No timer; no close; the second word's block and the charge's debit UNMOVED (CO5, CO7)."""
    k, src = event['kind'], event['case_source']
    E_ = lambda eff, s, cp=None, amount=None, due=None, law='', value=None: {'effect': eff, 'subject': s, 'counterparty': cp, 'amount': amount, 'due': due, 'value': value if value is not None else True, 'source_law': law, 'case_source': src}
    if k == 'shema_declared':
        return [E_('shema_commanded', 'israel', value={'creed': 'hear, O Israel: the LORD our God, the LORD is one (6:4)', 'love': 'with all your heart, with all your soul, with all your might (6:5)', 'duties': ['the recitation — when you lie down and when you rise up (6:7)', 'the teaching — to your sons (6:7)', 'the tefillin — a sign upon your hand, frontlets between your eyes (6:8)', 'the mezuzah — the doorposts of your house and your gates (6:9)'], 'compartments': {'hand': 1, 'head': 4, 'kind': 'PARAMETER (the Sifrei 35:3-4; Menachot 34b-35a; Sanhedrin 4b:12-14) — the open row the_spellings'}, 'day': 'the counter\'s (40, 11, 1), no marker'}, law="F3 [INK 6:4-9 'hear, O Israel … and you shall write them upon the doorposts of your house and upon your gates' — THE FOUR DUTIES compiled at THE DEUTERONOMY WALK 4b from the ink with the answer sheet Mishnah Berakhot 1:1-3:6, 2:2, 9:5, Menachot 3:7, Sotah 7:1 (no cell in any runner before): a STATUS on Israel at the chapter's own line; the compartments a parameter, the derivation from the spellings the open row (11:18 plene in the ink); the third passage in mekoshesh's span by REFERENCE]")]
    if k == 'testing_barred':
        return [E_('test_barred', 'israel', value={'the_word': 'you shall not test the LORD your God, as you tested him at Massah (6:16)', 'massah': "the tape's named line — Exodus 17:7 'Massah and Meribah' (murmured 17:2-3, rock_struck 17:6)", 'the_trials': 'ten (Arakhin 15a — two at the water: Marah, Rephidim)', 'with_it': "surely keep (6:17); the right and the good — the abutter (6:18, Bava Metzia 108a); thrust out (6:19, 9:4 forward)"}, law="F5 [INK 6:16-19 'you shall not test the LORD your God, as you tested him at Massah' — a BLOCK on Israel at the chapter's second line; Massah A RUN CITATION BY NAME (the tape's Exodus 17:7 line FOUND by kind and first verse — CO3; ES.trials by CALL); 'surely keep' the infinitive absolute, the testimonies' three seats; 'the right and the good' Bava Metzia 108a's abutter]")]
    if k == 'shema_case':
        fn = {'header': the_header, 'creed': the_creed, 'duties': the_four_duties, 'gift': the_gift_and_the_warning, 'test': the_test_and_the_right, 'son': the_sons_question}[event['cell']]
        v, e, _ = fn({'ask': event['ask']}, DATA); L = '%s [%s]' % ({'header': 'F1', 'creed': 'F2', 'duties': 'F3', 'gift': 'F4', 'test': 'F5', 'son': 'F6'}[event['cell']], event['ask']); s_ = event['person']
        W = {'accepted': E_('accepted', s_, value=v, law=L), 'exempt': E_('exempt', s_, value=v, law=L)}
        return [W[x] for x in e if x != FX.NONE]
    return []


LINES = [
    ('Deut 6:4-9 — hear, O Israel: the LORD our God, the LORD is one; and you shall love the LORD your God with all your heart and with all your soul and with all your might; and these words which I command you this day shall be upon your heart; and you shall teach them diligently to your sons and speak of them when you sit in your house and when you walk by the way and when you lie down and when you rise up; and you shall bind them for a sign upon your hand and they shall be for frontlets between your eyes; and you shall write them upon the doorposts of your house and upon your gates',),
    ('Deut 6:16-19 — you shall not test the LORD your God, as you tested him at Massah; you shall surely keep the commandments of the LORD your God and his testimonies and his statutes which he commanded you; and you shall do the right and the good in the eyes of the LORD, that it may be well with you and that you may go in and possess the good land which the LORD swore to your fathers, to thrust out all your enemies from before you, as the LORD has spoken',),
]
CLOSES = "none — no close this chapter: the charge to teach (commanded on Moses) stays CLOSED by the prior run (6:1 a reference row); the second word's block stands (6:14 no second write); the refuge debit OPEN; the header, the gift and the answer no write"

PERSONS = [
    ('the-priest-entering-to-eat-terumah', 'duties', 'recite_when', "Mishnah Berakhot 1:1; Berakhot 2a-2b — the exam's row recite_when"),
    ('the-reader-by-the-road', 'duties', 'recite_how', "Mishnah Berakhot 1:3; Berakhot 10b-11a — the exam's row recite_how"),
    ('the-bridegroom', 'duties', 'recite_who', "Mishnah Berakhot 2:5; Berakhot 16a — the exam's row recite_who"),
    ('the-daughter', 'duties', 'daughters_exempt', "Kiddushin 29b; 34a:3 — the exam's row daughters_exempt"),
    ('the-four-compartment-maker', 'duties', 'tefillin_compartments', "the Sifrei 35:3-4; Menachot 34b-35a; Sanhedrin 4b:12-14 — the exam's row tefillin_compartments"),
    ('the-left-handed', 'duties', 'tefillin_arm', "the Sifrei 35:5-10; Menachot 36b-37a — the exam's row tefillin_arm"),
    ('the-scroll-writer', 'duties', 'mezuzah_writing', "the Sifrei 36:1-2; Menachot 34a:11; Shabbat 103b — the exam's row mezuzah_writing"),
    ('the-bathhouse-owner', 'duties', 'mezuzah_gates', "the Sifrei 36:6-8; Yoma 11a — the exam's row mezuzah_gates"),
    ('the-true-swearer', 'gift', 'fear_serve_swear', "Temurah 3b:17-4a:2; Shevuot 35a — the exam's row fear_serve_swear"),
    ('the-idolaters-companion', 'gift', 'no_other_gods', "Tosefta Avodah Zarah 1:3 — the exam's row no_other_gods"),
    ('the-tester-at-massah', 'test', 'you_shall_not_test', "Exodus 17:2-7; Arakhin 15a — the exam's row you_shall_not_test"),
    ('the-abutters-buyer', 'test', 'the_right_and_the_good', "Bava Metzia 108a:1-4 — the exam's row the_right_and_the_good"),
    ('the-wise-son', 'son', 'the_four_askings', "Pesachim 116a-b; Mishnah Pesachim 10:4 — the exam's row the_four_askings"),
    ('the-son-who-asks-tomorrow', 'son', 'the_answer_rows', "Deut 6:20-25; THE_LOOP.md step 6 (T1) — the exam's row the_answer_rows"),
]


def scene():
    """THE SCENE — the exam's rows replayed on the world engine (the exodus epoch): the exam's persons through shema_case — the priest at evening,
    the reader by the road, the bridegroom and the daughter (exempt), the compartments, the left-handed, the scroll, the bathhouse (exempt), the true
    swearer, the idolaters' companion, the tester, the abutter's buyer, the wise son, the son who asks tomorrow."""
    with contextlib.redirect_stdout(io.StringIO()):
        w = WE.World(era='Deut 6:1-25: chapter 6 on the shelf — Berakhot, Menachot, Kiddushin, Sanhedrin, Temurah, Bava Metzia, Pesachim, Yoma on the engine (the exodus epoch)', epoch='exodus')
        w.laws = [law_hear_o_israel]
        w.advance(w.clock.day_in('exodus', 40, 11, 1))
        # THE DAEMON GATE READS LITERAL SUBMITS ONLY — the fourteen persons typed out from PERSONS
        w.submit({'kind': 'shema_case', 'subject': 'the-priest-entering-to-eat-terumah', 'person': 'the-priest-entering-to-eat-terumah', 'cell': 'duties', 'ask': 'recite_when', 'case_source': "Mishnah Berakhot 1:1; Berakhot 2a-2b — the exam's row recite_when"})
        w.submit({'kind': 'shema_case', 'subject': 'the-reader-by-the-road', 'person': 'the-reader-by-the-road', 'cell': 'duties', 'ask': 'recite_how', 'case_source': "Mishnah Berakhot 1:3; Berakhot 10b-11a — the exam's row recite_how"})
        w.submit({'kind': 'shema_case', 'subject': 'the-bridegroom', 'person': 'the-bridegroom', 'cell': 'duties', 'ask': 'recite_who', 'case_source': "Mishnah Berakhot 2:5; Berakhot 16a — the exam's row recite_who"})
        w.submit({'kind': 'shema_case', 'subject': 'the-daughter', 'person': 'the-daughter', 'cell': 'duties', 'ask': 'daughters_exempt', 'case_source': "Kiddushin 29b; 34a:3 — the exam's row daughters_exempt"})
        w.submit({'kind': 'shema_case', 'subject': 'the-four-compartment-maker', 'person': 'the-four-compartment-maker', 'cell': 'duties', 'ask': 'tefillin_compartments', 'case_source': "the Sifrei 35:3-4; Menachot 34b-35a; Sanhedrin 4b:12-14 — the exam's row tefillin_compartments"})
        w.submit({'kind': 'shema_case', 'subject': 'the-left-handed', 'person': 'the-left-handed', 'cell': 'duties', 'ask': 'tefillin_arm', 'case_source': "the Sifrei 35:5-10; Menachot 36b-37a — the exam's row tefillin_arm"})
        w.submit({'kind': 'shema_case', 'subject': 'the-scroll-writer', 'person': 'the-scroll-writer', 'cell': 'duties', 'ask': 'mezuzah_writing', 'case_source': "the Sifrei 36:1-2; Menachot 34a:11; Shabbat 103b — the exam's row mezuzah_writing"})
        w.submit({'kind': 'shema_case', 'subject': 'the-bathhouse-owner', 'person': 'the-bathhouse-owner', 'cell': 'duties', 'ask': 'mezuzah_gates', 'case_source': "the Sifrei 36:6-8; Yoma 11a — the exam's row mezuzah_gates"})
        w.submit({'kind': 'shema_case', 'subject': 'the-true-swearer', 'person': 'the-true-swearer', 'cell': 'gift', 'ask': 'fear_serve_swear', 'case_source': "Temurah 3b:17-4a:2; Shevuot 35a — the exam's row fear_serve_swear"})
        w.submit({'kind': 'shema_case', 'subject': 'the-idolaters-companion', 'person': 'the-idolaters-companion', 'cell': 'gift', 'ask': 'no_other_gods', 'case_source': "Tosefta Avodah Zarah 1:3 — the exam's row no_other_gods"})
        w.submit({'kind': 'shema_case', 'subject': 'the-tester-at-massah', 'person': 'the-tester-at-massah', 'cell': 'test', 'ask': 'you_shall_not_test', 'case_source': "Exodus 17:2-7; Arakhin 15a — the exam's row you_shall_not_test"})
        w.submit({'kind': 'shema_case', 'subject': 'the-abutters-buyer', 'person': 'the-abutters-buyer', 'cell': 'test', 'ask': 'the_right_and_the_good', 'case_source': "Bava Metzia 108a:1-4 — the exam's row the_right_and_the_good"})
        w.submit({'kind': 'shema_case', 'subject': 'the-wise-son', 'person': 'the-wise-son', 'cell': 'son', 'ask': 'the_four_askings', 'case_source': "Pesachim 116a-b; Mishnah Pesachim 10:4 — the exam's row the_four_askings"})
        w.submit({'kind': 'shema_case', 'subject': 'the-son-who-asks-tomorrow', 'person': 'the-son-who-asks-tomorrow', 'cell': 'son', 'ask': 'the_answer_rows', 'case_source': "Deut 6:20-25; THE_LOOP.md step 6 (T1) — the exam's row the_answer_rows"})
    n = lambda eid, eff: len([e for e in w.entity(eid).ledger if e['effect'] == eff])
    tset = len([l for l in w.log if l[0] == 'TIMER-SET']); tfire = len([l for l in w.log if l[0] == 'TIMER-FIRE']); tcan = len([l for l in w.log if l[0] == 'TIMER-CANCEL'])
    closes = len([e for ent in w.entities.values() for e in ent.ledger if e.get('closed_by')])
    return (tuple(n(p, 'accepted') + n(p, 'exempt') for p, _, _, _ in PERSONS), (n('the-bridegroom', 'exempt'), n('the-daughter', 'exempt'), n('the-bathhouse-owner', 'exempt')), (tset, tfire, tcan, len(w.timers)), len(w.entities), closes), w
SCENE, _W = scene()
# THE PREDICTION (typed before the first run — the design's arithmetic): every exam person written once; the three exempt arms ONE each; no timer;
# ENTITIES the fourteen persons; CLOSES 0.
SCENE_PREDICTED = ((1,) * 14, (1, 1, 1), (0, 0, 0, 0), 14, 0)
assert SCENE == SCENE_PREDICTED, ('THE DEUTERONOMY WALK 4b: the scene moved from its prediction', SCENE, SCENE_PREDICTED)


def narrative():
    """THE DEUTERONOMY WALK 4b (2026-09-17): the chapter's own acts AS HISTORY — the two lines on the counter's own day (40, 11, 1), NO marker (the
    retrograde stretch of 5:23 ended at 5:32's forward marker) — on a world with this runner's daemon: 2 writes (shema_commanded, test_barred), no
    timer, ONE entity (Israel), the counter at (11, 1), no close, no row, no dated line. Recorded by the sequential run's recorder and stitched onto
    the tape (page_order after the last Deuteronomy 5 line). Not a graded cell: the tuple below is a tripwire typed from the design."""
    with contextlib.redirect_stdout(io.StringIO()):
        w = WE.World(era='Deut 6:1-25 on the tape — the Shema declared and the test barred, the counter\'s own day (the exodus epoch)', epoch='exodus')
        w.laws = [law_hear_o_israel]
        w.advance(w.clock.day_in('exodus', 40, 11, 1))
        # THE DAEMON GATE READS LITERAL SUBMITS ONLY — the two lines typed out; no marker; no field named `until`, `days` or `due`
        w.submit({'kind': 'shema_declared', 'subject': 'israel', 'creed': 'hear, O Israel: the LORD our God, the LORD is one (6:4)', 'duties': ['recite', 'teach', 'bind', 'write'], 'case_source': LINES[0][0]})
        w.submit({'kind': 'testing_barred', 'subject': 'israel', 'first_telling': 'Exod 17:2-7', 'massah': 'as you tested at Massah (6:16) — the tape\'s named line Exod 17:7', 'case_source': LINES[1][0]})
    writes = len([l for l in w.log if l[0] == 'WRITE'])
    closes = len([e for ent in w.entities.values() for e in ent.ledger if e.get('closed_by')])
    rows = len([l for l in w.log if l[0] == 'ROW'])
    dated = len([l for l in w.log if l[0] == 'EVENT' and l[2].get('dated') is not None])
    return (writes, len([l for l in w.log if l[0] == 'TIMER-SET']), len(w.entities), w.clock.eras['exodus'].date(w.clock.day)[1:], closes, rows, len(w.tables['population']), dated), w


NARRATIVE, _WN = narrative()
NARRATIVE_PREDICTED = (2, 0, 1, (11, 1), 0, 0, 0, 0)   # DEUTERONOMY_WALK.md "Sitting 4b": 2 writes, no timer, ONE entity, the counter's day (11, 1), no close, no row, no population row, no dated line
assert NARRATIVE == NARRATIVE_PREDICTED, ('THE DEUTERONOMY WALK 4b: the chapter\'s narrative moved from its prediction', NARRATIVE, NARRATIVE_PREDICTED)
_isr = _WN.entity('israel').ledger
assert [e['effect'] for e in _isr] == ['shema_commanded', 'test_barred'] and _isr[0]['value']['compartments']['head'] == 4 and not any(e.get('closed_by') for e in _isr), [e['effect'] for e in _isr]
