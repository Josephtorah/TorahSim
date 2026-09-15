import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE NUMBERS WALK 7b — the closing records, every anchor asserted; the sweep's numbers READ from run_cold_all's own print (never typed).
import re, os, subprocess
ROOT = _ROOT; SCR = os.path.dirname(os.path.abspath(__file__)); MEM = '<memory>'
sweep = open(f'{SCR}/balak_sweep1.out', encoding='utf-8').read()
m = re.search(r'run_cold_all: (\d+)/(\d+) runners green, (\d+) graded cells in all', sweep)
assert m and 'sweep exit 0' in sweep, 'the sweep has not finished green'
NR, ND, CELLS = int(m.group(1)), int(m.group(2)), int(m.group(3))
assert NR == ND == 49 and CELLS == 5613 + 105, (NR, ND, CELLS)
unc = subprocess.run(['git', 'status', '--porcelain'], cwd=ROOT, capture_output=True, text=True).stdout
NUNC = len([l for l in unc.splitlines() if l.strip()])
def rw(p, f):
    t = open(p, encoding='utf-8').read(); t2 = f(t); assert t2 != t, p; open(p, 'w', encoding='utf-8').write(t2)
# ---- NUMBERS_WALK.md: the as-built ----
asb = open(f'{SCR}/balak_asbuilt.md', encoding='utf-8').read()
gates = ('THE PROBE GATES: installation 6/6 (I5 54), clock 22/22, sequence 4/4, cursor 6/6, view 6/6, journal 6/6. THE JOURNAL GATE GREEN (the index over 4 segments 11,810 rows, the running world\'s counts matching the RUN tuple). THE SWEEP run_cold_all.py: %d/%d runners green, %s graded cells (6b\'s 5,613 + Balak\'s 105), the daemon and dependency gates first.' % (NR, ND, f'{CELLS:,}'))
assert asb.count('THE PROBE GATES and THE JOURNAL GATE: below.') == 1
asb = asb.replace('THE PROBE GATES and THE JOURNAL GATE: below.', gates)
asb += '\nNEXT on the ruling: CHAPTER 26 — the second census\'s reading (26:1-65, with 25:19\'s half-verse and its marker "after the plague"; Simeon\'s 22,200 the checkpoint the plague set), THEN its compile — never the next reading first.\n'
def f_walk(t):
    assert t.rstrip().endswith('COMPILE_DEBT\'s sitting-7b box paid, the state doc, THE_STEPS, THE_BRIEFING, RESUME, memory).') and '## Sitting 7b — THE COMPILE OF BALAK, AS BUILT' not in t
    return t.rstrip('\n') + '\n' + asb
rw(f'{ROOT}/World/step9/NUMBERS_WALK.md', f_walk)
# ---- THE_STEPS.md: the walk paragraph ----
def f_steps(t):
    a = '## THE FINDINGS LOOP + THE STAMP LAW (owner-approved 2026-08-31)'
    assert t.count(a) == 1 and 'SITTING 7b — THE COMPILE OF BALAK' not in t
    par = ('SITTING 7b — THE COMPILE OF BALAK (Numbers 22:1-25:19, 2026-09-11, on Brian\'s "Go" after the #131 rereads; World/step9/NUMBERS_WALK.md "Sitting 7b"\n'
           'design + as-built): the exam docket 199 rows by the union rule (67 laws; the Balaam sugya — the Talmud\'s case discussion — read whole,\n'
           'Sanhedrin 105a-106b, with the Jerusalem Talmud\'s two law-sections); the parser taught the plene "three" (22:32) and the construct "thousands\n'
           'of" (Exod 32:28\'s 3,000, read 3 since the first day) — 159/159 probes, the corpus diff moving the four probed verses alone; cold_run_balak.py\n'
           '105/105 on the first graded run, twelve engines called live (the spec of Exod 34:15-16 at its Peor run, the judges\' 78,600, Aaron\'s incense\n'
           'clause at the spear, the priesthood\'s addressees with Phinehas the exception, the wood-gatherer\'s court for the hanging); law_balak the 54th\n'
           'daemon with THE ZEALOTS\' RULE INSTALLED BY A DEED (rule_installed on the tent at the covenant\'s output — THE TENT\'s form at a second seat, no\n'
           'halt and no docket); the forty-one lines on the tape with no marker (the stretch undated), RUN matched on the second tape run after two\n'
           'readings — a close without a value takes the FIRST open entry of that effect (Korach\'s plague, left open by its daemon — a filed debt) and\n'
           'a status can never close (the act in progress is a BODY entry); THE REST 6b\'s exactly; CL1-CL9 all MATCH; every gate green; the sweep %d/%d at\n'
           '%s cells. Numbers 1:1-25:19 read, frozen, compiled and on the tape. Next: chapter 26 (the second census) — the reading, then its compile.\n\n' % (NR, ND, f'{CELLS:,}'))
    return t.replace(a, par + a)
