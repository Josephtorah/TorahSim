#!/usr/bin/env python3
"""Author exo_15_the_song_and_marah (Exod 15:1-27) — forward-era unit #29 (run FWD-6 block 5).
Run from repo root. REDO after the 2026-08-09 crash: the verified manifest
(13/13) is the block's whole inheritance; this script rebuilds the unit."""
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
assert (hp(15, 1, 0), hp(15, 1, 1)) == ("אז", "ישיר")            # then sang
assert [hp(15, 1, i) for i in range(13, 20)] == \
       [hp(15, 21, i) for i in range(5, 12)]                      # the refrain verbatim (7 tokens)
assert hp(15, 21, 3) == "שירו"                                    # the imperative
assert (hp(15, 23, 12), hp(15, 23, 13), hp(15, 23, 14)) == ("קרא", "שמה", "מרה")  # the naming
assert census("וילנו") == [("Exod", 15, 24), ("Num", 14, 2), ("Num", 17, 6)]      # the murmur-form's three
assert (hp(7, 21, 7), hp(7, 21, 9)) == ("יכלו", "לשתות")          # Egypt could not drink (full)
assert (hp(15, 23, 3), hp(15, 23, 4)) == ("יכלו", "לשתת")         # Israel could not drink (lean)
assert hp(15, 15, 0) == "אז"                                      # the second then
assert hp(15, 12, 2) == "תבלעמו"                                  # the earth swallowed
assert any(r[0].replace("/", "") == "ויבלע" for r in db.execute(
    "SELECT w.he_plain FROM words w JOIN verses v ON w.verse_id=v.id "
    "WHERE v.book='Exod' AND v.chapter=7 AND v.verse=12"))         # the staff swallowed (7:12)
assert (hp(15, 25, 11), hp(15, 25, 16), hp(15, 27, 10)) == ("שם", "ושם", "שם")   # the there-triple
assert hp(15, 25, 9) == "וימתקו"                                  # the waters sweetened
assert hp(15, 26, 26) == "רפאך"                                   # your Healer
assert (hp(15, 27, 3), hp(15, 27, 4), hp(15, 27, 7)) == ("שתים", "עשרה", "ושבעים")  # 12 + 70

P = "PRECONDITION_STATE"
D = "DECLARE"
R = "RESULT"
E = "EVENT"
N = "NAME"

def v(op, en, left, right, comment, ops):
    return dict(op=op, en=en, left_en=left, right_en=right, comment=comment, operators=ops)

def p(expr, span, prose):
    return dict(op=P, expr_en=expr, he_span=span, prose=prose)

V = {}
V[1] = v("THEN_SANG_MOSES", "Then sang Moses and the sons of Israel this song to the LORD, and they spoke, saying: I will sing to the LORD, for He is highly exalted; the horse and its rider He has thrown into the sea.",
  "then sang Moses and the sons of Israel this song to the LORD, and they spoke, saying", "I will sing to the LORD, for He is highly exalted: the horse and its rider He has thrown into the sea",
  "The Song event; the refrain minted.",
  [dict(op=E, expr_en="shirat_ha_yam(e1); Agent(e1, moshe); Theme(e1, bene-yisrael)", he_span=(0,10),
    prose="THE SONG [EX15-03 CROWN]. AZ YASHIR moshe u-vene yisrael — 'THEN SANG Moses and the sons of Israel': THE EVENT — the corpus's first song, and the then-sang frame stands exactly TWICE in the Torah (VERIFIED): the Sea here and THE WELL (Num 21:17 — where Moses' name is withheld, the Kitzur: 'he too sang — but it does not name him, FOR HE WAS STRUCK THROUGH WATER': the water-singer barred by water, Num 20 armed); the yod of yashir counted as TEN SONGS (the Sea, the Well, the witness-song, Joshua, Deborah, Hannah, David, Solomon, Hezekiah, and THE SONG TO COME — the chain's canon of history, the last unsung); and the Kitzur's redeemed grudge: 'with the word I COMPLAINED — u-ME-AZ bati el-paro (5:23: SINCE THEN it has gone worse) — with that word I WILL BEGIN THE PRAISE' (asserted: exo_05's bitterest adverb returned as the Song's first word); yashir bound by maqqef (MS, EX15-13); the machine stamps the singing and notes the tense the readings live on: the future-form sang in the past, named-only."),
   p("HOLDS(ki_gao_gaa_sus_ve_rokhvo, t0)", (11,19),
    "THE REFRAIN. ashira la-YHWH ki GAO GAA — 'I will sing to the LORD, for He is HIGHLY EXALTED' (the cohortative: the Song opens on a first-person vow); the doubled exaltation-verb SOFT then HARD (EX15-01: both checked — the Masorah's twin-pairs file); sus ve-rokhvo rama va-yam — 'the horse and its rider He has THROWN into the sea': the refrain-line minted whole — SEVEN tokens that will return VERBATIM in Miriam's mouth (asserted at the build: 15:1 and 15:21 token-identical): the machine arms the antiphon.")])
V[2] = v("MY_STRENGTH_AND_SONG", "My strength and song is the LORD, and He has become my salvation; this is my God, and I will glorify Him — my father's God, and I will exalt Him.",
  "my strength and song is the LORD, and He has become my salvation", "this is my God, and I will glorify Him; my father's God, and I will exalt Him",
  "The salvation receipted; the vow-pair.",
  [p("HOLDS(uzi_ve_zimrat_yah, t0)", (0,5),
    "THE STRENGTH [EX15-12; EX15-13]. UZI ve-zimrat YAH — 'my STRENGTH and song is the LORD': the strength-word Torah-unique (VERIFIED) — the Kitzur's three named (the Hallel's and Isaiah's wells-of-salvation twin) with the sweet-floor: 'SWEET water flowed from the sea-bed and they DREW IT IN JOY'; and the word's own grammar carries a loss (MS, EX15-13): the ayin in QAMATZ-CHATUF 'because of the zayin's dagesh, WHICH MARKS THE DROPPED ROOT-LETTER' — the strength-word spelled minus a letter of its own root (15:13's nehalta ve-ozkha the same rule, bet raphe; va-aromemenhu's first mem on sheva alone); va-yehi-LI li-YSHUA — 'He has become MY SALVATION': 14:13's stand-and-see oracle receipted in the first person (the yeshua armed at the panic, delivered at 14:30, SUNG at 15:2 — the machine closes the salvation-arc in the singer's own mouth); and the readings' counter named-only: my-strength against the prince of Egypt the Kitzur named at the drawing-near (14:10's arm paid)."),
   p("HOLDS(ze_eli_ve_anvehu, t0)", (6,11),
    "THE VOW-PAIR. ZE eli ve-ANVEHU — 'THIS is my God, and I will GLORIFY Him' (the pointing-word: the readings on the finger at the sea — the maidservant seeing what prophets sought — named-only); elohe AVI va-aromemenhu — 'my FATHER'S God, and I will EXALT Him': the machine files the Song's self-volitives (anvehu, aromemenhu — cohortative vows of praise, not demands on any agent: the quoted-mood class) and the two-generation credential: the God claimed by sight and by inheritance in one breath (3:6's fathers-formula sung).")])
V[3] = v("A_MAN_OF_WAR", "The LORD is a man of war; the LORD is His name.",
  "the LORD is a man of war", "the LORD is His name",
  "The doctrine sung.",
  [p("HOLDS(YHWH_ish_milchama, t0)", (0,4),
    "THE WAR-MAN. YHWH ISH MILCHAMA — 'the LORD is a MAN OF WAR': 14:14's doctrine ('the LORD will FIGHT for you') and 14:25's enemy-confession ('the LORD FIGHTS for them') resolved into a title — the machine notes the fight-verb's arc: promised to the trembling, confessed by the drowning, sung by the saved; YHWH SHEMO — 'the LORD is His NAME': the Name held level with the war-title (the readings: He fights with the Name of mercy — a man of war whose name stays the merciful Name; named-only): the Song's shortest theology.")])
