import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE DEUTERONOMY WALK sitting 7b — THE COMPILE OF CHAPTER 9, RUN B (2026-09-19): THE RECORDS, written after every gate ran — the numbers COMPUTED from the
# gates chain's own prints in the scratchpad (gates_ch9b/*.out; never recited) and the docket's own rows; every text built whole before any file is
# opened; the ledgers appended, the map appended, the checklist's boxes marked paid, the recovery page REWRITTEN in its section 2 under its cap, the
# memory index edited under its cap. `--check` parses and prints without writing. Sitting 6b's form (write_ch8b_records.py) on the sheet World/step9/RECORD_FORMS.md.
import os, re, sys, subprocess
ROOT = _ROOT
SP = os.path.dirname(os.path.abspath(__file__))
G = f'{SP}/gates_ch9b'
MEM = os.path.expanduser('~/.claude/projects/-Users-Shared-TorahSim/memory')
CHECK = '--check' in sys.argv
def rd(name): return open(name if name.startswith('/') else f'{G}/{name}', encoding='utf-8', errors='ignore').read()
def last_frac(name, m):
    t = rd(name); hits = re.findall(r'(\d+)/%d\b' % m, t); assert hits, (name, 'no n/%d' % m); return int(hits[-1])
# ---- THE NUMBERS FROM THE PRINTS ----
summ = rd('SUMMARY.txt'); assert 'GATES CHAIN DONE — ALL GREEN' in summ, summ
tape = rd('tape.out'); assert '10/10 checkpoints' in tape and 'OK   THE REST' in tape
DA = re.findall(r'CHECKPOINT (DA\d) .*? (MATCH|MISS|DIVERGE)$', tape, flags=re.M); assert len(DA) == 9 and all(v == 'MATCH' for _, v in DA), DA
tape_elapsed = re.search(r'elapsed ([\d.]+)s', tape).group(1)
PL = re.search(r"PLACEMENT \(O9 T2\): markers (\{[^}]*\}); events (\{[^}]*\})", tape); assert PL
assert PL.group(1) == "{'text_constrained': 107, 'reading_placed': 47}" and PL.group(2) == "{'text_constrained': 109, 'page_order': 1146, 'reading_placed': 56}", PL.groups()
rg = rd('register.out'); m = re.search(r'DECLARED (\d+); DEBT (\d+); FAILS (\d+)', rg); assert m and 'THE REGISTER GATE: GREEN' in rg
RG = tuple(int(x) for x in m.groups())
assert not re.search(r'^\s*Deut 9:\d+\s+(CHAPTER|DAEMONS|ACT|CLOSE|RUN)', rg, flags=re.M), 'a seat in chapter 9 appeared'   # no receipt form in the chapter (the design's measure)
dg = rd('daemon.out'); m = re.search(r'\((\d+) daemons, (\d+) functions\)', dg); assert m and 'gate satisfied' in dg; DG = tuple(int(x) for x in m.groups())
dp = rd('dependency.out'); m = re.search(r'dispositions on file: (\d+) edges, (\d+) pointers', dp); assert m and 'gate satisfied' in dp; DP = tuple(int(x) for x in m.groups())
LC = re.search(r'LINK CENSUS \(the link review law\): reference (\d+), transfer (\d+), hypothesis (\d+), none (\d+)', dp); assert LC; LC = tuple(int(x) for x in LC.groups())
m = re.search(r'required edges (\d+), required pointers (\d+); live import edges (\d+)', dp); DPR = tuple(int(x) for x in m.groups())
bw = rd('build.out'); assert 'ALL GREEN' in bw, bw[-600:]
jg = rd('journal.out'); assert 'GATE GREEN' in jg; m = re.search(r'(\d+) kinds, (\d+) rows in the index', jg); JG = tuple(int(x) for x in m.groups())   # since THE GATES CUT the journal gate runs ONCE before the sweep; the stamp and the UNMOVED gate stand after it
um = rd('unmoved.out'); assert 'GATE GREEN' in um and 'THE JOURNAL UNMOVED' in um, um[-300:]; st_ = rd('stamp.out'); assert 'THE JOURNAL STAMPED' in st_, st_[-300:]
sw = rd('sweep.out'); SW_P = len(re.findall(r'^PASS +cold_run_\w+\.py', sw, flags=re.M)); SW_F = len(re.findall(r'^FAIL +cold_run_\w+\.py', sw, flags=re.M))
SW_CELLS = sum(int(a) for a, b in re.findall(r'score=(\d+)/(\d+)', sw)); assert SW_P + SW_F == 63, (SW_P, SW_F); assert SW_F == 0, 'the sweep has failures — read them first'   # the 64 runners minus the sequence file the sweep skips
assert 'FULL of 64' in sw and '63/63 runners green' in sw, sw[-400:]
po = rd('positions.out'); m = re.search(r'(\d+) checkpoints over (\d+) pauses', po); assert m, po[-800:]; PO = tuple(int(x) for x in m.groups())
PR = {'census': last_frac('probe_census.out', 224), 'installation': last_frac('probe_installation.out', 6), 'readback': last_frac('probe_readback.out', 24),
      'register': last_frac('probe_register.out', 7), 'sequence': last_frac('probe_sequence.out', 4), 'view': last_frac('probe_view.out', 6),
      'population': last_frac('probe_population.out', 9), 'journal': last_frac('probe_journal.out', 7), 'cursor': last_frac('probe_cursor.out', 6),
      'large_letter': last_frac('probe_large_letter.out', 6), 'checkpoint': last_frac('checkpoint.out', 7), 'ink_cache': last_frac('probe_ink_cache.out', 8)}
ck = rd('probe_clock.out'); m = re.findall(r'(\d+)/(\d+)', ck); PR['clock'] = ('%s/%s' % m[-1]) if m else 'exit 0'
assert PR['checkpoint'] == 7 and PR['readback'] == 24 and PR['installation'] == 6 and PR['large_letter'] == 6 and PR['ink_cache'] == 8, PR
run1 = rd(f'{SP}/ch9_run1.out'); assert '51/51' in run1
CASES_N = int(re.search(r'CASES generated: (\d+)', rd(f'{SP}/ch9_cases_gen.out')).group(1)); PER_CELL = re.search(r'per cell (\{.*?\})', rd(f'{SP}/ch9_cases_gen.out')).group(1)
t1 = rd(f'{SP}/ch9_tape1.out'); assert '9/10 checkpoints' in t1 and "'CA1 DIVERGE'" in t1, 'the first tape run: 9/10, CA1 the miss'
rec = rd(f'{SP}/seq_record_ch9.out'); m = re.search(r'recording: (\d+) records written', rec); REC_N = int(m.group(1)); assert REC_N > 2000, REC_N
st = rd(f'{SP}/seq_stitch_ch9.out'); m = re.search(r'CENSUS tuple .*?: (\(.*\))', st); CENSUS = m.group(1); assert '1311' in CENSUS and '169' in CENSUS and '856' in CENSUS, CENSUS
pf = rd(f'{SP}/ch9b_probes_fail.out'); assert 'the daemon order and the dispositions disagree' in pf, 'the fail print: the daemon assertion'
c1 = rd(f'{SP}/ch9b_chain_SUMMARY_first.txt'); assert 'FAIL probes' in c1 and 'FAIL dependency' in c1 and 'GATES CHAIN DONE — FAILURES ABOVE' in c1, 'the first chain: the probes and the dependency gate'
d1 = rd(f'{SP}/ch9b_chain_dependency_first.out'); assert 'FAIL EDGE not_righteousness -> chatat' in d1 and 'FAIL EDGE not_righteousness -> family' in d1 and 'FAIL POINTER Deut 9:3 AS_WHEN' in d1, 'the three demands'
r1 = rd(f'{SP}/ch9b_chain_probe_readback_first.out'); assert 'readback_probes: 21/24' in r1 and 'FAIL Q14' in r1 and 'FAIL Q17' in r1 and 'FAIL Q20' in r1, 'the three older probes'
k1 = rd(f'{SP}/ch9b_chain_probe_ink_cache_first.out'); assert 'FAIL C2' in k1 and "'_SRC'" in k1, 'the eighteenth slip'
c2 = rd(f'{SP}/ch9b_chain_SUMMARY_second.txt'); assert 'SKIP tape (before --from)' in c2 and 'FAIL probes' in c2 and 'ink_cache: 8/8' in c2 and 'PASS dependency' in c2, 'the second pass: from the probes step — the readback probe without the live journal'
r2 = rd(f'{SP}/ch9b_chain_probe_readback_second.out'); assert 'FileNotFoundError' in r2 and '.jsonl.live' in r2, 'the live journal missing at the second pass'
c3 = rd(f'{SP}/ch9b_chain_SUMMARY_third.txt'); assert 'PASS tape' in c3 and 'PASS probes' in c3 and 'ink_cache: 8/8' in c3 and 'PASS register' in c3 and 'positions' not in c3, 'the third pass: green to the register gate, killed at the positions table by the memory watchdog'
c4 = rd(f'{SP}/ch9b_chain4.log'); po_direct = rd('positions.out'); assert 'BY 4 WORKERS' in po_direct, 'the positions table by four workers (the eight-worker step killed twice)'
# the docket's numbers from its own rows
DK = 'logic/oral_triage/deu_09_ekev_exam_2026-09-19.md'
dk = open(f'{ROOT}/{DK}', encoding='utf-8').read()
rows = [l for l in dk.split('\n') if re.match(r'^- .*? — (LAW|DERIVATION|DISPUTE|CONTEXT|OUTSIDE)\.', l)]
VD = {v: sum(1 for l in rows if re.match(r'^- .*? — %s\.' % v, l)) for v in ('LAW', 'DERIVATION', 'DISPUTE', 'CONTEXT', 'OUTSIDE')}
NROWS = len(rows); NLINK = sum(1 for l in rows if '[LINK' in l); NTOPIC = sum(1 for l in rows if '[TOPIC' in l); NCRED = sum(1 for l in rows if 'CREDITED' in l)
NWHOLE = sum(1 for l in rows if '[whole:' in l); DKB = len(dk.encode('utf-8'))
assert NROWS == 397 and NLINK + NTOPIC == NROWS and NWHOLE == 0, (NROWS, NLINK, NTOPIC, NWHOLE)
hp = subprocess.run(['python3', 'logic/solo_tools/scrub_home_paths.py', '--check'], cwd=ROOT, capture_output=True, text=True); assert hp.returncode == 0, hp.stdout[-500:] + hp.stderr[-500:]
NUM = dict(RG=RG, DG=DG, DP=DP, LC=LC, DPR=DPR, JG=JG, SW=(SW_P, SW_CELLS), PO=PO, PR=PR, PL=PL.groups(), tape_elapsed=tape_elapsed, cases=(CASES_N, PER_CELL), docket=(NROWS, NLINK, NTOPIC, NCRED, NWHOLE, DKB, VD), rec=REC_N, census=CENSUS)
print('THE NUMBERS:', NUM)
pr_line = ('census %d/224, installation %d/6 (I5 69), readback %d/24 (Q22-Q24 the sixth form), register %d/7, clock %s, sequence %d/4, view %d/6, population %d/9, journal %d/7, cursor %d/6, large_letter %d/6, checkpoint %d/7, ink_cache %d/8'
           % (PR['census'], PR['installation'], PR['readback'], PR['register'], PR['clock'], PR['sequence'], PR['view'], PR['population'], PR['journal'], PR['cursor'], PR['large_letter'], PR['checkpoint'], PR['ink_cache']))
