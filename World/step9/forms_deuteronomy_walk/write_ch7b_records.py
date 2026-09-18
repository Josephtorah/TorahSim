#!/usr/bin/env python3
import os as _os, subprocess as _sp
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
# THE DEUTERONOMY WALK sitting 5b — THE COMPILE OF CHAPTER 7 (2026-09-18): THE RECORDS, written after every gate ran — the numbers COMPUTED from the
# gates chain's own prints in the scratchpad (gates_ch7b/*.out; never recited) and the docket's own rows; every text built whole before any file is
# opened; the ledgers appended, the map appended, the checklist's boxes marked paid, the recovery page REWRITTEN whole under its cap, the memory index
# edited under its cap. `--check` parses and prints without writing. Sitting 4b's form (write_ch6b_records.py) on the sheet World/step9/RECORD_FORMS.md.
import os, re, sys, subprocess
ROOT = _ROOT
SP = os.path.dirname(os.path.abspath(__file__))
G = f'{SP}/gates_ch7b'
MEM = os.path.expanduser('~/.claude/projects/-Users-Shared-TorahSim/memory')
CHECK = '--check' in sys.argv
def rd(name): return open(name if name.startswith('/') else f'{G}/{name}', encoding='utf-8', errors='ignore').read()
def last_frac(name, m):
    t = rd(name); hits = re.findall(r'(\d+)/%d\b' % m, t); assert hits, (name, 'no n/%d' % m); return int(hits[-1])
# ---- THE NUMBERS FROM THE PRINTS ----
summ = rd('SUMMARY.txt'); assert 'GATES CHAIN DONE — ALL GREEN' in summ, summ
tape = rd('tape.out'); assert '10/10 checkpoints' in tape and 'OK   THE REST' in tape
CQ = re.findall(r'CHECKPOINT (CQ\d) .*? (MATCH|MISS|DIVERGE)$', tape, flags=re.M); assert len(CQ) == 9 and all(v == 'MATCH' for _, v in CQ), CQ
tape_elapsed = re.search(r'elapsed ([\d.]+)s', tape).group(1)
PL = re.search(r"PLACEMENT \(O9 T2\): markers (\{[^}]*\}); events (\{[^}]*\})", tape); assert PL
assert PL.group(2) == "{'text_constrained': 109, 'page_order': 1143, 'reading_placed': 55}", PL.group(2)
rg = rd('register.out'); m = re.search(r'DECLARED (\d+); DEBT (\d+); FAILS (\d+)', rg); assert m and 'THE REGISTER GATE: GREEN' in rg
RG = tuple(int(x) for x in m.groups())
assert not re.search(r'^\s*Deut 7:\d+\s+(CHAPTER|DAEMONS|ACT|CLOSE|RUN)', rg, flags=re.M), 'a seat in chapter 7 appeared'   # no receipt form in the chapter (the design's measure)
dg = rd('daemon.out'); m = re.search(r'\((\d+) daemons, (\d+) functions\)', dg); assert m and 'gate satisfied' in dg; DG = tuple(int(x) for x in m.groups())
dp = rd('dependency.out'); m = re.search(r'dispositions on file: (\d+) edges, (\d+) pointers', dp); assert m and 'gate satisfied' in dp; DP = tuple(int(x) for x in m.groups())
LC = re.search(r'LINK CENSUS \(the link review law\): reference (\d+), transfer (\d+), hypothesis (\d+), none (\d+)', dp); assert LC; LC = tuple(int(x) for x in LC.groups())
m = re.search(r'required edges (\d+), required pointers (\d+); live import edges (\d+)', dp); DPR = tuple(int(x) for x in m.groups())
bw = rd('build.out'); assert 'ALL GREEN' in bw, bw[-600:]
jg = rd('journal2.out'); assert 'GATE GREEN' in jg and 'GATE GREEN' in rd('journal.out'); m = re.search(r'(\d+) kinds, (\d+) rows in the index', jg); JG = tuple(int(x) for x in m.groups())
sw = rd('sweep.out'); SW_P = len(re.findall(r'^PASS +cold_run_\w+\.py', sw, flags=re.M)); SW_F = len(re.findall(r'^FAIL +cold_run_\w+\.py', sw, flags=re.M))
SW_CELLS = sum(int(a) for a, b in re.findall(r'score=(\d+)/(\d+)', sw)); assert SW_P + SW_F == 62, (SW_P, SW_F); assert SW_F == 0, 'the sweep has failures — read them first'
po = rd('positions.out'); m = re.search(r'(\d+) checkpoints over (\d+) pauses', po); assert m, po[-800:]; PO = tuple(int(x) for x in m.groups())
PR = {'census': last_frac('probe_census.out', 224), 'installation': last_frac('probe_installation.out', 6), 'readback': last_frac('probe_readback.out', 18),
      'register': last_frac('probe_register.out', 7), 'sequence': last_frac('probe_sequence.out', 4), 'view': last_frac('probe_view.out', 6),
      'population': last_frac('probe_population.out', 9), 'journal': last_frac('probe_journal.out', 7), 'cursor': last_frac('probe_cursor.out', 6),
      'large_letter': last_frac('probe_large_letter.out', 6), 'checkpoint': last_frac('checkpoint.out', 7)}
ck = rd('probe_clock.out'); m = re.findall(r'(\d+)/(\d+)', ck); PR['clock'] = ('%s/%s' % m[-1]) if m else 'exit 0'
assert PR['checkpoint'] == 7 and PR['readback'] == 18 and PR['installation'] == 6 and PR['large_letter'] == 6, PR
run1 = rd(f'{SP}/ch7_run1.out'); assert '51/51' in run1
# the docket's numbers from its own rows
DK = 'logic/oral_triage/deu_07_vaetchanan_ekev_exam_2026-09-18.md'
dk = open(f'{ROOT}/{DK}', encoding='utf-8').read()
rows = [l for l in dk.split('\n') if re.match(r'^- .*? — (LAW|DERIVATION|DISPUTE|CONTEXT|OUTSIDE)\.', l)]
VD = {v: sum(1 for l in rows if re.match(r'^- .*? — %s\.' % v, l)) for v in ('LAW', 'DERIVATION', 'DISPUTE', 'CONTEXT', 'OUTSIDE')}
NROWS = len(rows); NLINK = sum(1 for l in rows if '[LINK' in l); NTOPIC = sum(1 for l in rows if '[TOPIC' in l); NCRED = sum(1 for l in rows if 'CREDITED' in l)
NWHOLE = sum(1 for l in rows if '[whole:' in l); DKB = len(dk.encode('utf-8'))
assert NROWS == 520 and NLINK + NTOPIC == NROWS and NWHOLE == 0, (NROWS, NLINK, NTOPIC, NWHOLE)
hp = subprocess.run(['python3', 'logic/solo_tools/scrub_home_paths.py', '--check'], cwd=ROOT, capture_output=True, text=True); assert hp.returncode == 0, hp.stdout[-500:] + hp.stderr[-500:]
NUM = dict(RG=RG, DG=DG, DP=DP, LC=LC, DPR=DPR, JG=JG, SW=(SW_P, SW_CELLS), PO=PO, PR=PR, PL=PL.groups(), tape_elapsed=tape_elapsed, docket=(NROWS, NLINK, NTOPIC, NCRED, NWHOLE, DKB, VD))
print('THE NUMBERS:', NUM)
pr_line = ('census %d/224, installation %d/6 (I5 67), readback %d/18 (Q16-Q18 the readback on the kin), register %d/7, clock %s, sequence %d/4, view %d/6, population %d/9, journal %d/7, cursor %d/6, large_letter %d/6, checkpoint %d/7'
           % (PR['census'], PR['installation'], PR['readback'], PR['register'], PR['clock'], PR['sequence'], PR['view'], PR['population'], PR['journal'], PR['cursor'], PR['large_letter'], PR['checkpoint']))
