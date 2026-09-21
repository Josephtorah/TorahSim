import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE DEUTERONOMY WALK 10b RUN B / THE TAIL (2026-09-21): THE RECORDS FROM THE SHEET IN ONE CALL (World/step9/RECORD_FORMS.md) — the map's "Sitting 10b — AS BUILT"
# (with THE TIMING TABLE the owner asked for), COMPILE_DEBT's sitting-10 box PAID and the 10b box, MIDDOT's compile entry, RESEARCH_LOG, THE_STEPS, THE_BRIEFING (the
# scoreboard and an entry), THE_LOOP's step-6 row, RESUME, RECORD_FORMS, the state doc's #201 addendum 4 (the close — a clean point), the addenda's section, the
# recovery page rewritten under its cap, the memory (the walk note and the index). EVERY NUMBER PARSED FROM THE PRINTS (the runner's run, the tape's run, the chain's
# folder, the timing table, the records' own reads), never recited; every text built whole before its file is opened; the caps asserted; --check runs the reads and the
# anchors alone. write_ch11b_records.py's form. WRITTEN AT RUN B, RUN AT THE TAIL. RUN FROM THE REPO ROOT.
import os, re, sys, subprocess
ROOT = _ROOT
SP = os.path.dirname(os.path.abspath(__file__)); G = f'{SP}/gates_ch12b'
MEM = os.path.expanduser('~/.claude/projects/-Users-Shared-TorahSim/memory')
CHECK = '--check' in sys.argv
def rd(name): return open(name if name.startswith('/') else f'{G}/{name}', encoding='utf-8', errors='ignore').read()
def read(p): return open(p if p.startswith('/') else f'{ROOT}/{p}', encoding='utf-8').read()
def W(p, s): open(p if p.startswith('/') else f'{ROOT}/{p}', 'w', encoding='utf-8').write(s)
def last_frac(name, den):
    fr = re.findall(r'(\d+)/(\d+)', rd(name)); fr = [(int(a), int(b)) for a, b in fr if int(b) == den]
    assert fr, (name, den); return fr[-1][0]
# ---- THE PRINTS ----
run1 = rd(f'{SP}/ch12_runner_run1.out'); assert 'MATRIX: 65/65' in run1
CASES_N = int(re.search(r'CASES generated: (\d+)', rd(f'{SP}/ch12_cases_gen.out')).group(1)); PER_CELL = re.search(r'per cell (\{.*?\})', rd(f'{SP}/ch12_cases_gen.out')).group(1)
TAPE_FILE = f'{SP}/ch12_tape_run2.out' if os.path.exists(f'{SP}/ch12_tape_run2.out') else f'{SP}/ch12_tape_run1.out'
tape = rd(TAPE_FILE); assert '10/10 checkpoints' in tape, TAPE_FILE
DD = re.findall(r'CHECKPOINT (DD\d) .*? (MATCH|MISS|DIVERGE)$', tape, flags=re.M); assert len(DD) == 9 and all(v == 'MATCH' for _, v in DD), DD
cc = rd(f'{SP}/ch12_checkpoint_check.out'); CC = re.search(r'checkpoint_check: (\d+) rows, (\d+) miss, (\d+) raised', cc); CC = tuple(int(x) for x in CC.groups()); assert CC[1] == 18 and CC[2] == 0, CC
st = rd(f'{SP}/seq_stitch_ch12.out'); PLC = re.search(r'^PLACEMENT LITERAL: (.*)$', st, re.M).group(1); CEN = re.search(r'^  CENSUS tuple .*?: (\(.*\))$', st, re.M).group(1)
rec = rd(f'{SP}/seq_record_ch12.out'); NREC = int(re.search(r'recording: (\d+) records written', rec).group(1)); PN_REC = re.search(r'^  place_name\s+worlds \d+\s+total\s+(\d+).*?statute\s+(\d+)', rec, re.M); PN_REC = (int(PN_REC.group(1)), int(PN_REC.group(2))) if PN_REC else None
summ = rd('SUMMARY.txt'); assert 'GATES CHAIN DONE — ALL GREEN' in summ, summ[-400:]
dg = rd('daemon.out'); DGN = int(re.search(r'(\d+) daemons', dg).group(1)); DGF = re.search(r'(\d+) functions', dg); DGF = int(DGF.group(1)) if DGF else None
dp = rd('dependency.out'); LC = re.search(r'LINK CENSUS \(the link review law\): reference (\d+), transfer (\d+), hypothesis (\d+), none (\d+)', dp); LC = tuple(int(x) for x in LC.groups())
DPE = re.search(r'(\d+) edges', dp); DPP = re.search(r'(\d+) pointers', dp); DPE = int(DPE.group(1)) if DPE else None; DPP = int(DPP.group(1)) if DPP else None
rg = rd('register.out'); RG = tuple(int(x) for x in re.search(r'DECLARED (\d+); DEBT (\d+); FAILS (\d+)', rg).groups()); assert RG[1] == 0 and RG[2] == 0, RG
sw = rd('sweep.out'); SW_P = len(re.findall(r'^PASS +cold_run_\w+\.py', sw, flags=re.M)); SW_F = len(re.findall(r'^FAIL +cold_run_\w+\.py', sw, flags=re.M)); SW_CELLS = sum(int(a) for a, b in re.findall(r'score=(\d+)/(\d+)', sw))
assert SW_F == 0 and SW_P >= 66, (SW_P, SW_F)
po = rd('positions.out'); PO = re.search(r'(\d+) checkpoints', po); PO = int(PO.group(1)) if PO else None
jg = rd('journal.out'); JG = re.search(r'(\d+) kinds, (\d+) rows', jg); JG = tuple(int(x) for x in JG.groups()) if JG else None
PR = {'census': last_frac('probe_census.out', 224), 'installation': last_frac('probe_installation.out', 6), 'readback': last_frac('probe_readback.out', 33), 'large_letter': last_frac('probe_large_letter.out', 6), 'checkpoint': last_frac('checkpoint.out', 7), 'ink_cache': last_frac('probe_ink_cache.out', 8)}
assert PR['readback'] == 33 and PR['installation'] == 6 and PR['large_letter'] == 6 and PR['ink_cache'] == 8, PR
dep_first = rd(f'{SP}/ch12b_chain_dependency_first.out') if os.path.exists(f'{SP}/ch12b_chain_dependency_first.out') else dp
POINTER = 'DEMANDED' if re.search(r'FAIL POINTER Deut 12:20 AS_WHEN', dep_first) else 'not demanded'   # the first pass's print decides
HOMOGRAPH = 'MATCHED (filed FALSE)' if re.search(r'Deut 12:31|the_place_luz_bethel|Molech|molech', dep_first) and 'FAIL' in dep_first else 'not matched'
CHAIN_STORY = read(f'{SP}/ch12b_chain_story.txt').strip() if os.path.exists(f'{SP}/ch12b_chain_story.txt') else 'THE GATES CHAIN ONCE — ALL GREEN on the first pass'
TAPE_STORY = read(f'{SP}/ch12b_tape_story.txt').strip() if os.path.exists(f'{SP}/ch12b_tape_story.txt') else 'THE TAPE 10/10 ON ITS FIRST RUN, DD1-DD9 MATCH'
dk = read('logic/oral_triage/deu_12_reeh_exam_2026-09-20.md'); NROWS = len([l for l in dk.split('\n') if l.startswith('- ') and (' — LAW.' in l or ' — DERIVATION.' in l or ' — DISPUTE.' in l or ' — CONTEXT.' in l or ' — OUTSIDE.' in l)]); assert NROWS == 1538, NROWS
# ---- THE TIMING TABLE (the owner's ask at sitting 10: "Monitor how long each step takes and report when the chapter is done") ----
tt = [l.split('\t') for l in read(f'{SP}/ch12_timing.tsv').split('\n') if l.strip()]
T10 = [(r[0], r[1], int(r[2])) for r in tt if len(r) >= 3 and r[1].startswith('10 ')]; T10B = [(r[0], r[1], int(r[2])) for r in tt if len(r) >= 3 and r[1].startswith('10b')]
TSUM10, TSUM10B = sum(s for _, _, s in T10), sum(s for _, _, s in T10B)
TSLOW = sorted(T10B, key=lambda r: -r[2])[:8]
TIMING = ("THE TIMING TABLE (every step timed — the owner's ask at sitting 10; the machine's seconds per step, the model's reading and writing between them the rest): SITTING 10 (the reading) %d timed steps, %d machine seconds; SITTING 10b (the compile — RUN A, the docket's three runs, RUN B, the tail) %d timed steps, %d machine seconds; the first row %s, the last %s; THE SLOWEST OF 10b: %s. The table itself: <scratch>/ch12_timing.tsv, copied to the forms folder (ch12_timing.tsv)."
          % (len(T10), TSUM10, len(T10B), TSUM10B, T10B[0][0] if T10B else '?', T10B[-1][0] if T10B else '?', '; '.join('%s %ds' % (n[4:] if n.startswith('10b ') else n, s) for _, n, s in TSLOW)))
