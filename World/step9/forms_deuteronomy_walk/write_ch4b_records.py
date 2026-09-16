import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE DEUTERONOMY WALK sitting 2b — THE COMPILE OF CHAPTER 4 (2026-09-16): THE RECORDS, written after every gate ran — the numbers COMPUTED from the
# gates' own prints in the scratchpad (never recited); every text built whole before any file is opened; the ledgers appended, the map appended,
# the checklist's box marked paid on 1b's precedent. `--check` parses and prints without writing. Sitting 1b's form (write_deu_records.py).
import os, re, sys, subprocess
ROOT = _ROOT
SP = os.path.dirname(os.path.abspath(__file__))
CHECK = '--check' in sys.argv
def rd(name): return open(f'{SP}/{name}', encoding='utf-8', errors='ignore').read()
def last_frac(name, m):
    t = rd(name); hits = re.findall(r'(\d+)/%d\b' % m, t); assert hits, (name, 'no n/%d' % m); return int(hits[-1])
# ---- THE NUMBERS FROM THE PRINTS ----
tape = rd('tape_run_ch4_6.out'); assert '10/10 checkpoints' in tape and 'OK   THE REST' in tape
CC = re.findall(r'CHECKPOINT (CC\d) .*? (MATCH|MISS|DIVERGE)$', tape, flags=re.M); assert len(CC) == 9 and all(v == 'MATCH' for _, v in CC), CC
tape_elapsed = re.search(r'elapsed ([\d.]+)s', tape).group(1)
PL = re.search(r"PLACEMENT \(O9 T2\): markers (\{[^}]*\}); events (\{[^}]*\})", tape); assert PL
rg = rd('register_gate_ch4.out'); m = re.search(r'DECLARED (\d+); DEBT (\d+); FAILS (\d+)', rg); assert m and 'THE REGISTER GATE: GREEN' in rg
RG = tuple(int(x) for x in m.groups()); assert re.search(r'Deut 4:5 +ACT +declared', rg) and re.search(r'Deut 4:45 +DAEMONS +green .*daemons 2', rg)
dg = rd('daemon_gate_ch4_2.out'); m = re.search(r'\((\d+) daemons, (\d+) functions\)', dg); assert m and 'gate satisfied' in dg; DG = tuple(int(x) for x in m.groups())
dp = rd('dependency_gate_ch4_4.out'); m = re.search(r'dispositions on file: (\d+) edges, (\d+) pointers', dp); assert m and 'gate satisfied' in dp; DP = tuple(int(x) for x in m.groups())
LC = re.search(r'LINK CENSUS \(the link review law\): reference (\d+), transfer (\d+), hypothesis (\d+), none (\d+)', dp); assert LC; LC = tuple(int(x) for x in LC.groups())
m = re.search(r'required edges (\d+), required pointers (\d+); live import edges (\d+)', dp); DPR = tuple(int(x) for x in m.groups())
jg = rd('journal_gate_ch4_final.out'); assert 'GATE GREEN' in jg; m = re.search(r'(\d+) kinds, (\d+) rows in the index', jg); JG = tuple(int(x) for x in m.groups())
sw = rd('sweep_ch4.out'); SW_P = len(re.findall(r'^PASS +cold_run_\w+\.py', sw, flags=re.M)); SW_F = len(re.findall(r'^FAIL +cold_run_\w+\.py', sw, flags=re.M))
SW_CELLS = sum(int(a) for a, b in re.findall(r'score=(\d+)/(\d+)', sw)); assert SW_P + SW_F == 59, (SW_P, SW_F); assert SW_F == 0, 'the sweep has failures — read them first'
po = rd('positions_ch4.out'); m = re.search(r'(\d+) checkpoints over (\d+) pauses', po); assert m, po[-800:]; PO = tuple(int(x) for x in m.groups())
PR = {'census': last_frac('census_probes_ch4.out', 224), 'installation': last_frac('installation_probes_ch4.out', 6), 'readback': last_frac('readback_probes_ch4.out', 9),
      'register': last_frac('register_probes_ch4.out', 7), 'sequence': last_frac('sequence_probes_ch4.out', 4), 'view': last_frac('view_probes_ch4.out', 6),
      'population': last_frac('population_probes_ch4.out', 9), 'journal': last_frac('journal_probes_ch4.out', 7), 'cursor': last_frac('cursor_probes_ch4.out', 6),
      'checkpoint': last_frac('checkpoint_probes_ch4.out', 7)}
ck = rd('clock_probes_ch4.out'); m = re.findall(r'(\d+)/(\d+)', ck); PR['clock'] = ('%s/%s' % m[-1]) if m else 'exit 0'
assert PR['checkpoint'] == 7, PR
run1 = rd('ch4_run1.out'); assert '52/52' in run1
hp = subprocess.run(['python3', 'logic/solo_tools/scrub_home_paths.py', '--check'], cwd=ROOT, capture_output=True, text=True); assert hp.returncode == 0, hp.stdout[-500:] + hp.stderr[-500:]
NUM = dict(RG=RG, DG=DG, DP=DP, LC=LC, DPR=DPR, JG=JG, SW=(SW_P, SW_CELLS), PO=PO, PR=PR, PL=PL.groups(), tape_elapsed=tape_elapsed)
print('THE NUMBERS:', NUM)
pr_line = ('census %d/224, installation %d/6 (I5 64), readback %d/9, register %d/7, clock %s, sequence %d/4, view %d/6, population %d/9, journal %d/7, cursor %d/6, checkpoint %d/7'
           % (PR['census'], PR['installation'], PR['readback'], PR['register'], PR['clock'], PR['sequence'], PR['view'], PR['population'], PR['journal'], PR['cursor'], PR['checkpoint']))
gates_line = ('the daemon gate GREEN (%d daemons, %d functions); the dependency gate GREEN (%d edges and %d pointers on file — the link census reference %d / transfer %d / hypothesis %d / none %d; required %d edges and %d pointers, live import edges %d); '
              'build_world ALL GREEN (standing 2191, hash 8b8fff1fa28953af unmoved); the journal gate GREEN twice — before and after the sweep (%d kinds, %d rows in the index); THE REGISTER GATE --strict GREEN (DECLARED %d, DEBT %d, FAILS %d — Deut 4:5 ACT declared, its write adding_barred on Israel; Deut 4:45 DAEMONS green with daemons 2: law_opening_speech@Deut 1:16 and law_obey_horeb@Deut 4:2); '
              'the positions table %d checkpoints over %d pauses (CC1-CC9 in it; checkpoint_probes %d/7 after the rebuild); the sweep %d/59 at %s graded cells; the home-path gate GREEN'
              % (DG[0], DG[1], DP[0], DP[1], LC[0], LC[1], LC[2], LC[3], DPR[0], DPR[1], DPR[2], JG[0], JG[1], RG[0], RG[1], RG[2], PO[0], PO[1], PR['checkpoint'], SW_P, format(SW_CELLS, ',')))

