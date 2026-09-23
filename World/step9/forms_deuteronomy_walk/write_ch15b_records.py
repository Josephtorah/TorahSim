import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE DEUTERONOMY WALK 13b THE TAIL (2026-09-23): THE RECORDS FROM THE SHEET IN ONE CALL (World/step9/RECORD_FORMS.md) — the map's "Sitting 13b — AS BUILT" (with THE
# TIMING TABLE) and sitting 13's lesson 4 CORRECTED in place (a dated rider), the reading ledger's CORRECTION row, COMPILE_DEBT's sitting-13 box PAID and the 13b box,
# MIDDOT's compile entry, RESEARCH_LOG, THE_STEPS, THE_BRIEFING (the scoreboard's date, a bullet and an entry), THE_LOOP's step-6 row, RESUME, RECORD_FORMS, the state
# doc's #207 addendum 5 (the close — a clean point), the addenda's section, the recovery page rewritten under its cap, the memory (the walk note and the index).
# EVERY NUMBER PARSED FROM THE PRINTS (the runner's run, the tape's runs, the chain's folder and its first pass kept aside, the timing table, the NFKC re-measure, the
# records' own reads), never recited; every text built whole before its file is opened; the caps asserted; the gloss lint's count per file asserted UNMOVED by the
# write; --check runs the reads and the anchors alone. write_ch14b_records.py's form. WRITTEN AND RUN AT THE TAIL (the design's 'at RUN B' moved under the cap). RUN FROM THE REPO ROOT.
import os, re, sys, subprocess
ROOT = _ROOT   # the scratchpad original (the copier prepends the portable header in the forms folder)
SP = os.path.dirname(os.path.abspath(__file__)); G = f'{SP}/gates_ch15b'
MEM = os.path.expanduser('~/.claude/projects/-Users-Shared-TorahSim/memory')
CHECK = '--check' in sys.argv
def rd(name): return open(name if name.startswith('/') else f'{G}/{name}', encoding='utf-8', errors='ignore').read()
def read(p): return open(p if p.startswith('/') else f'{ROOT}/{p}', encoding='utf-8').read()
def W(p, s): open(p if p.startswith('/') else f'{ROOT}/{p}', 'w', encoding='utf-8').write(s)
def last_frac(name, den=None):
    fr = [(int(a), int(b)) for a, b in re.findall(r'(\d+)/(\d+)', rd(name)) if den is None or int(b) == den]
    assert fr, (name, den); return fr[-1]
def newest(pat): return sorted(f for f in os.listdir(SP) if re.match(pat, f))[-1]
# ---- THE PRINTS ----
RUN_FILE = newest(r'ch15_runner_run\d\.out$'); run = rd(f'{SP}/{RUN_FILE}'); MX = re.search(r'MATRIX: (\d+)/(\d+)', run); MX = tuple(int(x) for x in MX.groups()); assert MX[0] == MX[1], (RUN_FILE, MX)
SCANS = re.search(r"^THE SCANS on the one database: (.*)$", run, re.M).group(1)
cg = rd(f'{SP}/ch15_cases_gen.out'); CASES_N = int(re.search(r'CASES generated: (\d+)', cg).group(1)); PER_CELL = re.search(r'per cell (\{.*?\})', cg).group(1)
NARR = re.search(r'^THE NARRATIVE: (\(.*?\)) \(the fifteen on Israel', run, re.M).group(1); SCENE = re.search(r'^THE SCENE on the bench: .*?; entities (\d+); closes (\d+)$', run, re.M); SCENE = (int(SCENE.group(1)), int(SCENE.group(2))) if SCENE else None
TAPE_FILE = newest(r'ch15_tape_run\d\.out$'); tape = rd(f'{SP}/{TAPE_FILE}'); assert '10/10 checkpoints' in tape, TAPE_FILE
TAPE_RUNS = len([f for f in os.listdir(SP) if re.match(r'ch15_tape_run\d\.out$', f)])
DG = re.findall(r'CHECKPOINT (DG\d) .*? (MATCH|MISS|DIVERGE)$', tape, flags=re.M); assert len(DG) == 9 and all(v == 'MATCH' for _, v in DG), DG
RETYPED = re.findall(r'CHECKPOINT (CQ6|DC6|DD2|DF5|CU5) .*? (MATCH|MISS|DIVERGE)$', tape, flags=re.M); assert len(RETYPED) == 5 and all(v == 'MATCH' for _, v in RETYPED), RETYPED
cc = rd(f'{SP}/ch15_checkpoint_check.out'); CC = re.search(r'checkpoint_check: (\d+) rows, (\d+) miss, (\d+) raised', cc); CC = tuple(int(x) for x in CC.groups()); assert CC[1] == 18 and CC[2] == 0, CC
st = rd(f'{SP}/seq_stitch_ch15.out'); PLC = re.search(r'^PLACEMENT LITERAL: (.*)$', st, re.M).group(1); CEN = re.search(r'^  CENSUS tuple .*?: (\(.*\))$', st, re.M).group(1)
rec = rd(f'{SP}/seq_record_ch15.out'); NREC = int(re.search(r'recording: (\d+) records written', rec).group(1)); RF_REC = re.search(r'^  release_firstborn\s+worlds \d+\s+total\s+(\d+).*?statute\s+(\d+)', rec, re.M); RF_REC = (int(RF_REC.group(1)), int(RF_REC.group(2))) if RF_REC else None
pf = rd(f'{SP}/ch15b_probes_fail.out'); PF = tuple(int(x) for x in re.search(r'readback_probes: (\d+)/(\d+)', pf).groups()); assert PF == (35, 42), PF
ty = rd(f'{SP}/add_types_ch15.out'); TY = tuple(int(x) for x in re.search(r'THE TYPES DONE: kinds (\d+), effects (\d+), daemons (\d+), functions blocks (\d+), edges from release_firstborn (\d+), I5 75, parameters (\d+)', ty).groups())
pl = rd(f'{SP}/patch_seq_literals_ch15.out'); WN = int(re.search(r'the writes W read from the narrative: (\d+)', pl).group(1))
summ = rd('SUMMARY.txt'); ALL_GREEN = 'GATES CHAIN DONE — ALL GREEN' in summ
if not CHECK: assert ALL_GREEN, summ[-400:]
dg = rd('daemon.out'); DGN = int(re.search(r'(\d+) daemons', dg).group(1)); DGF = re.search(r'(\d+) functions', dg); DGF = int(DGF.group(1)) if DGF else None; assert DGN == 75, DGN
dp = rd('dependency.out'); LC = re.search(r'LINK CENSUS \(the link review law\): reference (\d+), transfer (\d+), hypothesis (\d+), none (\d+)', dp); LC = tuple(int(x) for x in LC.groups()) if LC else None
DPE = re.search(r'dispositions on file: (\d+) edges, (\d+) pointers', dp); DPE, DPP = (int(DPE.group(1)), int(DPE.group(2))) if DPE else (None, None)
rg = rd('register.out'); RG = tuple(int(x) for x in re.search(r'DECLARED (\d+); DEBT (\d+); FAILS (\d+)', rg).groups()); assert RG[1] == 0 and RG[2] == 0, RG
def have(n): return os.path.exists(f'{G}/{n}')
sw = rd('sweep.out') if have('sweep.out') else ''; SW_P = len(re.findall(r'^PASS +cold_run_\w+\.py', sw, flags=re.M)); SW_F = len(re.findall(r'^FAIL +cold_run_\w+\.py', sw, flags=re.M)); SW_CELLS = sum(int(a) for a, b in re.findall(r'score=(\d+)/(\d+)', sw))
if not CHECK: assert SW_F == 0 and SW_P >= 69, (SW_P, SW_F)
po = rd('positions.out') if have('positions.out') else ''; PO = re.search(r'(\d+) checkpoints', po); PO = int(PO.group(1)) if PO else None
jg = rd('journal.out'); JG = re.search(r'(\d+) kinds, (\d+) rows', jg); JG = tuple(int(x) for x in JG.groups()) if JG else None
PR = {'census': last_frac('probe_census.out'), 'installation': last_frac('probe_installation.out', 6), 'readback': last_frac('probe_readback.out', 42), 'large_letter': last_frac('probe_large_letter.out', 6), 'ink_cache': last_frac('probe_ink_cache.out', 8)}
PR['checkpoint'] = last_frac('checkpoint.out', 7) if have('checkpoint.out') else None
if not CHECK: assert PR['readback'] == (42, 42) and PR['installation'] == (6, 6) and PR['large_letter'] == (6, 6) and PR['ink_cache'] == (8, 8) and PR['census'][0] == PR['census'][1] and PR['checkpoint'] == (7, 7), PR
dep_first = rd(f'{SP}/ch15b_chain_dependency_first.out'); DEMANDS = [l.strip()[5:] for l in dep_first.splitlines() if l.startswith('  FAIL ')]; assert len(DEMANDS) == 5, DEMANDS
POINTER = 'DEMANDED (Deut 15:6 AS_WHEN — the design\'s H row; filed OWED under 10b\'s debt line, link hypothesis)' if any(d.startswith('POINTER Deut 15:6 AS_WHEN') for d in DEMANDS) else 'not demanded'
HOMOGRAPH = ('the registry\'s three (the servant Abraham\'s, the place Bethel, Jacob\'s flock) NOT matched; the census\'s two — 15:4\'s "for an inheritance" (the family runner) filed FALSE by the gift formula\'s seats computed, 15:21\'s "lame" read as the Passover (the pesach runner) named inside the VIA row'
             if any('-> family' in d for d in DEMANDS) and any('-> pesach' in d for d in DEMANDS) else 'as the first pass printed: %s' % DEMANDS)
