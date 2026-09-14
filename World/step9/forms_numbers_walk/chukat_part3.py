
# ---- the retellings and the echoes, computed on the ink (F3-F6's crowns) ----
THEN_SANG = sorted(k for k, ws in _BYV.items() if any(ws[i] == 'אז' and ws[i + 1] == 'ישיר' for i in range(len(ws) - 1)))
assert THEN_SANG == [('Exod', 15, 1), ('Num', 21, 17)], THEN_SANG                 # "then sang" — the sea's and the well's
LAWGIVER = seats_of('מחקק') + seats_of('במחקק') + seats_of('ומחקק'); assert set(('Gen 49:10', 'Num 21:18', 'Deut 33:21')) <= set(LAWGIVER), LAWGIVER
SURVIVOR = sorted(('%s %d:%d' % k) for k, ws in _BYV.items() if any(ws[i] == 'בלתי' and ws[i + 1] == 'השאיר' for i in range(len(ws) - 1)))
assert set(('Num 21:35', 'Deut 3:3', 'Josh 8:22', 'Josh 10:33', '2Kgs 10:11')) <= set(SURVIVOR), SURVIVOR   # "until no survivor was left" — Joshua's refrain born here
def delta(a, b):
    A, B = verse_text(*a[1:], book=a[0]).split(), verse_text(*b[1:], book=b[0]).split()
    return [w for w in A if w not in B], [w for w in B if w not in A]
D33 = delta(('Num', 21, 33), ('Deut', 3, 1)); D34 = delta(('Num', 21, 34), ('Deut', 3, 2)); D35 = delta(('Num', 21, 35), ('Deut', 3, 3))
assert D33 == (['ויפנו', 'ויעלו', 'לקראתם'], ['ונפן', 'ונעל', 'לקראתנו']) and D34[0] == ['משה'] and D34[1] == ['אלי'], (D33, D34)   # Deut 3 = 21:33-35 with the pronouns shifted
JER = set(verse_text(48, 45, book='Jer').split()) & set(verse_text(21, 28).split()); assert JER == {'כי', 'אש', 'מחשבון', 'מואב'}, JER   # Jeremiah 48:45 quotes 21:28 with FOUR exact tokens ("for a fire", "from Heshbon", "Moab") — the rest shifted in spelling (read off the assert driver, 2026-09-11: the hand had typed >= 5, and had reversed chapter and verse in five calls)
MERIBAH_17 = set(verse_text(17, 2, book='Exod').split()) | set(verse_text(17, 3, book='Exod').split())
FIRST_MERIBAH_CLAUSES = [w for w in ('וירב', 'העליתנו', 'ממצרים') if w in verse_text(20, 3).split() + verse_text(20, 5).split() and w in MERIBAH_17]
assert FIRST_MERIBAH_CLAUSES == ['וירב', 'העליתנו', 'ממצרים'], FIRST_MERIBAH_CLAUSES   # the first Meribah's clauses at the second
FIRSTFRUITS = [w for w in ('ונצעק', 'וירעו') if w in verse_text(20, 15).split() + verse_text(20, 16).split()]
assert 'ונצעק' in FIRSTFRUITS and 'ונצעק' in verse_text(26, 7, book='Deut').split(), FIRSTFRUITS   # "and we cried" — Deut 26:7's clause in the Edom letter

