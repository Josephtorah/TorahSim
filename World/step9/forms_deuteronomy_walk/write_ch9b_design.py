import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE DEUTERONOMY WALK sitting 7b — THE COMPILE OF CHAPTER 9 (2026-09-19; the owner: "Ok do ch 9" after the import cache): THE DESIGN written into the map
# at the close of RUN A of two (the rereads, the measurements — ch9_compile_recon.py, ch9_docket_scan.py, the running world's snapshot queried — and this
# section, BEFORE any code; the docket its own run by the window's budget), with the state doc's checkpoint (#197 addendum 3) naming the next step,
# the recovery page's lines, RESUME's head, the memory note and the index line. Every number typed from the instruments' prints of this run; the caps
# asserted before any file is opened; --check prints the plan only. Sitting 6b's form (write_ch8b_design.py).
import os, re, subprocess, sys
ROOT = _ROOT
MEM = os.path.expanduser('~/.claude/projects/-Users-Shared-TorahSim/memory')
CHECK = '--check' in sys.argv
R = lambda p: open(p, encoding='utf-8').read()
def W(p, s): open(p, 'w', encoding='utf-8').write(s)

DESIGN = r'''
## Sitting 7b — THE COMPILE OF CHAPTER 9, Deuteronomy 9:1-29 (2026-09-19; the owner: "Ok do ch 9" after THE VERIFIED-IMPORT CACHE): THE DESIGN — written at
## the close of RUN A of two under THE TWO-RUN RULE (the rereads: THE_STEPS' compiler block and Step 5's head, the sitting-7 AS BUILT, the 6b design as the
## compile's form, the 7b box (a)-(j); the measurements: ch9_compile_recon.py, ch9_docket_scan.py in the scratchpad, the running world's snapshot queried)
## and BEFORE any code; the docket ITS OWN RUN by the window's budget (395 rows, under the ~700 clause — the run that measured and designed had spent its 300k)

THE TWO RUNS AND THE DOCKET'S OWN: RUN A the rereads, the measurements and this design — CLOSED HERE, a clean compaction point (#197 addendum 3); THE
DOCKET by the union rule, EVERY ROW WHOLE (the parts on 6b's whole-row instruments, the writer write_ch9_docket.py, coverage computed) — its own run, the
dump already written (ch9_docket_dump.txt, 1,187 lines); RUN B the probes to FAIL (readback Q22-Q24), the types by script, the callees' facts printed, the
runner in parts with the fast checker and the generated CASES, the recorder and the stitcher, the literals DA1-DA9, the tape to 10/10 with THE REST,
checkpoint_check.py --all AFTER the tape, gates_chain.sh in one summary (the import cache in place), the records from the sheet in one call, the forms
copied, this section's AS BUILT, the commit message.

THE MEASUREMENTS (what the tape, the runners, the registries and the running world say before a line is typed): THE COUNTER stands at (40, 11, 1); the
tape's LAST LINES are chapter 8's three (grace_commanded, forgetting_warned, perishing_testified — on the counter's day, no marker) and its LAST MARKER the
forward one at Deut 5:32 (M['charge']). EVERY ACT THE CHAPTER RETELLS IS ON THE TAPE, in the erection runner's stretch (the recon's section 5, the days
read off the snapshot's log and rendered by the clock): moses_ascended 'first' at Exod 24:18 under the marker M['ascent'] = the seventh of Sivan — (1, 3, 7)
— placed by Ta'anit 28b at the erection's compile; calf_made at 32:4 (subject aaron, worshipped False) and moses_interceded plea 'relent' at 32:11-14
(decree_relented ONE on israel_people) — BOTH ON THE ASCENT'S DAY 894379, the calf's own day (the sixteenth of Tammuz, Shabbat 89a's sixth hour) UNMARKED
on the tape, the lines inheriting the last marker's day: an OPEN row for the owner, no change this sitting; the breaking marker M['breaking'] = the
SEVENTEENTH OF TAMMUZ, (1, 4, 17) — MISHNAH TA'ANIT 4:6's DATE IS ALREADY THE TAPE'S (reading_placed at the erection's compile; erection.ascent's cells
'seventeenth_tammuz' and 'sheet_taanit_4_6' the compile rules); tablets_broken (32:19), calf_destroyed (32:20 — Avodah Zarah 44a's four verbs, purpose
to_test), levites_gathered (32:26-29); the morrow marker M['morrow'] = M['breaking'] + 1 at 32:30 — (1, 4, 18), "the intercession's ascent (32:31)";
moses_interceded plea 'blot_me' at 32:31-33 (blotted_from_the_book ONE on the-sinners), tent_pitched_outside (33:7-11); the second-ascent marker at Exod
34:4, M['second_ascent'] = M['second_tablets'] − 40 where M['second_tablets'] = (1, 7, 10) from CAL_PARAMS second_tablets_given (Ta'anit 30b — the last
tablets given on Yom Kippur): (1, 5, 29) — THE TWENTY-NINTH OF AV BY THE MACHINE'S SUBTRACTION, where the tradition's Rosh Chodesh Elul is two days later
(the parameter's own open row — "not on the local Babylonian shelf"; Seder Olam Rabbah IS in the export, its chapter 6 keyed by name — the docket reads
it); moses_ascended 'second' at 34:2-4, 28 (the tradition's THIRD ascent — the tape's 'second', the intercession's forty a marked stretch, not a line);
attributes_proclaimed_at_sinai (34:6-7), covenant_cut_at_sinai (34:10, 27); the tablets_given line at Deut 4:13 (chapter 4's retrograde write,
first_telling Exod 31:18, dated at the breaking). THE CLOCK'S OWN ARITHMETIC REPRODUCES THE THREE FORTIES: 894379 → 894419 (the ascent to the breaking,
40), 894420 → 894460 (the morrow to the second ascent, 40), 894460 → 894500 = 10 Tishri (the second ascent to the last tablets, 40 — 10:10's forty, next
chapter's). NO LINE for God's word at 32:7-10 (speech — the register test; the intercession's case_source begins 32:11), for 33:1-6 (the ornaments), for
Aaron's peril (9:20 — nowhere: the LORD's anger at Aaron and Moses' prayer for him are TOLD ONLY HERE; the investiture and milluim ledgers read Aaron's
re-acceptance from this verse; shemini_day's cell reads Lev 9:7's 'approach' as the public re-acceptance after the calf). THE STATE "stiff-necked": NO
entry on israel_people names stiff or neck (the ledger scanned); the phrase's six Bible seats all the calf's; erection.calf('saru_stiff') counts them
((3, 6) — "turned quickly" three, "stiff-necked" six). THE FOUR PROVOCATIONS on the tape: fire_of_the_lord_burned (Num 11:1-3, name Taberah — fire_sank a
STATUS on israel), named 'Massah and Meribah' (Exod 17:7 — by first verse among the tape's sixty-one named lines), quail_and_plague (Num 11:31-35, graves
Kibroth-hattaavah), the rejection at Kadesh — spies_sent, spies_returned, report_given, evil_report_spread, congregation_wept, joshua_and_caleb_pleaded,
moses_pleaded_on_the_attributes (14:13-19 — offer "I will make of you a greater nation", argument "Egypt will hear"), pardoned_and_decreed,
decree_declared (14:26-35), presumed_to_go_up, smitten_to_hormah. THE OATH's line sworn_by_himself (Gen 22:16-18). THE KIN IN THE CODE: erection.ascent
(forty — the phrase's nine seats, seventeenth_tammuz, sheet_taanit_4_6, six_seventh, under_mountain), erection.calf (molten_calf, saru_stiff, seized —
Berakhot 32a:16 "let Me alone", three_legged, vayechal, vow_annulled, oath_endures, relent, four_verbs, nullification_dispute — Mishnah Avodah Zarah 3:3,
fourth_verb_decides — 44a:2, great_sin, individual_rule, surcharge — Sanhedrin 102a:15, plague, reading_law — Mishnah Megillah 4:10), erection.tablets
(breaking_ratified, fragments_by_call, finger_and_forms), erection.craftsmen (finger), exodus_story.trials (ten_list, count_by_exodus),
beha.taberah_and_quail (fire_at_edge, fire_sank, graves), shelach.decree (ability — "not able", egypt_will_hear, offer_second_seat, plea,
attributes_deleted, exceptions), shelach.spies (giants, forty_days), opening_speech.the_spies_read_back (the_murmuring, the_presumption, the_asking,
the_exceptions), obey_horeb.the_one_god('to_dispossess_nations' — 4:38), obey_horeb.no_image('consuming_fire_jealous_god' — 4:24),
obey_horeb.horeb_retold('the_ten_words_and_the_tablets' — 4:13), obey_horeb.the_exile_case('the_merciful_god' — 4:31),
covenant_at_horeb.the_voice_and_the_request('the_tablets_given_to_me' — 5:22), hear_o_israel.the_test_and_the_right('you_shall_not_test' — 6:16 Massah),
seven_nations.the_seven_nations('the_seven' — 7:1's "greater and mightier than you"), shemini_day.day('aaron_chatat_run' — the eighth day's calf, Lev 9:2,
the re-acceptance), good_land.the_way_of_forty_years (8:2's forty). THE REGISTRY: aaron mapped (28 entries — accepted, anointed, atoned_forgiven,
barred_from_the_land …), israel_people, moses, the_ark, the_mountain, the_covenant_at_sinai; NO row for the-calf or the-tablets (tape subjects without a
registry id, as at the erection); no registry row for taberah, massah, kibroth-hattaavah, kadesh-barnea (place tokens). THE CHECKPOINT PREFIX SPACE
(the 7b box's (i), measured before a name is typed): EVERY two-letter C-prefix is USED (C0-C5 and CA through CZ; FREE: []); the names are keyed by their
first word everywhere — checkpoint_positions.py per prefix name.split(' ')[0], checkpoint_check.py startswith(prefix), checkpoint_probes.py name.split,
the VERDICTS list literal strings — and NO code assumes a first letter (the scan of World/step9/*.py for startswith/== on 'C' beside cp/checkpoint/name:
nothing): 7b OPENS THE D SERIES — DA1-DA9 (no name on file starts with DA). THE PROBES on file: readback Q1-Q21 (Q10 absent); this sitting Q22-Q24.
THE DOCKET SIZED (ch9_docket_scan.py): 16 LINK rows in 10 works (Berakhot 4 — 7a:35 on 9:14, 32a:14 on 9:14, 32b:8 on 9:26-27, 34a:11 on 9:25; Avodah
Zarah 44a:1 and 52a:4 on 9:21; Megillah 19b:5 on 9:10 and 21a:17 on 9:9; Nedarim 32a:4 on 9:19 and 38a:8 on 9:17; Bava Batra 9b:7 on 9:19; Chullin 90b:12
and Tamid 29a:8 on 9:1 — the hyperbole rule, the Sifrei 25:4's kin; Pesachim 87b:22 on 9:17; Yoma 75b:11 on 9:9; Tosefta Avodah Zarah 4:3 on 9:21 — ten
verses cited, 1, 9, 10, 14, 17, 19, 21, 25, 26, 27), 377 TOPIC rows by address (Mishnah Avodah Zarah 3 whole 10, Avot 5:4 and 5:6 — the ten trials and
the ten wonders, Megillah 4:10, Yoma 8:8-9; Ta'anit 26a — Mishnah 4:6's amud — 14, Berakhot 32a-32b 64, 7a 36, Shabbat 87a-89a 40, Menachot 99a-99b 35,
Bava Batra 14b 12, Ta'anit 28b-29a 34, Avodah Zarah 43b-44a 39, Sanhedrin 102a 18, Beitzah 25b 16, Shabbat 55a 18, Arakhin 15a 21, Yoma 86b 19) and the
two midrash rows the box names (Vayikra Rabbah 10:5 — Aaron's sons; Devarim Rabbah 2:1 — the ten names of prayer) = 395 addresses, 161 CREDITED by
address (the erection's own docket 41, the Exodus triage ledger 52, chapter 4's docket 35 the largest — the calf's rows read at its own sitting); at the
docket's run Mishnah Ta'anit 4:6-7 (the export's Mishnah_Ta_anit) and Seder Olam Rabbah 6 are added and every row read WHOLE.

THE NAME: cold_run_not_righteousness.py — the 64th runner ("not for your righteousness", 9:4, 9:5, 9:6 — the chapter's refrain; the unit
deu_09_not_righteousness); the daemon law_not_righteousness, given_at Deut 9:1, installed_by boot (the Deuteronomy daemons' form); six cells.

THE READBACK ON THIS CHAPTER — THE SIXTH FORM: THE RETELLING OF A STRETCH (THE LOOP's step 6; after T1 the narrative retelling, T2 the retelling that fills
a hole, T3 the retelling inside a law, T4 the laws' form on the kin, T5 the retelling of a state): chapter 9 is Moses telling the calf in his own voice — so
its rows are T1's reference rows against the tape's lines by kind and first verse or the kin's cells by CALL (God's word VERBATIM at 9:13, Moses' acts in
his own words at 9:17), T2's one hole filled (Aaron's peril, 9:20 — SUPPLIED WITH A WRITE, the retrograde form of 3b), AND a row-kind no chapter had: "forty
days and forty nights" told THREE TIMES (9:9, 9:18, 9:25) is not a line but a STRETCH between two markers, graded against THE CLOCK's own arithmetic (the
days between the markers, 40 and 40) and the answer sheet's dates (Ta'anit 4:6 the seventeenth of Tammuz; 28b the seventh of Sivan) — THE CLOCK READ BACK.
THE DECISIONS (the design's, open to the owner's word): (1) AARON'S PERIL IS AN ACT told only in the retelling — "I prayed for Aaron also at that time" —
so it is WRITTEN ONCE at its own day by a RETROGRADE MARKER (the retelling rules; 3b's mediator form): M['aaron_told'] = M['morrow'] — "at that time" is the
second forty, whose day the tape holds at 32:30 (18 Tammuz, (1, 4, 18)); placement reading_placed (the shelf places the prayer for Aaron inside the
second forty — the docket's rows to confirm); the line prayed_for_aaron (an ACT: subject moses, for aaron; the LORD's anger "to destroy him" its field;
first_telling "told only here"); the stretch ENDED by a forward marker at Deut 9:21 (M['speech_resumed_9'] = M['speech'], text_constrained — the counter's
day re-asserted, 4:25's and 5:32's form). THE WRITE: destruction_averted — a STATUS on aaron, written by law_not_righteousness watching prayed_for_aaron
(the effects law: the vocabulary the shelf's — Vayikra Rabbah 10:5 reads "to destroy him" as the destruction of SONS, two dying and two saved by the
prayer; the docket's rows fix the name before the types are typed). (2) THE STIFF NECK IS A STATE IN THE FIRST TELLING (Exod 32:9 — not told only here):
its rows reference the kin's cell by CALL (erection.calf('saru_stiff')) and carry NO write and NO supplied grade — the phrase's six seats a DATA row; the
absence of any entry asserted on the world (6b's CU7 form). (3) THE CALF'S OWN DAY stays unmarked (16 Tammuz by Shabbat 89a; calf_made on the ascent's day)
— an OPEN row named in the table, no marker added this sitting (a change to the Exodus stretch is not this chapter's). (4) THE SECOND ASCENT'S DATE (29 Av
by subtraction against the tradition's 1 Elul) — an OPEN row on the clock, the parameter's own; Seder Olam Rabbah 6 read at the docket, no retype of the
parameter without the shelf's row. THE ROWS (about thirty predicted; the grades' census typed from the runner's print at RUN B): 9:1 "nations greater and
mightier than you" — obey_horeb.the_one_god('to_dispossess_nations') by CALL (4:38): VERBATIM in kind; 9:1 "cities great and fortified to the heavens" —
opening_speech.the_spies_read_back by CALL (1:28): VARIANT (the spelling); 9:2 "a people great and tall, the sons of the Anakim" — the same cell and
shelach.spies('giants'): VERBATIM in kind (1:28 five tokens); 9:3 "a consuming fire" — obey_horeb.no_image('consuming_fire_jealous_god') by CALL (4:24):
VERBATIM in kind; 9:5 "the word which the LORD swore to your fathers" — sworn_by_himself (Gen 22:16) by kind: VERBATIM in kind (7:8's form); 9:6 "a
stiff-necked people" — erection.calf('saru_stiff') by CALL: VERBATIM in kind (Exod 33:3 seven tokens); 9:7 "from the day you came out of Egypt until you
came to this place you have been rebellious" — exodus_story.trials('ten_list') by CALL (the ten trials, Avot 5:4 and Arakhin 15a the answer sheet):
EXPANDED (the whole span made one rebellion); 9:8 "at Horeb you provoked the LORD" — calf_made (Exod 32:4) by kind: VARIANT; 9:9 "the tablets of the
covenant … forty days and forty nights, bread I did not eat and water I did not drink" — THE STRETCH from M['ascent'] to M['breaking'] (40 days, the clock's
arithmetic) with moses_ascended 'first' (24:18) by kind: EXPANDED (the fasting supplied from 34:28 — the Sifrei 14:1 and 306:25 read 9:9 with 34:28); 9:10
"two tablets of stone written with the finger of God … on the day of the assembly" — tablets_given (Deut 4:13, first_telling 31:18) by kind and
covenant_at_horeb.the_voice_and_the_request('the_tablets_given_to_me') by CALL (5:22): VERBATIM in kind (10:4's ten tokens forward); 9:11 "at the end of
forty days … the LORD gave me the two tablets" — the same line: VERBATIM in kind (the plene/defective pair in one verse a DATA row); 9:12 "arise, go down
quickly … your people have corrupted … a molten image" — the calf_made line by kind and the ink of 32:7-8 (nine tokens): VARIANT; 9:13 "I have seen this
people, and behold it is a stiff-necked people" — the ink of 32:9 (ELEVEN OF THIRTEEN) and erection.calf('saru_stiff'): VERBATIM; 9:14 "let Me alone, that
I may destroy them and blot out their name … and I will make of you a nation mightier and more numerous" — erection.calf('seized') and ('three_legged')
by CALL, moses_interceded 'relent' (32:11) by kind: VARIANT (THE OFFER'S THREE FORMS a DATA row: Exod 32:10, Num 14:12, 9:14; "blot out their name"
supplied); 9:15 "I turned and came down … the mountain burning with fire, the two tablets on my two hands" — tablets_broken (32:19) by kind (32:15 four
tokens): VARIANT; 9:16 "and I looked, and behold, you had sinned … a molten calf" — calf_made by kind (32:8 four, 32:4 three): VARIANT (the vision formula
supplied); 9:17 "I took hold of the two tablets and threw them from my two hands and broke them before your eyes" — tablets_broken by kind (ONE token
with 32:19): EXPANDED in Moses' own words (Shabbat 87a's "which you broke" — erection.tablets('breaking_ratified') by CALL); 9:18 "I fell down before the
LORD as at the first, forty days and forty nights … because of all your sin" — THE STRETCH from M['morrow'] to M['second_ascent'] (40) with
moses_interceded 'blot_me' (32:31) by kind: EXPANDED (the forty days supplied — Exodus has "and Moses returned to the LORD" with no forty; Yoma 86b's
confession the kin's cell 'confess_specify'); 9:19 "the LORD hearkened to me that time also" — the intercession's effect decree_relented (32:14) by kind:
TURNED (the relenting told as hearkening; Onkelos "accepted my prayer"); 9:20 AARON'S PERIL — NO LINE, NO CELL: SUPPLIED, WITH THE WRITE (the retrograde
line prayed_for_aaron at (1, 4, 18); the sixth form's T2 row); 9:21 "your sin, the calf … I burned it with fire and crushed it, grinding it thoroughly until
it was fine as dust; and I threw its dust into the brook" — calf_destroyed (32:20) by kind and erection.calf('four_verbs', 'fourth_verb_decides') by
CALL: VARIANT (the dust into the brook supplied, THE FOURTH VERB — the drinking — DROPPED: Avodah Zarah 44a's test not retold, a DATA row; Josiah's
Kidron the kin); 9:22 "at Taberah, at Massah, at Kibroth-hattaavah" — fire_of_the_lord_burned (Num 11:1), named (Exod 17:7), quail_and_plague (Num 11:31)
by kind, hear_o_israel.the_test_and_the_right('you_shall_not_test') by CALL: VERBATIM in kind (three names, three lines; out of the tape's order); 9:23
"when the LORD sent you from Kadesh-barnea, saying go up and possess … you rebelled … you did not believe Him nor hearken" — congregation_wept (14:1) and
decree_declared (14:26) by kind, opening_speech.the_spies_read_back('the_murmuring', 'the_presumption') by CALL (1:26, 1:32): VARIANT; 9:24 "you have
been rebellious with the LORD from the day I knew you" — the trials cell again: VERBATIM in kind (9:7's doublet); 9:25 "the forty days and forty nights
that I fell down" — THE SAME STRETCH told with the article (the doublet of 9:18; the Sifrei 26:7's "I fell down" among the ten names of prayer):
VERBATIM in kind; 9:26 "Lord GOD, do not destroy Your people and Your inheritance, which You redeemed … with a mighty hand" — moses_interceded 'relent'
(32:11 five tokens) by kind: VARIANT (1 Kings 8:51 and Nehemiah 1:10 quote THIS telling — the run outside the Torah, a DATA row); 9:27 "remember Your
servants Abraham, Isaac and Jacob; do not turn to the stubbornness of this people" — the same line (32:13 — Israel there, Jacob here) and
erection.calf('oath_endures') by CALL: VARIANT (Shabbat 55a's merit of the fathers the exam's row); 9:28 "lest the land … say: because the LORD was not
able … and because He hated them" — moses_pleaded_on_the_attributes (Num 14:13-19 — 14:16 seven tokens) by kind and shelach.decree('ability',
'egypt_will_hear') by CALL, Exod 32:12's "why should the Egyptians say" (two tokens): VARIANT (THE TAUNT'S FOUR FORMS a DATA row — 32:12, 14:16, 1:27,
9:28); 9:29 "Your people and Your inheritance whom You brought out by Your great power and Your outstretched arm" — the same intercession line (32:11
"great power and a mighty hand") and obey_horeb.the_one_god by CALL (4:34, 4:37): VERBATIM in kind. THE HOLES: ONE — Aaron's peril (9:20), the act with
no line and no cell, filled by the retrograde write; the calf's own day and the second ascent's date OPEN rows, not holes.

THE CELLS (F1-F6; every token probed; effects on every cell; the exam's rows the docket's crowns): F1 THE FRAME — "not for your righteousness" (9:1-6: Hear,
O Israel; the nations greater and mightier by CALL (4:38, 7:1); the Anakim by CALL (1:28); the consuming fire by CALL (4:24); THE THREE REASONS — the
nations' wickedness, the word sworn to the fathers (the oath's line), the stiff neck (the cell by CALL, no write); the boaster's "my righteousness" barred
(9:4 "do not say in your heart"); MERIT (Onkelos's word at 9:4-6) against RIGHTEOUSNESS — the exam: Shabbat 55a (the merit of the fathers ceased — R.
Shmuel bar Nachmani), Beitzah 25b (the stiff-necked people the most impudent of the nations); the effect: NONE on the tape (a declaration, no write) — the
cell's verdicts EFFECTS = [FX.NONE] as the ink's 'not' has no act). F2 THE CALF RETOLD — 9:7-17: the readback rows above by kind and by CALL (erection's
cells: molten_calf, saru_stiff, seized, three_legged, vayechal, breaking_ratified, four_verbs), THE OFFER'S THREE FORMS and THE THREE SPELLINGS OF
"TABLETS" DATA rows (the box's (g) and (h)); the exam: Berakhot 32a (the seizing; the three-legged chair; the vow annulled), 7a:35 (9:14 "I will make of
you" — every promise fulfilled: the link row), Shabbat 87a (the breaking approved), Nedarim 38a:8 and Pesachim 87b:22 (9:17 Moses' might — the link
rows), Menachot 99a-b and Bava Batra 14b (the fragments in the ark — 10:2 forward, the kin's cell fragments_by_call). F3 THE FORTY DAYS — THE CLOCK READ
BACK (9:9, 9:11, 9:18, 9:25): the three stretches measured on the running world by the markers' days (the ascent to the breaking 40; the morrow to the
second ascent 40; the second ascent to 10 Tishri 40 — 10:10 forward), rendered as dates — (1, 3, 7), (1, 4, 17), (1, 4, 18), (1, 5, 29), (1, 7, 10) — and
GRADED against the answer sheet: Mishnah Ta'anit 4:6 (the seventeenth of Tammuz — MATCH), Ta'anit 28b (the seventh of Sivan — MATCH; the forty-day
arithmetic), Shabbat 88a-89a (the giving's days; Moses among the angels — the Sifrei 14:1, 306:25), Seder Olam Rabbah 6 (the ascents' dates — the 1 Elul
row, OPEN against the machine's 29 Av); the parser's [40, 40] at 9:9, 9:11, 9:18, 9:25 asserted; Megillah 21a:17 (9:9 — the link row). F4 AARON'S PERIL —
9:20: the retrograde line and its write (decision 1); the exam: Vayikra Rabbah 10:5 ("to destroy him" — the sons; two died, two remained by the prayer),
Sanhedrin 102a (the calf's surcharge — the kin's cell 'surcharge'), the milluim's re-acceptance by CALL (shemini_day.day('aaron_chatat_run') — Lev 9:2's
calf for the calf; the investiture and milluim ledgers' rows cited); the register: Aaron's "atoned_forgiven" entry stands, the new status beside it. F5
THE FOUR PROVOCATIONS — 9:22-24: the three named lines and the rejection's, out of the tape's order (the retelling's own order — Taberah, Massah, Kibroth,
Kadesh: the reading's finding), by CALL to beha, hear_o_israel, opening_speech, shelach; the exam: Avot 5:4 and Arakhin 15a (the ten trials — which
four these are), Nedarim 32a:4 and Bava Batra 9b:7 (9:19 — the link rows). F6 THE INTERCESSION'S SECOND TELLING — 9:25-29: the rows against
moses_interceded (32:11-14) and moses_pleaded_on_the_attributes (14:13-19) — the same argument twice on the tape (Israel/Jacob, the Egyptians/the land,
the mountains/the wilderness — the three swaps a DATA row), THE TAUNT'S FOUR FORMS, SOLOMON AND NEHEMIAH QUOTING THIS TELLING (1 Kings 8:51, Nehemiah
1:10 — the run outside the Torah, a DATA row: the prayer's words at the temple's dedication), the ten names of prayer (the Sifrei 26:7, Devarim Rabbah
2:1 — 9:25 "I fell down" and 9:26 "I prayed" two of the ten), the exam: Berakhot 32b:8 and 34a:11 (the link rows — prayer's praise, the prostration),
Berakhot 7a (the promises fulfilled), Yoma 8:8-9 and 86b (repentance and the confession's specifying — the kin's cell). THE DATA ROWS (about twelve): the
readback table, the offer's three forms, the tablets' three spellings, the taunt's four forms, the three swaps, the fourth verb dropped, Solomon and
Nehemiah, the ten names of prayer, the calf's own day (OPEN), the second ascent's date (OPEN), the stiff neck's six seats, the three voices on one
pronoun (the reading's finding — no cell).

THE LINES ON THE TAPE (the recorder and the stitcher; the design's arithmetic): ONE retrograde marker at Deut 9:20 (M['aaron_told'] = M['morrow'];
reading_placed), ONE line — prayed_for_aaron (act; subject moses, for aaron; case_source 'Deut 9:20 — …'; first_telling 'told only here'; dated (1, 4,
18)), ONE forward marker at Deut 9:21 (M['speech_resumed_9'] = M['speech']; text_constrained) — the stretch ended, the counter's day (40, 11, 1)
re-asserted; the daemon's ONE write destruction_averted (a STATUS on aaron, dated with the line). THE TYPES (add_types_ch9.py): event_vocabulary +2
(prayed_for_aaron — form act, witness Deut 9:20; not_righteousness_case — the exam's case kind), effect_vocabulary +1 (destruction_averted — status, on
aaron; the shelf's vocabulary from the docket), daemon_dispositions (law_not_righteousness — file, wraps, given_at Deut 9:1, installed_by boot, watches
{prayed_for_aaron: [destruction_averted], not_righteousness_case: [accepted, exempt]}; the functions block's six cells WRAPPED), dependency_dispositions
(the span [[Deut, 9, 1, 29]]; the CALL edges predicted ELEVEN — erection, exodus_story, beha, shelach, opening_speech, obey_horeb, covenant_at_horeb,
hear_o_israel, seven_nations, shemini_day, good_land — the census decides (4b's, 5b's and 6b's lesson: the design's pointer list is a prediction; "as at
the first" (9:18) the one AS_WHEN candidate, a RUN_CITATION of 9:9's stretch if demanded), installation_probes I5 68 → 69.

THE PREDICTION'S ARITHMETIC: RUN = (1311, 96, 88, 0, 12, 1606, 40, 319, the four pairs, 127) — events +1 (the one line), timers set +0, fired +0 (no clock
walk — a retrograde marker leaves the counter unmoved), cancels 0, retro-writes 12 UNMOVED (the RETRO-WRITE tag is the timers' and dedications' — a write
under a retrograde stretch is a WRITE with a dated field, 3b's form; READ FROM THE STITCHER'S PRINT), writes +1 (the daemon's one), daemons fired +1
(law_not_righteousness), entities +0 (aaron on the registry), closes +0; PREVIOUS_RUN = 6b's RUN EXACTLY (1310, 96, 88, 0, 12, 1605, 39, 319, the four
pairs, 127): THE REST drops the one line by the runner's tag and the span and the daemon's write with it — no delta; NEWEST_RUNNER 'not_righteousness';
markers 167 → 169 (PLACEMENT markers text_constrained 106 → 107, reading_placed 46 → 47; R 23 → 24, F 129 → 130 — typed from the stitcher's print);
events page_order 1146 → 1147 (text_constrained 109 and reading_placed 55 unmoved, the dated line page_order); CENSUS on tape 1310 → 1311, history +1,
kinds 855 → 856, subjects 272 UNMOVED (moses), markers 169, closes 71 unmoved; the population table 148 UNMOVED; the scene's tuple PREDICTED BY SCRIPT at the
runner step (the exam's persons through not_righteousness_case — each written once; no timer; no close); the narrative's (its own world: 1 write, 0
closes, the entities aaron and moses, the counter's day (11, 1) with ONE dated line (the retrograde), no row).

THE CHECKPOINTS DA1-DA9 (the D series opened; the literals typed from the prints at RUN B):
DA1 THE LINES — one event prayed_for_aaron on the tape AFTER the tape's last Deuteronomy 8 line, DATED (1, 4, 18) by the retrograde marker at Deut 9:20
(markers 167 → 169: the retrograde one and the forward one at 9:21); the counter ends at (40, 11, 1).
DA2 THE WRITE — destruction_averted on aaron ONE (a status), source beginning "Deut 9:20", dated with the line; law_not_righteousness registered,
given_at Deut 9:1, installed_by boot; the functions block's six cells WRAPPED.
DA3 THE READBACK OF THE CALF — the_readback's rows (about thirty; the census from the print), every reference row's entry FOUND: the tape lines by kind and
first verse (calf_made Exod 32:4, moses_interceded 32:11 and 32:31, tablets_broken 32:19, calf_destroyed 32:20, moses_ascended 24:18, tablets_given Deut
4:13, fire_of_the_lord_burned Num 11:1, named Exod 17:7, quail_and_plague Num 11:31, congregation_wept 14:1, decree_declared 14:26,
moses_pleaded_on_the_attributes 14:13, sworn_by_himself Gen 22:16) and the kin's cells by CALL (each returning its verdict on its own ask); the one
SUPPLIED row 9:20's WITH its write; the two OPEN rows named; the one hole named.
DA4 THE CLOCK READ BACK — the four markers' dates on the running world: 'Exod 24:18' (1, 3, 7), 'Exod 32:19' (1, 4, 17), 'Exod 32:30' (1, 4, 18), 'Exod
34:4' (1, 5, 29); the three stretches 40, 40, 40 (the last to 10 Tishri, day 894500); Ta'anit 4:6's date MATCH, 28b's MATCH; the second ascent OPEN.
DA5 THE KIN STANDS — decree_relented ONE on israel_people, blotted_from_the_book ONE on the-sinners, tablets_delivered FOUR entries (the ark, moses, the
tablets twice), fire_sank ONE, atoned_forgiven on aaron UNMOVED (the readback references, no second write); moses_interceded TWO lines and
moses_pleaded_on_the_attributes ONE UNMOVED (the new line is NOT a third intercession — its own kind).
DA6 THE STIFF NECK — no effect naming stiff or neck on israel_people (the state in the first telling, no entry; asserted on the world); the DATA row's
six seats.
DA7 THE FOUR PROVOCATIONS — fire_of_the_lord_burned ONE, quail_and_plague ONE, named at Exod 17:7 ONE, decree_declared ONE, congregation_wept ONE,
presumed_to_go_up ONE, smitten_to_hormah ONE UNMOVED; nothing written on Taberah, Massah, Kibroth or Kadesh (no registry rows).
DA8 THE INTERCESSION'S TWO TELLINGS — the tape's two lines (32:11-14, Num 14:13-19) UNMOVED; the readback's three swaps and the taunt's four forms the
DATA rows; the effect decree_relented's entry the reference, no second write.
DA9 THE REST — entities 319 UNMOVED, closes 127, markers 169, the population table 148 UNMOVED, the one kind present; the other counts 6b's exactly with
the one line and the daemon's one write dropped (THE REST test — NO declared delta). NO retype of the older REST literals expected but ONE — every
older checkpoint holding "markers 167" as a literal moves to 169 (5b's and 6b's lesson on a stale literal: grep for 'markers 167' / '167' beside markers
BEFORE the tape; retyped from the print); every miss shown at once by checkpoint_check.py --all AFTER the tape.

THE PROBES (RUN B's first step): readback_probes.py Q22-Q24 written to FAIL before the runner exists — Q22 the runner and its the_readback table — THE
SIXTH FORM (the retelling of a STRETCH): the rows and their census typed from the print; every reference row's entry found (the tape by kind and first
verse, the kin's cells by CALL, the three stretches by the markers' days); the one SUPPLIED row 9:20's with its write; the two OPEN rows; the one hole;
Q23 the retrograde line — prayed_for_aaron dated (1, 4, 18) under the marker at Deut 9:20 (stated day = M['morrow']), the forward marker at 9:21, markers
169, the counter (40, 11, 1); the write destruction_averted ONE on aaron, source 'Deut 9:20', dated with the line; Q24 the kin stands and THE CLOCK —
decree_relented, blotted_from_the_book, tablets_delivered, fire_sank, atoned_forgiven UNMOVED; moses_interceded two, moses_pleaded one; the four
markers' dates and the three forties as DA4; Q19-Q21 unchanged; NO parser rule this sitting (the seven number verses read right at the reading —
census_probes unmoved at 224); the register gate unchanged (no receipt form in the chapter); checkpoint_probes' verse computed (2b's form).

THE ORDER: this design → the state doc's checkpoint (#197 addendum 3 — RUN A closed) → THE DOCKET, ITS OWN RUN: the dump (ch9_docket_dump.txt, 1,187
lines, 395 rows; Mishnah Ta'anit 4:6-7 and Seder Olam Rabbah 6 added at its run), the parts on 6b's whole-row instruments (ch8_docket_A/B/C.py,
ch8_docket_common.py, ch8_docket_rows.py derived), EVERY ROW WHOLE, the verdicts LAW / DERIVATION / DISPUTE / CONTEXT / OUTSIDE with the credits computed,
the writer write_ch9_docket.py, the docket's records (COMPILE_DEBT's box (j), MIDDOT — every code checked in MIDDOT.md before it is typed, MISHNAH_TOPICS,
the state doc's checkpoint) → RUN B: the probes to FAIL (patch_probes_ch9.py: Q22-Q24), the types (add_types_ch9.py), the callees' facts printed before
any assert (ch9_callees.py — every CALL named above), the runner in parts with the fast checker (ch9_fastcheck.py) and the generated CASES
(ch9_cases_gen.py; the guard's count from the generator's print), the recorder (seq_record_ch9.py) and the stitcher (seq_stitch_ch9.py; the placement
print read for the retrograde line), the literals DA1-DA9 and the VERDICTS entries (patch_seq_literals_ch9.py; the stale 'markers 167' literals
retyped from the print), the tape to 10/10 with THE REST, checkpoint_check.py --all AFTER the tape, gates_chain.sh in one summary (the cache in place:
the moved runner's own harvest once; the sweep of the moved runners and their importers), the records from the sheet in one call (write_ch9b_records.py:
the map's AS BUILT, COMPILE_DEBT's sitting-7 box PAID and the 7b box, MIDDOT, MISHNAH_TOPICS, RESEARCH_LOG, THE_STEPS, THE_BRIEFING, THE_LOOP's step-6 row
(the sixth form), RESUME, RECORD_FORMS, the state doc, the addenda, the recovery page, the memory), the forms copied (copy_ch9b_forms.py), the commit
message (the cache's and this sitting's, for the owner's word).
'''

