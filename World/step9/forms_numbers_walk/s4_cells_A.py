# ---- (4) THE CELLS — twenty-three, in the text's order; each query a cell(value, provenance, why, effects) ----
NUM = {'מאתים': 200, 'עשרים': 20, 'ועשרים': 20, 'שלשים': 30, 'ארבעים': 40, 'עשרה': 10, 'ועשרה': 10}
_NAME = ('יהוה', 'ליהוה', 'ביהוה', 'ויהוה')


def _gift():
    """the gift's head count by the numerals of Gen 32:15-16, verse by verse (a measurement): two hundred she-goats, twenty he-goats,
    two hundred ewes, twenty rams; thirty milch camels (their colts unnumbered), forty cows, ten bulls, twenty she-asses, ten foals"""
    return [[NUM[w] for w in toks(32, vs) if w in NUM] for vs in (15, 16)]


def _all_seats(pred, chs):
    """seats over EVERY chapter named (the family's included — the census that must not stop at the span)"""
    return [(ch, vs) for ch in chs for vs in range(1, NV[ch] + 1) if pred(toks(ch, vs))]


def _name_by_chapter():
    """the Tetragrammaton's tokens per chapter of Genesis 37-50, the family's chapters included (a measurement); the zero chapters dropped"""
    out = {ch: sum(1 for vs in range(1, NV[ch] + 1) for w in toks(ch, vs) if w in _NAME) for ch in range(37, 51)}
    return {ch: n for ch, n in out.items() if n}


def _pit_seats():
    return [vs for vs in range(1, NV[37] + 1) if any(re.fullmatch(r'ה?ב[ו]?ר[הות]?', w) for w in toks(37, vs))]


def _timer_span(eff):
    """the fire day less the set day of a timer on the scene's own world (a measurement from the log)"""
    s_ = [l[1] for l in _W.log if l[0] == 'TIMER-SET' and l[2]['effect'] == eff]; f_ = [l[1] for l in _W.log if l[0] == 'TIMER-FIRE' and l[2]['effect'] == eff]
    return f_[0] - s_[0] if s_ and f_ else None


def _mohar():
    """THE MOHAR by call: Shechem's 'multiply upon me exceedingly bride-price and gift' (34:12) laid on the seducer's compiled function
    of Exodus 22:15-16 — the rapist's case (34:2 'and he violated her'), run on a bare world; (the fixed sum's value, the money entries)"""
    with contextlib.redirect_stdout(io.StringIO()):
        w = WE.World(era='the mohar of Gen 34:12 on a bare world')
    out = MP2.law_mishpatim_2({'kind': 'virgin_seduced', 'subject': 'shechem', 'seducer': 'shechem', 'father': 'jacob', 'raped': True, 'day': 1,
                               'case_source': 'Gen 34:2 — and he took her and lay with her and violated her; 34:12 the mohar unbounded'}, w)
    fixed = [e for e in out if e['effect'] == 'gives_fixed_sum']
    return (fixed[0]['value'] if fixed else None, len([e for e in out if e['effect'] in ('gives_fixed_sum', 'pays')]))


def jabbok(q):
    if q == 'two_namings': return cell(('mahanaim', 'peniel'), I, "'and he called the name of that place Mahanaim' (32:3), 'and Jacob called the name of the place Peniel' (32:31) — the stretch's first two namings, both Jacob's; name_given twice on the scene", ['name_given', 'camp_of_god_seen'])
    if q == 'angel_bands': return cell('bands_of_angels_all_night', M, "Bereshit Rabbah 78:11 — 'whose is all this camp that I met' (33:8): all that night the ministering angels went in bands and companies and struck Esau's men, who said 'we are Esau's' — 'strike, strike'", ['camp_of_god_seen', 'esau_approaching'])
    if q == 'gift_by_verse': return cell(_gift(), I, "the numerals of 32:15 and 32:16 parsed by _gift() — a measurement; the camels' colts carry no number", ['gift_sent_ahead'])
    if q == 'gift_head_count': return cell(sum(sum(v) for v in _gift()), I, "the gift's head count: 440 of the flock (32:15) + 110 of the herd and the asses (32:16) = 550 — the ink's own arithmetic, no head listed twice", ['gift_sent_ahead'])
    if q == 'too_small': return cell('i_am_too_small_for_all_the_kindnesses', I, "'I am too small for all the kindnesses and all the truth' (32:11, קטנתי) — the prayer's opening; deliverance_prayed the HEAVEN entry the sunrise answers", ['deliverance_prayed'])
    if q == 'left_alone': return cell('alone', I, "'and Jacob was left alone, and a man wrestled with him' (32:25, לבדו) — the wrestling's condition; thigh_dislocated the body entry, never closed: 'and he limped' (32:32)", ['thigh_dislocated', 'limping'])
    if q == 'thigh_socket': return cell(('socket', 'thigh'), I, "'the socket of his thigh' (32:26, כף ירכו) — the sinew statute's own noun pair (32:33 'the socket of the thigh'), the family engine's seat", ['thigh_dislocated'])
    if q == 'renaming_seat': return cell('family_engine_32_29', I, "'your name shall no more be called Jacob but Israel' (32:29) — the family engine's `renamed` seat (O2: one act, one writer); this scene submits name_asked at 32:30 and the blessing, nothing at 32:29", ['blessed_at_the_ford', 'blessing_demanded'])
    if q == 'peniel_penuel': return cell(('peniel', 'penuel'), I, "'Peniel' (32:31, פניאל) and 'Penuel' (32:32, פנואל) — the place's two spellings a verse apart (the tokens measured); one naming on the scene, the second spelling the narrator's", ['name_given', 'limping'])
    if q == 'sinew_seat': return cell('family_engine_32_33', I, "'therefore the children of Israel do not eat the sinew of the thigh-vein to this day' (32:33) — the family engine's `sinew_barred` statute at its own seat, excluded from this span's acts (8a)", ['limping'])
    return cell('no_case', I, '', [FX.NONE])


