#!/usr/bin/env python3
# THE NUMBERS WALK sitting 12b — THE COMPILE OF GAD AND REUBEN (2026-09-12; World/step9/NUMBERS_WALK.md "Sitting 12b"): THE TYPES FIRST — TWELVE
# tape kinds (the chapter's speeches and acts, Num 32:1-42), FOUR case-form kinds for the exam's scene, ONE new effect (clear_before_the_lord_
# and_israel, status — the ink's own words at 32:22), SEVEN registry rows (the sons of Gad and Reuben — the ink's compound; the sons of Gad; the
# sons of Reuben; the half tribe of Manasseh; the dividers of the land — 32:28's triad; Jair son of Manasseh; Nobah — the parties whose tokens the
# registry's homographs would have swallowed: gad and reuben are Jacob's sons), the 59th daemon's block (law_gad_reuben, given_at Num 32:20,
# installed_by BOOT with the class named — a stipulation in Moses' voice with no divine frame, 30:2's class), the functions block, the dependency
# span and edges (the pointers after the gate's print), the installation probe's count. The `he` is cut from the pointed DB text (cantillation
# stripped) by FINDING the phrase's tokens (never a typed index); the witnesses the plain consonantal verses. Idempotent (add_types_midian.py's form).
import re, sqlite3, yaml
ROOT = "<repo-old>"
db = sqlite3.connect(f"file:{ROOT}/elijah_docket/tanakh.sqlite?mode=ro", uri=True)
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
def PHRASE(ch, vs, toks):
    """the pointed text of the phrase FOUND in the verse by its plain tokens (the index computed, never typed)"""
    plain = LV('Num', ch, vs).split(); n = len(toks)
    hits = [i for i in range(len(plain) - n + 1) if plain[i:i + n] == toks]
    assert len(hits) == 1, (ch, vs, toks, hits, plain)
    return PV('Num', ch, vs, hits[0] + 1, hits[0] + n)
q = lambda s: '"' + s.replace('\\', '\\\\').replace('"', '\\"') + '"'
N = 'Num'
def HE(ch, lo, hi, en, cap=6):
    vv = list(range(lo, min(hi, lo + cap - 1) + 1))
    s = ' · '.join(PV(N, ch, v) + ' (%s — Num %d:%d)' % (en if v == lo else 'the verse continues', ch, v) for v in vv)
    return s + (' · … (through Num %d:%d)' % (ch, hi) if hi > vv[-1] else '')
def WIT(ch, lo, hi):
    return ['Num %d:%d | %s' % (ch, v, LV(N, ch, v)) for v in range(lo, hi + 1)]