gates_line = ('the daemon gate GREEN (%d daemons, %d functions WRAPPED); the dependency gate GREEN (%d edges and %d pointers on file — the link census reference %d / transfer %d / hypothesis %d / none %d; required %d edges and %d pointers, live import edges %d); '
              'build_world ALL GREEN (223 units, standing 2221, hash 8b8fff1fa28953af unmoved — no freeze this run); the journal gate GREEN before the sweep (%d kinds, %d rows in the index) and THE JOURNAL UNMOVED after it (the stamped digest equal — the sweep wrote nothing); THE REGISTER GATE --strict GREEN (DECLARED %d, DEBT %d, FAILS %d — no seat in chapter 9: no receipt form in it, as the design measured); '
              'the positions table %d checkpoints over %d pauses (DA1-DA9 in it; checkpoint_probes %d/7 after the rebuild); the sweep %d/63 at %s graded cells (the 64 runners less the sequence file it skips; FULL — the moved runner and its importers); the home-path gate GREEN'
              % (DG[0], DG[1], DP[0], DP[1], LC[0], LC[1], LC[2], LC[3], DPR[0], DPR[1], DPR[2], JG[0], JG[1], RG[0], RG[1], RG[2], PO[0], PO[1], PR['checkpoint'], SW_P, format(SW_CELLS, ',')))
docket_line = ('%d rows (link %d / topic %d; LAW %d, DERIVATION %d, DISPUTE %d, CONTEXT %d, OUTSIDE %d; credited %d; %s bytes), EVERY ROW READ WHOLE FROM THE START — no cut, no overlay (the parts\' WHOLE dicts empty, the correction counts zero and computed)'
               % (NROWS, NLINK, NTOPIC, VD['LAW'], VD['DERIVATION'], VD['DISPUTE'], VD['CONTEXT'], VD['OUTSIDE'], NCRED, format(DKB, ',')))
W7 = "THE DEUTERONOMY WALK sitting 7b"

# ---- 1. THE MAP — AS BUILT ----
AS_BUILT = """
## Sitting 7b — THE COMPILE OF CHAPTER 9 — AS BUILT (2026-09-19; the design above stands as written but for the departures below; RUN A the design
## on "Ok do ch 9", THE DOCKET its own run on "Go" in RUN A's window, RUN B on "Go" after the compaction — THE TWO-RUN RULE's second compile sitting, the docket clause applied)

THE RUN: cold_run_not_righteousness.py the 64th runner — %d/%d on its FIRST graded run (six cells, %d asks — per cell %s; the CASES generated from the cells'
own asks and frozen under the honest-pairing guard, the guard's count from the generator's print); law_not_righteousness the 69th daemon (given_at Deut 9:1,
installed_by boot); THE READBACK'S SIXTH FORM — THE RETELLING OF A STRETCH: THIRTY-TWO rows VERBATIM 14 / VARIANT 12 / EXPANDED 4 / TURNED 1 / SUPPLIED 1
(the design's "about thirty" — 9:22's three names three rows, 9:23's two seats two rows), twenty-two found on the tape by kind and first verse, nine in
the kin's cells by CALL, FOUR STRETCH ROWS (9:9 and 9:11 the ascent to the breaking, 9:18 and 9:25 the morrow to the second ascent) measured on the running
world by the markers' days at DA4 and Q22 — 40 and 40, Ta'anit 28b:9's twenty-four of Sivan and sixteen of Tammuz REPRODUCED by the calendar (Sivan thirty
days that year), Mishnah Ta'anit 4:6's seventeenth of Tammuz MATCH; the one SUPPLIED row 9:20's — AARON'S PERIL — WITH ITS WRITE: the act prayed_for_aaron
written ONCE at its own day by the RETROGRADE marker at Deut 9:20 (M['aaron_told'] = M['morrow'], (1, 4, 18)) and the status destruction_halved on aaron (THE
NAME FROM THE DOCKET — Vayikra Rabbah 10:5), the stretch ended by the forward marker at 9:21; the two OPEN rows (the calf's own day, the second ascent's date)
and the one hole named; twenty-three DATA rows (the docket's finds among them: Taberah outside the ten trials, the fasting's seat 9:9's own, the calf forbidden
from its making, the merit of the fathers a parameter with four dates, the crowns of Horeb stripped with no line, Mishnah Megillah 4:10's asymmetry, the
three requests of Exodus 33 with no line, the tablets' size); fifteen exam persons, two exempt (the one who prolongs and expects; the pleader after Hazael's
days), NO LASHES (the chapter holds no prohibition). THE TAPE 10/10 ON ITS SECOND RUN with RUN (1311, 96, 88, 0, 12, 1606, 40, 319, the four pairs, 127) AS THE
DESIGN'S ARITHMETIC WROTE IT, PREVIOUS_RUN 6b's exactly (no declared delta — a marker is not a line), CENSUS %s read at the stitcher's print as predicted
(on tape 1311, markers 169 — F 130, R 24 — kinds 856), markers 167 -> 169, closes 127, entities 319 unmoved, DA1-DA9 MATCH (%s s) — THE D SERIES OPENED;
THE FIRST RUN 9/10 — ONE OLDER CHECKPOINT MOVED: chapter 1b's CA1 holds THE DEUTERONOMY MARKERS' LIST as a literal (every retrograde marker with its
stated day, every forward marker's day) — the design's DA9 note had named only the COUNT literals (the nine 'markers 167' retyped as it said, CP6's 129 ->
130 with them); the list retyped from the print. THE TYPES: kinds 1133 -> 1135 (prayed_for_aaron an ACT, not_righteousness_case), effects 1031 -> 1032
(destruction_halved a status on aaron — the design's destruction_averted superseded by the docket's row before the types were typed), daemons 68 -> 69
(I5 69), ELEVEN CALL edges and the registration as predicted (the census demanded nothing more). THE PROBES: readback_probes Q22-Q24 written to FAIL before
the runner — the FAIL print a REFUSAL, not 21/24: the types had been run first and the world's reader (register_census.running_world) asserts the daemon
order against the dispositions ('the daemon order and the dispositions disagree: law_not_righteousness') — 24/24 after. THE GATES (the chain THREE TIMES — the first stopped at the probes step and the dependency gate, the second from the probes step at the readback probe without the tape's live journal, the third whole and GREEN to the register gate then KILLED at the positions table by the session's memory watchdog, the fourth from the positions table killed at the same step, the positions table then measured by FOUR workers with the step's own command outside the chain script, the fifth from the checkpoint probe %s): %s; the
thirteen probe suites — %s. THE DOCKET (its own run, 2026-09-19): %s.

THE DEPARTURES FROM THE DESIGN (twenty-one, each read from a print): (1) THE PROBES' FAIL PRINT IS A REFUSAL — add_types_ch9.py ran before readback_probes.py
(the order slipped from 6b's), and the snapshot reader refused the world at the daemon assertion; the FAIL is on record as that refusal (ch9b_probes_fail.out);
(2) THE RECORDER UNDER THE IMPORT CACHE RECORDED 118 SUBMITS — a module restored from the cache never runs its scene, so its submits never happen: the
stitcher wrote a tape of 241 lines into the sequence file before its own prediction step failed; rerun with INK_CACHE=0 (%d records, the tape 1,682 lines)
— THE RECORDER RUNS WITH THE CACHE OFF; (3) the stitcher's mk code carried placement='reading_placed' where with_placement() adds it — 'keyword argument
repeated' at the prediction step; removed; (4) THE PLACEMENT — the line at the marker's own verse takes the marker's class: events reading_placed 55 -> 56,
page_order 1146 UNMOVED where the design wrote page_order 1147 (THE NUMBERS WALK 8b's lesson a second time, read at the stitcher's print); (5) CA1 retyped
(above) — a LIST literal, not a count; (6) the narrative's entities ONE, not two — a line's subject makes no entity, a write does (the tripwire retyped from
the first assembly's print); (7) DELTA's token counts typed from the fast checker's print (one assert fell on the first pass, on the forms — the LENs); (8)
the rows thirty-two, the grades 14/12/4/1/1 (the design's twenty-nine at 12/11/4/1/1); (9) moses_pleaded_on_the_attributes' first verse is Num 14:11, not
14:13 (the callees' print — 6b's lesson a third time); (10) the readback row 9:9's note corrected by the shelf — the fasting's seat is 9:9's own (Yoma
75b:11), not supplied from 34:28; (11) rb() extended for the sixth form — a SUPPLIED row carries its WRITE, a stretch row its two markers and days; (12)
the exam's persons fifteen and two exempt (the design did not number them); (13) F2 thirteen asks, F3 eight — the docket's crowns became exam rows (the
confession specified, the calf's own day, the calf's debt, prolonging without expecting, the merit ceased); (14) the callees' two call forms settled by the
print — erection's and shemini_day's cells take a string and return a dict, the Deuteronomy runners' take a case dict; ES.trials' tuple stands for
cell_found; (15) the peril's ledger scan EXCLUDES this sitting's own effect once the fold carries it (the honest form of a hole's ground after the write);
(16) the recorder's and the stitcher's derived forms needed `import subprocess as _sp` prepended — the forms' first header line lacks it (a NameError on
the first run); (17) THREE OLDER READBACK PROBES MOVED — 4b's Q14, 5b's Q17 and 6b's Q20 hold the marker COUNT (167) as a literal beside their 'no marker in
this chapter' test: 21/24 at the first chain, retyped from the print (patch_probes167_ch9.py) — a count literal in a PROBE is the same class as one in a
checkpoint; (18) THE IMPORT CACHE'S EIGHTEENTH SLIP — ink_cache_probes C2 fell on `_SRC` in every runner that reads cold_run_sequence.py at import (the INK
block, the stitcher's way): the cache keyed those modules on their own source and the shared files, and after the tape was re-stitched it restored the OLD
text of the sequence file; the fix (patch_ink_cache_key_ch9.py): the sequence file's digest joins the key of every module whose source names it — those
re-harvest once per tape change, the others keep their blobs (FORM unmoved); (19) YAML's FALSE is a boolean — the dispositions script's own assert fell on
it after the rows were written (4b's lesson a second time), retyped; (20) A CHAIN RERUN THAT INCLUDES THE PROBES STEP STARTS AT THE TAPE — the second pass
(--from probes) found ink_cache 8/8 and the dependency gate GREEN but the readback probe crashed on a missing live journal (the tape step writes it, the
journal gate consumes it): 6b's second pass had started at the dependency step and never showed it; the third pass ran the whole chain; (21) THE THIRD PASS
KILLED at the positions table (eight workers, each the whole tape) by the session's memory watchdog — not the machine's own gate: every step to the register
gate GREEN in that pass (tape, the thirteen probe suites, daemon, dependency, build, journal, register); the fourth pass from the positions table was killed
at the same step (eight workers, each the whole tape — the machine at 48 GB with the session beside it), so the positions table was measured by FOUR workers with
the step's own command (`checkpoint_positions.py --jobs 4`, its print in the chain's folder) and the fifth pass from the checkpoint probe finished the chain
(checkpoint, stamp, sweep, journal again, unmoved). THE CHAIN RUN FIVE TIMES: the first stopped at the probes step (readback 21/24 — the three
older probes; ink_cache 7/8 — C2) and the dependency gate by THREE demands — two EDGES the token census matched on HOMOGRAPHS (not_righteousness -> chatat at
9:16, 9:18, 9:27: the chapter's 'your sin' the calf's, not the SIN OFFERING's; -> family at 9:26, 9:29: 'Your inheritance' Israel as the LORD's own, not the
inheritance LAW's transfer) filed FALSE with their whys (5b's Molech/king form), and ONE POINTER at Deut 9:3 in the AS_WHEN form ('as the LORD has spoken to
you') dispositioned RUN_CITATION of the dispossession's word (7:1-2, 7:22-24; Exodus 23:23-30 — seven_nations by CALL) — add_dispositions_ch9.py, the tokens
checked on the DB; the design's 'as at the first' (9:18) demanded nothing; the second chain from the probes step — ink_cache 8/8, the dependency gate GREEN, the
readback probe without its live journal; the third chain whole — GREEN to the register gate, killed at the positions table by the memory watchdog; the fourth
from the positions table killed there again; the positions by four workers outside the script; the fifth from the checkpoint probe — ALL GREEN over the three.

THE LESSONS (fifteen, for the next compile): (1) THE RECORDER RUNS WITH THE CACHE OFF — a module restored from the cache never submits: any instrument that
captures a scene's submits needs INK_CACHE=0 (the sweep's and --full's way; a new consumer of the native path, owed to GATES_CHAIN.md's D38 list); (2) the
probes' FAIL run precedes the types — every reader of the world asserts the daemon order against the dispositions, so the types must wait for the probes'
print (6b's order held for a reason); (3) A LITERAL THAT LISTS THE MARKERS MOVES AS SURELY AS ONE THAT COUNTS THEM — before the tape, grep the marker VERSES
in the older checkpoints, not only 'markers N' (the count-literal lesson's fourth class: closes, debits, a status, now a list); (4) the line at the marker's
own verse takes the marker's class (8b's rule, now for a retrograde Deuteronomy line) — the placement is read, never predicted page_order; (5) a line's
subject makes no entity, a write does; (6) THE SIXTH FORM HELD — a stretch is graded against the clock: the markers' days on the running world (DA4, Q22),
the bare world's arithmetic (the runner's CLOCK) and Ta'anit 28b:9's own count agree; the clock read back is a compile rule's test; (7) the docket names the
effect — destruction_halved from the row's own words, the design's provisional name superseded before the types; (8) the callees' print settles the call
forms and the first verses before an assert is typed; (9) a design's tape verse is the LINE's first verse (14:11); (10) the sixth form's SUPPLIED row is
T2's — an act told only in the retelling, written once at its own day by a retrograde marker WITH its write — and the hole's ground (the scan) must
exclude the write once the fold carries it; (11) the stitcher's with_placement() adds the kwarg — an mk code carries none; (12) a count literal in a PROBE moves like one in a checkpoint — the older chapters' 'no marker' probes hold the tape's marker count: grep the probes too
before the chain; (13) THE CACHE'S KEY COVERS EVERY FILE A MODULE READS AT IMPORT — the sequence file was the one left out (its eighteenth slip, found by C2
as the honesty guards were built to find it: nothing set aside); (14) a chain rerun that includes the probes step starts at the tape — the probes read the
tape's live journal and the journal gate consumes it (--from a later step is the only short cut); (15) THE TWO-RUN RULE HELD ON ITS
SECOND COMPILE SITTING — RUN A the design (a clean point), the docket its own run in the same window on the owner's word (a clean point), RUN B this (the
probes, the types, the callees, the runner in parts with the fast checker, the cases, the recorder and the stitcher twice, the literals, the tape twice, the
checkpoint check, the chain five times, the records in one call) — the D series opened at DA1-DA9.
""" % (CASES_N, CASES_N, CASES_N, PER_CELL, CENSUS, tape_elapsed, 'ALL GREEN', gates_line, pr_line, docket_line, REC_N)

