

def scene():
    """THE SCENE — the exam's rows replayed on the world engine (the exodus epoch): the nazirite's term as a TIMER (set, cancelled by a
    defilement, re-set from the eighth day), the sotah's outcomes, the send-out's ladder, the theft's algebra, the blessing's who, the
    dedication's exceptions, the work-count's ages."""
    with contextlib.redirect_stdout(io.StringIO()):
        w = WE.World(era='Num 4:21-7:89: Mishnah Sotah, Nazir, Bava Kamma 9, Megillah 4, Kelim 1, Makkot 3 and the Talmud\'s rows on the engine (the exodus epoch)', epoch='exodus')
        w.laws = [law_naso]
        w.advance(w.clock.day_in('exodus', 2, 2, 1))
        w.submit({'kind': 'send_out_case', 'subject': 'the-leper-at-the-gate', 'person': 'the-leper-at-the-gate', 'who': 'leper', 'case_source': 'Num 5:2; Pesachim 67a:11 — the leper out of all three camps'})
        w.submit({'kind': 'send_out_case', 'subject': 'the-zav-at-the-mount', 'person': 'the-zav-at-the-mount', 'who': 'zav', 'case_source': 'Num 5:2; Pesachim 67a:12 — the zav out of two'})
        w.submit({'kind': 'send_out_case', 'subject': 'the-mourner-at-the-court', 'person': 'the-mourner-at-the-court', 'who': 'corpse_unclean', 'case_source': 'Num 5:2; Zevachim 117a — the corpse-unclean out of one'})
        w.submit({'kind': 'send_out_case', 'subject': 'the-impure-who-entered', 'person': 'the-impure-who-entered', 'who': 'zav', 'camp_entered': 'the_courtyard', 'case_source': 'Num 5:3; Makkot 14b:6; Mishnah Makkot 3:2 — the impure who entered the Temple'})
        w.submit({'kind': 'theft_confessed_case', 'subject': 'the-robber-of-the-proselyte', 'person': 'the-robber-of-the-proselyte', 'ask': 'proselyte_dead', 'value': 100, 'case_source': 'Num 5:8; Mishnah Bava Kamma 9:11 — the proselyte dead without heirs'})
        w.submit({'kind': 'theft_confessed_case', 'subject': 'the-robber-who-swore', 'person': 'the-robber-who-swore', 'ask': 'algebra', 'value': 100, 'victim': 'the-victim', 'case_source': 'Num 5:7; Lev 5:24 — the principal and the fifth (Lev 5\'s cell called)'})
        w.submit({'kind': 'theft_confessed_case', 'subject': 'the-son-who-robbed-his-father', 'person': 'the-son-who-robbed-his-father', 'ask': 'robbed_father', 'value': 100, 'victim': 'the-heirs', 'case_source': 'Num 5:7; Mishnah Bava Kamma 9:9 — robbed his father'})
        w.submit({'kind': 'gifts_case', 'subject': 'the-father-of-a-firstborn', 'person': 'the-father-of-a-firstborn', 'ask': 'firstborn_thirty', 'age_days': 31, 'case_source': 'Num 5:9-10; Sifrei 6:1; Bekhorot 49a — the firstborn\'s thirty days (Bamidbar called)'})
        w.submit({'kind': 'sotah_case', 'subject': 'the-guilty-wife', 'person': 'the-guilty-wife', 'ask': 'outcome', 'guilty': True, 'case_source': 'Num 5:27; Mishnah Sotah 3:4 — the guilty one drinks'})
        w.submit({'kind': 'sotah_case', 'subject': 'the-innocent-wife', 'person': 'the-innocent-wife', 'ask': 'outcome', 'guilty': False, 'case_source': 'Num 5:28 — cleared and sown with seed'})
        w.submit({'kind': 'sotah_case', 'subject': 'the-betrothed-warned', 'person': 'the-betrothed-warned', 'ask': 'status', 'who': 'betrothed', 'case_source': 'Num 5:29; Mishnah Sotah 4:1 — the betrothed neither drinks nor collects'})
        w.submit({'kind': 'sotah_case', 'subject': 'the-wife-with-witnesses-overseas', 'person': 'the-wife-with-witnesses-overseas', 'ask': 'witnesses_overseas', 'case_source': 'Num 5:13; Sotah 6a:10 — witnesses overseas'})
        w.submit({'kind': 'sotah_case', 'subject': 'the-wife-who-refused-late', 'person': 'the-wife-who-refused-late', 'ask': 'refuses', 'when': 'after_erasure', 'case_source': 'Num 5:27; Mishnah Sotah 3:3 — forced after the erasure'})
        w.submit({'kind': 'sotah_case', 'subject': 'the-wife-of-an-unclean-husband', 'person': 'the-wife-of-an-unclean-husband', 'ask': 'husband_clean', 'clean': False, 'case_source': 'Num 5:31; Kiddushin 27b:9 — the man not clear of iniquity'})
        d0 = w.clock.day
        w.submit({'kind': 'nazirite_case', 'subject': 'the-thirty-day-nazirite', 'person': 'the-thirty-day-nazirite', 'ask': 'vow', 'term': 30, 'case_source': 'Num 6:2; Mishnah Nazir 1:3, 3:1 — an unspecified naziriteship: thirty days'})
        w.submit({'kind': 'nazirite_case', 'subject': 'the-nazirite-defiled', 'person': 'the-nazirite-defiled', 'ask': 'vow', 'term': 30, 'case_source': 'Num 6:2 — a second nazirite, to be defiled on his twentieth day'})
        w.submit({'kind': 'nazirite_case', 'subject': 'the-nazirite-who-drank', 'person': 'the-nazirite-who-drank', 'ask': 'ate', 'product': 'wine', 'amount': 'quarter_log', 'case_source': 'Num 6:3; Mishnah Nazir 6:1 — a quarter-log of wine'})
        w.submit({'kind': 'nazirite_case', 'subject': 'the-nazirite-at-the-unburied', 'person': 'the-nazirite-at-the-unburied', 'ask': 'impurity_for', 'who': 'met_mitzvah', 'case_source': 'Num 6:7; Nazir 48a — the met mitzvah'})
        w.submit({'kind': 'nazirite_case', 'subject': 'the-leper-nazirite', 'person': 'the-leper-nazirite', 'ask': 'leper_nazirite_shaves', 'case_source': 'Num 6:5; Lev 14:9; Nazir 41a — the leper-nazirite shaves (the metzora engine called)'})
        w.submit({'kind': 'nazirite_case', 'subject': 'the-nazirite-completing', 'person': 'the-nazirite-completing', 'ask': 'foreleg', 'case_source': 'Num 6:19-20; Mishnah Nazir 6:9 — the foreleg on his palms (Tzav\'s cell called)'})
        w.advance(d0 + 20)
        w.submit({'kind': 'nazirite_case', 'subject': 'the-nazirite-defiled', 'person': 'the-nazirite-defiled', 'ask': 'defiled', 'term': 30, 'case_source': 'Num 6:9-12; Mishnah Nazir 6:6 — defiled on the twentieth day: the former days fall; the recount from the eighth'})
        w.advance(d0 + 31)
        fired_first = len([l for l in w.log if l[0] == 'TIMER-FIRE'])
        w.advance(d0 + 20 + 8 + 30)
        w.submit({'kind': 'blessing_case', 'subject': 'the-priest-with-blemished-hands', 'person': 'the-priest-with-blemished-hands', 'ask': 'who_blesses', 'who': 'blemished_hands', 'case_source': 'Num 6:23; Mishnah Megillah 4:7 — blemished hands (the priesthood\'s cell called)'})
        w.submit({'kind': 'blessing_case', 'subject': 'the-drunk-priest', 'person': 'the-drunk-priest', 'ask': 'who_blesses', 'who': 'drunk', 'case_source': 'Num 6:23; Taanit 26b:16 — the drunk priest'})
        w.submit({'kind': 'blessing_case', 'subject': 'the-priests-in-the-province', 'person': 'the-priests-in-the-province', 'ask': 'form', 'place': 'province', 'case_source': 'Num 6:23-27; Mishnah Sotah 7:6 — the blessing in the province'})
        w.submit({'kind': 'dedication_case', 'subject': 'the-princes-sabbath', 'person': 'the-princes-sabbath', 'ask': 'sabbath', 'case_source': 'Num 7:72, 7:78; Moed Katan 9a — the Sabbath overridden'})
        w.submit({'kind': 'dedication_case', 'subject': 'the-palgas-offered', 'person': 'the-palgas-offered', 'ask': 'animal_age', 'age_months': 13, 'case_source': 'Num 7:15; Mishnah Parah 1:3 — thirteen months: neither'})
        w.submit({'kind': 'work_count_case', 'subject': 'the-apprentice-levite', 'person': 'the-apprentice-levite', 'ask': 'fitness', 'who': 'levite', 'age': 27, 'carrying': True, 'case_source': 'Num 4:47; Chullin 24a:12 — twenty-seven: an apprentice (Bamidbar called)'})
        w.submit({'kind': 'work_count_case', 'subject': 'the-old-levite-at-shiloh', 'person': 'the-old-levite-at-shiloh', 'ask': 'fitness', 'who': 'levite', 'age': 55, 'carrying': False, 'case_source': 'Num 4:47; Chullin 24a:11 — not carrying: fit (Bamidbar called)'})
    n = lambda eid, eff: len([e for e in w.entity(eid).ledger if e['effect'] == eff])
    val = lambda eid, eff: [e.get('value') for e in w.entity(eid).ledger if e['effect'] == eff]
    L = lambda k: len([l for l in w.log if l[0] == k])
    return (val('the-leper-at-the-gate', 'sent_outside_the_camp'), val('the-zav-at-the-mount', 'sent_outside_the_camp'), val('the-mourner-at-the-court', 'sent_outside_the_camp'), n('the-impure-who-entered', 'lashes'),
            n('the-robber-of-the-proselyte', 'due_to_priest'), val('the-robber-who-swore', 'pays'), n('the-son-who-robbed-his-father', 'adds_fifth'), val('the-father-of-a-firstborn', 'pays'),
            n('the-guilty-wife', 'put_to_death'), n('the-innocent-wife', 'accepted'), n('the-betrothed-warned', 'ketubah_forfeited'), n('the-wife-with-witnesses-overseas', 'exempt'), n('the-wife-who-refused-late', 'tested_by_the_waters'), n('the-wife-of-an-unclean-husband', 'exempt'),
            n('the-thirty-day-nazirite', 'nazirite_term_fulfilled'), n('the-nazirite-defiled', 'count_voided'), n('the-nazirite-defiled', 'nazirite_term_fulfilled'), fired_first, L('TIMER-SET'), L('TIMER-CANCEL'), L('TIMER-FIRE'),
            n('the-nazirite-who-drank', 'lashes'), n('the-nazirite-at-the-unburied', 'count_voided'), n('the-leper-nazirite', 'accepted'), n('the-nazirite-completing', 'due_to_priest'),
            n('the-priest-with-blemished-hands', 'disqualified'), n('the-drunk-priest', 'disqualified'), n('the-priests-in-the-province', 'blessed_by_the_priests'), n('the-princes-sabbath', 'accepted'), n('the-palgas-offered', 'disqualified'),
            n('the-apprentice-levite', 'exempt'), n('the-old-levite-at-shiloh', 'appointed_to_serve'), len(w.entities)), w
