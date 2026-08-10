#!/usr/bin/env python3
"""Author exo_21_the_ordinances (Exod 21:1-37) — forward-era unit #35 (run FWD-8 block 5).
Run from repo root."""
import sys, sqlite3
sys.path.insert(0, "<scratch>")
import unitgen

db = sqlite3.connect(unitgen.DB)

def hp(ch, vs, idx, book="Exod"):
    return db.execute("SELECT w.he_plain FROM words w JOIN verses v ON w.verse_id=v.id "
                      "WHERE v.book=? AND v.chapter=? AND v.verse=? AND w.idx=?",
                      (book, ch, vs, idx)).fetchone()[0].replace("/", "")

def census(sp):
    return db.execute("""SELECT v.book, v.chapter, v.verse FROM words w
        JOIN verses v ON w.verse_id=v.id
        WHERE replace(w.he_plain,'/','')=? ORDER BY v.book, v.chapter, v.verse""",
        (sp,)).fetchall()

def vlen(ch, vs):
    return db.execute("SELECT COUNT(*) FROM words w JOIN verses v ON w.verse_id=v.id "
                      "WHERE v.book='Exod' AND v.chapter=? AND v.verse=?", (ch, vs)).fetchone()[0]

# ---- build-time machine evidence (asserted, not crowns) -------------------
assert (hp(21, 8, 5), hp(21, 8, 6)) == ("לא", "לו")                             # the alef/vav qere, adjacent tokens
assert "".join(hp(21, 1, i)[-1] for i in range(4)) == "הםרם"                    # the header's finals (the fraud-letters)
assert vlen(21, 1) == 5                                                        # five words at the code's door
assert (hp(21, 19, 0)[0], hp(21, 19, 12)[-1]) == ("א", "א")                     # the healing-verse's alef brackets
assert (hp(21, 21, 0)[0], hp(21, 21, 10)[-1]) == ("א", "א")                     # the day-or-two brackets
assert (hp(21, 26, 0)[0], hp(21, 26, 14)[-1]) == ("ו", "ו")                     # the eye-verse's vav brackets
assert (hp(21, 27, 0)[0], hp(21, 27, 10)[-1]) == ("ו", "ו")                     # the tooth-verse's vav brackets
assert vlen(21, 26) + vlen(21, 27) == 26                                       # the twenty-six words / limbs
assert census("יזיד") == [("Deut", 18, 20)]                                    # the full presumption (the prophet)
assert census("בערמה") == [("Exod", 21, 14)]                                   # the scheme, unique
assert census("כצאת") == [("Exod", 21, 7), ("Exod", 33, 8)]                     # the two goings-out
assert census("נגח") == [("Exod", 21, 29), ("Exod", 21, 36)]                    # the goring pair, in-span
assert census("מתמול") == [("Deut", 4, 42), ("Deut", 19, 6), ("Exod", 4, 10), ("Exod", 21, 36)]  # the full yesterdays
assert census("וענתה") == [("Deut", 25, 9), ("Deut", 31, 21), ("Exod", 21, 10), ("Gen", 30, 33)]  # the answer-skeleton's four
assert census("באגרף") == [("Exod", 21, 18)]                                   # the fist, unique
G = {"א":1,"ב":2,"ג":3,"ד":4,"ה":5,"ו":6,"ז":7,"ח":8,"ט":9,"י":10,"כ":20,"ך":20,
     "ל":30,"מ":40,"ם":40,"נ":50,"ן":50,"ס":60,"ע":70,"פ":80,"ף":80,"צ":90,"ץ":90,
     "ק":100,"ר":200,"ש":300,"ת":400}
g = lambda s: sum(G[c] for c in s if c in G)
assert g("מרצע") == 400                                                        # the awl = the four hundred years
assert g("ולא") + g("יאכל") == g("ולא") + g("הנאה") == 98                       # no eating = no benefit

P = "PRECONDITION_STATE"
C = "CASE"
H = "HANDLER"
S = "STATUTE"

def v(op, en, left, right, comment, ops):
    return dict(op=op, en=en, left_en=left, right_en=right, comment=comment, operators=ops)

def p(expr, span, prose):
    return dict(op=P, expr_en=expr, he_span=span, prose=prose)

def c_(expr, span, prose):
    return dict(op=C, expr_en=expr, he_span=span, prose=prose)

def h_(expr, span, prose):
    return dict(op=H, expr_en=expr, he_span=span, prose=prose)

def s_(expr, span, prose):
    return dict(op=S, expr_en=expr, he_span=span, prose=prose)

V = {}
V[1] = v("AND_THESE_ARE_THE_ORDINANCES", "And these are the ordinances which you shall set before them.",
  "and these are the ordinances", "which you shall set before them",
  "The code's door; the fraud-finals.",
  [p("HOLDS(ve_ele_ha_mishpatim, t0)", (0,4),
    "THE HEADER [EX21-01 CROWN]. VE-ELE ha-MISHPATIM — 'AND THESE are the ordinances': the vav of continuity (the readings: as the former from Sinai, so these from Sinai — the civil code joined to the Decalogue by one letter); asher TASIM lifnehem — 'which you shall SET BEFORE THEM' (set like a laid table, the readings named-only); and the header's four words END IN THE LETTERS OF MIRMA, fraud (VERIFIED final-letters): 'if a FRAUDULENT CASE comes before the judge, let him probe it to its truth' — the code's title warning its own bench; FIVE words (asserted): the true judge as upholder of the five books and partner in creation (18:13's He-He doctrine at the code's door); the Kitzur's acronym-duties named (probe the case; offer compromise first; if both parties will): the machine notes the addressees: lifnehem — BEFORE THEM, the judges of 18's pyramid: the courts Jethro drew now get their statute-book.")])
V[2] = v("THE_HEBREW_SLAVE", "When you acquire a Hebrew slave, six years he shall serve; and in the seventh he shall go out free, for nothing.",
  "when you acquire a Hebrew slave, six years he shall serve", "and in the seventh he shall go out free, for nothing",
  "The code opens with release.",
  [c_("CASE(ki tiqne eved ivri) ROUTE(eved_ivri)", (0,3),
    "THE FIRST CASE. ki tiqne EVED IVRI — 'when you acquire a HEBREW SLAVE': the case-opener installed (the ki-filter of the law-genre: the code's first word of substance is SLAVE — the machine files the order as doctrine: a nation of freed slaves legislates slavery FIRST, and legislates it as a countdown); SHESH shanim yaavod u-va-SHEVIIT yetze la-CHOFSHI CHINAM — 'six years he shall serve, and in the SEVENTH he goes out FREE, FOR NOTHING': the six-and-one frame's third appearance (creation's week, the manna's week, now the SLAVE'S week — the Sabbath-shape scaled to years: the machine wires 20:9-11's frame onto a human term of service); the shin of u-va-sheviit under the guard-stroke (MS, named).")])
V[3] = v("AS_HE_CAME", "If he came in by himself, he shall go out by himself; if he was the husband of a wife, then his wife shall go out with him.",
  "if he came in by himself, he shall go out by himself", "if he was the husband of a wife, then his wife shall go out with him",
  "The exit mirrors the entry.",
  [p("HOLDS(be_gapo_yavo_be_gapo_yetze, t0)", (0,4),
    "THE MIRROR. im-be-GAPO yavo be-GAPO yetze — 'by HIMSELF in, by HIMSELF out' (the rare gap-word doubled: the term of service may not subtract a man's family state); im-BAAL ISHA hu VE-YATZA ishto imo — 'his wife goes out WITH HIM': the exit-verb's first station of the chapter (the corpus's exit-file opens: VE-YATZA — the machine arms 21:11's crown: the three Torah she-went-outs are all women leaving a man's house, and the first is a wife leaving WITH her man): the readings on the master's duty to feed her meanwhile, named-only.")])
