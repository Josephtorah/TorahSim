
# ---- THE CALLEES' FACTS (every edge live at the cells that consume them; the values asserted from the callees' own prints — ch5_callees.out) ----
DC_VAINOATH = DC.vain_name({'ask': 'vain_oath'}, DC.DATA); DC_VAIN = DC.vain_name({'ask': 'vain_and_false_utterance'}, DC.DATA); DC_REM = DC.sabbath_clauses({'ask': 'remember'}, DC.DATA); DC_SCOPE = DC.sabbath_clauses({'ask': 'labor_scope'}, DC.DATA); DC_LADEN = DC.sabbath_clauses({'ask': 'laden_beast'}, DC.DATA); DC_KID = DC.theft_commandment({'ask': 'kidnapper'}, DC.DATA); DC_MONEY = DC.theft_commandment({'ask': 'money_theft_here'}, DC.DATA)
assert DC_VAINOATH[:2] == ('lashes', ['lashes']) and DC_VAIN[0] == 'spoken as one' and DC_REM[:2] == ('sanctify over wine', ['sanctify_day']) and DC_SCOPE[:2] == ('the whole household barred', ['labor_barred', 'rest_required']) and DC_LADEN[:2] == ('driving the laden beast barred', ['labor_barred']) and DC_KID[:2] == ('capital — the kidnapper', ['put_to_death']) and DC_MONEY[0] == 'routed to the ordinances span' and DC.GUARDED == 13, (DC_VAIN[0], DC_KID[:2])
OH_LIST = OH.DATA['the_no_image_list']['value']; OH_HOLE = OH.DATA['the_horeb_hole']['value']; OH_VOICE = OH.horeb_retold({'ask': 'the_voice_and_no_form'}, OH.DATA); OH_TABLETS = OH.horeb_retold({'ask': 'the_ten_words_and_the_tablets'}, OH.DATA)
assert len(OH_LIST) == 11 and OH_LIST[0] == 'a graven image' and OH_HOLE == {'exod_20_1': 'no_line_on_the_tape', 'exod_31_18': 'no_line_on_the_tape'} and OH_VOICE[1] == ['covenant_declared'] and OH_TABLETS[1] == ['tablets_delivered'] and len(OH.READBACK) == 11 and OH.GRADES == ('VERBATIM', 'TURNED', 'SHORTENED', 'EXPANDED', 'SUPPLIED', 'DISAGREES'), (len(OH_LIST), OH_VOICE[1])
ER_SPEECH = ER.presence('speech_with_speech'); ER_BOOK = ER.blood_covenant('book_of_covenant'); ER_VOICE1 = ER.blood_covenant('one_voice'); ER_TEN = ER.tablets('ten_words'); ER_TORAH = ER.ascent('torah_mitzvah')
assert ER_SPEECH['v'] == 'speech_with_speech' and ER_BOOK['v'] == 4 and ER_VOICE1['v'] == 2 and ER_TEN['v'] == 3 and ER_TORAH['v'] == 2, (ER_SPEECH['v'], ER_BOOK['v'], ER_VOICE1['v'], ER_TEN['v'], ER_TORAH['v'])
ES_DAYS = ES.sinai('days_r_yose'); ES_SEATS = ES.sinai('we_will_do_seats'); ES_TUB = ES.sinai('tub'); ES_MARAH = ES.marah('statute_list')
assert ES_DAYS['v'] == (2, 3, 4, 7) and ES_SEATS['v'] == [(19, 8), (24, 3), (24, 7)] and ES_TUB['v'] == 'the_mountain_held_over_them_like_a_tub' and ES_MARAH['v'] == ('seven_of_the_sons_of_noah', 'courts', 'sabbath', 'honoring_father_and_mother'), (ES_DAYS['v'], ES_SEATS['v'], ES_MARAH['v'])
OS_ASK = OS.the_spies_read_back({'ask': 'the_asking'}, OS.DATA); OS_OATH = OS.the_spies_read_back({'ask': 'the_oath'}, OS.DATA); OS_WRITE = OS.the_frame({'ask': 'the_write'}, OS.DATA)
assert OS_ASK[0].startswith('the asking (1:22)') and OS_OATH[0].startswith('the oath (1:34-36)') and OS_WRITE[1] == ['torah_expounded'] and len(OS.READBACK) == 42 and callable(OS._closed_by_prior_run), (OS_ASK[0][:30], OS_OATH[0][:30], OS_WRITE[1])
HO_HONOR = HO.frame('honor_defined'); HO_FEAR = HO.frame('fear_defined'); HO_ORDER = HO.frame('parents_order'); HO_THREE = HO.frame('three_partners'); HO_WOMAN = HO.frame('woman_included')
assert HO_HONOR['v'] == ['feed', 'give_drink', 'clothe', 'cover', 'bring_in', 'take_out'] and HO_FEAR['v'] == ['not_sit_in_his_place', 'not_speak_in_his_place', 'not_contradict_him'] and HO_ORDER['v'] == 'mother_first_here_father_first_at_Sinai_both_equal' and HO_THREE['v'] == ['God', 'father', 'mother'] and HO_WOMAN['v'] == 'woman_bound_to_fear_when_able', (HO_HONOR['v'], HO_FEAR['v'], HO_ORDER['v'])
M3_KILL = M3.killer('mode'); M3_STRIKE = M3.parent_striker('mode'); M3_CURSE = M3.parent_curser('the_woman')
assert M3_KILL['v'] == 'the_sword' and M3_STRIKE['v'] == 'strangling' and M3_CURSE['v'] == 'included', (M3_KILL['v'], M3_STRIKE['v'], M3_CURSE['v'])
SA_ADULT = SA.adultery('mode'); SA_BOTH = SA.adultery('both'); SA_CURSER = SA.curser('mode')
assert SA_ADULT['v'] == 'strangling' and SA_BOTH['v'] == 'the_adulterer_and_the_adulteress' and SA_CURSER['v'] == 'stoning', (SA_ADULT['v'], SA_BOTH['v'], SA_CURSER['v'])
RF_MURD = RF.the_murderer({'ask': 'he_is_a_murderer'}, RF.DATA)
assert RF_MURD[0].startswith('he is a murderer (35:16-18, 21)') and RF_MURD[1] == ['put_to_death'], RF_MURD[:2]
OR_FALSE = OR.courts('false_report'); OR_VIOL = OR.courts('witness_of_violence')
assert OR_FALSE['v'] == 'hapax' and OR_VIOL['v'] == 'robbers_disqualified', (OR_FALSE['v'], OR_VIOL['v'])
PS_DELTA = PS.sabbath('delta_20_11'); PS_REPEAT = PS.noahide('repeated_at_sinai'); PS_PROCR = PS.noahide('procreation_israel')
assert PS_DELTA['v'] == (18, 22, True, True) and PS_REPEAT['v'] == 'the_repetition_is_the_edge' and PS_PROCR['v'] == 'israel_only_by_the_framework', (PS_DELTA['v'], PS_REPEAT['v'], PS_PROCR['v'])


