import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE DEUTERONOMY WALK 20b (LEAN): THE CLEAN COMPACTION POINT at RUN B's end — the state doc's #236, the recovery page (section 2 rewritten under its cap), the memory
# (the index line and the walk note) — written in ONE call after the types, the runner, the gates alone, the tape to 10/10 and the chain's launch; every number READ FROM
# ITS PRINT (the types' prints, the runner's graded runs, the stitcher's census, the tape's verdicts and its RUN literal, checkpoint_check, the dependency and daemon gates'
# prints, the scan census, the timing table); every text built whole before a file is opened; the lints and the caps asserted. --check prints without writing.
# write_ch29b_point2.py's form WITHOUT THE MARKER. RUN FROM THE REPO ROOT with PYTHONPATH the scratchpad.
import os, re, sys, subprocess, glob
ROOT = _ROOT
SP = os.path.dirname(os.path.abspath(__file__))
MEM = os.path.expanduser('~/.claude/projects/-Users-Shared-TorahSim/memory')
CHECK = '--check' in sys.argv
SD = f'{ROOT}/logic/pre_logic_methods_2026-07-28/PROMPT_continue_solo_era_2026-08-06.md'; REC = f'{ROOT}/logic/pre_logic_methods_2026-07-28/RECOVERY_new_thread_2026-09-12.md'
MM = f'{MEM}/MEMORY.md'; MW = f'{MEM}/deuteronomy-walk.md'; SEQ = f'{ROOT}/World/step9/cold_run_sequence.py'; RUNNER = f'{ROOT}/World/step9/cold_run_song_charge_nebo.py'
def rd(p): return open(p, encoding='utf-8').read()
def R(pat, text, name, g=1):
    m = re.search(pat, text, re.M); assert m, (name, pat); return m.group(g)
