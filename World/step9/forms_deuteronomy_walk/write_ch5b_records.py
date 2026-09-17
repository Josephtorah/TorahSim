import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE DEUTERONOMY WALK sitting 3b — THE COMPILE OF CHAPTER 5 (2026-09-16): THE RECORDS, written after every gate ran — the numbers COMPUTED from the
# gates chain's own prints in the scratchpad (gates_ch5/*.out; never recited); every text built whole before any file is opened; the ledgers appended,
# the map appended, the checklist's boxes marked paid, the recovery page REWRITTEN whole under its cap, the memory index edited under its cap.
# `--check` parses and prints without writing. Sitting 2b's form (write_ch4b_records.py) on the sheet World/step9/RECORD_FORMS.md.
import os, re, sys, subprocess
ROOT = _ROOT
SP = os.path.dirname(os.path.abspath(__file__))
G = f'{SP}/gates_ch5'
MEM = os.path.expanduser('~/.claude/projects/-Users-Shared-TorahSim/memory')
CHECK = '--check' in sys.argv
def rd(name): return open(name if name.startswith('/') else f'{G}/{name}', encoding='utf-8', errors='ignore').read()
def last_frac(name, m):
    t = rd(name); hits = re.findall(r'(\d+)/%d\b' % m, t); assert hits, (name, 'no n/%d' % m); return int(hits[-1])
# ---- THE NUMBERS FROM THE PRINTS ----
summ = rd('SUMMARY.txt'); assert 'GATES CHAIN DONE — ALL GREEN' in summ, summ
tape = rd('tape.out'); assert '10/10 checkpoints' in tape and 'OK   THE REST' in tape
CI = re.findall(r'CHECKPOINT (CI\d) .*? (MATCH|MISS|DIVERGE)$', tape, flags=re.M); assert len(CI) == 9 and all(v == 'MATCH' for _, v in CI), CI
tape_elapsed = re.search(r'elapsed ([\d.]+)s', tape).group(1)
PL = re.search(r"PLACEMENT \(O9 T2\): markers (\{[^}]*\}); events (\{[^}]*\})", tape); assert PL
rg = rd('register.out'); m = re.search(r'DECLARED (\d+); DEBT (\d+); FAILS (\d+)', rg); assert m and 'THE REGISTER GATE: GREEN' in rg
RG = tuple(int(x) for x in m.groups()); assert all(re.search(r'Deut 5:%d +CHAPTER +declared' % v, rg) for v in (12, 16, 32)) and re.search(r'Deut 4:45 +DAEMONS +green .*daemons 2', rg), rg[-1500:]
dg = rd('daemon.out'); m = re.search(r'\((\d+) daemons, (\d+) functions\)', dg); assert m and 'gate satisfied' in dg; DG = tuple(int(x) for x in m.groups())
dp = rd('dependency.out'); m = re.search(r'dispositions on file: (\d+) edges, (\d+) pointers', dp); assert m and 'gate satisfied' in dp; DP = tuple(int(x) for x in m.groups())
LC = re.search(r'LINK CENSUS \(the link review law\): reference (\d+), transfer (\d+), hypothesis (\d+), none (\d+)', dp); assert LC; LC = tuple(int(x) for x in LC.groups())
m = re.search(r'required edges (\d+), required pointers (\d+); live import edges (\d+)', dp); DPR = tuple(int(x) for x in m.groups())
bw = rd('build.out'); assert 'ALL GREEN' in bw, bw[-600:]
jg = rd('journal2.out'); assert 'GATE GREEN' in jg and 'GATE GREEN' in rd('journal.out'); m = re.search(r'(\d+) kinds, (\d+) rows in the index', jg); JG = tuple(int(x) for x in m.groups())
sw = rd('sweep.out'); SW_P = len(re.findall(r'^PASS +cold_run_\w+\.py', sw, flags=re.M)); SW_F = len(re.findall(r'^FAIL +cold_run_\w+\.py', sw, flags=re.M))
SW_CELLS = sum(int(a) for a, b in re.findall(r'score=(\d+)/(\d+)', sw)); assert SW_P + SW_F == 60, (SW_P, SW_F); assert SW_F == 0, 'the sweep has failures — read them first'
po = rd('positions.out'); m = re.search(r'(\d+) checkpoints over (\d+) pauses', po); assert m, po[-800:]; PO = tuple(int(x) for x in m.groups())
PR = {'census': last_frac('probe_census.out', 224), 'installation': last_frac('probe_installation.out', 6), 'readback': last_frac('probe_readback.out', 12),
      'register': last_frac('probe_register.out', 7), 'sequence': last_frac('probe_sequence.out', 4), 'view': last_frac('probe_view.out', 6),
      'population': last_frac('probe_population.out', 9), 'journal': last_frac('probe_journal.out', 7), 'cursor': last_frac('probe_cursor.out', 6),
      'checkpoint': last_frac('checkpoint.out', 7)}
ck = rd('probe_clock.out'); m = re.findall(r'(\d+)/(\d+)', ck); PR['clock'] = ('%s/%s' % m[-1]) if m else 'exit 0'
assert PR['checkpoint'] == 7 and PR['readback'] == 12 and PR['installation'] == 6, PR
run1 = rd(f'{SP}/ch5_run1.out'); assert '49/49' in run1
hp = subprocess.run(['python3', 'logic/solo_tools/scrub_home_paths.py', '--check'], cwd=ROOT, capture_output=True, text=True); assert hp.returncode == 0, hp.stdout[-500:] + hp.stderr[-500:]
NUM = dict(RG=RG, DG=DG, DP=DP, LC=LC, DPR=DPR, JG=JG, SW=(SW_P, SW_CELLS), PO=PO, PR=PR, PL=PL.groups(), tape_elapsed=tape_elapsed)
print('THE NUMBERS:', NUM)
pr_line = ('census %d/224, installation %d/6 (I5 65), readback %d/12, register %d/7, clock %s, sequence %d/4, view %d/6, population %d/9, journal %d/7, cursor %d/6, checkpoint %d/7'
           % (PR['census'], PR['installation'], PR['readback'], PR['register'], PR['clock'], PR['sequence'], PR['view'], PR['population'], PR['journal'], PR['cursor'], PR['checkpoint']))
gates_line = ('the daemon gate GREEN (%d daemons, %d functions); the dependency gate GREEN (%d edges and %d pointers on file — the link census reference %d / transfer %d / hypothesis %d / none %d; required %d edges and %d pointers, live import edges %d); '
              'build_world ALL GREEN (standing 2197, hash 8b8fff1fa28953af unmoved — no freeze this sitting); the journal gate GREEN twice — before and after the sweep (%d kinds, %d rows in the index); THE REGISTER GATE --strict GREEN (DECLARED %d, DEBT %d, FAILS %d — Deut 5:12, 5:16, 5:32 CHAPTER declared, the receipts inside the code run citations of the giving; Deut 4:45 DAEMONS green with daemons 2); '
              'the positions table %d checkpoints over %d pauses (CI1-CI9 in it; checkpoint_probes %d/7 after the rebuild); the sweep %d/60 at %s graded cells; the home-path gate GREEN'
              % (DG[0], DG[1], DP[0], DP[1], LC[0], LC[1], LC[2], LC[3], DPR[0], DPR[1], DPR[2], JG[0], JG[1], RG[0], RG[1], RG[2], PO[0], PO[1], PR['checkpoint'], SW_P, format(SW_CELLS, ',')))