CORPUS = "num_32_gad_reuben (STEP_Nm_32_1 through STEP_Nm_32_42; claims MT32A-01 through MT32A-10)"
SUB = "submitted by cold_run_gad_reuben.py [subjects: %s] (the narrative scene, THE NUMBERS WALK 12b); re-submitted on the sequential tape by cold_run_sequence.py; consumed by law_gad_reuben (cold_run_gad_reuben.py) -> %s"
CASE = "submitted by cold_run_gad_reuben.py [subjects: the exam's persons] (the wrap's scene); consumed by law_gad_reuben (cold_run_gad_reuben.py) -> %s"
INK_ALL = "Num 32:1-42; Onkelos Num 32:1-42 (a place fit for a house of cattle; before the PEOPLE of the LORD at the six martial seats; Nebo the burial place of Moses; what goes out of your mouth in the vows' Aramaic; the holding of our possession); the Sifrei on Numbers SILENT (no piska from 31:25 to 35:8 — found by position; 86:1, 95:1, 106:1 cite 32:1 and 32:37-38); Num 30:3 (the utterance rule's first seat — 'all that goes out of his mouth he shall do'); Num 14:21-35 (the oath retold — 'as I live', the forty years, the doomed set 'from twenty years old and upward', Caleb and Joshua excepted); Num 21:21-35 (Sihon's and Og's kingdoms — the grant's source); Num 26:7, 18, 34 (the two and a half's counts); Num 26:29, 27:1, 36:1 (Machir's line); Num 1:3, 26:2, Exod 30:14 (the census formula); Gen 50:23 (the sons of Machir on Joseph's knees); Gen 47:11 (a holding given — the same word); Deut 3:12-20, Josh 1:12-18, 4:12-13, 13:8-32, 22:1-9 (the retellings and the RELEASE — runs outside the Torah); Josh 14:1, 21:1 (the commission's triad); Josh 17:1-6 (Machir the man of war; the ten parts beside Gilead and Bashan); Judg 5:16, 8:11, 10:3-5, 11:10, 11:36 (observed); 1Chr 2:21-22, 5:18 (Jair's other lineage; the 44,760); Isa 15-16, Jer 48, Ezek 25:9 (Moab's later hold); Babylonian Talmud Kiddushin 61a-62a, Bava Metzia 94a, Gittin 75a-b, Nedarim 11a, Shevuot 36a, Yoma 38a, Pesachim 13a, Bava Batra 117a-122a, Sotah 34b-35a, Sanhedrin 111a, Sotah 3a, 13b, Berakhot 8b, Bekhorot 4b; Mishnah Kiddushin 3:4, Shekalim 3:2"
KINDS = [
 ("land_requested", "speech",
  "the land requested — 'and the sons of Reuben and the sons of Gad had much cattle, very numerous; and they saw the land of Jazer and the land of Gilead, and behold, the place was a place for cattle; and the sons of Gad and the sons of Reuben came and spoke to Moses and to Eleazar the priest and to the princes of the congregation, saying: Ataroth and Dibon and Jazer and Nimrah and Heshbon and Elealeh and Sebam and Nebo and Beon, the land which the LORD smote before the congregation of Israel, is a land for cattle, and your servants have cattle; and they said: if we have found favour in your eyes, let this land be given to your servants for a possession; do not bring us over the Jordan' (Num 32:1-5): REUBEN FIRST at 32:1 alone, GAD FIRST at the compound's six seats (32:2, 6, 25, 29, 31, 33 — the party the ink's compound); 27:2's TRIAD addressed WITHOUT a halt (no case brought before the LORD; no divine frame in the chapter); the nine cities; 'a possession' (a holding — Genesis 47:11's word); the plea's status on the asked (Hobab's, Caleb's form)",
  HE(32, 1, 5, "and the sons of Reuben and the sons of Gad had much cattle, very numerous"), WIT(32, 1, 5), INK_ALL, CORPUS,
  SUB % ("the-sons-of-gad-and-reuben", "plea_made on the-sons-of-gad-and-reuben (the request's two clauses — 'let this land be given to your servants for a possession; do not bring us over the Jordan'); one entity"), ["to", "cities", "request"]),
 ("moses_rebuked_the_tribes", "speech",
  "Moses' rebuke and the oath retold — 'shall your brothers go to war and you sit here? why do you DISCOURAGE the heart of the children of Israel from passing over into the land which the LORD has given them? so did your fathers when I sent them from Kadesh-barnea to see the land ... and the LORD's anger burned on that day and HE SWORE, saying: surely none of the men who came up from Egypt, FROM TWENTY YEARS OLD AND UPWARD, shall see the land which I swore to Abraham, to Isaac and to Jacob, for they have not followed Me fully — save Caleb son of Jephunneh THE KENIZZITE and Joshua son of Nun, for they have followed the LORD fully; and the LORD's anger burned against Israel and he made them wander in the wilderness FORTY YEARS, until all the generation that did evil in the eyes of the LORD was consumed; and behold, you have risen in your fathers' stead, a brood of sinful men, to add yet to the fierce anger of the LORD against Israel; for if you turn from after him he will yet again leave them in the wilderness, and you will destroy all this people' (Num 32:6-15): THE HINDER-ROOT the vows' verb (30:6-12; 32:7 a written-and-read pair); the spies' verb at each telling; THE OATH RETOLD WITH THE VERB SUPPLIED (14:21, 28 'as I live'); the census formula the doomed set's (14:29 — 603,550 by CALL); the exceptions by CALL; the parser's [20] and [40]; the causative's one Torah seat; 'did evil in the eyes of the LORD' the Kings' formula at its first seat; NO WRITE — the rebuke reads chapter 14's ledger (the checkpoint CG3)",
  HE(32, 6, 15, "and Moses said to the sons of Gad and to the sons of Reuben: shall your brothers go to war and you sit here?"), WIT(32, 6, 15), INK_ALL, CORPUS,
  SUB % ("moses", "NO WRITE — the oath retold is read against the ledger: israel_people's sentence_pronounced (14:26-35) and the forty years' timer fired at (40, 5, 9); caleb's holding_owed OPEN; the decree's set by CALL"), ["to", "oath", "set", "exceptions", "years"]),
 ("tribes_offered_to_arm", "speech",
  "the offer — 'and they drew near to him and said: folds for our cattle we will build here, and cities for our little ones; and WE will arm ourselves, hastening, before the children of Israel until we have brought them to their place, and our little ones shall dwell in the fortified cities because of the inhabitants of the land; we will not return to our houses until the children of Israel have inherited every man his inheritance; for we will not inherit with them across the Jordan and beyond, because our inheritance has come to us on this side of the Jordan eastward' (Num 32:16-19): THE CATTLE BEFORE THE CHILDREN (Moses reverses it at 32:24); THE ARM-ROOT's seven tokens; 'until every man has inherited' — the retellings' 'until the LORD gives rest' (Deuteronomy 3:20, Joshua 1:15) and the release 'now the LORD has given rest' (Joshua 22:4); NO WRITE — the offer is the utterance the rule binds at Moses' word (32:24)",
  HE(32, 16, 19, "and they drew near to him and said: folds for our cattle we will build here, and cities for our little ones"), WIT(32, 16, 19), INK_ALL, CORPUS,
  SUB % ("the-sons-of-gad-and-reuben", "NO WRITE — the undertaking is bound at the condition's line (32:20-24) by the utterance rule"), ["folds", "cities", "arm", "until"]),
 ("condition_stipulated", "speech",
  "the condition stipulated — 'and Moses said to them: if you do this thing, if you arm yourselves before the LORD for the war, and every armed one of you passes over the Jordan before the LORD until he has dispossessed his enemies from before him, and the land is subdued before the LORD, and afterward you return — you shall be CLEAR BEFORE THE LORD AND BEFORE ISRAEL, and this land shall be yours for a possession before the LORD; and if you do not do so, behold, you have sinned against the LORD, and know your sin which will find you; build for yourselves cities for your little ones and folds for your sheep, and THAT WHICH HAS GONE OUT OF YOUR MOUTH YOU SHALL DO' (Num 32:20-24): THE DOUBLED CONDITION — Mishnah Kiddushin 3:4's exemplar (the positive arm 32:20-22, the negative 32:23; the condition before the act; the positive before the negative; the condition's matter and the act's distinct — Gittin 75a-b; a condition that can be fulfilled — Bava Metzia 94a); 'before the LORD' seven tokens, Onkelos buffering the six martial seats to 'before the people of the LORD'; THE CLEARANCE — Shekalim 3:2's proof; 'your sin which will find you' Judah's idiom (Genesis 44:16); THE UTTERANCE RULE'S SECOND SEAT — 30:3's phrase, the vows' cell by CALL (its own effect commanded); THE LEDGER — the debit to cross armed OPEN BY DESIGN (the release Joshua 22:1-9 a run outside the Torah), the build command CLOSED at 32:34-38",
  HE(32, 20, 24, "and Moses said to them: if you do this thing, if you arm yourselves before the LORD for the war"), WIT(32, 20, 24), INK_ALL, CORPUS,
  SUB % ("moses", "commanded on the-sons-of-gad-and-reuben TWICE (the values cross_armed_before_the_lord_until_the_land_is_subdued — OPEN, its run Joshua 22:1-9 outside the Torah; build_cities_and_folds — closed by value at 32:34-38); the utterance rule VW.the_man('all_that_proceeds') by CALL"), ["to", "positive_arm", "negative_arm", "clearance", "utterance_rule", "build"]),
 ("tribes_accepted_the_condition", "speech",
  "the acceptance — 'and the sons of Gad and the sons of Reuben spoke to Moses, saying: your servants will do as my lord commands; our little ones, our wives, our cattle and all our beasts shall be there in the cities of Gilead; and your servants will pass over, every armed one for war before the LORD, to the war, as my lord says' (Num 32:25-27): 'my lord' for Moses (32:25, 27 — Joshua's 11:28, Aaron's 12:11, the Gileadite heads' 36:2); the acceptance's order little ones, wives, cattle — Moses' reversal held (the retellings Deuteronomy 3:19, Joshua 1:14); NO WRITE — the debit was written at the condition; the assent stands on the tape as a speech",
  HE(32, 25, 27, "and the sons of Gad and the sons of Reuben spoke to Moses, saying: your servants will do as my lord commands"), WIT(32, 25, 27), INK_ALL, CORPUS,
  SUB % ("the-sons-of-gad-and-reuben", "NO WRITE — the condition's seal on the parties' side; the debit stands from 32:20-24"), ["to", "order"]),
 ("commission_charged", "speech",
  "the commission charged — 'and Moses commanded concerning them Eleazar the priest, and Joshua son of Nun, and the heads of the fathers of the tribes of the children of Israel; and Moses said to them: if the sons of Gad and the sons of Reuben pass over the Jordan with you, every armed one for war before the LORD, and the land is subdued before you, you shall give them the land of Gilead for a possession; and if they do not pass over armed with you, they shall take possessions among you in the land of Canaan' (Num 32:28-30): THE TRIAD of Joshua 14:1 and 21:1 word for word — the dividers of the land; THE SECOND DOUBLING (32:29-30 — the exam's proof verses); the commission's debit OPEN BY DESIGN (Joshua 1:12-18 the charge repeated, 22:1-9 the release — runs outside the Torah); Bava Batra 122a:4's picture of the lottery (Eleazar with the Urim, Joshua and all Israel before him)",
  HE(32, 28, 30, "and Moses commanded concerning them Eleazar the priest, and Joshua son of Nun, and the heads of the fathers of the tribes of the children of Israel"), WIT(32, 28, 30), INK_ALL, CORPUS,
  SUB % ("moses", "commanded on the-dividers-of-the-land (the value give_them_gilead_if_they_cross — OPEN, its run Joshua 1:12-18 and 22:1-9 outside the Torah); one entity"), ["to", "positive_arm", "negative_arm"]),
 ("tribes_answered_so_will_we_do", "speech",
  "the answer — 'and the sons of Gad and the sons of Reuben answered, saying: that which the LORD has spoken to your servants, so will we do; WE will pass over armed before the LORD to the land of Canaan, and the possession of our inheritance with us across the Jordan' (Num 32:31-32): THE PARTIES CALL MOSES' STIPULATION THE LORD'S WORD (Joshua 22:9's 'by the commandment of the LORD by the hand of Moses' — the installed_by class's witness); 'we' in its short form (three Bible seats); 'the possession of our inheritance' the daughters' construct (27:7); NO WRITE",
  HE(32, 31, 32, "and the sons of Gad and the sons of Reuben answered, saying: that which the LORD has spoken to your servants, so will we do"), WIT(32, 31, 32), INK_ALL, CORPUS,
  SUB % ("the-sons-of-gad-and-reuben", "NO WRITE — the answer stands on the tape as a speech"), ["to", "the_lords_word"]),
 ("land_granted_east", "act",
  "the land granted east of the Jordan — 'and Moses gave to them — to the sons of Gad and to the sons of Reuben and to half the tribe of Manasseh son of Joseph — the kingdom of Sihon king of the Amorite and the kingdom of Og king of Bashan, the land with its cities in the borders, the cities of the land round about' (Num 32:33): THREE TRANSFERS from Israel's possession by conquest (the chukat runner's land_possessed at 21:24-25, 21:31-32, 21:35 — the grant's source on the ledger; CK.well_and_kings('land_east') by CALL); HALF MANASSEH FIRST NAMED at the grant (no stipulation spoken to it in the chapter — Deuteronomy 3:18-20, Joshua 1:12-15, 4:12 extend the crossing; Joshua 17:5-6's 'beside the land of Gilead and Bashan', Bava Batra 118b:8); THE TWO AND A HALF'S COUNT 43,730 + 40,500 + 52,700 ÷ 2 = 110,580 from the population table against Joshua 4:13's 'about forty thousand' and 1 Chronicles 5:18's 44,760; 'on condition' is 'from now' — the gift takes effect at once under the condition (Gittin 75b:2)",
  HE(32, 33, 33, "and Moses gave to them — to the sons of Gad and to the sons of Reuben and to half the tribe of Manasseh son of Joseph — the kingdom of Sihon king of the Amorite and the kingdom of Og king of Bashan"), WIT(32, 33, 33), INK_ALL, CORPUS,
  SUB % ("moses", "holding_given on the-sons-of-gad, on the-sons-of-reuben and on the-half-tribe-of-manasseh (cp israel — the holder by conquest; the value the two kingdoms from the ledger's own land_possessed entries); three entities"), ["to", "kingdoms", "count"]),
 ("cities_built_east", "act",
  "the cities built — 'and the sons of Gad built Dibon and Ataroth and Aroer, and Atroth-shophan and Jazer and Jogbehah, and Beth-nimrah and Beth-haran, fortified cities and folds for sheep; and the sons of Reuben built Heshbon and Elealeh and Kiriathaim, and Nebo and Baal-meon (their names being changed) and Sibmah, and they called by names the names of the cities which they built' (Num 32:34-38): GAD'S EIGHT and REUBEN'S SIX from the tokens; the nine asked split four and five (Nimrah as Beth-nimrah, Sebam as Sibmah, Beon as Baal-meon); the two renamed one seat; THE RUN of 32:24's 'build for yourselves cities' — the build debit CLOSED BY VALUE; Dibon Gad the itinerary's witness (33:45-46); Dibon and Heshbon crossed between the tribes in Joshua 13; ten of the cities Moab's in the prophets; Nebo Reuben's — Moses' grave (Sotah 13b:20; Onkelos 32:3)",
  HE(32, 34, 38, "and the sons of Gad built Dibon and Ataroth and Aroer"), WIT(32, 34, 38), INK_ALL, CORPUS,
  SUB % ("the-sons-of-gad-and-reuben", "cities_built on the-sons-of-gad (the eight) and on the-sons-of-reuben (the six, two renamed); CLOSE the-sons-of-gad-and-reuben's commanded build_cities_and_folds by value (32:34-38)"), ["gad", "reuben", "renamed"]),
 ("gilead_taken_by_machir", "act",
  "Gilead taken by the sons of Machir — 'and the sons of Machir son of Manasseh went to Gilead and took it, and dispossessed the Amorite who was in it; and Moses gave Gilead to Machir son of Manasseh, and he dwelt in it' (Num 32:39-40): THE SONS OF MACHIR the Genesis 50:23 collective ('born on Joseph's knees' — the registry's row, its second write); 'dispossessed the Amorite' 21:32's verb (the land possessed by conquest — the chukat runner's effect at its fourth seat); Machir the clan under the ancestor's name (26:29 'Machir begot Gilead'; Joshua 17:1 'the father of Gilead, for he was a man of war'; Deuteronomy 3:15); Jair and Machir the wilderness' survivors born in Jacob's days (Bava Batra 121b:9)",
  HE(32, 39, 40, "and the sons of Machir son of Manasseh went to Gilead and took it, and dispossessed the Amorite who was in it"), WIT(32, 39, 40), INK_ALL, CORPUS,
  SUB % ("the-sons-of-machir", "land_possessed on the-sons-of-machir (cp the-amorite — Gilead taken, the Amorite dispossessed) and holding_given on the-sons-of-machir (cp moses — 'Moses gave Gilead to Machir'); no new entity (Genesis's collective written on again)"), ["took", "dispossessed", "given"]),
 ("villages_taken_by_jair", "act",
  "the villages taken by Jair — 'and Jair son of Manasseh went and took their villages, and called them Havvoth-jair' (Num 32:41): 'went and took' at 32:41-42 alone; Havvoth-jair's six seats (Deuteronomy 3:14, Joshua 13:30, Judges 10:4, 1 Kings 4:13, 1 Chronicles 2:23); JAIR'S TWO LINEAGES — 'son of Manasseh' here, Deuteronomy 3:14, 1 Kings 4:13 against 1 Chronicles 2:21-22's Hezron's grandson by Machir's daughter; the judge Jair's thirty cities 'called Havvoth-jair' (Judges 10:4 — the parser's [30, 30, 30]), Mordecai's ancestor (Esther 2:5), Elhanan's father (1 Chronicles 20:5) the homograph traps; 'about thirty-six' at Ai read as Jair (Bava Batra 121b:10)",
  HE(32, 41, 41, "and Jair son of Manasseh went and took their villages, and called them Havvoth-jair"), WIT(32, 41, 41), INK_ALL, CORPUS,
  SUB % ("jair", "land_possessed on jair (their villages, called Havvoth-jair — the naming inside the value); one entity (jair)"), ["took", "named"]),
 ("kenath_taken_by_nobah", "act",
  "Kenath taken by Nobah — 'and Nobah went and took Kenath and its daughters, and called it Nobah after his own name' (Num 32:42): 'its daughters' the villages (21:25 Heshbon's, 21:32 Jazer's); NOBAH AND JOGBEHAH together at Judges 8:11 on Gideon's route against Midian — the two names' only other seat; the place Nobah the homograph trap; Kenath's one other seat 1 Chronicles 2:23",
  HE(32, 42, 42, "and Nobah went and took Kenath and its daughters, and called it Nobah after his own name"), WIT(32, 42, 42), INK_ALL, CORPUS,
  SUB % ("nobah", "land_possessed on nobah (Kenath and its daughters, called Nobah — the naming inside the value); one entity (nobah)"), ["took", "named"]),
 ("stipulation_case", "case", "the exam's rows on the doubled condition and the law of conditions (Num 32:20-24, 32:29-30 — Mishnah Kiddushin 3:4; Kiddushin 61a:9-62a:14; Gittin 75a:10-75b:8; Bava Metzia 94a:2-14; Nedarim 11a:2; Shevuot 36a:25-29): the doubling (R. Meir / R. Chanina ben Gamliel), the condition before the act, the positive before the negative, the condition's matter and the act's distinct, a condition that can be fulfilled (R. Yehuda ben Teima), the negative arm's two readings, 'on condition' as 'from now', a condition counter to the Torah, the rule's scope (monetary / ritual), the exemplar's kin across the books",
  HE(32, 29, 30, "and Moses said to them: if the sons of Gad and the sons of Reuben pass over the Jordan with you, every armed one for war before the LORD, and the land is subdued before you, you shall give them the land of Gilead for a possession"), WIT(32, 20, 24) + WIT(32, 29, 30), INK_ALL, CORPUS, CASE % "commanded / holding_given / accepted / exempt (the exam's persons)", ["person", "ask"]),
 ("clearance_case", "case", "the exam's rows on the clearance (Num 32:22 — Mishnah Shekalim 3:2; Yoma 38a:9, 38a:12; Pesachim 13a:13-14): the treasury's clerk with no cuffed garment, shoe, sandal, phylacteries or amulet; the House of Garmu's coarse bread; the House of Avtinas's unperfumed brides; the charity collectors who sell and change with others — 'a person must appear justified before people as before the Omnipresent'",
  HE(32, 22, 22, "and the land is subdued before the LORD, and afterward you return — you shall be clear before the LORD and before Israel, and this land shall be yours for a possession before the LORD"), WIT(32, 22, 22), INK_ALL, CORPUS, CASE % "clear_before_the_lord_and_israel / accepted / exempt (the exam's persons)", ["person", "ask"]),
 ("oath_retold_case", "case", "the exam's rows on the oath retold (Num 32:6-15 — Sanhedrin 111a:6, 111a:12-13; Bava Batra 117b:2, 118b:3, 121a:9-121b:1, 121b:8, 121b:11, 122a:12; Sotah 34b:3, 34b:7-8, 35a:4): two of six hundred thousand, the exceptions and their portions, Caleb's Hebron and 'another spirit', Joshua childless and nothing owed him, the decree's set and its edges (Levi outside; under twenty and over sixty), the deaths ceased on the fifteenth of Av, 'send you' at Moses' discretion beside 'when I sent them', slow to anger at the pardon",
  HE(32, 11, 12, "surely none of the men who came up from Egypt, from twenty years old and upward, shall see the land which I swore to Abraham, to Isaac and to Jacob, for they have not followed Me fully"), WIT(32, 6, 15), INK_ALL, CORPUS, CASE % "exempt / holding_owed / accepted (the exam's persons)", ["person", "ask"]),
 ("land_east_case", "case", "the exam's rows on the grant east of the Jordan, the cities and the conquerors (Num 32:1-5, 32:33-42 — Bava Batra 118b:8, 119a:1, 119a:5, 119b:3-4, 121b:9-11, 122a:4; Sotah 13b:20; Berakhot 8b:1; Bekhorot 4b:7): half Manasseh's Gilead and Bashan beside its ten parts, the land held before assignment, the exodus generation bequeathing without inheriting, Jair and Machir the wilderness' survivors, the commission at the lottery, Moses' grave in Reuben's Nebo, the nine names read twice with their translation, the cattle's multitude as a proof",
  HE(32, 33, 33, "and Moses gave to them — to the sons of Gad and to the sons of Reuben and to half the tribe of Manasseh son of Joseph — the kingdom of Sihon king of the Amorite and the kingdom of Og king of Bashan"), WIT(32, 1, 5) + WIT(32, 33, 42), INK_ALL, CORPUS, CASE % "holding_given / land_possessed / accepted / exempt (the exam's persons)", ["person", "ask"]),
]
assert len(KINDS) == 16, len(KINDS)
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
print('kinds: %d added of %d, registry %d' % (len(out), len(KINDS), len(after['events'])))
# ---- ONE new effect, the ink's own words, the `he` FOUND in the verse ----
path = f"{ROOT}/World/step9/effect_vocabulary.yaml"
text = open(path, encoding='utf-8').read()
fx = yaml.safe_load(text)['effects']
for e in ('plea_made', 'commanded', 'holding_given', 'holding_owed', 'cities_built', 'land_possessed', 'accepted', 'exempt'):
    assert e in fx, e
