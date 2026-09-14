

# ---- THE WRAP — the daemon, the scene, the narrative ------------------------------------------------------
def law_journeys(event, world):
    """Num 33:1-56 (cold_run_journeys.py F1-F5). given_at Num 33:50; installed_by boot — A LAW IN THE DIVINE VOICE SPOKEN IN THE PLAINS
    OF MOAB (the class named in the registry, the second pass decides). THREE TAPE LINES: the writing (33:1-2) — journeys_recorded on the
    people, its value THE LIST of forty-two; the departure retold with the judgments on the gods (33:3-4) — a STATUS on Egypt, the run of
    Exodus 12:12's first telling (the firstborn's plague OPEN: a burial is no removal); the command (33:50-56) — TWO DEBITS on Israel OPEN BY
    DESIGN (dispossess and possess; destroy the three objects), the lot's debit of 26:52-56 cited, not rewritten. No line for the stations
    (the list) or for 33:38-40 (the tape's 20:28 and 21:1). The exam's two case kinds dispatch to the cells with LITERAL effects per kind
    (2b's form — an unnamed effect is a KeyError)."""
    k, src = event['kind'], event['case_source']
    E_ = lambda eff, s, cp=None, amount=None, due=None, law='', value=None: {'effect': eff, 'subject': s, 'counterparty': cp, 'amount': amount, 'due': due, 'value': value if value is not None else True, 'source_law': law, 'case_source': src}
    day = event.get('day', world.clock.day)      # THE SEQUENTIAL RUN: the event's own day
    # ---- the three lines (page_order at the counter's day, no marker in the chapter) ----
    if k == 'journeys_written':
        return [E_('journeys_recorded', 'israel', value='%d places — %s' % (len(PLACES_EN), ', '.join(PLACES_EN)), law='F1 [INK 33:2 "and Moses wrote their goings out by their journeys by the mouth of the LORD" — THE FOUR WRITINGS (Exodus 24:4, Numbers 33:2, Deuteronomy 31:9, 31:22); the value THE LIST: forty-two places built from the DB (Rameses and forty-one camps; forty-two "journeyed" and forty-two "camped"), eighteen named nowhere else, eighteen with a first telling outside the chapter, seventeen with a witness on the tape — a retelling never writes a camp twice; the DATA row the_stations]')]
    if k == 'gods_judged_at_the_departure':
        return [E_('judgments_executed_on_their_gods', 'egypt_people', value='and on their gods the LORD executed judgments (33:4) — THE RUN OF EXODUS 12:12 ("on all the gods of Egypt I will execute judgments") recorded here alone, forty years on; Egypt burying every firstborn — the plague\'s aftermath, the entry OPEN', law='F2 [INK 33:3-4 — the date (1, 1, 15) = the exodus marker (a retelling\'s date a checkpoint); "on the morrow of the Passover" 33:3 and Joshua 5:11; "with a high hand" Exodus 14:8\'s; the perfect "executed judgments" ONE Bible seat, the future Exodus 12:12 and Ezekiel 25:11: Exodus narrates the firstborn and never the gods — the act\'s FIRST telling; a burial is not a removal (ten struck, four removed by CALL)]')]
    if k == 'dispossession_commanded':
        return [E_('commanded', 'israel', value='dispossess_the_inhabitants_and_possess_the_land', law='F5 [INK 33:52-53 "you shall drive out all the inhabitants of the land from before you … and you shall dispossess the land and dwell in it, for to you I have given the land to possess it" — OPEN BY DESIGN: its runs Joshua\'s (Sotah 34a:5 the crossing\'s purpose); the negative arm 33:55-56 run back reversed by Joshua 23:13 and Judges 2:3 (the DATA row negative_arm_outcome; Megillah 11a:13-14 Saul\'s Amalek and Haman); the class of Caleb\'s Hebron, the captives\' sentence and the crossing\'s debit]'),
                E_('commanded', 'israel', value='destroy_their_images', law='F5 [INK 33:52 "destroy all their figured stones, and all their molten images you shall destroy, and all their high places you shall demolish" — THE THREE OBJECTS the value\'s fields (the figured stone Leviticus 26:1\'s word, its ban UNCOMPILED — journeys → tochacha OWED; the molten image the calf\'s word, Exodus 34:17 and Leviticus 19:4 by CALL; the high places Leviticus 26:30\'s curse in the same verb — the Canaanites\', another sense than the private altar\'s eras); OPEN BY DESIGN: its runs Joshua\'s and Judges\', 2 Kings 23\'s the last; the lot of 33:54 CITES 26:52-56\'s open debit — no third write]')]
    # ---- the exam's case kinds: each names LITERALLY every effect it can write (2b's form) ----
    if k == 'journeys_case':
        fn = {'writing': the_heading_and_the_writing, 'departure': the_departure, 'stations': the_stations}.get(event.get('cell'), aarons_death_retold)
        v, e, _ = fn(dict(event, ask=event['ask']), DATA); L = '%s [%s]' % ({'writing': 'F1', 'departure': 'F2', 'stations': 'F3'}.get(event.get('cell'), 'F4'), v); s_ = event['person']
        W = {'journeys_recorded': E_('journeys_recorded', s_, value=v, law=L), 'accepted': E_('accepted', s_, value=v, law=L), 'exempt': E_('exempt', s_, value=v, law=L)}
        return [W[x] for x in e if x != FX.NONE]
    if k == 'dispossession_case':
        v, e, _ = the_command(dict(event, ask=event['ask']), DATA); L = 'F5 [%s]' % v; s_ = event['person']
        W = {'commanded': E_('commanded', s_, value=v, law=L), 'accepted': E_('accepted', s_, value=v, law=L), 'exempt': E_('exempt', s_, value=v, law=L)}
        return [W[x] for x in e if x != FX.NONE]
    return []


