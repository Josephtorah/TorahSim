#!/usr/bin/env python3
import os as _os, subprocess as _sp
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
# THE DEUTERONOMY WALK sitting 6b — THE COMPILE OF CHAPTER 8, RUN B (2026-09-19): THE RECORDS, written after every gate ran — the numbers COMPUTED from the
# gates chain's own prints in the scratchpad (gates_ch8b/*.out; never recited) and the docket's own rows; every text built whole before any file is
# opened; the ledgers appended, the map appended, the checklist's boxes marked paid, the recovery page REWRITTEN in its section 2 under its cap, the
# memory index edited under its cap. `--check` parses and prints without writing. Sitting 5b's form (write_ch7b_records.py) on the sheet World/step9/RECORD_FORMS.md.
import os, re, sys, subprocess
ROOT = _ROOT
SP = os.path.dirname(os.path.abspath(__file__))
G = f'{SP}/gates_ch8b'
MEM = os.path.expanduser('~/.claude/projects/-Users-Shared-TorahSim/memory')
CHECK = '--check' in sys.argv
def rd(name): return open(name if name.startswith('/') else f'{G}/{name}', encoding='utf-8', errors='ignore').read()
def last_frac(name, m):
    t = rd(name); hits = re.findall(r'(\d+)/%d\b' % m, t); assert hits, (name, 'no n/%d' % m); return int(hits[-1])
# ---- THE NUMBERS FROM THE PRINTS ----
summ = rd('SUMMARY.txt'); assert 'GATES CHAIN DONE — ALL GREEN' in summ, summ
tape = rd('tape.out'); assert '10/10 checkpoints' in tape and 'OK   THE REST' in tape
CU = re.findall(r'CHECKPOINT (CU\d) .*? (MATCH|MISS|DIVERGE)$', tape, flags=re.M); assert len(CU) == 9 and all(v == 'MATCH' for _, v in CU), CU
tape_elapsed = re.search(r'elapsed ([\d.]+)s', tape).group(1)
PL = re.search(r"PLACEMENT \(O9 T2\): markers (\{[^}]*\}); events (\{[^}]*\})", tape); assert PL
assert PL.group(2) == "{'text_constrained': 109, 'page_order': 1146, 'reading_placed': 55}", PL.group(2)
rg = rd('register.out'); m = re.search(r'DECLARED (\d+); DEBT (\d+); FAILS (\d+)', rg); assert m and 'THE REGISTER GATE: GREEN' in rg
RG = tuple(int(x) for x in m.groups())
assert not re.search(r'^\s*Deut 8:\d+\s+(CHAPTER|DAEMONS|ACT|CLOSE|RUN)', rg, flags=re.M), 'a seat in chapter 8 appeared'   # no receipt form in the chapter (the design's measure; the runner's F1 no_receipt)
dg = rd('daemon.out'); m = re.search(r'\((\d+) daemons, (\d+) functions\)', dg); assert m and 'gate satisfied' in dg; DG = tuple(int(x) for x in m.groups())
dp = rd('dependency.out'); m = re.search(r'dispositions on file: (\d+) edges, (\d+) pointers', dp); assert m and 'gate satisfied' in dp; DP = tuple(int(x) for x in m.groups())
LC = re.search(r'LINK CENSUS \(the link review law\): reference (\d+), transfer (\d+), hypothesis (\d+), none (\d+)', dp); assert LC; LC = tuple(int(x) for x in LC.groups())
m = re.search(r'required edges (\d+), required pointers (\d+); live import edges (\d+)', dp); DPR = tuple(int(x) for x in m.groups())
bw = rd('build.out'); assert 'ALL GREEN' in bw, bw[-600:]
jg = rd('journal2.out'); assert 'GATE GREEN' in jg and 'GATE GREEN' in rd('journal.out'); m = re.search(r'(\d+) kinds, (\d+) rows in the index', jg); JG = tuple(int(x) for x in m.groups())
sw = rd('sweep.out'); SW_P = len(re.findall(r'^PASS +cold_run_\w+\.py', sw, flags=re.M)); SW_F = len(re.findall(r'^FAIL +cold_run_\w+\.py', sw, flags=re.M))
SW_CELLS = sum(int(a) for a, b in re.findall(r'score=(\d+)/(\d+)', sw)); assert SW_P + SW_F == 63, (SW_P, SW_F); assert SW_F == 0, 'the sweep has failures — read them first'
po = rd('positions.out'); m = re.search(r'(\d+) checkpoints over (\d+) pauses', po); assert m, po[-800:]; PO = tuple(int(x) for x in m.groups())
PR = {'census': last_frac('probe_census.out', 224), 'installation': last_frac('probe_installation.out', 6), 'readback': last_frac('probe_readback.out', 21),
      'register': last_frac('probe_register.out', 7), 'sequence': last_frac('probe_sequence.out', 4), 'view': last_frac('probe_view.out', 6),
      'population': last_frac('probe_population.out', 9), 'journal': last_frac('probe_journal.out', 7), 'cursor': last_frac('probe_cursor.out', 6),
      'large_letter': last_frac('probe_large_letter.out', 6), 'checkpoint': last_frac('checkpoint.out', 7)}
ck = rd('probe_clock.out'); m = re.findall(r'(\d+)/(\d+)', ck); PR['clock'] = ('%s/%s' % m[-1]) if m else 'exit 0'
assert PR['checkpoint'] == 7 and PR['readback'] == 21 and PR['installation'] == 6 and PR['large_letter'] == 6, PR
run1 = rd(f'{SP}/ch8_run1.out'); assert '55/55' in run1
CASES_N = int(re.search(r'CASES generated: (\d+)', rd(f'{SP}/ch8_cases_gen.out')).group(1)); PER_CELL = re.search(r'per cell (\{.*?\})', rd(f'{SP}/ch8_cases_gen.out')).group(1)
t1 = rd(f'{SP}/ch8_tape1.out'); assert '9/10 checkpoints' in t1 and "'CC7 DIVERGE'" in t1, 'the first tape run: 9/10, CC7 the miss'
# the docket's numbers from its own rows
DK = 'logic/oral_triage/deu_08_ekev_exam_2026-09-19.md'
dk = open(f'{ROOT}/{DK}', encoding='utf-8').read()
rows = [l for l in dk.split('\n') if re.match(r'^- .*? — (LAW|DERIVATION|DISPUTE|CONTEXT|OUTSIDE)\.', l)]
VD = {v: sum(1 for l in rows if re.match(r'^- .*? — %s\.' % v, l)) for v in ('LAW', 'DERIVATION', 'DISPUTE', 'CONTEXT', 'OUTSIDE')}
NROWS = len(rows); NLINK = sum(1 for l in rows if '[LINK' in l); NTOPIC = sum(1 for l in rows if '[TOPIC' in l); NCRED = sum(1 for l in rows if 'CREDITED' in l)
NWHOLE = sum(1 for l in rows if '[whole:' in l); DKB = len(dk.encode('utf-8'))
assert NROWS == 451 and NLINK + NTOPIC == NROWS and NWHOLE == 0, (NROWS, NLINK, NTOPIC, NWHOLE)
hp = subprocess.run(['python3', 'logic/solo_tools/scrub_home_paths.py', '--check'], cwd=ROOT, capture_output=True, text=True); assert hp.returncode == 0, hp.stdout[-500:] + hp.stderr[-500:]
NUM = dict(RG=RG, DG=DG, DP=DP, LC=LC, DPR=DPR, JG=JG, SW=(SW_P, SW_CELLS), PO=PO, PR=PR, PL=PL.groups(), tape_elapsed=tape_elapsed, cases=(CASES_N, PER_CELL), docket=(NROWS, NLINK, NTOPIC, NCRED, NWHOLE, DKB, VD))
print('THE NUMBERS:', NUM)
pr_line = ('census %d/224, installation %d/6 (I5 68), readback %d/21 (Q19-Q21 the fifth form), register %d/7, clock %s, sequence %d/4, view %d/6, population %d/9, journal %d/7, cursor %d/6, large_letter %d/6, checkpoint %d/7'
           % (PR['census'], PR['installation'], PR['readback'], PR['register'], PR['clock'], PR['sequence'], PR['view'], PR['population'], PR['journal'], PR['cursor'], PR['large_letter'], PR['checkpoint']))
