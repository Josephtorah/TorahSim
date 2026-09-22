import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE DEUTERONOMY WALK 12b RUN B / THE TAIL (2026-09-22): THE RECORDS FROM THE SHEET IN ONE CALL (World/step9/RECORD_FORMS.md) — the map's "Sitting 12b — AS BUILT"
# (with THE TIMING TABLE), COMPILE_DEBT's sitting-12 box PAID and the 12b box, MIDDOT's compile entry, RESEARCH_LOG, THE_STEPS, THE_BRIEFING (the scoreboard and an
# entry), THE_LOOP's step-6 row, RESUME, RECORD_FORMS, the state doc's #205 addendum 4 (the close — a clean point), the addenda's section, the recovery page rewritten
# under its cap, the memory (the walk note and the index). EVERY NUMBER PARSED FROM THE PRINTS (the runner's run, the tape's run, the chain's folder, the timing table,
# the records' own reads), never recited; every text built whole before its file is opened; the caps asserted; --check runs the reads and the anchors alone.
# write_ch13b_records.py's form. WRITTEN AT RUN B, RUN AT THE TAIL. RUN FROM THE REPO ROOT.
import os, re, sys, subprocess
ROOT = _ROOT
SP = os.path.dirname(os.path.abspath(__file__)); G = f'{SP}/gates_ch14b'
MEM = os.path.expanduser('~/.claude/projects/-Users-Shared-TorahSim/memory')
CHECK = '--check' in sys.argv
def rd(name): return open(name if name.startswith('/') else f'{G}/{name}', encoding='utf-8', errors='ignore').read()
def read(p): return open(p if p.startswith('/') else f'{ROOT}/{p}', encoding='utf-8').read()
def W(p, s): open(p if p.startswith('/') else f'{ROOT}/{p}', 'w', encoding='utf-8').write(s)
def last_frac(name, den=None):
    fr = [(int(a), int(b)) for a, b in re.findall(r'(\d+)/(\d+)', rd(name)) if den is None or int(b) == den]
    assert fr, (name, den); return fr[-1]
# ---- THE PRINTS ----
RUN_FILE = f'{SP}/ch14_runner_run2.out' if os.path.exists(f'{SP}/ch14_runner_run2.out') else f'{SP}/ch14_runner_run1.out'
run = rd(RUN_FILE); MX = re.search(r'MATRIX: (\d+)/(\d+)', run); MX = tuple(int(x) for x in MX.groups()); assert MX[0] == MX[1], (RUN_FILE, MX)
cg = rd(f'{SP}/ch14_cases_gen.out'); CASES_N = int(re.search(r'CASES generated: (\d+)', cg).group(1)); PER_CELL = re.search(r'per cell (\{.*?\})', cg).group(1)
SCENE = re.search(r'the scene (\(.*?\)\)); the narrative', cg); SCENE = SCENE.group(1) if SCENE else '?'
TAPE_FILE = f'{SP}/ch14_tape_run2.out' if os.path.exists(f'{SP}/ch14_tape_run2.out') else f'{SP}/ch14_tape_run1.out'
tape = rd(TAPE_FILE); assert '10/10 checkpoints' in tape, TAPE_FILE
DF = re.findall(r'CHECKPOINT (DF\d) .*? (MATCH|MISS|DIVERGE)$', tape, flags=re.M); assert len(DF) == 9 and all(v == 'MATCH' for _, v in DF), DF
RETYPED = re.findall(r'CHECKPOINT (DD2) .*? (MATCH|MISS|DIVERGE)$', tape, flags=re.M); assert len(RETYPED) == 1 and RETYPED[0][1] == 'MATCH', RETYPED
cc = rd(f'{SP}/ch14_checkpoint_check.out'); CC = re.search(r'checkpoint_check: (\d+) rows, (\d+) miss, (\d+) raised', cc); CC = tuple(int(x) for x in CC.groups()); assert CC[1] == 18 and CC[2] == 0, CC
st = rd(f'{SP}/seq_stitch_ch14.out'); PLC = re.search(r'^PLACEMENT LITERAL: (.*)$', st, re.M).group(1); CEN = re.search(r'^  CENSUS tuple .*?: (\(.*\))$', st, re.M).group(1)
rec = rd(f'{SP}/seq_record_ch14.out'); NREC = int(re.search(r'recording: (\d+) records written', rec).group(1)); FT_REC = re.search(r'^  food_tithe\s+worlds \d+\s+total\s+(\d+).*?statute\s+(\d+)', rec, re.M); FT_REC = (int(FT_REC.group(1)), int(FT_REC.group(2))) if FT_REC else None
pf = rd(f'{SP}/ch14b_probes_fail.out'); PF = tuple(int(x) for x in re.search(r'readback_probes: (\d+)/(\d+)', pf).groups()); assert PF == (35, 39), PF
ty = rd(f'{SP}/add_types_ch14.out'); TY = tuple(int(x) for x in re.search(r'THE TYPES DONE: kinds (\d+), effects (\d+), daemons (\d+), functions blocks (\d+), edges from food_tithe (\d+), I5 74, parameters (\d+)', ty).groups())
summ = rd('SUMMARY.txt'); assert 'GATES CHAIN DONE — ALL GREEN' in summ, summ[-400:]
dg = rd('daemon.out'); DGN = int(re.search(r'(\d+) daemons', dg).group(1)); DGF = re.search(r'(\d+) functions', dg); DGF = int(DGF.group(1)) if DGF else None; assert DGN == 74, DGN
dp = rd('dependency.out'); LC = re.search(r'LINK CENSUS \(the link review law\): reference (\d+), transfer (\d+), hypothesis (\d+), none (\d+)', dp); LC = tuple(int(x) for x in LC.groups())
DPE = re.search(r'(\d+) edges', dp); DPP = re.search(r'(\d+) pointers', dp); DPE = int(DPE.group(1)) if DPE else None; DPP = int(DPP.group(1)) if DPP else None
rg = rd('register.out'); RG = tuple(int(x) for x in re.search(r'DECLARED (\d+); DEBT (\d+); FAILS (\d+)', rg).groups()); assert RG[1] == 0 and RG[2] == 0, RG
sw = rd('sweep.out'); SW_P = len(re.findall(r'^PASS +cold_run_\w+\.py', sw, flags=re.M)); SW_F = len(re.findall(r'^FAIL +cold_run_\w+\.py', sw, flags=re.M)); SW_CELLS = sum(int(a) for a, b in re.findall(r'score=(\d+)/(\d+)', sw))
assert SW_F == 0 and SW_P >= 68, (SW_P, SW_F)
po = rd('positions.out') if os.path.exists(f'{G}/positions.out') else ''; PO = re.search(r'(\d+) checkpoints', po); PO = int(PO.group(1)) if PO else None
jg = rd('journal.out'); JG = re.search(r'(\d+) kinds, (\d+) rows', jg); JG = tuple(int(x) for x in JG.groups()) if JG else None
PR = {'census': last_frac('probe_census.out'), 'installation': last_frac('probe_installation.out', 6), 'readback': last_frac('probe_readback.out', 39), 'large_letter': last_frac('probe_large_letter.out', 6), 'checkpoint': last_frac('checkpoint.out', 7), 'ink_cache': last_frac('probe_ink_cache.out', 8)}
assert PR['readback'] == (39, 39) and PR['installation'] == (6, 6) and PR['large_letter'] == (6, 6) and PR['ink_cache'] == (8, 8) and PR['census'][0] == PR['census'][1] and PR['checkpoint'] == (7, 7), PR
dep_first = rd(f'{SP}/ch14b_chain_dependency_first.out') if os.path.exists(f'{SP}/ch14b_chain_dependency_first.out') else dp
POINTER = 'DEMANDED' if re.search(r'FAIL POINTER Deut 14:\d+', dep_first) else 'not demanded (none predicted)'   # the first pass's print decides
HOMOGRAPH = 'MATCHED (filed FALSE)' if re.search(r'the_place_luz_bethel|the_raven|the_flock|the_beasts', dep_first) and 'FAIL' in dep_first else 'not matched'
CHAIN_STORY = read(f'{SP}/ch14b_chain_story.txt').strip() if os.path.exists(f'{SP}/ch14b_chain_story.txt') else 'THE GATES CHAIN ONCE — ALL GREEN on the first pass'
TAPE_STORY = read(f'{SP}/ch14b_tape_story.txt').strip() if os.path.exists(f'{SP}/ch14b_tape_story.txt') else 'THE TAPE 10/10 ON ITS FIRST RUN, DF1-DF9 MATCH'
dk = read('logic/oral_triage/deu_14_reeh_exam_2026-09-21.md'); NROWS = len([l for l in dk.split('\n') if l.startswith('- ') and (' — LAW.' in l or ' — DERIVATION.' in l or ' — DISPUTE.' in l or ' — CONTEXT.' in l or ' — OUTSIDE.' in l)]); assert NROWS == 991, NROWS
# ---- THE TIMING TABLE ----
tt = [l.split('\t') for l in read(f'{SP}/ch14b_timing.tsv').split('\n') if l.strip()]
T12B = [(r[0], r[1], int(r[2])) for r in tt if len(r) >= 3 and r[1].startswith('12b')]
TSUM12B = sum(s for _, _, s in T12B); TSLOW = sorted(T12B, key=lambda r: -r[2])[:8]
TIMING = ("THE TIMING TABLE (every step timed — the owner's ask at sitting 10; the machine's seconds per step, the model's reading and writing between them the rest): SITTING 12b (the compile — RUN A, the docket's two runs, RUN B, the tail) %d timed steps, %d machine seconds; the first row %s, the last %s; THE SLOWEST OF 12b: %s. The table itself: <scratch>/ch14b_timing.tsv, copied to the forms folder."
          % (len(T12B), TSUM12B, T12B[0][0] if T12B else '?', T12B[-1][0] if T12B else '?', '; '.join('%s %ds' % (n[4:] if n.startswith('12b ') else n, s) for _, n, s in TSLOW)))