def esau_met(q):
    if q == 'last_dearest': return cell('last_last_is_dearest', M, "Bereshit Rabbah 78:8 — 'and he put the maids and their children first' (33:2): this says, the last, the last is the dearest", ['children_divided'])
    if q == 'bowed_seven': return cell(7, I, "'and bowed to the ground seven times' (33:3) — the number parsed; bowed_seven_times with value 7 on the ledger", ['bowed_seven_times'])
    if q == 'bow_seats': return cell(len(_seats(lambda ws: any('שתחו' in w for w in ws), 32, 50)), I, "the prostration verb's seats in the span (measured): 33:3, 33:6, 33:7, 37:7, 37:9, 37:10, 42:6, 43:26, 43:28, 47:31 — ten verses; the dreams' bows (37:7-10) received at 42:6, 43:26, 43:28 (the family's 48:12 outside the span)", ['bowed_seven_times', 'bowed_as_the_sheaves', 'bowed_on_the_bed'])
    if q == 'bow_table': return cell(_seats(lambda ws: any('שתחו' in w for w in ws), 32, 50), I, "the same ten seats listed by the census function (a measurement, printed)", ['bowed_as_the_sheaves'])
    if q == 'prostration_form': return cell('hands_and_feet_spread', M, "Berakhot 34b:3 — a baraita: kidah is on the face, keriah on the knees, hishtachavaah is the spreading of hands and feet, from 'shall I and your mother and your brothers come to bow down to you to the ground' (37:10) — the dream's own verb defines the posture", ['bowed_as_the_sheaves'])
    if q == 'dotted_kiss': return cell('script_equals_dots', M, "Bereshit Rabbah 78:9 — 'and he kissed him' (33:4) is dotted: R. Shimon ben Elazar — where the script exceeds the dots expound the script, where the dots exceed expound the dots; here neither exceeds — he kissed him with all his heart (the frozen unit's hard case of the dotted-letters rule)", ['kissed_and_wept'])
    if q == 'grace_verb': return cell('graciously_given', I, "'the children whom God has graciously given your servant' (33:5, חנן) — the grace verb's seat in the meeting (the frozen unit's 'grace verb born')", ['children_divided'])
    if q == 'face_of_god': return cell('as_the_face_of_god_is_judgment', M, "Bereshit Rabbah 78:12 — 'as one sees the face of God' (33:10): as the face of God is judgment, so your face is judgment", ['blessing_returned'])
    if q == 'blessing_returned': return cell('my_blessing', I, "'take, I pray, my blessing that is brought to you' (33:11, ברכתי) — the blessing of Genesis 27 returned by its own name; blessing_returned on Esau's ledger, counterparty Jacob", ['blessing_returned', 'gift_declined'])
    if q == 'seir_promised': return cell('never_narrated', I, "'until I come to my lord to Seir' (33:14, שעירה) — Seir promised and never reached (8m OPEN); seir_promised a HEAVEN-class entry left open on the scene; Bereshit Rabbah 78:14 — 'let my lord pass before his servant': do you wish us to be partners in your world? — let my lord pass", ['seir_promised', 'convoy_declined'])
    if q == 'widen_the_road': return cell('as_jacob_to_esau', M, "Avodah Zarah 25b:8 — if he asks where you go, widen the road for him, as Jacob our father did to Esau the wicked: 'until I come to my lord to Seir' (33:14)", ['seir_promised'])
    if q == 'sukkot_naming': return cell(('booths', 'sukkot'), I, "'and made booths for his cattle; therefore the name of the place is called Sukkot' (33:17, סכת / סכות) — the booths and the name from one verse", ['booths_made', 'name_given'])
    if q == 'sukkot_months': return cell(18, M, "Megillah 17a:7 — he tarried on the road two years: a baraita — he went out from Aram-naharaim and came to Sukkot and made there eighteen months, 'and Jacob journeyed to Sukkot and built him a house and made booths for his cattle' (33:17) — the marker road_years the tape carries", ['encamped_at'])
    return cell('no_case', I, '', [FX.NONE])


def shechem_arrival(q):
    if q == 'came_whole': return cell(('body', 'sons', 'money'), M, "Bereshit Rabbah 79:5 — 'and Jacob came whole' (33:18): whole in his body (against 32:32's limp), whole in his sons (against 32:9's fear), whole in his money", ['came_whole'])
    if q == 'hundred_kesitah': return cell(100, I, "'for a hundred kesitah' (33:19, במאה קשיטה) — the price parsed; field_acquired with amount on the ledger, the family's purchased kind at this scene's seat", ['field_acquired'])
    if q == 'three_places': return cell(3, M, "Bereshit Rabbah 79:7 — R. Yudan bar Simon: one of three places the nations cannot cheat Israel of, saying 'stolen in your hands': the cave of Machpelah, the Temple, and Joseph's tomb", ['field_acquired'])
    if q == 'purchase_by_call': return cell(FA.purchase('three_modes')['v'], P, "CALLED cold_run_family.purchase('three_modes') -> the Mishnah's money, deed, possession run at Machpelah [IMPORT, live]: 'and he bought the portion of the field' (33:19) read against the modes the engine keeps", ['field_acquired'])
    if q == 'purchase_seat': return cell('law_joseph_writes_33_19', I, "the family's `purchased` branch seat-checked to Gen 23 (8k); the field at Shechem written here by law_joseph — one act, one writer", ['field_acquired'])
    if q == 'el_elohe_israel': return cell('god_called_jacob_el', M, "Megillah 18a:17 — R. Acha in R. Elazar's name: whence that the Holy One called Jacob 'el'? 'and he called him El-elohe-Israel' (33:20) — if the altar, it should say 'and Jacob called it'; rather, He called Jacob 'el'", ['altar_built', 'name_given'])
    if q == 'god_below': return cell('you_god_above_i_god_below', M, "Bereshit Rabbah 79:8 — Resh Lakish: 'and he called it El-elohe-Israel' — he said, You are God in the upper worlds and I am god in the lower; Rav Huna in his name: even the synagogue's attendant takes no authority for himself", ['altar_built'])
    return cell('no_case', I, '', [FX.NONE])


