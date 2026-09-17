
# ---- THE LAWS' READBACK — the first form's (R1)-(R6) ON LAW: SIXTEEN law rows (one per verse of the code, 5:6-21) graded against the runner's
# cell that compiles each word, and FIVE narrative rows; the deltas recomputed above; VARIANT the grade the code's copy adds ----
GRADES = ('VERBATIM', 'VARIANT', 'TURNED', 'SHORTENED', 'EXPANDED', 'SUPPLIED', 'DISAGREES')
def rb(verses, told, tape_kind, tape_verse, entry, grade, why, open_=False, law=False, cell=None):
    assert grade in GRADES, grade
    return {'verses': verses, 'told': told, 'tape_kind': tape_kind, 'tape_verse': tape_verse, 'entry': entry, 'grade': grade, 'why': why, 'open': open_, 'law': law, 'cell': cell}
def lr(v, grade, cell, told, why):
    e = v - 4
    d = DIFF(('Deut', 5, v), ('Exod', 20, e))
    return rb('Deut 5:%d' % v, told, 'ten_words_declared', 'Deut 4:10', "covenant_declared on israel_people dated (1, 3, 7) — the code's giving on the tape (Exodus 20:%d the first copy; 2b's supplied line at Deut 4:10-13)" % e, grade, '%s [the diff computed against Exodus 20:%d: %s; tokens %d against %d]' % (why, e, d if d else 'none', LEN('Deut', 5, v), LEN('Exod', 20, e)), law=True, cell=cell)