# ---- 1. THE MAP — AS BUILT ----
AS_BUILT = """

## Sitting 2b — THE COMPILE OF CHAPTER 4 — AS BUILT (2026-09-16; the design above stands as written; every departure from it named here)

THE RESULT. Deuteronomy 4:1-49 is COMPILED AND ON THE TAPE: World/step9/cold_run_obey_horeb.py the 59th runner (MATRIX 52/52 on its first graded run —
the fractions ink 8 / moves 37 / data 7; six cells F1 the_exhortation … F6 the_cities_and_the_frame with 52 asks; nineteen DATA rows; the readback's
eleven rows; 96 token probes fired; the guard 52 by the generated CASES; the scene and the narrative tuples matched as predicted), law_obey_horeb the
64th daemon (given_at Deut 4:2, installed_by boot with the vows' class named — a law in Moses' voice; six functions WRAPPED; WATCH seen 19 fired 19),
six kinds and four effects in the registries (1119 kinds, 1019 effects), five lines and four markers on the tape. THE TAPE 10/10 WITH THE REST:
RUN (1300, 96, 88, 0, 12, 1588, 35, 319, the four pairs, 126) exactly as THE PREDICTION'S ARITHMETIC wrote it; PREVIOUS_RUN 1b's reproduced by the
tape minus this runner's lines; NEWEST_RUNNER obey_horeb; markers 161 → 165 (forward 126 → 128, retrograde 20 → 22, proleptic 15); entities 319
UNMOVED (Israel and Moses the written-on parties), closes 126 UNMOVED (no close — the refuge debit stays OPEN by design), the population table 148
UNMOVED; PLACEMENT markers %s, events %s; CENSUS (2458, 1309, 1300, 1133, 6, 10, 9, 0, 71, 165, 128, 15, 22, 845, 272); CC1-CC9 all MATCH; the run
%ss. THE DOCKET logic/oral_triage/deu_04_vaetchanan_exam_2026-09-16.md by the union rule: 327 rows (link 68 / topic 259; CONTEXT 169, DERIVATION 70,
DISPUTE 12, LAW 76; credited 98), the nine Talmud ranges read whole (Rosh Hashanah 28b; Eruvin 95b-96a; Sanhedrin 88b-89a; Kiddushin 30a; Rosh
Hashanah 24a-24b; Avodah Zarah 55a; Ketubot 111b; Makkot 9b-10a; Berakhot 32b), ten Mishnah rows, sixteen crowns.

THE READBACK ON CHAPTER 4 (the first form's (R1)-(R6) applied): eleven reference rows — SHORTENED 3, EXPANDED 5, SUPPLIED 2, DISAGREES 1; every row's
tape entry FOUND on the running world by kind and first verse (CC4). THE TAPE'S HOLE, found by the measurement and filled here: the tape held no line for
Exodus 20:1 (the ten words spoken) nor for 31:18 (the first tablets given) — the decalogue runner compiled the law layer and the erection runner folded
the tablets into the ascent line — so both are told for the first time IN THE RETELLING and were written ONCE at their own days by RETROGRADE markers:
ten_words_declared at Deut 4:10-13 dated (1, 3, 7) (the sinai_days row's giving, Rabbi Yose's seventh — the Exodus 19:16 marker's day; CC2, CC5) and
tablets_given at Deut 4:13 dated (1, 4, 17) (the fortieth day — Taanit 28b; given and broken on one day: the same day as the tablets_broken line at
Exodus 32:19; CC5). The bar's THIRD telling (4:21-22, with an oath and a new ground) a second DISAGREES row beside 1b's 1:37 row, OPEN — no ledger
entry cites Deut 4:21 (CC4, CC6). The second frame (4:44-49) NO WRITE (R6). The receipt in Moses' own voice (4:5) a RUN CITATION with the register
class ACT — the exhortation's one write's source 4:1-8 contains the verse (CC3; the seat declared this sitting, the gate green).

THE LAW AND THE CASE. The one law (4:2, add nothing / diminish nothing) the cell F1 with the arms the docket taught (an addition IN ITS TIME and an
addition BESIDE the mitzvah — Rosh Hashanah 28b, Eruvin 95b-96a, Sanhedrin 88b-89a; 13:1 its second seat forward): its write adding_barred, a BLOCK on
Israel with its source beginning "Deut 4:1" (CC3). The one case (4:25-31) the kind horeb_case with its arms the exile and the return (accepted / exempt)
— "in the end of days" a prophecy, no timer set by the sitting's lines (CC7). Moses' three cities (4:41-43): the act three_cities_set_apart writes
cities_set_apart, a STATUS on Israel valued the three by CALL to the refuge runner's row, and THE REFUGE DEBIT appoint_six_cities_of_refuge STAYS OPEN —
the design's departure from the reading's "closed here", decided on Mishnah Makkot 2:4 and Makkot 9b-10a (the three east admitted no one until Joshua's
three; "six cities shall they be", Numbers 35:13): the close is outside the Torah at Joshua 20:7-8 (CC8). The witnesses (4:26) a status
heaven_and_earth_witness on Israel dated (40, 11, 1) (CC7). THE SECOND WORD (Exodus 20:3-6, the image law) has NO CELL in any runner: the no-image list
of 4:16-19 is DATA (its parameter table), the edge obey_horeb → decalogue a live CALL whose why names the debt — OWED to chapter 5's sitting.

THE DEPARTURES FROM THE DESIGN, each found by an instrument and each a lesson below: (1) add_nothing_commanded's form is STATUTE, not speech — the
stitcher's register test dropped the line (no wayyiqtol, "and he did", in 4:1-8; the chapter's first narrative verb is at 4:11), and a law sentence in
the narrator's own mouth is the statute form (sinew_barred's); (2) FOUR markers, not two — the retrograde stretch after 4:13 ran to the next marker and
dated the witnesses' and the cities' own-day lines, so a FORWARD marker at Deut 4:25 (speech_resumed = the speech's day) closes it; and the
exhortation's line fell INSIDE 1b's Deut 2:2 stretch, still open on the tape, so a FORWARD marker at Deut 4:1 (chapter_4 = the speech's day) opens the
chapter — markers 165 (the design's arithmetic said 163); CA1's forward-marker list is now three (40, 11, 1) entries; (3) the census's kinds column is
845, not 846 — the case kind is no tape kind; (4) CC5 and CC6 select their lines BY VERSE OR VALUE: lord_descended has two lines on the tape (Babel at
Genesis 11:5 and Horeb at Exodus 19:18), plague_struck on the people three, and Numbers 33:50-56 wrote TWO debits; (5) the marker row for Deut 4:13
declares the verse's numbers [10, 2]; (6) the tape took SIX runs to 10/10 — the missing retypes (run 1), Babel's line dated before the exodus era's
epoch (2), an undefined registry name (3), a write script that aborted on its own assertion and wrote nothing (4), the eras read off the world instead
of the clock (5), 10/10 (6).

THE GATES, COMPUTED FROM THEIR PRINTS: the probe suites %s; %s.

⚠ THE LESSONS OF 2b (eleven): (1) A RETROGRADE STRETCH RUNS TO THE NEXT MARKER — every own-day line after a supplied line needs a FORWARD marker back
to the counter's day (Leviticus 9:1's form); (2) A NEW CHAPTER AFTER A STRETCH OPENS WITH A FORWARD MARKER — the previous sitting's stretch is still
open on the tape; check the tape's last marker before designing the chapter's first line; (3) A LAW CLAUSE IN A SPEECH WITH NO NARRATIVE VERB IS A
STATUTE-FORM LINE — the stitcher's register test reads the form; (4) THE MARKER ROW DECLARES THE VERSE'S NUMBERS — the stitcher's ink check reads them;
(5) A HEREDOC-WRITTEN MARKER ROW NEEDS THE APOSTROPHE DOUBLY ESCAPED (the file must hold two backslashes); (6) A CALLEE'S ASK IS TYPED FROM THE RECON'S
PRINT, never from memory (the tablets' torah_mitzvah is the ascent cell's); (7) THE CENSUS COUNTS TAPE KINDS ONLY; (8) A KIND SHARED ACROSS BOOKS IS
SELECTED BY VERSE — a checkpoint that dates "the" line of a kind must name the verse (Babel's descent shares lord_descended with Horeb's); an effect
written thrice on one party is selected by verse or value; (9) THE ERAS LIVE ON THE CLOCK (w.clock.eras), not on the marker's log line; the effects
registry is read from its YAML, not from a module name; (10) A WRITE SCRIPT NEVER GATES ITS WRITES ON AN UNVERIFIED ASSERTION — compute, print, read,
then write in a second script (the aborted script cost a tape run); the DB stores a word's morphemes split by a slash (עָבְרִ/י, "my crossing"); (11)
THE FAST CHECKER'S TAGS ARE TYPED FROM THE PRINT (a morph tag; `A and B or C` binds as `(A and B) or C`).

THE DISPOSITIONS ADDED: sixteen edges (eleven CALL — balak, refuge, opening_speech, erection, exodus_story, tochacha, pre_sinai, primeval, decalogue
with the second word's debt in its why, chukat, borders; the registration edge sequence → obey_horeb; four FALSE by the sense or the points —
family [inheritance] at 4:20, 4:21, 4:38 (the land a gift named whole, no estate divided), lev24 [talion_formula] at 4:11, 4:19, 4:49 (the preposition
"under"), mishpatim [hebrew_slave] at 4:21 ("my crossing", not "a Hebrew" — the qamats against the chirik, lemma 5674 against 5680), sanctions
[molech_ov] at 4:46-47 (the kings, not Molech)) and two pointers (RUN_CITATION — Deut 4:5 the receipt of the teaching's command, Exodus 24:12 by the
erection runner's ascent cell; Deut 4:33 "as you have heard", the voice at Horeb on the tape).

THE FORMS: the sitting's scripts and prints copied into World/step9/forms_deuteronomy_walk/ by copy_ch4b_forms.py (the recon, the docket's scan and
parts, the types, the probes' patch, the runner's four parts with the generator, the assembler and the fast checker, the recorder and the stitcher
under their sitting's names, the literals' patcher, the seat's declaration, the design's and the records' writers, the chains, the gates' prints —
no scratch path and no home path in any copied form). MOVE_CATALOG CHECKED, unmoved: the runner's 37 move cells are CALLS into the callees and the
shelf's own readings (Ketubot 111b:6-8 and Sotah 14a:3 with the Sifrei 49:2 — cleaving to the LORD as cleaving to His ways); no new move.

NEXT on the ruling: SITTING 3 — chapter 5's reading (the export's thirty-verse chapter 5 measured against the DB's thirty-three FIRST); the
Decalogue-schema sitting (on the table) after 2b on the owner's word — its natural seat chapter 5, where the code is restated and the laws' readback
opens. Nothing committed: the tree uncommitted since b8b721d, on the owner's word only.
""" % (PL.group(1), PL.group(2), tape_elapsed, pr_line, gates_line)

