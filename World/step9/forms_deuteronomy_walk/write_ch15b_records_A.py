import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE DEUTERONOMY WALK 13b THE TAIL (2026-09-23): THE RECORDS FROM THE SHEET IN ONE CALL (World/step9/RECORD_FORMS.md) — the map's "Sitting 13b — AS BUILT" (with THE
# TIMING TABLE) and sitting 13's lesson 4 CORRECTED in place (a dated rider), the reading ledger's CORRECTION row, COMPILE_DEBT's sitting-13 box PAID and the 13b box,
# MIDDOT's compile entry, RESEARCH_LOG, THE_STEPS, THE_BRIEFING (the scoreboard's date, a bullet and an entry), THE_LOOP's step-6 row, RESUME, RECORD_FORMS, the state
# doc's #207 addendum 5 (the close — a clean point), the addenda's section, the recovery page rewritten under its cap, the memory (the walk note and the index).
# EVERY NUMBER PARSED FROM THE PRINTS (the runner's run, the tape's runs, the chain's folder and its first pass kept aside, the timing table, the NFKC re-measure, the
# records' own reads), never recited; every text built whole before its file is opened; the caps asserted; the gloss lint's count per file asserted UNMOVED by the
# write; --check runs the reads and the anchors alone. write_ch14b_records.py's form. WRITTEN AND RUN AT THE TAIL (the design's 'at RUN B' moved under the cap). RUN FROM THE REPO ROOT.
import os, re, sys, subprocess
ROOT = _ROOT   # the scratchpad original (the copier prepends the portable header in the forms folder)
SP = os.path.dirname(os.path.abspath(__file__)); G = f'{SP}/gates_ch15b'
MEM = os.path.expanduser('~/.claude/projects/-Users-Shared-TorahSim/memory')
CHECK = '--check' in sys.argv
def rd(name): return open(name if name.startswith('/') else f'{G}/{name}', encoding='utf-8', errors='ignore').read()
def read(p): return open(p if p.startswith('/') else f'{ROOT}/{p}', encoding='utf-8').read()
def W(p, s): open(p if p.startswith('/') else f'{ROOT}/{p}', 'w', encoding='utf-8').write(s)
def last_frac(name, den=None):
    fr = [(int(a), int(b)) for a, b in re.findall(r'(\d+)/(\d+)', rd(name)) if den is None or int(b) == den]
    assert fr, (name, den); return fr[-1]