# ---- 2. COMPILE_DEBT — the sitting-7 box marked PAID + the 7b box ----
DEBT_HDR_OLD = "## SITTING 7 — CHAPTER 9 (2026-09-19, the reading; deu_09_not_righteousness frozen) — OWED TO THE COMPILE 7b: (a) THE READBACK'S ROWS OF THE CALF"
DEBT_HDR_NEW = "## SITTING 7 — CHAPTER 9 (2026-09-19, the reading; deu_09_not_righteousness frozen) — PAID AT 7b (the 7b box below, item by item) — AS WRITTEN AT THE READING, OWED TO THE COMPILE 7b: (a) THE READBACK'S ROWS OF THE CALF"
DEBT_BOX = """
## DEUTERONOMY SITTING 7b — THE COMPILE OF CHAPTER 9 (2026-09-19; DEUTERONOMY_WALK.md "Sitting 7b" design + THE DOCKET — AS RUN + AS BUILT; logic/oral_triage/deu_09_ekev_exam_2026-09-19.md
## %d rows, every row read whole from the start; cold_run_not_righteousness.py %d/%d; law_not_righteousness the 69th daemon; the tape 10/10 with RUN (1311, 96, 88, 0, 12, 1606, 40, 319, pairs, 127)).
## THE SITTING-7 BOX (a)-(j) PAID — (a) THE READBACK'S ROWS OF THE CALF — F2 and F6: thirty-two rows against the erection runner's lines (calf_made, moses_interceded twice,
## tablets_broken, calf_destroyed, moses_ascended) and its cells by CALL; 9:13 VERBATIM (eleven of thirteen), 9:12 VARIANT, 9:9 and 9:18 EXPANDED as STRETCHES (the sixth
## form), 9:21 VARIANT (the fourth verb dropped), 9:17 EXPANDED (the breaking approved at three seats), 9:19 TURNED; (b) AARON'S PERIL (9:20) — F4: the RETROGRADE WRITE at
## the morrow of the breaking (1, 4, 18) — the line prayed_for_aaron, the status destruction_halved on aaron (Vayikra Rabbah 10:5), the stretch ended at 9:21; (c) THE
## STATE "stiff-necked" — F1 stiff_necked: NOTHING on the tape — a state in the first telling, no write, the scan empty at build and at DA6; the six seats a DATA row; (d)
## THE THREE FORTIES — F3: the clock's markers (1, 3, 7) → (1, 4, 17) → (1, 4, 18) → (1, 5, 29) → (1, 7, 10), the stretches 40 / 40 / 40 measured on the running world (DA4,
## Q24) and on the runner's bare world; Ta'anit 4:6 MATCH, 28b:9's 24 + 16 reproduced; Shabbat 88a:3's two arms recorded; the second ascent's date OPEN; (e) THE FOUR
## PROVOCATIONS — F5: the rows 9:22 (three) and 9:23 (two) against fire_of_the_lord_burned, named (Exod 17:7), quail_and_plague, congregation_wept by kind and the kin's cells
## by CALL, out of the tape's order (a DATA row); TABERAH NOT AMONG THE TEN TRIALS (a DATA row); (f) THE INTERCESSION'S SECOND TELLING — F6: 9:26-29 against moses_interceded
## (32:11-14) and moses_pleaded_on_the_attributes (Num 14:11-19); the three swaps and the taunt's four forms DATA rows; Solomon and Nehemiah a DATA row; the merit of the
## fathers a PARAMETER (two arms, four dates) with two exam persons; (g) THE OFFER'S THREE FORMS — a DATA row, the offer fulfilled outside the Torah (Berakhot 7a:35-36);
## (h) THE THREE SPELLINGS OF "TABLETS" — a DATA row (the erection's count by CALL); (i) THE CHECKPOINT PREFIX SPACE — THE D SERIES OPENED, DA1-DA9 (measured at the design,
## no code assuming a letter); (j) THE DOCKET — %d rows by the union rule, EVERY ROW WHOLE FROM THE START (its own run in RUN A's window). OWED FROM 7b: (i) THE FRAGMENTS
## IN THE ARK — 10:1-5's line at chapter 10's compile writes the fragments' entry (Menachot 99a:12; Bava Batra 14b:4-7; erection.tablets('fragments_by_call') = both_in_the_ark;
## the tape's testimony_placed at 40:20 holds tablets_delivered on the ark); (ii) THE CALF'S OWN DAY — the marker at the sixteenth of Tammuz (Shabbat 89a:6, the fortieth
## day's sixth hour; the ascent + 39) ON THE OWNER'S WORD: the tape's calf_made and the first intercession sit on the ascent's day (1, 3, 7) unmarked; (iii) THE SECOND
## ASCENT'S DATE — the machine's 29 Av against the tradition's 1 Elul (two days by the calendar): the parameter's own open row, Seder Olam Rabbah 6 unreachable in the
## export; (iv) 10:10's forty (the third forty's end on 10 Tishri — CAL_PARAMS second_tablets_given) and 10:4's "the ten words" at chapter 10, citing 9:9-11 by CALL;
## (v) THE RECORDER RUNS WITH THE CACHE OFF and THE CACHE'S EIGHTEENTH SLIP (the sequence file in the key) — GATES_CHAIN.md's D38 note (paid in this sitting's records);
## (vi) 10:12's "what does the LORD your God ask of you" (6b's owed item, unchanged); (vii) the crowns of Horeb (Exodus 33:1-6 — no line) and the three requests (33:12-23 —
## no line) named as holes outside this chapter's span — an Exodus 33 sitting's, if ever; (viii) THE OWNER'S WORD ON THE SUPPLIED-WITH-A-WRITE form — the sixth form's
## decision 1 (an act told only in the retelling written at its own day) stands as the design's, the retelling rules' own; ON THE TABLE with the fifth form's SUPPLIED.
## NOTHING ELSE IN CHAPTER 9 IS OWED TO A LATER SITTING OF ITS OWN.
""" % (NROWS, CASES_N, CASES_N, NROWS)

