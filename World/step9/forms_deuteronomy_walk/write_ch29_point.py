import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE DEUTERONOMY WALK 19 (LEAN, 2026-09-27): THE CLEAN COMPACTION POINT at RUN 1's end — the state doc's #227, the recovery page (section 2 rewritten under its cap),
# the memory (the index line and the walk note) — written in ONE call after the design; every number READ FROM ITS PRINT (the three dumps', the split's, the measure's
# size and its F section, the ink runs', CORPUS_TRUTH's literals, the map's own section); every text built whole before a file is opened; the lints and the caps asserted.
# --check prints without writing. write_ch26_point.py's form without the rows (RUN 1 of sitting 19 typed none — the window opened at 387k). RUN FROM THE REPO ROOT.
import os, re, sys, subprocess, ast
ROOT = _ROOT
SP = os.path.dirname(os.path.abspath(__file__))
MEM = os.path.expanduser('~/.claude/projects/-Users-Shared-TorahSim/memory')
CHECK = '--check' in sys.argv
SD = f'{ROOT}/logic/pre_logic_methods_2026-07-28/PROMPT_continue_solo_era_2026-08-06.md'; REC = f'{ROOT}/logic/pre_logic_methods_2026-07-28/RECOVERY_new_thread_2026-09-12.md'
MM = f'{MEM}/MEMORY.md'; MW = f'{MEM}/deuteronomy-walk.md'; MAP = f'{ROOT}/World/step9/DEUTERONOMY_WALK.md'
def rd(p): return open(p, encoding='utf-8').read()
def R(pat, text, name):
    g = re.search(pat, text, re.M); assert g, (name, pat); return g.group(1)
