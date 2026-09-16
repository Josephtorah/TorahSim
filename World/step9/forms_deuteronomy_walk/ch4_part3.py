
# ---- THE CALLEES' FACTS (every edge live at the cells that consume them; the values asserted from the callees' own prints) ----
BK_PLAGUE = BK.peor({'ask': 'plague_count'}, BK.DATA); BK_SERVICE = BK.peor({'ask': 'peor_service'}, BK.DATA); BK_LAST = BK.the_call({'ask': 'last_camp'}, BK.DATA)
RF_SIX = RF.the_refuge_law({'ask': 'six_cities'}, RF.DATA); RF_DEBIT = RF.the_refuge_law({'ask': 'the_debit'}, RF.DATA); RF_ENEMY = RF.the_manslayer({'ask': 'not_his_enemy'}, RF.DATA); RF_BLIND = RF.the_manslayer({'ask': 'without_seeing'}, RF.DATA)
OS_BAR = OS.the_spies_read_back({'ask': 'the_bars_ground'}, OS.DATA); OS_REFUSAL = OS.the_plea({'ask': 'the_refusal'}, OS.DATA); OS_HERMON = OS.sihon_and_og({'ask': 'hermon'}, OS.DATA); OS_AFTER = OS.the_frame({'ask': 'after_sihon'}, OS.DATA); OS_ROWS = OS.READBACK
ER_TEN = ER.tablets('ten_words'); ER_TAMMUZ = ER.ascent('seventeenth_tammuz'); ER_FORMS = ER.tablets('finger_and_forms'); ER_TORAH_MITZVAH = ER.ascent('torah_mitzvah'); ER_HOREB = ER.presence('horev_plene')
ES_DAYS = ES.sinai('days_r_yose'); ES_DESC = ES.sinai('descents'); ES_TEN = ES.plagues('ten'); ES_SEA = ES.sea('ten_at_sea'); ES_SENT = ES.night('sent_formula')
TC_RECOVERY = TC.recovery(True, True); TC_NOT_BROKEN = TC.NOT_BROKEN
PS_CREATED = PS.creation('created_made')
PR_FURNACE = PR.pieces('furnace'); PR_LAND = PR.call('land_seats')
DC_STEPS = DC.altar_rules({'ask': 'steps'}, DC.DATA)
CK_DELTA = CK.well_and_kings({'ask': 'deut3_delta'}, CK.DATA)
BO_EXTENTS = BO.the_four_sides({'ask': 'the_promised_extents'}, BO.DATA)
assert ER_TEN['v'] == 3 and ER_TAMMUZ['v'] == '17_tammuz' and ER_HOREB['v'] == 1 and ER_TORAH_MITZVAH['v'] == 2 and ER_FORMS['v']['לוחת'] == 3 and ER_FORMS['v']['לחת'] == 12, (ER_TEN['v'], ER_TAMMUZ['v'], ER_HOREB['v'], ER_TORAH_MITZVAH['v'], ER_FORMS['v'])   # 'the ten words' three seats; the seventeenth of Tammuz; Horeb plene once; 24:12's pair; the tablets' forms
assert ES_DAYS['v'] == (2, 3, 4, 7) and ES_DESC['v'] == 'one_of_ten' and ES_TEN['v'] == 10 and ES_SEA['v'] == 10 and ES_SENT['v'] == 'the_mouth_that_said_i_will_not_send', (ES_DAYS['v'], ES_DESC['v'], ES_TEN['v'], ES_SEA['v'], ES_SENT['v'])   # Rabbi Yose's days — the giving on the seventh; the ten plagues, the ten at the sea
assert PS_CREATED['v'] == (6, 10) and PR_FURNACE['v'] == ('michael', 'the_holy_one_himself') and TC_RECOVERY['v'] == 'covenant_remembered' and TC_NOT_BROKEN['v'] == 'never_broken' and len(OS_ROWS) == 42, (PS_CREATED['v'], PR_FURNACE['v'], TC_RECOVERY['v'], TC_NOT_BROKEN['v'], len(OS_ROWS))
assert RF_SIX[0].startswith('six cities (35:13-15)') and RF_DEBIT[0].startswith('the debit (35:11-14)') and OS_BAR[0].startswith("the bar's ground (1:37)") and DC_STEPS[0].startswith('a ramp') and RF.DATA['the_six_cities']['value']['beyond_the_jordan'] == ['Bezer (Reuben)', 'Ramoth in Gilead (Gad)', 'Golan in Bashan (Manasseh)'], (RF_SIX[0][:60], RF_DEBIT[0][:60], OS_BAR[0][:60], DC_STEPS[0][:40])
assert [r['verses'] for r in OS_ROWS if r['grade'] == 'DISAGREES'] == ['Deut 1:37', 'Deut 2:29'], 'the 1b DISAGREES rows this chapter\'s 4:21-22 joins'