def newest(pat): return sorted(f for f in os.listdir(SP) if re.match(pat, f))[-1]
# ---- THE PRINTS ----
RUN_FILE = newest(r'ch15_runner_run\d\.out$'); run = rd(f'{SP}/{RUN_FILE}'); MX = re.search(r'MATRIX: (\d+)/(\d+)', run); MX = tuple(int(x) for x in MX.groups()); assert MX[0] == MX[1], (RUN_FILE, MX)
SCANS = re.search(r"^THE SCANS on the one database: (.*)$", run, re.M).group(1)
cg = rd(f'{SP}/ch15_cases_gen.out'); CASES_N = int(re.search(r'CASES generated: (\d+)', cg).group(1)); PER_CELL = re.search(r'per cell (\{.*?\})', cg).group(1)
NARR = re.search(r'^THE NARRATIVE: (\(.*?\)) \(the fifteen on Israel', run, re.M).group(1); SCENE = re.search(r'^THE SCENE on the bench: .*?; entities (\d+); closes (\d+)$', run, re.M); SCENE = (int(SCENE.group(1)), int(SCENE.group(2))) if SCENE else None
TAPE_FILE = newest(r'ch15_tape_run\d\.out$'); tape = rd(f'{SP}/{TAPE_FILE}'); assert '10/10 checkpoints' in tape, TAPE_FILE
TAPE_RUNS = len([f for f in os.listdir(SP) if re.match(r'ch15_tape_run\d\.out$', f)])
DG = re.findall(r'CHECKPOINT (DG\d) .*? (MATCH|MISS|DIVERGE)$', tape, flags=re.M); assert len(DG) == 9 and all(v == 'MATCH' for _, v in DG), DG
RETYPED = re.findall(r'CHECKPOINT (CQ6|DC6|DD2|DF5|CU5) .*? (MATCH|MISS|DIVERGE)$', tape, flags=re.M); assert len(RETYPED) == 5 and all(v == 'MATCH' for _, v in RETYPED), RETYPED
cc = rd(f'{SP}/ch15_checkpoint_check.out'); CC = re.search(r'checkpoint_check: (\d+) rows, (\d+) miss, (\d+) raised', cc); CC = tuple(int(x) for x in CC.groups()); assert CC[1] == 18 and CC[2] == 0, CC
st = rd(f'{SP}/seq_stitch_ch15.out'); PLC = re.search(r'^PLACEMENT LITERAL: (.*)$', st, re.M).group(1); CEN = re.search(r'^  CENSUS tuple .*?: (\(.*\))$', st, re.M).group(1)
rec = rd(f'{SP}/seq_record_ch15.out'); NREC = int(re.search(r'recording: (\d+) records written', rec).group(1)); RF_REC = re.search(r'^  release_firstborn\s+worlds \d+\s+total\s+(\d+).*?statute\s+(\d+)', rec, re.M); RF_REC = (int(RF_REC.group(1)), int(RF_REC.group(2))) if RF_REC else None
pf = rd(f'{SP}/ch15b_probes_fail.out'); PF = tuple(int(x) for x in re.search(r'readback_probes: (\d+)/(\d+)', pf).groups()); assert PF == (35, 42), PF
ty = rd(f'{SP}/add_types_ch15.out'); TY = tuple(int(x) for x in re.search(r'THE TYPES DONE: kinds (\d+), effects (\d+), daemons (\d+), functions blocks (\d+), edges from release_firstborn (\d+), I5 75, parameters (\d+)', ty).groups())
pl = rd(f'{SP}/patch_seq_literals_ch15.out'); WN = int(re.search(r'the writes W read from the narrative: (\d+)', pl).group(1))
summ = rd('SUMMARY.txt'); ALL_GREEN = 'GATES CHAIN DONE — ALL GREEN' in summ
if not CHECK: assert ALL_GREEN, summ[-400:]
dg = rd('daemon.out'); DGN = int(re.search(r'(\d+) daemons', dg).group(1)); DGF = re.search(r'(\d+) functions', dg); DGF = int(DGF.group(1)) if DGF else None; assert DGN == 75, DGN
dp = rd('dependency.out'); LC = re.search(r'LINK CENSUS \(the link review law\): reference (\d+), transfer (\d+), hypothesis (\d+), none (\d+)', dp); LC = tuple(int(x) for x in LC.groups()) if LC else None
DPE = re.search(r'dispositions on file: (\d+) edges, (\d+) pointers', dp); DPE, DPP = (int(DPE.group(1)), int(DPE.group(2))) if DPE else (None, None)
rg = rd('register.out'); RG = tuple(int(x) for x in re.search(r'DECLARED (\d+); DEBT (\d+); FAILS (\d+)', rg).groups()); assert RG[1] == 0 and RG[2] == 0, RG
def have(n): return os.path.exists(f'{G}/{n}')
sw = rd('sweep.out') if have('sweep.out') else ''; SW_P = len(re.findall(r'^PASS +cold_run_\w+\.py', sw, flags=re.M)); SW_F = len(re.findall(r'^FAIL +cold_run_\w+\.py', sw, flags=re.M)); SW_CELLS = sum(int(a) for a, b in re.findall(r'score=(\d+)/(\d+)', sw))
if not CHECK: assert SW_F == 0 and SW_P >= 69, (SW_P, SW_F)
po = rd('positions.out') if have('positions.out') else ''; PO = re.search(r'(\d+) checkpoints', po); PO = int(PO.group(1)) if PO else None
jg = rd('journal.out'); JG = re.search(r'(\d+) kinds, (\d+) rows', jg); JG = tuple(int(x) for x in JG.groups()) if JG else None
PR = {'census': last_frac('probe_census.out'), 'installation': last_frac('probe_installation.out', 6), 'readback': last_frac('probe_readback.out', 42), 'large_letter': last_frac('probe_large_letter.out', 6), 'ink_cache': last_frac('probe_ink_cache.out', 8)}
PR['checkpoint'] = last_frac('checkpoint.out', 7) if have('checkpoint.out') else None
if not CHECK: assert PR['readback'] == (42, 42) and PR['installation'] == (6, 6) and PR['large_letter'] == (6, 6) and PR['ink_cache'] == (8, 8) and PR['census'][0] == PR['census'][1] and PR['checkpoint'] == (7, 7), PR
dep_first = rd(f'{SP}/ch15b_chain_dependency_first.out'); DEMANDS = [l.strip()[5:] for l in dep_first.splitlines() if l.startswith('  FAIL ')]; assert len(DEMANDS) == 5, DEMANDS
POINTER = 'DEMANDED (Deut 15:6 AS_WHEN — the design\'s H row; filed OWED under 10b\'s debt line, link hypothesis)' if any(d.startswith('POINTER Deut 15:6 AS_WHEN') for d in DEMANDS) else 'not demanded'
HOMOGRAPH = ('the registry\'s three (the servant Abraham\'s, the place Bethel, Jacob\'s flock) NOT matched; the census\'s two — 15:4\'s "for an inheritance" (the family runner) filed FALSE by the gift formula\'s seats computed, 15:21\'s "lame" read as the Passover (the pesach runner) named inside the VIA row'
             if any('-> family' in d for d in DEMANDS) and any('-> pesach' in d for d in DEMANDS) else 'as the first pass printed: %s' % DEMANDS)
