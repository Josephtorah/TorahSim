import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE DEUTERONOMY WALK sitting 11b — THE COMPILE OF CHAPTER 13: THE DESIGN appended to the map at the close of RUN A, after the rereads and the measurements
# (ch13_compile_recon.py, ch13_docket_scan.py) and BEFORE any code — write_ch13_design.py's form (the previous last section asserted, the section appended
# whole, the lint after). Every number below is read from the recon's and the scan's prints named beside it.
import os, re, subprocess
ROOT = _ROOT
P = f'{ROOT}/World/step9/DEUTERONOMY_WALK.md'
s = open(P, encoding='utf-8').read()
assert s.rstrip().split('\n## ')[-1].startswith('Sitting 11 — CHAPTER 13 — AS BUILT'), 'the previous last section is not sitting 11\'s AS BUILT'
assert '## Sitting 11b — THE COMPILE OF CHAPTER 13' not in s
SEC = '''


## Sitting 11b — THE COMPILE OF CHAPTER 13, Deuteronomy 13:1-19 (2026-09-21; the owner: "Go" after sitting 11's tail — the commit still on his word, sitting 11 uncommitted since 2b0c9c8): THE DESIGN — written at the close of RUN A under THE COST RULES (two runs + the tail; the rereads: THE_STEPS' compiler block whole, Step 2's head and Step 5's head, the sitting-11 AS BUILT and the 11b box (a)-(l) in the tail's own context, the 10b design and AS BUILT as the compile's form; the measurements: ch13_compile_recon.py derived from 10b's by asserted line-based block substitutions (derive_ch13_recon.py — one header line missed and caught by the derive's own guard; 16 s), ch13_docket_scan.py derived from 10b's (derive_ch13_docket_scan.py — the English numbering's 12:32 folded to 13:1, one new line; its first run fell on a chapter past an export's end, guarded; 135 s) — all in the scratchpad) and BEFORE any code; the docket ONE RUN by the ~700 clause (566 addresses in the dump; 196 credited by address at the scan; some 370 to read whole)

THE RUNS AND THE DOCKET'S OWN: RUN A the rereads, the measurements and this design — CLOSED HERE, a clean compaction point (#203); THE DOCKET by the union rule in
ONE RUN (the 91 link rows; Sanhedrin 67a, 88b, 89a-90a, 40a-41a, 111b-113b; Zevachim 80a-81b; Sukkah 34b; Menachot 41b-42a; Rosh Hashanah 28b; Eruvin 96a; Avodah
Zarah 49b-50a; Bava Metzia 59b; Yevamot 90b; Shabbat 151b; the twenty-two Mishnah rows; Tosefta Sanhedrin 11, 12, 14; the Sifrei on Numbers 103, 113, 114), EVERY
ROW WHOLE — the 196 credited rows CARRIED with their ledgers' own verdict lines (10b's form, ch12_credit_carry.py derived), the uncredited read whole in chunk files
(the cap 64,000 — 10b's D2 lesson), the writer derived from 10b's, coverage computed — its own clean point; RUN B the probes to FAIL (readback Q34-Q36, BEFORE the
types — 7b's lesson 2), the types by script with the docket's names, the callees' facts printed before any assert (every CALL's ask read at the cell's own source —
10b's lesson 2), the runner in parts with the fast checker and the generated CASES, the recorder with the cache OFF (7b's lesson 1) and the stitcher, the literals
DE1-DE9, the tape to 10/10 with THE REST, checkpoint_check.py --all AFTER the tape, the records writer and the copier WRITTEN, gates_chain.sh LAUNCHED in the
background (the positions step at FOUR workers if the owner rules it; eight the standing form), the clean point; THE TAIL after the compaction: the summary read
once, the demands filed, the records from the sheet in one call, the forms copied, this section's AS BUILT, the commit message for the owner's word.

THE MEASUREMENTS (what the tape, the runners, the registries and the running world say before a line is typed — ch13_recon.out, sectioned in ch13_recon_excerpt.txt):
THE COUNTER stands at (40, 11, 1), day 908865; the tape's LAST LINES are chapter 12's four own-day lines (demolition_restated, place_chosen_declared,
profane_slaughter_permitted, nations_cut_off_warned) after chapter 11's two, its LAST MARKER the forward marker at Deut 10:12 (M['speech_resumed_10']); RUN
(1323, 96, 88, 0, 12, 1626, 43, 319, the four pairs, 127), PREVIOUS_RUN 9b's (1319, 96, 88, 0, 12, 1618, 42, 319, the four pairs, 127); markers 172
(text_constrained 108, reading_placed 49), events text_constrained 110 / page_order 1155 / reading_placed 58; CENSUS (2520, 1319, 1323, 1185, 6, 10, 9, 0, 71, 172,
131, 15, 26, 868, 272); 67 runners, 72 daemons (installed_by boot 31, erected 3, covenant_blood_thrown 14, called_from_the_tent 17, sentence_declared 2,
statute_declared 2, milluim_blood_sprinkled 1, entered_the_land 1, pending 1), kinds 1150, effects 1049; the D series DA, DB, DC and DD in use (nine each) — THE
NEXT NAME DE (no code assumes a letter; the two startswith seats are on strings, not checkpoints); 67 spans, 648 edges, 207 pointers — NONE naming Deut 13; THE
REGISTER: NO seat naming Deut 13 (the reading's finder found no receipt, header or footer; 13:18's "as He swore to your fathers" the oath's AS_WHEN form); the
readback probes Q1-Q33 on file (Q10 unused), the next Q34. THE KIN'S CELLS, FOUND BY THE REFS PER DEF: THE HEADER'S TWIN IS A CELL — obey_horeb.the_exhortation
('add_nothing', 'diminish_nothing', 'add_beside', 'add_out_of_its_time' — 4:2's cell) and THE EFFECT adding_barred ON FILE, a BLOCK on israel_people written ONCE
at 4:1-8's line (six rows on the one database's run_ledger — ONE write by 10b's lesson 12; CC3 in cold_run_sequence.py holds "adding_barred on israel_people ONE" AS A
COUNT LITERAL — its own row read: ab_oh a list, the checkpoint its length); THE SECOND WORD — covenant_at_horeb.the_second_word (other_gods_barred ON FILE, a BLOCK
at 4:10-13's line — the seducers' "other gods" the second word's object by CALL); THE TESTING — hear_o_israel.the_test_and_the_right (test_barred ON FILE, 6:16;
tested_the_lord the counter STATUS), good_land.the_way_of_forty_years (8:2, 16's testing), mamre.moriah (Gen 22:1's tested — the first seat, the line on the tape;
god_fearing_known the verdict's STATUS); THE SIX VERBS — second_tablets ('cleaving_commanded' ON FILE, a STATUS on israel_people written ONCE at 10:20-22's line —
"fear, serve, cleave, swear (10:20) — 6:13 with the fourth clause added"), hear_o_israel (6:13-15 — the four verbs, the gods round about), blessing_and_curse
(11:13's heart and soul, 11:22's cleave, 11:28's other gods not known); THE BAN AND THE DEVOTED THING — seven_nations.the_seven_nations('the_ban',
'the_bans_condition'), .the_images_and_the_devoted('devoted_like_it', 'into_your_house', 'lest_snared' — house_abomination_barred ON FILE, 7:26), .hearing_blessed
(law_seven_nations writes pity_barred — 7:16's "YOUR EYE SHALL NOT PITY THEM": THE INCITER'S CLAUSE ALREADY AN EFFECT, ON FILE ONCE), temurah.devote (Lev 27:28-29 —
thing_devoted a CASE kind; no effect named 'devoted'), chukat.arad_and_the_serpent('cherem_law', 'hormah' — israel_vowed_the_cherem and canaanites_devoted_hormah_named
on the tape, the DEBIT cherem_vowed closed by 21:3, destroyed (body) on the_king_of_arad — THE BAN'S RUN CASE), ordinances.capital('idolater_row', 'devoted_seats',
'service_architecture' — Exod 22:19's sacrificed_to_gods, a CASE kind; the effect destroyed (body) "the idolatrous sacrificer's ban": THE BAN'S FIRST SEAT IS A
CELL); THE STONING — mekoshesh.capital_procedure('stones_and_a_stone', 'stoning', 'warning', 'venue', 'hanging', 'burial', 'confession', 'custody', 'mode',
'stripping'; the DATA stoning_house_height, warning_names_the_death, hanging_after_stoning: 90:1'S STONES AND THE STONE ARE IN THE ENGINE ALREADY — the
wood-gatherer's cell; law_mekoshesh writes stoned, hanged, buried on stoning_carried_out), lev24 (the blasphemer — law_lev24 writes stoned on blasphemed_the_name;
sentence_declared's 'hands_laid' — 24:14's witnesses' hands, 13:10's "your hand first" the kin), sanctions.census('stoned', 'strangled', 'burned', 'lashes',
'karet_count' — THE FOUR DEATHS' CENSUS the mode parameter reads; NO effect named 'strangled' on file — put_to_death carries "mode per the compiled law"),
sanctions.molech('who_stones' — Lev 20:2 the people of the land, 'family', 'concealed'), sanctions.frame('court_warned', 'karet_persons'); THE PROCEDURE —
ordinances.courts('acquitted_retried', 'circumstantial', 'dissenter', 'begin_from_side', 'enemy_ox' — Exod 23:5's ass, 89:2's standing duty) — THE COURT'S RULE
THAT 89:6-7 INVERTS IS A CELL; holiness.conduct('blood' — Lev 19:16 the neighbor's blood, 89:3's duty; 'hate', 'grudge', 'great_rule' — 19:18's love, 89:1's duty):
THE FIVE PROHIBITIONS' STANDING DUTIES ARE CELLS; THE CLOUD — erection.cloud('journeys', 'first_lifting'), beha.march (cloud_lifted on the tape at Num 10:11 —
85:1's run citation has a line), beha.miriam('dreams', 'dibbur' — Num 12:6-8, the dream God's channel; 83:2's citation); THE CALF — erection.calf('four_verbs',
'bow_likened', 'individual_r…'; calf_made Exod 32:4 on the tape — the seducers' formula "these are your gods" the run's case), not_righteousness.the_calf_retold;
THE FIERCE ANGER — balak.peor('anger_third', 'hang_before_the_sun'; hanging_commanded Num 25:4 on the tape; yoked_to_baal_peor, mark_of_anger the STATUSES); THE
HIGH HAND — shelach.high_hand('blasphemer_identity', 'despiser', 'karet_reason'; high_hand_case); THE RIGHT IN HIS EYES — place_name (12:25, 28) and
hear_o_israel.the_test_and_the_right('the_right_and_the_good'); THE NATIONS CUT OFF — place_name.the_nations_cut_off_and_the_abomination (12:29-31; the tape's last
line); THE PREAMBLE — covenant_at_horeb (5:6); THE REDEEMING — not_righteousness.the_intercession (9:26). THE REGISTRY: 'the-court' mapped to the_court; 'the-heap' to
the_heap — LABAN'S HEAP (Galeed, Genesis 31: the registry's homograph, named FALSE if the census matches it); 'the-friend' to ahuzzath (Abimelech's friend —
another homograph); 'the-cities' to the_cities_around_shechem (a third); 'the-people' to israel_people; NO registry row for the-prophet, the-dreamer, the-brother,
the-city, the-inhabitants, the-men, the-sword, the-spoil, the-devoted-thing — the chapter's persons are the exam's, no entity; 'purge_commanded' ON FILE is
JACOB'S (Genesis 35:2 "remove the foreign gods") — a homograph of the purge formula, FALSE if the token census matches it. THE KINDS AND EFFECTS ON FILE touching
the matter: sacrificed_to_gods (case), seed_given_to_molech (case), blasphemed_the_name, cursed_the_name (case), gathered_wood_on_the_sabbath, stoning_carried_out
(case — THE PROTOCOL), stoned_as_commanded, israel_vowed_the_cherem, canaanites_devoted_hormah_named, calf_made, calf_destroyed, tested, came_in_a_dream, dreamed,
dream_told, cloud_lifted, hanging_commanded, add_nothing_commanded, testing_barred, cleaving_commanded, nations_devoted, abomination_barred, nations_cut_off_warned,
high_hand_case, peor_case, witnesses_called; the effects adding_barred (block, ONE), other_gods_barred (block), test_barred (block), tested_the_lord (status),
cleaving_commanded (status, ONE), pity_barred (block, ONE — 7:16), house_abomination_barred (block), covenant_barred (block), stoned (body), put_to_death (body),
hanged (body), destroyed (body — Exod 22:19's ban; the king of Arad's), karet_cut_off (heaven), death_by_heaven (heaven), burned_by_court (body), lashes (body),
cherem_vowed (debit), hormah_named, mark_of_anger, mercy_prayed, prophet_declared (Abraham's), heaven_and_earth_witness, fear_of_heaven_asked, purge_deadline (a
timer — the LEAVEN's, a homograph) — and NO effect naming the false prophet's hearing barred, the LORD's testing declared as a law, Israel's hearing and fearing,
the condemned city's inquiry, the devoted thing cleaving to the hand, the evil purged from the midst, or a city devoted (the seven names asserted absent from both
registries at the design; adding_barred, cleaving_commanded, pity_barred, stoned, put_to_death present). THE DOCKET SCAN (ch13_docket_scan.out; the dump
ch13_docket_dump.txt 386,948 bytes, 1,700 lines): 91 LINK rows in 31 works (Sanhedrin 39, Avodah Zarah 7, Chullin 5, Mishnah Sanhedrin 4, Makkot 3, Bava Kamma 2,
Mishnah Avodah Zarah 2, Shabbat 2, Sotah 2, Tosefta Avodah Zarah 2, Yevamot 2, Rambam's Introduction 2, one each in seventeen more), the verses cited every one but
13:3 (13:18 the most — twenty-six rows on "nothing shall cleave"), THE ENGLISH NUMBERING'S 12:32 FOLDED TO 13:1 (the header cited so by Zevachim 80a:3, Eruvin
100a:18, Menachot 40b:10, Chagigah 8b:11 and Mishnah Zevachim 8:10 — the not-adding's law seats); 463 TOPIC rows (Sanhedrin 223 — 67a 23, 88b 19, 89a-90a 64,
40a-41a 64, 111b-113b 71; Zevachim 80a-81b 54; Menachot 41b-42a 40; Avodah Zarah 49b-50a 33; Rosh Hashanah 28b 25; Yevamot 90b 17; Shabbat 151b 17; Bava Metzia
59b 16; Eruvin 96a 14; Sukkah 34b 9; the twenty-two Mishnah rows); Tosefta Sanhedrin 11 (three rows, the English EMPTY strings), 12 (five), 14 (one — "a beguiled
city has never existed and never will"); Tosefta Zevachim 8 PAST THE END of the export (five chapters held), Tosefta Bava Kamma 9 EMPTY — their rows through the
Sifrei's citations (82:3, 96:4) read whole at the reading; the Sifrei on Numbers 103, 113, 114 one row each (the English's parallels); 566 addresses, 196 CREDITED BY
ADDRESS — chapter 4's docket 83 (Sanhedrin 88b 19 of 19 and Rosh Hashanah 28b 25 of 25: THE NOT-ADDING READ WHOLE AT 2b, its rows carried), chapter 7's 32 (the
devoted thing's Avodah Zarah rows), chapter 10's 17, the Exodus triage 14, chapter 8's 14, the ordinances docket 12, the Genesis triage 11, the sanctions docket
and the rest; the Mishnah rows credited: Sanhedrin 1:5, 4:1, 5:1, 11:1, 11:4-6, Makkot 1:6, Avodah Zarah 3:3, 3:4, 3:9 and more — some 370 rows to read whole: ONE
DOCKET RUN.

THE NAME: cold_run_seducers.py — the 68th runner (the seducers of chapter 13 — the prophet with the sign, the brother in secret, the city drawn away; the unit
deu_13_seducers); the daemon law_seducers, given_at Deut 13:1, installed_by boot (the Deuteronomy daemons' form; THE INSTALL HYPOTHESIS on the table unchanged); six
cells F1-F6 on the six claims' spans (13:1, 2-6, 7-12, 13-16, 17-18, 19) and the_readback — SEVEN WRAPPED (10b's lesson 4: the functions block counts what the daemon
wraps).

THE READBACK ON THIS CHAPTER — THE FORMS ON FILE, NO NEW FORM: chapter 13 is law from its first word to its last (Moses' voice, no act, no divine frame, no
"if" — the three cases on "when"), so its nineteen rows are T4 rows graded against the cells that compile their kin, by CALL (13:1 against 4:2; 13:3, 7, 14
against the second word; 13:4 against 6:16 and 8:2, 16; 13:5 against 6:13 and 10:20; 13:6 against 5:6 and 9:26; 13:9 against 7:16 and Leviticus 19:16, 19:18,
Exodus 23:5; 13:10-11 against Leviticus 24:14, 23 and Numbers 15:35-36; 13:16 against Exodus 22:19, Leviticus 27:28-29, Numbers 21:2-3 and 7:2; 13:18 against 7:26
and Numbers 25:4; 13:19 against 12:25, 28 and 6:18) and T1 reference rows against the tape's lines by kind and first verse (add_nothing_commanded Deut 4:1;
calf_made Exod 32:4 — "these are your gods" the seducers' formula in the run; tested Gen 22:1 — the testing's first seat; cloud_lifted Num 10:11 — 85:1's cloud;
cleaving_commanded Deut 10:20; stoned_as_commanded Lev 24:23 and Num 15:36 — the stoning rite performed; canaanites_devoted_hormah_named Num 21:3 — the ban
performed; hanging_commanded Num 25:4 — the fierce anger; nations_devoted Deut 7:1; abomination_barred Deut 7:25; nations_cut_off_warned Deut 12:29); NO
retrograde marker, NO act told only here, NO T2 row, NO state row; the run's cases OUTSIDE THE TAPE (Jericho's oath and Hiel — Joshua 6:26, 1 Kings 16:34; Achan
and Ai — Joshua 7:1, 7:26, 8:28; Makkedah — Joshua 10:28; Naboth's witnesses — 1 Kings 21:10; Jeroboam's altar — 1 Kings 13:3; Hananiah son of Azzur — Jeremiah 28;
Jehoshaphat — 1 Kings 22:43; Samuel's lamb — 1 Samuel 7:9; Saul and Amalek — 1 Samuel 15:3; Gideon's fleece — Judges 6:36-40; Gibeah — Judges 19:22) DATA rows; THE
CODE'S HOLES compiled at the chapter's own day (40, 11, 1), NO marker, after the tape's last Deut 12 line (nations_cut_off_warned): (a) THE HEADER'S SEAL (13:1 — A
REUSE), (b) THE PROPHET'S TEST AND THE FALSE PROPHET'S DEATH (13:2-6), (c) THE INCITER'S LAW (13:7-12), (d) THE CONDEMNED CITY'S LAW (13:13-19). THE DECISIONS (the
design's, open to the owner's word; the docket to confirm the names — 7b's lesson 7): (1) THE HEADER IS A SECOND ENTRY, NOT A NEW LAW — 13:1's "you shall not add
to it nor take from it" REUSES adding_barred (8b's and 10b's lesson: a reused effect is a second entry on the same ledger and moves an older count — the line
word_sealed writes adding_barred on israel_people a SECOND time, the value 'the singular seal on all the word — "all the word that I command you, it you shall keep
to do" (13:1; 4:2 the plural, the only two seats); the shelf at the word's grain (82:5 — not a word added to the priests' blessing), the count's (82:4 — the four
species, the fringes: both edges barred) and the rite's (82:3 — the mixed bloods, Mishnah Zevachim 8:10); R. Eliezer son of Jacob: "keep" the prohibition, "do" the
command (82:2, 85:3)'); CC3'S LITERAL "adding_barred … ONE" moves ONE -> TWO, retyped from the print BEFORE the tape (the grep at RUN B decides the list — 10b's
lesson 1: a boolean is not a count). (2) THE PROPHET'S TEST — prophet_test_declared writes THREE: false_prophet_hearing_barred, a BLOCK on israel_people (13:4 "you
shall not hearken to the words of that prophet or that dreamer of the dream" — the sign granted true and the hearing barred anyway, R. Yose the Galilean 84:1; a
fallen prophet's standing, R. Akiva 84:2 — THE SIGN'S STATUS A PARAMETER the_signs_status with the two arms; not one who retracts, not one suspected in hindsight
84:3-4; the sign not decisive at the oven of Akhnai — Bava Metzia 59b at the docket), tested_by_the_lord, a STATUS on israel_people (13:4 "for the LORD your God is
testing you, to know whether you love the LORD your God with all your heart and with all your soul" — the participle's one seat; Genesis 22:1's tested by kind, 8:2
and 8:16 by CALL; 84:5 the verse whole; test_barred (6:16 — Israel testing God) the mirror by CALL, a DATA row), and cleaving_commanded REUSED — a SECOND ENTRY on
israel_people (13:5's SIX VERBS: "after the LORD your God you shall walk, and Him you shall fear, and His commandments you shall keep, and His voice you shall obey,
and Him you shall serve, and to Him you shall cleave" — 10:20's four verbs the first entry, 6:13's three by CALL; 85:1 THE FIRST VERB IS THE CLOUD — a RUN CITATION of
cloud_lifted (Num 10:11) inside a law; 85:4 "His voice" the voice of His prophets — the true prophet's channel seated in the false prophet's chapter (18:15 ahead;
Yevamot 90b the temporary uprooting at the docket); 85:5 serve Him in His Torah and His sanctuary; 85:6 separate from idolatry and cleave; Sotah 14a's "walk after
His attributes" at the docket a DATA row beside 85:1's cloud); the literal counting cleaving_commanded ONE (8b's checkpoints — the grep decides) retyped from the
print if it counts. (3) THE FALSE PROPHET'S DEATH — at the CASE, not the statute: seducers_case's false prophet gets stoned (body, REUSED — the analogy of "thrusting"
with 13:11, 86:6, 90:2 — the Sifrei's majority) OR put_to_death (body, REUSED — "mode per the compiled law": STRANGLING, R. Shimon 86:6 and MISHNAH SANHEDRIN 11:1's
list of the strangled — THE ANSWER SHEET'S ARM), THE MODE A PARAMETER the_prophets_death with the two arms (the docket at Sanhedrin 89a-90a decides the value the
runner's DATA carries; 11:5-6 the prophet who prophesies what he did not hear, in another's name, in the name of idolatry); its reason the a fortiori from the
plotting witness (86:3 — Mishnah Makkot 1:4-6 by the docket); the exemptions of duress and error (86:1-2 — the exam's persons: exempt); and evil_purged_from_the_midst
— a NEW body effect, THE FORMULA'S FIRST SEAT (13:6 "and you shall purge the evil from your midst" — nine seats in the Bible, all in the book, 13:6 the first: 86:10
"purge the DOER of evils from Israel" — the person removed; written at the case on the condemned person; REUSED at 17:7, 17:12, 19:19, 21:21, 22:21, 22:22, 22:24,
24:7 ahead, each a second entry — the compile's gain from naming it at its first seat; the leaven's purge_deadline a homograph, a DATA row). (4) THE INCITER —
inciter_law_declared writes TWO: pity_barred REUSED — a SECOND ENTRY on israel_people (13:9 "you shall not consent to him nor hearken to him, nor shall your eye
pity him, nor shall you spare nor conceal him" — 7:16's "your eye shall not pity them" the first entry on the nations, the inciter the second object; THE FIVE
PROHIBITIONS EACH AGAINST A STANDING DUTY — the love of the neighbor (89:1 — Leviticus 19:18, holiness.conduct by CALL), the enemy's ass (89:2 — Exodus 23:5,
ordinances.courts('enemy_ox') by CALL), the neighbor's blood (89:3 — Leviticus 19:16, holiness.conduct('blood') by CALL), the defense barred and the silence barred
(89:4-5 — ordinances.courts by CALL: THE COURT'S RULE INVERTED, 89:6-7 — convicted not brought back to acquit, acquitted brought back to convict; Mishnah Sanhedrin
4:1 the ordinary rule by the docket; Sanhedrin 29a, 33b, 36b at the docket); "spare" the Torah's two — Saul's order at 1 Samuel 15:3 a DATA row), and
israel_hears_and_fears, a STATUS on israel_people, THE FORMULA'S FIRST SEAT (13:12 "and all Israel shall hear and fear, and shall not do again such an evil thing" —
the four seats 13:12, 17:13, 19:20, 21:21, the first with the paragogic nun; REUSED thrice ahead; THE EXECUTION'S TIMING A PARAMETER the_execution_timing — kept
until the festival, R. Akiva 91:1, against no delay in court, R. Judah 91:2; Mishnah Sanhedrin 11:4 and Sanhedrin 89a:6's four at the docket; Tosefta Sanhedrin
11 through the Sifrei's note); THE HAND FIRST (13:10 — the enticed's own commandment, any man's after, 89:8; 17:7's witnesses' hand the twin ahead; Leviticus
24:14's hands laid by CALL) and THE STONING'S RITE (13:11 — mekoshesh.capital_procedure('stones_and_a_stone', 'stoning', 'warning', 'venue') by CALL: 90:1's stones
and the stone ARE THE CELL; Leviticus 20:27's singular by CALL; law_mekoshesh's stoned/hanged/buried the run's own performance) the case's mode — stoned (body,
REUSED) on the inciter, evil_purged_from_the_midth's entry with it; THE INCITER'S KIN AN INCLUSION TABLE (87:4-11 — the brother by the father, the mother's son, the
son and the daughter of any kind, the betrothed and the married, the convert, THE FATHER in "as your own soul") the exam's persons; "entice" the Torah's one token
with two senses (87:1-2 — error, provocation) a DATA row; the concealed witnesses and the entrapment (Mishnah Sanhedrin 7:10, Sanhedrin 67a) the docket's rows;
THE FIFTEEN UTTERANCES (91:3) and the honors not capital (91:4 — Mishnah Sanhedrin 7:6, credited from the Exodus 22 sitting's docket if the carry finds it) DATA
rows; seclusion derived from "the son of your mother" (Kiddushin 80b, Sanhedrin 21b, Avodah Zarah 36b) a DATA row on the link rows' second use of the verse.
(5) THE CONDEMNED CITY — condemned_city_law_declared writes TWO: condemned_city_inquiry_required, a STATUS on israel_people (13:13-15 — "when you hear in one of your
cities … you shall inquire and search and ask diligently, and behold, if it is true, the thing certain": ONE CITY AT A TIME (92:3 — not three, two allowed; Mishnah
Sanhedrin 1:5 — the court of seventy-one, Sanhedrin 2a, 16b), JERUSALEM EXCLUDED by "to dwell there" (92:5 — chapter 12's place outside the ban; Bava Kamma 82b),
the border excluded (93:3 — Tosefta 14), THE SEDUCERS' PARAMETERS from one noun (93:1 — men, not women, not minors, two at least; 93:4 of their own city; 93:5 the
speech the warning — Mishnah Sanhedrin 10:4), THE THREE VERBS THREE SOURCES (92:2), THE SEVEN INQUIRIES AND THE PROBES — the_inquiries A PARAMETER (93:6-9; 149:1-2;
190:7-8 — Mishnah Sanhedrin 5:1-2; Sanhedrin 40a-41a: the two examinations' two rules, "I do not know" voiding the inquiries and not the probes, a contradiction
voiding both — THE CHAPTER TEACHES EVERY CAPITAL COURT ITS PROCEDURE: the parameter's value a table the cell reads as data), and devoted_thing_cleaving_barred, a
BLOCK on israel_people (13:18 "and nothing of the devoted thing shall cleave to your hand" — 7:26's house_abomination_barred the kin by CALL; the benefit from the
devoted at Mishnah Avodah Zarah 3:9 with 49b-50a (96:2 — the staff, the fork, the spindle, the rod; the Salt Sea), the twenty-six link rows on 13:18 (Avodah Zarah
12b, 34b, 42a, 43b, 44b, 48b; Makkot 22a; Pesachim 48a; Mishnah Shabbat 9:6 with Shabbat 90a; Tosefta Avodah Zarah 4:3, 7:5) the docket's rows; Makkot 22a:2's
lashes for the devoted thing's benefit the exam's lashes person if the docket reads it so); THE CASE — seducers_case's city gets city_devoted, a NEW destroy
effect written on the case's city (13:16-17 — "smite, you shall smite the inhabitants of that city with the edge of the sword, devoting it and all that is in it
and its cattle; gather all its spoil into its street and burn with fire the city and all its spoil wholly to the LORD; a heap forever, not built again": THE
PROPERTY TABLE (94:4-5, 95:1 — the righteous' inside lost, outside saved; the wicked's lost either way — Mishnah Sanhedrin 10:5; 112a-b at the docket) a decision
table in the cell, Heaven's spoil and the consecrated (94:6, 95:4-5 — Mishnah 10:6; 112b-113a; Temurah 8a) its exceptions, THE CHILDREN DISPUTED (94:3 — Abba
Hanan from 24:16) a PARAMETER's arm the docket weighs, "by any means" (94:1 — Bava Metzia 31b the doubling), the sword's manner (Sanhedrin 52b), the heap
forever by Joshua's oath (95:6-7, 96:1 — Jericho, Hiel; Sanhedrin 111b:13; not even gardens — R. Akiva) the value's tail; destroyed (body, Exod 22:19's) the kin
effect on the persons — the inhabitants' death by the sword the case's put_to_death (mode the sword) on the exam's persons, the docket to confirm; THE ANGER
KEYED TO IDOLATRY'S PRESENCE (96:3 — "as long as idolatry is in the world, fierce anger is in the world") the condition in devoted_thing_cleaving_barred's value,
Achan's valley (Joshua 7:26) and Peor's hanging_commanded (Num 25:4) by kind; THE MERCY TWO-ARMED (96:4 — Rabban Gamliel son of Rabbi: as you have mercy on
creatures, Heaven has mercy on you; Shabbat 151b, Yevamot 79a's three marks at the docket; Tosefta Bava Kamma 9 through the Sifrei) a DATA row — no write (a
promise's arm, not a law's); the oath the fathers' merit (96:5 — 7b's parameter by CALL, not_righteousness) and 13:18's "AS HE SWORE TO YOUR FATHERS" an AS_WHEN
pointer — RUN_CITATION of the oath (seven_nations.the_holy_people('the_oath'); the patriarchs' oath lines by kind) IF the census demands it (the census decides —
4b's to 10b's lesson). (6) THE FOOTER (13:19) — NO line, NO write: the footer is the condition of the chapter's laws ("when you hearken to the voice of the LORD your
God, to keep all His commandments … to do the right in the eyes of the LORD your God"), folded into condemned_city_law_declared's value; 28:1's blessing (fourteen
tokens in order) and 28:15's curse ahead; "the right in the eyes of the LORD" place_name (12:25, 28) and hear_o_israel (6:18) by CALL; 96:6-8 (a little to much; the
light as the weighty — 82:1's sentence at both ends; the right Heaven's — R. Ishmael) DATA rows; Avot 2:1, 3:9, 3:14 the docket's rows. (7) THE DREAM AND THE SIGN —
"a dreamer of a dream" (13:2) the dream's noun and verb in the book only at 13:2, 4, 6: beha.miriam('dreams', 'dibbur') by CALL (Numbers 12:6-8 — the dream the
prophets' channel, Moses' mouth to mouth: 83:2), the Genesis dream lines (dreamed, dream_told, came_in_a_dream) by kind DATA rows; THE PROPHET'S FORMS ARE MOSES'
(83:1 — thus said; part delivered, part fulfilled; the general and the particular) a DATA row; "a sign or a wonder" (13:2) — the sign in the heavens and the wonder
on the earth (83:4-5 — Genesis 1:14's lights, Gideon's fleece) DATA rows; 1 Kings 13:3's sign at Jeroboam's altar (the one two-token kin) a DATA row; the four
signs 84:1's dominion over the sun and the moon (R. Yose the Galilean) inside the parameter's arm. (8) THE EXODUS FORMULA WITH REDEEMING (13:6, 13:11) — 5:6's
preamble by CALL (covenant_at_horeb), 9:26's redeeming by CALL (not_righteousness), 7:8's by CALL (seven_nations.the_holy_people('brought_out_redeemed')); "even
had He no claim on you but that He brought you out of Egypt, enough" (86:4-5, 90:3) DATA rows; "for he spoke rebellion against the LORD" the noun's two Torah seats
(13:6, 19:16 — 189:1 reading each by the other, Hananiah's sentence Jeremiah 28:16) a DATA row for 19:16's sitting. (9) THE TWO VERBS OF STONING (Deuteronomy's
at 13:11, 17:5, 22:21, 24 against Leviticus's and Numbers' at Molech's giver, the necromancer, the blasphemer, the wood-gatherer; 21:21 both) — a DATA row on
the DB's lemmas (the reading's ink by CALL from the ink block); THE HAND FIRST 17:7's twin ahead (a look at chapter 17's compile); "afterward" the Torah's two
seats both this clause a DATA row. (10) THE TESTING SHELF'S HOMOGRAPHS — purge_commanded (Jacob's), purge_deadline (the leaven's), the-heap (Laban's), the-friend
(Ahuzzath), the-cities (Shechem's), the family runner's brother/son/daughter/wife (10b's precedent — the family runner matched on homographs of sense at 12:9
and 12:12): each filed FALSE with its why IF the census matches (the census decides). (11) THE REGISTER — NO seat in chapter 13 (the reading's finder: no receipt,
no header, no footer); DECLARED 100 unmoved; 13:1's header is 4:2's law restated, not a register header (the register's headers are the formulas — "these are the
statutes", "these are the words"); the gate --strict GREEN expected. (12) THE INSTRUMENT'S SLIPS AS DATA — the tagger's "Np" substring inside "VNp" and the bare
number check inside "swore" (the reading's lesson 3) DATA rows; the parser's [1] at 13:13 (12:14's and 17:2's the kin) a DATA row; THE KETIV AT 13:16 in the store
(329 against 328) a DATA row; the register's DATA rows (no imperative, no "if", the seducers' "we", the four infinitive absolutes, the one wayyiqtol, no divine
frame, Israel once, Moses never).

THE ROWS (nineteen predicted, one per verse; the grades' census typed from the runner's print at RUN B): 13:1 "all the word that I command you, it you shall keep to
do; you shall not add to it nor take from it" — add_nothing_commanded (4:1) by kind, obey_horeb.the_exhortation('add_nothing', 'diminish_nothing') by CALL: VERBATIM
in kind (4:2 the plural, 13:1 the singular — the only two seats; THE LINE word_sealed's REUSE adding_barred the second entry); 13:2 "when a prophet arises among you,
or a dreamer of a dream, and gives you a sign or a wonder" — THE LINE prophet_test_declared; beha.miriam('dreams') by CALL, mamre.moriah by CALL: SUPPLIED AS A LAW
(the first seat — 18:15's "from among you" the true prophet ahead; the dream's three book seats; the sign in the heavens, the wonder on the earth 83:4-5); 13:3
"and the sign and the wonder come to pass … saying, let us go after other gods which you have not known, and let us serve them" — calf_made (Exod 32:4) by kind,
covenant_at_horeb.the_second_word by CALL, blessing_and_curse (11:28's "other gods which you have not known") by CALL: VARIANT (THE SEDUCER'S ONE FORMULA — 13:3, 7,
14 each other's closest kin; "let us go" the cohortative nine in the Torah; 84:1-2's dispute the parameter's arms; 1 Kings 13:3 the sign's one two-token kin a
DATA row); 13:4 "you shall not hearken to the words of that prophet … for the LORD your God is testing you, to know whether you love the LORD your God with all
your heart and with all your soul" — THE WRITES false_prophet_hearing_barred and tested_by_the_lord; tested (Gen 22:1) by kind, good_land (8:2, 16) and
hear_o_israel (6:16 test_barred — the mirror) by CALL, blessing_and_curse (11:13's plural heart and soul) by CALL: SUPPLIED AS A LAW (the participle's one seat;
"whether you are" one; 11:13 the closest kin nine tokens in order); 13:5 "after the LORD your God you shall walk, and Him you shall fear, and His commandments you
shall keep, and His voice you shall obey, and Him you shall serve, and to Him you shall cleave" — cleaving_commanded (10:20) by kind and REUSED, hear_o_israel
(6:13) and second_tablets by CALL, cloud_lifted (Num 10:11) by kind for 85:1's cloud: EXPANDED (the four verbs six; each clause one seat; 85:1-6 the six readings —
the cloud, His fear upon you, the prohibition, the prophets' voice, His Torah and His sanctuary, separate and cleave; Joshua 22:5's three tokens; Sotah 14a's
attributes at the docket); 13:6 "and that prophet or that dreamer of the dream shall be put to death, for he spoke rebellion against the LORD your God who brought
you out of the land of Egypt and redeemed you from the house of bondage, to thrust you from the way … and you shall purge the evil from your midst" — THE CASE'S
WRITES (stoned / put_to_death by the parameter, evil_purged_from_the_midst — THE FORMULA'S FIRST SEAT), covenant_at_horeb (5:6) and not_righteousness (9:26) by
CALL, sanctions.census('stoned', 'strangled') by CALL: SUPPLIED AS A LAW (the noun "rebellion" two Torah seats; the participle "who redeemed you" one; "thrust"
ten in the book; 86:1-10's readings — not coerced, not misled, the a fortiori, the two claims, the analogy, the two halves, the part and the whole, the doer
removed); 13:7 "when your brother, the son of your mother, or your son or your daughter or the wife of your bosom or your friend who is as your own soul entices
you in secret, saying, let us go and serve other gods which you have not known, you nor your fathers" — THE LINE inciter_law_declared; covenant_at_horeb by CALL:
SUPPLIED AS A LAW (the first seat; "entice" the Torah's one token, two senses 87:1-2; THE INCLUSION TABLE 87:4-11 the exam's persons; "the wife of your bosom",
"as your own soul" one seat each; 87:3's fathers and sons — 24:16 ahead; 87:12 in secret; 87:13 Israel's disgrace); 13:8 "of the gods of the peoples round about
you, near to you or far from you, from one end of the earth to the other" — hear_o_israel (6:14's clause plene) by CALL: VERBATIM in kind (6:14's clause spelled
defective here — a DATA row; 88:1-2 THE HEADLESS PISKA — the near teach the far, the far the sun and the moon; 28:64's exile ahead); 13:9 "you shall not consent to
him nor hearken to him, nor shall your eye pity him, nor shall you spare nor conceal him" — THE WRITE pity_barred REUSED (7:16's first entry on the nations),
seven_nations.hearing_blessed by CALL, holiness.conduct and ordinances.courts by CALL for the standing duties: EXPANDED (five negations in one verse; 89:1-5 each
against a duty; 89:4-5 the defense and the silence; "spare" the Torah's two and Saul's third); 13:10 "but kill, you shall kill him; your hand shall be on him first
to put him to death, and the hand of all the people afterward" — lev24 (24:14's hands laid) by CALL, mekoshesh.capital_procedure by CALL: VARIANT (89:6-7 THE
COURT'S RULE INVERTED — the doubled verb's two halves; 89:8 the enticed's own commandment; 17:7's twin ahead; "afterward" the Torah's two); 13:11 "and you shall
stone him with stones that he die, for he sought to thrust you from the LORD your God who brought you out of the land of Egypt, out of the house of bondage" —
stoned_as_commanded (Lev 24:23, Num 15:36) by kind, mekoshesh.capital_procedure('stones_and_a_stone', 'stoning') and sanctions.molech('who_stones') by CALL,
covenant_at_horeb (5:6) by CALL: VARIANT (90:1 THE STONES AND THE STONE — the wood-gatherer's cell holds it; 90:2 the analogy run back; 90:3 the exodus enough; the
two verbs of stoning a DATA row; 5:6's six tokens in order); 13:12 "and all Israel shall hear and fear, and shall not do again such an evil thing as this in your
midst" — THE WRITE israel_hears_and_fears — THE FORMULA'S FIRST SEAT: SUPPLIED AS A LAW (the four seats ahead; the paragogic nun; 91:1-2 the timing's two arms; 91:3
the fifteen utterances; 91:4 the honors not capital — Mishnah Sanhedrin 7:6; Israel's one token; the root of adding at "do again" a DATA row); 13:13 "when you hear
in one of your cities which the LORD your God gives you to dwell there, saying" — THE LINE condemned_city_law_declared; place_name (12:14's [1]) by CALL: SUPPLIED
AS A LAW (the first seat; THE NUMBER VERSE [1] — 92:3's one city; "to dwell there" the Torah's one — 92:5 Jerusalem; 92:1 the report received; 92:4 in any place);
13:14 "men, sons of Belial, have gone out from your midst and have drawn away the inhabitants of their city, saying, let us go and serve other gods which you have
not known" — covenant_at_horeb by CALL: VARIANT (THE ONE NARRATIVE VERB; "sons of Belial" the Torah's two — 117:3's analogy with 15:9, Naboth's witnesses the
closest verse; 93:1-5 the seducers' parameters; 93:2 without a yoke; 93:3 the border; the same letters read two ways at 13:3 and 13:14 a DATA row); 13:15 "then
you shall inquire and search and ask diligently; and behold, if it is true, the thing certain, that this abomination was done in your midst" — THE WRITE
condemned_city_inquiry_required with THE PARAMETER the_inquiries: SUPPLIED AS A LAW (17:4 the twin — nine of twelve tokens in order, ahead; 93:6-9 THE SEVEN
INQUIRIES AND THE PROBES — 149:1-2, 190:7-8 the analogy at three seats; 93:10 converts and freed slaves; "diligently" five in the book); 13:16 "smite, you shall
smite the inhabitants of that city with the edge of the sword, devoting it and all that is in it and its cattle with the edge of the sword" — canaanites_devoted_hormah_named
(Num 21:3) by kind, ordinances.capital('devoted_seats' — Exod 22:19), temurah.devote (Lev 27:28-29), chukat.arad_and_the_serpent('cherem_law') and
seven_nations.the_seven_nations('the_ban') by CALL: EXPANDED (THE CASE'S city_devoted; 94:1 by any means; 94:2 THE KETIV read; 94:3 the children disputed; 94:4-6
the property table's first cells; "with the edge of the sword" the Torah's five; Joshua 10:28 Makkedah the closest verse a DATA row); 13:17 "and all its spoil you
shall gather into the midst of its street, and burn with fire the city and all its spoil wholly to the LORD your God; and it shall be a heap forever, it shall not
be built again" — the case's city_devoted's value: VARIANT (95:1 the table's fourth cell; 95:2-3 the street; 95:4-5 Heaven's spoil, the consecrated — Mishnah
Sanhedrin 10:6; 95:6-7 JERICHO the run's case, Hiel wilful; 96:1 not even gardens; "wholly" Samuel's lamb, "a heap forever" Ai's, "not built again" Tyre's DATA
rows; "its street" the Torah's one); 13:18 "and nothing of the devoted thing shall cleave to your hand, that the LORD may turn from the fierceness of His anger and
give you mercy, and have mercy on you and multiply you, as He swore to your fathers" — THE WRITE devoted_thing_cleaving_barred; seven_nations.the_images_and_the_devoted
(7:26) by CALL, hanging_commanded (Num 25:4) by kind for the anger, THE POINTER (decision 5): SUPPLIED AS A LAW (96:2 the benefit to the Salt Sea — Mishnah Avodah
Zarah 3:9; 96:3 the anger keyed to idolatry; 96:4 the mercy two-armed a DATA row; 96:5 the fathers' merit by CALL; Achan's valley saying the words back, Jacob's
"give you mercy" DATA rows); 13:19 "when you hearken to the voice of the LORD your God, to keep all His commandments which I command you today, to do the right
in the eyes of the LORD your God" — place_name (12:25, 28) and hear_o_israel (6:18) by CALL: VERBATIM in kind (NO line — the footer the laws' condition; 28:1 and
28:15 ahead; Jehoshaphat's measure a DATA row; 96:6-8 the header's sentence at the footer). THE HOLES: FOUR IN THE CODE compiled at the chapter's own day (the
header's seal a reuse; the prophet's test; the inciter's law; the condemned city's law); NONE told only here; the pointer at 13:18 if demanded; no state row, no
retrograde marker.

THE CELLS (F1-F6 + the_readback; every token probed; effects on every cell; the exam's rows the docket's crowns): F1 THE HEADER (13:1): the reuse's second entry;
4:2 by CALL; the exam: the four species and the fringes (Mishnah Sukkah 3:4 with Sukkah 34b; Menachot 41b-42a — 82:4), the priests' blessing (Rosh Hashanah 28b,
Eruvin 96a — 82:5; credited whole from chapter 4's docket, carried), the mixed bloods (Mishnah Zevachim 8:10 with Zevachim 80a-81b — 82:3; Tosefta Zevachim 8 past
the export's end, through the Sifrei), the rebellious elder's not-adding (Sanhedrin 88b — credited whole from chapter 4's docket, carried), R. Eliezer son of
Jacob's rule (82:2) a DATA row. F2 THE PROPHET AND THE TEST (13:2-6): the line and its three writes (two new, one reused); the two parameters (the sign's status,
the prophet's death); the exam: Mishnah Sanhedrin 11:1 (the strangled — credited, carried), 11:5-6 with Sanhedrin 89a-90a (the false prophet's three; the one who
suppresses; the sign — 30 of 64 credited), Bava Metzia 59b (the oven of Akhnai — the sign not decisive), Yevamot 90b (Elijah on Carmel — the temporary uprooting;
85:4), Horayot 13a and Tosefta Horayot 2:8 (the prophet's precedence — 13:2's "prophet" the link rows' use), Sotah 14a and 39b (13:5's "after the LORD you shall
walk"), Mishnah Makkot 1:4-6 (86:3's a fortiori — 1:6 credited), Chullin 139a-140a (13:6's "shall be put to death" read on a bird — a DATA row), Sanhedrin 78a and
84a (13:6's death clause in other derivations — DATA rows), the Rambam's Introduction 5:2-3 (the prophet not examined — DATA rows), Sifrei Numbers 103 (Miriam's
dream — 83:2's channel). F3 THE INCITER (13:7-12): the line and its two writes (one reused, one new — the formula's first seat); the timing parameter; the exam:
Mishnah Sanhedrin 7:10 with Sanhedrin 67a (the concealed witnesses, the entrapment — 4 of 23 credited), 61b (the inciter's speech — Rav Yosef, Abaye, Rava on 13:7-9),
63b (the inciter's prohibition), 29a, 33b, 36b (the court's rule inverted — 89:4-7), 43a (Ulla's proof from 13:9 — a DATA row on the link row), 54b (the stoning
derived from "shall be put to death" — 13:10-11), 85b, Makkot 12a (13:9 in the avenger's derivation — a DATA row), Kiddushin 80b, Sanhedrin 21b, Avodah Zarah 36b
(seclusion from "the son of your mother" — a DATA row), Sanhedrin 89a:6 (the four executed at the festival — 91:1-2; Mishnah 11:4 credited), Mishnah Sanhedrin
7:6 (the honors — 91:4; credited from the Exodus docket if carried), Sanhedrin 16b:13-14 and Mishnah 1:5 (one city, not three — 92:3, F4's too), Sifrei Numbers 113,
114 (the wood-gatherer's stoning — the rite's kin). F4 THE CITY HEARD OF, THE INQUIRY AND THE SWORD (13:13-16): the line and its first write with THE PARAMETER
the_inquiries; the case's city_devoted; the exam: Mishnah Sanhedrin 10:4-6 with Sanhedrin 111b-113b (the condemned city — 6 of 71 credited: the residents' share,
the smiting, the devoting, the spoil, the heap, the consecrated, the scrolls, "nothing shall cleave"), Sanhedrin 2a and 16b (the court of seventy-one; three
cities), 71a (a city with one mezuzah), Bava Kamma 82b (Jerusalem cannot become one — 92:5), Mishnah Sanhedrin 5:1-2 with Sanhedrin 40a-41a (the inquiries and the
probes — 93:6-9; 5 of 64 credited), Sanhedrin 3a (one manner of law — 13:15 in the link rows), Bava Metzia 31b (94:1's doubling), Sanhedrin 52b (the sword's
manner), 45b, Temurah 8a (the city's consecrated animals — Tosefta Sanhedrin 4:5 by the link row), Yevamot 122b (13:15's "true and certain" in a witness rule — a
DATA row), Tosefta Sanhedrin 14:1 (never was, never will be — "examine and take a reward": THE LAW AS A STUDY TEXT, a DATA row), Bava Batra 10a, Ketubot 68a,
Berakhot 31b, Tosefta Peah 4:19 (Belial — the one who turns his eyes from charity; the drunken Hannah: DATA rows on 13:14's word), Tosefta Sanhedrin 12 (five rows —
the honors), 11 (three rows, the English empty — through the Sifrei's note). F5 THE WHOLE OFFERING, THE HEAP AND THE MERCY (13:17-18): the line's second write;
the pointer; the exam: Sanhedrin 111b:13 (a heap forever), 112a:7-18 (the smiting, the spoil, the hair of pious women), 112b-113a (the consecrated, the scrolls),
113b:2 ("nothing shall cleave"), Chullin 89a:11-12 (the ashes of the burned city and the covering — a DATA row), Mishnah Avodah Zarah 3:9 with Avodah Zarah
49b-50a (96:2 — the Salt Sea; 3:9 credited), 3:3-4 (credited from chapter 7's docket), Avodah Zarah 12b, 34b, 42a, 43b, 44b, 48b (the benefit from the devoted —
"nothing shall cleave": the link rows' seat), Makkot 22a:2, 22a:9 (the lashes' list — Rabbi Hiyya's baraita; Rav Ashi's plow), Pesachim 48a, Mishnah Shabbat 9:6
with Shabbat 90a (the idol's measure for carrying — a DATA row), Tosefta Avodah Zarah 4:3, 7:5, Beitzah 32b (the wealthy without mercy — 96:4's kin), Yevamot 79a
(the three marks — the merciful, 96:4), Shabbat 151b (the mercy two-armed — 96:4; Tosefta Bava Kamma 9 empty in the export), Tosefta Sotah 10:1 (the righteous and
mercy), Sanhedrin 45b. F6 THE FOOTER (13:19): no line; the rows by CALL; the exam: Avot 2:1 (the light as the weighty — 82:1, 96:7; credited from 10b's docket if
carried), 3:9 and 3:14 (the docket's rows), Chagigah 8b, Eruvin 100a, Menachot 40b (the not-adding's other seats on the link rows — F1's too). THE READBACK TABLE
(the_readback — the nineteen rows with their grades, the pointer, the DATA rows). THE DATA ROWS (about thirty): the readback table; the header's twin 4:2; the
seducers' one formula; the dream's three seats; the sign in the heavens and the wonder on the earth; 1 Kings 13:3's sign; the participle "is testing"; test_barred
the mirror; the six verbs against the four; the cloud's line; Sotah 14a's attributes; the noun "rebellion" two seats; the exodus formula with redeeming; "entice"
two senses; the inclusion table; 6:14 plene and 13:8 defective; the five prohibitions' duties; Saul's "spare"; the court's rule inverted; the hand first and 17:7;
"afterward" two seats; the two verbs of stoning; the stones and the stone; the formula's four seats; the timing's two arms; the fifteen utterances; the honors; the
parser's [1]; "to dwell there" one seat; Belial's Torah two and Naboth; the one narrative verb; the same letters two ways; the seven inquiries' three seats; the four
infinitive absolutes; THE KETIV in the store; the property table; the children; Jericho, Hiel, Ai, Tyre, Makkedah; "wholly" and Samuel's lamb; the Salt Sea; the
anger keyed to idolatry; Achan's valley; the mercy two-armed; Jacob's "give you mercy"; the fathers' merit; the AS_WHEN oath; the footer and 28:1, 28:15;
Jehoshaphat's measure; the header's sentence at the footer; the register's rows; the instrument's two slips; the homographs (purge_commanded, purge_deadline,
the_heap, ahuzzath, the_cities_around_shechem); Tosefta Sanhedrin 14:1's "never was" — the law as a study text.

THE LINES ON THE TAPE (the recorder and the stitcher; the design's arithmetic): NO MARKER; FOUR OWN-DAY LINES after the tape's last Deuteronomy 12 line
(nations_cut_off_warned) — word_sealed (13:1), prophet_test_declared (13:2-6), inciter_law_declared (13:7-12), condemned_city_law_declared (13:13-19), all STATUTE by
form (the form declared — 4b's lesson); THE DAEMON'S NINE WRITES AT THE STATUTES — adding_barred (REUSED — a second entry on israel_people), false_prophet_hearing_barred
(a BLOCK), tested_by_the_lord (a STATUS), cleaving_commanded (REUSED — a second entry), pity_barred (REUSED — a second entry), israel_hears_and_fears (a STATUS),
condemned_city_inquiry_required (a STATUS), devoted_thing_cleaving_barred (a BLOCK) — EIGHT writes (three reuses, five new); the case's writes at the exam only
(stoned, put_to_death, evil_purged_from_the_midst, city_devoted, accepted, exempt, lashes). THE TYPES (add_types_ch13.py, after the probes' FAIL print):
event_vocabulary +5 (the four lines — form statute, witnesses Deut 13:1, 13:2, 13:7, 13:13; seducers_case — the exam's case kind) 1150 -> 1155; effect_vocabulary
+7 (false_prophet_hearing_barred, devoted_thing_cleaving_barred — block; tested_by_the_lord, israel_hears_and_fears, condemned_city_inquiry_required — status;
evil_purged_from_the_midst — body; city_devoted — destroy; the names the docket confirms) 1049 -> 1056, adding_barred's, cleaving_commanded's and pity_barred's rows
AMENDED with the chapter's seats (adding_barred's 'ink' already names 13:1); daemon_dispositions (law_seducers — file, wraps seducers, given_at Deut 13:1,
installed_by boot, watches {word_sealed: [adding_barred], prophet_test_declared: [false_prophet_hearing_barred, tested_by_the_lord, cleaving_commanded],
inciter_law_declared: [pity_barred, israel_hears_and_fears], condemned_city_law_declared: [condemned_city_inquiry_required, devoted_thing_cleaving_barred],
seducers_case: [accepted, exempt, stoned, put_to_death, evil_purged_from_the_midst, city_devoted, lashes]}; the functions block's SEVEN WRAPPED — the six cells and
the_readback); dependency_dispositions (the span [[Deut, 13, 1, 19]]; the CALL edges predicted NINETEEN — obey_horeb, covenant_at_horeb, hear_o_israel,
seven_nations, good_land, not_righteousness, second_tablets, blessing_and_curse, place_name, ordinances, erection, sanctions, lev24, mekoshesh, temurah, chukat,
balak, beha, mamre (shelach and holiness if the census asks) — the census decides; ONE AS_WHEN pointer predicted at Deut 13:18 — RUN_CITATION of the oath — the
census decides; FALSE edges on the homographs if matched); installation_probes I5 72 -> 73; calendar_parameters.yaml +4 (the_signs_status, the_prophets_death,
the_execution_timing, the_inquiries — the sojourn_start form, the docket's values); the register file untouched (DECLARED 100).

THE PREDICTION'S ARITHMETIC: RUN = (1327, 96, 88, 0, 12, 1634, 44, 319, the four pairs, 127) — events +4, timers set +0, fired +0 (no clock walk), cancels 0,
retro-writes 12 UNMOVED, writes +8 (the daemon's eight at the statutes), daemons fired +1 (law_seducers), entities +0 (israel_people on the registry; no person or
city an entity), closes +0 (no debit, no close); PREVIOUS_RUN = 10b's RUN EXACTLY (1323, 96, 88, 0, 12, 1626, 43, 319, the four pairs, 127): THE REST drops the four
lines by the runner's tag and the span and the daemon's eight writes with them — no delta; NEWEST_RUNNER 'seducers'; markers 172 UNMOVED (PLACEMENT markers
text_constrained 108, reading_placed 49 unmoved); events page_order 1155 -> 1159, text_constrained 110 and reading_placed 58 UNMOVED — READ, never predicted; CENSUS
on tape 1323 -> 1327, kinds 868 -> 872, subjects 272 UNMOVED, markers 172, closes 71 unmoved; the population table 148 UNMOVED; THE OPEN DEBITS ON israel_people 10
UNMOVED (no debit this chapter); THE BLOCKS on israel_people +4 in count (adding_barred and pity_barred the second entries, two new — the literals counting the
blocks grepped); adding_barred ONE -> TWO on israel_people (CC3's count literal retyped from the print BEFORE the tape — 8b's and 10b's lesson), cleaving_commanded
ONE -> TWO (the 8b checkpoint's literal, if it counts — the grep decides), pity_barred ONE -> TWO (the 5b checkpoint's literal, if it counts); the scene's tuple
PREDICTED BY SCRIPT at the runner step (the exam's persons through seducers_case — each written once; no timer; no close); the narrative's (its own world: the eight
writes, 0 closes, the entity israel, the counter's day (11, 1), no row).

THE CHECKPOINTS DE1-DE9 (the D series at its fifth name; the literals typed from the prints at RUN B):
DE1 THE LINES — four events on the tape AFTER the tape's last Deuteronomy 12 line: word_sealed, prophet_test_declared, inciter_law_declared and
condemned_city_law_declared on the counter's day (40, 11, 1), NO marker (markers 172 UNMOVED); the counter ends at (40, 11, 1).
DE2 THE WRITES — false_prophet_hearing_barred ONE, tested_by_the_lord ONE, israel_hears_and_fears ONE, condemned_city_inquiry_required ONE,
devoted_thing_cleaving_barred ONE on israel_people; adding_barred TWO (4:1's and 13:1's), cleaving_commanded TWO (10:20's and 13:5's), pity_barred TWO (7:16's and
13:9's) on israel_people; law_seducers registered, given_at Deut 13:1, installed_by boot; the seven cells WRAPPED.
DE3 THE READBACK — the_readback's rows (nineteen; the census from the print), every reference row's entry FOUND: the tape lines by kind and first verse
(add_nothing_commanded Deut 4:1, calf_made Exod 32:4, tested Gen 22:1, cloud_lifted Num 10:11, cleaving_commanded Deut 10:20, stoned_as_commanded Lev 24:23 and
Num 15:36, canaanites_devoted_hormah_named Num 21:3, hanging_commanded Num 25:4, nations_devoted Deut 7:1, abomination_barred Deut 7:25, nations_cut_off_warned Deut
12:29) and the kin's cells by CALL (each returning its verdict on its own ask); the pointer; no retrograde row, no state row.
DE4 THE HOLES — NO effect naming the false prophet's hearing, the LORD's testing, Israel's hearing and fearing, the condemned city's inquiry or the devoted thing's
cleaving on israel_people BEFORE this daemon's lines (the ledger scan on the running world at the tape's Deut 12 end: EMPTY — asserted before the lines run) and
ONE each after; adding_barred, cleaving_commanded and pity_barred ONE each before and TWO after; the seven new names absent from both registries at sitting 11's
tree (asserted on the registry files).
DE5 THE KIN STAND — 4:2's cell returning its own verdict on 'add_nothing' and 'diminish_nothing' by CALL (obey_horeb.the_exhortation), the second word's
other_gods_barred ONE UNMOVED, test_barred ONE UNMOVED, house_abomination_barred ONE UNMOVED, the ban's debit OPEN (nations_devoted's 'commanded' UNMOVED), cherem_vowed
CLOSED (Num 21:3) UNMOVED, destroyed's count UNMOVED (the king of Arad's), stoned's count UNMOVED (the blasphemer's, the wood-gatherer's), the wood-gatherer's cell
returning the stones and the stone by CALL (mekoshesh.capital_procedure('stones_and_a_stone')), the four deaths' census by CALL (sanctions.census); the open
debits on israel_people 10 UNMOVED.
DE6 THE FORMULA'S FIRST SEATS — evil_purged_from_the_midst absent from every ledger BEFORE the exam's case and written on the case's persons after (the runner's
scene); israel_hears_and_fears ONE on israel_people, its value naming 13:12 as the first of four; adding_barred's second entry's source beginning "Deut 13:1".
DE7 THE PARAMETERS AND THE POINTER — the_signs_status, the_prophets_death, the_execution_timing and the_inquiries on file (calendar_parameters.yaml, the
sojourn_start form), no clock use; the pointer at 13:18 in the dispositions IF the census demanded it (the file read at the gates); the homographs filed FALSE if
matched; NO register seat at Deut 13 (the finder called on the chapter at the tape — the reading's measurement repeated).
DE8 THE DATA — the two verbs of stoning on the DB (Deuteronomy's four seats, Leviticus's and Numbers' eight, 21:21 both); the purge formula's nine seats on the DB
(all in the book, 13:6 the first); "all Israel shall hear and fear" four seats (13:12 the first); the header's two seats (4:2, 13:1); the seducers' formula at 13:3,
7, 14; the ketiv at 13:16 (the store's 329 against the DB's 328); the parser's [1] at 13:13; 6:14 plene against 13:8 defective — every one by CALL to the ink block.
DE9 THE REST — entities 319 UNMOVED, closes 127, markers 172, the population table 148 UNMOVED, the four kinds present; the other counts 10b's exactly with the
four lines and the eight writes dropped (THE REST test — NO declared delta). THE STALE LITERALS predicted (grepped at the design): CC3 in cold_run_sequence.py
("adding_barred on israel_people ONE" — a count on a list, line 3094-3097: MOVES); the 8b checkpoint on cleaving_commanded and the 5b checkpoint on pity_barred
(the grep at RUN B decides — 10b's lesson 1); the checkpoints counting the blocks on israel_people (if any); every miss shown at once by checkpoint_check.py --all
AFTER the tape.

THE PROBES (RUN B's FIRST step, before the types — 7b's lesson 2): readback_probes.py Q34-Q36 written to FAIL before the runner exists — Q34 the runner and its
the_readback table (the rows and their census typed from the print; every reference row's entry found; the pointer; no retrograde row, no state row); Q35 the four
own-day lines on the counter's day (40, 11, 1) with NO marker (markers 172 UNMOVED) and their eight writes (five new on israel_people; adding_barred,
cleaving_commanded and pity_barred TWO each — the reuses); Q36 the kin standing (DE5's counts) and the holes filled (DE4, DE6); the probes holding adding_barred,
cleaving_commanded or pity_barred ONE retyped from the print; Q22-Q33 unchanged (no marker count moves); THE PARSER — 13:13's "in one of your cities" [1] measured at
the reading: a census probe row IF the form asks (the probes' own count read at RUN B; census_probes 224 at 10b); the register gate --strict (no seat; DECLARED 100
unmoved); checkpoint_probes' verse computed (2b's form).

THE ORDER: this design -> the state doc's checkpoint (#203 — RUN A closed) -> THE DOCKET IN ONE RUN: the dump (ch13_docket_dump.txt, 1,700 lines — 91 LINK rows in
31 works and 463 TOPIC rows: the fourteen folio ranges (Sanhedrin 67a 23, 88b 19, 89a-90a 64, 40a-41a 64, 111b-113b 71; Zevachim 80a-81b 54; Sukkah 34b 9;
Menachot 41b-42a 40; Rosh Hashanah 28b 25; Eruvin 96a 14; Avodah Zarah 49b-50a 33; Bava Metzia 59b 16; Yevamot 90b 17; Shabbat 151b 17) and the twenty-two Mishnah
rows (Sanhedrin 1:5, 4:1, 5:1-2, 7:6, 7:10, 10:4-6, 11:1, 11:4-6; Makkot 1:4-6; Zevachim 8:10; Sukkah 3:4; Avodah Zarah 3:9; Avot 2:1, 3:9, 3:14); Tosefta Sanhedrin
11, 12, 14 and the Sifrei on Numbers 103, 113, 114 (twelve rows); Tosefta Zevachim 8 past the export's end and Tosefta Bava Kamma 9 EMPTY — their rows through the
Sifrei's citations read whole at the reading (82:3, 96:4)), 196 CREDITED BY ADDRESS at the scan — chapter 4's docket 83 (Sanhedrin 88b and Rosh Hashanah 28b
whole), chapter 7's 32, chapter 10's 17, the Exodus triage 14, chapter 8's 14, the ordinances docket 12, the Genesis triage 11 and the rest — every credited row
CARRIED with its ledger's own verdict line (10b's form) and listed with its ledger; the some 370 UNCREDITED rows READ WHOLE in chunk files (the cap 64,000 bytes —
one chunk one Read page), the parts on 10b's whole-row instruments (ch12_docket_A.py's form, ch12_docket_common.py, ch12_credit_carry.py derived), EVERY ROW WHOLE,
the verdicts LAW / DERIVATION / DISPUTE / CONTEXT / OUTSIDE with the credits computed, the writer derived from write_ch12_docket.py, the docket's records
(COMPILE_DEBT's box (l), MIDDOT — every code checked in MIDDOT.md before it is typed, MISHNAH_TOPICS, the state doc's checkpoint) -> RUN B: the probes to FAIL
(patch_probes_ch13.py: Q34-Q36; the reuse literals retyped ONE -> TWO), the types (add_types_ch13.py — the docket's names; the four parameters), the callees' facts
printed before any assert (ch13_callees.py — every CALL named above, each ask read at the cell's own source), the runner in parts with the fast checker
(ch13_fastcheck.py) and the generated CASES (ch13_cases_gen.py; the guard's count from the generator's print), the recorder (seq_record_ch13.py, INK_CACHE=0) and
the stitcher (seq_stitch_ch13.py; no marker — the four lines on the counter's day), the literals DE1-DE9 and the VERDICTS entries (patch_seq_literals_ch13.py), the
tape to 10/10 with THE REST, checkpoint_check.py --all AFTER the tape, the records writer (write_ch13b_records.py) and the copier WRITTEN, gates_chain.sh LAUNCHED
in the background, the clean point -> THE TAIL: the summary read once, the demands filed (a rerun --from the step), the records from the sheet in one call (the
map's AS BUILT, COMPILE_DEBT's sitting-11 box PAID and the 11b box, MIDDOT, MISHNAH_TOPICS, RESEARCH_LOG, THE_STEPS, THE_BRIEFING, THE_LOOP's step-6 row, RESUME,
RECORD_FORMS, the state doc, the addenda, the recovery page, the memory), the forms copied (copy_ch13b_forms.py), the commit message (this sitting's and sitting
11's, for the owner's word).
'''
assert not re.search(r'/Users/(?!Shared/)', SEC) and os.path.expanduser('~') not in SEC
open(P, 'a', encoding='utf-8').write(SEC)
print('appended', len(SEC.encode()), 'bytes to the map;', sum(1 for _ in open(P, encoding='utf-8')), 'lines now')