V[4] = v("THE_MASTERS_WIFE", "If his master gives him a wife, and she bears him sons or daughters — the wife and her children shall be her master's, and he shall go out by himself.",
  "if his master gives him a wife, and she bears him sons or daughters", "the wife and her children shall be her master's, and he shall go out by himself",
  "The split household.",
  [p("HOLDS(ha_isha_vi_yladeha_tihye_la_adoneha, t0)", (10,16),
    "THE SPLIT. im-ADONAV yiten-lo ISHA — 'if his MASTER gives him a wife' (the Canaanite bondwoman, the readings); ha-isha vi-YLADEHA tihye la-ADONEHA — 'the wife and her children shall be HER MASTER'S, and he goes out by himself': the machine files the case's hard edge without softening it (the readings' law: the master-given union ends with the term — the lean record keeps the verse's own severity), and notes what the NEXT verse does with it: the law immediately stages the man who refuses this arithmetic — the code writes its own exception before the ink dries.")])
V[5] = v("I_LOVE_MY_MASTER", "And if the slave shall plainly say: I love my master, my wife, and my sons — I will not go out free.",
  "and if the slave shall plainly say: I love my master, my wife, and my sons", "I will not go out free",
  "The refusal of freedom.",
  [p("HOLDS(ahavti_et_adoni, t0)", (1,10),
    "THE DECLARATION. ve-im-AMOR YOMAR ha-eved — 'if the slave shall PLAINLY SAY' (the doubled saying: the readings' law — said and said again, once and once more at the term's edge); AHAVTI et-ADONI et-ISHTI ve-et-BANAI — 'I LOVE my master, my wife, and my sons': the love-verb's strangest deployment in the corpus (the machine notes the inventory: master first, then wife, then sons — the declaration lists its loves in the order the LAW created them); LO ETZE CHOFSHI — 'I will NOT go out free': the corpus's first recorded REFUSAL OF FREEDOM (8:22's refusal was Moses refusing Pharaoh's grant; this is a man refusing the code's own gift — the readings' verdict arms the next verse's awl).")])
V[6] = v("THE_AWL_AND_THE_DOOR", "Then his master shall bring him to God, and bring him to the door, or to the doorpost; and his master shall pierce his ear with the awl — and he shall serve him forever.",
  "then his master shall bring him to God, and bring him to the door, or to the doorpost", "and his master shall pierce his ear with the awl — and he shall serve him forever",
  "The handler; the awl's four hundred.",
  [h_("HANDLER IF(amor yomar ha-eved ahavti) THEN(ve-ratza et-azno ba-martzea, va-avado le-olam)", (10,16),
    "THE PROCEDURE [EX21-02 CROWN]. ve-higisho adonav el-ha-ELOHIM — 'to GOD' (the judges, the readings — the refusal must pass the bench); ve-higisho el-ha-DELET o el-ha-MEZUZA — 'to the DOOR or the doorpost': the Kitzur — 'let him guard his master's house' (the threshold as the sentence); ve-RATZA adonav et-AZNO ba-MARTZEA — 'and pierce his EAR with the AWL': and MARTZEA = 400, EXACT (VERIFIED at the build) — 'the Name redeemed us after FOUR HUNDRED YEARS of bondage, and this man went and enslaved himself: let him be pierced by the awl of four hundred' (Gen 15:13's number driven through the ear that chose new servitude; the ear that heard at Sinai, the readings); va-avado LE-OLAM — 'FOREVER' written LEAN (to the jubilee, the readings — the machine notes the letter-scale justice: 19:9's faith and ban got the FULL forevers; servitude gets the thinned one).")])
V[7] = v("THE_DAUGHTER_SOLD", "And when a man sells his daughter as a maidservant, she shall not go out as the slaves go out.",
  "and when a man sells his daughter as a maidservant", "she shall not go out as the slaves go out",
  "The second case.",
  [c_("CASE(ve-khi yimkor ish et bito le-ama) ROUTE(ama_ivriya)", (0,5),
    "THE SECOND CASE [EX21-05]. ve-khi-YIMKOR ish et-BITO le-AMA — 'when a man sells HIS DAUGHTER as a maidservant': the case installed (the poverty-sale, the readings — the code regulates what it does not praise); LO TETZE ke-TZET ha-avadim — 'she shall NOT go out AS THE SLAVES go out': the going-out word's Torah-pair (asserted at the build): the maid's exit and MOSES' going out to the tent (33:8) — the Kitzur's sun-twin named ('the face of Moses like the face of the sun... as the sun goes out in its might'): her exit is NOT the slaves' — the machine notes the code's method: the girl's protections will be stated as a ladder of exits (designation, redemption, or free), each one guarded.")])
V[8] = v("THE_QERE_OF_MERCY", "If she is bad in the eyes of her master, who has not designated her — then he shall let her be redeemed; to a foreign people he shall not rule to sell her, since he has dealt treacherously with her.",
  "if she is bad in the eyes of her master, who has not designated her — then he shall let her be redeemed", "to a foreign people he shall not rule to sell her, since he has dealt treacherously with her",
  "The alef read as vav; the garment pair.",
  [p("HOLDS(ve_hefda, t0)", (4,8),
    "THE MERCY-QERE [EX21-03 + EX21-04 CROWNS]. asher-LO yeada — WRITTEN 'who has NOT designated her' (alef), READ 'who has designated her FOR HIMSELF' (vav): one of the Torah's THREE alef-written-vav-read words (VERIFIED adjacent-token pair at the build; the Shemini roster: the locust's legs, the walled city) — 'and all three come for exposition': HE OUGHT TO HAVE DESIGNATED HER — 'the duty of designation precedes the duty of redemption' (Onkelos): the law's mercy voiced out of its own negation; ve-HEFDA — 'he shall let her be REDEEMED'; le-am NAKHRI lo-yimshol le-makhra BE-VIGDO bah — 'to a FOREIGN people he shall not sell her, since he has DEALT TREACHEROUSLY with her': and the garment-betrayal word's Torah-pair (VERIFIED): this master and POTIPHAR'S WIFE ('she seized him BY HIS GARMENT,' Gen 39:12) — Rabbi Eliezer: the spread garment forbids the sale; Rabbi Aqiva: the betrayal does ('for THERE TOO was betrayal'): cloth and treason one skeleton, the maid's law and Joseph's trial reading each other.")])
V[9] = v("AS_THE_DAUGHTERS", "And if he designates her for his son — according to the ordinance of the daughters he shall do for her.",
  "and if he designates her for his son", "according to the ordinance of the daughters he shall do for her",
  "The daughter-standard.",
  [p("HOLDS(ke_mishpat_ha_banot, t0)", (3,6),
    "THE STANDARD. ve-im-li-VENO yiadena — 'if he designates her FOR HIS SON'; ke-MISHPAT ha-BANOT yaase-lah — 'according to the ORDINANCE OF THE DAUGHTERS he shall do for her': the code's title-word (mishpatim) makes its first in-span return — and it returns to protect a purchased girl with a FREE DAUGHTER'S standard (the machine files the equation: the ama designated to the son is re-classed OUT of the property rules into family law — the readings on food, clothing, and season, arming the next verse).")])
V[10] = v("HER_THREE_RIGHTS", "If he takes himself another — her flesh, her covering, and her season he shall not diminish.",
  "if he takes himself another", "her flesh, her covering, and her season he shall not diminish",
  "The three duties; the lean season.",
  [p("HOLDS(sheera_kesuta_ve_onata, t0)", (4,8),
    "THE THREE [EX21-05]. im-ACHERET yiqach-lo — 'if he takes ANOTHER'; SHEERA KESUTA VE-ONATA lo yigra — 'her FLESH (food), her COVERING, and her SEASON he shall not DIMINISH': the corpus's first marital-duty triple (the three rights the tradition reads onto every wife from the maidservant's case — the a-fortiori the readings draw, named-only); and VE-ONATA written LEAN (the answer-skeleton's four stations asserted at the build: Jacob's testifying righteousness, the chalitza's answer, the song's testimony — and this, the only conjugal one): the Kitzur on the missing letter: 'the ESSENTIAL season is the SABBATH, not the six weekdays' — the law of tenderness carried by a lean spelling.")])