def dinah(q):
    if q == 'dinah_seats': return cell(len(_all_seats(lambda ws: 'דינה' in ws or 'ודינה' in ws, range(1, 51))), I, "Dinah's name in Genesis (measured): 30:21, 34:1, 34:5, 34:13, 34:25, 34:26, 46:15 — seven seats", ['violated'])
    if q == 'three_verbs': return cell(('took', 'lay', 'violated'), I, "'and he took her, and lay with her, and violated her' (34:2) — three verbs; violated and defiled (34:5 'defiled') the body entries", ['violated', 'defiled'])
    if q == 'cleaved_loved_spoke': return cell(('cleaved', 'loved', 'spoke_to_her_heart'), I, "'and his soul cleaved to Dinah ... and he loved the girl, and spoke to the girl's heart' (34:3) — the three clauses before the demand (34:4)", ['marriage_demanded'])
    if q == 'silence_kept': return cell('kept_silent_until_they_came', I, "'and Jacob kept silent until they came' (34:5, החרש); Bereshit Rabbah 80:6 — 'a man of understanding keeps silent' (Prov 11:12)", ['silence_kept'])
    if q == 'outrage_phrase': return cell('not_done_in_israel', I, "'he had done an outrage in Israel ... and so it is not done' (34:7, נבלה בישראל) — the phrase's first seat; outrage_in_israel a status", ['outrage_in_israel'])
    if q == 'mohar_unbounded': return cell('multiply_upon_me', I, "'multiply upon me exceedingly bride-price and gift, and I will give as you say to me' (34:12, מהר ומתן) — the law's own noun (Exod 22:16 'the mohar of virgins') named before the law; mohar_offered_unbounded", ['mohar_offered_unbounded'])
    if q == 'mohar_by_call': return cell(_mohar(), P, "CALLED cold_run_mishpatim_2.law_mishpatim_2 on Shechem's case (raped) [IMPORT, live]: the seducer's fixed sum is a POINTER ('FETCH-50' — Deut 22:29's fifty, Ketubot 29b), and the money entries are four (the fine, humiliation, degradation, pain — Mishnah Ketubot 3:4): the law bounds what Shechem offered unbounded", ['mohar_offered_unbounded'])
    if q == 'seducer_sheet': return cell(('three', 'four'), A, "Mishnah Ketubot 3:4 — the seducer gives three things, the rapist four: humiliation, degradation and the fine; the rapist adds the pain — the answer sheet the call reproduces", ['mohar_offered_unbounded'])
    if q == 'deceit_word': return cell('with_guile', I, "'and the sons of Jacob answered Shechem and Hamor with guile' (34:13, במרמה); Bereshit Rabbah 80:8 — you think there is deception here? the holy spirit says 'because he had defiled Dinah their sister'", ['circumcision_conditioned'])
    if q == 'foreskin_homograph': return cell('shechems_ruse_not_the_sign', I, "'a man who has a foreskin' (34:14) and 'as they are circumcised' (34:22) — the covenant's tokens inside the ruse; the scene's own males_circumcised, not the pre-Sinai engine's sign_in_the_flesh (FALSE at the census, 8k)", ['circumcised_by_the_condition'])
    if q == 'third_day_sheet': return cell('bathing_on_the_third_day', A, "Mishnah Shabbat 19:3 — R. Elazar ben Azariah: one bathes the infant on the third day that falls on the Sabbath, for it is said 'and it came to pass on the third day, when they were in pain' (34:25) — the proof text is this verse; Bereshit Rabbah 80:9 brings the row to the verse ('there we learned: one bathes the infant')", ['circumcised_by_the_condition'])
    if q == 'third_day_danger': return cell('danger', M, "Nedarim 31b:14 — Rabbi: Moses did not delay the circumcision; he said, shall I circumcise and go out? it is danger, as it is said 'on the third day, when they were in pain' (34:25)", ['circumcised_by_the_condition'])
    if q == 'third_day_verse': return cell('Gen 34:25', I, "'on the third day, when they were in pain, two of Jacob's sons, Simeon and Levi, Dinah's brothers, took each his sword' (34:25) — the ordinal parsed; the scene's day 546", ['slain_by_sword', 'hamor_and_shechem_slain'])
    if q == 'took_no_counsel': return cell('took_no_counsel_from_jacob', M, "Bereshit Rabbah 80:10 — 'two of Jacob's sons': sons of Jacob who took no counsel from Jacob; 'Simeon and Levi': who took counsel from each other; 'Dinah's brothers': was she the sister of the two alone?", ['slain_by_sword'])
    if q == 'troubled_charged': return cell('the_cask_was_clear', M, "Bereshit Rabbah 80:12 — 'you have troubled me' (34:30): the rabbis — the cask was clear and you have muddied it", ['troubled_charged'])
    if q == 'few_in_number': return cell('few_in_number', I, "'and I being few in number' (34:30, מתי מספר) — the charge's ground; troubled_charged on Simeon and Levi", ['troubled_charged'])
    if q == 'question_unanswered': return cell('as_a_harlot', I, "'should he deal with our sister as with a harlot?' (34:31) — the chapter ends on a question the ink never answers; question_unanswered a status", ['question_unanswered'])
    return cell('no_case', I, '', [FX.NONE])


