import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE DEUTERONOMY WALK sitting 4b — THE COMPILE OF CHAPTER 6 (2026-09-17): THE RECORDS, written after every gate ran — the numbers COMPUTED from the
# gates chain's own prints in the scratchpad (ch6b_chain/*.out; never recited) and the docket's own rows; every text built whole before any file is
# opened; the ledgers appended, the map appended, the checklist's boxes marked paid, the recovery page REWRITTEN whole under its cap, the memory index
# edited under its cap. `--check` parses and prints without writing. Sitting 3b's form (write_ch5b_records.py) on the sheet World/step9/RECORD_FORMS.md.
import os, re, sys, subprocess
ROOT = _ROOT
SP = os.path.dirname(os.path.abspath(__file__))
G = f'{SP}/ch6b_chain'
MEM = os.path.expanduser('~/.claude/projects/-Users-Shared-TorahSim/memory')
CHECK = '--check' in sys.argv
def rd(name): return open(name if name.startswith('/') else f'{G}/{name}', encoding='utf-8', errors='ignore').read()
def last_frac(name, m):
    t = rd(name); hits = re.findall(r'(\d+)/%d\b' % m, t); assert hits, (name, 'no n/%d' % m); return int(hits[-1])
# ---- THE NUMBERS FROM THE PRINTS ----
summ = rd('SUMMARY.txt'); assert 'GATES CHAIN DONE — ALL GREEN' in summ, summ
tape = rd('tape.out'); assert '10/10 checkpoints' in tape and 'OK   THE REST' in tape
CO = re.findall(r'CHECKPOINT (CO\d) .*? (MATCH|MISS|DIVERGE)$', tape, flags=re.M); assert len(CO) == 9 and all(v == 'MATCH' for _, v in CO), CO
tape_elapsed = re.search(r'elapsed ([\d.]+)s', tape).group(1)
PL = re.search(r"PLACEMENT \(O9 T2\): markers (\{[^}]*\}); events (\{[^}]*\})", tape); assert PL
assert PL.group(2) == "{'text_constrained': 109, 'page_order': 1140, 'reading_placed': 55}", PL.group(2)
rg = rd('register.out'); m = re.search(r'DECLARED (\d+); DEBT (\d+); FAILS (\d+)', rg); assert m and 'THE REGISTER GATE: GREEN' in rg
RG = tuple(int(x) for x in m.groups()); assert all(re.search(r'Deut 5:%d +CHAPTER +declared' % v, rg) for v in (12, 16, 32)) and re.search(r'Deut 4:45 +DAEMONS +green .*daemons 2', rg), rg[-1500:]
assert not re.search(r'^\s*Deut 6:\d+\s+(CHAPTER|DAEMONS|ACT|CLOSE|RUN)', rg, flags=re.M), 'a seat in chapter 6 appeared'   # the finder blind to 6:25 — asserted at CO6 too
dg = rd('daemon.out'); m = re.search(r'\((\d+) daemons, (\d+) functions\)', dg); assert m and 'gate satisfied' in dg; DG = tuple(int(x) for x in m.groups())
dp = rd('dependency.out'); m = re.search(r'dispositions on file: (\d+) edges, (\d+) pointers', dp); assert m and 'gate satisfied' in dp; DP = tuple(int(x) for x in m.groups())
LC = re.search(r'LINK CENSUS \(the link review law\): reference (\d+), transfer (\d+), hypothesis (\d+), none (\d+)', dp); assert LC; LC = tuple(int(x) for x in LC.groups())
m = re.search(r'required edges (\d+), required pointers (\d+); live import edges (\d+)', dp); DPR = tuple(int(x) for x in m.groups())
bw = rd('build.out'); assert 'ALL GREEN' in bw, bw[-600:]
jg = rd('journal2.out'); assert 'GATE GREEN' in jg and 'GATE GREEN' in rd('journal.out'); m = re.search(r'(\d+) kinds, (\d+) rows in the index', jg); JG = tuple(int(x) for x in m.groups())
sw = rd('sweep.out'); SW_P = len(re.findall(r'^PASS +cold_run_\w+\.py', sw, flags=re.M)); SW_F = len(re.findall(r'^FAIL +cold_run_\w+\.py', sw, flags=re.M))
SW_CELLS = sum(int(a) for a, b in re.findall(r'score=(\d+)/(\d+)', sw)); assert SW_P + SW_F == 61, (SW_P, SW_F); assert SW_F == 0, 'the sweep has failures — read them first'
po = rd('positions.out'); m = re.search(r'(\d+) checkpoints over (\d+) pauses', po); assert m, po[-800:]; PO = tuple(int(x) for x in m.groups())
PR = {'census': last_frac('probe_census.out', 224), 'installation': last_frac('probe_installation.out', 6), 'readback': last_frac('probe_readback.out', 15),
      'register': last_frac('probe_register.out', 7), 'sequence': last_frac('probe_sequence.out', 4), 'view': last_frac('probe_view.out', 6),
      'population': last_frac('probe_population.out', 9), 'journal': last_frac('probe_journal.out', 7), 'cursor': last_frac('probe_cursor.out', 6),
      'large_letter': last_frac('probe_large_letter.out', 6), 'checkpoint': last_frac('checkpoint.out', 7)}
ck = rd('probe_clock.out'); m = re.findall(r'(\d+)/(\d+)', ck); PR['clock'] = ('%s/%s' % m[-1]) if m else 'exit 0'
assert PR['checkpoint'] == 7 and PR['readback'] == 15 and PR['installation'] == 6 and PR['large_letter'] == 6, PR
run1 = rd(f'{SP}/ch6_run1.out'); assert '42/42' in run1
# the docket's numbers from its own rows
DK = 'logic/oral_triage/deu_06_vaetchanan_exam_2026-09-17.md'
dk = open(f'{ROOT}/{DK}', encoding='utf-8').read()
rows = [l for l in dk.split('\n') if re.match(r'^- .*? — (LAW|DERIVATION|DISPUTE|CONTEXT|OUTSIDE)\.', l)]
VD = {v: sum(1 for l in rows if re.match(r'^- .*? — %s\.' % v, l)) for v in ('LAW', 'DERIVATION', 'DISPUTE', 'CONTEXT', 'OUTSIDE')}
NROWS = len(rows); NLINK = sum(1 for l in rows if '[LINK' in l); NTOPIC = sum(1 for l in rows if '[TOPIC' in l); NCRED = sum(1 for l in rows if 'CREDITED' in l)
NWHOLE = sum(1 for l in rows if '[whole:' in l); DKB = len(dk.encode('utf-8'))
assert NROWS == 747 and NLINK + NTOPIC == NROWS and VD['OUTSIDE'] == 0, (NROWS, NLINK, NTOPIC, VD)
hp = subprocess.run(['python3', 'logic/solo_tools/scrub_home_paths.py', '--check'], cwd=ROOT, capture_output=True, text=True); assert hp.returncode == 0, hp.stdout[-500:] + hp.stderr[-500:]
NUM = dict(RG=RG, DG=DG, DP=DP, LC=LC, DPR=DPR, JG=JG, SW=(SW_P, SW_CELLS), PO=PO, PR=PR, PL=PL.groups(), tape_elapsed=tape_elapsed, docket=(NROWS, NLINK, NTOPIC, NCRED, NWHOLE, DKB, VD))
print('THE NUMBERS:', NUM)
pr_line = ('census %d/224, installation %d/6 (I5 66), readback %d/15 (Q13-Q15 the third form), register %d/7, clock %s, sequence %d/4, view %d/6, population %d/9, journal %d/7, cursor %d/6, large_letter %d/6, checkpoint %d/7'
           % (PR['census'], PR['installation'], PR['readback'], PR['register'], PR['clock'], PR['sequence'], PR['view'], PR['population'], PR['journal'], PR['cursor'], PR['large_letter'], PR['checkpoint']))
