#!/usr/bin/env python3
# THE DEUTERONOMY WALK sitting 6b — THE COMPILE OF CHAPTER 8 (2026-09-18; the owner: "Next" after sitting 6's close): THE DESIGN written into the map
# at the close of RUN A of two (the rereads, the measurements — ch8_compile_recon.py, ch8_docket_scan.py, the one database queried here — and this
# section, BEFORE any code; the docket its own run after the window's budget), with the state doc's checkpoint (#196 addendum 2) naming the next step,
# the recovery page's line, the memory note and the index line. Every number typed from the two instruments' prints of this run or computed here from
# the one database; the caps asserted before any file is opened; --check prints the plan only. Sitting 5b's form (write_ch7b_design.py).
import os, re, subprocess, sys, sqlite3, yaml
ROOT = subprocess.check_output(['git', 'rev-parse', '--show-toplevel'], text=True).strip()
MEM = os.path.expanduser('~/.claude/projects/-Users-Shared-TorahSim/memory')
SP = os.path.dirname(os.path.abspath(__file__))
CHECK = '--check' in sys.argv
def rd(p): return open(p, encoding='utf-8').read()
R = rd(f'{SP}/ch8_recon.out'); S = rd(f'{SP}/ch8_scan.out')
assert "FREE prefixes: ['CU']" in R and 'LINK rows 34 in 17 works' in S and 'TOPIC rows 417' in S and 'PRIOR READS (credited): 101 addresses of 451' in S and 'Berakhot 35a-49b whole: 506 rows; the amudim read here: 197' in S
assert 'RUN (1307, 96, 88, 0, 12, 1602, 38, 319' in R and 'NEWEST_RUNNER seven_nations' in R and "I5 expects: ['67']" in R and 'pointers naming Deut 8: []; edges naming Deut 8: []' in R and 'DAEMON_ORDER 67' in R
assert 'kinds 1129, effects 1029' in R and "PLACEMENT {'markers': {'text_constrained': 106, 'reading_placed': 46}, 'events': {'text_constrained': 109, 'page_order': 1143, 'reading_placed': 55}}" in R
assert 'CENSUS (2504, 1316, 1307, 1172, 6, 10, 9, 0, 71, 167, 129, 15, 23, 852, 272)' in R and 'the verses NOT cited by anyone: [1, 2, 4, 6, 12, 13, 17, 18, 19, 20]' in S
assert 'an effect row (forgetting_barred): ABSENT' in R and 'an effect row (manna_provided): {' in R and 'an effect row (serpents_sent): {' in R and 'water_from_the_rock' in R and 'bread_and_water_blessed' in R
for k in ("'kind': 'manna_fell'", "'kind': 'rock_struck'", "'kind': 'rock_struck_twice'", "'kind': 'fiery_serpents_sent'", "'kind': 'decree_declared'", "'years': 40", "'kind': 'brought_out'", "'kind': 'sworn_by_himself'", "'kind': 'oath_upheld'", "'kind': 'visitation_promised'", "'kind': 'covenant_offered'", "'kind': 'nations_devoted'"):
    assert k in R, k
assert 'the register seats naming Deut 8 / 7 / 6: []' in R and "'the-manna': 'the_manna', 'the-rock': 'the_rock', 'the-serpent': 'the_serpent'" in R
# THE ONE DATABASE — the kin's effects on the running world (presence by effect and entity; the rows accumulate over the recorded runs, so presence is the fact)
db = sqlite3.connect(f'file:{ROOT}/World/journal/data/world.sqlite?mode=ro', uri=True)
def present(effect, entity=None):
    q = "SELECT COUNT(*), COALESCE(SUM(open), 0) FROM run_ledger WHERE effect=?" + (" AND entity=?" if entity else '')
    n, o = db.execute(q, (effect, entity) if entity else (effect,)).fetchone(); return n, o
P_MAN = present('manna_provided'); P_ROCK = present('water_from_the_rock'); P_SERP = present('serpents_sent'); P_BW = present('bread_and_water_blessed')
P_SHM = present('shema_commanded', 'israel_people'); P_TST = present('test_barred', 'israel_people'); P_OTH = present('other_gods_barred', 'israel_people'); P_BFH = present('blessings_for_hearing', 'israel_people')
P_FGT = present('forgetting_barred'); P_BLS = present('bless_after_eating_commanded'); P_TRE = present('treasured_people', 'israel_people')
assert P_MAN[0] > 0 and P_ROCK[0] > 0 and P_SERP[0] > 0 and P_SHM[0] > 0 and P_TST[0] > 0 and P_OTH[0] > 0 and P_BFH[0] > 0 and P_TRE[0] > 0 and P_FGT[0] == 0 and P_BLS[0] == 0, (P_MAN, P_ROCK, P_SERP, P_SHM, P_TST, P_OTH, P_BFH, P_TRE, P_FGT, P_BLS)
GARM = db.execute("SELECT effect, entity, verse FROM run_ledger WHERE effect LIKE '%garment%' OR effect LIKE '%cloth%' OR effect LIKE '%shoe%' OR effect LIKE '%swell%'").fetchall()
GARM_ISR = [g for g in GARM if g[1] == 'israel_people']
dd = yaml.safe_load(open(f'{ROOT}/World/step9/daemon_dispositions.yaml', encoding='utf-8'))
W426 = dd['daemons']['law_obey_horeb']['watches'].get('witnesses_called')
W426_ISR = [present(e, 'israel_people') for e in (W426 or [])]
DECREE_W = dd['daemons']['law_shelach']['watches'].get('decree_declared')
MANNA_W = dd['daemons']['law_exodus_story']['watches'].get('manna_fell'); ROCK_W = dd['daemons']['law_exodus_story']['watches'].get('rock_struck'); SERP_W = dd['daemons']['law_chukat']['watches'].get('fiery_serpents_sent')
print('THE WORLD:', dict(manna_provided=P_MAN, water_from_the_rock=P_ROCK, serpents_sent=P_SERP, bread_and_water_blessed=P_BW, shema_commanded=P_SHM, test_barred=P_TST, other_gods_barred=P_OTH, blessings_for_hearing=P_BFH, treasured_people=P_TRE, forgetting_barred=P_FGT, bless_after_eating_commanded=P_BLS, garment_rows=GARM[:6], garment_rows_on_israel=GARM_ISR))
print('THE WATCHES: witnesses_called →', W426, W426_ISR, '| decree_declared →', DECREE_W, '| manna_fell →', MANNA_W, '| rock_struck →', ROCK_W, '| fiery_serpents_sent →', SERP_W)
TESTI = (f"4:26's line witnesses_called is watched by law_obey_horeb writing {W426} (present on Israel: {W426_ISR}) — the chapter's 8:19 REUSES that effect at its second seat, no new effect (the effects 1029 → 1031)" if W426 and any(n for n, _ in W426_ISR)
         else f"4:26's line witnesses_called writes {W426 or 'NOTHING'} on Israel — the chapter's 8:19-20 writes perishing_testified NEW, a conditional HEAVEN entry on Israel (the form of blessings_for_hearing turned: if you forget, you perish) — the effects 1029 → 1032")