# ===== THE WRAP (D9-iv): the daemon over the cells — the ledger written, no event emitted =====================
def law_obey_horeb(event, world):
    """Deut 4:1-49 (cold_run_obey_horeb.py F1-F6). given_at Deut 4:2; installed_by boot — A LAW IN MOSES' VOICE WITH NO DIVINE FRAME ('the word
    which I command you', 4:2 — the vows' class; the second pass's D2 question). FIVE TAPE LINES: the exhortation with the one law (a BLOCK on
    Israel — adding_barred; the receipt 4:5 in the line's source), the two SUPPLIED Horeb lines (the tape's hole — covenant_declared on Israel dated
    (1, 3, 7); tablets_delivered on Moses dated (1, 4, 17)), the witnesses called (a STATUS on Israel — the one case's evidence), the three cities set
    apart (a STATUS on Israel — the refuge debit READ OPEN, not closed). The exam's case kind dispatches to the cells in EXPLICIT branches with
    LITERAL effects per kind (an unnamed effect is a KeyError). No close, no timer."""
    k, src = event['kind'], event['case_source']
    E_ = lambda eff, s, cp=None, amount=None, due=None, law='', value=None: {'effect': eff, 'subject': s, 'counterparty': cp, 'amount': amount, 'due': due, 'value': value if value is not None else True, 'source_law': law, 'case_source': src}
    if k == 'add_nothing_commanded':
        return [E_('adding_barred', 'israel', value='you shall not add to the word which I command you, nor diminish from it (4:2) — in its time without intent, out of its time with intent (Rosh Hashanah 28b:24); an addition that spoils (Sanhedrin 89a:2); 13:1 the second seat', law='F1 [INK 4:2 "you shall not add to the word which I command you, nor diminish from it" — THE CHAPTER\'S ONE LAW: a BLOCK on Israel; the line 4:1-8 holds the receipt "as the LORD my God commanded me" (4:5) — the register seat ACT, the teaching\'s run of Exodus 24:12\'s command (ER by CALL); the exam\'s rows Rosh Hashanah 28b, Eruvin 95b-96a, Sanhedrin 88b-89a]')]
    if k == 'ten_words_declared':
        return [E_('covenant_declared', 'israel', value={'the_ten_words': 'his covenant which he commanded you to do, the ten words (4:13) — Exodus 20:1-17 the first telling', 'dated': (1, 3, 7), 'the_hole': 'no line on the tape for Exodus 20:1 until this one (the readback\'s finding)'}, law='F2 [INK 4:12-13 "the LORD spoke to you from the midst of the fire: a voice of words you heard, but no form … and he declared to you his covenant, the ten words" — TOLD HERE with no line on the tape (Exodus 20:1 the first telling; the tape runs from 19:20 to 24:1): written ONCE at its own time, dated (1, 3, 7) by the retrograde marker at 4:10 — the giving\'s day by Rabbi Yose (ES.sinai by CALL); the ten words three seats (ER by CALL)]')]
    if k == 'tablets_given':
        return [E_('tablets_delivered', 'moses', value='two tablets of stone written with the finger of God (Exodus 31:18; Deuteronomy 4:13 — the tablets plene) — given at the fortieth day of the ascent and broken the same day (Taanit 28b:9)', law='F2 [INK 4:13 "and he wrote them on two tablets of stone" — Exodus 31:18\'s giving TOLD HERE with no line on the tape (the erection runner folded the tablets into the ascent\'s line): written ONCE at its own time, dated (1, 4, 17) by the retrograde marker at 4:13 — the seventh of Sivan plus forty (ER.ascent by CALL); the erection\'s effect at its first tape seat]')]
    if k == 'witnesses_called':
        return [E_('heaven_and_earth_witness', 'israel', value='I call heaven and earth to witness against you this day (4:26) — the exile case\'s witnesses: corrupt → perish, scatter, few, serve wood and stone; seek → find; return → mercy; the end of days a prophecy, no timer', law='F4 [INK 4:25-31 "when you beget sons … I call heaven and earth to witness against you this day" — THE CHAPTER\'S ONE CASE: a STATUS on Israel, the Sifrei 306:1\'s chain (the third of eleven; 30:19, 31:28 forward); the arms DATA — Leviticus 26:33 and 26:42 the first tellings (TC by CALL), no exile written; Gittin 88a the exile hastened]')]
    if k == 'three_cities_set_apart':
        return [E_('cities_set_apart', 'israel', value=['Bezer (Reuben)', 'Ramoth in Gilead (Gad)', 'Golan in Bashan (Manasseh)'], law='F6 [INK 4:41-43 "then Moses set apart three cities beyond the Jordan toward the sunrise … Bezer … Ramoth … Golan" — Moses\' own ACT in the third person: a STATUS on Israel valued the three (RF.DATA the_six_cities by CALL); THE REFUGE DEBIT appoint_six_cities_of_refuge READ OPEN AND NOT CLOSED — Mishnah Makkot 2:4: the three east admitted no one until Joshua\'s three, "six cities of refuge shall they be" (35:13); Makkot 10a:15-16 R. Simlai; Joshua 20:7-8 the close outside the Torah]')]
    if k == 'horeb_case':
        fn = {'exhortation': the_exhortation, 'horeb': horeb_retold, 'image': no_image, 'exile': the_exile_case, 'god': the_one_god, 'cities': the_cities_and_the_frame}[event['cell']]
        v, e, _ = fn({'ask': event['ask']}, DATA); L = '%s [%s]' % ({'exhortation': 'F1', 'horeb': 'F2', 'image': 'F3', 'exile': 'F4', 'god': 'F5', 'cities': 'F6'}[event['cell']], event['ask']); s_ = event['person']
        W = {'accepted': E_('accepted', s_, value=v, law=L), 'exempt': E_('exempt', s_, value=v, law=L)}
        return [W[x] for x in e if x != FX.NONE]
    return []


