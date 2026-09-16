#!/usr/bin/env python3
# THE DEUTERONOMY WALK sitting 1b — THE COMPILE OF THE OPENING SPEECH (2026-09-15; World/step9/DEUTERONOMY_WALK.md "Sitting 1b"): THE TYPES FIRST —
# SIXTEEN tape kinds (the four of Numbers 27:12-23 — the commission, the callee; the twelve of Deuteronomy 1-3 — the frame's one act of its own day
# and the eleven acts told only in the retelling, each written ONCE at its own time by a retrograde marker), TWO case kinds for the exam's scene
# (judges_case, speech_case), THREE new effects (judges_charged — a status on the court, the six clauses; torah_expounded — a status on Israel;
# contending_barred — a block on a people), ONE registry row (the_sons_of_ammon — Genesis 19:38's people, the Moabites' form), the 63rd daemon's
# block (law_opening_speech, given_at Deut 1:16, installed_by BOOT with the class named — a law in Moses' voice with no divine frame, the vows'
# class), the functions block, the dependency span (the first in two books) and the eighteen CALL edges (the pointers and the token-demanded
# edges after the gate's print), the installation probe's count 62 -> 63.
# The `he` is cut from the pointed DB text by FINDING the phrase's tokens (never a typed index); the witnesses the plain consonantal verses.
# Idempotent (add_types_ref.py's form).
import re, sqlite3, yaml, subprocess
ROOT = subprocess.check_output(['git', 'rev-parse', '--show-toplevel'], text=True).strip()   # a scratch script: the repo root from git, never typed
db = sqlite3.connect(f"file:{ROOT}/Data/tanakh.sqlite?mode=ro", uri=True)
def words(book, ch, vs):
    return [r[0] for r in db.execute("SELECT w.he FROM words w JOIN verses v ON w.verse_id=v.id WHERE v.book=? AND v.chapter=? AND v.verse=? ORDER BY w.idx", (book, ch, vs)).fetchall()]
pv = lambda w: ''.join(c for c in w if c != '/' and not (0x0591 <= ord(c) <= 0x05AF))
pl = lambda w: ''.join(c for c in w if c != '/' and not (0x0591 <= ord(c) <= 0x05C7))
def PV(book, ch, vs, lo=None, hi=None):
    ws = words(book, ch, vs); assert ws, (book, ch, vs)
    if lo is not None: ws = ws[lo - 1:hi]
    return ' '.join(pv(w) for w in ws)
def LV(book, ch, vs):
    return ' '.join(pl(w) for w in words(book, ch, vs))
def PHRASE(book, ch, vs, toks):
    """the pointed text of the phrase FOUND in the verse by its plain tokens (the index computed, never typed)"""
    plain = LV(book, ch, vs).split(); n = len(toks)
    hits = [i for i in range(len(plain) - n + 1) if plain[i:i + n] == toks]
    assert len(hits) == 1, (book, ch, vs, toks, hits, plain)
    return PV(book, ch, vs, hits[0] + 1, hits[0] + n)
q = lambda s: '"' + s.replace('\\', '\\\\').replace('"', '\\"') + '"'
def HE(book, ch, lo, hi, en, cap=6):
    vv = list(range(lo, min(hi, lo + cap - 1) + 1))
    s = ' · '.join(PV(book, ch, v) + ' (%s — %s %d:%d)' % (en if v == lo else 'the verse continues', book, ch, v) for v in vv)
    return s + (' · … (through %s %d:%d)' % (book, ch, hi) if hi > vv[-1] else '')
def WIT(book, ch, lo, hi):
    return ['%s %d:%d | %s' % (book, ch, v, LV(book, ch, v)) for v in range(lo, hi + 1)]