# ---- 3. MIDDOT — the compile's entry (the docket's entry stands from its own run; this the runner's use of the codes — every code checked in this file's own lists) ----
MIDDOT_ANCHOR = "\n## Exodus block campaign — owner's word \"Do 3\")\n"
MIDDOT_ENTRY = """- THE CHAPTER-9 COMPILE (THE DEUTERONOMY WALK sitting 7b RUN B, 2026-09-19; cold_run_not_righteousness.py — the docket's rules carried into the cells' asks, each
  code checked in this file's lists before it was typed):
  · THE A-FORTIORI (I1, qal wa-chomer) at four seats the cells cite — Shabbat 87a:5 (F2 the_breaking_in_my_own_words: from the Paschal lamb's "no alien shall eat" to the
    tablets and the apostates — Moses' own reasoning, ratified "may your strength be true"); Berakhot 32a:17 (F2 let_me_alone, F6 remember_your_servants: the three-legged
    chair against the one leg); Yoma 75b:11 (F3 bread_i_did_not_eat: from the man who ascends on high and does not eat to the angels — FROM 9:9 ITSELF, the fasting's seat
    this chapter's own); Arakhin 15a:11 (F5 — the spies' se'ah, credited).
  · THE VERBAL ANALOGY (I2, gezerah shavah) at two seats — Berakhot 32a:19 (F6 do_not_destroy_your_people: vayechal / "he shall not profane [yachel] his word", Numbers 30:3
    — the vow annulled by the vows' own law, the intercession's mechanism); Berakhot 7a:36 (F2 let_me_alone: "were very many" / "were very many" — Rehaviah's sons more
    than 600,000, the offer of 9:14 FULFILLED outside the Torah).
  · THE PARABLE (E26, mashal) at Berakhot 32a:9-11 and 32a:15 (F2 gods_word_verbatim: the well-wisher's parable on "leave Me be" — the matter depends on Moses).
  · THE "DO NOT READ" READINGS NAMED, NO CODE — Shabbat 89a:6 (F2 the_calfs_own_day: boshesh read ba'u shesh, the sixth hour — the OPEN row's shelf source); Berakhot 32a:5
    (F5 taberah: "to" [el] read "onto" [al] — Moses' impertinence); Shabbat 55a:9 (F6: the letter tav's readings behind the merit of the fathers' two arms).
  · THE CLOCK READ BACK AS A COMPILE RULE'S TEST (no middah — the machine's own): Ta'anit 28b:9's "twenty-four days remaining in Sivan plus the first sixteen of Tammuz
    = forty" is an ARITHMETIC RULE on the calendar; the tape's markers reproduce it by the calendar's own month lengths (Sivan thirty that year) — the sixth form grades a
    stretch against the rule's arithmetic and the answer sheet's date (Mishnah Ta'anit 4:6) at once: MATCH; the two arms of the giving's day (Shabbat 88a:3) a PARAMETER
    recorded, R. Yosei's the tape's.
  · THE HYPERBOLE RULE (a reading rule on the code's own words — Rabban Shimon ben Gamliel at Chullin 90b:12, Tamid 29a:8, the Sifrei 25:4): "fortified to the heavens"
    (9:1) an exaggeration, not a height — the parser's silence on the phrase its own witness (F1 fortified_to_the_heavens).
  · A DISPUTE'S HINGE ON AN OMISSION (Mishnah Avodah Zarah 3:3; Avodah Zarah 44a:1-2; Tosefta 4:3 — F2 the_calf_ground_to_dust): R. Yosei's proof from the RETELLING'S verbs
    (9:21 — grind and scatter), the Rabbis' from the FIRST TELLING'S fourth verb (32:20 — the drinking, a test as the sotah's) which the retelling DROPS: the readback's
    VARIANT grade is the dispute's ground; the ruling the Rabbis' (the tape's calf_destroyed purpose to_test).
  · HALF THE EDICT (Vayikra Rabbah 10:5 — F4 half_the_edict): "destruction" DEFINED as the eradication of children by Amos 2:9 (a definition by a proof-text), the edict on
    Aaron's four sons halved by prayer — TWO DIED AND TWO REMAINED: the effect's NAME taken from the row's own words (destruction_halved), the dispute's other arm (R.
    Yehuda: prayer all, repentance half) recorded.
  · A PARAMETER WITH TWO ARMS AND FOUR SETTINGS (Shabbat 55a:11, 55a:13-16 — F6 remember_your_servants, the_merit_ceased): the merit of the fathers ceased (Shmuel) or
    stands (R. Yochanan); from when — Hosea's, Hazael's (2 Kings 13:23 the last mention), Elijah's, Hezekiah's days: two exam persons, one accepted and one exempt.
  · THE FEMININE NOUN KEPT (Berakhot 32a:27 — F6 lest_the_land_say): "not the ABILITY [yekholet] of the LORD" (Numbers 14:16) where "was not able" was expected — the
    retelling keeps the noun's form at 9:28 (מבלי יכלת); a grammar rule read as the taunt's content.
  · "AT THAT TIME" A TIME ORDAINED FOR CALAMITY (Sanhedrin 102a:5 — F4 at_that_time): R. Yosei's seats of the phrase — the marker's placement word read by the shelf.
""" % ()

# ---- 4. MISHNAH_TOPICS — the rows touched by the compile (the docket's own notes stand on five rows from its run) ----
DKF = "deu_09_ekev_exam_2026-09-19.md"
TOPIC_NOTES = {
 "**1. Mishnah, Blessings**": " — Berakhot 32a-32b, 7a READ WHOLE and 34a:11 READ 2026-09-19 (%s: the intercession's rules — the seizing, the three-legged chair, the vow annulled, the oath by the Name, the taunt's feminine noun, the concession; every promise of good fulfilled — 9:14's offer in Rehaviah's sons; the forty days as the measure of prayer and its guard, 9:18, 9:25; Taberah's impertinence, 9:22; the calf's cause conceded — %s; the cells F2, F3, F5, F6)" % (W7, DKF),
 "**12. Mishnah, Sabbath**": " — Shabbat 87a-89a and 55a READ WHOLE 2026-09-19 (%s: the breaking approved — Moses' own a fortiori, 9:17; the giving's day's two arms, 9:9; the crowns of Horeb stripped with no line, 9:8; the bride under her canopy and the calf's own day and hour (boshesh), the OPEN row; the merit of the fathers a parameter with four dates, 9:27; the one retraction — %s)" % (W7, DKF),
 "**14. Mishnah, Passover**": " — Pesachim 87b:22 READ 2026-09-19 (%s: the letters flying back at the breaking, 9:17)" % W7,
 "**18. Mishnah, Festival Day**": " — Beitzah 25b READ WHOLE (sixteen rows) 2026-09-19 (%s: the Torah given because they are impudent — the stiff neck as the reason for the Torah, 9:6; the three impudent ones; F1's exam row)" % W7,
 "**26. Mishnah, Vows**": " — Nedarim 32a:4 and 38a:8 READ 2026-09-19 (%s: the anger and the wrath's two nouns, 9:19; Moses' might from 9:17's own verbs — the tablets six by six by three)" % W7,
 "**33. Mishnah, Last Gate**": " — Bava Batra 14b READ WHOLE (twelve rows) and 9b:7 READ 2026-09-19 (%s: the fragments in the ark — both sets, 10:2 forward; the breaking's third seat of one rule, 9:17; charity in secret greater than Moses' fear, 9:19)" % W7,
 "**34. Mishnah, Courts**": " — Sanhedrin 102a READ WHOLE (eighteen rows) 2026-09-19 (%s: 'at that time' a time ordained for calamity, 9:20; the calf's surcharge — one twenty-fourth in every punishment, its collection after twenty-four generations; Israel suckling from one calf)" % W7,
 "**42. Mishnah, Grain Offerings**": " — Menachot 99a-99b READ WHOLE (thirty-five rows) 2026-09-19 (%s: the fragments in the ark, 10:2 forward; the breaking's second seat — 'your strength is true', 9:17; the Torah given in forty days as the soul is formed in forty)" % W7,
 "**43. Mishnah, Slaughter**": " — Chullin 90b:12 READ 2026-09-19 (%s: the hyperbole rule — 'fortified to the heavens', 9:1)" % W7,
 "**45. Mishnah, Valuations**": " — Arakhin 15a READ WHOLE (twenty-one rows) 2026-09-19 (%s: the ten trials — Massah, Kibroth, the calf and Kadesh among them, TABERAH NOT, 9:22-23; the sentence sealed for the spies' speech, 'now ten times'; the trials' seats)" % W7,
 "**49. Mishnah, Daily Offering**": " — Tamid 29a:8 READ 2026-09-19 (%s: the hyperbole rule's second seat, 9:1)" % W7,
}