LINES = [
    ('Num 33:1-2 — these are the journeys of the children of Israel who went out of the land of Egypt by their hosts by the hand of Moses and Aaron; and Moses wrote their goings out by their journeys by the mouth of the LORD, and these are their journeys by their goings out', 'moses'),
    ('Num 33:3-4 — and they journeyed from Rameses in the first month, on the fifteenth day of the first month; on the morrow of the Passover the children of Israel went out with a high hand in the sight of all Egypt; and Egypt was burying those whom the LORD had struck among them, every firstborn; and on their gods the LORD executed judgments', 'egypt_people'),
    ('Num 33:50-56 — and the LORD spoke to Moses in the plains of Moab by the Jordan at Jericho, saying: speak to the children of Israel and say to them: when you pass over the Jordan into the land of Canaan, you shall drive out all the inhabitants of the land from before you, and destroy all their figured stones, and all their molten images you shall destroy, and all their high places you shall demolish; and you shall dispossess the land and dwell in it, for to you I have given the land to possess it; and you shall inherit the land by lot by your families — to the many you shall give more inheritance and to the few less; to whom the lot goes out, his it shall be; by the tribes of your fathers you shall inherit; but if you do not drive out the inhabitants of the land from before you, then those you leave of them shall be thorns in your eyes and pricks in your sides, and they shall harass you on the land in which you dwell; and it shall be that as I thought to do to them, I will do to you', 'israel'),
]
CLOSES = 'none — the gods\' judgment had no entry to close; the firstborn\'s plague stays open (a burial is no removal); the lot\'s debit (26:52-56) stays open, cited by 33:54'


