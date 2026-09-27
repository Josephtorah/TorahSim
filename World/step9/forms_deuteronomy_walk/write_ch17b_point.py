import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE DEUTERONOMY WALK 15b (LEAN): THE CLEAN COMPACTION POINT at the compile window's end — the state doc's #212, the recovery page (section 2 under its cap), the
# memory (the index line and the walk note) — written in ONE call after the tape is 10/10 and the gates chain is LAUNCHED; every number READ FROM ITS PRINT (the
# runner's, the tape's, the checkpoint check's, the sequence file's RUN literal, the dependency gate's, the stitcher's, the scan census's); every text built whole before a
# file is opened; the lints and the caps asserted. --check prints without writing. write_ch16b_point.py's form. RUN FROM THE REPO ROOT.
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
def RL(pat, text, name):   # the LAST match — the runner's own MATRIX line follows the callees' import-time reports in its print (read at the point's first check: 287/287 the first line, the runner's 66/66 the last)
    g = re.findall(pat, text, re.M); assert g, (name, pat); return g[-1]
run = rd(sorted(glob.glob(f'{SP}/ch17_runner_run*.out'))[-1]); tapes = sorted(glob.glob(f'{SP}/ch17_tape_run*.out')); tape = rd(tapes[-1]); NRUN = len(tapes); cc = rd(sorted(glob.glob(f'{SP}/ch17_checkpoint_check*.out'))[-1]); seq = rd(f'{ROOT}/World/step9/cold_run_sequence.py'); dep = rd(sorted(glob.glob(f'{SP}/ch17b_dependency_after*.out'))[-1]); st = rd(f'{SP}/seq_stitch_ch17.out'); sc = rd(f'{SP}/ch17_scan_census.out')
MATRIX = RL(r'^MATRIX: (\d+/\d+) cells match', run, 'the runner'); assert MATRIX.split('/')[0] == MATRIX.split('/')[1], MATRIX
NARR = ast.literal_eval(R(r'^THE NARRATIVE: (\(.*?\)) \(the thirty-seven', run, 'the narrative')); W = NARR[0]
NPAR = int(R(r'the thirty (\d+) \(in the registry', run, 'the parameters'))
RBG = R(r'^THE READBACK — THE FORMS ON FILE, NO NEW FORM: 42 rows — (\{.*?\});', run, 'the readback')
TAPE_CP = R(r'(\d+/\d+) checkpoints?', tape, 'the tape') if re.search(r'\d+/\d+ checkpoints?', tape) else R(r'checkpoints[^\n]*?(\d+/\d+)', tape, 'the tape')
assert TAPE_CP.split('/')[0] == TAPE_CP.split('/')[1], ('THE TAPE NOT AT 10/10 — the point waits', TAPE_CP)
CC_LINE = R(r'^(checkpoint_check: \d+ rows, \d+ miss, \d+ raised[^\n]*)', cc, 'the checkpoint check'); assert ', 18 miss, 0 raised' in CC_LINE, CC_LINE   # the eighteen known misses (13b's count — the calendar's open checkpoints), none new; the DI block MATCH
RUN = R(r"^RUN = \((\d+, \d+, \d+, \d+, \d+, \d+, \d+, \d+),", seq, 'RUN'); assert RUN.startswith('1349, 96, 88, 0, 12, %d, 48, 319' % (1672 + W)), RUN
DEP = R(r'^(DEPENDENCY GATE: [^\n]*)', dep, 'the dependency gate')
NDEP = R(r'dispositions on file: (\d+ edges, \d+ pointers)', dep, 'the dispositions')
CENSUS = ast.literal_eval(R(r'^  CENSUS tuple .*?: (\(.*\))$', st, 'the census')); assert CENSUS[2] == 1349 and CENSUS[13] == 894, CENSUS
SCAN = R(r'^(SCAN CENSUS DONE[^\n]*)', sc, 'the scan census'); SCAN_TRIPS = [l for l in sc.split('\n') if l.startswith(' TRIPS')]
print('THE PRINTS: runner %s; writes %d; parameters %d; readback %s; the tape %s on run %d; %s; RUN (%s); %s; %s; %s (%d tripping seats listed)' % (MATRIX, W, NPAR, RBG, TAPE_CP, NRUN, CC_LINE, RUN, DEP, NDEP, SCAN, len(SCAN_TRIPS)))
EXTRA = os.environ.get('POINT_EXTRA', '')   # the seats widened and the runs, typed from the prints at the run (the shell's own word)
# ---- #212 ----
sd = rd(SD); assert '\n#212 ' not in sd
P212 = ('\n\n#212 (2026-09-24, THE DEUTERONOMY WALK sitting 15b — CHAPTERS 17-18\'s COMPILE IN THE LEAN FORM, the lean pass\'s second compile sitting and the first over two chapters; on the owner\'s "Reread go" after the compaction at #211 — no "Commit" said, the tree UNCOMMITTED since f730559 and 15b opened on it; A CLEAN COMPACTION POINT AT THE COMPILE WINDOW\'S END — the design in the map ("Sitting 15b — THE COMPILE OF CHAPTERS 17-18 … LEAN"), the probe Q44 to FAIL, the lean exam file logic/oral_triage/deu_17_18_shoftim_exam_2026-09-24.md (the eight Mishnah rows the spine cites, read whole, no segment), the types (eight kinds, thirty-seven effects, the daemon law_courts_prophet the 77th over two chapters, the span two ranges, twenty CALL edges all reference, I5 77), the callees\' facts printed from twenty runners and typed, the runner cold_run_courts_prophet.py (the 72nd) in four parts — %s on its first graded run (eight cells and the table; %d writes on Israel in the narrative, every one its first entry; %d parameters in DATA; the readback %s), the tape %s on run %d (RUN (%s, the four pairs, 127); %s; DI1-DI5 the D series\' ninth name; THE SCAN CENSUS extended to the probes\' and the tape\'s substring scans run after the first tape run%s), %s (%s — the demands read before the chain, filed at the tail), THE GATES CHAIN LAUNCHED once in the background (ch17b_gates.sh — the register gate --strict, the positions at four workers; its SUMMARY unread); the tree UNCOMMITTED. NEXT: THE TAIL after the compaction (the summary read once, the demands filed from the print, the records from the sheet in one call — the map\'s AS BUILT with the timing table, this doc, the recovery page, the memory, COMPILE_DEBT\'s lean box — the forms, the message), then the commit on his word ("Commit" = no push; "commit push" = both). POST-COMPACTION REREADS: the recovery page, the map\'s newest section ("Sitting 15b — THE COMPILE OF CHAPTERS 17-18 … LEAN" — the design; the AS BUILT not yet written), MEMORY.md; then this checkpoint.' % (MATRIX, W, NPAR, RBG, TAPE_CP, NRUN, RUN, CC_LINE, EXTRA, DEP, NDEP))
# ---- the recovery page ----
rec = rd(REC)
def sub1(t, a, b, name):
    assert t.count(a) == 1, (name, t.count(a), a[:70]); return t.replace(a, b)