READBACK = [
    lr(6, 'VERBATIM', 'NO CELL', "I am the LORD your God, who brought you out of the land of Egypt, out of the house of bondage", "THE FIRST WORD — a declaration, not a case: NO CELL in any runner and none owed; heard from the Almighty's mouth with the second (Makkot 24a:1 — the two of the six hundred thirteen); nine words the same"),
    lr(7, 'VERBATIM', 'F2 the_second_word (this runner)', "you shall have no other gods before me", "THE SECOND WORD'S HEAD — NO CELL in any runner until this one (the 2b debt): compiled here from both copies; Onkelos 'another god except me'; the second heard from the Almighty's mouth (Makkot 24a:1); the block other_gods_barred written at the giving's line"),
    lr(8, 'VARIANT', 'F2 the_second_word (this runner)', "you shall not make for yourself a graven image, any form of what is in the heavens above or on the earth beneath or in the waters under the earth", "'any form' for 'and any form' — one letter, the conjunction dropped, the sense unchanged; the no-image list of 4:16-19 the parameter table (the obey_horeb runner's DATA row by CALL); the images for study credited (Rosh Hashanah 24a-24b)"),
    lr(9, 'VARIANT', 'F2 the_second_word (this runner)', "you shall not bow down to them nor serve them, for I the LORD your God am a jealous God, visiting the iniquity of the fathers upon the sons and upon the third and upon the fourth generation of those who hate me", "'fathers' plene and 'AND upon the third' — a letter and a conjunction; 'the third generation' starred by the parser (not thirty); the visiting's arms DATA (Berakhot 7a; Makkot 24a:30 — revoked by Ezekiel); the bower's death by 17:5's juxtaposition (Sanhedrin 60b:11), the prohibition's seat 34:14 (60b:12)"),
    lr(10, 'VARIANT', 'F2 the_second_word (this runner)', "and doing mercy to thousands of those who love me and keep his commandments", "THE KETIV — the written 'his commandments' where Exodus writes 'my' (the DB's one written-and-read token of the chapter; the store's seventh token the read 'my'): a DATA note, no line moves; 'to thousands' a bare plural, no number"),
    lr(11, 'VERBATIM', 'decalogue.vain_name', "you shall not take the name of the LORD your God in vain, for the LORD will not hold guiltless him who takes his name in vain", "seventeen words the same: decalogue.vain_name by CALL — the vain oath and the broken future oath lashed, 'vain and false SPOKEN AS ONE UTTERANCE, like remember and observe' the cell's own ask (Shevuot 20b:9); Mishnah Shevuot 3:8-9 the answer sheet"),
    lr(12, 'EXPANDED', 'decalogue.sabbath_clauses', "KEEP the sabbath day to sanctify it, AS THE LORD YOUR GOD COMMANDED YOU", "'keep' for 'remember' (the infinitive absolute in both copies) and THE RECEIPT INSIDE THE CODE added — nine words for five: KEEP AND REMEMBER IN ONE UTTERANCE (Shevuot 20b:9; Rosh Hashanah 27a:2, 27a:6; Berakhot 20b:10 — women obligated in kiddush; the Sifrei 233:1 the reading's exhibit); the receipt a RUN CITATION of the giving — the register seat CHAPTER; the teacher's referent Marah (Sanhedrin 56b:16; Shabbat 87b:1); decalogue.sabbath_clauses('remember') by CALL"),
    lr(13, 'VERBATIM', 'decalogue.sabbath_clauses', "six days you shall labor and do all your work", "six words the same; [6] the parser's number at both copies; decalogue.sabbath_clauses the cell (20:8-10's span)"),
    lr(14, 'EXPANDED', 'decalogue.sabbath_clauses', "but the seventh day is a sabbath to the LORD your God: you shall not do any work — you, your son, your daughter, AND your servant, your maidservant, YOUR OX AND YOUR ASS AND ALL your cattle, your stranger within your gates — THAT YOUR SERVANT AND YOUR MAIDSERVANT MAY REST LIKE YOU", "twenty-six words for eighteen — 'and your servant', 'your ox and your ass and all your cattle', 'that your servant and your maidservant may rest like you': THE OX AND THE ASS EVERY ANIMAL (Bava Kamma 54b:13 — R. Yosei in R. Yishmael's name reads the expansion itself), the rest 'like you' the analogy's limit (54b:28), the circumcised slave and the righteous convert (Yevamot 48b:5-6); decalogue.sabbath_clauses('labor_scope', 'laden_beast') by CALL"),
    lr(15, 'TURNED', 'decalogue.sabbath_clauses', "and you shall remember that you were a slave in the land of Egypt, and the LORD your God brought you out from there with a mighty hand and an outstretched arm; therefore the LORD your God commanded you to do the sabbath day", "THE GROUND TURNED WHOLE — the exodus for the creation (twenty-three words for twenty-six; 'the sabbath day' the one shared run): the fourth word's TWO GROUNDS a DATA row (the creation of 20:11 the pre-Sinai runner's by CALL; 'remember that you were a slave' five seats, all this book's); decalogue.sabbath_clauses the cell"),
    lr(16, 'EXPANDED', 'holiness.frame', "honor your father and your mother, AS THE LORD YOUR GOD COMMANDED YOU, that your days may be long AND THAT IT MAY GO WELL WITH YOU on the ground which the LORD your God gives you", "twenty-two words for fifteen — the receipt and 'that it may go well with you' added, 'be long' a longer form: NO CELL AT THE DECALOGUE'S SEAT — the fifth word compiled at its kin's, Leviticus 19:3 (holiness.frame by CALL — the honor and the fear defined, the order, the three partners, the woman: Kiddushin 30b-31b); THE EXPANSION'S OWN ROW (Bava Kamma 55a:1 — 'good' not in the first tablets; Kiddushin 39b-40a; Chullin 142a); the sanctions' seats mishpatim_3.parent_striker and parent_curser, sanctions.curser by CALL; the receipt CHAPTER (Marah — Sanhedrin 56b:16)"),
    lr(17, 'VERBATIM', 'mishpatim_3.killer', "you shall not murder", "two words the same: the sixth word's code at Exodus 21:12-14 (mishpatim_3.killer by CALL — the sword) and Numbers 35 (refuge.the_murderer by CALL); the context of the eighth word's reading (Sanhedrin 86a:16)"),
    lr(18, 'VARIANT', 'sanctions.adultery', "and you shall not commit adultery", "'and not' for 'not' — the conjunction; the seventh word's code at Leviticus 20:10 (sanctions.adultery by CALL — strangling, both)"),
    lr(19, 'VARIANT', 'decalogue.theft_commandment', "and you shall not steal", "the conjunction; THE THEFT OF PERSONS by the context (Sanhedrin 86a:15-17 — the decalogue runner's own move): decalogue.theft_commandment('kidnapper') by CALL; Leviticus 19:11's of property by its context"),
    lr(20, 'TURNED', 'ordinances.courts', "and you shall not answer against your neighbor a VAIN witness", "'vain' for 'false' and the conjunction — the ninth word's parameter a DATA row (Onkelos 'false' at both copies): NO CELL AT THE DECALOGUE'S SEAT — the kin at Exodus 23:1 (ordinances.courts('false_report', 'witness_of_violence') by CALL); the conspiring witnesses Deuteronomy 19:16-21 forward"),
    lr(21, 'TURNED', 'F5 the_tenth_word (this runner)', "and you shall not covet your neighbor's wife; and you shall not DESIRE your neighbor's house, HIS FIELD, or his servant or his maidservant, his ox or his ass, or anything that is your neighbor's", "THE WIFE FIRST (the house first in Exodus), DESIRE for the second 'covet', 'his field' added, 'and his ox' — sixteen words for fifteen: NO CELL in any runner until this one — compiled here (Bava Metzia 5b:19-20 the coveter who pays); the block coveting_barred written at the giving's line"),
    rb('Deut 5:1-5, 32-33', "and Moses called all Israel and said to them: hear, O Israel, the statutes and the judgments which I speak in your ears this day; learn them, and keep to do them; the LORD our God made a covenant with us in Horeb — not with our fathers, but with us, we who are all here alive this day; face in face the LORD spoke with you in the mountain out of the midst of the fire, I standing between the LORD and you at that time … and you shall observe to do as the LORD your God commanded you; you shall not turn aside right or left", 'speech_opened', 'Deut 1:1', "torah_expounded on israel_people at (40, 11, 1) — the book's one act of its own day", 'EXPANDED', "THE FRAME'S SECOND SEAT AGAIN (R6): the second speech's opening and its charge — NO WRITE; 5:1 against 4:1 (twenty-two tokens for twenty-four, three shared — computed); 5:2-3 the covenant against the tape's covenant_offered (Exod 19:5-6), people_answered (19:8, 24:3, 24:7) and covenant_blood_thrown (24:8) — 'not with our fathers' against 29:13-14 a DATA note; 5:4 'face IN face' the Bible's one seat (Onkelos 'speech with speech' — ER.presence by CALL); the covenants counted forty-eight per mitzva times the guarantors (Sotah 37b); 5:32-33 the charge NO WRITE, the receipt CHAPTER"),
    rb('Deut 5:22', "these words the LORD spoke to all your assembly in the mountain out of the midst of the fire, the cloud and the thick darkness, with a great voice, and he added no more; and he wrote them on two tablets of stone and gave them to me", 'ten_words_declared', 'Deut 4:10', "covenant_declared on israel_people dated (1, 3, 7) and tablets_delivered on moses dated (1, 4, 17) — 2b's two SUPPLIED lines, FOUND (no second write)", 'EXPANDED', "twenty-four tokens for 4:13's fifteen, three shared ('and he wrote them on two' — computed); Exodus 20:1's seven and 31:18's sixteen the first tellings; 'to all your assembly' the Bible's one seat; 'ADDED NO MORE' a DATA note with Onkelos 'did not cease' (Sanhedrin 17a:12 — Eldad and Medad; Sotah 10b:12 — Judah); the tablets defective here, plene at 4:13; OH.horeb_retold by CALL"),
    rb('Deut 5:23-27', "and it came to pass, when you heard the voice out of the midst of the darkness, while the mountain burned with fire, that you came near to me, all the heads of your tribes and your elders, and you said: … go you near and hear all that the LORD our God shall say, and you speak to us all that the LORD our God speaks to you, and we will hear and do", 'mediator_requested', 'Deut 5:23', "torah_through_moses on israel_people dated (1, 3, 7) — THE SUPPLIED LINE (Exodus 20:18-19 the first telling, no line on the tape)", 'SUPPLIED', "THE TAPE'S SECOND HOLE: Exodus 20:18-19's 'and all the people saw the thunders … speak you with us and we will hear' has no line on the tape (20:18 sits in no runner's span; 20:19-21 are the ordinances' law cells): written ONCE at its own time, dated (1, 3, 7) by the retrograde marker at Deut 5:23 (the ink's own 'when you heard the voice'); ninety-one tokens for 20:18's eighteen and 20:19's thirteen; 'you came near to me' 1:22's phrase (the mob there, the heads and elders here — the Sifrei 20:1; OS by CALL); the first two words from the Almighty's mouth, the rest through Moses (Makkot 24a:1); 5:5 'I stood between' folded here"),
    rb('Deut 5:27', "go you near and hear all that the LORD our God shall say, and you speak to us all that the LORD our God speaks to you, AND WE WILL HEAR AND DO", 'people_answered', 'Exod 24:7', "people_answered at Exod 24:7 — 'the book of the covenant read: we will do and we will hear' (the erection's W7 line)", 'TURNED', "THE ORDER TURNED: 'we will hear and do' against 24:7's 'we will do and hear' (twenty-one tokens against thirteen, two shared — computed; 'we will do' at 19:8, 24:3, 24:7 by ES.sinai('we_will_do_seats')); R. Simai's two crowns for 'we will do' before 'we will hear' (Shabbat 88a:7), the angels' secret (88a:8), the heretic's 'impulsive nation' (88a:9); Onkelos 'we will accept and do'"),
    rb('Deut 5:28-31', "and the LORD heard the voice of your words when you spoke to me; and the LORD said to me: … they have done well in all that they have spoken; who would give that they had such a heart … go say to them: return to your tents; but as for you, stand here with me, and I will speak to you all the commandment and the statutes and the judgments which you shall teach them", 'stand_here_commanded', 'Deut 5:28', "commanded on moses valued teach_the_commandment — written and CLOSED inside the daemon by the prior run (the closer Deut 1:1-5); returned_to_tents on israel_people dated (1, 3, 7) — THE SUPPLIED LINE (told only here; 18:16-17 forward)", 'SUPPLIED', "TOLD ONLY IN THE RETELLING (Exodus 20:22's answer another speech; 18:17's 'they have well said' cites this verdict forward — six tokens, three shared, computed): written ONCE at its own time inside the retrograde stretch of 5:23; 'the LORD heard the voice of your words' 1:34's five words (OS by CALL); THE CHARGE TO TEACH a DEBIT on Moses CLOSED AT ONCE BY THE PRIOR RUN — the book's expounding at 1:5 and 4:5's receipt the run (Exodus 24:12's 'to teach them' — ER.ascent by CALL); 'return to your tents' the separation of 19:15 released (Beitzah 5a-b; Shabbat 87a; Yevamot 62a); 'stand here with me' the Torah received standing (Megillah 21a; the Sifrei 357:40)"),
]
RB_GRADES = collections.Counter(r['grade'] for r in READBACK)
assert len(READBACK) == 21 and RB_GRADES == collections.Counter({'VERBATIM': 5, 'VARIANT': 5, 'EXPANDED': 5, 'TURNED': 4, 'SUPPLIED': 2}) and not any(r['open'] for r in READBACK), (len(READBACK), RB_GRADES)
assert sum(1 for r in READBACK if r['law']) == 16 and [r['verses'] for r in READBACK if r['law'] and r['cell'] == 'NO CELL'] == ['Deut 5:6'] and sum(1 for r in READBACK if r['law'] and r['cell'] != 'NO CELL') == 15