gates_line = ('the daemon gate GREEN (%d daemons, %d functions WRAPPED); the dependency gate GREEN (%d edges and %d pointers on file — the link census reference %d / transfer %d / hypothesis %d / none %d; required %d edges and %d pointers, live import edges %d); '
              'build_world ALL GREEN (222 units, standing 2215, hash 8b8fff1fa28953af unmoved — no freeze this run); the journal gate GREEN twice — before and after the sweep (%d kinds, %d rows in the index); THE REGISTER GATE --strict GREEN (DECLARED %d, DEBT %d, FAILS %d — no seat in chapter 8: no receipt form in it, as the design measured and the runner\'s F1 asserts by the finder\'s own rule); '
              'the positions table %d checkpoints over %d pauses (CU1-CU9 in it; checkpoint_probes %d/7 after the rebuild); the sweep %d/63 at %s graded cells; the home-path gate GREEN'
              % (DG[0], DG[1], DP[0], DP[1], LC[0], LC[1], LC[2], LC[3], DPR[0], DPR[1], DPR[2], JG[0], JG[1], RG[0], RG[1], RG[2], PO[0], PO[1], PR['checkpoint'], SW_P, format(SW_CELLS, ',')))
docket_line = ('%d rows (link %d / topic %d; LAW %d, DERIVATION %d, DISPUTE %d, CONTEXT %d, OUTSIDE %d; credited %d; %s bytes), EVERY ROW READ WHOLE FROM THE START — no cut, no overlay (the parts\' WHOLE dicts empty, the correction counts zero and computed)'
               % (NROWS, NLINK, NTOPIC, VD['LAW'], VD['DERIVATION'], VD['DISPUTE'], VD['CONTEXT'], VD['OUTSIDE'], NCRED, format(DKB, ',')))
W6 = "THE DEUTERONOMY WALK sitting 6b"

# ---- 1. THE MAP — AS BUILT ----
AS_BUILT = """
## Sitting 6b — THE COMPILE OF CHAPTER 8 — AS BUILT (2026-09-19; the design above stands as written but for the departures below; RUN A the design
## on 2026-09-18, THE DOCKET its own run and RUN B on "Go run b", 2026-09-19 — THE TWO-RUN RULE's first compile sitting, the docket clause applied)

THE RUN: cold_run_good_land.py the 63rd runner — %d/%d on its FIRST graded run (six cells, %d asks — per cell %s; the CASES generated from the cells'
own asks and frozen under the honest-pairing guard, the guard's count read from the generator's print after one trip: a grep counted 54 where a label
carried an apostrophe); law_good_land the 68th daemon (given_at Deut 8:1, installed_by boot); THE READBACK'S FIFTH FORM — THE RETELLING OF A STATE:
eighteen rows VERBATIM 6 / VARIANT 5 / EXPANDED 4 / TURNED 2 / SUPPLIED 1 AS PREDICTED, ten found on the tape by kind and first verse, seven in the
kin's cells by CALL, the one SUPPLIED row 8:4's (the garment and the foot) with its ledger scan EMPTY on the one database at build and on the running
world at CU7 — NO retrograde write (the design's decision, open to the owner; the docket found no row on 8:4 — the shelf does not challenge it); the
three holes named (the grace, the forgetting, the testimony REUSED); eighteen DATA rows (the four the docket added: the grace conditional on eating,
the four blessings' three divisions, the blessing before refuted, the heart lifted); thirteen exam persons, four exempt, NO LASHES (the chapter's one
prohibition has no action — Makkot 13b:6). THE TAPE 10/10 ON ITS SECOND RUN with RUN (1310, 96, 88, 0, 12, 1605, 39, 319, the four pairs, 127) AS THE
DESIGN'S ARITHMETIC WROTE IT, PREVIOUS_RUN 5b's exactly (no declared delta), PLACEMENT page_order 1143 -> 1146 and CENSUS on tape 1307 -> 1310, kinds 852
-> 855 read at the stitcher's print as predicted, markers 167, closes 127, entities 319 unmoved, CU1-CU9 MATCH (%s s); THE FIRST RUN 9/10 — ONE OLDER
CHECKPOINT MOVED: chapter 4's CC7 holds the current count of heaven_and_earth_witness on Israel as a literal (ONE), and the reuse at 8:19 is a second
entry on the same ledger — retyped from the print (1 -> 2, its note dated; 5b's lesson a second time, on a status count). THE TYPES: kinds 1129 -> 1133,
effects 1029 -> 1031 (bless_after_eating_commanded a status, forgetting_barred a block; the testimony's effect present, reused), daemons 67 -> 68 (I5
68), THIRTEEN CALL edges and the registration (the design's fourteenth, decalogue, DROPPED at the callees' print — that runner holds no cell on the
second word; the first copy's clause rides covenant_at_horeb's cell). THE PROBES: readback_probes Q19-Q21 written to FAIL before the runner (18/21),
21/21 after. THE GATES (one chain, %s): %s; the twelve probe suites — %s. THE DOCKET (its own run, 2026-09-19): %s.

THE DEPARTURES FROM THE DESIGN (thirteen, each read from a print): (1) the decalogue CALL edge dropped — no cell on the second word in
cold_run_decalogue (its cells altar_rules, sabbath_clauses, theft_commandment, vain_name); the census demanded nothing there; (2) the testimony's tape verse
is 4:25, not 4:26 — the line witnesses_called's source begins at 4:25 (the LINE's first verse, read at the runner); (3) CU2's source "Deut 8:7", not
8:10 — the effect carries its LINE's source (5b's form); (4) the DATA rows eighteen, not fourteen — the docket's four; (5) the exam's persons thirteen
and no lashes person — the watch list keeps lashes as the case kind's standard, unfired; (6) F3 twenty asks — the docket's crowns became exam rows (the
measure of "satisfied", less than an egg-bulk, the blessing before, the four blessings, the grace conditional, the Sabbath forgotten, the persons, the
meal's base, the first fruits, any language, the meal's end); (7) CC7 retyped — the design said "no retype of the older REST literals expected" and was
wrong on one: a REUSE is a second entry on an older count; (8) the register gate's finder RULE replicated in the runner (its module imports
cold_run_sequence — circular from a runner), and it found chapter 1's THREE seats where the design's memory held two (1:19 the CHAPTER seat the probes
list) — typed from the fast checker's print; (9) the state's word list WORD-BOUNDED after the first pass's bare "wore" matched "swore" in the blessings'
value (the fast checker's print); (10) the guard's count from the generator's print (%d), never a grep; (11) the readback's rb() form extended — a
SUPPLIED row has no tape line and no cell and carries its ledger scan (the assertion form of the fifth grade); (12) opening_speech.the_commission holds
no ask for 1:19 — the wilderness row cites OS.READBACK's own row 1:19 (the first form's table: the cloud lifted at Numbers 10:11); (13) 5:6's formula
is CH.the_first_tablet('the_first_word'), not the second word's header. THE RECORDER AND THE STITCHER: their forms carry the root line in two shapes —
the derivation by count failed once, by regex it held (a lesson for the sed). THE CHAIN RUN TWICE: the first stopped at the dependency gate by ONE
demand — a POINTER at 8:5 in the AS_WHEN form ("as a man disciplines his son": the census reads the 'as' as a citation form) — dispositioned RUN_CITATION of
1:31's carrying by the readback row (add_pointers_ch8.py, the tokens checked on the DB); NO EDGE demanded; the design's eight predicted RUN_CITATION pointers
the census asked for as ONE (4b's and 5b's lesson a third time — the pointer list is a prediction, the census decides); the second chain from that step ALL GREEN.

THE LESSONS (eleven, for the next compile): (1) A REUSED EFFECT IS A SECOND ENTRY ON THE SAME LEDGER — an older checkpoint's count literal moves (the
count-literal lesson's third class: 3b's closes, 5b's debits, now a status); (2) a design's tape verse is the LINE's first verse, not the verse the
retelling cites — read the line's source at the runner; (3) the callees' print before the asserts found two design holes (no second-word cell in the
decalogue runner; no 1:19 ask in the commission) — the print decides the edges, then the census; (4) a word list for a ledger scan is word-bounded; (5)
a gate's rule is replicated, not imported, when the import is circular — and the replica found a seat the design forgot; (6) the count of generated
cases is read from the generator's print; (7) THE FIFTH FORM HELD: a state has no line, no closer, no lashes and no write — the SUPPLIED grade with the
ledger scan asserted at build and at the tape, the decision the owner's; (8) the docket's crowns become exam rows — the compile grows by the shelf
(F3's twenty asks), as the design's (n) allowed; (9) a derivation by sed on a form with a repeated line goes by regex, not by count; (10) THE TWO-RUN
RULE HELD ON ITS FIRST COMPILE SITTING with the docket clause applied — RUN A the design (a clean point), the docket its own run (a clean point), RUN B
this (the probes to fail, the types, the runner in parts with the fast checker, the recorder and the stitcher, the literals, the tape twice, the chain
once, the records in one call) — the checkpoint prefix space now ends: CU was the last two-letter prefix, the next compile opens a new series (owed forward); (11) the census asks for the
pointers it needs and no other — eight predicted, one demanded (8:5's 'as'), the chain run twice as 5b's was.
""" % (CASES_N, CASES_N, CASES_N, PER_CELL, tape_elapsed, 'ALL GREEN', gates_line, pr_line, docket_line, CASES_N)