ta, tb = rd(f'{SP}/ch32b_types_a.out'), rd(f'{SP}/ch32b_types_b.out')
RUNS = sorted(glob.glob(f'{SP}/ch32_runner_run*.out')); rr = rd(RUNS[-1]); r1 = rd(RUNS[0]); st = rd(f'{SP}/seq_stitch_ch32.out'); seq = rd(SEQ)
TAPES = sorted(glob.glob(f'{SP}/ch32_tape_run*.out')); CCS = sorted(glob.glob(f'{SP}/ch32_checkpoint_check*.out')); cc = rd(CCS[-1])
DGS = sorted(glob.glob(f'{SP}/ch32b_dependency_*.out'), key=os.path.getmtime); dg = rd(DGS[-1]); dm = rd(f'{SP}/ch32b_daemon_first.out'); sc = rd(f'{SP}/ch32_scan_census.out'); tsv = rd(f'{SP}/ch32b_timing.tsv')
KADD, KREG = R(r'^kinds: (\d+) added of \d+ \(14 speech / 1 act / 1 statute\), registry (\d+);', ta, 'kinds'), R(r'^kinds: \d+ added of \d+ \(14 speech / 1 act / 1 statute\), registry (\d+);', ta, 'kinds reg')
EADD, EREG, SEATS = R(r'^effects: (\d+) added \(registry (\d+)\)', ta, 'effects'), R(r'^effects: \d+ added \(registry (\d+)\)', ta, 'effects reg'), R(r'the reused rows amended with (\d+) seats', ta, 'seats')
DAEM, FB = R(r'^daemons: (\d+) \(law_song_charge_nebo True\); functions blocks: (\d+);', tb, 'daemons'), R(r'functions blocks: (\d+);', tb, 'fb')
E42, PTRS0 = R(r'^dependency: the span \(one range\) \+ (\d+) edges', tb, 'e42'), R(r'; edges \d+, pointers (\d+)$', tb, 'pointers0')
I5, CAL = R(r'^installation_probes I5: (\d+)', tb, 'i5'), R(r'^calendar: (\d+) parameters', tb, 'cal')
assert (KADD, KREG, EADD, EREG, SEATS, DAEM, FB, E42, I5, CAL) == ('16', '1269', '42', '1441', '3', '82', '76', '42', '82', '75'), (KADD, KREG, EADD, EREG, SEATS, DAEM, FB, E42, I5, CAL)
MATRIX = re.findall(r'^MATRIX: (\d+/\d+) cells match the answer sheet$', rr, re.M)[-1]; MATRIX1 = re.findall(r'^MATRIX: (\d+/\d+) cells', r1, re.M)[-1]; assert MATRIX.split('/')[0] == MATRIX.split('/')[1], (MATRIX, MATRIX1)
FRAC = re.findall(r'^FRACTIONS: (pure ink \d+/\d+ \(\d+%\) · named moves \d+/\d+ \(\d+%\) · data \d+/\d+ \(\d+%\)) ·', rr, re.M)[-1]
RB = R(r'^THE READBACK — THE FORMS ON FILE, NO NEW FORM: (\d+) rows — ', rr, 'readback'); RBG = R(r'^THE READBACK — THE FORMS ON FILE, NO NEW FORM: \d+ rows — (\{[^}]+\});', rr, 'grades'); RBT = R(r'^THE READBACK — THE FORMS ON FILE, NO NEW FORM: \d+ rows — \{[^}]+\}; on the tape (\d+),', rr, 'on tape')
PAR, NDATA = R(r'the parameters (\d+) \(in the registry (\d+), in DATA \d+\); DATA rows (\d+)$', rr, 'parameters'), R(r'; DATA rows (\d+)$', rr, 'data'); INREG = R(r'the parameters \d+ \(in the registry (\d+),', rr, 'in registry')
NARR = R(r'^THE NARRATIVE: (\(\d+, \d+, \d+, \(\d+, \d+\), \d+, \d+, \d+, \d+, \[[^\]]*\]\))', rr, 'narrative')
LINT_R = re.search(r'(\d+) flag', subprocess.run(['python3', f'{ROOT}/logic/solo_tools/gloss_lint.py', RUNNER], capture_output=True, text=True).stdout).group(1); assert LINT_R == '0', LINT_R
PLACE = R(r"^PLACEMENT LITERAL: (\{.*\})$", st, 'placement'); CENSUS = R(r'^  CENSUS tuple \([^)]*\): (\(.*\))$', st, 'census')
RUN = R(r'^RUN = \((\d+, \d+, \d+, \d+, \d+, \d+, \d+, \d+),', seq, 'RUN'); PREV = R(r'^PREVIOUS_RUN = \((\d+, \d+, \d+, \d+, \d+, \d+, \d+, \d+),', seq, 'PREV'); assert PREV == '1423, 102, 94, 0, 12, 2003, 52, 319', (RUN, PREV)
VS = [(re.search(r'^(\d+/10) checkpoints$', rd(t), re.M).group(1) if re.search(r'^(\d+/10) checkpoints$', rd(t), re.M) else 'TRIPPED') for t in TAPES]; assert VS[-1] == '10/10', VS
def divs(t): return sorted(set(l.split()[1] for l in t.split('\n') if l.lstrip().startswith('CHECKPOINT ') and l.split()[-1] == 'DIVERGE'))
BASE = divs(rd(TAPES[-1])); DIVS = [[d for d in divs(rd(t)) if d not in BASE] for t in TAPES[:-1]]
DN = [l.split()[1] for l in rd(TAPES[-1]).split('\n') if re.match(r'\s*CHECKPOINT DN\d', l) and l.split()[-1] == 'MATCH']; assert len(set(DN)) == 5, DN
MK = R(r'^  CENSUS tuple \([^)]*\): \((?:\d+, ){9}(\d+),', st, 'markers in the census'); assert MK == '173', MK
CC = R(r'^checkpoint_check: (\d+ rows, \d+ miss, \d+ raised)', cc, 'checkpoint_check'); assert CC.endswith('0 raised'), CC
DGL = R(r'^DEPENDENCY GATE coverage: (\d+) runners declared', dg, 'runners'); DGE = R(r'dispositions on file: (\d+ edges, \d+ pointers)$', dg, 'edges'); DGOK = 'gate satisfied' in dg
LINKC = R(r'^LINK CENSUS \(the link review law\): (reference \d+, transfer \d+, hypothesis \d+, none \d+)', dg, 'link census')
import yaml as _y; _dd = _y.safe_load(open(f'{ROOT}/World/step9/dependency_dispositions.yaml', encoding='utf-8')); MINE = len([e for e in _dd['edges'] if e.get('from') == 'song_charge_nebo']); ONFILE = len(_dd['edges']); NPTR = len(_dd['pointers']); OWED = len([p for p in _dd['pointers'] if p.get('disposition') == 'OWED'])
assert DGE.startswith('%d edges, %d pointers' % (ONFILE, NPTR)), (DGE, ONFILE, NPTR)
DMN, DMF = R(r'regenerated \((\d+) daemons, (\d+) functions\)', dm, 'daemons'), R(r'regenerated \(\d+ daemons, (\d+) functions\)', dm, 'functions'); DMOK = 'gate satisfied' in dm; assert DMN == DAEM
SCP, SCT = R(r'chapter 32 present: (\d+) \[', sc, 'present'), R(r'^SCAN CENSUS DONE — runner scans tripping: (\d+)$', sc, 'tripping')   # the census scans israel_people alone — READ FROM THE PRINT (the six on Joshua and Moses outside its scan)
RSIZE = os.path.getsize(RUNNER)
rows = [l.split('\t') for l in tsv.split('\n') if l.split('\t')[1:2] and l.split('\t')[1].startswith('20b ')]; NSTEPS = len(rows); SECS = sum(int(r[2]) for r in rows)
FC = sorted(glob.glob(f'{SP}/ch32_fastcheck_run*.out')); FCL = rd(FC[-1]).strip().split('\n')[-1]; AK = sorted(glob.glob(f'{SP}/ch32_askcheck_run*.out')); AKL = rd(AK[-1]).strip().split('\n')[-1]
print('THE PRINTS: kinds +%s -> %s, effects +%s -> %s (%s seats), daemons %s, blocks %s, edges %s, I5 %s, calendar %s; MATRIX %s (run 1 %s); %s; readback %s rows %s on the tape %s; parameters %s (in the registry %s), DATA %s; NARRATIVE %s; runner %d bytes lint %s; PLACEMENT %s; CENSUS %s; RUN (%s) from (%s); the tape %s, the diverges before the last %s; DN %d; checkpoint_check %s; the daemon gate %s (%s daemons, %s functions); the dependency gate %s (%s runners, %s; %s) — mine %d, on file %d edges, %d pointers, OWED %d; the scan census present %s tripping %s; the fast checker %s; the ask checker %s; %d steps, %d s' % (KADD, KREG, EADD, EREG, SEATS, DAEM, FB, E42, I5, CAL, MATRIX, MATRIX1, FRAC, RB, RBG, RBT, PAR, INREG, NDATA, NARR, RSIZE, LINT_R, PLACE, CENSUS, RUN, PREV, VS, DIVS, len(set(DN)), CC, 'GREEN' if DMOK else 'RED', DMN, DMF, 'GREEN' if DGOK else 'RED', DGL, DGE, LINKC, MINE, ONFILE, NPTR, OWED, SCP, SCT, FCL, AKL, NSTEPS, SECS))
sd = rd(SD); assert '\n#236 ' not in sd and '\n#235 (' in sd
P236 = ('\n\n#236 (2026-09-28, THE DEUTERONOMY WALK sitting 20b — CHAPTER 32\'s COMPILE IN THE LEAN FORM, THE SONG, RUN B of two; on the owner\'s "Reread and go" after the compaction at #235 — no commit word said since 7798bee, the tree UNCOMMITTED with the post-push records and RUN A\'s and RUN B\'s files; A CLEAN COMPACTION POINT AT RUN B\'S END, THE GATES CHAIN LAUNCHED IN THE BACKGROUND (its summary to be read once at the tail): '
        'THE REREADS done (the recovery page, the map\'s newest section — the design\'s THE ORDER paragraph and the whole, MEMORY.md, #235; the spec module ch32b_spec.py before the types; THE_STEPS Step 5\'s head and the compiler block). '
        'THE TYPES BY SCRIPT (add_types_ch32_a.py: %s kinds IN THREE FORMS — 14 speech, 1 act, 1 statute — on the registry (%s); %s effects (%s) — 32 statuses, 10 heaven entries, no block on three ledgers (Israel 36, Moses 5, Joshua 1 under the Hebrew key yehoshua), every `he` FOUND in its verse from the store\'s own print; the three reused rows amended with %s seats (heaven_and_earth_witness 32:1 the fifth, face_hidden_and_forsaken_foretold 32:20 the second, length_of_days_on_the_land_promised 32:47 the second); the reused and referenced rows\' ops READ from the registry\'s print (treasured_people a heaven entry, gathered_to_his_people a status — the first check tripped on a typed guess); add_types_ch32_b.py: the daemon law_song_charge_nebo given_at Deut 32:1, installed_by boot — %s daemons, %s function blocks (seventeen WRAPPED); the span\'s one range and %s CALL edges all reference (OWED pointers in the file %s); I5 81 -> %s; THE CALENDAR UNTOUCHED (%s rows); the register file untouched). '
        'THE TAPE TOOLS derived (seq_record_ch32.py, seq_stitch_ch32.py — the 20b note after 19b\'s note and its marker row, NO MARKER ROW of our own) and the shells (the assembler, the fast checker, the ask checker, the cases generator, the chains, the gates shell, the scan census — the generated main\'s callee and narrative lines retyped for three ledgers). '
        'THE RUNNER cold_run_song_charge_nebo.py (the 77th; %d bytes; the lint %s): part 1 DERIVED (the helpers from the chapter 29-31 runner; the ink blocks from ch32_ink.py by content markers — six blocks, 12 asserts, 3 lines dropped, glossed from the store\'s own print with a small table; the parser\'s hits [8] THE FALSE EIGHT at 32:15 and [1, 1002] THE JOINED THOUSAND at 32:30 — the chapter\'s one number verse, no count; the tokens {32: 615}, the Name bare 7, the negations at ten verses, the twins and the scans typed from the first pass\'s print by parse_ch32_fastcheck.py; THE CALLEES\' FACTS on forty-two runners — 99 facts printed at the first pass and asserted from the print at the second (the repr\'s first sixty characters, typed by the parser), the shelach alias SHL (19b\'s lesson 3 met again — SH the shared-run measure)); parts 2-4 the sixteen cells (65 asks), part 5 the readback (%s rows one per verse — %s; on the tape %s) and the DATA (%s parameters, %s rows), part 6 the daemon with 16 LITERAL submits in three forms (moses for the song\'s stanzas and the act, israel for the statute, god for the two summons speeches), NO MARKER in the narrative and the readback\'s table; part 7 the cases GENERATED from the cells\' own asks; the fast checker %s; the ask checker %s. '
        'THE GRADED RUNS: MATRIX %s (the first run %s); %s; THE NARRATIVE %s — 45 writes on THREE ledgers (Israel 39, Joshua 1, Moses 5), the counter at (12, 7), NO marker log, the writes on one day. '
        'THE GATES ALONE: the daemon gate %s (%s daemons, %s functions); the dependency gate %s (%s runners; %s; %s) — this runner\'s edges on file %d. '
        'THE TAPE: the recorder (INK_CACHE=0), the stitcher (PLACEMENT %s — the markers\' placement 19b\'s exactly; CENSUS %s — on the tape 1423 -> 1439, markers 173 UNMOVED), the literals patched (RUN (%s) from PREVIOUS_RUN (%s); DN1-DN5); the tape\'s runs %s (the diverges before the last %s); DN1-DN5 %d MATCH; checkpoint_check %s; THE SCAN CENSUS present %s, tripping %s. '
        'THE STATE: the tape %s; %d timed steps, %d machine seconds so far. THE CHAIN LAUNCHED (ch32b_gates.sh — the register gate --strict, the positions at four workers; DONE file ch32b_gates.DONE). NEXT: THE TAIL after a compaction — the summary read once, the demands filed from the prints, the records from the sheet in one call (the map\'s AS BUILT with the departures — 22 -> 21 Mishnah rows at RUN A, the reused rows\' ops read not typed, the alias; this doc, the recovery page, the memory; COMPILE_DEBT\'s lean box line (13) replacing " 20b (the compile of 32): next." and adding " 21 (the reading of 33): next."), the forms, the message; THE COMMIT ON HIS WORD ONLY. POST-COMPACTION REREADS: the recovery page, the map\'s newest section, MEMORY.md; then this checkpoint.'
        % (KADD, KREG, EADD, EREG, SEATS, DAEM, FB, E42, OWED, I5, CAL, RSIZE, LINT_R, RB, RBG, RBT, PAR, NDATA, FCL, AKL, MATRIX, MATRIX1, FRAC, NARR, 'GREEN' if DMOK else 'RED', DMN, DMF, 'GREEN' if DGOK else 'RED (the demands to file at the tail)', DGL, DGE, LINKC, MINE, PLACE, CENSUS, RUN, PREV, VS, DIVS, len(set(DN)), CC, SCP, SCT, VS[-1], NSTEPS, SECS))
