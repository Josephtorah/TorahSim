import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE DEUTERONOMY WALK 16b (LEAN): THE CLEAN COMPACTION POINT at RUN B's end — the state doc's #216, the recovery page (section 2 under its cap, old clauses trimmed),
# the memory (the index line and the walk note) — written in ONE call after the tape is 10/10 and the gates chain is LAUNCHED; every number READ FROM ITS PRINT (the
# runner's, the tape's, the checkpoint check's, the sequence file's RUN literal, the dependency gate's, the stitcher's, the scan census's); every text built whole before a
# file is opened; the lints and the caps asserted. --check prints without writing. write_ch17b_point.py's form. RUN FROM THE REPO ROOT.
import os, re, sys, subprocess, ast, glob
ROOT = _ROOT
SP = os.path.dirname(os.path.abspath(__file__))
MEM = os.path.expanduser('~/.claude/projects/-Users-Shared-TorahSim/memory')
CHECK = '--check' in sys.argv
SD = f'{ROOT}/logic/pre_logic_methods_2026-07-28/PROMPT_continue_solo_era_2026-08-06.md'; REC = f'{ROOT}/logic/pre_logic_methods_2026-07-28/RECOVERY_new_thread_2026-09-12.md'
MM = f'{MEM}/MEMORY.md'; MW = f'{MEM}/deuteronomy-walk.md'
def rd(p): return open(p, encoding='utf-8').read()
def R(pat, text, name):
    g = re.search(pat, text, re.M); assert g, (name, pat); return g.group(1)
def RL(pat, text, name):   # the LAST match — the runner's own MATRIX line follows the callees' import-time reports in its print
    g = re.findall(pat, text, re.M); assert g, (name, pat); return g[-1]
run = rd(sorted(glob.glob(f'{SP}/ch19_runner_run*.out'))[-1]); tapes = sorted(glob.glob(f'{SP}/ch19_tape_run*.out')); tape = rd(tapes[-1]); NRUN = len(tapes); cc = rd(sorted(glob.glob(f'{SP}/ch19_checkpoint_check*.out'))[-1]); seq = rd(f'{ROOT}/World/step9/cold_run_sequence.py'); dep = rd(sorted(glob.glob(f'{SP}/ch19b_dependency_after*.out'))[-1]); st = rd(f'{SP}/seq_stitch_ch19.out'); sc = rd(sorted(glob.glob(f'{SP}/ch19_scan_census*.out'))[-1])
MATRIX = RL(r'^MATRIX: (\d+/\d+) cells match', run, 'the runner'); assert MATRIX.split('/')[0] == MATRIX.split('/')[1], MATRIX
NARR = ast.literal_eval(R(r'^THE NARRATIVE: (\(.*?\)) \(the forty-five', run, 'the narrative')); W = NARR[0]
NPAR = int(R(r'the parameters (\d+) \(in the registry', run, 'the parameters'))
RBG = R(r'^THE READBACK — THE FORMS ON FILE, NO NEW FORM: 64 rows — (\{.*?\});', run, 'the readback')
TAPE_CP = R(r'(\d+/\d+) checkpoints?', tape, 'the tape') if re.search(r'\d+/\d+ checkpoints?', tape) else R(r'checkpoints[^\n]*?(\d+/\d+)', tape, 'the tape')
assert TAPE_CP.split('/')[0] == TAPE_CP.split('/')[1], ('THE TAPE NOT AT 10/10 — the point waits', TAPE_CP)
CC_LINE = R(r'^(checkpoint_check: \d+ rows, \d+ miss, \d+ raised[^\n]*)', cc, 'the checkpoint check'); assert ', 18 miss, 0 raised' in CC_LINE, CC_LINE   # the eighteen known misses, none new; the DJ block MATCH
RUN = R(r"^RUN = \((\d+, \d+, \d+, \d+, \d+, \d+, \d+, \d+),", seq, 'RUN'); assert RUN.startswith('1362, 96, 88, 0, 12, %d, 49, 319' % (1709 + W)), RUN
DEP = R(r'^(DEPENDENCY GATE: [^\n]*)', dep, 'the dependency gate')
NDEP = R(r'dispositions on file: (\d+ edges, \d+ pointers)', dep, 'the dispositions')
CENSUS = ast.literal_eval(R(r'^  CENSUS tuple .*?: (\(.*\))$', st, 'the census')); assert CENSUS[2] == 1362 and CENSUS[13] == 907, CENSUS
SCAN = R(r'^(SCAN CENSUS DONE[^\n]*)', sc, 'the scan census'); SCAN_TRIPS = [l for l in sc.split('\n') if l.startswith(' TRIPS')]
print('THE PRINTS: runner %s; writes %d; parameters %d; readback %s; the tape %s on run %d; %s; RUN (%s); %s; %s; %s (%d tripping seats listed)' % (MATRIX, W, NPAR, RBG, TAPE_CP, NRUN, CC_LINE, RUN, DEP, NDEP, SCAN, len(SCAN_TRIPS)))
EXTRA = os.environ.get('POINT_EXTRA', '')   # the seats widened and the runs, typed from the prints at the run (the shell's own word)
# ---- #216 ----
sd = rd(SD); assert '\n#216 ' not in sd
P216 = ('\n\n#216 (2026-09-25, THE DEUTERONOMY WALK sitting 16b — CHAPTERS 19-21\'s COMPILE IN THE LEAN FORM, RUN B; on the owner\'s "Reread and go" after the compaction at #215 — no commit word said, the tree UNCOMMITTED since f730559 with sittings 15, 15b, 16 and 16b riding; A CLEAN COMPACTION POINT AT RUN B\'S END — the tape tools and the shells derived from 15b\'s forms (derive_ch19_seq_tools.py, derive_ch19_shells.py), the runner cold_run_refuge_war_family.py (the 73rd) derived and typed in five parts (part 1 from the chapter 17-18 runner\'s helpers and ch19_ink.py\'s three blocks with the callees\' facts typed from the print; parts 2-4 the nine cells; part 5 the readback\'s sixty-four rows, the data, the daemon, the thirteen lines, the narrative) — %s on its first graded run (nine cells and the table; %d writes on Israel in the narrative, every one its first entry; %d parameters in DATA; the readback %s), the tape %s on run %d (RUN (%s, the four pairs, 127); %s; DJ1-DJ5 the D series\' tenth name; THE SCAN CENSUS extended over the forty-five names run after the first tape run%s), %s (%s — the demands read before the chain, filed at the tail), THE GATES CHAIN LAUNCHED once in the background (ch19b_gates.sh — the register gate --strict, the positions at four workers; its SUMMARY unread); the tree UNCOMMITTED. NEXT: THE TAIL after the compaction (the summary read once, the demands and THE RECEIPT 20:17 filed from the prints — the register\'s class as the world says, the records from the sheet in one call — the map\'s AS BUILT with the timing table, this doc, the recovery page, the memory, COMPILE_DEBT\'s lean box — the forms, the message), then the commit on his word ("Commit" = no push; "commit push" = both). POST-COMPACTION REREADS: the recovery page, the map\'s newest section ("Sitting 16b — THE COMPILE OF CHAPTERS 19-21 … LEAN" — the design; the AS BUILT not yet written), MEMORY.md; then this checkpoint.' % (MATRIX, W, NPAR, RBG, TAPE_CP, NRUN, RUN, CC_LINE, EXTRA, DEP, NDEP))
# ---- the recovery page ----
rec = rd(REC)
def sub1(t, a, b, name):
    assert t.count(a) == 1, (name, t.count(a), a[:70]); return t.replace(a, b)
