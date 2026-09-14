#!/usr/bin/env python3
# THE NUMBERS WALK 8b — THE COMPILE OF THE SECOND CENSUS AND THE POPULATION TABLE (2026-09-11): THE RECORDS, written after the gates and the
# sweep (their prints READ here, never typed): NUMBERS_WALK.md as-built; COMPILE_DEBT's sitting-8b box (the sitting-8 box paid, the seeding
# filed, the new debt lines); RESEARCH_LOG's entry; THE_STEPS' paragraph; THE_BRIEFING's scoreboard bullet and entry; World/RESUME.md's line;
# the reading ledger's correction row (append-only); the three memory files; the state doc's COMPACTION POINT #134. Every insert anchored on
# text that must exist (an assert), every file linted after (the baselines: NUMBERS_WALK 0, COMPILE_DEBT 0, RESEARCH_LOG 52, THE_STEPS 1,
# THE_BRIEFING 0, RESUME 0, the ledger 0, the memory files 7 / 5 / 0, the state doc 147).
import re, os, sys, subprocess
ROOT = '<repo-old>'; SP = os.path.dirname(os.path.abspath(__file__)); MEM = '<memory>'
DATE = '2026-09-11'
def rd(p): return open(p, encoding='utf-8').read()
def wr(p, s): open(p, 'w', encoding='utf-8').write(s)
def append(p, s):
    t = rd(p); wr(p, t + ('' if t.endswith('\n') else '\n') + s)
def insert_before(p, anchor, s):
    t = rd(p); assert t.count(anchor) == 1, (p, anchor[:60], t.count(anchor)); i = t.index(anchor); wr(p, t[:i] + s + t[i:])
def insert_after(p, anchor, s):
    t = rd(p); assert t.count(anchor) == 1, (p, anchor[:60], t.count(anchor)); i = t.index(anchor) + len(anchor); wr(p, t[:i] + s + t[i:])
def replace_once(p, old, new):
    t = rd(p); assert t.count(old) == 1, (p, old[:60], t.count(old)); wr(p, t.replace(old, new))
def lint(p):
    out = subprocess.run([sys.executable, f'{ROOT}/logic/solo_tools/gloss_lint.py', p], capture_output=True, text=True).stdout
    m = re.search(r'gloss_lint: (\d+) flag', out); return int(m.group(1)) if m else -1

# ---- THE PRINTS READ ----
sweep = rd(f'{SP}/census2_sweep1.out')
m = re.search(r'(\d+)/(\d+) runners? green.*?([\d,]+) graded cells', sweep) or re.search(r'(\d+)/(\d+)[^\n]*?([\d,]+)\s+cells', sweep)
assert m, sweep[-600:]
SW_OK, SW_N, SW_CELLS = int(m.group(1)), int(m.group(2)), int(m.group(3).replace(',', ''))
assert SW_OK == SW_N == 50 and SW_CELLS == 5788, (SW_OK, SW_N, SW_CELLS)
jg = rd(f'{SP}/census2_journal_gate.out'); assert 'gate satisfied' in jg or 'GREEN' in jg or 'JOURNAL GATE' in jg, jg[-400:]
JG_ROWS = re.findall(r'(\d[\d,]*) rows', jg)
probes = {p: rd(f'{SP}/census2_{p}.out').strip().split('\n')[-1] for p in ('cursor_probes', 'sequence_probes')}
for p, line in probes.items():
    assert re.search(r'(\d+)/(\d+)', line) and (lambda a, b: a == b)(*map(int, re.search(r'(\d+)/(\d+)', line).groups())), (p, line)
ck = rd(f'{SP}/census2_clock_probes.out').split('\n')
CK_PASS = sum(1 for l in ck if l.strip().startswith('PASS')); assert CK_PASS == 22 and not any(l.strip().startswith('FAIL') for l in ck), (CK_PASS, [l for l in ck if l.strip().startswith('FAIL')])
PR = ', '.join('%s %s' % (p.split('_')[0], re.search(r'(\d+/\d+)', l).group(1)) for p, l in probes.items()) + ', clock 22 PASS'