DATA = {
    'the_readback': {'value': READBACK, 'settings': {'the_first_form_on_law': "THE_LOOP.md step 6's laws' half (the owner's 'go', 2026-09-16): a word of the code retold is a REFERENCE ROW graded against the runner's cell that compiles it — VERBATIM / VARIANT / EXPANDED / TURNED — and names its cell or NO CELL; TWENTY-ONE rows: sixteen law rows (VERBATIM 5, VARIANT 5, EXPANDED 3, TURNED 3) and five narrative rows (EXPANDED 2, SUPPLIED 2, TURNED 1); the deltas recomputed from the DB; THE CODE'S HOLE (the second and the tenth words) filled here; THE TAPE'S SECOND HOLE (Exodus 20:18-21) written once at its own time", 'the_ten_as_a_unit': "the ten words a unit on the shelf — read daily by the priests in the Temple, sought outside and ABOLISHED for the heretics' grievance (Berakhot 12a:4-8); the nations conceded the first two words when the fifth was said ('the words of Your mouth', Kiddushin 31a:6-7): the schema question's second exhibit", 'the_third_telling': "R. Akiva — the generals and the details said at Sinai, repeated at the Tent, and REITERATED A THIRD TIME by Moses in the plains of Moab; R. Yishmael — the generals at Sinai only (Sotah 37b:3; Tosefta Sotah 8:11): the second copy's own status on the shelf — the readback's teacher", 'the_second_numbering': "the shelf's English cites chapter 5 by TWO numberings (the export's and one a verse lower around the short words): every docket verdict names the DB verse by the row's quoted words"}},
    'the_second_word': {'value': {'prohibitions': ['no other gods before me', 'no graven image nor any form', 'not bow down to them', 'not serve them'], 'liable_to_death': ['worship in its way', 'slaughter', 'incense', 'libation', 'bowing'], 'a_prohibition_without_death': ['hug', 'kiss', 'sweep', 'sprinkle', 'wash', 'anoint', 'dress', 'shoe', 'a vow or oath by its name'], 'mode': 'stoning', 'sanction_seat': 'Deut 17:2-7 (forward; a REFERENCE the ink makes — by juxtaposition, Sanhedrin 60b:11)'}, 'settings': {'the_answer_sheet': "Mishnah Sanhedrin 7:6 with Sanhedrin 60b:1-19 — the idolater stoned for worship in its way and for the Temple's four rites even not in its way (slaughter, incense, libation, bowing — 'except to the LORD alone', Exodus 22:19 emptied the rites to the Name; R. Yirmeya, 60b:5); the hugger and the kisser a prohibition without death (60b:2, 60b:13); Peor's exposure and Markulis's stone their own service (60b:3)", 'the_bowers_death': "by the juxtaposition of 'and bowed to them' (Deut 17:3) to 'you shall stone them' (17:5) — Sanhedrin 60b:11; the PROHIBITION of bowing from 'you shall bow to no other god' (Exodus 34:14 — 60b:12), not from the second word's 'to them' (said of the images)", 'the_disputed_arm': "Rava bar Rav Chanan: any HONORABLE service capital, not the Temple's rites only (60b:18)", 'the_first_two_words': "'I am' and 'you shall have no other gods' heard from the Almighty's mouth — 611 and 2 (Makkot 24a:1)", 'onkelos': "'another god EXCEPT ME' (5:7); 'rebellious children … when the children complete to sin after their fathers' the translation's supplied condition at 5:9"}},
    'the_visiting': {'value': {'generations': 'the third and the fourth of those who hate me', 'mercy': 'thousands of those who love me', 'ketiv': "his commandments (written) / my commandments (read; Exodus 20:6's word)"}, 'settings': {'berakhot_7a': "'visiting the iniquity of the fathers upon the sons' against 'the sons shall not die for the fathers' (24:16) — when they hold their fathers' deeds in their hands (Berakhot 7a:27, credited from the Decalogue's block)", 'makkot_24a': "Moses' decree 'he visits the transgression of the fathers upon the sons' (Exodus 34:7) REVOKED by Ezekiel — 'the soul that sins, it shall die' (18:4) (Makkot 24a:30)", 'the_parser': "'the third generation' STARRED — not thirty (rule 15); 'to thousands' a bare plural; the lemma's five seats (Genesis 50:23 the first)", 'the_ketiv': "the DB's one x-ketiv token of the chapter (5:10); the store carries both glosses; no line moves"}},
    'the_no_image_list': {'value': OH.DATA['the_no_image_list']['value'], 'settings': {'by_call': "the obey_horeb runner's DATA row — 4:16-19's forms restating Exodus 20:4's 'any likeness' in seven kinds and the host: the second word's parameter table; the images for study (Mishnah Rosh Hashanah 2:8; Rosh Hashanah 24a-24b) and the statues (Mishnah Avodah Zarah 3:1-3) credited from 2b's docket"}},
    'the_tenth_word': {'value': {'verbs': ['covet (the wife)', 'desire (the house, the field, the servants, the beasts, all)'], 'order': "the wife first here, the house first in Exodus", 'added': 'his field', 'the_coveter_who_pays': 'transgresses — taking by force or deceit even with payment (Rav Acha of Difti); most people read it as taking without payment, so the bailee who pays is not disqualified (Bava Metzia 5b:19-20)'}, 'settings': {'the_mekhilta': "covet in deed, desire in the heart — the Mekhilta d'Rabbi Yishmael Bahodesh 8 (the first copy's spine, named, unopened)", 'onkelos': "'AND DO NOT DESIRE' (5:21)", 'the_root': "the desire-root's twenty-five seats (Numbers 11:4, 34 the craving); 'covet' 2ms four seats"}},
    'the_sabbath_grounds': {'value': {'exodus_20_11': 'the creation — six days he made the heavens and the earth, rested the seventh', 'deut_5_15': 'the exodus — you were a slave in Egypt and the LORD brought you out'}, 'settings': {'by_call': "the creation ground the pre-Sinai runner's (PS.sabbath('delta_20_11') — Genesis 2:2-3 against Exodus 20:11 by token); 'remember that you were a slave' five seats, all this book's (15:15, 16:12, 24:18, 24:22); the readback row 5:15 TURNED"}},
    'the_ninth_word': {'value': {'exodus_20_16': 'a false witness', 'deut_5_20': 'a vain witness', 'onkelos': 'false at both'}, 'settings': {'the_kin': "Exodus 23:1's 'you shall not take up a false report … a witness of violence' (ordinances.courts by CALL); the conspiring witnesses Deuteronomy 19:16-21 forward; 'vain' four Torah seats (5:11, 5:20, Exodus 20:7, 23:1); the witnesses to half a matter (Sanhedrin 86a:18-19)"}},
    'keep_and_remember': {'value': 'one_utterance', 'settings': {'shevuot_20b': "'remember' and 'keep' spoken in one utterance — what the mouth cannot say nor the ear hear; the vain and the false oath 'one' by the same rule (20b:9 — the decalogue runner's ask vain_and_false_utterance)", 'rosh_hashanah_27a': "two sounds from ONE source cannot be discerned — Sinai's miracle (27a:2, 27a:6)", 'berakhot_20b': "whoever is in 'keep' is in 'remember' — women obligated in kiddush by the Torah (Rava, 20b:10)", 'shabbat_33b': "the two bundles of myrtle (33b:8)", 'the_sifrei': "233:1 on 22:11-12 with 5:12 and Exodus 20:8 — the reading's exhibit (the schema question)"}},
    'the_reward_clause': {'value': {'deut_5_16': 'that your days may be long AND THAT IT MAY GO WELL WITH YOU', 'exodus_20_12': 'that your days may be long'}, 'settings': {'bava_kamma_55a': "why 'good' here and not in the first tablets? R. Chiya bar Abba sends to R. Tanchum bar Chanilai (55a:1; the answer in the following segment, named: the first tablets were to be broken)", 'the_court': "a positive mitzva whose reward is stated beside it — the court below not warned to enforce it (Chullin 110b:3)", 'the_world': "the reward after the resurrection (R. Yaakov — Chullin 142a:3; Kiddushin 39b:7) or in this world (Rava — Kiddushin 40a:5): the arms"}},
    'the_honor_by_call': {'value': {'honor': HO.frame('honor_defined')['v'], 'fear': HO.frame('fear_defined')['v'], 'order': HO.frame('parents_order')['v'], 'partners': HO.frame('three_partners')['v'], 'woman': HO.frame('woman_included')['v']}, 'settings': {'kiddushin_30b_31b': "what is fear and what is honor (31b:14); the three equations — honor with wealth, fear with fear, cursing with cursing, striking not equated (30b:18-20); the three partners (30b:21); the father first in 'honor', the mother first in 'fear' (30b:22-31a:1); the woman under her husband, divorced equal (30b:16-17); the father first when both ask (31a:4-5); how far — Dama ben Netina (31a:8-13); the manner — pheasant and the millstone (31a:14); in life and in death (31b:10-13)", 'the_sanctions': "the striker (Exodus 21:15) strangled, the curser (21:17; Leviticus 20:9) stoned — mishpatim_3 and sanctions by CALL"}},
    'the_receipts': {'value': {'Deut 5:12': 'CHAPTER', 'Deut 5:16': 'CHAPTER', 'Deut 5:32': 'CHAPTER'}, 'settings': {'the_ink': "'as the LORD your God commanded you' INSIDE the ten words (5:12, 5:16; 20:17 the third seat) and the plural at 5:32 — a law citing its prior giving: RUN CITATIONS of the tape's ten_words_declared (Exodus 20:8, 20:12, 20:1-17 the first tellings); no ledger write pays a receipt (R5)", 'the_teacher': "Rav Yehuda — commanded AT MARAH (Exodus 15:25: the Sabbath and honoring parents among Marah's statutes — Sanhedrin 56b:16; Shabbat 87b:1; ES.marah('statute_list') by CALL): the pointers name both referents", 'the_gate': "the class from the gate's own code: no write's source contains the verses (the second copy is no line), the chapter holds a closed entry (the charge to teach, closed inside the daemon) — CHAPTER"}},
    'the_two_copies': {'value': {'exodus_20_2_17': COPIES[0], 'deut_5_6_21': COPIES[1], 'per_word': WORD_TOK}, 'settings': {'computed': "tokens and letters (consonants, no maqaf) recomputed from the DB; the per-verse tokens (DB verse, Exodus verse, Exodus tokens, Deuteronomy tokens)"}},
    'the_second_hole': {'value': {'exod_20_18': 'in no runner\'s span', 'exod_20_19_21': "the ordinances' law cells, no narrative line", 'the_tape': 'runs from Exod 19:20 to 24:1'}, 'settings': {'the_answer': "R3's form — the request written ONCE at its own time from the retelling's seat (mediator_requested, dated (1, 3, 7) by the retrograde marker at 5:23); the answer told only here (stand_here_commanded, the same day); a forward marker at 5:32 ends the stretch"}},
    'the_export_division': {'value': {'export': 30, 'db': 33, 'the_map': '1-16 = 1-16; 17 = 17-20; 18 = 21; 19-30 = 22-33'}, 'settings': {'the_citations': "the shelf's English cites the chapter by two numberings — Sanhedrin 17a:12 cites 5:19 and Sotah 10b:12 cites 5:18 for one verse (the DB's 22); the quoted words fix the verse"}},
    'the_mediator': {'value': {'deut_5_5': 'I stood between the LORD and you', 'deut_5_27': 'you speak to us … and we will hear and do', 'deut_5_31': 'stand here with me and I will speak to you all the commandment'}, 'settings': {'makkot_24a': "'I am' and 'you shall have no other gods' from the Almighty's mouth; 611 through Moses (24a:1)", 'avot_1_1': "'Moses received the Torah from Sinai and handed it on' — the vocabulary of the status torah_through_moses", 'onkelos': "'between the MEMRA of the LORD and you' (5:5)", 'moses_separation': "Moses separated from his wife by an a fortiori, and God agreed — 'and you, stand here with me' (Shabbat 87a:4; Yevamot 62a:2)"}},
    'the_return_to_tents': {'value': 'the_separation_of_exodus_19_15_released', 'settings': {'beitzah_5a': "a matter forbidden by a count needs a count to permit — Rav Yosef from 'return to your tents' after 'do not come near a woman' (5a:7, 5b:3)", 'his_tent': "'his tent' is his wife (Moed Katan 7b:5, 15b:13)", 'procreation': "repeated at Sinai — Israel's by the framework (Sanhedrin 59b:3-4; PS.noahide by CALL)"}},
    'the_charge_to_teach': {'value': {'debit': 'teach_the_commandment', 'on': 'moses', 'closed_by': 'Deut 1:5 — the prior run (the book itself)'}, 'settings': {'the_ink': "'stand here with me and I will speak to you all the commandment and the statutes and the judgments WHICH YOU SHALL TEACH THEM' (5:31); Exodus 24:12's 'to teach them' (ER.ascent('torah_mitzvah') by CALL); 4:14 'the LORD commanded me at that time to teach you'; 4:5 'I have taught you … as the LORD my God commanded me' (the register seat ACT since 2b)", 'the_form': "THE CLOSE BY A PRIOR RUN (R3) — the opening speech's _closed_by_prior_run: the debit written and closed inside the daemon with the tape's EARLIER line as the closer (speech_opened at Deut 1:1-5, 'Moses undertook to expound this Torah')"}},
    'the_face_in_face': {'value': {'deut_5_4': 'face IN face (the one seat)', 'the_other_form': 'face TO face (five seats — Jacob, Moses at the tent 33:11, 34:10, Gideon, Ezekiel)'}, 'settings': {'onkelos': "'speech with speech' — as at Exodus 33:11 (ER.presence('speech_with_speech') by CALL)", 'yoma_4b': "'He called to Moses' — Moses and all Israel standing and listening: all Israel heard the voice at Horeb; at the Tent Moses alone (Numbers 7:89) (4b:7-8)", 'the_day': "the sixth or the seventh of Sivan (Yoma 4b:3; Shabbat 88a:2-3) — the sinai_days row's two settings, Rabbi Yose's the running one"}},
    'the_fathers_and_us': {'value': {'deut_5_3': 'not with our fathers did the LORD make this covenant, but with us, we who are all here alive this day', 'deut_29_13_14': 'not with you alone … but with him who stands here with us this day and with him who is not here'}, 'settings': {'computed': "5:3 against 29:13 (sixteen tokens for eleven, three shared); 'our fathers' six Torah seats; 'this covenant' three; a DATA note — no teacher joins them here (the Sifrei silent); the guarantors — every one of Israel a guarantor for the rest, 603,550 covenants (Sotah 37b:5-6)"}},
    'the_hear_and_do': {'value': {'deut_5_27': 'we will hear and do', 'exodus_24_7': 'we will do and hear', 'exodus_19_8_24_3': 'all that the LORD has spoken we will do'}, 'settings': {'shabbat_88a': "R. Simai — 'we will do' before 'we will hear': two crowns on each, removed at the calf (88a:7); the angels' secret (88a:8); the heretic to Rava (88a:9); the mountain overturned like a tub and the caveat (88a:5 — ES.sinai('tub') by CALL)", 'onkelos': "'we will ACCEPT and do' (5:27)"}},
}
assert len(DATA) == 20, len(DATA)