LINES = [
    ('Deut 4:1-8 — and now, Israel, hear the statutes and the judgments which I teach you, to do them, that you may live and go in and possess the land which the LORD, the God of your fathers, gives you; you shall not add to the word which I command you, nor diminish from it, to keep the commandments of the LORD your God which I command you; your eyes have seen what the LORD did at Baal-peor, for every man who followed Baal-peor the LORD your God destroyed from your midst; but you who cleave to the LORD your God are alive, all of you, this day; behold, I have taught you statutes and judgments, as the LORD my God commanded me, to do so in the midst of the land which you go in to possess; keep them and do them, for this is your wisdom and your understanding in the eyes of the peoples, who will hear all these statutes and say: surely this great nation is a wise and understanding people; for what great nation has God so near to it as the LORD our God is whenever we call upon him; and what great nation has statutes and judgments so righteous as all this Torah which I set before you this day',),
    ('Deut 4:10-13 — the day you stood before the LORD your God at Horeb, when the LORD said to me: assemble the people to me, and I will make them hear my words, that they may learn to fear me all the days they live on the earth, and that they may teach their sons; and you came near and stood under the mountain, and the mountain burned with fire to the heart of heaven, darkness, cloud and thick darkness; and the LORD spoke to you from the midst of the fire: a voice of words you heard, but no form, only a voice; and he declared to you his covenant which he commanded you to do, the ten words, and he wrote them on two tablets of stone',),
    ('Deut 4:13 — and he wrote them on two tablets of stone (Exodus 31:18 — and He gave to Moses, when He finished speaking with him on Mount Sinai, two tablets of the testimony, tablets of stone written with the finger of God)',),
    ('Deut 4:25-31 — when you beget sons and sons\' sons and have grown old in the land and deal corruptly and make a graven image, the form of anything, and do evil in the eyes of the LORD your God to provoke him: I call heaven and earth to witness against you this day that you shall surely perish quickly from the land which you cross the Jordan to possess; you shall not prolong your days upon it but shall be utterly destroyed; and the LORD will scatter you among the peoples and you shall be left few in number among the nations where the LORD will lead you; and there you shall serve gods the work of men\'s hands, wood and stone, which neither see nor hear nor eat nor smell; and from there you will seek the LORD your God and find him, if you seek him with all your heart and all your soul; in your distress, when all these things find you in the end of days, you will return to the LORD your God and hearken to his voice; for the LORD your God is a merciful God: he will not fail you nor destroy you nor forget the covenant of your fathers which he swore to them',),
    ('Deut 4:41-43 — then Moses set apart three cities beyond the Jordan toward the sunrise, that the manslayer might flee there, who slays his neighbor unawares and hated him not in time past, and that fleeing to one of these cities he might live: Bezer in the wilderness in the plain for the Reubenites, and Ramoth in Gilead for the Gadites, and Golan in Bashan for the Manassites',),
]
CLOSES = 'none — the refuge debit appoint_six_cities_of_refuge stays OPEN (Mishnah Makkot 2:4: not until all six; Joshua 20:7-8 the close outside the Torah); no oath written at 4:21 (the sentence read back); the second frame no write'

