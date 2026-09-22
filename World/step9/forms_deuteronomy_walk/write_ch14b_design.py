import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE DEUTERONOMY WALK sitting 12b — THE COMPILE OF CHAPTER 14: THE DESIGN appended to the map at the close of RUN A, after the rereads and the measurements
# (ch14_compile_recon.py, ch14_docket_scan.py) and BEFORE any code — write_ch13b_design.py's form (the previous last section asserted, the section appended
# whole, the lint after). Every number below is read from the recon's and the scan's prints named beside it. RUN FROM THE REPO ROOT.
import os, re, subprocess
ROOT = _ROOT
P = f'{ROOT}/World/step9/DEUTERONOMY_WALK.md'
s = open(P, encoding='utf-8').read()
assert s.rstrip().split('\n## ')[-1].startswith('Sitting 12 — CHAPTER 14 — AS BUILT'), 'the previous last section is not sitting 12\'s AS BUILT'
assert '## Sitting 12b — THE COMPILE OF CHAPTER 14' not in s
SEC = '''


## Sitting 12b — THE COMPILE OF CHAPTER 14, Deuteronomy 14:1-29 (2026-09-21; the owner: "Go" after sitting 12's tail — the commit still on his word, sittings 11b and 12 uncommitted since fb797a1): THE DESIGN — written at the close of RUN A under THE COST RULES (two runs + the tail; the rereads: THE_STEPS' compiler block whole, Step 2's head and Step 5's head, the sitting-12 AS BUILT and the 12b box (a)-(o), the 11b design and AS BUILT as the compile's form; the measurements: ch14_compile_recon.py derived from 11b's by asserted line-based block substitutions (derive_ch14_recon.py — the forms folder's copy with its portable header stripped and ROOT from git restored; 40 s), ch14_docket_scan.py derived from 11b's (derive_ch14_docket_scan.py — chapter 13's folded line REMOVED, the export's chapter 14 the DB's; its first derive fell on the header block's suffix, retyped; 141 s) — all in the scratchpad) and BEFORE any code; THE DOCKET TWO RUNS by the ~700 clause (992 addresses in the dump; 288 credited by address at the scan; some 700 to read whole — the clean point after the first half UNCONDITIONALLY, sitting 12's lesson 1)

THE RUNS AND THE DOCKET'S OWN: RUN A the rereads, the measurements and this design — CLOSED HERE, a clean compaction point (#205); THE DOCKET by the union rule in
TWO RUNS — D1 the 144 link rows, Chullin 59a-66b (178 rows) and the ninety Mishnah rows (412 addresses); D2 the seventeen other folio ranges (Chullin 68a-69a,
72b-73a, 77a, 80a, 113a-116b; Makkot 20a-21a; Yevamot 13b-14a, 47b, 86a-b; Kiddushin 36a, 54b; Rosh Hashanah 12a-13a; Bekhorot 34a-35a, 53b; Pesachim 21b,
50b-51a; Bava Metzia 88a) with Tosefta Peah 4 and Tosefta Kilayim 1 (580 addresses; Tosefta Sanhedrin 3 EMPTY in the export — its rows 3:5-6 through the Sifrei's
citations read whole at the reading, 106:2 and 106:4), EVERY ROW WHOLE — the 288 credited rows CARRIED with their ledgers' own verdict lines (11b's form,
ch13_credit_carry.py derived), the uncredited read whole in chunk files (the cap 64,000 — 10b's D2 lesson), the writer derived from 11b's, coverage computed —
each run its own clean point; RUN B the probes to FAIL (readback Q37-Q39, BEFORE the types — 7b's lesson 2), the types by script with the docket's names, the
callees' facts printed before any assert (every CALL's ask read at the cell's own source — 10b's lesson 2), the runner in parts with the fast checker and the
generated CASES, the recorder with the cache OFF (7b's lesson 1) and the stitcher, the literals DF1-DF9, the tape to 10/10 with THE REST, checkpoint_check.py
--all AFTER the tape, the records writer and the copier WRITTEN, gates_chain.sh LAUNCHED in the background (the positions step at FOUR workers if the owner
rules it; eight the standing form), the clean point; THE TAIL after the compaction: the summary read once, the demands filed, the records from the sheet in one
call, the forms copied, this section's AS BUILT, the commit message for the owner's word.

THE MEASUREMENTS (what the tape, the runners, the registries and the running world say before a line is typed — ch14_recon.out, 535,054 bytes, read by its
seven sections): THE COUNTER stands at (40, 11, 1), day 908865 (the snapshot world: entities 319, log 3604); the tape's LAST LINES are chapter 13's four
own-day lines (word_sealed, prophet_test_declared, inciter_law_declared, condemned_city_law_declared) after chapter 12's four, its LAST MARKER the forward marker
at Deut 10:12 (M['speech_resumed_10']); RUN (1327, 96, 88, 0, 12, 1634, 44, 319, the four pairs, 127), PREVIOUS_RUN 10b's (1323, 96, 88, 0, 12, 1626, 43, 319,
the four pairs, 127); markers 172 (text_constrained 108, reading_placed 49), events text_constrained 110 / page_order 1159 / reading_placed 58; CENSUS (2520,
1319, 1327, 1185, 6, 10, 9, 0, 71, 172, 131, 15, 26, 872, 272); 68 runners, 73 daemons (installed_by boot 32, erected 3, covenant_blood_thrown 14,
called_from_the_tent 17, sentence_declared 2, statute_declared 2, milluim_blood_sprinkled 1, entered_the_land 1, pending 1), kinds 1155, effects 1056; the D
series DA, DB, DC, DD and DE in use (nine each) — THE NEXT NAME DF (no code assumes a letter; the two startswith seats are on strings); 68 spans, 669 edges,
208 pointers — NO pointer naming Deut 14, ONE EDGE naming it already: priesthood -> holiness_b (transfer, taught by Sifra Emor Chapter 1 1-3 and Makkot
20a:12-14 — "baldness-baldness: Leviticus 21:5 read with Deuteronomy 14:1 and Leviticus 19:27-28 both ways": THE CHAPTER'S FIRST VERSE IS A TEACHER'S SEAT
BEFORE ITS COMPILE); THE REGISTER: NO seat naming Deut 14 (the reading's finder found no receipt, header or footer; the two number verses 14:6 [2] and 14:28 [3]
no count lines); the readback probes Q1-Q36 on file (Q10 unused), the next Q37. THE KIN'S CELLS, FOUND BY THE REFS PER DEF: THE TWIN CHAPTER IS A CLASSIFIER —
shemini.classify (a dict of signs in: {'clazz': 'land', 'hoof': True, 'cud': True} as the sanctions engine calls it — PURE_BEAST; the water's fins and scales;
THE BIRD BLACKLIST by name, twenty in the ink; the camel "cud yes hoof no", the hare "counter-stated" in its own table — THE FOUR ARE THE CLASSIFIER'S OWN
EXCEPTION ROWS), shemini.touch_effect (carcass_touched -> impure_until_evening), law_shemini watching forbidden_kind_eaten -> lashes ("the ban layer; the
answer sheet: Makkot 3:2 lists the eaters of carcasses, terefot (torn), detestables and swarmers"); THE CARCASS'S BAN NAMED HERE BY THE LEVITICUS RUNNER —
sanctions.carcass('beast_carcass', 'effect', 'equality_test', 'failure', 'garments_boundary', 'impure_species', 'lashes_for_eating', 'minimum', 'pinching',
'slaughtered', 'where_defiles', 'who' — its lashed cell: "Makkot 3:2 — the eater of carcass and torn: THE BAN IS DEUT 14:21 / EXOD 22:30"; law_sanctions
watching carcass_eaten -> impure_until_evening, washes_and_bathes, defiles_garments, bears_sin, lashes, karet_cut_off (karet — excision)); THE KID'S CELL —
calendar.kid_in_milk('cook', 'eat', 'benefit' — each barred, barred_from_it at the case; its move: "the clause stands WRITTEN THREE TIMES (23:19, 34:26, Deut
14:21 — the census machine-verified in this run's probes): one for cooking, one for eating, one for benefit") and erection.repeats (34:26 the second seat,
across files); THE TORN — ordinances.torn('cannot_live', 'dogs_wage', 'field_common_case', 'fit_list', 'holy_men', 'lashes', 'to_the_dog', 'torn_seats';
law_ordinances watching flesh_torn -> torn_flesh_to_dogs, lashes); THE PRIESTS' BALDNESS — priesthood.family('gash_multiplier', 'hair_rend', 'corners' — "per
bald spot, the whole head (not only 'between the eyes', Deut 14:1), per gash"), THE CUTTINGS — holiness_b.body (19:27-28; the Makkot rows in its ink eleven);
THE GLEANINGS — holiness.gifts (19:9-10 — leket, olelet, the corner; left_for_the_poor the effect; ITS IMPORT TABLE NAMES THIS CHAPTER: GIFTS_IMPORT
{'forgotten_sheaf': 'Deut 24:19', 'forgotten_olive': 'Deut 24:20', 'poor_tithe': 'Deut 14:28'} — THE POOR TITHE POINTED AT 14:28 FROM LEVITICUS 19),
moadim.harvest_reaped (23:22 — barred_from_it); THE FIRST TITHE — korach.the_tithe ('liable_produce', 'exclusion_table', 'levite_he', 'levite_preceded',
'no_inheritance', 'recipients', 'removal', 'confession', 'mourner', 'every_place', 'agent' … — Numbers 18:20-32; portion_declared and
tithe_of_the_tithe_commanded ON THE TAPE; tithe_granted and inheritance_barred the Levites' entries; "Rosh Hashanah 12b:3 — the first tithe juxtaposed to an
inheritance — no interruption in the third year" ALREADY A MOVE THERE; the tithe thresholds by Bava Metzia 88a a DATA row there), korach.the_gifts (the
firstling — Bekhorot 109 lines); THE HERD'S TITHE — temurah.tithe (27:32 — 'not_a_tithe': the tenth an ordinal, not a proportion), temurah.redeem; THE
CYCLE — yovel.cycle, yovel.sabbatical, yovel.tithe_naming, calendar.sabbatical (the seventh year's timer on the land); THE HOLY PEOPLE —
seven_nations.the_holy_people (7:6 — 'the_oath', 'brought_out_redeemed'; treasured_people ON FILE ONCE at Exod 19:5, a HEAVEN entry — CQ5's literal ONE
UNMOVED; nations_devoted on the tape at 7:1-5); THE LEVITE AND THE FOUR — second_tablets.the_levites_separated (10:9 — no portion) and
.the_god_of_gods_and_the_stranger (10:18 — stranger_love_commanded on the tape, love_owed the effect); THE PLACE — place_name.the_place_chosen (12:5-14 —
place_chosen_required, rejoicing_before_the_lord_commanded, high_places_banned ON FILE), .the_profane_slaughter_the_blood_and_the_gates (12:15-19 — the gazelle
and the hart; holy_things_in_the_gates_barred (the tithe in the gates) and levite_forsaking_barred ON FILE), .the_border_enlarged_and_the_altar (12:20-28 —
12:21's far clause); THE FIRST SEATS OF THE TENTH — primeval (tithe_given Gen 14:20 ON THE TAPE, a TRANSFER; olah_offered Gen 8:20 with 7:2's clean beasts),
mamre.bethel (vowed Gen 28:20-22 ON THE TAPE; tithe_vowed the DEBIT on Jacob). THE REGISTRY: 'the-levites' mapped to the_levites (THE TRUE MATCH — the tithe's
recipients), 'the-place' to the_place_luz_bethel (JACOB'S PLACE — a homograph, FALSE if the census matches it), 'the-raven' to the_raven (Noah's), 'the-flock'
to the_flock (Jacob's), 'the-beasts' to the_beasts (Noah's), 'the-people' to israel_people; NO registry row for the-levite, the-sojourner, the-stranger,
the-fatherless, the-widow, the-ox, the-sheep, the-goat, the-kid, the-carcass, the-tithe, the-firstlings, the-herd, the-money, the-gates — the chapter's persons
are the exam's, no entity; the daemon's writes on israel_people alone. THE KINDS AND EFFECTS ON FILE touching the matter: kid_boiled_in_milk (case — three
seats), carcass_eaten (case — 17:15), carcass_touched (case — Lev 11), forbidden_kind_eaten (case — shemini's), flesh_torn (case — 22:30), herd_tithed (case —
27:30-33), tithe_case (Num 18), tithe_given (act — Gen 14:20), tithe_of_the_tithe_commanded, harvest_reaped (case — 19:9, 23:22), firstling_born (case),
profane_slaughter_permitted (statute — 12:15-19), place_chosen_declared, stranger_love_commanded (statute — 10:17-19), stranger_wronged (case — Exod
22:20-23), hearing_blessed, nations_devoted; the effects levite_forsaking_barred (block, ONE — 12:19), rejoicing_before_the_lord_commanded (status, ONE —
12:7), profane_slaughter_permitted (status), holy_things_in_the_gates_barred (block — the tithe in the gates), tithe_granted (status on the Levites),
inheritance_barred, tithe_given (transfer), tithe_vowed (debit), terumah_of_the_tithe_owed (status), torn_flesh_to_dogs (transfer), treasured_people (heaven,
ONE), left_for_the_poor, barred_from_it, impure_until_evening, lashes, love_owed, same_day_slaughter_barred, stranger_barred (the terumah's) — and NO effect
naming the cuttings or the baldness for the dead, the abomination's eating, the carcass's eating (the ban the sanctions engine names at 14:21 has no effect of
its own), the second tithe or the poor man's tithe (the five names asserted absent from both registries at the design; rejoicing_before_the_lord_commanded and
levite_forsaking_barred present ONCE each). THE DOCKET SCAN (ch14_docket_scan.out; the dump ch14_docket_dump.txt 636,447 bytes, 2,978 lines): 144 LINK rows in
38 works (Chullin 30, Bekhorot 13, Kiddushin 9, Makkot 9, Bava Kamma 7, Bava Metzia 7, Pesachim 7, Shabbat 5, Eruvin 4, Nedarim 4, Yevamot 4, Zevachim 4,
Avodah Zarah 3, Menachot 3, Rosh Hashanah 3, Sukkah 3, Temurah 3, Yoma 3, Keritot 2, Shevuot 2, Tosefta Bekhorot 2, one each in seventeen more), the verses
cited 14:21 the most (32 rows — the kid and the carcass), 14:25 (19), 14:23 (18), 14:22 and 14:26 (17), 14:1 (12), 14:24 (10); NOT CITED BY ANYONE 14:9 and
14:14-18 (the water's permission and the birds' names); 817 TOPIC rows (Chullin 59a-66b 178, 68a-69a 62, 72b-73a 32, 77a 16, 80a 21, 113a-116b 135; Makkot
20a-21a 43; Yevamot 13b-14a 42, 47b 19, 86a-b 23; Kiddushin 36a 22, 54b 16; Rosh Hashanah 12a-13a 39; Bekhorot 34a-35a 51, 53b 17; Pesachim 21b 11, 50b-51a
24; Bava Metzia 88a 9; the ninety Mishnah rows — Chullin 8, Makkot 2, Maaser Sheni 57 (the five chapters whole), Maasrot 5, Temurah 1, Eduyot 1, Zevachim 1,
Peah 5, Bekhorot 8 (chapter 9 whole — the cattle tithe), Avot 2); Tosefta Peah 4 (20 rows), Tosefta Kilayim 1 (11 rows), Tosefta Sanhedrin 3 EMPTY; 992
addresses, 288 CREDITED BY ADDRESS — chapter 12's docket 157 (Chullin 113a-116b 118 of 135: FLESH IN MILK READ WHOLE AT 10b, its rows carried), the Korach
docket 28, the Exodus triage 27, chapter 10's 21, the priesthood docket 17, the Genesis triage 17, the ordinances docket 12, the leaven block 9, the
holiness_b docket 9 and the rest; the Mishnah rows credited: Bekhorot 9:1-8, Chullin 3:6-7, 8:1-4, Maaser Sheni 3:8 and more — some 700 rows to read whole: TWO
DOCKET RUNS.

THE NAME: cold_run_food_tithe.py — the 69th runner (the food laws and the tithes of chapter 14 — the sons and the cuttings, the beasts, the water and the birds,
the carcass and the kid, the second tithe, the third year's tithe; the unit deu_14_food_tithe); the daemon law_food_tithe, given_at Deut 14:1, installed_by boot
(the Deuteronomy daemons' form; THE INSTALL HYPOTHESIS on the table unchanged); seven cells F1-F7 on the seven claims' spans (14:1-2, 3-8, 9-20, 21, 22-23,
24-27, 28-29) and the_readback — EIGHT WRAPPED (10b's lesson 4: the functions block counts what the daemon wraps).

THE READBACK ON THIS CHAPTER — THE FORMS ON FILE, NO NEW FORM: chapter 14 is law from its first word to its last (Moses' voice, no act, no divine frame, no
"if" — the one case on "and when" at 14:24), so its twenty-nine rows are T4 rows graded against the cells that compile their kin, by CALL (14:1 against
Leviticus 19:27-28 and 21:5; 14:2 against 7:6; 14:3-20 against Leviticus 11 — THE TWIN CHAPTER, verse by verse; 14:21 against Leviticus 17:15, 22:8, Exodus
22:30 and the kid's 23:19, 34:26; 14:22-23 against Numbers 18:21-24, Leviticus 27:30 and 12:6, 12:17-18; 14:24 against 12:21; 14:26 against 12:7; 14:27
against 12:19 and 10:9; 14:28-29 against Leviticus 19:9-10, 23:22 and 10:18) and T1 reference rows against the tape's lines by kind and first verse
(tithe_given Gen 14:20 — Abram's tenth, the word's first seat; vowed Gen 28:20-22 — Jacob's tithe vowed, the debit OPEN; olah_offered Gen 8:20 — 7:2's clean
beasts, the word's first seat; covenant_offered Exod 19:5-6 — the treasured people; portion_declared Num 18:20-24 and tithe_of_the_tithe_commanded Num
18:25-32; nations_devoted Deut 7:1-5 — 7:6's holy people; stranger_love_commanded Deut 10:17-19; place_chosen_declared Deut 12:5 and
profane_slaughter_permitted Deut 12:15 — the gazelle and the hart, the tithe in the gates barred, the Levite kept); NO tape line for Leviticus 11, 17, 19,
21-23 or 27 nor for Exodus 22:30, 23:19 or 34:26 — THE TENT'S LAWS ARE INSTALLED BY CALL, NOT WRITTEN AS LINES (their cells by CALL); NO retrograde marker, NO
act told only here, NO T2 row, NO state row; the run's cases OUTSIDE THE TAPE (Solomon's table — 1 Kings 5:3, 14:5's one kin in the Bible; Samaria's fall at the
end of three years — 2 Kings 18:10, 14:28's kin; Amos 4:4's tithes; Nehemiah's storerooms — 10:38-39, 13:5-12; Hezekiah's tithes — 2 Chronicles 31:5-12;
Malachi 3:8-10; the swine's flesh — Isaiah 65:4, 66:17; Ezekiel's carcass — 4:14, 44:31; Samuel's tenth — 1 Samuel 8:15-17; Ruth's gleaning) DATA rows; THE
CODE'S HOLES compiled at the chapter's own day (40, 11, 1), NO marker, after the tape's last Deut 13 line (condemned_city_law_declared): (a) THE SONS AND THE
CUTTINGS (14:1-2), (b) THE FOOD LAW (14:3-20 — the beasts, the water, the birds), (c) THE CARCASS AND THE KID (14:21), (d) THE SECOND TITHE with the far place,
the money, the rejoicing and the Levite (14:22-27), (e) THE THIRD YEAR'S TITHE (14:28-29). THE DECISIONS (the design's, open to the owner's word; the docket to
confirm the names — 7b's lesson 7): (1) THE SONS AND THE CUTTINGS — sons_and_mourning_declared writes cuttings_for_the_dead_barred, a NEW BLOCK on
israel_people (14:1 "you shall not cut yourselves nor make baldness between your eyes for the dead" — 96:10 the cut, 96:12 the baldness by the analogy run both
ways with the priests' 21:5 (I2 — the whole head, not only between the eyes; per spot: priesthood.family('gash_multiplier', 'corners') by CALL; Mishnah Makkot
3:5-6 and Makkot 20a-21a at the docket — the lashes' count and "for the dead" the conditions), 19:27-28's cuttings by CALL (holiness_b.body); THE SECOND
READING "no factions" (96:10-11 — lo titgodedu read as "do not make yourselves into factions": Yevamot 13b-14a at the docket) INSIDE THE VALUE as a derived law
beside the plain one, no parameter — both hold; "sons of the LORD" (14:1 — 96:9: sons when you act as sons, or sons either way — R. Meir; Kiddushin 36a at the
docket) a DATA row and the exam's persons; 14:2 the ground — seven_nations.the_holy_people by CALL (7:6 VERBATIM in kind — eighteen of nineteen tokens by the
reading's computation; treasured_people ON FILE ONCE at Exod 19:5, a HEAVEN entry UNMOVED — no write here: the reason clause, not a law). (2) THE FOOD LAW —
food_law_declared writes abomination_eating_barred, a NEW BLOCK on israel_people (14:3 "you shall not eat any abomination" — 99:1-2: what I have made abominable
for you; the general clause over the whole list; Chullin 114b-115a at the docket for the abomination's reach) — THE TWIN CHAPTER'S CELLS BY CALL
(shemini.classify on the signs — the beasts' two, the water's two, the birds by name; carcass_touched by CALL for 14:8's "their carcass you shall not touch");
THE CHAPTER'S GAIN OVER LEVITICUS 11 inside the value: THE TEN NAMED CLEAN BEASTS (14:4-5 — the three domestic and the seven wild: 100:1-2; nowhere else in the
Torah; Chullin 59a-b at the docket — the wild beast's horn signs for the fat and the blood, the shesuah (the cleft one, 98:2 — Chullin 60b: a creature of its own
kind) a DATA row), THE PERMISSION FOR THE CLEAN BIRD (14:11, 14:20 — Leviticus 11 has no "you may eat" for the birds: 103:1) with THE PARAMETER the_birds_signs
FROM THE ANSWER SHEET (103:8 — Mishnah Chullin 3:6 in the row's own Hebrew: the extra toe, the crop, the peelable gizzard, not a clawer; Chullin 59a, 61a-65a at
the docket — a bird is clean by signs where the Torah names only the unclean: THE CODE/DATA SEPARATION LAW'S OWN CASE, the value DATA), THE TWO NAMES ADDED
(the ra'ah for Leviticus's da'ah — 98:5-6, Chullin 63b: one bird two names; the dayyah — 98:6 "the whole gain of the restatement") DATA rows, the locusts
absent here (Leviticus 11:21-22 by CALL — 103:10 the frames); THE FOUR (14:7-8) the written exception set — the classifier's own rows by CALL, the four named
the exception and the sign the class (101:10 — I1); the lexicon rule "bird = clean" (98:3; 228:5 — I3) and the counting rule (100:2, 103:7) DATA rows; the
altar's disqualified by the names (101:1-9 — Mishnah Temurah 6:1) and the afterbirth (101:7 — Chullin 68a-69a, 77a) DATA rows; the exam's rows through
forbidden_kind_eaten (shemini's case kind REUSED — lashes at the case; Makkot 3:2's list a DATA row) and the chapter's own case kind food_tithe_case. (3) THE
CARCASS — carcass_and_kid_declared writes carcass_eating_barred, a NEW BLOCK on israel_people (14:21 "you shall not eat any carcass; to the sojourner in your
gates you may give it that he eat it, or sell it to a foreigner" — THE BAN'S SEAT NAMED BY THE SANCTIONS ENGINE ITSELF: its lashed cell reads "the ban is Deut
14:21 / Exod 22:30"; Leviticus 17:15's carcass_eaten the impurity's case by CALL, 22:8's priest by CALL (priesthood.holy_food), Exodus 22:30's flesh_torn by
CALL (ordinances.torn — torn_flesh_to_dogs the TRANSFER); "any carcass" the torn included — 104:1, Chullin 72b-73a, Mishnah Chullin 4:4 — inside the value); THE
FOUR-CELL TABLE A PARAMETER the_carcass_table with two arms (104:5-6 — giving and selling over the resident alien and the foreigner: the Sages either to
either, R. Judah "as written" — Pesachim 21b at the docket); the resident alien (104:2 — Onkelos "the uncircumcised sojourner": THE SOJOURNER'S FIRST PERSON)
and the custom's bar (104:7 — Pesachim 50b-51a) DATA rows. (4) THE KID — NO NEW WRITE: kid_boiled_in_milk the CASE KIND ON FILE (written three times — the
census machine-verified at the calendar's compile) and calendar.kid_in_milk('cook', 'eat', 'benefit') THE CELL by CALL (barred on all three; barred_from_it at
the case; 34:26 through erection.repeats by CALL) — THE THIRD SEAT'S GAIN IS THE ASSIGNMENT: the three covenants (104:8, reread whole), R. Akiva's three
exclusions — the wild beast, the fowl, the unclean (104:9; Mishnah Chullin 8:4; Chullin 113a-116b — 118 of its 135 rows credited from chapter 12's docket and
CARRIED, the seventeen read whole at D2), the fowl out by "its mother's milk" (104:10), the eating from 12:24's clause (76:7 — I1; Chullin 115b) — the cell
asserts the three seats on the DB and reads the three verdicts from the calendar's cell: DATA rows; the exam's rows through kid_boiled_in_milk by CALL. (5)
THE SECOND TITHE — second_tithe_declared writes second_tithe_owed, a NEW STATUS on israel_people (14:22-23 "tithe, you shall tithe all the yield of your seed …
and you shall eat before the LORD your God in the place which He will choose … the tithe of your grain, your wine and your oil, and the firstlings of your herd
and your flock, that you may learn to fear the LORD your God all the days" — NAMED THE SECOND BY THE SHELF, 105:2; Numbers 18's first tithe by CALL —
korach.the_tithe: tithe_granted ON FILE on the Levites UNMOVED, Q33's literal unmoved); THE LIABILITIES FROM THE VERSE'S CLAUSES inside the value (105:1-19 —
"the yield of your seed" what grows from seed, "the field" what goes out to the field, "year by year" no tithing from one year for another: Mishnah Maasrot 1:1,
1:3, 2:4, 4:5-6; Rosh Hashanah 12b; Bekhorot 53b; Bava Metzia 88a's courtyard — korach.the_tithe('liable_produce') by CALL; Leviticus 27:30 by CALL
temurah.tithe); THREE CONDITIONS FOR THE EATING inside the value, each from its row — the wall of Jerusalem (106:3 — I1 with the lesser holies; Mishnah Zevachim
5:8), the House standing (106:4 — the juxtaposition with the firstling, no code; Tosefta Sanhedrin 3:6 through the Sifrei's note), the year passed no bar
(106:5, reread whole); the firstling at 14:23 by CALL (ordinances.firstling; korach.the_gifts; Bekhorot 34a-35a at the docket) a DATA row; the firstling from
outside the Land not brought (106:2 — Tosefta Sanhedrin 3:5; 15:19-23 ahead by CALL when it comes) a DATA row; "that you may learn to fear" (106:6 — the study)
the effect's ground. (6) THE FAR PLACE, THE MONEY AND THE SPENDING (14:24-26) — inside second_tithe_declared's value and writes: THE FAR PLACE of place not time,
any distance, the rich too (107:1-3; 12:21's clause by CALL place_name.the_border_enlarged_and_the_altar — twelve tokens in order by the reading's computation)
a DATA row; THE MONEY'S FORM A PARAMETER the_moneys_form with two arms (107:4 — I1 "and bind up the money in your hand": money with a form — coined, not
uncoined; Mishnah Maaser Sheni 1:2 the coin; Mishnah Eduyot 3:2's arm — the docket decides the values); the possession (107:5 — "in your hand": one's own) a
DATA row; Shiloh and the eternal House (107:6 — the eras table by CALL place_name.the_place_chosen) a DATA row; THREE MONEYS THE LAW'S TABLE (107:7 — I1;
Mishnah Maaser Sheni 3:10) a DATA row; THE CLASS FROM THE FOUR NAMED (14:26 — cattle, sheep, wine, strong drink: 107:8-11, I3 — fruit from fruit, growing from
the ground, whose keeping is by the land: Mishnah Maaser Sheni 1:5, 1:7, 2:1) inside the value; the containers (107:12-15 — Mishnah Maaser Sheni 1:3; Mishnah
Chullin 1:7) DATA rows; THE REJOICING — rejoicing_before_the_lord_commanded REUSED, a SECOND ENTRY on israel_people (12:7's the first; 14:26 "and you shall
rejoice, you and your household" — 107:16: I2 with 27:7 ahead, the rejoicing peace offerings; DD2's count literal ONE and Q32's tuple MOVE — retyped from the
print BEFORE the tape, 8b's and 10b's lesson: the grep at RUN B decides the list). (7) THE LEVITE (14:27) — levite_forsaking_barred REUSED, a SECOND ENTRY on
israel_people (12:19's the first; 14:27 "the Levite who is in your gates, you shall not forsake him, for he has no portion or inheritance with you" — 108:1 THE
LADDER OF FOUR: a status with four sources — 10:9 by CALL second_tablets.the_levites_separated, 12:12 and 12:19 by CALL place_name, Numbers 18:20-24 by CALL
korach (portion_declared on the tape; inheritance_barred and tithe_granted the Levites' entries UNMOVED), 14:29 the fourth; DD2's and DD4's literals and Q32's
tuple MOVE). (8) THE THIRD YEAR — third_year_tithe_declared writes poor_tithe_owed, a NEW STATUS on israel_people (14:28-29 "at the end of three years you shall
bring out all the tithe of your yield in that year and lay it up within your gates; and the Levite … and the sojourner and the fatherless and the widow who are
in your gates shall come and eat and be satisfied, that the LORD your God may bless you in all the work of your hand" — ONE TITHE NOT TWO: the poor man's
replaces the second in the third and the sixth year, 109:5, 109:10-11; Numbers 18:21's first tithe by CALL, unmoved); THE REMOVAL'S DATE A CLOCK DATUM — THE
PARAMETER the_removal_date (109:1-3 — the eve of the last festival day of Passover of the fourth and the seventh year: Mishnah Maaser Sheni 5:6; I2 "at the
end" with 31:10 ahead; 26:12 ahead — the docket confirms the arms), the years by CALL to the sabbatical cycle (yovel.cycle, yovel.sabbatical, calendar.sabbatical
— the seventh year exempt: 109:4, Exodus 23:10-11 through its spine; 15:1 ahead: THE CELL READS THE COUNT'S YEAR FROM THE CYCLE, never a constant); THE TITHES'
NEW YEAR A CLOCK DATUM — THE PARAMETER the_tithes_new_year (109:8 — the vegetables' year; Rosh Hashanah 12a-13a at the docket: the first of Tishri for grain and
legumes, the fifteenth of Shevat for the tree — Mishnah Rosh Hashanah 1:1's four new years; the docket decides); the gifts exempt (109:12 — Leviticus 19:9-10
and 23:22 by CALL holiness.gifts and moadim: left_for_the_poor; THE LEVITICUS RUNNER'S IMPORT TABLE ALREADY POINTS AT 14:28 — a REVERSE edge candidate the
census decides) a DATA row; THE FOUR IN WANT (110:1-2 — I3: the Levite, the sojourner, the fatherless, the widow; the measures at the threshing floor — Mishnah
Peah 8:5-9 with Tosefta Peah 4:2, 4:11: half a kav of wheat, a kav of barley …) DATA rows and the exam's persons; THE SOJOURNER TWO PERSONS (14:21's resident
alien, 14:29's convert — 110:2; Onkelos "the convert" against 14:21's "the uncircumcised"; Yevamot 47b, 86a-b at the docket — the convert eats the poor man's
tithe, the resident alien the carcass: THE CELL READS THE NOUN BY ITS SEAT, no parameter; a DATA row and two exam persons); the storing within the gates
(14:28 — the tithe left for the poor to come, 109:9) inside the value; the blessing on the work of the hand (14:29) the effect's ground (the confession at
26:12-14 ahead by CALL when it comes). (9) THE REGISTER — NO seat in chapter 14 (the reading's finder: no receipt, no header, no footer; the two number verses
14:6 [2] and 14:28 [3] no count lines — census probe rows if the form asks); DECLARED 98 UNMOVED — a second daemon given inside the block (Deut 12:1, Deut
28:69] moves nothing (11b's lesson 2: both declarations on that block are gone, the header and the footer DAEMONS already); the gate --strict GREEN expected.
(10) THE HOMOGRAPHS — the_place_luz_bethel (Jacob's place at 'the-place'), the_raven (Noah's), the_flock and the_beasts (Jacob's, Noah's): each filed FALSE with
its why IF the census matches (the census decides); the_levites the TRUE match (the tithe's recipients — the value's object, the write on israel_people). (11)
THE INSTRUMENT'S SLIPS AS DATA — the parser's [2] at 14:6 (the two hoofs) and [3] at 14:28; the ra'ah's resh against Leviticus 11:14's da'ah's dalet (the twin
diffed verse by verse — the reading's lesson 6) a DATA row; the register's DATA rows (the food laws plural, the tithe singular, 14:21 both; no imperative; no
"if"; the one "and when" at 14:24; no first person; no narrative verb; the starred tithe tokens; no written/read pair). (12) THE KIN BY CALL — EIGHTEEN CALL edges
predicted: shemini, sanctions, calendar, erection, ordinances, priesthood, holiness, holiness_b, moadim, temurah, korach, yovel, seven_nations, second_tablets,
place_name, primeval, mamre, seducers (13:1's word sealed — the header of the block both chapters sit in, if the census asks) — the census decides; NO pointer
predicted (14:23-25's "the place which the LORD your God will choose" the formula's fourth and fifth seats — place_name by CALL, the formula the cell's own; no
AS_WHEN form in the chapter); the priesthood -> holiness_b edge on file names Deut 14:1 already — a teacher's seat before the compile, a DATA row.

THE ROWS (twenty-nine predicted, one per verse; the grades' census typed from the runner's print at RUN B): 14:1 "sons you are to the LORD your God; you shall
not cut yourselves nor make baldness between your eyes for the dead" — THE LINE sons_and_mourning_declared; holiness_b.body (19:27-28) and priesthood.family
(21:5) by CALL: SUPPLIED AS A LAW (the first seat of the cutting's bar for all Israel; "between your eyes" the frontlets' clause 6:8, 11:18 — a DATA row; 96:9's
sonship, 96:10-11's two readings, 96:12's analogy both ways); 14:2 "for you are a holy people to the LORD your God, and the LORD has chosen you to be His
treasured people from all the peoples on the face of the earth" — nations_devoted (Deut 7:1) by kind for 7:6, covenant_offered (Exod 19:5) by kind,
seven_nations.the_holy_people by CALL: VERBATIM in kind (7:6 eighteen of nineteen tokens; 97:1-5 — the holiness your own and your fathers', the chosen, the
treasured); 14:3 "you shall not eat any abomination" — THE LINE food_law_declared: SUPPLIED AS A LAW (the one clause; 99:1-2 what I made abominable for you;
Chullin 114b at the docket); 14:4 "this is the beast which you may eat: the ox, the sheep and the goat" — shemini.classify by CALL: VARIANT (Leviticus 11:2-3
without the names; 100:1 the three domestic); 14:5 "the hart, the gazelle, the roebuck, the wild goat, the ibex, the antelope and the mountain sheep" —
place_name (12:15's gazelle and hart) by CALL: SUPPLIED (the seven wild beasts nowhere else in the Torah — Solomon's table 1 Kings 5:3 the one kin in the Bible
a DATA row; 100:2 the count; Chullin 59a-b the wild beast's signs); 14:6 "and every beast that parts the hoof and has the hoof cloven in two and chews the cud
among the beasts, it you may eat" — shemini.classify by CALL: VARIANT (11:3 with "two" — the parser's [2]; 98:1 the three signs from the three clauses; 101:1-9
the altar's disqualified); 14:7 "but these you shall not eat of those that chew the cud or part the cloven hoof: the camel, the hare and the coney — for they
chew the cud but do not part the hoof; they are unclean for you" — shemini.classify by CALL: VARIANT (11:4-6's three folded into one; THE FOUR the written
exception set — 101:10 I1); 14:8 "and the swine, because it parts the hoof but does not chew the cud, it is unclean for you; of their flesh you shall not eat,
and their carcass you shall not touch" — carcass_touched by CALL (shemini.touch_effect): VERBATIM in kind (11:7-8; 102:1 the touch); 14:9 "these you may eat of
all that are in the waters: all that have fins and scales you may eat" — shemini.classify by CALL: VARIANT (11:9's twelve of twelve with the seas and the
rivers dropped; NOT CITED BY ANYONE on the shelf); 14:10 "and whatever has not fins and scales you shall not eat; it is unclean for you" — by CALL: VARIANT
(11:10-12 shortened, "unclean for you" for "detestable"; Chullin 66a-b at the docket); 14:11 "every clean bird you may eat" — THE PARAMETER the_birds_signs:
SUPPLIED (the permission Leviticus lacks — 103:1; 103:8 the answer sheet's four signs); 14:12 "and these are they of which you shall not eat: the eagle, the
vulture and the osprey" — by CALL: VARIANT (11:13's three; 103:3-4 the list carried by its head — I2); 14:13 "the glede, the kite and the falcon after its kind"
— by CALL: VARIANT (the ra'ah for the da'ah, the dayyah added — 98:5-6, Chullin 63b); 14:14 "and every raven after its kind" — by CALL: VERBATIM in kind
(11:15; the_raven the registry's homograph — Noah's); 14:15 "and the ostrich, the nighthawk, the seagull and the hawk after its kind" — by CALL: VERBATIM in kind
(11:16 to the letter — the reading's diff); 14:16 "the little owl, the great owl and the horned owl" — by CALL: VARIANT (11:17-18's order); 14:17 "the pelican,
the carrion vulture and the cormorant" — by CALL: VARIANT (11:17-18); 14:18 "the stork, the heron after its kind, the hoopoe and the bat" — by CALL: VERBATIM in
kind (11:19); 14:19 "and every swarming winged thing is unclean for you; they shall not be eaten" — by CALL: VARIANT (11:20 — "unclean" for "detestable"; the
locusts 11:21-22 absent here, by CALL — 103:10 the frames); 14:20 "every clean fowl you may eat" — by CALL: SUPPLIED (the second permission — 103:9-10; 228:5 the
lexicon rule); 14:21 "you shall not eat any carcass; to the sojourner in your gates you may give it that he eat it, or sell it to a foreigner, for you are a holy
people to the LORD your God; you shall not boil a kid in its mother's milk" — THE LINE carcass_and_kid_declared; carcass_eaten (Lev 17:15) by CALL
(sanctions.carcass), priesthood.holy_food (22:8) and ordinances.torn (Exod 22:30 — flesh_torn) by CALL, kid_boiled_in_milk by CALL (calendar.kid_in_milk — THE
THIRD SEAT): EXPANDED (THE FOUR-CELL TABLE 104:5-6; the resident alien 104:2; the custom's bar 104:7; the three covenants 104:8; R. Akiva's three exclusions
104:9; the fowl out 104:10; 76:7 the eating — the chapter's most-cited verse, 32 link rows); 14:22 "tithe, you shall tithe all the yield of your seed that
comes out of the field year by year" — THE LINE second_tithe_declared; korach.the_tithe by CALL, temurah.tithe by CALL: SUPPLIED AS A LAW (the second tithe's
first seat — the doubled verb; the starred tokens; 105:1-19 the liabilities); 14:23 "and you shall eat before the LORD your God in the place which He will
choose to make His name dwell there, the tithe of your grain, your wine and your oil, and the firstlings of your herd and your flock, that you may learn to fear
the LORD your God all the days" — place_chosen_declared (12:5) by kind, place_name.the_place_chosen and .the_profane_slaughter_the_blood_and_the_gates (12:6,
12:17-18) by CALL, ordinances.firstling by CALL: EXPANDED (the place formula's fourth seat; 106:1-6 the three conditions and the firstling; "learn to fear" one
seat); 14:24 "and when the way is too long for you, so that you cannot carry it, because the place is too far from you which the LORD your God will choose to
put His name there, when the LORD your God blesses you" — place_name.the_border_enlarged_and_the_altar (12:21) by CALL: VARIANT (12:21's clause twelve in
order; 107:1-3 the far place; THE ONE "AND WHEN" of the chapter); 14:25 "then you shall turn it into money, and bind up the money in your hand, and go to the
place which the LORD your God will choose" — THE PARAMETER the_moneys_form: SUPPLIED (the money's first seat; 107:4-7; 19 link rows); 14:26 "and you shall
spend the money for whatever your soul desires, for cattle or sheep, for wine or strong drink, or whatever your soul asks of you; and you shall eat there before
the LORD your God and rejoice, you and your household" — rejoicing_before_the_lord_commanded (12:7) REUSED, place_name.the_place_chosen by CALL: EXPANDED
(the class from the four named 107:8-11 — I3; the containers 107:12-15; 107:16 the rejoicing peace offerings — I2 with 27:7); 14:27 "and the Levite who is in
your gates, you shall not forsake him, for he has no portion or inheritance with you" — levite_forsaking_barred (12:19) REUSED, second_tablets (10:9) and
korach (Num 18:20-24 — portion_declared by kind) by CALL: VERBATIM in kind (12:19's clause; 108:1 the ladder of four); 14:28 "at the end of three years you
shall bring out all the tithe of your yield in that year, and lay it up within your gates" — THE LINE third_year_tithe_declared; THE PARAMETERS the_removal_date
and the_tithes_new_year; yovel.cycle by CALL: SUPPLIED AS A LAW (the third year's first seat; the parser's [3]; 109:1-12 — the date, the seventh year, one tithe
not two, the vegetables' year, the gifts exempt; Samaria's fall 2 Kings 18:10 the closest verse a DATA row); 14:29 "and the Levite, because he has no portion
or inheritance with you, and the sojourner and the fatherless and the widow who are in your gates shall come and eat and be satisfied, that the LORD your God
may bless you in all the work of your hand which you do" — stranger_love_commanded (Deut 10:17) by kind, second_tablets.the_god_of_gods_and_the_stranger
(10:18) and holiness.gifts (19:9-10) by CALL: EXPANDED (14:27's clause seven tokens in order — the chapter's own closest kin; 24:19's clause ahead; 110:1-4 the
four in want, the convert, the measure, the Land; the blessing). THE HOLES: FIVE IN THE CODE compiled at the chapter's own day (the sons and the cuttings; the
food law; the carcass and the kid; the second tithe; the third year); NONE told only here; no pointer; no state row; no retrograde marker.

THE CELLS (F1-F7 + the_readback; every token probed; effects on every cell; the exam's rows the docket's crowns): F1 THE SONS AND THE CUTTINGS (14:1-2): the
line and its one write; the exam: Mishnah Makkot 3:5-6 with Makkot 20a-21a (the baldness — how many bald spots, how many lashes; the cuttings for the dead;
"between your eyes" the whole head), Yevamot 13b-14a (no factions — the two courts in one town; Beit Shammai and Beit Hillel), Kiddushin 36a (sons of the
LORD — R. Judah and R. Meir), Avot 3:14 (beloved are Israel, called sons — the link row), Leviticus 19:27-28's and 21:5's cells by CALL (the Sifra credited
from their sittings). F2 THE BEASTS (14:3-8): the line and its one write; the exam: Mishnah Chullin 3:6-7 with Chullin 59a-66b (the signs of the beasts, the
wild beast's horns, the four, the shesuah (the cleft one), the fish's signs, the birds' signs, the locusts — 178 rows, 18 credited), Mishnah Temurah 6:1 (the
altar's disqualified by the names — 101:1-9), Chullin 68a-69a (the afterbirth — 101:7), Chullin 77a (the afterbirth's rows), Chullin 80a (the koy — a doubtful
kind; Tosefta Kilayim 1:9), Bekhorot 34a-35a (the firstling's blemish — 14:23's firstling), Mishnah Bekhorot 9 with Bekhorot 53b (the cattle tithe — 27:32's
kin by CALL). F3 THE WATER AND THE BIRDS (14:9-20): the parameter the_birds_signs; the exam: Chullin 59a and 61a-65a inside F2's range (the signs of a clean
bird — the extra toe, the crop, the peelable gizzard, the clawing; the ra'ah and the dayyah; the twenty-four unclean birds; the locusts' four signs), Chullin
66a-b (fins and scales — a fish with scales has fins), Mishnah Chullin 3:7 (the locusts). F4 THE CARCASS AND THE KID (14:21): the line and its one write; the
parameter the_carcass_table; the exam: Pesachim 21b (the carcass to the alien — the table; R. Judah), Chullin 72b-73a with Mishnah Chullin 4:4 (the torn and the
fetus — "any carcass"), Pesachim 50b-51a (the custom's bar — the place's custom), Mishnah Chullin 8:1-4 with Chullin 113a-116b (meat in milk — the three
readings, the fowl, the beast's and the wild's milk, the cooking's and the eating's warnings; 118 rows carried from chapter 12's docket), Leviticus 17:15's,
22:8's and Exodus 22:30's cells by CALL. F5 THE SECOND TITHE (14:22-23): the line and its one new write; the exam: Mishnah Maasrot 1:1, 1:3, 2:4, 4:5-6 (the
liabilities — what is food, guarded, grows from the ground; the courtyard; the seasons), Mishnah Maaser Sheni 1-2 (the tithe's sanctity — not sold, not
pledged, not weighed; the money; the produce), Mishnah Zevachim 5:8 (the wall — the second tithe eaten within the wall), Kiddushin 54b (the second tithe
Heaven's property — R. Meir; the docket's link rows), Rosh Hashanah 12a-13a (the tithe's year — grain, legumes, vegetables, the tree; the fifteenth of Shevat),
Bekhorot 53b (the cattle tithe's years), Bava Metzia 88a (the liability by the courtyard — the pile smoothed, the skimming, the trough: korach's rows), Yevamot
86a-b (the first tithe to the Levite — Ezra's penalty; the poor tithe to the priest), Numbers 18's and Leviticus 27's cells by CALL. F6 THE FAR PLACE, THE MONEY,
THE REJOICING AND THE LEVITE (14:24-27): the two reuses; the parameter the_moneys_form; the exam: Mishnah Maaser Sheni 1:2 (coined money), 1:3 (the
containers), 1:5, 1:7, 2:1 (the class from the four — cattle, sheep, wine, strong drink; not water, not salt), 3:10 (the three moneys), 4-5 (the redemption's
fifth, the doubtful, the tithe's removal), Mishnah Eduyot 3:2 (the money's form — the docket's arm), Kiddushin 54b, Rosh Hashanah 12a (the link rows), 12:21's
and 12:7's cells by CALL. F7 THE THIRD YEAR (14:28-29): the line and its one write; the parameters the_removal_date and the_tithes_new_year; the exam: Mishnah
Maaser Sheni 5:6-15 (the removal — the eve of the festival of the fourth year; the confession's conditions), Mishnah Peah 8:5-9 with Tosefta Peah 4 (the poor
man's tithe's measures — half a kav of wheat, a kav of barley; the poor who travel; who is poor — two hundred zuz), Yevamot 47b (the convert — the poor tithe;
the convert's acceptance), 86a-b (the poor tithe's recipients), Rosh Hashanah 12a-13a (the third year's new year), Tosefta Sanhedrin 3:5-6 (through the Sifrei),
Leviticus 19:9-10's and 23:22's cells by CALL, Avot 3:9 (the link row). THE READBACK TABLE (the_readback — the twenty-nine rows with their grades, the DATA
rows). THE DATA ROWS (about thirty-five): the readback table; the twin diffed (14:15 = 11:16 to the letter; 14:6 = 11:3 with "two"; 14:7 folds 11:4-6; 14:9
twelve of 11:9's twelve); 14:2 = 7:6 eighteen of nineteen; 14:24 holds 12:21's twelve; 14:29 has 24:19's seven and 14:27's seven; "between your eyes" the
frontlets' clause; the sonship's two arms; the two readings of the cutting; the ten named beasts and Solomon's table; the shesuah (the cleft one); the two names
added; the lexicon rule; the counting rule; the altar's disqualified; the afterbirth; the locusts absent; the resident alien and the convert — the sojourner two
persons; the custom's bar; the three covenants; R. Akiva's exclusions; the fowl out; the kid's three seats on the DB; the first tithe's liabilities; the three
conditions; the firstling and the firstling from outside; "learn to fear"; the far place of place not time; the possession; Shiloh and the House; the three
moneys; the class from the four; the containers; the rejoicing peace offerings; the ladder of four; one tithe not two; the removal's date; the seventh year; the
vegetables' year; the gifts exempt and the Leviticus runner's pointer; the four in want and their measures; Samaria's fall; the blessing; the parser's [2] and
[3]; the ra'ah's resh; the register's rows; the homographs (the_place_luz_bethel, the_raven, the_flock, the_beasts); the priesthood -> holiness_b edge naming
14:1; the verses no one cites (14:9, 14-18).

THE LINES ON THE TAPE (the recorder and the stitcher; the design's arithmetic): NO MARKER; FIVE OWN-DAY LINES after the tape's last Deuteronomy 13 line
(condemned_city_law_declared) — sons_and_mourning_declared (14:1-2), food_law_declared (14:3-20), carcass_and_kid_declared (14:21), second_tithe_declared
(14:22-27), third_year_tithe_declared (14:28-29), all STATUTE by form (the form declared — 4b's lesson); THE DAEMON'S SEVEN WRITES AT THE STATUTES —
cuttings_for_the_dead_barred (a BLOCK), abomination_eating_barred (a BLOCK), carcass_eating_barred (a BLOCK), second_tithe_owed (a STATUS), poor_tithe_owed (a
STATUS) — five new; rejoicing_before_the_lord_commanded (REUSED — a second entry on israel_people), levite_forsaking_barred (REUSED — a second entry) — two
reuses; the case's writes at the exam only (lashes, barred_from_it, impure_until_evening, torn_flesh_to_dogs, left_for_the_poor, accepted, exempt). THE TYPES
(add_types_ch14.py, after the probes' FAIL print): event_vocabulary +6 (the five lines — form statute, witnesses Deut 14:1, 14:3, 14:21, 14:22, 14:28;
food_tithe_case — the exam's case kind) 1155 -> 1161; effect_vocabulary +5 (cuttings_for_the_dead_barred, abomination_eating_barred, carcass_eating_barred —
block; second_tithe_owed, poor_tithe_owed — status; the names the docket confirms) 1056 -> 1061, rejoicing_before_the_lord_commanded's and
levite_forsaking_barred's rows AMENDED with the chapter's seats; daemon_dispositions (law_food_tithe — file, wraps food_tithe, given_at Deut 14:1, installed_by
boot, watches {sons_and_mourning_declared: [cuttings_for_the_dead_barred], food_law_declared: [abomination_eating_barred], carcass_and_kid_declared:
[carcass_eating_barred], second_tithe_declared: [second_tithe_owed, rejoicing_before_the_lord_commanded, levite_forsaking_barred], third_year_tithe_declared:
[poor_tithe_owed], food_tithe_case: [accepted, exempt, lashes, barred_from_it, impure_until_evening, torn_flesh_to_dogs, left_for_the_poor]}; the functions
block's EIGHT WRAPPED — the seven cells and the_readback); dependency_dispositions (the span [[Deut, 14, 1, 29]]; the CALL edges predicted EIGHTEEN — shemini,
sanctions, calendar, erection, ordinances, priesthood, holiness, holiness_b, moadim, temurah, korach, yovel, seven_nations, second_tablets, place_name,
primeval, mamre, seducers — the census decides; NO pointer predicted; FALSE edges on the homographs if matched; the holiness runner's GIFTS_IMPORT pointer at
14:28 a REVERSE candidate if the census asks); installation_probes I5 73 -> 74; calendar_parameters.yaml +5 (the_birds_signs, the_carcass_table,
the_moneys_form, the_removal_date, the_tithes_new_year — the sojourn_start form, the docket's values); the register file untouched (DECLARED 98).

THE PREDICTION'S ARITHMETIC: RUN = (1332, 96, 88, 0, 12, 1641, 45, 319, the four pairs, 127) — events +5, timers set +0, fired +0 (no clock walk), cancels 0,
retro-writes 12 UNMOVED, writes +7 (the daemon's seven at the statutes), daemons fired +1 (law_food_tithe), entities +0 (israel_people on the registry; no
person, beast or bird an entity), closes +0 (no debit, no close — Jacob's tithe_vowed OPEN unmoved); PREVIOUS_RUN = 11b's RUN EXACTLY (1327, 96, 88, 0, 12,
1634, 44, 319, the four pairs, 127): THE REST drops the five lines by the runner's tag and the span and the daemon's seven writes with them — no delta;
NEWEST_RUNNER 'food_tithe'; markers 172 UNMOVED (PLACEMENT markers text_constrained 108, reading_placed 49 unmoved); events page_order 1159 -> 1164,
text_constrained 110 and reading_placed 58 UNMOVED — READ, never predicted; CENSUS on tape 1327 -> 1332, kinds 872 -> 877, subjects 272 UNMOVED, markers 172,
closes 71 unmoved; the population table 148 UNMOVED; THE OPEN DEBITS ON israel_people 10 UNMOVED (no debit this chapter); THE BLOCKS on israel_people +4 in
count (three new; levite_forsaking_barred's second entry — the literals counting the blocks grepped); rejoicing_before_the_lord_commanded ONE -> TWO on
israel_people (DD2's count literal, Q32's tuple at readback_probes line 459 — retyped from the print BEFORE the tape, 8b's and 10b's lesson), levite_forsaking_barred
ONE -> TWO (DD2, DD4's holes and Q32 — the grep decides); treasured_people ONE UNMOVED (CQ5, Q17); tithe_granted and inheritance_barred ONE each on the Levites
UNMOVED (Q33); the scene's tuple PREDICTED BY SCRIPT at the runner step (the exam's persons through food_tithe_case — each written once; no timer; no close);
the narrative's (its own world: the seven writes, 0 closes, the entity israel, the counter's day (11, 1), no row).

THE CHECKPOINTS DF1-DF9 (the D series at its sixth name; the literals typed from the prints at RUN B):
DF1 THE LINES — five events on the tape AFTER the tape's last Deuteronomy 13 line: sons_and_mourning_declared, food_law_declared, carcass_and_kid_declared,
second_tithe_declared and third_year_tithe_declared on the counter's day (40, 11, 1), NO marker (markers 172 UNMOVED); the counter ends at (40, 11, 1).
DF2 THE WRITES — cuttings_for_the_dead_barred ONE, abomination_eating_barred ONE, carcass_eating_barred ONE, second_tithe_owed ONE, poor_tithe_owed ONE on
israel_people; rejoicing_before_the_lord_commanded TWO (12:7's and 14:26's), levite_forsaking_barred TWO (12:19's and 14:27's) on israel_people;
law_food_tithe registered, given_at Deut 14:1, installed_by boot; the eight cells WRAPPED.
DF3 THE READBACK — the_readback's rows (twenty-nine; the census from the print), every reference row's entry FOUND: the tape lines by kind and first verse
(tithe_given Gen 14:20, vowed Gen 28:20, olah_offered Gen 8:20, covenant_offered Exod 19:5, portion_declared Num 18:20, tithe_of_the_tithe_commanded Num 18:25,
nations_devoted Deut 7:1, stranger_love_commanded Deut 10:17, place_chosen_declared Deut 12:5, profane_slaughter_permitted Deut 12:15) and the kin's cells by
CALL (each returning its verdict on its own ask — the classifier on the four, the kid's cell on its three asks, the carcass's ban naming 14:21, the tithe's
liabilities); no pointer, no retrograde row, no state row.
DF4 THE HOLES — NO effect naming the cuttings for the dead, the abomination's eating, the carcass's eating, the second tithe or the poor man's tithe on
israel_people BEFORE this daemon's lines (the ledger scan on the running world at the tape's Deut 13 end: EMPTY — asserted before the lines run) and ONE each
after; rejoicing_before_the_lord_commanded and levite_forsaking_barred ONE each before and TWO after; the five new names absent from both registries at sitting
12's tree (asserted on the registry files).
DF5 THE KIN STAND — the classifier returning the four by CALL (shemini.classify: the camel, the hare, the coney cud without hoof; the swine hoof without cud),
the kid's cell barred on 'cook', 'eat' and 'benefit' by CALL (calendar.kid_in_milk), the carcass's ban naming Deut 14:21 by CALL (sanctions.carcass's lashed
cell), the torn to the dogs by CALL (ordinances.torn), the first tithe's liabilities by CALL (korach.the_tithe), the herd's tenth an ordinal by CALL
(temurah.tithe), the priests' baldness per spot by CALL (priesthood.family), the corners left by CALL (holiness.gifts); treasured_people ONE UNMOVED (a heaven
entry, OPEN), tithe_granted ONE and inheritance_barred ONE on the Levites UNMOVED, tithe_given's transfer (Abram's) UNMOVED, tithe_vowed's debit (Jacob's) OPEN
UNMOVED, holy_things_in_the_gates_barred ONE UNMOVED, profane_slaughter_permitted ONE UNMOVED; the open debits on israel_people 10 UNMOVED.
DF6 THE PARAMETERS AND THE CLOCK — the_birds_signs, the_carcass_table, the_moneys_form, the_removal_date and the_tithes_new_year on file
(calendar_parameters.yaml, the sojourn_start form); THE REMOVAL'S YEAR READ FROM THE CYCLE BY CALL (yovel — the fourth and the seventh of the count; the bare
world before the entry: the count not begun, the cell's verdict "no count" asserted; the running world's count read and printed) — the date's rendering the
clock's, never a constant; no marker.
DF7 THE REGISTER AND THE EDGES — NO register seat at Deut 14 (the finder called on the chapter at the tape — the reading's measurement repeated); DECLARED 98
UNMOVED; the eighteen CALL edges on file as the census filed them (the file read at the gates); the homographs FALSE if matched; no pointer.
DF8 THE DATA — the twin diffed on the DB (14:15 = Leviticus 11:16 to the letter; 14:6 = 11:3 with "two"; 14:7 folds 11:4-6; 14:9 twelve of 11:9's twelve; the
ra'ah's resh against the da'ah's dalet); 14:2 = 7:6 eighteen of nineteen; 14:24 holds 12:21's twelve in order; 14:29 holds 14:27's seven; the kid's three seats
on the DB (23:19, 34:26, 14:21 — the census's own count); the tithe's starred tokens at 14:22, 23, 28; the parser's [2] at 14:6 and [3] at 14:28; the
sojourner's two renderings from the Onkelos store (14:21 "the uncircumcised", 14:29 "the convert") — every one by CALL to the ink block.
DF9 THE REST — entities 319 UNMOVED, closes 127, markers 172, the population table 148 UNMOVED, the five kinds present; the other counts 11b's exactly with the
five lines and the seven writes dropped (THE REST test — NO declared delta). THE STALE LITERALS predicted (grepped at the design): DD2 in cold_run_sequence.py
("rejoicing_before_the_lord_commanded ONE", "levite_forsaking_barred ONE" — line 3299: MOVES), DD4 (the holes' SEVEN ALONE — line 3305: the grep decides), Q32's
tuple in readback_probes.py (line 459 — the seven (1, verse) pairs: TWO of them MOVE), the checkpoints counting the blocks on israel_people (if any); every
miss shown at once by checkpoint_check.py --all AFTER the tape.

THE PROBES (RUN B's FIRST step, before the types — 7b's lesson 2): readback_probes.py Q37-Q39 written to FAIL before the runner exists — Q37 the runner and its
the_readback table (the rows and their census typed from the print; every reference row's entry found; no pointer, no retrograde row, no state row); Q38 the
five own-day lines on the counter's day (40, 11, 1) with NO marker (markers 172 UNMOVED) and their seven writes (five new on israel_people;
rejoicing_before_the_lord_commanded and levite_forsaking_barred TWO each — the reuses); Q39 the kin standing (DF5's counts) and the holes filled (DF4, DF6);
Q32's tuple retyped from the print; Q22-Q36 otherwise unchanged (no marker count moves); THE PARSER — 14:6's [2] and 14:28's [3] measured at the reading: census
probe rows IF the form asks (the probes' own count read at RUN B; census_probes 224 at 11b); the register gate --strict (no seat; DECLARED 98 unmoved);
checkpoint_probes' verse computed (2b's form).

THE ORDER: this design -> the state doc's checkpoint (#205 — RUN A closed) -> THE DOCKET IN TWO RUNS: D1 the dump's 144 LINK rows, Chullin 59a-66b (178 rows,
18 credited) and the ninety Mishnah rows (Chullin 1:7, 3:6-7, 4:4, 8:1-4; Makkot 3:5-6; Maaser Sheni 1-5 whole; Maasrot 1:1, 1:3, 2:4, 4:5-6; Temurah 6:1;
Eduyot 3:2; Zevachim 5:8; Peah 8:5-9; Bekhorot 9 whole; Avot 3:9, 3:14) — 412 addresses, the credited CARRIED with their ledgers' own verdict lines (11b's form,
ch13_credit_carry.py derived), the uncredited read whole in chunk files (the cap 64,000 bytes — one chunk one Read page), the parts on 11b's whole-row
instruments (ch13_docket_A.py's form, ch13_docket_common.py, ch13_docket_U.py — ONE SHARED FILE for the unresolved rows), EVERY ROW WHOLE, the verdicts LAW /
DERIVATION / DISPUTE / CONTEXT / OUTSIDE with the credits computed, its own clean point; D2 the seventeen other folio ranges (Chullin 68a-69a 62, 72b-73a 32,
77a 16, 80a 21, 113a-116b 135 — 118 carried; Makkot 20a-21a 43; Yevamot 13b-14a 42, 47b 19, 86a-b 23; Kiddushin 36a 22, 54b 16; Rosh Hashanah 12a-13a 39;
Bekhorot 34a-35a 51, 53b 17; Pesachim 21b 11, 50b-51a 24; Bava Metzia 88a 9) with Tosefta Peah 4 (20) and Tosefta Kilayim 1 (11) — 580 addresses, the writer
derived from write_ch13_docket.py (the eighteen ranges ASSERTED against the scan's print), the docket's records (COMPILE_DEBT's box (o), MIDDOT — every code
checked in MIDDOT.md before it is typed, MISHNAH_TOPICS, the state doc's checkpoint), its own clean point -> RUN B: the probes to FAIL (patch_probes_ch14.py:
Q37-Q39; the reuse literals retyped ONE -> TWO), the types (add_types_ch14.py — the docket's names; the five parameters), the callees' facts printed before any
assert (ch14_callees.py — every CALL named above, each ask read at the cell's own source), the runner in parts with the fast checker (ch14_fastcheck.py) and
the generated CASES (ch14_cases_gen.py; the guard's count from the generator's print), the recorder (seq_record_ch14.py, INK_CACHE=0) and the stitcher
(seq_stitch_ch14.py; no marker — the five lines on the counter's day), the literals DF1-DF9 and the VERDICTS entries (patch_seq_literals_ch14.py), the tape to
10/10 with THE REST, checkpoint_check.py --all AFTER the tape, the records writer (write_ch14b_records.py) and the copier WRITTEN, gates_chain.sh LAUNCHED in
the background, the clean point -> THE TAIL: the summary read once, the demands filed (a rerun --from the step), the records from the sheet in one call (the
map's AS BUILT, COMPILE_DEBT's sitting-12 box PAID and the 12b box, MIDDOT, MISHNAH_TOPICS, RESEARCH_LOG, THE_STEPS, THE_BRIEFING, THE_LOOP's step-6 row,
RESUME, RECORD_FORMS, the state doc, the addenda, the recovery page, the memory), the forms copied (copy_ch14b_forms.py), the commit message (this sitting's
beneath chapter 14's and 13b's, for the owner's word).
'''
assert not re.search(r'/Users/(?!Shared/)', SEC) and os.path.expanduser('~') not in SEC
assert not re.search(r'[֐-׿]', SEC), 'Hebrew script in the design — the map lints at 0'
open(P, 'a', encoding='utf-8').write(SEC)
print('appended', len(SEC.encode()), 'bytes to the map;', sum(1 for _ in open(P, encoding='utf-8')), 'lines now')