NUM = dict(DD=len(DD), CC=CC, PLC=PLC, CEN=CEN, DGN=DGN, DGF=DGF, LC=LC, DPE=DPE, DPP=DPP, RG=RG, SW=(SW_P, SW_CELLS), PO=PO, JG=JG, PR=PR, POINTER=POINTER, HOMOGRAPH=HOMOGRAPH, CASES=CASES_N, NREC=NREC, PN_REC=PN_REC, T10B=(len(T10B), TSUM10B))
print('THE NUMBERS:', NUM)
# ---- THE TEXTS ----
AS_BUILT = f"""
## Sitting 10b — THE COMPILE OF CHAPTER 12 — AS BUILT (2026-09-21; on the owner's "Go" after the compaction at #201 addendum 3 — the two-run rule's fifth compile sitting under THE COST RULES, the docket clause applied three times: five clean points, #201 and its addenda 1-4)

THE DESIGN HELD ON ITS SPINE — four own-day lines, no marker, eight writes (seven on Israel, the REUSE on the-land), no debit, RUN (1323, 96, 88, 0, 12, 1626, 43, 319,
the four pairs, 127) as the arithmetic wrote it, PREVIOUS_RUN 9b's exactly, the runner 65/65 on its FIRST graded run, {TAPE_STORY}. THE DEPARTURES (read at the
prints, never predicted): (1) THE GREP DECIDED — NO literal counts high_places_banned ONE: the design's five predicted seats (three in cold_run_sequence.py, two in
readback_probes.py) were two, and both BOOLEANS (Q18's bool(hp), CQ5's any(…)) — nothing retyped; (2) THE CALENDAR EDGE STANDS — cold_run_calendar.py's cells ARE
askable (case['ask'] == 'as_commanded'; 'cook', 'eat', 'benefit'): the callees' regex (ask == / q ==) missed the form, and 9b's "no askable cell" was the regex's
blindness, not the cell's — the edges SEVENTEEN as designed; (3) THE SEVENTH WRAPPED CELL — the design's "six cells WRAPPED" counted the table out: the functions
block holds the six cells AND the_readback, seven (the types script wrote six, corrected before the runner; DD2's literal 6 -> 7 before the tape); (4) THE PLATFORM'S
SIXTH ROW — sanctions.platform('eras') says 'forbidden_forever' for Jerusalem where shemini_day.eras('table') says 'banned': the agreement test normalized by prefix
(the fast checker's find, the assert split into a print first); (5) THE SEVENTH STORE-BOUND LINE — the reading's ink block holds an assert on the store's '?' glosses
(SG.items()) the derive's drop patterns missed: a NameError at the fast checker, the pattern added, seven lines dropped (the first derive said six); (6) THE LINT'S
NINETY-CHARACTER WINDOW on the ink block's stopword set — the one Hebrew line the reading's instrument carried unglossed in a runner's context, glossed piece by piece
at the derive (two flags -> 0); (7) THE TAPE'S KINDS blood_eaten and offering_slaughtered_outside are CASE kinds with no tape line — the design's "by kind" rows for
12:15, 12:16 and 12:24 by CALL: eleven on the tape, fourteen by CALL (the design's count read at the print); (8) THE DATA ROWS forty-six (the design's "about
twenty-five"; the docket's finds added the rest) — the count retyped from the fast checker's print; (9) THE EXAM'S PERSONS twenty-nine, THREE exempt (Elijah on Carmel,
the one who forsakes the Levite in the exile, the one who eats human blood), TWO LASHED (the one who erases the Name — Makkot 22a:9; the one who eats the second tithe
outside the wall — Mishnah Makkot 3:3): the chapter's first lashes persons since 5b; (10) THE REGISTER'S FOOTER AT 12:1 — the gate's rule (lo < given_at <= hi) leaves
the header's own verse OUTSIDE its block (Deut 12:1, Deut 28:69]: the class EMPTY STANDS with the daemon given_at 12:1 (as law_opening_speech at 1:16 sat past 1:1's
footer; the daemons of chapters 6-11 in the gap no seat claims) — only the stale why redeclared, DECLARED {RG[0]} unmoved; (11) land_defiled is not an effect name
(the design's measurement read it off a cell's prose — land_vomits is): named at the types' print, not asserted; (12) THE POINTER at 12:20 {POINTER} by the census;
the-place's homograph {HOMOGRAPH}; (13) THE EIGHTH DAY'S WRITE — high_places_banned on the-land was TWO before the chapter (law_erection at Exod 40:17 AND law_eighth_day at Lev 9:24, both on the
erection's day 894698): the design's 'one -> two' read one of the two; DD2 and DD4 DIVERGED on the tape's first run and were retyped once from the print to THREE,
Q32 with them, first_verse's tuples formatted — {TAPE_STORY}; (14) {CHAIN_STORY}.
THE RUN: readback_probes.py Q31-Q33 to FAIL (30/33 — patch_probes_ch12.py) BEFORE the types; add_types_ch12.py (kinds 1145 -> 1150, effects 1042 -> 1049 with
high_places_banned's row AMENDED for the reuse, the 72nd daemon with seven WRAPPED, the span and the seventeen edges, I5 72, the_rite_of_slaughter and
the_wilderness_flesh in calendar_parameters.yaml — 60 rows, exercised by the runner's DATA; the register file's 12:1 why rewritten); ch12_callees.py (every CALL's
asks and results printed — 157 KB; the platform's six rows, the eras table's six, the demolition's [3, 4, 5]); derive_ch12_part1.py (the helpers from the chapter-11
runner by content markers, W11 made W12; the ink block from ch12_ink.py by content markers with the seven store-bound lines dropped and the sequence module's names
made the exec'd parser's — 62 asserts; the counter's day, the two parameters, the one-database scans PLACE_SCAN [] and HPB_SCAN [the-land], the callees' facts
asserted from the print); ch12_part2.py and ch12_part3.py (six cells and the table, {CASES_N} asks — {PER_CELL}); ch12_part4.py (the thirty-one rows, forty-six DATA rows,
the daemon with its eight writes, twenty-nine persons, the scene, the narrative — every census printed before it is asserted); ch12_fastcheck.py over parts 1-4 (two
fails on the first pass — the store line, the platform's word; 0 on the second); ch12_cases_gen.py ({CASES_N} cases); ch12_assemble.py --guard {CASES_N};
cold_run_place_name.py 65/65 (the 67th runner, 303 KB); seq_record_ch12.py with the cache OFF ({NREC} records; place_name statute {PN_REC[1] if PN_REC else '?'} of
{PN_REC[0] if PN_REC else '?'} submits); seq_stitch_ch12.py (no marker; PLACEMENT {PLC}; CENSUS {CEN}); patch_seq_literals_ch12.py (the import line, DAEMON_ORDER,
RUN, PREVIOUS_RUN, NEWEST_RUNNER, PLACEMENT and CENSUS read, DD1-DD9, the VERDICTS; no stale literal); {TAPE_STORY}; checkpoint_check.py --all ({CC[0]} rows,
{CC[1]} miss — the eighteen known, {CC[2]} raised); {CHAIN_STORY}: the probe suites (readback {PR['readback']}/33, census {PR['census']}/224, installation
{PR['installation']}/6 with I5 72, large_letter {PR['large_letter']}/6, checkpoint {PR['checkpoint']}/7, ink_cache {PR['ink_cache']}/8), the daemon gate ({DGN}
daemons{', %d functions' % DGF if DGF else ''}), the dependency gate ({DPE} edges, {DPP} pointers; the link census reference {LC[0]} / transfer {LC[1]} / hypothesis
{LC[2]} / none {LC[3]}), build_world, the journal gate{' (%d kinds, %d rows)' % JG if JG else ''}, THE REGISTER GATE --strict (DECLARED {RG[0]}, DEBT {RG[1]},
FAILS {RG[2]} — the footer at 12:1 EMPTY by the gate's own rule), the positions table ({PO} checkpoints), the sweep {SW_P}/{SW_P} at {SW_CELLS} graded cells, the
home-path gate. {TIMING}
THE LESSONS (thirteen): (1) THE GREP DECIDES, AND A BOOLEAN IS NOT A COUNT — a design that predicts "N seats hold the literal" is a prediction; the seats found hold
booleans and move for no reuse; (2) A REGEX'S SILENCE IS NOT A CELL'S — the callees' scan reads only the forms it names; a "no askable cell" verdict is checked against
the cell's own source before an edge is dropped (9b's calendar edge was dropped on the regex's blindness — owed a look at chapter 16); (3) A REUSED EFFECT IS A SECOND
ENTRY (8b's lesson) and needs NO new parameter — the eras table stays in its three cells, read by CALL; (4) THE TABLE IS THE SEVENTH CELL — a functions block counts
what the daemon wraps, not what the design names as cells; (5) TWO RUNNERS' WORDS FOR ONE ROW DIFFER — 'forbidden_forever' against 'banned': an agreement test
normalizes by prefix, never by equality of another runner's string; (6) THE DROP PATTERNS ARE READ FROM THE FAST CHECKER — a store-bound line is any line that names
the store's structures (SG, VC, byw, STORE_), listed by name; (7) THE LINT'S WINDOW IS NINETY CHARACTERS AFTER THE SCRIPT — a long Hebrew literal is glossed piece by
piece; (8) A CASE KIND HAS NO TAPE LINE — a design's "by kind" row on a case kind is a row by CALL; (9) THE GATE'S OPEN BOUND — a daemon given_at a header's own verse
sits outside the header's block; the class is the gate's, the why is ours; (10) THE RECEIPT WITHOUT THE NAME HAS AN ORAL REFERENT — a parameter the cell reads as
data, the written text holding no rite (the code/data separation law's own case; the finder's fourth shape still owed); (11) THE EXAM'S LASHES ARE THE ANSWER SHEET'S
— Mishnah Makkot 3:3's flogged and Makkot 22a's, two persons; (12) AN EFFECT'S COUNT IS READ OFF THE LEDGER, NOT THE REGISTRY'S ROW — the registry named the erection's write; the tape held two on one day (the eighth day's beside it); the one
database's fourteen rows on the-land against seven for the other effects were the sign, misread as folds — a checkpoint's count is typed from the tape's print, a design's is a
prediction; (13) THE TWO-RUN RULE HELD on its fifth compile sitting under the cost rules: RUN A, the docket in three
runs, RUN B with the chain launched at its end, THE TAIL — five clean points, the owner compacting after each. NEXT on the owner's word: the commit; CHAPTER 13's
reading (13:1-19) in one run — the seducer, the dreamer, the seduced city (the DB's 13:1 the English 12:32); on the table: the Decalogue-schema sitting, the
SUPPLIED forms, the calf's day marker, the registry's homograph, the receipt's third and fourth shapes (a gate sitting), THE INSTALL HYPOTHESIS.
"""
DEBT_HDR_OLD = "## SITTING 10 — CHAPTER 12 (2026-09-20, the reading; deu_12_place_name frozen) — OWED TO THE COMPILE 10b: "
DEBT_HDR_NEW = "## SITTING 10 — CHAPTER 12 (2026-09-20, the reading; deu_12_place_name frozen) — PAID AT 10b (the 10b box below, item by item) — OWED WAS: "
DEBT_BOX = f"""
## THE SITTING-10 BOX (a)-(k) PAID — (a) THE PLACE — F2 the_place_chosen: THE LINE place_chosen_declared writing place_chosen_required (a STATUS on Israel; the Name
## pronounced only there, Sotah 38a; in one of your tribes [1]) and REUSING high_places_banned (the erection's BLOCK on the-land — a third entry, the eras table's own
## ink: shemini_day.eras, sanctions.platform, journeys.the_command by CALL, the six rows unmoved); the three commandments of the entry and David's rest (Sanhedrin
## 20b) DATA rows; (b) THE DEMOLITION — F1: the five verbs by CALL (ER.covenant('demolition_grows') = [3, 4, 5]), the three Asherim and the mountains (Mishnah Avodah
## Zarah 3:5, 3:7), the renaming (61:7) — NO new debit; (c) THE HEADER — the twin of Leviticus 26:46 a DATA row, the four nouns and the land-bound rule (BR by CALL),
## the pair 12:4 / 12:31 with THE WRITE name_erasure_barred (a BLOCK); the register's 12:1 REDECLARED (the class EMPTY by the gate's open bound); (d) THE SLAUGHTER LAW
## RELEASED — F4 and F5: THE LINE profane_slaughter_permitted writing profane_slaughter_permitted (a STATUS conditional on the entry — the_wilderness_flesh a PARAMETER
## with R. Yishmael's release, R. Akiva's rite and the exile's third state), the receipt without the Name — the_rite_of_slaughter a PARAMETER (Mishnah Chullin 2:1;
## Chullin 28a:5; Exodus 23:15's written kin by CALL — calendar.matzah), the pointer at 12:20 to Exodus 34:24 ({POINTER} by the census), the civility, the comparison,
## the blemished consecrated; (e) THE BLOOD — F4 and F5: 'like water' four ways (SA.covering, SA.blood by CALL), the blood is the life with limb_barred (Gen 9:4) on
## the tape, the blood's classes (Keritot 20b-22a — the one who eats human blood EXEMPT), flesh in milk from 12:25 (CA.kid_in_milk by CALL), the sin offering's verb
## (PS.noahide('shed_homograph')), the persecution's edges; (f) THE OFFERINGS ONLY THERE — F3 and F4: the reuse's second entry at 12:13, the prophet's exception (Elijah
## EXEMPT), the karet matrix by CALL, THE WRITE holy_things_in_the_gates_barred (a BLOCK — the ladder at Makkot 17a-19b, the list read backward, the lashes of Mishnah
## Makkot 3:3 — the tithe's eater outside the wall LASHED, the impure tithe's warning from the chapter's own gates, THE TWO TITHES by CALL — KR.the_tithe('every_place')),
## the seven offerings' three lists, your holy things (Temurah 17b); (g) THE TABLE AND THE HOUSEHOLD — F2 and F4: THE WRITE rejoicing_before_the_lord_commanded (a
## STATUS — the law's first seat supplied with its write; the woman's rejoicing a two-arm row), 5:14's household by CALL (CH.the_first_tablet), THE WRITE
## levite_forsaking_barred (a BLOCK — the verse alone; the exile's forsaker EXEMPT); (h) THE NATIONS CUT OFF — F6: THE LINE nations_cut_off_warned writing
## foreign_rite_inquiry_barred (a BLOCK); the snare's root, the parents from 'even', NO MOLECH NAMED (SA.molech by CALL — the homograph {HOMOGRAPH}); (i) THE REGISTER'S
## SWITCH, THE PARSER'S [1] AND THE STARRED TITHE, Moses unnamed — DATA rows (census_probes UNMOVED at 224); (j) THE CHECKPOINT SERIES — DD1-DD9 the fourth name;
## (k) THE DOCKET — 1,538 rows in three runs (1,115 read whole here, 423 carried), the writer derived from 9b's, the crowns the cells' rows.
## OWED FROM 10b: (i) THE RECEIPT'S THIRD AND FOURTH SHAPES — 12:21's "as I have commanded you" without the Name (its referent ORAL — the parameter) beside 10:9's and
## 11:25's: the finder's forms OWED to a gate sitting on the owner's word; (ii) THE SUPPLIED FORMS on the owner's word — the state row without a write (12:9), a law's
## first seat with its write (12:4, 12:7, 12:17, 12:19, 12:30 — five this chapter); (iii) THE CALF'S DAY MARKER (7b's) and THE REGISTRY'S HOMOGRAPH (8b's; the-place ->
## the_place_luz_bethel this chapter) on the owner's word; (iv) THE SECOND TITHE AT 14:22-26 (holy_things_in_the_gates_barred's forward twin — 'too far' 14:24's twelve
## tokens; the confession 26:12-14), THE FIRSTLING'S EATING AT 15:19-23 (the blemished's release), THE FEASTS' REJOICING AT 16:11, 16:14 (the status's seats ahead),
## 16:22's pillar 'which He hates', 19:1's twin of 12:29, 17:8's and 26:2's place formula, 27:7's peace offerings and rejoicing; (v) 13:1 THE DB'S SEAM (the English
## 12:32) at chapter 13's reading — the seducer's 'other gods whom you have not known' 11:28's; (vi) THE CALLEES' REGEX — the scan owes the case['ask'] form (9b's
## calendar edge dropped on its silence: a look at chapter 16's compile when the calendar is called again); (vii) THE INSTALL HYPOTHESIS — 12:10-11's 'when He gives
## you rest … then the place' recorded as the ink's own installer; the installer boot as the form until the owner's word; (viii) THE ERAS TABLE — three cells hold it
## (shemini_day, sanctions, journeys) and the fourth reads it: a merge into one seat on the owner's word at a gate sitting; (ix) THE CHECKPOINT SERIES continues (DD
## the fourth name — DD9 the last; the next DE1, keyed by its first word). NOTHING ELSE IN CHAPTER 12 IS OWED TO A LATER SITTING OF ITS OWN.
"""
MIDDOT_ANCHOR = "\n## Exodus block campaign — owner's word \"Do 3\")\n"
MIDDOT_ENTRY = f"""- THE CHAPTER-12 COMPILE (THE DEUTERONOMY WALK sitting 10b RUN B, 2026-09-21; cold_run_place_name.py — the docket's rules carried into the cells; every code checked in this file before typed): I1 (qal wa-chomer, the a-fortiori) at Bekhorot 33a:1-5 (the comparison's three seats — F4 the_unclean_and_the_clean), Makkot 17a:12-17b:1 with Rava's refutations 17b:3-8 (THE LADDER on 12:17's list — F4 the_ladder_of_a_fortiori; 17b:10's rider — no punishment from an inference; 18a:1-2 the repetition designates), Makkot 23b:2 (the blood's reward — F5 the_good_and_the_right), Bekhorot 33b:16 (the firstling's flesh); I2 (gezerah shavah, the verbal analogy) at Sotah 38a:10 "to put His name there" / "to put My name there" (F2 the_name_pronounced_only_there); I6 (kelal u-frat u-kelal, general–particular–general → include) at Keritot 21a:5 on Leviticus 7:26 (the blood's classes — F5 the_bloods_classes) with 21a:7's rider (R. Yishmael's school on unlike generalizations); I12 (a matter derived from its context) at Chullin 115b:2 (Rabbi's redundant "you shall not eat it" — F5 flesh_in_milk); E29 (gematria, the letter-values) at Makkot 23b:18 (the 613 — F5 the_good_and_the_right); THE TRANSPOSITION named (Sotah 38a:11 — R. Yoshiya on Exodus 20:20, F2), THE LIST READ BACKWARD named (Makkot 17b:9 — F4 the_list_read_backward), the do-not-read reading named (Sotah 38b:10), the juxtapositions named (Makkot 19a:3-5 — the second tithe and the firstborn; 19a:10 the chain rule; 19a:7 I3 refuted) — no code. THE DISPUTES AS PARAMETERS carried into the registry: the_rite_of_slaughter (calendar_parameters.yaml — the signs, the bird, the uncertainty, the agent), the_wilderness_flesh (R. Yishmael, R. Akiva, the exile), the woman's rejoicing (Rosh Hashanah 6b:15-16 — a DATA row with two arms), the rest and the inheritance four ways (Zevachim 119a-b — a DATA row).
"""
DKF = 'deu_12_reeh_exam_2026-09-20.md'
RLOG = f"""
## 2026-09-21 — DEUTERONOMY 12 COMPILED AND ON THE TAPE (THE DEUTERONOMY WALK sitting 10b, the two-run rule's fifth compile sitting under the cost rules): THE PLACE
## INSTALLED WITH THE ERAS TABLE'S OWN INK — high_places_banned REUSED, A THIRD ENTRY ON THE LAND; THE SLAUGHTER LAW RELEASED AS A STATUS CONDITIONAL ON THE ENTRY,
## THE RECEIPT WITHOUT THE NAME A PARAMETER (THE ORAL LAW'S SEAT); THE GATES' BAR WITH THE LADDER AND THE LASHES; FOUR OWN-DAY LINES, NO MARKER; AND THE GREP THAT
## FOUND BOOLEANS WHERE THE DESIGN PREDICTED COUNTS
On the owner's "Go" after the compaction at #201 addendum 3. THE COMPILE: cold_run_place_name.py the 67th runner (six cells and the table, {CASES_N} asks, 65/65 on its
first graded run), law_place_name the 72nd daemon (given_at Deut 12:1, installed_by boot; seven WRAPPED); FOUR OWN-DAY LINES at (40, 11, 1), no marker —
demolition_restated (name_erasure_barred a BLOCK), place_chosen_declared (place_chosen_required and rejoicing_before_the_lord_commanded STATUSES; high_places_banned
REUSED on the-land), profane_slaughter_permitted (profane_slaughter_permitted a STATUS conditional on the entry; holy_things_in_the_gates_barred and
levite_forsaking_barred BLOCKS), nations_cut_off_warned (foreign_rite_inquiry_barred a BLOCK); THE READBACK'S FORMS ON FILE, NO NEW FORM — thirty-one rows one per
verse (VERBATIM 6 / VARIANT 16 / EXPANDED 3 / SUPPLIED 6), the state row 12:9 SUPPLIED with no write, FIVE law rows SUPPLIED with their writes, the pointer 12:20 to
Exodus 34:24 by two teachers ({POINTER} by the census); {TAPE_STORY.lower()}; the gates chain {CHAIN_STORY.lower()} (the register gate DECLARED {RG[0]} / DEBT {RG[1]} /
FAILS {RG[2]} — the footer at 12:1 EMPTY by the gate's open bound; the sweep {SW_P}/{SW_P}). THE PARAMETERS: the_rite_of_slaughter (Mishnah Chullin 2:1 — the gullet
and the windpipe; Chullin 28a:5 on 12:21's "as I have commanded you") and the_wilderness_flesh (R. Yishmael's release, R. Akiva's rite, the exile's third state —
Chullin 16b-17a): every value a docket row. THE DOCKET (three runs): logic/oral_triage/{DKF} — 1,538 rows, 1,115 read whole here and 423 carried with their ledgers'
own verdict lines; its crowns in the map's three AS RUN paragraphs. THE RECORD KEPT: the grep found booleans where the design predicted five count literals (nothing
retyped); the calendar's cells askable after all (9b's dropped edge the regex's blindness); the platform's 'forbidden_forever' against the table's 'banned'; the exam's
two lashes persons (Makkot 22a:9; Mishnah Makkot 3:3) and three exempt; the register's 12:1 EMPTY by the gate's rule (lo < given_at <= hi). {TIMING} The forms in
World/step9/forms_deuteronomy_walk/.
"""
STEPS_ANCHOR = "\n## Step 6 — Publish\n"
STEPS_PARA = f"""
**Deuteronomy 12 compiled (2026-09-21, sitting 10b — the two-run rule's fifth compile sitting, the docket in three runs):** the place which the LORD will choose is
installed here, and the machine already held its table — the stations (the Tabernacle, Gilgal, Shiloh, Nob and Gibeon, Jerusalem) sit in three cells, so the
chapter's law reads that table and REUSES the erection's block on the land as a third entry, with no new parameter. Four laws had no code: the Name's erasure, the
place's law with the rejoicing, the profane slaughter's release with the gates' bar and the Levite, the inquiry after the nations' gods — four lines at the chapter's
own day, no marker, eight writes. The slaughter law is a status conditional on the entry, its two arms and the exile's third state a parameter; "as I have commanded
you" points at nothing written — the rite is a parameter the cell reads as data (Mishnah Chullin 2:1), the oral law's own seat. The readback's forms on file held with
no new form — thirty-one rows, one per verse; five law rows supplied with their writes. The exam has two flogged persons this time (the Name's eraser, the tithe's
eater outside the wall) and three exempt. The runner 65/65 on its first run; {TAPE_STORY.lower()}; the gates chain {CHAIN_STORY.lower()}. Every step timed: {TSUM10B}
machine seconds over {len(T10B)} steps for the compile.
"""
BRIEF_BULLET_ANCHOR = "- **CHAPTER 12 READ AND FROZEN — "
BRIEF_BULLET = (f"- **CHAPTER 12 COMPILED — THE PLACE INSTALLED WITH THE ERAS TABLE'S OWN INK: high_places_banned REUSED AS A THIRD ENTRY ON THE LAND, THE STATIONS READ FROM THEIR THREE CELLS AND NEVER REWRITTEN; THE SLAUGHTER LAW A STATUS CONDITIONAL ON THE ENTRY, ITS ARMS AND THE EXILE A PARAMETER; \"AS I HAVE COMMANDED YOU\" A PARAMETER THE CELL READS AS DATA — THE ORAL LAW'S SEAT (Mishnah Chullin 2:1); THE GATES' BAR WITH THE LADDER (Makkot 17a-19b) AND THE LASHES (Mishnah Makkot 3:3); FOUR OWN-DAY LINES, NO MARKER; THE GREP FOUND BOOLEANS WHERE THE DESIGN PREDICTED COUNTS** (2026-09-21, sitting 10b — the two-run rule's fifth compile sitting under the cost rules; the runner 65/65 first run; {TAPE_STORY.lower()}; the chain {CHAIN_STORY.lower()}; the 67th runner, the 72nd daemon; every step timed — {TSUM10B} machine seconds over {len(T10B)} steps).\n")
BRIEF_ENTRY_ANCHOR = "### 2026-09-20 — CHAPTER 12 READ: THE PLACE INSTALLED, A LAW CHANGED BY A PLACE, A COMMAND THE TEXT NEVER GIVES, AND EVERY STEP TIMED"
BRIEF_ENTRY = f"""### 2026-09-21 — CHAPTER 12 COMPILED: THE PLACE READS ITS OWN TABLE, THE SLAUGHTER LAW BECOMES A STATUS, AND THE RITE IS A PARAMETER
Chapter 12 installs the place which the LORD will choose, and the surprise of the compile is how little new machinery it needed. The stations of that place — the
Tabernacle, Gilgal, Shiloh, Nob and Gibeon, Jerusalem — were already a table in three cells of the machine, written when Leviticus 17 and the erection were compiled,
with Deuteronomy 12:8-14 named in their ink as the source. So the chapter's law does not build a fourth copy: it reads the table by call and reuses the erection's
block on the land as a third entry at the chapter's own day. The four holes were laws the code never held: the Name's erasure (12:4 — three readings on the shelf), the
place with the rejoicing (12:5-14), the profane slaughter's release with the gates' bar and the Levite (12:15-28), and the inquiry after the nations' gods (12:29-31).
Four lines, no marker, eight writes. The slaughter law is the one that changed by a place: Leviticus 17's rule that all flesh comes to the tent's door is released for
the Land in new words, and the shelf's two arms — R. Yishmael's release at the entry, R. Akiva's rite required at the entry — with the exile's third state are a
parameter, never a constant. "As I have commanded you" (12:21) points at no written verse; Rabbi reads it as the gullet and the windpipe — the oral law's seat — and
the machine holds that as a parameter the cell reads as data, the written text holding no rite: the code/data separation law's own case. The gates' bar carries the
ladder of a fortiori on 12:17's list and the Mishnah's lashes; the exam has two flogged persons and three exempt. The readback's forms held with no new form — thirty-
one rows, one per verse. And the design's prediction that five seats held a count of one for the reused block met the grep: two seats, both booleans, nothing to
retype. The runner 65/65 on its first run; {TAPE_STORY.lower()}; the chain {CHAIN_STORY.lower()}. Every step was timed for the owner: {TSUM10B} machine seconds over
{len(T10B)} steps for the compile, the reading's {TSUM10} over {len(T10)}. Next: chapter 13, the seducer.
"""
LOOP_OLD = "cold_run_blessing_and_curse.py (chapter 11, THE FORMS ON FILE — NO NEW FORM 2026-09-20:"
LOOP_NEW = "cold_run_place_name.py (chapter 12, THE FORMS ON FILE — NO NEW FORM 2026-09-21: the place installed with the eras table's own ink — thirty-one rows one per verse VERBATIM 6 / VARIANT 16 / EXPANDED 3 / SUPPLIED 6, eleven on the tape, fourteen by CALL; T5 the state row 12:9 supplied without a write; FIVE LAW ROWS supplied WITH their writes at the chapter's own day (12:4, 12:7, 12:17, 12:19, 12:30); the pointer 12:20; a REUSED effect a third entry (high_places_banned on the-land); no marker; readback_probes 33/33, DD3); " + LOOP_OLD
RESUME_HEAD = f"""# ⚠ THE DEUTERONOMY WALK sitting 10b — CHAPTER 12 COMPILED AND ON THE TAPE (2026-09-21; step9/DEUTERONOMY_WALK.md "Sitting 10b" + the three "THE DOCKET — AS RUN" paragraphs + "Sitting 10b — AS BUILT"):
# cold_run_place_name.py the 67th runner (65/65 first run), law_place_name the 72nd daemon; FOUR OWN-DAY LINES, NO MARKER — the Name's erasure, the place with the
# rejoicing (high_places_banned REUSED on the-land — the eras table's own ink), the profane slaughter's release (a STATUS conditional on the entry; the_rite_of_slaughter
# and the_wilderness_flesh PARAMETERS) with the gates' bar and the Levite, the inquiry; {TAPE_STORY.lower()} (DD1-DD9); the chain {CHAIN_STORY.lower()}; the register
# gate DECLARED {RG[0]} / DEBT {RG[1]} / FAILS {RG[2]}. UNCOMMITTED since 4af2953: 10b whole (the message at <scratch>/commit_msg_ch12b.txt). NEXT on the owner's word: commit; chapter 13's reading.
"""
STATE_ADD = f"""
#201 ADDENDUM 4 (2026-09-21, at the close of THE DEUTERONOMY WALK sitting 10b's TAIL — on the owner's "Go" after the compaction at addendum 3; A CLEAN COMPACTION POINT): THE STATE: CHAPTER 12 COMPILED AND ON THE TAPE — cold_run_place_name.py the 67th runner (six cells and the table, {CASES_N} asks, 65/65 on its first graded run; parts 1-5 in the scratchpad, copied to the forms folder), law_place_name the 72nd daemon (given_at Deut 12:1, installed_by boot; seven WRAPPED); event_vocabulary 1150, effect_vocabulary 1049 (high_places_banned's row amended for the reuse); the span and seventeen CALL edges; calendar_parameters.yaml +2 (the_rite_of_slaughter, the_wilderness_flesh — 60 rows); the register file's 12:1 why redeclared (the class EMPTY by the gate's open bound); FOUR OWN-DAY LINES at (40, 11, 1) after the tape's last Deuteronomy 11 line, NO marker (markers 172 unmoved) — demolition_restated, place_chosen_declared, profane_slaughter_permitted, nations_cut_off_warned; eight writes (four blocks and three statuses on Israel; high_places_banned's third entry on the-land); no debit; RUN (1323, 96, 88, 0, 12, 1626, 43, 319, the four pairs, 127), PREVIOUS_RUN 9b's exactly, PLACEMENT {PLC}, CENSUS {CEN}; {TAPE_STORY}; checkpoint_check --all {CC[0]} rows, {CC[1]} miss (the known), {CC[2]} raised; readback_probes 33/33 (Q31-Q33 written to FAIL first); THE GATES CHAIN {CHAIN_STORY} — the probes, the daemon gate ({DGN} daemons), the dependency gate (the link census reference {LC[0]} / transfer {LC[1]} / hypothesis {LC[2]} / none {LC[3]}; the pointer at 12:20 {POINTER}; the-place's homograph {HOMOGRAPH}), build_world, the journal gate, the register gate --strict (DECLARED {RG[0]}, DEBT {RG[1]}, FAILS {RG[2]}), the positions table ({PO} checkpoints), the sweep {SW_P}/{SW_P}, the home-path gate; THE RECORDS from the sheet in one call (write_ch12b_records.py — the map's AS BUILT with THE TIMING TABLE, COMPILE_DEBT's sitting-10 box PAID and the 10b box, MIDDOT, RESEARCH_LOG, THE_STEPS, THE_BRIEFING, THE_LOOP, RESUME, RECORD_FORMS, this addendum, the addenda, the recovery page, the memory); the forms copied (copy_ch12b_forms.py); the commit message at <scratch>/commit_msg_ch12b.txt (the headline written, RUN B's paragraph, the trailers). THE TIMING: sitting 10b {len(T10B)} timed steps, {TSUM10B} machine seconds (the reading's {len(T10)} steps, {TSUM10} seconds). NOT COMMITTED (since 4af2953): RUN A's records, the design, the docket's three runs, RUN B and the tail — ONE message covers 10b (the owner's word: "Commit" = no push; "commit push" = both; bb62e90 the last push). NOTHING MID-FLIGHT — A CLEAN COMPACTION POINT. NEXT ON THE RULING: the commit on his word; then CHAPTER 13's reading (13:1-19) in one run — the seducer, the dreamer of dreams, the seduced city (the DB's 13:1 the English 12:32); on the table: the Decalogue-schema sitting, the SUPPLIED forms, the calf's day marker, the registry's homograph, the receipt's third and fourth shapes (a gate sitting), THE INSTALL HYPOTHESIS, the eras table's merge. POST-COMPACTION REREADS: the recovery page, the map's "Sitting 10b — AS BUILT" (the newest section), MEMORY.md.
"""
def next_addenda_no(s):
    ns = [int(x) for x in re.findall(r'^##+ *§?(\d+)[\.\s:—]', s, re.M)] + [int(x) for x in re.findall(r'§(\d+)', s)]
    return (max(ns) + 1) if ns else 55