# ===== F3: MIRIAM'S DEATH AND THE WATERS OF MERIBAH (Num 20:1-13) ==========================================
def meribah(case, data):
    del P[:]
    ask = case['ask']
    if ask == 'well_by_merit':
        ink('20:1-2', '"and Miriam died there... and there was no water for the congregation" — the two verses adjacent')
        dat('the row well_by_merit: %s' % data['well_by_merit']['value'])
        return out('the well gone at Miriam\'s death, returned by Moses\' and Aaron\'s merit (Taanit 9a; Seder Olam 10:2)', [FX.NONE])
    if ask == 'death_by_the_kiss':
        dat('the row death_by_the_kiss: %s' % data['death_by_the_kiss']['value'])
        return out('Miriam too by the kiss — "there" / "there" with Deut 34:5 (Bava Batra 17a)', [FX.NONE])
    if ask == 'burial_near_death':
        ink('20:1', '"and Miriam died there and was BURIED there" — Deborah\'s (Gen 35:8) and Rachel\'s (35:19) formula')
        move('Moed Katan 28a:2', 'buried near where she died; a woman\'s bier not set down in the street (R. Elazar)')
        return out('buried near the death — the woman\'s bier not set down in the street (Moed Katan 28a)', ['buried'])
    if ask == 'there_there':
        ink('20:1', '"died THERE" — with Deut 21:4\'s "there" (the eglah arufah)')
        move('Avodah Zarah 29b:12; Sanhedrin 47b:17', 'benefit from a corpse forbidden by the analogy; Abaye: by designation')
        return out('benefit from a corpse forbidden — "there" / "there" with the eglah arufah (Avodah Zarah 29b; Sanhedrin 47b)', [FX.NONE])
    if ask == 'astrologers':
        ink('20:13', '"THESE are the waters of Meribah"')
        move('Sanhedrin 101b:10; Sotah 12b:14', "the waters Pharaoh's astrologers saw and erred on — the savior stricken by water: Meribah, not the Nile")
        return out('the astrologers\' waters — Meribah, not the Nile (Sanhedrin 101b; Sotah 12b)', [FX.NONE])
    if ask == 'quarrel_with_teacher':
        ink('20:13', '"where the children of Israel strove WITH THE LORD" — the quarrel was with Moses')
        move('Sanhedrin 110a:9', 'who quarrels with his teacher quarrels with the Presence (R. Chama b. R. Chanina)')
        return out('a quarrel with the teacher is a quarrel with the Presence (Sanhedrin 110a)', [FX.NONE])
    if ask == 'cattle_water':
        ink('20:8', '"give drink to the congregation AND THEIR CATTLE"')
        move('Menachot 76b:13', 'the Torah spared Israel\'s money — the miracle even for the livestock (R. Elazar)')
        return out('the cattle included — the Torah spared Israel\'s money (Menachot 76b)', ['water_from_the_rock'])
    if ask == 'struck_twice':
        ink('20:11', '"and he struck the rock with his staff TWICE" — the dual read %s by the taught parser (rule 19; Gen 27:36, 41:32, 43:10 its kin %s)' % (TWICE, TWICE_KIN))
        return out('struck twice — [2] by the parser (20:11); much water came out', ['water_from_the_rock'])
    if ask == 'sin':
        ink('20:8, 20:11-12', 'SPEAK commanded (20:8); STRUCK twice done (20:11); "because you did not believe in Me, to sanctify Me" (20:12)')
        dat('the row meribah_sin: %s' % data['meribah_sin']['value'])
        move('Shabbat 55b:2; Yoma 86b:15, 87a:3; Ps 106:32-33', 'even Moses and Aaron died for their sin; Moses asked his disgrace written; "he spoke rashly with his lips"')
        return out('the spec\'s SPEAK, the run\'s STRUCK TWICE — the sin the ink\'s own delta; the rash speech the Psalm\'s (20:8-12; Ps 106:33)', [FX.NONE])
    if ask == 'died_for_sin':
        move('Shabbat 55b:2; Yoma 87a:3', 'R. Shimon b. Elazar: had you believed, your time had not yet come — even Moses and Aaron died for their sin')
        return out('died for their sin — had they believed, their time had not come (Shabbat 55b; Yoma 87a)', ['barred_from_the_land'])
    if ask == 'disgrace_written':
        move('Yoma 86b:15', 'Moses: let my disgrace be written (20:12); David: hidden (Ps 32:1)')
        return out('Moses\' disgrace written explicitly at 20:12 (Yoma 86b)', [FX.NONE])
    if ask == 'sentence':
        ink('20:12', '"therefore you shall not bring this assembly into the land which I have given them" — the frame to Moses AND Aaron; 20:24, 27:14, Deut 32:51 the run citations')
        return out('barred from the land — Moses and Aaron; Aaron\'s closed at 20:28, Moses\' at Deut 34 (20:12)', ['barred_from_the_land'])
    if ask == 'miriam_day':
        ink('20:1', '"in the first month" — the ordinal reader\'s %s; no day, no year in the ink' % FIRST_MONTH)
        dat('the row miriam_death_day: %s' % data['miriam_death_day']['value'])
        return out('the tenth of Nisan (Seder Olam 10:2); the arrival on the new moon (9:2) — the tape\'s marker on the first, the row\'s arm the tenth', [FX.NONE])
    if ask == 'meribah_seats':
        ink('20:13, 20:24, 27:14; Exod 17:7; Deut 32:51, 33:8; Ps 81:8, 95:8, 106:32; Ezek 47:19, 48:28', 'the Meribah-word\'s seats in the five books (computed): %s — Gen 13:8\'s "strife" the named homograph, not counted' % MERIBAH_SEATS)
        return out('Meribah at %d seats — Exod 17:7 the first, Num 20:13 the second (computed)' % len(MERIBAH_SEATS), [FX.NONE])
    if ask == 'first_meribah_clauses':
        ink('20:3, 20:5; Exod 17:2-3', 'the first Meribah\'s clauses at the second (computed): %s — "the people strove", "why did you bring us up from Egypt"' % FIRST_MERIBAH_CLAUSES)
        return out('Exod 17:2-3\'s clauses at Num 20:3-5 — strove, brought up, from Egypt (computed)', ['gathered_against'])
    if ask == 'rebels_skin':
        ink('20:10', '"hear now, you REBELS" — one consonantal skin with Miriam\'s name (20:1) and Marah\'s waters (Exod 15:23), told by the points (the reading\'s crown)')
        return out('the rebels, Miriam and the bitter waters — one consonantal skin, three words (20:10)', [FX.NONE])
    return out('no verdict in span', [FX.NONE])