# ---- A. NUMBERS_WALK.md — AS BUILT ----
ASBUILT = f'''
## Sitting 8b — THE COMPILE OF THE SECOND CENSUS AND THE POPULATION TABLE, AS BUILT ({DATE}; the owner: "Ok go" on the one-sitting form)

THE COURSE (1b's order held, the table's step FIRST): the design -> population_probes.py to FAIL (0/9 on the unchanged engine) -> the fifth
registry population_schema.yaml + the engine's table (World.tables, World.row, World.population) + the journal's ninth class ROW -> run.row
(KINDS, the register, the sink's line), the fifth view run_population and the views gate's population check, the fifth question
`population [tribe]`, journal_probes J3 amended -> population 9/9, journal 6/6, view 6/6 (the engine proved before a line of the runner)
-> the docket (264 rows verdicted, 124 credited with a quick look) -> the types (ten kinds, no effect, no registry row, the 55th daemon's
block with the two SHARED kinds, the functions block, the span + nine edges, I5 55) -> the gates to FAIL (the daemon gate 2 ways, the
dependency gate 9) -> the runner in one file -> the first graded run -> the gates read -> the recorder -> the stitcher -> the literals ->
the tape run -> the probe gates -> the journal gate -> the sweep -> the records.

THE ENGINE (world_engine.py; the design's table built as typed): the fifth registry loaded beside the four (POP_SCHEMA); World.tables a list
per table; World.row refuses a row written by hand (no daemon consuming) and a row outside the schema (an unknown table, an unknown grain, a
missing required column, an unknown column — the three refusals P3 proves), stamps written_by / day / year / table, appends, logs the class
ROW; World.population answers equality queries. The journal: KINDS gains ROW -> run.row; the sink writes subj (the registry id of a named
row's person, a counted row's tribe name), unit (the daemon), ref (the verse); the fifth view run_population over run.row; the views gate's
sixth check (population = rows); the fifth question. journal_probes J3: the seven engine classes the probe world exercises are KINDS less
run.skip and run.row. Every probe file green: population 9/9, journal 6/6, view 6/6, installation 6/6 (I5 55), {PR}.

THE RUNNER cold_run_second_census.py (the 50th; law_second_census the 55th): the guard 70 (the design's count held); 35 token probes (every
one measured on the DB before it was typed); five cells — F1 the_command 5 asks, F2 the_roll 16, F3 the_land 15, F4 the_levites 9, F5
the_rolls 9 (one a HYPOTHESIS cell, class H) — and fourteen number rows, the scene and the narrative: 70 answer-sheet rows, 70/70 ON THE
SECOND GRADED RUN — the first fell on ONE TYPED FACT: Ard stands BARE at 26:40 ('the sons of Bela: ARD and Naaman'), the hand had typed him
with the preposition Naaman carries; and before the first run THE MEASUREMENT PASS corrected a second: "Moses and Eleazar" ADJACENT stands
at TEN seats in Numbers (20:28, 26:1, 26:3, 26:63, 31:12, 31:13, 31:31, 31:51, 31:54, 32:2) — the reading's prose said "seven seats from
20:28" — the first the succession's own verse, the second the census's command (the reading ledger's correction row appended). Eight
engines CALLED live (bamidbar's twelve and total and lineage and the Levites' delta, balak's plague count — peor('plague_count'), a
constant read being no call form: the dependency gate's own reading — korach's 14,700 and 250 and four rows, shelach's decree set and
exceptions and the dying ceased, zelophehad's plea and names' order and run and three portions and uncertainty and reach and lapse and the
land row with its forks and heir_of and the firstborn's double, joseph's seventy cells and rosters, chukat's succession, the eighth day's
strange fire). THE NARRATIVE: the two SHARED events replayed first at (2, 2, 1), the 25:19 marker reading-placed, the five lines; the
tuple PREDICTED AND MATCHED FIRST RUN — 136 rows: counted 12 + 4 + 69 + 9, delta 12 + 1, named 18 + 9 + 2 = 29 (Eliab and Nemuel son of Eliab
beside the design's twenty-seven: persons the roll names beside the family list), Simeon's delta -37,100 and its unexplained -13,100, one
marker, two entities. FRACTIONS: ink 18/70, moves 47/70, data 4/70, hypotheses 1/70 — the H class counted apart for the first time.

THE DAEMON law_second_census: four writes at the lines (the census's debit and its counted status 601,730 on Israel, the land's debit
divide_the_land OPEN, the Levites' counted status 23,000 — the 18:23-24 block READ off the ledger and named in the law text), one close
(the census's debit at 26:51), NO timer, and THE TABLE'S ROWS at four kinds — the two SHARED kinds (census_taken at Num 1:17-19: the twelve
tribe rows; levites_counted at Num 3:16: the three houses and the total) rows only, no effect; the second census's rows, the deltas
computed FROM THE TABLE (the daemon's own chapter-1 rows — a world without them declares no delta), the named rows. THE GATES' FIRST FAILS,
READ: the daemon gate's '?UNRESOLVED?' — the narrative's five lines written as a loop over LINES and the scene's eighteen as a loop over a
tuple (7b's lesson relearned at a second seat: LITERAL SUBMITS ONLY — both rewritten as literals); the dependency gate's FOUR undispositioned
edges from the token census — family [inheritance] at 26:53-56 and 26:62 (VIA zelophehad: the land's holding reached through the runner
this one calls), moadim [first_fruits] at 26:35 (Becher's family name — FALSE), offerings [shelamim] at 26:49 (Shillem — FALSE), pesach
[firstborn] at 26:5 and 26:35 (Reuben the firstborn son, Becher — FALSE, the first foreseen) — and the AS_WHEN pointer at 26:4 ('as the LORD
commanded Moses' — RUN_CITATION), and balak's CALL with no live edge (CB.COUNT a constant read — the live call added). Both gates GREEN:
55 daemons watching 1,025 kinds, 382 WRAPPED, 0 OWED; 398 edges + 157 pointers, 275 live edges.

THE TAPE: the recorder 50 modules; the stitcher's CENSUS typed from its print (2144, 1253, 1244, 875, 6, 10, 9, 0, 71, 157, 125, 15, 17,
789, 265) — on tape 1239 -> 1244 (+5), markers 156 -> 157 (F 125: the 25:19 row reading-placed), DEDUPED 7 -> 9 (the two shared events at
their verses, bamidbar first in the order), kinds +5, subjects UNMOVED at 265 (no row is a subject); THE PLACEMENT LITERAL READ AT THE
STITCHER'S PRINT: events reading_placed 39 -> 40 and page_order 1094 -> 1098 — THE COMMAND LINE'S KEY IS THE MARKER'S VERSE (its case_source
opens 'Num 25:19-26:4') and takes the marker's class; the design had typed page_order +5 ("no event at its own verse"). THE FIRST TAPE RUN
READ THREE MISSES: (i) the RUN literal's THIRD LINE — the closes 113 where the head had been retyped to the prediction's +1 (THE TENT
sitting 1's lesson, A RETYPE COVERS EVERY LINE OF A MULTI-LINE LITERAL, relearned) and PREVIOUS_RUN's third line likewise (110 for 7b's
113); (ii) CL2 DIVERGE — 7b's "markers 156 unmoved" a GLOBAL count moved by the new marker: scoped to Balak's own span (no marker inside
22:1-25:18), THE OLD CHECKPOINT KEEPS ITS VERSES; (iii) CP6 DIVERGE — the five lines' placement set carried the command line's reading_placed
(the stitcher's rule, typed before its print was read). RUN = (1244, 52, 52, 0, 12, 1469, 26, 302, the four pairs, 114) PREDICTED AND
MATCHED ON THE SECOND TAPE RUN — the arithmetic held on the first, the literals lagged; THE REST = 7b's RUN EXACTLY (the row-only daemon
returns no effect on chapter 1's shared kinds: not 'fired', no write); 10/10; CP1-CP9 MATCH; the log's classes on the running world: MARKER
157, EVENT 1244, WRITE 1469, TIMER-SET 52, TIMER-FIRE 52, ROW 136, RETRO-WRITE 12; the journal's index 18,963 rows from 8 segments; the
probe gates green ({PR}); THE JOURNAL GATE GREEN (the fifth view's population check on every world — the rows the table's own); THE SWEEP
run_cold_all.py: {SW_OK}/{SW_N} runners green, {SW_CELLS:,} graded cells (7b's 5,718 + the second census's 70), the daemon and dependency
gates first.

THE CHECKPOINTS AS RUN: CP1 the table's 136 rows by grain and census, every one law_second_census's; CP2 the twelve at both seats from the
table = the parser's, 603,550 and 601,730, five negative (-61,020), seven positive (+59,200), the whole -1,820; CP3 Simeon's row explained
by the plague's 24,000 (by call, the tribe the shelf's) and -13,100 unexplained, eleven other deltas wholly unexplained; CP4 the Levites
22,000 -> 23,000 (+1,000 unexplained), five families against eight (Shimei, Amram, Izhar, Uzziel gone; Korah in), the houses' 22,300 the
callee's; CP5 THE MEMBERSHIP PREDICATE — of the roll's named dead FIVE carry a death-class entry (Er, Onan slain_by_heaven at Genesis 38;
Dathan, Abiram, Korach put_to_death at Numbers 16) and TWO have NO ENTITY (Nadab, Abihu — the eighth day's fire wrote on no person: a
debt line), the exceptions Caleb and Joshua carry none, the decree's timer fired before the census's line, the Levites' block on the ledger
since 18:23-24, Korach's plague entry of 17:11 STILL OPEN; CP6 the marker reading_placed at (40, 6, 1), 157 markers, the command line
reading_placed and the four page_order at (40, 6, 1); CP7 the five daughters' rows "had no sons, only daughters" BEFORE the 27:1 marker on
the log — the premise on the table before the plea, heir_of = daughter; CP8 Jochebed's row "born to Levi in Egypt" — CJ3b's witness, the
verdict DIVERGE unchanged (32 against 33); CP9 the land's debit OPEN, the census's CLOSED, the two counted statuses, land_divided_among =
left_egypt (the Zelophehad runner's running setting, read by call).

THE DOCKET (logic/oral_triage/num_26_second_census_exam_{DATE}.md): 264 rows by the union rule — 19 link rows in four works, 245 topic rows
by address (Bava Batra 117a-123a whole, 143b, Sotah 12a-13a whole, Sanhedrin 110a, Yoma 73b, Mishnah Bava Batra 8:1-2 and 7:1-4, Seder Olam
Rabbah 9-10 — its chapters under an EMPTY KEY in the export, measured); LAW 52, DERIVATION 42, DISPUTE 12, CONTEXT 149, OUTSIDE 9 (27:21's
Urim rows — Joshua's appointment not compiled — and Yoma's afflictions); 124 credited with a quick look (THE TENT's inheritance docket 53);
the crowns in the file (the dead inherit the living on the Talmud's page; the lot's mouth the oracle's; by tribes then by numbers within —
the table's two grains the Talmud's two levels; "only" twice; the spies' and the protesters' portions; ten parts; morasha both ways;
Jochebed on three pages; the fifteenth of Av; Levi outside and the age edges; Korach's two deaths on one verse; the plural for one son;
Serah on both rolls; Joseph's double on the census's face).

THE DESIGN'S CORRECTIONS, each read off an instrument: (i) the named rows 27 -> 29 (Eliab, Nemuel son of Eliab); (ii) the placement of the
command line (the stitcher's print); (iii) "Moses and Eleazar" seven -> ten adjacent (the DB); (iv) Ard bare at 26:40 (the first run's
assert); (v) the four token edges and the pointer the census demanded (the gate's first fail); (vi) balak's live call (the gate); (vii)
the two loops rewritten as literals (the daemon gate).

OWED FORWARD: NADAB AND ABIHU HAVE NO ENTITY on the tape (the eighth day's fire — Lev 10:1-2 — wrote on no person; the shemini-day runner's
debt); DATHAN'S, ABIRAM'S AND KORACH'S put_to_death BODY ENTRIES OPEN (the swallowing is the death; law_korach closes none — beside Korach's
open plague of 17:11, 7b's debt); 27:12-23 (Joshua's appointment; 27:21 "the judgment of the Urim" — the lot's mouth) NOT COMPILED at THE
TENT (the daughters' runner spans 27:1-11 and 36) — a readback line; the land's debit divide_the_land OPEN to Joshua 14-19 (the readback);
the Midian debit and Balaam's death at Matot (7b's); THE BACKWARD SEEDING FILED (the ark's kinds, Genesis 10, Genesis 46 by name) — built
when a daemon queries a person before Numbers 1.

LESSONS (banked in memory): THE TABLE IS THE DAEMON'S INSTRUMENT — the deltas are read from the daemon's own earlier rows, and a world
without them declares none (the scene's bench has no table row); A ROW IS NOT A WRITE — the RUN tuple unmoved by 136 rows, the class ROW
its own count (the design's arithmetic held); THE DAEMON GATE READS LITERAL SUBMITS ONLY, a third time (two loops at one sitting); A
CONSTANT READ IS NO CALL FORM (CB.COUNT — the dependency gate demands `alias.name(`); A RETYPE COVERS EVERY LINE OF A MULTI-LINE LITERAL,
again (RUN's and PREVIOUS_RUN's third lines); THE OLD CHECKPOINT KEEPS ITS VERSES, again (CL2's global marker count scoped); THE STITCHER'S
PLACEMENT RULE — an event whose key is the marker's verse takes the marker's class (the command line at 25:19); THE MEASUREMENT PASS ON THE
HAND'S FACTS, again (ten seats for seven; Ard bare); THE TOKEN CENSUS NAMES THE HOMOGRAPHS AMONG FAMILY NAMES (Becher, Shillem, the firstborn
son); THE EXPORT'S CHAPTERS CAN SIT UNDER AN EMPTY KEY (Seder Olam Rabbah — a fifth defect class of the shelf export); A HYPOTHESIS CELL IS
COUNTED APART (the ark's roster — the H tag's first exemplar in a FRACTIONS line).

NEXT on the ruling: CHAPTER 28 — the reading (28:1-30:1 the portion's grain, the daily and festival offerings; chapter 27 frozen at THE
TENT and skipped), THEN its compile — never the next reading first.
'''
append(f'{ROOT}/World/step9/NUMBERS_WALK.md', ASBUILT)