# ===== F1: THE ASSEMBLY CALLED — the frame's second seat (Deut 5:1-5) ====================================
def the_assembly_called(case, data):
    del P_[:]
    ask = case['ask']
    if ask == 'hear_learn_keep_do':
        ink('5:1', '"and Moses called all Israel and said to them: hear, O Israel, the statutes and the judgments which I speak in your ears this day; learn them, and keep to do them" — "and Moses called all Israel" %s (the book\'s two convocations); "hear, O Israel" %s; "in your ears" %s the Torah\'s one seat; "keep to do them" one seat; "hear" the imperative %s' % (P('ויקרא', 'משה', 'אל', 'כל', 'ישראל'), P('שמע', 'ישראל'), U('באזניכם'), IMPER[1]))
        move('Yevamot 109b:5', "Rav Pappa — 'that you may learn them and keep to do them': whoever is engaged in doing is engaged in learning; not doing, not even Torah")
        dat('the row the_readback: 5:1-5 with 5:32-33 EXPANDED against speech_opened (Deut 1:1) — NO WRITE (R6)')
        return out("hear, learn, keep, do (5:1) — the second speech opened: Moses' call to all Israel, the four verbs in order; the frame's second seat, no write", ['accepted'])
    if ask == 'the_covenant_at_horeb':
        ink('5:2', '"the LORD our God made a covenant with us in Horeb" — "made a covenant with us" %s the one seat; Horeb the name (lemma %s)' % (P('כרת', 'עמנו', 'ברית'), lemma_of('Deut', 5, 2, 'בחרב')))
        move('Sotah 37b:1-6', "the covenants counted — four general and four specific, with blessings and curses sixteen, at Sinai, the Tent and Moab: forty-eight per mitzva, times 603,550 guarantors (R. Shimon ben Yehuda of Kefar Akko)")
        move('Sotah 37b:3', "R. Akiva — the generals and the details said at Sinai, repeated at the Tent, reiterated a third time at Moab; R. Yishmael — the generals at Sinai only: the second copy's own status")
        dat("the tape's covenant: covenant_offered (Exod 19:5-6), people_answered (19:8, 24:3, 24:7), covenant_blood_thrown (24:8) — the book of the covenant %d seats, 'one voice' %d (ER by CALL)" % (ER_BOOK['v'], ER_VOICE1['v']))
        return out("the covenant at Horeb (5:2) — the tape's covenant READ BACK: the book and the blood (ER by CALL); forty-eight covenants per mitzva (Sotah 37b); the second copy a third saying (R. Akiva)", ['accepted'])
    if ask == 'not_with_our_fathers':
        ink('5:3', '"not with our fathers did the LORD make this covenant, but with us, we who are all here alive this day" — "not with our fathers" %s; "this covenant" %s in the Torah; "all of us alive" %s; against 29:13-14 (the diff computed: %s tokens for %s, %s shared)' % (P('לא', 'את', 'אבתינו'), P('הברית', 'הזאת', books=T), P('כלנו', 'חיים'), FRAME_DIFF[3], FRAME_DIFF[4], FRAME_DIFF[5]))
        dat('the row the_fathers_and_us: a DATA note — no teacher joins 5:3 to 29:13-14 here; the guarantors (Sotah 37b:5)')
        return out("not with our fathers (5:3) — the covenant with the living here: a DATA note against 29:13-14, no link of our own", ['accepted'])
    if ask == 'face_in_face':
        ink('5:4', '"face in face the LORD spoke with you in the mountain out of the midst of the fire" — "face IN face" %s THE BIBLE\'S ONE SEAT; "face to face" %s; "in the mountain from the midst of the fire" %s' % (P('פנים', 'בפנים'), P('פנים', 'אל', 'פנים'), P('בהר', 'מתוך', 'האש')))
        move('Onkelos Deut 5:4 (ER.presence by CALL)', "'speech with speech' — the rendering of Exodus 33:11's 'face to face' (%s)" % ER_SPEECH['v'])
        move('Yoma 4b:7-8', "R. Elazar — 'He called to Moses': Moses and all Israel standing and listening; all Israel heard the voice at Horeb, at the Tent Moses alone (Numbers 7:89)")
        return out("face in face (5:4) — the one seat of the form; Onkelos 'speech with speech' (ER by CALL); all Israel heard the voice (Yoma 4b)", ['accepted'])
    if ask == 'i_stood_between':
        ink('5:5', '"I stood between the LORD and you at that time to declare to you the word of the LORD, for you were afraid of the fire and did not go up the mountain, saying" — "I stood between" %s; "stood between" %s; "at that time" fifteen seats in the book; "saying" the chapter\'s one seat; the Memra between (Onkelos)' % (P('אנכי', 'עמד', 'בין'), P('עמד', 'בין')))
        move('Makkot 24a:1', "'I am' and 'you shall have no other gods' heard from the Almighty's mouth; the rest through Moses — the mediator's row")
        dat('the row the_mediator: 5:5 folded into the request\'s SUPPLIED row (5:23-27); Exodus 20:21 "Moses drew near to the thick darkness" the first telling of the standing between')
        return out("I stood between (5:5) — the mediator: the first two words direct, the rest through Moses (Makkot 24a); the request's row", ['accepted'])
    return out('no verdict in span', [FX.NONE])


