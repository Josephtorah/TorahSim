import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE DEUTERONOMY WALK 21b (LEAN): THE CLEAN COMPACTION POINT at RUN B's end — the state doc's #242, the recovery page (section 2 rewritten under its cap), the memory
# (the index line and the walk note) — written in ONE call after the types, the runner, the gates alone, the tape to 10/10 and the chain's launch; every number READ FROM
# ITS PRINT (the types' prints, the runner's graded runs, the stitcher's census, the tape's verdicts and its RUN literal, checkpoint_check, the dependency and daemon gates'
# prints, the scan census, the timing table); every text built whole before a file is opened; the lints and the caps asserted. --check prints without writing.
# write_ch32b_point2.py's form WITHOUT THE MARKER AND WITHOUT A REUSE. RUN FROM THE REPO ROOT with PYTHONPATH the scratchpad.
import os, re, sys, subprocess, glob
ROOT = _ROOT
SP = os.path.dirname(os.path.abspath(__file__))
MEM = os.path.expanduser('~/.claude/projects/-Users-Shared-TorahSim/memory')
CHECK = '--check' in sys.argv
SD = f'{ROOT}/logic/pre_logic_methods_2026-07-28/PROMPT_continue_solo_era_2026-08-06.md'; REC = f'{ROOT}/logic/pre_logic_methods_2026-07-28/RECOVERY_new_thread_2026-09-12.md'
MM = f'{MEM}/MEMORY.md'; MW = f'{MEM}/deuteronomy-walk.md'; SEQ = f'{ROOT}/World/step9/cold_run_sequence.py'; RUNNER = f'{ROOT}/World/step9/cold_run_blessing_of_moses.py'
def rd(p): return open(p, encoding='utf-8').read()
def R(pat, text, name, g=1):
    m = re.search(pat, text, re.M); assert m, (name, pat); return m.group(g)