gates_line = ('the daemon gate GREEN (%d daemons, %d functions WRAPPED); the dependency gate GREEN (%d edges and %d pointers on file — the link census reference %d / transfer %d / hypothesis %d / none %d; required %d edges and %d pointers, live import edges %d); '
              'build_world ALL GREEN (221 units, standing 2209, hash 8b8fff1fa28953af unmoved — no freeze this sitting); the journal gate GREEN twice — before and after the sweep (%d kinds, %d rows in the index); THE REGISTER GATE --strict GREEN (DECLARED %d, DEBT %d, FAILS %d — no seat in chapter 7: no receipt form in it, as the design measured); '
              'the positions table %d checkpoints over %d pauses (CQ1-CQ9 in it; checkpoint_probes %d/7 after the rebuild); the sweep %d/62 at %s graded cells; the home-path gate GREEN'
              % (DG[0], DG[1], DP[0], DP[1], LC[0], LC[1], LC[2], LC[3], DPR[0], DPR[1], DPR[2], JG[0], JG[1], RG[0], RG[1], RG[2], PO[0], PO[1], PR['checkpoint'], SW_P, format(SW_CELLS, ',')))
docket_line = ('%d rows (link %d / topic %d; LAW %d, DERIVATION %d, DISPUTE %d, CONTEXT %d, OUTSIDE %d; credited %d; %s bytes), EVERY ROW READ WHOLE FROM THE START — no cut, no overlay (the parts\' WHOLE dicts empty, the correction counts zero and computed)'
               % (NROWS, NLINK, NTOPIC, VD['LAW'], VD['DERIVATION'], VD['DISPUTE'], VD['CONTEXT'], VD['OUTSIDE'], NCRED, format(DKB, ',')))

# ---- 1. THE MAP — AS BUILT ----
AS_BUILT = """

## Sitting 5b — THE COMPILE OF CHAPTER 7 — AS BUILT (2026-09-18; the design above stands as written — the four runs ran as designed, the RUN 2 and RUN 3
## paragraphs their record; every departure from the design named here)

THE RESULT. Deuteronomy 7:1-26 is COMPILED AND ON THE TAPE: World/step9/cold_run_seven_nations.py the 62nd runner (MATRIX 51/51 on its first graded
run; six cells F1 the_seven_nations, F2 the_holy_people, F3 the_faithful_god, F4 because_you_hear, F5 do_not_fear, F6 the_images_and_the_devoted with
51 asks; nineteen DATA rows; the readback's twenty-one rows and four holes; fourteen exam persons — four exempt (the praiser who thanks the Creator, the
one without another way, the Canaanite outside the Land, the finder of the money at the idol's head), one flogged (the Asherah's wood-burner); the scene
and the narrative tuples matched as predicted by script), law_seven_nations the 67th daemon (given_at Deut 7:1 — the ban's first and only giving;
installed_by boot; six functions WRAPPED; no timer), four kinds and four effects in the registries (1129 kinds, 1029 effects), THREE LINES AND NO MARKER
on the tape — nations_devoted (7:1-5), hearing_blessed (7:12-16), abomination_barred (7:25-26) under "# ---- Deut 7 ----" on the counter's own day
(40, 11, 1). THE CODE'S FOUR HOLES COMPILED: the ban (commanded valued devote_the_seven_nations — a DEBIT on Israel OPEN to Joshua), no favor
(favor_barred — the three readings), no pity (pity_barred — on the ink alone), the abomination into the house (house_abomination_barred); and TWO OLD
EFFECTS WRITTEN ON THE TAPE FOR THE FIRST TIME — covenant_barred (Exodus 23:32's; its case kind entered_the_land Joshua's) and intermarriage_barred
(34:16's, valued both directions); blessings_for_hearing the conditional heaven entry. THE TAPE 10/10 WITH THE REST ON ITS SECOND RUN: RUN (1307, 96,
88, 0, 12, 1602, 38, 319, the four pairs, 127) exactly as THE PREDICTION'S ARITHMETIC wrote it; PREVIOUS_RUN 4b's RUN EXACTLY — no declared delta;
NEWEST_RUNNER seven_nations; markers 167 UNMOVED (forward 129, retrograde 23, proleptic 15); entities 319, closes 127, the population table 148
UNMOVED; PLACEMENT markers %s, events %s (page_order 1140 → 1143 — AS PREDICTED); CENSUS (2504, 1316, 1307, 1172, 6, 10, 9, 0, 71, 167, 129, 15, 23,
852, 272) as the stitcher printed it (on tape 1304 → 1307, kinds 849 → 852, subjects 272 unmoved); CQ1-CQ9 all MATCH; the run %ss. THE DOCKET %s by
the union rule: %s; Avodah Zarah 42a-54b's six verse-anchored amudim (42a-42b, 44b-46b, 47b-48b, 49b, 51b-52b, 53b-54b — 303 rows) read whole, the
remainder (162 rows) ENUMERATED outside declared scope; the crowns fifteen in the docket's own list.

THE READBACK ON THE KIN — THE LAWS' FORM RUN ON ANOTHER CHAPTER'S CODE (THE LOOP's step 6; the fourth exhibit of the form): twenty-one reference rows —
six against the tape's lines found by kind and first verse (covenant_offered at Exodus 19:5 twice, brought_out at 12:51, stand_here_commanded at
Deuteronomy 5:28, healer_promised at 15:26, the ten plague_struck lines at 7:20), fifteen against the KIN'S CELLS BY CALL (ordinances.land — no_covenant,
bread_water, no_barren, not_dwell, hornet, little_by_little, borders; erection.covenant — nations_seven_orders, daughters_two_seats,
child_follows_mother, demolition_grows; journeys.the_command — drive_out, three_objects_own; covenant_at_horeb — the_visiting twice, covet_and_desire),
each cell's verdict asserted at build (cell_found) — graded VERBATIM 4 / VARIANT 5 / EXPANDED 8 / TURNED 3 / SHORTENED 1 as the design predicted; no
row OPEN; no second write (R1) — the demolition of 7:5 a reference row against journeys' OPEN debit destroy_their_images. THE INSTALL HYPOTHESIS tested in
passing and not ruled: the code re-declared with the target's names graded as the laws' readback, nothing of the engine changed.

THE DEPARTURES FROM THE DESIGN, each found by an instrument and each a lesson below: (1) THE EFFECT NAME blessing_promised WAS ALREADY ABRAM'S — the
ladder's heaven entry (Genesis 12:2-3; 26:24) sat in the registry, so the types script's first run added three of four: the chapter's entry is
blessings_for_hearing (the daemon watch, the kind's text, the runner and the probe Q17 carry it); (2) covenant_offered's FIRST VERSE IS 19:5, not the
design's 19:4 (the case_source 'Exod 19:5-6' — read by grep of the runners' submits before the rows were typed); (3) THE EXAM ASKS RETURNED THE WRITE
EFFECTS at the first assembly (favor_barred and its kin) and the daemon's case branch maps accepted / exempt / lashes only — the seven exam asks retyped
to accepted, the writes on the the_write asks alone (4b's form); (4) FOUR OLDER CHECKPOINTS DIVERGED ON THE FIRST TAPE RUN — CV2, CX2, CW3, CR3 hold the
CURRENT COUNT of the commanded entries on israel_people (18, the newest begin_to_possess_sihons_land, open 7) and the ban's DEBIT makes 19 /
devote_the_seven_nations / 8: retyped from the print with the 5b note (the design's 'no retype' clause named closes and markers only); (5) THE
GATES-TO-FAIL STEP (daemon, dependency) WAS NOT RUN SEPARATELY before the runner — the runner was built directly and the gates ran in the chain;
(6) THE MAP'S RUN-2 PARAGRAPH WAS SKIPPED by a guard that tested for 'RUN 2 — AS RUN (2026-09-18' — a string sitting 5's reading paragraph already
carried — and appended at run 3's close from the writer's print; (7) THE PITY'S HOLE HAS NO ROW ON THE SHELF — the docket's scan cites 7:16 once, for
'consume' (Bava Kamma 113b): pity_barred stands on the ink alone, its exam rows the book's later seats forward; (8) THE DOCKET'S CREDIT COUNT — the
whole-range scan's 89 counted credits in the enumerated part; the rerun with the amudim named gives 65; (9) OUTSIDE USED — 75 rows of the declared
ranges are digressions on another matter (the gazing and the Angel of Death, the permissive court and the bill of divorce, the newborn in the pit, the
Ark's journeys, the ephod's stones, the plower's lashes list): the honest verdict when a range is read whole (1b's form); (10) THE OTHER THREAD HAD
APPENDED A §8 TO THE RECOVERY PAGE (over its cap) — folded into one READ ON DEMAND line at run 3's close; (11) THE DEPENDENCY GATE DEMANDED ONE
EDGE AND NO POINTER — the token census matched 'king' in 7:8's 'Pharaoh KING of Egypt' to the sanctions span's Molech (the same consonants; the lemmas
4428 and 4432 on the DB): a HOMOGRAPH, dispositioned FALSE with its why (add_pointers_ch7.py); the design's (n) had predicted seven RUN_CITATION
pointers (7:6, 7:8, 7:12, 7:13, 7:18, 7:19, 7:22) and the census demanded none — the citations ride the CALL edges' whys (4b's lesson held again);
the chain's first run stopped at that step, the second from it ALL GREEN (the tape's and the probes' prints the first run's).

THE GATES, COMPUTED FROM THEIR PRINTS (one chain, gates_chain.sh — run twice: the first stopped at the dependency gate by the one homograph demand,
the second from that step ALL GREEN; the tape's and the probes' prints the first run's): the probe suites %s; %s.

⚠ THE LESSONS OF 5b (eleven): (1) A REGISTRY NAME THE DESIGN PREDICTS MAY ALREADY EXIST — the types script's 'added N of M' count is the tripwire; the
registry decides the name; (2) THE CENSUS DECIDES THE FIRST VERSE — a tape line's first verse is read from the runner's submit, never from the design's
memory (19:5, not 19:4); (3) THE EXAM ASKS RETURN VERDICTS, THE WRITE ASKS RETURN WRITES — the daemon's case branch maps the verdict effects only;
(4) A DEBIT ON ISRAEL MOVES THE OLDER CHECKPOINTS' COMMANDED-COUNT LITERALS (3b's closes lesson, now on the debits): a 'no retype' clause covers only
what it names; grep the older cp() names for the counts a write moves before the tape; (5) THE CALLEES' FACTS PRINT FIRST — the asks' signatures differ
by runner (a string and a dict; a case and a tuple; a signs dict): read them before an assert is typed; (6) A PROBE WRITTEN BEFORE THE RUNNER IS RETYPED
ONCE (Q17's effect name); (7) A GUARD NAMES THE SITTING — a string another sitting also wrote is no guard; (8) A HOLE THE DESIGN PREDICTS MAY HAVE NO ROW
ON THE SHELF — the write stands on the ink alone and the docket says so; (9) THE WHOLE-RANGE SCAN'S CREDIT COUNT IS NOT THE DOCKET'S — rerun the scan
with the amudim named before the credits are counted; (10) THE SHELF TEACHES THE REASON AND THE CONDITION of a command the design took as bare — the
calf's agency behind the demolition (Avodah Zarah 53b:7-11), repentance and the Land's border behind the ban (Sotah 35b:10-36a:1): DATA rows added at
run 3, the war chapter's cells still owed forward; (11) THE CENSUS READS HOMOGRAPHS AND DECIDES THE POINTERS — 'king' matched Molech, named FALSE
with its why; the design's seven pointers not demanded: read the gate's print, disposition each demand on the DB, never a blanket row.

THE DISPOSITIONS ADDED: the span seven_nations [[Deut, 7, 1, 26]]; thirteen CALL edges (ordinances, erection, journeys, covenant_at_horeb, decalogue,
exodus_story, obey_horeb, hear_o_israel, opening_speech, mamre, joseph, balak, shemini) and the registration edge sequence → seven_nations; the
one FALSE edge the census demanded past the imports (seven_nations → sanctions at 7:8 — 'king' / Molech, the homograph named on the DB) and NO
pointer (the design's seven RUN_CITATION pointers ride the CALL edges' whys — the dependency gate's print). MOVE_CATALOG CHECKED, unmoved:
the runner's law cells return the shelf's parameters (the three readings of favor, the marriage bar's scope and the child, the Asherah's definition,
the nullification, the decorative item, the exchange) and CALL the callees' cells; the shelf's own moves on the chapter (the spelling argument, the reason
expounded, two verses as one, the doubled verb, the inference barred, the calf's agency) are the docket's and MIDDOT's rows, no new move of the compiler.

THE FORMS: the sitting's scripts and prints copied into World/step9/forms_deuteronomy_walk/ by copy_ch7b_forms.py (the recon, the scan and the dump, the
docket's four parts with the common helper and the four row prints, the writer, the run-2 close, the design's writer, the types, the callees' print, the
runner's four parts with the generator, the assembler and the fast checker, the recorder and the stitcher under their sitting's names, the literals'
patcher, the pointers, the records' writer, the gates chain's folder — no scratch path, no home path, no git root in any copied form).

NEXT on the ruling: the commit on the owner's word (sitting 5, 5b, the tutorial and the design thread's files, since 64a8362); then CHAPTER 8's reading
(8:1-20 — the manna and the humility, the good land, the forgetting; the reading shape, in four runs, every row whole) — or the Decalogue-schema sitting
first (ON THE TABLE, not a ruling). Nothing committed: the tree uncommitted since 64a8362, on the owner's word only.
""" % (PL.group(1), PL.group(2), tape_elapsed, DK, docket_line, pr_line, gates_line)

