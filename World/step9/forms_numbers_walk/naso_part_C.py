

# ===== F6: THE PRIESTS' BLESSING (Num 6:22-27) ==============================================================
def blessing(case, data):
    del P[:]
    ask = case['ask']
    if ask == 'form':
        place = case['place']
        ink('6:23', '"THUS shall you bless the children of Israel; SAY to them"')
        move('Mishnah Sotah 7:6; Mishnah Tamid 7:2; Sotah 38a; Sifrei 39:1', 'in the Temple one blessing, the Name as written, the hands above the head (the High Priest not above the frontplate; R. Yehuda even he); in the province three with amen, the substitute, the hands at the shoulders')
        if place == 'temple':
            return out('one blessing; the Name as written; the hands above the head (the High Priest not above the frontplate)', ['blessed_by_the_priests'])
        return out('three blessings with amen; the substitute name; the hands at the shoulders', ['blessed_by_the_priests'])
    if ask == 'language':
        move('Sotah 33b:3 (R. Yehuda: "so"); 38a:2 (bless/bless with Deut 27:12)', 'the holy tongue'); return out('the holy tongue (so/so)', ['blessed_by_the_priests'])
    if ask == 'who_blesses':
        who = case['who']
        if who == 'priest':
            return out('blesses', ['blessed_by_the_priests'])
        if who == 'blemished_hands':
            b = PR.blemish('blemish_tokens')['v']                                                                     # THE CALL
            move('CALLED cold_run_priesthood.blemish(blemish_tokens) -> %s [IMPORT, live]' % b, 'the priesthood\'s blemish file; Mishnah Megillah 4:7: blemished hands — the people would look')
            return out('does not lift his hands (Megillah 4:7)', ['disqualified'])
        if who == 'drunk':
            move('Taanit 26b:16 (bar Kappara)', 'the blessing juxtaposed to the nazirite — a drunk priest may not bless'); return out('may not (the nazirite\'s juxtaposition)', ['disqualified'])
        if who in ('minor', 'exposed'):
            move('Mishnah Megillah 4:6', 'a minor does not lift his hands; the exposed not'); return out('not', ['disqualified'])
        if who == 'non_priest':
            return out('not — the priests bless', ['exempt'])
        return out('no verdict in span', [FX.NONE])
    if ask == 'quorum':
        move('Mishnah Megillah 4:3', 'not with fewer than ten'); return out('ten', ['blessed_by_the_priests'])
    if ask == 'who_is_blessed':
        ink('6:23', '"say to them"'); move('Sotah 38a:12', 'converts, women, freed slaves included'); return out('all Israel — converts, women, freed slaves', ['blessed_by_the_priests'])
    if ask == 'translated':
        move('Mishnah Megillah 4:10; Megillah 25a-b', 'read, not translated — lest "lift His face" be heard as favoritism'); return out('read, not translated', ['blessed_by_the_priests'])
    if ask == 'three_commands':
        move('Sotah 38b:4; Menachot 44a:18', 'a priest who does not ascend violates three'); return out('so you shall bless; say to them; put My name', ['blessed_by_the_priests'])
    if ask == 'priests_blessed':
        ink('6:27', '"and I will bless THEM"'); move('Chullin 49a:16 (R. Yishmael)', 'the priests bless Israel, the Holy One blesses the priests'); return out('by Heaven (I will bless them)', ['blessed_by_the_priests'])
    if ask == 'face_lifted':
        s = data['face_lifted']['value']; dat('the row face_lifted = %s: %s' % (s, data['face_lifted']['settings'][s]))
        return out('when they do His will (the Sifrei) / beyond the letter (Berakhot 20b) / before the sentence (Niddah 70b) — three reconciliations', ['blessed_by_the_priests'])
    if ask == 'counts':
        ink('6:24-26', 'words %s, letters %s — computed on the ink; the Name thrice' % (BLESS_WORDS, BLESS_LETTERS))
        return out('3, 5, 7 words; 15, 20, 25 letters; the Name thrice', ['blessed_by_the_priests'])
    if ask == 'name':
        s = data['blessing_name_by_place']['value']; dat('the row blessing_name_by_place = %s' % s); ink('6:27', '"they shall put MY NAME"')
        return out('the Name in the Temple, the substitute in the province', ['blessed_by_the_priests'])
    if ask == 'four_times':
        move('Taanit 26b', 'the four daily times of the blessing'); return out('the four daily times (Taanit 26b)', ['blessed_by_the_priests'])
    return out('no verdict in span', [FX.NONE])