# ---- B. COMPILE_DEBT.md ----
DEBT = f'''
## SITTING 8b ({DATE}, THE COMPILE OF THE SECOND CENSUS AND THE POPULATION TABLE — Numbers 25:19-26:65; NUMBERS_WALK.md "Sitting 8b" design + as-built): THE SITTING-8 BOX
## ABOVE PAID — (a) the parser: nothing owed, none taught (the chapter re-measured right at every seat); (b) THE TWO CENSUSES AS TABLES: cold_run_second_census.py
## (the 50th runner, law_second_census the 55th daemon) 70/70 on the second graded run, THE POPULATION TABLE built as engine state (World.tables; the fifth registry
## population_schema.yaml; World.row never by hand; the ninth log class ROW -> run.row; the fifth view run_population; the fifth question `population`; probes 0/9 -> 9/9)
## with the two rolls as counted rows (12 + 4 + 69 + 9), the deltas DECLARED (Simeon -37,100 explained by the plague's 24,000 by CALL, -13,100 labeled; the Levites +1,000
## labeled; the other eleven wholly unexplained), the family table 57 with gentilics keyed to Genesis 46 (five absent, nine renamed, two moved), the daughters' row (26:33)
## and Jochebed's row (26:59) by CALL to zelophehad and joseph (CP7, CP8 — CJ3b's witness, the verdict DIVERGE kept), the land's two functions with land_divided_among READ
## from the Zelophehad runner's row (three settings), the membership predicate CP5 on the table against the ledger's death entries, the Levite families five for eight;
## (c) THE TAPE: 25:19's marker READING-PLACED at (40, 6, 1) (Seder Olam 9:2's order), the five lines, RUN (1244, 52, 52, 0, 12, 1469, 26, 302, the four pairs, 114) matched on
## the second tape run, THE REST 7b's exactly, CP1-CP9, the sweep {SW_OK}/{SW_N} at {SW_CELLS:,}; the edges second_census -> bamidbar, balak, korach, shelach, zelophehad, joseph, chukat,
## shemini_day CALL, family VIA zelophehad, moadim / offerings / pesach FALSE (Becher, Shillem, the firstborn son), the 26:4 pointer RUN_CITATION, sequence -> second_census
## the registration. STILL OWED / NEW: KORACH'S PLAGUE ENTRY (17:11) OPEN — 7b's line stands; DATHAN'S, ABIRAM'S AND KORACH'S put_to_death BODY ENTRIES OPEN on the tape
## (the swallowing is the death — law_korach closes none: a close by the deed at 16:32-33 owed); NADAB AND ABIHU NO ENTITY (Lev 10:1-2's fire wrote on no person — the
## shemini-day runner owes the two named rows their ledger entries); 27:12-23 NOT COMPILED (Joshua's appointment; 27:21 'the judgment of the Urim' = 26:56's lot's mouth —
## the daughters' runner spans 27:1-11 and 36): a readback line; the land's debit divide_the_land OPEN to Joshua 14-19 (the readback); THE BACKWARD SEEDING FILED (the
## owner's call {DATE}): the ark's kind table (Gen 6:19-20, 7:2-3, 7:14, 8:19), the nations table (Gen 10), Genesis 46's roster by name (the Joseph runner's ROSTERS) —
## built when a daemon queries a person before Numbers 1; "kinds do not mix" a data row until Lev 19:19; the ark-roster link a HYPOTHESIS cell (class H), no teacher.
'''
append(f'{ROOT}/World/step9/COMPILE_DEBT.md', DEBT)