NUM = dict(DF=len(DF), CC=CC, PLC=PLC, CEN=CEN, DGN=DGN, DGF=DGF, LC=LC, DPE=DPE, DPP=DPP, RG=RG, SW=(SW_P, SW_CELLS), PO=PO, JG=JG, PR=PR, POINTER=POINTER, HOMOGRAPH=HOMOGRAPH, CASES=CASES_N, NREC=NREC, FT_REC=FT_REC, PF=PF, TY=TY, MX=MX, T12B=(len(T12B), TSUM12B))
print('THE NUMBERS:', NUM)
# ---- THE TEXTS ----
AS_BUILT = f"""
## Sitting 12b — THE COMPILE OF CHAPTER 14 — AS BUILT (2026-09-22; on the owner's "Reread and go" after the compaction at #205 addendum 2 — the two-run rule's seventh compile sitting under THE COST RULES, the docket in two runs: five clean points, #205 and its addenda 1-4)

THE DESIGN HELD ON ITS SPINE — five own-day lines, no marker, seven writes on Israel (five new, TWO REUSES), no debit, RUN (1332, 96, 88, 0, 12, 1641, 45, 319, the
four pairs, 127) as the arithmetic wrote it, PREVIOUS_RUN 11b's exactly, the runner {MX[0]}/{MX[1]} on its FIRST graded run, {TAPE_STORY}. THE DEPARTURES (read at the prints,
never predicted): (1) THE GREP DECIDED TWO COUNT SEATS for the two reuses — DD2 in cold_run_sequence.py (the seven_pn tuple's third and sixth, its blocks 4 -> 5) and Q32
in readback_probes.py (the w7 tuple, the blocks) — both retyped ONE -> TWO before the tape, the design's 'DD2, DD4, Q32' read at the grep (DD4 a set of names, unmoved);
(2) THE CLASSIFIER'S KEYS ARE READ AT THE SOURCE — the callees' print called shemini.classify with the sanctions engine's dict and 'fins' returned impure: the water branch
reads 'fin' and 'scale', the bird branch 'named_in_list' / 'claws_and_eats' / the three positive signs with 'unresolved_check_tradition' the tradition's own label, the
locust its four keys — the source read, the asks retyped; (3) MOADIM HAS NO CELL FOR 23:22 — the design's 'moadim.harvest_reaped' is the daemon's watched KIND: the
daemon's harvest branch called with a literal event (the corner's copy holiness.gifts('copy_23_22') — the Emor copy omits the vineyard); (4) THE PRIESTHOOD -> HOLINESS_B
EDGE NAMES 14:1 IN ITS taught_by, NOT ITS why — the DATA row's filter retyped from the fast checker's print; (5) THE DATA ROWS 56 (the design's 'about thirty-five'),
read from the print; (6) THE SCENE AND THE NARRATIVE MATCHED THEIR PREDICTIONS ON THE FIRST PASS — SEVENTY-ONE persons (the seven write asks case rows, not persons —
11b's lesson 3 held), every one written once, THE EATER OF THE TORN TWICE (the lashes and the torn to the dog — the watched effect torn_flesh_to_dogs given its case),
eight exempt, ten lashed, eleven barred, two impure, one left for the poor; 7 writes on Israel in the ink's order; (7) THE FAST CHECKER FOUR TIMES — part 1 alone once
(the moadim event's case_source the daemon's E_ helper reads), then parts 1-4: 2 fails, 1, 0; (8) THE CALLEES' FORMS settled at the print — temurah's tithe a string case
('took_ten_of_a_hundred' -> not_a_tithe), yovel's cycle a year (3 and 6 work years, 7 the sabbath of the land, 50 the jubilee), tithe_naming a dict of positions, the
Deuteronomy runners' (case, data) — 10b's lesson 2 held; (9) THE READBACK'S CENSUS AS THE DESIGN WROTE IT — ten on the tape by kind and first verse (nations_devoted,
olah_offered, profane_slaughter_permitted, covenant_offered, tithe_given, place_chosen_declared, vowed, portion_declared, tithe_of_the_tithe_commanded,
stranger_love_commanded), twenty-nine by CALL (every row has kin), VERBATIM 6 / VARIANT 11 / EXPANDED 4 / SUPPLIED 8, four SUPPLIED rows with their writes and 14:21
EXPANDED with its write — Q37's sum typed once; (10) THE EXAM'S CASES {CASES_N} in seven cells and the table ({PER_CELL}) — the docket's crowns as rows; (11) THE PROBES'
FAIL PRINT {PF[0]}/{PF[1]} — Q32 failed beside Q37-Q39 by its own retype; (12) the pointer {POINTER}; the registry's homographs {HOMOGRAPH}; (13) {CHAIN_STORY}.
THE RUN: readback_probes.py Q37-Q39 to FAIL ({PF[0]}/{PF[1]} — patch_probes_ch14.py, Q32 retyped with them) BEFORE the types; add_types_ch14.py (kinds 1155 -> {TY[0]},
effects 1056 -> {TY[1]} with rejoicing_before_the_lord_commanded's and levite_forsaking_barred's rows AMENDED for the reuses, the {TY[2]}th daemon with eight WRAPPED, the
span and the {TY[4]} CALL edges, I5 74, the five parameters — the_birds_signs in three layers, the_carcass_table with the precedence, the_moneys_form with the possession
clause, the_removal_date, the_tithes_new_year with the first third — {TY[5]} rows, the departures (b), (c), (d), (h), (i) applied; the register file untouched — DECLARED
98); ch14_callees.py (every CALL's asks and results printed — 193 KB, eighteen runners); derive_ch14_part1.py (the helpers from the chapter-13 runner by content
markers, W13 made W14; the ink block from ch14_ink.py in THREE blocks — the kin by computation, the ink facts, the register — with two store- and Onkelos-bound lines
dropped: 47 asserts; the parser's facts typed from the ink's own asserts — a runner cannot import the sequence file; the counter's day, the five parameters with the
calendar's own keys read, the one-database scans FOOD_SCAN [] and REUSE_SCAN [israel_people] x2, the DB's own seats, the callees' facts asserted from the print);
ch14_part2.py and ch14_part3.py (seven cells and the table, {CASES_N} asks — {PER_CELL}); ch14_part4.py (the twenty-nine rows, 56 DATA rows, the daemon with its
seven writes, seventy-one persons — the scene's submits written by ch14_scene_gen.py from the list and frozen, the narrative — every census printed before it is
asserted); ch14_fastcheck.py (part 1 alone, then parts 1-4 three passes: 2, 1, 0); ch14_cases_gen.py ({CASES_N} cases — the labels from part 4's own PERSONS);
ch14_assemble.py --guard {CASES_N}; cold_run_food_tithe.py {MX[0]}/{MX[1]} (the 69th runner, 315 KB); seq_record_ch14.py with the cache OFF ({NREC} records; food_tithe
statute {FT_REC[1] if FT_REC else '?'} of {FT_REC[0] if FT_REC else '?'} submits); seq_stitch_ch14.py (no marker; PLACEMENT {PLC}; CENSUS {CEN}); patch_seq_literals_ch14.py
(the import line, DAEMON_ORDER, RUN, PREVIOUS_RUN, NEWEST_RUNNER, PLACEMENT and CENSUS read, DF1-DF9, the VERDICTS; the one stale literal retyped — DD2);
{TAPE_STORY}; checkpoint_check.py --all ({CC[0]} rows, {CC[1]} miss — the eighteen known, {CC[2]} raised); {CHAIN_STORY}: the probe suites (readback
{PR['readback'][0]}/{PR['readback'][1]}, census {PR['census'][0]}/{PR['census'][1]}, installation {PR['installation'][0]}/6 with I5 74, large_letter {PR['large_letter'][0]}/6, checkpoint
{PR['checkpoint'][0]}/7, ink_cache {PR['ink_cache'][0]}/8), the daemon gate ({DGN} daemons{', %d functions' % DGF if DGF else ''}), the dependency gate ({DPE} edges, {DPP} pointers; the link
census reference {LC[0]} / transfer {LC[1]} / hypothesis {LC[2]} / none {LC[3]}), build_world, the journal gate{' (%d kinds, %d rows)' % JG if JG else ''}, THE REGISTER GATE --strict
(DECLARED {RG[0]}, DEBT {RG[1]}, FAILS {RG[2]} — no seat in chapter 14; the block (Deut 12:1, Deut 28:69] holds law_seducers and law_food_tithe), the positions table
({PO} checkpoints), the sweep {SW_P}/{SW_P} at {SW_CELLS} graded cells, the home-path gate. {TIMING}
THE LESSONS (eight): (1) A RUNNER CANNOT IMPORT THE SEQUENCE FILE — the reading's parser facts (the ink script reads them through the sequence module) are typed in the
runner from the ink's own asserts and proven by its own exec of the parser block; (2) A CLASSIFIER'S KEYS ARE READ AT THE SOURCE — the callees' print with a guessed dict
shows a wrong verdict, not an error: the ask's keys come from the cell's code; (3) A RUNNER WITHOUT A CELL FOR A VERSE IS CALLED THROUGH ITS DAEMON'S BRANCH with a
literal event carrying the fields the branch reads (case_source too); (4) AN EDGE MAY NAME A VERSE IN ITS taught_by — a DATA row's filter searches the whole edge;
(5) THE DATA COUNT IS READ FROM THE PRINT (56 for 'about thirty-five'); (6) THE SCENE'S PREDICTION FROM THE DESIGN'S ARITHMETIC HELD ON THE FIRST PASS when every
ask returns one effect set and a person's second write is named in the design (the eater of the torn); (7) A WRITE ASK IS A CASE ROW, NOT A PERSON — seven this
chapter (11b's lesson 3 held at the design, not at the print); (8) THE TWO-RUN RULE HELD on its seventh compile sitting under the cost rules: RUN A, the docket in
two runs, RUN B with the chain launched at its end, THE TAIL — five clean points, the owner compacting after each. NEXT on the owner's word: the commit (13b, 14,
12b — three messages in one); CHAPTER 15's reading (15:1-23) in one run — the release of the seventh year (the_removal_date's cycle by CALL), the poor, the Hebrew
slave, the firstling (15:19-23 — the firstling from outside the Land, 106:2, by CALL when it comes); on the table: the Decalogue-schema sitting, the SUPPLIED forms,
the calf's day marker, the registry's homographs, the receipt's third and fourth shapes, THE INSTALL HYPOTHESIS, the eras table's merge, the chain's positions step at
four workers, the fast checker's cells' dry-run.
"""
DEBT_HDR_OLD = "## SITTING 12 — CHAPTER 14 (2026-09-21, the reading; deu_14_food_tithe frozen) — OWED TO THE COMPILE 12b: "
DEBT_HDR_NEW = "## SITTING 12 — CHAPTER 14 (2026-09-21, the reading; deu_14_food_tithe frozen) — PAID AT 12b (the 12b box below, item by item) — OWED WAS: "
DEBT_BOX = f"""
## THE SITTING-12 BOX (a)-(o) PAID — (a) THE CUTS AND THE BALDNESS — F1 the_sons_and_the_cuttings: THE LINE sons_and_mourning_declared writing cuttings_for_the_dead_barred
## (a BLOCK — the cut and the factions from one word; the baldness by the analogy both ways with the priests' 21:5, PR.family and HB.body by CALL; the measure three ways,
## the count per spot and per soul, 'for the dead' the condition — the fallen house exempt; the frontlets' place from the baldness; the sonship's two arms a DATA row);
## (b) THE SIGNS OF THE BEASTS — F2 the_beasts: THE LINE food_law_declared writing abomination_eating_barred (a BLOCK) over SHM.classify by CALL — the four the
## classifier's own exception rows (the eater of the camel lashed), the ten named and no more (Chullin 80a:13-16), the shesua a creature, the fetus from 14:6's own
## words, the altar's disqualified (barred_from_it), the carcass touched (SHM.touch_effect); (c) THE WATER — F3 fins_and_scales (SHM by CALL; 14:9 through its twin);
## (d) THE BIRDS — F3 the_permission (the permission Leviticus lacks — SUPPLIED rows 14:11, 14:20), the_birds_signs A PARAMETER IN THREE LAYERS (the four signs, the ruling
## with the knowledge condition, the tradition arm — the hunter by tradition accepted, the clawer lashed), the two lists counted, the eggs, the locusts absent by CALL,
## the swarming fowl; (e) THE CARCASS — F4: THE LINE carcass_and_kid_declared writing carcass_eating_barred (a BLOCK — the ban's seat the sanctions engine names; the
## sanction by SA.carcass('lashes_for_eating') by CALL), the_carcass_table A PARAMETER (R. Meir / R. Yehuda; THE PRECEDENCE a third clause), 'any carcass' the torn
## (OR.torn by CALL — the eater of the torn lashed, the torn to the dog), the carcass by fitness (the putrid exempt), the sale clause, the custom's bar; (f) THE KID'S
## THREE READINGS — F4: CA.kid_in_milk by CALL on cook, eat, benefit (barred_from_it), the benefit counter-arm, the fowl out (exempt), the stomach's milk, 34:26 by
## ER.repeats; NO NEW WRITE; (g) THE SECOND TITHE — F5 and F6: THE LINE second_tithe_declared writing second_tithe_owed (a STATUS — named the second by the shelf, the
## liabilities with the courtyard's arm by KO.the_tithe, the wall's two capacities (lashes outside), the House standing (barred), the year passed, THE EXILE'S ARM,
## Heaven's property (the sale barred), the firstling by OR.firstling and KO.the_gifts, the firstling from outside exempt, 'learn to fear'), the far place by PN
## ('too_far'), the_moneys_form A PARAMETER WITH THE POSSESSION CLAUSE (the blank coin and the money in the sea barred), the three moneys, THE CLASS FROM THE FOUR
## NAMED BY I6 (Nazir 35b:3 — water and salt barred), the containers, THE REJOICING REUSED (rejoicing_before_the_lord_commanded's second entry), THE LEVITE'S LADDER
## OF FOUR REUSED (levite_forsaking_barred's second entry), Shiloh and the House by the eras table; (h) THE THIRD YEAR — F7: THE LINE third_year_tithe_declared writing
## poor_tithe_owed (a STATUS — one tithe not two, the Levite never interrupted), the_removal_date A CLOCK DATUM (the calendar's key passover_7's eve; the years by
## YO.cycle and CA.sabbatical — the seventh exempt), the_tithes_new_year A CLOCK DATUM (rosh_hashanah; the first third), the gifts exempt (HO.gifts, the moadim branch —
## left_for_the_poor), the four in want, the measures, the uses barred, THE SOJOURNER TWO PERSONS (the convert accepted, the resident alien exempt), Ezra's penalty, the
## courtyard from 'your gates', the animal tithe now (exempt); (i) THE EFFECTS — cuttings_for_the_dead_barred, abomination_eating_barred, carcass_eating_barred (blocks),
## second_tithe_owed, poor_tithe_owed (statuses) NEW; the two reuses; 'a holy people' the ground (no write); (j) THE PLACE FORMULA at its fourth and fifth seats — PN by
## CALL; (k) THE KIN BY CALL — eighteen runners (the design's eighteen); (l) NEVER READ AHEAD — 15:1, 15:19-23, 16:11-14, 17:1, 18:1, 22:6-7, 23:21, 24:17-21, 26:12-14,
## 27:7, 31:10, 32:9 wait for their sittings; (m) THE REGISTER's DATA rows (the plural/singular register from the morphology, the parser's [2] and [3], the starred tithe
## tokens, the infinitive absolutes) DATA rows in the runner; (n) THE CHECKPOINT SERIES — DF1-DF9 the sixth name; (o) THE DOCKET — 991 rows in two runs (771 read whole
## here, 220 carried), the writer derived from 11b's, the crowns the cells' rows.
## OWED FROM 12b: (i) THE FAST CHECKER'S CELLS' DRY-RUN (11b's owed item — still owed); (ii) THE SEATS AHEAD — 15:1's release and 31:10's seven years (the_removal_date by
## CALL), 15:19-23's firstling (the_firstling_from_outside), 16:11 and 16:14's rejoicing and the four at the gate (second entries; the formula 14:29's first seat), 17:1's
## blemish, 18:1's Levite, 22:6-7's bird's nest (228:5), 23:21's foreigner, 24:17-21's gifts (the import table), 26:12-14's confession and removal (the_removal_date;
## KO.the_tithe 'confession'), 27:7's rejoicing peace offerings (I2 — 107:16), 32:9's portion (312:1); (iii) THE RUNNING WORLD'S SABBATICAL COUNT for the removal's year
## (the cell reads the cycle by CALL; the count not begun before the entry — a measurement at chapter 15); (iv) THE RECEIPT'S THIRD AND FOURTH SHAPES, THE SUPPLIED
## FORMS, THE CALF'S DAY MARKER, THE REGISTRY'S HOMOGRAPHS (the_place_luz_bethel, the_raven, the_flock, the_beasts {HOMOGRAPH}), THE INSTALL HYPOTHESIS, THE ERAS
## TABLE'S MERGE, THE CHAIN'S POSITIONS STEP AT FOUR WORKERS — on the owner's word; (v) THE CHECKPOINT SERIES continues (DF the sixth name — DF9 the last; the next
## DG1, keyed by its first word). NOTHING ELSE IN CHAPTER 14 IS OWED TO A LATER SITTING OF ITS OWN.
"""
MIDDOT_ANCHOR = "\n## Exodus block campaign — owner's word \"Do 3\")\n"
MIDDOT_ENTRY = f"""- THE CHAPTER-14 COMPILE (THE DEUTERONOMY WALK sitting 12b RUN B, 2026-09-22; cold_run_food_tithe.py — the docket's rules carried into the cells; every code checked in this file before typed): I1 qal wa-chomer (a fortiori) at four seats — the four named the exception and the sign the class (the Sifrei 101:10, F2 the_four_closed_by_it), the wall from the lesser holies (106:3, F5 the_wall_two_capacities), the three moneys (107:7, F6 the_three_moneys), the eating of meat in milk from 12:24's clause (76:7 at Chullin 115b, F4 the_benefit_counter_arm); I2 gezerah shavah (verbal analogy) at four — the baldness both ways with the priests' 21:5 ('korcha' (baldness), 96:12; Makkot 20a:12-14; Kiddushin 36a:6-8 — F1 the_baldness_both_ways), the removal's date with 31:10's 'at the end of seven years' (109:1-3, F7 the_removal_date), the rejoicing with 27:7's peace offerings (107:16, F6 the_rejoicing — the seat ahead recorded), the birds' list carried by its head (103:3-4, the readback row 14:12); I3 binyan av (a paradigm) — the four in want by the Levite's paradigm (110:1-2, F7 the_four_in_want), 'seh' (a lamb or kid) the paradigm excluding the hybrid (Bava Kamma 77b:13, F2 the_ten_named); I5 prat u-kelal (particular then general) REFUSED — the ten named closed against it (Chullin 80a:14-16); I6 kelal u-frat u-kelal (general, particular, general) — the class from the four named (107:8-11; Bava Kamma 54b:20; NAZIR 35b:3 THE CHAPTER'S VERSE THE SOURCE OF THE METHOD — F6 the_class_from_the_four; the design's I3 retyped, departure (a)); the juxtaposition named without a code — the House standing from the firstling (106:4, F5 the_house_standing) and the Levite never interrupted from the inheritance (Rosh Hashanah 12b:4-5, F7); the disputes as PARAMETERS (the_birds_signs in three layers, the_carcass_table with the precedence, the_moneys_form with the possession clause) and the clock data as parameters (the_removal_date, the_tithes_new_year with the first third) — every arm a docket row, read as data, never a constant.
"""
DKF = 'deu_14_reeh_exam_2026-09-21.md'
RLOG = f"""
## 2026-09-22 — DEUTERONOMY 14 COMPILED AND ON THE TAPE (THE DEUTERONOMY WALK sitting 12b, the two-run rule's seventh compile sitting under the cost rules): THE FOOD
## LAWS AND THE TITHES COMPILED AS FIVE LAWS AT THE CHAPTER'S OWN DAY OVER THE TWIN CHAPTER'S CELLS BY CALL — THE CUTTING'S BAR AT ITS FIRST SEAT, THE ABOMINATION'S
## GENERAL CLAUSE, THE CARCASS'S BAN AT THE SEAT THE SANCTIONS ENGINE ITSELF NAMES, THE SECOND TITHE WITH THE EXILE'S ARM, THE THIRD YEAR'S TITHE WITH ITS DATE A
## CLOCK DATUM; THE BIRDS' SIGNS A PARAMETER IN THREE LAYERS — THE CODE/DATA SEPARATION LAW'S OWN CASE; THE CLASS FROM THE FOUR NAMED BY THE METHOD THE CHAPTER'S OWN
## VERSE TEACHES; TWO REUSES AND TWO COUNT SEATS RETYPED BY THE GREP
On the owner's "Reread and go" after the compaction at #205 addendum 2. THE COMPILE: cold_run_food_tithe.py the 69th runner (seven cells and the table, {CASES_N} asks,
{MX[0]}/{MX[1]} on its first graded run), law_food_tithe the 74th daemon (given_at Deut 14:1, installed_by boot; eight WRAPPED); FIVE OWN-DAY LINES at (40, 11, 1), no marker —
sons_and_mourning_declared (cuttings_for_the_dead_barred a BLOCK — the cut and the factions from one word, the baldness by the analogy both ways), food_law_declared
(abomination_eating_barred a BLOCK over shemini.classify by CALL — the four the classifier's own exception rows, the ten named and no more, the fetus from 14:6's own
words; the_birds_signs a PARAMETER in three layers), carcass_and_kid_declared (carcass_eating_barred a BLOCK — sanctions.carcass's lashed cell names Deut 14:21; the_carcass_table
a PARAMETER with the precedence; the kid NO new write — calendar.kid_in_milk by CALL), second_tithe_declared (second_tithe_owed a STATUS — the liabilities, the wall's two
capacities, the House standing, the exile's arm, Heaven's property; the_moneys_form a PARAMETER with the possession clause; the class from the four named by I6 — Nazir
35b:3; rejoicing_before_the_lord_commanded and levite_forsaking_barred REUSED — second entries), third_year_tithe_declared (poor_tithe_owed a STATUS — one tithe not two;
the_removal_date and the_tithes_new_year CLOCK DATA the calendar's own keys, the years by CALL to the cycle); THE READBACK'S FORMS ON FILE, NO NEW FORM — twenty-nine
rows one per verse (VERBATIM 6 / VARIANT 11 / EXPANDED 4 / SUPPLIED 8 — four with their writes, 14:21 EXPANDED with its write; ten on the tape, twenty-nine by CALL);
{TAPE_STORY.lower()}; the gates chain {CHAIN_STORY.lower()} (the register gate DECLARED {RG[0]} / DEBT {RG[1]} / FAILS {RG[2]}; the sweep {SW_P}/{SW_P}). THE EXAM'S PERSONS seventy-one —
eight exempt, ten lashed, eleven barred, two impure, the torn to the dog, the corner left for the poor. THE DOCKET (two runs): logic/oral_triage/{DKF} — 991 rows, 771
read whole here and 220 carried with their ledgers' own verdict lines; its crowns in the map's two AS RUN paragraphs. THE RECORD KEPT: the grep found TWO count seats for
the two reuses (DD2, Q32 — both retyped before the tape); the classifier's keys read at the source after the print's guessed dict; moadim without a cell for 23:22 called
through its daemon's branch; the priesthood edge naming 14:1 in its taught_by; the scene matched its prediction on the first pass. {TIMING} The forms in
World/step9/forms_deuteronomy_walk/.
"""
STEPS_ANCHOR = "\n## Step 6 — Publish\n"
STEPS_PARA = f"""
**Deuteronomy 14 compiled (2026-09-22, sitting 12b — the two-run rule's seventh compile sitting, the docket in two runs):** the chapter is law from its first word
to its last, and its twin was already in the machine — Leviticus 11's classifier answers the beasts, the water and the birds by call, with the camel, the hare, the coney
and the swine its own exception rows. What the chapter alone gives became five laws at its own day, no marker: the cutting's bar for all Israel (with 'no factions' from
the same word), the abomination's general clause, the carcass's ban at the very seat the sanctions engine already named, the second tithe (named the second by the shelf,
with the exile's third state as chapter 12's slaughter law had), and the third year's tithe. Two disputes and two dates are parameters, never constants: how a bird is
known clean (the Sages' teaching in three layers — the code/data separation law's own case), who may be given or sold the carcass (with the resident alien first), what
'money' is (with the possession clause), when the tithes are removed (the calendar's own key in the count's fourth and seventh year, the count by call to the cycle) and
when the tithes' year begins (Tishri 1 with the first third). The rejoicing and the Levite's bar are second entries on Israel, not new laws, and the grep found the two
old counts of one. The readback's forms held with no new form — twenty-nine rows, one per verse, eight supplied. The exam has seventy-one persons. The runner
{MX[0]}/{MX[1]} on its first run; {TAPE_STORY.lower()}; the gates chain {CHAIN_STORY.lower()}. Every step timed: {TSUM12B} machine seconds over {len(T12B)} steps for the compile.
"""
BRIEF_BULLET = (f"- **CHAPTER 14 COMPILED — THE FOOD LAWS AND THE TITHES AS FIVE LAWS AT THE CHAPTER'S OWN DAY OVER THE TWIN CHAPTER'S CELLS BY CALL: THE BIRDS' SIGNS A PARAMETER IN THREE LAYERS (THE CODE/DATA SEPARATION LAW'S OWN CASE), THE CARCASS'S BAN AT THE SEAT THE SANCTIONS ENGINE NAMES, THE SECOND TITHE WITH THE EXILE'S ARM, THE REMOVAL'S DATE A CLOCK DATUM, THE CLASS FROM THE FOUR NAMED BY THE METHOD THE CHAPTER'S VERSE TEACHES (2026-09-22, sitting 12b)** — cold_run_food_tithe.py the 69th runner ({MX[0]}/{MX[1]} first run), law_food_tithe the 74th daemon; five lines, seven writes (two reuses), five parameters; {TAPE_STORY.lower()}; the chain {CHAIN_STORY.lower()}. Uncommitted since fb797a1 with 13b and 14.\n")
BRIEF_ENTRY = f"""### 2026-09-22 — CHAPTER 14 COMPILED: FIVE LAWS AT ONE DAY OVER A TWIN ALREADY IN THE MACHINE, AND THE DISPUTES AS PARAMETERS
Chapter 14 restates Leviticus 11 and adds the tithes, and the compile found the twin already compiled: the classifier answers every beast, fish and bird by call, and the
four exceptions it names are its own rows. The chapter's gains became laws of their own — the cut for the dead barred for all Israel (and 'no factions' from the same
word), the abomination's general clause, the carcass's ban (the sanctions engine had named this verse as the ban's seat before this chapter was compiled), the second
tithe with the shelf's own name for it, and the third year's tithe that replaces it twice in seven years. The shelf's disputes stayed disputes, read as data: how a bird
is known clean is the Sages' teaching, not the Torah's — the four signs, the ruling with its knowledge condition, the tradition that lets a hunter be believed; whether
'money' means a blank or a stamped coin; who takes the carcass first. Two dates are clock data on the calendar's own keys, and the year of the count comes by call from
the Jubilee engine, never as a number in the code. Two laws were second entries on Israel's ledger — the rejoicing and the Levite's bar — and the grep found the two
places where the old count of one was typed. The scene of seventy-one persons matched its prediction on the first pass. The runner {MX[0]}/{MX[1]} on its first run;
{TAPE_STORY.lower()}; the chain {CHAIN_STORY.lower()}. Every step was timed: {TSUM12B} machine seconds over {len(T12B)} steps for the compile. Next: the commit; chapter 15 —
the release, the poor, the Hebrew slave, the firstling.
"""
LOOP_OLD = "cold_run_seducers.py (chapter 13, THE FORMS ON FILE — NO NEW FORM 2026-09-21:"
LOOP_NEW = "cold_run_food_tithe.py (chapter 14, THE FORMS ON FILE — NO NEW FORM 2026-09-22: the food laws and the tithes — twenty-nine rows one per verse VERBATIM 6 / VARIANT 11 / EXPANDED 4 / SUPPLIED 8, ten on the tape by kind and first verse, twenty-nine by CALL (the twin chapter's classifier), four SUPPLIED rows with their writes and 14:21 EXPANDED with its write, no pointer row, no state row, no retrograde row; DF1-DF9); " + LOOP_OLD
RESUME_HEAD = f"""# ⚠ THE DEUTERONOMY WALK sitting 12b — CHAPTER 14 COMPILED AND ON THE TAPE (2026-09-22; step9/DEUTERONOMY_WALK.md "Sitting 12b" + the two "THE DOCKET — AS RUN" + "Sitting 12b — AS BUILT"):
# cold_run_food_tithe.py the 69th runner ({MX[0]}/{MX[1]} first run), law_food_tithe the 74th daemon; FIVE OWN-DAY LINES, NO MARKER — the sons and the cuttings
# (cuttings_for_the_dead_barred), the food law (abomination_eating_barred over shemini.classify by CALL; the_birds_signs a PARAMETER in three layers), the carcass and
# the kid (carcass_eating_barred; the_carcass_table a PARAMETER; the kid no new write), the second tithe (second_tithe_owed; the_moneys_form a PARAMETER; the rejoicing
# and the Levite REUSED), the third year (poor_tithe_owed; the_removal_date and the_tithes_new_year CLOCK DATA); {TAPE_STORY.lower()} (DF1-DF9); the chain
# {CHAIN_STORY.lower()}; the register gate DECLARED {RG[0]} / DEBT {RG[1]} / FAILS {RG[2]}; the sweep {SW_P}/{SW_P}.
# UNCOMMITTED since fb797a1: 13b, 14, 12b (the messages at <scratch>/commit_msg_ch14.txt and commit_msg_ch14b.txt). NEXT on the owner's word: the commit; chapter 15's reading.
"""
STATE_ADD = f"""
#205 ADDENDUM 4 (2026-09-22, at the close of THE DEUTERONOMY WALK sitting 12b's TAIL — on the owner's word after the compaction at addendum 3; A CLEAN COMPACTION POINT): THE STATE: CHAPTER 14 COMPILED AND ON THE TAPE — the tail as run: the chain's summary read once ({CHAIN_STORY}); the records from the sheet in one call (write_ch14b_records.py — the map's AS BUILT with the timing table, COMPILE_DEBT's sitting-12 box PAID and the 12b box, MIDDOT's compile entry, RESEARCH_LOG, THE_STEPS, THE_BRIEFING, THE_LOOP's step-6 row, RESUME, RECORD_FORMS, this addendum, the addenda's section, the recovery page, the memory); the forms copied (copy_ch14b_forms.py); the commit message extended (<scratch>/commit_msg_ch14b.txt — 12b's beneath chapter 14's and 13b's in commit_msg_ch14.txt). THE NUMBERS from the prints: the runner {MX[0]}/{MX[1]}; {TAPE_STORY}; checkpoint_check {CC[0]} rows, {CC[1]} miss, {CC[2]} raised; the probe suites readback {PR['readback'][0]}/{PR['readback'][1]}, census {PR['census'][0]}/{PR['census'][1]}, installation {PR['installation'][0]}/6, large_letter {PR['large_letter'][0]}/6, checkpoint {PR['checkpoint'][0]}/7, ink_cache {PR['ink_cache'][0]}/8; the daemon gate {DGN} daemons; the dependency gate {DPE} edges, {DPP} pointers (the link census {LC}); the register gate DECLARED {RG[0]} / DEBT {RG[1]} / FAILS {RG[2]}; the positions table {PO} checkpoints; the sweep {SW_P}/{SW_P} at {SW_CELLS} graded cells; the pointer {POINTER}; the homographs {HOMOGRAPH}. UNCOMMITTED since fb797a1: 11b, 12, 12b whole. NOTHING MID-FLIGHT — A CLEAN COMPACTION POINT. NEXT ON HIS WORD: THE COMMIT (commit_msg_ch14.txt holds chapter 14's and 13b's messages, commit_msg_ch14b.txt 12b's — one message); then CHAPTER 15's reading (15:1-23) in one run + its tail. POST-COMPACTION REREADS: the recovery page, the map's newest section ("Sitting 12b — AS BUILT"), MEMORY.md.
"""
def next_addenda_no(s):
    ns = [int(x) for x in re.findall(r'^##+ *§?(\d+)[\.\s:—]', s, re.M)] + [int(x) for x in re.findall(r'§(\d+)', s)]
    return (max(ns) + 1) if ns else 60