rw(f'{ROOT}/THE_STEPS.md', f_steps)
# ---- THE_BRIEFING.md: the scoreboard entry and the count line ----
def f_brief(t):
    a = '## SCOREBOARD (as of 2026-09-11, latest)\n'
    assert t.count(a) == 1 and 'BALAK COMPILED — SITTING 7b DONE' not in t
    entry = ('- **BALAK COMPILED — SITTING 7b DONE: THE ZEALOTS\' RULE ENTERS THE TAPE BY A DEED, THE PARSER READS THE PLENE THREE AND THE CALF\'S THREE THOUSAND, AND A CLOSE WITHOUT A NAME TOOK ANOTHER RUNNER\'S OPEN PLAGUE** '
             '(2026-09-11, on your "Go" after the #131 rereads; World/step9/NUMBERS_WALK.md "Sitting 7b"). The exam docket 199 rows by the union rule — the whole Balaam discussion of Sanhedrin 105a-106b and the Jerusalem Talmud\'s two law-sections read row by row; '
             'the parser taught two rules (22:32\'s vav-spelled "three"; Exod 32:28\'s "about three thousands of men" = 3,000 — read 3 since the parser\'s first day), 159/159 probes, the corpus diff moving exactly the four probed verses; '
             'cold_run_balak.py 105/105 on its first graded run with twelve engines called live — the covenant\'s "lest you whore after their gods" clause runs at Shittim, the judges of 25:5 are Jethro\'s 78,600 (each executing two, the Jerusalem Talmud\'s 157,200), '
             'Aaron\'s "and the plague was stayed" at Phinehas\'s spear, Phinehas not a priest until the deed (Zevachim 101b) — the priesthood engine\'s "sons of Aaron" row his named exception; '
             'THE ZEALOTS\' RULE ("one who cohabits with an Aramean woman, zealots strike him" — with its four limits: during the act, self-defense, not taught, a law from Sinai) installed on the tent BY THE DEED and ratified by the covenant — THE TENT\'s form at a second seat with no halt and no docket; '
             'the forty-one lines on the tape undated (no marker: the ink and Seder Olam give no day), RUN matched on the second run after two honest reads — the engine\'s close without a value closed KORACH\'S plague (17:8-15, never closed by its daemon: a filed debt) and a status entry cannot close at all (Zimri\'s act in progress retyped a BODY entry); '
             'THE REST reproduced 6b exactly; nine checkpoints MATCH; every gate green; the sweep %d/%d runners at %s cells. Numbers 1:1-25:19 read, frozen, compiled and on the tape; next chapter 26, the second census.\n' % (NR, ND, f'{CELLS:,}'))
    t = t.replace(a, a + entry)
    b = '53 daemons; the sweep 48/48 runners green at 5,613 cells; Numbers 1:1-25:19 read and frozen, 1:1-21:35'
    assert t.count(b) == 1, t.count(b)
    t = t.replace(b, '54 daemons; the sweep %d/%d runners green at %s cells; Numbers 1:1-25:19 read, frozen, compiled and on the tape, 1:1-21:35' % (NR, ND, f'{CELLS:,}'))
    return t