# ---- 1. THE MAP — AS BUILT ----
AS_BUILT = """

## Sitting 3b — THE COMPILE OF CHAPTER 5 — AS BUILT (2026-09-16; the design above stands as written; every departure from it named here)

THE RESULT. Deuteronomy 5:1-33 is COMPILED AND ON THE TAPE: World/step9/cold_run_covenant_at_horeb.py the 60th runner (MATRIX 49/49 on its first
graded run — the fractions moves 34 / data 15; seven cells F1 the_assembly_called … F7 the_answer_and_the_charge with 49 asks; twenty DATA rows; the
readback's twenty-one rows; the guard 49 by the generated CASES; the scene and the narrative tuples matched as predicted on the generator's first
import), law_covenant_at_horeb the 65th daemon (given_at Exodus 20:3 — the second word's first giving; installed_by covenant_blood_thrown; seven
functions WRAPPED; WATCH seen 11 fired 11 on the bench), three kinds and four effects in the registries (1122 kinds, 1023 effects), two lines and two
markers on the tape. THE TAPE 10/10 WITH THE REST ON ITS THIRD RUN (the RUN tuple and THE REST matched on the first): RUN (1302, 96, 88, 0, 12, 1593, 36, 319, the four pairs, 127) exactly as THE
PREDICTION'S ARITHMETIC wrote it; PREVIOUS_RUN 2b's WITH THE ONE DECLARED DELTA reproduced by the tape minus this runner's lines (the daemon's two
blocks at 2b's giving line — writes 1590, daemons fired 36 on THE REST); NEWEST_RUNNER covenant_at_horeb; markers 165 → 167 (forward 128 → 129,
retrograde 22 → 23, proleptic 15); entities 319 UNMOVED, closes 126 → 127 (the charge to teach closed inside the daemon), the population table 148
UNMOVED; PLACEMENT markers %s, events %s — AS PREDICTED (the answer's line inside the stretch reading_placed); CENSUS (2471, 1311, 1302, 1144, 6, 10,
9, 0, 71, 167, 129, 15, 23, 847, 272); CI1-CI9 all MATCH; the run %ss. THE DOCKET logic/oral_triage/deu_05_vaetchanan_exam_2026-09-16.md by the union
rule: 275 rows (link 43 / topic 232; LAW 77, DERIVATION 19, DISPUTE 14, CONTEXT 165; credited 94), the ten Talmud ranges read whole (Shabbat 88a;
Sanhedrin 17a; Makkot 24a; Berakhot 12a; Kiddushin 30b-31b; Sanhedrin 86a; Bava Metzia 5b; Yoma 4b; Sotah 37b; Sanhedrin 60b — the second word's,
added by the design) and three Mishnah rows (Shevuot 3:8-9; Sanhedrin 7:6), seventeen crowns.

THE LAWS' READBACK — THE FIRST FORM ON LAW (L1)-(L6) BUILT: twenty-one reference rows — SIXTEEN on the code (one per verse of 5:6-21, each naming the
runner's cell that compiles the word or NO CELL: VERBATIM 5, VARIANT 5, EXPANDED 3, TURNED 3) and five on the narrative (EXPANDED 2, SUPPLIED 2,
TURNED 1); every row's tape entry FOUND on the running world by kind and first verse (CI4); no row open. THE CODE'S HOLE, found by the measurement and
filled here: the SECOND word (no other gods, no image, no bowing, the jealous God visiting) and the TENTH (covet, desire) had NO CELL in any runner — the
first NO CELL by nature (a declaration), the fifth and the ninth compiled at their kin's seats only (Leviticus 19:3; Exodus 23:1) — so F2 the_second_word
and F5 the_tenth_word compile them from both copies' ink with their answer sheets (Mishnah Sanhedrin 7:6 and Sanhedrin 60b; Bava Metzia 5b), and their
BLOCKS other_gods_barred and coveting_barred are written on Israel AT THE CODE'S OWN LINE — 2b's supplied ten_words_declared, dated (1, 3, 7) (CI3): the
readback's R3 on law — the retelling's cell compiles, the giving's line carries the write; THE REST carries it as its one declared delta (6b's form).
THE TAPE'S SECOND HOLE, found by the measurement and filled here: Exodus 20:18-21 (the people's request for a mediator) has no line on the tape —
20:18 sits in no runner's span, 20:19-26 are the ordinances' law cells — so the request (5:23-27) and the answer told only here (5:28-31; 18:16-17
forward) were written ONCE at their own day by ONE retrograde marker at Deut 5:23 dated (1, 3, 7), a forward marker at 5:32 ending the stretch (CI1,
CI2): torah_through_moses on Israel (Makkot 24a:1 — the first two words from the Almighty's mouth, the rest through Moses), THE CHARGE TO TEACH a DEBIT
on Moses CLOSED AT ONCE BY THE PRIOR RUN (the closer the frame's own line Deut 1:1-5, earlier on the tape — CI6; the opening speech's form reused),
returned_to_tents on Israel (the separation of Exodus 19:15 released — Beitzah 5a-b; CI5). THE RECEIPTS INSIDE THE CODE (5:12, 5:16; 5:32 the plural)
RUN CITATIONS of the giving with the teacher's second referent Marah (Sanhedrin 56b:16; Shabbat 87b:1) — the register seats CHAPTER as the gate's code
predicted (no write's source holds the verses, the chapter holds the closed charge; CI7), the three pointers naming both referents. 5:22's voice and
tablets FOUND (2b's lines, no second write; CI8); 5:27's "we will hear and do" TURNED against 24:7's "do and hear" (Shabbat 88a:7); the frame's two
ends (5:1-5, 5:32-33) NO WRITE (R6).

THE DEPARTURES FROM THE DESIGN, each found by an instrument and each a lesson below: (1) EIGHT older REST checkpoints, not the three the design named,
carried the tape's closes as the literal 126 (CT9, CV2, CV9, CX9, CY9, CZ9, CW9, CR9 — retyped to 126 at 1b, unmoved at 2b): the first tape run's one
miss (9/10 — the RUN tuple and THE REST both matched), read from the print and retyped AS OF this sitting; (2) the fast checkpoint check REFUSED before
the tape ran — the stepper found the journal's base moved at the giving's ordinal (the new daemon writes there): a daemon that writes on an older
runner's line moves the base, so the tape runs first and the fast check follows; (3) THE CLOSER NAMES ONE VERSE — written first as the frame's range
"Deut 1:1-5", it folded the older receipt at 1:3 into a CLOSE (the gate's class by containment: the second run's one miss, CA8's seat Deut 1:3 ACT
computed CLOSE), so the closer names 1:5 alone (the expounding) and the readback's earlier-on-the-tape test finds the closer's line BY CONTAINMENT
(the frame's 1:1-5 holds 1:5; first_verse returns a tuple — CI6 and Q11 retyped); (4) one ink assert fell on the fast checker — Exodus 20:1's tokens are seven, typed eight from memory; (5) the fast checker
strips the callee imports, so a DATA row built from a callee's value (the no-image list by CALL; the honor's measures) is checked by the runner's own
import, not by the fast checker — part 2's two "errors" there were no faults; (6) the receipt's referent is TWO — the ink's (the giving, 20:8 / 20:12)
and the teacher's (Marah): the pointers and the seats name both.

THE GATES, COMPUTED FROM THEIR PRINTS (one chain, gates_chain.sh, one summary): the probe suites %s; %s.

⚠ THE LESSONS OF 3b (nine): (1) THE SHELF'S CITATIONS OF A CHAPTER MAY FOLLOW TWO NUMBERINGS — the export's and one a verse lower around the short
words: THE ROW'S QUOTED WORDS FIX THE VERSE, never the cited number; (2) A DAEMON THAT WRITES ON AN OLDER RUNNER'S LINE moves the journal's base — run
the tape before the fast check, and declare THE REST's delta at the design (the code's hole is filled at the code's own line); (3) EVERY "closes
UNMOVED" LITERAL IS A CURRENT COUNT — one close moves every REST checkpoint since the count was last retyped (eight here), not only the newest three;
grep the literal before the tape; (4) A CLOSER NAMES ONE VERSE — a verse RANGE in a closer reclasses every receipt inside it (the register gate reads
closers by containment); the readback's "earlier on the tape" test finds the closer's line by containment, and first_verse returns a (book, chapter,
verse) tuple; (5) THE FAST CHECKER COVERS THE INK ASSERTS, NOT THE CALLEE-BUILT ROWS — its two errors on a callee's DATA are
by design; (6) A TOKEN COUNT IS TYPED FROM THE PRINT (Exodus 20:1's seven); (7) A RECEIPT HAS TWO REFERENTS when the teacher names an earlier giving —
the pointer names both; (8) THE LAWS' READBACK GRADES ONE ROW PER VERSE OF THE CODE and adds VARIANT (a letter or a conjunction, the sense unchanged)
to the six grades; (9) THE READING SHAPE'S COMPILE HELD ON A CODE CHAPTER: measure (the cells located per word FIRST) → design → probes to fail →
docket → types → recorder and stitcher → gates to fail → runner (49/49 first run) → literals → tape (10/10 on the second run) → one gates chain →
the records from the sheet in one call — the tape's three runs (the closes' literals; the closer's range) each one miss read from the print.

THE DISPOSITIONS ADDED: twelve edges (eleven CALL — decalogue, obey_horeb, erection, exodus_story, opening_speech, holiness, mishpatim_3, sanctions,
refuge, ordinances, pre_sinai; the registration edge sequence → covenant_at_horeb) and three pointers (RUN_CITATION — Deut 5:12, 5:16, 5:32 the
receipts, each naming the giving and Marah); the token census demanded NO further edge (0 uncited); the 2b edge obey_horeb → decalogue's why amended
"PAID at 3b". MOVE_CATALOG CHECKED, unmoved: the runner's 34 move cells are CALLS into the callees and the shelf's own readings (a matter learned from
its context at Sanhedrin 86a:16 the decalogue runner's own; the juxtaposition of 17:3 to 17:5 at Sanhedrin 60b:11 the courts' block's); no new move.

THE FORMS: the sitting's scripts and prints copied into World/step9/forms_deuteronomy_walk/ by copy_ch5b_forms.py (the recon, the callees' print, the
docket's scan and parts, the types, the runner's four parts with the generator, the assembler and the fast checker, the recorder and the stitcher under
their sitting's names, the literals' patcher and the closes' retype, the seats' declaration, the pointers, the design's and the records' writers, the
gates chain's folder — no scratch path and no home path in any copied form).

NEXT on the ruling: the commit on the owner's word; then CHAPTER 6's reading (6:1-25 — the Shema, the words on the heart; the reading shape) — or the
Decalogue-schema sitting first (ON THE TABLE, not a ruling; its exhibits now three: the Sifrei 233:1, remember-and-keep in one utterance, the ten as
one reading abolished for the heretics' grievance). Nothing committed: the tree uncommitted since 834602b, on the owner's word only.
""" % (PL.group(1), PL.group(2), tape_elapsed, pr_line, gates_line)