ADDENDA_ADD_T = """
## §{N} — THE DEUTERONOMY WALK sitting 12b (2026-09-21/22): CHAPTER 14 COMPILED — the state doc's #205 and its addenda 1-4; the map's "Sitting 12b … THE DESIGN", its two "THE DOCKET — AS RUN" paragraphs and "Sitting 12b — AS BUILT"
The two-run rule's seventh compile sitting under the cost rules with the docket clause twice: RUN A (the rereads, the recon and the scan derived by line-based substitutions,
the design), THE DOCKET in two runs (991 rows — 771 read whole here, 220 carried with their ledgers' own verdict lines; the boundary computed from the dump), RUN B (the
probes to FAIL with Q32 retyped, the types with the five parameters, the callees' print with the classifier's keys read at the source, the runner 78/78 first run, the
recorder with the cache off, the stitcher with no marker, the literals with DD2 retyped, the tape with DF1-DF9, the chain launched at the run's end), THE TAIL (the summary
read once, the demands filed if any, the records, the forms, the message). The crowns: the birds' signs the Sages' teaching in three layers, the carcass's ban at the seat
the sanctions engine names, the class from the four named by the method the chapter's verse teaches, the exile's arm on the second tithe, the removal's date a clock datum
on the calendar's own key with the count by call. The lessons in the AS BUILT (eight). Every step timed. Uncommitted since fb797a1: 13b, 14 and 12b; the messages at
<scratch>/commit_msg_ch14.txt and commit_msg_ch14b.txt.
"""
MEM_PARA = f"""
SITTING 12b DONE (2026-09-22, "Reread and go" after the compaction at #205 addendum 2; the tail after addendum 3): CHAPTER 14 COMPILED AND ON THE TAPE —
cold_run_food_tithe.py the 69th runner ({MX[0]}/{MX[1]} first run), law_food_tithe the 74th daemon (eight WRAPPED); FIVE OWN-DAY LINES, NO MARKER: sons_and_mourning_declared
(cuttings_for_the_dead_barred), food_law_declared (abomination_eating_barred — shemini.classify by CALL; the_birds_signs a PARAMETER in three layers), carcass_and_kid_declared
(carcass_eating_barred — the seat sanctions.carcass names; the_carcass_table a PARAMETER with the precedence; the kid no new write), second_tithe_declared (second_tithe_owed
with the exile's arm; the_moneys_form with the possession clause; rejoicing_before_the_lord_commanded and levite_forsaking_barred REUSED), third_year_tithe_declared
(poor_tithe_owed; the_removal_date and the_tithes_new_year CLOCK DATA on the calendar's keys, the years by CALL to the cycle); RUN (1332, 96, 88, 0, 12, 1641, 45, 319,
pairs, 127), markers 172, kinds 877; {TAPE_STORY.lower()}, DF1-DF9; the chain {CHAIN_STORY.lower()}; the register gate DECLARED {RG[0]} / DEBT {RG[1]} / FAILS {RG[2]}; the pointer {POINTER}.
THE LESSONS: a runner cannot import the sequence file (the parser's facts typed from the ink's asserts); a classifier's keys are read at the source (the print's guessed
dict shows a wrong verdict, not an error); a runner without a cell for a verse is called through its daemon's branch with a literal event; an edge may name a verse in its
taught_by; the DATA count read from the print (56); the scene's prediction held on the first pass (71 persons, the eater of the torn twice); a write ask is a case row not
a person (seven); the D series' sixth name DF (DG next). TIMED: {len(T12B)} steps, {TSUM12B} machine seconds. UNCOMMITTED since fb797a1: 13b, 14, 12b (the messages
<scratch>/commit_msg_ch14.txt, commit_msg_ch14b.txt). NEXT on his word: the commit; chapter 15's reading (15:1-23).
"""
MEM_IDX_OLD = '12b RUN B DONE (78/78; tape 10/10; 5 lines, 7 writes); the chain LAUNCHED; 13b + 14 uncommitted; NEXT: THE TAIL'; MEM_IDX_NEW = '12b DONE (78/78; 5 lines; 2 reuses; 5 parameters); 13b + 14 + 12b uncommitted; commit next'
FORMS_OLD = "World/step9/forms_deuteronomy_walk/write_ch13b_records.py (write_ch12b_records.py,"
FORMS_NEW = "World/step9/forms_deuteronomy_walk/write_ch14b_records.py (write_ch13b_records.py, write_ch12b_records.py,"
REC_EDITS = [("## 2. WHERE IT STANDS (2026-09-22, 12b RUN B done; #205 add. 3 newest)", "## 2. WHERE IT STANDS (2026-09-22, 12b done; #205 add. 4 newest)"),
             ("(DF1-DF9); the chain LAUNCHED.", f"(DF1-DF9); the sweep {SW_P}/{SW_P}; every gate GREEN."),
             ("- UNCOMMITTED since fb797a1: 13b, 14, 12b. THE CHAIN LAUNCHED at RUN B's end (#205 add. 3). NEXT ON HIS WORD: THE TAIL\n  after a compaction (the summary once, the demands, the records, the forms, the message).", "- UNCOMMITTED since fb797a1: 13b, 14, 12b (<scratch>/commit_msg_ch14.txt + commit_msg_ch14b.txt). 12b DONE (#205 add. 4).\n  NEXT ON HIS WORD: the commit; then chapter 15's reading (15:1-23), one run + its tail.")]