V[11] = v("OUT_FREE_WITHOUT_MONEY", "And if these three he does not do for her — then she shall go out for nothing, without money.",
  "and if these three he does not do for her", "then she shall go out for nothing, without money",
  "The handler; the three women's exits.",
  [h_("HANDLER IF(shelash ele lo yaase lah) THEN(ve-yatza chinam en kasef)", (6,9),
    "THE RELEASE [EX21-05 CROWN]. ve-im-SHELASH-ELE lo yaase lah — 'if these THREE he does not do' (the clipped qamatz under the binder, MS named); VE-YATZA CHINAM EN KASEF — 'she shall GO OUT for nothing, WITHOUT MONEY': the handler installed — and the she-went-out verb's Torah-census is exactly THREE (VERIFIED), ALL WOMEN LEAVING A MAN'S HOUSE: the slave's WIFE with him (21:3), the MAIDSERVANT free here, and the DIVORCEE (Deut 24:2) — the Kitzur's likeness sealed by the pair: 'the maid is likened to the wife — as the wife by document, so the maid' (one exit-verb walking the corpus's three doors); en KASEF — the Kitzur's juxtaposition named (no-money beside the death-law: the greater penalty swallows the payment): the girl's ladder tops out at free.")])
V[12] = v("THE_STRIKER_OF_MAN", "He who strikes a man, and he dies — shall surely be put to death.",
  "he who strikes a man, and he dies", "shall surely be put to death",
  "The first capital statute.",
  [s_("STATUTE FORBID(makkeh_ish)", (0,4),
    "THE CAPITAL CODE OPENS. MAKKE ISH va-MET, MOT YUMAT — 'he who STRIKES A MAN, and he dies — shall SURELY BE PUT TO DEATH': the participial statute (the apodictic form inside the casuistic code: no ki, no if — a standing description of a doomed man: the machine notes the grammar-shift the law-genre makes for murder); the death-doubling MOT YUMAT (16:29's court-file armed at exo_16 now in its home genre); the readings on witnesses and warning, named-only: the corpus installs the statute bare, as the verse does.")])
V[13] = v("THE_PLACE_TO_FLEE", "And he who did not lie in wait, but God caused it to come to his hand — I will set for you a place where he may flee.",
  "and he who did not lie in wait, but God caused it to come to his hand", "I will set for you a place where he may flee",
  "The refuge handler.",
  [h_("HANDLER IF(lo tzada, ve-ha-elohim ina le-yado) THEN(ve-samti lekha maqom asher yanus shama)", (6,11),
    "THE REFUGE. va-asher LO TZADA — 'who did NOT lie in wait' — ve-ha-ELOHIM INA le-yado — 'but GOD caused it to come to his hand': the corpus's boldest theology of accident (the unintended death assigned to the Hand behind hands — the readings' two-hotels doctrine, named-only); VE-SAMTI lekha MAQOM asher YANUS shama — 'I will SET for you a PLACE where he may FLEE': the handler installed — the CITY-OF-REFUGE law in seed (Num 35 and Deut 19 armed; the Kitzur's boundary-gematria named as the tradition's device): the machine notes the speaker-shift: the I of the code (ve-samti) — the refuge is the one institution in the chapter God builds Himself.")])
V[14] = v("FROM_MY_ALTAR", "And when a man presumes against his fellow, to kill him by scheme — from My altar you shall take him, to die.",
  "and when a man presumes against his fellow, to kill him by scheme", "from My altar you shall take him, to die",
  "The two presumptions; no asylum.",
  [h_("HANDLER IF(yazid ish al reehu le-horgo ve-arma) THEN(me-im mizbechi tiqachenu la-mut)", (7,10),
    "NO ASYLUM [EX21-06 CROWN]. ve-khi-YAZID ish al-reehu — 'when a man PRESUMES against his fellow': the presume-verb LEAN here and FULL at the FALSE PROPHET (VERIFIED: the Torah's only other station, Deut 18:20's yazid — MS: 'one lean, one full'; the Kitzur: 'the prophet who presumes is AS ONE WHO MURDERS' — the scheming killer and the lying prophet one verb, two spellings); le-horgo VE-ARMA — 'by SCHEME': Torah-unique (VERIFIED at the build) — the GIBEONITES its Scripture-twin: 'this one schemed to kill and was taken FROM MY ALTAR to die; those schemed to join and were brought TO the altar' (one cunning-word, the altar refusing and receiving); me-im MIZBECHI tiqachenu LA-MUT — 'from MY ALTAR you shall take him': the handler installed — sanctity is no shield for the deliberate (the readings: even a priest mid-service; Joab at the horns armed, named-only).")])
V[15] = v("THE_STRIKER_OF_PARENTS", "And he who strikes his father and his mother shall surely be put to death.",
  "and he who strikes his father and his mother", "shall surely be put to death",
  "The second capital statute.",
  [s_("STATUTE FORBID(makkeh_aviv_ve_imo)", (0,4),
    "THE PARENT-STRIKER. u-MAKKE AVIV ve-IMO, MOT YUMAT — 'he who STRIKES his father and his mother shall surely die': the second participial statute — the fifth utterance's dark mirror (20:12 commanded the honoring; 21:15 prices the striking: the machine wires the Decalogue to its case-law across one chapter); the readings' wound-requirement, named-only; and the placement noted: the parent-striker stands between the man-striker and the man-stealer — the code files violence against parents WITH the capital violences, not with the property wrongs.")])
V[16] = v("THE_MAN_STEALER", "And he who steals a man, and sells him, and he is found in his hand — shall surely be put to death.",
  "and he who steals a man, and sells him, and he is found in his hand", "shall surely be put to death",
  "The third capital statute.",
  [s_("STATUTE FORBID(gonev_ish)", (0,4),
    "THE KIDNAPPER. ve-GONEV ISH u-mekharo ve-nimtza ve-yado, MOT YUMAT — 'he who STEALS A MAN, and sells him... shall surely die': the third participial statute — and the eighth utterance's referent by the tradition's own count (20:15's two-word lo-tignov read here: THE THEFT AMONG THE TEN IS THIS ONE, the capital theft — the Kitzur's cipher at the Decalogue named): the machine notes the code's hierarchy made explicit: stealing PROPERTY ends this chapter in repayment (21:37); stealing a PERSON stands here among the death-laws — the corpus prices a man as the one thing that cannot be restituted.")])
V[17] = v("THE_CURSER_OF_PARENTS", "And he who curses his father and his mother shall surely be put to death.",
  "and he who curses his father and his mother", "shall surely be put to death",
  "The fourth capital statute; the head and the tail.",
  [s_("STATUTE FORBID(meqalel_aviv_ve_imo)", (0,4),
    "THE CURSER [EX21-13 CROWN]. u-MEQALEL AVIV ve-imo, MOT YUMAT — 'he who CURSES his father and his mother shall surely die': the fourth participial statute — and the curser-word's only Torah station (VERIFIED), standing at its VERSE'S HEAD while its Scripture-twin (SHIMI cursing David) closes its own verse: the Kitzur — 'the curser WAS HEAD of the Sanhedrin AND BECAME THE TAIL' (the word's two placements as the curser's career); the machine files the pair 21:15/21:17 as the code's own commentary: the STRIKE and the CURSE of parents carry one sentence — the hand and the mouth weighed equal at the family's root (the readings on the curse's stone-penalty cipher named).")])
V[18] = v("THE_BRAWL", "And when men quarrel, and a man strikes his fellow with a stone or with a fist, and he does not die, but falls to bed —",
  "and when men quarrel, and a man strikes his fellow with a stone or with a fist", "and he does not die, but falls to bed",
  "The injury case.",
  [c_("CASE(ve-khi yerivun anashim ve-hika ish et reehu) ROUTE(makkeh_reehu)", (0,6),
    "THE THIRD CASE. ve-khi-YERIVUN anashim — 'when men QUARREL' (17:2's quarrel-verb domesticated: Massah's riv against Heaven becomes the street-brawl the courts inherit); ve-hika ish et-reehu be-EVEN o ve-EGROF — 'with a STONE or with a FIST': the fist-word Torah-unique (VERIFIED at the build) — Isaiah's 'fist of wickedness' its Scripture-twin (the Kitzur: the blow must carry killing-force — the fist that jails its owner); ve-lo yamut ve-nafal le-MISHKAV — 'and he does not die, but falls TO BED': the case installed — the corpus's first NON-FATAL violence law (until now the code priced death; here it learns to price a lost week).")])