HE_CLEAR = PHRASE(32, 22, ['והייתם', 'נקיים', 'מיהוה', 'ומישראל'])
NEW = [
 ('clear_before_the_lord_and_israel', 'status',
  "clear before the LORD and before Israel — the STATUS the condition's positive arm names as its outcome and the exam writes on the person who is beyond suspicion: 'and the land is subdued before the LORD, and afterward you return — you shall be CLEAR BEFORE THE LORD AND BEFORE ISRAEL, and this land shall be yours for a possession before the LORD' (Num 32:22); the tradition's rule from this verse: A PERSON MUST APPEAR JUSTIFIED BEFORE PEOPLE AS BEFORE THE OMNIPRESENT — the one who collects from the treasury chamber enters with no cuffed garment, shoe, sandal, phylacteries or amulet (Mishnah Shekalim 3:2), the House of Garmu's descendants never held refined bread and the House of Avtinas's brides never perfumed (Yoma 38a:9, 38a:12), the charity collectors sell to others and change money with others (Pesachim 13a:13-14); INSIDE THE TORAH THE STATUS IS NEVER WRITTEN ON THE TAPE — the release is Joshua's ('now the LORD has given rest to your brothers as he spoke to them; now turn and go to your tents', Joshua 22:4), a run outside the Torah; David's 'I and my kingdom are clear before the LORD' (2 Samuel 3:28) its kin; 1 Chronicles 22:18's 'subdued before the LORD and before his people' the double in Chronicles' own ink",
  HE_CLEAR + " (and you shall be clear before the LORD and before Israel — Num 32:22)",
  "Num 32:22 ('clear before the LORD and before Israel' — one Bible seat; 'the land is subdued before the LORD'; 'a possession before the LORD'), 32:20-24 (the condition's positive arm), 32:29 (the second doubling's 'subdued before you'); Onkelos 32:22 ('acquitted before the LORD and before Israel'); Josh 22:1-9 (the release — the run outside the Torah); 2 Sam 3:28; 1 Chr 22:18; Mishnah Shekalim 3:2; Babylonian Talmud Yoma 38a:9, 38a:12; Pesachim 13a:13-14",
  "num_32_gad_reuben (STEP_Nm_32_22; the claim MT32A-06)",
  "cold_run_gad_reuben.py (F4 the_condition — the clearance's cell; the exam kind clearance_case: the effect on the clerk, the bakers, the perfumers, the collectors); Mishnah Shekalim 3:2 (the headline row)"),
]
added = 0
for name, op, en, he, ink, corpus, exam in NEW:
    if name in fx: continue
    text = text.rstrip('\n') + '\n' + f"  {name}:\n    en: {q(en)}\n    he: {q(he)}\n    ledger_op: {op}   # THE NUMBERS WALK 12b (2026-09-12): Gad and Reuben's compile — {name}\n    ink: {q(ink)}\n    corpus: {q(corpus)}\n    exam: {q(exam)}\n"
    added += 1
