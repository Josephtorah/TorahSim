#!/usr/bin/env python3
# THE NUMBERS WALK sitting 2b — THE COMPILE OF NASO (2026-09-10; World/step9/NUMBERS_WALK.md "Sitting 2b"): THE TYPES FIRST — eleven kinds on
# the tape (five SPEECH, six ACTS), eight CASE kinds for the exam's scene, fourteen effects, fourteen entities, the 49th daemon's block, the
# functions block, the dependency span and edges, the installation probe's count. The `he` built from the pointed DB text (cantillation
# stripped), the witnesses the plain consonantal runs; every index range FOUND by the consonantal word, never typed. Idempotent
# (add_types_bamidbar.py's form).
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
SUB = "submitted by cold_run_naso.py [subjects: %s] (the narrative scene, THE NUMBERS WALK 2b); re-submitted on the sequential tape by cold_run_sequence.py; consumed by law_naso (cold_run_naso.py) -> %s"
CASE = "submitted by cold_run_naso.py [subjects: the exam's persons] (the wrap's scene); consumed by law_naso (cold_run_naso.py) -> %s"
KINDS = [
 ("gershon_service_commanded", "speech",
  "the Gershonites' count and service commanded — 'lift the head of the sons of Gershon, them also, by their fathers' house, by their families; from thirty years old and upward until fifty you shall count them, everyone who comes to host the host, to work the work in the tent of meeting' (Num 4:22-23); their burden the soft — the curtains, the tent, its covering, the screens, the cords (4:25-26); by the mouth of Aaron and his sons, in the hand of Ithamar (4:27-28)",
  P(N, 4, 22, 'נשא', 'למשפחתם') + " (lift the head of the sons of Gershon, them also — Num 4:22)", ["Num 4:22 | " + L(N, 4, 22, 'נשא', 'למשפחתם')],
  "Num 4:21-28; Onkelos Num 4:21-28 (receive the sum; to host the host; handed over; Ithamar's hand); Arakhin 11a:17 (4:47's 'service of service' = the song)",
  "num_04_gershon_merari (STEP_Nm_4_21, STEP_Nm_4_22, STEP_Nm_4_24; claims NS04A-02, NS04A-04)", SUB % ("the-levites", "commanded (the count's debit, closed by the work-count)"), ["house", "ages", "burden", "under"]),
 ("merari_service_commanded", "speech",
  "the Merarites' count and service commanded — 'the sons of Merari by their families, by their fathers' house you shall count them; from thirty years old and upward until fifty' (Num 4:29-30); their burden the hard — the frames, the bars, the pillars, the sockets, the pegs, the cords, 'and by names you shall appoint the vessels of the charge of their burden' (4:31-32); in the hand of Ithamar (4:33)",
  P(N, 4, 29, 'בני', 'אתם') + " (the sons of Merari... you shall count them — Num 4:29)", ["Num 4:29 | " + L(N, 4, 29, 'בני', 'אתם')],
  "Num 4:29-33; Onkelos Num 4:29-33 (the frames, the bars; by names)",
  "num_04_gershon_merari (STEP_Nm_4_29, STEP_Nm_4_31; claims NS04A-02)", SUB % ("the-levites", "commanded (the count's debit, closed by the work-count)"), ["house", "ages", "burden", "by_names", "under"]),
 ("levites_work_counted", "act",
  "the work-count taken — 'and Moses and Aaron and the princes of the congregation counted the sons of the Kohathite... everyone who comes to the host for the work in the tent of meeting; their counted were two thousand seven hundred and fifty' (Num 4:34-36), Gershon two thousand six hundred and thirty (4:38-40), Merari three thousand two hundred (4:42-44), 'all the counted... eight thousand five hundred and eighty' (4:46-48) — the four numbers by the engine's parser; 'by the mouth of the LORD by the hand of Moses' (4:37, 4:45, 4:49; 4:41 'by the mouth of the LORD'); the three counts CLOSE the Kohathites' service debit of Bamidbar and the two counts commanded here",
  P(N, 4, 34, 'ויפקד', 'אבתם') + " (and Moses and Aaron and the princes of the congregation counted the sons of the Kohathite — Num 4:34) · " + P(N, 4, 48, 'ויהיו', 'ושמנים') + " (and their counted were eight thousand five hundred and eighty — Num 4:48)",
  ["Num 4:34 | " + L(N, 4, 34, 'ויפקד', 'אבתם'), "Num 4:48 | " + L(N, 4, 48, 'ויהיו', 'ושמנים')],
  "Num 4:34-49; Onkelos Num 4:34-49 (the numerals; by the Word of the LORD by the hand of Moses); Chullin 24a:8-12 (the ages — credited at Bamidbar); Arakhin 11a:17 (the song)",
  "num_04_gershon_merari (STEP_Nm_4_34, STEP_Nm_4_36, STEP_Nm_4_46, STEP_Nm_4_48; claims NS04A-01, NS04A-03, NS04A-05)", SUB % ("the-levites", "work_counted (the status with the four numbers); the three debits CLOSED"), ["counts", "total", "princes_joined"]),
 ("send_out_commanded", "speech",
  "the unclean sent out — the command: 'command the children of Israel that they send out of the camp every leper and everyone with an issue and everyone unclean by a corpse; male and female alike you shall send out, outside the camp you shall send them, that they not defile their camps in whose midst I dwell' (Num 5:2-3) — the three classes; 'their camps' plural (the three camps: the leper out of all, the zav out of two, the corpse-unclean out of one — Pesachim 67a; the Sifrei 1:3-4); Onkelos 'MY SHEKHINAH dwells'; R. Levi: one of the eight sections said on the day the tabernacle was erected (Gittin 60a:17 — the reading-placed retrograde marker)",
  P(N, 5, 2, 'צו', 'לנפש') + " (command the children of Israel that they send out of the camp every leper and every zav and everyone unclean by a corpse — Num 5:2) · " + P(N, 5, 3, 'מזכר', 'תשלחום') + " (male and female you shall send out, outside the camp you shall send them — Num 5:3)",
  ["Num 5:2 | " + L(N, 5, 2, 'צו', 'לנפש'), "Num 5:3 | " + L(N, 5, 3, 'מזכר', 'תשלחום')],
  "Num 5:1-3; Onkelos Num 5:1-3 (My Shekhinah); Sifrei Bamidbar 1:1-1:7 (the warning for 19:20's punishment; the three camps; male and female); Pesachim 67a:7-12, 66b:13, 95b:14-17 (the ladder; the Passover in impurity); Eruvin 104b:10, Niddah 28b:1 (who is sent); Makkot 14b:6 (lashes); Gittin 60a:17 (the day)",
  "num_05_camp_pure_theft (STEP_Nm_5_1, STEP_Nm_5_2, STEP_Nm_5_3; claims NS05A-01..03)", SUB % ("israel", "commanded (the send-out owed)"), ["classes", "camps", "male_and_female", "spoken_day"]),
 ("unclean_sent_out", "act",
  "the unclean sent out — the run: 'and the children of Israel did so, and sent them out, outside the camp; as the LORD spoke to Moses, so did the children of Israel' (Num 5:4) — the doubled report (the Sifrei 1:8: before the calf / after); the debit closed",
  P(N, 5, 4, 'ויעשו', 'למחנה') + " (and the children of Israel did so, and sent them out, outside the camp — Num 5:4)", ["Num 5:4 | " + L(N, 5, 4, 'ויעשו', 'למחנה')],
  "Num 5:4; Onkelos Num 5:4; Sifrei Bamidbar 1:8 (the run's doubling read)",
  "num_05_camp_pure_theft (STEP_Nm_5_4; claim NS05A-01)", SUB % ("the-unclean-of-the-camp", "sent_outside_the_camp (the status by class); israel's debit CLOSED"), ["classes", "as_spoken"]),
 ("wagons_brought", "act",
  "the wagons brought — 'and the princes of Israel, the heads of their fathers' houses — they are the princes of the tribes, they who stood over the counted — brought near; and they brought their offering before the LORD: six covered wagons and twelve oxen, a wagon for two princes and an ox for one, and they brought them before the tabernacle' (Num 7:2-3) — the numbers by the parser after the construct rule ([6, 12, 2, 1]); 'covered' (Rebbi — Onkelos' word); on the day Moses finished setting up the tabernacle (7:1 — the erection's day: RETROGRADE)",
  P(N, 7, 2, 'ויקריבו', 'הפקדים') + " (and the princes of Israel... they who stood over the counted, brought near — Num 7:2) · " + P(N, 7, 3, 'ויביאו', 'המשכן') + " (and they brought their offering before the LORD: six covered wagons and twelve oxen... — Num 7:3)",
  ["Num 7:2 | " + L(N, 7, 2, 'ויקריבו', 'הפקדים'), "Num 7:3 | " + L(N, 7, 3, 'ויביאו', 'המשכן')],
  "Num 7:1-3; Onkelos Num 7:1-3 (the day; covered; the numerals); Sifrei Bamidbar 44:1-45:1 (the day-stack; the princes; covered; a wagon for two)",
  "num_07_carts_offerings_a (STEP_Nm_7_1, STEP_Nm_7_2, STEP_Nm_7_3; claims NS07A-01, NS07A-02)", SUB % ("the-princes-of-israel", "wagons_brought (the status with the numbers)"), ["wagons", "oxen", "per_prince", "day"]),
 ("wagons_accepted_commanded", "speech",
  "the wagons accepted — 'and the LORD said to Moses: take from them, and they shall be for the service of the tent of meeting, and you shall give them to the Levites, each according to his service' (Num 7:4-5) — not accepted until told (the Sifrei 45:1)",
  P(N, 7, 5, 'קח', 'עבדתו') + " (take from them, and they shall be for the service of the tent of meeting, and you shall give them to the Levites, each according to his service — Num 7:5)", ["Num 7:5 | " + L(N, 7, 5, 'קח', 'עבדתו')],
  "Num 7:4-5; Onkelos Num 7:4-5; Sifrei Bamidbar 45:1 (not accepted until told)",
  "num_07_carts_offerings_a (STEP_Nm_7_4; claim NS07A-02)", SUB % ("moses", "commanded (the distribution owed)"), ["from", "to", "by_service"]),
 ("wagons_assigned", "act",
  "the wagons assigned — 'and Moses took the wagons and the oxen and gave them to the Levites: two wagons and four oxen to the sons of Gershon by their service, and four wagons and eight oxen to the sons of Merari by their service, in the hand of Ithamar; and to the sons of Kohath he gave none, for the service of the holy is upon them — on the shoulder they carry' (Num 7:6-9) — as Moses saw fit (the Sifrei 46:1); David's error and return (46:2 — the flow reversed); the debit closed",
  P(N, 7, 6, 'ויקח', 'הלוים') + " (and Moses took the wagons and the oxen and gave them to the Levites — Num 7:6) · " + P(N, 7, 9, 'ולבני', 'ישאו') + " (and to the sons of Kohath he gave none... on the shoulder they carry — Num 7:9)",
  ["Num 7:6 | " + L(N, 7, 6, 'ויקח', 'הלוים'), "Num 7:9 | " + L(N, 7, 9, 'ולבני', 'ישאו')],
  "Num 7:6-9; Onkelos Num 7:6-9; Sifrei Bamidbar 46:1-2 (as he saw fit; David's wagon); Sotah 35a:22 (David's error); Arakhin 11a:19 ('they carry' as song)",
  "num_07_carts_offerings_a (STEP_Nm_7_6, STEP_Nm_7_9; claim NS07A-03)", SUB % ("the-levites", "wagons_assigned (the transfer by house: 2/4 Gershon, 4/8 Merari, Kohath none); moses' debit CLOSED"), ["gershon", "merari", "kohath", "under"]),
 ("dedication_brought", "act",
  "the dedication brought — 'and the princes brought near the dedication of the altar on the day it was anointed, and the princes brought near their offering before the altar' (Num 7:10) — all on the anointing day (the erection's, 1 Nisan — Zevachim 101b:6's three goats); the body's debit: to be offered by days",
  P(N, 7, 10, 'ויקריבו', 'אתו') + " (and the princes brought near the dedication of the altar on the day it was anointed — Num 7:10)", ["Num 7:10 | " + L(N, 7, 10, 'ויקריבו', 'אתו')],
  "Num 7:10; Onkelos Num 7:10; Sifrei Bamidbar 47:1 (the order Moses did not know); Zevachim 101b:6 (the three goats of one day); Sifrei 53:1 (7:84 = 7:88, the same day)",
  "num_07_carts_offerings_a (STEP_Nm_7_10; claim NS07A-04)", SUB % ("the-princes-of-israel", "dedication_brought (the debit the twelfth day's offering closes)"), ["day", "before"]),
 ("dedication_order_commanded", "speech",
  "the dedication's order commanded — 'and the LORD said to Moses: one prince per day, one prince per day, they shall bring near their offering for the dedication of the altar' (Num 7:11) — THE SCHEDULE: twelve dues from the anointing day, one per day in the camp's order (2:3-31 = 7:12-83, computed), the Sabbath overridden (Moed Katan 9a:11-12 — 'on the day of the eleventh day'); inside the retrograde stretch the engine writes each due at submission as a RETRO-WRITE",
  P(N, 7, 11, 'נשיא', 'המזבח') + " (one prince per day, one prince per day, they shall bring near their offering for the dedication of the altar — Num 7:11)", ["Num 7:11 | " + L(N, 7, 11, 'נשיא', 'המזבח')],
  "Num 7:11-88; Onkelos Num 7:11-88 (the sela; the numerals); Sifrei Bamidbar 47:1-57:1 (the order by the journeying; each on his day; the dish by the sanctuary shekel; the 120 decides; one of each; the four exceptions; the totals); Moed Katan 9a:11-12 (the Sabbath overridden); Menachot 8a-8b, 88a, Zevachim 88a (the vessels); Menachot 92b:7 (Nahshon's goat); Chagigah 23b:7, Pesachim 19a:8 (the pan joins)",
  "num_07_carts_offerings_a (STEP_Nm_7_11, STEP_Nm_7_12, STEP_Nm_7_13, STEP_Nm_7_14; claims NS07A-04..07); num_07_offerings_b_total (STEP_Nm_7_84, STEP_Nm_7_85, STEP_Nm_7_86; claims NS07B-01..03)", SUB % ("the-princes-of-israel", "dedication_offered on each prince (twelve retro-writes with their days); the body's dedication_brought CLOSED by the twelfth"), ["per_day", "order", "days"]),
 ("voice_heard_from_the_ark", "act",
  "the Voice heard from the ark — 'and when Moses came into the tent of meeting to speak with Him, he heard the Voice speaking itself to him from above the ark-cover that is upon the ark of the testimony, from between the two cherubim; and He spoke to him' (Num 7:89) — the reflexive by the points (the reading's NS07B-04); Lev 1:1 against Exod 25:22 reconciled here (I13 — the Sifrei 58:1); Moses alone heard (Yoma 4b:8)",
  P(N, 7, 89, 'ובבא', 'הכרבים') + " (and when Moses came into the tent of meeting to speak with Him, he heard the Voice speaking itself to him from above the ark-cover... from between the two cherubim — Num 7:89)", ["Num 7:89 | " + L(N, 7, 89, 'ובבא', 'הכרבים')],
  "Num 7:89; Onkelos Num 7:89 (both verbs reflexive); Sifrei Bamidbar 58:1-2 (the third verse; the thirteen exclusions; not a low voice); Yoma 4b:8 (unto him — Moses alone)",
  "num_07_offerings_b_total (STEP_Nm_7_89; claims NS07B-04..06)", SUB % ("moses", "spoken_to_from_the_ark (the status: the Voice speaking itself, between the cherubim)"), ["reflexive", "from", "who_heard"]),
 ("send_out_case", "case",
  "who is sent out and from which camp — the exam's case on 5:2-3: the leper (out of all three camps), the zav (out of two), the corpse-unclean (out of one — the Presence's); the purifiable only (not a creeping thing's carcass); male and female (not the tumtum); the tent rolled up; the Passover in impurity; the impure who entered (lashes)",
  P(N, 5, 2, 'וישלחו', 'לנפש') + " (that they send out of the camp every leper and every zav and everyone unclean by a corpse — Num 5:2)", ["Num 5:2 | " + L(N, 5, 2, 'וישלחו', 'לנפש')],
  "Num 5:2-4; Pesachim 67a-b, 92a, 95b; Eruvin 104b; Niddah 28b; Makkot 14b-15a; Mishnah Makkot 3:2; Mishnah Kelim 1:5-8; Taanit 21b; Zevachim 117a; Sifrei Bamidbar 1:3-1:5",
  "num_05_camp_pure_theft (STEP_Nm_5_2; claim NS05A-01)", CASE % "sent_outside_the_camp / exempt / lashes", ["person", "who", "camp_entered", "tent_standing", "majority_impure"]),
 ("theft_confessed_case", "case",
  "the confessed theft and its restitution — the exam's case on 5:6-8: the confession, the principal 'at its head', the fifth (its base disputed), the ram after the money; the proselyte who died without heirs (to the priests of the watch); the robber who died on the way; the priest-thief; the woman equal to the man; R. Natan's creditor's creditor; the fifth on the fifth",
  P(N, 5, 7, 'והתודו', 'לו') + " (and they shall confess their sin which they did, and he shall return his guilt at its head and add its fifth to it, and give it to him against whom he was guilty — Num 5:7)", ["Num 5:7 | " + L(N, 5, 7, 'והתודו', 'לו')],
  "Num 5:5-8; Mishnah Bava Kamma 9:5-12; Bava Kamma 106a, 109a-111a; Arakhin 28b; Sifrei Bamidbar 2:1-4:2; Mishnah Sanhedrin 6:2; Lev 5:20-26 (the guilt cell CALLED)",
  "num_05_camp_pure_theft (STEP_Nm_5_5, STEP_Nm_5_6, STEP_Nm_5_7; claims NS05A-04..06)", CASE % "guilt_acknowledged / pays / adds_fifth / due_to_priest", ["person", "ask", "victim", "heirs", "swore", "confessed", "value", "means", "died"]),
 ("gifts_case", "case",
  "the priest's gifts — the exam's case on 5:9-10: 'every man's hallowed things shall be his; what a man gives the priest, his it shall be' — the owner's choice of priest, the terumah's measure, the blemished priest's own offering (its flesh and hide his), the firstborn's thirty days (Bamidbar's cell CALLED), the tithe Onkelos inserts",
  P(N, 5, 10, 'ואיש', 'יהיה') + " (and every man's hallowed things shall be his; what a man gives the priest, his it shall be — Num 5:10)", ["Num 5:10 | " + L(N, 5, 10, 'ואיש', 'יהיה')],
  "Num 5:9-10; Bava Kamma 109b:16, 110a:9; Arakhin 34a:6; Mishnah Terumot 4:5; Sifrei Bamidbar 5:1-6:1; Bekhorot 49a (credited)",
  "num_05_camp_pure_theft (STEP_Nm_5_9, STEP_Nm_5_10; claim NS05A-07)", CASE % "due_to_priest / exempt", ["person", "ask", "priest", "measure", "age_days"]),
 ("sotah_case", "case",
  "the suspected wife — the exam's case on 5:11-31: warned before witnesses, secluded the measure of defilement, the doubt; who drinks and who does not (the betrothed, the widow awaiting the levir, the forbidden marriages, the ailonit, the convert, the priest's wife, the eunuch's wife); the husband clean, the husband first; the witnesses (one for defilement, two for the seclusion; overseas; conspiring); the rite (the court, the gate, the uncovering, the water and dust, the vessel, the scroll — its text, material, ink, order, erasure, time, for her name; the oath — any language, the innocent clause first, amen amen, two oaths; the minchah — barley, no oil no frankincense, waved by her hand, brought near, not for its name; the order of drinking and offering; refusal before and after the erasure); the outcomes (guilty: the paramour too; merit suspends; innocent: cleared, conceives); the consequences (her husband, her paramour, the priesthood, terumah, levirate, the ketubah); the abolition",
  P(N, 5, 12, 'איש', 'מעל') + " (any man whose wife goes aside and commits a trespass against him — Num 5:12)", ["Num 5:12 | " + L(N, 5, 12, 'איש', 'מעל')],
  "Num 5:11-31; Mishnah Sotah 1-6, 7:1, 9:9; Sotah 2a-31a's link rows; Kiddushin 27b, 36b, 62a; Ketubot 51b, 72a, 74a, 81a; Shevuot 5a, 29b, 32a, 35b-36a; Yevamot 11a, 38b, 56b, 58a; Menachot 4a, 59a-61a; Keritot 9b, 24a, 26a; Temurah 12b; Nedarim 73a; Berakhot 15b, 31b; Eruvin 13a-b; Megillah 20b; Mishnah Eduyot 5:6; Mishnah Menachot 5:3, 5:6; Sifrei Bamidbar 7:1-21:3",
  "num_05_sotah (STEP_Nm_5_11 ... STEP_Nm_5_31; claims NS05B-01..11)", CASE % "tested_by_the_waters / forbidden_to_her_husband / ketubah_forfeited / exempt / disqualified / accepted / not_accepted", ["person", "ask", "warned_before", "secluded", "witnesses", "status", "husband_clean", "husband_first", "confessed", "refuses_when", "merit", "guilty", "language", "who"]),
 ("nazirite_case", "case",
  "the nazirite — the exam's case on 6:1-21: the vow (substitutes, intimations, conditions, errors, chains, who vows, the ages), the term (thirty by default; the forms), the three prohibitions (the vine's products, amounts, combination, the taste; the razor and every means; the corpse — kinds, modes, the met mitzvah, the High Priest beside him), what negates (impurity all, shaving thirty, wine nothing; the first days; the last day; unknown impurity), the defiled nazirite's week (sprinkled, shaved on the seventh, the birds and the lamb on the eighth, the recount day), the completion (the three animals, the loaves, the libations, the shaving where the peace-offering is cooked, the hair under the pot, the foreleg on the palms, waved, then wine), the leper-nazirite, the funds, the woman's nullification, lashes per warning, the doubtful cases",
  P(N, 6, 2, 'כי', 'ליהוה') + " (when a man or woman shall clearly utter a vow, the vow of a nazirite, to separate himself to the LORD — Num 6:2)", ["Num 6:2 | " + L(N, 6, 2, 'כי', 'ליהוה')],
  "Num 6:1-21; Mishnah Nazir 1-9; Nazir 2a-66b's link rows; Mishnah Nedarim 1:1; Mishnah Niddah 5:6; Mishnah Kinnim 1:1, 2:5; Mishnah Keritot 2:2; Mishnah Meilah 3:2; Mishnah Makkot 3:7-8; Mishnah Chullin 10:4; Mishnah Zevachim 5:5; Mishnah Tahorot 4:7, 4:12; Mishnah Sotah 3:8; Menachot 27a, 46b-47a, 73a, 78a, 91a-b; Pesachim 23a, 41b, 43b-45a, 80b-81b; Kiddushin 36b, 57b; Keritot 2b, 9a-b, 13b; Temurah 10a, 28a, 34a; Nedarim 3a-5b, 18a; Chullin 98a, 134b; Zevachim 4b, 8a, 23b, 55a, 100a; Yevamot 5a, 7a; Megillah 3b; Berakhot 19b; Sanhedrin 22b, 35a; Taanit 11a, 17a; Moed Katan 19b; Yoma 16a; Sifrei Bamidbar 22:1-38:1",
  "num_06_nazir (STEP_Nm_6_1 ... STEP_Nm_6_21; claims NS06A-01..10)", CASE % "nazirite_vow_bound / nazirite_term_fulfilled / count_voided / lashes / karet_cut_off / exempt / disqualified / accepted / due_to_priest", ["person", "ask", "form", "term", "who", "age", "product", "amount", "means", "source", "mode", "day", "on_the_way_to", "which", "allocated", "warnings"]),
 ("blessing_case", "case",
  "the priests' blessing — the exam's case on 6:22-27: the form (the holy tongue, standing, the raised hands, the Name in the Temple and the substitute in the province, one blessing or three, face to face, aloud, the prompter), who blesses (a priest; not the blemished-hands, the drunk, the minor, the exposed), the quorum, who is blessed (all Israel — converts, women, freed slaves), read not translated, the three commands, the priests blessed by Heaven, the face lifted",
  P(N, 6, 23, 'כה', 'להם') + " (thus shall you bless the children of Israel; say to them — Num 6:23)", ["Num 6:23 | " + L(N, 6, 23, 'כה', 'להם')],
  "Num 6:22-27; Mishnah Sotah 7:6; Mishnah Tamid 7:2; Mishnah Megillah 4:3-7, 4:10; Sotah 33b, 38a-b; Menachot 44a; Chullin 49a; Taanit 26b; Megillah 25a-b; Berakhot 20b; Niddah 70b; Sifrei Bamidbar 39:1-43:1",
  "num_06_priest_blessing (STEP_Nm_6_22 ... STEP_Nm_6_27; claims NS06B-01..05)", CASE % "blessed_by_the_priests / exempt / disqualified", ["person", "ask", "who", "place", "language", "count"]),
 ("dedication_case", "case",
  "the dedication offering — the exam's case on 7:10-88: the order (by the journeying, not by birth), the vessels (the dish by the sanctuary shekel, the pan of ten weighed in silver, full — the vessel sanctifies, the bowls sanctify dry, the pan joins its contents), the animals (one of each — none like it; the animal's own year; Nahshon's goat's leaning; the sin-offering for the grave of the depths), the prince's exceptions (the Sabbath overridden, an individual's incense, a sin-offering not for a sin), the totals credited to each, the same day",
  P(N, 7, 13, 'וקרבנו', 'אחת') + " (and his offering: one silver dish — Num 7:13)", ["Num 7:13 | " + L(N, 7, 13, 'וקרבנו', 'אחת')],
  "Num 7:10-88; Sifrei Bamidbar 47:1-57:1; Moed Katan 9a; Menachot 8a-b, 19b, 88a, 92b; Zevachim 88a, 101b; Chagigah 23b; Pesachim 19a; Yoma 47a; Mishnah Parah 1:3; Sanhedrin 16b, Shevuot 15a, Menachot 57b (the anointing); Horayot 12a",
  "num_07_carts_offerings_a (STEP_Nm_7_12, STEP_Nm_7_13, STEP_Nm_7_14, STEP_Nm_7_15, STEP_Nm_7_16, STEP_Nm_7_17; claims NS07A-04..07); num_07_offerings_b_total (STEP_Nm_7_84, STEP_Nm_7_85, STEP_Nm_7_86, STEP_Nm_7_87, STEP_Nm_7_88; claims NS07B-01..03)", CASE % "accepted / disqualified / exempt", ["person", "ask", "prince", "day", "vessel", "animal", "age_months"]),
 ("work_count_case", "case",
  "the Levites' work — the exam's case on 4:21-49: the ages (thirty to fifty — Bamidbar's fitness cell CALLED), the service of service (the song), the houses' loads (the soft, the hard; the holy Kohath's), the shares against chapter 3, the princes among the counters, the closing formula's variant",
  P(N, 4, 47, 'מבן', 'מועד') + " (from thirty years old and upward until fifty... the service of service and the service of burden in the tent of meeting — Num 4:47)", ["Num 4:47 | " + L(N, 4, 47, 'מבן', 'מועד')],
  "Num 4:21-49; Arakhin 11a:17-19; Chullin 24a:8-12 (credited); Shabbat 28a:2 (4:25's tent); Ketubot 45b:10, Zevachim 59b:10 (4:26's seats)",
  "num_04_gershon_merari (STEP_Nm_4_23, STEP_Nm_4_47; claims NS04A-01, NS04A-04)", CASE % "appointed_to_serve / exempt / charge_kept", ["person", "ask", "who", "age", "house", "carrying"]),
]
EFFECTS = [
 ("work_counted", "status", "work-counted — the STATUS the work-count writes on the tribe of Levi with THE FOUR NUMBERS: Kohath 2,750 (Num 4:36), Gershon 2,630 (4:40), Merari 3,200 (4:44), all 8,580 (4:48) — computed from the ink by the engine's parser; the three counts close the debits commanded (4:2, 4:22, 4:29)",
  P(N, 4, 48, 'ויהיו', 'ושמנים') + " (and their counted were eight thousand five hundred and eighty — Num 4:48)", "Num 4:34-49; Onkelos Num 4:34-49", "num_04_gershon_merari (STEP_Nm_4_48; claim NS04A-01)", "law_naso (cold_run_naso.py) on levites_work_counted"),
 ("sent_outside_the_camp", "status", "sent outside the camp — the STATUS the send-out writes on the unclean of the camp BY CLASS: the leper out of all three camps, the zav out of two, the corpse-unclean out of one (Num 5:2-4; 'their camps' plural — Pesachim 67a; the Sifrei 1:3-4)",
  P(N, 5, 4, 'וישלחו', 'למחנה') + " (and sent them out, outside the camp — Num 5:4)", "Num 5:2-4; Onkelos; Sifrei Bamidbar 1:3-1:4, 1:7; Pesachim 67a:11-12; Mishnah Kelim 1:7-8", "num_05_camp_pure_theft (STEP_Nm_5_2, STEP_Nm_5_4; claim NS05A-01)", "law_naso (cold_run_naso.py) on unclean_sent_out and send_out_case"),
 ("wagons_assigned", "transfer", "the wagons assigned — the TRANSFER Moses' distribution writes to the Levites by house: two wagons and four oxen to Gershon, four and eight to Merari, none to Kohath (Num 7:6-9) — as he saw fit (the Sifrei 46:1); 'on the shoulder they carry' the negative clause (46:2: David's error)",
  P(N, 7, 6, 'ויתן', 'הלוים') + " (and gave them to the Levites — Num 7:6)", "Num 7:6-9; Onkelos; Sifrei Bamidbar 46:1-2; Sotah 35a:22", "num_07_carts_offerings_a (STEP_Nm_7_6, STEP_Nm_7_9; claim NS07A-03)", "law_naso (cold_run_naso.py) on wagons_assigned"),
 ("dedication_brought", "debit", "the dedication brought — the DEBIT the princes' bringing writes on their body: 'the princes brought near the dedication of the altar on the day it was anointed' (Num 7:10) — brought together, to be OFFERED by days (7:11); closed by the twelfth day's offering (7:78-83)",
  P(N, 7, 10, 'ויקריבו', 'אתו') + " (and the princes brought near the dedication of the altar on the day it was anointed — Num 7:10)", "Num 7:10-11, 7:84-88; Onkelos; Sifrei Bamidbar 47:1, 53:1", "num_07_carts_offerings_a (STEP_Nm_7_10, STEP_Nm_7_11; claim NS07A-04)", "law_naso (cold_run_naso.py) on dedication_brought; closed on the twelfth retro-write"),
 ("dedication_offered", "status", "the dedication offered — the STATUS each prince's day writes on him with HIS DAY and his offering's numbers: 'and he who brought near his offering on the first day was Nahshon son of Amminadab of the tribe of Judah' (Num 7:12) ... the twelfth day Ahira son of Enan (7:78) — the twelve days one continuous period (Moed Katan 9a), one prince per day from the anointing day (7:11): inside the retrograde stretch each due is a RETRO-WRITE at submission",
  P(N, 7, 12, 'ויהי', 'יהודה') + " (and he who brought near his offering on the first day was Nahshon son of Amminadab of the tribe of Judah — Num 7:12)", "Num 7:12-83; Onkelos; Sifrei Bamidbar 47:1-52:1, 57:1; Moed Katan 9a:11-12", "num_07_carts_offerings_a (STEP_Nm_7_12; claims NS07A-04, NS07A-05); num_07_offerings_b_total (STEP_Nm_7_84; claim NS07B-01)", "law_naso (cold_run_naso.py) on dedication_order_commanded — twelve dues"),
 ("tested_by_the_waters", "status", "tested by the waters — the STATUS the drinking writes on the suspected wife: 'and he shall make her drink the water, and it shall be, if she was defiled... the waters that cause the curse shall enter her for bitterness, and her belly shall swell and her thigh fall' (Num 5:27); 'and if the woman was not defiled but is clean, she shall be cleared and sown with seed' (5:28) — the value guilty / innocent / suspended (merit)",
  P(N, 5, 27, 'והשקה', 'עמה') + " (and he shall make her drink the water... and the woman shall be a curse among her people — Num 5:27)", "Num 5:24-28; Onkelos; Sifrei Bamidbar 15:1-19:1; Mishnah Sotah 3:2-5; Sotah 20b:14", "num_05_sotah (STEP_Nm_5_24, STEP_Nm_5_27, STEP_Nm_5_28; claims NS05B-08..10)", "law_naso (cold_run_naso.py) on sotah_case"),
 ("forbidden_to_her_husband", "status", "forbidden to her husband — the STATUS the doubt writes on the warned and secluded wife until the waters clear her (Num 5:14 'and she was defiled... and she was not defiled' — the doubtful case, Sotah 28a:21; Mishnah Sotah 1:2 'forbidden to her home'), and the guilty verdict's consequence with her paramour, the priesthood and terumah (5:29's 'and is defiled' — R. Akiva's four)",
  P(N, 5, 29, 'זאת', 'ונטמאה') + " (this is the law of jealousies, when a wife goes aside under her husband and is defiled — Num 5:29)", "Num 5:14, 5:29; Sotah 28a:19-21, 29a:2; Mishnah Sotah 1:2, 5:1", "num_05_sotah (STEP_Nm_5_14, STEP_Nm_5_29; claims NS05B-01, NS05B-11)", "law_naso (cold_run_naso.py) on sotah_case"),
 ("ketubah_forfeited", "transfer", "the marriage contract forfeited — the TRANSFER the exam's rows write on the wife who neither drinks nor collects (Mishnah Sotah 4:1-3, 1:5's receipt): the betrothed, the widow awaiting the levir, the forbidden marriages, the confessed, the refusing; the ink's own seat 5:31 'and that woman shall bear her iniquity' (the contract the shelf's institution, said so)",
  P(N, 5, 31, 'והאשה', 'עונה') + " (and that woman shall bear her iniquity — Num 5:31)", "Num 5:31; Mishnah Sotah 1:5, 4:1-3, 6:1-2; Ketubot 81a; Yevamot 38b", "num_05_sotah (STEP_Nm_5_31; claim NS05B-11)", "law_naso (cold_run_naso.py) on sotah_case"),
 ("nazirite_vow_bound", "status", "bound by the nazirite vow — the STATUS the vow writes on the vower with his TERM (thirty by default — the data row; the forms of Mishnah Nazir 1:3-7) and the three prohibitions (Num 6:3-8): 'when a man or woman shall clearly utter a vow, the vow of a nazirite, to separate himself to the LORD' (6:2); the term's due a TIMER on the scene (fulfilled at its end, re-set by a defilement)",
  P(N, 6, 2, 'כי', 'ליהוה') + " (when a man or woman shall clearly utter a vow, the vow of a nazirite, to separate himself to the LORD — Num 6:2)", "Num 6:1-8; Onkelos; Sifrei Bamidbar 22:1-27:1; Mishnah Nazir 1-2; Nedarim 3a, 18a; Nazir 5a", "num_06_nazir (STEP_Nm_6_2 ... STEP_Nm_6_8; claims NS06A-01..05)", "law_naso (cold_run_naso.py) on nazirite_case"),
 ("nazirite_term_fulfilled", "status", "the nazirite's term fulfilled — the STATUS the completion writes: 'and this is the law of the nazirite on the day the days of his separation are fulfilled: he shall bring himself to the door of the tent of meeting' (Num 6:13) — the three animals, the loaves, the shaving where the peace-offering is cooked, the foreleg on his palms, waved, 'and after that the nazirite may drink wine' (6:20)",
  P(N, 6, 13, 'וזאת', 'מועד') + " (and this is the law of the nazirite on the day the days of his separation are fulfilled — Num 6:13)", "Num 6:13-21; Onkelos; Sifrei Bamidbar 32:1-38:1; Mishnah Nazir 6:7-11; Nazir 45a-46b", "num_06_nazir (STEP_Nm_6_13 ... STEP_Nm_6_21; claims NS06A-08..10)", "law_naso (cold_run_naso.py) on nazirite_case (the timer's fire)"),
 ("count_voided", "status", "the count voided — the STATUS a defilement writes on the nazirite: 'and the former days shall fall, for his separation was defiled' (Num 6:12) — impurity voids all (the recount from the eighth day — Rebbi; the seventh — R. Yosei b. R. Yehuda), shaving voids thirty (Mishnah Nazir 6:5), wine voids nothing (Nazir 44a)",
  P(N, 6, 12, 'והימים', 'נזרו') + " (and the former days shall fall, for his separation was defiled — Num 6:12)", "Num 6:9-12; Onkelos; Sifrei Bamidbar 28:1-31:1; Mishnah Nazir 3:3-4, 6:5-6; Nazir 44a:11-13, 18a-19b", "num_06_nazir (STEP_Nm_6_9, STEP_Nm_6_12; claims NS06A-06, NS06A-07)", "law_naso (cold_run_naso.py) on nazirite_case"),
 ("blessed_by_the_priests", "status", "blessed by the priests — the STATUS the priests' blessing writes on Israel, and God's on the priests: 'so shall they put My name upon the children of Israel, and I will bless them' (Num 6:27) — the three verses of 3, 5, 7 words (computed at the reading); the form by place (the Name in the Temple, the substitute in the province — Mishnah Sotah 7:6)",
  P(N, 6, 27, 'ושמו', 'אברכם') + " (and they shall put My name upon the children of Israel, and I will bless them — Num 6:27)", "Num 6:22-27; Onkelos; Sifrei Bamidbar 39:1-43:1; Mishnah Sotah 7:6; Mishnah Tamid 7:2; Sotah 38a-b; Chullin 49a", "num_06_priest_blessing (STEP_Nm_6_23, STEP_Nm_6_27; claims NS06B-01, NS06B-05)", "law_naso (cold_run_naso.py) on blessing_case"),
 ("spoken_to_from_the_ark", "status", "spoken to from the ark — the STATUS the Voice writes on Moses: 'he heard the Voice speaking itself to him from above the ark-cover, from between the two cherubim; and He spoke to him' (Num 7:89) — the reflexive stem by the points; Moses alone heard (Yoma 4b:8); Lev 1:1's 'from the tent' reconciled with Exod 25:22's 'from above the ark-cover' by this third verse (I13)",
  P(N, 7, 89, 'וישמע', 'הכרבים') + " (and he heard the Voice speaking itself to him from above the ark-cover that is upon the ark of the testimony, from between the two cherubim — Num 7:89)", "Num 7:89; Onkelos Num 7:89; Sifrei Bamidbar 58:1-2; Yoma 4b:8; Sukkah 5a", "num_07_offerings_b_total (STEP_Nm_7_89; claims NS07B-04..06)", "law_naso (cold_run_naso.py) on voice_heard_from_the_ark"),
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
PRINCES = [('nahshon_ben_amminadab', 'Nahshon son of Amminadab, the prince of Judah — the first day (Num 7:12-17; 1:7, 2:3; 10:14)'), ('nethanel_ben_zuar', 'Nethanel son of Zuar, the prince of Issachar — the second day (7:18-23; 1:8, 2:5; 10:15)'),
           ('eliab_ben_helon', 'Eliab son of Helon, the prince of Zebulun — the third day (7:24-29; 1:9, 2:7; 10:16 with the vav)'), ('elizur_ben_shedeur', 'Elizur son of Shedeur, the prince of Reuben — the fourth day (7:30-35; 1:5, 2:10; 10:18)'),
           ('shelumiel_ben_zurishaddai', 'Shelumiel son of Zurishaddai, the prince of Simeon — the fifth day (7:36-41; 1:6, 2:12; 10:19; Sanhedrin 82b:11 the Zimri identity, an arm unassigned)'), ('eliasaph_ben_deuel', 'Eliasaph son of Deuel, the prince of Gad — the sixth day (7:42-47 with the dalet; 1:14 Deuel; 2:14 Reuel — the dalet/resh recorded; 10:20)'),
           ('elishama_ben_ammihud', 'Elishama son of Ammihud, the prince of Ephraim — the seventh day (7:48-53; 1:10, 2:18; 10:22)'), ('gamaliel_ben_pedahzur', 'Gamaliel son of Pedahzur, the prince of Manasseh — the eighth day (7:54-59, Pedah-zur two tokens; 1:10, 2:20; 10:23)'),
           ('abidan_ben_gideoni', 'Abidan son of Gideoni, the prince of Benjamin — the ninth day (7:60-65; 1:11, 2:22; 10:24 with the vav)'), ('ahiezer_ben_ammishaddai', 'Ahiezer son of Ammishaddai, the prince of Dan — the tenth day (7:66-71; 1:12, 2:25; 10:25)'),
           ('pagiel_ben_ochran', 'Pagiel son of Ochran, the prince of Asher — the eleventh day (7:72-77; 1:13, 2:27; 10:26)'), ('ahira_ben_enan', 'Ahira son of Enan, the prince of Naphtali — the twelfth day (7:78-83; 1:15, 2:29; 10:27)')]
ENT = [("the_princes_of_israel", "people", "the princes of Israel as a body — 'the princes of Israel, the heads of their fathers' houses, they are the princes of the tribes, they who stood over the counted' (Num 7:2): the twelve who brought the wagons (7:2-9) and the dedication (7:10) and offered it by days in the camp's order (7:12-83 = 2:3-31, computed); the census aides of 1:5-16, the standard-bearers of 2, the march's captains of 10:14-27", "the-princes-of-israel")]
ENT += [(pid, "person", en + " — one of the twelve princes (the registry's the_princes_of_israel the body); his day's offering a RETRO-WRITE on the tape (THE NUMBERS WALK 2b)", pid.replace('_', '-')) for pid, en in PRINCES]
ENT += [("the_unclean_of_the_camp", "people", "the unclean of the camp as one body — 'every leper and everyone with an issue and everyone unclean by a corpse' (Num 5:2), sent outside the camp at 5:4 by class (the leper out of all three camps, the zav out of two, the corpse-unclean out of one — Pesachim 67a; the Sifrei 1:3-4); NOT the registry's the_unclean_men (Num 9's second-Passover pleaders)", "the-unclean-of-the-camp")]
added = 0
for eid, kind, en, tok in ENT:
    if eid in ids: continue
    if not text.endswith('\n'): text += '\n'
    text += f"  - id: {eid}\n    en: {q(en)}\n    kind: {kind}\n    members:\n      - {{token: {tok}, units: [step9-scenes]}}   # cold_run_naso.py's narrative scene (THE NUMBERS WALK 2b, 2026-09-10); the frozen units' tokens a later join\n"
    added += 1
if added:
    text = text.replace("#   2026-09-09 THE NUMBERS WALK 1b (World/step9/NUMBERS_WALK.md \"Sitting 1b\"):", "#   2026-09-10 THE NUMBERS WALK 2b (World/step9/NUMBERS_WALK.md \"Sitting 2b\"): the_princes_of_israel (people), the twelve princes in the camp's order (person), the_unclean_of_the_camp (people); each with one step9-scenes member\n#   2026-09-09 THE NUMBERS WALK 1b (World/step9/NUMBERS_WALK.md \"Sitting 1b\"):", 1)
    open(path, 'w', encoding='utf-8').write(text)
reg = yaml.safe_load(open(path, encoding='utf-8'))
assert all(any(e['id'] == eid for e in reg['entities']) for eid, *_ in ENT)
print('entities: %d added, registry %d' % (added, len(reg['entities'])))
# ---- the daemon block + the functions block (daemon_dispositions.yaml) ----
path = f"{ROOT}/World/step9/daemon_dispositions.yaml"
text = open(path, encoding='utf-8').read()
if '  law_naso:' not in text:
    block = '''  law_naso:
    file: cold_run_naso.py
    wraps: naso
    given_at: Num 4:21
    installed_by: boot   # THE NUMBERS WALK 2b (2026-09-10): a law spoken at its verse with no installing act on the tape — the standing setting
    watches:
      gershon_service_commanded: [commanded]                          # 4:22-28: the count and service owed
      merari_service_commanded: [commanded]                           # 4:29-33: the count and service owed
      levites_work_counted: [work_counted]                            # 4:34-49: the four numbers; the three debits CLOSED (Kohath's of Bamidbar, Gershon's, Merari's)
      send_out_commanded: [commanded]                                 # 5:2-3: the send-out owed
      unclean_sent_out: [sent_outside_the_camp]                       # 5:4: the status by class; israel's debit CLOSED
      wagons_brought: [wagons_brought]                                # 7:2-3: the status with the numbers
      wagons_accepted_commanded: [commanded]                          # 7:4-5: the distribution owed
      wagons_assigned: [wagons_assigned]                              # 7:6-9: the transfer by house; moses' debit CLOSED
      dedication_brought: [dedication_brought]                        # 7:10: the debit on the body
      dedication_order_commanded: [dedication_offered]                # 7:11: twelve dues from the anointing day — RETRO-WRITES; the twelfth closes the body's debit
      voice_heard_from_the_ark: [spoken_to_from_the_ark]              # 7:89: the status on Moses
      send_out_case: [sent_outside_the_camp, exempt, lashes]          # the exam's rows on 5:2-4
      theft_confessed_case: [guilt_acknowledged, pays, adds_fifth, due_to_priest]   # the exam's rows on 5:5-8 (Lev 5's cell CALLED)
      gifts_case: [due_to_priest, exempt]                             # the exam's rows on 5:9-10
      sotah_case: [tested_by_the_waters, forbidden_to_her_husband, ketubah_forfeited, exempt, disqualified, accepted, not_accepted]   # the exam's rows on 5:11-31
      nazirite_case: [nazirite_vow_bound, nazirite_term_fulfilled, count_voided, lashes, karet_cut_off, exempt, disqualified, accepted, due_to_priest]   # the exam's rows on 6:1-21
      blessing_case: [blessed_by_the_priests, exempt, disqualified]   # the exam's rows on 6:22-27
      dedication_case: [accepted, disqualified, exempt]               # the exam's rows on 7:10-88
      work_count_case: [appointed_to_serve, exempt, charge_kept]      # the exam's rows on 4:21-49 (Bamidbar's fitness cell CALLED)
'''
    i = text.index('  law_zelophehad:')
    text = text[:i] + block + text[i:]
if '\n  naso:   # THE NUMBERS WALK 2b' not in text:
    fb = '''  naso:   # THE NUMBERS WALK 2b (2026-09-10)
    work_count: {status: WRAPPED, by: law_naso}
    camp_purity: {status: WRAPPED, by: law_naso}
    restitution: {status: WRAPPED, by: law_naso}
    sotah: {status: WRAPPED, by: law_naso}
    nazirite: {status: WRAPPED, by: law_naso}
    blessing: {status: WRAPPED, by: law_naso}
    wagons: {status: WRAPPED, by: law_naso}
    dedication: {status: WRAPPED, by: law_naso}
    voice: {status: WRAPPED, by: law_naso}
'''
    i = text.index('  bamidbar:   # THE NUMBERS WALK 1b (2026-09-09)')
    j = text.index('\n  pre_sinai:', i)
    text = text[:j + 1] + fb + text[j + 1:]
open(path, 'w', encoding='utf-8').write(text)
dd = yaml.safe_load(open(path, encoding='utf-8'))
assert 'law_naso' in dd['daemons'] and 'naso' in dd['functions'], (list(dd)[:5])
print('daemons: %d (law_naso %s); functions blocks: %d' % (len(dd['daemons']), 'law_naso' in dd['daemons'], len(dd['functions'])))
# ---- the dependency span + edges ----
path = f"{ROOT}/World/step9/dependency_dispositions.yaml"
text = open(path, encoding='utf-8').read()
if '  naso:' not in text:
    a = "  bamidbar:    [[Num, 1, 1, 54], [Num, 2, 1, 34], [Num, 3, 1, 51], [Num, 4, 1, 20]]"
    i = text.index(a); j = text.index('\n', i)
    text = text[:j + 1] + "  naso:        [[Num, 4, 21, 49], [Num, 5, 1, 31], [Num, 6, 1, 27], [Num, 7, 1, 89]]   # THE NUMBERS WALK 2b (2026-09-10; NUMBERS_WALK.md \"Sitting 2b\"): Naso's work-count, the camp's purity, the theft and the gifts, the suspected wife, the nazirite, the blessing, the wagons, the dedication, the Voice\n" + text[j + 1:]
    edges = '''  - {from: naso, to: bamidbar, disposition: CALL, link: reference, carries: verdict,
     why: "THE NUMBERS WALK 2b (2026-09-10) | 5:2-3's THREE CAMPS ('their camps' plural — Pesachim 67a) map onto Bamidbar's camp cell (Zevachim 116b); 5:9-10's firstborn redemption after THIRTY DAYS is Bamidbar's levites('age'); 4:47's ages are Bamidbar's charges('fitness'); the work-counts' shares read chapter 3's HOUSES — cold_run_bamidbar.camp / levites / charges / HOUSES CALLED"}
  - {from: naso, to: vayikra5, disposition: CALL, link: reference, carries: verdict,
     why: "THE NUMBERS WALK 2b (2026-09-10) | 5:6-8 repeats Lev 5:20-26's guilt-and-fifth for the proselyte (Sifrei 2:1's rule of repetition; Bava Kamma 110a): the principal, the fifth and the ram — cold_run_vayikra5.deposit_restitution CALLED for the payment algebra"}
  - {from: naso, to: minchah, disposition: CALL, link: reference, carries: verdict,
     why: "THE NUMBERS WALK 2b (2026-09-10) | 5:15 'no oil, no frankincense' — the sotah's meal-offering with the sinner's (Lev 5:11; Mishnah Menachot 5:3) and 5:26's fistful: cold_run_minchah.adjuncts('sinner') and fistful CALLED (the meal-offering engine's own object; 4:16's continual meal-offering stays OWED to Num 28)"}
  - {from: naso, to: tzav, disposition: CALL, link: reference, carries: verdict,
     why: "THE NUMBERS WALK 2b (2026-09-10) | 6:20 'beside the breast of waving and the thigh of lifting' (I11 stated on the verse — Sifrei 37:1): cold_run_tzav.dues_machine('breast_thigh') CALLED"}
  - {from: naso, to: priesthood, disposition: CALL, link: reference, carries: verdict,
     why: "THE NUMBERS WALK 2b (2026-09-10) | the blemished-hands priest does not lift his hands (Mishnah Megillah 4:7): the priesthood engine's blemish list CALLED for the blessing's 'who blesses'"}
  - {from: naso, to: metzora, disposition: CALL, link: reference, carries: verdict,
     why: "THE NUMBERS WALK 2b (2026-09-10) | 6:5's razor against Lev 14:9's 'his head' — the nazirite-leper shaves (Nazir 41a, 58a; Yevamot 5a): cold_run_metzora.shave CALLED"}
  - {from: naso, to: incense_shekel, disposition: CALL, link: reference, carries: verdict,
     why: "THE NUMBERS WALK 2b (2026-09-10) | 7:13 'by the shekel of the sanctuary' (the sela — Onkelos; Sifrei 49:1) and 7:1's ANOINTING of the tabernacle and its vessels (Exod 30:22-33's oil; 'them' — Sanhedrin 16b, Shevuot 15a, Menachot 57b): cold_run_incense_shekel.shekel and oil CALLED"}
  - {from: naso, to: offerings, disposition: CALL, link: reference, carries: verdict,
     why: "THE NUMBERS WALK 2b (2026-09-10) | the nazirite's burnt-, sin-, peace- and guilt-offerings (6:11-17) and the princes' (7:15-17): cold_run_offerings.dispatch CALLED for the kinds' procedures (Mishnah Zevachim 5:5's asham among them)"}
  - {from: naso, to: clocks, disposition: CALL, link: reference, carries: verdict,
     why: "THE NUMBERS WALK 2b (2026-09-10) | 5:2's zav — the purity clocks' status (cold_run_clocks.zav CALLED for the zav's grade: Mishnah Kelim 1:5's two and three sightings)"}
  - {from: naso, to: negaim, disposition: CALL, link: reference, carries: verdict,
     why: "THE NUMBERS WALK 2b (2026-09-10) | 5:2's leper — the confirmed leper's isolated_outside_camp (Lev 13:46 'alone'; Pesachim 67a:7): cold_run_negaim.standing_verdict CALLED for the confirmed / confined fork (Mishnah Kelim 1:5)"}
  - {from: naso, to: heifer, disposition: OWED, link: reference,
     why: "THE NUMBERS WALK 2b (2026-09-10) | 5:2's 'unclean by a corpse' — the heifer's water (Num 19; with 8:7's water at Beha'alotcha): no runner compiles chapter 19; OWED FORWARD to its walk (COMPILE_DEBT)"}
  - {from: sequence, to: naso, disposition: CALL, link: none,
     why: "THE NUMBERS WALK 2b (2026-09-10) | the sequential run's REGISTRATION edge — ('cold_run_naso', 'law_naso') in DAEMON_ORDER (the runner compiles no verse: link none, O4's license)"}
'''
    a = "  - {from: sequence, to: bamidbar, disposition: CALL, link: none,"
    i = text.index(a); j = text.index('\n', text.index('why:', i)) + 1
    text = text[:j] + edges + text[j:]
    open(path, 'w', encoding='utf-8').write(text)
dep = yaml.safe_load(open(path, encoding='utf-8'))
assert 'naso' in str(dep)[:40000]
print('dependency: span + 12 edges (naso)')
# ---- the installation probe's count ----
path = f"{ROOT}/World/step9/installation_probes.py"
text = open(path, encoding='utf-8').read()
a = "len(real) == 48 and all('given_at' in d and 'installed_by' in d for d in real.values())   # THE NUMBERS WALK 1b (2026-09-09): 47 -> 48, law_census;"
if a in text:
    text = text.replace(a, "len(real) == 49 and all('given_at' in d and 'installed_by' in d for d in real.values())   # THE NUMBERS WALK 2b (2026-09-10): 48 -> 49, law_naso; 1b: 47 -> 48, law_census;")
    open(path, 'w', encoding='utf-8').write(text)
print('installation_probes I5: 49')