STATE = r'''
#197 ADDENDUM 3 (2026-09-19, at the close of RUN A of THE DEUTERONOMY WALK sitting 7b — THE COMPILE OF CHAPTER 9, on the owner's "Ok do ch 9" — A CLEAN COMPACTION POINT): THE STATE: RUN A DONE — the rereads (THE_STEPS' compiler block and Step 5's head, the sitting-7 design and AS BUILT, the 7b box (a)-(j), the 6b design as the form), the measurements (ch9_compile_recon.py over the sixty-three runners, the registries, the tape and the running world's snapshot — every act the chapter retells found on the tape in the erection runner's stretch; THE CLOCK's dates at the calf rendered: the ascent (1, 3, 7), the breaking (1, 4, 17) = Mishnah Ta'anit 4:6's seventeenth of Tammuz ALREADY THE TAPE'S, the morrow (1, 4, 18), the second ascent (1, 5, 29) by subtraction from 10 Tishri — an OPEN row against the tradition's 1 Elul; the three forties reproduced by the clock's own arithmetic; Aaron's peril (9:20) on no line and in no cell; the stiff neck no entry; the checkpoint prefix space MEASURED — every C-prefix used, the names keyed by their first word everywhere, no code assuming a letter: THE D SERIES OPENS, DA1-DA9; ch9_docket_scan.py — 16 link rows in 10 works, 377 topic rows + 2 midrash rows = 395 addresses, 161 credited), and THE DESIGN in the map (World/step9/DEUTERONOMY_WALK.md "Sitting 7b — THE COMPILE OF CHAPTER 9 … THE DESIGN"): THE READBACK'S SIXTH FORM — THE RETELLING OF A STRETCH (the forties graded against the clock's arithmetic and the answer sheet's dates), Aaron's peril SUPPLIED WITH A WRITE (one retrograde marker at 9:20 to the morrow's day, the line prayed_for_aaron, the status destruction_averted on aaron, the forward marker at 9:21), the stiff neck a state in the first telling (no write), the calf's own day and the second ascent's date OPEN rows, about thirty readback rows predicted, six cells F1-F6, RUN predicted (1311, 96, 88, 0, 12, 1606, 40, 319, the four pairs, 127), markers 169, the probes Q22-Q24, eleven CALL edges predicted. NOT COMMITTED: THE VERIFIED-IMPORT CACHE (the message at <scratch>/commit_msg_cache.txt) and this design. NOTHING MID-FLIGHT — A CLEAN COMPACTION POINT. NEXT ON THE RULING ("Ok do ch 9"): THE DOCKET, ITS OWN RUN (395 rows, every row whole — the dump at <scratch>/ch9_docket_dump.txt, 1,187 lines; the instruments ch8_docket_A/B/C.py and ch8_docket_common.py in the forms, derived by sed; Mishnah Ta'anit 4:6-7 and Seder Olam Rabbah 6 added), then RUN B (the probes to FAIL, the types, the runner, the tape to 10/10, the chain, the records). POST-COMPACTION REREADS: the recovery page, the map's "Sitting 7b … THE DESIGN" (the newest section), MEMORY.md.
'''