# ---- C. RESEARCH_LOG.md ----
RL = f'''
## {DATE} — THE SHELF EXPORT'S CHAPTERS UNDER AN EMPTY KEY, "MOSES AND ELEAZAR" AT TEN SEATS NOT SEVEN, ARD BARE ON THE ROLL, AND THE TOKEN CENSUS'S HOMOGRAPHS AMONG THE FAMILY NAMES (THE NUMBERS WALK sitting 8b, the compile of the second census; the docket logic/oral_triage/num_26_second_census_exam_{DATE}.md)

1. THE EXPORT'S CHAPTERS UNDER AN EMPTY KEY. The Seder Olam Rabbah export's "text" is a DICTIONARY, not a list — two keys, "Introduction" (an empty list) and
   "" (the empty string), the thirty chapters under the empty key. The docket scan's chapter lookup (a list index) printed NO SUCH NODE for chapters 9 and 10
   until the shape was measured; the five rows (9:1-2, 10:1-3) entered by address after the fix. A FIFTH DEFECT CLASS of the shelf export beside the mistyped
   heads, the mistyped citations inside rows, the translator stopping mid-row and the English reversing a frame: the export's TREE SHAPE differs by work.
2. "MOSES AND ELEAZAR" ADJACENT AT TEN SEATS. The reading's prose (sitting 8) said the pair stands at "seven seats from 20:28"; the compile's measurement on
   the DB — the tokens משה ("Moses") and ואלעזר ("and Eleazar"), or משה ואל אלעזר ("Moses and to Eleazar"), adjacent — finds TEN in Numbers: 20:28 (the
   succession's own verse), 26:1, 26:3, 26:63, 31:12, 31:13, 31:31, 31:51, 31:54, 32:2. The reading counted another form; the runner's assert typed from the print;
   the reading ledger carries the correction row (append-only).
3. ARD BARE ON THE ROLL. 26:40 "and the sons of Bela were ARD and Naaman; [of Ard] the family of the Ardite, of NAAMAN the family of the Naamite" — the DB
   writes אַרְדְּ ("Ard") bare and לְנַעֲמָן ("of Naaman") with the preposition: the roll gives Ard's family its gentilic without repeating his name under the
   preposition. The runner's first assert fell on the hand's לארד; the typed fact retyped from the verse.
4. THE TOKEN CENSUS'S HOMOGRAPHS AMONG THE FAMILY NAMES. The dependency gate's type census read three family names as institution tokens: Becher (26:35,
   Ephraim's family — the first-fruits stem בכר), Shillem (26:49, Naphtali's — the peace offering's stem שלם), and "Reuben the firstborn" (26:5 — the firstborn's
   redemption): each dispositioned FALSE with its name; and the land's "inheritance" (26:53-56, 26:62) as the family engine's institution — VIA the Zelophehad
   runner. A roll of proper names is a field of homographs for a stem census; the gate names them, the file answers each.
'''
append(f'{ROOT}/RESEARCH_LOG.md', RL)