# ===== F2: THE SECOND WORD — compiled here from both copies (Deut 5:7-10; Exodus 20:3-6) ===================
def the_second_word(case, data):
    del P_[:]
    ask = case['ask']
    if ask == 'no_other_gods':
        ink('5:7', '"you shall have no other gods before me" — %s the two copies verbatim; "other gods" %d Torah seats, %d this book\'s; Onkelos "another god EXCEPT ME"' % (P('אלהים', 'אחרים', 'על', 'פני'), len(P('אלהים', 'אחרים', books=T)), len(P('אלהים', 'אחרים', books=('Deut',)))))
        move('Makkot 24a:1', "the second of the two words heard from the Almighty's mouth — 611 and 2")
        move('Sanhedrin 60b:12', "the PROHIBITION of bowing from 'you shall bow to no other god' (Exodus 34:14) — the second word's 'to them' said of the images")
        dat('the row the_second_word: NO CELL in any runner until this one — the code\'s hole filled from the retelling\'s seat')
        return out("no other gods before me (5:7) — the second word's head, compiled here: the block other_gods_barred on Israel at the giving's line", ['accepted'])
    if ask == 'no_image':
        ink('5:8', '"you shall not make for yourself a graven image, any form of what is in the heavens above or on the earth beneath or in the waters under the earth" — "any form" for Exodus\'s "and any form" (%s / %s); "a graven image" %d Torah seats; "in the waters under the earth" %s' % (P('פסל', 'כל', 'תמונה'), P('פסל', 'וכל', 'תמונה'), len(U('פסל', 'ופסל', books=T)), P('במים', 'מתחת', 'לארץ')))
        dat("the row the_no_image_list (OH by CALL): %d kinds — 4:16-19's parameter table; the images for study (Rosh Hashanah 24a-24b) and the statues (Mishnah Avodah Zarah 3:1-3) credited" % len(data['the_no_image_list']['value']))
        return out("no image (5:8) — the making barred; the no-image list of 4:16-19 the parameter table (OH by CALL); the images for study credited", ['accepted'])
    if ask == 'bow_and_serve':
        ink('5:9', '"you shall not bow down to them nor serve them" — %s the two copies; the prohibitions %s; "a jealous God" %s' % (P('לא', 'תשתחוה', 'להם', 'ולא', 'תעבדם'), PROHIB[9], P('אל', 'קנא')))
        move('Mishnah Sanhedrin 7:6; Sanhedrin 60b:1, 60b:5', "the idolater STONED — the worshipper in its way, the slaughterer, the incense-burner, the libation-pourer, the BOWER (even not in its way — the Temple's rites emptied to the Name, 'except to the LORD alone', Exodus 22:19: 60b:8-9), the one who accepts it as a god, 'you are my god'")
        move('Sanhedrin 60b:11', "the bower's death by the juxtaposition of 'and bowed to them' (Deut 17:3) to 'you shall stone them' (17:5) — the mode STONING, 17:2-7's procedure chapter 17's sitting")
        move('Sanhedrin 60b:18', "Rava bar Rav Chanan — any honorable service capital? the disputed arm (DATA)")
        return out("bow and serve (5:9) — the bower stoned: the second word's answer sheet (Mishnah Sanhedrin 7:6; the four services, Sanhedrin 60b); the mode by 17:5's juxtaposition", ['put_to_death'])
    if ask == 'in_its_way':
        ink('5:9', '"nor serve them" — the service in its own manner: Peor\'s exposure and Markulis\'s stone (the balak runner\'s Peor the kin)')
        move('Mishnah Sanhedrin 7:6; Sanhedrin 60b:3, 60b:5', "one who defecates before Peor or throws a stone at Markulis is liable — that is its worship (R. Yirmeya: worship in its typical manner liable)")
        return out("in its way (5:9) — Peor's exposure, Markulis's stone: liable, the idol's own service (Mishnah Sanhedrin 7:6)", ['put_to_death'])
    if ask == 'the_embracer':
        ink('5:9', '"you shall not bow down to them nor serve them" — the acts below service')
        move('Mishnah Sanhedrin 7:6; Sanhedrin 60b:2, 60b:13', "the hugger, the kisser, the sweeper, the sprinkler, the washer, the anointer, the dresser, the shoer — a PROHIBITION, not liable to death (excluded by 'he who sacrifices'); the vow and the oath by its name a prohibition")
        return out("the embracer (5:9) — a prohibition without death: the hugger, the kisser, the dresser exempt from the sanction (Mishnah Sanhedrin 7:6)", ['exempt'])
    if ask == 'the_visiting':
        ink('5:9-10', '"visiting the iniquity of the fathers upon the sons and upon the third and upon the fourth generation of those who hate me, and doing mercy to thousands of those who love me and keep his commandments" — "visiting the iniquity of fathers upon sons" %s (not Exodus 20:5 — its "fathers" defective); the third generation starred (the lemma\'s seats %s); "to thousands" %s' % (P('פקד', 'עון', 'אבות', 'על', 'בנים'), LEMV('8029'), U('לאלפים')))
        move('Berakhot 7a:27 (credited); Makkot 24a:30', "when they hold their fathers' deeds in their hands; Moses' decree revoked by Ezekiel 18:4 — the two arms")
        dat('the row the_visiting: %s' % data['the_visiting']['value'])
        return out("the visiting (5:9-10) — the generations and the thousands a DATA row: when they hold their fathers' deeds (Berakhot 7a); revoked by Ezekiel (Makkot 24a)", ['accepted'])
    if ask == 'the_ketiv':
        ink('5:10', '"keep his commandments" — the written "his" (%s), Exodus 20:6\'s "my" (%s); the DB\'s one written-and-read token of the chapter' % (P('לאהבי', 'ולשמרי', 'מצותו'), P('לאהבי', 'ולשמרי', 'מצותי')))
        dat("the ketiv: wtype x-ketiv at 5:10's last token; the store carries both glosses ('his commandments', 'my commandments'); no line moves")
        return out("the ketiv (5:10) — 'his' written, 'my' read: a DATA note, no line", ['accepted'])
    if ask == 'the_write':
        ink('5:7-10', 'the second word whole — the block written on Israel AT THE GIVING\'S LINE (ten_words_declared, dated (1, 3, 7)), never at the retelling\'s')
        dat("the write: other_gods_barred on israel — law_covenant_at_horeb watches ten_words_declared (2b's supplied line); THE REST's one declared delta")
        return out("the write (5:7-10) — other_gods_barred on Israel: the code's hole filled at the code's own line", ['other_gods_barred'])
    return out('no verdict in span', [FX.NONE])


