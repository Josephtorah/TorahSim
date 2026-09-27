import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE DEUTERONOMY WALK 16 (LEAN, 2026-09-24): THE CLEAN COMPACTION POINT at RUN 1's end — the state doc's #213, the recovery page (section 2 under its cap), the
# memory (the index line and the walk note) — written in ONE call after the rows of chapters 19-20 are checked; every number READ FROM ITS PRINT (the dumps',
# the split's, the measure's size, the ink runs', the check's, CORPUS_TRUTH's literals, the map's own section); every text built whole before a file is opened;
# the lints and the caps asserted. --check prints without writing. write_ch17b_point.py's form. RUN FROM THE REPO ROOT.
import os, re, sys, subprocess, glob
ROOT = _ROOT
SP = os.path.dirname(os.path.abspath(__file__))
MEM = os.path.expanduser('~/.claude/projects/-Users-Shared-TorahSim/memory')
CHECK = '--check' in sys.argv
SD = f'{ROOT}/logic/pre_logic_methods_2026-07-28/PROMPT_continue_solo_era_2026-08-06.md'; REC = f'{ROOT}/logic/pre_logic_methods_2026-07-28/RECOVERY_new_thread_2026-09-12.md'
MM = f'{MEM}/MEMORY.md'; MW = f'{MEM}/deuteronomy-walk.md'; MAP = f'{ROOT}/World/step9/DEUTERONOMY_WALK.md'
def rd(p): return open(p, encoding='utf-8').read()
def R(pat, text, name):
    g = re.search(pat, text, re.M); assert g, (name, pat); return g.group(1)