def bethel_again(q):
    if q == 'foreign_gods_seats': return cell(2, I, "'put away the foreign gods' (35:2) and 'all the foreign gods' (35:4) (הנכר) — two seats; the DEBIT of 35:2 closed at 35:4 on the scene", ['foreign_gods_removal_owed', 'foreign_gods_buried'])
    if q == 'vow_delay': return cell('delay_punished', M, "Bereshit Rabbah 81:1-2 — 'arise, go up to Bethel' (35:1): 'it is a snare to a man to swallow holy things, and after vows to inquire' (Prov 20:25) — the vow's delay read as punished; the DEBIT ascent_to_bethel_owed closed at 35:6, altar_owed at 35:7", ['ascent_to_bethel_owed', 'altar_owed'])
    if q == 'return_closed': return cell('Gen 35:6', I, "28:15 'I will bring you back to this land' (S3's HEAVEN entry) — closed on the tape at 35:6 'and Jacob came to Luz, that is Bethel'; nothing on the bare scene (the entry lives on S3's world)", ['encamped_at'])
    if q == 'vow_closed': return cell('Gen 35:7', I, "28:20-22's vow (S3's entry vow_of_bethel) — closed on the tape at 35:7 'and he built there an altar'; the tithe of 28:22 never narrated as paid (8m OPEN)", ['altar_built'])
    if q == 'terror_of_god': return cell('terror_of_god', I, "'and the terror of God was upon the cities' (35:5, חתת אלהים) — the phrase's seat; terror_of_god a status on the cities", ['terror_of_god'])
    if q == 'allon_bakhut': return cell('greek_for_another_mourning', M, "Bereshit Rabbah 81:5 — 'Allon-bakhut' (35:8): R. Shmuel bar Nachman — it is Greek: allon, another; while he kept Deborah's mourning the news came that his mother had died (Rebekah's death unnarrated — 8m)", ['nurse_died', 'name_given'])
    if q == 'israel_repeated': return cell('Gen 35:10', I, "'your name is Jacob; your name shall not be called Jacob any more, but Israel shall be your name' (35:10) — the renaming repeated by God; the tape's rename is the family engine's (32:29), this seat's blessed_by_the_lord", ['blessed_by_the_lord'])
    if q == 'like_case': return cell('cited_as_the_like_case', M, "Berakhot 12b:28 — 'likewise you say: your name shall no more be called Jacob, but Israel shall be your name' (35:10) — the renaming cited as the like case of a mention that persists beside the new (12b's subject: the exodus remembered beside the future redemption)", ['blessed_by_the_lord'])
    if q == 'be_fruitful_sheet': return cell('a_man_does_not_cease', A, "Mishnah Yevamot 6:6 — a man does not cease from being fruitful and multiplying unless he has children — the commandment's holder", ['fruitfulness_blessed'])
    if q == 'fruitful_singular': return cell('said_to_jacob_singular', M, "Yevamot 65b:5 — Rav Yosef from here: 'I am God Almighty, be fruitful and multiply' (35:11) — said in the singular to Jacob, not 'be fruitful and multiply' in the plural (the man commanded, not the woman)", ['fruitfulness_blessed'])
    if q == 'kings_promised': return cell('kings_from_your_loins', I, "'a nation and an assembly of nations shall be of you, and kings shall come out of your loins' (35:11) — three HEAVEN clauses: fruitfulness_blessed, assembly_of_nations_promised, kings_promised (Genesis 36's kings of Edom before Israel's, 36:31)", ['kings_promised', 'assembly_of_nations_promised'])
    if q == 'land_promised': return cell('to_abraham_and_isaac', I, "'the land which I gave to Abraham and to Isaac, to you I will give it' (35:12) — the third generation's land entry", ['land_promised'])
    if q == 'libation_token': return cell('nesekh_by_name', I, "'and he poured on it a libation, and he poured on it oil' (35:14, נסך) — the drink offering's token read by name; the offerings engine's REFERENCE at the census (no verdict: Exodus 29:40-41's law is the erection's)", ['libation_poured', 'pillar_anointed'])
    if q == 'bethel_named_twice': return cell(2, I, "'and Jacob called the name of the place ... Bethel' at 28:19 (S3's) and 35:15 (this scene's) — the second naming on the scene; name_given on the-place", ['name_given'])
    return cell('no_case', I, '', [FX.NONE])


def three_deaths(q):
    if q == 'buried_writes': return cell(3, I, "the burials the scene writes: Deborah under the oak (35:8), Rachel on the way to Ephrath (35:19), Isaac by Esau and Jacob (35:29) — three `buried` entries by law_joseph (the family's `buried` branch answers 23, 48, 49, 50 alone)", ['buried', 'buried_by_both_sons'])
    if q == 'ben_oni_binyamin': return cell(('ben_oni_aramaic', 'binyamin_holy_tongue'), M, "Bereshit Rabbah 82:9 — 'Ben-oni': son of my sorrow in Aramaic; 'and his father called him Binyamin': in the holy tongue — two namings on one verse (35:18), the mother's and the father's", ['name_given', 'died_in_childbirth'])
    if q == 'benjamin_plene': return cell((len(_all_seats(lambda ws: any(w.endswith('בנימין') for w in ws), range(1, 51))), len(_all_seats(lambda ws: any(w.endswith('בנימן') for w in ws), range(1, 51)))), I, "Benjamin's spelling in Genesis MEASURED against Sotah 36b:9 (Rav Nachman bar Yitzchak: 'in the whole Torah it is written Binyamin short, and here Binyamin full, as 35:18'): full at 35:18, 42:4, 43:14, 43:16, 43:29, 45:12, 49:27 — seven; short at 35:24, 42:36, 43:15, 43:34, 44:12, 45:14, 45:22, 46:19, 46:21 — nine; recorded whichever way it falls (8m): the DB's letters give seven full seats in Genesis alone", ['name_given'])
    if q == 'grave_pillar': return cell('no_monuments_for_the_righteous', M, "Bereshit Rabbah 82:10 — 'and Jacob set a pillar on her grave' (35:20): R. Shimon ben Gamliel — one makes no monuments for the righteous; their words are their memorial", ['grave_marked'])
    if q == 'until_this_day': return cell('the_pillar_of_rachels_grave', I, "'it is the pillar of Rachel's grave to this day' (35:20) — the narrator's present; grave_marked on the-grave-of-rachel", ['grave_marked'])
    if q == 'reuben_sheet': return cell('read_not_translated', A, "Mishnah Megillah 4:10 — the act of Reuben (35:22) is read and not translated; concubine_lain_with carries the value read_not_translated on the ledger", ['concubine_lain_with'])
    if q == 'israel_heard': return cell('and_israel_heard', I, "'and Israel heard' (35:22, וישמע ישראל) — the verse breaks mid-line (the frozen unit's read of the open space); israel_heard a status, the sentence never finished", ['israel_heard'])
    if q == 'twelve_kept': return cell(12, I, "'and the sons of Jacob were twelve' (35:22) — parsed, in the same verse as the act; Bereshit Rabbah 82:11: the chain of lineage is hard to uproot before the Holy One", ['twelve_sons_listed', 'concubine_lain_with'])
    if q == 'twelve_named': return cell(len(ROSTERS['twelve']), I, "Reuben, Simeon, Levi, Judah, Issachar, Zebulun, Joseph, Benjamin, Dan, Naphtali, Gad, Asher (35:23-26) — twelve name tokens, each verified in its verse by the probes; 'born to him in Paddan-aram' with Benjamin among them (35:26 — the frozen unit's note)", ['twelve_sons_listed'])
    if q == 'isaac_180': return cell(180, I, "'and the days of Isaac were a hundred and eighty years' (35:28) — parsed; the marker died:isaac on the tape, proleptic (CJ2: twelve years after the sale)", ['full_of_days'])
    if q == 'buried_by_both': return cell(('esau', 'jacob'), I, "'and Esau and Jacob his sons buried him' (35:29) — Esau named first; buried_by_both_sons", ['buried_by_both_sons'])
    if q == 'gathered_seat': return cell('law_joseph_35_29', I, "the family's `gathered` branch seat-checked to Gen 49 (8k); Isaac's gathering written here — 'old and full of days' (35:29) full_of_days beside it", ['gathered_to_his_people', 'full_of_days'])
    return cell('no_case', I, '', [FX.NONE])


