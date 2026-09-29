def RNG(r):
    c, vv = r.split(':'); parts = vv.split('-'); return int(c), int(parts[0]), int(parts[-1])
KINDS = []
for kind, first, rng, claim, cell, form, fields, effs, reuses in S.LINES:
    c, lo, hi = RNG(rng); en, he_en, extra, speaker, tape = KEN[kind]
    KINDS.append((kind, form, en, HE(D, c, lo, hi, he_en), WIT(D, c, lo, hi) + [w for ws in extra for w in ws], INK, CORPUS, SUB % (speaker, tape), fields))
OWN16 = [k[0] for k in KINDS]
assert len(KINDS) == 16 and OWN16 == S.KINDS and all(len(k[8]) >= 3 for k in KINDS)
assert [k[1] for k in KINDS].count('speech') == 14 and [k[1] for k in KINDS].count('act') == 1 and [k[1] for k in KINDS].count('statute') == 1
path = f"{ROOT}/World/step9/event_vocabulary.yaml"
text = open(path, encoding='utf-8').read()
have = yaml.safe_load(text)['events']
HOLEK = sorted(k for k in have if k in OWN16)
NEARK = sorted(k for k in have if k not in OWN16 and any(t in k for t in ('song_', 'witnesses_called', 'crooked', 'nations_divided', 'desert', 'honey', 'jeshurun', 'face_hidden', 'evils_heaped', 'enemys', 'thousand', 'vengeance', 'i_am_he', 'set_your_heart', 'nebo', 'meribah')))
print('the registry\'s kinds among the sixteen before this sitting:', HOLEK, '| the near kinds on file (not ours):', NEARK)
assert HOLEK == [] or HOLEK == sorted(OWN16), HOLEK   # the sixteen kinds absent before this sitting — or this sitting's own, written by the first run (idempotent)
out = []
for name, form, en, he, wit, ink, corpus, tape, fields in KINDS:
    if name in have: continue
    out.append(f"  {name}:\n    en: {q(en)}\n    he: {q(he)}\n    form: {form}\n    witness: [{', '.join(q(w) for w in wit)}]\n    ink: {q(ink)}\n    corpus: {q(corpus)}\n    tape: {q(tape)}\n    fields: [{', '.join(q(f) for f in fields)}]\n")
if out and not CHECK:
    i = text.index('\nnarrative_verbs:\n')
    text = text[:i] + '\n' + ''.join(out).rstrip('\n') + text[i:]
    open(path, 'w', encoding='utf-8').write(text)
after = yaml.safe_load(open(path, encoding='utf-8'))
assert CHECK or all(k[0] in after['events'] for k in KINDS)
print('kinds: %d %s of %d (14 speech / 1 act / 1 statute), registry %d; the ledger sources %d (%d excluded -> %d), Onkelos %d, the spine %d, outside %d rows in piskaot %s' % (len(out), 'to add' if CHECK else 'added', len(KINDS), len(after['events']), N_SRC, N_EX, N_SRC - N_EX, N_ONK, N_SPINE, N_OUT, OUTSIDE))
# ---- FORTY-TWO new effects (the shelf's own words for their names and values, the `he` FOUND in the verse); the kin's effects asserted present; THE FORTY-TWO NAMES ASSERTED ABSENT before (the holes) ----
path = f"{ROOT}/World/step9/effect_vocabulary.yaml"
text = open(path, encoding='utf-8').read()
fx = yaml.safe_load(text)['effects']
for e in list(S.KIN_UNMOVED) + list(S.REUSE_BEFORE):
    assert e in fx, e
