#!/usr/bin/env python3
# THE NUMBERS WALK sitting 3b — THE COMPILE OF BEHA'ALOTCHA (2026-09-10; World/step9/NUMBERS_WALK.md "Sitting 3b"): THE TYPES FIRST — sixteen
# new kinds on the tape (six SPEECH, nine ACTS, one STATUTE; two kinds REUSED: cloud_lifted at 10:11 — its own tape text names that verse as
# its first run — and lamps_raised at 8:3, the erection's verb under Aaron), seven CASE kinds for the exam's scene, six effects, six entities,
# the 50th daemon's block, the functions block, the dependency span and edges, the installation probe's count. The `he` built from the
# pointed DB text (cantillation stripped), the witnesses the plain consonantal runs; every index range FOUND by the consonantal word, never
# typed. Idempotent (add_types_naso.py's form).
import re, sqlite3, yaml
ROOT = "<repo-old>"
db = sqlite3.connect(f"file:{ROOT}/elijah_docket/tanakh.sqlite?mode=ro", uri=True)
def words(book, ch, vs):
    return [r[0] for r in db.execute("SELECT w.he FROM words w JOIN verses v ON w.verse_id=v.id WHERE v.book=? AND v.chapter=? AND v.verse=? ORDER BY w.idx", (book, ch, vs)).fetchall()]
def pointed(book, ch, vs, lo, hi):
    return ' '.join(''.join(c for c in w if c != '/' and not (0x0591 <= ord(c) <= 0x05AF)) for w in words(book, ch, vs)[lo:hi])
def plain(book, ch, vs, lo, hi):
    return ' '.join(''.join(c for c in w if c != '/' and not (0x0591 <= ord(c) <= 0x05C7)) for w in words(book, ch, vs)[lo:hi])
q = lambda s: '"' + s.replace('\\', '\\\\').replace('"', '\\"') + '"'
def span(book, ch, vs, first, last):
    ws = [''.join(c for c in w if c != '/' and not (0x0591 <= ord(c) <= 0x05C7)) for w in words(book, ch, vs)]
    lo, hi = ws.index(first), len(ws) - 1 - ws[::-1].index(last)
    assert lo <= hi, (book, ch, vs, first, last)
    return lo, hi + 1