rec = rd(REC)
i, j = rec.index('## 2. WHERE IT STANDS'), rec.index('## 3. THE STANDING LAWS'); assert 0 < i < j
SEC2 = ('## 2. WHERE IT STANDS (2026-09-28; #236 — sitting 20b RUN B, newest)\n'
        '- NUMBERS CLOSED. DEUTERONOMY 1:1-32:52 ON THE TAPE (1-31 PUSHED through c4b14ce; 32 READ PUSHED 7798bee; 32\'s compile uncommitted).\n'
        '- units 249 / standing 2360, hash 8b8fff1fa28953af. %s runners, %s daemons; %s kinds / %s effects.\n'
        '- THE TAPE at RUN (%s, pairs, 127); %s on its %d runs (DN1-DN5); MARKERS 173 — Moses\' last day (40, 12, 7) at 31:1, NO marker at 32; checkpoint_check %s.\n'
        '- ⚠ THE LEAN PASS (#208): 16-34 in 8 lean sittings — core shelf, 4 records, chain once; full process OWED.\n'
        '- SITTING 20b RUN B (ch 32 COMPILE, LEAN) at #236: the 77th runner song_charge_nebo %s; %d edges; THE GATES CHAIN LAUNCHED (its summary not yet read). NEXT: THE TAIL (the summary once, the demands, the records, COMPILE_DEBT\'s line, the forms, the message), then the commit on his word.\n\n\n'
        % (DGL, DAEM, KREG, EREG, RUN, VS[-1], len(TAPES), CC, MATRIX, MINE))