gates_line = ('the daemon gate GREEN (%d daemons, %d functions WRAPPED); the dependency gate GREEN (%d edges and %d pointers on file — the link census reference %d / transfer %d / hypothesis %d / none %d; required %d edges and %d pointers, live import edges %d); '
              'build_world ALL GREEN (220 units, standing 2203, hash 8b8fff1fa28953af unmoved — no freeze this sitting); the journal gate GREEN twice — before and after the sweep (%d kinds, %d rows in the index); THE REGISTER GATE --strict GREEN (DECLARED %d, DEBT %d, FAILS %d — no seat in chapter 6: the finder blind to 6:25 as measured; Deut 5:12, 5:16, 5:32 CHAPTER and 4:45 DAEMONS unmoved); '
              'the positions table %d checkpoints over %d pauses (CO1-CO9 in it; checkpoint_probes %d/7 after the rebuild); the sweep %d/61 at %s graded cells; the home-path gate GREEN'
              % (DG[0], DG[1], DP[0], DP[1], LC[0], LC[1], LC[2], LC[3], DPR[0], DPR[1], DPR[2], JG[0], JG[1], RG[0], RG[1], RG[2], PO[0], PO[1], PR['checkpoint'], SW_P, format(SW_CELLS, ',')))
docket_line = ('%d rows (link %d / topic %d; LAW %d, DERIVATION %d, DISPUTE %d, CONTEXT %d; credited %d; %s bytes), EVERY ROW READ WHOLE — %d rows carry a "[whole: …]" note naming what the 170-character pass had missed'
               % (NROWS, NLINK, NTOPIC, VD['LAW'], VD['DERIVATION'], VD['DISPUTE'], VD['CONTEXT'], NCRED, format(DKB, ','), NWHOLE))

# ---- 1. THE MAP — AS BUILT ----
AS_BUILT = """

## Sitting 4b — THE COMPILE OF CHAPTER 6 — AS BUILT (2026-09-17; the design above stands as written; every departure from it named here; THE WHOLE-ROW
## RULE was ruled between this sitting's RUN 2 and RUN 3 and its fix (a)-(d) ran inside the sitting — the two tail sections above)

THE RESULT. Deuteronomy 6:1-25 is COMPILED AND ON THE TAPE: World/step9/cold_run_hear_o_israel.py the 61st runner (MATRIX 42/42 on its first graded
run; six cells F1 the_header, F2 the_creed, F3 the_four_duties, F4 the_gift_and_the_warning, F5 the_test_and_the_right, F6 the_sons_question with 42
asks; eighteen DATA rows; the readback's seven rows; fourteen exam persons, three exempt — the bridegroom, the daughter, the bathhouse owner; the scene
and the narrative tuples matched as predicted by script), law_hear_o_israel the 66th daemon (given_at Deut 6:4 — the Shema's first and only giving;
installed_by boot; six functions WRAPPED; no timer), three kinds and two effects in the registries (1125 kinds, 1025 effects), TWO LINES AND NO MARKER
on the tape — shema_declared (6:4-9) and testing_barred (6:16-19) under "# ---- Deut 6 ----" on the counter's own day (40, 11, 1). THE TAPE 10/10 WITH
THE REST ON ITS FIRST RUN: RUN (1304, 96, 88, 0, 12, 1595, 37, 319, the four pairs, 127) exactly as THE PREDICTION'S ARITHMETIC wrote it; PREVIOUS_RUN
3b's RUN EXACTLY — no declared delta (the daemon writes only on its own lines, so the tape minus this runner's lines reproduces 3b's tuple);
NEWEST_RUNNER hear_o_israel; markers 167 UNMOVED (forward 129, retrograde 23, proleptic 15); entities 319, closes 127, the population table 148
UNMOVED; PLACEMENT markers %s, events %s (page_order 1138 → 1140 — AS PREDICTED); CENSUS (2487, 1313, 1304, 1158, 6, 10, 9, 0, 71, 167, 129, 15, 23,
849, 272) as the stitcher printed it (on tape 1302 → 1304, kinds 847 → 849, subjects 272 unmoved); CO1-CO9 all MATCH; the run %ss. THE SHEMA'S LAW IS
COMPILED FOR THE FIRST TIME, its giving the chapter's own day: shema_commanded a STATUS on Israel (the four duties standing — the recitation, the
teaching, the tefillin, the mezuzah), test_barred a BLOCK on Israel; the second word's block stands from 3b (no second write — CO5); the charge to
teach stands CLOSED by the prior run (6:1 a reference row — CO7). THE DOCKET %s by the union rule: %s; Berakhot 2a-16a's five verse-anchored
stretches (2a-2b, 10b-11a, 13a-13b, 15a-16a) and 61b read whole, the remainder of the range (541 rows) ENUMERATED outside declared scope; the crowns
twenty-two in the docket's own list.

THE READBACK'S THIRD FORM — A RETELLING INSIDE A LAW (T1) BUILT: seven reference rows — the son's answer's five (6:21-25), the header's (6:1 against
stand_here_commanded — the charge executed, the debit's close by the prior run unmoved), the test's (6:16 against Rephidim's named line, Massah — a RUN
CITATION by name) — graded VERBATIM 3 / EXPANDED 3 / SHORTENED 1 (typed from the runner's print; the design's prediction held), every row's tape entry
FOUND on the running world by kind and first verse (CO4: brought_out at Exodus 12:51, the ten plague_struck lines, sworn_by_himself at Genesis 22:16,
oath_upheld at 26:3, visitation_promised at 50:24, stand_here_commanded at Deuteronomy 5:28, ten_words_declared at 4:10); no row OPEN. THE RULE T1 HELD:
"and you shall say to your son" (6:21) is a law's clause, so the retelling's rows are graded by the cell that compiles the duty to answer — F6
the_sons_question (the four askings: Exodus 12:26, 13:8, 13:14, Deuteronomy 6:20 — Mishnah Pesachim 10:4, Pesachim 116a-b; the passover runner's
firstborn cell by CALL for 13:14's ink) — and the shelf itself taught the form's seat: Pesachim 116a:11 puts the chapter's own verse in the answer's
first clause ("we were slaves to Pharaoh" — Shmuel's opening of the telling), the readback's row 6:21 the telling's obligatory clause. THE RECEIPT
WITHOUT THE NAME (6:25 "as He commanded us") a RUN_CITATION pointer of form AS_WHEN naming stand_here_commanded and the giving; the register gate's
own finder (class_receipts, by CALL at CO6) lists no seat at 6:25 nor anywhere in the chapter — the blindness MEASURED and ASSERTED, the finder's third
form owed to a gate sitting (the 4b box below).

THE DEPARTURES FROM THE DESIGN, each found by an instrument and each a lesson below: (1) THE TWO KINDS ARE STATUTE BY FORM, not speech — the stitcher's
register test dropped both lines as register-off on its first print (no narrative verb within ten verses; the chapter's verbs are the law's own), and
the design had missed 2b's lesson that the own-day giving of a law passes the register test by form (add_nothing_commanded, chapter 4): retyped
from the stitcher's print, the registry comment names it; (2) THE OATH'S THREE POINTERS (the design's (i) — 6:10, 6:18, 6:23 "swore to your fathers")
WERE NOT DEMANDED by the token census: the citations ride the mamre and joseph edges' whys; the census demanded instead FOUR AS_WHEN pointers (6:3,
6:16, 6:19, 6:25 — each a RUN_CITATION with its referent named) and ONE uncited installation token at 6:11 — "and you shall EAT and be satisfied" is
the land's eating, matched by the census to the offerings' institution (the tzav span): a homograph, dispositioned FALSE with its why; (3) THE FAST
CHECK REFUSED BEFORE THE TAPE — checkpoint_check.py rides the journal, and the tape had grown by two lines (the stepper's base shorter than the tape):
the order when lines are ADDED is the tape first, then the check (235 rows after — 226 + the nine CO rows; the standing eighteen DIVERGE-expected misses
read by label, none CO); (4) THREE INK ASSERTS TYPED FROM MEMORY FAILED THE FAST CHECKER (the readback's deltas; Exodus 17:7's and Numbers 14:22's
tokens) — retyped from the print (1b's lesson, three times over); (5) A FORMS COPY CARRIES THE PORTABLE THREE-LEVEL ROOT HEADER — a scratch derivation
by plain sed ran with the wrong root (the effects layer not found; the wrong database): derive_form.py turns the header back to git and applies its
substitutions asserted; (6) YAML READS FALSE AS A BOOLEAN — the pointer script's check compared the disposition as a string and found none; the check
reads it back as str().upper(); (7) THE DOCKET'S SHORT CUT WAS STRUCK BY THE OWNER'S RULE mid-sitting — the 747 rows had been read at 170 characters
at RUN 2; every row was printed whole and reread between RUN 2 and RUN 3 (70 rows corrected, 21 verdicts moved, the parts' WHOLE overlays the record),
and the four older cuts were reread and corrected in the same pass (the two tail sections above); (8) A CELL OF CHAPTER 4 RODE THIS SITTING'S TAPE —
cold_run_obey_horeb.py's add_beside retyped from a whole row (Sanhedrin 89a:2 — the cut had typed the Gemara's challenge as the ruling; R. Zeira's
answer makes the fifth compartment spoil either way: accepted), one ledger effect on one exam person, no count moved; (9) TWO PROBES RETYPED FROM THE
CHAIN'S FIRST PRINT — readback Q13, written at RUN 2 before the runner existed, looked for a 'found' key the runner's rows never carry (it now finds
each row on the running world by kind and first verse — Q2's form, the tape's CO4); large_letter H5, sitting 4's exhibit that 6:4 had NO tape line,
moved when the compile filed the Shema's line there (retyped to the new state: a statute line at 6:4, still no register seat, the large-letter edge
still unfiled — PARKED): the chain's first run stopped at the probes step (14/15, 5/6), the second run from that step ALL GREEN (the tape's print
the first run's, kept).

THE GATES, COMPUTED FROM THEIR PRINTS (one chain, gates_chain.sh — run twice, the first stopped at the probes step by the two retypes above, the
second from that step ALL GREEN; the tape's print the first run's): the probe suites %s; %s.

⚠ THE LESSONS OF 4b (eleven): (1) THE OWN-DAY GIVING OF A LAW IS STATUTE BY FORM — the stitcher's register test passes a statute by its form and an act
or a speech only by a narrative verb within ten verses of the same chapter; a chapter of law has no such verb, so its lines are typed statute (2b's
lesson, missed at the design and caught by the print); (2) THE DESIGN'S POINTER LIST IS A PREDICTION — the token census decides which citations need
a pointer (the AS_WHEN receipts) and which ride an edge's why; read its demands on the DB, one by one; (3) THE CENSUS READS HOMOGRAPHS — an
institution's token ("eat", the offerings') matches the land's eating: named FALSE with its why, never a blanket row; (4) THE TAPE FIRST, THEN THE
FAST CHECK, when the tape grows — the checker rides the journal; its standing misses are the declared divergences, read by label; (5) THE PRINT FIRST,
THEN THE ASSERT (the callees' facts printed by ch6_callees.py before part 3; the ink's deltas from the fast checker's print) — three asserts typed from
memory failed; (6) A FORMS COPY IS PORTABLE, A SCRATCH DERIVATION IS NOT — derive_form.py turns the three-level header back to git and asserts every
substitution; (7) YAML'S FALSE IS A BOOLEAN — compare str(value).upper(); (8) A CUT ROW ENDS BEFORE THE ANSWER — the Gemara's challenge or hypothesis
sits at a row's head and the resolution at its tail, so a verdict from an opening is right in kind and wrong in substance about one time in ten (the
measure: at 170 characters one in ten wrong, two in a hundred on the wrong row; at 650 none) — EVERY ROW WHOLE, the owner's rule; (9) A DAEMON THAT
WATCHES ONLY ITS OWN LINES LEAVES THE REST WITHOUT A DELTA — PREVIOUS_RUN is the prior sitting's tuple exactly, the first sitting since 1b with no
declared delta; (10) THE READBACK HAS THREE FORMS NOW — acts (1b), laws (3b), a retelling inside a law (4b: the grades are the cell's verdicts) — and the
third's seat was taught by the shelf (Pesachim 116a: the telling opens with the chapter's verse); (11) A PROBE WRITTEN TO FAIL BEFORE THE RUNNER
EXISTS IS RETYPED ONCE TO THE RUNNER'S SHAPE (Q13's key), AND A HYPOTHESIS'S EXHIBIT MOVES WHEN THE TAPE GROWS (H5's premise — 1b's lesson on a
probe's verse, now on a probe's premise): the chain's first FAIL is read and both retyped from its print, the chain rerun from the failed step.

THE DISPOSITIONS ADDED: eleven edges (ten CALL — covenant_at_horeb, obey_horeb, decalogue, exodus_story, pesach, opening_speech, mamre, joseph,
mekoshesh, erection; the registration edge sequence → hear_o_israel), one FALSE edge (hear_o_israel → tzav at 6:11, the homograph) and four pointers
(RUN_CITATION, form AS_WHEN — Deut 6:3, 6:16, 6:19, 6:25); the span hear_o_israel [[Deut, 6, 1, 25]]; the token census demanded NO further edge.
MOVE_CATALOG CHECKED, unmoved: the runner's law cells return the shelf's parameters (the compartments FOUR, the times, the postures, the gates) and CALL
the callees' cells; the shelf's own moves on the chapter (the count from the spellings, the two analogies with the rule of choice, the re-pointed verb
that exempts the mother, the particle withdrawn) are the docket's and MIDDOT's rows, no new move of the compiler.

THE FORMS: the sitting's scripts and prints copied into World/step9/forms_deuteronomy_walk/ by copy_ch6b_forms.py (the recon, the scan and the dump,
the docket's parts with their WHOLE overlays and the common helper, the types, the callees' print, the runner's four parts with the generator, the
assembler and the fast checker, the recorder and the stitcher under their sitting's names, the literals' patcher, the pointers, the design's, the
runs' and the records' writers, the whole-row instruments and their seven chunk prints, the chapter-4 retype, the checkpoints' writers, the gates
chain's folder — no scratch path and no home path in any copied form).

NEXT on the ruling: the commit on the owner's word (4b whole, the rule and its fix, since a7955cc); then CHAPTER 7's reading (7:1-26 — the seven
nations and the ban, the chosen people, the reward; the reading shape, in four runs, every row whole) — or the Decalogue-schema sitting first (ON THE
TABLE, not a ruling). Nothing committed: the tree uncommitted since a7955cc, on the owner's word only.
""" % (PL.group(1), PL.group(2), tape_elapsed, DK, docket_line, pr_line, gates_line)