# ---- 2. COMPILE_DEBT — the sitting-6 box marked PAID + the 6b box ----
DEBT_HDR_OLD = "## deu_08_ekev_2026-09-18.md, 36 sources; one unit deu_08_manna_humility FROZEN, the 222nd) — OWED TO THE COMPILE (sitting 6b): (a) THE BLESSING AFTER THE MEAL"
DEBT_HDR_NEW = "## deu_08_ekev_2026-09-18.md, 36 sources; one unit deu_08_manna_humility FROZEN, the 222nd) — PAID AT 6b (the 6b box below, item by item) — AS WRITTEN AT THE READING, OWED TO THE COMPILE (sitting 6b): (a) THE BLESSING AFTER THE MEAL"
DEBT_BOX = """
## DEUTERONOMY SITTING 6b — THE COMPILE OF CHAPTER 8 (2026-09-19; DEUTERONOMY_WALK.md "Sitting 6b" design + AS BUILT; logic/oral_triage/deu_08_ekev_exam_2026-09-19.md
## %d rows, every row read whole from the start; cold_run_good_land.py %d/%d; law_good_land the 68th daemon; the tape 10/10 with RUN (1310, 96, 88, 0, 12, 1605, 39, 319, pairs, 127)).
## THE SITTING-6 BOX (a)-(n) PAID — (a) THE BLESSING AFTER THE MEAL — F3 eat_be_satisfied_bless: the code's hole, bless_after_eating_commanded a STATUS on Israel at
## grace_commanded (8:7-10); the measure of "satisfied" a PARAMETER (R. Meir's olive / R. Yehuda's egg; the Torah edge 20b:14), the four blessings cut three ways
## (48b:5, Tosefta 6:1, 48b:6), the before-blessing refuted and rabbinic, the grace conditional on eating (49b:4), bread its object (44a:10) — the exam's rows;
## (b) THE SEVEN SPECIES — F3 the_seven_species: no write; the order by the verse and the two "land"s (41a:8, 41b:5), the first fruits (Bikkurim 1:3, 1:10; Menachot
## 84a-b), the measures a DATA row (Eruvin 4a, Sukkah 5b; the Rambam's row), honey without milk a DATA row; (c) THE MANNA AND THE HUMBLING — F2, the rows 8:3 TURNED
## and 8:16 EXPANDED against manna_fell (exodus_story and beha by CALL); Yoma 74b's analogy with its two guards; manna_provided UNMOVED (CU5); (d) THE FORTY YEARS
## AS A STATE — F2 the_garment_and_the_foot SUPPLIED, the fifth form, no retrograde write (the owner's decision open; the shelf silent on 8:4); the decree's row
## 8:2 EXPANDED (shelach by CALL); Sanhedrin 99a's forty a DATA note; (e) THE DISCIPLINE — the row 8:5 VARIANT (opening_speech by CALL); Berakhot 5a's afflictions of
## love and the Land through suffering the exam's rows; (f) TAKE HEED LEST — F4 take_heed_lest: the code's hole, forgetting_barred a BLOCK at forgetting_warned (8:11-18),
## 6:12's cell called (the ask without a write); "beware, lest, not" nothing but a prohibition at three seats; no action, no lashes; (g) THE HEART LIFTED — a DATA row
## (Sotah 4b-5a; the eighth of an eighth); 17:20 OWED forward; (h) THE EXODUS FORMULA — the row 8:14 VERBATIM (brought_out by kind; covenant_at_horeb's first word by CALL);
## (i) THE SERPENTS AND THE ROCK — the rows 8:15 EXPANDED and VARIANT (chukat by CALL; the two rocks' two words a DATA row); serpents_sent and water_from_the_rock UNMOVED;
## (j) MY POWER — a DATA row; (k) THE COVENANT ESTABLISHED — the row 8:18 VERBATIM against the oath's three lines (seven_nations, mamre, joseph by CALL); (l) THE
## TESTIMONY — F6: the rows 8:19 VARIANT (witnesses_called by kind; obey_horeb by CALL), 8:19 VARIANT (the second word by CALL — the serve/bow order a DATA row), 8:20
## TURNED (nations_devoted by kind); heaven_and_earth_witness REUSED at perishing_testified — no new effect (CU6); (m) THE KING'S LAW'S TOKENS — a DATA row; the CALL
## OWED forward; (n) THE DOCKET — %d rows by the union rule, EVERY ROW WHOLE FROM THE START (its own run). OWED FROM 6b: (i) THE KING'S LAW — 17:17's "silver and gold he
## shall not multiply" and 17:20's "that his heart be not lifted up" cite 8:13-14 by CALL when chapter 17 compiles; (ii) THE CHECKPOINT PREFIX SPACE ENDS AT CU — the
## two-letter series CA-CZ is spent; the next compile (7b, chapter 9) opens a NEW SERIES at its design, and the probes' 'C[A-Z]' regexes (the recon's finder,
## checkpoint_positions.py, checkpoint_probes.py, cold_run_sequence's VERDICTS list) are MEASURED there before a name is typed; (iii) THE FINDER'S THIRD FORM (4b's
## owed item, unchanged — no receipt in chapter 8; the rule now replicated in a runner, cold_run_good_land.py's receipt_seats); (iv) 12:21 "as I have commanded you"
## — a RECEIPT SEAT for chapter 12's compile (Yoma 75b:4 — Moses commanded the slaughter's laws); (v) 28:48's "in want of all things" — the inversion of 8:9 at
## chapter 28's sitting, citing 8:9 by CALL; (vi) 10:12's "what does the LORD your God ask of you" at chapter 10, citing 8:6 (keep, walk, fear); (vii) 11:13-17
## the rain and the grain conditional on hearing (Berakhot 35b:5 — whose grain) at chapter 11, citing 8:12-14; (viii) 30:18's third "surely perish" and 30:19's
## testimony at chapter 30, citing 8:19 and 4:26 by CALL; (ix) JOSHUA'S RECEIPTS — the entry's bread_and_water_blessed (ordinances' entered_the_land, in the
## registry and absent from the world), the manna ceasing (Joshua 5:12), Joshua's manna at Sinai (Yoma 76a:1) — the run, outside the Torah; (x) THE OWNER'S WORD
## ON THE SUPPLIED GRADE — the fifth form's decision (a state told only in the retelling, no retrograde write) stands as the design's, ON THE TABLE.
## NOTHING ELSE IN CHAPTER 8 IS OWED TO A LATER SITTING OF ITS OWN.
""" % (NROWS, CASES_N, CASES_N, NROWS)