V[4] = v("CAST_INTO_THE_SEA", "Pharaoh's chariots and his host He has cast into the sea; and the choice of his officers are sunk in the Reed Sea.",
  "Pharaoh's chariots and his host He has cast into the sea", "and the choice of his officers are sunk in the Reed Sea",
  "The choice-men; the sea given teeth.",
  [p("HOLDS(u_mivchar_shalishav_tubu, t0)", (5,9),
    "THE CASTING [EX15-12 CROWN]. markevot paro ve-chelo YARA va-yam — 'Pharaoh's chariots and his host He CAST into the sea' (the chariot-word's idol-file named: Josiah burning the SUN-CHARIOTS, 2 Kgs 23:11 — 'Pharaoh's host had their idols PAINTED ON THEIR GARMENTS'; Shebna's glory-chariots beside it); U-MIVCHAR shalishav — 'and THE CHOICE of his officers': the choice-word Torah-UNIQUE here (VERIFIED), its Masorah-twin 'the choice of his young men went down to SLAUGHTER' — the Kitzur: 'after they drowned, they went down to be BUTCHERED on the rocks of the sea' (the sea given teeth — 14:27's shaking read to its end); TUBU ve-yam-SUF — 'SUNK in the REED SEA': the sea named by name inside the Song (10:19's first naming, 13:18's road, 15:4's grave — the machine files the Reed Sea's three offices in the corpus so far).")])
V[5] = v("THE_DEEPS_COVER_THEM", "The deeps cover them — they went down into the depths like a stone.",
  "the deeps cover them", "they went down into the depths like a stone",
  "The once-vocalization; the first stone.",
  [p("HOLDS(tehomot_yekhasyumu, t0)", (0,1),
    "THE COVER'S CODA [EX15-08 CROWN]. tehomot YEKHASYUMU — 'the deeps COVER THEM': the cover-word Torah-UNIQUE (VERIFIED) in a ONCE-IN-SCRIPTURE vocalization — MS quoting Rashi: 'there is NOTHING LIKE IT in Scripture in its pointing' (the machine notes the coda: the cover-verb chain that closed at 14:28 — frog, locust, sea — is re-sung in a form the language uses exactly once: the final cover wears a pointing with no twin); BI-MTZOLOT — 'in the DEPTHS' on its ruled skeleton (checked unique; the Hilleli's and Yerushalmi's variants dual-tracked, the Masorah and the Ramah with the stream) — the Kitzur's three depths: 'they were IN DARKNESS in the depths, as it is written: the cloud and the darkness' (14:20's severed night wired into the Song); yardu... KEMO AVEN — 'like a STONE': the Song's stone-file opens (armed to 15:16's stone-still peoples).")])
V[6] = v("YOUR_RIGHT_HAND_DOUBLED", "Your right hand, O LORD, majestic in power — Your right hand, O LORD, shatters the enemy.",
  "Your right hand, O LORD, majestic in power", "Your right hand, O LORD, shatters the enemy",
  "The anaphora; the power-pair.",
  [p("HOLDS(yeminkha_YHWH_nedari_va_koach, t0)", (0,3),
    "THE RIGHT HAND [EX15-12]. YEMINKHA YHWH... YEMINKHA YHWH — the Song's first anaphora: the right hand named twice in one verse (the readings: when Israel does His will, the left too becomes right — named-only); nedari BA-KOACH — 'majestic IN POWER': the power-word an all-Torah pair (VERIFIED at the build): the arm that saved here — and Moses' intercession at the calf ('whom You brought out of Egypt WITH GREAT POWER,' 32:11): the machine arms the wire — the Song's word for the saving arm will be the plea's word when the saved sin (the Kitzur's Scripture-fellows named: the herald's lifted voice, the last redemption likened to the first); tiratz OYEV — 'SHATTERS the enemy': the enemy-word singular (15:9's speaker pre-named).")])
V[7] = v("LIKE_STUBBLE", "And in the greatness of Your exaltation You overthrow those who rise against You; You send forth Your burning — it consumes them like stubble.",
  "and in the greatness of Your exaltation You overthrow those who rise against You", "You send forth Your burning; it consumes them like stubble",
  "The five sendings.",
  [p("HOLDS(teshalach_charonkha, t0)", (4,7),
    "THE SENDING [EX15-10 CROWN]. TESHALACH charonkha yokhlemo ka-QASH — 'You SEND FORTH Your burning — it consumes them like STUBBLE': the send-forth form's Torah-census exactly FIVE (VERIFIED): the AKEDA'S stayed hand (Gen 22:12), Moses' deflection (4:13), the burning here, the show-me plea (33:12), and THE MOTHER-BIRD (Deut 22:7) — and the Kitzur's grand reading rides the last: 'He SENT THE FATHERS from before His face and they died in the wilderness, and TOOK THE CHILDREN and brought them into the Land — and even so they have a share in the world to come: You send forth Your breath, they are created' (the five-station career from the withheld knife to the released bird); QAMEKHA — 'Your RISERS' Torah-unique (VERIFIED at the build), its Psalm-twin: 'the DIN of Your risers ascends continually — therefore You BREAK Your risers'; u-ve-rov GEONKHA — 'in the greatness of Your EXALTATION' full-vav (MS, EX15-13: the old tikkun's lean variant named, the Ramah ruling full): the wrath-verse filed with its census exact.")])
V[8] = v("THE_WIND_OF_YOUR_NOSTRILS", "And by the wind of Your nostrils the waters were heaped up — the streams stood like a mound; the deeps congealed in the heart of the sea.",
  "and by the wind of Your nostrils the waters were heaped up; the streams stood like a mound", "the deeps congealed in the heart of the sea",
  "The nostril-pair; the two hearts of the sea.",
  [p("HOLDS(u_ve_ruach_apekha_neermu_mayim, t0)", (0,7),
    "THE BLAST [EX15-09 CROWN]. u-ve-RUACH APEKHA neermu mayim — 'by the WIND OF YOUR NOSTRILS the waters were heaped': the nostrils-word stands exactly TWICE in the Torah (VERIFIED) — and MS marks the pair himself: 'see what I noted at Genesis on BY THE SWEAT OF YOUR FACE — its fellow' (Gen 3:19): Adam's sweat and the Name's blast, the curse of labor and the weapon of rescue on one rare noun (both full-yod, the Masorah's two; NEERMU likewise full-yod with MS's own maqqef-preference confessed: 'in some books bound — and it is CORRECT IN MY EYES'); the Kitzur's four winds ('with the wind of His lips He slays; with the wind of His mouth He made all their host — with wind He burns, with wind He creates'); the machine notes the re-description: 14:21's STRONG EAST WIND — the meteorology of the narrative — is sung as the breath of His anger: the instrument-clause of the split promoted to anatomy; nitzvu khemo NED nozlim — 'the streams STOOD like a MOUND' (the mound-word: Jordan's heap named, outside the Torah, named-only); qafu tehomot BE-LEV YAM — 'the deeps CONGEALED in the HEART of the sea': the heart-of-the-sea phrase Torah-unique in the Song (VERIFIED at the build) — the Kitzur's two hearts: 'Israel walked a PAVED ROAD like a ship's wake; Egypt tossed like the drunkard LYING in the heart of the sea.'")])
V[9] = v("THE_ENEMY_SAID", "The enemy said: I will pursue, I will overtake, I will divide spoil; my desire shall be filled of them — I will draw my sword, my hand shall dispossess them.",
  "the enemy said: I will pursue, I will overtake, I will divide spoil", "my desire shall be filled of them; I will draw my sword, my hand shall dispossess them",
  "The dead vows quoted.",
  [p("HOLDS(amar_oyev_erdof_asig, t0)", (0,5),
    "THE QUOTED DEAD. AMAR OYEV — 'the ENEMY SAID': the Song hands the drowned their own microphone — ERDOF ASIG ACHALEQ shalal — 'I will PURSUE, I will OVERTAKE, I will DIVIDE spoil': five first-person vows in a row WITHOUT A SINGLE VAV (the corpus's densest volitive cluster, unconjoined — the panting rhythm the trope preserves); timlaemo NAFSHI... ariq CHARBI torishemo YADI — my desire, my sword, MY HAND (the possessives stacked — the readings: the hand that boasted against the great hand of 14:31, named-only): the machine files the class — QUOTED-MOOD, agent dead: these volitives push nothing (the sea already refused them at 14:27-28); the Song quotes the plan pluperfectly, between the blast that heaped the water (15:8) and the blast that sank it (15:10): the boast is the filling of the sandwich its two winds close.")])
