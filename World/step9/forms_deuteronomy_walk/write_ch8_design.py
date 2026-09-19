#!/usr/bin/env python3
import os as _os, subprocess as _sp
_ROOT = _sp.check_output(['git', 'rev-parse', '--show-toplevel'], text=True).strip()   # the scratch form: ROOT from git, never typed
# THE DEUTERONOMY WALK sitting 6 — CHAPTER 8 (2026-09-18; the owner: "Go" after 5b's commit and the two-run rule): THE DESIGN appended to the map after the
# measurements and the ink, before a row is typed. The guard names THE SITTING (5b's lesson: a guard that matches another sitting's string is no guard).
P = _ROOT + '/World/step9/DEUTERONOMY_WALK.md'
s = open(P, encoding='utf-8').read()
HDR = '## Sitting 6 — CHAPTER 8, Deuteronomy 8:1-20 (2026-09-18; the owner: "Go" after 5b\'s commit 29c189b and THE TWO-RUN RULE): the reading and the unit — THE DESIGN, written after the measurements and the ink, before a row is typed; ONE RUN (a reading sitting under the two-run rule)'
assert HDR not in s and '## Sitting 6 — CHAPTER 8' not in s
D = HDR + '''

THE ONE RUN: the rereads (the recovery page, the map's "RUN 3 — AS RUN" and the 5b AS BUILT, the memory; THE_STEPS' compiler block, Step 2 and Step 5's head — this
window), the measurements (ch8_dump0.py DERIVED from ch7_dump0.py by twenty-one asserted substitutions; ch8_measure1.py chapter 8's own, 170 KB of print read whole), the ink
(ch8_ink.py — every fact an assert run by assert_driver.py: FOUR fell on the first pass, all forms and none facts, 0 on the second) and this design; then the rows — the
sixteen outside rows WHOLE (ch8_sifrei_outside.txt, 42 KB, read at the dump) and the twenty Onkelos rows WHOLE (ch8_onkelos.txt) — ch8_rows_onkelos_a/b.py and
ch8_rows_outside.py on sitting 5's forms, write_ch8_ledger.py from write_ch7_ledger.py (lint 0; coverage computed); the display layer's patch (32 by gloss, 20 by reference), the
manifest (six claims), the seat, the chain (the ritual), the fold predicted and matched, build_world, the journal gate, the register gate --strict, the home-path gate; the
records from the sheet in one call (write_ch8_records.py from write_ch7_records.py), the forms copied, this section's AS BUILT, the commit message for the owner's word.

THE DRAFT: deu_08_manna_humility 8:1-20 — 20 of 20 verses, missing 0 (computed from the DB's verse table), depends_on deu_07_nations_cherem and exo_16_manna_shabbat, 27
scenarios, 24 comment lines, no operators, no step E; the next draft deu_09_not_righteousness opens at 9:1 (9:1-29; depends_on this unit and the calf's). THE CHAPTER THE UNIT;
no portion edge inside it (Ekev runs 7:12-11:25). ONE ledger: logic/oral_triage/deu_08_ekev_2026-09-18.md; the claims' prefix DV08 (absent everywhere, asserted).

THE TWO DIVISIONS AGREE: the export's chapter 8 twenty rows, the DB's twenty verses; the alignment instrument gives the identity at cost 25; chapter 5 the book's ONE split
(asserted on all thirty-four).

THE SHELF, BY POSITION — THE SPINE IS SILENT ON THE CHAPTER (chapters 4 and 7 the form): no piska heads in chapter 8 — 36 on 6:9 before, 37 on 11:10 after; but the Sifrei's
Ekev piskaot on 11:10-12 QUOTE THE CHAPTER'S PRAISE OF THE LAND back at it, and its other piskaot quote the chapter's sentences as proof-texts: SIXTEEN OUTSIDE ROWS by the
union of both files' citations (the Hebrew's book-named form found fifteen citations on twelve rows; the English's "(Dt.8:n" twenty-six on fifteen rows; the union sixteen):
19:2 on 1:20 (the tutor's parable — forty years Moses said "a good land … brooks of water" (8:7), at the Land "you have come"); 32:10, 32:12, 32:15 on 6:5 (the discipline —
R. Meir: you know your deeds and the chastisements, the latter not as the deeds; R. Nathan b. R. Joseph: a covenant cut for chastisements as for the Land — 8:5 then 8:7; the
Land — whence? 8:5-7); 37:5 on 11:10 (R. Shimon b. Yohai: "the world" is the Land, spiced with everything — "you shall lack nothing" 8:9); 39:4, 39:6, 39:8 on 11:11 (twelve
lands for twelve tribes, 8:7-10's "land" clauses counted among them; the Land drinks rain, irrigation, snow and dew — "a land of brooks of water" 8:7); 40:10 on 11:12 (the
blessing in the house as in the field — even in eating and satisfaction, 8:10; even in the belly, Exodus 23:25); 43:7 on 11:15-16 (a person rebels only out of satiety —
8:12-14, 31:20, the calf); 48:8 on 11:22 (forget the first and the last go — "if you surely forget" 8:19; "a day you leave Me, two I leave you"); 48:10 on 11:22 ("not by bread
alone" = midrash, "all that proceeds" = the laws and the homilies — 8:3); 53:1 on 11:26 (the two paths — the righteous suffer two or three days, "to do you good in your end"
8:16); 297:4 on 26:2 (the first fruits from the seven species for which the Land is praised — 8:8 the list); 313:15 on 32:10 (the great and terrible wilderness = the four
kingdoms, 8:15); 318:1 on 32:15 (Jeshurun grew fat — out of satiety they rebel: the Flood, the Tower, Sodom, the calf, and Israel in the Land, 8:12-14; the copyist's
abridgement marked in both files). FIVE READ BEFORE (19:2 at sitting 1; 32:10, 32:12, 32:15 at chapter 6; 318:1 as a dup row at a Genesis sitting) — every one REREAD WHOLE here
(the whole-row rule; the credit guard's quick look made a full look). THE RANGE CITATIONS the Hebrew regex does not read — "(דברים ח ה-ז)" ("Deuteronomy 8:5-7") at 32:15, "ח ז-י"
at 39:4, "ח יב-יג" at 43:7 — found through the English and asserted by string (a slip this way would be a row missed, not a row invented); the English's 53:1 form "(be'akharitecha;
Dt.8:16)" found through the Hebrew. THE ONE DIVISION DIFFERENCE: the English's 39:6 runs on through the Hebrew's 39:6, 39:7 and 39:8 — the citation of 8:7 sits in the Hebrew's
39:8 and the English's 39:6; both rows read whole, each file's own row counted (chapter 6's lesson: the two files compared row by row). No interpolation, no slip (no cited verse
beyond 20). 297 strict Sifrei rows anywhere before this ledger. NO Onkelos row of chapter 8 in any ledger. THE KIN'S SPINE READ ALREADY, CREDITED BY NAME at the ledger: the manna
and the craving (Numbers 11:4-9 — six Onkelos rows), the forty years (14:33-34 — two), Meribah (20:1-13 — thirteen), the serpents (21:4-9 — six); the Exodus manna and the rock at
Horeb (16:1-36, 17:1-7) never read through Onkelos — the Mekhilta's eight rows over the ledgers. Five ledgers NAME a verse of chapter 8 (the grace after meals from 8:10 at 1b's
exam; 8:2 at chapter 6; 8:8 and 8:15 at the Numbers 20 and 21 ledgers; 8:8 at the offerings-calendar exam).

THE INK, COMPUTED (ch8_dump0.py, ch8_measure1.py; the asserts typed from the print — FOUR fell on the first pass, all forms: a vowel letter typed for a vowel mark, a shared block
that was two blocks, a phrase list that had folded two calls, a census sum missing two forms; each retyped from the print, none after):
- THE PARSER MEASURED FIRST: TWO number verses in 20 — 8:2 and 8:4 "THESE FORTY YEARS" [40] (2:7 the same phrase; the wilderness's forty years at Exodus 16:35, Numbers 14:33-34,
  32:13, 29:4, Joshua 5:6, Nehemiah 9:21, Psalm 95:10, Amos 2:10 — [40] at every seat; "forty years" thirty-one seats over the Bible); THE SEVEN-STEM HOMOGRAPH "AND YOU SHALL BE
  SATISFIED" (8:10, 8:12 — the lemma 7646) STARRED, as at 6:11, 11:15, 31:20; "swore" (8:1, 8:18) not a number; no ordinal; NO GAP. The tokens 293, the letters 1,148.
- THE STORE = THE DB at every verse but 8:2: the store carries the written מצותו ("His commandments", no yod) AND the read מצותיו (with the yod) — THE CHAPTER'S ONE WRITTEN/READ
  PAIR, 7:9's and 5:10's kin (the token's five Bible seats: 5:10, 7:9, 8:2, 27:10, Numbers 15:31; the DB's 1,268 written-marked tokens); no large letter; the two unglossed
  tokens "I" (8:1, 8:11).
- THE KIN DIFFED (the DB's tokens): 8:1 against 4:1, 11:8 ("all the commandment which I command you this day" — six tokens shared), 30:16; 8:2 against 29:4 ("forty years in the
  wilderness"), 2:7, 13:4 and Exodus 16:4 — THE MANNA'S OWN TEST-CLAUSE "whether … or not" shared at the verse's end (the two tokens); 8:3 against Exodus 16:15, 31, 35 and
  Numbers 11:6-9 ("for they did not know" shared with 16:15), 8:16 (the doublet), 13:7, Leviticus 18:5 ("man shall live"); 8:4 against 29:4 ("did not wear out" — the singular
  garment here, the plural there) and Nehemiah 9:21 (the only other "did not swell"); 8:5 against 1:31 ("as a man … his son" — carried there, disciplined here: the two seats),
  4:36, 11:2, Proverbs 3:11-12; 8:6 against 10:12, 28:9, 30:16 ("walk in His ways"); 8:7 against 11:10-12, Exodus 3:8, 10:7 (Jotbah's "brooks of water"); 8:8 against 2 Kings
  18:32 (the Rabshakeh's "a land of olive oil and honey"), 7:13, 11:14, Numbers 13:23, 20:5, Haggai 2:19; 8:9 against 2:7 ("you lacked nothing"), 33:25; 8:10 against 6:11-12,
  11:15, 31:20, 14:29; 8:11 against 6:12 (SIX tokens shared — "take heed to yourself lest you forget the LORD"), 4:9, 12:13, 15:9, 7:11, 11:1, 30:16 (the triad's other orders);
  8:12 against 6:10-11, 28:30; 8:13 against 17:16-17 — THE KING'S LAW: "silver and gold he shall NOT multiply" against "silver and gold SHALL multiply for you", the same tokens;
  8:14 against 17:20 (the king's heart not lifted), 6:12, 5:6, 13:6, 13:11 (SEVEN tokens shared — the exodus formula whole), Hosea 13:6; 8:15 against 1:19, Numbers 21:6-8,
  20:5-11, Exodus 17:6, Psalm 114:8, 32:13; 8:16 against Exodus 16:35 (nothing shared — the retelling's own words); 8:17 against 7:17, 9:4 (the three "say in your heart"),
  Judges 7:2, Isaiah 10:13; 8:18 against 7:8, 7:12, 9:5, 4:31, Genesis 26:3, 17:7; 8:19 against 4:26 and 30:18 ("that you shall surely perish" shared), 6:14, 11:16, 4:19,
  the ten words; 8:20 against 4:26, 7:12, 7:22-24, 9:3-4, 28:45, 62, Genesis 22:18, 26:5 (the heel), Exodus 15:26, 19:5.
- THE PHRASE CENSUSES (the crowns): "all the commandment" eight, all this book's; "which I command you this day" eighteen; "that you may live" five with the nun at 5:33, 8:1
  alone; "and go in and possess" 4:1, 8:1, 11:8; "and you shall remember" nine (the slave five); "these forty years" three; "to humble you" the verb's seven Deuteronomy seats
  (three this chapter's; the four others the seduced, the ravished, the Egyptians' affliction); "to test you" the lemma's fifteen Torah seats; "WHETHER … OR NOT" the verse-ending
  pair at seven seats — 8:2 and Exodus 16:4 the manna's; THE INTERROGATIVE HE ON A VERB the book's ONE (8:2); "the manna" thirteen; "nor did your fathers know" 8:3, 8:16 alone; THE
  PARAGOGIC NUN eight in the chapter (the book's densest after 4); "NOT BY BREAD ALONE" ONE; "all that proceeds from the mouth of the LORD" ONE; "man shall live" 8:3 and
  Ecclesiastes; "the mouth of the LORD" twenty-five Torah seats; "did not swell" the verb's TWO Bible seats; "as a man disciplines his son" ONE; "discipline" eight Torah; "to walk
  in His ways" three; "and to fear Him" ONE; "a good land" twelve; "brooks of water" three; "springs and deeps" ONE — "deeps" in the Torah here and the Song of the Sea; THE SEVEN
  SPECIES — 8:8 ALONE holds all seven lemmas in the Bible (three or more at five seats: Numbers 20:5, Haggai 2:19, Joel 1:12, Habakkuk 3:17, Jeremiah 41:8); "milk" absent — HONEY
  WITHOUT MILK; "in poverty" ONE; "you shall not lack anything" ONE; "iron" eight, "copper" three; "hew" three Torah; "EAT, BE SATISFIED, BLESS" ONE — the Torah's ONE command to
  bless the LORD; "eat and be satisfied" six; "take heed to yourself lest" nine; "lest you forget the LORD" two; "forget" fourteen in the book — 8:19's INFINITIVE ABSOLUTE the
  lemma's one such form in the Bible; "His commandments, His judgments and His statutes" ONE in this order (the triads seventeen verses over the Bible, no two in one order but
  5:31, 6:1, 7:11's); "good houses you build and dwell" ONE; "silver and gold" seven Torah (8:13 and 17:17 the pair); "multiply" twenty in the book, three at 8:13; "and your
  heart be lifted up" ONE (17:20 the king's; Hosea 13:6 the chapter's sequence in the prophet's mouth); "the house of bondage" twelve; "the great and terrible" 1:19 and 8:15
  the wilderness; "fiery serpent" 8:15 and Numbers 21:6, 8; "scorpion" six; "flint" five; "the rock" — Exodus' tzur, Numbers' sela: 8:15 the tzur; "to do you good in your end"
  ONE; "end" ten Torah; "and you say in your heart" 8:17 and Isaiah 49:21; "my power and the might of my hand" ONE; "to get wealth" seven; "that He may establish His covenant"
  ONE (twenty-three "establish … covenant" seats); "as at this day" six in the book; "if you surely forget" ONE; "after other gods" sixteen; "other gods" seventeen in the book;
  "serve … and bow" the pair ten Torah seats — serve-then-bow at 8:19, 11:16, 17:3, 29:25; bow-then-serve at 4:19, 30:17 and the ten words; "I testify against you this day"
  ONE (the verb's ten Torah seats); "that you shall surely perish" 4:26, 8:19, 30:18 — the infinitive absolute at those three alone; "like the nations … so shall you perish"
  ONE — the measure-for-measure form; "BECAUSE" THE HEEL fifteen over the Bible, five in the Torah; "hearken to the voice of the LORD your God" ten in the book, 8:20 the ONE plural.
- THE FRAMES AND THE REGISTER: NO divine frame, NO "saying" — Moses' voice throughout; the narrative verbs THREE, all God's past acts at 8:3 (humbled, let hunger, fed); ONE
  IMPERATIVE — "take heed" (8:11, the niphal; nine such in the book); TWO INFINITIVE ABSOLUTES, both at 8:19; the law's form the consecutive perfect in ten verses; the
  PROHIBITION FORM twice and neither a command (8:9 "you shall not lack" a promise, 8:20 "you would not hear" a report) — the chapter's negatives are the past (8:3, 8:4, 8:16);
  the second person SINGULAR in sixteen verses, PLURAL in one (8:20), BOTH in two (8:1 the frame, 8:19 "I testify against YOU"), NEITHER in 8:8 (the seven species — no verb);
  THE ARTICLE + PARTICIPLE CHAIN "who brought you out … who led you … who brought out water … who fed you … who gives you power" (8:14-18, five); the first person Moses' (8:1,
  8:11 "I command", 8:19 "I testify") and the boaster's (8:17 "my power, my hand, for me"), no "we"; "for/that" six, "if" two (8:2 the question's tail, 8:19 the case), "lest" two
  (8:11, 8:12) — no "when", no "or"; "so that" six (the book's forty-three); the Name thirteen; "the LORD your God" nine singular and ONE plural (8:20); Moses and Israel never
  named; Egypt at 8:14 alone; the fathers at 8:1, 3, 16, 18.
- ONKELOS (the renderings' seats over the book, computed): 8:1 "swore" MADE "ESTABLISHED" (as at 7:8 — twenty-two seats); 8:3 THE MEMRA — "not by bread alone is man SUSTAINED, but
  by everything that PROCEEDS FROM THE WORD OF THE LORD is man sustained" (the sustaining verb five seats; "the Memra of the LORD" twenty-four over the book — 8:3 and 8:20 the
  chapter's two); "the manna" named at 1:1's Di-zahab too (three seats); 8:4 "your foot did not swell" MADE "YOUR SHOES DID NOT GO BARE" (the shoe-word 8:4, 29:4); 8:5
  "disciplines" MADE "TEACHES" (4:1's word); 8:6 "in His ways" MADE "in the ways that are RIGHT BEFORE HIM" (five seats); 8:7 "flowing brooks", "fountains of springs" (one each);
  8:8 the seven species PLURAL, "a land whose olives make oil and which makes honey" (the English's brackets); 8:9 "in straits" (one); 8:11, 8:14, 8:19 THE FEAR SUPPLIED — "lest
  you forget THE FEAR OF the LORD your God" at the chapter's three forgettings (the fear-word twelve seats over the book); 8:12 "BEAUTIFUL houses" (one); 8:15 "A PLACE OF
  serpents, burning ones and scorpions", "a house of thirst" (8:15, 32:10), "THE MIGHTY ROCK" for the flint; 8:17 "wealth" MADE "POSSESSIONS" (8:17, 8:18, 32:15 Jeshurun's);
  8:18 THE COUNSEL — "He gives you COUNSEL to acquire possessions" (power made counsel; two seats); 8:19 "other gods" MADE "the IDOLS of the peoples" (eighteen), "I testify"
  (4:26, 8:19, 30:19), "surely perish" (4:26, 8:19, 30:18); 8:20 "because" MADE "IN EXCHANGE FOR" (eight — 7:12's), "hearken to the voice" MADE "ACCEPT THE MEMRA" (five in this
  form, thirteen with "to the Memra"); no parenthesised variant in the chapter's Hebrew rows; the English's sixteen brackets over seven verses, eight at 8:15; "mon" kept twice.
- THE DISPLAY LAYER (the patch): THIRTY-TWO rewrites BY GLOSS ("and-mark" → "and-remember", "the-whatness" → "the-manna", "whatness" → "manna", "to-separation-him" → "alone",
  "going-forth" → "what-proceeds-from", "fail" → "wore-out", "perhaps-to-swell-up" → "swelled", "in-split" → "in-the-valley", "in-indigence" → "in-poverty", "the-set" →
  "who-gives", "and-mislay" → "and-forget", "the-bring-forth-you" → "who-brought-you-out", "the-go-you" → "who-led-you", "burning" → "fiery-serpent", "from-cliff" →
  "from-the-rock", "the-eat-you" → "who-fed-you", "in-last-you" → "in-your-end", "vigor-me" → "my-power", "and-depress" → "and-bow-down", "duplicate" → "testify",
  "wander-away" → "perish", "like-nation" → "like-the-nations", the two suffix families "know" and "hear" …) and TWENTY BY REFERENCE ("I" at 8:1 and 8:11; "led-you";
  "will-you-keep" for the interrogative; "springs" for "eye"; "and-deeps"; "flowing-out"; "you-shall-hew" for "cut"; "gave" for "set"; "and-be-lifted-up"; "bondage" for
  "servant"; "who-brought-out"; "the-wealth" and "wealth" for "force"; "power" for "vigor"; "to-establish" for "arise"; "because" for "heel" at 8:20; "makes-perish" …);
  ELEVEN of the chapter's families already rewritten at sittings 1-5 and left standing ("in-the-wilderness", "and-be-satisfied", "forget", "so-as-not", "and-the-terrible",
  "after", "other", "you-shall-perish", "keep", "you-may-live", "multiply").

THE CLAIMS PLANNED (write_ch8_manifest.py): SIX — DV08-01 8:1 the frame (all the commandment; live, multiply, go in, possess; the land sworn); DV08-02 8:2-6 the way of forty
years (remember; the humbling, the testing, the heart; the manna, not by bread alone; the garment and the foot; the discipline of a son; keep, walk, fear); DV08-03 8:7-10 the
good land (brooks, springs and deeps; the seven species; iron and copper; eat, be satisfied, bless); DV08-04 8:11-14 take heed lest you forget (the commandments, judgments,
statutes; the houses, the herds, the silver and gold; the heart lifted; who brought you out); DV08-05 8:15-18 the chain and the covenant (who led you through the serpents
and the thirst, who brought water from the flint, who fed you manna, to do you good in your end; "my power and the might of my hand"; He gives the power, to establish the
covenant sworn); DV08-06 8:19-20 the testimony (if you surely forget and serve other gods: I testify today, you shall surely perish, like the nations, because you would not
hear) — each check the block's longest store-piece whole (8:2's "His commandments" NOT a check — the store's two tokens). THE FOLD PREDICTED: units 222, standing 2209 + 6 =
2215, hash unmoved (the tripwire's literals set before the bake). THE SEATS: six WITNESS_READ operators at 8:1, 2, 7, 11, 15, 19, step E. THE REGISTER GATE: no seat in the
chapter (no receipt form; "which I command you" the giving) — GREEN unchanged (DECLARED 100). THE LEDGER PREDICTED: Onkelos 20 rows; the Sifrei 16 outside rows, all read whole
here (five named as reread — sitting 1's, chapter 6's, a Genesis sitting's); the kin's rows CREDITED by name (the Numbers 11, 14, 20 and 21 ledgers; the Mekhilta's eight rows);
coverage COMPUTED at the writing.

OWED TO THE COMPILE (sitting 6b; the box in COMPILE_DEBT.md at the records): THE BLESSING AFTER THE MEAL (8:10 — the Torah's one command to bless: Berakhot 48b (the grace's
blessings from the verse), 20b-21a (the Torah obligation), 49b and Mishnah Berakhot 7:2 (the measure of "satisfied"), 35a (the blessing before, an inference); Mishnah Berakhot
6-7 whole by topic); THE SEVEN SPECIES (8:8 — Berakhot 41a-b the order of blessings by the verse's order and its two "land"s; 44a the after-blessing; Mishnah Berakhot 6:4;
Bikkurim 1:3, 1:10 the first fruits (the Sifrei 297:4); Menachot 84b CREDITED at the offerings-calendar exam); THE MANNA AND THE HUMBLING (8:2-3, 8:16 — Yoma 74b-76a: "afflicted
you and let you hunger", the manna's forms; the readback rows against the tape's manna lines by kind — Exodus 16 exodus_story by CALL); THE FORTY YEARS (8:2, 8:4 — the clothes
not wearing out and the feet not swelling: a state over forty years with no earlier line — the readback's SUPPLIED grade on a state, not an act: the design decision of 6b);
THE DISCIPLINE (8:5 — Berakhot 5a's afflictions of love; the Sifrei 32:10-15 CREDITED here); "TAKE HEED LEST" (8:11 — Makkot 13b / Eruvin 96a: "take heed, lest, do not" a
negative command — the rule's exhibit; the cell forgetting_barred?); THE HEART LIFTED UP (8:14 — Sotah 4b-5a arrogance as idolatry; 17:20 the king's law by CALL at chapter 17);
THE EXODUS FORMULA (8:14 — brought_out 12:51 by kind, the readback), THE SERPENTS AND THE ROCK (8:15 — Numbers 21:6-9 and 20:8-11, Exodus 17:6 by the tape's lines and by CALL
into chukat and exodus_story), THE MANNA (8:16); "MY POWER AND THE MIGHT OF MY HAND" (8:17 — a DATA row; the Sifrei 48:10's "not by bread alone" reading); THE COVENANT
ESTABLISHED (8:18 — the oath's lines by kind, as 7:8); THE TESTIMONY (8:19-20 — 4:26's line by kind (obey_horeb's cell by CALL), the perishing "like the nations" a DATA row,
the heel's second seat 7:12's cell by CALL; "other gods" the second word's cell by CALL); the docket by the union rule (the scan will name the tractates; the topic ranges
expected: Berakhot 20b-21a, 35a-b, 41a-44a, 48b-49b; Mishnah Berakhot 6-7; Bikkurim 1; Yoma 74b-76a; Sotah 4b-5a; Makkot 13b; Eruvin 96a; Berakhot 5a). NOTHING ELSE IN
CHAPTER 8 IS OWED TO A LATER SITTING OF ITS OWN.

⚠ LESSONS (so far): THE SPINE'S SILENCE IS NOT THE SHELF'S — sixteen outside rows quote chapter 8 from the Ekev piskaot on 11:10-12 (the Land's praise) and from eight other
piskaot: a chapter without a section is a chapter the shelf cites. A RANGE CITATION IS INVISIBLE TO THE CITATION REGEX — "(דברים ח ה-ז)" ("Deuteronomy 8:5-7") at three rows; the
union of both files found them through the English, and the Hebrew's range is asserted by string. THE TWO FILES DIVIDE A PISKA'S ROWS DIFFERENTLY (39:6-8) — each file's own
row carries the citation, both rows read whole, neither counted twice. A CONSONANTAL ASSERT NEVER TYPES A POINTING — the shelf's bytes stripped to consonants before the compare
(HB0); the one form that fell typed a vowel letter for a vowel mark. THE FIRST TYPED PASS FELL FOUR WAYS ON FORMS — the print first, then the assert. THE CREDIT GUARD MADE FULL —
five rows read before were reread whole (the whole-row rule leaves the quick look nothing to save).

THE ORDER (the rest of the one run): the twenty Onkelos rows and the sixteen outside rows WHOLE (read at the dump; ch8_onkelos.txt, ch8_sifrei_outside.txt) → ch8_rows_onkelos_a.py
(8:1-10), ch8_rows_onkelos_b.py (8:11-20), ch8_rows_outside.py (sitting 5's forms; the cuts by consonants — HP / AP / SP_) → write_ch8_ledger.py (from write_ch7_ledger.py) → lint 0,
coverage computed (Onkelos 20; the Sifrei 16; the kin's credits by name) → ch8_patch_overrides.py (32 by gloss, 20 by reference; the anchors sitting 5's last rows), the ink rerun
PATCHED → write_ch8_manifest.py (six claims DV08-01..06) → seat_ch8.py (six WITNESS_READ at 8:1, 2, 7, 11, 15, 19; step E) → ch8_chain.sh (the seat, verify_text, the ritual) →
ch8_fold.sh (222 / 2215 / the hash unmoved) → build_world → the journal gate → the register gate --strict → the home-path gate → the records from the sheet in one call → the forms
copied → the commit message → the clean point.
'''
s = s.rstrip('\n') + '\n\n\n' + D
open(P, 'w', encoding='utf-8').write(s)
print('the design appended:', len(D.encode()), 'bytes; the map', len(s.encode()))
