

# ---- THE WRAP — the daemon, the scene, the narrative ------------------------------------------------------
def law_beha(event, world):
    """Num 8:1-26 + 10:1-12:16 (cold_run_beha.py F1-F7). installed_by boot — the standing setting for a law spoken at its verse."""
    k, src = event['kind'], event['case_source']
    E_ = lambda eff, s, cp=None, amount=None, due=None, law='', value=None: {'effect': eff, 'subject': s, 'counterparty': cp, 'amount': amount, 'due': due, 'value': value if value is not None else True, 'source_law': law, 'case_source': src}
    day = event.get('day', world.clock.day)      # THE SEQUENTIAL RUN: the event's own day
    if k == 'lamps_commanded':
        return [E_('commanded', event['subject'], value='the_lamps', law='F1 [INK 8:2 "when you raise the lamps, toward the face of the lampstand shall the seven lamps give light" — the lighting owed]')]
    if k == 'lamps_raised':
        if not src.startswith('Num 8:'):           # the erection's kind (Exod 40:25) at its second seat — this span's line only; law_erection's own seat is its own
            return []
        world.close('aaron', 'commanded', 'Num 8:3 — and Aaron did so; toward the face of the lampstand he raised its lamps, as the LORD commanded Moses', value='the_lamps')
        return [E_('lamp_arranged', event['subject'], value='toward the face of the lampstand — Aaron did not change (Sifrei 60:1)', law='F1 [INK 8:3 — the run; the lamps\' debit CLOSED]')]
    if k == 'levites_purification_commanded':
        return [E_('commanded', event['subject'], value='the_rite', law='F2 [INK 8:6-7 "take the Levites... and purify them" — the sprinkling, the razor, the garments, the two bulls, the two layings of hands, the three wavings, the giving: owed]')]
    if k == 'levites_purified_and_given':
        world.close(event['subject'], 'commanded', 'Num 8:20-22 — and Moses and Aaron and all the congregation did to the Levites according to all that the LORD commanded', value='the_rite')
        return [E_('waved', event['subject'], value='one waving in the run (8:21) against three in the spec — M-22', law='F2 [INK 8:21 "and Aaron waved them as a wave offering before the LORD"]'),
                E_('given_to_aaron', event['subject'], cp='aaron-and-sons', value='the service entered before Aaron and before his sons', law='F2 [INK 8:22 "the Levites went in to do their service in the tent of meeting before Aaron and before his sons"; the rite\'s debit CLOSED]')]
    if k == 'levite_age_rule':
        return [E_('charge_kept', event['subject'], value='the_age_rule: 25 in (8:24), 50 out to the charge (8:25-26) — the parameter levite_age', law='F2 [INK 8:24-26; Chullin 24a:12; 1 Chr 23:26 the run\'s re-setting]')]
    if k == 'trumpets_commanded':
        return [E_('commanded', event['subject'], value='the_trumpets', law='F3 [INK 10:2 "make for yourself two trumpets of silver" — a command with no narrated making in the span: OPEN, its run Num 31:6]')]
    if k == 'cloud_lifted':
        return []                                  # 10:11-13: the erection's standing rule at its first run — law_erection's own write; this daemon's march line follows
    if k == 'march_in_order':
        return [E_('arrayed_by_banners', event['subject'], value='the first march — Judah, Reuben, the tent in the midst (Gershon and Merari bearing the tabernacle after Judah; Kohath bearing the sanctuary after Reuben), Ephraim, Dan (10:14-28 = 2:3-31)', law='F4 [INK 10:13-28; the camp\'s order CALLED from Bamidbar]'),
                E_('charge_kept', 'the-levites', value='the burdens on the march: Gershon and Merari the tabernacle (10:17), Kohath the sanctuary — set up before their coming (10:21)', law='F4 [INK 10:17, 10:21]')]
    if k == 'hobab_asked':
        return [E_('plea_made', event['subject'], cp='moses', value='asked to come (10:29), refused (10:30), asked again (10:31-32) — the answer not in the ink (Judg 1:16)', law='F4 [INK 10:29-32; Sifrei 78:1-81:1]')]
    if k == 'ark_journeyed':
        return [E_('journey_of_three_days', event['subject'], due=day + 3, value='three days\' journey from the mountain of the LORD — the ark before them (10:33)', law='F4 [INK 10:33; Taanit 29a:3 — the fire at the twenty-third, the reading-placed marker at 11:1]')]
    if k == 'fire_of_the_lord_burned':
        return [E_('fire_sank', event['subject'], value='the fire of the LORD at the edge of the camp, sunk at Moses\' prayer — Taberah (11:1-3)', law='F5 [INK 11:1-3; Sifrei 85:1-86:1]')]
    if k == 'lust_and_weeping':
        return [E_('lusted', event['subject'], value='lusted a lust — the five foods, the manna despised, Israel weeping by families after them (11:4-10)', law='F5 [INK 11:4-15; Yoma 75a; Shabbat 130a]')]
    if k == 'elders_commanded':
        return [E_('commanded', event['subject'], value='the_gathering', law='F6 [INK 11:16-17 "gather to Me seventy men of the elders" — the gathering owed on Moses]'),
                E_('flesh_for_a_month', 'israel', due=day + 30, value='not one day, nor two, nor five, nor ten, nor twenty — until a month of days (11:19-20)', law='F5 [INK 11:18-20; Yoma 75b:2 the two timers; Taanit 29a:3-4 the stack — CE3]')]
    if k == 'elders_prophesied':
        world.close('moses', 'commanded', 'Num 11:24-25 — and Moses gathered seventy men of the elders of the people and set them around the tent; and the LORD came down in the cloud', value='the_gathering')
        return [E_('spirit_rested', event['subject'], value='the spirit rested on the seventy — they prophesied and did not continue (11:25; the setting continued)', law='F6 [INK 11:24-25; Sanhedrin 17a:12-13]'),
                E_('spirit_rested', 'eldad-and-medad', value='the spirit rested on the two in the camp — they prophesied in the camp and did not cease (11:26-27)', law='F6 [INK 11:26-29; Sanhedrin 17a:4, 17a:13]')]
    if k == 'quail_and_plague':
        return [E_('put_to_death', event['subject'], cp='HEAVEN', value='struck with the flesh between their teeth — the very great blow (11:33); the month\'s timer the second arm', law='F5 [INK 11:31-33; Yoma 75b:2 / Sifrei 94:1 one plague, two timers]'),
                E_('buried', event['subject'], value='Kibroth-hattaavah — the graves of lust (11:34)', law='F5 [INK 11:34; Sifrei 98:1]')]
    if k == 'miriam_spoke':
        return [E_('evil_speech_spoken', event['subject'], value='Miriam first — the feminine singular verb; the Cushite woman (12:1-2)', law='F7 [INK 12:1-2; Sifrei 99:1; Arakhin 15a]'),
                E_('evil_speech_spoken', 'aaron', value='and Aaron — with her (12:1); struck too by R. Akiva, not by R. Yehuda b. Beteira', law='F7 [INK 12:1; Shabbat 97a]')]
    if k == 'miriam_stricken_and_shut_out':
        return [E_('stricken_with_leprosy', event['subject'], value='leprous as snow — the confirmed grade (12:10)', law='F7 [INK 12:10; Yevamot 103b; Zevachim 101b-102a who declared]'),
                E_('confined_seven_days', event['subject'], amount=NG.days(1), due=day + NG.days(1), value='shut out of the camp seven days — the leper\'s week (12:14-15)', law='F7 [INK 12:14-15; the negaim engine\'s week CALLED; Taanit 29a:4 — the fire at the twenty-ninth of Sivan, CE4]'),
                E_('journey_halted', 'israel', value='until_miriam_gathered', law='F7 [INK 12:15 "the people did not journey until Miriam was gathered in" — Mishnah Sotah 1:9 measure for measure; closed by 12:16]')]
    if k == 'paran_reached':
        world.close('israel', 'journey_halted', 'Num 12:16 — and afterward the people journeyed from Hazeroth and encamped in the wilderness of Paran', value='until_miriam_gathered')
        return []
    # ---- the exam's case kinds: each names LITERALLY every effect it can write (2b's form — an unnamed effect is a KeyError to read) ----
    if k == 'lamps_case':
        v, e, _ = lamps({'ask': event['ask']}, DATA); L = 'F1 [%s]' % v; s_ = event['person']
        W = {'accepted': E_('accepted', s_, value=v, law=L), 'disqualified': E_('disqualified', s_, value=v, law=L), 'lamp_arranged': E_('lamp_arranged', s_, value=v, law=L)}
        return [W[x] for x in e if x != FX.NONE]
    if k == 'levite_rite_case':
        v, e, _ = levites_rite({'ask': event['ask'], 'who': event.get('who', 'levite'), 'age': event.get('age', 40), 'carrying': event.get('carrying', True), 'blemished': event.get('blemished', False)}, DATA); L = 'F2 [%s]' % v; s_ = event['person']
        W = {'appointed_to_serve': E_('appointed_to_serve', s_, value=v, law=L), 'exempt': E_('exempt', s_, value=v, law=L), 'disqualified': E_('disqualified', s_, value=v, law=L), 'waved': E_('waved', s_, value=v, law=L), 'accepted': E_('accepted', s_, value=v, law=L),
             'commanded': E_('commanded', s_, value=v, law=L), 'given_to_aaron': E_('given_to_aaron', s_, value=v, law=L), 'charge_kept': E_('charge_kept', s_, value=v, law=L)}
        return [W[x] for x in e if x != FX.NONE]
    if k == 'trumpet_case':
        v, e, _ = trumpets({'ask': event['ask'], 'occasion': event.get('occasion', 'journey'), 'kind': event.get('kind', 'war'), 'day': event.get('day_kind', 'rosh_hashanah')}, DATA); L = 'F3 [%s]' % v; s_ = event['person']
        W = {'accepted': E_('accepted', s_, value=v, law=L), 'disqualified': E_('disqualified', s_, value=v, law=L), 'exempt': E_('exempt', s_, value=v, law=L), 'sanctify_day': E_('sanctify_day', s_, value=v, law=L), 'commanded': E_('commanded', s_, value=v, law=L)}
        return [W[x] for x in e if x != FX.NONE]
    if k == 'march_case':
        v, e, _ = march({'ask': event['ask']}, DATA); L = 'F4 [%s]' % v; s_ = event['person']
        W = {'accepted': E_('accepted', s_, value=v, law=L), 'disqualified': E_('disqualified', s_, value=v, law=L), 'arrayed_by_banners': E_('arrayed_by_banners', s_, value=v, law=L), 'charge_kept': E_('charge_kept', s_, value=v, law=L),
             'journey_of_three_days': E_('journey_of_three_days', s_, value=v, law=L), 'plea_made': E_('plea_made', s_, value=v, law=L)}
        return [W[x] for x in e if x != FX.NONE]
    if k == 'elders_case':
        v, e, _ = seventy_elders({'ask': event['ask']}, DATA); L = 'F6 [%s]' % v; s_ = event['person']
        W = {'appointed_to_serve': E_('appointed_to_serve', s_, value=v, law=L), 'spirit_rested': E_('spirit_rested', s_, value=v, law=L), 'accepted': E_('accepted', s_, value=v, law=L), 'disqualified': E_('disqualified', s_, value=v, law=L)}
        return [W[x] for x in e if x != FX.NONE]
    if k == 'quail_case':
        v, e, _ = taberah_and_quail({'ask': event['ask']}, DATA); L = 'F5 [%s]' % v; s_ = event['person']
        W = {'put_to_death': E_('put_to_death', s_, cp='HEAVEN', value=v, law=L), 'lusted': E_('lusted', s_, value=v, law=L), 'fire_sank': E_('fire_sank', s_, value=v, law=L), 'accepted': E_('accepted', s_, value=v, law=L), 'disqualified': E_('disqualified', s_, value=v, law=L),
             'exempt': E_('exempt', s_, value=v, law=L), 'flesh_for_a_month': E_('flesh_for_a_month', s_, value=v, law=L), 'buried': E_('buried', s_, value=v, law=L)}
        return [W[x] for x in e if x != FX.NONE]
    if k == 'miriam_case':
        v, e, _ = miriam({'ask': event['ask']}, DATA); L = 'F7 [%s]' % v; s_ = event['person']
        W = {'evil_speech_spoken': E_('evil_speech_spoken', s_, value=v, law=L), 'stricken_with_leprosy': E_('stricken_with_leprosy', s_, value=v, law=L), 'disqualified': E_('disqualified', s_, value=v, law=L), 'accepted': E_('accepted', s_, value=v, law=L),
             'exempt': E_('exempt', s_, value=v, law=L), 'healed': E_('healed', s_, value=v, law=L), 'journey_halted': E_('journey_halted', s_, value=v, law=L),
             'confined_seven_days': E_('confined_seven_days', s_, amount=NG.days(1), due=(day + NG.days(1)) if event['ask'] == 'quarantine' else None, value=v, law=L)}
        return [W[x] for x in e if x != FX.NONE]
    return []