# ---- 2. COMPILE_DEBT — the sitting-2 box marked PAID (1b's precedent) + the 2b box ----
DEBT_HDR_OLD = "## units deu_04_obey_horeb, deu_04_refuge_east FROZEN) — OWED TO THE COMPILE (sitting 2b), each item named at its verse: (a) THE ONE LAW — 4:2's \"you"
DEBT_HDR_NEW = "## units deu_04_obey_horeb, deu_04_refuge_east FROZEN) — PAID AT 2b (the 2b box below, item by item) — AS WRITTEN AT THE READING, OWED TO THE COMPILE (sitting 2b), each item named at its verse: (a) THE ONE LAW — 4:2's \"you"
DEBT_BOX = """
## DEUTERONOMY SITTING 2b — THE COMPILE OF CHAPTER 4 (2026-09-16; DEUTERONOMY_WALK.md "Sitting 2b" design + AS BUILT; logic/oral_triage/deu_04_vaetchanan_exam_2026-09-16.md
## 327 rows; cold_run_obey_horeb.py 52/52; law_obey_horeb the 64th daemon; the tape 10/10 with RUN (1300, 96, 88, 0, 12, 1588, 35, 319, pairs, 126)). THE SITTING-2
## BOX (a)-(l) PAID — (a) the one law the cell F1 (adding_barred a BLOCK on Israel, its arms in-its-time / beside from Rosh Hashanah 28b, Eruvin 95b-96a, Sanhedrin
## 88b-89a; 13:1 forward); (b) the one case the kind horeb_case with the arms the exile and the return (no timer — a prophecy); (c) the receipt's seat Deut 4:5 declared
## ACT (the write's source contains the verse; the register gate green) — the class predicted from the gate's code, (R5); (d) the three cities the act
## three_cities_set_apart writing cities_set_apart, a STATUS valued the three by CALL — THE REFUGE DEBIT LEFT OPEN (Mishnah Makkot 2:4 / 9b-10a: not until all six;
## the close Joshua 20:7-8, outside the Torah); (e) the readback's eleven rows (SHORTENED 3, EXPANDED 5, SUPPLIED 2, DISAGREES 1), THE TAPE'S HOLE filled — the ten
## words spoken and the tablets given, written once at (1, 3, 7) and (1, 4, 17) by retrograde markers; the bar's third telling a second open DISAGREES row; (f) the
## two frames' day — the second frame NO WRITE (R6), 4:45 the footer of the block (Deut 1:1, Deut 4:45] with daemons 2 (green); (g) the no-image list DATA — the
## second word's parameter table, the pointer to Exodus 20:4 in the CALL edge's why; (h) the host "apportioned" a DATA note (Avodah Zarah 55a:9 "let slip" — no link
## of our own); (i) the chapter-5 division — the recorder and the stitcher address by the DB; the next reading's first measurement STANDS OWED; (j) the gloss families
## a display sitting's, unmoved; (k) the docket by the union rule (the nine ranges whole; ten Mishnah rows; sixteen crowns); (l) the Mekhilta's question credited by
## name (the reading shelf's). OWED FROM 2b: (i) THE SECOND WORD — Exodus 20:3-6 (the image law) has NO CELL in any runner; the edge obey_horeb → decalogue
## (DC.altar_rules('steps')) names the debt in its why; 4:16-19's list its parameter table; OWED to chapter 5's sitting (the Decalogue's second copy) — the schema
## sitting on the table its natural home; (ii) THE REFUGE DEBIT — appoint_six_cities_of_refuge OPEN on Israel since Numbers 35:14, unmoved by Moses' three (a status,
## not a close); the close at Joshua 20:7-8, THE READBACK's when the Prophets are walked; (iii) THE D2 CANDIDATE — law_decalogue's installed_by: the tape now
## carries ten_words_declared at its own day (1, 3, 7); whether the giving's line installs the decalogue daemon (D2 — installation by an act) is a loop sitting's
## decision, the row unmoved (boot); (iv) THE BAR'S THIRD TELLING — the DISAGREES rows 1:37 and 4:21-22 OPEN, no write; (v) 4:26's "not prolong days" and 4:30's
## "in your distress … return" open topics (the tochacha's scattered_among_nations registered, never written — no exile on the tape); (vi) THE CHAPTER-5 DIVISION —
## the export's thirty verses against the DB's thirty-three, measured FIRST at chapter 5's reading. NOTHING ELSE IN CHAPTER 4 IS OWED TO A LATER SITTING OF ITS OWN.
"""