# ===== F4: EDOM, MOUNT HOR, THE SUCCESSION AND THE MOURNING (Num 20:14-29) ================================
def edom_and_hor(case, data):
    del P[:]
    ask = case['ask']
    if ask == 'arad_heard':
        ink('20:29; 21:1; 33:40', '"and all the congregation SAW that Aaron was dead" — "the Canaanite king of Arad heard"')
        dat('the row arad_heard: %s' % data['arad_heard']['value'])
        return out('Arad heard that Aaron died and the clouds departed (Rosh Hashanah 3a; Taanit 9a) — the attack during the mourning', [FX.NONE])
    if ask == 'death_dates':
        ink('33:38-39', '"in the fortieth year, in the fifth month, on the first of the month" — read whole by the parser: %s; his age %s' % (AARON_DATE, AARON_AGE))
        dat('the rows miriam_death_day: %s; deaths_ceased: %s' % (data['miriam_death_day']['value'], data['deaths_ceased']['value']))
        move('Seder Olam Rabbah 10:2', 'Miriam the tenth of Nisan, Aaron the first of Av, Moses the seventh of Adar — one year, not one month (Zech 11:8)')
        return out('Aaron (40, 5, 1) by the ink, aged 123; Miriam the tenth of Nisan by the shelf; Moses the seventh of Adar (33:38-39; Seder Olam 10:2)', [FX.NONE])
    if ask == 'seder_olam_walk':
        dat('the row moserah: %s' % data['moserah']['value'])
        move('Seder Olam Rabbah 9:2', 'the new moon of Nisan at Zin; three months at Kadesh; Aaron at 123; the clouds departed, Arad came; the retreat of seven stations to Moserah; Gudgod, Beer, Oboth, Iye-abarim, Zered, beyond Arnon, Sihon, Og, Arvot Moab, the plague, the census, the daughters')
        return out('the fortieth year\'s walk: (40, 1, 1) the arrival, three months at Kadesh, Aaron\'s death, the retreat to Moserah, the daughters after the conquest (Seder Olam 9:2)', [FX.NONE])
    if ask == 'moserah':
        ink('20:28; Deut 10:6', '"Aaron died there on the top of the mountain" / "at Moserah there Aaron died" — the DIVERGE')
        dat('the row moserah: %s' % data['moserah']['value'])
        return out('Moserah — the retreat of seven stations after Arad\'s attack, the mourning renewed there (Seder Olam 9:2); the death at Mount Hor (20:28)', [FX.NONE])
    if ask == 'succession':
        ink('20:26, 20:28', '"strip Aaron of his garments and put them on Eleazar his son" — Exod 29:29-30\'s spec RUN')
        dat('the row succession_by: %s' % data['succession_by']['value'])
        move('CALLED cold_run_vestments.investiture(substitute) -> %s; cold_run_priesthood.family(one_hour) -> %s; family(high_priest_dead) -> %s [IMPORT, live]' % (VS_SUBSTITUTE, PR_HOUR, PR_HP_DEAD), "the garments transferable to the son after him; the office attaches at the pouring — here at the dressing; the high priest's mourning rows")
        return out('the garments to Eleazar and the office with them — Exod 29:29-30 run at Mount Hor (20:26-28)', ['garments_transferred', 'invested_office', 'gathered_to_his_people'])
    if ask == 'thirty_days':
        ink('20:29', '"they wept for Aaron thirty days, all the house of Israel" — the parser\'s %s; Moses\' %s at Deut 34:8' % (DAYS30, MOSES_MOURNED))
        dat('the row aaron_mourned_by_all: %s' % data['aaron_mourned_by_all']['value'])
        return out('thirty days\' weeping by all the house of Israel — a timer due (40, 6, 1) (20:29; Deut 34:8 Moses\' thirty)', [FX.NONE])
    if ask == 'edom_passage':
        ink('20:18, 20:20-21', '"you shall not pass through me" twice; "and Israel turned away from him"')
        dat('the row edom_passage: %s' % data['edom_passage']['value'])
        return out('Edom refused twice and Israel turned away (20:18-21); Deut 2:28-29\'s purchase the other arm — DISPUTE', ['refused'])
    if ask == 'two_messages':
        ink('20:17; 21:22', 'the Edom letter\'s request and Sihon\'s — %d shared tokens (computed): %s' % (len(SHARED_MSG), SHARED_MSG))
        return out('thirteen tokens shared between the Edom and Sihon messages (20:17; 21:22 — computed)', [FX.NONE])
    if ask == 'two_mount_hors':
        ink('20:22-27, 21:4, 33:37-41; 34:7-8', 'Mount Hor at the border of Edom (Aaron\'s) and Mount Hor of the northern border — two')
        return out('two Mount Hors — Aaron\'s at Edom\'s border, the northern border\'s (34:7-8)', [FX.NONE])
    if ask == 'aaron_age':
        ink('33:39', '"a hundred and twenty-three years" — %s by the parser' % AARON_AGE)
        return out('Aaron 123 at his death (33:39 — [123])', [FX.NONE])
    if ask == 'firstfruits_clauses':
        ink('20:15-16; Deut 26:6-7', '"the Egyptians did evil to us... and we CRIED to the LORD" — the firstfruits declaration\'s two clauses in the Edom letter (computed: %s; "and we cried" at Deut 26:7 too)' % FIRSTFRUITS)
        return out('the firstfruits declaration\'s clauses in the Edom letter — "and we cried to the LORD" at Num 20:16 and Deut 26:7 alone', ['plea_made'])
    if ask == 'messengers_word':
        ink('20:14, 20:16', '"messengers" (the men) and "a messenger" (the LORD\'s) — one noun; Onkelos ENVOYS for the men, the ANGEL kept')
        return out('one noun, two translations — envoys for Moses\' men, the angel for the LORD\'s (20:14, 20:16)', [FX.NONE])
    return out('no verdict in span', [FX.NONE])