rb_first = rd(f'{SP}/ch15b_chain_readback_first.out'); assert 'readback_probes: 41/42' in rb_first and 'FAIL Q17' in rb_first
CHAIN_STORY = read(f'{SP}/ch15b_chain_story.txt').strip() if os.path.exists(f'{SP}/ch15b_chain_story.txt') else 'THE GATES CHAIN (the story file not yet written)'
TAPE_STORY = read(f'{SP}/ch15b_tape_story.txt').strip()
TAPE_SHORT = 'the tape 10/10 on its THIRD run (CU5\'s stale count read from the first run\'s print; the retype\'s apostrophes; the scan\'s ground fixed to exclude the daemon\'s own writes)'
CHAIN_SHORT = 'the gates chain in three passes (Q17 and the dependency gate\'s five demands from the first pass, the positions table by four workers, then all green)'
dk = read('logic/oral_triage/deu_15_reeh_exam_2026-09-23.md'); NROWS = len([l for l in dk.split('\n') if l.startswith('- ') and (' — LAW.' in l or ' — DERIVATION.' in l or ' — DISPUTE.' in l or ' — CONTEXT.' in l or ' — OUTSIDE.' in l)]); assert NROWS == 974, NROWS
nf = read('World/step9/forms_deuteronomy_walk/ch14_aramaic_nfkc.out'); NF1 = re.search(r'(\d+) code points in (\d+) rows', nf).groups(); NF2 = re.search(r'MOVE under the fold: (\d+) of (\d+)', nf).groups(); NF3 = re.search(r'differs under the fold: \[\] \(of (\d+)\)', nf).group(1); NF4 = re.search(r'the whole book: (\d+) verses of (\d+) differ', nf).groups()
assert NF1[0] == '0' and NF2[0] == '0' and NF4[0] == '0', (NF1, NF2, NF4)
# ---- THE TIMING TABLE ----
tt = [l.split('\t') for l in read(f'{SP}/ch15b_timing.tsv').split('\n') if l.strip()]
T13B = [(r[0], r[1], int(r[2])) for r in tt if len(r) >= 3 and r[1].startswith('13b')]
TSUM = sum(s for _, _, s in T13B); TSLOW = sorted(T13B, key=lambda r: -r[2])[:8]
PH = {k: (len([1 for _, n, _ in T13B if n.startswith('13b ' + k)]), sum(s for _, n, s in T13B if n.startswith('13b ' + k))) for k in ('A', 'D', 'B', 'T')}
TIMING = ("THE TIMING TABLE (every step timed — the owner's ask at sitting 10; the machine's seconds per step, the model's reading and writing between them the rest): SITTING 13b %d timed steps, %d machine seconds — RUN A %d steps %ds, THE DOCKET %d steps %ds, RUN B %d steps %ds, THE TAIL %d steps %ds; the first row %s, the last %s; THE SLOWEST OF 13b: %s. The table itself: <scratch>/ch15b_timing.tsv, copied to the forms folder."
          % (len(T13B), TSUM, PH['A'][0], PH['A'][1], PH['D'][0], PH['D'][1], PH['B'][0], PH['B'][1], PH['T'][0], PH['T'][1], T13B[0][0] if T13B else '?', T13B[-1][0] if T13B else '?', '; '.join('%s %ds' % (n[4:] if n.startswith('13b ') else n, s) for _, n, s in TSLOW)))