# ===== F3: THE FIRST TABLET — the words one to four read back (Deut 5:6-15) =============================
def _row(v): return [r for r in READBACK if r['verses'] == 'Deut 5:%d' % v][0]
def the_first_tablet(case, data):
    del P_[:]
    ask = case['ask']
    if ask == 'the_first_word':
        r = _row(6)
        ink('5:6', '"I am the LORD your God, who brought you out of the land of Egypt, out of the house of bondage" — %s VERBATIM (the diff %s); "I am the LORD your God" %s; "house of bondage" twelve seats' % (r['grade'], DIFF(('Deut', 5, 6), ('Exod', 20, 2)) or 'none', P('אנכי', 'יהוה', 'אלהיך')))
        move('Makkot 24a:1', "the first of the six hundred thirteen, from the Almighty's mouth")
        dat('the row: NO CELL — a declaration, not a case')
        return out("the first word (5:6) — VERBATIM; NO CELL: a declaration heard from the Almighty's mouth", ['accepted'])
    if ask == 'the_second_word_row':
        rows = [_row(v) for v in (7, 8, 9, 10)]
        ink('5:7-10', 'the second word\'s four verses — %s; the diffs %s' % ([r['grade'] for r in rows], [DIFF(('Deut', 5, v), ('Exod', 20, v - 4)) for v in (7, 8, 9, 10)]))
        dat("the rows name F2 the_second_word (this runner) — the code's hole filled")
        return out("the second word (5:7-10) — VERBATIM, VARIANT, VARIANT, VARIANT: the cell F2 (compiled here)", ['accepted'])
    if ask == 'the_third_word':
        ink('5:11', '"you shall not take the name of the LORD your God in vain" — VERBATIM (%s); "in vain" %d seats; "will not hold guiltless" %d' % (DIFF(('Deut', 5, 11), ('Exod', 20, 7)) or 'none', len(U('לשוא')), len(P('לא', 'ינקה'))))
        move('decalogue.vain_name by CALL', "the vain oath lashed (%r), the broken future oath lashed, 'vain and false spoken as one — like remember and observe' (%r)" % (DC_VAINOATH[0], DC_VAIN[0]))
        move('Mishnah Shevuot 3:8-9', "the vain oath defined — the known falsehood, the impossible, the oath against a mitzva, the witnesses' oath; the oath against an oath")
        return out("the third word (5:11) — VERBATIM: decalogue.vain_name by CALL (the vain oath lashed; Mishnah Shevuot 3:8-9)", ['accepted'])
    if ask == 'the_fourth_word':
        rows = [_row(v) for v in (12, 13, 14, 15)]
        ink('5:12-15', 'the fourth word\'s four verses — %s; the tokens %s against Exodus 20:8-11\'s %s' % ([r['grade'] for r in rows], [LEN('Deut', 5, v) for v in (12, 13, 14, 15)], [LEN('Exod', 20, v) for v in (8, 9, 10, 11)]))
        move('decalogue.sabbath_clauses by CALL', "remember → %r; labor_scope → %r; laden_beast → %r" % (DC_REM[0], DC_SCOPE[0], DC_LADEN[0]))
        return out("the fourth word (5:12-15) — EXPANDED, VERBATIM, EXPANDED, TURNED: decalogue.sabbath_clauses by CALL", ['accepted'])
    if ask == 'keep_and_remember':
        ink('5:12', '"KEEP the sabbath day to sanctify it" against "REMEMBER the sabbath day to sanctify it" — %s / %s; both the infinitive absolute (%s; Exodus 20:8 %s)' % (P('שמור', 'את', 'יום', 'השבת'), P('זכור', 'את', 'יום', 'השבת'), INFA[12], wm('Exod', 20, 8)[0]))
        move('Shevuot 20b:9; Rosh Hashanah 27a:2, 27a:6', "'remember' and 'keep' spoken in ONE UTTERANCE — what the mouth cannot say nor the ear hear; two sounds from one source")
        move('Berakhot 20b:10', "Rava — whoever is in 'keep' is in 'remember': women obligated in kiddush by the Torah")
        dat('the row keep_and_remember; the Sifrei 233:1 the reading\'s exhibit')
        return out("keep and remember (5:12) — one utterance: the diff's first word the tradition's exhibit; women's kiddush (Berakhot 20b)", ['accepted'])
    if ask == 'the_ox_and_the_ass':
        ink('5:14', '"your ox and your ass and all your cattle" %s the one seat — Exodus 20:10\'s "your cattle"; the diff %s' % (P('ושורך', 'וחמרך', 'וכל', 'בהמתך'), DIFF(('Deut', 5, 14), ('Exod', 20, 10))[1]))
        move('Bava Kamma 54b:13', "R. Yosei in R. Yishmael's name — the ox and the ass specified inside 'all cattle' to teach EVERY ANIMAL wherever 'ox and ass' are written: muzzling (54b:10), diverse kinds (54b:11), unloading (54b:9, 54b:25)")
        move('decalogue.sabbath_clauses by CALL', "the laden beast — %r" % DC_LADEN[0])
        return out("the ox and the ass (5:14) — every animal by the verbal analogy: the expansion read by the tradition itself (Bava Kamma 54b)", ['accepted'])
    if ask == 'the_servants_rest':
        ink('5:14', '"that your servant and your maidservant may rest like you" %s the one seat; "like you" seven Torah seats' % P('למען', 'ינוח', 'עבדך', 'ואמתך'))
        move('Bava Kamma 54b:28', "Rav Acha bar Yaakov — people equated with animals for RESTING only: the analogy's limit")
        move('Yevamot 48b:5-6', "the circumcised slave rests by this clause, the uncircumcised by 23:12's; 'your stranger within your gates' the righteous convert, 23:12's the resident alien")
        return out("the servants' rest (5:14) — the circumcised slave and the righteous convert (Yevamot 48b); the analogy's limit (Bava Kamma 54b)", ['accepted'])
    if ask == 'the_two_grounds':
        ink('5:15', '"remember that you were a slave in Egypt … therefore the LORD your God commanded you to do the sabbath day" — the exodus for the creation; "the sabbath day" the shared run %s; "remember that you were a slave" %s' % (SHARED(('Deut', 5, 15), ('Exod', 20, 11)), P('וזכרת', 'כי', 'עבד', 'היית')))
        move('pre_sinai.sabbath by CALL', "the creation ground of 20:11 against Genesis 2:2-3 by token — %r" % (PS_DELTA['v'],))
        dat('the row the_sabbath_grounds: %s' % data['the_sabbath_grounds']['value'])
        return out("the two grounds (5:15) — the creation (20:11, PS by CALL) and the exodus: a DATA row; the readback row TURNED", ['accepted'])
    if ask == 'the_receipt_5_12':
        ink('5:12', '"AS THE LORD YOUR GOD COMMANDED YOU" — the receipt inside the code %s; the plural 5:32 %s' % (RECEIPT_SG, RECEIPT_PL))
        move('Sanhedrin 56b:16; Shabbat 87b:1 (ES.marah by CALL)', "Rav Yehuda — commanded AT MARAH: %s" % (ES_MARAH['v'],))
        dat("the row the_receipts: RUN CITATION of the giving (the tape's ten_words_declared); the register seat CHAPTER")
        return out("the receipt at 5:12 — a run citation of the giving (the ink) read as Marah (the teacher): the seat CHAPTER", ['accepted'])
    return out('no verdict in span', [FX.NONE])