# ---- 2. COMPILE_DEBT — the sitting-3 box marked PAID + the 3b box; the 2b box's second word PAID ----
DEBT_HDR_OLD = "## 38 sources; one unit deu_05_decalogue FROZEN, the 219th) — OWED TO THE COMPILE (sitting 3b): (a) THE LAWS' READBACK"
DEBT_HDR_NEW = "## 38 sources; one unit deu_05_decalogue FROZEN, the 219th) — PAID AT 3b (the 3b box below, item by item) — AS WRITTEN AT THE READING, OWED TO THE COMPILE (sitting 3b): (a) THE LAWS' READBACK"
DEBT_2B_OLD = "## name (the reading shelf's). OWED FROM 2b: (i) THE SECOND WORD — Exodus 20:3-6 (the image law) has NO CELL in any runner;"
DEBT_2B_NEW = "## name (the reading shelf's). OWED FROM 2b: (i) THE SECOND WORD — PAID AT 3b (cold_run_covenant_at_horeb.py F2 the_second_word, 2026-09-16; the block other_gods_barred at the giving's line) — AS WRITTEN AT 2b: Exodus 20:3-6 (the image law) has NO CELL in any runner;"
DEBT_BOX = """
## DEUTERONOMY SITTING 3b — THE COMPILE OF CHAPTER 5 (2026-09-16; DEUTERONOMY_WALK.md "Sitting 3b" design + AS BUILT; logic/oral_triage/deu_05_vaetchanan_exam_2026-09-16.md
## 275 rows; cold_run_covenant_at_horeb.py 49/49; law_covenant_at_horeb the 65th daemon; the tape 10/10 with RUN (1302, 96, 88, 0, 12, 1593, 36, 319, pairs, 127)). THE SITTING-3
## BOX (a)-(k) PAID — (a) THE LAWS' READBACK built: sixteen rows on the code (one per verse of 5:6-21) graded VERBATIM 5 / VARIANT 5 / EXPANDED 3 / TURNED 3, each naming
## the cell that compiles the word or NO CELL (5:6 alone), five narrative rows; (b) THE SECOND WORD compiled — F2 the_second_word from both copies (Mishnah Sanhedrin 7:6;
## Sanhedrin 60b), its block other_gods_barred on Israel written at the giving's line (1, 3, 7); AND THE TENTH WORD, found without a cell by the same measurement — F5
## the_tenth_word (Bava Metzia 5b), coveting_barred at the giving's line; (c) THE RECEIPTS' SEATS Deut 5:12, 5:16, 5:32 declared CHAPTER (the gate's code: no write holds
## the verses, the chapter holds the closed charge), the pointers RUN_CITATION naming the giving and the teacher's Marah (Sanhedrin 56b); (d) the ketiv a DATA note; (e) the
## sabbath's two grounds a DATA row (the creation by the pre-Sinai runner's call); (f) the vain witness a DATA row (ordinances.courts by call; 19:16-21 forward); (g) the
## voice and the tablets FOUND, no second write; (h) the request and the answer TWO SUPPLIED lines dated (1, 3, 7) by the retrograde marker at 5:23 — THE TAPE'S SECOND
## HOLE (Exodus 20:18-21) filled; "hear and do" TURNED against 24:7; "they have done well" a DATA note (18:17 forward); (i) the block's edge — chapter 5 installs ONE
## daemon (the second and tenth words'; given_at Exodus 20:3, outside 4:45's block), no footer, the charge no write; (j) the docket by the union rule — 275 rows, the
## second word's answer sheet added; (k) the schema sitting stays ON THE TABLE. OWED FROM 3b: (i) THE IDOLATER'S PROCEDURE — Deuteronomy 17:2-7 (the stoning by the
## juxtaposition, Sanhedrin 60b:11) compiles at chapter 17's sitting; the second word's cell cites it by reference; (ii) THE CONSPIRING WITNESSES — 19:16-21 the ninth
## word's own procedure, chapter 19's sitting; (iii) THE PROPHET'S PROMISE — 18:15-19 cites 5:28's "they have done well" forward, chapter 18's; (iv) THE D2 CANDIDATE —
## law_decalogue's and law_covenant_at_horeb's installed_by (covenant_blood_thrown) may turn to ten_words_declared, a loop sitting's decision; (v) THE VISITING CLAUSE —
## the third and fourth generation's arms (Berakhot 7a; Makkot 24a:30 revoked by Ezekiel) recorded as DATA, no cell of its own; (vi) THE SEPARATION'S RELEASE — the
## tape's people_sanctified timer stands as fired; returned_to_tents a status beside it, no close (the timer's entry is not a debit); (vii) the Mekhilta on Exodus 20
## (Bahodesh 7-8 — one utterance, covet and desire) named, unopened — the first copy's spine, a reading sitting's if the schema sitting opens. NOTHING ELSE IN
## CHAPTER 5 IS OWED TO A LATER SITTING OF ITS OWN.
"""