# ===== F5: ARAD, THE VOW, THE SERPENTS AND THE POLE (Num 21:1-9) ==========================================
def arad_and_the_serpent(case, data):
    del P[:]
    ask = case['ask']
    if ask == 'captive_acquired':
        ink('21:1', '"and took some of them captive"')
        dat('the row captive_count: %s' % data['captive_count']['value'])
        move('Gittin 38a:4', 'a gentile acquires a Jew by conquest — an act of possession')
        return out('acquired by conquest — a gentile acquires a Jew by possession (Gittin 38a); the shelf\'s one maidservant', ['taken_captive'])
    if ask == 'vow_form':
        ink('21:2', '"if You will indeed give this people into my hand, I will devote their cities" — Jacob\'s (Gen 28:20) and Jephthah\'s (Judg 11:30) form')
        dat('the row cherem_law: %s' % data['cherem_law']['settings']['vow_form'])
        move('Eruvin 64b:3', 'one who wishes to succeed sanctifies a portion for Heaven')
        return out('the conditional vow — a portion sanctified for success (21:2; Eruvin 64b)', ['cherem_vowed'])
    if ask == 'cherem_law':
        ink('21:3', '"and he devoted them and their cities" — Onkelos DESTROYED')
        dat('the row cherem_law: %s' % data['cherem_law']['value'])
        move('CALLED cold_run_temurah.devote(status) -> %s; devote(person) -> %s [IMPORT, live]' % (TM_DEVOTE, TM_PERSON), "Lev 27:28-29's devotion: most holy, not sold, not redeemed; a person devoted put to death")
        return out('the cherem executed — the devoted not redeemed, the persons put to death (21:3; Lev 27:28-29 by the temurah engine)', ['destroyed'])
    if ask == 'hormah':
        ink('21:3; 14:45', '"and he called the name of the place Hormah" — the proleptic name\'s naming; 14:45\'s use six chapters before (CF9\'s row)')
        return out('Hormah named at 21:3 after its use at 14:45 — the proleptic name closed; Judg 1:17 the second naming', ['hormah_named'])
    if ask == 'turn_back':
        ink('21:4; 14:25', '"they journeyed from Mount Hor by the way of the Red Sea" — 14:25\'s "tomorrow turn and journey by the way of the Red Sea" RUN; Deut 2:1')
        return out('14:25\'s turn-back run at 21:4 — the open debit closed (CF8)', [FX.NONE])
    if ask == 'light_bread':
        ink('21:5', '"our soul loathes the light bread" — the manna (Onkelos: this manna whose food is light)')
        dat('the row manna_absorbed: %s' % data['manna_absorbed']['value'])
        return out('the manna called light — absorbed in the limbs (Yoma 75a); ingrates (Avodah Zarah 5b)', ['confessed'])
    if ask == 'spoke_against':
        ink('21:5', '"and the people spoke against God and against Moses"')
        move('Sanhedrin 110a:10', 'who suspects his teacher suspects the Presence — God and Moses likened (R. Abbahu)')
        return out('against God and against Moses likened — suspecting the teacher (Sanhedrin 110a)', ['confessed'])
    if ask == 'bite_and_burn':
        ink('21:6', '"the FIERY serpents... and they BIT the people" — the burn-word the heifer\'s (19:5); the bite usury\'s verb (Deut 23:20)')
        return out('the fiery serpents — the heifer\'s burn-word, usury\'s bite (21:6)', ['serpents_sent'])
    if ask == 'singular_serpent':
        ink('21:6-7, 21:9', '"the serpents" plural (21:6), "the serpent" singular (21:7, 21:9) — the reading\'s measurement')
        return out('the serpents sent, the serpent removed — plural then singular (21:6-9)', [FX.NONE])
    if ask == 'pole_word':
        ink('21:8-9; Exod 17:15; Num 26:10', '"a POLE" — YHWH-nissi\'s word and Korach\'s sign\'s; Onkelos one Aramaic word (את, "a sign"); Deut 34:7 / 4:42 the homographs "fled" / "to flee"')
        return out('the pole-word — the banner of Exod 17:15 and the sign of 26:10 (21:8-9)', [FX.NONE])
    if ask == 'serpent_property':
        ink('21:8', '"make YOU" — from Moses\' own property')
        dat('the row nehushtan: %s' % data['nehushtan']['value'])
        move('Avodah Zarah 44a:7', 'a person does not render forbidden what is not his — the worshipped serpent no idol by right')
        return out('Moses\' own serpent — not an idol by right, its worship notwithstanding (Avodah Zarah 44a)', ['set_on_the_pole'])
    if ask == 'serpent_heals':
        ink('21:8-9', '"everyone bitten who sees it shall live... he looked at the copper serpent and lived" — the look that killed Lot\'s wife (Gen 19:26)')
        dat('the row serpent_kills_or_heals: %s' % data['serpent_kills_or_heals']['value'])
        move('Mishnah Rosh Hashanah 3:8; Rosh Hashanah 29a:7', 'does the serpent kill or give life? the heart subjected to the Father in heaven — with Moses\' hands at Amalek')
        return out('the serpent neither kills nor heals — the heart subjected to Heaven heals (Mishnah Rosh Hashanah 3:8)', ['healed'])
    if ask == 'nehushtan':
        ink('21:9; 2 Kgs 18:4', 'the object\'s run ends at Hezekiah — "he broke in pieces the copper serpent that Moses had made... and he called it Nehushtan"')
        dat('the row nehushtan: %s' % data['nehushtan']['value'])
        return out('Nehushtan — broken by Hezekiah, the Sages agreed (2 Kgs 18:4; Berakhot 10b; Pesachim 56a)', [FX.NONE])
    return out('no verdict in span', [FX.NONE])