N_EFF = 1031 if (W426 and any(n for n, _ in W426_ISR)) else 1032
GARM_TXT = ("NO ROW on any ledger names a garment, clothing, a shoe or a swelling on Israel" if not GARM_ISR else f"the ledger rows naming a garment on Israel: {GARM_ISR} — READ before the row is typed") + (f" (the other garment rows on the world: {len(GARM)} — the vestments', Joseph's, Aaron's)" if GARM else '')
DATE = '2026-09-18'
DESIGN_A = f'''

## Sitting 6b — THE COMPILE OF CHAPTER 8, Deuteronomy 8:1-20 ({DATE}; the owner: "Next" after sitting 6's close): THE DESIGN — written at the close of
## RUN A of two under THE TWO-RUN RULE (the rereads: THE_STEPS' compiler block and Step 5's head, the 5b AS BUILT and the 5b design's writer as the compile's
## form, the 6b box (a)-(n); the measurements: ch8_compile_recon.py, ch8_docket_scan.py in the scratchpad, the one database queried) and BEFORE any code;
## the docket ITS OWN RUN by the window's budget (451 rows, under the ~700 clause — the run that measured and designed had spent its 300k already)

THE TWO RUNS AND THE DOCKET'S OWN: RUN A the rereads, the measurements and this design — CLOSED HERE, a clean compaction point (#196 addendum 2); THE
DOCKET by the union rule, EVERY ROW WHOLE (three parts A-C on 5b's whole-row instruments, the writer write_ch8_docket.py, coverage computed) — its own
run, the dump already written (ch8_docket_dump.txt, 1,355 lines); RUN B the probes to FAIL (readback Q19-Q21), the types by script, the recorder and the
stitcher, the runner in parts with the fast checker and the generated CASES, the literals CU1-CU9, the tape to 10/10 with THE REST, checkpoint_check.py
--all AFTER the tape, gates_chain.sh in one summary, the records from the sheet in one call, the forms copied, this section's AS BUILT, the commit message.

THE MEASUREMENTS (what the tape, the runners, the registries and the one database say before a line is typed): THE COUNTER stands at (40, 11, 1); the
tape's LAST LINES are chapter 7's three (nations_devoted 7:1-5, hearing_blessed 7:12-16, abomination_barred 7:25-26 — on the counter's day, no marker)
and its LAST MARKER the forward one at Deut 5:32 (M['charge']) — CHAPTER 8 OPENS ON THE COUNTER'S OWN DAY, NO MARKER, the speech continuing. EVERY ACT
THE CHAPTER RETELLS IS ON THE TAPE (the recon's section 5): the manna — manna_fell (Exod 16:13-15; 16:4 the test-clause "whether they will walk in My law
or not"), the naming (16:31 "manna — what is it"), the omer kept (16:33-34), the murmurings (the fleshpot 16:2-3, the manna left till morning, the seventh
day); the rock — rock_struck (Exod 17:6 — Rephidim's "give us water" 17:2-3, the naming Massah and Meribah 17:7) and rock_struck_twice (Num 20:10-11 —
Meribah's second seat, the congregation's strife 20:2-5, the sentence 20:12-13); the serpents — fiery_serpents_sent (Num 21:6), the pole commanded (21:8),
the copper serpent made (21:9), "our soul loathes the light bread" (21:5); the forty years — decree_declared (Num 14:26-35: years 40, day_for_year [40,
40]); the craving — lust_and_weeping and quail_and_plague (Num 11:4-35, the manna described like coriander seed); the exodus — brought_out (Exod 12:51)
with its two closes; the oath's three lines (sworn_by_himself Gen 22:16-18, oath_upheld 26:3-5, visitation_promised 50:24); the treasure —
covenant_offered (Exod 19:5-6); Marah's healer_promised (15:26) and the statute set (15:25); the testimony — witnesses_called (Deut 4:26, obey_horeb's
line); the Shema's warning — shema_declared and testing_barred (6:4-9, 6:16-19; 6:10-12's houses a cell without a line); the heel — hearing_blessed
(7:12-16). THE ONE ACT WITH NO LINE IS NOT AN ACT: "your garment did not wear out upon you, nor did your foot swell, these forty years" (8:4) — a STATE
over forty years, told only here (29:4 the plural garments, Nehemiah 9:21 the only other "did not swell"); {GARM_TXT}. THE CHAPTER'S KIN IS IN THE CODE:
exodus_story.manna (day_by_day, double, fifteenth_sabbath, FORTY_YEARS, less_thirty, omer_before, sabbath, seventh_none, twilight), exodus_story.trials
(ten_list, count_by_exodus — the ten trials of Israel against God, the other direction), exodus_story.marah (healer_condition, statute_list),
exodus_story.plagues / sea / sinai (treasure_seats); beha.taberah_and_quail (dew, five_foods, manna_fell, manna_form, manna_taste — the craving's manna);
shelach.decree (day_for_year, count_from, deaths_ceased, due — the forty years); chukat.meribah (first_meribah_clauses, meribah_seats, cattle_water) and
chukat.arad_and_the_serpent (bite_and_burn, light_bread, nehushtan, pole_word, serpent_heals, singular_serpent); ordinances.land (bread_water — Exodus
23:25 "He shall bless your bread and your water", the Sifrei 40:10's kin); opening_speech.the_bypass (forty_years_lacking_nothing — 2:7),
the_spies_read_back (the_carrying — 1:31 "as a man carries his son"; good_is_the_land), the_commission (1:19's "great and terrible wilderness");
obey_horeb.the_exhortation (hear_and_do — 4:1 "that you may live and go in and possess"), horeb_retold (take_heed_lest_you_forget — 4:9),
the_exile_case (the_witnesses, perish_and_scatter, serve_wood_and_stone — 4:26's testimony), the_one_god (because_he_loved_your_fathers);
covenant_at_horeb.the_second_word (no_other_gods, bow_and_serve, the_visiting); hear_o_israel.the_header (the_land_flowing, the_triad),
the_gift_and_the_warning (the_list — the houses you did not build, LEST_YOU_FORGET — 6:12, no_other_gods, fear_serve_swear), the_sons_question;
seven_nations.the_holy_people (the_oath — 7:8's three lines by CALL), because_you_hear (the_heel — 7:12; the_write), the_seven_nations (the_ban — the
nations perishing before you); sanctions' Leviticus 18:5 rows ("and live by them" — 8:1's and 8:3's living); mamre and joseph (the oath's lines);
decalogue (20:3-6 the first copy of the second word). THE EFFECTS ALREADY IN THE REGISTRY for the chapter's matter: manna_provided (a STATUS on the
people — 16:4), water_from_the_rock (a STATUS — 17:6), serpents_sent (a HEAVEN entry — 21:6), bread_and_water_blessed (a HEAVEN entry on the people who
serve — 23:25), shema_commanded (a STATUS — 6:4), test_barred (a BLOCK — 6:16), other_gods_barred (the second word's BLOCK), blessings_for_hearing (the
conditional HEAVEN entry — 7:12), treasured_people (19:5-6), covenant_barred and the 5b blocks; NO EFFECT ANYWHERE for the blessing after the meal, the
forgetting barred, the humbling, the discipline, the garment (asserted on the registry: bless_after_eating_commanded and forgetting_barred ABSENT).
THE ONE DATABASE READ (run_ledger): manna_provided PRESENT {P_MAN}, water_from_the_rock PRESENT {P_ROCK}, serpents_sent PRESENT {P_SERP},
bread_and_water_blessed PRESENT {P_BW}, shema_commanded {P_SHM} and test_barred {P_TST} on Israel, other_gods_barred {P_OTH}, blessings_for_hearing
{P_BFH}, treasured_people {P_TRE}; forgetting_barred and bless_after_eating_commanded ABSENT (never written). THE TESTIMONY'S EFFECT: {TESTI}. THE
CODE'S HOLES (no cell anywhere — the recon's regex per def over all sixty-two runners): THE BLESSING AFTER THE MEAL ("satisfied/grace" only the modules'
strip helpers and Balak's seats; no cell reads "eat, be satisfied, bless"), THE FORGETTING BARRED (hear_o_israel's the_gift_and_the_warning holds
6:12's clause as an ask, lest_you_forget, WITHOUT A WRITE — the block never reached the tape), "NOT BY BREAD ALONE" (no cell; the Sifrei 48:10's and
Yoma 74b's matter), THE DISCIPLINE OF A SON (8:5 — no cell; Berakhot 5a's afflictions of love), THE GARMENT AND THE FOOT (8:4 — no cell, no line, no
effect: THE FIFTH FORM'S question) — compiled or graded here. THE CHECKPOINT PREFIX measured FREE: CU — THE LAST of the two-letter space (CA-CZ all
used but CU; the next compile opens a new series — the probes' regexes reading 'C[A-Z]' (the recon's finder, checkpoint_positions, checkpoint_probes)
to be measured at 7b's design: a NOTE for COMPILE_DEBT, owed forward). THE GLOBAL COUNTS grepped before the tape run: markers 167 (F 129, R 23, P 15)
UNMOVED — no marker this chapter; closes 127 UNMOVED — no close; entities 319 UNMOVED (Israel the written-on party; the-manna, the-rock, the-serpent
mapped to their registry rows, untouched — the readback references their lines); daemons 67 → 68 (I5 67 → 68); kinds 1129 → 1133 (three tape kinds,
one case kind), effects 1029 → {N_EFF}; CENSUS on tape 1307 → 1310, kinds 852 → 855; PLACEMENT events page_order 1143 → 1146 (the lines on the counter's
day, no marker), markers unmoved; the positions table 244 → 253 checkpoints. THE REGISTER GATE: no receipt form in the chapter ("which I command you"
the giving; no "as the LORD commanded") — DECLARED 100 unmoved, no seat.
THE DOCKET SIZED (ch8_docket_scan.py — the export's chapter 8 the DB's, no division map): 34 LINK rows in 17 works (Berakhot 9, Yoma 4, Sotah 3, Sukkah
3, Menachot 2, Tosefta Berakhot 2, Arakhin, Bava Metzia, Chullin, Eruvin, Ketubot, Mishnah Sukkah, Pesachim, Sanhedrin, Taanit, Tosefta Bikkurim one
each, and the Rambam's Introduction to the Mishnah 8:23 — a commentary's row that passed the export's category filter, read and marked); the verses
cited 3 (four), 5, 7 (two), 8 (eight), 9 (five), 10 (TWENTY — the grace after meals' seat), 11, 14 (three), 15, 16 — TEN VERSES CITED BY NO ONE (1, 2, 4,
6, 12, 13, 17-20: the frame, the forty years, the garment, the walking, the herds and the silver, the boast, the testimony — narrative and exhortation, not
law); + THE TOPIC RANGES SIZED: Mishnah Berakhot 6-7 whole (13 rows — the blessings over food, the zimmun), Mishnah Bikkurim 1 whole (11 — the first
fruits from the seven species); Berakhot 5a 24 rows (the afflictions of love — 8:5, 8:7), 20b-21a 39 (the grace after meals by Torah law — 8:10),
35a-35b 44 (the blessing before as an inference; "the earth He gave to man" after a blessing), 41a-44a 100 (the order of blessings by the verse's order
and its two "land"s — 8:8; the after-blessing 44a), 48b-49b 53 (the grace's four blessings from the verse; the measure of "satisfied"); Yoma 74b-76a
69 ("afflicted you and let you hunger" — the manna's forms, the sixty cubits, the tastes; 8:3, 8:16); Sotah 4b-5a 39 (arrogance as denial — 8:11, 8:14);
Makkot 13b 21 and Eruvin 96a 14 ("take heed, lest, do not" a negative command — 8:11) — THE DESIGN DECLARES every range whole (417 topic rows); Berakhot
35a-49b's OTHER amudim (36a-40b, 44b-48a — 309 rows: the blessings over each species, the zimmun's mechanics, the wine) ENUMERATED and marked outside
declared scope (Step 2's standing rule; the scan's count the enumeration): the docket 451 rows (34 + 417), 101 credited (the Numbers 30 vows exam, the
chapter-4 docket, Beha's exam, the Exodus ledgers — Mishnah Berakhot 6:3, 7:1, Bikkurim 1:2, 1:3, 1:9 among them), in THREE parts A-C, EVERY ROW WHOLE.
THE CHAPTER'S OWN INK (the reading's 144 asserts, reused in the runner): two number verses (8:2 and 8:4 "these forty years" [40] — 2:7 the same phrase,
[40] at every seat of the wilderness's forty years), no gap; the sated verb starred at 8:10 and 8:12; no divine frame, no "saying", three narrative verbs
at 8:3 (humbled, let hunger, fed), ONE imperative (8:11 "take heed"), two infinitive absolutes at 8:19, the consecutive perfect in ten verses, the
prohibition form twice and neither a command (8:9 a promise, 8:20 a report), singular in sixteen verses, plural in one (8:20), both in two (8:1, 8:19),
neither in 8:8 (no verb); the article + participle chain of five (8:14-18); the written/read pair at 8:2 (the store's extra token — kept out of every
check); the phrase censuses (the design of sitting 6): "eat, be satisfied, bless" ONE, "not by bread alone" ONE, the seven species at 8:8 alone, "did not
swell" two Bible seats, "silver and gold" 8:13 / 17:17 the pair, "and your heart be lifted up" ONE (17:20), "if you surely forget" ONE, "that you shall
surely perish" 4:26 / 8:19 / 30:18, "because" the heel's five seats, "hearken to the voice of the LORD your God" ten with 8:20 the one plural.

THE NAME: cold_run_good_land.py — the 63rd runner ("a good land", 8:7 and 8:10 — the chapter's refrain; the manna and the land its two halves);
law_good_land the 68th daemon (given_at Deut 8:1 — the chapter's frame, its own line; installed_by boot — the four Deuteronomy daemons' form); the span
[[Deut, 8, 1, 20]]; the checkpoints CU1-CU9; the unit deu_08_manna_humility the frozen reading.
'''
DESIGN_B = f'''
THE READBACK ON THIS CHAPTER — THE FIFTH FORM: THE RETELLING OF A STATE (THE LOOP's step 6; after T1 the narrative retelling, T2 the retelling that fills
a hole, T3 the retelling inside a law, T4 the laws' form on the kin): chapter 8 retells the wilderness as a REASON for a law ("remember … lest you
forget"), so its rows are REFERENCE ROWS graded against the tape's lines by kind and first verse or against the kin's cells by CALL, never a second
write — and ONE row retells a STATE the tape never wrote and cannot write as an act: the garment that did not wear out and the foot that did not swell
over forty years. THE DECISION (the design's, open to the owner's word): a state told only in the retelling is graded SUPPLIED — a new grade beside
VERBATIM / VARIANT / EXPANDED / TURNED / SHORTENED — with NO retrograde write: the tape records acts at days (the retelling rules' "an act told only in
the retelling is written once at its own day" names an ACT), a forty-year condition has no day; the row names the state, its span (the exodus to the
counter's day), the ledger scan that found no entry (asserted at build — no effect naming a garment, clothing, a shoe or a swelling on Israel), and the
kin (29:4's plural garments, Nehemiah 9:21). THE ROWS (eighteen predicted; the grades' census typed from the runner's print at RUN B): 8:1 "that you may
live and multiply and go in and possess" — against obey_horeb.the_exhortation('hear_and_do') by CALL (4:1): VERBATIM in kind; 8:2 "led you these forty
years in the wilderness, to humble you, to test you, to know what was in your heart" — against decree_declared (Num 14:26-35, years 40) by kind:
EXPANDED (the purpose supplied — the humbling, the test, the heart); 8:2 "whether you would keep His commandments or not" — against manna_fell's test
clause (Exod 16:4 "whether they will walk in My law or not"; exodus_story.manna by CALL): VERBATIM in kind; 8:3 "He humbled you and let you hunger and
fed you the manna" — against manna_fell (16:13-15) and the fleshpot's murmuring (16:2-3): TURNED (the hunger God's act, the murmuring's occasion made
the humbling's means; the manna's status manna_provided stands); 8:4 THE GARMENT AND THE FOOT — against NO LINE: SUPPLIED (the fifth form's row); 8:5
"as a man disciplines his son" — against 1:31 "as a man carries his son" (opening_speech.the_spies_read_back('the_carrying') by CALL): VARIANT (carried
→ disciplined; Berakhot 5a's row the exam's); 8:7-9 the good land — against 6:10-11's gift (hear_o_israel.the_gift_and_the_warning('the_list') by CALL)
and 6:3's "flowing with milk and honey" (the_header('the_land_flowing')): EXPANDED (the waters, the seven species, iron and copper; honey without milk);
8:9 "you shall not lack anything" — against 2:7 (opening_speech.the_bypass('forty_years_lacking_nothing') by CALL): VERBATIM in kind; 8:11 "take heed
to yourself lest you forget the LORD your God" — against 6:12 (hear_o_israel.the_gift_and_the_warning('lest_you_forget') by CALL — six tokens shared):
VERBATIM; 8:12-13 "eaten and satisfied, built good houses, herds and flocks and silver and gold multiplied" — against 6:10-11 (the houses you did not
build, the cisterns, the vineyards): VARIANT (the gift's list made the growth's; the king's law's tokens a DATA row, 17:16-17 forward); 8:14 "who
brought you out of the land of Egypt, out of the house of bondage" — against brought_out (Exod 12:51) by kind and 5:6 (covenant_at_horeb.the_second_word
by CALL — the formula's seats): VERBATIM in kind; 8:15 "who led you through the great and terrible wilderness, fiery serpents and scorpions and thirst"
— against fiery_serpents_sent (Num 21:6) by kind and 1:19 (opening_speech.the_commission by CALL): EXPANDED (the scorpions and the thirst named — no
line for either; 21:5's "no water" the thirst's seat); 8:15 "who brought you water out of the rock of flint" — against rock_struck (Exod 17:6) by kind
(rock_struck_twice Num 20:10-11 the second seat; chukat.meribah('meribah_seats') by CALL): VARIANT (the flint's word for Exodus' rock; the two rocks'
two words — a DATA row); 8:16 "who fed you manna in the wilderness which your fathers did not know, to humble you and test you, to do you good in your
end" — against manna_fell (16:13-15; 16:31 the naming): EXPANDED (the purpose — "in your end"); 8:18 "to establish His covenant which He swore to your
fathers" — against the oath's three lines (sworn_by_himself Gen 22:16, oath_upheld 26:3, visitation_promised 50:24) by kind and seven_nations.
the_holy_people('the_oath') by CALL (7:8's form): VERBATIM in kind; 8:19 "go after other gods and serve them and bow down to them" — against the second
word (covenant_at_horeb.the_second_word('no_other_gods', 'bow_and_serve') by CALL; 5:9 bow-then-serve): VARIANT (serve-then-bow — the census's ten
seats, four in this order); 8:19 "I testify against you this day that you shall surely perish" — against witnesses_called (Deut 4:26) by kind and
obey_horeb.the_exile_case('the_witnesses', 'perish_and_scatter') by CALL: VARIANT (heaven and earth the witnesses there, "I" here; the same infinitive
absolute; 30:18 forward); 8:20 "like the nations which the LORD makes perish before you, so shall you perish, because you would not hearken" — against
nations_devoted (7:1-5; seven_nations.the_seven_nations('the_ban') by CALL) and 7:12's heel (because_you_hear('the_heel')): TURNED (the measure for
measure — Israel like the nations; the heel's second seat). THE CENSUS PREDICTED: VERBATIM 6 / VARIANT 5 / EXPANDED 4 / TURNED 2 / SUPPLIED 1 —
eighteen rows; no row OPEN. THE RETELLING'S OWN WORDS, NO FIRST TELLING (DATA rows, not reference rows): "not by bread alone … but by all that proceeds
from the mouth of the LORD" (8:3 — a teaching, not an act; the Sifrei 48:10, Yoma 74b), "my power and the might of my hand" (8:17 — the boast the
chapter answers; Sotah 4b-5a), "He gives you power to get wealth" (8:18). THE CODE'S THREE HOLES (no cell and no write anywhere): THE BLESSING AFTER
THE MEAL (8:10 — the Torah's one command to bless; Mishnah Berakhot 6-7, Berakhot 48b, 20b-21a, 49b the answer sheet), THE FORGETTING BARRED (8:11 —
6:12's clause has a cell and no write; the block written here, its first tape write), THE TESTIMONY (8:19-20 — {('reused' if N_EFF == 1031 else 'NEW')}
per the watches read) — compiled here, their writes at the chapter's own day.

THE DESIGN'S DECISIONS (the box's (a)-(n) settled on the measurements):
(a) THE BLESSING AFTER THE MEAL — F3's eat_be_satisfied_bless: the code's hole — the WRITE bless_after_eating_commanded, a STATUS on Israel (the form of
shema_commanded), at the chapter's first line grace_commanded (8:7-10 — the good land's clause and the command); the measure of "satisfied" a PARAMETER
(Mishnah Berakhot 7:2's olive-bulk and egg-bulk; Berakhot 20b the rabbinic measure, 49b — the shelf's data, never the source); the four blessings from
the verse (48b — "bless" the blessing of the food, "for the land" the land's, "the good" Jerusalem's, "which He gave you" the good and the beneficent —
the exam's rows), the zimmun (Tosefta Berakhot 6:1, Berakhot 45a-b enumerated), the blessing before by inference (35a; Tosefta 6:2), the grace in any
language (Sotah 33a), Rabbi Tzadok's egg-bulk in the sukkah (Sukkah 26b, Mishnah Sukkah 2:5, Chullin 107a, Yoma 79b), consecrated property's blessing
(Bava Metzia 114a, Arakhin 4a) the exam's rows.
(b) THE SEVEN SPECIES — F3's the_seven_species: no write; the order of blessings by the verse's order and its two "land"s (Berakhot 41a-b — "each food
that precedes in the verse precedes in the blessing"; 44a Rabban Gamliel's after-blessing) the exam's rows; the first fruits from the seven species
(Mishnah Bikkurim 1:3 — the Sifrei 297:4's I2; Menachot 84a-b; Tosefta Bikkurim 2:8 the seven vessels) the exam's rows; the measures from the verse
(Eruvin 4a, Sukkah 5b — "a land of wheat and barley …" the measures' seats, the Rambam's row) a DATA row the_measures_seat; HONEY WITHOUT MILK a DATA row.
(c) THE MANNA AND THE HUMBLING — F2's the_manna and the_humbling: the rows 8:3 TURNED and 8:16 EXPANDED against manna_fell (exodus_story.manna by CALL
— forty_years, day_by_day; beha.taberah_and_quail by CALL for the craving's description); Yoma 74b-76a's readings ("afflicted you" as the affliction of
Yom Kippur — the school of R. Yishmael; the manna's tastes and forms; the sixty cubits) the exam's rows; no write (manna_provided stands — CU5).
(d) THE FORTY YEARS AS A STATE — F2's the_garment_and_the_foot: the fifth form's row SUPPLIED (above); the forty years' decree the row 8:2 EXPANDED
(shelach.decree('day_for_year') by CALL); the two [40]s the parser's (no rule); Sanhedrin 99a's forty (the messianic era) the exam's row.
(e) THE DISCIPLINE — F2's the_discipline: the row 8:5 VARIANT against 1:31's carrying (opening_speech by CALL); Berakhot 5a's afflictions of love (8:5
and 8:7 — the Torah, the Land, the world to come through suffering; the Sifrei 32:10-15 CREDITED) the exam's rows; no write.
(f) "TAKE HEED LEST" — F4's take_heed_lest: the code's hole — the WRITE forgetting_barred, a BLOCK on Israel (NEW), at the chapter's second line
forgetting_warned (8:11-18 — the warning, the growth, the heart, the chain, the boast, the covenant); the row 8:11 VERBATIM against 6:12 by CALL; "take
heed, lest, do not" a negative command (Makkot 13b; Eruvin 96a — the rule's exhibit) the exam's rows.
(g) THE HEART LIFTED UP — F4's the_heart_lifted: Sotah 4b-5a (arrogance as denial of the core belief — 8:11-14 the source; "filling his stomach" Berakhot
32a) the exam's rows; 17:20 the king's law by CALL when chapter 17 compiles (OWED forward); a DATA row the_kings_law_tokens (8:13 / 17:17).
(h) THE EXODUS FORMULA — F4's the_exodus_formula: the row 8:14 VERBATIM against brought_out by kind (5:6, 6:12, 13:6, 13:11 the formula's seats — the
second word's header by CALL); no write.
(i) THE SERPENTS AND THE ROCK — F5's the_serpents and the_rock_of_flint: the rows 8:15 EXPANDED and VARIANT against fiery_serpents_sent and rock_struck by
kind (chukat.arad_and_the_serpent and chukat.meribah by CALL; exodus_story's 17:6); the two rocks' two words a DATA row the_two_rocks; no write
(serpents_sent and water_from_the_rock stand — CU5).
(j) "MY POWER AND THE MIGHT OF MY HAND" — F5's my_power_my_hand: a DATA row (the boast; the Sifrei 48:10's "not by bread alone" reading; Sotah 4b-5a);
"He gives you power to get wealth" the answer — no write.
(k) THE COVENANT ESTABLISHED — F5's the_covenant_established: the row 8:18 VERBATIM against the oath's three lines by kind (seven_nations.the_holy_people
('the_oath') by CALL — 7:8's form; mamre and joseph the lines' runners); no write.
(l) THE TESTIMONY — F6's i_testify and like_the_nations: the rows 8:19 VARIANT (witnesses_called by kind; obey_horeb.the_exile_case by CALL), 8:19
VARIANT (the second word by CALL — the serve/bow order a DATA row), 8:20 TURNED (nations_devoted by kind; the heel's second seat by CALL); the WRITE at
the chapter's third line perishing_testified (8:19-20): {('the effect witnesses_called writes, REUSED — no new effect' if N_EFF == 1031 else 'perishing_testified NEW, a conditional HEAVEN entry on Israel (the form of blessings_for_hearing, turned)')}.
(m) THE KING'S LAW'S TOKENS — a DATA row the_kings_law_tokens (8:13 "silver and gold shall multiply for you" / 17:17 "he shall not multiply"; 8:14 /
17:20 the heart lifted); the pair's CALL when chapter 17 compiles (OWED forward, with the heart's).
(n) THE DOCKET by the union rule — the scan's 34 link rows + the Mishnah rows (24) + the ranges declared above (417 topic rows; 451 in all; 101
credited) in THREE parts A-C — LAW / DERIVATION / DISPUTE / CONTEXT / OUTSIDE, EVERY ROW WHOLE; the crowns expected: the grace after meals from the
Torah and its four blessings (48b; 21a; 20b's measure); the blessing before by inference and the zimmun (35a; Tosefta 6:1-2); the measure of
"satisfied" (49b; Mishnah 7:2); the order of blessings by the verse and its two "land"s (41a-b; 44a); the first fruits from the seven species (Bikkurim
1:3; Menachot 84a-b; Tosefta Bikkurim 2:8); the measures from the verse (Eruvin 4a; Sukkah 5b); "afflicted you" and the manna's forms (Yoma 74b-76a);
arrogance as denial (Sotah 4b-5a); "take heed, lest" a negative command (Makkot 13b; Eruvin 96a); the afflictions of love (Berakhot 5a); the messianic
forty years (Sanhedrin 99a); the pepper tree and Rabbi Meir's fruit (Sukkah 35a; Yoma 81b on 8:9); the stones of iron as the scholars (Taanit 4a);
"she'era" (Ketubot 47b on 8:3 — a lexical link); the grace in any language (Sotah 33a).

THE CELLS (six, matching the reading's six claims; each returning out(verdict, effects); the INK block exec'd from the sequence file; the token probes
zero-report; every seat list typed from the reading's print and the recon): F1 the_frame (8:1 — asks: all_the_commandment (the eight seats), live_and_possess
(4:1 by CALL — the row), the_oath_seats (8:1, 8:18 — "swore" no number), no_receipt (the register gate's finder called — no seat)); F2
the_way_of_forty_years (8:2-6 — asks: forty_years (the two [40]s; decree_declared by kind — the row; shelach by CALL), the_test (16:4 by CALL — the row;
the interrogative he), the_humbling (the verb's seven seats), the_manna (manna_fell by kind — the rows 8:3, 8:16; exodus_story.manna and
beha.taberah_and_quail by CALL), not_by_bread_alone (DATA — the crown), the_garment_and_the_foot (SUPPLIED — the fifth form; the ledger scan asserted),
the_discipline (1:31 by CALL — the row), keep_walk_fear (10:12 forward — DATA)); F3 the_good_land (8:7-10 — asks: the_good_land (the twelve seats; 6:10-11
and 6:3 by CALL — the row), the_waters (springs and deeps — the one seat), the_seven_species (8:8 alone; (b)), honey_without_milk (DATA), lack_nothing
(2:7 by CALL — the row), iron_and_copper (the seats), eat_be_satisfied_bless (a — THE WRITE bless_after_eating_commanded; the measure a PARAMETER)); F4
take_heed_lest_you_forget (8:11-14 — asks: take_heed_lest (f — the row; THE WRITE forgetting_barred), the_triad (7:11 by CALL — seven_nations.
the_faithful_god('the_triad')), the_growth_list (6:10-11 by CALL — the row VARIANT; the king's law's tokens DATA), the_heart_lifted (g — DATA; Sotah),
the_exodus_formula (h — the row)); F5 the_chain_and_the_covenant (8:15-18 — asks: the_wilderness (1:19 by CALL — the great and terrible), the_serpents (i —
the row), the_rock_of_flint (i — the row; the two rocks), the_manna_to_do_you_good (c — the row 8:16), my_power_my_hand (j — DATA), the_covenant_established
(k — the row)); F6 the_testimony (8:19-20 — asks: if_you_forget (the infinitive absolute — the one seat), other_gods_serve_bow (l — the row; the serve/bow
order DATA), i_testify (l — the row; THE WRITE), like_the_nations (l — the row TURNED), the_heel (7:12's cell by CALL — the second seat), hearken_plural
(8:20 the one plural — the ten seats)). The readback table the_readback (the eighteen rows, the SUPPLIED grade, the three holes).

THE DATA ROWS (fourteen): the_readback, not_by_bread_alone (c), the_garment_and_the_foot (d — the state, the span, the ledger scan), honey_without_milk (b),
the_seven_species_seat (b — 8:8 alone; the five three-or-more seats), the_measures_seat (b — Eruvin 4a, Sukkah 5b), the_kings_law_tokens (m), my_power_my_hand
(j), the_written_read_pair (8:2 — the store's extra token), the_interrogative_he (8:2 — the book's one), the_two_rocks (i — Exodus' word, Numbers' word),
the_serve_bow_order (l — the ten seats), the_ten_uncited (the scan's verses cited by no one), the_credits (the 101 addresses — the Numbers walk's and the
earlier dockets' Berakhot rows).

THE DAEMON law_good_land (given_at Deut 8:1; installed_by boot): watches grace_commanded → [bless_after_eating_commanded]; forgetting_warned →
[forgetting_barred]; perishing_testified → [{('the reused effect' if N_EFF == 1031 else 'perishing_testified')}]; good_land_case → [accepted, exempt, lashes]. No
timer; literal W dicts per kind; the case kind dispatching to the cells by name in EXPLICIT branches.

THE TYPES (add_types_ch8.py from add_types_ch7.py): THREE tape kinds — grace_commanded (statute by form, 8:7-10; the good land's clause, the seven species
in the row, the command "eat, be satisfied, bless"), forgetting_warned (statute by form, 8:11-18; the warning, the growth's list, the heart, the chain, the
boast, the covenant established), perishing_testified (statute by form, 8:19-20; the case "if you surely forget", the testimony, the measure for measure)
— ONE case kind (good_land_case); the new effects — bless_after_eating_commanded (status on Israel; 8:10), forgetting_barred (block on Israel; 8:11){(', perishing_testified (heaven on Israel, conditional; 8:19)' if N_EFF == 1032 else '')};
the effects reused — accepted, exempt, lashes{(', the witnesses-line effect at 8:19' if N_EFF == 1031 else '')}; NO registry row (Israel the written-on party; the manna, the rock and the
serpent already rows, untouched); the daemon block; the functions block good_land (the six cells WRAPPED); the span [[Deut, 8, 1, 20]]; the CALL edges by
the ink — obey_horeb (4:1, 4:9, 4:26), exodus_story (the manna, the rock at 17:6, the exodus, the trials), shelach (the decree), beha (the craving's
manna), chukat (Meribah, the serpents), hear_o_israel (6:3, 6:10-12), opening_speech (1:19, 1:31, 2:7), covenant_at_horeb (the second word; 5:6),
seven_nations (7:8's oath, 7:11's triad, 7:12's heel, the ban), ordinances (23:25 — the Sifrei 40:10's kin), sanctions (Leviticus 18:5 — "and live by
them" for 8:1 and 8:3's living), mamre and joseph (the oath's lines), decalogue (20:3-6); the pointers a PREDICTION only — RUN_CITATION at 8:2 and
8:4 (the decree), 8:3 and 8:16 (the manna), 8:14 (the exodus), 8:15 (the serpents, the rock), 8:18 (the oath), 8:19 (4:26): every demand the census makes
past the imports read on the DB and declared, never a blanket row (4b's and 5b's lesson: the census decides); I5 67 → 68.

THE TAPE (three lines, NO marker): under "# ---- Deut 8 ----" after the tape's last Deuteronomy 7 line: grace_commanded (8:7-10), forgetting_warned
(8:11-18), perishing_testified (8:19-20), all on the counter's own day (40, 11, 1), page_order. The markers 167 UNMOVED; the closes 127 UNMOVED; the
counter ends at (40, 11, 1) UNMOVED. THE READBACK'S ROWS WRITE NOTHING (8:1-6 and 8:14-18 reference rows; the manna's, the rock's and the serpents'
entries stand).

THE CHECKPOINTS CU1-CU9 (the prefix measured free — the last of its series):
CU1 THE LINES — three events of the sitting's kinds on the tape in the ink's order, all AFTER the tape's last Deuteronomy 7 line, all on the counter's day
(40, 11, 1), NO marker added (markers 167); the counter ends at (40, 11, 1).
CU2 THE BLESSING — bless_after_eating_commanded on israel_people ONE (a status), source beginning "Deut 8:10"; law_good_land registered, given_at Deut
8:1, installed_by boot; the functions block's six cells WRAPPED.
CU3 THE FORGETTING — forgetting_barred on israel_people ONE (a block; its first tape write — 6:12's cell called, no write there), source beginning "Deut 8:11".
CU4 THE READBACK OF A STATE — the_readback's rows eighteen, every reference row's entry FOUND: the tape lines by kind and first verse (decree_declared at
Num 14:26, manna_fell at Exod 16:13, brought_out at Exod 12:51, fiery_serpents_sent at Num 21:6, rock_struck at Exod 17:6, rock_struck_twice at Num
20:10, sworn_by_himself at Gen 22:16, oath_upheld at Gen 26:3, visitation_promised at Gen 50:24, witnesses_called at Deut 4:26, nations_devoted at Deut
7:1) and the kin's cells by CALL (each returning its verdict on its own ask); the grades' census typed from the runner's print (VERBATIM 6, VARIANT 5,
EXPANDED 4, TURNED 2, SUPPLIED 1 predicted); the one SUPPLIED row the garment's — no entry on any ledger, asserted; no row OPEN; the three holes named.
CU5 THE KIN STANDS — manna_provided, water_from_the_rock, serpents_sent UNMOVED (the readback references, no second write); shema_commanded ONE and
test_barred ONE UNMOVED; other_gods_barred ONE UNMOVED (the cell CALLED); blessings_for_hearing ONE UNMOVED; treasured_people UNMOVED.
CU6 THE TESTIMONY — {('the witnesses-line effect on israel_people +1 at source "Deut 8:19" (the reuse), the 4:26 entry UNMOVED' if N_EFF == 1031 else 'perishing_testified on israel_people ONE (heaven, conditional), source beginning "Deut 8:19"; the 4:26 line witnesses_called UNMOVED')}.
CU7 THE STATE — no effect naming a garment, clothing, a shoe or a swelling on israel_people (the SUPPLIED grade's assertion, run on the world); the
readback's SUPPLIED row names the span and the scan.
CU8 THE WILDERNESS READ BACK — brought_out ONE, manna_fell ONE, rock_struck ONE, rock_struck_twice ONE, fiery_serpents_sent ONE, decree_declared ONE
UNMOVED; nothing written on Egypt, the manna, the rock, the serpent (their registry rows untouched).
CU9 THE REST — entities 319 UNMOVED, closes 127, markers 167, the population table 148 UNMOVED, the three kinds present; the other counts 5b's exactly
with the three lines and the daemon's three writes dropped (THE REST test — NO declared delta this sitting: the daemon writes only on its own lines).
NO retype of the older REST literals expected (closes and markers unmoved; no debit on Israel this chapter — the 5b lesson's commanded-count literals
untouched: the three writes a status, a block and a heaven entry; checked by grep before the tape); every miss shown at once by checkpoint_check.py --all
AFTER the tape (4b's lesson: the tape first when the tape grows).

THE PREDICTION'S ARITHMETIC: RUN = (1310, 96, 88, 0, 12, 1605, 39, 319, the four pairs, 127) — events +3 (the three lines), timers set +0, fired +0 (no
clock walk), cancels 0, retro-writes 12 UNMOVED, writes +3 (the daemon's watches summed: one per line), daemons fired +1 (law_good_land), entities +0,
closes +0; PREVIOUS_RUN = 5b's RUN EXACTLY (1307, 96, 88, 0, 12, 1602, 38, 319, the four pairs, 127): THE REST drops the three lines by the runner's tag and
the span and the daemon's three writes with them — no delta; NEWEST_RUNNER 'good_land'; PLACEMENT markers UNMOVED ({{'text_constrained': 106,
'reading_placed': 46}}), events page_order 1143 → 1146 (text_constrained 109, reading_placed 55 unmoved) — read at the stitcher's print; CENSUS typed from
the stitcher's print (on tape 1307 → 1310, history +3, kinds 852 → 855 — the three tape kinds, subjects 272 UNMOVED, markers 167 (F 129, R 23), closes 71
unmoved; the case rows the exam's persons); the population table 148 UNMOVED; the scene's tuple PREDICTED BY SCRIPT at the runner step (the exam's persons
through good_land_case — each written once; no timer; no close); the narrative's (on its own world: 3 writes, 0 closes, the entities israel = 1, the
counter's day (11, 1), 0 dated lines, no row).

THE PROBES (RUN B's first step): readback_probes.py Q19-Q21 written to FAIL before the runner exists — Q19 the runner and its the_readback table (eighteen
rows; the census VERBATIM 6 / VARIANT 5 / EXPANDED 4 / TURNED 2 / SUPPLIED 1; every reference row's entry found — the tape lines by kind and verse, the
kin's cells by CALL; the one SUPPLIED row the garment's, with the ledger scan's empty result; the three holes named), Q20 the three lines on the counter's
day with NO marker (markers 167 after the run) and the three writes on Israel with their sources (the status, the block, the testimony's entry), Q21 the
kin stands — manna_provided, water_from_the_rock, serpents_sent, shema_commanded, test_barred, other_gods_barred, blessings_for_hearing UNMOVED, no second
write; Q16-Q18 unchanged; NO parser rule this sitting (the two number verses read right at the reading — census_probes unmoved at 224); the register gate
unchanged; checkpoint_probes' verse computed (2b's form).

THE ORDER: this design → the state doc's checkpoint (#196 addendum 2 — RUN A closed) → THE DOCKET, ITS OWN RUN: the dump (ch8_docket_dump.txt, written
by the scan — 34 link + 417 topic rows, 101 credited); the rows read WHOLE in three parts A-C on 5b's whole-row instruments (ch7_docket_A-D.py with
ch7_docket_common.py and the WHOLE overlays the forms: the address, the kind, the row entire); the verdicts LAW / DERIVATION / DISPUTE / CONTEXT /
OUTSIDE with the crowns the design expects; the writer write_ch8_docket.py from write_ch7_docket.py by sed with the coverage computed and the cite index
→ the checkpoint (#196 addendum 3) → RUN B: the probes to FAIL (Q19-Q21 0/3) → the types by script (add_types_ch8.py) → the recorder and the stitcher
(the scratch copies: SPAN_ORDER + 'good_land'; no marker row) → the runner (ch8_part1-4.py assembled by cat; the fast checker over parts 1 and 2; the
honest-pairing guard; zero-report probes; the scene and the narrative predicted by script; CASES generated from the cells' asks) → the recorder → the
stitcher → the literals CU1-CU9 (patch_seq_literals_ch8.py) → the tape run (10/10 with THE REST) → `checkpoint_check.py --all` AFTER the tape →
`gates_chain.sh` in the background (one summary: the probe gates incl. readback Q19-Q21 to 21/21, the daemon and dependency gates, build_world, the
journal gate, THE REGISTER GATE --strict unmoved, the positions table 244 → 253, checkpoint_probes, the sweep 63 runners, the journal gate again) → the
records from the sheet in one call (this section's AS BUILT, COMPILE_DEBT's sitting-6 box PAID + the 6b box with the king's law's tokens and the heart
owed forward and the prefix note, MOVE_CATALOG (checked), MIDDOT's docket entries, MISHNAH_TOPICS (Berakhot 6-7, Bikkurim 1 READ), RESEARCH_LOG,
THE_STEPS, THE_BRIEFING, THE_LOOP.md's step 6 row (the fifth form — the retelling of a state), RESUME, memory, the state doc's addendum, the recovery page
rewritten, the addenda's section) → the forms copied → the commit message for the owner's word.
'''
DESIGN = DESIGN_A + DESIGN_B
STATE = f'''
#196 ADDENDUM 2 ({DATE} — RUN A OF SITTING 6b CLOSED, on the owner's "Next" after sitting 6's close (the tree uncommitted since 29c189b — the reading's message drafted, his word not yet given): THE COMPILE OF CHAPTER 8 — the rereads, the measurements, the design). THE REREADS: THE_STEPS' compiler block and Step 5's head, the map's "Sitting 5b — AS BUILT" and the 5b design's writer (the compile's form), the 6b box (a)-(n). THE MEASUREMENTS (ch8_compile_recon.py → ch8_recon.out 381 KB, read by section; ch8_docket_scan.py → ch8_scan.out and the dump ch8_docket_dump.txt 1,355 lines; the one database's run_ledger queried): every act the chapter retells is on the tape (manna_fell, rock_struck and rock_struck_twice, fiery_serpents_sent, decree_declared with years 40, brought_out, the oath's three lines, witnesses_called at 4:26, the craving's lines) and the garment's forty years on none — a STATE, not an act; the kin's cells in the code (exodus_story.manna / trials / marah, beha.taberah_and_quail, shelach.decree, chukat.meribah / arad_and_the_serpent, ordinances.land's bread_water, opening_speech's forty_years_lacking_nothing and the_carrying, obey_horeb's hear_and_do / take_heed_lest_you_forget / the_exile_case, hear_o_israel's lest_you_forget and the_list, covenant_at_horeb's second word, seven_nations' the_oath / the_heel / the_ban); the registry's effects manna_provided, water_from_the_rock, serpents_sent, bread_and_water_blessed PRESENT on the world; NO effect and NO cell for the blessing after the meal, the forgetting barred (6:12's cell has the ask and no write), the discipline, the garment — THE CODE'S HOLES; the testimony's effect read from law_obey_horeb's watches ({TESTI[:120]}…); the prefix CU free — THE LAST of the two-letter series (a note owed forward); the counts markers 167 / closes 127 / entities 319 / daemons 67 unmoved before the tape; the docket 34 link rows in 17 works + the topic ranges sized (Berakhot 5a, 20b-21a, 35a-35b, 41a-44a, 48b-49b; Yoma 74b-76a; Sotah 4b-5a; Makkot 13b; Eruvin 96a; Mishnah Berakhot 6-7; Bikkurim 1 — 417 rows, every range whole; Berakhot 35a-49b's other amudim 309 rows enumerated outside declared scope; 451 rows in all, 101 credited; ten verses of the chapter cited by no one). THE DESIGN written into the map: "Sitting 6b — THE COMPILE OF CHAPTER 8 … THE DESIGN" — the runner cold_run_good_land.py (the 63rd), the daemon law_good_land (given_at Deut 8:1, boot), THREE tape lines and NO marker (grace_commanded 8:7-10, forgetting_warned 8:11-18, perishing_testified 8:19-20), the new effects bless_after_eating_commanded (a status) and forgetting_barred (a block) with the testimony's by the watches read, six cells, fourteen DATA rows, THE READBACK'S FIFTH FORM — THE RETELLING OF A STATE (eighteen rows, VERBATIM 6 / VARIANT 5 / EXPANDED 4 / TURNED 2 / SUPPLIED 1 predicted; the garment graded SUPPLIED with no retrograde write — the design's decision, open to the owner), the decisions (a)-(n), CU1-CU9, RUN (1310, 96, 88, 0, 12, 1605, 39, 319, the four pairs, 127) and PREVIOUS_RUN 5b's exactly. THE DOCKET ITS OWN RUN — by the window's budget (this run had spent its 300k on the reading's close before the design), not by the row count (451, under the ~700 clause): the two-run rule's docket clause applied and named. NOTHING MID-FLIGHT — A CLEAN COMPACTION POINT. The tree: sitting 6 whole and the two-run rule's records (uncommitted; the commit message at <scratch>/commit_msg_ch8.txt still stands for the reading — the design rides the next message), the map, the state doc, the recovery page, the memory. THE SESSION NOTE stands: the shell's grep function is broken in this session — /usr/bin/grep by path. THE WORD FOR THE NEXT SITTING — THE DOCKET OF 6b, its first step: the dump already written (<scratch>/ch8_docket_dump.txt — 1,355 lines; the scan ch8_docket_scan.py in the scratchpad, its print ch8_scan.out); the rows read WHOLE in three parts A-C on 5b's whole-row instruments (World/step9/forms_deuteronomy_walk/ch7_docket_A-D.py and ch7_docket_common.py with their WHOLE overlays — the forms; the address, the kind, the row entire), the verdicts LAW / DERIVATION / DISPUTE / CONTEXT / OUTSIDE with the crowns the design expects; write_ch8_docket.py from write_ch7_docket.py by sed (the coverage computed, the cite index; the ledger logic/oral_triage/deu_08_ekev_exam_2026-09-18.md); the checkpoint #196 addendum 3. POST-COMPACTION REREADS: the recovery page, the map's "Sitting 6b … THE DESIGN" (the newest section), MEMORY.md; then THE_STEPS Step 5 for the docket's verdict forms if needed.
'''
MN = f'''
SITTING 6b RUN A DONE {DATE} (on "Next" after sitting 6's close; the tree uncommitted since 29c189b): the measurements (ch8_compile_recon.py, ch8_docket_scan.py, the one database) and THE DESIGN in the map ("Sitting 6b — THE COMPILE OF CHAPTER 8 … THE DESIGN"): the runner cold_run_good_land.py (the 63rd), the daemon law_good_land (boot, given_at Deut 8:1), three tape lines (grace_commanded 8:7-10, forgetting_warned 8:11-18, perishing_testified 8:19-20) and NO marker, the new effects bless_after_eating_commanded and forgetting_barred (the code's holes — no cell anywhere for the grace after meals; 6:12's cell had no write), THE READBACK'S FIFTH FORM — the retelling of a STATE: the garment graded SUPPLIED with no retrograde write (the design's decision, open to the owner), eighteen rows predicted VERBATIM 6 / VARIANT 5 / EXPANDED 4 / TURNED 2 / SUPPLIED 1; CU1-CU9 (CU the LAST free prefix — the next compile opens a new series, owed forward); RUN (1310, 96, 88, 0, 12, 1605, 39, 319, the four pairs, 127). The docket 451 rows (34 link + 417 topic; 101 credited) — ITS OWN RUN by the window's budget. Clean point (#196 addendum 2). NEXT: the docket in three parts, EVERY ROW WHOLE, write_ch8_docket.py; then RUN B.
'''
plans = []
P = f'{ROOT}/World/step9/DEUTERONOMY_WALK.md'; s = rd(P); assert '## Sitting 6b — THE COMPILE OF CHAPTER 8' not in s and s.rstrip().endswith('Then chapter 9, and on in order.')
plans.append((P, s.rstrip('\n') + DESIGN))
P = f'{ROOT}/logic/pre_logic_methods_2026-07-28/PROMPT_continue_solo_era_2026-08-06.md'; s = rd(P); assert '#196 ADDENDUM 2' not in s and '#196 ADDENDUM 1' in s
plans.append((P, s.rstrip('\n') + STATE))
P = f'{ROOT}/logic/pre_logic_methods_2026-07-28/RECOVERY_new_thread_2026-09-12.md'; s = rd(P)
old = '- NEXT ON HIS WORD: the commit; then 6b — THE COMPILE OF CHAPTER 8 in TWO runs (the debt box its list), or the schema sitting.\n'
new = '- IN FLIGHT: 6b RUN A DONE (the design in the map); NEXT: the docket WHOLE (its own run), then RUN B. The commit on his word.\n'
assert s.count(old) == 1; s2 = s.replace(old, new); assert len(s2.encode()) <= 10240, len(s2.encode()); plans.append((P, s2))
P = f'{MEM}/deuteronomy-walk.md'; s = rd(P); assert 'SITTING 6b RUN A DONE' not in s
plans.append((P, s.rstrip('\n') + '\n' + MN))
P = f'{MEM}/MEMORY.md'; s = rd(P)
old = 'SITTING 6 DONE 2026-09-18 (ch 8 FROZEN, 222 units); NEXT: commit, then 6b'
new = 'SITTING 6 DONE 2026-09-18 (ch 8 FROZEN, 222 units); 6b RUN A DONE; NEXT: the docket'
assert s.count(old) == 1, s.count(old)
s2 = s.replace(old, new); assert len(s2.encode('utf-8')) < 17000, len(s2.encode('utf-8'))
plans.append((P, s2))
for p, s2 in plans: assert s2 != rd(p), p
if CHECK:
    for p, s2 in plans: print('WOULD WRITE', p.replace(ROOT, '<repo>').replace(MEM, '<memory>'), len(rd(p)), '->', len(s2))
    sys.exit(0)
for p, s2 in plans:
    open(p, 'w', encoding='utf-8').write(s2); print('WROTE', p.replace(ROOT, '<repo>').replace(MEM, '<memory>'), len(s2.encode('utf-8')))
print('the 6b design and the run A checkpoint written')