# ---- 3. MIDDOT — the docket entry (before the Exodus block campaign header, after sitting 2's reading entry) ----
MIDDOT_ANCHOR = "\n## Exodus block campaign — owner's word \"Do 3\")\n"
MIDDOT_ENTRY = """- THE CHAPTER-4 DOCKET (THE DEUTERONOMY WALK sitting 2b, 2026-09-16; logic/oral_triage/deu_04_vaetchanan_exam_2026-09-16.md — 327 rows; the rules
  about rules the docket carries, each at its row):
  · "YOU SHALL NOT ADD" READ AS A COUNT IN ITS TIME (Rosh Hashanah 28b; Eruvin 95b-96a; Sanhedrin 88b-89a on Deuteronomy 4:2 and 13:1): the priest who
    adds a blessing, the sleeper who adds a blast, tefillin at night or a second pair, the rebellious elder's fifth compartment — an addition counts
    when the mitzvah's TIME holds and the thing is added BESIDE it: the cell's two arms (add_out_of_its_time / add_beside), a parameter of time on a
    prohibition without a case token.
  · THE IMAGES OF THE MOON (Rosh Hashanah 24a-24b on Rabban Gamliel's forms, Mishnah 2:8; Avodah Zarah 3:1-3 credited): a court's teaching
    instruments against "the likeness of any figure" (4:16-19) — the arms image_for_study / image_of_the_host of the second word's parameter table,
    the engine itself OWED (no cell compiles Exodus 20:3-6).
  · TEACH YOUR SONS' SONS (Kiddushin 30a on 4:9-10): "make them known to your sons and your sons' sons" — the grandfather's duty read off the doubled
    noun; "the day you stood before the LORD at Horeb" the next verse — teaching a grandson is standing at Horeb: a DATA row (the_teach_your_sons),
    the learn/teach one word (4:10's two pointings) beside it.
  · THE HOST "ALLOTTED" READ "LET SLIP" (Avodah Zarah 55a:9 on 4:19; Onkelos "prepared"): the same letters, a second sense kept alive by Rav Yehuda's
    explanation — a DATA note at the row the_host_apportioned, no link of our own (the reading's (h)).
  · CLEAVING TO THE LORD (Ketubot 111b:6-8; Sotah 14a:3; the Sifrei 49:2 on 4:4 and 11:22): "is He not a consuming fire?" — the impossible literal
    replaced by cleaving to His ways and to scholars: a substitution reading, the runner's move cell.
  · "NOT UNTIL ALL SIX" (Mishnah Makkot 2:4; Makkot 9b-10a on 4:41-43 with Numbers 35:13): Moses' three admitted no one until Joshua's three — the
    act a STATUS (cities_set_apart), the debit OPEN, the close outside the Torah: the design's departure from the reading's "closed here", decided on
    the Mishnah's word.
  · THE FORMER DAYS AS A BOUND (Chagigah 11b:21; Tosefta Chagigah 2:3; Mishnah Chagigah 2:1 on 4:32): "from the day God created man" — one may ask,
    two may not; the bound of inquiry a DATA row (the_former_days), no rule.
  · THE JUDGE'S WAGES (Bekhorot 29a:7 on 4:5; Mishnah Bekhorot 4:6): "as the LORD my God commanded me" — as I taught for free, so you: the receipt
    verse read as a rule about teaching; a row at F1 taught_as_commanded, no cell.
  · MOSES' PLEA AND THE BAR (Berakhot 32b on 3:23-26 and 4:21): "the LORD was angry with me on your account" — the bar's third ground; the DISAGREES
    row widened beside 1:37's, OPEN, no write.
"""