# ---- 2. COMPILE_DEBT — the sitting-4 box marked PAID + the 4b box ----
DEBT_HDR_OLD = "## deu_06_vaetchanan_2026-09-17.md, 97 sources; one unit deu_06_shema FROZEN, the 220th) — OWED TO THE COMPILE (sitting 4b): (a) THE SHEMA'S FOUR DUTIES AS"
DEBT_HDR_NEW = "## deu_06_vaetchanan_2026-09-17.md, 97 sources; one unit deu_06_shema FROZEN, the 220th) — PAID AT 4b (the 4b box below, item by item) — AS WRITTEN AT THE READING, OWED TO THE COMPILE (sitting 4b): (a) THE SHEMA'S FOUR DUTIES AS"
DEBT_BOX = """
## DEUTERONOMY SITTING 4b — THE COMPILE OF CHAPTER 6 (2026-09-17; DEUTERONOMY_WALK.md "Sitting 4b" design + AS BUILT; logic/oral_triage/deu_06_vaetchanan_exam_2026-09-17.md
## %d rows, every row read whole; cold_run_hear_o_israel.py 42/42; law_hear_o_israel the 66th daemon; the tape 10/10 with RUN (1304, 96, 88, 0, 12, 1595, 37, 319, pairs, 127)). THE
## SITTING-4 BOX (a)-(l) PAID — (a) THE FOUR DUTIES as law cells — F3 the_four_duties: recite_when / recite_how / recite_who (Mishnah Berakhot 1:1-3:6 the answer sheet; the
## postures, the audibility, the language, the exemptions), the_passages, teach_your_sons, the tefillin's five asks and the mezuzah's three, the_seven; THE COMPARTMENTS FOUR A
## PARAMETER taught by the shelf, the spellings' open row a DATA row (6:8 defective, 11:18 plene, Exodus 13:16 plene; the shelf's count needs 11:18 defective — recorded, not
## resolved); the write shema_commanded a STATUS on Israel at the chapter's own line; (b) FEAR, SERVE, SWEAR — 6:13 a positive clause (Temurah 3b:17 the true oath permitted),
## the prohibition's side decalogue.vain_name by CALL; (c) NO OTHER GODS — covenant_at_horeb.the_second_word by CALL, other_gods_barred standing (CO5); Tosefta Avodah Zarah 1:3's
## "go along with" the application; (d) THE TEST — exodus_story.trials by CALL, the Rephidim lines FOUND, test_barred a BLOCK at the second line, the pointer at 6:16 (Massah);
## (e) THE RIGHT AND THE GOOD — the abutter (Bava Metzia 108a) the exam's case, its bounds (108b) DATA; (f) THE SON'S ANSWER — THE READBACK'S THIRD FORM (T1) BUILT: seven rows
## VERBATIM 3 / EXPANDED 3 / SHORTENED 1, the four askings, no write; (g) 6:1'S EDGE — a reference row against stand_here_commanded, the charge's close unmoved (CO7), the
## triad 5:31 / 6:1 / 7:11; (h) THE LIST — a DATA row (Chullin 17a's conquest houses beside it); (i) "SWORE TO YOUR FATHERS" — the citations carried by the mamre and joseph
## CALL edges' whys, the census demanding no pointer (the design's three amended away); (j) THE RECEIPT WITHOUT THE NAME — a RUN_CITATION pointer (AS_WHEN) at 6:25, the finder's
## blindness asserted at CO6 by CALL; (k) THE LARGE LETTERS — parked, a DATA row, no edge; (l) THE DOCKET — %d rows by the union rule, EVERY ROW READ WHOLE under the owner's rule
## of this date. OWED FROM 4b: (i) THE FINDER'S THIRD FORM — "as He commanded" (the comparative with the verb and a suffix, no Name: Deuteronomy 6:25 and Ezra 4:3 the Bible's
## two seats) taught to register_census.py's receipts finder at a GATE SITTING (a gate change across the whole Torah, never one runner's); until then 6:25 stands on its pointer;
## (ii) THE WAR CHAPTER'S CALL INTO 6:11 — the spoil of the seven nations permitted (the Sifrei 201:3; Chullin 17a) compiles at chapter 20's sitting and cites 6:11 by CALL;
## (iii) THE FRINGES' LAW — Numbers 15:37-41 the Shema's third passage, held in mekoshesh's span by REFERENCE; its own cell (the corners, the thread, who is bound — Menachot 38a
## on) a sitting of the second pass; (iv) THE SPELLINGS' OPEN ROW stands open — a codex question (RESEARCH_LOG 2026-09-17), no sitting owns it; (v) the Mekhilta Pisha 17 (the
## first copy's spine on the tefillin) named, unopened — a reading sitting's if the tefillin's Exodus seats are reread; (vi) THE LARGE LETTERS parked on the owner's word.
## NOTHING ELSE IN CHAPTER 6 IS OWED TO A LATER SITTING OF ITS OWN.
""" % (NROWS, NROWS)