def P(book, ch, vs, first, last): return pointed(book, ch, vs, *span(book, ch, vs, first, last))
def L(book, ch, vs, first, last): return plain(book, ch, vs, *span(book, ch, vs, first, last))
N = 'Num'
SUB = "submitted by cold_run_beha.py [subjects: %s] (the narrative scene, THE NUMBERS WALK 3b); re-submitted on the sequential tape by cold_run_sequence.py; consumed by law_beha (cold_run_beha.py) -> %s"
CASE = "submitted by cold_run_beha.py [subjects: the exam's persons] (the wrap's scene); consumed by law_beha (cold_run_beha.py) -> %s"
KINDS = [
 ("lamps_commanded", "speech",
  "the lamps commanded — 'speak to Aaron and say to him: when you raise the lamps, toward the face of the lampstand shall the seven lamps give light' (Num 8:2); the lampstand's making recalled, beaten gold to its shaft and its flower, as the pattern shown (8:4)",
  P(N, 8, 2, 'דבר', 'הנרות') + " (speak to Aaron and say to him: when you raise the lamps, toward the face of the lampstand shall the seven lamps give light — Num 8:2)", ["Num 8:2 | " + L(N, 8, 2, 'דבר', 'הנרות'), "Num 8:4 | " + L(N, 8, 4, 'וזה', 'המנרה')],
  "Num 8:1-4; Onkelos Num 8:1-4 (the lamps toward the face; beaten — drawn); Sifrei Bamidbar 59:1, 60:1, 61:1",
  "num_08_menorah_levites (STEP_Nm_8_1, STEP_Nm_8_2, STEP_Nm_8_4; claims BH08A-01, BH08A-02)", SUB % ("aaron", "commanded (the lamps' debit, closed by the lighting at 8:3 — lamps_raised, the erection's kind reused)"), ["geometry", "count", "pattern"]),
 ("levites_purification_commanded", "speech",
  "the Levites' purification commanded — 'take the Levites from among the children of Israel and purify them; and thus you shall do to them to purify them: sprinkle the water of purification on them, and they shall pass a razor over all their flesh and wash their garments' (Num 8:6-7); the two bulls, the laying of hands, the waving, 'given, given are they to Me' (8:8-19)",
  P(N, 8, 6, 'קח', 'אתם') + " (take the Levites from among the children of Israel and purify them — Num 8:6) · " + P(N, 8, 7, 'וכה', 'והטהרו') + " (and thus you shall do to them to purify them: sprinkle the water of purification on them, and they shall pass a razor over all their flesh and wash their garments and purify themselves — Num 8:7)", ["Num 8:6 | " + L(N, 8, 6, 'קח', 'אתם'), "Num 8:7 | " + L(N, 8, 7, 'וכה', 'והטהרו'), "Num 8:16 | " + L(N, 8, 16, 'כי', 'לי')],
  "Num 8:5-19; Onkelos Num 8:5-19 (the water of purification; the razor as shears; waving as lifting; 'given, given' as 'separated, separated'); Sifrei 92:1 the ten 'unto Me'; Menachot 61b-62a; Bekhorot 4a-5a",
  "num_08_menorah_levites (STEP_Nm_8_5 through STEP_Nm_8_19; claims BH08A-03, BH08A-04, BH08A-05)", SUB % ("the-levites", "commanded (the rite's debit — the sprinkling, the razor, the garments, the two bulls, the two layings of hands, the three wavings, the giving; closed by the rite at 8:20-22)"), ["water", "razor", "garments", "bulls", "hands_laid", "wavings", "given_doubled"]),
 ("levites_purified_and_given", "act",
  "the Levites purified, waved and given — 'and Moses and Aaron and all the congregation of the children of Israel did to the Levites according to all that the LORD commanded Moses concerning the Levites, so did the children of Israel to them; and the Levites purified themselves and washed their garments, and Aaron waved them as a wave offering before the LORD and made atonement for them to purify them; and afterward the Levites went in to do their service' (Num 8:20-22) — ONE waving in the run against three in the spec (M-22)",
  P(N, 8, 21, 'ויתחטאו', 'לטהרם') + " (and the Levites purified themselves and washed their garments, and Aaron waved them as a wave offering before the LORD and made atonement for them to purify them — Num 8:21)", ["Num 8:20 | " + L(N, 8, 20, 'ויעש', 'ישראל'), "Num 8:21 | " + L(N, 8, 21, 'ויתחטאו', 'לטהרם'), "Num 8:22 | " + L(N, 8, 22, 'ואחרי', 'להם')],
  "Num 8:20-22; Onkelos Num 8:20-22",
  "num_08_menorah_levites (STEP_Nm_8_20, STEP_Nm_8_21, STEP_Nm_8_22; claim BH08A-05)", SUB % ("the-levites", "waved (the one waving of the run), given_to_aaron (the service entered — 8:22 'before Aaron and before his sons'); the rite's debit CLOSED"), ["wavings_in_run", "atoned", "service_entered"]),
 ("levite_age_rule", "statute",
  "the Levites' ages — 'this is what belongs to the Levites: from twenty-five years old and upward he shall come to host the host in the service of the tent of meeting; and from fifty years old he shall return from the host of the service and shall serve no more, but shall minister with his brothers in the tent of meeting to keep the charge, and shall do no service' (Num 8:24-26) — twenty-five here against thirty at 4:3 and twenty in Chronicles: a three-setting parameter",
  P(N, 8, 24, 'זאת', 'מועד') + " (this is what belongs to the Levites: from twenty-five years old and upward he shall come to host the host in the service of the tent of meeting — Num 8:24) · " + P(N, 8, 25, 'ומבן', 'עוד') + " (and from fifty years old he shall return from the host of the service and shall serve no more — Num 8:25)", ["Num 8:24 | " + L(N, 8, 24, 'זאת', 'מועד'), "Num 8:25 | " + L(N, 8, 25, 'ומבן', 'עוד'), "Num 8:26 | " + L(N, 8, 26, 'ושרת', 'במשמרתם')],
  "Num 8:23-26; Onkelos Num 8:23-26; Sifrei Bamidbar 62:1, 63:1; Chullin 24a:7-12; Mishnah Chullin 1:6; 1 Chr 23:24-27; Arakhin 11a",
  "num_08_menorah_levites (STEP_Nm_8_23, STEP_Nm_8_24, STEP_Nm_8_25, STEP_Nm_8_26; claims BH08A-06, BH08A-07)", SUB % ("the-levites", "charge_kept (the age rule as the value: 25 to serve, 50 to return and keep the charge — the parameter's setting on the ledger)"), ["age_in", "age_out", "after_fifty"]),
 ("trumpets_commanded", "speech",
  "the trumpets commanded — 'make for yourself two trumpets of silver, of beaten work you shall make them, and they shall be for you for the calling of the congregation and for the journeying of the camps' (Num 10:2); the sounds and the offices (10:3-8), the war and the oppressor (10:9), the days of gladness (10:10) — a command with NO narrated making in the span: the debit stays OPEN (the trumpets in Phinehas' hand at 31:6 the readback)",
  P(N, 10, 2, 'עשה', 'המחנות') + " (make for yourself two trumpets of silver, of beaten work you shall make them, and they shall be for you for the calling of the congregation and for the journeying of the camps — Num 10:2)", ["Num 10:2 | " + L(N, 10, 2, 'עשה', 'המחנות'), "Num 10:9 | " + L(N, 10, 9, 'וכי', 'מאיביכם'), "Num 10:10 | " + L(N, 10, 10, 'וביום', 'אלהיכם')],
  "Num 10:1-10; Onkelos Num 10:1-10 (the teruah a WAIL); Sifrei Bamidbar 72:1-77:1; Rosh Hashanah 26b-27a, 32a, 33b-34a; Mishnah Rosh Hashanah 3:3-4, 4:5-6, 4:9; Menachot 28a-b; Mishnah Ta'anit 1-3; Mishnah Sukkah 5:4-5",
  "num_10_trumpets_depart (STEP_Nm_10_1 through STEP_Nm_10_10; claims BH10A-01, BH10A-02, BH10A-03, BH10A-04)", SUB % ("moses", "commanded (the trumpets' debit — 'make for yourself': OPEN in this span, its run at Num 31:6)"), ["count", "material", "work", "offices", "sounds", "war", "gladness"]),
 ("march_in_order", "act",
  "the first march in the camp's order — 'and they journeyed first by the mouth of the LORD by the hand of Moses; and the standard of the camp of the children of Judah journeyed first by their hosts... and the tabernacle was taken down, and the sons of Gershon and the sons of Merari journeyed, bearing the tabernacle... and the Kohathites journeyed, bearing the sanctuary, and they set up the tabernacle before their coming' (Num 10:13-28)",
  P(N, 10, 14, 'ויסע', 'עמינדב') + " (and the standard of the camp of the children of Judah journeyed first by their hosts, and over its host was Nahshon son of Amminadab — Num 10:14) · " + P(N, 10, 21, 'ונסעו', 'באם') + " (and the Kohathites journeyed, bearing the sanctuary, and they set up the tabernacle before their coming — Num 10:21)", ["Num 10:13 | " + L(N, 10, 13, 'ויסעו', 'משה'), "Num 10:14 | " + L(N, 10, 14, 'ויסע', 'עמינדב'), "Num 10:17 | " + L(N, 10, 17, 'והורד', 'המשכן'), "Num 10:21 | " + L(N, 10, 21, 'ונסעו', 'באם'), "Num 10:28 | " + L(N, 10, 28, 'אלה', 'ויסעו')],
  "Num 10:11-28; Onkelos Num 10:11-28 (the standard a Greek ORDER; the gatherer the COLLECTOR); Num 2:3-31 the camp's order; Zevachim 61b, 116b",
  "num_10_trumpets_depart (STEP_Nm_10_11 through STEP_Nm_10_28; claims BH10A-05, BH10A-06)", SUB % ("israel", "arrayed_by_banners (Bamidbar's effect with the march's order as the value — Judah, Reuben, the tent, Ephraim, Dan); charge_kept on the-levites (Gershon and Merari bearing the tabernacle after Judah, Kohath bearing the sanctuary after Reuben)"), ["order", "levites_places", "princes"]),
 ("hobab_asked", "speech",
  "Hobab asked — 'and Moses said to Hobab son of Reuel the Midianite, Moses' father-in-law: we are journeying to the place of which the LORD said, I will give it to you; come with us and we will do you good... and he said to him: I will not go, but to my own land and to my kindred I will go. And he said: leave us not, I pray... and you shall be to us for eyes' (Num 10:29-32) — a plea with no recorded answer in the ink (Judg 1:16, 4:11 the readback)",
  P(N, 10, 29, 'ויאמר', 'ישראל') + " (and Moses said to Hobab son of Reuel the Midianite, Moses' father-in-law: we are journeying to the place of which the LORD said, I will give it to you; come with us and we will do you good, for the LORD has spoken good concerning Israel — Num 10:29) · " + P(N, 10, 30, 'ויאמר', 'אלך') + " (and he said to him: I will not go, but to my own land and to my kindred I will go — Num 10:30)", ["Num 10:29 | " + L(N, 10, 29, 'ויאמר', 'ישראל'), "Num 10:30 | " + L(N, 10, 30, 'ויאמר', 'אלך'), "Num 10:31 | " + L(N, 10, 31, 'ויאמר', 'לעינים')],
  "Num 10:29-32; Onkelos Num 10:29-32 ('eyes for us' — 'the mighty deeds done for us you saw with your eyes'); Sifrei Bamidbar 78:1-81:1; Zevachim 116a (Jethro before or after Sinai)",
  "num_10_trumpets_depart (STEP_Nm_10_29, STEP_Nm_10_30, STEP_Nm_10_31, STEP_Nm_10_32; claim BH10A-07)", SUB % ("hobab", "plea_made (the status on Hobab: asked to come, refused, asked again — no close in the span; Judg 1:16 the readback)"), ["three_readings", "answer"]),
 ("ark_journeyed", "act",
  "the ark journeyed before them — 'and they journeyed from the mountain of the LORD three days' journey, and the ark of the covenant of the LORD journeyed before them three days' journey to spy out for them a resting place; and the cloud of the LORD was over them by day... and when the ark journeyed Moses said: Rise, LORD... and when it rested he said: Return, LORD, to the myriads of the thousands of Israel' (Num 10:33-36) — the three days a TIMER on the tape, the two inverted nuns around 10:35-36",
  P(N, 10, 33, 'ויסעו', 'מנוחה') + " (and they journeyed from the mountain of the LORD three days' journey, and the ark of the covenant of the LORD journeyed before them three days' journey to spy out for them a resting place — Num 10:33)", ["Num 10:33 | " + L(N, 10, 33, 'ויסעו', 'מנוחה'), "Num 10:35 | " + L(N, 10, 35, 'ויהי', 'מפניך'), "Num 10:36 | " + L(N, 10, 36, 'ובנחה', 'ישראל')],
  "Num 10:33-36; Onkelos Num 10:33-36 ('to spy out' — 'to prepare'; 'Rise, LORD' — 'reveal Yourself'); Sifrei Bamidbar 82:1-84:5; Shabbat 115b-116a; Mishnah Yadayim 3:5; Yevamot 64a; Taanit 29a:3",
  "num_10_trumpets_depart (STEP_Nm_10_33, STEP_Nm_10_34, STEP_Nm_10_35, STEP_Nm_10_36; claims BH10A-08, BH10A-09, BH10A-10)", SUB % ("the-ark", "journey_of_three_days (the TIMER on the ark's body, due the march's day + 3 — fired on the walk to 11:1's reading-placed marker); the seven clouds and the 22,000 as data"), ["days", "clouds", "song", "signs"]),
 ("fire_of_the_lord_burned", "act",
  "the fire of the LORD burned — 'and the people were as murmurers, evil in the ears of the LORD; and the LORD heard, and His anger burned, and the fire of the LORD burned among them and consumed at the edge of the camp; and the people cried to Moses, and Moses prayed to the LORD, and the fire sank; and he called the name of that place Taberah' (Num 11:1-3)",
  P(N, 11, 1, 'ותבער', 'המחנה') + " (and the fire of the LORD burned among them and consumed at the edge of the camp — Num 11:1) · " + P(N, 11, 2, 'ותשקע', 'האש') + " (and the fire sank — Num 11:2)", ["Num 11:1 | " + L(N, 11, 1, 'ויהי', 'המחנה'), "Num 11:2 | " + L(N, 11, 2, 'ויצעק', 'האש'), "Num 11:3 | " + L(N, 11, 3, 'ויקרא', 'יהוה')],
  "Num 11:1-3; Onkelos Num 11:1-3 (Taberah rendered a name); Sifrei Bamidbar 85:1-86:1; Deut 9:22; 1 Kgs 18:38",
  "num_11_complaint_quail (STEP_Nm_11_1, STEP_Nm_11_2, STEP_Nm_11_3; claims BH11A-01, BH11A-02)", SUB % ("israel", "fire_sank (the status: the fire at the edge, sunk at Moses' prayer, the place named Taberah)"), ["edge", "who", "prayer", "name"]),
 ("lust_and_weeping", "act",
  "the lust and the weeping — 'and the rabble that was among them lusted a lust, and the children of Israel also wept again and said: who shall give us flesh to eat? we remember the fish... the cucumbers and the melons and the leeks and the onions and the garlic; and now our soul is dried away, there is nothing at all but this manna before our eyes' (Num 11:4-6); the manna described (11:7-9); the weeping by families and Moses' cry (11:10-15)",
  P(N, 11, 4, 'והאספסף', 'בשר') + " (and the rabble that was among them lusted a lust, and the children of Israel also wept again and said: who shall give us flesh to eat? — Num 11:4)", ["Num 11:4 | " + L(N, 11, 4, 'והאספסף', 'בשר'), "Num 11:10 | " + L(N, 11, 10, 'וישמע', 'רע')],
  "Num 11:4-15; Onkelos Num 11:4-15 (the rabble the MIXED MULTITUDE; 'lusted a lust' — 'asked a request'); Sifrei Bamidbar 86:1-91:1; Yoma 75a; Shabbat 130a; Arakhin 15a; Psalm 106:14",
  "num_11_complaint_quail (STEP_Nm_11_4 through STEP_Nm_11_15; claims BH11A-03, BH11A-04)", SUB % ("the-rabble", "lusted (the status on the rabble with Israel weeping after them — the five foods, the manna's taste, the families)"), ["foods", "manna", "families", "moses_cry"]),
 ("elders_commanded", "speech",
  "the seventy commanded, and flesh for a month — 'gather to Me seventy men of the elders of Israel... and I will come down and speak with you there, and I will set apart of the spirit that is on you and put it on them, and they shall bear with you the burden of the people' (Num 11:16-17); 'and to the people you shall say: sanctify yourselves for tomorrow and you shall eat flesh... not one day, nor two days, nor five days, nor ten days, nor twenty days — until a month of days, until it comes out of your nostrils' (11:18-20); Moses' six hundred thousand and the hand not shortened (11:21-23)",
  P(N, 11, 16, 'אספה', 'עמך') + " (gather to Me seventy men of the elders of Israel whom you know to be the elders of the people and its officers, and take them to the tent of meeting and let them stand there with you — Num 11:16) · " + P(N, 11, 20, 'עד', 'לזרא') + " (until a month of days, until it comes out of your nostrils and is loathsome to you — Num 11:20)", ["Num 11:16 | " + L(N, 11, 16, 'אספה', 'עמך'), "Num 11:17 | " + L(N, 11, 17, 'וירדתי', 'לבדך'), "Num 11:18 | " + L(N, 11, 18, 'ואל', 'ואכלתם'), "Num 11:20 | " + L(N, 11, 20, 'עד', 'ממצרים')],
  "Num 11:16-23; Onkelos Num 11:16-23 ('set apart of the spirit' — 'make greater'; 'sanctify yourselves' — 'prepare'; 'the hand short' — 'the Word held back'); Sifrei Bamidbar 92:1-95:2; Sanhedrin 17a; Mishnah Sanhedrin 1:6; Yoma 75b",
  "num_11_complaint_quail (STEP_Nm_11_16 through STEP_Nm_11_23; claims BH11A-05, BH11A-06)", SUB % ("moses", "commanded (the gathering's debit on Moses, closed by 11:24-25); flesh_for_a_month set as a TIMER on israel, due the day + 30 (the month of 11:20 — fired on the walk to 12:16's marker; Taanit 29a's stack the checkpoint)"), ["seventy", "spirit", "day_ladder", "month", "six_hundred_thousand"]),
 ("elders_prophesied", "act",
  "the seventy prophesied, and the two in the camp — 'and the LORD came down in the cloud and spoke to him, and set apart of the spirit that was on him and gave it to the seventy men, the elders; and it was, when the spirit rested on them, they prophesied, and did not continue. And two men remained in the camp, the name of the one Eldad and the name of the second Medad, and the spirit rested on them... and they prophesied in the camp' (Num 11:25-26); Joshua's 'restrain them' and Moses' 'would that all the LORD's people were prophets' (11:28-29)",
  P(N, 11, 25, 'וירד', 'יספו') + " (and the LORD came down in the cloud and spoke to him, and set apart of the spirit that was on him and gave it to the seventy men, the elders; and it was, when the spirit rested on them, they prophesied, and did not continue — Num 11:25) · " + P(N, 11, 26, 'וישארו', 'במחנה') + " (and two men remained in the camp... and the spirit rested on them... and they prophesied in the camp — Num 11:26)", ["Num 11:24 | " + L(N, 11, 24, 'ויצא', 'האהל'), "Num 11:25 | " + L(N, 11, 25, 'וירד', 'יספו'), "Num 11:26 | " + L(N, 11, 26, 'וישארו', 'במחנה'), "Num 11:29 | " + L(N, 11, 29, 'ויאמר', 'עליהם')],
  "Num 11:24-30; Onkelos Num 11:24-30 ('did not continue' — 'DID NOT CEASE': the spine disagreeing with itself; 'restrain' — 'bind'); Sifrei Bamidbar 95:2-96:1; Sanhedrin 17a",
  "num_11_complaint_quail (STEP_Nm_11_24 through STEP_Nm_11_30; claims BH11A-07)", SUB % ("the-seventy-elders", "spirit_rested (the status on the seventy — the prophecy that did not continue — and on eldad-and-medad, whose did: the two readings of 'did not continue' as the value's arms); moses' gathering debit CLOSED"), ["seventy", "two", "continued", "restrain"]),
 ("quail_and_plague", "act",
  "the quail and the plague — 'and a wind went out from the LORD and brought quail from the sea and let them fall by the camp, about a day's journey on this side and a day's journey on that side round about the camp, and about two cubits above the face of the earth; and the people rose all that day and all the night and all the next day and gathered the quail — he who gathered least gathered ten homers... the flesh was yet between their teeth, before it was chewed, and the anger of the LORD burned against the people, and the LORD struck the people with a very great blow; and he called the name of that place Kibroth-hattaavah, for there they buried the people that lusted; from Kibroth-hattaavah the people journeyed to Hazeroth, and they were at Hazeroth' (Num 11:31-35)",
  P(N, 11, 31, 'ורוח', 'הארץ') + " (and a wind went out from the LORD and brought quail from the sea and let them fall by the camp, about a day's journey on this side and a day's journey on that side round about the camp, and about two cubits above the face of the earth — Num 11:31) · " + P(N, 11, 33, 'הבשר', 'מאד') + " (the flesh was yet between their teeth, before it was chewed, and the anger of the LORD burned against the people, and the LORD struck the people with a very great blow — Num 11:33)", ["Num 11:31 | " + L(N, 11, 31, 'ורוח', 'הארץ'), "Num 11:32 | " + L(N, 11, 32, 'ויקם', 'המחנה'), "Num 11:33 | " + L(N, 11, 33, 'הבשר', 'מאד'), "Num 11:34 | " + L(N, 11, 34, 'ויקרא', 'המתאוים'), "Num 11:35 | " + L(N, 11, 35, 'מקברות', 'בחצרות')],
  "Num 11:31-35; Onkelos Num 11:31-35 (Kibroth-hattaavah rendered a name; 'ten homers' — 'ten heaps'; 'smote a blow' — 'killed a killing'); Sifrei Bamidbar 97:1-98:1; Yoma 75b; Chullin 27b; Num 33:16-17; Deut 9:22",
  "num_11_complaint_quail (STEP_Nm_11_31 through STEP_Nm_11_35; claims BH11A-08, BH11A-09)", SUB % ("the-lusters", "put_to_death (by HEAVEN — the blow with the flesh between their teeth; the fit die at once, the rest after the month: Sifrei 94:1's two timers), buried (the graves of lust the place's name); the journey to Hazeroth"), ["height", "gathered", "blow", "graves", "hazeroth"]),
 ("miriam_spoke", "speech",
  "Miriam and Aaron spoke against Moses — 'and Miriam spoke, and Aaron, against Moses because of the Cushite woman whom he had taken, for he had taken a Cushite woman; and they said: has the LORD indeed spoken only with Moses? has He not spoken also with us? and the LORD heard' (Num 12:1-2); the LORD's answer at the tent's door — mouth to mouth, not in riddles (12:4-8); 'and the anger of the LORD burned against them, and He went' (12:9)",
  P(N, 12, 1, 'ותדבר', 'לקח') + " (and Miriam spoke, and Aaron, against Moses because of the Cushite woman whom he had taken, for he had taken a Cushite woman — Num 12:1) · " + P(N, 12, 2, 'ויאמרו', 'יהוה') + " (and they said: has the LORD indeed spoken only with Moses? has He not spoken also with us? and the LORD heard — Num 12:2)", ["Num 12:1 | " + L(N, 12, 1, 'ותדבר', 'לקח'), "Num 12:2 | " + L(N, 12, 2, 'ויאמרו', 'יהוה'), "Num 12:5 | " + L(N, 12, 5, 'וירד', 'שניהם'), "Num 12:9 | " + L(N, 12, 9, 'ויחר', 'וילך')],
  "Num 12:1-9; Onkelos Num 12:1-9 (the Cushite woman — 'the BEAUTIFUL woman'; 'mouth to mouth' — 'speech with speech'; 'the likeness of the LORD' — 'of the GLORY'); Sifrei Bamidbar 99:1-104:1; Arakhin 15a-16b; Shabbat 87a, 97a; Yevamot 49b; Deut 24:9",
  "num_12_miriam (STEP_Nm_12_1 through STEP_Nm_12_9; claims BH12A-01, BH12A-02, BH12A-03, BH12A-04)", SUB % ("miriam", "evil_speech_spoken (the status on Miriam — first by the grammar — and on Aaron: the tradition's paradigm of evil speech, Arakhin 15a; Deut 24:9)"), ["who_first", "cushite", "answer", "aaron_struck"]),
 ("miriam_stricken_and_shut_out", "act",
  "Miriam stricken and shut out seven days — 'and the cloud departed from over the tent, and behold Miriam was leprous as snow; and Aaron turned to Miriam, and behold, leprous' (Num 12:10); Aaron's plea and Moses' cry 'God, heal her, I pray' (12:11-13); 'if her father had but spit in her face, would she not be ashamed seven days? let her be shut out of the camp seven days, and afterward she shall be gathered in; and Miriam was shut out of the camp seven days, and the people did not journey until Miriam was gathered in' (12:14-15) — the seven a TIMER, the people's halt a BLOCK",
  P(N, 12, 10, 'והענן', 'מצרעת') + " (and the cloud departed from over the tent, and behold Miriam was leprous as snow; and Aaron turned to Miriam, and behold, leprous — Num 12:10) · " + P(N, 12, 15, 'ותסגר', 'מרים') + " (and Miriam was shut out of the camp seven days, and the people did not journey until Miriam was gathered in — Num 12:15)", ["Num 12:10 | " + L(N, 12, 10, 'והענן', 'מצרעת'), "Num 12:13 | " + L(N, 12, 13, 'ויצעק', 'לה'), "Num 12:14 | " + L(N, 12, 14, 'ויאמר', 'תאסף'), "Num 12:15 | " + L(N, 12, 15, 'ותסגר', 'מרים')],
  "Num 12:10-15; Onkelos Num 12:10-15 ('leprous as snow' — 'white as snow' then 'shut up'; 12:12 rewritten; 'cried' — 'prayed'; 'spat, spat' — 'rebuked, rebuked'); Sifrei Bamidbar 105:1-106:1; Bava Kamma 25a; Mishnah Bava Kamma 2:5; Mishnah Sotah 1:9; Berakhot 34a; Zevachim 101b-102a; Mishnah Negaim 2:5; Moed Katan 7b",
  "num_12_miriam (STEP_Nm_12_10 through STEP_Nm_12_15; claims BH12A-05, BH12A-06, BH12A-07)", SUB % ("miriam", "stricken_with_leprosy (the status), confined_seven_days (the leper's week as a TIMER on Miriam, due the day + 7 — the negaim effect reused for the same verb; fired on the walk to 12:16's marker), journey_halted (the BLOCK on israel: 'the people did not journey until Miriam was gathered in' — closed by paran_reached)"), ["stricken", "prayer", "dayo", "days", "halt"]),
 ("paran_reached", "act",
  "the people journeyed from Hazeroth to Paran — 'and afterward the people journeyed from Hazeroth and encamped in the wilderness of Paran' (Num 12:16) — the halt CLOSED after Miriam's seven days fired; the arrival written at 10:12 and again here; the twenty-ninth of Sivan on the shelf's stack (Taanit 29a:4-5), the day the spies go",
  P(N, 12, 16, 'ואחר', 'פארן') + " (and afterward the people journeyed from Hazeroth and encamped in the wilderness of Paran — Num 12:16)", ["Num 12:16 | " + L(N, 12, 16, 'ואחר', 'פארן'), "Num 10:12 | " + L(N, 10, 12, 'ויסעו', 'פארן')],
  "Num 12:16; Onkelos Num 12:16; Num 10:12; Taanit 29a:4-5; Seder Olam Rabbah 8:2",
  "num_12_miriam (STEP_Nm_12_16; claim BH12A-08)", SUB % ("israel", "journeyed (the itinerary's kind — 12:16's own verb 'journeyed' is the exodus story's registered act; here the halt's CLOSE: the daemon closes journey_halted on israel and writes nothing new)"), ["from", "to", "halt_closed"]),
 ("lamps_case", "case", "the exam's rows on the lamps (Num 8:1-4 — the geometry, the western lamp, beaten / the material ladder, the seven, the steps, the pattern)", P(N, 8, 2, 'אל', 'הנרות') + " (toward the face of the lampstand shall the seven lamps give light — Num 8:2)", ["Num 8:2 | " + L(N, 8, 2, 'אל', 'הנרות')], "Num 8:1-4; Sifrei 59:1-61:1; Menachot 28a-29a, 98b; Shabbat 22b; Mishnah Menachot 3:7; Mishnah Tamid 3:9", "the exam's rows (the docket)", CASE % "accepted / disqualified / lamp_arranged", ["ask", "geometry", "material", "count"]),
 ("levite_rite_case", "case", "the exam's rows on the Levites' rite and ages (Num 8:5-26 — the fitness by age and blemish and voice, the wavings, the giving, the firstborn ground)", P(N, 8, 24, 'מבן', 'ומעלה') + " (from twenty-five years old and upward — Num 8:24)", ["Num 8:24 | " + L(N, 8, 24, 'מבן', 'ומעלה')], "Num 8:5-26; Chullin 24a-b; Mishnah Chullin 1:6; Menachot 61b-62a; Bekhorot 4a-5a; Arakhin 11a", "the exam's rows (the docket)", CASE % "appointed_to_serve / exempt / disqualified / waved / accepted", ["ask", "age", "carrying", "blemished", "voice"]),
 ("trumpet_case", "case", "the exam's rows on the trumpets (Num 10:1-10 — the sounds, the identity with the shofar, the blast counts, the fasts' alarm, the blemished priest, the material, the instance scope)", P(N, 10, 5, 'ותקעתם', 'קדמה') + " (and you shall blow a teruah, and the camps that encamp eastward shall journey — Num 10:5)", ["Num 10:5 | " + L(N, 10, 5, 'ותקעתם', 'קדמה')], "Num 10:1-10; Rosh Hashanah 26b-27a, 32a, 33b-34a; Mishnah Rosh Hashanah 3-4; Mishnah Ta'anit 1-3; Mishnah Sukkah 5:4-5; Menachot 28a-b; Sifrei 72:1-77:1", "the exam's rows (the docket)", CASE % "accepted / disqualified / exempt / sanctify_day", ["ask", "who", "occasion", "count"]),
 ("march_case", "case", "the exam's rows on the march and the ark (Num 10:11-36 — the order, the tent on the march, the clouds, the signs, the 22,000, Hobab)", P(N, 10, 28, 'אלה', 'ויסעו') + " (these are the journeys of the children of Israel by their hosts, and they journeyed — Num 10:28)", ["Num 10:28 | " + L(N, 10, 28, 'אלה', 'ויסעו')], "Num 10:11-36; Zevachim 61b, 116a-b; Shabbat 115b-116a; Mishnah Yadayim 3:5; Yevamot 64a; Sifrei 78:1-84:5", "the exam's rows (the docket)", CASE % "accepted / disqualified / arrayed_by_banners", ["ask", "who", "what"]),
 ("elders_case", "case", "the exam's rows on the seventy and the two (Num 11:16-30 — the lots, the seventy-one, Eldad and Medad, 'restrain them', the descents)", P(N, 11, 16, 'אספה', 'ישראל') + " (gather to Me seventy men of the elders of Israel — Num 11:16)", ["Num 11:16 | " + L(N, 11, 16, 'אספה', 'ישראל')], "Num 11:16-30; Sanhedrin 17a; Mishnah Sanhedrin 1:6; Sifrei 92:1-96:1", "the exam's rows (the docket)", CASE % "appointed_to_serve / spirit_rested / accepted / disqualified", ["ask", "who", "count"]),
 ("quail_case", "case", "the exam's rows on Taberah, the lust and the quail (Num 11:1-15, 11:31-35 — the murmurers, the five foods, the families' weeping, the quail's height and slaughter, the two timers, the ten trials)", P(N, 11, 33, 'ויך', 'מאד') + " (and the LORD struck the people with a very great blow — Num 11:33)", ["Num 11:33 | " + L(N, 11, 33, 'ויך', 'מאד')], "Num 11:1-15, 11:31-35; Yoma 75a-76a; Chullin 27b; Arakhin 15a; Taanit 9a; Shabbat 130a; Sifrei 85:1-91:1, 97:1-98:1", "the exam's rows (the docket)", CASE % "put_to_death / lusted / fire_sank / accepted / disqualified / exempt", ["ask", "who", "what"]),
 ("miriam_case", "case", "the exam's rows on Miriam (Num 12:1-16 — evil speech, the Cushite, mouth to mouth, who declared her, the kin rule, the short prayer, DAYO, measure for measure, the leper as one dead)", P(N, 12, 14, 'הלא', 'למחנה') + " (would she not be ashamed seven days? let her be shut out of the camp seven days — Num 12:14)", ["Num 12:14 | " + L(N, 12, 14, 'הלא', 'למחנה')], "Num 12:1-16; Arakhin 15a-16b; Shabbat 87a, 97a; Yevamot 49b; Berakhot 34a; Bava Kamma 25a; Mishnah Bava Kamma 2:5; Mishnah Sotah 1:9; Zevachim 101b-102a; Mishnah Negaim 2:5; Moed Katan 7b; Mishnah Moed Katan 3:1", "the exam's rows (the docket)", CASE % "evil_speech_spoken / stricken_with_leprosy / confined_seven_days / disqualified / accepted / exempt / healed", ["ask", "who", "days"]),
]
EFFECTS = [
 ("plea_made", "status", "a plea made — the STATUS a spoken request writes on the one asked, with no close of its own: Moses to Hobab, 'come with us and we will do you good... leave us not, I pray' (Num 10:29-32) — Hobab's refusal ('I will not go') and Moses' second asking recorded as the value; the answer is not in the ink (Judg 1:16, 4:11 the readback)",
  P(N, 10, 31, 'ויאמר', 'אתנו') + " (and he said: leave us not, I pray — Num 10:31)", "Num 10:29-32; Onkelos; Sifrei Bamidbar 78:1-81:1", "num_10_trumpets_depart (STEP_Nm_10_29 through STEP_Nm_10_32; claim BH10A-07)", "law_beha (cold_run_beha.py) on hobab_asked — the status on hobab"),
 ("journey_of_three_days", "timer", "a journey of three days — the TIMER the ark's setting-out writes on the ark's body: 'and they journeyed from the mountain of the LORD three days' journey' (Num 10:33) — due the march's day plus three; its fire on the walk to 11:1's reading-placed marker is the shelf's own arithmetic (Taanit 29a:3: 'adds to the first twenty days an additional three days')",
  P(N, 10, 33, 'ויסעו', 'ימים') + " (and they journeyed from the mountain of the LORD three days' journey — Num 10:33)", "Num 10:33; Onkelos; Sifrei Bamidbar 82:1; Taanit 29a:3", "num_10_trumpets_depart (STEP_Nm_10_33; claim BH10A-08)", "law_beha (cold_run_beha.py) on ark_journeyed — the timer on the-ark"),
 ("fire_sank", "status", "the fire sank — the STATUS Taberah writes on Israel: 'the fire of the LORD burned among them and consumed at the edge of the camp; and the people cried to Moses, and Moses prayed to the LORD, and the fire sank' (Num 11:1-2) — the place named by the event (Sifrei 86:1)",
  P(N, 11, 2, 'ויצעק', 'האש') + " (and the people cried to Moses, and Moses prayed to the LORD, and the fire sank — Num 11:2)", "Num 11:1-3; Onkelos; Sifrei Bamidbar 85:1-86:1", "num_11_complaint_quail (STEP_Nm_11_1, STEP_Nm_11_2, STEP_Nm_11_3; claims BH11A-01, BH11A-02)", "law_beha (cold_run_beha.py) on fire_of_the_lord_burned — the status on israel"),
 ("lusted", "status", "lusted — the STATUS the rabble's craving writes: 'and the rabble that was among them lusted a lust, and the children of Israel also wept again' (Num 11:4) — Psalm 106:14 'they lusted a lust in the wilderness'; the graves of lust the name it earns (11:34)",
  P(N, 11, 4, 'והאספסף', 'תאוה') + " (and the rabble that was among them lusted a lust — Num 11:4)", "Num 11:4-6, 11:34; Onkelos ('asked a request'); Sifrei Bamidbar 86:1-87:1; Psalm 106:14", "num_11_complaint_quail (STEP_Nm_11_4; claim BH11A-03)", "law_beha (cold_run_beha.py) on lust_and_weeping — the status on the-rabble"),
 ("flesh_for_a_month", "timer", "flesh for a month — the TIMER the LORD's word writes on Israel: 'not one day, nor two days, nor five days, nor ten days, nor twenty days — until a month of days, until it comes out of your nostrils and is loathsome to you' (Num 11:19-20) — due the speech's day plus thirty; the shelf's stack lands Hazeroth on the twenty-second of Sivan (Taanit 29a:4): the machine's fire against it is the checkpoint",
  P(N, 11, 19, 'לא', 'יום') + " (not one day you shall eat, nor two days, nor five days, nor ten days, nor twenty days — Num 11:19) · " + P(N, 11, 20, 'עד', 'ימים') + " (until a month of days — Num 11:20)", "Num 11:18-20, 11:33; Onkelos; Sifrei Bamidbar 94:1; Yoma 75b; Taanit 29a:3-4", "num_11_complaint_quail (STEP_Nm_11_18, STEP_Nm_11_19, STEP_Nm_11_20; claim BH11A-06)", "law_beha (cold_run_beha.py) on elders_commanded — the timer on israel"),
 ("spirit_rested", "status", "the spirit rested — the STATUS the LORD's setting-apart writes on the seventy elders and on the two in the camp: 'and it was, when the spirit rested on them, they prophesied, and did not continue' (Num 11:25); 'and the spirit rested on them... and they prophesied in the camp' (11:26) — Onkelos 'did NOT CEASE' the spine's other arm, carried as the value's setting",
  P(N, 11, 25, 'ויהי', 'יספו') + " (and it was, when the spirit rested on them, they prophesied, and did not continue — Num 11:25)", "Num 11:25-29; Onkelos; Sifrei Bamidbar 95:2-96:1; Sanhedrin 17a", "num_11_complaint_quail (STEP_Nm_11_25, STEP_Nm_11_26; claim BH11A-07)", "law_beha (cold_run_beha.py) on elders_prophesied — the status on the-seventy-elders and on eldad-and-medad"),
 ("evil_speech_spoken", "status", "evil speech spoken — the STATUS Miriam's and Aaron's words write on them: 'and Miriam spoke, and Aaron, against Moses because of the Cushite woman' (Num 12:1) — the tradition's paradigm of evil speech (Arakhin 15a-16b; Deut 24:9 'remember what the LORD your God did to Miriam'); Miriam first by the grammar, the feminine singular verb before two subjects",
  P(N, 12, 1, 'ותדבר', 'במשה') + " (and Miriam spoke, and Aaron, against Moses — Num 12:1)", "Num 12:1-2; Onkelos; Sifrei Bamidbar 99:1-100:1; Arakhin 15a-16b; Deut 24:9", "num_12_miriam (STEP_Nm_12_1, STEP_Nm_12_2; claims BH12A-01, BH12A-02)", "law_beha (cold_run_beha.py) on miriam_spoke — the status on miriam and on aaron"),
 ("stricken_with_leprosy", "status", "stricken with leprosy — the STATUS the cloud's departing writes on Miriam: 'and the cloud departed from over the tent, and behold Miriam was leprous as snow' (Num 12:10) — the three 'as snow' (Moses' hand, Miriam, Gehazi); the leper's shutting-out follows as the negaim engine's week (confined_seven_days)",
  P(N, 12, 10, 'והנה', 'כשלג') + " (and behold Miriam was leprous as snow — Num 12:10)", "Num 12:10-15; Onkelos ('white as snow'); Sifrei Bamidbar 105:1; Zevachim 101b-102a; Mishnah Negaim 2:5", "num_12_miriam (STEP_Nm_12_10; claim BH12A-05)", "law_beha (cold_run_beha.py) on miriam_stricken_and_shut_out — the status on miriam"),
 ("journey_halted", "block", "the journey halted — the BLOCK Miriam's week writes on the people: 'and the people did not journey until Miriam was gathered in' (Num 12:15) — Mishnah Sotah 1:9's measure for measure (she waited an hour for Moses at the river, Israel waited seven days for her); closed by 12:16's journey to Paran after the seven days fired",
  P(N, 12, 15, 'והעם', 'מרים') + " (and the people did not journey until Miriam was gathered in — Num 12:15)", "Num 12:15-16; Onkelos; Sifrei Bamidbar 106:1; Mishnah Sotah 1:9; Sotah 9b, 11a", "num_12_miriam (STEP_Nm_12_15, STEP_Nm_12_16; claims BH12A-07, BH12A-08)", "law_beha (cold_run_beha.py) on miriam_stricken_and_shut_out — the block on israel, closed by paran_reached"),
]
# ---- the kinds: append INTO the `events:` mapping (before `narrative_verbs:`) ----
path = f"{ROOT}/World/step9/event_vocabulary.yaml"
text = open(path, encoding='utf-8').read()
have = yaml.safe_load(text)['events']
out = []
for name, form, en, he, wit, ink, corpus, tape, fields in KINDS:
    if name in have: continue
    out.append(f"  {name}:\n    en: {q(en)}\n    he: {q(he)}\n    form: {form}\n    witness: [{', '.join(q(w) for w in wit)}]\n    ink: {q(ink)}\n    corpus: {q(corpus)}\n    tape: {q(tape)}\n    fields: [{', '.join(q(f) for f in fields)}]\n")
