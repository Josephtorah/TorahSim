#!/usr/bin/env python3
"""Author exo_16_manna_and_sabbath (Exod 16:1-36) — forward-era unit #30 (run FWD-7 block 1).
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

# ---- build-time machine evidence (asserted, not crowns) -------------------
assert census("ממטיר") == [("Exod", 9, 18), ("Exod", 16, 4), ("Gen", 7, 4)]   # rain: flood, hail, bread
assert census("מאנתם") == [("Exod", 16, 28)]                                   # the refuse-verb, plural, unique
assert census("וישבתו") == [("Exod", 16, 30)]                                  # and-they-rested, unique
assert census("ויקצף") == [("Deut", 1, 34), ("Exod", 16, 20), ("Gen", 40, 2),
                           ("Lev", 10, 16), ("Num", 31, 14)]                   # the wrath-verb five
assert census("המן") == [("Deut", 8, 3), ("Exod", 16, 35), ("Exod", 16, 35),
                         ("Gen", 3, 11), ("Num", 11, 6), ("Num", 11, 9),
                         ("Num", 20, 10)]                                      # the manna-and-question skeleton
assert (hp(16, 2, 0), hp(16, 2, 1)) == ("וילינו", "וילונו")                    # ketiv/qere murmur 1
assert (hp(16, 7, 13), hp(16, 7, 14)) == ("תלונו", "תלינו")                    # ketiv/qere murmur 2
assert (hp(16, 17, 0), hp(16, 17, 1)) == ("ויעשו", "כן")                       # they did so
assert (hp(16, 24, 4), hp(16, 24, 5)) == ("כאשר", "צוה")                       # as commanded
assert (hp(16, 31, 0), hp(16, 31, 4), hp(16, 31, 5)) == ("ויקראו", "שמו", "מן")  # the naming
assert (hp(16, 34, 5), hp(16, 34, 6)) == ("ויניחהו", "אהרן")                   # Aaron lays it
G = {"א":1,"ב":2,"ג":3,"ד":4,"ה":5,"ו":6,"ז":7,"ח":8,"ט":9,"י":10,"כ":20,"ך":20,
     "ל":30,"מ":40,"ם":40,"נ":50,"ן":50,"ס":60,"ע":70,"פ":80,"ף":80,"צ":90,"ץ":90,
     "ק":100,"ר":200,"ש":300,"ת":400}
g = lambda s: sum(G[c] for c in s if c in G)
assert g("סין") == g("הסנה") == 120                                            # Sin = the bush
assert g("מחספס") == 248                                                       # the 248 limbs
toks16 = [hp(16, 16, i) for i in range(18)]
norm = {"ך":"כ","ם":"מ","ן":"נ","ף":"פ","ץ":"צ"}
letters = {norm.get(c, c) for c in "".join(toks16)}
assert set("אבגדהוזחטיכלמנסעפצקרשת") <= letters                                # the whole alphabet in 16:16
assert sorted(hp(16, 32, i)[0] for i in range(12, 16)) == sorted("אליה")       # the Elijah initials

P = "PRECONDITION_STATE"
D = "DECLARE"
R = "RESULT"
E = "EVENT"

def v(op, en, left, right, comment, ops):
    return dict(op=op, en=en, left_en=left, right_en=right, comment=comment, operators=ops)

def p(expr, span, prose):
    return dict(op=P, expr_en=expr, he_span=span, prose=prose)

V = {}
V[1] = v("INTO_THE_WILDERNESS_OF_SIN", "And they journeyed from Elim, and all the congregation of the sons of Israel came to the wilderness of Sin, which is between Elim and Sinai, on the fifteenth day of the second month after their going out from the land of Egypt.",
  "and they journeyed from Elim, and all the congregation of the sons of Israel came to the wilderness of Sin, which is between Elim and Sinai", "on the fifteenth day of the second month after their going out from the land of Egypt",
  "The dated station; the bush-cipher.",
  [p("HOLDS(va_yavou_el_midbar_sin, t0)", (0,14),
    "THE STATION [EX16-11 CROWN]. va-yisu me-ELIM... el-midbar-SIN — from the twelve springs to the wilderness of SIN: the desert's name counts THE BUSH (asserted at the build: 120 = 120 — the Kitzur: named for the thornbush of the calling; 'and it is called SINAI for the TEN utterances given on it': the desert plus its yod — the mountain named as the wilderness plus its commandments); the station-word's Torah-census exactly FOUR (VERIFIED: the arrival, the departure 17:1, the itinerary's pair) — with MS's spelling-law over the file: every Sin with the samekh FULL, every Tzin with the tzadi LEAN (two deserts kept apart by orthography); ben-ELIM u-ven SINAI — the address given as a span between water and law; ba-CHAMISHA ASAR yom la-chodesh ha-SHENI — the corpus's second full date (12:2's calendar-card paying: the itinerary now keeps time in the new reckoning — one month from the exodus, the machine notes the ledger: the bread of Egypt ran out on the day the manna-chapter opens, the readings named-only).")])
V[2] = v("THE_WHOLE_CONGREGATION_MURMURS", "And all the congregation of the sons of Israel murmured against Moses and against Aaron in the wilderness.",
  "and all the congregation of the sons of Israel murmured against Moses and against Aaron", "in the wilderness",
  "The dual-written murmur; Aaron added.",
  [p("HOLDS(va_yilonu_al_moshe_ve_al_aharon, t0)", (0,10),
    "THE MURMUR DOUBLED [EX16-13]. va-YILONU kol-adat bene-yisrael — 'and all the congregation MURMURED': exo_15's arm PAYS (15:24's target was Moses alone; 16:2 adds AARON — the escalation armed at Marah arrives on schedule) — and the verb itself is DUAL-WRITTEN (asserted at the build: written one way, READ va-yilonu — the ketiv-and-qere convention, gen_59's adjacent-token precedent): the murmuring reaches the page spelled one way and voiced another — the corpus's complaint-verb refusing to sit still even as a word; kol-ADAT — the kaf DAGESHED (VERIFIED in-token: the guard-class again); the WHOLE congregation (15:24's ha-am widened): ba-MIDBAR — the machine notes the address-line: the wilderness itself joins the sentence, the theater of the test named as party.")])
V[3] = v("THE_FLESH_POTS", "And the sons of Israel said to them: Would that we had died by the hand of the LORD in the land of Egypt, when we sat by the flesh-pot, when we ate bread to the full — for you have brought us out to this wilderness, to kill this whole assembly with hunger.",
  "and the sons of Israel said to them: would that we had died by the hand of the LORD in the land of Egypt, when we sat by the flesh-pot, when we ate bread to the full", "for you have brought us out to this wilderness, to kill this whole assembly with hunger",
  "The death-wish; the hunger-file opens.",
  [p("HOLDS(mi_yiten_mutenu, t0)", (4,17),
    "THE WISH [EX16-13]. MI-YITEN mutenu ve-yad-YHWH be-eretz mitzrayim — 'WOULD THAT we had died by the hand of the LORD in Egypt': the death-wish in the optative frame (the quoted-wish class — no push: a longing, not a demand; 14:11-12's grave-complaint escalated from irony to appetite); be-shivtenu al-SIR HA-BASAR be-akhlenu lechem LA-SOVA — 'when we sat by the FLESH-POT, when we ate bread TO THE FULL': the remembered menu (the Kitzur's four fill-words named: 'even in Egypt He summoned their fill — the fish free of charge': the corpus's own audit of the nostalgia — the fullness they credit to Egypt the chain credits to the same Hand they wish had killed them); le-hamit et-kol-ha-qahal ha-ze BA-RAAV — 'to kill this whole assembly WITH HUNGER': the HUNGER-FILE opens (exo_15 opened thirst, exo_16 opens famine — the wilderness-cycle testing one organ at a time).")])
V[4] = v("BREAD_FROM_HEAVEN", "And the LORD said to Moses: Behold, I rain for you bread from the heavens; and the people shall go out and gather the day's portion in its day, that I may test him — will he walk in My law, or not?",
  "and the LORD said to Moses: behold, I rain for you bread from the heavens", "and the people shall go out and gather the day's portion in its day, that I may test him — will he walk in My law, or not",
  "The rain-verb's third career; the test named.",
  [dict(op=D, expr_en="DECLARE(YHWH, LET(ve_laqtu_devar_yom_be_yomo))", he_span=(4,9),
    prose="THE RATION [EX16-07]. hineni MAMTIR lakhem LECHEM min-ha-SHAMAYIM — 'behold, I RAIN for you BREAD from the HEAVENS': the rain-causative's Torah-career exactly THREE (asserted at the build): the FLOOD (Gen 7:4), the HAIL (9:18), and the BREAD — the corpus's own arc: the verb that drowned a world and broke Egypt's stalks now sets the table (exo_15's repair-turn continued: the weapon-grammar re-tooled for provision); ve-yatzu ha-am VE-LAQTU devar-yom BE-YOMO — 'and the people shall go out and GATHER the DAY'S PORTION IN ITS DAY': the card pushed — bread by subscription, not by barn (the readings on daily trust, named-only); LEMAAN ANASENU — 'that I may TEST him': 15:25's armed test-verb PAYS ON SCHEDULE (the verdict-less test of Marah gains its named instrument: bread), ha-YELEKH be-TORATI IM-LO — 'will he walk in MY LAW, OR NOT': the test's oracle spelled as a question with both answers left standing (the machine arms the im-lo: 16:20 and 16:27 will answer it) — and the Kitzur beside it: 'THE TORAH WAS GIVEN ONLY TO THE EATERS OF THE MANNA.'")])
V[5] = v("DOUBLE_ON_THE_SIXTH", "And it shall be on the sixth day, that they shall prepare that which they bring in; and it shall be double what they gather day by day.",
  "and it shall be on the sixth day, that they shall prepare that which they bring in", "and it shall be double what they gather day by day",
  "The double armed.",
  [dict(op=D, expr_en="DECLARE(YHWH, LET(ve_hekhinu_mishne))", he_span=(0,8),
    prose="THE SIXTH [EX16-07]. ve-haya ba-yom ha-SHISHI ve-HEKHINU et asher-yaviu — 'on the SIXTH day they shall PREPARE what they bring in': the second card pushed — a calendar hidden inside a ration (the Sabbath not yet named: the machine notes the pedagogy's order — the people will meet the double before they hear its reason, 16:22-23); ve-haya MISHNE — 'and it shall be DOUBLE': the Kitzur's rule of the day: 'EVERYTHING of the Sabbath is DOUBLE — two lambs, two loaves, two lights, REMEMBER and KEEP': the mishne-word filed as the Sabbath's signature arithmetic, pushed here and popped at 16:22's two omers.")])
V[6] = v("EVENING_AND_YOU_SHALL_KNOW", "And Moses and Aaron said to all the sons of Israel: At evening — and you shall know that the LORD has brought you out from the land of Egypt.",
  "and Moses and Aaron said to all the sons of Israel", "at evening — and you shall know that the LORD has brought you out from the land of Egypt",
  "The know-ledger turns home.",
  [p("HOLDS(erev_vi_ydatem, t0)", (7,14),
    "THE KNOWING. EREV — vi-YDATEM ki YHWH hotzi etkhem me-eretz mitzrayim — 'at EVENING — and you shall KNOW that the LORD brought you out': the know-ledger OPENS A SECOND ACCOUNT (Egypt's closed underwater at 14:25; Israel's opens at supper): the same formula that priced the plagues now prices the quail — the machine files the ledger's turn: knowledge by judgment for Egypt, knowledge by provision for Israel — and the exodus re-attributed (the murmur said YOU brought us out, 16:3; the answer: THE LORD brought you out — the pronoun corrected before the meat arrives).")])
V[7] = v("MORNING_AND_THE_GLORY", "And at morning — and you shall see the glory of the LORD, in His hearing your murmurings against the LORD; and we — what are we, that you murmur against us?",
  "and at morning — and you shall see the glory of the LORD, in His hearing your murmurings against the LORD", "and we — what are we, that you murmur against us?",
  "The what-are-we; the second dual-writing.",
  [p("HOLDS(u_reitem_et_kevod_YHWH, t0)", (0,9),
    "THE FORECAST [EX16-13]. u-VOQER — u-reitem et-KEVOD YHWH — 'at MORNING — you shall SEE the GLORY of the LORD' (the glory-word's first forecast to the nation — armed, paid at 16:10); be-SHAM'O et-telunotekhem — 'in His HEARING your murmurings' (the Kitzur's three hearings named: 'in distress and justly murmuring — He heard; the self-blesser at peace — He will not hear': the heard complaint filed as the LAWFUL kind); ve-NACHNU MA — 'and we — WHAT are we?': the deflection (the readings on the humility greater than Abraham's dust-and-ashes, named-only) — and the murmur-verb DUAL-WRITTEN A SECOND TIME (asserted at the build: written talonu, READ talinu — the chapter's second ketiv-and-qere, both on the complaint-verb): the machine notes the pattern: the word the chapter cannot spell one way is the word the people cannot stop saying.")])
V[8] = v("NOT_AGAINST_US", "And Moses said: In the LORD's giving you flesh at evening to eat, and bread at morning to the full — in the LORD's hearing your murmurings which you murmur against Him; and we — what are we? Not against us are your murmurings, but against the LORD.",
  "and Moses said: in the LORD's giving you flesh at evening to eat, and bread at morning to the full — in the LORD's hearing your murmurings which you murmur against Him", "and we — what are we? Not against us are your murmurings, but against the LORD",
  "The address corrected.",
  [p("HOLDS(lo_alenu_telunotekhem, t0)", (19,26),
    "THE RE-ADDRESS. be-tet YHWH lakhem ba-erev BASAR... ve-LECHEM ba-boqer lisboa — the menu itemized before it falls (flesh at evening, bread at morning: the forecast the night will keep); ve-nachnu MA — the what-are-we doubled (16:7's deflection repeated verbatim-class); LO-ALENU telunotekhem KI AL-YHWH — 'NOT AGAINST US are your murmurings, BUT AGAINST THE LORD': the address-correction (8:8's right-address cry taught Pharaoh where petitions go; 16:8 teaches Israel where complaints land — the machine files the routing-rule: murmuring at the visible officers is murmuring at the invisible King; the readings named-only).")])
V[9] = v("DRAW_NEAR", "And Moses said to Aaron: Say to all the congregation of the sons of Israel: Draw near before the LORD — for He has heard your murmurings.",
  "and Moses said to Aaron: say to all the congregation of the sons of Israel: draw near before the LORD", "for He has heard your murmurings",
  "The summons.",
  [dict(op=D, expr_en="DECLARE(moshe, LET(qirvu_lifne_YHWH))", he_span=(4,12),
    prose="THE SUMMONS. emor el-kol-adat... QIRVU lifne YHWH — 'SAY to all the congregation: DRAW NEAR before the LORD': the card pushed through AARON (the say-command relay-class of 6:10ff — Moses to Aaron to the assembly: the chain of command the credential-file certified); ki SHAMA et telunotekhem — 'for He has HEARD your murmurings': the summons's warrant is the complaint itself — the machine notes the inversion: the murmur, lawful in hunger (16:7's hearing-rule), becomes the very writ that convenes the court.")])
V[10] = v("THE_GLORY_IN_THE_CLOUD", "And it was, as Aaron spoke to all the congregation of the sons of Israel, that they turned toward the wilderness; and behold — the glory of the LORD appeared in the cloud.",
  "and it was, as Aaron spoke to all the congregation of the sons of Israel, that they turned toward the wilderness", "and behold — the glory of the LORD appeared in the cloud",
  "The event; the card pops.",
  [dict(op=R, expr_en="RESULT: HOLDS(qirvu_lifne_YHWH, t1)", he_span=(0,7),
    prose="THE COMPLIANCE. va-yehi KE-DABER AHARON el-kol-adat — 'as AARON SPOKE to all the congregation': the draw-near card POPS on the speaking itself (the compliance narrated in the relay's own verb) — and the Kitzur reads the name: 'as AARON spoke — and not Moses — for BY AARON'S MERIT WERE THE CLOUDS; therefore it is juxtaposed: and the glory appeared IN THE CLOUD' (the speaker matched to the vessel: the cloud-man's word answered in cloud)."),
   dict(op=E, expr_en="nirat_kevod_YHWH(e1); Theme(e1, kevod-YHWH)", he_span=(11,15),
    prose="THE APPEARANCE. va-yifnu el-ha-MIDBAR — 'they turned toward the WILDERNESS' (toward the empty quarter — the readings: toward the place with nothing in it, named-only); ve-hine KEVOD YHWH nira BE-ANAN — 'and behold, the GLORY of the LORD APPEARED IN THE CLOUD': THE EVENT — the glory's first narrated appearance to the nation (13:21's pillar was guidance-infrastructure; 16:10 is DISCLOSURE: the machine stamps the corpus's first public theophany — summoned not by Sinai's thunder but by a bread-complaint: the glory shows itself to answer a menu).")])
V[11] = v("THE_FRAME", "And the LORD spoke to Moses, saying:",
  "and the LORD spoke", "to Moses, saying",
  "The frame.",
  [p("HOLDS(va_yedaber_16, t0)", (0,4),
    "THE FRAME. va-yedaber YHWH el-moshe LEMOR — the five-word frame (no etnachta; the class of 13:1 and 14:1): the machine notes the placement — the frame drops mid-chapter, AFTER the glory-event: the speech it opens (16:12) will be the chapter's only direct divine oration to Moses since 16:4 — the provision-decree's second half, spoken with the cloud still lit.")])
V[12] = v("I_HAVE_HEARD", "I have heard the murmurings of the sons of Israel — speak to them, saying: Between the evenings you shall eat flesh, and at morning you shall be filled with bread; and you shall know that I am the LORD your God.",
  "I have heard the murmurings of the sons of Israel — speak to them, saying: between the evenings you shall eat flesh, and at morning you shall be filled with bread", "and you shall know that I am the LORD your God",
  "The unique spelling; the formula comes home.",
  [p("HOLDS(shamati_et_telunot, t0)", (0,4),
    "THE HEARING [EX16-01 CROWN — THE MARQUEE]. SHAMATI et-TELUNOT bene yisrael — 'I have HEARD the MURMURINGS of the sons of Israel': the murmurings-word in a spelling with NO TWIN in the Torah (VERIFIED: full first vav, lean second — once) — and MS corrects the PRINTED MASORAH to prove it (the note that claimed a pair ruled AN ERROR: the census stands at one — the printed-authority file's next station); Lekach Tov reads the lean letter: 'they were being DIMINISHED FROM THEIR MERITS' — and the same midrash's mercy kept whole: 'all the complaints are as ONE COMPLAINT — and though they murmur, THEY ARE MY SONS: sons of Abraham, sons of Isaac bound for My name'; the nun DAGESHED for the swallowed rest-letter (MS, the Mikhlol): the verse where the Name repeats the people's murmuring back spells it as nothing else in the Torah — the machine files the crown: the complaint, heard on high, comes back with one letter of merit missing and all its sonship intact."),
   p("HOLDS(ani_YHWH_elohekhem, t0)", (15,19),
    "THE FORMULA HOME. ben ha-arbayim tokhlu VASAR u-va-boqer tisbeu-LACHEM — flesh between the evenings, bread-fullness at morning (16:8's itemization now in the first person); vi-ydatem KI ANI YHWH ELOHEKHEM — 'and you shall know that I AM THE LORD YOUR GOD': the spine-formula (6:2's self-declaration; 6:7's promise 'you shall know that I am the LORD your God who brings you out') lands its receipt — the machine closes the wire: the sentence promised in Egypt's brickyards is paid at a wilderness supper: the know-ledger's home account funded by quail.")])
V[13] = v("QUAIL_AND_DEW", "And it was at evening, that the quail came up and covered the camp; and at morning there was a layer of dew around the camp.",
  "and it was at evening, that the quail came up and covered the camp", "and at morning there was a layer of dew around the camp",
  "The event; the quail-pair.",
  [dict(op=E, expr_en="matan_basar_va_lechem(e2); Agent(e2, YHWH); Theme(e2, ha-selav)", he_span=(0,6),
    prose="THE SUPPER [EX16-03 CROWN]. va-yehi va-EREV va-taal HA-SELAV va-tekhas et-ha-machane — 'at EVENING the QUAIL came up and COVERED the camp': THE EVENT — the forecast of 16:8/12 pays on its own clock (evening flesh first, morning bread after: the promise's word-order kept); and the quail-word stands exactly TWICE in the Torah (VERIFIED): this supper and KIVROT-HATTAAVA (Num 11:32, the graves of craving) — the Kitzur: 'here too they gathered MUCH, but it CEASED — and so they went back and murmured over it' (one bird, the gift and the grave: the machine arms the pair's dark half); the word LEAN-yod in the precise books (MS with the Ramah, against the Chizkuni), and Yoma's pointed reading carried: 'the righteous eat it IN PEACE; to the wicked it is THORNS' — the cover-verb (va-TEKHAS) making its first benign appearance since the sea covered the pursuit (14:28): the same verb, dinner instead of drowning."),
   p("HOLDS(shikhvat_ha_tal, t0)", (7,12),
    "THE LAYER. u-va-boqer hayta shikhvat HA-TAL saviv la-machane — 'at morning a LAYER OF DEW around the camp': the bread arrives wrapped (the readings on the dew above and below — the manna served between linens like the showbread, named-only): the machine holds the verse at its surface — the gift comes covered, and 16:14 lifts the lid.")])
V[14] = v("FINE_AS_FROST", "And the layer of dew went up, and behold — on the face of the wilderness a fine flake-like thing, fine as frost on the ground.",
  "and the layer of dew went up", "and behold, on the face of the wilderness a fine flake-like thing, fine as frost on the ground",
  "The hapax; the 248.",
  [p("HOLDS(daq_mechuspas, t0)", (3,12),
    "THE REVEAL [EX16-06 CROWN]. va-taal shikhvat ha-tal — the dew-layer LIFTS (the unveiling verb — the same aliyah-verb that raised the quail raises the cover); ve-hine al-pene ha-midbar DAQ MECHUSPAS — 'a fine FLAKE-LIKE thing': the flake-word an absolute Torah-HAPAX (VERIFIED — the language uses it once, for a food no one had seen twice), and the Kitzur counts it: MECHUSPAS = 248 (asserted at the build) — 'for the manna was ABSORBED IN THE 248 LIMBS' (the bread with no waste: its one-time word carrying the body's own census); daq KA-KEFOR al-ha-aretz — 'fine as FROST on the ground': the machine notes the descriptive crisis the verse performs — the text reaching for three comparisons in one line for a thing that is only like itself.")])
V[15] = v("WHAT_IS_IT", "And the sons of Israel saw, and said each to his brother: What is it? — for they knew not what it was; and Moses said to them: It is the bread which the LORD has given you to eat.",
  "and the sons of Israel saw, and said each to his brother: What is it? — for they knew not what it was", "and Moses said to them: it is the bread which the LORD has given you to eat",
  "The question that will be the name.",
  [p("HOLDS(man_hu, t0)", (7,13),
    "THE QUESTION. va-yomru ish el-achiv MAN HU — 'and they said each to his brother: WHAT IS IT?' — ki LO YADU ma-hu — 'for they KNEW NOT what it was': the question-word that will become the food's NAME (16:31 armed: the corpus's only entity named for the question it raised — the machine notes the epistemic comedy the chapter builds: the know-ledger's chapter [16:6, 16:12 — you shall KNOW] pivots on a breakfast nobody can identify); va-yomer moshe... HU HA-LECHEM asher natan YHWH lakhem le-akhla — 'it IS THE BREAD which the LORD has GIVEN you': Moses answers the what with a whence (the readings on bread-of-the-mighty, named-only) — the giving-verb that will run the chapter (natan 16:15, noten 16:29 twice-given Sabbath) starts its count.")])
V[16] = v("AN_OMER_A_HEAD", "This is the thing which the LORD commanded: Gather of it, each man according to his eating; an omer a head, by the number of your souls — each man for those in his tent shall you take.",
  "this is the thing which the LORD commanded: gather of it, each man according to his eating", "an omer a head, by the number of your souls — each man for those in his tent shall you take",
  "The alphabet-verse; the measure.",
  [p("HOLDS(omer_la_gulgolet, t0)", (0,9),
    "THE MEASURE [EX16-07 CROWN]. ze ha-davar asher TZIVA YHWH — 'this is the thing the LORD COMMANDED': the errand-delivery (16:4's ration-card handed down with its measure attached — the delivery-class of 10:3); LIQTU mimenu ish LE-FI OKHLO — 'GATHER of it, each according to his EATING'; OMER la-GULGOLET — 'an OMER A HEAD, by the number of your souls' (both gimels of the skull-word dageshed — MS, asserted at the build): and the verse carrying the law carries THE WHOLE ALPHABET (VERIFIED at the build: all twenty-two letters stand in 16:16) — the Kitzur: 'whoever UPHOLDS THE TORAH, the Holy One summons him his sustenance WITHOUT TOIL, like the eaters of the manna' — the machine files the crown: the ration-verse written with every letter the Torah owns, the alphabet itself vouching for the table.")])
V[17] = v("GREAT_AND_SMALL", "And the sons of Israel did so; and they gathered — he who took much, and he who took little.",
  "and the sons of Israel did so", "and they gathered — he who took much, and he who took little",
  "The card pops.",
  [dict(op=R, expr_en="RESULT: HOLDS(ve_laqtu_devar_yom_be_yomo, t1)", he_span=(0,3),
    prose="THE COMPLIANCE. VA-YAASU-KHEN bene yisrael — 'and the sons of Israel DID SO' (asserted): the gather-card POPS on the corpus's compliance-formula (14:4's va-yaasu-khen class); va-yilqetu HA-MARBE VE-HA-MAMIT — 'he who took MUCH and he who took LITTLE': the machine holds the verse's suspense — obedience narrated with its variance showing (the leveling waits one verse: the corpus lets the unequal baskets walk home unequal before 16:18 weighs them).")])
V[18] = v("NO_LACK_NO_SURPLUS", "And they measured with the omer, and he who took much had nothing over, and he who took little lacked nothing; each man according to his eating had they gathered.",
  "and they measured with the omer, and he who took much had nothing over, and he who took little lacked nothing", "each man according to his eating had they gathered",
  "The leveled measure.",
  [p("HOLDS(lo_hedif_ve_lo_hechsir, t0)", (0,7),
    "THE LEVELING [EX16-13]. va-yamodu VA-OMER — 'they MEASURED with the omer'; ve-LO HEDIF ha-marbe ve-ha-mamit LO HECHSIR — 'the much-taker had NOTHING OVER, the little-taker LACKED NOTHING' (neither he carries a lengthener — MS's stroke-note): the measured miracle — the machine files the economy the chapter legislates: effort varies, the omer does not (the readings on the manna as the corpus's one perfectly progressive commodity, named-only): ish le-fi okhlo LAQATU — the eating-phrase file (MS: the first two le-fi, the third ke-fi at 16:21 — the Masorah tracking even the ration's prepositions).")])
V[19] = v("LEAVE_NONE_TILL_MORNING", "And Moses said to them: Let no man leave over of it till morning.",
  "and Moses said to them", "let no man leave over of it till morning",
  "The standing daily rule.",
  [dict(op=D, expr_en="DECLARE(moshe, LET(al_yoter_mimenu_ad_boqer))", he_span=(3,8),
    prose="THE PROHIBITION. ish AL-YOTER mimenu AD-BOQER — 'let NO MAN LEAVE OVER of it TILL MORNING': the card pushed — the ration's second law (gather daily; KEEP NOTHING): trust legislated as an empty shelf (the readings: bread in the basket overnight is tomorrow held hostage — named-only); the machine files the card's class: a STANDING DAILY RULE of the manna era (no single pop can close it — it stays OPEN as law), and arms the breach one verse ahead.")])
V[20] = v("WORMS_AND_WRATH", "And they listened not to Moses, and men left over of it till morning, and it bred worms and stank; and Moses was angry with them.",
  "and they listened not to Moses, and men left over of it till morning, and it bred worms and stank", "and Moses was angry with them",
  "The breach; the three liftings.",
  [p("HOLDS(va_yarum_tolaim, t0)", (4,11),
    "THE BREACH [EX16-04 CROWN]. ve-LO-SHAMU el-moshe — 'and they LISTENED NOT to Moses': the prohibition BREACHED in its first night (the card stands open and defied — the test's im-lo takes its first negative datum); va-YOTIRU anashim mimenu — 'and men LEFT OVER of it': the left-over form Torah-UNIQUE (VERIFIED), its Scripture-twin ELISHA'S BREAD ('they ate AND LEFT OVER, by the word of the LORD') — the Kitzur: 'there BY the word, a BLESSING sent into it; here AGAINST the word, a CURSE' (one verb, the obedient surplus and the hoarded rot); va-YARUM tolaim va-yivash — 'and it BRED (lifted) WORMS and stank': the lifting-word with the Kitzur's three named (the worms lift, the GLORY lifts from the cherub, the HEART lifts — 'whoever's heart lifts will lift worms: the hope of man is the worm') and MS's letter-crown VERIFIED: the resh's vowel THREE DOTS, 'in our Masorah NONE OTHER' — pointed apart precisely from the GLORY's lifting (Ezek 10:4): worm-rise and glory-rise, one skeleton, one dot-row of difference; va-YIQTZOF alehem moshe — 'and Moses was ANGRY': the wrath-verb's Torah-five (asserted at the build): Pharaoh at his servants, MOSES HERE (his first anger at the people), Moses at the priests, Moses at the officers, and the LORD at the generation — the anger-ledger opens its Moses-column on hoarded bread.")])
V[21] = v("MORNING_BY_MORNING", "And they gathered it morning by morning, each man according to his eating; and when the sun grew hot, it melted.",
  "and they gathered it morning by morning, each man according to his eating", "and when the sun grew hot, it melted",
  "The settled rhythm; the oracle of the sun.",
  [p("HOLDS(ve_cham_ha_shemesh_ve_namas, t0)", (7,9),
    "THE RHYTHM [EX16-13]. va-yilqetu oto BA-BOQER BA-BOQER — 'morning by MORNING' (the doubled adverb: the law of 16:4 become habit — after the worms, the verse of compliance without comment); ish KE-FI okhlo — the third eating-phrase (ke-fi now — MS's preposition-file closing); ve-CHAM ha-shemesh VE-NAMAS — 'when the sun grew HOT, it MELTED' (the pausal long vowel closing the verse — MS walking the grammarians' dispute, dual-tracked; the Kitzur's Yoma-file named: the melted manna ran to the streams, the nations' hunters TASTED the run-off and ground their teeth — and the sun-hot phrase itself the tradition's ORACLE: disputed paternity, disputed betrothal, disputed servants settled by WHERE THE OMER TURNED UP — the manna as the wilderness's court of record): the machine files the daily physics: what obedience gathers keeps; what waits for the sun is water.")])
V[22] = v("THE_SIXTH_DAY_DOUBLE", "And it was on the sixth day, that they gathered double bread — two omers for the one; and all the princes of the congregation came and told Moses.",
  "and it was on the sixth day, that they gathered double bread — two omers for the one", "and all the princes of the congregation came and told Moses",
  "The double lands; the card pops.",
  [dict(op=R, expr_en="RESULT: HOLDS(ve_hekhinu_mishne, t1)", he_span=(0,8),
    prose="THE DOUBLE. va-yehi ba-yom ha-SHISHI laqtu LECHEM MISHNE shene ha-omer la-echad — 'on the SIXTH day they gathered DOUBLE bread, two omers for the one': 16:5's card POPS on the ground (the double arrives in the baskets before its law arrives in words — the machine notes the sequence: the miracle complies BEFORE the people are told why); va-yavou kol-NESIE ha-eda va-yagidu le-moshe — 'and all the PRINCES came and TOLD Moses': the roster's officers report an unordered surplus (the readings: Moses had not yet relayed 16:5 — named-only): the corpus's first recorded audit — leadership discovering law by inventory.")])
V[23] = v("TOMORROW_IS_THE_REST", "And he said to them: This is what the LORD spoke — a solemn rest, a holy sabbath to the LORD, is tomorrow; that which you would bake — bake, and that which you would boil — boil, and all the surplus lay up for yourselves in keeping until the morning.",
  "and he said to them: this is what the LORD spoke — a solemn rest, a holy sabbath to the LORD, is tomorrow", "that which you would bake — bake, and that which you would boil — boil, and all the surplus lay up for yourselves in keeping until the morning",
  "The Sabbath named; the fence-order.",
  [dict(op=D, expr_en="DECLARE(moshe, LET(et_ha_odef_hanichu_le_mishmeret))", he_span=(6,10),
    prose="THE FIRST SABBATH-LAW [EX16-09 CROWN]. hu asher diber YHWH — 'this is what the LORD spoke' (16:5's withheld reason delivered); SHABBATON shabbat-QODESH la-YHWH MACHAR — 'a SOLEMN REST, a HOLY SABBATH to the LORD, is TOMORROW': THE SABBATH NAMED IN LAW for the first time in the corpus (Gen 2:2-3's seventh day, sanctified at creation and silent since, surfaces as legislation — before Sinai, over bread) — and the word-order itself the crown (VERIFIED: the rest-word-before-Sabbath adjacency stands here UNIQUELY; Vayaqhel reverses it): the Kitzur — 'to teach that WE ADD FROM THE WEEKDAY ONTO THE HOLY at its ENTRY and at its EXIT' (the day fenced on both sides by its two word-orders — the tailor's needle down before dark); et asher-tofu EFU... bashelu — 'bake what you would bake, boil what you would boil' (tomorrow's kitchen closed tonight); ve-et kol-ha-ODEF hanichu LE-MISHMERET — 'lay up the SURPLUS IN KEEPING till morning': the card pushed — yesterday's crime (16:19-20) made tonight's commandment: the machine files the inversion crown-side: the SAME ACT (keeping manna overnight) is rot on Thursday and religion on Friday — the difference is only the word it obeys.")])
V[24] = v("IT_DID_NOT_STINK", "And they laid it up until the morning, as Moses commanded; and it did not stink, and no worm was in it.",
  "and they laid it up until the morning, as Moses commanded", "and it did not stink, and no worm was in it",
  "The clean surplus; the card pops.",
  [dict(op=R, expr_en="RESULT: HOLDS(et_ha_odef_hanichu_le_mishmeret, t1)", he_span=(0,6),
    prose="THE KEEPING [EX16-05 CROWN]. va-yanichu oto ad-ha-boqer KA-ASHER TZIVA MOSHE — 'they laid it up... AS MOSES COMMANDED' (asserted): the card POPS on the exact obedience-formula — and the manna answers the obedience in kind: ve-LO hivish ve-RIMA lo-hayta bo — 'it did NOT stink, and NO WORM was in it': the worm-word Torah-UNIQUE (VERIFIED), its Scripture-twin JOB'S GRAVE ('together they lie in the dust, and the WORM covers them') — the Kitzur: 'the worm has NO POWER over the Sabbath, and no power over the manna-eaters': 16:20's Thursday worms and 16:24's Friday stillness, one substance two verdicts — the machine seals the chapter's central experiment: the variable was never the bread.")])
V[25] = v("EAT_IT_TODAY", "And Moses said: Eat it today, for today is a sabbath to the LORD; today you shall not find it in the field.",
  "and Moses said: eat it today, for today is a sabbath to the LORD", "today you shall not find it in the field",
  "The three todays.",
  [p("HOLDS(shabat_ha_yom_la_YHWH, t0)", (2,7),
    "THE TODAY. ikhluhu HA-YOM ki-shabat HA-YOM la-YHWH HA-YOM lo timtzauhu ba-sade — 'eat it TODAY, for TODAY is a sabbath to the LORD; TODAY you shall not find it': the today-word TRIPLED in one verse (asserted in-span: the readings hang the three meals of the Sabbath on the three todays, named-only) — the machine files the verse's rhetoric: rest argued from the calendar's own insistence; lo timtzauhu BA-SADE — the field emptied by decree: the first negative provision (what the LORD gives on six days He withholds as deliberately on the seventh — absence as signature).")])
V[26] = v("SIX_DAYS_AND_THE_SEVENTH", "Six days you shall gather it; and on the seventh day — a sabbath: it shall not be in it.",
  "six days you shall gather it", "and on the seventh day — a sabbath: it shall not be in it",
  "The week legislated.",
  [p("HOLDS(sheshet_yamim_tilqetuhu, t0)", (0,8),
    "THE WEEK. SHESHET YAMIM tilqetuhu — 'SIX DAYS you shall gather it' — u-va-yom ha-SHEVII shabat LO YIHYE-BO — 'and on the seventh, a sabbath: IT SHALL NOT BE': the creation-week's shape (Gen 2:2's six-and-one) re-cut in bread — the machine notes the formula's future: this exact six-and-the-seventh frame is the Decalogue's skeleton (20:9 armed: six days shall you labor — the manna teaching the commandment before the mountain speaks it); the readings on the double negative — no gathering AND nothing to gather — named-only.")])
V[27] = v("THEY_FOUND_NOTHING", "And it was on the seventh day, that some of the people went out to gather — and they found none.",
  "and it was on the seventh day, that some of the people went out to gather", "and they found none",
  "The second breach.",
  [p("HOLDS(yatzu_min_ha_am_lilqot, t0)", (0,8),
    "THE SECOND BREACH [EX16-13]. va-yehi ba-yom ha-shevii YATZU min-ha-am LILQOT — 'on the seventh day SOME OF THE PEOPLE went out TO GATHER' (min-ha-am — the partitive mercy: not the people, some of it — the machine notes the census-grammar of guilt narrowing since 16:20's anashim); ve-LO MATZAU — 'and they FOUND NONE': the second breach breaks against a kept field (the first breach spoiled the bread; the second finds the LORD keeping His own commandment — the field observes the Sabbath the gatherers do not); the Kitzur's gleaning-wire named: 'TWO are gleanings, THREE are not — two omers they gathered on the sixth; on the Sabbath they went out for the THIRD and found nothing' (the field-law of Peah read back into the manna-field: the wilderness keeping the corner-statutes before the Land exists).")])
V[28] = v("HOW_LONG_DO_YOU_REFUSE", "And the LORD said to Moses: How long do you refuse to keep My commandments and My laws?",
  "and the LORD said to Moses", "how long do you refuse to keep My commandments and My laws?",
  "The verdict; the test fails.",
  [dict(op="TEST", expr_en="TESTS += FAIL(anasenu, ha_yelekh_be_torati)", he_span=(4,9),
    prose="THE VERDICT. AD-ANA MEANTEM lishmor mitzvotai ve-torotai — 'HOW LONG do you REFUSE to keep My commandments and My laws?': THE TEST OF 16:4 RETURNS ITS FIRST VERDICT — FAIL (the corpus's second FAIL, Tier-A textual warrant: the oracle's own im-lo answered by the text's refusal-verb) — and the refusal-verb is PHARAOH'S (asserted at the build: the me'en-form here is Torah-unique in this plural, and the root is the throne's — 'he REFUSES to let the people go,' 7:14/10:3: the machine files the bitterest handover in the ledger: the verb of Egypt's king passing to Egypt's freedmen inside two chapters); ad-ANA — 'how long' (10:3's ad-matai to Pharaoh, ad-ana to Israel — the how-long file); and the plural MEANTEM aimed through Moses at the nation (the readings on the leader bundled with his people, named-only): TESTS ledger 1 FAIL — the verdict is DATA, and the next verse answers it with a gift.")])
V[29] = v("LET_NO_MAN_GO_OUT", "See, that the LORD has given you the Sabbath — therefore He gives you on the sixth day bread for two days; sit every man in his place: let no man go out of his place on the seventh day.",
  "see, that the LORD has given you the Sabbath — therefore He gives you on the sixth day bread for two days", "sit every man in his place: let no man go out of his place on the seventh day",
  "The Sabbath given; the boundary.",
  [dict(op=D, expr_en="DECLARE(YHWH, LET(al_yetze_ish_mi_meqomo))", he_span=(15,23),
    prose="THE BOUNDARY [EX16-10 CROWN]. REU ki-YHWH NATAN lakhem HA-SHABAT — 'SEE, that the LORD has GIVEN you the Sabbath': the Sabbath as GIFT (the give-verb doubled: natan the Sabbath, noten the double bread — the day and its groceries one grant; and the printed-authority file gains its station: 'books that write ET here are IN ERROR,' MS — the object-marker struck from the giving); SHEVU ish tachtav — 'SIT every man in his place'; AL-YETZE ish mi-meqomo ba-yom ha-shevii — 'LET NO MAN GO OUT of his place on the seventh day': the let-none-go-out adjacency Torah-UNIQUE (VERIFIED) — the corpus's first SPATIAL law: rest legislated as geometry — with the Kitzur's three courts named ('OF HIS PLACE — four cubits; the fugitive OF THE CITY — the Sabbath-limit; come-strike-them — the court flogs boundary-breaches from the Torah'): the card pushed — the machine notes the day acquiring its second dimension: 16:23 fenced its time, 16:29 fences its space.")])
V[30] = v("AND_THE_PEOPLE_RESTED", "And the people rested on the seventh day.",
  "and the people rested", "on the seventh day",
  "The card pops; the lean seventh.",
  [dict(op=R, expr_en="RESULT: HOLDS(al_yetze_ish_mi_meqomo, t1)", he_span=(0,3),
    prose="THE REST [EX16-02 CROWN — THE MARQUEE'S TWIN]. va-YISHBETU ha-am ba-yom HA-SHEVII — 'and the people RESTED on the seventh day': the boundary-card POPS on the four-word verse — and the verse is a double crown: the rest-verb in this form is Torah-UNIQUE (asserted at the build: Gen 2:2's va-yishbot was GOD's rest; 16:30 is the only 'and-they-rested' — THE FIRST HUMAN SABBATH in the corpus, performed by the nation entire), and the seventh-word is written LEAN — one of the Ramah's THREE lean sevenths in the whole Torah (VERIFIED census exact: the leaven-removal day 12:15, THIS FIRST REST, and the Jubilee's horn Lev 25:9 — the day the leaven goes, the day the people first stop, the day liberty is blown: the Torah's three great cessations sharing one thinned skeleton): the machine stamps the smallest verse in the chapter as its summit — creation's rest, on loan since Genesis 2, finally answered in kind.")])
V[31] = v("THE_HOUSE_NAMED_IT_MANNA", "And the house of Israel called its name Manna; and it was like coriander seed, white, and its taste like a wafer in honey.",
  "and the house of Israel called its name Manna", "and it was like coriander seed, white; and its taste like a wafer in honey",
  "The name written.",
  [dict(op="NAME", expr_en="name(ha-lechem) := Man", he_span=(0,5),
    prose="THE NAMING. va-yiqreu VET-YISRAEL et-shemo MAN — 'and the HOUSE OF ISRAEL called its name MANNA': the naming-verb spent by the nation (the corpus's first collective naming — not Moses, not the Name: the HOUSE names its bread), and the name IS the question (16:15's man hu — 'what is it?' — hardened into a noun: the only entity in the corpus named for the ignorance it caused; and the skeleton's own file asserted at the build: the same two letters open Eden's indictment — 'HAVE YOU [eaten] FROM the tree?' Gen 3:11 — and the craving's cry, Num 11:6: the what-bread of the wilderness written with the from-word of the first eating); ve-hu ke-zera GAD lavan — 'like coriander seed, white' (ke-zera's pointing per the Chizkuni, MS); ve-tamo ke-TZAPICHIT bi-devash — 'its taste like a WAFER IN HONEY': a second hapax for the same food (16:14's flake-word, 16:31's wafer-word — the vocabulary spent on the manna used once and retired, like the thing it describes).")])
V[32] = v("A_KEEPSAKE_FOR_GENERATIONS", "And Moses said: This is the thing which the LORD commanded: The fill of the omer of it in keeping for your generations — that they may see the bread which I fed you in the wilderness, when I brought you out from the land of Egypt.",
  "and Moses said: this is the thing which the LORD commanded: the fill of the omer of it in keeping for your generations", "that they may see the bread which I fed you in the wilderness, when I brought you out from the land of Egypt",
  "The Elijah initials.",
  [p("HOLDS(melo_ha_omer_le_mishmeret, t0)", (12,15),
    "THE KEEPSAKE [EX16-08 CROWN]. ze ha-davar asher tziva YHWH: MELO HA-OMER mimenu LE-MISHMERET le-dorotekhem — 'the FILL OF THE OMER in KEEPING FOR YOUR GENERATIONS': the manna made museum-piece by command (the corpus's first commanded RELIC — history curated in advance); LEMAAN YIRU ET HA-LECHEM — 'THAT THEY MAY SEE THE BREAD': and the purpose-clause signs itself (VERIFIED: the four words' initial letters are the letters of ELIJAH) — the Kitzur: 'to say it shall be KEPT UNTIL ELIJAH COMES': the jar's audience named in acrostic — the generations addressed include a prophet not yet born (the machine files the arc: the bread kept for the far end of history, its label already carrying the herald's name); asher HEEKHALTI etkhem ba-midbar — the feeding claimed in the first person: the exhibit's caption is the Name's own testimony.")])
V[33] = v("THE_JAR", "And Moses said to Aaron: Take one jar, and put there the fill of the omer of manna; and lay it before the LORD, in keeping for your generations.",
  "and Moses said to Aaron: take one jar, and put there the fill of the omer of manna", "and lay it before the LORD, in keeping for your generations",
  "The hapax vessel.",
  [dict(op=D, expr_en="DECLARE(moshe, LET(qach_tzintzenet_achat))", he_span=(4,11),
    prose="THE VESSEL [EX16-12 CROWN]. qach TZINTZENET achat — 'take ONE JAR': the jar-word an absolute Torah-HAPAX (VERIFIED) — the vessel that must outlive its era named once, like both words for its contents (the hapax-cluster the machine tracks: mechuspas, tzapichit, tzintzenet — the manna surrounded by single-use vocabulary); VE-HANACH oto lifne YHWH — 'and LAY IT before the LORD': the lay-word's Masorah-pair named — GIDEON'S ROCK (where the fire consumed the meal of itself): the Kitzur — 'as there it was consumed of itself, so the manna was ABSORBED IN THE LIMBS' (one verb for the two self-consuming meals); the card pushed to AARON — the relay of 16:9 reversed into custody: the speaker becomes the keeper.")])
V[34] = v("BEFORE_THE_TESTIMONY", "As the LORD commanded Moses, so Aaron laid it before the Testimony, in keeping.",
  "as the LORD commanded Moses", "and Aaron laid it before the Testimony, in keeping",
  "The card pops; the anachrony.",
  [dict(op=R, expr_en="RESULT: HOLDS(qach_tzintzenet_achat, t1)", he_span=(5,9),
    prose="THE PLACEMENT. ka-asher tziva YHWH el-moshe — the obedience-formula; va-YANICHEHU AHARON lifne HA-EDUT le-mishmaret — 'and AARON LAID IT before THE TESTIMONY' (asserted): the card POPS — before an ark that does not yet exist (the Testimony named eight chapters before its pattern is shown, 25:16 armed — the readings on the verse written from the Tabernacle's vantage, named-only): the machine files the narrative's second forward-leaning seam (with 16:35's forty years): the manna-chapter keeps its receipts in a future tense the grammar hides.")])
V[35] = v("FORTY_YEARS", "And the sons of Israel ate the manna forty years, until their coming to an inhabited land; the manna they ate, until their coming to the edge of the land of Canaan.",
  "and the sons of Israel ate the manna forty years, until their coming to an inhabited land", "the manna they ate, until their coming to the edge of the land of Canaan",
  "The longest receipt.",
  [p("HOLDS(akhlu_et_ha_man_arbaim_shana, t0)", (0,11),
    "THE RETROSPECT. u-vene yisrael akhlu et-HA-MAN ARBAIM SHANA — 'and the sons of Israel ate the manna FORTY YEARS': the corpus's longest forward look narrated as past (the verse stands at the manna's first week and speaks from beyond its last — the readings on Moses' hand in the line, named-only; Joshua's cessation named, outside the Torah: the day after the Passover of Gilgal); ad-boam el-ERETZ NOSHAVET... el-qetze eretz KENAAN — the doubled until (an inhabited land; the edge of Canaan — the readings split the two arrivals, named-only): the machine files the chapter's closing symmetry: it opened on a dated day (16:1) and closes on a measured era — the manna bracketed by calendar at both ends.")])
V[36] = v("THE_OMER_GLOSS", "And the omer — a tenth of the efa it is.",
  "and the omer — a tenth of the efa", "it is",
  "The metrological footnote.",
  [p("HOLDS(ve_ha_omer_asirit_ha_efa, t0)", (0,3),
    "THE GLOSS [EX16-12]. ve-HA-OMER asirit HA-EFA hu — 'and the omer — a TENTH OF THE EFA it is': the corpus's first metrological footnote (the text glossing its own unit for readers who no longer measure in omers — the machine notes the audience-seam: the verse presumes the generations of 16:32-33, not the gatherers); and the Kitzur reads the juxtaposition: 'the OMER beside the manna-chapter — a hint that they would eat the manna UNTIL THEY OFFERED THE OMER' (the measure-word naming the offering whose arrival ends the miracle, Josh 5 named): the chapter closes by weighing its bread in the unit of its own expiry.")])

# ---- scenarios ----------------------------------------------------------
BASE = "no test, no name."
TFAIL = "TESTS += FAIL(anasenu, ha_yelekh_be_torati);"
REG = "REGISTRY: ha-lechem->Man (1 write)"
D1s = "LET(ve_laqtu_devar_yom_be_yomo) pushed and OPEN;"
D2s = "LET(ve_hekhinu_mishne) pushed and OPEN;"
D3s = "LET(qirvu_lifne_YHWH) pushed and OPEN;"
D5s = "LET(al_yoter_mimenu_ad_boqer) pushed and OPEN;"
D6s = "LET(et_ha_odef_hanichu_le_mishmeret) pushed and OPEN;"
D7s = "LET(al_yetze_ish_mi_meqomo) pushed and OPEN;"
D8s = "LET(qach_tzintzenet_achat) pushed and OPEN;"
expects = {}
for vs in (1, 2, 3):
    expects[vs] = [BASE]
expects[4] = [D1s, BASE]
for vs in (5, 6, 7, 8):
    expects[vs] = [D1s, D2s, BASE]
expects[9] = [D1s, D2s, D3s, BASE]
for vs in range(10, 17):
    expects[vs] = [D1s, D2s, BASE]
for vs in (17, 18):
    expects[vs] = [D2s, BASE]
for vs in (19, 20, 21):
    expects[vs] = [D2s, D5s, BASE]
expects[22] = [D5s, BASE]
expects[23] = [D5s, D6s, BASE]
for vs in (24, 25, 26, 27):
    expects[vs] = [D5s, BASE]
expects[28] = [D5s, TFAIL]
expects[29] = [D5s, D7s, TFAIL]
expects[30] = [D5s, TFAIL]
for vs in (31, 32):
    expects[vs] = [D5s, TFAIL, REG]
expects[33] = [D5s, D8s, TFAIL, REG]
for vs in (34, 35, 36):
    expects[vs] = [D5s, TFAIL, REG]
titles = {
    1: "into the wilderness of Sin", 2: "the whole congregation murmurs",
    3: "the flesh-pots", 4: "bread from heaven", 5: "double on the sixth",
    6: "evening, and you shall know", 7: "morning, and the glory",
    8: "not against us", 9: "draw near", 10: "the glory in the cloud",
    11: "the frame", 12: "I have heard", 13: "quail and dew",
    14: "fine as frost", 15: "what is it", 16: "an omer a head",
    17: "great and small", 18: "no lack, no surplus",
    19: "leave none till morning", 20: "worms and wrath",
    21: "morning by morning", 22: "the sixth day double",
    23: "tomorrow is the rest", 24: "it did not stink", 25: "eat it today",
    26: "six days and the seventh", 27: "they found nothing",
    28: "how long do you refuse", 29: "let no man go out",
    30: "and the people rested", 31: "the house named it Manna",
    32: "a keepsake for generations", 33: "the jar",
    34: "before the Testimony", 35: "forty years", 36: "the omer gloss",
}

steps, scenarios = [], []
for i, vs in enumerate(sorted(V), 1):
    spec = V[vs]
    steps.append(unitgen.build_step(db, "Exod", "Exod", 16, vs, i, spec))
    scenarios.append(unitgen.scenario_for(
        db, "Exod", 16, vs, "S%d" % i,
        "after STEP_Ex_16_%d — %s" % (vs, titles[vs]),
        spec["en"].replace("[EN-AID] ", ""), expects[vs]))

ttl_he, ttl_tr = unitgen.join_tokens(unitgen.verse_tokens(db, "Exod", 16, 4)[7:10], strip_accents=False)

META = '''# =============================================================================
# LOGIC UNIT: Exodus 16:1-36 — the manna, the murmurings, the test's first
#             verdict, and the first human Sabbath
# FORWARD ERA unit #30 — derived 2026-08-09 (oral layer in-pipeline; review waived)
# Run FWD-7 block 1.
# =============================================================================
# Experimental model — not binding religious law.

meta:
  id: "exo_16_manna_and_sabbath"
  title_en: "The manna and the Sabbath (16:1-36)"
  title_he: %s
  title_he_translit: "%s"
  title_he_en: "'bread from the heavens'"
  book_he: שְׁמוֹת
  book_he_translit: Shemot
  book_en: Exodus
  refs: "16:1-36"
  unit_span_planned: "16:1-36"
  data_paths_he:
  - "Data/Exod.xml"
  status: frozen
  draft_note_en: >
    DERIVED 2026-08-09 · FORWARD ERA unit #30 (run FWD-7 block 1;
    Exod 1-16 continuous behind it). Span: 16:1-36, whole chapter:
    36 verses (SNAPSHOT-verified; 16:2, 16:11, 16:30, 16:36
    without etnachta; TWO ketiv-and-qere pairs in-span, BOTH on
    the murmur-verb — 16:2 and 16:7, adjacent-token convention,
    gen_59 precedent). Oral layer IN-PIPELINE: manifest 13/13
    VERIFIED, zero FAILED — see oral_audit_note_en.

    MACHINE PROFILE. SEVEN DECLAREs, SIX RESULTs, TWO EVENTS,
    ONE NAME, ONE TEST-FAIL. The command-densest block since
    exo_12, and the corpus's first LAW-LOOP chapter: five of the
    seven cards pop in-span on narrated compliance (gather-daily
    16:4→16:17 va-yaasu-khen; prepare-double 16:5→16:22;
    draw-near 16:9→16:10 as-Aaron-spoke; Sabbath-keeping
    16:23→16:24 as-Moses-commanded; the jar 16:33→16:34
    as-the-LORD-commanded), one stands as PERPETUAL DAILY LAW
    (leave-none-over 16:19 — breached its first night at 16:20,
    kept thereafter 16:21, excepted by the Sabbath-law 16:23),
    and the boundary-card (16:29) pops at 16:30 on the FIRST
    HUMAN SABBATH. TWO EVENTS: the glory's first public
    appearance (16:10 — summoned by a bread-complaint) and the
    provision (16:13). THE TEST OF 16:4 (15:25's armed nisahu
    PAYS: lemaan anasenu, ha-yelekh be-torati im-lo) RETURNS
    THE CORPUS'S SECOND FAIL at 16:28 — Tier-A textual warrant:
    ad-ana MEANTEM (the refuse-verb, Torah-unique in this
    plural, asserted — PHARAOH'S verb handed to Israel;
    verdicts are data). ONE NAME: the house of Israel names
    the bread MAN (16:31 — the corpus's first collective
    naming; REGISTRY 1). The know-ledger opens Israel's
    account (16:6 hotzi, 16:12 ani-YHWH-elohekhem — 6:7's
    promise paid at supper). MACHINE EVIDENCE asserted at the
    build: the rain-causative's Torah-three (flood Gen 7:4 →
    hail 9:18 → bread 16:4); the wrath-verb's five (Pharaoh
    Gen 40:2 → Moses' first anger 16:20 → Lev 10:16, Num
    31:14, Deut 1:34); va-yishbetu Torah-unique (God's rest
    Gen 2:2, the people's here); the manna-skeleton's seven
    stations incl. Eden's from-question (Gen 3:11). Queue at
    close: ONE OPEN in-unit (leave-none-over — perpetual
    daily law of the manna era) plus the standing opens.
    REGISTRY 1; TESTS 1 FAIL.

    CARE-POINTS: the dual-written murmur (ketiv/qere twice,
    both on the complaint-verb); the unordered double (16:22
    complies before 16:23 explains — miracle ahead of law);
    the same act rot-then-religion (16:20 vs 16:24 — keeping
    manna overnight cursed Thursday, commanded Friday); the
    partitive breaches (anashim 16:20, min-ha-am 16:27 —
    guilt narrowing); the three todays (16:25); the
    hapax-cluster (mechuspas, tzapichit, tzintzenet); the two
    forward-leaning seams (the Testimony 16:34 before 25:16;
    the forty years 16:35). WATCHLIST ARMS: 17:1-7 (Rephidim
    — the thirst-cycle's second station, from Sin by
    journeys), 20:8-11 (the Sabbath commanded at Sinai — the
    manna's six-and-one frame scaled to law), 25:16 (the
    Testimony receives its ark), Num 11 (the quail's dark
    twin, VERIFIED pair; the craving), Deut 8:3 (man-by-man —
    the manna moralized). Outside-Torah names (named-only):
    Josh 5:12 (the manna ceases at the omer), 2 Kgs 4:44
    (Elisha's left-over blessing), Ezek 10:4 (the glory
    lifts), Job 21:26 (the worm-covered grave), Judg 6:20-21
    (Gideon's rock).
  oral_audit_note_en: >
    ORAL AUDIT 2026-08-09 (IN-PIPELINE, forward era; manifest
    logic/oral_audit/manifests/exo_16_manna_and_sabbath_claims.json
    13/13 VERIFIED, zero FAILED; record
    logic/oral_audit/AUDIT_exo_16_2026-08-09.md). CROWNS
    (chain-attested + DB-verified). THE UNIQUE MURMURINGS
    [EX16-01, MS on 16:12 + Lekach Tov — THE MARQUEE]: תלונת
    ("murmurings") in a spelling with NO TWIN in the Torah
    (census 1, checked) — the PRINTED MASORAH'S pair-note
    ruled AN ERROR by MS (printed-authority file); Lekach
    Tov: the lean letter = "diminished from their merits,"
    and the frame's mercy: "all complaints are as one — and
    though they murmur, THEY ARE MY SONS." THE THREE LEAN
    SEVENTHS [EX16-02, MS on 16:30 citing the Ramah]: השבעי
    ("the seventh") lean exactly THREE times in the Torah
    (census exact, checked): the leaven-removal day (12:15),
    THE FIRST HUMAN SABBATH (16:30), and the Jubilee's horn
    (Lev 25:9) — the three great cessations on one thinned
    skeleton. THE QUAIL PAIR [EX16-03, KB + MS + Yoma]: השלו
    ("the quail") exactly twice (here + Num 11:32 the graves
    of craving) — "here too it ceased, and they murmured
    again"; lean-yod per the Ramah; Yoma: the righteous eat
    it in peace, to the wicked it is thorns. THE LEFT-OVER
    AND THE LIFTINGS [EX16-04, KB + MS on 16:20]: ויותרו
    ("and they left over") Torah-unique — Elisha's twin: by
    the word a blessing, against the word a curse; וירם
    ("and it bred/lifted") with the THREE-DOT vowel, "in our
    Masorah NONE OTHER" — pointed apart from the GLORY's
    lifting (Ezek 10:4); the heart that lifts, lifts worms.
    THE WORMLESS SABBATH [EX16-05, KB on 16:24]: ורמה ("and
    no worm") Torah-unique — Job's grave its twin: the worm
    powerless over the Sabbath and the manna-eaters. THE 248
    [EX16-06, KB on 16:14]: מחספס ("flake-like") an absolute
    hapax = 248 (asserted) — "absorbed in the 248 limbs."
    THE ALPHABET-VERSE [EX16-07, KB on 16:16/4/5]: all
    TWENTY-TWO letters stand in the omer-verse (asserted) —
    "whoever upholds the Torah is fed without toil, like the
    manna-eaters"; "the Torah was given only to the eaters
    of the manna" (16:4); everything of the Sabbath DOUBLE
    (16:5). THE ELIJAH INITIALS [EX16-08, KB on 16:32]: the
    initials of למען יראו את הלחם ("that they may see the
    bread") = the letters of אליה (ELIJAH, checked) — "kept
    until Elijah comes." THE FENCE-ORDER [EX16-09, KB on
    16:23]: שבתון ("solemn rest") before שבת ("sabbath")
    UNIQUELY here (adjacency checked; Vayaqhel reverses) —
    "we add from the weekday onto the holy at entry and
    exit." THE BOUNDARY [EX16-10, KB on 16:29]: אל יצא
    ("let none go out") adjacency Torah-unique (checked) —
    four cubits, the Sabbath-limit, the court's lash: rest
    as geometry. SIN AND THE BUSH [EX16-11, KB + MS on
    16:1]: סין = הסנה ("the bush," 120=120, asserted); Sinai
    = Sin + the yod of the ten utterances; the station-word's
    Torah-four (checked); every Sin full, every Tzin lean
    (MS). THE JAR [EX16-12, KB on 16:33/36]: צנצנת ("jar")
    an absolute hapax (checked); והנח ("and lay it") —
    Gideon's rock: two self-consuming meals; the omer-gloss
    juxtaposed — manna until the OMER is offered (Josh 5).
    THE LETTER-FILE [EX16-13, MS + KB]: kol-adat's kaf
    dageshed (16:2, checked); the murmur dual-written twice
    (16:2, 16:7 — ketiv/qere both times); תלונת's nun
    dageshed for the swallowed letter; לגלגלת ("a head") —
    both gimels dageshed (checked at the build); no
    lengtheners in 16:18's he's; ונמס ("it melted") pausal —
    the grammarians' divergence dual-tracked; כזרע ("like
    seed") per the Chizkuni; books that add את (the
    object-marker) to the Sabbath-giving of 16:29 "are IN
    ERROR" (printed-authority); בשמעו three
    (the just complaint heard); לשבע four (fish free even in
    Egypt); the clouds by AARON'S MERIT (16:10).
  owner_language_note: >
    English for reading only. Hebrew is the derivation source.
  oral_policy_note_en: >
    Written trees first. Dual-track Oral only when named; never
    silent-merge.
  tree_derive_version: logic_derived_v1
  tree_derive_phase: "FWD-30"
  confidence_overall: "structure tested; oral layer verified 13/13"
  genre: "provision_law_fsm"
  build_track: exodus_stack
  depends_on: exo_15_the_song_and_marah
  depends_note_en: >
    Depends for PATTERN only (the murmur adds Aaron on schedule;
    Marah's armed test pays at 16:4; the statute-station's law
    deepens to a code). Standalone machine. Exod 1-16 continuous,
    92 frozen units.
''' % (ttl_he, ttl_tr)

DLOG = '''derivation_log:
  - step: A
    name_en: "Block choice"
    comment: >
      FORWARD ERA run 7, block 1 (owner: "do one more block").
      Canon continuation: Exod 16:1-36 — the manna-chapter, whole.
    confidence: established
  - step: B
    name_en: "Span + source + conventions"
    comment: >
      SNAPSHOT prestage: 36 verses; 16:2, 16:11, 16:30, 16:36
      without etnachta. TWO ketiv/qere pairs in-span, both on the
      murmur-verb (16:2, 16:7 — adjacent-token convention).
      Volitive census: seven real pushes (16:4 gather-daily, 16:5
      prepare-double, 16:9 draw-near, 16:19 leave-none, 16:23
      keep-surplus, 16:29 boundary, 16:33 the jar); 16:3's
      death-wish is quoted-optative (no push); 16:25-26's
      eat-today/six-days folds into the standing frame.
    confidence: established
  - step: C
    name_en: "Machine structure"
    comment: >
      7D/6R/2E/1N/1 TEST-FAIL. Five cards pop on narrated
      compliance-formulas; leave-none-over stands as perpetual
      daily law (breached 16:20, kept 16:21); the boundary pops
      on the first human Sabbath (16:30, va-yishbetu
      Torah-unique asserted). The glory-event (16:10) and the
      provision-event (16:13). The 16:4 test returns FAIL at
      16:28 on the text's own refuse-verb (meantem
      Torah-unique, asserted — Pharaoh's verb handed on). The
      house names the manna (16:31, REGISTRY 1). Asserted
      machine evidence: mamtir's flood-hail-bread three; the
      wrath-verb five; the manna-skeleton's seven stations.
    confidence: tested
  - step: D
    name_en: "Oral scan (in-pipeline)"
    comment: >
      Local mirror only (zero fetches): Minchat Shai on Exod 16
      (20 notes) + Kitzur Baal HaTurim on Exod 16 (21 notes).
      Manifest 13 rows: 13 VERIFIED / 0 FAILED / 0 UNCHECKABLE,
      first run. The unique murmurings (printed Masorah
      corrected); the three lean sevenths (the Ramah's census
      exact); the quail pair; the left-over/liftings file; the
      wormless Sabbath; the 248; the alphabet-verse; the Elijah
      initials (initial_letters check); the fence-order; the
      boundary; Sin=the-bush; the jar; the letter-file.
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
      status: frozen 2026-08-09 on green mechanical gates (forward-era
      law). Oral layer in-pipeline. Changes require a new derive pass,
      not silent edits. Exod 1-16 continuous.
    confidence: established
'''

unitgen.emit_unit(META, DLOG, steps, scenarios, "logic/units/exo_16_manna_and_sabbath.yaml")
print("wrote logic/units/exo_16_manna_and_sabbath.yaml —", len(steps), "steps,", len(scenarios), "scenarios")