# ---- 4. MISHNAH_TOPICS — the rows touched, a note appended to each ----
TOPIC_NOTES = {
 "**1. Mishnah, Blessings**": " — 5:1's gemara Berakhot 32b READ 2026-09-16 (THE DEUTERONOMY WALK sitting 2b, chapter 4's docket: Moses' plea and the bar 'on your account', Deuteronomy 3:23-26 / 4:21; deu_04_vaetchanan_exam_2026-09-16.md)",
 "**13. Mishnah, Merging Domains**": " — 10:1's gemara Eruvin 95b-96a READ 2026-09-16 (THE DEUTERONOMY WALK sitting 2b: tefillin at night and a second pair under 'you shall not add', Deuteronomy 4:2 — the addition in its time)",
 "**14. Mishnah, Passover**": " — 10:4 READ 2026-09-16 (THE DEUTERONOMY WALK sitting 2b, chapter 4's docket: the son's questions and the telling's order — 4:34's exodus 'with signs and wonders' by reference; deu_04_vaetchanan_exam_2026-09-16.md)",
 "**19. Mishnah, New Year**": " — 2:8 READ with its gemara 24a-24b, and 3:7's gemara 28b READ 2026-09-16 (THE DEUTERONOMY WALK sitting 2b: Rabban Gamliel's forms of the moon against the image law, 4:16-19; the priest who adds a blessing under 'you shall not add', 4:2)",
 "**23. Mishnah, Pilgrimage Offering**": " — 2:1 CREDITED 2026-09-16 (THE DEUTERONOMY WALK sitting 2b: Chagigah 11b:21 and Tosefta Chagigah 2:3 — 'ask now of the former days', 4:32, the bound of inquiry)",
 "**25. Mishnah, Marriage Contracts**": " — 13:11's gemara Ketubot 111b READ 2026-09-16 (THE DEUTERONOMY WALK sitting 2b: 'you who cleave to the LORD', 4:4 — cleaving to scholars; the land's dead)",
 "**30. Mishnah, Betrothal**": " — 1:7's gemara Kiddushin 30a READ 2026-09-16 (THE DEUTERONOMY WALK sitting 2b: 'make them known to your sons and your sons' sons', 4:9 — the grandfather's duty; the day you stood at Horeb, 4:10)",
 "**34. Mishnah, Courts**": " — 11:2-4's gemara Sanhedrin 88b-89a READ 2026-09-16 (THE DEUTERONOMY WALK sitting 2b: the rebellious elder who adds a fifth compartment — 'you shall not add', 4:2)",
 "**35. Mishnah, Lashes**": " — 2:4 READ with its gemara Makkot 9b-10a 2026-09-16 (THE DEUTERONOMY WALK sitting 2b: Moses' three cities admitted no one until Joshua's three, 4:41-43 — the refuge debit left OPEN, cities_set_apart a status; Bezer not Bozrah, Avodah Zarah 58b)",
 "**38. Mishnah, Idolatry**": " — 3:1-3 CREDITED and 4:7's gemara 55a READ 2026-09-16 (THE DEUTERONOMY WALK sitting 2b: the host 'allotted' read 'let slip', 4:19; the jealousy parables 54b-55a on 4:24)",
 "**39. Mishnah, Fathers (ethics)**": " — 3:8 READ 2026-09-16 (THE DEUTERONOMY WALK sitting 2b: 'whoever forgets one word of his learning' — 4:9 'lest you forget')",
 "**44. Mishnah, Firstborn**": " — 4:6's gemara Bekhorot 29a READ 2026-09-16 (THE DEUTERONOMY WALK sitting 2b: the judge who takes wages — 'as the LORD my God commanded me', 4:5, taught for free)",
}

# ---- 5. RESEARCH_LOG ----
RLOG = """

## 2026-09-16 — DEUTERONOMY 4 COMPILED (THE DEUTERONOMY WALK sitting 2b — CHAPTER 4): THE TAPE'S HOLE — TWO ACTS THE TAPE NEVER WROTE; A RETROGRADE
## STRETCH RUNS TO THE NEXT MARKER; A LAW SENTENCE WITH NO NARRATIVE VERB; A KIND SHARED ACROSS BOOKS; THE SECOND WORD UNCOMPILED; THE REFUGE DEBIT
## LEFT OPEN ON THE MISHNAH'S WORD

THE TAPE'S HOLE. The measurement before the design read the tape from Exodus 19:20 to 24:1 and found NO LINE for the ten words spoken (Exodus 20:1)
nor for the first tablets given (31:18): the decalogue runner compiled the law layer only, and the erection runner folded the tablets into the ascent
line. Deuteronomy 4:10-13 tells both — "he declared to you his covenant … the ten words; and he wrote them on two tablets of stone" — so THE RETELLING
IS THEIR FIRST TELLING ON THE TAPE. The readback's first form (1b) already had the case: an act told only in the retelling is written ONCE at its own
time by a retrograde marker. Here two: ten_words_declared at (1, 3, 7) — the sinai_days row's giving, Rabbi Yose's seventh, the day of the Exodus
19:16 marker — and tablets_given at (1, 4, 17), the fortieth day (Taanit 28b), the same day as the tape's tablets_broken line at Exodus 32:19: given
and broken on one day, the checkpoint CC5 reads both dates off the ledger. The two rows graded SUPPLIED; the other nine SHORTENED 3, EXPANDED 5,
DISAGREES 1 (the bar's third telling, 4:21-22, with an oath and a new ground — a second open row beside 1:37's).

A RETROGRADE STRETCH RUNS TO THE NEXT MARKER. The stitcher's first census placed the chapter's last two lines (the witnesses, the cities) INSIDE the
stretch the 4:13 marker opened, dated to the seventeenth of Tammuz of the first year — and the chapter's first line inside 1b's Deuteronomy 2:2 stretch,
still open on the tape after the previous sitting. The engine's rule, read off the census: a retrograde marker's stretch runs to the NEXT marker, so an
own-day line after a supplied line needs a FORWARD marker back to the counter's day (Leviticus 9:1's form), and a chapter that opens after a stretch
opens with one. Four markers, not the design's two: forward at 4:1, retrograde at 4:10 and 4:13, forward at 4:25. Markers 165.

A LAW SENTENCE WITH NO NARRATIVE VERB. The stitcher dropped the exhortation's line as 'register': its test wants a wayyiqtol ("and he did", the
narrative verb form) within a window of the cited verses, and 4:1-8 has none — the chapter's first is at 4:11. The line is the narrator's own law
sentence (4:2, add nothing, diminish nothing); its form is STATUTE, the form of sinew_barred and statute_set, which the test passes by form. The
kind's form was retyped in the registry with the reason beside it.

A KIND SHARED ACROSS BOOKS. The checkpoint CC5 dated "the" lord_descended line and crashed the run: the kind has TWO lines on the tape — Babel's
descent at Genesis 11:5 (the primeval runner) and Horeb's at Exodus 19:18 — and the first falls before the exodus era's epoch. A checkpoint that dates a
kind's line names the VERSE. The same lesson twice more in the next run: plague_struck on the people three times (Numbers 11, 17, 25); Numbers
33:50-56's command two debits. The other crashes of the six tape runs were the sitting's own: the missing retypes, a registry read by a module name that
does not exist (the effects registry is its YAML), the eras read off the world instead of the clock, and a write script that gated its writes on an
unverified assertion and wrote nothing — a rule written down: compute, print, read, then write.

THE SECOND WORD UNCOMPILED. The no-image list of 4:16-19 (figure, male, female, beast, bird, creeping thing, fish, sun, moon, stars, the host) is the
parameter table of Exodus 20:3-6, and the measurement found that NO RUNNER HAS A CELL for the image law: the decalogue runner's cells are the altar
rules and the ten as a list. The list is DATA here; the edge obey_horeb → decalogue is a live CALL whose why names the debt; the docket's Rosh Hashanah
24a-24b (Rabban Gamliel's forms of the moon) and Avodah Zarah 3:1-3 are its test rows, filed. Owed to chapter 5's sitting, where the ten are restated —
and where the schema question on the table (the ten as headers over the laws) has its seat.

THE REFUGE DEBIT LEFT OPEN. The reading said Moses' three cities (4:41-43) CLOSE the refuge runner's debit open since Numbers 35:14. The docket said
otherwise: Mishnah Makkot 2:4 and Makkot 9b-10a — the three east of the Jordan admitted no one until Joshua's three were set apart, "six cities shall
they be" (Numbers 35:13). The act writes a STATUS (cities_set_apart on Israel valued the three, by CALL to the refuge runner's row) and the debit stays
OPEN; the close is Joshua 20:7-8, outside the Torah, THE READBACK's when the Prophets are walked. Closes 126 unmoved.

THE DISPOSITIONS BY THE POINTS. Four token-demanded edges FALSE, each told by the vowels or the lemma: "my crossing" (4:21, the qamats under the ayin,
lemma 5674) is not "a Hebrew" (the chirik, 5680); "king" (4:46-47, the segols) is not "Molech" (the cholam with the dagesh); "under" (4:11, 4:19, 4:49)
is the preposition, not the talion's "in place of"; "inheritance" (4:20, 4:21, 4:38) the land as a gift named whole, no estate divided. Two pointers
RUN_CITATION: 4:5's receipt of the teaching's command (Exodus 24:12, by the erection runner's ascent cell) and 4:33's "as you have heard" (the voice at
Horeb on the tape).
"""