NUM = dict(DG=len(DG), TAPE_RUNS=TAPE_RUNS, CC=CC, PLC=PLC, CEN=CEN, DGN=DGN, DGF=DGF, LC=LC, DPE=DPE, DPP=DPP, RG=RG, SW=(SW_P, SW_CELLS), PO=PO, JG=JG, PR=PR, POINTER=POINTER[:40], DEMANDS=len(DEMANDS), CASES=CASES_N, NREC=NREC, RF_REC=RF_REC, PF=PF, TY=TY, MX=MX, WN=WN, NARR=NARR, SCENE=SCENE, NROWS=NROWS, NFKC=(NF1, NF2, NF3, NF4), T13B=(len(T13B), TSUM), ALL_GREEN=ALL_GREEN)
print('THE NUMBERS:', NUM)
# ---- THE TEXTS ----
AS_BUILT = f"""
## Sitting 13b — THE COMPILE OF CHAPTER 15 — AS BUILT (2026-09-23; RUN B on the owner's "Reread" then "Go" after the compaction at #207 addendum 3, THE TAIL on his "Go" at 189k without a compaction — the two-run rule's eighth compile sitting under THE COST RULES, the docket in three runs: six clean points, #207 and its addenda 1-5)

THE DESIGN HELD ON ITS SPINE — four own-day lines, no marker, {WN} writes on Israel from the lines (eleven new of ten names, work_of_the_hand_blessed at 15:10 and at 15:18;
FOUR REUSES — blessings_for_hearing, cry_heard, bears_sin, holy_things_in_the_gates_barred), the case's own writes beside them (severance_gift_owed a DEBIT priced by the
erection's own value, serves_for_ever, consecrated_firstborn), twenty-seven parameters (two clock data), RUN (1336, 96, 88, 0, 12, 1641 + {WN}, 46, 319, the four pairs, 127)
as the arithmetic wrote it with the writes read from the narrative's print, PREVIOUS_RUN 12b's exactly, the runner {MX[0]}/{MX[1]} on its FIRST graded run, {TAPE_SHORT}.
THE DEPARTURES (read at the prints, never predicted): (1) THE GREP DECIDED EIGHT COUNT SEATS AND THE RUNS FOUND TWO MORE — CQ6, DC6, DD2, DF5 in cold_run_sequence.py and
Q21, Q30, Q32, Q39 in readback_probes.py retyped ONE -> TWO before the tape; CU5 (the tape's first run 9/10) and Q17 (the chain's first pass, readback 41/42) missed — both
lines LISTED by the grep and CUT AT 200 CHARACTERS with the effect's name past the cut, read as lines without the name: the whole-row rule holds for a grep's lines; (2)
THE CALLEES' FORMS SETTLED AT THE PRINT (10b's lesson 2 held) — the erection's repeats('empty_exported') a VALUE ('five_selas_to_the_severance_gift'; the design had named the
value as the ask), temurah's tithe and devote STRING cases, the seducers' Belial ask 'belial_and_naboth' found by a scan of the cell's source, metzora's eighth-day members,
good_land's receipt finder EMPTY at chapter 15, yovel's cycle / jubilee / valuation — and MISHPATIM'S F1 A TABLE, NO CELL (the release list's three rows, the probes, the
wrap — read as data; the dependency gate then found no live call and the edge is PARAMETER since the tail); (3) THE BARE WORLD HAS NO 'count' ERA — the clock's method
PRINTS "no era set" and EXITS, never raises: the era is asked for before the call ('no count' on the bare world); the firstling's year by the clock 354 days (read from the
print); (4) hand_opening_commanded A KIND AND AN EFFECT SHARING A NAME — kept (profane_slaughter_permitted's precedent); (5) THE WRITES {WN}, NOT FOURTEEN — the narrative's
print counted work_of_the_hand_blessed twice (15:10, 15:18); (6) THE DATA ROWS 71 (typed 69 once; the print's 71 retyped); (7) THE TYPES REFUSED THEMSELVES BEFORE ANY WRITE
— the hole check's substring 'hebrew_slave' inside acquire_hebrew_slave, the pattern narrowed to 'hebrew_slave_law'; (8) THE FAST CHECKER THREE PASSES (the era; 0 / 0 / -1 /
-1; 0 / 0 / 0 / 1 -> the 71) and THE ASK-CHECKER's order (every part exec'd first — the KeyError was the order's, not a cell's); (9) F2's ask the_registers_two_near_misses
named an undefined finder — the good-land runner's receipt_seats by CALL took its place; (10) THE SEVERANCE GIFT'S DEBIT written at the case, its close left to the case
world (no scene close); (11) THE DERIVED CHAINS' TIMING pointed at the reading's table — corrected by a python edit (sed's '#' delimiter breaks on a '#' in the
replacement); (12) THE SCENE AND THE NARRATIVE MATCHED THEIR PREDICTIONS ON THE FIRST PASS — {SCENE[0] if SCENE else 82} entities, the nine write asks case rows, not persons
(11b's lesson 3 held), {NARR}; (13) THE TAPE THREE RUNS — {TAPE_STORY} (14) THE CHAIN FIVE PASSES — {CHAIN_STORY} (15) THE POINTER {POINTER}; THE HOMOGRAPHS —
{HOMOGRAPH}; (16) THE RECORDS WRITER MOVED TO THE TAIL — the design's 'WRITTEN at RUN B' given up under the cap (the clean-point writer and the copier written at RUN B);
(17) THE CLEAN POINT WAS DECLARED BEFORE THE CHAIN'S PRINT ARRIVED — the chain's two failures came after the clean-point records were written: an addendum's NOTE carried
them (the tail's list, each fix named from the print), and the tail ran in the same window on the owner's "Go" (189k — no compaction owed); (18) SITTING 13'S LESSON 4
CORRECTED — ch14_aramaic_nfkc.py at RUN A measured {NF1[0]} presentation-form code points in the Onkelos export's {NF4[1]} Deuteronomy rows, {NF2[0]} of {NF2[1]} seat literals
moving under the fold, {NF4[0]} verses differing: the export carries none; the miss was on the typing side; the piece cutter needs no fold (the rider at the lesson, the
CORRECTION row on the reading's ledger).
THE RUN: readback_probes.py Q40-Q42 to FAIL ({PF[0]}/{PF[1]} — patch_probes_ch15.py, the four kin probes retyped with them) BEFORE the types; add_types_ch15.py (kinds 1161
-> {TY[0]}, effects 1061 -> {TY[1]} with the four reused rows AMENDED, the {TY[2]}th daemon with eight WRAPPED, the span and the {TY[4]} CALL edges (nineteen reference,
two transfers taught), I5 75, the two calendar data — the_release_date and the_firstlings_year in the_removal_date's form — {TY[5]} parameter rows); ch15_callees.py (every
CALL's asks and results printed — 428 KB, twenty-one runners, read in two cuts); ch15_callees_facts.py (every kin value asserted from the print); derive_ch15_shells.py and
derive_ch15_seq_tools.py (12b's forms by asserted substitutions); derive_ch15_part1.py (the helpers from the chapter-14 runner, W14 made W15; the ink blocks from ch15_ink.py
with two store- and Onkelos-bound lines dropped: 66 asserts; the counter's day, the two clock data with the calendar's own keys read, the one-database scans, the DB's own
seats); ch15_part2.py and ch15_part3.py (seven cells and the table, {CASES_N} asks — {PER_CELL}); ch15_part4.py (the twenty-three rows, 71 DATA rows, the daemon with its
four line branches and the case branch, eighty-two persons — the scene's submits written by ch15_scene_gen.py from the list, the narrative — every census printed before it
is asserted); ch15_fastcheck.py (part 1 alone, then parts 1-2, then 1-4); ch15_askcheck.py (30 + 41 asks, 0 failed); ch15_cases_gen.py ({CASES_N} cases); ch15_assemble.py
--guard {CASES_N}; cold_run_release_firstborn.py {MX[0]}/{MX[1]} (the 70th runner, 420 KB); seq_record_ch15.py with the cache OFF ({NREC} records; release_firstborn statute
{RF_REC[1] if RF_REC else '?'} of {RF_REC[0] if RF_REC else '?'} submits); seq_stitch_ch15.py (no marker; PLACEMENT {PLC}; CENSUS {CEN}); patch_seq_literals_ch15.py (the import line,
DAEMON_ORDER, RUN with the writes read, PREVIOUS_RUN, NEWEST_RUNNER, PLACEMENT and CENSUS read, DG1-DG9, the VERDICTS; the four stale literals retyped); the tape's three
runs (ch15_tape_run1-3.out; patch_tape_cu5_ch15.py, patch_reuse_scan_ch15.py); checkpoint_check.py --all ({CC[0]} rows, {CC[1]} miss — the eighteen known, {CC[2]} raised);
the chain's passes (patch_tail_ch15b.py — the six demands; the positions table by four workers): the probe suites (readback {PR['readback'][0]}/{PR['readback'][1]}, census
{PR['census'][0]}/{PR['census'][1]}, installation {PR['installation'][0]}/6 with I5 75, large_letter {PR['large_letter'][0]}/6, checkpoint {PR['checkpoint'][0] if PR['checkpoint'] else '?'}/7, ink_cache
{PR['ink_cache'][0]}/8), the daemon gate ({DGN} daemons{', %d functions' % DGF if DGF else ''}), the dependency gate ({DPE} edges, {DPP} pointers; the link census reference
{LC[0] if LC else '?'} / transfer {LC[1] if LC else '?'} / hypothesis {LC[2] if LC else '?'} / none {LC[3] if LC else '?'}), build_world, the journal gate{' (%d kinds, %d rows)' % JG if JG else ''}, THE REGISTER
GATE --strict (DECLARED {RG[0]}, DEBT {RG[1]}, FAILS {RG[2]} — no seat in chapter 15; 15:5's 'commanding' and 15:6's 'spoke' the two near misses, a DATA row), the positions
table ({PO} checkpoints), the sweep {SW_P}/{SW_P} at {SW_CELLS} graded cells, the home-path gate. {TIMING}
THE LESSONS (twelve): (1) A CUT LINE ENDS BEFORE THE ANSWER — the whole-row rule (2026-09-17) holds for a grep's lines: a count seat is read WHOLE or the grep did not
decide it (two seats this sitting, each found by a run); (2) A SCAN OF THE FOLD EXCLUDES THE SCANNER'S OWN WRITES — an import-time assert on the one database is true only
once unless its ground is 'before this daemon's lines' (bears_sin, the first reuse with no prior entry, folded by the tape's first run); (3) A RETYPE INTO A SINGLE-QUOTED
SEAT ESCAPES ITS APOSTROPHES, and py_compile runs before the tape (twice this sitting — the seat and the clean-point writer's sentence); (4) THE CLOCK'S ERA IS ASKED FOR
BEFORE ITS METHOD — the method prints and exits; (5) THE CALLEES' FORMS ARE READ AT THE PRINT — a value named as an ask, a table where a cell was expected, a string case;
(6) A TOKEN'S HOMOGRAPH IS THE CONSONANTS' — the census reads 'lame' as the Passover; the disposition names the vowels; (7) THE GATE'S LIVE EDGE IS A CALL — a table read
is PARAMETER, and the runner's import comment says so; (8) A POINTER AHEAD IS OWED UNDER A DEBT LINE ALREADY ON FILE — the gate's OWED wants the why's prefix in
COMPILE_DEBT.md, and 10b's line served; (9) THE WRITES ARE READ FROM THE NARRATIVE'S PRINT — fifteen for the design's fourteen; (10) THE CHAIN'S FAILURES ARRIVE AFTER THE
CLEAN POINT — the NOTE beneath an addendum carries them for the tail, the clean point's records stand; (11) A PASS AFTER ANY SOURCE CHANGE STARTS AT THE TAPE — the readers
load the saved world keyed by the sources' digest; without it they run the world themselves under the live name, two at once, and a filing at the tail moves the
checkpoint that counts the file (DG7); (12) THE TWO-RUN RULE HELD on its eighth compile sitting under
the cost rules: RUN A, the docket in three runs, RUN B with the chain launched at its end, THE TAIL — six clean points, the tail in RUN B's window at 189k. NEXT on
the owner's word: the commit (13b alone — chapter 15 committed at b0eaa56); the push (on "push"); CHAPTER 16's reading (16:1-22) in two runs + the tail — the feasts
(the calendar and the moadim by CALL), the judges, the pillar; from chapter 16's design on: folio ranges at the SEGMENT grain; on the table: the chain's positions step
at four workers, the SUPPLIED forms, the calf's day marker, the registry's homographs, the receipt's third and fourth shapes (15:6 -> 28:3 an H pointer until 28:3),
THE INSTALL HYPOTHESIS, the eras table's merge, the fast checker's dry-run, the Decalogue-schema sitting.
"""
LESSON4_OLD = "(4) THE ARAMAIC EXPORT CARRIES PRESENTATION-FORM LETTERS — a substring count misses them unless folded through NFKC; the seat counter folds, the piece cutter does not (the pieces are typed around such a word); chapter 14's Aramaic counts owe a re-measure at 13b."
RIDER = f" [CORRECTED AT 13b (2026-09-23): the export carries NO presentation-form letters — ch14_aramaic_nfkc.py measured {NF1[0]} code points in {NF4[1]} rows, {NF2[0]} of {NF2[1]} seat literals moving under the fold, {NF4[0]} verses differing; the miss was on the typing side; the piece cutter needs no fold; chapter 14's counts stand as measured.]"
LESSON4_NEW = LESSON4_OLD + RIDER; L4P = "(4) THE ARAMAIC EXPORT CARRIES PRESENTATION-FORM LETTERS"; L4E = "re-measure at 13b."   # the map wraps the sentence across lines: anchored by its head and its tail
LEDGER_CORR = f"""
## CORRECTION (2026-09-23, appended at 13b's tail — the sitting's lesson 4 as the map recorded it): THE ARAMAIC EXPORT CARRIES NO PRESENTATION-FORM LETTERS. ch14_aramaic_nfkc.py (13b's RUN A) measured {NF1[0]} presentation-form code points (U+FB1D-FB4F) in the Onkelos export's {NF4[1]} Deuteronomy rows, {NF2[0]} of ch14_ink.py's {NF2[1]} seat literals moving under NFKC, {NF4[0]} of chapter 14's {NF3} verses and {NF4[0]} of the book's {NF4[1]} differing under the fold; the needy word's five seats (15:4, 7, 9, 11; 24:14) are found by the plain substring. The earlier miss was on the typing side, not the export's; the piece cutter needs no fold. Nothing above is changed — the ledger is append-only; the counts stand as measured.
"""
DEBT_HDR_OLD = "## SITTING 13 — CHAPTER 15 (2026-09-22, the reading; deu_15_release_firstborn frozen) — OWED TO THE COMPILE 13b: "
DEBT_HDR_NEW = "## SITTING 13 — CHAPTER 15 (2026-09-22, the reading; deu_15_release_firstborn frozen) — PAID AT 13b (the 13b box below, item by item) — OWED WAS: "
DEBT_BOX = f"""
## THE SITTING-13 BOX (a)-(o) PAID — (a) THE RELEASE — F1 the_release: THE LINE release_law_declared writing debt_release_owed (a STATUS — 'end' at the year's end by the
## analogy with 31:10, THE ONE CALENDAR for the whole world; the release-year A CLOCK DATUM the_release_date in the_removal_date's form; the onset and the territory TWO
## PARAMETERS; the manner said; loans only, the pledge-loan not released, HILLEL'S PROZBUL A PARAMETER FROM THE ANSWER SHEET, the witnesses), exaction_barred (a BLOCK — the
## exaction a prohibition, the neighbor and the brother two exclusions, the foreigner a positive command); the two years' powers by I1 with Leviticus 25 by CALL (yovel,
## calendar); THE RUNNING WORLD'S SABBATICAL COUNT measured — the bare world has no count era ('no count' — the clock's method prints and exits; asked for before the call);
## (b) THE NEEDY AND THE BLESSING — F2: THE TWO VERSES UPHELD BY A CONDITION (I13 without its third verse) — a STATE ROW 15:4 with the blessing's arm and the default
## (no write); blessings_for_hearing REUSED at 15:5 (the conditional heaven entry, 11:13 by CALL); THE RECEIPT'S REFERENT FORWARD 15:6 -> 28:3 THE READBACK'S H POINTER
## ROW (the gate's pointer filed OWED, link hypothesis, under 10b's debt line); lend not borrow, rule not be ruled; the register's two near misses a DATA row; (c) THE HAND
## OPENED — F3 the_hand_opened: THE LINE hand_opening_commanded (the kind and the effect one name) writing hand_opening_commanded (a STATUS), hand_shutting_barred and
## base_thought_barred (BLOCKS — 'base' without a yoke by the analogy with 13:14, the seducers' Belial cell by CALL, the transfer taught by the Sifrei 117:3), work_of_the_
## hand_blessed (HEAVEN), cry_heard and bears_sin REUSED (the cry a hastener, the sin unconditional — ordinances' loan by CALL); THE RANKS OF THE POOR a PRECEDENCE
## PARAMETER, the heart before the hand, the gift dressed as a loan, THE PLEDGE A DISPUTE (two arms), THE MEASURE OF NEED (the horse and the slave, the wife), the secret
## gift, the four grades, the three measures; 14:28-29's four at the gate by CALL (food_tithe); (d) THE HEBREW SLAVE — F4 the_hebrew_slave: THE LINE hebrew_slave_law_
## declared writing furnishing_commanded (a STATUS), empty_sending_barred (a BLOCK), work_of_the_hand_blessed again; THE THREE CASES each twin law its own (mishpatim's F1
## TABLE read as data — PARAMETER; Leviticus 25:39 by yovel; the maidservant's exits by mishpatim_3, the released by mishpatim_2), the exits TWO TABLES, the gift's measure
## a dispute, the severance gift's price by the erection's own value (five selas — severance_gift_owed a DEBIT at the case), BY DAY THEY PIERCE a time datum, 5:15 by
## covenant_at_horeb; (e) THE AWL — F5 the_awl_and_the_double_hire: the two sayings and times, illness bars, the tool A DISPUTE, the upper right ear by the analogy with
## the leper's (metzora's eighth-day members by CALL — the transfer taught by the Sifrei 122:5-6 and Kiddushin 15a), 'FOR EVER' the master's lifetime (serves_for_ever a
## STATUS at the case), R. ISHMAEL'S THREE CIRCUMVENTIONS a DATA row; (f) THE DOUBLE HIRE — the night's service a dispute of two spines, the blessing beside every money
## loss (the second work_of_the_hand_blessed); (g) THE FIRSTLING — F6 the_firstling: THE LINE firstling_law_declared writing firstling_sanctification_commanded (a STATUS
## — 'SANCTIFY' FOR ITS VALUE, NEVER FOR THE ALTAR: temurah's value consecration by CALL, consecrated_firstborn at the case), firstling_work_and_shearing_barred (a BLOCK),
## holy_things_in_the_gates_barred REUSED (place_name's profane slaughter thrice by CALL); the caesarean out, the refuted a fortiori, 'your' and the two files disputes,
## 'YEAR BY YEAR' TWO DAYS ACROSS THE YEAR'S EDGE — the_firstlings_year A CLOCK DATUM (354 days by the clock's own count, read from the print); korach's Numbers 18:15-18
## by CALL (the pesach runner's firstborn VIA korach — the gate's row); (h) THE BLEMISH AND THE BLOOD — F7 the_blemish_and_the_blood: the class visible and permanent by
## I8 (priesthood's Leviticus 22 list by CALL), the permanent blemish lent to all the consecrated by I2, drinking is eating, the witnesses' warning gating the penalty, THE
## OLIVE a quantity, the ground not the pit, the neck and the seeds; sanctions' blood ban and place_name's blood and gates by CALL; (i) THE EFFECTS — twelve NEW (debt_
## release_owed, hand_opening_commanded, furnishing_commanded, serves_for_ever, firstling_sanctification_commanded statuses; exaction_barred, hand_shutting_barred, base_
## thought_barred, empty_sending_barred, firstling_work_and_shearing_barred blocks; work_of_the_hand_blessed heaven; severance_gift_owed debit), FOUR REUSED (rows
## amended); (j) THE KIN BY CALL — twenty-one runners (nineteen reference, two transfers taught); (k) NEVER READ AHEAD — 16:5, 16:12-13, 17:1, 17:18, 21:3, 23:17-22,
## 24:14-22, 26:12-19, 28:1-12, 29:12, 31:10 wait for their sittings; (l) THE REGISTER's DATA rows — singular end to end, the one narrative verb 15:15 (the verse no docket
## row cites — computed), the four number verses and the ordinal, the homograph of Moses' name at 15:2 by lemma, the two near misses; (m) THE AS-MEASURED NOTE — chapter
## 14's Aramaic counts re-measured through NFKC: {NF1[0]} presentation-form code points in {NF4[1]} rows, {NF2[0]} of {NF2[1]} literals moving, {NF4[0]} verses differing — THE COUNTS
## STAND, sitting 13's lesson 4 corrected (the rider in the map, the CORRECTION row on the reading's ledger); (n) THE CHECKPOINT SERIES — DG1-DG9 the seventh name;
## (o) THE DOCKET — {NROWS} rows in three runs (814 read whole here, 160 carried), the writer derived from 12b's, the crowns the cells' rows.
## OWED FROM 13b: (i) THE FAST CHECKER'S CELLS' DRY-RUN (12b's owed item — still owed); (ii) THE SEATS AHEAD — 16:5 and 16:12-13 (the feasts' rejoicing and the slave's
## remembrance), 17:1's blemish (147:3-4 by CALL when it comes), 17:18's writing, 21:3's heifer 'not worked' (the firstling's twin), 23:17-22's vows and the foreigner, 24:14-22's
## hire and pledge (279:4 at 24:15), 26:12-19, 28:1-12 (THE RECEIPT'S REFERENT — the H pointer row 15:6 -> 28:3 RESOLVED at 28:3's sitting: the gate's OWED pointer paid
## there), 29:12, 31:10's seven years; (iii) THE COUNT ERA — the sabbatical and jubilee counts begin at the entry (no marker before it): the release-year's arithmetic by
## CALL once the count is set — a measurement at the conquest's sitting; (iv) THE SCAN'S GROUND as a form — every runner's import-time scan of the one database excludes
## its own daemon's writes (13b's lesson 2; the earlier runners' scans held only because their reuses stood on Israel already — a gate sitting may fold the exclusion into
## them); (v) THE GREP'S LINES WHOLE — the design's count-seat grep prints its lines uncut (13b's lesson 1; two seats found by runs this sitting); (vi) THE RECEIPT'S
## THIRD AND FOURTH SHAPES, THE SUPPLIED FORMS, THE CALF'S DAY MARKER, THE REGISTRY'S HOMOGRAPHS (none matched this sitting; the census's two filed), THE INSTALL
## HYPOTHESIS, THE ERAS TABLE'S MERGE, THE CHAIN'S POSITIONS STEP AT FOUR WORKERS (the eight-worker step skipped and the table measured by four outside the chain again)
## — on the owner's word; (vii) FOLIO RANGES AT THE SEGMENT GRAIN from chapter 16's design on (13b's docket lesson); (viii) THE CHECKPOINT SERIES continues (DG the seventh
## name — DG9 the last; the next DH1, keyed by its first word). NOTHING ELSE IN CHAPTER 15 IS OWED TO A LATER SITTING OF ITS OWN.
"""
MIDDOT_ANCHOR = "\n## Exodus block campaign — owner's word \"Do 3\")\n"
MIDDOT_ENTRY = f"""- THE CHAPTER-15 COMPILE (THE DEUTERONOMY WALK sitting 13b RUN B, 2026-09-23; cold_run_release_firstborn.py — the docket's rules carried into the cells; every code checked in this file before typed; the codes' seats counted in the runner's own source, never recited): I2 gezerah shavah (verbal analogy) the chapter's spine — the release's 'end' with 31:10's (the Sifrei 111:1, F1 the_release), the one calendar named in the Hebrew (111:3-8), 'base' with 13:14's (117:1-3, F3 the_hand_opened — the transfer taught, the seducers' cell by CALL), the upper right ear with the leper's (122:5-6, F5 the_awl_and_the_double_hire — metzora by CALL), the son not the daughter from 'his' (122:8, F4 the_hebrew_slave), the permanent blemish lent to all the consecrated (71:6, F7 the_blemish_and_the_blood), the firstling's seats (F6) — seven cells and the readback; I1 qal wa-chomer (a fortiori) at the two years' powers (112:2-4, F1) and the consecrated by the refuted argument (124:3, F6 — the refutation the verdict); I6 kelal u-frat u-kelal (general, particular, general) at the gift's kind (119:1-4, F4 — only what resembles the particular, the feature a dispute) and the tool of the piercing (122:1, F5), the blemish's class (F7); I8 (a particular singled out teaches about its general) — lame and blind the particulars that teach the class visible and permanent (126:1, F7); I13 (two verses stand until a third) at 15:4 against 15:11 — UPHELD BY A CONDITION, NOT A THIRD VERSE (114:1, 118:1, F2 the_needy_and_the_blessing — the state row); E30 notarikon (a word read as an abbreviation) at 'base' (117:1-3, F3 — the shelf's reading recorded as data beside the I2 transfer); the disputes as PARAMETERS (the pledge's two arms, the gift's measure four opinions, the tool, 'your' two ways, the two files, the night's service of two spines) and the two clock data (the_release_date, the_firstlings_year — 354 days by the clock's count) — every arm a docket row, read as data, never a constant.
"""
DKF = 'deu_15_reeh_exam_2026-09-23.md'
RLOG = f"""
## 2026-09-23 — DEUTERONOMY 15 COMPILED AND ON THE TAPE (THE DEUTERONOMY WALK sitting 13b, the two-run rule's eighth compile sitting under the cost rules): THE RELEASE,
## THE HAND, THE HEBREW SLAVE AND THE FIRSTLING COMPILED AS FOUR LAWS AT THE CHAPTER'S OWN DAY — THE RELEASE-YEAR AND THE FIRSTLING'S YEAR CLOCK DATA ON THE CALENDAR'S
## OWN KEYS (THE BARE WORLD'S 'NO COUNT' ASKED FOR BEFORE THE CLOCK'S METHOD), THE TWO VERSES UPHELD BY A CONDITION AS A STATE ROW, THE RECEIPT'S REFERENT AHEAD A
## POINTER ROW GRADED H AND A GATE'S OWED POINTER, THE SEVERANCE GIFT PRICED BY THE ERECTION'S OWN VALUE, TWO TRANSFERS TAUGHT (THE SEDUCERS' BELIAL, THE LEPER'S EAR);
## FOUR REUSES AND EIGHT COUNT SEATS RETYPED BY THE GREP, TWO MORE FOUND BY THE RUNS (THE CUT LINE); THE SCAN'S GROUND FIXED TO EXCLUDE THE DAEMON'S OWN WRITES
On the owner's "Reread" then "Go" after the compaction at #207 addendum 3 (RUN B) and "Go" for the tail. THE COMPILE: cold_run_release_firstborn.py the 70th runner
(seven cells and the table, {CASES_N} asks, {MX[0]}/{MX[1]} on its first graded run), law_release_firstborn the 75th daemon (given_at Deut 15:1, installed_by boot; eight
WRAPPED); FOUR OWN-DAY LINES at (40, 11, 1), no marker — release_law_declared (debt_release_owed a STATUS, exaction_barred a BLOCK, blessings_for_hearing REUSED — the
one calendar, the prozbul a parameter from the answer sheet, the_release_date a CLOCK DATUM), hand_opening_commanded (the kind and the effect one name — a STATUS,
hand_shutting_barred and base_thought_barred BLOCKS, work_of_the_hand_blessed HEAVEN, cry_heard and bears_sin REUSED; the ranks of the poor a precedence parameter, the
pledge a dispute), hebrew_slave_law_declared (furnishing_commanded a STATUS, empty_sending_barred a BLOCK, work_of_the_hand_blessed again; mishpatim's F1 read as a
TABLE, the severance gift's price by the erection's value — a DEBIT at the case, serves_for_ever at the awl), firstling_law_declared (firstling_sanctification_commanded
a STATUS — 'sanctify' for its value by temurah, firstling_work_and_shearing_barred a BLOCK, holy_things_in_the_gates_barred REUSED; the_firstlings_year a CLOCK DATUM of
354 days read from the print; the blemish's class by I8 over the priesthood's list); THE READBACK'S FORMS ON FILE, NO NEW FORM — twenty-three rows one per verse (TURNED
2 / SUPPLIED 11 / VARIANT 2 / VERBATIM 3 / SHORTENED 1 / DISAGREES 2 open / EXPANDED 2; eleven on the tape, twenty-three by CALL; the pointer row 15:6 -> 28:3 graded H,
the state row 15:4); {TAPE_SHORT}; {CHAIN_SHORT} (the register gate DECLARED {RG[0]} / DEBT {RG[1]} / FAILS {RG[2]}; the sweep {SW_P}/{SW_P}). THE EXAM'S PERSONS
eighty-two — eleven exempt, two lashed, seventeen barred, three freed, one furnished, one pierced for ever, one consecrated. THE DOCKET (three runs): logic/oral_triage/
{DKF} — {NROWS} rows, 814 read whole here and 160 carried; its crowns in the map's three AS RUN paragraphs. THE RECORD KEPT: the grep found eight count seats and the
runs two more (CU5 in the tape, Q17 in the chain — both lines cut at 200 characters with the name past the cut); the scan of the one database refused the tape's second
run until it excluded the daemon's own writes; the dependency gate's five demands filed from its print (the gift formula's seats computed by lemma; 'lame' the
Passover's homograph; the table read a PARAMETER; the registration edge; the pointer ahead OWED under 10b's line); sitting 13's lesson 4 corrected by the NFKC measure
({NF1[0]} code points in {NF4[1]} rows). {TIMING} The forms in World/step9/forms_deuteronomy_walk/.
"""
STEPS_ANCHOR = "\n## Step 6 — Publish\n"
STEPS_PARA = f"""
**Deuteronomy 15 compiled (2026-09-23, sitting 13b — the two-run rule's eighth compile sitting, the docket in three runs):** four laws at the chapter's own day, no
marker — the release of debts at the seventh year's end (one calendar for the whole world; the release-year a clock datum on the calendar's own key, read by call from
the jubilee engine once the count is set — the bare world has no count yet, and the machine says so instead of guessing), the hand opened to the poor (the ranks of the
poor a parameter, the pledge a dispute in two arms, the cry and the sin second entries on Israel), the Hebrew slave's release with his furnishing (the term clock read
from Exodus 21's own table; the severance gift priced by the value the erection already fixed), and the firstling sanctified for its value, never for the altar, with
its year of two days across the year's edge. Two verses that seem to contradict — 'there shall be no needy' and 'the needy shall never cease' — are a condition, not a
third verse, and the machine keeps them as a state row with two arms. One receipt points forward to a verse the book has not yet spoken (28:3); it is a labeled
hypothesis until that chapter is compiled, and the dependency gate files it as owed. Four laws were second entries on Israel's ledger; the grep found eight old counts
of one, and the runs found two more the grep had listed but cut short — the lesson of the whole row, now for greps. The exam has eighty-two persons. The runner
{MX[0]}/{MX[1]} on its first run; {TAPE_SHORT}; {CHAIN_SHORT}. Every step timed: {TSUM} machine seconds over {len(T13B)} steps for the compile.
"""
BRIEF_BULLET = (f"- **CHAPTER 15 COMPILED — THE RELEASE, THE HAND, THE HEBREW SLAVE AND THE FIRSTLING AS FOUR LAWS AT THE CHAPTER'S OWN DAY: THE RELEASE-YEAR AND THE FIRSTLING'S YEAR CLOCK DATA ON THE CALENDAR'S OWN KEYS, THE TWO VERSES UPHELD BY A CONDITION AS A STATE ROW, THE RECEIPT'S REFERENT AHEAD A POINTER ROW GRADED H, THE SEVERANCE GIFT PRICED BY THE ERECTION'S OWN VALUE, TWO TRANSFERS TAUGHT; EIGHT COUNT SEATS RETYPED BY THE GREP AND TWO MORE FOUND BY THE RUNS (2026-09-23, sitting 13b)** — cold_run_release_firstborn.py the 70th runner ({MX[0]}/{MX[1]} first run), law_release_firstborn the 75th daemon; four lines, {WN} writes (four reuses), twenty-seven parameters; {TAPE_SHORT}; {CHAIN_SHORT}. Uncommitted since b0eaa56.\n")
BRIEF_ENTRY = f"""### 2026-09-23 — CHAPTER 15 COMPILED: FOUR LAWS AT ONE DAY, TWO CLOCK DATA, A RECEIPT THAT POINTS AHEAD, AND THE GREP'S CUT LINES
Chapter 15 is law from its first word to its last, and the compile made four laws of it at the chapter's own day: the release of debts at the seventh year's end, the
hand opened to the poor, the Hebrew slave's release with his furnishing, and the firstling sanctified for its value. Two of its numbers are clock data on the calendar's
own keys — the release-year and the firstling's year of two days across the year's edge — and the year of the count comes by call from the jubilee engine; on the bare
world no count has begun, and the machine says 'no count' instead of guessing. The shelf's disputes stayed disputes, read as data: the ranks of the poor, the pledge,
the gift's measure, the tool of the piercing, whose the firstling is. Two verses that seem to contradict are kept as a condition with two arms, not resolved by a third
verse. One receipt — 'as He spoke to you' — points to a verse the book has not yet spoken; it is a labeled hypothesis until chapter 28, and the gate files it as owed.
Four laws were second entries on Israel's ledger. The grep found eight old counts of one and retyped them; the tape's first run and the chain's first pass each found one
more — lines the grep had listed but cut at two hundred characters, the name past the cut. The whole-row rule now holds for greps too. The scene of eighty-two persons
matched its prediction on the first pass. The runner {MX[0]}/{MX[1]} on its first run; {TAPE_SHORT}; {CHAIN_SHORT}. Every step was timed: {TSUM} machine seconds over
{len(T13B)} steps for the compile. Next: the commit; chapter 16 — the feasts, the judges, the pillar.
"""
SCORE_OLD = "## SCOREBOARD (as of 2026-09-22, latest)"; SCORE_NEW = "## SCOREBOARD (as of 2026-09-23, latest)"
LOOP_OLD = "cold_run_food_tithe.py (chapter 14, THE FORMS ON FILE — NO NEW FORM 2026-09-22:"
LOOP_NEW = "cold_run_release_firstborn.py (chapter 15, THE FORMS ON FILE — NO NEW FORM 2026-09-23: the release, the hand, the Hebrew slave and the firstling — twenty-three rows one per verse TURNED 2 / SUPPLIED 11 / VARIANT 2 / VERBATIM 3 / SHORTENED 1 / DISAGREES 2 open / EXPANDED 2, eleven on the tape by kind and first verse, twenty-three by CALL, the pointer row 15:6 -> 28:3 graded H (the referent ahead), the state row 15:4, no retrograde row; DG1-DG9); " + LOOP_OLD
RESUME_HEAD = f"""# ⚠ THE DEUTERONOMY WALK sitting 13b — CHAPTER 15 COMPILED AND ON THE TAPE (2026-09-23; step9/DEUTERONOMY_WALK.md "Sitting 13b" + the three "THE DOCKET — AS RUN" + "Sitting 13b — AS BUILT"):
# cold_run_release_firstborn.py the 70th runner ({MX[0]}/{MX[1]} first run), law_release_firstborn the 75th daemon; FOUR OWN-DAY LINES, NO MARKER — the release
# (debt_release_owed, exaction_barred; the_release_date a CLOCK DATUM; blessings_for_hearing REUSED), the hand opened (hand_opening_commanded, hand_shutting_barred,
# base_thought_barred, work_of_the_hand_blessed; cry_heard and bears_sin REUSED), the Hebrew slave (furnishing_commanded, empty_sending_barred; the severance gift a DEBIT
# at the case), the firstling (firstling_sanctification_commanded, firstling_work_and_shearing_barred; the_firstlings_year a CLOCK DATUM; holy_things_in_the_gates_barred
# REUSED); {TAPE_SHORT} (DG1-DG9); {CHAIN_SHORT}; the register gate DECLARED {RG[0]} / DEBT {RG[1]} / FAILS {RG[2]}; the sweep {SW_P}/{SW_P}.
# UNCOMMITTED since b0eaa56: 13b (the message at <scratch>/commit_msg_ch15b.txt). NEXT on the owner's word: the commit; the push on "push"; chapter 16's reading.
"""
STATE_ADD = f"""
#207 ADDENDUM 5 (2026-09-23, at the close of THE DEUTERONOMY WALK sitting 13b's TAIL — on the owner's "Go" at 189k without a compaction; A CLEAN COMPACTION POINT): THE STATE: CHAPTER 15 COMPILED AND ON THE TAPE — the tail as run: the chain's first pass read once (two failures — the NOTE beneath addendum 4), the six demands filed from the prints (patch_tail_ch15b.py: Q17's tenth seat 1 -> 2; release_firstborn -> family FALSE by the gift formula's seats computed by lemma; -> pesach VIA korach with 'lame' the homograph named; -> mishpatim CALL -> PARAMETER (the F1 table read); the registration edge sequence -> release_firstborn; the pointer Deut 15:6 AS_WHEN OWED, link hypothesis, under 10b's 'THE RECEIPT'S THIRD AND FOURTH SHAPES' line; the runner's import comment amended), the dependency gate green alone in 2s, {CHAIN_STORY}; the records from the sheet in one call (write_ch15b_records.py — the map's AS BUILT with the timing table and sitting 13's lesson 4 CORRECTED in place, the reading ledger's CORRECTION row, COMPILE_DEBT's sitting-13 box PAID and the 13b box, MIDDOT's compile entry, RESEARCH_LOG, THE_STEPS, THE_BRIEFING (the scoreboard's date, a bullet, an entry), THE_LOOP's step-6 row, RESUME, RECORD_FORMS, this addendum, the addenda's section, the recovery page, the memory; MISHNAH_TOPICS untouched — the docket's thirteen notes stand); the forms copied (copy_ch15b_forms.py); the commit message (<scratch>/commit_msg_ch15b.txt — 13b alone, chapter 15 committed at b0eaa56). THE NUMBERS from the prints: the runner {MX[0]}/{MX[1]}; the tape {TAPE_RUNS} runs to 10/10 (DG1-DG9; CQ6, DC6, DD2, DF5, CU5 MATCH); checkpoint_check {CC[0]} rows, {CC[1]} miss, {CC[2]} raised; the probe suites readback {PR['readback'][0]}/{PR['readback'][1]}, census {PR['census'][0]}/{PR['census'][1]}, installation {PR['installation'][0]}/6, large_letter {PR['large_letter'][0]}/6, checkpoint {PR['checkpoint'][0] if PR['checkpoint'] else '?'}/7, ink_cache {PR['ink_cache'][0]}/8; the daemon gate {DGN} daemons; the dependency gate {DPE} edges, {DPP} pointers (the link census {LC}); the register gate DECLARED {RG[0]} / DEBT {RG[1]} / FAILS {RG[2]}; the positions table {PO} checkpoints; the sweep {SW_P}/{SW_P} at {SW_CELLS} graded cells; the pointer {POINTER}; the homographs — {HOMOGRAPH}. THE TIMING: {len(T13B)} steps, {TSUM} machine seconds (RUN A {PH['A'][1]}s, the docket {PH['D'][1]}s, RUN B {PH['B'][1]}s, the tail {PH['T'][1]}s). UNCOMMITTED since b0eaa56: 13b whole. NOTHING MID-FLIGHT — A CLEAN COMPACTION POINT. NEXT ON HIS WORD: THE COMMIT (commit_msg_ch15b.txt — one message); the push on "push"; then CHAPTER 16's reading (16:1-22) in two runs + its tail, with folio ranges at the SEGMENT grain from its design on. POST-COMPACTION REREADS: the recovery page, the map's newest section ("Sitting 13b — AS BUILT"), MEMORY.md.
"""
def next_addenda_no(s):
    ns = [int(x) for x in re.findall(r'^##+ *§?(\d+)[\.\s:—]', s, re.M)] + [int(x) for x in re.findall(r'§(\d+)', s)]
    return (max(ns) + 1) if ns else 60
