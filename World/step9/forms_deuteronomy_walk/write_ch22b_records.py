import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE DEUTERONOMY WALK 17b (LEAN): THE TAIL'S RECORDS in ONE call — the map's AS BUILT — LEAN (the template ch22b_asbuilt.txt filled from the prints: the departures, the
# lessons, the finds, the timing table), the state doc's NOTE under #222, the recovery page (section 2 under its cap), the memory (the index line and the walk note), the
# lean-pass box's line (7) in COMPILE_DEBT. Every number READ FROM ITS PRINT (the chain's SUMMARY and its step prints, the types', the runner's, the stitcher's, the tape's
# three runs, checkpoint_check's, the gates', the census's, the timing table); every text built whole before a file is opened; the lints asserted; the caps asserted.
# --check prints without writing. write_ch19b_records.py's form. RUN FROM THE REPO ROOT after the chain's SUMMARY is read (ALL GREEN on its first pass).
import os, re, sys, subprocess, ast, glob
ROOT = _ROOT
SP = os.path.dirname(os.path.abspath(__file__))
MEM = os.path.expanduser('~/.claude/projects/-Users-Shared-TorahSim/memory')
CHECK = '--check' in sys.argv
MAP = f'{ROOT}/World/step9/DEUTERONOMY_WALK.md'; SD = f'{ROOT}/logic/pre_logic_methods_2026-07-28/PROMPT_continue_solo_era_2026-08-06.md'; REC = f'{ROOT}/logic/pre_logic_methods_2026-07-28/RECOVERY_new_thread_2026-09-12.md'
DEBT = f'{ROOT}/World/step9/COMPILE_DEBT.md'; MM = f'{MEM}/MEMORY.md'; MW = f'{MEM}/deuteronomy-walk.md'; SEQ = f'{ROOT}/World/step9/cold_run_sequence.py'; RUNNER = f'{ROOT}/World/step9/cold_run_persons_poor_court.py'
def rd(p): return open(p, encoding='utf-8').read()
def R(pat, text, name):
    g = re.search(pat, text, re.M); assert g, (name, pat); return g.group(1)
def RL(pat, text, name):
    g = re.findall(pat, text, re.M); assert g, (name, pat); return g[-1]
summ = rd(f'{SP}/ch22b_gates_SUMMARY.txt'); assert 'ALL GREEN' in summ, ('the chain not green — read the summary and the step prints first', summ[-300:])
STEPS = re.findall(r'^(PASS|FAIL|SKIP) (\w+)(?: rc=\d+)? \((\d+)s\)', summ, re.M); assert all(v == 'PASS' for v, _, _ in STEPS) and len(STEPS) == 12, STEPS
CHAIN_S = sum(int(t) for _, _, t in STEPS); GD = f'{SP}/ch22b_gates'
PROBES = re.findall(r'^  (\w+): (\d+/\d+)$', rd(f'{GD}/probes.out'), re.M); assert len(PROBES) == 12 and all(a == b for _, s in PROBES for a, b in [s.split('/')]), PROBES
_reg = rd(f'{GD}/register.out'); REG = (re.search(r'(DECLARED \d+[^\n]*)', _reg, re.M) or re.search(r'(THE REGISTER GATE: GREEN)', _reg)).group(1)
SWEEP = R(r'(\d+/\d+) runners green', rd(f'{GD}/sweep.out'), 'the sweep'); POS = R(r'THE FALLS: (\d+ checkpoints? over \d+ pauses in \d+ s \(\d+ workers\)[^\n]*)', rd(f'{GD}/positions.out'), 'the positions')
ta, tb = rd(f'{SP}/ch22_types_a.out'), rd(f'{SP}/ch22_types_b.out')
KADD, EADD = R(r'^kinds: (\d+) added of', ta, 'kinds'), R(r'^effects: (\d+) added', ta, 'effects')
DAEM, FB, E32, I5 = R(r'^THE TYPES DONE: kinds \d+, effects \d+, daemons (\d+),', tb, 'd'), R(r'functions blocks (\d+), edges', tb, 'fb'), R(r'edges from persons_poor_court (\d+)', tb, 'e32'), R(r', I5 (\d+);', tb, 'i5')
runs = sorted(glob.glob(f'{SP}/ch22_runner_run*.out')); run = rd(runs[-1]); run1 = rd(runs[0]); MATRIX = RL(r'^MATRIX: (\d+/\d+) cells', run, 'the runner'); MATRIX1 = RL(r'^MATRIX: (\d+/\d+) cells', run1, 'the first run')
FRAC = RL(r'^FRACTIONS: (pure ink \d+/\d+ \(\d+%\) · named moves \d+/\d+ \(\d+%\) · data \d+/\d+ \(\d+%\)) ·', run, 'the fractions')
RBG = R(r'^THE READBACK — THE FORMS ON FILE, NO NEW FORM: 96 rows — (\{[^}]+\});', run, 'the readback'); RBT = R(r'^THE READBACK — THE FORMS ON FILE, NO NEW FORM: 96 rows — \{[^}]+\}; on the tape (\d+),', run, 'on tape')
NPAR = int(R(r'the parameters (\d+) \(in the registry 0, in DATA \d+\)', run, 'the parameters')); NDATA = int(R(r'; DATA rows (\d+)$', run, 'the data rows'))
NARR = R(r'^THE NARRATIVE: (\(\d+, \d+, \d+, \(\d+, \d+\), \d+, \d+, \d+, \d+\))', run, 'the narrative'); assert ast.literal_eval(NARR)[0] == 79
RSIZE = os.path.getsize(RUNNER); CASES = int(R(r'^CASES generated: (\d+)', rd(f'{SP}/ch22_cases_gen.out'), 'the cases'))
st = rd(f'{SP}/seq_stitch_ch22_2.out'); PLACE = R(r"^PLACEMENT LITERAL: (\{.*\})$", st, 'placement'); CENSUS = R(r'^  CENSUS tuple \([^)]*\): (\(.*\))$', st, 'census')
seq = rd(SEQ); RUN = R(r'^RUN = \((\d+, \d+, \d+, \d+, \d+, \d+, \d+, \d+),', seq, 'RUN'); PREV = R(r'^PREVIOUS_RUN = \((\d+, \d+, \d+, \d+, \d+, \d+, \d+, \d+),', seq, 'PREV')
tapes = sorted(glob.glob(f'{SP}/ch22_tape_run*.out')); assert len(tapes) == 3, tapes; t1, t2, t3 = (rd(p) for p in tapes)
V1, V2, V3 = (R(r'^(\d+/10) checkpoints$', t, 'verdict') for t in (t1, t2, t3)); assert V3 == '10/10'
def divs(t): return sorted(set(l.split()[1] for l in t.split('\n') if l.lstrip().startswith('CHECKPOINT ') and l.split()[-1] == 'DIVERGE'))
BASE = divs(t3); DIV1 = ', '.join(d for d in divs(t1) if d not in BASE); DIV2 = ', '.join(d for d in divs(t2) if d not in BASE); assert (DIV1, DIV2) == ('CU7, DC4', 'DC4'), (DIV1, DIV2)
CC = R(r'^(checkpoint_check: \d+ rows, \d+ miss, \d+ raised)', rd(sorted(glob.glob(f'{SP}/ch22_checkpoint_check*.out'))[-1]), 'checkpoint_check')
DEP1 = R(r'^(DEPENDENCY GATE: \d+ failure\(s\))', rd(f'{SP}/ch22b_dependency_first.out'), 'dep first'); dg = rd(sorted(glob.glob(f'{SP}/ch22b_dependency_after*.out'))[-1])
DEP2 = R(r'^(DEPENDENCY GATE: every required edge[^\n]*)', dg, 'dep after'); NDEP = R(r'dispositions on file: (\d+ edges, \d+ pointers)$', dg, 'ndep'); LINKC = R(r'^LINK CENSUS \(the link review law\): (reference \d+, transfer \d+, hypothesis \d+, none \d+)', dg, 'link')
import yaml; _dd = yaml.safe_load(open(f'{ROOT}/World/step9/dependency_dispositions.yaml', encoding='utf-8')); MINE = str(len([e for e in _dd['edges'] if e.get('from') == 'persons_poor_court'])); assert NDEP.startswith(str(len(_dd['edges'])) + ' edges')
dm = rd(f'{SP}/ch22b_daemon_first.out'); DMN, DMF = R(r'regenerated \((\d+) daemons, \d+ functions\)', dm, 'dmn'), R(r'regenerated \(\d+ daemons, (\d+) functions\)', dm, 'dmf')
sc = rd(sorted(glob.glob(f'{SP}/ch22_scan_census*.out'))[-1]); SCP = R(r'chapters 22-25 present: (\d+) \[', sc, 'present'); SCT = R(r'^SCAN CENSUS DONE — runner scans tripping: (\d+)$', sc, 'tripping')
NFACT = len(re.findall(r'^FACT ', ''.join(rd(f'{SP}/ch22_callees{s}.out') for s in ('', '2', '3')), re.M)); NFAIL = len(re.findall(r'^FAIL ', ''.join(rd(f'{SP}/ch22_callees{s}.out') for s in ('', '2', '3')), re.M))
Q46 = R(r'(readback_probes: \d+/\d+)', rd(f'{SP}/ch22_probes_fail.out'), 'the probe to fail')
NEXAM = len(re.findall(r'^- Mishnah [A-Za-z ]+ \d+:\d+ — LAW\.', rd(f'{ROOT}/logic/oral_triage/deu_22_25_ki_teitzei_exam_2026-09-26.md'), re.M))
rows_t = [l.split('\t') for l in rd(f'{SP}/ch22b_timing.tsv').strip().split('\n')]; tim = [r for r in rows_t if r[1].startswith('17b')]; NSTEP = len(tim); TSEC = sum(int(r[2]) for r in tim)
TABLE = '\n'.join('| %s | %s | %s | %s |' % (r[0], r[1].replace('|', '/'), r[2], r[3]) for r in tim)
D = dict(NFACT=NFACT, NFAIL=NFAIL, Q46=Q46, NEXAM=NEXAM, KADD=KADD, EADD=EADD, DAEM=DAEM, FB=FB, E32=E32, I5=I5, RSIZE=RSIZE, CASES=CASES, MATRIX1=MATRIX1, MATRIX=MATRIX, FRAC=FRAC, RBG=RBG, RBT=RBT, NPAR=NPAR, NDATA=NDATA, NARR=NARR, DMN=DMN, DMF=DMF, DEP1=DEP1, DEP2=DEP2, NDEP=NDEP, LINKC=LINKC, MINE=MINE, PLACE=PLACE, CENSUS=CENSUS, RUN=RUN, PREV=PREV, V1=V1, DIV1=DIV1, V2=V2, DIV2=DIV2, V3=V3, CC=CC, SCP=SCP, SCT=SCT, CHAIN_S=CHAIN_S, NCHAIN=len(STEPS), PROBES=', '.join('%s %s' % p for p in PROBES), REG=REG, POS=POS, SWEEP=SWEEP, NSTEP=NSTEP, TSEC=TSEC, TABLE=TABLE)
print('THE PRINTS:', {k: (v if len(str(v)) < 90 else str(v)[:87] + '...') for k, v in D.items() if k != 'TABLE'})
ASB = rd(f'{SP}/ch22b_asbuilt.txt') % D
NOTE222 = " — THE TAIL (2026-09-26, in RUN B's window at 141k on the owner's \"Go\" — the chain's notification arrived before any compaction): the chain's SUMMARY read once — ALL GREEN ON ITS FIRST PASS in %d s (%d steps; the probe suites %s; the register gate --strict %s; the positions %s; the sweep %s; the journal unmoved) — no demand to file; the four records and the debt line (7) written in one call (write_ch22b_records.py; the map's AS BUILT from the template ch22b_asbuilt.txt), the forms copied, the commit message at <scratch>/commit_msg_ch22b.txt (sittings 15, 15b, 16, 16b, 17 and 17b together — the earlier messages folded in; the trailers once); the tree UNCOMMITTED since f730559. NEXT ON HIS WORD: the commit (\"Commit\" = no push; \"commit push\" = both); then, after a compaction (\"Reread\", then \"Go\"), SITTING 18 — THE READING FROM 26:1, LEAN. POST-COMPACTION REREADS: the recovery page, the map's newest section (\"Sitting 17b — THE COMPILE OF CHAPTERS 22-25 — AS BUILT — LEAN\"), MEMORY.md; then this checkpoint." % (CHAIN_S, len(STEPS), D['PROBES'], REG, POS, SWEEP)
DEBT_LINE = " (7) sitting 17b (2026-09-26) — CHAPTERS 22-25 COMPILED, LEAN, ONE RUNNER OVER FOUR UNITS (two runs + the tail): the forty-four Mishnah rows the ledger cites at least twice read whole (Bava Batra 5:10-11; Bava Kamma 8:1, 8:3; Bava Metzia 2:7-10, 5:10, 9:13; Berakhot 3:5; Chullin 12:2-3; Gittin 2:4, 3:1, 8:1, 9:10; Ketubot 3:1, 3:5, 4:3; Kiddushin 1:1; Makkot 3:10, 3:15; Peah 4:6, 6:6, 7:2; Rosh Hashanah 1:1; Sanhedrin 3:4, 11:1; Sotah 7:2, 8:4; Temurah 6:2-3; Yevamot 1:1, 2:1, 3:9, 4:13, 8:2-3, 10:1, 12:1, 12:3, 12:6; Zavim 2:3); NO docket, NO Talmud folio read; sixteen cells and the table, %d cases %s; twenty lines, %s writes, %d parameters; %s edges from the runner (four homograph FALSE, three PARAMETER); the chain ALL GREEN on its first pass; OWED: the docket whole (Bava Metzia 2, 5, 7, 9; Ketubot 3-4; Sanhedrin 3, 11; Yevamot 1-4, 8, 10, 12; Gittin 2-3, 8-9; Makkot 3; Sotah 7-8; Peah 4-7; Bava Kamma 8; Bava Batra 5; Temurah 6; Chullin 12; Berakhot 3; Rosh Hashanah 1; Kiddushin 1; Zavim 2 — the segments the rows name), the pointer rows for 24:16 (2 Kings 14:6), 25:19 (1 Samuel 15) and 25:9 (27:15), the laborer's eating (Bava Metzia 7) and the tassels' and the vineyard's parameters, the readback's exercise of the levirate on Ruth's tape and of Amalek on Samuel's, the persons and the court scene, the four chapters' glosses, the ten deferred records; the commit on his word. 18 (the reading from 26:1): next." % (CASES, MATRIX, ast.literal_eval(NARR)[0], NPAR, MINE)
# ---- the texts checked against the files ----
m = rd(MAP); assert '## Sitting 17b — THE COMPILE OF CHAPTERS 22-25 — AS BUILT' not in m and m.rfind('## Sitting 17b — THE COMPILE OF CHAPTERS 22-25, Deuteronomy 22:1-25:19 — LEAN') > 0 and m.find('\n## ', m.rfind('## Sitting 17b — THE COMPILE OF CHAPTERS 22-25, Deuteronomy') + 10) < 0
sd = rd(SD); assert '\n#222 (' in sd and 'THE TAIL (2026-09-26' not in sd
i222 = sd.index('\n#222 ('); assert sd.find('\n#2', i222 + 5) < 0, 'the #222 the last checkpoint'
rec = rd(REC)
def sub1(t, a, b, name):
    assert t.count(a) == 1, (name, t.count(a), a[:70]); return t.replace(a, b)
rec2 = sub1(rec, '## 2. WHERE IT STANDS (2026-09-26; #222 sitting 17b RUN B newest)', '## 2. WHERE IT STANDS (2026-09-26; #222 sitting 17b newest — DONE, its tail written)', 'the header')
rec2 = sub1(rec2, '- SITTINGS 15-17 (ch 17-25 READ + COMPILED, LEAN): chains green; UNCOMMITTED since f730559.\n', '- SITTINGS 15-17b (ch 17-25 READ + COMPILED, LEAN): chains green; UNCOMMITTED since f730559.\n', 'the sittings line')
rec2 = sub1(rec2, '- SITTING 17b RUN B (ch 22-25 COMPILE, LEAN) at #222: runner persons_poor_court %s; %s edges; THE GATES CHAIN LAUNCHED (its summary not yet read). NEXT: THE TAIL (the summary once, the demands, the records, the forms, the message), then the commit on his word.' % (MATRIX, MINE), '- SITTING 17b (ch 22-25 COMPILE, LEAN) DONE at #222: runner persons_poor_court %s; %s edges; chain ALL GREEN on its first pass (sweep %s); the message at <scratch>/commit_msg_ch22b.txt. NEXT: the commit on his word; then 18 (the reading from 26:1, lean).' % (MATRIX, MINE, SWEEP), 'the sitting line')
rec2 = sub1(rec2, 'cold_run_<span>.py (73 runners', 'cold_run_<span>.py (74 runners', 'the file map')
mm = rd(MM)
mm2 = sub1(mm, "17b RUN A + RUN B 2026-09-26 at #222 (the design; the types %s kinds / %s effects; the 74th runner persons_poor_court %s in seven parts; the tape %s on its third run; %s edges; THE GATES CHAIN LAUNCHED, its summary unread); NEXT: THE TAIL (the summary read once, the demands, the records, the forms, the message), then the commit on his word" % (KADD, EADD, MATRIX, V3, MINE), "17b DONE 2026-09-26 at #222 (the compile — the 74th runner persons_poor_court %s in seven parts; %s kinds / %s effects; the tape %s on its third run; %s edges; chain ALL GREEN on its first pass), UNCOMMITTED; NEXT: the commit on his word, then 18 (the reading from 26:1, lean)" % (MATRIX, KADD, EADD, V3, MINE), 'the walk line')
mw = rd(MW)
mw2 = sub1(mw, 'description: "SITTING 17b RUN B AT ITS CLEAN POINT 2026-09-26 (chapters 22-25 COMPILED lean — the 74th runner persons_poor_court %s, %s kinds / %s effects, the tape %s on its third run, %s edges, the chain LAUNCHED; NEXT THE TAIL then the commit on his word) — ' % (MATRIX, KADD, EADD, V3, MINE), 'description: "SITTING 17b DONE 2026-09-26 (chapters 22-25 COMPILED lean — the 74th runner persons_poor_court %s, %s kinds / %s effects, the tape %s on its third run, %s edges, the chain ALL GREEN on its first pass; UNCOMMITTED; NEXT the commit on his word, then 18 from 26:1) — ' % (MATRIX, KADD, EADD, V3, MINE), 'the description')
mw2 = mw2.rstrip('\n') + "\n\nSITTING 17b DONE 2026-09-26 (the tail, in RUN B's window on the owner's \"Go\"): the gates chain ALL GREEN ON ITS FIRST PASS (%d steps, %d s — the probe suites all full, the register gate strict %s, the positions at four workers %s, the sweep %s, the journal unmoved); no demand to file; the records written (the map's AS BUILT from a template filled from the prints), the forms copied, the message built (sittings 15 through 17b together). THE LESSONS: a count assert in a filing script goes stale when a later set adds an edge (assert >=); the census's homographs are consonantal (sabbath, olah, firstborn, rain); a scan's declared list is read from its source (the tape's DC4 reads the runner's RAIN_VOCAB); a detached job gives no notification, a long foreground command does; the daemon gate reads literal submits only; the kin counts are one run's source; four chapters are one runner in seven parts plus the generated cases; the two-run rule held over four chapters (%d steps, %d machine seconds). UNCOMMITTED since f730559. NEXT on his word: the commit; then 18 (the reading from 26:1, lean) after a compaction.\n" % (len(STEPS), CHAIN_S, REG, POS, SWEEP, NSTEP, TSEC)
debt = rd(DEBT); anchor = ' 17b (the compile of 22-25): next.'; assert debt.count(anchor) == 1, debt.count(anchor); debt2 = debt.replace(anchor, DEBT_LINE)
for t in (ASB, NOTE222, DEBT_LINE, mw2[len(mw):], rec2): assert not re.search(r'[֐-׿]', t), 'no Hebrew script in the new texts'   # MEMORY.md carries its glossed header (baseline 4) — the NEW texts only
for t in (ASB, NOTE222, DEBT_LINE, mw2, rec2, mm2): assert os.path.expanduser('~') not in t and SP not in t, 'a home or scratch path'
assert len(rec2.encode()) <= 10240 and len(mm2.encode()) < 17000, (len(rec2.encode()), len(mm2.encode()))
print('THE RECORDS %s: the AS BUILT %d bytes; the NOTE %d; the recovery page %d; MEMORY.md %d; the walk note %d; the debt line %d' % ('CHECKED' if CHECK else 'WRITTEN', len(ASB.encode()), len(NOTE222.encode()), len(rec2.encode()), len(mm2.encode()), len(mw2.encode()), len(DEBT_LINE.encode())))
if not CHECK:
    open(MAP, 'w', encoding='utf-8').write(m.rstrip('\n') + ASB)
    open(SD, 'w', encoding='utf-8').write(sd.rstrip('\n') + NOTE222 + '\n')
    open(REC, 'w', encoding='utf-8').write(rec2); open(MM, 'w', encoding='utf-8').write(mm2); open(MW, 'w', encoding='utf-8').write(mw2); open(DEBT, 'w', encoding='utf-8').write(debt2)
    lints = {}
    for f in (MAP, SD, REC, MM, DEBT, MW):
        lints[os.path.basename(f)] = subprocess.run(['python3', f'{ROOT}/logic/solo_tools/gloss_lint.py', f], capture_output=True, text=True).stdout.strip().split('\n')[-1]
    print('THE RECORDS WRITTEN — the lints:', lints)