# ---- 6. THE_STEPS ----
STEPS_ANCHOR = "\n## Step 6 — Publish\n"
STEPS_PARA = """
DEUTERONOMY — SITTING 2b — CHAPTER 4 COMPILED (2026-09-16, on Brian's "ok get ready to compact. then we finish 4" — the word given before the
compaction; World/step9/DEUTERONOMY_WALK.md "Sitting 2b" and "Sitting 2b — AS BUILT"). The compile ran in the walk's order — the measurements, the
design in the map before any code, the probes written to fail, the docket by the union rule, the types, the gates to fail, the runner, the recorder
and the stitcher, the literals, the tape, the gates, the records. The measurement found a hole in the tape: no line for the ten words spoken at Horeb
and none for the first tablets given — the earlier runners compiled the law and folded the tablets into the ascent. Chapter 4 tells both, so the
retelling is their first telling, and they were written once at their own days by the readback's retrograde markers — the giving on Rabbi Yose's
seventh of Sivan, the tablets on the seventeenth of Tammuz, the same day the tape breaks them. The stitcher then taught the engine's own rule back to
the design: a retrograde stretch runs to the next marker, so a forward marker closes it and another opens the chapter, four markers where the design
drew two. The chapter's one law compiled as a block with the shelf's two arms (an addition in its time, an addition beside), its one case as a kind
with the exile and the return as arms, Moses' three cities as a status — and the refuge law's debt stays open on the Mishnah's word, not until all six,
its close in Joshua. The second word of the ten — the image law — turned out to have no cell anywhere; its list of forms is data here and the debt is
named at the edge. The runner reproduced the answer sheet on its first graded run; the tape reached ten of ten on its sixth, each miss read from the
print and each a lesson written down; every probe suite and every gate green, the sweep whole. Next: chapter 5's reading, measuring the export's
thirty verses against the database's thirty-three first; the schema question waits on your word.
"""

# ---- 7. THE_BRIEFING ----
BRIEF_SB_OLD = "## SCOREBOARD (as of 2026-09-15, latest)\n"
BRIEF_SB_NEW = "## SCOREBOARD (as of 2026-09-16, latest)\n"
BRIEF_BULLET_ANCHOR = "- **CHAPTER 4 READ AND FROZEN — THE SHELF IS SILENT ON THE WHOLE CHAPTER"
BRIEF_BULLET = ("- **CHAPTER 4 COMPILED — THE TAPE HAD A HOLE AND THE RETELLING FILLED IT: THE TEN WORDS SPOKEN AND THE TABLETS GIVEN, TOLD ONLY IN MOSES' RETELLING, WRITTEN ONCE AT THEIR OWN DAYS; THE ONE LAW A BLOCK WITH THE SHELF'S TWO ARMS; MOSES' THREE CITIES A STATUS, THE REFUGE DEBT OPEN UNTIL JOSHUA; THE IMAGE LAW FOUND UNCOMPILED AND NAMED AS DEBT** "
                "(2026-09-16, on your \"then we finish 4\"; World/step9/DEUTERONOMY_WALK.md \"Sitting 2b\" + AS BUILT): cold_run_obey_horeb.py the 59th runner (52/52), law_obey_horeb the 64th daemon; the readback's eleven rows; the tape 10/10 with RUN (1300, 96, 88, 0, 12, 1588, 35, 319, pairs, 126) as predicted, markers 165; every gate GREEN, the sweep %d/59. NEXT: chapter 5's reading.\n" % SW_P)
BRIEF_ENTRY_ANCHOR = "### 2026-09-16 — CHAPTER 4 READ: THE SHELF IS SILENT, THE CHAPTER HAS ONE LAW, AND MOSES' THREE CITIES WAIT FOR THE COMPILE\n"
BRIEF_ENTRY = """### 2026-09-16 — CHAPTER 4 COMPILED: THE TAPE HAD A HOLE, AND THE RETELLING FILLED IT AT ITS OWN TIME

Before any code was written, the tape was measured against the chapter, and the measurement found something the first three chapters had not shown:
two acts that the tape never wrote. Exodus 19-24 is on the tape, but the moment the ten words are spoken and the moment the tablets are handed over
are not lines there — the earlier compiles took the ten as law and folded the tablets into Moses' ascent. Chapter 4 tells both plainly. So the rule
built at the first three chapters did its work here in the strongest case: a retelling that is the FIRST telling is still written once, at its own
day, by a marker that reaches back — the ten words on the seventh of Sivan the shelf gives, the tablets on the seventeenth of Tammuz, the same day the
tape already breaks them. The chapter's one law (add nothing, take nothing away) became a block with the two arms the Talmud argues — an addition in
the mitzvah's own time, an addition beside it; its one case (when you grow old and corrupt) became a kind with the exile and the return as its arms
and no timer, because "the end of days" is a prophecy, not a due date. Moses' three cities, which the reading expected to close the refuge law's
debt, do not: the Mishnah says the three east of the Jordan sheltered no one until Joshua's three, so the act is a status and the debt stays open
until a book we have not walked. And one debt was found by looking: the second of the ten words, the image law, has no cell in any runner; the
chapter's list of forbidden forms is its parameter table, kept as data, and the debt is named at the edge that calls the Decalogue. The stitcher
corrected the design three times from its own census — a stretch of supplied time runs until a marker ends it, a chapter that opens after such a
stretch opens with one, a law sentence with no narrative verb is a statute line — and the tape took six runs to reach ten of ten, each miss a lesson
now written down. Every gate is green and the sweep is whole. Next: chapter 5, where the ten words are restated and the laws' readback opens.

"""

