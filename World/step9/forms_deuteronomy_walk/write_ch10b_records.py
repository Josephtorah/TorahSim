import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE DEUTERONOMY WALK sitting 8b — THE COMPILE OF CHAPTER 10, RUN B (2026-09-20): THE RECORDS, written after every gate ran — the numbers COMPUTED from the
# gates chain's own prints in the scratchpad (gates_ch10b/*.out; never recited) and the docket's own rows; every text built whole before any file is
# opened; the ledgers appended, the map appended, the checklist's boxes marked paid, the recovery page REWRITTEN in its section 2 under its cap, the
# memory index edited under its cap. `--check` parses and prints without writing. Sitting 7b's form (write_ch9b_records.py) on the sheet World/step9/RECORD_FORMS.md.
import os, re, sys, subprocess
ROOT = _ROOT
SP = os.path.dirname(os.path.abspath(__file__))
G = f'{SP}/gates_ch10b'
MEM = os.path.expanduser('~/.claude/projects/-Users-Shared-TorahSim/memory')
CHECK = '--check' in sys.argv
def rd(name): return open(name if name.startswith('/') else f'{G}/{name}', encoding='utf-8', errors='ignore').read()
def last_frac(name, m):
    t = rd(name); f = re.findall(r'(\d+)/%d' % m, t); return int(f[-1]) if f else -1
CHAIN_STORY = "THE GATES CHAIN TWICE — the first pass stopped at the probes step (readback 24/27: 4b's Q14, 5b's Q17 and 6b's Q20 hold the marker count as a literal — 7b's lesson 12 repeated, the design's list having named Q23 alone; retyped 169 -> 172 from the print, patch_probes172_ch10.py) and at the dependency gate by SIX demands — FOUR EDGES the token census matched on HOMOGRAPHS, filed FALSE with their whys (family at 10:9 — the Levite's inheritance DENIED, Numbers 18:20's portion, not the inheritance law's transfer between heirs; offerings at 10:1 — 'come up' [olah], the ascent's verb, not the burnt offering; pre_sinai at 10:16 — the heart's circumcision, WHICH THE SHELF ITSELF REFUSES as the circumcision law's object, Shabbat 108a:7's grammar guard; priesthood at 10:18 — the widow whose judgment God executes, Exodus 22:21's, not the priest's widow of Leviticus 21-22) and the TWO POINTERS the design predicted (10:5 and 10:9 in the AS_WHEN form — RUN_CITATION of testimony_placed and of portion_declared, riding the CALL edges: the census deciding a fifth time; add_dispositions_ch10.py, the tokens checked on the DB, YAML's FALSE a boolean); the register gate GREEN at the first pass with Deut 10:5 ACT on the fragments' write (the design's prediction from 4:5's pair); the second pass whole — a rerun with the probes starts at the tape (7b's lesson 14) — ALL GREEN; THE SECOND PASS green to the register gate and FAILED AT THE POSITIONS TABLE — one of the eight workers raised on the cached path and the cache's own report of which node crashed on a shadowed name (`src` the module's source text rebound to a module in the restore loop — get_source_segment(a module): THE NINETEENTH SLIP, the cache's own reporting; renamed srcm, FORM unmoved, patch_ink_cache_src_ch10.py); a single worker rerun clean after the fix, the table measured by FOUR workers with the step's own command (7b's way) and THE THIRD PASS from the checkpoint probe (checkpoint, stamp, sweep, journal again, unmoved) ALL GREEN"
CHAIN_SHORT = "the chain three times — the first pass stopped at the probes step (three older probes' marker counts retyped) and the dependency gate (four homograph edges FALSE, the two predicted pointers RUN_CITATION); the second green to the register gate and failed at the eight-worker positions table (a worker raising on the cached path, the cache's own report masked by a shadowed name — the nineteenth slip, fixed); the positions by four workers and the third pass from the checkpoint probe ALL GREEN"
# ---- THE NUMBERS FROM THE PRINTS ----
summ = rd('SUMMARY.txt'); assert 'GATES CHAIN DONE — ALL GREEN' in summ, summ
tape = rd('tape.out'); assert '10/10 checkpoints' in tape and 'OK   THE REST' in tape
DB = re.findall(r'CHECKPOINT (DB\d) .*? (MATCH|MISS|DIVERGE)$', tape, flags=re.M); assert len(DB) == 9 and all(v == 'MATCH' for _, v in DB), DB
tape_elapsed = re.search(r'elapsed ([\d.]+)s', tape).group(1)
PL = re.search(r"PLACEMENT \(O9 T2\): markers (\{[^}]*\}); events (\{[^}]*\})", tape); assert PL
assert PL.group(1) == "{'text_constrained': 108, 'reading_placed': 49}" and PL.group(2) == "{'text_constrained': 110, 'page_order': 1149, 'reading_placed': 58}", PL.groups()
rg = rd('register.out'); m = re.search(r'DECLARED (\d+); DEBT (\d+); FAILS (\d+)', rg); assert m and 'THE REGISTER GATE: GREEN' in rg
RG = tuple(int(x) for x in m.groups())
SEAT_10_5 = re.search(r'^\s*Deut 10:5\s+(\w+)', rg, flags=re.M); SEAT_10_5 = SEAT_10_5.group(1) if SEAT_10_5 else 'unlisted'
dg = rd('daemon.out'); m = re.search(r'\((\d+) daemons, (\d+) functions\)', dg); assert m and 'gate satisfied' in dg; DG = tuple(int(x) for x in m.groups()); assert DG[0] == 70, DG
dp = rd('dependency.out'); m = re.search(r'dispositions on file: (\d+) edges, (\d+) pointers', dp); assert m and 'gate satisfied' in dp; DP = tuple(int(x) for x in m.groups())
LC = re.search(r'LINK CENSUS \(the link review law\): reference (\d+), transfer (\d+), hypothesis (\d+), none (\d+)', dp); assert LC; LC = tuple(int(x) for x in LC.groups())
m = re.search(r'required edges (\d+), required pointers (\d+); live import edges (\d+)', dp); DPR = tuple(int(x) for x in m.groups())
bw = rd('build.out'); assert 'ALL GREEN' in bw, bw[-600:]
jg = rd('journal.out'); assert 'GATE GREEN' in jg; m = re.search(r'(\d+) kinds, (\d+) rows in the index', jg); JG = tuple(int(x) for x in m.groups())
um = rd('unmoved.out'); assert 'GATE GREEN' in um and 'THE JOURNAL UNMOVED' in um, um[-300:]; st_ = rd('stamp.out'); assert 'THE JOURNAL STAMPED' in st_, st_[-300:]
sw = rd('sweep.out'); SW_P = len(re.findall(r'^PASS +cold_run_\w+\.py', sw, flags=re.M)); SW_F = len(re.findall(r'^FAIL +cold_run_\w+\.py', sw, flags=re.M))
SW_CELLS = sum(int(a) for a, b in re.findall(r'score=(\d+)/(\d+)', sw)); assert SW_P + SW_F == 64, (SW_P, SW_F); assert SW_F == 0, 'the sweep has failures — read them first'   # the 65 runners minus the sequence file the sweep skips
assert '64/64 runners green' in sw, sw[-400:]
po = rd('positions.out'); m = re.search(r'(\d+) checkpoints over (\d+) pauses', po); assert m, po[-800:]; PO = tuple(int(x) for x in m.groups())
PR = {'census': last_frac('probe_census.out', 224), 'installation': last_frac('probe_installation.out', 6), 'readback': last_frac('probe_readback.out', 27),
      'register': last_frac('probe_register.out', 7), 'sequence': last_frac('probe_sequence.out', 4), 'view': last_frac('probe_view.out', 6),
      'population': last_frac('probe_population.out', 9), 'journal': last_frac('probe_journal.out', 7), 'cursor': last_frac('probe_cursor.out', 6),
      'large_letter': last_frac('probe_large_letter.out', 6), 'checkpoint': last_frac('checkpoint.out', 7), 'ink_cache': last_frac('probe_ink_cache.out', 8)}
ck = rd('probe_clock.out'); m = re.findall(r'(\d+)/(\d+)', ck); PR['clock'] = ('%s/%s' % m[-1]) if m else 'exit 0'
assert PR['checkpoint'] == 7 and PR['readback'] == 27 and PR['installation'] == 6 and PR['large_letter'] == 6 and PR['ink_cache'] == 8, PR
run1 = rd(f'{SP}/ch10_run1.out'); assert '62/62' in run1
CASES_N = int(re.search(r'CASES generated: (\d+)', rd(f'{SP}/ch10_cases_gen.out')).group(1)); PER_CELL = re.search(r'per cell (\{.*?\})', rd(f'{SP}/ch10_cases_gen.out')).group(1)
t1 = rd(f'{SP}/ch10_tape1.out'); assert '9/10 checkpoints' in t1 and "'DA1 DIVERGE'" in t1, 'the first tape run: 9/10, DA1 the miss'
rec = rd(f'{SP}/seq_record_ch10.out'); m = re.search(r'recording: (\d+) records written', rec); REC_N = int(m.group(1)); assert REC_N > 2000, REC_N
st = rd(f'{SP}/seq_stitch_ch10.out'); m = re.search(r'CENSUS tuple .*?: (\(.*\))', st); CENSUS = m.group(1); assert '1317' in CENSUS and '172' in CENSUS and '862' in CENSUS, CENSUS
pf = rd(f'{SP}/ch10b_probes_fail.out'); assert 'readback_probes: 23/27' in pf and 'FAIL Q25' in pf and 'FAIL Q23' in pf, 'the fail print: 23/27 — Q23 on 172 before the tape, Q25-Q27 on the missing runner'
cc = rd(f'{SP}/ch10_checkpoint_check.out'); m = re.search(r'(\d+) rows', cc); CC_ROWS = m.group(1) if m else '?'
# the docket's numbers from its own rows
DK = 'logic/oral_triage/deu_10_ekev_exam_2026-09-20.md'
dk = open(f'{ROOT}/{DK}', encoding='utf-8').read()
rows = [l for l in dk.split('\n') if re.match(r'^- .*? — (LAW|DERIVATION|DISPUTE|CONTEXT|OUTSIDE)\.', l)]
VD = {v: sum(1 for l in rows if re.match(r'^- .*? — %s\.' % v, l)) for v in ('LAW', 'DERIVATION', 'DISPUTE', 'CONTEXT', 'OUTSIDE')}
NROWS = len(rows); NLINK = sum(1 for l in rows if '[LINK' in l); NTOPIC = sum(1 for l in rows if '[TOPIC' in l); NCRED = sum(1 for l in rows if 'CREDITED' in l)
NWHOLE = sum(1 for l in rows if '[whole:' in l); DKB = len(dk.encode('utf-8'))
assert NROWS == 532 and NLINK + NTOPIC == NROWS and NWHOLE == 0, (NROWS, NLINK, NTOPIC, NWHOLE)
hp = subprocess.run(['python3', 'logic/solo_tools/scrub_home_paths.py', '--check'], cwd=ROOT, capture_output=True, text=True); assert hp.returncode == 0, hp.stdout[-500:] + hp.stderr[-500:]
NUM = dict(RG=RG, SEAT_10_5=SEAT_10_5, DG=DG, DP=DP, LC=LC, DPR=DPR, JG=JG, SW=(SW_P, SW_CELLS), PO=PO, PR=PR, PL=PL.groups(), tape_elapsed=tape_elapsed, cases=(CASES_N, PER_CELL), docket=(NROWS, NLINK, NTOPIC, NCRED, NWHOLE, DKB, VD), rec=REC_N, census=CENSUS, cc_rows=CC_ROWS)
print('THE NUMBERS:', NUM)
assert 'PLACEHOLDER' not in CHAIN_STORY and 'PLACEHOLDER' not in CHAIN_SHORT, 'the chain story must be typed from the chain\'s prints before the records are written'
pr_line = ('census %d/224, installation %d/6 (I5 70), readback %d/27 (Q25-Q27 the forms combined), register %d/7, clock %s, sequence %d/4, view %d/6, population %d/9, journal %d/7, cursor %d/6, large_letter %d/6, checkpoint %d/7, ink_cache %d/8'
           % (PR['census'], PR['installation'], PR['readback'], PR['register'], PR['clock'], PR['sequence'], PR['view'], PR['population'], PR['journal'], PR['cursor'], PR['large_letter'], PR['checkpoint'], PR['ink_cache']))