# ---- D. THE_STEPS.md ----
STEPS = f'''SITTING 8b — THE COMPILE OF THE SECOND CENSUS AND THE POPULATION TABLE ({DATE}, on Brian's "Let's discuss the database option
again" / "What do you recommend" / "Ok go"; World/step9/NUMBERS_WALK.md "Sitting 8b"). The machine gained a POPULATION TABLE beside its
ledger: engine state written only by a daemon consuming an event (a row by hand is refused), its columns a registry of the ink's own words
(population_schema.yaml — the fifth registry), two grains (persons the roll names; counted rows per tribe and family, the families with no
number because the ink gives none) and a third for the DECLARED deltas; journaled as the ninth log class, read back by a fifth view and a
fifth question. The second census's runner filled it: the twelve at both seats by the parser, 603,550 and 601,730, the deltas declared —
Simeon's fall explained by the Peor plague's 24,000 by call and 13,100 labeled unexplained, the Levites +1,000 labeled, the rest wholly
unexplained; fifty-seven families keyed to Genesis 46; twenty-nine named persons with the ink's clause on each; the daughters' row on the
table BEFORE their plea, Jochebed's row the witness the seventy's missing one waited on. The land's law as two functions (size by count,
place by lot) with the division's three-way dispute read from the Zelophehad runner's row; the membership predicate checked against the
ledger's death entries (five of the roll's named dead carry one, Nadab and Abihu have no entity — a debt named). The docket 264 rows; the
runner 70/70; the tape's RUN tuple predicted and matched on the second run (the literals' third lines lagged); the sweep {SW_OK}/{SW_N} at
{SW_CELLS:,}. Filed, not built: the table's seeding backward to the ark, Genesis 10 and Genesis 46. Next: chapter 28 (27 frozen at THE TENT).

'''
insert_before(f'{ROOT}/THE_STEPS.md', '## THE FINDINGS LOOP + THE STAMP LAW (owner-approved 2026-08-31)', STEPS)

# ---- E. THE_BRIEFING.md ----
SB = f'''- **THE POPULATION TABLE IS BUILT AND THE SECOND CENSUS FILLS IT — SITTING 8b DONE: A DAEMON WRITES ROWS, NEVER BY HAND; THE DELTAS ARE DECLARED, NOT DERIVED; THE DAUGHTERS' ROW STANDS ON THE TABLE BEFORE THEIR PLEA** ({DATE}, on your "Ok go" after the database discussion; World/step9/NUMBERS_WALK.md "Sitting 8b"). The engine's fifth registry (the columns the ink's own words), the ninth log class, the fifth view and question; the runner 70/70, the tape 10/10 with CP1-CP9, the sweep {SW_OK}/{SW_N} at {SW_CELLS:,}; Simeon's 13,100 beyond the plague labeled unexplained; Jochebed's row the witness the seventy's missing one waited on; the backward seeding filed on your call.
'''
insert_after(f'{ROOT}/THE_BRIEFING.md', '## SCOREBOARD (as of 2026-09-11, latest)\n', SB)
ENTRY = f'''### {DATE} — THE MACHINE GETS A POPULATION TABLE, AND THE SECOND CENSUS FILLS IT

You asked to discuss the database option again and then said "Ok go" on the
recommendation: build the table inside the compile of chapter 26, minimal and
honest, and file the seeding backward (the ark, Genesis 10, Genesis 46) for a
later pass. Sitting 8b did that (World/step9/NUMBERS_WALK.md "Sitting 8b").

What changed in the machine: the world engine now carries a TABLE beside its
ledger. Its columns are a registry of the ink's own words — tribe, family, the
number of names, the counted, son of, the clauses the roll writes about a person
("died in the land of Canaan", "had no sons, only daughters", "born to Levi in
Egypt"). A row is written only by a daemon consuming an event; a row written by
hand is refused by the engine itself. A row is not a ledger entry and moves none
of the tape's counts; it is its own class in the log, journaled, and read back by
a fifth view and a fifth question ("population" — all rows, or one tribe's).

What the second census wrote into it: the twelve tribes at both censuses with the
parser's numbers (603,550 and 601,730), fifty-seven families with their gentilics
and NO number (the ink gives none, so the table keeps none), twenty-nine persons
the roll names, and the deltas — DECLARED, never derived. Simeon's fall of 37,100
is explained in part by the Peor plague's 24,000 (fetched from the Balak runner;
the tribe the tradition's claim, not the ink's), and 13,100 stays labeled
unexplained; the Levites' rise of 1,000 and every other tribe's change are wholly
unexplained and say so. The first readers of the table are the daughters of
Zelophehad — their row "had no sons, only daughters" stands on the table BEFORE
their plea at 27:1, and the inheritance engine answers from it — and Jochebed,
whose row "born to Levi in Egypt" is the ink witness the seventy's missing one
waited on since the Joseph chapters; that checkpoint stays DIVERGE on purpose,
because the row is a witness, not a resolution.

The honest catches of the sitting, each read off an instrument: the roll's Ard
stands bare where the hand typed a preposition; "Moses and Eleazar" stand
adjacent at ten seats, not the reading's seven; the stitcher placed the census's
first line by the marker's own class; three of the roll's family names are
homographs of institution tokens (Becher, Shillem, "the firstborn") and the
dependency gate named them; and two loops in the runner had to become literal
lines because the daemon gate reads literals only. The docket read 264 Talmud
rows, the runner passed 70 of 70, the tape 10 of 10 with nine new checkpoints,
the sweep {SW_OK} of {SW_N} runners at {SW_CELLS:,} cells. Nadab and Abihu have no
entity on the tape (the eighth day's fire wrote on no person) — a debt named,
not hidden. Next on the ruling: chapter 28.

'''
insert_after(f'{ROOT}/THE_BRIEFING.md', '## ENTRIES (newest first)\n\n', ENTRY)