# ---- 8. THE_LOOP step-6 row ----
LOOP_OLD = "readback_probes.py 6/6, the tape's CA4-CA8 |"
LOOP_NEW = ("readback_probes.py 6/6, the tape's CA4-CA8; cold_run_obey_horeb.py (chapter 4 on the same form, 2026-09-16 — eleven rows; THE TAPE'S HOLE: the ten words spoken and the tablets given, told only in the retelling, "
            "written once at their own days by two retrograde markers with a forward marker closing the stretch; the bar's third telling a second open row; readback_probes 9/9, CC4-CC6) |")

# ---- 9. RESUME ----
RESUME_HEAD = """# ⚠ THE DEUTERONOMY WALK sitting 2b (2026-09-16; step9/DEUTERONOMY_WALK.md "Sitting 2b" + "Sitting 2b — AS BUILT"): CHAPTER 4 COMPILED —
# step9/cold_run_obey_horeb.py the 59th runner (52/52; six cells; the readback's eleven rows), law_obey_horeb the 64th daemon (given_at Deut 4:2);
# THE TAPE'S HOLE filled: the ten words spoken and the tablets given, told only in the retelling, written once at (1, 3, 7) and (1, 4, 17) by
# retrograde markers (a forward marker closes the stretch, another opens the chapter — four markers); Moses' three cities a STATUS, the refuge debit
# OPEN until Joshua's three (Mishnah Makkot 2:4); the second word (the image law) found UNCOMPILED — its list DATA, the debt named at the edge; the
# tape 10/10 with RUN (1300, 96, 88, 0, 12, 1588, 35, 319, pairs, 126) as predicted, markers 165; every probe suite and gate GREEN, the sweep %d/59.
# NEXT on the ruling: chapter 5's reading (the export's thirty verses measured against the DB's thirty-three FIRST); the schema sitting on the owner's word.
""" % SW_P

# ---- 10. THE STATE DOC — #186 ADDENDUM 1 ----
STATE_ADD = """
#186 ADDENDUM 1 (2026-09-16, at the close of THE DEUTERONOMY WALK sitting 2b — THE COMPILE OF CHAPTER 4 — A CLEAN COMPACTION POINT): THE SITTING RAN
END TO END in the compile shape after the compaction (the rereads → the retypes → the tape → the gates → the records); the map's "Sitting 2b — AS BUILT"
is the record (the departures, the six tape runs, the eleven lessons, the gates computed from their prints). THE STATE: cold_run_obey_horeb.py the 59th
runner (52/52), law_obey_horeb the 64th daemon (%d daemons, %d functions), the registries 1119 kinds / 1019 effects, the tape 10/10 with RUN (1300, 96,
88, 0, 12, 1588, 35, 319, the four pairs, 126) and markers 165 (F 128 / P 15 / R 22), entities 319, closes 126, the population table 148; the docket
logic/oral_triage/deu_04_vaetchanan_exam_2026-09-16.md (327 rows); the readback's eleven rows (SHORTENED 3, EXPANDED 5, SUPPLIED 2, DISAGREES 1) with THE
TAPE'S HOLE filled — ten_words_declared at (1, 3, 7) and tablets_given at (1, 4, 17) by retrograde markers, forward markers at Deut 4:1 and 4:25; the
refuge debit OPEN by design (Mishnah Makkot 2:4); the second word OWED (no cell compiles Exodus 20:3-6). THE GATES: the probe suites %s; %s. THE RECORDS
written: the map's AS BUILT, COMPILE_DEBT (the sitting-2 box PAID; the 2b box with six owed items), MIDDOT's docket entry (nine rules about rules),
MISHNAH_TOPICS (twelve rows), RESEARCH_LOG, THE_STEPS, THE_BRIEFING (the bullet and the entry), THE_LOOP's step-6 row, World/RESUME.md, the recovery
file's section 34, memory (deuteronomy-walk.md, MEMORY.md under 17,000 bytes); the forms copied by copy_ch4b_forms.py. NOT COMMITTED (the tree
uncommitted since b8b721d — the owner's word only; NOT PUSHED). NEXT ON THE RULING: SITTING 3 — chapter 5's reading (measure the export's thirty-verse
chapter 5 against the DB's thirty-three FIRST); the Decalogue-schema sitting (ON THE TABLE, not a ruling) after it on the owner's word — its seat chapter 5.
IF THIS COMPACTS HERE: reread the recovery file's section 34, the map's "Sitting 2b — AS BUILT" and THE_LOOP.md's step-6 row; nothing is mid-flight.
""" % (DG[0], DG[1], pr_line, gates_line)

