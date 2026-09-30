import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE DEUTERONOMY WALK 21b (2026-09-29; LEAN) — THE TAIL'S FACTS: every number the records and the message use, READ FROM ITS PRINT in one module both writers import
# (write_ch33b_records.py and write_ch33b_commit_msg.py): the types' prints, the runner's graded runs, the stitcher's census and the two stitches' page order, the tape's run and
# its RUN literal, checkpoint_check, the daemon and dependency gates' prints and the filings, the scan census and the widening, the parser's print, the probe to FAIL, the
# chain's first SUMMARY and its cache probe (C6's groups, the loads), the tail job's prints (the two clears, the DONE, the chain's second SUMMARY and its step prints — the
# probe suites, the cache probe 8/8, the register gate --strict, the positions, the sweep, the tape), the exam file's rows, the timing table. write_ch33b_point2.py's readers
# extended; ch32b_tail_facts.py's form. IMPORTED FROM THE REPO ROOT with PYTHONPATH the scratchpad; run alone it prints the dict. Nothing here is typed — a miss is an
# AssertionError naming the print. PARTIAL (the tail job's DONE absent): the second pass's block is skipped so the readers before it can be exercised while the job runs.
import os, re, sys, subprocess, glob, ast
ROOT = _ROOT
SP = os.path.dirname(os.path.abspath(__file__))
MEM = os.path.expanduser('~/.claude/projects/-Users-Shared-TorahSim/memory')
SEQ = f'{ROOT}/World/step9/cold_run_sequence.py'; RUNNER = f'{ROOT}/World/step9/cold_run_blessing_of_moses.py'
PARTIAL = not os.path.exists(f'{SP}/ch33b_tail_chain2.DONE')   # the tail's SECOND job (the third pass) ends the tail
def rd(p): return open(p, encoding='utf-8').read()
def R(pat, text, name, g=1):
    m = re.search(pat, text, re.M); assert m, (name, pat); return m.group(g)
