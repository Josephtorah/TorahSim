#!/usr/bin/env python3
"""Author exo_20_the_ten_utterances (Exod 20:1-26) — forward-era unit #34 (run FWD-8 block 4).
Run from repo root."""
import sys, sqlite3
sys.path.insert(0, "<scratch>")
import unitgen

db = sqlite3.connect(unitgen.DB)

def hp(ch, vs, idx, book="Exod"):
    return db.execute("SELECT w.he_plain FROM words w JOIN verses v ON w.verse_id=v.id "
                      "WHERE v.book=? AND v.chapter=? AND v.verse=? AND w.idx=?",
                      (book, ch, vs, idx)).fetchone()[0].replace("/", "")

def he(ch, vs, idx, book="Exod"):
    return db.execute("SELECT w.he FROM words w JOIN verses v ON w.verse_id=v.id "
                      "WHERE v.book=? AND v.chapter=? AND v.verse=? AND w.idx=?",
                      (book, ch, vs, idx)).fetchone()[0]

def census(sp):
    return db.execute("""SELECT v.book, v.chapter, v.verse FROM words w
        JOIN verses v ON w.verse_id=v.id
        WHERE replace(w.he_plain,'/','')=? ORDER BY v.book, v.chapter, v.verse""",
        (sp,)).fetchall()

# ---- build-time machine evidence (asserted, not crowns) -------------------
letters = words = 0
for vs in range(2, 18):
    for (w,) in db.execute("SELECT w.he_plain FROM words w JOIN verses v ON w.verse_id=v.id "
                           "WHERE v.book='Exod' AND v.chapter=20 AND v.verse=? ORDER BY w.idx", (vs,)):
        letters += len(w.replace("/", "")); words += 1
assert letters == 620                                                          # the Ten = KETER (the crown)
assert words == 172                                                            # the Ten = EQEV
assert hp(20, 2, 0)[0] == "א" and hp(20, 17, 14)[-1] == "ך"                    # alef to kaf: AKH (surely good)
assert len(hp(20, 13, 0)) + len(hp(20, 13, 1)) == 6                            # the sixth utterance, six letters
two_word = db.execute("""SELECT v.book, v.chapter, v.verse FROM words w JOIN verses v ON w.verse_id=v.id
    GROUP BY v.id HAVING COUNT(*)=2 ORDER BY v.book, v.chapter, v.verse""").fetchall()
assert two_word == [("Deut", 5, 17), ("Deut", 5, 18), ("Deut", 5, 19),
                    ("Exod", 20, 13), ("Exod", 20, 14), ("Exod", 20, 15)]      # the Torah's ONLY two-word verses
assert hp(20, 8, 0)[0] == "ז"                                                  # zakhor opens with zayin (= 7)
assert [hp(20, 10, i) for i in range(9, 16)] == ["אתה", "ובנך", "ובתך", "עבדך", "ואמתך", "ובהמתך", "וגרך"]  # seven resters
assert "ַ" in he(20, 3, 6) and "ָ" in he(20, 3, 6)                              # panai: both vowels in-token
assert "ַ" in he(20, 4, 11) and "ָ" in he(20, 4, 11)                            # mitachat: both vowels in-token
assert census("תחטאו") == [("Exod", 20, 20), ("Gen", 42, 22)]                   # the two sin-nots (Reuben + Moses)
assert census("נגש") == [("Exod", 20, 21), ("Gen", 33, 7)]                      # the two fearful approaches
assert census("הלפידם") == [("Exod", 20, 18)]                                   # the torches, full-then-lean, unique
G = {"א":1,"ב":2,"ג":3,"ד":4,"ה":5,"ו":6,"ז":7,"ח":8,"ט":9,"י":10,"כ":20,"ך":20,
     "ל":30,"מ":40,"ם":40,"נ":50,"ן":50,"ס":60,"ע":70,"פ":80,"ף":80,"צ":90,"ץ":90,
     "ק":100,"ר":200,"ש":300,"ת":400}
g = lambda s: sum(G[c] for c in s if c in G)
assert g("כתר") == 620 and g("עקב") == 172                                      # the two count-ciphers
assert g("הערפל") == g("שכינה") == 385                                          # the dark = the Presence
assert g("אנכי") == g("כסא") == 81                                              # the I = the throne
assert g("אבוא") == 10                                                          # the minyan coming
assert g("תמונה") == g("פרצוף") + g("אדם") == 501                               # image = human visage
assert g("יראתו") + g("על") + g("פניכם") == g("זה") + g("הוא") + g("בושת") + g("הפנים") == 917  # fear = shame

P = "PRECONDITION_STATE"
D = "DECLARE"
R = "RESULT"
E = "EVENT"
S = "STATUTE"

def v(op, en, left, right, comment, ops):
    return dict(op=op, en=en, left_en=left, right_en=right, comment=comment, operators=ops)

def p(expr, span, prose):
    return dict(op=P, expr_en=expr, he_span=span, prose=prose)

def st(expr, span, prose):
    return dict(op=S, expr_en=expr, he_span=span, prose=prose)

V = {}
V[1] = v("GOD_SPOKE_ALL_THESE_WORDS", "And God spoke all these words, saying:",
  "and God spoke all these words", "saying",
  "The frame of the Ten.",
  [p("HOLDS(va_yedaber_elohim, t0)", (0,6),
    "THE FRAME. va-yedaber ELOHIM et KOL-ha-devarim ha-ele LEMOR — 'and GOD spoke ALL these words': the seven-word frame with no mid-verse rest (the readings: ALL the words IN ONE UTTERANCE — 'what the mouth cannot say and the ear cannot hear'; the Kitzur's cipher-face named: the verse counted to 'all that is in writing and all that is oral' — the frame claiming the whole Torah); the machine notes the speaker-title: ELOHIM (the judgment-name) speaks the law — 19:19's dialogue-channel now carries the code itself; and 19:25's open mouth closes here: what Moses turned to say, God says.")])