rw(f'{ROOT}/THE_BRIEFING.md', f_brief)
# ---- World/RESUME.md ----
def f_resume(t):
    assert 'SITTING 7b DONE' not in t
    return t.rstrip('\n') + '\nSITTING 7b DONE 2026-09-11 (THE COMPILE OF BALAK; NUMBERS_WALK.md "Sitting 7b" design + as-built): the docket 199 rows (67 LAW); the parser taught the plene "three" and the construct "thousands of" (159/159; the diff moved the four probed verses alone); cold_run_balak.py 105/105 first graded run, twelve engines CALLED; law_balak the 54th daemon, the zealots\' rule installed by the deed (rule_installed on the tent at 25:10-13); the forty-one lines on the tape with no marker, RUN (1239, 52, 52, 0, 12, 1465, 25, 302, four pairs, 113) matched on the second tape run (the first-open close took Korach\'s open plague — filed; a status cannot close — the act retyped BODY); THE REST 6b\'s exactly; CL1-CL9 MATCH; the gates green; the sweep %d/%d at %s cells. NUMBERS 1:1-25:19 READ, FROZEN, COMPILED AND ON THE TAPE. NEXT: chapter 26 (the second census) — the reading, then its compile.\n' % (NR, ND, f'{CELLS:,}')
rw('<world-link>/RESUME.md', f_resume)
# ---- memory: numbers-in-order-ruling.md ----
def f_rule(t):
    a = '; NEXT the compile of Balak (7b), then chapter 26"'
    assert t.count(a) == 1
    t = t.replace(a, '; SITTING 7b DONE 2026-09-11 (the compile: 105/105 first graded run; rules 21-22 the plene three and the construct thousands-of; the zealots\' rule installed by a deed; no marker; RUN matched on the second tape run — the first-open close and a status that cannot close; the sweep %d/%d at %s); NEXT chapter 26 (the second census) — the reading, then its compile"' % (NR, ND, f'{CELLS:,}'))
    b = 'Related: [[the-loop-ruling]], [[step9-exam-era]], [[spine-default]].'
    assert t.count(b) == 1
    par = ('SITTING 7b DONE 2026-09-11 — THE COMPILE OF BALAK (NUMBERS_WALK.md "Sitting 7b" design + as-built; COMPILE_DEBT\'s sitting-7 box PAID): the docket 199\n'
           'rows by the union rule (Sanhedrin 105a-106b whole, the Jerusalem Talmud\'s Taanit 4:5 and Sanhedrin 10:2 by address; 67 LAW); the parser taught THE PLENE "THREE"\n'
           '(22:32; Deut 16:16, 19:2) and THE CONSTRUCT "THOUSANDS OF" (Exod 32:28 = 3,000; the bare construct silent at 10:36, Deut 33:17) — 159/159, the diff moving the four\n'
           'probed verses alone; cold_run_balak.py 105/105 first graded run (five cells; twelve engines CALLED — the spec of Exod 34:15-16 at its run, the judges\' 78,600, the\n'
           'incense clause, the priesthood\'s addressees, the hanging, the tellers, the total, Isaac\'s clauses, Judah\'s lion, the ladder, the idolatry principle, the olah the\n'
           'census demanded); law_balak the 54th daemon — THE ZEALOTS\' RULE INSTALLED BY A DEED (rule_installed on the tent at 25:10-13: THE TENT\'s form at a second seat, no\n'
           'halt and no docket), three closes its own; the tape\'s forty-one lines page_order at (40, 6, 1), no marker; RUN (1239, 52, 52, 0, 12, 1465, 25, 302, four pairs, 113)\n'
           'matched on the SECOND tape run (the first read: the SLOTS literal not retyped from the stitcher\'s print; a close without a value took KORACH\'S open plague of\n'
           '17:8-15 — closed by value now, the Korach entry a filed debt; Zimri\'s act a STATUS that cannot close — retyped BODY); THE REST 6b\'s exactly; CL1-CL9 MATCH; the\n'
           'probe gates and the journal gate GREEN; the sweep %d/%d at %s. NUMBERS 1:1-25:19 READ, FROZEN, COMPILED AND ON THE TAPE. UNCOMMITTED since 0a98276. NEXT:\n'
           'CHAPTER 26 — the second census\'s reading (26:1-65 with 25:19\'s half-verse as its marker; Simeon\'s 22,200 the plague\'s checkpoint), THEN its compile — never the\n'
           'next reading first.\n' % (NR, ND, f'{CELLS:,}'))
    return t.replace(b, par + b)