# ---- 3. MIDDOT — the docket entry ----
MIDDOT_ANCHOR = "\n## Exodus block campaign — owner's word \"Do 3\")\n"
MIDDOT_ENTRY = """- THE CHAPTER-6 DOCKET (THE DEUTERONOMY WALK sitting 4b, 2026-09-17; logic/oral_triage/deu_06_vaetchanan_exam_2026-09-17.md — %d rows, every row read
  whole; the rules about rules the docket carries, each at its row):
  · ONE WORD READ TWICE (Berakhot 15a:9-10 on 6:4 "hear"; the Sifrei 31:7): R. Yose takes two rules from one word — make it heard to your ear AND in any
    language; the first tanna one — the recitation's audibility and language from a single imperative: F3 recite_how; the arms at Sotah 32b:18-21 and
    Berakhot 13a:26-27 (Rabbi: Hebrew, from "and these words shall be", 6:6; the Rabbis: any language, from "hear").
  · A DUTY'S TIMES FROM THE VERB'S TWO CLAUSES (Berakhot 2a:8, 10b:31 on 6:7 "when you lie down and when you rise"): the evening first because the verse
    says lying down first; the morning until three hours (R. Yehoshua) — the answer sheet's times a PARAMETER table read off the clause order: F3 recite_when.
  · "THE WAY" IS A VOLUNTARY WALK (Berakhot 11a:4-8 on 6:7; Tosefta Berakhot 1:5 the clauses assigned the other way round): one busy with a duty is exempt
    because the verse's walking is one's own — the groom of a virgin: F3 recite_who (the exemptions' ground in the verse).
  · THE COUNT FROM THE SPELLINGS (Menachot 34b:1; Sanhedrin 4b:12-14 on 6:8, 11:18, Exodus 13:16 "frontlets"): two seats written defective and one plene
    make FOUR compartments — "the vocalization against the tradition" (Rabbi's count by the written form); the ink spells 11:18 plene, so the number is a
    PARAMETER the shelf teaches and the derivation a recorded argument: F3 tefillin_compartments, the DATA row the_spellings (THE OPEN ROW).
  · THE TWO ANALOGIES AND THE RULE OF CHOICE (Menachot 34a:12 on 6:9 "you shall write"; the Sifrei 36:2): "writing" here resembles the stones (27:8) or
    the suspected wife's scroll (Numbers 5:23) — "let us see which it resembles": a writing for the generations from a writing for the generations —
    the reception rule's own exhibit, a verbal analogy with two candidates settled by the like: F3 mezuzah_writing.
  · "YOUR HOUSE" IS YOUR RESIDENCE (Yoma 11a:3, 11a:7-14; Bava Metzia 101b:19; Chullin 135b:15 on 6:9; Mishnah Maaser Sheni 3:8): city gates and
    courtyards obligated, the store and the bath exempt, the renter and the partners obligated, the Temple's chambers by what they open to: F3 mezuzah_gates.
  · THE ORDER OF DONNING FROM THE ORDER OF THE VERSE (Menachot 36a:5 on 6:8; the Sifrei 35:11): the arm bound first, the head first removed — "as long as
    they are between your eyes, let them be two": F3 tefillin_order.
  · THE JUXTAPOSITION REFUSED (Arakhin 3b:10 on 6:8 "bind … frontlets"): the priests bound in the head's tefillin though the garments bar the arm's — the
    two words side by side do not make the two one duty: F3 tefillin (the arm and the head two duties — DATA the_tefillin_table).
  · THE PARTICLE'S EXTENSION WITHDRAWN (Bava Kamma 41b:7; Bekhorot 6b:4 on 6:13 "you shall fear ET the LORD"): Shimon HaAmasoni expounded every accusative
    particle and withdrew at this one — whose fear beside God's? — his reward for the withdrawal as for the expositions: E1 refused on F4 fear_serve_swear.
  · THE POSITIVE CLAUSE THAT PERMITS (Temurah 3b:16-17, 4a:2 on 6:13 "by His name you shall swear"): the true oath is permitted by the clause itself (with
    the bailee's oath of Exodus 22:10 its pair), and "you shall fear" is refused as the warning a flogging needs: F4 fear_serve_swear (the oath's cases
    holiness.deposit_case and vayikra5's by CALL).
  · A RULE BEYOND THE LETTER SEATED IN THE INK (Bava Metzia 108a:10, 108b:4, 16b:13, 35a:12 on 6:18 "the right and the good"): the abutter's right, the
    debtor's land returned, the appraisal reversed — a verse of conduct made a rule of property with its bounds (the gentile buyer, the seller's ban): F5
    the_right_and_the_good, the DATA row the_abutter.
  · THE ONE EXCEPTION TO "YOU SHALL NOT TEST" (Taanit 9a:3 on 6:16 with Malachi 3:10): the tithe — "test Me in this" — R. Yochanan's exception written into
    the prohibition's own cell: F5 you_shall_not_test (DATA).
  · THE ANSWER OPENS WITH THE CHAPTER'S VERSE (Pesachim 116a:11-12 on 6:21; Mishnah Pesachim 10:4; Pesachim 116b the four sons): "we were slaves to
    Pharaoh" is Shmuel's "disgrace" — the telling's first clause is the retelling the chapter commands; "according to the son's understanding" the four
    askings' rule — THE READBACK'S THIRD FORM taught by the shelf: F6 the_answer_rows, the_four_askings.
  · TWO CLAUSES, TWO MEN (Berakhot 61b:5-10; Sanhedrin 74a:15; Mishnah Berakhot 9:5; Tosefta Berakhot 6:11 on 6:5): R. Eliezer reads "with all your soul"
    to the man whose body is dearer and "with all your might" to the man whose money is dearer; R. Akiva — "even if He takes your soul", and lived it: F2
    with_all_your_soul, with_all_your_might (the creed's three terms — the DATA row the_creed_terms).
  · THE CREED FIRST SAID AT A DEATHBED (Pesachim 56a:6-8 on 6:4): "hear, Israel" addressed to the father Jacob by his sons, and his answer the whispered
    response line — Moses did not say it, Jacob said it: F2 hear_o_israel (DATA; the Sifrei 31:6's Talmud seat).
  · THE VERB RE-POINTED EXEMPTS THE MOTHER (Kiddushin 29b:8-11 on 6:7 / 11:19 "and you shall teach them"): "you shall teach" read as "you shall learn" —
    one whose duty it is to learn teaches, the mother not obligated; he before his son: F3 teach_your_sons (the father's duty; the Sifrei 34:1-4).
  · THE TRIAD READ AS ONE SCOPE (Bava Kamma 87a:2 on 6:1; Pesachim 116b:12): "the commandment, the statutes and the judgments" juxtaposed — whoever is in
    the judgments is in the commandments (R. Yehuda: the blind exempt from all); the blind obligated to tell (116b): F1 the_header (DATA the_blind).
  · "GO AFTER" READ AS "GO ALONG WITH" (Tosefta Avodah Zarah 1:3 on 6:14): the caravan to the idolaters' festival — the plural prohibition's application
    to conduct, the second word's cell by CALL: F4 no_other_gods.
""" % NROWS