D = {c: rd(f'{SP}/ch{c}_dump0.out') for c in (29, 30, 31)}
NV = {c: int(R(r'^  DB verses (\d+) \|', D[c], 'verses')) for c in D}; TOK = {c: int(R(r'^  token count chapter \d+ : (\d+)', D[c], 'tokens')) for c in D}
MIS = {c: len(ast.literal_eval(R(r"verses whose store token count differs from the DB: (\[.*?\])$", D[c], 'mismatch'))) for c in D}
HEADS = {c: len(ast.literal_eval(R(r'^  heads whose chapter is \d+ : (\[.*?\]) \|', D[c], 'heads'))) for c in D}
sp_ = rd(f'{SP}/ch29_split.out'); TOT = R(r'\| totals (\{[^}]*\}) \d+$', sp_, 'the split'); TOTN = int(R(r'\| totals \{[^}]*\} (\d+)$', sp_, 'the split total')); NOUT = int(R(r'^the outside rows \[.*?\] (\d+) \|', sp_, 'outside'))
ms = rd(f'{SP}/ch29_measure_lean.out'); MSZ = len(ms.encode()); PRIOR = len(ast.literal_eval(R(r'outside rows read before: (\{.*\}) \| fresh:', ms, 'prior'))); FRESH = len(ast.literal_eval(R(r'\| fresh: (\[.*\])$', ms, 'fresh')))
F = [int(R(r'^(\d+) failing statements', rd(f'{SP}/ch29_ink_run{i}.out'), f'run{i}')) for i in (1, 2, 3)]; assert F[1:] == [0, 0], F
NA = sum(len(re.findall(r'^assert ', rd(f'{SP}/{f}'), re.M)) for f in ('ch29_ink_body.py', 'ch29_ink_body_b.py'))
ct = rd(f'{ROOT}/logic/corpus/CORPUS_TRUTH.py'); U0 = int(R(r'assert len\(W\["units"\]\) == (\d+)', ct, 'U0')); S0 = int(R(r'assert len\(W\["standing"\]\) == (\d+)', ct, 'S0'))
m = rd(MAP); i = m.index('## Sitting 19 — CHAPTERS 29-31'); DBYTES = len(m[i:].encode()); assert '## Sitting 19 — CHAPTERS 29-31 — AS BUILT' not in m and m.find('\n## ', i + 10) < 0
NT = len([l for l in rd(f'{SP}/ch29_timing.tsv').split('\n') if l.startswith(('0', '1', '2'))])
assert (NV, TOTN, NOUT, PRIOR, FRESH, NA) == ({29: 28, 30: 20, 31: 30}, 8, 19, 14, 5, 41), (NV, TOTN, NOUT, PRIOR, FRESH, NA)
print('THE PRINTS: verses %s; tokens %s; mismatches %s; heads %s; the split totals %s = %d, outside %d (read before %d, fresh %d); the measure %d bytes; the ink %d asserts (%d/%d/%d); the fold %d/%d; the design %d bytes; %d timed steps' % (NV, TOK, MIS, HEADS, TOT, TOTN, NOUT, PRIOR, FRESH, MSZ, NA, F[0], F[1], F[2], U0, S0, DBYTES, NT))
sd = rd(SD); assert '\n#227 ' not in sd and '\n#226 (' in sd
P227 = ('\n\n#227 (2026-09-27, THE DEUTERONOMY WALK sitting 19 — CHAPTERS 29-31\'s READING IN THE LEAN FORM, the lean pass\'s eleventh sitting, its sixth reading and the second on chapters WITHOUT A SPINE PISKA, RUN 1 of two; on the owner\'s "Continue" after sitting 18b\'s tail with NO compaction between (/context 387k at the open) — no commit word said, the tree UNCOMMITTED since 68191ea with 18b riding, 19 opened on it; A CLEAN COMPACTION POINT AT RUN 1\'s END — NO ROWS TYPED IN THIS RUN (the window; a departure from sitting 18\'s shape, named in the design): THE MEASUREMENTS (three dumps derived from the forms\' chapter-22 dump by one derive WITH THE SPINE GUARDED — the verses %s, the tokens %s, THE TWO DIVISIONS the identity in all three; the store differs from the DB at %d verse of chapter 29 (29:22 — Zeboiim\'s ketiv and qere) and none elsewhere; the Sifrei\'s heads by chapter %s — ONE in 31 (304 on 31:14), none in 29-30: the spine 304-305, 305 HEADLESS folded in at the split, %s = %d rows on Moses\' death and Joshua\'s commission; %d outside rows over the three chapters — %d read before, %d FRESH from Haazinu\'s and Vezot Habrachah\'s piskaot; eight blank glosses all the pronoun I; NO register seat); THE LEAN MEASURE (%d bytes — the kin, the twins, the formulas, Onkelos, the register and the parser, the prior reads); THE INK (%d asserts in two blocks; %d fell on the first pass — the English rows\' opening apparatus, piska 334\'s chapter guessed, 318:1 read before — %d and %d on the second and third; the parser\'s false six at 30:9 and the seven\'s four homographs asserted); THE DESIGN in the map (%d bytes — 15 claims over three units, the fold predicted %d -> 247 units and %d -> 2344 standing, TWO RUNS + the tail with RUN 1 rowless); the forms copied, the home-path gate green; %d timed steps. NEXT: RUN 2 after the compaction — THE_STEPS Step 2 and Step 5 reread; THE ROWS read whole and typed in slices (Onkelos 29, 30, 31 — 78; the spine 304-305 — 8; the nineteen outside rows), the import check, the ledger deu_29_31_nitzavim_vayelech_2026-09-27.md (coverage computed), the manifests (15 claims; the middah codes checked in MIDDOT.md), the seat, the fold, build_world, the chain LAUNCHED; the clean point; then THE TAIL (the summary, the display patch, verify_claims, the labels census, the records, the debt line (10), the message); the commit on his word (18b and 19 together). POST-COMPACTION REREADS: the recovery page, the map\'s newest section ("Sitting 19 — CHAPTERS 29-31 … LEAN"), MEMORY.md; then this checkpoint; THE_STEPS Step 2 + Step 5 before the ledger.'
        % (NV, TOK, MIS[29], HEADS, TOT, TOTN, NOUT, PRIOR, FRESH, MSZ, NA, F[0], F[1], F[2], DBYTES, U0, S0, NT))
rec = rd(REC); i, j = rec.index('## 2. WHERE IT STANDS'), rec.index('## 3. THE STANDING LAWS'); assert 0 < i < j
SEC2 = ('## 2. WHERE IT STANDS (2026-09-27; #227 — sitting 19 RUN 1, newest)\n'
        '- NUMBERS CLOSED. DEUTERONOMY 1:1-28:69 ON THE TAPE (1-25 PUSHED through 68191ea; 26-28\'s compile uncommitted); 29-31 in reading.\n'
        '- %d units, standing %d, hash 8b8fff1fa28953af. 75 runners, 80 daemons; 1233 kinds / 1340 effects.\n'
        '- THE TAPE at RUN (1403, 96, 88, 0, 12, 1929, 51, 319, pairs, 127); 10/10 on its 4 runs (DL1-DL5); checkpoint_check 341 rows, 18 miss.\n'
        '- ⚠ THE LEAN PASS (#208): 16-34 in 8 lean sittings — core shelf, 4 records, chain once; full process OWED.\n'
        '- SITTING 18b (ch 26-28 COMPILE, LEAN) DONE at #226: chain ALL GREEN (2nd pass); message at <scratch>/commit_msg_ch26b.txt.\n'
        '- SITTING 19 (ch 29-31 READ, LEAN, three units; the Sifrei\'s spine 304-305 on 31:14-23 ALONE) RUN 1 at #227: dumps, split, measure, ink %d/0, design; NO ROWS YET. NEXT: RUN 2 after the compaction — the rows (Onkelos 78, spine %d, outside %d), the ledger, the manifests, the freeze, the chain; the tail; the commit (18b + 19).\n\n\n'
        % (U0, S0, NA, TOTN, NOUT))