V[2] = v("I_AM", "I am the LORD your God, who brought you out of the land of Egypt, out of the house of slaves.",
  "I am the LORD your God", "who brought you out of the land of Egypt, out of the house of slaves",
  "Utterance one; the first statute.",
  [st("STATUTE BIND(anokhi_YHWH_elohekha)", (0,2),
    "UTTERANCE ONE [EX20-01 + EX20-13 CROWNS]. ANOKHI YHWH ELOHEKHA — 'I AM the LORD your God': the first utterance INSTALLED as standing law (the corpus's statute-class debut in Exodus: the apodictic operator of the law-books arrives with the Ten — and the first statute is not a rule but a RELATION: the I binds before any thou-shalt); asher HOTZETIKHA me-eretz mitzrayim — the credential: the brought-you-out word's Torah-three (VERIFIED): UR OF THE CHALDEES (Gen 15:7, to Abraham), and the TWO DECALOGUES — 'brought out of Ur to give his sons the Torah' (the Kitzur): the nation's exodus spelled with the father's; all three FULL-full-full (MS with the Ramah; the Jerusalem Talmud's lean split named); mi-BET AVADIM — 'out of the house of SLAVES' (the machine notes the ground of the law: the code opens by citing the emancipation that makes commanding possible); ANOKHI = KISE, the throne (81 = 81, asserted): the I weighing its own seat; and the count-dispute sealed (MS): 'as the sages received — ANOKHI and LO-YIHYE are the two heard FROM THE MOUTH OF THE POWER.'")])
V[3] = v("NO_OTHER_GODS", "There shall not be to you other gods before My face.",
  "there shall not be to you other gods", "before My face",
  "Utterance two; the double-pointed close.",
  [st("STATUTE FORBID(elohim_acherim)", (0,4),
    "UTTERANCE TWO [EX20-04 CROWN]. lo yihye-lekha ELOHIM ACHERIM — 'there shall not BE to you OTHER GODS': the second statute (heard, with the first, from the Power's own mouth — the received count; the exclusivity-law covering 20:3-6 as one utterance); al-PANAI — 'before MY FACE' (the readings: wherever I am — which is everywhere: the ban with no territorial edge, named-only) — and the closing token carries TWO VOWELS IN ONE SLOT (VERIFIED in-token: the verse-end reading's long vowel AND the running reading's short — the DOUBLE-READING SYSTEM'S trace in the SNAPSHOT itself: the lone reader closes the verse here; the public reader runs the whole utterance as one — MS's essay from ibn Habib: accents, vowels, and soft-hard letters all doubled to keep both readings; the Rama of Fano's warning named: read one fork, never both).")])
V[4] = v("NO_GRAVEN_IMAGE", "You shall not make yourself a graven image, or any likeness of what is in the heavens above, or what is in the earth beneath, or what is in the waters beneath the earth.",
  "you shall not make yourself a graven image, or any likeness of what is in the heavens above", "or what is in the earth beneath, or what is in the waters beneath the earth",
  "The image-ban's three floors.",
  [p("HOLDS(lo_taase_lekha_fesel, t0)", (0,5),
    "THE IMAGE-BAN. lo taase-lekha FESEL ve-khol-TEMUNA — 'no graven image, or ANY LIKENESS': the second utterance's detail-law (the statute of 20:3 unpacked — heavens above, earth beneath, waters beneath the earth: the three floors of the creation swept for portrait-subjects); TEMUNA = PARTZUF ADAM ('the human visage,' 501 = 501, asserted at the build — the Kitzur: the likeness-ban counting the likeliest likeness: man's own face); the beneath-word double-pointed at the mid-verse rest (VERIFIED in-token: the pausal and running vowels both held — the double-reading system's second trace); the Kitzur's earth-count named (the mountains and the hills): the machine files the ban's scope: nothing that IS may stand for the One who IS.")])
V[5] = v("A_JEALOUS_GOD", "You shall not bow down to them, and you shall not serve them; for I the LORD your God am a jealous God, visiting the iniquity of fathers on sons, on the third and on the fourth generation, to those who hate Me.",
  "you shall not bow down to them, and you shall not serve them", "for I the LORD your God am a jealous God, visiting the iniquity of fathers on sons, on the third and on the fourth generation, to those who hate Me",
  "The enforcement clause.",
  [p("HOLDS(el_qana, t0)", (5,10),
    "THE JEALOUSY. lo-tishtachave lahem ve-lo TAAVDEM — 'not bow, not SERVE' (the worship-verbs banned in the pair the exodus freed: avad, the slave-root — the machine notes the exchange: out of the house of avadim, and immediately forbidden to avad elsewhere: the emancipation was a transfer of service, not its end); ki anokhi YHWH elohekha EL QANA — 'a JEALOUS God' (the marriage-frame of 19:4's betrothal enforcing itself: jealousy is the covenant's grammar, not its temper — the readings named-only); POQED avon AVOT al-BANIM al-shileshim ve-al-ribeim LE-SONAI — 'visiting the iniquity of fathers on sons... to those who HATE Me': the visiting-verb (the ledger-verb of 3:16's I-have-surely-visited turned to audit), the four generations counted against the next verse's THOUSANDS — the machine holds the asymmetry for 20:6.")])
V[6] = v("MERCY_TO_THOUSANDS", "And doing kindness to thousands — to those who love Me, and to those who keep My commandments.",
  "and doing kindness to thousands", "to those who love Me, and to those who keep My commandments",
  "The asymmetry; the kindness-file.",
  [p("HOLDS(ve_ose_chesed_la_alafim, t0)", (0,2),
    "THE KINDNESS [EX20-05 CROWN]. VE-OSE CHESED la-ALAFIM — 'and DOING KINDNESS to THOUSANDS': the mercy-clause outnumbering the audit four-to-two-thousand (the readings' five-hundred-to-one arithmetic, named-only) — and the doing-kindness contact stands THREE times in the Torah (VERIFIED adjacency): the SERVANT'S PRAYER ('do kindness with my master Abraham,' Gen 24:12 — the corpus's first do-kindness, a plea FOR a master) and the TWO DECALOGUES (the Master's own pledge): the phrase that entered the canon as a servant's request returns as divine self-description; the Kitzur's David-file named ('who does kindness is done kindness'); le-OHAVAI u-le-shomre MITZVOTAI — lovers and keepers: the law's two grips (the heart's and the hand's); and the next utterance's ornament filed as instrument-gap: the SEVEN CROWNLETS on the oath-ban's shin (the tagin above the SNAPSHOT's letter-stream — the sevens named).")])