# ---- F. World/RESUME.md ----
RES = f'''SITTING 8b DONE {DATE} (THE COMPILE OF THE SECOND CENSUS AND THE POPULATION TABLE; NUMBERS_WALK.md "Sitting 8b" design + as-built; the owner: "Ok go" on the one-sitting form): THE POPULATION TABLE as engine state (World.tables; population_schema.yaml the FIFTH registry; World.row never by hand; the NINTH log class ROW -> run.row; the fifth view run_population; the fifth question `population`; population_probes 0/9 -> 9/9); cold_run_second_census.py the 50th runner 70/70 (second run — Ard bare), law_second_census the 55th daemon writing 136 rows (counted 94, delta 13, named 29) — the deltas DECLARED, Simeon's 13,100 labeled; the docket 264 rows (52 LAW); eight engines CALLED; the 25:19 marker reading-placed; RUN (1244, 52, 52, 0, 12, 1469, 26, 302, four pairs, 114) matched on the second tape run (the literals' third lines), THE REST 7b's exactly, CP1-CP9; the sweep {SW_OK}/{SW_N} at {SW_CELLS:,}; the seeding backward FILED. NEXT: chapter 28's reading (27 frozen at THE TENT, skipped), then its compile.
'''
insert_after(f'<world-link>/RESUME.md', rd('<world-link>/RESUME.md').split('\n')[[i for i, l in enumerate(rd('<world-link>/RESUME.md').split('\n')) if l.startswith('SITTING 8 DONE 2026-09-11')][0]] + '\n', RES)

# ---- G. the reading ledger's correction row (append-only) ----
CORR = f'''
## CORRECTION APPENDED AT THE COMPILE (sitting 8b, {DATE}) — append-only, the rows above stand
- THE INK block's line '"Moses and Eleazar" seven seats from 20:28' is corrected by the compile's measurement on the DB: the pair ADJACENT (משה ואלעזר — "Moses and Eleazar"; משה ואל אלעזר — "Moses and to Eleazar") stands at TEN seats in Numbers — 20:28, 26:1, 26:3, 26:63, 31:12, 31:13, 31:31, 31:51, 31:54, 32:2 — the first the succession's own verse, the second this chapter's command; the reading's seven counted another form (cold_run_second_census.py's ME_SEATS; RESEARCH_LOG.md {DATE}). No claim of the manifest carries the count; PN26A-01 stands.
'''
append(f'{ROOT}/logic/oral_triage/num_26_second_census_{DATE}.md', CORR)

# ---- H. memory ----
p = f'{MEM}/numbers-in-order-ruling.md'
replace_once(p, "NEXT the compile of the second census (8b), then chapter 28\"", f"SITTING 8b DONE {DATE} (THE POPULATION TABLE built as engine state — the fifth registry, World.row never by hand, the ninth log class, the fifth view and question, probes 0/9 -> 9/9; the second census compiled 70/70, 136 rows written, the deltas DECLARED with Simeon's 13,100 labeled; RUN matched on the second tape run, THE REST 7b's exactly, CP1-CP9; the sweep {SW_OK}/{SW_N} at {SW_CELLS:,}; the seeding backward filed); NEXT chapter 28\"")
insert_before(p, 'Related: [[the-loop-ruling]]', f'''SITTING 8b DONE {DATE} — THE COMPILE OF THE SECOND CENSUS AND THE POPULATION TABLE (NUMBERS_WALK.md "Sitting 8b" design + as-built; the owner: "Let's discuss
the database option again" -> "What do you recommend" -> "Ok go" on the recommendation — one sitting, the table built first as engine state, the backward seeding
FILED): World.tables + population_schema.yaml (the FIFTH registry — the columns the ink's words; grains counted / named / delta), World.row (a daemon consuming an
event, NEVER BY HAND — refused in code; the schema's three refusals), World.population (the daemons' query), the NINTH log class ROW -> run.row (the register, the
sink), the fifth view run_population + the views gate's check, the fifth question `population [tribe]`; population_probes.py 0/9 -> 9/9, journal and view probes
unmoved; cold_run_second_census.py the 50th runner (law_second_census the 55th) 70/70 on the second graded run (Ard bare at 26:40 the one typed fact; "Moses and
Eleazar" ten adjacent seats measured for the reading's seven), the narrative's 136 rows PREDICTED AND MATCHED FIRST RUN (counted 12 + 4 + 69 + 9, delta 12 + 1, named
29); the deltas DECLARED — Simeon -37,100 explained by the plague's 24,000 by CALL (the tribe the shelf's row), -13,100 labeled; the Levites +1,000 labeled; eleven
wholly unexplained; the docket 264 rows (19 link, 245 topic; 52 LAW; 124 credited); the gates' first fails read (two loops -> literal submits; four token
homographs FALSE / VIA; the 26:4 pointer; CB.COUNT no call form); the 25:19 marker reading-placed at the counter's day; RUN (1244, 52, 52, 0, 12, 1469, 26, 302,
four pairs, 114) matched on the SECOND tape run (the RUN and PREVIOUS_RUN literals' THIRD LINES lagged; CL2 scoped; CP6's set), THE REST 7b's exactly, CP1-CP9
MATCH, the probe gates and the journal gate GREEN, the sweep {SW_OK}/{SW_N} at {SW_CELLS:,}. OWED: Nadab and Abihu no entity; the three put_to_death entries open;
27:12-23 uncompiled; the seeding filed. NEXT: CHAPTER 28 — the reading, then its compile; never the next reading first.
''')
p = f'{MEM}/step9-exam-era.md'
insert_before(p, '⚠ THE NUMBERS WALK sitting 8 — THE SECOND CENSUS\'S READING', f'''⚠ THE NUMBERS WALK sitting 8b — THE COMPILE OF THE SECOND CENSUS AND THE POPULATION TABLE ({DATE}): THE TABLE IS THE DAEMON'S INSTRUMENT — the deltas are read from the daemon's own earlier rows (World.population) and a world without them declares none. A ROW IS NOT A WRITE — the class ROW is its own count (136 on the tape), the RUN tuple unmoved by it; a row's subject is not an entity (tribes and families stay names; the persons the roll names enter the table, the registry unchanged). A ROW BY HAND IS REFUSED BY THE ENGINE (World.row demands a consuming daemon) and a row outside the fifth registry's schema is refused three ways — probes written first, 0/9 then 9/9. THE DAEMON GATE READS LITERAL SUBMITS ONLY, A THIRD TIME — two loops (the narrative's LINES, the scene's tuple) read as '?UNRESOLVED?' with ten kinds 'submitted on NO tape'. A CONSTANT READ IS NO CALL FORM — CB.COUNT left the balak edge dead; the gate demands `alias.name(`. A RETYPE COVERS EVERY LINE OF A MULTI-LINE LITERAL, AGAIN — RUN's and PREVIOUS_RUN's third lines (the closes) lagged the retyped heads. THE OLD CHECKPOINT KEEPS ITS VERSES, AGAIN — CL2's global 'markers 156' moved by the new marker: scoped to Balak's span. THE STITCHER'S PLACEMENT RULE — an event whose key is the marker's own verse takes the marker's class (the command line at 25:19 reading_placed; the design had typed page_order). THE MEASUREMENT PASS ON THE HAND'S FACTS, AGAIN — "Moses and Eleazar" ten adjacent seats for the reading's seven; Ard BARE at 26:40 where Naaman carries the preposition. THE TOKEN CENSUS NAMES HOMOGRAPHS AMONG FAMILY NAMES (Becher, Shillem, Reuben the firstborn son) and the land's 'inheritance' (VIA zelophehad). THE EXPORT'S CHAPTERS CAN SIT UNDER AN EMPTY KEY (Seder Olam Rabbah's 'text' a dict — a fifth defect class). A HYPOTHESIS CELL IS COUNTED APART (the ark's roster beside 26:64 — class H, the FRACTIONS line's first 'hypotheses 1/70'). THE COMPILE SITTING'S SHAPE HELD with the table's step first: design -> probes to FAIL -> the engine -> probes 9/9 -> docket -> types -> gates to FAIL -> runner (70/70 second run) -> recorder -> stitcher -> literals -> tape (10/10 second run) -> probe gates -> journal gate -> sweep -> records.
''')
p = f'{MEM}/MEMORY.md'
OLD = "UNCOMMITTED since a42f518. NEXT: THE COMPILE OF THE SECOND CENSUS (8b) — the two censuses as tables with the ink's checkpoints, the population-table design on the owner's word — THEN chapter 28 (27 frozen, skipped) — never the next reading first."
NEW = f"SITTING 8b DONE {DATE} — THE COMPILE OF THE SECOND CENSUS AND THE POPULATION TABLE (the owner: 'Ok go' on the one-sitting form; World.tables + population_schema.yaml the FIFTH registry, World.row NEVER BY HAND, the NINTH log class run.row, the fifth view run_population, the fifth question `population`, probes 0/9 -> 9/9; law_second_census the 55th daemon writing 136 rows; the deltas DECLARED, Simeon's 13,100 labeled; the runner 70/70; RUN (1244, 52, 52, 0, 12, 1469, 26, 302, four pairs, 114) matched on the second tape run — the literals' third lines; CP1-CP9; the sweep {SW_OK}/{SW_N} at {SW_CELLS:,}; the docket 264 rows; the seeding backward FILED). UNCOMMITTED since a42f518. NEXT: CHAPTER 28 (27 frozen at THE TENT, skipped) — the reading, then its compile; never the next reading first."
replace_once(p, OLD, NEW)
assert os.path.getsize(p) < 17400, os.path.getsize(p)