# ---- 3. MIDDOT — the docket entry (every code checked in this file's own lists before it was typed: I1 the a-fortiori, I2 the verbal analogy; the 'do not read' has no code here — described) ----
MIDDOT_ANCHOR = "\n## Exodus block campaign — owner's word \"Do 3\")\n"
MIDDOT_ENTRY = """- THE CHAPTER-8 DOCKET (THE DEUTERONOMY WALK sitting 6b, 2026-09-19; logic/oral_triage/deu_08_ekev_exam_2026-09-19.md — %d rows, every row read
  whole from the start; the rules about rules the docket carries, each at its row):
  · THE VERBAL ANALOGY GUARDED TWICE (I2, gezerah shavah — Yoma 74b:11-13): the Day's "afflict" (Leviticus 16:29) from 8:3's "he afflicted you" — the school of
    R. Yishmael; then the guards: not from Laban's "if you afflict my daughters" (Genesis 31:50) because THE PUBLIC'S AFFLICTION IS DERIVED FROM THE PUBLIC'S; not
    from Egypt's "our affliction" (26:7) because AFFLICTION BY THE HAND OF GOD IS DERIVED FROM GOD'S HAND, not from man's — two governance rules on which seats may
    teach a received analogy (the shelf's own reading of 8:3's hunger as God's act on the whole people — the readback row 8:3 TURNED's ground).
  · THE PREFIX'S IDENTITY IN A VERBAL ANALOGY (I2 — Makkot 13b:12-15): "before the eyes of" (Leviticus 20:17, the excision) from "before your eyes" (25:3, the
    lashes) — yes; "from the eyes of" (Numbers 15:24) from "before your eyes" — no: the analogy runs on the surface form with its prefix; the objection from the
    school of R. Yishmael's "return"/"come" (Leviticus 14:39, 44) left standing — the docket carries both.
  · THE ARTICLE BREAKS THE ANALOGY (I2 — Yoma 76a:1): "man" (Psalm 78:25) from "a MAN in whom is spirit" (Numbers 27:18, Joshua) — yes; from "THE man Moses" (12:3)
    — no: "the man" is not "man".
  · THE VERBAL ANALOGIES THE DOCKET NAMES (I2, each at its row): "land" / "your land" (8:8 / 26:2 — the first fruits the seven species, Menachot 84b:14; the Sifrei
    297:4's runs on "bring"); "afflicted" (8:3 / Psalm 90:15 — the messianic forty, Sanhedrin 99a:5); "gave" / "I will give" (8:10 / Exodus 24:12 — the Torah's
    blessing from the grace, Berakhot 48b:10); "produce" (Leviticus 19:25 / 22:9 — the fourth year's vineyard, Berakhot 35a:5); "covenant" (the salt / the
    afflictions, Berakhot 5a:19); "hewn down" / "hew down" (Isaiah 10:33 / 7:5 — the arrogant as an Asherah, Sotah 5a:10); "opened" / "opened" (Genesis 7:11 /
    Psalm 78:23 — the manna's sixty cubits, Yoma 76a:10).
  · THE A-FORTIORI REFUTED (I1, qal wa-chomer — the refutable one, as this file's I1 note says): from the SATIATED to the HUNGRY (Berakhot 35a:7, 35a:17, 48b:5;
    R. Yochanan's pair 21a:5 — the Torah's blessing after from food's, food's before from the Torah's) refuted at 21a:6 (food gives bodily pleasure, the Torah
    eternal life; and the mishna itself has the impure bless after, not before) and at 35a:18 (meat, eggs and fish have no verse) — THE BLESSING BEFORE FOUNDED
    ON REASON (35a:18-19); the a-fortiori that stands: the slave's tooth and eye to the afflictions' atonement (5a:18), R. Yishmael's from food to the Torah (48b:10).
  · "BEWARE", "LEST", "NOT" — NOTHING BUT A PROHIBITION (a form rule on the code's own words — R. Avin in R. Ile'a's name at Sotah 5a:3, Makkot 13b:5, Eruvin
    96a:8): 8:11's "take heed to yourself lest you forget" a negative command; THE LIMIT (Eruvin 96a:9): "observe" beside a positive has a positive's force (the
    Paschal lamb's "observe this ordinance"); THE LASHES' EDGE (Makkot 13b:6-8): a prohibition without an action is not flogged ("if you will not observe TO
    PERFORM"), nor one rectified by a positive — lashes only for what is like the muzzling (25:4, juxtaposed to the lashes' passage).
  · "A LAND" CONCLUDED THE MATTER (Berakhot 44a:10 — a scope rule by a repeated word): the second "a land" (8:9) closes the seven species' clause, so "eat, be
    satisfied, bless" (8:10) falls on BREAD alone (the Rabbis); for Rabban Gamliel the word excludes the raw wheat chewer.
  · RAV HAMNUNA'S TWO "LAND"S (Berakhot 41b:5 — counting from each occurrence): the order of blessings by the verse (41a:8 — "each food that precedes in the verse
    precedes in the blessing") refined by the verse's own structure: the date second to the second "land", the pomegranate fifth to the first.
  · ABAYE'S "HERE ON THE VERSE, THERE ON REASONING" (Berakhot 49b:9-10; Pesachim 49b:17): R. Meir's olive-bulk and R. Yehuda's egg-bulk read the two verbs
    ("eat" eating, "be satisfied" drinking / eating that satisfies) — not reversed though the same sages reverse elsewhere on reasoning.
  · "ONE DOES NOT PERFORM COMMANDMENTS IN BUNDLES" (Berakhot 49a:12 — why a blessing concludes with one theme); "THE HALAKHA IS AS THE DECISOR" (43b:9 — Rabban
    Gamliel between the houses); "ONE SHOULD NEVER EXCLUDE HIMSELF FROM THE COLLECTIVE" (49b:16 — the invitation's "let us bless").
  · THE "DO NOT READ" READINGS (no code in this file's lists — described): "whose stones" read "whose builders" (Taanit 4a:3 on 8:9); "he will bless" read "you
    shall bless" (Berakhot 48b:7 on Exodus 23:25); "how little" read "an altar" (Sotah 4b:13); "him" read "with him" (Sotah 5a:14); "teach him" read "teach us"
    (Berakhot 5a:17); "spread" read "slaughtered" (Yoma 75b:3); "mighty" read "limbs" (Yoma 75b:16) — each a homily on the letters, none a rule the machine runs.
  · THE COUNT FROM THE SPELLING (Yoma 75b:10): the 248 limbs from "fine flaky" WITHOUT the vav (254 with it) — the defective spelling counted, the chapter-6
    lesson's kin; THE WRITTEN/READ PAIR ON THE SHELF (Yoma 75b:6): the quail written with shin, read with samekh (Numbers 11:31) — the righteous in peace, the
    wicked as thorns.
  · A COMMAND CONDITIONAL ON AN ACT (Berakhot 49b:4): the grace "not an obligation — if he wants he eats, if not, not" — the shelf's reading of 8:10's own order
    (eat, be satisfied, bless), against the prayer's standing obligation: a status whose trigger is the eating, the write's form.
""" % NROWS