V[10] = v("SANK_LIKE_LEAD", "You blew with Your wind — the sea covered them; they sank like lead in the mighty waters.",
  "You blew with Your wind; the sea covered them", "they sank like lead in the mighty waters",
  "The lead-word's three; the full lead.",
  [p("HOLDS(tzalalu_ka_oferet, t0)", (4,7),
    "THE SINKING [EX15-13]. nashafta ve-ruchakha — 'You BLEW with Your wind' (one breath answers five vows — the machine prices the exchange: 15:9's whole arsenal against one exhalation); TZALALU ka-OFERET — 'they SANK like LEAD': the sink-word Torah-unique (VERIFIED at the build) — the Kitzur's three: the lead that SANK, the lips that QUIVERED at the sound, the gates of Jerusalem that DARKENED ('sounds and sword' — one skeleton for sinking, quivering, and dusk); ka-oferet FULL-vav (asserted in-verse: 'in all precise copies FULL — and ONE lean: the spoils'-fire lead of Num 31:22, checked: the Song's lead full, the furnace's lean'); the lamed on sheva alone (MS); be-mayim ADIRIM — 'in the MIGHTY waters': the mighty-word held for 15:11's mighty ones (the machine notes the hinge: the waters called mighty in the verse before might itself is asked who owns it).")])
V[11] = v("WHO_IS_LIKE_YOU", "Who is like You among the mighty, O LORD? Who is like You, majestic in holiness — feared in praises, doing wonder?",
  "who is like You among the mighty, O LORD? who is like You, majestic in holiness", "feared in praises, doing wonder",
  "The guard-dageshim; the two lean like-You's.",
  [p("HOLDS(mi_khamokha_ba_elim, t0)", (0,7),
    "THE INCOMPARABLE [EX15-01 + EX15-02 CROWNS — THE MARQUEE]. mi KHAMOKHA ba-elim YHWH mi KAMOKHA nedar ba-qodesh — 'WHO IS LIKE YOU among the mighty... WHO IS LIKE YOU, majestic in holiness': the Song's GUARD-DAGESHIM — the first like-You SOFT and the second HARD (both VERIFIED in-stream; the dagesh-after-open-vowel guard-list of Daniel 5) — and the tradition names the reason: 'SO AS NOT TO STAMMER MICAH BESIDE THE NAME' (the soft kaf would slur toward the idol-name — the idol the chain marched through the sea at 14:22/29 is barred from the Song by ONE DOT); Lekach Tov's other face: 'at first they praised with a WEAK LIP, at the end from the walls of their hearts WITH A FULL MOUTH'; and the Ramah's census EXACT (VERIFIED): every like-You in the Torah is written full-vav without the final he EXCEPT TWO — lean-vav WITH the he — 'AND BOTH ARE IN ONE VERSE': this one; BA-ELIM lean-of-lean (VERIFIED Torah-unique) read aloud by the rabbis: 'who is like You AMONG THE MUTE' (the God who keeps silence while His house burns — the tradition's darkest praise folded into the Song's brightest line; 14:14's be-silent doctrine given its terrible depth), with Isaiah's inflamed oak-idols as the Masorah's full twin (the Kitzur: shade without fruit against 'His shade is lovely and His fruit sweet'); the bet of ba-elim DAGESHED with NO PASEQ before it, 'AGAINST THE PRINTER'S EMENDATION' (MS, EX15-13 — the press corrected a tenth time: printed-authority file); the guard-class runs the Song (EX15-01): gaalta's gimel HARD ('were it soft it would sound DEFILED — and one would blaspheme,' the Rokeach), ka-aven's kaf HARD ('lest it say A STONE would silence You'), gao/gaa soft-then-hard: a liturgy whose consonants harden exactly where praise could slip into idol, defilement, or silence."),
   p("HOLDS(nora_tehilot_ose_fele, t0)", (8,11),
    "THE WONDER-CLAUSE. NORA tehilot — 'FEARED in praises' (the readings: praise that knows its limit — the silence-praise of the mute-reading one clause back, named-only); nedar's alef on sheva alone (MS, EX15-13); OSE FELE — 'doing WONDER': the wonder-word singular (the machine notes the count's restraint: one wonder-word for the whole sea — the Song's arithmetic opposite to 15:9's five boasts).")])
V[12] = v("THE_EARTH_SWALLOWED", "You stretched out Your right hand — the earth swallowed them.",
  "You stretched out Your right hand", "the earth swallowed them",
  "The swallow-ledger; the pivot.",
  [p("HOLDS(tivlaemo_aretz, t0)", (0,3),
    "THE SWALLOW. natita YEMINKHA — 'You stretched out Your RIGHT HAND' (the stretch-verb of 14:16/21/26-27 sung to the hand that owned it at 15:6); TIVLAEMO ARETZ — 'the EARTH SWALLOWED THEM': the swallow-verb's return (asserted at the build: 7:12's staff that SWALLOWED the staffs — the corpus's swallow-ledger: the wonder that opened the duel closes the burial; the readings: the sea cast them to the land's mouth, burial as the drowned army's one kindness — named-only; the earth's next great swallow armed: Num 16:32's mouth of the ground): the machine marks the PIVOT — four words with no etnachta, the Song's shortest verse, and on its far side the theme turns from drowning to shepherding (15:1-12 the enemy, 15:13-18 the people).")])
V[13] = v("YOU_GUIDED_IN_KINDNESS", "You guided in Your kindness the people You redeemed; You led them in Your strength to Your holy habitation.",
  "You guided in Your kindness the people You redeemed", "You led them in Your strength to Your holy habitation",
  "The shepherd-cloud; the people-this.",
  [p("HOLDS(am_zu_gaalta, t0)", (0,4),
    "THE SHEPHERD [EX15-04 CROWN]. NACHITA ve-chasdkha — 'You GUIDED in Your kindness': the guided-word Torah-unique (VERIFIED), its Psalm-twin 'You guided Your people LIKE THE FLOCK' — the Kitzur's shepherd-cloud: 'as the shepherd paces each sheep by its stride, the cloud led each by his walking — the great by his greatness, the small by his smallness — and shaded them at noon' (13:21's pillar given a shepherd's gait — the tenderest logistics in the chain); am-ZU gaalta — 'the people THIS-ONE You redeemed': the people-this frame stands exactly TWICE in the Torah, BOTH IN THIS SONG (VERIFIED: the redeemed here, the acquired at 15:16), the Masorah's third outside: 'the people I FORMED for Myself' (Isa 43:21) — the Kitzur: 'when You acquired them in redeeming them, it is AS IF YOU FORMED THEM THEN A NEW CREATURE' (redemption as second creation — the Song's own theology in three verbs: redeemed, acquired, formed); the gimel of gaalta HARD (EX15-01's guard-list: the blasphemy barred); nehalta ve-OZKHA — 'You LED them in Your strength' (bet raphe, the qamatz-chatuf rule again, MS): el-NEVE qodshekha — 'to Your holy HABITATION': the homing-word (the machine opens the Song's destination-arc: habitation 15:13, mountain and sanctuary 15:17, reign 15:18).")])
V[14] = v("THE_PEOPLES_HEARD", "The peoples heard — they tremble; pang seized the dwellers of Philistia.",
  "the peoples have heard — they tremble", "pang has seized the dwellers of Philistia",
  "The panic-quartet opens.",
  [p("HOLDS(shamu_amim_yirgazun, t0)", (0,2),
    "THE HEARING. SHAMU amim YIRGAZUN — 'the peoples HEARD — they TREMBLE' (the archaic long-form: the trembling lengthened by its final nun — the Song's register); chil ACHAZ yoshve PELASHET — 'pang SEIZED the dwellers of PHILISTIA' (the seize-word's Masorah-pair named-only: Adonijah gripping the altar-horns — 'trembling seized him till he gripped the horns'; and the other tongue's not-grasped); the machine opens the PANIC-QUARTET (Philistia, Edom, Moab, Canaan — 15:14-16) and files its genre: the Song's only FORECAST section — sung terror running ahead of the marchers (Rahab's confession named, outside the Torah: 'we HEARD... and hearts MELTED' — the receipt the quartet arms).")])
