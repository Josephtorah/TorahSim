

# ---- THE WRAP — the daemon, the scene, the narrative ------------------------------------------------------
def law_shelach(event, world):
    """Num 13:1-15:31 (cold_run_shelach.py F1-F7). installed_by boot — the laws spoken at their verses; the libations' and the challah's
    land gate is the cell's own (15:2, 15:18), not the daemon's, so the spies' lines dispatch in year 2."""
    k, src = event['kind'], event['case_source']
    E_ = lambda eff, s, cp=None, amount=None, due=None, law='', value=None: {'effect': eff, 'subject': s, 'counterparty': cp, 'amount': amount, 'due': due, 'value': value if value is not None else True, 'source_law': law, 'case_source': src}
    day = event.get('day', world.clock.day)      # THE SEQUENTIAL RUN: the event's own day
    if k == 'spies_commanded':
        return [E_('commanded', event['subject'], value='the_sending', law='F1 [INK 13:2 "send for yourself men that they may spy out the land" — the sending owed on Moses, at his discretion (Sotah 34b:3)]')]
    if k == 'spies_sent':
        world.close('moses', 'commanded', 'Num 13:3 — and Moses sent them from the wilderness of Paran by the mouth of the LORD', value='the_sending')
        return [E_('sent_to_spy', event['subject'], value='the twelve by tribe — a fourth order, Levi absent, Joseph over Manasseh; Hoshea renamed Joshua (13:16)', law='F1 [INK 13:3-16; Sotah 34b:5-8]'),
                E_('spied_forty_days', event['subject'], due=day + FORTY[0], value='forty days of spying — the return "at the end of forty days" (13:25) on the Ninth of Av (Taanit 29a:5); the fire the day after the marker (CF2)', law='F1 [INK 13:25; Taanit 29a:5-6]')]
    if k == 'spies_instructed':
        return [E_('commanded', event['subject'], value='the_questionnaire', law='F1 [INK 13:17-20 — the seven questions owed an answer: strong or weak, few or many, good or bad, camps or fortresses, fat or lean, trees or none; the fruit]')]
    if k in ('spies_went_up', 'spies_returned'):
        return []                                  # the timer runs; the return is the tape's reading-placed marker (2, 5, 9)
    if k == 'report_given':
        world.close(event['subject'], 'commanded', 'Num 13:27 — and they told him and said: we came to the land where you sent us', value='the_questionnaire')
        return [E_('report_given', event['subject'], value='fat (milk and honey, the fruit); strong (the people fierce, the Anak); fortified; the map — the questionnaire answered; truth first (Sotah 35a:2)', law='F1 [INK 13:27-29; the questionnaire\'s debit CLOSED]')]
    if k == 'caleb_hushed_the_people':
        return [E_('plea_made', 'caleb', cp='israel', value='we shall surely go up and possess it, for we can surely prevail — the ruse (Sotah 35a:3-6)', law='F1 [INK 13:30]')]
    if k == 'evil_report_spread':
        return [E_('evil_report_spread', event['subject'], value='stronger than us — or than Him; a land that eats its inhabitants; the Nephilim; grasshoppers (13:31-33)', law='F1 [INK 13:31-33; Arakhin 15a:12-13; Sotah 35a:7-9]')]
    if k == 'congregation_wept':
        return [E_('wept', event['subject'], value='that night — the Ninth of Av (Taanit 29a:7; Sotah 35a:11; Sanhedrin 104b:4)', law='F2 [INK 14:1]'),
                E_('tested_the_lord', event['subject'], value='the tenth trial — the spies (Arakhin 15a-b; 14:22 "these ten times"); "let us appoint a head and return to Egypt"', law='F2 [INK 14:2-4; Arakhin 15a:10 (Reish Lakish: sealed for this sin)]')]
    if k == 'joshua_and_caleb_pleaded':
        return [E_('plea_made', 'joshua', cp='israel', value='the garments rent; the land is very very good; their shadow has departed; fear them not (14:6-9)', law='F2 [INK 14:5-9; Taanit 14b:13]'),
                E_('plea_made', 'caleb', cp='israel', value='the garments rent; the land is very very good; fear them not (14:6-9)', law='F2 [INK 14:5-9]')]
    if k == 'glory_appeared_at_the_threat':
        return [E_('glory_appeared', 'the-tabernacle', cp='HEAVEN', value='at the stoning threat — the glory of the LORD appeared in the tent of meeting to all the children of Israel (14:10); the stones thrown upward (Sotah 35a:12)', law='F2 [INK 14:10; Lev 9:23 the first seat, Num 16:19, 17:7, 20:6 the rest]')]
    if k == 'moses_pleaded_on_the_attributes':
        return [E_('plea_made', 'moses', cp='HEAVEN', value='the offer refused a second time (14:12 = Exod 32:10); Egypt will hear (14:13); the attributes quoted back "as You have spoken" (14:17-18 — a subsequence of Exod 34:6-7); pardon, I pray (14:19)', law='F2 [INK 14:11-19; Berakhot 32a:27-31; Sanhedrin 111b:1]')]
    if k == 'pardoned_and_decreed':
        return [E_('pardoned', 'israel', cp='HEAVEN', value='I have pardoned according to your word (14:20 — once in the Bible); the rider: they shall not see the land (14:21-23)', law='F2 [INK 14:20-23; Berakhot 32a:29]'),
                E_('holding_owed', 'caleb', cp='HEAVEN', value='him I will bring into the land where he went, and his seed shall possess it (14:24) — Hebron: PAID at Josh 14:13-14; Moses\' oath there (Josh 14:9)', law='F2 [INK 14:24; Josh 14:6-14; Deut 1:36]'),
                E_('commanded', 'israel', value='the_turn_back', law='F2 [INK 14:25 "tomorrow turn and journey into the wilderness by the way of the Red Sea" — OPEN in this span: its run Num 21:4 (the same phrase), Deut 2:1]')]
    if k == 'decree_declared':
        return [E_('sentence_pronounced', 'israel', cp='HEAVEN', value='in this wilderness your carcasses shall fall — the census set %d (Bamidbar CALLED), from twenty and upward; Caleb and Joshua excepted; the children brought in; a day for a year (14:28-35)' % BM.TOTAL, law='F2 [INK 14:26-35; Mishnah Sanhedrin 1:6, 10:3; Bava Batra 121b:8-11]'),
                E_('carcasses_fall_in_the_wilderness', 'israel', cp='HEAVEN', due=world.clock.calendar.add(day, 38, 'year'), value='forty years, a day for a year (14:33-34) — thirty-eight from Kadesh to Zered by Deut 2:14\'s ink: due the ninth of Av of the fortieth year; the dying ceased on the fifteenth (Bava Batra 121a:9)', law='F2 [INK 14:33-34; Deut 2:14-16; Ezek 4:6]')]
    if k == 'ten_spies_died_by_plague':
        return [E_('put_to_death', event['subject'], cp='HEAVEN', value='died by the plague before the LORD (14:37) — the tongue to the navel (Sotah 35a:13); Joshua and Caleb lived (14:38)', law='F2 [INK 14:36-38; Arakhin 15a:13; Mishnah Sanhedrin 10:3]')]
    if k == 'presumed_to_go_up':
        return [E_('presumed_to_go_up', 'israel', value='mourned; rose early; the LORD is not among you; presumed to go up — the ark and Moses did not depart (14:39-44); Zelophehad among them (Shabbat 97a)', law='F2 [INK 14:39-44; Deut 1:41-43]')]
    if k == 'smitten_to_hormah':
        return [E_('defeated', 'israel', cp='amalek-and-the-canaanite', value='smitten and beaten down to Hormah (14:45) — the name used six chapters before its naming at 21:3', law='F2 [INK 14:45; Deut 1:44; Num 21:3; Judg 1:17]')]
    # ---- the exam's case kinds: each names LITERALLY every effect it can write (2b's form — an unnamed effect is a KeyError to read) ----
    if k == 'spies_case':
        v, e, _ = spies({'ask': event['ask']}, DATA); L = 'F1 [%s]' % v; s_ = event['person']
        W = {'accepted': E_('accepted', s_, value=v, law=L), 'disqualified': E_('disqualified', s_, value=v, law=L), 'plea_made': E_('plea_made', s_, value=v, law=L), 'evil_report_spread': E_('evil_report_spread', s_, value=v, law=L)}
        return [W[x] for x in e if x != FX.NONE]
    if k == 'decree_case':
        v, e, _ = decree({'ask': event['ask']}, DATA); L = 'F2 [%s]' % v; s_ = event['person']
        W = {'accepted': E_('accepted', s_, value=v, law=L), 'disqualified': E_('disqualified', s_, value=v, law=L), 'exempt': E_('exempt', s_, value=v, law=L), 'sentence_pronounced': E_('sentence_pronounced', s_, cp='HEAVEN', value=v, law=L),
             'put_to_death': E_('put_to_death', s_, cp='HEAVEN', value=v, law=L), 'holding_owed': E_('holding_owed', s_, value=v, law=L), 'wept': E_('wept', s_, value=v, law=L), 'pardoned': E_('pardoned', s_, value=v, law=L),
             'carcasses_fall_in_the_wilderness': E_('carcasses_fall_in_the_wilderness', s_, cp='HEAVEN', due=world.clock.calendar.add(day, 38, 'year'), value=v, law=L), 'commanded': E_('commanded', s_, value=v, law=L), 'presumed_to_go_up': E_('presumed_to_go_up', s_, value=v, law=L), 'defeated': E_('defeated', s_, value=v, law=L)}
        return [W[x] for x in e if x != FX.NONE]
    if k == 'libation_case':
        v, e, _ = libations({'ask': event['ask'], 'offering': event.get('offering'), 'where': event.get('where'), 'pair': event.get('pair', ('bull', 'ram')), 'logs': event.get('logs')}, DATA); L = 'F3 [%s]' % v; s_ = event['person']
        W = {'accepted': E_('accepted', s_, value=v, law=L), 'disqualified': E_('disqualified', s_, value=v, law=L), 'exempt': E_('exempt', s_, value=v, law=L), 'libation_owed': E_('libation_owed', s_, value=v, law=L)}
        return [W[x] for x in e if x != FX.NONE]
    if k == 'stranger_case':
        v, e, _ = stranger({'ask': event['ask']}, DATA); L = 'F4 [%s]' % v; s_ = event['person']
        W = {'accepted': E_('accepted', s_, value=v, law=L), 'disqualified': E_('disqualified', s_, value=v, law=L), 'exempt': E_('exempt', s_, value=v, law=L)}
        return [W[x] for x in e if x != FX.NONE]
    if k == 'challah_case':
        v, e, _ = challah({'ask': event['ask'], 'who': event.get('who', 'householder'), 'impure': event.get('impure'), 'grain': event.get('grain'), 'owner': event.get('owner', 'israelite'), 'direction': event.get('direction', 'in')}, DATA); L = 'F5 [%s]' % v; s_ = event['person']
        W = {'accepted': E_('accepted', s_, value=v, law=L), 'disqualified': E_('disqualified', s_, value=v, law=L), 'exempt': E_('exempt', s_, value=v, law=L), 'due_to_priest': E_('due_to_priest', s_, cp='the-priest', value=v, law=L)}
        return [W[x] for x in e if x != FX.NONE]
    if k == 'error_case':
        v, e, _ = error({'ask': event['ask'], 'knew_error': event.get('knew_error', False)}, DATA); L = 'F6 [%s]' % v; s_ = event['person']
        W = {'accepted': E_('accepted', s_, value=v, law=L), 'disqualified': E_('disqualified', s_, value=v, law=L), 'exempt': E_('exempt', s_, value=v, law=L), 'atoned_forgiven': E_('atoned_forgiven', s_, value=v, law=L)}
        return [W[x] for x in e if x != FX.NONE]
    if k == 'high_hand_case':
        v, e, _ = high_hand({'ask': event['ask'], 'intent': event.get('intent', 'intentional')}, DATA); L = 'F7 [%s]' % v; s_ = event['person']
        W = {'accepted': E_('accepted', s_, value=v, law=L), 'disqualified': E_('disqualified', s_, value=v, law=L), 'exempt': E_('exempt', s_, value=v, law=L), 'karet_cut_off': E_('karet_cut_off', s_, cp='HEAVEN', value=v, law=L), 'atoned_forgiven': E_('atoned_forgiven', s_, value=v, law=L)}
        return [W[x] for x in e if x != FX.NONE]
    return []