# ---- 4. MISHNAH_TOPICS — the rows touched ----
DKF = "deu_08_ekev_exam_2026-09-19.md"
TOPIC_NOTES = {
 "**1. Mishnah, Blessings**": " — 6-7 READ WHOLE (thirteen rows, the answer sheet) with Berakhot 5a, 20b-21a, 35a-35b, 41a-44a, 48b-49b READ WHOLE 2026-09-19 (%s: the grace after meals by Torah law and its four blessings, 8:10; the measure of 'satisfied'; the blessing before refuted; the order of blessings by the verse and its two 'land's, 8:8; the afflictions of love and the Land through suffering, 8:5, 8:7; the grace conditional on eating; 'filling his stomach', 8:14 — %s)" % (W6, DKF),
 "**11. Mishnah, First Fruits**": " — 1 READ WHOLE (eleven rows) with Menachot 84a-b and Tosefta Bikkurim 2:8 READ 2026-09-19 (%s: the first fruits from the seven species, 8:8; beyond the Jordan; the seven vessels)" % W6,
 "**16. Mishnah, Day of Atonement**": " — Yoma 74b-76a READ WHOLE (sixty-nine rows; the Numbers 11 exam's manna rows credited, given their quick look) and 79b:9, 81b:6 READ 2026-09-19 (%s: 'afflicted you' the Day's affliction by the analogy with 8:3 and its two guards; the manna's forms and tastes, the daily manna's reason, the sixty cubits; the invitation's measure, 8:10; the pepper, 8:9)" % W6,
 "**28. Mishnah, Suspected Wife**": " — Sotah 4b-5a READ WHOLE (thirty-nine rows) and 33a:10 READ 2026-09-19 (%s: arrogance as denial from 8:14 and as idolatry by 7:26; 'beware, lest, not' a prohibition, 8:11; the eighth of an eighth; the grace in any language, 8:10)" % W6,
 "**35. Mishnah, Lashes**": " — Makkot 13b READ WHOLE (twenty-one rows) 2026-09-19 (%s: 'observe, lest, do not' nothing but a prohibition — the lashes' scope; a prohibition without an action not flogged, 8:11)" % W6,
 "**13. Mishnah, Merging Domains**": " — Eruvin 96a READ WHOLE (fourteen rows; the chapter-4 docket's credit, given its quick look) and 4a:11 READ 2026-09-19 (%s: 'observe' beside a positive; the measures from the verse, 8:8)" % W6,
 "**17. Mishnah, Booth**": " — 2:5 READ with Sukkah 26b:9, 5b:14 and 35a:2 READ 2026-09-19 (%s: R. Tzadok's less than an egg-bulk, 8:10; the measures from the verse and the pepper tree, 8:8-9)" % W6,
 "**43. Mishnah, Slaughter**": " — Chullin 107a:12 READ 2026-09-19 (%s: the egg-bulk and the hand-washing, 8:10)" % W6,
 "**45. Mishnah, Valuations**": " — Arakhin 4a:4 READ 2026-09-19 (%s: the priests at the atonement meal form the invitation — 'eat and be satisfied', 8:10)" % W6,
 "**32. Mishnah, Middle Gate**": " — Bava Metzia 114a:9 READ 2026-09-19 (%s: consecrated property needs the blessing, 8:10)" % W6,
 "**14. Mishnah, Passover**": " — Pesachim 49b:17 READ 2026-09-19 (%s: the invitation's measure from the two verbs — Abaye, 8:10)" % W6,
 "**34. Mishnah, Courts**": " — Sanhedrin 99a:5 READ 2026-09-19 (%s: the messianic era forty years from 8:3's 'afflicted')" % W6,
 "**20. Mishnah, Fasts**": " — Taanit 4a:3 READ 2026-09-19 (%s: 'whose stones are iron' read 'whose builders', 8:9)" % W6,
 "**25. Mishnah, Marriage Contracts**": " — Ketubot 47b:11 READ 2026-09-19 (%s: 'onata' sustenance from 8:3)" % W6,
 "**42. Mishnah, Grain Offerings**": " — Menachot 84a:14, 84b:14 READ 2026-09-19 (%s: the first fruits' species by the verbal analogy 'land' / 'your land', 8:8)" % W6,
}

# ---- 5. RESEARCH_LOG ----
RLOG = """

## 2026-09-19 — DEUTERONOMY 8 COMPILED (THE DEUTERONOMY WALK sitting 6b — CHAPTER 8): THE READBACK'S FIFTH FORM — THE RETELLING OF A STATE; THE CODE'S TWO HOLES
## COMPILED AT THE CHAPTER'S OWN DAY AND THE TESTIMONY'S EFFECT REUSED; A REUSED EFFECT MOVES AN OLDER COUNT; THE SHELF READS THE GRACE AS CONDITIONAL ON THE ACT;
## THE FIRST BLESSING INSTITUTED BEFORE ITS VERSE

THE READBACK OF A STATE. Chapter 8 retells the wilderness as the reason for a law — remember the way, lest you forget — so its rows are reference rows
against the tape's lines (the decree, the manna, the going out, the serpents, the rock, the oath, the testimony, the ban) and the kin's cells (4:1's
exhortation, 1:31's carrying, 2:7's lacking nothing, 6:3's land and 6:10-12's gift and warning, 5:6's formula and 5:9's second word): eighteen rows,
VERBATIM 6 / VARIANT 5 / EXPANDED 4 / TURNED 2 as the design predicted. And ONE row retells a state the tape never wrote and cannot write as an act: your
garment did not wear out, your foot did not swell, these forty years (8:4). The tape records acts at days; a forty-year condition has no day. The row was
graded SUPPLIED — a new grade — with NO retrograde write, its ledger scan asserted empty at build (the one database) and at the tape (CU7 on the running
world), its kin named (29:4, Nehemiah 9:21), and the docket found NO ROW on the shelf citing 8:4: the shelf does not challenge the decision, which stays
the owner's. THE CODE'S HOLES: no runner held the Torah's one command to bless Him (8:10) — bless_after_eating_commanded a STATUS on Israel; 6:12's cell held
"take heed to yourself lest you forget" as an ask WITHOUT A WRITE — forgetting_barred a BLOCK on Israel, its first tape write; 4:26's testimony is on the tape
with its effect, so 8:19 REUSES heaven_and_earth_witness at its second seat, no new effect — and the reuse moved an older checkpoint's count literal (chapter
4's CC7: ONE -> TWO), retyped from the print. THE SHELF'S FINDS THE DESIGN DID NOT PREDICT (the docket's own run): the grace "not an obligation — if he wants
he eats" (Berakhot 49b:4), a status whose trigger is the eating; MOSES INSTITUTED THE FIRST BLESSING WHEN THE MANNA FELL (48b:2) — the blessing before its
verse, an install-order note beside THE INSTALL HYPOTHESIS; the verse cut into the four blessings THREE ways and the fourth blessing's standing disputed;
"a land" (8:9) concluded the matter — bread the grace's object; the analogy's two guards (Yoma 74b:12-13 — the public's from the public's, God's hand from
God's hand) read 8:3's hunger as God's act on the whole people, which is the readback row's own TURNED grade; 12:21 a receipt seat for chapter 12; 28:48
inverts 8:9. THE NUMBERS: cold_run_good_land.py the 63rd runner %d/%d on its first graded run; the tape 10/10 on its second (the first 9/10, CC7); RUN
(1310, 96, 88, 0, 12, 1605, 39, 319, the four pairs, 127) as predicted; kinds 1133, effects 1031, daemons 68, thirteen CALL edges (the design's decalogue
edge dropped — no cell there); the docket %s; every gate green in one chain (the sweep %d/63). THE TWO-RUN RULE'S FIRST COMPILE SITTING: RUN A the design,
the docket its own run, RUN B the build — three clean points, the owner compacting twice.
""" % (CASES_N, CASES_N, docket_line, SW_P)

