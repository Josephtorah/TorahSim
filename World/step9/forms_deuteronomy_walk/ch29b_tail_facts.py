import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE DEUTERONOMY WALK 19b (2026-09-27; LEAN) — THE TAIL'S FACTS: every number the records and the message use, READ FROM ITS PRINT in one module both writers import
# (write_ch29b_records.py and write_ch29b_commit_msg.py): the types' prints, the runner's graded runs, the stitcher's census, the tape's runs and its RUN literal, checkpoint_check,
# the daemon and dependency gates' prints, the scan census, the probe retypes' prints, the chain's two SUMMARIES and the second pass's step prints (the probe suites, the register
# gate --strict, the positions, the sweep), the exam file's rows, the timing table. write_ch29b_point2.py's readers extended. IMPORTED FROM THE REPO ROOT with PYTHONPATH the
# scratchpad; run alone it prints the dict. Nothing here is typed — a miss is an AssertionError naming the print.
import os, re, sys, subprocess, glob, ast
ROOT = _ROOT
SP = os.path.dirname(os.path.abspath(__file__))
MEM = os.path.expanduser('~/.claude/projects/-Users-Shared-TorahSim/memory')
SEQ = f'{ROOT}/World/step9/cold_run_sequence.py'; RUNNER = f'{ROOT}/World/step9/cold_run_covenant_return_charge.py'
def rd(p): return open(p, encoding='utf-8').read()
def R(pat, text, name, g=1):
    m = re.search(pat, text, re.M); assert m, (name, pat); return m.group(g)
def RL(pat, text, name):
    g = re.findall(pat, text, re.M); assert g, (name, pat); return g[-1]