V[7] = v("THE_NAME_IN_VAIN", "You shall not take up the name of the LORD your God in vain; for the LORD will not hold him guiltless who takes up His name in vain.",
  "you shall not take up the name of the LORD your God in vain", "for the LORD will not hold him guiltless who takes up His name in vain",
  "Utterance three.",
  [st("STATUTE FORBID(shem_la_shav)", (0,6),
    "UTTERANCE THREE. lo TISA et-shem-YHWH elohekha LA-SHAV — 'you shall not TAKE UP the Name in VAIN': the third statute (the lift-verb: the Name as a thing carried — misuse is bad freight); ki LO YENAQE YHWH — 'the LORD will NOT HOLD GUILTLESS': the statute arrives with its own enforcement rider (the machine notes the form: the only utterance whose sanction is a refusal — no penalty named, only pardon withheld); the Kitzur's juxtaposition carried: mercy-to-keepers beside the oath-ban — 'the vain oath weighs as all the commandments'; and the readings on shav doubled (the false and the pointless), named-only.")])
V[8] = v("REMEMBER_THE_SABBATH", "Remember the sabbath day, to keep it holy.",
  "remember the sabbath day", "to keep it holy",
  "Utterance four; the sevens.",
  [st("STATUTE BIND(zakhor_et_yom_ha_shabat)", (0,4),
    "UTTERANCE FOUR [EX20-06 CROWN]. ZAKHOR et-yom ha-SHABAT le-qadsho — 'REMEMBER the sabbath day, to keep it holy': the fourth statute — and the manna's classroom becomes law (the machine settles exo_16's arm: the six-and-one frame taught in bread at 16:26 is here spoken from the mountain — the Sabbath commanded at Sinai, learned first at breakfast); the Kitzur's arithmetic ALL VERIFIED at the build: FIVE words ('who upholds the Sabbath upholds the FIVE books'), the SEVENTH verse of the span, opening with ZAYIN (= 7), and SEVEN resters coming in its law — verse seven, letter seven, roster seven: the day's number stamped at every scale; zakhor the infinitive-absolute (the readings: remember-and-keep IN ONE SAYING — Deut 5's shamor its twin utterance, named-only).")])
V[9] = v("SIX_DAYS_SHALL_YOU_LABOR", "Six days shall you labor, and do all your work.",
  "six days shall you labor", "and do all your work",
  "The week's other side.",
  [p("HOLDS(sheshet_yamim_taavod, t0)", (0,3),
    "THE SIX. SHESHET YAMIM taavod — 'SIX DAYS shall you labor': 16:26's exact frame (sheshet yamim... u-va-yom ha-shevii) re-cut as command — the machine closes the wire: the manna-week armed at exo_16 pays at Sinai; ve-asita KOL-melakhtekha — 'ALL your work' (the readings: rest as if all the work were done — the kaf that reads both hard and soft in the two reading-systems, MS's four-letter file): the labor-clause as the Sabbath's other face: the seventh is holy only where the six are worked.")])
V[10] = v("THE_SEVENTH_IS_REST", "And the seventh day is a sabbath to the LORD your God; you shall not do any work — you, and your son and your daughter, your servant and your maid, and your beast, and your stranger who is within your gates.",
  "and the seventh day is a sabbath to the LORD your God", "you shall not do any work — you, and your son and your daughter, your servant and your maid, and your beast, and your stranger who is within your gates",
  "The seven resters.",
  [p("HOLDS(shabat_la_YHWH_elohekha, t0)", (9,15),
    "THE ROSTER. ve-yom ha-SHEVII shabat la-YHWH elohekha — 'the seventh day is a sabbath TO THE LORD'; lo-taase khol-melakha — the work-ban universal — and then the SEVEN RESTERS counted (VERIFIED at the build): ATA u-vinkha u-vitekha, avdekha va-amatekha, u-vehemtekha, ve-gerkha — you, son, daughter, servant, maid, BEAST, STRANGER: the Kitzur: 'against them the seven rests were ordained' — the machine files the roster's reach: the rest-law is the corpus's first command addressed THROUGH a person to his whole economic shadow (children, staff, livestock, guests — the Sabbath as the first labor-law), and the first statute with a BEAST among its beneficiaries.")])
V[11] = v("THE_CREATION_WARRANT", "For six days the LORD made the heavens and the earth, the sea and all that is in them, and He rested on the seventh day; therefore the LORD blessed the sabbath day, and sanctified it.",
  "for six days the LORD made the heavens and the earth, the sea and all that is in them, and He rested on the seventh day", "therefore the LORD blessed the sabbath day, and sanctified it",
  "The warrant cited.",
  [p("HOLDS(al_ken_berakh_YHWH, t0)", (18,25),
    "THE WARRANT. ki sheshet-yamim ASA YHWH et-ha-shamayim ve-et-ha-aretz — 'for six days the LORD MADE the heavens and the earth' — va-YANACH ba-yom ha-shevii — 'and He RESTED on the seventh': the statute cites its precedent — CREATION ITSELF entered as the Sabbath's case-law (the machine notes the jurisprudence: the fourth utterance is the only one of the Ten that argues — al-KEN, THEREFORE — and its warrant is Gen 2:2-3 quoted into the code: berakh... va-yeqadshehu, the blessing and sanctifying verbs of the creation-week now legislation); the corpus closes its oldest arc: the seventh day sanctified at the world's first week, kept first by a nation at 16:30, here becomes statute — blessed twice, once at the beginning and once on the mountain.")])
V[12] = v("HONOR_FATHER_AND_MOTHER", "Honor your father and your mother — that your days may be long on the land which the LORD your God gives you.",
  "honor your father and your mother", "that your days may be long on the land which the LORD your God gives you",
  "Utterance five; the lean lengthening.",
  [st("STATUTE BIND(kabed_av_va_em)", (0,4),
    "UTTERANCE FIVE [EX20-07 CROWN]. KABED et-AVIKHA ve-et-IMEKHA — 'HONOR your father and your mother': the fifth statute — and the KAVED-ROOT'S FINAL TURN (the machine closes the file: Pharaoh's heavy heart, Moses' heavy hands, the heavy caseload, the heavy cloud — and now kabed as command: the weight-word redeemed into HONOR: to make one's parents WEIGHTY); the Kitzur's placement-law with its English face: 'honoring parents is NEXT TO the Sabbath — as one honors the Sabbath, one honors father and mother' (the first tablet's last human-facing law leaning on the Creator's day: the readings on the three partners, named-only); lemaan YAARIKHUN yamekha — 'that your days may be LONG': the lengthening-word written LEAN (VERIFIED census-unique) — 'no length of days in THIS world, created with He — but in the WORLD TO COME, created with yod': the reward-word missing exactly the letter of the world where the reward lives.")])