# ---- 4. MISHNAH_TOPICS — the rows touched ----
W4 = "THE DEUTERONOMY WALK sitting 4b"
DKF = "deu_06_vaetchanan_exam_2026-09-17.md"
TOPIC_NOTES = {
 "**1. Mishnah, Blessings**": " — 1:1-3:6 READ WHOLE (eighteen rows, the recitation's answer sheet) and 9:5 READ 2026-09-17 (%s: the times, the postures, the exemptions, the passages' order; the three terms of 6:5; Berakhot 2a-2b, 10b-11a, 13a-13b, 15a-16a and 61b READ WHOLE, the rest of 2a-16a enumerated outside scope; %s)" % (W4, DKF),
 "**8. Mishnah, Second Tithe**": " — 3:8 READ 2026-09-17 (%s: the Temple's chambers open to the profane or the holy — the mezuzah's gates, 6:9)" % W4,
 "**12. Mishnah, Sabbath**": " — 12:3's gemara Shabbat 103b:14-17 CREDITED and reread 2026-09-17 (%s: the perfect letters of the mezuzah, 6:9)" % W4,
 "**14. Mishnah, Passover**": " — 10:4 READ with Pesachim 116a-116b READ WHOLE, 56a:6-8 CREDITED 2026-09-17 (%s: the four sons; 'we were slaves' the answer's first clause — the readback's third form, 6:20-21; the creed at Jacob's bed, 6:4)" % W4,
 "**16. Mishnah, Day of Atonement**": " — 1:1's gemara Yoma 11a READ WHOLE 2026-09-17 (%s: the mezuzah's gates — 'your house' your residence, 6:9)" % W4,
 "**20. Mishnah, Fasts**": " — 1:1's gemara Taanit 9a:3 READ 2026-09-17 (%s: the tithe the one exception to 'you shall not test', 6:16)" % W4,
 "**21. Mishnah, Scroll of Esther**": " — 1:8's gemara Megillah 9a:5-9, 17b:1 and 20a:2 READ 2026-09-17 (%s: tefillin and mezuzot written in Hebrew from 'these words shall be', 6:6; the audibility's arms, 6:4)" % W4,
 "**28. Mishnah, Suspected Wife**": " — 7:1 READ with Sotah 32b:18-21 READ 2026-09-17 (%s: the Shema in any language from 'hear', 6:4; Rabbi's Hebrew from 6:6)" % W4,
 "**30. Mishnah, Betrothal**": " — 1:7's gemara Kiddushin 29a-30b READ WHOLE 2026-09-17 (%s: the father's duties — teach your sons, 6:7 / 11:19; the mother exempt by the re-pointed verb; the threefold study)" % W4,
 "**31. Mishnah, First Gate**": " — 41b:7 and 87a:2 READ 2026-09-17 (%s: Shimon HaAmasoni's particle withdrawn at 6:13; the blind exempt by the triad, 6:1)" % W4,
 "**32. Mishnah, Middle Gate**": " — 9:?'s gemara Bava Metzia 108a READ WHOLE, 16b:13, 35a:12, 101b:19 and 108b:4 READ 2026-09-17 (%s: the abutter — 'the right and the good', 6:18; the mezuzah the resident's, 6:9)" % W4,
 "**34. Mishnah, Courts**": " — 1:1's gemara Sanhedrin 4b and 8:7's gemara 74a READ WHOLE 2026-09-17 (%s: the compartments from the spellings — the vocalization against the tradition, 6:8; the martyr — 'with all your soul', 6:5)" % W4,
 "**38. Mishnah, Idolatry**": " — Tosefta Avodah Zarah 1:3 and Avodah Zarah 25a:13 READ 2026-09-17 (%s: 'you shall not go after' read as going along with, 6:14; the book of the upright, 6:18)" % W4,
 "**42. Mishnah, Grain Offerings**": " — 3:7 READ with Menachot 31b-37b READ WHOLE and 43b 2026-09-17 (%s: the four passages invalidate each other; the compartments, the arm, the order, the head; the mezuzah's writing and post; the seven, 6:8-9)" % W4,
 "**43. Mishnah, Slaughter**": " — 17a:12, 91b:16 and 135b:15 READ 2026-09-17 (%s: the conquest's houses, 6:11; the partners' mezuzah, 6:9)" % W4,
 "**45. Mishnah, Valuations**": " — 3b:10 READ 2026-09-17 (%s: the priests bound in the head's tefillin — the juxtaposition refused, 6:8)" % W4,
 "**46. Mishnah, Substitution**": " — 1:1's gemara Temurah 3b-4a READ WHOLE 2026-09-17 (%s: the true oath by the Name permitted, 6:13)" % W4,
}