def edom(q):
    if q == 'wives_recorded': return cell(('adah', 'oholibamah', 'basemath'), I, "'Adah the daughter of Elon the Hittite, and Oholibamah the daughter of Anah ... and Basemath, Ishmael's daughter, sister of Nebaioth' (36:2-3) — three wives, three wife_taken entries; against 26:34 (Judith, Basemath daughter of Elon) and 28:9 (Mahalath daughter of Ishmael): recorded, no fold (8m)", ['wife_taken'])
    if q == 'timna_concubine': return cell('concubine', I, "'and Timna was concubine to Eliphaz, Esau's son, and she bore to Eliphaz Amalek' (36:12, פילגש); Bereshit Rabbah 82:14 — why is this written? to tell the honour of Abraham's house, how far kings and rulers wished to cleave to it", ['begotten'])
    if q == 'timna_amalek': return cell('rejected_proselyte', M, "Sanhedrin 99b:8 — Timna sought to convert; she came to Abraham, Isaac and Jacob and they did not accept her; she went and became a concubine to Eliphaz: 'better a maidservant to this nation than a lady to another' — from her came Amalek, who afflicted Israel: because they should not have pushed her away (a conduct verdict, a status — 8m)", ['begotten'])
    if q == 'two_anas': return cell('one_anah_zibeon_on_his_mother', M, "Bava Batra 115b:4 — 'these are the sons of Seir the Horite: Lotan, Shobal, Zibeon and Anah' (36:20) and 'these are the sons of Zibeon: Aiah and Anah' (36:24) — it teaches that Zibeon came upon his mother and begot Anah; Bereshit Rabbah 82:15 the same (8m)", ['horites_listed'])
    if q == 'kings_count': return cell(sum(1 for vs in range(1, NV[36] + 1) for w in toks(36, vs) if w == 'וימלך'), I, "'and he reigned' (וימלך) in Genesis 36 — eight tokens (36:32-39, measured): Bela, Jobab, Husham, Hadad, Samlah, Shaul, Baal-hanan, Hadar; reigned_in_edom eight times on the scene", ['reigned_in_edom'])
    if q == 'kings_named': return cell(len(ROSTERS['kings']), I, "the eight kings' names verified in their verses by the probes (36:32-39)", ['reigned_in_edom'])
    if q == 'before_a_king': return cell('before_israel_had_a_king', I, "'these are the kings who reigned in the land of Edom before there reigned any king over the children of Israel' (36:31) — the narrator's forward glance; 35:11's kings_promised the entry it answers to", ['reigned_in_edom'])
    if q == 'nations_as_ship': return cell('a_ship_from_many_places', M, "Bereshit Rabbah 83:1 — 'these are the kings' (36:31): R. Yitzchak — the nations are likened to a ship, its mast from one place and its anchors from another", ['reigned_in_edom'])
    if q == 'melekh_homograph': return cell('king_not_molech', I, "'before there reigned any king' (36:31, מלך) — the king word's consonants are Molech's; a homograph, FALSE at the census (S2, S3 the same)", ['reigned_in_edom'])
    if q == 'holding_homograph': return cell('edoms_holding_not_the_jubilees', I, "'in the land of their holding' (36:43, אחזה) — Edom's holding outside the land of the jubilee's law: a homograph, FALSE at the census", ['dwelt_in_seir'])
    if q == 'parted_for_room': return cell('too_great_to_dwell_together', I, "'their possessions were too great for them to dwell together' (36:7) — the parting's ground, as 13:6's (S2's Lot); parted and dwelt_in_seir on Esau", ['parted', 'dwelt_in_seir'])
    return cell('no_case', I, '', [FX.NONE])