# ---- 3. MIDDOT — the docket entry ----
MIDDOT_ANCHOR = "\n## Exodus block campaign — owner's word \"Do 3\")\n"
MIDDOT_ENTRY = """- THE CHAPTER-5 DOCKET (THE DEUTERONOMY WALK sitting 3b, 2026-09-16; logic/oral_triage/deu_05_vaetchanan_exam_2026-09-16.md — 275 rows; the rules
  about rules the docket carries, each at its row):
  · ONE UTTERANCE SAYS TWO WORDS (Shevuot 20b:9; Rosh Hashanah 27a:2, 27a:6; Berakhot 20b:10 on Deuteronomy 5:12 and Exodus 20:8): "remember" and
    "keep" spoken at once — what the mouth cannot say nor the ear hear; the vain and the false oath "one" by the same rule; whoever is in "keep" is in
    "remember" (women's kiddush) — the diff's first word read as a rule about the giving: the DATA row keep_and_remember; the readback row 5:12.
  · THE EXPANSION READ AS A TEACHING (Bava Kamma 54b:13 on 5:14; Bava Kamma 55a:1 on 5:16): the second copy's "your ox and your ass" inside "all your
    cattle" teaches every animal wherever the pair is written; "that it may go well with you" absent from the first tablets because they were to be
    broken — the readback's EXPANDED rows carry the tradition's own reading of the expansion.
  · THE RECEIPT READ AS MARAH (Sanhedrin 56b:16; Shabbat 87b:1 on 5:12, 5:16): "as the LORD your God commanded you" = at Marah (Exodus 15:25) — a
    receipt's referent taught earlier than its plain one; the pointers name both.
  · A MATTER LEARNED FROM ITS CONTEXT (Sanhedrin 86a:16-17 on 5:19 / Exodus 20:15 and Leviticus 19:11): "you shall not steal" among capital words
    speaks of persons; among property words of property — the decalogue runner's own move at its Talmud seat, the readback row 5:19.
  · THE TEMPLE'S RITES EMPTIED TO THE NAME (Sanhedrin 60b:8-15 on Exodus 22:19; 60b:11 on Deuteronomy 17:3-5): slaughter, incense, libation — the
    Temple's services — capital for an idol even not in its way; bowing by the juxtaposition of "bowed" to "stone them"; the hugger and the kisser a
    prohibition without death: the second word's cell F2, the DATA row the_second_word.
  · COVETING EVEN WITH PAYMENT (Bava Metzia 5b:19-20 on 5:21 / Exodus 20:17): taking by force or deceit violates the tenth word though the taker pays;
    the people read it as without payment, so the payer's oath stands — the tenth word's cell F5, the exam's person the coveter who pays.
  · THE FIRST TWO WORDS FROM THE ALMIGHTY'S MOUTH (Makkot 24a:1 on 5:6-7 and 5:27): 611 through Moses and two direct — the request for a mediator
    read as the code's own division: the status torah_through_moses, the DATA row the_mediator.
  · "WE WILL DO" BEFORE "WE WILL HEAR" (Shabbat 88a:5-9 on 5:27 against Exodus 24:7): the order a crown, the mountain a tub over them — the TURNED row.
  · A COUNT NEEDS A COUNT TO PERMIT (Beitzah 5a:7-5b:3; Sanhedrin 59b:4 on 5:30): "return to your tents" said though the three days had passed —
    the status returned_to_tents, the separation of Exodus 19:15 released by a word.
  · THE HONOR AND THE FEAR DEFINED (Kiddushin 30b:16-31b:14 on 5:16 with Leviticus 19:3): the six services and the three abstentions; the three
    equations; the father first in "honor", the mother first in "fear" — the fifth word compiled at its kin's seat by CALL.
  · THE SECOND COPY A THIRD SAYING (Sotah 37b:3 on the ten words; Tosefta Sotah 8:11): R. Akiva — generals and details at Sinai, at the Tent, at Moab;
    R. Yishmael — the generals at Sinai only: the readback's own status on the shelf, a DATA setting.
  · THE TEN AS ONE READING, ABOLISHED (Berakhot 12a:4-8; Kiddushin 31a:6-7): read daily in the Temple, sought outside and abolished for the heretics'
    grievance; the nations conceded the first words when the fifth was said — the schema question's exhibits, no rule.
"""

# ---- 4. MISHNAH_TOPICS — the rows touched ----
W3 = "THE DEUTERONOMY WALK sitting 3b"
TOPIC_NOTES = {
 "**1. Mishnah, Blessings**": " — 2:? READ: Berakhot 12a whole and 20b:10 READ 2026-09-16 (%s: the ten words read daily in the Temple and abolished outside; women's kiddush from 'keep' and 'remember', Deuteronomy 5:12; deu_05_vaetchanan_exam_2026-09-16.md)" % W3,
 "**12. Mishnah, Sabbath**": " — 9:3's gemara Shabbat 88a READ, 33b:8 and 87a:4-87b:1 CREDITED 2026-09-16 (%s: 'we will do' before 'we will hear' against 5:27; the Sabbath commanded at Marah, 5:12)" % W3,
 "**16. Mishnah, Day of Atonement**": " — 1:1's gemara Yoma 4b READ 2026-09-16 (%s: the sixth or the seventh of Sivan; all Israel heard the voice, 5:4)" % W3,
 "**18. Mishnah, Festival Day**": " — 1:1's gemara Beitzah 5a:7-5b:3 CREDITED 2026-09-16 (%s: 'return to your tents', 5:30 — a count needs a count to permit)" % W3,
 "**21. Mishnah, Scroll of Esther**": " — 4:1's gemara Megillah 21a:14 READ 2026-09-16 (%s: the Torah read standing from 'stand here with me', 5:31)" % W3,
 "**24. Mishnah, Levirate Marriage**": " — 48b:5-6, 62a:2, 109b:5 READ 2026-09-16 (%s: the servant's rest and the stranger's two kinds, 5:14; Moses' separation; 'learn and do', 5:1)" % W3,
 "**28. Mishnah, Suspected Wife**": " — 7:5's gemara Sotah 37b READ, 10b:12 CREDITED 2026-09-16 (%s: the covenants counted; the second copy a third saying (R. Akiva); 'did not cease', 5:22)" % W3,
 "**30. Mishnah, Betrothal**": " — 1:7's gemara Kiddushin 30b-31b READ WHOLE, 39b-40a READ 2026-09-16 (%s: the honor and the fear defined — the fifth word, 5:16; the reward clause)" % W3,
 "**31. Mishnah, First Gate**": " — 5:? gemara Bava Kamma 54b:9-28, 55a:1, 67b:6 READ 2026-09-16 (%s: the ox and the ass every animal, 5:14; 'good' not in the first tablets, 5:16)" % W3,
 "**32. Mishnah, Middle Gate**": " — 1:1's gemara Bava Metzia 5b READ WHOLE, 89a:1 READ 2026-09-16 (%s: the coveter who pays, 5:21 — the tenth word's answer sheet)" % W3,
 "**33. Mishnah, Last Gate**": " — 110a:3 CREDITED 2026-09-16 (%s: 'stand HERE with me', 5:31 in Micah's house)" % W3,
 "**34. Mishnah, Courts**": " — 7:6 READ with its gemara Sanhedrin 60b WHOLE (the four services, the bower's stoning by 17:3-5); 1:6's gemara 17a and 11:1's gemara 86a READ WHOLE; 56b:16, 59b:3-4 CREDITED 2026-09-16 (%s: the second word's answer sheet; the theft of persons by the context, 5:19; the receipts at Marah)" % W3,
 "**35. Mishnah, Lashes**": " — 3:16's gemara Makkot 24a READ WHOLE 2026-09-16 (%s: the first two words from the Almighty's mouth, 5:6-7; the visiting revoked by Ezekiel, 5:9)" % W3,
 "**36. Mishnah, Oaths**": " — 3:8-9 READ with 20b:9 CREDITED 2026-09-16 (%s: the vain oath defined — the third word, 5:11; vain and false in one utterance like remember and keep)" % W3,
 "**38. Mishnah, Idolatry**": " — 1:1's gemara Avodah Zarah 4b:17-5a:21 READ 2026-09-16 (%s: 'who would give that they had such a heart', 5:29 — the calf and the penitents)" % W3,
 "**43. Mishnah, Slaughter**": " — 110b:3, 142a:3-9 READ 2026-09-16 (%s: a mitzva whose reward is stated beside it — 'that it may go well with you', 5:16)" % W3,
}