# ---- 5. RESEARCH_LOG ----
RLOG = """

## 2026-09-17 — DEUTERONOMY 6 COMPILED (THE DEUTERONOMY WALK sitting 4b — CHAPTER 6): THE READBACK'S THIRD FORM — A RETELLING INSIDE A LAW; THE SHEMA'S
## LAW COMPILED AT ITS OWN DAY, STATUTE BY FORM; THE RECEIPT WITHOUT THE NAME — THE FINDER'S BLINDNESS ASSERTED; THE COMPARTMENTS A PARAMETER OVER AN
## OPEN SPELLING; THE CENSUS AND A HOMOGRAPH; THE WHOLE-ROW MEASURE

THE READBACK'S THIRD FORM. The readback's first form (1b) graded Moses' retelling of acts against the tape; the second (3b) graded the code said again
against the code. Chapter 6 holds a third: a retelling COMMANDED — "and you shall say to your son: we were slaves to Pharaoh …" (6:21-25) is a law's
clause, and the son's answer retells the exodus in the first person plural. The form's one new rule (T1): the answer's rows are reference rows graded
against the tape as before, AND the cell that compiles the duty to answer returns its verdict on the answer's form — the retelling's grades are the
exam's cells. Seven rows: the answer's five (6:21-25), the header's (6:1 against the charge to teach at 5:31 — executed, its debit closed by the prior
run at 3b) and the test's (6:16 against the tape's named line at Exodus 17:7, Massah — a run citation by name); VERBATIM 3, EXPANDED 3, SHORTENED 1
(the ten plagues shortened to one clause — "signs and wonders great and grievous"); every row's entry found on the running world. The shelf taught the
form's seat before the runner did: Pesachim 116a:11 puts the chapter's own verse in the telling's first clause ("we were slaves" — Shmuel's "disgrace"),
and Mishnah Pesachim 10:4's "according to the son's understanding" is the four askings' rule (Exodus 12:26, 13:8, 13:14, Deuteronomy 6:20 — the four sons).

THE SHEMA'S LAW AT ITS OWN DAY. No runner held a cell for the recitation, the teaching, the tefillin or the mezuzah — the chapter compiles them for the
first time, and their giving is the chapter's own day on the counter, (40, 11, 1), with no marker: two lines, shema_declared (6:4-9) and testing_barred
(6:16-19), the daemon writing shema_commanded (a status: the four duties standing) and test_barred (a block) on Israel. The stitcher's register test
dropped both lines on its first print — the design had typed them speech, and a chapter of law has no narrative verb within ten verses — so they are
STATUTE BY FORM, as chapter 4's own-day law was at 2b. The tape reached ten of ten on its first run with the previous sitting's tuple reproduced
exactly: a daemon that writes only on its own lines leaves the rest of the tape without a delta.

THE RECEIPT WITHOUT THE NAME. 6:25 "and it shall be righteousness for us … AS HE COMMANDED US" is a receipt with no Name in it — the comparative, the
verb and a suffix (Ezra 4:3 the Bible's one other seat). The register gate's finder scans two forms, both with the Name, so it lists no seat in the
chapter: measured at the design, asserted at the tape by calling the finder itself (CO6), and dispositioned as a run-citation pointer naming the
charge to teach (5:31) and the giving. The finder's third form is owed to a gate sitting — a change across the whole Torah, never one runner's.

THE COMPARTMENTS A PARAMETER OVER AN OPEN SPELLING. The shelf's four compartments of the head's tefillin are counted from the spellings of "frontlets"
(Menachot 34b; Sanhedrin 4b — "the vocalization against the tradition"): two seats written defective and one plene make four. The ink spells 11:18
plene (6:8 defective, Exodus 13:16 plene), so the count does not run from the text as stored. The cell returns FOUR as a parameter the shelf teaches,
the derivation stands as a recorded argument on another witness, and the DATA row the_spellings names the divergence — recorded at the reading, carried
by the compile, resolved by neither.

THE CENSUS AND A HOMOGRAPH. The token census, run past the runner's imports, demanded four AS_WHEN pointers (6:3, 6:16, 6:19, 6:25 — receipts of
what "the LORD has spoken" or "commanded") and one edge the runner never imports: an installation token at 6:11, "and you shall EAT and be satisfied",
matched to the offerings' eating of Leviticus 6-7. The verse's eating is the land's; the edge is dispositioned FALSE with its why. The oath's three
"swore to your fathers" seats (6:10, 6:18, 6:23) were not demanded at all — the citations ride the edges to the oath's own runners. The design's pointer
list is a prediction; the census decides.

THE WHOLE-ROW MEASURE. The owner ruled between this sitting's second and third runs that every row of the shelf is read whole before its verdict is
typed, and the cuts taken since the four-run rule were reread whole and corrected. The measure across the five dockets: at 170 characters one verdict
in ten was wrong in substance and two in a hundred sat on the wrong row (chapter 6: 70 of 747 rows corrected, 21 verdicts moved); at 650 characters
none moved in chapters 1-5 but one cell had been typed from a cut row's challenge instead of its answer (Sanhedrin 89a:2 — the fifth compartment
spoils even beside the four, R. Zeira; the chapter-4 cell retyped and carried by this sitting's tape); at 1,500 none. The lesson stands in the map: a
cut row ends before the answer — the Gemara's challenge sits at a row's head, the resolution at its tail.
"""

# ---- 6. THE_STEPS ----
STEPS_ANCHOR = "\n## Step 6 — Publish\n"
STEPS_PARA = """
DEUTERONOMY — SITTING 4b — CHAPTER 6 COMPILED (2026-09-17, on Brian's "Go", "Next go" and "Ok go" for its runs; World/step9/DEUTERONOMY_WALK.md
"Sitting 4b" and "Sitting 4b — AS BUILT"). The Shema's law — hear, love, keep the words on your heart, teach them, bind them, write them on the
doorposts — had never been compiled anywhere in the machine, so this sitting compiled it for the first time and gave it at the day the chapter is
spoken, with no marker: the four duties stand on Israel's ledger from that day, and the test at Massah is barred from it. The readback took its third
form here: the son's question and the answer are a law that commands a retelling, so the answer's rows are graded against the tape as before, and the
grading is the law's own cell doing its work — the Talmud itself puts the chapter's verse in the first clause of the Passover telling. In the middle of
the sitting Brian ruled that no row of the Talmud is ever read cut: the docket's seven hundred and forty-seven rows were reread whole, seventy
corrected, and the four earlier dockets reread where a cut had been taken — one cell of chapter 4 had been typed from a challenge instead of its
answer and was retyped. The runner matched its answer sheet on the first run; the tape reached ten of ten on the first run with the previous tape
reproduced exactly; every probe suite and every gate green in one chain, the sweep whole. Next: the commit on your word; then chapter 7's reading — or
the schema sitting first, on your word.
"""

# ---- 7. THE_BRIEFING ----
BRIEF_BULLET_ANCHOR = "- **CHAPTER 6 READ AND FROZEN — THE SHEMA:"
BRIEF_BULLET = ("- **CHAPTER 6 COMPILED — THE SHEMA'S LAW GIVEN AT ITS OWN DAY FOR THE FIRST TIME, THE READBACK'S THIRD FORM (A RETELLING INSIDE A LAW), THE RECEIPT WITHOUT THE NAME THE GATE CANNOT SEE, AND THE WHOLE-ROW RULE RULED AND PAID INSIDE THE SITTING** "
                "(2026-09-17, on your \"Go\", \"Next go\" and \"Ok go\"; World/step9/DEUTERONOMY_WALK.md \"Sitting 4b\" + AS BUILT): cold_run_hear_o_israel.py the 61st runner (42/42), law_hear_o_israel the 66th daemon (%d functions); the readback's seven rows; the tape 10/10 on its first run with RUN (1304, 96, 88, 0, 12, 1595, 37, 319, pairs, 127) as predicted, markers 167; the docket 747 rows every one read whole; every gate GREEN, the sweep %d/61. NEXT: the commit on your word; chapter 7's reading, or the schema sitting first.\n" % (DG[1], SW_P))
BRIEF_ENTRY_ANCHOR = "### 2026-09-17 — THE WHOLE-ROW RULE: NO CUT ON THE SHELF, EVER\n"
BRIEF_ENTRY = """### 2026-09-17 — CHAPTER 6 COMPILED: THE SHEMA GIVEN AT ITS OWN DAY, AND THE READBACK'S THIRD FORM

Every chapter so far had its law compiled somewhere already, or told of acts already on the tape. Chapter 6 is the first whose law had no cell anywhere:
the recitation, the teaching, the tefillin, the mezuzah — the Shema — were read at the last sitting and are compiled here for the first time, and they
are given at the day Moses speaks them, not carried back to Sinai, because nothing on the tape gave them before. The Talmud's answer sheets on them are
long (Berakhot's first three chapters, Menachot's pages on the straps and the boxes, Yoma's on the gates), and one of them turned out to count from
the text's spellings a number the stored text does not support: the four compartments of the head's box. The cell returns four because the tradition
teaches four, and the row that shows the spelling stands open. The readback grew its third form: the chapter tells a father what to answer his son
about the exodus, so the answer is a retelling inside a law — graded against the tape like Moses' own retellings, but by the law's own cell, and the
Talmud itself says the first clause of the Passover telling is this chapter's verse. One small receipt, "as He commanded us", has no Name in it, and
the gate that finds receipts cannot see it — measured, asserted, and owed to a sitting on the gate. In the middle of this sitting you ruled that no row
of the Talmud is ever read cut; the docket was reread whole, seventy rows corrected, and the earlier dockets reread where a shortcut had been taken —
one cell of chapter 4 had been typed from the Talmud's challenge instead of its answer, and was retyped. The runner matched its sheet on the first run,
the tape reached ten of ten on the first run with the previous tape reproduced exactly, and every gate is green in one chain. Next, on your word: the
commit, then chapter 7 — or the schema question first.

"""

# ---- 8. THE_LOOP step-6 row ----
LOOP_OLD = "readback_probes 12/12, CI4-CI6) | the laws' half BUILT at chapter 5 (3b); the second pass after Deuteronomy |"
LOOP_NEW = ("readback_probes 12/12, CI4-CI6); cold_run_hear_o_israel.py (chapter 6, THE THIRD FORM BUILT 2026-09-17 — a retelling INSIDE A LAW: the son's answer's rows graded against the tape by the cell that compiles the duty to answer (T1); seven rows VERBATIM 3 / EXPANDED 3 / SHORTENED 1; "
            "readback_probes 15/15, CO4) | the three forms BUILT — acts (1b), laws (3b), a retelling inside a law (4b); the second pass after Deuteronomy |")