# ===== F7: THE WAGONS (Num 7:1-9) ===========================================================================
def wagons(case, data):
    del P[:]
    ask = case['ask']
    if ask == 'day':
        ink('7:1', '"on the day Moses finished setting up the tabernacle" — Exod 40:33\'s finishing; the erection\'s day'); move('Sifrei 44:1; Shabbat 87b; Zevachim 101b:6', 'the day-stack of the first of Nisan — RETROGRADE after 1:1')
        return out('the erection\'s day — the day-stack (Sifrei 44:1; Shabbat 87b): RETROGRADE', ['wagons_brought'])
    if ask == 'numbers':
        ink('7:3', '"six covered wagons and twelve oxen, a wagon for two princes and an ox for one" — the parser: %s' % WAGONS)
        return out('6 wagons, 12 oxen; a wagon for two princes, an ox for one (the parser: [6, 12, 2, 1])', ['wagons_brought'])
    if ask == 'covered':
        move('Sifrei 45:1 (Rebbi); Onkelos 7:3', '"covered" — the translation\'s word'); return out('covered (Rebbi — Onkelos)', ['wagons_brought'])
    if ask == 'accepted':
        ink('7:4-5', '"take from them"'); move('Sifrei 45:1', 'not accepted until told'); return out('not accepted until told (7:4-5)', ['commanded'])
    if ask == 'distribution':
        ink('7:7-9', 'Gershon %s, Merari %s, Kohath none' % (DIST_G, DIST_M)); s = data['wagons_distribution']['value']; dat('the row wagons_distribution = %s' % s)
        return out('as Moses saw fit: Gershon 2 and 4, Merari 4 and 8, Kohath none — on the shoulder', ['wagons_assigned'])
    if ask == 'shoulder':
        ink('7:9', '"the service of the holy is upon them — on the shoulder they carry"'); move('Sifrei 46:2; Sotah 35a:22; Arakhin 11a:19', 'David\'s error and return; "they carry" as song')
        return out('David\'s error and return (the flow reversed); the song from "they carry"', ['wagons_assigned'])
    if ask == 'anointing':
        o = IS.oil('holy_anointing_oil')['v']                                                                       # THE CALL
        s = data['anointing_scope']['value']; dat('the row anointing_scope = %s: %s' % (s, data['anointing_scope']['settings'][s]))
        ink('7:1', '"he anointed it and sanctified it and all its vessels, the altar and all its vessels; he anointed THEM and sanctified them"')
        move('CALLED cold_run_incense_shekel.oil(holy_anointing_oil) -> %r [IMPORT, live]' % (o,), 'Exod 30:22-33\'s oil; "them" — Moses\' vessels by anointing, the generations\' by service (Sanhedrin 16b; Shevuot 15a); Horayot 12a: anointed, not poured')
        return out('Moses\' vessels by anointing (the liquid measures in and out, the dry inside — R. Yoshiya); the generations\' by service', ['wagons_brought'])
    return out('no verdict in span', [FX.NONE])