if out:
    i = text.index('\nnarrative_verbs:\n')
    text = text[:i] + '\n' + ''.join(out).rstrip('\n') + text[i:]
    open(path, 'w', encoding='utf-8').write(text)
after = yaml.safe_load(open(path, encoding='utf-8'))
assert all(k[0] in after['events'] for k in KINDS)
print('kinds: %d added, registry %d' % (len(out), len(after['events'])))
# ---- the effects ----
path = f"{ROOT}/World/step9/effect_vocabulary.yaml"
text = open(path, encoding='utf-8').read()
have = yaml.safe_load(text)['effects']
out = []
for name, op, en, he, ink, corpus, exam in EFFECTS:
    if name in have: continue
    out.append(f"  {name}:\n    en: {q(en)}\n    he: {q(he)}\n    ledger_op: {op}\n    ink: {q(ink)}\n    corpus: {q(corpus)}\n    exam: {q(exam)}\n")
if out:
    if not text.endswith('\n'): text += '\n'
    open(path, 'w', encoding='utf-8').write(text + ''.join(out))
after = yaml.safe_load(open(path, encoding='utf-8'))['effects']
assert all(e[0] in after for e in EFFECTS)
print('effects: %d added, registry %d' % (len(out), len(after)))
# ---- the entities (append at the registry's end; the EOF branch) ----
path = f"{ROOT}/logic/corpus/entity_registry.yaml"
text = open(path, encoding='utf-8').read()
reg = yaml.safe_load(text)
ids = {e['id'] for e in reg['entities']}
ENT = [("miriam", "person", "Miriam — Moses' and Aaron's sister: the song at the sea (Exod 15:20-21), the speaking against Moses and the leprosy (Num 12:1-15), her death at Kadesh (Num 20:1); Deut 24:9 'remember what the LORD your God did to Miriam'", "miriam"),
       ("hobab", "person", "Hobab son of Reuel the Midianite, Moses' father-in-law (Num 10:29 — Jethro's house; Judg 1:16, 4:11 the Kenites who went): asked to come, refused, asked again — the answer not in the ink", "hobab"),
       ("the_seventy_elders", "people", "the seventy elders as a body — 'seventy men of the elders of Israel... and they shall bear with you the burden of the people' (Num 11:16-17), gathered at the tent, the spirit set apart on them, prophesied and did not continue (11:24-25); the Sanhedrin of seventy-one (Mishnah Sanhedrin 1:6); chosen by lot (Sanhedrin 17a)", "the-seventy-elders"),
       ("eldad_and_medad", "people", "Eldad and Medad — the two who remained in the camp, 'and the spirit rested on them, and they were among the written, and they did not go out to the tent, and they prophesied in the camp' (Num 11:26-29); Sanhedrin 17a's three prophecies", "eldad-and-medad"),
       ("the_rabble", "people", "the rabble — 'the mixed multitude that was among them lusted a lust' (Num 11:4; Onkelos 'the mixed multitude'; Exod 12:38's 'mixed multitude' the tradition's identification): the craving's first movers", "the-rabble"),
       ("the_lusters", "people", "the lusters — 'the people that lusted', struck with the flesh between their teeth and buried at the graves of lust (Num 11:33-34; Sifrei 94:1 / Yoma 75b: the fit at once, the rest after the month)", "the-lusters")]