V[13] = v("NO_MURDER", "You shall not murder.",
  "you shall not", "murder",
  "Utterance six; six letters.",
  [st("STATUTE FORBID(retzach)", (0,1),
    "UTTERANCE SIX [EX20-02 + EX20-03 CROWNS]. LO TIRTZACH — 'you shall not MURDER': the sixth statute — SIX LETTERS at the SIXTH utterance (VERIFIED: 'for MAN WAS CREATED ON THE SIXTH DAY' — the murder-ban sized to its victim's birthday), and one of the Torah's SIX two-word verses (VERIFIED census: murder, adultery, theft, in both Decalogues — the whole canon holds no other two-word verse): the shortest laws in the language, and the Zohar's hinge carried (MS): 'were it not for the PAUSING ACCENT, killing would be forbidden even to the court — the pause forbids and permits' (the cantillation as the law's own joint); the machine files the statute at its size: two words against the first crime the corpus ever narrated (Gen 4 — the readings, named-only).")])
V[14] = v("NO_ADULTERY", "You shall not commit adultery.",
  "you shall not", "commit adultery",
  "Utterance seven.",
  [st("STATUTE FORBID(niuf)", (0,1),
    "UTTERANCE SEVEN [EX20-03]. LO TINAF — 'you shall not commit ADULTERY': the seventh statute, the second two-word verse (VERIFIED in the six-verse census) — the Zohar's hinge again: 'without the pause, even the marriage-bed and the joy of the commandment would fall under it — the pause forbids and permits'; the machine notes the code's marriage-logic: the covenant offered as betrothal (19:4-5) writes the betrayal-ban into its core — the jealous God of 20:5 and the adultery-ban one doctrine at two scales (the readings named-only).")])
V[15] = v("NO_THEFT", "You shall not steal.",
  "you shall not", "steal",
  "Utterance eight.",
  [st("STATUTE FORBID(geneva)", (0,1),
    "UTTERANCE EIGHT [EX20-03]. LO TIGNOV — 'you shall not STEAL': the eighth statute, the third two-word verse (VERIFIED) — the tradition reads the KIDNAPPER here (the Kitzur's near-count named: lo-tignov weighed against the man-stealer — the capital theft among thefts, as the neighboring statutes are capital); the Zohar's hinge completes its three: 'without the pause, even to steal the teacher's mind in learning, or the thief's mind to bring the truth to light — the pause forbids and permits'; the machine files the triple: three two-word statutes, three pausing accents, three hinges — the terser the law, the more its music carries.")])
V[16] = v("NO_FALSE_WITNESS", "You shall not answer against your fellow as a false witness.",
  "you shall not answer against your fellow", "as a false witness",
  "Utterance nine.",
  [st("STATUTE FORBID(ed_shaqer)", (0,4),
    "UTTERANCE NINE. lo-taane ve-reakha ED SHAQER — 'you shall not ANSWER against your fellow as a FALSE WITNESS': the ninth statute — the court-crime (the machine notes the code's architecture: after the crimes of hand and bed, the crime of the MOUTH IN COURT: the Ten protect the tribunal itself — 18's judges armed with their own statute); ED — the witness-word (the readings wire Deut 5's ed shav, the two vanities, named-only): the corpus files the pairing: the third utterance guards the Name from vain lifting, the ninth guards the neighbor from vain testimony — the same crime at two altitudes.")])
V[17] = v("NO_COVETING", "You shall not covet your fellow's house; you shall not covet your fellow's wife, or his servant, or his maid, or his ox, or his donkey, or anything that is your fellow's.",
  "you shall not covet your fellow's house", "you shall not covet your fellow's wife, or his servant, or his maid, or his ox, or his donkey, or anything that is your fellow's",
  "Utterance ten; the statutes stand.",
  [st("STATUTE FORBID(chimud)", (0,3),
    "UTTERANCE TEN [EX20-13 CROWN]. lo TACHMOD bet reekha — 'you shall not COVET': the tenth statute — the code's only law against a STATE OF MIND (nine utterances police word and deed; the tenth polices wanting: the machine files the closing escalation — the Ten end inside the heart); lo tachmod ESHET reekha, ve-avdo va-amato ve-shoro va-chamoro — the inventory (the house first, then the persons and beasts: MS's codex-file: the precise texts hold SEVEN CLOSED BREAKS in the Ten and SPLIT THE TWO COVETS — the section-shape that misled some to cut the utterances differently, 'and the truth is as the sages received'); ve-KHOL asher le-reekha — 'and ANYTHING that is your fellow's': the catch-all (the readings: covet nothing, for the whole inventory is one man's peace); THE TEN NOW STAND (the machine's own count: ten statutes installed, verse two to verse seventeen — 620 letters, the CROWN; 172 words, the EQEV; alef to kaf, SURELY GOOD — all verified at the build).")])
V[18] = v("SEEING_THE_VOICES", "And all the people were seeing the voices and the torches, and the voice of the shofar, and the mountain smoking; and the people saw, and they swayed, and stood far off.",
  "and all the people were seeing the voices and the torches, and the voice of the shofar, and the mountain smoking", "and the people saw, and they swayed, and stood far off",
  "The event; the traded senses.",
  [dict(op=E, expr_en="roim_et_ha_qolot(e1); Theme(e1, ha-qolot)", he_span=(0,12),
    prose="THE SEEING [EX20-08 + EX20-09 CROWNS]. ve-khol-ha-am ROIM et-HA-QOLOT — 'and all the people were SEEING THE VOICES': THE EVENT — the senses traded at the mountain (the readings: seeing what is heard); and the voices-word is written FULL-then-LEAN, census-unique (VERIFIED) — 'this alone is so written' (the Ramah, against the Meiri) — with the torches-word likewise full-then-lean, unique (asserted): MS convicting the PRINTER twice over ('greatly confused in the Masorah and the verses — in all precise manuscripts the opposite': the printed roster inverted, corrected from manuscripts); va-yar ha-am VA-YANUU — 'and they SWAYED': the sway-verb Torah-unique (VERIFIED) — the Kitzur: 'THEREFORE WE SWAY at the study of Torah, for it was given in awe, in trembling' (the study-house's rocking traced to this verse); the twelve-mil recoil named; Isaiah's swaying doorposts the Scripture-twin ('there by an angel, here by angels'); va-yaamdu ME-RACHOQ — 'and stood FAR OFF': the machine opens the distance the next verse will legislate.")])