V[19] = v("THE_HEALING_LICENSE", "If he rises, and walks outside on his staff, then the striker shall be cleared; only his sitting he shall give — and he shall surely heal.",
  "if he rises, and walks outside on his staff, then the striker shall be cleared", "only his sitting he shall give — and he shall surely heal",
  "The handler; the physician's charter.",
  [h_("HANDLER IF(yaqum ve-hithalekh ba-chutz al mishanto) THEN(ve-niqa ha-makke, shivto yiten ve-rapo yerape)", (8,12),
    "THE LICENSE [EX21-07 CROWN]. im-YAQUM ve-hithalekh ba-chutz al-MISHANTO — 'if he rises and walks outside ON HIS STAFF' (on his own strength, the readings); ve-NIQA ha-makke — 'the striker is CLEARED' (the Kitzur's three amnesties named: 'THREE are forgiven all their sins — the sick man who recovered, the bridegroom, and the king'); raq SHIVTO yiten — his idleness paid ('excluding the patient who defied the physician,' the Kitzur's rider); VE-RAPO YERAPE — 'and he shall SURELY HEAL': the heal-word's ONLY Torah station in this form (VERIFIED) — the tradition's charter: FROM HERE, PERMISSION IS GRANTED TO THE PHYSICIAN TO HEAL (the corpus's two healing-grants: Marah's 'I am the LORD your Healer' and this human license — the machine closes exo_15's arm: the Healer's title did not retire the doctor; it commissioned him); and the verse runs ALEF TO ALEF (VERIFIED brackets): 'sufferings are sent WITH A DECREE — to such a day, to such an hour' (the sickness bracketed like its verse).")])
V[20] = v("THE_STRUCK_SLAVE", "And when a man strikes his slave or his maidservant with the rod, and he dies under his hand — he shall surely be avenged.",
  "and when a man strikes his slave or his maidservant with the rod, and he dies under his hand", "he shall surely be avenged",
  "The slave's blood counts.",
  [c_("CASE(ve-khi yake ish et avdo o et amato ba-shevet u-met) ROUTE(makkeh_avdo)", (0,11),
    "THE FOURTH CASE. ve-khi-YAKE ish et-AVDO o et-AMATO ba-SHEVET u-MET tachat yado — 'when a man strikes his SLAVE or his MAIDSERVANT with the rod, and he dies UNDER HIS HAND': the case installed — NAQOM YINAQEM, 'he shall surely be AVENGED': the machine files the legal revolution at its size: the Canaanite slave's death is AVENGED (the vengeance-doubling the code's strongest for a servant — the readings: death by the sword; the corpus notes the ancient world's silence this verse breaks: the master is not the owner of the breath).")])
V[21] = v("A_DAY_OR_TWO_DAYS", "But if he stand a day or two days, he shall not be avenged — for he is his money.",
  "but if he stand a day or two days, he shall not be avenged", "for he is his money",
  "The handler; the Cain-skeleton.",
  [h_("HANDLER IF(yom o yomayim yaamod) THEN(lo yuqam, ki khaspo hu)", (5,10),
    "THE EXCEPTION [EX21-08 CROWN]. akh im-YOM o YOMAYIM yaamod — 'but if he STAND a day or two days' — LO YUQAM ki KHASPO hu — 'he shall NOT BE AVENGED, for he is his money': the handler installed — and the avenge-skeleton's Torah-census is FOUR (VERIFIED): CAIN ('sevenfold shall he be AVENGED,' Gen 4:15), LAMECH ('seventy-seven,' 4:24), the struck slave here — the vengeance-verb born at the first murder, regulated at the slave-law (the Kitzur wiring Eve's qaniti into ki-khaspo: the acquired man) — with ESAU's let-my-father-ARISE the skeleton's fourth face (Gen 27:31, the rise-verb sharing the letters, named); and the verse runs ALEF TO ALEF (VERIFIED): 'he must live A FULL CYCLE, from time to time' (the Kitzur — the day-or-two bracketed like the healing-verse); the machine holds the hard verse at its surface, lean-record: the exception is the verse's, and the tradition's boundaries on it are named-only.")])
V[22] = v("THE_STRUCK_MOTHER", "And when men fight, and strike a pregnant woman, and her children go out, and there is no harm — he shall surely be fined, as the woman's husband lays on him, and he shall give by the judges.",
  "and when men fight, and strike a pregnant woman, and her children go out, and there is no harm", "he shall surely be fined, as the woman's husband lays on him, and he shall give by the judges",
  "The unborn priced.",
  [c_("CASE(ve-khi yinatzu anashim ve-nagfu isha hara ve-yatzu yeladeha) ROUTE(ason_o_lo)", (0,10),
    "THE FIFTH CASE. ve-khi-YINATZU anashim — 'when men FIGHT' (the Kitzur's pair named: this fight and Deut 25:11's — 'as there, money; so here, money': the two brawl-verses one rule); ve-nagfu ISHA HARA ve-yatzu YELADEHA — 'and strike a PREGNANT woman, and her children GO OUT' — ve-lo yihye ASON — 'and there is NO HARM': the case installed on its fork (ason or no ason — the readings' entire jurisprudence of the unborn hangs on this word, named-only); ANOSH YEANESH — 'he shall surely be FINED' (the fine-word FULL against the Jerusalem exemplar's lean — MS with the Ramah); ve-natan BI-FELILIM — 'by the JUDGES' (lean-then-full, the exemplars split — MS): the miscarried pregnancy priced by the bench, not the street.")])
V[23] = v("LIFE_FOR_LIFE", "And if there is harm — then you shall give life for life.",
  "and if there is harm", "then you shall give life for life",
  "The talion's head.",
  [h_("HANDLER IF(ason yihye) THEN(ve-natata nefesh tachat nafesh)", (3,6),
    "THE HARM-FORK. ve-im-ASON yihye — 'and if there IS harm' — ve-natata NEFESH TACHAT NAFESH — 'you shall give LIFE FOR LIFE': the handler installed — the tachat-formula's first rung (the machine notes the grammar the tradition reads: VE-NATATA, you shall GIVE — the talion spoken in the currency-verb: the giving-word that carries payment everywhere else in the code carries this clause too; the readings' monetary reading rides the verb itself, named prominently as the tradition's law).")])
V[24] = v("EYE_FOR_EYE", "Eye for eye, tooth for tooth, hand for hand, foot for foot,",
  "eye for eye, tooth for tooth", "hand for hand, foot for foot",
  "The talion table.",
  [p("HOLDS(ayin_tachat_ayin, t0)", (0,5),
    "THE TABLE. AYIN tachat AYIN, SHEN tachat SHEN, YAD tachat YAD, REGEL tachat RAGEL — 'EYE for eye, TOOTH for tooth, HAND for hand, FOOT for foot': the corpus's most famous table — four pairs on one pivot-word (TACHAT, the under-word: eight body-words balanced on four unders) — and the tradition's unanimous law carried at full prominence: MONETARY COMPENSATION ('eye for eye — MONEY,' the readings' universal ruling; the Talmud's proofs named-only): the machine files the table as the code's measuring-doctrine: not symmetry of wounds but EQUIVALENCE OF VALUE — the next verses (the slave freed for an eye) are the table's own commentary.")])
V[25] = v("BURN_FOR_BURN", "burn for burn, wound for wound, bruise for bruise.",
  "burn for burn, wound for wound", "bruise for bruise",
  "The table's second row.",
  [p("HOLDS(kviya_tachat_kviya, t0)", (0,5),
    "THE SECOND ROW. KEVIYA tachat keviya, PETZA tachat patza, CHABURA tachat chabura — 'BURN for burn, WOUND for wound, BRUISE for bruise': the table descends from lost limbs to marks that heal (the machine notes the code's precision: three grades of non-permanent injury each priced — the readings' five payment-heads (damage, pain, healing, idleness, shame) distributed across 21:19's and this verse's clauses, named): the corpus's injury-law complete in two verses and seven unders.")])