def scene():
    """THE SCENE — the exam's rows replayed on the world engine (the exodus epoch): the exam's persons through the two case kinds."""
    with contextlib.redirect_stdout(io.StringIO()):
        w = WE.World(era='Num 33:1-56: the journeys on the shelf — Rosh Hashanah, Kiddushin, Megillah, Bava Batra, Seder Olam on the engine (the exodus epoch)', epoch='exodus')
        w.laws = [law_journeys]
        w.advance(w.clock.day_in('exodus', 40, 6, 1))
        # ---- the exam's persons through the two case kinds (LITERAL submits — the daemon gate parses no loop) ----
        w.submit({'kind': 'journeys_case', 'subject': 'the-era-new-year', 'person': 'the-era-new-year', 'cell': 'death', 'ask': 'the_era_new_year', 'case_source': 'Rosh Hashanah 2b:9 — the exam\'s row the_era_new_year'})
        w.submit({'kind': 'journeys_case', 'subject': 'the-morrow', 'person': 'the-morrow', 'cell': 'departure', 'ask': 'the_morrow', 'case_source': 'Kiddushin 37b:14 — the exam\'s row the_morrow'})
        w.submit({'kind': 'journeys_case', 'subject': 'the-manna', 'person': 'the-manna', 'cell': 'departure', 'ask': 'the_manna', 'case_source': 'Kiddushin 38a:3-4 — the exam\'s row the_manna'})
        w.submit({'kind': 'journeys_case', 'subject': 'the-seventh-of-adar', 'person': 'the-seventh-of-adar', 'cell': 'death', 'ask': 'moses_seventh_adar', 'case_source': 'Kiddushin 38a:5 — the exam\'s row moses_seventh_adar'})
        w.submit({'kind': 'journeys_case', 'subject': 'the-kiss', 'person': 'the-kiss', 'cell': 'death', 'ask': 'by_the_mouth_kiss', 'case_source': 'Bava Batra 17a:3 — the exam\'s row by_the_mouth_kiss'})
        w.submit({'kind': 'journeys_case', 'subject': 'the-retreat', 'person': 'the-retreat', 'cell': 'stations', 'ask': 'moseroth_seven', 'case_source': 'Seder Olam Rabbah 9:2 — the exam\'s row moseroth_seven'})
        w.submit({'kind': 'journeys_case', 'subject': 'the-camps-extent', 'person': 'the-camps-extent', 'cell': 'stations', 'ask': 'the_last_camp', 'case_source': 'Eruvin 55b:15 — the exam\'s row the_last_camp'})
        w.submit({'kind': 'journeys_case', 'subject': 'the-directional-ending', 'person': 'the-directional-ending', 'cell': 'stations', 'ask': 'directional_ending', 'case_source': 'Yevamot 13b:6 — the exam\'s row directional_ending'})
        w.submit({'kind': 'journeys_case', 'subject': 'the-left-by-day', 'person': 'the-left-by-day', 'cell': 'departure', 'ask': 'left_by_day', 'case_source': 'Berakhot 9a:25 — the exam\'s row left_by_day'})
        w.submit({'kind': 'journeys_case', 'subject': 'the-arad-identity', 'person': 'the-arad-identity', 'cell': 'death', 'ask': 'arad', 'case_source': 'Rosh Hashanah 3a:3 — the exam\'s row arad'})
        w.submit({'kind': 'dispossession_case', 'subject': 'the-crossings-purpose', 'person': 'the-crossings-purpose', 'ask': 'drive_out', 'case_source': 'Sotah 34a:5 — the exam\'s row drive_out'})
        w.submit({'kind': 'dispossession_case', 'subject': 'the-thorns', 'person': 'the-thorns', 'ask': 'negative_arm', 'case_source': 'Megillah 11a:13 — the exam\'s row negative_arm'})
        w.submit({'kind': 'dispossession_case', 'subject': 'the-figured-stone', 'person': 'the-figured-stone', 'ask': 'figured_stones', 'case_source': 'Megillah 22b:11 — the exam\'s row figured_stones'})
        w.submit({'kind': 'dispossession_case', 'subject': 'the-private-altar', 'person': 'the-private-altar', 'ask': 'private_altar_eras', 'case_source': 'Mishnah Zevachim 14:4 — the exam\'s row private_altar_eras'})
        w.submit({'kind': 'dispossession_case', 'subject': 'the-lot-arms', 'person': 'the-lot-arms', 'ask': 'the_lot_arms', 'case_source': 'Bava Batra 117a:2 — the exam\'s row the_lot_arms'})
        w.submit({'kind': 'dispossession_case', 'subject': 'the-held-before', 'person': 'the-held-before', 'ask': 'possess_and_dwell', 'case_source': 'Bava Batra 119a:1 — the exam\'s row possess_and_dwell'})
        w.submit({'kind': 'dispossession_case', 'subject': 'the-lot-and-urim', 'person': 'the-lot-and-urim', 'ask': 'the_lot_restated', 'case_source': 'Bava Batra 122a:3 — the exam\'s row the_lot_restated'})
    n = lambda eid, eff: len([e for e in w.entity(eid).ledger if e['effect'] == eff])
    tset = len([l for l in w.log if l[0] == 'TIMER-SET']); tfire = len([l for l in w.log if l[0] == 'TIMER-FIRE']); tcan = len([l for l in w.log if l[0] == 'TIMER-CANCEL'])
    return ((n('the-era-new-year', 'accepted'), n('the-morrow', 'accepted'), n('the-manna', 'accepted'), n('the-seventh-of-adar', 'accepted'), n('the-kiss', 'accepted'), n('the-retreat', 'accepted'), n('the-camps-extent', 'accepted'), n('the-directional-ending', 'accepted'), n('the-left-by-day', 'accepted'), n('the-arad-identity', 'accepted'),
             n('the-crossings-purpose', 'commanded'), n('the-thorns', 'accepted'), n('the-figured-stone', 'commanded'), n('the-private-altar', 'exempt'), n('the-lot-arms', 'accepted'), n('the-held-before', 'accepted'), n('the-lot-and-urim', 'accepted')),
            (tset, tfire, tcan, len(w.timers)),
            len(w.entities)), w