# ---- 2. COMPILE_DEBT — the sitting-5 box marked PAID + the 5b box ----
DEBT_HDR_OLD = "## deu_07_vaetchanan_ekev_2026-09-17.md, 29 sources; one unit deu_07_nations_cherem FROZEN, the 221st) — OWED TO THE COMPILE (sitting 5b): (a) THE BAN"
DEBT_HDR_NEW = "## deu_07_vaetchanan_ekev_2026-09-17.md, 29 sources; one unit deu_07_nations_cherem FROZEN, the 221st) — PAID AT 5b (the 5b box below, item by item) — AS WRITTEN AT THE READING, OWED TO THE COMPILE (sitting 5b): (a) THE BAN"
DEBT_BOX = """
## DEUTERONOMY SITTING 5b — THE COMPILE OF CHAPTER 7 (2026-09-18; DEUTERONOMY_WALK.md "Sitting 5b" design + AS BUILT; logic/oral_triage/deu_07_vaetchanan_ekev_exam_2026-09-18.md
## %d rows, every row read whole from the start; cold_run_seven_nations.py 51/51; law_seven_nations the 67th daemon; the tape 10/10 with RUN (1307, 96, 88, 0, 12, 1602, 38, 319, pairs, 127)).
## THE SITTING-5 BOX (a)-(p) PAID — (a) THE BAN — F1 the_ban: the code's hole, commanded valued devote_the_seven_nations a DEBIT on Israel OPEN to Joshua at nations_devoted; the
## dispossession's two debits referenced by CALL, not doubled; the east's devotings a DATA row; (b) NO COVENANT AND NO FAVOR — ordinances.land and erection.covenant by CALL,
## covenant_barred's FIRST TAPE WRITE; favor_barred NEW (the three readings — Avodah Zarah 20a); (c) NO MARRIAGE BOTH WAYS — erection.covenant by CALL, intermarriage_barred's
## first tape write valued both directions; the child follows the mother (Kiddushin 68b, Yevamot 23a, Mishnah Kiddushin 3:12); (d) THE FOUR OBJECTS — the demolition a REFERENCE
## row against journeys' OPEN debit (no second debit); the renaming a DATA row; the shelf's order fell / conquer / eradicate and the calf's agency DATA; (e) THE CHOSEN PEOPLE — F2
## by CALL (exodus_story.sinai, obey_horeb.the_one_god), no write; (f) THE FAITHFUL GOD — F3 by CALL (covenant_at_horeb.the_second_word), the rows 7:9 VARIANT and 7:10 TURNED;
## Onkelos's doctrine and the written/read pair DATA rows; (g) BECAUSE YOU HEAR — F4, blessings_for_hearing a conditional HEAVEN entry (NOT blessing_promised — Abram's);
## (h) NO PITY — pity_barred NEW, on the ink alone (no row on the shelf); no serving the second word's clause by CALL, no second write; (i) DO NOT FEAR — F5 no write, the war
## chapter's fear rule OWED FORWARD; (j) LITTLE BY LITTLE — ordinances.land by CALL, the pointer at 7:22; (k) THE KINGS AND THE NAME — a DATA row; Amalek's phrase by CALL;
## (l) THE IDOLS' SILVER AND GOLD — covenant_at_horeb.the_tenth_word by CALL, coveting_barred UNMOVED; the decorative item (51b) the exam's rule; (m) THE ABOMINATION INTO THE
## HOUSE — house_abomination_barred NEW; the two lemmas a DATA row; shemini.classify by CALL; (n) THE RUN CITATIONS — the pointers the census demanded, on the DB, one by one;
## (o) THE DOCKET — %d rows by the union rule, EVERY ROW WHOLE FROM THE START; (p) THE FLOCK'S "YOUNG" — a DATA row the_morph_tag. OWED FROM 5b: (i) THE WAR CHAPTER'S CELLS —
## 20:16-18 (the ban's spec for the Land's cities: 'keep alive none that breathes … lest they teach you' — the ban's condition on the shelf, Sotah 35b:10-36a:1, waits for that
## cell), 20:1-4 and 20:8 (the fear rule 7:17-24 promises: 'you shall not fear them' 7:18 / 20:1); (ii) THE FINDER'S THIRD FORM (4b's owed item, unchanged — no receipt in
## chapter 7); (iii) THE BLESSINGS AND THE CURSES — 28:4, 11, 18, 51, 60 (7:13-15's list said again) compile at chapter 28's sitting and cite 7:13 by CALL; (iv) 12:2-3 — the
## demolition's fuller form (five verbs; 'destroy their name' — the renaming) at chapter 12's sitting, citing 7:5 by CALL; (v) 13:18's 'nothing of the devoted shall cleave' — the
## devoted thing's second seat, at chapter 13's sitting; (vi) THE PITY'S FOUR LATER SEATS (13:9, 19:13, 19:21, 25:12) each at its chapter, citing 7:16 by CALL; (vii) Joshua's
## receipts (1:5 'no man shall stand', 24:12 the hornet, 7:21 Achan's coveting, 2:34 / 3:6 the east's devotings already on the tape) — the run, outside the Torah.
## NOTHING ELSE IN CHAPTER 7 IS OWED TO A LATER SITTING OF ITS OWN.
""" % (NROWS, NROWS)