PERSONS = [
    ('the-priest-who-adds', 'exhortation', 'add_nothing', "Rosh Hashanah 28b:10 — the exam's row add_nothing"),
    ('the-sleeper-on-the-eighth', 'exhortation', 'add_out_of_its_time', "Rosh Hashanah 28b:8-9; Eruvin 96a:5 — the exam's row add_out_of_its_time"),
    ('the-fifth-beside', 'exhortation', 'add_beside', "Sanhedrin 89a:2 — the exam's row add_beside"),
    ('the-one-sprinkling', 'exhortation', 'diminish_nothing', "Rosh Hashanah 28b:16-18 — the exam's row diminish_nothing"),
    ('the-paid-teacher', 'exhortation', 'taught_as_commanded', "Bekhorot 29a:7; Nedarim 37a:2 — the exam's row taught_as_commanded"),
    ('the-scholar-s-father-in-law', 'exhortation', 'the_cleaving', "Ketubot 111b:6-7 — the exam's row the_cleaving"),
    ('the-community-s-sentence', 'exhortation', 'god_so_near', "Rosh Hashanah 18a:10; Yevamot 105a:17 — the exam's row god_so_near"),
    ('the-grandfather', 'horeb', 'take_heed_lest_you_forget', "Kiddushin 30a:3-6; Menachot 99b:3; Avot 3:8 — the exam's row take_heed_lest_you_forget"),
    ('the-daughters', 'horeb', 'the_daughters_excluded', "Kiddushin 30a:6 — the exam's row the_daughters_excluded"),
    ('the-one-commanded-to-teach', 'horeb', 'commanded_to_teach', "Nedarim 38a:5 — the exam's row commanded_to_teach"),
    ('the-moon-forms', 'image', 'image_for_study', "Mishnah Rosh Hashanah 2:8; Rosh Hashanah 24b:13 — the exam's row image_for_study"),
    ('the-vessel-with-the-sun', 'image', 'image_of_the_host', "Rosh Hashanah 24b:8; Mishnah Avodah Zarah 3:3 — the exam's row image_of_the_host"),
    ('the-allotted-host', 'image', 'the_host_apportioned', "Avodah Zarah 55a:9 — the exam's row the_host_apportioned"),
    ('the-grown-old', 'exile', 'the_case_head', "Gittin 88a:15-17 — the exam's row the_case_head"),
    ('the-inquirer', 'god', 'the_former_days', "Chagigah 11b:21-24 — the exam's row the_former_days"),
    ('the-sorcerer-s-victim', 'god', 'you_were_shown', "Chullin 7b:14 — the exam's row you_were_shown"),
    ('the-haggadah-s-expounder', 'god', 'the_nation_from_a_nation', "Mishnah Pesachim 10:4 — the exam's row the_nation_from_a_nation"),
    ('the-manslayer-in-moses-three', 'cities', 'not_until_all_six', "Mishnah Makkot 2:4 — the exam's row not_until_all_six"),
    ('the-teacher-exiled', 'cities', 'the_manslayer_defined', "Makkot 10a:11 — the exam's row the_manslayer_defined"),
]