# ---- 11. THE RECOVERY FILE — section 34 ----
RECOVERY_ADD = """
## 34. ADDENDUM (2026-09-16, THE DEUTERONOMY WALK sitting 2b — THE COMPILE OF CHAPTER 4, Deuteronomy 4:1-49 COMPILED AND ON THE TAPE; the owner: "ok get ready to compact. then we finish 4" — the word given before the compaction; the state doc's COMPACTION POINT #186 + ADDENDUM 1)

THE SITTING RAN IN THE COMPILE SHAPE (section 5; "Sitting 1b" the form on this book): World/step9/DEUTERONOMY_WALK.md "Sitting 2b" (the design, written
before any code) and "Sitting 2b — AS BUILT" (the departures and the lessons). THE STATE: cold_run_obey_horeb.py the 59th runner (52/52 — six cells,
nineteen DATA rows, the readback's eleven rows, 96 token probes), law_obey_horeb the 64th daemon (given_at Deut 4:2, boot with the vows' class named;
%d daemons, %d functions), event_vocabulary +6 (1119), effect_vocabulary +4 (1019), dependency_dispositions +16 edges +2 pointers (%d edges, %d pointers
on file), register_dispositions Deut 4:5 ACT; THE TAPE 10/10 WITH THE REST — RUN (1300, 96, 88, 0, 12, 1588, 35, 319, the four pairs, 126) as predicted,
PREVIOUS_RUN 1b's, NEWEST_RUNNER obey_horeb, markers 165 (F 128 / P 15 / R 22), entities 319, closes 126, the population table 148, CC1-CC9 MATCH; the
docket logic/oral_triage/deu_04_vaetchanan_exam_2026-09-16.md (327 rows — link 68 / topic 259; LAW 76; credited 98; the nine ranges whole). THE GATES:
the probe suites %s; %s.

WHAT THE SITTING FOUND (RESEARCH_LOG 2026-09-16, the compile entry): THE TAPE'S HOLE — no line for Exodus 20:1 (the ten words spoken) nor 31:18 (the
tablets given): both told first in the retelling and written ONCE at their own days by retrograde markers at Deut 4:10 (1, 3, 7) and 4:13 (1, 4, 17);
A RETROGRADE STRETCH RUNS TO THE NEXT MARKER (forward markers at 4:1 and 4:25 — four, not the design's two); A LAW SENTENCE WITH NO NARRATIVE VERB is a
statute-form line (add_nothing_commanded); A KIND SHARED ACROSS BOOKS is selected by verse (lord_descended at Genesis 11:5 and Exodus 19:18); THE
SECOND WORD (Exodus 20:3-6, the image law) has NO CELL in any runner — 4:16-19's list DATA, the debt named at the edge obey_horeb → decalogue, OWED to
chapter 5's sitting; THE REFUGE DEBIT LEFT OPEN on Mishnah Makkot 2:4 (Moses' three a STATUS; the close Joshua 20:7-8, outside the Torah); the bar's
third telling (4:21-22) a second DISAGREES row OPEN beside 1:37's. THE ELEVEN LESSONS in the map's AS BUILT (the stretch's forward marker; the chapter's
opening marker; the statute form; the marker row's numbers; the doubly escaped apostrophe; the callee's ask from the recon's print; the census's tape
kinds; a shared kind by verse; the eras on the clock; a write script never gates on an unverified assertion; the fast checker's tags from the print).

THE FILES CHANGED BY 2b: World/step9/cold_run_obey_horeb.py (new), cold_run_sequence.py (the tape section, the literals, CC1-CC9, CA1/CC1/CC9's
retypes, CP6), event_vocabulary.yaml, effect_vocabulary.yaml, daemon_dispositions.yaml, dependency_dispositions.yaml, register_dispositions.yaml,
readback_probes.py (Q7-Q9; Q4 narrowed), checkpoint_probes.py (beyond_the_tape()), installation_probes.py (I5 64), checkpoint_positions.yaml (rebuilt),
the docket (new), the forms folder (copy_ch4b_forms.py), the records (the map, COMPILE_DEBT, MIDDOT, MISHNAH_TOPICS, RESEARCH_LOG, THE_STEPS,
THE_BRIEFING, THE_LOOP, RESUME, this file, the state doc, memory). NOT COMMITTED — the tree uncommitted since b8b721d; commit on the owner's word only.

NEXT ON THE RULING: SITTING 3 — CHAPTER 5's READING: measure the export's thirty-verse chapter 5 against the DB's thirty-three FIRST (the Decalogue's
division), then the reading in the reading shape (section 5). ON THE TABLE, NOT A RULING: the Decalogue-schema sitting (the ten as headers over the
laws; the state doc's #185 addendum 1; the map's tail) — after 2b on the owner's word, its natural seat chapter 5. THE FRAME (the owner, 2026-09-16):
law is code, narrative everything else in a computer program.
""" % (DG[0], DG[1], DP[0], DP[1], pr_line, gates_line)

# ---- THE WRITES (every text built above; the files opened only now) ----
def read(p): return open(f'{ROOT}/{p}', encoding='utf-8').read()
def write(p, s): open(f'{ROOT}/{p}', 'w', encoding='utf-8').write(s)
plans = []
# the map
plans.append(('World/step9/DEUTERONOMY_WALK.md', lambda s: s.rstrip('\n') + '\n' + AS_BUILT))
# COMPILE_DEBT
def f_debt(s):
    assert s.count(DEBT_HDR_OLD) == 1, s.count(DEBT_HDR_OLD); return s.replace(DEBT_HDR_OLD, DEBT_HDR_NEW).rstrip('\n') + '\n' + DEBT_BOX
plans.append(('World/step9/COMPILE_DEBT.md', f_debt))
# MIDDOT
def f_middot(s):
    assert s.count(MIDDOT_ANCHOR) == 1, s.count(MIDDOT_ANCHOR); return s.replace(MIDDOT_ANCHOR, '\n' + MIDDOT_ENTRY + MIDDOT_ANCHOR)
plans.append(('logic/MIDDOT.md', f_middot))
# MISHNAH_TOPICS
def f_topics(s):
    lines = s.split('\n'); done = set()
    for i, l in enumerate(lines):
        for head, note in TOPIC_NOTES.items():
            if l.startswith(head):
                assert head not in done; lines[i] = l.rstrip() + note; done.add(head)
    assert done == set(TOPIC_NOTES), set(TOPIC_NOTES) - done
    return '\n'.join(lines)
plans.append(('logic/MISHNAH_TOPICS.md', f_topics))
# RESEARCH_LOG
plans.append(('RESEARCH_LOG.md', lambda s: s.rstrip('\n') + '\n' + RLOG))
# THE_STEPS
def f_steps(s):
    assert s.count(STEPS_ANCHOR) == 1; return s.replace(STEPS_ANCHOR, STEPS_PARA + STEPS_ANCHOR)
plans.append(('THE_STEPS.md', f_steps))
# THE_BRIEFING
def f_brief(s):
    assert s.count(BRIEF_SB_OLD) == 1 and s.count(BRIEF_BULLET_ANCHOR) == 1 and s.count(BRIEF_ENTRY_ANCHOR) == 1
    s = s.replace(BRIEF_SB_OLD, BRIEF_SB_NEW); s = s.replace(BRIEF_BULLET_ANCHOR, BRIEF_BULLET + BRIEF_BULLET_ANCHOR)
    return s.replace(BRIEF_ENTRY_ANCHOR, BRIEF_ENTRY + BRIEF_ENTRY_ANCHOR)
plans.append(('THE_BRIEFING.md', f_brief))
# THE_LOOP
def f_loop(s):
    assert s.count(LOOP_OLD) == 1; return s.replace(LOOP_OLD, LOOP_NEW)
plans.append(('World/step9/THE_LOOP.md', f_loop))
# RESUME
plans.append(('World/RESUME.md', lambda s: RESUME_HEAD + s))
# the state doc
plans.append(('logic/pre_logic_methods_2026-07-28/PROMPT_continue_solo_era_2026-08-06.md', lambda s: s.rstrip('\n') + '\n' + STATE_ADD))
# the recovery file
plans.append(('logic/pre_logic_methods_2026-07-28/RECOVERY_new_thread_2026-09-12.md', lambda s: s.rstrip('\n') + '\n' + RECOVERY_ADD))
outs = []
for p, f in plans:
    s = read(p); s2 = f(s); assert s2 != s, p; outs.append((p, s2, len(s), len(s2)))
if CHECK:
    for p, s2, a, b in outs: print('WOULD WRITE', p, a, '->', b)
    sys.exit(0)
for p, s2, a, b in outs:
    write(p, s2); print('WROTE', p, a, '->', b)
print('the records written')