# ===== F8: THE DEDICATION (Num 7:10-88) =====================================================================
def dedication(case, data):
    del P[:]
    ask = case['ask']
    if ask == 'first_day':
        ink('7:10', '"on the day it was anointed"'); move('Zevachim 101b:6', 'three goats on one day — Nahshon\'s, the eighth day\'s, the New Moon\'s: the first of Nisan'); return out('the anointing day = the erection = 1 Nisan: three goats on one day (Zevachim 101b)', ['dedication_brought'])
    if ask == 'order':
        ink('7:12-83', 'the twelve by day: %s = the camp\'s 2:3-31 (computed)' % ORDER_7); s = data['princes_order']['value']; dat('the row princes_order = %s' % s); move('Sifrei 47:1, 52:1', 'by the journeying, not by birth; Reuben\'s protest, Moses\' rebuke')
        return out('by the journeying = the camp\'s order (computed = 2:3-31), not by birth; Reuben\'s protest', ['dedication_offered'])
    if ask == 'per_day':
        ink('7:11', '"one prince per day, one prince per day"'); ink('7:72, 7:78', '"on the DAY of the eleventh DAY" — the doubled day: %s' % DAY_TOKENS); move('Moed Katan 9a:11-12', 'one continuous period — the Sabbath overridden')
        return out('one prince per day — twelve dues from the anointing day, the Sabbath overridden (Moed Katan 9a)', ['dedication_offered'])
    if ask == 'same_day':
        ink('7:84, 7:88', '"on the day of its anointing" / "after it was anointed"'); move('Sifrei 53:1', 'the same day'); return out('7:84 = 7:88 — on the day of its anointing / after: the same day (Sifrei 53:1)', ['dedication_offered'])
    if ask == 'one_text':
        move('the reading (NS07A-05, computed)', 'the twelve blocks one text but the opening verb, the name, one spelling'); return out('the twelve blocks one text (computed at the reading)', ['dedication_offered'])
    if ask == 'dish':
        ink('7:13', '"one silver dish, a hundred and thirty its weight; one silver bowl, seventy shekels, by the shekel of the sanctuary" — %s' % DISH)
        move('CALLED cold_run_incense_shekel.shekel(twenty_gerah) -> %s [IMPORT, live]' % SHEKEL_SEATS, 'the sanctuary shekel = Exod 30:13\'s twenty gerah — the sela (Onkelos; Sifrei 49:1, 54:1)')
        return out('130 and 70 by the sanctuary shekel (Exod 30:13\'s twenty gerah — the sela)', ['accepted'])
    if ask == 'pan':
        ink('7:14', '"one pan, ten of gold, full of incense" — %s (M-26: the tevir on "one")' % PAN); ink('7:86', '"all the gold of the pans, a hundred and twenty" = 12 x 10 — %s' % TOTALS[86]); move('Sifrei 49:1, 55:1', 'gold weighed in silver shekels — the total decides')
        return out('ten of gold weighed in silver — 120 = 12 x 10 decides (M-26)', ['accepted'])
    if ask == 'full':
        ink('7:13', '"both of them FULL of fine flour"'); move('Menachot 8a:13; 88a:8', 'a full tenth sanctifies (R. Yosei: unless meant to add)'); return out('a full tenth sanctifies (R. Yosei: unless meant to add)', ['accepted'])
    if ask == 'bowls_sanctify_dry':
        move('Menachot 8b:5, 19b:6; Zevachim 88a:6 (Shmuel)', 'the bowls sanctify dry goods'); return out('yes (Shmuel)', ['accepted'])
    if ask == 'vessel_joins':
        s = data['vessel_joining']['value']; dat('the row vessel_joining = %s' % s); ink('7:14', '"full of incense"'); return out('Torah law (R. Chanin); R. Yochanan rabbinic', ['accepted'])
    if ask == 'animals':
        ink('7:15-17', '"one bull, one ram, one lamb of its first year for a burnt-offering; one goat for a sin-offering; two oxen, five rams, five he-goats, five lambs for peace-offerings" — %s' % BLOCK17); move('Sifrei 50:1-51:1', 'none like it in its herd; its own year')
        d = OF.dispatch('olah')                                                                                   # THE CALL
        move('CALLED cold_run_offerings.dispatch(olah) -> %s [IMPORT, live]' % sorted(d), 'the burnt-offering\'s procedure the offering engine\'s')
        return out('one bull, one ram, one lamb (burnt); one goat (sin); two oxen, five, five, five (peace) — none like it; its own year', ['accepted'])
    if ask == 'animal_age':
        m = case['months']; move('Mishnah Parah 1:3', 'lambs to a year, rams to two — day to day; thirteen months neither (a palgas)')
        return out('a lamb' if m <= 12 else ('neither (a palgas)' if m == 13 else 'a ram'), ['accepted'] if m != 13 else ['disqualified'])
    if ask == 'goat':
        ink('7:16', '"one he-goat for a sin-offering"'); move('Sifrei 51:1; Horayot 6a; Menachot 92b:7', 'for the grave of the depths; leaning — R. Yehuda yes, R. Shimon the idolatry goats'); return out('for the grave of the depths; leaning — R. Yehuda yes (R. Shimon the idolatry goats)', ['accepted'])
    if ask == 'exceptions':
        s = data['prince_exceptions']['value']; dat('the row prince_exceptions = %s: %s' % (s, data['prince_exceptions']['settings'][s]))
        return out('the Sabbath overridden; an individual\'s incense; a sin-offering not for a sin; one of each', ['accepted'])
    if ask == 'sabbath':
        move('Moed Katan 9a:11-12', 'the twelve days continuous — the Sabbath overridden'); return out('overridden — the days continuous (Moed Katan 9a)', ['accepted'])
    if ask == 'totals':
        ink('7:84-88', '%s' % TOTALS); return out('2400 = 12 x (130 + 70); 120 = 12 x 10; 12/12/12/12; 24/60/60/60 — computed', ['accepted'])
    if ask == 'credited':
        move('Sifrei 55:1-57:1', 'each credited with all twelve'); return out('each credited with all twelve (Sifrei 55:1-57:1)', ['accepted'])
    if ask == 'weights':
        move('Sifrei 54:1', 'Temple vessels weigh the same singly and together'); return out('Temple vessels weigh the same singly and together (54:1)', ['accepted'])
    return out('no verdict in span', [FX.NONE])