rw(f'{MEM}/numbers-in-order-ruling.md', f_rule)
# ---- memory: MEMORY.md (the bullet, kept under the size limit) ----
def f_index(t):
    a = "SITTING 7 DONE 2026-09-11 — 22:1-25:19 READ AND FROZEN (Balak, with the drafts' own edges 22:1 and 25:10-19: 120 sources, 40 claims, 200 units, standing 2063, hash unmoved; the Sifrei's one piska 131 on 25:1, none on 22-24; the plene three a new parser gap, the calf's 3,000 found read 3; the export joins 25:19 into 26:1; twelve asserts fell on the marks' order — NFC on both sides). ALL UNCOMMITTED since 0a98276. NEXT the compile of Balak (7b), then chapter 26 (the second census) — never the next reading first."
    assert t.count(a) == 1
    b = ("SITTING 7 DONE 2026-09-11 — 22:1-25:19 READ AND FROZEN (120 sources, 40 claims, 200 units, standing 2063; the export joins 25:19 into 26:1; NFC on both sides). "
         "SITTING 7b DONE 2026-09-11 — BALAK COMPILED AND ON THE TAPE (105/105 first run; the plene three and the construct thousands-of taught; the zealots' rule installed by a DEED; no marker; RUN (1239, 52, 52, 0, 12, 1465, 25, 302, four pairs, 113) matched second tape run — a close without a value takes the FIRST open entry (Korach's plague, filed) and a STATUS cannot close; 54 daemons; the sweep %d/%d at %s). ALL UNCOMMITTED since 0a98276. NEXT chapter 26 — the second census's reading (25:19 its marker), THEN its compile — never the next reading first." % (NR, ND, f'{CELLS:,}'))
    return t.replace(a, b)
rw(f'{MEM}/MEMORY.md', f_index)
assert os.path.getsize(f'{MEM}/MEMORY.md') < 17400, os.path.getsize(f'{MEM}/MEMORY.md')
# ---- memory: step9-exam-era.md (the lesson paragraph first under the standing lessons) ----
def f_lessons(t):
    a = '## STANDING LESSONS AND WATCHES (moved verbatim from the MEMORY.md index line on 2026-09-07 to keep the index under its size limit; the W4/W3/W2/W1/D9/G/E lesson tail as it stood)\n'
    assert t.count(a) == 1 and 'sitting 7b — THE COMPILE OF BALAK' not in t
    par = ("⚠ THE NUMBERS WALK sitting 7b — THE COMPILE OF BALAK (2026-09-11): A CLOSE WITHOUT A VALUE CLOSES THE FIRST OPEN ENTRY OF THAT EFFECT ON THE TAPE — law_balak's 'the plague was stayed' took KORACH'S plague entry (17:8-15, left open by law_korach at 17:13) and left Peor's open; NAME the entry by VALUE and close by value (O8 S1's frogs lesson relearned; Korach's open plague a filed debt). A STATUS OP CANNOT CLOSE — the engine opens debit / heaven / body entries only: an act in progress the text ENDS (Zimri's, ended by the spear) is a BODY entry. THE DAEMON GATE READS LITERAL SUBMITS ONLY — a narrative written as a loop over a list of dicts reads as '?UNRESOLVED?' with every kind 'submitted on NO tape' while the recorder captured them all: two instruments, two views (5b's parser lesson at the narrative's seat). THE SLOTS LITERAL IS TYPED FROM THE STITCHER'S PRINT LIKE THE CENSUS (morning +3 printed, not retyped — the first tape run's miss). THE ASSERT DRIVER BEFORE THE RUN, AGAIN — four typed facts fell at once (the atonement verb's third seat 8:21; the stayed verb's two; the shelach ask's home in its error cell; the block's open flag False — a block is never opened, 6b's lesson applied the wrong way round). THE MEASUREMENT PASS ON THE PROBE TOKENS before the runner is typed (six of the hand's forms fell: the plene plains, 'but only' with its vav, 'from your existence', 'alone' with its lamed, 'and the shout of', 'the judges of'). THE PARSER'S GAP WAS NOT WHERE THE READING NAMED IT — the approximation prefix read right (Exod 12:37); the missing word was the construct plural 'thousands of' — measure the class before typing the rule. THE DEPENDENCY CENSUS DEMANDS EDGES THE DESIGN DID NOT LIST (the olah at four verses) and names homographs to FALSE (the talion's 'under', Molech's 'king').\n")
    return t.replace(a, a + par)