def dreamer(q):
    if q == 'seventeen': return cell(17, I, "'Joseph, seventeen years old' (37:2) — parsed; the marker age:joseph:17 the tape computes off born:jacob (8k: born:joseph is not on the tape at 37:2)", ['loved_by_the_father'])
    if q == 'youthful_deeds': return cell('deeds_of_youth', M, "Bereshit Rabbah 84:7 — 'seventeen years old ... and he was a lad' (37:2): he did the deeds of youth — touching his eyes, lifting his heel, arranging his hair", ['evil_report_brought'])
    if q == 'coat_seats': return cell(len(_seats(lambda ws: any(w.endswith('פסים') for w in ws), 37, 37)), I, "'a coat of stripes' (כתנת פסים) in Genesis 37 — 37:3 (made), 37:23 (stripped), 37:32 (sent): three seats, measured; the coat's three acts on the ledger; Bereshit Rabbah 84:16 — 'they stripped Joseph' (37:23): four garments named on the one verse, the coat of stripes the third", ['coat_of_stripes_made', 'stripped_of_the_coat', 'coat_recognized'])
    if q == 'why_loved': return cell(('likeness', 'the_laws_of_shem_and_eber'), M, "Bereshit Rabbah 84:8 — 'and Israel loved Joseph' (37:3): R. Yehuda — his features resembled his; R. Nechemya — all the laws Shem and Eber handed to Jacob he handed to him", ['loved_by_the_father'])
    if q == 'dreams_told': return cell(2, I, "the sheaves (37:5-8) and the sun, moon and stars (37:9-11) — two dreams told; dream_of_sheaves, dream_of_sun_moon_stars on Joseph", ['dream_of_sheaves', 'dream_of_sun_moon_stars'])
    if q == 'dream_hope_years': return cell(22, M, "Berakhot 55b:2 — R. Levi: a man should hope for a good dream up to twenty-two years — from Joseph: 'seventeen years old' (37:2) and 'thirty years old when he stood before Pharaoh' (41:46), thirteen, and the seven of plenty and two of famine: twenty-two (the sequence runner CJ0's twenty-two on the other chain)", ['dream_of_sheaves'])
    if q == 'word_kept': return cell('kept_the_matter', I, "'and his brothers envied him, but his father kept the matter' (37:11, שמר) — envied on the brothers, word_kept on Jacob", ['envied', 'word_kept'])
    if q == 'pit_seats': return cell(len(_pit_seats()), I, "the pit noun's seats in Genesis 37 (measured by _pit_seats(): 37:22, 37:24, 37:28, 37:29) — four; 'one of the pits' (37:20) the plural; in_the_pit the body entry from 37:24, closed at 37:28", ['in_the_pit'])
    if q == 'pit_empty': return cell('snakes_and_scorpions', M, "Chagigah 3a:14 — 'and the pit was empty, there was no water in it' (37:24): from 'empty' I do not know there was no water? rather, water there was not, but snakes and scorpions there were", ['in_the_pit'])
    if q == 'what_profit': return cell('botzea_is_judah', M, "Sanhedrin 6b:5 — R. Meir: 'botzea' (Ps 10:3) is said only of Judah: 'and Judah said to his brothers, what profit (בצע) if we slay our brother' (37:26) — whoever blesses Judah blasphemes", ['sale_proposed'])
    if q == 'sellers_grammar': return cell('midianites_drew_ishmaelites_bought_medanites_sold', I, "'and Midianite men, merchants, passed; and they drew and lifted Joseph out of the pit, and sold Joseph to the Ishmaelites for twenty silver' (37:28); 'and the Medanites sold him into Egypt to Potiphar' (37:36); 'whom you sold into Egypt' (45:4) — the seller OPEN (8m); Bereshit Rabbah 84:18 'the Midianites passed'; 84:17 — 'and they sat down to eat bread' (37:25): the tribes' transgression is remembered forever", ['sold_into_egypt', 'sold_to_potiphar'])
    if q == 'twenty_silver': return cell(20, I, "'for twenty silver' (37:28, בעשרים כסף) — parsed; sold_into_egypt with amount 20 on Joseph's ledger; Sotah 36b:19 the astrologers' 'a slave his master bought for twenty silver'", ['sold_into_egypt'])
    if q == 'reuben_where': return cell(('sackcloth_and_fast', 'his_turn_to_serve'), M, "Bereshit Rabbah 84:19 — 'and Reuben returned to the pit' (37:29): where had he been? R. Eliezer — in his sackcloth and his fast; R. Yehoshua — his turn had come to serve his father", ['rescue_urged'])
    if q == 'tunic_by_call': return cell(VS.tunics('tunic_atones')['v'], P, "CALLED cold_run_vestments.tunics('tunic_atones') -> the vestments engine's own row [IMPORT, live]: the TUNIC atones for bloodshed, 'and they slaughtered a goat and dipped the tunic in the blood' (37:31) — Arakhin 16a:13, Zevachim 88b:6: THE FLOW REVERSED, a narrative verse the source of a law's row", ['coat_dipped'])
    if q == 'recognition_row': return cell('recognize_answered_by_recognize', M, "Sotah 10b:7 — R. Chama bar Chanina: with 'recognize' he told his father ('recognize now whether it is your son's coat', 37:32), with 'recognize' they told him ('recognize now whose these are', 38:25 — the family's seat)", ['coat_recognized'])
    if q == 'recognized_seat': return cell('law_joseph_37_33', I, "the family's `recognized` branch seat-checked to Gen 38 (8k — Judah's acquittal of Tamar); the coat's recognition (37:33) written here: coat_recognized, 'an evil beast has devoured him; Joseph is surely torn'", ['coat_recognized'])
    if q == 'mourned_many_days': return cell('many_days', I, "'and mourned for his son many days' (37:34, ימים רבים); 'and he refused to be comforted' (37:35) — mourned_many_days, comfort_refused: the mourning that outlives its object", ['mourned_many_days', 'comfort_refused'])
    if q == 'daughters_plural': return cell('sons_in_law_and_daughters_in_law', M, "Bereshit Rabbah 84:21 — 'and all his sons and all his daughters rose' (37:35): how many daughters had he? one, and would that he had buried her — rather, a man does not refrain from calling his son-in-law son and his daughter-in-law daughter; R. Yehuda: the tribes married their sisters", ['comfort_refused'])
    return cell('no_case', I, '', [FX.NONE])