RESUME = r'''# ⚠ THE DEUTERONOMY WALK sitting 7b — THE COMPILE OF CHAPTER 9, RUN A DONE (2026-09-19; the design in step9/DEUTERONOMY_WALK.md "Sitting 7b … THE DESIGN"):
# the readback's SIXTH FORM (the forties graded against the clock — the tape already holds Ta'anit 4:6's 17 Tammuz), Aaron's peril a retrograde write, the D
# series of checkpoints (DA1-DA9). NEXT: the docket (its own run, 395 rows whole), then RUN B. UNCOMMITTED: the import cache and this design.
'''

MEMO = r'''
SITTING 7b — THE COMPILE OF CHAPTER 9, RUN A DONE (2026-09-19, "Ok do ch 9"): the design in the map — THE READBACK'S SIXTH FORM, THE RETELLING OF A STRETCH
(9:9, 9:18, 9:25's forty days are a stretch between two markers, graded against the clock's arithmetic and the answer sheet's dates: the breaking (1, 4, 17)
= Ta'anit 4:6's 17 Tammuz is ALREADY THE TAPE'S; the second ascent (1, 5, 29) by subtraction vs the tradition's 1 Elul an OPEN row); Aaron's peril (9:20)
SUPPLIED WITH A WRITE (a retrograde marker to the morrow's day, the line prayed_for_aaron, the status destruction_averted on aaron); the stiff neck a state
in the first telling (no write); THE D SERIES (DA1-DA9 — every C-prefix used; the names keyed by their first word everywhere). NEXT: the docket its own run
(395 rows), then RUN B (the runner cold_run_not_righteousness.py, the 64th; the daemon law_not_righteousness).
'''