added = 0
for eid, kind, en, tok in ENT:
    if eid in ids: continue
    if not text.endswith('\n'): text += '\n'
    text += f"  - id: {eid}\n    en: {q(en)}\n    kind: {kind}\n    members:\n      - {{token: {tok}, units: [step9-scenes]}}   # cold_run_beha.py's narrative scene (THE NUMBERS WALK 3b, 2026-09-10); the frozen units' tokens a later join\n"
    added += 1
if added:
    open(path, 'w', encoding='utf-8').write(text)
reg = yaml.safe_load(open(path, encoding='utf-8'))
assert all(any(e['id'] == eid for e in reg['entities']) for eid, *_ in ENT)
print('entities: %d added, registry %d' % (added, len(reg['entities'])))
# ---- the daemon block + the functions block (daemon_dispositions.yaml) ----
path = f"{ROOT}/World/step9/daemon_dispositions.yaml"
text = open(path, encoding='utf-8').read()
if '  law_beha:' not in text:
    block = '''  law_beha:
    file: cold_run_beha.py
    wraps: beha
    given_at: Num 8:1
    installed_by: boot   # THE NUMBERS WALK 3b (2026-09-10): a law spoken at its verse with no installing act on the tape — the standing setting
    watches:
      lamps_commanded: [commanded]                                    # 8:1-4: the lamps' debit on Aaron
      lamps_raised: [lamp_arranged]                                   # 8:3: the run under Aaron — the erection's kind (Exod 40:25) at its second seat; Aaron's debit CLOSED
      levites_purification_commanded: [commanded]                     # 8:5-19: the rite's debit on the Levites
      levites_purified_and_given: [waved, given_to_aaron]             # 8:20-22: the one waving of the run, the service entered; the rite's debit CLOSED
      levite_age_rule: [charge_kept]                                  # 8:23-26: the age rule as the value on the Levites (25 in, 50 out to the charge)
      trumpets_commanded: [commanded]                                 # 10:1-10: 'make for yourself' — OPEN in this span (Num 31:6 the run)
      cloud_lifted: [arrayed_by_banners]                              # 10:11-13: the cloud's first lifting — the standard journeys first (the erection's kind at its first run; law_erection fires too)
      march_in_order: [arrayed_by_banners, charge_kept]               # 10:14-28: the order on Israel, the Levites' burdens
      hobab_asked: [plea_made]                                        # 10:29-32: the plea on Hobab, no close
      ark_journeyed: [journey_of_three_days]                          # 10:33-36: the timer on the ark
      fire_of_the_lord_burned: [fire_sank]                            # 11:1-3: Taberah
      lust_and_weeping: [lusted]                                      # 11:4-15: the rabble
      elders_commanded: [commanded, flesh_for_a_month]                # 11:16-23: the gathering's debit on Moses; the month timer on Israel
      elders_prophesied: [spirit_rested]                              # 11:24-30: the seventy and the two; Moses' debit CLOSED
      quail_and_plague: [put_to_death, buried]                        # 11:31-35: the blow by HEAVEN on the lusters; the graves
      miriam_spoke: [evil_speech_spoken]                              # 12:1-9: Miriam and Aaron
      miriam_stricken_and_shut_out: [stricken_with_leprosy, confined_seven_days, journey_halted]   # 12:10-15: the leprosy, the week's timer, the halt on Israel
      paran_reached: []                                               # 12:16: the halt CLOSED — no write of its own
      lamps_case: [accepted, disqualified, lamp_arranged]             # the exam's rows on 8:1-4
      levite_rite_case: [appointed_to_serve, exempt, disqualified, waved, accepted]   # the exam's rows on 8:5-26 (Bamidbar's fitness CALLED)
      trumpet_case: [accepted, disqualified, exempt, sanctify_day]    # the exam's rows on 10:1-10 (the moadim's teruah CALLED)
      march_case: [accepted, disqualified, arrayed_by_banners]        # the exam's rows on 10:11-36
      elders_case: [appointed_to_serve, spirit_rested, accepted, disqualified]   # the exam's rows on 11:16-30
      quail_case: [put_to_death, lusted, fire_sank, accepted, disqualified, exempt]   # the exam's rows on 11:1-15, 11:31-35
      miriam_case: [evil_speech_spoken, stricken_with_leprosy, confined_seven_days, disqualified, accepted, exempt, healed]   # the exam's rows on 12:1-16 (the negaim engine CALLED)
'''
    i = text.index('  law_zelophehad:')
    text = text[:i] + block + text[i:]