gates_line = ('the daemon gate GREEN (%d daemons, %d functions WRAPPED); the dependency gate GREEN (%d edges and %d pointers on file — the link census reference %d / transfer %d / hypothesis %d / none %d; required %d edges and %d pointers, live import edges %d); '
              'build_world ALL GREEN (224 units, standing 2227, hash 8b8fff1fa28953af unmoved — no freeze this run); the journal gate GREEN before the sweep (%d kinds, %d rows in the index) and THE JOURNAL UNMOVED after it (the stamped digest equal — the sweep wrote nothing); THE REGISTER GATE --strict GREEN (DECLARED %d, DEBT %d, FAILS %d — the seat Deut 10:5 %s, the class the design predicted from 4:5\'s pair; 10:22 NONE with the compile\'s why); '
              'the positions table %d checkpoints over %d pauses (DB1-DB9 in it; checkpoint_probes %d/7 after the rebuild); the sweep %d/64 at %s graded cells (the 65 runners less the sequence file it skips; the moved runner and its importers); the home-path gate GREEN'
              % (DG[0], DG[1], DP[0], DP[1], LC[0], LC[1], LC[2], LC[3], DPR[0], DPR[1], DPR[2], JG[0], JG[1], RG[0], RG[1], RG[2], SEAT_10_5, PO[0], PO[1], PR['checkpoint'], SW_P, format(SW_CELLS, ',')))
docket_line = ('%d rows (link %d / topic %d; LAW %d, DERIVATION %d, DISPUTE %d, CONTEXT %d, OUTSIDE %d; credited %d; %s bytes), EVERY ROW READ WHOLE FROM THE START — no cut, no overlay (the parts\' WHOLE dicts empty, the correction counts zero and computed)'
               % (NROWS, NLINK, NTOPIC, VD['LAW'], VD['DERIVATION'], VD['DISPUTE'], VD['CONTEXT'], VD['OUTSIDE'], NCRED, format(DKB, ',')))
W8 = "THE DEUTERONOMY WALK sitting 8b"

# ---- 1. THE MAP — AS BUILT ----
AS_BUILT = """
## Sitting 8b — THE COMPILE OF CHAPTER 10 — AS BUILT (2026-09-20; the design above stands as written but for the departures below; RUN A the design on
## "Go", THE DOCKET its own run on "The docket go" in RUN A's window, RUN B on "Go" after the compaction — THE TWO-RUN RULE's third compile sitting, the docket clause applied)

THE RUN: cold_run_second_tablets.py the 65th runner — %d/%d on its FIRST graded run (six cells, %d asks — per cell %s; the CASES generated from the cells'
own asks and frozen under the honest-pairing guard, the guard's count from the generator's print); law_second_tablets the 70th daemon (given_at Deut 10:1,
installed_by boot); THE READBACK'S FORMS COMBINED, NO SEVENTH: TWENTY-FIVE rows VERBATIM 9 / VARIANT 10 / EXPANDED 3 / TURNED 1 / SUPPLIED 2 (the design's
"about thirty" — 10:2 two rows, God's word and the supplied clause; 10:6 three, the stations, the death, the burial; 10:10 two, the stretch and the
hearkening), ten found on the tape by kind and first verse, thirteen in the kin's cells by CALL; T2 SUPPLIED WITH A WRITE TWICE — THE FRAGMENTS IN THE ARK
(10:2 'and you shall put them in the ark', read of both sets by Menachot 99a:12 and Bava Batra 14b:6) written ONCE at the erection's day by the RETROGRADE marker
at Deut 10:2 (M['fragments_told'] = M['erected'], (2, 1, 1)) with the status fragments_in_the_ark on the ark (THE VALUE FROM THE DOCKET — the tablets and the
fragments; the scroll inside for R. Meir, beside for R. Yehuda), and AARON'S BURIAL (10:6 'and he was buried there', the Torah's one seat) written ONCE at his
death by the RETROGRADE marker at Deut 10:6 (M['burial_told'] = M['aaron_death'], (40, 5, 1)) with the status buried REUSED (the world's ninth — Sarah, Abraham,
Deborah, Rachel, Isaac, Jacob, the lusters, Miriam before him, read at the scan); T6 ONE stretch row — 10:10's third forty from the second ascent's marker at
Exod 34:4 (1, 5, 29) to THE TIMERS' FIRE at (1, 7, 10): 40 on the running world (DB4, Q25) and on the runner's bare world; THE SECOND ASCENT'S DATE MATCHES
SEDER OLAM RABBAH 6:2 (up the 29th of Av 'as at the first days', down the 10th of Tishri) — 7b's OPEN row on the clock CLOSED, its owed item (iii) PAID; T4 the
laws' form on 10:12-22 by CALL with THE CODE'S FOUR HOLES compiled at the chapter's own day (40, 11, 1) after the FORWARD marker at 10:12 — demand_declared
writing fear_of_heaven_asked (THE SHELF'S NAME, Berakhot 33b:23), heart_circumcision_commanded writing heart_circumcision_commanded (the evil inclination,
Sukkah 52a:7 — the grammar guard Shabbat 108a:7) and stiffening_barred (the chapter's one prohibition, no lashes), stranger_love_commanded writing love_owed
FOR THE FIRST TIME ON THE TAPE (Leviticus 19:34's effect, holiness_b's cell by CALL; a DEBIT by its registry op, the stranger the counterparty),
cleaving_commanded writing cleaving_commanded (the scholars, Ketubot 111b:7; the four clauses positive, Temurah 4a:2); the OPEN row (the place of the death
— Moserah / Mount Hor, the retreat of seven stations the parameter already on file at journeys and chukat) and the one hole outside the span (the go —
Exodus 32:34's and 33:1's speeches with no line) named; twenty-nine DATA rows (the docket's finds among them: the two arks of the Tosefta, the ark's contents'
two arms, the grammar guard, the inclination's name, the burial among the attributes, the positive form, the convert's intake, the editor's 'first of Tammuz'
variant, the face thrice reconciled, the six judges); twenty-four exam persons, three exempt (the judge who takes a fee for evident loss, the private convert,
the truthful swearer), NO LASHES (the one prohibition has no action). THE TAPE 10/10 ON ITS FOURTH RUN (the first 9/10 on DA1, two at import on the hole-ground scans, the third 9/10 on four literals) with RUN (1317, 96, 88, 0, 12, 1613, 41, 319, the
four pairs, 127) AS THE DESIGN'S ARITHMETIC WROTE IT, PREVIOUS_RUN 7b's exactly (no declared delta — a marker is not a line), CENSUS %s read at the
stitcher's print as predicted (on tape 1317, markers 172 — F 131, R 26 — kinds 862), markers 169 -> 172, closes 127, entities 319 unmoved, DB1-DB9 MATCH (%s s);
THE FIRST RUN 9/10 — ONE OLDER CHECKPOINT MOVED: 7b's own DA1 holds 'markers 169' in a tuple form the ten retypes did not cover ("[(40, 11, 1)], 169" — typed
at 7b after the nine older literals were retyped, so outside their patterns), retyped from the print; the stale literals ELEVEN where the design predicted
three (the six REST tuples, the three LINES tuples, CP6's count and F, DA1). THE TYPES: kinds 1135 -> 1142 (two ACTS, four STATUTES, second_tablets_case),
effects 1032 -> 1037 (four statuses and a block with the docket's names and values), daemons 69 -> 70 (I5 70), SEVENTEEN CALL edges and the registration —
the design's eighteenth (opening_speech) DROPPED AT THE CALLEES' PRINT: the opening-speech runner holds no cell on 1:10's 'as the stars of heaven for
multitude' (1:10's phrase a DATA row by the ink, 10:22's row on the Joseph runner alone). THE PROBES: readback_probes Q25-Q27 written to FAIL before the
types — 23/27 at the FAIL print (Q25-Q27 on the missing runner; Q23 on 'markers 172' before the tape, its literal retyped with the probe) — 27/27 after; Q25's
stretch resolver extended for a timer's fire. THE GATES (%s): %s; the thirteen probe suites — %s. THE DOCKET (its own run, 2026-09-20): %s.

THE DEPARTURES FROM THE DESIGN (twenty-two, each read from a print): (1) THE STRETCH'S END IS A TIMER'S FIRE, NOT A MARKER — the second ascent's line sets
tablets_delivered and face_radiant, fired at (1, 7, 10); no marker sits at 34:28: the runner's stretch names 'timer:tablets_delivered' and Q25's resolver
takes a marker's verse or a timer's fire (the design named the fire; the probe as first written assumed a marker); (2) THE PLACEMENT — the own-day line AT THE
FORWARD MARKER'S OWN VERSE (demand_declared at Deut 10:12) takes the marker's class: events text_constrained 109 -> 110, page_order 1146 -> 1149 where the
design wrote 1150 (the marker's-verse rule holds for a forward marker too — read at the stitcher's print); (3) the opening_speech edge dropped at the
callees' print (above) — the edge file follows the print before the runner is typed; (4) love_owed IS A DEBIT BY ITS REGISTRY OP — the runner's print
'LEDGER OPS: debit x1': the open debits on Israel 8 -> 9 (DB7 retyped from OPEN-UNMOVED to 9), a standing duty toward the stranger with no closer; closes
unmoved; (5) DA1 the eleventh stale literal (above); (6) the clock's hor_to_death 29 — Tammuz twenty-nine days that year (one part-1 assert fell on the fast
checker's first pass, retyped from the print); (7) the rows twenty-five at 9/10/3/1/2 (the design's "about thirty"); (8) the exam's persons twenty-four,
three exempt (the design did not number them); (9) the stitcher's mk code carried placement='reading_placed' where with_placement() adds it — 7b's lesson 11
repeated once ('keyword argument repeated' at the prediction step), removed; (10) the fragments' line source 'Deut 10:2-5' — the receipt's verse carried
inside the line's own source so the register gate's finder reads the write at 10:5 (the ACT class %s at the gate); (11) the derive-by-content form for part 1 —
the reading's own ink instrument (ch10_ink_body.py) copied by content markers into the runner's INK block, 71 asserts, the store's four and the verse-count
table dropped (the runner reads the DB alone), the sequence module's names made the exec'd parser's; (12) 'not_righteousness' absent from the stitcher's
SPAN_ORDER (7b never joined it) — second_tablets not joined either, the CENSUS tuple unaffected (the per-runner table the print's own); (13) the register's
10:22 why retyped at the types (the cell by CALL, no row — Exodus 1:5's form); (14) the FAIL print 23/27, not a refusal (the probes ran before the types this
time — 7b's lesson 2 held); (15) the stitcher's docstring '169 markers, 1311 history events' regenerated by the stitcher itself (not a retype — the design
listed it among the three); (16) AN OLDER RUNNER'S HOLE-GROUND SCAN BROKEN BY THIS SITTING'S WRITE — the tape's second attempt fell at IMPORT: the chapter-9
runner scans the one database for stiff / neck on Israel and asserts it empty (7b's decision 2, the stiff neck a STATE), and the tape's first run had sealed
stiffening_barred (the COMMAND, its value naming the neck) into the fold — the older runner's scan and DA6 now exclude the later sitting's effect (the
peril's form, patch_nr_scan_ch10.py); (17) the runner's own LAW_SCAN missed its fifth effect — the third attempt fell at import on love_owed (its value
names the bribe declaration); excluded with the four; (18) THE TAPE'S THIRD RUN 9/10 WITH FOUR DIFFS, each retyped from the print: CA1 — chapter 1b's
LINES checkpoint LISTS the Deuteronomy markers (7b's lesson 3 a second time: the two retrograde markers at 10:2 and 10:6 join the list, the forward markers
six); DB1 — the placements set holds text_constrained (the own-day line at the forward marker's verse — the checkpoint had the design's two classes though
the stitcher's print had said three); DB4 — the stretch's end is the first fire of tablets_delivered AT OR AFTER the marker (the log's first fire of that
effect is the first tablets' delivery at the breaking, -41 read; Q25's resolver takes the same rule); DB7 — circumcision_due 22 on the running world (the
design's 24 the one database's count, which folds the scene worlds' two); (19) the tape ran FOUR times to 10/10 — the first 9/10 (DA1), two at import (the
scans), the third 9/10 (the four), the fourth 10/10; (20) THREE OLDER READBACK PROBES held the marker count (Q14, Q17, Q20 — 7b's lesson 12 repeated: the design's
list named Q23 alone), retyped from the chain's first print; (21) THE CACHE'S NINETEENTH SLIP — its own error report: a worker of the positions table raised on the
cached path and the report crashed on a shadowed name (the source text `src` rebound to a module), masking the real error; renamed, a single worker rerun
clean, the table by four workers; (22) %s.

THE LESSONS (twelve, for the next compile): (1) A STRETCH MAY END AT A TIMER'S FIRE — the clock's spans run between markers OR fires; a probe's resolver
takes both; (2) the marker's-verse rule holds for a FORWARD marker too — the placement is read, never predicted page_order (7b's lesson 4 a second time, the
other class); (3) A REUSED EFFECT BRINGS ITS REGISTRY OP — love_owed a debit: the open-debit counts move as a status count would (6b's lesson on a reused
status, now on a reused debit); read the runner's LEDGER OPS line before the checkpoints are typed; (4) THE NEWEST SITTING'S OWN CHECKPOINTS JOIN THE
STALE-LITERAL LIST — 7b's DA1 typed its marker count after the nine older ones were retyped: before the tape, grep every LINES and REST tuple for the old count,
not the older sittings' forms alone; (5) the callees' print drops an edge before it is typed — a design's CALL is a prediction the callee's source decides
(6b's lesson a second time); (6) the T2 form twice in one chapter is two retrograde markers, two dated lines and no clock walk — the counter unmoved, the
forward marker at the pivot; (7) THE FORMS COMBINE — a chapter that is a retelling's tail and a laws' head takes T1, T2, T6 and T4 together, no seventh form:
the readback has six forms and they compose; (8) the reading's ink instrument is the runner's INK block by content markers — no assert retyped twice; (9) THE
FOLD CARRIES EVERY SITTING'S WRITES INTO THE ONE DATABASE — an older runner's hole-ground scan on the same words is broken by a later sitting's write, and
the runner's own scans by its own: every such scan names the later effects it excludes (the ground stands as of its sitting; the tape's first run seals the
writes, the second attempt reads them); (10) the first fire of an effect may lie BEFORE a stretch — a stretch's end is the fire at or after its start (DB4,
Q25), as the markers' list literal moves with every marker (CA1, 7b's lesson 3 again); (11) THE CACHE'S ERROR REPORT IS PART OF THE CACHE — a masked message cost a chain pass; the report's own names checked when the cache is touched; and the eight-worker positions step fails two sittings running (the watchdog at 7b, a cached-path raise here): FOUR WORKERS the step's standing form until the eight are measured; (12) THE
TWO-RUN RULE HELD ON ITS THIRD COMPILE SITTING — RUN A the design (a clean point), the docket its own run in the same window on the owner's word (a clean
point), RUN B this (the probes, the types, the callees, the runner in parts with the fast checker, the cases, the recorder with the cache off, the stitcher
twice, the literals, the tape twice, the checkpoint check, the chain, the records in one call) — the D series' second name DB1-DB9.
""" % (CASES_N, CASES_N, CASES_N, PER_CELL, CENSUS, tape_elapsed, CHAIN_SHORT, gates_line, pr_line, docket_line, SEAT_10_5, CHAIN_STORY)