rec2 = rec[:i] + SEC2 + rec[j:]
assert len(rec2.encode('utf-8')) <= 10240, len(rec2.encode('utf-8'))
idx = rd(MM)
m = re.search(r"20b RUN A at #235 2026-09-28 \(.*?\); NEXT: RUN B after a compaction \(.*?\), then the tail; the commit on his word", idx); assert m, 'the walk line'
NEWL = "20b RUN A + RUN B 2026-09-28 at #236 (the design; the types %s kinds in three forms / %s effects + %s seats; the 77th runner song_charge_nebo %s in six parts + the generated cases; NO MARKER — Moses' last day (40, 12, 7), markers 173; the tape %s; %d edges; THE GATES CHAIN LAUNCHED, its summary unread); NEXT: THE TAIL (the summary read once, the demands, the records, COMPILE_DEBT's line, the forms, the message), then the commit on his word" % (KADD, EADD, SEATS, MATRIX, VS[-1], MINE)
idx = idx[:m.start()] + NEWL + idx[m.end():]
assert len(idx.encode('utf-8')) <= 17000, len(idx.encode('utf-8'))
wk = rd(MW)
def sub1(t, a, b, name):
    assert t.count(a) == 1, (name, t.count(a), a[:70]); return t.replace(a, b)
wk = sub1(wk, 'description: "SITTING 20b RUN A AT ITS CLEAN POINT 2026-09-28 (', 'description: "SITTING 20b RUN B AT ITS CLEAN POINT 2026-09-28 (chapter 32 COMPILED lean — the 77th runner song_charge_nebo %s, %s kinds in three forms / %s effects, NO MARKER, the tape %s, %d edges, the chain LAUNCHED; NEXT THE TAIL then the commit on his word) — SITTING 20b RUN A AT ITS CLEAN POINT 2026-09-28 (' % (MATRIX, KADD, EADD, VS[-1], MINE), 'the description')
NOTE = ('\n\nSITTING 20b RUN B AT ITS CLEAN POINT 2026-09-28 — CHAPTER 32 COMPILED AND ON THE TAPE (lean): the types (%s kinds in three forms, %s effects — 32 statuses, 10 heaven on three ledgers; the three reused rows amended with %s seats; the daemon law_song_charge_nebo; 42 edges all reference; the calendar untouched), the runner in six parts + the generated cases (MATRIX %s; the readback %s rows; THE NARRATIVE %s — 45 writes on three ledgers, NO marker), the gates alone (the daemon gate %s, the dependency gate %s — %d edges of this runner), the tape %s over %s (RUN %s), checkpoint_check %s, the scan census (tripping %s), THE GATES CHAIN LAUNCHED. '
        'THE LESSONS SO FAR: (1) the registry\'s ops are read, never typed (treasured_people a heaven entry, gathered_to_his_people a status — the types\' first check tripped); (2) the store\'s glosses carry apostrophes — dropped before they sit inside a quoted token; (3) the shelach alias collides again (SHL — 19b\'s lesson 3 stands as a rule: no two-letter alias that is a helper\'s name); (4) a DATA row\'s value is under \'value\', a q-cell\'s under \'v\' — the facts\' printer reads both or prints None; (5) the facts\' asserts are WRITTEN BY THE PARSER from the print (99 lines) — no hand typing of a callee\'s words; (6) the generated main\'s callee and narrative lines are the sitting\'s own (the derive\'s substitutions leave 19b\'s fact names — retyped before the first graded run). NEXT: THE TAIL after a compaction, then the commit on his word.'
        % (KADD, EADD, SEATS, MATRIX, RB, NARR, 'GREEN' if DMOK else 'RED', 'GREEN' if DGOK else 'RED', MINE, VS[-1], VS, RUN, CC, SCT))