open(path, 'w', encoding='utf-8').write(text)
fx = yaml.safe_load(open(path, encoding='utf-8'))['effects']
assert all(n in fx for n, *_ in NEW) and fx['clear_before_the_lord_and_israel']['ledger_op'] == 'status'
print('effects: %d added (registry %d); the he found in the verse: %s' % (added, len(fx), HE_CLEAR))
# ---- the entities (append at the registry's end; the EOF branch — add_types_balak.py's form) ----
path = f"{ROOT}/logic/corpus/entity_registry.yaml"
text = open(path, encoding='utf-8').read()
reg = yaml.safe_load(text)
have_ids = {e['id'] for e in reg['entities']}
ENT = [
 ("the_sons_of_gad_and_reuben", "collective", "the sons of Gad and the sons of Reuben — THE INK'S COMPOUND PARTY at six seats (Num 32:2, 6, 25, 29, 31, 33; Gad first at every one — Reuben first at 32:1 alone): the askers of the land east (32:1-5), the offerers (32:16-19), the addressees of Moses' rebuke (32:6-15) and of THE DOUBLED CONDITION (32:20-24 — the debit to cross armed before the LORD until the land is subdued, OPEN to Joshua 22:1-9 outside the Torah; the build command closed at 32:34-38), the accepters (32:25-27, 31-32), the builders of the fourteen cities (32:34-38); the exam's exemplar of every condition (Mishnah Kiddushin 3:4); the registry's gad and reuben are JACOB'S SONS (Genesis 29:32, 30:11 — the persons), the tribes another party; the grant's three grantees are the_sons_of_gad, the_sons_of_reuben and the_half_tribe_of_manasseh (32:33)", "the-sons-of-gad-and-reuben"),
 ("the_sons_of_gad", "collective", "the sons of Gad — the tribe as one grantee of the land east (Num 32:33 'to the sons of Gad'), the builders of Dibon, Ataroth, Aroer, Atroth-shophan, Jazer, Jogbehah, Beth-nimrah and Beth-haran (32:34-36 — 'fortified cities and folds for sheep'); 'Dibon Gad' the itinerary's witness (33:45-46); Joshua 13:24-28 the allotment retold ('the border of the sons of Gad'), 22:1-9 the release; Deuteronomy 33:20-21 Gad's blessing ('the lawgiver's portion'); the registry's gad is Jacob's son (Genesis 30:11), the compound party the_sons_of_gad_and_reuben the stipulation's", "the-sons-of-gad"),
 ("the_sons_of_reuben", "collective", "the sons of Reuben — the tribe as one grantee of the land east (Num 32:33 'to the sons of Reuben'), the builders of Heshbon, Elealeh, Kiriathaim, Nebo, Baal-meon and Sibmah (32:37-38 — 'their names being changed'); Nebo in Reuben's portion Moses' grave (Sotah 13b:20; Onkelos 32:3 'the burial place of Moses'); Joshua 13:15-23 the allotment retold, 22:1-9 the release; Judges 5:15-16 'why did you sit among the sheepfolds' (observed); the registry's reuben is Jacob's firstborn (Genesis 29:32 — the person, demoted at 49:3-4), the compound party the_sons_of_gad_and_reuben the stipulation's", "the-sons-of-reuben"),
 ("the_half_tribe_of_manasseh", "collective", "the half tribe of Manasseh son of Joseph — FIRST NAMED AT THE GRANT (Num 32:33 'and to half the tribe of Manasseh son of Joseph'), no stipulation spoken to it in the chapter; its conquerors Machir's sons, Jair and Nobah (32:39-42); 34:14-15 'the half tribe of Manasseh' among the two and a half that received their inheritance beyond the Jordan; Deuteronomy 3:13-15, Joshua 1:12, 4:12, 13:29-31, 22:1-9 (the retellings and the release — the crossing extended to the three); Joshua 17:5-6's 'beside the land of Gilead and Bashan' (Bava Batra 118b:8); the phrase's nineteen seats; the second census's Manasseh 52,700 (26:34) halved in the two and a half's count", "the-half-tribe-of-manasseh"),
 ("the_dividers_of_the_land", "collective", "the dividers of the land — 'Eleazar the priest, and Joshua son of Nun, and the heads of the fathers of the tribes of the children of Israel' (Num 32:28 — the TRIAD Moses charged with the doubled condition's second form, 32:29-30), WORD FOR WORD Joshua 14:1's and 21:1's dividers ('these are the inheritances which ... Eleazar the priest and Joshua son of Nun and the heads of the fathers of the tribes of the children of Israel distributed'); 34:17-18 Eleazar and Joshua with a prince of every tribe the same office; the debit give_them_gilead_if_they_cross OPEN — its run Joshua 1:12-18 (Joshua's charge) and 22:1-9 (the release), outside the Torah; Bava Batra 122a:4's lottery (Eleazar with the Urim, Joshua and all Israel before him); the registry's the_court is Moses' court (Exodus 18) and the_heads_of_gilead 36:1's pleaders — other parties", "the-dividers-of-the-land"),
 ("jair_son_of_manasseh", "person", "Jair son of Manasseh — 'and Jair son of Manasseh went and took their villages, and called them Havvoth-jair' (Num 32:41); Deuteronomy 3:14 ('Jair son of Manasseh took all the region of Argob ... and called them after his own name, Havvoth-jair, to this day'), 1 Kings 4:13 ('Havvoth-jair son of Manasseh'), Joshua 13:30 ('all Havvoth-jair in Bashan, sixty cities'); THE INK'S SECOND LINEAGE — 1 Chronicles 2:21-22: Hezron of Judah took Machir's daughter and begot Segub, and Segub begot Jair, 'who had twenty-three cities in the land of Gilead'; the shelf: born in Jacob's days and did not die until the entry (Bava Batra 121b:9), 'about thirty-six' at Ai read as Jair alone (121b:10), already old at the decree (121b:11); THE HOMOGRAPH TRAPS: Jair the Gileadite judge with thirty sons and thirty cities 'called Havvoth-jair to this day' (Judges 10:3-5), Jair Mordecai's ancestor (Esther 2:5), Jair Elhanan's father (1 Chronicles 20:5)", "jair"),
 ("nobah", "person", "Nobah — 'and Nobah went and took Kenath and its daughters, and called it Nobah after his own name' (Num 32:42): his one seat as a person; Kenath's other seat 1 Chronicles 2:23 ('Geshur and Aram took Havvoth-jair from them, with Kenath and its daughters'); THE HOMOGRAPH TRAP: Nobah the place on Gideon's route against Midian, 'east of Nobah and Jogbehah' (Judges 8:11 — the two names' only other seat, Jogbehah Gad's city of 32:35)", "nobah"),
]
added_e = 0
for eid, kind, en, tok in ENT:
    if eid in have_ids: continue
    text = text.rstrip('\n') + '\n' + f"  - id: {eid}\n    en: {q(en)}\n    kind: {kind}\n    members:\n      - {{token: {tok}, units: [step9-scenes]}}   # cold_run_gad_reuben.py's narrative scene (THE NUMBERS WALK 12b, 2026-09-12); the frozen unit's tokens a later registry pass\n"
    added_e += 1
