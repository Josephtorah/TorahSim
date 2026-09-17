

# =====================================================================
# Motion 2 — THE TEST DATA: the answer sheet's rows (the docket's LAW rows and the cells' asks) — GENERATED FROM THE CELLS' OWN ASKS by ch5_cases_gen.py
# (1b's lesson: a mistyped expected string grades nothing), then frozen as literals under the honest-pairing guard.
# =====================================================================
CASES = [
    # F1 — the_assembly_called
    ('Deut 5:1 — hear_learn_keep_do', lambda: the_assembly_called({'ask': 'hear_learn_keep_do'}, DATA), "hear, learn, keep, do (5:1) — the second speech opened: Moses' call to all Israel, the four verbs in order; the frame's second seat, no write"),
    ('Deut 5:2 — the_covenant_at_horeb', lambda: the_assembly_called({'ask': 'the_covenant_at_horeb'}, DATA), "the covenant at Horeb (5:2) — the tape's covenant READ BACK: the book and the blood (ER by CALL); forty-eight covenants per mitzva (Sotah 37b); the second copy a third saying (R. Akiva)"),
    ('Deut 5:3 — not_with_our_fathers', lambda: the_assembly_called({'ask': 'not_with_our_fathers'}, DATA), 'not with our fathers (5:3) — the covenant with the living here: a DATA note against 29:13-14, no link of our own'),
    ('Deut 5:4 — face_in_face', lambda: the_assembly_called({'ask': 'face_in_face'}, DATA), "face in face (5:4) — the one seat of the form; Onkelos 'speech with speech' (ER by CALL); all Israel heard the voice (Yoma 4b)"),
    ('Deut 5:5 — i_stood_between', lambda: the_assembly_called({'ask': 'i_stood_between'}, DATA), "I stood between (5:5) — the mediator: the first two words direct, the rest through Moses (Makkot 24a); the request's row"),
    # F2 — the_second_word
    ('Deut 5:7 — no_other_gods', lambda: the_second_word({'ask': 'no_other_gods'}, DATA), "no other gods before me (5:7) — the second word's head, compiled here: the block other_gods_barred on Israel at the giving's line"),
    ('Deut 5:8 — no_image', lambda: the_second_word({'ask': 'no_image'}, DATA), 'no image (5:8) — the making barred; the no-image list of 4:16-19 the parameter table (OH by CALL); the images for study credited'),
    ('Deut 5:9; Mishnah Sanhedrin 7:6 — bow_and_serve', lambda: the_second_word({'ask': 'bow_and_serve'}, DATA), "bow and serve (5:9) — the bower stoned: the second word's answer sheet (Mishnah Sanhedrin 7:6; the four services, Sanhedrin 60b); the mode by 17:5's juxtaposition"),
    ('shelf: Sanhedrin 60b:3 — in_its_way', lambda: the_second_word({'ask': 'in_its_way'}, DATA), "in its way (5:9) — Peor's exposure, Markulis's stone: liable, the idol's own service (Mishnah Sanhedrin 7:6)"),
    ('shelf: Sanhedrin 60b:2 — the_embracer', lambda: the_second_word({'ask': 'the_embracer'}, DATA), 'the embracer (5:9) — a prohibition without death: the hugger, the kisser, the dresser exempt from the sanction (Mishnah Sanhedrin 7:6)'),
    ('Deut 5:9-10 — the_visiting', lambda: the_second_word({'ask': 'the_visiting'}, DATA), "the visiting (5:9-10) — the generations and the thousands a DATA row: when they hold their fathers' deeds (Berakhot 7a); revoked by Ezekiel (Makkot 24a)"),
    ('Deut 5:10 — the_ketiv', lambda: the_second_word({'ask': 'the_ketiv'}, DATA), "the ketiv (5:10) — 'his' written, 'my' read: a DATA note, no line"),
    ('the write — the_write', lambda: the_second_word({'ask': 'the_write'}, DATA), "the write (5:7-10) — other_gods_barred on Israel: the code's hole filled at the code's own line"),
    # F3 — the_first_tablet
    ('Deut 5:6 — the_first_word', lambda: the_first_tablet({'ask': 'the_first_word'}, DATA), "the first word (5:6) — VERBATIM; NO CELL: a declaration heard from the Almighty's mouth"),
    ('Deut 5:7-10 — the_second_word_row', lambda: the_first_tablet({'ask': 'the_second_word_row'}, DATA), 'the second word (5:7-10) — VERBATIM, VARIANT, VARIANT, VARIANT: the cell F2 (compiled here)'),
    ('Deut 5:11 — the_third_word', lambda: the_first_tablet({'ask': 'the_third_word'}, DATA), 'the third word (5:11) — VERBATIM: decalogue.vain_name by CALL (the vain oath lashed; Mishnah Shevuot 3:8-9)'),
    ('Deut 5:12-15 — the_fourth_word', lambda: the_first_tablet({'ask': 'the_fourth_word'}, DATA), 'the fourth word (5:12-15) — EXPANDED, VERBATIM, EXPANDED, TURNED: decalogue.sabbath_clauses by CALL'),
    ('Deut 5:12; Shevuot 20b — keep_and_remember', lambda: the_first_tablet({'ask': 'keep_and_remember'}, DATA), "keep and remember (5:12) — one utterance: the diff's first word the tradition's exhibit; women's kiddush (Berakhot 20b)"),
    ('Deut 5:14; Bava Kamma 54b — the_ox_and_the_ass', lambda: the_first_tablet({'ask': 'the_ox_and_the_ass'}, DATA), 'the ox and the ass (5:14) — every animal by the verbal analogy: the expansion read by the tradition itself (Bava Kamma 54b)'),
    ('Deut 5:14; Yevamot 48b — the_servants_rest', lambda: the_first_tablet({'ask': 'the_servants_rest'}, DATA), "the servants' rest (5:14) — the circumcised slave and the righteous convert (Yevamot 48b); the analogy's limit (Bava Kamma 54b)"),
    ('Deut 5:15 — the_two_grounds', lambda: the_first_tablet({'ask': 'the_two_grounds'}, DATA), 'the two grounds (5:15) — the creation (20:11, PS by CALL) and the exodus: a DATA row; the readback row TURNED'),
    ('Deut 5:12; Sanhedrin 56b — the_receipt_5_12', lambda: the_first_tablet({'ask': 'the_receipt_5_12'}, DATA), 'the receipt at 5:12 — a run citation of the giving (the ink) read as Marah (the teacher): the seat CHAPTER'),
    # F4 — the_second_tablet
    ('Deut 5:16 — the_fifth_word', lambda: the_second_tablet({'ask': 'the_fifth_word'}, DATA), "the fifth word (5:16) — EXPANDED: NO CELL at the Decalogue's seat, holiness.frame by CALL (the honor and the fear defined, Kiddushin 31b)"),
    ('Deut 5:17 — the_sixth_word', lambda: the_second_tablet({'ask': 'the_sixth_word'}, DATA), 'the sixth word (5:17) — VERBATIM: mishpatim_3.killer and refuge.the_murderer by CALL'),
    ('Deut 5:18 — the_seventh_word', lambda: the_second_tablet({'ask': 'the_seventh_word'}, DATA), 'the seventh word (5:18) — VARIANT: sanctions.adultery by CALL (Leviticus 20:10)'),
    ('Deut 5:19; Sanhedrin 86a — the_eighth_word', lambda: the_second_tablet({'ask': 'the_eighth_word'}, DATA), 'the eighth word (5:19) — VARIANT: the theft of persons by the context (Sanhedrin 86a); decalogue.theft_commandment by CALL'),
    ('Deut 5:20 — the_ninth_word', lambda: the_second_tablet({'ask': 'the_ninth_word'}, DATA), 'the ninth word (5:20) — TURNED: vain for false, the parameter a DATA row; ordinances.courts by CALL (23:1)'),
    ('Deut 5:21 — the_tenth_word_row', lambda: the_second_tablet({'ask': 'the_tenth_word_row'}, DATA), 'the tenth word (5:21) — TURNED: the cell F5 (compiled here)'),
    ('Deut 5:16; Bava Kamma 55a — the_reward_clause', lambda: the_second_tablet({'ask': 'the_reward_clause'}, DATA), "the reward clause (5:16) — the expansion's own Talmud row: 'good' not in the first tablets (Bava Kamma 55a)"),
    ('Deut 5:16; Sanhedrin 56b — the_receipt_5_16', lambda: the_second_tablet({'ask': 'the_receipt_5_16'}, DATA), 'the receipt at 5:16 — a run citation of the giving read as Marah: the seat CHAPTER'),
    ('Deut 5:6-21 — the_counts', lambda: the_second_tablet({'ask': 'the_counts'}, DATA), 'the counts (5:6-21) — 189 tokens / 708 letters against 172 / 620: recomputed'),
    # F5 — the_tenth_word
    ('Deut 5:21 — covet_and_desire', lambda: the_tenth_word({'ask': 'covet_and_desire'}, DATA), "covet and desire (5:21) — the two verbs: the tenth word compiled here; the block coveting_barred on Israel at the giving's line"),
    ('Deut 5:21 — the_wife_first', lambda: the_tenth_word({'ask': 'the_wife_first'}, DATA), 'the wife first (5:21) — the order turned, his field added: a DATA row'),
    ('shelf: Bava Metzia 5b:19-20 — the_coveter_who_pays', lambda: the_tenth_word({'ask': 'the_coveter_who_pays'}, DATA), "the coveter who pays (5:21) — the prohibition stands (Rav Acha), the people's reading spares his oath: not a robber (Bava Metzia 5b)"),
    ('the write — the_write', lambda: the_tenth_word({'ask': 'the_write'}, DATA), "the write (5:21) — coveting_barred on Israel: the code's hole filled at the code's own line"),
    # F6 — the_voice_and_the_request
    ('Deut 5:22 — added_no_more', lambda: the_voice_and_the_request({'ask': 'added_no_more'}, DATA), "added no more (5:22) — 2b's ten words and tablets FOUND (OH by CALL); 'did not cease' the Talmud's and Onkelos's reading"),
    ('Deut 5:22 — the_tablets_given_to_me', lambda: the_voice_and_the_request({'ask': 'the_tablets_given_to_me'}, DATA), 'the tablets given to me (5:22) — tablets_given FOUND at (1, 4, 17); no second write'),
    ('Deut 5:23 — you_came_near', lambda: the_voice_and_the_request({'ask': 'you_came_near'}, DATA), "you came near (5:23) — 1:22's phrase at its second seat: the mob and the elders (OS by CALL; the Sifrei 20:1)"),
    ('Deut 5:24-27 — the_request', lambda: the_voice_and_the_request({'ask': 'the_request'}, DATA), "the request (5:24-27) — SUPPLIED: the tape's second hole written once at its own time; the mediator asked for (Makkot 24a)"),
    ('Deut 5:27; Shabbat 88a — hear_and_do', lambda: the_voice_and_the_request({'ask': 'hear_and_do'}, DATA), "hear and do (5:27) — TURNED against 24:7's 'do and hear' (Shabbat 88a); Onkelos 'accept and do'"),
    ('the write — the_write', lambda: the_voice_and_the_request({'ask': 'the_write'}, DATA), "the write (5:23-27) — torah_through_moses on Israel: the mediator's status"),
    # F7 — the_answer_and_the_charge
    ('Deut 5:28 — the_lord_heard', lambda: the_answer_and_the_charge({'ask': 'the_lord_heard'}, DATA), "the LORD heard (5:28) — 1:34's phrase at its second seat (OS by CALL)"),
    ('Deut 5:28 — done_well', lambda: the_answer_and_the_charge({'ask': 'done_well'}, DATA), 'they have done well (5:28) — cited forward at 18:17: a DATA note'),
    ('Deut 5:29; Avodah Zarah 4b-5a — who_would_give', lambda: the_answer_and_the_charge({'ask': 'who_would_give'}, DATA), "who would give (5:29) — the calf and the penitents (Avodah Zarah 4b-5a): an aggadah on the answer's verse"),
    ('Deut 5:30; Beitzah 5a-b — return_to_your_tents', lambda: the_answer_and_the_charge({'ask': 'return_to_your_tents'}, DATA), 'return to your tents (5:30) — the separation released: returned_to_tents on Israel (Beitzah 5a-b)'),
    ('Deut 5:31 — stand_here_with_me', lambda: the_answer_and_the_charge({'ask': 'stand_here_with_me'}, DATA), 'stand here with me (5:31) — SUPPLIED: the charge to teach a debit on Moses closed by the prior run (Deut 1:5); the Torah received standing'),
    ('Deut 5:32-33 — the_charge', lambda: the_answer_and_the_charge({'ask': 'the_charge'}, DATA), "the charge (5:32-33) — no write: the frame's close; the plural receipt's seat CHAPTER"),
    ('Deut 5:1-33 — the_readback_table', lambda: the_answer_and_the_charge({'ask': 'the_readback_table'}, DATA), 'the readback table — twenty-one rows graded (sixteen on the code, five on the narrative); no row open'),
    ('Deut 5:12, 16, 32 — the_register_seats', lambda: the_answer_and_the_charge({'ask': 'the_register_seats'}, DATA), "the register seats — Deut 5:12, 5:16, 5:32 CHAPTER (the gate's code); 4:45 DAEMONS 2"),
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
    print('THE INK: numbers %s; the one frame %s; the case tokens %s; the register singular-only %s, plural-only %s, both %s; the ketiv at 5:10' % (sorted(PARSED.items()), DIV, dict(collections.Counter(x for l in CASE_TOK.values() for x in l)), SG_ONLY, PL_ONLY, BOTH))
    print('THE LAWS\' READBACK: %d rows — %s; the law rows %d (the cells named %d, NO CELL %s); the deltas: the frame %s; the voice %s; the request %s; hear and do %s; the answer %s' % (len(READBACK), dict(RB_GRADES), sum(1 for r in READBACK if r['law']), sum(1 for r in READBACK if r['law'] and r['cell'] != 'NO CELL'), [r['verses'] for r in READBACK if r['cell'] == 'NO CELL'], FRAME_DIFF, VOICE_DELTA, REQUEST_DELTA, HEAR_DO_DELTA, ANSWER_DELTA))
    print('THE TWO COPIES: %s (tokens, letters) — Exodus 20:2-17 against Deuteronomy 5:6-21; per word %s' % (COPIES, WORD_TOK))
    print('THE HOLES: the tape\'s first (2b) %s; the second — Exodus 20:18-21 no line (this sitting); the code\'s — the second and the tenth words compiled here' % (OH_HOLE,))
    print('THE CALLEES: the honor %s; the fear %s; the days %s; we will do %s; Marah %s' % (HO_HONOR['v'], HO_FEAR['v'], ES_DAYS['v'], ES_SEATS['v'], ES_MARAH['v']))
    print('THE SCENE on the bench: %s; the exempt and stoned arms %s; the timers (set, fired, cancelled, pending) %s; entities %d; closes %d' % (SCENE[0], SCENE[1], SCENE[2], SCENE[3], SCENE[4]))
    print('THE NARRATIVE: %s' % (NARRATIVE,))
    print('THE PARAMETER ROWS: ' + '; '.join('%s = %s' % (k, DATA[k]['value'] if k != 'the_readback' else '%d rows' % len(DATA[k]['value'])) for k in DATA) + ' (the other settings recorded in DATA)')
    if ok == len(CASES):
        print('\nTHE COMPILE OF CHAPTER 5: the answer sheet REPRODUCED — %d/%d' % (ok, len(CASES)))
    sys.exit(0 if ok == len(CASES) else 1)
