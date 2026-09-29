import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE DEUTERONOMY WALK 20b (2026-09-28; LEAN) — THE TAIL'S FACTS: every number the records and the message use, READ FROM ITS PRINT in one module both writers import
# (write_ch32b_records.py and write_ch32b_commit_msg.py): the types' prints, the runner's graded runs, the stitcher's census, the tape's runs and its RUN literal, checkpoint_check,
# the daemon and dependency gates' prints, the scan census, the chain's first SUMMARY and its probe prints (the readback 45/49, the cache probe's C6), the retypes' print, the tail
# job's prints (the readback suite alone, the cache cleared, the chain's second SUMMARY and its step prints — the probe suites, the register gate --strict, the positions, the
# sweep), the exam file's rows, the timing table. write_ch32b_point2.py's readers extended; ch29b_tail_facts.py's form. IMPORTED FROM THE REPO ROOT with PYTHONPATH the
# scratchpad; run alone it prints the dict. Nothing here is typed — a miss is an AssertionError naming the print.
import os, re, sys, subprocess, glob, ast
ROOT = _ROOT
SP = os.path.dirname(os.path.abspath(__file__))
MEM = os.path.expanduser('~/.claude/projects/-Users-Shared-TorahSim/memory')
SEQ = f'{ROOT}/World/step9/cold_run_sequence.py'; RUNNER = f'{ROOT}/World/step9/cold_run_song_charge_nebo.py'
def rd(p): return open(p, encoding='utf-8').read()
def R(pat, text, name, g=1):
    m = re.search(pat, text, re.M); assert m, (name, pat); return m.group(g)
