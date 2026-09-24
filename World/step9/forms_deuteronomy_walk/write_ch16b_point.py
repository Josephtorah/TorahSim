import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE DEUTERONOMY WALK 14b (LEAN): THE CLEAN COMPACTION POINT at the compile window's end — the state doc's #210, the recovery page (section 2 under its cap), the
# memory (the index line and the walk note) — written in ONE call after the tape is 10/10 and the gates chain is LAUNCHED; every number READ FROM ITS PRINT (the
# runner's, the tape's, the checkpoint check's, the sequence file's RUN literal, the dependency gate's); every text built whole before a file is opened; the lints
# and the caps asserted. --check prints without writing. write_ch16_records.py's form. RUN FROM THE REPO ROOT.
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
run1 = rd(f'{SP}/ch16_runner_run1.out'); tape = rd(sorted(glob.glob(f'{SP}/ch16_tape_run*.out'))[-1]); NRUN = len(glob.glob(f'{SP}/ch16_tape_run*.out')); cc = rd(f'{SP}/ch16_checkpoint_check2.out'); seq = rd(f'{ROOT}/World/step9/cold_run_sequence.py'); dep = rd(f'{SP}/ch16b_dependency_after.out'); st = rd(f'{SP}/seq_stitch_ch16.out')
MATRIX = R(r'^MATRIX: (\d+/\d+) cells match', run1, 'the runner'); assert MATRIX.split('/')[0] == MATRIX.split('/')[1], MATRIX
NARR = ast.literal_eval(R(r'^THE NARRATIVE: (\(.*?\)) \(the sixteen', run1, 'the narrative')); W = NARR[0]
NPAR = int(R(r'the twenty-nine (\d+) \(in the registry', run1, 'the parameters'))
RBG = R(r'^THE READBACK — THE FORMS ON FILE, NO NEW FORM: 22 rows — (\{.*?\});', run1, 'the readback')
TAPE_CP = R(r'(\d+/\d+) checkpoints?', tape, 'the tape') if re.search(r'\d+/\d+ checkpoints?', tape) else R(r'checkpoints[^\n]*?(\d+/\d+)', tape, 'the tape')
CC_LINE = R(r'^(checkpoint_check: \d+ rows, \d+ miss, \d+ raised[^\n]*)', cc, 'the checkpoint check'); assert ', 18 miss, 0 raised' in CC_LINE, CC_LINE   # the eighteen known misses (13b's count — the calendar's open checkpoints), none new; the DH block MATCH
RUN = R(r"^RUN = \((\d+, \d+, \d+, \d+, \d+, \d+, \d+, \d+),", seq, 'RUN'); assert RUN.startswith('1341, 96, 88, 0, 12, %d, 47, 319' % (1656 + W)), RUN
DEP = R(r'^(DEPENDENCY GATE: [^\n]*)', dep, 'the dependency gate'); assert 'satisfied' in DEP or '0 failure' in DEP, DEP
NDEP = R(r'dispositions on file: (\d+ edges, \d+ pointers)', dep, 'the dispositions')
CENSUS = ast.literal_eval(R(r'^  CENSUS tuple .*?: (\(.*\))$', st, 'the census')); assert CENSUS[2] == 1341 and CENSUS[13] == 886, CENSUS
print('THE PRINTS: runner %s; writes %d; parameters %d; readback %s; the tape %s; %s; RUN (%s); %s; %s' % (MATRIX, W, NPAR, RBG, TAPE_CP, CC_LINE, RUN, DEP, NDEP))
# ---- #210 ----
sd = rd(SD); assert '\n#210 ' not in sd
P210 = ('\n\n#210 (2026-09-23, THE DEUTERONOMY WALK sitting 14b — CHAPTER 16\'s COMPILE IN THE LEAN FORM, the lean pass\'s first compile sitting; on the owner\'s "Reread and go" after the compaction at #209 — no "Commit" said, the tree UNCOMMITTED since e824e52 and 14b opened on it; A CLEAN COMPACTION POINT AT THE COMPILE WINDOW\'S END — the design in the map ("Sitting 14b — THE COMPILE OF CHAPTER 16 … LEAN … THE DESIGN"), the probe Q43 to FAIL, the types (five kinds, fifteen effects, the bribe\'s row amended, the daemon law_festivals_judges the 76th, fifteen CALL edges, I5 76), the callees\' facts printed and typed, the runner cold_run_festivals_judges.py (the 71st) in three parts — %s on its first graded run (six cells and the table; %d writes on Israel in the narrative; %d parameters in DATA; the readback %s), the lean exam file logic/oral_triage/deu_16_reeh_shoftim_exam_2026-09-23.md (the eight Mishnah rows read whole, no segment), the second-tablets callee\'s bribe scan widened for 16:19\'s first entry, the tape %s on its FIFTH run (the first 9/10 — DD4, chapter 12\'s hole scan, matched 16:5\'s block by the substring \'in_the_gates\' and was retyped; the second and third runs stopped at two callees\' scans of the one database — second_tablets\' LAW_SCAN and place_name\'s PLACE_SCAN — moved by the first run\'s own writes on Israel, each widened with the note; the fourth the patch\'s anchor miss; THE SCAN CENSUS ch16_scan_census.py written to replay every runner\'s hole scan on the one database at once; RUN (%s, the four pairs, 127); %s; DH1-DH5 the D series\' eighth name; DB7 the one stale literal retyped), the dependency gate\'s two demands filed from its print (the widow FALSE — the household list\'s; 16:10\'s "as He blesses you" PARAMETER) and the gate green alone (%s), THE GATES CHAIN LAUNCHED in the background (gates_chain.sh — one pass, the positions at four workers; its summary <scratch>/ch16b_gates_SUMMARY.txt, its log <scratch>/ch16b_gates.log) — the records writer and the copier WRITTEN): THE STATE: the tree UNCOMMITTED (sitting 14\'s reading and the lean-pass ruling ride with this). NEXT ON HIS WORD: THE TAIL after the compaction ("Reread", then "Go"): (1) the chain\'s SUMMARY read ONCE (never polled) — every FAIL read from its step print in <scratch>/ch16b_gates/<step>.out, the demands filed, a pass after any source change STARTS AT THE TAPE (13b\'s lesson); (2) write_ch16b_records.py --check then write (the four records — the map\'s AS BUILT — LEAN, this checkpoint\'s NOTE, the recovery page, the memory — and the lean-pass box\'s line in COMPILE_DEBT); (3) copy_ch16b_forms.py; (4) write_ch16b_commit_msg.py; then the commit on his word ("Commit" = no push; "commit push" = both). POST-COMPACTION REREADS: the recovery page, the map\'s newest section ("Sitting 14b — THE COMPILE OF CHAPTER 16, Deuteronomy 16:1-22 — LEAN … THE DESIGN"), MEMORY.md; then this checkpoint.' % (MATRIX, W, NPAR, RBG, TAPE_CP, RUN, CC_LINE, DEP))
# ---- the recovery page ----
rec = rd(REC)
def sub1(t, a, b, name):
    assert t.count(a) == 1, (name, t.count(a), a[:70]); return t.replace(a, b)
