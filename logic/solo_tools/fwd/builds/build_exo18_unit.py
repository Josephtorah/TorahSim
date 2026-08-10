#!/usr/bin/env python3
"""Author exo_18_jethro_and_the_judges (Exod 18:1-27) — forward-era unit #32 (run FWD-8 block 2).
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

def adjacency(first, second_set):
    hits = []
    for b, c, v, i in db.execute("""SELECT v.book, v.chapter, v.verse, w.idx FROM words w
            JOIN verses v ON w.verse_id=v.id WHERE replace(w.he_plain,'/','')=?""", (first,)):
        nxt = db.execute("SELECT w.he_plain FROM words w JOIN verses vv ON w.verse_id=vv.id "
                         "WHERE vv.book=? AND vv.chapter=? AND vv.verse=? AND w.idx=?", (b, c, v, i + 1)).fetchone()
        if nxt and nxt[0].replace("/", "") in second_set:
            hits.append((b, c, v))
    return sorted(hits)

# ---- build-time machine evidence (asserted, not crowns) -------------------
assert adjacency("לא", {"טוב"}) == [("Exod", 18, 17), ("Gen", 2, 18)]          # the Torah's two not-goods
assert census("ויצלני") == [("Exod", 18, 4)]                                   # lean rescue 2
assert census("ויצלהו") == [("Gen", 37, 21)]                                   # lean rescue 1
assert census("תורתיו") == [("Exod", 18, 16)]                                  # His torahs, unique
assert census("לדרש") == [("Exod", 18, 15), ("Gen", 25, 22)]                   # the seekers: the nation + Rebekah
assert census("וצוך") == [("Exod", 18, 23)]                                    # the gate, unique
assert census("וזבחים") == [("Exod", 18, 12)]                                  # the meal's sacrifices, unique
assert (hp(18, 13, 12), hp(18, 13, 14)) == ("הבקר", "הערב")                     # the articles present
assert (hp(18, 14, 26), hp(18, 14, 28)) == ("בקר", "ערב")                       # the articles gone
assert (hp(18, 22, 14), hp(18, 26, 14)) == ("ישפטו", "ישפוטו")                  # the verb grows a vav
assert hp(18, 18, 15) == "עשהו"                                                # lean, per the Ramah
assert hp(18, 22, 8) == "הגדל"                                                 # lean
assert hp(18, 24, 2) == "לקול"                                                 # full
assert (hp(18, 21, 21), hp(18, 25, 18)) == ("עשרת", "עשרת")                     # the tens, lean twice
assert hp(18, 18, 10) == "כבד"                                                 # the heavy-root's third station
assert tuple(hp(18, 24, i) for i in range(8)) == ("וישמע", "משה", "לקול", "חתנו", "ויעש", "כל", "אשר", "אמר")  # the compliance
G = {"א":1,"ב":2,"ג":3,"ד":4,"ה":5,"ו":6,"ז":7,"ח":8,"ט":9,"י":10,"כ":20,"ך":20,
     "ל":30,"מ":40,"ם":40,"נ":50,"ן":50,"ס":60,"ע":70,"פ":80,"ף":80,"צ":90,"ץ":90,
     "ק":100,"ר":200,"ש":300,"ת":400}
g = lambda s: sum(G[c] for c in s if c in G)
assert g("יתרו") == g("התורה") == 616                                          # Jethro = the Torah

P = "PRECONDITION_STATE"
D = "DECLARE"
R = "RESULT"
E = "EVENT"

def v(op, en, left, right, comment, ops):
    return dict(op=op, en=en, left_en=left, right_en=right, comment=comment, operators=ops)

def p(expr, span, prose):
    return dict(op=P, expr_en=expr, he_span=span, prose=prose)

V = {}
V[1] = v("JETHRO_HEARS", "And Jethro, priest of Midian, Moses' father-in-law, heard all that God had done for Moses and for Israel His people — that the LORD had brought Israel out from Egypt.",
  "and Jethro, priest of Midian, Moses' father-in-law, heard all that God had done for Moses and for Israel His people", "that the LORD had brought Israel out from Egypt",
  "The hearing; the did-God pair.",
  [p("HOLDS(va_yishma_yitro, t0)", (0,5),
    "THE HEARING [EX18-01 CROWN]. va-YISHMA yitro khohen midyan choten moshe — 'and JETHRO HEARD': the chapter opens on the hear-verb it will close on (18:24 — Jethro heard the news; Moses will hear the counsel: the chapter is one ear answering another); WHAT he heard (the readings named): the sea's tearing 'roared until all the kings of east and west heard' — and Amalek's war (the two neighboring chapters as the broadcast); et kol-asher ASA ELOHIM le-moshe u-le-yisrael — the did-God pair (VERIFIED): Miqetz's 'what is this God has DONE to us' (the brothers' terror at the sacks) and Jethro's good news — 'in the language they grieved, in that language came their relief'; and the guest's name is its own credential (asserted at the build): YITRO = HA-TORAH, 616 = 616 — 'he came to convert and to receive the Torah' (the Kitzur's further faces named: the six names; the 613 assembled from his letters); ki HOTZI YHWH et-yisrael mi-mitzrayim — the exodus stated as the headline: the machine notes the verse's own theology: the deed credited to ELOHIM for the household, to YHWH for the nation.")])
V[2] = v("AFTER_HER_SENDING", "And Jethro, Moses' father-in-law, took Zipporah, Moses' wife — after her being sent away.",
  "and Jethro, Moses' father-in-law, took Zipporah, Moses' wife", "after her being sent away",
  "The returned household.",
  [p("HOLDS(achar_shilucheha, t0)", (4,9),
    "THE RETURN. va-yiqach yitro... et-TZIPORA eshet moshe — Zipporah RE-ENTERS (4:20 took her toward Egypt; 4:24-26's blood-bridegroom crisis was her last scene; the corpus never narrated the sending the verse now cites); ACHAR SHILUCHEHA — 'after her being SENT AWAY': the send-verb's noun on a wife (the readings the Kitzur carries: sent yet still his wife — 'a king may not take back a divorcee,' so she was never that; the Mekhilta's split on when and why, named-only): the machine holds the surface: the deliverer's own household arrives at the camp as returned freight, ahead of a chapter about what Moses can and cannot carry alone.")])
V[3] = v("GERSHOM", "And her two sons — of whom the name of the one was Gershom, for he said: A stranger have I been in a foreign land.",
  "and her two sons", "of whom the name of the one was Gershom, for he said: a stranger have I been in a foreign land",
  "The first son's name recalled.",
  [p("HOLDS(ger_hayiti_be_eretz_nakhriya, t0)", (5,12),
    "THE FIRST NAME. asher shem ha-echad GERSHOM ki amar GER HAYITI be-eretz nakhriya — Gershom's etymology REPLAYED VERBATIM from 2:22 (the corpus's registry holds the write from there; the citation is a read, not a write): 'a STRANGER have I been in a foreign land' — the machine notes what the replay does at this station: the stranger-name is recited at the tent where the strangerhood ENDS (the family reunited at the mount of God) — and the readings the Kitzur files on the naming-order (the condition with Jethro; the son wired to Jonathan the idol-priest's line) stay named-only: the corpus keeps the verse's own face.")])
V[4] = v("ELIEZER", "And the name of the one was Eliezer — for the God of my father was my help, and delivered me from the sword of Pharaoh.",
  "and the name of the one was Eliezer", "for the God of my father was my help, and delivered me from the sword of Pharaoh",
  "The second son's name — first heard.",
  [p("HOLDS(elohe_avi_be_ezri, t0)", (3,9),
    "THE SECOND NAME [EX18-02]. ve-shem ha-echad ELIEZER — 'and the name of the one was ELIEZER': the corpus LEARNS THIS NAME HERE FIRST (2:22 named only Gershom; 4:20's 'sons' rode unnamed: the registry's long-deferred second son surfaces with his etymology eighteen chapters after his birth-window — the report-class, no naming-verb: the write happened off-stage and the text files the receipt); ki elohe AVI be-EZRI — 'the God of MY FATHER was my HELP'; va-YATZILENI me-CHEREV paro — 'and DELIVERED ME from the SWORD OF PHARAOH' (2:15's flight cited as the etymology): and the rescue-verb is the SECOND OF THE RAMAH'S THREE LEAN SPELLINGS (VERIFIED census at the build; the trio: Reuben's rescue of Joseph, this rescue from the sword, 18:8's rescue of the nation — two of the three in this chapter): the boy's name carries the family's thinnest-written verb.")])
V[5] = v("TO_THE_MOUNT_OF_GOD", "And Jethro, Moses' father-in-law, came, and his sons and his wife, to Moses — to the wilderness where he was camping, the mount of God.",
  "and Jethro, Moses' father-in-law, came, and his sons and his wife, to Moses", "to the wilderness where he was camping, the mount of God",
  "The arrival; the camping participle.",
  [p("HOLDS(el_har_ha_elohim, t0)", (8,15),
    "THE ARRIVAL [EX18-03 CROWN]. va-yavo yitro... el-ha-midbar asher hu CHONE sham — 'to the wilderness where he was CAMPING': the camping-participle Torah-unique (VERIFIED) — its Scripture-twin the Psalm's angel ('the angel of the LORD CAMPS around those who fear Him'): the Kitzur — Jethro NEEDED NO DIRECTIONS: 'he saw the CLOUD TIED over the tent, and by it he knew' (the address written in sky); HAR HA-ELOHIM — 'the MOUNT OF GOD': 3:1's address recurs (the bush's mountain, 4:27's meeting-mountain, now the reunion's: the machine notes the magnetism — every homecoming in this stack lands on the same rock, one chapter before Sinai's own arrival at 19:2); MS's small stroke named: the qadma-accent riding the guest's name.")])
V[6] = v("I_YOUR_FATHER_IN_LAW", "And he said to Moses: I, your father-in-law Jethro, am coming to you — and your wife, and her two sons with her.",
  "and he said to Moses: I, your father-in-law Jethro, am coming to you", "and your wife, and her two sons with her",
  "The announcement.",
  [p("HOLDS(ani_chotenkha_ba_elekha, t0)", (3,7),
    "THE ANNOUNCEMENT. va-yomer el-moshe ANI chotenkha yitro BA elekha — 'I, your father-in-law Jethro, am COMING to you': the visitor announces himself by RELATION first, name second (choten runs THIRTEEN times in this chapter's frame — the text will barely say Jethro without saying father-in-law: the machine notes the insistence: the chapter that builds Israel's courts credits the design to kinship, not office); ve-ISHTEKHA u-shene VANEHA ima-ה — 'and YOUR WIFE, and her two sons WITH HER': the family listed as the caravan's cargo (the readings on the pronouns — HER sons — named-only).")])
V[7] = v("THE_GREETING", "And Moses went out to meet his father-in-law, and bowed, and kissed him, and they asked each man his fellow of peace — and they came into the tent.",
  "and Moses went out to meet his father-in-law, and bowed, and kissed him, and they asked each man his fellow of peace", "and they came into the tent",
  "The protocol of welcome.",
  [p("HOLDS(va_yishalu_ish_le_reehu_le_shalom, t0)", (7,10),
    "THE GREETING. va-yetze moshe liqrat chotno va-YISHTACHU va-YISHAQ-lo — Moses GOES OUT, BOWS, KISSES (the readings on who bowed to whom — 'a man to his FELLOW' read to Moses, the king bowing to the guest — named-only); va-yishalu ish le-reehu LE-SHALOM — 'they asked each man his fellow OF PEACE': the corpus's first narrated mutual shalom-exchange (4:27's brother-kiss was one-way; 18:7 is symmetric — the machine files the etiquette-protocol: the chapter of case-law opens with the law of the doorway); va-yavou HA-OHELA — 'into the TENT' (the readings: the tent = the house of study, named-only).")])
V[8] = v("MOSES_RECOUNTS", "And Moses recounted to his father-in-law all that the LORD had done to Pharaoh and to Egypt on account of Israel; all the travail that had found them on the way — and the LORD delivered them.",
  "and Moses recounted to his father-in-law all that the LORD had done to Pharaoh and to Egypt on account of Israel", "all the travail that had found them on the way — and the LORD delivered them",
  "The debrief; the third lean rescue.",
  [p("HOLDS(va_yesaper_moshe, t0)", (0,2),
    "THE TELLING [EX18-02 + EX18-04 CROWNS]. va-YESAPER moshe le-chotno — 'and Moses RECOUNTED to his father-in-law': the corpus's first PERSONAL DEBRIEF (the deeds so far narrated by the text or sung by the nation; here they are TOLD, one man to one man, as news — the readings: 'to draw his heart near to the Torah,' named-only); al ODOT yisrael — 'on account of ISRAEL': the on-account word with its first vav FULL — MS convicting the PRINTED MASORAH of corruption (the four-count ruled wrong; the Ramah: TWO in the Torah, VERIFIED census): Abraham's grief on account of HIS SON and this telling on account of ISRAEL — both full-vav on-accounts on account of a son (4:22's My-firstborn); et kol-ha-TELAA — 'all the TRAVAIL on the way'; va-YATZILEM YHWH — 'and the LORD DELIVERED THEM': THE THIRD LEAN RESCUE (VERIFIED: the Ramah's roster — Reuben's, the sword's at 18:4, the nation's here; everywhere else the yod stands full): the debrief closes on the family's thin verb, now nation-sized.")])
V[9] = v("JETHRO_REJOICES", "And Jethro rejoiced over all the good which the LORD had done for Israel — that He had delivered him from the hand of Egypt.",
  "and Jethro rejoiced over all the good which the LORD had done for Israel", "that He had delivered him from the hand of Egypt",
  "The unique joy.",
  [p("HOLDS(va_yichad_yitro, t0)", (0,1),
    "THE JOY [EX18-05 CROWN]. va-YICHAD yitro al kol-ha-TOVA — 'and Jethro REJOICED over all the GOOD': the rejoicing-verb Torah-unique (VERIFIED; MS's Masorah names the one Scripture-twin: Job's 'let no JOY enter it' — the night cursing what Jethro feels); the Kitzur's two faces carried whole: 'he made his heart ONE to the One God — and became a Jew' / 'his flesh became PRICKLES upon prickles over Egypt's ruin' (the convert's joy with the convert's shudder in one skeleton; the dalet's stroke over a silent rest, the Mikhlol — checked at the build); asher HITZILO mi-yad mitzrayim — 'that He delivered HIM': the expected-but-not-written station (MS: 'one supposes THEM; the reading is HIM' — the sevirin class): the machine files the grammar's verdict: the delivered nation counted as one body — and the joy-verb spent on it once in the whole Torah.")])
V[10] = v("BLESSED_BE_THE_LORD", "And Jethro said: Blessed be the LORD, who delivered you from the hand of Egypt and from the hand of Pharaoh — who delivered the people from under the hand of Egypt.",
  "and Jethro said: blessed be the LORD, who delivered you from the hand of Egypt and from the hand of Pharaoh", "who delivered the people from under the hand of Egypt",
  "The doxology.",
  [p("HOLDS(barukh_YHWH, t0)", (2,10),
    "THE BLESSING [EX18-06 CROWN]. BARUKH YHWH — 'BLESSED BE THE LORD': the priest of Midian blesses the Name (the Masorah files even its pointing: the Name under the little-upright pause, VERIFIED mark) — the corpus's first narrated human blessing of the LORD since MELCHIZEDEK ('blessed be God Most High, who delivered your foes,' Gen 14:20 — twice in the canon a FOREIGN PRIEST blesses the Deliverer before Israel's own liturgy exists; the readings that sharpen it, named-only); asher HITZIL etkhem... mi-tachat YAD mitzrayim — the delivered-verb's third run in two verses, and the HAND-ledger closes: 3:19-20's hand-against-hand forecast, 14:31's great hand seen — 18:10 files Egypt's hand as the thing crawled out from UNDER (the machine notes the blessing's anatomy: two hands named and one Name blessing over both).")])
V[11] = v("NOW_I_KNOW", "Now I know that the LORD is greater than all the gods — for in the thing in which they dealt proudly, against them.",
  "now I know that the LORD is greater than all the gods", "for in the thing in which they dealt proudly, against them",
  "The know-ledger's foreign account.",
  [p("HOLDS(ata_yadati, t0)", (0,6),
    "THE CREED. ATA YADATI ki-GADOL YHWH mi-kol-ha-ELOHIM — 'NOW I KNOW that the LORD is greater than all the gods': THE KNOW-LEDGER'S FIRST VOLUNTARY FOREIGN DEPOSIT (Egypt was made to know by drowning, 14:4/18; Israel promised knowing by supper, 16:12; Jethro walks in and FILES HIS OWN — the priest of another altar auditing all altars: the readings on 'he had tried every idolatry,' named-only); ki VA-DAVAR asher ZADU alehem — 'for in the THING in which they DEALT PROUDLY — against them': the measure-for-measure clause (the readings: the water they schemed with became the water over them — the pot cooked in its own plot; named-only): the machine books the entry as the ledger's cleanest line: knowledge reached by comparison shopping, sealed by symmetry.")])
V[12] = v("THE_MEAL_BEFORE_GOD", "And Jethro, Moses' father-in-law, took a burnt-offering and sacrifices for God; and Aaron came, and all the elders of Israel, to eat bread with Moses' father-in-law before God.",
  "and Jethro, Moses' father-in-law, took a burnt-offering and sacrifices for God", "and Aaron came, and all the elders of Israel, to eat bread with Moses' father-in-law before God",
  "The event; the convert's table.",
  [dict(op=E, expr_en="zevach_yitro(e1); Agent(e1, yitro); Theme(e1, ola_u_zvachim)", he_span=(0,6),
    prose="THE OFFERING. va-yiqach yitro... OLA u-ZVACHIM le-ELOHIM — 'a BURNT-OFFERING and SACRIFICES for God': THE EVENT — the corpus's first narrated sacrifice since Egypt was left (the altar-file's Exodus opener is a CONVERT'S: the and-sacrifices form Torah-unique, asserted at the build), brought by the priest of Midian the verse before Israel's own law arrives; va-yavo AHARON ve-khol ZIQNE yisrael le-ekhol-LECHEM im-choten moshe LIFNE HA-ELOHIM — 'to eat BREAD... BEFORE GOD': the elders' table set at the Presence (the readings: 'whoever enjoys a meal at which scholars sit enjoys the radiance' — and the missing host: where is MOSES? standing and serving, the tradition answers — named-only): the machine files the scene: Israel's first interfaith state dinner, catered by the guest, addressed to the Host.")])
V[13] = v("THE_COURT_DAY", "And it was on the morrow, that Moses sat to judge the people; and the people stood over Moses from the morning until the evening.",
  "and it was on the morrow, that Moses sat to judge the people", "and the people stood over Moses from the morning until the evening",
  "The bottleneck pictured.",
  [p("HOLDS(va_yeshev_moshe_lishpot, t0)", (7,14),
    "THE COURT [EX18-07 CROWN]. va-yehi MI-MACHORAT — 'on the MORROW' (the Kitzur's with-the-words count to 'the morrow of the Day of Atonement' named as the tradition's device — the docket read as Moses down from the mount); va-YESHEV moshe LISHPOT et-ha-am — Moses SITS TO JUDGE (the judge-verb opens its chapter-long run); va-yaamod ha-am al-moshe min-HA-BOQER ad-HA-AREV — 'from THE morning until THE evening': the narration spends BOTH ARTICLES on the court-day — and Jethro's replay one verse down DROPS THEM (bare boqer, bare arev — VERIFIED both at the build): the Kitzur counts the two spare letters: He and He — 'the judge who judges truly is made a PARTNER to the Holy One in the work of creation, created with He' (the narrator grants the creation-letters; the complaint strips them); the six-hour bench-rule named (ad, not ve-ad): the machine files the picture the verse takes: one seated man, a nation on its feet, and a day measured at both ends.")])
V[14] = v("WHY_ALONE", "And Moses' father-in-law saw all that he was doing for the people — and he said: What is this thing that you are doing for the people? Why do you sit alone, and all the people stand over you from morning until evening?",
  "and Moses' father-in-law saw all that he was doing for the people", "and he said: what is this thing that you are doing for the people? why do you sit alone, and all the people stand over you from morning until evening?",
  "The consultant's question.",
  [p("HOLDS(madua_ata_yoshev_levadekha, t0)", (17,20),
    "THE QUESTION. va-YAR choten moshe — the father-in-law SEES (the chapter's verbs: he heard, he came, now he WATCHES — the corpus's first process-audit); MA-ha-davar ha-ze asher ATA OSE la-am — 'WHAT is this thing that YOU are doing for the people'; MADUA ata yoshev LEVADEKHA — 'WHY do you sit ALONE': the alone-word lands (the machine arms it: 18:18 will answer it with the Torah's second not-good — Eden's pair); min-BOQER ad-AREV — the same day, STRIPPED of its articles (the He's of partnership are the narrator's to give, not the visitor's — VERIFIED at the build): the outsider sees the hours; the text alone sees the creation-letters in them.")])
V[15] = v("TO_SEEK_GOD", "And Moses said to his father-in-law — because the people come to me to seek God.",
  "and Moses said to his father-in-law", "because the people come to me to seek God",
  "The docket named.",
  [p("HOLDS(lidrosh_elohim, t0)", (3,8),
    "THE ANSWER [EX18-08 CROWN]. ki-yavo elai ha-am LIDROSH ELOHIM — 'because the people come to me TO SEEK GOD': the phrase's only Torah station (VERIFIED adjacency; the Kitzur's Scripture-four: Saul over the donkeys, David over the plague, Uzziah in the war — 'for ALL their needs they came to seek God': the lost, the sick, the besieged); and the bare seek-verb's Torah-twin is REBEKAH (asserted at the build: 'and she went TO SEEK the LORD,' Gen 25:22): the corpus's first seeker carried a war in her body; the nation brings its questions to a tent — the machine notes what Moses claims: not that he judges, but that THEY SEEK: the docket described from the plaintiff's side.")])
V[16] = v("STATUTES_AND_TORAHS", "When they have a matter, it comes to me, and I judge between a man and his fellow — and I make known the statutes of God, and His torahs.",
  "when they have a matter, it comes to me, and I judge between a man and his fellow", "and I make known the statutes of God, and His torahs",
  "The plural law before Sinai.",
  [p("HOLDS(ve_hodati_et_chuqe_ha_elohim, t0)", (11,16),
    "THE DOCKET [EX18-08]. ki-yihye lahem DAVAR ba elai — 'when they have a MATTER, it comes to me'; ve-SHAFATTI ben ish u-ven reehu — 'and I JUDGE between a man and his fellow' (the judge-verb's second station of the chapter's run); ve-HODATI et-CHUQE ha-elohim ve-et-TOROTAV — 'and I make known the statutes of God and HIS TORAHS': the word Torah-unique in this plural (VERIFIED) — the Kitzur: its two Scripture-twins stand in EZEKIEL'S TEMPLE-vision ('a hint of the building of the Sanctuary') — the machine files the astonishment plainly: TORAHS, plural, cited as existing case-law BEFORE SINAI (the readings on what law Moses taught at Marah's statute-station, 15:25, named-only): the docket already runs on a library the mountain has not yet published.")])
V[17] = v("NOT_GOOD", "And Moses' father-in-law said to him: Not good is the thing that you are doing.",
  "and Moses' father-in-law said to him", "not good is the thing that you are doing",
  "The Torah's second not-good.",
  [p("HOLDS(lo_tov_ha_davar, t0)", (4,9),
    "THE VERDICT. LO-TOV ha-davar asher ata ose — 'NOT GOOD is the thing that you are doing': the corpus's SECOND not-good (asserted at the build: the adjacency stands exactly TWICE in the Torah — EDEN'S 'not good the man's being ALONE' (Gen 2:18) and here — and both indict the same condition: 18:14's LEVADEKHA, you sit ALONE, answered by 2:18's LEVADO): the machine files the frame-signature: the last time the text said not-good, it built the man a partner; Jethro is about to prescribe seventy-eight thousand of them (the readings on the audacity — a Midianite priest grading the prophet's workflow, and the Torah printing the grade — named-only); MS's stroke-file on the verse named: the lengthener on asher, the low-pause on ata.")])
V[18] = v("YOU_WILL_WILT", "You will surely wilt — both you and this people that is with you; for the thing is too heavy for you — you cannot do it alone.",
  "you will surely wilt — both you and this people that is with you", "for the thing is too heavy for you; you cannot do it alone",
  "The diagnosis; the heavy-root's third station.",
  [p("HOLDS(navol_tibol, t0)", (9,16),
    "THE DIAGNOSIS [EX18-09 CROWN]. NAVOL TIBOL — 'you will surely WILT' (the doubled leaf-wither verb: burnout as botany); gam-ATA gam-ha-AM — 'both YOU and THIS PEOPLE' (the queue damages both its ends); ki-KHAVED mimkha ha-davar — 'for the thing is TOO HEAVY for you': the kaf under the guard-stroke (VERIFIED in-token) — and the machine files the root's arc (asserted): the heavy HEART (Pharaoh, nine plagues), the heavy HANDS (17:12), now the heavy CASELOAD — the first heaviness in the file that DELEGATION can cure; lo-tukhal ASOHU levadekha — 'you cannot DO IT alone': the do-word written LEAN (the printed Masorah's 'none like it and full' ruled AN ERROR — most copies and the Ramah: lean, VERIFIED skeleton): the printed-authority file lands on the very word Jethro says cannot be done single-handed.")])
V[19] = v("HEAR_MY_VOICE", "Now hear my voice — I will counsel you, and God be with you; be you for the people toward God, and bring you the matters to God.",
  "now hear my voice — I will counsel you, and God be with you", "be you for the people toward God, and bring you the matters to God",
  "The counsel card pushed.",
  [dict(op=D, expr_en="DECLARE(yitro, LET(shema_be_qoli_iatzkha))", he_span=(0,6),
    prose="THE COUNSEL [EX18-11 CROWN]. ata SHEMA be-QOLI — 'now HEAR MY VOICE': the card pushed (a human counselor files a card at the prophet — the corpus's first ADVISORY declare: not a command, an offer with a blessing riding it: vi-YHI ELOHIM IMAKH, 'and God be with you'); IATZKHA — 'I will COUNSEL you': the counsel-verb's Torah-census exactly TWO (VERIFIED): JETHRO here and BALAAM (Num 24:14, 'come, I will counsel you') — the corpus's two outside counselors under one verb, the builder of Israel's courts and the architect of its snare (the Kitzur's doctrine: Moses HEEDED and 'shall come to his place in peace'; Zedekiah refused Jeremiah's and lost his place — counsel heard keeps a man his place); HEYE ATA la-am MUL ha-elohim — 'BE YOU for the people TOWARD God': the job re-scoped upward (the interface retained, the queue re-routed); ve-heveta ata et-ha-devarim el-ha-elohim — the hard channel kept open to the top.")])
V[20] = v("WARN_AND_TEACH", "And you shall warn them of the statutes and the torahs — and make known to them the way they shall walk in, and the deed they shall do.",
  "and you shall warn them of the statutes and the torahs", "and make known to them the way they shall walk in, and the deed they shall do",
  "The unique warn-word.",
  [p("HOLDS(ve_hizharta_ethem, t0)", (0,5),
    "THE TEACHING [EX18-10 CROWN]. VE-HIZHARTA ETHEM et-ha-CHUQIM ve-et-ha-TOROT — 'and you shall WARN THEM of the statutes and the torahs': the warn-word written with a FINAL HE — 'and NONE LIKE IT in the reading' (VERIFIED census-unique; MS) — and the midrash counts the surplus (Lekach Tov, the Kitzur): the He of the warning and the He of the warned — FIVE AND FIVE — 'these are the TEN UTTERANCES' (the teaching-command carrying Sinai's number two chapters early); ha-CHUQIM under the guard-stroke (checked at the build); ve-hodata lahem et-ha-DEREKH yelkhu VAH — 'the WAY they shall walk in' (printed-authority: the presses' intruding relative-word struck — MS); ve-et-ha-MAASE asher YAASUN — 'and the DEED they shall do': the machine files the curriculum's order: statutes, torahs, way, deed — law taught downhill from text to footstep (the readings that hang livelihood, visiting the sick, burial, and beyond-the-line on these four, named-only).")])
V[21] = v("MEN_OF_WORTH", "And you shall see out of all the people men of worth, fearers of God, men of truth, haters of gain — and set over them princes of thousands, princes of hundreds, princes of fifties, and princes of tens.",
  "and you shall see out of all the people men of worth, fearers of God, men of truth, haters of gain", "and set over them princes of thousands, princes of hundreds, princes of fifties, and princes of tens",
  "The job description; the four tiers.",
  [p("HOLDS(anshe_chayil_yire_elohim, t0)", (4,11),
    "THE ROSTER [EX18-12]. ve-ata TECHEZE mi-kol-ha-am — 'and you shall SEE OUT of all the people' (the seer-verb for the search: leadership recruited by vision, the readings on the prophetic screen named-only); the FOUR QUALIFICATIONS: anshe-CHAYIL (worth), yire ELOHIM (fearers of God), anshe EMET (truth), sone VATZA (haters of gain — the one-codex binder-stroke named, MS): the corpus's first published JOB DESCRIPTION — character-criteria only, no birth, no tribe (the machine notes what is absent: lineage — the courts open on merit while the priesthood will close on blood); sare ALAFIM, MEOT, CHAMISHIM, ASAROT — thousands, hundreds, fifties, TENS (the tens-word LEAN both times, VERIFIED at the build; the readings' arithmetic — 78,600 officers for 600,000 — named-only): the pyramid drawn in four words.")])
V[22] = v("GREAT_AND_SMALL", "And they shall judge the people at every time; and it shall be: every great matter they shall bring to you, and every small matter they shall judge themselves — and lighten it from off you, and they shall bear with you.",
  "and they shall judge the people at every time; and it shall be: every great matter they shall bring to you, and every small matter they shall judge themselves", "and lighten it from off you, and they shall bear with you",
  "The routing rule.",
  [p("HOLDS(ve_haqel_me_alekha, t0)", (16,19),
    "THE ROUTING [EX18-13]. ve-SHAFTU et-ha-am be-khol-ET — 'and they shall judge the people AT EVERY TIME' (the queue goes continuous: no more one-day bottleneck); kol-ha-davar ha-GADOL yaviu elekha — the GREAT matter up (the great-word lean, VERIFIED at the build — absent from the full-roster of Noah's parasha), ve-khol-ha-davar ha-QATON yishptu-HEM — the SMALL they judge (the judging-verb here LEAN — armed: 18:26 will replay this clause with the verb GROWN A VAV); ve-HAQEL me-alekha — 'and LIGHTEN it from off you': the heavy-diagnosis (18:18 khaved) answered by its own antonym (the machine closes the arc: the chapter is one mass-transfer problem — kaved in, haqel out); ve-NASU itakh — 'and they shall BEAR WITH you': the carrying shared (Numbers 11's seventy elders armed, the readings named-only).")])
V[23] = v("TO_ITS_PLACE_IN_PEACE", "If you do this thing, and God command you, then you will be able to stand — and also all this people will come to its place in peace.",
  "if you do this thing, and God command you, then you will be able to stand", "and also all this people will come to its place in peace",
  "The gated forecast.",
  [p("HOLDS(al_meqomo_yavo_ve_shalom, t0)", (9,16),
    "THE FORECAST [EX18-11]. im et-ha-davar ha-ze taase VE-TZIVKHA ELOHIM — 'if you do this thing AND GOD COMMAND YOU': the counselor GATES HIS OWN COUNSEL on the divine countersignature (the command-word Torah-unique, VERIFIED at the build; its Scripture-twin 'and He command you as RULER' — the Kitzur: with the commissioning, you can stand; without it, no standing): the corpus's most self-limiting card — advice that requires ratification to bind; ve-yakholta AMOD — 'you will be able to STAND' (the wilting reversed); ve-gam kol-ha-am ha-ze AL-MEQOMO yavo VE-SHALOM — 'and also all this people will come TO ITS PLACE IN PEACE': the place-phrase's Job-twin named (the Kitzur: 'judge below and there is peace; if not, judgment is done above — and you shall look on his place, and he is not'): the machine notes the forecast's scope — the reform is priced not in Moses' relief but in the PEOPLE'S arrival: good process as the nation's way home.")])
V[24] = v("MOSES_HEARS", "And Moses heard the voice of his father-in-law — and did all that he had said.",
  "and Moses heard the voice of his father-in-law", "and did all that he had said",
  "The card pops.",
  [dict(op=R, expr_en="RESULT: HOLDS(shema_be_qoli_iatzkha, t1)", he_span=(0,7),
    prose="THE HEEDING [EX18-12 CROWN]. va-YISHMA moshe LE-QOL chotno — 'and Moses HEARD THE VOICE of his father-in-law': the card POPS on the hear-verb that opened the chapter (18:1 Jethro heard of Israel; 18:24 Moses hears Jethro: the chapter rings closed ear to ear) — and the voice-word is written FULL (VERIFIED skeleton; the Ramah's rule: every Torah voice-form full but five — the voice Moses obeys carries its whole letter); va-YAAS KOL ASHER AMAR — 'and DID ALL that he had said' (asserted): the compliance-formula, unqualified (the machine files the credential in reverse: the prophet who relays God's law takes a man's advice whole — the readings on which parts waited for God's ratification, named-only, riding 18:23's gate).")])
V[25] = v("THE_JUDGES_INSTALLED", "And Moses chose men of worth out of all Israel, and gave them heads over the people — princes of thousands, princes of hundreds, princes of fifties, and princes of tens.",
  "and Moses chose men of worth out of all Israel, and gave them heads over the people", "princes of thousands, princes of hundreds, princes of fifties, and princes of tens",
  "The pyramid built.",
  [p("HOLDS(va_yiten_otam_rashim, t0)", (0,8),
    "THE INSTALLATION [EX18-12]. va-YIVCHAR moshe anshe-CHAYIL mi-kol-yisrael — 'and Moses CHOSE men of WORTH out of all Israel' (the machine notes the delta against the spec: 18:21 listed FOUR qualifications; the execution names ONE — worth (the readings: only that grade was found in supply; the spec-versus-delivery seam, named-only — the corpus files the shortfall as data, not failure); va-yiten otam RASHIM al-ha-am — 'and gave them HEADS over the people': the appointment executed; sare alafim, meot, chamishim, asarot — the four-tier pyramid stood up verbatim (the tens LEAN again, the hundreds FULL — VERIFIED at the build: the roster's letters keep their discipline through the repetition).")])
V[26] = v("THE_HARD_TO_MOSES", "And they judged the people at every time; the hard matter they would bring to Moses, and every small matter they would judge themselves.",
  "and they judged the people at every time", "the hard matter they would bring to Moses, and every small matter they would judge themselves",
  "The verb grows a letter.",
  [p("HOLDS(yishputu_hem, t0)", (11,15),
    "THE PRACTICE [EX18-13 CROWN]. ve-shaftu et-ha-am be-khol-et — the standing docket (the judge-verb's run through the chapter closes here); et-ha-davar ha-QASHE yeviun el-moshe — 'the HARD matter to Moses' (the Kitzur's wire: the HARD matter beside the STIFF neck, Deut 31:27 — 'Moses judged the cases of the stiff-necked'; and the delta named: 18:22 routed the GREAT matter up, 18:26 routes the HARD — the readings on size versus difficulty, named-only: practice re-sorted the docket by what actually needs the prophet); ve-khol-ha-davar ha-qaton YISHPUTU hem — and the judging-verb comes back GROWN A VAV (VERIFIED: the long spelling Torah-unique, against 18:22's lean twin in the same clause — MS climbing the grammarians for its long-stressed reading, the Mikhlol twice): the machine files the letter where it landed: the verb gained its vav in the verse where the judging became real.")])
V[27] = v("THE_SEND_OFF", "And Moses sent his father-in-law away — and he went him to his land.",
  "and Moses sent his father-in-law away", "and he went him to his land",
  "The consultant departs.",
  [p("HOLDS(va_yelekh_lo_el_artzo, t0)", (4,7),
    "THE DEPARTURE. va-YESHALACH moshe et-chotno — 'and Moses SENT his father-in-law away' (the send-verb that ran the exodus — shalach, nine chapters of let-My-people-go — spent here on a blessing-bearing guest: the machine notes the verb's gentlest station in the book); va-YELEKH LO el-ARTZO — 'and he went HIM to his land': the reflexive going (the readings hear lekh-lekha's shadow — the go-for-yourself of Gen 12:1 echoed in a Midianite's homeward turn; and the Mekhilta's errand: 'he went to convert his family' — named-only): the corpus closes the visit in the chapter it opened — the counselor arrives hearing and leaves heard, and the courts he drew stay standing behind him.")])

# ---- scenarios ----------------------------------------------------------
BASE = "no test, no name."
Dcoun = "LET(shema_be_qoli_iatzkha) pushed and OPEN;"
expects = {}
for vs in range(1, 19):
    expects[vs] = [BASE]
for vs in (19, 20, 21, 22, 23):
    expects[vs] = [Dcoun, BASE]
for vs in (24, 25, 26, 27):
    expects[vs] = [BASE]
titles = {
    1: "Jethro hears", 2: "after her sending", 3: "Gershom", 4: "Eliezer",
    5: "to the mount of God", 6: "I, your father-in-law", 7: "the greeting",
    8: "Moses recounts", 9: "Jethro rejoices", 10: "blessed be the LORD",
    11: "now I know", 12: "the meal before God", 13: "the court day",
    14: "why alone", 15: "to seek God", 16: "statutes and torahs",
    17: "not good", 18: "you will wilt", 19: "hear my voice",
    20: "warn and teach", 21: "men of worth", 22: "great and small",
    23: "to its place in peace", 24: "Moses hears",
    25: "the judges installed", 26: "the hard to Moses", 27: "the send-off",
}

steps, scenarios = [], []
for i, vs in enumerate(sorted(V), 1):
    spec = V[vs]
    steps.append(unitgen.build_step(db, "Exod", "Exod", 18, vs, i, spec))
    scenarios.append(unitgen.scenario_for(
        db, "Exod", 18, vs, "S%d" % i,
        "after STEP_Ex_18_%d — %s" % (vs, titles[vs]),
        spec["en"].replace("[EN-AID] ", ""), expects[vs]))

ttl_he, ttl_tr = unitgen.join_tokens(unitgen.verse_tokens(db, "Exod", 18, 19)[0:4], strip_accents=False)

META = '''# =============================================================================
# LOGIC UNIT: Exodus 18:1-27 — Jethro: the hearing, the meal, and the courts
#             (the corpus's first delegation)
# FORWARD ERA unit #32 — derived 2026-08-10 (oral layer in-pipeline; review waived)
# Run FWD-8 block 2.
# =============================================================================
# Experimental model — not binding religious law.

meta:
  id: "exo_18_jethro_and_the_judges"
  title_en: "Jethro and the judges (18:1-27)"
  title_he: %s
  title_he_translit: "%s"
  title_he_en: "'now hear my voice — I will counsel you'"
  book_he: שְׁמוֹת
  book_he_translit: Shemot
  book_en: Exodus
  refs: "18:1-27"
  unit_span_planned: "18:1-27"
  data_paths_he:
  - "Data/Exod.xml"
  status: frozen
  draft_note_en: >
    DERIVED 2026-08-10 · FORWARD ERA unit #32 (run FWD-8 block 2;
    Exod 1-18 continuous behind it). Span: 18:1-27, whole
    chapter: 27 verses (SNAPSHOT-verified). Oral layer
    IN-PIPELINE: manifest 13/13 VERIFIED, zero FAILED — see
    oral_audit_note_en.

    MACHINE PROFILE. ONE DECLARE, ONE RESULT, ONE EVENT — the
    lightest command-load since the forward era opened, and
    deliberately so: the chapter is a HEARING, not a decree.
    The one card is ADVISORY (18:19 shema-be-qoli — a human
    counselor files at the prophet; the corpus's first
    advisory declare), self-gated on the divine
    countersignature (18:23 ve-tzivkha, the command-word
    unique), and pops at 18:24 on the hear-verb that opened
    the chapter (18:1 Jethro heard / 18:24 Moses heard — the
    chapter rings closed ear to ear) with the unqualified
    compliance-formula (va-yaas kol asher amar, asserted).
    ONE EVENT: the convert's offering (18:12 — the corpus's
    first narrated sacrifice since leaving Egypt;
    u-zvachim unique, asserted; the elders eat before God).
    The KNOW-LEDGER takes its first voluntary foreign deposit
    (18:11 ata yadati — Egypt knew by drowning, Jethro by
    comparison). REGISTRY 0 (Gershom's name is a READ of
    2:22's write; ELIEZER surfaces as report-class — the
    corpus learns the second son's name here first, no
    naming-verb, registry deferred to the run-end entity
    file). MACHINE EVIDENCE asserted at the build: the
    Torah's TWO not-goods (adjacency census: Gen 2:18 Eden's
    alone / 18:17 Jethro's alone — both indict aloneness);
    the kaved-root's third station (Pharaoh's heart, Moses'
    hands, now the caseload — the first heaviness delegation
    can cure, answered by 18:22 ve-haqel); the lean-rescue
    trio (ve-yatzilehu Gen 37:21 / va-yatzileni 18:4 /
    va-yatzilem 18:8 — two of three in-span); the seek-verb's
    pair (18:15 + Rebekah Gen 25:22); yishptu/yishputu — the
    delegation-clause's verb grown a vav between plan (18:22)
    and practice (18:26); the articles dropped between 18:13
    and 18:14 (the He's of partnership); Jethro = the-Torah
    (616). Queue at close: EMPTY in-unit (the standing opens
    ride). TESTS 0.

    CARE-POINTS: the advisory card's gate (the counsel binds
    only through God's ratification — the pop at 18:24 is
    Moses adopting, not God commanding; the readings on
    which clauses waited, named-only); the spec-vs-delivery
    seam (18:21's four qualifications, 18:25's one — filed
    as data); the great-vs-hard re-sort (18:22 plan routes
    by SIZE, 18:26 practice by DIFFICULTY); Zipporah's
    unnarrated sending (achar shilucheha cites an off-stage
    event); Eliezer's deferred name (report-class, no
    registry write — entity file at run-end). WATCHLIST
    ARMS: 19:1-2 (the Sinai arrival — the mount of God
    becomes THE mount); 24:14 (the elders + Hur hold the
    camp — the delegation tested); Num 10:29-32 (Hobab
    asked to stay — the family's road-fork); Num 11:14-17
    (I cannot alone — the seventy; the kaved-file's next
    station); Deut 1:9-18 (Moses retells this chapter —
    the retrospective's deltas). Outside-Torah names
    (named-only): 1 Sam 9 (Saul's seeking), 2 Sam 24 / 1
    Chr 21 (David's plague-seeking), 2 Chr 26 (Uzziah),
    Ps 34:8 (the camping angel), Job 3:6 (the joy-ban),
    Judg 1:16 (Jethro's sons in the land), Ezek 43-44
    (the torahs of the house).
  oral_audit_note_en: >
    ORAL AUDIT 2026-08-10 (IN-PIPELINE, forward era; manifest
    logic/oral_audit/manifests/exo_18_jethro_and_the_judges_claims.json
    13/13 VERIFIED, zero FAILED; record
    logic/oral_audit/AUDIT_exo_18_2026-08-10.md). CROWNS
    (chain-attested + DB-verified). THE DID-GOD PAIR
    [EX18-01, KB on 18:1]: עשה אלהים ("God did") adjacency
    exactly twice (checked): Miqetz's terror ("what is this
    God has done to us," Gen 42:28) and Jethro's good news —
    "in the language they grieved, in that language came
    their relief"; what he heard: the sea's roar + Amalek's
    war; יתרו = התורה (616 = 616, asserted) — "he came to
    receive the Torah"; the six names; the 613 from his
    letters (named). THE THREE LEAN RESCUES [EX18-02, MS on
    18:8 with the Ramah]: the rescue-verb lean (no yod)
    exactly three times in the Torah — ויצלהו (Reuben, Gen
    37:21), ויצלני (from Pharaoh's sword, 18:4), ויצלם (the
    nation, 18:8; checked, others asserted) — two of the
    three in this chapter: brother-of-brother, God-of-a-
    fugitive, God-of-a-nation on one thinned skeleton. THE
    CAMPING ANGEL [EX18-03, KB + MS on 18:5]: חנה
    ("camping") participle Torah-unique (checked) — Psalm
    34's twin: "the angel of the LORD camps around His
    fearers" — Jethro needed no directions: he saw the cloud
    tied over the tent; the qadma on the guest's name. THE
    ON-ACCOUNT PAIR [EX18-04, MS on 18:8]: אודת with first
    vav full — the PRINTED MASORAH CONVICTED of corruption
    (its four-count smuggled in Toledot's well; the Menachat
    Cohen misled): the Ramah + manuscript Masorah: TWO in
    the Torah (census checked) — Abraham's "on account of
    his SON" (Gen 21:11) and "on account of ISRAEL": both
    full-vav on-accounts on account of a son (4:22's
    My-firstborn). THE UNIQUE JOY [EX18-05, KB + MS on
    18:9]: ויחד ("and he rejoiced") Torah-unique (checked;
    the Masorah's one Scripture-twin: Job's "let no joy
    enter it"); the two faces — heart made ONE / flesh gone
    prickles; the dalet's stroke on a silent rest (the
    Mikhlol); and the expected-but-not-written: הצילו ("He
    delivered HIM") where one supposes "them" — the nation
    one body. THE POINTED BLESSING [EX18-06, MS on 18:10]:
    ברוך יהוה ("blessed be the LORD") — the Name under the
    little-upright pause (mark checked): the first human
    blessing of the LORD since Melchizedek — both from
    foreign priests. THE CREATION-LETTERS [EX18-07, KB on
    18:13]: the court-day with BOTH articles — הבקר ("THE
    morning")... הערב ("THE evening"), checked — where
    Jethro's replay drops them (18:14 bare, asserted) — the two spare He's: "the true judge is a
    partner in the creation, created with He"; the six-hour
    bench; the morrow (named). THE SEEK-FILE [EX18-08, KB
    on 18:15-16]: לדרש אלהים ("to seek God") — the Torah's
    only station (adjacency checked; the Scripture-four:
    Saul's donkeys, David's plague, Uzziah's war — "for all
    their needs"); the bare verb's Torah-twin REBEKAH (Gen
    25:22, asserted); תורתיו ("His torahs," plural before
    Sinai) unique (checked) — its two Scripture-twins in
    Ezekiel's Temple. THE HEAVY GUARD-STROKE [EX18-09, MS
    on 18:18]: the kaf of כי under the guard-stroke
    (checked in-token); עשהו ("do it") LEAN — the printed
    Masorah's "none like it and full" ruled AN ERROR (the
    Ramah: lean); the heavy-root's third station
    (asserted). THE TEN-UTTERANCE WARNING [EX18-10, MS +
    KB + Lekach Tov on 18:20]: והזהרתה ("and you shall
    warn") full with final He — "NONE LIKE IT in the
    reading" (census checked); the two surplus He's (5+5) =
    the TEN utterances; החקים dageshed (asserted);
    printed-authority: the intruding relative-word struck.
    THE TWO COUNSELORS [EX18-11, KB on 18:19/23]: איעצך
    ("I will counsel you") exactly twice in the Torah
    (census checked): JETHRO and BALAAM (Num 24:14) — the
    courts' builder and the snare's architect; heeded
    counsel keeps a man his place (Moses vs Zedekiah);
    וצוך ("and God command you") unique (checked at the
    build) — the counsel self-gated; על מקומו — the
    Job-twin: judge below or be judged above. THE ROSTER'S
    LETTERS [EX18-12, MS on 18:21-25]: לקול ("the voice")
    FULL (the Ramah: every Torah voice-form full but five —
    the heeded voice whole; checked in-verse); עשרת
    ("tens") lean both times; הגדל lean; מאות full;
    the one-codex stroke on haters-of-gain (named). THE
    GROWN VAV [EX18-13, MS + KB on 18:26]: ישפוטו ("they
    shall judge") long-spelled, Torah-unique (checked)
    against 18:22's lean ישפטו in the same clause
    (asserted) — the verb gains its vav where judging
    turns from plan to practice; the long stress (the
    Mikhlol); the HARD matter beside the STIFF neck
    (Deut 31:27) — "Moses judged the stiff-necked."
  owner_language_note: >
    English for reading only. Hebrew is the derivation source.
  oral_policy_note_en: >
    Written trees first. Dual-track Oral only when named; never
    silent-merge.
  tree_derive_version: logic_derived_v1
  tree_derive_phase: "FWD-32"
  confidence_overall: "structure tested; oral layer verified 13/13"
  genre: "counsel_and_courts_fsm"
  build_track: exodus_stack
  depends_on: exo_17_massah_and_amalek
  depends_note_en: >
    Depends for PATTERN only (18:1 hears 17's war; the kaved-root
    passes from the hands to the caseload; the mount of God
    reprises 3:1 ahead of 19's arrival). Standalone machine.
    Exod 1-18 continuous, 94 frozen units.
''' % (ttl_he, ttl_tr)

DLOG = '''derivation_log:
  - step: A
    name_en: "Block choice"
    comment: >
      FORWARD ERA run 8, block 2 (owner: "lets do 5 more blocks").
      Canon continuation: Exod 18:1-27 — Jethro, whole chapter.
    confidence: established
  - step: B
    name_en: "Span + source + conventions"
    comment: >
      SNAPSHOT prestage: 27 verses, all with etnachta. Volitive
      census: ONE real push (18:19 the counsel — advisory class,
      gated at 18:23); 18:20-22's instructions fold into the
      counsel-card as its content; the greeting, the meal, the
      court-day are narration.
    confidence: established
  - step: C
    name_en: "Machine structure"
    comment: >
      1D/1R/1E — the hearing-chapter: the advisory card (18:19)
      pops at 18:24 on the chapter's own opening verb (heard/
      heard) with the unqualified compliance-formula. The
      convert's offering-event (18:12). The know-ledger's first
      voluntary foreign deposit (18:11). REGISTRY 0 — Eliezer
      arrives report-class (name learned here first, no
      naming-verb; entity file at run-end). Asserted machine
      evidence: the Torah's two not-goods (Eden/Jethro — both
      aloneness); the kaved arc completed by ve-haqel; the lean
      rescue trio; the seek-pair with Rebekah; the vav grown
      between 18:22 and 18:26; the dropped articles; 616.
    confidence: tested
  - step: D
    name_en: "Oral scan (in-pipeline)"
    comment: >
      Local mirror only (zero fetches): Minchat Shai on Exod 18
      (18 notes) + Kitzur Baal HaTurim on Exod 18 (18 notes).
      Manifest 13 rows: 13 VERIFIED / 0 FAILED / 0 UNCHECKABLE,
      first run. The did-God pair; the three lean rescues; the
      camping angel; the on-account pair (printed Masorah
      convicted); the unique joy + the sevirin; the pointed
      blessing; the creation-letters; the seek-file; the heavy
      guard-stroke; the ten-utterance warning; the two
      counselors; the roster's letters; the grown vav.
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
      not silent edits. Exod 1-18 continuous.
    confidence: established
'''

unitgen.emit_unit(META, DLOG, steps, scenarios, "logic/units/exo_18_jethro_and_the_judges.yaml")
print("wrote logic/units/exo_18_jethro_and_the_judges.yaml —", len(steps), "steps,", len(scenarios), "scenarios")