# ===== F4: THE SECOND TABLET — the words five to ten read back (Deut 5:16-21) ============================
def the_second_tablet(case, data):
    del P_[:]
    ask = case['ask']
    if ask == 'the_fifth_word':
        ink('5:16', '"honor your father and your mother" %s — the infinitive absolute (%s); the diff %s' % (P('כבד', 'את', 'אביך', 'ואת', 'אמך'), INFA[16], DIFF(('Deut', 5, 16), ('Exod', 20, 12))))
        move('holiness.frame by CALL (Kiddushin 30b-31b)', "honor %s; fear %s; the order %r; the partners %s; the woman %r" % (HO_HONOR['v'], HO_FEAR['v'], HO_ORDER['v'], HO_THREE['v'], HO_WOMAN['v']))
        move('mishpatim_3 and sanctions by CALL', "the striker %r, the curser %r (the woman %r)" % (M3_STRIKE['v'], SA_CURSER['v'], M3_CURSE['v']))
        return out("the fifth word (5:16) — EXPANDED: NO CELL at the Decalogue's seat, holiness.frame by CALL (the honor and the fear defined, Kiddushin 31b)", ['accepted'])
    if ask == 'the_sixth_word':
        ink('5:17', '"you shall not murder" %s VERBATIM' % P('לא', 'תרצח'))
        move('mishpatim_3.killer and refuge.the_murderer by CALL', "the mode %r; %r" % (M3_KILL['v'], RF_MURD[0][:40]))
        return out("the sixth word (5:17) — VERBATIM: mishpatim_3.killer and refuge.the_murderer by CALL", ['accepted'])
    if ask == 'the_seventh_word':
        ink('5:18', '"and you shall not commit adultery" — the conjunction; %s' % U('תנאף'))
        move('sanctions.adultery by CALL', "the mode %r; %r" % (SA_ADULT['v'], SA_BOTH['v']))
        return out("the seventh word (5:18) — VARIANT: sanctions.adultery by CALL (Leviticus 20:10)", ['accepted'])
    if ask == 'the_eighth_word':
        ink('5:19', '"and you shall not steal" — the conjunction; %s; Leviticus 19:11\'s plural %s' % (U('תגנב'), P('לא', 'תגנבו')))
        move('decalogue.theft_commandment by CALL', "the kidnapper %r; money theft %r" % (DC_KID[0], DC_MONEY[0]))
        move('Sanhedrin 86a:15-17', "R. Yoshiya from 'you shall not steal' and R. Yochanan from Leviticus 25:42; the theft of PERSONS by the context; 19:11's of property by its context")
        return out("the eighth word (5:19) — VARIANT: the theft of persons by the context (Sanhedrin 86a); decalogue.theft_commandment by CALL", ['accepted'])
    if ask == 'the_ninth_word':
        ink('5:20', '"a VAIN witness" %s against "a FALSE witness" %s; "vain" %s' % (P('עד', 'שוא'), P('עד', 'שקר'), U('שוא', 'לשוא', books=T)))
        move('ordinances.courts by CALL', "the false report %r; the witness of violence %r" % (OR_FALSE['v'], OR_VIOL['v']))
        dat('the row the_ninth_word: %s' % data['the_ninth_word']['value'])
        return out("the ninth word (5:20) — TURNED: vain for false, the parameter a DATA row; ordinances.courts by CALL (23:1)", ['accepted'])
    if ask == 'the_tenth_word_row':
        ink('5:21', 'the tenth word — the diff %s' % DIFF(('Deut', 5, 21), ('Exod', 20, 17)))
        dat("the row names F5 the_tenth_word (this runner) — the code's hole filled")
        return out("the tenth word (5:21) — TURNED: the cell F5 (compiled here)", ['accepted'])
    if ask == 'the_reward_clause':
        ink('5:16', '"that your days may be long AND THAT IT MAY GO WELL WITH YOU" — %s the one seat; "be long" %s / %s' % (P('ולמען', 'ייטב', 'לך'), P('למען', 'יאריכן', 'ימיך'), P('למען', 'יארכון', 'ימיך')))
        move('Bava Kamma 55a:1', "why is 'good' written here and not in the first tablets? — sent to R. Tanchum bar Chanilai (the answer named: the first tablets were to be broken)")
        move('Chullin 110b:3; Chullin 142a:3; Kiddushin 39b:7, 40a:5', "the court not warned to enforce a mitzva whose reward is stated; the reward after the resurrection (R. Yaakov) or in this world (Rava)")
        return out("the reward clause (5:16) — the expansion's own Talmud row: 'good' not in the first tablets (Bava Kamma 55a)", ['accepted'])
    if ask == 'the_receipt_5_16':
        ink('5:16', '"AS THE LORD YOUR GOD COMMANDED YOU" — the second receipt inside the code (%s)' % RECEIPT_SG)
        move('Sanhedrin 56b:16', "honoring parents commanded at Marah (Rav Yehuda) — the teacher's referent; the ink's the giving (20:12)")
        return out("the receipt at 5:16 — a run citation of the giving read as Marah: the seat CHAPTER", ['accepted'])
    if ask == 'the_counts':
        ink('5:6-21', 'the two copies %s (tokens, letters) against %s; per word %s' % (COPIES[1], COPIES[0], WORD_TOK))
        dat('the row the_two_copies — recomputed from the DB')
        return out("the counts (5:6-21) — 189 tokens / 708 letters against 172 / 620: recomputed", ['accepted'])
    return out('no verdict in span', [FX.NONE])


# ===== F5: THE TENTH WORD — compiled here from both copies (Deut 5:21; Exodus 20:17) =======================
def the_tenth_word(case, data):
    del P_[:]
    ask = case['ask']
    if ask == 'covet_and_desire':
        ink('5:21', '"you shall not covet your neighbor\'s wife; you shall not DESIRE your neighbor\'s house" — "covet" %s; "desire" %s the hitpael\'s one seat (the root\'s %d seats)' % (U('תחמד'), U('תתאוה'), len(LEMV('183'))))
        dat("the row the_tenth_word: covet in deed, desire in the heart — the Mekhilta d'Rabbi Yishmael Bahodesh 8 (named, unopened); Onkelos 'and do not desire'")
        return out("covet and desire (5:21) — the two verbs: the tenth word compiled here; the block coveting_barred on Israel at the giving's line", ['accepted'])
    if ask == 'the_wife_first':
        ink('5:21', 'THE WIFE FIRST — Exodus 20:17 "your neighbor\'s house" first; "his field" added (%d seats); the diff %s' % (len(U('שדהו')), DIFF(('Deut', 5, 21), ('Exod', 20, 17))))
        dat("the row the_tenth_word: the order and 'his field' DATA — the readback row TURNED")
        return out("the wife first (5:21) — the order turned, his field added: a DATA row", ['accepted'])
    if ask == 'the_coveter_who_pays':
        ink('5:21', '"you shall not covet" — the bailee who keeps the deposit and pays')
        move('Bava Metzia 5b:19', "Rav Acha of Difti — taking by force or deceit violates 'you shall not covet' EVEN WITH PAYMENT")
        move('Bava Metzia 5b:20', "most people read 'you shall not covet' as taking WITHOUT payment — the bailee unaware, his oath credible: not disqualified as a robber")
        return out("the coveter who pays (5:21) — the prohibition stands (Rav Acha), the people's reading spares his oath: not a robber (Bava Metzia 5b)", ['exempt'])
    if ask == 'the_write':
        ink('5:21', 'the tenth word whole — the block written on Israel AT THE GIVING\'S LINE, never at the retelling\'s')
        dat("the write: coveting_barred on israel — law_covenant_at_horeb watches ten_words_declared")
        return out("the write (5:21) — coveting_barred on Israel: the code's hole filled at the code's own line", ['coveting_barred'])
    return out('no verdict in span', [FX.NONE])


