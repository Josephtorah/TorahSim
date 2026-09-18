import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE DEUTERONOMY WALK sitting 5b — THE COMPILE OF CHAPTER 7 (2026-09-18; the owner: "Go" after sitting 5's run 4): THE DESIGN written into the map
# at the close of RUN 1 of four (the rereads, the measurements — ch7_compile_recon.py, ch7_docket_scan.py, the one database queried here — and this
# section, BEFORE any code), with the state doc's checkpoint (#194 addendum 4) naming RUN 2's first step, the recovery page's line, the memory note and
# the index line. Every number typed from the two instruments' prints of this run or computed here from the one database; the caps asserted before any
# file is opened; --check prints the plan only. Sitting 4b's form (write_ch6b_design.py).
import os, re, subprocess, sys, sqlite3
ROOT = _ROOT
MEM = os.path.expanduser('~/.claude/projects/-Users-Shared-TorahSim/memory')
SP = os.path.dirname(os.path.abspath(__file__))
CHECK = '--check' in sys.argv
def rd(p): return open(p, encoding='utf-8').read()
R = rd(f'{SP}/ch7_recon.out'); S = rd(f'{SP}/ch7_scan.out')
assert "FREE prefixes: ['CQ', 'CU']" in R and 'LINK rows 52 in 19 works' in S and 'Avodah_Zarah              42a-54b     465 rows,  11 link rows' in S and 'PRIOR READS (credited): 89 addresses of 682' in S
assert 'RUN (1304, 96, 88, 0, 12, 1595, 37, 319' in R and 'NEWEST_RUNNER hear_o_israel' in R and "I5 expects: ['66']" in R and 'pointers naming Deut 7: []; edges naming Deut 7: []' in R and 'DAEMON_ORDER 66' in R
assert 'kinds 1125, effects 1025' in R and "PLACEMENT {'markers': {'text_constrained': 106, 'reading_placed': 46}, 'events': {'text_constrained': 109, 'page_order': 1140, 'reading_placed': 55}}" in R
assert 'CENSUS (2487, 1313, 1304, 1158, 6, 10, 9, 0, 71, 167, 129, 15, 23, 849, 272)' in R and 'TOPIC rows 630' in S and 'the verses NOT cited by anyone: [1, 6, 8, 12, 17, 18, 19, 21, 22, 23, 24]' in S
# THE ONE DATABASE — the kin's effects on the running world (presence by effect and entity; the rows accumulate over the recorded runs, so presence is the fact)
db = sqlite3.connect(f'file:{ROOT}/World/journal/data/world.sqlite?mode=ro', uri=True)
def present(effect, entity=None):
    q = "SELECT COUNT(*), COALESCE(SUM(open), 0) FROM run_ledger WHERE effect=?" + (" AND entity=?" if entity else '')
    n, o = db.execute(q, (effect, entity) if entity else (effect,)).fetchone(); return n, o
P_COV = present('covenant_barred'); P_INT = present('intermarriage_barred'); P_DRV = present('nations_driven_out'); P_TRE = present('treasured_people', 'israel_people')
P_OTH = present('other_gods_barred', 'israel_people'); P_COV10 = present('coveting_barred', 'israel_people'); P_SHM = present('shema_commanded', 'israel_people'); P_HPB = present('high_places_banned')
DISP = db.execute("SELECT effect, entity, value, open, verse FROM run_ledger WHERE effect='commanded' AND (verse LIKE 'Num 33:5%' OR source LIKE 'Num 33:5%' OR value LIKE '%dispossess%')").fetchall()
assert P_COV[0] == 0 and P_INT[0] == 0 and P_DRV[0] == 0 and P_TRE[0] > 0 and P_OTH[0] > 0 and P_COV10[0] > 0 and P_SHM[0] > 0 and P_HPB[0] > 0, (P_COV, P_INT, P_DRV, P_TRE, P_OTH, P_COV10, P_SHM, P_HPB)
DISP_TXT = (f"the journeys' dispossession debits FOUND on the world — commanded on israel_people valued {sorted(set(str(d[2]) for d in DISP))}, {'OPEN' if all(d[3] for d in DISP) else 'some CLOSED'} (Num 33:50-56)" if DISP else "the journeys' dispossession debit NOT FOUND by the effect 'commanded' at a Num 33:5x verse — its daemon watches dispossession_commanded → ['commanded']; the runner's fast checker reads the row by its own key at run 3 (a measurement owed, not a fact typed)")
print('THE WORLD:', dict(covenant_barred=P_COV, intermarriage_barred=P_INT, nations_driven_out=P_DRV, treasured_people=P_TRE, other_gods_barred=P_OTH, coveting_barred=P_COV10, shema_commanded=P_SHM, high_places_banned=P_HPB, dispossession=DISP[:2]))
DATE = '2026-09-18'
DESIGN = f'''

## Sitting 5b — THE COMPILE OF CHAPTER 7, Deuteronomy 7:1-26 ({DATE}; the owner: "Go" after sitting 5's run 4): THE DESIGN — written at the close of
## RUN 1 of four (the rereads: THE_STEPS' compiler block and Step 5's head (this window), the 5b box (a)-(p), the 4b design and AS BUILT as the compile's
## form; the measurements: ch7_compile_recon.py, ch7_docket_scan.py in the scratchpad, the one database queried) and BEFORE any code; the four-run rule's
## fourth sitting, every row of the docket WHOLE under THE WHOLE-ROW RULE

THE FOUR RUNS: RUN 1 the rereads, the measurements and this design — CLOSED HERE, a clean compaction point (#194 addendum 4); RUN 2 the probes to FAIL
(readback Q16-Q18), then THE DOCKET by the union rule, EVERY ROW WHOLE (four parts A-D on 4b's whole-row instruments, the writer write_ch7_docket.py,
coverage computed) — the docket takes the runs it needs; RUN 3 the types by script, the recorder and the stitcher, the gates to FAIL, the runner in parts
with the fast checker and the generated CASES, the literals CQ1-CQ9, checkpoint_check.py --all AFTER the tape (the tape grows), the tape to 10/10 with
THE REST; RUN 4 gates_chain.sh in one summary, the records from the sheet in one call, the forms copied, this section's AS BUILT.

THE MEASUREMENTS (what the tape, the runners, the registries and the one database say before a line is typed): THE COUNTER stands at (40, 11, 1); the
tape's LAST LINES are chapter 6's two (shema_declared 6:4-9, testing_barred 6:16-19, both on the counter's day, no marker) and its LAST MARKER the
forward one at Deut 5:32 (M['charge']) — CHAPTER 7 OPENS ON THE COUNTER'S OWN DAY, NO MARKER, the speech continuing. THE CHAPTER'S KIN IS ON THE TAPE
AND IN THE CODE: the angel's clauses (Exodus 23:20-33) are ordinances.land — its asks hornet, little_by_little, no_barren, no_covenant, not_dwell (the
snare), break_pillars, bread_water, serve_before, angel, borders, not_forgive (the recon's section 2); the renewed covenant (34:10-16) is erection.covenant
— its asks nations_seven_orders, no_covenant_by_call, daughters_two_seats, intermarriage_channels, child_follows_mother (Kiddushin 68b's rule already
there), cut_four, pillars_exod, molten_two_seats, demolition_first_seat, demolition_grows, sheet_az_2_3 / 3_5 / 4_2 / 4_4 (Mishnah Avodah Zarah's rows
graded at the erection docket); the dispossession (Numbers 33:50-56) is journeys.the_command — drive_out, figured_stones, molten_images, high_places,
three_objects_own, negative_arm, when_you_pass, possess_and_dwell; the second word and the tenth are covenant_at_horeb.the_second_word (no_other_gods,
the_visiting — "to thousands", "those who hate Me") and the_tenth_word (covet_and_desire, the_coveter_who_pays, the_wife_first); the plagues, the sea,
Marah's healer, the trials, Amalek's blotting and the treasure at 19:5-6 are exodus_story (plagues, sea, marah(healer_condition), trials(ten_list,
count_by_exodus), amalek(blotting), sinai(treasure_seats)); 4:34's trials, 4:37's "because He loved your fathers" and 4:35/39's "He is God" are
obey_horeb.the_one_god (because_he_loved_your_fathers, to_dispossess_nations, you_were_shown); 1:28's fear is opening_speech.the_spies_read_back; Baal
Peor's whoring (Numbers 25:1-3 — the marriage law's exhibit) is balak.peor; Leviticus 11:43's detesting verb is shemini.classify. THE EFFECTS ALREADY IN
THE REGISTRY for the chapter's matter: covenant_barred (a BLOCK "on the people entering the land" — ordinances' case kind entered_the_land, Exodus
23:32-33), intermarriage_barred (a BLOCK "at the border" — erection's case kind daughters_taken, 34:16), nations_driven_out (a TRANSFER — 34:11),
treasured_people (a conditional HEAVEN entry — 19:5-6), other_gods_barred and coveting_barred (the two words' BLOCKS from 3b), high_places_banned (the
erection's BLOCK on the land), amalek_to_be_blotted (17:14), cherem_vowed (Hormah), destroyed (the sacrificer's ban); the case kinds daughters_taken,
sacrifice_of_inhabitant_eaten, entered_the_land, dispossession_case. THE ONE DATABASE READ (run_ledger): on the running world covenant_barred is ABSENT
(its case kind entered_the_land is Joshua's — never fired), intermarriage_barred ABSENT (the exam's case only), nations_driven_out ABSENT;
treasured_people PRESENT on Israel (a heaven entry, open), other_gods_barred and coveting_barred PRESENT (3b's lines), shema_commanded PRESENT (4b's),
high_places_banned PRESENT on the land; {DISP_TXT}. THE TAPE'S LINES THE CHAPTER RETELLS (every one FOUND by the recon's section 5): the ten
plague_struck lines with their closes (Exodus 7:20 to 12:29), sent_out, brought_out (12:51), sea_split, saved_at_the_sea, believed (14:21-31),
healer_promised (15:26), blotting_sworn (17:14-16 — Amalek; the phrase "from under heaven"), covenant_offered (19:5-6 — the treasure, the holy nation),
the oath's three lines (sworn_by_himself 22:16-18, oath_upheld 26:3-5, visitation_promised 50:24), covenant_cut_at_sinai (34:10 — the renewed covenant's
head), the Shittim lines (25:1-3 — the whoring after the daughters of Moab, the yoke to Baal Peor), dispossession_commanded (33:50-56), and the tape's own
DEVOTINGS — sihons_cities_devoted and ogs_cities_devoted (2:34, 3:6 — Israel's ban executed on the east before the ban's spec for the west), Hormah's
cherem_vowed (21:2-3). NO LINE OF THE CHAPTER'S OWN LAW IS ON THE TAPE: the cherem on the seven nations, "show them no favor", "your eye shall not
pity", the abomination into the house and the devoted thing have NO CELL anywhere (the recon's regex per def over all sixty-one runners: "favor" only
the loan's "gracious" and holiness' mrow; "pity" nowhere; "abomination" the shepherds' and Leviticus 18's land; "cherem/devoted" the vow's, the
sacrificer's, the temurah's devotings, Hormah's, Sihon's and Og's — none the seven nations' spec) — THE CODE'S FOUR HOLES, compiled here at the chapter's
own day. THE CHECKPOINT PREFIX measured FREE: CQ (CQ, CU free; neither a label elsewhere). THE GLOBAL COUNTS grepped before the tape run: markers 167
(F 129, R 23, P 15) UNMOVED — no marker this chapter; closes 127 UNMOVED — no close (the ban's debit OPEN to Joshua); entities 319 UNMOVED (Israel the
written-on party; the seven nations a counterparty string — no registry row for the-nations, the-hittite … the-jebusite; the-amorite alone has an entity,
Sihon's, untouched); daemons 66 → 67 (I5 66 → 67); kinds 1125 → 1129 (three tape kinds, one case kind), effects 1025 → 1029 (four new); CENSUS on tape
1304 → 1307, kinds 849 → 852; PLACEMENT events page_order 1140 → 1143 (the lines on the counter's day, no marker), markers unmoved; the positions table
235 → 244 checkpoints. THE REGISTER GATE: no receipt form in the chapter ("swore to your fathers" 7:8, 12, 13 are RUN_CITATION pointers, not receipts) —
DECLARED 100 unmoved, no seat.
THE DOCKET SIZED (ch7_docket_scan.py — the export's chapter 7 the DB's, no division map): 52 LINK rows in 19 works (Avodah Zarah 18, Kiddushin 5, Sotah 4,
Chullin 3, Mishnah Avodah Zarah 3, Tosefta Avodah Zarah 3, Eruvin 2, Shabbat 2, Temurah 2, Bava Kamma, Bava Metzia, Bekhorot, Berakhot, Makkot,
Pesachim, Sanhedrin, Tosefta Sotah, Tosefta Zavim, Yevamot one each); the verses cited 2, 3, 4, 5, 7, 9, 10, 11, 13, 14, 15, 16, 20, 25 (ten rows), 26
(seventeen) — ELEVEN VERSES CITED BY NO ONE (1, 6, 8, 12, 17-19, 21-24: the list, the reason, the fear and the promises — narrative and promise, not
law); + THE TOPIC RANGES SIZED: Mishnah Avodah Zarah 1:1-4:12 whole (38 rows, 24 CREDITED at the erection docket and the decalogue docket), Mishnah
Kiddushin 3:12; Avodah Zarah 20a-20b 31 rows, 36b-37a 34, 42a-54b 465 (40 credited, 11 link rows); Kiddushin 68b 10; Yevamot 23a 14; Sotah 35b-36a 27
(8 credited); Chullin 89a 16 (6 credited); Makkot 22a 16 — THE DESIGN DECLARES: every range whole EXCEPT Avodah Zarah 42a-54b, of which the
VERSE-ANCHORED amudim are read whole — 42a-42b (41: the mishna on an idol's fragments — 7:25-26's abomination into the house), 44b-46b (70: the
mountains and hills worshipped, the Asherah, "the graven images of their gods" — 7:5, 7:25; 46a's renaming, the Sifrei 61:7's kin), 47b-48b (53: the
Asherah's wood and shade; the house adjacent to the idol's — Mishnah 3:6), 49b (21: the Asherah's wood — Makkot 22a's lashes), 51b-52b (66: the money
and ornaments on the idol — 7:25 read by R. Akiva and R. Yishmael; the nullification 4:4-5), 53b-54b (52: Ahaz's vessels, the exchange's exchange —
7:26) — 303 rows; the remainder 43a-44a (57 — the heavenly bodies' images, chapter 4's matter), 47a (22 — bestiality, chapter 27's), 49a (19 — orlah,
Leviticus 19's), 50a-51a (48 — Markulis, the offerings to idols; the erection docket's kin), 53a (16 — partnership) ENUMERATED and marked outside
declared scope (Step 2's standing rule; the scan's count the enumeration): the docket near 540 rows (52 + 39 + 148 + 303), some 90 credited (89
addresses found — some in the enumerated part), in FOUR parts A-D, EVERY ROW WHOLE — the four-run rule's docket takes the runs it needs. THE CHAPTER'S
OWN INK (the reading's 119 asserts, reused in the runner): two number verses (7:1 [7] with the seven gentilic tokens as its witness — the Bible's three
seven-name lists and eleven six-name lists carry no numeral; 7:9 [1000] against the ten words' bare "to thousands"), no gap; the oath's noun starred;
no divine frame, no "saying", two narrative verbs (7:7 "and He chose", 7:8 "and He redeemed you"), five infinitive absolutes, sixteen prohibitions
(eleven second person, five third), plural at 7:5 and 7:7 only; the written/read pair at 7:9 (the store's extra token — kept out of every check); the
phrase censuses (the design of sitting 5): "seven nations" one seat, "you shall not covet" 7:25 and Exodus 20:17, "little by little" 7:22 and Exodus
23:30, the hornet's three seats, "no man shall stand before you" 7:24 and Joshua 1:5, "an abomination to the LORD your God" the book's five.

THE NAME: cold_run_seven_nations.py — the 62nd runner ("seven nations", 7:1); law_seven_nations the 67th daemon (given_at Deut 7:1 — the ban's first and
only giving, the chapter's own line; installed_by boot — the three Deuteronomy daemons' form); the span [[Deut, 7, 1, 26]]; the checkpoints CQ1-CQ9; the
unit deu_07_nations_cherem the frozen reading.

THE READBACK ON THIS CHAPTER — THE CODE RE-DECLARED FOR THE LAND (the laws' form (L1)-(L6) of 3b, run for the first time on a chapter that re-says
ANOTHER chapter's law rather than its own copy: the row's first telling is a KIN CELL — Exodus 23's, 34's, Numbers 33's, the two words' — or a tape line;
the retelling's rows are REFERENCE ROWS graded against the cell's verdict by CALL or the tape's entry by kind and verse, never a second write; what has
no first telling is THE CODE'S HOLE, compiled here). THE ROWS (twenty-one predicted; the grades' census typed from the runner's print at run 3): 7:1 the
seven-name list — against ordinances.land's 23:23 and erection.covenant's 34:11 (six names each): EXPANDED (the Girgashite; the count); 7:1 "clears
away" — against journeys.the_command's 33:52 "you shall drive out": VARIANT (the verb); 7:2 "you shall make no covenant with them" — against 23:32
(ordinances.land no_covenant; 34:12, 15 "lest"): VERBATIM in kind; 7:3 no intermarriage BOTH WAYS — against 34:16 (erection.covenant daughters_two_seats
— one direction): EXPANDED; 7:4 the reason (he will turn your son) — against 34:16's "whore after their gods … make your sons whore": VARIANT (the
tape's Shittim lines the exhibit — a DATA note); 7:5 the four objects — against 34:13's three (cut_four) and 33:52's three (three_objects_own): EXPANDED
(the images burned); 7:6 holy people, chosen, treasure — against covenant_offered (19:5-6, the tape's line; exodus_story.sinai treasure_seats) and
4:37's "chose" (obey_horeb): EXPANDED; 7:8 the oath, "brought you out with a strong hand", "redeemed you" — against brought_out (12:51) and the oath's
three lines: EXPANDED (as 6:21-23); 7:9 "to a thousand generations, those who love Him" — against the second word's clause (5:10 / Exodus 20:6;
covenant_at_horeb.the_second_word the_visiting): VARIANT ([1000] for the bare plural; the third person for the first); 7:10 the hater repaid to his own
face — against 5:9 / 34:7 "visiting the fathers' iniquity on the sons": TURNED (the recipient; Onkelos's doctrine a DATA note); 7:11 the triad — against
stand_here_commanded (5:31) and 6:1 (hear_o_israel.the_header the_triad): VERBATIM in kind; 7:12 "because you hear … He will keep the covenant" —
against covenant_offered's condition (19:5 "if you will hear My voice and keep My covenant"): VARIANT; 7:13-15 the blessing's list, no barrenness, the
sickness removed — against 23:25-26 (ordinances.land bread_water, no_barren): EXPANDED (the fruit, the grain, the increase and the young); 7:14 "there
shall not be a barren" — against 23:26: VERBATIM in kind; 7:15 the diseases of Egypt not put on you but on those who hate you — against healer_promised
(15:26): TURNED (the diseases redirected); 7:16 not serve their gods, a snare — against 23:33 (ordinances.land not_dwell): VARIANT; 7:18-19 what He did
to Pharaoh, the trials, the signs and wonders, the hand and the arm — against the ten plague_struck lines, sea_split, saved_at_the_sea (and 4:34's list,
obey_horeb): SHORTENED; 7:20 the hornet — against 23:28 (ordinances.land hornet): EXPANDED ("those who remain and hide"); 7:22 little by little, the
beasts of the field — against 23:29-30 (little_by_little): VERBATIM in kind; 7:23-24 the confusion, the kings, the name from under heaven, no man shall
stand — against 23:27 ("My terror … confusion") and 23:31 ("the inhabitants into your hand"): EXPANDED (the kings; the name — blotting_sworn's phrase);
7:25 "you shall not covet" the idols' silver and gold — against the tenth word (covenant_at_horeb.the_tenth_word covet_and_desire): TURNED (the object
— the neighbor's house to the idols' silver and gold). THE CENSUS PREDICTED: VERBATIM 4 / VARIANT 5 / EXPANDED 8 / TURNED 3 / SHORTENED 1 — twenty-one
rows; no row OPEN. THE CODE'S FOUR HOLES (no first telling in any cell): THE BAN on the seven nations (7:2 "you shall utterly destroy them" — Exodus 23
says cut off and drive out, Numbers 33 dispossess; the tape's own devotings of Sihon and Og and Hormah's vow are RUNS before the spec; 20:16-18's cell
OWED forward), NO FAVOR (7:2 — Avodah Zarah 20a's three readings), NO PITY (7:16 — the book's five seats, this the first), THE ABOMINATION INTO THE
HOUSE AND THE DEVOTED THING (7:25-26 — Mishnah Avodah Zarah 1:8-9, 3:6; Makkot 22a; Avodah Zarah 54b) — compiled here, their writes at the chapter's
own day. THE INSTALL HYPOTHESIS (on the table) is TESTED IN PASSING and not ruled: the seventh exhibit's rows are graded here as the laws' readback —
the code re-declared with the target's names — and nothing of the engine changes for the hypothesis.

THE DESIGN'S DECISIONS (the box's (a)-(p) settled on the measurements):
(a) THE BAN — F1's the_ban: the code's hole — the WRITE commanded valued devote_the_seven_nations, a DEBIT on Israel OPEN to Joshua (the run), at the
chapter's first line nations_devoted (7:1-5); the dispossession's two debits (journeys.the_command('drive_out') by CALL — dispossess_the_inhabitants_and_possess_the_land, destroy_their_images, both OPEN on the world) REFERENCED, not doubled; 20:16-18's
cell declared OWED FORWARD in the dispositions (the war chapter's runner) — the Sifrei's war sections unread; the tape's prior devotings (Sihon, Og,
Hormah) named in the cell's DATA row the_devotings as RUNS before the spec (the tent's reverse flow noted, not claimed).
(b) NO COVENANT AND NO FAVOR — F1's no_covenant: ordinances.land('no_covenant') by CALL (23:32) and erection.covenant('no_covenant_by_call') by CALL
(34:12, 15); the WRITE covenant_barred on Israel at nations_devoted — THE EFFECT'S FIRST TAPE WRITE (its case kind entered_the_land is Joshua's; the
Moab giving stands from here; when the entry fires at the run, the ordinances' daemon writes it again on its own case — a second write on a second act,
not a doubled law); F1's no_favor: the code's hole — the WRITE favor_barred (a BLOCK, NEW) with Avodah Zarah 20a's three readings as the exam's rows
(no settlement, no gift, no praise).
(c) NO MARRIAGE, BOTH DIRECTIONS — F1's no_marriage: erection.covenant('daughters_two_seats', 'intermarriage_channels', 'child_follows_mother') by
CALL (34:16 one direction; Kiddushin 68b's rule already in that cell); the WRITE intermarriage_barred on Israel at nations_devoted, valued both
directions — THE EFFECT'S FIRST TAPE WRITE (the exam's case daughters_taken until now); Mishnah Kiddushin 3:12, Yevamot 23a, Avodah Zarah 36b the
exam's rows; 7:4's reason a VARIANT row with the Shittim lines as the tape's exhibit (balak.peor by CALL for the DATA).
(d) THE ALTARS, THE PILLARS, THE ASHERIM, THE IMAGES — F1's the_four_objects: erection.covenant('cut_four', 'pillars_exod') and journeys.the_command
('figured_stones', 'molten_images', 'high_places') by CALL; the demolition a REFERENCE row against journeys' OPEN debit destroy_their_images (33:52's three objects — no second debit, R1; the ban's debit
values the devoting alone); 12:3's fuller form forward; the Sifrei 61:7's renaming for the worse a DATA row the_renaming (Avodah Zarah 46a the
exam's row); Mishnah Avodah Zarah 3:5-10 CREDITED (the erection docket).
(e) THE CHOSEN PEOPLE — F2 the_holy_people: exodus_story.sinai('treasure_seats') by CALL (19:5-6; treasured_people on the world a heaven entry — CQ5
unmoved), obey_horeb.the_one_god('because_he_loved_your_fathers') by CALL (4:37); Chullin 89a's "not because you were more" the exam's row; no write
(the readback's rows 7:6, 7:8).
(f) THE FAITHFUL GOD AND THE HATER REPAID — F3 the_faithful_god: covenant_at_horeb.the_second_word('the_visiting') by CALL ("to thousands", "those who
hate Me" — 5:9-10); the rows 7:9 VARIANT, 7:10 TURNED; Onkelos's doctrine of the wicked paid in this world a DATA row the_supplied_doctrine (Eruvin
22a's reading the exam's row); Shabbat 10b's "the faithful God" in the bathroom the exam's row; the triad 7:11 by CALL to hear_o_israel.the_header
('the_triad'); the written/read pair at 7:9 a DATA row the_written_read_pair; no write.
(g) "BECAUSE YOU HEAR" AND THE BLESSINGS — F4 because_you_hear: the WRITE blessing_promised — a conditional HEAVEN entry on Israel (NEW; the form of
treasured_people) at the chapter's second line hearing_blessed (7:12-16); the conjunction "because" (the heel) a DATA row the_heel (the five seats);
ordinances.land('bread_water', 'no_barren') by CALL (23:25-26); exodus_story.marah('healer_condition') by CALL (15:26 — the row 7:15 TURNED); 28:4, 11,
18, 51, 60 forward (the blessings and the curses); Bekhorot 44b, Bava Metzia 107b, Berakhot 51b, Chullin 84b the exam's rows.
(h) NO PITY AND NO SERVING — F4's consume_no_pity: the code's hole — the WRITE pity_barred (a BLOCK, NEW) at hearing_blessed ("your eye shall not pity"
the book's five seats, 13:9, 19:13, 19:21, 25:12 forward); F4's no_serving_snare: covenant_at_horeb.the_second_word('no_other_gods') by CALL
(other_gods_barred stands — CQ5) and ordinances.land('not_dwell') by CALL (23:33's snare); Bava Kamma 113b's "consume" the exam's row.
(i) DO NOT FEAR — F5 do_not_fear: NO LINE, NO WRITE — 7:17-24 is promise and exhortation whose law seat is the war chapter's (20:1-4, 20:8 — the
officers' proclamation), declared OWED FORWARD; the cell's asks by CALL: opening_speech.the_spies_read_back (1:28's fear), exodus_story.plagues,
sea, trials('ten_list', 'count_by_exodus'), obey_horeb.the_one_god('you_were_shown') (4:34), ordinances.land('hornet', 'little_by_little')
(23:28-30), hear_o_israel.the_gift_and_the_warning('the_jealous_god') (6:15's Shekhinah pair), exodus_story.amalek('blotting') (17:14's phrase); the
rows 7:18-19 SHORTENED, 7:20 EXPANDED, 7:22 VERBATIM, 7:23-24 EXPANDED; Sotah 36a's hornet at the Jordan the exam's row (Joshua 24:12 the receipt, forward).
(j) LITTLE BY LITTLE — inside (i): ordinances.land('little_by_little') by CALL; the beasts of the field the reason kept whole; a RUN_CITATION pointer
at Deut 7:22 (the promise's seat 23:29-30, a law speech — the pointer names the cell, not a tape line).
(k) THE KINGS AND THE NAME — inside (i): the phrase "from under heaven" blotting_sworn's (17:14 — exodus_story.amalek by CALL); 25:19 forward; Joshua
1:5's "no man shall stand" the receipt, forward — a DATA row the_name_from_under_heaven.
(l) THE IDOLS' SILVER AND GOLD — F6 the_images_and_the_devoted: covenant_at_horeb.the_tenth_word('covet_and_desire') by CALL (coveting_barred stands —
CQ7; the row 7:25 TURNED); Mishnah Avodah Zarah 3:5 CREDITED, 4:4-5 the nullification; Avodah Zarah 51b-52b the exam's rows (R. Akiva / R. Yishmael on
"the graven images of their gods"); Achan's Joshua 7:21 the run's case, forward; no second write for the coveting.
(m) THE ABOMINATION INTO THE HOUSE AND THE DEVOTED THING — F6's into_your_house: the code's hole — the WRITE house_abomination_barred (a BLOCK, NEW) at
the chapter's third line abomination_barred (7:25-26); Mishnah Avodah Zarah 1:8-9 (the renting), 3:6 (the wall), Avodah Zarah 21a, 42a-42b, 54b (the
exchange's exchange), Kiddushin 58a, Temurah 30b, Chullin 140a, Makkot 22a and Pesachim 48a (the Asherah's wood flogged) the exam's rows; the devoted
thing's lemma against the ban's (7:2) a DATA row the_two_lemmas; shemini.classify by CALL for Leviticus 11:43's detesting verb (Avodah Zarah 47b and
Tosefta Zavim 5:6 — "idol worship is like a creeping thing" — the exam's rows).
(n) THE RUN CITATIONS — RUN_CITATION pointers: Deut 7:6 (covenant_offered 19:5-6), 7:8 / 7:12 / 7:13 (the oath's three lines — 6:10's form), 7:18 (the
plagues), 7:19 (the sea; 4:34's list), 7:22 (the promise's cell); every demand the census makes past the imports read on the DB and declared, never a
blanket row (4b's lesson: the design's pointer list is a prediction — the census decides).
(o) THE DOCKET by the union rule — the scan's 52 link rows + the Mishnah rows (39) + the ranges declared above (near 540 rows, some 90 credited) in
FOUR parts A-D — LAW / DERIVATION / DISPUTE / CONTEXT / OUTSIDE, EVERY ROW WHOLE; the crowns expected: "show them no favor" read three ways (20a); the
gentile's betrothal ineffective and the child follows the mother (Kiddushin 68b; 36b's decree); the Asherah defined — its shade, its wood, its trunk
(45b-48b), the renaming for the worse (46a — the Sifrei 61:7's kin); the money and ornaments on the idol, "the graven images of THEIR GODS" (51b-52b),
the nullification by a gentile (4:4-5); the exchange's exchange (54b); the house adjacent and the renting (Mishnah 1:8-9, 3:6; 21a); the Asherah's
wood flogged (Makkot 22a; Pesachim 48a); "not because you were more" (Chullin 89a); the hornet at the Jordan (Sotah 36a); arrogance as idolatry
(Sotah 4b-5a on 7:26 and 7:5); "today to do them, tomorrow to receive" (Avodah Zarah 3a, 4b; Eruvin 22a); the hater repaid (Eruvin 22a); the barren
and the sickness (Bekhorot 44b; Bava Metzia 107b); Daniel and the images (Sanhedrin 93a); stealing from a gentile (Bava Kamma 113b).
(p) THE FLOCK'S "YOUNG" TAGGED A NAME — a DATA row the_morph_tag (the four seats); no cell, no edge, the parser unaffected.

THE CELLS (six, each returning out(verdict, effects); the INK block exec'd from the sequence file; the token probes zero-report; every seat list typed
from the reading's print and the recon): F1 the_seven_nations (7:1-5 — asks: the_seven (the count and its witness; the three seven-name lists, the
eleven six-name; the Girgashite), the_ban (a), no_covenant (b), no_favor (b — the hole), no_marriage (c), the_four_objects (d); the writes commanded
valued devote_the_seven_nations, covenant_barred, favor_barred, intermarriage_barred); F2 the_holy_people (7:6-8 — asks: holy_people (14:2, 26:19;
19:6 by CALL), chose_you (4:37 by CALL), the_fewest (Chullin 89a — DATA), the_oath (the three lines by CALL — mamre, joseph, opening_speech; the
noun starred), brought_out_redeemed (the row 7:8)); F3 the_faithful_god (7:9-11 — asks: he_is_god (4:35, 39 by CALL), the_faithful (the one seat;
Shabbat 10b), thousand_generations (f — the row 7:9), the_hater_repaid (f — the row 7:10), the_triad (7:11 by CALL), the_written_read_pair (DATA)); F4
because_you_hear (7:12-16 — asks: the_heel (g — DATA), covenant_kept (g — the write blessing_promised), the_blessing_list (g), no_barren (23:26 by
CALL — the row 7:14), the_diseases (15:26 by CALL — the row 7:15), consume_no_pity (h — the write pity_barred), no_serving_snare (h)); F5 do_not_fear
(7:17-24 — asks: the_doubt (1:28 by CALL), remember_pharaoh (the rows 7:18-19), the_trials (4:34 by CALL), the_hornet (23:28 by CALL — the row 7:20),
in_your_midst (6:15 by CALL), little_by_little (j — the row 7:22), the_kings_and_the_name (k — the row 7:23-24); no write); F6 the_images_and_the_devoted
(7:25-26 — asks: burn_the_images (7:5's clause; 12:3 forward), not_covet_silver_gold (l — the row 7:25), lest_snared (23:33 by CALL — DATA),
abomination_to_the_lord (the book's eight seats — DATA), into_your_house (m — the write house_abomination_barred), devoted_like_it (m — the two
lemmas), utterly_detest (m — Leviticus 11:43 by CALL)). The readback table the_readback (the twenty-one rows and the four holes).

THE DATA ROWS (sixteen): the_readback, the_devotings (a — Sihon, Og, Hormah on the tape), the_three_readings_of_favor (b — 20a), the_shittim_exhibit (c —
the tape's 25:1-3 lines), the_renaming (d — 61:7; 46a), the_fewest (e — 89a), the_supplied_doctrine (f — Onkelos 7:10), the_written_read_pair (f), the_heel
(g — the five seats), the_blessing_list (g — 28's seats forward), the_name_from_under_heaven (k), the_two_lemmas (m — the ban's and the devoted thing's),
the_abomination_seats (the book's thirteen; the eight "to the LORD"), the_morph_tag (p), the_eleven_uncited (the scan's verses cited by no one), the_credits
(the erection docket's Mishnah Avodah Zarah rows — the addresses).

THE DAEMON law_seven_nations (given_at Deut 7:1; installed_by boot): watches nations_devoted → [commanded, covenant_barred, favor_barred,
intermarriage_barred]; hearing_blessed → [blessing_promised, pity_barred]; abomination_barred → [house_abomination_barred]; seven_nations_case →
[accepted, exempt, lashes]. No timer; literal W dicts per kind; the case kind dispatching to the cells by name in EXPLICIT branches.

THE TYPES (add_types_ch7.py from add_types_ch6.py): THREE tape kinds — nations_devoted (statute by form, 7:1-5; the seven names in the row; the
witnesses the verses), hearing_blessed (statute by form, 7:12-16; the blessing's condition and the two prohibitions), abomination_barred (statute by
form, 7:25-26) — ONE case kind (seven_nations_case); FOUR new effects — favor_barred (block on Israel; 7:2), pity_barred (block on Israel; 7:16),
blessing_promised (heaven on Israel, conditional; 7:12-15), house_abomination_barred (block on Israel; 7:26); the effects reused — commanded (the
ban's debit, valued devote_the_seven_nations), covenant_barred (23:32's, its first tape write), intermarriage_barred (34:16's, its first tape write),
accepted, exempt, lashes; NO registry row (Israel the written-on party; the seven nations a counterparty string); the daemon block; the functions block
seven_nations (the six cells WRAPPED); the span [[Deut, 7, 1, 26]]; the CALL edges by the ink — ordinances (the angel's clauses), erection (the renewed
covenant; the exam's credits), journeys (the dispossession; the three objects), covenant_at_horeb (the second word's visiting, the tenth word's
coveting, the charge's line for the triad), decalogue (20:5-6, 20:17 the first copies), exodus_story (the plagues, the sea, the healer, the trials, the
treasure, Amalek's phrase), obey_horeb (4:34-39), hear_o_israel (6:1's triad, 6:15's pair), opening_speech (1:28; 1:8's oath seats; the east's
devotings), mamre and joseph (the oath's lines), balak (the Shittim exhibit — DATA), shemini (Leviticus 11:43's verb); the pointers RUN_CITATION of (n);
every demand the census makes past the imports read on the DB and declared; I5 66 → 67.

THE TAPE (three lines, NO marker): under "# ---- Deut 7 ----" after the tape's last Deuteronomy 6 line: nations_devoted (7:1-5), hearing_blessed
(7:12-16), abomination_barred (7:25-26), all on the counter's own day (40, 11, 1), page_order. The markers 167 UNMOVED; the closes 127 UNMOVED (the
ban's debit OPEN); the counter ends at (40, 11, 1) UNMOVED.

THE CHECKPOINTS CQ1-CQ9 (the prefix measured free):
CQ1 THE LINES — three events of the sitting's kinds on the tape in the ink's order, all AFTER the tape's last Deuteronomy 6 line, all on the counter's day
(40, 11, 1), NO marker added (markers 167); the counter ends at (40, 11, 1).
CQ2 THE BAN — commanded on israel_people valued devote_the_seven_nations ONE, OPEN, source beginning "Deut 7:1"; law_seven_nations registered, given_at
Deut 7:1, installed_by boot; the functions block's six cells WRAPPED.
CQ3 THE BORDER BLOCKS — covenant_barred on israel_people ONE (its first tape write; the case kind entered_the_land ABSENT from the tape), favor_barred
ONE, intermarriage_barred ONE valued both directions — sources beginning "Deut 7:2" / "Deut 7:2" / "Deut 7:3".
CQ4 THE READBACK ON THE KIN — the_readback's rows twenty-one, every row's entry FOUND: the tape lines by kind and first verse (covenant_offered at Exod
19:4, brought_out at Exod 12:51, plague_struck ten by value, sea_split at Exod 14:21, healer_promised at Exod 15:26, sworn_by_himself at Gen 22:16,
oath_upheld at Gen 26:3, visitation_promised at Gen 50:24, stand_here_commanded at Deut 5:28, ten_words_declared at Deut 4:10) and the kin's cells by
CALL (ordinances.land, erection.covenant, journeys.the_command, covenant_at_horeb.the_second_word and the_tenth_word — each returning its verdict on its
own ask); the grades' census typed from the runner's print (VERBATIM 4, VARIANT 5, EXPANDED 8, TURNED 3, SHORTENED 1 predicted); no row OPEN; the four
holes named.
CQ5 THE KIN STANDS — other_gods_barred on israel_people ONE UNMOVED, coveting_barred ONE UNMOVED (the cells CALLED, no second write), treasured_people
ONE UNMOVED (a heaven entry, open), high_places_banned UNMOVED, the dispossession's two debits (dispossess_the_inhabitants_and_possess_the_land, destroy_their_images) OPEN UNMOVED.
CQ6 THE BLESSING AND THE PITY — blessing_promised on israel_people ONE (heaven, open), pity_barred ONE (a block), sources beginning "Deut 7:12" and
"Deut 7:16".
CQ7 THE ABOMINATION — house_abomination_barred on israel_people ONE (a block), source beginning "Deut 7:25"; coveting_barred UNMOVED (the object's turn a
readback row, not a second write).
CQ8 THE EXODUS READ BACK — the ten plague_struck lines and their closes UNMOVED; brought_out ONE; sea_split ONE; healer_promised ONE; the Shittim
lines UNMOVED; nothing written on Egypt, Pharaoh, Amalek or the seven nations (no entity for the seven; the-amorite untouched).
CQ9 THE REST — entities 319 UNMOVED, closes 127, markers 167, the population table 148 UNMOVED, the three kinds present; the other counts 4b's exactly
with the three lines and the daemon's seven writes dropped (THE REST test — NO declared delta this sitting: the daemon writes only on its own lines).
NO retype of the older REST literals (closes and markers unmoved — checked by grep before the tape); every miss shown at once by checkpoint_check.py
--all AFTER the tape (4b's lesson: the tape first when the tape grows).

THE PREDICTION'S ARITHMETIC: RUN = (1307, 96, 88, 0, 12, 1602, 38, 319, the four pairs, 127) — events +3 (the three lines), timers set +0, fired +0 (no
clock walk), cancels 0, retro-writes 12 UNMOVED, writes +7 (the daemon's watches summed: four at the first line, two at the second, one at the third),
daemons fired +1 (law_seven_nations), entities +0, closes +0; PREVIOUS_RUN = 4b's RUN EXACTLY (1304, 96, 88, 0, 12, 1595, 37, 319, the four pairs, 127):
THE REST drops the three lines by the runner's tag and the span and the daemon's seven writes with them — no delta; NEWEST_RUNNER 'seven_nations';
PLACEMENT markers UNMOVED ({{'text_constrained': 106, 'reading_placed': 46}}), events page_order 1140 → 1143 (text_constrained 109, reading_placed 55
unmoved) — read at the stitcher's print; CENSUS typed from the stitcher's print (on tape 1304 → 1307, history +3, kinds 849 → 852 — the three tape
kinds, subjects 272 UNMOVED, markers 167 (F 129, R 23), closes 71 unmoved; the case rows the exam's persons); the population table 148 UNMOVED; the
scene's tuple PREDICTED BY SCRIPT at the runner step (the exam's persons through seven_nations_case — each written once; no timer; no close); the
narrative's (on its own world: 7 writes, 0 closes, the entities israel = 1, the counter's day (11, 1), 0 dated lines, no row).

THE PROBES (RUN 2's first step): readback_probes.py Q16-Q18 written to FAIL before the runner exists — Q16 the runner and its the_readback table
(twenty-one rows; the census VERBATIM 4 / VARIANT 5 / EXPANDED 8 / TURNED 3 / SHORTENED 1; every row's entry found — the tape lines by kind and verse,
the kin's cells by CALL; the four holes named), Q17 the three lines on the counter's day with NO marker (markers 167 after the run) and the seven
writes on Israel with their sources (the ban's debit OPEN; the three border blocks; the blessing's heaven entry; the pity's block; the abomination's
block), Q18 the kin stands — other_gods_barred, coveting_barred, treasured_people, high_places_banned and the dispossession's debit UNMOVED, no second
write for the coveting or the other gods; Q13-Q15 unchanged; NO parser rule this sitting (the two number verses read right at the reading —
census_probes unmoved at 224); the register gate unchanged; checkpoint_probes' verse computed (2b's form).

THE ORDER: this design → the state doc's checkpoint (#194 addendum 4 — RUN 1 closed) → RUN 2: the probes to FAIL (Q16-Q18 0/3) → THE DOCKET by the
union rule (the scan rerun with the Avodah Zarah amudim named — 42a-42b, 44b-46b, 47b-48b, 49b, 51b-52b, 53b-54b — and the rest of 42a-54b dropped to
the enumeration, the dump; the rows read WHOLE in four parts A-D on 4b's whole-row instruments (ch6_docket_A-D.py with their WHOLE overlays the forms:
the address, the kind, the row entire); the verdicts LAW / DERIVATION / DISPUTE / CONTEXT / OUTSIDE with the crowns the design expects; the writer
write_ch7_docket.py from write_ch6_docket.py by sed with the coverage computed and the cite index) → the checkpoint (#194 addendum 5) → RUN 3: the
types by script (add_types_ch7.py) → the recorder and the stitcher (the scratch copies: SPAN_ORDER + 'seven_nations'; no marker row) → the gates to
FAIL (daemon, dependency) → the runner (ch7_part1-4.py assembled by cat; the fast checker over parts 1 and 2; the honest-pairing guard; zero-report
probes; the scene and the narrative predicted by script; CASES generated from the cells' asks) → the recorder → the stitcher → the literals CQ1-CQ9
(patch_seq_literals_ch7.py) → the tape run (10/10 with THE REST) → `checkpoint_check.py --all` AFTER the tape → the checkpoint (#194 addendum 6) →
RUN 4: `gates_chain.sh` in the background (one summary: the probe gates incl. readback Q16-Q18 to 18/18, the daemon and dependency gates, build_world,
the journal gate, THE REGISTER GATE --strict unmoved, the positions table 235 → 244, checkpoint_probes, the sweep 62 runners, the journal gate again) →
the records from the sheet in one call (this section's AS BUILT, COMPILE_DEBT's sitting-5 box PAID + the 5b box with the war chapter's cells owed
forward, MOVE_CATALOG (checked), MIDDOT's docket entries, MISHNAH_TOPICS (Avodah Zarah 1-4; Kiddushin 3:12), RESEARCH_LOG, THE_STEPS, THE_BRIEFING,
THE_LOOP.md's step 6 row (the laws' form on the kin), RESUME, memory, the state doc's addendum, the recovery page rewritten, the addenda's section) →
the forms copied → the commit message for the owner's word.
'''
STATE = f'''
#194 ADDENDUM 4 ({DATE} — RUN 1 OF SITTING 5b CLOSED, on the owner's "Go" after sitting 5's run 4 (the tree uncommitted since 64a8362 — the reading's message drafted, his word not yet given): THE COMPILE OF CHAPTER 7 — the rereads, the measurements, the design). THE REREADS: THE_STEPS' compiler block and Step 5's head (this window, at the reading's run 2), the map's "Sitting 4b" design and AS BUILT (the compile's form), the 5b box (a)-(p). THE MEASUREMENTS (ch7_compile_recon.py → ch7_recon.out 302 KB, read by section; ch7_docket_scan.py → ch7_scan.out and the dump ch7_docket_dump.txt 2,048 lines; the one database's run_ledger queried): the chapter's kin in the code — ordinances.land (Exodus 23:20-33), erection.covenant (34:10-16), journeys.the_command (33:50-56), covenant_at_horeb's second and tenth words, exodus_story's plagues / sea / marah / trials / amalek / sinai, obey_horeb.the_one_god, opening_speech, balak.peor, shemini.classify; the registry's effects covenant_barred and intermarriage_barred exist but are ABSENT from the running world (their case kinds Joshua's and the exam's), treasured_people / other_gods_barred / coveting_barred / high_places_banned PRESENT; the retellings' tape lines all present (the plagues, the sea, the healer, the oath's three, the treasure at 19:5-6, the Shittim lines, the dispossession, Sihon's and Og's devotings); NO cell anywhere for the ban on the seven nations, no favor, no pity, the abomination into the house — THE CODE'S FOUR HOLES; the prefix CQ free; the counts markers 167 / closes 127 / entities 319 / daemons 66 unmoved before the tape; the docket 52 link rows in 19 works + the topic ranges sized (Avodah Zarah 42a-54b 465 — the design reads its verse-anchored amudim, 303 rows, the rest enumerated outside declared scope; eleven verses of the chapter cited by no one). THE DESIGN written into the map: "Sitting 5b — THE COMPILE OF CHAPTER 7 … THE DESIGN" — the runner cold_run_seven_nations.py (the 62nd), the daemon law_seven_nations (given_at Deut 7:1, boot), THREE tape lines and NO marker (nations_devoted 7:1-5, hearing_blessed 7:12-16, abomination_barred 7:25-26), four new effects (favor_barred, pity_barred, blessing_promised, house_abomination_barred) and three reused (commanded valued devote_the_seven_nations — the ban's debit OPEN to Joshua; covenant_barred and intermarriage_barred at their first tape writes), six cells, sixteen DATA rows, THE READBACK ON THE KIN (the laws' form run on another chapter's code — twenty-one rows, VERBATIM 4 / VARIANT 5 / EXPANDED 8 / TURNED 3 / SHORTENED 1 predicted; the four holes compiled here), the decisions (a)-(p), CQ1-CQ9, RUN (1307, 96, 88, 0, 12, 1602, 38, 319, the four pairs, 127) and PREVIOUS_RUN 4b's exactly; the install hypothesis tested in passing, not ruled. NOTHING MID-FLIGHT — A CLEAN COMPACTION POINT. The tree: sitting 5 whole (uncommitted; the commit message at <scratch>/commit_msg_ch7.txt still stands for the reading — the design rides the next message), the map, the state doc, the recovery page, the memory. THE WORD FOR THE NEXT SITTING — RUN 2 OF 5b, its first step: readback_probes.py Q16-Q18 written to FAIL (0/3), then the docket — ch7_docket_scan.py rerun with the Avodah Zarah amudim named (42a-42b, 44b-46b, 47b-48b, 49b, 51b-52b, 53b-54b) and the rest of 42a-54b dropped to the enumeration, the dump; the rows read WHOLE in four parts A-D on 4b's whole-row instruments (World/step9/forms_deuteronomy_walk/ch6_docket_A-D.py and ch6_docket_common.py with their WHOLE overlays — the forms; the address, the kind, the row entire), the verdicts LAW / DERIVATION / DISPUTE / CONTEXT / OUTSIDE with the crowns the design expects; write_ch7_docket.py from write_ch6_docket.py by sed (the coverage computed, the cite index); the checkpoint #194 addendum 5. POST-COMPACTION REREADS: the recovery page, the map's "Sitting 5b … THE DESIGN", MEMORY.md.
'''
MN = f'''
SITTING 5b RUN 1 DONE {DATE} (on "Go" after sitting 5's run 4; the tree uncommitted since 64a8362): the measurements (ch7_compile_recon.py, ch7_docket_scan.py, the one database) and THE DESIGN in the map ("Sitting 5b — THE COMPILE OF CHAPTER 7 … THE DESIGN"): the runner cold_run_seven_nations.py, the daemon law_seven_nations (boot, given_at Deut 7:1), three tape lines (nations_devoted 7:1-5, hearing_blessed 7:12-16, abomination_barred 7:25-26) and NO marker, four new effects + the ban's debit OPEN to Joshua + covenant_barred and intermarriage_barred at their first tape writes, six cells, THE READBACK ON THE KIN (the laws' form on Exodus 23, 34, Numbers 33 and the two words — twenty-one rows predicted VERBATIM 4 / VARIANT 5 / EXPANDED 8 / TURNED 3 / SHORTENED 1; the code's four holes compiled here), CQ1-CQ9, RUN (1307, 96, 88, 0, 12, 1602, 38, 319, the four pairs, 127), PREVIOUS_RUN 4b's. Clean point (#194 addendum 4). NEXT: RUN 2 — readback Q16-Q18 to FAIL, then the docket (52 link rows + the ranges; Avodah Zarah's verse-anchored amudim) in four parts, EVERY ROW WHOLE, write_ch7_docket.py.
'''
plans = []
P = f'{ROOT}/World/step9/DEUTERONOMY_WALK.md'; s = rd(P); assert '## Sitting 5b — THE COMPILE OF CHAPTER 7' not in s and s.rstrip().endswith('Then chapter 8, and on in order.')
plans.append((P, s.rstrip('\n') + DESIGN))
P = f'{ROOT}/logic/pre_logic_methods_2026-07-28/PROMPT_continue_solo_era_2026-08-06.md'; s = rd(P); assert '#194 ADDENDUM 4' not in s and '#194 ADDENDUM 3' in s
plans.append((P, s.rstrip('\n') + STATE))
P = f'{ROOT}/logic/pre_logic_methods_2026-07-28/RECOVERY_new_thread_2026-09-12.md'; s = rd(P)
old = '- NEXT ON HIS WORD: the commit; then 5b — THE COMPILE OF CHAPTER 7 in four runs (the debt box; the design first), or the schema sitting.\n'
new = '- IN FLIGHT: 5b RUN 1 DONE (the design in the map); NEXT: RUN 2 — readback Q16-Q18 to FAIL, then the docket WHOLE. The commit on his word.\n'
assert s.count(old) == 1; s2 = s.replace(old, new); assert len(s2.encode()) <= 10240, len(s2.encode()); plans.append((P, s2))
P = f'{MEM}/deuteronomy-walk.md'; s = rd(P); assert 'SITTING 5b RUN 1 DONE' not in s
plans.append((P, s.rstrip('\n') + '\n' + MN))
P = f'{MEM}/MEMORY.md'; s = rd(P)
old = 'SITTING 5 DONE 2026-09-18 (ch 7 FROZEN, 221 units); the INSTALL hypothesis ON THE TABLE; NEXT: commit, then 5b'
new = 'SITTING 5 DONE 2026-09-18 (ch 7 FROZEN, 221 units); 5b RUN 1 DONE (the design); NEXT: RUN 2 the docket'
assert s.count(old) == 1, s.count(old)
s2 = s.replace(old, new); assert len(s2.encode('utf-8')) < 17000, len(s2.encode('utf-8'))
plans.append((P, s2))
for p, s2 in plans: assert s2 != rd(p), p
if CHECK:
    for p, s2 in plans: print('WOULD WRITE', p.replace(ROOT, '<repo>').replace(MEM, '<memory>'), len(rd(p)), '->', len(s2))
    sys.exit(0)
for p, s2 in plans:
    open(p, 'w', encoding='utf-8').write(s2); print('WROTE', p.replace(ROOT, '<repo>').replace(MEM, '<memory>'), len(s2.encode('utf-8')))
print('the 5b design and the run 1 checkpoint written')