def scene():
    """THE SCENE — the exam's rows replayed on the world engine (the exodus epoch): the exam's persons through horeb_case — bal tosif's arms, the
    teaching, the images, the host, the exile, the inquiry, the creed, the Haggadah, the cities."""
    with contextlib.redirect_stdout(io.StringIO()):
        w = WE.World(era='Deut 4:1-49: chapter 4 on the shelf — Rosh Hashanah, Eruvin, Sanhedrin, Kiddushin, Bekhorot, Ketubot, Avodah Zarah, Chagigah, Chullin, Gittin, Makkot, Pesachim on the engine (the exodus epoch)', epoch='exodus')
        w.laws = [law_obey_horeb]
        w.advance(w.clock.day_in('exodus', 40, 11, 1))
        # THE DAEMON GATE READS LITERAL SUBMITS ONLY — the nineteen persons typed out from PERSONS
        w.submit({'kind': 'horeb_case', 'subject': 'the-priest-who-adds', 'person': 'the-priest-who-adds', 'cell': 'exhortation', 'ask': 'add_nothing', 'case_source': "Rosh Hashanah 28b:10 — the exam's row add_nothing"})
        w.submit({'kind': 'horeb_case', 'subject': 'the-sleeper-on-the-eighth', 'person': 'the-sleeper-on-the-eighth', 'cell': 'exhortation', 'ask': 'add_out_of_its_time', 'case_source': "Rosh Hashanah 28b:8-9; Eruvin 96a:5 — the exam's row add_out_of_its_time"})
        w.submit({'kind': 'horeb_case', 'subject': 'the-fifth-beside', 'person': 'the-fifth-beside', 'cell': 'exhortation', 'ask': 'add_beside', 'case_source': "Sanhedrin 89a:2 — the exam's row add_beside"})
        w.submit({'kind': 'horeb_case', 'subject': 'the-one-sprinkling', 'person': 'the-one-sprinkling', 'cell': 'exhortation', 'ask': 'diminish_nothing', 'case_source': "Rosh Hashanah 28b:16-18 — the exam's row diminish_nothing"})
        w.submit({'kind': 'horeb_case', 'subject': 'the-paid-teacher', 'person': 'the-paid-teacher', 'cell': 'exhortation', 'ask': 'taught_as_commanded', 'case_source': "Bekhorot 29a:7; Nedarim 37a:2 — the exam's row taught_as_commanded"})
        w.submit({'kind': 'horeb_case', 'subject': 'the-scholar-s-father-in-law', 'person': 'the-scholar-s-father-in-law', 'cell': 'exhortation', 'ask': 'the_cleaving', 'case_source': "Ketubot 111b:6-7 — the exam's row the_cleaving"})
        w.submit({'kind': 'horeb_case', 'subject': 'the-community-s-sentence', 'person': 'the-community-s-sentence', 'cell': 'exhortation', 'ask': 'god_so_near', 'case_source': "Rosh Hashanah 18a:10; Yevamot 105a:17 — the exam's row god_so_near"})
        w.submit({'kind': 'horeb_case', 'subject': 'the-grandfather', 'person': 'the-grandfather', 'cell': 'horeb', 'ask': 'take_heed_lest_you_forget', 'case_source': "Kiddushin 30a:3-6; Menachot 99b:3; Avot 3:8 — the exam's row take_heed_lest_you_forget"})
        w.submit({'kind': 'horeb_case', 'subject': 'the-daughters', 'person': 'the-daughters', 'cell': 'horeb', 'ask': 'the_daughters_excluded', 'case_source': "Kiddushin 30a:6 — the exam's row the_daughters_excluded"})
        w.submit({'kind': 'horeb_case', 'subject': 'the-one-commanded-to-teach', 'person': 'the-one-commanded-to-teach', 'cell': 'horeb', 'ask': 'commanded_to_teach', 'case_source': "Nedarim 38a:5 — the exam's row commanded_to_teach"})
        w.submit({'kind': 'horeb_case', 'subject': 'the-moon-forms', 'person': 'the-moon-forms', 'cell': 'image', 'ask': 'image_for_study', 'case_source': "Mishnah Rosh Hashanah 2:8; Rosh Hashanah 24b:13 — the exam's row image_for_study"})
        w.submit({'kind': 'horeb_case', 'subject': 'the-vessel-with-the-sun', 'person': 'the-vessel-with-the-sun', 'cell': 'image', 'ask': 'image_of_the_host', 'case_source': "Rosh Hashanah 24b:8; Mishnah Avodah Zarah 3:3 — the exam's row image_of_the_host"})
        w.submit({'kind': 'horeb_case', 'subject': 'the-allotted-host', 'person': 'the-allotted-host', 'cell': 'image', 'ask': 'the_host_apportioned', 'case_source': "Avodah Zarah 55a:9 — the exam's row the_host_apportioned"})
        w.submit({'kind': 'horeb_case', 'subject': 'the-grown-old', 'person': 'the-grown-old', 'cell': 'exile', 'ask': 'the_case_head', 'case_source': "Gittin 88a:15-17 — the exam's row the_case_head"})
        w.submit({'kind': 'horeb_case', 'subject': 'the-inquirer', 'person': 'the-inquirer', 'cell': 'god', 'ask': 'the_former_days', 'case_source': "Chagigah 11b:21-24 — the exam's row the_former_days"})
        w.submit({'kind': 'horeb_case', 'subject': 'the-sorcerer-s-victim', 'person': 'the-sorcerer-s-victim', 'cell': 'god', 'ask': 'you_were_shown', 'case_source': "Chullin 7b:14 — the exam's row you_were_shown"})
        w.submit({'kind': 'horeb_case', 'subject': 'the-haggadah-s-expounder', 'person': 'the-haggadah-s-expounder', 'cell': 'god', 'ask': 'the_nation_from_a_nation', 'case_source': "Mishnah Pesachim 10:4 — the exam's row the_nation_from_a_nation"})
        w.submit({'kind': 'horeb_case', 'subject': 'the-manslayer-in-moses-three', 'person': 'the-manslayer-in-moses-three', 'cell': 'cities', 'ask': 'not_until_all_six', 'case_source': "Mishnah Makkot 2:4 — the exam's row not_until_all_six"})
        w.submit({'kind': 'horeb_case', 'subject': 'the-teacher-exiled', 'person': 'the-teacher-exiled', 'cell': 'cities', 'ask': 'the_manslayer_defined', 'case_source': "Makkot 10a:11 — the exam's row the_manslayer_defined"})
    n = lambda eid, eff: len([e for e in w.entity(eid).ledger if e['effect'] == eff])
    tset = len([l for l in w.log if l[0] == 'TIMER-SET']); tfire = len([l for l in w.log if l[0] == 'TIMER-FIRE']); tcan = len([l for l in w.log if l[0] == 'TIMER-CANCEL'])
    closes = len([e for ent in w.entities.values() for e in ent.ledger if e.get('closed_by')])
    return (tuple(n(p, 'accepted') + n(p, 'exempt') for p, _, _, _ in PERSONS), (n('the-sleeper-on-the-eighth', 'exempt'), n('the-fifth-beside', 'exempt'), n('the-daughters', 'exempt'), n('the-moon-forms', 'exempt'), n('the-manslayer-in-moses-three', 'exempt')), (tset, tfire, tcan, len(w.timers)), len(w.entities), closes), w