rec2 = sub1(rec, '## 2. WHERE IT STANDS (2026-09-25; #215 sitting 16b RUN A newest)', '## 2. WHERE IT STANDS (2026-09-25; #216 sitting 16b RUN B newest)', 'the header')
rec2 = sub1(rec2, '- NUMBERS CLOSED. DEUTERONOMY 1:1-18:22 ON THE TAPE (PUSHED through f730559 — 1-16); 17-18 compiled, 19-21 READ + FROZEN, their compile DESIGNED + TYPED (uncommitted).', '- NUMBERS CLOSED. DEUTERONOMY 1:1-21:23 ON THE TAPE (PUSHED through f730559 — 1-16; 17-21 uncommitted).', 'the tape line')
rec2 = sub1(rec2, '72 runners, 78 daemons; 1192 kinds / 1170 effects.', '73 runners, 78 daemons; 1192 kinds / 1170 effects.', 'the counts')
rec2 = sub1(rec2, "- THE TAPE at RUN (1349, 96, 88, 0, 12, 1709, 48, 319, pairs, 127); 10/10 (DI1-DI5); 15b's chain green.", "- THE TAPE at RUN (%s, pairs, 127); %s (DJ1-DJ5); 16b's chain LAUNCHED, summary unread." % (RUN, TAPE_CP), 'the RUN line')
rec2 = sub1(rec2, '- SITTINGS 15/15b (ch 17-18, LEAN): chain green; UNCOMMITTED.\n- SITTING 16 (ch 19-21 READ, LEAN) DONE at #214: 335 sources; 13 claims; chain green; UNCOMMITTED.\n', '- SITTINGS 15/15b/16 (ch 17-18 compiled, ch 19-21 read, LEAN): chains green; UNCOMMITTED.\n', 'the 15-16 lines')
rec2 = sub1(rec2, '- SITTING 16b RUN A (ch 19-21 COMPILE, LEAN) at #215: designed + typed (one runner refuge_war_family, 9 cells, 13 lines, 45 effects, 23 edges; Q45 FAIL 44/45; the exam 28 rows); NO RUNNER YET. NEXT: RUN B (the runner, the tape, the chain LAUNCHED), the tail, the commit.', '- SITTING 16b RUN B (ch 19-21 COMPILE, LEAN) at #216: runner refuge_war_family %s; 13 lines, %d writes; the tape %s; the chain LAUNCHED. NEXT: THE TAIL (summary once; the receipt 20:17; records; forms; message), then the commit.' % (MATRIX, W, TAPE_CP), 'the 16b line')
# ---- the memory ----
mm = rd(MM)
OLDL = '16b RUN A 2026-09-25 (the compile DESIGNED + TYPED — one runner refuge_war_family, 13 lines, 45 effects; the probe Q45 to FAIL 44/45; the exam 28 Mishnah rows; NO runner yet), UNCOMMITTED; NEXT: RUN B (the runner, the tape, the chain launched), the tail, then the commit'
NEWL = '16b 2026-09-25 (the compile — one runner refuge_war_family %s, 13 lines, %d writes; the tape %s; the chain launched), UNCOMMITTED; NEXT: the tail, then the commit' % (MATRIX, W, TAPE_CP)
mm2 = sub1(mm, OLDL, NEWL, 'the walk line')
mw = rd(MW)
DESC_OLD = 'description: "SITTING 16b RUN A AT ITS CLEAN POINT 2026-09-25'
assert mw.count(DESC_OLD) == 1
mw2 = mw.replace(DESC_OLD, 'description: "SITTING 16b RUN B AT ITS CLEAN POINT 2026-09-25 (chapters 19-21 COMPILED lean in one runner — refuge_war_family %s, thirteen lines, %d writes, the tape %s, the gates chain launched; UNCOMMITTED; NEXT the tail then the commit) — SITTING 16b RUN A AT ITS CLEAN POINT 2026-09-25' % (MATRIX, W, TAPE_CP), 1)
NOTE = ('\n\nSITTING 16b RUN B AT ITS CLEAN POINT 2026-09-25 — CHAPTERS 19-21 COMPILED IN THE LEAN FORM (the third compile sitting of [[lean-pass-ruling]], the first over three chapters — ONE runner, ONE daemon, the span three ranges): the tape tools and the shells derived from 15b\'s forms, the runner cold_run_refuge_war_family.py in five parts (the helpers and the ink blocks derived, the callees\' facts typed from the print; the cities of refuge, the landmark and the witnesses, the priest\'s speech, the siege, the heifer, the captive, the firstborn\'s double, the rebellious son, the hanged; the readback\'s sixty-four rows) %s on its first graded run (%d writes, %d parameters, the readback %s), the tape %s on run %d (RUN %s; DJ1-DJ5%s), the scan census extended over the forty-five names, the dependency gate\'s demands read (%s), the gates chain LAUNCHED once (the positions at four workers). UNCOMMITTED since f730559. NEXT: the tail after a compaction — the summary read once, the demands and the receipt 20:17 filed, the records, the forms, the message; then the commit on his word.' % (MATRIX, W, NPAR, RBG, TAPE_CP, NRUN, RUN, EXTRA, DEP))
mw2 = mw2.rstrip('\n') + NOTE + '\n'
# ---- the caps and the lints ----
rec_bytes = len(rec2.encode()); mm_bytes = len(mm2.encode())
assert rec_bytes <= 10240, ('the recovery page over its cap', rec_bytes)
assert mm_bytes < 17000, ('MEMORY.md over its cap', mm_bytes)
assert not re.search(r'[֐-׿]', P216 + NOTE + NEWL), 'no Hebrew script in the new texts'
print('THE POINT CHECKED: #216 %d bytes; the recovery page %d; MEMORY.md %d; the walk note %d' % (len(P216.encode()), rec_bytes, mm_bytes, len(mw2.encode())))
if not CHECK:
    open(SD, 'w', encoding='utf-8').write(sd.rstrip('\n') + P216 + '\n')
    open(REC, 'w', encoding='utf-8').write(rec2); open(MM, 'w', encoding='utf-8').write(mm2); open(MW, 'w', encoding='utf-8').write(mw2)
    import subprocess as sp_
    for f in (SD, REC, MM, MW):
        out = sp_.run(['python3', f'{ROOT}/logic/solo_tools/gloss_lint.py', f], capture_output=True, text=True).stdout.strip().split('\n')[-1]
        print('  lint', os.path.basename(f), out)
    print('THE POINT WRITTEN: #216, the recovery page (%d bytes), MEMORY.md (%d bytes), the walk note' % (rec_bytes, mm_bytes))