SCENE, _W = scene()


def narrative():
    """THE NUMBERS WALK 2b (2026-09-10; NUMBERS_WALK.md "Sitting 2b"): the portion's own acts AS HISTORY — the eleven lines of Num 4:21-7:89 in
    the text's order on a world with this runner's daemon after Bamidbar's forward marker at 1:1 (2, 2, 1): the two counts commanded and the
    work-count (three closes — the third Bamidbar's Kohathite debit, absent on this bare world), the send-out commanded and run under the
    reading-placed retrograde marker at 5:1, the wagons and the dedication under 7:1's retrograde marker, THE SCHEDULE of 7:11 as twelve
    RETRO-WRITES, the Voice; recorded by the sequential run's recorder and stitched onto the tape (the fourteen markers the stitcher's rows).
    Not a graded cell: the tuple below is a tripwire typed from the first run's print; the sequence world's RUN tuple grades the tape."""
    with contextlib.redirect_stdout(io.StringIO()):
        w = WE.World(era='Num 4:21-7:89: Naso on the tape — the work-count, the send-out, the wagons, the dedication, the Voice (the exodus epoch)', epoch='exodus')
        w.laws = [law_naso]
        w.marker('Num 1:1', w.clock.day_in('exodus', 2, 2, 1), value='the census commanded (1:1) — Bamidbar\'s FORWARD marker, the context of every Naso date')
        w.submit({'kind': 'gershon_service_commanded', 'subject': 'the-levites', 'house': 'gershon', 'ages': [30, 50], 'burden': 'the soft: the curtains, the tent, its covering, the screens, the cords', 'under': 'ithamar', 'case_source': 'Num 4:21-28 — and the LORD spoke to Moses saying: lift the head of the sons of Gershon, them also... from thirty years old and upward until fifty... this is the service of the families of the Gershonites... in the hand of Ithamar'})
        w.submit({'kind': 'merari_service_commanded', 'subject': 'the-levites', 'house': 'merari', 'ages': [30, 50], 'burden': 'the hard: the frames, the bars, the pillars, the sockets, the pegs, the cords', 'by_names': True, 'under': 'ithamar', 'case_source': 'Num 4:29-33 — the sons of Merari by their families... you shall count them... and by names you shall appoint the vessels of the charge of their burden... in the hand of Ithamar'})
        w.submit({'kind': 'levites_work_counted', 'subject': 'the-levites', 'counts': dict(WORK), 'total': WORK_TOTAL, 'princes_joined': True, 'case_source': 'Num 4:34-49 — and Moses and Aaron and the princes of the congregation counted the sons of the Kohathite... their counted two thousand seven hundred and fifty... Gershon two thousand six hundred and thirty... Merari three thousand two hundred... all the counted eight thousand five hundred and eighty; by the mouth of the LORD by the hand of Moses'})
        w.marker('Num 5:1', w.clock.day_in('exodus', 2, 1, 1), value='the sending away of the impure — READING-PLACED on the day the tabernacle was erected (R. Levi, Gittin 60a:17): RETROGRADE', placement='reading_placed')
        w.submit({'kind': 'send_out_commanded', 'subject': 'israel', 'classes': ['leper', 'zav', 'corpse_unclean'], 'camps': 3, 'male_and_female': True, 'spoken_day': 'the first of Nisan (R. Levi)', 'case_source': 'Num 5:1-3 — and the LORD spoke to Moses saying: command the children of Israel that they send out of the camp every leper and everyone with an issue and everyone unclean by a corpse; male and female alike you shall send out, outside the camp, that they not defile their camps in whose midst I dwell'})
        w.submit({'kind': 'unclean_sent_out', 'subject': 'the-unclean-of-the-camp', 'classes': ['leper', 'zav', 'corpse_unclean'], 'as_spoken': True, 'case_source': 'Num 5:4 — and the children of Israel did so, and sent them out, outside the camp; as the LORD spoke to Moses, so did the children of Israel'})
        w.marker('Num 7:1', w.clock.day_in('exodus', 2, 1, 1), value='on the day Moses finished setting up the tabernacle (7:1) — the erection\'s day: RETROGRADE after 1:1')
        w.submit({'kind': 'wagons_brought', 'subject': 'the-princes-of-israel', 'wagons': WAGONS[0], 'oxen': WAGONS[1], 'per_prince': 'a wagon for two, an ox for one', 'day': 'the day Moses finished', 'case_source': 'Num 7:2-3 — and the princes of Israel, the heads of their fathers\' houses, they who stood over the counted, brought near; and they brought their offering before the LORD: six covered wagons and twelve oxen, a wagon for two princes and an ox for one, and they brought them before the tabernacle'})
        w.submit({'kind': 'wagons_accepted_commanded', 'subject': 'moses', 'from': 'the-princes-of-israel', 'to': 'the-levites', 'by_service': True, 'case_source': 'Num 7:4-5 — and the LORD said to Moses: take from them, and they shall be for the service of the tent of meeting, and give them to the Levites, each according to his service'})
        w.submit({'kind': 'wagons_assigned', 'subject': 'the-levites', 'gershon': DIST_G, 'merari': DIST_M, 'kohath': [0, 0], 'under': 'ithamar', 'case_source': 'Num 7:6-9 — and Moses took the wagons and the oxen and gave them to the Levites: two wagons and four oxen to the sons of Gershon, four wagons and eight oxen to the sons of Merari, in the hand of Ithamar; and to the sons of Kohath he gave none, for the service of the holy is upon them: on the shoulder they carry'})
        w.submit({'kind': 'dedication_brought', 'subject': 'the-princes-of-israel', 'day': 'the day it was anointed', 'before': 'the altar', 'case_source': 'Num 7:10 — and the princes brought near the dedication of the altar on the day it was anointed, and the princes brought near their offering before the altar'})
        w.submit({'kind': 'dedication_order_commanded', 'subject': 'the-princes-of-israel', 'per_day': 1, 'order': 'the camp\'s (2:3-31)', 'days': 12, 'case_source': 'Num 7:11 — and the LORD said to Moses: one prince per day, one prince per day, they shall bring near their offering for the dedication of the altar'})
        w.close('the-princes-of-israel', 'dedication_brought', 'Num 7:84-88 — this is the dedication of the altar on the day it was anointed: twelve dishes, twelve bowls, twelve pans... all the gold of the pans a hundred and twenty; the twelve days complete', value='the_dedication')
        w.submit({'kind': 'voice_heard_from_the_ark', 'subject': 'moses', 'reflexive': True, 'from': 'between the two cherubim', 'who_heard': 'moses alone', 'case_source': 'Num 7:89 — and when Moses came into the tent of meeting to speak with Him, he heard the Voice speaking itself to him from above the ark-cover that is upon the ark of the testimony, from between the two cherubim; and He spoke to him'})
    n = lambda eid, eff: len([e for e in w.entity(eid).ledger if e['effect'] == eff])
    is_open = lambda eid, eff: [e.get('open') for e in w.entity(eid).ledger if e['effect'] == eff]
    L = lambda k: len([l for l in w.log if l[0] == k])
    markers = [l for l in w.log if l[0] == 'MARKER']
    retro = [l for l in w.log if l[0] == 'RETRO-WRITE']
    return (n('the-levites', 'commanded'), is_open('the-levites', 'commanded'), n('the-levites', 'work_counted'), n('the-levites', 'wagons_assigned'),
            n('israel', 'commanded'), is_open('israel', 'commanded'), n('the-unclean-of-the-camp', 'sent_outside_the_camp'),
            n('moses', 'commanded'), is_open('moses', 'commanded'), n('moses', 'spoken_to_from_the_ark'),
            n('the-princes-of-israel', 'wagons_brought'), n('the-princes-of-israel', 'dedication_brought'), is_open('the-princes-of-israel', 'dedication_brought'),
            sum(n(t, 'dedication_offered') for t in PRINCE_TOKENS), L('RETRO-WRITE'), sorted(set(r[2].get('due') - w.clock.day_in('exodus', 2, 1, 1) for r in retro)),
            len(markers), [m[2].get('retrograde') for m in markers], L('EVENT'), L('WRITE'), len(w.entities)), w