rw(f'{MEM}/step9-exam-era.md', f_lessons)
# ---- the state doc: COMPACTION POINT #132 ----
def f_state(t):
    assert 'COMPACTION POINT #132' not in t and t.rstrip().endswith("PLAGUE-COUNT CROSS-CHECK'S CALF GAP (a probe to FAIL at 7b).")
    cp = ('\n═══ COMPACTION POINT #132 (2026-09-11 — written at THE NUMBERS WALK sitting 7b\'s close; BALAK COMPILED AND ON THE TAPE; NUMBERS 1:1-25:19 READ, FROZEN, COMPILED AND ON THE TAPE) ═══\n'
          'STATE: 200 frozen units, standing 2063, hash 8b8fff1fa28953af UNMOVED (no unit touched this sitting); 49 runners, 54 daemons (law_balak the 54th), the sweep %d/%d at %s graded cells (6b\'s 5,613 + Balak\'s 105); the journal gate GREEN; every probe gate green (installation 6/6 with I5 54, clock 22/22, sequence 4/4, cursor 6/6, view 6/6, journal 6/6).\n'
          'THE COMPILE (NUMBERS_WALK.md "Sitting 7b" design + as-built; COMPILE_DEBT\'s sitting-7 box PAID): the docket logic/oral_triage/num_22_25_balak_exam_2026-09-11.md — 199 rows by the union rule (88 link rows in 24 works; Sanhedrin 105a-106b whole; Mishnah Sanhedrin 7:6, 9:6, 10:1-2; Avot 5:6, 5:19; the Jerusalem Talmud\'s Taanit 4:5 and Sanhedrin 10:2 by address; 67 LAW, 7 DISPUTE, 30 DERIVATION, 95 CONTEXT; 20 credited with a quick look; the twenty-four other folios sized); the parser taught rules 21 (the plene "three" — שלוש with the vav = 3) and 22 (the construct "thousands of" after a unit multiplies; bare it is a noun) — census_probes 159/159 after J1-J4 failed first, the corpus diff (5,853 verses) moving exactly the four probed; cold_run_balak.py (949 lines): the guard 105, 96 probes, five cells (the_call 18 asks, the_ass_and_the_angel 13, the_stands 35, peor 23, phinehas_and_midian 17), 38 DATA rows, 105/105 ON THE FIRST GRADED RUN after the assert driver read four typed facts at once; twelve engines CALLED (erection, exodus_story, korach, mekoshesh, priesthood, chukat, bamidbar, mamre, family, primeval, shelach, and offerings — the edge the census demanded); the scene 39 slots predicted and matched first run; the narrative rewritten as literal submits for the gate; two declarations amended at the code step; the dependency gate\'s seven demands read (the olah CALL; the talion and Molech homographs FALSE; three AS_WHEN pointers INTERNAL).\n'
          'THE TAPE: the recorder 49 modules, balak 41 HISTORY / 30 case; the stitcher\'s CENSUS (2119, 1246, 1239, 857, 6, 10, 7, 0, 71, 156, 124, 15, 17, 784, 265) typed from its print; NO MARKER (the stretch undated in the ink and on the shelf — every line page_order at (40, 6, 1) between the og_smitten line and the daughters\' marker); RUN (1239, 52, 52, 0, 12, 1465, 25, 302, the four pairs, 113) PREDICTED AND MATCHED ON THE SECOND TAPE RUN — the first read two misses: the SLOTS literal (morning 14 -> 17 printed by the stitcher, not retyped) and closes 112 (a close without a value took KORACH\'S open plague of 17:8-15 — Peor\'s entry now carries the value the_plague_of_peor and closes by value; Zimri\'s cohabits entry a STATUS that cannot close — retyped BODY in the registry); THE REST = 6b\'s RUN exactly; CL1-CL9 all MATCH; the journal index 18,415 rows from 8 segments.\n'
          'THE RECORDS: NUMBERS_WALK.md "Sitting 7b" (design + as-built); COMPILE_DEBT.md\'s 7b PAID paragraph with the new debts (Korach\'s open plague entry — 17:13\'s close owed to law_korach; the two court debits open forever; the block; 25:19\'s marker; Simeon\'s checkpoint at 26:14; Balaam\'s death and the Midian run at Matot); RESEARCH_LOG.md\'s seven findings; MIDDOT.md\'s three entries (the zealots\' rule\'s four limits; the wine decree dated on three shelves; the retelling as the rule\'s proof); THE_STEPS, THE_BRIEFING\'s scoreboard entry and count line, World/RESUME.md, the three memory files. LAST COMMIT 0a98276; UNCOMMITTED %d paths by git status — commit only on "commit push".\n'
          'NEXT on the owner\'s word: CHAPTER 26 — THE SECOND CENSUS\'S READING (26:1-65 with 25:19\'s half-verse — the export joins it into 26:1 — and its marker "after the plague" READING-PLACED after Balak\'s undated stretch; the Sifrei\'s piska 132 at 26:53; the parser on the twelve counts, Simeon\'s 22,200 the checkpoint the plague set), THEN its compile — never the next reading first. Commit only on "commit push".\n'
          'POST-COMPACTION REREADS (mandatory, first sitting): numbers-in-order-ruling.md + this entry + NUMBERS_WALK.md "Sitting 7b — AS BUILT" (the compile\'s form) + NUMBERS_WALK.md "Sitting 7" (the reading\'s form) + THE_STEPS Step 2 + Step 5 + the compiler block; memory\'s STANDING LESSONS head (the sitting-7b paragraph first). WATCHES: as #131\'s + A CLOSE WITHOUT A VALUE TAKES THE FIRST OPEN ENTRY (name entries by value) + A STATUS CANNOT CLOSE (an act in progress is a BODY entry) + THE GATE READS LITERAL SUBMITS ONLY + THE SLOTS LITERAL FROM THE STITCHER\'S PRINT + THE ASSERT DRIVER BEFORE THE RUN + THE PROBE TOKENS MEASURED BEFORE TYPING + KORACH\'S OPEN PLAGUE (a debt line).\n' % (NR, ND, f'{CELLS:,}', NUNC))
    return t.rstrip('\n') + '\n' + cp
rw(f'{ROOT}/logic/pre_logic_methods_2026-07-28/PROMPT_continue_solo_era_2026-08-06.md', f_state)
print('records written: the walk, THE_STEPS, THE_BRIEFING, RESUME, three memory files, the state doc #132; uncommitted %d; sweep %d/%d at %d' % (NUNC, NR, ND, CELLS))