V[26] = v("THE_EYE_THAT_FREES", "And when a man strikes the eye of his slave, or the eye of his maidservant, and destroys it — he shall let him go free for his eye.",
  "and when a man strikes the eye of his slave, or the eye of his maidservant, and destroys it", "he shall let him go free for his eye",
  "The handler; the vav brackets.",
  [h_("HANDLER IF(yake ish et en avdo ve-shichatah) THEN(la-chafshi yeshalchenu tachat eno)", (11,14),
    "THE EYE [EX21-09 CROWN]. ve-khi-yake ish et-EN avdo o et-en amato VE-SHICHATAH — 'strikes the EYE of his slave... and DESTROYS it' — LA-CHOFSHI yeshalchenu TACHAT ENO — 'he shall let him go FREE for his eye': the handler installed — the talion-table applied to the slave becomes MANUMISSION (the under-word's third use in three verses: the slave's eye is 'paid' with his liberty); and the letter-frame VERIFIED at the build: this verse and the tooth-verse BOTH OPEN WITH VAV AND CLOSE WITH VAV, together exactly TWENTY-SIX WORDS — the Kitzur: the twenty-four limb-tips by which a slave goes free, with TOOTH and EYE joined: twenty-six (the freedom-roster counted by the verses that establish it) — and the far parallel named: Noah's CURSED-CANAAN and BLESSED-THE-LORD verses share the same frame (vav to vav, twenty-six words): the verses that freed a slave's eye answering the verses where slavery entered the canon.")])
V[27] = v("THE_TOOTH_THAT_FREES", "And if he makes the tooth of his slave, or the tooth of his maidservant, fall out — he shall let him go free for his tooth.",
  "and if he makes the tooth of his slave, or the tooth of his maidservant, fall out", "he shall let him go free for his tooth",
  "The smallest limb; the same door.",
  [h_("HANDLER IF(shen avdo o shen amato yapil) THEN(la-chafshi yeshalchenu tachat shino)", (7,10),
    "THE TOOTH [EX21-09]. ve-im-SHEN avdo o-shen amato YAPIL — 'if he makes the TOOTH of his slave fall' — la-CHOFSHI yeshalchenu tachat SHINO — 'free for his tooth': the second freedom-handler (the vav-to-vav frame's second half, VERIFIED) — the machine notes the a-fortiori the pair performs: the EYE is a man's world and the TOOTH his smallest permanent part, and the code prices both at the SAME liberty: between the greatest loss and the least, the master's title does not survive either (the readings' twenty-four extensions ride exactly this equivalence).")])
V[28] = v("THE_GORING_OX", "And when an ox gores a man or a woman, and he dies — the ox shall surely be stoned, and its flesh shall not be eaten; and the owner of the ox is clear.",
  "and when an ox gores a man or a woman, and he dies — the ox shall surely be stoned, and its flesh shall not be eaten", "and the owner of the ox is clear",
  "The beast on trial.",
  [c_("CASE(ve-khi yigach shor et ish o et isha va-met) ROUTE(shor_nagach)", (0,8),
    "THE SIXTH CASE [EX21-10 CROWN]. ve-khi-YIGACH SHOR et-ish o et-isha va-MET — 'when an OX GORES a man or a woman, and he dies': the case installed — SAQOL YISAQEL ha-shor: the surely-stoned doubling's second and last Torah station (the 19:13 pair CLOSES IN-SPAN: the mountain-toucher's protocol becomes the ox's — 'from here we learn for the generations': the Sinai-fence's one-time rule now standing court-law); VE-LO YEAKHEL et-besaro — 'its flesh shall NOT BE EATEN': and the cipher EXACT (VERIFIED at the build): ve-lo yeakhel = VE-LO HANAA, 'and no BENEFIT' (98 = 98 — the halakha's benefit-ban encoded in the letters' own arithmetic); u-vaal ha-shor NAQI — 'and the owner is CLEAR' (first goring — the readings' three readings of naqi, named-only): the machine files the marvel plainly: the corpus puts an ANIMAL ON TRIAL, executes it by the mountain's own protocol, and quarantines its carcass by cipher.")])
V[29] = v("THE_WARNED_OX", "And if it was a goring ox from yesterday and the day before, and its owner was warned, and he did not guard it, and it killed a man or a woman — the ox shall be stoned, and its owner shall also die.",
  "and if it was a goring ox from yesterday and the day before, and its owner was warned, and he did not guard it, and it killed a man or a woman", "the ox shall be stoned, and its owner shall also die",
  "The handler; the lean yesterday.",
  [h_("HANDLER IF(shor nagach hu mi-temol shilshom, ve-huad bi-vealav ve-lo yishmerenu, ve-hemit) THEN(ha-shor yisaqel ve-gam bealav yumat)", (0,9),
    "THE WARNED OWNER [EX21-11 CROWN]. ve-im SHOR NAGACH hu MI-TEMOL shilshom — 'a GORING ox FROM YESTERDAY and before': the from-yesterday word LEAN — and the same idiom returns FULL at 21:36 (asserted): TWO SPELLINGS, ONE CHAPTER — MS documenting the guardianship: the Hillel and Jerusalem exemplars SPLIT OVER BOTH VERSES IN OPPOSITE DIRECTIONS, 'and in all our books: lean at the first, full at the second' (the Ramah sealing both); and the lean form's Torah-pair VERIFIED: this ox and the MANSLAYER ('who hated him not FROM YESTERDAY,' Deut 19:4) — the ox CONVICTED by its yesterdays, the manslayer ACQUITTED by his (one thinned word carrying past-record both ways); ve-HUAD bi-vealav — 'and its owner was WARNED' (the muad-doctrine installs: liability follows knowledge); ve-gam BEALAV YUMAT — 'its owner SHALL ALSO DIE' (with the next verse's ransom the readings read it to Heaven's court, named): NAGACH's in-span pair asserted — 'damages learned from death.'")])
V[30] = v("THE_RANSOM", "If a ransom be laid on him — then he shall give the redemption of his life, according to all that is laid on him.",
  "if a ransom be laid on him", "then he shall give the redemption of his life, according to all that is laid on him",
  "The handler; the priced life.",
  [h_("HANDLER IF(kofer yushat alav) THEN(ve-natan pidyon nafsho)", (4,6),
    "THE RANSOM [EX21-12 CROWN]. im-KOFER yushat alav — 'if a RANSOM be laid on him' — ve-natan PIDYON NAFSHO — 'the REDEMPTION of his life': the handler installed — and the redemption-word's only Torah station, written LEAN (VERIFIED); its Scripture-twin the Psalm ('PRECIOUS is the redemption of their soul'): the Kitzur — 'a hint that THE RANSOM ATONES: because their soul is PRECIOUS in the eyes of the Holy One, He granted a ransom for atonement' (the code's only capital charge that money may answer — the machine files the theology: the life is buyable back because it is dear, not cheap).")])
V[31] = v("SON_OR_DAUGHTER", "Whether it gore a son, or gore a daughter — according to this ordinance shall it be done to him.",
  "whether it gore a son, or gore a daughter", "according to this ordinance shall it be done to him",
  "The minors covered.",
  [p("HOLDS(ka_mishpat_ha_ze, t0)", (6,9),
    "THE EXTENSION. o-VEN yigach o-VAT yigach — 'whether a SON it gore or a DAUGHTER' — ka-MISHPAT ha-ZE yease lo — 'according to THIS ORDINANCE': the code's title-word again (the mishpat applied to minors: the Kitzur's rule from the Masorah-pair named — 'liability for the small as for the great'): the machine notes the verse's quiet doctrine: the child's life carries the adult's law — no discount for size.")])