rec2 = sub1(rec, '## 2. WHERE IT STANDS (2026-09-23; #209 sitting 14 newest)', '## 2. WHERE IT STANDS (2026-09-23; #210 sitting 14b newest)', 'the header')
rec2 = sub1(rec2, '- NUMBERS CLOSED. DEUTERONOMY 1:1-15:23 ON THE TAPE (PUSHED through e824e52 — 15 and 13b).', '- NUMBERS CLOSED. DEUTERONOMY 1:1-16:22 ON THE TAPE (PUSHED through e824e52 — 15/13b; 16 uncommitted).', 'the tape line')
rec2 = sub1(rec2, '70 runners, 75 daemons; 1166 kinds / 1073 effects.', '71 runners, 76 daemons; 1171 kinds / 1088 effects.', 'the counts')
rec2 = sub1(rec2, '- SITTING 13/13b (ch 15): 132 sources; the docket 974 rows; release_firstborn 91/91; 4 lines, 15 writes, 27 parameters; PUSHED e824e52.', '- SITTING 13/13b (ch 15): 132 sources; release_firstborn 91/91; PUSHED e824e52.', 'the 13b line')
rec2 = sub1(rec2, '- THE TAPE at RUN (1336, 96, 88, 0, 12, 1656, 46, 319, pairs, 127), markers 172, closes 127; 10/10 (DG1-DG9); sweep 69/69; all gates GREEN, 5 passes.', '- THE TAPE at RUN (%s, pairs, 127), markers 172, closes 127; %s (DH1-DH5); 14b\'s chain LAUNCHED, summary unread.' % (RUN, TAPE_CP), 'the RUN line')
rec2 = sub1(rec2, '- SITTING 14 (ch 16 READ, LEAN) DONE at #209: 136 sources; 8 claims; FROZEN; chain green; UNCOMMITTED. NEXT: the commit; then 14b after a compaction.', '- SITTING 14/14b (ch 16 READ + COMPILED, LEAN) at #210: 136 sources; runner %s; 5 lines, %d writes; the tape %s; UNCOMMITTED. NEXT: THE TAIL (summary once; records; forms; message), then the commit.' % (MATRIX, W, TAPE_CP), 'the sitting line')
# ---- the memory ----
mm = rd(MM)
OLDL = '14 (ch 16 READ, lean) DONE 2026-09-23 (136 sources, 8 claims), UNCOMMITTED; NEXT: the commit, then 14b'
NEWL = '14/14b (ch 16 READ + COMPILED, lean) 2026-09-23 (136 sources; 53/53; the tape %s; the chain launched), UNCOMMITTED; NEXT: the tail, then the commit' % TAPE_CP
mm2 = sub1(mm, OLDL, NEWL, 'the walk line')
mw = rd(MW)
DESC_OLD = 'description: "COMMITTED AND PUSHED THROUGH e824e52'
assert mw.count(DESC_OLD) == 1
mw2 = mw.replace(DESC_OLD, 'description: "SITTING 14b AT ITS CLEAN POINT 2026-09-23 (chapter 16 COMPILED lean — festivals_judges %s, five lines, %d writes, the tape %s, the gates chain launched; UNCOMMITTED; NEXT the tail then the commit) — COMMITTED AND PUSHED THROUGH e824e52' % (MATRIX, W, TAPE_CP), 1)
NOTE = ('\n\nSITTING 14b AT ITS CLEAN POINT 2026-09-23 — CHAPTER 16 COMPILED IN THE LEAN FORM (the first compile sitting of [[lean-pass-ruling]]): the design (the place added to the three feasts and the pilgrimage, the courts in every gate, the asherah and the pillar — five own-day lines, fifteen new effects and the bribe\'s first entry), the probe Q43, the types, the callees\' facts from their prints, the runner cold_run_festivals_judges.py in three parts %s on its first graded run (%d writes, %d parameters, the readback %s), the lean exam file (the eight Mishnah rows the spine cites, read whole; no segment), the tape %s on its fifth run (DD4 retyped; two callees\' scans of the one database widened — second_tablets twice, place_name once; the scan census the instrument; RUN %s; DH1-DH5; DB7 retyped), the dependency gate\'s two demands filed (the widow FALSE, 16:10 PARAMETER), the gates chain LAUNCHED once (the positions at four workers). UNCOMMITTED since e824e52. NEXT: the tail after a compaction — the summary read once, the records, the forms, the message; then the commit on his word.' % (MATRIX, W, NPAR, RBG, TAPE_CP, RUN))
mw2 = mw2.rstrip('\n') + NOTE + '\n'
# ---- the caps and the lints ----
rec_bytes = len(rec2.encode()); mm_bytes = len(mm2.encode())
assert rec_bytes <= 10240, ('the recovery page over its cap', rec_bytes)
assert mm_bytes < 17000, ('MEMORY.md over its cap', mm_bytes)
assert not re.search(r'[֐-׿]', P210 + NOTE + NEWL), 'no Hebrew script in the new texts'
print('THE POINT CHECKED: #210 %d bytes; the recovery page %d; MEMORY.md %d; the walk note %d' % (len(P210.encode()), rec_bytes, mm_bytes, len(mw2.encode())))
if not CHECK:
    open(SD, 'w', encoding='utf-8').write(sd.rstrip('\n') + P210 + '\n')
    open(REC, 'w', encoding='utf-8').write(rec2); open(MM, 'w', encoding='utf-8').write(mm2); open(MW, 'w', encoding='utf-8').write(mw2)
    import subprocess as sp_
    for f in (SD, REC, MM, MW):
        out = sp_.run(['python3', f'{ROOT}/logic/solo_tools/gloss_lint.py', f], capture_output=True, text=True).stdout.strip().split('\n')[-1]
        print('  lint', os.path.basename(f), out)
    print('THE POINT WRITTEN: #210, the recovery page (%d bytes), MEMORY.md (%d bytes), the walk note' % (rec_bytes, mm_bytes))