ta, tb = rd(f'{SP}/ch33b_types_a.out'), rd(f'{SP}/ch33b_types_b.out')
RUNS = sorted(glob.glob(f'{SP}/ch33_runner_run*.out')); rr = rd(RUNS[-1]); r1 = rd(RUNS[0]); st = rd(f'{SP}/seq_stitch_ch33.out'); seq = rd(SEQ)
TAPES = sorted(glob.glob(f'{SP}/ch33_tape_run*.out')); CCS = sorted(glob.glob(f'{SP}/ch33_checkpoint_check*.out')); cc = rd(CCS[-1])
DGS = sorted(glob.glob(f'{SP}/ch33b_dependency_*.out'), key=os.path.getmtime); dg = rd(DGS[-1]); dm = rd(f'{SP}/ch33b_daemon_first.out'); sc = rd(f'{SP}/ch33_scan_census.out'); tsv = rd(f'{SP}/ch33b_timing.tsv')
KADD, KREG = R(r'^kinds: (\d+) added of \d+ \(10 speech / 1 act\), registry (\d+);', ta, 'kinds'), R(r'^kinds: \d+ added of \d+ \(10 speech / 1 act\), registry (\d+);', ta, 'kinds reg')
EADD, EREG = R(r'^effects: (\d+) added \(registry (\d+)\)', ta, 'effects'), R(r'^effects: \d+ added \(registry (\d+)\)', ta, 'effects reg')
DAEM, FB = R(r'^daemons: (\d+) \(law_blessing_of_moses True\); functions blocks: (\d+);', tb, 'daemons'), R(r'functions blocks: (\d+);', tb, 'fb')
E39, PTRS0 = R(r'^dependency: the span \(one range\) \+ (\d+) edges', tb, 'e39'), R(r'; edges \d+, pointers (\d+)$', tb, 'pointers0')
I5, CAL = R(r'^installation_probes I5: (\d+)', tb, 'i5'), R(r'^calendar: (\d+) parameters', tb, 'cal')
assert (KADD, KREG, EADD, EREG, DAEM, FB, E39, I5, CAL) == ('11', '1280', '28', '1469', '83', '77', '39', '83', '75'), (KADD, KREG, EADD, EREG, DAEM, FB, E39, I5, CAL)
MATRIX = re.findall(r'^MATRIX: (\d+/\d+) cells match the answer sheet$', rr, re.M)[-1]; MATRIX1 = re.findall(r'^MATRIX: (\d+/\d+) cells', r1, re.M)[-1]; assert MATRIX.split('/')[0] == MATRIX.split('/')[1], (MATRIX, MATRIX1)
FRAC = re.findall(r'^FRACTIONS: (pure ink \d+/\d+ \(\d+%\) · named moves \d+/\d+ \(\d+%\) · data \d+/\d+ \(\d+%\)) ·', rr, re.M)[-1]
RB = R(r'^THE READBACK — THE FORMS ON FILE, NO NEW FORM: (\d+) rows — ', rr, 'readback'); RBG = R(r'^THE READBACK — THE FORMS ON FILE, NO NEW FORM: \d+ rows — (\{[^}]+\});', rr, 'grades'); RBT = R(r'^THE READBACK — THE FORMS ON FILE, NO NEW FORM: \d+ rows — \{[^}]+\}; on the tape (\d+),', rr, 'on tape')
PAR, NDATA = R(r'the parameters (\d+) \(in the registry (\d+), in DATA \d+\); DATA rows (\d+)$', rr, 'parameters'), R(r'; DATA rows (\d+)$', rr, 'data'); INREG = R(r'the parameters \d+ \(in the registry (\d+),', rr, 'in registry')
NARR = R(r'^THE NARRATIVE: (\(\d+, \d+, \d+, \(\d+, \d+\), \d+, \d+, \d+, \d+, \[[^\]]*\]\))', rr, 'narrative')
NFACTS = R(r'^THE CALLEES \(the facts printed and asserted from the print\): (\d+) facts', rr, 'facts')
LINT_R = re.search(r'(\d+) flag', subprocess.run(['python3', f'{ROOT}/logic/solo_tools/gloss_lint.py', RUNNER], capture_output=True, text=True).stdout).group(1); assert LINT_R == '0', LINT_R
PLACE = R(r"^PLACEMENT LITERAL: (\{.*\})$", st, 'placement'); CENSUS = R(r'^  CENSUS tuple \([^)]*\): (\(.*\))$', st, 'census')
RUN = R(r'^RUN = \((\d+, \d+, \d+, \d+, \d+, \d+, \d+, \d+),', seq, 'RUN'); PREV = R(r'^PREVIOUS_RUN = \((\d+, \d+, \d+, \d+, \d+, \d+, \d+, \d+),', seq, 'PREV'); assert PREV == '1439, 102, 94, 0, 12, 2048, 53, 319', (RUN, PREV)
VS = [(re.search(r'^(\d+/10) checkpoints$', rd(t), re.M).group(1) if re.search(r'^(\d+/10) checkpoints$', rd(t), re.M) else 'TRIPPED') for t in TAPES]; assert VS[-1] == '10/10', VS
def divs(t): return sorted(set(l.split()[1] for l in t.split('\n') if l.lstrip().startswith('CHECKPOINT ') and l.split()[-1] == 'DIVERGE'))
BASE = divs(rd(TAPES[-1])); DIVS = [[d for d in divs(rd(t)) if d not in BASE] for t in TAPES[:-1]]
DO = [l.split()[1] for l in rd(TAPES[-1]).split('\n') if re.match(r'\s*CHECKPOINT DO\d', l) and l.split()[-1] == 'MATCH']; assert len(set(DO)) == 5, DO
MK = R(r'^  CENSUS tuple \([^)]*\): \((?:\d+, ){9}(\d+),', st, 'markers in the census'); assert MK == '173', MK
CC = R(r'^checkpoint_check: (\d+ rows, \d+ miss, \d+ raised)', cc, 'checkpoint_check'); assert CC.endswith('0 raised'), CC
DGL = R(r'^DEPENDENCY GATE coverage: (\d+) runners declared', dg, 'runners'); DGE = R(r'dispositions on file: (\d+ edges, \d+ pointers)$', dg, 'edges'); DGOK = 'gate satisfied' in dg
LINKC = R(r'^LINK CENSUS \(the link review law\): (reference \d+, transfer \d+, hypothesis \d+, none \d+)', dg, 'link census')
import yaml as _y; _dd = _y.safe_load(open(f'{ROOT}/World/step9/dependency_dispositions.yaml', encoding='utf-8')); MINE = len([e for e in _dd['edges'] if e.get('from') == 'blessing_of_moses']); ONFILE = len(_dd['edges']); NPTR = len(_dd['pointers']); OWED = len([p for p in _dd['pointers'] if p.get('disposition') == 'OWED'])
assert DGE.startswith('%d edges, %d pointers' % (ONFILE, NPTR)), (DGE, ONFILE, NPTR)
DMN, DMF = R(r'regenerated \((\d+) daemons, (\d+) functions\)', dm, 'daemons'), R(r'regenerated \(\d+ daemons, (\d+) functions\)', dm, 'functions'); DMOK = 'gate satisfied' in dm; assert DMN == DAEM
SCP, SCT = R(r'chapter 33 present: (\d+) \[', sc, 'present'), R(r'^SCAN CENSUS DONE — runner scans tripping: (\d+)$', sc, 'tripping')   # READ FROM THE PRINT
RSIZE = os.path.getsize(RUNNER)
rows = [l.split('\t') for l in tsv.split('\n') if l.split('\t')[1:2] and l.split('\t')[1].startswith('21b ')]; NSTEPS = len(rows); SECS = sum(int(r[2]) for r in rows)
FC = sorted(glob.glob(f'{SP}/ch33_fastcheck_run*.out')); FCL = rd(FC[-1]).strip().split('\n')[-1]; AK = sorted(glob.glob(f'{SP}/ch33_askcheck_run*.out')); AKL = rd(AK[-1]).strip().split('\n')[-1]
print('THE PRINTS: kinds +%s -> %s, effects +%s -> %s, daemons %s, blocks %s, edges %s, I5 %s, calendar %s; MATRIX %s (run 1 %s); %s; readback %s rows %s on the tape %s; parameters %s (in the registry %s), DATA %s; NARRATIVE %s; facts %s; runner %d bytes lint %s; PLACEMENT %s; CENSUS %s; RUN (%s) from (%s); the tape %s, the diverges before the last %s; DO %d; checkpoint_check %s; the daemon gate %s (%s daemons, %s functions); the dependency gate %s (%s runners, %s; %s) — mine %d, on file %d edges, %d pointers, OWED %d; the scan census present %s tripping %s; the fast checker %s; the ask checker %s; %d steps, %d s' % (KADD, KREG, EADD, EREG, DAEM, FB, E39, I5, CAL, MATRIX, MATRIX1, FRAC, RB, RBG, RBT, PAR, INREG, NDATA, NARR, NFACTS, RSIZE, LINT_R, PLACE, CENSUS, RUN, PREV, VS, DIVS, len(set(DO)), CC, 'GREEN' if DMOK else 'RED', DMN, DMF, 'GREEN' if DGOK else 'RED', DGL, DGE, LINKC, MINE, ONFILE, NPTR, OWED, SCP, SCT, FCL, AKL, NSTEPS, SECS))
sd = rd(SD); assert '\n#242 ' not in sd and '\n#241 (' in sd
P242 = ('\n\n#242 (2026-09-29, THE DEUTERONOMY WALK sitting 21b — CHAPTER 33\'s COMPILE IN THE LEAN FORM, THE BLESSING, RUN B of two; on the owner\'s "Reread and go" after the compaction at #241 — no commit word said since 472d2a3, the tree UNCOMMITTED with sitting 21 whole, its display patch, RUN A\'s and RUN B\'s files; A CLEAN COMPACTION POINT AT RUN B\'S END, THE GATES CHAIN LAUNCHED IN THE BACKGROUND (its summary to be read once at the tail): '
        'THE REREADS done (the recovery page, the map\'s newest section — the design\'s THE ORDER paragraph and the whole, MEMORY.md, #241; the spec module ch33b_spec.py before the types; THE_STEPS Step 5\'s head and the compiler block). '
        'THE TYPES BY SCRIPT (add_types_ch33_a.py: %s kinds IN TWO FORMS — 10 speech, 1 act — on the registry (%s); %s effects (%s) — 28 statuses, no block, no heaven entry on TWELVE ledgers (Israel 10 and the tribes\' own — reuben 1, judah 1, levi 4, benjamin 1, joseph 3, zebulun 1, issachar 1, gad 2, dan_son 1, naphtali 1, asher 2), every `he` FOUND in its verse from the store\'s own print (the fiery law\'s phrase on the ketiv alone — the qere\'s two tokens live in the gloss print, not in the store\'s words table: the first check tripped and the phrase was retyped); NO reused row; add_types_ch33_b.py: the daemon law_blessing_of_moses given_at Deut 33:1, installed_by boot — %s daemons, %s function blocks (twelve WRAPPED); the span\'s one range and %s CALL edges all reference (OWED pointers in the file %s); I5 82 -> %s; THE CALENDAR UNTOUCHED (%s rows); the register file untouched). '
        'THE TAPE TOOLS derived (seq_record_ch33.py, seq_stitch_ch33.py — the 21b note after 20b\'s note, NO MARKER ROW of our own) and the shells (the assembler, the fast checker, the ask checker, the cases generator, the chains, the gates shell, the scan census — the generated main\'s callee and narrative lines retyped for twelve ledgers). '
        'THE RUNNER cold_run_blessing_of_moses.py (the 78th; %d bytes; the lint %s): part 1 DERIVED (the helpers from the song\'s runner; the ink blocks from ch33_ink.py by content markers — six blocks, 19 asserts, 3 lines dropped, glossed from the store\'s own print with a small table (no apostrophe inside a gloss — the first derive tripped on one); the parser\'s hits — NO number verse, 33:23 THE FALSE SEVEN marked and counted as nothing; the tokens {33: 336}, the Name bare 7, the negations at 33:9 alone, the twins and the scans typed from the first pass\'s print by parse_ch33_fastcheck.py; THE CALLEES\' FACTS on thirty-nine runners — %s facts printed at the first pass and asserted from the print at the second, every callee CALLED by its literal name with the bindings assignments (20b\'s tail lesson built in)); parts 2-4 the eleven cells (35 asks), part 5 the readback (%s rows one per verse — %s; on the tape %s; THE TWO POINTER ROWS 33:5 and 33:28 — 20b\'s owed pointers PAID, grade R) and the DATA (%s parameters, %s rows), part 6 the daemon with 11 LITERAL submits in two forms (moses for the frame\'s act and the ten speeches), NO MARKER in the narrative and the readback\'s table; part 7 the cases GENERATED from the cells\' own asks; the fast checker %s; the ask checker %s. '
        'THE GRADED RUNS: MATRIX %s (the first run %s); %s; THE NARRATIVE %s — 28 writes on TWELVE ledgers, the counter at (12, 7), NO marker log, the writes on one day. '
        'THE GATES ALONE: the daemon gate %s (%s daemons, %s functions); the dependency gate %s (%s runners; %s; %s) — this runner\'s edges on file %d. '
        'THE TAPE: the recorder (INK_CACHE=0), the stitcher (PLACEMENT %s — the markers\' placement 20b\'s exactly; CENSUS %s — on the tape 1439 -> 1450, markers 173 UNMOVED), the literals patched (RUN (%s) from PREVIOUS_RUN (%s); DO1-DO5 — the twins\' literals read from the runner\'s print); the tape\'s runs %s (the diverges before the last %s); DO1-DO5 %d MATCH; checkpoint_check %s; THE SCAN CENSUS present %s, tripping %s. '
        'THE STATE: the tape %s; %d timed steps, %d machine seconds so far. THE CHAIN LAUNCHED (ch33b_gates.sh — the register gate --strict, the positions at four workers; DONE file ch33b_gates.DONE). NEXT: THE TAIL after a compaction — the summary read once, the demands filed from the prints, the records from the sheet in one call (the map\'s AS BUILT with the departures; this doc, the recovery page, the memory; COMPILE_DEBT\'s lean box line (15) replacing " 21b (the compile of 33): next." and adding " 22 (the reading of 34): next."), the forms, the message; THE COMMIT ON HIS WORD ONLY (sitting 21 with 21b). POST-COMPACTION REREADS: the recovery page, the map\'s newest section, MEMORY.md; then this checkpoint.'
        % (KADD, KREG, EADD, EREG, DAEM, FB, E39, OWED, I5, CAL, RSIZE, LINT_R, NFACTS, RB, RBG, RBT, PAR, NDATA, FCL, AKL, MATRIX, MATRIX1, FRAC, NARR, 'GREEN' if DMOK else 'RED', DMN, DMF, 'GREEN' if DGOK else 'RED (the demands to file at the tail)', DGL, DGE, LINKC, MINE, PLACE, CENSUS, RUN, PREV, VS, DIVS, len(set(DO)), CC, SCP, SCT, VS[-1], NSTEPS, SECS))