assert fx['heaven_and_earth_witness']['ledger_op'] == 'status' and fx['face_hidden_and_forsaken_foretold']['ledger_op'] == 'heaven' and fx['length_of_days_on_the_land_promised']['ledger_op'] == 'heaven' and fx['barred_from_the_land']['ledger_op'] == 'heaven' and fx['gathered_to_his_people']['ledger_op'] == 'status' and fx['treasured_people']['ledger_op'] == 'heaven' and fx['other_gods_barred']['ledger_op'] == 'block' and fx['manna_provided']['ledger_op'] == 'status', 'the reused and referenced rows\' ops (READ from the registry\'s print at RUN B — treasured_people a heaven entry, gathered_to_his_people a status)'
OWN42 = tuple(S.NEW_EFFECTS)
assert len(OWN42) == 42 and len(set(OWN42)) == 42
HOLE0 = sorted(k for k in fx if k in OWN42)
NEAR0 = sorted(k for k in fx if k not in OWN42 and any(t in k for t in ('doctrine', 'name_of_the_lord', 'the_rock', 'crooked', 'acquired', 'days_of_old', 'nations_bounds', 'lords_portion', 'desert', 'apple', 'eagle', 'alone_led', 'heights', 'feast_of', 'jeshurun', 'demons', 'begot', 'no_people', 'sheol', 'evils_heaped', 'hunger_beasts', 'blotting', 'void_of_counsel', 'thousand', 'vine_of_sodom', 'in_store', 'judges_his_people', 'their_gods', 'i_am_he', 'make_alive', 'hand_lifted', 'whetted', 'land_atones', 'song_spoken_in', 'hoshea', 'set_your_heart', 'no_empty', 'nebo', 'gathered_to_your', 'as_aaron', 'meribath', 'not_go_there')))
print('the registry\'s effects among the forty-two before this sitting:', HOLE0, '| the near effects on file (not ours):', NEAR0)
assert HOLE0 == [] or HOLE0 == sorted(OWN42), HOLE0   # THE HOLES — the forty-two names absent before this sitting (the recon measured them absent) — or this sitting's own, written by the first run (idempotent)
# THE HEBREW FOUND IN THE VERSES — the plain tokens typed from the store's print (ch32_store_glosses.txt — the 52 verses' tokens) at RUN B's head; PHRASE refuses two hits or none
H = {}
# F1 THE WITNESSES AND THE ROCK
H['doctrine_as_rain_and_dew_likened'] = PHRASE(D, 32, 2, ['יערף', 'כמטר', 'לקחי', 'תזל', 'כטל', 'אמרתי']); H['name_of_the_lord_proclaimed_greatness_ascribed'] = PHRASE(D, 32, 3, ['כי', 'שם', 'יהוה', 'אקרא', 'הבו', 'גדל', 'לאלהינו'])
H['the_rock_perfect_and_just_declared'] = PHRASE(D, 32, 4, ['הצור', 'תמים', 'פעלו', 'כי', 'כל', 'דרכיו', 'משפט'])
# F2 THE CROOKED GENERATION
H['generation_crooked_not_his_children'] = PHRASE(D, 32, 5, ['שחת', 'לו', 'לא', 'בניו', 'מומם', 'דור', 'עקש', 'ופתלתל']); H['father_who_acquired_you_requited'] = PHRASE(D, 32, 6, ['הלוא', 'הוא', 'אביך', 'קנך', 'הוא', 'עשך', 'ויכננך'])
# F3 THE NATIONS DIVIDED AND THE PORTION
H['days_of_old_remember_commanded'] = PHRASE(D, 32, 7, ['זכר', 'ימות', 'עולם', 'בינו', 'שנות', 'דור', 'ודור']); H['nations_bounds_set_by_number_of_israel'] = PHRASE(D, 32, 8, ['יצב', 'גבלת', 'עמים', 'למספר', 'בני', 'ישראל'])
H['lords_portion_his_people_jacob'] = PHRASE(D, 32, 9, ['כי', 'חלק', 'יהוה', 'עמו', 'יעקב', 'חבל', 'נחלתו'])
# F4 THE DESERT AND THE EAGLE
H['found_in_the_desert_encircled_and_kept'] = PHRASE(D, 32, 10, ['ימצאהו', 'בארץ', 'מדבר', 'ובתהו', 'ילל', 'ישמן', 'יסבבנהו', 'יבוננהו']); H['apple_of_his_eye_kept'] = PHRASE(D, 32, 10, ['יצרנהו', 'כאישון', 'עינו'])
H['as_an_eagle_stirring_its_nest_borne'] = PHRASE(D, 32, 11, ['כנשר', 'יעיר', 'קנו', 'על', 'גוזליו', 'ירחף']); H['the_lord_alone_led_no_foreign_god'] = PHRASE(D, 32, 12, ['יהוה', 'בדד', 'ינחנו', 'ואין', 'עמו', 'אל', 'נכר'])
# F5 THE HEIGHTS AND THE FEAST
H['heights_of_the_land_ridden_honey_from_the_rock'] = PHRASE(D, 32, 13, ['וינקהו', 'דבש', 'מסלע', 'ושמן', 'מחלמיש', 'צור']); H['feast_of_curd_milk_fat_and_wine_given'] = PHRASE(D, 32, 14, ['חמאת', 'בקר', 'וחלב', 'צאן', 'עם', 'חלב', 'כרים'])
# F6 JESHURUN FAT AND THE DEMONS
H['jeshurun_fat_kicked_forsook_god'] = PHRASE(D, 32, 15, ['וישמן', 'ישרון', 'ויבעט', 'שמנת', 'עבית', 'כשית', 'ויטש', 'אלוה', 'עשהו']); H['demons_and_new_gods_sacrificed'] = PHRASE(D, 32, 17, ['יזבחו', 'לשדים', 'לא', 'אלה', 'אלהים', 'לא', 'ידעום'])
H['rock_that_begot_you_forgotten'] = PHRASE(D, 32, 18, ['צור', 'ילדך', 'תשי', 'ותשכח', 'אל', 'מחללך'])
# F7 THE HIDDEN FACE AND THE FIRE
H['jealousy_by_no_people_foolish_nation'] = PHRASE(D, 32, 21, ['ואני', 'אקניאם', 'בלא', 'עם', 'בגוי', 'נבל', 'אכעיסם']); H['fire_kindled_to_the_lowest_sheol'] = PHRASE(D, 32, 22, ['כי', 'אש', 'קדחה', 'באפי', 'ותיקד', 'עד', 'שאול', 'תחתית'])
# F8 THE EVILS HEAPED
H['evils_heaped_arrows_spent'] = PHRASE(D, 32, 23, ['אספה', 'עלימו', 'רעות', 'חצי', 'אכלה', 'בם']); H['hunger_beasts_serpents_sword_terror_sent'] = PHRASE(D, 32, 24, ['ושן', 'בהמות', 'אשלח', 'בם', 'עם', 'חמת', 'זחלי', 'עפר'])
# F9 THE ENEMY'S BOAST
H['blotting_out_stayed_by_the_enemys_boast'] = PHRASE(D, 32, 27, ['לולי', 'כעס', 'אויב', 'אגור', 'פן', 'ינכרו', 'צרימו']); H['nation_void_of_counsel'] = PHRASE(D, 32, 28, ['כי', 'גוי', 'אבד', 'עצות', 'המה', 'ואין', 'בהם', 'תבונה'])
# F10 THE JOINED THOUSAND AND THE VINE OF SODOM
H['one_chasing_a_thousand_rock_sold_them'] = PHRASE(D, 32, 30, ['איכה', 'ירדף', 'אחד', 'אלף', 'ושנים', 'יניסו', 'רבבה']); H['vine_of_sodom_gall_grapes'] = PHRASE(D, 32, 32, ['כי', 'מגפן', 'סדם', 'גפנם', 'ומשדמת', 'עמרה'])
# F11 THE CUP IN STORE AND THE VENGEANCE
H['vengeance_laid_up_in_store_sealed'] = PHRASE(D, 32, 34, ['הלא', 'הוא', 'כמס', 'עמדי', 'חתם', 'באוצרתי']); H['lord_judges_his_people_repents_himself'] = PHRASE(D, 32, 36, ['כי', 'ידין', 'יהוה', 'עמו', 'ועל', 'עבדיו', 'יתנחם'])
H['where_are_their_gods_asked'] = PHRASE(D, 32, 37, ['ואמר', 'אי', 'אלהימו', 'צור', 'חסיו', 'בו'])
# F12 I AM HE AND THE LAND ATONES
H['i_i_am_he_no_god_beside_me'] = PHRASE(D, 32, 39, ['ראו', 'עתה', 'כי', 'אני', 'אני', 'הוא', 'ואין', 'אלהים', 'עמדי']); H['i_kill_and_make_alive_none_delivers'] = PHRASE(D, 32, 39, ['אני', 'אמית', 'ואחיה', 'מחצתי', 'ואני', 'ארפא', 'ואין', 'מידי', 'מציל'])
H['hand_lifted_to_heaven_live_forever_sworn'] = PHRASE(D, 32, 40, ['כי', 'אשא', 'אל', 'שמים', 'ידי', 'ואמרתי', 'חי', 'אנכי', 'לעלם']); H['sword_whetted_vengeance_rendered'] = PHRASE(D, 32, 41, ['אם', 'שנותי', 'ברק', 'חרבי', 'ותאחז', 'במשפט', 'ידי', 'אשיב', 'נקם', 'לצרי'])
H['nations_sing_with_his_people_land_atones'] = PHRASE(D, 32, 43, ['הרנינו', 'גוים', 'עמו', 'כי', 'דם', 'עבדיו', 'יקום'])
# F13 THE SONG SPOKEN WITH HOSHEA
H['song_spoken_in_the_ears_of_the_people'] = PHRASE(D, 32, 44, ['ויבא', 'משה', 'וידבר', 'את', 'כל', 'דברי', 'השירה', 'הזאת', 'באזני', 'העם']); H['hoshea_speaks_the_song_beside_moses'] = PHRASE(D, 32, 44, ['הוא', 'והושע', 'בן', 'נון'])
# F14 THE CHARGE AFTER THE SONG
H['set_your_heart_to_these_words_commanded'] = PHRASE(D, 32, 46, ['שימו', 'לבבכם', 'לכל', 'הדברים', 'אשר', 'אנכי', 'מעיד', 'בכם', 'היום']); H['it_is_your_life_no_empty_matter'] = PHRASE(D, 32, 47, ['כי', 'לא', 'דבר', 'רק', 'הוא', 'מכם', 'כי', 'הוא', 'חייכם'])
# F15 THE SUMMONS TO NEBO
H['go_up_to_nebo_see_the_land_commanded'] = PHRASE(D, 32, 49, ['עלה', 'אל', 'הר', 'העברים', 'הזה', 'הר', 'נבו']); H['die_in_the_mountain_gathered_to_your_people_commanded'] = PHRASE(D, 32, 50, ['ומת', 'בהר', 'אשר', 'אתה', 'עלה', 'שמה', 'והאסף', 'אל', 'עמיך'])
H['as_aaron_died_in_hor_and_was_gathered'] = PHRASE(D, 32, 50, ['כאשר', 'מת', 'אהרן', 'אחיך', 'בהר', 'ההר', 'ויאסף', 'אל', 'עמיו'])
# F16 MERIBAH AND THE SEEING
H['trespassed_at_meribath_kadesh_not_sanctified'] = PHRASE(D, 32, 51, ['על', 'אשר', 'מעלתם', 'בי', 'בתוך', 'בני', 'ישראל', 'במי', 'מריבת', 'קדש']); H['see_the_land_from_afar_not_go_there'] = PHRASE(D, 32, 52, ['כי', 'מנגד', 'תראה', 'את', 'הארץ', 'ושמה', 'לא', 'תבוא'])
assert len(H) == 42 and set(H) == set(OWN42), (len(H), set(OWN42) - set(H), set(H) - set(OWN42))
EX = "cold_run_song_charge_nebo.py (%s %s — %s; the line %s) — THE LEAN PASS: the exam the twenty-six Mishnah and Tosefta rows the ledger cites (deu_32_haazinu_exam_2026-09-28.md)"
W20 = 'THE DEUTERONOMY WALK 20b (2026-09-28)'