# ===== F9: THE VOICE (Num 7:89) =============================================================================
def voice(case, data):
    del P[:]
    ask = case['ask']
    if ask == 'reflexive':
        ink('7:89', '"he heard the Voice SPEAKING ITSELF [middabber] to him" — the hitpael by the points (the reading\'s NS07B-04); Onkelos both verbs reflexive')
        return out('the Voice speaking ITSELF (the hitpael by the points); Onkelos both verbs', ['spoken_to_from_the_ark'])
    if ask == 'third_verse':
        move('Sifrei 58:1 (I13 stated here)', 'Lev 1:1 "from the tent" against Exod 25:22 "from above the ark-cover" — 7:89 the third'); return out('Lev 1:1 against Exod 25:22 reconciled by 7:89 (I13)', ['spoken_to_from_the_ark'])
    if ask == 'exclusions':
        move('Sifrei 58:1', 'thirteen utterances to Moses and Aaron, thirteen exclusions of Aaron'); ink('the frame census', '"to Moses and to Aaron" at %d verses of Exodus-Numbers (computed)' % TO_MOSES_AND_AARON)
        return out('thirteen utterances to Moses and Aaron, thirteen exclusions — the frame census %d' % TO_MOSES_AND_AARON, ['spoken_to_from_the_ark'])
    if ask == 'who_heard':
        ink('7:89', '"speaking UNTO HIM"'); move('Yoma 4b:8', 'Moses alone at the Tent; at Sinai all heard'); return out('Moses alone at the Tent (Yoma 4b); all at Sinai', ['spoken_to_from_the_ark'])
    if ask == 'great_voice':
        move('Sifrei 58:2', 'THE voice — not low: Deut 5:19\'s great voice'); return out('not a low voice — the great voice of Sinai (58:2)', ['spoken_to_from_the_ark'])
    if ask == 'door':
        move('Yoma 4b; Sukkah 5a', 'the Voice at the door of the tent'); return out('the Voice at the door (Yoma 4b; Sukkah 5a)', ['spoken_to_from_the_ark'])
    return out('no verdict in span', [FX.NONE])


# ---- THE WRAP — the daemon, the scene, the narrative ------------------------------------------------------
PRINCE_TOKENS = ['nahshon-ben-amminadab', 'nethanel-ben-zuar', 'eliab-ben-helon', 'elizur-ben-shedeur', 'shelumiel-ben-zurishaddai', 'eliasaph-ben-deuel',
                 'elishama-ben-ammihud', 'gamaliel-ben-pedahzur', 'abidan-ben-gideoni', 'ahiezer-ben-ammishaddai', 'pagiel-ben-ochran', 'ahira-ben-enan']