NARRATIVE, _WN = narrative()
NARRATIVE_PREDICTED = (2, [False, False], 1, 1,
                       1, [False], 1,
                       1, [False], 1,
                       1, 1, [False],
                       12, 12, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
                       3, [False, True, True], 11, 10, 17)   # typed from the design's arithmetic BEFORE the first run: two count debits (closed by the work-count), the send-out's (closed), the wagons' (closed), the dedication's (closed by the scene's 7:84 line); twelve retro-writes at the anointing day + 0..11; three markers (1:1 forward, 5:1 and 7:1 retrograde); eleven events; ten WRITEs (the twelve dedication entries are RETRO-WRITEs); entities: the-levites, israel, the-unclean-of-the-camp, moses, the-princes-of-israel, the twelve = 17
assert NARRATIVE == NARRATIVE_PREDICTED, ('THE NUMBERS WALK: Naso\'s narrative moved from its prediction', NARRATIVE, NARRATIVE_PREDICTED)


# =====================================================================
# Motion 2 — THE TEST DATA: the answer sheet's rows (the docket's LAW rows).
# =====================================================================
CASES = [
    # F1 — the work-count
    ('Num 4:36-48 — the four work-counts summed (the parser on the ink)', lambda: work_count({'ask': 'counts'}, DATA), '2750 + 2630 + 3200 = 8580'),
    ('Num 4:36-48 against 3:22-34 — the shares (Bamidbar\'s houses CALLED)', lambda: work_count({'ask': 'shares'}, DATA), 'kohath 32, gershon 35, merari 52 of a hundred — the frame-carriers the largest share'),
    ('Num 4:47; Chullin 24a:12 — the ages (Bamidbar\'s table CALLED)', lambda: work_count({'ask': 'ages'}, DATA), 'thirty to fifty — 25 learn, 30 serve, 50 return'),
    ('Chullin 24a:12 — the apprentice of twenty-seven (Bamidbar\'s fitness CALLED)', lambda: work_count({'ask': 'fitness', 'who': 'levite', 'age': 27}, DATA), 'unfit — under thirty (twenty-five to apprentice)'),
    ('Chullin 24a:11 — fifty-five at Shiloh, not carrying', lambda: work_count({'ask': 'fitness', 'who': 'levite', 'age': 55, 'carrying': False}, DATA), 'fit — years disqualify only while carrying'),
    ('Arakhin 11a:17 — 4:47 the service of service', lambda: work_count({'ask': 'song'}, DATA), 'the service of service is the song (Arakhin 11a)'),
    ('Num 4:25-32; 7:9 — the three loads', lambda: work_count({'ask': 'loads'}, DATA), 'gershon the soft, merari the hard; kohath the holy (on the shoulder)'),
    ('Num 4:28, 4:33, 4:16 — under whose hand', lambda: work_count({'ask': 'under'}, DATA), 'Gershon and Merari under Ithamar; Kohath under Eleazar'),
    ('Num 4:37, 4:41, 4:45, 4:49 — the formula and its variant', lambda: work_count({'ask': 'formula'}, DATA), 'by the mouth of the LORD by the hand of Moses at 4:37, 4:45, 4:49; by the mouth of the LORD at 4:41'),
    ('Num 4:34, 4:46 — the princes among the counters', lambda: work_count({'ask': 'princes'}, DATA), 'the princes counted with Moses and Aaron (4:34, 4:46)'),
    # F2 — the camp's purity
    ('Num 5:2 — the three classes', lambda: camp_purity({'ask': 'classes'}, DATA), 'the leper, the zav, the corpse-unclean — three classes'),
    ('Pesachim 67a:11; Mishnah Kelim 1:7 — the leper (the negaim engine CALLED)', lambda: camp_purity({'ask': 'ladder', 'who': 'leper'}, DATA), 'out of all three camps (Israel, Levi, the Presence)'),
    ('Pesachim 67a:12; Mishnah Kelim 1:8 — the zav (the clocks engine CALLED)', lambda: camp_purity({'ask': 'ladder', 'who': 'zav'}, DATA), 'out of two (Levi and the Presence)'),
    ('Zevachim 117a:1 — the corpse-unclean (the heifer OWED FORWARD)', lambda: camp_purity({'ask': 'ladder', 'who': 'corpse_unclean'}, DATA), 'out of one (the Presence)'),
    ('Zevachim 116b; Mishnah Kelim 1:7-8 — the three camps (Bamidbar CALLED)', lambda: camp_purity({'ask': 'three_camps'}, DATA), 'israel: the walls to the mount; levites: the mount to nicanor; presence: the courtyard'),
    ('Eruvin 104b:10 — the purifiable is sent', lambda: camp_purity({'ask': 'who_is_sent', 'what': 'purifiable'}, DATA), 'sent — has a purification (Eruvin 104b)'),
    ('Eruvin 104b:10 — a creeping thing\'s carcass', lambda: camp_purity({'ask': 'who_is_sent', 'what': 'creeping_carcass'}, DATA), 'not sent — no purification (Eruvin 104b)'),
    ('Niddah 28b:1 — the tumtum', lambda: camp_purity({'ask': 'who_is_sent', 'what': 'tumtum'}, DATA), 'not liable — male and female (Niddah 28b)'),
    ('Makkot 14b:6; Mishnah Makkot 3:2 — the impure who entered', lambda: camp_purity({'ask': 'entered_impure'}, DATA), 'lashes (5:3 the prohibition, 19:13 the punishment)'),
    ('Pesachim 67a:7 / 67a:11 — the leper beyond his boundary', lambda: camp_purity({'ask': 'leper_entered'}, DATA), 'a dispute: exempt (Rav Chisda) / liable (R. Yehuda\'s tanna)'),
    ('Pesachim 67b:8, 95b:14 — the Passover in impurity', lambda: camp_purity({'ask': 'impure_pesach', 'majority_impure': True}, DATA), 'zavim and lepers not liable to karet (R. Eliezer)'),
    ('Pesachim 67b:8 — the majority pure', lambda: camp_purity({'ask': 'impure_pesach', 'majority_impure': False}, DATA), 'liable to karet (the corpse-unclean sent)'),
    ('Pesachim 92a:15 — the tevul yom and the Passover', lambda: camp_purity({'ask': 'tevul_yom_pesach'}, DATA), 'may enter — the Passover\'s karet overrides (Pesachim 92a)'),
    ('Taanit 21b:5 — the tent rolled up (Bamidbar\'s tent CALLED)', lambda: camp_purity({'ask': 'tent_rolled_up'}, DATA), 'the place unsacred — the Presence, not the ground (Taanit 21b)'),
    ('Sifrei 1:1 — the warning for 19:20', lambda: camp_purity({'ask': 'warning'}, DATA), 'the warning for 19:20\'s punishment (Sifrei 1:1)'),
    ('Gittin 60a:17 — the day the section was said', lambda: camp_purity({'ask': 'day'}, DATA), 'the first of Nisan — R. Levi\'s eight sections (Gittin 60a:17): reading-placed'),
    ('Sifrei 1:8 — the run doubled', lambda: camp_purity({'ask': 'run_doubled'}, DATA), 'before the calf no zavim; after — the doubling (Sifrei 1:8)'),
    # F3 — the theft's restitution and the gifts
    ('Num 5:7; Mishnah Sanhedrin 6:2 — the confession', lambda: restitution({'ask': 'confession'}, DATA), 'confess (the executed confess — Sanhedrin 6:2)'),
    ('Bava Kamma 110a:12-17 — the principal', lambda: restitution({'ask': 'principal'}, DATA), 'at its head — the principal, not the double'),
    ('Bava Metzia 54a; Sifrei 3:1 — the fifth\'s base (the running setting)', lambda: restitution({'ask': 'fifth'}, DATA), 'a quarter added = a fifth of the whole (Bava Metzia 54a)'),
    ('Lev 5:24 CALLED — the algebra for a hundred', lambda: restitution({'ask': 'algebra', 'value': 100}, DATA), 'pay its value; add the fifth (25.00); ram at the valuation floor'),
    ('Mishnah Bava Kamma 9:7 — the fifth on the fifth (Lev 5\'s cell CALLED)', lambda: restitution({'ask': 'algebra', 'value': 100, 'swore_on_fifth': True}, DATA), 'pay its value; add the fifth (25.00); fifth on the fifth, to the perutah floor; ram at the valuation floor'),
    ('Bava Kamma 111a:11; Mishnah 9:12 — the order', lambda: restitution({'ask': 'order'}, DATA), 'the money first, then the ram (Bava Kamma 111a; Mishnah 9:12)'),
    ('Bava Kamma 109a:5; Arakhin 28b:1; Mishnah 9:11 — the proselyte dead', lambda: restitution({'ask': 'proselyte_dead'}, DATA), 'to the priests of the watch (5:8; Arakhin 28b)'),
    ('Mishnah Bava Kamma 9:11 — the robber died on the way', lambda: restitution({'ask': 'robber_died_before'}, DATA), 'the money to his children; the ram grazes, sold for communal gifts (Mishnah 9:11)'),
    ('Mishnah Bava Kamma 9:12 — given to the watch then died', lambda: restitution({'ask': 'given_then_died'}, DATA), 'the heirs cannot reclaim — 5:10 (Mishnah 9:12)'),
    ('Mishnah Bava Kamma 9:12 — the fifth missing', lambda: restitution({'ask': 'fifth_not_precluding'}, DATA), 'the fifth missing does not preclude the ram (Mishnah 9:12)'),
    ('Bava Kamma 15a:4 — the equating rule', lambda: restitution({'ask': 'woman_equals_man'}, DATA), 'a woman equals a man for all punishments (5:6 — Bava Kamma 15a)'),
    ('Sifrei 4:2 — the priest-thief', lambda: restitution({'ask': 'priest_thief'}, DATA), 'the priest-thief does not keep it (Sifrei 4:2)'),
    ('Mishnah Bava Kamma 9:5 — to whom', lambda: restitution({'ask': 'to_whom'}, DATA), 'to the victim himself, even to Media; not his son or agent (Mishnah 9:5)'),
    ('Mishnah Bava Kamma 9:6 — the remainder', lambda: restitution({'ask': 'remainder'}, DATA), 'pursue for the principal, not for the fifth; a perutah the floor (Mishnah 9:6)'),
    ('Mishnah Bava Kamma 9:9 — robbed his father', lambda: restitution({'ask': 'robbed_father'}, DATA), 'to the father\'s sons or brothers; forfeits his share; the ram (Mishnah 9:9)'),
    ('Bava Kamma 106a:16 — confessed after the oath', lambda: restitution({'ask': 'confessed_after_oath'}, DATA), 'principal and fifth even where the oath would exempt (Bava Kamma 106a)'),
    ('Bava Kamma 109b:3 — the female proselyte', lambda: restitution({'ask': 'proselyte_female'}, DATA), 'an open dilemma (Bava Kamma 109b:3)'),
    ('Num 5:9-10; Arakhin 34a:6 — the owner\'s choice', lambda: restitution({'ask': 'owners_choice'}, DATA), 'the owner\'s choice of priest; the priest\'s own offering his'),
    ('Mishnah Terumot 4:5 — the terumah\'s measure', lambda: restitution({'ask': 'terumah_measure'}, DATA), 'the owner\'s measure, with a floor: some must remain non-sacred (Mishnah Terumot 4:5)'),
    ('Bava Kamma 109b:16 — the blemished priest\'s own offering', lambda: restitution({'ask': 'blemished_priests_offering'}, DATA), 'flesh and hide his (Bava Kamma 109b:16)'),
    ('Sifrei 6:1; Bekhorot 49a — the firstborn after thirty days (Bamidbar CALLED)', lambda: restitution({'ask': 'firstborn_thirty', 'age_days': 31}, DATA), 'after thirty days'),
    ('Bekhorot 49a — before thirty days (Bamidbar CALLED)', lambda: restitution({'ask': 'firstborn_thirty', 'age_days': 20}, DATA), 'not yet — before thirty days'),
    ('Onkelos 5:10 — the tithe inserted', lambda: restitution({'ask': 'tithe_inserted'}, DATA), 'the tithe Onkelos inserts at 5:10'),
    # F4 — the suspected wife
    ('Num 5:13 — the six conditions', lambda: sotah({'ask': 'conditions'}, DATA), 'six: lain with, hidden, secreted, defiled, no witness, not seized'),
    ('Sotah 2a:12; Mishnah 6:3 — one witness for defilement', lambda: sotah({'ask': 'witnesses', 'what': 'defilement'}, DATA), 'one witness suffices (5:13)'),
    ('Mishnah Sotah 1:1 — two for the warning', lambda: sotah({'ask': 'witnesses', 'what': 'warning'}, DATA), 'two (R. Yehoshua; the mishnah)'),
    ('Sotah 2b:10 — the seclusion (the running setting)', lambda: sotah({'ask': 'witnesses', 'what': 'seclusion'}, DATA), 'two (R. Yehoshua) — R. Eliezer one'),
    ('Sotah 4a:9 — the measure of seclusion (the running setting)', lambda: sotah({'ask': 'secluded'}, DATA), 'the time for the first stage of intercourse — the returning of a palm (R. Eliezer)'),
    ('Mishnah Sotah 4:1; Kiddushin 27b:7 — the betrothed', lambda: sotah({'ask': 'status', 'who': 'betrothed'}, DATA), 'neither drinks nor collects (5:29 under her husband)'),
    ('Mishnah Sotah 4:1 — the widow awaiting the levir', lambda: sotah({'ask': 'status', 'who': 'awaiting_levir'}, DATA), 'neither drinks nor collects (5:29 under her husband)'),
    ('Mishnah Sotah 4:1 — a forbidden marriage', lambda: sotah({'ask': 'status', 'who': 'forbidden_marriage'}, DATA), 'neither drinks nor collects (a forbidden marriage)'),
    ('Sotah 25b:3; Mishnah 4:3 — the ailonit', lambda: sotah({'ask': 'status', 'who': 'ailonit'}, DATA), 'neither (the Rabbis; R. Elazar: drinks)'),
    ('Sotah 26a:11; Mishnah Eduyot 5:6 — the convert', lambda: sotah({'ask': 'status', 'who': 'convert'}, DATA), 'drinks (the Sages; Akavya recorded)'),
    ('Mishnah Sotah 4:4; Sotah 26a:12 — the priest\'s wife', lambda: sotah({'ask': 'status', 'who': 'priests_wife'}, DATA), 'drinks; cleared she is permitted'),
    ('Mishnah Sotah 4:4; Sotah 26a:15 — the eunuch\'s wife', lambda: sotah({'ask': 'status', 'who': 'eunuchs_wife'}, DATA), 'drinks'),
    ('Mishnah Sotah 4:3 — pregnant or nursing', lambda: sotah({'ask': 'status', 'who': 'pregnant_or_nursing'}, DATA), 'the Rabbis: drinks; R. Meir: neither'),
    ('Kiddushin 27b:9; Sotah 28a:1 — the husband not clean', lambda: sotah({'ask': 'husband_clean', 'clean': False}, DATA), 'the waters do not test — the man not clear of iniquity (5:31)'),
    ('Sotah 24b:2; Yevamot 58a:14 — the husband first', lambda: sotah({'ask': 'husband_first'}, DATA), 'only when the husband\'s cohabitation preceded (5:20)'),
    ('Ketubot 81a:6; Mishnah 4:2 — the husband died (the running setting)', lambda: sotah({'ask': 'husband_dead'}, DATA), 'Beit Hillel: no drink, no ketubah'),
    ('Mishnah Sotah 4:4; Sotah 26b:1 — warned about a relative', lambda: sotah({'ask': 'warned_about', 'who': 'relative'}, DATA), 'valid'),
    ('Sotah 26b:6 — warned about a gentile', lambda: sotah({'ask': 'warned_about', 'who': 'gentile'}, DATA), 'valid'),
    ('Sotah 26b:2 — warned about a minor', lambda: sotah({'ask': 'warned_about', 'who': 'minor'}, DATA), 'no warning'),
    ('Sotah 24a:10 — the warning\'s scope', lambda: sotah({'ask': 'warning_scope'}, DATA), 'the betrothed and the shomeret yavam can be warned, not tested'),
    ('Mishnah Sotah 4:5; Sotah 27a:7 — the court warns', lambda: sotah({'ask': 'court_warns'}, DATA), 'to disqualify the ketubah (the Sages); R. Yosei: to drink too'),
    ('Sotah 6a:10 — witnesses overseas', lambda: sotah({'ask': 'witnesses_overseas'}, DATA), 'not tested — witnesses exist overseas'),
    ('Keritot 24a:9 — conspiring witnesses', lambda: sotah({'ask': 'witnesses_conspiring'}, DATA), 'her minchah non-sacred'),
    ('Mishnah Sotah 6:1 — the rumor', lambda: sotah({'ask': 'rumor'}, DATA), 'R. Eliezer: divorce with the ketubah; R. Yehoshua: not until the spinners'),
    ('Mishnah Sotah 6:2 — a slave\'s testimony', lambda: sotah({'ask': 'witness_of_defilement', 'who': 'slave'}, DATA), 'believed — bars the ketubah'),
    ('Mishnah Sotah 6:2 — the mother-in-law\'s', lambda: sotah({'ask': 'witness_of_defilement', 'who': 'mother_in_law'}, DATA), 'believed only to bar the drinking'),
    ('Mishnah Sotah 6:4 — one against one', lambda: sotah({'ask': 'contradicting', 'for': 1, 'against': 1}, DATA), 'drinks'),
    ('Mishnah Sotah 6:4 — two against one', lambda: sotah({'ask': 'contradicting', 'for': 2, 'against': 1}, DATA), 'does not drink, divorced'),
    ('Sotah 7a:10; Mishnah 1:3 — the escort', lambda: sotah({'ask': 'escort'}, DATA), 'two scholars (rabbinic; R. Yehuda: trusted)'),
    ('Sotah 7b:3; Mishnah 1:4 — the court', lambda: sotah({'ask': 'court'}, DATA), 'the Sanhedrin of seventy-one (torah/torah)'),
    ('Mishnah Sotah 1:4 — the admonition', lambda: sotah({'ask': 'admonition'}, DATA), 'wine, levity, immaturity, bad neighbors; act for the great Name'),
    ('Mishnah Sotah 1:5 — she confesses', lambda: sotah({'ask': 'confesses'}, DATA), 'a receipt for the ketubah; divorced'),
    ('Sotah 8a:2; Mishnah 1:5 — the place', lambda: sotah({'ask': 'place'}, DATA), 'the Nicanor gate — before the LORD'),
    ('Sotah 8a:10; Mishnah 1:5-6 — the uncovering', lambda: sotah({'ask': 'uncovering'}, DATA), 'the head, the body, the hair unbraided; black garments; the Egyptian rope; the adornments removed'),
    ('Mishnah Sotah 2:1; Menachot 59a:5 — the minchah\'s form (the minchah engine CALLED)', lambda: sotah({'ask': 'minchah_form'}, DATA), 'barley, unsifted; no oil, no frankincense — as the sinner\'s: neither'),
    ('Onkelos 5:15 — the ephah as three se\'ah', lambda: sotah({'ask': 'ephah'}, DATA), 'a tenth of an ephah = a tenth of three se\'ah (Onkelos)'),
    ('Num 5:26 — the fistful (the minchah engine CALLED)', lambda: sotah({'ask': 'fistful'}, DATA), 'the scoop level — the meal-offering engine: overflowing or fingertips invalid'),
    ('Kiddushin 36b:4; Mishnah 3:1 — the waving', lambda: sotah({'ask': 'waving'}, DATA), 'by her hand and the priest\'s together (hand/hand with Lev 7:30)'),
    ('Menachot 60b:6; Mishnah Menachot 5:6 — bringing near', lambda: sotah({'ask': 'bringing_near'}, DATA), 'required (5:25 draw it near)'),
    ('Menachot 4a:8 — not for its name', lambda: sotah({'ask': 'minchah_not_for_its_name'}, DATA), 'disqualified; the surplus to communal gifts'),
    ('Mishnah Sotah 2:2; Temurah 12b:6 — the water and the dust', lambda: sotah({'ask': 'water_and_dust'}, DATA), 'half a log from the laver (R. Yehuda a quarter); the dust from the Sanctuary floor, visible on the water; water first (R. Shimon: either)'),
    ('Sotah 15b:4 — the vessel', lambda: sotah({'ask': 'vessel'}, DATA), 'a new earthenware vessel (R. Yishmael)'),
    ('Sotah 20a:4 — the bitter substance', lambda: sotah({'ask': 'bitter_added'}, DATA), 'a bitter substance in the water'),
    ('Mishnah Sotah 2:3 — the scroll\'s text', lambda: sotah({'ask': 'scroll_text'}, DATA), 'from 5:19 through 5:22\'s curses, without the frame and the amens (the Rabbis); R. Yosei whole; R. Yehuda curses alone'),
    ('Mishnah Sotah 2:4; Eruvin 13a:10 — the scroll\'s material and ink', lambda: sotah({'ask': 'scroll_material'}, DATA), 'a scroll (parchment); erasable ink; no iron sulfate'),
    ('Sotah 17b:3 — by day', lambda: sotah({'ask': 'scroll_time'}, DATA), 'by day'),
    ('Sotah 17b:4 — the order', lambda: sotah({'ask': 'scroll_order'}, DATA), 'the Torah\'s order'),
    ('Sotah 17b:5 — before the oath', lambda: sotah({'ask': 'scroll_before_oath'}, DATA), 'unfit'),
    ('Sotah 18a:2 — the erasure', lambda: sotah({'ask': 'scroll_erasure'}, DATA), 'written whole, erased at once'),
    ('Eruvin 13b:2; Sotah 20b:6 — for her name', lambda: sotah({'ask': 'for_her_name'}, DATA), 'the erasure for her name; the writing not'),
    ('Sotah 32b:2; Mishnah 7:1 — the language', lambda: sotah({'ask': 'language'}, DATA), 'any language'),
    ('Sanhedrin 32b:18 — the oath\'s order', lambda: sotah({'ask': 'oath_order'}, DATA), 'the innocent clause first'),
    ('Sotah 18a:8 — two oaths', lambda: sotah({'ask': 'oaths_count'}, DATA), 'two: before and after the erasure'),
    ('Mishnah Sotah 2:5; Kiddushin 27b:6 — amen, amen', lambda: sotah({'ask': 'amen_amen'}, DATA), 'on the curse and the oath; this man and another; betrothed, married, awaiting the levir, married to the levir'),
    ('Shevuot 29b:9 — amen is an oath', lambda: sotah({'ask': 'amen_is_oath'}, DATA), 'amen = her oath (Shmuel)'),
    ('Shevuot 35b:23 — the oath\'s form', lambda: sotah({'ask': 'oath_form'}, DATA), 'a curse, in the Name'),
    ('Mishnah Sotah 2:6 — the oath\'s scope', lambda: sotah({'ask': 'oath_scope'}, DATA), 'only acts that would forbid her'),
    ('Keritot 9b:10 — several warnings', lambda: sotah({'ask': 'several_warnings'}, DATA), 'one meal-offering (jealousies)'),
    ('Mishnah Sotah 3:2; Sotah 19a — the order of drinking and offering (the running setting)', lambda: sotah({'ask': 'order'}, DATA), 'drink then offer (the Rabbis); R. Shimon offer then drink; either valid after the fact'),
    ('Sotah 19b:2 — R. Shimon\'s three preconditions', lambda: sotah({'ask': 'preconditions'}, DATA), 'R. Shimon: the fistful offered, the scroll erased, the oath accepted'),
    ('Mishnah Sotah 3:3 — refuses before the erasure', lambda: sotah({'ask': 'refuses', 'when': 'before_erasure'}, DATA), 'the scroll sequestered, the minchah burned; not forced'),
    ('Mishnah Sotah 3:3; Sotah 19b:1 — refuses after the erasure', lambda: sotah({'ask': 'refuses', 'when': 'after_erasure'}, DATA), 'forced to drink'),
    ('Mishnah Sotah 3:3 — confesses after the erasure', lambda: sotah({'ask': 'refuses', 'when': 'confesses_after_erasure'}, DATA), 'the water poured out, the minchah scattered'),
    ('Mishnah Megillah 2:5 — the time', lambda: sotah({'ask': 'time'}, DATA), 'by day, the whole day'),
    ('Sotah 8a:4; Nedarim 73a:7 — two at once', lambda: sotah({'ask': 'two_at_once'}, DATA), 'not together'),
    ('Mishnah Sotah 3:4, 1:7 — the guilty outcome', lambda: sotah({'ask': 'outcome', 'guilty': True}, DATA), 'her face greens, her belly swells, her thigh falls — she dies; the paramour too'),
    ('Mishnah Sotah 3:4; Sotah 20b:14 — merit suspends (the running setting)', lambda: sotah({'ask': 'outcome', 'guilty': True, 'merit': True}, DATA), 'suspended (three, nine, twelve months — the Sifrei; one to three years — the mishnah; R. Shimon none)'),
    ('Num 5:28; Sotah 26a:7-8 — the innocent outcome', lambda: sotah({'ask': 'outcome', 'guilty': False}, DATA), 'cleared and sown with seed (the barren conceives — R. Akiva; R. Yishmael: ease)'),
    ('Mishnah Sotah 5:1 — the paramour tested', lambda: sotah({'ask': 'paramour_tested'}, DATA), 'tested too (5:24, 5:27)'),
    ('Sotah 28a:19, 29a:2 — the consequences', lambda: sotah({'ask': 'defiled_consequences'}, DATA), 'forbidden to her husband, her paramour, the priesthood and terumah (R. Akiva)'),
    ('Sotah 28a:21; Mishnah 1:2 — the doubt forbids', lambda: sotah({'ask': 'doubt_forbids'}, DATA), 'forbidden to her husband until clarified'),
    ('Yevamot 11a:10 — the levirate', lambda: sotah({'ask': 'levirate'}, DATA), 'exempt from levirate and chalitzah (Yevamot 11a)'),
    ('Mishnah Sotah 3:6 — the confessed one\'s minchah', lambda: sotah({'ask': 'minchah_disposition', 'case': 'confessed'}, DATA), 'burned (once in a service vessel; redeemed if before)'),
    ('Mishnah Sotah 3:7 — a priest\'s daughter married to an Israelite', lambda: sotah({'ask': 'minchah_disposition', 'case': 'priests_daughter_to_israelite'}, DATA), 'eaten'),
    ('Sotah 27a:10-27b:1 — the blind, the lame, the mute', lambda: sotah({'ask': 'disabled', 'who': 'blind'}, DATA), 'neither side drinks or gives to drink'),
    ('Ketubot 51b:13 — raped', lambda: sotah({'ask': 'intercourse', 'consent': 'raped'}, DATA), 'permitted to her husband'),
    ('Yevamot 56b:7 — the priest\'s wife raped', lambda: sotah({'ask': 'intercourse', 'consent': 'raped', 'who': 'priests_wife'}, DATA), 'forbidden (the priest\'s wife)'),
    ('Sotah 18b:15 — drinks twice', lambda: sotah({'ask': 'drinks_twice'}, DATA), 'drinks again for a second warning'),
    ('Mishnah Sotah 9:9; Sotah 47b — the abolition (the tape runs the rite)', lambda: sotah({'ask': 'abolished'}, DATA), 'the rite runs (the ink); abolished by Rabban Yochanan ben Zakkai — Hosea 4:14 (the tradition\'s setting)'),
    ('Sotah 3a:17 — the warning permitted', lambda: sotah({'ask': 'warning_permitted'}, DATA), 'permitted (R. Eliezer b. Yaakov); optional or obligatory disputed'),
    ('Kiddushin 62a:2; Sotah 3a:4 — the spellings the teacher re-reads (measured)', lambda: sotah({'ask': 'spelling'}, DATA), 'hinnaki without the yod read also as chinnaki; tisteh read as folly — the ink measured'),
    # F5 — the nazirite
    ('Nedarim 3a:5; Mishnah Nazir 1:1 — a substitute', lambda: nazirite({'ask': 'vow_form', 'form': 'substitute'}, DATA), 'binds (nazir lehazir)'),
    ('Mishnah Nazir 1:2 — a partial vow', lambda: nazirite({'ask': 'vow_form', 'form': 'partial'}, DATA), 'a full nazirite'),
    ('Mishnah Nazir 1:1 — "birds"', lambda: nazirite({'ask': 'vow_form', 'form': 'birds'}, DATA), 'the Sages: not (R. Meir: a nazirite)'),
    ('Mishnah Nazir 2:3 — the cup', lambda: nazirite({'ask': 'vow_form', 'form': 'from_the_cup'}, DATA), 'a nazirite; the drunk woman\'s a konam'),
    ('Mishnah Nazir 2:4 — on condition to drink', lambda: nazirite({'ask': 'vow_form', 'form': 'conditioned_on_wine'}, DATA), 'a full nazirite'),
    ('Mishnah Nazir 2:4 — thought the Sages would permit', lambda: nazirite({'ask': 'vow_form', 'form': 'mistaken_sages_permit'}, DATA), 'free (R. Shimon bound)'),
    ('Mishnah Nazir 2:1; Nazir 9a:2 — from figs', lambda: nazirite({'ask': 'vow_form', 'form': 'figs'}, DATA), 'Beit Hillel: not (Shammai: a nazirite)'),
    ('Mishnah Nazir 1:2 — like Samson', lambda: nazirite({'ask': 'vow_form', 'form': 'samson'}, DATA), 'a Samson-nazirite: never shaves, no impurity offering'),
    ('Nedarim 5b:5 — an ambiguous intimation', lambda: nazirite({'ask': 'vow_form', 'form': 'ambiguous_intimation'}, DATA), 'Rava: not'),
    ('Mishnah Nazir 5:5; Nazir 34a:1 — the uncertain vow', lambda: nazirite({'ask': 'vow_form', 'form': 'uncertain'}, DATA), 'Hillel: whose statement failed; R. Tarfon none'),
    ('Nazir 61a:7; Mishnah 9:1 — a gentile', lambda: nazirite({'ask': 'who_vows', 'who': 'gentile'}, DATA), 'no naziriteship'),
    ('Mishnah Nazir 9:1 — a slave', lambda: nazirite({'ask': 'who_vows', 'who': 'slave'}, DATA), 'yes (the master forces)'),
    ('Niddah 46a:2; Mishnah Niddah 5:6 — a boy of thirteen and a day', lambda: nazirite({'ask': 'who_vows', 'who': 'boy', 'age': 13}, DATA), 'valid (thirteen and a day)'),
    ('Mishnah Niddah 5:6 — a boy of twelve', lambda: nazirite({'ask': 'who_vows', 'who': 'boy', 'age': 12}, DATA), 'examined (the twelfth year)'),
    ('Mishnah Nazir 1:3; Nazir 5a:16 — the unspecified term (the data row)', lambda: nazirite({'ask': 'term', 'form': 'unspecified'}, DATA), '30 days'),
    ('Mishnah Nazir 1:3 — "and a day"', lambda: nazirite({'ask': 'term', 'form': 'and_a_day'}, DATA), '60 days (two terms)'),
    ('Mishnah Nazir 1:3 — thirty days and an hour', lambda: nazirite({'ask': 'term', 'form': 'thirty_and_an_hour'}, DATA), '31 days'),
    ('Mishnah Nazir 1:4 — like the hairs of my head', lambda: nazirite({'ask': 'term', 'form': 'like_the_hairs'}, DATA), 'forever, shaving every thirty (Rebbi: one term)'),
    ('Mishnah Nazir 1:6 — from here to a place forty days off', lambda: nazirite({'ask': 'term', 'form': 'distance', 'days': 40}, DATA), '40 days'),
    ('Mishnah Nazir 1:7 — the solar year', lambda: nazirite({'ask': 'term', 'form': 'solar_year'}, DATA), '365 terms'),
    ('Mishnah Nazir 3:1 — the shaving day', lambda: nazirite({'ask': 'shaving_day', 'form': 'unspecified'}, DATA), 'the thirty-first (the thirtieth fulfilled)'),
    ('Mishnah Nazir 3:2 — two terms', lambda: nazirite({'ask': 'shaving_day', 'form': 'two_terms'}, DATA), '31 and 61 (30 and 60; 59 fulfilled)'),
    ('Mishnah Nazir 6:1 — a quarter-log of wine', lambda: nazirite({'ask': 'ate', 'product': 'wine', 'amount': 'quarter_log'}, DATA), 'lashes'),
    ('Mishnah Nazir 6:1; Nazir 38b:1 — less than a quarter-log', lambda: nazirite({'ask': 'ate', 'product': 'wine', 'amount': 'less_than_a_quarter_log'}, DATA), 'exempt (R. Akiva: an olive\'s bulk with bread)'),
    ('Nazir 34b:7 — leaves (the running setting)', lambda: nazirite({'ask': 'ate', 'product': 'leaves'}, DATA), 'permitted (the Rabbis; R. Elazar forbids)'),
    ('Nazir 35b:12 — a permitted mixture', lambda: nazirite({'ask': 'ate', 'product': 'mixture'}, DATA), 'combines — liable (soaked)'),
    ('Nazir 38b:4 / Pesachim 41b:5 — a seed', lambda: nazirite({'ask': 'ate', 'product': 'seed'}, DATA), 'lashes (Rava one set; Abaye two)'),
    ('Mishnah Nazir 6:2 — R. Elazar b. Azarya\'s measure', lambda: nazirite({'ask': 'ate', 'product': 'two_seeds_one_skin'}, DATA), 'R. Elazar b. Azarya\'s measure — liable'),
    ('Nazir 4a:3, 44a:9 — mitzvah wine', lambda: nazirite({'ask': 'mitzvah_wine'}, DATA), 'forbidden like optional'),
    ('Pesachim 23a:5 — benefit from wine', lambda: nazirite({'ask': 'benefit_from_wine'}, DATA), 'permitted (his naziriteship)'),
    ('Mishnah Nazir 6:3 — scissors', lambda: nazirite({'ask': 'shaving_means', 'means': 'scissors'}, DATA), 'liable'),
    ('Nazir 39b:5-6 — plucked any amount', lambda: nazirite({'ask': 'shaving_means', 'means': 'plucked_any'}, DATA), 'R. Yoshiya liable (R. Yonatan exempt)'),
    ('Mishnah Nazir 6:3 — shampooing', lambda: nazirite({'ask': 'shaving_means', 'means': 'shampoo'}, DATA), 'permitted; combing not'),
    ('Nazir 44a:17 — shaved by another', lambda: nazirite({'ask': 'shaved_by_another'}, DATA), 'both liable'),
    ('Nazir 42a:3 — the shaving\'s amount', lambda: nazirite({'ask': 'shaving_amount'}, DATA), 'all the hair'),
    ('Nazir 40a — the final shaving\'s tool', lambda: nazirite({'ask': 'final_shaving_tool'}, DATA), 'a razor'),
    ('Mishnah Nazir 7:2 — a half-log of blood', lambda: nazirite({'ask': 'impurity_kinds', 'source': 'half_log_blood'}, DATA), 'shaves'),
    ('Mishnah Nazir 7:2 — a barley-grain bone by tent', lambda: nazirite({'ask': 'impurity_kinds', 'source': 'barley_grain_bone', 'mode': 'tent'}, DATA), 'not — the barley-grain bone does not defile by tent'),
    ('Mishnah Nazir 7:3-4 — a quarter-log of blood (the halakhah from Sinai)', lambda: nazirite({'ask': 'impurity_kinds', 'source': 'quarter_log_blood'}, DATA), 'not (a halakhah to Moses from Sinai — R. Akiva\'s a-fortiori refused)'),
    ('Mishnah Nazir 7:3 — the land of the nations', lambda: nazirite({'ask': 'impurity_kinds', 'source': 'land_of_nations'}, DATA), 'not — sprinkled, no negation'),
    ('Nazir 48a:1 — their leprosy', lambda: nazirite({'ask': 'impurity_kinds', 'source': 'leprosy'}, DATA), 'not corpse impurity — no negation; the days count'),
    ('Pesachim 80b:15 — a creeping thing', lambda: nazirite({'ask': 'impurity_kinds', 'source': 'creeping'}, DATA), 'not — only the corpse'),
    ('Zevachim 100a:6 — a relative on the way to the Passover', lambda: nazirite({'ask': 'impurity_for', 'who': 'relative'}, DATA), 'not — even on the way to the Passover'),
    ('Nazir 48a; Yevamot 7a:3 — the met mitzvah', lambda: nazirite({'ask': 'impurity_for', 'who': 'met_mitzvah'}, DATA), 'becomes impure — even on the way to the Passover'),
    ('Mishnah Nazir 7:1 — with the High Priest', lambda: nazirite({'ask': 'met_mitzvah_with_high_priest'}, DATA), 'the nazirite becomes impure (the Rabbis); R. Eliezer the priest'),
    ('Nazir 42b:1 — the impurity\'s lashes', lambda: nazirite({'ask': 'impurity_lashes'}, DATA), 'a set per distinct ban (the corpse and the enclosure); repeated impurity one set'),
    ('Mishnah Makkot 3:7 — drinking all day', lambda: nazirite({'ask': 'lashes_count', 'warnings': 0}, DATA), '1 set(s) — one, or one per warning'),
    ('Mishnah Makkot 3:7 — three warnings', lambda: nazirite({'ask': 'lashes_count', 'warnings': 3}, DATA), '3 set(s) — one, or one per warning'),
    ('Mishnah Nazir 6:5, 7:2 — impurity negates', lambda: nazirite({'ask': 'what_negates', 'act': 'impurity', 'day': 15, 'term': 30}, DATA), 'all — recount after purification and offerings'),
    ('Mishnah Nazir 3:3 — impure on the thirtieth', lambda: nazirite({'ask': 'what_negates', 'act': 'impurity', 'day': 30, 'term': 30}, DATA), 'all (R. Eliezer seven)'),
    ('Mishnah Nazir 3:4 — the hundredth day', lambda: nazirite({'ask': 'what_negates', 'act': 'impurity', 'day': 100, 'term': 100}, DATA), 'all (R. Eliezer thirty)'),
    ('Mishnah Nazir 3:4 — the hundred and first', lambda: nazirite({'ask': 'what_negates', 'act': 'impurity', 'day': 101, 'term': 100}, DATA), 'thirty (R. Eliezer seven)'),
    ('Nazir 19b:2-5 — impure on the second day', lambda: nazirite({'ask': 'what_negates', 'act': 'impurity', 'day': 2, 'term': 30}, DATA), 'nothing — no first days (two)'),
    ('Mishnah Nazir 6:3, 6:5 — shaving negates', lambda: nazirite({'ask': 'what_negates', 'act': 'shaving'}, DATA), 'thirty'),
    ('Nazir 44a:11 — wine negates', lambda: nazirite({'ask': 'what_negates', 'act': 'wine'}, DATA), 'nothing'),
    ('Nazir 63a:4; Mishnah 9:2 — the depths', lambda: nazirite({'ask': 'what_negates', 'act': 'unknown_impurity'}, DATA), 'nothing (the depths)'),
    ('Mishnah Nazir 3:5; Nazir 18a:2 — vowed in a cemetery', lambda: nazirite({'ask': 'vowed_in_cemetery'}, DATA), 'the days do not count; no shaving, no birds; re-entered: counts and brings'),
    ('Mishnah Nazir 6:6; Keritot 2b:5 — the defiled nazirite\'s week (the running setting)', lambda: nazirite({'ask': 'defiled'}, DATA), 'sprinkled the third and seventh, shaves the seventh, brings the eighth (a lamb asham, two birds); intentional as unwitting; the recount from the eighth'),
    ('Mishnah Kinnim 1:1, 2:5 — the birds', lambda: nazirite({'ask': 'birds'}, DATA), 'one chatat, one olah; not mixed'),
    ('Mishnah Nazir 6:7-8 — the completion (the offering engine CALLED)', lambda: nazirite({'ask': 'completion'}, DATA), 'three animals — the sin, the burnt, the peace; shaves after the peace-offering (R. Yehuda; R. Elazar the sin); any one suffices'),
    ('Nazir 45a:13; Yoma 16a:2 — where he shaves', lambda: nazirite({'ask': 'where_shaves'}, DATA), 'where the peace-offering is cooked — the Chamber of the Nazirites (Abba Chanan: while the entrance is open)'),
    ('Mishnah Nazir 6:8; Menachot 91b:1 — the hair under the pot', lambda: nazirite({'ask': 'hair_under_pot'}, DATA), 'under the peace-offering\'s pot (the others fulfill)'),
    ('Temurah 34a:4 — the impure nazirite\'s hair', lambda: nazirite({'ask': 'hair_under_pot', 'which': 'impurity'}, DATA), 'not thrown; the hair buried (the pure\'s burned)'),
    ('Kiddushin 57b:6; Avodah Zarah 74a:3 — the hair', lambda: nazirite({'ask': 'hair'}, DATA), 'holy — forbidden for benefit in any amount; burned'),
    ('Mishnah Menachot 7:2, 3:6; Menachot 46b, 91a — the loaves', lambda: nazirite({'ask': 'loaves'}, DATA), 'loaves and wafers (no poached), ten kav; both indispensable; sanctified by the ram\'s slaughter; with libations for the burnt- and peace-offerings'),
    ('Num 6:19-20; Mishnah 6:9 — the foreleg (Tzav\'s cell CALLED)', lambda: nazirite({'ask': 'foreleg'}, DATA), 'the cooked foreleg, a loaf and a wafer on his palms, waved (the woman too); beside the breast and thigh to the priests after the smoking'),
    ('Mishnah Chullin 10:4 — the foreleg\'s bounds', lambda: nazirite({'ask': 'foreleg_bounds'}, DATA), 'the lower knee joint to the thigh bone\'s protrusion (Mishnah Chullin 10:4)'),
    ('Zevachim 55a:6 — who eats the ram', lambda: nazirite({'ask': 'ram_eaten_by'}, DATA), 'the owner; the foreleg the priest\'s'),
    ('Mishnah Zevachim 5:5 — the guilt-offering (the offering engine CALLED)', lambda: nazirite({'ask': 'asham'}, DATA), 'north; two placements that are four; male priests within the curtains, a day and a night (Mishnah Zevachim 5:5)'),
    ('Mishnah Nazir 6:9; Nazir 46a:2 — permitted after (the running setting)', lambda: nazirite({'ask': 'permitted_after'}, DATA), 'after one offering (the Rabbis; R. Shimon); R. Eliezer after all'),
    ('Nazir 14b-15a — after the term, before the offerings', lambda: nazirite({'ask': 'after_term_before_offerings'}, DATA), 'lashes for impurity, shaving and wine alike (the baraita)'),
    ('Nazir 46b:1 / Menachot 19a:12 — the waving', lambda: nazirite({'ask': 'waving_indispensable'}, DATA), 'not (the Tosefta: with or without palms); Rav: yes'),
    ('Nedarim 18a:3 — a vow on a vow', lambda: nazirite({'ask': 'vow_on_vow'}, DATA), 'takes effect (two terms)'),
    ('Mishnah Nazir 4:1 — the first dissolved', lambda: nazirite({'ask': 'chained_vows', 'which_dissolved': 'first'}, DATA), 'all dissolved'),
    ('Mishnah Nazir 4:1-2 — the wife\'s "and I"', lambda: nazirite({'ask': 'spouse_and_i', 'who_first': 'husband'}, DATA), 'he nullifies hers, his stands'),
    ('Mishnah Nazir 4:5 — after the blood', lambda: nazirite({'ask': 'husband_annuls_after', 'stage': 'blood_sprinkled_purity'}, DATA), 'cannot (R. Akiva: after any slaughter)'),
    ('Mishnah Nazir 4:5 — at the impurity shaving', lambda: nazirite({'ask': 'husband_annuls_after', 'stage': 'impurity_shaving'}, DATA), 'can — a downcast wife'),
    ('Mishnah Nazir 4:3 — nullified without her knowing', lambda: nazirite({'ask': 'nullified_unknown'}, DATA), 'no lashes (R. Yehuda: lashes of rebellion)'),
    ('Mishnah Nazir 4:4 — her animals after nullification', lambda: nazirite({'ask': 'nullified_after_separation', 'whose': 'hers'}, DATA), 'the sin-offering dies, the burnt offered, the peace eaten a day without loaves'),
    ('Mishnah Meilah 3:2 — died with allocated funds', lambda: nazirite({'ask': 'died_with_funds', 'whose': 'hers', 'allocated': True}, DATA), 'the sin\'s to the Dead Sea, the burnt\'s an olah (misuse), the peace\'s a shelamim a day without loaves'),
    ('Mishnah Meilah 3:2 — died with unallocated funds', lambda: nazirite({'ask': 'died_with_funds', 'whose': 'hers', 'allocated': False}, DATA), 'communal gifts'),
    ('Mishnah Nazir 4:6; Mishnah Sotah 3:8 — a father vows his son', lambda: nazirite({'ask': 'father_vows_son'}, DATA), 'a father may (not a mother); the son\'s or relatives\' objection cancels'),
    ('Mishnah Nazir 4:7 — the father\'s funds', lambda: nazirite({'ask': 'shaves_on_fathers_funds', 'when_vowed': 'in_lifetime'}, DATA), 'may (vowed in his father\'s lifetime)'),
    ('Temurah 10a:5 — designated by others', lambda: nazirite({'ask': 'designated_by_others'}, DATA), 'effective (6:21 his means)'),
    ('Mishnah Nazir 5:3 — released by a sage', lambda: nazirite({'ask': 'dissolved_by_sage', 'released': True}, DATA), 'the animal grazes'),
    ('Mishnah Nazir 5:4 — the animal stolen before the vow', lambda: nazirite({'ask': 'vow_in_error', 'event_before': True}, DATA), 'not — an error from the outset (Nachum the Mede)'),
    ('Mishnah Nazir 2:7 — "a son" and a daughter born', lambda: nazirite({'ask': 'conditioned_on_birth', 'form': 'son', 'born': 'daughter'}, DATA), 'not'),
    ('Mishnah Nazir 2:7 — "a child" and a daughter born', lambda: nazirite({'ask': 'conditioned_on_birth', 'form': 'child', 'born': 'daughter'}, DATA), 'a nazirite'),
    ('Mishnah Nazir 2:10 — born after seventy days', lambda: nazirite({'ask': 'two_terms_order', 'born_on_day': 80}, DATA), 'born within seventy days — nothing lost; after — the seventy negated'),
    ('Mishnah Nazir 5:6; Tahorot 4:12 — the doubtful vow', lambda: nazirite({'ask': 'doubtful_vow', 'case': 'turned_back'}, DATA), 'none (lenient; R. Shimon\'s condition)'),
    ('Mishnah Nazir 5:7 — the koy', lambda: nazirite({'ask': 'doubtful_vow', 'case': 'koy'}, DATA), 'all bound (the koy)'),
    ('Mishnah Nazir 8:1 — two doubtful nazirites', lambda: nazirite({'ask': 'two_doubtful'}, DATA), 'ben Zoma\'s procedure (the Rabbis)'),
    ('Mishnah Nazir 8:2; Nazir 60a:6 — the doubtful leper', lambda: nazirite({'ask': 'doubtful_leper'}, DATA), 'sixty days to sacred food, a hundred and twenty to wine and the dead'),
    ('Nazir 41a:3; Yevamot 5a:8 — the leper-nazirite shaves (the metzora engine CALLED)', lambda: nazirite({'ask': 'leper_nazirite_shaves'}, DATA), 'shaves with a razor — the leper\'s command overrides (metzora: commanded_shave_overrides)'),
    ('Shevuot 22b:8 — the oath on a seed', lambda: nazirite({'ask': 'oath_on_seed'}, DATA), 'an open dilemma (Rav Ashi)'),
    ('Bava Kamma 91b:12 / Taanit 11a:16 — a sinner or holy', lambda: nazirite({'ask': 'sinner'}, DATA), 'a sinner (HaKappar) / holy (R. Elazar) — a dispute'),
    ('Mishnah Nazir 6:5 — the exemptions', lambda: nazirite({'ask': 'exemptions'}, DATA), 'the vine none; impurity and shaving: the met mitzvah, the leper\'s shaving'),
    ('Mishnah Nazir 6:11 — impure after the first blood', lambda: nazirite({'ask': 'impure_after_first_blood'}, DATA), 'brings the rest and is pure (the Rabbis); R. Eliezer negates all'),
    ('Mishnah Nazir 6:10 — shaved on an invalid offering', lambda: nazirite({'ask': 'shaved_on_invalid'}, DATA), 'the shaving invalid (R. Shimon: that one alone fails); one of three valid — valid'),
    ('Mishnah Nazir 3:6 — vowed abroad', lambda: nazirite({'ask': 'vowed_abroad'}, DATA), 'Hillel: all again (Shammai: thirty)'),
    # F6 — the blessing
    ('Mishnah Sotah 7:6; Tamid 7:2 — in the Temple', lambda: blessing({'ask': 'form', 'place': 'temple'}, DATA), 'one blessing; the Name as written; the hands above the head (the High Priest not above the frontplate)'),
    ('Mishnah Sotah 7:6 — in the province', lambda: blessing({'ask': 'form', 'place': 'province'}, DATA), 'three blessings with amen; the substitute name; the hands at the shoulders'),
    ('Sotah 33b:3, 38a:2 — the language', lambda: blessing({'ask': 'language'}, DATA), 'the holy tongue (so/so)'),
    ('Mishnah Megillah 4:7 — blemished hands (the priesthood CALLED)', lambda: blessing({'ask': 'who_blesses', 'who': 'blemished_hands'}, DATA), 'does not lift his hands (Megillah 4:7)'),
    ('Taanit 26b:16 — the drunk priest', lambda: blessing({'ask': 'who_blesses', 'who': 'drunk'}, DATA), 'may not (the nazirite\'s juxtaposition)'),
    ('Mishnah Megillah 4:6 — a minor', lambda: blessing({'ask': 'who_blesses', 'who': 'minor'}, DATA), 'not'),
    ('Mishnah Megillah 4:3 — the quorum', lambda: blessing({'ask': 'quorum'}, DATA), 'ten'),
    ('Sotah 38a:12 — who is blessed', lambda: blessing({'ask': 'who_is_blessed'}, DATA), 'all Israel — converts, women, freed slaves'),
    ('Mishnah Megillah 4:10 — translated?', lambda: blessing({'ask': 'translated'}, DATA), 'read, not translated'),
    ('Sotah 38b:4; Menachot 44a:18 — the three commands', lambda: blessing({'ask': 'three_commands'}, DATA), 'so you shall bless; say to them; put My name'),
    ('Chullin 49a:16 — the priests blessed', lambda: blessing({'ask': 'priests_blessed'}, DATA), 'by Heaven (I will bless them)'),
    ('Sifrei 42:2; Berakhot 20b; Niddah 70b — the face lifted', lambda: blessing({'ask': 'face_lifted'}, DATA), 'when they do His will (the Sifrei) / beyond the letter (Berakhot 20b) / before the sentence (Niddah 70b) — three reconciliations'),
    ('Num 6:24-26 — the counts (computed)', lambda: blessing({'ask': 'counts'}, DATA), '3, 5, 7 words; 15, 20, 25 letters; the Name thrice'),
    ('Sotah 38a:9; Mishnah 7:6 — the Name by place', lambda: blessing({'ask': 'name'}, DATA), 'the Name in the Temple, the substitute in the province'),
    # F7 — the wagons
    ('Num 7:1; Sifrei 44:1 — the day', lambda: wagons({'ask': 'day'}, DATA), 'the erection\'s day — the day-stack (Sifrei 44:1; Shabbat 87b): RETROGRADE'),
    ('Num 7:3 — the numbers (the parser after the construct rule)', lambda: wagons({'ask': 'numbers'}, DATA), '6 wagons, 12 oxen; a wagon for two princes, an ox for one (the parser: [6, 12, 2, 1])'),
    ('Sifrei 45:1 — covered', lambda: wagons({'ask': 'covered'}, DATA), 'covered (Rebbi — Onkelos)'),
    ('Num 7:4-5; Sifrei 45:1 — accepted when told', lambda: wagons({'ask': 'accepted'}, DATA), 'not accepted until told (7:4-5)'),
    ('Num 7:6-9; Sifrei 46:1 — the distribution', lambda: wagons({'ask': 'distribution'}, DATA), 'as Moses saw fit: Gershon 2 and 4, Merari 4 and 8, Kohath none — on the shoulder'),
    ('Sifrei 46:2; Sotah 35a:22 — the shoulder', lambda: wagons({'ask': 'shoulder'}, DATA), 'David\'s error and return (the flow reversed); the song from "they carry"'),
    ('Num 7:1; Menachot 57b; Sanhedrin 16b — the anointing (the incense engine CALLED)', lambda: wagons({'ask': 'anointing'}, DATA), 'Moses\' vessels by anointing (the liquid measures in and out, the dry inside — R. Yoshiya); the generations\' by service'),
    # F8 — the dedication
    ('Zevachim 101b:6 — the first day', lambda: dedication({'ask': 'first_day'}, DATA), 'the anointing day = the erection = 1 Nisan: three goats on one day (Zevachim 101b)'),
    ('Sifrei 47:1 — the order (computed)', lambda: dedication({'ask': 'order'}, DATA), 'by the journeying = the camp\'s order (computed = 2:3-31), not by birth; Reuben\'s protest'),
    ('Num 7:11; Moed Katan 9a — one prince per day', lambda: dedication({'ask': 'per_day'}, DATA), 'one prince per day — twelve dues from the anointing day, the Sabbath overridden (Moed Katan 9a)'),
    ('Sifrei 53:1 — the same day', lambda: dedication({'ask': 'same_day'}, DATA), '7:84 = 7:88 — on the day of its anointing / after: the same day (Sifrei 53:1)'),
    ('Num 7:13; Sifrei 49:1 — the dish (the shekel CALLED)', lambda: dedication({'ask': 'dish'}, DATA), '130 and 70 by the sanctuary shekel (Exod 30:13\'s twenty gerah — the sela)'),
    ('Num 7:14, 7:86; Sifrei 55:1 — the pan (M-26)', lambda: dedication({'ask': 'pan'}, DATA), 'ten of gold weighed in silver — 120 = 12 x 10 decides (M-26)'),
    ('Menachot 8a:13 — full', lambda: dedication({'ask': 'full'}, DATA), 'a full tenth sanctifies (R. Yosei: unless meant to add)'),
    ('Menachot 8b:5; Zevachim 88a:6 — the bowls', lambda: dedication({'ask': 'bowls_sanctify_dry'}, DATA), 'yes (Shmuel)'),
    ('Chagigah 23b:7 / Pesachim 19a:8 — the pan joins', lambda: dedication({'ask': 'vessel_joins'}, DATA), 'Torah law (R. Chanin); R. Yochanan rabbinic'),
    ('Num 7:15-17; Sifrei 50:1 — the animals (the offering engine CALLED)', lambda: dedication({'ask': 'animals'}, DATA), 'one bull, one ram, one lamb (burnt); one goat (sin); two oxen, five, five, five (peace) — none like it; its own year'),
    ('Mishnah Parah 1:3 — thirteen months', lambda: dedication({'ask': 'animal_age', 'months': 13}, DATA), 'neither (a palgas)'),
    ('Sifrei 51:1; Menachot 92b:7 — the goat', lambda: dedication({'ask': 'goat'}, DATA), 'for the grave of the depths; leaning — R. Yehuda yes (R. Shimon the idolatry goats)'),
    ('Sifrei 51:1; Menachot 50a — the four exceptions', lambda: dedication({'ask': 'exceptions'}, DATA), 'the Sabbath overridden; an individual\'s incense; a sin-offering not for a sin; one of each'),
    ('Moed Katan 9a:11-12 — the Sabbath', lambda: dedication({'ask': 'sabbath'}, DATA), 'overridden — the days continuous (Moed Katan 9a)'),
    ('Num 7:84-88 — the totals (computed)', lambda: dedication({'ask': 'totals'}, DATA), '2400 = 12 x (130 + 70); 120 = 12 x 10; 12/12/12/12; 24/60/60/60 — computed'),
    ('Sifrei 55:1-57:1 — each credited', lambda: dedication({'ask': 'credited'}, DATA), 'each credited with all twelve (Sifrei 55:1-57:1)'),
    ('Sifrei 54:1 — the weights', lambda: dedication({'ask': 'weights'}, DATA), 'Temple vessels weigh the same singly and together (54:1)'),
    # F9 — the Voice
    ('Num 7:89 — the reflexive (the points)', lambda: voice({'ask': 'reflexive'}, DATA), 'the Voice speaking ITSELF (the hitpael by the points); Onkelos both verbs'),
    ('Sifrei 58:1 — the third verse (I13)', lambda: voice({'ask': 'third_verse'}, DATA), 'Lev 1:1 against Exod 25:22 reconciled by 7:89 (I13)'),
    ('Yoma 4b:8 — who heard', lambda: voice({'ask': 'who_heard'}, DATA), 'Moses alone at the Tent (Yoma 4b); all at Sinai'),
    ('Sifrei 58:2 — the great voice', lambda: voice({'ask': 'great_voice'}, DATA), 'not a low voice — the great voice of Sinai (58:2)'),
    ('Yoma 4b; Sukkah 5a — the door', lambda: voice({'ask': 'door'}, DATA), 'the Voice at the door (Yoma 4b; Sukkah 5a)'),
]


if __name__ == '__main__':
    ok = 0
    for name, run, want in CASES:
        v, e, pr = run()
        hit = v == want
        ok += hit
        print('  %s  %s\n        -> %s  %s' % ('PASS' if hit else 'MISS', name, v, e))
        if not hit:
            print('        expected: %s' % want)
    print('\nNASO: %d/%d cells; the scene %s; the narrative %s' % (ok, len(CASES), SCENE, NARRATIVE))
    print('the exclusions census (to Moses and to Aaron, Exodus-Numbers): %d' % TO_MOSES_AND_AARON)
    sys.exit(0 if ok == len(CASES) else 1)