rec2 = sub1(rec, '## 2. WHERE IT STANDS (2026-09-24; #211 sitting 15 newest)', '## 2. WHERE IT STANDS (2026-09-24; #212 sitting 15b newest)', 'the header')
rec2 = sub1(rec2, '- NUMBERS CLOSED. DEUTERONOMY 1:1-16:22 ON THE TAPE (PUSHED through f730559); 17-18 READ AND FROZEN (lean).', '- NUMBERS CLOSED. DEUTERONOMY 1:1-18:22 ON THE TAPE (PUSHED through f730559 — 1-16; 17-18 uncommitted).', 'the tape line')
rec2 = sub1(rec2, '71 runners, 76 daemons; 1171 kinds / 1088 effects.', '72 runners, 77 daemons; 1179 kinds / 1125 effects.', 'the counts')
rec2 = sub1(rec2, '- SITTING 14/14b (ch 16 READ + COMPILED, LEAN): 136 sources; runner 53/53; the tape 10/10; PUSHED f730559.', '- SITTING 14/14b (ch 16, LEAN): PUSHED f730559.', 'the 14b line')
rec2 = sub1(rec2, "- THE TAPE at RUN (1341, 96, 88, 0, 12, 1672, 47, 319, pairs, 127), markers 172, closes 127; 10/10 (DH1-DH5); 14b's chain ALL GREEN once (sweep 70/70).", "- THE TAPE at RUN (%s, pairs, 127), markers 172, closes 127; %s (DI1-DI5); 15b's chain LAUNCHED, summary unread." % (RUN, TAPE_CP), 'the RUN line')
rec2 = sub1(rec2, '- SITTING 15 (ch 17-18 READ, LEAN, two units) DONE at #211: 234 sources; 8 claims; FROZEN; chain green; UNCOMMITTED. NEXT: the commit, then 15b (the compile).', '- SITTING 15/15b (ch 17-18 READ + COMPILED, LEAN; one runner) at #212: 234 sources; runner %s; 8 lines, %d writes; the tape %s; UNCOMMITTED. NEXT: THE TAIL (summary once; records; forms; message), then the commit.' % (MATRIX, W, TAPE_CP), 'the sitting line')
# ---- the memory ----
mm = rd(MM)
OLDL = '15 (ch 17-18 READ, lean — two units, one ledger) DONE 2026-09-24 (234 sources, 8 claims; FROZEN; chain green), UNCOMMITTED; NEXT: the commit, then 15b (the compile of 17-18)'
NEWL = '15/15b (ch 17-18 READ + COMPILED, lean — one runner) 2026-09-24 (234 sources; %s; the tape %s; the chain launched), UNCOMMITTED; NEXT: the tail, then the commit' % (MATRIX, TAPE_CP)
mm2 = sub1(mm, OLDL, NEWL, 'the walk line')
mw = rd(MW)
DESC_OLD = 'description: "SITTING 14b AT ITS CLEAN POINT 2026-09-23'
assert mw.count(DESC_OLD) == 1
mw2 = mw.replace(DESC_OLD, 'description: "SITTING 15b AT ITS CLEAN POINT 2026-09-24 (chapters 17-18 COMPILED lean in one runner — courts_prophet %s, eight lines, %d writes, the tape %s, the gates chain launched; UNCOMMITTED; NEXT the tail then the commit) — SITTING 14b AT ITS CLEAN POINT 2026-09-23' % (MATRIX, W, TAPE_CP), 1)
NOTE = ('\n\nSITTING 15b AT ITS CLEAN POINT 2026-09-24 — CHAPTERS 17-18 COMPILED IN THE LEAN FORM (the second compile sitting of [[lean-pass-ruling]], the first over two chapters — ONE runner, ONE daemon, the span two ranges): the design (the blemished sacrifice, the idolater\'s trial, THE HIGH COURT AT THE PLACE — the courts\' second daemon paid in the lean form, the king with his three limits, the priests\' dues and the fleece, the Levite at the place, the diviners, THE PROPHET WITH THE TEST BY THE EVENT — eight own-day lines, thirty-seven new effects every one its first entry), the probe Q44, the lean exam file (the eight Mishnah rows the spine cites, read whole; no segment), the types, the callees\' facts from twenty runners\' prints, the runner cold_run_courts_prophet.py in four parts %s on its first graded run (%d writes, %d parameters, the readback %s), the tape %s on run %d (RUN %s; DI1-DI5%s), the scan census extended to the probes\' and the tape\'s scans, the dependency gate\'s demands read (%s), the gates chain LAUNCHED once (the positions at four workers). UNCOMMITTED since f730559. NEXT: the tail after a compaction — the summary read once, the demands filed, the records, the forms, the message; then the commit on his word.' % (MATRIX, W, NPAR, RBG, TAPE_CP, NRUN, RUN, EXTRA, DEP))
mw2 = mw2.rstrip('\n') + NOTE + '\n'
# ---- the caps and the lints ----
rec_bytes = len(rec2.encode()); mm_bytes = len(mm2.encode())
assert rec_bytes <= 10240, ('the recovery page over its cap', rec_bytes)
assert mm_bytes < 17000, ('MEMORY.md over its cap', mm_bytes)
assert not re.search(r'[֐-׿]', P212 + NOTE + NEWL), 'no Hebrew script in the new texts'
print('THE POINT CHECKED: #212 %d bytes; the recovery page %d; MEMORY.md %d; the walk note %d' % (len(P212.encode()), rec_bytes, mm_bytes, len(mw2.encode())))
if not CHECK:
    open(SD, 'w', encoding='utf-8').write(sd.rstrip('\n') + P212 + '\n')
    open(REC, 'w', encoding='utf-8').write(rec2); open(MM, 'w', encoding='utf-8').write(mm2); open(MW, 'w', encoding='utf-8').write(mw2)
    import subprocess as sp_
    for f in (SD, REC, MM, MW):
        out = sp_.run(['python3', f'{ROOT}/logic/solo_tools/gloss_lint.py', f], capture_output=True, text=True).stdout.strip().split('\n')[-1]
        print('  lint', os.path.basename(f), out)
    print('THE POINT WRITTEN: #212, the recovery page (%d bytes), MEMORY.md (%d bytes), the walk note' % (rec_bytes, mm_bytes))