def scene():
    """THE SCENE — the exam's rows replayed on the world engine (the exodus epoch): the decree's set, the libation owed and refused, the
    convert's olah, the householder's twenty-fourth, the individual's she-goat, the high hand's karet."""
    with contextlib.redirect_stdout(io.StringIO()):
        w = WE.World(era='Num 13-15: Mishnah Sanhedrin 1, 10, Menachot 9, 12-13, Challah 1-4, Horayot 1-2, Keritot 1, Shekalim 7 and the Talmud\'s rows on the engine (the exodus epoch)', epoch='exodus')
        w.laws = [law_shelach]
        w.advance(w.clock.day_in('exodus', 2, 5, 9))
        w.submit({'kind': 'spies_case', 'subject': 'the-hushing-spy', 'person': 'the-hushing-spy', 'ask': 'caleb_hushed', 'case_source': 'Sotah 35a:3; Num 13:30 — persuaded them'})
        w.submit({'kind': 'decree_case', 'subject': 'the-generation-of-the-wilderness', 'person': 'the-generation-of-the-wilderness', 'ask': 'set', 'case_source': 'Bava Batra 121b:8; Num 14:29 — the census set (Bamidbar called)'})
        w.submit({'kind': 'decree_case', 'subject': 'the-spy-of-judah', 'person': 'the-spy-of-judah', 'ask': 'caleb_entitlement', 'case_source': 'Josh 14:13; Num 14:24 — Hebron owed'})
        w.submit({'kind': 'libation_case', 'subject': 'the-vowed-olah', 'person': 'the-vowed-olah', 'ask': 'takes', 'offering': 'olah', 'case_source': 'Mishnah Menachot 9:6; Num 15:3 — libations'})
        w.submit({'kind': 'libation_case', 'subject': 'the-firstborn-offering', 'person': 'the-firstborn-offering', 'ask': 'takes', 'offering': 'firstborn', 'case_source': 'Mishnah Menachot 9:6; Num 15:3 — no libations'})
        w.submit({'kind': 'libation_case', 'subject': 'the-five-log-pledge', 'person': 'the-five-log-pledge', 'ask': 'donated', 'logs': 5, 'case_source': 'Mishnah Menachot 12:4; Num 15:13 — no such libation'})
        w.submit({'kind': 'stranger_case', 'subject': 'the-convert', 'person': 'the-convert', 'ask': 'convert_offering', 'case_source': 'Keritot 8b:18; Num 15:14 — as you do'})
        w.submit({'kind': 'challah_case', 'subject': 'the-householder', 'person': 'the-householder', 'ask': 'measure', 'who': 'householder', 'case_source': 'Mishnah Challah 2:7; Num 15:20 — one twenty-fourth'})
        w.submit({'kind': 'error_case', 'subject': 'the-unwitting-idolater', 'person': 'the-unwitting-idolater', 'ask': 'individual', 'case_source': 'Mishnah Horayot 2:6; Num 15:27 — the she-goat (the chatat engine called)'})
        w.submit({'kind': 'high_hand_case', 'subject': 'the-high-handed', 'person': 'the-high-handed', 'ask': 'class', 'intent': 'intentional', 'case_source': 'Horayot 8a:14; Num 15:30 — karet (the chatat engine called)'})
    n = lambda eid, eff: len([e for e in w.entity(eid).ledger if e['effect'] == eff])
    return (n('the-hushing-spy', 'plea_made'), n('the-generation-of-the-wilderness', 'sentence_pronounced'), n('the-spy-of-judah', 'holding_owed'), n('the-vowed-olah', 'libation_owed'), n('the-firstborn-offering', 'exempt'),
            n('the-five-log-pledge', 'disqualified'), n('the-convert', 'accepted'), n('the-householder', 'due_to_priest'), n('the-unwitting-idolater', 'accepted'), n('the-high-handed', 'karet_cut_off'), len(w.entities)), w