V[19] = v("SPEAK_YOU_WITH_US", "And they said to Moses: Speak you with us, and we will hear; and let God not speak with us, lest we die.",
  "and they said to Moses: speak you with us, and we will hear", "and let God not speak with us, lest we die",
  "The mediation demand.",
  [dict(op=D, expr_en="DECLARE(ha_am, LET(daber_ata_imanu))", he_span=(3,6),
    prose="THE DEMAND. va-yomru el-moshe DABER-ATA imanu VE-NISHMAA — 'SPEAK YOU with us, and WE WILL HEAR': the card pushed — the people PETITION FOR A MEDIATOR (the corpus's second demand-from-below, and the inverse of 17:2's: there they demanded water from Moses' hand; here they demand Moses' VOICE between them and the Voice); ve-al-yedaber imanu ELOHIM pen-NAMUT — 'let GOD not speak with us, LEST WE DIE': the machine books the exchange 19:9 predicted ('that the people may HEAR in My speaking with you') — the terror certifies the channel: prophecy is instituted at the people's own request (Deut 5:24-28's ratification and 18:16-17's law armed, the readings named-only); MS's stroke on the petition named (the segol-tzere split in the books on daber).")])
V[20] = v("FEAR_NOT_THE_TEST", "And Moses said to the people: Fear not, for in order to test you God has come — and in order that His fear be on your faces, that you sin not.",
  "and Moses said to the people: fear not, for in order to test you God has come", "and in order that His fear be on your faces, that you sin not",
  "The third test-station; the shame-cipher.",
  [p("HOLDS(le_vaavur_nasot_etkhem, t0)", (6,11),
    "THE TEST [EX20-10 CROWN]. al-TIRAU — 'FEAR NOT' — ki LE-VAAVUR NASOT etkhem ba ha-elohim — 'for IN ORDER TO TEST you God has come': the in-order word Torah-unique (VERIFIED; the Kitzur's Masorah-three runs to David's court — 'stand the test and be as David') — and the machine files the corpus's THIRD TEST-STATION: God tested with bread (16:4), the people tested at the rock (17:2,7), and the theophany itself is NASOT — the test-verb's arc closing on the mountain; u-vaavur tihye YIRATO al-PENEKHEM — 'that His FEAR be ON YOUR FACES' — the cipher EXACT (asserted at the build): yirato-al-penekhem = ZE HU BOSHET HA-PANIM ('this is SHAME-OF-FACE,' 917 = 917): 'whoever has shame of face does not quickly sin — shame restrains where anger invites'; le-vilti TECHETAU — 'that you SIN NOT': the sin-word's Torah-pair (VERIFIED): REUBEN'S 'do not sin against the boy' (Gen 42:22) and Moses' here — the corpus's two sin-not warnings: a brother's plea and a mediator's charge.")])
V[21] = v("INTO_THE_THICK_CLOUD", "And the people stood far off — and Moses drew near to the thick cloud where God was.",
  "and the people stood far off", "and Moses drew near to the thick cloud where God was",
  "The card pops; the dark = the Presence.",
  [dict(op=R, expr_en="RESULT: HOLDS(daber_ata_imanu, t1)", he_span=(3,9),
    prose="THE MEDIATION [EX20-11 CROWN]. va-yaamod ha-am ME-RACHOQ — the people hold their distance — u-moshe NIGASH el-HA-ARAFEL — 'and Moses DREW NEAR to the THICK CLOUD': the card POPS IN GEOMETRY (the demand was for a mediator; the compliance is narrated as two positions — the people far, Moses in: the office accepted by walking into it); and HA-ARAFEL = SHEKHINA (385 = 385, asserted EXACT — the dark named, by number, as exactly What it hides; the Kitzur with the mirror's English face); the approach-verb read passive (Pirkei deRabbi Eliezer, with translation: 'MICHAEL AND GABRIEL seized him by his two hands and brought him near against his will' — even the mediator must be carried into the dark); and the verb's Torah-pair asserted: JOSEPH drawing near to bow before Esau (Gen 33:7) and MOSES into the cloud — two approaches into fear: toward a brother's face, and into the dark where the Face is.")])
V[22] = v("FROM_THE_HEAVENS", "And the LORD said to Moses: So shall you say to the sons of Israel: You have seen that from the heavens I spoke with you.",
  "and the LORD said to Moses: so shall you say to the sons of Israel", "you have seen that from the heavens I spoke with you",
  "The altar-code's preamble.",
  [p("HOLDS(min_ha_shamayim_dibarti, t0)", (9,15),
    "THE PREAMBLE. ko tomar el-bene yisrael — the relay-formula (19:3's frame returns: the mediation now standard procedure); ATEM REITEM — 'YOU have seen' (19:4's eagle-verse opener re-spent: the second atem-reitem in one stack — what they saw then was Egypt's fall; what they see now is the sky speaking); ki MIN-HA-SHAMAYIM dibarti imakhem — 'that FROM THE HEAVENS I spoke with you': the machine holds the dialectic the tradition holds (Rashi at 19:20: He bent the heavens onto the mountain — descended AND from the heavens: the two verses one doctrine of undamaged transcendence): the altar-code's preamble grounds the coming law in the hearing itself — you SAW the speaking; now build accordingly.")])
V[23] = v("NO_GODS_OF_SILVER", "You shall not make with Me gods of silver, and gods of gold you shall not make for yourselves.",
  "you shall not make with Me gods of silver", "and gods of gold you shall not make for yourselves",
  "The altar-code opens.",
  [st("STATUTE FORBID(elohe_khesef_ve_zahav)", (0,6),
    "THE CODE OPENS [EX20-12]. lo taasun ITI elohe KHESEF ve-lohe ZAHAV — 'you shall not make WITH ME gods of SILVER and gods of GOLD': the altar-code's first statute (the eleventh standing law of the chapter — the Ten sealed, the applied code begins: the machine notes the seam: from the spoken constitution to its first building regulations, no narrative between); iti — 'WITH Me' (the readings: even as ornament to My service — the ban on gilding the worship itself, named-only); the mil'el stress on elohe-khesef named (one of the Masorah's three): the corpus files the code's opening move: before commanding an altar, forbid its counterfeit.")])
