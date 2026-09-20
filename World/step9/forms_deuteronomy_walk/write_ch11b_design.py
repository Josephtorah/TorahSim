#!/usr/bin/env python3
# THE DEUTERONOMY WALK sitting 9b — THE COMPILE OF CHAPTER 11 (2026-09-20): THE DESIGN appended to the map at the close of RUN A (the rereads, the
# measurements — ch11_compile_recon.py and ch11_docket_scan.py, both derived from 8b's forms — and this text), BEFORE any code; every number in it read from the
# recon's and the scan's prints (ch11_recon.out, ch11_docket_scan.out). The section asserted absent first; the lint 0 after. 8b's form (write_ch10b_design.py).
import os, re, subprocess, sys
ROOT = subprocess.check_output(['git', 'rev-parse', '--show-toplevel'], text=True).strip()
SP = os.path.dirname(os.path.abspath(__file__))
MAP = f'{ROOT}/World/step9/DEUTERONOMY_WALK.md'
rec = open(f'{SP}/ch11_recon.out', encoding='utf-8').read(); scan = open(f'{SP}/ch11_docket_scan.out', encoding='utf-8').read()
assert 'RUN (1317, 96, 88, 0, 12, 1613, 41, 319' in rec and 'NEWEST_RUNNER second_tablets' in rec and "the next name: DC" in rec and 'DAEMON_ORDER 70' in rec and 'kinds 1142, effects 1037' in rec
assert 'the register seats naming Deut 11 (WHOLE): []' in rec and 'pointers naming Deut 11: []; edges naming Deut 11: []' in rec and "'korach_named': False" in rec and 'I5 expects: [\'70\']' in rec
assert 'LINK rows 74 in 20 works' in scan and 'TOPIC rows 952' in scan and 'PRIOR READS (credited): 622 addresses of 1049' in scan and 'Tosefta_Sotah 8: 7 rows' in scan and 'Tosefta_Sheviit 4: 16 rows' in scan and 'NO SUCH WORK Mishnah_Taanit' in scan
HEAD = '## Sitting 9b — THE COMPILE OF CHAPTER 11, Deuteronomy 11:1-32 (2026-09-20; the owner: "9b go" after sitting 9\'s commit 2f4ec5b): THE DESIGN'
t = open(MAP, encoding='utf-8').read(); assert HEAD not in t and '## Sitting 9 — CHAPTER 11 — AS BUILT' in t
D = HEAD + ''' — written at the close of RUN A of two under THE TWO-RUN RULE (the rereads: THE_STEPS' compiler block and Step 5's head, the sitting-9 AS BUILT, the 8b
## design and AS BUILT as the compile's form, the 9b box (a)-(n); the measurements: ch11_compile_recon.py derived from 8b's by asserted line-based substitutions
## (derive_ch11_recon.py), ch11_docket_scan.py derived from 8b's (derive_ch11_docket_scan.py) — all in the scratchpad) and BEFORE any code; the docket ITS OWN RUN
## by the ~700 clause (1,049 addresses in the dump plus the two Tosefta chapters; 622 credited by address at the scan; some 450 to read whole)

THE TWO RUNS AND THE DOCKET'S OWN: RUN A the rereads, the measurements and this design — CLOSED HERE, a clean compaction point (#199); THE DOCKET by the union
rule, EVERY ROW WHOLE (the parts on 8b's whole-row instruments as 7b derived them, the writer write_ch11_docket.py, coverage computed) — its own run, the dump
already written (ch11_docket_dump.txt, 3,149 lines); RUN B the probes to FAIL (readback Q28-Q30, BEFORE the types — 7b's lesson 2), the types by script with the
docket's names, the callees' facts printed before any assert, the runner in parts with the fast checker and the generated CASES, the recorder with the cache OFF
(7b's lesson 1) and the stitcher, the literals DC1-DC9, the tape to 10/10 with THE REST, checkpoint_check.py --all AFTER the tape, gates_chain.sh in one
summary, the records from the sheet in one call, the forms copied, this section's AS BUILT, the commit message.

THE MEASUREMENTS (what the tape, the runners, the registries and the running world say before a line is typed): THE COUNTER stands at (40, 11, 1), day
908865; the tape's LAST LINES are chapter 10's four own-day lines (demand_declared, heart_circumcision_commanded, stranger_love_commanded, cleaving_commanded)
after the forward marker at Deut 10:12 (M['speech_resumed_10']) and its LAST MARKER that one; RUN (1317, 96, 88, 0, 12, 1613, 41, 319, the four pairs, 127),
PREVIOUS_RUN 7b's; markers 172 (text_constrained 108, reading_placed 49), events text_constrained 110 / page_order 1149 / reading_placed 58; CENSUS (2520,
1319, 1317, 1185, 6, 10, 9, 0, 71, 172, 131, 15, 26, 862, 272); 65 runners, 70 daemons (installed_by boot 29), kinds 1142, effects 1037; the D series DA and
DB in use — THE NEXT NAME DC (no code assumes a letter). THE ACTS THE CHAPTER RETELLS, ON THE TAPE WITH THEIR DAYS (the snapshot's log): THE EXODUS —
plague_struck 12:29 under the marker M['exodus'] (day 894328), sent_out 12:31-33, vessels_asked, journeyed to Succoth, brought_out 12:51 (the closes
sent_to_pharaoh on moses, to_be_brought_out on israel); THE SEA — heart_hardened 14:8, pursued 14:8-9 (egypt_people), murmured 14:11, sea_split 14:21 under
M['sea'] (day 894334 — the twenty-first of Nisan by CAL_PARAMS sea_split_date), sea_returned 14:27-28 with the DESTROY egypt_drowned on Pharaoh's host,
saved_at_the_sea 14:30 closing pursued_by_egypt and to_be_delivered, believed 14:31, sang 15:1/21, Shur under M['shur'] (894337): 11:4's "made the waters of
the Red Sea flow over them as they pursued you" is sea_returned BY KIND; DATHAN AND ABIRAM — korach_gathered_against 16:1-3 (parties korach, dathan, abiram,
on; count 250), dathan_and_abiram_refused 16:12-14 (subject dathan), congregation_withdrew 16:25-27, creation_test_declared 16:28-30, earth_swallowed 16:31-34
— subject dathan, swallowed ['dathan', 'abiram', 'their households', 'every person who belonged to Korach'], korach_named False: THE TAPE ALREADY READS THE
VERSE AS THE CHAPTER DOES (Korah unnamed at the swallowing — the reading's find, on the tape since the Korah compile), fire_consumed_the_two_hundred_fifty
16:35; THE WILDERNESS — chapter 8's state row, no line (good_land.the_way_of_forty_years by CALL); "every living thing" — all_flesh_expired Gen 7:21-23 with
the close to_be_wiped "and He wiped out every living thing"; Abram at Shechem — journeyed 'the place of Shechem' Gen 12:6 (Moreh's seat); Lot's choice —
lot_chose 13:10-11; the river — covenant_cut_with_abram 15:18-21 with the closes land_promised; THE BORDERS — borders_commanded Num 34:1-12 (27 points; the
STATUS borders_declared on the-land-of-canaan); THE SHEMA — shema_declared 6:4-9 (duties recite, teach, bind, write; shema_commanded on israel_people); THE
ESCORT — Exodus 23:20-33 HAS NO LINE BY VERSE: ordinances.land the cell (angel, borders, hornet, little_by_little, bread_water, no_barren, no_bow, no_covenant,
not_dwell, serve_before, break_pillars, not_forgive) and entered_the_land its CASE kind — an INSTALLING ACT on the registry; LEVITICUS 26 HAS NO LINE ON THE
TAPE (the tochacha runner's kinds covenant_kept, iniquity_confessed, people_exiled, warning_refused are exam cases; the rains of 26:4 and the heavens as iron of
26:19 live in its covenant / cascade cells): NO EFFECT ANYWHERE NAMES THE RAIN — the vocabulary's one 'rain' is fire_rained, Sodom's; THE HOLE MEASURED; the
pilgrim's land guarded — pilgrim_land_guarded (a HEAVEN entry) written by the calendar runner (Exodus 34:24's warranty inserted at the pilgrimage) and the
erection's; terror_of_god (Genesis 35:5's STATUS on the cities — the form's seat); nations_driven_out (the covenant's TRANSFER); THE SECOND WORD'S BLOCKS
other_gods_barred and coveting_barred on israel_people at the giving's line (1, 3, 7), CI3 — 11:16's "serve other gods and bow down to them" by CALL;
blessings_for_hearing (7:12's conditional HEAVEN entry) and pity_barred on israel_people; seven_nations.because_you_hear('the_blessing_list' — 7:13's grain,
wine and oil = 11:14's) and do_not_fear('little_by_little', 'the_hornet'); THE CELLS THAT COMPILE THE KIN: hear_o_israel.the_four_duties (tefillin_arm,
tefillin_head, tefillin_compartments, tefillin_passages, mezuzah_doorpost, mezuzah_gates, mezuzah_writing, teach_your_sons, daughters_exempt), the_header
(the_land_flowing, your_sons_son, the_triad), the_creed; good_land.the_frame (all_the_commandment, live_and_possess, the_oath_seats — 8:1 = 11:8-9's frame),
the_way_of_forty_years (the_discipline 8:5, forty_years, keep_walk_fear 8:6), the_good_land (8:7-10), the_testimony (other_gods_serve_bow, hearken_plural —
8:19-20); seven_nations.the_seven_nations (the_seven), the_holy_people, because_you_hear, do_not_fear; not_righteousness.the_frame (nations_greater — 9:1);
obey_horeb.the_one_god (to_dispossess_nations — 4:38), the_exhortation (the_cleaving — 4:4); second_tablets (demand_declared 10:12 with fear_of_heaven_asked;
cleaving_commanded 10:20 — 11:22's "to cleave to Him" the command's second seat); covenant_at_horeb.the_second_word (no_other_gods, bow_and_serve);
borders.the_four_sides (the_promised_extents, the_sea_as_border, the_great_sea, the_jordan_as_border — 11:24's extents against Numbers 34:6, Exodus 23:31 and
Genesis 15:18 ALREADY A CELL), the_land_and_its_fall (the_land_bound_rule — 44:1's partition already a cell), moses_restatement (joshuas_receipt);
korach.rebellion (swallowed, earth_mouth_cain, names, sons_of_korach, death_mode); second_census.the_roll (hu_dathan, korach_recalled, sons_of_korach —
26:9-11); exodus_story.sea (saved_seat, song_mode, ten_at_sea), plagues, night; primeval.flood, nations; calendar (the pilgrimage's warranty). THE REGISTER —
the finder's two forms ("as / which … commanded the LORD"; "according to all that the LORD commanded") see NO seat in chapter 11 (the register seats naming
Deut 11: none — asserted); 11:25's "as He spoke to you" has neither "commanded" nor the Name — outside the finder's forms AND outside 4b's owed third form
(10:9's "as the LORD your God spoke to him", with the Name): A FOURTH SHAPE, 1:11's — the run citation by "spoke" without the Name (sixteen seats in the
book, the reading's count); the docket to confirm; the design's disposition a RUN_CITATION pointer (below). THE DEPENDENCY FILE — no pointer or edge names
Deut 11 (asserted); 610 edges, 203 pointers. THE PROBES — readback Q1-Q27 (Q10 absent); the marker-count literals (Q14's 167, Q20's, Q23's 172) UNMOVED this
sitting (no marker predicted); THE DEBIT-COUNT LITERALS: the checkpoints holding the open debits on israel_people as a literal (DB7 and the older ones 8b
retyped 8 → 9: 5b's CV2, CX2, CW3, CR3 — the grep at RUN B decides the list) MOVE 9 → 10 with the ceremony's debit: THE STALE LITERALS predicted, retyped from
the print BEFORE the tape (7b's lesson 12; 8b's lesson — the newest sitting's own checkpoints join the list).

THE NAME: cold_run_blessing_and_curse.py — the 66th runner (the blessing and the curse set, 11:26 — the chapter's law; the unit deu_11_bless_curse_set); the
daemon law_blessing_and_curse, given_at Deut 11:1, installed_by boot (the Deuteronomy daemons' form); six cells F1-F6.

THE READBACK ON THIS CHAPTER — THE FORMS ON FILE, NO NEW FORM: T1 reference rows against the tape's lines by kind and first verse (11:2-7 the exodus, the sea,
Dathan and Abiram; 11:24 the borders' spec; 11:18-20 the Shema's line) — EVERY ACT THE CHAPTER RETELLS HAS A LINE (measured): NO retrograde marker, NO act
told only here, NO T2 row; T4 THE LAWS' FORM ON THE KIN (11:1, 8-9, 13-25, 26-28, 31-32 against the cells that compile them, by CALL); T5 THE STATE ROW (11:5
"what He did for you in the wilderness until you came to this place" — chapter 8's fifth form: SUPPLIED, no write, no day; the owner's open decision reused
unchanged); THE CODE'S HOLES compiled at the chapter's own day (40, 11, 1), NO marker, after the tape's last Deut 10 line: (a) THE RAIN CONDITIONAL and (b)
THE BLESSING-AND-CURSE SET WITH THE CEREMONY'S DEBIT; the receipt at 11:25 a RUN_CITATION pointer (the census decides); Joshua's receipts DATA rows (the run
outside the tape — 1:3-5, 1:11, 5:6, 22:5, 23:16, 24:31; Rahab's 2:10; 8:30-35 the ceremony run). THE DECISIONS (the design's, open to the owner's word; the
docket to confirm the names — 7b's lesson 7): (1) THE RAIN CONDITIONAL (11:13-17) — ONE LINE second_paragraph_declared (STATUTE by form — "and it shall be, if
you hearken, hearken …": chapter 7's hearing_blessed the form, 7:12's "and it shall be, because you hear") writing THREE effects: rain_in_its_season — a
conditional HEAVEN entry on israel_people (blessings_for_hearing's form; value 'the rain of your land in its season, the early rain and the late rain; grain,
wine and oil; grass for your cattle — if you hearken (11:13-15); Leviticus 26:4 by CALL'), heavens_shut_for_turning — a conditional HEAVEN entry on
israel_people (value 'the heavens shut, no rain, the ground without its produce, perishing quickly from the good land — if you turn aside and serve other gods
(11:16-17); Leviticus 26:19-20 by CALL; 28:12 the pair the shelf reads at 40:12 and 306:4-9; the shutting verb the wombs' — 306:6, Ta'anit 8b:1'), and
yoke_of_the_commandments_accepted — a STATUS on israel_people, THE MISHNAH'S OWN NAME FOR THIS PARAGRAPH (Berakhot 2:2 — the first paragraph the yoke of the
kingdom of heaven, the second the yoke of the commandments; Berakhot 13a-b the docket): the paragraph's duties (11:18-20) are 6:6-9's said again in the plural
— rows by CALL against hear_o_israel.the_four_duties, NO second shema line; the warning 11:16 against the second word's block other_gods_barred by CALL
(VARIANT — "serve … and bow down" 5:9's pair in the other order), NO second block (a warning by "take heed" is not a new prohibition — 4:23's form). (2) THE
BLESSING AND THE CURSE SET (11:26-32) — ONE LINE blessing_and_curse_set (STATUTE by form — "See, I set before you today …") writing TWO effects:
blessing_and_curse_set — a STATUS on israel_people (value 'the blessing if you hearken, the curse if you do not (11:27-28); the choice commanded at 30:19 ahead
— 53:1's crossroads, 54:1'), and gerizim_ebal_ceremony_owed — a DEBIT on israel_people toward Heaven (value 'the blessing on Mount Gerizim and the curse on
Mount Ebal, beyond the Jordan opposite Gilgal (11:29-30); the form at 27:11-13 — the Levites, the loud voice, the holy tongue, the Amen (55:2; Mishnah Sotah
7:5); the closer Joshua 8:30-35 — THE RUN, outside the Torah's tape'): OPEN on the tape (chapter 7's form — the ban's debit open to Joshua); the open debits
on israel_people 9 → 10; no closer, no timer. (3) THE STATE ROW 11:5 — SUPPLIED, NO WRITE (chapter 8's decision reused; the owner's word standing open). (4)
THE RECEIPT 11:25 "as He spoke to you" — a RUN_CITATION POINTER at Deut 11:25 (the AS_WHEN form) to ordinances.land's Exodus 23:27 clause ("I will send My
terror before you and confound all the people") — THE CALLEE NAMED BY THE TEACHER (the Sifrei 52:4: "and where did He speak? — Exodus 23:27"), a REFERENCE
link through the row; IF the census demands the form (the design's prediction, the census decides — 4b's, 5b's, 6b's, 7b's, 8b's lesson); the register file
untouched (no seat declared in the chapter; the finder's third form (10:9's, with the Name) and this fourth shape (1:11's, without it) OWED to a gate sitting
on the owner's word — COMPILE_DEBT). (5) THE RAIN'S DATES — a PARAMETER, never a constant: the mention from the last day of the feast and the request from the
seventh of Marcheshvan (Mishnah Ta'anit 1:1-3 through the Gemara's citations — the export lacks Mishnah_Taanit; Ta'anit 2a-3a), the early rain's three dates
(Ta'anit 6a — the third, the seventh, the seventeenth of Marcheshvan; the link rows on 11:14) and the late rain in Nisan: written into
calendar_parameters.yaml as rain_dates with the docket's rows (the sojourn_start form — a parameter no cell reads yet; a DATA row); no timer, no clock walk.
(6) THE FRONTLETS' SPELLINGS — the tefillin cell's open row STANDS (hear_o_israel.the_four_duties 'tefillin_compartments' over the DB's plene 11:18; the
reading's measurement asserted on the runner as a DATA row; no change to the DB). (7) THE CEREMONY'S PLACE — a PARAMETER (gerizim_ebal_place: Shechem by the
analogy with Genesis 12:6 — 56:3, R. Judah / the two mounds by Gilgal — R. Eliezer, Sotah 33b-34a) recorded with the Samaritan "Shechem" a DATA row, the tape
unmoved. (8) THE LAND-BOUND PARTITION (44:1) — borders.the_land_and_its_fall('the_land_bound_rule') ALREADY A CELL (Numbers 34's compile): by CALL, a DATA
row; the exile's cause (43:34), the study before the deed (41:12 — Kiddushin 40b) and the dwelling weighed against all (80:4-5; Ketubot 110b-111a) DATA rows.
(9) THE DISPOSSESSION (11:23-25) — NO WRITE: the promise's rows by CALL (nations_devoted's line 7:1-5 by kind; do_not_fear's little_by_little and the_hornet
7:20-24; ordinances.land 23:27-31; borders.the_four_sides('the_promised_extents') — 11:24 against Exodus 23:31 / Genesis 15:18 / Numbers 34:6, the Sifrei
51:2's analogy "shall be" the cell's own comparison; the STATUS borders_declared UNMOVED); "than you" 4:38 / 9:1 by CALL (50:4's E10 a DATA row).

THE ROWS (about thirty-two predicted, one per verse; the grades' census typed from the runner's print at RUN B): 11:1 "you shall love the LORD your God and
keep His charge, His statutes, His judgments and His commandments always" — shema_commanded (6:5's love) and demand_declared (10:12's fear, walk, love, serve,
keep) by kind: VARIANT ("His charge" the book's one seat — a DATA row; the Memra at 11:1 Onkelos's); 11:2 "know today — not your children who have not known
and have not seen the discipline of the LORD" — good_land.the_way_of_forty_years('the_discipline' — 8:5) by CALL: VARIANT (the noun's one Torah seat; the
children the second census counts — second_census by CALL); 11:3 "His signs and His deeds in the midst of Egypt to Pharaoh" — plague_struck (Exod 12:29) and
the plagues' lines by kind, exodus_story.plagues by CALL: VERBATIM in kind ("signs and deeds" 7:3's pair); 11:4 "what He did to the army of Egypt, its horses
and chariots, over whom He made the waters of the Red Sea flow as they pursued you, and the LORD destroyed them to this day" — sea_returned (14:27-28) by kind
with egypt_drowned (the DESTROY on Pharaoh's host), pursued (14:8-9): VERBATIM in kind, the verb TURNED ("made flow" the hiphil's one seat; "to this day" the
run's stamp); 11:5 "what He did for you in the wilderness until you came to this place" — THE STATE ROW: SUPPLIED, no write (decision 3); 11:6 "what He did
to Dathan and Abiram, sons of Eliab son of Reuben — the earth opened its mouth and swallowed them, their households, their tents and every living thing at
their feet, in the midst of all Israel" — earth_swallowed (16:31-34) by kind: VARIANT (the tape's "their households" and "every person who belonged to Korach"
against the retelling's "their tents and every living thing at their feet"; Korah unnamed on both — korach_named False asserted; second_census.the_roll
('hu_dathan', 'korach_recalled' — 26:9-11) by CALL; "every living thing" the flood's word — all_flesh_expired by kind, a DATA row); 11:7 "for your eyes have
seen every great deed of the LORD which He did" — a declaration (Joshua 24:31 and Judges 2:7 the run's sentence — a DATA row); 11:8-9 "keep all the
commandment … that you may be strong and go in and possess … and prolong days on the land the LORD swore to your fathers" — good_land.the_frame (8:1
'all_the_commandment', 'live_and_possess', 'the_oath_seats') by CALL, sworn_by_himself (Gen 22:16) by kind: VERBATIM in kind (11:8 against 8:1 twelve tokens;
"that you may be strong" one seat with Ezra 9:12; "to give to them" the resurrection's word at 11:21 — a DATA row); 11:10-12 "the land you are entering is
not like the land of Egypt … a land of hills and valleys, drinking water by the rain of heaven, a land the LORD your God cares for; the eyes of the LORD your
God are always on it" — good_land.the_good_land (8:7-10) and hear_o_israel.the_header('the_land_flowing') by CALL, lot_chose (Gen 13:10 — "like the land of
Egypt", Lot's clause) by kind: EXPANDED (the comparison with Egypt, the garden's labor against heaven's rain, the year's frame — THE DECLARATION THAT GROUNDS
THE CONDITIONAL; the Sifrei 37-40; Ta'anit 9b-10a the Land drinks first — the exam); 11:13-15 "if you hearken, hearken to My commandments … I will give the
rain of your land in its season, the early rain and the late rain … grass in your field for your cattle, and you shall eat and be satisfied" — THE LINE
second_paragraph_declared with rain_in_its_season: against tochacha.covenant (Leviticus 26:3-5) by CALL: VARIANT (26:4 "I will give your rains in their season"
against 11:14 "I will give the rain of your land in its season, THE EARLY RAIN AND THE LATE RAIN" — the two named rains ADDED, a DATA row; 7:13's grain, wine
and oil by CALL — VERBATIM in kind; "with all your heart and with all your soul" 6:5's tokens by kind; "My commandments" inside Moses' speech a DATA row);
11:16 "take heed to yourselves lest your heart be deceived and you turn aside and serve other gods and bow down to them" — other_gods_barred (the second
word's block at (1, 3, 7)) by CALL and good_land.the_testimony('other_gods_serve_bow' — 8:19) by CALL: VARIANT (the warning's form "take heed to yourselves"
4:23's; the prohibition already written — NO second block); 11:17 "and the anger of the LORD be kindled against you and He shut the heavens and there be no
rain and the ground not give its produce, and you perish quickly from off the good land" — heavens_shut_for_turning against tochacha.cascade (26:19-20 the
heavens as iron) by CALL: VARIANT (the shutting verb the wombs' — 306:6, Ta'anit 8b:1; "perish quickly from off the good land" = Joshua 23:16 — the run's
receipt, a DATA row; 28:12 the pair ahead); 11:18 "put these My words on your heart and on your soul, bind them for a sign on your hand and let them be
frontlets between your eyes" — shema_declared's 'bind' by kind and hear_o_israel.the_four_duties('tefillin_arm', 'tefillin_head', 'tefillin_compartments',
'tefillin_passages') by CALL: VERBATIM in kind (THE SPELLINGS' OPEN ROW — the DB's plene 11:18 asserted as the DATA row; "between your eyes" plural; Menachot
34b:1 the four compartments, 37b:3, 44a:16 the link rows); 11:19 "teach them to your sons, speaking of them sitting in your house, walking on the way, lying
down and rising" — 'teach' by kind and the_four_duties('teach_your_sons', 'daughters_exempt') by CALL: VARIANT ("teach" the piel against 6:7's "repeat" —
Onkelos's two verbs; "your sons and not your daughters" 46:1 — Kiddushin 29b:8-10 the link rows, the exam); 11:20 "write them on the doorposts of your house
and on your gates" — 'write' by kind and the_four_duties('mezuzah_doorpost', 'mezuzah_gates', 'mezuzah_writing') by CALL: VERBATIM in kind (the two plurals
36:3 a DATA row; Menachot 34a:9, Berakhot 20b:6, Yoma 11b:8 the link rows); 11:21 "that your days and the days of your sons be multiplied on the land the LORD
swore to your fathers to give to them, as the days of the heavens above the earth" — the_header('your_sons_son') and sworn_by_himself by kind: VARIANT ("as
the days of the heavens above the earth" one seat; THE RESURRECTION FROM "TO THEM" — 47:2, Sanhedrin 90b:12 the link row; 99a:10 the messianic era — DATA
rows); 11:22 "if you keep, keep all this commandment … to love the LORD your God, to walk in all His ways and to cleave to Him" — cleaving_commanded (10:20)
by kind, second_tablets by CALL, good_land.the_way_of_forty_years('keep_walk_fear' — 8:6) by CALL: VARIANT (the second doubled infinitive; "to walk in all
His ways" 10:12's; 11:22 against Joshua 22:5 twelve tokens — the run's receipt; 49:1's imitation of the attributes Sotah 14a — 8b's docket credited); 11:23
"the LORD will dispossess all these nations from before you, and you shall dispossess nations greater and mightier than you" — nations_devoted (7:1-5) by
kind, seven_nations.the_seven_nations('the_seven'), not_righteousness.the_frame('nations_greater' — 9:1) and obey_horeb.the_one_god('to_dispossess_nations' —
4:38) by CALL: VARIANT ("than you" plural — 50:4's E10 a DATA row; the sin the pace — 50:2 with Exodus 23:29-30 by CALL); 11:24 "every place where the sole
of your foot treads shall be yours — from the wilderness and Lebanon, from the river, the river Euphrates, to the western sea shall be your border" —
borders_commanded (Num 34:1-12) by kind with borders_declared ON THE LAND, borders.the_four_sides('the_promised_extents', 'the_sea_as_border') by CALL,
ordinances.land('borders' — Exodus 23:31) by CALL, covenant_cut_with_abram (Gen 15:18) by kind: VARIANT (the four extents in the retelling's own words —
Joshua 1:3-4's receipt without the article; the returners' lines 51:2-3 a PARAMETER — Mishnah Sheviit 6:1 the answer sheet, Gittin 8a, credited); 11:25 "no
man shall stand before you: the dread of you and the fear of you the LORD your God will put on the face of all the land you tread, as He spoke to you" —
ordinances.land('angel' — 23:27's terror; 'hornet') and seven_nations.do_not_fear('the_hornet', 'little_by_little', 'the_kings_and_the_name' — 7:24's "no
man shall stand") by CALL, terror_of_god by kind (Genesis 35:5's STATUS on the cities — the form's seat): VARIANT — THE RECEIPT'S POINTER (decision 4); the
pilgrimage's guard Exodus 34:24 by CALL (calendar's pilgrim_land_guarded — 52:4's second reading, a DATA row); 11:26-28 "See, I set before you today a
blessing and a curse: the blessing if you hearken … and the curse if you do not hearken and turn aside from the way … to go after other gods" — THE LINE
blessing_and_curse_set with its STATUS: against hearing_blessed (7:12-16's conditional) by kind and the_testimony (8:19-20) by CALL: EXPANDED (the pair
named; "turn aside from the way" 9:12's calf — not_righteousness by CALL; 30:15-20 ahead; 54:4's idolatry the whole Torah's denial — Sotah 37a the exam);
11:29-30 "you shall set the blessing on Mount Gerizim and the curse on Mount Ebal — beyond the Jordan, behind the way of the sunset, in the land of the
Canaanite in the Arabah opposite Gilgal, beside the terebinths of Moreh" — THE DEBIT gerizim_ebal_ceremony_owed: NO tape line to reference (27:11-13 ahead —
chapter 27's compile the form's seat; Joshua 8:30-35 the run — OUTSIDE the tape): SUPPLIED AS A LAW (the debit's first seat; the place a PARAMETER — decision
7; Gilgal the Torah's one seat; journeyed 'the place of Shechem' Gen 12:6 by kind for Moreh — a DATA row; Sotah 32a:10, 33b:4, 37b:10 the link rows, the
exam); 11:31-32 "for you are crossing the Jordan … and you shall possess it and dwell in it, and keep to do all the statutes and the judgments which I set
before you today" — good_land.the_frame('live_and_possess') by CALL: VERBATIM in kind ("possess it and dwell in it" one seat — 80:4-5's DATA row; Kiddushin
26a:10's possession the link row; "which I set before you today" 4:8's, 12:1 reopens — a DATA row). THE HOLES: TWO IN THE CODE (the rain conditional; the
blessing-and-curse set with the ceremony's debit) compiled at the chapter's own day; NONE told only here (every act 11:2-7 names has a line — measured); the
receipt a pointer; the state row supplied without a write.

THE CELLS (F1-F6; every token probed; effects on every cell; the exam's rows the docket's crowns): F1 THE DISCIPLINE RETOLD (11:1-7): the six reference rows
and the state row; the exam: Pesachim 119a:12 and Sanhedrin 110a:11 (Korah's wealth from 11:6 — the link rows), the Korah docket credited. F2 THE LAND
WATERED BY HEAVEN (11:8-12): the rows by CALL; the exam: Ta'anit 9b-10a (the Land drinks from the upper waters, the world from the residue — 9b:11 the link
row on 11:11), Shabbat 85a:3 (the garden bed — the link row on 11:10), Rosh Hashanah 16a-17b (the year judged at four seasons; the rain's measure fixed at the
head of the year — 16b:3 the link row on 11:12; 17b:11 the baraita "a land which the LORD cares for" — the exam), Rosh Hashanah 7a-9b (the New Year for years
from 11:12's "from the beginning of the year" — 7a:18, 8a:16, 8b:6, 9b:11 the link rows), Berakhot 55a:9 (three things need mercy — the rain among them, from
11:12), Bava Batra 19a:18 (the link row on 11:11). F3 THE SECOND PARAGRAPH (11:13-21): the line and its three writes; the rows by CALL; the exam: Mishnah
Berakhot 2:2 and Berakhot 13a-16a (the paragraphs' order — the yoke of the kingdom before the yoke of the commandments; 13b:5, 14b:13, 15b:27, 16a:4-5 the
link rows; 146 of the 191 rows credited from chapter 6's docket, the rest read here), Berakhot 20b:6 (women obligated in mezuzah — the link row), Menachot
28a:6, 31b:7-9, 32a:1, 34a:9, 34b:1-9, 35a:1, 37b:3 (tefillin and mezuzah — the link rows; 34a-37b credited whole from 4b's docket, listed with its ledger),
Menachot 44a:16-19 (eight positive mitzvot of tefillin; two of mezuzah — the link rows), Kiddushin 29b:8-10, 30a:5-6, 30b:3 (teach your sons; "and you shall
place" — the link rows; 29a-30b credited from 4b), Kiddushin 34a:2-8 (women exempt from the time-bound; mezuzah juxtaposed to study — the link rows),
Kiddushin 36a:9 (Isi's verbal analogy "between your eyes" — the link row), Kiddushin 36b-37a (the land-bound — credited whole), Ta'anit 2a-3a (the mention
of rain from 11:13-14 — 2a:11 the link row; 3b:6 on 11:17), Ta'anit 6a:3-7 and 6b:8 (the early rain's three dates; the first rainfall — the link rows on
11:14, 11:17: THE PARAMETER'S ROWS), Ta'anit 7a-10a (the rain as Torah; the rain withheld for the sin — 7b:5, 8a:18, 8b:1 the link rows on 11:17: Reish
Lakish's "closing up" by the wombs = the Sifrei 306:6), Berakhot 33a (the mention of rain in the second blessing — the exam), Berakhot 35b:4 and 40a:1
(11:14-15 — "you shall gather your grain" the way of the world; the cattle fed before the man — with Gittin 62a:16 the link rows), Sanhedrin 90b:12 and
99a:10 (the resurrection and the messianic era from 11:21 — the link rows; 90b credited whole), Bava Batra 21a:2, 110b:7, Berakhot 8a:6, Yoma 11b:8, Chullin
135b:15, Shabbat 32b:4, 105b:11 (the link rows on 11:19-21 — the schools of Joshua ben Gamla; a son before a daughter; the elders' days; the joint house's
mezuzah; children die for the mezuzah's neglect), Sanhedrin 113a:11 and Yevamot 78b:14 (11:16-17 — Ahab and the rain; David's decree — the link rows),
Zevachim 37b:14 (the link row on 11:18), Mishnah Menachot 3:7, Mishnah Sotah 7:8, Mishnah Tamid 5:1, Tamid 32b:8, Sotah 41a:18, Tosefta Sotah 7:9 (the
paragraph in the king's reading and the daily service — the link rows). F4 THE BORDERS AND THE DREAD (11:22-25): the rows by CALL; the pointer; the exam:
Kiddushin 26a:10 (possession — the link row on 11:31), Gittin 8a and Mishnah Sheviit 6:1 (the borders by the returners — credited), Pesachim 8b (the
pilgrimage guarded — 52:4's Exodus 34:24), Kiddushin 40b (study and deed — 41:12), Ketubot 110b-111a (dwelling in the Land — 80:4-5), Sukkah 52a (the
inclination — 45:1; two rows credited from 8b). F5 THE BLESSING AND THE CURSE, GERIZIM AND EBAL (11:26-32): the line and its two writes; the exam: Mishnah
Sotah 7:5 and Sotah 32a:10, 33b:4, 37b:10 (the ceremony and the mountains — the link rows on 11:29-30), Sotah 32a-37b (the ceremony's form, the place, the
Amen, idolatry the whole Torah — 121 of 188 rows credited from chapter 7's docket, the rest read here), Tosefta Sotah 8:6 (the miracles of the day — the link
row) and Tosefta Sotah 8 whole (7 rows), Tosefta Sheviit 4 whole (16 rows — the baraita of the borders, 51:3). F6 THE READBACK TABLE (the_readback — the
thirty-two rows with their grades, the state row, the pointer, the DATA rows). THE DATA ROWS (about eighteen): the readback table; Korah unnamed on the tape
and in the retelling; "every living thing" the flood's word; the two named rains added to Leviticus 26's; the frontlets' three spellings (the DB's plene
11:18); the doorposts' two plurals; the receipt's fourth shape and "as He spoke" sixteen in the book; the borders' four extents against three seats; the
returners' lines a PARAMETER; the rain's dates a PARAMETER; the ceremony's place a PARAMETER with the Samaritan variant; Gilgal the Torah's one seat; Moses
unnamed 6-14; no number verse; Joshua's seven receipts; the portion edge inside the chapter; the open debits 9 → 10.

THE LINES ON THE TAPE (the recorder and the stitcher; the design's arithmetic): NO MARKER; TWO OWN-DAY LINES after the tape's last Deuteronomy 10 line
(cleaving_commanded) — second_paragraph_declared (11:13-21) and blessing_and_curse_set (11:26-32), both STATUTE by form (the stitcher's register test dropped
chapter 6's as speech — 4b's lesson, the form declared); THE DAEMON'S FIVE WRITES — rain_in_its_season (a HEAVEN entry, conditional, on israel_people),
heavens_shut_for_turning (a HEAVEN entry, conditional), yoke_of_the_commandments_accepted (a STATUS), blessing_and_curse_set (a STATUS),
gerizim_ebal_ceremony_owed (a DEBIT, open — the counterparty Heaven). THE TYPES (add_types_ch11.py, after the probes' FAIL print): event_vocabulary +3
(second_paragraph_declared, blessing_and_curse_set — form statute, witnesses Deut 11:13 and 11:26; blessing_curse_case — the exam's case kind) 1142 → 1145;
effect_vocabulary +5 (rain_in_its_season, heavens_shut_for_turning — heaven; yoke_of_the_commandments_accepted, blessing_and_curse_set — status;
gerizim_ebal_ceremony_owed — debit; the names the docket confirms) 1037 → 1042; daemon_dispositions (law_blessing_and_curse — file, wraps blessing_and_curse,
given_at Deut 11:1, installed_by boot, watches {second_paragraph_declared: [rain_in_its_season, heavens_shut_for_turning, yoke_of_the_commandments_accepted],
blessing_and_curse_set: [blessing_and_curse_set, gerizim_ebal_ceremony_owed], blessing_curse_case: [accepted, exempt]}; the functions block's six cells
WRAPPED); dependency_dispositions (the span [[Deut, 11, 1, 32]]; the CALL edges predicted FIFTEEN — hear_o_israel, good_land, seven_nations,
not_righteousness, obey_horeb, second_tablets, covenant_at_horeb, tochacha, ordinances, borders, korach, second_census, exodus_story, primeval, calendar — the
census decides; ONE AS_WHEN pointer predicted, Deut 11:25 — RUN_CITATION of ordinances.land's Exodus 23:27 with the Sifrei 52:4 the teacher — the census
decides); installation_probes I5 70 → 71; calendar_parameters.yaml +1 (rain_dates — the docket's values); the register file untouched (DECLARED 100).

THE PREDICTION'S ARITHMETIC: RUN = (1319, 96, 88, 0, 12, 1618, 42, 319, the four pairs, 127) — events +2, timers set +0, fired +0 (no clock walk), cancels 0,
retro-writes 12 UNMOVED, writes +5 (the daemon's five), daemons fired +1 (law_blessing_and_curse), entities +0 (israel_people on the registry; Heaven a
counterparty, not an entity — 7b's lesson 5), closes +0 (the debit OPEN); PREVIOUS_RUN = 8b's RUN EXACTLY (1317, 96, 88, 0, 12, 1613, 41, 319, the four pairs,
127): THE REST drops the two lines by the runner's tag and the span and the daemon's five writes with them — no delta; NEWEST_RUNNER 'blessing_and_curse';
markers 172 UNMOVED (PLACEMENT markers text_constrained 108, reading_placed 49 unmoved); events page_order 1149 → 1151, text_constrained 110 and
reading_placed 58 UNMOVED — READ, never predicted; CENSUS on tape 1317 → 1319, history +2, kinds 862 → 864, subjects 272 UNMOVED (israel), markers 172, closes
71 unmoved; the population table 148 UNMOVED; THE OPEN DEBITS ON israel_people 9 → 10 (the literals move — grepped); the scene's tuple PREDICTED BY SCRIPT at
the runner step (the exam's persons through blessing_curse_case — each written once; no timer; no close); the narrative's (its own world: the five writes, 0
closes, the entity israel, the counter's day (11, 1), no row).

THE CHECKPOINTS DC1-DC9 (the D series at its third name; the literals typed from the prints at RUN B):
DC1 THE LINES — two events on the tape AFTER the tape's last Deuteronomy 10 line: second_paragraph_declared and blessing_and_curse_set on the counter's day
(40, 11, 1), NO marker (markers 172 UNMOVED); the counter ends at (40, 11, 1).
DC2 THE WRITES — rain_in_its_season ONE and heavens_shut_for_turning ONE on israel_people (HEAVEN entries, conditional, source beginning "Deut 11:13"),
yoke_of_the_commandments_accepted ONE (a status), blessing_and_curse_set ONE (a status, source beginning "Deut 11:26"), gerizim_ebal_ceremony_owed ONE (a
debit, OPEN — no close on the tape); law_blessing_and_curse registered, given_at Deut 11:1, installed_by boot; the six cells WRAPPED.
DC3 THE READBACK — the_readback's rows (thirty-two; the census from the print), every reference row's entry FOUND: the tape lines by kind and first verse
(plague_struck Exod 12:29, brought_out Exod 12:51, pursued Exod 14:8, sea_split Exod 14:21, sea_returned Exod 14:27, earth_swallowed Num 16:31,
all_flesh_expired Gen 7:21, lot_chose Gen 13:10, covenant_cut_with_abram Gen 15:18, journeyed Gen 12:6, borders_commanded Num 34:1, shema_declared Deut 6:4,
nations_devoted Deut 7:1, hearing_blessed Deut 7:12, demand_declared Deut 10:12, cleaving_commanded Deut 10:20) and the kin's cells by CALL (each returning
its verdict on its own ask); the state row SUPPLIED with no write; the pointer; no retrograde row.
DC4 THE RAIN'S HOLE — NO effect naming the rain, the heavens shut or the yoke on israel_people BEFORE this daemon's lines (the ledger scan on the running
world at the tape's Deut 10 end: EMPTY — asserted before the lines run) and ONE each after; the vocabulary's 'rain' before this sitting fire_rained alone
(asserted on the registry at the commit 2f4ec5b).
DC5 THE DEBIT — gerizim_ebal_ceremony_owed OPEN on israel_people; the open debits 9 → 10 (the count computed on the world; the older checkpoints' literals
retyped from the print); no closer on the tape (Joshua 8:30-35 the run — outside); love_owed and the ban's debit UNMOVED.
DC6 THE KIN STAND — shema_commanded ONE, test_barred ONE, blessings_for_hearing ONE, pity_barred ONE, fear_of_heaven_asked ONE, cleaving_commanded ONE,
love_owed ONE on israel_people UNMOVED; other_gods_barred ONE and coveting_barred ONE UNMOVED (no second block at 11:16); borders_declared ONE on
the-land-of-canaan UNMOVED; pilgrim_land_guarded UNMOVED; NO second shema line (asserted on the world).
DC7 THE RETELLING'S LINES UNMOVED — earth_swallowed ONE (subject dathan, korach_named False, the swallowed list the tape's four); egypt_drowned ONE on
Pharaoh's host; plague_struck TEN; sea_split ONE and sea_returned ONE; all_flesh_expired ONE; the closes to_be_wiped, pursued_by_egypt and to_be_delivered
UNMOVED (no second close).
DC8 THE SPELLINGS AND THE EXTENTS — the DB's three frontlet tokens (6:8 defective, 11:18 and Exodus 13:16 plene) asserted at the tape as the DATA row; the
doorposts' two plurals; the borders' extents — borders.the_four_sides('the_promised_extents') by CALL returning its own comparison (Exodus 23:31, Genesis
15:18, Numbers 34, Deuteronomy 1:7 and 11:24); the rain's dates a parameter row on file (rain_dates), no clock use.
DC9 THE REST — entities 319 UNMOVED, closes 127, markers 172, the population table 148 UNMOVED, the two kinds present; the other counts 8b's exactly with
the two lines and the five writes dropped (THE REST test — NO declared delta). THE STALE LITERALS predicted (grepped at the design): the checkpoints holding
the open debits on israel_people as a literal (DB7; 8b's retyped older ones — 5b's CV2, CX2, CW3, CR3; the grep at RUN B decides the list) — retyped 9 → 10
from the print BEFORE the tape; every miss shown at once by checkpoint_check.py --all AFTER the tape.

THE PROBES (RUN B's FIRST step, before the types — 7b's lesson 2): readback_probes.py Q28-Q30 written to FAIL before the runner exists — Q28 the runner and
its the_readback table (the rows and their census typed from the print; every reference row's entry found; the state row; the pointer; no retrograde row);
Q29 the two own-day lines on the counter's day (40, 11, 1) with NO marker (markers 172 UNMOVED) and their five writes on israel_people (the two HEAVEN entries
conditional; the debit OPEN; the open debits 10); Q30 the kin standing (DC6-DC7's counts) and the rain's hole filled (DC4); Q22-Q27 unchanged (no marker
count moves); NO parser rule this sitting (no number verse — census_probes unmoved at 224); the register gate: no seat in the chapter (DECLARED 100 unmoved;
the fourth shape a COMPILE_DEBT line); checkpoint_probes' verse computed (2b's form).

THE ORDER: this design → the state doc's checkpoint (#199 — RUN A closed) → THE DOCKET, ITS OWN RUN: the dump (ch11_docket_dump.txt, 3,149 lines — 74 LINK
rows in 20 works and 952 TOPIC rows: the fifteen folio ranges (Berakhot 13a-16a 191, Menachot 34a-37b 98, Kiddushin 29a-30b 75, 36b-37a 24, 40b 14, Ta'anit
2a-3a 44, 7a-10a 118, Berakhot 33a 37, Rosh Hashanah 16a-17b 67, Gittin 8a 11, Pesachim 8b 17, Sotah 32a-37b 188, Ketubot 110b-111a 52, Sanhedrin 90b 21,
Sukkah 52a 13) and the ten Mishnah rows; Tosefta Sotah 8 (7 rows) and Tosefta Sheviit 4 (16) whole; the export lacks Mishnah_Taanit — its rows through the
Gemara's citations), 622 CREDITED BY ADDRESS at the scan — the chapter-6 docket 339 (Berakhot 13a-16a 146 of 191; Menachot 34a-37b 98 of 98; Kiddushin
29a-30b 75 of 75), the Devarim docket 75, the Exodus triage 52, the Musafim docket 48, the Genesis triage 44, the borders' docket 38, the Gad-Reuben docket
37 (Kiddushin 36b-37a 24 of 24), the chapter-5 docket 36, chapter 7's 27 (Sotah 32a-37b 121 of 188), the Shelach docket 26, chapter 10's 18 — every credited
row READ WHOLE at its docket and listed here with its ledger; the some 450 UNCREDITED rows READ WHOLE here (Ta'anit 7a-10a 98, Sotah 32a-37b 67, Ketubot
110b-111a 48, Berakhot 13a-16a 45, Berakhot 33a 35, Rosh Hashanah 16a-17b 35, Kiddushin 40b 14, Ta'anit 2a-3a 13, Pesachim 8b 13, Sukkah 52a 11, the
Tosefta's 23, the uncredited link rows) — the parts on 8b's whole-row instruments (ch10_docket_A/B/C.py, ch10_docket_common.py, ch10_docket_rows.py
derived), EVERY ROW WHOLE, the verdicts LAW / DERIVATION / DISPUTE / CONTEXT / OUTSIDE with the credits computed, the writer write_ch11_docket.py, the
docket's records (COMPILE_DEBT's box (n), MIDDOT — every code checked in MIDDOT.md before it is typed, MISHNAH_TOPICS, the state doc's checkpoint) → RUN B:
the probes to FAIL (patch_probes_ch11.py: Q28-Q30; the debit-count literals retyped 9 → 10), the types (add_types_ch11.py — the docket's names; the calendar
parameter), the callees' facts printed before any assert (ch11_callees.py — every CALL named above), the runner in parts with the fast checker
(ch11_fastcheck.py) and the generated CASES (ch11_cases_gen.py; the guard's count from the generator's print), the recorder (seq_record_ch11.py, INK_CACHE=0)
and the stitcher (seq_stitch_ch11.py; no marker — the two lines on the counter's day), the literals DC1-DC9 and the VERDICTS entries
(patch_seq_literals_ch11.py), the tape to 10/10 with THE REST, checkpoint_check.py --all AFTER the tape, gates_chain.sh in one summary (the cache in place:
the moved runner's own harvest once; the sweep of the moved runners and their importers), the records from the sheet in one call (write_ch11b_records.py:
the map's AS BUILT, COMPILE_DEBT's sitting-9 box PAID and the 9b box, MIDDOT, MISHNAH_TOPICS, RESEARCH_LOG, THE_STEPS, THE_BRIEFING, THE_LOOP's step-6 row,
RESUME, RECORD_FORMS, the state doc, the addenda, the recovery page, the memory), the forms copied (copy_ch11b_forms.py), the commit message (this sitting's,
for the owner's word).
'''
assert not re.search(r'/Users/(?!Shared/)', D) and '<home>' not in D   # the username never typed, not even as a guard (the home-path gate refused the copy at the commit: the guard's literal was the username)
open(MAP, 'a', encoding='utf-8').write('\n\n' + D)
out = subprocess.run([sys.executable, f'{ROOT}/logic/solo_tools/gloss_lint.py', MAP], capture_output=True, text=True).stdout
print('design appended:', len(D.encode()), 'bytes; the map', os.path.getsize(MAP), 'bytes;', out.strip().split('\n')[-1])