# ===== F6: THE STATIONS, THE WELL, SIHON AND OG (Num 21:10-35) ============================================
def well_and_kings(case, data):
    del P[:]
    ask = case['ask']
    if ask == 'zered_date':
        ink('21:12; Deut 2:14', '"and camped at the brook Zered" — Deut 2:14: "the days we walked from Kadesh-barnea until we crossed the brook Zered were THIRTY-EIGHT years" — the parser\'s %s; the decree\'s due (40, 5, 9) = %s' % (THIRTY_EIGHT, EX0.date(D_DUE38)))
        dat('the row deaths_ceased: %s' % (data['deaths_ceased']['value'],))
        return out('the Zered crossed after the thirty-eight years (Deut 2:14 — [38]); the timer due (40, 5, 9), the dying ceased the fifteenth of Av by the shelf, the crossing after the mourning by the text', [FX.NONE])
    if ask == 'book_of_wars':
        ink('21:14-15', '"therefore it is said in the Book of the Wars of the LORD: Vaheb in Suphah and the brooks of Arnon"')
        move('Bava Batra 14b; Kiddushin 30b:2; Moed Katan 25b:2', 'the book named; Vahev love at the end; the phrase in a eulogy')
        return out('the Book of the Wars of the LORD cited — the unnamed book\'s one citation (21:14)', [FX.NONE])
    if ask == 'arnon_miracle':
        dat('the row arnon_miracle: %s' % data['arnon_miracle']['value'])
        return out('the mountains met over the Emorites, the blood ran to the Arnon, the lepers saw and Israel sang (Berakhot 54a-b)', [FX.NONE])
    if ask == 'then_sang':
        ink('21:17; Exod 15:1', '"THEN SANG Israel this song" — the sea\'s formula at its second seat (computed: %s); "answer it" Miriam\'s verb (15:21)' % [('%s %d:%d' % k) for k in THEN_SANG])
        return out('"then sang" at two seats — the sea and the well (Exod 15:1; Num 21:17)', ['well_given'])
    if ask == 'lawgiver':
        ink('21:18; Gen 49:10; Deut 33:21', '"with the LAWGIVER, with their staffs" — Judah\'s word (Onkelos SCRIBES at both): %s' % LAWGIVER)
        return out('the lawgiver — Judah\'s word at Gen 49:10, the well\'s at 21:18, Gad\'s at Deut 33:21 (Onkelos: the scribes)', [FX.NONE])
    if ask == 'well_mouth':
        move('Mishnah Avot 5:6', 'the mouth of the well the second of the ten created at twilight')
        return out('the well\'s mouth created at twilight — the second of the ten (Avot 5:6)', [FX.NONE])
    if ask == 'mattanah_reading':
        ink('21:18-20', '"from the wilderness Mattanah, from Mattanah Nahaliel, from Nahaliel Bamoth, from Bamoth the valley... Pisgah" — Mattanah 18:6-7\'s gift-word')
        dat('the row well_song_reading: %s' % data['well_song_reading']['value'])
        return out('the stations as the Torah\'s ladder — the gift, the inheritance, the heights, the valley (Nedarim 55a; Eruvin 54a)', [FX.NONE])
    if ask == 'from_his_hand':
        ink('21:26', '"and taken all his land FROM HIS HAND as far as Arnon"')
        move('Bava Metzia 56b:4, 56b:7', "'his hand' here means his possession — the one seat where it cannot be the hand")
        return out('"from his hand" = from his possession (Bava Metzia 56b)', [FX.NONE])
    if ask == 'sihon_purified':
        ink('21:26', '"Heshbon was the city of Sihon who had fought against the former king of Moab and taken all his land" — the apparently needless verse')
        dat('the row sihon_purified: %s' % data['sihon_purified']['value'])
        return out('Ammon and Moab purified through Sihon — Israel\'s title by his conquest (Chullin 60b; Deut 2:9)', ['land_possessed'])
    if ask == 'parable_tellers':
        ink('21:27', '"therefore the PARABLE-TELLERS say" — Balaam\'s word (23:7 and after); the hapax')
        dat('the row parable_tellers: %s' % data['parable_tellers']['value'])
        return out('the parable-tellers — Balaam and Beor (Chullin 60b); the homily on the inclination (Bava Batra 78b)', [FX.NONE])
    if ask == 'jeremiah_quote':
        ink('21:28; Jer 48:45', 'Jeremiah quotes the song — the shared tokens (computed): %s' % sorted(JER))
        return out('Jeremiah 48:45-46 quotes 21:28-29 — the parable-tellers\' song in the prophet (computed)', [FX.NONE])
    if ask == 'ammon_border':
        ink('21:24', '"for the border of the sons of Ammon was STRONG"')
        dat('the row ammon_border: %s' % data['ammon_border']['value'])
        return out('Ammon\'s border strong here, commanded off-limits at Deut 2:19, 2:37', [FX.NONE])
    if ask == 'land_east':
        ink('21:24-25, 21:31-32, 21:35', '"and possessed his land from Arnon to Jabbok... Heshbon and its daughters... Jazer... and they possessed his land" — the land east of the Jordan')
        return out('the land east of the Jordan possessed — Sihon\'s from Arnon to Jabbok, Jazer, Og\'s Bashan (21:24-35); chapter 32\'s status', ['land_possessed', 'kings_smitten'])
    if ask == 'spy_verb':
        dat('the row spy_verb: %s' % data['spy_verb']['value'])
        return out('"to spy out Jazer" — Caleb\'s verb (Josh 14:7), not the spies\' "tour" (13:2)', [FX.NONE])
    if ask == 'og_lore':
        ink('21:33-35; Deut 3:11', '"Og king of Bashan came out against them" — his bed %s by the parser' % OG_BED)
        dat('the row og_lore: %s' % data['og_lore']['value'])
        return out('Og — Sihon\'s brother of the Rephaim, the flood\'s survivor by the lore; his bed nine by four (Deut 3:11)', ['fear_not_promised'])
    if ask == 'deut3_delta':
        ink('21:33-35; Deut 3:1-3', 'the retelling with the pronouns shifted (computed): %s / %s; one token at 3:2 (%s / %s)' % (D33[0], D33[1], D34[0], D34[1]))
        return out('Deuteronomy 3:1-3 = 21:33-35 with the pronouns shifted — we for they, "to me" for "to Moses" (computed)', [FX.NONE])
    if ask == 'joshua_refrain':
        ink('21:35', '"until no survivor was left to him" — the refrain\'s seats (computed): %s' % SURVIVOR)
        return out('"until no survivor was left" — born at 21:35, Joshua\'s refrain (8:22, 10:33), 2 Kgs 10:11', ['kings_smitten'])
    if ask == 'sihon_refused':
        ink('21:23', '"and Sihon did not let Israel pass through his border" — Deut 2:30\'s hardening; Judg 11:20\'s distrust')
        return out('Sihon refused the passage and came to Jahaz — hardened (Deut 2:30)', ['refused'])
    return out('no verdict in span', [FX.NONE])
