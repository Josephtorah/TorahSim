import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
import os, subprocess
ROOT = _ROOT   # the scratch form: ROOT from git, never typed
# THE DEUTERONOMY WALK sitting 7 — CHAPTER 9 (2026-09-19; the owner: "Let's keep run as it is and do another section"): THE DESIGN appended to the map after
# the measurements and the ink, before a row is typed. The guard names THE SITTING (5b's lesson: a guard that matches another sitting's string is no guard).
P = ROOT + '/World/step9/DEUTERONOMY_WALK.md'
s = open(P, encoding='utf-8').read()
HDR = '## Sitting 7 — CHAPTER 9, Deuteronomy 9:1-29 (2026-09-19; the owner: "Let\'s keep run as it is and do another section" after THE GATES CUT): the reading and the unit — THE DESIGN, written after the measurements and the ink, before a row is typed; ONE RUN (a reading sitting under THE TWO-RUN RULE)'
assert HDR not in s and '## Sitting 7 — CHAPTER 9' not in s
D = HDR + '''

THE ONE RUN: the rereads (the recovery page, the map\'s "Sitting 6b — AS BUILT", the memory index; THE_STEPS Step 2 whole, Step 5\'s head and the compiler block), the
measurements (ch9_dump0.py derived from the forms\' ch8_dump0.py by twenty-three asserted substitutions; ch9_measure1.py — chapter 8\'s helpers and register block by
substitution, its eight sections chapter 9\'s own: 586 kin diffs, the phrase censuses, the seven number verses, Onkelos\'s renderings over the book, the English\'s
brackets, the store\'s gloss families, the prior reads), THE INK (ch9_ink.py — every fact an assert typed from the prints; EIGHTEEN fell on the first pass and thirteen
forms were retyped from the print, none a fact: the shelf\'s own spellings "hyperbole" and "a-fortiori" as its bytes carry them, the Name\'s count, the shared counts of
single tokens, "fortified" plene at 1:28 against defective at 9:1, the article of "who passes over", three phrase splits; 0 on the second), THIS DESIGN, then the rows,
the ledger, the display patch, the manifest, the seat, the chain, the fold, the gates, the records, the forms, the commit message, the clean point.

THE DRAFT: deu_09_not_righteousness 9:1-29 — 29 of 29 verses, missing 0 (computed from the DB\'s verse table), depends_on deu_08_manna_humility and exo_32_golden_calf
(both frozen — asserted), 36 scenarios and 33 comment lines in the draft (typed from the dump\'s G print), the claim prefix DV09 absent from every unit and manifest
(computed). The chapter the unit, per the ruling CHAPTER NUMBERS; the portion Ekev runs on (7:12-11:25) — no edge inside the chapter.

THE TWO DIVISIONS AGREE: the export\'s chapter 9 twenty-nine rows, the DB\'s twenty-nine verses; the alignment instrument gives the identity at cost 37 (asserted; chapter
5\'s 30-against-33 the book\'s one split); the store\'s token count equals the DB\'s at every verse (499 tokens, 1,973 letters); NO written/read pair in the chapter (the
DB\'s wtype None at all 499 — the first chapter of the book\'s walk without one since chapter 4); the store\'s three "?" glosses are its own split place names ("and-in-?"
the Kibroth of Kibroth-hattaavah at 9:22, "from-?" the Kadesh of Kadesh-barnea at 9:23) and 9:2\'s "who?".

THE SHELF, BY POSITION — THE SPINE IS SILENT ON THE CHAPTER (chapters 4, 7 and 8 the form): no piska head in chapter 9 — 36 on 6:9 before, 37-38 on 11:10 and 39 on 11:11
after (the heads computed on the Hebrew\'s first rows; chapters 7-10 without a section — asserted). Its whole voice on the chapter is SEVEN rows outside any piska, found
by the union of both files\' citations (the Hebrew\'s strict form reads six rows, the English\'s nine hits add 342:1, whose Hebrew cites the RANGE "9:7-8" the regex does not
read — asserted by string): 14:1 on 1:14 (from whom to learn Torah — from Moses who suffered for it forty days and nights: 9:9 quoted beside Exodus 34:28), 25:4 on 1:28
(Rabban Shimon ben Gamliel\'s HYPERBOLE RULE — 9:1\'s "fortified to the heavens" is hyperbole; the promise to Abraham of the stars is not), 26:7 on 3:23 (THE TEN NAMES OF
PRAYER — 9:25 "I fell down" is falling, 9:26 "I prayed" is prayer), 27:2 on 3:24 (THE DOOR OPENED — "let Me alone and I will destroy them", 9:14: was Moses holding the
Holy One? He opened the door; the a-fortiori: if the prayer of one for the many is heard, the prayer of the many for one all the more — I1, the row\'s own words "קל
וחמר" ("light and heavy")), 306:25 on 32:2 (Moses\' suffering for the Torah among the angels — 9:9 quoted beside Exodus 34:28; THE ENGLISH MIS-CITES the Exodus verse as
"Ex.36:28" where the Hebrew has 34:28 — a slip on the kin\'s citation, the row kept and read whole in both files), 342:1 on 33:1 (the harsh words spoken first — "at Horeb
you provoked the LORD", "you have been rebellious", 9:7-8 among 32:24-25 — then the blessing), 357:44 on 34:12 (R. Elazar: the breaking of the tablets among the
wonders "before the eyes of all Israel" — "it is said there: I broke them BEFORE YOUR EYES (9:17), and here: which Moses did before the eyes of all Israel" — the verbal
analogy, I2). FOUR of the seven were read at sitting 1 (14:1, 25:4, 26:7, 27:2 — chapters 1-3\'s piskaot; 25:4 also at a Genesis sitting by topic) and are REREAD WHOLE
here under the whole-row rule; three are fresh (306:25, 342:1, 357:44). Three of the seven piskaot\'s first rows carry no head citation (14, 27, 342): the row\'s own first
citation stands for the head, asserted by string. No "ibid" candidates; no interpolation; none excluded (no cited verse beyond 29). The prior reads over the ledgers:
twelve ledgers NAME a verse of chapter 9 (the Numbers walk\'s Taberah and Kibroth rows, the rejection\'s "the offer\'s second seat" on 9:14, the milluim and investiture
ledgers on 9:20 — Aaron\'s peril known from Deuteronomy alone; asserted); no ledger holds an Onkelos row of chapter 9.

THE INK, COMPUTED (ch9_dump0.py, ch9_measure1.py; the asserts typed from the print):
- THE PARSER MEASURED FIRST: SEVEN number verses in 29 — the forty days and forty nights [40, 40] at 9:9, 9:11, 9:18, 9:25 (the phrase\'s NINE Bible seats: Genesis 7:4,
  7:12 the rain, Exodus 24:18, 34:28, Deuteronomy 9:9, 11, 18, 25, 10:10; 1 Kings 19:8 Elijah\'s the tenth; the article\'s form "THE forty days and THE forty nights" 9:25
  alone); the two tablets [2] at 9:10, 9:11 and the two tablets on the two hands [2, 2] at 9:15, 9:17 (the dual marked); "swore" (9:5, the lemma 7650) NOT a number —
  the seven-stem homograph as at 8:1, 8:18; no ordinal; NO GAP. The kin: Exodus 24:18 [40, 40], 34:28 [40, 40, 10] (the ten words), 31:18 [2], 32:15 [2], 4:13 [10, 2],
  10:4 [10] with the ordinal [1] "the first writing", 10:10 [40, 40]; Numbers 13:25 [40] the spies\' forty days; Exodus 32:28 [3000] the calf\'s dead.
- THE STORE = THE DB at every verse: no written/read pair; the DB\'s morphology gives 9:10\'s "written" the passive participle (the lemma\'s 76 such seats in the Bible),
  9:21\'s "grinding thoroughly" TWO INFINITIVE ABSOLUTES side by side, the store\'s place names split by their prefixes.
- THE THREE SPELLINGS OF "TABLETS" (the lemma 3871): לוחת ("tablets", plene vav — 9:9 twice, 9:10; elsewhere 10:1 alone), לחת (defective — 9:11, 9:15; Exodus\'s form
  at every seat), לחות (the second plene — 9:11; 4:13 and 1 Kings 8:9 its only kin); 9:11 HOLDS TWO SPELLINGS IN ONE VERSE; "the tablets of the covenant" 9:9, 9:11,
  9:15 — THE BIBLE\'S THREE SEATS, all this chapter\'s (Exodus says "the tablets of the testimony"); "written with the finger of God" Exodus 31:18 and 9:10 alone; "the
  finger of God" Exodus 8:15 (the magicians\'), 31:18, 9:10 — the Bible\'s three.
- THE KIN DIFFED (the DB\'s tokens, the shared tokens counted in order): 9:13 against Exodus 32:9 ELEVEN OF THIRTEEN — God\'s word quoted whole but for "to me, saying"
  where Exodus has "to Moses", the closest row of the chapter; 9:12 against 32:8 nine ("turned aside quickly from the way which I commanded them; they have made them")
  and 32:7 six; 9:9 against Exodus 34:28 nine, 24:18 five ("on the mountain forty days and forty nights"), 24:8 five ("the covenant which the LORD cut with you" — THE
  BLOOD\'S VERSE) and 9:18 eleven (the doublet); 9:10 against 10:4 ten, 5:4 six, Exodus 31:18 five; 9:14 against Exodus 32:10 three ("and I will make you into a nation")
  and Numbers 14:12 three single tokens — THE OFFER\'S THREE FORMS ("a great nation"; "a nation greater and mightier than it"; "a nation mightier and more numerous than
  they"); 9:15 against 32:15 four; 9:16 against 32:8 four and 32:4 three ("a molten calf"); 9:17 against Exodus 32:19 ONE TOKEN — THE BREAKING RETOLD IN MOSES\' OWN WORDS
  ("I took hold … threw them from my two hands … broke them before your eyes" against "he threw from his hand the tablets and broke them beneath the mountain"); 9:18
  against 34:28 ten; 9:19 against 10:10 six and Exodus 32:14 one (the relenting told as "hearkened"); 9:20 against Exodus 32:21 one — AARON\'S PERIL TOLD ONLY HERE (Exodus
  has his making, not the LORD\'s anger at him nor Moses\' prayer for him); 9:21 against 32:20 seven ("the calf … until it was fine" — the dust to the brook here, the
  water drunk there); 9:23 against 1:26 five and Joshua 14:7 five; 9:26 against 1 Kings 8:51 five (SOLOMON QUOTES THIS TELLING — "Your people and Your inheritance whom
  You brought out of Egypt") and Exodus 32:11 five; 9:27 against Exodus 32:13 three — "to Abraham, to Isaac" shared, ISRAEL there and JACOB here, "Your servants" both;
  9:28 against Numbers 14:16 seven ("the LORD was not able … into the land which") and Exodus 32:12 two ("why should the Egyptians say" there — "lest the land say" here);
  9:29 against 1 Kings 8:51 four (and Nehemiah 1:10 quoting "Your great power" from this verse). The opening: 9:1 against 4:38 four ("nations greater and mightier than
  you" — the two seats), 9:2 against 1:28 five, 9:3 against 31:3 nine and 4:24 six ("a consuming fire"), 9:5 against 30:20 ten, 9:6 against Exodus 33:3 seven ("for you are
  a stiff-necked people"), 9:7 against 11:5 six ("until you came to this place").
- THE PHRASE CENSUSES (the crowns): "Hear, O Israel" FOUR (5:1, 6:4, 9:1, 20:3); "nations greater and mightier than you" 4:38 and 9:1 alone; "cities great and fortified
  to the heavens" 1:28 (plene) and 9:1 (defective) — the spelling the only difference; "a people great and tall" and "the sons of the Anakim" 1:28 and 9:2 alone; "who can
  stand before" 9:2 the Torah\'s one seat; "a consuming fire" 4:24, 9:3 in the book; "righteousness" the noun 9:4, 5, 6 — three of the Torah\'s nine seats (Abraham\'s at
  Genesis 15:6), the chapter\'s thread; "wickedness" the noun 9:4, 9:5, 25:2 — the Torah\'s three; STIFF-NECKED SIX SEATS IN THE BIBLE, ALL THE CALF\'S (Exodus 32:9, 33:3,
  33:5, 34:9, Deuteronomy 9:6, 9:13); "stubbornness" (9:27) the Bible\'s ONE seat of the noun; "remember, do not forget" ONE; the imperative "remember" 9:7, 9:27, 32:7 in
  the book; "provoke" the hiphil 9:7, 8, 22 — THE TORAH\'S THREE, all this chapter\'s; "you have been rebellious with the LORD" 9:7, 9:24 alone (31:27 the kin); "and the
  LORD was angry" (the hithpael) 1:37, 4:21, 9:8, 9:20 — the book\'s four; "to destroy you" 9:8, 19, 25 and "to destroy him" (Aaron) 9:20 the Bible\'s one seat;
  "bread I did not eat and water I did not drink" 9:9, 9:18 (Exodus 34:28 and Ezra 10:6 the third person); "and I stayed on the mountain" 9:9 (Isaiah 14:13 the king of
  Babylon\'s boast the only other); "at the end of forty days" 9:11, Genesis 8:6 (the ark\'s window), Numbers 13:25 (the spies\' return); "on the day of the assembly"
  9:10, 10:4, 18:16 — the book\'s three; "from the midst of the fire" ten in the book; "arise, go down quickly" ONE — Exodus 32:7\'s "go, get down"; "your people have
  corrupted" 9:12 and Exodus 32:7 alone (Isaiah 14:20 the homograph); "turned aside quickly from the way" Exodus 32:8, 9:12, 9:16, Judges 2:17 — the four; "a molten calf"
  Exodus 32:4, 32:8, 9:16, Nehemiah 9:18; "the calf" the Torah\'s ten seats (Exodus 32\'s seven, 9:16, 9:21, Leviticus 9\'s two); "I have seen this people" 9:13 and Exodus
  32:9 alone; "let Me alone" (9:14) ONE — Exodus 32:10\'s "let Me be" another verb; "blot out their name from under heaven" — 9:14 among the eight "from under heaven"
  seats (7:24, 25:19 Amalek, 29:19, Exodus 17:14); "and I will make you into a nation" Exodus 32:10, Numbers 14:12, 9:14 (Genesis 12:2 Abram\'s); "the mountain burned
  with fire" 4:11, 5:23, 9:15 — the book\'s three; "before your eyes" 1:30, 9:17, 29:1; "and I looked, and behold" 9:16 THE TORAH\'S ONE SEAT of the prophets\' vision
  formula (Ezekiel, Zechariah, Daniel); "fell down before the LORD" (the hithpael) 9:18, 9:25 — the Torah\'s two; "to do what is evil in the eyes of the LORD" 9:18 THE
  TORAH\'S ONE SEAT of the Kings\' formula (fifty-three in the DB); "to provoke Him" 4:25, 9:18, 31:29 — the book\'s three; "the anger and the wrath" 9:19 (Jeremiah 36:7);
  "afraid" (יגר, 9:19) 9:19 and 28:60 in the Torah; "and the LORD hearkened to me … that time also" 9:19, 10:10 alone; "at that time" fifteen in the book; "and I prayed"
  (the hithpael) 9:20, 9:26 — the Torah\'s eight seats of the verb: Abraham\'s two, Taberah\'s, the serpents\' two, Jacob\'s "I had not thought", and these; "crushed" (כתת)
  9:21, 1:44 and Numbers 14:45 (the Amorites\' beating) — the Torah\'s three; "grinding" the infinitive absolute ONE; "fine" (דק) 9:21, Exodus 32:20, 30:36 (the incense);
  "the dust into the brook" — JOSIAH\'S KIN (2 Kings 23:6, 23:12 "to the brook Kidron … beat it to dust"); "Taberah" Numbers 11:3 and 9:22 — TWO; "Massah" Exodus 17:7,
  6:16, 9:22, 33:8, Psalm 95:8; "Kibroth-hattaavah" five — DEFECTIVE here and at Numbers 33:16-17, PLENE at 11:34-35 (the Numbers ledger noted it); "Kadesh-barnea" ten
  seats (four in the book); "go up and possess" 9:23 (1:21 "go up, possess" singular); "you rebelled against the mouth of the LORD" 1:26, 1:43, 9:23 — the book\'s three
  (Numbers 20:24, 27:14 Moses\' and Aaron\'s, the form "you rebelled against My mouth"); "the mouth of the LORD" 1:26, 1:43, 8:3, 9:23, 34:5 in the book; "from the day I
  knew you" ONE; "Lord GOD" (the double Name) 3:24, 9:26 in the book — the Torah\'s four with Abraham\'s two (Genesis 15:2, 15:8); "Your people and Your inheritance" 9:26,
  9:29, 1 Kings 8:51 — the three (Psalm 94:14 "His people … His inheritance"); "You redeemed" (the 2ms perfect) 9:26, 21:8 — the two; "with a mighty hand" 5:15, 6:21,
  7:8, 9:26, 26:8 in the book; "remember Your servants" 9:27 (Exodus 32:13 "remember Abraham" — the servants after); "do not turn to" 9:27, Numbers 16:15 (Moses on
  Korah\'s offering), Job 36:21; "its wickedness and its sin" ONE; "lest they say" 9:28, 32:27, Judges 9:54; "because the LORD was not able" 9:28 and Numbers 14:16 — THE
  TWO SEATS, "for lack of" spelled מבלי here and מבלתי there; "because He hated them" 9:28 — 1:27 "in the LORD\'s hatred of us" (the noun\'s Torah seats 1:27, 9:28,
  Numbers 35:20); "to kill them in the wilderness" 9:28 — FOUR FORMS OF THE NATIONS\' TAUNT: "to kill them in the mountains" (Exodus 32:12), "slaughtered them in the
  wilderness" (Numbers 14:16), "to destroy us" by the Amorite\'s hand (1:27), and this; "great power" 9:29, 4:37, Exodus 32:11, 2 Kings 17:36, Jeremiah 32:17, Nehemiah
  1:10; "outstretched arm" 4:34, 5:15, 7:19, 9:29, 11:2, 26:8 — the book\'s six (and Exodus 6:6\'s); the Name thirty-four bare tokens (twenty-one verses); "the LORD your
  God" singular 3-7 and PLURAL at 23 alone; "God" bare at 9:10 (the finger); MOSES NEVER NAMED — the chapter his "I"; Aaron at 9:20; Israel at 9:1; Egypt 7, 12, 26;
  Horeb 8; the Jordan 1; the three fathers 5 and 27; Anak 2.
- THE FRAMES AND THE REGISTER: TWO divine frames INSIDE the retelling (9:12 "and the LORD said to me", 9:13 "and the LORD said to me, saying" — God\'s speech of Exodus
  32:7-9 quoted); "saying" 9:4 (the boaster\'s), 9:13, 9:23; THE NARRATIVE VERBS TWENTY-TWO in sixteen verses over 9:8-26 (chapter 8 had three) — was angry, stayed, gave,
  was, said, said, turned, came down, saw, took hold, threw, broke, fell down, hearkened, prayed, burned, crushed, threw, rebelled, fell down, prayed, said; the first
  person Moses\' in eighteen verses (9:4 the boaster\'s "my righteousness … brought me" the only "I" not his); THE SECOND PERSON SINGULAR in twelve verses — 1-6 Israel,
  then GOD\'S "you" to Moses at 12 and 14, then MOSES\' "You" to God at 26-29 — THREE VOICES ON ONE PRONOUN; PLURAL in twelve (8-10, 16-19, 21-25); BOTH in 9:7 alone (the
  switch inside the verse: "you (sg.) provoked … until you (pl.) came … you (pl.) have been rebellious"); NEITHER in 11, 13, 15, 20; imperatives SIX — "hear" (9:1),
  "remember" (9:7, 9:27), "arise, go down" (9:12, God\'s), "let alone" (9:14, God\'s), "go up and possess" (9:23, God\'s, plural); infinitive absolutes "quickly" four
  times (the adverb\'s form) and 9:21\'s pair; consecutive perfects FOUR, all at 9:3 and 9:6 — the law\'s form only at the opening; NO prohibition "not + imperfect" — the
  chapter\'s "not"s are perfects (did not eat, did not drink, did not believe, did not hearken) and 9:5-6\'s "not for your righteousness"; "for/that" seven seats, "lest"
  ONE (9:28), no "if", no "when"; "so that" ONE (9:5; the book\'s forty-three); the participles: "who passes over before you" (9:3 — the article\'s form 9:3 alone; 31:3
  "He passes over" without it), "consuming", "dispossessing" (4, 5), "gives" (6), "rebellious" (7, 24), "burning" (15), "that descends" (21), "provoking" (22).
- ONKELOS (the renderings\' seats over the book, computed): 9:3 THE MEMRA — "His Word is a consuming fire" for "He is a consuming fire" (4:24 and 9:3 the two seats of
  the phrase; "His Memra" ten seats in the book); 9:23 THE DECREE OF THE MEMRA for "the mouth of the LORD" (1:43 the kin — the two seats) and "you did not accept His
  Memra" for "did not hearken to His voice"; MERIT for "righteousness" (9:4, 5, 6 — three of the book\'s five merit seats) and "the SINS of the nations" for "the
  wickedness"; "to the HEIGHT of heaven" (1:28, 4:11, 9:1); "the sons of the GIANTS" (9:2); "when He SMASHES them" for "thrusts them out" (9:4); THE REVERENCE — "you
  provoked BEFORE the LORD" (7, 8, 22), "rebellious BEFORE the LORD" (7, 24), "there was anger FROM BEFORE the LORD" (9:8, 9:20 — 1:37 and 3:26 the kin, the four seats),
  "it is REVEALED before Me" for "I have seen" (9:13; 31:21, 32:20 the kin), "LEAVE YOUR PRAYER from before Me" for "let Me alone" (9:14 — the prayer SUPPLIED; Exodus
  32:10\'s Onkelos the same), "the LORD ACCEPTED MY PRAYER" for "hearkened to me" (9:19, 10:10 — the two seats), "I prayed BEFORE the LORD" (9:26; 3:23); 9:21 THE FILE —
  "I filed it with a file, well" for "crushed it, grinding thoroughly" (Exodus 32:20\'s Onkelos "he filed it"), and TWO ARAMAIC WORDS FOR FIRE: the calf burned "in
  nura" (the burnings\' fire — 7:5, 7:25, 12:3, 12:31, 13:17, 18:10 and 9:21: the idols, the Asherah, the child, the city, the calf) against "eshata" the mountain\'s fire
  (9:10, 9:15 and the seventeen theophany seats); 9:22 THE THREE NAMES TRANSLATED — "in the Burning, in the Testing, in the Graves of the Askers" (as at Numbers 11:3,
  11:34-35 and Exodus 17:7 — the Onkelos Numbers and Exodus rows quoted; "the Testing" spelled נסתא here, נסיתא at Exodus 17:7; 28:22\'s "burning" the fever); 9:23
  REKEM GEAH for Kadesh-barnea (1:2, 1:19, 2:14, 9:23 — the four seats); 9:26 "the LORD God" for the double Name (3:24 the kin), "with Your STRENGTH" for "Your
  greatness"; 9:28 "THE INHABITANTS of the land" supplied for "the land [would] say"; 9:29 "Your great strength and Your UPLIFTED arm" (7:19, 11:2, 26:8 the kin);
  "stiff-necked" literal, "hard of neck" (9:6, 9:13). The English\'s brackets TWENTY-ONE in thirteen verses (the supplied words: merit, sins, His word is, from before,
  revealed before Me, Rekam Geyah, the decree of the word of, accept His word, the inhabitants); no parenthesis rows in chapter 9.
- THE DISPLAY LAYER (the patch): THIRTY-SIX rewrites BY GLOSS where the store\'s every token of the gloss is the one word ("the-meaning-to-glisten" → "the-tablets",
  "crack-off" → "provoke", "in-something-to-sieze-with" → "with-the-finger", "pouring-over" → "molten-image", "the-nose" → "the-anger", "nape" → "neck", "the-assemblage"
  → "the-assembly", "imbibe" → "drink", "grind-meal" → "grinding", "to-die-them" → "to-kill-them", "in-rightness-me/my" → "for-my-righteousness", "in-wrong" → "for-the-
  wickedness-of", "and-in-?" → "and-in-Kibroth", …) and SIXTY BY REFERENCE where the family is mixed ("mark" → "remember" at 9:7, 9:27; "sin-offering" → "your-sin" at
  9:18, 9:21 and "its-sin" at 9:27 — the homograph with Leviticus\'s offering; "be--bitter" → "rebellious" at 9:7, 9:24; "build-up" → "you-believed" at 9:23; "and-judge"
  → "and-I-prayed" at 9:20, 9:26; "and-manipulate" → "and-I-took-hold-of" at 9:17; "sever" → "you-redeemed" at 9:26; "slacken" → "let-alone" at 9:14; "grave" →
  "written" at 9:10; "decay" → "has-corrupted" at 9:12 and "destroy" at 9:26; "severe" → "stiff" at 9:6, 9:13; "Lord-me/my" → "Lord" at 9:26; "from-?" → "from-Kadesh" at
  9:23; "Kibroth-hattaavah" → "hattaavah" at 9:22 beside the by-gloss Kibroth; "food" → "bread" at 9:9, 9:18; …); TWENTY-FIVE of the chapter\'s glosses ALREADY rewritten by
  the earlier sittings ("tablets", "forget", "quickly", "in-the-wilderness", "and-fortified", "was-angry", "to-provoke-him", "the-outstretched", "Anakim", …); the
  anchors sitting 6\'s last rows ("hear-suffix": "hear" the by-gloss block\'s, "Deut.8.20:3" the by-ref block\'s).

THE CLAIMS PLANNED (write_ch9_manifest.py): SIX — DV09-01 9:1-6 NOT FOR YOUR RIGHTEOUSNESS (the frame — Hear, O Israel; the nations greater and mightier, the
Anakim, the consuming fire who passes over before you; the three reasons — the nations\' wickedness, the word sworn to the fathers, the stiff neck; the boaster\'s "my
righteousness" barred); DV09-02 9:7-14 THE CALF RETOLD, THE FIRST FORTY DAYS (remember, do not forget — rebellious from Egypt to here; Horeb; the tablets of the covenant,
forty days and nights without bread or water; the two tablets written with the finger of God on the day of the assembly; God\'s word: go down, your people have corrupted
— a molten image; the stiff-necked people; "let Me alone … a nation mightier than they"); DV09-03 9:15-21 THE BREAKING, THE SECOND FORTY DAYS, AARON, THE CALF\'S DUST
(the mountain burning, the two tablets on the two hands; the molten calf seen; the tablets broken before your eyes; the prayer of forty days for all your sin; the
anger and the wrath feared, the LORD hearkened that time also; Aaron\'s peril and the prayer for him; the calf burned, crushed, ground fine as dust, thrown into the
brook); DV09-04 9:22-24 THE FOUR PROVOCATIONS (Taberah, Massah, Kibroth-hattaavah; Kadesh-barnea — go up and possess, you rebelled, did not believe, did not hearken;
rebellious from the day I knew you); DV09-05 9:25-29 THE INTERCESSION (the forty days again; Lord GOD, do not destroy Your people and Your inheritance redeemed with Your
greatness; remember Your servants Abraham, Isaac and Jacob; do not turn to the stubbornness; lest the land say — not able, hated them, to kill them; Your people and
Your inheritance, Your great power and outstretched arm); DV09-06 THE RETELLING ON THE TAPE — the readback\'s rows OWED to the compile (7b): 9:8-21 against Exodus 32\'s
lines (the calf made, the tablets broken, Moses\' prayer, the calf burned), the forty days against Exodus 24:18 and 34:28, the tablets against 31:18, Aaron\'s peril
(9:20) an act TOLD ONLY IN THE RETELLING, 9:22-23 against Numbers 11:1-3, Exodus 17:1-7, Numbers 11:31-34 and 13-14, 9:26-29 against Exodus 32:11-13 — the prayer\'s
second telling. Seated as six WITNESS_READ operators at 9:1, 9:7, 9:12 (God\'s word retold), 9:15, 9:22, 9:25; step E.

OWED TO THE COMPILE (sitting 7b; the box in COMPILE_DEBT.md at the records): THE READBACK\'S ROWS of the calf (9:8-21, 9:25-29) against the kitisa runner\'s lines and
the ascent\'s (Exodus 24:12-18), the second tablets\' (34:1-4, 28) and the craftsmen\'s (31:18) — the forms VERBATIM (9:13), VARIANT (9:12, 9:9, 9:21), EXPANDED, TURNED
(the relenting as "hearkened", 9:19), and THE ACT TOLD ONLY HERE (9:20 — the LORD\'s anger at Aaron and Moses\' prayer for him: a RETROGRADE WRITE at Exodus 32\'s own day,
the design question), THE STATE "stiff-necked" (9:6, 9:13 — is it a status on Israel on the tape? Exodus 32:9\'s line measured at the design); THE THREE FORTIES — the
tradition\'s three ascents (Exodus 24:18; 32:30-34:9; 34:28 — Sifrei 14:1 and 306:25 read 9:9 with 34:28) and the tape\'s dates for them (Ta\'anit 4:6: the tablets broken
on the seventeenth of Tammuz — the answer sheet\'s DATE for 9:17; Ta\'anit 28b and Shabbat 87a-88a the forty-day arithmetic from 7 Sivan to 10 Tishri — the clock\'s test);
THE FOUR PROVOCATIONS as run citations of Numbers 11:1-3, Exodus 17:1-7, Numbers 11:31-34, 13-14 (all on the tape); THE INTERCESSION\'S SECOND TELLING (9:26-29 against
Exodus 32:11-13 and Numbers 14:13-19 — the same argument twice on the tape); THE CHECKPOINT PREFIX SPACE — 7b OPENS A NEW SERIES (CU the last two-letter prefix; the
probes\' regexes measured at its design). THE TESTING SHELF routed to 7b\'s docket: Berakhot 32a (Moses\' prayer — "let Me alone": Moses seized the Holy One like a man
seizing his fellow\'s garment; "the anger and the wrath"), Berakhot 7a, Shabbat 87a (Moses broke the tablets on his own reasoning and God approved — "which you broke":
"your strength be firm that you broke"), Shabbat 88a-89a (the forty days), Menachot 99a-b and Bava Batra 14b (the broken tablets in the ark), Avodah Zarah 43b-44a and
Mishnah Avodah Zarah 3:3 (the calf\'s burning and grinding the idol\'s destruction — R. Yose\'s "grind and scatter"), Ta\'anit 4:6 and 28b (the seventeenth of Tammuz — the
tablets broken; the dates of the three ascents), Sanhedrin 102a and Vayikra Rabbah 10:5 (Aaron\'s peril — "to destroy him" his sons), Beitzah 25b (the stiff-necked
people the most impudent of nations), Shabbat 55a (the merit of the fathers — 9:27), Devarim Rabbah 2:1 (the ten names of prayer).

THE ORDER (the rest of the one run): the twenty-nine Onkelos rows and the seven outside rows WHOLE (read at the dump; ch9_onkelos.txt, ch9_sifrei_outside.txt) →
ch9_rows_onkelos_a.py (9:1-14), ch9_rows_onkelos_b.py (9:15-29), ch9_rows_outside.py (sitting 6\'s forms; the cuts by consonants — HP / AP / SP_) → write_ch9_ledger.py
(from write_ch8_ledger.py) → lint 0, coverage computed (Onkelos 29; the Sifrei 7; the kin\'s credits by name — the Exodus ledgers\' rows on the calf, the ascent, the
second tablets and the craftsmen, the Numbers ledgers\' rows on Taberah, Kibroth and the spies) → ch9_patch_overrides.py (36 by gloss, 60 by reference; the anchors
sitting 6\'s last rows), the ink rerun PATCHED → write_ch9_manifest.py (six claims DV09-01..06) → seat_ch9.py (six WITNESS_READ at 9:1, 7, 12, 15, 22, 25; step E) →
ch9_chain.sh (the seat, verify_text, the ritual) → ch9_fold.sh (223 / 2221 / the hash unmoved) → build_world → the journal gate → the register gate --strict →
large_letter_probes → the home-path gate → the records from the sheet in one call → the forms copied → the commit message → the clean point.
'''
s = s.rstrip('\n') + '\n\n\n' + D
open(P, 'w', encoding='utf-8').write(s)
print('the design appended:', len(D.encode()), 'bytes; the map', len(s.encode()))