V[24] = v("AN_ALTAR_OF_EARTH", "An altar of earth shall you make for Me, and you shall sacrifice on it your burnt-offerings and your peace-offerings, your flock and your herd; in every place where I cause My name to be mentioned, I will come to you and bless you.",
  "an altar of earth shall you make for Me, and you shall sacrifice on it your burnt-offerings and your peace-offerings, your flock and your herd", "in every place where I cause My name to be mentioned, I will come to you and bless you",
  "The earthen altar; the minyan-cipher.",
  [st("STATUTE BIND(mizbach_adama)", (0,3),
    "THE ALTAR [EX20-12 CROWN]. mizbach ADAMA taase-li — 'an altar of EARTH shall you make for Me': the code's positive statute (earth, the humblest material — the readings on the altar as adam's namesake, named-only); ve-zavachta alav et-OLOTEKHA ve-et-SHELAMEKHA — burnt-offerings and peace-offerings (the corpus's sacrifice-vocabulary becoming statute: Jethro's meal at 18:12 was the last free-form offering; from here the altar has law); be-khol-ha-MAQOM asher AZKIR et-shemi — 'in EVERY PLACE where I cause My Name to be mentioned' — AVO elekha U-VERAKHTIKHA — 'I will COME to you and BLESS you': and AVO = TEN (asserted at the build) — the Kitzur: 'if I find TEN in the synagogue, I COME and bless you' (the minyan encoded in the coming-verb): the machine files the statute's astonishing warranty: a standing divine RESPONSE-LAW — wherever the Name is named, the coming and the blessing are self-obligated.")])
V[25] = v("NO_HEWN_STONES", "And if an altar of stones you make for Me, you shall not build them hewn; for you have lifted your sword upon it, and profaned it.",
  "and if an altar of stones you make for Me, you shall not build them hewn", "for you have lifted your sword upon it, and profaned it",
  "The sword and the altar.",
  [st("STATUTE FORBID(gazit)", (5,8),
    "THE HEWN BAN [EX20-12 CROWN]. ve-im-mizbach AVANIM taase-li — 'and if an altar of STONES' — lo-tivne ethen GAZIT — 'you shall not build them HEWN'; ki CHARBEKHA henafta aleha VA-TECHALLEHA — 'for you have lifted your SWORD upon it, AND PROFANED IT': the profane-word Torah-unique, written with NO YOD (VERIFIED; the Ramah) — and the statute's doctrine carried by the readings (named): the altar lengthens man's days and iron shortens them — 'the shortener may not be lifted over the lengthener' (the sword disqualifies the stone it touches: the corpus's first tool-purity law, and the machine notes its reach: the peace-instrument may not be manufactured by the war-instrument).")])
V[26] = v("NO_STEPS", "And you shall not go up by steps onto My altar — that your nakedness be not uncovered on it.",
  "and you shall not go up by steps onto My altar", "that your nakedness be not uncovered on it",
  "The code's last modesty.",
  [st("STATUTE FORBID(maalot)", (0,4),
    "THE STEPS BAN [EX20-12]. ve-lo-taale VE-MAALOT al-mizbechi — 'you shall not go up BY STEPS onto My altar' (the ramp inferred: the ascent graded, not stepped); asher lo-TIGALE ervatkha alav — 'that your NAKEDNESS be not UNCOVERED on it': the Kitzur's Masorah-file named ('if he uncovers on the altar — his evil is uncovered in the assembly'); the bet of ve-maalot SOFT in all books (MS against the Rav Pealim's printed claim — 'I have seen it soft in all the books': the printed-authority file's last station of the chapter); the machine seals the block's arc: the chapter that opened with the Presence descending in fire closes regulating the priest's STRIDE — fourteen statutes standing (ten spoken to the nation, four for the altar), and the law's final concern is the dignity of a man climbing to serve.")])

# ---- scenarios ----------------------------------------------------------
BASE = "no test, no name."
Dd = "LET(daber_ata_imanu) pushed and OPEN;"
def STn(n):
    return "STATUTES %d standing" % n
expects = {}
expects[1] = [BASE]
expects[2] = [STn(1), BASE]
for vs in (3, 4, 5, 6):
    expects[vs] = [STn(2), BASE]
expects[7] = [STn(3), BASE]
for vs in (8, 9, 10, 11):
    expects[vs] = [STn(4), BASE]
expects[12] = [STn(5), BASE]
expects[13] = [STn(6), BASE]
expects[14] = [STn(7), BASE]
expects[15] = [STn(8), BASE]
expects[16] = [STn(9), BASE]
for vs in (17, 18):
    expects[vs] = [STn(10), BASE]
for vs in (19, 20):
    expects[vs] = [Dd, STn(10), BASE]
for vs in (21, 22):
    expects[vs] = [STn(10), BASE]
expects[23] = [STn(11), BASE]
expects[24] = [STn(12), BASE]
expects[25] = [STn(13), BASE]
expects[26] = [STn(14), BASE]
titles = {
    1: "God spoke all these words", 2: "I am", 3: "no other gods",
    4: "no graven image", 5: "a jealous God", 6: "mercy to thousands",
    7: "the Name in vain", 8: "remember the Sabbath",
    9: "six days shall you labor", 10: "the seventh is rest",
    11: "the creation warrant", 12: "honor father and mother",
    13: "no murder", 14: "no adultery", 15: "no theft",
    16: "no false witness", 17: "no coveting", 18: "seeing the voices",
    19: "speak you with us", 20: "fear not — the test",
    21: "into the thick cloud", 22: "from the heavens",
    23: "no gods of silver", 24: "an altar of earth",
    25: "no hewn stones", 26: "no steps",
}

steps, scenarios = [], []
for i, vs in enumerate(sorted(V), 1):
    spec = V[vs]
    steps.append(unitgen.build_step(db, "Exod", "Exod", 20, vs, i, spec))
    scenarios.append(unitgen.scenario_for(
        db, "Exod", 20, vs, "S%d" % i,
        "after STEP_Ex_20_%d — %s" % (vs, titles[vs]),
        spec["en"].replace("[EN-AID] ", ""), expects[vs]))

ttl_he, ttl_tr = unitgen.join_tokens(unitgen.verse_tokens(db, "Exod", 20, 2)[0:3], strip_accents=False)