# ---- 2. COMPILE_DEBT — the sitting-8 box marked PAID + the 8b box ----
DEBT_HDR_OLD = "## SITTING 8 — CHAPTER 10 (2026-09-20, the reading; deu_10_second_tablets frozen) — OWED TO THE COMPILE 8b: (a) THE FRAGMENTS IN THE ARK"
DEBT_HDR_NEW = "## SITTING 8 — CHAPTER 10 (2026-09-20, the reading; deu_10_second_tablets frozen) — PAID AT 8b (the 8b box below, item by item) — AS WRITTEN AT THE READING, OWED TO THE COMPILE 8b: (a) THE FRAGMENTS IN THE ARK"
DEBT_BOX = """
## DEUTERONOMY SITTING 8b — THE COMPILE OF CHAPTER 10 (2026-09-20; DEUTERONOMY_WALK.md "Sitting 8b" design + THE DOCKET — AS RUN + AS BUILT; logic/oral_triage/deu_10_ekev_exam_2026-09-20.md
## %d rows, every row read whole from the start; cold_run_second_tablets.py %d/%d; law_second_tablets the 70th daemon; the tape 10/10 with RUN (1317, 96, 88, 0, 12, 1613, 41, 319, pairs, 127)).
## THE SITTING-8 BOX (a)-(n) PAID — (a) THE FRAGMENTS IN THE ARK — F1: the T2 row SUPPLIED WITH A WRITE, the retrograde line fragments_placed_in_the_ark at the erection's day (2, 1, 1),
## the status fragments_in_the_ark on the ark with the docket's value (the tablets and the fragments; the scroll inside or beside); 7b's owed item (i) PAID; (b) THE ARK ONE — F1 the_ark_is_one:
## the Bavli's "the ark that Moses fashioned" (Bava Batra 14a:8) against the Tosefta's two (Sotah 7:9 — a DISPUTE row); the registry's homograph (one id for tevah and aron) a DATA row, the
## split owed to a gate sitting; (c) THE STATIONS AND AARON'S BURIAL — F2: the stations reversed VARIANT by CALL (journeys.the_stations('moseroth_seven')); the burial SUPPLIED WITH A WRITE
## at his death (40, 5, 1), buried REUSED (the ninth); THE PLACE OPEN (Moserah / Mount Hor — the retreat of seven stations the parameter already on file, no marker); (d) "AT THAT TIME"
## THE LEVITES — F3: the tape's own (1, 4, 17), the three offices by CALL (bamidbar, beha, korach, naso), 10:9 portion_declared by kind; "which time" asked by no row (a DATA row); the receipt
## "spoke to him" the finder's third form (4b's owed item stands); (e) THE THIRD FORTY — F4: the stretch row from the marker at 34:4 to the timers' fire = 40 (DB4); THE SECOND ASCENT'S
## DATE MATCH — Seder Olam Rabbah 6:2 (7b's owed item (iii) PAID; the "first of Elul" not this shelf's text); (f) THE GO — F4: VARIANT, the hole named OUTSIDE the span (Exodus 32:34,
## 33:1-3 — an Exodus 33 sitting's; 7b's (vii) form); the charge to Joshua a DATA row; (g) THE DEMAND (10:12-13) — F5: the line demand_declared writing fear_of_heaven_asked (Berakhot 33b:23 —
## 6b's and 7b's owed item 10:12 PAID); the five infinitives by CALL (hear_o_israel, good_land), "with all your might" dropped a DATA row; (h) THE HEART AND THE NECK (10:16) — F5: the line
## heart_circumcision_commanded writing the status (the evil inclination — Sukkah 52a:7) and the block stiffening_barred (the chapter's one prohibition; no lashes); the grammar guard
## (Shabbat 108a:7) a DATA row; (i) THE STRANGER'S LOVE (10:19) — F6: the line stranger_love_commanded writing love_owed FOR THE FIRST TIME (Leviticus 19:34's cell by CALL; a DEBIT by its
## registry op, the stranger the counterparty); 10:17-18's attributes, face and bribe declarations by CALL, no write; (j) THE CLEAVING (10:20-22) — F6: the line cleaving_commanded writing
## the status (the scholars — Ketubot 111b:7); the four clauses positive (Temurah 4a:2); 10:22's seventy by CALL (joseph), the register seat NONE with the compile's why; (k) 10:4's "the
## ten words" and 10:10's forty citing 9:9-11 by CALL (7b's owed item (iv) PAID); (l) THE READBACK'S FORMS COMBINED, NO SEVENTH — twenty-five rows; (m) THE CHECKPOINTS DB1-DB9 (the D
## series' second name); (n) THE DOCKET — %d rows by the union rule, EVERY ROW WHOLE FROM THE START (its own run in RUN A's window). OWED FROM 8b: (i) THE REGISTRY'S HOMOGRAPH — one id
## the_ark for the flood's tevah and the sanctuary's aron (rested_on_ararat beside ark_spec): a split owed to a gate sitting ON THE OWNER'S WORD; (ii) THE RECEIPT FINDER'S THIRD FORM
## ("as the LORD your God SPOKE to him", 10:9; 4b's owed item) — a gate sitting's; (iii) THE CALF'S OWN DAY — the marker at the sixteenth of Tammuz (Shabbat 89a:6) ON THE OWNER'S WORD
## (7b's (ii), unchanged); (iv) THE EXODUS 33 HOLES — the go (32:34, 33:1-3), the crowns (33:1-6) and the three requests (33:12-23) with no line: an Exodus 33 sitting's, if ever (7b's
## (vii), the go joined); (v) love_owed's OPEN DEBIT on Israel toward the stranger — a standing duty with no closer on the tape (Leviticus 19:34's form): its closer, if any, a later
## sitting's question (the register's open debits 8 -> 9); (vi) 30:6's "the LORD your God will circumcise your heart" (the passive forward — chapter 30's compile cites 10:16 by CALL);
## 31:26's "beside the ark" (R. Yehuda's arm the ink's own — chapter 31's); 16:19's bribe command (chapter 16's — Exodus 23:8's block written at last there?); 28:62's "as the stars"
## (chapter 28's); 13:5's "walk after Him" (chapter 13's — Sotah 14a's attributes); (vii) THE OWNER'S WORD ON THE SUPPLIED FORMS — the fifth's (no write) and the sixth's (with a write,
## twice here) stand as the designs', the retelling rules' own; ON THE TABLE. NOTHING ELSE IN CHAPTER 10 IS OWED TO A LATER SITTING OF ITS OWN.
""" % (NROWS, CASES_N, CASES_N, NROWS)