def scene():
    """THE SCENE — the exam's rows replayed on the world engine (the exodus epoch): the fitness by age, the trumpets' occasions, the lamps' geometry,
    the seventy-one, the quail's two arms, and Miriam's week as a TIMER (set at the case, fired eight days on)."""
    with contextlib.redirect_stdout(io.StringIO()):
        w = WE.World(era='Num 8, 10-12: Mishnah Chullin 1, Menachot 3-4, Tamid, Rosh Hashanah 3-4, Ta\'anit, Sukkah 5, Sanhedrin 1, Negaim 2-3, Bava Kamma 2:5 and the Talmud\'s rows on the engine (the exodus epoch)', epoch='exodus')
        w.laws = [law_beha]
        w.advance(w.clock.day_in('exodus', 2, 2, 1))
        w.submit({'kind': 'lamps_case', 'subject': 'the-priest-at-the-lamps', 'person': 'the-priest-at-the-lamps', 'ask': 'geometry', 'case_source': 'Menachot 98b:18; Num 8:2 — the six toward the middle'})
        w.submit({'kind': 'levite_rite_case', 'subject': 'the-apprentice-levite', 'person': 'the-apprentice-levite', 'ask': 'fitness', 'who': 'levite', 'age': 27, 'case_source': 'Chullin 24a:12; Num 8:24 — twenty-seven: an apprentice (Bamidbar called)'})
        w.submit({'kind': 'levite_rite_case', 'subject': 'the-old-levite-at-shiloh', 'person': 'the-old-levite-at-shiloh', 'ask': 'fitness', 'who': 'levite', 'age': 55, 'carrying': False, 'case_source': 'Chullin 24a:11; Num 8:25 — not carrying: fit'})
        w.submit({'kind': 'levite_rite_case', 'subject': 'the-blemished-levite', 'person': 'the-blemished-levite', 'ask': 'fitness', 'who': 'levite', 'age': 40, 'blemished': True, 'case_source': 'Chullin 24a:9; Mishnah Chullin 1:6; Num 8:24 — a blemish does not disqualify a Levite'})
        w.submit({'kind': 'levite_rite_case', 'subject': 'the-levites-waved', 'person': 'the-levites-waved', 'ask': 'wavings', 'case_source': 'Menachot 61b; Num 8:11-21 — three wavings in the spec, one in the run'})
        w.submit({'kind': 'trumpet_case', 'subject': 'the-priests-at-the-fast', 'person': 'the-priests-at-the-fast', 'ask': 'with_shofar', 'day_kind': 'fast', 'case_source': 'Mishnah Rosh Hashanah 3:4; Num 10:9 — the trumpets the day\'s mitzvah'})
        w.submit({'kind': 'trumpet_case', 'subject': 'the-city-with-too-much-rain', 'person': 'the-city-with-too-much-rain', 'ask': 'oppression', 'kind': 'excess_rain', 'case_source': 'Mishnah Ta\'anit 3:8; Num 10:9 — no alarm for a blessing'})
        w.submit({'kind': 'trumpet_case', 'subject': 'the-city-in-pestilence', 'person': 'the-city-in-pestilence', 'ask': 'oppression', 'kind': 'pestilence', 'case_source': 'Mishnah Ta\'anit 3:4; Num 10:9 — three dead in three days'})
        w.submit({'kind': 'trumpet_case', 'subject': 'the-shofar-of-rosh-hashanah', 'person': 'the-shofar-of-rosh-hashanah', 'ask': 'shofar_identity', 'case_source': 'Rosh Hashanah 34a:8; Num 10:5-6 — the identity (the moadim engine called)'})
        w.submit({'kind': 'trumpet_case', 'subject': 'the-trumpets-of-moses', 'person': 'the-trumpets-of-moses', 'ask': 'scope', 'case_source': 'Menachot 28b:3; Num 10:2 — for you, twice'})
        w.submit({'kind': 'march_case', 'subject': 'the-camp-on-the-march', 'person': 'the-camp-on-the-march', 'ask': 'order', 'case_source': 'Num 10:14-28; Num 2:3-31 — the camp\'s order (Bamidbar called)'})
        w.submit({'kind': 'march_case', 'subject': 'the-scroll-of-eighty-five', 'person': 'the-scroll-of-eighty-five', 'ask': 'eighty_five', 'case_source': 'Mishnah Yadayim 3:5; Num 10:35-36 — the letters computed'})
        w.submit({'kind': 'elders_case', 'subject': 'the-great-sanhedrin', 'person': 'the-great-sanhedrin', 'ask': 'sanhedrin', 'case_source': 'Mishnah Sanhedrin 1:6; Num 11:16 — seventy-one'})
        w.submit({'kind': 'elders_case', 'subject': 'the-seventy-two-ballots', 'person': 'the-seventy-two-ballots', 'ask': 'lots', 'case_source': 'Sanhedrin 17a:4-5; Num 11:26 — the box (Bamidbar\'s lots called)'})
        w.submit({'kind': 'quail_case', 'subject': 'the-eater-of-the-quail', 'person': 'the-eater-of-the-quail', 'ask': 'two_timers', 'case_source': 'Yoma 75b:2; Num 11:33 — one plague, two timers'})
        w.submit({'kind': 'quail_case', 'subject': 'the-weepers-by-families', 'person': 'the-weepers-by-families', 'ask': 'families_weeping', 'case_source': 'Yoma 75a:9; Num 11:10 — the forbidden relations'})
        w.submit({'kind': 'miriam_case', 'subject': 'the-goring-ox-on-private-ground', 'person': 'the-goring-ox-on-private-ground', 'ask': 'dayo', 'case_source': 'Mishnah Bava Kamma 2:5; Bava Kamma 25a; Num 12:14 — dayo'})
        d0 = w.clock.day
        w.submit({'kind': 'miriam_case', 'subject': 'the-leper-shut-out', 'person': 'the-leper-shut-out', 'ask': 'quarantine', 'case_source': 'Mishnah Negaim 3:1; Num 12:14-15 — the leper\'s week (the negaim engine called)'})
        w.submit({'kind': 'miriam_case', 'subject': 'the-short-prayer', 'person': 'the-short-prayer', 'ask': 'short_prayer', 'case_source': 'Berakhot 34a:12; Num 12:13 — five words'})
        w.submit({'kind': 'miriam_case', 'subject': 'the-confirmed-leper', 'person': 'the-confirmed-leper', 'ask': 'grade', 'case_source': 'Yevamot 103b:16; Num 12:10 — as one dead: the confirmed only'})
        w.advance(d0 + 8)
    n = lambda eid, eff: len([e for e in w.entity(eid).ledger if e['effect'] == eff])
    L = lambda k: len([l for l in w.log if l[0] == k])
    return (n('the-priest-at-the-lamps', 'lamp_arranged'), n('the-apprentice-levite', 'exempt'), n('the-old-levite-at-shiloh', 'appointed_to_serve'), n('the-blemished-levite', 'appointed_to_serve'), n('the-levites-waved', 'waved'),
            n('the-priests-at-the-fast', 'sanctify_day'), n('the-city-with-too-much-rain', 'exempt'), n('the-city-in-pestilence', 'sanctify_day'), n('the-shofar-of-rosh-hashanah', 'sanctify_day'), n('the-trumpets-of-moses', 'commanded'),
            n('the-camp-on-the-march', 'arrayed_by_banners'), n('the-scroll-of-eighty-five', 'arrayed_by_banners'), n('the-great-sanhedrin', 'appointed_to_serve'), n('the-seventy-two-ballots', 'appointed_to_serve'),
            n('the-eater-of-the-quail', 'put_to_death'), n('the-weepers-by-families', 'lusted'), n('the-goring-ox-on-private-ground', 'confined_seven_days'), n('the-leper-shut-out', 'confined_seven_days'), L('TIMER-SET'), L('TIMER-FIRE'),
            n('the-short-prayer', 'healed'), n('the-confirmed-leper', 'stricken_with_leprosy'), len(w.entities)), w
