

# =====================================================================
# Motion 2 — THE TEST DATA: the answer sheet's rows (the docket's LAW rows and the cells' asks) — GENERATED FROM THE CELLS' OWN ASKS by ch4_cases_gen.py
# (1b's lesson: a mistyped expected string grades nothing), then frozen as literals under the honest-pairing guard.
# =====================================================================
CASES = [
    # F1 — the_exhortation
    ('Deut 4:1 — hear_and_do', lambda: the_exhortation({'ask': 'hear_and_do'}, DATA), "hear and do (4:1) — the exhortation's head: the singular imperative, the plural object; the teach-root's first seat"),
    ('Deut 4:2 — add_nothing', lambda: the_exhortation({'ask': 'add_nothing'}, DATA), "you shall not add (4:2) — THE CHAPTER'S ONE LAW: a BLOCK on Israel (adding_barred); the exam's parameters — in its time without intent, out of its time with intent (Rava); an addition that spoils (the elder's fifth compartment)"),
    ('Deut 4:2 — diminish_nothing', lambda: the_exhortation({'ask': 'diminish_nothing'}, DATA), "nor diminish (4:2) — the pair's other arm: an omission where adding is an act (R. Yehoshua); 13:1 the second seat forward"),
    ('shelf: Rosh Hashanah 28b:9 — add_out_of_its_time', lambda: the_exhortation({'ask': 'add_out_of_its_time'}, DATA), 'an addition out of its time (Rosh Hashanah 28b) — no intent, no transgression: the sleeper on the eighth day exempt'),
    ('shelf: Sanhedrin 89a:2 — add_beside', lambda: the_exhortation({'ask': 'add_beside'}, DATA), 'an addition placed beside (Sanhedrin 89a) — the four compartments stand alone: no spoiling, exempt'),
    ('Deut 4:3 — baal_peor_seen', lambda: the_exhortation({'ask': 'baal_peor_seen'}, DATA), "Baal-peor seen (4:3) — Numbers 25:3-9 READ BACK, SHORTENED: the yoking, the slaying and the plague's count in one clause (BK by CALL)"),
    ('Deut 4:4 — the_cleaving', lambda: the_exhortation({'ask': 'the_cleaving'}, DATA), 'you who cleave (4:4) — the survivors of Peor; cleaving to a consuming fire resolved as cleaving to the sages (the Sifrei 49:2; Ketubot 111b)'),
    ('Deut 4:5 — taught_as_commanded', lambda: the_exhortation({'ask': 'taught_as_commanded'}, DATA), "taught as commanded (4:5) — THE RECEIPT in Moses' own voice: the teaching's run of Exodus 24:12's command (ER by CALL); the register seat ACT; free teaching (Bekhorot 29a)"),
    ('Deut 4:6 — wisdom_before_the_peoples', lambda: the_exhortation({'ask': 'wisdom_before_the_peoples'}, DATA), "your wisdom before the peoples (4:6) — the reckoning of the seasons (Shabbat 75a); Solomon's pair the kin"),
    ('Deut 4:7 — god_so_near', lambda: the_exhortation({'ask': 'god_so_near'}, DATA), "God so near (4:7) — the plural adjective with the singular 'upon him' (Sanhedrin 38b); a community's sentence never sealed (Rosh Hashanah 18a)"),
    ('Deut 4:8 — righteous_statutes', lambda: the_exhortation({'ask': 'righteous_statutes'}, DATA), "righteous statutes (4:8) — the exhortation's close: the Torah set before them this day (11:32 the pair)"),
    ('Deut 4:1-8 — the_write', lambda: the_exhortation({'ask': 'the_write'}, DATA), "the write (4:1-8) — adding_barred on Israel: the one law's block; the receipt inside the line's source"),
    # F2 — horeb_retold
    ('Deut 4:9 — take_heed_lest_you_forget', lambda: horeb_retold({'ask': 'take_heed_lest_you_forget'}, DATA), "take heed lest you forget (4:9) — the forgetter's prohibition (Menachot 99b; Avot 3:8); the grandsons included, the daughters excluded (Kiddushin 30a)"),
    ('shelf: Kiddushin 30a:6 — the_daughters_excluded', lambda: horeb_retold({'ask': 'the_daughters_excluded'}, DATA), "the daughters excluded (Kiddushin 30a) — 'your sons' not your daughters; the grandsons taught: exempt from the duty's addressees"),
    ('Deut 4:10 — the_day_at_horeb', lambda: horeb_retold({'ask': 'the_day_at_horeb'}, DATA), "the day at Horeb (4:10) — the assembly's day (1, 3, 7) by Rabbi Yose's seventh (ES by CALL); the retrograde marker's day at Deut 4:10"),
    ('Deut 4:10 — learn_and_teach', lambda: horeb_retold({'ask': 'learn_and_teach'}, DATA), "learn and teach are one word (4:10) — qal and piel by the pointing alone: the reading's crown, DATA"),
    ('Deut 4:11 — the_mountain_burning', lambda: horeb_retold({'ask': 'the_mountain_burning'}, DATA), 'the mountain burning (4:11) — Exodus 19:17-18 READ BACK, EXPANDED: the heart of heaven, the darkness, cloud and thick darkness told larger than the smoke'),
    ('Deut 4:12 — the_voice_and_no_form', lambda: horeb_retold({'ask': 'the_voice_and_no_form'}, DATA), "the voice and no form (4:12, 15) — THE TAPE'S HOLE: Exodus 20:1's speaking written once at its own time (1, 3, 7) — covenant_declared on Israel (SUPPLIED)"),
    ('Deut 4:13 — the_ten_words_and_the_tablets', lambda: horeb_retold({'ask': 'the_ten_words_and_the_tablets'}, DATA), "the ten words and the tablets (4:13) — three seats of 'the ten words' (ER by CALL); the tablets plene; Exodus 31:18's giving written once at (1, 4, 17) — tablets_delivered on Moses (SUPPLIED)"),
    ('Deut 4:14 — commanded_to_teach', lambda: horeb_retold({'ask': 'commanded_to_teach'}, DATA), "commanded to teach (4:14) — the command 4:5's receipt answers (Exodus 24:12); who was commanded disputed (Nedarim 38a)"),
    # F3 — no_image
    ('Deut 4:15 — no_form_seen', lambda: no_image({'ask': 'no_form_seen'}, DATA), "no form seen (4:15) — the guard's reason: the voice without a form (4:12 read back)"),
    ('Deut 4:16-18 — the_image_list', lambda: no_image({'ask': 'the_image_list'}, DATA), "the no-image list (4:16-18) — Exodus 20:4's likeness restated in seven kinds: THE SECOND WORD'S PARAMETER TABLE as DATA; its engine OWED (chapter 5's sitting)"),
    ('shelf: Rosh Hashanah 24b:13 — image_for_study', lambda: no_image({'ask': 'image_for_study'}, DATA), "the images for study (Rosh Hashanah 24b) — Rabban Gamliel's forms permitted: made by others, in pieces, to teach himself — exempt"),
    ('shelf: Rosh Hashanah 24b:8 — image_of_the_host', lambda: no_image({'ask': 'image_of_the_host'}, DATA), "an image of the host (Rosh Hashanah 24b:8) — forming the sun and the moon prohibited: the second word's row holds (its engine OWED)"),
    ('Deut 4:19 — the_host_apportioned', lambda: no_image({'ask': 'the_host_apportioned'}, DATA), "the host apportioned (4:19) — with 29:25 by the Sifrei 148:8's pair; Rav's reading (Avodah Zarah 55a): a DATA note, no link of our own"),
    ('Deut 4:20 — the_iron_furnace', lambda: no_image({'ask': 'the_iron_furnace'}, DATA), 'the iron furnace (4:20) — the exodus READ BACK, EXPANDED: the furnace told only here in the Torah (1 Kings 8:51 outside; PR by CALL)'),
    ('Deut 4:21-22 — the_bar_third_telling', lambda: no_image({'ask': 'the_bar_third_telling'}, DATA), "the bar's third telling (4:21-22) — 'on your account' and an oath against Numbers 20:12's 'because you did not believe': DISAGREES, the 1b row widened, an OPEN row; no oath written"),
    ('Deut 4:23 — the_covenant_not_forgotten', lambda: no_image({'ask': 'the_covenant_not_forgotten'}, DATA), "the covenant not forgotten (4:23) — the guard's second seat: the covenant cut at Horeb (the tape's covenant_blood_thrown) and the image"),
    ('Deut 4:24 — consuming_fire_jealous_god', lambda: no_image({'ask': 'consuming_fire_jealous_god'}, DATA), "a consuming fire, a jealous God (4:24) — the second word's 'jealous' (Exodus 20:5 by reference); jealousy at the worshipper, not the idol (Avodah Zarah 54b-55a)"),
    # F4 — the_exile_case
    ('Deut 4:25 — the_case_head', lambda: the_exile_case({'ask': 'the_case_head'}, DATA), "the case head (4:25) — THE CHAPTER'S ONE CASE: 'when' with the imperfect; the arms DATA; the exile hastened by two years (Gittin 88a)"),
    ('Deut 4:26 — the_witnesses', lambda: the_exile_case({'ask': 'the_witnesses'}, DATA), "the witnesses (4:26) — heaven and earth called: a STATUS on Israel (the Sifrei 306:1's chain, the third of eleven)"),
    ('Deut 4:26-27 — perish_and_scatter', lambda: the_exile_case({'ask': 'perish_and_scatter'}, DATA), "perish and scatter (4:26-27) — the case's first arm: Leviticus 26:33's scattering by CALL (TC), no entry written"),
    ('Deut 4:28 — serve_wood_and_stone', lambda: the_exile_case({'ask': 'serve_wood_and_stone'}, DATA), 'serve wood and stone (4:28) — 28:36 and 28:64 forward; Psalm 115:5 the kin'),
    ('Deut 4:29 — seek_and_find', lambda: the_exile_case({'ask': 'seek_and_find'}, DATA), "seek and find (4:29) — the case's second arm: the Shema's words (6:5 forward); 30:10's kin"),
    ('Deut 4:30 — in_your_distress_return', lambda: the_exile_case({'ask': 'in_your_distress_return'}, DATA), "in your distress, return (4:30) — the case's third arm: 30:2's kin; 'the end of days' a prophecy, no timer (TC by CALL)"),
    ('Deut 4:31 — the_merciful_god', lambda: the_exile_case({'ask': 'the_merciful_god'}, DATA), "the merciful God (4:31) — Exodus 34:6's attribute; the fathers' covenant sworn (Genesis 22:16, 26:3 by reference); Leviticus 26:42 the first telling"),
    # F5 — the_one_god
    ('Deut 4:32 — the_former_days', lambda: the_one_god({'ask': 'the_former_days'}, DATA), 'the former days (4:32) — the creation READ BACK as a time-reference (PS by CALL); the limits of inquiry (Chagigah 11b)'),
    ('Deut 4:33 — the_voice_and_lived', lambda: the_one_god({'ask': 'the_voice_and_lived'}, DATA), "the voice and lived (4:33) — 5:26's kin; the assembly's lord_descended by reference"),
    ('Deut 4:34 — the_nation_from_a_nation', lambda: the_one_god({'ask': 'the_nation_from_a_nation'}, DATA), "a nation from the midst of a nation (4:34) — the seven instruments: the exodus READ BACK, EXPANDED (ES by CALL); the Haggadah's row (Pesachim 10:4)"),
    ('Deut 4:35 — you_were_shown', lambda: the_one_god({'ask': 'you_were_shown'}, DATA), "you were shown (4:35) — the creed's first seat: 'none else beside him' (even sorcery — Chullin 7b); the kingship verses disputed"),
    ('Deut 4:36 — from_heaven_the_voice', lambda: the_one_god({'ask': 'from_heaven_the_voice'}, DATA), 'from heaven the voice (4:36) — Exodus 20:22 READ BACK (DC by CALL for the seat; the Mekhilta credited by name)'),
    ('Deut 4:37 — because_he_loved_your_fathers', lambda: the_one_god({'ask': 'because_he_loved_your_fathers'}, DATA), "because he loved your fathers (4:37) — the choice of the seed (Genesis 17's phrase; PR by CALL); the outbringing READ BACK"),
    ('Deut 4:38 — to_dispossess_nations', lambda: the_one_god({'ask': 'to_dispossess_nations'}, DATA), 'to dispossess nations (4:38) — the open dispossess debit of Numbers 33:50-56 READ; 9:1 the kin'),
    ('Deut 4:39 — know_this_day', lambda: the_one_god({'ask': 'know_this_day'}, DATA), "know this day (4:39) — the creed's second seat: Rahab's and Solomon's words outside the Torah; the seventh son's (Gittin 57b)"),
    ('Deut 4:40 — keep_the_statutes', lambda: the_one_god({'ask': 'keep_the_statutes'}, DATA), "keep the statutes (4:40) — the reward clause: well with you, prolonged days (5:16's pair forward)"),
    # F6 — the_cities_and_the_frame
    ('Deut 4:41 — then_moses_set_apart', lambda: the_cities_and_the_frame({'ask': 'then_moses_set_apart'}, DATA), "then Moses set apart (4:41) — Moses' own act in the third person: cities_set_apart on Israel (the Song's 'then' form; R. Simlai's mitzva that came his way)"),
    ('Deut 4:41; Num 35:13-14 — not_until_all_six', lambda: the_cities_and_the_frame({'ask': 'not_until_all_six'}, DATA), "not until all six (Makkot 2:4) — the three east admitted no one: the refuge debit on Israel READ OPEN and left open (RF by CALL); the manslayer's refuge exempt until Joshua's three"),
    ('Deut 4:42 — the_manslayer_defined', lambda: the_cities_and_the_frame({'ask': 'the_manslayer_defined'}, DATA), "the manslayer defined (4:42) — 19:4's words with 'slays' for 'smites' (computed); the refuge runner's clauses by CALL; 'and live' the teacher exiled with his school (Makkot 10a)"),
    ('Deut 4:43 — the_three_names', lambda: the_cities_and_the_frame({'ask': 'the_three_names'}, DATA), "the three names (4:43) — Bezer, Ramoth, Golan (RF's row by CALL); the two rows of vines (Makkot 9b:18); Joshua 20:8's Gaulon"),
    ('Deut 4:44-45 — the_second_frame', lambda: the_cities_and_the_frame({'ask': 'the_second_frame'}, DATA), "the second frame (4:44-45) — the second speech's head: a stamp of place and era, NO WRITE (R6); EXPANDED against 1:1-5 (OS by CALL)"),
    ('Deut 4:46-49 — the_borders_verbatim', lambda: the_cities_and_the_frame({'ask': 'the_borders_verbatim'}, DATA), "the borders verbatim (4:46-49) — the retelling of a retelling: the speech's own 1:4, 3:8, 2:36, 3:17 in their own clauses (computed); Mount Sion the fourth name (CK, BO, OS, BK by CALL)"),
    ('Deut 4:3-49 — the_readback_table', lambda: the_cities_and_the_frame({'ask': 'the_readback_table'}, DATA), "the readback table — eleven reference rows graded; the two supplied lines the tape's hole; the one disagreement widened, open (CC4)"),
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
    print('THE INK: numbers %s; the one frame %s; the case tokens %s; the register singular-only %s, plural-only %s, both %s' % (sorted(PARSED.items()), DIV, dict(collections.Counter(x for l in CASE_TOK.values() for x in l)), SG_ONLY, PL_ONLY, BOTH))
    print('THE READBACK: %d rows — %s; the deltas: Peor %s; Horeb %s; the tablets %s; the bar %s; the instruments %s; the frame %s; the borders %s' % (len(READBACK), dict(RB_GRADES), PEOR_DELTA, HOREB_DELTA, TABLETS_DELTA, BAR_DELTA, INSTR_DELTA, FRAME_DELTA, BORDERS_DELTA))
    print('THE HOLE: the ten words %s seats; the tablets plene %s; the giving\'s day %s (Rabbi Yose); the fortieth day %s' % (TEN_WORDS, TABLETS_PLENE, ES_DAYS['v'], ER_TAMMUZ['v']))
    print('THE CITIES: %s; the debit %s; the manslayer\'s diff %s' % (RF.DATA['the_six_cities']['value']['beyond_the_jordan'], RF_DEBIT[0][:60], MANSLAYER_DIFF[2:4]))
    print('THE SCENE on the bench: %s; the exempt arms %s; the timers (set, fired, cancelled, pending) %s; entities %d; closes %d' % (SCENE[0], SCENE[1], SCENE[2], SCENE[3], SCENE[4]))
    print('THE NARRATIVE: %s' % (NARRATIVE,))
    print('THE PARAMETER ROWS: ' + '; '.join('%s = %s' % (k, DATA[k]['value'] if k != 'the_readback' else '%d rows' % len(DATA[k]['value'])) for k in DATA) + ' (the other settings recorded in DATA)')
    if ok == len(CASES):
        print('\nTHE COMPILE OF CHAPTER 4: the answer sheet REPRODUCED — %d/%d' % (ok, len(CASES)))
    sys.exit(0 if ok == len(CASES) else 1)