# ---- 3. MIDDOT — the compile's entry (the docket's entry stands from its own run; this the runner's use of the codes — every code checked in this file's own lists) ----
MIDDOT_ANCHOR = "\n## Exodus block campaign — owner's word \"Do 3\")\n"
MIDDOT_ENTRY = """- THE CHAPTER-10 COMPILE (THE DEUTERONOMY WALK sitting 8b RUN B, 2026-09-20; cold_run_second_tablets.py — the docket's rules carried into the cells' asks, each
  code checked in this file's lists before it was typed):
  · THE A-FORTIORI (I1, qal wa-chomer) at Ketubot 105a:16 (F6 takes_no_bribe: the bribe blinds the eyes of the WISE — how much more the foolish); R. Yishmael bar R.
    Yosei's own at 105b:12 (F6 the_bribe_of_words: "if I who did not take feel so, how much more those who take" — the judge's reasoning on himself).
  · THE VERBAL ANALOGY (I2, gezerah shavah) at three seats — Shabbat 108a:7 (F5 the_grammar_guard: foreskin / foreskin between Leviticus 12:3 and 19:23 takes the COMPLETE
    form orlato / orlato and REFUSES 10:16's construct orlat — the analogy's own grammar guard: the heart's foreskin is not the circumcision law's object); Shevuot 35b:23
    (F6 swear_by_his_name: ala / ala — the oath by the appellations liable as by the Name); Menachot 43b:9 (credited — chapter 6's, the tzitzit's).
  · THE ET-EXTENSION (E1, ribui) at Pesachim 22b:11 (F6 the_et_of_10_20: Shimon HaAmmassoni's retraction at "you shall fear [et] the LORD your God" and R. Akiva's "to
    include Torah scholars" — the fear's object extended as the cleaving's value) and Bava Batra 123a:21 (F6 seventy_persons: "with" extends — Dinah's twin refuted, Jochebed
    the seventieth).
  · RESTRICTION AFTER RESTRICTION, WHICH EXTENDS (E4) at Bava Batra 14a:10 (F1 the_fragments_in_the_ark: 1 Kings 8:9's "nothing in the ark EXCEPT the two tablets" — the
    fragments' third derivation, R. Yehuda's).
  · THE PARABLE (E26, mashal) at Berakhot 33b:25 (F5 a_small_thing: the large vessel that seems small to him who has it — the fear of Heaven a small thing for Moses) and
    Berakhot 33b:22 / Megillah 25a:8 (F6 the_attributes_three: the king with a thousand thousand gold dinars praised for silver — the one who adds praises).
  · NOTARIKON (E30) at Ketubot 105b:5 (F6 the_bribe_of_words: shochad = she-hu chad, "he is one" with the giver).
  · THE "DO NOT READ" READINGS NAMED, NO CODE — Menachot 43b:15 (F5 a_hundred_blessings: ma read me'a); Ta'anit 9a:11 (F2 arad_heard: "saw" read "were seen" — the clouds
    departed); Rosh Hashanah 3a:2 (the same row's juxtaposition of Arad's hearing to Aaron's death).
  · THE JUXTAPOSITIONS NAMED, NO CODE — Sotah 38a:8 (F3 to_bless_in_his_name: 18:5's "to stand to minister" through 10:8 to Leviticus 9:22's lifted hands); Megillah 31a:13
    (10:17-18's greatness beside the humility — credited).
  · THE POSITIVE FORM RULE (a form rule on the code's own imperfects — Temurah 4a:2; Sanhedrin 56a:11): "you shall fear the LORD your God" A WARNING STATED AS A POSITIVE
    COMMAND — 10:20's four clauses positive, the write a STATUS not a BLOCK, no lashes (F6 fear_serve_cleave_swear); the chapter's ONE prohibition 10:16's neck (F5
    stiffen_no_more) a BLOCK without lashes (Makkot 13b:6's form — a prohibition without an action).
  · THE CLOCK READ BACK AGAINST THE SHELF'S OWN DATE (no middah — the machine's own): Seder Olam Rabbah 6:2's twenty-ninth of Av IS the calendar's subtraction from 10 Tishri
    (CAL_PARAMS second_tablets_given): the third forty measured on the running world between the second ascent's marker and the timers' fire — MATCH (DB4); 7b's OPEN row
    on the clock was the reader's error ("the tradition's first of Elul" not this shelf's text), closed by the row read whole (F4 the_second_ascents_date).
  · A DISPUTE'S TWO ARMS AS A PARAMETER'S SECOND ARM (Tosefta Sotah 7:9 against Bava Batra 14a:8 — F1 the_ark_is_one): two arks (the war ark with the scroll, the camp ark
    with the fragments) against one ("that Moses fashioned" with 25:10's cubits): the tape's one id the Bavli's reading, the Tosefta's arm recorded; and WHAT ELSE THE
    ARK HELD (14a:12-14b:1 — R. Meir's cubit six with the scroll inside, R. Yehuda's cubit five with the scroll beside): the effect's value's second parameter.
  · THE REASON CLAUSE'S RULE (Bava Metzia 59b:15 — F6 the_thirty_six_warnings): R. Natan on "for you were strangers in the land of Egypt" — a defect in you, do not
    mention in another: the four seats' reason clause read as a rule about speech.
  · THE FEAR OF HEAVEN THE ONE FREE VARIABLE (Berakhot 33b:23; Megillah 25a:9; Niddah 16b:13 — F5 the_fear_of_heaven): a principle stated FROM the verse's question form
    ("what … but to fear") — the effect fear_of_heaven_asked NAMED by the row's own words.
""" % ()

# ---- 4. MISHNAH_TOPICS — the rows touched by the compile (the docket's own notes stand on three rows from its run) ----
DKF = "deu_10_ekev_exam_2026-09-20.md"
TOPIC_NOTES = {
 "**12. Mishnah, Sabbath**": " — Shabbat 108a:7 and 31b:1-3 READ WHOLE 2026-09-20 (%s: the verbal analogy foreskin / foreskin refuses 10:16's construct — the heart's foreskin not the circumcision law's object; the fear of sin the storehouse's key; F5's grammar guard — %s)" % (W8, DKF),
 "**14. Mishnah, Passover**": " — Pesachim 22b:11 and 104a:10 READ 2026-09-20 (%s: Shimon HaAmmassoni's retraction at 10:20's 'et' and R. Akiva's scholars, E1; the three distinctions — priests, Levites, Israelites, 10:8)" % W8,
 "**16. Mishnah, Day of Atonement**": " — Yoma 3b:3, 72b:8, 69b:13-16 READ WHOLE 2026-09-20 (%s: 'make you an ark' against 'they shall make' — Moses commanded, Bezalel's hands, 10:1-3; the great assembly restoring Moses' three attributes, 10:17; 52b the ark hidden with the jar, the oil and the staff — credited)" % W8,
 "**17. Mishnah, Booth**": " — Sukkah 52a:7 READ WHOLE 2026-09-20 (%s: the evil inclination's seven names — 'foreskin' Moses' name for it from 10:16: the effect heart_circumcision_commanded's VALUE)" % W8,
 "**19. Mishnah, New Year**": " — Rosh Hashanah 3a:1-13 and 17b:17 READ WHOLE 2026-09-20 (%s: Arad heard that Aaron died — the clouds departed, 10:6; the era's chain; Beloria's question on 'lifts no face' against the priestly blessing, 10:17)" % W8,
 "**20. Mishnah, Fasts**": " — Ta'anit 9a:9-12 and 26b:17 READ WHOLE 2026-09-20 (%s: the three gifts by three shepherds — the cloud by Aaron's merit, 10:6, 'saw' read 'were seen' named; the blessing's four times, 10:8)" % W8,
 "**21. Mishnah, Scroll of Esther**": " — Megillah 25a:7-10, 31a:13 and 21a:17 READ WHOLE 2026-09-20 (%s: the one who adds praises silenced and 'everything but the fear of Heaven', 10:12, 10:17; the greatness beside the humility juxtaposed, 10:17-18; 'I sat' against 'I stood', 10:10)" % W8,
 "**24. Mishnah, Levirate Marriage**": " — Yevamot 47a:1-47b:19 READ WHOLE (thirty-four rows) 2026-09-20 (%s: THE CONVERT'S INTAKE — 'what did you see that you come?', the light and the grave commandments, circumcised and immersed an Israelite in all respects; the private convert not believed; the slave and the captive — the stranger line's exam, 10:19: F6's persons the convert at the intake (accepted) and the private convert (exempt))" % W8,
 "**25. Mishnah, Marriage Contracts**": " — Ketubot 105a:10-105b:15 and 111b:6-8 READ WHOLE (fifty-six rows) 2026-09-20 (%s: THE BRIBE — even to judge truly, a salary voids, evident loss permitted, THE BRIBE OF WORDS (Shmuel's hand, Ameimar's feather, Mar Ukva's spittle, R. Yishmael's sharecropper, R. Yishmael bar Elisha's shearing, Rav Anan's fish — the six judges F6's persons), shochad = she-hu chad (E30), the bribe blinds a fortiori (I1), 10:17; THE CLEAVING = the scholars — marry a daughter, trade, benefit: cleaving_commanded's VALUE, 10:20)" % W8,
 "**30. Mishnah, Betrothal**": " — Kiddushin 58b READ 2026-09-20 (%s: one who takes a fee to judge — his judgments void (Mishnah Bekhorot 4:6 there): F6's person the judge who takes a salary, 10:17)" % W8,
 "**32. Mishnah, Middle Gate**": " — Bava Metzia 59b:13-15 READ WHOLE 2026-09-20 (%s: the stranger's wronging three prohibitions, the thirty-six / forty-six warnings, R. Natan's 'a defect in you, do not mention in another' on 'for you were strangers' — the reason clause's rule at 10:19; F6's person the one who wrongs the stranger with words)" % W8,
 "**33. Mishnah, Last Gate**": " — Bava Batra 14a:8-14b:7 and 123a:21-123b:1 READ WHOLE 2026-09-20 (%s: THE ARK ONE 'that Moses fashioned' with 25:10's cubits; the fragments' three derivations (10:2's 'them', 2 Samuel 6:2's doubled Name, 1 Kings 8:9's double restriction E4); WHAT ELSE THE ARK HELD — R. Meir's scroll inside, R. Yehuda's beside: fragments_in_the_ark's VALUE; Jochebed the seventieth and Dinah's twin refuted (E1), 10:22)" % W8,
 "**34. Mishnah, Courts**": " — Sanhedrin 56a:11 READ 2026-09-20 (%s: the blasphemer's warning from 'you shall fear the LORD your God' — the positive form rule's second seat, 10:20)" % W8,
 "**35. Mishnah, Lashes**": " — Makkot 13b:6 credited 2026-09-20 (%s: a prohibition without an action is not flogged — 10:16's 'you shall not stiffen', the chapter's one prohibition; F5's person the stiffener)" % W8,
 "**36. Mishnah, Oaths**": " — Shevuot 35b:22-23 READ WHOLE 2026-09-20 (%s: the oath by the appellations liable; ala / ala the analogy (I2), 10:20; F6's person the swearer by the appellations)" % W8,
 "**40. Mishnah, Erroneous Rulings**": " — Horayot 13a:18 READ 2026-09-20 (%s: a priest precedes a Levite — 1 Chronicles 23:13's 'separated' beside 10:8; a row citing 10:8 that asks nothing of the time)" % W8,
 "**41. Mishnah, Animal Offerings**": " — Zevachim 16a:13 READ 2026-09-20 (%s: sitting invalidates — 'to stand before the LORD', 10:8)" % W8,
 "**42. Mishnah, Grain Offerings**": " — Menachot 28b:2 READ and 99a-99b, 43b:15 credited 2026-09-20 (%s: 'make for yourself' against the future generations' vessels, 10:1; the fragments in the ark PAID at this compile (7b's owed item); a hundred blessings from 'what' — the do-not-read reading named, 10:12)" % W8,
 "**45. Mishnah, Valuations**": " — Arakhin 11a:10 READ 2026-09-20 (%s: the Levites' song the service — the blessing beside it, not itself 'service', 10:8)" % W8,
 "**46. Mishnah, Substitution**": " — Temurah 3b:17-4a:2 READ WHOLE 2026-09-20 (%s: Rav Giddel's 'by His name you shall swear' a positive command — a truthful oath permitted (F6's person the truthful swearer, exempt); 'you shall fear the LORD your God' a warning stated as a positive command — THE POSITIVE FORM RULE: 10:20's four clauses STATUS, no lashes)" % W8,
 "**58. Mishnah, Family Purity**": " — Niddah 16b:13 and 70b:5 READ 2026-09-20 (%s: everything in the hands of Heaven except the fear of Heaven — the angel over conception, 10:12; the sages of Alexandria's before / after the sentence on 'lifts no face', 10:17)" % W8,
}

