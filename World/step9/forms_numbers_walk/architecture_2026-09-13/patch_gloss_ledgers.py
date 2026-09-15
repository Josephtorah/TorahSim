import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE PROJECT REVIEW, finding 13's ledger side (2026-09-14; the owner's ruling "ok first one go": a gloss is DISPLAY, not content —
# an English gloss beside a Hebrew word changes no reading and no verdict, so the old ledgers are edited in place at the flagged
# word). The lint's window is ninety characters, stops at a period, and checks the FIRST occurrence of each run / compound / term.
# Every replacement asserted once; a pair already applied is skipped. Every gloss read at its verse or its row.
R = (_ROOT + '/')
O = R + 'logic/oral_triage/'
def patch(path, pairs):
    p = R + path if not path.startswith('/') else path
    t = open(p, encoding='utf-8').read(); done = 0
    for old, new in pairs:
        n = t.count(old)
        if n == 0 and new in t: continue
        assert n == 1, (path, n, old[:60]); t = t.replace(old, new); done += 1
    open(p, 'w', encoding='utf-8').write(t); print('patched', path.split('/')[-1], done)
patch('logic/oral_triage/EXOD_TALMUD_TRIAGE_LEDGER.md', [('- AGGADAH — narrative/homiletic expansion of Exodus', '- AGGADAH (the narrative lore) — narrative/homiletic expansion of Exodus')])
patch('logic/oral_triage/exo_22_property_social_2026-09-01.md', [
 ('the pikuach-nefesh seed in', 'the pikuach-nefesh (the saving of life) seed in'),
 ('kal va-chomer to hekdesh)', 'kal va-chomer (the a-fortiori argument) to hekdesh)'),
 ('(ed ha-terefah, R. Yonatan', '(ed ha-terefah, the torn carcass as witness, R. Yonatan'),
 ('R. Yishmael sword (lo-tichyeh to', "R. Yishmael sword (lo-tichyeh 'you shall not let live' to"),
 ('יחרם read as EXECUTION.', "יחרם ('shall be devoted') read as EXECUTION."),
 ('fearing-the-LORD-and-serving-their-gods', 'fearing the LORD and serving their gods'),
 ('with דיניא consistently for the court tokens).', "with דיניא ('judges') consistently for the court tokens)."),
])
patch('logic/oral_triage/exo_23_escort_land_2026-09-01.md', [
 ('double verbs (פַגָרָא תְּפַגְרִנוּן וְתַבָּרָא תְתַבַּר).', "double verbs (פַגָרָא תְּפַגְרִנוּן 'you shall utterly overthrow them' וְתַבָּרָא תְתַבַּר 'and utterly break')."),
 ('עֲרָעִיתָא — carried as the creature', "עֲרָעִיתָא ('the hornet') — carried as the creature"),
 ('(יְחַיְבוּן יָתָךְ קֳדָמָי)...', "(יְחַיְבוּן יָתָךְ קֳדָמָי 'they make you sin before Me')…"),
])
patch('logic/oral_triage/exo_23_justice_calendar_2026-09-01.md', [('(R. Yoshiyah both-in-perikah + the a-fortiori', '(R. Yoshiyah both-in-perikah (both verses in the unloading) + the a-fortiori')])
patch('logic/oral_triage/exo_24_covenant_ascent_2026-09-01.md', [
 ('kept (לְבָרִירוּ).', "kept (לְבָרִירוּ 'in clearness')."),
 ('ONE VOICE (קָלָא חַד).', "ONE VOICE (קָלָא חַד 'one voice')."),
 ('the receiving-verb the Targum uses for obedience', 'the receiving-verb the Targum (the Aramaic translation) uses for obedience'),
 ('CUT (דִגְזַר) with you', "CUT (דִגְזַר 'cut') with you"),
])
patch('logic/oral_triage/exo_25_ark_table_menorah_2026-09-01.md', [
 ('the same double-buffering exo_24 recorded', 'the same double-buffering (two layers held at once) exo_24 recorded'),
 ('SHOWN (מַחֲזֵי) a likeness', "SHOWN (מַחֲזֵי 'shown') a likeness"),
 ('rendered לְחֵם אַפַּיָּא... תְּדִירָא (', "rendered לְחֵם אַפַּיָּא ('the bread of the face') … תְּדִירָא ("),
 ('the תדיר continuity-token', "the תדיר ('continual') continuity-token"),
 ('from מאת כל איש... תקחו', "from מאת כל איש ('from every man') … תקחו"),
 ('five-disqualified table verbatim at Buber 2', 'five-disqualified table, the same one, verbatim at Buber 2'),
])
patch('logic/oral_triage/exo_26_curtains_boards_2026-09-01.md', [('Midrash Tanchuma joins Onkelos', 'Midrash Tanchuma (the collection) joins Onkelos')])
patch('logic/oral_triage/exo_27_altar_court_2026-09-01.md', [('Midrash Tanchuma joins Onkelos', 'Midrash Tanchuma (the collection) joins Onkelos')])
patch('logic/oral_triage/exo_29_investiture_2026-09-01.md', [
 ('(וּתְקָרֵב קֻרְבָּנָא — 29:9', "(וּתְקָרֵב קֻרְבָּנָא 'and you shall bring near the offering' — 29:9"),
 ('וְיִסְמוֹךְ ... יָת', "וְיִסְמוֹךְ ('and he shall lean') … יָת"),
 ('(לְכַהֵן לִי — our 29:1)', "(לְכַהֵן לִי 'to serve Me as priest' — our 29:1)"),
])
patch('logic/oral_triage/exo_30_incense_shekel_2026-09-01.md', [('(the pairing-of-couples', '(the pairing-of-couples, the matchmaking,')])
patch('logic/oral_triage/exo_32_golden_calf_2026-09-01.md', [('wrath-pacified frame).', 'wrath-pacified (the wrath appeased) frame).')])
patch('logic/oral_triage/exo_33_presence_2026-09-01.md', [
 ('the reflexive מִתְמַלֵּל guarding', "the reflexive מִתְמַלֵּל ('was spoken with') guarding"),
 ("33:14's פָּנַי יֵלֵכוּ as the", "33:14's פָּנַי יֵלֵכוּ ('My presence will go') as the"),
])
patch('logic/oral_triage/exo_35_36_work_start_2026-09-02.md', [
 ('line: מִסַּת לְכָל עִבִדְתָּא... וִיתָרָת (', "line: מִסַּת לְכָל עִבִדְתָּא ('enough for all the work') … וִיתָרָת ("),
 ('(סַסְגּוֹנָא) covers.', "(סַסְגּוֹנָא 'the multicolored skin') covers."),
 ('The frame: דַּפַּיָּא... קָיְמִין', "The frame: דַּפַּיָּא ('planks') … קָיְמִין"),
 ("mitzvah-drags-mitzvah and R. Meir's", "mitzvah-drags-mitzvah (one commandment draws another) and R. Meir's"),
])
patch('logic/oral_triage/exo_35_shabbat_donate_2026-09-02.md', [('spinners דְּאִתְרְעֵי לִבְּהֶן...', "spinners דְּאִתְרְעֵי לִבְּהֶן ('whose hearts moved them') …")])
patch('logic/oral_triage/exo_37_furniture_made_2026-09-02.md', [
 ("(EX30-06's karet-guarded", "(EX30-06's karet-guarded (guarded by excision)"),
 ('8:1 pre-provisioning row states', '8:1 pre-provisioning (provided beforehand) row states'),
])
patch('logic/oral_triage/exo_38_court_inventory_2026-09-02.md', [
 ('מְכֻוָּן reading).', "מְכֻוָּן ('aligned') reading)."),
 ('the two רְאֵה', "the two רְאֵה ('see')"),
])
patch('logic/oral_triage/exo_40_erect_fill_2026-09-02.md', [
 ('יָכִיל... לְמֵעַל (', "יָכִיל ('was not able') … לְמֵעַל ("),
 ('(the beautiful נוֹף that SIFTS the nations).', "(the beautiful נוֹף 'height' that SIFTS the nations)."),
 ('(עָרְבָה read from the evening-word)', "(עָרְבָה 'darkened' read from the evening-word)"),
])
patch('logic/oral_triage/exodus_backfill_mishnah_2026-09-01.md', [
 ('food-sorting law;', 'food-sorting (the sorting of food) law;'),
 ('(עדים זוממין) who testified', "(עדים זוממין 'conspiring witnesses') who testified"),
 ('הברזל נברא לקצר... והמזבח נברא להאריך (', "הברזל נברא לקצר ('iron was created to shorten') … והמזבח נברא להאריך ("),
 ('— וימררו, our 1:14).', "— וימררו ('and they embittered'), our 1:14)."),
 ('שחטו קדם חצות פסול...', "שחטו קדם חצות פסול ('slaughtered before midday, invalid') …"),
 ('flow-impure (זבין) still', "flow-impure (זבין 'those with a flow') still"),
 ('R. Akiva: אז ישיר... ויאמרו לאמר (', "R. Akiva: אז ישיר ('then sang') … ויאמרו לאמר ("),
 ('geometry of כי יגנב איש שור או שה); no', "geometry of כי יגנב איש שור או שה 'when a man steals an ox or a sheep'); no"),
 ('nefesh-tachat-nefesh token', "nefesh-tachat-nefesh ('life for life') token"),
])
patch('logic/oral_triage/exodus_block_matza_2026-09-04.md', [('THE KETIV: R. Yishmael counts', 'THE KETIV (the written form): R. Yishmael counts')])
patch('logic/oral_triage/exodus_block_shabbat_2026-09-04.md', [('(אכלהו היום... היום... היום — "eat it TODAY', "(אכלהו היום ('eat it today') … היום … היום — \"eat it TODAY")])
patch('logic/oral_triage/gen_01_creation_boot_2026-07-30.md', [
 ("BR 3:7's seder-zemanim mood argument", "BR 3:7's seder-zemanim (the order of times) mood argument"),
 ('by the choshekh-symmetry + stars-out contradiction', 'by the choshekh-symmetry (the darkness symmetry) + stars-out contradiction'),
 ('a marked, deliberate re-tokenization for an altar homily', 'a marked, deliberate re-tokenization (a re-cutting of the word) for an altar homily'),
 ("Beit Hillel's hayetah-pluperfect argument again |", "Beit Hillel's hayetah-pluperfect ('it had been', the pluperfect) argument again |"),
 ('| tov-le-khol homily |', "| tov-le-khol ('good to all') homily |"),
 ('(tzidkatekha ke-harerei el)', "(tzidkatekha ke-harerei el = 'your righteousness is like the mighty mountains')"),
 ('naghei/leilei bedikat-chametz sugya', 'naghei/leilei bedikat-chametz (the search for leaven) sugya'),
 ('| wine gematria homily |', '| wine gematria (letter-count) homily |'),
 ("the minim's how-many-deities challenge", "the minim's how-many-deities (how many gods) challenge"),
 ('| yelamdenu-question frame', "| yelamdenu-question (the 'let our master teach us' opening) frame"),
 ('a qatal-semantics move', "a qatal-semantics (the perfect verb's sense) move"),
 ("the minim's how-many-authorities challenge", "the minim's how-many-authorities (how many powers) challenge"),
 ("(cf. row 406's din-then-rachamim)", "(cf. row 406's din-then-rachamim = justice then mercy)"),
 ('| 467 | Midrash Aggadah, Exodus 21:1:2 |', '| 467 | Midrash Aggadah (the collection), Exodus 21:1:2 |'),
])
patch('logic/oral_triage/gen_02_raqia_day_2026-08-23.md', [
 ('the jussive read as strengthen-the-existing;', "the jussive (the 'let it be' form) read as strengthen-the-existing (strengthening what exists);"),
 ('the vayhi-woe polarity rule', "the vayhi-woe ('and it was' as woe) polarity rule"),
])
patch('logic/oral_triage/gen_03_double_build_2026-08-23.md', [
 ('the kav-measure + yekavu-await + mute-palace', "the kav-measure + yekavu-await ('let them gather' as await) + mute-palace"),
 ('(li-zneh, tree only)', "(li-zneh 'after its kind', tree only)"),
 ('the vayhi-woe polarity rule', "the vayhi-woe ('and it was' as woe) polarity rule"),
])
patch('logic/oral_triage/gen_04_lights_calendar_2026-07-30.md', [
 ('owner of the three-orthographies flag;', 'owner of the three-orthographies (three spellings) flag;'),
 ('| 32 | Midrash Aggadah, Exodus 38:21:2 |', '| 32 | Midrash Aggadah (the collection), Exodus 38:21:2 |'),
 ('the ha-chodesh piska, PR recension', "the ha-chodesh ('this month') piska, PR recension"),
 ('| 110 | Tanna DeBei Eliyahu Zuta, Additions', '| 110 | Tanna DeBei Eliyahu Zuta (the collection), Additions'),
])
patch('logic/oral_triage/gen_05_swarms_blessing_2026-07-30.md', [
 ('Targum Jonathan; no Targum Jerusalem', 'Targum Jonathan (the Aramaic translation); no Targum Jerusalem'),
 ('| the fish-shechitah episode in the Solomon frame |', "| the fish-shechitah (the fish's slaughter) episode in the Solomon frame |"),
 ('the ein-tzayyar catalogue', "the ein-tzayyar ('there is no artist like our God') catalogue"),
])
patch('logic/oral_triage/gen_06_land_adam_dominion_2026-08-23.md', [
 ('the du-partzufin reading', 'the du-partzufin (the double-formed human) reading'),
 ('ketiv/qere family, honestly unnumbered', 'ketiv/qere (the written and the read forms) family, honestly unnumbered'),
 ('— vayhi-woe polarity at our commit tokens', "— vayhi-woe ('and it was' as woe) polarity at our commit tokens"),
 ('kind-word li-znah per class', "kind-word li-znah ('after its kind') per class"),
])
patch('logic/oral_triage/gen_48_bethel_ladder_vow_2026-08-27.md', [('four namings (almond-fruitfulness; no-mouth', "four namings (almond-fruitfulness, the almond's fruit; no-mouth")])
for f in ['gen_51_opened_womb_twelve_names_2026-08-27.md', 'gen_52_send_me_speckled_wage_rods_2026-08-27.md', 'gen_54_pursuit_heap_two_tongues_2026-08-27.md']:
    patch('logic/oral_triage/' + f, [('Sarah and Toledot ledgers on 2026-08-30.', "Sarah and Toledot ('generations') ledgers on 2026-08-30.")])