# ===== F6: THE VOICE AND THE REQUEST (Deut 5:22-27) =========================================================
def the_voice_and_the_request(case, data):
    del P_[:]
    ask = case['ask']
    if ask == 'added_no_more':
        ink('5:22', '"these words the LORD spoke to all your assembly … with a great voice, and he added no more" — "to all your assembly" %s; "and added no more" %s; against 4:13 (tokens %d for %d, %d shared)' % (P('אל', 'כל', 'קהלכם'), P('ולא', 'יסף'), VOICE_DELTA[0], VOICE_DELTA[1], VOICE_DELTA[2]))
        move('obey_horeb.horeb_retold by CALL', "2b's supplied lines FOUND — %r; %r" % (OH_VOICE[1], OH_TABLETS[1]))
        move('Sanhedrin 17a:12; Sotah 10b:12', "'did not cease' — Eldad and Medad who did not stop; Judah who did not cease: Onkelos's reading")
        dat("'added no more' / 'did not cease' a DATA note; the readback row EXPANDED")
        return out("added no more (5:22) — 2b's ten words and tablets FOUND (OH by CALL); 'did not cease' the Talmud's and Onkelos's reading", ['accepted'])
    if ask == 'the_tablets_given_to_me':
        ink('5:22', '"and he wrote them on two tablets of stone and gave them to me" — "and gave them to me" %s; the tablets defective here (%s), plene at 4:13; [2] the parser\'s' % (P('ויתנם', 'אלי'), PT('Deut', 5, 22, 'לחת')))
        move('erection.tablets by CALL', "'the ten words' at %d seats" % ER_TEN['v'])
        return out("the tablets given to me (5:22) — tablets_given FOUND at (1, 4, 17); no second write", ['accepted'])
    if ask == 'you_came_near':
        ink('5:23', '"you came near to me, all the heads of your tribes and your elders" — %s the two seats (1:22 the mob); "the heads of your tribes" %s' % (P('ותקרבון', 'אלי'), P('ראשי', 'שבטיכם')))
        move('opening_speech.the_spies_read_back by CALL', "1:22's asking — %r" % OS_ASK[0][:60])
        move('the Sifrei 20:1 (credited at sitting 1)', "the mob there against the elders and the heads here")
        return out("you came near (5:23) — 1:22's phrase at its second seat: the mob and the elders (OS by CALL; the Sifrei 20:1)", ['accepted'])
    if ask == 'the_request':
        ink('5:24-27', '"go you near and hear … and you speak to us … and we will hear and do" — %s; "why should we die" %s; "the living God" %s; ninety-one tokens against Exodus 20:18\'s eighteen and 20:19\'s thirteen' % (P('קרב', 'אתה', 'ושמע'), P('למה', 'נמות'), P('אלהים', 'חיים')))
        dat("THE TAPE'S SECOND HOLE: Exodus 20:18-19 has no line (20:18 in no span; 20:19-21 the ordinances' cells) — SUPPLIED, dated (1, 3, 7) by the retrograde marker at 5:23 (Rabbi Yose's seventh, ES by CALL: %s)" % (ES_DAYS['v'],))
        move('Makkot 24a:1', "the first two words direct, the rest through Moses — the mediator's row")
        return out("the request (5:24-27) — SUPPLIED: the tape's second hole written once at its own time; the mediator asked for (Makkot 24a)", ['accepted'])
    if ask == 'hear_and_do':
        ink('5:27', '"WE WILL HEAR AND DO" %s against Exodus 24:7\'s "we will do and hear" %s; "we will do" at %s' % (P('ושמענו', 'ועשינו'), P('נעשה', 'ונשמע'), ES_SEATS['v']))
        move('Shabbat 88a:7-9', "R. Simai — 'we will do' before 'we will hear': two crowns; the angels' secret (R. Elazar); the heretic's 'impulsive nation'")
        move('Shabbat 88a:5 (ES.sinai by CALL)', "the mountain overturned like a tub — %r" % ES_TUB['v'])
        return out("hear and do (5:27) — TURNED against 24:7's 'do and hear' (Shabbat 88a); Onkelos 'accept and do'", ['accepted'])
    if ask == 'the_write':
        ink('5:23-27', 'the request whole — the SUPPLIED line writes torah_through_moses on Israel')
        dat("the write: torah_through_moses on israel dated (1, 3, 7) — Avot 1:1's vocabulary; Makkot 24a's two words")
        return out("the write (5:23-27) — torah_through_moses on Israel: the mediator's status", ['torah_through_moses'])
    return out('no verdict in span', [FX.NONE])


# ===== F7: THE ANSWER AND THE CHARGE (Deut 5:28-33) ========================================================
def the_answer_and_the_charge(case, data):
    del P_[:]
    ask = case['ask']
    if ask == 'the_lord_heard':
        ink('5:28', '"and the LORD heard the voice of your words" %s — 1:34\'s five words (the wrath there, the praise here); the one divine frame %s' % (P('וישמע', 'יהוה', 'את', 'קול', 'דבריכם'), DIV))
        move('opening_speech.the_spies_read_back by CALL', "1:34's oath — %r" % OS_OATH[0][:40])
        return out("the LORD heard (5:28) — 1:34's phrase at its second seat (OS by CALL)", ['accepted'])
    if ask == 'done_well':
        ink('5:28', '"they have done well in all that they have spoken" %s — 18:17 cites it forward (%s)' % (P('היטיבו', 'כל', 'אשר', 'דברו'), U('היטיבו')))
        dat("'they have done well' a DATA note; the prophet's promise (18:15-19) chapter 18's sitting; Onkelos 'rightly'")
        return out("they have done well (5:28) — cited forward at 18:17: a DATA note", ['accepted'])
    if ask == 'who_would_give':
        ink('5:29', '"who would give that they had such a heart as this always" %s — "who would give" %d seats (Job\'s nine)' % (P('מי', 'יתן', 'והיה', 'לבבם', 'זה', 'להם'), len(P('מי', 'יתן'))))
        move('Avodah Zarah 4b:17-5a:21', "the calf made to give a claim to penitents; 'with their children forever' those who stood at Sinai; the Angel of Death's decree; 'ingrates' — they should have said 'give us the heart'")
        return out("who would give (5:29) — the calf and the penitents (Avodah Zarah 4b-5a): an aggadah on the answer's verse", ['accepted'])
    if ask == 'return_to_your_tents':
        ink('5:30', '"go say to them: return to your tents" %s — "to your tents" %s; the imperatives %s' % (P('שובו', 'לכם', 'לאהליכם'), U('לאהליכם'), IMPER[30]))
        move('Beitzah 5a:7, 5b:3', "Rav Yosef — the separation of 19:15 released by an explicit word: a matter forbidden by a count needs a count to permit")
        move('Moed Katan 7b:5; Sanhedrin 59b:3-4 (PS.noahide by CALL)', "'his tent' his wife; procreation repeated at Sinai — %r" % PS_PROCR['v'])
        return out("return to your tents (5:30) — the separation released: returned_to_tents on Israel (Beitzah 5a-b)", ['returned_to_tents'])
    if ask == 'stand_here_with_me':
        ink('5:31', '"and you, stand here with me, and I will speak to you all the commandment and the statutes and the judgments which you shall teach them" %s; "which you shall teach them" %s; "all the commandment and the statutes and the judgments" %s (6:1 without "all")' % (P('ואתה', 'פה', 'עמד', 'עמדי'), P('אשר', 'תלמדם'), P('את', 'כל', 'המצוה', 'והחקים', 'והמשפטים')))
        move('erection.ascent by CALL', "Exodus 24:12's 'to teach them' — the pair at %d seats" % ER_TORAH['v'])
        move('Megillah 21a:14; the Sifrei 357:40 (credited)', "the Torah received standing; Moses prophesied standing")
        dat("THE CHARGE TO TEACH a DEBIT on Moses CLOSED AT ONCE BY THE PRIOR RUN — the closer speech_opened at 1:1-5 (OS.the_frame: %r); 4:5's receipt the same run" % OS_WRITE[1])
        return out("stand here with me (5:31) — SUPPLIED: the charge to teach a debit on Moses closed by the prior run (Deut 1:5); the Torah received standing", ['commanded'])
    if ask == 'the_charge':
        ink('5:32-33', '"you shall observe to do as the LORD your God commanded you; you shall not turn aside right or left" %s — "right or left" %s (17:11 the judges\'); "in all the way" six seats; the plural receipt %s' % (P('לא', 'תסרו', 'ימין', 'ושמאל'), P('ימין', 'ושמאל'), RECEIPT_PL))
        dat("NO WRITE (the frame's charge); the receipt 5:32 a run citation of the giving — the seat CHAPTER; the forward marker at 5:32 ends the stretch")
        return out("the charge (5:32-33) — no write: the frame's close; the plural receipt's seat CHAPTER", ['accepted'])
    if ask == 'the_readback_table':
        dat('the row the_readback: %d rows — %s; the law rows %d, the cells named %d, NO CELL %s' % (len(READBACK), dict(RB_GRADES), sum(1 for r in READBACK if r['law']), sum(1 for r in READBACK if r['law'] and r['cell'] != 'NO CELL'), [r['verses'] for r in READBACK if r['cell'] == 'NO CELL']))
        return out("the readback table — twenty-one rows graded (sixteen on the code, five on the narrative); no row open", ['accepted'])
    if ask == 'the_register_seats':
        dat('the row the_receipts: %s; Deut 4:45 DAEMONS 2 unmoved (the new daemon\'s seat Exodus 20:3 outside the block)' % data['the_receipts']['value'])
        return out("the register seats — Deut 5:12, 5:16, 5:32 CHAPTER (the gate's code); 4:45 DAEMONS 2", ['accepted'])
    return out('no verdict in span', [FX.NONE])
