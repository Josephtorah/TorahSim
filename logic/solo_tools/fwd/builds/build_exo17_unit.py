#!/usr/bin/env python3
"""Author exo_17_massah_and_amalek (Exod 17:1-16) — forward-era unit #31 (run FWD-8 block 1).
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
assert census("תנסון") == [("Exod", 17, 2)]                                    # the test-verb, unique
assert census("ברפידים") == [("Exod", 17, 1)]                                  # full at the arrival
assert census("מרפידים") == [("Exod", 19, 2)]                                  # full at the departure
assert census("ויחלש") == [("Exod", 17, 13)]                                   # the weaken-verb, unique
assert census("וחור") == [("Exod", 17, 10), ("Exod", 17, 12), ("Exod", 24, 14)]  # Hur's whole career
assert census("למים") == [("Exod", 17, 3), ("Gen", 1, 6)]                       # thirst + the creation-division
assert census("מדר") == [("Exod", 17, 16)]                                     # from-generation, lean, unique
assert census("זכרון")[0] == ("Exod", 17, 14)                                  # the memorial's first station
assert (hp(17, 6, 14), hp(17, 6, 15), hp(17, 6, 16)) == ("ויעש", "כן", "משה")   # Moses did so
assert tuple(hp(17, 10, i) for i in range(6)) == ("ויעש", "יהושע", "כאשר", "אמר", "לו", "משה")  # Joshua's compliance
assert tuple(hp(17, 7, i) for i in range(5)) == ("ויקרא", "שם", "המקום", "מסה", "ומריבה")  # the double name
assert tuple(hp(17, 15, i) for i in range(3, 7)) == ("ויקרא", "שמו", "יהוה", "נסי")  # the altar named
assert hp(17, 12, 2) == "כבדים"                                                # the heavy hands (the kaved-root)
assert hp(17, 12, 21) == "בא"                                                  # the lean sun-coming
assert hp(17, 8, 5) == "ברפידם"                                                # lean at the attack
assert [hp(17, 14, i)[0] for i in range(6, 10)] == list("זבוב")                # the fly initials
assert all(len(hp(17, 16, i)) == 2 for i in range(1, 6))                       # five two-letter words
G = {"א":1,"ב":2,"ג":3,"ד":4,"ה":5,"ו":6,"ז":7,"ח":8,"ט":9,"י":10,"כ":20,"ך":20,
     "ל":30,"מ":40,"ם":40,"נ":50,"ן":50,"ס":60,"ע":70,"פ":80,"ף":80,"צ":90,"ץ":90,
     "ק":100,"ר":200,"ש":300,"ת":400}
g = lambda s: sum(G[c] for c in s if c in G)
assert g("מחה") + g("אמחה") == g("זה") + g("המן") == 107                        # the blot = this-is-Haman
assert 10 + g("יד") == g("דויד") == 24                                          # the yod + the hand = David
assert g("מדר") + g("דר") == g("לימי") + g("משיח") == 448                       # to the days of Messiah

P = "PRECONDITION_STATE"
D = "DECLARE"
R = "RESULT"
E = "EVENT"

def v(op, en, left, right, comment, ops):
    return dict(op=op, en=en, left_en=left, right_en=right, comment=comment, operators=ops)

def p(expr, span, prose):
    return dict(op=P, expr_en=expr, he_span=span, prose=prose)

V = {}
V[1] = v("NO_WATER_IN_REPHIDIM", "And all the congregation of the sons of Israel journeyed from the wilderness of Sin, by their journeys, according to the mouth of the LORD; and they camped in Rephidim — and there was no water for the people to drink.",
  "and all the congregation of the sons of Israel journeyed from the wilderness of Sin, by their journeys, according to the mouth of the LORD", "and they camped in Rephidim, and there was no water for the people to drink",
  "The dry station; the full spelling.",
  [p("HOLDS(va_yachanu_bi_refidim_ve_en_mayim, t0)", (11,16),
    "THE STATION [EX17-06]. va-yisu... mi-midbar-SIN le-MASE-HEM al-PI YHWH — 'by their JOURNEYS, according to the MOUTH of the LORD': the itinerary marches on orders (the machine notes the bitter arithmetic the verse sets up: the dry camp is REACHED BY OBEDIENCE — the route to no-water was commanded); va-yachanu BI-REFIDIM — the station-name FULL-spelled at the arrival (asserted at the build: the arrival 17:1 and the departure 19:2 both full; the name thins only where the enemy lands, 17:8) — ve-EN MAYIM lishtot ha-am — 'and NO WATER for the people to drink': the thirst-file reopens (15:22's three dry days, 15:27's twelve springs — the cycle's third station arrives at zero): exo_16 tested with too much bread kept; 17 tests with no water at all.")])
V[2] = v("GIVE_US_WATER", "And the people quarreled with Moses, and said: Give us water, that we may drink. And Moses said to them: Why do you quarrel with me? Why do you test the LORD?",
  "and the people quarreled with Moses, and said: give us water, that we may drink", "and Moses said to them: why do you quarrel with me? why do you test the LORD?",
  "The demand pushed; the test inverted.",
  [dict(op=D, expr_en="DECLARE(ha_am, LET(tenu_lanu_mayim))", he_span=(5,8),
    prose="THE DEMAND [EX17-01 CROWN]. va-YAREV ha-am im-moshe — 'and the people QUARRELED with Moses' (the quarrel-verb: not murmuring now — litigation); TENU-lanu MAYIM ve-nishte — 'GIVE us water, that we may drink': the card pushed BY THE PEOPLE at the throne's officer (the corpus's first imperative demand from below — 15:24 asked what-shall-we-drink ABOUT Moses; 17:2 commands GIVE at him; and the printed-authority file opens here: books reading tena for TENU struck, MS); ma TERIVUN imadi — the quarrel-verb Torah-unique (VERIFIED; the Kitzur's Scripture-three: Gideon's Baal-quarrel, Job — 'whoever quarrels with his master quarrels with the Holy One'); ma TENASUN et-YHWH — 'why do you TEST the LORD?': the test-verb equally alone (asserted) — the machine files the INVERSION crown-side: 16:4's lemaan anasenu (I test THEM) answered within a chapter by tenasun (they test HIM) — the examiner's verb seized by the examined; both verbs lean, the eight double-ma verses named (MS).")])
V[3] = v("WHY_DID_YOU_BRING_US_UP", "And the people thirsted there for water, and the people murmured against Moses, and said: Why is this — you brought us up from Egypt, to kill me and my sons and my cattle with thirst?",
  "and the people thirsted there for water, and the people murmured against Moses", "and he said: why is this — you brought us up from Egypt, to kill me and my sons and my cattle with thirst?",
  "The four-station accusation-file opens.",
  [p("HOLDS(va_yalen_ha_am_al_moshe, t0)", (4,7),
    "THE THIRST [EX17-02 CROWN]. va-yitzma sham ha-am LA-MAYIM — 'and the people THIRSTED there for water': the thirst-word's Torah-pair (VERIFIED at the build: here and the CREATION-DIVISION, 'between waters and waters,' Gen 1:6 — the word that first sundered the waters returns where there are none; the Kitzur's Scripture-five named: Elisha's healed spring, Isaiah's ho-every-thirsty, Jeremiah's drought, Amos's famine-of-hearing); va-YALEN ha-am — the murmur-verb again (16's chapter-verb carried forward, singular now); lama ze HEELITANU mi-mitzrayim — 'why is this — you BROUGHT US UP from Egypt': the accusation-verb's Torah-FOUR (VERIFIED census exact): Rephidim, KORACH ('the very same men,' the Kitzur's Masorah-wire), MERIBAH-KADESH, the SERPENTS — the forty-year complaint-file opened here under one verb; le-hamit OTI ve-et-BANAI ve-et-MIQNAI — 'to kill ME and MY SONS and MY CATTLE': the machine notes the grammar's narrowing — the congregation's plural grievance collapsing into one man's household inventory (each speaker suddenly alone with his children and his herd).")])
V[4] = v("THEY_WILL_STONE_ME", "And Moses cried to the LORD, saying: What shall I do for this people? Yet a little — and they will stone me.",
  "and Moses cried to the LORD, saying: what shall I do for this people?", "yet a little — and they will stone me",
  "The cry; the armed receipt.",
  [p("HOLDS(od_meat_u_seqaluni, t0)", (9,11),
    "THE CRY [EX17-03 CROWN]. va-YITZAQ moshe el-YHWH — 'and Moses CRIED to the LORD': THE ARMED CRY PAYS (the watchlist's wire from the sea: 14:10's people-cry and 15:25's Marah-cry now Moses' own — the third station of the leader crying the people's verb); ma eese la-AM ha-ze — 'what shall I do for THIS people': the question of office (5:22's why-have-You-dealt-ill matured into operational despair); OD MEAT u-SEQALUNI — 'YET A LITTLE — and they will STONE ME': the stoning-word Torah-unique (VERIFIED) with MS's letter-law: lean after the lamed, final yod WRITTEN AND READ ('all precise texts' — the Sura tradition's vav rejected, the Ramah ruling): the corpus's first named lynching-threat, priced by its own spelling to a single exact skeleton — the machine files the escalation: 16 murmured about menus; 17 reaches for rocks.")])
V[5] = v("PASS_BEFORE_THE_PEOPLE", "And the LORD said to Moses: Pass before the people, and take with you of the elders of Israel; and your staff, with which you struck the Nile, take in your hand — and go.",
  "and the LORD said to Moses: pass before the people, and take with you of the elders of Israel", "and your staff, with which you struck the Nile, take in your hand — and go",
  "The staff's resume; the card pushed.",
  [dict(op=D, expr_en="DECLARE(YHWH, LET(avor_lifne_ha_am_ve_hikita))", he_span=(4,10),
    prose="THE ORDER. AVOR lifne ha-am — 'PASS BEFORE the people': the answer to stone-fear is proximity (the readings: walk past them and see — named-only); ve-qach itkha mi-ZIQNE yisrael — the elders taken as witnesses (the protocol needs a bench); u-MAT-KHA asher HIKITA BO et-ha-YEOR — 'and your STAFF, WITH WHICH YOU STRUCK THE NILE': the corpus's first TOOL-RESUME — the instrument cited by its own service record (7:20's blood-strike recalled at the water-lack: the machine notes the pointed symmetry: the staff that turned water undrinkable is fetched to make water drinkable — one rod, both valves); QACH be-yadkha ve-HALAKHTA — 'take it in your hand, and GO': the card pushed with its kit-list.")])
V[6] = v("THE_ROCK_AT_HOREB", "Behold, I stand before you there on the rock at Horeb; and you shall strike the rock, and water shall come out of it, and the people shall drink. And Moses did so before the eyes of the elders of Israel.",
  "behold, I stand before you there on the rock at Horeb; and you shall strike the rock, and water shall come out of it, and the people shall drink", "and Moses did so before the eyes of the elders of Israel",
  "The Presence on the rock; both cards pop.",
  [dict(op=R, expr_en="RESULT: HOLDS(avor_lifne_ha_am_ve_hikita, t1)", he_span=(14,16),
    prose="THE COMPLIANCE [EX17-04 CROWN]. hineni OMED lefanekha sham AL-HA-TZUR be-CHOREV — 'behold, I STAND before you there ON THE ROCK at Horeb': the Presence takes a position ON the thing to be struck (the machine files the staggering routing: the im-ayin of 17:7 — is the LORD in our midst? — is answered BEFORE it is asked: He is standing on the rock, and the rock is about to take the blow; the readings on the mercy of that geometry, named-only) — with Ben Asher's own stroke on the preposition (VERIFIED: the AL bound to its rock by the binder-stroke, the little lengthener in-token — MS: 'so it is for Ben Asher'); ve-hikita VA-TZUR ve-yatzu mimenu MAYIM — strike, and water; va-YAAS KEN moshe — 'and Moses DID SO' (asserted): the card POPS on the compliance-formula, le-ENE ziqne yisrael — before the bench that was convened for it."),
   dict(op=R, expr_en="RESULT: HOLDS(tenu_lanu_mayim, t1)", he_span=(9,13),
    prose="THE DEMAND PAID. ve-SHATA ha-am — 'and the people shall DRINK': the give-us-water card POPS with the protocol (the machine notes the terse ledger: the drinking itself is never narrated — the corpus closes the demand on the command's own warranty, the water leaving the rock offstage: 15:25's sweetened water was tasted in-verse; 17:6's rock-water is banked sight-unseen).")])
V[7] = v("MASSAH_AND_MERIBAH", "And he called the name of the place Massah and Meribah, for the quarrel of the sons of Israel, and for their testing the LORD, saying: Is the LORD in our midst, or not?",
  "and he called the name of the place Massah and Meribah", "for the quarrel of the sons of Israel, and for their testing the LORD, saying: is the LORD in our midst, or not?",
  "The double name; the or-not pair.",
  [dict(op="NAME", expr_en="name(maqom_refidim) := Masa_u_Meriva", he_span=(0,4),
    prose="THE NAMING [EX17-05 CROWN]. va-yiqra shem ha-maqom MASA u-MERIVA — 'and he called the name of the place TESTING-AND-QUARREL': the corpus's first DOUBLE place-name (Mara carried one sin; Rephidim is filed under two — the site indicted on both counts of 17:2's double question, ma terivun / ma tenasun: the name is the charge sheet); al-RIV bene yisrael ve-al NASOTAM et-YHWH — the two counts recited in the deed; lemor ha-YESH YHWH be-qirbenu IM-AYIN — 'is the LORD in our midst — OR NOT?': the or-not question in its long pausal form stands exactly TWICE in the Torah (VERIFIED): here and the SPIES' is-there-wood (Num 13:20) — the Kitzur running both to WAR ('because they said is-the-LORD-in-our-midst-or-not, AMALEK CAME'): the machine seals the mirror: 16:4's im-lo (will they walk in My law, OR NOT) is handed back as im-ayin (is He among us, OR NOT) — the test-grammar reversed on the Tester, and the next verse is the invoice.")])
V[8] = v("AMALEK_COMES", "And Amalek came, and fought with Israel in Rephidim.",
  "and Amalek came", "and fought with Israel in Rephidim",
  "The war-event; the thinned name.",
  [dict(op=E, expr_en="milchemet_amaleq(e1); Agent(e1, amaleq); Theme(e1, yisrael)", he_span=(0,5),
    prose="THE ATTACK [EX17-06 CROWN]. va-YAVO AMALEQ — 'and AMALEK CAME': THE EVENT — the corpus's first pitched battle against Israel (Egypt drowned without Israel lifting a hand, 14:14 'the LORD will fight for you'; Amalek must be fought — the covering fire has an edge, and the machine opens the WAR-LEDGER on the far side of it); va-yilachem im-yisrael BI-REFIDIM — the station-name written LEAN at the attack (VERIFIED: the thin spelling stands here and in the itinerary's memorial of this camp, Num 33:14 — while the arrival 17:1 and departure 19:2 write it full): the Kitzur reads the missing letter: REFIDIM = REFU YADAYIM, 'they WEAKENED THEIR HANDS from the commandments, therefore Amalek came' (the tradition's own arithmetic-face named) — the name slackens in the verse where the enemy lands, and the chapter will answer the slack hands with raised ones.")])
V[9] = v("CHOOSE_US_MEN", "And Moses said to Joshua: Choose us men, and go out, fight against Amalek; tomorrow I stand on the top of the hill, and the staff of God in my hand.",
  "and Moses said to Joshua: choose us men, and go out, fight against Amalek", "tomorrow I stand on the top of the hill, and the staff of God in my hand",
  "Joshua's debut; the card pushed.",
  [dict(op=D, expr_en="DECLARE(moshe, LET(bechar_lanu_anashim_ve_tze))", he_span=(4,9),
    prose="THE COMMISSION [EX17-07 CROWN]. va-yomer moshe el-YEHOSHUA — 'and Moses said to JOSHUA': THE SUCCESSOR'S DEBUT — unintroduced, unpatronymed, no office (the corpus meets the man who will end the book of its books mid-battle-order: the machine files the entrance-class with Hur's, one verse down); BECHAR-lanu anashim VE-TZE hilachem ba-amaleq — 'choose us men and GO OUT, fight': the card pushed — and the go-out imperative stands exactly TWICE in the Torah (VERIFIED): Moses to Joshua here and ISAAC TO ESAU ('go out to the field and hunt me game,' Gen 27:3) — the Kitzur: 'out BEYOND THE CLOUDS' (the battle is outside the cover); the corpus adds the pair's unnamed edge: the verb that sent Esau hunting sends Israel against Esau's GRANDSON (Amalek son of Eliphaz son of Esau, Gen 36:12) — one imperative, the first feud and its farthest descendant; machar anokhi NITZAV al-rosh ha-giva u-MATE ha-ELOHIM be-yadi — 'tomorrow I STAND on the hilltop, the STAFF OF GOD in my hand': the resume-staff (17:5) renamed for its highest posting.")])
V[10] = v("UP_THE_HILL", "And Joshua did as Moses had said to him, to fight against Amalek; and Moses, Aaron, and Hur went up the top of the hill.",
  "and Joshua did as Moses had said to him, to fight against Amalek", "and Moses, Aaron, and Hur went up the top of the hill",
  "The card pops; Hur's debut.",
  [dict(op=R, expr_en="RESULT: HOLDS(bechar_lanu_anashim_ve_tze, t1)", he_span=(0,5),
    prose="THE COMPLIANCE [EX17-08 CROWN]. va-YAAS yehoshua KA-ASHER AMAR LO moshe — 'and Joshua DID AS MOSES HAD SAID to him' (asserted): the card POPS on the exact obedience-formula — the successor's FIRST NARRATED ACT is compliance without commentary (the machine files the credential: the man who will inherit the book enters it obeying it); u-moshe AHARON ve-chur — 'and Moses, AARON, and Hur': the printed-authority file's station (VERIFIED: aharon stands bare in the verse — MS: 'some err writing ve-Aharon'; one vav serves the list); ve-CHUR — HUR'S DEBUT: unintroduced like Joshua one verse up, and his whole Torah career is THREE tokens (asserted at the build): the hands here, the hands at 17:12, the regency at 24:14 — the corpus's most economical officer: he exists to hold things up; alu ROSH ha-giva — the command post manned: the battle now runs on two elevations (the readings on the hilltop as the war's true front, named-only).")])
V[11] = v("THE_HANDS_AND_THE_BATTLE", "And it was, when Moses would raise his hand, that Israel prevailed; and when he would rest his hand, that Amalek prevailed.",
  "and it was, when Moses would raise his hand, that Israel prevailed", "and when he would rest his hand, that Amalek prevailed",
  "The control loop.",
  [p("HOLDS(ka_asher_yarim_ve_gavar_yisrael, t0)", (0,6),
    "THE MECHANISM. ka-asher YARIM moshe yad-o ve-GAVAR yisrael — 'when Moses would RAISE his hand, ISRAEL PREVAILED'; ve-kha-asher YANICHA yad-o ve-gavar AMALEQ — and the converse: the corpus's first narrated CONTROL LOOP — a visible state-variable (one man's hand) driving a battlefield in real time, sampled in both directions by the verse's own if-and-if frame (the machine notes what the loop is made of: not a weapon — the hand holds the staff but the verse tracks the HAND; the readings the Mishna itself asks here — 'do Moses' hands make or break the war?' — named-only, with its answer: the hands aimed the eyes upward, and the heart followed): the battle below become an instrument reading of the posture above.")])
V[12] = v("HANDS_OF_FAITHFULNESS", "And Moses' hands were heavy; and they took a stone and put it under him, and he sat on it; and Aaron and Hur supported his hands, from this side one and from this side one; and his hands were faithfulness until the coming of the sun.",
  "and Moses' hands were heavy; and they took a stone and put it under him, and he sat on it", "and Aaron and Hur supported his hands, from this side one and from this side one; and his hands were faithfulness until the coming of the sun",
  "The heavy hands held; the three fathers.",
  [p("HOLDS(yadav_emuna_ad_bo_ha_shamesh, t0)", (17,22),
    "THE HOLDING [EX17-09 + EX17-10 CROWNS]. vi-yde moshe KEVEDIM — 'and Moses' hands were HEAVY': the kaved-root CROSSES THE LEDGER (asserted in-span: the root that ran Pharaoh's heavy heart through nine plagues lands on the deliverer's hands — the machine files the transfer: heaviness is no longer a moral verdict but a physical bill, and it is PAYABLE: a stone, two officers); va-yiqchu EVEN — the stone-seat (the readings: he refused a cushion — 'Israel is in distress, I am with them in distress' — named-only); ve-AHARON ve-CHUR tamkhu ve-yadav mi-ze echad u-mi-ze echad — one on each side: the corpus's first SUPPORTED leader (the office propped by other hands — the priest-to-be and the officer with no biography); va-yehi YADAV EMUNA ad-BO ha-shamesh — 'and his hands WERE FAITHFULNESS until the coming of the sun': the plene YADAV defended (VERIFIED in-verse; MS: the Recanati's lean yado 'a copyist's error — in ALL our books full with yod,' the Masorah proving it), the derash riding the GRAMMAR instead (va-yehi SINGULAR with plural hands — Ibn Ezra: each hand severally; the Zohar: all hangs on the right); the Kitzur reading the closing phrase as THREE FATHERS holding the line (EMUNA Abraham-who-believed, AD-BO Isaac-who-came, HA-SHAMESH Jacob-whose-sun-set); and BO written LEAN (VERIFIED skeleton; MS walking the Masorah-lists with the Ramah arbitrating: the battle-sunset and Mishpatim's mercy-sunset, 22:25, share one thinned word).")])
V[13] = v("BY_THE_MOUTH_OF_THE_SWORD", "And Joshua weakened Amalek and his people by the mouth of the sword.",
  "and Joshua weakened Amalek and his people", "by the mouth of the sword",
  "The event; the unique verb.",
  [dict(op=E, expr_en="va_yachalosh_yehoshua(e2); Agent(e2, yehoshua); Theme(e2, amaleq)", he_span=(0,7),
    prose="THE WEAKENING. va-YACHALOSH yehoshua et-amaleq ve-et-am-o — 'and Joshua WEAKENED Amalek and his people': THE EVENT — and the verb is Torah-unique (asserted at the build: not defeated, not destroyed — WEAKENED: the corpus's first battle ends without an ending, and 17:14-16 legislates the remainder); le-FI CHAREV — 'by the MOUTH of the sword': the machine notes the closing figure: a battle steered all day by HANDS is settled by a MOUTH — the idiom hands the sword the chapter's own anatomy (the verse itself runs straight through with NO mid-verse rest, asserted from the trope-file: the one verse in the chapter without the divider-accent — the kill-sentence takes no breath).")])
V[14] = v("WRITE_THIS_IN_THE_BOOK", "And the LORD said to Moses: Write this, a memorial in the book, and set it in the ears of Joshua: that I will utterly blot out the memory of Amalek from under the heavens.",
  "and the LORD said to Moses: write this, a memorial in the book, and set it in the ears of Joshua", "that I will utterly blot out the memory of Amalek from under the heavens",
  "The first write-command; the blot-pair.",
  [dict(op=D, expr_en="DECLARE(YHWH, LET(ketov_zot_zikaron_ba_sefer))", he_span=(4,10),
    prose="THE WRITE-COMMAND [EX17-11 + EX17-12 CROWNS]. KETOV zot ZIKARON ba-SEFER — 'WRITE this, a memorial, IN THE BOOK': THE TORAH'S FIRST WRITE-COMMAND (and zikaron's first station, asserted) — the corpus, itself a written thing, here records the order that founds its own medium: and the first commissioned text is an ERASURE NOTICE (write, so that a blotting-out is never forgotten — the machine files the paradox as the card's own terms); ve-SIM be-AZNE yehoshua — the successor briefed by ear as well as ink; and the four words' INITIALS spell ZEVUV, THE FLY (VERIFIED by machine: 'Amalek chased after the blood of Israel like a fly' — the Kitzur): the enemy's portrait signed inside his own death warrant; ki MACHO EMCHE et-ZEKHER amaleq — 'I will UTTERLY BLOT OUT the memory of Amalek': the blot-verb's Torah-pair (VERIFIED): THE FLOOD (Gen 6:7) and here — the Kitzur: 'as there ALL was blotted, so Amalek wholly — and SAUL was punished for the remnant' (1 Sam 15 named), the doubled verb carrying the remnant's name in cipher (MACHO EMCHE = ZE HAMAN, 107=107, asserted — Esther's Agagite as the unfinished business); the card stands OPEN — the one command in the chapter with no in-span receipt (Deut 25:19 armed: the blotting is homework for the whole canon).")])
V[15] = v("THE_LORD_IS_MY_BANNER", "And Moses built an altar, and called its name: The LORD is my banner.",
  "and Moses built an altar", "and he called its name: the LORD is my banner",
  "The altar named.",
  [dict(op="NAME", expr_en="name(mizbeach) := YHWH_Nisi", he_span=(3,6),
    prose="THE ALTAR [EX17-13]. va-yiven moshe MIZBEACH — 'and Moses built an ALTAR': MOSES' FIRST ALTAR (the corpus's altar-file — Noah after the flood, Abraham's four, Isaac's, Jacob's — gains its first since Genesis, and the first built on a battlefield); va-yiqra shem-o YHWH NISI — 'and he called its name THE LORD IS MY BANNER': the naming-verb's second spend this chapter (17:7 named the shame; 17:15 names the victory — one chapter files both deeds under va-yiqra); and the banner-word's only Torah station (VERIFIED at the build; the Kitzur's Scripture-twin named: 'I will raise My BANNER to the peoples,' Isaiah — 'a REAL banner: he called the Holy One my banner and my standard'): the machine notes the sound the name carries: NISI rings against MASA's testing (nes/nisa — the tradition's own pun, named as pun): the place named for the test, the altar named for the standard.")])
V[16] = v("THE_THRONE_OATH", "And he said: For a hand is upon the throne of YH — war for the LORD against Amalek, from generation to generation.",
  "and he said: for a hand is upon the throne of YH — war for the LORD against Amalek", "from generation to generation",
  "The shortened throne; the perpetual war.",
  [p("HOLDS(milchama_la_YHWH_ba_amaleq_mi_dor_dor, t0)", (0,8),
    "THE OATH [EX17-13 CROWN]. ki-YAD al-KES YAH — 'for a HAND is upon the THRONE OF YH': the throne-word KES a Torah-hapax bound uniquely to the HALF-NAME (VERIFIED adjacency) — the tradition beneath the shortened pair: NEITHER THE THRONE NOR THE NAME IS WRITTEN WHOLE while Amalek remains (the oath sworn on a broken seal); MS files the era's ruling on the words themselves: Radak read ONE word, the West's codices one, the EAST'S two, the Talmud's amoraim split (Pesachim) — 'and the Ramah ruled: in precise texts TWO WORDS' (the Meiri concurring; the SNAPSHOT writes two — dual-tracked as the grammarians' file); the verse one of the Masorah's SIX with FIVE consecutive two-letter words (asserted: ki, yad, al, kes, yah — the oath-clause built entirely of two-letter bricks, the syntax itself in fragments); MILCHAMA la-YHWH ba-amaleq — 'WAR FOR THE LORD against Amalek': the LORD's own standing war (not pushed as a card: His commitments transcend the queue — the mandate-class); mi-DOR DOR — 'from GENERATION to GENERATION': both lean (MS; the first form Torah-unique, asserted) — and the Kitzur signs the war's two future generals in cipher (asserted at the build): the yod of ki plus YAD = DAVID (24), and MI-DOR DOR = LI-YEME MASHIACH, 'to the days of MESSIAH' (448): the throne completed by the hand of one, the war ended in the days of the other.")])

# ---- scenarios ----------------------------------------------------------
BASE = "no test, no name."
Dtenu = "LET(tenu_lanu_mayim) pushed and OPEN;"
Davor = "LET(avor_lifne_ha_am_ve_hikita) pushed and OPEN;"
Dbechar = "LET(bechar_lanu_anashim_ve_tze) pushed and OPEN;"
Dketov = "LET(ketov_zot_zikaron_ba_sefer) pushed and OPEN;"
REG1 = "REGISTRY: maqom_refidim->Masa_u_Meriva (1 write)"
REG2 = "REGISTRY: maqom_refidim->Masa_u_Meriva, mizbeach->YHWH_Nisi (2 writes)"
expects = {}
expects[1] = [BASE]
for vs in (2, 3, 4):
    expects[vs] = [Dtenu, BASE]
expects[5] = [Dtenu, Davor, BASE]
expects[6] = [BASE]
expects[7] = [REG1]
expects[8] = [REG1]
expects[9] = [Dbechar, REG1]
for vs in (10, 11, 12, 13):
    expects[vs] = [REG1]
expects[14] = [Dketov, REG1]
expects[15] = [Dketov, REG2]
expects[16] = [Dketov, REG2]
titles = {
    1: "no water in Rephidim", 2: "give us water",
    3: "why did you bring us up", 4: "they will stone me",
    5: "pass before the people", 6: "the rock at Horeb",
    7: "Massah and Meribah", 8: "Amalek comes", 9: "choose us men",
    10: "up the hill", 11: "the hands and the battle",
    12: "hands of faithfulness", 13: "by the mouth of the sword",
    14: "write this in the book", 15: "the LORD is my banner",
    16: "the throne oath",
}

steps, scenarios = [], []
for i, vs in enumerate(sorted(V), 1):
    spec = V[vs]
    steps.append(unitgen.build_step(db, "Exod", "Exod", 17, vs, i, spec))
    scenarios.append(unitgen.scenario_for(
        db, "Exod", 17, vs, "S%d" % i,
        "after STEP_Ex_17_%d — %s" % (vs, titles[vs]),
        spec["en"].replace("[EN-AID] ", ""), expects[vs]))

ttl_he, ttl_tr = unitgen.join_tokens(unitgen.verse_tokens(db, "Exod", 17, 15)[5:7], strip_accents=False)

META = '''# =============================================================================
# LOGIC UNIT: Exodus 17:1-16 — Massah-Meribah (the rock at Horeb) and Amalek
#             (the hands, the book, the throne-oath)
# FORWARD ERA unit #31 — derived 2026-08-10 (oral layer in-pipeline; review waived)
# Run FWD-8 block 1.
# =============================================================================
# Experimental model — not binding religious law.

meta:
  id: "exo_17_massah_and_amalek"
  title_en: "Massah-Meribah and Amalek (17:1-16)"
  title_he: %s
  title_he_translit: "%s"
  title_he_en: "'the LORD is my banner'"
  book_he: שְׁמוֹת
  book_he_translit: Shemot
  book_en: Exodus
  refs: "17:1-16"
  unit_span_planned: "17:1-16"
  data_paths_he:
  - "Data/Exod.xml"
  status: frozen
  draft_note_en: >
    DERIVED 2026-08-10 · FORWARD ERA unit #31 (run FWD-8 block 1;
    Exod 1-17 continuous behind it). Span: 17:1-16, whole chapter:
    16 verses (SNAPSHOT-verified; 17:13 the only verse without a
    mid-verse rest — the kill-sentence takes no breath). Oral
    layer IN-PIPELINE: manifest 13/13 VERIFIED, zero FAILED —
    see oral_audit_note_en.

    MACHINE PROFILE. FOUR DECLAREs, THREE RESULTs, TWO EVENTS,
    TWO NAMEs. Two theaters in one chapter: the WATER COURT
    (17:1-7) and the WAR (17:8-16). The people's demand (17:2
    tenu-lanu — the corpus's first imperative demand from
    below) and the strike-order (17:5) both pop at 17:6 on
    va-yaas-ken; Joshua's commission (17:9) pops at 17:10 on
    the full obedience-formula; the WRITE-COMMAND (17:14 —
    the Torah's first, and zikaron's first station) stands
    OPEN with no in-span receipt: the blotting of Amalek is
    homework for the canon (Deut 25:19 armed). TWO EVENTS:
    Amalek's attack (17:8 — the corpus's first pitched
    battle) and Joshua's weakening (17:13 — the unique verb:
    the battle ends without an ending). TWO NAMEs, one
    naming-verb: the place named for the shame (17:7
    Masa-u-Meriva, the corpus's first DOUBLE place-name — the
    charge sheet) and the altar for the victory (17:15
    YHWH-Nisi); REGISTRY 2. The know-ledger's mirror: 16:4's
    im-lo (will they walk, OR NOT) returns as 17:7's im-ayin
    (is He among us, OR NOT) — the test-grammar seized by the
    tested. MACHINE EVIDENCE asserted at the build: tenasun
    unique (the inverted test-verb); the station-name's
    spelling arc (full at arrival 17:1 and departure 19:2,
    LEAN at the attack 17:8 + its Num 33:14 memorial); the
    weaken-verb unique; Hur's whole career the three ve-chur
    tokens (17:10, 17:12, 24:14); the kaved-root crossing
    from Pharaoh's heart to Moses' hands (17:12 kevedim);
    zikaron's first station; the three ciphers (blot-pair =
    this-is-Haman 107; yod+hand = David 24; from-generation
    = days-of-Messiah 448); five two-letter words in the
    oath-clause. Queue at close: ONE OPEN in-unit (the
    write-command) plus the standing opens. REGISTRY 2;
    TESTS 0.

    CARE-POINTS: the double pop at 17:6 (strike-order and
    water-demand close on one compliance-formula; the
    drinking itself unnarrated — banked on warranty); the
    unintroduced debuts (Joshua 17:9, Hur 17:10 — no
    patronym, no office); the control loop (17:11 — a hand
    as the battle's state-variable, sampled both directions);
    the supported leader (17:12 — the office propped by
    other hands); the perpetual war held as mandate-class
    (17:16 — the LORD's standing commitments transcend the
    queue, BLESS precedent). WATCHLIST ARMS: 19:2 (the
    departure from Rephidim, full spelling — the Sinai
    arrival); 24:14 (Hur's regency — his third and last
    token); Num 13:20 (the or-not pair's second station —
    the spies); Num 20:1-13 (Meribah-Kadesh: the thirst
    repeated, the strike gone wrong — heelitanu's third
    station); Deut 25:17-19 (remember Amalek — the
    write-command's far receipt); Deut 6:16 (you shall not
    test as you tested at Massah). Outside-Torah names
    (named-only): Josh 8 (the write-successor writes), 1 Sam
    15 (Saul and Agag), Esther (Haman the Agagite), Isa
    49:22 (the ensign), 2 Sam 17 (Absalom's counsel), Judg
    6:31 (the Baal-quarrel), Job 33:13.
  oral_audit_note_en: >
    ORAL AUDIT 2026-08-10 (IN-PIPELINE, forward era; manifest
    logic/oral_audit/manifests/exo_17_massah_and_amalek_claims.json
    13/13 VERIFIED, zero FAILED; record
    logic/oral_audit/AUDIT_exo_17_2026-08-10.md). CROWNS
    (chain-attested + DB-verified). THE QUARREL-FILE [EX17-01,
    KB + MS on 17:2]: תריבון ("you quarrel") Torah-unique
    (checked; the Kitzur's Scripture-three: Gideon's
    Baal-quarrel, Job — "whoever quarrels with his master
    quarrels with the Holy One"); תנסון ("you test") equally
    alone (asserted): 16:4's test-verb inverted on the Tester;
    both lean (Chizkuni); one of the Masorah's EIGHT double-מה
    ("what... what...") verses; printed-authority: תנו ("give,"
    plural) defended against presses' תנה (MS). THE
    BROUGHT-US-UP FILE [EX17-02, KB on 17:3]: העליתנו ("you
    brought us up") exactly FOUR in the Torah (census exact):
    Rephidim, Korach (Num 16:13 — "the very same men," the
    Masorah's pair-wire), Meribah-Kadesh (Num 20:5), the
    serpents (Num 21:5) — the forty-year accusation under one
    verb; למים ("for water") a Torah-pair: the thirst here and
    the creation-division (Gen 1:6). THE STONING-WORD
    [EX17-03, MS on 17:4]: וסקלני ("and they will stone me")
    Torah-unique (checked); lean after the lamed, final yod
    written AND read — the Sura tradition's vav rejected by
    the Ramah. BEN ASHER'S STROKE [EX17-04, MS on 17:6]:
    על־הצור ("on the rock") — the preposition bound to its
    rock by the binder-stroke with the little lengthener
    in-token, "so it is for Ben Asher" (the binder-stroke
    checked in the SNAPSHOT column): the LORD stands ON the
    thing about to be struck. THE OR-NOT PAIR [EX17-05, KB on 17:7]: אם אין
    ("or not?") in the long pausal form exactly TWICE
    (adjacency checked): the presence-question and the spies'
    wood-question (Num 13:20) — the Kitzur wiring both to
    war: "because they said is-the-LORD-in-our-midst-or-not,
    Amalek came." THE SLACK HANDS [EX17-06, KB on 17:8]:
    ברפידם ("in Rephidim") LEAN exactly at the attack and its
    itinerary-memorial (Num 33:14, census pair, checked);
    full at arrival and departure (17:1, 19:2, asserted) —
    the Kitzur: Rephidim = רפו ידים ("they weakened their
    hands from the commandments, therefore Amalek came").
    THE GO-OUT PAIR [EX17-07, KB on 17:9]: וצא ("and go
    out") exactly twice (checked): Moses to Joshua and Isaac
    to Esau (Gen 27:3) — "out beyond the clouds"; the corpus
    adds: the verb that sent Esau hunting sends Israel
    against Esau's grandson. THE BARE AARON [EX17-08, MS on
    17:10]: ומשה אהרן וחור ("and Moses, Aaron, and Hur") —
    printed-authority: "some err writing ve-Aharon" (the name
    checked bare in-verse); Hur's debut — his
    whole career three tokens (asserted). THE FULL HANDS
    [EX17-09, MS + KB on 17:12]: ידיו ("his hands") PLENE
    defended — the Recanati's lean ידו "a copyist's error; in
    all our books full with yod" (checked in-verse); the
    derash rides the grammar (ויהי singular, hands plural —
    Ibn Ezra, the Zohar's right hand); the Kitzur: אמונה
    ("faithfulness") = Abraham, עד בא ("until the coming") =
    Isaac, השמש ("the sun") = Jacob — three fathers holding
    the line. THE LEAN SUN [EX17-10, MS on 17:12]: בא
    ("coming") written lean here and at Mishpatim's
    pledge-sunset (22:25) — the printed Masorah's roster of
    full spellings corrected, the Ramah arbitrating (skeleton
    checked at the build). THE BLOT-PAIR [EX17-11, KB on 17:14]: אמחה
    ("I will blot out") exactly TWICE in the Torah (census
    pair, checked): the FLOOD (Gen 6:7) and Amalek — "as
    there all was blotted, so Amalek wholly; and Saul was
    punished for the remnant"; מחה אמחה ("utterly blot") =
    זה המן ("this is Haman," 107 = 107, asserted); זכרון
    ("memorial") — the word's first Torah station (asserted):
    the first commanded text is an erasure notice. THE FLY
    [EX17-12, KB on 17:14]: the initials of זכרון בספר ושים
    באזני ("a memorial in the book, and set it in the ears")
    spell זבוב ("a FLY," machine-checked) — "Amalek chased
    after the blood of Israel like a fly." THE THRONE-FILE
    [EX17-13, KB + MS on 17:15-16]: כס ("throne") a
    Torah-hapax bound uniquely to the half-Name יה (adjacency
    checked) — neither throne nor Name written whole while
    Amalek remains; the two-word ruling (Radak's one word vs
    the Ramah and Meiri's two; West/East codices split; the
    Pesachim dispute — dual-tracked; the SNAPSHOT writes
    two); FIVE consecutive two-letter words (asserted; the
    Masorah's six-verse file); נסי ("my banner")
    Torah-unique (asserted; the Kitzur: "a REAL banner" —
    Isaiah's ensign its Scripture-twin); מדר דר ("from
    generation to generation") both lean (MS; first form
    unique, asserted); the ciphers: yod + יד ("hand") =
    דויד (David, 24 = 24) and מדר דר = לימי משיח ("to the
    days of Messiah," 448 = 448, asserted) — the war's two
    future generals signed into the oath.
  owner_language_note: >
    English for reading only. Hebrew is the derivation source.
  oral_policy_note_en: >
    Written trees first. Dual-track Oral only when named; never
    silent-merge.
  tree_derive_version: logic_derived_v1
  tree_derive_phase: "FWD-31"
  confidence_overall: "structure tested; oral layer verified 13/13"
  genre: "thirst_and_war_fsm"
  build_track: exodus_stack
  depends_on: exo_16_manna_and_sabbath
  depends_note_en: >
    Depends for PATTERN only (16:4's im-lo test-grammar returns
    inverted as 17:7's im-ayin; the murmur-cycle's third organ:
    bread, then kept-bread, now water; the armed cry pays).
    Standalone machine. Exod 1-17 continuous, 93 frozen units.
''' % (ttl_he, ttl_tr)

DLOG = '''derivation_log:
  - step: A
    name_en: "Block choice"
    comment: >
      FORWARD ERA run 8, block 1 (owner: "lets do 5 more blocks").
      Canon continuation: Exod 17:1-16 — Massah-Meribah and
      Amalek, whole chapter.
    confidence: established
  - step: B
    name_en: "Span + source + conventions"
    comment: >
      SNAPSHOT prestage: 16 verses; 17:13 the only verse without
      etnachta (split at tifcha). Volitive census: four real
      pushes (17:2 the people's water-demand, 17:5 the
      strike-order, 17:9 Joshua's commission, 17:14 the
      write-command); 17:16's perpetual war is mandate-class
      (no push — the LORD's standing commitments transcend the
      queue); 17:6's strike instruction folds into 17:5's card.
    confidence: established
  - step: C
    name_en: "Machine structure"
    comment: >
      4D/3R/2E/2N. The water court (demand + order both pop at
      17:6 on va-yaas-ken) and the war (commission pops 17:10;
      the write-command stands OPEN — the chapter's one
      unreceipted card). Events: the attack (17:8), the
      weakening (17:13, unique verb). Two names on one
      naming-verb: the charge sheet (17:7, the corpus's first
      double place-name) and the banner-altar (17:15).
      REGISTRY 2. Asserted machine evidence: tenasun unique;
      the Rephidim spelling arc; ve-chur's three; kevedim on
      the deliverer's hands; zikaron's debut; the three
      ciphers; the five two-letter words.
    confidence: tested
  - step: D
    name_en: "Oral scan (in-pipeline)"
    comment: >
      Local mirror only (zero fetches): Minchat Shai on Exod 17
      (10 notes) + Kitzur Baal HaTurim on Exod 17 (13 notes).
      Manifest 13 rows: 13 VERIFIED / 0 FAILED / 0 UNCHECKABLE.
      One row sharpened by the verifier itself: the or-not
      census is a PAUSAL-FORM pair (17:7 + Num 13:20), not a
      four — the two long or-nots are exactly the two the
      Kitzur wires to war. The quarrel-file; the four
      brought-us-ups; the stoning-word; Ben Asher's stroke;
      the slack hands; the go-out pair; the bare Aaron; the
      full hands + three fathers; the lean sun; the
      blot-pair + this-is-Haman; the fly initials; the
      throne-file with David and Messiah.
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
      not silent edits. Exod 1-17 continuous.
    confidence: established
'''

unitgen.emit_unit(META, DLOG, steps, scenarios, "logic/units/exo_17_massah_and_amalek.yaml")
print("wrote logic/units/exo_17_massah_and_amalek.yaml —", len(steps), "steps,", len(scenarios), "scenarios")
