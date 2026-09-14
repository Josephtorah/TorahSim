
# =====================================================================
# Motion 1 — THE FUNCTION, compiled from the ink (F1-F6)
# =====================================================================
# ===== F1: THE HEIFER'S RITE (Num 19:1-10) ================================================================
def heifer_rite(case, data):
    """19:1-10 — the statute, the heifer's conditions as parameters, the procession, the slaughter, the seven sprinklings, the burning
    with the kit, the rite's contagion, the ashes for a keeping. Every quantity the ink leaves open is a DATA row."""
    del P[:]
    ask = case['ask']
    if ask == 'statute_indispensable':
        ink('19:2', '"this is the STATUTE of the Torah that the LORD commanded" — the statute-word on the section (its two seats %s)' % [('%s %d:%d' % k) for k in STATUTE_SEATS])
        move('Menachot 19a:10; 27a:18, 27a:29; Yoma 42a:6; Zevachim 14b:6, 68b:5', "where law and statute are stated, omission invalidates (Rav): the three of the kit, the seven sprinklings, the priest's slaughter each indispensable")
        return out('every detail indispensable — statute and law both written (19:2)', ['disqualified'])
    if ask == 'statute_seats':
        ink('19:2, 31:21', '"this is the statute of the Torah" at its two seats — the heifer and the Midian war\'s vessels (computed)')
        return out('two seats: Num 19:2, Num 31:21', [FX.NONE])
    if ask == 'frames':
        ink('19:1; 20:7, 20:12, 20:23; 21:8, 21:34', 'six frames in the portion (computed): three to Moses and Aaron together (19:1, 20:12, 20:23)')
        return out('six frames — 19:1, 20:7, 20:12, 20:23, 21:8, 21:34', [FX.NONE])
    if ask == 'yoke':
        ink('19:2', '"upon which never came a yoke" — the yoke clause (1 Sam 6:7 its other seat: the ark-cows)')
        dat('the row heifer_yoke: %s' % data['heifer_yoke']['value'])
        move('Avodah Zarah 23a:6; Sotah 46a:11, 46a:16; Shabbat 52a:7; Pesachim 26a:16; Mishnah Parah 2:3-4', 'any burden placed disqualifies (Rav); the bit no burden; threshing by intent; for its own sake valid, for another\'s invalid; a male mounted invalid')
        burden = case.get('burden', 'sacks')
        if burden in ('bit', 'rope', 'sandal', 'cloak_against_flies', 'bird'):
            return out('valid — for its own sake, no burden (Parah 2:3-4; Shabbat 52a)', ['accepted'])
        return out('disqualified — a burden came on it (19:2; Rav: a bundle of sacks)', ['disqualified'])
    if ask == 'blemish':
        ink('19:2', '"whole, in which there is no blemish" — the blemish clause; "wherein [bah]" excludes the eglah arufah (Sotah 46a:2)')
        move('CALLED cold_run_priesthood.blemish(beast_unfits_in_man) -> %s; blemish(passed_blemish) -> %s [IMPORT, live]' % (PR_BEAST, PR_PASSED), 'all blemishes that invalidate consecrated animals invalidate the heifer (Mishnah Parah 2:3); the passed blemish fit')
        dat('the row heifer_blemish: %s' % data['heifer_blemish']['value'])
        if case.get('passed'):
            return out('fit — the blemish passed (the priesthood engine\'s row)', ['accepted'])
        return out('disqualified by any consecrated-animal blemish (Parah 2:3; Sotah 46a:2)', ['disqualified'])
    if ask == 'age':
        ink('19:2', '"a red heifer" — NO AGE in the ink')
        dat('the row heifer_age: %s' % data['heifer_age']['value'])
        return out('three or four years (the Sages); R. Eliezer two; R. Meir even five — DATA', [FX.NONE])
    if ask == 'hairs':
        ink('19:2', '"red" — the color; NO count of hairs in the ink')
        dat('the row heifer_hairs: %s' % data['heifer_hairs']['value'])
        return out('two black or white hairs in one follicle invalidate (Parah 2:5) — DATA', ['disqualified'])
    if ask == 'pregnant':
        dat('the row heifer_pregnant: %s' % data['heifer_pregnant']['value'])
        return out('invalid (the Sages); R. Eliezer valid — DATA (Parah 2:1)', ['disqualified'])
    if ask == 'from_gentile':
        ink('19:2', '"speak to the children of Israel that they take to you" — the phrase Exod 25:2 shares')
        dat('the row heifer_from_gentile: %s' % data['heifer_from_gentile']['value'])
        return out('valid from gentiles (the Sages — Parah 2:1); R. Eliezer no (Avodah Zarah 23a-24a)', ['accepted'])
    if ask == 'who_burns':
        ink('19:3', '"you shall give IT to Eleazar the priest" — the deputy named for the first')
        dat('the row who_burns: %s' % data['who_burns']['value'])
        move('Yoma 42b:10-11, 43a:3; Mishnah Parah 4:1', "the first by Eleazar alone; after it even a common priest (some say) / the high priest (some say; Parah 4:1 — R. Yehuda valid otherwise)")
        return out('the first by Eleazar the deputy; later heifers by a common priest (some say) or the high priest — DATA', [FX.NONE])
    if ask == 'who_slaughters':
        ink('19:3', '"and he shall slaughter it BEFORE HIM" — Eleazar named, the slaughter watched')
        dat('the row who_slaughters: %s' % data['who_slaughters']['value'])
        move('Yoma 42a:6-11; Menachot 6b:11; Zevachim 14b:6, 68b:5', "Shmuel: a non-priest slaughters and Eleazar watches — valid; Rav: 'Eleazar the priest' and 'statute' — a priest, else invalid")
        return out('a stranger\'s slaughter valid with Eleazar watching (Shmuel); Rav: a priest — DISPUTE', [FX.NONE])
    if ask == 'slaughter_whole':
        ink('19:3, 19:5', '"he shall slaughter... he shall burn" — as the slaughter is whole so the burning is whole')
        move('Chullin 11a:15', 'the majority followed — not a tereifa (the principle of the unquantifiable majority from the heifer)')
        return out('burned whole as slaughtered whole — the majority followed (Chullin 11a)', ['accepted'])
    if ask == 'slaughter_not_neck':
        ink('19:2-3', '"the statute" with "he shall slaughter it" — slaughter fits, neck-breaking does not')
        move('Chullin 24a:1', 'with slaughter yes, with breaking the neck no')
        return out('slaughter only — neck-breaking invalid (Chullin 24a)', ['disqualified'])
    if ask == 'slaughter_alone':
        ink('19:3', '"he shall slaughter IT" — it, not it and another')
        move('Chullin 32a:2', 'slaughtered together with even a non-sacred animal the heifer is disqualified (Rava for R. Natan)')
        return out('disqualified with another animal in one act (Chullin 32a)', ['disqualified'])
    if ask == 'outside_the_camp':
        ink('19:3-4', '"outside the camp... toward the front of the tent of meeting" — three camps, east')
        move('Yoma 68a:9; Zevachim 105b:17, 113a:4-5; Yoma 2a:6; Mishnah Parah 3:6, 4:2', "burned outside three camps, east of Jerusalem opposite the entrance (R. Eliezer); slaughtered within the walls or not opposite the entrance — disqualified; the ramp to the Mount of Olives; its own pit")
        return out('outside three camps, east, opposite the entrance — the Mount of Olives by the ramp (Yoma 68a; Parah 3:6)', ['accepted'])
    if ask == 'sprinkling':
        ink('19:4', '"with his finger... toward the front of the tent of meeting seven times" — the parser\'s %s' % SEVEN)
        move('CALLED cold_run_chatat.sprinklings(anointed) -> %d; cold_run_yoma.service_order() 16:14 -> %r [IMPORT, live]' % (CH_SEVEN, YM_1614), "the sin-bull's seven and the Day's finger — the seat's kin")
        dat('the row sprinkle_toward: %s' % data['sprinkle_toward']['value'])
        move('Menachot 27a:14, 27a:29, 27b:2; Zevachim 40a:1; Mishnah Parah 3:9, 4:2; Menachot 27b:15', 'seven indispensable, each its own dip, for its name and toward the entrance; the seventh from the sixth invalid, an eighth from the seventh valid; R. Yehuda: precisely toward')
        return out('seven sprinklings toward the entrance, each its own dip, all indispensable (19:4 [7]; Parah 3:9, 4:2)', ['sprinkled_seven'])
    if ask == 'finger_wipe':
        ink('19:4-5', '"with his finger" (19:4); "its blood" burned (19:5)')
        move('Menachot 7b:20; Zevachim 93b:14; Mishnah Parah 3:9', 'after the sprinklings the hand wiped on the body; between them the finger on the bowl\'s lip (Abaye — Ezra 1:10\'s bowls)')
        return out('the hand wiped on the heifer after the seventh; the finger on the bowl\'s lip between (Zevachim 93b)', [FX.NONE])
    if ask == 'burn_list':
        ink('19:5', '"its hide, its flesh and its blood with its dung" — %s; the sin-bull\'s lists (Exod 29:14, Lev 4:11, 16:27) carry no blood-word: %s (computed)' % (BURN_19, BLOOD_AT_SIN_BULL))
        move('CALLED cold_run_chatat.carcass(anointed) -> %s; blood(anointed) -> %s [IMPORT, live]' % (CH_CARCASS, CH_BLOOD), "the sin-bull's carcass burned outside the camp; its blood brought INSIDE — the heifer's blood burned with the flesh instead (Menachot 7b:20; Zevachim 93b:14)")
        return out('the sin-bull\'s burn-list WITH THE BLOOD ADDED — burned whole with its blood (19:5; Zevachim 93b)', ['accepted'])
    if ask == 'kit':
        ink('19:6', '"cedar wood and hyssop and scarlet" cast into the burning — the order %s = the house\'s dipping at Lev 14:51-52 %s; the three takings 14:4 / 14:6 / 14:49 %s (measured at six seats)' % (KIT_19, KIT_14_51, KIT_14_49))
        move('CALLED cold_run_metzora.birds(kit) -> %s [IMPORT, live]' % MZ_KIT, "the leper's four (two birds, cedar, scarlet, hyssop) — the heifer's three")
        dat('the row bundle: %s' % data['bundle']['value'])
        move('Menachot 27a:13, 27a:18; Mishnah Menachot 3:6; Yoma 41b:18, 43a:4; Mishnah Parah 3:10-11', 'the three indispensable by "statute"; by a priest; burned in the air before the mass valid, singed before it replaced; asked thrice, wrapped, cast')
        return out('cedar, hyssop and scarlet — the three indispensable, cast into the burning by a priest (19:6; Menachot 27a)', ['accepted'])
    if ask == 'kit_order':
        ink('19:6; Lev 14:4, 14:6, 14:49, 14:51, 14:52', 'the kit\'s order at the six seats (computed): the heifer %s; the takings 14:4 %s, 14:6 %s, 14:49 %s; the house\'s dipping 14:51 %s, 14:52 %s' % (KIT_19, KIT_14_4, KIT_14_6, KIT_14_49, KIT_14_51, KIT_14_52))
        return out('the heifer\'s order is Lev 14:51-52\'s (cedar, hyssop, scarlet — the house\'s dipping); the takings 14:4, 14:6, 14:49 have cedar, scarlet, hyssop — computed at six seats', [FX.NONE])
    if ask == 'priest_in_garments':
        ink('19:7', '"the PRIEST shall wash his garments... and the priest shall be unclean until the evening" — the priest restated')
        move('Yoma 43a:5; Mishnah Parah 4:1', 'in his priestly state — the garments worn, in future generations too; prepared in WHITE garments; not in all the garments invalid')
        return out('by a priest in his garments — white garments (Parah 4:1; Yoma 43a)', ['accepted'])
    if ask == 'work_invalidates':
        ink('19:3-9', 'the rite\'s stages from the slaughter to the ashes')
        dat('the row work_invalidates: %s' % data['work_invalidates']['value'])
        move('Mishnah Parah 4:4, 7:1-12, 8:1', 'other work invalidates until it is ashes; the water\'s filling and mixing by the purpose test; the two guards')
        return out('other work invalidates from the slaughter until the ashes; the water until the ashes are in it (Parah 4:4, 7)', ['disqualified'])
    if ask == 'sequestering':
        ink('19:2', '"that the LORD commanded" — with Lev 8:34\'s "commanded"')
        move('Yoma 2a:10; Mishnah Parah 3:1', 'sequestered seven days before the heifer as before the inauguration; sprinkled all seven (R. Yose: the third and seventh)')
        return out('seven days\' sequestering in the Stone Chamber, sprinkled through them (Yoma 2a; Parah 3:1)', ['accepted'])
    if ask == 'procession':
        move('Mishnah Parah 3:2-3, 3:6-8', 'the children born over the hollow, the oxen with doors, the Shiloah\'s water, the ashes taken by a child; the ramp; the pile of cedar, pine, spruce and fig wood facing west; the immersion')
        return out('the children\'s water, the child\'s mixing, the ramp to the Mount of Olives, the pile facing west (Parah 3:2-8)', [FX.NONE])
    if ask == 'tvul_yom':
        ink('19:19, 19:9', '"the CLEAN one shall sprinkle on the unclean" — clean by inference from unclean; "a clean man" gathers')
        dat('the row tvul_yom_fit: %s' % data['tvul_yom_fit']['value'])
        move('Yoma 43b:3; Zevachim 17b:3; Yevamot 73a:1; Mishnah Parah 3:7', 'the tevul yom fit to sprinkle and to burn; the burning priest deliberately defiled and immersed against the Sadducees')
        return out('the tevul yom fit — the burner defiled on purpose against the Sadducees (Parah 3:7; Yoma 43b)', ['accepted'])
    if ask == 'gatherer':
        ink('19:9', '"a MAN who is PURE shall gather the ashes of the heifer and PLACE them" — three words')
        dat('the row who_sanctifies: %s; the row a_clean_man: %s' % (data['who_sanctifies']['value'], data['a_clean_man']['value']))
        move('Yoma 43a:7; Yevamot 72b:16', "'a man' a non-priest; 'pure' even a woman; 'place' excludes the deaf-mute, imbecile and minor; the sanctifier as the gatherer")
        return out('a non-priest and a woman gather; the deaf-mute, imbecile and minor do not (Yoma 43a:7)', ['ashes_kept_for_niddah_water'])
    if ask == 'ashes_thirds':
        ink('19:9', '"lay them outside the camp in a clean place... for a keeping, for waters of niddah" — "for a keeping" the manna jar\'s and Aaron\'s staff\'s word')
        dat('the row ashes_thirds: %s' % data['ashes_thirds']['value'])
        return out('three parts — the rampart, the Mount of Olives, the priestly watches (Parah 3:11); kept for waters of niddah', ['ashes_kept_for_niddah_water'])
    if ask == 'meilah':
        ink('19:9', '"it is a SIN OFFERING" — Exod 29:14\'s formula')
        dat('the row meilah_on_the_heifer: %s' % data['meilah_on_the_heifer']['value'])
        move('CALLED cold_run_vayikra5.sacrilege(meilah) -> %s [IMPORT, live]' % V5_MEILAH, "me'ilah applies to the heifer by Torah law (Menachot 51b:22); always subject to trespass (Parah 4:4)")
        return out('me\'ilah applies — a sin offering (19:9; Menachot 51b): the principal, the fifth, the ram', ['pays'])
    if ask == 'for_its_name':
        move('Mishnah Parah 4:1, 4:3', 'slaughtered, received or sprinkled not for its name invalid (R. Eliezer valid); the intention to eat its flesh harmless (R. Eliezer: no intention invalidates)')
        return out('not for its name invalid; the eating intention harmless (Parah 4:1, 4:3)', ['disqualified'])
    if ask == 'nine_heifers':
        ink('19:2', 'the heifer commanded — its first burning NEVER NARRATED in the ink: the tape\'s debit OPEN')
        dat('the row nine_heifers: %s' % data['nine_heifers']['value'])
        return out('nine heifers — Moses, Ezra, seven after (the Sages; R. Meir five): the shelf\'s run of the open debit (Parah 3:5)', [FX.NONE])
    if ask == 'day_and_priest':
        ink('19:2, 19:19', '"law" includes the rite\'s stages; "THIS is the statute" excludes the gathering, the filling and the sanctification; "on the third DAY"')
        move('Yoma 42b:3-4; Mishnah Parah 4:4', 'the slaughter, the blood, the sprinkling, the burning and the casting by a man by day; the ashes, the water and the mixing not so bound')
        return out('the rite\'s stages by a priest by day; the gathering, filling and mixing not so bound (Yoma 42b; Parah 4:4)', ['accepted'])
    if ask == 'attention':
        ink('19:3, 19:5, 19:9', '"before him" / "in his sight" / "it shall be kept" — the attention clauses')
        move('Yoma 42a:11, 42b:1', 'no diverting of attention from the slaughter to the completion, through the gathering; the casting of the kit excepted')
        return out('attention undiverted from the slaughter through the keeping; the kit\'s casting excepted (Yoma 42a-b)', ['accepted'])
    if ask == 'defiles_garments':
        ink('19:7-8, 19:10', '"the priest shall be unclean until the evening... he who burns it... he who gathers" — the rite\'s three made unclean (impure_until_evening each)')
        move('Mishnah Parah 4:4, 8:3; Yoma 14a', "everyone occupied from the slaughter to the ashes defiles his garments; the heifer itself does not — the paradox: 'that which defiled you did not defile me'")
        return out('the burner, the gatherer and the priest unclean until evening — the rite defiles its servants, the heifer does not (Parah 4:4, 8:3)', ['impure_until_evening'])
    if ask == 'wood':
        move('Mishnah Parah 3:8, 4:3', 'the pile of cedar, pine, spruce and fig wood; burned with any wood, straw or stubble valid; flayed and cut valid')
        return out('any wood, straw or stubble valid; the pile\'s four woods (Parah 3:8, 4:3)', ['accepted'])
    if ask == 'taken_out_alone':
        ink('19:3', '"he shall bring IT out" — it alone')
        move('Yoma 42b:12; Mishnah Parah 3:7', 'no black cow, no second red heifer taken out with it (Rebbi from "it"; the Sages lest people say)')
        return out('brought out alone — no black cow, no second red one (Parah 3:7; Yoma 42b)', ['accepted'])
    if ask == 'who_sprinkles_blood':
        ink('19:4', '"Eleazar the priest shall take of its blood with his finger" — Eleazar named again')
        move('Yoma 43a:3; Kiddushin 36b:2', "Shmuel: returned to Eleazar for the blood; Rav: a restrictive after a restrictive includes a common priest; women excluded a fortiori")
        return out('a priest sprinkles the blood — Eleazar (Shmuel) or any priest (Rav); not a woman (Kiddushin 36b)', ['accepted'])
    if ask == 'madaf':
        dat('the row madaf: %s' % data['madaf']['value'])
        move('Mishnah Parah 10:1-6', "the heifer-purity's stringency: the hatat-clean touching food with the hand unclean, with the foot clean; the flask over the oven disputed; the two flasks")
        return out('madaf — the unclean has it, the clean not (the Sages; Parah 10:1); the hand defiles, the foot not (10:2)', ['disqualified'])
    if ask == 'first_heifer_open':
        ink('19:1-22', 'the statute spoken; no verse of the Torah narrates the first heifer\'s burning')
        return out('the heifer\'s debit OPEN on the tape — the ink never narrates the first burning; Parah 3:5 the shelf\'s run', [FX.NONE])
    return out('no verdict in span', [FX.NONE])