V[32] = v("THIRTY_SHEKELS", "If the ox gore a slave or a maidservant — thirty shekels of silver he shall give to his master, and the ox shall be stoned.",
  "if the ox gore a slave or a maidservant", "thirty shekels of silver he shall give to his master, and the ox shall be stoned",
  "The fixed price; the stoning stands.",
  [h_("HANDLER IF(eved yigach ha-shor o ama) THEN(kesef sheloshim sheqalim yiten la-adonav, ve-ha-shor yisaqel)", (6,12),
    "THE SLAVE'S TARIFF. im-EVED yigach ha-shor o AMA — 'if the ox gore a SLAVE or a MAIDSERVANT' — kesef SHELOSHIM SHEQALIM yiten la-adonav — 'THIRTY SHEKELS to his master': the handler installed — the code's one FIXED tariff (free victims are priced by ransom-assessment; the slave by flat rate — the machine files the asymmetry as data, lean-record, with the readings' whether-worth-more rule named); ve-ha-SHOR YISAQEL — 'and the ox SHALL BE STONED': the stoning stands regardless of the victim's status (the machine notes the floor under the asymmetry: the OX dies for the slave exactly as for the free — the execution-protocol knows no rank even where the tariff does).")])
V[33] = v("THE_OPEN_PIT", "And when a man opens a pit, or when a man digs a pit, and does not cover it — and an ox or a donkey falls in there:",
  "and when a man opens a pit, or when a man digs a pit, and does not cover it", "and an ox or a donkey falls in there",
  "The negligence case.",
  [c_("CASE(ve-khi yiftach ish bor o ki yikhre ish bor ve-lo yekhasenu) ROUTE(baal_ha_bor)", (0,10),
    "THE SEVENTH CASE. ve-khi-YIFTACH ish BOR o ki-YIKHRE ish bor — 'when a man OPENS a pit, or DIGS a pit' (the opener and the digger both — the readings: even the re-opener of another's digging owns the hazard); VE-LO YEKHASENU — 'and does NOT COVER IT': the case installed on the omission (the machine files the category-shift: the code moves from blows and horns to NEGLIGENCE — liability without any striking hand: the pit-owner's crime is a lid not placed); ve-nafal SHAMA shor o CHAMOR — the shin of the falling ox dageshed in the precise codices (MS, named).")])
V[34] = v("THE_PIT_PAYS", "The owner of the pit shall pay; silver he shall return to its owner — and the dead shall be his.",
  "the owner of the pit shall pay; silver he shall return to its owner", "and the dead shall be his",
  "The handler; the first restitution.",
  [h_("HANDLER IF(nafal shama shor o chamor) THEN(baal ha-bor yeshalem, kesef yashiv li-vealav)", (0,5),
    "THE RESTITUTION [EX21-12]. BAAL HA-BOR yeshalem — 'the OWNER OF THE PIT shall pay': the handler installed — the code's restitution-verb (shalem) opens its career (the machine notes the ledger the next chapter will run on this verb); KESEF yashiv li-VEALAV — 'silver he shall RETURN to its owner' (the Kitzur's owner-file: this payment, the bailee's (22:13), and Ecclesiastes' 'wealth kept for its owner TO HIS HURT' — 'from his wealth he dug the pit, and it is to his hurt'; the even-bran rule named); ve-ha-MET yihye-LO — 'and the dead shall be HIS' (the carcass to the victim's owner in the accounting — the readings; the Kitzur's tending-cipher named): the corpus's first tort settled in full.")])
V[35] = v("OX_AGAINST_OX", "And when a man's ox strikes his fellow's ox, and it dies — they shall sell the living ox and divide its silver, and the dead one they shall also divide.",
  "and when a man's ox strikes his fellow's ox, and it dies", "they shall sell the living ox and divide its silver, and the dead one they shall also divide",
  "The split loss.",
  [c_("CASE(ve-khi yigof shor ish et shor reehu va-met) ROUTE(shor_et_shor)", (0,7),
    "THE EIGHTH CASE. ve-khi-YIGOF shor-ish et-SHOR REEHU va-met — 'when a man's ox strikes HIS FELLOW'S OX, and it dies': the case installed — beast against beast (no human victim: the code completing its coverage matrix — man on man, man on beast's owner, beast on man, now beast on beast); u-makhru et-ha-shor ha-CHAI ve-CHATZU et-kaspo ve-gam et-ha-MET yechetzun — 'they shall SELL the LIVING ox and DIVIDE its silver, and the DEAD they shall also divide': the fifty-fifty of the first, unwarned goring (the readings' half-damages doctrine riding the split, named): the machine files the verse's elegant court-math: two owners, one carcass, one live ox — everything halved because fault is not yet assigned.")])
V[36] = v("THE_KNOWN_GORER", "Or it was known that it was a goring ox from yesterday and the day before, and its owner did not guard it — he shall surely pay ox for ox, and the dead shall be his.",
  "or it was known that it was a goring ox from yesterday and the day before, and its owner did not guard it", "he shall surely pay ox for ox, and the dead shall be his",
  "The handler; the full yesterday.",
  [h_("HANDLER IF(noda ki shor nagach hu mi-temol shilshom ve-lo yishmerenu bealav) THEN(shalem yeshalem shor tachat ha-shor)", (11,15),
    "THE KNOWN GORER [EX21-11]. o NODA ki shor NAGACH hu MI-TEMOL shilshom — 'or it was KNOWN that it was a goring ox FROM YESTERDAY': the from-yesterday word now FULL (VERIFIED census at the build — the four full stations; the exemplars' opposite splits sealed by the Ramah: lean at 29, full here) — and the goring-word's in-span pair closes (21:29 + 21:36, asserted); SHALEM YESHALEM shor tachat ha-shor — 'he shall SURELY PAY, ox for ox': the handler installed — knowledge converts the half-split to FULL restitution (the muad-doctrine priced: the tachat-formula's last in-span use — the under-word that ran the talion-table closes the chapter's accounting); ve-ha-MET yihye-lo — the carcass credited (the second lamed dageshed like the first, MS named).")])
V[37] = v("FIVE_OXEN_FOUR_SHEEP", "When a man steals an ox or a sheep, and slaughters it or sells it — five oxen he shall pay for the ox, and four sheep for the sheep.",
  "when a man steals an ox or a sheep, and slaughters it or sells it", "five oxen he shall pay for the ox, and four sheep for the sheep",
  "The ninth case; the open seam.",
  [c_("CASE(ki yignov ish shor o se u-tevacho o mekharo) ROUTE(ganav_shor_o_se)", (0,8),
    "THE NINTH CASE [EX21-13]. ki YIGNOV ish SHOR o-SE u-TEVACHO o mekharo — 'when a man STEALS an ox or a sheep, and SLAUGHTERS it or sells it': the case installed at a CLOSED SECTION (MS: the break stands here, with the held vowel-and-binder note) — CHAMISHA VAQAR yeshalem tachat ha-shor ve-ARBA-TZON tachat ha-se — 'FIVE oxen for the ox, FOUR sheep for the sheep': the multiplied restitution (the readings' two accounts of the ox's extra ox — the beast's lost labor, or the thief's shoulder-shame spared the sheep-carrier — named-only); and the machine files the chapter's final care-point: THE PERICOPE DOES NOT END HERE — the thief's law runs past the chapter-break into the next span (the tunneler, the double-payment: armed): the code, unlike the chapter, does not pause — the corpus's law-genre has learned to be continuous.")])