CORPUS_D = "deu_01_frame_officers, deu_01_spies_refuse, deu_02_bypass_nations, deu_02_sihon, deu_03_og_gilead, deu_03_moses_barred (STEP_Dt_1_1 through STEP_Dt_3_29; claims DV01A-01 through DV03B-02)"
CORPUS_N = "num_27_zelophehad_joshua (STEP_Nm_27_12 through STEP_Nm_27_23; claims NM27-01 through NM27-11 — THE TENT's fourth sitting, the callee compiled here)"
SUB = "submitted by cold_run_opening_speech.py [subjects: %s] (the narrative scene, THE DEUTERONOMY WALK 1b); re-submitted on the sequential tape by cold_run_sequence.py; consumed by law_opening_speech (cold_run_opening_speech.py) -> %s"
CASE = "submitted by cold_run_opening_speech.py [subjects: the exam's persons] (the wrap's scene); consumed by law_opening_speech (cold_run_opening_speech.py) -> %s"
INK_D = "Deut 1:1-3:29; Onkelos Deut 1:1-3:29 (the eleven words of 1:1 written as the rebuke's sins; 'his sons' for 'his son' at 2:33; the Temple at 3:25; 'the sons of Esau who dwell in Seir did for me' at 2:29 the retelling's own arm); Sifrei Devarim piskaot 1-30 by position (147 rows; no piska on 1:29-3:22); the reading ledger deu_01_03_devarim_2026-09-15.md (259 sources, 21 claims); the exam docket deu_01_03_devarim_exam_2026-09-15.md (864 rows — Sanhedrin 23a-31b whole, 2a-2b, 6b-7a, 16b-17a, 32a-32b, 90b-91a; Rosh Hashanah 2b-3a; Sotah 34a-35a; Berakhot 30a; Makkot 9b-10a; the thirty Mishnah rows; 67 link rows in 26 works)"
INK_N = "Num 27:12-23; Onkelos Num 27:12-23; Sifrei Bamidbar 135-141 (credited at THE TENT's fourth sitting — the daughters of Zelophehad and Joshua's commission); Deut 3:27-28 and 34:1-4 the retellings and the run; the exam docket deu_01_03_devarim_exam_2026-09-15.md (Sanhedrin 17a:10 Eldad and Medad's prophecy; Bava Batra 75a the sun and the moon by REFERENCE)"
D, N = 'Deut', 'Num'
KINDS = [
 ("moses_told_to_ascend_abarim", "speech",
  "Moses told to ascend Abarim — 'and the LORD said to Moses: go up to this mountain of Abarim and SEE THE LAND which I have given to the children of Israel; and when you have seen it, you also shall be gathered to your people, as Aaron your brother was gathered; because you rebelled against My word in the wilderness of Zin, in the strife of the congregation, to sanctify Me at the waters before their eyes — these are the waters of Meribah of Kadesh in the wilderness of Zin' (Num 27:12-14) — ONE DEBIT on Moses (commanded, the value see_the_land_from_abarim) OPEN BY DESIGN to its run at Deuteronomy 34:1-4 (this book's own end: 'and Moses went up from the plains of Moab to Mount Nebo, the top of Pisgah'); 27:14's Meribah an INTERNAL pointer to 20:12's sentence — the barred_from_the_land entry on Moses OPEN, read; Deuteronomy 3:27 the retelling with Pisgah for Abarim (34:1: one mountain, three names — DATA the_commission), READ BACK, no second write",
  HE(N, 27, 12, 14, "and the LORD said to Moses: go up to this mountain of Abarim and see the land which I have given to the children of Israel"), WIT(N, 27, 12, 14), INK_N, CORPUS_N,
  SUB % ("moses", "commanded on moses (the DEBIT see_the_land_from_abarim, OPEN by design — Deuteronomy 34:1-4 this book's end)"), ["mountain", "land", "sentence"]),
 ("a_shepherd_asked", "speech",
  "a shepherd asked — 'and Moses spoke to the LORD, saying: let the LORD, the God of the spirits of all flesh, appoint a man over the congregation, who may go out before them and who may come in before them, and who may lead them out and who may bring them in, that the congregation of the LORD be not as sheep which have no shepherd' (Num 27:15-17) — plea_made on Moses (the status Hobab's row carries, the plea the value): the successor asked before he is named; 'the God of the spirits of all flesh' 16:22's phrase at its second seat; 'go out and come in' the leader's idiom",
  HE(N, 27, 15, 17, "and Moses spoke to the LORD, saying"), WIT(N, 27, 15, 17), INK_N, CORPUS_N,
  SUB % ("moses", "plea_made on moses (the plea the value: a man over the congregation, that they be not as sheep without a shepherd)"), ["plea"]),
 ("joshua_commission_commanded", "speech",
  "Joshua's commission commanded — 'and the LORD said to Moses: take you Joshua the son of Nun, a man in whom is spirit, and lay your hand upon him; and set him before Eleazar the priest and before all the congregation, and command him in their sight; and you shall put of your honor upon him, that all the congregation of the children of Israel may hear; and he shall stand before Eleazar the priest, who shall inquire for him by the judgment of the Urim before the LORD; at his word shall they go out and at his word shall they come in, he and all the children of Israel with him, even all the congregation' (Num 27:18-21) — ONE DEBIT on Moses (commanded, the value commission_joshua_before_eleazar), CLOSED by its run at 27:22-23 in the next line; ONE hand commanded, two laid (the Sifrei 141, credited at THE TENT); 'some of your honor' (Bava Batra 75a:8 — the sun and the moon: DATA); the Urim's judgment final (C2.DATA['urim_judgment'] by CALL)",
  HE(N, 27, 18, 21, "and the LORD said to Moses: take you Joshua the son of Nun, a man in whom is spirit, and lay your hand upon him"), WIT(N, 27, 18, 21), INK_N, CORPUS_N,
  SUB % ("moses", "commanded on moses (the DEBIT commission_joshua_before_eleazar — closed by the next line's run)"), ["successor", "priest", "urim"]),
 ("joshua_commissioned", "act",
  "Joshua commissioned — 'and Moses did as the LORD commanded him; and he took Joshua and set him before Eleazar the priest and before all the congregation; and he laid his hands upon him and commanded him, as the LORD spoke by the hand of Moses' (Num 27:22-23) — invested_office on Joshua (the value: the hand laid, some of Moses' honor, before Eleazar the priest by the judgment of the Urim) AND THE CLOSE of the commission's debit on Moses by its run (closed_by 'Num 27:22-23' — the receipt 'as the LORD commanded' the spec/run pair's form): the register seat Num 27:22 CLOSE; Deuteronomy 3:28's 'command Joshua, strengthen him' the commissioning READ BACK (Kiddushin 29a:14 — 'command' a galvanization, immediate and for generations)",
  HE(N, 27, 22, 23, "and Moses did as the LORD commanded him; and he took Joshua and set him before Eleazar the priest and before all the congregation"), WIT(N, 27, 22, 23), INK_N, CORPUS_N,
  SUB % ("yehoshua, moses", "invested_office on yehoshua; the commission debit on moses CLOSED by its run (the daemon's own close, closed_by Num 27:22-23)"), ["hand", "honor", "receipt"]),
 ("speech_opened", "speech",
  "the speech opened — 'these are the words which Moses spoke to all Israel beyond the Jordan, in the wilderness, in the Arabah over against Suph, between Paran and Tophel and Laban and Hazeroth and Di-zahab; eleven days from Horeb by the way of Mount Seir to Kadesh-barnea; and it came to pass in the fortieth year, in the eleventh month, on the first of the month, that Moses spoke to the children of Israel according to all that the LORD had commanded him to them; after he had smitten Sihon king of the Amorites … and Og king of Bashan …; beyond the Jordan, in the land of Moab, Moses undertook to expound this Torah, saying' (Deut 1:1-5) — THE BOOK'S ONE ACT OF ITS OWN DAY: a STATUS on Israel, torah_expounded, dated (40, 11, 1) by the forward marker at 1:3 (the number reader [40, 11, 1]; the era the exodus's by the taught verbal analogy with Numbers 33:38 — Rosh Hashanah 2b:11) placed at the tape position Deut 1:1; the eleven words of 1:1 the Sifrei's rebuke by places, Onkelos writing the sins into the verse; 1:3's 'according to all' the receipt of the whole book's rules (the Sifrei 2:8 — the hermeneutic rules themselves): the register seat Deut 1:3 ACT; everything after it in chapters 1-3 read back or supplied at its own time",
  HE(D, 1, 1, 5, "these are the words which Moses spoke to all Israel beyond the Jordan, in the wilderness, in the Arabah"), WIT(D, 1, 1, 5), INK_D, CORPUS_D,
  SUB % ("israel", "torah_expounded on israel_people (a STATUS, dated (40, 11, 1) — the book's one act of its own day)"), ["places", "date", "after"]),
 ("horeb_departure_commanded", "speech",
  "the departure from Horeb commanded — 'the LORD our God spoke to us in Horeb, saying: you have dwelt long enough in this mountain; turn and take your journey and go to the hill country of the Amorites and to all the places near it, in the Arabah, in the hill country, in the lowland, in the Negev and by the seashore, the land of the Canaanites and Lebanon, as far as the great river, the river Euphrates; behold, I have set the land before you: go in and possess the land which the LORD swore to your fathers, to Abraham, to Isaac and to Jacob, to give to them and to their seed after them' (Deut 1:6-8) — A SUPPLIED ACT (told only in the retelling; Exodus 33:1 gives the command's kin, Numbers 10:11-12 the departure's day): ONE DEBIT on Israel (commanded, the value journey_to_the_mountain_of_the_amorite) dated (2, 2, 20) by the RETROGRADE marker at 1:6 (M['march'], Numbers 10:11's own day) and CLOSED IN THE SAME BLOCK BY THE PRIOR RUN — Numbers 12:16's arrival in Paran (closed_by 'Num 12:16'): the ledger's record that the command came to the reader after its execution; 'go in and possess' a REFERENCE to land_granted (Genesis 15:18) and to the open dispossess debit (33:50-56), cited, not rewritten; the seven regions (1:7) DATA (Bava Kamma 81b:6; Shevuot 47b:6)",
  HE(D, 1, 6, 8, "the LORD our God spoke to us in Horeb, saying: you have dwelt long enough in this mountain"), WIT(D, 1, 6, 8), INK_D, CORPUS_D,
  SUB % ("israel", "commanded on israel_people (the DEBIT journey_to_the_mountain_of_the_amorite, dated (2, 2, 20), CLOSED at once by the prior run Num 12:16)"), ["regions", "closed_by"]),
 ("judges_charged", "speech",
  "the judges charged — 'and I charged your judges at that time, saying: hear the causes between your brothers, and judge righteously between a man and his brother and the stranger with him; you shall not respect persons in judgment; you shall hear the small and the great alike; you shall not be afraid of the face of any man, for the judgment is God's; and the cause that is too hard for you, you shall bring to me and I will hear it; and I commanded you at that time all the things that you should do' (Deut 1:16-18) — THE LAW OF THIS SPAN, in Moses' voice with no divine frame: ONE STATUS on the court, judges_charged (a NEW effect), its value the six clauses — hear between your brothers; judge righteously between a man and his brother and his stranger; no faces in judgment; the small as the great; fear no man, for the judgment is God's; the hard matter to me — dated (1, 2, 16) by the RETROGRADE marker at 1:9 (the day of the court's founding, courts_established's own day read off Israel's ledger); the appointment itself (1:9-15) a REFERENCE to judges_appointed (Exodus 18:25, TURNED — the three qualities for Jethro's four; the officers added; THE OFFICERS' TABLE 78,600 / 79,064 DATA); the charge's clauses the exam's rows (Sanhedrin 7b:14-8a:6 clause by clause; 6b the compromise and the refusal before hearing; Mishnah Sanhedrin 1, 3, 4; Avot 1:1)",
  HE(D, 1, 16, 18, "and I charged your judges at that time, saying: hear the causes between your brothers, and judge righteously"), WIT(D, 1, 16, 18), INK_D, CORPUS_D,
  SUB % ("the-court", "judges_charged on the-court (a STATUS, the six clauses the value, dated (1, 2, 16))"), ["clauses"]),
 ("turn_northward_commanded", "speech",
  "the turn northward commanded — 'and the LORD spoke to me, saying: you have compassed this mountain long enough; turn you northward; and command the people, saying: you are to pass through the border of your brothers the children of Esau, who dwell in Seir, and they will be afraid of you; take good heed to yourselves therefore; do not contend with them, for I will not give you of their land, no, not so much as for the sole of the foot to tread on, because I have given Mount Seir to Esau for a possession; you shall buy food of them for money … and water … for the LORD your God has blessed you … these forty years the LORD your God has been with you; you have lacked nothing' (Deut 2:2-7) — A SUPPLIED ACT dated (40, 6, 1) by the RETROGRADE marker at 2:2 (M['hor_departure'], 21:4's text-constrained day): ONE DEBIT on Israel (commanded, the value turn_northward) CLOSED IN THE SAME BLOCK BY THE PRIOR RUN — Numbers 21:10-13's march past Moab (closed_by 'Num 21:10-13'); AND contending_barred on Edom (a NEW effect, a BLOCK — 2:5) AND land_granted on Edom valued mount_seir (Kiddushin 18a:2 — a gentile inherits by Torah law from this verse); the purchase (2:6) a permission, DATA (Avodah Zarah 37b:15); the forty years lacking nothing (2:7) the manna by CALL",
  HE(D, 2, 2, 7, "and the LORD spoke to me, saying"), WIT(D, 2, 2, 7), INK_D, CORPUS_D,
  SUB % ("israel, edom", "commanded on israel_people (the DEBIT turn_northward, CLOSED at once by the prior run Num 21:10-13); contending_barred and land_granted (mount_seir) on edom"), ["bar", "grant", "purchase", "closed_by"]),
 ("moab_spared_commanded", "speech",
  "Moab spared commanded — 'and the LORD said to me: do not harass Moab nor contend with them in battle, for I will not give you of his land for a possession, because I have given Ar to the children of Lot for a possession' (Deut 2:9) — A SUPPLIED ACT dated (40, 6, 1): contending_barred on the Moabites (the people's row Balak's runner wrote) AND land_granted on the Moabites valued ar; the bar's teachers — Bava Kamma 38a:16 (Moses' own a fortiori from Midian needed the bar), Horayot 10b:19 / Nazir 23b:11 (battle forbidden, harassing not — the reward of Lot's elder daughter's euphemism), Chullin 60b:13 (Moab's land purified through Sihon — CK.DATA['sihon_purified'] by CALL)",
  HE(D, 2, 9, 9, "and the LORD said to me: do not harass Moab nor contend with them in battle"), WIT(D, 2, 9, 9), INK_D, CORPUS_D,
  SUB % ("the-moabites", "contending_barred (a BLOCK) and land_granted (ar) on the-moabites"), ["bar", "grant"]),
 ("zered_crossing_commanded", "speech",
  "the crossing of the Zered commanded — 'now rise up and get you over the brook Zered; and we went over the brook Zered' (Deut 2:13) — A SUPPLIED ACT dated (40, 6, 1): ONE DEBIT on Israel (commanded, the value cross_the_brook_zered) CLOSED IN THE SAME BLOCK BY THE PRIOR RUN — Numbers 21:12's camp at the brook Zered (closed_by 'Num 21:12'); 2:14's thirty-eight years from Kadesh-barnea to the Zered against the tape's years (the spies' return (2, 5, 9) to the counter's (40, 6, 1) — computed by the era's year); 2:16-17 the men of war consumed, the LORD spoke — the fifteenth of Av (Taanit 30b:12; Bava Batra 121b:1 — only after the last of that generation; deaths_ceased (40, 5, 15) by CALL to SL.DATA)",
  HE(D, 2, 13, 13, "now rise up and get you over the brook Zered; and we went over the brook Zered"), WIT(D, 2, 13, 13), INK_D, CORPUS_D,
  SUB % ("israel", "commanded on israel_people (the DEBIT cross_the_brook_zered, CLOSED at once by the prior run Num 21:12)"), ["closed_by"]),
 ("ammon_spared_commanded", "speech",
  "Ammon spared commanded — 'and the LORD spoke to me, saying: you are this day to pass over Ar, the border of Moab; and when you come near over against the children of Ammon, do not harass them nor contend with them, for I will not give you of the land of the children of Ammon for a possession, because I have given it to the children of Lot for a possession' (Deut 2:17-19) — A SUPPLIED ACT dated (40, 6, 1): contending_barred on the sons of Ammon (a NEW registry row — Genesis 19:38's people, Lot's younger daughter's; the Moabites' form) AND land_granted on the sons of Ammon; Ammon not even harassed (Bava Kamma 38b:6 / Horayot 11a:1 / Nazir 23b:12 — the reward of the younger daughter's euphemism); 21:24's 'the border of the sons of Ammon was strong' CK.DATA['ammon_border'] by CALL; the Zamzummim, the Avvim and the Caphtorim (2:20-23 — Chullin 60b:11 the verses fit to be burned; Genesis 10:14 by CALL)",
  HE(D, 2, 17, 19, "and the LORD spoke to me, saying"), WIT(D, 2, 17, 19), INK_D, CORPUS_D,
  SUB % ("the-sons-of-ammon", "contending_barred (a BLOCK) and land_granted on the-sons-of-ammon (the one new written-on party)"), ["bar", "grant"]),
 ("sihon_war_commanded", "speech",
  "the war on Sihon commanded — 'rise up, take your journey, and pass over the valley of Arnon; behold, I have given into your hand Sihon the Amorite, king of Heshbon, and his land; begin to possess it, and contend with him in battle; this day will I begin to put the dread of you and the fear of you upon the peoples that are under the whole heaven, who, when they hear the report of you, shall tremble and be in anguish because of you' (Deut 2:24-25; 2:31 'begin to possess, that you may inherit his land') — A SUPPLIED ACT dated (40, 6, 1): ONE DEBIT on Israel (commanded, the value begin_to_possess_sihons_land) CLOSED IN THE SAME BLOCK BY THE PRIOR RUN — Numbers 21:24-25's smiting and possession (closed_by 'Num 21:24-25'); 'I will begin to put the dread of you' DATA (Avodah Zarah 25a:7-9; Taanit 20a:6-8 — the sun stood still for Moses: 'I will begin' / 'I will begin' with Joshua 3:7; 'put' / 'put' with Joshua 10:12; R. Yochanan from the verse itself)",
  HE(D, 2, 24, 25, "rise up, take your journey, and pass over the valley of Arnon; behold, I have given into your hand Sihon the Amorite, king of Heshbon, and his land"), WIT(D, 2, 24, 25) + WIT(D, 2, 31, 31), INK_D, CORPUS_D,
  SUB % ("israel", "commanded on israel_people (the DEBIT begin_to_possess_sihons_land, CLOSED at once by the prior run Num 21:24-25)"), ["dread", "closed_by"]),
 ("sihons_cities_devoted", "act",
  "Sihon's cities devoted — 'and we took all his cities at that time, and utterly destroyed every city, the men and the women and the little ones; we left none remaining; only the cattle we took for a prey to ourselves, with the spoil of the cities which we had taken' (Deut 2:34-35) — A SUPPLIED ACT dated (40, 6, 1): destroyed (the body effect the king of Arad's line wrote at 21:3) on the Amorite, valued every city — the men, the women and the little ones; the cattle and the spoil taken: THE BAN TOLD ONLY HERE (Numbers 21:24-25 say smote and possessed); Genesis 15:16's amorite_not_full STATUS on the Amorite READ beside it (the fourth generation's return, OPEN since 15:13-16 — a printed line, no verdict); Deuteronomy 20:16-17's law FORWARD",
  HE(D, 2, 34, 35, "and we took all his cities at that time, and utterly destroyed every city, the men and the women and the little ones; we left none remaining"), WIT(D, 2, 34, 35), INK_D, CORPUS_D,
  SUB % ("the-amorite", "destroyed on the-amorite (the ban on every city of Sihon's — told only here)"), ["cities", "spoil"]),
 ("ogs_cities_devoted", "act",
  "Og's cities devoted — 'and we utterly destroyed them, as we did to Sihon king of Heshbon, utterly destroying every city, the men and the women and the little ones; but all the cattle and the spoil of the cities we took for a prey to ourselves' (Deut 3:6-7) — A SUPPLIED ACT dated (40, 6, 1): destroyed on the Amorite a second time, valued every city of the sixty (3:4-5 [60] — Argob; Arakhin 32b:6 / Megillah 10a:10 / Shevuot 16a:14 the walled cities from Joshua's days); Numbers 21:35 says smote and possessed — THE BAN TOLD ONLY HERE; 'as we did to Sihon' the retelling's own cross-reference",
  HE(D, 3, 6, 7, "and we utterly destroyed them, as we did to Sihon king of Heshbon, utterly destroying every city, the men and the women and the little ones"), WIT(D, 3, 6, 7), INK_D, CORPUS_D,
  SUB % ("the-amorite", "destroyed on the-amorite (the ban on every city of Og's sixty — told only here)"), ["cities", "spoil"]),
 ("joshua_encouraged", "speech",
  "Joshua encouraged — 'and I commanded Joshua at that time, saying: your eyes have seen all that the LORD your God has done to these two kings; so shall the LORD do to all the kingdoms to which you go over; you shall not fear them, for the LORD your God, He it is who fights for you' (Deut 3:21-22) — A SUPPLIED ACT dated (40, 6, 1): fear_not_promised on Joshua (the HEAVEN effect the tape wrote on Moses at Numbers 21:34 — 'fear him not') valued 'your eyes have seen; so shall the LORD do to all the kingdoms; He fights for you' — Joshua 1:6 and Ai's run outside the Torah (the readback's; the Sifrei 29:8-9 the condition Joshua broke, DATA); Joshua written plene at 3:21 alone in the Torah",
  HE(D, 3, 21, 22, "and I commanded Joshua at that time, saying: your eyes have seen all that the LORD your God has done to these two kings"), WIT(D, 3, 21, 22), INK_D, CORPUS_D,
  SUB % ("yehoshua", "fear_not_promised on yehoshua (HEAVEN's promise — Numbers 21:34's effect at its second party)"), ["seen", "promise"]),
 ("moses_besought", "speech",
  "Moses besought — 'and I besought the LORD at that time, saying: O Lord GOD, You have begun to show Your servant Your greatness and Your strong hand … let me go over, I pray, and see the good land that is beyond the Jordan, that goodly hill country and Lebanon; but the LORD was wroth with me for your sakes and did not hear me; and the LORD said to me: let it suffice you; speak no more to Me of this matter' (Deut 3:23-26) — A SUPPLIED ACT dated (40, 6, 1): plea_made on Moses valued the plea AND ITS ANSWER (as Hobab's row carries the refusal): 'let me go over and see the good land — REFUSED: enough for you, speak no more to Me of this matter; the LORD was wroth for your sakes' — the barred_from_the_land HEAVEN entry OPEN read, no new heaven write; praise before the request (Berakhot 32a:32; Avodah Zarah 7b:18); 'I pleaded' the pleading mode (Berakhot 30b:9); 'let it suffice you' measure for measure for Korach's 'enough for you' (Sotah 13b:13); the ten names of prayer (the Sifrei 26:7) and the directions of prayer (the Sifrei 29:5; Mishnah Berakhot 4:5-6) DATA; 3:27's Pisgah the see-the-land debit READ BACK; 3:28's 'command Joshua' the commission READ BACK",
  HE(D, 3, 23, 26, "and I besought the LORD at that time, saying"), WIT(D, 3, 23, 26), INK_D, CORPUS_D,
  SUB % ("moses", "plea_made on moses (the plea and its refusal the value; the barred_from_the_land entry OPEN, read)"), ["plea", "answer"]),
 ("judges_case", "case", "the exam's rows on the judges' charge (Deut 1:9-18 — Mishnah Sanhedrin 1:1-6 the courts' sizes; 3:1-8 the litigants' choice, the disqualified by conduct and by kin, the lover and the hater, the examination, the verdict, the new proof; 4:1 money against capital; Avot 1:1 be deliberate; Sanhedrin 6b:1-8a:6 the compromise, the refusal before hearing, the charge clause by clause; 2a-2b the twenty-three; 16b-17a the seventy-one from Moses' seventy and the officers' second seat; 32a-32b the ten differences; 23a-31b the court's chapter whole; Yevamot 47a:7 the convert before a court; Rosh Hashanah 28b:10 the blessing not added; Eruvin 100b:18 / Nedarim 20b:10 the generation's sons; the Sifrei 13-18 by position — the gentile litigant, the appointer, the al tikrei, Zelophehad's daughters the hard matter)",
  PHRASE(D, 1, 16, ['שמע', 'בין', 'אחיכם', 'ושפטתם', 'צדק']) + " (hear between your brothers and judge righteously — Deut 1:16)", WIT(D, 1, 9, 18), INK_D, CORPUS_D, CASE % "accepted / exempt / judgment_perverted (the exam's persons — the judge who perverts: HO.conduct('five_effects') by CALL)", ["person", "ask"]),
 ("speech_case", "case", "the exam's rows on the speech's other cells (Deut 1:1-8, 1:19-3:29; Num 27:12-23 — the frame and the date: Rosh Hashanah 2b-3a the chain, Mishnah Rosh Hashanah 1:1, Berakhot 32a:7 / Sanhedrin 102a:14 Di-zahab, Sotah 35b:6, Zevachim 115b:17, Mishnah Sotah 7:8 the king's reading; the spies read back: Sotah 34a-35a, 34b:3-4, Shevuot 47b:5; the bypass: Bava Kamma 38a-38b, Horayot 10b-11a, Nazir 23b, Kiddushin 18a:2, Chullin 60b:11-14, Avodah Zarah 25a / Taanit 20a the sun, Taanit 30b:12 / Bava Batra 121b:1 the fifteenth of Av; Sihon and Og: Arakhin 32b:6, Megillah 10a:10, Shevuot 16a:14 the sixty cities, Kelim 17:9-10 / Eruvin 4:8 the cubit, Sanhedrin 90b-91a the land's title; the east and the charges: Kiddushin 29a:14; the plea: Berakhot 32a:32, Avodah Zarah 7b:18, Berakhot 30b:9, Sotah 13b:13, Gittin 56b:1, Mishnah Berakhot 4:5-6 / Berakhot 30a; the commission: Sanhedrin 17a:10; Makkot 9b-10a the eastern refuge cities — chapter 4's, OUTSIDE)",
  PHRASE(D, 1, 5, ['הואיל', 'משה', 'באר', 'את', 'התורה', 'הזאת']) + " (Moses undertook to expound this Torah — Deut 1:5)", WIT(D, 1, 1, 5), INK_D, CORPUS_D, CASE % "accepted / exempt (the exam's persons)", ["person", "ask"]),
]
assert len(KINDS) == 18, len(KINDS)
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
print('kinds: %d added of %d, registry %d' % (len(out), len(KINDS), len(after['events'])))
# ---- THREE new effects, the ink's own words, the `he` FOUND in the verse ----
path = f"{ROOT}/World/step9/effect_vocabulary.yaml"
text = open(path, encoding='utf-8').read()
fx = yaml.safe_load(text)['effects']
for e in ('commanded', 'plea_made', 'invested_office', 'fear_not_promised', 'destroyed', 'land_granted', 'accepted', 'exempt', 'judgment_perverted', 'barred_from_the_land', 'courts_established', 'hard_cases_to_moses'):
    assert e in fx, e