V[15] = v("THE_CHIEFS_DISMAYED", "Then were the chiefs of Edom dismayed; the rams of Moab — trembling seizes them; all the dwellers of Canaan are melted away.",
  "then were the chiefs of Edom dismayed; the rams of Moab — trembling seizes them", "all the dwellers of Canaan are melted away",
  "The second then; the melt-verb.",
  [p("HOLDS(namogu_kol_yoshve_khenaan, t0)", (8,11),
    "THE QUARTET'S BODY. AZ nivhalu ALUFE edom — 'THEN were the CHIEFS of Edom dismayed': the then-word's second station in the chapter (asserted: 15:1's then of song, 15:15's then of dread — one adverb for the singing and the shuddering); the chief-word is Esau's own registry-title (Gen 36's roll of chiefs — the machine notes the corpus-echo: the family that kept its chiefs on parchment now keeps them trembling); ELE moav — 'the RAMS of Moab' (the flock-nobility, the readings named-only); yochazemo RAAD — trembling seizes them (the -mo suffix again: the Song's archaic object-endings clustering); NAMOGU kol yoshve KHENAAN — 'all the dwellers of Canaan are MELTED': the melt-verb (its great receipt named, outside the Torah: Jericho's 'the dwellers are melted' in Rahab's mouth and at the crossing) — the machine holds the quartet OPEN toward Joshua: sung geography the conquest will walk.")])
V[16] = v("STILL_AS_A_STONE", "Terror and dread fall upon them; by the greatness of Your arm they are still as a stone — till Your people cross over, O LORD, till the people You acquired cross over.",
  "terror and dread fall upon them; by the greatness of Your arm they are still as a stone", "till Your people cross over, O LORD, till this people You acquired cross over",
  "The stone-still; the double crossing.",
  [p("HOLDS(ad_yaavor_am_zu_qanita, t0)", (8,16),
    "THE CROSSING-CLAUSE [EX15-04; EX15-01]. tipol alehem EMATA va-fachad — 'TERROR and dread fall upon them' (the terror-word wearing the archaic he-ending; alehem with NO paseq, MS, EX15-13); bi-gedol ZEROAKHA — 'by the greatness of Your ARM' — the arm-word FULL against the Yerushalmi's lean (VERIFIED: the Hilleli WITH the stream — dual-tracked per the divergence law); yidmu KA-AVEN — 'STILL AS A STONE': the kaf HARD (EX15-01's guard-list: 'lest it seem to say A STONE would silence You' — the same dot-law that barred the idol at 15:11 bars the stone from silencing praise), and the stone-file closes its frame (15:5's enemy sank like a stone; 15:16's peoples stand like one — what the sea did to Egypt in water, the report does to Canaan on land); AD-YAAVOR amkha YHWH ad-yaavor AM-ZU QANITA — 'TILL Your people CROSS OVER... till the people You ACQUIRED cross over': the crossing-verb doubled (the readings: two crossings — the sea behind, the Jordan ahead — named-only) and the people-this frame's second Song-station (VERIFIED, EX15-04): the acquired-word joins the redeemed-word of 15:13 — the machine arms the far bank the quartet already fears.")])
V[17] = v("PLANT_THEM_ON_YOUR_MOUNTAIN", "You will bring them in and plant them on the mountain of Your inheritance — the place for Your dwelling which You made, O LORD; the sanctuary, O Lord, which Your hands established.",
  "You will bring them in and plant them on the mountain of Your inheritance — the place for Your dwelling which You made, O LORD", "the sanctuary, O Lord, which Your hands established",
  "The sanctuary-forecast.",
  [p("HOLDS(makhon_le_shivtekha_paalta, t0)", (4,7),
    "THE HOUSE BEFORE THE TENT [EX15-05 CROWN]. TEVIEMO ve-titaemo be-HAR nachalatkha — 'You will BRING them and PLANT them on the MOUNTAIN of Your inheritance' (the planting-verb for a people — the readings' vineyard named-only): the Song's terminal FORECAST; makhon LE-SHIVTEKHA paalta YHWH — 'the place FOR YOUR DWELLING which You made': the dwelling-word Torah-UNIQUE (VERIFIED), its Masorah-twins SOLOMON'S DEDICATION ('I have surely built You a house of habitation, a place for Your dwelling forever,' 1 Kgs 8:13, with the Chronicles repeat) — the Kitzur: 'THE TEMPLE BELOW IS ALIGNED OPPOSITE THE TEMPLE ABOVE' (the placed-word read as aimed-word); and the cipher lands EXACT (asserted at the build): the dwelling-word's letters count JERUSALEM plus ZION (752 = 752 — one word carrying both its addresses); MIQDASH adonai konnu YADEKHA — 'the SANCTUARY... Your HANDS established': the qof dageshed LE-TIFERET ('for splendor' — the ornamental dagesh named as such, MS, EX15-13), the extra yod of the hands-word counted ('for the TEN miracles in the Temple and the TEN sanctities of the Land'): the machine files the forecast OPEN — the Song names the house sixty-five chapters before the book builds a tent (25:8's build-Me armed).")])
V[18] = v("THE_REIGN_FOREVER", "The LORD shall reign forever and ever.",
  "the LORD shall reign", "forever and ever",
  "The reign-line; the cutoff dispute.",
  [p("HOLDS(YHWH_yimlokh_le_olam_va_ed, t0)", (0,3),
    "THE REIGN [EX15-07 CROWN]. YHWH YIMLOKH le-olam va-ed — 'the LORD shall REIGN forever and ever': the Song's four-word seal (the reign-verb once in the verse, VERIFIED) — and the line carries a CHAIN-VS-STREAM DIVERGENCE, dual-tracked per the law: the Kitzur rules a PASEQ after the reigning ('when the time comes that they say THE-LORD-REIGNED, THE-LORD-REIGNS, THE-LORD-SHALL-REIGN — then the kingdom of the nations SHALL BE CUT OFF': the divider-stroke as the empires' terminus) — and THE STREAM WRITES NO PASEQ (VERIFIED: the four words run unbroken — the Kitzur's cutoff named, the stream's unbroken reign standing); the frame's grammar-note carried: 'MOSES put the Name BEFORE the kingship; DAVID put the kingship before the Name (Ps 146:10) — for David's line had just said the way of the wicked He makes crooked, and he would not set the Name beside the evil'; the forever-word LEAN with MS's vowel-note on the vav (per Rashi and Ibn Ezra, as in an old print): the machine closes the Song's poetry on the corpus's first kingship-line for the Name — sung, not yet legislated.")])
V[19] = v("THE_PROSE_SEAL", "For the horse of Pharaoh came, with his chariots and with his horsemen, into the sea, and the LORD returned upon them the waters of the sea; and the sons of Israel walked on the dry ground in the midst of the sea.",
  "for the horse of Pharaoh came, with his chariots and with his horsemen, into the sea, and the LORD returned upon them the waters of the sea", "and the sons of Israel walked on the dry ground in the midst of the sea",
  "The warrant-verse.",
  [p("HOLDS(ki_va_sus_paro_ba_yam, t0)", (0,6),
    "THE WARRANT. KI va SUS paro — 'FOR the horse of Pharaoh CAME': the Song's own citation apparatus — a prose verse inside the Song's scroll-block stating the evidence for the poetry (the horse came 14:23, the waters returned 14:28, Israel walked dry 14:29 — the machine reads 15:19 as the unit's for-clause: the claims of eighteen verses receipted against the narrative in one); sus singular again (the nation's mount one horse, as its man was one man at 14:25); u-vene yisrael halkhu VA-YABASHA be-tokh ha-yam — the dry-ground clause of 14:29 re-inscribed VERBATIM as testimony: the machine notes the Song's honesty-of-genre — where poetry ends, the record signs.")])