open(path, 'w', encoding='utf-8').write(text)
reg = yaml.safe_load(open(path, encoding='utf-8'))
assert all(e in {x['id'] for x in reg['entities']} for e, *_ in ENT)
print('entities: %d added of %d, registry %d' % (added_e, len(ENT), len(reg['entities'])))
# ---- the daemon block + the functions block (daemon_dispositions.yaml) ----
path = f"{ROOT}/World/step9/daemon_dispositions.yaml"
text = open(path, encoding='utf-8').read()
if '  law_gad_reuben:' not in text:
    block = '''  law_gad_reuben:
    file: cold_run_gad_reuben.py
    wraps: gad_reuben
    given_at: Num 32:20
    installed_by: boot   # THE NUMBERS WALK 12b (2026-09-12): A STIPULATION IN MOSES' VOICE WITH NO DIVINE FRAME — the chapter has no 'and the LORD spoke' in forty-two verses (the Numbers chapters without one: 22-24, 29, 30, 32, 36); the law the shelf reads from it is Moses' condition (32:20-24, 32:29-30 — 'from where do we learn the laws of all conditions? from the condition of the sons of Gad and Reuben', Gittin 75a:11) and the utterance rule's second seat (32:24 = 30:3); the parties call it 'that which the LORD has spoken to your servants' (32:31) and Joshua 22:9 'by the commandment of the LORD by the hand of Moses' — 30:2's CLASS (the vows' relay in Moses' voice, law_vows) at a second seat, beside 31:21's priest's relay (law_midian) and 36:6's relayed output (command_relayed); the installing acts are institution-erecting events on a `kind: institution` entity and Moses' stipulation erects none — the walk's standing setting; THE SECOND PASS (D2) decides whether a stipulation in Moses' voice is itself an installing act (COMPILE_DEBT.md's sitting-12b box)
    watches:
      land_requested: [plea_made]                                                    # 32:1-5: the request's STATUS on the compound party (Hobab's form — no close of its own)
      moses_rebuked_the_tribes: []                                                   # 32:6-15: NO WRITE — the oath retold is read against chapter 14's ledger (CG3)
      tribes_offered_to_arm: []                                                      # 32:16-19: NO WRITE — the utterance the rule binds at 32:24
      condition_stipulated: [commanded]                                              # 32:20-24: TWO DEBITS on the compound party — cross armed (OPEN to Joshua 22:1-9, outside the Torah) and build cities and folds (closed at 32:34-38); the vows' cell's own effect by CALL
      tribes_accepted_the_condition: []                                              # 32:25-27: NO WRITE — the seal on the parties' side
      commission_charged: [commanded]                                                # 32:28-30: the DEBIT on the dividers of the land — OPEN (Joshua 1:12-18, 22:1-9)
      tribes_answered_so_will_we_do: []                                              # 32:31-32: NO WRITE
      land_granted_east: [holding_given]                                             # 32:33: THREE TRANSFERS from Israel's possession by conquest to the three grantees
      cities_built_east: [cities_built]                                              # 32:34-38: the eight and the six as statuses; the build debit CLOSED by value (a close is no write)
      gilead_taken_by_machir: [land_possessed, holding_given]                        # 32:39-40: Gilead taken (the Amorite the counterparty) and given by Moses — the Genesis collective's second write
      villages_taken_by_jair: [land_possessed]                                       # 32:41: Havvoth-jair
      kenath_taken_by_nobah: [land_possessed]                                        # 32:42: Kenath and its daughters, called Nobah
      stipulation_case: [commanded, holding_given, accepted, exempt]                 # the exam's rows on the doubled condition and the law of conditions
      clearance_case: [clear_before_the_lord_and_israel, accepted, exempt]           # the exam's rows on 32:22 — the clerk, the bakers, the perfumers, the collectors
      oath_retold_case: [exempt, holding_owed, accepted]                             # the exam's rows on the oath retold — the exceptions, Caleb's Hebron, the set's edges
      land_east_case: [holding_given, land_possessed, accepted, exempt]              # the exam's rows on the grant, the cities and the conquerors
'''
    i = text.index('  law_zelophehad:')
    text = text[:i] + block + text[i:]
