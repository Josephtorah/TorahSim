# ---- FIFTY-NINE new effects (the shelf's own words for their names and values, the `he` FOUND in the verse); the kin's effects asserted present; THE FIFTY-NINE NAMES ASSERTED ABSENT before (the holes) ----
path = f"{ROOT}/World/step9/effect_vocabulary.yaml"
text = open(path, encoding='utf-8').read()
fx = yaml.safe_load(text)['effects']
for e in list(S.KIN_UNMOVED) + list(S.REUSE_BEFORE):
    assert e in fx, e
assert fx['entered_the_covenant']['ledger_op'] == 'status' and fx['became_the_lords_people_this_day']['ledger_op'] == 'status' and fx['heaven_and_earth_witness']['ledger_op'] == 'status' and fx['blessing_and_curse_set']['ledger_op'] == 'status' and fx['cleaving_commanded']['ledger_op'] == 'status' and fx['fear_not_promised']['ledger_op'] == 'heaven' and fx['glory_appeared']['ledger_op'] == 'heaven' and fx['barred_from_the_land']['ledger_op'] == 'heaven' and fx['reprieve_of_a_hundred_and_twenty']['ledger_op'] == 'timer', 'the reused and referenced rows\' ops'
OWN59 = tuple(S.NEW_EFFECTS)
assert len(OWN59) == 59 and len(set(OWN59)) == 59
HOLE0 = sorted(k for k in fx if k in OWN59)
NEAR0 = sorted(k for k in fx if k not in OWN59 and any(t in k for t in ('covenant_words', 'standing_before', 'covenant_oath', 'not_here', 'heart_turning', 'self_blessing', 'unpardoned', 'idolater', 'blotted', 'separated', 'brimstone', 'nations_question', 'uprooted', 'hidden_things', 'revealed', 'captivity', 'gathered', 'multiplied_above', 'heart_circumcised', 'curses_put', 'abounding', 'rejoiced_over', 'commandment_', 'life_and_death', 'choose_life', 'living_and', 'perishing_for', 'length_of_days', 'joshua_', 'be_strong', 'nations_dispossessed', 'law_written', 'hakhel', 'moses_days', 'moses_to_sleep', 'whoring', 'covenant_breaking', 'face_hidden', 'evils_and', 'song_', 'lord_with_joshua', 'book_', 'elders_and_officers', 'corruption_after')))
print('the registry\'s effects among the fifty-nine before this sitting:', HOLE0, '| the near effects on file (not ours):', NEAR0)
assert HOLE0 == [] or HOLE0 == sorted(OWN59), HOLE0   # THE HOLES — the fifty-nine names absent before this sitting (the recon measured them absent) — or this sitting's own, written by the first run (idempotent)
# THE HEBREW FOUND IN THE VERSES — the plain tokens typed from the 78 verses' print at RUN B's head; PHRASE refuses two hits or none
H = {}
# F1 THE MOAB RECITAL
H['covenant_words_keeping_commanded'] = PHRASE(D, 29, 8, ['ושמרתם', 'את', 'דברי', 'הברית', 'הזאת'])
# F2 THE COVENANT AND THE OATH
H['standing_before_the_lord_this_day'] = PHRASE(D, 29, 9, ['אתם', 'נצבים', 'היום', 'כלכם', 'לפני', 'יהוה', 'אלהיכם']); H['covenant_oath_sworn_this_day'] = PHRASE(D, 29, 11, ['לעברך', 'בברית', 'יהוה', 'אלהיך', 'ובאלתו'])
H['covenant_with_those_not_here'] = PHRASE(D, 29, 14, ['ואת', 'אשר', 'איננו', 'פה', 'עמנו', 'היום'])
# F3 THE INDIVIDUAL'S CURSE
H['heart_turning_to_other_gods_barred'] = PHRASE(D, 29, 17, ['אשר', 'לבבו', 'פנה', 'היום', 'מעם', 'יהוה', 'אלהינו']); H['stubborn_self_blessing_barred'] = PHRASE(D, 29, 18, ['והתברך', 'בלבבו', 'לאמר', 'שלום', 'יהיה', 'לי'])
H['hidden_idolater_unpardoned'] = PHRASE(D, 29, 19, ['לא', 'יאבה', 'יהוה', 'סלח', 'לו']); H['curses_of_the_book_on_the_idolater'] = PHRASE(D, 29, 19, ['ורבצה', 'בו', 'כל', 'האלה', 'הכתובה', 'בספר', 'הזה'])
H['name_blotted_from_under_heaven'] = PHRASE(D, 29, 19, ['ומחה', 'יהוה', 'את', 'שמו', 'מתחת', 'השמים']); H['separated_for_evil_from_all_tribes'] = PHRASE(D, 29, 20, ['והבדילו', 'יהוה', 'לרעה', 'מכל', 'שבטי', 'ישראל'])
# F4 THE LAND'S DESOLATION
H['land_brimstone_salt_like_sodom'] = PHRASE(D, 29, 22, ['גפרית', 'ומלח', 'שרפה', 'כל', 'ארצה']); H['nations_question_answered_covenant_forsaken'] = PHRASE(D, 29, 24, ['ואמרו', 'על', 'אשר', 'עזבו', 'את', 'ברית', 'יהוה'])
H['uprooted_and_cast_into_another_land'] = PHRASE(D, 29, 27, ['ויתשם', 'יהוה', 'מעל', 'אדמתם'])
# F5 THE HIDDEN AND THE REVEALED
H['hidden_things_the_lords'] = PHRASE(D, 29, 28, ['הנסתרת', 'ליהוה', 'אלהינו']); H['revealed_things_ours_to_do'] = PHRASE(D, 29, 28, ['והנגלת', 'לנו', 'ולבנינו', 'עד', 'עולם'])
# F6 THE RETURN AND THE GATHERING
H['return_to_the_lord_the_condition'] = PHRASE(D, 30, 2, ['ושבת', 'עד', 'יהוה', 'אלהיך', 'ושמעת', 'בקלו']); H['captivity_returned_on_return'] = PHRASE(D, 30, 3, ['ושב', 'יהוה', 'אלהיך', 'את', 'שבותך', 'ורחמך'])
H['gathered_from_all_the_peoples'] = PHRASE(D, 30, 3, ['ושב', 'וקבצך', 'מכל', 'העמים']); H['gathered_from_the_end_of_heaven'] = PHRASE(D, 30, 4, ['אם', 'יהיה', 'נדחך', 'בקצה', 'השמים'])
H['brought_into_the_fathers_land_again'] = PHRASE(D, 30, 5, ['והביאך', 'יהוה', 'אלהיך', 'אל', 'הארץ', 'אשר', 'ירשו', 'אבתיך']); H['multiplied_above_the_fathers'] = PHRASE(D, 30, 5, ['והיטבך', 'והרבך', 'מאבתיך'])
# F7 THE HEART CIRCUMCISED
H['heart_circumcised_by_the_lord'] = PHRASE(D, 30, 6, ['ומל', 'יהוה', 'אלהיך', 'את', 'לבבך']); H['curses_put_on_the_enemies'] = PHRASE(D, 30, 7, ['ונתן', 'יהוה', 'אלהיך', 'את', 'כל', 'האלות', 'האלה', 'על', 'איביך'])
H['return_and_hearken_and_do_commanded'] = PHRASE(D, 30, 8, ['ואתה', 'תשוב', 'ושמעת', 'בקול', 'יהוה']); H['abounding_in_fruit_of_body_cattle_ground'] = PHRASE(D, 30, 9, ['והותירך', 'יהוה', 'אלהיך', 'בכל', 'מעשה', 'ידך'])
H['rejoiced_over_as_over_the_fathers'] = PHRASE(D, 30, 9, ['כי', 'ישוב', 'יהוה', 'לשוש', 'עליך', 'לטוב'])
# F8 THE COMMANDMENT NEAR
H['commandment_not_too_hard_nor_far'] = PHRASE(D, 30, 11, ['לא', 'נפלאת', 'הוא', 'ממך', 'ולא', 'רחקה', 'הוא']); H['commandment_not_in_heaven_nor_beyond_the_sea'] = PHRASE(D, 30, 12, ['לא', 'בשמים', 'הוא'])
H['commandment_in_mouth_and_heart_to_do'] = PHRASE(D, 30, 14, ['כי', 'קרוב', 'אליך', 'הדבר', 'מאד', 'בפיך', 'ובלבבך', 'לעשתו'])
# F9 LIFE AND DEATH
H['life_and_death_set_before_israel'] = PHRASE(D, 30, 15, ['ראה', 'נתתי', 'לפניך', 'היום', 'את', 'החיים', 'ואת', 'הטוב', 'ואת', 'המות', 'ואת', 'הרע']); H['choose_life_commanded'] = PHRASE(D, 30, 19, ['ובחרת', 'בחיים', 'למען', 'תחיה', 'אתה', 'וזרעך'])
H['living_and_multiplying_for_hearkening'] = PHRASE(D, 30, 16, ['וחיית', 'ורבית', 'וברכך', 'יהוה', 'אלהיך']); H['perishing_for_turning_away'] = PHRASE(D, 30, 18, ['הגדתי', 'לכם', 'היום', 'כי', 'אבד', 'תאבדון'])
H['length_of_days_on_the_land_promised'] = PHRASE(D, 30, 20, ['כי', 'הוא', 'חייך', 'וארך', 'ימיך'])
# F10 THE CHARGE AND THE CROSSING
H['joshua_to_cross_before_israel'] = PHRASE(D, 31, 3, ['יהושע', 'הוא', 'עבר', 'לפניך', 'כאשר', 'דבר', 'יהוה']); H['nations_dispossessed_as_sihon_and_og_promised'] = PHRASE(D, 31, 4, ['ועשה', 'יהוה', 'להם', 'כאשר', 'עשה', 'לסיחון', 'ולעוג'])
H['be_strong_and_courageous_commanded'] = PHRASE(D, 31, 6, ['חזקו', 'ואמצו', 'אל', 'תיראו', 'ואל', 'תערצו', 'מפניהם']); H['joshua_charged_to_bring_israel_in'] = PHRASE(D, 31, 7, ['כי', 'אתה', 'תבוא', 'את', 'העם', 'הזה', 'אל', 'הארץ'])
# F11 THE LAW WRITTEN AND THE HAKHEL
H['law_written_and_given_to_priests_and_elders'] = PHRASE(D, 31, 9, ['ויכתב', 'משה', 'את', 'התורה', 'הזאת', 'ויתנה', 'אל', 'הכהנים', 'בני', 'לוי']); H['hakhel_reading_commanded'] = PHRASE(D, 31, 11, ['תקרא', 'את', 'התורה', 'הזאת', 'נגד', 'כל', 'ישראל', 'באזניהם'])
H['hakhel_assembly_of_all_commanded'] = PHRASE(D, 31, 12, ['הקהל', 'את', 'העם', 'האנשים', 'והנשים', 'והטף', 'וגרך', 'אשר', 'בשעריך']); H['hakhel_children_hear_and_learn_commanded'] = PHRASE(D, 31, 13, ['ובניהם', 'אשר', 'לא', 'ידעו', 'ישמעו', 'ולמדו'])
# F12 THE TENT AND THE COMMISSION
H['moses_days_approach_to_die'] = PHRASE(D, 31, 14, ['הן', 'קרבו', 'ימיך', 'למות']); H['joshua_commissioned_to_bring_israel_in'] = PHRASE(D, 31, 23, ['כי', 'אתה', 'תביא', 'את', 'בני', 'ישראל', 'אל', 'הארץ', 'אשר', 'נשבעתי', 'להם'])
H['lord_with_joshua_promised'] = PHRASE(D, 31, 23, ['ואנכי', 'אהיה', 'עמך'])
# F13 THE APOSTASY FORETOLD
H['moses_to_sleep_with_the_fathers'] = PHRASE(D, 31, 16, ['הנך', 'שכב', 'עם', 'אבתיך']); H['future_whoring_after_foreign_gods_foretold'] = PHRASE(D, 31, 16, ['וקם', 'העם', 'הזה', 'וזנה', 'אחרי', 'אלהי', 'נכר', 'הארץ'])
H['covenant_breaking_foretold'] = PHRASE(D, 31, 16, ['ועזבני', 'והפר', 'את', 'בריתי', 'אשר', 'כרתי', 'אתו']); H['face_hidden_and_forsaken_foretold'] = PHRASE(D, 31, 17, ['ועזבתים', 'והסתרתי', 'פני', 'מהם'])
H['evils_and_troubles_befall_foretold'] = PHRASE(D, 31, 17, ['ומצאהו', 'רעות', 'רבות', 'וצרות'])
# F14 THE SONG COMMANDED
H['song_writing_commanded'] = PHRASE(D, 31, 19, ['ועתה', 'כתבו', 'לכם', 'את', 'השירה', 'הזאת']); H['song_taught_and_put_in_mouths_commanded'] = PHRASE(D, 31, 19, ['ולמדה', 'את', 'בני', 'ישראל', 'שימה', 'בפיהם'])
H['song_a_witness_against_israel'] = PHRASE(D, 31, 19, ['למען', 'תהיה', 'לי', 'השירה', 'הזאת', 'לעד', 'בבני', 'ישראל']); H['song_written_and_taught_by_moses'] = PHRASE(D, 31, 22, ['ויכתב', 'משה', 'את', 'השירה', 'הזאת', 'ביום', 'ההוא', 'וילמדה', 'את', 'בני', 'ישראל'])
# F15 THE BOOK BESIDE THE ARK AND THE ASSEMBLY
H['book_of_the_law_beside_the_ark_commanded'] = PHRASE(D, 31, 26, ['לקח', 'את', 'ספר', 'התורה', 'הזה', 'ושמתם', 'אתו', 'מצד', 'ארון', 'ברית', 'יהוה', 'אלהיכם']); H['book_a_witness_against_israel'] = PHRASE(D, 31, 26, ['והיה', 'שם', 'בך', 'לעד'])
H['elders_and_officers_assembled_commanded'] = PHRASE(D, 31, 28, ['הקהילו', 'אלי', 'את', 'כל', 'זקני', 'שבטיכם', 'ושטריכם']); H['corruption_after_moses_death_foretold'] = PHRASE(D, 31, 29, ['כי', 'ידעתי', 'אחרי', 'מותי', 'כי', 'השחת', 'תשחתון'])
H['song_spoken_to_the_assembly_to_its_end'] = PHRASE(D, 31, 30, ['וידבר', 'משה', 'באזני', 'כל', 'קהל', 'ישראל', 'את', 'דברי', 'השירה', 'הזאת', 'עד', 'תמם'])
assert len(H) == 59 and set(H) == set(OWN59), (len(H), set(OWN59) - set(H), set(H) - set(OWN59))
EX = "cold_run_covenant_return_charge.py (%s %s — %s; the line %s) — THE LEAN PASS: the exam the seven Mishnah and Tosefta rows the ledger cites (deu_29_31_nitzavim_vayelech_exam_2026-09-27.md)"
W19 = 'THE DEUTERONOMY WALK 19b (2026-09-27)'