# ---- 5. RESEARCH_LOG ----
RLOG = """

## 2026-09-19 — DEUTERONOMY 9 COMPILED (THE DEUTERONOMY WALK sitting 7b — CHAPTER 9): THE READBACK'S SIXTH FORM — THE RETELLING OF A STRETCH; THE CLOCK READ BACK
## AGAINST THE ANSWER SHEET'S OWN ARITHMETIC; AARON'S PERIL WRITTEN ONCE AT ITS OWN DAY WITH A WRITE NAMED BY THE SHELF; THE RECORDER RUNS WITH THE CACHE OFF

THE READBACK OF A STRETCH. Chapter 9 is Moses telling the calf in his own voice, so its rows are reference rows against the tape's Exodus 24-34 and Numbers 11-14
lines and the kin's cells by CALL — thirty-two rows, VERBATIM 14 / VARIANT 12 / EXPANDED 4 / TURNED 1 / SUPPLIED 1: God's word comes back VERBATIM (9:13 eleven of
thirteen tokens with Exodus 32:9), Moses' acts in his own words (9:17 one token shared with 32:19 — the breaking approved at three seats of the shelf), the calf's
destruction without its fourth verb (9:21 — the drinking dropped, the dispute's hinge). And a row-kind no chapter had: "forty days and forty nights" told at 9:9,
9:11, 9:18 and 9:25 is not a line but a STRETCH between two of the tape's markers, graded against THE CLOCK'S OWN ARITHMETIC — the ascent (1, 3, 7) to the breaking
(1, 4, 17) is forty by the calendar, Ta'anit 28b:9's "twenty-four days of Sivan plus sixteen of Tammuz" reproduced by the machine's month lengths; the morrow
(1, 4, 18) to the second ascent (1, 5, 29) is the forty Exodus never gives and the retelling supplies; the second ascent to the last tablets on 10 Tishri the
third, next chapter's. The answer sheet's date (Mishnah Ta'anit 4:6, the seventeenth of Tammuz) was already the tape's: MATCH — asserted on the running world's
markers (DA4, Q22, Q24) and on the runner's bare world alike. AARON'S PERIL (9:20) is told only here — Exodus has Aaron's report and the plague, no anger at
Aaron, no prayer for him — the tape's hole, filled with a write: the act prayed_for_aaron written ONCE at its own day by a retrograde marker at Deut 9:20 (the
morrow of the breaking — "at that time" the second forty's ascent), the status destruction_halved on aaron NAMED BY THE DOCKET (Vayikra Rabbah 10:5: destruction
is the eradication of children; since Moses prayed, half the edict was withheld — two died and two remained, both halves already on the tape), the stretch
ended by a forward marker at 9:21. THE STIFF NECK a state in the first telling — no write, the scan empty at build and on the running world. THE SHELF'S FINDS
THE DESIGN DID NOT PREDICT: Taberah is NOT among the ten trials (Arakhin 15a:14) though the retelling names it first; the fasting's seat is 9:9's own (Yoma 75b:11
cites this verse, not 34:28); the merit of the fathers is a PARAMETER with two arms and four dates (Shabbat 55a:11-16 — 2 Kings 13:23 the last mention); the calf
is forbidden from its making (52a:4 — the tape's worshipped=False with its row); the crowns of Horeb stripped (Shabbat 88a:7 — Exodus 33:6) and Moses' three
requests (Berakhot 7a:23-25 — 33:12-23) have NO LINE on the tape; Aaron's report is read and not translated while the retelling of his peril is (Mishnah
Megillah 4:10's asymmetry). THE MACHINE'S LESSONS: THE RECORDER RUNS WITH THE CACHE OFF — a module restored from the import cache never runs its scene, so the
recorder captured 118 submits of 2,983 and the stitcher wrote a truncated tape (rerun native, 1,682 lines); the line at the marker's own verse takes the marker's
class (reading_placed, not page_order — the placement read at the stitcher's print); an older checkpoint that LISTS the Deuteronomy markers as a literal (CA1)
moved with the new marker — the count literals were retyped as the design said, the list literal read from the tape's first print (9/10). THE NUMBERS:
cold_run_not_righteousness.py the 64th runner %d/%d on its first graded run; the tape 10/10 on its second (the first 9/10, CA1); RUN (1311, 96, 88, 0, 12, 1606,
40, 319, the four pairs, 127) as predicted; markers 167 -> 169; kinds 1135, effects 1032, daemons 69, eleven CALL edges; the docket %s; every gate green in one
chain's third to fifth passes (the first stopped at three demands — two homograph edges filed FALSE, one pointer a run citation — and at three older probes holding the
marker count; the second, from the probes step, at the readback probe without the tape's live journal; the third green to the register gate and killed at the positions table by
the session's memory watchdog, the fourth killed there again, the positions then by four workers and the fifth finishing from the checkpoint probe; the sweep %d/63; the import cache 8/8 after its eighteenth slip was keyed — the sequence file a runner reads at import). THE TWO-RUN RULE'S SECOND COMPILE SITTING: RUN A the design, the docket its own run
in the same window on the owner's word, RUN B the build after one compaction — three clean points.
""" % (CASES_N, CASES_N, docket_line, SW_P)

# ---- 6. THE_STEPS ----
STEPS_ANCHOR = "\n## Step 6 — Publish\n"
STEPS_PARA = """
DEUTERONOMY — SITTING 7b — CHAPTER 9 COMPILED (2026-09-19, on Brian's "Ok do ch 9" for the design, "Go" for the docket and "Go" for the build after a compaction;
World/step9/DEUTERONOMY_WALK.md "Sitting 7b", "THE DOCKET — AS RUN" and "Sitting 7b — AS BUILT"). Chapter 9 is Moses telling the golden calf again in his own
words, so this sitting graded each sentence of his telling against the tape's own line from Exodus or the older cell that compiled it: God's words come back
word for word, Moses' own acts come back rephrased, and the calf's destruction comes back without the drinking — which is exactly the detail the sages argued
over. Three times the chapter says "forty days and forty nights", and that is not an event but a stretch of the clock between two of the tape's date marks.
So the machine measured the stretches on its own calendar: the day Moses went up to the day the tablets broke is forty; the day after the breaking to his
second ascent is forty; and the Talmud's own count — twenty-four days left in Sivan plus sixteen of Tammuz — comes out of the calendar unprompted, landing
on the seventeenth of Tammuz the Mishnah names. One thing in the chapter is told nowhere else: God's anger at Aaron and Moses' prayer for him. That act was
written back once into Exodus's own day, the day after the breaking, and the ledger entry it writes took its name from the Talmud's midrash — half the
edict withheld, two of Aaron's sons died and two lived. The reading of the shelf, four hundred rows read whole, corrected the design in small ways: the
fasting's proof-text is this chapter's own verse; Taberah, the first provocation the chapter names, is not among the ten trials the sages count; the merit
of the fathers is a disputed parameter with four dates for when it ran out. The machine learned one rule of its own: the instrument that records the runners'
scenes must run with the new import cache off, because a runner restored from the cache never re-runs its scene. The runner matched its sheet on the first run;
the tape reached ten of ten on the second; every gate was green over the chain's third to fifth passes — the first asked for three dispositions (two look-alike words the census matched to other laws, one citation) and
found three older checks and the cache holding stale counts and text, each retyped from its print; the second, started past the tape, showed that the checks
which read the tape's own record need the tape run first; the third was cut off by the session's memory watchdog after seven green steps, the fourth at the same eight-worker step, and the table was then measured by
four workers and the fifth pass finished the rest. Next: the commit on your word; then chapter 10's reading.
"""

# ---- 7. THE_BRIEFING ----
BRIEF_BULLET_ANCHOR = "- **CHAPTER 9 READ AND FROZEN — THE CALF RETOLD:"
BRIEF_BULLET = ("- **CHAPTER 9 COMPILED — THE RETELLING OF A STRETCH: FORTY DAYS IS NOT AN EVENT BUT A SPAN OF THE CLOCK, AND THE TALMUD'S OWN COUNT COMES OUT OF THE CALENDAR; AARON'S PERIL WRITTEN ONCE INTO EXODUS'S OWN DAY, ITS EFFECT NAMED BY THE MIDRASH; THE SCENE RECORDER MUST RUN WITH THE CACHE OFF** "
                "(2026-09-19, on your \"Ok do ch 9\", \"Go\" and \"Go\"; World/step9/DEUTERONOMY_WALK.md \"Sitting 7b\" + THE DOCKET — AS RUN + AS BUILT): cold_run_not_righteousness.py the 64th runner (%d/%d), law_not_righteousness the 69th daemon (%d functions); the readback's sixth form thirty-two rows, four stretches, one SUPPLIED with a write; the tape 10/10 with RUN (1311, 96, 88, 0, 12, 1606, 40, 319, pairs, 127) as predicted, markers 169; the docket %d rows every row whole; every gate green over the chain's third to fifth passes, the sweep %d/63; the two-run rule's second compile sitting, three clean points.\n" % (CASES_N, CASES_N, DG[1], NROWS, SW_P))