# ===== F2: THE CORPSE'S UNCLEANNESS AND THE SPRINKLING (Num 19:11-22) ======================================
def corpse_tumah(case, data):
    """19:11-22 — the toucher's seven days, the third and the seventh as timers with the four failure states, the punishment split, the
    tent, the open vessel, the field's four sources, the water and the sprinkler; the removes and the geometry as data (Oholot)."""
    del P[:]
    ask = case['ask']
    day = case.get('day', 0)
    if ask == 'seven_days':
        ink('19:11', '"he who touches the dead of any human soul shall be unclean SEVEN days" — the parser\'s %s; "a human soul" the blasphemer\'s clause (Lev 24:17)' % SEVENS[0])
        return out('unclean seven days — the toucher (19:11)', ['corpse_unclean_seven_days'])
    if ask == 'schedule':
        ink('19:12, 19:19', '"he shall purify himself on the third day and on the seventh day" — the ordinal reader\'s %s and %s' % (SCHEDULE, SCHEDULE_19))
        dat('the row third_day_fixed: %s' % data['third_day_fixed']['value'])
        move('Kiddushin 62a:4-7; Shabbat 16b:3; Sifrei 125', 'the third excludes the second, the seventh the sixth; the third and the eighth invalid — a fixed interval; both needed even for terumah')
        third, seventh = case.get('third', True), case.get('seventh', True)
        if third and seventh:
            return out('sprinkled on the third and the seventh: clean in the evening of the seventh (19:12, 19:19)', ['sprinkling_due_third_day', 'sprinkling_due_seventh_day', 'declared_pure'])
        if third and not seventh:
            return out('the seventh omitted: not clean (19:12b)', ['sprinkling_due_third_day', 'not_purified'])
        if seventh and not third:
            return out('the third omitted: the seventh does not clean — the interval fixed (Kiddushin 62a)', ['sprinkling_due_seventh_day', 'not_purified'])
        return out('neither sprinkling: not clean — his uncleanness is yet on him (19:13)', ['not_purified'])
    if ask == 'purification':                                                  # THE PAID EDGE naso -> chukat: 5:2's corpse-unclean sent out of the Presence's camp — his purification here
        ink('19:12, 19:19', 'the corpse-unclean purified by the water of niddah on the third and the seventh day; sent out of the Presence\'s camp alone (5:2 — naso\'s ladder)')
        return out('the third and the seventh day\'s sprinkling with the water of niddah, then the wash, the bath and the evening (19:12, 19:19)', ['sprinkling_due_third_day', 'sprinkling_due_seventh_day', 'declared_pure'])
    if ask == 'sprinkling_water':                                              # THE PAID EDGE beha -> chukat: 8:7's water of purification on the Levites
        ink('19:9, 19:17-18', '"waters of niddah" — the ashes kept for it; living water into a vessel; a clean man dips hyssop and sprinkles')
        return out('the heifer\'s ashes on living water in a vessel, sprinkled with hyssop by a clean man (19:9, 19:17-18) — 8:7\'s water', ['declared_pure'])
    if ask == 'minor':
        dat('the row minor_and_karet: %s' % data['minor_and_karet']['value'])
        move('Arakhin 3a:6-7; Niddah 44a:7', "'the persons that were there' — a minor becomes impure, a day old; 'the man' excludes him from the karet")
        return out('a minor impure (even a day old), no karet for his entry (Arakhin 3a; Niddah 44a)', ['corpse_unclean_seven_days', 'exempt'])
    if ask == 'toucher_of_toucher':
        ink('19:22', '"whatever the unclean touches shall be unclean, and the soul that touches shall be unclean until the evening"')
        move('Avodah Zarah 37b:7, 37b:9; Mishnah Oholot 1:1', 'the toucher of the toucher impure by Torah law — until evening: the second grade')
        return out('the toucher of the toucher unclean until evening (19:22; Oholot 1:1)', ['impure_until_evening'])
    if ask == 'removes':
        dat('the row removes: %s' % data['removes']['value'])
        move('Mishnah Oholot 1:1-4; Kelim 1:4; Avodah Zarah 37b:9', 'two, three, four defiled through a corpse; the tent does not count; the corpse the top of the ladder')
        return out('the removes — the toucher seven days, the second until evening; vessels three in a series, persons two (Oholot 1:1-4)', ['corpse_unclean_seven_days', 'impure_until_evening'])
    if ask == 'karet_entry':
        ink('19:13, 19:20', '"he has defiled the TABERNACLE of the LORD, and that soul shall be cut off" / "the SANCTUARY of the LORD" — the Sifrei\'s pair; the punishment here, the prohibition at 5:3')
        dat('the row punishment_split: %s' % data['punishment_split']['value'])
        move('Makkot 14b:6, 14b:8, 8a:16, 8b:1; Zevachim 33b:5, 43b:8; Shevuot 7b:1, 2a:2; Nazir 45a:5; Mishnah Keritot 1:1-2; Mishnah Shevuot 1:1-2:5', "karet and lashes for the impure who entered; the met mitzvah's burier not exempt; any impurity; the body's impurity; the tevul yom and the lacking-atonement included; the unwitting's sliding-scale offering; the awareness grid as data")
        if case.get('intent') == 'unwitting':
            return out('unwitting entry — the sliding-scale offering by the awareness grid (Mishnah Shevuot 1:1-2:5; Keritot 1:2)', ['disqualified'])
        return out('cut off — the intentional entry of the impure into the sanctuary; lashes with it (19:13, 19:20; Makkot 14b)', ['karet_cut_off', 'lashes'])
    if ask == 'high_priest_exempt':
        dat('the row high_priest_exempt: %s' % data['high_priest_exempt']['value'])
        return out('the high priest exempt from the entry\'s karet (Horayot 9b; Parah 12:4)', ['exempt'])
    if ask == 'impure_inside':
        move('Shevuot 16b:1; Mishnah Shevuot 2:3', 'the second verse (19:20) for one made impure INSIDE the courtyard who bowed, tarried or left by the longer route: liable; the shortest way exempt')
        return out('made impure inside: liable unless he leaves by the shortest way (Shevuot 16b; Mishnah Shevuot 2:3)', ['disqualified'])
    if ask == 'metal_vessels_decree':
        move('Shabbat 16b:3', "the Sages' decree of previous impurity on metal vessels — a fence for the purification water's use")
        return out('metal vessels keep their impurity until the sprinkling — the Sages\' fence (Shabbat 16b)', ['disqualified'])
    if ask == 'tent':
        ink('19:14', '"this is the Torah: a man who dies in a tent — everyone who comes into the tent and everything in the tent shall be unclean seven days"')
        dat('the row tent_measure: %s; the row tent_material: %s' % (data['tent_measure']['value'], data['tent_material']['value']))
        move('Mishnah Oholot 3:6-7; Shabbat 17a:2; Sukkah 21a:1; Shabbat 28a:1', 'the handbreadth; any shelter (the Rabbis) / man-made (R. Yehuda); linen by the analogy, widened')
        return out('the tent\'s enterers and contents unclean seven days — by the handbreadth (19:14; Oholot 3:6-7)', ['tent_unclean', 'corpse_unclean_seven_days'])
    if ask == 'tent_gentile':
        dat('the row tent_gentile: %s' % data['tent_gentile']['value'])
        return out('gentiles\' graves defile by touch and carrying, not by tent (Bava Metzia 114b; Yevamot 61a)', ['exempt'])
    if ask == 'tent_limbs':
        move('Bekhorot 45a:20', "'when a person dies in a tent' — only what is equal for all people (the limbs found only in a woman do not defile in a tent)")
        return out('the tent\'s impurity from the limbs equal for all (Bekhorot 45a)', [FX.NONE])
    if ask == 'tent_material':
        dat('the row tent_material: %s' % data['tent_material']['value'])
        return out('any shelter (the Rabbis — "tent, tent" amplifies); R. Yehuda man-made (Sukkah 21a; Shabbat 28a)', [FX.NONE])
    if ask == 'tent_measure':
        dat('the row tent_measure: %s' % data['tent_measure']['value'])
        return out('a handbreadth square blocks and conveys; a corpse\'s opening four; the beam\'s circumference three round, four square (Oholot 3:6-7, 12:6-7)', [FX.NONE])
    if ask == 'overshadowing_table':
        move('Mishnah Oholot 4-15', "the cupboard, the oven, the hatch, the hive, the projection, the split house, the partitions — the tradition's tables of overshadowing as DATA: 'the manner of uncleanness is to go out and not to go in'; a cubic handbreadth the unit")
        return out('the overshadowing tables as DATA (Oholot 4-15) — the handbreadth the unit; out, not in', [FX.NONE])
    if ask == 'open_vessel':
        ink('19:15', '"and every open vessel that has no cord-bound cover upon it is unclean" — Onkelos inserts OF EARTHENWARE')
        dat('the row vessel_census: %s; the row tzamid_patil: %s' % (data['vessel_census']['value'], data['tzamid_patil']['value']))
        move('Chullin 25a:3, 25a:10, 71a:24; Chagigah 22a:19, 25a:5; Shabbat 84b:3; Mishnah Kelim 9:1-10:8; Oholot 5:3-7, 8:6; Eduyot 1:14; Parah 11:1', 'the earthenware\'s airspace; the tight cover protects (not holies; not the hatat water itself); the materials; Beit Shammai\'s foods-only arm, Beit Hillel retracted')
        if case.get('covered'):
            return out('protected — a cord-bound cover on it: earthenware protects foods, liquids and earthenware; the other vessels everything (19:15; Kelim 10:1)', ['exempt'])
        return out('unclean — an open vessel in the tent (19:15; Kelim 10:1)', ['open_vessel_unclean'])
    if ask == 'field_sources':
        ink('19:16, 19:18', '"one slain by the sword, or a dead body, or a human bone, or a grave" — the four; reordered at 19:18: %s -> %s (computed)' % (SRC_16, SRC_18))
        dat('the row field_phrase: %s; the row bone_measure: %s' % (data['field_phrase']['value'], data['bone_measure']['value']))
        move('Nazir 53b:10, 54a:1; Chullin 2b:14, 72a:6; Avodah Zarah 37b:5; Mishnah Oholot 2:1-7', 'the Sages\' four readings: the overlier, the limb from the living, the barley-grain bone, the sealed grave that breaks through; the tent\'s list as data')
        return out('the four sources — the slain, the dead, the bone (a barley-grain), the grave: unclean seven days (19:16; Nazir 54a; Oholot 2)', ['corpse_unclean_seven_days'])
    if ask == 'sword_like_slain':
        dat('the row sword_like_slain: %s' % data['sword_like_slain']['value'])
        return out('a sword is like the slain — the metal vessel takes the corpse\'s grade (Pesachim 14b, 79a; Shabbat 101b)', ['corpse_unclean_seven_days'])
    if ask == 'fetus_in_womb':
        dat('the row field_phrase: %s' % data['field_phrase']['value'])
        return out('the dead fetus in the womb — excluded (R. Yishmael) / impure from "of the life" (R. Akiva) — DISPUTE (Chullin 72a)', [FX.NONE])
    if ask == 'quarter_log_blood':
        ink('19:13', '"of the LIFE of a person that died" — a quarter-log of blood, the life (Deut 12:23)')
        dat('the row bone_measure: %s' % data['bone_measure']['value'])
        move('Chullin 72a:8; Mishnah Oholot 2:2, 3:2-5', 'a quarter-log defiles like the corpse; absorbed in the ground clean; mixed blood the arms')
        return out('a quarter-log of blood defiles as the corpse (Chullin 72a; Oholot 2:2)', ['corpse_unclean_seven_days'])
    if ask == 'living_water':
        ink('19:17', '"living water into a vessel" — Isaac\'s well\'s word (Gen 26:19)')
        dat('the row living_water: %s' % data['living_water']['value'])
        move('Pesachim 34b:13; Sanhedrin 5b:7; Mishnah Parah 6:4-5, 8:8-11; Mikvaot 1:8', 'the spring\'s water drawn into a vessel; the conduit\'s susceptibility; the seas, marsh and mixed rivers unfit; the sixth degree')
        return out('spring water drawn straight into a vessel; the seas and the marsh rivers unfit (Pesachim 34b; Parah 8:8-11)', ['accepted'])
    if ask == 'mixing_order':
        ink('19:17', '"of the DUST of the burning" — ashes called dust (19:9-10 ashes; 19:17 dust — the two words)')
        dat('the row mixing_order: %s' % data['mixing_order']['value'])
        move('Sotah 16b:15; Temurah 12b:7; Chullin 88b:8; Sukkah 37b:1; Mishnah Parah 6:1-3', 'the ashes ON the water (the sotah analogy); by hand, intentionally; the sponge')
        return out('the ashes upon the water, by hand and with intent — the dust-word for the sotah analogy (Sotah 16b; Parah 6:1)', ['accepted'])
    if ask == 'sprinkler_who':
        dat('the row sprinkler_who: %s' % data['sprinkler_who']['value'])
        return out('a man, not a woman (a minor by "pure"); R. Yehuda: an adult, a woman by "pure" — DISPUTE (Yoma 43a; Parah 12:10)', [FX.NONE])
    if ask == 'who_sanctifies':
        dat('the row who_sanctifies: %s' % data['who_sanctifies']['value'])
        return out('as the gatherer — a woman sanctifies; two take and one puts (Yevamot 72b; Yoma 43a)', ['accepted'])
    if ask == 'sprinkling_day':
        dat('the row sprinkling_day: %s' % data['sprinkling_day']['value'])
        return out('by day, from sunrise; dipped by day and sprinkled at night invalid (Megillah 20a; Parah 12:11)', ['disqualified'])
    if ask == 'sprinkling_on_pure':
        move('Yoma 14a:5; Mishnah Parah 12:3', "R. Akiva: sprinkled on the pure he becomes impure; the Rabbis: only on the susceptible counts; the intention grid")
        return out('sprinkling counts only on the susceptible (the Rabbis); R. Akiva: the pure sprinkled becomes impure — DISPUTE', [FX.NONE])
    if ask == 'sprinkler_carrier':
        ink('19:21', '"he who sprinkles the water of niddah shall wash his clothes, and he who touches shall be unclean until the evening"')
        dat('the row sprinkler_or_carrier: %s' % data['sprinkler_or_carrier']['value'])
        move('Yoma 14a:9; Niddah 9a:15; Mishnah Parah 12:5; Kelim 1:1-2', "'sprinkles' = carries a sprinkling's worth: the sprinkler clean, the carrier's grade heavier than the toucher's")
        return out('the sprinkler clean, the carrier washes his clothes, the toucher unclean until evening (19:21; Yoma 14a)', ['washes_and_bathes', 'impure_until_evening'])
    if ask == 'hyssop_dip':
        ink('19:18', '"a clean man shall take hyssop and dip it in the water and sprinkle" — the Passover\'s two verbs (Exod 12:22)')
        move('Sukkah 37a:8; Menachot 7b:9; Zevachim 93b:5; Gittin 86b:14; Mishnah Parah 12:1-2', 'lengthened by a string valid (taking by another object); enough water from the outset; the diminished water by the tips; the doubts invalid')
        return out('the hyssop dipped in the vessel\'s own water, lengthened if short; the doubts invalid (Sukkah 37a; Parah 12:1-2)', ['accepted'])
    if ask == 'hyssop_species':
        move('CALLED cold_run_metzora.birds(hyssop) -> %s [IMPORT, live]' % MZ_HYSSOP, "the leper's hyssop the same species")
        move('Mishnah Parah 11:7-9', 'plain hyssop — not lavender, blue, Roman or wild; three stalks with three buds; the leper\'s shared')
        return out('plain hyssop of three stalks — the leper\'s kind; the named kinds invalid (Parah 11:7-9)', ['accepted'])
    if ask == 'water_measure':
        dat('the row sprinkler_measure: %s' % data['sprinkler_measure']['value'])
        return out('enough to dip the tips of the buds and sprinkle (Parah 12:5; Sifrei 129); under it a father by contact, above by carrying (Kelim 1:1-2)', [FX.NONE])
    if ask == 'connection':
        move('Shabbat 48b:10, 58b:11; Mishnah Parah 12:8-10', 'parts that come apart are a connection for impurity, not for the sprinkling; the kettle\'s lid on a chain by the houses')
        return out('connected for impurity, not for the sprinkling — each part sprinkled (Shabbat 48b; Parah 12:9)', ['disqualified'])
    if ask == 'sprinkle_on_part':
        move('Kiddushin 25a:15', 'Rebbi: the sprinkling reaches any part of the body that can become impure')
        return out('on any part of the body that can become impure (Rebbi — Kiddushin 25a) — DISPUTE', [FX.NONE])
    if ask == 'gentile_no_tumah':
        dat('the row gentile_no_tumah: %s' % data['gentile_no_tumah']['value'])
        return out('the gentile has no corpse-impurity — no membership in the assembly (Nazir 61b)', ['exempt'])
    if ask == 'tevul_yom_hatat':
        move('Mishnah Parah 11:4-6', 'the Torah\'s immersers defile holies and terumah and may not enter; the scribes\' immersers no guilt for entering; all defile the hatat water and ashes')
        return out('the tevul yom by Torah law guilty for entering; by the scribes\' word not; both defile the hatat water (Parah 11:4-6)', ['disqualified'])
    if ask == 'invalid_water':
        move('Mishnah Parah 9:1-9; Gittin 86b:14', 'water or dew fallen in (R. Eliezer / the Sages); insects that burst, a beetle; the drinkers except the dove; the cow that drank; the kartzit harmless')
        return out('invalidated by water fallen in, bursting insects, a beast that drank; the kartzit harmless (Parah 9; Gittin 86b)', ['disqualified'])
    if ask == 'water_defiles':
        move('Mishnah Parah 8:2, 9:8-9, 11:2-3, 12:6-7', 'the sandal paradox; the two cleannesses; the terumah figs; the hyssop\'s and the hands\' chains to a hundred')
        return out('the hatat water defiles the terumah-clean by hands or body, the hatat-clean by hands (Parah 9:8; the chains 12:6-7)', ['disqualified'])
    if ask == 'water_transport':
        move('Mishnah Parah 9:6', 'not carried across a river by ship, floated or thrown; crossed with the water to the neck')
        return out('not carried across a river by ship (Parah 9:6)', ['disqualified'])
    if ask == 'vessel_for_water':
        move('Mishnah Parah 5:2-9', 'the vessel dried; a vessel required — not the walls, a jug\'s side, cupped hands; the trough in the rock no vessel; two troughs joined by a spout')
        return out('a vessel required for the filling, the mixing and the sprinkling; the trough in the rock is none (Parah 5:5-9)', ['disqualified'])
    if ask == 'all_trusted':
        ink('19:9', '"it shall be kept for the congregation" — R. Yehuda: all believed in guarding the water')
        move('Tosefta Chagigah 3:20; Mishnah Parah 5:1; Oholot 5:5', 'the am haaretz trusted for the hatat; the vessel\'s bringer; a vessel clean for purification protects with the tent\'s walls')
        return out('all are trusted for the heifer\'s water (Tosefta Chagigah 3:20; Parah 5:1)', ['accepted'])
    if ask == 'bet_peras':
        move('Mishnah Oholot 16:2-18:6', 'the mounds near a city; the graveyard\'s search; the plowed grave a hundred cubits; the three kinds; the purification by three handbreadths; the land of the gentiles')
        return out('a bet peras — the plowed grave\'s hundred cubits, the lost grave\'s field, the kokhin field: contact and carriage; purified by three handbreadths (Oholot 17-18)', ['corpse_unclean_seven_days'])
    if ask == 'gentile_dwellings':
        move('Mishnah Oholot 18:7-10', 'gentile dwellings unclean after forty days; the drains examined; ten places excepted')
        return out('gentile dwellings unclean after forty days; ten places excepted (Oholot 18:7-10)', ['corpse_unclean_seven_days'])
    if ask == 'grave_stones':
        move('Mishnah Oholot 2:4, 15:8-9; Chullin 72a:6', 'the covering and buttressing stones by contact and overshadowing (R. Akiva from "the open field"); the tomb\'s courtyard; the jar and the animal as covering stones')
        return out('the grave\'s covering and buttressing stones defile by contact and overshadowing, not carriage (Oholot 2:4)', ['corpse_unclean_seven_days'])
    if ask == 'limb':
        move('Mishnah Oholot 1:7-8, 3:3-4; Eduyot 6:2-3', 'a whole limb no minimum; 248 limbs; the teeth, hair and nails clean apart; human connections not connections; the limb from the living disputed')
        return out('a whole limb defiles at any size; 248 limbs; the teeth, hair and nails clean when severed (Oholot 1:7-8, 3:3)', ['corpse_unclean_seven_days'])
    if ask == 'bone_measure':
        dat('the row bone_measure: %s' % data['bone_measure']['value'])
        return out('a barley-grain of bone by contact and carriage; a quarter-kav or the majority by tent; deficient clean (Oholot 2:1-7)', [FX.NONE])
    if ask == 'death_moment':
        move('Mishnah Oholot 1:6', 'no corpse-defilement until death; cut up or dying he binds the levirate and feeds terumah; the convulsing beast unclean')
        return out('defiles from the death, not before — the dying binds and feeds still (Oholot 1:6)', [FX.NONE])
    if ask == 'dry_flesh':
        move('Niddah 55a:4', 'as a bone is dry, the corpse defiles even when dry (R. Yochanan from 19:16)')
        return out('the corpse defiles dry, as the bone (Niddah 55a)', ['corpse_unclean_seven_days'])
    if ask == 'birth_and_fetus':
        move('Mishnah Oholot 7:4-6', 'the woman in hard labor carried between houses; twins; the child cut up for her life, not after the greater part emerged')
        return out('the opened tomb; the mother\'s life before the fetus until the greater part emerges (Oholot 7:4-6)', [FX.NONE])
    if ask == 'ox_goad':
        move('Shabbat 17a:2; Mishnah Oholot 16:1-2', "R. Akiva's three measures: to the carrier at an ox-goad's thickness, to themselves at any, to others at a handbreadth")
        return out('movables convey to the carrier at an ox-goad\'s thickness, to themselves at any, to others at a handbreadth (Oholot 16:1)', ['corpse_unclean_seven_days'])
    if ask == 'window_measures':
        move('Mishnah Oholot 13:1-6', 'the light-hole by the drill; for use a square handbreadth; the reducers and the non-reducers: the clean reduces, the unclean does not')
        return out('the window\'s measures — the drill\'s hole for light, a square handbreadth for use; the clean reduces (Oholot 13)', [FX.NONE])
    if ask == 'madaf':
        dat('the row madaf: %s' % data['madaf']['value'])
        return out('madaf for the hatat — the unclean has it, the clean not (Parah 10:1)', [FX.NONE])
    if ask == 'mikveh_grades':
        move('Mishnah Mikvaot 1:1-8, 2:1-10', 'six degrees of waters — the pools, the unstopped flows, forty seahs, the small spring, the smitten waters, the living waters; the doubts; the three logs')
        return out('six degrees — the living waters the top: the zav, the leper and the hatat water (Mikvaot 1:8)', ['accepted'])
    if ask == 'camps':
        move('Mishnah Kelim 1:7-8', 'the corpse carried within the walled city but not brought back; the corpse-impure barred at the chel — naso\'s three camps by the paid CALL')
        return out('the corpse-impure barred at the chel; out of the Presence\'s camp alone (Kelim 1:8; Num 5:2)', ['sent_outside_the_camp'])
    if ask == 'torah_endures':
        move('Berakhot 63b:14; Gittin 57b:22; Shabbat 83b:10', 'Reish Lakish: "this is the Torah: when one dies in a tent" — Torah endures in one who kills himself over it (the homily\'s three seats)')
        return out('the homily — Torah endures in one who kills himself over it in its tent (Berakhot 63b)', [FX.NONE])
    return out('no verdict in span', [FX.NONE])