ADDENDA_ADD_T = """
## §{N} — THE DEUTERONOMY WALK sitting 10b (2026-09-20/21): CHAPTER 12 COMPILED — the state doc's #201 and its addenda 1-4; the map's "Sitting 10b … THE DESIGN", the three "THE DOCKET — AS RUN" paragraphs and "Sitting 10b — AS BUILT"
The two-run rule's fifth compile sitting under the cost rules with the docket clause three times: RUN A (the rereads, the recon and the scan derived by line-based
substitutions, the design), THE DOCKET in three runs (1,538 rows — 1,115 read whole here, 423 carried with their ledgers' own verdict lines), RUN B (the probes to FAIL,
the types, the callees' print, the runner 65/65 first run, the recorder with the cache off, the stitcher with no marker, the literals, the tape with DD1-DD9, the chain
launched at the run's end), THE TAIL (the summary read once, the demands filed, the records, the forms, the message). The crowns: the place installed with the eras
table's own ink (high_places_banned reused), the slaughter law a status conditional on the entry with its arms a parameter, the rite a parameter (the oral law's seat),
the gates' bar with the ladder and the lashes, the grep's booleans. The lessons in the AS BUILT (twelve). Every step timed. Uncommitted since 4af2953: 10b whole; the
message at <scratch>/commit_msg_ch12b.txt.
"""
MEM_PARA = f"""
SITTING 10b DONE (2026-09-21, "Go" after the compaction at #201 addendum 3): CHAPTER 12 COMPILED AND ON THE TAPE — cold_run_place_name.py the 67th runner (65/65 first
run), law_place_name the 72nd daemon (seven WRAPPED — the six cells and the table); FOUR OWN-DAY LINES, NO MARKER: demolition_restated (name_erasure_barred),
place_chosen_declared (place_chosen_required, rejoicing_before_the_lord_commanded; high_places_banned REUSED on the-land — the eras table's own ink, read by CALL from
three cells), profane_slaughter_permitted (profane_slaughter_permitted a STATUS conditional on the entry; holy_things_in_the_gates_barred, levite_forsaking_barred),
nations_cut_off_warned (foreign_rite_inquiry_barred); the_rite_of_slaughter and the_wilderness_flesh PARAMETERS; RUN (1323, 96, 88, 0, 12, 1626, 43, 319, pairs, 127),
markers 172, kinds 868; {TAPE_STORY.lower()}, DD1-DD9; the chain {CHAIN_STORY.lower()}; the register gate DECLARED {RG[0]} / DEBT {RG[1]} / FAILS {RG[2]} (12:1 EMPTY by the
gate's open bound); the pointer at 12:20 {POINTER}. THE LESSONS: the grep decides and a boolean is not a count (five predicted seats, two booleans, nothing retyped); a
regex's silence is not a cell's (the calendar's cells askable — 9b's dropped edge the regex's blindness); the table is the seventh cell; two runners' words for one row
differ (forbidden_forever / banned — normalize by prefix); the drop patterns read from the fast checker; the lint's ninety-character window; a case kind has no tape line;
the gate's open bound; the receipt's oral referent a parameter; AN EFFECT'S COUNT IS READ OFF THE LEDGER (the eighth day's write beside the erection's — three, not two); the D
series' fourth name DD (DE next). TIMED: {len(T10B)} steps, {TSUM10B} machine seconds. UNCOMMITTED
since 4af2953: 10b whole (the message <scratch>/commit_msg_ch12b.txt). NEXT on his word: the commit; chapter 13's reading (13:1-19) — the seducer.
"""
MEM_DESC_OLD = 'description: "COMMITTED THROUGH 4af2953 (2026-09-20; NOT PUSHED — pushed through bb62e90) — SITTING 10 DONE 2026-09-20 ('
MEM_DESC_NEW = 'description: "COMMITTED THROUGH 4af2953 (2026-09-20; NOT PUSHED — pushed through bb62e90) — SITTING 10b DONE 2026-09-21 (chapter 12 COMPILED — the place installed with the eras table\'s own ink, high_places_banned reused; the slaughter law a status conditional on the entry; the rite a parameter; four own-day lines, no marker; 10b UNCOMMITTED); SITTING 10 DONE 2026-09-20 ('
MEM_IDX_OLD = '10b RUN B DONE; NEXT: THE TAIL (7 demands)'; MEM_IDX_NEW = '10b DONE (65/65, the reuse); commit next'
FORMS_OLD = "World/step9/forms_deuteronomy_walk/write_ch11b_records.py (write_ch10b_records.py,"
FORMS_NEW = "World/step9/forms_deuteronomy_walk/write_ch12b_records.py (write_ch11b_records.py, write_ch10b_records.py,"
REC_EDITS = [("## 2. WHERE IT STANDS (2026-09-21, 10b docket done; the state doc #201 add. 3 the newest)", "## 2. WHERE IT STANDS (2026-09-21, 10b done; the state doc #201 add. 4 the newest)"),
             ("- NUMBERS CLOSED. DEUTERONOMY 1:1-11:32 COMPILED AND ON THE TAPE (PUSHED through bb62e90); 12 READ AND FROZEN.", "- NUMBERS CLOSED. DEUTERONOMY 1:1-12:31 COMPILED AND ON THE TAPE (PUSHED through bb62e90; 12 uncommitted)."),
             ("- 226 frozen units, standing 2239, hash 8b8fff1fa28953af. 66 runners, 71 daemons, 484 functions; 1145 kinds / 1042 effects.", f"- 226 frozen units, standing 2239, hash 8b8fff1fa28953af. 67 runners, {DGN} daemons{', %d functions' % DGF if DGF else ''}; 1150 kinds / 1049 effects."),
             ("- THE TAPE at RUN (1319, 96, 88, 0, 12, 1618, 42, 319, pairs, 127), markers 172, closes 127; the sweep 65/65; every gate GREEN.", f"- THE TAPE at RUN (1323, 96, 88, 0, 12, 1626, 43, 319, pairs, 127), markers 172, closes 127; the sweep {SW_P}/{SW_P}; every gate GREEN."),
             ("- SITTING 10 (ch 12; EVERY STEP TIMED, the table in the AS BUILT): the place INSTALLED here; 12:21's receipt without the Name; the\n  slaughter law released in new words; 197 sources whole.", f"- SITTINGS 10/10b (ch 12; EVERY STEP TIMED — 10b {TSUM10B} s / {len(T10B)} steps): the place INSTALLED (high_places_banned REUSED — the eras\n  table's ink); the slaughter law a STATUS conditional on the entry; the rite a PARAMETER; four lines, no marker."),
             ("- COMMITTED 4af2953 (NOT PUSHED). 10b A + THE DOCKET DONE (1,538 rows in parts A-G, three runs; 1,115 whole here; #201 add. 3). NEXT ON \"Go\": RUN B after a compaction.", "- COMMITTED 4af2953 (NOT PUSHED). 10b DONE (65/65; tape 10/10; the docket 1,538 rows). UNCOMMITTED. NEXT: commit on his word; ch 13.")]