for f in ['gen_56_blessing_returned_first_altar_2026-08-27.md', 'gen_57_deceit_at_the_gate_2026-08-27.md', 'gen_58_israel_written_three_deaths_2026-08-27.md', 'gen_59_esau_edom_kings_ledger_2026-08-27.md']:
    patch('logic/oral_triage/' + f, [('Sarah, Toledot and Vayetze ledgers', "Sarah, Toledot ('generations') and Vayetze ledgers")])
patch('logic/oral_triage/gen_56_blessing_returned_first_altar_2026-08-27.md', [('(33:4): va-yishakehu carries scribal DOTS', "(33:4): va-yishakehu ('and he kissed him') carries scribal DOTS")])
patch('logic/oral_triage/gen_61_yehuda_tamar_2026-08-28.md', [('the Ketura-perfumed-with-mitzvot naming pattern', 'the Ketura-perfumed-with-mitzvot (perfumed with commandments) naming pattern')])
patch('logic/oral_triage/gen_63_two_dreams_prison_2026-08-28.md', [('7 of its 10 midrash sources', '7 of its 10 midrash (rabbinic) sources')])
patch('logic/oral_triage/gen_67_cup_and_surety_2026-08-28.md', [('quoted inside the midrash [the two-shelves', 'quoted inside the midrash (the rabbinic reading) [the two-shelves')])
patch('logic/oral_triage/gen_69_descent_seventy_2026-08-28.md', [('as Sheva son of Bikhri was', 'as Sheva son of Bikhri (the man, 2 Samuel 20) was')])
patch('logic/oral_triage/gen_72_testament_twelve_2026-08-28.md', [
 ('‹יַקְהֶה› the teeth', "‹יַקְהֶה› ('he will blunt') the teeth"),
 ('the THIGH ‹יָרֵךְ› from which he came', "the THIGH ‹יָרֵךְ› ('thigh') from which he came"),
])
patch('logic/oral_triage/kitisa_exam_mishnah_2026-09-01.md', [
 ('אֲשֶׁר לֹא יְעָדָהּ וְהֶפְדָּהּ);', "אֲשֶׁר לֹא יְעָדָהּ וְהֶפְדָּהּ 'whom he has not designated, he shall let her be redeemed');"),
 ('A cross-domain duty-ordering algebra.', 'A cross-domain duty-ordering (which duty first) algebra.'),
])
patch('logic/oral_triage/lev_01_call_and_korban_opening_2026-09-03.md', [('A name-pairing invariant', 'A name-pairing (which Name the word pairs with) invariant')])
patch('logic/oral_triage/lev_01_olah_bird_2026-09-03.md', [('wall-wringing carried plainly.', "wall-wringing (the wringing at the altar's wall) carried plainly.")])
patch('logic/oral_triage/lev_03_shelamim_2026-09-03.md', [('(lo-lishmah) validity', "(lo-lishmah 'not for its own sake') validity")])
patch('logic/oral_triage/lev_05_asham_graded_2026-09-03.md', [('oath-then-witnessing is outside the class.', 'oath-then-witnessing (the oath before the witnessing) is outside the class.')])
patch('logic/oral_triage/mishpatim_exam_mishnah_2026-09-01.md', [
 ('wind-fanned all exempt);', 'wind-fanned (fanned by the wind) all exempt);'),
 ('— ראשית... תביא', "— ראשית ('the first') … תביא"),
 ('the lo-taaneh clause', "the lo-taaneh ('you shall not answer') clause"),
 ('the pesach-chametz\n', 'the pesach-chametz (Passover and leaven)\n'),
])
patch('logic/oral_triage/noahide_exam_reading_2026-09-01.md', [
 ('from איש איש).', "from איש איש 'any man')."),
 ('אזהרה שלהן זו היא מיתתן — THEIR PROHIBITION', "אזהרה שלהן זו היא מיתתן ('their prohibition is their death') — THEIR PROHIBITION"),
 ('aggadah-book baraita:', 'aggadah-book (the lore book) baraita:'),
 ('a shibbuta-fish).', 'a shibbuta-fish (a river fish)).'),
])
patch('logic/oral_triage/talmud_triage_gen_2026-09-01.md', [('- AGGADAH — narrative/homiletic expansion of Genesis', '- AGGADAH (the narrative lore) — narrative/homiletic expansion of Genesis')])
patch('logic/oral_triage/tetzaveh_exam_mishnah_2026-09-01.md', [
 ("own זֹג token", "own זֹג ('bell') token"),
 ('bringing-near in the WEST,', "bringing-near (the offering's approach) in the WEST,"),
])
patch('logic/oral_triage/vayakhel_pekudei_exam_mishnah_2026-09-02.md', [('(יְצִיאוֹת הַשַּׁבָּת שְׁתַּיִם שֶׁהֵן אַרְבַּע),', "(יְצִיאוֹת הַשַּׁבָּת שְׁתַּיִם שֶׁהֵן אַרְבַּע 'the carryings-out of the Sabbath are two which are four'),")])
patch('World/step9/EXAM_LEDGER.md', [
 ('ve-khivshuha ketiv).', 've-khivshuha ketiv, the written form).'),
 ('Midrash Tanchuma Ki Tisa whole', 'Midrash Tanchuma (the collection) Ki Tisa whole'),
 ("EX13-08's Masorah chain held", "EX13-08's Masorah (the scribal tradition) chain held"),
 ("R. Shimon's always-accepting w/ the Yom", "R. Shimon's always-accepting (always susceptible) w/ the Yom"),
 ('the replicable-attendants ladder', 'the replicable-attendants (attendants one may copy) ladder'),
 ('flags verified pre-existing at HEAD).', 'flags verified pre-existing (there before) at HEAD).'),
])
patch('World/step9/REPORT_CANON_HUNT.md', [
 ('וְלֹא יְחַשְּׁבוּ אֶת הָאֲנָשִׁים... כִּי', "וְלֹא יְחַשְּׁבוּ אֶת הָאֲנָשִׁים ('they did not reckon with the men') … כִּי"),
 ('אַךְ לֹא יֵחָשֵׁב אִתָּם\n', "אַךְ לֹא יֵחָשֵׁב אִתָּם ('only there was no reckoning with them')\n"),
 ('הַכֶּסֶף... כִּי בֶאֱמוּנָה הֵם עֹשִׂים — THE SAME', "הַכֶּסֶף ('the silver') … כִּי בֶאֱמוּנָה הֵם עֹשִׂים ('for they dealt faithfully') — THE SAME"),
 ('as THE TARGUM: the public', 'as THE TARGUM (the Aramaic translation): the public'),
])
patch('World/step9/REPORT_FESTIVALS.md', [
 ('(the Masorah chain on the tefillin verse)', '(the Masorah, the scribal tradition, chain on the tefillin verse)'),
 ('with the two-hoeings refinement;', 'with the two-hoeings (the two diggings) refinement;'),
])
patch('logic/CORE_SHELF.md', [('differently-versified chapters excluded and named', 'differently-versified chapters (their verse divisions differ) excluded and named')])