def newest(pat): return max(glob.glob(pat), key=os.path.getmtime)
# ---- RUN B's prints (write_ch29b_point2.py's readers) ----
ta, tb = rd(f'{SP}/ch29b_types_a.out'), rd(f'{SP}/ch29b_types_b.out')
RUNS = sorted(glob.glob(f'{SP}/ch29_runner_run*.out')); rr = rd(RUNS[-1]); r1 = rd(RUNS[0]); st = rd(f'{SP}/seq_stitch_ch29.out'); seq = rd(SEQ)
TAPES = sorted(glob.glob(f'{SP}/ch29_tape_run*.out')); CCS = sorted(glob.glob(f'{SP}/ch29_checkpoint_check*.out')); cc = rd(CCS[-1])
DGS = sorted(glob.glob(f'{SP}/ch29b_dependency_*.out'), key=os.path.getmtime); dg = rd(DGS[-1]); dm = rd(f'{SP}/ch29b_daemon_first.out'); sc = rd(f'{SP}/ch29_scan_census.out'); tsv = rd(f'{SP}/ch29b_timing.tsv')
KADD, KREG = R(r'^kinds: (\d+) added of \d+ \(13 statute / 4 act / 3 speech\), registry (\d+);', ta, 'kinds'), R(r'^kinds: \d+ added of \d+ \(13 statute / 4 act / 3 speech\), registry (\d+);', ta, 'kinds reg')
EADD, EREG, SEATS = R(r'^effects: (\d+) added \(registry (\d+)\)', ta, 'effects'), R(r'^effects: \d+ added \(registry (\d+)\)', ta, 'effects reg'), R(r'the reused rows amended with (\d+) seats', ta, 'seats')
DAEM, FB = R(r'^daemons: (\d+) \(law_covenant_return_charge True\); functions blocks: (\d+);', tb, 'daemons'), R(r'functions blocks: (\d+);', tb, 'fb')
E33, PTRS0 = R(r'^dependency: the span \(three ranges\) \+ (\d+) edges', tb, 'e33'), R(r'; edges \d+, pointers (\d+)$', tb, 'pointers0')
I5, CAL = R(r'^installation_probes I5: (\d+)', tb, 'i5'), R(r'^calendar: (\d+) parameters', tb, 'cal')
assert (KADD, KREG, EADD, EREG, SEATS, DAEM, FB, E33, I5, CAL) == ('20', '1253', '59', '1399', '9', '81', '75', '33', '81', '75'), (KADD, KREG, EADD, EREG, SEATS, DAEM, FB, E33, I5, CAL)
MATRIX = re.findall(r'^MATRIX: (\d+/\d+) cells match the answer sheet$', rr, re.M)[-1]; MATRIX1 = re.findall(r'^MATRIX: (\d+/\d+) cells', r1, re.M)[-1]; assert MATRIX.split('/')[0] == MATRIX.split('/')[1], (MATRIX, MATRIX1)
NRUNS = len(RUNS)
FRAC = re.findall(r'^FRACTIONS: (pure ink \d+/\d+ \(\d+%\) · named moves \d+/\d+ \(\d+%\) · data \d+/\d+ \(\d+%\)) ·', rr, re.M)[-1]
RB = R(r'^THE READBACK — THE FORMS ON FILE, NO NEW FORM: (\d+) rows — ', rr, 'readback'); RBG = R(r'^THE READBACK — THE FORMS ON FILE, NO NEW FORM: \d+ rows — (\{[^}]+\});', rr, 'grades'); RBT = R(r'^THE READBACK — THE FORMS ON FILE, NO NEW FORM: \d+ rows — \{[^}]+\}; on the tape (\d+),', rr, 'on tape')
PAR, NDATA = R(r'the parameters (\d+) \(in the registry (\d+), in DATA \d+\); DATA rows (\d+)$', rr, 'parameters'), R(r'; DATA rows (\d+)$', rr, 'data'); INREG = R(r'the parameters \d+ \(in the registry (\d+),', rr, 'in registry')
NARR = R(r'^THE NARRATIVE: (\(\d+, \d+, \d+, \(\d+, \d+\), \d+, \d+, \d+, \d+, \[[^\]]*\]\))', rr, 'narrative'); NWRITES = ast.literal_eval(NARR)[0]
LINT_R = re.search(r'(\d+) flag', subprocess.run(['python3', f'{ROOT}/logic/solo_tools/gloss_lint.py', RUNNER], capture_output=True, text=True).stdout).group(1); assert LINT_R == '0', LINT_R
CASES = int(R(r'^CASES generated: (\d+)', rd(f'{SP}/ch29_cases_gen.out'), 'the cases'))
PLACE = R(r"^PLACEMENT LITERAL: (\{.*\})$", st, 'placement'); CENSUS = R(r'^  CENSUS tuple \([^)]*\): (\(.*\))$', st, 'census')
RUN = R(r'^RUN = \((\d+, \d+, \d+, \d+, \d+, \d+, \d+, \d+),', seq, 'RUN'); PREV = R(r'^PREVIOUS_RUN = \((\d+, \d+, \d+, \d+, \d+, \d+, \d+, \d+),', seq, 'PREV'); assert PREV == '1403, 96, 88, 0, 12, 1929, 51, 319' and RUN == '1423, 102, 94, 0, 12, 2003, 52, 319', (RUN, PREV)
VS = [(re.search(r'^(\d+/10) checkpoints$', rd(t), re.M).group(1) if re.search(r'^(\d+/10) checkpoints$', rd(t), re.M) else 'TRIPPED') for t in TAPES]; assert VS[-1] == '10/10', VS
def divs(t): return sorted(set(l.split()[1] for l in t.split('\n') if l.lstrip().startswith('CHECKPOINT ') and l.split()[-1] == 'DIVERGE'))
BASE = divs(rd(TAPES[-1])); DIVS = [[d for d in divs(rd(t)) if d not in BASE] for t in TAPES[:-1]]
DM = [l.split()[1] for l in rd(TAPES[-1]).split('\n') if re.match(r'\s*CHECKPOINT DM\d', l) and l.split()[-1] == 'MATCH']; assert len(set(DM)) == 5, DM
MK = R(r'^  CENSUS tuple \([^)]*\): \((?:\d+, ){9}(\d+),', st, 'markers in the census'); assert MK == '173', MK
CC = R(r'^(checkpoint_check: \d+ rows, \d+ miss, \d+ raised)', cc, 'checkpoint_check'); assert CC.endswith('0 raised'), CC
DEP1 = R(r'^(DEPENDENCY GATE: \d+ failure\(s\))', rd(f'{SP}/ch29b_dependency_first.out'), 'dep first')
DGL = R(r'^DEPENDENCY GATE coverage: (\d+) runners declared', dg, 'runners'); DGE = R(r'dispositions on file: (\d+ edges, \d+ pointers)$', dg, 'edges'); assert 'gate satisfied' in dg, 'the dependency gate not green in its last print'
LINKC = R(r'^LINK CENSUS \(the link review law\): (reference \d+, transfer \d+, hypothesis \d+, none \d+)', dg, 'link census')
import yaml as _y; _dd = _y.safe_load(open(f'{ROOT}/World/step9/dependency_dispositions.yaml', encoding='utf-8')); MINE = len([e for e in _dd['edges'] if e.get('from') == 'covenant_return_charge']); ONFILE = len(_dd['edges']); NPTR = len(_dd['pointers']); OWED = len([p for p in _dd['pointers'] if p.get('disposition') == 'OWED'])
assert DGE.startswith('%d edges, %d pointers' % (ONFILE, NPTR)), (DGE, ONFILE, NPTR)
DMN, DMF = R(r'regenerated \((\d+) daemons, (\d+) functions\)', dm, 'daemons'), R(r'regenerated \(\d+ daemons, (\d+) functions\)', dm, 'functions'); assert 'gate satisfied' in dm and DMN == DAEM
SCP, SCT = R(r'chapters 29-31 present: (\d+) \[', sc, 'present'), R(r'^SCAN CENSUS DONE — runner scans tripping: (\d+)$', sc, 'tripping'); assert SCP == '53', SCP
RSIZE = os.path.getsize(RUNNER)
Q48 = R(r'(readback_probes: \d+/\d+)', rd(f'{SP}/ch29b_probes_fail.out'), 'Q48 to FAIL')
EXAM = re.findall(r'^- ((?:Mishnah|Tosefta) [A-Za-z ]+ \d+:\d+(?:-\d+)?) — LAW\.', rd(f'{ROOT}/logic/oral_triage/deu_29_31_nitzavim_vayelech_exam_2026-09-27.md'), re.M); NEXAM = len(EXAM); assert NEXAM == 7, EXAM; EXAMROWS = '; '.join(EXAM)
# ---- THE TAIL's prints ----
summ1 = rd(f'{SP}/ch29b_gates_SUMMARY.txt'); assert 'FAIL probes' in summ1, 'the first pass: the readback probes'
CHAIN1 = sum(int(t) for _, _, t in re.findall(r'^(PASS|FAIL|SKIP) (\w+)(?: rc=\d+)? \((\d+)s\)', summ1, re.M))
RB1 = R(r'(readback_probes: \d+/\d+)', rd(f'{SP}/ch29b_gates/probe_readback.out'), 'the first pass readback')
ret = rd(f'{SP}/ch29b_probes_retypes.out'); NRET, NRETP = R(r'^edits (\d+) over \d+ probes; comment lines \d+ \| WRITTEN$', ret, 'retypes'), R(r'^edits \d+ over (\d+) probes; comment lines \d+ \| WRITTEN$', ret, 'retyped probes')
RETQ = R(r"^failing probes read from the print: (\[.*\])$", ret, 'the failing probes'); HW = R(r"\| \[:10\] = ('Deut [^']+')$", ret, 'q20 head')
RBK = R(r'(readback_probes: \d+/\d+)', rd(f'{SP}/ch29b_gates2_killed_probe_readback.out'), 'the killed pass readback')
Q47FIX = R(r"^the ninety-one writes whose count is not one, from the print: (\[.*\])$", rd(f'{SP}/ch29b_probe_q47.out'), 'q47')
summA = rd(f'{SP}/ch29b_gates2_part1_SUMMARY.txt')   # the third launch's rows to the register gate — killed by the session's memory watchdog at the positions step (four workers)
A = re.findall(r'^(PASS|FAIL|SKIP) (\w+)(?: rc=\d+)? \((\d+)s\)', summA, re.M); assert [n for _, n, _ in A] == ['tape', 'probes', 'daemon', 'dependency', 'build', 'journal', 'register'] and all(v == 'PASS' for v, _, _ in A), A
posout = rd(f'{SP}/ch29b_gates3_positions.out'); POS = R(r'THE FALLS: (\d+ checkpoints? over \d+ pauses in \d+ s \(\d+ workers\)[^\n]*)', posout, 'the positions')
done3 = rd(f'{SP}/ch29b_gates3.DONE'); assert R(r'^positions rc=(\d+)$', done3, 'positions rc') == '0' and R(r'^chain rc=(\d+)$', done3, 'chain rc') == '0', done3
POSS = [r for r in [l.split('\t') for l in tsv.strip().split('\n')] if r[1:2] and r[1].startswith('19b TAIL the positions table')]; assert len(POSS) == 1, POSS; POSSEC = int(POSS[0][2])
summ = rd(f'{SP}/ch29b_gates3_SUMMARY.txt'); assert 'FAILURES' not in summ, summ[-300:]
B = re.findall(r'^(PASS|FAIL|SKIP) (\w+)(?: rc=\d+)? \((\d+)s\)', summ, re.M); assert [n for _, n, _ in B] == ['checkpoint', 'stamp', 'sweep', 'unmoved'] and all(v == 'PASS' for v, _, _ in B), B
STEPS = A + [('PASS', 'positions', str(POSSEC))] + B; assert len(STEPS) == 12, STEPS
CHAIN_S = sum(int(t) for _, _, t in STEPS); GD = f'{SP}/ch29b_gates2'; GD3 = f'{SP}/ch29b_gates3'
PROBES = re.findall(r'^  (\w+): (\d+/\d+)$', rd(f'{GD}/probes.out'), re.M); assert len(PROBES) == 12 and all(a == b for _, s_ in PROBES for a, b in [s_.split('/')]), PROBES
_reg = rd(f'{GD}/register.out'); REG = (re.search(r'(DECLARED \d+[^\n]*)', _reg, re.M) or re.search(r'(THE REGISTER GATE: GREEN)', _reg)).group(1)
SWEEP = R(r'(\d+/\d+) runners green', rd(f'{GD3}/sweep.out'), 'the sweep')
rows_t = [l.split('\t') for l in tsv.strip().split('\n') if l.split('\t')[1:2] and l.split('\t')[1].startswith('19b')]; NSTEP = len(rows_t); TSEC = sum(int(r[2]) for r in rows_t)
TABLE = '\n'.join('| %s | %s | %s | %s |' % (r[0], r[1].replace('|', '/'), r[2], r[3]) for r in rows_t)
D = dict(EXAMROWS=EXAMROWS, NEXAM=NEXAM, Q48=Q48, KADD=KADD, KREG=KREG, EADD=EADD, EREG=EREG, SEATS=SEATS, DAEM=DAEM, FB=FB, E33=E33, I5=I5, CAL=CAL, RSIZE=RSIZE, LINT_R=LINT_R, NDATA=NDATA, PAR=PAR, INREG=INREG, CASES=CASES, MATRIX1=MATRIX1, MATRIX=MATRIX, NRUNS=NRUNS, FRAC=FRAC, RB=RB, RBG=RBG, RBT=RBT, NARR=NARR, NWRITES=NWRITES, DMN=DMN, DMF=DMF, DEP1=DEP1, DGL=DGL, DGE=DGE, LINKC=LINKC, MINE=MINE, ONFILE=ONFILE, NPTR=NPTR, OWED=OWED, PLACE=PLACE, CENSUS=CENSUS, RUN=RUN, PREV=PREV, VS=VS, NTAPES=len(TAPES), DIVS=DIVS, NDIVS1=len(DIVS[0]) if DIVS else 0, CC=CC, SCP=SCP, SCT=SCT, CHAIN1=CHAIN1, RB1=RB1, NRET=NRET, NRETP=NRETP, RETQ=RETQ, HW=HW, RBK=RBK, Q47FIX=Q47FIX, CHAIN_S=CHAIN_S, NCHAIN=len(STEPS), PROBES=', '.join('%s %s' % p for p in PROBES), REG=REG, POS=POS, SWEEP=SWEEP, NSTEP=NSTEP, TSEC=TSEC, TABLE=TABLE)
if __name__ == '__main__':
    print('THE TAIL\'S FACTS:', {k: (v if len(str(v)) < 100 else str(v)[:97] + '...') for k, v in D.items() if k != 'TABLE'})