print('  1:16 plain:', LV(D, 1, 16)); print('  1:5 plain:', LV(D, 1, 5)); print('  2:5 plain:', LV(D, 2, 5))
HE_CHARGE = PHRASE(D, 1, 16, ['ואצוה', 'את', 'שפטיכם', 'בעת', 'ההוא', 'לאמר', 'שמע', 'בין', 'אחיכם', 'ושפטתם', 'צדק'])
HE_EXPOUND = PHRASE(D, 1, 5, ['הואיל', 'משה', 'באר', 'את', 'התורה', 'הזאת'])
HE_CONTEND = PHRASE(D, 2, 5, ['אל', 'תתגרו', 'בם'])
NEW = [
 ('judges_charged', 'status',
  "the judges charged — the STATUS Moses' charge writes on the court: 'and I charged your judges at that time, saying: hear between your brothers, and judge righteously between a man and his brother and the stranger with him; you shall not respect persons in judgment; you shall hear the small and the great alike; you shall not be afraid of the face of any man, for the judgment is God's; and the cause that is too hard for you, you shall bring to me' (Deut 1:16-17) — the value the six clauses (hear between your brothers; judge righteously between a man and his brother and his stranger; no faces in judgment; the small as the great; fear no man, for the judgment is God's; the hard matter to me), dated (1, 2, 16) — the day of the court's founding (courts_established's own day, Exodus 18:25-26's judges_appointed the in-force cell the charge is spoken over); THE LAW OF THE OPENING SPEECH, in Moses' voice with no divine frame (the vows' class); the shelf: Sanhedrin 7b:14-8a:6 the clauses read one by one — 'charged' with alacrity, the rod and the strap; 'hear' — not one litigant without the other (R. Chanina); 'righteously' — the true judgment truly (R. Yonatan, 7a:17); 'the stranger' — the convert before a court (Yevamot 47a:7); 'no faces' — do not befriend / do not estrange (R. Yehuda / R. Elazar, 7b:18); 'the small as the great' — the peruta as the hundred maneh (Reish Lakish, 8a:2); 'not afraid' — a term for gathering in, the student not silent (7a:16; 6b:13); 'the judgment is God's' — pierce the mountain (6b:3), the judge who takes from one and gives to the other (7a:18); 'the hard matter' — Zelophehad's daughters (the Sifrei 17:7); the compromise's three settings (6b:1-15); the Sifrei 16-17 the gentile litigant, the appointer",
  HE_CHARGE + " (and I charged your judges at that time, saying: hear between your brothers and judge righteously — Deut 1:16)",
  "Deut 1:16 ('and I charged your judges at that time, saying: hear between your brothers, and judge righteously between a man and his brother and the stranger with him'), 1:17 ('you shall not respect persons in judgment; you shall hear the small and the great alike; you shall not be afraid of the face of any man, for the judgment is God's; and the cause that is too hard for you, you shall bring to me and I will hear it'), 1:18 ('and I commanded you at that time all the things that you should do'); Exodus 18:21-26 (the appointment and the hard cases — the exodus story runner by CALL); Leviticus 19:15 ('in righteousness you shall judge your neighbor' — the holiness runner by CALL); Deuteronomy 16:18-20 FORWARD; Onkelos 1:16-17; the Sifrei 16:1-17:7; Babylonian Talmud Sanhedrin 6b:1-8a:6, 7a:16-19, 32a-32b, Yevamot 47a:7; Mishnah Sanhedrin 1:1-6, 3:1-8, 4:1; Avot 1:1",
  "deu_01_frame_officers (STEP_Dt_1_16, STEP_Dt_1_17, STEP_Dt_1_18; the claims DV01A-03, DV01A-04)",
  "cold_run_opening_speech.py (F2 the_officers_and_the_judges — the_charge cell and its asks hear / judge_righteously / no_faces / small_and_great / no_fear / the_judgment_is_gods / the_hard_matter; the exam kind judges_case)"),
 ('torah_expounded', 'status',
  "the Torah expounded — the STATUS the frame writes on Israel at the speech's opening: 'beyond the Jordan, in the land of Moab, Moses undertook to expound this Torah, saying' (Deut 1:5) — dated (40, 11, 1) by 1:3's own date (the fortieth year, the eleventh month, the first of the month — the number reader; the era the exodus's by the verbal analogy with Numbers 33:38, Rosh Hashanah 2b:11), THE BOOK'S ONE ACT OF ITS OWN DAY: the value the speech's frame — the eleven words of 1:1 (the Sifrei 1's rebuke by places, Onkelos writing the sins into the verse), 1:3's receipt of the whole book's rules ('according to all that the LORD commanded him' — the Sifrei 2:8: the hermeneutic rules), 1:4's 'after he had smitten Sihon' (the order of the fortieth year — Rosh Hashanah 2b:13, 3a:12); the shelf: Sotah 35b:6 ('expound' with Deuteronomy 27:8's 'clearly' — the seventy languages); Zevachim 115b:17 (R. Akiva: the generalities and the details at Sinai, repeated in the Tent, a third time in the plains of Moab); the king's reading from 'these are the words' (Mishnah Sotah 7:8; Sotah 41a:18); the Rambam's introduction 2:19 (the first of Shevat)",
  HE_EXPOUND + " (Moses undertook to expound this Torah — Deut 1:5)",
  "Deut 1:5 ('beyond the Jordan, in the land of Moab, Moses undertook to expound this Torah, saying' — the expound-root's Torah seats 1:5 and 27:8, Habakkuk 2:2 the third), 1:1 ('these are the words which Moses spoke to all Israel'), 1:3 ('in the fortieth year, in the eleventh month, on the first of the month … according to all that the LORD had commanded him to them'), 1:4 ('after he had smitten Sihon'); Onkelos 1:1-5; the Sifrei 1:1-4:2; Babylonian Talmud Sotah 35b:6, 41a:18, Zevachim 115b:17, Berakhot 32a:7, Sanhedrin 102a:14, Rosh Hashanah 2b:7-3a:15; Mishnah Sotah 7:8, Rosh Hashanah 1:1",
  "deu_01_frame_officers (STEP_Dt_1_1 through STEP_Dt_1_5; the claims DV01A-01, DV01A-02)",
  "cold_run_opening_speech.py (F1 the_frame — the_words, the_date, the_receipt_of_the_rules, began_to_expound cells; the exam kind speech_case)"),
 ('contending_barred', 'block',
  "contending barred — the BLOCK the bypass writes on a people Israel may not war with: 'do not contend with them, for I will not give you of their land, no, not so much as for the sole of the foot to tread on, because I have given Mount Seir to Esau for a possession' (Deut 2:5 — Edom), 'do not harass Moab nor contend with them in battle' (2:9 — the Moabites), 'do not harass them nor contend with them' (2:19 — the sons of Ammon): the contend-root's three seats in the chapter (2:5, 2:9, 2:19; 2:24 its positive 'contend with him in battle' at Sihon — the fourth, no block), each beside a land_granted on the same people (Mount Seir; Ar; the land of the sons of Ammon — 'I have given … for a possession'); the bars' difference DATA — Moab: battle forbidden, harassing not (Horayot 10b:19; Nazir 23b:11 — the reward of the elder daughter's euphemism); Ammon: not even harassed (Bava Kamma 38b:6; Horayot 11a:1; Nazir 23b:12 — the younger's); Edom: 'your brothers' (2:4, 2:8; Deuteronomy 23:8 forward); Bava Kamma 38a:16 — Moses' own a fortiori from Midian made the bar needed; Kiddushin 18a:2 — a gentile inherits by Torah law from 2:5; the retelling's own arm at 2:29 ('as the sons of Esau did for me') against Numbers 20:18-21's refusal — an OPEN row, no teacher joins them",
  HE_CONTEND + " (do not contend with them — Deut 2:5)",
  "Deut 2:5 ('do not contend with them … because I have given Mount Seir to Esau for a possession'), 2:9 ('do not harass Moab nor contend with them in battle … because I have given Ar to the children of Lot for a possession'), 2:19 ('do not harass them nor contend with them … because I have given it to the children of Lot for a possession'), 2:24 ('contend with him in battle' — Sihon, the positive), 2:4, 2:8 ('your brothers the children of Esau'), 2:29 (the retelling's arm); Genesis 19:37-38 (Moab and Ammon born — the mamre runner by CALL), 36:8 (Esau in Seir — the joseph runner by CALL); Numbers 20:14-21 (Edom's refusal — the chukat runner by CALL), 21:13, 21:24 (the Arnon and Ammon's border); Onkelos 2:5, 2:9, 2:19; the Sifrei 20-21 by position; Babylonian Talmud Bava Kamma 38a:16-38b:6, Horayot 10b:19-11a:1, Nazir 23b:11-12, Kiddushin 18a:2, Chullin 60b:13, Avodah Zarah 37b:15",
  "deu_02_bypass_nations (STEP_Dt_2_5, STEP_Dt_2_9, STEP_Dt_2_19; the claims DV02A-01, DV02A-02, DV02A-03)",
  "cold_run_opening_speech.py (F4 the_bypass — esau, moab, ammon cells; the tape kinds turn_northward_commanded, moab_spared_commanded, ammon_spared_commanded)"),
]
added = 0
for name, op, en, he, ink, corpus, exam in NEW:
    if name in fx: continue
    text = text.rstrip('\n') + '\n' + f"  {name}:\n    en: {q(en)}\n    he: {q(he)}\n    ledger_op: {op}   # THE DEUTERONOMY WALK 1b (2026-09-15): the opening speech's compile — {name}\n    ink: {q(ink)}\n    corpus: {q(corpus)}\n    exam: {q(exam)}\n"
    added += 1