def potiphar(q):
    if q == 'potiphar_spellings': return cell((_all_seats(lambda ws: 'פוטיפר' in ws or 'לפוטיפר' in ws, range(1, 51)), _all_seats(lambda ws: 'פוטי' in ws, range(1, 51))), I, "'Potiphar' (פוטיפר) at 37:36, 39:1 and 'Poti-phera' (פוטי פרע, two tokens) at 41:45, 41:50, 46:20 — measured; Sotah 13b:12 — Rav: he bought him for himself; Gabriel came and castrated him: at first 'Potiphar', at the end 'Potiphera' — recorded, no fold (8m)", ['bought_by_potiphar'])
    if q == 'bought_ones_buy': return cell('bought_ones_acquire', M, "Bereshit Rabbah 86:3 — 'and he bought him' (39:1): the bought acquire — all slaves diminish their master's house, but this one, 'the LORD blessed the Egyptian's house for Joseph's sake' (39:5); all slaves are suspected of theft, but this one, 'Joseph gathered all the silver' (47:14)", ['bought_by_potiphar', 'house_blessed_for_joseph'])
    if q == 'the_name_in_39': return cell(_name_by_chapter(), I, "the Tetragrammaton in Genesis 37-50 by chapter (measured over the family's chapters too): 39 eight tokens ('and the LORD was with Joseph' 39:2, 39:21, and six more), 38 three (the family's Judah and Tamar), 49 one (49:18 'I wait for Your salvation, LORD'), every other chapter zero — the Name in the Joseph story lives in Potiphar's house and the prison", ['prospering', 'house_blessed_for_joseph'])
    if q == 'adjoined_blessing': return cell('adjoin_blessing_to_scholars', M, "Berakhot 42a:8 — Abaye: adjoin a blessing to scholars: 'and the LORD blessed the Egyptian's house for Joseph's sake' (39:5)", ['house_blessed_for_joseph'])
    if q == 'handsome_as_rachel': return cell('as_rachel', I, "'and Joseph was of beautiful form and beautiful appearance' (39:6, יפה תאר ויפה מראה) = 29:17's 'of beautiful form and beautiful appearance' of Rachel (יפת תאר ויפת מראה) — the same pair in the masculine (the tokens measured)", ['lie_with_me_demanded'])
    if q == 'lifted_eyes': return cell('the_eyes_of_the_wife', M, "Horayot 10b:11 — 'and his master's wife lifted her eyes to Joseph' (39:7) among the eye-liftings the row lists with Lot's (13:10) and Samson's; 'and Shechem the son of Hamor saw her' (34:2) beside them", ['lie_with_me_demanded'])
    if q == 'refused': return cell('a_transgression_is_refused', M, "Bereshit Rabbah 87:5 — 'and he refused' (39:8): Yehuda ben Rabbi — in a matter of commandment one refuses ('my brother-in-law refuses', Deut 25:7), in a matter of transgression one refuses: 'and he refused and said to his master's wife'", ['refused'])
    if q == 'as_this_day': return cell('to_do_his_work', I, "'and it came to pass about this day, that he went into the house to do his work' (39:11, לעשות מלאכתו) — the ink's own clause; fled_outside and garment_left the acts", ['fled_outside', 'garment_left'])
    if q == 'hebrew_seats': return cell(len(_seats(lambda ws: any(w in ('עברי', 'העברי', 'עברים', 'העברים') for w in ws), 39, 43)), I, "'Hebrew' in Genesis 39-43 (measured): 39:14, 39:17 (the wife's accusation), 40:15 ('the land of the Hebrews'), 41:12 ('a Hebrew lad, a slave'), 43:32 ('the Hebrews') — five seats; the epithet, not the Hebrew slave law's subject (FALSE at the census)", ['accused_falsely'])
    if q == 'prison_house': return cell(sum(1 for ch in (39, 40) for vs in range(1, NV[ch] + 1) for w in toks(ch, vs) if w == 'הסהר'), I, "'the round-house' (הסהר) in Genesis 39-40 — eight tokens (measured); imprisoned the body entry, appointed_over_the_prisoners its reversal within the walls", ['imprisoned', 'appointed_over_the_prisoners'])
    if q == 'service_pleasant': return cell('his_service_pleasant', M, "Bereshit Rabbah 87:10 — 'and the LORD was with Joseph ... and the keeper of the prison gave' (39:21-22): Rav Huna in R. Acha's name — his service was pleasant to his master: he went out and rinsed the cups, set the tables, made the beds", ['favor_in_the_keepers_eyes'])
    return cell('no_case', I, '', [FX.NONE])


def prison_dreams(q):
    if q == 'two_officers': return cell(('cupbearer', 'baker'), I, "'the chief of the cupbearers and the chief of the bakers' (40:2) — two officers, one night, two dreams (40:5); dreams_in_one_night", ['dreams_in_one_night', 'in_custody'])
    if q == 'three_days_parsed': return cell((3, 3), I, "'the three branches are three days' (40:12), 'the three baskets are three days' (40:18) — parsed; two timers set on day 735 due 738 on the bare scene", ['interpretation_given', 'head_lifted_up_due', 'head_lifted_off_due'])
    if q == 'third_day_timers': return cell(_timer_span('head_lifted_up_due'), I, "the cupbearer's timer on the bare scene, MEASURED from the log (the fire day less the set day): 'in yet three days' (40:13) read INCLUSIVE as the tape reads every third day (22:4, 31:22) — set at the interpretation, fires on the third day, the birthday (40:20), before the acts (CJ6 on the tape); the model's exclusive 738 corrected at the design of the tape's rows (8n)", ['head_lifted_up_due', 'head_lifted_off_due'])
    if q == 'birthday': return cell('Gen 40:20', I, "'and it came to pass on the third day, Pharaoh's birthday' (40:20) — the ordinal parsed; the marker birthday on the tape; feast_made", ['feast_made'])
    if q == 'lifted_head_two_ways': return cell(('restored', 'hanged'), I, "'lift up your head' (40:13) and 'lift up your head from off you' (40:19) — one idiom, two verdicts: 'restored the chief cupbearer to his cupbearing' (40:21), 'the chief baker he hanged' (40:22)", ['restored_to_the_cup', 'hanged'])
    if q == 'former_custom': return cell('the_first_manner', I, "'according to the former manner when you were his cupbearer' (40:13, כמשפט הראשון) — the citation form AS_PRESCRIBED filed INTERNAL: the cupbearer's own office cited (40:1-2), no law's prescription", ['restored_to_the_cup'])
    if q == 'custody_closes': return cell(('Gen 40:21', 'Gen 40:22'), I, "in_custody (40:3) closed twice on the scene: the cupbearer's at his restoration, the baker's at his hanging", ['in_custody'])
    if q == 'vine_is_israel': return cell('israel', M, "Bereshit Rabbah 88:5 — 'behold a vine before me' (40:9): these are Israel ('You brought a vine out of Egypt', Ps 80:9); 'three branches' — Moses, Aaron and Miriam", ['dreams_in_one_night'])
    if q == 'forgot': return cell('you_forget_i_do_not', M, "Bereshit Rabbah 88:7 — 'and the chief cupbearer did not remember Joseph' (40:23): the Holy One said, you forget him and I will not forget him; petition_forgotten a status, the DEBIT the two years of 41:1 measure", ['petition_forgotten', 'remembrance_asked'])
    return cell('no_case', I, '', [FX.NONE])


