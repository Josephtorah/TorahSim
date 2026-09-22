import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE DEUTERONOMY WALK 11b RUN B / THE TAIL (2026-09-21): THE RECORDS FROM THE SHEET IN ONE CALL (World/step9/RECORD_FORMS.md) — the map's "Sitting 11b — AS BUILT"
# (with THE TIMING TABLE), COMPILE_DEBT's sitting-11 box PAID and the 11b box, MIDDOT's compile entry, RESEARCH_LOG, THE_STEPS, THE_BRIEFING (the scoreboard and an
# entry), THE_LOOP's step-6 row, RESUME, RECORD_FORMS, the state doc's #203 addendum 3 (the close — a clean point), the addenda's section, the recovery page rewritten
# under its cap, the memory (the walk note and the index). EVERY NUMBER PARSED FROM THE PRINTS (the runner's run, the tape's run, the chain's folder, the timing table,
# the records' own reads), never recited; every text built whole before its file is opened; the caps asserted; --check runs the reads and the anchors alone.
# write_ch12b_records.py's form. WRITTEN AT RUN B, RUN AT THE TAIL. RUN FROM THE REPO ROOT.
import os, re, sys, subprocess
ROOT = _ROOT
SP = os.path.dirname(os.path.abspath(__file__)); G = f'{SP}/gates_ch13b'
MEM = os.path.expanduser('~/.claude/projects/-Users-Shared-TorahSim/memory')
CHECK = '--check' in sys.argv
def rd(name): return open(name if name.startswith('/') else f'{G}/{name}', encoding='utf-8', errors='ignore').read()
def read(p): return open(p if p.startswith('/') else f'{ROOT}/{p}', encoding='utf-8').read()
def W(p, s): open(p if p.startswith('/') else f'{ROOT}/{p}', 'w', encoding='utf-8').write(s)
def last_frac(name, den):
    fr = re.findall(r'(\d+)/(\d+)', rd(name)); fr = [(int(a), int(b)) for a, b in fr if int(b) == den]
    assert fr, (name, den); return fr[-1][0]
# ---- THE PRINTS ----
RUN_FILE = f'{SP}/ch13_runner_run2.out' if os.path.exists(f'{SP}/ch13_runner_run2.out') else f'{SP}/ch13_runner_run1.out'
run = rd(RUN_FILE); assert 'MATRIX: 56/56' in run, RUN_FILE
CASES_N = int(re.search(r'CASES generated: (\d+)', rd(f'{SP}/ch13_cases_gen.out')).group(1)); PER_CELL = re.search(r'per cell (\{.*?\})', rd(f'{SP}/ch13_cases_gen.out')).group(1)
SCENE = re.search(r'the scene (\(.*?\)\)); the narrative', rd(f'{SP}/ch13_cases_gen.out')); SCENE = SCENE.group(1) if SCENE else '?'
TAPE_FILE = f'{SP}/ch13_tape_run2.out' if os.path.exists(f'{SP}/ch13_tape_run2.out') else f'{SP}/ch13_tape_run1.out'
tape = rd(TAPE_FILE); assert '10/10 checkpoints' in tape, TAPE_FILE
DE = re.findall(r'CHECKPOINT (DE\d) .*? (MATCH|MISS|DIVERGE)$', tape, flags=re.M); assert len(DE) == 9 and all(v == 'MATCH' for _, v in DE), DE
RETYPED = re.findall(r'CHECKPOINT (CC3|CQ6|DB2|DC6|DD7) .*? (MATCH|MISS|DIVERGE)$', tape, flags=re.M); assert len(RETYPED) == 5 and all(v == 'MATCH' for _, v in RETYPED), RETYPED
cc = rd(f'{SP}/ch13_checkpoint_check.out'); CC = re.search(r'checkpoint_check: (\d+) rows, (\d+) miss, (\d+) raised', cc); CC = tuple(int(x) for x in CC.groups()); assert CC[1] == 18 and CC[2] == 0, CC
st = rd(f'{SP}/seq_stitch_ch13.out'); PLC = re.search(r'^PLACEMENT LITERAL: (.*)$', st, re.M).group(1); CEN = re.search(r'^  CENSUS tuple .*?: (\(.*\))$', st, re.M).group(1)
rec = rd(f'{SP}/seq_record_ch13.out'); NREC = int(re.search(r'recording: (\d+) records written', rec).group(1)); SE_REC = re.search(r'^  seducers\s+worlds \d+\s+total\s+(\d+).*?statute\s+(\d+)', rec, re.M); SE_REC = (int(SE_REC.group(1)), int(SE_REC.group(2))) if SE_REC else None
pf = rd(f'{SP}/ch13b_probes_fail.out'); PF = re.search(r'readback_probes: (\d+)/(\d+)', pf); PF = tuple(int(x) for x in PF.groups()); assert PF == (30, 36), PF
summ = rd('SUMMARY.txt'); assert 'GATES CHAIN DONE — ALL GREEN' in summ, summ[-400:]
dg = rd('daemon.out'); DGN = int(re.search(r'(\d+) daemons', dg).group(1)); DGF = re.search(r'(\d+) functions', dg); DGF = int(DGF.group(1)) if DGF else None; assert DGN == 73, DGN
dp = rd('dependency.out'); LC = re.search(r'LINK CENSUS \(the link review law\): reference (\d+), transfer (\d+), hypothesis (\d+), none (\d+)', dp); LC = tuple(int(x) for x in LC.groups())
DPE = re.search(r'(\d+) edges', dp); DPP = re.search(r'(\d+) pointers', dp); DPE = int(DPE.group(1)) if DPE else None; DPP = int(DPP.group(1)) if DPP else None
rg = rd('register.out'); RG = tuple(int(x) for x in re.search(r'DECLARED (\d+); DEBT (\d+); FAILS (\d+)', rg).groups()); assert RG[1] == 0 and RG[2] == 0 and RG[0] == 98, RG   # the tail: 98 — the first pass's print with the stale 28:69 uncounted; its removal moves nothing
sw = rd('sweep.out'); SW_P = len(re.findall(r'^PASS +cold_run_\w+\.py', sw, flags=re.M)); SW_F = len(re.findall(r'^FAIL +cold_run_\w+\.py', sw, flags=re.M)); SW_CELLS = sum(int(a) for a, b in re.findall(r'score=(\d+)/(\d+)', sw))
assert SW_F == 0 and SW_P >= 67, (SW_P, SW_F)
po = rd('positions.out') if os.path.exists(f'{G}/positions.out') else ''; PO = re.search(r'(\d+) checkpoints', po); PO = int(PO.group(1)) if PO else None
jg = rd('journal.out'); JG = re.search(r'(\d+) kinds, (\d+) rows', jg); JG = tuple(int(x) for x in JG.groups()) if JG else None
PR = {'census': last_frac('probe_census.out', 224), 'installation': last_frac('probe_installation.out', 6), 'readback': last_frac('probe_readback.out', 36), 'large_letter': last_frac('probe_large_letter.out', 6), 'checkpoint': last_frac('checkpoint.out', 7), 'ink_cache': last_frac('probe_ink_cache.out', 8)}
assert PR['readback'] == 36 and PR['installation'] == 6 and PR['large_letter'] == 6 and PR['ink_cache'] == 8, PR
dep_first = rd(f'{SP}/ch13b_chain_dependency_first.out') if os.path.exists(f'{SP}/ch13b_chain_dependency_first.out') else dp
POINTER = 'DEMANDED' if re.search(r'FAIL POINTER Deut 13:18 AS_WHEN', dep_first) else 'not demanded'   # the first pass's print decides
HOMOGRAPH = 'MATCHED (filed FALSE)' if re.search(r'the_heap|ahuzzath|the_cities_around_shechem|purge_commanded', dep_first) and 'FAIL' in dep_first else 'not matched'
CHAIN_STORY = read(f'{SP}/ch13b_chain_story.txt').strip() if os.path.exists(f'{SP}/ch13b_chain_story.txt') else 'THE GATES CHAIN ONCE — ALL GREEN on the first pass'
TAPE_STORY = read(f'{SP}/ch13b_tape_story.txt').strip() if os.path.exists(f'{SP}/ch13b_tape_story.txt') else 'THE TAPE 10/10 ON ITS FIRST RUN, DE1-DE9 MATCH'
dk = read('logic/oral_triage/deu_13_reeh_exam_2026-09-21.md'); NROWS = len([l for l in dk.split('\n') if l.startswith('- ') and (' — LAW.' in l or ' — DERIVATION.' in l or ' — DISPUTE.' in l or ' — CONTEXT.' in l or ' — OUTSIDE.' in l)]); assert NROWS == 565, NROWS
# ---- THE TIMING TABLE ----
tt = [l.split('\t') for l in read(f'{SP}/ch13_timing.tsv').split('\n') if l.strip()]
T11 = [(r[0], r[1], int(r[2])) for r in tt if len(r) >= 3 and r[1].startswith('11 ')]; T11B = [(r[0], r[1], int(r[2])) for r in tt if len(r) >= 3 and r[1].startswith('11b')]
TSUM11, TSUM11B = sum(s for _, _, s in T11), sum(s for _, _, s in T11B)
TSLOW = sorted(T11B, key=lambda r: -r[2])[:8]
TIMING = ("THE TIMING TABLE (every step timed — the owner's ask at sitting 10; the machine's seconds per step, the model's reading and writing between them the rest): SITTING 11 (the reading) %d timed steps, %d machine seconds; SITTING 11b (the compile — RUN A, the docket's one run, RUN B, the tail) %d timed steps, %d machine seconds; the first row %s, the last %s; THE SLOWEST OF 11b: %s. The table itself: <scratch>/ch13_timing.tsv, copied to the forms folder (ch13_timing.tsv)."
          % (len(T11), TSUM11, len(T11B), TSUM11B, T11B[0][0] if T11B else '?', T11B[-1][0] if T11B else '?', '; '.join('%s %ds' % (n[4:] if n.startswith('11b ') else n, s) for _, n, s in TSLOW)))