# ---- 3. MIDDOT — the docket entry ----
MIDDOT_ANCHOR = "\n## Exodus block campaign — owner's word \"Do 3\")\n"
MIDDOT_ENTRY = """- THE CHAPTER-7 DOCKET (THE DEUTERONOMY WALK sitting 5b, 2026-09-18; logic/oral_triage/deu_07_vaetchanan_ekev_exam_2026-09-18.md — %d rows, every row read
  whole from the start; the rules about rules the docket carries, each at its row):
  · THE SPELLING ARGUMENT (Avodah Zarah 20a:2-3 on 7:2 "show them no favor"): the defective verb yields THREE readings — spelled with the vav it would mean
    favor alone, with the yod the gift alone; spelled short, learn all three (the land, the praise, the gift): F1 no_favor, the DATA row the_three_readings_of_favor.
  · THE REASON EXPOUNDED (Avodah Zarah 36b:6; Kiddushin 68b:6-7; Yevamot 23a:13-14 on 7:3-4): R. Shimon reads the verse's reason ("for he will turn your son")
    and extends the marriage bar to every nation; the Rabbis, who do not expound the reason, find the other nations at 21:13 (the captive) and the child at
    21:15: F1 no_marriage (the scope's two arms; the exam's parameter).
  · THE TORAH'S BAR IS THE SEVEN NATIONS (Avodah Zarah 36b:5 on 7:3): by Torah law the seven; the other nations by the students' decree — a chain of decrees
    wine → daughters → idolatry (36b:4): F1 no_marriage; the write intermarriage_barred's scope by Torah law.
  · "HEW DOWN" AND "BURN" ARE TWO CASES (Avodah Zarah 45b:9; 48a:9 on 7:5 / 12:3): since "burn their asherim" is written, "hew down their asherim" is superfluous
    and read of the tree planted and afterward worshipped — the fourth verb the shelf's hook; reversible (48a:9): F1 the_four_objects (the readback row 7:5 EXPANDED).
  · THE ORDER FROM THE VERB (Avodah Zarah 45b:10-12 on 7:5 "hew down"): R. Yehoshua ben Levi — fell the Asherim, conquer the land, then eradicate; Rav Yosef: break
    the altars and leave them; Rav Huna: pursue the enemy, return and burn — the demolition's stages read off one verb: F1 the_four_objects (the demolition a
    reference row against the dispossession's OPEN debit).
  · THE DOUBLED VERB (Avodah Zarah 45b:13-14 on 12:2 "you shall utterly destroy"; the Sifrei 61:7 on 7:26 "utterly detest … utterly abhor"): two stages (R. Yosei
    son of R. Yehuda) or the traces rooted out (the Rabbis); on 7:26 the renaming for the worse (R. Akiva against R. Eliezer): F1 the_four_objects, the DATA row
    the_renaming; F6 utterly_detest.
  · THE CALF'S AGENCY (Avodah Zarah 53b:7-11 on 12:3 / 7:5): the Land is Israel's inheritance and a person cannot forbid what is not his — so the gentiles who
    worshipped its trees were ISRAEL'S AGENTS after the calf ("these are your GODS", plural): the Asherim a Jew's idols, irrevocable, hence burned: F1
    the_four_objects, the DATA row the_calfs_agency (the reason of the demolition command the design took as bare).
  · THE LAWS OF IDOLATRY DERIVED FROM JOSHUA'S WAR (Avodah Zarah 53b:5-6 on 7:2): the idols of the gentiles killed in the war, who meant to return, NOT revoked —
    the ban's run read back by the shelf: F6 burn_the_images; F1 the_ban's debit OPEN to Joshua.
  · "ON THEM" READ BY "WITH THEM" (Avodah Zarah 51b:10-12 on 7:25 / 29:16): the two verses reconciled — the DECORATIVE item forbidden, the rest permitted, and
    why the chapter's clause stands (else inferred a fortiori): F6 not_covet_silver_gold.
  · THE WORD READ AS "THE REVOKED OF" (Avodah Zarah 52a:9-10 on 7:25 "the graven images of their gods"): the nullification by a gentile from the word's letters
    (R. Yishmael) or from the verse's two halves — "not covet" against "take it for yourself" (Shmuel for R. Akiva): F6 burn_the_images.
  · "LEST", "BEWARE", "DO NOT" ARE PROHIBITIONS (Avodah Zarah 51b:3 — R. Avin in R. Ilea's name): the chapter's sixteen prohibitions and its two "lest" (7:22, 7:25):
    F6 lest_snared (a DATA note).
  · TWO VERSES THAT COME AS ONE (Avodah Zarah 54b:6-11; Kiddushin 58a:12 on 7:26 "for IT is devoted" / Leviticus 25:12 "IT is a Jubilee"): idolatry's and the
    Sabbatical's exchange rules teach no third case — or they do, and "it" excludes orla and diverse kinds: F6 devoted_like_it.
  · "BECOME DEVOTED LIKE IT" — WHAT YOU GENERATE (Chullin 140a:12; Temurah 30b:7; Kiddushin 58a:7; Avodah Zarah 54b:3 on 7:26): the verb "become" read as "give
    life to" — whatever comes from the idol is like it (the birds, the money, the animal exchanged); the exchange's exchange two arms (54b:4-5): F6 devoted_like_it.
  · A PERSON CANNOT FORBID WHAT IS NOT HIS — AND A RITE UPON IT DOES (Avodah Zarah 54a:2-54b:2): bowing to another's animal does not forbid it, a sacrificial rite
    upon it does; Ahaz's vessels the source (II Chronicles 29:19 "prepared" = interred): F6 burn_the_images (the run's case by REFERENCE).
  · THE INFERENCE BARRED BY A VERSE (Avodah Zarah 46a:14 on 7:26): the worshipped boulders — though one might derive by inference to permit them, "you shall
    not bring an abomination … detest it" says do not derive: F6 utterly_detest's verse as a bar on inference (a parameter row).
  · THE TREATED-AS-DEITY TEST AND ITS FIVE ANSWERS WEIGHED (Mishnah Avodah Zarah 3:4; Avodah Zarah 44b:7-15 on 12:2 "their gods" / 7:25): each of Rabban Gamliel's
    answers to Proclus tried as deceptive or true (Peor's manner; Mishnah 4:3's favor; the passing scorn; the adornment): F6 burn_the_images.
  · THE IMPORTANT PERSON IS DIFFERENT (Avodah Zarah 48b:10 on 7:5): one with no other way may pass beneath the Asherah, and Rav Sheshet ran — lest others learn
    from him: F1 the_four_objects (the exam's edge no_other_way EXEMPT).
  · THE MIXED CAUSE (Avodah Zarah 48b:12-18 on 7:5): the foliage and the ground both grow the vegetables — forbidden or permitted? the attribution reversed, or
    Rav Mari's offset (the foliage's gain against the shade's damage): F1 the_four_objects (DATA).
  · THE STRINGENT A FORTIORI (Avodah Zarah 46b:6-9): between an inference to leniency and one to stringency, the stringency — with R. Akiva's exception that
    was no inference but a reminder: a rule about inferences on the docket, outside the chapter's cells.
  · THE BAN'S CONDITION AND SCOPE (Sotah 35b:10-13, 36a:1 on 20:16-18, 21:10 / 7:2): the law written on the plaster and "lest they teach you" below for the
    nations — the inhabitants who repent accepted; the Canaanite outside the Land not devoted: F1 the_ban (the DATA row the_bans_condition; the war chapter's
    cell owed forward).
  · "CONSUME" IS THE WAR'S SPOIL (Bava Kamma 113b:7 on 7:16): robbing a gentile prohibited — the peoples' property consumed only when delivered into your
    hand: F4 consume_no_pity.
  · A THOUSAND FOR FEAR, THOUSANDS FOR LOVE (Sotah 31a:9-10 on 7:9 / Exodus 20:6): the numbered clause against the bare plural read as two motives: F3
    thousand_generations (the readback row 7:9 VARIANT's shelf reading).
""" % NROWS