if '\n  beha:   # THE NUMBERS WALK 3b' not in text:
    fb = '''  beha:   # THE NUMBERS WALK 3b (2026-09-10)
    lamps: {status: WRAPPED, by: law_beha}
    levites_rite: {status: WRAPPED, by: law_beha}
    trumpets: {status: WRAPPED, by: law_beha}
    march: {status: WRAPPED, by: law_beha}
    taberah_and_quail: {status: WRAPPED, by: law_beha}
    seventy_elders: {status: WRAPPED, by: law_beha}
    miriam: {status: WRAPPED, by: law_beha}
'''
    i = text.index('  naso:   # THE NUMBERS WALK 2b (2026-09-10)')
    j = text.index('\n  pre_sinai:', i)
    text = text[:j + 1] + fb + text[j + 1:]
open(path, 'w', encoding='utf-8').write(text)
dd = yaml.safe_load(open(path, encoding='utf-8'))
assert 'law_beha' in dd['daemons'] and 'beha' in dd['functions'], (list(dd)[:5])
print('daemons: %d (law_beha %s); functions blocks: %d' % (len(dd['daemons']), 'law_beha' in dd['daemons'], len(dd['functions'])))
# ---- the dependency span + edges ----
path = f"{ROOT}/World/step9/dependency_dispositions.yaml"
text = open(path, encoding='utf-8').read()
if '  beha:' not in text:
    a = "  naso:        [[Num, 4, 21, 49], [Num, 5, 1, 31], [Num, 6, 1, 27], [Num, 7, 1, 89]]"
    i = text.index(a); j = text.index('\n', i)
    text = text[:j + 1] + "  beha:        [[Num, 8, 1, 26], [Num, 10, 1, 36], [Num, 11, 1, 35], [Num, 12, 1, 16]]   # THE NUMBERS WALK 3b (2026-09-10; NUMBERS_WALK.md \"Sitting 3b\"): Beha'alotcha's lamps, the Levites' rite and ages, the trumpets, the march and the ark, Taberah and the quail, the seventy, Miriam (chapter 9 frozen at THE TENT and skipped)\n" + text[j + 1:]
    edges = '''  - {from: beha, to: bamidbar, disposition: CALL, link: reference, carries: verdict,
     why: "THE NUMBERS WALK 3b (2026-09-10) | 10:14-28's march runs in THE CAMP'S ORDER (2:3-31 — Bamidbar's camp('march')); 8:24-26's ages are Bamidbar's charges('fitness') with the three-setting parameter; the seventy BY LOT is the 273's mechanism (Sanhedrin 17a — Bamidbar's the_lots row): cold_run_bamidbar CALLED"}
  - {from: beha, to: pesach, disposition: CALL, link: reference, carries: verdict,
     why: "THE NUMBERS WALK 3b (2026-09-10) | 8:16-18 'instead of every firstborn... on the day I smote every firstborn in Egypt I sanctified them to Me' — the firstborn's ground: cold_run_pesach.firstborn CALLED"}
  - {from: beha, to: sanctuary_build, disposition: CALL, link: reference, carries: verdict,
     why: "THE NUMBERS WALK 3b (2026-09-10) | 8:4 'this is the work of the lampstand: beaten gold... as the pattern the LORD showed Moses' cites Exod 25:31-40 — the lampstand's spec: cold_run_sanctuary_build.menorah / lamp CALLED for the seven lamps, the beaten work, the pattern"}
  - {from: beha, to: moadim, disposition: CALL, link: reference, carries: verdict,
     why: "THE NUMBERS WALK 3b (2026-09-10) | 10:5-6's teruah is the teruah of Lev 23:24 (Rosh Hashanah) and 25:9 (the Jubilee) by the identity (Rosh Hashanah 33b-34a; Sifrei 73:2): cold_run_moadim.rosh_hashanah()['sound' / 'instrument'] CALLED for the sound and the shofar"}
  - {from: beha, to: negaim, disposition: CALL, link: reference, carries: verdict,
     why: "THE NUMBERS WALK 3b (2026-09-10) | 12:14-15 'let her be shut out of the camp seven days' — the leper's verb (Lev 13:4 'the priest shall shut up'): the negaim engine's confinement week (confined_seven_days, days(1)) CALLED for Miriam's timer; Mishnah Negaim 2:5's kin rule the docket's row"}
  - {from: beha, to: heifer, disposition: OWED, link: reference,
     why: "THE NUMBERS WALK 3b (2026-09-10) | 8:7 'sprinkle the water of purification on them' — the heifer's water (Num 19:9 the water of sprinkling; with 5:2's corpse-unclean at Naso): no runner compiles chapter 19; OWED FORWARD to its walk (COMPILE_DEBT)"}
  - {from: sequence, to: beha, disposition: CALL, link: none,
     why: "THE NUMBERS WALK 3b (2026-09-10) | the sequential run's REGISTRATION edge — ('cold_run_beha', 'law_beha') in DAEMON_ORDER (the runner compiles no verse: link none, O4's license)"}
'''
    a = "  - {from: sequence, to: naso, disposition: CALL, link: none,"
    i = text.index(a); j = text.index('\n', text.index('why:', i)) + 1
    text = text[:j] + edges + text[j:]
    open(path, 'w', encoding='utf-8').write(text)
dep = yaml.safe_load(open(path, encoding='utf-8'))
assert 'beha' in str(dep)[:60000]
print('dependency: span + 7 edges (beha)')
# ---- the installation probe's count ----
path = f"{ROOT}/World/step9/installation_probes.py"
text = open(path, encoding='utf-8').read()
a = "len(real) == 49 and all('given_at' in d and 'installed_by' in d for d in real.values())   # THE NUMBERS WALK 2b (2026-09-10): 48 -> 49, law_naso;"
if a in text:
    text = text.replace(a, "len(real) == 50 and all('given_at' in d and 'installed_by' in d for d in real.values())   # THE NUMBERS WALK 3b (2026-09-10): 49 -> 50, law_beha; 2b: 48 -> 49, law_naso;")
    open(path, 'w', encoding='utf-8').write(text)
print('installation_probes I5: 50')
