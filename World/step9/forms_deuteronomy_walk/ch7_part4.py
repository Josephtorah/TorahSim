

# =====================================================================
# Motion 2 — THE TEST DATA: the answer sheet's rows (the docket's LAW rows and the cells' asks) — GENERATED FROM THE CELLS' OWN ASKS by ch7_cases_gen.py
# (1b's lesson: a mistyped expected string grades nothing), then frozen as literals under the honest-pairing guard.
# =====================================================================
CASES = [
    # F1 — the_seven_nations
    ('Deut 7:1; the Sifrei 50:4 — the_seven', lambda: the_seven_nations({'ask': 'the_seven'}, DATA), 'the seven (7:1) — the list counted by its own verse: seven where every Exodus list has six, the Girgashite the seventh (ER by CALL); the readback row EXPANDED'),
    ('Deut 7:2; Num 33:52-53 by CALL — the_ban', lambda: the_seven_nations({'ask': 'the_ban'}, DATA), "the ban (7:2) — 'you shall utterly devote them': the code's hole compiled — a DEBIT on Israel open to Joshua; the east's devotings runs before the spec; the dispossession's debit referenced (JO by CALL), not doubled"),
    ('shelf: Sotah 35b:10-13, 36a:1 — the_bans_condition', lambda: the_seven_nations({'ask': 'the_bans_condition'}, DATA), "the ban's condition (7:2) — the Canaanite outside the Land, or who repents, is not devoted (Sotah 35b-36a; 20:16-18 and 21:10 forward): EXEMPT from the ban's debit"),
    ('Deut 7:2; Exod 23:32 by CALL — no_covenant', lambda: the_seven_nations({'ask': 'no_covenant'}, DATA), "no covenant (7:2) — 23:32's clause verbatim in kind (OR and ER by CALL): covenant_barred written here for the first time on the tape, the border block standing from the Moab giving"),
    ('Deut 7:2; Avodah Zarah 20a:1-4 — no_favor', lambda: the_seven_nations({'ask': 'no_favor'}, DATA), "no favor (7:2) — the code's hole compiled: no land, no praise, no gift (Avodah Zarah 20a; Mishnah 1:8): the renter of a house to a gentile in the Land barred — favor_barred on Israel"),
    ('shelf: Avodah Zarah 20a:10-11 — praise_of_the_creator', lambda: the_seven_nations({'ask': 'praise_of_the_creator'}, DATA), 'the praise of the Creator (7:2) — thanks to God for his creatures is not favor to the creature (Avodah Zarah 20a:11): the praiser who thanks the Creator EXEMPT'),
    ('Deut 7:3; Kiddushin 68b:2 — no_marriage', lambda: the_seven_nations({'ask': 'no_marriage'}, DATA), "no marriage (7:3) — both directions barred where 34:16 barred one (ER by CALL); the betrothal with a gentile woman ineffective (Kiddushin 68b): the gentile woman's betrothed holds no betrothal — intermarriage_barred on Israel"),
    ('Deut 7:3-4; Kiddushin 68b:3 — the_child_follows_the_mother', lambda: the_seven_nations({'ask': 'the_child_follows_the_mother'}, DATA), "the child follows the mother (7:3-4) — the gentile woman's son is hers, not yours (Kiddushin 68b; Yevamot 23a; Mishnah Kiddushin 3:12; ER by CALL): the gentile mother's son not his father's"),
    ('Deut 7:5; Exod 34:13 by CALL — the_four_objects', lambda: the_seven_nations({'ask': 'the_four_objects'}, DATA), "the four objects (7:5) — four verbs where 34:13 had three, the images burned (ER and JO by CALL); the demolition a reference row against the dispossession's open debit; the shelf's order: fell, conquer, eradicate"),
    ('shelf: Mishnah Avodah Zarah 3:8 — the_asherah_shade', lambda: the_seven_nations({'ask': 'the_asherah_shade'}, DATA), "the Asherah's shade (7:5) — not sat in, even the shade of its shade (Mishnah 3:8; Avodah Zarah 48b): the sitter in the Asherah's shade barred"),
    ('shelf: Avodah Zarah 48b:7-10 — no_other_way', lambda: the_seven_nations({'ask': 'no_other_way'}, DATA), 'no other way (7:5) — one with no other way may pass beneath the Asherah ab initio (Avodah Zarah 48b:8): EXEMPT; an important person runs'),
    ('shelf: Makkot 22a:2-3 — the_asherah_wood', lambda: the_seven_nations({'ask': 'the_asherah_wood'}, DATA), "the Asherah's wood (7:5, 7:26) — used, its user is FLOGGED (Makkot 22a; Pesachim 48a): the wood-burner lashed; the redemption R. Eliezer's (Avodah Zarah 49b)"),
    ('the write — the_write', lambda: the_seven_nations({'ask': 'the_write'}, DATA), "the write (7:1-5) — the ban's debit open to the run and the three border blocks on Israel at the chapter's first line"),
    # F2 — the_holy_people
    ('Deut 7:6; Exod 19:5-6 by CALL — holy_people', lambda: the_holy_people({'ask': 'holy_people'}, DATA), "a holy people (7:6) — 19:5-6's treasure and holy nation read back with 14:2 the pair; treasured_people stands (ES by CALL); the readback row EXPANDED"),
    ('Deut 7:6-7; Deut 4:37 by CALL — chose_you', lambda: the_holy_people({'ask': 'chose_you'}, DATA), "chose you (7:6-7) — the choice of the people after 4:37's choice of the fathers' seed (OH by CALL); 'set his love' the captive's and Shechem's word"),
    ('Deut 7:7; Chullin 89a — the_fewest', lambda: the_holy_people({'ask': 'the_fewest'}, DATA), "the fewest (7:7) — 'not because you were more': the humblest, on the shelf (Chullin 89a); Onkelos 'the smallest': a DATA row, no write"),
    ('Deut 7:8; Gen 22:16, 26:3, 50:24 by CALL — the_oath', lambda: the_holy_people({'ask': 'the_oath'}, DATA), 'the oath (7:8) — the noun starred by the parser, the swearing no number; the three lines on the tape (MA and JS by CALL); the pointers at 7:8, 7:12, 7:13'),
    ('Deut 7:8; Exod 12:51 — brought_out_redeemed', lambda: the_holy_people({'ask': 'brought_out_redeemed'}, DATA), "brought out and redeemed (7:8) — the going out read back with the oath's reason (ES by CALL; the tape's brought_out found): the readback row EXPANDED; no write"),
    # F3 — the_faithful_god
    ('Deut 7:9; Deut 4:35, 39 by CALL — he_is_god', lambda: the_faithful_god({'ask': 'he_is_god'}, DATA), "he is God (7:9) — the creed's third seat after 4:35 and 4:39 (OH by CALL); 'know therefore' the chapter's imperative-less charge"),
    ('Deut 7:9; Shabbat 10b — the_faithful', lambda: the_faithful_god({'ask': 'the_faithful'}, DATA), "the faithful God (7:9) — the phrase's one seat; on the shelf a translation, sayable in the bathroom (Shabbat 10b): a DATA note"),
    ('Deut 7:9; Deut 5:10 by CALL — thousand_generations', lambda: the_faithful_god({'ask': 'thousand_generations'}, DATA), "a thousand generations (7:9) — the second word's clause numbered [1000] for the bare plural (CH by CALL): the readback row VARIANT; fear's thousand against love's thousands (Sotah 31a)"),
    ('Deut 7:10; Deut 5:9 by CALL — the_hater_repaid', lambda: the_faithful_god({'ask': 'the_hater_repaid'}, DATA), "the hater repaid (7:10) — the visiting's recipient turned to the hater's own face (CH by CALL): the readback row TURNED; Onkelos's supplied doctrine a DATA row"),
    ('Deut 7:11; Deut 6:1 by CALL — the_triad', lambda: the_faithful_god({'ask': 'the_triad'}, DATA), 'the triad (7:11) — the commandment, the statutes and the judgments: the third seat after 5:31 and 6:1 (HI by CALL): the readback row VERBATIM in kind; today to do, tomorrow to receive'),
    ('Deut 7:9 (the store) — the_written_read_pair', lambda: the_faithful_god({'ask': 'the_written_read_pair'}, DATA), "the written/read pair (7:9) — 'his commandments' written without the yod and read with it, the store's extra token kept out of every check; 5:10's kin: a DATA row"),
    # F4 — because_you_hear
    ('Deut 7:12; Onkelos — the_heel', lambda: because_you_hear({'ask': 'the_heel'}, DATA), "because (7:12) — the heel as a conjunction, 'in consequence of' at five seats; Onkelos 'in exchange for': the portion's name; a DATA row"),
    ('Deut 7:12; Exod 19:5 — covenant_kept', lambda: because_you_hear({'ask': 'covenant_kept'}, DATA), "the covenant kept (7:12) — 19:5's condition read back as 'because you hear', the covenant kept by God: the readback row VARIANT; blessings_for_hearing a conditional heaven entry on Israel"),
    ('Deut 7:13; Exod 23:25 by CALL — the_blessing_list', lambda: because_you_hear({'ask': 'the_blessing_list'}, DATA), "the blessing's list (7:13) — 23:25's bread and water expanded to womb, ground, grain, wine, oil, cattle and flock (OR by CALL): the readback row 7:13-15 EXPANDED; the flock's 'young' tagged a name in the DB"),
    ('Deut 7:14; Exod 23:26 by CALL — no_barren', lambda: because_you_hear({'ask': 'no_barren'}, DATA), "no barren (7:14) — 23:26's clause verbatim in kind with the cattle added (OR by CALL): the readback row VERBATIM"),
    ('Deut 7:15; Exod 15:26 by CALL — the_diseases', lambda: because_you_hear({'ask': 'the_diseases'}, DATA), "the diseases (7:15) — 15:26's healer's promise turned: the diseases of Egypt laid on those who hate you (ES by CALL; the tape's healer_promised found): the readback row TURNED"),
    ('Deut 7:16; Bava Kamma 113b — consume_no_pity', lambda: because_you_hear({'ask': 'consume_no_pity'}, DATA), "consume without pity (7:16) — the code's hole compiled on the ink alone (no row on the shelf); 'consume' the war's spoil only — the robber of a gentile barred (Bava Kamma 113b): pity_barred on Israel"),
    ('Deut 7:16; Exod 23:33 by CALL — no_serving_snare', lambda: because_you_hear({'ask': 'no_serving_snare'}, DATA), "no serving, a snare (7:16) — 23:33's snare restated (OR by CALL); the second word's block stands (CH by CALL), no second write: the readback row VARIANT"),
    ('the write — the_write', lambda: because_you_hear({'ask': 'the_write'}, DATA), "the write (7:12-16) — the blessings' conditional entry and the pity's block on Israel at the chapter's second line"),
    # F5 — do_not_fear
    ('Deut 7:17; Deut 1:28 by CALL — the_doubt', lambda: do_not_fear({'ask': 'the_doubt'}, DATA), "the doubt (7:17) — the spies' fear voiced again ('more than I; how can I') against 1:28 and 4:38 (OS and OH by CALL); no write"),
    ('Deut 7:18-19; Exod 7:20-12:29 — remember_pharaoh', lambda: do_not_fear({'ask': 'remember_pharaoh'}, DATA), "remember Pharaoh (7:18-19) — the plagues, the sea, the signs and the wonders in one clause (ES by CALL; the tape's ten lines found): the readback row SHORTENED; the fear rule owed to the war chapter"),
    ('Deut 7:19; Deut 4:34 by CALL — the_trials', lambda: do_not_fear({'ask': 'the_trials'}, DATA), "the great trials (7:19) — 4:34's list read back (ES and OH by CALL); Onkelos 'the miracles'; 16:10's measure the homograph"),
    ('Deut 7:20; Exod 23:28 by CALL — the_hornet', lambda: do_not_fear({'ask': 'the_hornet'}, DATA), "the hornet (7:20) — 23:28's promise with the hiders added (OR by CALL): the readback row EXPANDED; the hornet at the Jordan's bank on the shelf (Sotah 36a)"),
    ('Deut 7:21; Deut 6:15 by CALL — in_your_midst', lambda: do_not_fear({'ask': 'in_your_midst'}, DATA), "in your midst (7:21) — 6:15's pair, Onkelos the Shekhinah at both (HI by CALL); 'a great and awesome God' 10:17's four"),
    ('Deut 7:22; Exod 23:29-30 by CALL — little_by_little', lambda: do_not_fear({'ask': 'little_by_little'}, DATA), "little by little (7:22) — 23:29-30's clause verbatim in kind, the beasts' reason kept (OR by CALL): the readback row VERBATIM; the pointer at 7:22"),
    ('Deut 7:23-24; Exod 23:27, 31 by CALL — the_kings_and_the_name', lambda: do_not_fear({'ask': 'the_kings_and_the_name'}, DATA), "the kings and the name (7:23-24) — 23:27 and 23:31 expanded with the kings, the name from under heaven (Amalek's phrase) and Joshua 1:5's receipt (OR and ES by CALL): the readback row EXPANDED"),
    # F6 — the_images_and_the_devoted
    ('Deut 7:25; Mishnah Avodah Zarah 4:4 — burn_the_images', lambda: the_images_and_the_devoted({'ask': 'burn_the_images'}, DATA), "the images burned (7:25) — 'the graven images of their gods': a gentile's idol forbidden from its making (Avodah Zarah 52a; Mishnah 4:4 — ER by CALL); 7:5's clause said again with 12:3 forward"),
    ('shelf: Avodah Zarah 52a:9-10 — the_gentile_revokes', lambda: the_images_and_the_devoted({'ask': 'the_gentile_revokes'}, DATA), "the gentile revokes his idol (7:25) — 'the graven images of their gods' read 'the revoked of' (Avodah Zarah 52a; Mishnah 4:4-5): the gentile who cut its ear's tip holds; the Joshua-war idols stay forbidden"),
    ('shelf: Avodah Zarah 42a:12 — the_jew_bent_it', lambda: the_images_and_the_devoted({'ask': 'the_jew_bent_it'}, DATA), "the Jew who bent the idol (7:25) — not revoked, by Rava's decree lest he acquire it (Avodah Zarah 42a:12); a Jew's idol interred (52a:12): the rule holds against him"),
    ('Deut 7:25; Deut 5:21 by CALL — not_covet_silver_gold', lambda: the_images_and_the_devoted({'ask': 'not_covet_silver_gold'}, DATA), "you shall not covet (7:25) — the tenth word's verb turned to the idols' silver and gold (CH by CALL; coveting_barred stands): the readback row TURNED; the decorative item the shelf's rule (Avodah Zarah 51b)"),
    ('shelf: Mishnah Avodah Zarah 4:2 — the_money_at_the_head', lambda: the_images_and_the_devoted({'ask': 'the_money_at_the_head'}, DATA), "the money at the idol's head (7:25) — permitted, not an ornament (Mishnah Avodah Zarah 4:2; 51b:13-14): the finder EXEMPT from the coveting's bar"),
    ('Deut 7:25; Exod 23:33 by CALL — lest_snared', lambda: the_images_and_the_devoted({'ask': 'lest_snared'}, DATA), "lest snared (7:25) — 23:33's snare (OR by CALL); 'lest' a prohibition on the shelf (Avodah Zarah 51b:3): a DATA note"),
    ('Deut 7:25; Deut 27:15 — abomination_to_the_lord', lambda: the_images_and_the_devoted({'ask': 'abomination_to_the_lord'}, DATA), "an abomination to the LORD (7:25) — the book's phrase at its first seat; the idol an abomination from its making (Avodah Zarah 52a): a DATA row"),
    ('Deut 7:26; Mishnah Avodah Zarah 1:9 — into_your_house', lambda: the_images_and_the_devoted({'ask': 'into_your_house'}, DATA), "the abomination into the house (7:26) — the code's hole compiled: the renter for a residence barred, the wall withdrawn, a house bowed to forbidden (Mishnah 1:9, 3:6; Avodah Zarah 47b): house_abomination_barred on Israel"),
    ('Deut 7:26; Avodah Zarah 54b — devoted_like_it', lambda: the_images_and_the_devoted({'ask': 'devoted_like_it'}, DATA), "devoted like it (7:26) — whatever you generate from the idol is like it: the exchange forbidden, the exchange's exchange disputed (Avodah Zarah 54b; Kiddushin 58a): the idol's exchanger holds nothing; the two lemmas a DATA row"),
    ('Deut 7:26; Lev 11:43 by CALL — utterly_detest', lambda: the_images_and_the_devoted({'ask': 'utterly_detest'}, DATA), "utterly detest (7:26) — Leviticus 11:43's verb on the idol: the impurity of the idol's stones as a creeping animal's (Avodah Zarah 47b; SH by CALL); the Sifrei 61:7's renaming"),
    ('Deut 7:1-26 — the_readback_table', lambda: the_images_and_the_devoted({'ask': 'the_readback_table'}, DATA), "the readback table — twenty-one rows graded (VERBATIM 4, VARIANT 5, EXPANDED 8, TURNED 3, SHORTENED 1); six on the tape, fifteen in the kin's cells by CALL; four holes compiled; no row open"),
    ('the write — the_write', lambda: the_images_and_the_devoted({'ask': 'the_write'}, DATA), "the write (7:25-26) — the abomination's block on Israel at the chapter's third line; the coveting's block stands unmoved"),
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
    print('THE INK: the two number verses %s (the oath\'s noun starred at 7:8); no frame %s, no saying, no imperative %s; the case tokens %s; the register singular-only %s, plural-only %s, both %s, neither %s; the infinitive absolutes %s; the prohibitions second person %d, third %d; the first person %s' % (sorted(PARSED.items()), DIV, IMPER, dict(collections.Counter(x for l in CASE_TOK.values() for x in l)), SG_ONLY, PL_ONLY, BOTH, NEITHER, {v: [x for x, _ in l] for v, l in INFA.items()}, sum(1 for v in PRO for _, m in PRO[v] if 'i2' in m), sum(1 for v in PRO for _, m in PRO[v] if 'i3' in m), {v: [x for x, _ in l] for v, l in ONE_CS.items()}))
    print('THE READBACK ON THE KIN: %d rows — %s; on the tape %d, in the kin\'s cells by CALL %d (every cell found %s); no row open %s; the holes %d: %s' % (len(READBACK), dict(RB_GRADES), sum(1 for r in READBACK if r['tape_kind']), sum(1 for r in READBACK if r['cell']), all(r['cell_found'] for r in READBACK if r['cell']), not any(r['open'] for r in READBACK), len(HOLES), [h['hole'].split(' — ')[0] for h in HOLES]))
    print('THE DELTAS (computed): %s' % (DELTA,))
    print('THE SEVEN-NAME LISTS %s; the six-name lists %d; the Girgashite %s' % (SEVEN_LISTS, len(SIX_LISTS), LEMV('1622')))
    print('THE CALLEES: no_covenant %s / not_dwell %s / hornet %s / little %s; the orders %s, the daughters %s, the child %s, the demolition %s; drive_out %s; the visiting %s, the coveting %s; the plagues %s, the treasure %s, the healer %s, the blotting %s; loved %s, shown %s; the triad %s; the murmuring %s; the oath lines %s / %s / %s; the Shittim spec %s; the classifier %s' % (OR_NOCOV['v'], OR_DWELL['v'], OR_HORNET['v'], OR_LITTLE['v'], ER_ORD['v'], ER_DAU['v'], ER_CHILD['v'], ER_GROW['v'], JO_DRIVE[1], CH_VIS[1], CH_COV[1], ES_TEN['v'], ES_TREAS['v'], ES_HEAL['v'], ES_BLOT['v'], OH_LOVED[1], OH_SHOWN[1], HI_TRIAD[1], OS_MURM[1], MA_TEST['v'], MA_FAM['v'], JS_KT['v'], BK_SPEC[1], SH_SWARM[0]))
    print('THE SCENE on the bench: %s; the exempt arms %s; the lashes %s; the timers (set, fired, cancelled, pending) %s; entities %d; closes %d' % (SCENE[0], SCENE[1], SCENE[2], SCENE[3], SCENE[4], SCENE[5]))
    print('THE NARRATIVE: %s' % (NARRATIVE,))
    print('THE PARAMETER ROWS: ' + '; '.join('%s = %s' % (k, DATA[k]['value'] if k != 'the_readback' else '%d rows, %d holes' % (len(DATA[k]['value']), len(DATA[k]['holes']))) for k in DATA) + ' (the other settings recorded in DATA)')
    if ok == len(CASES):
        print('\nTHE COMPILE OF CHAPTER 7: the answer sheet REPRODUCED — %d/%d' % (ok, len(CASES)))
    sys.exit(0 if ok == len(CASES) else 1)