open(path, 'w', encoding='utf-8').write(text)
fx = yaml.safe_load(open(path, encoding='utf-8'))['effects']
assert all(n in fx for n, *_ in NEW) and fx['judges_charged']['ledger_op'] == 'status' and fx['torah_expounded']['ledger_op'] == 'status' and fx['contending_barred']['ledger_op'] == 'block'
print('effects: %d added (registry %d); the he found in the verses: %s | %s | %s' % (added, len(fx), HE_CHARGE, HE_EXPOUND, HE_CONTEND))
# ---- ONE registry row: the sons of Ammon (the people written on for the first time — the Moabites' form) ----
path = f"{ROOT}/logic/corpus/entity_registry.yaml"
text = open(path, encoding='utf-8').read()
reg = yaml.safe_load(text)
ids = {e['id'] for e in reg['entities']}
assert all(x in ids for x in ('moses', 'israel_people', 'the_court', 'edom', 'the_moabites', 'the_amorite', 'yehoshua', 'eleazar_son_of_aaron')), 'the written-on and the named parties must stand'
ENT = [("the_sons_of_ammon", "people", "the sons of Ammon — Lot's younger daughter's people: 'and the younger, she also bore a son, and called his name Ben-ammi; the same is the father of the children of Ammon to this day' (Gen 19:38); 'the border of the children of Ammon was strong' (Num 21:24); 'when you come near over against the children of Ammon, do not harass them nor contend with them, for I will not give you of the land of the children of Ammon for a possession, because I have given it to the children of Lot for a possession' (Deut 2:19 — the bar and the grant; 2:37 the border respected; 3:11 Rabbah of the children of Ammon, Og's bed); Deut 23:4-7 the exclusion with Moab (forward); Judges 11 Jephthah's letter outside the Torah; the person Ben-ammi (Gen 19:38) is another row, as Moab beside the_moabites and Esau beside edom", "the-sons-of-ammon")]
added = 0
for eid, kind, en, tok in ENT:
    if eid in ids: continue
    if not text.endswith('\n'): text += '\n'
    text += f"  - id: {eid}\n    en: {q(en)}\n    kind: {kind}\n    members:\n      - {{token: {tok}, units: [step9-scenes]}}   # cold_run_opening_speech.py's narrative scene (THE DEUTERONOMY WALK 1b, 2026-09-15); the frozen units' tokens a later registry pass\n"
    added += 1