MAP = f'{ROOT}/World/step9/DEUTERONOMY_WALK.md'; STATEDOC = f'{ROOT}/logic/pre_logic_methods_2026-07-28/PROMPT_continue_solo_era_2026-08-06.md'
REC = f'{ROOT}/logic/pre_logic_methods_2026-07-28/RECOVERY_new_thread_2026-09-12.md'; RES = f'{ROOT}/World/RESUME.md'
WALK = f'{MEM}/deuteronomy-walk.md'; IDX = f'{MEM}/MEMORY.md'
REC_EDITS = [
 ("the state doc #197 addendum 2 the newest)", "the state doc #197 addendum 3 the newest)"),
 ("- NEXT ON HIS WORD: the commit; then 7b (chapter 9's compile, two runs: the calf's readback rows, Aaron's retrograde write, a NEW\n  checkpoint series — CU the last prefix).",
  "- 7b RUN A DONE (the design in the map; the D series opens). NEXT: the docket (its own run, 395 rows whole), then RUN B; the\n  cache and 7b uncommitted."),
]
IDX_EDIT = ("NEXT: 7b (a NEW checkpoint series)", "7b RUN A done; the docket next")
ok = True
for a, b in REC_EDITS:
    if R(REC).count(a) != 1: print('REC ANCHOR', R(REC).count(a), a[:50]); ok = False