V[20] = v("MIRIAM_TAKES_THE_TIMBREL", "And Miriam the prophetess, the sister of Aaron, took the timbrel in her hand; and all the women went out after her, with timbrels and with dances.",
  "and Miriam the prophetess, the sister of Aaron, took the timbrel in her hand", "and all the women went out after her, with timbrels and with dances",
  "The sister signed; the layout-law sealed.",
  [p("HOLDS(va_tiqach_miryam_et_ha_tof, t0)", (0,7),
    "THE SISTER SIGNED [EX15-13]. va-tiqach MIRYAM ha-NEVIA achot AHARON — 'and MIRIAM THE PROPHETESS, the SISTER OF AARON, took the timbrel': the watching sister of 2:4 NAMED AT LAST — exo_02's withheld-name restraint pays its third installment (the parents signed at 6:20, the sister at 15:20), and she arrives already titled: THE PROPHETESS (the corpus's first woman so titled; the readings on the prophecy before Moses' birth, and on sister-of-AARON — the title from the days when she had one brother — named-only); et-HA-TOF — 'THE timbrel' (the article's readings: the instruments prepared in Egypt by the women who trusted the exodus enough to pack for singing — named-only); ve-tetzena KHOL ha-nashim — 'ALL the women went out' (the kaf SOFT, MS, EX15-13) be-tupim u-vi-MECHOLOT — with timbrels and DANCES; and HERE MS CLOSES THE SONG-LAYOUT LAW (EX15-13): 'THIS is the Song per the author's view — printed in two columns only for the page's narrowness; IN A TORAH SCROLL IT MUST BE ONE COLUMN, with FIVE LINES before it and FIVE after' (14:25's brick-grid arm executed and sealed): the machine files the registry-note for the fold (the entity-registry gains the sister) and the scroll its own architecture.")])
V[21] = v("SING_TO_THE_LORD", "And Miriam answered them: Sing to the LORD, for He is highly exalted; the horse and its rider He has thrown into the sea.",
  "and Miriam answered them", "sing to the LORD, for He is highly exalted: the horse and its rider He has thrown into the sea",
  "The antiphon; the imperative pushed.",
  [dict(op=D, expr_en="DECLARE(miryam, LET(shiru_la_YHWH))", he_span=(3,11),
    prose="THE ANTIPHON. va-TAAN lahem miryam — 'and Miriam ANSWERED THEM' (the answer-verb: the Song made responsive; la-HEM in the masculine — the readings on whom she answered, named-only; her gaa in the guard-list's dagesh-file too, MS); SHIRU la-YHWH — 'SING to the LORD': the Song's ONLY IMPERATIVE — the machine files the push (DECLARE: the command to sing) and the arc it closes: the Song opened on a first-person vow (ashira, 'I WILL SING'), it ends on a command (shiru, 'SING!') — praise scaled from volunteer to summons; and the refrain returns VERBATIM (asserted at the build: 15:21's seven closing tokens = 15:1's, letter for letter): the machine notes the card's state — the women's own singing beyond the refrain is UNNARRATED (the unnarrated-compliance class: the demand stands OPEN, the answered-verb the only receipt the text writes).")])
V[22] = v("THREE_DAYS_NO_WATER", "And Moses made Israel journey from the Reed Sea, and they went out to the wilderness of Shur; and they went three days in the wilderness, and found no water.",
  "and Moses made Israel journey from the Reed Sea, and they went out to the wilderness of Shur", "and they went three days in the wilderness, and found no water",
  "The forced march; the thirst opens.",
  [p("HOLDS(sheloshet_yamim_ve_lo_matzu_mayim, t0)", (10,16),
    "THE MARCH [EX15-11]. va-YASA moshe et-yisrael mi-yam-suf — 'and Moses MADE ISRAEL JOURNEY from the Reed Sea': the causative journey-verb — the Kitzur's jewel-derash named: 'he made them journey AGAINST THEIR WILL, for they were gathering the precious stones the sea-floor gave up' (the shepherd moving a flock from a rich pasture), with JOB the counselor's measure beside it ('my hope UPROOTED like a tree — for Job was in Pharaoh's counsel at the hard labor'); el-midbar-SHUR — toward the wilderness of SHUR (the corpus recalls the road: Hagar's well-road at Gen 16:7 — the desert that once opened a spring for a runaway now meets the redeemed); va-yelkhu SHELOSHET YAMIM ba-midbar VE-LO-MATZU MAYIM — 'THREE DAYS... and found NO WATER': the thirst-file OPENS (the wilderness-cycle's first shortage — the machine notes the ledger's turn: five verses after twelve verses of water as weapon and wall, the absence of water becomes the test).")])
V[23] = v("MARAH_NAMED", "And they came to Marah, and could not drink the waters of Marah, for they were bitter; therefore its name was called Marah.",
  "and they came to Marah, and could not drink the waters of Marah, for they were bitter", "therefore its name was called Marah",
  "The bitter station; the name written.",
  [dict(op=N, expr_en="name(maqom) := Mara", he_span=(10,14),
    prose="THE NAMING [EX15-11]. va-yavou MARATA — 'and they came TO MARAH': the to-Marah form Torah-unique (VERIFIED), its Masorah-twin Jeremiah's 'she has REBELLED against Me' — the Kitzur: 'as there they rebelled, so here' (the station's name and the station's sin one skeleton); ve-lo yakhlu LISHTOT mayim mi-mara ki MARIM hem — 'they COULD NOT DRINK the waters... for they were BITTER': the could-not-drink frame returns (asserted at the build: 7:21's Egypt that could not drink the blood-river, 15:23's Israel that cannot drink Marah — the first thirst after the sea quotes the first plague's clause, the drink-word full there and LEAN here: the lean-drink file re-lands); al-ken QARA SHEMA MARA — 'therefore its NAME was called MARAH': the naming-verb spent on a taste — the machine writes the register (the corpus's first station named for its complaint) and notes the mirror the readings press: the bitter waters, the bitter drinkers, one adjective, named-only.")])
V[24] = v("WHAT_SHALL_WE_DRINK", "And the people murmured against Moses, saying: What shall we drink?",
  "and the people murmured against Moses, saying", "what shall we drink?",
  "The murmur-verb's first station.",
  [dict(op=D, expr_en="DECLARE(ha_am, LET(ma_nishte))", he_span=(0,6),
    prose="THE MURMUR. va-YILONU ha-am al-moshe — 'and the people MURMURED against Moses': the murmuring-VERB arrives — and its exact form stands exactly THREE times in the Torah (asserted at the build): MARAH, the SPIES (Num 14:2), and the morrow of KORAH (Num 17:6) — water, land, and the dead: the wilderness-file's three great openings on one skeleton, the first here (14:11's complaint-class gains its signature verb; 16:2's murmur WITH AARON armed — here the target is Moses alone); MA-NISHTE — 'WHAT SHALL WE DRINK?': the machine pushes the demand (the plea's whole content two words — against 15:9's five-verb boast, the corpus's arithmetic of need vs. greed) and notes the timing the readings press: three days from the Song to the murmur, named-only.")])