# ---- 6. THE_STEPS ----
STEPS_ANCHOR = "\n## Step 6 — Publish\n"
STEPS_PARA = """
DEUTERONOMY — SITTING 6b — CHAPTER 8 COMPILED (2026-09-18/19, on Brian's "Next" for the design, "Go" for the docket and "Go run b" for the build;
World/step9/DEUTERONOMY_WALK.md "Sitting 6b" and "Sitting 6b — AS BUILT"). Chapter 8 tells the wilderness again as a reason — remember the way, lest you
forget — so this sitting graded each retelling against the tape's own line or the older cell that holds it, eighteen rows, and found one thing the tape
could not hold: the garment that did not wear out and the foot that did not swell over forty years is a condition, not an act, and a condition has no
day. That row got a new grade, SUPPLIED, and no line was written back into the past; the machine asserts that no ledger anywhere names the state, and
the answer sheet turned out to cite that verse nowhere. Two commands had no code: eat, be satisfied and bless — the Torah's one command to bless Him — and
take heed lest you forget, which chapter 6's cell asked about and never wrote; both were compiled here and written at the day the chapter is spoken. The
testimony of 8:19 reuses chapter 4's, and that reuse moved one old count in the checks, retyped from the print. The docket read the tractate on blessings
at its verse-anchored pages whole — four hundred and fifty-one rows, every one entire — and taught what the design had not guessed: the grace is not an
obligation but follows the eating, and Moses instituted the first blessing when the manna fell, before the verse that commands it. The runner matched its
sheet on the first run; the tape reached ten of ten on the second; every gate green in one chain. This was the two-run rule's first compile: the design,
then the docket as its own run, then the build. Next: the commit on your word; then chapter 9's reading.
"""

# ---- 7. THE_BRIEFING ----
BRIEF_BULLET_ANCHOR = "- **CHAPTER 8 READ AND FROZEN — THE MANNA AND THE GOOD LAND:"
BRIEF_BULLET = ("- **CHAPTER 8 COMPILED — THE RETELLING OF A STATE: A CONDITION HAS NO DAY, SO THE MACHINE GRADES IT AND WRITES NOTHING BACK; THE TORAH'S ONE COMMAND TO BLESS AND THE FORGETTING BARRED COMPILED AT THE CHAPTER'S OWN DAY; THE SHELF SAYS THE GRACE FOLLOWS THE EATING AND THE FIRST BLESSING CAME BEFORE ITS VERSE** "
                "(2026-09-19, on your \"Next\", \"Go\" and \"Go run b\"; World/step9/DEUTERONOMY_WALK.md \"Sitting 6b\" + AS BUILT): cold_run_good_land.py the 63rd runner (%d/%d), law_good_land the 68th daemon (%d functions); the readback's fifth form eighteen rows, one SUPPLIED; the tape 10/10 with RUN (1310, 96, 88, 0, 12, 1605, 39, 319, pairs, 127) as predicted; the docket %d rows every row whole; every gate green, the sweep %d/63; the two-run rule's first compile sitting, three clean points.\n" % (CASES_N, CASES_N, DG[1], NROWS, SW_P))
BRIEF_ENTRY_ANCHOR = "### 2026-09-18 — CHAPTER 8 READ: THE MANNA, THE GOOD LAND, AND THE FIRST ONE-RUN READING\n"
BRIEF_ENTRY = """### 2026-09-19 — CHAPTER 8 COMPILED: A STATE THE TAPE CANNOT HOLD, AND THE GRACE THAT FOLLOWS THE EATING

Chapter 8 is Moses telling the wilderness again as a reason: remember the way, the manna, the rock, the serpents — lest you forget when the houses and the
herds and the silver multiply. The machine's readback has graded retellings before: against the tape's own lines, against the older cell that compiled
the law first. This chapter added a case those forms could not hold. Your garment did not wear out, your foot did not swell, these forty years. That is
not an act at a day; it is a condition over forty years, and the tape records acts at days. So the row got a new grade — SUPPLIED — and nothing was written
back into the past: the machine asserts instead that no ledger anywhere names a garment or a shoe or a swelling on Israel, and the Talmud, read whole for
the answer sheet, cites that verse nowhere. The decision that no line be written is yours to keep or reverse; the shelf does not press either way. Two
commands in the chapter had no code at all. Eat and be satisfied and bless — the Torah's one command to bless God — had no cell in sixty-two runners; it
is compiled here, and the Talmud's tractate on blessings is its answer sheet: the grace is from the Torah, its four blessings are cut from this one verse
three different ways, the measure of "satisfied" is a parameter the sages disputed from the verse's two verbs, and — the thing the design did not guess —
the grace is not an obligation like the prayer but follows the eating, "if he wants he eats, if not, not". The shelf also says Moses instituted the first
blessing when the manna fell, forty years before the verse commands it: the blessing before its verse, filed beside the install hypothesis. The second
hole is "take heed lest you forget": chapter 6's cell had asked the question and never written the block; it is written now. The testimony at the end
reuses chapter 4's, and that reuse moved one old count in the checks, retyped from the print — the machine keeps counts as literals so that a change
shows. The runner matched its sheet on the first run; the tape reached ten of ten on the second; every gate is green in one chain. This was the first
compile under your two-run rule, with the docket as its own run between: three clean points. Next, on your word: the commit, then chapter 9.

"""

# ---- 8. THE_LOOP step-6 row ----
LOOP_OLD = "readback_probes 18/18, CQ4) | the three forms BUILT — acts (1b), laws (3b, and on the kin 5b), a retelling inside a law (4b); the second pass after Deuteronomy |"
LOOP_NEW = ("readback_probes 18/18, CQ4); cold_run_good_land.py (chapter 8, THE FIFTH FORM — THE RETELLING OF A STATE 2026-09-19: the wilderness retold as a law's reason graded against the tape's lines and the kin's cells — eighteen rows VERBATIM 6 / VARIANT 5 / EXPANDED 4 / TURNED 2 / SUPPLIED 1; the garment and the foot (8:4) a condition with no day, SUPPLIED with NO retrograde write, its ledger scan asserted empty at build and at CU7; two holes compiled, the testimony reused; "
            "readback_probes 21/21, CU4) | the four forms BUILT — acts (1b), laws (3b, and on the kin 5b), a retelling inside a law (4b), a STATE (6b); the second pass after Deuteronomy |")

# ---- 9. RESUME ----
RESUME_HEAD = """# ⚠ THE DEUTERONOMY WALK sitting 6b (2026-09-18/19; step9/DEUTERONOMY_WALK.md "Sitting 6b" + "Sitting 6b — AS BUILT"): CHAPTER 8 COMPILED —
# step9/cold_run_good_land.py the 63rd runner (%d/%d; six cells; THE READBACK'S FIFTH FORM — the retelling of a STATE: eighteen rows, ten on the tape, seven
# by CALL, ONE SUPPLIED (8:4 the garment and the foot — no retrograde write, the scan empty); two holes compiled), law_good_land the 68th daemon (given_at
# Deut 8:1, boot); THREE LINES on the counter's own day (40, 11, 1), NO marker — bless_after_eating_commanded a STATUS, forgetting_barred a BLOCK (6:12's ask
# without a write), heaven_and_earth_witness REUSED at 8:19; the tape 10/10 on its second run with RUN (1310, 96, 88, 0, 12, 1605, 39, 319, pairs, 127) as
# predicted, PREVIOUS_RUN 5b's exactly, markers 167, closes 127 (chapter 4's CC7 retyped — the reuse a second entry); the docket %d rows read whole from
# the start (its own run); every probe suite and gate GREEN, the sweep %d/63. THE TWO-RUN RULE's first compile sitting: three clean points.
# NEXT on the ruling: the commit on the owner's word; chapter 9's reading (9:1-29) — the next compile opens a NEW checkpoint series (CU the last two-letter prefix).
""" % (CASES_N, CASES_N, NROWS, SW_P)