def pharaoh_dreams(q):
    if q == 'two_years': return cell('two_years_of_days', I, "'at the end of two years of days' (41:1, שנתים ימים) — the marker pharaoh_dreams on the tape; Nazir 5a:5 — 'days' without 'years' are learned from 'days' without 'years', and not from this, which has years with it", ['spirit_troubled'])
    if q == 'end_to_darkness': return cell('an_end_set_to_darkness', M, "Bereshit Rabbah 89:1 — 'at the end of two years' (41:1): 'He sets an end to darkness' (Job 28:3) — a time was given to the world, how many years it shall do in gloom", ['spirit_troubled'])
    if q == 'seven_and_plenty': return cell(sum(1 for vs in range(1, NV[41] + 1) for w in toks(41, vs) if w in ('שבע', 'ושבע', 'שבעת', 'שבעה', 'השבע')), I, "the consonants שבע in Genesis 41 — thirty-one tokens (measured): seven (sheva) and plenty (sava) share one skeleton, the sin/shin split invisible to the consonants ('seven years of plenty', 41:34 בשבע שני השבע, two words one spelling) — the vowel layer separates them (the Onkelos/vowel finding of the ink era)", ['one_dream', 'plenty_seven_years'])
    if q == 'one_dream': return cell('one', I, "'the dream of Pharaoh is one' (41:25), 'it is one dream' (41:26) — the interpretation's first move; one_dream with value 7 years", ['one_dream'])
    if q == 'doubled': return cell('established_and_hastened', I, "'and as for the dream being doubled to Pharaoh twice, it is because the thing is established by God, and God will shortly bring it to pass' (41:32, השנות — the doubling, פעמים — twice) — the doubling read as a legal signature", ['pharaohs_dream_doubled'])
    if q == 'not_i_god': return cell('god_will_answer', I, "'it is not in me; God will answer Pharaoh's peace' (41:16) — not_i_god a status before the interpretation", ['not_i_god', 'no_interpreter'])
    if q == 'fifth_counsel': return cell('a_fifth', I, "'and let him take a fifth of the land of Egypt in the seven years of plenty' (41:34, וחמש) — the verb of the fifth; the sanctuary's fifth (Lev 27) a homograph, FALSE at the census", ['counsel_of_the_fifth'])
    if q == 'rushed_from_the_pit': return cell('the_pit_again', I, "'and they rushed him from the pit' (41:14, מן הבור) — the prison called by the pit's noun (37:24's); rushed_from_the_pit", ['rushed_from_the_pit'])
    return cell('no_case', I, '', [FX.NONE])


def the_rise(q):
    if q == 'joseph_of_his_own': return cell('of_his_own_they_gave_him', M, "Bereshit Rabbah 90:3 — 'and Pharaoh said to Joseph ... and Pharaoh removed his ring' (41:41-42): R. Shimon ben Gamliel — of Joseph's own they gave him: the mouth that did not kiss in transgression, 'by your mouth shall all my people be fed'; the body that did not touch transgression, 'and he clothed him'", ['ring_given', 'set_over_egypt'])
    if q == 'astrologers': return cell('a_slave_bought_for_twenty', M, "Sotah 36b:19 — when Pharaoh said 'without you no man shall lift his hand' (41:44), Pharaoh's astrologers said: a slave his master bought for twenty silver you would set over us? he said: I see royal traits in him", ['set_over_egypt'])
    if q == 'zaphenath': return cell(1, I, "'Zaphenath-paneah' (41:45, צפנת פענח) — the name's only seat (measured); name_given by Pharaoh", ['name_given'])
    if q == 'asenath': return cell('daughter_of_potiphera_priest_of_on', I, "'Asenath the daughter of Poti-phera priest of On' (41:45) — wife_taken with husband Joseph, asenath_given by Pharaoh; the marriage the family engine's vocabulary at this scene's seat", ['asenath_given', 'wife_taken'])
    if q == 'thirty': return cell(30, I, "'and Joseph was thirty years old when he stood before Pharaoh' (41:46) — parsed; the marker joseph30 the tape carries, born:joseph computed from it", ['thirty_at_the_standing'])
    if q == 'seventeen_to_thirty': return cell(13, I, "thirty (41:46) minus seventeen (37:2): thirteen years from the sale to the standing — the ink's own arithmetic (Berakhot 55b:2 counts it)", ['thirty_at_the_standing'])
    if q == 'handfuls': return cell('by_handfuls', M, "Bereshit Rabbah 90:5 — 'and the earth brought forth in the seven years of plenty by handfuls' (41:47): R. Yochanan — the shrunken and the unshrunken", ['food_gathered_as_sand'])
    if q == 'two_sons_before_the_famine': return cell('before_the_famine', I, "'and to Joseph were born two sons before the year of famine came' (41:50) — two_sons_before_the_famine; Manasseh and Ephraim `born` under Genesis 17, the eighth-day timers set", ['two_sons_before_the_famine'])
    if q == 'famine_years_bar': return cell('marital_relations_barred_in_famine', M, "Taanit 11a:4 — Resh Lakish: it is forbidden to a man to serve his bed in the years of famine, as it is said 'and to Joseph were born two sons before the year of famine came' (41:50); a tanna: the childless serve their beds in the years of famine", ['two_sons_before_the_famine'])
    if q == 'manasseh_ephraim': return cell(('made_me_forget', 'made_me_fruitful'), I, "'Manasseh, for God has made me forget all my toil' (41:51), 'Ephraim, for God has made me fruitful in the land of my affliction' (41:52) — two namings by Joseph, name_given twice", ['name_given'])
    if q == 'eighth_days': return cell(3, I, "the eighth-day timers on the scene's births: Benjamin (35:18), Manasseh and Ephraim (41:50) — three, none on a daughter; the pre-Sinai daemon's own run (CJ8 on the tape)", ['two_sons_before_the_famine'])
    if q == 'covenant_heads_by_call': return cell(PS_.covenant('covenant_heads')['v'], P, "CALLED cold_run_pre_sinai.covenant('covenant_heads') -> the covenant's addressees [IMPORT, live]: 'you and your seed after you' (17:9) — the births of this stretch are that seed's, the eighth day their statute", ['two_sons_before_the_famine'])
    if q == 'plenty_timer_days': return cell(2555, D, "the seven years of plenty on the bare scene: 7 × 365 days (no epoch — the Calendar's year on the tape); the famine's seven set at their fire (41:54), the five remaining at 45:6 — CJ9: one due day", ['plenty_seven_years', 'famine_seven_years'])
    if q == 'famine_in_all_lands': return cell('all_lands', I, "'and the famine was over all the face of the earth' (41:56), 'and all the earth came to Egypt' (41:57) — famine_in_all_lands on the-lands; Pesachim 119a:6 the silver of all lands", ['famine_in_all_lands', 'storehouses_opened'])
    return cell('no_case', I, '', [FX.NONE])