# ---- 5. RESEARCH_LOG ----
RLOG = """

## 2026-09-16 — DEUTERONOMY 5 COMPILED (THE DEUTERONOMY WALK sitting 3b — CHAPTER 5): THE LAWS' READBACK — CODE AGAINST CODE; THE CODE'S HOLE — TWO
## WORDS NO RUNNER COMPILED; THE TAPE'S SECOND HOLE — THE REQUEST FOR A MEDIATOR; THE RECEIPT'S TWO REFERENTS; THE SHELF'S TWO NUMBERINGS; A CLOSE
## MOVES EVERY OLD COUNT

THE LAWS' READBACK. The readback's first form (1b, 2b) graded Moses' retelling of ACTS against the tape. Chapter 5 retells the CODE — the ten words
said again — so the form was applied to law: one reference row per verse of the second copy (5:6-21), each graded against the runner's cell that
compiles the word and NAMING that cell. The grades: VERBATIM five (5:6, 7, 11, 13, 17), VARIANT five (a letter or a conjunction moved, the sense
unchanged — 5:8, 9, 10, 18, 19; the grade the code's copy adds), EXPANDED three (5:12 keep for remember with the receipt; 5:14 the beasts and the
servants' rest; 5:16 the receipt and "that it may go well"), TURNED three (5:15 the exodus for the creation; 5:20 vain for false; 5:21 the wife first
and desire for covet). The tradition itself reads the expansions as teachings: the ox and the ass inside "all cattle" teach every animal wherever the
pair is written (Bava Kamma 54b:13); "good" is absent from the first tablets because they were to be broken (Bava Kamma 55a); keep and remember were
one utterance (Shevuot 20b, Rosh Hashanah 27a). The deltas recomputed from the DB: 172 tokens / 620 letters against 189 / 708.

THE CODE'S HOLE. Locating each word's cell first — a regex over every runner's ink references, per def — found that the SECOND word (no other gods,
no image, no bowing, the jealous God) and the TENTH (covet, desire) had NO CELL in any runner: the first word none by nature (a declaration), the fifth
and the ninth compiled at their kin's seats only (Leviticus 19:3; Exodus 23:1), six at the Decalogue's or the ordinances'. The retelling's seat
compiled both from both copies' ink with their answer sheets — Mishnah Sanhedrin 7:6 with Sanhedrin 60b (the idolater stoned for worship in its way
and for the Temple's four rites even not in its way; the bower by the juxtaposition of 17:3 to 17:5; the hugger a prohibition without death) and Bava
Metzia 5b (coveting even with payment) — and wrote their BLOCKS on Israel AT THE CODE'S OWN LINE: the daemon watches 2b's supplied ten_words_declared,
dated (1, 3, 7), and writes other_gods_barred and coveting_barred there, never at the retelling's. The readback's R3 on law. THE REST test carried it
as a declared delta (6b's form): the tape minus this runner's lines still has the daemon firing on the giving's line.

THE TAPE'S SECOND HOLE. The same measurement found no line on the tape for Exodus 20:18-21 — the people's request for a mediator: 20:18 sits in NO
runner's span (the decalogue's ends at 20:17, the ordinances' begins at 20:19) and 20:19-26 are law cells. Chapter 5 tells the request (5:23-27) and
an answer told nowhere else (5:28-31 — "they have done well … return to your tents … stand here with me"; 18:16-17 cites it forward). Both written
once at their own day by one retrograde marker at 5:23 dated (1, 3, 7), a forward marker at 5:32 ending the stretch (2b's lesson 1). The answer writes
two: THE CHARGE TO TEACH a debit on Moses closed at once by the prior run — the book's own opening (1:1-5) is its run, so the closer is the frame's
line, earlier on the tape (the opening speech's form) — and "return to your tents" a status on Israel, the separation of Exodus 19:15 released by an
explicit word (Beitzah 5a-b: a matter forbidden by a count needs a count to permit). The request writes torah_through_moses: Makkot 24a:1 — the first
two words from the Almighty's mouth, the rest through Moses. Closes 126 → 127. The closer's text taught one more rule: written first as the frame's
range "Deut 1:1-5", it reclassed the older receipt at 1:3 as CLOSE — the register gate reads a closer by containment — so a closer names one verse.

THE RECEIPT'S TWO REFERENTS. "As the LORD your God commanded you" inside the fourth and fifth words (5:12, 5:16) and closing the chapter (5:32) is a
law citing its prior giving — the ink's referent the ten words' line on the tape. The docket added the teacher's: Rav Yehuda reads the receipt as
MARAH (Sanhedrin 56b:16; Shabbat 87b:1 — the Sabbath and honoring parents among Exodus 15:25's statutes). The register seats declared CHAPTER as the
gate's code predicted (no write's source holds the verses — the second copy is no line; the chapter holds the closed charge), and the three pointers
name both referents.

THE SHELF'S TWO NUMBERINGS. The scan of the shelf's English for "Deuteronomy 5:n" found the citations follow TWO divisions — the export's thirty
verses (17 = the four short words) and one a verse lower around them: Sanhedrin 17a:12 cites 5:19 and Sotah 10b:12 cites 5:18 for the same "did not
cease" (the DB's 22); Avodah Zarah 5a:8 cites 5:26 for "with their children forever" (the DB's 29) and Beitzah 5a:7 cites 5:26 for "return to your
tents" (the DB's 30). The rule: the row's quoted words fix the DB verse; every docket verdict names the verse by the quote.

A CLOSE MOVES EVERY OLD COUNT. The first tape run reached 9/10 — the RUN tuple and THE REST both as predicted — with one miss: eight older REST
checkpoints (CT9, CV2, CV9, CX9, CY9, CZ9, CW9, CR9) hold the tape's closes as a literal 126, retyped to that at 1b and unmoved since; the design had
named only the newest three. Retyped to 127 as of this sitting; 10/10 on the second run. Beside it the fast checkpoint check refused before the tape
ran — the journal's base had moved at the giving's ordinal, where the new daemon now writes — so a daemon that writes on an older line means the tape
runs first and the fast check follows.
"""