# ---- 4. MISHNAH_TOPICS — the rows touched ----
W5 = "THE DEUTERONOMY WALK sitting 5b"
DKF = "deu_07_vaetchanan_ekev_exam_2026-09-18.md"
TOPIC_NOTES = {
 "**38. Mishnah, Idolatry**": " — 1:1-4:12 READ WHOLE (thirty-eight rows, the answer sheet — twenty-four credited from the erection docket, given their quick look) with Avodah Zarah 20a-20b, 36b-37a, 42a-42b, 44b-46b, 47b-48b, 49b, 51b-52b, 53b-54b READ WHOLE 2026-09-18 (%s: the three readings of 'show them no favor', 7:2; the marriage bar's scope, 7:3; the Asherah defined, the demolition's order, the renaming, 7:5; the nullification, the money on the idol, the abomination into the house, the devoted thing, 7:25-26; the rest of 42a-54b enumerated outside scope; %s)" % (W5, DKF),
 "**30. Mishnah, Betrothal**": " — 3:12 READ with Kiddushin 68b READ WHOLE and 58a:7-12 2026-09-18 (%s: the betrothal with a gentile woman ineffective, the child follows the mother, 7:3-4; the idol's exchange money, 7:26)" % W5,
 "**24. Mishnah, Levirate Marriage**": " — Yevamot 23a READ WHOLE and 76a:12 READ 2026-09-18 (%s: the sister from a gentile mother, the child follows the mother — 7:3-4's second seat; the Gibeonite and 7:3)" % W5,
 "**28. Mishnah, Suspected Wife**": " — Sotah 35b-36a READ WHOLE, 4b:10, 5a:10 and 31a:9-10 READ 2026-09-18 (%s: the ban's condition and scope — repentance, the Land's border; the hornet at the Jordan, 7:20; arrogance as idolatry, 7:26; a thousand for fear, 7:9)" % W5,
 "**43. Mishnah, Slaughter**": " — Chullin 89a READ WHOLE, 84b:1 and 140a:12 READ 2026-09-18 (%s: 'not because you were more', 7:7; the flock's word, 7:13; the birds exchanged for an idol, 7:26)" % W5,
 "**35. Mishnah, Lashes**": " — Makkot 22a READ WHOLE 2026-09-18 (%s: the Asherah's wood flogged under 7:26 and 13:18; the lashes' count 25:2-3)" % W5,
 "**31. Mishnah, First Gate**": " — Bava Kamma 113b:7 READ 2026-09-18 (%s: robbing a gentile prohibited — 'consume' the war's spoil, 7:16)" % W5,
 "**32. Mishnah, Middle Gate**": " — Bava Metzia 107b:2 READ 2026-09-18 (%s: the sickness the evil eye, 7:15)" % W5,
 "**13. Mishnah, Merging Domains**": " — Eruvin 22a:3, 22a:5 READ 2026-09-18 (%s: the hater repaid to his face, 7:10; today to do, tomorrow to receive, 7:11)" % W5,
 "**12. Mishnah, Sabbath**": " — Shabbat 10b:3 and 82b:1 READ 2026-09-18 (%s: 'the faithful God' a translation, 7:9; the idol's stones impure as a creeping animal or a menstruant, 7:26)" % W5,
 "**46. Mishnah, Substitution**": " — Temurah 28b:5 and 30b:7 READ 2026-09-18 (%s: the coating of worshipped things, 7:25; what you generate from the idol, 7:26)" % W5,
 "**14. Mishnah, Passover**": " — Pesachim 48a:6 READ 2026-09-18 (%s: the Asherah's wood flogged under 7:26 — Makkot 22a's twin)" % W5,
 "**34. Mishnah, Courts**": " — Sanhedrin 93a:10 READ 2026-09-18 (%s: Daniel and 'the graven images of their gods', 7:25)" % W5,
 "**1. Mishnah, Blessings**": " — Berakhot 51b:5 READ 2026-09-18 (%s: 'the fruit of YOUR body' — the cup of blessing, 7:13)" % W5,
}

# ---- 5. RESEARCH_LOG ----
RLOG = """

## 2026-09-18 — DEUTERONOMY 7 COMPILED (THE DEUTERONOMY WALK sitting 5b — CHAPTER 7): THE READBACK ON THE KIN — THE LAWS' FORM RUN ON ANOTHER CHAPTER'S CODE;
## THE CODE'S FOUR HOLES COMPILED AT THE CHAPTER'S OWN DAY; TWO OLD EFFECTS WRITTEN ON THE TAPE FOR THE FIRST TIME; THE REGISTRY DECIDES A NAME; A DEBIT
## MOVES THE OLDER COUNTS; THE SHELF'S REASON AND CONDITION FOR A COMMAND THE DESIGN TOOK AS BARE

THE READBACK ON THE KIN. The readback's three forms (1b the acts, 3b the laws, 4b a retelling inside a law) each graded a chapter against its own first
telling. Chapter 7 re-says ANOTHER chapter's law with the target's names — the angel's clauses of Exodus 23, the renewed covenant of 34, the
dispossession of Numbers 33, the second and the tenth words — so the laws' form ran with the kin's cells as the first telling: fifteen rows graded by
CALL to ordinances.land, erection.covenant, journeys.the_command and covenant_at_horeb's two words (each cell's verdict asserted when the row was built),
six against tape lines found by kind and first verse; VERBATIM 4, VARIANT 5, EXPANDED 8, TURNED 3, SHORTENED 1, exactly the design's census. What the
kin never said is the code's hole: the ban on the seven nations, "show them no favor", "your eye shall not pity", "you shall not bring an abomination into
your house" — four cells compiled here, their writes at the chapter's own day. The install hypothesis (the code re-declared for the land) was tested in
passing by these rows and not ruled.

TWO OLD EFFECTS WRITTEN FOR THE FIRST TIME. covenant_barred (Exodus 23:32's block) and intermarriage_barred (34:16's) had stood in the registry since the
Exodus sittings and never reached the tape — their case kinds are Joshua's (the entry into the land) and the exam's (the daughters taken). Chapter 7
writes both at nations_devoted, the marriage bar valued in both directions where 34:16 had one; when the entry fires at the run, the ordinances' daemon
will write its own on its own case — a second write on a second act, not a doubled law. The ban's debit on Israel stands OPEN to Joshua beside the
dispossession's two debits, the demolition of 7:5 a reference row against those, no second debit.

THE REGISTRY DECIDES A NAME. The design named the blessings' heaven entry blessing_promised; the types script added three effects of four — the name was
Abram's, the ladder's entry (Genesis 12:2-3; 26:24). The chapter's entry is blessings_for_hearing. The 'added N of M' line is the tripwire, and the
probe written before the runner was retyped once to the registry's name.

A DEBIT MOVES THE OLDER COUNTS. The tape reached nine of ten on its first run: every checkpoint of the chapter matched and the previous sitting's tuple
was reproduced exactly, but four checkpoints from the Numbers walk (the vows, Midian, the borders, the refuge cities) hold the current count of the
commanded entries on Israel — eighteen, the newest Sihon's land, seven open — and the ban's debit makes nineteen, eight open. Retyped from the print
with the sitting's note. The lesson of 3b on the closes, now on the debits: a literal that counts a ledger is a current count, and a design's "no retype"
clause covers only what it names.

THE SHELF'S REASON AND CONDITION. Two things the design took as bare commands the shelf supplies with a reason and a condition. The demolition: the Land
is Israel's inheritance from the fathers and a person cannot forbid what is not his — so the gentiles who worshipped its trees were Israel's agents after
the calf, the Asherim a Jew's idols, irrevocable, hence burned rather than revoked (Avodah Zarah 53b:7-11; the laws of idolatry derived from Joshua's
war, 53b:5-6). The ban: the law written on the plaster with "lest they teach you" below for the nations to read — the inhabitants who repent accepted;
the Canaanite outside the Land not devoted (Sotah 35b:10-13, 36a:1). Both are DATA rows on the runner; the war chapter's cells (20:16-18, 20:1-8) are
owed forward. And one hole the design predicted has no row on the shelf at all — 7:16's "your eye shall not pity" is cited by no link row (the verse
once, for "consume": robbing a gentile prohibited); pity_barred stands on the ink alone, its exam rows the book's four later seats.
"""