SCENE, _W = scene()


def narrative():
    """THE NUMBERS WALK 3b (2026-09-10; NUMBERS_WALK.md "Sitting 3b"): the portion's own acts AS HISTORY — the eighteen lines of Num 8:1-26 +
    10:1-12:16 in the text's order on a world with this runner's daemon (the erection's cloud_lifted and lamps_raised kinds reused at their
    second seats), the four FORWARD markers — 10:11 the ink's own (2, 2, 20), and Taanit 29a's three reading-placed: 11:1 (2, 2, 23), 11:35
    (2, 3, 22), 12:16 (2, 3, 29) — and the ink's three durations as TIMERS firing on the walks between them. Not a graded cell: the tuple
    below is a tripwire PREDICTED before the first run; the sequence world's RUN tuple grades the tape."""
    with contextlib.redirect_stdout(io.StringIO()):
        w = WE.World(era='Num 8, 10-12: Beha\'alotcha on the tape — the lamps, the Levites, the trumpets, the march, Taberah, the quail, the seventy, Miriam (the exodus epoch)', epoch='exodus')
        w.laws = [law_beha]
        w.submit({'kind': 'lamps_commanded', 'subject': 'aaron', 'geometry': 'toward the face', 'count': LAMPS[0], 'pattern': 'as shown', 'case_source': 'Num 8:1-4 — and the LORD spoke to Moses saying: speak to Aaron and say to him: when you raise the lamps, toward the face of the lampstand shall the seven lamps give light; and this is the work of the lampstand: beaten gold... as the pattern the LORD showed Moses'})
        w.submit({'kind': 'lamps_raised', 'subject': 'aaron', 'toward': 'the face of the lampstand', 'case_source': 'Num 8:3 — and Aaron did so: toward the face of the lampstand he raised its lamps, as the LORD commanded Moses'})
        w.submit({'kind': 'levites_purification_commanded', 'subject': 'the-levites', 'water': 'the water of purification', 'razor': True, 'garments': 'washed', 'bulls': 2, 'hands_laid': 2, 'wavings': 3, 'given_doubled': True, 'case_source': 'Num 8:5-19 — and the LORD spoke to Moses saying: take the Levites from among the children of Israel and purify them... for given, given are they to Me from among the children of Israel'})
        w.submit({'kind': 'levites_purified_and_given', 'subject': 'the-levites', 'wavings_in_run': 1, 'atoned': True, 'service_entered': True, 'case_source': 'Num 8:20-22 — and Moses and Aaron and all the congregation did to the Levites according to all that the LORD commanded Moses; and the Levites purified themselves and washed their garments, and Aaron waved them... and afterward the Levites went in to do their service'})
        w.submit({'kind': 'levite_age_rule', 'subject': 'the-levites', 'age_in': AGE_IN[0], 'age_out': AGE_OUT[0], 'after_fifty': 'the charge, no service', 'case_source': 'Num 8:23-26 — and the LORD spoke to Moses saying: this is what belongs to the Levites: from twenty-five years old and upward he shall come to host the host... and from fifty years old he shall return... and shall do no service'})
        w.submit({'kind': 'trumpets_commanded', 'subject': 'moses', 'count': TRUMPETS[0], 'material': 'silver', 'work': 'beaten', 'offices': ['the congregation', 'the camps'], 'sounds': 'tekiah / teruah', 'war': 'the oppressor', 'gladness': 'the festivals, the new moons', 'case_source': 'Num 10:1-10 — and the LORD spoke to Moses saying: make for yourself two trumpets of silver, of beaten work you shall make them... on the day of your gladness... I am the LORD your God'})
        w.marker('Num 10:11', w.clock.day_in('exodus', 2, 2, 20), value='in the second year, in the second month, on the twentieth of the month, the cloud was taken up (10:11) — the ink\'s own date: the tape\'s FORWARD marker after 1:1\'s (2, 2, 1); Rosh Hashanah 3a:5 Nisan and Iyar in one year')
        w.submit({'kind': 'cloud_lifted', 'subject': 'israel', 'from': 'the tabernacle of the testimony', 'to': 'the wilderness of Paran', 'first': True, 'case_source': 'Num 10:11-13 — and the cloud was taken up from over the tabernacle of the testimony; and the children of Israel journeyed by their journeys from the wilderness of Sinai, and the cloud rested in the wilderness of Paran; and they journeyed first by the mouth of the LORD by the hand of Moses'})
        w.submit({'kind': 'march_in_order', 'subject': 'israel', 'order': ORDER_10, 'levites_places': 'Gershon and Merari after Judah; Kohath after Reuben', 'princes': NAMES, 'case_source': 'Num 10:14-28 — and the standard of the camp of the children of Judah journeyed first by their hosts... and the tabernacle was taken down... and the Kohathites journeyed, bearing the sanctuary... these are the journeys of the children of Israel by their hosts, and they journeyed'})
        w.submit({'kind': 'hobab_asked', 'subject': 'hobab', 'three_readings': 'we are journeying', 'answer': 'not in the ink', 'case_source': 'Num 10:29-32 — and Moses said to Hobab son of Reuel the Midianite, Moses\' father-in-law: we are journeying to the place... come with us; and he said: I will not go... and he said: leave us not, I pray'})
        w.submit({'kind': 'ark_journeyed', 'subject': 'the-ark', 'days': THREE_DAYS[0], 'clouds': DATA['seven_clouds']['value'], 'song': 'Rise, LORD / Return, LORD', 'signs': 'two inverted nuns', 'case_source': 'Num 10:33-36 — and they journeyed from the mountain of the LORD three days\' journey, and the ark of the covenant of the LORD journeyed before them... and when the ark journeyed Moses said: Rise, LORD... and when it rested he said: Return, LORD, to the myriads of the thousands of Israel'})
        w.marker('Num 11:1', w.clock.day_in('exodus', 2, 2, 23), value='the three days\' journey elapsed — READING-PLACED by Taanit 29a:3 ("adds to the first twenty days an additional three days\' journey: twenty-three"); the murmuring at Taberah', placement='reading_placed')
        w.submit({'kind': 'fire_of_the_lord_burned', 'subject': 'israel', 'edge': True, 'who': DATA['fire_at_the_edge']['value'], 'prayer': 'Moses prayed', 'name': 'Taberah', 'case_source': 'Num 11:1-3 — and the people were as murmurers, evil in the ears of the LORD; and the LORD heard, and His anger burned, and the fire of the LORD burned among them and consumed at the edge of the camp; and the people cried to Moses, and Moses prayed to the LORD, and the fire sank; and he called the name of that place Taberah'})
        w.submit({'kind': 'lust_and_weeping', 'subject': 'the-rabble', 'foods': ['the fish', 'the cucumbers', 'the melons', 'the leeks', 'the onions', 'the garlic'], 'manna': 'like coriander seed, its taste as a cake baked with oil', 'families': 'weeping by its families', 'moses_cry': 'why have You dealt ill with Your servant', 'case_source': 'Num 11:4-15 — and the rabble that was among them lusted a lust, and the children of Israel also wept again and said: who shall give us flesh to eat?... and Moses heard the people weeping by its families... and Moses said to the LORD: why have You dealt ill with Your servant'})
        w.submit({'kind': 'elders_commanded', 'subject': 'moses', 'seventy': SEVENTY[0], 'spirit': 'set apart', 'day_ladder': DAY_LADDER, 'month': DATA['month_of_days']['value'], 'six_hundred_thousand': SIX_HUNDRED[0], 'case_source': 'Num 11:16-23 — and the LORD said to Moses: gather to Me seventy men of the elders of Israel... and to the people you shall say: sanctify yourselves for tomorrow and you shall eat flesh... not one day, nor two days, nor five days, nor ten days, nor twenty days — until a month of days... is the hand of the LORD shortened?'})
        w.submit({'kind': 'elders_prophesied', 'subject': 'the-seventy-elders', 'seventy': SEVENTY[0], 'two': ['Eldad', 'Medad'], 'continued': DATA['continued']['value'], 'restrain': 'Joshua: my lord Moses, restrain them', 'case_source': 'Num 11:24-30 — and Moses went out and spoke to the people the words of the LORD, and gathered seventy men of the elders of the people and set them around the tent; and the LORD came down in the cloud... and the spirit rested on them and they prophesied and did not continue; and two men remained in the camp... Eldad... Medad... and they prophesied in the camp'})
        w.submit({'kind': 'quail_and_plague', 'subject': 'the-lusters', 'height': TWO_CUBITS[0], 'gathered': TEN_HOMERS[0], 'blow': 'a very great blow', 'graves': 'Kibroth-hattaavah', 'hazeroth': True, 'case_source': 'Num 11:31-35 — and a wind went out from the LORD and brought quail from the sea... about two cubits above the face of the earth... he who gathered least gathered ten homers... the flesh was yet between their teeth... and the LORD struck the people with a very great blow; and he called the name of that place Kibroth-hattaavah... from Kibroth-hattaavah the people journeyed to Hazeroth'})
        w.marker('Num 11:35', w.clock.day_in('exodus', 2, 3, 22), value='the arrival at Hazeroth — READING-PLACED by Taanit 29a:4 (the twenty-ninth of Sivan less the seven days shut out: the twenty-second; Seder Olam Rabbah 8:2\'s stack); the month of flesh ended here on the shelf\'s count', placement='reading_placed')
        w.submit({'kind': 'miriam_spoke', 'subject': 'miriam', 'who_first': MIRIAM_FIRST, 'cushite': 'the Cushite woman', 'answer': 'mouth to mouth, not in riddles', 'aaron_struck': DATA['aaron_struck']['value'], 'case_source': 'Num 12:1-9 — and Miriam spoke, and Aaron, against Moses because of the Cushite woman whom he had taken... and the LORD heard... and the LORD came down in a pillar of cloud and stood at the door of the tent, and called Aaron and Miriam... mouth to mouth I speak with him... and the anger of the LORD burned against them, and He went'})
        w.submit({'kind': 'miriam_stricken_and_shut_out', 'subject': 'miriam', 'stricken': 'leprous as snow', 'prayer': ' '.join(PRAYER), 'dayo': DATA['dayo']['value'], 'days': SEVEN[0], 'halt': True, 'case_source': 'Num 12:10-15 — and the cloud departed from over the tent, and behold Miriam was leprous as snow... and Moses cried to the LORD saying: God, heal her, please... let her be shut out of the camp seven days, and afterward she shall be gathered in; and Miriam was shut out of the camp seven days, and the people did not journey until Miriam was gathered in'})
        w.marker('Num 12:16', w.clock.day_in('exodus', 2, 3, 29), value='the journey from Hazeroth to Paran — READING-PLACED by Taanit 29a:4-5 ("they remained in Hazeroth until the twenty-ninth of Sivan before traveling on to Paran"; the baraita: on the twenty-ninth of Sivan Moses sent the spies); Seder Olam 8:2 the twenty-eighth (the row spies_sent_day)', placement='reading_placed')
        w.submit({'kind': 'paran_reached', 'subject': 'israel', 'from': 'Hazeroth', 'to': 'the wilderness of Paran', 'halt_closed': True, 'case_source': 'Num 12:16 — and afterward the people journeyed from Hazeroth and encamped in the wilderness of Paran'})
    n = lambda eid, eff: len([e for e in w.entity(eid).ledger if e['effect'] == eff])
    is_open = lambda eid, eff: [e.get('open') for e in w.entity(eid).ledger if e['effect'] == eff]
    L = lambda k: len([l for l in w.log if l[0] == k])
    ex = w.clock.eras['exodus']
    markers = [l for l in w.log if l[0] == 'MARKER']
    fires = [l for l in w.log if l[0] == 'TIMER-FIRE']
    return (n('aaron', 'commanded'), is_open('aaron', 'commanded'), n('aaron', 'lamp_arranged'), n('aaron', 'evil_speech_spoken'),
            n('the-levites', 'commanded'), is_open('the-levites', 'commanded'), n('the-levites', 'waved'), n('the-levites', 'given_to_aaron'), n('the-levites', 'charge_kept'),
            n('moses', 'commanded'), is_open('moses', 'commanded'),
            n('israel', 'arrayed_by_banners'), n('israel', 'fire_sank'), n('israel', 'flesh_for_a_month'), n('israel', 'journey_halted'), is_open('israel', 'journey_halted'),
            n('hobab', 'plea_made'), n('the-ark', 'journey_of_three_days'), n('the-rabble', 'lusted'), n('the-seventy-elders', 'spirit_rested'), n('eldad-and-medad', 'spirit_rested'),
            n('the-lusters', 'put_to_death'), n('the-lusters', 'buried'), n('miriam', 'evil_speech_spoken'), n('miriam', 'stricken_with_leprosy'), n('miriam', 'confined_seven_days'),
            L('TIMER-SET'), L('TIMER-FIRE'), [ex.date(f[1]) for f in fires], len(markers), [m[2].get('retrograde') for m in markers], L('EVENT'), L('WRITE'), len(w.entities)), w