# ---- 6. THE_STEPS ----
STEPS_ANCHOR = "\n## Step 6 — Publish\n"
STEPS_PARA = """
DEUTERONOMY — SITTING 3b — CHAPTER 5 COMPILED (2026-09-16, on Brian's "go"; World/step9/DEUTERONOMY_WALK.md "Sitting 3b" and "Sitting 3b — AS
BUILT"). This was the readback's other half, the one the loop's sixth step had owed since Numbers: not a retold act graded against the tape, but the
code itself said again — the ten words in Moses' mouth graded against the code as it was compiled. Before the design, every word was traced to the
cell that compiles it, and two had none anywhere: the second word (no other gods, no image, no bowing) and the tenth (covet). Both were compiled here
from both copies of the ink with the Talmud's own answer sheets, and their blocks were written on the ledger at the day the words were first spoken,
not at the day they were repeated — the rule the earlier sittings built for acts now holding for law. Sixteen rows on the code, graded exactly (five
the same letter for letter; five a letter or a conjunction apart; three grown by a clause; three with a ground or a term replaced), and the tradition
turned out to read the very differences as teachings. The measurement also found a second hole in the tape: the people's request for a mediator at
Horeb had never been written, and the answer to it is told only here — both written once at the giving's day, the charge to teach closed by the
book's own opening. The receipt "as the LORD your God commanded you", written inside two of the words, was read two ways — the ink's (the giving) and
the teacher's (Marah) — and the register seats now say so. The shelf's citations of this chapter turned out to follow two numberings, so every docket
row was pinned by its quoted words. The runner reproduced the answer sheet on its first run; the tape reached ten of ten on its third, the misses
being eight old counts of closes that one new close moved, and a closer written as a range that swept an older receipt into its close; every probe
suite and every gate green in one chain, the sweep whole. Next: the commit on
your word; then chapter 6's reading — or the schema sitting first, on your word.
"""

# ---- 7. THE_BRIEFING ----
BRIEF_BULLET_ANCHOR = "- **CHAPTER 5 READ AND FROZEN — THE TEN WORDS SAID AGAIN"
BRIEF_BULLET = ("- **CHAPTER 5 COMPILED — THE CODE SAID AGAIN AND GRADED AGAINST THE CODE: SIXTEEN ROWS OF THE TEN WORDS, EACH NAMING THE CELL THAT COMPILES IT; TWO WORDS HAD NO CELL ANYWHERE — THE SECOND AND THE TENTH — COMPILED HERE AND WRITTEN AT THE DAY THEY WERE FIRST SPOKEN; A SECOND HOLE IN THE TAPE, THE REQUEST FOR A MEDIATOR, FILLED; THE RECEIPT READ TWO WAYS** "
                "(2026-09-16, on your \"go\"; World/step9/DEUTERONOMY_WALK.md \"Sitting 3b\" + AS BUILT): cold_run_covenant_at_horeb.py the 60th runner (49/49), law_covenant_at_horeb the 65th daemon; the readback's twenty-one rows; the tape 10/10 with RUN (1302, 96, 88, 0, 12, 1593, 36, 319, pairs, 127) as predicted, markers 167; every gate GREEN, the sweep %d/60. NEXT: the commit on your word; chapter 6's reading, or the schema sitting first.\n" % SW_P)
BRIEF_ENTRY_ANCHOR = "### 2026-09-16 — CHAPTER 5 READ: THE TEN WORDS SAID AGAIN, AND THE DIFFERENCES ARE THE FINDS\n"
BRIEF_ENTRY = """### 2026-09-16 — CHAPTER 5 COMPILED: THE CODE GRADED AGAINST THE CODE, AND TWO WORDS FOUND UNCOMPILED

The readback built at the first three chapters graded Moses' retelling of what happened against the tape of what happened. Chapter 5 is different:
Moses says the ten words again, so what gets graded is the code against the code. Before any design, every one of the ten was traced to the place in
the machine that compiles it — and two had no such place anywhere. The second word (no other gods, no image, no bowing) and the tenth (you shall not
covet) had been read and discussed for weeks but never turned into a cell. Both were compiled in this sitting from the two copies of the ink, with
the Talmud's answer sheets for each — who is stoned for idolatry and who merely transgresses; whether coveting is coveting when the taker pays — and,
by the rule the walk built for acts, their entries were written on the ledger at the day the words were first spoken at Horeb, not at the day Moses
repeated them. The sixteen verses of the code were graded one by one: five identical, five a letter or a conjunction apart, three grown by a clause,
three with a ground or a word replaced — and the tradition, it turned out, reads those very differences as teachings (the ox and the ass teach "every
animal"; "that it may go well with you" was left out of the first tablets because they were going to be broken). The measurement found a second hole
in the tape too: the people's plea at Horeb for Moses to stand between them and the voice had never been written, and God's answer to it — "they
have done well … return to your tents … you stand here with me" — is told nowhere but here. Both were written once at the giving's day; the charge
to teach was closed by the book's own opening, which is its fulfilment. The little receipt inside two of the words, "as the LORD your God commanded
you", was read both ways the tradition reads it — the giving, and the earlier statutes at Marah. One thing the shelf did that we had not seen: its
citations of this chapter follow two different verse numberings, so every row of the docket was pinned by the words it quotes, not by the number it
cites. The runner matched its answer sheet on the first run; the tape reached ten of ten on the third — eight old counts that a single new close had
moved, then a closer written as a range of verses that quietly re-filed an older receipt, both read off the print and corrected. Every gate is green in one chain. Next, on your word: the commit, then chapter 6 — or the schema question first.

"""

# ---- 8. THE_LOOP step-6 row ----
LOOP_OLD = "readback_probes 9/9, CC4-CC6) | the laws' half a sitting when chapter 5 opens |"
LOOP_NEW = ("readback_probes 9/9, CC4-CC6); cold_run_covenant_at_horeb.py (chapter 5, THE LAWS' HALF BUILT 2026-09-16 — sixteen rows on the code graded VERBATIM / VARIANT / EXPANDED / TURNED, each naming the cell that compiles the word; "
            "the second and the tenth words compiled at the retelling's seat and written at the giving's line; the tape's second hole (Exodus 20:18-21) filled — the request and the answer supplied, the charge to teach closed by the prior run; readback_probes 12/12, CI4-CI6) | the laws' half BUILT at chapter 5 (3b); the second pass after Deuteronomy |")