rec = rd(REC)
i, j = rec.index('## 2. WHERE IT STANDS'), rec.index('## 3. THE STANDING LAWS'); assert 0 < i < j
SEC2 = ('## 2. WHERE IT STANDS (2026-09-29; #242 — sitting 21b RUN B, newest)\n'
        '- NUMBERS CLOSED. DEUTERONOMY 1:1-33:29 ON THE TAPE (1-32 PUSHED through 472d2a3; 33 READ + COMPILED, uncommitted).\n'
        '- units 250 / standing 2371, hash 8b8fff1fa28953af. %s runners, %s daemons; %s kinds / %s effects.\n'
        '- THE TAPE at RUN (%s, pairs, 127); %s on its %d runs (DO1-DO5); MARKERS 173 — Moses\' last day (40, 12, 7) at 31:1, NO marker at 32 or 33; checkpoint_check %s.\n'
        '- ⚠ THE LEAN PASS (#208): 16-34 lean — core shelf, 4 records, chain once; full process OWED. A MARKER or BIG-CALLEE compile splits RUN B.\n'
        '- 21 (ch 33 READ, LEAN) DONE #240: 176 sources, 11 claims, FROZEN, chain green; UNCOMMITTED.\n'
        '- 21b RUN B (ch 33 COMPILE, LEAN) at #242: the 78th runner blessing_of_moses %s; %d edges; THE GATES CHAIN LAUNCHED, unread. NEXT: THE TAIL (the summary, the records, the debt line, the forms, the message), then the commit on his word (21 with 21b).\n\n\n'
        % (DGL, DAEM, KREG, EREG, RUN, VS[-1], len(TAPES), CC, MATRIX, MINE))