# ---- 5. RESEARCH_LOG ----
RLOG = """

## 2026-09-20 — DEUTERONOMY 10 COMPILED (THE DEUTERONOMY WALK sitting 8b — CHAPTER 10): THE READBACK'S FORMS COMBINED, NO SEVENTH; TWO ACTS TOLD ONLY IN THE
## RETELLING WRITTEN ONCE AT THEIR OWN DAYS; THE SECOND ASCENT'S DATE MATCHES SEDER OLAM'S; THE CODE'S FOUR HOLES COMPILED AT THE CHAPTER'S OWN DAY

THE FORMS COMBINED. Chapter 10 is the retelling's tail (10:1-11) and the laws' head (10:12-22), so its rows took the forms already on file and no seventh:
twenty-five rows, VERBATIM 9 / VARIANT 10 / EXPANDED 3 / TURNED 1 / SUPPLIED 2 — ten on the tape by kind and first verse (the second ascent's line at 34:2, the
ark's making at 37:1, the testimony placed at 40:20, Aaron's death at Numbers 20:28, the Levites gathered at Exodus 32:26, the portion declared at Numbers
18:20, the intercession, the oath), thirteen in the kin's cells by CALL. TWO ACTS ARE TOLD ONLY HERE: "and you shall put THEM in the ark" (10:2 — the two
tokens Exodus 34:1 never gives; the shelf reads 'them' of both sets, the whole tablets and the fragments: Rav Yosef's baraita at Bava Batra 14b:6 and Menachot
99a:12, Rav Huna's doubled Name from 2 Samuel 6:2, R. Yehuda's double restriction from 1 Kings 8:9) and "and he was buried there" (10:6 — the Torah's one
seat; Numbers tells the death, the mourning, the date and the age, never the burial). Each was written ONCE at its own day by a retrograde marker: the
fragments at the erection's day (2, 1, 1), the day Exodus 40:20 placed the tablets, with a status on the ark whose VALUE the docket supplied (the tablets and
the fragments; the scroll inside for R. Meir, beside for R. Yehuda — the cubit six or five); the burial at Aaron's death (40, 5, 1), the status buried REUSED
— Aaron the world's ninth buried, Sarah to Miriam before him. THE PLACE IS OPEN: Moserah in the retelling, Mount Hor on the tape — and the shelf's
reconciliation (Seder Olam Rabbah 9:2's retreat of seven stations) was already a parameter of the Numbers compile, found on file at journeys and chukat; no
marker for the retreat, the disagreement inside the burial line's own field. THE THIRD FORTY (10:10) is a stretch on the clock from the second ascent's marker
at Exodus 34:4 (1, 5, 29) to THE TIMERS' FIRE at (1, 7, 10) — forty on the running world, and its end is a fire, not a marker: the probe's resolver takes both.
And THE SECOND ASCENT'S DATE MATCHES THE SHELF: Seder Olam Rabbah 6:2, read whole under the export's empty key, says up on the twenty-ninth of Av and down
on the tenth of Tishri — the machine's (1, 5, 29) by subtraction from 10 Tishri is the shelf's own date; 7b's OPEN row ("the tradition's first of Elul") was
the reader's error and is closed. THE LAWS' HEAD: 10:12-22 graded by CALL against the cells that compile them (the creed, 6:13, 8:6, 4:1, 4:39, 4:37, 7:7, 7:9,
Numbers 6:26, Exodus 23:8, 22:21, Leviticus 19:34, 6:13 again, 7:19, Genesis 46:27) — and FOUR HOLES IN THE CODE compiled at the chapter's own day (40, 11, 1)
after a forward marker at 10:12: the demand (fear_of_heaven_asked — the tradition's own name for 10:12, "everything is in the hands of Heaven except the fear
of Heaven", Berakhot 33b:23), the heart and the neck (heart_circumcision_commanded — its value the evil inclination, Moses' name for it "foreskin" from this
verse, Sukkah 52a:7; guarded by grammar at Shabbat 108a:7, where the verbal analogy takes the complete form and refuses the construct; stiffening_barred the
chapter's one prohibition, a block with no lashes), the stranger's love (love_owed — Leviticus 19:34's effect in the vocabulary since the holiness compile
and NEVER WRITTEN ON THE TAPE until this line; a debit by its registry op, the stranger the counterparty; R. Natan's rule on the reason clause, the convert's
intake as the exam), the cleaving (cleaving_commanded — its value the scholars, Ketubot 111b:7; the four clauses of 10:20 positive by Temurah 4a:2, a status
not a block). THE MACHINE'S LESSONS: a stretch may end at a timer's fire; the line at a FORWARD marker's own verse takes the marker's class too (the
placement read at the stitcher's print — text_constrained 110, page_order 1149); a reused effect brings its registry op (a debit moves the open-debit counts);
the newest sitting's own checkpoints join the stale-literal list (7b's DA1 held 'markers 169' in a form the ten retypes missed — the tape 9/10 on its first
run, 10/10 on its second); the callees' print drops a design's edge before it is typed (no cell on 1:10's stars — seventeen CALL edges, not eighteen). THE
NUMBERS: cold_run_second_tablets.py the 65th runner %d/%d on its first graded run; the tape 10/10 on its second (the first 9/10, DA1); RUN (1317, 96, 88, 0, 12,
1613, 41, 319, the four pairs, 127) as predicted; markers 169 -> 172; kinds 1142, effects 1037, daemons 70, seventeen CALL edges; the docket %s; every gate green
(%s; the sweep %d/64). THE TWO-RUN RULE'S THIRD COMPILE SITTING: RUN A the design, the docket its own run in the same window on the owner's word, RUN B the
build after one compaction — three clean points.
""" % (CASES_N, CASES_N, docket_line, CHAIN_SHORT, SW_P)

# ---- 6. THE_STEPS ----
STEPS_ANCHOR = "\n## Step 6 — Publish\n"
STEPS_PARA = """
DEUTERONOMY — SITTING 8b — CHAPTER 10 COMPILED (2026-09-20, on Brian's "Go" for the design, "The docket go" for the docket and "Go" for the build after a
compaction; World/step9/DEUTERONOMY_WALK.md "Sitting 8b", "THE DOCKET — AS RUN" and "Sitting 8b — AS BUILT"). Chapter 10 finishes Moses' retelling of the calf
and begins his restatement of the law, so the sitting used the grading forms it already had and needed no new one: each sentence of the retelling against the
tape's own line or the older cell, and each restated law against the cell that compiles it. Two things in the chapter are told nowhere else. "Put them in the
ark" — the sages read "them" as both sets, the whole tablets and the broken ones — and "he was buried there" of Aaron, which Numbers never says. Each was
written once into its own day: the fragments on the day the tabernacle was raised and the tablets placed, the burial on the day Aaron died; the entry for the
fragments took its value from the Talmud's argument over what else the ark held (a Torah scroll inside it or beside it, depending on the size of a cubit), and
the entry for the burial reused the one the machine already had for Sarah and the others, Aaron the ninth. Where the chapter puts Aaron's death (Moserah) and
where Numbers puts it (Mount Hor) disagree, and that disagreement stays open inside the line — the sages' answer, a retreat of seven stations, was already a
parameter the machine had from the Numbers compile. The third forty days on the mountain measured forty on the calendar from the second ascent to the day
the tablets came down, and this time the shelf's own chronology, read in full, gave the same date for the ascent as the machine's subtraction — the earlier
open question on that date was a misreading and is closed. Four laws in the chapter had no code anywhere: what the LORD asks of you (the sages' "everything
is in the hands of Heaven except the fear of Heaven" is their name for this verse), circumcise your heart and stiffen your neck no more (the Talmud names the
evil inclination "foreskin" from this verse, and its grammar refuses to let the heart's foreskin fall under the law of circumcision), love the stranger (the
older law's effect had been in the vocabulary since Leviticus and never once written on the tape), and cleave to Him (the scholars, the sages say; and all
four clauses of that verse are positive commands, so the entry is a status, not a prohibition). The runner matched its sheet on the first run; the tape
reached ten of ten on the fourth — one of last sitting's own checks held the old marker count, two older scans of the machine's own database found this sitting's fresh entries and had to be told to look past them, and the book's list of date marks grew by two; %s. Next: the commit on your word; then chapter 11.
""" % (CHAIN_SHORT,)