# ---- 9. RESUME ----
RESUME_HEAD = """# ⚠ THE DEUTERONOMY WALK sitting 3b (2026-09-16; step9/DEUTERONOMY_WALK.md "Sitting 3b" + "Sitting 3b — AS BUILT"): CHAPTER 5 COMPILED —
# step9/cold_run_covenant_at_horeb.py the 60th runner (49/49; seven cells; the readback's twenty-one rows — sixteen on the code, code against code),
# law_covenant_at_horeb the 65th daemon (given_at Exod 20:3); THE CODE'S HOLE filled: the second and the tenth words had no cell anywhere — compiled
# here, their blocks written at the giving's line (1, 3, 7); THE TAPE'S SECOND HOLE filled: the request for a mediator (Exodus 20:18-21) and the
# answer told only here, written once at (1, 3, 7) by a retrograde marker at 5:23, the charge to teach closed by the prior run; the receipts 5:12,
# 5:16, 5:32 CHAPTER (the giving and Marah); the tape 10/10 with RUN (1302, 96, 88, 0, 12, 1593, 36, 319, pairs, 127) as predicted, markers 167,
# closes 127; every probe suite and gate GREEN, the sweep %d/60.
# NEXT on the ruling: the commit on the owner's word; chapter 6's reading (6:1-25) — or the schema sitting first, on his word.
""" % SW_P

# ---- 10. THE STATE DOC — #188 ADDENDUM 2 ----
STATE_ADD = """
#188 ADDENDUM 2 (2026-09-16, at the close of THE DEUTERONOMY WALK sitting 3b — THE COMPILE OF CHAPTER 5 — A CLEAN COMPACTION POINT): THE SITTING RAN
END TO END in the compile shape on the owner's "go" (the rereads → the measurements → the design → the probes to fail → the docket → the types → the
recorder and the stitcher → the gates to fail → the runner → the literals → the tape → one gates chain → the records from the sheet in one call); the
map's "Sitting 3b — AS BUILT" is the record (the departures, the three tape runs, the nine lessons, the gates computed from their prints). THE STATE:
cold_run_covenant_at_horeb.py the 60th runner (49/49), law_covenant_at_horeb the 65th daemon (%d daemons, %d functions), the registries 1122 kinds /
1023 effects, the tape 10/10 with RUN (1302, 96, 88, 0, 12, 1593, 36, 319, the four pairs, 127) and markers 167 (F 129 / P 15 / R 23), entities 319,
closes 127, the population table 148; the docket logic/oral_triage/deu_05_vaetchanan_exam_2026-09-16.md (275 rows); THE LAWS' READBACK BUILT — the
readback's twenty-one rows (sixteen on the code: VERBATIM 5, VARIANT 5, EXPANDED 3, TURNED 3; five narrative: EXPANDED 2, SUPPLIED 2, TURNED 1) with
THE CODE'S HOLE filled (the second and the tenth words compiled, their blocks at the giving's line) and THE TAPE'S SECOND HOLE filled (the request and
the answer at (1, 3, 7) by the marker at Deut 5:23, the forward marker at 5:32); the receipts 5:12, 5:16, 5:32 CHAPTER; the corpus unmoved (219 units,
standing 2197, hash 8b8fff1fa28953af — no freeze this sitting). THE GATES: the probe suites %s; %s. THE RECORDS written: the map's AS BUILT,
COMPILE_DEBT (the sitting-3 box PAID; the 2b box's second word PAID; the 3b box with seven owed items), MIDDOT's docket entry (twelve rules about rules),
MISHNAH_TOPICS (sixteen rows), RESEARCH_LOG, THE_STEPS, THE_BRIEFING (the bullet and the entry), THE_LOOP's step-6 row (the laws' half BUILT),
World/RESUME.md, the recovery page rewritten, the addenda's section 37, memory (deuteronomy-walk.md, MEMORY.md under 17,000 bytes); the forms copied by
copy_ch5b_forms.py. NOT COMMITTED (the tree uncommitted since 834602b — the owner's word only; NOT PUSHED). NEXT ON THE RULING: the commit on the
owner's word; then CHAPTER 6's reading (6:1-25 — the Shema; the reading shape on sitting 3's forms) — or the Decalogue-schema sitting first (ON THE
TABLE, not a ruling; its exhibits three: the Sifrei 233:1, remember-and-keep in one utterance, the ten as one reading). IF THIS COMPACTS HERE: reread the
recovery page, the map's "Sitting 3b — AS BUILT" and MEMORY.md; nothing is mid-flight.
""" % (DG[0], DG[1], pr_line, gates_line)

# ---- 11. THE RECOVERY ADDENDA — section 37 ----
ADDENDA_ADD = """

## 37. ADDENDUM (2026-09-16, THE DEUTERONOMY WALK sitting 3b — THE COMPILE OF CHAPTER 5, Deuteronomy 5:1-33 COMPILED AND ON THE TAPE; the owner: "go"; the state doc's #188 addendum 2)

THE SITTING RAN IN THE COMPILE SHAPE (section 5; "Sitting 2b" the form): World/step9/DEUTERONOMY_WALK.md "Sitting 3b" (the design, written before any
code) and "Sitting 3b — AS BUILT" (the departures and the lessons). THE STATE: cold_run_covenant_at_horeb.py the 60th runner (49/49 — seven cells,
twenty DATA rows, the readback's twenty-one rows), law_covenant_at_horeb the 65th daemon (given_at Exod 20:3, installed_by covenant_blood_thrown; %d
daemons, %d functions), event_vocabulary +3 (1122), effect_vocabulary +4 (1023), dependency_dispositions +12 edges +3 pointers (%d edges, %d pointers on
file), register_dispositions Deut 5:12 / 5:16 / 5:32 CHAPTER; THE TAPE 10/10 WITH THE REST — RUN (1302, 96, 88, 0, 12, 1593, 36, 319, the four pairs,
127) as predicted, PREVIOUS_RUN 2b's with ONE DECLARED DELTA (the daemon's two blocks on THE REST), NEWEST_RUNNER covenant_at_horeb, markers 167 (F 129 /
P 15 / R 23), entities 319, closes 127, the population table 148, CI1-CI9 MATCH; the docket logic/oral_triage/deu_05_vaetchanan_exam_2026-09-16.md (275
rows — link 43 / topic 232; LAW 77; credited 94; the ten ranges whole). THE GATES: the probe suites %s; %s.

WHAT THE SITTING FOUND (RESEARCH_LOG 2026-09-16, the compile entry): THE LAWS' READBACK — sixteen rows on the code, each naming its cell, VARIANT the
grade the code's copy adds; THE CODE'S HOLE — the second and the tenth words had NO CELL in any runner: compiled here from both copies, their blocks
written at the giving's line (1, 3, 7), THE REST's one declared delta; THE TAPE'S SECOND HOLE — Exodus 20:18-21 (the request for a mediator) has no line:
the request and the answer (told only here) written once at (1, 3, 7) by the retrograde marker at Deut 5:23, the forward marker at 5:32; THE CHARGE TO
TEACH a debit on Moses closed by the prior run (the frame's line 1:1-5 the closer); THE RECEIPT'S TWO REFERENTS (the giving; Marah — Sanhedrin 56b) at
the seats and the pointers; THE SHELF'S TWO NUMBERINGS — the quoted words fix the verse; A CLOSE MOVES EVERY OLD COUNT — eight REST literals retyped.
THE NINE LESSONS in the map's AS BUILT.

THE FILES CHANGED BY 3b: World/step9/cold_run_covenant_at_horeb.py (new), cold_run_sequence.py (the tape section, the literals, CI1-CI9, the retypes
CP6 / CA1 / CA9 / CC8 / CC9 and the eight closes literals), event_vocabulary.yaml, effect_vocabulary.yaml, daemon_dispositions.yaml,
dependency_dispositions.yaml (the span, twelve edges, three pointers; the 2b OWED why amended PAID), register_dispositions.yaml, readback_probes.py
(Q10-Q12), installation_probes.py (I5 65), checkpoint_positions.yaml (rebuilt), the docket (new), the forms folder (copy_ch5b_forms.py), the records
(the map, COMPILE_DEBT, MIDDOT, MISHNAH_TOPICS, RESEARCH_LOG, THE_STEPS, THE_BRIEFING, THE_LOOP, RESUME, the recovery page, this file, the state doc,
memory). NOT COMMITTED — the tree uncommitted since 834602b; commit on the owner's word only.

NEXT ON THE RULING: the commit on the owner's word; then CHAPTER 6's READING (6:1-25 — the Shema, the words on the heart, the reading shape on sitting 3's
forms). ON THE TABLE, NOT A RULING: the Decalogue-schema sitting (the ten as headers over the laws; its seat chapter 5 — the exhibits the Sifrei 233:1,
remember-and-keep in one utterance, the ten as one reading) — on the owner's word.
""" % (DG[0], DG[1], DP[0], DP[1], pr_line, gates_line)