# ---- 6. THE_STEPS ----
STEPS_ANCHOR = "\n## Step 6 — Publish\n"
STEPS_PARA = """
DEUTERONOMY — SITTING 5b — CHAPTER 7 COMPILED (2026-09-18, on Brian's "Go", "Go", "keep going" and "keep going" for its runs; World/step9/DEUTERONOMY_WALK.md
"Sitting 5b" and "Sitting 5b — AS BUILT"). Chapter 7 says the old law again for the new place — no covenant, no marriage, the altars and the Asherim,
the hornet, little by little — so this sitting graded each verse against the cell that compiled the law the first time, in Exodus and Numbers, the way
earlier sittings graded a retelling against the tape: fifteen rows by call to the older cells, six against the tape's lines, and four holes the older
code never held — the ban on the seven nations, show them no favor, your eye shall not pity, no abomination into the house — compiled here and written
at the day the chapter is spoken. Two effects that had waited in the registry since Exodus were written on the tape for the first time. The docket read
the tractate on idolatry whole — five hundred and twenty rows, every one read entire before its verdict, seventy-five of them digressions named as such.
The runner matched its answer sheet on the first run; the tape reached ten of ten on the second, the first run's one miss four older checkpoints that
count Israel's debits, moved by the new one and retyped from the print; every probe suite and every gate green in one chain, the sweep whole. Next: the
commit on your word; then chapter 8's reading — or the schema sitting first, on your word.
"""

# ---- 7. THE_BRIEFING ----
BRIEF_BULLET_ANCHOR = "- **CHAPTER 7 READ AND FROZEN — THE SEVEN NATIONS:"
BRIEF_BULLET = ("- **CHAPTER 7 COMPILED — THE OLD LAW SAID AGAIN FOR THE NEW PLACE, GRADED AGAINST THE CELLS THAT COMPILED IT FIRST; FOUR HOLES COMPILED AT THE CHAPTER'S OWN DAY; TWO EFFECTS FROM EXODUS WRITTEN ON THE TAPE FOR THE FIRST TIME** "
                "(2026-09-18, on your \"Go\" and \"keep going\"; World/step9/DEUTERONOMY_WALK.md \"Sitting 5b\" + AS BUILT): cold_run_seven_nations.py the 62nd runner (51/51), law_seven_nations the 67th daemon (%d functions); the readback on the kin twenty-one rows; the tape 10/10 with RUN (1307, 96, 88, 0, 12, 1602, 38, 319, pairs, 127) as predicted, markers 167; the docket 520 rows every one read whole from the start; every gate GREEN, the sweep %d/62. NEXT: the commit on your word; chapter 8's reading, or the schema sitting first.\n" % (DG[1], SW_P))
BRIEF_ENTRY_ANCHOR = "### 2026-09-18 — CHAPTER 7 READ: THE SEVEN NATIONS, AND A CHAPTER THE SHELF DOES NOT EXPOUND\n"
BRIEF_ENTRY = """### 2026-09-18 — CHAPTER 7 COMPILED: THE OLD LAW GRADED AGAINST ITS FIRST TELLING, AND THE HOLES FILLED

Chapter 7 is Deuteronomy doing what you asked about at the reading — altering old code and then creating new. Most of its verses say again what Exodus
and Numbers said first: no covenant with the nations, no marriage, break their altars, the hornet, little by little. So this sitting did not compile
those again. It graded each verse against the cell that compiled the law the first time — the machine called the old cell and read its verdict — the
way the earlier sittings graded Moses' retellings against the tape: fifteen rows that way, six against the tape's own lines, twenty-one in all, and the
grades came out exactly as the design predicted. What no old cell held is the new code: the ban on the seven nations, show them no favor, your eye shall
not pity, no abomination into your house — four cells compiled here and written at the day the chapter is spoken, the ban a debt on Israel that stays
open until Joshua. Two effects that had sat in the registry since Exodus — the covenant barred, the marriage barred — reached the tape for the first
time, because their first tellings were conditions for the land and this chapter gives them at Moab. The Talmud's tractate on idolatry was read whole for
the answer sheet, five hundred and twenty rows, and it supplied two things the text states bare: why the Asherim had to be burned rather than revoked,
and that the ban has a condition — the nations that repent are accepted. One rule in the chapter, the pity, has no row on the shelf at all; the machine
holds it on the verse alone and says so. The runner matched its sheet on the first run; the tape reached ten of ten on the second — the new debt moved
four old counts, retyped from the print; every gate is green in one chain. Next, on your word: the commit, then chapter 8 — or the schema question first.

"""

# ---- 8. THE_LOOP step-6 row ----
LOOP_OLD = "readback_probes 15/15, CO4) | the three forms BUILT — acts (1b), laws (3b), a retelling inside a law (4b); the second pass after Deuteronomy |"
LOOP_NEW = ("readback_probes 15/15, CO4); cold_run_seven_nations.py (chapter 7, THE LAWS' FORM ON THE KIN 2026-09-18 — the code re-said for the new place graded against the KIN'S CELLS by CALL and the tape's lines: twenty-one rows VERBATIM 4 / VARIANT 5 / EXPANDED 8 / TURNED 3 / SHORTENED 1, four holes compiled; "
            "readback_probes 18/18, CQ4) | the three forms BUILT — acts (1b), laws (3b, and on the kin 5b), a retelling inside a law (4b); the second pass after Deuteronomy |")

# ---- 9. RESUME ----
RESUME_HEAD = """# ⚠ THE DEUTERONOMY WALK sitting 5b (2026-09-18; step9/DEUTERONOMY_WALK.md "Sitting 5b" + "Sitting 5b — AS BUILT"): CHAPTER 7 COMPILED —
# step9/cold_run_seven_nations.py the 62nd runner (51/51; six cells; THE READBACK ON THE KIN — twenty-one rows, fifteen by CALL to the kin's cells, six on
# the tape; four holes compiled), law_seven_nations the 67th daemon (given_at Deut 7:1, boot); THREE LINES on the counter's own day (40, 11, 1), NO marker —
# the ban a DEBIT on Israel OPEN to Joshua, covenant_barred and intermarriage_barred written on the tape for the first time, favor_barred, pity_barred,
# house_abomination_barred three new blocks, blessings_for_hearing a conditional heaven entry; the tape 10/10 on its second run with RUN (1307, 96, 88, 0,
# 12, 1602, 38, 319, pairs, 127) as predicted, PREVIOUS_RUN 4b's exactly, markers 167, closes 127 (four older debit-count checkpoints retyped); the docket
# 520 rows read whole from the start; every probe suite and gate GREEN, the sweep %d/62.
# NEXT on the ruling: the commit on the owner's word; chapter 8's reading (8:1-20) — or the schema sitting first, on his word.
""" % SW_P