# ---- RUN B's prints (write_ch32b_point2.py's readers) ----
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
NRUNS = len(RUNS)
FRAC = re.findall(r'^FRACTIONS: (pure ink \d+/\d+ \(\d+%\) · named moves \d+/\d+ \(\d+%\) · data \d+/\d+ \(\d+%\)) ·', rr, re.M)[-1]
RB = R(r'^THE READBACK — THE FORMS ON FILE, NO NEW FORM: (\d+) rows — ', rr, 'readback'); RBG = R(r'^THE READBACK — THE FORMS ON FILE, NO NEW FORM: \d+ rows — (\{[^}]+\});', rr, 'grades'); RBT = R(r'^THE READBACK — THE FORMS ON FILE, NO NEW FORM: \d+ rows — \{[^}]+\}; on the tape (\d+),', rr, 'on tape')
PAR, NDATA = R(r'the parameters (\d+) \(in the registry (\d+), in DATA \d+\); DATA rows (\d+)$', rr, 'parameters'), R(r'; DATA rows (\d+)$', rr, 'data'); INREG = R(r'the parameters \d+ \(in the registry (\d+),', rr, 'in registry')
NARR = R(r'^THE NARRATIVE: (\(\d+, \d+, \d+, \(\d+, \d+\), \d+, \d+, \d+, \d+, \[[^\]]*\]\))', rr, 'narrative'); NWRITES = ast.literal_eval(NARR)[0]
NFACTS = R(r'^THE CALLEES \(the facts printed and asserted from the print\): (\d+) facts', rr, 'facts')
LINT_R = re.search(r'(\d+) flag', subprocess.run(['python3', f'{ROOT}/logic/solo_tools/gloss_lint.py', RUNNER], capture_output=True, text=True).stdout).group(1); assert LINT_R == '0', LINT_R
CASES = int(R(r'^CASES generated: (\d+)', rd(f'{SP}/ch32_cases_gen.out'), 'the cases')); PERCELL = R(r'^CASES generated: \d+ \(per cell (\{[^}]+\})\)', rd(f'{SP}/ch32_cases_gen.out'), 'per cell')
PLACE = R(r"^PLACEMENT LITERAL: (\{.*\})$", st, 'placement'); CENSUS = R(r'^  CENSUS tuple \([^)]*\): (\(.*\))$', st, 'census')
RUN = R(r'^RUN = \((\d+, \d+, \d+, \d+, \d+, \d+, \d+, \d+),', seq, 'RUN'); PREV = R(r'^PREVIOUS_RUN = \((\d+, \d+, \d+, \d+, \d+, \d+, \d+, \d+),', seq, 'PREV'); assert PREV == '1423, 102, 94, 0, 12, 2003, 52, 319', (RUN, PREV)
VS = [(re.search(r'^(\d+/10) checkpoints$', rd(t), re.M).group(1) if re.search(r'^(\d+/10) checkpoints$', rd(t), re.M) else 'TRIPPED') for t in TAPES]; assert VS[-1] == '10/10', VS
def divs(t): return sorted(set(l.split()[1] for l in t.split('\n') if l.lstrip().startswith('CHECKPOINT ') and l.split()[-1] == 'DIVERGE'))
BASE = divs(rd(TAPES[-1])); DIVS = [[d for d in divs(rd(t)) if d not in BASE] for t in TAPES[:-1]]
DN = [l.split()[1] for l in rd(TAPES[-1]).split('\n') if re.match(r'\s*CHECKPOINT DN\d', l) and l.split()[-1] == 'MATCH']; assert len(set(DN)) == 5, DN
MK = R(r'^  CENSUS tuple \([^)]*\): \((?:\d+, ){9}(\d+),', st, 'markers in the census'); assert MK == '173', MK
CC = R(r'^(checkpoint_check: \d+ rows, \d+ miss, \d+ raised)', cc, 'checkpoint_check'); assert CC.endswith('0 raised'), CC
CC1 = R(r'^(checkpoint_check: \d+ rows, \d+ miss, \d+ raised)', rd(CCS[0]), 'checkpoint_check first')
# the gate's RED first print (15:50) was overwritten by its green run at 16:37 under the same output name — the filing's own print is the record (patch_deps_ch32.out)
_pd = rd(f'{SP}/patch_deps_ch32.out'); _pb = re.search(r'^before: edges (\d+) pointers (\d+)$', _pd, re.M); _pa = re.search(r'^after: edges (\d+) pointers (\d+)$', _pd, re.M); assert _pb and _pa, 'the filing print'
assert 'the twenty-four CALL edges without a live call fixed in the runner' in _pd and 'two token edges FALSE by homograph' in _pd and 'the pointer 32:50 RUN_CITATION as predicted' in _pd, 'the filing departures'
DEP1 = '%s -> %s, pointers %s -> %s' % (_pb.group(1), _pa.group(1), _pb.group(2), _pa.group(2))
DEPR = R(r'^WRITTEN: the registration edge sequence -> song_charge_nebo; edges (\d+)$', rd(f'{SP}/patch_deps_ch32_reg.out'), 'the registration edge'); DEPG1 = R(r'dispositions on file: (\d+) edges', rd(f'{SP}/ch32b_dependency_first.out'), 'the gate green at 16:37'); assert DEPG1 == _pa.group(1) and 'gate satisfied' in rd(f'{SP}/ch32b_dependency_first.out'), (DEPG1, _pa.group(1))
DGL = R(r'^DEPENDENCY GATE coverage: (\d+) runners declared', dg, 'runners'); DGE = R(r'dispositions on file: (\d+ edges, \d+ pointers)$', dg, 'edges'); assert 'gate satisfied' in dg, 'the dependency gate not green in its last print'
LINKC = R(r'^LINK CENSUS \(the link review law\): (reference \d+, transfer \d+, hypothesis \d+, none \d+)', dg, 'link census')
import yaml as _y; _dd = _y.safe_load(open(f'{ROOT}/World/step9/dependency_dispositions.yaml', encoding='utf-8')); MINE = len([e for e in _dd['edges'] if e.get('from') == 'song_charge_nebo']); ONFILE = len(_dd['edges']); NPTR = len(_dd['pointers']); OWED = len([p for p in _dd['pointers'] if p.get('disposition') == 'OWED'])
MFALSE = len([e for e in _dd['edges'] if e.get('from') == 'song_charge_nebo' and e.get('disposition') == 'FALSE']); MCALL = len([e for e in _dd['edges'] if e.get('from') == 'song_charge_nebo' and e.get('disposition') == 'CALL'])
assert DGE.startswith('%d edges, %d pointers' % (ONFILE, NPTR)), (DGE, ONFILE, NPTR)
DMN, DMF = R(r'regenerated \((\d+) daemons, (\d+) functions\)', dm, 'daemons'), R(r'regenerated \(\d+ daemons, (\d+) functions\)', dm, 'functions'); assert 'gate satisfied' in dm and DMN == DAEM
SCP, SCT = R(r'chapter 32 present: (\d+) \[', sc, 'present'), R(r'^SCAN CENSUS DONE — runner scans tripping: (\d+)$', sc, 'tripping')
RSIZE = os.path.getsize(RUNNER)
FC = sorted(glob.glob(f'{SP}/ch32_fastcheck_run*.out')); FCL = rd(FC[-1]).strip().split('\n')[-1]; AK = sorted(glob.glob(f'{SP}/ch32_askcheck_run*.out')); AKL = rd(AK[-1]).strip().split('\n')[-1]
Q49 = R(r'(readback_probes: \d+/\d+)', rd(f'{SP}/ch32b_probes_fail.out'), 'Q49 to FAIL')
EXAM = re.findall(r'^- ((?:Mishnah|Tosefta) [A-Za-z ]+ \d+:\d+)(?: \([^)]*\))? — LAW\.', rd(f'{ROOT}/logic/oral_triage/deu_32_haazinu_exam_2026-09-28.md'), re.M); NEXAM = len(EXAM); assert NEXAM == 26, (NEXAM, EXAM)
NMISH, NTOS = len([e for e in EXAM if e.startswith('Mishnah')]), len([e for e in EXAM if e.startswith('Tosefta')]); EXAMROWS = '; '.join(EXAM)
RETY = rd(f'{SP}/patch_tape_retypes_ch32.out'); NTAPE_RET = R(r'^edits (\d+) checkpoints (\d+) \| WRITTEN$', RETY, 'tape retypes'); NTAPE_RETC = R(r'^edits \d+ checkpoints (\d+) \| WRITTEN$', RETY, 'tape retyped checkpoints')
# ---- THE TAIL's prints ----
summ1 = rd(f'{SP}/ch32b_gates_SUMMARY.txt'); assert 'FAIL probes' in summ1, 'the first pass: the probes'
CHAIN1 = sum(int(t) for _, _, t in re.findall(r'^(PASS|FAIL|SKIP) (\w+)(?: rc=\d+)? \((\d+)s\)', summ1, re.M))
A1 = re.findall(r'^(PASS|FAIL|SKIP) (\w+)(?: rc=\d+)? \((\d+)s\)', summ1, re.M); assert [(v, n) for v, n, _ in A1] == [('PASS', 'tape'), ('FAIL', 'probes'), ('PASS', 'daemon'), ('PASS', 'dependency'), ('PASS', 'build'), ('PASS', 'journal'), ('PASS', 'register')], A1
RB1 = R(r'(readback_probes: \d+/\d+)', rd(f'{SP}/ch32b_gates/probe_readback.out'), 'the first pass readback')
RB1Q = sorted(re.findall(r'^\s*FAIL (Q\d+) ', rd(f'{SP}/ch32b_gates/probe_readback.out'), re.M), key=lambda q: int(q[1:]))
ic = rd(f'{SP}/ch32b_gates/probe_ink_cache.out'); IC1 = R(r'^(\d+/8 probes)$', ic, 'ink cache first'); C6 = R(r'^\s*FAIL (C6 [^\n]*?): added:', ic, 'C6'); C6G = R(r'^\s*FAIL C6 [^\n]*?: (added: \[.*\]; lost: \[.*\])$', ic, 'C6 groups')
ICLOAD = R(r'^\s*(the full load \d+ s, the warm load \(a harvest on a cold cache\) \d+ s, the cached load \d+ s)$', ic, 'the cache loads')
PROBES1 = re.findall(r'^  (\w+): (\d+/\d+)$', rd(f'{SP}/ch32b_gates/probes.out'), re.M); assert len(PROBES1) == 12
ret = rd(f'{SP}/ch32b_probes_retypes.out'); NRET = R(r'^edits (\d+) \(the walker \d+ \+ RE \d+ \+ the generator 1\) over \d+ probes; comment lines \d+ \| WRITTEN$', ret, 'retypes'); NRETW = R(r'^edits \d+ \(the walker (\d+) \+', ret, 'the walker'); NRETP = R(r'over (\d+) probes; comment lines \d+ \| WRITTEN$', ret, 'retyped probes')
RETQ = R(r"^failing probes read from the print: (\[.*\])$", ret, 'the failing probes'); TWO = R(r"^\s*q48 w59 seats at 2 \(from the print\): (\[.*\])$", ret, 'the two seats')
Q20V = R(r"\(\(10,\), 'Deut 31:28', \"('Deut [^']+')\"\)", ret, 'q20 tenth')
RBA = R(r'(readback_probes: \d+/\d+)', rd(f'{SP}/ch32b_probes_after_retypes.out'), 'the readback suite alone'); assert RBA.split(': ')[1].split('/')[0] == RBA.split('/')[1], RBA
CLEAR = R(r'^(INK CACHE cleared)', rd(f'{SP}/ch32b_cache_clear.out'), 'the cache cleared')
done = rd(f'{SP}/ch32b_tail_chain.DONE'); assert R(r'^probes rc=(\d+)$', done, 'probes rc') == '0' and R(r'^chain rc=(\d+)$', done, 'chain rc') == '1', done   # the first job: the chain's second pass RED on the cache probe
summ2 = rd(f'{SP}/ch32b_gates2_SUMMARY.txt'); A2 = re.findall(r'^(PASS|FAIL|SKIP) (\w+)(?: rc=\d+)? \((\d+)s\)', summ2, re.M); assert [(v, n) for v, n, _ in A2] == [('PASS', 'tape'), ('FAIL', 'probes'), ('PASS', 'daemon'), ('PASS', 'dependency'), ('PASS', 'build'), ('PASS', 'journal'), ('PASS', 'register')], A2
CHAIN2 = sum(int(t) for _, _, t in A2)
ic2 = rd(f'{SP}/ch32b_gates2/probe_ink_cache.out'); IC2 = R(r'^(\d+/8 probes)$', ic2, 'ink cache second'); C6G2 = R(r'^\s*FAIL C6 [^\n]*?: (added: \[.*\]; lost: \[.*\])$', ic2, 'C6 groups second')
RB2 = R(r'(readback_probes: \d+/\d+)', rd(f'{SP}/ch32b_gates2/probe_readback.out'), 'the second pass readback'); assert RB2.split(': ')[1].split('/')[0] == RB2.split('/')[1], RB2
PROBES2 = re.findall(r'^  (\w+): (\d+/\d+)$', rd(f'{SP}/ch32b_gates2/probes.out'), re.M); assert len(PROBES2) == 12 and [n for n, s_ in PROBES2 for a, b in [s_.split('/')] if a != b] == ['ink_cache'], PROBES2
fb = rd(f'{SP}/ch32b_runner_fbind.out'); NFB, FBL1, FBL2 = re.search(r"^edits (\d+) over lines (\d+)-(\d+); F's globals write removed \| WRITTEN$", fb, re.M).groups(); FCALLS = R(r'^F calls in the file: (\d+); module-level F statements: \d+', fb, 'F calls'); assert FCALLS == NFB, (FCALLS, NFB)
LINT2 = R(r'^gloss_lint: (\d+) flag\(s\)$', rd(f'{SP}/ch32b_runner_lint2.out'), 'the runner lint after'); assert LINT2 == '0', LINT2
MATRIX5 = R(r'^MATRIX: (\d+/\d+) cells match the answer sheet$', rd(f'{SP}/ch32_runner_run5.out'), 'the fifth graded run'); assert MATRIX5 == '72/72', MATRIX5
CLEAR2 = R(r'^(INK CACHE cleared)', rd(f'{SP}/ch32b_cache_clear2.out'), 'the cache cleared again')
done2 = rd(f'{SP}/ch32b_tail_chain2.DONE'); assert R(r'^runner rc=(\d+)$', done2, 'runner rc') == '0' and R(r'^chain rc=(\d+)$', done2, 'chain rc 2') == '1', done2   # the second job: the chain's third pass RED at the sweep's limit
summ3 = rd(f'{SP}/ch32b_gates3_SUMMARY.txt'); STEPS3 = re.findall(r'^(PASS|FAIL|SKIP) (\w+)(?: rc=\d+)? \((\d+)s\)', summ3, re.M)
assert [(v, n) for v, n, _ in STEPS3] == [('PASS', 'tape'), ('PASS', 'probes'), ('PASS', 'daemon'), ('PASS', 'dependency'), ('PASS', 'build'), ('PASS', 'journal'), ('PASS', 'register'), ('PASS', 'positions'), ('PASS', 'checkpoint'), ('PASS', 'stamp'), ('FAIL', 'sweep')] and 'SKIP unmoved (an earlier step failed)' in summ3, STEPS3
CHAIN3 = sum(int(t) for _, _, t in STEPS3); POS_S = int([t for _, n, t in STEPS3 if n == 'positions'][0]); GD = f'{SP}/ch32b_gates3'
sw3 = rd(f'{GD}/sweep.out'); SWEEP3 = R(r'(\d+/\d+) runners green', sw3, 'the third pass sweep'); SWT = R(r'^FAIL\s+cold_run_song_charge_nebo\.py rc=124\s+score=rc-only \(no score line printed\)\s+([\d.]+)s$', sw3, 'the song runner timed out')
SW_TOP = sorted(((float(t), n) for n, t in re.findall(r'^PASS\s+(cold_run_\w+)\.py rc=0\s+score=\d+/\d+\s+([\d.]+)s$', sw3, re.M)), reverse=True)[:3]; SW_TOP = '; '.join('%s %.1f s' % (n[9:], t) for t, n in SW_TOP)
SWTO = R(r'^the sweep limit (900 -> 2400) \(--timeout N\); three edits \| WRITTEN$', rd(f'{SP}/ch32b_sweep_timeout.out'), 'the sweep limit')
done3 = rd(f'{SP}/ch32b_tail_chain3.DONE'); assert R(r'^chain rc=(\d+)$', done3, 'chain rc 3') == '0', done3
summ = rd(f'{SP}/ch32b_gates4_SUMMARY.txt'); assert 'FAILURES' not in summ, summ[-300:]
STEPS = re.findall(r'^(PASS|FAIL|SKIP) (\w+)(?: rc=\d+)? \((\d+)s\)', summ, re.M); assert [(v, n) for v, n, _ in STEPS] == [('PASS', 'stamp'), ('PASS', 'sweep'), ('PASS', 'unmoved')] and summ.count('(before --from)') == 9, STEPS
CHAIN4 = sum(int(t) for _, _, t in STEPS); CHAIN_S = CHAIN3 + CHAIN4; NCHAIN = len({n for v, n, _ in STEPS3 + STEPS if v == 'PASS'}); assert NCHAIN == 12, NCHAIN; GD4 = f'{SP}/ch32b_gates4'
PROBES = re.findall(r'^  (\w+): (\d+/\d+)$', rd(f'{GD}/probes.out'), re.M); assert len(PROBES) == 12 and all(a == b for _, s_ in PROBES for a, b in [s_.split('/')]), PROBES
_reg = rd(f'{GD}/register.out'); REG = (re.search(r'(DECLARED \d+[^\n]*)', _reg, re.M) or re.search(r'(THE REGISTER GATE: GREEN)', _reg)).group(1)
POS = R(r'THE FALLS: (\d+ checkpoints? over \d+ pauses in \d+ s \(\d+ workers\)[^\n]*)', rd(f'{GD}/positions.out'), 'the positions')
SWEEP = R(r'(\d+/\d+) runners green', rd(f'{GD4}/sweep.out'), 'the sweep'); SWT4 = R(r'^PASS\s+cold_run_song_charge_nebo\.py rc=0\s+score=72/72\s+([\d.]+)s$', rd(f'{GD4}/sweep.out'), 'the song runner in the fourth pass')
TAPE2 = R(r'^(\d+/10) checkpoints$', rd(f'{GD}/tape.out'), 'the chain tape'); assert TAPE2 == '10/10', TAPE2
TAILROWS = [l.split('\t') for l in tsv.strip().split('\n') if l.split('\t')[1:2] and l.split('\t')[1].startswith('20b TAIL')]
RBA_S = [int(r[2]) for r in TAILROWS if 'the readback suite alone' in r[1]]; assert len(RBA_S) == 1, RBA_S; RBA_S = RBA_S[0]
RUN5_S = [int(r[2]) for r in TAILROWS if 'fifth graded run' in r[1]]; assert len(RUN5_S) == 1, RUN5_S; RUN5_S = RUN5_S[0]
rows_t = [l.split('\t') for l in tsv.strip().split('\n') if l.split('\t')[1:2] and l.split('\t')[1].startswith('20b')]; NSTEP = len(rows_t); TSEC = sum(int(r[2]) for r in rows_t)
TABLE = '\n'.join('| %s | %s | %s | %s |' % (r[0], r[1].replace('|', '/'), r[2], r[3]) for r in rows_t)
D = dict(CHAIN3=CHAIN3, POS_S=POS_S, SWEEP3=SWEEP3, SWT=SWT, SW_TOP=SW_TOP, SWTO=SWTO, CHAIN4=CHAIN4, SWT4=SWT4, CHAIN2=CHAIN2, IC2=IC2, C6G2=C6G2, RB2=RB2, NFB=NFB, FBL1=FBL1, FBL2=FBL2, LINT2=LINT2, MATRIX5=MATRIX5, CLEAR2=CLEAR2, RUN5_S=RUN5_S, EXAMROWS=EXAMROWS, NEXAM=NEXAM, NMISH=NMISH, NTOS=NTOS, Q49=Q49, KADD=KADD, KREG=KREG, EADD=EADD, EREG=EREG, SEATS=SEATS, DAEM=DAEM, FB=FB, E42=E42, I5=I5, CAL=CAL, RSIZE=RSIZE, LINT_R=LINT_R, NDATA=NDATA, PAR=PAR, INREG=INREG, CASES=CASES, PERCELL=PERCELL, MATRIX1=MATRIX1, MATRIX=MATRIX, NRUNS=NRUNS, FRAC=FRAC, RB=RB, RBG=RBG, RBT=RBT, NARR=NARR, NWRITES=NWRITES, NFACTS=NFACTS, DMN=DMN, DMF=DMF, DEP1=DEP1, DGL=DGL, DGE=DGE, LINKC=LINKC, MINE=MINE, MFALSE=MFALSE, MCALL=MCALL, ONFILE=ONFILE, NPTR=NPTR, OWED=OWED, PLACE=PLACE, CENSUS=CENSUS, RUN=RUN, PREV=PREV, VS=VS, NTAPES=len(TAPES), DIVS=DIVS, NDIVS1=len(DIVS[0]) if DIVS else 0, CC=CC, CC1=CC1, SCP=SCP, SCT=SCT, FCL=FCL, AKL=AKL, NTAPE_RET=NTAPE_RET, NTAPE_RETC=NTAPE_RETC, CHAIN1=CHAIN1, RB1=RB1, RB1Q=', '.join(RB1Q), IC1=IC1, C6=C6, C6G=C6G, ICLOAD=ICLOAD, PROBES1=', '.join('%s %s' % p for p in PROBES1), NRET=NRET, NRETW=NRETW, NRETP=NRETP, RETQ=RETQ, TWO=TWO, Q20V=Q20V, RBA=RBA, RBA_S=RBA_S, CLEAR=CLEAR, CHAIN_S=CHAIN_S, NCHAIN=NCHAIN, PROBES=', '.join('%s %s' % p for p in PROBES), REG=REG, POS=POS, SWEEP=SWEEP, TAPE2=TAPE2, NSTEP=NSTEP, TSEC=TSEC, TABLE=TABLE)
if __name__ == '__main__':
    print('THE TAIL\'S FACTS:', {k: (v if len(str(v)) < 100 else str(v)[:97] + '...') for k, v in D.items() if k != 'TABLE'})