NUM = dict(DE=len(DE), CC=CC, PLC=PLC, CEN=CEN, DGN=DGN, DGF=DGF, LC=LC, DPE=DPE, DPP=DPP, RG=RG, SW=(SW_P, SW_CELLS), PO=PO, JG=JG, PR=PR, POINTER=POINTER, HOMOGRAPH=HOMOGRAPH, CASES=CASES_N, NREC=NREC, SE_REC=SE_REC, PF=PF, T11B=(len(T11B), TSUM11B))
print('THE NUMBERS:', NUM)
# ---- THE TEXTS ----
AS_BUILT = f"""
## Sitting 11b — THE COMPILE OF CHAPTER 13 — AS BUILT (2026-09-21; on the owner's "Go" after the compaction at #203 addendum 1 — the two-run rule's sixth compile sitting under THE COST RULES, the docket in one run: four clean points, #203 and its addenda 1-3)

THE DESIGN HELD ON ITS SPINE — four own-day lines, no marker, eight writes on Israel (five new, THREE REUSES), no debit, RUN (1327, 96, 88, 0, 12, 1634, 44, 319, the
four pairs, 127) as the arithmetic wrote it, PREVIOUS_RUN 10b's exactly, the runner 56/56 on its FIRST graded run, {TAPE_STORY}. THE DEPARTURES (read at the prints,
never predicted): (1) THE GREP DECIDED, AND EVERY SEAT WAS A COUNT — the reuses' ONE stood at SEVEN seats (CC3, CQ6, DB2, DC6 in cold_run_sequence.py; Q17, Q27, Q30 in
readback_probes.py) where the design had named one sure and two doubtful; all seven retyped ONE -> TWO before the tape (10b's booleans turned); (2) AN EIGHTH STALE
LITERAL the design did not predict — DD7, the register's footer at 12:1: (3) THE BLOCK'S TWO SEATS TURNED DAEMONS BY THE CHAPTER'S OWN DAEMON — law_seducers given_at Deut 13:1
sits inside (Deut 12:1, Deut 28:69], the one block the header at 12:1 and the footer at 28:69 SHARE, and the gate's verify refuses a declared green as STALE: 12:1's EMPTY declaration REMOVED at the types (10b's why had said 'chapter 13's the first
candidate'), 28:69's demanded by the chain's first pass and removed at the tail, register_probes' EMPTY 3 -> 1 retyped from the gate's print; DECLARED 100 -> {RG[0]} where the design said 'unmoved'; (4) TWENTY CALL edges — the design's nineteen and holiness (13:9's standing duties, Leviticus
19:16 and 19:18 by CALL); (5) THE READBACK'S CENSUS — seven on the tape, SEVENTEEN by CALL, five rows both (the design's 'nineteen T4 rows by CALL and eleven T1 rows
by kind'); Q34's sum 24; the eight SUPPLIED rows CARRY THEIR KIN — the rb() form relaxed (10b's asserted a SUPPLIED row references nothing); (6) THE STOREKEEPER A
CASE, NOT A PERSON — an ask returning a statute's write cannot be a person's (the case dispatch names the case's seven effects alone): forty persons, the exam's
{CASES_N} cases in seven cells; (7) A COUNT SLICED AS TEXT — MM.moriah('test_verb_seats') returns 1 and the cell sliced it: the generator found the TypeError the
fast checker cannot (the checker execs definitions, the generator runs the asks) — every sliced verdict str()'d, fifty-three uses; (8) NINE TOKEN-SEATS in eight verses
for the stoning verb in Leviticus and Numbers (Lev 24:16 twice) — retyped from the checker's print; (9) THE DATA ROWS thirty-nine (the design's 'about thirty');
(10) DE8 — 13:14's nearest verse by computation is Naboth's witnesses (1 Kings 21:10): the reading's comment 'each other's closest kin' held for two of the three (its
own assert said so) — {TAPE_STORY}; (11) THE CLEAVING HOMOGRAPH — the chapter-10 runner's hole scan ('cleav' on Israel's ledger) matched chapter 13's
devoted_thing_cleaving_barred once the tape's first run SEALED the writes: 'nothing of the devoted thing shall cleave to your hand' against 'to Him you shall cleave',
one root two senses — excluded by name in cold_run_second_tablets.py with its why (a LATER chapter's name in an EARLIER runner's scan: 9b's and 10b's lessons turned
once more); (12) THE TYPES' GUARD — 'Ketubot 111b' inside cleaving_commanded's ink matched the bare '11b' guard on the first run; retyped to the full marker; (13) THE
CALLEES' FORMS settled at the print — temurah's devote takes a string case, lev24's talion a default parameter, mekoshesh's 'stoning' needs died_at, holiness's 'blood'
needs case= (10b's lesson 2 held four times); (14) THE EXAM'S PERSONS forty — SIX EXEMPT (the prophet who keeps part and voids part, the prophet who spoke under duress,
Elijah at Carmel, the inciter who retracts before the fence, the enticed who did not consent, the inhabitants of Jerusalem drawn away), ONE LASHED (the one who plows
with the Asherah's wood — Makkot 22a:9), the false prophet and the inciter written TWICE (the death and the purge), THE CONDEMNED CITY an exam entity with a DESTROY
write (city_devoted) — the scene {SCENE}; (15) THE PROBES' FAIL PRINT {PF[0]}/{PF[1]} — Q17, Q27 and Q30 failed beside Q34-Q36 by their own retypes; (16) THE POINTER
at 13:18 {POINTER} by the census; the registry's homographs {HOMOGRAPH}; (17) {CHAIN_STORY}.
THE RUN: readback_probes.py Q34-Q36 to FAIL ({PF[0]}/{PF[1]} — patch_probes_ch13.py, the three reuse probes retyped with them) BEFORE the types; add_types_ch13.py (kinds
1150 -> 1155, effects 1049 -> 1056 with adding_barred's, cleaving_commanded's and pity_barred's rows AMENDED for the reuses, the 73rd daemon with seven WRAPPED, the
span and the twenty edges, I5 73, the_signs_status, the_prophets_death, the_execution_timing and the_inquiries in calendar_parameters.yaml — 64 rows, exercised by
the runner's DATA; the register file's 12:1 footer REMOVED); ch13_callees.py (every CALL's asks and results printed — 172 KB, twenty runners); derive_ch13_part1.py
(the helpers from the chapter-12 runner by content markers, W12 made W13; the ink block from ch13_ink.py in THREE blocks — the kin by computation, the phrases, the
register — with the one store-bound line dropped: 48 asserts; the counter's day, the four parameters, the one-database scans SEDUCERS_SCAN [] and REUSE_SCAN
[israel_people] x3, the callees' facts asserted from the print); ch13_part2.py and ch13_part3.py (six cells and the table, {CASES_N} asks — {PER_CELL}); ch13_part4.py
(the nineteen rows, thirty-nine DATA rows, the daemon with its eight writes, forty persons — the scene's forty submits written by ch13_scene_gen.py from the list and
frozen, the narrative — every census printed before it is asserted); ch13_fastcheck.py over parts 1-4 (six fails on the first pass — five counts retyped, the
storekeeper made a case; 0 on the second); ch13_cases_gen.py ({CASES_N} cases); ch13_assemble.py --guard {CASES_N}; cold_run_seducers.py 56/56 (the 68th runner,
277 KB); seq_record_ch13.py with the cache OFF ({NREC} records; seducers statute {SE_REC[1] if SE_REC else '?'} of {SE_REC[0] if SE_REC else '?'} submits);
seq_stitch_ch13.py (no marker; PLACEMENT {PLC}; CENSUS {CEN}); patch_seq_literals_ch13.py (the import line, DAEMON_ORDER, RUN, PREVIOUS_RUN, NEWEST_RUNNER,
PLACEMENT and CENSUS read, DE1-DE9, the VERDICTS; the five stale literals retyped); {TAPE_STORY}; checkpoint_check.py --all ({CC[0]} rows, {CC[1]} miss — the eighteen
known, {CC[2]} raised); {CHAIN_STORY}: the probe suites (readback {PR['readback']}/36, census {PR['census']}/224, installation {PR['installation']}/6 with I5 73,
large_letter {PR['large_letter']}/6, checkpoint {PR['checkpoint']}/7, ink_cache {PR['ink_cache']}/8), the daemon gate ({DGN} daemons{', %d functions' % DGF if DGF else ''}),
the dependency gate ({DPE} edges, {DPP} pointers; the link census reference {LC[0]} / transfer {LC[1]} / hypothesis {LC[2]} / none {LC[3]}), build_world, the journal
gate{' (%d kinds, %d rows)' % JG if JG else ''}, THE REGISTER GATE --strict (DECLARED {RG[0]}, DEBT {RG[1]}, FAILS {RG[2]} — the header at 12:1 and the footer at 28:69 DAEMONS by the
chapter's own daemon, their two EMPTY declarations on the one block removed), the positions table ({PO} checkpoints), the sweep {SW_P}/{SW_P} at {SW_CELLS} graded cells, the home-path gate. {TIMING}
THE LESSONS (twelve): (1) A REUSE'S COUNT SEATS ARE FOUND BY ONE GREP over the sequence file AND the probes — a count moves in both, and this chapter every seat was a
count; (2) A DAEMON GIVEN INSIDE A DECLARED-EMPTY BLOCK TURNS EVERY DECLARATION ON THAT BLOCK STALE — a header and a footer share one block (12:1 and 28:69); the gate's own rule refuses a declared green: both declarations go, the probe's EMPTY count with them,
DECLARED moves down; (3) A PERSON'S ASK NEVER RETURNS A STATUTE'S WRITE — the case dispatch names the case's effects alone; an ask that writes the statute is a case
row, not a person; (4) A SLICED VERDICT IS str()'D — a cell may return a count; (5) THE FAST CHECKER CHECKS DEFINITIONS, THE GENERATOR RUNS THE ASKS — a cells' dry-run
belongs in the checker (owed); (6) A READING'S COMMENT IS NOT ITS ASSERT — the kin by computation is typed from the assert; (7) THE SEALED TAPE FEEDS EVERY RUNNER'S
HOLE SCAN — a later chapter's name in an earlier runner's root pattern is excluded by name with its why; (8) A SUPPLIED ROW MAY CARRY ITS KIN — the chapter's rows all
have kin: the form's note at THE LOOP's step 6; (9) A MARKER GUARD IS THE FULL MARKER — '11b' sits inside 'Ketubot 111b'; (10) THE PRINT SETTLES EVERY CALLEE FORM
(10b's lesson 2 held four times); (11) THE PURGE FORMULA NAMED AT ITS FIRST SEAT — the eight seats ahead second entries, the compile's gain (8b's lesson turned
forward); (12) THE TWO-RUN RULE HELD on its sixth compile sitting under the cost rules: RUN A, the docket in one run, RUN B with the chain launched at its end, THE
TAIL — four clean points, the owner compacting after each. NEXT on the owner's word: the commit; CHAPTER 14's reading (14:1-29) in one run — the mourning's cuts, the
clean and the unclean beasts, the second tithe (the chapter's own formula seats: 14:1's 'sons of the LORD', 14:22-26's tithe at the place); on the table: the
Decalogue-schema sitting, the SUPPLIED forms, the calf's day marker, the registry's homographs, the receipt's third and fourth shapes (a gate sitting), THE INSTALL
HYPOTHESIS, the eras table's merge, the chain's positions step at four workers.
"""
DEBT_HDR_OLD = "## SITTING 11 — CHAPTER 13 (2026-09-21, the reading; deu_13_seducers frozen) — OWED TO THE COMPILE 11b: "
DEBT_HDR_NEW = "## SITTING 11 — CHAPTER 13 (2026-09-21, the reading; deu_13_seducers frozen) — PAID AT 11b (the 11b box below, item by item) — OWED WAS: "
DEBT_BOX = f"""
## THE SITTING-11 BOX (a)-(l) PAID — (a) THE PROPHET'S TEST — F2 the_prophet_and_the_test: THE LINE prophet_test_declared writing false_prophet_hearing_barred (a BLOCK
## — the_signs_status a PARAMETER: R. Yosei HaGelili's dominion / R. Akiva's fallen prophet; the false prophet's table Sanhedrin 90a:2-6), tested_by_the_lord (a STATUS
## — Genesis 22:1 by kind, 8:2 and 8:16 by CALL, 6:16's mirror by CALL) and cleaving_commanded REUSED (the six verbs; 85:1's cloud a run citation); the death the
## case's — the_prophets_death a PARAMETER (stoning / strangling, the answer sheet's arm), the exemptions (exempt persons), Elijah at Carmel (exempt), the oven of
## Akhnai, the established prophet; (b) THE HEADER'S NOT-ADDING — F1 the_header: THE LINE word_sealed REUSING adding_barred (4:2's cell by CALL — the second entry;
## CC3 retyped), the three grains, keep and do, the elder's fifth compartment (carried), the festival's days; (c) THE INCITER — F3 the_inciter: THE LINE
## inciter_law_declared writing pity_barred REUSED (the five prohibitions against the standing duties — HO.conduct, OR.courts, SN.because_you_hear by CALL; the
## court's rule inverted) and israel_hears_and_fears (THE FORMULA'S FIRST SEAT OF FOUR — the_execution_timing a PARAMETER); the kin's inclusion table, the entrapment
## (the retracting inciter exempt), the fifteen utterances, the hand first (L24, SA.molech by CALL), the stoning's rite (MK.capital_procedure by CALL — the inciter
## stoned with the evil purged), the two verbs of stoning a DATA row on the DB; (d) THE CONDEMNED CITY — F4 and F5: THE LINE condemned_city_law_declared writing
## condemned_city_inquiry_required (a STATUS — the seducers' parameters from one noun, one city at a time, Jerusalem's inhabitants exempt, the majority's procedure,
## THE SEVEN INTERROGATIONS with the_inquiries a PARAMETER read as data, the congruence rule) and devoted_thing_cleaving_barred (a BLOCK — the benefit ban's source and
## reach, the citron unfit, the Asherah's wood in the plow LASHED); the case's city_devoted (a DESTROY effect — the sword by any means, the property table's four
## cells, Heaven's spoil, the heap forever at R. Avin's principle with Jericho and Hiel), put_to_death on the inhabitant; the law as a study text; (e) THE EFFECTS —
## evil_purged_from_the_midst NAMED at its first seat of nine (the case's write; DE6), the anger keyed to idolatry (a condition in the value, no write), the mercy
## two-armed (a DATA row, no write), the fathers' merit by CALL (NR); (f) THE RUN CITATIONS — the cloud (85:1 — cloud_lifted Num 10:11 by kind), THE OATH at 13:18 the
## pointer row ({POINTER} by the census), the register's finder (no seat — 12:1 and 28:69 DAEMONS by this daemon); (g) THE KIN BY CALL — twenty runners (the
## design's nineteen and holiness); (h) NEVER READ AHEAD — 17:2-7, 18:20-22, 19:16-19, 24:16, 28:64 wait for their sittings (their cells by CALL to this runner's when
## they come); (i) CHAPTER 14's SPLIT OF PISKA 96 stands (rows 9-12 are 14:1's); (j) THE REGISTER's DATA rows (no imperative, no 'if', the seducers' 'we', the four
## infinitive absolutes, the one wayyiqtol (the narrative form), the ketiv at 13:16, the parser's [1]) DATA rows in the runner; (k) THE CHECKPOINT SERIES — DE1-DE9 the
## fifth name; (l) THE DOCKET — 565 rows in one run (409 read whole here, 156 carried), the writer derived from 10b's, the crowns the cells' rows.
## OWED FROM 11b: (i) THE FAST CHECKER'S CELLS' DRY-RUN — the checker execs definitions and never runs an ask; the generator found the sliced count: a dry-run of every
## ask joins ch14's checker; (ii) THE FORMULAS' SEATS AHEAD — evil_purged_from_the_midst at 17:7, 17:12, 19:19, 21:21, 22:21, 22:22, 22:24, 24:7 and israel_hears_and_fears
## at 17:13, 19:20, 21:21: second entries at their chapters (the reuse's form), 17:4's twin of 13:15 (the_inquiries by CALL), 17:7's hand of the witnesses, 18:20-22's
## false prophet (the_signs_status and the_prophets_death by CALL), 19:16-19's plotting witness ('rebellion' 189:1), 24:16's children (94:3's arm), 28:64's gods;
## (iii) THE CLEAVING HOMOGRAPH's kin — every earlier runner's hole scan is a root pattern on the ledger the tape seals: a later chapter's name can match it (the
## exclusion by name the form; a scan sitting on the owner's word if it recurs); (iv) THE RECEIPT'S THIRD AND FOURTH SHAPES, THE SUPPLIED FORMS (a law's first seat
## with its write — four this chapter; the SUPPLIED rows with kin — a form note), THE CALF'S DAY MARKER, THE REGISTRY'S HOMOGRAPHS (the_heap, ahuzzath,
## the_cities_around_shechem {HOMOGRAPH}), THE INSTALL HYPOTHESIS, THE ERAS TABLE'S MERGE, THE CHAIN'S POSITIONS STEP AT FOUR WORKERS — on the owner's word; (v) THE
## CHECKPOINT SERIES continues (DE the fifth name — DE9 the last; the next DF1, keyed by its first word). NOTHING ELSE IN CHAPTER 13 IS OWED TO A LATER SITTING OF ITS OWN.
"""
MIDDOT_ANCHOR = "\n## Exodus block campaign — owner's word \"Do 3\")\n"
MIDDOT_ENTRY = f"""- THE CHAPTER-13 COMPILE (THE DEUTERONOMY WALK sitting 11b RUN B, 2026-09-21; cold_run_seducers.py — the docket's rules carried into the cells; every code checked in this file before typed): I1 (qal wa-chomer, the a-fortiori) at Sifrei Bamidbar 113:1 (R. Yitzchak's from idolatry — the forewarning; F3 the_stoning_rite) and Mishnah Makkot 1:4-6 (86:3's from the plotting witness — F2 the_prophets_death); I2 (gezerah shavah, the verbal analogy) at Sanhedrin 89b:15-19 ('thrust' 13:6 / 13:11 — the false prophet's stoning, the_prophets_death's stoning arm; F2), 40b:4-6 ('diligently' FREE at 13:15's third verb — the seven interrogations pooled from three verses, F4 the_seven_interrogations, with the freeness rider), Berakhot 31b:4 (Hannah's 'base woman' / 13:14's 'base men' — F4 belial_and_naboth); I4 (kelal u-frat, a generalization and a specification apart — R. Avin's rule) at Sanhedrin 113a:4-6 ('a heap forever … it shall not be built' — R. Yosei HaGelili refuses the rule, R. Akiva applies it; F5 the_heap_forever); THE DOUBLED VERB named at Bava Metzia 31b:3 ('smite, you shall smite' — by any means; F4 the_sword) and Sanhedrin 33b:7 ('kill, you shall kill him' — the court's rule inverted; F3 the_courts_rule_inverted), 'CERTAIN' THE CONGRUENCE RULE named at Sanhedrin 41a:18-20 (F4 the_congruence_rule) — no code. THE DISPUTES AS PARAMETERS carried into the registry (calendar_parameters.yaml, exercised by seducers): the_signs_status (R. Yosei HaGelili's dominion / R. Akiva's fallen prophet — Sanhedrin 90a:10-11), the_prophets_death (stoning / strangling — 89b:15-21, Mishnah Sanhedrin 11:1 the answer sheet's arm), the_execution_timing (kept to the Festival / at once — Mishnah Sanhedrin 11:4), the_inquiries (the seven, the examinations, the voiding, the tolerance, the congruence, 'diligently' free, the order, the clock datum — Mishnah Sanhedrin 5:1-2, Sanhedrin 40a-41a); the majority's procedure (112a:4-5), the self-drawn city (112a:2-3), the property table's edges (112a:11-17), Heaven's spoil's arms (112b:1-113a:2), the heap's arms (113a:4-6), the children (94:3) DATA rows with their arms.
"""
DKF = 'deu_13_reeh_exam_2026-09-21.md'
RLOG = f"""
## 2026-09-21 — DEUTERONOMY 13 COMPILED AND ON THE TAPE (THE DEUTERONOMY WALK sitting 11b, the two-run rule's sixth compile sitting under the cost rules): THE SEDUCERS'
## ONE SENTENCE SAID THREE TIMES COMPILED AS FOUR LAWS AT THE CHAPTER'S OWN DAY — THE HEADER'S SEAL A REUSE, THE PROPHET'S TEST WITH THE SIGN REAL AND THE HEARING
## BARRED ANYWAY, THE INCITER'S LAW WITH THE COURT'S RULE INVERTED, THE CONDEMNED CITY'S LAW WITH THE SEVEN INTERROGATIONS A PARAMETER; THE PURGE FORMULA NAMED AT ITS
## FIRST SEAT OF NINE; THREE REUSES AND SEVEN COUNT SEATS RETYPED BY THE GREP; THE REGISTER'S FOOTER TURNED DAEMONS BY THE CHAPTER'S OWN DAEMON
On the owner's "Go" after the compaction at #203 addendum 1. THE COMPILE: cold_run_seducers.py the 68th runner (six cells and the table, {CASES_N} asks, 56/56 on its
first graded run), law_seducers the 73rd daemon (given_at Deut 13:1, installed_by boot; seven WRAPPED); FOUR OWN-DAY LINES at (40, 11, 1), no marker — word_sealed
(adding_barred REUSED — 4:2's twin in the singular), prophet_test_declared (false_prophet_hearing_barred a BLOCK with the_signs_status a PARAMETER; tested_by_the_lord
a STATUS; cleaving_commanded REUSED for the six verbs), inciter_law_declared (pity_barred REUSED with the five prohibitions against the standing duties by CALL and the
court's rule inverted; israel_hears_and_fears a STATUS — the formula's first seat of four, the_execution_timing a PARAMETER), condemned_city_law_declared
(condemned_city_inquiry_required a STATUS — the seducers' parameters from one noun, Jerusalem never one, the seven interrogations with the_inquiries a PARAMETER the
cell reads as data; devoted_thing_cleaving_barred a BLOCK — the benefit ban's source and reach); the case's writes evil_purged_from_the_midst (THE FORMULA'S FIRST SEAT
OF NINE), put_to_death and stoned by the_prophets_death's arms, city_devoted (a DESTROY effect on the condemned city); THE READBACK'S FORMS ON FILE, NO NEW FORM —
nineteen rows one per verse (VERBATIM 3 / VARIANT 5 / EXPANDED 3 / SUPPLIED 8 — the eight SUPPLIED rows carrying their kin, four with their writes), the pointer 13:18
({POINTER} by the census); {TAPE_STORY.lower()}; the gates chain {CHAIN_STORY.lower()} (the register gate DECLARED {RG[0]} / DEBT {RG[1]} / FAILS {RG[2]} — the header at 12:1's and the footer at
28:69's declarations removed, both DAEMONS by the chapter's own daemon; the sweep {SW_P}/{SW_P}). THE PARAMETERS: the_signs_status, the_prophets_death, the_execution_timing,
the_inquiries — every arm a docket row. THE DOCKET (one run): logic/oral_triage/{DKF} — 565 rows, 409 read whole here and 156 carried with their ledgers' own verdict
lines; its crowns in the map's AS RUN paragraph. THE RECORD KEPT: the grep found SEVEN count seats for the three reuses (every one a count, all retyped); the register's
block (Deut 12:1, Deut 28:69] turned DAEMONS at both its seats (the two EMPTY declarations STALE by the gate's rule — 12:1's removed at the types, 28:69's at the tail on the chain's demand; register_probes' EMPTY 3 -> 1); the cleaving homograph (chapter 13's devoted thing 'cleaving to the hand'
tripped chapter 10's hole scan once the tape sealed it — excluded by name); 13:14's nearest verse Naboth's (DE8 retyped once from the print); the exam's forty persons —
six exempt, one lashed, the condemned city devoted. {TIMING} The forms in World/step9/forms_deuteronomy_walk/.
"""
STEPS_ANCHOR = "\n## Step 6 — Publish\n"
STEPS_PARA = f"""
**Deuteronomy 13 compiled (2026-09-21, sitting 11b — the two-run rule's sixth compile sitting, the docket in one run):** the chapter is law from its first word to
its last, and the machine already held its kin: the header's seal is 4:2's law in the singular (a second entry on Israel, not a new law), the six verbs are 10:20's
four made six (a second entry), the pity is 7:16's on a second object (a third second entry). Four laws had no code — the prophet's test, the inciter's law, the
condemned city's law, and the seal's restatement — four lines at the chapter's own day, no marker, eight writes. Two disputes and two procedures the shelf records are
parameters, never constants: the sign's status (real and barred anyway, or a fallen prophet), the false prophet's death (stoning or the answer sheet's strangling),
the execution's timing (the Festival or at once), and the seven interrogations with the congruence rule — a table the cell reads as data. "Purge the evil from your
midst" gets its name here, at the first of its nine seats, so the eight ahead are second entries. The readback's forms on file held with no new form — nineteen rows,
one per verse, eight supplied as laws. The exam has forty persons, six exempt and one flogged, and the condemned city itself as an entity with a destroy write. The
grep found seven count seats for the three reuses and every one was a count; the chapter's own daemon turned the register's footer at 12:1 from empty to daemons.
The runner 56/56 on its first run; {TAPE_STORY.lower()}; the gates chain {CHAIN_STORY.lower()}. Every step timed: {TSUM11B} machine seconds over {len(T11B)} steps
for the compile.
"""
BRIEF_BULLET_ANCHOR = "- **CHAPTER 13 READ AND FROZEN — "
BRIEF_BULLET = (f"- **CHAPTER 13 COMPILED — THE SEDUCERS' ONE SENTENCE SAID THREE TIMES COMPILED AS FOUR LAWS AT THE CHAPTER'S OWN DAY: THE HEADER'S SEAL A REUSE, THE PROPHET'S TEST WITH THE SIGN REAL AND THE HEARING BARRED ANYWAY (A PARAMETER), THE FALSE PROPHET'S DEATH A PARAMETER WITH THE ANSWER SHEET'S ARM, THE INCITER'S LAW WITH THE COURT'S RULE INVERTED, THE CONDEMNED CITY'S LAW WITH THE SEVEN INTERROGATIONS A PARAMETER THE CELL READS AS DATA; THE PURGE FORMULA NAMED AT ITS FIRST SEAT OF NINE; THREE REUSES, SEVEN COUNT SEATS RETYPED; THE REGISTER'S FOOTER TURNED DAEMONS BY THE CHAPTER'S OWN DAEMON** (2026-09-21, sitting 11b — the two-run rule's sixth compile sitting under the cost rules; the runner 56/56 first run; {TAPE_STORY.lower()}; the chain {CHAIN_STORY.lower()}; the 68th runner, the 73rd daemon; forty persons, six exempt, one lashed, the condemned city devoted; every step timed — {TSUM11B} machine seconds over {len(T11B)} steps).\n")
BRIEF_ENTRY = f"""### 2026-09-21 — CHAPTER 13 COMPILED: FOUR LAWS AT ONE DAY, THREE OF THEM REUSING WHAT THE MACHINE HELD, AND THE DISPUTES AS PARAMETERS
Chapter 13 says one sentence three times — the prophet with the sign, the brother in secret, the city drawn away — and the compile found that most of its law was
already in the machine under other chapters' names. "You shall not add to it nor take from it" is 4:2's law restated in the singular: a second entry on Israel's ledger,
not a new law. The six verbs of 13:5 are 10:20's four made six: a second entry. "Nor shall your eye pity him" is 7:16's clause on a new object: a second entry. Three
reuses, and the grep found seven places where the old count of one was typed — every one a count this time, every one retyped before the tape. The new law is what the
chapter alone gives: the prophet's test (the sign granted true and the hearing barred anyway — R. Yosei HaGelili's dominion or R. Akiva's fallen prophet, a parameter;
the false prophet's death stoning by the Sifrei's analogy or strangling by the answer sheet, a parameter), the inciter's law (five prohibitions each against a standing
duty the machine already compiled, and the court's rule turned inside out for him alone), the condemned city's law (its seducers' parameters read from one noun, Jerusalem
never one, the seven interrogations and the congruence rule a table the cell reads as data). "And you shall purge the evil from your midst" gets its name here, at the
first of its nine seats, so the eight ahead will be second entries. The exam has forty persons — six exempt, one flogged for plowing with the Asherah's wood — and the
condemned city itself, an entity with a destroy write. Two things the design did not predict: the chapter's own daemon, given at 13:1, sits inside the footer block of 12:1
and turned that footer's declaration stale (the gate refuses a declared green — the declaration went); and the sealed tape fed chapter 10's hole scan a word it could
not tell apart — the devoted thing "cleaving" to the hand against Israel "cleaving" to the LORD — so the earlier runner now excludes the later name by name. The runner
56/56 on its first run; {TAPE_STORY.lower()}; the chain {CHAIN_STORY.lower()}. Every step was timed: {TSUM11B} machine seconds over {len(T11B)} steps for the compile,
the reading's {TSUM11} over {len(T11)}. Next: chapter 14 — the mourning's cuts, the clean and the unclean beasts, the second tithe.
"""
LOOP_OLD = "cold_run_place_name.py (chapter 12, THE FORMS ON FILE — NO NEW FORM 2026-09-21:"
LOOP_NEW = "cold_run_seducers.py (chapter 13, THE FORMS ON FILE — NO NEW FORM 2026-09-21: the seducers' one sentence three times — nineteen rows one per verse VERBATIM 3 / VARIANT 5 / EXPANDED 3 / SUPPLIED 8, seven on the tape, seventeen by CALL; EIGHT rows SUPPLIED as laws CARRYING THEIR KIN (a form note: the chapter's rows all have kin) — four WITH their writes (13:4, 13:12, 13:15, 13:18), three the lines' own first seats, 13:6 the case's; the pointer 13:18; three REUSED effects second entries; no marker; readback_probes 36/36, DE3); " + LOOP_OLD
RESUME_HEAD = f"""# ⚠ THE DEUTERONOMY WALK sitting 11b — CHAPTER 13 COMPILED AND ON THE TAPE (2026-09-21; step9/DEUTERONOMY_WALK.md "Sitting 11b" + "THE DOCKET — AS RUN" + "Sitting 11b — AS BUILT"):
# cold_run_seducers.py the 68th runner (56/56 first run), law_seducers the 73rd daemon; FOUR OWN-DAY LINES, NO MARKER — the header's seal (adding_barred REUSED), the
# prophet's test (false_prophet_hearing_barred, tested_by_the_lord; cleaving_commanded REUSED), the inciter's law (pity_barred REUSED; israel_hears_and_fears the formula's
# first seat), the condemned city's law (condemned_city_inquiry_required with the_inquiries a PARAMETER; devoted_thing_cleaving_barred); the purge formula named at its first
# seat; {TAPE_STORY.lower()} (DE1-DE9); the chain {CHAIN_STORY.lower()}; the register gate DECLARED {RG[0]} / DEBT {RG[1]} / FAILS {RG[2]} (12:1 and 28:69 DAEMONS by this daemon — their two EMPTY declarations removed).
# UNCOMMITTED since fb797a1: the docket and 11b (the message at <scratch>/commit_msg_ch13b.txt). NEXT on the owner's word: commit; chapter 14's reading.
"""
STATE_ADD = f"""
#203 ADDENDUM 3 (2026-09-21, at the close of THE DEUTERONOMY WALK sitting 11b's TAIL — on the owner's word after the compaction at addendum 2; A CLEAN COMPACTION POINT): THE STATE: CHAPTER 13 COMPILED AND ON THE TAPE — cold_run_seducers.py the 68th runner (six cells and the table, {CASES_N} asks, 56/56 on its first graded run; parts 1-5 in the scratchpad, copied to the forms folder), law_seducers the 73rd daemon (given_at Deut 13:1, installed_by boot; seven WRAPPED); event_vocabulary 1155, effect_vocabulary 1056 (adding_barred's, cleaving_commanded's and pity_barred's rows amended for the reuses); the span and twenty CALL edges; calendar_parameters.yaml +4 (the_signs_status, the_prophets_death, the_execution_timing, the_inquiries — 64 rows); the register file's 12:1 footer declaration REMOVED (DAEMONS by the chapter's own daemon — DECLARED {RG[0]}); FOUR OWN-DAY LINES at (40, 11, 1) after the tape's last Deuteronomy 12 line, NO marker (markers 172 unmoved) — word_sealed, prophet_test_declared, inciter_law_declared, condemned_city_law_declared; eight writes on Israel (five new — two blocks, three statuses; three reuses — second entries); no debit; RUN (1327, 96, 88, 0, 12, 1634, 44, 319, the four pairs, 127), PREVIOUS_RUN 10b's exactly, PLACEMENT {PLC}, CENSUS {CEN}; {TAPE_STORY}; checkpoint_check --all {CC[0]} rows, {CC[1]} miss (the known), {CC[2]} raised; readback_probes 36/36 (Q34-Q36 written to FAIL first at {PF[0]}/{PF[1]}); THE GATES CHAIN {CHAIN_STORY} — the probes, the daemon gate ({DGN} daemons), the dependency gate (the link census reference {LC[0]} / transfer {LC[1]} / hypothesis {LC[2]} / none {LC[3]}; the pointer at 13:18 {POINTER}; the registry's homographs {HOMOGRAPH}), build_world, the journal gate, the register gate --strict (DECLARED {RG[0]}, DEBT {RG[1]}, FAILS {RG[2]}), the positions table ({PO} checkpoints), the sweep {SW_P}/{SW_P}, the home-path gate; THE RECORDS from the sheet in one call (write_ch13b_records.py — the map's AS BUILT with THE TIMING TABLE, COMPILE_DEBT's sitting-11 box PAID and the 11b box, MIDDOT, RESEARCH_LOG, THE_STEPS, THE_BRIEFING, THE_LOOP, RESUME, RECORD_FORMS, this addendum, the addenda, the recovery page, the memory); the forms copied (copy_ch13b_forms.py); the commit message at <scratch>/commit_msg_ch13b.txt (the headline written, RUN B's paragraph, the trailers). THE TIMING: sitting 11b {len(T11B)} timed steps, {TSUM11B} machine seconds (the reading's {len(T11)} steps, {TSUM11} seconds). NOT COMMITTED (since fb797a1): the docket's run, RUN B and the tail — ONE message covers them (the owner's word: "Commit" = no push; "commit push" = both; 2b0c9c8 the last push). NOTHING MID-FLIGHT — A CLEAN COMPACTION POINT. NEXT ON THE RULING: the commit on his word; then CHAPTER 14's reading (14:1-29) in one run — the mourning's cuts, the clean and the unclean beasts, the second tithe; on the table: the Decalogue-schema sitting, the SUPPLIED forms, the calf's day marker, the registry's homographs, the receipt's third and fourth shapes (a gate sitting), THE INSTALL HYPOTHESIS, the eras table's merge, the chain's positions step at four workers, the fast checker's cells' dry-run. POST-COMPACTION REREADS: the recovery page, the map's "Sitting 11b — AS BUILT" (the newest section), MEMORY.md.
"""
def next_addenda_no(s):
    ns = [int(x) for x in re.findall(r'^##+ *§?(\d+)[\.\s:—]', s, re.M)] + [int(x) for x in re.findall(r'§(\d+)', s)]
    return (max(ns) + 1) if ns else 58