# ---- 7. THE_BRIEFING ----
BRIEF_BULLET_ANCHOR = "- **CHAPTER 10 READ AND FROZEN — THE ARK PUT INTO GOD'S QUOTED WORD:"
BRIEF_BULLET = ("- **CHAPTER 10 COMPILED — THE FORMS COMBINE: TWO ACTS TOLD ONLY IN THE RETELLING (THE FRAGMENTS IN THE ARK, AARON'S BURIAL) WRITTEN ONCE INTO THEIR OWN DAYS; THE SHELF'S OWN CHRONOLOGY GIVES THE MACHINE'S DATE FOR THE SECOND ASCENT; FOUR LAWS WITH NO CODE COMPILED, THE STRANGER'S LOVE WRITTEN ON THE TAPE FOR THE FIRST TIME** "
                "(2026-09-20, on your \"Go\", \"The docket go\" and \"Go\"; World/step9/DEUTERONOMY_WALK.md \"Sitting 8b\" + THE DOCKET — AS RUN + AS BUILT): cold_run_second_tablets.py the 65th runner (%d/%d), law_second_tablets the 70th daemon (%d functions); the readback twenty-five rows in the forms combined — two SUPPLIED with a write, one stretch, the laws by CALL; the tape 10/10 with RUN (1317, 96, 88, 0, 12, 1613, 41, 319, pairs, 127) as predicted, markers 172; the docket %d rows every row whole; every gate green (%s), the sweep %d/64; the two-run rule's third compile sitting, three clean points.\n" % (CASES_N, CASES_N, DG[1], NROWS, CHAIN_SHORT, SW_P))
BRIEF_ENTRY_ANCHOR = "### 2026-09-20 — CHAPTER 10 READ: THE ARK ADDED TO GOD'S WORD"
BRIEF_ENTRY = """### 2026-09-20 — CHAPTER 10 COMPILED: TWO ACTS WRITTEN INTO THE PAST, A DATE THE SHELF CONFIRMS, AND FOUR LAWS THAT HAD NO CODE

Chapter 10 is the tail of one thing and the head of another — the last of Moses' retelling of the calf, then the first of his restatement of the law — so the
machine graded it with the forms it already had and needed no new one. The retelling gave it two acts told nowhere else. "Put them in the ark": the sages read
"them" as both sets, the whole tablets and the broken ones, and the tape had never recorded the fragments anywhere. "And he was buried there" of Aaron: Numbers
gives his death, the thirty days of mourning, the date and the age, and never the burial. Each act was written once into its own day — the fragments on the day
the tabernacle was raised and the tablets placed, the burial on the day Aaron died — and the entries took their content from the shelf: the ark held the
tablets and the fragments, with a Torah scroll inside it or beside it depending on whether a cubit is six handbreadths or five; Aaron was the ninth person the
world had buried. Where he died is left open inside the line, Moserah against Mount Hor, because the sages' reconciliation — the people retreated seven
stations and mourned him there — was already a parameter the machine held from Numbers. The third forty days measured forty on the calendar, from the mark at
the second ascent to the day the tablets came down, which is a timer's firing rather than a mark; and the shelf's own chronology, read in full this time,
puts the ascent on the twenty-ninth of Av, exactly the machine's date — the earlier worry that tradition said the first of Elul was a misreading, now closed.
Then the law. Four commands in the chapter had no code in any runner. "What does the LORD your God ask of you but to fear" — the sages' "everything is in the
hands of Heaven except the fear of Heaven" is their name for this verse, and it became the entry's name. "Circumcise the foreskin of your heart, and stiffen
your neck no more" — the Talmud names the evil inclination "foreskin" from this verse, and its grammar refuses to let the heart's foreskin fall under the law
of circumcision, so the entry is new and the neck's clause is the chapter's one prohibition, a block that carries no lashes because it has no act. "Love the
stranger" — Leviticus's own effect for that love had been in the vocabulary since the holiness chapters and had never once been written on the tape; it was
written here, a standing debt toward the stranger with no closer. "Cleave to Him" — the scholars, the sages say; and since every clause of that verse is a
positive command, the entry is a status, not a bar. The runner matched its sheet on the first run; the tape reached ten of ten on the second, one of last
sitting's own checks having held the old marker count; %s. Next, on your word: the commit, then chapter 11.

""" % (CHAIN_SHORT,)

# ---- 8. THE_LOOP step-6 row ----
LOOP_OLD = "readback_probes 24/24, DA3) | the five forms BUILT — acts (1b), laws (3b, and on the kin 5b), a retelling inside a law (4b), a STATE (6b), a STRETCH (7b); the second pass after Deuteronomy |"
LOOP_NEW = ("readback_probes 24/24, DA3); cold_run_second_tablets.py (chapter 10, THE FORMS COMBINED — NO SEVENTH 2026-09-20: the retelling's tail and the laws' head in one chapter — twenty-five rows VERBATIM 9 / VARIANT 10 / EXPANDED 3 / TURNED 1 / SUPPLIED 2; T2 twice — the fragments in the ark (10:2) and Aaron's burial (10:6) written once at their own days by retrograde markers, the statuses fragments_in_the_ark (the docket's value) and buried (reused); T6 once — 10:10's third forty to the timers' fire; T4 on 10:12-22 with the code's four holes compiled at the chapter's own day (fear_of_heaven_asked, heart_circumcision_commanded + stiffening_barred, love_owed's first write, cleaving_commanded); readback_probes 27/27, DB3) | the five forms BUILT and COMBINED (8b) — acts (1b), laws (3b, and on the kin 5b), a retelling inside a law (4b), a STATE (6b), a STRETCH (7b); the second pass after Deuteronomy |")

# ---- 9. RESUME ----
RESUME_HEAD = """# ⚠ THE DEUTERONOMY WALK sitting 8b (2026-09-20; step9/DEUTERONOMY_WALK.md "Sitting 8b" + "THE DOCKET — AS RUN" + "Sitting 8b — AS BUILT"): CHAPTER 10 COMPILED —
# step9/cold_run_second_tablets.py the 65th runner (%d/%d; six cells; THE READBACK'S FORMS COMBINED, NO SEVENTH: twenty-five rows, ten on the tape, thirteen by CALL,
# TWO SUPPLIED WITH A WRITE (the fragments in the ark at the erection's day (2, 1, 1); Aaron's burial at his death (40, 5, 1) — the retrograde markers at Deut 10:2 and
# 10:6), ONE stretch row (10:10's third forty to the timers' fire = 40; THE SECOND ASCENT'S DATE MATCH — Seder Olam Rabbah 6:2), the laws' form on 10:12-22 with FOUR
# own-day lines after the forward marker at 10:12 — demand_declared (fear_of_heaven_asked), heart_circumcision_commanded (+ stiffening_barred the one prohibition),
# stranger_love_commanded (love_owed's FIRST write — a debit toward the stranger), cleaving_commanded (the scholars)), law_second_tablets the 70th daemon (given_at
# Deut 10:1, boot); the tape 10/10 on its fourth run with RUN (1317, 96, 88, 0, 12, 1613, 41, 319, pairs, 127) as predicted, PREVIOUS_RUN 7b's exactly, markers 172,
# closes 127 (four runs: DA1 — 7b's own count literal — retyped; two attempts at import on the hole-ground scans; CA1, DB1, DB4, DB7 from the third run's print); the docket %d rows read whole from the start (its own
# run); every probe suite and gate GREEN (%s), the sweep %d/64. ⚠ the open debits on Israel 8 -> 9 (love_owed a DEBIT by its registry op); the opening_speech edge dropped at the callees' print (17 CALL edges).
# NEXT on the ruling: the commit on the owner's word (the cache's, 7b's, 8's and 8b's — ONE message); chapter 11's reading (11:1-32) — one run.
""" % (CASES_N, CASES_N, NROWS, CHAIN_SHORT, SW_P)