ADDENDA_ADD_T = """
## §{N} — THE DEUTERONOMY WALK sitting 13b (2026-09-22/23): CHAPTER 15 COMPILED — the state doc's #207 and its addenda 1-5; the map's "Sitting 13b … THE DESIGN", its three "THE DOCKET — AS RUN" paragraphs and "Sitting 13b — AS BUILT"
The two-run rule's eighth compile sitting under the cost rules with the docket clause three times: RUN A (the rereads, the recon and the scan, the NFKC re-measure that
corrected sitting 13's lesson 4, the design), THE DOCKET in three runs (974 rows — 814 read whole here, 160 carried with their ledgers' own verdict lines), RUN B (the
probes to FAIL with the four kin probes retyped, the types with the twenty-seven parameters, the callees' print read in two cuts, the runner 91/91 first run, the
recorder with the cache off, the stitcher with no marker, the literals with four seats retyped, the tape in three runs — CU5's stale count, the retype's apostrophes,
the scan's ground — the chain launched at the run's end), THE TAIL in the same window (the summary read once, the six demands filed from the prints, the chain in three
passes, the records, the forms, the message). The crowns: the release-year and the firstling's year clock data, the two verses a state row with two arms, the receipt
pointing ahead an H row and an OWED pointer, the severance gift priced by the erection's value, the two transfers taught, the gift formula's homograph computed by lemma,
'lame' the Passover's homograph. The lessons in the AS BUILT (eleven — the cut line, the scan's ground, the apostrophes, the clock's era, the callees' forms, the
consonants' homograph, the gate's live edge, the pointer ahead, the writes read, the chain's late failures, the pass after a source change, the two-run rule). Every step timed. Uncommitted since
b0eaa56: 13b; the message at <scratch>/commit_msg_ch15b.txt.
"""
MEM_PARA = f"""
SITTING 13b DONE (2026-09-23, "Reread" then "Go" after the compaction at #207 addendum 3 for RUN B; "Go" at 189k for the tail — no compaction): CHAPTER 15 COMPILED AND ON
THE TAPE — cold_run_release_firstborn.py the 70th runner ({MX[0]}/{MX[1]} first run), law_release_firstborn the 75th daemon (eight WRAPPED); FOUR OWN-DAY LINES, NO
MARKER: release_law_declared (debt_release_owed, exaction_barred; blessings_for_hearing REUSED; the_release_date a CLOCK DATUM — 'no count' on the bare world, the era
asked for before the clock's method), hand_opening_commanded (a kind and an effect one name; hand_shutting_barred, base_thought_barred, work_of_the_hand_blessed; cry_heard
and bears_sin REUSED; the ranks of the poor a parameter), hebrew_slave_law_declared (furnishing_commanded, empty_sending_barred; mishpatim's F1 a TABLE read — the gate's
PARAMETER; the severance gift a DEBIT priced by the erection's value), firstling_law_declared (firstling_sanctification_commanded, firstling_work_and_shearing_barred;
holy_things_in_the_gates_barred REUSED; the_firstlings_year 354 days); RUN (1336, 96, 88, 0, 12, 1641 + {WN}, 46, 319, pairs, 127), markers 172, kinds 881; {TAPE_SHORT},
DG1-DG9; {CHAIN_SHORT}; the register gate DECLARED {RG[0]} / DEBT {RG[1]} / FAILS {RG[2]}; the pointer 15:6 -> 28:3 an H row and an OWED pointer under 10b's line.
THE LESSONS: a cut grep line ends before the answer (CU5, Q17 — the whole-row rule for greps); a scan of the fold excludes the scanner's own writes; a retype into a
single-quoted seat escapes its apostrophes (py_compile before the run); the clock's era is asked for before its method; the callees' forms read at the print; a token's
homograph is the consonants' ('lame' the Passover); the gate's live edge is a call (a table read is PARAMETER); a pointer ahead is OWED under a debt line on file; the
writes read from the narrative's print (15 for 14); the chain's failures arrive after the clean point (the NOTE form); a pass after a source change starts at the tape; the D series' seventh name DG (DH next). TIMED:
{len(T13B)} steps, {TSUM} machine seconds. UNCOMMITTED since b0eaa56: 13b (the message <scratch>/commit_msg_ch15b.txt). NEXT on his word: the commit; the push on
"push"; chapter 16's reading (16:1-22) in two runs + the tail, folio ranges at the SEGMENT grain.
"""
MEM_IDX_OLD = '13b: design + docket 974 + RUN B DONE (91/91; tape 10/10); NEXT: THE TAIL'; MEM_IDX_NEW = '13b DONE (91/91; 4 lines; 4 reuses; 27 params); uncommitted; commit next, ch 16'
FORMS_OLD = "World/step9/forms_deuteronomy_walk/write_ch14b_records.py (write_ch13b_records.py,"
FORMS_NEW = "World/step9/forms_deuteronomy_walk/write_ch15b_records.py (write_ch14b_records.py, write_ch13b_records.py,"
REC_EDITS = [("## 2. WHERE IT STANDS (2026-09-23, 13b RUN B done; #207 add. 4 newest)", "## 2. WHERE IT STANDS (2026-09-23, 13b done; #207 add. 5 newest)"),
             ("(PUSHED through 049f55c; 15 + 13b uncommitted since b0eaa56).", "(PUSHED through 049f55c; 15 COMMITTED b0eaa56 not pushed; 13b uncommitted)."),
             ("10/10 (DG1-DG9); CHAIN PASS 1: probes FAIL (Q17 1->2) + dependency 5 demands (#207 add. 4 NOTE).", f"10/10 (DG1-DG9); sweep {SW_P}/{SW_P}; all gates GREEN, 5 passes."),
             ("- NEXT ON HIS WORD: THE TAIL after a compaction (the NOTE's list; rerun --from probes; records; message).", "- 13b DONE (#207 add. 5). NEXT ON HIS WORD: commit (<scratch>/commit_msg_ch15b.txt); push on \"push\"; ch 16's reading (16:1-22), two runs + tail.")]