if '\n  gad_reuben:   # THE NUMBERS WALK 12b' not in text:
    fb = '''  gad_reuben:   # THE NUMBERS WALK 12b (2026-09-12)
    the_request: {status: WRAPPED, by: law_gad_reuben}
    the_rebuke: {status: WRAPPED, by: law_gad_reuben}
    the_offer: {status: WRAPPED, by: law_gad_reuben}
    the_condition: {status: WRAPPED, by: law_gad_reuben}
    the_acceptance_and_the_charge: {status: WRAPPED, by: law_gad_reuben}
    the_grant: {status: WRAPPED, by: law_gad_reuben}
    the_cities: {status: WRAPPED, by: law_gad_reuben}
    machir_jair_nobah: {status: WRAPPED, by: law_gad_reuben}
'''
    i = text.index('  midian:   # THE NUMBERS WALK 11b (2026-09-12)')
    j = text.index('\n  pre_sinai:', i)
    text = text[:j + 1] + fb + text[j + 1:]
open(path, 'w', encoding='utf-8').write(text)
dd = yaml.safe_load(open(path, encoding='utf-8'))
assert 'law_gad_reuben' in dd['daemons'] and 'gad_reuben' in dd['functions'], (list(dd)[:5])
print('daemons: %d (law_gad_reuben %s); functions blocks: %d' % (len(dd['daemons']), 'law_gad_reuben' in dd['daemons'], len(dd['functions'])))
# ---- the dependency span + edges (the POINTERS after the gate's print) ----
path = f"{ROOT}/World/step9/dependency_dispositions.yaml"
text = open(path, encoding='utf-8').read()
if '\n  gad_reuben:' not in text.split('\nedges:')[0]:
    a = "  midian:      [[Num, 31, 1, 54]]"
    i = text.index(a); j = text.index('\n', i)
    text = text[:j + 1] + "  gad_reuben:  [[Num, 32, 1, 42]]   # THE NUMBERS WALK 12b (2026-09-12; NUMBERS_WALK.md \"Sitting 12b\"): Gad and Reuben — the request, the oath retold, the doubled condition and the utterance rule, the commission, the grant east, the cities, Machir, Jair and Nobah\n" + text[j + 1:]
    edges = '''  - {from: gad_reuben, to: vows, disposition: CALL, link: reference, carries: verdict,
     why: "THE NUMBERS WALK 12b (2026-09-12) | 32:24's 'THAT WHICH HAS GONE OUT OF YOUR MOUTH YOU SHALL DO' is 30:3's 'all that goes out of his mouth he shall do' — the phrase's two Bible seats (the same three lemmas; Onkelos renders both in one Aramaic): THE UTTERANCE RULE'S SECOND SEAT, the ink naming the rule — VW.the_man({'ask': 'all_that_proceeds'}) CALLED, its own effect commanded the debit's (10b's filed seat 'Num 32:24 forward' PAID); 32:7's 'discourage the heart' the vows' hinder-root (30:6-12 — the six Torah tokens all in 30 and 32) the shared token"}
  - {from: gad_reuben, to: shelach, disposition: CALL, link: reference, carries: verdict,
     why: "THE NUMBERS WALK 12b (2026-09-12) | 32:8-13 RETELLS 13:2-14:35 in the oath's own words — 'from Kadesh-barnea', 'the valley of Eshcol', 'from twenty years old and upward' (14:29), 'save Caleb son of Jephunneh and Joshua son of Nun', 'followed the LORD fully' (14:24), 'forty years' (14:33-34), 'until all the generation was consumed': SL.decree('set' / 'exceptions' / 'due' / 'count_from' / 'day_for_year' / 'caleb_entitlement' / 'deaths_ceased' / 'pardon') and SL.spies('joshua_name' / 'joshua_caleb_equal' / 'send_for_yourself' / 'eshcol' / 'hebron_visitor') CALLED — the shared tokens the reference; the checkpoint CG3 reads the shelach daemon's entries and the forty years' timer's fire off the running world"}
  - {from: gad_reuben, to: chukat, disposition: CALL, link: reference, carries: verdict,
     why: "THE NUMBERS WALK 12b (2026-09-12) | 32:33's 'the kingdom of Sihon king of the Amorite and the kingdom of Og king of Bashan' names 21:21-35's conquests (the chukat runner's land_possessed on israel_people at 21:24-25, 21:31-32, 21:35 — THE GRANT'S SOURCE ON THE LEDGER); 32:1 and 32:35's Jazer 21:32's; 32:42's 'its daughters' 21:25 and 21:32's word; 32:39's 'dispossessed the Amorite' 21:32's verb: CK.well_and_kings('land_east' / 'deut3_delta' / 'og_lore' / 'sihon_purified' / 'spy_verb') CALLED — the shared tokens the reference"}
  - {from: gad_reuben, to: second_census, disposition: CALL, link: reference, carries: verdict,
     why: "THE NUMBERS WALK 12b (2026-09-12) | the two and a half's count is the second census's own rows — Reuben 43,730 (26:7), Gad 40,500 (26:18), Manasseh 52,700 (26:34) — read off the population table (world.population(grain='counted', family=None), the second census runner's form) and C2.the_roll('total') / C2.the_land('by_lot' / 'thirteen_tribes' / 'ten_parts' / 'morasha') CALLED; 32:11's 'from twenty years old and upward' 26:2's formula; 32:39's 'Machir son of Manasseh' 26:29's family; the lot's division of Canaan (26:52-56, the OPEN commanded divide_the_land) is NOT this chapter's grant (the east by Moses' word, Bava Batra 118b:8's 'beside the land of Gilead and Bashan')"}
  - {from: gad_reuben, to: bamidbar, disposition: CALL, link: reference, carries: verdict,
     why: "THE NUMBERS WALK 12b (2026-09-12) | 32:11's 'from twenty years old and upward' is 1:3's census formula (the twenty-three seats — Exodus 30:14, Numbers 1:3, 26:2 among them): BM.census('threshold' / 'orders') CALLED — the shared tokens the reference; 'Gad moves from eleventh to third' in the camps (the bamidbar runner's own note on the tribe's order)"}
  - {from: sequence, to: gad_reuben, disposition: CALL, link: none,
     why: "THE NUMBERS WALK 12b (2026-09-12) | the sequential run's REGISTRATION edge — ('cold_run_gad_reuben', 'law_gad_reuben') in DAEMON_ORDER (the runner compiles no verse: link none, O4's license)"}
'''
    a = "  - {from: sequence, to: midian, disposition: CALL, link: none,"
    i = text.index(a); j = text.index('\n', text.index('why:', i)) + 1
    text = text[:j] + edges + text[j:]
    open(path, 'w', encoding='utf-8').write(text)
dep = yaml.safe_load(open(path, encoding='utf-8'))
assert 'gad_reuben' in dep['spans']
print('dependency: span + 6 edges (gad_reuben); the pointers after the gate\'s print')
# ---- the installation probe's count ----
path = f"{ROOT}/World/step9/installation_probes.py"
text = open(path, encoding='utf-8').read()
a = "len(real) == 58 and all('given_at' in d and 'installed_by' in d for d in real.values())   # THE NUMBERS WALK 11b (2026-09-12): 57 -> 58, law_midian"
if a in text:
    text = text.replace(a, "len(real) == 59 and all('given_at' in d and 'installed_by' in d for d in real.values())   # THE NUMBERS WALK 12b (2026-09-12): 58 -> 59, law_gad_reuben (installed_by boot — a stipulation in Moses' voice with no divine frame, 30:2's class named); 11b: 57 -> 58, law_midian")
    open(path, 'w', encoding='utf-8').write(text)
assert "len(real) == 59" in open(path, encoding='utf-8').read()
print('installation_probes I5: 59')