if added:
    open(path, 'w', encoding='utf-8').write(text)
reg = yaml.safe_load(open(path, encoding='utf-8'))
assert all(any(e['id'] == eid for e in reg['entities']) for eid, *_ in ENT)
print('entities: %d added of %d, registry %d' % (added, len(ENT), len(reg['entities'])))
# ---- the daemon block + the functions block (daemon_dispositions.yaml) ----
path = f"{ROOT}/World/step9/daemon_dispositions.yaml"
text = open(path, encoding='utf-8').read()
if '  law_opening_speech:' not in text:
    block = '''  law_opening_speech:
    file: cold_run_opening_speech.py
    wraps: opening_speech
    given_at: Deut 1:16
    installed_by: boot   # THE DEUTERONOMY WALK 1b (2026-09-15): A LAW IN MOSES' VOICE WITH NO DIVINE FRAME — 'and I charged your judges at that time' (1:16): the vows' class (Numbers 30:2 — Moses to the heads of the tribes), the second pass's D2 question (whether Moses' relay is itself an installing ACT); no installing act, no tent — the walk's standing setting; the class named here so the second pass finds it. THE READBACK'S FIRST FORM (THE_LOOP.md step 6, the owner's 'Yes 1. Go'): the eleven acts told only in the retelling are written ONCE at their own time by retrograde markers, four of them CLOSED at once by a prior run inside the daemon's branch; the retold acts are reference rows (DATA the_readback), never second acts
    watches:
      moses_told_to_ascend_abarim: [commanded]                                  # Num 27:12-14: ONE debit on Moses — see_the_land_from_abarim, OPEN by design (Deuteronomy 34:1-4 this book's end)
      a_shepherd_asked: [plea_made]                                             # Num 27:15-17: the plea the value
      joshua_commission_commanded: [commanded]                                  # Num 27:18-21: ONE debit on Moses — commission_joshua_before_eleazar
      joshua_commissioned: [invested_office]                                    # Num 27:22-23: on Joshua; the commission debit CLOSED by its run (the daemon's own close, closed_by Num 27:22-23) — the register seat Num 27:22 CLOSE
      speech_opened: [torah_expounded]                                          # Deut 1:1-5: the frame — a STATUS on Israel dated (40, 11, 1), the book's one act of its own day
      horeb_departure_commanded: [commanded]                                    # Deut 1:6-8: ONE debit on Israel dated (2, 2, 20), CLOSED at once by the prior run Num 12:16 (THE CLOSE BY A PRIOR RUN)
      judges_charged: [judges_charged]                                          # Deut 1:16-18: THE LAW — a STATUS on the court, the six clauses, dated (1, 2, 16)
      turn_northward_commanded: [commanded, contending_barred, land_granted]    # Deut 2:2-7: ONE debit on Israel CLOSED by the prior run Num 21:10-13; the bar and the grant (Mount Seir) on Edom
      moab_spared_commanded: [contending_barred, land_granted]                  # Deut 2:9: the bar and the grant (Ar) on the Moabites
      zered_crossing_commanded: [commanded]                                     # Deut 2:13: ONE debit on Israel CLOSED by the prior run Num 21:12
      ammon_spared_commanded: [contending_barred, land_granted]                 # Deut 2:17-19: the bar and the grant on the sons of Ammon (the one new party)
      sihon_war_commanded: [commanded]                                          # Deut 2:24-25, 2:31: ONE debit on Israel CLOSED by the prior run Num 21:24-25
      sihons_cities_devoted: [destroyed]                                        # Deut 2:34-35: the ban on Sihon's cities — on the Amorite (told only here)
      ogs_cities_devoted: [destroyed]                                           # Deut 3:6-7: the ban on Og's sixty — on the Amorite (told only here)
      joshua_encouraged: [fear_not_promised]                                    # Deut 3:21-22: HEAVEN's promise on Joshua (Numbers 21:34's effect at its second party)
      moses_besought: [plea_made]                                               # Deut 3:23-26: the plea and its refusal the value; the barred entry OPEN, read
      judges_case: [accepted, exempt, judgment_perverted]                       # the exam's rows on the judges' charge — the clauses, the courts' sizes, the disqualified, the examination, the verdict; the perverting judge the holiness engine's five effects by CALL
      speech_case: [accepted, exempt]                                           # the exam's rows on the frame, the date, the spies read back, the bypass, Sihon and Og, the east, the plea, the commission
'''
    i = text.index('  law_census:')
    text = text[:i] + block + text[i:]