# ---- 10. THE STATE DOC — #197 ADDENDUM 9 ----
STATE_ADD = """
#197 ADDENDUM 10 (2026-09-20, at the close of THE DEUTERONOMY WALK sitting 8b — THE COMPILE OF CHAPTER 10, RUN B of two under THE TWO-RUN RULE, on the owner's "Go" after the compaction — A CLEAN COMPACTION POINT): THE SITTING RAN AS THE RULE SAYS — RUN A the rereads, the measurements and the design (#197 addendum 7), THE DOCKET its own run in RUN A's window on "The docket go" (#197 addendum 8), RUN B this (its compaction point mid-run #197 addendum 9): patch_probes_ch10.py (Q25-Q27 written to FAIL before the types — 23/27 at the FAIL print: Q25-Q27 on the missing runner, Q23 on its own literal retyped 169 -> 172 before the tape), add_types_ch10.py (kinds 1142 — fragments_placed_in_the_ark and aaron_buried ACTS, demand_declared, heart_circumcision_commanded, stranger_love_commanded, cleaving_commanded STATUTES, second_tablets_case; effects 1037 — fragments_in_the_ark, fear_of_heaven_asked, heart_circumcision_commanded, cleaving_commanded statuses and stiffening_barred a block, THE NAMES AND VALUES FROM THE DOCKET; the daemon law_second_tablets the 70th; the functions block; the span and EIGHTEEN CALL edges; I5 70; the register's 10:5 reclassed ACT and 10:22's why), ch10_callees.py (every CALL's facts printed before an assert — the older runners' cells take q, the Deuteronomy runners' (case, data); NO CELL on 1:10's stars in the opening-speech runner: the design's eighteenth edge DROPPED, patch_after_callees_ch10.py — 17 CALL edges; Q25's stretch resolver extended for a timer's fire), the runner in three parts — part 1 DERIVED by content markers from the chapter-9 runner's helpers and the reading's own ink instrument (71 asserts; one clock literal retyped from the fast checker's print: Hor to the death 29 days), parts 2 and 3 typed — with the fast checker (0 fails), the CASES generated (%d, per cell %s) and frozen under the guard, cold_run_second_tablets.py %d/%d ON ITS FIRST GRADED RUN (the scene twenty-four persons, three exempt, no lashes; the narrative 7 writes, three entities, two dated lines; love_owed a DEBIT by its registry op — LEDGER OPS read), the recorder with the cache off (%d records; second_tablets 30 submits — HISTORY 2, statute 4, case 24), the stitcher twice — the first fell on a repeated placement kwarg (7b's lesson 11 repeated once), the second whole (the three markers at Deut 10:2, 10:6 and 10:12 in the MK list; PLACEMENT read — the own-day line AT THE FORWARD MARKER'S OWN VERSE takes the marker's class: text_constrained 110, page_order 1149, reading_placed 58; CENSUS %s as predicted), patch_seq_literals_ch10.py (RUN, PREVIOUS_RUN 7b's exactly, NEWEST_RUNNER, PLACEMENT and CENSUS read from the stitcher's print, DB1-DB9 — the D series' second name, the VERDICTS entries, the ten 'markers 169' literals retyped to 172 with CP6's 130 -> 131), THE TAPE 9/10 ON ITS FIRST RUN — THE REST OK, RUN OK, the D-series miss DA1: 7b's own LINES checkpoint holds 'markers 169' in a tuple form outside the ten retypes' patterns — THE ELEVENTH STALE LITERAL, retyped from the print (patch_da1_ch10.py); the second and third attempts FELL AT IMPORT on the hole-ground scans (the fold now carrying this sitting's writes: the chapter-9 runner's stiff-neck scan found stiffening_barred, the runner's own LAW_SCAN found love_owed — each excludes the later effect, patch_nr_scan_ch10.py and part 1 re-derived); THE THIRD RUN 9/10 with FOUR diffs retyped from the print (patch_tape2_ch10.py: CA1 the markers' list, DB1 the placements' three classes, DB4 the fire at or after the marker with Q25's resolver, DB7 circumcision_due 22) — 10/10 ON THE FOURTH RUN (%s s) with RUN (1317, 96, 88, 0, 12, 1613, 41, 319, the four pairs, 127) as the design's arithmetic wrote it; checkpoint_check.py --all after the tape (%s rows); THE GATES CHAIN — %s: the thirteen probe suites (%s), %s. THE READBACK'S FORMS COMBINED AS BUILT: twenty-five rows VERBATIM 9 / VARIANT 10 / EXPANDED 3 / TURNED 1 / SUPPLIED 2; the two SUPPLIED rows with their writes, dated (2, 1, 1) and (40, 5, 1); the stretch row to the timers' fire (40 — DB4, Q25); THE SECOND ASCENT'S DATE MATCH (Seder Olam Rabbah 6:2 — 7b's OPEN row closed, its item (iii) paid); the OPEN row the place of the death; the hole the go, outside the span; the four own-day lines after the forward marker at 10:12. THE RECORDS (write_ch10b_records.py from the sheet, one call): the map's "Sitting 8b — AS BUILT" (twenty-two departures, twelve lessons), COMPILE_DEBT's sitting-8 box PAID + the 8b box (seven owed items — the registry's homograph, the finder's third form, the calf's own day, the Exodus 33 holes, love_owed's open debit, the forward kin at chapters 13, 16, 28, 30, 31, the owner's word on the SUPPLIED forms), MIDDOT's compile entry (I1, I2 at three seats, E1 at two, E4, E26 at two, E30, the do-not-read readings and the juxtapositions named; the positive form rule; the clock read back against the shelf's date), MISHNAH_TOPICS (twenty-one heads), RESEARCH_LOG, THE_STEPS, THE_BRIEFING (the scoreboard bullet and an entry), THE_LOOP's step-6 row (the forms combined), RESUME, RECORD_FORMS (the writer's pointer), this addendum, the addenda §50, the recovery page (section 2 rewritten under its cap; 65 runners; the newest instances), the memory (the walk note and the index line under 17,000). THE FORMS copied (copy_ch10b_forms.py — RUN B's scripts and prints, the chain's folder). THE TREE: + cold_run_second_tablets.py, the registries (event_vocabulary, effect_vocabulary, daemon_dispositions, dependency_dispositions, register_dispositions), cold_run_sequence.py (the tape's six lines and three markers, the literals, DB1-DB9, DA1 and the ten counts), readback_probes.py, installation_probes.py, checkpoint_positions.yaml, sweep_stamp.json, the records, the forms. NOT COMMITTED (since a985fbc): THE VERIFIED-IMPORT CACHE, sitting 7b whole, sitting 8 and sitting 8b whole (RUN A, the docket, RUN B) — ONE message at <scratch>/commit_msg_ch9b.txt covers all for the owner's word ("commit" = no push; "commit push" = both). NOTHING MID-FLIGHT — A CLEAN COMPACTION POINT. NEXT ON THE RULING: the commit on his word; then CHAPTER 11's reading (11:1-32) — one run; THE INSTALL HYPOTHESIS, THE SUPPLIED GRADE (the fifth form's, no write), THE SUPPLIED-WITH-A-WRITE FORM (the sixth's, twice here), the calf's own day marker and the registry's homograph on the table. POST-COMPACTION REREADS: the recovery page, the map's "Sitting 8b — AS BUILT" (the newest section — the departures and the lessons), MEMORY.md.
""" % (CASES_N, PER_CELL, CASES_N, CASES_N, REC_N, CENSUS, tape_elapsed, CC_ROWS, CHAIN_STORY, pr_line, gates_line)

# ---- 11. THE RECOVERY ADDENDA — section 50 ----
ADDENDA_ADD = """

## 50. ADDENDUM (2026-09-20, THE DEUTERONOMY WALK sitting 8b — THE COMPILE OF CHAPTER 10, Deuteronomy 10:1-22 COMPILED AND ON THE TAPE in two runs with the docket its own run; the owner: "Go", "The docket go", "Go"; the state doc's #197 addenda 7-9)

THE SHAPE: THE TWO-RUN RULE's third compile sitting — RUN A the rereads, the measurements (ch10_compile_recon.py, ch10_measure2.py, ch10_measure3.py, ch10_docket_scan.py on the
running world's snapshot: every retold act on the tape with its day, the fragments on no entry, Aaron unburied, the Levites' investiture at the calf, the laws' kin's cells
with no write for 6:13, the register's one receipt seat) and the design in the map; THE DOCKET its own run in the same window on "The docket go" (532 rows in three parts,
every row whole; deu_10_ekev_exam_2026-09-20.md — THE SECOND ASCENT'S DATE MATCHES SEDER OLAM RABBAH 6:2; the ark one in the Bavli, two in the Tosefta; the effects' names and
values from the rows); RUN B the build after one compaction (the probes to fail 23/27, the types, the callees' print — one edge dropped, the runner in parts with part 1
derived by content markers, the fast checker, the cases generated, the recorder with the cache off, the stitcher twice, the literals with the D series' second name, the tape
twice — the eleventh stale literal 7b's own DA1, the checkpoint check, the chain — %s — the records in one call, the forms) — three clean points. THE FORMS COMBINED: T1
reference rows, T2 SUPPLIED WITH A WRITE twice (the fragments in the ark at (2, 1, 1), Aaron's burial at (40, 5, 1) — two retrograde markers, no clock walk), T6 one stretch
row (10:10 to the timers' fire — forty), T4 the laws' form with the code's four holes compiled at (40, 11, 1) after the forward marker at 10:12 (fear_of_heaven_asked,
heart_circumcision_commanded + stiffening_barred, love_owed's first write — a debit, cleaving_commanded); the OPEN row the place of the death (the retreat of seven stations
the parameter already on file); the hole the go, outside the span. THE DESIGN'S ERRORS caught by prints: the stretch's end a timer's fire (Q25's resolver extended), the
placement at a forward marker's own verse (text_constrained 110, page_order 1149), the opening_speech edge (no cell on 1:10), love_owed's op (a debit — the open debits 8 -> 9),
DA1's count literal (9/10 on the first tape run), the clock's Hor-to-death 29, the rows twenty-five at 9/10/3/1/2, the persons twenty-four. THE NUMBERS:
cold_run_second_tablets.py %d/%d; the tape 10/10 on its second run, RUN (1317, 96, 88, 0, 12, 1613, 41, 319, pairs, 127) as predicted, markers 172; kinds 1142, effects 1037,
daemons 70, seventeen CALL edges; the docket %d rows; the sweep %d/64; every gate green. OWED FORWARD: the registry's homograph (one id for tevah and aron) on the owner's word,
the finder's third form, the calf's own day on his word, the Exodus 33 holes, love_owed's open debit, the forward kin (13:5, 16:19, 28:62, 30:6, 31:26), the owner's word on the
SUPPLIED forms. The records on the sheet, the forms in World/step9/forms_deuteronomy_walk/ (copy_ch10b_forms.py).
""" % (CHAIN_SHORT, CASES_N, CASES_N, NROWS, SW_P)

# ---- 12. THE RECOVERY PAGE — section 2 rewritten; sections 4, 5, 6 retouched; the cap asserted ----
def f_recovery(s):
    i = s.index('## 2. WHERE IT STANDS'); j = s.index('## 3. THE STANDING LAWS')
    sec2 = """## 2. WHERE IT STANDS (2026-09-20, after 8b; the state doc #197 addendum 10 the newest)
- NUMBERS CLOSED. DEUTERONOMY 1:1-10:22 COMPILED AND ON THE TAPE (1-7 at 29c189b, 8 at a985fbc — PUSHED; 9 at 7/7b, 10 at 8/8b).
- 224 frozen units, standing 2227, hash 8b8fff1fa28953af. 65 runners, 70 daemons, %d functions; 1142 kinds / 1037 effects.
- THE TAPE at RUN (1317, 96, 88, 0, 12, 1613, 41, 319, pairs, 127), markers 172, closes 127; the sweep %d/64; every gate GREEN; the
  register gate DECLARED %d / DEBT 0 (10:5's receipt seat %s). The readback's forms COMBINED (8b): two acts SUPPLIED WITH A WRITE,
  the third forty a stretch to the timers' fire, the second ascent's date MATCH (Seder Olam 6:2); the calf's day marker, the
  fifth form's SUPPLIED and the registry's homograph (one id for tevah and aron) his decisions, open.
- Uncommitted since a985fbc: the cache, 7b, 8, 8b; ONE message at <scratch>/commit_msg_ch9b.txt covers all.
- NEXT ON HIS WORD: the commit; then CHAPTER 11 (11:1-32) — one run.

""" % (DG[1], SW_P, RG[0], SEAT_10_5)
    s = s[:i] + sec2 + s[j:]
    old4 = "cold_run_<span>.py (64 runners)"; assert s.count(old4) == 1, s.count(old4)
    s = s.replace(old4, "cold_run_<span>.py (65 runners)")
    old5 = 'the newest instances: the map\'s "Sitting 8" and "Sitting 7b")'; assert s.count(old5) == 1
    s = s.replace(old5, 'the newest instances: the map\'s "Sitting 8" and "Sitting 8b")')
    old6 = "- Deuteronomy's sittings: the map; the addenda §31-49 (§39 the whole-row rule). The cost cuts: §35, §45, §47."; assert s.count(old6) == 1
    s = s.replace(old6, "- Deuteronomy's sittings: the map; the addenda §31-50 (§39 the whole-row rule). The cost cuts: §35, §45, §47.")
    assert len(s.encode('utf-8')) <= 10240, ('THE RECOVERY PAGE OVER ITS CAP', len(s.encode('utf-8')))
    return s