# ---- 9. RESUME ----
RESUME_HEAD = """# ⚠ THE DEUTERONOMY WALK sitting 4b (2026-09-17; step9/DEUTERONOMY_WALK.md "Sitting 4b" + "Sitting 4b — AS BUILT"): CHAPTER 6 COMPILED —
# step9/cold_run_hear_o_israel.py the 61st runner (42/42; six cells; the readback's third form — seven rows, a retelling inside a law), law_hear_o_israel
# the 66th daemon (given_at Deut 6:4, boot); THE SHEMA'S LAW compiled for the first time and given at the chapter's own day (40, 11, 1), NO marker —
# shema_commanded a status, test_barred a block on Israel; the receipt without the Name (6:25) a pointer, the gate's finder blind (asserted); the
# compartments FOUR a parameter over the spellings' open row; the tape 10/10 on its first run with RUN (1304, 96, 88, 0, 12, 1595, 37, 319, pairs, 127)
# as predicted, PREVIOUS_RUN 3b's exactly, markers 167, closes 127; THE WHOLE-ROW RULE (2026-09-17) ruled inside the sitting — the docket's 747 rows
# read whole, the older cuts reread, one chapter-4 cell retyped; every probe suite and gate GREEN, the sweep %d/61.
# NEXT on the ruling: the commit on the owner's word; chapter 7's reading (7:1-26) — or the schema sitting first, on his word.
""" % SW_P

# ---- 10. THE STATE DOC — #193 ADDENDUM 1 ----
STATE_ADD = """
#193 ADDENDUM 1 (2026-09-17, at the close of THE DEUTERONOMY WALK sitting 4b — THE COMPILE OF CHAPTER 6, RUN 4 of four — A CLEAN COMPACTION POINT): THE
SITTING RAN IN FOUR RUNS on the owner's "Go" (RUN 1 — #190 addendum 5), "One more run" (RUN 2 — #190 addendum 6, the compaction #191), the whole-row
rule and its fix between (#191 addenda 1-3, #192 addendum 1), "Next go" (RUN 3 — #192 addendum 2, the compaction #193) and "Ok go" (RUN 4 — this):
the gates chain in one summary (run twice — the first stopped at the probes step, two probes retyped from its print: readback Q13's key,
large_letter H5's moved exhibit; the second from that step ALL GREEN), the records from the sheet in one call, the forms copied; the map's "Sitting 4b
— AS BUILT" is the record (the nine departures, the eleven lessons, the gates computed from their prints). THE STATE: cold_run_hear_o_israel.py the 61st runner (42/42), law_hear_o_israel the
66th daemon (%d daemons, %d functions), the registries 1125 kinds / 1025 effects, the tape 10/10 with RUN (1304, 96, 88, 0, 12, 1595, 37, 319, the four
pairs, 127) and PREVIOUS_RUN 3b's exactly, markers 167 (F 129 / P 15 / R 23), entities 319, closes 127, the population table 148; the docket
logic/oral_triage/deu_06_vaetchanan_exam_2026-09-17.md (%d rows, every row read whole); THE READBACK'S THIRD FORM BUILT (seven rows: VERBATIM 3,
EXPANDED 3, SHORTENED 1 — a retelling inside a law, T1); THE SHEMA'S LAW compiled for the first time at the chapter's own day, statute by form; the
receipt without the Name a pointer with the finder's blindness asserted; the corpus unmoved (220 units, standing 2203, hash 8b8fff1fa28953af — no freeze
this sitting). THE GATES: the probe suites %s; %s. THE RECORDS written: the map's AS BUILT, COMPILE_DEBT (the sitting-4 box PAID; the 4b box with six
owed items), MIDDOT's docket entry (eighteen rules about rules), MISHNAH_TOPICS (seventeen rows), RESEARCH_LOG, THE_STEPS, THE_BRIEFING (the bullet and
the entry), THE_LOOP's step-6 row (the three forms), World/RESUME.md, the recovery page rewritten, the addenda's section 40, RECORD_FORMS' pointer, memory
(deuteronomy-walk.md, MEMORY.md under 17,000 bytes); the forms copied by copy_ch6b_forms.py. NOT COMMITTED (the tree uncommitted since a7955cc — the
owner's word only; NOT PUSHED); the commit message drafted at <scratch>/commit_msg_ch6b.txt. NEXT ON THE RULING: the commit on the owner's word; then
CHAPTER 7's reading (7:1-26 — the seven nations and the ban, the chosen people; the reading shape in four runs, every row whole) — or the
Decalogue-schema sitting first (ON THE TABLE, not a ruling). IF THIS COMPACTS HERE: reread the recovery page, the map's "Sitting 4b — AS BUILT" and
MEMORY.md; nothing is mid-flight.
""" % (DG[0], DG[1], NROWS, pr_line, gates_line)

# ---- 11. THE RECOVERY ADDENDA — section 40 ----
ADDENDA_ADD = """

## 40. ADDENDUM (2026-09-17, THE DEUTERONOMY WALK sitting 4b — THE COMPILE OF CHAPTER 6, Deuteronomy 6:1-25 COMPILED AND ON THE TAPE in four runs; the owner: "Go", "One more run", "Next go", "Ok go"; the state doc's #193 addendum 1)

THE SITTING RAN IN THE COMPILE SHAPE IN FOUR RUNS (section 5; "Sitting 3b" the form; the whole-row rule of §39 ruled between its runs 2 and 3 and paid
inside it): World/step9/DEUTERONOMY_WALK.md "Sitting 4b" (the design, written before any code) and "Sitting 4b — AS BUILT" (the departures and the
ten lessons). THE STATE: cold_run_hear_o_israel.py the 61st runner (42/42 — six cells, eighteen DATA rows, the readback's seven rows, fourteen exam
persons), law_hear_o_israel the 66th daemon (given_at Deut 6:4, installed_by boot; %d daemons, %d functions), event_vocabulary +3 (1125), effect_vocabulary
+2 (1025), dependency_dispositions +12 edges +4 pointers (%d edges, %d pointers on file); THE TAPE 10/10 WITH THE REST ON ITS FIRST RUN — RUN (1304, 96,
88, 0, 12, 1595, 37, 319, the four pairs, 127) as predicted, PREVIOUS_RUN 3b's EXACTLY (no declared delta), NEWEST_RUNNER hear_o_israel, markers 167
UNMOVED, entities 319, closes 127, the population table 148, CO1-CO9 MATCH; the docket logic/oral_triage/deu_06_vaetchanan_exam_2026-09-17.md (%d rows —
link %d / topic %d; LAW %d; credited %d; EVERY ROW READ WHOLE). THE GATES: the probe suites %s; %s.

WHAT THE SITTING FOUND (RESEARCH_LOG 2026-09-17, the compile entry): THE READBACK'S THIRD FORM — a retelling inside a law, the grades the cell's verdicts
(T1), the shelf's own seat at Pesachim 116a; THE SHEMA'S LAW compiled for the first time at the chapter's own day, STATUTE BY FORM (the stitcher's
register test); THE RECEIPT WITHOUT THE NAME — the finder blind at 6:25, asserted by calling it; THE COMPARTMENTS A PARAMETER over the spellings' open
row; THE CENSUS AND A HOMOGRAPH ("eat" at 6:11 FALSE; the oath's pointers not demanded); THE WHOLE-ROW MEASURE (one verdict in ten wrong at 170
characters; a cut row ends before the answer). THE ELEVEN LESSONS in the map's AS BUILT (the eleventh from the gates step: two probes retyped from the
chain's first print — Q13's key, H5's exhibit moved by the tape's growth).

THE FILES CHANGED BY 4b: World/step9/cold_run_hear_o_israel.py (new), cold_run_sequence.py (the two lines under "# ---- Deut 6 ----", the literals,
CO1-CO9), cold_run_obey_horeb.py (the fifth-compartment cell retyped under the rule), event_vocabulary.yaml, effect_vocabulary.yaml,
daemon_dispositions.yaml, dependency_dispositions.yaml (the span, twelve edges, four pointers), readback_probes.py (Q13-Q15; Q13 retyped at RUN 4),
large_letter_probes.py (H5 retyped — the creed classed, the hypothesis parked), installation_probes.py (I5 66), checkpoint_positions.yaml (rebuilt — 235), DAEMON_INDEX.md and DEPENDENCY_INDEX.md (regenerated), the docket (new; rewritten whole), the four
appended REREAD WHOLE sections (the chapter-6 ledger, the 3b, 2b and 1b dockets), the forms folder (copy_ch6b_forms.py), the records (the map, COMPILE_DEBT,
MIDDOT, MISHNAH_TOPICS, RESEARCH_LOG, THE_STEPS, THE_BRIEFING, THE_LOOP, RESUME, RECORD_FORMS, the recovery page, this file, the state doc, memory).
NOT COMMITTED — the tree uncommitted since a7955cc; commit on the owner's word only.

NEXT ON THE RULING: the commit on the owner's word; then CHAPTER 7's READING (7:1-26 — the seven nations and the ban, the chosen people, the reward; the
reading shape in four runs, every row whole). ON THE TABLE, NOT A RULING: the Decalogue-schema sitting — on the owner's word.
""" % (DG[0], DG[1], DP[0], DP[1], NROWS, NLINK, NTOPIC, VD['LAW'], NCRED, pr_line, gates_line)