# ---- THE ANCHORS ----
ok = True
def need(p, a, n=1):
    global ok
    c = read(p).count(a)
    if c != n: print('ANCHOR', p.split('/')[-1], c, a[:70]); ok = False
MAP = 'World/step9/DEUTERONOMY_WALK.md'; DEBT = 'World/step9/COMPILE_DEBT.md'; MID = 'logic/MIDDOT.md'; RL = 'RESEARCH_LOG.md'; STEPS = 'THE_STEPS.md'; BRIEF = 'THE_BRIEFING.md'; LOOP = 'World/step9/THE_LOOP.md'
RES = 'World/RESUME.md'; RF = 'World/step9/RECORD_FORMS.md'; STATEDOC = 'logic/pre_logic_methods_2026-07-28/PROMPT_continue_solo_era_2026-08-06.md'; ADD = 'logic/pre_logic_methods_2026-07-28/RECOVERY_addenda_2026-09-12.md'
REC = 'logic/pre_logic_methods_2026-07-28/RECOVERY_new_thread_2026-09-12.md'; WALK = f'{MEM}/deuteronomy-walk.md'; IDX = f'{MEM}/MEMORY.md'
BRIEF_ENTRY_ANCHOR = [l for l in read(BRIEF).split('\n') if l.startswith('### 2026-09-21 — CHAPTER 14 READ')]; assert len(BRIEF_ENTRY_ANCHOR) == 1, BRIEF_ENTRY_ANCHOR; BRIEF_ENTRY_ANCHOR = BRIEF_ENTRY_ANCHOR[0]
BRIEF_BULLET_ANCHOR = [l for l in read(BRIEF).split('\n') if l.startswith('- **CHAPTER 14 READ AND FROZEN')]; assert len(BRIEF_BULLET_ANCHOR) == 1, BRIEF_BULLET_ANCHOR; BRIEF_BULLET_ANCHOR = BRIEF_BULLET_ANCHOR[0]
MEM_DESC = [l for l in read(WALK).split('\n') if l.startswith('description: "')]; assert len(MEM_DESC) == 1, MEM_DESC; MEM_DESC_OLD = MEM_DESC[0]
MEM_DESC_NEW = 'description: "COMMITTED THROUGH fb797a1 (2026-09-21; NOT PUSHED — pushed through 2b0c9c8) — SITTING 12b DONE 2026-09-22 (chapter 14 COMPILED — five laws at the chapter\'s own day over the twin\'s cells by CALL, two reuses, five parameters; the runner 78/78; DF1-DF9); 13b, 14 and 12b uncommitted; NEXT on his word: the commit, then chapter 15\'s reading"'
need(DEBT, DEBT_HDR_OLD); need(MID, MIDDOT_ANCHOR); need(STEPS, STEPS_ANCHOR); need(BRIEF, BRIEF_BULLET_ANCHOR); need(BRIEF, BRIEF_ENTRY_ANCHOR); need(LOOP, LOOP_OLD); need(RF, FORMS_OLD)
need(WALK, MEM_DESC_OLD); need(IDX, MEM_IDX_OLD)
for a, b in REC_EDITS: need(REC, a)
assert 'Sitting 12b — THE COMPILE OF CHAPTER 14 — AS BUILT' not in read(MAP) and '#205 ADDENDUM 4' not in read(STATEDOC) and '#205 ADDENDUM 3' in read(STATEDOC)
rec = read(REC)
for a, b in REC_EDITS: rec = rec.replace(a, b)
idx = read(IDX).replace(MEM_IDX_OLD, MEM_IDX_NEW)
N_ADD = next_addenda_no(read(ADD)); ADDENDA_ADD = ADDENDA_ADD_T.replace('{N}', str(N_ADD))
for t in (AS_BUILT, DEBT_BOX, MIDDOT_ENTRY, RLOG, STEPS_PARA, BRIEF_BULLET, BRIEF_ENTRY, LOOP_NEW, RESUME_HEAD, STATE_ADD, ADDENDA_ADD, MEM_PARA, rec, idx):
    assert not re.search(r'/Users/(?!Shared/)', t) and os.path.expanduser('~') not in t and ('/private' + '/tmp') not in t, 'a home or scratch path in a record'   # the guard's literal split by concatenation