BRIEF_ENTRY_ANCHOR = "### 2026-09-19 — CHAPTER 9 READ: THE CALF TOLD TWICE, AND WHAT THE SECOND TELLING ADDS\n"
BRIEF_ENTRY = """### 2026-09-19 — CHAPTER 9 COMPILED: A STRETCH OF THE CLOCK, AND A PRAYER WRITTEN INTO THE PAST

The machine has graded retellings four ways before — against the tape's own lines, against an older law's cell, inside a law, and, last chapter, a state
with no day. Chapter 9 needed a fifth thing. Three times Moses says "forty days and forty nights". That is not an act the tape can hold as a line; it is a
stretch of the calendar between two marks the tape already carries — the day he went up, the day the tablets broke, the day after, the day he went up again.
So the sitting measured the stretches on the machine's own calendar and graded them against what the sages say. The Talmud's count is explicit: twenty-four
days remaining in Sivan and the first sixteen of Tammuz make forty, and the tablets broke on the seventeenth. The calendar, asked for the days between the
two marks, gives forty; asked for the month's length, gives thirty; the seventeenth of Tammuz is the Mishnah's date and it was already the tape's. Match.
The second forty is a stretch Exodus never states at all — it says only "on the morrow Moses returned" — and the retelling supplies it; the machine holds it
as the span from the morrow to the second ascent, forty exactly. The third forty ends on the Day of Atonement and belongs to the next chapter. One sentence in
the chapter is told nowhere else: the LORD was very angry with Aaron, to destroy him, and I prayed for Aaron also at that time. Exodus has Aaron's excuse and
the plague; it has no anger at him and no prayer for him. So that act was written once into Exodus's own day — the day after the breaking, when Moses went
back up — and the entry it writes on Aaron took its name from the midrash rather than from the design: destruction is the eradication of children, and since
Moses prayed, half the edict was withheld; two of Aaron's sons died at the eighth day and two lived to succeed him, and both halves were already on the
tape. The shelf, read whole, corrected the design three times: the proof that Moses fasted on the mountain is this chapter's own verse, not Exodus's;
Taberah, which the chapter names first among the provocations, is not one of the ten trials the sages count; and whether the merit of the fathers still
stands is a dispute with four proposed dates for its ending, the last a verse in Kings. The machine learned one rule about itself. The instrument that
records every runner's scene for the tape ran under the new import cache and captured almost nothing, because a runner restored from the cache never
re-runs its scene; the tape it stitched was a stub. It was rerun natively and the tape came back whole. That rule is now written where the cache is
described. The runner matched its sheet on the first run; the tape reached ten of ten on the second, one old check having listed the book's date marks by
name and grown by one; the chain's first pass asked for three dispositions and caught three older checks and the cache's own key holding stale counts and text — each retyped from its
print — its second pass, started past the tape, showed that the checks which read the tape's own record need the tape run first; its third pass was green through seven steps and cut off by the memory watchdog, its fourth cut off at the same eight-worker step, the table then measured by
four workers and the fifth pass finishing the rest. Next, on your word: the commit, then chapter 10.

"""

# ---- 8. THE_LOOP step-6 row ----
LOOP_OLD = "readback_probes 21/21, CU4) | the four forms BUILT — acts (1b), laws (3b, and on the kin 5b), a retelling inside a law (4b), a STATE (6b); the second pass after Deuteronomy |"
LOOP_NEW = ("readback_probes 21/21, CU4); cold_run_not_righteousness.py (chapter 9, THE SIXTH FORM — THE RETELLING OF A STRETCH 2026-09-19: the calf retold in Moses' own voice graded against the tape's Exodus 24-34 and Numbers 11-14 lines and the kin's cells — thirty-two rows VERBATIM 14 / VARIANT 12 / EXPANDED 4 / TURNED 1 / SUPPLIED 1; 'forty days and forty nights' (9:9, 9:11, 9:18, 9:25) a STRETCH between two markers graded against THE CLOCK's own arithmetic and the answer sheet's date (Ta'anit 28b:9's 24 + 16 reproduced; Mishnah Ta'anit 4:6 MATCH — DA4, Q22, Q24); Aaron's peril (9:20) SUPPLIED WITH A WRITE — the retrograde marker at Deut 9:20, the line prayed_for_aaron, the status destruction_halved named by the docket; THE RECORDER RUNS WITH THE CACHE OFF; "
            "readback_probes 24/24, DA3) | the five forms BUILT — acts (1b), laws (3b, and on the kin 5b), a retelling inside a law (4b), a STATE (6b), a STRETCH (7b); the second pass after Deuteronomy |")

# ---- 9. RESUME ----
RESUME_HEAD = """# ⚠ THE DEUTERONOMY WALK sitting 7b (2026-09-19; step9/DEUTERONOMY_WALK.md "Sitting 7b" + "THE DOCKET — AS RUN" + "Sitting 7b — AS BUILT"): CHAPTER 9 COMPILED —
# step9/cold_run_not_righteousness.py the 64th runner (%d/%d; six cells; THE READBACK'S SIXTH FORM — the retelling of a STRETCH: thirty-two rows, twenty-two on the
# tape, nine by CALL, four STRETCH rows measured on the clock (the three forties 40 / 40 / 40 — Ta'anit 28b:9's 24 + 16 reproduced, Mishnah Ta'anit 4:6 MATCH), ONE
# SUPPLIED WITH A WRITE (9:20 Aaron's peril)), law_not_righteousness the 69th daemon (given_at Deut 9:1, boot); ONE LINE prayed_for_aaron dated (1, 4, 18) by the
# RETROGRADE marker at Deut 9:20 (M['aaron_told'] = M['morrow']), the forward marker at 9:21 — destruction_halved a STATUS on aaron (the name from Vayikra Rabbah
# 10:5); the tape 10/10 on its second run with RUN (1311, 96, 88, 0, 12, 1606, 40, 319, pairs, 127) as predicted, PREVIOUS_RUN 6b's exactly, markers 169, closes
# 127 (CA1 — the markers' list literal — retyped; the nine 'markers 167' counts retyped as designed); the docket %d rows read whole from the start (its own run);
# every probe suite and gate GREEN over the chain's third and fourth passes (the first: three demands, three older probes, the cache's eighteenth slip; the second, from the probes step, the readback probe without the live journal — a rerun with the probes starts at the tape; the third killed at the positions table by the memory watchdog, the fourth there again, the positions by four workers, the fifth from the checkpoint probe), the sweep %d/63. ⚠ THE RECORDER RUNS WITH THE CACHE OFF (INK_CACHE=0 — a restored module never submits); the cache's key now covers the sequence file a runner reads at import.
# NEXT on the ruling: the commit on the owner's word (the cache's message and 7b's); chapter 10's reading (10:1-22) — the fragments in the ark owed to its compile.
""" % (CASES_N, CASES_N, NROWS, SW_P)

