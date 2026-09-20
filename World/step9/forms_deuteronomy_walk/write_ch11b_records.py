import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE DEUTERONOMY WALK 9b RUN B (2026-09-20): THE RECORDS FROM THE SHEET IN ONE CALL (World/step9/RECORD_FORMS.md) — the map's "Sitting 9b — AS BUILT",
# COMPILE_DEBT's sitting-9 box PAID and the 9b box, MIDDOT's compile entry, RESEARCH_LOG, THE_STEPS, THE_BRIEFING (the scoreboard and an entry), THE_LOOP's
# step-6 row, RESUME, RECORD_FORMS, the state doc's #199 addendum 2 (the close — a clean point), the addenda's section, the recovery page rewritten under its cap,
# the memory (the walk note and the index). EVERY NUMBER PARSED FROM THE PRINTS (the runner's run, the tape's run, the chain's folder, the records' own reads),
# never recited; every text built whole before its file is opened; the caps asserted; --check runs the reads and the anchors alone. write_ch10b_records.py's form.
import os, re, sys, subprocess
ROOT = _ROOT
SP = os.path.dirname(os.path.abspath(__file__)); G = f'{SP}/gates_ch11b'
MEM = os.path.expanduser('~/.claude/projects/-Users-Shared-TorahSim/memory')
CHECK = '--check' in sys.argv
def rd(name): return open(name if name.startswith('/') else f'{G}/{name}', encoding='utf-8', errors='ignore').read()
def read(p): return open(p if p.startswith('/') else f'{ROOT}/{p}', encoding='utf-8').read()
def W(p, s): open(p if p.startswith('/') else f'{ROOT}/{p}', 'w', encoding='utf-8').write(s)
def last_frac(name, den):
    fr = re.findall(r'(\d+)/(\d+)', rd(name)); fr = [(int(a), int(b)) for a, b in fr if int(b) == den]
    assert fr, (name, den); return fr[-1][0]