# ===== THE WRAP (D9-iv): the daemon over the cells — the ledger written, no event emitted =====================
def law_covenant_at_horeb(event, world):
    """Deut 5:1-33 (cold_run_covenant_at_horeb.py F1-F7). given_at Exodus 20:3 — THE SECOND WORD'S FIRST GIVING, its code compiled here from the
    second copy (5:7-10) with the first, and the tenth word's (5:21 with 20:17): THE CODE'S HOLE FILLED FROM THE RETELLING'S SEAT; installed_by
    covenant_blood_thrown (law_decalogue's own installer). THE BLOCKS WRITTEN AT THE CODE'S OWN LINE: the daemon watches 2b's supplied line
    ten_words_declared (dated (1, 3, 7)) and writes other_gods_barred and coveting_barred there — never at the retelling's (THE REST's one declared
    delta). TWO TAPE LINES of its own, both SUPPLIED and dated (1, 3, 7) by the retrograde marker at Deut 5:23: the request for a mediator (the
    tape's second hole — torah_through_moses on Israel) and the answer (the charge to teach a DEBIT on Moses CLOSED AT ONCE BY THE PRIOR RUN — the
    opening speech's form, the closer Deut 1:5; return to your tents a STATUS on Israel). The exam's case kind dispatches to the cells in EXPLICIT
    branches with LITERAL effects per kind (an unnamed effect is a KeyError). No timer."""
    k, src = event['kind'], event['case_source']
    E_ = lambda eff, s, cp=None, amount=None, due=None, law='', value=None: {'effect': eff, 'subject': s, 'counterparty': cp, 'amount': amount, 'due': due, 'value': value if value is not None else True, 'source_law': law, 'case_source': src}
    if k == 'ten_words_declared':
        return [E_('other_gods_barred', 'israel', value='no other gods before me; no graven image nor any form; not bow down to them nor serve them — the bower, the slaughterer, the incense-burner, the libation-pourer stoned (Mishnah Sanhedrin 7:6; Sanhedrin 60b), the hugger and the kisser a prohibition; the visiting to the third and the fourth generation, mercy to thousands (5:7-10 / 20:3-6)', law='F2 [INK 5:7-10 with Exodus 20:3-6 — THE SECOND WORD, compiled at THE DEUTERONOMY WALK 3b from its second copy (no cell in any runner before): a BLOCK on Israel written at the giving\'s own line (2b\'s ten_words_declared, dated (1, 3, 7)); the answer sheet Mishnah Sanhedrin 7:6 with Sanhedrin 60b:1-19 — the mode stoning by the juxtaposition of Deut 17:3 to 17:5, the prohibition of bowing from Exodus 34:14; the no-image list 4:16-19 the parameter table (OH by CALL)]'),
                E_('coveting_barred', 'israel', value="you shall not covet your neighbor's wife; you shall not desire your neighbor's house, his field, his servant, his maidservant, his ox, his ass, anything that is your neighbor's (5:21 / 20:17) — taking by force or deceit even with payment (Bava Metzia 5b:19); most people read it as without payment (5b:20)", law="F5 [INK 5:21 with Exodus 20:17 — THE TENTH WORD, compiled at THE DEUTERONOMY WALK 3b from its second copy (no cell in any runner before): a BLOCK on Israel written at the giving's own line; the wife first here, the house first there, 'desire' for the second covet, 'his field' added; Bava Metzia 5b:19-20 the answer sheet]")]
    if k == 'mediator_requested':
        return [E_('torah_through_moses', 'israel', value={'the_request': 'go you near and hear all that the LORD our God shall say, and you speak to us all that the LORD our God speaks to you, and we will hear and do (5:27)', 'the_first_telling': 'Exodus 20:18-19 — speak you with us and we will hear, but let not God speak with us lest we die', 'dated': (1, 3, 7), 'the_hole': "no line on the tape for Exodus 20:18-21 until this one (the laws' readback's finding)", 'makkot_24a': "the first two words from the Almighty's mouth, the rest through Moses"}, law="F6 [INK 5:23-27 'when you heard the voice … you came near to me, all the heads of your tribes and your elders … go you near and hear … and we will hear and do' — THE TAPE'S SECOND HOLE (Exodus 20:18-19 the first telling; 20:18 in no runner's span, 20:19-21 the ordinances' law cells): written ONCE at its own time, dated (1, 3, 7) by the retrograde marker at 5:23 (Rabbi Yose's seventh, ES.sinai by CALL); a STATUS on Israel — Avot 1:1's vocabulary, Makkot 24a:1's count; 'we will hear and do' against 24:7's order (Shabbat 88a)]")]
    if k == 'stand_here_commanded':
        eff = E_('commanded', 'moses', value='teach_the_commandment', law="F7 [INK 5:31 'and you, stand here with me, and I will speak to you all the commandment and the statutes and the judgments WHICH YOU SHALL TEACH THEM' — TOLD ONLY IN THE RETELLING (Exodus 20:22's answer another speech; 18:16-17 forward): written once, dated (1, 3, 7) inside the retrograde stretch of 5:23, CLOSED AT ONCE BY THE PRIOR RUN — the book's own expounding (1:5) and 4:5's 'I have taught you … as the LORD my God commanded me' (Exodus 24:12's 'to teach them', ER.ascent by CALL); Megillah 21a:14 the Torah received standing; the Sifrei 357:40]")
        eff['written_by'] = 'law_covenant_at_horeb'
        OS._closed_by_prior_run(world, event, eff, "Deut 1:5 — beyond the Jordan, in the land of Moab, Moses undertook to expound this Torah, saying: THE CLOSE BY A PRIOR RUN (R3) — the charge to teach given at Horeb (5:31, told only in the retelling) ran at the book's own opening (the frame's line 1:1-5, torah_expounded) and at the exhortation's receipt 'I have taught you statutes and judgments as the LORD my God commanded me' (4:5), the tape's earlier lines; the command came to the reader after its execution (the closer names 1:5 alone — a range would fold 1:3's receipt into a CLOSE, the gate's class by containment)")
        return [E_('returned_to_tents', 'israel', value={'the_word': 'go say to them: return to your tents (5:30)', 'released': "the separation of Exodus 19:15 — 'do not come near a woman' (the tape's people_sanctified, 19:10-15)", 'dated': (1, 3, 7), 'beitzah_5a': 'a matter forbidden by a count needs a count to permit (Rav Yosef)', 'moses': "and you, stand here with me — Moses' own separation agreed (Shabbat 87a; Yevamot 62a)"}, law="F7 [INK 5:30 'go say to them: return to your tents' — a STATUS on Israel: the separation of Exodus 19:15 released by an explicit word (Beitzah 5a:7-5b:3; Moed Katan 7b:5 'his tent' his wife; Sanhedrin 59b:3-4 procreation repeated at Sinai — PS.noahide by CALL); told only in the retelling, dated (1, 3, 7)]")]
    if k == 'horeb_covenant_case':
        fn = {'assembly': the_assembly_called, 'second': the_second_word, 'first_tablet': the_first_tablet, 'second_tablet': the_second_tablet, 'tenth': the_tenth_word, 'voice': the_voice_and_the_request, 'answer': the_answer_and_the_charge}[event['cell']]
        v, e, _ = fn({'ask': event['ask']}, DATA); L = '%s [%s]' % ({'assembly': 'F1', 'second': 'F2', 'first_tablet': 'F3', 'second_tablet': 'F4', 'tenth': 'F5', 'voice': 'F6', 'answer': 'F7'}[event['cell']], event['ask']); s_ = event['person']
        W = {'accepted': E_('accepted', s_, value=v, law=L), 'exempt': E_('exempt', s_, value=v, law=L), 'put_to_death': E_('put_to_death', s_, value='stoned — ' + v, law=L)}
        return [W[x] for x in e if x != FX.NONE]
    return []