V[25] = v("THE_TREE_AND_THE_STATUTE", "And he cried out to the LORD, and the LORD showed him a tree; and he cast it into the waters, and the waters were sweetened. There He set for him a statute and an ordinance, and there He tested him.",
  "and he cried out to the LORD, and the LORD showed him a tree; and he cast it into the waters, and the waters were sweetened", "there He set for him a statute and an ordinance, and there He tested him",
  "The repair-miracle; the first statute-station.",
  [dict(op=E, expr_en="hamtaqat_ha_mayim(e2); Agent(e2, moshe); Theme(e2, ha-mayim)", he_span=(0,9),
    prose="THE SWEETENING. va-YITZAQ el-YHWH — 'and he CRIED OUT to the LORD': the cry-ledger's third station (the people's at the sea 14:10, Moses' at Marah — and 14:15's why-cry-to-Me not contradicted: there the hour demanded motion, here there is no command in hand and the cry IS the liturgy; 17:4's next cry armed); va-YOREHU YHWH ETZ — 'and the LORD SHOWED him a TREE' (the show-verb from the teach-root — the readings hear the Torah-word inside it, named-only; the Kitzur's bitter tree at the manifest: 'as the bitter sweetens the bitter' — EX15-11's paradox-class); va-yashlekh el-ha-mayim — he CAST it in: THE EVENT — the corpus's first REPAIR-miracle: every wonder since 7:20 broke something whole (water to blood, light to dark, life to death); this one turns bad to good — the machine files the inversion of the first plague and lets the verse-pair speak (asserted at the build: the same could-not-drink clause at 7:21 and 15:23, one river ruined, one pool healed)."),
   dict(op=R, expr_en="RESULT: HOLDS(ma_nishte, t1)", he_span=(9,10),
    prose="THE ANSWER. va-YIMTEQU ha-mayim — 'and the waters were SWEETENED' (asserted): ma-nishte PAID in its own element — pushed at 15:24, popped at 15:25: the murmur-file's first entry closes in one verse (the machine notes the cycle-time: the corpus's fastest demand — and the pattern armed: the manna and the rock will run the same loop longer)."),
   p("HOLDS(sham_sam_lo_choq_u_mishpat, t0)", (11,15),
    "THE FIRST STATUTE-STATION [EX15-11 CROWN]. SHAM SAM lo CHOQ U-MISHPAT — 'THERE He SET for him a STATUTE AND AN ORDINANCE': the statute-and-ordinance adjacency Torah-UNIQUE at Marah (VERIFIED), the Masorah's fellows named: JOSHUA AT SHECHEM ('and he set for them a statute and an ordinance,' Josh 24:25) and EZRA ('to teach in Israel statute and ordinance') — the Kitzur: 'as at Marah, so at Shechem AS IF TORAH WERE GIVEN THAT DAY; and in Ezra the script was renewed' (THREE REFOUNDINGS on one phrase — law given at a spring, a stone, and a return); and the cipher asserted: SHAM counts PARA ADUMA with the inclusive one — 'as the bitter wood SWEETENS the bitter, the RED HEIFER purifies the defiled and defiles the pure' (the statute-class of paradox founded at the first statute-station); the machine files LAW BEFORE SINAI: the corpus's first named statute-giving since the Passover code (12:49's one-law), content unspecified in the written layer (the readings name Sabbath and honor and judgments — named-only, unclaimed)."),
   p("HOLDS(ve_sham_nisahu, t0)", (16,17),
    "THE TEST. ve-SHAM NISAHU — 'and THERE He TESTED him': the test-verb returns (Gen 22:1's word — the Akeda's verb aimed now at a nation; no verdict narrated: the machine files the VERDICT-LESS TEST as a standing fact, TESTS ledger untouched — 16:4's 'that I may TEST them' armed as the verb's next station); and the there-word TRIPLED (asserted at the build: THERE He set, THERE He tested, and THERE they camped at 15:27 — the itinerary teaching its grammar: every address in the wilderness is a syllabus).")])
V[26] = v("I_AM_YOUR_HEALER", "And He said: If you diligently listen to the voice of the LORD your God, and do what is right in His eyes, and give ear to His commandments, and keep all His statutes — all the disease which I set upon Egypt I will not set upon you; for I am the LORD your healer.",
  "and He said: if you diligently listen to the voice of the LORD your God, and do what is right in His eyes, and give ear to His commandments, and keep all His statutes", "all the disease which I set upon Egypt I will not set upon you, for I am the LORD your healer",
  "The listen-covenant; the healer's soft letter.",
  [dict(op=D, expr_en="DECLARE(YHWH, LET(im_shamoa_tishma))", he_span=(0,14),
    prose="THE LISTEN-COVENANT. im SHAMOA TISHMA le-qol YHWH elohekha — 'IF you DILIGENTLY LISTEN to the voice of the LORD your God': the corpus's first CONDITIONAL law to the nation — the if-word opens covenant-grammar (19:5's if-you-listen at Sinai armed: Marah drafts the form the mountain will scale), and the doubled hearing (the infinitive absolute before its verb — the listening listened, the corpus's emphatic pattern) heads a FOUR-RUNG LADDER: listen / do the right in His eyes / give ear to His commandments / keep ALL HIS STATUTES (chuqav — the statute-word of 15:25 already plural: one verse after the first statute-station, a statute-CODE is presupposed; the qof dageshed, MS, EX15-13): the machine pushes the card and files its class — PERPETUAL-CONDITIONAL, no pop possible in-span (the demand is a standing covenant: it joins the perpetual statutes in the open queue)."),
   p("HOLDS(ani_YHWH_rofekha, t0)", (15,26),
    "THE HEALER [EX15-06 CROWN]. kol-HA-MACHALA asher samti ve-mitzrayim lo-asim alekha — 'all the DISEASE which I set upon Egypt I will not set upon you': the plague-cycle re-classed in one word as DISEASE (the corpus's own retrospect: what Egypt received is what obedience is spared) — and the Kitzur's anagram-pharmacy asserted: the disease-word's letters are THE BREAD and THE SALT (letter for letter, finals normalized), its number its own etiology ('EIGHTY-THREE kinds of illness hang on the gall — and morning bread with salt and a jug of water ANNULS THEM ALL — therefore SPRINGS OF WATER are juxtaposed': 15:27 next verse — the remedy spelled inside the malady, the menu inside the diagnosis); kol-ha-machala's lengthener-and-binder ruled, the he WITHOUT a lengthener 'so for BEN ASHER' (the codex-master cited twice in one verse, MS, EX15-13); ki ANI YHWH ROFEKHA — 'for I AM THE LORD YOUR HEALER': the I-am-the-LORD formula (6:2's spine-word) gains its first TITLE — and the title's own letter rules the theology (VERIFIED): the pe of the healer SOFT ('healing by the hand of Heaven comes GENTLY'), while the human healers of Mishpatim (21:19) carry BOTH pes DAGESHED ('healing by man's hand comes HARD'): the soft Physician and the hard physicians, one letter's pressure apart — the machine closes the covenant-verse on the know-ledger's new inflection: the Name that Egypt learned by plague, Israel is to know by its absence.")])
V[27] = v("TWELVE_SPRINGS_SEVENTY_PALMS", "And they came to Elim, and there — twelve springs of water and seventy palm trees; and they camped there by the waters.",
  "and they came to Elim, and there — twelve springs of water and seventy palm trees", "and they camped there by the waters",
  "The counted oasis; the water-arc closes.",
  [p("HOLDS(shtem_esre_enot_ve_shivim_temarim, t0)", (2,8),
    "THE OASIS. va-yavou ELIMA — 'and they came to ELIM': the juxtaposition the tradition itself demanded (EX15-06: 'therefore SPRINGS OF WATER are juxtaposed' — the healer's verse answered by a watering-place in the very next breath); ve-sham SHTEM-ESRE enot mayim ve-SHIVIM temarim — 'TWELVE springs of water and SEVENTY palm trees' (asserted): the wilderness counted in the nation's own numbers (the readings: a spring for each tribe, a palm for each elder — named-only; the corpus's own registers: the twelve of the name-roll 1:1-4, the seventy of the descent 1:5/Gen 46:27 — the oasis shaped like the census); va-yachanu SHAM al-ha-mayim — 'and they camped THERE BY THE WATERS': the unit's last word is THE WATERS — the machine closes the water-arc it has run since 14:21 (sea as wall, sea as grave, no water, bitter water, sweetened water, twelve springs): the chapter that opened with water defeated ends encamped beside water given — and the block seals with the there-word's third station (the syllabus-grammar of 15:25 resting).")])

# ---- scenarios ----------------------------------------------------------
BASE = "no test, no name."
REG = "REGISTRY: maqom->Mara (1 write)"
DMIR = "LET(shiru_la_YHWH) pushed and OPEN;"
DDRINK = "LET(ma_nishte) pushed and OPEN;"
DCOV = "LET(im_shamoa_tishma) pushed and OPEN;"
expects = {}
for vs in range(1, 21):
    expects[vs] = [BASE]
expects[21] = [DMIR, BASE]
expects[22] = [DMIR, BASE]
expects[23] = [DMIR, REG]
expects[24] = [DMIR, DDRINK, REG]
expects[25] = [DMIR, REG]
expects[26] = [DMIR, DCOV, REG]
expects[27] = [DMIR, DCOV, REG]
titles = {
    1: "then sang Moses", 2: "my strength and song", 3: "a man of war",
    4: "cast into the sea", 5: "the deeps cover them", 6: "Your right hand doubled",
    7: "like stubble", 8: "the wind of Your nostrils", 9: "the enemy said",
    10: "sank like lead", 11: "who is like You", 12: "the earth swallowed",
    13: "You guided in kindness", 14: "the peoples heard", 15: "the chiefs dismayed",
    16: "still as a stone", 17: "plant them on Your mountain", 18: "the reign forever",
    19: "the prose seal", 20: "Miriam takes the timbrel", 21: "sing to the LORD",
    22: "three days, no water", 23: "Marah named", 24: "what shall we drink",
    25: "the tree and the statute", 26: "I am your Healer",
    27: "twelve springs, seventy palms",
}