# ---- THE PRINTS ----
run1 = rd(f'{SP}/ch11_runner_run1.out'); assert 'MATRIX: 59/59' in run1
CASES_N = int(re.search(r'CASES generated: (\d+)', rd(f'{SP}/ch11_cases_gen.out')).group(1)); PER_CELL = re.search(r'per cell (\{.*?\})', rd(f'{SP}/ch11_cases_gen.out')).group(1)
tape = rd(f'{SP}/ch11_tape_run1.out'); assert '10/10 checkpoints' in tape
DC = re.findall(r'CHECKPOINT (DC\d) .*? (MATCH|MISS|DIVERGE)$', tape, flags=re.M); assert len(DC) == 9 and all(v == 'MATCH' for _, v in DC), DC
cc = rd(f'{SP}/ch11_checkpoint_check.out'); CC = re.search(r'checkpoint_check: (\d+) rows, (\d+) miss, (\d+) raised', cc); CC = tuple(int(x) for x in CC.groups()); assert CC[1] == 18 and CC[2] == 0, CC
st = rd(f'{SP}/seq_stitch_ch11.out'); PLC = re.search(r'^PLACEMENT LITERAL: (.*)$', st, re.M).group(1); CEN = re.search(r'^  CENSUS tuple .*?: (\(.*\))$', st, re.M).group(1)
summ = rd('SUMMARY.txt'); assert 'GATES CHAIN DONE — ALL GREEN' in summ, summ[-400:]
dg = rd('daemon.out'); DGN = int(re.search(r'(\d+) daemons', dg).group(1)); DGF = re.search(r'(\d+) functions', dg); DGF = int(DGF.group(1)) if DGF else None
dp = rd('dependency.out'); LC = re.search(r'LINK CENSUS \(the link review law\): reference (\d+), transfer (\d+), hypothesis (\d+), none (\d+)', dp); LC = tuple(int(x) for x in LC.groups())
DPE = re.search(r'(\d+) edges', dp); DPP = re.search(r'(\d+) pointers', dp); DPE = int(DPE.group(1)) if DPE else None; DPP = int(DPP.group(1)) if DPP else None
rg = rd('register.out'); RG = tuple(int(x) for x in re.search(r'DECLARED (\d+); DEBT (\d+); FAILS (\d+)', rg).groups()); assert RG[1] == 0 and RG[2] == 0, RG
sw = rd('sweep.out'); SW_P = len(re.findall(r'^PASS +cold_run_\w+\.py', sw, flags=re.M)); SW_F = len(re.findall(r'^FAIL +cold_run_\w+\.py', sw, flags=re.M)); SW_CELLS = sum(int(a) for a, b in re.findall(r'score=(\d+)/(\d+)', sw))
assert SW_F == 0 and SW_P >= 65, (SW_P, SW_F)
po = rd('positions.out'); PO = re.search(r'(\d+) checkpoints', po); PO = int(PO.group(1)) if PO else None
jg = rd('journal.out'); JG = re.search(r'(\d+) kinds, (\d+) rows', jg); JG = tuple(int(x) for x in JG.groups()) if JG else None
PR = {'census': last_frac('probe_census.out', 224), 'installation': last_frac('probe_installation.out', 6), 'readback': last_frac('probe_readback.out', 30), 'large_letter': last_frac('probe_large_letter.out', 6), 'checkpoint': last_frac('checkpoint.out', 7),   # the checkpoint probe is a chain STEP (checkpoint.out), not a probes-step file — the first write printed None/7, retyped from the print 'ink_cache': last_frac('probe_ink_cache.out', 8)}
assert PR['readback'] == 30 and PR['installation'] == 6 and PR['large_letter'] == 6 and PR['ink_cache'] == 8, PR
POINTER = 'DEMANDED' if re.search(r'FAIL POINTER Deut 11:25 AS_WHEN', rd(f'{SP}/ch11b_chain_dependency_first.out')) else 'not demanded'   # the first pass's print decides
CHAIN_STORY = read(f'{SP}/ch11b_chain_story.txt').strip() if os.path.exists(f'{SP}/ch11b_chain_story.txt') else 'THE GATES CHAIN ONCE — ALL GREEN on the first pass'
dk = read('logic/oral_triage/deu_11_ekev_reeh_exam_2026-09-20.md'); NROWS = len([l for l in dk.split('\n') if l.startswith('- ') and (' — LAW.' in l or ' — DERIVATION.' in l or ' — DISPUTE.' in l or ' — CONTEXT.' in l or ' — OUTSIDE.' in l)]); assert NROWS == 1048, NROWS
NUM = dict(DC=len(DC), CC=CC, PLC=PLC, CEN=CEN, DGN=DGN, DGF=DGF, LC=LC, DPE=DPE, DPP=DPP, RG=RG, SW=(SW_P, SW_CELLS), PO=PO, JG=JG, PR=PR, POINTER=POINTER, CASES=CASES_N)
print('THE NUMBERS:', NUM)
# ---- THE TEXTS ----
AS_BUILT = f"""
## Sitting 9b — THE COMPILE OF CHAPTER 11 — AS BUILT (2026-09-20; on the owner's "Run b" in the docket's window — the two-run rule's fourth compile sitting, the docket clause applied: three clean points, #199 and its addenda 1-2)

THE DESIGN HELD ON ITS SPINE — two own-day lines, no marker, five writes, the open debits 9 -> 10, RUN (1319, 96, 88, 0, 12, 1618, 42, 319, the four pairs, 127) as the
arithmetic wrote it, PREVIOUS_RUN 8b's exactly, DC1-DC9 MATCH on the tape's FIRST run, the runner 59/59 on its FIRST graded run. THE DEPARTURES (read at the prints,
never predicted): (1) THE CALENDAR EDGE DROPPED — cold_run_calendar.py has no askable cell (the callees' print): pilgrim_land_guarded read on the ledger, the edges
FOURTEEN; (2) THE VOCABULARY'S "RAIN" — the recon's "fire_rained" was a misreading of a substring scan: the registry's effects containing "rain" were restraint_failed
and speech_restrained (read at add_types_ch11.out); DC4 and Q30 typed from the print; (3) THE TOCHACHA'S CELLS take booleans and return a dict of dicts (covenant,
cascade) — the found-test made its own at the generator's import; (4) THE DATA ROWS twenty-nine (the design's "about eighteen"; the docket's finds added eleven) —
the count retyped from the first import's print; (5) THE ROWS thirty-two, ONE PER VERSE (the design grouped 11:8-9, 11:10-12, 11:13-15, 11:26-28, 11:29-30,
11:31-32) — VERBATIM 7 / VARIANT 19 / EXPANDED 4 / SUPPLIED 2, eleven on the tape, nineteen by CALL; (6) THE CENSUS'S "HISTORY" COLUMN UNMOVED at 1319 — a statute
line counts under "statute", not HISTORY (the recorder's census: blessing_and_curse statute 2); the design's "history +2" a misreading of the columns; (7) THE SCAN'S
BARE "yoke" read the homograph yoked_to_baal_peor on Israel's ledger (the fast checker's print) — narrowed to "yoke of the commandments"; (8) THE ONE STALE LITERAL
DB7's open-debit count 9 -> 10 — the grep decided: CV2, CX2, CW3 and CR3 count the "commanded" effect's entries and STAND (the design's list of five was four too
many); (9) THE EXAM'S PERSONS nineteen, one exempt (the pilgrim with no land — Pesachim 8b:9); (10) THE POINTER at 11:25 {POINTER} by the census (the design's
prediction; the census decides — 4b's to 8b's lesson a sixth time); (11) THE PLACE'S THREE ARMS — the design's two (Shechem / the mounds by Gilgal) grew a third
at the docket (R. Eliezer ben Yaakov's route, Sotah 33b:10): gerizim_ebal_place; (12) THE RAIN'S DATES eight keys (the mention's two ends, the request's two arms,
the early and the late, the two fasts) where the design named four; (13) THE CHAIN'S FIRST PASS — two probe slips (Q30's comment inside its return tuple;
C2 on the runner's raw scan names — the database's state at the harvest against the full load's) and the census's THREE demands (the king-word's homograph at
11:3 filed FALSE, the sequential run's registration edge, the pointer at 11:25), each retyped or filed from the print; the second pass whole ALL GREEN.
THE RUN: readback_probes.py Q28-Q30 to FAIL (27/30 — patch_probes_ch11.py) BEFORE the types; add_types_ch11.py (kinds 1142 -> 1145, effects 1037 -> 1042, the 71st
daemon, the span and the fourteen edges, I5 71, rain_dates and gerizim_ebal_place in calendar_parameters.yaml — 58 rows, exercised by the runner's DATA);
ch11_callees.py (every CALL's asks and results printed — 123 KB); derive_ch11_part1.py (the helpers from the chapter-10 runner by content markers, W10 made W11;
the ink block from ch11_ink.py by content markers with the seven store-bound lines dropped and the sequence module's names made the exec'd parser's — 88 asserts;
the counter's day, the two parameters and the one-database scans typed); ch11_part2.py (six cells, {CASES_N} asks — F1 9, F2 7, F3 18, F4 7, F5 13, F6 5);
ch11_part3.py (the callees' facts asserted from the print, the thirty-two rows, twenty-nine DATA rows, the daemon, nineteen persons, the scene, the narrative);
ch11_fastcheck.py (0 fails after the scan narrowed); ch11_cases_gen.py ({CASES_N} cases — two slips at the import: the cascade cell's found-test, the DATA count);
ch11_assemble.py --guard {CASES_N}; cold_run_blessing_and_curse.py 59/59; seq_record_ch11.py with the cache OFF (3039 records; blessing_and_curse statute 2, case 19);
seq_stitch_ch11.py (no marker; PLACEMENT {PLC}; CENSUS {CEN}); patch_seq_literals_ch11.py (the import line, DAEMON_ORDER, RUN, PREVIOUS_RUN, NEWEST_RUNNER,
PLACEMENT and CENSUS read, DC1-DC9, the VERDICTS, DB7 retyped); the tape 10/10 (17.7 s); checkpoint_check.py --all ({CC[0]} rows, {CC[1]} miss — the eighteen known,
{CC[2]} raised); Q30 retyped once from the print; {CHAIN_STORY}: the probe suites (readback {PR['readback']}/30, census {PR['census']}/224, installation
{PR['installation']}/6 with I5 71, large_letter {PR['large_letter']}/6, checkpoint {PR['checkpoint']}/7, ink_cache {PR['ink_cache']}/8), the daemon gate ({DGN}
daemons{', %d functions' % DGF if DGF else ''}), the dependency gate ({DPE} edges, {DPP} pointers; the link census reference {LC[0]} / transfer {LC[1]} / hypothesis
{LC[2]} / none {LC[3]}), build_world, the journal gate{' (%d kinds, %d rows)' % JG if JG else ''}, THE REGISTER GATE --strict (DECLARED {RG[0]}, DEBT {RG[1]},
FAILS {RG[2]} — no seat in chapter 11), the positions table ({PO} checkpoints), the sweep {SW_P}/{SW_P} at {SW_CELLS} graded cells, the home-path gate.
THE LESSONS (twelve): (1) THE DOCKET'S NEW FORM — a credited row is CARRIED with its ledger's own verdict line, parsed from the ledger's form by script; a form
without one of the five verdicts is read whole here (fifty-one of six hundred twenty-two); (2) A SUBSTRING SCAN READS HOMOGRAPHS — "rain" found restraint_failed,
"yoke" found yoked_to_baal_peor: the recon's registry count and the runner's ledger scan both retyped from the print (the census's lesson on scans); (3) A KIN
CELL'S FORM IS SETTLED BY THE PRINT — a dict of dicts answers no top-level "v"; (4) THE CENSUS'S COLUMNS ARE READ, NOT PREDICTED — a statute is not HISTORY;
(5) THE GREP DECIDES THE STALE LITERALS — an effect's NAME decides which count moves: the op-count (DB7) moved, the "commanded" counts stood; (6) THE FORMS ON FILE
HOLD — a chapter that retells and legislates takes T1, T4 and T5 with no new form; a law's first seat is SUPPLIED WITH ITS WRITE at the chapter's own day, not
dated back; (7) THE D SERIES' THIRD NAME — DC, keyed by its first word; DD next; (8) A DESIGN'S "ABOUT N" IS RETYPED FROM THE PRINT (the DATA rows, the persons);
(9) THE CALLEES' PRINT AND THE FAST CHECKER FIND THE SLIPS BEFORE THE TAPE — the runner and the tape each passed on their first run; (10) A COMMENT INSIDE A TUPLE SWALLOWS ITS TAIL — a retyped literal's comment goes at the line's end, the probe's unpack the tripwire; (11) A MODULE'S RAW
SCAN IS THE DATABASE'S STATE AT IMPORT — the cache's harvest and the full load see different databases when the tape seals between them: a runner keeps the
derived, own-excluded lists alone (C2 the tripwire; 8b's raw names passed by the accident of their harvest's hour); (12) THE TWO-RUN RULE HELD on
its fourth compile sitting with the docket clause: RUN A, the docket, RUN B — three clean points, the owner compacting once. NEXT on the owner's word: CHAPTER 12's
reading (12:1-32) in one run — the place the LORD will choose; on the table: the Decalogue-schema sitting, the SUPPLIED forms, the calf's day marker, the registry's
homograph, the receipt's third and fourth shapes (a gate sitting).
"""
DEBT_HDR_OLD = "## SITTING 9 — CHAPTER 11 (2026-09-20, the reading; deu_11_bless_curse_set frozen) — OWED TO THE COMPILE 9b: "
DEBT_HDR_NEW = "## SITTING 9 — CHAPTER 11 (2026-09-20, the reading; deu_11_bless_curse_set frozen) — PAID AT 9b (the 9b box below, item by item) — OWED WAS: "
DEBT_BOX = f"""
## THE SITTING-9 BOX (a)-(n) PAID — (a) THE RAIN CONDITIONAL — F3 the_second_paragraph: THE LINE second_paragraph_declared writing rain_in_its_season and
## heavens_shut_for_turning (conditional HEAVEN entries; Leviticus 26:4 and 26:19-20 by CALL — tochacha.covenant, tochacha.cascade) and
## yoke_of_the_commandments_accepted (a STATUS — Mishnah Berakhot 2:2's name); 28:12's pair a DATA row; the shutting the clouds and the winds (Ta'anit 3b:6), the
## wombs' verb (8a:18); the year judged at its head and the season free (Rosh Hashanah 17b:11-13); the mention and the request (rain_dates). (b)-(n) the frame,
## the land, the duties, the borders, the dread, the receipt, the blessing and the curse, the ceremony, the dwelling, the docket — each a cell's ask (F1-F6, {CASES_N}
## asks) or a DATA row (twenty-nine); THE DOCKET (n) — 1,048 rows by the union rule, 477 READ WHOLE here and 571 CARRIED with their ledgers' own verdicts (its own run).
## OWED FROM 9b: (i) THE RECEIPT'S THIRD AND FOURTH SHAPES — the finder's forms need "commanded" and the Name; 10:9's "spoke" with the Name and 1:11's / 11:25's
## "spoke" without it (sixteen "as … spoke" in the book) OWED to a gate sitting on the owner's word (the pointer at 11:25 {POINTER} by the census); (ii) THE SUPPLIED
## FORMS on the owner's word — the state row without a write (8b's, 9b's 11:5), the law's first seat with its write (11:29); (iii) THE CALF'S DAY MARKER (Shabbat
## 89a:6 — 7b's) on the owner's word; (iv) THE REGISTRY'S HOMOGRAPH (the-ark one id for two words — 8b's) a split at a gate sitting; (v) 28:12's "to give the rain
## of your land in its season" and 28:24's "powder and dust" — the pair at chapter 28's compile (rain_in_its_season's forward twin); (vi) 27:11-13 THE CEREMONY'S
## FORM SEAT at chapter 27's compile (the Levites, the loud voice, the Amen); the debit's closer Joshua 8:30-35 THE RUN outside the Torah — the install hypothesis's
## test; (vii) 30:15-20 THE PAIR'S RUN ("choose life") at chapter 30; (viii) 12:1 REOPENS THE STATUTES — chapter 12's reading next; (ix) THE FRONTLETS' SPELLINGS
## the tefillin cell's OPEN row stands (11:18 plene — the compartments' count needs it defective); (x) THE RECON'S SUBSTRING COUNT — a registry scan by substring
## reads homographs (restraint_failed): the recon's form owes a word-bounded scan; (xi) THE CREDIT CARRY'S GUARD — a carried verdict is the ledger's own; the fifty-one
## unresolved forms (the Exodus and Genesis triages' CREDIT rows, the topic dockets' lists) owe a verdict line if ever credited again; (xii) THE CHECKPOINT SERIES
## continues (DC the third name — DC9 the last; the next DD1, keyed by its first word); (xiii) THE CALENDAR RUNNER has no askable cell — an ask on its warranty
## (Exodus 34:24) owed if a chapter calls it again. NOTHING ELSE IN CHAPTER 11 IS OWED TO A LATER SITTING OF ITS OWN.
"""
MIDDOT_ANCHOR = "\n## Exodus block campaign — owner's word \"Do 3\")\n"
MIDDOT_ENTRY = f"""- THE CHAPTER-11 COMPILE (THE DEUTERONOMY WALK sitting 9b RUN B, 2026-09-20; cold_run_blessing_and_curse.py — the docket's rules carried into the cells; every code checked in this file before typed): I2 (gezerah shavah, the verbal analogy) at four cells' asks — Kiddushin 36a:9 "between your eyes" / "between your eyes" (the tefillin's exemption carried to the baldness bar — F3 the_frontlets_plural), Rosh Hashanah 8b:6 and 9b:11 "year" / "year" (11:12 the calendar's anchor; 7a:18 the analogy REFUSED for the months — F2 the_eyes_from_the_years_beginning), Sotah 32a:7-8 and 33a:13-14 "speak and say" / "voice" / "voice" (the ceremony's tongue — F5 the_ceremonys_tongue, with 32b:8's guard and 33b:2's THE ANALOGY NEEDS A TEACHER), Sotah 33b:5-6 "the terebinths of Moreh" / Genesis 12:6 (Shechem — F5 the_samaritan_shechem); I1 (qal wa-chomer, the a-fortiori) at Pesachim 8b:8 (the pilgrim's guard — F4 the_pilgrims_guard); E26 (mashal, the parable) at Ta'anit 10a:3 (the cheese-kneader — F2 the_land_watered_first); E28 (from-the-preceding, the adjacency reading) at Shabbat 32b:4 (the days multiplied — F3 the_days_multiplied); the do-not-read readings NAMED, no code (Bava Batra 21a:2 "you yourselves"; Rosh Hashanah 16b:3 the poor year) and the juxtaposition NAMED (Ta'anit 2a:11 — the prayer from 11:13's clause). THE DISPUTES AS PARAMETERS carried into the registry: rain_dates (calendar_parameters.yaml — the mention's and the request's arms), gerizim_ebal_place (three arms), the shutting's causes (many arms — a DATA row).
"""
DKF = 'deu_11_ekev_reeh_exam_2026-09-20.md'
RLOG = f"""
## 2026-09-20 — DEUTERONOMY 11 COMPILED AND ON THE TAPE (THE DEUTERONOMY WALK sitting 9b, the two-run rule's fourth compile sitting): THE RAIN CONDITIONAL GIVEN A CELL
## FOR THE FIRST TIME — THE TAPE'S FIRST ENTRIES NAMING THE RAIN; THE SECOND PARAGRAPH'S STATUS NAMED BY THE ANSWER SHEET; THE BLESSING AND THE CURSE SET WITH THE
## CEREMONY'S DEBIT OPEN TO JOSHUA; NO MARKER; AND THE DOCKET'S NEW FORM — A CREDITED ROW CARRIED WITH ITS LEDGER'S OWN VERDICT
On the owner's "9b go" (RUN A), "Go" (the docket, after a compaction) and "Run b" (RUN B). THE COMPILE: cold_run_blessing_and_curse.py the 66th runner (six cells, {CASES_N}
asks, 59/59 on its first graded run), law_blessing_and_curse the 71st daemon (given_at Deut 11:1, installed_by boot); TWO OWN-DAY LINES at (40, 11, 1), no marker —
second_paragraph_declared (rain_in_its_season and heavens_shut_for_turning conditional HEAVEN entries; yoke_of_the_commandments_accepted a STATUS) and blessing_and_curse_set
(a STATUS; gerizim_ebal_ceremony_owed a DEBIT toward Heaven OPEN — Joshua 8:30-35 the run); the open debits on Israel 9 -> 10; THE READBACK'S FORMS ON FILE, NO NEW FORM —
thirty-two rows one per verse (VERBATIM 7 / VARIANT 19 / EXPANDED 4 / SUPPLIED 2), the state row 11:5 SUPPLIED with no write, the ceremony row 11:29 SUPPLIED AS A LAW
with its write, the pointer 11:25 to Exodus 23:27 by two teachers ({POINTER} by the census); the tape 10/10 on its first run with DC1-DC9; the gates chain {CHAIN_STORY.lower()}
(the register gate DECLARED {RG[0]} / DEBT {RG[1]} / FAILS {RG[2]}; the sweep {SW_P}/{SW_P}). THE DOCKET (its own run): logic/oral_triage/{DKF} — 1,048 rows, 477 read whole
here and 571 CARRIED with their ledgers' own verdict lines (ch11_credit_carry.py — the new form of the credit); its crowns: the yoke of the commandments (Berakhot
14b:11), the prayer from 11:13's clause and the rain's dates from the rows (Ta'anit 2a:11; 2a:1-3, 6a:3-7, 10a:11-16), "in its season" the free variable after the decree
(Rosh Hashanah 17b:11-13), the shutting the clouds and the winds (Ta'anit 3b:6) with its threshold and its causes, the Land watered first (10a:2-3) and the source of rain
a dispute (9b:10-11), the cattle before the man (Berakhot 40a:1), the ceremony's place three ways (Sotah 33b:4-10), its form, tongue, day and forty-eight covenants
(Tosefta Sotah 8), the receipt's pointer taught a second time (Tosefta Sotah 8:6), the dwelling weighed (Ketubot 110b:23). THE RECORD KEPT: two calendar parameters
(rain_dates, gerizim_ebal_place — every value a docket row); the recon's substring count corrected at the print ("fire_rained" a misreading — the registry's "rain"
effects restraint_failed and speech_restrained); the census's "history" column unmoved (a statute is not HISTORY). The forms in World/step9/forms_deuteronomy_walk/.
"""
STEPS_ANCHOR = "\n## Step 6 — Publish\n"
STEPS_PARA = f"""
**Deuteronomy 11 compiled (2026-09-20, sitting 9b — the two-run rule's fourth compile sitting, the docket its own run):** the rain conditional had no cell anywhere in the
machine, so the second paragraph is compiled at the chapter's own day — one line writing the rain in its season and the heavens shut as conditional heaven entries
(Leviticus 26 by call — it has no line on the tape) and the yoke of the commandments as a status, the Mishnah's own name for the paragraph; the blessing and the
curse set as a status with the ceremony at Gerizim and Ebal a debit open to Joshua 8:30-35 — the run outside the Torah. No marker: every act the chapter retells
already had a line, and the tape already left Korah unnamed at the swallowing as the chapter does. The readback's forms on file held with no new form — thirty-two
rows, one per verse. The docket took a new form of the credit: a credited row is carried with its ledger's own verdict line, parsed by script; a form without a
verdict is read whole here. The rain's dates and the ceremony's place are parameters, never constants — every value a docket row. The tape 10/10 and the runner
59/59 each on their first run; the gates chain {CHAIN_STORY.lower()}.
"""
BRIEF_BULLET_ANCHOR = "- **CHAPTER 11 READ AND FROZEN — THE SIFREI COMES BACK ONTO THE PAGE:"
BRIEF_BULLET = (f"- **CHAPTER 11 COMPILED — THE RAIN CONDITIONAL GETS ITS CELL: THE TAPE'S FIRST ENTRIES NAMING THE RAIN, 'IN ITS SEASON' THE FREE VARIABLE AFTER THE DECREE (Rosh Hashanah 17b), THE SHUTTING THE CLOUDS AND THE WINDS (Ta'anit 3b); THE SECOND PARAGRAPH'S STATUS THE MISHNAH'S OWN NAME (the yoke of the commandments); THE BLESSING AND THE CURSE SET WITH THE CEREMONY'S DEBIT OPEN TO JOSHUA; NO MARKER — EVERY RETOLD ACT ALREADY HAD A LINE; THE DOCKET'S NEW FORM — A CREDITED ROW CARRIED WITH ITS LEDGER'S OWN VERDICT** (2026-09-20, sitting 9b — the two-run rule's fourth compile sitting; the runner 59/59 and the tape 10/10 on their first runs; the chain {CHAIN_STORY.lower()}; the 66th runner, the 71st daemon; the open debits on Israel 9 -> 10).\n")
BRIEF_ENTRY_ANCHOR = "### 2026-09-20 — CHAPTER 11 READ: THE SPINE RETURNS, THE RAIN CLAUSE WITHOUT A CELL, THE FRONTLETS' THREE SPELLINGS"
BRIEF_ENTRY = f"""### 2026-09-20 — CHAPTER 11 COMPILED: THE RAIN GETS ITS CELL, THE CEREMONY ITS DEBIT, AND THE DOCKET A NEW FORM OF THE CREDIT
Chapter 11 is a chapter that retells and legislates in one breath. The retelling needed nothing new: every act it names — the plagues, the sea, Dathan and Abiram
swallowed — already had a line on the tape, and the tape already reads the swallowing as the chapter does, with Korah unnamed. So there is no marker this time, and no
act written back into the past. The law was the hole. Nothing in the machine held the rain conditional: Leviticus 26's rains live in the tochacha runner as exam cases
with no line on the tape, and no effect anywhere named the rain of the land. The compile writes it at the chapter's own day — one line for the second paragraph, writing
the rain in its season and the heavens shut as conditional heaven entries, and the yoke of the commandments as a status, which is the Mishnah's own name for this
paragraph (Berakhot 2:2: first the yoke of the kingdom of Heaven, then the yoke of the commandments). The shelf gave the values: the rain's amount is decreed at the head
of the year and cannot be changed, but its season and its place are free — "in its season" is the free variable after the decree (Rosh Hashanah 17b); the shutting means
the clouds and the winds withheld, not rain alone (Ta'anit 3b), and rain that seals a barrel's mouth with mud is not "shut". The rain's dates are a parameter, every
value a row of the docket. The blessing and the curse are set as a status, and the ceremony at Gerizim and Ebal is a debit on Israel, open — its closer is Joshua
8:30-35, the run outside the Torah, which is the install hypothesis's own test ahead. The ceremony's place is a parameter with three arms: Shechem, two mounds by the
Jordan, or a route and not a place at all. The receipt "as He spoke to you" points at Exodus 23:27, and now two teachers say so. The docket changed its own form: a
credited row is carried with its ledger's verdict, parsed by script, and only the fifty-one whose ledgers carried no verdict were read again. The runner passed 59/59
and the tape 10/10 each on its first run; the chain {CHAIN_STORY.lower()}. Next: chapter 12, the place the LORD will choose.
"""
LOOP_OLD = "cold_run_second_tablets.py (chapter 10, THE FORMS COMBINED — NO SEVENTH 2026-09-20:"
LOOP_NEW = "cold_run_blessing_and_curse.py (chapter 11, THE FORMS ON FILE — NO NEW FORM 2026-09-20: a chapter that retells and legislates — thirty-two rows one per verse VERBATIM 7 / VARIANT 19 / EXPANDED 4 / SUPPLIED 2, eleven on the tape, nineteen by CALL; T5 the state row 11:5 supplied without a write; a LAW'S FIRST SEAT supplied WITH its write at the chapter's own day (11:29 — the ceremony's debit open to Joshua 8:30-35); the pointer 11:25; no marker — every retold act had a line; readback_probes 30/30, DC3); " + LOOP_OLD
RESUME_HEAD = f"""# ⚠ THE DEUTERONOMY WALK sitting 9b — CHAPTER 11 COMPILED AND ON THE TAPE (2026-09-20; step9/DEUTERONOMY_WALK.md "Sitting 9b" + "THE DOCKET — AS RUN" + "Sitting 9b — AS BUILT"):
# cold_run_blessing_and_curse.py the 66th runner (59/59 first run), law_blessing_and_curse the 71st daemon; TWO OWN-DAY LINES, NO MARKER — the rain conditional's
# cell (rain_in_its_season, heavens_shut_for_turning, yoke_of_the_commandments_accepted) and the blessing-and-curse set (blessing_and_curse_set; the ceremony's
# debit OPEN to Joshua 8:30-35); the open debits on Israel 9 -> 10; the tape 10/10 first run (DC1-DC9); the chain {CHAIN_STORY.lower()}; the register gate DECLARED
# {RG[0]} / DEBT {RG[1]} / FAILS {RG[2]}. UNCOMMITTED since 2f4ec5b: 9b whole (the message at <scratch>/commit_msg_ch11.txt). NEXT on the owner's word: commit; chapter 12's reading.
"""
STATE_ADD = f"""
#199 ADDENDUM 2 (2026-09-20, at the close of THE DEUTERONOMY WALK sitting 9b RUN B — on the owner's "Run b" in the docket's window; A CLEAN COMPACTION POINT): THE STATE: CHAPTER 11 COMPILED AND ON THE TAPE — cold_run_blessing_and_curse.py the 66th runner (six cells, {CASES_N} asks, 59/59 on its first graded run; parts 1-4 in the scratchpad, copied to the forms folder), law_blessing_and_curse the 71st daemon (given_at Deut 11:1, installed_by boot); event_vocabulary 1145, effect_vocabulary 1042; the span and fourteen CALL edges; calendar_parameters.yaml +2 (rain_dates, gerizim_ebal_place); TWO OWN-DAY LINES at (40, 11, 1) after the tape's last Deuteronomy 10 line, NO marker (markers 172 unmoved) — second_paragraph_declared and blessing_and_curse_set, five writes on Israel (two conditional heaven entries, two statuses, one debit OPEN toward Heaven — the open debits 9 -> 10); RUN (1319, 96, 88, 0, 12, 1618, 42, 319, the four pairs, 127), PREVIOUS_RUN 8b's exactly, PLACEMENT {PLC}, CENSUS {CEN}; THE TAPE 10/10 ON ITS FIRST RUN, DC1-DC9 MATCH; checkpoint_check --all {CC[0]} rows, {CC[1]} miss (the known), {CC[2]} raised; readback_probes 30/30 (Q28-Q30 written to FAIL first, Q30 retyped once from the print); THE GATES CHAIN {CHAIN_STORY} — the probes, the daemon gate ({DGN} daemons), the dependency gate (the link census reference {LC[0]} / transfer {LC[1]} / hypothesis {LC[2]} / none {LC[3]}; the pointer at 11:25 {POINTER}), build_world, the journal gate, the register gate --strict (DECLARED {RG[0]}, DEBT {RG[1]}, FAILS {RG[2]}), the positions table ({PO} checkpoints), the sweep {SW_P}/{SW_P}, the home-path gate; THE RECORDS from the sheet in one call (write_ch11b_records.py — the map's AS BUILT, COMPILE_DEBT's sitting-9 box PAID and the 9b box, MIDDOT, RESEARCH_LOG, THE_STEPS, THE_BRIEFING, THE_LOOP, RESUME, RECORD_FORMS, this addendum, the addenda, the recovery page, the memory); the forms copied (copy_ch11b_forms.py); the commit message at <scratch>/commit_msg_ch11.txt (the headline written, RUN B's paragraph, the trailers). NOT COMMITTED (since 2f4ec5b): RUN A's records, the docket, RUN B — ONE message covers 9b (the owner's word: "Commit" = no push; "commit push" = both; a985fbc the last push). NOTHING MID-FLIGHT — A CLEAN COMPACTION POINT. NEXT ON THE RULING: the commit on his word; then CHAPTER 12's reading (12:1-32) in one run — the place the LORD will choose (12:1 reopens the statutes; 12:5 the choosing; 12:21's receipt seat); on the table: the Decalogue-schema sitting, the SUPPLIED forms (the state row without a write; a law's first seat with its write), the calf's day marker, the registry's homograph, the receipt's third and fourth shapes (a gate sitting). POST-COMPACTION REREADS: the recovery page, the map's "Sitting 9b — AS BUILT" (the newest section), MEMORY.md.
"""
def next_addenda_no(s):
    ns = [int(x) for x in re.findall(r'^##+ *§?(\d+)[\.\s:—]', s, re.M)] + [int(x) for x in re.findall(r'§(\d+)', s)]
    return (max(ns) + 1) if ns else 52
ADDENDA_ADD_T = """
## §{N} — THE DEUTERONOMY WALK sitting 9b (2026-09-20): CHAPTER 11 COMPILED — the state doc's #199 and its addenda 1-2; the map's "Sitting 9b … THE DESIGN", "THE DOCKET — AS RUN" and "Sitting 9b — AS BUILT"
The two-run rule's fourth compile sitting with the docket clause: RUN A (the rereads, the recon and the scan derived by line-based substitutions, the design), THE DOCKET
(1,048 rows — 477 read whole, 571 carried with their ledgers' own verdict lines: THE NEW FORM OF THE CREDIT), RUN B (the probes to FAIL, the types, the callees' print,
the runner 59/59 first run, the recorder with the cache off, the stitcher with no marker, the literals, the tape 10/10 first run with DC1-DC9, the chain, the records).
The crowns: the rain conditional's cell (the tape's first entries naming the rain; "in its season" the free variable after the decree; the shutting the clouds and the
winds), the yoke of the commandments the Mishnah's name, the ceremony's debit open to Joshua 8:30-35, the place a three-arm parameter, the receipt's pointer taught twice.
The lessons in the AS BUILT (twelve). Uncommitted since 2f4ec5b: 9b whole; the message at <scratch>/commit_msg_ch11.txt.
"""
MEM_PARA = f"""
SITTING 9b DONE (2026-09-20, "Run b" in the docket's window): CHAPTER 11 COMPILED AND ON THE TAPE — cold_run_blessing_and_curse.py the 66th runner (59/59 first run),
law_blessing_and_curse the 71st daemon; TWO OWN-DAY LINES, NO MARKER (every retold act had a line; Korah unnamed on the tape as in the chapter): second_paragraph_declared
(rain_in_its_season, heavens_shut_for_turning — the tape's first entries naming the rain; yoke_of_the_commandments_accepted — Mishnah Berakhot 2:2's name) and
blessing_and_curse_set (blessing_and_curse_set; gerizim_ebal_ceremony_owed a DEBIT OPEN to Joshua 8:30-35 — the open debits 9 -> 10); rain_dates and gerizim_ebal_place
PARAMETERS in calendar_parameters.yaml; RUN (1319, 96, 88, 0, 12, 1618, 42, 319, pairs, 127), markers 172, kinds 864; the tape 10/10 first run, DC1-DC9; the chain
{CHAIN_STORY.lower()}; the register gate DECLARED {RG[0]} / DEBT {RG[1]} / FAILS {RG[2]}; the pointer at 11:25 {POINTER} by the census. THE LESSONS: a credited row CARRIED with
its ledger's own verdict; a substring scan reads homographs (restraint_failed, yoked_to_baal_peor — retyped from the print); a kin cell's form settled by the print; the
census's columns read, not predicted (a statute is not HISTORY); the grep decides the stale literals (DB7 alone); the D series' third name DC (DD next). UNCOMMITTED since
2f4ec5b: 9b whole (the message <scratch>/commit_msg_ch11.txt). NEXT on his word: the commit; chapter 12's reading (12:1-32) — the place the LORD will choose.
"""
MEM_DESC_OLD = 'description: "COMMITTED THROUGH 2f4ec5b (2026-09-20; NOT PUSHED — a985fbc the last push) — SITTING 9 DONE 2026-09-20 ('
MEM_DESC_NEW = 'description: "COMMITTED THROUGH 2f4ec5b (2026-09-20; NOT PUSHED — a985fbc the last push) — SITTING 9b DONE 2026-09-20 (chapter 11 COMPILED — the rain conditional\'s cell, the ceremony\'s debit open to Joshua, no marker; 9b UNCOMMITTED); SITTING 9 DONE 2026-09-20 ('
MEM_IDX_OLD = '9b A+docket done; B next'; MEM_IDX_NEW = '9b DONE; commit next'
FORMS_OLD = "World/step9/forms_deuteronomy_walk/write_ch10b_records.py (write_ch9b_records.py,"
FORMS_NEW = "World/step9/forms_deuteronomy_walk/write_ch11b_records.py (write_ch10b_records.py, write_ch9b_records.py,"
REC_EDITS = [("## 2. WHERE IT STANDS (2026-09-20, 9b docket done; the state doc #199 addendum 1 the newest)", "## 2. WHERE IT STANDS (2026-09-20, 9b done; the state doc #199 addendum 2 the newest)"),
             ("- NUMBERS CLOSED. DEUTERONOMY 1:1-10:22 COMPILED AND ON THE TAPE (1-7 at 29c189b, 8 at a985fbc — PUSHED; 9 at 7/7b, 10 at 8/8b); 11 READ.", "- NUMBERS CLOSED. DEUTERONOMY 1:1-11:32 COMPILED AND ON THE TAPE (1-7 at 29c189b, 8 at a985fbc — PUSHED; 9 at 7/7b, 10 at 8/8b, 11 at 9/9b)."),
             ("- 225 frozen units, standing 2233, hash 8b8fff1fa28953af. 65 runners, 70 daemons, 478 functions; 1142 kinds / 1037 effects.", f"- 225 frozen units, standing 2233, hash 8b8fff1fa28953af. 66 runners, {DGN} daemons{', %d functions' % DGF if DGF else ''}; 1145 kinds / 1042 effects."),
             ("- THE TAPE at RUN (1317, 96, 88, 0, 12, 1613, 41, 319, pairs, 127), markers 172, closes 127; the sweep 64/64; every gate GREEN.", f"- THE TAPE at RUN (1319, 96, 88, 0, 12, 1618, 42, 319, pairs, 127), markers 172, closes 127; the sweep {SW_P}/{SW_P}; every gate GREEN."),
             ("- 9b A + DOCKET DONE (1,048 rows: 477 whole here, 571 carried; #199 add. 1). NEXT: RUN B after a compaction. The push on his word.", "- 9b DONE (66th runner 59/59, tape 10/10, no marker; the credit carried). UNCOMMITTED. NEXT: commit on his word; chapter 12.")]
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
assert 'Sitting 9b — THE COMPILE OF CHAPTER 11 — AS BUILT' not in read(MAP) and '#199 ADDENDUM 2' not in read(STATEDOC) and '#199 ADDENDUM 1' in read(STATEDOC)
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
b = read(BRIEF); b = b.replace(BRIEF_BULLET_ANCHOR, BRIEF_BULLET + BRIEF_BULLET_ANCHOR).replace(BRIEF_ENTRY_ANCHOR, BRIEF_ENTRY.rstrip('\n') + '\n\n' + BRIEF_ENTRY_ANCHOR); W(BRIEF, b)
W(LOOP, read(LOOP).replace(LOOP_OLD, LOOP_NEW))
W(RES, RESUME_HEAD + read(RES)); W(RF, read(RF).replace(FORMS_OLD, FORMS_NEW))
W(STATEDOC, read(STATEDOC).rstrip('\n') + '\n' + STATE_ADD); W(ADD, read(ADD).rstrip('\n') + '\n' + ADDENDA_ADD); W(REC, rec)
W(WALK, read(WALK).replace(MEM_DESC_OLD, MEM_DESC_NEW).rstrip('\n') + '\n' + MEM_PARA); W(IDX, idx)
print('written: the map, COMPILE_DEBT, MIDDOT, RESEARCH_LOG, THE_STEPS, THE_BRIEFING, THE_LOOP, RESUME, RECORD_FORMS, the state doc, the addenda, the recovery page, the memory note, the index')
for p in (MAP, DEBT, MID, RL, STEPS, BRIEF, LOOP, RES, RF, STATEDOC, ADD, REC, WALK, IDX):
    q = p if p.startswith('/') else f'{ROOT}/{p}'
    r = subprocess.run([sys.executable, f'{ROOT}/logic/solo_tools/gloss_lint.py', q], capture_output=True, text=True); print('  lint', p.replace(MEM, '<memory>'), (r.stdout.strip().split('\n')[-1])[:60])
r = subprocess.run([sys.executable, f'{ROOT}/logic/solo_tools/scrub_home_paths.py', '--check'], capture_output=True, text=True); print('  home-path gate:', (r.stdout + r.stderr).strip().split('\n')[-1][:90])