NARRATIVE, _WN = narrative()
NARRATIVE_PREDICTED = (1, [False], 1, 1,
                       1, [False], 1, 1, 2,
                       2, [True, False],
                       1, 1, 1, 1, [False],
                       1, 1, 1, 1, 1,
                       1, 1, 1, 1, 1,
                       3, 3, [(2, 2, 23), (2, 3, 24), (2, 3, 29)], 4, [False, False, False, False], 18, 24, 11)   # PREDICTED from the design BEFORE the first run (NUMBERS_WALK.md "Sitting 3b"): the lamps' debit closed by 8:3; the rite's debit closed by 8:20-22 with the one waving and the giving; the Levites' charge twice (the age rule, the march's burdens); Moses' two debits — the trumpets OPEN (their run Num 31:6), the gathering closed; Israel's march, fire, month, halt (closed by 12:16); Hobab's plea; the ark's three days; the rabble; the seventy and the two; the lusters struck and buried; Miriam's three; THREE TIMERS set and fired on the walks — the three days at (2, 2, 23) = the 11:1 marker, the month at (2, 3, 24) two days after the Hazeroth marker (the inclusive count — CE3 DIVERGE expected), Miriam's seven at (2, 3, 29) = the 12:16 marker; four forward markers, none retrograde; eighteen events; twenty-four writes (twenty-one at the lines + the three fires); eleven entities