META = '''# =============================================================================
# LOGIC UNIT: Exodus 20:1-26 — the Ten Utterances and the altar-code
#             (the corpus's constitution: fourteen standing statutes)
# FORWARD ERA unit #34 — derived 2026-08-10 (oral layer in-pipeline; review waived)
# Run FWD-8 block 4.
# =============================================================================
# Experimental model — not binding religious law.

meta:
  id: "exo_20_the_ten_utterances"
  title_en: "The Ten Utterances (20:1-26)"
  title_he: %s
  title_he_translit: "%s"
  title_he_en: "'I am the LORD your God'"
  book_he: שְׁמוֹת
  book_he_translit: Shemot
  book_en: Exodus
  refs: "20:1-26"
  unit_span_planned: "20:1-26"
  data_paths_he:
  - "Data/Exod.xml"
  status: frozen
  draft_note_en: >
    DERIVED 2026-08-10 · FORWARD ERA unit #34 (run FWD-8 block 4;
    Exod 1-20 continuous behind it). Span: 20:1-26, whole
    chapter: 26 verses in the SNAPSHOT's division (the
    individual-reading verse-order; eight verses without a
    mid-verse rest, including the frame 20:1 and the four short
    prohibitions). Oral layer IN-PIPELINE: manifest 13/13
    VERIFIED, zero FAILED — see oral_audit_note_en.

    MACHINE PROFILE. FOURTEEN STATUTES, ONE DECLARE, ONE
    RESULT, ONE EVENT — the STATUTE-CLASS DEBUT in the exodus
    stack (the apodictic operator introduced at lev_19 arrives
    at its own source): the TEN UTTERANCES installed as
    standing law, one statute per utterance at its head-verse
    (the received count — anokhi and lo-yihye the first two,
    'from the mouth of the Power'), the machine literally
    counting them: STATUTES 10 STANDING at 20:17 — then the
    ALTAR-CODE's four (silver-gods ban, the earthen altar
    with its coming-and-blessing warranty, the hewn-stone
    ban, the steps ban): FOURTEEN standing at close. The one
    exchange: the people's mediation-demand (20:19
    daber-ata-imanu — prophecy instituted by petition) pops
    at 20:21 IN GEOMETRY (the people far, Moses into the
    thick cloud — the office accepted by walking into it).
    ONE EVENT: the seeing of the voices (20:18). THE DECALOGUE'S
    ARITHMETIC ALL MACHINE-VERIFIED at the build: 620 letters
    = KETER (the crown), 172 words = EQEV, alef-to-kaf =
    AKH (surely good), the sixth utterance six letters, the
    Torah's ONLY six two-word verses (both Decalogues'
    murder/adultery/theft), the zakhor-verse's sevens (verse
    7 of the span, opens with zayin, five words, seven
    resters), the double-pointed tokens (panai, mitachat —
    the two-reading system's trace in the SNAPSHOT). Wires
    closed: exo_16's six-and-one manna-frame pays at 20:8-11
    (the Sabbath commanded); the kaved-root's arc ends in
    KABED (the weight-word redeemed into honor); 19:9's
    hear-in-My-speaking certified by 20:19; 19:25's open
    mouth filled by 20:1. Queue at close: EMPTY in-unit
    (the statutes stand as world-facts, not cards).
    REGISTRY 0; TESTS 0.

    CARE-POINTS: the statute-per-utterance convention (the
    utterance-count is the received one; 20:3-6 one
    utterance, its detail-verses P-ops); the altar-code as
    four MORE statutes (10 + 4 — the count-checkpoint at
    both 20:17 and 20:26); the two-reading system (upper/
    lower cantillation — the SNAPSHOT carries double vowels
    at panai and mitachat, single pausal at tirtzach: the
    stream's shape filed, not forced); the seven closed
    sections (codex-side, not in the stream — instrument
    gap); the versification seam (the scroll-app's known
    Exod 20 gloss-chain fallback rides this chapter's
    division — pre-existing, noted). WATCHLIST ARMS: 24:12
    (the tablets — the Ten get stone), 31:18-32:19 (written
    and broken), 34:1-28 (rewritten), Deut 5 (the second
    Decalogue — the deltas: shamor, the two-word verses
    census-verified there too), Deut 4:12-13 (the voice and
    the ten), 27:5-6 (the hewn-ban re-legislated), Josh
    8:31 (the iron-free altar built). Outside-Torah names
    (named-only): Ps 62:12 (one spoke, two heard), Isa
    6:4 (the swaying doorposts), Hos 2 (the betrothal),
    the Yerushalmi of Sheqalim (the two readings), Pirkei
    deRabbi Eliezer (the seized hands).
  oral_audit_note_en: >
    ORAL AUDIT 2026-08-10 (IN-PIPELINE, forward era; manifest
    logic/oral_audit/manifests/exo_20_the_ten_utterances_claims.json
    13/13 VERIFIED, zero FAILED; record
    logic/oral_audit/AUDIT_exo_20_2026-08-10.md). CROWNS
    (chain-attested + DB-verified). THE TRIPLE-PLENE
    BROUGHT-YOU-OUT [EX20-01, KB + MS on 20:2]: הוצאתיך ("I
    brought you out") exactly THREE in the Torah (census
    checked): UR OF THE CHALDEES (Gen 15:7, to Abraham) and
    the TWO DECALOGUES — "brought from Ur to give his sons
    the Torah"; all three full-full-full (the Ramah; the
    Jerusalem Talmud's lean split named); אנכי ("I") = כסא
    ("throne," 81 = 81, asserted) — the heavens torn to the
    throne. THE CROWN-COUNT [EX20-02, KB — THE MARQUEE]:
    the Ten hold exactly 620 LETTERS = כתר ("crown": the
    613 + the sons of Noah's seven — "Torah for its own
    sake is a crown") and 172 WORDS = עקב ("because" —
    "BECAUSE Abraham heard My voice"), both machine-counted
    on the SNAPSHOT; the Ten open with alef and close with
    kaf — אך ("SURELY good to Israel"); לא תרצח — six
    letters at the sixth utterance ("man was created on the
    sixth day"). THE SIX TWO-WORD VERSES [EX20-03, the
    Chizkuni + the Zohar via MS]: the whole Torah holds
    exactly SIX verses of two words — murder, adultery,
    theft, in BOTH Decalogues (census asserted at the
    build; the anchor-verses checked) — "no verse of two
    words in Scripture except these"; the Zohar's PAUSING
    ACCENT: without the pause, killing forbidden even to
    the court, union even in marriage — "the pause forbids
    and permits." THE DOUBLE-POINTED TOKENS [EX20-04, MS's
    essay from ibn Habib]: פני ("My face") carries BOTH the
    pausal and running vowels in one token (checked
    in-token; מתחת likewise, asserted) — the TWO READINGS
    (the lone reader closes verses; the public reader reads
    each utterance whole — accents, vowels, and soft-hard
    letters all doubled); the Rama of Fano: he who reads
    both aloud is silenced with rebuke; the four
    dagesh-and-soft letters named; the SNAPSHOT's shape
    filed honestly (double at panai/mitachat, single pausal
    at tirtzach). THE KINDNESS-FILE [EX20-05, KB on 20:6]:
    ועשה חסד ("and doing kindness") three in the Torah
    (adjacency checked): the SERVANT'S PRAYER (Gen 24:12)
    and the two Decalogues — the phrase that entered as a
    servant's plea returns as the Master's pledge; David's
    pair named; the SEVEN CROWNLETS on lo-tisa's shin
    (instrument gap — the tagin above the stream). THE
    ZAKHOR ARITHMETIC [EX20-06, KB on 20:8]: FIVE words
    (checked — "the five books"), the SEVENTH verse of the
    span opening with ZAYIN (asserted), SEVEN resters
    (counted): verse seven, letter seven, roster seven. THE
    LEAN LENGTHENING [EX20-07, KB on 20:12]: יארכון ("may
    be long") census-unique lean (checked) — "no length of
    days in this world, created with He — but in the world
    to come, created with yod"; honor-beside-Sabbath (with
    the mirror's English). THE SWAYING [EX20-08, KB on
    20:18]: וינעו ("and they swayed") Torah-unique
    (checked) — "THEREFORE WE SWAY at the study of Torah";
    the twelve-mil recoil named; Isaiah's doorposts the
    twin. THE PRINTER CONVICTED TWICE [EX20-09, MS on
    20:18]: הקולת ("the voices") full-then-lean,
    census-unique (checked); הלפידם ("the torches")
    likewise (asserted) — the printed edition "greatly
    confused in the Masorah and the verses," corrected
    from the manuscripts and the Ramah. THE TEST AND THE
    SHAME [EX20-10, KB on 20:20]: לבעבור ("in order to")
    Torah-unique (checked) — the Masorah-three to David's
    court ("stand the test and be as David"); תחטאו ("you
    sin") a Torah-pair (checked): REUBEN's don't-sin and
    Moses' — a brother's plea and a mediator's charge; the
    shame-cipher EXACT: יראתו על פניכם ("His fear on your
    faces") = זה הוא בושת הפנים ("this is shame-of-face,"
    917 = 917, asserted). THE DARK = THE PRESENCE
    [EX20-11, KB on 20:21]: הערפל ("the thick cloud")
    Torah-unique (checked) = שכינה ("the Presence," 385 =
    385, asserted) — the darkness named by number as What
    it hides; נגש read passive (Pirkei deRabbi Eliezer,
    with English: Michael and Gabriel seized his hands);
    the approach-pair asserted: Joseph to Esau, Moses into
    the cloud. THE ALTAR-CODE'S LETTERS [EX20-12, MS + KB
    on 20:24-26]: ותחללה ("and profaned it") unique, no
    yod (checked; the Ramah); אבוא ("I will come") = TEN
    (asserted) — "if I find ten in the synagogue, I come
    and bless"; תגלה's Masorah-three named; במעלת soft
    against the printed hard-claim ("I have seen it soft
    in all the books"). THE SEVEN SECTIONS AND THE COUNT
    [EX20-13, MS's essay]: the precise codices hold seven
    closed breaks in the Ten, splitting the two covets
    (instrument gap — the stream carries no break-marks);
    the split misled some to un-count the first utterance —
    "the truth is as the sages received: אנכי ("I am") and
    לא יהיה ("there shall not be") ARE the two, heard from
    the mouth of the Power" (the I-am word anchored
    in-verse, checked).
  owner_language_note: >
    English for reading only. Hebrew is the derivation source.
  oral_policy_note_en: >
    Written trees first. Dual-track Oral only when named; never
    silent-merge.
  tree_derive_version: logic_derived_v1
  tree_derive_phase: "FWD-34"
  confidence_overall: "structure tested; oral layer verified 13/13"
  genre: "decalogue_statute_code"
  build_track: exodus_stack
  depends_on: exo_19_sinai_and_the_covenant
  depends_note_en: >
    Depends for PATTERN only (19:25's open mouth filled at 20:1;
    the mediation 19:9 promised and 20:19 petitioned; exo_16's
    six-and-one frame become statute; the kaved-arc redeemed
    into KABED). Standalone machine. Exod 1-20 continuous, 96
    frozen units.
''' % (ttl_he, ttl_tr)