SCENE, _W = scene()
# THE PREDICTION (typed before the first run, NUMBERS_WALK.md "Sitting 13b"): every exam person written once — seventeen ones; no timer in the
# chapter (set 0, fired 0, cancelled 0, pending 0). ENTITIES: the exam's 17 persons alone (an entity is a written-on party; no counterparty written on).
SCENE_PREDICTED = ((1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1), (0, 0, 0, 0), 17)
assert SCENE == SCENE_PREDICTED, ('THE NUMBERS WALK: the scene moved from its prediction', SCENE, SCENE_PREDICTED)


def narrative():
    """THE NUMBERS WALK 13b (2026-09-12): the chapter's own acts AS HISTORY — the THREE lines of 33:1-56 at the counter's day (40, 6, 1),
    page-order after Gad and Reuben's twelve (32:1-42), on a world with this runner's daemon: 4 writes, no timer, no marker, two entities
    (israel and egypt_people — moses a subject with no write), no close. Recorded by the sequential run's recorder and stitched onto the tape.
    Not a graded cell: the tuple below is a tripwire typed from the design; the sequence world's RUN tuple and CZ1-CZ9 grade the tape."""
    with contextlib.redirect_stdout(io.StringIO()):
        w = WE.World(era='Num 33:1-56: the journeys on the tape — the writing, the departure with the judgments on the gods, the command (the exodus epoch)', epoch='exodus')
        w.laws = [law_journeys]
        w.advance(w.clock.day_in('exodus', 40, 6, 1))
        # THE DAEMON GATE READS LITERAL SUBMITS ONLY — the three lines typed out
        w.submit({'kind': 'journeys_written', 'subject': 'moses', 'count': 42, 'by_the_mouth_of_the_lord': True, 'first': 'Rameses', 'case_source': LINES[0][0]})
        w.submit({'kind': 'gods_judged_at_the_departure', 'subject': 'egypt_people', 'date': [1, 1, 15], 'morrow_of_the_passover': True, 'high_hand': True, 'burying': 'the_firstborn', 'case_source': LINES[1][0]})
        w.submit({'kind': 'dispossession_commanded', 'subject': 'israel', 'objects': ['figured_stones', 'molten_images', 'high_places'], 'lot': True, 'negative_arm': True, 'frame': 'and the LORD spoke to Moses in the plains of Moab', 'case_source': LINES[2][0]})
    writes = len([l for l in w.log if l[0] == 'WRITE'])
    closes = len([e for ent in w.entities.values() for e in ent.ledger if e.get('closed_by')])
    return (writes, len([l for l in w.log if l[0] == 'TIMER-SET']), len(w.entities), w.clock.eras['exodus'].date(w.clock.day)[1:], closes), w


NARRATIVE, _WN = narrative()
NARRATIVE_PREDICTED = (4, 0, 2, (6, 1), 0)   # NUMBERS_WALK.md "Sitting 13b": 4 writes (L1 1, L2 1, L3 2), no timer, TWO entities (israel, egypt_people — the written-on parties; moses a subject with no write), the counter's day (6, 1), no close
assert NARRATIVE == NARRATIVE_PREDICTED, ('THE NUMBERS WALK: the journeys\' narrative moved from its prediction', NARRATIVE, NARRATIVE_PREDICTED)