if '\n  opening_speech:   # THE DEUTERONOMY WALK 1b' not in text:
    fb = '''  opening_speech:   # THE DEUTERONOMY WALK 1b (2026-09-15)
    the_commission: {status: WRAPPED, by: law_opening_speech}
    the_frame: {status: WRAPPED, by: law_opening_speech}
    the_officers_and_the_judges: {status: WRAPPED, by: law_opening_speech}
    the_spies_read_back: {status: WRAPPED, by: law_opening_speech}
    the_bypass: {status: WRAPPED, by: law_opening_speech}
    sihon_and_og: {status: WRAPPED, by: law_opening_speech}
    the_east_and_the_charges: {status: WRAPPED, by: law_opening_speech}
    the_plea: {status: WRAPPED, by: law_opening_speech}
'''
    i = text.index('  refuge:   # THE NUMBERS WALK 15b (2026-09-13)')
    j = text.index('\n  pre_sinai:', i)
    text = text[:j + 1] + fb + text[j + 1:]
open(path, 'w', encoding='utf-8').write(text)
dd = yaml.safe_load(open(path, encoding='utf-8'))
assert 'law_opening_speech' in dd['daemons'] and 'opening_speech' in dd['functions'], (list(dd)[:5])
print('daemons: %d (law_opening_speech %s); functions blocks: %d' % (len(dd['daemons']), 'law_opening_speech' in dd['daemons'], len(dd['functions'])))
# ---- the dependency span (the first in two books) + the eighteen CALL edges (the token-demanded edges and the POINTERS after the gate's print) ----
path = f"{ROOT}/World/step9/dependency_dispositions.yaml"
text = open(path, encoding='utf-8').read()
if '\n  opening_speech:' not in text.split('\nedges:')[0]:
    a = "  refuge:      [[Num, 35, 1, 34]]"
    i = text.index(a); j = text.index('\n', i)
    text = text[:j + 1] + "  opening_speech: [[Num, 27, 12, 23], [Deut, 1, 1, 46], [Deut, 2, 1, 37], [Deut, 3, 1, 29]]   # THE DEUTERONOMY WALK 1b (2026-09-15; DEUTERONOMY_WALK.md \"Sitting 1b\"): the opening speech with Joshua's commission as its callee — THE FIRST SPAN IN TWO BOOKS; the frame's one act of its own day, the judges' charge THE LAW (a status on the court), the eleven acts told only in the retelling written once at their own time by retrograde markers (four closed at once by a prior run), the retold acts reference rows graded (DATA the_readback), the three bars and grants, the two bans, the plea with its refusal\n" + text[j + 1:]
    W = "THE DEUTERONOMY WALK 1b (2026-09-15) | "
    edges = f'''  - {{from: opening_speech, to: exodus_story, disposition: CALL, link: reference, carries: verdict,
     why: "{W}1:9-15's officers are Exodus 18:21-26's judges retold (ES.jethro('denominations') CALLED = the four grains; ES.jethro('judges') CALLED = 78,600 — Sanhedrin 18a's total on the round six hundred thousand; ES.jethro('hard_cases') the hard matter of 1:17 read as the standing status hard_cases_to_moses); 2:7's forty years lacking nothing the manna's (ES.manna('forty_years') CALLED — Exodus 16:35); 1:33's pillar of fire and cloud Exodus 13:21's (by REFERENCE through the exodus story's by-day row); 1:44's 'as bees do' and Hormah with Exodus 17:13's Amalek"}}
  - {{from: opening_speech, to: shelach, disposition: CALL, link: reference, carries: verdict,
     why: "{W}1:19-46 is Numbers 13-14 READ BACK — every retold act a reference row graded against the tape's own line (DATA the_readback): the sending (13:2 against 1:22 — SL.spies by CALL: 'send for yourself' Sotah 34b:3), the twelve, the cluster, the report, the murmuring, the oath (SL.decree('set' / 'exceptions' / 'count_from' / 'deaths_ceased' / 'hormah' / 'turn_back' / 'presumption') CALLED — the sentence's rows read at the readback checkpoint), 1:39 VERBATIM = 14:31, 2:14's thirty-eight years from the spies' return (2, 5, 9); deaths_ceased (40, 5, 15) the fifteenth of Av at 2:16"}}
  - {{from: opening_speech, to: chukat, disposition: CALL, link: reference, carries: verdict,
     why: "{W}2:1-3:11 is Numbers 20-21 READ BACK — Edom's refusal against 2:4-8 and 2:29 (CK.edom_and_hor('edom_passage') CALLED: the DISPUTE row holding both arms, no teacher joins them — the readback's OPEN row), the departure from Mount Hor (40, 6, 1) the retrograde marker's day at 2:2 (CK.edom_and_hor('death_dates')), the Zered (21:12) and the march past Moab (21:10-13) the prior runs that CLOSE 2:2-7's and 2:13's debits, Sihon (21:21-25) the prior run closing 2:24-25's, Og TURNED (3:1-3 = 21:33-35: CK.well_and_kings('deut3_delta') CALLED), Og's lore (3:11's bed: CK.well_and_kings('og_lore')), Moab's land purified through Sihon (2:9: CK.well_and_kings('sihon_purified')), Ammon's border (2:37: CK.well_and_kings('ammon_border')), the succession for 27:19's Eleazar (CK.edom_and_hor('succession'))"}}
  - {{from: opening_speech, to: gad_reuben, disposition: CALL, link: reference, carries: verdict,
     why: "{W}3:12-20 is Numbers 32 READ BACK — the three holdings (32:33: GR.the_grant('three_parties' / 'land_held') CALLED — holding_given read at the readback checkpoint, 3:12-13 EXPANDED dividing what 32:33 gave whole), Jair and Machir (3:14-15 against 32:40-41: GR.machir_jair_nobah), the condition's debit OPEN (3:18-20 against 32:20-22: GR.the_condition), 'armed' at 3:18 = 32:30, 32; the fifteenth of Av (GR.DATA['deaths_ceased'])"}}
  - {{from: opening_speech, to: zelophehad, disposition: CALL, link: reference, carries: verdict,
     why: "{W}Numbers 27:12-23 is the callee's own chapter: the daughters' halt (27:1-11) is THE HARD MATTER of 1:17 ('the cause that is too hard for you' — the Sifrei 17:7: ZL.the_daughters('halt') CALLED, the third form — the judgment carried in by Moses); 27:12's 'go up' follows 27:11's statute on the tape (the daughters' marker at (40, 6, 1) the four lines' page_order bound); 36:1-12's second halt the tent's"}}
  - {{from: opening_speech, to: journeys, disposition: CALL, link: reference, carries: verdict,
     why: "{W}1:3's 'in the fortieth year' is dated the exodus's by the verbal analogy with 33:38's 'in the fortieth year of the going out' (Rosh Hashanah 2b:11 — JO.aarons_death_retold('verbal_analogy') CALLED: THE TRANSFER TAUGHT that places the forward marker; 'the_date' / 'the_era_new_year' / 'the_order' / 'arad' the chain's links — Aaron's death before the speech by 1:4's 'after he had smitten Sihon', Rosh Hashanah 2b:13); 1:1's stations against the list (JO.the_stations); Moses' seventh of Adar the speech's end (JO.aarons_death_retold('moses_seventh_adar'))"}}
  - {{from: opening_speech, to: borders, disposition: CALL, link: reference, carries: verdict,
     why: "{W}3:12-17's east and 1:7's promised extents against Numbers 34: the nine and a half (BO.moses_restatement('the_nine_and_a_half' / 'the_grant_read' / 'the_relay') CALLED — 3:12-13's halves read [1/2] by rule 30 as 34:13-15's), the Salt Sea and the Jordan the east's border at 3:17 (34:12), the Great Sea's side against 1:7's seashore; the relay form of 34:13"}}
  - {{from: opening_speech, to: second_census, disposition: CALL, link: reference, carries: verdict,
     why: "{W}the officers' count with the exact census: 79,064 by integer division at every grain of 603,550 (C2 the rolls' total — the exact against ES.jethro's round 78,600; the Sifrei 15:4's rounding rule integer division's own form); 27:21's 'the judgment of the Urim' final (C2.DATA['urim_judgment'] CALLED); 26:64-65's none left of the counted at 2:14-16 (C2.DATA['wilderness_survivors']); the age edges of the decree (C2.DATA['decree_age_edges'])"}}
  - {{from: opening_speech, to: balak, disposition: CALL, link: reference, carries: verdict,
     why: "{W}3:29's 'the valley over against Beth-peor' is the last camp (22:1: BK.the_call('last_camp') CALLED — the plains of Moab the speech's place; 4:46 and 34:6 the valley's other seats); the judges' count 78,600 at its Talmud seat (BK.peor('judges_count') CALLED — the Jerusalem Talmud's arithmetic); Moab spared at 2:9 against Balak's Moab and Midian (BK.DATA the midian_not_moab row — Bava Kamma 38a:16's a fortiori)"}}
  - {{from: opening_speech, to: primeval, disposition: CALL, link: reference, carries: verdict,
     why: "{W}1:8's 'the land which the LORD swore to your fathers' and 1:7's 'as far as the great river, the river Euphrates' are Genesis 15:18's covenant (PR.call('land_seats') CALLED — land_granted on the fathers' line, the effect standing since 15:18; 2:5, 2:9, 2:19's grants to Esau and Lot's sons the same effect on other peoples); 2:10-12's Emim and Rephaim Genesis 14:5's (PR the kings' war — the Rephaim, the Zuzim, the Emim at their first seats); 2:34's ban beside Genesis 15:16's 'the iniquity of the Amorite is not yet full' (the amorite_not_full status READ, a printed line)"}}
  - {{from: opening_speech, to: mamre, disposition: CALL, link: reference, carries: verdict,
     why: "{W}2:9's 'the children of Lot' and 2:19's 'the children of Lot' are Genesis 19:37-38's Moab and Ben-ammi (MM's Lot cells CALLED — the two daughters' sons named; the registry row the_sons_of_ammon the younger's people): the bars' difference the reward of the daughters' two speeches (Horayot 10b:19-11a:1; Nazir 23b:11-12); 3:24's 'O Lord GOD' Abraham's two seats (Genesis 15:2, 15:8) beside Moses' two (3:24; 9:26)"}}
  - {{from: opening_speech, to: joseph, disposition: CALL, link: reference, carries: verdict,
     why: "{W}2:4-5's 'your brothers the children of Esau, who dwell in Seir … I have given Mount Seir to Esau for a possession' is Genesis 36:8's 'Esau dwelt in Mount Seir; Esau is Edom' (JS's Esau cells CALLED — the settlement in Seir, 36:6-8); 2:12, 2:22's Horites 'who dwelt in Seir beforetime' Genesis 36:20-21's (JS the sons of Seir the Horite — the dispossessions DATA)"}}
  - {{from: opening_speech, to: ordinances, disposition: CALL, link: reference, carries: verdict,
     why: "{W}1:16-17's charge and Exodus 23:1-8's court clauses (OR.courts CALLED — 'asymmetry' the majority of two for evil and one for good at Mishnah Sanhedrin 3:6-7's divided court and 2a:16's twenty-three; 'twenty_three'; 'one_vs_two' the ten differences' second, 32a:3; 'bribe' at 1:17's no faces — Peah 8:9); 1:7's Euphrates and Exodus 23:31's border ('from the wilderness to the river' — the same extent)"}}
  - {{from: opening_speech, to: holiness, disposition: CALL, link: reference, carries: verdict,
     why: "{W}1:17's 'you shall not respect persons in judgment' is Leviticus 19:15's 'you shall not respect the person of the poor nor honor the person of the mighty; in righteousness you shall judge your neighbor' (HO.conduct('five_effects') CALLED — the judge who perverts defiles the land, profanes the Name, removes the Presence, fells by the sword, exiles: the exam's judgment_perverted verdict; HO.conduct('talebearer') at Sanhedrin 30a:16 / 31a:10 — Leviticus 19:16 the divided court's silence); 'judge righteously' (1:16) the same verse's 'in righteousness'"}}
  - {{from: opening_speech, to: erection, disposition: CALL, link: reference, carries: verdict,
     why: "{W}1:6's 'the LORD our God spoke to us in Horeb … turn and take your journey' is Exodus 33:1's 'depart, go up hence, you and the people' retold (ER.presence('horev_plene') CALLED — Horeb written plene at Exodus 33:6 alone; the departure's command's kin, its day Numbers 10:11's — the retrograde marker at 1:6); Avot 1:1's chain from Moses to Joshua (ER's oral_law_unwritten row) at the charge's be_deliberate; the nations' seven orders (ER) beside 1:7's seven regions"}}
  - {{from: opening_speech, to: bamidbar, disposition: CALL, link: reference, carries: verdict,
     why: "{W}the officers' exact count is the census's total: 603,550 (CB.census('total') CALLED — 1:46; 79,064 = 603 + 6,035 + 12,071 + 60,355 by integer division at the four grains); 1:15's 'heads over you, captains of thousands, of hundreds, of fifties, of tens, and officers for your tribes' the tribes' order the camp's (CB.camp)"}}
  - {{from: opening_speech, to: beha, disposition: CALL, link: reference, carries: verdict,
     why: "{W}1:9-12's 'I am not able to bear you myself alone … how can I myself alone bear your cumbrance and your burden and your strife' is Numbers 11:14's 'I am not able to bear all this people alone' (BH.seventy_elders('sanhedrin') CALLED — the seventy with Moses over them the seventy-one, Sanhedrin 2a:13 / 16b:18; 'with you — like you', 17a:3 the same burden-word); 1:6's departure day (2, 2, 20) is 10:11's march (BH.march('date') CALLED — M['march'] the retrograde marker's day); Hobab's row the plea_made effect's first form (11:29-32)"}}
  - {{from: opening_speech, to: refuge, disposition: CALL, link: reference, carries: verdict,
     why: "{W}3:12-17's east holds the three cities of Deuteronomy 4:41-43 (Bezer in the plain for the Reubenites, Ramoth in Gilead for the Gadites, Golan in Bashan for the Manassites — RF.the_refuge_law('six_cities') CALLED: the six cities DATA row naming them, the debit appoint_six_cities_of_refuge OPEN BY DESIGN to 4:41 — CHAPTER 4's, not this compile's, READ THEN COMPILE PER PORTION; Makkot 9b:18, 10a:14-15 the docket's OUTSIDE rows); 1:17's 'no faces' and the kin and the haters off the bench (RF.DATA['the_court_of_twenty_three'] — Sanhedrin 29a:6 on Numbers 35:23's 'not his enemy')"}}
  - {{from: sequence, to: opening_speech, disposition: CALL, link: none,
     why: "{W}the sequential run's REGISTRATION edge — ('cold_run_opening_speech', 'law_opening_speech') in DAEMON_ORDER (the runner compiles no verse: link none, O4's license); the sixteen tape lines and the four markers (Deut 1:1 forward; 1:6, 1:9, 2:2 retrograde) this sitting's"}}
'''
    a = "  - {from: sequence, to: refuge, disposition: CALL, link: none,"
    i = text.index(a); j = text.index('\n', text.index('why:', i)) + 1
    text = text[:j] + edges + text[j:]
    open(path, 'w', encoding='utf-8').write(text)
dep = yaml.safe_load(open(path, encoding='utf-8'))
n_os = sum(1 for e in dep['edges'] if e['from'] == 'opening_speech')
assert 'opening_speech' in dep['spans'] and n_os == 18, n_os
print('dependency: span (two books) + 19 edges (opening_speech 18 CALL and the registration); the token-demanded edges and the pointers after the gate\'s print')
# ---- the installation probe's count ----
path = f"{ROOT}/World/step9/installation_probes.py"
text = open(path, encoding='utf-8').read()
if "len(real) == 62 and all(" in text:
    text = text.replace("len(real) == 62 and all('given_at' in d and 'installed_by' in d for d in real.values())   # THE NUMBERS WALK 15b (2026-09-13): 61 -> 62, law_refuge",
                        "len(real) == 63 and all('given_at' in d and 'installed_by' in d for d in real.values())   # THE DEUTERONOMY WALK 1b (2026-09-15): 62 -> 63, law_opening_speech (installed_by boot — a law in Moses' voice with no divine frame, the class named); 15b: 61 -> 62, law_refuge")
    open(path, 'w', encoding='utf-8').write(text)
assert "len(real) == 63" in open(path, encoding='utf-8').read()
print('installation_probes I5: 63')