# ---- I. the state doc — COMPACTION POINT #134 ----
SD = f'''
═══ COMPACTION POINT #134 ({DATE} — written at THE NUMBERS WALK sitting 8b's close; THE SECOND CENSUS COMPILED AND THE POPULATION TABLE BUILT; NUMBERS 1:1-26:65 READ, FROZEN, COMPILED AND ON THE TAPE, 27 by THE TENT) ═══
STATE: 201 frozen units (unmoved), standing 2075, hash 8b8fff1fa28953af UNMOVED (no unit changed); 50 runners, 55 daemons, the sweep {SW_OK}/{SW_N} at {SW_CELLS:,} graded cells (7b's 5,718 + the second census's 70); the journal gate GREEN (the fifth view's population check on every world); RUN (1244, 52, 52, 0, 12, 1469, 26, 302, the four pairs, 114); the running world's log MARKER 157, EVENT 1244, WRITE 1469, TIMER-SET 52, TIMER-FIRE 52, ROW 136, RETRO-WRITE 12; the index 18,963 rows from 8 segments.
THE OWNER'S DECISION: "Let's discuss the database option again" -> "What do you recommend" -> "Ok go": the population table built INSIDE 8b as one sitting, minimal and honest, the backward seeding (the ark, Genesis 10, Genesis 46) FILED — the file ARCHITECTURE/DATABASE_SPECULATION.md section 3 answered (our append; the file's committing the owner's call; our staging excludes ARCHITECTURE).
THE ENGINE (world_engine.py, world_journal.py, run_views.sql, event_kinds.yaml, journal_probes.py; the design NUMBERS_WALK.md "Sitting 8b"; the as-built THE_LOOP.md's ninth-class section): World.tables the tables of THE FIFTH REGISTRY World/step9/population_schema.yaml (the columns the ink's own words; grains counted / named / delta with required and optional columns); World.row — a daemon consuming an event, NEVER BY HAND (refused in code), the schema's three refusals, the stamps written_by / day / year / table, the log class ROW; World.population the daemons' query; the ninth journal class run.row (the register, the sink's subj / unit / ref); the fifth view run_population and the views gate's population check; the fifth question `population [tribe]`; population_probes.py 0/9 -> 9/9, journal 6/6, view 6/6, installation 6/6 (I5 55), {PR}.
THE COMPILE (NUMBERS_WALK.md "Sitting 8b" design + as-built; the docket logic/oral_triage/num_26_second_census_exam_{DATE}.md — 264 rows, 19 link + 245 topic, LAW 52 / DERIVATION 42 / DISPUTE 12 / CONTEXT 149 / OUTSIDE 9, 124 credited): cold_run_second_census.py the 50th runner (the guard 70; 35 probes; F1-F5 with one HYPOTHESIS cell, class H — the ark's roster, no teacher; fourteen number rows; the scene; the narrative's 136 rows PREDICTED AND MATCHED FIRST RUN) 70/70 ON THE SECOND GRADED RUN — Ard BARE at 26:40 the one typed fact; "Moses and Eleazar" TEN adjacent seats measured for the reading's seven (the ledger's correction row appended); law_second_census the 55th daemon: four writes, one close, no timer, THE TABLE'S ROWS at four kinds (the two SHARED kinds census_taken / levites_counted rows only — chapter 1's and 3's snapshots; the second census's tribes, families, deltas computed FROM THE TABLE, named rows); eight engines CALLED (bamidbar, balak — peor('plague_count'), a constant read no call form —, korach, shelach, zelophehad — the land row READ, never re-declared —, joseph, chukat, shemini_day); the gates' first fails read (the daemon gate: two loops -> literal submits, 7b's lesson at a second seat; the dependency gate: family VIA zelophehad, moadim / offerings / pesach FALSE — Becher, Shillem, the firstborn son —, the 26:4 pointer RUN_CITATION, the balak live call); both GREEN (55 daemons, 382 wrapped; 398 edges + 157 pointers, 275 live); the stitcher's CENSUS (2144, 1253, 1244, 875, 6, 10, 9, 0, 71, 157, 125, 15, 17, 789, 265) and PLACEMENT (markers 102 / 40; events 106 / 1098 / 40 — the command line at the marker's own verse reading_placed, read at the print); the tape's FIRST RUN read three misses (the RUN and PREVIOUS_RUN literals' THIRD LINES — the closes 113 / 110 —, CL2's global marker count scoped to Balak's span, CP6's set) and the SECOND matched: RUN as predicted, THE REST 7b's EXACTLY, CP1-CP9 MATCH, 10/10.
THE CHECKPOINTS: CP1 136 rows by grain and census (12 + 4 + 69 + 9 counted, 12 + 1 delta, 18 + 9 + 2 named), all law_second_census's; CP2 the twelve at both seats = the parser's, 603,550 and 601,730, five fell (-61,020), seven rose (+59,200), -1,820; CP3 Simeon's -37,100 explained by the plague's 24,000 (by CALL; the tribe the shelf's row plague_tribe) and -13,100 UNEXPLAINED, eleven deltas wholly unexplained; CP4 the Levites 22,000 -> 23,000 (+1,000 labeled), five families for eight; CP5 THE MEMBERSHIP PREDICATE — five of the roll's named dead with a death-class entry (Er, Onan; Dathan, Abiram, Korach), Nadab and Abihu NO ENTITY (a debt), Caleb and Joshua none, the decree's timer fired before the census, the Levites' block since 18:23-24, Korach's plague of 17:11 STILL OPEN; CP6 the 25:19 marker reading_placed at (40, 6, 1), markers 157; CP7 the daughters' five rows on the table BEFORE the 27:1 marker, heir_of = daughter; CP8 Jochebed's row "born to Levi in Egypt" — CJ3b's witness, the verdict DIVERGE kept; CP9 the land's debit OPEN, the census's CLOSED, land_divided_among = left_egypt by call.
THE RECORDS: NUMBERS_WALK.md "Sitting 8b" (design + as-built); THE_LOOP.md's ninth-class section; COMPILE_DEBT.md's sitting-8b box (the sitting-8 box PAID; NEW: Nadab and Abihu no entity; the three put_to_death entries open; 27:12-23 uncompiled — a readback line; the seeding filed); RESEARCH_LOG.md's four findings (the export's chapters under an empty key — a fifth defect class; ten seats; Ard bare; the homographs among family names); the reading ledger's correction row; THE_STEPS' sitting-8b paragraph; THE_BRIEFING's scoreboard bullet and entry (THE MACHINE GETS A POPULATION TABLE); World/RESUME.md; ARCHITECTURE/DATABASE_SPECULATION.md's "Built at the compile" (excluded from our staging); the three memory files. LAST COMMIT a42f518; UNCOMMITTED: sitting 8's and 8b's paths — commit only on "commit push".
NEXT on the ruling: CHAPTER 28 — the reading (the portion opening at 28:1: the daily and festival offerings — the Sifrei's piskaot by position; the parser measured on the chapter's own numbers; the draft's grain at both ends; chapter 27 FROZEN at THE TENT and skipped), THEN its compile (28b) on 1b's order — never the next reading first. The standing map's other items wait behind the walk unless the owner calls them; the backward seeding waits for a consumer.
POST-COMPACTION REREADS (mandatory, first sitting): numbers-in-order-ruling.md + this entry + NUMBERS_WALK.md "Sitting 8b — AS BUILT" (the compile's form with the table's step) + NUMBERS_WALK.md "Sitting 8" (the reading's form) + THE_STEPS Step 2 + Step 5 + the compiler block; memory's STANDING LESSONS head (the sitting-8b paragraph first). WATCHES: as #133's + THE TABLE IS THE DAEMON'S INSTRUMENT + A ROW IS NOT A WRITE + LITERAL SUBMITS ONLY (a third time) + A CONSTANT READ IS NO CALL FORM + THE THIRD LINE OF A MULTI-LINE LITERAL + THE OLD CHECKPOINT KEEPS ITS VERSES + THE STITCHER'S PLACEMENT RULE AT THE MARKER'S VERSE + NADAB AND ABIHU NO ENTITY + THE THREE OPEN put_to_death ENTRIES + 27:12-23 UNCOMPILED.
'''
append(f'{ROOT}/logic/pre_logic_methods_2026-07-28/PROMPT_continue_solo_era_2026-08-06.md', SD)