# ---- 12. THE RECOVERY PAGE — rewritten whole under its cap (section 2 replaced; sections 4, 5, 6 retouched) ----
def f_recovery(s):
    i = s.index('## 2. WHERE IT STANDS'); j = s.index('## 3. THE STANDING LAWS')
    sec2 = """## 2. WHERE IT STANDS (2026-09-17, after sitting 4b — chapter 6's compile; the state doc #193 addendum 1)
- NUMBERS CLOSED. DEUTERONOMY 1:1-6:25 READ, FROZEN, COMPILED AND ON THE TAPE (sittings 1-4b).
- 220 frozen units, standing 2203, hash 8b8fff1fa28953af. 61 runners, 66 daemons, %d functions; registries 1125 kinds / 1025 effects.
- THE TAPE at RUN (1304, 96, 88, 0, 12, 1595, 37, 319, the four pairs, 127), markers 167, closes 127, the counter (40, 11, 1); the sweep %d/61;
  every gate GREEN; the register gate DECLARED %d / DEBT 0 (no seat in chapter 6 — the finder blind to 6:25, its third form owed to a gate sitting).
- THE READBACK'S THREE FORMS BUILT (acts 1b, laws 3b, a retelling inside a law 4b). THE WHOLE-ROW RULE ruled and its fix (a)-(d) paid inside 4b.
- LAST COMMIT a7955cc (2026-09-17, NOT pushed): sitting 4. Uncommitted: 4b whole, the rule and its fix, one chapter-4 cell retyped.
- NEXT ON HIS WORD: the commit; then CHAPTER 7's reading (7:1-26) — or the schema sitting first (on the table, not a ruling).

""" % (DG[1], SW_P, RG[0])
    s = s[:i] + sec2 + s[j:]
    old4 = "(60 runners;\ncold_run_covenant_at_horeb.py the newest form)"; assert s.count(old4) == 1, s.count(old4)
    s = s.replace(old4, "(61 runners;\ncold_run_hear_o_israel.py the newest form)")
    old5 = 'the newest instances: the map\'s "Sitting 4" and "Sitting 3b")'; assert s.count(old5) == 1
    s = s.replace(old5, 'the newest instances: the map\'s "Sitting 4" and "Sitting 4b")')
    old6 = "- Deuteronomy's sittings: the map; the addenda §31-38. The cost cuts: §35."; assert s.count(old6) == 1
    s = s.replace(old6, "- Deuteronomy's sittings: the map; the addenda §31-40 (§39 the whole-row rule). The cost cuts: §35.")
    old2b = "(the sheet RECORD_FORMS.md names them); MEMORY.md under 17,000 bytes; this page rewritten."
    assert s.count(old2b) == 1
    assert len(s.encode('utf-8')) <= 10240, ('THE RECOVERY PAGE OVER ITS CAP', len(s.encode('utf-8')))
    return s

# ---- 13. MEMORY ----
MEM_DESC_OLD = 'SITTING 4 DONE 2026-09-17 (chapter 6 READ AND FROZEN'
MEM_PARA = """

SITTING 4b DONE 2026-09-17 (the owner: "Go", "One more run", "Next go", "Ok go" — four runs, the compactions #191 and #193 between; the map's "Sitting
4b" + AS BUILT): CHAPTER 6 COMPILED — cold_run_hear_o_israel.py the 61st runner (42/42), law_hear_o_israel the 66th daemon (given_at Deut 6:4, boot).
THE SHEMA'S LAW compiled for the first time and given at the chapter's own day (40, 11, 1) with NO marker — two lines STATUTE by form (the stitcher's
register test; 2b's lesson), shema_commanded a status and test_barred a block on Israel. THE READBACK'S THIRD FORM (T1): a retelling inside a law —
the son's answer's rows graded by the cell that compiles the duty to answer; seven rows VERBATIM 3 / EXPANDED 3 / SHORTENED 1; the shelf's own seat
Pesachim 116a. The receipt without the Name (6:25) a RUN_CITATION pointer, the register gate's finder blind (asserted by CALL at CO6; the third form
owed to a gate sitting). The compartments FOUR a parameter over the spellings' open row. The tape 10/10 on its FIRST run with RUN (1304, 96, 88, 0, 12,
1595, 37, 319, pairs, 127), PREVIOUS_RUN 3b's exactly, markers 167; the docket 747 rows EVERY ROW READ WHOLE (the rule ruled mid-sitting; 70 corrected);
every gate green, the sweep 61/61. ⚠ LESSONS: the own-day giving of a law is statute by form; the design's pointer list is a prediction — the census
decides (four AS_WHEN pointers; the oath's three not demanded; "eat" at 6:11 a homograph FALSE); the tape first, then the fast check, when the tape
grows; the print first, then the assert; a forms copy is portable, a scratch derivation is not (derive_form.py); YAML's FALSE is a boolean; a cut row
ends before the answer; a probe written before the runner is retyped once to its shape (Q13) and a hypothesis's exhibit moves when the tape grows (H5 —
the chain's first FAIL read, the chain rerun from the failed step). NOT COMMITTED (since a7955cc). NEXT on the ruling: the commit; chapter 7's reading (7:1-26) or the schema sitting.
"""
MEM_IDX_OLD = "chapters 1-6 READ, 1-5 COMPILED (a7955cc); 4b RUNS 1-3 DONE (docket 747, runner 42/42, tape 10/10); NEXT: RUN 4 gates, records, forms, commit"
MEM_IDX_NEW = "chapters 1-6 READ AND COMPILED (4b DONE 2026-09-17, four runs; uncommitted since a7955cc); NEXT: the commit on his word, then chapter 7's reading"

# ---- 14. RECORD_FORMS — the writer's form pointer ----
FORMS_OLD = "World/step9/forms_deuteronomy_walk/write_ch4b_records.py. Keep this sheet current"
FORMS_NEW = "World/step9/forms_deuteronomy_walk/write_ch6b_records.py (write_ch5b_records.py and write_ch4b_records.py the earlier forms). Keep this sheet current"

# ---- THE WRITES (every text built above; the files opened only now) ----
def read(p): return open(p if p.startswith('/') else f'{ROOT}/{p}', encoding='utf-8').read()
def write(p, s): open(p if p.startswith('/') else f'{ROOT}/{p}', 'w', encoding='utf-8').write(s)
plans = []
plans.append(('World/step9/DEUTERONOMY_WALK.md', lambda s: s.rstrip('\n') + '\n' + AS_BUILT))
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
    assert s.count(BRIEF_BULLET_ANCHOR) == 1 and s.count(BRIEF_ENTRY_ANCHOR) == 1 and '## SCOREBOARD (as of 2026-09-17, latest)\n' in s, (s.count(BRIEF_BULLET_ANCHOR), s.count(BRIEF_ENTRY_ANCHOR))
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
    s = s.replace(MEM_DESC_OLD, 'SITTING 4b DONE 2026-09-17 (chapter 6 COMPILED — the Shema\'s law at its own day; the readback\'s third form; the whole-row rule ruled and paid inside it; uncommitted); ' + MEM_DESC_OLD, 1)
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