assert NARRATIVE == NARRATIVE_PREDICTED, ('THE NUMBERS WALK: Beha\'alotcha\'s narrative moved from its prediction', NARRATIVE, NARRATIVE_PREDICTED)


# =====================================================================
# Motion 2 — THE TEST DATA: the answer sheet's rows (the docket's LAW rows).
# =====================================================================
CASES = [
    # F1 — the lamps
    ('Sifrei 59:1; Menachot 98b:18; Megillah 21b:13 — the geometry', lambda: lamps({'ask': 'geometry'}, DATA), 'six toward the middle, the middle toward the Presence'),
    ('Shabbat 22b; Mishnah Tamid 6:1 — the western lamp (the sanctuary engine CALLED)', lambda: lamps({'ask': 'western_lamp'}, DATA), 'the western lamp burns continually; the rest kindled from it'),
    ('Menachot 28a:16 — the material (the sanctuary engine CALLED)', lambda: lamps({'ask': 'material'}, DATA), 'gold beaten; other metals cast, fragments valid'),
    ('Sifrei 61:1; Menachot 28a:16-18 — the 2x2', lambda: lamps({'ask': 'two_by_two'}, DATA), 'the lampstand: gold beaten, other metals cast; the trumpets: silver only'),
    ('Mishnah Menachot 3:7 — the seven (the sanctuary engine CALLED)', lambda: lamps({'ask': 'count'}, DATA), '7 lamps, each indispensable'),
    ('Menachot 29a:2 — the ninth flower (the sanctuary engine CALLED)', lambda: lamps({'ask': 'flowers'}, DATA), '9 flowers — the ninth near the base'),
    ('Sifrei 59:1; Mishnah Tamid 3:9 — the steps', lambda: lamps({'ask': 'steps'}, DATA), 'three stairs on the stone before the lampstand'),
    ('Menachot 29a:14-15 — the pattern (the sanctuary engine CALLED)', lambda: lamps({'ask': 'pattern'}, DATA), 'shown with the finger — an exact replica (one of three)'),
    ('Mishnah Menachot 4:4 — the inauguration', lambda: lamps({'ask': 'inauguration'}, DATA), 'inaugurated by the seven lamps at evening'),
    ('Sifrei 60:1 — Aaron did not change', lambda: lamps({'ask': 'aaron_unchanged'}, DATA), 'Aaron did not change'),
    ('Sifrei 60:1; Yoma 24b — the sons equated', lambda: lamps({'ask': 'sons_equated'}, DATA), 'the sons equated with the father by three facets'),
    ('Gittin 60b:1 — the day the section was said', lambda: lamps({'ask': 'day_spoken'}, DATA), 'the first of Nisan by R. Levi'),
    ('Lev 24:3; Sifrei 59:1 — evening to morning', lambda: lamps({'ask': 'evening_to_morning'}, DATA), 'from evening to morning'),
    # F2 — the Levites' rite and ages
    ('Num 8:7 — the purification (the heifer OWED FORWARD)', lambda: levites_rite({'ask': 'purification'}, DATA), 'sprinkled with the water of purification, a razor over all the flesh, the garments washed'),
    ('Nazir 40a:8; Mishnah Negaim 14:4 — the razor', lambda: levites_rite({'ask': 'razor'}, DATA), 'a razor over all the flesh; two hairs left = nothing'),
    ('Num 8:8 — the two bulls', lambda: levites_rite({'ask': 'bulls'}, DATA), 'two bulls — a sin offering and a burnt offering with its meal offering'),
    ('Zevachim 89b:1-2 — the order', lambda: levites_rite({'ask': 'bulls_order'}, DATA), "the sin offering's blood first, its portions after the burnt offering's limbs"),
    ('Horayot 5b:17 — the sin offering not eaten', lambda: levites_rite({'ask': 'sin_offering_eaten'}, DATA), 'not eaten — second to and like the burnt offering'),
    ('Mishnah Parah 1:2 — the bulls\' age', lambda: levites_rite({'ask': 'bull_age'}, DATA), 'up to three years (the Sages); two (R. Yosei HaGelili); five (R. Meir)'),
    ('Num 8:10, 8:12 — the two layings of hands', lambda: levites_rite({'ask': 'hands_laid'}, DATA), 'twice — Israel on the Levites, the Levites on the bulls'),
    ('Num 8:11-21 — the wavings (M-22)', lambda: levites_rite({'ask': 'wavings'}, DATA), 'three in the spec, one in the run'),
    ('Menachot 61b-62a; Nazir 40a:11 — the bodies waved', lambda: levites_rite({'ask': 'waved_bodies'}, DATA), 'a live wave offering — the Levites waved by Aaron'),
    ('Num 3:9 / 8:16 — given, given (M-23)', lambda: levites_rite({'ask': 'given'}, DATA), "'given, given' doubled at 3:9 and 8:16"),
    ('Bekhorot 4b:22; Mishnah Bekhorot 1:1 — the firstborn ground (the pesach engine CALLED)', lambda: levites_rite({'ask': 'firstborn_ground'}, DATA), 'the wilderness seat of the firstborn (8:17); the Levites for the firstborn'),
    ('Num 8:19 — the five (computed)', lambda: levites_rite({'ask': 'five_times'}, DATA), '5 times in 8:19'),
    ('Chullin 24a:12; 1 Chr 23:24-27 — the age parameter', lambda: levites_rite({'ask': 'age'}, DATA), '25 to learn, 30 to serve, 50 to return; 20 in the Temple'),
    ('Chullin 24a:12 — the ages (Bamidbar CALLED)', lambda: levites_rite({'ask': 'ages'}, DATA), '25 learn, 30 serve, 50 return'),
    ('Chullin 24a:12 — the apprentice of twenty-seven (Bamidbar CALLED)', lambda: levites_rite({'ask': 'fitness', 'who': 'levite', 'age': 27}, DATA), 'unfit — under thirty (twenty-five to apprentice)'),
    ('Chullin 24a:11 — fifty-five at Shiloh, not carrying (Bamidbar CALLED)', lambda: levites_rite({'ask': 'fitness', 'who': 'levite', 'age': 55, 'carrying': False}, DATA), 'fit — years disqualify only while carrying'),
    ('Chullin 24a:9; Mishnah Chullin 1:6 — the blemished Levite (Bamidbar CALLED)', lambda: levites_rite({'ask': 'fitness', 'who': 'levite', 'age': 40, 'blemished': True}, DATA), 'fit — a blemish does not disqualify a Levite'),
    ('Mishnah Chullin 1:6 — the blemished priest (Bamidbar CALLED)', lambda: levites_rite({'ask': 'fitness', 'who': 'priest', 'blemished': True}, DATA), 'unfit — a blemish'),
    ('Mishnah Chullin 1:6 — the chiasm', lambda: levites_rite({'ask': 'chiasm'}, DATA), 'years disqualify Levites, blemishes priests'),
    ('Chullin 24a:9; Sifrei 62:1, 63:1 — the two a-fortioris refused', lambda: levites_rite({'ask': 'a_fortiori_refused'}, DATA), "'this' caps the inference: blemishes do not disqualify Levites; years do not disqualify priests"),
    ('Num 8:25-26; Chullin 24a — after fifty', lambda: levites_rite({'ask': 'after_fifty'}, DATA), 'keeps the charge, no service — the gates and the wagons'),
    ('Arakhin 11a:7; Mishnah Arakhin 2:6 — the song', lambda: levites_rite({'ask': 'song'}, DATA), 'the song indispensable (R. Meir); twelve Levites the floor'),
    ('1 Chr 23:24-27 — Chronicles re-sets the spec', lambda: levites_rite({'ask': 'chronicles'}, DATA), 'twenty — no more carrying: the run re-sets the spec'),
    ('Gittin 60a:17 — the day the section was said', lambda: levites_rite({'ask': 'day_spoken'}, DATA), 'the first of Nisan by R. Levi'),
    # F3 — the trumpets
    ('Sifrei 72:1; Mishnah Arakhin 2:5 — the count', lambda: trumpets({'ask': 'count'}, DATA), "2 — the wilderness pair; the Temple's floor two, more permitted"),
    ('Menachot 28a:18; Rosh Hashanah 27a:10 — the material', lambda: trumpets({'ask': 'material'}, DATA), 'silver only; fragments valid; the fast-day shofar silver-plated from it'),
    ('Menachot 28b:2-3 — the instance scope', lambda: trumpets({'ask': 'scope'}, DATA), "instance — Moses' trumpets hidden, the generations make their own"),
    ('Num 10:2 — the two offices', lambda: trumpets({'ask': 'offices'}, DATA), 'the calling of the congregation; the journeying of the camps'),
    ('Num 10:3, 10:7; Rosh Hashanah 34a:6 — the congregation', lambda: trumpets({'ask': 'sounds', 'occasion': 'congregation'}, DATA), 'a tekiah, no teruah'),
    ('Num 10:4 — the princes', lambda: trumpets({'ask': 'sounds', 'occasion': 'princes'}, DATA), 'one trumpet — the princes'),
    ('Num 10:5-6; Rosh Hashanah 34a:7 — the journeys', lambda: trumpets({'ask': 'sounds', 'occasion': 'journey'}, DATA), 'tekiah, teruah, tekiah'),
    ('Arakhin 10a:7-8; Sukkah 53b — the blast unit', lambda: trumpets({'ask': 'blast_unit'}, DATA), 'three separate sounds (the Rabbis); one unit (R. Yehuda)'),
    ('Rosh Hashanah 34a:8; Mishnah Rosh Hashanah 4:9 — the identity (the moadim engine CALLED)', lambda: trumpets({'ask': 'shofar_identity'}, DATA), "the Rosh Hashanah shofar's order from 10:5-6 — tekiah, teruah, tekiah, three sets"),
    ('Rosh Hashanah 33b; Onkelos 10:5 — the teruah a wail', lambda: trumpets({'ask': 'teruah_form'}, DATA), 'a wail — three whimpers; the three sets by R. Abbahu'),
    ('Sifrei 73:3 — the blasts at the journeys', lambda: trumpets({'ask': 'blast_count_at_journeys'}, DATA), 'four — one per camp (Sifrei); two stated'),
    ('Sifrei 75:1 — the blemished priest blows', lambda: trumpets({'ask': 'blemished_priest'}, DATA), 'the blemished priest blows'),
    ('Num 10:9 — war', lambda: trumpets({'ask': 'oppression', 'kind': 'war'}, DATA), 'the alarm — war itself (10:9)'),
    ('Mishnah Ta\'anit 1:4-1:6 — drought', lambda: trumpets({'ask': 'oppression', 'kind': 'drought'}, DATA), "the fasts' ladder — individuals from the seventeenth of Marcheshvan, the community from Kislev, the alarm on the last seven"),
    ('Mishnah Ta\'anit 3:1 — forty days between rains', lambda: trumpets({'ask': 'oppression', 'kind': 'drought_plague'}, DATA), 'the alarm at once — forty days between rains'),
    ('Mishnah Ta\'anit 3:2 — partial rain', lambda: trumpets({'ask': 'oppression', 'kind': 'partial_rain'}, DATA), 'the alarm at once'),
    ('Mishnah Ta\'anit 3:3 — one city', lambda: trumpets({'ask': 'oppression', 'kind': 'one_city'}, DATA), 'the city sounds and fasts, the neighbors fast (R. Akiva: sound, not fast)'),
    ('Mishnah Ta\'anit 3:4 — pestilence', lambda: trumpets({'ask': 'oppression', 'kind': 'pestilence'}, DATA), 'the alarm — three dead in three days per five hundred'),
    ('Mishnah Ta\'anit 3:5 — the spreading calamities', lambda: trumpets({'ask': 'oppression', 'kind': 'spreading'}, DATA), 'everywhere — blight, mildew, locust, beasts, the sword'),
    ('Mishnah Ta\'anit 3:7 — the Sabbath', lambda: trumpets({'ask': 'oppression', 'kind': 'sabbath'}, DATA), 'even on the Sabbath — a besieged city, a flooding river, a ship at sea'),
    ('Mishnah Ta\'anit 3:8 — too much rain', lambda: trumpets({'ask': 'oppression', 'kind': 'excess_rain'}, DATA), 'no alarm — a blessing'),
    ('Mishnah Ta\'anit 2:1-2:5 — the fast\'s order', lambda: trumpets({'ask': 'fast_order'}, DATA), "twenty-four blessings, the six conclusions; the priests' blasts inside the Temple only"),
    ('Num 10:10; Mishnah Sukkah 5:4 — the days of gladness', lambda: trumpets({'ask': 'days_of_gladness'}, DATA), 'festivals, new moons, over the offerings; sets of three at the water-drawing'),
    ('Mishnah Sukkah 5:5; Mishnah Arakhin 2:3 — the Temple\'s blasts (computed)', lambda: trumpets({'ask': 'temple_blasts'}, DATA), '21 / 48 — the day 3 + 9 + 9; the Sukkot Friday 48'),
    ('Mishnah Tamid 7:3 — the daily service', lambda: trumpets({'ask': 'daily_service'}, DATA), 'nine per daily offering — three at the libation, three at the breaks'),
    ('Sukkah 55a:2 — the additional offerings', lambda: trumpets({'ask': 'musaf_blasts'}, DATA), 'one set for all the coinciding additional offerings'),
    ('Rosh Hashanah 32a:10; Mishnah Rosh Hashanah 4:5-6 — the kingship verses', lambda: trumpets({'ask': 'kingship_verses'}, DATA), 'remembrance and kingship from one verse; ten verses each'),
    ('Arakhin 11b:22; Zevachim 55a:3 — over the offerings', lambda: trumpets({'ask': 'over_offerings'}, DATA), 'the communal obligatory offerings; the communal peace offerings most holy, in the north'),
    ('Mishnah Rosh Hashanah 3:3 — with the shofar of Rosh Hashanah', lambda: trumpets({'ask': 'with_shofar', 'day': 'rosh_hashanah'}, DATA), "two trumpets at the sides, the shofar long — the day is the shofar's"),
    ('Mishnah Rosh Hashanah 3:4 — with the shofar of the fasts', lambda: trumpets({'ask': 'with_shofar', 'day': 'fast'}, DATA), "two trumpets in the middle, the shofarot short — the day is the trumpets'"),
    ('Menachot 28a:18; Mishnah Rosh Hashanah 3:6 — fragments', lambda: trumpets({'ask': 'fragments'}, DATA), 'trumpets of fragments valid; a shofar of fragments unfit'),
    ('Mishnah Rosh Hashanah 3:8 — who discharges', lambda: trumpets({'ask': 'who_discharges'}, DATA), 'the obligated only'),
    ('Mishnah Rosh Hashanah 3:7 — the hearing', lambda: trumpets({'ask': 'hearing'}, DATA), 'the sound, not the echo; intent required'),
    ('Mishnah Rosh Hashanah 3:2 — the shofar\'s kinds (the moadim engine CALLED)', lambda: trumpets({'ask': 'shofar_kinds'}, DATA), "all shofarot fit but a cow's horn"),
    # F4 — the march and the ark
    ('Num 10:11; Rosh Hashanah 3a:5 — the date', lambda: march({'ask': 'date'}, DATA), '(2, 2, 20) — the twentieth of Iyar, year two; the year does not turn in Iyar'),
    ('Num 10:14-28; Num 2 — the order (Bamidbar CALLED)', lambda: march({'ask': 'order'}, DATA), 'judah, reuben, the tent in the midst, ephraim, dan — as they camp so they journey'),
    ('Num 10:17, 10:21 — the Levites\' places', lambda: march({'ask': 'levites_places'}, DATA), 'Gershon and Merari after Judah bearing the tabernacle; Kohath after Reuben bearing the sanctuary — set up before their coming'),
    ('Menachot 98b:3 — the ark\'s bearers', lambda: march({'ask': 'ark_bearers'}, DATA), 'four bearers (two plurals)'),
    ('Shevuot 16b:4 against Eruvin 2a:14 — the sanctuary\'s name', lambda: march({'ask': 'sanctuary_name'}, DATA), "10:21's sanctuary is the ark and the vessels; the Tabernacle's name from Exod 25:8"),
    ('Num 2 = 7 = 10 — the princes\' order (computed)', lambda: march({'ask': 'princes_order'}, DATA), 'the camp\'s order a third time — 2 = 7 = 10'),
    ('Num 10:33; Taanit 29a:3; Shabbat 116a:3 — the three days', lambda: march({'ask': 'three_days'}, DATA), "three days' journey — the timer; that very day they turned (the first punishment)"),
    ('Num 10:33 — the ark\'s verb', lambda: march({'ask': 'spy_verb'}, DATA), "the ark's verb is the spies' verb — eight seats"),
    ('Sifrei 83:1 — the clouds', lambda: march({'ask': 'clouds'}, DATA), 'seven clouds (Sifrei); 13 / 4 / 2 the other settings'),
    ('Bava Kamma 83a:7; Yevamot 64a — the 22,000', lambda: march({'ask': 'shekhinah_minimum'}, DATA), '22,000 — the plurals\' minimum (the shelf\'s datum; no numeral on the ink)'),
    ('Mishnah Yadayim 3:5; Shabbat 115b:4 — the eighty-five (computed)', lambda: march({'ask': 'eighty_five'}, DATA), '85 letters — the measure of a scroll (Mishnah Yadayim 3:5)'),
    ('Shabbat 115b-116a; Sifrei 84:1 — the signs', lambda: march({'ask': 'signs'}, DATA), 'a book in itself (Rebbi) / to separate the two punishments (R. Shimon b. Gamliel)'),
    ('Num 10:29-32; Sifrei 78:3; Judg 1:16 — Hobab', lambda: march({'ask': 'hobab'}, DATA), 'asked, refused, asked again — the answer not in the ink (Judg 1:16)'),
    ('Zevachim 116a — Jethro at Sinai', lambda: march({'ask': 'jethro_at_sinai'}, DATA), 'before the giving (R. Yehoshua); after (R. Elazar HaModai)'),
    ('Taanit 29a:2-5; Seder Olam 8:2 — the day-stack', lambda: march({'ask': 'day_stack'}, DATA), 'the march (2, 2, 20); the three days to the twenty-third; Hazeroth on the twenty-second of Sivan; Paran on the twenty-ninth'),
    ('Rosh Hashanah 3a:5 — the year does not turn in Iyar', lambda: march({'ask': 'year_turns'}, DATA), 'not in Iyar — Nisan and Iyar in one year'),
    ('Sifrei 72:1, 84:5 — the cloud and the trumpets', lambda: march({'ask': 'cloud_and_trumpets'}, DATA), 'both kept — the cloud and the trumpets'),
    # F5 — Taberah, the lust, the quail
    ('Sifrei 85:1 — the people / My people', lambda: taberah_and_quail({'ask': 'the_people'}, DATA), "'the people' the wicked, 'My people' the upright"),
    ('Sifrei 85:1 — the fire at the edge', lambda: taberah_and_quail({'ask': 'fire_at_edge'}, DATA), 'the proselytes at the edge (Sifrei); the officers (R. Shimon b. Menassia)'),
    ('Num 11:2; Berakhot 32a:5 — the fire sank', lambda: taberah_and_quail({'ask': 'fire_sank'}, DATA), "sank at Moses' prayer"),
    ('Sifrei 86:1; Deut 9:22 — Taberah', lambda: taberah_and_quail({'ask': 'taberah_name'}, DATA), 'named by the event — Taberah (Deut 9:22)'),
    ('Onkelos 11:4 — the rabble', lambda: taberah_and_quail({'ask': 'rabble'}, DATA), 'the mixed multitude'),
    ('Yoma 75a:10 — the five foods', lambda: taberah_and_quail({'ask': 'five_foods'}, DATA), 'the manna tasted like all but these five (R. Ami / R. Asi)'),
    ('Yoma 75a:6 — the fish for nothing', lambda: taberah_and_quail({'ask': 'fish_for_nothing'}, DATA), "the forbidden relations ('for nothing'); fish ('which we ate')"),
    ('Yoma 75a:9; Shabbat 130a:13 — the families\' weeping', lambda: taberah_and_quail({'ask': 'families_weeping'}, DATA), 'the forbidden relations'),
    ('Yoma 75b:5 — the manna\'s taste by age', lambda: taberah_and_quail({'ask': 'manna_taste'}, DATA), 'by age — bread, oil, honey'),
    ('Yoma 75a:16 — how the manna fell', lambda: taberah_and_quail({'ask': 'manna_fell'}, DATA), 'by rank — the righteous at their doors, the average outside the camp, the wicked far off'),
    ('Yoma 75a:17 — the manna\'s form', lambda: taberah_and_quail({'ask': 'manna_form'}, DATA), 'by rank — baked, cakes, raw'),
    ('Yoma 75b:9 — the dew', lambda: taberah_and_quail({'ask': 'dew'}, DATA), 'dew above and dew below'),
    ('Yoma 75a:20 — the taste-word', lambda: taberah_and_quail({'ask': 'manna_taste_word'}, DATA), 'breast (R. Abbahu) / demon'),
    ('Num 11:19-20 — the day-ladder (the parser\'s dual)', lambda: taberah_and_quail({'ask': 'day_ladder'}, DATA), '1, 2, 5, 10, 20 — then a month'),
    ('Chagigah 17b:7; Megillah 5a:11 — a month of days', lambda: taberah_and_quail({'ask': 'month_of_days'}, DATA), 'thirty days, counted by days, no hours'),
    ('Num 11:21 — the six hundred thousand (computed)', lambda: taberah_and_quail({'ask': 'six_hundred_thousand'}, DATA), '600000 on foot'),
    ('Num 11:23 — the hand not shortened', lambda: taberah_and_quail({'ask': 'shortened_hand'}, DATA), 'not shortened — three seats'),
    ('Sanhedrin 8a:6 — the nursing-father', lambda: taberah_and_quail({'ask': 'nursing_father'}, DATA), "the judge's burden measured by Moses' clause"),
    ('Chullin 17a:6 — the wilderness\' meat', lambda: taberah_and_quail({'ask': 'wilderness_meat'}, DATA), 'slaughter (R. Yishmael); stabbing (R. Akiva)'),
    ('Num 11:31; Yoma 75b — two cubits (the parser\'s dual)', lambda: taberah_and_quail({'ask': 'quail_height'}, DATA), '2 cubits'),
    ('Chullin 27b:8-9 — the quail slaughtered', lambda: taberah_and_quail({'ask': 'quail_slaughter'}, DATA), "birds need slaughter — the quail's 'gathered' no exemption"),
    ('Num 11:32 — ten homers (computed)', lambda: taberah_and_quail({'ask': 'ten_homers'}, DATA), '10 homers the least'),
    ('Chullin 105a:8 — the meat between the teeth', lambda: taberah_and_quail({'ask': 'meat_between_teeth'}, DATA), 'still meat — no cheese until removed'),
    ('Yoma 75b:2; Sifrei 94:1 — one plague, two timers', lambda: taberah_and_quail({'ask': 'two_timers'}, DATA), 'the average at once (11:33), the wicked after a month (11:20) — one plague, two timers'),
    ('Num 11:34; Sifrei 98:1 — the graves of lust', lambda: taberah_and_quail({'ask': 'graves'}, DATA), 'Kibroth-hattaavah — the graves of lust'),
    ('Arakhin 15b:3; Pirkei Avot 5:4 — the ten trials', lambda: taberah_and_quail({'ask': 'trials'}, DATA), 'the quail among the ten trials'),
    ('Taanit 9a — the three gifts', lambda: taberah_and_quail({'ask': 'three_gifts'}, DATA), 'the well, the cloud, the manna — three gifts by three shepherds'),
    ('Yoma 75b:3 — spread or slaughtered', lambda: taberah_and_quail({'ask': 'spread_or_slaughtered'}, DATA), "spread (the ink); 'slaughtered' by Reish Lakish's re-reading"),
    # F6 — the seventy and the two
    ('Mishnah Sanhedrin 1:6; Sanhedrin 17a:1-2 — the Sanhedrin', lambda: seventy_elders({'ask': 'sanhedrin'}, DATA), '71 (the Sages); 70 (R. Yehuda)'),
    ('Sanhedrin 17a:4-5 — the lots (Bamidbar\'s box CALLED)', lambda: seventy_elders({'ask': 'lots'}, DATA), '72 ballots, 70 by lot — the box of the 273'),
    ('Horayot 4b; Kiddushin 76b; Sanhedrin 36b — with you', lambda: seventy_elders({'ask': 'with_you'}, DATA), 'counted with them / fit to rule / whole in body / of fit lineage'),
    ('Kiddushin 32b:8 — an elder', lambda: seventy_elders({'ask': 'elder_means'}, DATA), 'a sage — not merely the aged'),
    ('Sanhedrin 3b:16 — the count at the gathering', lambda: seventy_elders({'ask': 'count_when'}, DATA), 'at the gathering'),
    ('Sifrei 93:1 — the spirit set apart', lambda: seventy_elders({'ask': 'spirit'}, DATA), "set apart — Moses' spirit undiminished"),
    ('Sanhedrin 17a:12-13 — did not continue', lambda: seventy_elders({'ask': 'continued'}, DATA), 'the seventy stopped, the two did not'),
    ('Sanhedrin 17a:10 — Eldad and Medad\'s prophecy', lambda: seventy_elders({'ask': 'eldad_medad_prophecy'}, DATA), 'Moses dies and Joshua brings them in; the quail; Gog and Magog — three settings'),
    ('Sifrei 96:1; Sanhedrin 17a:14 — restrain them', lambda: seventy_elders({'ask': 'restrain_them'}, DATA), 'lay the public burden on them (Sifrei); imprison them (Sanhedrin 17a)'),
    ('Eruvin 63a:26 — Joshua childless', lambda: seventy_elders({'ask': 'joshua_childless'}, DATA), 'answered before his teacher — childless'),
    ('Sifrei 93:1 — the ten descents against the ink\'s eleven', lambda: seventy_elders({'ask': 'descents'}, DATA), "eleven on the ink against the Sifrei's ten — DIVERGE by one, open"),
    ('Num 11:29; Sanhedrin 17a:15 — would that', lambda: seventy_elders({'ask': 'would_that'}, DATA), "would that all the LORD's people were prophets"),
    # F7 — Miriam
    ('Sifrei 99:1 — Miriam first (the grammar, computed)', lambda: miriam({'ask': 'who_first'}, DATA), 'Miriam first — the feminine singular verb'),
    ('Sifrei 99:1 — dibbur', lambda: miriam({'ask': 'dibbur'}, DATA), 'harsh speech (dibbur)'),
    ('Moed Katan 16b:19; Sifrei 99:1 — the Cushite', lambda: miriam({'ask': 'cushite'}, DATA), 'distinguished by her deeds (Zipporah) — beautiful'),
    ('Shabbat 87a:4 — the separation', lambda: miriam({'ask': 'separation'}, DATA), "Moses' own a-fortiori, agreed to by God"),
    ('Keritot 9a:19 — suddenly', lambda: miriam({'ask': 'suddenly'}, DATA), 'beyond control — the three seats'),
    ('Num 12:5 — the summons (the parser\'s suffixed numeral)', lambda: miriam({'ask': 'summons'}, DATA), 'Aaron and Miriam — the summons reversed; the two came out'),
    ('Yevamot 49b; Berakhot 55b:14 — dreams and mouth to mouth', lambda: miriam({'ask': 'dreams'}, DATA), 'the prophets in dreams; Moses mouth to mouth, not in riddles'),
    ('Num 12:8; Berakhot 7a:32 — the likeness (computed)', lambda: miriam({'ask': 'likeness'}, DATA), 'seven bans on making one, one beholding (12:8)'),
    ('Shabbat 97a:2-3 — Aaron struck?', lambda: miriam({'ask': 'aaron_struck'}, DATA), 'not struck (R. Yehuda b. Beteira); struck and healed (R. Akiva)'),
    ('Num 12:10 — leprous as snow', lambda: miriam({'ask': 'as_snow'}, DATA), "Moses' hand, Miriam, Gehazi — leprous as snow"),
    ('Zevachim 101b:19-102a; Mishnah Negaim 2:5 — who declared Miriam', lambda: miriam({'ask': 'who_declared'}, DATA), 'the Holy One Himself; Moses as a priest in the installation week (Rav); not Aaron her kin'),
    ('Mishnah Negaim 2:5, 3:1 — the kin rule', lambda: miriam({'ask': 'kin_rule'}, DATA), "not his own, not his relatives' (R. Meir); only a priest declares"),
    ('Berakhot 34a:12; Mishnah Berakhot 5:5 — the short prayer (computed)', lambda: miriam({'ask': 'short_prayer'}, DATA), 'five words, the floor; forty days the ceiling; fluency the sign'),
    ('Bava Kamma 25a; Bava Batra 111a; Zevachim 69b; Mishnah Bava Kamma 2:5 — dayo', lambda: miriam({'ask': 'dayo'}, DATA), '7 of 14 — dayo is Torah law'),
    ('Moed Katan 16a:20 — admonition', lambda: miriam({'ask': 'admonition_days'}, DATA), 'seven days — admonition'),
    ('Num 12:14-15; Lev 13:4 — the quarantine (the negaim engine CALLED)', lambda: miriam({'ask': 'quarantine'}, DATA), 'shut out seven days — the leper\'s week (7)'),
    ('Yevamot 103b:16 — the grade (the negaim engine CALLED)', lambda: miriam({'ask': 'grade'}, DATA), 'confirmed — as one dead (the confirmed leper only)'),
    ('Nedarim 64b:6; Avodah Zarah 5a:19; Chullin 7b:12; Sanhedrin 47a:10 — as one dead', lambda: miriam({'ask': 'as_one_dead'}, DATA), 'the leper among the four as dead'),
    ('Mishnah Sotah 1:7, 1:9; Sotah 9b:8 — measure for measure', lambda: miriam({'ask': 'measure_for_measure'}, DATA), "an hour at the Nile, seven days' halt — measure for measure"),
    ('Num 12:15-16 — the halt', lambda: miriam({'ask': 'halt'}, DATA), 'the halt until she was gathered; then Paran'),
    ('Mishnah Moed Katan 3:1; Moed Katan 7b — the leper shaves on the festival', lambda: miriam({'ask': 'leper_shaves_on_festival'}, DATA), 'the leper shaves on the intermediate days'),
    ('Num 12:3; Nedarim 38a:9 — humble (the written-and-read pair)', lambda: miriam({'ask': 'humble'}, DATA), "humble — written without the yod, read with it"),
    ('Yoma 76a:1 — the article blocks the identity', lambda: miriam({'ask': 'article_blocks_identity'}, DATA), "'the man' no match for 'man' — the article blocks the identity"),
    ('Berakhot 63b; Makkot 10a; Taanit 7a — foolish', lambda: miriam({'ask': 'foolish'}, DATA), 'foolish, then sinned'),
    ('Deut 24:9; Arakhin 15a-16b — remember Miriam', lambda: miriam({'ask': 'remember_miriam'}, DATA), 'the paradigm of evil speech (Deut 24:9)'),
    ('Num 12:15 — the days (computed)', lambda: miriam({'ask': 'days'}, DATA), '7 days'),
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
    print('\nBEHA: %d/%d cells; the scene %s; the narrative %s' % (ok, len(CASES), SCENE, NARRATIVE))
    sys.exit(0 if ok == len(CASES) else 1)