# =====================================================================
# Motion 2 — THE TEST DATA: the answer sheet's rows (the docket's LAW rows).
# =====================================================================
CASES = [
    # F1 — the heading and the writing
    ('Num 33:1 / 10:28 — the heading', lambda: the_heading_and_the_writing({'ask': 'heading'}, DATA), "these are the journeys of the children of Israel (33:1) — 10:28's four words; sixty-three headings in the Torah"),
    ('Num 33:1 — by their hosts', lambda: the_heading_and_the_writing({'ask': 'by_their_hosts'}, DATA), "by their hosts (33:1) — sixteen seats, all in Numbers"),
    ('Num 33:1 / Ps 77:21 — by the hand of Moses and Aaron', lambda: the_heading_and_the_writing({'ask': 'by_the_hand'}, DATA), "by the hand of Moses and Aaron (33:1) — Psalm 77:21 the phrase's other seat, observed"),
    ('Num 33:2 — the four writings', lambda: the_heading_and_the_writing({'ask': 'moses_wrote'}, DATA), "and Moses wrote (33:2) — the four writings: Exodus 24:4, Numbers 33:2, Deuteronomy 31:9, 31:22"),
    ('Num 33:2, 38 / Bava Batra 17a:3 — by the mouth of the LORD', lambda: the_heading_and_the_writing({'ask': 'by_the_mouth'}, DATA), "by the mouth of the LORD — twenty-one Bible seats; Moses wrote by it (33:2), Aaron went up by it (33:38), and died by it on the shelf (Bava Batra 17a:3)"),
    ('Num 33:2 — the chiasm', lambda: the_heading_and_the_writing({'ask': 'the_chiasm'}, DATA), "their goings out by their journeys, their journeys by their goings out (33:2) — the chiasm; 'their goings out' two Bible seats, 'by their journeys' four"),
    ('Num 33:2, 5-49 — the list as the writing\'s value', lambda: the_heading_and_the_writing({'ask': 'the_list'}, DATA), "the journeys recorded — forty-two places as the writing's value: Rameses and forty-one camps, eighteen named nowhere else, eighteen with a first telling, seventeen with a witness on the tape"),
    # F2 — the departure
    ('Num 33:3 / Exod 12:41 — the date is the marker', lambda: the_departure({'ask': 'the_date'}, DATA), "the fifteenth day of the first month (33:3) = (1, 1, 15) — the tape's exodus marker; a retelling's date is a checkpoint, never a second marker"),
    ('Num 33:3 / Josh 5:11; Kiddushin 37b:14-38a:2 — the morrow of the Passover', lambda: the_departure({'ask': 'the_morrow'}, DATA), "on the morrow of the Passover — 33:3 and Joshua 5:11 the phrase's two seats: the run's two ends on one date-word; the omer's arm and the manna's"),
    ('Berakhot 9a:25 — left by day', lambda: the_departure({'ask': 'left_by_day'}, DATA), "left by day (33:3) — redeemed at evening, went out by day (Berakhot 9a:25); the exodus story's by_day by CALL"),
    ('Num 33:3 / Exod 14:8; 15:30 by CALL — with a high hand', lambda: the_departure({'ask': 'high_hand'}, DATA), "with a high hand (33:3) — Exodus 14:8's posture at the same going out, 15:30's the high-hand sinner's; the shelach runner names 33:3"),
    ('Num 33:4 / Exod 12:29 by CALL — the burial', lambda: the_departure({'ask': 'the_burial'}, DATA), "Egypt was burying every firstborn (33:4) — the plague's aftermath: the firstborn's plague_struck entry stays open, a burial is no removal (ten struck, four removed)"),
    ('Num 33:4 / Exod 12:12 — the run of the judgments', lambda: the_departure({'ask': 'the_gods_judged'}, DATA), "on their gods the LORD executed judgments (33:4) — the run of Exodus 12:12 recorded here alone: a status on Egypt written forty years on, the act's first telling"),
    ('Kiddushin 38a:3-4 / Exod 16:13 by CALL — the manna', lambda: the_departure({'ask': 'the_manna'}, DATA), "the manna forty years less thirty days (Kiddushin 38a:3-4) — from (1, 2, 16), the tape's marker at Exodus 16:13, to the sixteenth of Nisan; the cakes of 33:3's fifteenth thirty days"),
    # F3 — the stations
    ('Num 33:3-49 — forty-two places', lambda: the_stations({'ask': 'forty_two'}, DATA), "forty-two places (33:3-49) — Rameses and forty-one camps: the first departure and the last camp each told twice"),
    ('Num 33:3-49 — the verbs', lambda: the_stations({'ask': 'the_verbs'}, DATA), "forty-two 'journeyed' and forty-two 'camped' — forty-one verses with both; 33:3 the journey alone, 33:49 the camp alone"),
    ('Exod 12:37-19:2 by CALL — the nine', lambda: the_stations({'ask': 'exodus_nine'}, DATA), "the exodus story's nine stations by CALL — Succoth to Sinai on the tape as statuses and markers; the itinerary's list their run citation"),
    ('Num 33:8 / Exod 15:22; 34:33 — Etham for Shur', lambda: the_stations({'ask': 'etham_for_shur'}, DATA), "the wilderness of Etham (33:8) for Exodus 15:22's Shur — each one seat; 'a way of three days' six Torah seats; Exodus 34:33's 'speaking with them' a homograph"),
    ('Num 33:6 / Exod 13:20 — one word added', lambda: the_stations({'ask': 'one_word_added'}, DATA), "33:6 is Exodus 13:20 with one word added — the itinerary retelling its first telling on the tokens"),
    ('Num 33:9 / Exod 15:27 — Elim', lambda: the_stations({'ask': 'elim'}, DATA), "Elim's twelve springs and seventy palms (33:9) word for word with Exodus 15:27 — [12, 70] at both"),
    ('Num 33:10-13 — unnamed in Exodus', lambda: the_stations({'ask': 'unnamed_in_exodus'}, DATA), "the Red Sea camp, Dophkah and Alush (33:10-13) — three stations Exodus never names"),
    ('Num 33:16-17 / 11:34-35 by CALL — Kibroth-hattaavah and Hazeroth', lambda: the_stations({'ask': 'kibroth_hazeroth'}, DATA), "Kibroth-hattaavah and Hazeroth (33:16-17) — chapter 11's graves and Hazeroth by CALL: the burial on the tape, the markers at (2, 3, 22) and (2, 3, 29)"),
    ('Num 33:18 / 12:16; 13:3, 26 — Rithmah', lambda: the_stations({'ask': 'rithmah_paran'}, DATA), "Rithmah (33:18) — Paran under another name: the spies' base of 12:16, 13:3, 13:26; the tape's marker at (2, 3, 29)"),
    ('Num 33:10-46 — the eighteen only here', lambda: the_stations({'ask': 'only_here'}, DATA), "eighteen stations named nowhere else — seventeen by lemma (Dophkah to Almon-diblathaim) and the Red Sea camp"),
    ('Num 33:20, 26, 27 — the common-word names', lambda: the_stations({'ask': 'common_word_names'}, DATA), "Libnah, Tahath, Terah (33:20, 26, 27) — three names whose lemma's other seats are another referent"),
    ('Num 33:30-38 / Deut 10:6-7; Seder Olam 9:2 by CALL — Moseroth seven before Hor', lambda: the_stations({'ask': 'moseroth_seven'}, DATA), "Moseroth seven camps before Mount Hor (33:30-37) — Deuteronomy 10:6's 'there Aaron died' at Moserah reconciled by the retreat of seven stations (Seder Olam Rabbah 9:2; the chukat runner's row)"),
    ('Num 33:36-37 / Gen 14:7 — Kadesh and Mount Hor', lambda: the_stations({'ask': 'kadesh_hor'}, DATA), "Kadesh and Mount Hor (33:36-37) — 'that is Kadesh' with Genesis 14:7 (three of the pair's five seats read 'it is holy': a homograph); the edge of Edom one seat; two Mount Hors by CALL"),
    ('Num 33:41-47 / 21:4-20; 32:34 by CALL — the last stations', lambda: the_stations({'ask': 'chapter_21'}, DATA), "the last stations against chapter 21 — Zalmonah and Punon only here; Oboth and Iye-abarim shared; 21:18-20's stations absent; Dibon Gad the Gad runner's own witness by CALL; the mountains of Abarim before Nebo"),
    ('Num 33:48-49 / Eruvin 55b:15; Yoma 75b:14 — the last camp', lambda: the_stations({'ask': 'the_last_camp'}, DATA), "the plains of Moab (33:48-49) — the last camp by CALL; from Beth-jeshimoth to Abel-shittim three parasangs on the shelf (Eruvin 55b:15; Yoma 75b:14)"),
    ('Num 33:46-47 / Yevamot 13b:6 — the directional ending', lambda: the_stations({'ask': 'directional_ending'}, DATA), "Diblathaimah (33:46-47) — the directional ending on the station's name (Yevamot 13b:6's example)"),
    ('the tape\'s camps against the list', lambda: the_stations({'ask': 'tape_matched'}, DATA), "the tape's camps against the list — twelve names matched (Succoth to the plains of Moab), five statuses not (Goshen, Shur, the Red Sea way, Mattanah to Pisgah, Shittim)"),
    # F4 — Aaron's death retold
    ('Num 33:38 / 20:28 by CALL — the date', lambda: aarons_death_retold({'ask': 'the_date'}, DATA), "Aaron died on (40, 5, 1) (33:38) — the tape's marker at 20:28, built from this verse; the ordinal reader's year and month"),
    ('Num 33:39 / Exod 7:7; Deut 34:7 — the age', lambda: aarons_death_retold({'ask': 'the_age'}, DATA), "Aaron 123 at his death (33:39) = Exodus 7:7's 83 + 40; Moses 120 = 80 + 40 — the brothers three years apart at both ends, the ink's checksum"),
    ('Num 33:38 / Exod 19:1; 1 Kgs 6:1; Rosh Hashanah 2b:7 — the era\'s stamps', lambda: aarons_death_retold({'ask': 'the_eras_stamps'}, DATA), "the era's three stamps — Exodus 19:1, Numbers 33:38, 1 Kings 6:1 (the 480th year): the shelf's own chain of proof (Rosh Hashanah 2b:7, 3a:11)"),
    ('Rosh Hashanah 2b:9, 3a:5 — the era\'s new year', lambda: aarons_death_retold({'ask': 'the_era_new_year'}, DATA), "the era's new year from the chapter's date — (40, 5, 1) and (40, 11, 1) in one year, (2, 1, 1) and (2, 2, 20) in one year on the Calendar: not Tishrei, not Iyar (Rosh Hashanah 2b:9, 3a:5)"),
    ('Rosh Hashanah 2b:11 / Deut 1:3 — the verbal analogy', lambda: aarons_death_retold({'ask': 'verbal_analogy'}, DATA), "the fortieth year / the fortieth year — Deuteronomy 1:3's bare date counted from the exodus by the verbal analogy with 33:38 (Rosh Hashanah 2b:11, taught); the two date readers meet"),
    ('Bava Batra 17a:3 by CALL — the kiss', lambda: aarons_death_retold({'ask': 'by_the_mouth_kiss'}, DATA), "by the mouth of the LORD at the death (33:38) — the kiss (Bava Batra 17a:3); the chukat runner's row death_by_the_kiss by CALL"),
    ('Kiddushin 38a:5-7; Seder Olam 10:2 by CALL — Moses\' seventh of Adar', lambda: aarons_death_retold({'ask': 'moses_seventh_adar'}, DATA), "Moses' seventh of Adar — computed backward from the tenth of Nisan (Kiddushin 38a:5-6); born and died the same day, a hundred and twenty exact (38a:7): Aaron's date the ink's, Moses' the shelf's"),
    ('Num 33:40 / 21:1 by CALL; Rosh Hashanah 3a:1-3 — Arad', lambda: aarons_death_retold({'ask': 'arad'}, DATA), "the Canaanite king of Arad heard (33:40) — 21:1's hearing alone, a run citation of the tape's line at (40, 5, 1); what he heard by CALL: that Aaron died and the clouds departed"),
    ('Rosh Hashanah 2b:13 — the order', lambda: aarons_death_retold({'ask': 'the_order'}, DATA), "the fortieth year's order — Aaron's death, Arad, the departure, Sihon: the tape's days in the shelf's order (Rosh Hashanah 2b:13)"),
    ('Num 33:38-40 — no write', lambda: aarons_death_retold({'ask': 'no_write'}, DATA), "no write for 33:38-40 — the death and the hearing are the tape's 20:28 and 21:1 lines, checkpointed, not rewritten"),
    # F5 — the command
    ('Num 33:50 / 35:1 — the frame', lambda: the_command({'ask': 'the_frame'}, DATA), "and the LORD spoke to Moses in the plains of Moab (33:50) — the chapter's one divine frame after forty-nine verses without one; 35:1 the second seat"),
    ('Num 33:51 / 35:10; Deut 11:31 — when you pass over', lambda: the_command({'ask': 'when_you_pass'}, DATA), "when you pass over the Jordan into the land of Canaan (33:51) — the law's trigger; 35:10 and Deuteronomy 11:31 the clause's kin"),
    ('Num 33:52-53 / Sotah 34a:5 — drive out', lambda: the_command({'ask': 'drive_out'}, DATA), "drive out all the inhabitants of the land (33:52-53) — a DEBIT on Israel OPEN BY DESIGN: its runs Joshua's; the crossing's purpose at the Jordan (Sotah 34a:5)"),
    ('Num 33:52 / Lev 26:1; Megillah 22b:11-13 — the figured stones', lambda: the_command({'ask': 'figured_stones'}, DATA), "their figured stones (33:52) — Leviticus 26:1's word at its ban's seat, uncompiled: the edge owed, Megillah 22b:11-13's rows filed to the debt"),
    ('Num 33:52 / Exod 34:17; Lev 19:4 by CALL — the molten images', lambda: the_command({'ask': 'molten_images'}, DATA), "their molten images (33:52) — the calf's word; the ban on making at Exodus 34:17 and Leviticus 19:4 by CALL (the erection and holiness runners)"),
    ('Num 33:52 / Lev 26:30; Mishnah Zevachim 14:4-8 — the high places', lambda: the_command({'ask': 'high_places'}, DATA), "their high places (33:52) — Leviticus 26:30's curse in the same verb on the same object: the spec/curse pair; the private altar's eras (Mishnah Zevachim 14:4-8) another sense"),
    ('Exod 34:13; Deut 7:5, 12:3 by CALL — the three objects the chapter\'s own', lambda: the_command({'ask': 'three_objects_own'}, DATA), "the three objects (33:52) are the chapter's own — the other iconoclasm lists (three, four, five by CALL) name altars, pillars, asherim and graven images"),
    ('Num 33:53 / Bava Batra 119a:1 by CALL — possess and dwell', lambda: the_command({'ask': 'possess_and_dwell'}, DATA), "possess the land and dwell in it, for to you I have given it (33:53) — the promise's gift read in the perfect; held before assignment by CALL; no second entry"),
    ('Num 33:54 / 26:52-56 by CALL — the lot restated', lambda: the_command({'ask': 'the_lot_restated'}, DATA), "the lot restated to the people (33:54) — 26:52-56 word for word with the verb's number switching inside the verse; the open debit cited by CALL, not rewritten"),
    ('Num 33:55-56 / Josh 23:13; Judg 2:3; Megillah 11a — the negative arm', lambda: the_command({'ask': 'negative_arm'}, DATA), "the negative arm (33:55-56) — thorns in your eyes and pricks in your sides, run back reversed by Joshua 23:13 and Judges 2:3; Saul's Amalek and Haman on the shelf (Megillah 11a); a data row, no verdict on the tape"),
    ('Bava Batra 117a-122a by CALL — the lot\'s arms', lambda: the_command({'ask': 'the_lot_arms'}, DATA), "the lot's arms — divided among those who left Egypt (the running setting), those who entered, or both; by lot and by the Urim: the second census's rows by CALL"),
    ('Mishnah Zevachim 14:4-8 — the private altar\'s eras', lambda: the_command({'ask': 'private_altar_eras'}, DATA), "the private altar's eras (Mishnah Zevachim 14:4-8) — Israel's own altars by era, the erection runner's block: not this chapter's high places"),
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
    print('THE INK: integers %s; ordinals %s; starred none; marked none; the frame verbs %s (the one divine frame)' % (sorted(INTS.items()), sorted(ORDS.items()), FRAME_VERBS))
    print('THE STATIONS: %d places; %d journeyed, %d camped; only here %d (%s + the Red Sea); Moseroth %d camps before Mount Hor; the tape\'s camps matched %d, unmatched %d' % (len(STATIONS), len(JOURNEYED), len(CAMPED), sum(1 for s in STATIONS if s['only_here']), len(ONLY_HERE), PLACES_EN.index('Mount Hor') - PLACES_EN.index('Moseroth'), len(TAPE_CAMPS_MATCHED), len(TAPE_CAMPS_UNMATCHED)))
    print('THE DATES: the departure %s = the exodus marker; the death %s = the marker at 20:28; Aaron %d = %d + %d; Moses %d = %d + %d; the era\'s year at Av and Shevat %s / %s' % (DEPARTURE_DATE, AARON_DATE, AGE, AARON_83, YEAR, MOSES_120, MOSES_80, YEAR, ERA_AV, ERA_SHEVAT))
    print('THE SCENE on the bench: %s; the timers (set, fired, cancelled, pending) %s; entities %d' % SCENE)
    print('THE NARRATIVE: %s' % (NARRATIVE,))
    print('THE PARAMETER ROWS: ' + '; '.join('%s = %s' % (k, (DATA[k]['value'] if k != 'the_stations' else '%d places (a data list)' % len(DATA[k]['value']))) for k in DATA) + ' (the other settings recorded in DATA)')
    if ok == len(CASES):
        print('\nTHE COMPILE OF THE JOURNEYS: the answer sheet REPRODUCED — %d/%d' % (ok, len(CASES)))
    sys.exit(0 if ok == len(CASES) else 1)