# ---- 10. THE STATE DOC — #197 ADDENDUM 5 ----
STATE_ADD = """
#197 ADDENDUM 5 (2026-09-19, at the close of THE DEUTERONOMY WALK sitting 7b — THE COMPILE OF CHAPTER 9, RUN B of two under THE TWO-RUN RULE, on the owner's "Go" after the compaction — A CLEAN COMPACTION POINT): THE SITTING RAN AS THE RULE SAYS — RUN A the rereads, the measurements and the design (#197 addendum 3), THE DOCKET its own run in RUN A's window on "Go" (#197 addendum 4), RUN B this: patch_probes_ch9.py (Q22-Q24 written to FAIL before the runner — the FAIL print a REFUSAL at the daemon assertion, the types having run first: ch9b_probes_fail.out), add_types_ch9.py (kinds 1135 — prayed_for_aaron an ACT, not_righteousness_case; effects 1032 — destruction_halved a status on aaron, THE NAME FROM THE DOCKET; the daemon law_not_righteousness the 69th; the functions block; the span and ELEVEN CALL edges; I5 69), ch9_callees.py (every CALL's facts printed before an assert — the two call forms, the tape lines' first verses: moses_pleaded_on_the_attributes at Num 14:11), the runner in three parts with the fast checker (one assert fell on the first pass — DELTA's token counts, retyped from the print), the CASES generated (%d, per cell %s) and frozen under the guard, cold_run_not_righteousness.py %d/%d ON ITS FIRST GRADED RUN (the scene fifteen persons, two exempt, no lashes; the narrative 1 write, one entity, one dated line — the entity count retyped from the first assembly's print), the recorder and the stitcher TWICE — the first under THE IMPORT CACHE recorded 118 submits (a restored module never runs its scene) and the stitcher wrote a 241-line tape before its prediction step fell on a repeated placement kwarg; the second native (INK_CACHE=0; %d records; the tape 1,682 lines; the two markers at Deut 9:20 and 9:21 in the MK list; PLACEMENT read — the line at the marker's own verse takes the marker's class, reading_placed 56, page_order 1146 unmoved; CENSUS %s as predicted), patch_seq_literals_ch9.py (RUN, PREVIOUS_RUN 6b's exactly, NEWEST_RUNNER, PLACEMENT and CENSUS read from the stitcher's print, DA1-DA9 — THE D SERIES OPENED, the VERDICTS entries, the nine 'markers 167' literals retyped to 169 with CP6's 129 -> 130), THE TAPE 9/10 ON ITS FIRST RUN — DA1-DA9 all MATCH, THE REST OK, the one miss CA1: chapter 1b's LINES checkpoint holds THE DEUTERONOMY MARKERS' LIST as a literal — retyped from the print (patch_ca1_ch9.py: the seventh retrograde marker (1, 4, 18) at 9:20, the fifth forward at 9:21) — 10/10 ON THE SECOND RUN (%s s) with RUN (1311, 96, 88, 0, 12, 1606, 40, 319, the four pairs, 127) as the design's arithmetic wrote it; checkpoint_check.py --all after the tape (262 rows, the eighteen known diverges); THE GATES CHAIN TWICE — the first stopped at the probes step (readback 21/24: 4b's Q14, 5b's Q17 and 6b's Q20 hold the marker count 167 as a literal — retyped 169; ink_cache 7/8: C2 on `_SRC` — THE EIGHTEENTH SLIP, a runner that reads the sequence file at import restored its old text after the re-stitch: the sequence file's digest joins those modules' key, patch_ink_cache_key_ch9.py) and at the dependency gate by THREE demands (two homograph EDGES — chatat on 'your sin', family on 'Your inheritance' — filed FALSE; one POINTER at 9:3 AS_WHEN a RUN_CITATION of the dispossession's word; add_dispositions_ch9.py, whose own assert fell on YAML's boolean FALSE and was retyped), the second from the probes step — ink_cache 8/8 and the dependency gate GREEN, the readback probe crashed on the missing live journal (the tape writes it, the journal gate consumes it: A RERUN WITH THE PROBES STARTS AT THE TAPE), the third whole — GREEN to the register gate (the thirteen probe suites among them), KILLED at the positions table by the session's memory watchdog (eight workers each the whole tape; not the machine's own gate), the fourth from the positions table killed at the same step, THE POSITIONS TABLE THEN BY FOUR WORKERS with the step's own command (checkpoint_positions.py --jobs 4, its print in the chain's folder), the fifth from the checkpoint probe ALL GREEN — the thirteen probe suites (%s), %s. THE READBACK'S SIXTH FORM AS BUILT: thirty-two rows VERBATIM 14 / VARIANT 12 / EXPANDED 4 / TURNED 1 / SUPPLIED 1; the four stretch rows measured on the running world's markers (40, 40; the third to 10 Tishri) and on the runner's bare world alike; Ta'anit 28b:9's 24 + 16 reproduced; the one SUPPLIED row 9:20's WITH its write, dated (1, 4, 18); the two OPEN rows (the calf's own day — Shabbat 89a:6 the marker's shelf source on his word; the second ascent's date — 29 Av against 1 Elul); the stiff neck no entry (DA6). THE RECORDS (write_ch9b_records.py from the sheet, one call): the map's "Sitting 7b — AS BUILT" (twenty departures, fifteen lessons), COMPILE_DEBT's sitting-7 box PAID + the 7b box (eight owed items — the fragments in the ark at chapter 10, the calf's own day on his word, the second ascent's date, 10:10's forty and 10:4, the recorder's rule, 10:12, the Exodus 33 holes, the owner's word on SUPPLIED-with-a-write), MIDDOT's compile entry (I1 at four seats, I2 at two, E26 at two, the al-tikrei ('do not read') rows named; the clock read back a compile rule's test), MISHNAH_TOPICS (eleven heads), RESEARCH_LOG, THE_STEPS, THE_BRIEFING (the scoreboard bullet and an entry), THE_LOOP's step-6 row (the five forms) and D38's consumers note, GATES_CHAIN.md's D38 note (THE RECORDER RUNS WITH THE CACHE OFF; the eighteenth slip), RESUME, RECORD_FORMS (the writer's pointer), this addendum, the addenda §48, the recovery page (section 2 rewritten under its cap), the memory (the walk note and the index line under 17,000). THE FORMS copied (copy_ch9b_forms.py — RUN A's, the docket's and RUN B's scripts and prints, the chain's folder). THE TREE: + cold_run_not_righteousness.py, the registries (event_vocabulary, effect_vocabulary, daemon_dispositions, dependency_dispositions), cold_run_sequence.py (the tape's one line and two markers, the literals, DA1-DA9, CA1 and the nine counts), readback_probes.py, installation_probes.py, checkpoint_positions.yaml, sweep_stamp.json, the records, the forms. NOT COMMITTED (since a985fbc): THE VERIFIED-IMPORT CACHE (the message at <scratch>/commit_msg_cache.txt) and sitting 7b whole (RUN A, the docket, RUN B) — ONE message at <scratch>/commit_msg_ch9b.txt covers both for the owner's word ("commit" = no push; "commit push" = both). NOTHING MID-FLIGHT — A CLEAN COMPACTION POINT. NEXT ON THE RULING: the commit on his word; then CHAPTER 10's reading (10:1-22) — one run; its compile owes the fragments' entry (10:1-5) and the third forty's end (10:10); THE INSTALL HYPOTHESIS, THE SUPPLIED GRADE (the fifth form's, no write) and THE SUPPLIED-WITH-A-WRITE FORM (the sixth's) on the table. POST-COMPACTION REREADS: the recovery page, the map's "Sitting 7b — AS BUILT" (the newest section — the departures and the lessons), MEMORY.md.
""" % (CASES_N, PER_CELL, CASES_N, CASES_N, REC_N, CENSUS, tape_elapsed, pr_line, gates_line)

# ---- 11. THE RECOVERY ADDENDA — section 48 ----
ADDENDA_ADD = """

## 48. ADDENDUM (2026-09-19, THE DEUTERONOMY WALK sitting 7b — THE COMPILE OF CHAPTER 9, Deuteronomy 9:1-29 COMPILED AND ON THE TAPE in two runs with the docket its own run; the owner: "Ok do ch 9", "Go", "Go"; the state doc's #197 addenda 3-5)

THE SHAPE: THE TWO-RUN RULE's second compile sitting — RUN A the rereads, the measurements (ch9_compile_recon.py, ch9_docket_scan.py, the running world's snapshot: the
clock's dates at the calf, every retold act on the tape, Aaron's peril on none; the checkpoint prefix space measured — the D series) and the design in the map; THE
DOCKET its own run in the same window on "Go" (397 rows in three parts, every row whole; deu_09_ekev_exam_2026-09-19.md — the effect NAMED destruction_halved from
Vayikra Rabbah 10:5); RUN B the build after one compaction (the probes to fail — a refusal, the types, the callees' print, the runner in parts with the fast
checker, the cases generated, the recorder and the stitcher TWICE — THE RECORDER RUNS WITH THE CACHE OFF — the literals with the D series, the tape twice, the
checkpoint check, the chain three times — three demands (two homograph edges FALSE, one pointer), three older probes' count literals, the cache's eighteenth slip (the
sequence file in the key), a rerun with the probes starting at the tape, the third and fourth passes killed at the eight-worker positions table by the memory watchdog, the table by four workers, the fifth finishing it — the records in one call, the forms) — three clean points. THE SIXTH FORM: a stretch between two markers is graded
against the clock's own arithmetic — the three forties 40 / 40 / 40, Ta'anit 28b:9's 24 + 16 reproduced by the calendar, Mishnah Ta'anit 4:6's seventeenth of
Tammuz already the tape's: MATCH (DA4, Q22, Q24); Aaron's peril (9:20) SUPPLIED WITH A WRITE — the act written once at the morrow of the breaking (1, 4, 18) by
a retrograde marker at Deut 9:20, the status on aaron, the stretch ended at 9:21; the stiff neck a state, no write. THE DESIGN'S ERRORS caught by prints: the
placement (the line at the marker's verse takes the marker's class — reading_placed, not page_order), CA1's LIST literal (9/10 on the first tape run), the
narrative's entity count, DELTA's token counts, 14:11 the line's first verse, the rows thirty-two at 14/12/4/1/1, the effect's name. THE SHELF'S UNPREDICTED:
Taberah outside the ten trials (Arakhin 15a:14), the fasting's seat 9:9's own (Yoma 75b:11), the merit of the fathers a parameter with four dates (Shabbat
55a:11-16), the calf forbidden from its making (52a:4), the crowns of Horeb and the three requests with no line (Shabbat 88a:7; Berakhot 7a:23-25), Megillah 4:10's
asymmetry. THE NUMBERS: cold_run_not_righteousness.py %d/%d; the tape 10/10 on its second run, RUN (1311, 96, 88, 0, 12, 1606, 40, 319, pairs, 127) as predicted,
markers 169; kinds 1135, effects 1032, daemons 69, eleven CALL edges; the docket %d rows; the sweep %d/63; every gate green over the chain's third to fifth passes. OWED FORWARD:
the fragments in the ark (10:1-5), the calf's own day on the owner's word (Shabbat 89a:6), the second ascent's date (29 Av / 1 Elul), 10:10's forty and 10:4,
10:12, the Exodus 33 holes, the owner's word on the two SUPPLIED forms. The records on the sheet, the forms in World/step9/forms_deuteronomy_walk/ (copy_ch9b_forms.py).
""" % (CASES_N, CASES_N, NROWS, SW_P)

# ---- 12. THE RECOVERY PAGE — section 2 rewritten; sections 4, 5, 6 retouched; the standing law's cache line touched; the cap asserted ----
def f_recovery(s):
    i = s.index('## 2. WHERE IT STANDS'); j = s.index('## 3. THE STANDING LAWS')
    sec2 = """## 2. WHERE IT STANDS (2026-09-19, after 7b; the state doc #197 addendum 5 the newest)
- NUMBERS CLOSED. DEUTERONOMY 1:1-9:29 COMPILED AND ON THE TAPE (1-7 at 29c189b, 8 at a985fbc — PUSHED; 9 at sittings 7 and 7b).
- 223 frozen units, standing 2221, hash 8b8fff1fa28953af. 64 runners, 69 daemons, %d functions; 1135 kinds / 1032 effects.
- THE TAPE at RUN (1311, 96, 88, 0, 12, 1606, 40, 319, pairs, 127), markers 169, closes 127; the sweep %d/63; every gate GREEN; the
  register gate DECLARED %d / DEBT 0. The readback's SIXTH form (7b): a STRETCH graded against the clock — MATCH; Aaron's peril
  SUPPLIED WITH A WRITE at its own day; the fifth form's SUPPLIED and the calf's day marker his decisions, open.
- Uncommitted since a985fbc: the cache and 7b; ONE message at <scratch>/commit_msg_ch9b.txt covers both.
- NEXT ON HIS WORD: the commit; then CHAPTER 10 (10:1-22) — its compile owes the fragments in the ark and 10:10's forty.

""" % (DG[1], SW_P, RG[0])
    s = s[:i] + sec2 + s[j:]
    old4 = "cold_run_<span>.py (63 runners)"; assert s.count(old4) == 1, s.count(old4)
    s = s.replace(old4, "cold_run_<span>.py (64 runners)")
    old5 = 'the newest instances: the map\'s "Sitting 7" and "Sitting 6b")'; assert s.count(old5) == 1
    s = s.replace(old5, 'the newest instances: the map\'s "Sitting 7" and "Sitting 7b")')
    old6 = "- Deuteronomy's sittings: the map; the addenda §31-46 (§39 the whole-row rule). The cost cuts: §35, §45, §47."; assert s.count(old6) == 1
    s = s.replace(old6, "- Deuteronomy's sittings: the map; the addenda §31-48 (§39 the whole-row rule). The cost cuts: §35, §45, §47.")
    old7 = "ink_cache_probes.py 8/8 in the chain; --status|--clear) — a reader takes the SNAPSHOT"; assert s.count(old7) == 1, s.count(old7)
    s = s.replace(old7, "ink_cache_probes.py 8/8 in the chain; --status|--clear; the recorder runs with it OFF) — a reader takes the SNAPSHOT")
    assert len(s.encode('utf-8')) <= 10240, ('THE RECOVERY PAGE OVER ITS CAP', len(s.encode('utf-8')))
    return s