SCENE, _W = scene()
SCENE_PREDICTED = (1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 10)   # PREDICTED from the design BEFORE the first run: one effect per row — the hushing spy's plea; the generation sentenced; Caleb's holding owed; the vowed olah's libation owed; the firstborn exempt; the five logs refused; the convert accepted; the householder's twenty-fourth due; the idolater's she-goat accepted; the high hand cut off; ten entities
assert SCENE == SCENE_PREDICTED, ('THE NUMBERS WALK: the Shelach scene moved from its prediction', SCENE, SCENE_PREDICTED)


def narrative():
    """THE NUMBERS WALK 4b (2026-09-10; NUMBERS_WALK.md "Sitting 4b"): the portion's own acts AS HISTORY — the seventeen lines of Num 13:1-14:45 in
    the text's order on a world with this runner's daemon, from the sending's day (2, 3, 29) (12:16's marker — Taanit 29a:5), the ONE
    reading-placed marker at 13:25 (2, 5, 9) the Ninth of Av, the forty days' timer firing the day after it (the inclusive count, CF2) on a
    closing walk, the thirty-eight years' timer left PENDING. Not a graded cell: the tuple below is a tripwire PREDICTED before the first run;
    the sequence world's RUN tuple grades the tape."""
    with contextlib.redirect_stdout(io.StringIO()):
        w = WE.World(era='Num 13-14: Shelach on the tape — the spies, the decree (the exodus epoch)', epoch='exodus')
        w.laws = [law_shelach]
        w.advance(w.clock.day_in('exodus', 2, 3, 29))
        w.submit({'kind': 'spies_commanded', 'subject': 'moses', 'one_per_tribe': True, 'princes': True, 'case_source': 'Num 13:1-2 — and the LORD spoke to Moses saying: send for yourself men that they may spy out the land of Canaan which I give to the children of Israel; one man, one man for his fathers\' tribe you shall send, every one a prince among them'})
        w.submit({'kind': 'spies_sent', 'subject': 'the-twelve-spies', 'names': SPY_TRIBES, 'renamed': 'Hoshea to Joshua', 'days': FORTY[0], 'case_source': 'Num 13:3-16 — and Moses sent them from the wilderness of Paran by the mouth of the LORD, all of them men, heads of the children of Israel... and Moses called Hoshea son of Nun Joshua'})
        w.submit({'kind': 'spies_instructed', 'subject': 'the-twelve-spies', 'questions': QUESTIONS, 'season': 'the days of the first-ripe grapes', 'case_source': 'Num 13:17-20 — and Moses sent them to spy out the land of Canaan and said to them: go up this way by the south and go up into the mountain; and see the land, what it is... and be strong and take of the fruit of the land; and the days were the days of the first-ripe grapes'})
        w.submit({'kind': 'spies_went_up', 'subject': 'the-twelve-spies', 'route': 'Zin to Rehob, the entrance of Hamath', 'hebron': DATA['hebron_visitor']['value'], 'giants': ['Ahiman', 'Sheshai', 'Talmai'], 'cluster': 'on a pole between two', 'eshcol': True, 'case_source': 'Num 13:21-24 — and they went up and spied out the land from the wilderness of Zin to Rehob, to the entrance of Hamath; and they went up by the south, and he came to Hebron... and they came to the wadi of Eshcol and cut from there a branch with one cluster of grapes, and they carried it on a pole between two'})
        w.marker('Num 13:25', w.clock.day_in('exodus', 2, 5, 9), value='and they returned from spying out the land at the end of forty days (13:25) — READING-PLACED by Taanit 29a:5 (the baraita: sent on the twenty-ninth of Sivan, returned on the Ninth of Av; "forty days minus one" — thirty-nine; Abaye: Tammuz full); Mishnah Ta\'anit 4:6 the decree\'s day', placement='reading_placed')
        w.submit({'kind': 'spies_returned', 'subject': 'the-twelve-spies', 'days': FORTY[0], 'to': 'Kadesh', 'case_source': 'Num 13:25-26 — and they returned from spying out the land at the end of forty days; and they went and came to Moses and to Aaron and to all the congregation of the children of Israel, to the wilderness of Paran, to Kadesh, and brought back word to them and to all the congregation, and showed them the fruit of the land'})
        w.submit({'kind': 'report_given', 'subject': 'the-twelve-spies', 'answers': 'fat; strong; fortified; the Anak; the map', 'case_source': 'Num 13:27-29 — and they told him and said: we came to the land where you sent us, and it also flows with milk and honey, and this is its fruit; but the people who dwell in the land are strong, and the cities are fortified, very great, and also the children of Anak we saw there; Amalek dwells in the land of the south...'})
        w.submit({'kind': 'caleb_hushed_the_people', 'subject': 'caleb', 'words': 'we shall surely go up and possess it, for we can surely prevail over it', 'case_source': 'Num 13:30 — and Caleb hushed the people toward Moses and said: we shall surely go up and possess it, for we can surely prevail over it'})
        w.submit({'kind': 'evil_report_spread', 'subject': 'the-ten-spies', 'slander': 'stronger than us; a land that eats its inhabitants', 'nephilim': True, 'case_source': 'Num 13:31-33 — but the men who went up with him said: we are not able to go up against the people, for they are stronger than us; and they brought out an evil report of the land which they had spied to the children of Israel... and there we saw the Nephilim... and we were in our own eyes as grasshoppers'})
        w.submit({'kind': 'congregation_wept', 'subject': 'israel', 'night': 'that night', 'murmur': 'would that we had died in Egypt or in this wilderness', 'head': 'let us appoint a head and return to Egypt', 'case_source': 'Num 14:1-4 — and all the congregation lifted up and gave their voice, and the people wept that night; and all the children of Israel murmured against Moses and against Aaron... and they said one to another: let us appoint a head and return to Egypt'})
        w.submit({'kind': 'joshua_and_caleb_pleaded', 'subject': 'joshua', 'fell': 'Moses and Aaron on their faces', 'rent': 'Joshua and Caleb their garments', 'words': 'the land is very very good; fear not the people of the land', 'case_source': 'Num 14:5-9 — and Moses and Aaron fell on their faces before all the assembly of the congregation of the children of Israel; and Joshua son of Nun and Caleb son of Jephunneh, of those who had spied out the land, rent their garments; and they said to all the congregation of the children of Israel: the land through which we passed to spy it out, the land is very very good'})
        w.submit({'kind': 'glory_appeared_at_the_threat', 'subject': 'the-tabernacle', 'threat': 'to stone them with stones', 'case_source': 'Num 14:10 — and all the congregation said to stone them with stones; and the glory of the LORD appeared in the tent of meeting to all the children of Israel'})
        w.submit({'kind': 'moses_pleaded_on_the_attributes', 'subject': 'moses', 'offer': 'I will make of you a greater nation', 'argument': 'Egypt will hear', 'attributes': ' '.join(N18), 'case_source': 'Num 14:11-19 — and the LORD said to Moses: how long will this people scorn Me... I will smite them with the pestilence and disinherit them, and make of you a greater and mightier nation than they; and Moses said to the LORD: then Egypt will hear... and now, I pray, let the power of my Lord be great, as You have spoken, saying: the LORD, long of anger and abundant in kindness... pardon, I pray, the iniquity of this people'})
        w.submit({'kind': 'pardoned_and_decreed', 'subject': 'israel', 'pardon': 'I have pardoned according to your word', 'ten_times': TEN[0], 'caleb': 'him I will bring into the land where he went', 'turn': 'tomorrow turn and journey by the way of the Red Sea', 'case_source': 'Num 14:20-25 — and the LORD said: I have pardoned according to your word; but as I live... all the men who have seen My glory... and have tried Me these ten times... shall not see the land... but My servant Caleb... him I will bring into the land where he went, and his seed shall possess it... tomorrow turn and journey into the wilderness by the way of the Red Sea'})
        w.submit({'kind': 'decree_declared', 'subject': 'israel', 'set': BM.TOTAL, 'exceptions': ['Caleb', 'Joshua'], 'years': FORTY_YEARS[0], 'day_for_year': DAY_YEAR, 'case_source': 'Num 14:26-35 — and the LORD spoke to Moses and to Aaron saying: how long shall I bear with this evil congregation... say to them: as I live, says the LORD, surely as you have spoken in My ears, so I will do to you: in this wilderness your carcasses shall fall, and all your counted by all your number, from twenty years old and upward... your sons shall be shepherds in the wilderness forty years... forty days, a day for a year, a day for a year'})
        w.submit({'kind': 'ten_spies_died_by_plague', 'subject': 'the-ten-spies', 'mode': DATA['spies_death_mode']['value'], 'survivors': ['Joshua', 'Caleb'], 'case_source': 'Num 14:36-38 — and the men whom Moses sent to spy out the land, who returned and made all the congregation murmur against him by bringing out an evil report of the land, those men who brought out the evil report of the land died by the plague before the LORD; but Joshua son of Nun and Caleb son of Jephunneh lived'})
        w.submit({'kind': 'presumed_to_go_up', 'subject': 'israel', 'mourned': True, 'warning': 'the LORD is not among you', 'ark_stayed': True, 'case_source': 'Num 14:39-44 — and Moses spoke these words to all the children of Israel, and the people mourned greatly; and they rose early in the morning and went up to the top of the mountain, saying: here we are, and we will go up to the place which the LORD said, for we have sinned; and Moses said: why do you transgress the mouth of the LORD?... and they presumed to go up to the top of the mountain, but the ark of the covenant of the LORD and Moses did not depart from the midst of the camp'})
        w.submit({'kind': 'smitten_to_hormah', 'subject': 'israel', 'by': 'the Amalekite and the Canaanite', 'to': 'Hormah', 'case_source': 'Num 14:45 — and the Amalekite and the Canaanite who dwelt in that mountain came down and smote them and beat them down to Hormah'})
        w.advance(w.clock.day_in('exodus', 2, 5, 15))     # a closing walk to the fifteenth of Av: the forty days' timer fires at (2, 5, 10); the thirty-eight years' stays pending
    n = lambda eid, eff: len([e for e in w.entity(eid).ledger if e['effect'] == eff])
    is_open = lambda eid, eff: [e.get('open') for e in w.entity(eid).ledger if e['effect'] == eff]
    L = lambda k: len([l for l in w.log if l[0] == k])
    ex = w.clock.eras['exodus']
    markers = [l for l in w.log if l[0] == 'MARKER']
    fires = [l for l in w.log if l[0] == 'TIMER-FIRE']
    return (n('moses', 'commanded'), is_open('moses', 'commanded'), n('moses', 'plea_made'),
            n('the-twelve-spies', 'sent_to_spy'), n('the-twelve-spies', 'spied_forty_days'), n('the-twelve-spies', 'commanded'), is_open('the-twelve-spies', 'commanded'), n('the-twelve-spies', 'report_given'),
            n('caleb', 'plea_made'), n('caleb', 'holding_owed'), is_open('caleb', 'holding_owed'), n('joshua', 'plea_made'),
            n('the-ten-spies', 'evil_report_spread'), n('the-ten-spies', 'put_to_death'),
            n('israel', 'wept'), n('israel', 'tested_the_lord'), n('israel', 'pardoned'), n('israel', 'commanded'), is_open('israel', 'commanded'), n('israel', 'sentence_pronounced'), n('israel', 'carcasses_fall_in_the_wilderness'), n('israel', 'presumed_to_go_up'), n('israel', 'defeated'),
            n('the-tabernacle', 'glory_appeared'),
            L('TIMER-SET'), L('TIMER-FIRE'), [ex.date(f[1]) for f in fires], len(markers), [m[2].get('retrograde') for m in markers], L('EVENT'), L('WRITE'), len(w.entities)), w


NARRATIVE, _WN = narrative()
NARRATIVE_PREDICTED = (1, [False], 1,
                       1, 1, 1, [False], 1,
                       2, 1, [True], 1,
                       1, 1,
                       1, 1, 1, 1, [True], 1, 1, 1, 1,
                       1,
                       2, 1, [(2, 5, 10)], 1, [False], 17, 22, 7)   # PREDICTED from the design BEFORE the first run (NUMBERS_WALK.md "Sitting 4b"): Moses' sending closed by 13:3 and his plea; the twelve sent, timed, questioned (closed by the report), reporting; Caleb's two pleas and his holding OPEN; Joshua's plea; the ten's report and death; Israel wept, tested the tenth time, pardoned, the turn back OPEN, sentenced, timed, presumed, defeated; the glory on the tent; TWO TIMERS set, ONE fired — the forty days at (2, 5, 10), the day after the return marker (the inclusive count, CF2); one forward marker; seventeen events; twenty-two writes (twenty-one at the lines + the fire's one); seven entities
assert NARRATIVE == NARRATIVE_PREDICTED, ('THE NUMBERS WALK: Shelach\'s narrative moved from its prediction', NARRATIVE, NARRATIVE_PREDICTED)