# ---- 12b. GATES_CHAIN.md — THE NINETEENTH SLIP under D38 ----
GATES_OLD = "THE EIGHTEENTH SLIP (the same sitting, found by C2 at the first chain):"
GATES_NOTE = """THE NINETEENTH SLIP (THE DEUTERONOMY WALK 8b, 2026-09-20 — the cache's OWN ERROR REPORT): when a node raises on the cached path the cache reports which node
by `ast.get_source_segment(src, node)` — and `src`, the module's source text, had been REBOUND TO A MODULE a few lines above in the restore loop (an alias's home
module; a patch's source module), so the report itself crashed ('expected string or bytes-like object, got module') and masked the real error at the positions
table's eight workers. The two rebindings renamed srcm (patch_ink_cache_src_ch10.py); the report and the slow-node record read the source text again; FORM
unmoved. The positions table measured by FOUR workers (7b's way) — the eight-worker step has failed two sittings running (the watchdog at 7b, a cached-path raise
here) and four is its standing form until the eight are measured. The slips are nineteen.

THE EIGHTEENTH SLIP (the same sitting, found by C2 at the first chain):"""
def f_gates(s):
    assert s.count(GATES_OLD) == 1 and 'THE NINETEENTH SLIP' not in s; return s.replace(GATES_OLD, GATES_NOTE, 1)
plans_gates = ('World/step9/GATES_CHAIN.md', f_gates)

# ---- 13. MEMORY ----
MEM_DESC_OLD = "description: \"COMMITTED THROUGH a985fbc (2026-09-19; PUSHED) — SITTING 8 DONE 2026-09-20 (chapter 10 READ AND FROZEN"
MEM_DESC_NEW = "description: \"COMMITTED THROUGH a985fbc (2026-09-19; PUSHED) — SITTING 8b DONE 2026-09-20 (chapter 10 COMPILED — the readback's forms COMBINED, two acts told only in the retelling written once at their own days, the second ascent's date MATCH, four laws with no code compiled, love_owed's first write; UNCOMMITTED) — SITTING 8 DONE 2026-09-20 (chapter 10 READ AND FROZEN"
MEM_PARA = """

SITTING 8b RUN B DONE 2026-09-20 (the owner: "Go" after the compaction; the map's "Sitting 8b" + THE DOCKET — AS RUN + AS BUILT): CHAPTER 10 COMPILED —
cold_run_second_tablets.py the 65th runner (%d/%d on its first graded run), law_second_tablets the 70th daemon (given_at Deut 10:1, boot). THE READBACK'S FORMS
COMBINED, NO SEVENTH: twenty-five rows VERBATIM 9 / VARIANT 10 / EXPANDED 3 / TURNED 1 / SUPPLIED 2 — T2 TWICE: the fragments in the ark (10:2) written once at the
erection's day (2, 1, 1) by the retrograde marker at Deut 10:2 (fragments_in_the_ark a STATUS on the ark — the docket's value: the tablets and the fragments, the
scroll inside or beside), Aaron's burial (10:6) at his death (40, 5, 1) by the marker at Deut 10:6 (buried REUSED — the ninth); T6 once: 10:10's third forty to THE
TIMERS' FIRE (40 — DB4, Q25; a stretch may end at a fire); THE SECOND ASCENT'S DATE MATCH (Seder Olam 6:2 — 7b's open row closed); T4 on 10:12-22 with FOUR own-day
lines after the forward marker at 10:12 — demand_declared (fear_of_heaven_asked, Berakhot 33b:23), heart_circumcision_commanded (the evil inclination, Sukkah 52a:7;
stiffening_barred the one prohibition, no lashes), stranger_love_commanded (love_owed's FIRST write — a DEBIT by its registry op toward the stranger; the open debits
on Israel 8 -> 9), cleaving_commanded (the scholars, Ketubot 111b:7; the four clauses positive); the OPEN row the place of the death (the retreat of seven stations
already a parameter); the hole the go, outside the span. The tape 10/10 on its second run with RUN (1317, 96, 88, 0, 12, 1613, 41, 319, pairs, 127) as predicted,
markers 172 (the first run 9/10: 7b's own DA1 held 'markers 169' — the ELEVENTH stale literal; two attempts at import on the hole-ground scans; the third 9/10 on CA1, DB1, DB4, DB7 — retyped from the print; the fourth 10/10); kinds 1142, effects 1037, daemons 70,
SEVENTEEN CALL edges (the opening_speech edge dropped at the callees' print — no cell on 1:10's stars); every gate green (%s), the sweep %d/64.
⚠ LESSONS (nine, in the map): a stretch may end at a timer's fire; the marker's-verse rule holds for a FORWARD marker too (text_constrained 110, page_order 1149 —
read); A REUSED EFFECT BRINGS ITS REGISTRY OP (love_owed a debit — read LEDGER OPS before the checkpoints); THE NEWEST SITTING'S OWN CHECKPOINTS JOIN THE
STALE-LITERAL LIST (grep every LINES and REST tuple); the callees' print drops an edge before it is typed; T2 twice is two retrograde markers and no clock walk;
THE FORMS COMBINE — no seventh; part 1 by content markers from the reading's ink instrument; THE TWO-RUN RULE HELD on its third compile sitting. ⚠ OWED: the
registry's homograph (one id for tevah and aron) ON HIS WORD; the finder's third form; the calf's own day ON HIS WORD; the Exodus 33 holes; love_owed's open debit.
NOT COMMITTED (since a985fbc; ONE message at <scratch>/commit_msg_ch9b.txt covers the cache, 7b, 8 and 8b). NEXT on the ruling: the commit; chapter 11's reading
(11:1-32), one run.
""" % (CASES_N, CASES_N, CHAIN_SHORT, SW_P)
MEM_IDX_OLD = 'map World/step9/DEUTERONOMY_WALK.md; ch 1-9 COMPILED, 10 BUILT (8b RUN B: tape 10/10, chain pass 3 running); NEXT: the records, then commit'
MEM_IDX_NEW = 'map World/step9/DEUTERONOMY_WALK.md; ch 1-10 COMPILED (1-8 PUSHED a985fbc; 9, 10 + the cache UNCOMMITTED); NEXT: commit on his word, then ch 11'

# ---- 14. RECORD_FORMS — the writer's form pointer ----
FORMS_OLD = "World/step9/forms_deuteronomy_walk/write_ch9b_records.py (write_ch8b_records.py,"
FORMS_NEW = "World/step9/forms_deuteronomy_walk/write_ch10b_records.py (write_ch9b_records.py, write_ch8b_records.py,"

# ---- THE WRITES (every text built above; the files opened only now) ----
def read(p): return open(p if p.startswith('/') else f'{ROOT}/{p}', encoding='utf-8').read()
def write(p, s): open(p if p.startswith('/') else f'{ROOT}/{p}', 'w', encoding='utf-8').write(s)
plans = []
def f_map(s):
    assert 'THE DOCKET — AS RUN (2026-09-20, on "The docket go"' in s and '## Sitting 8b — THE COMPILE OF CHAPTER 10 — AS BUILT' not in s
    return s.rstrip('\n') + '\n' + AS_BUILT
plans.append(('World/step9/DEUTERONOMY_WALK.md', f_map))
def f_debt(s):
    assert s.count(DEBT_HDR_OLD) == 1, s.count(DEBT_HDR_OLD)
    return s.replace(DEBT_HDR_OLD, DEBT_HDR_NEW).rstrip('\n') + '\n' + DEBT_BOX
plans.append(('World/step9/COMPILE_DEBT.md', f_debt))
def f_middot(s):
    assert s.count(MIDDOT_ANCHOR) == 1, s.count(MIDDOT_ANCHOR); return s.replace(MIDDOT_ANCHOR, '\n' + MIDDOT_ENTRY + MIDDOT_ANCHOR)
plans.append(('logic/MIDDOT.md', f_middot))
def f_topics(s):
    lines = s.split('\n'); done = set()
    for i, l in enumerate(lines):
        for head, note in TOPIC_NOTES.items():
            if l.startswith(head):
                assert head not in done; lines[i] = l.rstrip() + note; done.add(head)
    assert done == set(TOPIC_NOTES), set(TOPIC_NOTES) - done
    return '\n'.join(lines)
plans.append(('logic/MISHNAH_TOPICS.md', f_topics))
plans.append(('RESEARCH_LOG.md', lambda s: s.rstrip('\n') + '\n' + RLOG))
def f_steps(s):
    assert s.count(STEPS_ANCHOR) == 1; return s.replace(STEPS_ANCHOR, STEPS_PARA + STEPS_ANCHOR)
plans.append(('THE_STEPS.md', f_steps))
def f_brief(s):
    assert s.count(BRIEF_BULLET_ANCHOR) == 1 and s.count(BRIEF_ENTRY_ANCHOR) == 1 and '## SCOREBOARD (as of 2026-09-20, latest)\n' in s, (s.count(BRIEF_BULLET_ANCHOR), s.count(BRIEF_ENTRY_ANCHOR))
    s = s.replace(BRIEF_BULLET_ANCHOR, BRIEF_BULLET + BRIEF_BULLET_ANCHOR)
    return s.replace(BRIEF_ENTRY_ANCHOR, BRIEF_ENTRY + BRIEF_ENTRY_ANCHOR)
plans.append(('THE_BRIEFING.md', f_brief))
def f_loop(s):
    assert s.count(LOOP_OLD) == 1; return s.replace(LOOP_OLD, LOOP_NEW)
plans.append(('World/step9/THE_LOOP.md', f_loop))
plans.append(plans_gates)
plans.append(('World/RESUME.md', lambda s: RESUME_HEAD + s))
plans.append(('logic/pre_logic_methods_2026-07-28/PROMPT_continue_solo_era_2026-08-06.md', lambda s: s.rstrip('\n') + '\n' + STATE_ADD))
plans.append(('logic/pre_logic_methods_2026-07-28/RECOVERY_addenda_2026-09-12.md', lambda s: s.rstrip('\n') + ADDENDA_ADD))
plans.append(('logic/pre_logic_methods_2026-07-28/RECOVERY_new_thread_2026-09-12.md', f_recovery))
def f_forms(s):
    assert s.count(FORMS_OLD) == 1; return s.replace(FORMS_OLD, FORMS_NEW)
plans.append(('World/step9/RECORD_FORMS.md', f_forms))
def f_mem(s):
    assert s.count(MEM_DESC_OLD) == 1, s.count(MEM_DESC_OLD)
    return s.replace(MEM_DESC_OLD, MEM_DESC_NEW, 1).rstrip('\n') + '\n' + MEM_PARA
plans.append((f'{MEM}/deuteronomy-walk.md', f_mem))
def f_idx(s):
    assert s.count(MEM_IDX_OLD) == 1, s.count(MEM_IDX_OLD); s2 = s.replace(MEM_IDX_OLD, MEM_IDX_NEW); assert len(s2.encode('utf-8')) < 17000, len(s2.encode('utf-8')); return s2
plans.append((f'{MEM}/MEMORY.md', f_idx))
outs = []
for p, f in plans:
    s = read(p); s2 = f(s); assert s2 != s, p; outs.append((p, s2, len(s), len(s2)))
if CHECK:
    for p, s2, a, b in outs: print('WOULD WRITE', p, a, '->', b)
    sys.exit(0)
for p, s2, a, b in outs:
    write(p, s2); print('WROTE', p, a, '->', b)
print('the records written')