LINES = [
    ('Deut 5:23-27 — and it came to pass, when you heard the voice out of the midst of the darkness, while the mountain burned with fire, that you came near to me, all the heads of your tribes and your elders, and you said: behold, the LORD our God has shown us his glory and his greatness, and his voice we have heard out of the midst of the fire; this day we have seen that God speaks with man and he lives; now therefore why should we die? for this great fire will consume us; if we hear the voice of the LORD our God any more, we shall die; for who is there of all flesh that has heard the voice of the living God speaking out of the midst of the fire, as we have, and lived? go you near and hear all that the LORD our God shall say, and you speak to us all that the LORD our God speaks to you, and we will hear and do',),
    ('Deut 5:28-31 — and the LORD heard the voice of your words when you spoke to me; and the LORD said to me: I have heard the voice of the words of this people which they have spoken to you; they have done well in all that they have spoken; who would give that they had such a heart as this always, to fear me and keep all my commandments, that it might be well with them and with their children forever; go say to them: return to your tents; but as for you, stand here with me, and I will speak to you all the commandment and the statutes and the judgments which you shall teach them, that they may do them in the land which I give them to possess',),
]
CLOSES = "one — the charge to teach (commanded on Moses, teach_the_commandment) CLOSED inside the daemon by the prior run, the closer Deut 1:5's expounding; no second write at 5:22 (the voice and the tablets FOUND); the frame and the charge no write"