# ---- 10. THE STATE DOC — #195 ADDENDUM 7 ----
STATE_ADD = """
#195 ADDENDUM 7 (2026-09-18, at the close of THE DEUTERONOMY WALK sitting 5b — THE COMPILE OF CHAPTER 7, RUN 4 of four — A CLEAN COMPACTION POINT): THE
SITTING RAN IN FOUR RUNS on the owner's "Go" (RUN 1 — #194 addendum 4), "Go" after the reread (RUN 2 — #195 addenda 2-3), "keep going" (RUN 3 — #195
addenda 4-6) and "keep going" (RUN 4 — this): the gates chain in one summary (ALL GREEN), the records from the sheet in one call, the forms copied; the
map's "Sitting 5b — AS BUILT" is the record (the eleven departures, the eleven lessons, the gates computed from their prints); the chain run twice — the first stopped at the dependency gate by ONE demand (the king / Molech homograph at 7:8, FALSE; no pointer demanded — the design's seven not asked for), the second from that step ALL GREEN. THE STATE: cold_run_seven_nations.py
the 62nd runner (51/51), law_seven_nations the 67th daemon (%d daemons, %d functions), the registries 1129 kinds / 1029 effects, the tape 10/10 with RUN
(1307, 96, 88, 0, 12, 1602, 38, 319, the four pairs, 127) and PREVIOUS_RUN 4b's exactly, markers 167 (F 129 / P 15 / R 23), entities 319, closes 127, the
population table 148; the docket logic/oral_triage/deu_07_vaetchanan_ekev_exam_2026-09-18.md (%d rows, every row read whole from the start); THE READBACK
ON THE KIN BUILT (twenty-one rows: VERBATIM 4, VARIANT 5, EXPANDED 8, TURNED 3, SHORTENED 1 — the laws' form on another chapter's code); THE CODE'S FOUR
HOLES compiled at the chapter's own day, statute by form; two old effects written on the tape for the first time; the corpus unmoved (221 units, standing
2209, hash 8b8fff1fa28953af — no freeze this sitting). THE GATES: the probe suites %s; %s. THE RECORDS written: the map's AS BUILT, COMPILE_DEBT (the
sitting-5 box PAID; the 5b box with seven owed items), MIDDOT's docket entry (twenty-one rules about rules), MISHNAH_TOPICS (fourteen rows), RESEARCH_LOG,
THE_STEPS, THE_BRIEFING (the bullet and the entry), THE_LOOP's step-6 row (the laws' form on the kin), World/RESUME.md, the recovery page rewritten, the
addenda's section 42, RECORD_FORMS' pointer, memory (deuteronomy-walk.md, MEMORY.md under 17,000 bytes); the forms copied by copy_ch7b_forms.py. NOT
COMMITTED (the tree uncommitted since 64a8362 — the owner's word only; NOT PUSHED); the commit message drafted at <scratch>/commit_msg_ch7.txt (the
reading, the tutorial, the design thread's files, 5b's four runs). NEXT ON THE RULING: the commit on the owner's word; then CHAPTER 8's reading (8:1-20 —
the manna and the humility, the good land, the forgetting; the reading shape in four runs, every row whole) — or the Decalogue-schema sitting first (ON
THE TABLE, not a ruling). IF THIS COMPACTS HERE: reread the recovery page, the map's "Sitting 5b — AS BUILT" and MEMORY.md; nothing is mid-flight.
""" % (DG[0], DG[1], NROWS, pr_line, gates_line)

# ---- 11. THE RECOVERY ADDENDA — section 42 ----
ADDENDA_ADD = """

## 42. ADDENDUM (2026-09-18, THE DEUTERONOMY WALK sitting 5b — THE COMPILE OF CHAPTER 7, Deuteronomy 7:1-26 COMPILED AND ON THE TAPE in four runs; the owner: "Go", "Go", "keep going", "keep going"; the state doc's #195 addendum 7)

THE SITTING RAN IN THE COMPILE SHAPE IN FOUR RUNS (section 5; "Sitting 4b" the form): World/step9/DEUTERONOMY_WALK.md "Sitting 5b" (the design, written
before any code) and "Sitting 5b — AS BUILT" (the departures and the ten lessons). THE STATE: cold_run_seven_nations.py the 62nd runner (51/51 — six cells,
nineteen DATA rows, the readback's twenty-one rows and four holes, fourteen exam persons), law_seven_nations the 67th daemon (given_at Deut 7:1,
installed_by boot; %d daemons, %d functions), event_vocabulary +4 (1129), effect_vocabulary +4 (1029 — blessings_for_hearing, not the design's
blessing_promised, Abram's), dependency_dispositions +15 edges (thirteen CALL, the registration, one FALSE — the king / Molech homograph at 7:8) and NO pointer (%d edges, %d pointers on file); THE TAPE 10/10 WITH
THE REST ON ITS SECOND RUN — RUN (1307, 96, 88, 0, 12, 1602, 38, 319, the four pairs, 127) as predicted, PREVIOUS_RUN 4b's EXACTLY (no declared delta),
NEWEST_RUNNER seven_nations, markers 167 UNMOVED, entities 319, closes 127, the population table 148, CQ1-CQ9 MATCH (the first run's one miss: four older
debit-count checkpoints CV2, CX2, CW3, CR3 retyped from the print); the docket logic/oral_triage/deu_07_vaetchanan_ekev_exam_2026-09-18.md (%d rows —
link %d / topic %d; LAW %d; OUTSIDE %d; credited %d; EVERY ROW READ WHOLE FROM THE START). THE GATES: the probe suites %s; %s.

WHAT THE SITTING FOUND (RESEARCH_LOG 2026-09-18, the compile entry): THE READBACK ON THE KIN — the laws' form run on another chapter's code, the kin's
cells the first telling by CALL; THE CODE'S FOUR HOLES compiled at the chapter's own day; TWO OLD EFFECTS written on the tape for the first time
(covenant_barred, intermarriage_barred both ways); THE REGISTRY DECIDES A NAME (blessing_promised was Abram's); A DEBIT MOVES THE OLDER COUNTS (the four
checkpoints); THE SHELF'S REASON AND CONDITION for the demolition (the calf's agency) and the ban (repentance; the Land's border); THE PITY'S HOLE with
no row on the shelf. THE ELEVEN LESSONS in the map's AS BUILT.

THE FILES CHANGED BY 5b: World/step9/cold_run_seven_nations.py (new), cold_run_sequence.py (the three lines under "# ---- Deut 7 ----", the literals,
CQ1-CQ9, four older checkpoints retyped), event_vocabulary.yaml, effect_vocabulary.yaml, daemon_dispositions.yaml, dependency_dispositions.yaml (the
span, fifteen edges, no pointer), readback_probes.py (Q16-Q18; Q17 retyped), installation_probes.py (I5 67), checkpoint_positions.yaml (rebuilt),
DAEMON_INDEX.md and DEPENDENCY_INDEX.md (regenerated), the docket (new), the forms folder (copy_ch7b_forms.py), the records (the map, COMPILE_DEBT, MIDDOT,
MISHNAH_TOPICS, RESEARCH_LOG, THE_STEPS, THE_BRIEFING, THE_LOOP, RESUME, RECORD_FORMS, the recovery page, this file, the state doc, memory). NOT COMMITTED —
the tree uncommitted since 64a8362; commit on the owner's word only.

NEXT ON THE RULING: the commit on the owner's word; then CHAPTER 8's READING (8:1-20 — the manna and the humility, the good land, the forgetting; the
reading shape in four runs, every row whole). ON THE TABLE, NOT A RULING: the Decalogue-schema sitting; THE INSTALL HYPOTHESIS (tested in passing at 5b).
""" % (DG[0], DG[1], DP[0], DP[1], NROWS, NLINK, NTOPIC, VD['LAW'], VD['OUTSIDE'], NCRED, pr_line, gates_line)