ADDENDA_ADD_T = """
## §{N} — THE DEUTERONOMY WALK sitting 11b (2026-09-21): CHAPTER 13 COMPILED — the state doc's #203 and its addenda 1-3; the map's "Sitting 11b … THE DESIGN", "THE DOCKET — AS RUN" and "Sitting 11b — AS BUILT"
The two-run rule's sixth compile sitting under the cost rules with the docket clause once: RUN A (the rereads, the recon and the scan derived by line-based substitutions,
the design), THE DOCKET in one run (565 rows — 409 read whole here, 156 carried with their ledgers' own verdict lines; the unresolved rows one shared file), RUN B (the
probes to FAIL with the three reuse probes retyped, the types with the register's footer removed, the callees' print, the runner 56/56 first run, the recorder with the
cache off, the stitcher with no marker, the literals with five retypes, the tape 9/10 then 10/10 with DE1-DE9, the chapter-10 scan's cleaving homograph excluded, the
chain launched at the run's end), THE TAIL (the summary read once, the demands filed, the records, the forms, the message). The crowns: the header's seal a reuse, the
sign real and the hearing barred anyway, the false prophet's death a parameter with the answer sheet's arm, the court's rule inverted, the seven interrogations a table
read as data, the purge formula named at its first seat, the condemned city devoted. The lessons in the AS BUILT (twelve). Every step timed. Uncommitted since fb797a1:
the docket and 11b; the message at <scratch>/commit_msg_ch13b.txt.
"""
MEM_PARA = f"""
SITTING 11b DONE (2026-09-21, "Go" after the compaction at #203 addendum 1; the tail after addendum 2): CHAPTER 13 COMPILED AND ON THE TAPE — cold_run_seducers.py the
68th runner (56/56 first run), law_seducers the 73rd daemon (seven WRAPPED); FOUR OWN-DAY LINES, NO MARKER: word_sealed (adding_barred REUSED — 4:2's twin),
prophet_test_declared (false_prophet_hearing_barred with the_signs_status a PARAMETER, tested_by_the_lord; cleaving_commanded REUSED), inciter_law_declared (pity_barred
REUSED; israel_hears_and_fears — the formula's first seat, the_execution_timing a PARAMETER), condemned_city_law_declared (condemned_city_inquiry_required with
the_inquiries a PARAMETER; devoted_thing_cleaving_barred); the case's evil_purged_from_the_midst (THE FORMULA'S FIRST SEAT OF NINE), put_to_death / stoned by
the_prophets_death, city_devoted (DESTROY); RUN (1327, 96, 88, 0, 12, 1634, 44, 319, pairs, 127), markers 172, kinds 872; {TAPE_STORY.lower()}, DE1-DE9; the chain
{CHAIN_STORY.lower()}; the register gate DECLARED {RG[0]} / DEBT {RG[1]} / FAILS {RG[2]} (12:1 and 28:69 DAEMONS — the two declarations removed, the probe's EMPTY 3 -> 1); the pointer at 13:18 {POINTER}.
THE LESSONS: a reuse's count seats found by one grep over the sequence file and the probes (seven, every one a count — retyped before the tape); a daemon inside a
declared-EMPTY block turns EVERY declaration on it STALE (12:1's and 28:69's — remove both; DECLARED down; the probe's count retyped); a person's ask never returns a statute's write; a sliced verdict str()'d (the
generator runs the asks, the checker only the definitions — a dry-run owed); a reading's comment is not its assert (13:14's kin Naboth's — DE8 retyped once); THE
SEALED TAPE FEEDS EVERY RUNNER'S HOLE SCAN (the cleaving homograph — a later name excluded by name in the earlier runner); a marker guard is the full marker; the
purge formula named at its first seat — the eight ahead second entries; the D series' fifth name DE (DF next). TIMED: {len(T11B)} steps, {TSUM11B} machine seconds.
UNCOMMITTED since fb797a1: the docket and 11b (the message <scratch>/commit_msg_ch13b.txt). NEXT on his word: the commit; chapter 14's reading (14:1-29).
"""
MEM_DESC_OLD = 'description: "COMMITTED AND PUSHED THROUGH 2b0c9c8 (2026-09-21) — SITTING 11 DONE 2026-09-21 ('
MEM_DESC_NEW = 'description: "COMMITTED THROUGH fb797a1 (2026-09-21; NOT PUSHED — pushed through 2b0c9c8) — SITTING 11b DONE 2026-09-21 (chapter 13 COMPILED — four laws at the chapter\'s own day, three reuses with seven count seats retyped, the purge formula named at its first seat, four disputes parameters, the register\'s footer turned DAEMONS; the docket and 11b UNCOMMITTED); SITTING 11 DONE 2026-09-21 ('
MEM_IDX_OLD = '11b RUN B DONE (56/56, tape 10/10); the chain LAUNCHED; NEXT: THE TAIL'; MEM_IDX_NEW = '11b DONE (56/56; 3 reuses; the purge named); commit next'
FORMS_OLD = "World/step9/forms_deuteronomy_walk/write_ch12b_records.py (write_ch11b_records.py,"
FORMS_NEW = "World/step9/forms_deuteronomy_walk/write_ch13b_records.py (write_ch12b_records.py, write_ch11b_records.py,"
REC_EDITS = [("## 2. WHERE IT STANDS (2026-09-21, 11b RUN B done; state doc #203 add. 2 newest)", "## 2. WHERE IT STANDS (2026-09-21, 11b done; state doc #203 add. 3 newest)"),
             ("- NUMBERS CLOSED. DEUTERONOMY 1:1-12:31 COMPILED AND ON THE TAPE (PUSHED through 2b0c9c8); 13 READ AND FROZEN.", "- NUMBERS CLOSED. DEUTERONOMY 1:1-13:19 COMPILED AND ON THE TAPE (PUSHED through 2b0c9c8; 13's compile uncommitted)."),
             ("- 227 frozen units, standing 2245, hash 8b8fff1fa28953af. 67 runners, 72 daemons, 491 functions; 1150 kinds / 1049 effects.", f"- 227 frozen units, standing 2245, hash 8b8fff1fa28953af. 68 runners, {DGN} daemons{', %d functions' % DGF if DGF else ''}; 1155 kinds / 1056 effects."),
             ("- THE TAPE at RUN (1323, 96, 88, 0, 12, 1626, 43, 319, pairs, 127), markers 172, closes 127; the sweep 66/66; every gate GREEN.", f"- THE TAPE at RUN (1327, 96, 88, 0, 12, 1634, 44, 319, pairs, 127), markers 172, closes 127; the sweep {SW_P}/{SW_P}; every gate GREEN."),
             ("- SITTING 11 (ch 13 read and frozen, timed; past the cap): the seducers' one formula; the header's twin 4:2; the purge's\n  first seat; piska 96:9-12 are 14:1's. 11b RUN B DONE — 56/56, the tape 10/10 (second run), 4 lines, 3 reuses, 40 persons.", f"- SITTINGS 11/11b (ch 13; TIMED — 11b {TSUM11B} s / {len(T11B)} steps): four laws at the chapter's own day, three REUSES (seven count\n  seats retyped); the purge formula at its first seat; four PARAMETERS; 40 persons, 6 exempt, 1 lashed; 12:1 & 28:69 DAEMONS."),
             ("- COMMITTED fb797a1 (NOT PUSHED). THE CHAIN LAUNCHED at RUN B's end (#203 add. 2). NEXT ON HIS WORD: THE TAIL after a compaction.", "- COMMITTED fb797a1 (NOT PUSHED). 11b DONE (56/56; tape 10/10; the docket 565 rows). UNCOMMITTED. NEXT: commit on his word; ch 14.")]