if R(IDX).count(IDX_EDIT[0]) != 1: print('IDX ANCHOR', R(IDX).count(IDX_EDIT[0])); ok = False
assert "## Sitting 7 — CHAPTER 9 — AS BUILT" in R(MAP) and "#197 ADDENDUM 2" in R(STATEDOC) and "## Sitting 7b" not in R(MAP)
rec = R(REC)
for a, b in REC_EDITS: rec = rec.replace(a, b)
idx = R(IDX).replace(*IDX_EDIT)
print('anchors %s; the recovery page would be %d bytes (cap 10240); MEMORY.md %d (cap 17000); the design %d bytes' % ('OK' if ok else 'BAD', len(rec.encode('utf-8')), len(idx.encode('utf-8')), len(DESIGN.encode('utf-8'))))
assert ok and len(rec.encode('utf-8')) <= 10240 and len(idx.encode('utf-8')) <= 17000
if CHECK: sys.exit(0)
W(MAP, R(MAP).rstrip('\n') + '\n' + DESIGN)
W(STATEDOC, R(STATEDOC).rstrip('\n') + '\n' + STATE)
W(REC, rec); W(RES, RESUME + R(RES)); W(WALK, R(WALK).rstrip('\n') + '\n' + MEMO); W(IDX, idx)
print('written: the map, the state doc, the recovery page, RESUME, the memory note, the index')
for p in (MAP, STATEDOC, REC, RES, WALK, IDX):
    r = subprocess.run([sys.executable, f'{ROOT}/logic/solo_tools/gloss_lint.py', p], capture_output=True, text=True); print('  lint', p.replace(ROOT, '<repo>').replace(MEM, '<memory>'), (r.stdout.strip().split('\n')[-1])[:60])
r = subprocess.run([sys.executable, f'{ROOT}/logic/solo_tools/scrub_home_paths.py', '--check'], capture_output=True, text=True); print('  home-path gate:', (r.stdout + r.stderr).strip().split('\n')[-1][:90])