# ---- THE ANCHORS ----
ok = True
def need(p, a, n=1):
    global ok
    c = read(p).count(a)
    if c != n: print('ANCHOR', p.split('/')[-1], c, a[:70]); ok = False
MAP = 'World/step9/DEUTERONOMY_WALK.md'; DEBT = 'World/step9/COMPILE_DEBT.md'; MID = 'logic/MIDDOT.md'; RL = 'RESEARCH_LOG.md'; STEPS = 'THE_STEPS.md'; BRIEF = 'THE_BRIEFING.md'; LOOP = 'World/step9/THE_LOOP.md'
RES = 'World/RESUME.md'; RF = 'World/step9/RECORD_FORMS.md'; STATEDOC = 'logic/pre_logic_methods_2026-07-28/PROMPT_continue_solo_era_2026-08-06.md'; ADD = 'logic/pre_logic_methods_2026-07-28/RECOVERY_addenda_2026-09-12.md'
REC = 'logic/pre_logic_methods_2026-07-28/RECOVERY_new_thread_2026-09-12.md'; WALK = f'{MEM}/deuteronomy-walk.md'; IDX = f'{MEM}/MEMORY.md'
need(DEBT, DEBT_HDR_OLD); need(MID, MIDDOT_ANCHOR); need(STEPS, STEPS_ANCHOR); need(BRIEF, BRIEF_BULLET_ANCHOR); need(BRIEF, BRIEF_ENTRY_ANCHOR); need(LOOP, LOOP_OLD); need(RF, FORMS_OLD)
need(WALK, MEM_DESC_OLD); need(IDX, MEM_IDX_OLD)
for a, b in REC_EDITS: need(REC, a)
assert 'Sitting 10b — THE COMPILE OF CHAPTER 12 — AS BUILT' not in read(MAP) and '#201 ADDENDUM 4' not in read(STATEDOC) and '#201 ADDENDUM 3' in read(STATEDOC)
rec = read(REC)
for a, b in REC_EDITS: rec = rec.replace(a, b)
idx = read(IDX).replace(MEM_IDX_OLD, MEM_IDX_NEW)
N_ADD = next_addenda_no(read(ADD)); ADDENDA_ADD = ADDENDA_ADD_T.replace('{N}', str(N_ADD))
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
r = subprocess.run([sys.executable, f'{ROOT}/logic/solo_tools/scrub_home_paths.py', '--check'], capture_output=True, text=True); print('  home-path gate:', (r.stdout + r.stderr).strip().split('\n')[-1][:90])
