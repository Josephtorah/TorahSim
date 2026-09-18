import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE DEUTERONOMY WALK sitting 4b — THE COMPILE OF CHAPTER 6 (2026-09-17; the owner: "Go" after sitting 4's commit): THE DESIGN written into the map
# at the close of RUN 1 of four (the rereads, the measurements — ch6_compile_recon.py, ch6_docket_scan.py — and this section, BEFORE any code), with
# the state doc's checkpoint (#190 addendum 5) naming RUN 2's first step, the memory note and the index line. Every number typed from the two
# instruments' prints of this run; the caps asserted before any file is opened; --check prints the plan only. Sitting 3b's form (write_ch5b_design.py).
import os, subprocess, sys
ROOT = _ROOT
MEM = os.path.expanduser('~/.claude/projects/-Users-Shared-TorahSim/memory')
SP = os.path.dirname(os.path.abspath(__file__))
CHECK = '--check' in sys.argv
def rd(p): return open(p, encoding='utf-8').read()
R = rd(f'{SP}/ch6_recon.out'); S = rd(f'{SP}/ch6_scan.out')
assert "FREE prefixes: ['CO', 'CQ', 'CU']" in R and 'LINK rows 95 in 33 works' in S and 'Berakhot                 2a-16a     787 rows' in S and 'Menachot                31b-37b     156 rows' in S
assert 'RUN (1302, 96, 88, 0, 12, 1593, 36, 319' in R and 'NEWEST_RUNNER covenant_at_horeb' in R and "I5 expects: ['65']" in R and 'pointers naming Deut 6: []' in R
DATE = '2026-09-17'
DESIGN = f'''

## Sitting 4b — THE COMPILE OF CHAPTER 6, Deuteronomy 6:1-25 ({DATE}; the owner: "Go" after sitting 4's commit a7955cc): THE DESIGN — written at the
## close of RUN 1 of four (the rereads: THE_STEPS' compiler block and Step 5, the 4b box (a)-(l), the 3b design and AS BUILT as the compile's form; the
## measurements: ch6_compile_recon.py, ch6_docket_scan.py in the scratchpad) and BEFORE any code; the four-run rule's second sitting

THE FOUR RUNS: RUN 1 the rereads, the measurements and this design — CLOSED HERE, a clean compaction point (#190 addendum 5); RUN 2 the probes to FAIL
(readback Q13-Q15), then THE DOCKET by the union rule at a short cut (four parts A-D on ch5's instrument, the writer write_ch6_docket.py, coverage
computed); RUN 3 the types by script, the recorder and the stitcher, the gates to FAIL, the runner in parts with the fast checker and the generated
CASES, the literals CO1-CO9, checkpoint_check.py --all, the tape to 10/10 with THE REST; RUN 4 gates_chain.sh in one summary, the records from the
sheet in one call, the forms copied, this section's AS BUILT.

THE MEASUREMENTS (what the tape, the runners and the gates say before a line is typed): THE COUNTER stands at (40, 11, 1); the tape's LAST LINE is
stand_here_commanded (5:28-31, dated (1, 3, 7) inside 5:23's retrograde stretch) and its LAST MARKER the FORWARD one at Deut 5:32 (M['charge'] =
M['speech'], (40, 11, 1)) — the stretch ENDED: CHAPTER 6 OPENS ON THE COUNTER'S OWN DAY, NO MARKER (2b's lesson 2 checked again). NO LINE OF THE
CHAPTER'S OWN MATTER IS ON THE TAPE — no runner holds a cell for the recitation, the tefillin, the mezuzah, the teaching, the test at 6:16 or the
right-and-good (the recon's regex per def over all sixty runners: "tefillin" only as a word in erection, family, vestments; "mezuzah" nowhere;
"fringes" a MODULE mention in mekoshesh, whose span holds Numbers 15:37-41; "shema/recite" only as the verb "recite" elsewhere) — THE SHEMA'S LAW IS
COMPILED HERE FOR THE FIRST TIME, its giving the chapter's own day. THE CELLS THE CHAPTER CALLS, located first: the other gods and the jealous God —
covenant_at_horeb.the_second_word (F2 of 3b: no_other_gods, no_image, bow_and_serve, the_visiting; other_gods_barred a BLOCK on Israel at the giving's
line); the oath by the Name — decalogue.vain_name (the third word's cell: vain_oath, false_future_oath) the prohibition's side, holiness.deposit_case and
vayikra5's graded_offering the oath's cases; the son's question — pesach.firstborn (Exodus 13:2-16 the passover's runner: the firstborn's consecration and
13:13-14's "when your son asks you"; the sign on the hand at 13:9, 13:16 in its ink, NO tefillin cell); the forgetting — obey_horeb's FORGET census
(thirteen seats, 6:12 among them) and the_exile_case (4:29's "with all your heart"); the testimonies' header — obey_horeb's 4:45 assert (the three seats
4:45, 6:17, 6:20); the trials — exodus_story.trials (count_by_exodus 6, ten_list — "two at the water" Marah and Rephidim; Arakhin 15a) and its 'murmured'
kind writing tested_the_lord; the oath to the fathers — mamre (sworn_by_himself at Genesis 22:16-18; oath_upheld at 26:3-5) and joseph (visitation_promised
at 50:24), opening_speech's 1:8 seats. THE TAPE'S LINES THE CHAPTER RETELLS (the son's answer 6:21-23 and the test 6:16 — every one FOUND): the ten
plague_struck lines (blood, frogs, lice, swarms, pestilence, boils, hail, locusts, darkness, the_firstborn — Exodus 7:20 to 12:29, with their closes),
sent_out (12:31-33), brought_out (12:51 — "the LORD brought out the sons of Israel"; the closes sent_to_pharaoh, to_be_brought_out), sea_split and
saved_at_the_sea (14:21, 14:30), believed (14:31); Rephidim — murmured (17:2-3, the trial "give us water"), rock_struck (17:6), named "Massah and
Meribah" (17:7); the oath — sworn_by_himself (Genesis 22:16-18), oath_upheld (26:3-5), visitation_promised (50:24); the giving — ten_words_declared and
tablets_given (2b's lines at Deut 4:10-13, (1, 3, 7)), stand_here_commanded (5:28-31 — "all the commandment … which you shall teach them": THE CHARGE
6:1 EXECUTES, its debit CLOSED at 3b by the prior run's Deut 1:5). THE REGISTER GATE'S FINDER IS BLIND TO 6:25 (its own code, section (7) of the recon):
the receipt form is "as (k/834) commanded (6680) the LORD (3068) within three" and the second form "according to ALL that the LORD commanded" — 6:25's
"AS HE COMMANDED US" (k/834 + 6680 with the suffix, NO Name; Ezra 4:3 the one other seat) is not scanned, so the gate lists no seat in chapter 6 (DECLARED
100 unmoved) — THE DECISION below. THE CHECKPOINT PREFIX measured FREE: CO (CO, CQ, CU free; none a label elsewhere). THE GLOBAL COUNTS grepped before the
tape run: markers 167 (F 129, R 23, P 15) UNMOVED — no marker this chapter; closes 127 UNMOVED — no close; entities 319 UNMOVED (Israel the written-on
party); daemons 65 → 66 (I5 65 → 66); kinds 1122 → 1125 (two tape kinds, one case kind), effects 1023 → 1025; CENSUS on tape 1302 → 1304, kinds 847 →
849; PLACEMENT events page_order 1138 → 1140 (the lines on the counter's day, no marker), markers unmoved; the positions table 226 → 235 checkpoints.
THE DOCKET SIZED (ch6_docket_scan.py — the export's chapter 6 the DB's, no division map): 95 LINK rows in 33 works (Menachot 21, Berakhot 12, Kiddushin
7, Bava Metzia 5, Megillah 4, Sanhedrin 4, Sotah 4, Yoma 4, Chullin 3 …; every verse of the chapter cited by someone) + THE TOPIC RANGES SIZED: Mishnah
Berakhot 1:1-3:6 whole (19 rows) with 9:5, Pesachim 10:4, Sotah 7:1, Maaser Sheni 3:8, Menachot 3:7 (the four passages); Berakhot 2a-16a 787 rows (102
credited), 61b 16; Menachot 31b-37b 156 (23 credited), 43b 18; Kiddushin 29a-30b 75 (47 credited — the father's duties read at a Genesis sitting);
Pesachim 56a 13, 116a-116b 26; Sanhedrin 4b 17, 74a 23; Shabbat 103b 17; Yoma 11a 14; Bava Metzia 108a 15; Temurah 3b-4a 29 — THE DESIGN DECLARES: every
range whole EXCEPT Berakhot 2a-16a, of which the VERSE-ANCHORED amudim are read whole — 2a-2b (the evening's time from "when you lie down"), 10b-11a (the
postures — the Sifrei 34:9's dispute), 13a-13b (the intention; "hear" in any language; the passages' order; "upon your heart"), 15a-15b (the audibility —
31:7's "hear"), 16a (the laborers, the bridegroom) — and the remainder of the range (the night's watches, David's harp, the laws of prayer and the
synagogue) is ENUMERATED and marked outside declared scope (Step 2's standing rule; the scan's count the enumeration): the docket near 650 rows, some 100
credited, in FOUR parts at a short cut (the four-run rule's docket). THE CHAPTER'S OWN INK (the reading's asserts, reused in the runner): one number
verse (6:4 [1] — the creed's word the numeral), no gap; no divine frame, one "saying" (the son's), two imperatives, one infinitive absolute (6:17), two
plural prohibitions in a singular chapter, the answer in the first person plural; the four seats of "a sign upon your hand", the three spellings of
"frontlets" (11:18 plene in the ink — the shelf's four compartments counted on a defective 11:18: THE OPEN ROW), the one-letter pair "doorposts"; the
two seats of "the LORD one", of "when your son asks you tomorrow" (6:20 = Exodus 13:14), of "as He commanded us" (6:25, Ezra 4:3).

THE NAME: cold_run_hear_o_israel.py — the 61st runner ("hear, O Israel", 6:4); law_hear_o_israel the 66th daemon (given_at Deut 6:4 — the Shema's
first and only giving, the chapter's own line; installed_by boot — the two Deuteronomy daemons' form, law_opening_speech and law_obey_horeb); the span
[[Deut, 6, 1, 25]]; the checkpoints CO1-CO9; the unit deu_06_shema the frozen reading.

THE READBACK'S THIRD FORM — A RETELLING INSIDE A LAW (the box's (f); the first form's (R1)-(R6) and the laws' form's (L1)-(L6) both hold; ONE new
rule): (T1) THE RETELLING IS COMMANDED — "and you shall say to your son" (6:21) is itself a law's clause: the answer's rows are REFERENCE ROWS graded
against the tape (never a second act — R1) AND the cell that compiles the DUTY TO ANSWER (the four askings, Mishnah Pesachim 10:4 "according to the
son's understanding"; Pesachim 116a-b the four sons; the passover's 13:8 "you shall tell your son" by CALL) returns its verdict on the answer's FORM:
the retelling's grades are the exam's cells. THE ROWS (seven — the answer's five, the header's one, the test's one): 6:1 "this is the commandment …
which the LORD your God commanded to teach you" — REFERENCE against stand_here_commanded (5:31 "all the commandment … which you shall teach them"):
the charge EXECUTED, its debit closed by the prior run (VERBATIM in kind — the triad's three seats 5:31 / 6:1 / 7:11); 6:16 "as you tested at Massah" —
REFERENCE against murmured (17:2-3), rock_struck (17:6), named (17:7): a RUN CITATION by name (VERBATIM — the name the tape wrote); 6:21 "we were slaves
to Pharaoh … the LORD brought us out of Egypt with a strong hand" — against brought_out (12:51): EXPANDED ("with a strong hand" the ink of 13:9); 6:22
"signs and wonders great and grievous upon Egypt, Pharaoh and all his house before our eyes" — against the TEN plague_struck lines: SHORTENED (ten lines
to one clause; the retelling's one word for the ten — Onkelos "all the men of his house" supplied); 6:23 "and us He brought out from there, to bring us
in, to give us the land which He swore to our fathers" — against brought_out and the oath's three lines (sworn_by_himself, oath_upheld,
visitation_promised): EXPANDED (the purpose "to bring us in"); 6:24 "and the LORD commanded us to do all these statutes, to fear … for our good always,
to keep us alive as at this day" — against ten_words_declared and stand_here_commanded: EXPANDED (the three purpose clauses); 6:25 "as He commanded us"
— THE RECEIPT WITHOUT THE NAME: a RUN CITATION of stand_here_commanded (5:31's "all the commandment"), VERBATIM in kind. Every row's entry FOUND on the
running world by kind and first verse (CO4); no row OPEN; the grades' census VERBATIM 3 / EXPANDED 3 / SHORTENED 1 typed from the runner's print.

THE DESIGN'S DECISIONS (the box's (a)-(l) settled on the measurements):
(a) THE FOUR DUTIES AS LAW CELLS — F3 the_four_duties: THE RECITATION (asks: recite_when — the evening from "when you lie down": the priests' entering
to eat their terumah, until the first watch / midnight / dawn (Mishnah Berakhot 1:1, the dispute Eliezer / the sages / Gamliel), the morning from blue-
against-white until sunrise / three hours (1:2); recite_how — the postures (1:3: Shammai reclining and standing by the letter, Hillel "in his way" from
"when you walk by the way"; the Sifrei 34:9-10), the audibility (2:3: R. Yose "did not fulfil" from "hear", the sages fulfilled; the Sifrei 31:7), the
intention (2:1), the language (Sotah 7:1: in any language, from "hear"); recite_who — the exemptions (3:1-6: the mourner, the bridegroom, women and
slaves and minors, the one in doubt); the_passages — the three passages in their order (2:2; the Sifrei 34:2-3: the fringes recited, Exodus 13's not, the
ten words excluded — Berakhot 12a credited from 3b; mekoshesh's span holds the third passage by REFERENCE); THE TEACHING (teach_your_sons — "sons" the
disciples, the Sifrei 34:1-4; Kiddushin 29a-30b the father's duties, credited where read); THE TEFILLIN (tefillin_passages — the four, Menachot 3:7 "the
four passages invalidate each other"; tefillin_compartments — the hand's ONE and the head's FOUR (the Sifrei 35:3-4; Menachot 34b-35a; Sanhedrin 4b):
THE NUMBER FOUR A PARAMETER taught by the shelf, its derivation from the three spellings a recorded argument that reads 11:18 defective where the ink is
plene — THE OPEN ROW, a DATA row the_spellings naming the divergence, the cell returning the parameter, never the count from the ink; tefillin_arm — the
left, the bicep, the amputee (35:5-10; Menachot 36b-37a); tefillin_order — the hand first, the head first off (35:11; Menachot 36a); tefillin_head — the
hairline, the plague-mark's place (35:12; Menachot 37a-b)); THE MEZUZAH (mezuzah_writing — a scroll in ink, not stone, the perfect letters (36:1-2;
Shabbat 103b; Menachot 31b-34a); mezuzah_doorpost — one post, the right of the entrance, the height (36:3-5; Menachot 33a-34a); mezuzah_gates — the
dwelling's, not the shed's, the bath's, the Temple's except the profane chambers (36:6-8; Yoma 11a; Maaser Sheni 3:8)); the_seven (36:9; Menachot 43b);
the WRITE shema_commanded — a STATUS on Israel (the four duties standing) at the chapter's own line shema_declared (6:4-9).
(b) FEAR, SERVE, SWEAR — F4's fear_serve_swear: 6:13 "by His name you shall swear" a POSITIVE clause (Temurah 3b-4a: "swear" a command when one swears
truly; Shevuot 35a the Name in an oath) with the prohibition's side decalogue.vain_name by CALL (the third word: vain_oath, false_future_oath); "serve"
BEFORE Him (Onkelos) a DATA note; no write (the block of the second word stands).
(c) NO OTHER GODS (6:14) — F4's no_other_gods: covenant_at_horeb.the_second_word('no_other_gods') by CALL; other_gods_barred stands from 3b (no second
write — CO5); the plural prohibition a DATA note (the two plural prohibitions in a singular chapter).
(d) THE TEST (6:16) — F5's you_shall_not_test: exodus_story.trials('ten_list') by CALL ("two at the water"); the tape's Rephidim lines FOUND (CO3); the
WRITE test_barred — a BLOCK on Israel at the chapter's second line testing_barred (6:16-19); the RUN_CITATION pointer at Deut 6:16 (Massah — the tape's
named line at 17:7).
(e) THE RIGHT AND THE GOOD (6:18) — F5's the_right_and_the_good: Bava Metzia 108a's abutter (the buyer of a field adjoining another's yields to the
neighbor — "you shall do the right and the good"): the exam's case row, the verdict accepted for the abutter; a DATA row the_abutter — a rule beyond the
letter seated in the ink's own words (the shelf's teaching; no link of our own).
(f) THE SON'S ANSWER — (T1) above: F6 the_sons_question (asks: the_four_askings — Exodus 12:26, 13:8, 13:14, 6:20 the four sons (Pesachim 116a-b;
Mishnah Pesachim 10:4); pesach.firstborn by CALL for 13:14's ink; the_answer_rows — the five reference rows graded; the_receipt — (j); righteousness_for_us
— Genesis 15:6's kin, 24:13's pledge, a DATA note); NO write (the answer's duty a REFERENCE to the passover's telling; the retelling never a second act).
(g) 6:1'S EDGE — F1 the_header: the triad 5:31 → 6:1 → 7:11 (the reading's assert), 6:1 a REFERENCE row against stand_here_commanded (the charge
executed; the debit's close by the prior run unmoved — CO7); "hear, O Israel, and observe to do" (6:3) the frame (R6, no write); the land flowing
with milk and honey the book's first (the oath's seats).
(h) 6:10-11'S LIST — F4's the_list: a DATA row (the cities, houses, cisterns, vineyards and olives "which you did not …"; Joshua 24:13 and Nehemiah 9:25
the retellings; the Sifrei 38:10's merit; 201:3's spoil permitted — the war chapter's CALL into 6:11 declared OWED FORWARD in the dispositions when
chapter 20 compiles).
(i) "SWORE TO YOUR FATHERS" (6:10, 18, 23) — RUN_CITATION pointers (three) naming the tape's sworn_by_himself (Genesis 22:16), oath_upheld (26:3),
visitation_promised (50:24); the land's promise the covenant's (the erection's book by CALL where the cell asks).
(j) THE RECEIPT WITHOUT THE NAME (6:25) — the register gate's finder BLIND (measured): a RUN_CITATION pointer at Deut 6:25 on the runner (form AS_WHEN,
the referent stand_here_commanded — 5:31's "all the commandment", the giving's ten_words_declared the second referent) declared with this why; THE
FINDER'S THIRD FORM ("as He commanded" — k/834 + 6680 with a suffix and no Name: 6:25, Ezra 4:3 the two Bible seats) OWED TO A GATE SITTING — a gate
change across the whole Torah, not this runner's; recorded in the 4b box's PAID line as owed forward; the gate's DECLARED 100 unmoved; CO6 asserts the
blindness by CALL to the gate's own receipts() finder.
(k) THE LARGE LETTERS — PARKED: no work; the DATA row the_large_letters names the store's two dropped tokens and the parked hypothesis; no edge.
(l) THE DOCKET by the union rule — the scan's 95 link rows + the Mishnah rows (24) + the ranges declared above (near 650 rows, some 100 credited) in
FOUR parts A-D — LAW / DERIVATION / DISPUTE / CONTEXT / OUTSIDE; the crowns expected: the times from "lie down" and "rise" (Berakhot 2a, 10b); the
postures (10b-11a); the audibility from "hear" (15a-b); any language from "hear" (Sotah 7:1; Berakhot 13a); the three terms — the two inclinations, the
soul, the money (9:5; 61b — R. Akiva's "with all your soul"); the four passages and the compartments from the spellings (Menachot 34b-35a; Sanhedrin 4b);
the left arm from "your hand" (36b-37a); the order (36a); the mezuzah's scroll, post, side, gates (31b-34a; Yoma 11a); the perfect letters (Shabbat 103b);
the seven (Menachot 43b); the father's duties (Kiddushin 29a-30b); the creed at Jacob's bed (Pesachim 56a); the four sons (Pesachim 116a-b); the martyr
(Sanhedrin 74a); the oath by the Name (Temurah 3b-4a); the abutter (Bava Metzia 108a).

THE CELLS (six, each returning out(verdict, effects); the INK block exec'd from the sequence file; the token probes zero-report; every seat list typed
from the reading's print and the recon): F1 the_header (6:1-3 — asks: the_triad, the_charge_executed (6:1 — the reference row; CO7), hear_and_observe
(6:3 — 5:1's kin), the_land_flowing (6:3 — the book's first; the oath's seats), your_sons_son (6:2 — three generations; Exodus 10:2 the kin, DATA)); F2
the_creed (6:4-5 — asks: hear_o_israel (the four seats; the imperative; Jacob's sons — Pesachim 56a; the response line), the_lord_is_one (the two seats;
the parser [1]; the_large_letters DATA), with_all_your_heart (the two inclinations — 9:5), with_all_your_soul (the martyr — Sanhedrin 74a; R. Akiva —
Berakhot 61b), with_all_your_might (the money — 9:5; the measure — the Sifrei 32:7), love_and_fear (the Sifrei 32:1; Sotah 31a)); F3 the_four_duties
((a) — the asks named there; the write shema_commanded); F4 the_gift_and_the_warning (6:10-15 — asks: the_list (h), lest_you_forget (6:12 — obey_horeb's
FORGET by CALL), fear_serve_swear (b), no_other_gods (c), the_jealous_god (6:15 — the_visiting by CALL; the Shekhinah DATA)); F5 the_test_and_the_right
(6:16-19 — asks: you_shall_not_test (d — the write test_barred), surely_keep (6:17 — the infinitive absolute; the testimonies' three seats), the_right_and_
the_good (e), thrust_out_enemies (6:19 — DATA; 9:4 forward)); F6 the_sons_question (f). The readback table the_readback (the seven rows of (T1)).

THE DATA ROWS (eighteen): the_readback, the_large_letters (k), the_spellings (the open row — 6:8 defective, 11:18 plene, Exodus 13:16 plene; the shelf's
1 + 1 + 2), the_two_sets (recited / bound; the ten words in neither), the_recitation_times (1:1-2's table), the_postures (1:3; the Sifrei 34:9-10),
the_exemptions (3:1-6), the_passages_order (2:2), the_tefillin_table (compartments, arm, order, head), the_mezuzah_table (writing, post, side, gates),
the_seven (36:9), the_list (h), the_oath_by_the_name (b), the_abutter (e), the_four_sons (f), the_receipt_without_the_name (j), the_creed_terms (heart /
soul / might — money, measure, thanks; Onkelos "property"), the_files_diverge (the export's 36:10 — the reading's caution, a note).

THE DAEMON law_hear_o_israel (given_at Deut 6:4; installed_by boot): watches shema_declared → [shema_commanded]; testing_barred → [test_barred];
shema_case → [accepted, exempt]. No timer; literal W dicts per kind; the case kind dispatching to the cells by name in EXPLICIT branches.

THE TYPES (add_types_ch6.py): TWO tape kinds — shema_declared (speech, 6:4-9; the four duties; the witnesses the verses), testing_barred (speech,
6:16-19; the first telling Exodus 17:2-7 named in the row) — ONE case kind (shema_case); TWO new effects — shema_commanded (status on Israel; 6:4-9),
test_barred (block on Israel; 6:16); the effects reused — accepted, exempt; NO registry row (Israel the written-on party); the daemon block; the
functions block hear_o_israel (the six cells WRAPPED); the span [[Deut, 6, 1, 25]]; the CALL edges by the ink — covenant_at_horeb (the second word, the
visiting; the charge's line), obey_horeb (the forgetting; the testimonies' header; the exile's heart), decalogue (the vain name — the oath's prohibition),
exodus_story (the trials; the plagues and the going out read back), pesach (the son's question at 13:14; the firstborn's passages), opening_speech (the
oath's seats at 1:8), mamre and joseph (the oath's lines), mekoshesh (the fringes — the third passage, REFERENCE), erection (the covenant's book where
asked); the pointers RUN_CITATION — Deut 6:16 (Massah), 6:10 / 6:18 / 6:23 (sworn to the fathers), 6:25 (the receipt without the Name — (j)); every
demand the census makes past the imports read on the DB and declared, never a blanket row; I5 65 → 66.

THE TAPE (two lines, NO marker): under "# ---- Deut 6 ----" after the tape's last Deuteronomy 5 line and the forward marker at 5:32: shema_declared
(6:4-9) then testing_barred (6:16-19), both on the counter's own day (40, 11, 1), page_order. The markers 167 UNMOVED; the closes 127 UNMOVED; the
counter ends at (40, 11, 1) UNMOVED.

THE CHECKPOINTS CO1-CO9 (the prefix measured free):
CO1 THE LINES — two events of the sitting's kinds on the tape in the ink's order, both AFTER the tape's last Deuteronomy 5 line, both on the counter's day
(40, 11, 1), NO marker added (markers 167); the counter ends at (40, 11, 1).
CO2 THE FOUR DUTIES — shema_commanded on israel_people ONE (a status), source beginning "Deut 6:4"; law_hear_o_israel registered, given_at Deut 6:4,
installed_by boot; the functions block's six cells WRAPPED.
CO3 THE TEST BARRED — test_barred on israel_people ONE (a block), source beginning "Deut 6:16"; the tape's Rephidim lines FOUND by kind and first verse:
murmured at Exod 17:2 ONE, rock_struck at Exod 17:6 ONE, named at Exod 17:7 ONE ("Massah and Meribah").
CO4 THE READBACK'S THIRD FORM — the_readback's rows SEVEN (the answer's five, the header's, the test's), every row's tape entry FOUND on the running
world by kind and first verse (rows n = found n): brought_out at Exod 12:51, plague_struck ten (the ten plagues by value), sworn_by_himself at Gen 22:16,
oath_upheld at Gen 26:3, visitation_promised at Gen 50:24, stand_here_commanded at Deut 5:28, ten_words_declared at Deut 4:10; the grades' census typed
from the runner's print (VERBATIM 3, EXPANDED 3, SHORTENED 1); no row OPEN.
CO5 THE SECOND WORD STANDS — other_gods_barred on israel_people ONE UNMOVED (no second write; the cell CALLED), coveting_barred ONE unmoved.
CO6 THE RECEIPT WITHOUT THE NAME — the register gate's own finder (register_census.receipts, by CALL) lists NO seat at Deut 6:25 on the chapter's ink
(the blindness measured, asserted); the RUN_CITATION pointer 'Deut 6:25' on file; DECLARED 100 unmoved (the gate's --strict print at the chain).
CO7 THE CHARGE EXECUTED — commanded on moses valued teach_the_commandment ONE, CLOSED, closed_by beginning "Deut 1:" UNMOVED (6:1 a reference row, no
write); closes 127.
CO8 THE EXODUS READ BACK — the ten plague_struck lines and their closes UNMOVED; brought_out ONE; sea_split ONE; the four sons' first telling
Exod 13:14 in the ink (the DATA row); nothing written on Egypt or Pharaoh.
CO9 THE REST — entities 319 UNMOVED, closes 127, markers 167, the population table 148 UNMOVED, the two kinds present; the other counts 3b's exactly
with the two lines and the daemon's two writes dropped (THE REST test — NO declared delta this sitting: the daemon writes only on its own lines).
NO retype of the older REST literals (closes and markers unmoved — 3b's lesson 3 checked by grep before the tape); every miss shown at once by
checkpoint_check.py --all before the tape.

THE PREDICTION'S ARITHMETIC: RUN = (1304, 96, 88, 0, 12, 1595, 37, 319, the four pairs, 127) — events +2 (the two lines), timers set +0, fired +0 (no
clock walk), cancels 0, retro-writes 12 UNMOVED, writes +2 (the daemon's watches summed: shema_commanded at the first line, test_barred at the second),
daemons fired +1 (law_hear_o_israel), entities +0, closes +0; PREVIOUS_RUN = 3b's RUN EXACTLY (1302, 96, 88, 0, 12, 1593, 36, 319, the four pairs, 127):
THE REST drops the two lines by the runner's tag and the span and the daemon's two writes with them — no delta; NEWEST_RUNNER 'hear_o_israel'; PLACEMENT
markers UNMOVED ({{'text_constrained': 106, 'reading_placed': 46}}), events page_order 1138 → 1140 (text_constrained 109, reading_placed 55 unmoved) —
read at the stitcher's print; CENSUS typed from the stitcher's print (on tape 1302 → 1304, history +2, kinds 847 → 849 — the two tape kinds, subjects
272 UNMOVED, markers 167 (F 129, R 23), closes 71 unmoved; the case rows the exam's persons); the population table 148 UNMOVED; the scene's tuple
PREDICTED BY SCRIPT at the runner step (the exam's persons through shema_case — each written once; no timer; no close); the narrative's (on its own
world: 2 writes, 0 closes, the entities israel = 1, the counter's day (11, 1), 0 dated lines, no row).

THE PROBES (RUN 2's first step): readback_probes.py Q13-Q15 written to FAIL before the runner exists — Q13 the runner and its the_readback table (seven
rows; the grades' census VERBATIM 3 / EXPANDED 3 / SHORTENED 1; every row's entry found), Q14 the two lines on the counter's day with NO marker (markers
167 after the run) and shema_commanded / test_barred on Israel with their sources, Q15 the receipt without the Name — the gate's finder blind at Deut
6:25 on the chapter's ink and the RUN_CITATION pointer on file; Q10-Q12 unchanged; NO parser rule this sitting (the one number verse read right at the
reading — census_probes unmoved at 224); the register gate unchanged; checkpoint_probes' verse computed (2b's form).

THE ORDER: this design → the state doc's checkpoint (#190 addendum 5 — RUN 1 closed) → RUN 2: the probes to FAIL (Q13-Q15 0/3) → THE DOCKET by the
union rule (the scan rerun with the Berakhot amudim named, the dump; four parts A-D on ch5_docket_rows.py's instrument at a short cut; the writer
write_ch6_docket.py with the coverage computed and the cite index) → the checkpoint (#190 addendum 6) → RUN 3: the types by script (add_types_ch6.py) →
the recorder and the stitcher (the scratch copies: SPAN_ORDER + 'hear_o_israel'; no marker row) → the gates to FAIL (daemon, dependency) → the runner
(ch6_part1-4.py assembled by cat; the fast checker over parts 1 and 2; the honest-pairing guard; zero-report probes; the scene and the narrative
predicted by script; CASES generated from the cells' asks) → the recorder → the stitcher → the literals CO1-CO9 (patch_seq_literals_ch6.py) →
`checkpoint_check.py --all` → the tape run (10/10 with THE REST) → the checkpoint (#190 addendum 7) → RUN 4: `gates_chain.sh` in the background (one
summary: the probe gates, the daemon and dependency gates, build_world, the journal gate, THE REGISTER GATE --strict unmoved, the positions table,
checkpoint_probes, the sweep, the journal gate again) → the records from the sheet in one call (this section's AS BUILT, COMPILE_DEBT's sitting-4 box
PAID + the 4b box with the finder's third form owed forward, MOVE_CATALOG (checked), MIDDOT's docket entries, MISHNAH_TOPICS (Berakhot 1-3, 9:5;
Pesachim 10:4; Sotah 7:1; Maaser Sheni 3:8; Menachot 3:7), RESEARCH_LOG, THE_STEPS, THE_BRIEFING, THE_LOOP.md's step 6 row (the third form), RESUME,
memory, the state doc's addendum, the recovery page rewritten, the addenda's section) → the forms copied.
'''
STATE = f'''

#190 ADDENDUM 5 ({DATE} — RUN 1 OF SITTING 4b CLOSED, on the owner's "Go" after a7955cc: THE COMPILE OF CHAPTER 6 — the rereads, the measurements, the design). THE REREADS: THE_STEPS' compiler block and Step 5's head (in this window), the map's "Sitting 3b" design and AS BUILT (the compile's form), the 4b box (a)-(l). THE MEASUREMENTS (ch6_compile_recon.py → ch6_recon.out 234 KB, read by section at a cut; ch6_docket_scan.py → ch6_scan.out and the dump ch6_docket_dump.txt 3,860 lines): no line of the chapter's matter on the tape; the retellings' lines all present (the ten plagues, brought_out, the sea, Rephidim's murmured / rock_struck / named, the oath's three lines, the giving, stand_here_commanded); the register gate's finder BLIND to 6:25's form; the prefix CO free; the counts markers 167 / closes 127 / entities 319 / daemons 65 unmoved before the tape; the docket 95 link rows + the topic ranges sized (Berakhot 2a-16a 787 — the design reads its verse-anchored amudim, the rest enumerated outside declared scope). THE DESIGN written into the map: "Sitting 4b — THE COMPILE OF CHAPTER 6 … THE DESIGN" — the runner cold_run_hear_o_israel.py (the 61st), the daemon law_hear_o_israel (given_at Deut 6:4, boot), two tape lines and NO marker, two effects (shema_commanded a status, test_barred a block), six cells, eighteen DATA rows, THE READBACK'S THIRD FORM (T1: a retelling inside a law — the son's answer's rows the exam's cells; seven rows, VERBATIM 3 / EXPANDED 3 / SHORTENED 1 predicted), the decisions (a)-(l) with the tefillin's compartments a PARAMETER and the spellings' open row, the receipt without the Name a RUN_CITATION pointer with the finder's third form OWED to a gate sitting, CO1-CO9, RUN (1304, 96, 88, 0, 12, 1595, 37, 319, the four pairs, 127) and PREVIOUS_RUN 3b's exactly. NOTHING MID-FLIGHT — A CLEAN COMPACTION POINT. The tree: the map, the state doc, the memory (uncommitted since a7955cc). THE WORD FOR THE NEXT SITTING — RUN 2 OF 4b, its first step: readback_probes.py Q13-Q15 written to FAIL (0/3), then the docket — ch6_docket_scan.py rerun with the Berakhot amudim named (2a-2b, 10b-11a, 13a-13b, 15a-16a) and the rest of 2a-16a dropped to the enumeration, the dump; the rows read in four parts A-D at a short cut on ch5_docket_rows.py's instrument (the address, the kind, 150 characters), the verdicts LAW / DERIVATION / DISPUTE / CONTEXT / OUTSIDE with the crowns the design expects; write_ch6_docket.py from write_ch5_docket.py by sed (the coverage computed, the cite index); the checkpoint #190 addendum 6. POST-COMPACTION REREADS: the recovery page, the map's "Sitting 4b … THE DESIGN", MEMORY.md.
'''
MN = f'''
SITTING 4b RUN 1 DONE {DATE} (on "Go" after a7955cc): the measurements (ch6_compile_recon.py, ch6_docket_scan.py) and THE DESIGN in the map ("Sitting 4b — THE COMPILE OF CHAPTER 6 … THE DESIGN"): the runner cold_run_hear_o_israel.py, the daemon law_hear_o_israel (boot, given_at Deut 6:4), two tape lines (shema_declared 6:4-9, testing_barred 6:16-19) and NO marker, the effects shema_commanded / test_barred, six cells, THE READBACK'S THIRD FORM (a retelling inside a law — the son's answer, seven rows), the compartments a PARAMETER with the spellings' open row, the receipt without the Name a RUN_CITATION pointer (the gate's finder blind — its third form owed to a gate sitting), CO1-CO9, RUN (1304, 96, 88, 0, 12, 1595, 37, 319, the four pairs, 127), PREVIOUS_RUN 3b's. Clean point (#190 addendum 5). NEXT: RUN 2 — readback Q13-Q15 to FAIL, then the docket (95 link rows + the ranges; Berakhot's verse-anchored amudim) in four parts at a short cut, write_ch6_docket.py.
'''
plans = []
P = f'{ROOT}/World/step9/DEUTERONOMY_WALK.md'; s = rd(P); assert '## Sitting 4b — THE COMPILE OF CHAPTER 6' not in s and s.rstrip().endswith('and on in order.')
plans.append((P, s.rstrip('\n') + DESIGN))
P = f'{ROOT}/logic/pre_logic_methods_2026-07-28/PROMPT_continue_solo_era_2026-08-06.md'; s = rd(P); assert '#190 ADDENDUM 5' not in s and '#190 ADDENDUM 4' in s
plans.append((P, s.rstrip('\n') + STATE))
P = f'{MEM}/deuteronomy-walk.md'; s = rd(P); assert 'SITTING 4b RUN 1 DONE' not in s
plans.append((P, s.rstrip('\n') + '\n' + MN))
P = f'{MEM}/MEMORY.md'; s = rd(P)
old = 'chapters 1-6 READ, 1-5 COMPILED (a7955cc not pushed); SITTING 4 DONE 2026-09-17 (220 units); NEXT: 4b on his word'
new = 'chapters 1-6 READ, 1-5 COMPILED (a7955cc); SITTING 4b RUN 1 DONE 2026-09-17 (the design); NEXT: RUN 2 the docket'
assert s.count(old) == 1, s.count(old)
s2 = s.replace(old, new); assert len(s2.encode('utf-8')) < 17000, len(s2.encode('utf-8'))
plans.append((P, s2))
for p, s2 in plans: assert s2 != rd(p), p
if CHECK:
    for p, s2 in plans: print('WOULD WRITE', p, len(rd(p)), '->', len(s2))
    sys.exit(0)
for p, s2 in plans:
    open(p, 'w', encoding='utf-8').write(s2); print('WROTE', p, len(s2.encode('utf-8')))
print('the 4b design and the run 1 checkpoint written')