# ---- 10. THE STATE DOC — #196 ADDENDUM 4 ----
STATE_ADD = """
#196 ADDENDUM 4 (2026-09-19, at the close of THE DEUTERONOMY WALK sitting 6b — THE COMPILE OF CHAPTER 8, RUN B of two under THE TWO-RUN RULE, on the owner's "Go run b" — A CLEAN COMPACTION POINT): THE SITTING RAN AS THE RULE SAYS — RUN A the rereads, the measurements and the design (#196 addendum 2, 2026-09-18), THE DOCKET its own run by the docket clause (#196 addendum 3), RUN B this: readback_probes.py Q19-Q21 written to FAIL before the runner (18/21), add_types_ch8.py (kinds 1133, effects 1031 — bless_after_eating_commanded a status, forgetting_barred a block, the testimony's heaven_and_earth_witness reused; the daemon law_good_land the 68th; the functions block; the span and THIRTEEN CALL edges — the design's decalogue edge DROPPED at the callees' print, no cell on the second word in that runner; I5 68), ch8_callees.py (every CALL's facts printed before an assert), the runner in three parts with the fast checker (two forms fell on the first pass and were retyped from the print: the register gate's finder RULE replicated in the runner found chapter 1's three seats — 1:19 the CHAPTER seat; the state's word list word-bounded after "wore" matched "swore"), the CASES generated (%d, per cell %s) and frozen under the guard (the guard's count from the generator's print — a grep counted 54 on a label with an apostrophe), cold_run_good_land.py %d/%d ON ITS FIRST GRADED RUN (the scene thirteen persons, four exempt, no lashes; the narrative 3 writes, one entity, the counter's day), the recorder and the stitcher (the tape's three lines under "# ---- Deut 8 ----", PLACEMENT page_order 1146 and CENSUS 1310 / 855 AS PREDICTED; the derivation's root line by regex after a count failed), patch_seq_literals_ch8.py (RUN, PREVIOUS_RUN 5b's exactly, NEWEST_RUNNER, PLACEMENT and CENSUS read from the stitcher's print, CU1-CU9), THE TAPE 9/10 ON ITS FIRST RUN — CU1-CU9 all MATCH, THE REST OK, the one miss the VERDICTS list: chapter 4's CC7 holds heaven_and_earth_witness ONE as a literal and the reuse at 8:19 is a second entry on the same ledger — RETYPED FROM THE PRINT (patch_cc7_ch8.py: 1 -> 2, the note dated; 5b's lesson on a status count) — 10/10 ON THE SECOND RUN (%s s) with RUN (1310, 96, 88, 0, 12, 1605, 39, 319, the four pairs, 127) as the design's arithmetic wrote it; checkpoint_check.py --all after the tape (253 rows, the eighteen known diverges); THE GATES CHAIN TWICE — the first stopped at the dependency gate by ONE demand (a POINTER at Deut 8:5 in the AS_WHEN form, "as a man disciplines his son" — dispositioned RUN_CITATION of 1:31's carrying by the readback row, add_pointers_ch8.py; no edge demanded; the design's eight predicted pointers asked for as one), the second from that step ALL GREEN — the twelve probe suites (%s), %s. THE READBACK'S FIFTH FORM AS BUILT: eighteen rows VERBATIM 6 / VARIANT 5 / EXPANDED 4 / TURNED 2 / SUPPLIED 1 as predicted; the one SUPPLIED row 8:4's with its ledger scan EMPTY at build (the one database) and at CU7 (the running world); the decision (no retrograde write) the owner's, the shelf silent on 8:4. THE RECORDS (write_ch8b_records.py from the sheet, one call): the map's "Sitting 6b — AS BUILT" (thirteen departures and the chain's demand, eleven lessons), COMPILE_DEBT's sitting-6 box PAID + the 6b box (ten owed items — the king's law's tokens, THE CHECKPOINT PREFIX SPACE ENDING AT CU, the finder's third form, 12:21's receipt seat, 28:48, 10:12, 11:13-17, 30:18, Joshua's receipts, the owner's word on SUPPLIED), MIDDOT's docket entry (every code checked in MIDDOT.md against the rows' own words: I2 the analogies with their guards, I1 the a-fortiori refuted; the "do not read" readings described without a code), MISHNAH_TOPICS (fifteen heads), RESEARCH_LOG, THE_STEPS, THE_BRIEFING (the scoreboard bullet and an entry), THE_LOOP's step-6 row (the four forms), RESUME, RECORD_FORMS (the writer's pointer), this addendum, the addenda §44, the recovery page (section 2 rewritten under its cap), the memory (the walk note and the index line under 17,000). THE FORMS copied (copy_ch8b_forms.py — RUN B's scripts and prints, the chain's folder). THE TREE: + cold_run_good_land.py, the registries (event_vocabulary, effect_vocabulary, daemon_dispositions, dependency_dispositions), cold_run_sequence.py (the tape's three lines, the literals, CU1-CU9, CC7), readback_probes.py, installation_probes.py, checkpoint_positions.yaml (the positions table), the records, the forms. NOT COMMITTED (since 29c189b): sitting 6 whole, the two-run rule's records, 6b whole (RUN A, the docket, RUN B) — the message at <scratch>/commit_msg_ch8.txt REWRITTEN to cover all three for the owner's word ("commit" = no push; "commit push" = both). NOTHING MID-FLIGHT — A CLEAN COMPACTION POINT. NEXT ON THE RULING: the commit on his word; then CHAPTER 9's reading (9:1-29) — one run; the next compile (7b) OPENS A NEW CHECKPOINT SERIES (CU the last two-letter prefix; the probes' 'C[A-Z]' regexes measured at its design) — or the Decalogue-schema sitting first, on his word; THE INSTALL HYPOTHESIS and THE SUPPLIED GRADE on the table. POST-COMPACTION REREADS: the recovery page, the map's "Sitting 6b — AS BUILT" (the newest section — the departures and the lessons), MEMORY.md.
""" % (CASES_N, PER_CELL, CASES_N, CASES_N, tape_elapsed, pr_line, gates_line)

# ---- 11. THE RECOVERY ADDENDA — section 44 ----
ADDENDA_ADD = """

## 44. ADDENDUM (2026-09-19, THE DEUTERONOMY WALK sitting 6b — THE COMPILE OF CHAPTER 8, Deuteronomy 8:1-20 COMPILED AND ON THE TAPE in two runs with the docket its own run; the owner: "Next", "Go", "Go run b"; the state doc's #196 addenda 2-4)

THE SHAPE: THE TWO-RUN RULE's first compile sitting — RUN A the rereads, the measurements (ch8_compile_recon.py, ch8_docket_scan.py, the one database) and the design in
the map (2026-09-18); THE DOCKET its own run by the rule's clause (451 rows in three parts, every row whole; deu_08_ekev_exam_2026-09-19.md; 2026-09-19); RUN B the
build (the probes to fail, the types, the callees' print, the runner in parts with the fast checker, the cases generated, the recorder and the stitcher, the
literals, the tape twice, the checkpoint check, the chain once, the records in one call, the forms) — three clean points, the owner compacting after each.
THE FIFTH FORM: a state told only in the retelling (8:4) is graded SUPPLIED with no retrograde write — its ledger scan asserted at build and at the tape; the
decision the owner's, the shelf silent. THE HOLES: the grace after the meal (a status) and the forgetting barred (a block — 6:12's ask without a write) compiled
at the chapter's own day; the testimony's effect reused, and the reuse moved chapter 4's CC7 (retyped from the print). THE DESIGN'S ERRORS caught by prints: the
decalogue edge (no cell), the line's first verse (4:25, 8:7), the finder's third seat (1:19), the word list ("wore" in "swore"), the generator's count, the
pointers (eight predicted, one demanded — 8:5's 'as', a run citation of 1:31; the chain run twice). THE
SHELF'S UNPREDICTED: the grace conditional on eating (49b:4), the first blessing at the manna (48b:2), the fourth blessing's standing (49a:5), "a land concluded
the matter" (44a:10), the analogy's two guards (Yoma 74b:12-13), 12:21 a receipt seat, 28:48's inversion. THE NUMBERS: cold_run_good_land.py %d/%d; the tape 10/10
on its second run, RUN (1310, 96, 88, 0, 12, 1605, 39, 319, pairs, 127) as predicted; kinds 1133, effects 1031, daemons 68, thirteen CALL edges; the docket %d rows;
the sweep %d/63; every gate green. OWED FORWARD: the king's law's tokens (17:17, 17:20), THE CHECKPOINT PREFIX SPACE (CU the last two-letter prefix — the next compile
opens a new series, the probes' regexes measured first), the finder's third form, 12:21's receipt seat, 28:48, 10:12, 11:13-17, 30:18, Joshua's receipts, the owner's
word on SUPPLIED. The records on the sheet, the forms in World/step9/forms_deuteronomy_walk/ (copy_ch8b_forms.py).
""" % (CASES_N, CASES_N, NROWS, SW_P)