# ---- 12. THE RECOVERY PAGE — rewritten whole under its cap (section 2 replaced; sections 4, 5, 6 retouched) ----
def f_recovery(s):
    i = s.index('## 2. WHERE IT STANDS'); j = s.index('## 3. THE STANDING LAWS')
    sec2 = """## 2. WHERE IT STANDS (2026-09-18, after 5b; the state doc #195 addendum 7)
- NUMBERS CLOSED. DEUTERONOMY 1:1-7:26 READ, FROZEN, COMPILED AND ON THE TAPE (1-6 at 64a8362, PUSHED; chapter 7 sittings 5 and 5b).
- 221 frozen units, standing 2209, hash 8b8fff1fa28953af. 62 runners, 67 daemons, %d functions; registries 1129 kinds / 1029 effects.
- THE TAPE at RUN (1307, 96, 88, 0, 12, 1602, 38, 319, the four pairs, 127), markers 167, closes 127; the sweep %d/62; every gate GREEN;
  the register gate DECLARED %d / DEBT 0. The readback's fourth form (5b): the laws' form on the kin's cells.
- Uncommitted since 64a8362: sittings 5 and 5b, the tutorial, the design thread; the message at <scratch>/commit_msg_ch7.txt.
- NEXT ON HIS WORD: the commit; then CHAPTER 8 (8:1-20) or the schema sitting (on the table).

""" % (DG[1], SW_P, RG[0])
    s = s[:i] + sec2 + s[j:]
    old4 = "(61 runners;\ncold_run_hear_o_israel.py the newest form)"; assert s.count(old4) == 1, s.count(old4)
    s = s.replace(old4, "(62 runners;\ncold_run_seven_nations.py the newest form)")
    old5 = 'the newest instances: the map\'s "Sitting 5" and "Sitting 4b")'; assert s.count(old5) == 1
    s = s.replace(old5, 'the newest instances: the map\'s "Sitting 5" and "Sitting 5b")')
    old6 = "- Deuteronomy's sittings: the map; the addenda §31-41 (§39 the whole-row rule). The cost cuts: §35."; assert s.count(old6) == 1
    s = s.replace(old6, "- Deuteronomy's sittings: the map; the addenda §31-42 (§39 the whole-row rule). The cost cuts: §35.")
    assert len(s.encode('utf-8')) <= 10240, ('THE RECOVERY PAGE OVER ITS CAP', len(s.encode('utf-8')))
    return s

# ---- 13. MEMORY ----
MEM_DESC_OLD = 'SITTING 5 DONE 2026-09-18 (chapter 7 READ AND FROZEN'
MEM_PARA = """

SITTING 5b DONE 2026-09-18 (the owner: "Go", "Go", "keep going", "keep going" — four runs, the compaction #195 after run 1; the map's "Sitting 5b" + AS BUILT):
CHAPTER 7 COMPILED — cold_run_seven_nations.py the 62nd runner (51/51), law_seven_nations the 67th daemon (given_at Deut 7:1, boot). THE READBACK ON THE
KIN: the laws' form run on ANOTHER chapter's code — the kin's cells (ordinances.land, erection.covenant, journeys.the_command, covenant_at_horeb's words)
the first telling by CALL, fifteen rows; six on the tape; twenty-one rows VERBATIM 4 / VARIANT 5 / EXPANDED 8 / TURNED 3 / SHORTENED 1; the code's four
holes (the ban — a DEBIT on Israel OPEN to Joshua; no favor; no pity — on the ink alone; the abomination into the house) compiled at the chapter's own day
(40, 11, 1), three lines STATUTE by form, no marker; covenant_barred and intermarriage_barred (both ways) WRITTEN ON THE TAPE FOR THE FIRST TIME;
blessings_for_hearing the heaven entry (blessing_promised was Abram's — the registry decides). The tape 10/10 on its SECOND run with RUN (1307, 96, 88,
0, 12, 1602, 38, 319, pairs, 127), PREVIOUS_RUN 4b's exactly, markers 167 (four older debit-count checkpoints retyped from the print); the docket 520 rows
EVERY ROW READ WHOLE FROM THE START (OUTSIDE 75); every gate green, the sweep 62/62. ⚠ LESSONS (eleven, in the map): a registry name may already exist; the
census decides the first verse; the exam asks return verdicts, the write asks writes; a DEBIT moves the older commanded-count literals; the callees'
facts print first; a probe retyped once; a guard names the sitting; a hole may have no row on the shelf; the whole-range scan's credits are not the
docket's; the shelf teaches the reason (the calf's agency) and the condition (repentance) of a command; the census reads homographs (king / Molech FALSE) and demanded none of the design's seven pointers. NOT COMMITTED (since 64a8362). NEXT on the ruling:
the commit; chapter 8's reading (8:1-20) or the schema sitting.
"""
MEM_IDX_OLD = 'chapters 1-6 COMPILED (64a8362 PUSHED); SITTING 5 DONE 2026-09-18 (ch 7 FROZEN, 221 units); 5b RUN 4 IN FLIGHT (the chain; state doc #195 add. 8)'   # the walk line's stale clauses, folded (the cap)
MEM_IDX_NEW = 'chapters 1-7 COMPILED (1-6 at 64a8362 PUSHED; 7 on 2026-09-18, sittings 5 and 5b, 221 units, UNCOMMITTED); NEXT: commit on his word, then ch 8'

# ---- 14. RECORD_FORMS — the writer's form pointer ----
FORMS_OLD = "World/step9/forms_deuteronomy_walk/write_ch6b_records.py (write_ch5b_records.py and write_ch4b_records.py the earlier forms). Keep this sheet current"
FORMS_NEW = "World/step9/forms_deuteronomy_walk/write_ch7b_records.py (write_ch6b_records.py, write_ch5b_records.py and write_ch4b_records.py the earlier forms). Keep this sheet current"

# ---- THE WRITES (every text built above; the files opened only now) ----
def read(p): return open(p if p.startswith('/') else f'{ROOT}/{p}', encoding='utf-8').read()
def write(p, s): open(p if p.startswith('/') else f'{ROOT}/{p}', 'w', encoding='utf-8').write(s)
plans = []
def f_map(s):
    assert 'RUN 3 — AS RUN (2026-09-18, on "keep going"' in s and '## Sitting 5b — THE COMPILE OF CHAPTER 7 — AS BUILT' not in s
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
    assert s.count(BRIEF_BULLET_ANCHOR) == 1 and s.count(BRIEF_ENTRY_ANCHOR) == 1 and '## SCOREBOARD (as of 2026-09-18, latest)\n' in s, (s.count(BRIEF_BULLET_ANCHOR), s.count(BRIEF_ENTRY_ANCHOR))
    s = s.replace(BRIEF_BULLET_ANCHOR, BRIEF_BULLET + BRIEF_BULLET_ANCHOR)
    return s.replace(BRIEF_ENTRY_ANCHOR, BRIEF_ENTRY + BRIEF_ENTRY_ANCHOR)
plans.append(('THE_BRIEFING.md', f_brief))
def f_loop(s):
    assert s.count(LOOP_OLD) == 1; return s.replace(LOOP_OLD, LOOP_NEW)
plans.append(('World/step9/THE_LOOP.md', f_loop))
plans.append(('World/RESUME.md', lambda s: RESUME_HEAD + s))
plans.append(('logic/pre_logic_methods_2026-07-28/PROMPT_continue_solo_era_2026-08-06.md', lambda s: s.rstrip('\n') + '\n' + STATE_ADD))
plans.append(('logic/pre_logic_methods_2026-07-28/RECOVERY_addenda_2026-09-12.md', lambda s: s.rstrip('\n') + ADDENDA_ADD))
plans.append(('logic/pre_logic_methods_2026-07-28/RECOVERY_new_thread_2026-09-12.md', f_recovery))
def f_forms(s):
    assert s.count(FORMS_OLD) == 1; return s.replace(FORMS_OLD, FORMS_NEW)
plans.append(('World/step9/RECORD_FORMS.md', f_forms))
def f_mem(s):
    assert s.count(MEM_DESC_OLD) == 1
    s = s.replace(MEM_DESC_OLD, 'SITTING 5b DONE 2026-09-18 (chapter 7 COMPILED — the readback on the kin; the four holes at the chapter\'s own day; two Exodus effects on the tape for the first time; uncommitted); ' + MEM_DESC_OLD, 1)
    return s.rstrip('\n') + '\n' + MEM_PARA
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