# ---- 12. THE RECOVERY PAGE — rewritten whole under its cap (section 2 replaced, sections 5 and 6 retouched) ----
def f_recovery(s):
    i = s.index('## 2. WHERE IT STANDS'); j = s.index('## 3. THE STANDING LAWS')
    sec2 = """## 2. WHERE IT STANDS (2026-09-16, after sitting 3b — chapter 5's compile; the state doc #188 addendum 2)
- NUMBERS CLOSED. DEUTERONOMY 1:1-5:33 READ, FROZEN, COMPILED AND ON THE TAPE (sittings 1-3b).
- 219 frozen units, standing 2197, hash 8b8fff1fa28953af. 60 runners, 65 daemons, %d functions; registries 1122 kinds / 1023 effects.
- THE TAPE at RUN (1302, 96, 88, 0, 12, 1593, 36, 319, the four pairs, 127), markers 167, closes 127, the counter (40, 11, 1); the sweep %d/60;
  every gate GREEN; the register gate DECLARED %d / DEBT 0 (5:12, 5:16, 5:32 CHAPTER).
- THE LAWS' READBACK BUILT (THE_LOOP step 6's other half): the ten words graded code against code; the second and the tenth words compiled at 3b.
- LAST COMMIT 834602b (NOT pushed). Uncommitted: sittings 3 and 3b; the schema tutorial, its epub and the builder (ARCHITECTURE/).
- ON THE TABLE, NOT A RULING: the Decalogue as a SCHEMA (seat chapter 5; the exhibits the Sifrei 233:1, one utterance, the ten as one reading).
- NEXT ON HIS WORD: the commit; then CHAPTER 6's reading (6:1-25, the Shema) — or the schema sitting first.

""" % (DG[1], SW_P, RG[0])
    s = s[:i] + sec2 + s[j:]
    old5 = 'the newest instances: the map\'s "Sitting 2" and "Sitting 2b")'; assert s.count(old5) == 1
    s = s.replace(old5, 'the newest instances: the map\'s "Sitting 3" and "Sitting 3b")')
    old6 = "- Deuteronomy's sittings: the map; the addenda §31-36. The cost cuts: §35."; assert s.count(old6) == 1
    s = s.replace(old6, "- Deuteronomy's sittings: the map; the addenda §31-37. The cost cuts: §35.")
    old2b = "(the sheet RECORD_FORMS.md names them); MEMORY.md under 17,000 bytes; this page rewritten."
    assert s.count(old2b) == 1
    assert len(s.encode('utf-8')) <= 10240, ('THE RECOVERY PAGE OVER ITS CAP', len(s.encode('utf-8')))
    return s

# ---- 13. MEMORY ----
MEM_DESC_OLD = 'SITTING 1 DONE 2026-09-15 (1:1-3:29 read and'
MEM_PARA = """

SITTING 3b DONE 2026-09-16 (the owner: "go"; the map's "Sitting 3b" + AS BUILT): CHAPTER 5 COMPILED — cold_run_covenant_at_horeb.py the 60th runner
(49/49), law_covenant_at_horeb the 65th daemon (given_at Exod 20:3). THE LAWS' READBACK BUILT: sixteen rows on the code (VERBATIM 5, VARIANT 5,
EXPANDED 3, TURNED 3), each naming the cell that compiles the word; THE CODE'S HOLE — the second and the tenth words had no cell anywhere, compiled
here, their blocks written at the giving's line (1, 3, 7); THE TAPE'S SECOND HOLE — the request for a mediator (Exodus 20:18-21) and the answer told
only here, written once at (1, 3, 7) by the marker at 5:23, the charge to teach closed by the prior run; the receipts CHAPTER (the giving and Marah).
The tape 10/10 with RUN (1302, 96, 88, 0, 12, 1593, 36, 319, pairs, 127), markers 167; every gate green. ⚠ LESSONS: the shelf's citations follow two
numberings — the quoted words fix the verse; a daemon writing on an older line moves the journal's base (the tape before the fast check) and is THE
REST's declared delta; a close moves every old "closes" literal (eight retypes); a closer names ONE verse (a range reclasses the receipts inside it —
the gate by containment); the fast checker covers the ink, not the callee-built rows. NOT COMMITTED (since 834602b). NEXT on the ruling: the commit; chapter 6's reading or the schema sitting.
"""
MEM_IDX_OLD = "SITTINGS 1-3 DONE 2026-09-16 (chapters 1-4 COMPILED, 5 READ; COMMITTED 834602b through 2b, not pushed); NEXT: 3b or the schema sitting, on his word"
MEM_IDX_NEW = "SITTINGS 1-3b DONE 2026-09-16 (chapters 1-5 COMPILED; COMMITTED 834602b through 2b, not pushed); NEXT: chapter 6 or the schema sitting, on his word"

# ---- THE WRITES (every text built above; the files opened only now) ----
def read(p): return open(p if p.startswith('/') else f'{ROOT}/{p}', encoding='utf-8').read()
def write(p, s): open(p if p.startswith('/') else f'{ROOT}/{p}', 'w', encoding='utf-8').write(s)
plans = []
plans.append(('World/step9/DEUTERONOMY_WALK.md', lambda s: s.rstrip('\n') + '\n' + AS_BUILT))
def f_debt(s):
    assert s.count(DEBT_HDR_OLD) == 1 and s.count(DEBT_2B_OLD) == 1, (s.count(DEBT_HDR_OLD), s.count(DEBT_2B_OLD))
    return s.replace(DEBT_HDR_OLD, DEBT_HDR_NEW).replace(DEBT_2B_OLD, DEBT_2B_NEW).rstrip('\n') + '\n' + DEBT_BOX
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
    assert s.count(BRIEF_BULLET_ANCHOR) == 1 and s.count(BRIEF_ENTRY_ANCHOR) == 1 and '## SCOREBOARD (as of 2026-09-16, latest)\n' in s
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
def f_mem(s):
    assert s.count(MEM_DESC_OLD) == 1
    s = s.replace(MEM_DESC_OLD, 'SITTING 3b DONE 2026-09-16 (chapter 5 COMPILED — the laws\' readback built, code against code; the second and the tenth words compiled); ' + MEM_DESC_OLD, 1)
    return s.rstrip('\n') + '\n' + MEM_PARA
plans.append((f'{MEM}/deuteronomy-walk.md', f_mem))
def f_idx(s):
    assert s.count(MEM_IDX_OLD) == 1; s2 = s.replace(MEM_IDX_OLD, MEM_IDX_NEW); assert len(s2.encode('utf-8')) < 17000, len(s2.encode('utf-8')); return s2
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