PERSONS = [
    ('the-bower', 'second', 'bow_and_serve', "Mishnah Sanhedrin 7:6; Sanhedrin 60b:11 — the exam's row bow_and_serve"),
    ('the-stone-thrower-at-markulis', 'second', 'in_its_way', "Mishnah Sanhedrin 7:6; Sanhedrin 60b:3 — the exam's row in_its_way"),
    ('the-embracer', 'second', 'the_embracer', "Mishnah Sanhedrin 7:6; Sanhedrin 60b:2 — the exam's row the_embracer"),
    ('the-coveter-who-pays', 'tenth', 'the_coveter_who_pays', "Bava Metzia 5b:19-20 — the exam's row the_coveter_who_pays"),
    ('the-woman-at-kiddush', 'first_tablet', 'keep_and_remember', "Berakhot 20b:10 — the exam's row keep_and_remember"),
    ('the-laden-beast-s-driver', 'first_tablet', 'the_ox_and_the_ass', "Bava Kamma 54b:13 — the exam's row the_ox_and_the_ass"),
    ('the-circumcised-slave', 'first_tablet', 'the_servants_rest', "Yevamot 48b:5 — the exam's row the_servants_rest"),
    ('the-vain-swearer', 'first_tablet', 'the_third_word', "Mishnah Shevuot 3:8 — the exam's row the_third_word"),
    ('the-son-who-feeds-pheasant', 'second_tablet', 'the_fifth_word', "Kiddushin 31a:14 — the exam's row the_fifth_word"),
    ('the-abductor-of-persons', 'second_tablet', 'the_eighth_word', "Sanhedrin 86a:16 — the exam's row the_eighth_word"),
    ('the-one-who-said-we-will-do-first', 'voice', 'hear_and_do', "Shabbat 88a:7 — the exam's row hear_and_do"),
]