rec2 = rec[:i] + SEC2 + rec[j:]
assert len(rec2.encode('utf-8')) <= 10240, len(rec2.encode('utf-8'))
idx = rd(MM)
m = re.search(r"21b RUN A at #241 2026-09-29 \(.*?\); NEXT: RUN B after a compaction \(.*?\), the tail; the commit on his word \(21 with 21b\)", idx); assert m, 'the walk line'
NEWL = "21b RUN A + B 2026-09-29 at #242 (the 78th runner blessing_of_moses %s; %s kinds / %s effects on 12 ledgers, NO MARKER, no reuse; the tape %s; %d edges; THE CHAIN LAUNCHED, unread); NEXT: THE TAIL (the summary, the demands, the records, the debt line, the forms, the message), then the commit on his word (21 with 21b)" % (MATRIX, KADD, EADD, VS[-1], MINE)
idx = idx[:m.start()] + NEWL + idx[m.end():]
assert len(idx.encode('utf-8')) <= 17000, len(idx.encode('utf-8'))
wk = rd(MW)
def sub1(t, a, b, name):
    assert t.count(a) == 1, (name, t.count(a), a[:70]); return t.replace(a, b)
wk = sub1(wk, 'description: "SITTING 21b RUN A AT ITS CLEAN POINT 2026-09-29 (', 'description: "SITTING 21b RUN B AT ITS CLEAN POINT 2026-09-29 (chapter 33 COMPILED lean — the 78th runner blessing_of_moses %s, %s kinds in two forms / %s effects on twelve ledgers, NO MARKER, no reuse, the tape %s, %d edges, the chain LAUNCHED; NEXT THE TAIL then the commit on his word) — SITTING 21b RUN A AT ITS CLEAN POINT 2026-09-29 (' % (MATRIX, KADD, EADD, VS[-1], MINE), 'the description')
NOTE = ('\n\nSITTING 21b RUN B AT ITS CLEAN POINT 2026-09-29 — CHAPTER 33 COMPILED AND ON THE TAPE (lean): the types (%s kinds in two forms, %s effects — 28 statuses on twelve ledgers, no reuse; the daemon law_blessing_of_moses; 39 edges all reference; the calendar untouched), the runner in six parts + the generated cases (MATRIX %s; the readback %s rows with the two pointer rows 33:5 and 33:28 paid; THE NARRATIVE %s — 28 writes on twelve ledgers, NO marker), the gates alone (the daemon gate %s, the dependency gate %s — %d edges of this runner), the tape %s over %s (RUN %s), checkpoint_check %s, the scan census (tripping %s), THE GATES CHAIN LAUNCHED. '
        'THE LESSONS SO FAR: (1) the store\'s words table holds the KETIV alone — the qere\'s tokens live in the gloss print; a PHRASE on a ketiv-qere seat is typed from the words table\'s tokens (the fiery law tripped once); (2) a manual gloss carries no apostrophe — it sits inside a quoted token (the first derive tripped on three); (3) a launcher never fires on a part that failed to compile — the test on the file\'s presence is not a test on its compile (the fast checker was launched once on a bad part 1 and relaunched); (4) the registry a part reads is loaded in THAT part (part 5\'s tape-kind assert loaded event_vocabulary before part 6 did); (5) every callee CALLED by its literal name from the first derive, the bindings assignments — 20b\'s two tail lessons built in, no retype; (6) the tape\'s kin kinds and their first verses are read from the sequence file\'s own submits before the readback rows are typed (the descent at Exodus 19:18, Isaac\'s blessing at Genesis 27:27, the testament at 49:3, the crossed hands at 48:14); (7) the twin literals of DO4 are read from the runner\'s print by the patcher, never typed; (8) A CALLEE\'S OWN FACT PRINTS WEAR THE SAME FORM — the song\'s runner prints its FACT lines at import; the parser reads the facts after THIS runner\'s own header alone (the first parse typed 208 asserts, 91 of them the song\'s — KeyErrors at the second fast check); (9) THE REGISTER TEST LOOKS BACK TEN VERSES FROM A CITED VERSE — a speech may use \'and he said\', an act may not: the stitcher\'s first pass dropped the frame\'s act (no non-speech wayyiqtol at 33:1-2) and Zebulun\'s line (33:9-19 verbless); the case sources cite the frame\'s 33:2 (the speeches) and 33:5\'s \'and there was\' (the act) — the events\' placement 1448 on the first stitch, 1450 on the second; (10) the chukat cells take an ask dict and zelophehad\'s ladder wants a survivors key — the first pass\'s print corrected two guessed call forms. NEXT: THE TAIL after a compaction, then the commit on his word (21 with 21b).'
        % (KADD, EADD, MATRIX, RB, NARR, 'GREEN' if DMOK else 'RED', 'GREEN' if DGOK else 'RED', MINE, VS[-1], VS, RUN, CC, SCT))