wk = wk.rstrip('\n') + NOTE + '\n'
LINT = {}
for p in (SD, REC, MM, MW):
    r = subprocess.run(['python3', f'{ROOT}/logic/solo_tools/gloss_lint.py', p], capture_output=True, text=True); LINT[os.path.basename(p)] = int(re.search(r'(\d+) flag', r.stdout).group(1))
for txt in (P236, rec2, idx, wk): assert os.path.expanduser('~') not in txt and SP not in txt, 'a home or scratch path'
assert not re.search(r'[֐-׿]', P236 + SEC2 + NOTE + NEWL), 'no Hebrew script in the blocks'
print('THE POINT %s: #236 %d bytes; the recovery page %d; MEMORY.md %d; the walk note %d; the lints before %s' % ('CHECKED' if CHECK else 'WRITTEN', len(P236.encode()), len(rec2.encode()), len(idx.encode()), len(wk.encode()), LINT))
if not CHECK:
    open(SD, 'a', encoding='utf-8').write(P236); open(REC, 'w', encoding='utf-8').write(rec2); open(MM, 'w', encoding='utf-8').write(idx); open(MW, 'w', encoding='utf-8').write(wk)
    L2 = {}
    for p in (SD, REC, MM, MW):
        r = subprocess.run(['python3', f'{ROOT}/logic/solo_tools/gloss_lint.py', p], capture_output=True, text=True); L2[os.path.basename(p)] = int(re.search(r'(\d+) flag', r.stdout).group(1))
    assert L2 == LINT, (LINT, L2)
    print('every lint unmoved:', L2)
