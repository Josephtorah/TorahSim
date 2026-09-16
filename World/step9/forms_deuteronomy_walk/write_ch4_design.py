import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE DEUTERONOMY WALK sitting 2b — THE COMPILE OF CHAPTER 4 (2026-09-16): THE DESIGN appended to World/step9/DEUTERONOMY_WALK.md BEFORE any code
# (the compile shape's second step; the whole text built here, the file opened once to write). Lint asserted at the map's baseline (0).
import subprocess, os, re
ROOT = _ROOT
P = f'{ROOT}/World/step9/DEUTERONOMY_WALK.md'
old = open(P, encoding='utf-8').read()
assert '## Sitting 2b — THE COMPILE OF CHAPTER 4' not in old
TEXT = r'''

## Sitting 2b — THE COMPILE OF CHAPTER 4, Deuteronomy 4:1-49 (the design, 2026-09-16; the owner: "ok get ready to compact. then we finish 4" — the
## word for the compile given before the compaction; written after the rereads and the measurements — ch4_compile_recon.py, ch4_docket_scan.py in the
## scratchpad, the 1b forms reread — and BEFORE any code; the compile shape of the recovery file's section 5 with "Sitting 1b" as the form on this book)

THE MEASUREMENTS (what the tape and the callees say before a line is typed): THE COUNTER stands at (40, 11, 1), the speech's day — chapter 4 continues
the first speech and carries no date; NO CLOCK COST this sitting (no forward marker; the retrograde markers below are dated points, the counter unmoved).
EVERY ACT THE CHAPTER RETELLS IS ON THE TAPE BUT ONE PAIR: Baal-peor (Num 25:3 israel_yoked_to_baal_peor, 25:5 judges_commanded_to_slay, 25:9 the dead
counted; plague_struck CLOSED at 25:8 by the spear with 25:9's count in the close), the bar (Num 20:12 sentence_at_meribah — barred_from_the_land on Moses
OPEN; 1:37 and 3:26 the retellings on the tape since 1b), the exodus (Exod 12:29 the plague, 12:51 brought_out, 13:21 pillar_set, 14:21-31 the sea),
the creation (Gen 1:31's marker "the sixth day — Adam created (1:27)", the era life:the_human; Gen 2:7 formed_from_dust), Horeb's assembly (Exod 19:16
thunder_and_horn at the giving's marker (1, 3, 7) by Rabbi Yose, 19:18-20 lord_descended, 19:20 moses_went_up; 24:18 moses_ascended "forty days —
the tablets at 31:18"; 32:19 tablets_broken at (1, 4, 17)), the two kings (Num 21:24-25 sihon_smitten_land_possessed, 21:35 og_smitten; the speech's own
lines 1:4, 2:36, 3:8, 3:17 since 1b), the refuge law (Num 35:9-34 refuge_law_given — the debit appoint_six_cities_of_refuge on Israel OPEN BY DESIGN),
the dispossession (Num 33:50-56 dispossession_commanded — the debit OPEN). THE ONE PAIR MISSING: THE TAPE HAS NO LINE FOR THE SPEAKING OF THE TEN WORDS
(Exodus 20:1 — "and God spoke all these words") NOR FOR THE GIVING OF THE FIRST TABLETS (31:18 — "and He gave to Moses, when He finished speaking with
him, two tablets of the testimony"): the tape runs from Exod 19:20 (moses_went_up, the third ascent) to Exod 24:1 (elders_ascended); the decalogue runner
(span Exod 20:1-17; law_decalogue given_at 20:1, installed_by covenant_blood_thrown) compiled the Decalogue's LAW LAYER (vain_name, sabbath_clauses,
theft_commandment; altar_rules) and wrote no narrative line; the erection runner (span including 31:18; its tablets cell with the effect
tablets_delivered in the registry) folded the tablets into the ascent's line at W7 ("the tablets at 31:18" inside moses_ascended's source) and wrote no
line at 31:18 — THE READBACK'S FIRST FINDING ON THIS CHAPTER: a first telling on the ink with no line on the tape. THE DECALOGUE'S SECOND WORD (Exodus
20:3-6 — no other gods, no graven image, no bowing) HAS NO CELL in any runner: the image law 4:16-19 restates is UNCOMPILED — an OWED edge, a
COMPILE_DEBT line (its natural seat chapter 5's sitting, where the Decalogue is restated). THE REGISTER GATE on chapter 4: Deut 4:5 NONE ("the book not
read"; the receipt "as the LORD my God commanded me") and Deut 4:45 the FOOTER, DAEMONS 1 (law_opening_speech@Deut 1:16 inside (Deut 1:1, Deut 4:45]);
THE GATE'S CLASS PREDICTED FROM ITS CODE (lesson viii): a receipt is ACT when a ledger write's source CONTAINS its verse — the exhortation's line
(4:1-8) contains 4:5 → ACT, declared with the compile's why; 4:45's block gains this sitting's daemon → DAEMONS 2. THE GLOBAL COUNTS grepped before the
tape run: CP6 (markers 161, F 126 — MOVES: 161 → 163, R 20 → 22), CA1 (the Deuteronomy markers' list — its retrograde list gains two entries: RETYPED as
of this sitting), CV2 / CX2 / CW3 / CR3 (commanded on Israel — UNMOVED: no debit this sitting), CT2 / CT4 / CT6 (the pending timers — UNMOVED: no clock
walk), CT9 / CV9 / CX9 / CY9 / CZ9 / CW9 / CR9 / CA9 (entities 319, closes 126 — UNMOVED); I5 63 → 64; the register probes' tallies (receipts 69 with
CLOSE 16; footers EMPTY 3) UNMOVED (4:5 NONE → ACT inside the same 69). THE CHECKPOINT PREFIX CC measured FREE (CC, CI, CO, CQ, CU free in the sequence
file and in every probe file). THE DOCKET SIZED — 68 link rows in 26 works (Avodah Zarah 9, Sanhedrin 8, Berakhot 5, Makkot 5, Gittin 4; the verses
cited most 4:9 nine, 4:7 six, 4:32 six, 4:44 five, 4:5 five, 4:16 five, 4:24 five) + 259 topic rows (Mishnah Avodah Zarah 3:1-3, Makkot 2:4-8, Pesachim
10:4, Rosh Hashanah 2:8-9; Rosh Hashanah 28b whole 25, Eruvin 95b-96a 36, Sanhedrin 88b-89a 42, Kiddushin 30a 15, Rosh Hashanah 24a-24b 34, Avodah
Zarah 55a 12, Ketubot 111b 23, Makkot 9b-10a 43, Berakhot 32b 31) = 327 rows, 98 credited (the opening speech's docket 50, the refuge docket 48, the
Decalogue's block 18): FOUR verdict parts on disk. THE CHAPTER'S OWN INK (the reading's asserts, reused): four number verses (4:13 [10, 2], 4:41 [3],
4:42 [1], 4:47 [2]), no ordinal; ONE divine frame (4:12); ONE LAW (4:2, no case token) and ONE CASE (4:25 "when you beget sons"); the second person
switching number by verse; the imperatives hear (4:1), see (4:5), take heed (4:9, 4:23), assemble (4:10), ask (4:32); the prohibitions add / diminish
(4:2), lest you forget (4:9, 4:23), lest you corrupt (4:16), lest you lift your eyes (4:19); Moses named at 41, 44, 45, 46 only; the retellings diffed
token by token at the reading (ch4_measure1_b.out section A) — the deltas this compile RECOMPUTES.

THE NAME: cold_run_obey_horeb.py — the 59th runner; law_obey_horeb the 64th daemon (given_at Deut 4:2, installed_by BOOT with the class NAMED — a law in
Moses' voice with no divine frame: "the word which I command you", the vows' class); the span [[Deut, 4, 1, 49]]; the checkpoints CC1-CC9; the units
deu_04_obey_horeb and deu_04_refuge_east the frozen reading.

THE READBACK ON CHAPTER 4 (the first form's (R1)-(R6) applied a second time; the laws' half still owed to chapter 5):
(R1) THE ROWS — the DATA table the_readback, one row per retold act, the tape's kind and first verse, the ledger entry presupposed, THE GRADE, the delta
RECOMPUTED from the DB: 4:3-4 Baal-peor SHORTENED (twenty tokens for 25:3-9's telling; "the LORD destroyed from your midst every man who followed" =
25:5's slaying and 25:9's twenty-four thousand; "you who cleave are alive" the plague's close read; israel_yoked_to_baal_peor Num 25:3); 4:10-11 the day
at Horeb EXPANDED (lord_descended Exod 19:18; "under the mountain" 19:17's phrase; the mountain burning to the heart of heaven, darkness, cloud, thick
darkness — 19:18's smoke told larger); 4:12 the voice and no form SUPPLIED (Exod 20:1 the first telling — THE TAPE'S HOLE: (R3) below); 4:13 the ten
words and the tablets SUPPLIED (Exod 20:1-17 and 31:18 — the hole's second line); 4:20 the iron furnace EXPANDED (brought_out Exod 12:51; the furnace
1 Kings 8:51 and Jeremiah 11:4 outside the Torah); 4:21-22 the bar DISAGREES (sentence_at_meribah Num 20:12 — THE THIRD TELLING: "the LORD was angry
with me on your account and SWORE that I should not cross the Jordan" — the oath supplied, the ground "on your account" against 20:12's "because you did
not believe": the 1b row 1:37 WIDENED by a telling, OPEN — (R4)); 4:32 the creation SHORTENED (the sixth day's marker at Gen 1:31, "Adam created (1:27)";
formed_from_dust Gen 2:7 — a time-reference clause for the creation's telling); 4:34 the instruments EXPANDED (brought_out Exod 12:51 — the seven: trials,
signs, wonders, war, a mighty hand, an outstretched arm, great terrors; 26:8's four and 7:19's five FORWARD); 4:37-38 the choice and the outbringing
EXPANDED (brought_out; "because he loved your fathers" — Genesis 15:18's land by REFERENCE; "to dispossess nations greater than you" — the dispossess
debit of Num 33:50-56 OPEN, READ); 4:44-45 the second frame EXPANDED (speech_opened Deut 1:1 — "the testimonies, the statutes and the judgments" for
"the words"; "when they came out of Egypt" the era's stamp, no day: (R6)); 4:46-49 the two kings and the borders SHORTENED (sihon_smitten_land_possessed
Num 21:24, og_smitten 21:35 — and the speech's own lines 1:4, 2:36, 3:8, 3:17 quoted in their own clauses: the retelling of a retelling; Mount Sion the
fourth name for Hermon). ELEVEN rows: SHORTENED 3, EXPANDED 5, SUPPLIED 2, DISAGREES 1 — the census typed from the runner's print.
(R2) EVERY ROW'S ENTRY FOUND on the running world by kind and first verse (CC4: rows n = found n); the state the chapter asserts read off the ledger:
yoked_to_baal_peor ONE, the plague CLOSED with the count, Moses barred OPEN, brought_out ONE, the human's marker, the dispossess debit OPEN.
(R3) THE TWO SUPPLIED LINES — THE TAPE'S HOLE WRITTEN ONCE, AT ITS OWN TIME, BY THIS RUNNER (the form of 1:6's departure from Horeb): ten_words_declared
(speech, Deut 4:10-13; Exodus 20:1-17 the first telling) at the RETROGRADE marker Deut 4:10 dated M['giving'] = (1, 3, 7) — "the day you stood before
the LORD your God at Horeb" (4:10) the ink's own dating word, the day the tape already gives the assembly (Exod 19:16's marker, the seventh of Sivan by
Rabbi Yose — Shabbat 86b:5, the calendar row sinai_days) — writing covenant_declared on Israel (a STATUS, the value the ten words on two tablets: 4:13
"he declared to you his covenant which he commanded you to do, the ten words"); tablets_given (act, Deut 4:13; Exodus 31:18 the first telling) at the
RETROGRADE marker Deut 4:13 dated M['breaking'] = (1, 4, 17) — the fortieth day of 24:18's forty (the erection's own cell: Taanit 28b:9-10, the seventh
of Sivan plus forty = the seventeenth of Tammuz, "he came down and broke the tablets" — the tablets GIVEN and BROKEN on one day, 32:15 "Moses turned and
went down with the two tablets"), writing tablets_delivered on Moses (the erection's registered effect at its FIRST tape seat — the transfer 31:18's own
words describe). WHY THIS RUNNER AND NOT THE DECALOGUE'S OR THE ERECTION'S: the two first tellings sit in compiled spans whose runners chose no line
(the Decalogue treated as the law's giving, the tablets folded into the ascent at W7) — the readback found the silence; R3's form writes the act once at
its own time from the retelling's seat, as 1:6-8 wrote the departure from Horeb; the debit form is absent here (no command to close). FILED to the second
pass (D2): whether law_decalogue's installed_by should turn from covenant_blood_thrown (24:8) to ten_words_declared (20:1) — the installing act now on
the tape. FILED as the readback's finding: THE DECALOGUE'S SECOND WORD IS UNCOMPILED (no cell) — chapter 5's sitting.
(R4) THE DISAGREEMENT WIDENED: 4:21-22 the bar's third telling — the ground "on your account" (1:37's "for your sakes", 3:26's "was wroth for your sakes")
against Numbers 20:12's "because you did not believe in Me", and an OATH the tape never wrote ("and swore that I should not cross the Jordan"): graded
DISAGREES, an OPEN row beside 1:37's; the tape's one entry stands, no oath written (an oath told only in the retelling of a sentence the tape carries is
the sentence read back, not a second act — the reading's crown; Psalm 106:32 outside the Torah, read, not run).
(R5) THE RECEIPT IN MOSES' OWN VOICE (4:5 "as the LORD my God commanded me") IS THE TEACHING'S RUN — the command Exodus 24:12's "the torah and the
commandment which I have written TO TEACH THEM" (the erection's tablets cell, torah_mitzvah, by CALL) and 4:14's own "the LORD commanded me at that time
to teach you statutes and judgments"; the exhortation's line (4:1-8) is the write whose source holds 4:5 → the register class ACT, declared with this why
(Bekhorot 29a:7-8 — "as I taught you for free, so you teach for free": the exam's row); 10:5 the pair FORWARD.
(R6) THE FRAME IS THE BOOK'S ONE ACT OF ITS OWN DAY — AT ITS SECOND SEAT TOO: 4:44-49 ("this is the Torah which Moses set before the children of Israel;
these are the testimonies, statutes and judgments which Moses spoke … when they came out of Egypt") is the SECOND SPEECH'S HEAD (5:1 "and Moses called
all Israel" follows), a stamp of place and era without a day: NO WRITE, a reference row EXPANDED against speech_opened (Deut 1:1-5); torah_expounded's
status stands; the footer 4:45 closes the block (Deut 1:1, Deut 4:45] — DAEMONS 2 (law_opening_speech@Deut 1:16, law_obey_horeb@Deut 4:2).

THE DESIGN'S DECISIONS (the box's (a)-(l) settled on the measurements):
(a) THE ONE LAW — 4:2 "you shall not add to the word which I command you, nor diminish from it": THE TAPE LINE add_nothing_commanded (speech, Deut
4:1-8 — the exhortation whole, the law inside it) page_order at the counter's day (40, 11, 1) → adding_barred on Israel (a NEW BLOCK effect: "you shall
not add … nor diminish" — 4:2 the plural's one seat; 13:1 the singular's, FORWARD; Exodus 5:8's bricks, Numbers 27:4 and 36:3-4's daughters the
diminish-root's kin, computed at the reading); THE CELL'S ASKS the exam's rows — the priest who adds a blessing (Rosh Hashanah 28b:10 — R. Shemen bar
Abba's objection: "you shall not add" on the fourth blessing), the one who sleeps in the sukkah on the eighth day (28b:8-9 — bal tosif needs its time:
"not in its time" needs intent, Rava; Rabbah), R. Akiva's tefillin at night and on the Sabbath (Eruvin 95b-96a — "from days to days" the time of
tefillin; the sleeper), the rebellious elder ruling a fifth compartment (Sanhedrin 88b-89a — Mishnah Sanhedrin 11:2-3: "the tefillin four compartments —
five" the elder's transgression by the scribes' word), a fifth species and a fifth fringe (the Sifrei 82:5 on 13:1 — the shelf's exhibit, credited by
name), THE VERDICTS accepted (the rule holds against him) / exempt (outside the rule — not in its time; for study); the daemon law_obey_horeb given_at
4:2; the second seat 13:1 the chapter-13 sitting's (the same block, the same effect read).
(b) THE ONE CASE — 4:25-31 "when you beget sons and sons' sons and grow old in the land and corrupt yourselves … I call heaven and earth to witness
against you this day": THE TAPE LINE witnesses_called (speech, Deut 4:25-31) page_order at (40, 11, 1) → heaven_and_earth_witness on Israel (a NEW STATUS
effect: 4:26 "I call heaven and earth to witness against you this day" — the Sifrei 306:1's chain: the third of eleven; 30:19 and 31:28 FORWARD, 30:19's
first seven words identical); THE ARMS AS DATA the_exile_case, no clock item — corrupt → "you shall surely perish quickly … not prolong days … the LORD
will scatter you among the peoples … few in number … serve gods the work of men's hands, wood and stone" (the tochacha's effects scattered_among_nations
and covenant_remembered by CALL — Leviticus 26:33, 26:42 the first tellings; 28:36, 28:64 FORWARD; no exile on the tape, no entry written); seek →
"you will seek the LORD from there and find him, if you seek with all your heart and all your soul" (the Shema's words, 6:5 FORWARD; 30:10's kin);
return → "in your distress, when all these things find you in the end of days, you will return to the LORD and hearken … for the LORD your God is a
merciful God; he will not fail you nor destroy you nor forget the covenant of your fathers which he swore" (30:2's kin; Exodus 34:6's attribute; the
fathers' oath Genesis 22:16, 26:3 by REFERENCE); "in the end of days" A PROPHECY, NO TIMER; THE EXAM'S ROWS Gittin 88a:15-17 (Rav Huna: "and grow old"
by its letters eight hundred and fifty-two, the exile hastened by two years; R. Ammi: the seven dynasties — DATA), Sanhedrin 38a:6 (Ulla: the
righteousness of hastening), Megillah 31b:2 (4:25-40 the Ninth of Av's reading), Berakhot 32b:30 (4:9, 4:15 — the pious man praying on the road: "only
take heed to yourself, and keep your soul" the officer's verse; the exam's row on the guarding clause).
(c) THE RECEIPT'S SEAT PAID — Deut 4:5 NONE → ACT, declared from the tape with (R5)'s why (the exhortation's write contains the verse; the teaching's
run of Exodus 24:12's command; Bekhorot 29a:7-8; Nedarim 37a:2, 38a:5 — the Torah taught for free from this verse and 4:14); Deut 4:45 DAEMONS (no
declaration, the class GREEN) with daemons 2.
(d) THE THREE CITIES — 4:41-43 "then Moses set apart three cities beyond the Jordan toward the sunrise": THE TAPE LINE three_cities_set_apart (act,
Deut 4:41-43 — Moses' own act in the third person, "then" plus the imperfect: the Song's form, the six Torah seats computed at the reading) page_order at
(40, 11, 1) → cities_set_apart on Israel (a NEW STATUS effect valued the three — Bezer in the wilderness in the plain for the Reubenite, Ramoth in Gilead
for the Gadite, Golan in Bashan for the Manassite; the names the refuge runner's DATA row the_six_cities by CALL, computed by seat; Joshua 20:8's
"Gaulon" the reading's crown). THE REFUGE DEBIT STAYS OPEN — THE DEPARTURE FROM THE OWED LIST'S "CLOSED HERE", DECIDED ON THE ANSWER SHEET'S OWN ROW:
Mishnah Makkot 2:4 (with Makkot 9b:14) — "until the three in the land of Canaan were selected, the three beyond the Jordan did not admit", "six cities of
refuge SHALL THEY BE" (Numbers 35:13): the command is ONE appointment of six, Moses' three its first half — a mitzva that came his way (R. Simlai,
Makkot 10a:15-16), no manslayer admitted; the debit appoint_six_cities_of_refuge on Israel READ OPEN (CC8), its close Joshua 20:7-8's, OUTSIDE THE
TORAH, THE READBACK'S when the Prophets are walked; 4:42's manslayer "who slays his neighbor unawares and hated him not in time past" = 19:4's words with
"slays" for "smites" (computed; Numbers 35:11's "unwittingly"; the refuge runner's the_manslayer cells not_his_enemy and without_seeing by CALL; the
murder-verb PLENE at 4:42 — the refuge runner's own assert); the docket's OUTSIDE rows of 1b (Makkot 9b:18, 10a:9-16) and the refuge docket's rows on
the chapter CREDITED; Makkot 10a:14 (Reuben first — R. Tanchum bar Chanilai: he saved Joseph), 10a:9 ("and live" — the teacher exiled, his school with
him; 10a:11 the juxtaposition "this is the Torah" after the cities), Gittin 12a:11 (the slave exiled), Sotah 49a:4 the exam's rows.
(e) THE READBACK ROWS — (R1) above: eleven rows, the two supplied lines, the one disagreement widened.
(f) THE TWO FRAMES' DAY — (R6) above: NO WRITE at 4:44-49; the footer's block DAEMONS 2; the chapter's daemon inside (Deut 1:1, Deut 4:45].
(g) THE NO-IMAGE LIST AS DATA the_no_image_list — 4:16-19's forms: a graven image, the form of any figure, the likeness of male or female, of any beast on
the earth, of any winged bird that flies in the heavens, of anything that creeps on the ground, of any fish in the waters under the earth; the sun, the
moon, the stars, all the host of heaven — THE SECOND WORD'S PARAMETER TABLE (Exodus 20:4's "any likeness of what is in the heavens above or on the earth
beneath or in the waters under the earth" restated in seven kinds; the likeness-word five times in 16-18, computed at the reading); THE POINTER TO
EXODUS 20:4 DISPOSITIONED: the edge obey_horeb → decalogue OWED — the Decalogue's second word has no cell (cold_run_decalogue.py wraps vain_name,
sabbath_clauses, theft_commandment; altar_rules by the ordinances): a COMPILE_DEBT line for chapter 5's sitting (the Decalogue restated; the laws'
readback opens); the shelf's rows read as DATA — Mishnah Avodah Zarah 3:1-3 (the statues; a hand or a foot; a sun, a moon or a dragon on vessels — cast
into the Dead Sea) with Rosh Hashanah 24a-24b (Rabban Gamliel's moon forms on the tablet — "you shall not make with Me" Exodus 20:20; the forms of the
servants, the forms of the lights; for study, permitted), Chullin 23a:3 / Avodah Zarah 23b:9 / Bekhorot 57a:12 / Temurah 28b:17 / Sanhedrin 57a:1
("corruption" = idolatry from 4:16, licentiousness from the flood's generation), Chullin 139b:17 (the birds of 4:17).
(h) THE HOST "APPORTIONED" — 4:19 "which the LORD your God apportioned to all the peoples under the whole heaven" with 29:25 "which he had not
apportioned to them" (the Sifrei 148:8's pair on 17:3; Avodah Zarah 55a:9 — Rav Yehuda to Rava bar Rav Yitzchak: the host allotted them for their
delusion; Megillah 9b:1 — the Septuagint's "to give light" added for Ptolemy); Onkelos "prepared": A DATA NOTE the_host_apportioned, no link of our own
(no teacher joins 4:19's allotment to 29:25's withholding but the Sifrei's own pair — recorded as its row, a REFERENCE the Sifrei names).
(i) THE CHAPTER-5 DIVISION — the export's thirty verses against the DB's thirty-three: the recorder and the stitcher address by the DB; the next reading's
FIRST measurement (a DATA note the_export_chapter_5, nothing built).
(j) THE STORE'S GLOSS FAMILIES — the mixed families a display sitting's, filed unchanged.
(k) THE DOCKET by the union rule — 327 rows in FOUR parts A-D on disk (the 68 link rows; the topic rows: bal tosif's three ranges, Kiddushin 30a, the
images' Mishnah with Rosh Hashanah 24a-24b, Avodah Zarah 55a, Ketubot 111b, Makkot 2:4-8 with 9b-10a, Pesachim 10:4, Berakhot 32b), LAW / DERIVATION /
DISPUTE / CONTEXT / OUTSIDE, the crowns expected — bal tosif's time (Rosh Hashanah 28b; Eruvin 96a); the elder's fifth compartment (Sanhedrin 88b);
the grandfather's duty and "as if from Sinai" (Kiddushin 30a); the seminal-emission decree from 4:9-10's juxtaposition (Berakhot 21b-22a); the
forgetter's prohibition (Menachot 99b:3; Avot 3:8); the free teaching (Bekhorot 29a; Nedarim 37a); the images for study (Rosh Hashanah 24a-b); the host
allotted (Avodah Zarah 55a); "corruption" (Chullin 23a); the cleaving to scholars (Ketubot 111b); the limits of inquiry and Adam's height (Chagigah 11b-12a;
Sanhedrin 38b); "none else — even sorcery" (Chullin 7b; Sanhedrin 67b); the kingship verses (Rosh Hashanah 32b); the exile hastened (Gittin 88a;
Sanhedrin 38a); the Ninth of Av's reading (Megillah 31b); the community never sealed (Rosh Hashanah 18a; Yevamot 105a); the teacher exiled with his
school (Makkot 10a); Reuben first (Makkot 10a:14); "this is the Torah — a drug of life" (Yoma 72b); the nations' plea (Avodah Zarah 2b); the tefillin's
compartments (Berakhot 6a); the Haggadah's exposition (Pesachim 10:4); the gates of prayer (Berakhot 32b).
(l) THE MEKHILTA'S QUESTION on Exodus 20:22 (4:36 "from heaven he made you hear his voice … and on earth he showed you his great fire") — the reading
shelf's, credited by name only; the decalogue runner's altar_rules cell (20:22-26, wrapped by the ordinances) by CALL for the seat.

THE CELLS (six, each returning out(verdict, effects); the INK block exec'd from the sequence file; the token probes zero-report; every seat list and slice
typed from the reading's print and the recon): F1 the_exhortation (4:1-8 — asks: hear_and_do (4:1 the imperative "hear"; "that you may live and go in and
possess"), add_nothing (4:2 — THE LAW; the exam's rows (a)), diminish_nothing (4:2 — the root's seats), baal_peor_seen (4:3 — SHORTENED; BK.peor by CALL:
plague_count, peor_service, judges_count), the_cleaving (4:4 — Onkelos "the fear of" supplied; Ketubot 111b:6; Sanhedrin 64a:11 the cord and the dates;
Sanhedrin 90b:13; the Sifrei 49:2), taught_as_commanded (4:5 — THE RECEIPT, (R5); ER.tablets by CALL: torah_mitzvah), wisdom_before_the_peoples (4:6 —
Shabbat 75a:4 the seasons' reckoning; Avodah Zarah 4b:16), god_so_near (4:7 — Berakhot 6a:24 the compartments; Megillah 11a:9; Rosh Hashanah 18a:10 and
Yevamot 105a:17 the community's sentence; Sanhedrin 38b:15 the heretics' verse), righteous_statutes (4:8), the_write (adding_barred)); F2 horeb_retold
(4:9-14 — asks: take_heed_lest_you_forget (4:9 — Menachot 99b:3 and Avot 3:8 the forgetter's prohibition; Shevuot 36a:20 the self-curse's warning;
Berakhot 21b:8-22a:4 and Moed Katan 15a:18 the juxtaposition; Kiddushin 30a:5-7 the grandfather), the_day_at_horeb (4:10 — the assembly's day (1, 3, 7)
by the sinai_days row, Rabbi Yose; ES.sinai by CALL), learn_and_teach (4:10's two "they shall learn / teach" — one consonantal word, qal and piel by the
pointing alone — the reading's crown; the store's one gloss), the_mountain_burning (4:11 — EXPANDED against Exod 19:17-18, the diff recomputed),
the_voice_and_no_form (4:12, 4:15 — SUPPLIED: ten_words_declared dated (1, 3, 7); the tape's hole), the_ten_words_and_the_tablets (4:13 — "the ten
words" three seats, ER.tablets('ten_words') by CALL; the tablets PLENE at 4:13 — the erection's c_tablets_forms by CALL, the reading's crown; SUPPLIED:
tablets_given dated (1, 4, 17) — ER.ascent('seventeenth_tammuz') by CALL), commanded_to_teach (4:14 — Sanhedrin 21b:25; Nedarim 37a:2; Tosefta
Sanhedrin 4:5; Exodus 24:12's "to teach them")); F3 no_image (4:15-24 — asks: no_form_seen (4:15), the_image_list (4:16-18 — DATA (g); the OWED edge),
the_host_apportioned (4:19 — DATA (h)), the_iron_furnace (4:20 — brought_out READ BACK; PR.pieces('furnace') by CALL — Genesis 15:17's smoking furnace
the word's first seat; 1 Kings 8:51 and Jeremiah 11:4 outside), the_bar_third_telling (4:21-22 — DISAGREES (R4); OS.the_plea('the_refusal') and
OS.the_spies_read_back('the_bars_ground') by CALL), the_covenant_not_forgotten (4:23), consuming_fire_jealous_god (4:24 — the Sifrei 49:2; Avodah Zarah
54b:18 and 55a:2 the philosopher's and Agrippas's questions to Rabban Gamliel; Ketubot 111b:6; Nedarim 62b:3; Sotah 14a:3 walking after the attributes;
Exodus 20:5's "jealous God" by REFERENCE — the second word again)); F4 the_exile_case (4:25-31 — asks: the_case_head (4:25 — the case token; Gittin
88a:15-17; Sanhedrin 38a:6), the_witnesses (4:26 — the write heaven_and_earth_witness; the Sifrei 306:1's eleven), perish_and_scatter (4:26-27 — TC by
CALL: scattered_among_nations; Megillah 31b:2), serve_wood_and_stone (4:28 — 28:36, 28:64 FORWARD; Psalm 115:5 the kin), seek_and_find (4:29 — the
Shema's words), in_your_distress_return (4:30 — "the end of days" a prophecy; TC.recovery by CALL: covenant_remembered), the_merciful_god (4:31 —
Exodus 34:6 by REFERENCE; the fathers' oath)); F5 the_one_god (4:32-40 — asks: the_former_days (4:32 — Chagigah 11b:21-24 and Tosefta Chagigah 2:3 the
limits of inquiry; Chagigah 12a:2 and Sanhedrin 38b:7 Adam's height; PS.creation by CALL — Genesis 1:27's "created", the book's one seat), the_voice_and_lived
(4:33 — 5:26's kin; lord_descended by reference), the_nation_from_a_nation (4:34 — the seven instruments DATA; Berakhot 6a:24; Megillah 11a:9; the
Sifrei 301:21; Mishnah Pesachim 10:4; ES.plagues('ten') and ES.sea('ten_at_sea') by CALL — the instruments' first tellings), you_were_shown (4:35 —
Sanhedrin 67b:7 and Chullin 7b:14 "none else — even sorcery"; Rosh Hashanah 32b:17), from_heaven_the_voice (4:36 — Exodus 20:22 by CALL to DC.altar_rules'
seat; the Mekhilta credited by name), because_he_loved_your_fathers (4:37 — 10:15's kin; PR.call('land_seats') by CALL; Onkelos "with his Memra"),
to_dispossess_nations (4:38 — the dispossess debit OPEN read, JO by CALL; 9:1's kin), know_this_day (4:39 — the creed's second seat; Gittin 57b:17 the
seventh son; Rosh Hashanah 32b:17; Rahab's and Solomon's outside), keep_the_statutes (4:40 — the reward clause; 5:16's kin)); F6 the_cities_and_the_frame
(4:41-49 — asks: then_moses_set_apart (4:41 — the ACT; Makkot 10a:15-16 R. Simlai; the "then" form's seats), not_until_all_six (Mishnah Makkot 2:4; 9b:14 —
RF.the_refuge_law('six_cities') by CALL; the debit READ OPEN), the_manslayer_defined (4:42 — 19:4's words; Numbers 35:11; RF.the_manslayer by CALL;
Makkot 10a:9, 10a:11; Gittin 12a:11; Sotah 49a:4), the_three_names (4:43 — RF.DATA['the_six_cities'] by CALL; Makkot 10a:14; Joshua 20:8's Gaulon),
the_second_frame (4:44-45 — (R6); Yoma 72b:14; Menachot 53b:4; Avodah Zarah 2b:6, 2b:9; Makkot 10a:11; the Sifrei 323:1), the_borders_verbatim (4:46-49
— SHORTENED; the four diffs recomputed; OS.sihon_and_og('hermon') and OS.the_frame('after_sihon') by CALL; BK.the_call('last_camp') for the valley
opposite Beth-peor; Mount Sion the fourth name), the_readback_table (the eleven rows graded)).

THE DATA ROWS (nineteen): the_readback (the eleven rows of (R1)), the_law_bal_tosif (the exam's arms of (a)), the_teach_your_sons (Kiddushin 30a; Berakhot
21b-22a; Menachot 99b), the_horeb_hole (the tape's silence at Exodus 20:1 and 31:18 — W7's choice, the readback's finding, the two supplied lines, the D2
candidate filed), the_ten_words_seats (Exodus 34:28, Deuteronomy 4:13, 10:4), the_tablets_plene (the spelling census by CALL), the_no_image_list (g),
the_host_apportioned (h), the_bars_third_telling (1:37, 3:26, 4:21 against Numbers 20:12 — the OPEN row widened), the_exile_case (b), the_witnesses_chain
(the Sifrei 306:1's eleven), the_creed (4:35, 4:39; the kingship verses), the_inquiry_limits (Chagigah 11b-12a), the_instruments (4:34's seven against 26:8
and 7:19), the_three_cities (d), the_manslayer_definition (4:42, 19:4, Numbers 35:11, Joshua 20:3), the_second_frame (f), the_number_switching (the second
person's number by verse — the reading's lists), the_export_chapter_5 (i).

THE DAEMON law_obey_horeb (given_at Deut 4:2; installed_by BOOT with the class NAMED — a law in Moses' voice with no divine frame, the vows' class):
watches add_nothing_commanded → [adding_barred]; ten_words_declared → [covenant_declared]; tablets_given → [tablets_delivered]; witnesses_called →
[heaven_and_earth_witness]; three_cities_set_apart → [cities_set_apart]; horeb_case → [accepted, exempt]. No close, no timer, literal W dicts per kind;
the case kind dispatching to the cells by name in EXPLICIT branches.

THE TYPES (add_types_ch4.py): FIVE tape kinds — add_nothing_commanded (speech, 4:1-8), ten_words_declared (speech, 4:10-13; the first telling Exodus 20:1
named in the row), tablets_given (act, 4:13; the first telling Exodus 31:18 named), witnesses_called (speech, 4:25-31), three_cities_set_apart (act,
4:41-43) — with their witnesses in their verses; ONE case kind (horeb_case); FOUR new effects — adding_barred (block on Israel; 4:2), covenant_declared
(status on Israel; 4:13 "he declared to you his covenant"), heaven_and_earth_witness (status on Israel; 4:26), cities_set_apart (status on Israel; 4:41
"then Moses set apart"); the effects reused — tablets_delivered (the erection's), accepted, exempt; NO registry row (Israel and Moses the written-on
parties, both standing — a counterparty is no entity); the daemon block; the functions block obey_horeb (the_exhortation … the_cities_and_the_frame
WRAPPED); the span [[Deut, 4, 1, 49]]; the CALL edges by the ink — balak (Peor), refuge (the cities, the manslayer), opening_speech (the bar, the frame,
the borders), erection (the tablets, the ten words, the ascent's forty, Horeb plene), exodus_story (Sinai's days, the plagues, the sea), tochacha (the
exile's arms), pre_sinai (the creation), primeval (the furnace, the land), journeys (the dispossession), decalogue (the second word — OWED; altar_rules
CALL for 20:22), and every demand the census makes past the imports read on the DB and declared (CALL / VIA / FALSE / PARAMETER / INTERNAL /
RUN_CITATION), never a blanket row; the pointers after the gate's print (4:5's receipt RUN_CITATION with (R5)'s why); I5 63 → 64.

THE TAPE (five lines, two markers): under "# ---- Deut 4 ----" after the tape's last Deuteronomy 3 line (moses_besought): add_nothing_commanded (4:1-8,
page_order at (40, 11, 1)); the RETROGRADE marker at Deut 4:10 (M['giving'], (1, 3, 7)) then ten_words_declared (4:10-13, dated); the RETROGRADE marker at
Deut 4:13 (M['breaking'], (1, 4, 17)) then tablets_given (4:13, dated); witnesses_called (4:25-31, page_order); three_cities_set_apart (4:41-43,
page_order). The markers 161 → 163 (forward 126 unmoved, retrograde 20 → 22, proleptic unmoved); the tape's closes 126 UNMOVED; the counter ends at
(40, 11, 1) UNMOVED.

THE CHECKPOINTS CC1-CC9 (the prefix measured free):
CC1 THE LINES — five events of the sitting's kinds on the tape in the ink's order, all AFTER the tape's last Deuteronomy 3 line; the three own-day lines
page_order at (40, 11, 1); the two supplied lines reading_placed, dated by the RETROGRADE markers at Deut 4:10 and 4:13 with their stated days (1, 3, 7)
and (1, 4, 17); the counter ends at (40, 11, 1).
CC2 THE HOREB DAYS — M['giving'] = day_in(1, 3, 7) (the sinai_days row's giving, Rabbi Yose's seventh); M['breaking'] − M['ascent'] = 40 (the seventh of
Sivan plus the forty days = the seventeenth of Tammuz, Taanit 28b); the ten words' line dated M['giving'], the tablets' line dated M['breaking']; the
tablets_broken line at Exod 32:19 carries the same day as tablets_given (given and broken on one day).
CC3 THE LAW — adding_barred on israel_people ONE (a block) with its source beginning "Deut 4:1"; law_obey_horeb registered, given_at Deut 4:2,
installed_by boot; the register seats by CALL — Deut 4:5 ACT (the write's source contains the verse), Deut 4:45 DAEMONS with daemons 2.
CC4 THE READBACK — the_readback's rows 11, every row's tape entry FOUND on the running world by kind and first verse (rows n = found n); the grades'
census typed from the runner's print (SHORTENED 3, EXPANDED 5, SUPPLIED 2, DISAGREES 1); the DISAGREES row 4:21-22 OPEN — no ledger entry cites Deut
4:21; the two SUPPLIED rows' lines dated.
CC5 HOREB READ BACK — lord_descended ONE (Exod 19:18) at (1, 3, 7); covenant_declared on israel_people ONE dated (1, 3, 7), source beginning "Deut 4:10";
tablets_delivered on moses ONE dated (1, 4, 17), source beginning "Deut 4:13"; tablets_broken's line ONE at Exod 32:19 the same day; moses_ascended TWO
(the first and the second forty days).
CC6 PEOR, THE BAR, THE EXODUS, THE CREATION READ BACK — yoked_to_baal_peor on israel_people ONE (25:3); plague_struck on israel_people CLOSED with the
closer's note beginning "Num 25:8"; barred_from_the_land on moses ONE OPEN unmoved (the third telling writes nothing, no oath written); brought_out on
israel_people ONE (Exod 12:51); the marker at Gen 1:31 present with the era life:the_human; the dispossess debit on israel_people ONE OPEN (Num 33:50-56).
CC7 THE WITNESSES AND THE CASE — heaven_and_earth_witness on israel_people ONE dated (40, 11, 1), source beginning "Deut 4:25"; no timer set by the
sitting's lines (the end of days a prophecy); the tochacha's scattered_among_nations registered and NOT written on the tape (no exile).
CC8 THE THREE CITIES — cities_set_apart on israel_people ONE valued the three (Bezer, Ramoth, Golan — the refuge row's names by CALL), source beginning
"Deut 4:41"; the refuge debit appoint_six_cities_of_refuge on israel_people ONE OPEN unmoved (Makkot 2:4 — not until all six); closes 126 unmoved.
CC9 THE REST — entities 319 UNMOVED (Israel and Moses the written-on parties, both standing), closes 126 UNMOVED, the population table 148 UNMOVED, the
five kinds present; markers 161 → 163; the other counts 1b's exactly with the five lines and two markers dropped (THE REST test).
CP6 RETYPED (markers 161 → 163, F 126 unmoved) and CA1 RETYPED (the Deuteronomy retrograde markers' list gains ((1, 3, 7), 'Deut 4:10') and ((1, 4, 17),
'Deut 4:13')) AS OF this sitting; readback_probes Q4 NARROWED to the opening speech's stretch (Deuteronomy 1-3's lines and markers — the probe tests 1b's
form, not the tape's length); checkpoint_probes' "beyond the tape" verse COMPUTED from the tape (the first verse of the chapter after the tape's last
line — lesson xiii's second half; 'Deut 4:1' would be a position on the tape again).

THE PREDICTION'S ARITHMETIC: RUN = (1300, 96, 88, 0, 12, 1588, 35, 319, the four pairs, 126) — events +5 (the five lines), timers set +0, fired +0 (no
clock walk; the retrograde markers are dated points), cancels 0, retro-writes 12 UNMOVED, writes +5 (the daemon's watches summed: one effect per line —
adding_barred, covenant_declared, tablets_delivered, heaven_and_earth_witness, cities_set_apart), daemons fired +1 (law_obey_horeb), entities +0 (Israel
and Moses standing), closes +0; PREVIOUS_RUN = 1b's RUN exactly — THE REST drops the five lines by the runner's tag and the two markers by the span and
reproduces (1295, 96, 88, 0, 12, 1583, 34, 319, the four pairs, 126); NEWEST_RUNNER 'obey_horeb'; PLACEMENT markers text_constrained 103 UNMOVED,
reading_placed 43 → 45; events text_constrained 107 UNMOVED, page_order 1137 → 1140 (the three own-day lines), reading_placed 51 → 53 (the two supplied
lines) — read at the stitcher's print; CENSUS typed from the stitcher's print (on tape 1295 → 1300, history +5, kinds 840 → 846 — the five tape kinds and
the case kind, subjects 272 UNMOVED (israel, moses standing), markers 161 → 163 (R 20 → 22), closes 71 unmoved; the case rows the exam's persons, read
from the print); the population table 148 UNMOVED; the scene's tuple PREDICTED BY SCRIPT at the runner step (the exam's persons through horeb_case — each
written once; no timer; the persons the entities; no close); the narrative's (5 events, 5 writes, 0 closes, the entities israel and moses = 2, the
counter's day (11, 1), 2 dated lines, no row).

THE PROBES: readback_probes.py Q7-Q9 written to FAIL before the runner exists (Q7 the runner and its the_readback table with the eleven rows and the
grades' census, the two SUPPLIED rows naming their first tellings Exod 20:1 and 31:18; Q8 the two supplied lines dated by the retrograde markers at Deut
4:10 and 4:13 with the stated days (1, 3, 7) and (1, 4, 17), the tablets' day = the breaking marker's day; Q9 the register seats on the new tape — Deut
4:5 ACT, Deut 4:45 DAEMONS with daemons 2 — and the refuge debit OPEN after the three cities' line) and Q4 narrowed to chapters 1-3; NO parser rule this
sitting (the four number verses read right at the reading — census_probes unmoved at 224); the register gate unchanged; checkpoint_probes' verse computed.

THE ORDER: the design (this section) → the probes to FAIL (readback Q7-Q9 0/3; Q4 narrowed still 1/1; checkpoint_probes' verse computed, 7/7 unmoved)
→ the state doc's checkpoint (the docket may cross a compaction) → THE DOCKET by the union rule (four parts A-D, the reading instrument ch4_docket_rows.py,
the writer write_ch4_docket.py with the coverage computed and the cite index) → the types by script (add_types_ch4.py) → the recorder and the stitcher
(the scratch copies: SPAN_ORDER + 'obey_horeb'; the two retrograde marker rows at Deut 4:10 and 4:13) → the gates to FAIL (daemon, dependency) → the
runner (ch4_part1-4.py assembled by cat; the fast checker ch4_fastcheck.py over parts 1 and 2 before the first run; the honest-pairing guard; zero-report
probes; the scene and the narrative predicted by script; CASES generated from the cells' asks) → the recorder → the stitcher → the literals, CC1-CC9 and the
retypes (patch_seq_literals_ch4.py) → the tape run (10/10 with THE REST) → the probe gates (census 224, installation I5 64, readback 9/9, register 7/7,
clock, sequence, view, population, journal, cursor after the base regenerates, checkpoint 7/7) → the daemon and dependency gates GREEN → build_world →
the journal gate → THE REGISTER GATE --strict (Deut 4:5 declared ACT; 4:45 green with daemons 2) → checkpoint_positions.py in the background (the block
gained CC1-CC9) → the sweep in the background → the journal gate alone after the sweep → the records (this file's AS BUILT, COMPILE_DEBT's sitting-2 box
PAID + the 2b box (the second word OWED; the D2 candidate; the refuge debit's close outside the Torah), MOVE_CATALOG (checked), MIDDOT's docket entries,
MISHNAH_TOPICS (Avodah Zarah 3; Makkot 2; Pesachim 10; Rosh Hashanah 2-3; Eruvin 10; Sanhedrin 11; Kiddushin 1; Ketubot 13; Berakhot 5 marked),
RESEARCH_LOG, THE_STEPS, THE_BRIEFING, THE_LOOP.md's step 6 row (the second chapter on the first form; the tape's hole), RESUME, memory, the state doc's
checkpoint at the close, the recovery file's section 34).
'''
new = old.rstrip('\n') + TEXT
tmp = P + '.tmp'
open(tmp, 'w', encoding='utf-8').write(new); os.replace(tmp, P)
r = subprocess.run(['python3', f'{ROOT}/logic/solo_tools/gloss_lint.py', P], capture_output=True, text=True)
print(r.stdout[-600:], r.stderr[-300:])
print('appended', len(TEXT), 'bytes; the map now', os.path.getsize(P), 'bytes')