wk = wk.rstrip('\n') + NOTE + '\n'
LINT = {}
for p in (SD, REC, MM, MW):
    r = subprocess.run(['python3', f'{ROOT}/logic/solo_tools/gloss_lint.py', p], capture_output=True, text=True); LINT[os.path.basename(p)] = int(re.search(r'(\d+) flag', r.stdout).group(1))
for txt in (P242, rec2, idx, wk): assert os.path.expanduser('~') not in txt and SP not in txt, 'a home or scratch path'
HEB = re.compile('[' + chr(0x5d0) + '-' + chr(0x5ea) + ']')
assert not HEB.search(P242 + SEC2 + NOTE + NEWL), 'no Hebrew script in the blocks'
print('THE POINT %s: #242 %d bytes; the recovery page %d; MEMORY.md %d; the walk note %d; the lints before %s' % ('CHECKED' if CHECK else 'WRITTEN', len(P242.encode()), len(rec2.encode()), len(idx.encode()), len(wk.encode()), LINT))
if not CHECK:
    open(SD, 'a', encoding='utf-8').write(P242); open(REC, 'w', encoding='utf-8').write(rec2); open(MM, 'w', encoding='utf-8').write(idx); open(MW, 'w', encoding='utf-8').write(wk)
    L2 = {}
    for p in (SD, REC, MM, MW):
        r = subprocess.run(['python3', f'{ROOT}/logic/solo_tools/gloss_lint.py', p], capture_output=True, text=True); L2[os.path.basename(p)] = int(re.search(r'(\d+) flag', r.stdout).group(1))
    assert L2 == LINT, (LINT, L2)
    print('every lint unmoved:', L2)