steps, scenarios = [], []
for i, vs in enumerate(sorted(V), 1):
    spec = V[vs]
    steps.append(unitgen.build_step(db, "Exod", "Exod", 15, vs, i, spec))
    scenarios.append(unitgen.scenario_for(
        db, "Exod", 15, vs, "S%d" % i,
        "after STEP_Ex_15_%d — %s" % (vs, titles[vs]),
        spec["en"].replace("[EN-AID] ", ""), expects[vs]))

ttl_he, ttl_tr = unitgen.join_tokens(unitgen.verse_tokens(db, "Exod", 15, 1)[11:13], strip_accents=False)

META = '''# =============================================================================
# LOGIC UNIT: Exodus 15:1-27 — the Song at the Sea, Miriam's antiphon, Marah's
#             statute-station, and the twelve springs
# FORWARD ERA unit #29 — derived 2026-08-09 (oral layer in-pipeline; review waived)
# Run FWD-6 block 5 (REDONE post-crash: the verified manifest was the whole
# inheritance; unit rebuilt on owner order 2026-08-09 evening).
# =============================================================================
# Experimental model — not binding religious law.

meta:
  id: "exo_15_the_song_and_marah"
  title_en: "The Song and Marah (15:1-27)"
  title_he: %s
  title_he_translit: "%s"
  title_he_en: "'I will sing to the LORD'"
  book_he: שְׁמוֹת
  book_he_translit: Shemot
  book_en: Exodus
  refs: "15:1-27"
  unit_span_planned: "15:1-27"
  data_paths_he:
  - "Data/Exod.xml"
  status: frozen
  draft_note_en: >
    DERIVED 2026-08-09 · FORWARD ERA unit #29 (run FWD-6 block 5;
    Exod 1-15 continuous behind it). Span: 15:1-27, whole chapter:
    27 verses (SNAPSHOT-verified; 15:12, 15:18, 15:24 without
    etnachta). Oral layer IN-PIPELINE: manifest 13/13 VERIFIED,
    zero FAILED — see oral_audit_note_en. BLOCK HISTORY: the
    first derivation session died 2026-08-09 18:27, nine seconds
    after the manifest verified — the unit was rebuilt from that
    verified inheritance on owner order the same evening.

    MACHINE PROFILE. THREE DECLAREs, ONE RESULT, TWO EVENTS, ONE
    NAME. The SONG EVENT stamps 15:1 (shirat ha-yam — the
    corpus's first song; the refrain's seven tokens minted, and
    returned VERBATIM at 15:21, asserted). The Song's body
    (15:2-18) encodes as sung PRECONDITION_STATE facts: the
    salvation-arc receipted in first person (14:13 → 14:30 →
    15:2); the war-doctrine resolved to a title (14:14 → 14:25 →
    15:3); 14:21's east wind re-sung as the nostrils' blast
    (15:8); the enemy's FIVE dead vows quoted unconjoined (15:9
    — the quoted-mood class, agent drowned: no push); the
    swallow-ledger extended (7:12's staff → 15:12's earth, Num
    16:32 armed); the panic-quartet forecast (15:14-16, Joshua's
    receipts armed outside the Torah); the sanctuary-forecast
    OPEN (15:17, 25:8 armed); the reign-line (15:18). The prose
    warrant-verse 15:19 re-inscribes 14:29 as testimony. MIRIAM
    SIGNED at 15:20 (the 2:4 sister named + titled prophetess;
    registry append at fold). Miriam's imperative pushes at
    15:21 — OPEN at close (unnarrated-compliance class). The
    murmur-verb's exact form debuts at 15:24 (its Torah-three
    asserted: Marah, the spies, after Korah); ma-nishte pushed
    15:24, POPPED 15:25 by the SWEETENING EVENT (the corpus's
    first repair-miracle; the could-not-drink clause of 7:21
    returned at 15:23, asserted — one river ruined, one pool
    healed). Marah NAMED (REGISTRY 1). The first
    statute-station files at 15:25 (choq u-mishpat, law before
    Sinai) with the VERDICT-LESS TEST (nisahu — TESTS 0; 16:4
    armed). The LISTEN-COVENANT pushes at 15:26 —
    perpetual-conditional, OPEN (19:5 armed; the healer-title
    extends the I-am-the-LORD formula). Elim closes the
    water-arc (15:27). Queue at close: TWO OPEN in-unit
    (Miriam's shiru — unnarrated class; the listen-covenant —
    perpetual class) plus the standing opens behind. REGISTRY 1;
    TESTS 0.

    CARE-POINTS: the Song's archaic register (the -mo object
    suffixes clustering, the paragogic nun, the three
    no-etnachta verses); the quoted dead volitives (15:9 push
    nothing); the vow-cohortatives (15:2, self-directed praise,
    not demands); Miriam's masculine la-hem (15:21); the
    then-word pair (15:1 song / 15:15 dread, asserted); the
    there-word triple (15:25 ×2 + 15:27, asserted); the
    verse-numbering note: the murmur-form census (15:24, Num
    14:2, Num 17:6) is exact-form only — the lodge-verb
    homographs share the skeleton in other forms and are
    excluded by form. WATCHLIST ARMS: 16:2 (murmur + Aaron),
    16:4 (the test named), 17:1-7 (the thirst repeated; the
    cry), 19:5 (if-you-listen scaled), 24:4 (twelve pillars),
    25:8 (the sanctuary-forecast's receipt), Num 16:32 (the
    earth-swallow), Num 20 (the water-striking), Num 21:17 (the
    Well — the second then-sang, VERIFIED pair), Num 12:13
    (Miriam's five-word prayer, standing). Outside-Torah names
    (named-only): Josh 2:9-11 + 24:25, Ezra, Jeremiah's
    rebelled-twin, Solomon's dedication, Ps 146:10.
  oral_audit_note_en: >
    ORAL AUDIT 2026-08-09 (IN-PIPELINE, forward era; manifest
    logic/oral_audit/manifests/exo_15_the_song_and_marah_claims.json
    13/13 VERIFIED, zero FAILED; record
    logic/oral_audit/AUDIT_exo_15_2026-08-09.md). CROWNS
    (chain-attested + DB-verified). THE GUARD-DAGESHIM
    [EX15-01, MS on 15:1/11/13/16 — the Masorah's Daniel-5
    guard-list; Lekach Tov; the Rokeach; Ben Asher] — THE
    UNIT'S MARQUEE: the Song's consonants harden exactly where
    praise could slip — מי כמכה ("who is like You") first SOFT
    then HARD 'so as not to stammer מיכה (MICAH) beside the
    Name' (the idol barred from the Song by one dot); גאלת
    ("You redeemed") gimel HARD lest it sound as מגאל
    ("defiled") and one blaspheme; כאבן ("like a stone") kaf
    HARD lest A STONE silence You; גאה גאה ("highly exalted")
    soft-then-hard in the twin-pairs file; Lekach Tov: 'at
    first a WEAK LIP, at the end WITH A FULL MOUTH.' THE TWO
    LEAN LIKE-YOU'S [EX15-02, MS + Kitzur on 15:11]: the
    Ramah — every כמוך ("like You") in the Torah full-vav
    without final he EXCEPT TWO, lean WITH the he, BOTH IN
    THIS VERSE (census exact); באלם ("among the mighty")
    lean-of-lean Torah-unique, read by Gittin and the Mekhilta
    as 'among THE MUTE' — the darkest praise in the brightest
    line; Isaiah's oak-idols the full twin. THE TEN SONGS
    [EX15-03, Kitzur on 15:1]: אז ישיר ("then sang") exactly
    twice in the Torah — the Sea and the Well (Num 21:17,
    where Moses goes unnamed, 'FOR HE WAS STRUCK THROUGH
    WATER'); the yod counts the TEN SONGS, the last unsung;
    and מאז ("since then," 5:23) — 'with the word I
    complained, with that word I BEGIN THE PRAISE.' THE PEOPLE
    FORMED TWICE [EX15-04, Kitzur on 15:13]: עם זו ("the
    people this-one") twice in the Torah, both in this Song
    (redeemed / acquired), Isaiah's 'formed' the third —
    redemption as second creation; נחית ("You guided")
    Torah-unique with the shepherd-cloud (each led by his
    stride, shaded at noon). THE DWELLING-CIPHER [EX15-05,
    Kitzur on 15:17]: לשבתך ("for Your dwelling") Torah-unique
    with Solomon's dedication-twins — 'the Temple below
    aligned opposite the Temple above'; לשבתך = ירושלים +
    ציון (752 = 752, asserted); the extra yod of ידיך ("Your
    hands") = ten miracles + ten sanctities. THE
    ANAGRAM-PHARMACY [EX15-06, Kitzur on 15:26]: מחלה
    ("disease") = הלחם ("the bread") = המלח ("the salt"),
    letter for letter (asserted); מחלה = 83 — 'eighty-three
    illnesses hang on the gall; morning bread with salt and
    water annuls them — therefore SPRINGS are juxtaposed'
    (15:27); the healer's pe SOFT, Mishpatim's human healers
    both DAGESHED — Heaven heals gently, man hard (checked).
    THE REIGN AND THE CUTOFF [EX15-07, Kitzur + MS on 15:18]:
    the Kitzur rules a paseq after ימלך ("shall reign") — the
    empires' terminus — and THE STREAM WRITES NONE (checked):
    chain-vs-stream divergence, dual-tracked; Moses
    Name-first, David kingship-first (Ps 146:10); לעלם
    ("forever") lean. THE ONCE-VOCALIZATION [EX15-08, MS on
    15:5]: יכסימו ("cover them") Torah-unique — Rashi:
    'NOTHING LIKE IT in Scripture in its pointing'; במצלת
    ("in the depths") on its ruled skeleton, Hilleli and
    Yerushalmi variants dual-tracked; the three depths in
    darkness (14:20 wired). THE NOSTRIL-PAIR [EX15-09, MS +
    Kitzur on 15:8]: אפיך ("Your nostrils") exactly twice in
    the Torah — MS's own pair-note to Gen 3:19's sweat:
    curse-labor and rescue-blast on one noun; the four winds;
    בלב ים ("in the heart of the sea") unique — the paved
    road and the drunkard. THE FIVE SENDINGS [EX15-10, Kitzur
    on 15:7]: תשלח ("You send forth") exactly FIVE in the
    Torah (the Akeda's stayed hand, send-by-whom, the
    burning, show-me, the mother-bird) — the fathers sent,
    the children brought in; קמיך ("Your risers") unique with
    the Psalm's therefore-You-break. THE THREE REFOUNDINGS
    [EX15-11, Kitzur on 15:25/22-23]: חק ומשפט ("statute and
    ordinance") Torah-unique at Marah — Joshua at Shechem,
    Ezra's teaching: three refoundings on one phrase; שם
    ("there") = פרה אדומה ("red heifer") with the inclusive
    one — the paradox-statute founded at the first
    statute-station; מרתה ("to Marah") unique with its twin in
    Jeremiah ("she has rebelled"); the jewel-derash on the
    forced march; Job in Pharaoh's counsel. THE BUTCHERED CHOICE [EX15-12,
    Kitzur on 15:4/2/6]: ומבחר ("and the choice of")
    Torah-unique — 'they went down to be BUTCHERED on the
    rocks of the sea'; the chariot-word's idol-file (Josiah's
    sun-chariots, Shebna); עזי ("my strength") unique with
    the sweet-floor drawn in joy; בכח ("in power") an
    all-Torah pair — the Song's arm re-invoked at the calf
    (32:11). THE LETTER-FILE [EX15-13, MS]: the Song's layout
    LAW CLOSED at 15:20 — 'in a Torah scroll ONE COLUMN, five
    lines before and five after' (14:25's brick-grid arm
    executed); באלם bet dageshed with NO paseq 'against the
    printer's emendation' (authority ten); עזי ("my
    strength") with its first vowel ruled short (the ayin in
    קמץ חטוף, "clipped qamatz") for the zayin's dagesh that
    MARKS THE DROPPED ROOT-LETTER (loss spelled inside
    strength; בעזך 15:13 same rule); the sheva-alone rulings
    (נאדר, צללו, וארממנהו); כעופרת ("like lead") full against
    the spoils'-furnace lean (Num 31:22, checked); צללו
    ("they sank") unique — sinking, quivering lips, darkened
    gates; זרועך ("Your arm") full vs the Yerushalmi's lean,
    dual-tracked; גאונך ("Your exaltation") full, the old
    tikkun's variant named; מקדש ("sanctuary") qof dageshed
    LE-TIFERET ("for splendor"); חקיו ("His statutes") qof
    hard with Ben Asher cited twice in one verse (15:26);
    ותצאן כל ("and all went out") kaf soft; ישיר ("he sings")
    bound by maqqef; נערמו ("were heaped") full-yod with MS's
    own preference for the binder-stroke confessed ("bound —
    and it is correct in my eyes").
  owner_language_note: >
    English for reading only. Hebrew is the derivation source.
  oral_policy_note_en: >
    Written trees first. Dual-track Oral only when named; never
    silent-merge.
  tree_derive_version: logic_derived_v1
  tree_derive_phase: "FWD-29"
  confidence_overall: "structure tested; oral layer verified 13/13"
  genre: "song_and_station_fsm"
  build_track: exodus_stack
  depends_on: exo_14_the_sea_splits
  depends_note_en: >
    Depends for PATTERN only (the Song re-describes the split; the
    salvation and silence arcs pay; the layout-law arm executes).
    Standalone machine. Exod 1-15 continuous, 91 frozen units.
''' % (ttl_he, ttl_tr)