rb_first = rd(f'{SP}/ch15b_chain_readback_first.out'); assert 'readback_probes: 41/42' in rb_first and 'FAIL Q17' in rb_first
CHAIN_STORY = read(f'{SP}/ch15b_chain_story.txt').strip() if os.path.exists(f'{SP}/ch15b_chain_story.txt') else 'THE GATES CHAIN (the story file not yet written)'
TAPE_STORY = read(f'{SP}/ch15b_tape_story.txt').strip()
TAPE_SHORT = 'the tape 10/10 on its THIRD run (CU5\'s stale count read from the first run\'s print; the retype\'s apostrophes; the scan\'s ground fixed to exclude the daemon\'s own writes)'
CHAIN_SHORT = 'the gates chain in three passes (Q17 and the dependency gate\'s five demands from the first pass, the positions table by four workers, then all green)'
dk = read('logic/oral_triage/deu_15_reeh_exam_2026-09-23.md'); NROWS = len([l for l in dk.split('\n') if l.startswith('- ') and (' — LAW.' in l or ' — DERIVATION.' in l or ' — DISPUTE.' in l or ' — CONTEXT.' in l or ' — OUTSIDE.' in l)]); assert NROWS == 974, NROWS
nf = read('World/step9/forms_deuteronomy_walk/ch14_aramaic_nfkc.out'); NF1 = re.search(r'(\d+) code points in (\d+) rows', nf).groups(); NF2 = re.search(r'MOVE under the fold: (\d+) of (\d+)', nf).groups(); NF3 = re.search(r'differs under the fold: \[\] \(of (\d+)\)', nf).group(1); NF4 = re.search(r'the whole book: (\d+) verses of (\d+) differ', nf).groups()
assert NF1[0] == '0' and NF2[0] == '0' and NF4[0] == '0', (NF1, NF2, NF4)
# ---- THE TIMING TABLE ----
tt = [l.split('\t') for l in read(f'{SP}/ch15b_timing.tsv').split('\n') if l.strip()]
T13B = [(r[0], r[1], int(r[2])) for r in tt if len(r) >= 3 and r[1].startswith('13b')]
TSUM = sum(s for _, _, s in T13B); TSLOW = sorted(T13B, key=lambda r: -r[2])[:8]
PH = {k: (len([1 for _, n, _ in T13B if n.startswith('13b ' + k)]), sum(s for _, n, s in T13B if n.startswith('13b ' + k))) for k in ('A', 'D', 'B', 'T')}
TIMING = ("THE TIMING TABLE (every step timed — the owner's ask at sitting 10; the machine's seconds per step, the model's reading and writing between them the rest): SITTING 13b %d timed steps, %d machine seconds — RUN A %d steps %ds, THE DOCKET %d steps %ds, RUN B %d steps %ds, THE TAIL %d steps %ds; the first row %s, the last %s; THE SLOWEST OF 13b: %s. The table itself: <scratch>/ch15b_timing.tsv, copied to the forms folder."
          % (len(T13B), TSUM, PH['A'][0], PH['A'][1], PH['D'][0], PH['D'][1], PH['B'][0], PH['B'][1], PH['T'][0], PH['T'][1], T13B[0][0] if T13B else '?', T13B[-1][0] if T13B else '?', '; '.join('%s %ds' % (n[4:] if n.startswith('13b ') else n, s) for _, n, s in TSLOW)))
NUM = dict(DG=len(DG), TAPE_RUNS=TAPE_RUNS, CC=CC, PLC=PLC, CEN=CEN, DGN=DGN, DGF=DGF, LC=LC, DPE=DPE, DPP=DPP, RG=RG, SW=(SW_P, SW_CELLS), PO=PO, JG=JG, PR=PR, POINTER=POINTER[:40], DEMANDS=len(DEMANDS), CASES=CASES_N, NREC=NREC, RF_REC=RF_REC, PF=PF, TY=TY, MX=MX, WN=WN, NARR=NARR, SCENE=SCENE, NROWS=NROWS, NFKC=(NF1, NF2, NF3, NF4), T13B=(len(T13B), TSUM), ALL_GREEN=ALL_GREEN)
print('THE NUMBERS:', NUM)
