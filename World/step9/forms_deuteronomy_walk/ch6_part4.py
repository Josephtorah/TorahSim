

# =====================================================================
# Motion 2 — THE TEST DATA: the answer sheet's rows (the docket's LAW rows and the cells' asks) — GENERATED FROM THE CELLS' OWN ASKS by ch6_cases_gen.py
# (1b's lesson: a mistyped expected string grades nothing), then frozen as literals under the honest-pairing guard.
# =====================================================================
CASES = [
    # F1 — the_header
    ('Deut 6:1 — the_triad', lambda: the_header({'ask': 'the_triad'}, DATA), "the triad (6:1) — the commandment, the statutes and the judgments: 5:31's charge opened here, 7:11 forward; the header's stamp, no write"),
    ('Deut 6:1 — the_charge_executed', lambda: the_header({'ask': 'the_charge_executed'}, DATA), "the charge executed (6:1) — 'to teach you' runs 5:31's 'which you shall teach them': a REFERENCE row against stand_here_commanded, its debit closed by the prior run (Deut 1:5); NO write"),
    ('Deut 6:3 — hear_and_observe', lambda: the_header({'ask': 'hear_and_observe'}, DATA), "hear and observe (6:3) — the frame's charge: no write; 'that it may be well with you' the book's refrain (seven seats)"),
    ('Deut 6:3 — the_land_flowing', lambda: the_header({'ask': 'the_land_flowing'}, DATA), "the land flowing (6:3) — the book's first 'milk and honey' (eleven Torah seats); the oath's promise the covenant's, its lines on the tape"),
    ('Deut 6:2 — your_sons_son', lambda: the_header({'ask': 'your_sons_son'}, DATA), "your son's son (6:2) — three generations in the fear; Exodus 10:2's kin: a DATA note, no write"),
    # F2 — the_creed
    ('Deut 6:4; Pesachim 56a — hear_o_israel', lambda: the_creed({'ask': 'hear_o_israel'}, DATA), "hear, O Israel (6:4) — the creed's call: Jacob's sons' answer the first saying (Pesachim 56a); the four seats all this book's"),
    ('Deut 6:4 — the_lord_is_one', lambda: the_creed({'ask': 'the_lord_is_one'}, DATA), "the LORD is one (6:4) — the two seats of the pair (6:4, Zechariah 14:9); the numeral the parser's [1]; the large letters a parked hypothesis"),
    ('Deut 6:5; Mishnah Berakhot 9:5 — with_all_your_heart', lambda: the_creed({'ask': 'with_all_your_heart'}, DATA), "with all your heart (6:5) — the two inclinations (Mishnah Berakhot 9:5; the Sifrei 32:2-4); 4:29's kin (OH by CALL)"),
    ('Deut 6:5; Berakhot 61b — with_all_your_soul', lambda: the_creed({'ask': 'with_all_your_soul'}, DATA), "with all your soul (6:5) — even if he takes your soul: the martyr's clause (R. Akiva, Berakhot 61b; Sanhedrin 74a)"),
    ('Deut 6:5; the Sifrei 32:7 — with_all_your_might', lambda: the_creed({'ask': 'with_all_your_might'}, DATA), "with all your might (6:5) — the Bible's one seat of the word: money, measure and thanks (9:5; the Sifrei 32:7); Onkelos 'your property'"),
    ('Deut 6:5; Sotah 31a — love_and_fear', lambda: the_creed({'ask': 'love_and_fear'}, DATA), "love and fear (6:5) — 'you shall love' the creed's command after its call; the one who acts from love greater (Sotah 31a; the Sifrei 32:1)"),
    # F3 — the_four_duties
    ('Deut 6:7; Mishnah Berakhot 1:1-2 — recite_when', lambda: the_four_duties({'ask': 'recite_when'}, DATA), "when to recite (6:7) — the evening from the priests' entering, the morning from blue against white: the times' table (Mishnah Berakhot 1:1-2; Berakhot 2a-2b) — the priest entering to eat his terumah begins it"),
    ('Deut 6:7; Mishnah Berakhot 1:3 — recite_how', lambda: the_four_duties({'ask': 'recite_how'}, DATA), 'how to recite (6:7) — in his way (Hillel: the times, not the postures; R. Tarfon rebuked, Mishnah Berakhot 1:3): the reader by the road holds'),
    ('shelf: Mishnah Berakhot 2:5 — recite_who', lambda: the_four_duties({'ask': 'recite_who'}, DATA), "who recites (6:7) — the bridegroom EXEMPT the first night (Mishnah Berakhot 2:5; Berakhot 16a); the mourner, women, slaves and minors the table's other rows"),
    ('shelf: Kiddushin 29b — daughters_exempt', lambda: the_four_duties({'ask': 'daughters_exempt'}, DATA), "the daughters (6:7) — 'your sons', not your daughters: the daughter EXEMPT from the teaching (Kiddushin 29b, 34a)"),
    ('Deut 6:6; Mishnah Berakhot 2:2 — the_passages', lambda: the_four_duties({'ask': 'the_passages'}, DATA), 'the passages (6:6) — three recited in order (Mishnah Berakhot 2:2), four bound (Menachot 3:7); two sets with two members each way, the ten words in neither (the Sifrei 34:2-3)'),
    ('Deut 6:7; Kiddushin 29a-30b — teach_your_sons', lambda: the_four_duties({'ask': 'teach_your_sons'}, DATA), "teach your sons (6:7) — the father's duty to teach Torah, the disciples 'sons' (the Sifrei 34:1; Kiddushin 29a-30b); sharp in the mouth (30a)"),
    ('Deut 6:8; Mishnah Menachot 3:7 — tefillin_passages', lambda: the_four_duties({'ask': 'tefillin_passages'}, DATA), "the tefillin's passages (6:8) — the four that say 'a sign upon your hand' (Menachot 3:7: each invalidates the others)"),
    ('Deut 6:8; the Sifrei 35:3-4 — tefillin_compartments', lambda: the_four_duties({'ask': 'tefillin_compartments'}, DATA), 'the compartments (6:8) — the hand one, the head FOUR: a PARAMETER (the Sifrei 35:3-4; Menachot 34b-35a; Sanhedrin 4b), its derivation from the spellings the open row (11:18 plene in the ink)'),
    ('Deut 6:8; Menachot 36b-37a — tefillin_arm', lambda: the_four_duties({'ask': 'tefillin_arm'}, DATA), "the arm (6:8) — the left, the weak hand (Menachot 36b-37a; the Sifrei 35:5-10); the left-handed on his right, the amputee's arm the table's row"),
    ('Deut 6:8; Menachot 36a — tefillin_order', lambda: the_four_duties({'ask': 'tefillin_order'}, DATA), 'the order (6:8) — the hand bound first, the head removed first (Menachot 36a; the Sifrei 35:11)'),
    ('Deut 6:8; Menachot 37a-b — tefillin_head', lambda: the_four_duties({'ask': 'tefillin_head'}, DATA), "the head (6:8) — the hairline, not between the eyes: the place of hair by 14:1's analogy (Menachot 37a-b; the Sifrei 35:12)"),
    ('Deut 6:9; Menachot 34a — mezuzah_writing', lambda: the_four_duties({'ask': 'mezuzah_writing'}, DATA), "the mezuzah's writing (6:9) — a scroll in ink with perfect letters, not the stones (Menachot 34a; Shabbat 103b; the Sifrei 36:1-2): the scroll-writer holds"),
    ('Deut 6:9; Menachot 33a-34a — mezuzah_doorpost', lambda: the_four_duties({'ask': 'mezuzah_doorpost'}, DATA), 'the doorpost (6:9) — one post, the right as one enters, the upper third (Menachot 33a-34a; the Sifrei 36:3-5)'),
    ('shelf: Yoma 11a — mezuzah_gates', lambda: the_four_duties({'ask': 'mezuzah_gates'}, DATA), "the gates (6:9) — the dwelling's, not the bathhouse's (Yoma 11a; the Sifrei 36:6-8): the bathhouse owner EXEMPT"),
    ('Deut 6:8-9; Menachot 43b — the_seven', lambda: the_four_duties({'ask': 'the_seven'}, DATA), 'the seven (6:8-9) — the head, the arm, four fringes, the mezuzah surround a man (Menachot 43b; the Sifrei 36:9): a DATA row'),
    ('the write — the_write', lambda: the_four_duties({'ask': 'the_write'}, DATA), "the write (6:4-9) — shema_commanded on Israel: the four duties standing from the chapter's own line"),
    # F4 — the_gift_and_the_warning
    ('Deut 6:10-11 — the_list', lambda: the_gift_and_the_warning({'ask': 'the_list'}, DATA), "the list (6:10-11) — cities, houses, cisterns, vineyards and olives 'which you did not …': a DATA row; the spoil permitted by 6:11 (the Sifrei 201:3) owed to the war chapter"),
    ('Deut 6:12 — lest_you_forget', lambda: the_gift_and_the_warning({'ask': 'lest_you_forget'}, DATA), "lest you forget (6:12) — obey_horeb's forgetting census (thirteen seats, 6:12 among them); the prohibition's seat 4:9 (OH by CALL)"),
    ('Deut 6:13; Temurah 3b-4a — fear_serve_swear', lambda: the_gift_and_the_warning({'ask': 'fear_serve_swear'}, DATA), "fear, serve, swear (6:13) — the true oath a positive clause (Temurah 3b-4a), its prohibition the third word's (DC by CALL); the true swearer holds"),
    ('Deut 6:14 — no_other_gods', lambda: the_gift_and_the_warning({'ask': 'no_other_gods'}, DATA), "no other gods (6:14) — the second word's clause: other_gods_barred stands from the giving (CH by CALL), no second write; the idolaters' companion the Tosefta's row"),
    ('Deut 6:15 — the_jealous_god', lambda: the_gift_and_the_warning({'ask': 'the_jealous_god'}, DATA), "the jealous God (6:15) — 4:24 and 5:9's word at its third Deuteronomy seat; the visiting's arms the second word's (CH by CALL); Onkelos the Shekhinah"),
    # F5 — the_test_and_the_right
    ('Deut 6:16; Arakhin 15a — you_shall_not_test', lambda: the_test_and_the_right({'ask': 'you_shall_not_test'}, DATA), "you shall not test (6:16) — Massah the tape's named line (Exodus 17:7), a run citation by name; the ten trials (Arakhin 15a; ES by CALL): the block test_barred on Israel"),
    ('Deut 6:17 — surely_keep', lambda: the_test_and_the_right({'ask': 'surely_keep'}, DATA), "surely keep (6:17) — the infinitive absolute (the book's three); the testimonies' three seats with 4:45's header (OH by CALL): no write"),
    ('Deut 6:18; Bava Metzia 108a — the_right_and_the_good', lambda: the_test_and_the_right({'ask': 'the_right_and_the_good'}, DATA), "the right and the good (6:18) — the abutter's rule (Bava Metzia 108a): the buyer of the adjoining field yields to the neighbor"),
    ('Deut 6:19 — thrust_out_enemies', lambda: the_test_and_the_right({'ask': 'thrust_out_enemies'}, DATA), "thrust out (6:19) — the enemies thrust out 'as the LORD has spoken': 9:4 forward, the manslayer's verb: a DATA note"),
    ('the write — the_write', lambda: the_test_and_the_right({'ask': 'the_write'}, DATA), "the write (6:16-19) — test_barred on Israel: the block at the chapter's second line"),
    # F6 — the_sons_question
    ('Deut 6:20; Pesachim 116a-b — the_four_askings', lambda: the_sons_question({'ask': 'the_four_askings'}, DATA), "the four askings (6:20) — the wise son's question, verbatim with Exodus 13:14 to 'saying' (the four sons, Pesachim 116a-b; PE by CALL)"),
    ('Deut 6:21-24 — the_answer_rows', lambda: the_sons_question({'ask': 'the_answer_rows'}, DATA), "the answer's rows (6:21-24) — the exodus retold in the first person plural: EXPANDED, SHORTENED, EXPANDED, EXPANDED against the tape's lines (T1); no second act"),
    ('Deut 6:25 — the_receipt', lambda: the_sons_question({'ask': 'the_receipt'}, DATA), "the receipt (6:25) — 'as he commanded us' without the Name: a run citation of the charge (5:31), VERBATIM in kind; the gate's finder blind, the pointer on file"),
    ('Deut 6:25 — righteousness_for_us', lambda: the_sons_question({'ask': 'righteousness_for_us'}, DATA), "righteousness for us (6:25) — Genesis 15:6's word at the answer's close; 24:13's pledge the kin; Onkelos 'merit': a DATA note"),
    ('Deut 6:1-25 — the_readback_table', lambda: the_sons_question({'ask': 'the_readback_table'}, DATA), 'the readback table — seven rows graded (VERBATIM 3, EXPANDED 3, SHORTENED 1); every row inside a law (T1); no row open'),
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
    print('THE INK: the one number verse %s; no frame %s; the case tokens %s; the register singular-only %s, plural-only %s, both %s, the answer\'s first person plural %s; the imperatives %s; the infinitive absolute %s; the two plural prohibitions %s' % (sorted(PARSED.items()), DIV, dict(collections.Counter(x for l in CASE_TOK.values() for x in l)), SG_ONLY, PL_ONLY, BOTH, sorted(ONE_CP), IMPER, INFA, PROHIB))
    print('THE READBACK\'S THIRD FORM: %d rows — %s; every row inside a law %s; the deltas: the header %s; Massah %s; the going out %s; the plagues %s; the oath %s; the charge %s' % (len(READBACK), dict(RB_GRADES), all(r['law'] for r in READBACK), HEADER_DELTA, MASSAH_DELTA, OUT_DELTA, PLAGUE_DELTA, OATH_DELTA, CHARGE_DELTA))
    print('THE SPELLINGS (the open row): %s; the sign\'s four seats %s' % (FRONT, SIGN))
    print('THE RECEIPT WITHOUT THE NAME: %s (the finder blind — CO6)' % (RECEIPT_NO_NAME,))
    print('THE CALLEES: the trials %s / %s; the forgetting %d seats; the vain oath %s; the firstborn %s; the oath lines %s / %s / %s; the charge %s' % (ES_TEN['v'], ES_SIX['v'], len(OH.FORGET), DC_VO[:2], PE_HUMAN[0][:20], MA_TEST['v'], MA_FAM['v'], JS_KT['v'], ER_TORAH['v']))
    print('THE SCENE on the bench: %s; the exempt arms %s; the timers (set, fired, cancelled, pending) %s; entities %d; closes %d' % (SCENE[0], SCENE[1], SCENE[2], SCENE[3], SCENE[4]))
    print('THE NARRATIVE: %s' % (NARRATIVE,))
    print('THE PARAMETER ROWS: ' + '; '.join('%s = %s' % (k, DATA[k]['value'] if k != 'the_readback' else '%d rows' % len(DATA[k]['value'])) for k in DATA) + ' (the other settings recorded in DATA)')
    if ok == len(CASES):
        print('\nTHE COMPILE OF CHAPTER 6: the answer sheet REPRODUCED — %d/%d' % (ok, len(CASES)))
    sys.exit(0 if ok == len(CASES) else 1)