def scene():
    """THE SCENE — the exam's rows replayed on the world engine (the exodus epoch): the exam's persons through horeb_covenant_case — the second
    word's idolater and embracer, the coveter who pays, the woman at kiddush, the laden beast, the slave's rest, the vain oath, the honor, the
    theft of persons, 'we will do' first."""
    with contextlib.redirect_stdout(io.StringIO()):
        w = WE.World(era='Deut 5:1-33: chapter 5 on the shelf — Sanhedrin, Bava Metzia, Berakhot, Bava Kamma, Yevamot, Shevuot, Kiddushin, Shabbat on the engine (the exodus epoch)', epoch='exodus')
        w.laws = [law_covenant_at_horeb]
        w.advance(w.clock.day_in('exodus', 40, 11, 1))
        # THE DAEMON GATE READS LITERAL SUBMITS ONLY — the eleven persons typed out from PERSONS
        w.submit({'kind': 'horeb_covenant_case', 'subject': 'the-bower', 'person': 'the-bower', 'cell': 'second', 'ask': 'bow_and_serve', 'case_source': "Mishnah Sanhedrin 7:6; Sanhedrin 60b:11 — the exam's row bow_and_serve"})
        w.submit({'kind': 'horeb_covenant_case', 'subject': 'the-stone-thrower-at-markulis', 'person': 'the-stone-thrower-at-markulis', 'cell': 'second', 'ask': 'in_its_way', 'case_source': "Mishnah Sanhedrin 7:6; Sanhedrin 60b:3 — the exam's row in_its_way"})
        w.submit({'kind': 'horeb_covenant_case', 'subject': 'the-embracer', 'person': 'the-embracer', 'cell': 'second', 'ask': 'the_embracer', 'case_source': "Mishnah Sanhedrin 7:6; Sanhedrin 60b:2 — the exam's row the_embracer"})
        w.submit({'kind': 'horeb_covenant_case', 'subject': 'the-coveter-who-pays', 'person': 'the-coveter-who-pays', 'cell': 'tenth', 'ask': 'the_coveter_who_pays', 'case_source': "Bava Metzia 5b:19-20 — the exam's row the_coveter_who_pays"})
        w.submit({'kind': 'horeb_covenant_case', 'subject': 'the-woman-at-kiddush', 'person': 'the-woman-at-kiddush', 'cell': 'first_tablet', 'ask': 'keep_and_remember', 'case_source': "Berakhot 20b:10 — the exam's row keep_and_remember"})
        w.submit({'kind': 'horeb_covenant_case', 'subject': 'the-laden-beast-s-driver', 'person': 'the-laden-beast-s-driver', 'cell': 'first_tablet', 'ask': 'the_ox_and_the_ass', 'case_source': "Bava Kamma 54b:13 — the exam's row the_ox_and_the_ass"})
        w.submit({'kind': 'horeb_covenant_case', 'subject': 'the-circumcised-slave', 'person': 'the-circumcised-slave', 'cell': 'first_tablet', 'ask': 'the_servants_rest', 'case_source': "Yevamot 48b:5 — the exam's row the_servants_rest"})
        w.submit({'kind': 'horeb_covenant_case', 'subject': 'the-vain-swearer', 'person': 'the-vain-swearer', 'cell': 'first_tablet', 'ask': 'the_third_word', 'case_source': "Mishnah Shevuot 3:8 — the exam's row the_third_word"})
        w.submit({'kind': 'horeb_covenant_case', 'subject': 'the-son-who-feeds-pheasant', 'person': 'the-son-who-feeds-pheasant', 'cell': 'second_tablet', 'ask': 'the_fifth_word', 'case_source': "Kiddushin 31a:14 — the exam's row the_fifth_word"})
        w.submit({'kind': 'horeb_covenant_case', 'subject': 'the-abductor-of-persons', 'person': 'the-abductor-of-persons', 'cell': 'second_tablet', 'ask': 'the_eighth_word', 'case_source': "Sanhedrin 86a:16 — the exam's row the_eighth_word"})
        w.submit({'kind': 'horeb_covenant_case', 'subject': 'the-one-who-said-we-will-do-first', 'person': 'the-one-who-said-we-will-do-first', 'cell': 'voice', 'ask': 'hear_and_do', 'case_source': "Shabbat 88a:7 — the exam's row hear_and_do"})
    n = lambda eid, eff: len([e for e in w.entity(eid).ledger if e['effect'] == eff])
    tset = len([l for l in w.log if l[0] == 'TIMER-SET']); tfire = len([l for l in w.log if l[0] == 'TIMER-FIRE']); tcan = len([l for l in w.log if l[0] == 'TIMER-CANCEL'])
    closes = len([e for ent in w.entities.values() for e in ent.ledger if e.get('closed_by')])
    return (tuple(n(p, 'accepted') + n(p, 'exempt') + n(p, 'put_to_death') for p, _, _, _ in PERSONS), (n('the-embracer', 'exempt'), n('the-coveter-who-pays', 'exempt'), n('the-bower', 'put_to_death'), n('the-stone-thrower-at-markulis', 'put_to_death')), (tset, tfire, tcan, len(w.timers)), len(w.entities), closes), w
