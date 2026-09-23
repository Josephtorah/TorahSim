#!/usr/bin/env python3
# THE DEUTERONOMY WALK sitting 13b — THE COMPILE OF CHAPTER 15: THE DESIGN appended to the map at the close of RUN A, after the rereads and the measurements
# (ch15_compile_recon.py, ch15_docket_scan.py, ch14_aramaic_nfkc.py) and BEFORE any code — write_ch14b_design.py's form (the previous last section asserted, the
# section appended whole, the lint after). Every number below is read from the recon's, the scan's and the NFKC re-measure's prints named beside it. RUN FROM
# THE REPO ROOT. Typed in two parts (write_ch15b_design_p1.py, _p2.py) and assembled.
import os, re, subprocess
ROOT = subprocess.check_output(['git', 'rev-parse', '--show-toplevel'], text=True).strip()
P = f'{ROOT}/World/step9/DEUTERONOMY_WALK.md'
s = open(P, encoding='utf-8').read()
assert s.rstrip().split('\n## ')[-1].startswith('Sitting 13 — CHAPTER 15 — AS BUILT'), 'the previous last section is not sitting 13\'s AS BUILT'
assert '## Sitting 13b — THE COMPILE OF CHAPTER 15' not in s
SEC = '''


## Sitting 13b — THE COMPILE OF CHAPTER 15, Deuteronomy 15:1-23 (2026-09-22; the owner: "Go" after sitting 13's commit b0eaa56 — the tree clean but for the docket gitlink and the commit's own records): THE DESIGN — written at the close of RUN A under THE COST RULES (two runs + the tail, the docket its own two runs by the ~700 clause; the rereads: THE_STEPS' compiler block whole, Step 2 whole and Step 5's head, the sitting-13 AS BUILT and the 13b box (a)-(o), the 12b design's opening, checkpoints and order as the compile's form; the measurements: ch15_compile_recon.py TYPED in two parts on 12b's form (the kin's seats, the kinds and effects, the registry, the tape, the sabbatical count, the finder's forms, the ledgers — 663,317 bytes, read by a digest of its seven sections with section 2 cut to the kin's nineteen modules), ch15_docket_scan.py derived from 12b's by asserted substitutions (derive_ch15_docket_scan.py — the candidate ranges of the box's (o) sized; the Tosefta chapters sized beside them), ch14_aramaic_nfkc.py the box's (m) — all in the scratchpad) and BEFORE any code

THE RUNS AND THE DOCKET'S OWN: RUN A the rereads, the measurements and this design — CLOSED HERE, a clean compaction point (#207); THE DOCKET by the union rule in
TWO RUNS by the ~700 clause (975 addresses in the dump — LINK 118 in 29 works, TOPIC 857 with the four Tosefta chapters; 249 credited by address at the scan; 726
to read whole) — D1 THE SMALL WORKS: every address outside Kiddushin 14b-22b and Bekhorot 25a-28b — the link rows of the other twenty-seven works, the forty-six
Mishnah rows (Sheviit 10 whole 9; Kiddushin 1:2-3; Peah 8:7-9; Bekhorot 1:1-2, 2:6-9, 3:3-4, 4:1-2, 5:1-6 and 6 whole 12; Temurah 3:5; Arakhin 8:7; Shekalim 5:6;
Chullin 2:9), the Tosefta (Sheviit 8: 12, Kiddushin 1: 11, Bekhorot 1: 6, 2: 7), Gittin 36a-37b (64), Arakhin 32b-33a (39), Makkot 3b (17), Rosh Hashanah 8b-9a
(20), Bava Metzia 31b (15) and 71a (20), Ketubot 67b (18), Bekhorot 33a-37b (189) and 53b (17) — the counts computed from the dump at D1, never typed; D2 THE
TWO LONG RANGES WHOLE WITH THEIR OWN LINK ROWS — Kiddushin 14b-22b (305 segments, 56 credited) and Bekhorot 25a-28b (121, 8 credited), THE CLEAN POINT BETWEEN
KIDDUSHIN AND BEKHOROT TAKEN UNCONDITIONALLY (sitting 13's lesson 5 — the point is the design's, the compaction his); EVERY ROW WHOLE — the credited rows CARRIED
with their ledgers' own verdict lines (12b's form, ch14_credit_carry.py derived; the credits' ledgers deu_14's exam 75, EXOD_TALMUD_TRIAGE 57, deu_12's exam 48,
the priesthood docket 17, the korach exam 16, the persons ledger 13, the sheviit docket 10, the ordinances docket 7 …), the uncredited read whole in chunk files
(the cap 64,000 — 10b's D2 lesson), the parts on 12b's whole-row instruments (ch14_docket_A.py's form, ch14_docket_common.py, the U file for the unresolved
rows), the writer derived from 12b's, coverage computed — each run its own clean point; RUN B the probes to FAIL (readback Q40-Q42, BEFORE the types — 7b's
lesson 2), the types by script with the docket's names, the callees' facts printed before any assert (every CALL's ask read at the cell's own source — 10b's
lesson 2), the runner in parts with the fast checker and the generated CASES, the recorder with the cache OFF (7b's lesson 1) and the stitcher, the literals
DG1-DG9, the tape to 10/10 with THE REST, checkpoint_check.py --all AFTER the tape, the records writer and the copier WRITTEN, gates_chain.sh LAUNCHED in the
background (the positions step at FOUR workers if the owner rules it; eight the standing form), the clean point; THE TAIL after the compaction: the summary read
once, the demands filed, the records from the sheet in one call, the forms copied, this section's AS BUILT, the commit message for the owner's word.

THE MEASUREMENTS (what the tape, the runners, the registries and the running world say before a line is typed — ch15_compile_recon.out, 663,317 bytes; the
digest 316,692): THE COUNTER stands at day 908865 (the snapshot world: entities 319, log 3616); the tape's LAST LINES are chapter 14's five own-day lines
(sons_and_mourning_declared, food_law_declared, carcass_and_kid_declared, second_tithe_declared, third_year_tithe_declared) after chapter 13's four, its LAST
MARKER the forward marker at Deut 10:12 (M['speech_resumed_10']); RUN (1332, 96, 88, 0, 12, 1641, 45, 319, the four pairs, 127), PREVIOUS_RUN 11b's (1327, 96,
88, 0, 12, 1634, 44, 319, the four pairs, 127); markers 172 (text_constrained 108, reading_placed 49), events text_constrained 110 / page_order 1164 /
reading_placed 58; CENSUS (2520, 1319, 1332, 1185, 6, 10, 9, 0, 71, 172, 131, 15, 26, 877, 272); 69 spans, 74 daemons (installed_by boot 33, erected 3,
covenant_blood_thrown 14, called_from_the_tent 17, sentence_declared 2, statute_declared 2, milluim_blood_sprinkled 1, entered_the_land 1, pending 1), kinds
1161, effects 1061; the D series DA-DF in use (nine each) — THE NEXT NAME DG; 689 edges, 208 pointers — NO pointer and NO edge naming Deut 15; THE REGISTER:
NO seat naming Deut 15 and none naming the kin's seats; the readback probes Q1-Q39 on file (Q10 unused), the next Q40. THE KIN'S CELLS, FOUND BY THE REFS
PER DEF: THE JUBILEE ENGINE ALREADY ROUTES THE MONEY RELEASE HERE — cold_run_yovel.py's cell 'debt_release': cell('routed_deut_15', M, "the money release is
Deuteronomy 15's (THE TWO RELEASES …") and its "release ON THE ACT; and 'even though they did not release' (Rosh Hashanah 9b:2-3)"; yovel's cells cycle,
jubilee, sabbatical (torah_labors), interest, interest_scope('brother' / 'foreigner'), hebrew_slave, going_out, support_duty, sale_manner; law_yovel watching
brother_grew_poor, brother_sold_as_slave, silver_lent, land_sown, jubilee_proclaimed, installed_by entered_the_land; THE EFFECTS ON FILE land_release (the
seventh-year TIMER on a LAND entity), sabbath_debt (the DEBIT on the land's account), jubilee_release ("a world-clock timer that overrides even the pierced
slave's forever"), jubilee_year and jubilee_holds, goes_out_in_the_jubilee (the entitlement), interest_barred (the BLOCK on the lender toward his brother);
calendar.sabbatical asks home_engine / timer / work_scope — Exodus 23:10-11 the same release by call into the jubilee engine; THE SLAVE'S TERM CLOCK IS
EXODUS 21'S — cold_run_mishpatim.py's F1 "the Hebrew slave's release list (code: 21:2-6, 8)", its IMPORT row "Leviticus 25; Kiddushin 15a:19: written even
for the pierced 'forever'", law_mishpatim watching redeemed_by_deduction (pays, goes_free); cold_run_mishpatim_3.maidservant (designation, exits, foreign_sale,
her_age, redemption, the_three, the_two_exits — its cell already citing "7 8, from Deut 15:12; redeemed against his will, not sold twice (Kiddushin 18a:5)" with
term_clock and goes_free, the fire E_('goes_free', … due=world.clock.after(6, 'year'), value='the seventh year')); mishpatim_2's slave_maimed (released,
goes_free); THE KINDS ON FILE acquire_hebrew_slave ("the six-year term clock"), slave_pierced ("his master shall pierce his ear"), redeemed_by_deduction,
brother_sold_as_slave, brother_grew_poor, silver_lent, garment_pledged, wage_withheld; THE ORDINANCES' LOAN CELL — cold_run_ordinances.loan asks bite_noun,
court_only, creditor_manner, five_prohibitions, foreigner, im_obligation, interest_spec, pledge_sunset, PRIORITY_LADDER, who_transgresses, widow_not_pledged,
and its cell 'lending_is_obligation' already NAMES THIS CHAPTER ("22:24 'IF money you lend' — 'if' here is OBLIGATION (proven from Deut 15:8's 'you shall
surely lend')"); law_ordinances watching silver_lent, garment_pledged (pledge_returned_by_sunset the TIMER), firstling_born, firstborn_son; ordinances.firstling
(donkey_by_call, eighth_and_onward, with_its_mother, two_seats_one_timer), ordinances.gifts (firstborn_son, five_sela, caesarean, thirty_days); THE SEVERANCE
GIFT ALREADY PRICED — cold_run_erection.repeats' cell 'five_selas_to_the_severance_gift' ("Kiddushin 17a:7 — R. Meir prices the Hebrew slave's severance gift
(Deut 15:13 …)"); THE FIRSTLING'S CELLS — cold_run_korach.the_gifts (sixty-one asks: blemished_firstborn, blemished_keeping, blemish_expert, clean_firstborn,
firstborn_blood_placement, firstborn_eaters, firstborn_eating_window, firstborn_portions, firstborn_sale, firstborn_without_altar, opens_the_womb,
suspect_firstborn, twins, unclean_firstborn_scope, redemption_* …), the effect consecrated_firstborn ("the firstborn belongs to the Lord from the womb; a
status written at birth"), redeem_or_break; cold_run_temurah's ink probe list carrying "[IMPORT] the firstborn: you SHALL sanctify (Deut 15:19)" against
27:26's "no man shall sanctify" (temurah.consecrate); cold_run_priesthood.acceptable (firstling_table, blemished_blood, blemished_limb, castration, eighth_day,
passing_blemish, worked_with …) with its closing rule "Mishnah Bekhorot 6:11-12 — one list serves the firstling (Deut 15:21 [IMPORT]) and Lev 27's redemption",
and its 22:10 cell "toshav: acquired_forever_the_pierced_slave; sachir: acquired_for_years"; THE PLACE AND THE BLOOD — cold_run_place_name's
the_profane_slaughter_the_blood_and_the_gates (the_blemished_consecrated, the_blood_like_water, the_unclean_and_the_clean, you_may_not_eat_within_your_gates,
the_eaters) and the_border_enlarged_and_the_altar (as_the_gazelle_and_the_hart, the_blood_is_the_life, the_bloods_classes, the_rite_of_slaughter), its DATA
the_blood_classes and like_water_four_ways; cold_run_sanctions.blood (atones, ban, karet_own_eating, lashes, which_blood) and covering (hunted_of_any_kind,
consecrated, not_with_the_foot); THE POOR — cold_run_holiness.gifts (poor_defined, recipients, for_named_poor, robs_the_poor …), holiness.wage (clock,
first_morning, hire_kinds, resident_alien), law_holiness watching wage_withheld (wage_due_by_morning the TIMER); cold_run_food_tithe.the_third_year
(the_seventh_year_by_the_cycle, the_removal_date, the_four_in_want, the_measures) and the_second_tithe (the_firstling, the_firstling_from_outside,
the_year_passed — 106:5's cell already on file, year_by_year); THE ANALOGIES' SEATS — cold_run_seducers' DATA row "Belial's word (the Torah's two seats; the
four analogies on the shelf); the exam's person the one who turns his eyes from the poor" (13:14 for 15:9 — 117:3's I2), cold_run_metzora.eighth (oil_on_blood,
precedence — the leper's right ear for 122:5's I2), cold_run_covenant_at_horeb (5:15 — "a slave in Egypt" the book's five), cold_run_blessing_and_curse (11:13's
second paragraph; 41:3's release after the conquest), cold_run_good_land.receipt_seats naming the four "as He spoke to you" (12:20, 15:6, 26:18-19, 29:12),
cold_run_primeval (Abel's firstlings 4:4 — first_offerings_brought on the tape), cold_run_exodus_story (the servitude decreed and the release refused —
the tape's decree_of_the_sojourn and release_refused, the close 'release_demanded' at Exod 12:31); THE REGISTRY MAP: NO row for the chapter's persons
(the-needy, the-creditor, the-hebrew, the-slave, the-maidservant, the-master, the-firstling, the-hireling …); THREE HOMOGRAPHS to guard — 'the-servant' maps to
servant_of_abraham (Genesis 24's), 'the-place' to the_place_luz_bethel, 'the-flock' to the_flock: none of them this chapter's; THE SABBATICAL COUNT: the clock
in the count era — calendar_parameters.yaml's eras row 'count' (new_year_month 7; "day 0 = the first day of the seventh month of count-year 1 — Lev 25:8 'you
shall count for yourself'; Mishnah Rosh Hashanah 1:1 the first of the seventh month for years, sabbaticals and jubilees; the count's start after entry per
count_start_offset_years"), yovel.cycle(year) the year's class (work_year / sabbath_of_the_land / jubilee — the cells food_tithe reads as YO_C3, YO_C6, YO_C7,
YO_C50), the clock's methods after / at_year / date_in / day_in / elapsed_in / next / year_in (the recon's render fell on 'date' — an attribute, not a method:
the running world's date is READ at RUN B through year_in, the print the measurement) — THE WORLD AT CHAPTER 14'S END STANDS BEFORE THE ENTRY: law_yovel is
installed_by entered_the_land, the count not begun, the release's cells answer "no count" on the bare world as DF6's removal did; THE FINDER'S FORMS READ
(register_census.py): a RECEIPT is "as (834) commanded (6680) the LORD (3068 within three)" or "according to ALL that commanded the LORD", a HEADER or FOOTER
is "these (428)" + statutes / commandments / judgments / words / testimonies (HEADER by a second-person imperfect), a REGISTER "these" + generations / names /
sons / families / the counted, a COUNT LINE a count-noun or a register footer with a numeral — 15:2's "and THIS (2088) is the WORD (1697) of the release" is
the footer NOUN in the singular after "this", not "these", and 15:6's "as He SPOKE (1696) to you" is not "commanded": both outside the forms by one token each,
THE REGISTER'S TWO NEAR MISSES a DATA row (the box's (l)); THE NFKC RE-MEASURE (ch14_aramaic_nfkc.py — the box's (m)): ZERO presentation-form letters
(U+FB1D-FB4F) in the Onkelos export's 956 rows, the only characters outside the letters and the points three quotation marks; the 27 onk_seats literals of
ch14_ink.py — 0 move under the fold; chapter 14's 29 verses and the book's 956 — 0 differ under NFKC: CHAPTER 14'S ARAMAIC COUNTS STAND AS MEASURED, and sitting
13's lesson 4 is CORRECTED — the export carries no presentation form, and the needy word's five seats (15:4, 7, 9, 11; 24:14) are found by the plain substring
(measured); whatever the earlier miss was, it was on the typing side, not the export's, and the piece cutter needs no fold (the lesson's correction into this
sitting's AS BUILT, a CORRECTION row appended to the reading's ledger at the tail, the memory's walk note).

THE RUNNER cold_run_release_firstborn.py (the 70th) and THE DAEMON law_release_firstborn (the 75th; given_at Deut 15:1; installed_by boot as the Deuteronomy
laws are; the wrap declared before the code and verified by the daemon gate): FOUR OWN-DAY LINES ON THE COUNTER'S DAY (40, 11, 1), NO MARKER (the speech
continues from 10:12 as chapters 11-14 did) — release_law_declared (15:1-6), hand_opening_commanded (15:7-11), hebrew_slave_law_declared (15:12-18),
firstling_law_declared (15:19-23) — each a statute by form (second_tithe_declared's), the exam's case kind release_firstborn_case a person brought to a cell's
ask; SEVEN CELLS ON THE SEVEN CLAIMS' SPANS (the manifest's DV15-01..07): F1 the_release (15:1-3), F2 the_needy_and_the_blessing (15:4-6), F3 the_hand_opened
(15:7-11), F4 the_hebrew_slave (15:12-15), F5 the_awl_and_the_double_hire (15:16-18), F6 the_firstling (15:19-20), F7 the_blemish_and_the_blood (15:21-23) —
and the_readback the table; every ask a claim of the ledger's rows, every parameter the data channel.

F1 THE RELEASE (15:1-3) — THE RELEASE IS AN EFFECT ON THE DEBTS AT THE SEVENTH YEAR'S END: the STATUS debt_release_owed written on israel_people at the line
(the standing duty — "every creditor shall release that which he lent to his neighbor"), its value THE RELEASE DATE a CLOCK DATUM the_release_date READ FROM
THE CYCLE BY CALL (yovel.cycle(year) — the year whose class is sabbath_of_the_land; "END" IS THE YEAR'S END by I2 with 31:10 at 111:1 and by 109:3's Booths; the
last day of the seventh year the release's moment — Rosh Hashanah 8b-9a at the docket: the first of Tishri the new year for the sabbatical, R. Yose the
Galilean's "the seventh year, the year of release, draws near" at 111:8 and 117:4; Sheviit 10:1 the seventh year releases at its end; the running world's count
read and printed, "no count" before the entry), THE ONE CALENDAR (111:3-7 — seven years for the whole world, never for each debtor: I2 named in the Hebrew,
the two paradigms deadlocked and broken; the debtor's own clock the REFUTED arm), THE ONSET a PARAMETER the_release_onset (111:9-11 and 41:3 — after the
conquest and the division; Arakhin 32b-33a at the docket: the count from the fourteenth year), THE TERRITORY a PARAMETER the_release_territory (112:11 — "to
the LORD": in the Land and outside it; Gittin 36a-b at the docket: outside the Land and when the jubilee is not in force the release stands by decree — the
two arms; Kiddushin 38b credited by address), THE MANNER the word said (112:1 — Mishnah Sheviit 10:8 inside the spine: "I release it"; the debtor who pays
anyway thanked), THE OBJECT loans only — not theft, deposit, wage or shop credit unless written up as a standing debt (112:5-7; Sheviit 10:1-2 — a DATA row
the_release_object with the exceptions' list), THE TWO YEARS' POWERS (112:2-4 — I1 twice, cancelled by two verses' "this": the seventh year releases the
loan, the jubilee frees the slave — Leviticus 25:13 by CALL to yovel.jubilee), THE EXACTION a BLOCK exaction_barred (112:8 — "he shall not exact"; the
neighbor and the brother two exclusions 112:9-10; the foreigner a positive command 113:1 — the_foreigner by CALL to yovel.interest_scope('foreigner'), the
same noun's rule at 23:21 when it comes), THE PLEDGE-LOAN NOT RELEASED (113:2 — Sheviit 10:2; the pledge by CALL to ordinances.loan(pledge_sunset)), and
HILLEL'S PROZBUL A PARAMETER FROM THE ANSWER SHEET the_prozbul (113:3 — Sheviit 10:3-4 inside the spine: the court's writ "I hand over to you, the judges …,
that I may collect any debt at any time"; "your hand" and not the court's — the verse leaves the procedure open; Gittin 36a-37b at the docket: Hillel's
reason 15:9 and the release rabbinic in his day — a procedure, not code; the witnesses Makkot 3b); Exodus 23:10-11 by CALL to calendar.sabbatical
(home_engine), Leviticus 25:1-7 by CALL to yovel.sabbatical; the exam: Mishnah Sheviit 10:1-9 whole (the loan released and not, the prozbul's text and its
conditions, the paying debtor, the orphans' loan), Tosefta Sheviit 8 sized (the design reads its 12 rows at D1).

F2 THE NEEDY AND THE BLESSING (15:4-6) — THE TWO VERSES UPHELD BY A CONDITION, NOT A THIRD VERSE (114:1, 118:1 — I13's question without its third verse): a
STATE VARIABLE the_needy_condition with two arms — the blessing's arm ("there shall be no needy among you" when the commandment is kept, 15:5) and the default
("the needy shall never cease", 15:11) — the cell returning the arm from the world's state (the condition 15:5's hearing), the blessing only in the Land
(114:2), the conquest first (114:3); blessings_for_hearing REUSED (chapter 11's conditional HEAVEN entry — 15:5 "if you diligently hearken" 28:1's header,
fourteen of seventeen in order, the same form; a second entry on israel_people — the grep decides the stale literals); THE WORDS OF THE SCRIBES (115:1 — the
oral law named at "hear, you shall hear": a DATA row the_scribes_words), the light as the weighty (115:2); THE RECEIPT'S REFERENT FORWARD — 116:1 answers
15:6's "as He spoke to you" with 28:3 "blessed shall you be in the city", a verse the book has not yet spoken: THE POINTER ROW OF THE READBACK WITH ITS
REFERENT AHEAD, graded H (the sixth provenance tag — a labeled HYPOTHESIS until 28:3's sitting; the receipt's third shape after the Name's and the
back-pointer's; no new readback form — the pointer row with a referent ahead and the H flag); lend not borrow, rule not be ruled (116:2-3 — 28:12 the twin by
CALL when it comes; Judges 1:7's Adoni-bezek the run's case; the sela and the shekel by CALL to yovel.valuation's twenty gerah); the exam: Rosh Hashanah
8b-9a's year, Makkot 3b's witnesses (the link rows).

F3 THE HAND OPENED (15:7-11) — THE RANKS OF THE POOR A PRECEDENCE PARAMETER the_needy_ranks (116:4-8: not others; the hungrier; the father's brother before
the mother's; the city before another city; the Land before outside it; the door-to-door beggar owed nothing from the fund — Bava Metzia 71a at the docket:
"the poor of your city first", the ladder ordinances.loan(priority_ladder) already holds by CALL), the heart's state before the hand's (116:10-11 — the
BLOCK hand_shutting_barred on the two verbs "harden" and "shut", 15:7), OPEN AND GIVE A HUNDRED TIMES (116:12, 117:6 — the doublings read REPEAT WITHOUT
LIMIT; the STATUS hand_opening_commanded on israel_people; lending_is_obligation by CALL to ordinances.loan — the cell that names 15:8), the gift dressed as a
loan (116:13), THE PLEDGE A DISPUTE the_pledge_dispute (116:14 — R. Judah and the sages: two arms; Bava Metzia 31b at the docket), THE MEASURE OF NEED
the_measure_of_need (116:15-18 — "sufficient for his need": not to enrich him, even a horse and a slave, Hillel's horse, the litra of meat, the wife by "for
him"; Mishnah Peah 8:7-9 with Ketubot 67b at the docket — the poor man's ration and the fund's rule), "BASE" without a yoke (117:1 — E30) and read as
idolatry by I2 with 13:14 (117:3 — the BLOCK base_thought_barred, 15:9; Belial's two seats by CALL to seducers' DATA row — the TRANSFER taught by the Sifrei
117:3, a labeled edge), beware and lest two prohibitions (117:2), THE CRY A HASTENER AND THE SIN UNCONDITIONAL (117:5 with 279:4 word for word — cry_heard
REUSED (the HEAVEN entry of the pledged poor man's cry, Exodus 22's) and bears_sin REUSED (the STATUS "it be sin in you" — the divine ledger); 24:15's
hireling by CALL when it comes), the secret gift (117:7 — Mishnah Shekalim 5:6 inside the spine: the chamber of the silent), THE FOUR GRADES OF THE GIVER
(117:8 — a DATA row), the three nouns three measures (118:3), THE BLESSING ON THE WORK OF THE HAND the HEAVEN entry work_of_the_hand_blessed (15:10 "in all
your work and in all you put your hand to" — 14:29's twin; the same entry again at 15:18; a reuse if 14:29's line wrote one — the registry read at the types
step decides the name); 14:28-29's four at the gate by CALL to food_tithe.the_third_year(the_four_in_want), the poor defined by CALL to
holiness.gifts(poor_defined); the exam: Mishnah Peah 8:7-9, Ketubot 67b, Bava Metzia 31b and 71a, Mishnah Shekalim 5:6.

F4 THE HEBREW SLAVE (15:12-15) — THE THREE CASES, EACH TWIN LAW ITS OWN (118:4 — Exodus 21:2 the buyer's, Leviticus 25:39 the self-seller's, 15:12 THE
COURT'S SALE: the cell's ask the_three_cases with the sale's road as the variable; the term SIX YEARS by CALL to mishpatim's F1 term clock — the same date six
years on, goes_free the fire; the woman ADDED here against Exodus 21:7 — "a Hebrew man or a Hebrew woman", the maidservant's exits by CALL to
mishpatim_3.maidservant(the_two_exits): years, jubilee, deduction, signs — Mishnah Kiddushin 1:2-3 inside the spine at 118:5 and at the docket with Kiddushin
14b-22b whole), THE MAN'S AND THE WOMAN'S EXITS TWO TABLES the_exits_tables (118:5 — a DATA row of the two lists), the son not the heir by two shared features
(118:6), THE FUGITIVE OWES HIS YEARS, THE SICK MAN NOT (118:7 — Kiddushin 17a at the docket), THE GIFT — furnishing_commanded the STATUS and
empty_sending_barred the BLOCK at the line (15:13-14 — "you shall not send him away empty"; the three sendings the gift's cases from the verb said three
times, the self-redeemer out (119:1), NOT TO HIS HEIRS (119:3), ONLY WHAT RESEMBLES THE PARTICULAR — fit for a blessing or bearing young, A DISPUTE
the_gift_feature (119:4 — I6's shape; Kiddushin 17a), THE MEASURE the blessing (119:5 — four opinions: severance_gift_owed the DEBIT the case writes on the
master toward the slave at the sending, its amount A PARAMETER the_severance_gift by CALL to erection.repeats(five_selas_to_the_severance_gift) — R. Meir's
five selas of each kind, R. Judah's thirty, R. Simeon's fifteen: Kiddushin 17a at the docket)), EGYPT THE MODEL OF THE GIFT (120:1 — the two spoils in two
verses: the exodus's "not empty" by CALL to exodus_story's close), BY DAY THEY PIERCE (120:2 — "today": a TIME DATUM the_piercing_by_day), THE MEMORY
(15:15 — 5:15 by CALL to covenant_at_horeb: the book's five "remember that you were a slave"; the chapter's ONE narrative verb "and He redeemed you" the
compile's T1 row — a REFERENCE row on the tape's release_demanded closed at Exod 12:31, never a second act); Leviticus 25:39-55 by CALL to yovel.hebrew_slave
and going_out; the exam: Mishnah Kiddushin 1:2-3, Kiddushin 14b-22b whole, Tosefta Kiddushin 1 sized.

F5 THE AWL AND THE DOUBLE HIRE (15:16-18) — THE SLAVE WHO STAYS: two sayings (121:1), two times (121:2 — the_awl_timing a DATA row: at the term's end, not
before), the love MUTUAL and the master's house (121:3 — "because he loves you and your house"; Exodus 21:5's wife and children by CALL to mishpatim's F1),
ILLNESS IN EITHER BARS THE RITE (121:4 — Kiddushin 22a-b at the docket), THE AWL any tool or metal A DISPUTE the_awl_tool (122:1 — Kiddushin 21b; R.
ISHMAEL'S THREE PLACES WHERE THE HALAKHA CIRCUMVENTS SCRIPTURE a DATA row the_three_circumventions — the blood's dust, the divorce's writ, the awl: the
code/data separation law's hardest case inside the spine), THE JUDGES PRESENT (122:3 — Exodus 21:6's "to the judges" by CALL; here NO judges, NO doorpost,
"into the door" — the readback's SHORTENED row), THE UPPER RIGHT EAR the_ear (122:5-6 — I2 with the leper's ear, Leviticus 14:14 by CALL to metzora.eighth —
the edge a TRANSFER taught by the Sifrei 122:5 and Kiddushin 15a, labeled; the priest not pierced lest he be blemished — priesthood.blemish by CALL), through
the ear into the door (122:7), "FOR EVER" THE MASTER'S LIFETIME (122:8 — I2 named in the Hebrew on the word at 15:17 and Exodus 21:6; the son not the
daughter, the pierced no heir; the STATUS serves_for_ever the case writes on the pierced slave, its term the master's life — and THE JUBILEE FREES EVEN HIM:
jubilee_release ON FILE by CALL to yovel, "the timer that overrides even the pierced slave's forever" — Kiddushin 15a at the docket), "LIKEWISE" REACHES THE
GIFT, NOT THE AWL (122:9 — the maidservant furnished, never pierced: the readback's DISAGREES row against Exodus 21:7 "she shall not go out as the
menservants do", OPEN for the exam — Kiddushin 14b-15a at the docket resolves it: she goes out by years, by signs and by the jubilee; the row's resolution
DATA, never the ink's), THE DOUBLE HIRE the_double_hire (123:1 — day and night: the night's service the Sifrei's reading AGAINST THE MEKHILTA'S — a DISPUTE
OF TWO SPINES, two arms; Kiddushin 15a at the docket; 123:2 work not idleness), the blessing beside every money loss (123:3 — work_of_the_hand_blessed the
second seat, 15:18); the hireling's wage by CALL to holiness.wage(hire_kinds); the exam: Kiddushin 14b-22b whole (the awl's folio 21b-22b), Tosefta
Kiddushin 1.

F6 THE FIRSTLING (15:19-20) — CONSECRATED FROM THE WOMB, SANCTIFIED FOR ITS VALUE: consecrated_firstborn REUSED (the STATUS "written at birth" — ordinances'
firstling_born and korach's opens_the_womb by CALL: the consecration is Exodus 13:2's and Numbers 18:17's, not this verse's), "YOU SHALL SANCTIFY" AGAINST
"NO MAN SHALL SANCTIFY" UPHELD BY DIVIDING THE SPHERES (124:4 — Mishnah Arakhin 8:7 inside the spine and at the docket: for its value, never for the altar;
Leviticus 27:26 by CALL to temurah.consecrate — the cell whose probe list already carries 15:19 as its IMPORT; the STATUS firstling_sanctification_commanded
on israel_people at the line, its value the_sanctify_for_value a PARAMETER: the declaration a mitzvah, the value the Temple treasury's — Arakhin 29a
credited), its year and the blemished from "every" (124:1), THE CAESAREAN OUT (124:2 — Mishnah Bekhorot 2:9: not a firstling — the_caesarean a DATA row;
korach.the_gifts(opens_the_womb) by CALL), the consecrated by a refuted a fortiori then the verse (124:3 — I1; 71:6's form), "YOUR" TWO WAYS (124:5 — a
DISPUTE the_your_two_ways: the owner's or the priest's — the firstling's flesh the priest's by Numbers 18:18, by CALL to korach.the_gifts(firstborn_eaters);
"you and your household" 14:26's twin), the two bars crossed by four a fortiori arguments and THE TWO FILES READING THE CLOSING VERSE OPPOSITE WAYS (124:6 —
a DISPUTE of the two files the_files_disagree, for the exam), THE WORK AND THE SHEARING a BLOCK firstling_work_and_shearing_barred (15:19 — "you shall not
work with the firstling of your ox nor shear the firstling of your flock"; Bekhorot 25a-28b at the docket: the shearing and the work, the blemished
firstling too; Mishnah Bekhorot 3:3-4; the herd's tithe's "under the rod" by CALL to temurah.tithe), "YEAR BY YEAR" TWO DAYS ACROSS THE YEAR'S EDGE
(125:1 — THE FIRSTLING'S YEAR a CLOCK DATUM the_firstlings_year: twelve months from its birth the eating window, the last day of its year and the first of
the next both "year by year" — Bekhorot 26b-27b at the docket; Mishnah Bekhorot 4:1 the unblemished within its year, the blemished thirty days after — the
window by CALL to korach.the_gifts(firstborn_eating_window); the year passed no bar 106:5 — food_tithe.the_second_tithe(the_year_passed) by CALL: the cell
on file), BEFORE THE LORD AT THE PLACE (15:20 — the formula's fourth seat in this form by CALL to place_name.the_place_chosen; holy_things_in_the_gates_barred
REUSED, 12:17-18's BLOCK — a second entry, the grep decides), the firstling from outside the Land (Bekhorot 53b at the docket; food_tithe's
the_firstling_from_outside by CALL), Abel's firstlings (Genesis 4:4 — first_offerings_brought on the tape, a REFERENCE row); the exam: Mishnah Bekhorot 1:1-2,
2:6-9, 3:3-4, 4:1-2, 5:1-6, Bekhorot 25a-28b, 53b, Mishnah Temurah 3:5, Mishnah Arakhin 8:7, Tosefta Bekhorot 1-2 sized.

F7 THE BLEMISH AND THE BLOOD (15:21-23) — THE CLASS VISIBLE AND PERMANENT: born and acquired in by "any", LAME AND BLIND THE PARTICULARS THAT TEACH THE
CLASS (126:1 — I8 in its own words; 147:3-4 the same at 17:1 by CALL when it comes; the list by CALL to priesthood.acceptable(firstling_table) — "one list
serves the firstling (Deut 15:21 [IMPORT])": Mishnah Bekhorot 6 whole at the docket and 33a-37b whole; Leviticus 22:17-27 and 21:16-23 by CALL to
priesthood.acceptable and .blemish — the_blemish_class the cell's verdict, never a list typed here), the permanent blemish lent to all the consecrated (71:6
— I2 on "your gates" with 12:15; place_name.the_profane_slaughter_the_blood_and_the_gates(the_blemished_consecrated) by CALL — the cell on file), the
blemished EATEN IN THE GATES the unclean and the clean together (15:22 — 12:15 and 12:22's clause at its THIRD seat: VERBATIM in the readback, by CALL to
place_name(the_unclean_and_the_clean, as_the_gazelle_and_the_hart)), one dish and the heave-offering apart (71:7-8 — a DATA row), THE BLOOD (15:23 —
12:16's formula at its third seat: "on the earth you shall pour it as water" by CALL to place_name(the_blood_like_water) and sanctions.blood(ban) — no new
write, the ban 12:16's and Leviticus 17's; drinking is eating (126:2), THE WITNESSES' WARNING gating the penalty (126:3 — REUSED from sanctions' warning
datum), THE OLIVE a quantity (126:4 — REUSED, sanctions' olive), the ground not the pit, the house not the market lest he imitate the sectarians (126:5 —
Mishnah Chullin 2:9 at the docket — a DATA row the_pouring_place), the neck and the seeds made susceptible (126:6 — a DATA row); Leviticus 17:13's hunted
blood covered by CALL to sanctions.covering — the contrast the readback names; Keritot 20b-22a credited from chapter 12's docket by address; the exam:
Mishnah Bekhorot 6:1-12, Bekhorot 33a-37b, Mishnah Chullin 2:9.

THE READBACK ON THIS CHAPTER — THE FORMS ON FILE, NO NEW FORM: chapter 15 is law from its first word to its last (Moses' voice, no divine frame, ONE
narrative verb — 15:15's "and He redeemed you", a REFERENCE row on the tape's close release_demanded at Exod 12:31, never a second act; no retrograde row),
so the table is the laws' readback (chapter 5's form) over the kin's cells by CALL: 15:1-2 REFERENCE to Exodus 23:10-11 and Leviticus 25:1-7 — TURNED (the
land's release turned to the money's: 111:2's "two releases"); 15:3 the foreigner SUPPLIED; 15:4-6 the state row (the_needy_condition) and THE POINTER ROW
WITH ITS REFERENT AHEAD (15:6 → 28:3, graded H); 15:7-11 SUPPLIED (the hand opened: no seat in Exodus — 22:24's loan the nearest by CALL, its
lending_is_obligation cell naming 15:8); 15:12 REFERENCE to Exodus 21:2 — VARIANT (the woman added, "be sold" the niphal, "your brother"; Jeremiah 34:14 the
run's case named in the row); 15:13-14 SUPPLIED (the gift — no seat in Exodus; erection's price cell by CALL); 15:15 REFERENCE to 5:15 — VERBATIM in kind
(eleven in order); 15:16-17 REFERENCE to Exodus 21:5-6 — SHORTENED (no judges, no doorpost, "into the door") and 15:17's maidservant DISAGREES with Exodus
21:7 (OPEN — the exam resolves, the resolution DATA); 15:18 SUPPLIED (the double hire); 15:19 REFERENCE to Exodus 13:2, 22:29, 34:19, Numbers 18:15-18 and
Leviticus 27:26 — the "sanctify" DISAGREES with 27:26 (OPEN — 124:4's division of spheres the resolution, DATA); 15:20 REFERENCE to 12:17-18 and Numbers
18:18 — EXPANDED (year by year; "you and your household" against the priest's flesh — 124:5's dispute in the row); 15:21 REFERENCE to Leviticus 22:20-25 —
EXPANDED (lame or blind named); 15:22 VERBATIM 12:15 and 12:22 (the third seat); 15:23 VERBATIM 12:16 (the formula's third seat; Leviticus 17:13's
covering the contrast); the rows' census from the runner's print at RUN B, never predicted here; the open disagreements TWO (15:17, 15:19), ledger entries
citing them 0 until the exam.

THE PARAMETERS (the data channel, every one from the answer sheet or the spine, none in the code; the registry calendar_parameters.yaml's sojourn_start form
for the clock data): the_release_date (CLOCK DATUM — the seventh year's end by the cycle), the_release_onset (after the conquest and the division — 41:3;
Arakhin 32b), the_release_territory (in the Land and outside; the decree's arm — Gittin 36a), the_release_object (loans only — Sheviit 10:1-2), the_prozbul
(Sheviit 10:3-4; Gittin 36a-37b), the_needy_condition (the state variable's two arms — 114:1, 118:1), the_needy_ranks (PRECEDENCE — 116:4-8; Bava Metzia
71a), the_measure_of_need (Peah 8:7-9; Ketubot 67b), the_pledge_dispute (116:14; Bava Metzia 31b), the_exits_tables (118:5 — Kiddushin 1:2), the_gift_feature
(119:4 — a dispute), the_severance_gift (Kiddushin 17a — three opinions; erection's cell by CALL), the_piercing_by_day (120:2), the_awl_tool (122:1 — a
dispute), the_ear (122:5-6), the_for_ever (the master's lifetime — 122:8; the jubilee's override on file), the_double_hire (123:1 — two spines), the_firstlings_year
(CLOCK DATUM — the two days across the edge, 125:1; Bekhorot 26b-27b), the_sanctify_for_value (Arakhin 8:7), the_caesarean (Bekhorot 2:9), the_your_two_ways
(124:5), the_files_disagree (124:6), the_blemish_class (by CALL — Bekhorot 6), the_pouring_place (Chullin 2:9), the_three_circumventions (122:1), the_scribes_words
(115:1), the_four_grades (117:8) — twenty-seven rows, the count printed by the types script at RUN B and asserted there, never here.

THE EFFECTS (effect_vocabulary.yaml — the registry's own vocabulary, the ledger never the event stream): NEW debt_release_owed (STATUS on israel_people — the
standing duty at the seventh year's end, its value the date by call), exaction_barred (BLOCK — "he shall not exact"), hand_opening_commanded (STATUS —
"open, you shall open"), hand_shutting_barred (BLOCK — "harden" and "shut"), base_thought_barred (BLOCK — 15:9), work_of_the_hand_blessed (HEAVEN — 15:10
and 15:18; a reuse if 14:29's line already wrote one — the registry read at the types step), furnishing_commanded (STATUS — 15:14), empty_sending_barred
(BLOCK — 15:13), severance_gift_owed (DEBIT on the master toward the slave at the case), serves_for_ever (STATUS on the pierced slave — the master's
lifetime, the jubilee's override by call), firstling_sanctification_commanded (STATUS — for its value), firstling_work_and_shearing_barred (BLOCK) — twelve;
REUSED blessings_for_hearing (15:5-6), cry_heard (15:9), bears_sin (15:9), consecrated_firstborn (the case), released and goes_free (mishpatim's — the
case), holy_things_in_the_gates_barred (15:20), jubilee_release (by call), pledge_returned_by_sunset (by call) — every reuse a second entry whose count
literal the grep finds at RUN B (8b's and 10b's lesson: retyped from the print BEFORE the tape).

THE KIN BY CALL — THE TWO QUESTIONS ASKED (reference or transfer; taught by whom): release_firstborn → yovel (REFERENCE — the ink names the seventh year, the
jubilee, the sold brother: 15:1, 15:12; the cells cycle, sabbatical, jubilee, interest_scope, hebrew_slave, going_out, valuation), calendar (REFERENCE — Exodus
23:10-11's release by name), mishpatim (REFERENCE — Exodus 21:2-6's term clock, the awl's case kind, redeemed_by_deduction), mishpatim_2 (REFERENCE —
released), mishpatim_3 (REFERENCE — the maidservant's exits), ordinances (REFERENCE — the loan, the pledge, the priority ladder, the firstling's eighth day,
the firstborn son's gifts), erection (REFERENCE — the severance gift's price, 34:19-20's firstborn), korach (REFERENCE — Numbers 18:15-18's firstling by
name), temurah (REFERENCE — Leviticus 27:26 by name at 124:4), priesthood (REFERENCE — the blemishes' list by name at 15:21), place_name (REFERENCE — 12:15-16,
12:22-24's clauses verbatim; the place formula), sanctions (REFERENCE — the blood's ban and the covering), holiness (REFERENCE — the poor and the hireling's
wage), food_tithe (REFERENCE — 14:28-29's four at the gate, the year passed, the cycle's third year), covenant_at_horeb (REFERENCE — 5:15 verbatim), blessing_and_curse
(REFERENCE — 11:13's second paragraph, the same conditional), exodus_story (REFERENCE — the release demanded and closed; Egypt the model), primeval (REFERENCE
— Abel's firstlings), good_land (REFERENCE — the receipt seats' scan), seducers (TRANSFER — Belial's word 13:14 for 15:9, TAUGHT BY the Sifrei 117:3 (I2 on the
shared word), the exemplar named; a labeled edge), metzora (TRANSFER — the leper's right ear for the awl's, TAUGHT BY the Sifrei 122:5-6 and Kiddushin 15a
(I2 "ear — ear"), labeled); NO HYPOTHESIS EDGE but the receipt's forward pointer (H — a pointer row, not an edge); the census (dependency_census.py) files
the required edges from the ink at RUN B's first step and the file may not understate the code (rule 9); THE HOMOGRAPHS FALSE if matched: 'the-servant'
(servant_of_abraham), 'the-place' (Bethel), 'the-flock' — named in the registry's homographs DATA row with 15:2's loan and Moses' name (the reading's find).

THE PREDICTION'S ARITHMETIC: RUN = (1332 + 4, 96, 88, 0, 12, 1641 + W, 45 + 1, 319, the four pairs, 127) — events +4 (the four own-day lines), timers set +0
and fired +0 (no clock walk — the release's date read by call, never a timer set on the bare world before the entry), cancels 0, retro-writes 12 UNMOVED,
writes +W (the daemon's writes at the four statutes: the twelve new effects' first entries less the case-only ones — severance_gift_owed and serves_for_ever
are the case's, consecrated_firstborn the case's — plus the reuses' second entries; W READ FROM THE RUNNER'S PRINT at RUN B and typed into the literal from
it, the design's count fourteen a prediction to be checked, never the literal), daemons fired +1 (law_release_firstborn), entities +0 (israel_people on the
registry; no person, slave or beast an entity), closes +0 (no debit at the lines — the severance gift's debit the case's, its own world); PREVIOUS_RUN =
12b's RUN EXACTLY (1332, 96, 88, 0, 12, 1641, 45, 319, the four pairs, 127): THE REST drops the four lines by the runner's tag and the span and the daemon's
writes with them — no delta; NEWEST_RUNNER 'release_firstborn'; markers 172 UNMOVED (text_constrained 108, reading_placed 49 unmoved); events page_order
1164 -> 1168, text_constrained 110 and reading_placed 58 UNMOVED — READ, never predicted; CENSUS on tape 1332 -> 1336, kinds 877 -> 881 (the four statute
kinds on the tape; the case kind off it), subjects 272 UNMOVED, markers 172, closes 71 unmoved; the population table 148 UNMOVED; THE OPEN DEBITS ON
israel_people 10 UNMOVED; THE BLOCKS on israel_people +5 in count (exaction_barred, hand_shutting_barred, base_thought_barred, empty_sending_barred,
firstling_work_and_shearing_barred; holy_things_in_the_gates_barred's second entry — the literals counting the blocks grepped); the reuses' counts ONE ->
TWO where the running world holds ONE (blessings_for_hearing, cry_heard, bears_sin, holy_things_in_the_gates_barred — their counts on the running world READ
at the design's probes, the tuples in readback_probes.py and the D series' literals retyped from the print BEFORE the tape); the scene's tuple PREDICTED BY
SCRIPT at the runner step (the exam's persons through release_firstborn_case — each written once; the case world's own timer for the six-year term by call
into mishpatim's clock, fired in the case world alone; the severance gift's debit and its close at the sending in the case world); the narrative's (its own
world: the writes, 0 closes, the entity israel, the counter's day (11, 1), no row).

THE CHECKPOINTS DG1-DG9 (the D series at its seventh name; the literals typed from the prints at RUN B):
DG1 THE LINES — four events on the tape AFTER the tape's last Deuteronomy 14 line: release_law_declared, hand_opening_commanded, hebrew_slave_law_declared
and firstling_law_declared on the counter's day (40, 11, 1), NO marker (markers 172 UNMOVED); the counter ends at (40, 11, 1).
DG2 THE WRITES — debt_release_owed ONE, exaction_barred ONE, hand_opening_commanded ONE, hand_shutting_barred ONE, base_thought_barred ONE,
furnishing_commanded ONE, empty_sending_barred ONE, firstling_sanctification_commanded ONE, firstling_work_and_shearing_barred ONE on israel_people;
work_of_the_hand_blessed TWO (15:10's and 15:18's — or THREE with 14:29's if the registry holds it); blessings_for_hearing, cry_heard, bears_sin and
holy_things_in_the_gates_barred each ONE MORE than the running world held before the lines (the before-count read, never typed); law_release_firstborn
registered, given_at Deut 15:1, installed_by boot; the eight cells WRAPPED.
DG3 THE READBACK — the_readback's rows (the census from the print), every reference row's entry FOUND: the tape lines by kind and first verse (the release
demanded and closed Exod 5:1 / 12:31, first_offerings_brought Gen 4:4, decree_of_the_sojourn Gen 15:13, profane_slaughter_permitted Deut 12:15,
second_paragraph_declared Deut 11:13, third_year_tithe_declared Deut 14:28) and the kin's cells by CALL (each returning its verdict on its own ask — the term
clock, the maidservant's exits, the loan's obligation and the ladder, the severance price, the firstling's consecration and window, 27:26's bar, the blemish
list, the blemished in the gates, the blood like water); THE POINTER ROW with its referent AHEAD (15:6 → 28:3) graded H — the readback's first; the open
DISAGREES rows 2 (15:17, 15:19), OPEN; no retrograde row; the state row (the_needy_condition) present.
DG4 THE HOLES — NO effect naming the release of debts, the exaction, the hand opened or shut, the base thought, the furnishing, the empty sending, the
firstling's sanctification or its work and shearing on israel_people BEFORE this daemon's lines (the ledger scan on the running world at the tape's Deut 14
end: EMPTY — asserted before the lines run) and ONE each after; the reuses' counts +1 each; the five new kinds absent from both registries at sitting 13's
tree (asserted on the registry files); the twelve new effects absent from the effects registry before the types step.
DG5 THE KIN STAND — the six-year term by CALL (mishpatim's F1: goes_free due six years on; mishpatim_3's the_two_exits), the released's jubilee override by
CALL (yovel: jubilee_release on file), the cycle by CALL (yovel.cycle — the seventh year's class sabbath_of_the_land; the count "no count" on the bare world
before the entry), the sabbatical by CALL (calendar.sabbatical home_engine -> yovel), the loan's obligation and the priority ladder by CALL (ordinances.loan
— the cell naming 15:8), the pledge's sunset by CALL, the severance gift's price by CALL (erection.repeats), the firstling's consecration from the womb by
CALL (ordinances.firstling, korach.the_gifts opens_the_womb) and its eating window and eaters by CALL (korach.the_gifts), 27:26's bar by CALL
(temurah.consecrate), the herd's tithe by CALL (temurah.tithe), the blemish list by CALL (priesthood.acceptable firstling_table), the blemished in the gates,
the unclean and the clean, the blood like water by CALL (place_name), the covering by CALL (sanctions.covering), the poor defined and the hireling's wage by
CALL (holiness.gifts, holiness.wage), the four at the gate and the year passed by CALL (food_tithe), Belial's two seats by CALL (seducers — the labeled
transfer), the leper's ear by CALL (metzora — the labeled transfer), 5:15 by CALL (covenant_at_horeb), the second paragraph's conditional by CALL
(blessing_and_curse); interest_barred, land_release, sabbath_debt, jubilee_release, goes_out_in_the_jubilee, consecrated_firstborn, released,
pledge_returned_by_sunset, wage_due_by_morning — their counts on the running world UNMOVED (read at the probes, never typed); the open debits on
israel_people 10 UNMOVED.
DG6 THE PARAMETERS AND THE CLOCK — the twenty-seven parameter rows on file (calendar_parameters.yaml for the two clock data in the sojourn_start form; the
runner's DATA for the rest), the count from the registry's print at the types step; THE RELEASE'S DATE READ FROM THE CYCLE BY CALL (yovel — the seventh
year's end; the bare world before the entry: the count not begun, the cell's verdict "no count" asserted; the running world's count read through
year_in and printed — the date's rendering the clock's, never a constant); THE FIRSTLING'S YEAR a clock datum with its two-day edge (the case world's
firstling born at a day, its window twelve months by the clock's after(12, 'month') or year_in — the form read at RUN B from the clock's own methods); no
marker.
DG7 THE REGISTER AND THE EDGES — NO register seat at Deut 15 (the finder called on the chapter at the tape — the reading's measurement repeated; THE
FINDER'S FORMS read: "commanded" 6680 for a receipt, "these" 428 + a footer noun for a header — 15:2's "this is the word of" and 15:6's "as He spoke" each
outside by one token: the DATA row the_registers_two_near_misses); DECLARED 98 UNMOVED; the CALL edges on file as the census filed them (the file read at the
gates), the two TRANSFER edges labeled with their teachers, no HYPOTHESIS edge; the homographs FALSE if matched ('the-servant', 'the-place', 'the-flock');
no pointer.
DG8 THE DATA — the twin laws diffed on the DB (15:12 against Exodus 21:2 three in order and Jeremiah 34:14 seven; 15:16-17 against Exodus 21:5-6, one token
of the awl's verse; 15:15 against 5:15 eleven and 24:18 fourteen; 15:5 against 28:1 fourteen; 15:6 against 28:12; 15:22-23 against 12:15-16 and 12:22-24;
15:9 against 24:15 seven; 15:4 against 15:11 three; 15:14 NO KIN); the four number verses (15:1 [7], 15:7 [1], 15:12 [6], 15:18 [6]) and the ordinal 15:9 [7];
the eight infinitive absolutes; the one narrative verb 15:15; the homograph of Moses' name at 15:2 by lemma (4874 against 4872); the Aramaic's "a son of
Israel or a daughter of Israel" at 15:12, "the master of the claim" at 15:2, the Memra's three seats (15:5, 9, 11), "two for one" at 15:18; THE NFKC
MEASURE (0 presentation-form letters in 956 rows; 0 of 27 literals move; chapter 14's 29 verses unmoved) — every one by CALL to the ink block.
DG9 THE REST — entities 319 UNMOVED, closes 127, markers 172, the population table 148 UNMOVED, the four statute kinds present on the tape; the other counts
12b's exactly with the four lines and the writes dropped (THE REST test — NO declared delta). THE STALE LITERALS predicted (grepped at the design's probes
step): the D-series entries counting the reused effects (DC's blessings_for_hearing, DD's holy_things_in_the_gates_barred, the Exodus series' cry_heard and
bears_sin if any count them ONE), the readback tuples Q29 / Q32 / Q38 where a reused effect's count sits in the tuple, the checkpoints counting the blocks
on israel_people (if any); every miss shown at once by checkpoint_check.py --all AFTER the tape.

THE PROBES (RUN B's FIRST step, before the types — 7b's lesson 2): readback_probes.py Q40-Q42 written to FAIL before the runner exists (patch_probes_ch15.py
from patch_probes_ch14.py's form) — Q40 the runner and its the_readback table (the rows and their census typed from the print; every reference row's entry
found; the pointer row's referent ahead graded H; the two DISAGREES rows open; no retrograde row; the state row); Q41 the four own-day lines on the counter's
day (40, 11, 1) with NO marker (markers 172 UNMOVED) and their writes (the nine new ONE each on israel_people; work_of_the_hand_blessed's count; the four
reuses +1 each); Q42 the kin standing (DG5's counts) and the holes filled (DG4, DG6 — the release's "no count" on the bare world, the firstling's year by the
clock); the stale literals of DG9 retyped from the print BEFORE the tape.

THE DOCKET — THE UNION RULE ON THE TESTING SHELF, computed by the scan (ch15_docket_scan.out; the dump ch15_docket_dump.txt 636,267 bytes, 2,927 lines; the
header ROWS 975 LINK 118 TOPIC 857 CREDITED 249): THE LINK ROWS 118 in 29 works — Kiddushin 27, Bekhorot 24, Bava Metzia 6, Ketubot 6, Arakhin 5, Chullin 5,
Gittin 5, Makkot 4, Shabbat 4, Sanhedrin 3, Shevuot 3, Tosefta Peah 3, then Bava Batra, Bava Kamma, Mishnah Bekhorot, Taanit, Temurah and Yevamot 2 each, and
eleven works with one (Berakhot, Mishnah Arakhin, Mishnah Sheviit, Moed Katan, Nazir, Nedarim, Niddah, Sotah, Tosefta Bekhorot, Tosefta Demai, Tosefta
Sheviit); THE VERSES CITED 15:19 the most (22 rows), 15:2 (14), 15:9 and 15:22 (10 each), 15:14 and 15:16 (9), 15:17 and 15:20 (7), 15:8 and 15:11 (6),
15:4, 15:10 and 15:21 (5), 15:13 (4), 15:1, 15:7, 15:12 and 15:18 (3), 15:23 (2), 15:3, 15:5 and 15:6 (1) — 15:15 THE ONE VERSE NO ONE CITES (the memory
verse — the readback's VERBATIM row with 5:15); THE TOPIC ROWS by address 857 — the eleven folio ranges (Gittin 36a-37b 64, 4 link; Arakhin 32b-33a 39;
Makkot 3b 17, 2 link; Rosh Hashanah 8b-9a 20; Kiddushin 14b-22b 305, 24 link; Bava Metzia 31b 15, 4 link; 71a 20; Ketubot 67b 18, 2 link; Bekhorot 25a-28b 121,
4 link; 33a-37b 189, 6 link; 53b 17), the forty-six Mishnah rows (Sheviit 10 whole 9 — 1 link; Kiddushin 1:2-3; Peah 8:7-9; Bekhorot 1:1-2, 2:6-9, 3:3-4,
4:1-2, 5:1-6 — 16, 2 link — and 6 whole 12; Temurah 3:5; Arakhin 8:7 — 1 link; Shekalim 5:6; Chullin 2:9), the four Tosefta chapters (Sheviit 8: 12 rows,
Kiddushin 1: 11, Bekhorot 1: 6 and 2: 7 — the dict-text export read under its empty key); THE PRIOR READS 249 addresses credited — by ledger deu_14's exam 75,
EXOD_TALMUD_TRIAGE 57, deu_12's exam 48, the priesthood docket 17, the korach exam 16, the persons ledger 13, the sheviit docket 10, the ordinances docket 7,
deu_13's exam 6, the calendar and the Genesis triage 5 each, the erection, family and backfill 4 each, the code hunt 3 — per range Kiddushin 56, Bekhorot
33a-37b 89, 53b 17 whole, 25a-28b 8, Rosh Hashanah 7, Ketubot 4, Bava Metzia 3 + 1, Arakhin 2, Gittin 1, Makkot 0; THIRTY-EIGHT MISHNAH ROWS CREDITED
(Sheviit 10 whole, Bekhorot 6 whole and 1:1-2, 2:6, 2:9, 4:1-2, 5:1-2, Kiddushin 1:2-3, Peah 8:7-9, Arakhin 8:7, Shekalim 5:6, Chullin 2:9, Temurah 3:5) —
every one CARRIED with its ledger's verdict line and, where the ledger's form carried no verdict, READ WHOLE HERE (12b's form); the Sifra on Leviticus 25
credited from its sitting (behar_exam_mishnah, the sheviit docket); THE SPLIT: D1 THE SMALL WORKS (every address outside the two long ranges — 575 by the
scan's counts, the credited among them carried) and D2 THE TWO LONG RANGES (Kiddushin 14b-22b and Bekhorot 25a-28b with their own link rows — 456 by the
scan's counts, 64 credited), the exact counts computed from the dump by the parts' common file at each run, never typed; a 700-plus run split again at its
own clean point.

THE ORDER: this design -> the state doc's checkpoint (#207 — RUN A closed) -> THE DOCKET IN TWO RUNS: D1 the small works (the link rows of the twenty-seven
other works, the forty-six Mishnah rows, the four Tosefta chapters, Gittin 36a-37b, Arakhin 32b-33a, Makkot 3b, Rosh Hashanah 8b-9a, Bava Metzia 31b and 71a,
Ketubot 67b, Bekhorot 33a-37b and 53b) — the credited CARRIED with their ledgers' own verdict lines (12b's form, ch14_credit_carry.py derived), the uncredited
read whole in chunk files (the cap 64,000 bytes — one chunk one Read page), the parts on 12b's whole-row instruments (ch14_docket_A.py's form,
ch14_docket_common.py, the U file for the unresolved rows), EVERY ROW WHOLE, the verdicts LAW / DERIVATION / DISPUTE / CONTEXT / OUTSIDE with the credits
computed, its own clean point; D2 Kiddushin 14b-22b whole, THE CLEAN POINT after it UNCONDITIONALLY, then Bekhorot 25a-28b whole — the writer derived from
write_ch14_docket.py (the eleven ranges ASSERTED against the scan's print), the docket's records (COMPILE_DEBT's box (o), MIDDOT — every code checked in
MIDDOT.md before it is typed, MISHNAH_TOPICS, the state doc's checkpoint), its own clean point -> RUN B: the probes to FAIL (patch_probes_ch15.py: Q40-Q42;
the reuse literals retyped from the running world's print), the types (add_types_ch15.py — the docket's names; the twenty-seven parameters; the twelve
effects; the five kinds), the callees' facts printed before any assert (ch15_callees.py — every CALL named above, each ask read at the cell's own source),
the runner in parts with the fast checker (ch15_fastcheck.py) and the generated CASES (ch15_cases_gen.py; the guard's count from the generator's print),
the recorder (seq_record_ch15.py, INK_CACHE=0) and the stitcher (seq_stitch_ch15.py; no marker — the four lines on the counter's day), the literals DG1-DG9
and the VERDICTS entries (patch_seq_literals_ch15.py), the tape to 10/10 with THE REST, checkpoint_check.py --all AFTER the tape, the records writer
(write_ch15b_records.py) and the copier WRITTEN, gates_chain.sh LAUNCHED in the background, the clean point -> THE TAIL: the summary read once, the demands
filed (a rerun --from the step), the records from the sheet in one call (the map's AS BUILT with sitting 13's lesson 4 CORRECTED, COMPILE_DEBT's sitting-13
box PAID and the 13b box, the reading's ledger's CORRECTION row appended, MIDDOT, MISHNAH_TOPICS, RESEARCH_LOG, THE_STEPS, THE_BRIEFING, THE_LOOP's step-6
row, RESUME, RECORD_FORMS, the state doc, the addenda, the recovery page, the memory), the forms copied (copy_ch15b_forms.py), the commit message (this
sitting's alone, for the owner's word).
'''
assert not re.search(r'/Users/(?!Shared/)', SEC) and os.path.expanduser('~') not in SEC
assert not re.search(r'[֐-׿]', SEC), 'Hebrew script in the design — the map lints at 0'
open(P, 'a', encoding='utf-8').write(SEC)
print('appended', len(SEC.encode()), 'bytes to the map;', sum(1 for _ in open(P, encoding='utf-8')), 'lines now')