# ---- scenarios ----------------------------------------------------------
BASE = "no test, no name."
expects = {}
expects[1] = [BASE]
expects[2] = ["Facts eved_ivri HOLD;", BASE]
expects[3] = [BASE]
expects[4] = [BASE]
expects[5] = [BASE]
expects[6] = ["Facts martzea HOLD;", BASE]
expects[7] = ["Facts ama_ivriya HOLD;", BASE]
expects[8] = [BASE]
expects[9] = [BASE]
expects[10] = [BASE]
expects[11] = ["Facts chinam HOLD;", BASE]
expects[12] = ["STATUTES 1 standing", BASE]
expects[13] = ["Facts yanus HOLD;", BASE]
expects[14] = ["Facts mizbechi HOLD;", BASE]
expects[15] = ["STATUTES 2 standing", BASE]
expects[16] = ["STATUTES 3 standing", BASE]
expects[17] = ["STATUTES 4 standing", BASE]
expects[18] = ["Facts makkeh_reehu HOLD;", BASE]
expects[19] = ["Facts yerape HOLD;", BASE]
expects[20] = ["Facts makkeh_avdo HOLD;", BASE]
expects[21] = ["Facts khaspo HOLD;", BASE]
expects[22] = ["Facts ason_o_lo HOLD;", BASE]
expects[23] = ["Facts nefesh HOLD;", BASE]
expects[24] = [BASE]
expects[25] = [BASE]
expects[26] = ["Facts chafshi HOLD;", BASE]
expects[27] = ["Facts shino HOLD;", BASE]
expects[28] = ["Facts shor_nagach HOLD;", BASE]
expects[29] = ["Facts yisaqel HOLD;", BASE]
expects[30] = ["Facts pidyon HOLD;", BASE]
expects[31] = [BASE]
expects[32] = ["Facts sheqalim HOLD;", BASE]
expects[33] = ["Facts baal_ha_bor HOLD;", BASE]
expects[34] = ["Facts yeshalem HOLD;", BASE]
expects[35] = ["Facts shor_et_shor HOLD;", BASE]
expects[36] = ["Facts shalem HOLD;", BASE]
expects[37] = ["Facts ganav_shor_o_se HOLD;", BASE]
titles = {
    1: "and these are the ordinances", 2: "the Hebrew slave", 3: "as he came",
    4: "the master's wife", 5: "I love my master", 6: "the awl and the door",
    7: "the daughter sold", 8: "the qere of mercy", 9: "as the daughters",
    10: "her three rights", 11: "out free, without money",
    12: "the striker of man", 13: "the place to flee", 14: "from My altar",
    15: "the striker of parents", 16: "the man-stealer",
    17: "the curser of parents", 18: "the brawl", 19: "the healing license",
    20: "the struck slave", 21: "a day or two days", 22: "the struck mother",
    23: "life for life", 24: "eye for eye", 25: "burn for burn",
    26: "the eye that frees", 27: "the tooth that frees",
    28: "the goring ox", 29: "the warned ox", 30: "the ransom",
    31: "son or daughter", 32: "thirty shekels", 33: "the open pit",
    34: "the pit pays", 35: "ox against ox", 36: "the known gorer",
    37: "five oxen, four sheep",
}

steps, scenarios = [], []
for i, vs in enumerate(sorted(V), 1):
    spec = V[vs]
    steps.append(unitgen.build_step(db, "Exod", "Exod", 21, vs, i, spec))
    scenarios.append(unitgen.scenario_for(
        db, "Exod", 21, vs, "S%d" % i,
        "after STEP_Ex_21_%d — %s" % (vs, titles[vs]),
        spec["en"].replace("[EN-AID] ", ""), expects[vs]))

ttl_he, ttl_tr = unitgen.join_tokens(unitgen.verse_tokens(db, "Exod", 21, 1)[0:2], strip_accents=False)