DLOG = '''derivation_log:
  - step: A
    name_en: "Block choice"
    comment: >
      FORWARD ERA run 8, block 4 (owner: "lets do 5 more blocks").
      Canon continuation: Exod 20:1-26 — the Ten Utterances and
      the altar-code, whole chapter.
    confidence: established
  - step: B
    name_en: "Span + source + conventions"
    comment: >
      SNAPSHOT prestage: 26 verses (the individual-reading
      division; eight without mid-verse rest). Volitive census:
      the utterances are APODICTIC LAW, not demands — statute
      class (lev_19's operator at its source); ONE real
      queue-card (20:19 the mediation-demand). The utterance
      count follows the received division: anokhi and lo-yihye
      the first two; 20:3-6 one utterance.
    confidence: established
  - step: C
    name_en: "Machine structure"
    comment: >
      14 STATUTES / 1D / 1R / 1E. Ten statutes installed at the
      utterance head-verses (STATUTES 10 standing checked at
      20:17), the altar-code's four after (14 at close). The
      mediation-demand pops in geometry at 20:21. The seeing-
      event (20:18). The Decalogue's arithmetic machine-verified:
      620 letters (KETER), 172 words (EQEV), alef-to-kaf, the
      six-letter sixth, the Torah's only six two-word verses,
      the zakhor sevens, the double-pointed tokens.
    confidence: tested
  - step: D
    name_en: "Oral scan (in-pipeline)"
    comment: >
      Local mirror only (zero fetches): Minchat Shai on Exod 20
      (30 notes incl. the double-cantillation essay) + Kitzur
      Baal HaTurim on Exod 20 (22 notes) + the MS Decalogue
      essay at the 19:24 ref. Manifest 13 rows: 13 VERIFIED /
      0 FAILED / 0 UNCHECKABLE, first run. The triple-plene
      brought-you-out; the crown-count (620/172, machine-
      counted); the six two-word verses; the double-pointed
      tokens; the kindness-file; the zakhor sevens; the lean
      lengthening; the swaying; the printer convicted twice;
      the test and the shame-cipher; the dark = the Presence;
      the altar-code's letters; the seven sections and the
      received count.
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
      not silent edits. Exod 1-20 continuous.
    confidence: established
'''

unitgen.emit_unit(META, DLOG, steps, scenarios, "logic/units/exo_20_the_ten_utterances.yaml")
print("wrote logic/units/exo_20_the_ten_utterances.yaml —", len(steps), "steps,", len(scenarios), "scenarios")