D = {c: rd(f'{SP}/ch{c}_dump0.out') for c in (19, 20, 21)}
NV = {c: int(R(r'^  DB verses (\d+) \|', D[c], 'verses')) for c in D}; TOK = {c: int(R(r'^  token count chapter \d+ : (\d+)', D[c], 'tokens')) for c in D}
MIS = {c: R(r"verses whose store token count differs from the DB: (\[.*?\])", D[c], 'mismatch') for c in D}
sp_ = rd(f'{SP}/ch19_split.out'); TOT = R(r'\| totals (\d+ \d+ \d+ \d+)$', sp_, 'the split'); NOUT = len(eval(R(r'^the outside rows (\[.*?\]) \|', sp_, 'outside')))
MSZ = os.path.getsize(f'{SP}/ch19_measure_lean.out')
F = [int(R(r'^(\d+) failing statements', rd(f'{SP}/ch19_ink_run{i}.out'), f'run{i}')) for i in (1, 2, 3)]; assert F[2] == 0, F
NA = len(re.findall(r'^assert ', rd(f'{SP}/ch19_ink.py'), re.M))
ck = rd(f'{SP}/ch19_rows_check_a2.out'); assert 'THE RUN-1 IMPORT CHECK GREEN' in ck
NS = int(R(r'^THE SIFREI ROWS TYPED \(chapters 19-20\): (\d+) \|', ck, 'sifrei')); NO = int(R(r'Onkelos typed: (\d+) ==', ck, 'onkelos')); NX = int(R(r'outside typed: (\d+) ==', ck, 'outside'))
VS = R(r"the verdicts: Counter\((\{[^}]*\})\) Counter", ck, 'verdicts S'); VX = R(r"Counter\(\{'MATERIAL': \d+\}\) Counter\((\{[^}]*\})\)$", ck, 'verdicts SO'); FAILS = R(r"the cuts' misses \(FAIL\): (\[.*?\])$", ck, 'fails'); assert FAILS == '[]', FAILS
ct = rd(f'{ROOT}/logic/corpus/CORPUS_TRUTH.py'); U0 = int(R(r'assert len\(W\["units"\]\) == (\d+)', ct, 'U0')); S0 = int(R(r'assert len\(W\["standing"\]\) == (\d+)', ct, 'S0'))
m = rd(MAP); i = m.index('## Sitting 16 — CHAPTERS 19-21'); DBYTES = len(m[i:].encode()); assert '## Sitting 16 — CHAPTERS 19-21 — AS BUILT' not in m
print('THE PRINTS: verses %s; tokens %s; mismatches %s; the split totals %s, outside %d; the measure %d bytes; the ink %d asserts (%d/%d/%d); the rows %d + %d + %d, verdicts %s / %s, FAIL %s; the fold %d/%d; the design %d bytes' % (NV, TOK, MIS, TOT, NOUT, MSZ, NA, F[0], F[1], F[2], NS, NO, NX, VS, VX, FAILS, U0, S0, DBYTES))
# ---- #213 ----
sd = rd(SD); assert '\n#213 ' not in sd
P213 = ('\n\n#213 (2026-09-24, THE DEUTERONOMY WALK sitting 16 — CHAPTERS 19-21\'s READING IN THE LEAN FORM, the lean pass\'s fifth sitting and the first on THREE chapters, RUN 1 of two; on the owner\'s "Reread go" after the compaction at #212 — no commit word said, the tree UNCOMMITTED since f730559 with sittings 15 and 15b riding, 16 opened on it; A CLEAN COMPACTION POINT AT RUN 1\'s END: THE MEASUREMENTS (three dumps derived from the forms\' chapter-17 dump by one derive; the split over three chapters — the spine 179-221, %s rows, with the two HEADLESS piskaot 183 and 187 inside chapter 19 joined WHOLE from the export, 190:16-21 running past into 20:1, 192 a variant piska heading on 20:8 out of verse order, 222 chapter 22\'s; %d outside rows; the verses %d / %d / %d, the tokens %d / %d / %d, the store the DB at every verse but 21:7 — %s), THE LEAN MEASURE (%d bytes, printed compact from the start and read in three slices), THE INK\'s %d asserts (%d fell on the first pass — the English\'s "Pisqa" prefix before a merged number, TWO HAND-SUMMED TOTALS dropped as recitals, a slice off by one; %d on the second — the prefix cut a character short; %d on the third), THE DESIGN in the map (%d bytes — the form, the measurements, thirteen finds, 13 claims over three units, the rows\' plan, the window\'s plan, the compile\'s shape; NO HEBREW SCRIPT, lint 0), and THE ROWS OF CHAPTERS 19 AND 20 TYPED AND CHECKED — %d Sifrei rows in five files (%s), %d Onkelos rows in two, the %d outside rows over the three chapters (%s) — ZERO CUT MISSES ON THE FIRST PASS (FAIL %s; sitting 15 had four), one REREAD mark corrected on the second check (198:1 marked fresh — 199:5 the prior read at chapters 1-3). NOTHING FROZEN; the ledger NOT YET WRITTEN; the repo\'s files touched by this run: the map (the design) only; the fold predicted %d -> %d units, %d -> %d standing, the hash unmoved. NEXT: RUN 2 after the compaction — chapter 21\'s rows (120 spine rows in four files 205-210, 211-215, 216-218, 219-221 from the split\'s ch19_spine_p*.txt; 23 Onkelos rows from ch21_onkelos.txt), the import check B over all ten row files, the ledger deu_19_21_shoftim_ki_teitzei (coverage computed; write_ch17_ledger.py the form), the manifests (13 claims), the seats (derive from the forms\' seat_ch17.py), the chain (three units; the fold; build_world; the journal gate; the register gate --strict; large_letter; the home gate), the display patch probed first, the records from the sheet (the map\'s AS BUILT with the timing table, this doc, the recovery page, the memory, COMPILE_DEBT\'s lean box line), the forms, the message; then the commit on his word ("Commit" = no push; "commit push" = both). POST-COMPACTION REREADS: the recovery page, the map\'s newest section ("Sitting 16 — CHAPTERS 19-21, Deuteronomy 19:1-21:23 — LEAN" — the design), MEMORY.md; then this checkpoint. THE SCRATCHPAD (this run\'s forms): derive_ch19_dump0.py, ch19_dump0.py / ch20_dump0.py / ch21_dump0.py (+ .out), split_ch19_spine.py (+ ch19_split.out), derive_ch19_ink.py, ch19_ink_head.py, ch19_ink_body.py, ch19_ink.py, ch19_measure_lean.py (+ .out), ch19_ink_run1-3.out, write_ch19_design.py, ch19_rows_sifrei_179_183.py, _184_188, _189_190, _191_197, _198_204, ch19_rows_onkelos_19.py, _20, ch19_rows_outside.py, ch19_rows_check_a.py (+ .out, 2.out), write_ch19_point.py, ch19_timing.tsv.' % (TOT.split()[-1], NOUT, NV[19], NV[20], NV[21], TOK[19], TOK[20], TOK[21], MIS[21], MSZ, NA, F[0], F[1], F[2], DBYTES, NS, VS, NO, NX, VX, FAILS, U0, U0 + 3, S0, S0 + 13))
# ---- the recovery page ----
rec = rd(REC)
def sub1(t, a, b, name):
    assert t.count(a) == 1, (name, t.count(a), a[:70]); return t.replace(a, b)