def law_naso(event, world):
    """Num 4:21-7:89 (cold_run_naso.py F1-F9). installed_by boot — the standing setting for a law spoken at its verse."""
    k, src = event['kind'], event['case_source']
    E_ = lambda eff, s, cp=None, amount=None, due=None, law='', value=None: {'effect': eff, 'subject': s, 'counterparty': cp, 'amount': amount, 'due': due, 'value': value if value is not None else True, 'source_law': law, 'case_source': src}
    if k == 'gershon_service_commanded':
        return [E_('commanded', event['subject'], value='the_gershonites_count', law='F1 [INK 4:22-28 "lift the head of the sons of Gershon, them also" — the count and the soft load owed]')]
    if k == 'merari_service_commanded':
        return [E_('commanded', event['subject'], value='the_merarites_count', law='F1 [INK 4:29-33 "the sons of Merari... you shall count them" — the count and the hard load owed]')]
    if k == 'levites_work_counted':
        for val, note in (('the_kohathites_service', 'Num 4:34-37 — the sons of Kohath counted, by the mouth of the LORD by the hand of Moses'), ('the_gershonites_count', 'Num 4:38-41 — the sons of Gershon counted'), ('the_merarites_count', 'Num 4:42-45 — the sons of Merari counted')):
            world.close(event['subject'], 'commanded', note, value=val)
        return [E_('work_counted', event['subject'], value=event.get('total', WORK_TOTAL), law='F1 [INK 4:36, 4:40, 4:44, 4:48 — %s = %d; the three debits closed]' % (WORK, WORK_TOTAL))]
    if k == 'send_out_commanded':
        return [E_('commanded', event['subject'], value='the_send_out', law='F2 [INK 5:2-3 "send out of the camp every leper and every zav and everyone unclean by a corpse" — the send-out owed]')]
    if k == 'unclean_sent_out':
        world.close('israel', 'commanded', 'Num 5:4 — and the children of Israel did so, and sent them outside the camp', value='the_send_out')
        return [E_('sent_outside_the_camp', event['subject'], value='leper: all three camps; zav: two; corpse-unclean: one', law='F2 [INK 5:4; the ladder — Pesachim 67a; Sifrei 1:3-4]')]
    if k == 'wagons_brought':
        return [E_('wagons_brought', event['subject'], value='%d wagons, %d oxen' % (WAGONS[0], WAGONS[1]), law='F7 [INK 7:2-3 — six covered wagons and twelve oxen before the tabernacle]')]
    if k == 'wagons_accepted_commanded':
        return [E_('commanded', event['subject'], value='the_wagons_distribution', law='F7 [INK 7:4-5 "take from them... give them to the Levites" — the distribution owed]')]
    if k == 'wagons_assigned':
        world.close('moses', 'commanded', 'Num 7:6 — and Moses took the wagons and the oxen and gave them to the Levites', value='the_wagons_distribution')
        return [E_('wagons_assigned', event['subject'], cp='moses', value='gershon 2/4, merari 4/8, kohath none', law='F7 [INK 7:6-9 — as Moses saw fit; Kohath on the shoulder]')]
    if k == 'dedication_brought':
        return [E_('dedication_brought', event['subject'], value='the_dedication', law='F8 [INK 7:10 "the princes brought near the dedication of the altar on the day it was anointed" — to be offered by days]')]
    if k == 'dedication_order_commanded':
        day = event.get('day', world.clock.day)      # THE SEQUENTIAL RUN: the event's own day (the text's date inside the retrograde stretch — the anointing day)
        return [E_('dedication_offered', tok, due=day + n, value='day %d: %s — the dish %d, the bowl %d, the pan %d of gold; the animals %s' % (n + 1, NAMES[n], DISH[1], DISH[3], PAN[1], BLOCK17),
                   law='F8 [INK 7:11 "one prince per day"; 7:%d — the %s day; the due the anointing day + %d (Moed Katan 9a: continuous)]' % (12 + 6 * n, ['first', 'second', 'third', 'fourth', 'fifth', 'sixth', 'seventh', 'eighth', 'ninth', 'tenth', 'eleventh', 'twelfth'][n], n))
                for n, tok in enumerate(PRINCE_TOKENS)]
    if k == 'voice_heard_from_the_ark':
        return [E_('spoken_to_from_the_ark', event['subject'], value='the Voice speaking itself, from between the two cherubim', law='F9 [INK 7:89 — the reflexive by the points; Yoma 4b: Moses alone]')]
    # ---- the exam's case kinds ----
    if k == 'send_out_case':
        v, e, _ = camp_purity({'ask': 'ladder', 'who': event['who']} if event.get('camp_entered') is None else {'ask': 'entered_impure'}, DATA)
        return [E_(e[0], event['person'], value=v, law='F2 [%s]' % v)]
    if k == 'theft_confessed_case':
        v, e, _ = restitution({'ask': event['ask'], 'value': event.get('value', 100), 'swore_on_fifth': event.get('swore_on_fifth', False)}, DATA)
        return [E_(x, event['person'], cp='the-priest' if event['ask'] == 'proselyte_dead' else event.get('victim'), amount=event.get('value') if x == 'pays' else None, value=v, law='F3 [%s]' % v) for x in e if x != FX.NONE]
    if k == 'gifts_case':
        v, e, _ = restitution({'ask': event['ask'], 'age_days': event.get('age_days', 31)}, DATA)
        return [E_(e[0], event['person'], cp='the-priest', value=v, law='F3 [%s]' % v)]
    if k == 'sotah_case':
        v, e, _ = sotah({'ask': event['ask'], 'who': event.get('who'), 'what': event.get('what'), 'clean': event.get('clean', True), 'guilty': event.get('guilty'), 'merit': event.get('merit'), 'when': event.get('when'), 'for': event.get('for'), 'against': event.get('against'), 'case': event.get('case')}, DATA)
        return [E_(x, event['person'], value=v, law='F4 [%s]' % v) for x in e if x != FX.NONE]
    if k == 'nazirite_case':
        a = event['ask']
        if a == 'vow':
            term = event.get('term', DATA['nazir_default_days']['value'])
            day = event.get('day', world.clock.day)
            return [E_('nazirite_vow_bound', event['person'], value='term %d days' % term, law='F5 [INK 6:2-8; the row nazir_default_days]'),
                    E_('nazirite_term_fulfilled', event['person'], due=day + term, value='the days of his separation fulfilled', law='F5 [INK 6:13 — the term\'s due: the timer]')]
        if a == 'defiled':
            world.cancel_timers(event['person'], 'nazirite_term_fulfilled', 'Num 6:9-12 — a corpse beside him: the former days fall')
            v, e, _ = nazirite({'ask': 'defiled'}, DATA)
            day = event.get('day', world.clock.day); term = event.get('term', DATA['nazir_default_days']['value'])
            return [E_('count_voided', event['person'], value=v, law='F5 [%s]' % v),
                    E_('nazirite_term_fulfilled', event['person'], due=day + 8 + term, value='the recount from the eighth day (the row nazir_recount_day)', law='F5 [INK 6:11-12 — sanctify his head that day; the former days fall: the timer re-set]')]
        v, e, _ = nazirite({'ask': a, 'form': event.get('form'), 'who': event.get('who'), 'age': event.get('age'), 'product': event.get('product'), 'amount': event.get('amount'), 'means': event.get('means'), 'source': event.get('source'), 'mode': event.get('mode'), 'act': event.get('act'), 'day': event.get('day_of_term'), 'term': event.get('term'), 'warnings': event.get('warnings', 0), 'which': event.get('which'), 'where': event.get('where'), 'stage': event.get('stage'), 'case': event.get('case')}, DATA)
        return [E_(x, event['person'], value=v, law='F5 [%s]' % v) for x in e if x != FX.NONE]
    if k == 'blessing_case':
        v, e, _ = blessing({'ask': event['ask'], 'who': event.get('who'), 'place': event.get('place')}, DATA)
        return [E_(x, event['person'], value=v, law='F6 [%s]' % v) for x in e if x != FX.NONE]
    if k == 'dedication_case':
        v, e, _ = dedication({'ask': event['ask'], 'months': event.get('age_months', 12)}, DATA)
        return [E_(x, event['person'], value=v, law='F8 [%s]' % v) for x in e if x != FX.NONE]
    if k == 'work_count_case':
        v, e, _ = work_count({'ask': event['ask'], 'who': event.get('who', 'levite'), 'age': event.get('age', 40), 'carrying': event.get('carrying', True)}, DATA)
        return [E_(x, event['person'], value=v, law='F1 [%s]' % v) for x in e if x != FX.NONE]
    return []