# ---- THE ANCHORS ----
ok = True
def need(p, a, n=1):
    global ok
    c = read(p).count(a)
    if c != n: print('ANCHOR', p.split('/')[-1], c, a[:70]); ok = False
MAP = 'World/step9/DEUTERONOMY_WALK.md'; DEBT = 'World/step9/COMPILE_DEBT.md'; MID = 'logic/MIDDOT.md'; RL = 'RESEARCH_LOG.md'; STEPS = 'THE_STEPS.md'; BRIEF = 'THE_BRIEFING.md'; LOOP = 'World/step9/THE_LOOP.md'
RES = 'World/RESUME.md'; RF = 'World/step9/RECORD_FORMS.md'; STATEDOC = 'logic/pre_logic_methods_2026-07-28/PROMPT_continue_solo_era_2026-08-06.md'; ADD = 'logic/pre_logic_methods_2026-07-28/RECOVERY_addenda_2026-09-12.md'
REC = 'logic/pre_logic_methods_2026-07-28/RECOVERY_new_thread_2026-09-12.md'; WALK = f'{MEM}/deuteronomy-walk.md'; IDX = f'{MEM}/MEMORY.md'; LEDGER = 'logic/oral_triage/deu_15_reeh_2026-09-22.md'
BRIEF_ENTRY_ANCHOR = [l for l in read(BRIEF).split('\n') if l.startswith('### 2026-09-22 — CHAPTER 15 READ')]; assert len(BRIEF_ENTRY_ANCHOR) == 1, BRIEF_ENTRY_ANCHOR; BRIEF_ENTRY_ANCHOR = BRIEF_ENTRY_ANCHOR[0]
BRIEF_BULLET_ANCHOR = [l for l in read(BRIEF).split('\n') if l.startswith('- **CHAPTER 15 READ AND FROZEN')]; assert len(BRIEF_BULLET_ANCHOR) == 1, BRIEF_BULLET_ANCHOR; BRIEF_BULLET_ANCHOR = BRIEF_BULLET_ANCHOR[0]
MEM_DESC = [l for l in read(WALK).split('\n') if l.startswith('description: "')]; assert len(MEM_DESC) == 1, MEM_DESC; MEM_DESC_OLD = MEM_DESC[0]
MEM_DESC_NEW = ('description: "COMMITTED THROUGH b0eaa56 (2026-09-22, chapter 15\'s reading; NOT PUSHED — pushed through 049f55c) — SITTING 13b DONE 2026-09-23 (chapter 15 COMPILED — four laws at the chapter\'s own day, two clock data, four reuses, twenty-seven parameters; the runner %d/%d; DG1-DG9; the tape in three runs, the chain in three passes); 13b uncommitted; NEXT on his word: the commit, the push on \\"push\\", then chapter 16\'s reading (16:1-22) in two runs + the tail"' % (MX[0], MX[1]))
need(DEBT, DEBT_HDR_OLD); need(MID, MIDDOT_ANCHOR); need(STEPS, STEPS_ANCHOR); need(BRIEF, BRIEF_BULLET_ANCHOR); need(BRIEF, BRIEF_ENTRY_ANCHOR); need(BRIEF, SCORE_OLD); need(LOOP, LOOP_OLD); need(RF, FORMS_OLD)
need(WALK, MEM_DESC_OLD); need(IDX, MEM_IDX_OLD); need(MAP, L4P); assert read(MAP).index(L4E, read(MAP).index(L4P)) - read(MAP).index(L4P) < 400, 'the lesson-4 tail not within its sentence'
for a, b in REC_EDITS: need(REC, a)
assert 'Sitting 13b — THE COMPILE OF CHAPTER 15 — AS BUILT' not in read(MAP) and '#207 ADDENDUM 5' not in read(STATEDOC) and '#207 ADDENDUM 4' in read(STATEDOC) and '## CORRECTION (2026-09-23' not in read(LEDGER)
rec = read(REC)
for a, b in REC_EDITS: rec = rec.replace(a, b)
idx = read(IDX).replace(MEM_IDX_OLD, MEM_IDX_NEW)
N_ADD = next_addenda_no(read(ADD)); ADDENDA_ADD = ADDENDA_ADD_T.replace('{N}', str(N_ADD))
for t in (AS_BUILT, LESSON4_NEW, LEDGER_CORR, DEBT_BOX, MIDDOT_ENTRY, RLOG, STEPS_PARA, BRIEF_BULLET, BRIEF_ENTRY, LOOP_NEW, RESUME_HEAD, STATE_ADD, ADDENDA_ADD, MEM_PARA, MEM_DESC_NEW, rec, idx):
    assert not re.search(r'/Users/(?!Shared/)', t) and os.path.expanduser('~') not in t and ('/private' + '/tmp') not in t, 'a home or scratch path in a record'   # the guard's literal split by concatenation
