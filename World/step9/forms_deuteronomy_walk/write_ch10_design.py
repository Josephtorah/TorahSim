import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
import os, subprocess
ROOT = _ROOT   # the scratch form: ROOT from git, never typed
# THE DEUTERONOMY WALK sitting 8 — CHAPTER 10 (2026-09-19; the owner: "Go"): THE DESIGN appended to the map after the measurements and the ink, before a row
# is typed. The guard names THE SITTING (5b's lesson: a guard that matches another sitting's string is no guard).
P = ROOT + '/World/step9/DEUTERONOMY_WALK.md'
s = open(P, encoding='utf-8').read()
HDR = '## Sitting 8 — CHAPTER 10, Deuteronomy 10:1-22 (2026-09-19; the owner: "Go" after the reread that followed 7b\'s compaction): the reading and the unit — THE DESIGN, written after the measurements and the ink, before a row is typed; ONE RUN (a reading sitting under THE TWO-RUN RULE)'
assert HDR not in s and '## Sitting 8 — CHAPTER 10' not in s
D = HDR + '''

THE ONE RUN: the rereads (the recovery page, the map\'s "Sitting 7b — AS BUILT", the memory index; THE_STEPS\' compiler block, Step 2 whole and Step 5\'s head),
the measurements (ch10_dump0.py derived from the forms\' ch9_dump0.py by twenty-three asserted substitutions; ch10_measure1.py — chapter 9\'s helpers and register
block by substitution, its eight sections chapter 10\'s own: 441 kin diffs with the shared count printed on every line, the phrase censuses, the five number
verses and the plural "first", Onkelos\'s renderings over the book, the English\'s brackets, the store\'s gloss families, the prior reads), THE INK (ch10_ink.py —
the generic helpers COPIED from ch9_ink.py by content markers, never retyped; every fact an assert typed from the prints; EIGHT fell on the first pass, none a
fact: the Numbers walk\'s later ledgers write "Deuteronomy" in full, the Genesis ledgers hold their Onkelos rows in a table with no row line, "and come up to
Me" carries its vav at 10:1 and not at Exodus 24:12, "the ark of the testimony" spelled two ways in Exodus, "your might" beside Josiah\'s "his might", the
heaven of heavens with the vav at 1 Kings 8:27 as at 10:14, "seventy" forty-two seats, the Bene-jaakan tokens; 0 on the second), THIS DESIGN, then the rows,
the ledger, the display patch, the manifest, the seat, the chain, the fold, the gates, the records, the forms, the commit message, the clean point.

THE DRAFT: deu_10_second_tablets 10:1-22 — 22 of 22 verses, missing 0 (computed from the DB\'s verse table), depends_on deu_09_not_righteousness and
exo_34_second_tablets (both frozen — asserted), 29 scenarios and 26 comment lines in the draft (typed from the dump\'s G print), the claim prefix DV10 absent from
every unit and manifest (computed). The chapter the unit, per the ruling CHAPTER NUMBERS; the portion Ekev runs on (7:12-11:25) — no edge inside the chapter.

THE TWO DIVISIONS AGREE: the export\'s chapter 10 twenty-two rows, the DB\'s twenty-two verses; the alignment instrument gives the identity at cost 14 (asserted;
chapter 5\'s 30-against-33 the book\'s one split); the store\'s token count equals the DB\'s at every verse (324 tokens, 1,252 letters); NO written/read pair in
the chapter (wtype None at all 324); the store\'s four "?" glosses are its split station name ("from-?" the Beeroth and "?" the bene of Beeroth-bene-jaakan at
10:6, one lemma over three tokens) and its "I" (10:10 "and-?", 10:13 "?").

THE SHELF, BY POSITION — THE SPINE IS SILENT ON THE CHAPTER (chapters 4, 7, 8 and 9 the form): no piska head in chapter 10 — 36 on 6:9 before, 37-38 on 11:10
and 39 on 11:11 after (the heads computed on the Hebrew\'s first rows; chapters 7-10 without a section — asserted). Its whole voice on the chapter is THREE rows
outside any piska, found by the union of both files\' citations (the two files agree — three rows, three hits each; no range form, no "ibid"): 32:1 on 6:5
(ACT FROM LOVE — the lover\'s reward doubled and redoubled; 10:20 "the LORD your God you shall fear and Him you shall serve" quoted as the FEARER\'S seat,
who abandons his fellow when needed; love and fear together in the All-Present alone), 301:4 on 26:5 (the first-fruits confession — "he went down to Egypt"
to sojourn, not to settle, not for a crown; "with few" — 10:22\'s "with seventy persons your fathers went down" quoted, and quoted PLENE: "your fathers" with
the vav the DB does not write), 311:5 on 32:8 (R. Eliezer son of R. Yose the Galilean: the borders of the peoples by the number of Israel — sixty queens and
eighty concubines are a hundred and forty nations against the seventy souls of 10:22, so "borders" (plural) gives each nation two shares; 10:22 quoted
DEFECTIVE here — the two rows spell the one verse two ways). Two of the three read before (32:1 at sitting 4 on the Shema\'s verse; 311:5 at the Babel
sitting by topic, credited at a second Genesis sitting) and REREAD WHOLE here; one fresh (301:4). Every first row carries its head citation (chapter 9 had
three without). No interpolation; none excluded (no cited verse beyond 22). The prior reads over the ledgers: seventeen ledgers NAME a verse of chapter 10
(the journeys ledger on 10:6-7 — Moserah, Bene-jaakan, Gudgodah, Jotbathah named from the itinerary; the priestly blessing ledger on 10:17 against
Numbers 6:26 — the face lifted and the face not lifted; the eighth day on 10:8; the second census on 10:22; the sanctuary block on 10:1 "make for
yourself an ark" against 25:10 "they shall make"; asserted), no ledger holds an Onkelos row of chapter 10.

THE INK, COMPUTED (ch10_dump0.py, ch10_measure1.py; the asserts typed from the print):
- THE PARSER MEASURED FIRST: FIVE number verses in 22 — the two tablets [2] at 10:1 and [2, 2] at 10:3 (the dual marked three times), the ten words [10]
  at 10:4 WITH THE ORDINAL [1] ("like the first writing" — the singular with the article, the parser\'s one ordinal in the chapter), the forty days and forty
  nights [40, 40] at 10:10 (the phrase\'s nine Bible seats — the fifth in the book), the seventy [70] at 10:22; "swear" (10:20, the lemma 7650) NOT a number —
  the seven-stem homograph as at 9:5; THE PLURAL "FIRST" (10:1, 10:3 "like the first ones", 10:2, 10:10 "the first ones") NO ORDINAL TO THE PARSER — the
  lemma 7223 five times in the chapter, read as a count once; NO GAP. The kin: Exodus 34:1 [2], 34:4 [2, 2], 34:28 [40, 40, 10], 34:29 [2], 25:10 and 37:1
  [2.5, 1.5, 1.5] (the ark\'s cubits), 31:18 [2], Deuteronomy 4:13 [10, 2], 5:22 [2], 9:17 [2, 2]; Numbers 33:38 [1] with the ordinals [40, 5] — AARON\'S DEATH
  DATED (the fortieth year, the fifth month, the first of the month), 33:39 [123] his age; Genesis 46:27 [2, 70], Exodus 1:5 [70]; 1 Kings 8:9 [2] the
  tablets in Solomon\'s ark; Numbers 3:39 [22000] the Levites counted.
- THE STORE = THE DB at every verse: no written/read pair; the DB\'s morphology gives 10:2\'s "you broke" the piel perfect second person (the form\'s two
  seats in the Torah — Exodus 34:1 and here), 10:6\'s "ministered as priest" the wayyiqtol of the piel (Numbers 3:4 the only other — Eleazar and Ithamar
  before Aaron), 10:8\'s "separated" the hiphil perfect (Numbers 16:9 the only other — Korah\'s "the God of Israel has separated you"), the station\'s
  three tokens one lemma with a plus-sign (the split name Beeroth-bene-jaakan).
- THE SPELLINGS OF "TABLETS" (the lemma 3871): לוחת ("tablets", plene) 10:1 alone in the chapter — the plene\'s three seats in the Bible are 9:9, 9:10 and
  10:1; לחת (defective) 10:3 — Exodus\'s form at every seat; הלחת ("the tablets", the article\'s form) five times, 10:2 twice, 10:3, 10:4, 10:5 (ten seats in
  the Bible); 1 Kings 8:9\'s second plene (לחות, 4:13\'s and 9:11\'s) absent here; ONE ARAMAIC SPELLING for all.
- THE KIN DIFFED (the DB\'s tokens, the shared tokens counted in order): 10:2 against Exodus 34:1 ELEVEN OF FOURTEEN — God\'s word quoted whole ("the words
  that were on the first tablets which you broke") WITH THE ARK\'S CLAUSE ADDED ("and you shall put them in the ark" — two tokens Exodus never gives); 10:1
  against 34:1 six — "hew for yourself two tablets of stone like the first" shared with ONE change inside it (the spelling of "tablets": plene here, defective
  there), and where Exodus continues "and I will write" the retelling has "and come up to Me on the mountain" (EXODUS 24:12\'S WORDS — the first ascent\'s
  call, the two seats of "come up to Me on the mountain", with the vav here and not there) "and make for yourself an ark of wood" — THE ARK INSERTED INTO
  GOD\'S QUOTED WORD; 10:3 against 34:4 four (the hewing; "an ark of acacia wood" 25:10\'s three tokens — the two seats — where 34:4 has "and Moses rose early
  in the morning"); 10:4 against 9:10 ten, 5:22 nine, Exodus 34:28 six ("and He wrote on the tablets … the ten words" — the two seats of the clause; "like
  the first writing" 10:4 alone, the noun\'s nine Bible seats, Exodus 32:16\'s "the writing was the writing of God" the kin) and 34:1 five; 10:5 against 9:15
  four ("and I turned and came down from the mountain" — the two seats) and 1 KINGS 8:9 four (Solomon\'s "nothing in the ark save the two tablets of stone
  which Moses put there at Horeb" — the ark\'s contents read back at the Temple); 10:6 against Numbers 33:31 ONE, 33:32 one, 33:38 one, 20:28 three — THE
  STATIONS IN ANOTHER ORDER AND ANOTHER FORM (Numbers: Moseroth → Bene-jaakan → Hor-haggidgad → Jotbathah, "they journeyed … and camped"; here: Beeroth-bene-
  jaakan → Moserah, Gudgodah → Jotbathah, "the children of Israel journeyed from … to"; Numbers puts Aaron\'s death at Mount Hor seven stations later —
  33:37-38 — the retelling puts it at Moserah: AN OPEN ROW for the compile); 10:7 against 33:32-34 NOTHING; 10:8 against 1 Chronicles 15:2 and 23:13 six
  ("to carry the ark … to minister to Him … forever" — David\'s and the Chronicler\'s readings of this verse) and 31:9 five; 10:9 against 18:2 eight, Joshua
  13:14 seven, 18:1 five ("the LORD is his inheritance" 10:9 and 18:2 the two seats; "portion or inheritance" six); 10:10 against 9:9, 9:11 and 9:19 six,
  9:18 five, Exodus 34:28 and 24:18 five; 10:11 against 31:7 and Joshua 1:6 seven (the charge to Joshua repeats the charge to Moses — "the land which I swore
  to their fathers to give them"), Exodus 33:1 and 1:8 five; 10:12 against 6:5, 11:22, 4:29 and Joshua 22:5 seven, Micah 6:8 and 11:13 five — "with all your
  heart and with all your soul" the Shema\'s seven tokens; 10:13 against 4:40 seven; 10:14 against Nehemiah 9:6 five and 1 Kings 8:27 four; 10:15 against 7:7
  six and 4:37 one; 10:16 against 30:6, Leviticus 26:41 and Jeremiah 4:4 ONE — the heart\'s foreskin in three other words at every kin; 10:17 against 7:9 five,
  16:19 four; 10:18 against Exodus 22:20-22 NOTHING — the orphan, the widow and the stranger in the attributes\' own words; 10:19 against Exodus 23:9 seven,
  Leviticus 19:34 six, Exodus 22:20 five ("for you were strangers in the land of Egypt" — the clause\'s FOUR seats, all four); 10:20 against 6:13 SEVEN OF EIGHT
  — 6:13\'s three clauses with a FOURTH ADDED ("and to Him you shall cleave") and the vav of "and Him" dropped; 10:21 against 7:19 four; 10:22 against 1:10
  four ("as the stars of heaven for multitude" — the book\'s three seats), 28:62 three, Genesis 46:27 two and Exodus 1:5 one (the seventy told in new words).
- THE PHRASE CENSUSES (the crowns): "at that time" fifteen in the book, 10:1 and 10:8 the chapter\'s two — THE LEVITES SEPARATED "AT THAT TIME" (which time
  the compile\'s question: the calf\'s or the second tablets\'); "hew for yourself" 10:1 and Exodus 34:1 alone; "an ark of wood" ONE, "an ark of acacia wood"
  10:3 and Exodus 25:10; "ark" the lemma forty-two seats in the Torah, EIGHT in the book (10:1, 2, 3, 5, 8; 31:9, 25, 26), Genesis 50:26\'s coffin among the
  forty-two; "the ark of the covenant of the LORD" 10:8, 31:9, 31:25, 31:26 in the Torah (Joshua\'s four), "the ark of the testimony" Exodus\'s seven in two
  spellings — THE BOOK NAMES THE ARK BY THE COVENANT, EXODUS BY THE TESTIMONY; "and I will write on the tablets" 10:2 alone (Exodus 34:1 "and I will write",
  34:28 "and He wrote"); "which you broke" 10:2 and Exodus 34:1; "and you shall put them in the ark" ONE; "the ten words" 10:4, 4:13, Exodus 34:28 — the
  Bible\'s three; "on the day of the assembly" 9:10, 10:4, 18:16; "and I turned and came down" 9:15, 10:5; "AS THE LORD COMMANDED ME" 10:5 and 4:5 in the
  Torah (the 1cs suffix\'s five Bible seats) — THE RECEIPT INSIDE THE NARRATIVE: the register gate\'s finder lists 10:5 declared NONE ("Deuteronomy is not on
  the tape") and 10:22\'s seventy beside it (asserted at the dump); "as the LORD your God spoke to him" 10:9 ONE (18:2, Joshua 13:14 "as He spoke to him" —
  Numbers 18:20\'s word the referent, the SECOND receipt form); "there Aaron died" ONE (Numbers 20:28 "and Aaron died there"); "and he was buried there"
  10:6 THE TORAH\'S ONE SEAT (Moses\' 34:6 "and He buried him"); "ministered as priest in his stead" ONE; "the LORD separated the tribe of Levi" ONE; "to carry
  the ark of the covenant of the LORD" 10:8 (31:25, Joshua, Chronicles); "to stand before the LORD to minister to Him" 10:8 (18:5, 1 Chronicles 23:13);
  "and to bless in His name" 10:8 and 1 Chronicles 23:13 (21:5 "in the name of the LORD"); "until this day" six in the book; "portion or inheritance" 10:9,
  12:12, 14:27, 14:29, 18:1 and Genesis 31:14 (Rachel and Leah\'s); "the LORD is his inheritance" 10:9, 18:2; "with his brothers" 10:9 alone in the book;
  "and I stood on the mountain" ONE (5:5 "I stood between the LORD and you"); "as the first days" 10:10 and Zechariah 8:11; "the LORD hearkened to me that
  time also" 9:19, 10:10; "THE LORD WAS NOT WILLING TO DESTROY YOU" ONE (4:31\'s "He will not destroy you"); "arise, go on the journey before the people" ONE —
  "journey" the noun\'s twelve Torah seats, the bare singular here and at Numbers 10:2 (the trumpets "for the journeying of the camps"); "let them go in and
  possess the land" ONE; "which I swore to their fathers to give them" ONE (the 1cs "I swore" eleven in the Torah); "and now, Israel" 4:1, 10:12; "what does the
  LORD your God ask of you" ONE — Micah 6:8\'s "what does the LORD require of you" five tokens shared; "ask" the participle 10:12 and 18:11 (the necromancer);
  "but only" (כי אם) seven in the book; "to fear the LORD your God" 10:12, 14:23 (the infinitive fourteen in the Bible); "to walk in all His ways" 10:12, 11:22,
  1 Kings 8:58; "to love" the infinitive eight in the book; "with all your heart and with all your soul" seven singular and two plural in the book, eleven in
  the Bible; "and with all your might" 6:5 and Josiah\'s 2 Kings 23:25 alone; "to keep the commandments of the LORD and His statutes" ONE; "which I command you
  today" eighteen singular, six plural; "for your good" 10:13 alone in the form (6:24 "for our good"); "behold, to the LORD your God" ONE — "behold" (הן) four
  in the book; "THE HEAVEN OF HEAVENS" 10:14, 1 Kings 8:27, 2 Chronicles 2:5, 6:18 (with the vav — the Temple\'s dedication and this chapter), Nehemiah 9:6,
  Psalm 148:4 — six; "the earth and all that is in it" ONE (Psalm 24:1 "the earth and its fullness", Exodus 19:5 "all the earth is Mine"); "delighted" 7:7,
  10:15 (the verb\'s four Torah seats — Shechem\'s and the captive\'s the others); "and He chose their seed after them" 10:15 (4:37 "his seed after him");
  "chose" thirty-one in the book; "as this day" six; "circumcise the foreskin of your heart" ONE — the foreskin\'s ten Torah seats, nine of them the flesh\'s;
  "circumcise" twenty-one in the Torah, the weqatal at 10:16, 30:6 (the LORD circumcises) and Exodus 12:44; "your neck you shall not stiffen any more" ONE —
  the hiphil twenty-one in the Bible, "you shall not stiffen" (the plural) 10:16, Psalm 95:8 (Meribah\'s), 2 Chronicles 30:8; "stiff-necked" six, all the
  calf\'s (9:6, 9:13); "GOD OF GODS AND LORD OF LORDS" 10:17 and Psalm 136:2-3 (the psalm\'s two verses on the one clause); "the great, the mighty and the
  awesome God" 10:17 — Nehemiah 9:32 whole, Jeremiah 32:18 and Nehemiah 1:5, Daniel 9:4 with one dropped (the Talmud\'s Yoma 69b on the dropping — the
  docket\'s); "the God" with the article Genesis 31:13, 46:3, Deuteronomy 7:9, 10:17 in the Torah; "who lifts no face" 10:17, 28:50 — Leviticus 19:15 "you shall
  not lift the face of the poor" and NUMBERS 6:26 "THE LORD LIFT HIS FACE TO YOU" the kin (the priestly blessing ledger\'s question); "nor takes a bribe" 10:17
  — 16:19 "you shall not take", Exodus 23:8 "a bribe you shall not take", 27:25 "who takes a bribe": the bribe\'s six Torah tokens; "who executes the judgment of
  the orphan and the widow" ONE — the pair eleven in the Torah, Exodus 22:21 the first ("widow and orphan"); "and loves the stranger" ONE, "and you shall love
  the stranger" ONE, "you shall love him as yourself" Leviticus 19:34, "your neighbor as yourself" 19:18 — "AND YOU SHALL LOVE" FIVE IN THE TORAH: the LORD
  (6:5, 11:1), the neighbor (19:18), the stranger (19:34, 10:19); "to give him bread and a garment" ONE (Jacob\'s vow "bread to eat and a garment to wear" the
  kin); "for you were strangers in the land of Egypt" Exodus 22:20, 23:9, Leviticus 19:34, 10:19 — FOUR; "stranger" twenty-two tokens in the book, twenty-one
  in Leviticus, twelve in Exodus, eleven in Numbers, two in Genesis; "love" twenty-two tokens in the book, four in this chapter; 10:20 AGAINST 6:13 — "fear",
  "serve", "swear by His name" the two seats, "and to Him you shall cleave" the fourth clause (the verb\'s seven book seats: 4:4, 11:22, 13:5, 13:18, 28:21,
  28:60, 30:20); "He is your praise" ONE — "praise" Exodus 15:11, 10:21, 26:19 in the Torah; "great and awesome things" — "the awesome" as a feminine plural
  participle with the article 10:21 the Bible\'s ONE seat; "which your eyes have seen" 4:9, 7:19, 10:21, 29:2 (Proverbs 25:7); "with seventy persons" ONE — Exodus
  1:5 "seventy persons" (the order reversed), Genesis 46:27 "seventy" alone; "seventy" forty-two seats in the Torah; "as the stars of heaven for multitude"
  1:10, 10:22, 28:62 — the book\'s three; "as the stars of heaven" seven (Abraham\'s 22:17, Isaac\'s 26:4, Moses\' 32:13, the Chronicler\'s 27:23); "went down to
  Egypt" 10:22 and 26:5; "placed you" the 3ms with the 2ms suffix 10:22 and Exodus 2:14 ("who made you a prince" — the Hebrew\'s taunt to Moses); the Name
  twenty-one bare tokens in fourteen verses; "the LORD your God" singular 9, 12, 20, 22 and PLURAL at 17 alone; "God" only at 10:17; MOSES NEVER NAMED — no
  "Moses" in chapters 6-11 of the book (1: three, 4: four, 5: one); Aaron and Eleazar at 10:6; Levi at 8-9; Israel at 6, 12.
- THE FRAMES AND THE REGISTER: ONE divine frame (10:11 "and the LORD said to me" — the command to journey) and God\'s word at 10:1-2 by "said" without the
  wayyiqtol; NO "saying"; THE NARRATIVE VERBS FOURTEEN in seven verses (10:3-6 the ark and the descent, 10:10 hearkened, 10:11 said, 10:15 chose — chapter 9
  had twenty-two in sixteen); the first person Moses\' at 1-5, 10, 13 and GOD\'S at 11 ("I swore"); THE SECOND PERSON SINGULAR in eleven verses — 1-2 God\'s "you"
  to Moses, 9-14 and 20-22 Israel\'s — PLURAL in four (4 "to you" at the assembly, 16 the heart\'s foreskin, 17 "your God", 19 "you were strangers"), BOTH in
  10:15 alone (the switch inside the verse: "your fathers … you (pl.) from all the peoples"), NEITHER in six (3, 5-8 the narrative, 18 the attributes); imperatives
  FOUR, all God\'s to Moses ("hew", "and come up" 10:1; "arise, go" 10:11); NO infinitive absolute; consecutive perfects FOUR — "and make" (10:1), "and you shall
  put them" (10:2), "and you shall circumcise" (10:16), "and you shall love" (10:19) — the law\'s form at the ark and at the heart; the imperfect second person at
  10:16 (THE CHAPTER\'S ONE PROHIBITION, "you shall not stiffen … any more", the plural) and 10:20\'s FOUR (fear, serve, cleave, swear — the law\'s form of 6:13);
  participles FIVE (10:12 "asks", 10:13 "commanding", 10:18 "executes", "loves", 10:21 "the awesome"); "for" at 12, 17, 19 with 10:12\'s "but only", no "if", no
  "lest", no "when"; "so that" NONE (the book\'s forty-three).
- ONKELOS (the renderings\' seats over the book, computed): NO MEMRA IN THE CHAPTER (the book\'s ten "His Memra" and twenty-four "the Memra of the LORD" all
  elsewhere); 10:1 "like the first ones" (the two seats 10:1, 10:3), "ascend to BEFORE Me" (the reverence at the ascent); 10:2 "which you smashed"; 10:5 "as He
  commanded me" (4:5 the kin); 10:6 the stations kept as names, "ministered"; 10:8 "the ark of the COVENANT (קימא) of the LORD" (31:9, 31:25 the kin — the
  Aramaic\'s one word for covenant, nineteen seats), "to stand before the LORD to serve Him"; 10:9 THE GIFTS SUPPLIED — "the gifts the LORD gave him, THEY are
  his inheritance" for "the LORD is his inheritance" (18:2 the same words; Numbers 18:20\'s Onkelos the source: "the gifts I gave you are your portion"); 10:10
  "the LORD ACCEPTED MY PRAYER" (9:19 the kin — the two seats), "was not willing to harm you"; 10:11 "arise, go"; 10:12 "what does the LORD your God DEMAND of
  you", "EXCEPT to fear BEFORE the LORD", "to walk in all the ways THAT ARE RIGHT BEFORE HIM" (the supplement\'s seven seats — 8:6, 10:12, 11:22, 19:9, 26:17,
  28:9, 30:16), "to serve BEFORE the LORD"; 10:14 "behold" (הא); 10:15 "desired", "took pleasure in their sons after them"; 10:16 THE FOOLISHNESS OF YOUR HEART
  for the foreskin (30:6 the same; Leviticus 26:41\'s "their foolish heart" the kin), the neck kept; 10:17 "GOD OF JUDGES AND LORD OF KINGS" for "God of gods
  and Lord of lords" (the two words\' other seats — "judges" 16:18, "kings" the blessing of Joseph), "there is not before Him the taking of faces, nor the
  accepting of a bribe"; 10:18 "the judgment of the orphan and the widow", "loves THE CONVERT to give him SUSTENANCE and CLOTHING"; 10:19 "love the convert,
  for DWELLERS you were in the land of Egypt" — THE TWO WORDS FOR THE STRANGER (the convert who joins, the dweller who sojourned — Exodus 22:20\'s and 23:9\'s
  Onkelos the same); 10:20 "fear", "serve BEFORE Him", "DRAW NEAR TO HIS FEAR" for "cleave to Him" (4:20, 11:22, 30:20 "His fear" the kin), "by His name
  ESTABLISH" for "swear" (6:13 the same); 10:21 "He is your praise"; 10:22 "seventy souls", "to multiply". The English\'s brackets FOURTEEN in eight verses (the
  gifts, the demand, the ways that are correct, the foolishness, the kings, the taking of faces, sustenance, shelter, the fear of Him); no parenthesis rows.
- THE DISPLAY LAYER (the patch): THIRTY-EIGHT rewrites BY GLOSS where the store\'s every token of the gloss is the one word ("like-first" → "like-the-first",
  "in-hand-me/my" → "in-my-hand", "like-thing-written" → "like-the-writing", "command-me/my" → "commanded-me", "Mosera" → "Moserah", "the-Gudgodah-suffix" →
  "to-Gudgodah", "Jotbath" → "Jotbathah", "and-officiate-as-a-priest" → "and-ministered-as-priest", "to-lift/carry" → "to-carry", "to-attend-as-a-menial-him/its"
  → "to-minister-to-Him", "inheritance-him/its" → "his-inheritance", "to-departure" → "to-journey", "lo!" → "behold", "prepuce" → "foreskin", "donation" →
  "bribe", "the-sojourner" → "the-stranger", "laudation-you/your" → "your-praise", "like-as/which" → "as", …) and EIGHTY-NINE BY REFERENCE where the family is
  mixed ("box" → "an-ark-of" at 10:1, 10:3 and "the-ark-of" at 10:8 — Joseph\'s coffin and Noah\'s ark in the family; "the-sovereign" → "the-lords" — the socket
  in the family; "smoothness" → "portion"; "scion" → "the-tribe-of"; "cling" → "delighted-in"; "impinge" → "you-shall-cleave"; "be-dense" → "stiffen"; "from-?"
  → "from-Beeroth", "?" → "bene", "Beeroth-of-the-children-of-J" → "jaakan"; "die" → "died"; "and-inter" (already "and-bury") → "and-he-was-buried"; "very-widely-
  used-as-a-relati" → "but", "as-demonstrative" → "only"; "the-fear" → "the-awesome-things"; "food" → "bread"; "living-being" → "persons"; …); TWENTY-THREE of the
  chapter\'s glosses ALREADY rewritten by the earlier sittings ("tablets", "the-tablets", "the-assembly", "break", "be-willing", "destroy-you", "ask", "only",
  "your-soul", "for-good", "to-give", "for-multitude", "the-God", …); the anchors sitting 7\'s last rows ("obstinacy" the by-gloss block\'s, "Deut.9.5:18" the
  by-ref block\'s).

THE CLAIMS PLANNED (write_ch10_manifest.py): SIX — DV10-01 10:1-5 THE SECOND TABLETS AND THE ARK (God\'s word of Exodus 34:1 quoted with the ark inserted;
"come up to Me on the mountain" Exodus 24:12\'s; the ark of acacia wood made BEFORE the ascent; the ten words written "like the first writing"; the tablets
put in the ark "as the LORD commanded me" — the receipt); DV10-02 10:6-9 THE STATIONS, AARON\'S DEATH, THE LEVITES (Beeroth-bene-jaakan to Moserah, Gudgodah
to Jotbathah — the itinerary\'s names in another order; Aaron died and was buried there, Eleazar in his stead; the tribe of Levi separated to carry the ark, to
stand, to minister, to bless in His name; no portion, the LORD his inheritance "as He spoke to him"); DV10-03 10:10-11 THE THIRD FORTY AND THE COMMAND TO GO
(the forty days as the first, the LORD hearkened that time also, not willing to destroy; arise, go before the people — the sworn land); DV10-04 10:12-16 WHAT
THE LORD ASKS (and now, Israel — to fear, to walk in all His ways, to love, to serve with all the heart and soul, to keep — for your good; the heaven of
heavens His, only your fathers He desired and chose their seed; circumcise the heart\'s foreskin, stiffen the neck no more); DV10-05 10:17-22 THE GOD OF GODS
(the great, mighty and awesome God who lifts no face and takes no bribe; the orphan\'s and the widow\'s judgment; the stranger loved with bread and a garment —
love the stranger, for you were strangers; fear, serve, cleave, swear; He is your praise; seventy souls to the stars); DV10-06 THE RETELLING ON THE TAPE —
the readback\'s rows OWED to the compile (8b): 10:1-5 against the second tablets\' lines (Exodus 34:1-4, 28-29) and the ark\'s (25:10-16, 37:1-9, 40:20 — THE
FRAGMENTS IN THE ARK: no line on the tape, the design question already owed from 7b); 10:6-7 against the itinerary\'s lines (Numbers 33:30-39) and Aaron\'s
death (20:22-29 — the retelling\'s station against the tape\'s Mount Hor, an OPEN row); 10:8-9 against the Levites\' lines (Numbers 3, 8, 18 — "at that time");
10:10 THE THIRD FORTY against the clock (the second ascent to 10 Tishri — 7b\'s third stretch, owed); 10:11 against Exodus 32:34 and 33:1; 10:12-22 the laws
restated (6:5, 6:13; Exodus 22:20-23, 23:8-9; Leviticus 19:33-34 — the laws\' form by CALL); the receipt at 10:5 and the second receipt form at 10:9. Seated as
six WITNESS_READ operators at 10:1, 10:5 (the receipt — the tape\'s seat), 10:6, 10:10, 10:12, 10:17; step E.

OWED TO THE COMPILE (sitting 8b; the box in COMPILE_DEBT.md at the records): THE FRAGMENTS IN THE ARK (10:1-5 — the ark made before the ascent and the tablets
put in it: Bava Batra 14a-b and Menachot 99a-b on the tablets and the broken tablets in the ark; the tape\'s ark line at Exodus 25 / 37 / 40:20 measured at
the design — THE SHELF\'S TWO ARKS, Bezalel\'s and this one); THE RECEIPT SEATS 10:5 "as the LORD commanded me" and 10:9 "as the LORD your God spoke to him"
(the register gate lists 10:5 declared NONE — its disposition the compile\'s); THE STATIONS AND AARON\'S DEATH (10:6-7 against Numbers 33:30-39 and 20:22-29 —
the order and the place; Seder Olam 9\'s walk; the OPEN row); "AT THAT TIME" THE LEVITES SEPARATED (10:8 — the calf\'s time, Numbers 8\'s line on the tape;
Exodus 32:26-29\'s "fill your hand" the kin); THE THIRD FORTY\'S END (10:10 — 10 Tishri on the clock, 7b\'s arithmetic; Seder Olam 6; Ta\'anit 30b); "WHAT DOES
THE LORD ASK" (10:12 — Berakhot 33b "is the fear of heaven a small thing?", Menachot 43b the hundred blessings from "what" read "a hundred", Shabbat 31b);
THE ATTRIBUTES (10:17 — Yoma 69b the men of the great assembly restoring what Jeremiah and Daniel dropped; Berakhot 33b the one who adds; Megillah 25a; the
face lifted against Numbers 6:26 — Berakhot 20b, Niddah 70b, the Sifrei on Numbers 42:2, the blessing ledger\'s three reconciliations); THE BRIBE (10:17 —
Ketubot 105a-b; 16:19 the law\'s seat); THE ORPHAN, THE WIDOW, THE STRANGER (10:18-19 — Bava Metzia 59b the stranger\'s thirty-six warnings; Yevamot 47a-b
the convert; Exodus 22:20-23 and Leviticus 19:33-34 the laws on the tape); THE FOUR CLAUSES (10:20 — Sotah 14a walking in His ways, Ketubot 111b cleaving,
Shevuot 35b swearing by the Name, Temurah 3b-4a; 6:13\'s cell by CALL); THE SEVENTY AND THE STARS (10:22 — Bava Batra 123a-b Jochebed the seventieth; the
Joseph runner\'s cell by CALL; the register\'s 10:22 seat); THE CHECKPOINT SERIES continues (DA the open series). THE TESTING SHELF routed to 8b\'s docket:
Bava Batra 14a-b, Menachot 99a-b, Berakhot 8b (the ark), Berakhot 33b, Menachot 43b, Shabbat 31b (the demand), Yoma 69b, Megillah 25a, Berakhot 20b, Niddah 70b
(the attributes), Ketubot 105a-b (the bribe), Bava Metzia 59b, Yevamot 47a-b (the stranger), Sotah 14a, Ketubot 111b, Shevuot 35b, Temurah 3b-4a (the four
clauses), Bava Batra 123a-b (the seventy), Rosh Hashanah 3a and Ta\'anit 9a (Aaron\'s death), Mishnah Shekalim 6:1-2, Mishnah Sotah 7:6, Mishnah Berakhot 9:5.

THE ORDER (the rest of the one run): the twenty-two Onkelos rows and the three outside rows WHOLE (read at the dump; ch10_onkelos.txt, ch10_sifrei_outside.txt)
→ ch10_rows_onkelos_a.py (10:1-11), ch10_rows_onkelos_b.py (10:12-22), ch10_rows_outside.py (sitting 7\'s forms; the cuts by consonants — HP / AP / SP_) →
write_ch10_ledger.py (from write_ch9_ledger.py) → lint 0, coverage computed (Onkelos 22; the Sifrei 3; the kin\'s credits by name — the Exodus ledgers\' rows on
the second tablets, the ark and its making, the Numbers ledgers\' rows on the stations, Aaron\'s death, the Levites\' separation and their portion, the Exodus
and Leviticus ledgers\' rows on the stranger) → ch10_patch_overrides.py (38 by gloss, 89 by reference; the anchors sitting 7\'s last rows), the ink rerun
PATCHED → write_ch10_manifest.py (six claims DV10-01..06) → seat_ch10.py (six WITNESS_READ at 10:1, 5, 6, 10, 12, 17; step E) → ch10_chain.sh (the seat,
verify_text, the ritual) → ch10_fold.sh (224 / 2227 / the hash unmoved) → build_world → the journal gate → the register gate --strict → large_letter_probes →
the home-path gate → the records from the sheet in one call → the forms copied → the commit message → the clean point.
'''
s = s.rstrip('\n') + '\n\n\n' + D
open(P, 'w', encoding='utf-8').write(s)
print('the design appended:', len(D.encode()), 'bytes; the map', len(s.encode()))