rec2 = sub1(rec, '## 2. WHERE IT STANDS (2026-09-24; #212 sitting 15b newest)', '## 2. WHERE IT STANDS (2026-09-24; #213 sitting 16 RUN 1 newest)', 'the header')
rec2 = sub1(rec2, "- THE TAPE at RUN (1349, 96, 88, 0, 12, 1709, 48, 319, pairs, 127), markers 172, closes 127; 10/10 (DI1-DI5); 15b's chain ALL GREEN once (sweep 71/71).\n", "- THE TAPE at RUN (1349, 96, 88, 0, 12, 1709, 48, 319, pairs, 127); 10/10 (DI1-DI5); 15b's chain green (sweep 71/71).\n", 'the RUN line')
rec2 = sub1(rec2, '- SITTING 14/14b (ch 16, LEAN): PUSHED f730559.\n', '', 'the 14b line')
rec2 = sub1(rec2, '- SITTING 15/15b (ch 17-18 READ + COMPILED, LEAN; one runner) at #212: 234 sources; runner 66/66; 8 lines, 37 writes; the tape 10/10; chain green; UNCOMMITTED. NEXT: the commit; then 16 (ch 19-21 read, lean).\n', '- SITTING 15/15b (ch 17-18, LEAN; one runner) at #212: 66/66; tape 10/10; chain green; UNCOMMITTED.\n- SITTING 16 (ch 19-21 READ, LEAN) RUN 1 at #213: ink %d/0; design; rows of 19-20 (%d + %d + %d) checked, 0 misses; NOT frozen. NEXT: RUN 2 — ch 21\'s rows, the ledger, the freeze, the records; the commit.\n' % (NA, NS, NO, NX), 'the sitting line')
# ---- the memory ----
mm = rd(MM)
OLDL = '15/15b (ch 17-18 READ + COMPILED, lean — one runner) 2026-09-24 (234 sources; 66/66; the tape 10/10; the chain launched), chain green; UNCOMMITTED; NEXT: the commit, then 16 (ch 19-21 read, lean)'
NEWL = '15/15b (ch 17-18 READ + COMPILED, lean — one runner) 2026-09-24 (66/66; tape 10/10; chain green), UNCOMMITTED; 16 (ch 19-21 READ, lean, three units) RUN 1 at #213 2026-09-24 (the ink %d/0, the design, the rows of 19-20 checked — 0 cut misses); NEXT: RUN 2 (ch 21\'s rows, the ledger, the freeze, the records), then the commit' % NA
mm2 = sub1(mm, OLDL, NEWL, 'the walk line')
mw = rd(MW)
DESC_OLD = 'description: "SITTING 15b AT ITS CLEAN POINT 2026-09-24'
assert mw.count(DESC_OLD) == 1
mw2 = mw.replace(DESC_OLD, 'description: "SITTING 16 RUN 1 AT ITS CLEAN POINT 2026-09-24 (chapters 19-21 READ lean — the ink %d/0, the design, the rows of 19-20 typed and checked with 0 cut misses; NOT frozen; NEXT RUN 2: chapter 21\'s rows, the ledger, the freeze, the records; then the commit) — SITTING 15b AT ITS CLEAN POINT 2026-09-24' % NA, 1)
NOTE = ('\n\nSITTING 16 RUN 1 AT ITS CLEAN POINT 2026-09-24 — CHAPTERS 19-21\'s READING IN THE LEAN FORM (the fifth sitting of [[lean-pass-ruling]], the first on THREE chapters; the tree UNCOMMITTED since f730559, 15/15b riding): one derive and three dumps, the split over three chapters (%s rows in piskaot 179-221 — the two HEADLESS piskaot 183 and 187 inside chapter 19 read WHOLE from the export; 192 heads on 20:8 out of verse order; 190:16-21 run past into 20:1; %d outside rows), the lean measure (%d bytes, compact), the ink\'s %d asserts (%d/%d/%d — two hand-summed totals fell as recitals), the design (%d bytes — 13 claims over deu_19_miklat_witness, deu_20_war_rules, deu_21_eglah_family; the window\'s plan two runs), the rows of chapters 19 and 20 typed and checked (%d Sifrei in five files, %d Onkelos, %d outside; ZERO cut misses on the first pass). THE LESSONS SO FAR: a headless piska inside the run is the spine\'s and the instrument lists only its citing rows as outside — the split reads it whole; the heads can come out of verse order (a variant piska); a hand-summed total is a recital — the dict from the print, no sum typed; a three-chapter reading is TWO RUNS under the cap. NEXT: RUN 2 after the compaction — chapter 21\'s rows, the check B, the ledger deu_19_21_shoftim_ki_teitzei, the manifests, the seats, the chain (the fold %d -> %d / %d -> %d), the display patch, the records, the forms, the message; then the commit on his word.' % (TOT.split()[-1], NOUT, MSZ, NA, F[0], F[1], F[2], DBYTES, NS, NO, NX, U0, U0 + 3, S0, S0 + 13))
mw2 = mw2.rstrip('\n') + NOTE + '\n'
rec_bytes = len(rec2.encode()); mm_bytes = len(mm2.encode())
assert rec_bytes <= 10240, ('the recovery page over its cap', rec_bytes)
assert mm_bytes < 17000, ('MEMORY.md over its cap', mm_bytes)
assert not re.search(r'[֐-׿]', P213 + NOTE + NEWL), 'no Hebrew script in the new texts'
print('THE POINT CHECKED: #213 %d bytes; the recovery page %d; MEMORY.md %d; the walk note %d' % (len(P213.encode()), rec_bytes, mm_bytes, len(mw2.encode())))
if not CHECK:
    open(SD, 'w', encoding='utf-8').write(sd.rstrip('\n') + P213 + '\n')
    open(REC, 'w', encoding='utf-8').write(rec2); open(MM, 'w', encoding='utf-8').write(mm2); open(MW, 'w', encoding='utf-8').write(mw2)
    for f in (SD, REC, MM, MW):
        out = subprocess.run(['python3', f'{ROOT}/logic/solo_tools/gloss_lint.py', f], capture_output=True, text=True).stdout.strip().split('\n')[-1]
        print('  lint', os.path.basename(f), out)
    print('THE POINT WRITTEN: #213, the recovery page (%d bytes), MEMORY.md (%d bytes), the walk note' % (rec_bytes, mm_bytes))