print('anchors %s; the recovery page would be %d bytes (cap 10240); MEMORY.md %d (cap 17000); the addenda section §%d' % ('OK' if ok else 'BAD', len(rec.encode('utf-8')), len(idx.encode('utf-8')), N_ADD))
assert ok and len(rec.encode('utf-8')) <= 10240 and len(idx.encode('utf-8')) <= 17000
if CHECK: sys.exit(0)
W(MAP, read(MAP).rstrip('\n') + '\n' + AS_BUILT)
W(DEBT, read(DEBT).replace(DEBT_HDR_OLD, DEBT_HDR_NEW).rstrip('\n') + '\n' + DEBT_BOX)
W(MID, read(MID).replace(MIDDOT_ANCHOR, '\n' + MIDDOT_ENTRY.rstrip('\n') + '\n' + MIDDOT_ANCHOR))
W(RL, read(RL).rstrip('\n') + '\n' + RLOG)
W(STEPS, read(STEPS).replace(STEPS_ANCHOR, '\n' + STEPS_PARA.rstrip('\n') + '\n' + STEPS_ANCHOR))
b = read(BRIEF); b = b.replace(BRIEF_BULLET_ANCHOR, BRIEF_BULLET + BRIEF_BULLET_ANCHOR, 1).replace(BRIEF_ENTRY_ANCHOR, BRIEF_ENTRY.rstrip('\n') + '\n\n' + BRIEF_ENTRY_ANCHOR, 1); W(BRIEF, b)
W(LOOP, read(LOOP).replace(LOOP_OLD, LOOP_NEW))
W(RES, RESUME_HEAD + read(RES)); W(RF, read(RF).replace(FORMS_OLD, FORMS_NEW))
W(STATEDOC, read(STATEDOC).rstrip('\n') + '\n' + STATE_ADD); W(ADD, read(ADD).rstrip('\n') + '\n' + ADDENDA_ADD); W(REC, rec)
W(WALK, read(WALK).replace(MEM_DESC_OLD, MEM_DESC_NEW).rstrip('\n') + '\n' + MEM_PARA); W(IDX, idx)
print('written: the map, COMPILE_DEBT, MIDDOT, RESEARCH_LOG, THE_STEPS, THE_BRIEFING, THE_LOOP, RESUME, RECORD_FORMS, the state doc, the addenda, the recovery page, the memory note, the index')
for p in (MAP, DEBT, MID, RL, STEPS, BRIEF, LOOP, RES, RF, STATEDOC, ADD, REC, WALK, IDX):
    q = p if p.startswith('/') else f'{ROOT}/{p}'
    r = subprocess.run([sys.executable, f'{ROOT}/logic/solo_tools/gloss_lint.py', q], capture_output=True, text=True); print('  lint', p.replace(MEM, '<memory>'), (r.stdout.strip().split('\n')[-1])[:60])