for t in (AS_BUILT, LESSON4_NEW, LEDGER_CORR, DEBT_BOX, MIDDOT_ENTRY, RLOG, STEPS_PARA, BRIEF_BULLET, BRIEF_ENTRY, LOOP_NEW, RESUME_HEAD, STATE_ADD, ADDENDA_ADD, MEM_PARA, MEM_DESC_NEW):   # the NEW texts alone (the recovery page and the index carry glossed Hebrew of their own)
    assert not re.search('[\\u0590-\\u05FF]', t), 'Hebrew script in a new record — the map, the ledgers and the sheets carry none'
def lint(p):
    q = p if p.startswith('/') else f'{ROOT}/{p}'
    r = subprocess.run([sys.executable, f'{ROOT}/logic/solo_tools/gloss_lint.py', q], capture_output=True, text=True); m = re.search(r'(\d+) flag', r.stdout + r.stderr); return int(m.group(1)) if m else None
FILES = (MAP, DEBT, MID, RL, STEPS, BRIEF, LOOP, RES, RF, STATEDOC, ADD, REC, WALK, IDX, LEDGER)
LINT_BEFORE = {p: lint(p) for p in FILES}
print('anchors %s; the recovery page would be %d bytes (cap 10240); MEMORY.md %d (cap 17000); the addenda section §%d; the lint before %s' % ('OK' if ok else 'BAD', len(rec.encode('utf-8')), len(idx.encode('utf-8')), N_ADD, {p.split('/')[-1]: n for p, n in LINT_BEFORE.items()}))
assert ok and len(rec.encode('utf-8')) <= 10240 and len(idx.encode('utf-8')) <= 17000
if CHECK: sys.exit(0)
m = read(MAP); i = m.index(L4P); j = m.index(L4E, i) + len(L4E); assert m.count(L4P) == 1 and RIDER not in m; W(MAP, (m[:j] + RIDER + m[j:]).rstrip('\n') + '\n' + AS_BUILT)
W(LEDGER, read(LEDGER).rstrip('\n') + '\n' + LEDGER_CORR)
W(DEBT, read(DEBT).replace(DEBT_HDR_OLD, DEBT_HDR_NEW).rstrip('\n') + '\n' + DEBT_BOX)
W(MID, read(MID).replace(MIDDOT_ANCHOR, '\n' + MIDDOT_ENTRY.rstrip('\n') + '\n' + MIDDOT_ANCHOR))
W(RL, read(RL).rstrip('\n') + '\n' + RLOG)
W(STEPS, read(STEPS).replace(STEPS_ANCHOR, '\n' + STEPS_PARA.rstrip('\n') + '\n' + STEPS_ANCHOR))
b = read(BRIEF); b = b.replace(SCORE_OLD, SCORE_NEW, 1).replace(BRIEF_BULLET_ANCHOR, BRIEF_BULLET + BRIEF_BULLET_ANCHOR, 1).replace(BRIEF_ENTRY_ANCHOR, BRIEF_ENTRY.rstrip('\n') + '\n\n' + BRIEF_ENTRY_ANCHOR, 1); W(BRIEF, b)
W(LOOP, read(LOOP).replace(LOOP_OLD, LOOP_NEW))
W(RES, RESUME_HEAD + read(RES)); W(RF, read(RF).replace(FORMS_OLD, FORMS_NEW))
W(STATEDOC, read(STATEDOC).rstrip('\n') + '\n' + STATE_ADD); W(ADD, read(ADD).rstrip('\n') + '\n' + ADDENDA_ADD); W(REC, rec)
W(WALK, read(WALK).replace(MEM_DESC_OLD, MEM_DESC_NEW).rstrip('\n') + '\n' + MEM_PARA); W(IDX, idx)
print('written: the map (+ the lesson-4 rider), the reading ledger\'s CORRECTION row, COMPILE_DEBT, MIDDOT, RESEARCH_LOG, THE_STEPS, THE_BRIEFING, THE_LOOP, RESUME, RECORD_FORMS, the state doc, the addenda, the recovery page, the memory note, the index')
LINT_AFTER = {p: lint(p) for p in FILES}
for p in FILES: print('  lint', p.replace(MEM, '<memory>'), LINT_BEFORE[p], '->', LINT_AFTER[p])
assert all(LINT_AFTER[p] == LINT_BEFORE[p] for p in FILES), 'a record moved the gloss lint'