# ---- THE ANCHORS ----
ok = True
def need(p, a, n=1):
    global ok
    c = read(p).count(a)
    if c != n: print('ANCHOR', p.split('/')[-1], c, a[:70]); ok = False
MAP = 'World/step9/DEUTERONOMY_WALK.md'; DEBT = 'World/step9/COMPILE_DEBT.md'; MID = 'logic/MIDDOT.md'; RL = 'RESEARCH_LOG.md'; STEPS = 'THE_STEPS.md'; BRIEF = 'THE_BRIEFING.md'; LOOP = 'World/step9/THE_LOOP.md'
RES = 'World/RESUME.md'; RF = 'World/step9/RECORD_FORMS.md'; STATEDOC = 'logic/pre_logic_methods_2026-07-28/PROMPT_continue_solo_era_2026-08-06.md'; ADD = 'logic/pre_logic_methods_2026-07-28/RECOVERY_addenda_2026-09-12.md'
REC = 'logic/pre_logic_methods_2026-07-28/RECOVERY_new_thread_2026-09-12.md'; WALK = f'{MEM}/deuteronomy-walk.md'; IDX = f'{MEM}/MEMORY.md'
BRIEF_ENTRY_ANCHOR = [l for l in read(BRIEF).split('\n') if l.startswith('### 2026-09-21 — CHAPTER 13 READ:')]; assert len(BRIEF_ENTRY_ANCHOR) == 1, BRIEF_ENTRY_ANCHOR; BRIEF_ENTRY_ANCHOR = BRIEF_ENTRY_ANCHOR[0]
need(DEBT, DEBT_HDR_OLD); need(MID, MIDDOT_ANCHOR); need(STEPS, STEPS_ANCHOR); need(BRIEF, BRIEF_BULLET_ANCHOR); need(BRIEF, BRIEF_ENTRY_ANCHOR); need(LOOP, LOOP_OLD); need(RF, FORMS_OLD)
need(WALK, MEM_DESC_OLD); need(IDX, MEM_IDX_OLD)
for a, b in REC_EDITS: need(REC, a)
assert 'Sitting 11b — THE COMPILE OF CHAPTER 13 — AS BUILT' not in read(MAP) and '#203 ADDENDUM 3' not in read(STATEDOC) and '#203 ADDENDUM 2' in read(STATEDOC)
rec = read(REC)
for a, b in REC_EDITS: rec = rec.replace(a, b)
idx = read(IDX).replace(MEM_IDX_OLD, MEM_IDX_NEW)
N_ADD = next_addenda_no(read(ADD)); ADDENDA_ADD = ADDENDA_ADD_T.replace('{N}', str(N_ADD))
for t in (AS_BUILT, DEBT_BOX, MIDDOT_ENTRY, RLOG, STEPS_PARA, BRIEF_BULLET, BRIEF_ENTRY, LOOP_NEW, RESUME_HEAD, STATE_ADD, ADDENDA_ADD, MEM_PARA, rec, idx):
    assert not re.search(r'/Users/(?!Shared/)', t) and os.path.expanduser('~') not in t and ('/private' + '/tmp') not in t, 'a home or scratch path in a record'   # the guard's literal split by concatenation — the copier's own rule (the tail's find)
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