# ---- 13. GATES_CHAIN.md and THE_LOOP — THE RECORDER RUNS WITH THE CACHE OFF (a consumer of the native path) ----
GATES_OLD = "## D38 — THE VERIFIED-IMPORT CACHE"
GATES_NOTE = """## D38 — THE VERIFIED-IMPORT CACHE

THE RECORDER RUNS WITH THE CACHE OFF (THE DEUTERONOMY WALK 7b, 2026-09-19 — read at the first stitch of chapter 9's tape): seq_record.py captures every runner's
scene by instrumenting submit/advance/close and IMPORTING every cold_run_*.py — a module restored from the cache never runs its scene, so its submits never happen:
the first recording held 118 records of 2,983 and the stitcher wrote a 241-line tape into the sequence file (rerun native, 1,682 lines). Every instrument that
needs a scene to RUN (the recorder, the sweep, --full) runs under INK_CACHE=0; every instrument that reads a module's STATE (the probes, the callees' print, the
runner's own asserts) may take the cache. The rule stands beside the sweep's and --full's in this section.

THE EIGHTEENTH SLIP (the same sitting, found by C2 at the first chain): a runner that READS THE SEQUENCE FILE at import (`_SRC = open(HERE/cold_run_sequence.py)
.read()` — the INK block exec'd the stitcher's way) was keyed on its own source and the shared files alone, so after the tape was re-stitched the cached path
restored the OLD text of the sequence file (the parser block unchanged, the value not — C2 fell on `_SRC` in every such module, NOTHING set aside). THE KEY NOW
CARRIES the sequence file's digest for every module whose source names it (patch_ink_cache_key_ch9.py; FORM unmoved): those modules re-harvest once per tape
change, the others keep their blobs. The slips are eighteen."""

# ---- 14. MEMORY ----
MEM_DESC_OLD = "description: \"COMMITTED THROUGH a985fbc (2026-09-19, on 'Commit push'; PUSHED — chapter 8's two sittings, the two-run rule, THE GATES CUT and chapter 9's reading in one commit) — SITTING 7 DONE 2026-09-19"
MEM_DESC_NEW = "description: \"COMMITTED THROUGH a985fbc (2026-09-19; PUSHED) — SITTING 7b DONE 2026-09-19 (chapter 9 COMPILED — the readback's SIXTH form, a STRETCH graded against the clock MATCH; Aaron's peril written once at its own day, destruction_halved named by the docket; THE RECORDER RUNS WITH THE CACHE OFF; UNCOMMITTED with the cache) — SITTING 7 DONE 2026-09-19"
MEM_PARA = """

SITTING 7b RUN B DONE 2026-09-19 (the owner: "Go" after the compaction; the map's "Sitting 7b" + THE DOCKET — AS RUN + AS BUILT): CHAPTER 9 COMPILED —
cold_run_not_righteousness.py the 64th runner (%d/%d on its first graded run), law_not_righteousness the 69th daemon (given_at Deut 9:1, boot). THE READBACK'S
SIXTH FORM — THE RETELLING OF A STRETCH: thirty-two rows VERBATIM 14 / VARIANT 12 / EXPANDED 4 / TURNED 1 / SUPPLIED 1; the four stretch rows (9:9, 9:11, 9:18,
9:25) measured on the running world's markers — the three forties 40 / 40 / 40, Ta'anit 28b:9's 24 + 16 reproduced by the calendar, Mishnah Ta'anit 4:6's
seventeenth of Tammuz MATCH (DA4, Q22, Q24); Aaron's peril (9:20) SUPPLIED WITH A WRITE — ONE LINE prayed_for_aaron dated (1, 4, 18) by the RETROGRADE marker at
Deut 9:20 (the morrow of the breaking), destruction_halved a STATUS on aaron (the name from Vayikra Rabbah 10:5), the forward marker at 9:21; the stiff neck no
write; the two OPEN rows (the calf's own day — Shabbat 89a:6 the marker's source ON HIS WORD; the second ascent's date). The tape 10/10 on its second run with
RUN (1311, 96, 88, 0, 12, 1606, 40, 319, pairs, 127) as predicted, markers 169 (the first run 9/10: CA1 LISTS the Deuteronomy markers as a literal — retyped;
the nine 'markers 167' counts retyped as designed); kinds 1135, effects 1032, daemons 69, ELEVEN CALL edges; every gate green over the chain's THIRD AND FOURTH passes (the first: two homograph edges FALSE, one pointer; three older probes' 167s; the cache's eighteenth slip — the sequence file in the key; the second from the probes step without the tape's live journal; the third and fourth killed at the eight-worker positions table by the session's memory watchdog, the table by four workers, the fifth from the checkpoint probe), the sweep %d/63.
⚠ LESSONS (fifteen, in the map): THE RECORDER RUNS WITH THE CACHE OFF (a restored module never submits — 118 records of 2,983, a 241-line tape, rerun native);
the probes' FAIL run precedes the types (the daemon order and the dispositions must agree for any reader); A LITERAL THAT LISTS THE MARKERS MOVES LIKE ONE THAT
COUNTS THEM (grep the marker verses before the tape); the line at the marker's own verse takes the marker's class (reading_placed, not page_order); a line's
subject makes no entity; the sixth form holds — the clock read back is a compile rule's test; the docket names the effect; the callees' print settles the call
forms and the first verses (14:11); the SUPPLIED-with-a-write scan excludes the write once the fold carries it; with_placement adds the kwarg; THE TWO-RUN RULE
HELD on its second compile sitting (three clean points, the docket in RUN A's window on his word); a count literal in a PROBE moves too; THE CACHE'S KEY COVERS EVERY
FILE A MODULE READS AT IMPORT; A CHAIN RERUN WITH THE PROBES STARTS AT THE TAPE. ⚠ OWED: the fragments in the ark (10:1-5) at chapter 10; the
calf's own day ON HIS WORD; 10:10's forty. NOT COMMITTED (since a985fbc; ONE message at <scratch>/commit_msg_ch9b.txt covers THE IMPORT CACHE and 7b). NEXT on
the ruling: the commit; chapter 10's reading (10:1-22), one run.
""" % (CASES_N, CASES_N, SW_P)
MEM_IDX_OLD = 'map World/step9/DEUTERONOMY_WALK.md; ch 1-8 COMPILED, ch 9 READ — ALL PUSHED at a985fbc (2026-09-19); 7b RUN A + docket done; RUN B next'
MEM_IDX_NEW = 'map World/step9/DEUTERONOMY_WALK.md; ch 1-9 COMPILED (1-8 PUSHED at a985fbc; 9 + the cache UNCOMMITTED); NEXT: commit on his word, then ch 10'

# ---- 15. RECORD_FORMS — the writer's form pointer ----
FORMS_OLD = "World/step9/forms_deuteronomy_walk/write_ch8b_records.py (write_ch7b_records.py, write_ch6b_records.py, write_ch5b_records.py and write_ch4b_records.py the earlier forms; a docket run's close by write_ch8_docket_records.py). Keep this sheet current"
FORMS_NEW = "World/step9/forms_deuteronomy_walk/write_ch9b_records.py (write_ch8b_records.py, write_ch7b_records.py, write_ch6b_records.py, write_ch5b_records.py and write_ch4b_records.py the earlier forms; a docket run's close by write_ch9_docket_records.py). Keep this sheet current"

# ---- THE WRITES (every text built above; the files opened only now) ----
def read(p): return open(p if p.startswith('/') else f'{ROOT}/{p}', encoding='utf-8').read()
def write(p, s): open(p if p.startswith('/') else f'{ROOT}/{p}', 'w', encoding='utf-8').write(s)
plans = []
def f_map(s):
    assert 'THE DOCKET — AS RUN (2026-09-19, on "Go" in the same window as RUN A' in s and '## Sitting 7b — THE COMPILE OF CHAPTER 9 — AS BUILT' not in s
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
    assert s.count(BRIEF_BULLET_ANCHOR) == 1 and s.count(BRIEF_ENTRY_ANCHOR) == 1 and '## SCOREBOARD (as of 2026-09-19, latest)\n' in s, (s.count(BRIEF_BULLET_ANCHOR), s.count(BRIEF_ENTRY_ANCHOR))
    s = s.replace(BRIEF_BULLET_ANCHOR, BRIEF_BULLET + BRIEF_BULLET_ANCHOR)
    return s.replace(BRIEF_ENTRY_ANCHOR, BRIEF_ENTRY + BRIEF_ENTRY_ANCHOR)
plans.append(('THE_BRIEFING.md', f_brief))
def f_loop(s):
    assert s.count(LOOP_OLD) == 1; return s.replace(LOOP_OLD, LOOP_NEW)
plans.append(('World/step9/THE_LOOP.md', f_loop))
def f_gates(s):
    assert s.count(GATES_OLD) == 1 and 'THE RECORDER RUNS WITH THE CACHE OFF' not in s; return s.replace(GATES_OLD, GATES_NOTE, 1)
plans.append(('World/step9/GATES_CHAIN.md', f_gates))
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