rec2 = rec[:i] + SEC2 + rec[j:]
mm = rd(MM)
OLDL = 'NEXT: the commit on his word, then 19 (the reading of 29-31, lean)'
NEWL = 'NEXT: the commit on his word; 19 (ch 29-31 READ, lean, three units — the Sifrei\'s spine 304-305 on 31:14-23 alone, 29-30 Onkelos and the outside rows) RUN 1 at #227 2026-09-27 (the dumps, the split, the measure, the ink %d/0, the design; NO rows yet — the window opened at 387k); NEXT: RUN 2 after a compaction (the rows — Onkelos 78, the spine %d, the outside %d; the ledger, the manifests, the freeze, the chain launched), the tail, then the commit (18b + 19)' % (NA, TOTN, NOUT)
assert mm.count(OLDL) == 1, mm.count(OLDL); mm2 = mm.replace(OLDL, NEWL)
mw = rd(MW)
DESC_OLD = 'description: "SITTING 18b DONE 2026-09-27 ('
assert mw.count(DESC_OLD) == 1
mw2 = mw.replace(DESC_OLD, 'description: "SITTING 19 RUN 1 AT ITS CLEAN POINT 2026-09-27 (chapters 29-31 READ lean, three units — the Sifrei spine 304-305 on 31:14-23 alone, 29-30 without a piska; the ink %d/0; the design; NO rows yet — the window opened at 387k; NEXT RUN 2 after a compaction: the rows, the ledger, the manifests, the freeze, the chain launched; then the tail; then the commit) — SITTING 18b DONE 2026-09-27 (' % NA, 1)
NOTE = ('\n\nSITTING 19 RUN 1 AT ITS CLEAN POINT 2026-09-27 — CHAPTERS 29-31\'s READING IN THE LEAN FORM (the eleventh sitting of [[lean-pass-ruling]], the second on chapters WITHOUT A SPINE PISKA; opened on the owner\'s "Continue" after 18b\'s tail without a compaction at 387k; the tree UNCOMMITTED since 68191ea, 18b riding): one derive and three dumps with THE SPINE GUARDED (the Sifrei heads %s — one in 31 at 31:14, none in 29-30), the split (%d rows in piskaot 304-305 — 305 HEADLESS, six long rows on Moses\' death read WHOLE from the export; %d outside rows over the three chapters, %d read before, %d fresh from the piskaot ahead), the lean measure (%d bytes), the ink\'s %d asserts (%d/%d/%d — the English rows open with the translator\'s apparatus; piska 334 heads on 32:44; 318:1 read before; the parser\'s false six at 30:9 and the seven\'s four homographs), the design (%d bytes — 15 claims over three units; TWO RUNS + the tail, RUN 1 ROWLESS by the window). NEXT: RUN 2 after the compaction — the rows, the ledger, the manifests, the seat, the fold, the chain launched; the tail; the commit on his word.\n'
        % (HEADS, TOTN, NOUT, PRIOR, FRESH, MSZ, NA, F[0], F[1], F[2], DBYTES))
mw2 = mw2.rstrip('\n') + NOTE
rec_bytes = len(rec2.encode()); mm_bytes = len(mm2.encode())
assert rec_bytes <= 10240, ('the recovery page over its cap', rec_bytes)
assert mm_bytes < 17000, ('MEMORY.md over its cap', mm_bytes)
assert not re.search(r'[֐-׿]', P227 + SEC2 + NOTE + NEWL), 'no Hebrew script in the new texts'
home = os.path.expanduser('~'); assert home not in P227 + NOTE + NEWL + SEC2 and SP not in P227 + NOTE + NEWL + SEC2
print('THE POINT CHECKED: #227 %d bytes; the recovery page %d; MEMORY.md %d; the walk note %d' % (len(P227.encode()), rec_bytes, mm_bytes, len(mw2.encode())))
if not CHECK:
    open(SD, 'w', encoding='utf-8').write(sd.rstrip('\n') + P227 + '\n')
    open(REC, 'w', encoding='utf-8').write(rec2); open(MM, 'w', encoding='utf-8').write(mm2); open(MW, 'w', encoding='utf-8').write(mw2)
    for f in (SD, REC, MM, MW):
        out = subprocess.run(['python3', f'{ROOT}/logic/solo_tools/gloss_lint.py', f], capture_output=True, text=True).stdout.strip().split('\n')[-1]
        print('  lint', os.path.basename(f), out)
    print('THE POINT WRITTEN: #227, the recovery page (%d bytes), MEMORY.md (%d bytes), the walk note' % (rec_bytes, mm_bytes))