DLOG = '''derivation_log:
  - step: A
    name_en: "Block choice"
    comment: >
      FORWARD ERA run 6, block 5 (owner: "process the next 5 blocks
      of exodus"). Canon continuation: Exod 15:1-27 — the Song, Miriam,
      Marah, Elim; whole chapter. REDO: the first session crashed
      2026-08-09 18:27 with the manifest verified and no unit built;
      rebuilt the same evening on owner order ("redo exodus 15"),
      wall-clock timed per the owner's request.
    confidence: established
  - step: B
    name_en: "Span + source + conventions"
    comment: >
      SNAPSHOT prestage: 27 verses; 15:12, 15:18, 15:24 without
      etnachta. No ketiv/qere pairs in-span. Volitive census: the
      Song's cohortatives are self-directed praise-vows (15:1
      ashira; 15:2 anvehu, aromemenhu — quoted-mood, no push); the
      enemy's five vows (15:9) are quoted dead — no push; the real
      pushes are Miriam's imperative (15:21), the people's plea
      (15:24), and the listen-covenant (15:26).
    confidence: established
  - step: C
    name_en: "Machine structure"
    comment: >
      Three DECLAREs, one RESULT (15:25 pops ma-nishte), two EVENTS
      (the Song 15:1; the sweetening 15:25 — the corpus's first
      repair-miracle), one NAME (Mara, 15:23 — REGISTRY 1). The
      verdict-less test filed as fact (TESTS 0). The refrain's
      verbatim return, the murmur-form's Torah-three, the
      could-not-drink echo of 7:21, the then-pair, and the
      there-triple asserted at the build as machine evidence.
      Queue at close: TWO open in-unit (the antiphon-command,
      unnarrated class; the listen-covenant, perpetual class).
    confidence: tested
  - step: D
    name_en: "Oral scan (in-pipeline)"
    comment: >
      Local mirror only (zero fetches): Minchat Shai on Exod 15 (28
      notes) + Kitzur Baal HaTurim on Exod 15 (28 notes). Manifest
      13 rows: 13 VERIFIED / 0 FAILED / 0 UNCHECKABLE (re-verified
      at the redo before the build). The guard-dageshim; the two
      lean like-You's; the ten songs; the people formed twice; the
      dwelling-cipher; the anagram-pharmacy; the reign-cutoff
      divergence; the once-vocalization; the nostril-pair; the five
      sendings; the three refoundings; the butchered choice; the
      letter-file with the Song-layout law closed.
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
      not silent edits. Exod 1-15 continuous.
    confidence: established
'''

unitgen.emit_unit(META, DLOG, steps, scenarios, "logic/units/exo_15_the_song_and_marah.yaml")
print("wrote logic/units/exo_15_the_song_and_marah.yaml —", len(steps), "steps,", len(scenarios), "scenarios")