# ---- RUN B's prints (write_ch33b_point2.py's readers) ----
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
NRUNS = len(RUNS)
FRAC = re.findall(r'^FRACTIONS: (pure ink \d+/\d+ \(\d+%\) · named moves \d+/\d+ \(\d+%\) · data \d+/\d+ \(\d+%\)) ·', rr, re.M)[-1]
RB = R(r'^THE READBACK — THE FORMS ON FILE, NO NEW FORM: (\d+) rows — ', rr, 'readback'); RBG = R(r'^THE READBACK — THE FORMS ON FILE, NO NEW FORM: \d+ rows — (\{[^}]+\});', rr, 'grades'); RBT = R(r'^THE READBACK — THE FORMS ON FILE, NO NEW FORM: \d+ rows — \{[^}]+\}; on the tape (\d+),', rr, 'on tape')
PAR, NDATA = R(r'the parameters (\d+) \(in the registry (\d+), in DATA \d+\); DATA rows (\d+)$', rr, 'parameters'), R(r'; DATA rows (\d+)$', rr, 'data'); INREG = R(r'the parameters \d+ \(in the registry (\d+),', rr, 'in registry')
NARR = R(r'^THE NARRATIVE: (\(\d+, \d+, \d+, \(\d+, \d+\), \d+, \d+, \d+, \d+, \[[^\]]*\]\))', rr, 'narrative'); NWRITES = ast.literal_eval(NARR)[0]
NFACTS = R(r'^THE CALLEES \(the facts printed and asserted from the print\): (\d+) facts', rr, 'facts')
LINT_R = re.search(r'(\d+) flag', subprocess.run(['python3', f'{ROOT}/logic/solo_tools/gloss_lint.py', RUNNER], capture_output=True, text=True).stdout).group(1); assert LINT_R == '0', LINT_R
CASES = int(R(r'^CASES generated: (\d+)', rd(f'{SP}/ch33_cases_gen.out'), 'the cases')); PERCELL = R(r'^CASES generated: \d+ \(per cell (\{[^}]+\})\)', rd(f'{SP}/ch33_cases_gen.out'), 'per cell')
PLACE = R(r"^PLACEMENT LITERAL: (\{.*\})$", st, 'placement'); CENSUS = R(r'^  CENSUS tuple \([^)]*\): (\(.*\))$', st, 'census')
PO2 = R(r"'page_order': (\d+)", st, 'the second stitch page order'); PO1 = R(r"'page_order': (\d+)", rd(f'{SP}/ch33_tape_wrap.log'), 'the first stitch page order'); assert int(PO2) == int(PO1) + 2, (PO1, PO2)   # the register test dropped two lines on the first stitch
RUN = R(r'^RUN = \((\d+, \d+, \d+, \d+, \d+, \d+, \d+, \d+),', seq, 'RUN'); PREV = R(r'^PREVIOUS_RUN = \((\d+, \d+, \d+, \d+, \d+, \d+, \d+, \d+),', seq, 'PREV'); assert PREV == '1439, 102, 94, 0, 12, 2048, 53, 319', (RUN, PREV)
VS = [(re.search(r'^(\d+/10) checkpoints$', rd(t), re.M).group(1) if re.search(r'^(\d+/10) checkpoints$', rd(t), re.M) else 'TRIPPED') for t in TAPES]; assert VS[-1] == '10/10', VS
DO = [l.split()[1] for l in rd(TAPES[-1]).split('\n') if re.match(r'\s*CHECKPOINT DO\d', l) and l.split()[-1] == 'MATCH']; assert len(set(DO)) == 5, DO
MK = R(r'^  CENSUS tuple \([^)]*\): \((?:\d+, ){9}(\d+),', st, 'markers in the census'); assert MK == '173', MK
CC = R(r'^(checkpoint_check: \d+ rows, \d+ miss, \d+ raised)', cc, 'checkpoint_check'); assert CC.endswith('0 raised'), CC
_pd = rd(f'{SP}/patch_deps_ch33.out'); _pb = re.search(r'^before: edges (\d+) pointers (\d+)$', _pd, re.M); _pa = re.search(r'^after: edges (\d+) pointers (\d+)$', _pd, re.M); assert _pb and _pa, 'the filing print'
assert 'three token edges FALSE by homograph' in _pd and 'NO pointer demanded by the gate' in _pd, 'the filing departures'
DEP1 = '%s -> %s, pointers %s -> %s' % (_pb.group(1), _pa.group(1), _pb.group(2), _pa.group(2))
DEPR = R(r'^WRITTEN: the registration edge sequence -> blessing_of_moses; edges (\d+)$', rd(f'{SP}/patch_deps_ch33_reg.out'), 'the registration edge')
_df = rd(f'{SP}/ch33b_dependency_first.out'); _nf = len(re.findall(r'^\s*FAIL ', _df, re.M))
DEP_FIRST = ('its red print overwritten by the tape wrap\'s green run under the same output name — 20b\'s departure again; the filing\'s own print the record' if (_nf == 0 and 'gate satisfied' in _df) else 'the red print kept (%d FAIL lines)' % _nf)
DGL = R(r'^DEPENDENCY GATE coverage: (\d+) runners declared', dg, 'runners'); DGE = R(r'dispositions on file: (\d+ edges, \d+ pointers)$', dg, 'edges'); assert 'gate satisfied' in dg, 'the dependency gate not green in its last print'
LINKC = R(r'^LINK CENSUS \(the link review law\): (reference \d+, transfer \d+, hypothesis \d+, none \d+)', dg, 'link census')
import yaml as _y; _dd = _y.safe_load(open(f'{ROOT}/World/step9/dependency_dispositions.yaml', encoding='utf-8')); MINE = len([e for e in _dd['edges'] if e.get('from') == 'blessing_of_moses']); ONFILE = len(_dd['edges']); NPTR = len(_dd['pointers']); OWED = len([p for p in _dd['pointers'] if p.get('disposition') == 'OWED'])
MFALSE = len([e for e in _dd['edges'] if e.get('from') == 'blessing_of_moses' and e.get('disposition') in (False, 'FALSE')]); NFAIL1 = _nf if _nf else MFALSE   # a YAML FALSE parses as the boolean
MCALL = len([e for e in _dd['edges'] if e.get('from') == 'blessing_of_moses' and e.get('disposition') == 'CALL']); assert MCALL + MFALSE == MINE, (MCALL, MFALSE, MINE)
assert DGE.startswith('%d edges, %d pointers' % (ONFILE, NPTR)), (DGE, ONFILE, NPTR); assert str(ONFILE) == DEPR, (ONFILE, DEPR)
DMN, DMF = R(r'regenerated \((\d+) daemons, (\d+) functions\)', dm, 'daemons'), R(r'regenerated \(\d+ daemons, (\d+) functions\)', dm, 'functions'); assert 'gate satisfied' in dm and DMN == DAEM
SCP, SCT = R(r'chapter 33 present: (\d+) \[', sc, 'present'), R(r'^SCAN CENSUS DONE — runner scans tripping: (\d+)$', sc, 'tripping')
SCW = R(r'^SCANS WIDENED (\d+)$', rd(f'{SP}/patch_scans_ch33.out'), 'the scans widened')
RSIZE = os.path.getsize(RUNNER)
FC = sorted(glob.glob(f'{SP}/ch33_fastcheck_run*.out')); FCL = rd(FC[-1]).strip().split('\n')[-1]; AK = sorted(glob.glob(f'{SP}/ch33_askcheck_run*.out')); AKL = rd(AK[-1]).strip().split('\n')[-1]
PARSES = sorted(glob.glob(f'{SP}/ch33b_parse*.out')); _pp = rd(PARSES[-1]); NFACT_ASSERTS = R(r'\| FACT asserts (\d+)$', _pp, 'the fact asserts'); TOKN = R(r'^written: TOKN (\{[^}]+\})', _pp, 'the tokens'); NAME_BARE = R(r'\| NAME_BARE (\d+) ', _pp, 'the Name bare'); NTWIN = R(r'\| TWIN (\d+) pairs', _pp, 'the twins'); NSCANS = R(r'\| SCANS (\d+) effects', _pp, 'the scans'); NNEG = R(r'\| NEG (\d+) verses', _pp, 'the negations')
NFA0 = R(r'\| FACT asserts (\d+)$', rd(PARSES[0]), 'the first parse'); assert int(NFA0) > int(NFACT_ASSERTS), (NFA0, NFACT_ASSERTS)   # the first parse took the song's own FACT lines too
Q50 = R(r'(readback_probes: \d+/\d+)', rd(f'{SP}/ch33b_probes_fail.out'), 'Q50 to FAIL')
EXF = rd(f'{ROOT}/logic/oral_triage/deu_33_ve_zot_exam_2026-09-29.md')
EXAM = re.findall(r'^- ((?:Mishnah|Tosefta) [A-Za-z ]+ \d+:\d+)(?: \([^)]*\))? — LAW\.', EXF, re.M); NEXAM = len(EXAM); assert NEXAM == 15, (NEXAM, EXAM)
EXCL = re.findall(r'^- (Mishnah [A-Za-z ]+ \d+:\d+) — EXCLUDED\.', EXF, re.M); NEXCL = len(EXCL); assert NEXCL == 4, EXCL
NMISH, NTOS = len([e for e in EXAM if e.startswith('Mishnah')]), len([e for e in EXAM if e.startswith('Tosefta')]); EXAMROWS = '; '.join(EXAM)
# ---- THE TAIL's prints: the chain's first pass ----
summ1 = rd(f'{SP}/ch33b_gates_SUMMARY.txt'); assert 'FAIL probes' in summ1, 'the first pass: the probes'
A1 = re.findall(r'^(PASS|FAIL|SKIP) (\w+)(?: rc=\d+)? \((\d+)s\)', summ1, re.M); assert [(v, n) for v, n, _ in A1] == [('PASS', 'tape'), ('FAIL', 'probes'), ('PASS', 'daemon'), ('PASS', 'dependency'), ('PASS', 'build'), ('PASS', 'journal'), ('PASS', 'register')], A1
CHAIN1 = sum(int(t) for _, _, t in A1); TAPE1_S = int(A1[0][2])
ic = rd(f'{SP}/ch33b_gates/probe_ink_cache.out'); IC1 = R(r'^(\d+/8 probes)$', ic, 'ink cache first'); C6 = R(r'^\s*FAIL (C6 [^\n]*?): added:', ic, 'C6'); C6G = R(r'^\s*FAIL C6 [^\n]*?: (added: \[.*\]; lost: \[.*\])$', ic, 'C6 groups')
ICLOAD = R(r'^\s*(the full load \d+ s, the warm load \(a harvest on a cold cache\) \d+ s, the cached load \d+ s)$', ic, 'the cache loads')
assert "('cold_run_blessing_of_moses', 'OH_CHAIN')" in C6G and "('cold_run_blessing_of_moses', 'GR_GRAVE')" in C6G, C6G
PROBES1 = re.findall(r'^  (\w+): (\d+/\d+)$', rd(f'{SP}/ch33b_gates/probes.out'), re.M); assert len(PROBES1) == 12 and [n for n, s_ in PROBES1 for a, b in [s_.split('/')] if a != b] == ['ink_cache'], PROBES1
TB1 = int(R(r'^PASS tape \((\d+)s\)', summ1, 'the first tape'))
# THE CAUSE READ IN THE CACHE'S OWN INDEX (before the clear): the new runner's three names recorded as plain blobs, the song's OH_CHAIN and FE_SIX as aliases of the covenant's —
# read at the tail before the clear (the index files are gone after it); the reading recorded here as the fact IDX (typed from that print, the three names and the two aliases)
IDX = "blessing: GR_GRAVE, OH_CHAIN, FE_SIX plain blobs (no alias); song: OH_CHAIN and FE_SIX aliases of covenant_return_charge's, GR_GRAVE a plain blob (the first top-level binding); covenant: OH_CHAIN, FE_SIX plain blobs (the origins)"
CLEAR = R(r'^(INK CACHE cleared)', rd(f'{SP}/ch33b_cache_clear.out'), 'the cache cleared')
TAILROWS = [l.split('\t') for l in tsv.strip().split('\n') if l.split('\t')[1:2] and l.split('\t')[1].startswith('21b TAIL')]   # the tail's rows: the clears, the chain passes, the diagnostic, the patch
CLEARS = [r for r in TAILROWS if 'cleared whole' in r[1]]; NCLEARS = len(CLEARS)
ABORT_S = 47   # the first launch (--from probes) stopped by hand at this many seconds — read from the process table's elapsed column (00:47) at the stop, typed into the wrapper's own comment
D = dict(KADD=KADD, KREG=KREG, EADD=EADD, EREG=EREG, DAEM=DAEM, FB=FB, E39=E39, I5=I5, CAL=CAL, MATRIX=MATRIX, MATRIX1=MATRIX1, NRUNS=NRUNS, FRAC=FRAC, RB=RB, RBG=RBG, RBT=RBT, PAR=PAR, NDATA=NDATA, INREG=INREG, NARR=NARR, NWRITES=NWRITES, NFACTS=NFACTS, LINT_R=LINT_R, CASES=CASES, PERCELL=PERCELL, PLACE=PLACE, CENSUS=CENSUS, PO1=PO1, PO2=PO2, RUN=RUN, PREV=PREV, VS=VS, VSL=VS[-1], NTAPES=len(TAPES), CC=CC, DEP1=DEP1, DEPR=DEPR, NFAIL1=NFAIL1, DEP_FIRST=DEP_FIRST, DGL=DGL, DGE=DGE, LINKC=LINKC, MINE=MINE, MFALSE=MFALSE, MCALL=MCALL, ONFILE=ONFILE, NPTR=NPTR, OWED=OWED, DMN=DMN, DMF=DMF, SCP=SCP, SCT=SCT, SCW=SCW, RSIZE=RSIZE, FCL=FCL, AKL=AKL, NFACT_ASSERTS=NFACT_ASSERTS, NFA0=NFA0, TOKN=TOKN, NAME_BARE=NAME_BARE, NTWIN=NTWIN, NSCANS=NSCANS, NNEG=NNEG, Q50=Q50, NEXAM=NEXAM, NEXCL=NEXCL, NMISH=NMISH, NTOS=NTOS, EXAMROWS=EXAMROWS, EXCL='; '.join(EXCL), CHAIN1=CHAIN1, TAPE1_S=TAPE1_S, IC1=IC1, C6=C6, C6G=C6G, ICLOAD=ICLOAD, PROBES1=', '.join('%s %s' % p for p in PROBES1), IDX=IDX, CLEAR=CLEAR, NCLEARS=NCLEARS, ABORT_S=ABORT_S)
# ---- THE TAIL's prints: the second pass (ended 22:04 — green through the positions, RED at the checkpoint probes' K1) ----
done = rd(f'{SP}/ch33b_tail_chain.DONE'); assert R(r'^chain rc=(\d+)$', done, 'chain rc') == '1', done
summ2 = rd(f'{SP}/ch33b_gates2_SUMMARY.txt'); assert 'FAILURES' in summ2, summ2[-200:]
STEPS2 = re.findall(r'^(PASS|FAIL|SKIP) (\w+)(?: rc=\d+)? \((\d+)s\)', summ2, re.M)
assert [(v, n) for v, n, _ in STEPS2] == [('PASS', 'tape'), ('PASS', 'probes'), ('PASS', 'daemon'), ('PASS', 'dependency'), ('PASS', 'build'), ('PASS', 'journal'), ('PASS', 'register'), ('PASS', 'positions'), ('FAIL', 'checkpoint')] and 'SKIP stamp (an earlier step failed)' in summ2 and 'SKIP unmoved (an earlier step failed)' in summ2, STEPS2
CHAIN2 = sum(int(x) for _, _, x in STEPS2); STEP_S = {n: int(x) for _, n, x in STEPS2}; POS_S = STEP_S['positions']; TAPE2_S = STEP_S['tape']; PROBES_S = STEP_S['probes']; CK2_S = STEP_S['checkpoint']; GD = f'{SP}/ch33b_gates2'
PROBES = re.findall(r'^  (\w+): (\d+/\d+)$', rd(f'{GD}/probes.out'), re.M); assert len(PROBES) == 12 and all(a == b for _, s_ in PROBES for a, b in [s_.split('/')]), PROBES
ic2 = rd(f'{GD}/probe_ink_cache.out'); IC2 = R(r'^(\d+/8 probes)$', ic2, 'ink cache second'); assert IC2 == '8/8 probes', IC2; ICLOAD2 = R(r'^\s*(the full load \d+ s, the warm load \(a harvest on a cold cache\) \d+ s, the cached load \d+ s)$', ic2, 'the cache loads 2'); C6OK = R(r'^\s*PASS C6 [^:\n]*: (\d+ shared groups)$', ic2, 'C6 groups kept')
_reg = rd(f'{GD}/register.out'); REG = (re.search(r'(DECLARED \d+[^\n]*)', _reg, re.M) or re.search(r'(THE REGISTER GATE: GREEN)', _reg)).group(1)
POS = R(r'THE FALLS: (\d+ checkpoints? over \d+ pauses in \d+ s \(\d+ workers\)[^\n]*)', rd(f'{GD}/positions.out'), 'the positions')
TAPE2 = R(r'^(\d+/10) checkpoints$', rd(f'{GD}/tape.out'), 'the chain tape'); assert TAPE2 == '10/10', TAPE2
ck2 = rd(f'{GD}/checkpoint.out'); CK2 = R(r'^(\d+/7 probes)$', ck2, 'the checkpoint probes second'); assert CK2 == '6/7 probes', CK2
K1D = R(r'^\s*(rows \d+; shape True; verdicts equal the pinned list False \(first difference \d+\))$', ck2, 'K1 detail'); K1I = R(r'first difference (\d+)\)', K1D, 'K1 index'); assert 'FAIL  K1 ' in ck2 and ck2.count('PASS  K') == 6, 'K1 alone red'
_vs = rd(SEQ); _vb = _vs[_vs.index('\nVERDICTS = ['):_vs.index('\nFORK_VERDICTS')]; _vl = [x for x in re.findall(r"'([A-Za-z0-9\-]+) (?:MATCH|DIVERGE)'", _vb)]; assert _vl[int(K1I)] == 'DO1', (_vl[int(K1I)], K1I)   # the pinned list's index at the first difference is DO1
diag = rd(f'{SP}/ch33b_k1_diag.out'); BEYOND1 = R(r'^beyond the tape: (Deut \d+:\d+)$', diag, 'beyond the tape'); assert BEYOND1 == 'Deut 33:1', BEYOND1
DIFFS = R(r'^rows \d+ \| equal False \| differences: (\[.*\])$', diag, 'the differences'); assert "'DO1 DIVERGE'" in DIFFS and "'DO2 DIVERGE'" in DIFFS and "'DO5 DIVERGE'" in DIFFS and 'DO3' not in DIFFS and 'DO4' not in DIFFS, DIFFS
DIFFS = ', '.join('%s computed %s against the pinned %s' % (a.split()[0], a.split()[1], b.split()[1]) for _, a, b in ast.literal_eval(DIFFS))
LOGN = R(r'^run_to done: log lines (\d+)', diag, 'the log lines'); assert R(r'^Deut 33 events in the log: (\d+)', diag, 'Deut 33 events') == '0'
pk = rd(f'{SP}/patch_k1_probe_ch33b.out'); _pk = re.search(r'the tape refs by the old form (\d+ \(last Deut \d+:\d+\)), by the new form (\d+ \(last Deut \d+:\d+\))', pk); assert _pk, 'the patch print'; PK = '%s by the single-quote form, %s by either quote' % (_pk.group(1), _pk.group(2))
_tape = _vs[_vs.find('# ==== TAPE BEGIN'):_vs.find('# ==== TAPE END ====')]; DQ = len(re.findall(r"'case_source': \"Deut 33:", _tape)); SQ33 = len(re.findall(r"'case_source': 'Deut 33:", _tape)); assert DQ == 11 and SQ33 == 0, (DQ, SQ33)
CHAIN_ROW = [int(r[2]) for r in TAILROWS if 'second pass, from the tape' in r[1]]; assert len(CHAIN_ROW) == 1, CHAIN_ROW; CHAIN_ROW = CHAIN_ROW[0]
D.update(CHAIN2=CHAIN2, POS_S=POS_S, TAPE2_S=TAPE2_S, PROBES_S=PROBES_S, CK2_S=CK2_S, PROBES=', '.join('%s %s' % q for q in PROBES), IC2=IC2, ICLOAD2=ICLOAD2, C6OK=C6OK, REG=REG, REG60=REG[:60], POS=POS, TAPE2=TAPE2, CK2=CK2, K1D=K1D, K1I=K1I, BEYOND1=BEYOND1, DIFFS=DIFFS, LOGN=LOGN, PK=PK, DQ=DQ, CHAIN_ROW=CHAIN_ROW)
# ---- THE TAIL's prints: the third pass --from checkpoint (after the second job's DONE) ----
if not PARTIAL:
    done2 = rd(f'{SP}/ch33b_tail_chain2.DONE'); assert R(r'^chain rc=(\d+)$', done2, 'chain rc 2') == '0', done2
    summ3 = rd(f'{SP}/ch33b_gates3_SUMMARY.txt'); assert 'FAILURES' not in summ3, summ3[-300:]
    STEPS3 = re.findall(r'^(PASS|FAIL|SKIP) (\w+)(?: rc=\d+)? \((\d+)s\)', summ3, re.M)
    assert [(v, n) for v, n, _ in STEPS3] == [('PASS', 'checkpoint'), ('PASS', 'stamp'), ('PASS', 'sweep'), ('PASS', 'unmoved')] and summ3.count('(before --from)') == 8, STEPS3
    CHAIN3 = sum(int(x) for _, _, x in STEPS3); STEP3_S = {n: int(x) for _, n, x in STEPS3}; SWEEP_S = STEP3_S['sweep']; CK3_S = STEP3_S['checkpoint']; GD3 = f'{SP}/ch33b_gates3'
    CK3 = R(r'^(\d+/7 probes)$', rd(f'{GD3}/checkpoint.out'), 'the checkpoint probes third'); assert CK3 == '7/7 probes', CK3
    sw = rd(f'{GD3}/sweep.out'); SWEEP = R(r'(\d+/\d+) runners green', sw, 'the sweep'); SWT = R(r'^PASS\s+cold_run_blessing_of_moses\.py rc=0\s+score=%s\s+([\d.]+)s$' % MATRIX, sw, 'the blessing runner in the sweep')
    SW_TOP = sorted(((float(x), n) for n, x in re.findall(r'^PASS\s+(cold_run_\w+)\.py rc=0\s+score=\d+/\d+\s+([\d.]+)s$', sw, re.M)), reverse=True)[:3]; SW_TOP = '; '.join('%s %.1f s' % (n[9:], x) for x, n in SW_TOP)
    CHAIN_S = CHAIN2 + CHAIN3; NCHAIN = len({n for v, n, _ in STEPS2 + STEPS3 if v == 'PASS'}); assert NCHAIN == 12, NCHAIN
    CHAIN_ROW3 = [int(r[2]) for r in TAILROWS if 'third pass, from the checkpoint probes' in r[1]]; assert len(CHAIN_ROW3) == 1, CHAIN_ROW3; CHAIN_ROW3 = CHAIN_ROW3[0]
    D.update(CHAIN3=CHAIN3, CK3=CK3, CK3_S=CK3_S, SWEEP=SWEEP, SWT=SWT, SW_TOP=SW_TOP, SWEEP_S=SWEEP_S, CHAIN_S=CHAIN_S, NCHAIN=NCHAIN, CHAIN_ROW3=CHAIN_ROW3)
rows_t = [l.split('\t') for l in tsv.strip().split('\n') if l.split('\t')[1:2] and l.split('\t')[1].startswith('21b')]; NSTEP = len(rows_t); TSEC = sum(int(r[2]) for r in rows_t)
TABLE = '\n'.join('| %s | %s | %s | %s |' % (r[0], r[1].replace('|', '/'), r[2], r[3]) for r in rows_t)
D.update(NSTEP=NSTEP, TSEC=TSEC, TABLE=TABLE)
if __name__ == '__main__':
    print('THE TAIL\'S FACTS (%s):' % ('PARTIAL — the second pass not yet read' if PARTIAL else 'WHOLE'), {k: (v if len(str(v)) < 100 else str(v)[:97] + '...') for k, v in D.items() if k != 'TABLE'})