META = '''# =============================================================================
# LOGIC UNIT: Exodus 21:1-37 — the ordinances: slaves, blows, oxen, and pits
#             (the corpus's first casuistic code)
# FORWARD ERA unit #35 — derived 2026-08-10 (oral layer in-pipeline; review waived)
# Run FWD-8 block 5.
# =============================================================================
# Experimental model — not binding religious law.

meta:
  id: "exo_21_the_ordinances"
  title_en: "The ordinances (21:1-37)"
  title_he: %s
  title_he_translit: "%s"
  title_he_en: "'and these are the ordinances'"
  book_he: שְׁמוֹת
  book_he_translit: Shemot
  book_en: Exodus
  refs: "21:1-37"
  unit_span_planned: "21:1-37"
  data_paths_he:
  - "Data/Exod.xml"
  status: frozen
  draft_note_en: >
    DERIVED 2026-08-10 · FORWARD ERA unit #35 (run FWD-8 block 5;
    Exod 1-21 continuous behind it). Span: 21:1-37, whole
    chapter: 37 verses (SNAPSHOT-verified; six without a
    mid-verse rest, incl. the header and the four capital
    participles). Oral layer IN-PIPELINE: manifest 13/13
    VERIFIED, zero FAILED — see oral_audit_note_en.

    MACHINE PROFILE. NINE CASES, FOURTEEN HANDLERS, FOUR
    STATUTES — the corpus's first PURE CASUISTIC CODE in the
    exodus stack (lev_13's CASE/HANDLER operators at their
    source): nine ki-intake-filters (the Hebrew slave, the
    daughter, the brawl, the struck slave, the struck
    mother, the goring ox, the pit, ox-against-ox, the
    thief), fourteen standing IF-THEN handlers, and four
    capital PARTICIPLES installed as statutes (the
    man-striker, the parent-striker, the man-stealer, the
    parent-curser — STATUTES 4 standing at 21:17). NOTHING
    OWED TO THE QUEUE: laws install, cases execute later —
    the queue closes empty (the corpus's law-genre
    signature: zero DECLAREs, zero RESULTs, zero EVENTS —
    the first exodus-stack unit with no narrative op at
    all). Wires closed IN-SPAN: 19:13's surely-stoned pair
    lands at the ox (21:28 — the Sinai-fence protocol
    becomes court-law); 15:26's I-am-your-Healer answered
    by 21:19's human license (the Torah's only
    he-shall-surely-heal); 17:2's quarrel-verb
    domesticated at 21:18; 20:12's honor-command priced at
    21:15/17; 20:15's theft identified at 21:16 (the
    kidnapper); the six-and-one frame's third scale (the
    slave's six years). MACHINE EVIDENCE asserted at the
    build: the header's fraud-finals + five words; the
    alef/vav qere pair adjacent (21:8); the alef-to-alef
    brackets (21:19, 21:21); the vav-to-vav freedom pair
    with its 26 words; the awl's 400; the no-benefit 98;
    the two yesterdays (lean 29 / full 36) with their
    censuses; the exit-verb's three women; the goring
    pair in-span. Queue at close: EMPTY in-unit.
    REGISTRY 0; TESTS 0.

    CARE-POINTS: the one-op-per-verse discipline (the
    pericope's IF sometimes lives a verse before its
    HANDLER — the handler quotes the IF); the participial
    statutes vs the ki-cases (apodictic form inside the
    casuistic code — the grammar-shift for capital law);
    the talion-table held with the tradition's monetary
    law named prominently (21:23-25); the hard verses
    (21:4's split household, 21:21's ki-khaspo) kept at
    the text's surface, lean-record, the tradition's
    boundaries named-only; THE OPEN SEAM: the thief's
    pericope (21:37) runs past the chapter into the next
    span — the code does not pause at the chapter-break.
    WATCHLIST ARMS: 22:1-3 (the thief's law continues —
    the tunneler, the double payment), 22:24 (the code
    turns to the poor), 24:7 (the book of the covenant
    read aloud — this code's public reading), Lev 24:19-20
    (the talion restated), Lev 25:39-46 (the slave-laws'
    second pass; the jubilee's forever), Num 35 (the
    refuge-cities built from 21:13's seed), Deut 15
    (the release re-legislated; the awl re-explained),
    Deut 19:4-6 (the manslayer's lean yesterday). Outside-
    Torah names (named-only): Josh 9 (the Gibeonites'
    scheme), 1 Kgs 2:28-34 (Joab at the altar-horns —
    21:14 executed), 2 Sam 16 (Shimi's verse-end curse),
    Ps 49 (the precious ransom), Isa 58:4 (the wicked
    fist), Eccl 5:12 (wealth to its owner's hurt).
  oral_audit_note_en: >
    ORAL AUDIT 2026-08-10 (IN-PIPELINE, forward era; manifest
    logic/oral_audit/manifests/exo_21_the_ordinances_claims.json
    13/13 VERIFIED, zero FAILED; record
    logic/oral_audit/AUDIT_exo_21_2026-08-10.md). CROWNS
    (chain-attested + DB-verified). THE FRAUD-FINALS
    [EX21-01, KB on 21:1]: the header's four words end in
    the letters of מרמה ("fraud," final-letters checked):
    "if a fraudulent case comes before the judge, probe it
    to its truth"; five words = the five books — the true
    judge as creation's partner; the first-letter duties
    named. THE AWL'S FOUR HUNDRED [EX21-02, KB on 21:6]: מרצע
    ("awl") = 400 EXACT (asserted) — "redeemed after 400
    years of bondage, and he went and enslaved himself:
    pierced by the awl of four hundred"; the door — "let
    him guard his master's house"; the lean forever. THE
    GARMENT-BETRAYAL PAIR [EX21-03, KB on 21:8]: בבגדו
    ("in his garment / his betrayal") exactly twice
    (checked): the treacherous master and POTIPHAR'S WIFE
    seizing Joseph's garment — Rabbi Eliezer's spread
    cloth, Rabbi Aqiva's "there too was betrayal." THE
    ALEF-VAV TRIO [EX21-04, MS on 21:8]: written לא
    ("not"), read לו ("for himself") — one of the Torah's
    THREE alef-written-vav-read words (adjacent tokens
    checked; the locust's legs, the walled city): "he
    OUGHT to have designated her — designation precedes
    redemption" (Onkelos): mercy voiced out of negation.
    THE THREE WOMEN'S EXITS [EX21-05, KB on 21:7-11]:
    ויצאה ("and she shall go out") exactly three in the
    Torah (checked) — ALL women leaving a man's house:
    the wife with him, the maid free, the divorcee; the
    maid likened to the wife; כצאת the Moses-pair
    (asserted; the sun-twin); וענתה lean — "the essential
    season is the Sabbath." THE TWO PRESUMPTIONS
    [EX21-06, MS + KB on 21:14]: יזד lean at the schemer,
    full at the FALSE PROPHET (Deut 18:20; both unique,
    checked/asserted) — "the prophet who presumes is as
    one who murders"; בערמה unique — the schemer taken
    FROM the altar, the Gibeonites' scheme brought TO it.
    THE HEALING LICENSE [EX21-07, KB on 21:19]: ירפא
    ("he shall heal") — the Torah's ONLY station
    (checked): "from here, permission is granted to the
    physician to heal" (Marah's Divine Healer and the
    human license — the corpus's two healing-grants); the
    verse runs alef to alef (asserted) — sufferings sent
    with a decree; the three amnesties (the healed, the
    cleared, the king). THE CAIN-SKELETON [EX21-08, KB on
    21:21]: יקם four in the Torah (checked): CAIN's
    sevenfold, LAMECH's, the slave NOT avenged — the
    vengeance-verb born at the first murder, regulated at
    the slave-law (Eve's "acquired" read into the
    for-he-is-his-money clause); Esau's arise the fourth
    face; alef-to-alef — the full cycle. THE VAV-TO-VAV FREEDOM [EX21-09, KB on
    21:26-27]: both freedom-verses open and close with
    vav, together exactly 26 words (checked/counted) —
    the limb-roster by which a slave goes free; Noah's
    curse-and-bless verses share the frame: the verses
    that free a slave's eye answering the verses where
    slavery entered the canon. THE NO-BENEFIT CIPHER
    [EX21-10, KB on 21:28]: ולא יאכל ("it shall not be
    eaten") = ולא הנאה ("and no benefit," 98 = 98,
    asserted) — the halakha in the arithmetic; 19:13's
    stoning-pair closes in-span. THE TWO YESTERDAYS
    [EX21-11, MS on 21:29/36]: מתמל lean at the warned
    ox, מתמול full seven verses later — the exemplars
    split both ways, the Ramah seals both; the lean
    pair (checked): the ox convicted by its yesterdays,
    the manslayer acquitted by his (Deut 19:4); נגח ("a
    gorer") the in-span pair. THE PRECIOUS RANSOM [EX21-12, KB on
    21:30]: פדין lean, unique (checked) — the Psalm's
    twin: "the ransom ATONES — because their soul is
    precious to Him"; the owner-file to Ecclesiastes'
    wealth-to-his-hurt. THE CURSER'S CAREER [EX21-13, KB
    + MS]: ומקלל unique at its VERSE'S HEAD (checked),
    Shimi's curse at its verse's END — "head of the
    Sanhedrin, and became the tail"; באגרף unique (the
    wicked fist); ענוש full, בפללים lean-full (the
    exemplar-splits); the closed section at the thief —
    whose law outruns the chapter.
  owner_language_note: >
    English for reading only. Hebrew is the derivation source.
  oral_policy_note_en: >
    Written trees first. Dual-track Oral only when named; never
    silent-merge.
  tree_derive_version: logic_derived_v1
  tree_derive_phase: "FWD-35"
  confidence_overall: "structure tested; oral layer verified 13/13"
  genre: "casuistic_law_code"
  build_track: exodus_stack
  depends_on: exo_20_the_ten_utterances
  depends_note_en: >
    Depends for PATTERN only (the Decalogue's case-law: the
    honor-command priced, the theft identified, the
    stoning-protocol inherited; the six-and-one frame's third
    scale). Standalone machine. Exod 1-21 continuous, 97
    frozen units.
''' % (ttl_he, ttl_tr)

DLOG = '''derivation_log:
  - step: A
    name_en: "Block choice"
    comment: >
      FORWARD ERA run 8, block 5 (owner: "lets do 5 more blocks").
      Canon continuation: Exod 21:1-37 — the ordinances, whole
      chapter.
    confidence: established
  - step: B
    name_en: "Span + source + conventions"
    comment: >
      SNAPSHOT prestage: 37 verses; six without etnachta (the
      header + the capital participles + the talion rows).
      Volitive census: ZERO queue-cards — the chapter is pure
      law: nine ki-cases, fourteen weqatal handlers, four
      participial capital statutes. The thief's pericope
      (21:37) runs past the chapter-break (care-point).
    confidence: established
  - step: C
    name_en: "Machine structure"
    comment: >
      9 CASES / 14 HANDLERS / 4 STATUTES / 0D / 0R / 0E — the
      first pure law-code unit of the exodus stack (lev_13's
      operators at their source). Laws install; the queue
      closes empty. In-span wires: the stoned-ox pair from
      19:13; the healing license answering Marah; the
      quarrel-verb domesticated; the Decalogue priced.
      Asserted evidence: the fraud-finals; the alef/vav
      adjacent pair; the four letter-brackets; 400; 98; the
      two yesterdays; the three women's exits; 26 words.
    confidence: tested
  - step: D
    name_en: "Oral scan (in-pipeline)"
    comment: >
      Local mirror only (zero fetches): Minchat Shai on Exod 21
      (19 notes) + Kitzur Baal HaTurim on Exod 21 (34 notes).
      Manifest 13 rows: 13 VERIFIED / 0 FAILED / 0 UNCHECKABLE,
      first run. The fraud-finals; the awl's 400; the
      garment-betrayal pair; the alef-vav trio; the three
      exits; the two presumptions; the healing license; the
      Cain-skeleton; the vav-to-vav freedom; the no-benefit
      cipher; the two yesterdays; the precious ransom; the
      curser's career.
    confidence: established
  - step: E
    name_en: "Gates"
    comment: >
      verify_claims.py 13/13 zero FAILED; verify_text.py green;
      preflight ALL GREEN; gloss_lint clean. Review waived per the
      revised standing law.
    confidence: established
  - step: F
    name_en: "Freeze"
    comment: >
      status: frozen 2026-08-10 on green mechanical gates (forward-era
      law). Oral layer in-pipeline. Changes require a new derive pass,
      not silent edits. Exod 1-21 continuous.
    confidence: established
'''

unitgen.emit_unit(META, DLOG, steps, scenarios, "logic/units/exo_21_the_ordinances.yaml")
print("wrote logic/units/exo_21_the_ordinances.yaml —", len(steps), "steps,", len(scenarios), "scenarios")