SCENE, _W = scene()
# THE PREDICTION (typed before the first run — the design's arithmetic): every exam person written once; the five exempt arms ONE each; no timer;
# ENTITIES the nineteen persons; CLOSES 0.
SCENE_PREDICTED = ((1,) * 19, (1, 1, 1, 1, 1), (0, 0, 0, 0), 19, 0)
assert SCENE == SCENE_PREDICTED, ('THE DEUTERONOMY WALK 2b: the scene moved from its prediction', SCENE, SCENE_PREDICTED)


def narrative():
    """THE DEUTERONOMY WALK 2b (2026-09-16): the chapter's own acts AS HISTORY — the three own-day lines at the speech's day (40, 11, 1) and the two
    SUPPLIED Horeb lines dated by the RETROGRADE markers at Deut 4:10 (1, 3, 7) and 4:13 (1, 4, 17), the stretch ENDED by a FORWARD marker at 4:25 back to the speech's day (the engine's stretch runs to the next marker — the first generator run's finding), and the chapter OPENED by a forward marker at 4:1 (1b's Deut 2:2 stretch still open on the tape — the first stitch's finding) — on a world with this runner's daemon: 5 writes
    (one effect per line), no timer, TWO entities (Israel, Moses), the counter at (11, 1), NO close, no row, TWO dated lines. Recorded by the
    sequential run's recorder and stitched onto the tape (the markers the stitcher's rows). Not a graded cell: the tuple below is a tripwire typed
    from the design."""
    with contextlib.redirect_stdout(io.StringIO()):
        w = WE.World(era='Deut 4:1-49 on the tape — the one law, the two supplied Horeb lines, the one case, the three cities (the exodus epoch)', epoch='exodus')
        w.laws = [law_obey_horeb]
        w.advance(w.clock.day_in('exodus', 40, 11, 1))
        # THE DAEMON GATE READS LITERAL SUBMITS ONLY — the five lines typed out; no field named `until`, `days` or `due`
        w.marker('Deut 4:1', w.clock.day_in('exodus', 40, 11, 1), value='chapter 4 opens at the speech\'s own day — on the tape this FORWARD marker ends 1b\'s retrograde stretch (Deut 2:2\'s); here the counter\'s own day re-asserted')
        w.submit({'kind': 'add_nothing_commanded', 'subject': 'israel', 'law': 'you shall not add nor diminish (4:2)', 'receipt': 'as the LORD my God commanded me (4:5)', 'case_source': LINES[0][0]})
        w.marker('Deut 4:10', w.clock.day_in('exodus', 1, 3, 7), value='the ten words told — dated at the giving (Exod 19:16): RETROGRADE', placement='reading_placed')
        w.submit({'kind': 'ten_words_declared', 'subject': 'israel', 'first_telling': 'Exod 20:1-17', 'dated': 'the giving (1, 3, 7)', 'case_source': LINES[1][0]})
        w.marker('Deut 4:13', w.clock.day_in('exodus', 1, 4, 17), value='the tablets told — dated at the breaking (Exod 32:19): RETROGRADE', placement='reading_placed')
        w.submit({'kind': 'tablets_given', 'subject': 'moses', 'first_telling': 'Exod 31:18', 'dated': 'the fortieth day (1, 4, 17)', 'plene': 'the tablets written plene (4:13)', 'case_source': LINES[2][0]})
        w.marker('Deut 4:25', w.clock.day_in('exodus', 40, 11, 1), value='the stretch ends at the speech\'s day — the counter\'s own day re-asserted after the two dated lines: FORWARD (the first generator run found the two own-day lines after 4:13 dated at Tammuz — a retrograde stretch runs to the next marker)')
        w.submit({'kind': 'witnesses_called', 'subject': 'israel', 'case': 'when you beget sons (4:25)', 'witnesses': 'heaven and earth (4:26)', 'case_source': LINES[3][0]})
        w.submit({'kind': 'three_cities_set_apart', 'subject': 'israel', 'cities': ['Bezer', 'Ramoth', 'Golan'], 'manslayer': 'who slays his neighbor unawares (4:42)', 'case_source': LINES[4][0]})
    writes = len([l for l in w.log if l[0] == 'WRITE'])
    closes = len([e for ent in w.entities.values() for e in ent.ledger if e.get('closed_by')])
    rows = len([l for l in w.log if l[0] == 'ROW'])
    dated = len([l for l in w.log if l[0] == 'EVENT' and l[2].get('dated') is not None])
    return (writes, len([l for l in w.log if l[0] == 'TIMER-SET']), len(w.entities), w.clock.eras['exodus'].date(w.clock.day)[1:], closes, rows, len(w.tables['population']), dated), w


NARRATIVE, _WN = narrative()
NARRATIVE_PREDICTED = (5, 0, 2, (11, 1), 0, 0, 0, 2)   # DEUTERONOMY_WALK.md "Sitting 2b": 5 writes (one per line), no timer, TWO entities, the counter's day (11, 1), NO close, no row, TWO dated lines (the retrograde stretches')
assert NARRATIVE == NARRATIVE_PREDICTED, ('THE DEUTERONOMY WALK 2b: the chapter\'s narrative moved from its prediction', NARRATIVE, NARRATIVE_PREDICTED)
_isr = _WN.entity('israel').ledger
assert [e['effect'] for e in _isr] == ['adding_barred', 'covenant_declared', 'heaven_and_earth_witness', 'cities_set_apart'] and [e['effect'] for e in _WN.entity('moses').ledger] == ['tablets_delivered'], ([e['effect'] for e in _isr], [e['effect'] for e in _WN.entity('moses').ledger])
assert [ex.date(l[2]['dated']) for l in _WN.log if l[0] == 'EVENT' and l[2].get('dated') is not None for ex in [_WN.clock.eras['exodus']]] == [(1, 3, 7), (1, 4, 17)], 'the two supplied lines dated by their markers'