SCENE, _W = scene()
# THE PREDICTION (typed before the first run — the design's arithmetic): every exam person written once; the two exempt arms and the two stoned
# ONE each; no timer; ENTITIES the eleven persons; CLOSES 0.
SCENE_PREDICTED = ((1,) * 11, (1, 1, 1, 1), (0, 0, 0, 0), 11, 0)
assert SCENE == SCENE_PREDICTED, ('THE DEUTERONOMY WALK 3b: the scene moved from its prediction', SCENE, SCENE_PREDICTED)


def narrative():
    """THE DEUTERONOMY WALK 3b (2026-09-16): the chapter's own acts AS HISTORY — the two SUPPLIED lines dated (1, 3, 7) by the RETROGRADE marker at
    Deut 5:23 (the giving's day), the stretch ENDED by a FORWARD marker at 5:32 back to the speech's day — on a world with this runner's daemon:
    3 writes (torah_through_moses; the charge's debit; returned_to_tents), no timer, TWO entities (Israel, Moses), the counter at (11, 1), ONE close
    (the charge closed by the prior run — the closer's line absent from this bare world, the close still the daemon's own), no row, TWO dated lines.
    The blocks at the giving's line are the TAPE's (the giving line is 2b's, not replayed here — the recorder attributes every submit to its scene).
    Recorded by the sequential run's recorder and stitched onto the tape (the markers the stitcher's rows). Not a graded cell: the tuple below is a
    tripwire typed from the design."""
    with contextlib.redirect_stdout(io.StringIO()):
        w = WE.World(era='Deut 5:1-33 on the tape — the request for a mediator and the answer, dated at the giving (the exodus epoch)', epoch='exodus')
        w.laws = [law_covenant_at_horeb]
        w.advance(w.clock.day_in('exodus', 40, 11, 1))
        # THE DAEMON GATE READS LITERAL SUBMITS ONLY — the two lines typed out; no field named `until`, `days` or `due`
        w.marker('Deut 5:23', w.clock.day_in('exodus', 1, 3, 7), value='the request told — dated at the giving (Exod 19:16): RETROGRADE', placement='reading_placed')
        w.submit({'kind': 'mediator_requested', 'subject': 'israel', 'first_telling': 'Exod 20:18-19', 'dated': 'the giving (1, 3, 7)', 'request': 'go you near and hear … and we will hear and do (5:27)', 'case_source': LINES[0][0]})
        w.submit({'kind': 'stand_here_commanded', 'subject': 'moses', 'first_telling': 'told only here — Deut 18:16-17 forward', 'dated': 'the giving (1, 3, 7)', 'answer': 'they have done well; return to your tents; stand here with me (5:28-31)', 'case_source': LINES[1][0]})
        w.marker('Deut 5:32', w.clock.day_in('exodus', 40, 11, 1), value='the charge at the speech\'s own day — the stretch ENDED: FORWARD (2b\'s lesson 1)')
    writes = len([l for l in w.log if l[0] == 'WRITE'])
    closes = len([e for ent in w.entities.values() for e in ent.ledger if e.get('closed_by')])
    rows = len([l for l in w.log if l[0] == 'ROW'])
    dated = len([l for l in w.log if l[0] == 'EVENT' and l[2].get('dated') is not None])
    return (writes, len([l for l in w.log if l[0] == 'TIMER-SET']), len(w.entities), w.clock.eras['exodus'].date(w.clock.day)[1:], closes, rows, len(w.tables['population']), dated), w


NARRATIVE, _WN = narrative()
NARRATIVE_PREDICTED = (3, 0, 2, (11, 1), 1, 0, 0, 2)   # DEUTERONOMY_WALK.md "Sitting 3b": 3 writes, no timer, TWO entities, the counter's day (11, 1), ONE close (the charge by the prior run), no row, TWO dated lines
assert NARRATIVE == NARRATIVE_PREDICTED, ('THE DEUTERONOMY WALK 3b: the chapter\'s narrative moved from its prediction', NARRATIVE, NARRATIVE_PREDICTED)
_isr = _WN.entity('israel').ledger
assert [e['effect'] for e in _isr] == ['torah_through_moses', 'returned_to_tents'] and [(e['effect'], e.get('value'), bool(e.get('closed_by'))) for e in _WN.entity('moses').ledger] == [('commanded', 'teach_the_commandment', True)], ([e['effect'] for e in _isr], [e['effect'] for e in _WN.entity('moses').ledger])
assert [ex.date(l[2]['dated']) for l in _WN.log if l[0] == 'EVENT' and l[2].get('dated') is not None for ex in [_WN.clock.eras['exodus']]] == [(1, 3, 7), (1, 3, 7)], 'the two supplied lines dated by the marker at 5:23'