# ---- 12. THE RECOVERY PAGE — section 2 rewritten; sections 4, 5, 6 retouched; the cap asserted ----
def f_recovery(s):
    i = s.index('## 2. WHERE IT STANDS'); j = s.index('## 3. THE STANDING LAWS')
    sec2 = """## 2. WHERE IT STANDS (2026-09-19, after 6b; the state doc #196 addendum 4 the newest)
- NUMBERS CLOSED. DEUTERONOMY 1:1-8:20 COMPILED AND ON THE TAPE (1-7 at 29c189b PUSHED; 8 at sittings 6 and 6b).
- 222 frozen units, standing 2215, hash 8b8fff1fa28953af. 63 runners, 68 daemons, %d functions; 1133 kinds / 1031 effects.
- THE TAPE at RUN (1310, 96, 88, 0, 12, 1605, 39, 319, pairs, 127), markers 167, closes 127; the sweep %d/63; every gate GREEN; the
  register gate DECLARED %d / DEBT 0. The readback's FIFTH form (6b): a STATE graded SUPPLIED, no write — his decision open.
- Uncommitted since 29c189b: sitting 6, the two-run rule, 6b; the message at <scratch>/commit_msg_ch8.txt.
- NEXT ON HIS WORD: the commit; then CHAPTER 9 (9:1-29); 7b opens a NEW checkpoint series (CU the last prefix).

""" % (DG[1], SW_P, RG[0])
    s = s[:i] + sec2 + s[j:]
    old4 = "(62 runners;\ncold_run_seven_nations.py the newest form)"; assert s.count(old4) == 1, s.count(old4)
    s = s.replace(old4, "(63 runners;\ncold_run_good_land.py the newest form)")
    old5 = 'the newest instances: the map\'s "Sitting 6b" and "Sitting 6")'; assert s.count(old5) == 1
    s = s.replace(old5, 'the newest instances: the map\'s "Sitting 6" and "Sitting 6b")')
    old6 = "- Deuteronomy's sittings: the map; the addenda §31-43 (§39 the whole-row rule). The cost cuts: §35."; assert s.count(old6) == 1
    s = s.replace(old6, "- Deuteronomy's sittings: the map; the addenda §31-44 (§39 the whole-row rule). The cost cuts: §35.")
    assert len(s.encode('utf-8')) <= 10240, ('THE RECOVERY PAGE OVER ITS CAP', len(s.encode('utf-8')))
    return s

# ---- 13. MEMORY ----
MEM_DESC_OLD = 'description: "COMMITTED THROUGH 29c189b (2026-09-18; PUSHED) — 6b DOCKET DONE 2026-09-19 (451 rows whole, deu_08_ekev_exam_2026-09-19.md; UNCOMMITTED) — '
MEM_DESC_NEW = 'description: "COMMITTED THROUGH 29c189b (2026-09-18; PUSHED) — SITTING 6b DONE 2026-09-19 (chapter 8 COMPILED — the readback\'s FIFTH form, a STATE graded SUPPLIED with no retrograde write; the grace and the forgetting compiled at the chapter\'s own day; the docket 451 rows whole; UNCOMMITTED) — '
MEM_PARA = """

SITTING 6b RUN B DONE 2026-09-19 (the owner: "Go run b"; the map's "Sitting 6b" + AS BUILT): CHAPTER 8 COMPILED — cold_run_good_land.py the 63rd runner
(%d/%d on its first graded run), law_good_land the 68th daemon (given_at Deut 8:1, boot). THE READBACK'S FIFTH FORM — THE RETELLING OF A STATE: eighteen rows
VERBATIM 6 / VARIANT 5 / EXPANDED 4 / TURNED 2 / SUPPLIED 1 as predicted; 8:4 (the garment and the foot) a condition with no day — SUPPLIED, NO retrograde
write, its ledger scan asserted empty at build and at CU7; the shelf cites 8:4 nowhere; THE DECISION THE OWNER'S, on the table. THE HOLES: the grace after the
meal (bless_after_eating_commanded a STATUS — the Torah's one command to bless Him; the grace by Torah law, its four blessings cut three ways, the measure a
PARAMETER, conditional on eating per 49b:4) and the forgetting (forgetting_barred a BLOCK — 6:12's ask without a write; 'beware, lest, not' a prohibition; no
action, no lashes); the testimony REUSED (heaven_and_earth_witness at 8:19) — and the reuse moved chapter 4's CC7 count (retyped from the print). Three lines on
the counter's day (40, 11, 1), no marker; the tape 10/10 on its second run with RUN (1310, 96, 88, 0, 12, 1605, 39, 319, pairs, 127) as predicted; kinds 1133,
effects 1031, daemons 68, THIRTEEN CALL edges (the decalogue edge dropped — no cell there); every gate green, the sweep %d/63 (the chain twice — one pointer demanded at 8:5, a run citation of 1:31). ⚠ LESSONS (eleven, in the map): a
reused effect is a second entry on the same ledger — an older count literal moves; the design's tape verse is the LINE's first verse; the callees' print finds the
design's holes; a scan's word list is word-bounded; a gate's rule replicated when the import is circular; the generator's count, never a grep; the fifth form
holds; the docket's crowns become exam rows; a form with a repeated line is derived by regex; the census asks for one pointer of eight predicted; THE TWO-RUN RULE HELD on its first compile sitting (three clean
points). ⚠ OWED: THE CHECKPOINT PREFIX SPACE ENDS AT CU — the next compile (7b) opens a NEW SERIES, the probes' 'C[A-Z]' regexes measured at its design. NOT
COMMITTED (since 29c189b; the message at <scratch>/commit_msg_ch8.txt covers sitting 6, the two-run rule and 6b). NEXT on the ruling: the commit; chapter 9's
reading (9:1-29), one run — or the schema sitting.
""" % (CASES_N, CASES_N, SW_P)
MEM_IDX_OLD = 'map World/step9/DEUTERONOMY_WALK.md; ch 1-7 COMPILED (29c189b PUSHED); SITTING 6 DONE (ch 8 FROZEN, 222 units); 6b RUN A + DOCKET DONE 2026-09-19; NEXT: RUN B'
MEM_IDX_NEW = 'map World/step9/DEUTERONOMY_WALK.md; ch 1-8 COMPILED (1-7 at 29c189b PUSHED; 8 UNCOMMITTED, sittings 6/6b); NEXT: commit on his word, then ch 9 (7b a new series)'

# ---- 14. RECORD_FORMS — the writer's form pointer ----
FORMS_OLD = "World/step9/forms_deuteronomy_walk/write_ch7b_records.py (write_ch6b_records.py, write_ch5b_records.py and write_ch4b_records.py the earlier forms). Keep this sheet current"
FORMS_NEW = "World/step9/forms_deuteronomy_walk/write_ch8b_records.py (write_ch7b_records.py, write_ch6b_records.py, write_ch5b_records.py and write_ch4b_records.py the earlier forms; a docket run's close by write_ch8_docket_records.py). Keep this sheet current"

# ---- THE WRITES (every text built above; the files opened only now) ----
def read(p): return open(p if p.startswith('/') else f'{ROOT}/{p}', encoding='utf-8').read()
def write(p, s): open(p if p.startswith('/') else f'{ROOT}/{p}', 'w', encoding='utf-8').write(s)
plans = []
def f_map(s):
    assert 'THE DOCKET — AS RUN (2026-09-19' in s and '## Sitting 6b — THE COMPILE OF CHAPTER 8 — AS BUILT' not in s
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
    s = s.replace('## SCOREBOARD (as of 2026-09-18, latest)\n', '## SCOREBOARD (as of 2026-09-19, latest)\n')
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