# ---- the lints ----
for path, base in ((f'{ROOT}/World/step9/NUMBERS_WALK.md', 0), (f'{ROOT}/World/step9/COMPILE_DEBT.md', 0), (f'{ROOT}/RESEARCH_LOG.md', 52), (f'{ROOT}/THE_STEPS.md', 1), (f'{ROOT}/THE_BRIEFING.md', 0),
                   ('<world-link>/RESUME.md', 0), (f'{ROOT}/logic/oral_triage/num_26_second_census_{DATE}.md', 0), (f'{MEM}/numbers-in-order-ruling.md', 0), (f'{MEM}/step9-exam-era.md', 7), (f'{MEM}/MEMORY.md', 5),
                   (f'{ROOT}/logic/pre_logic_methods_2026-07-28/PROMPT_continue_solo_era_2026-08-06.md', 147), (f'{ROOT}/World/step9/THE_LOOP.md', 0), (f'{ROOT}/ARCHITECTURE/DATABASE_SPECULATION.md', 0)):
    n = lint(path)
    print('%-95s lint %3d (baseline %d) %s' % (os.path.basename(path), n, base, 'OK' if n == base else 'MOVED'))
print('MEMORY.md bytes', os.path.getsize(f'{MEM}/MEMORY.md'))
print('RECORDS WRITTEN — the sweep %d/%d at %s cells; probes %s; journal gate rows %s' % (SW_OK, SW_N, format(SW_CELLS, ','), PR, JG_ROWS[:3]))
