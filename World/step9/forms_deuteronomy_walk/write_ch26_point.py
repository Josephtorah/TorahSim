import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE DEUTERONOMY WALK 18 (LEAN, 2026-09-26): THE CLEAN COMPACTION POINT at RUN 1's end — the state doc's #223, the recovery page (section 2 rewritten under its cap),
# the memory (the index line and the walk note) — written in ONE call after chapter 26's rows are checked; every number READ FROM ITS PRINT (the three dumps', the
# split's, the measure's size, the ink runs', the check's, CORPUS_TRUTH's literals, the map's own section); every text built whole before a file is opened; the
# lints and the caps asserted. --check prints without writing. write_ch22_point.py's form over three chapters and two runs. RUN FROM THE REPO ROOT.
import os, re, sys, subprocess
ROOT = _ROOT
SP = os.path.dirname(os.path.abspath(__file__))
MEM = os.path.expanduser('~/.claude/projects/-Users-Shared-TorahSim/memory')
CHECK = '--check' in sys.argv
SD = f'{ROOT}/logic/pre_logic_methods_2026-07-28/PROMPT_continue_solo_era_2026-08-06.md'; REC = f'{ROOT}/logic/pre_logic_methods_2026-07-28/RECOVERY_new_thread_2026-09-12.md'
MM = f'{MEM}/MEMORY.md'; MW = f'{MEM}/deuteronomy-walk.md'; MAP = f'{ROOT}/World/step9/DEUTERONOMY_WALK.md'
def rd(p): return open(p, encoding='utf-8').read()
def R(pat, text, name):
    g = re.search(pat, text, re.M); assert g, (name, pat); return g.group(1)
D = {c: rd(f'{SP}/ch{c}_dump0.out') for c in (26, 27, 28)}
NV = {c: int(R(r'^  DB verses (\d+) \|', D[c], 'verses')) for c in D}; TOK = {c: int(R(r'^  token count chapter \d+ : (\d+)', D[c], 'tokens')) for c in D}
MIS = {c: len(eval(R(r"verses whose store token count differs from the DB: (\[.*?\])$", D[c], 'mismatch'))) for c in D}
HEADS = {c: len(eval(R(r'^  heads whose chapter is \d+ : (\[.*?\]) \|', D[c], 'heads'))) for c in D}
sp_ = rd(f'{SP}/ch26_split.out'); TOT = R(r'\| totals (\{[^}]*\}) \d+$', sp_, 'the split'); TOTN = int(R(r'\| totals \{[^}]*\} (\d+)$', sp_, 'the split total')); NOUT = int(R(r'^the outside rows \[.*?\] (\d+) \|', sp_, 'outside'))
MSZ = os.path.getsize(f'{SP}/ch26_measure_lean.out')
F = [int(R(r'^(\d+) failing statements', rd(f'{SP}/ch26_ink_run{i}.out'), f'run{i}')) for i in (1, 2)]; assert F[1] == 0, F
NA = len(re.findall(r'^assert ', rd(f'{SP}/ch26_ink_body.py'), re.M))
ck = rd(f'{SP}/ch26_rows_check_a.out'); assert 'THE RUN-1 IMPORT CHECK GREEN' in ck
NS = int(R(r'^THE SIFREI ROWS TYPED \(chapter 26\): (\d+) \|', ck, 'sifrei')); NO = int(R(r'Onkelos typed: (\d+) ==', ck, 'onkelos')); PB = int(R(r'bytes of prose: (\d+)', ck, 'prose'))
VS, VO = re.search(r"the verdicts: Counter\((\{[^}]*\})\) Counter\((\{[^}]*\})\)", ck).groups(); FAILS = R(r"the cuts' misses \(FAIL\): (\[.*?\])$", ck, 'fails'); assert FAILS == '[]', FAILS
ct = rd(f'{ROOT}/logic/corpus/CORPUS_TRUTH.py'); U0 = int(R(r'assert len\(W\["units"\]\) == (\d+)', ct, 'U0')); S0 = int(R(r'assert len\(W\["standing"\]\) == (\d+)', ct, 'S0'))
m = rd(MAP); i = m.index('## Sitting 18 — CHAPTERS 26-28'); DBYTES = len(m[i:].encode()); assert '## Sitting 18 — CHAPTERS 26-28 — AS BUILT' not in m and m.find('\n## ', i + 10) < 0
NT = len([l for l in rd(f'{SP}/ch26_timing.tsv').split('\n') if l.startswith(('0', '1', '2'))])
print('THE PRINTS: verses %s; tokens %s; mismatches %s; heads %s; the split totals %s = %d, outside %d; the measure %d bytes; the ink %d asserts (%d/%d); the rows %d + %d (%d bytes), verdicts %s / %s, FAIL %s; the fold %d/%d; the design %d bytes; %d timed steps' % (NV, TOK, MIS, HEADS, TOT, TOTN, NOUT, MSZ, NA, F[0], F[1], NS, NO, PB, VS, VO, FAILS, U0, S0, DBYTES, NT))
# ---- #223 ----
sd = rd(SD); assert '\n#223 ' not in sd and '\n#222 (' in sd
P223 = ('\n\n#223 (2026-09-26, THE DEUTERONOMY WALK sitting 18 — CHAPTERS 26-28\'s READING IN THE LEAN FORM, the lean pass\'s ninth sitting, its fifth reading and the first on chapters WITHOUT A SPINE PISKA, RUN 1 of two; on the owner\'s "Continue" after sitting 17b\'s tail with NO compaction between (/context 202k at the open) — no commit word said, the tree UNCOMMITTED since f730559 with sittings 15, 15b, 16, 16b, 17 and 17b riding, 18 opened on it; A CLEAN COMPACTION POINT AT RUN 1\'s END: THE MEASUREMENTS (three dumps derived from the forms\' chapter-22 dump by one derive WITH THE SPINE GUARDED for a chapter with no head — the verses %s, the tokens %s, THE TWO DIVISIONS the identity in all three; the store differs from the DB at %d verses of chapter 28 and none elsewhere — 28:27 and 28:30 the ketiv/qere seats, the store one token more at each, COMPUTED; the Sifrei\'s heads by chapter %s — FOUR in chapter 26, NONE in 27 and 28: the Sifrei runs 303 on 26:15 to 304 on 31:14; the split — the spine 297-303 on chapter 26 alone, %s rows = %d, with the THREE HEADLESS piskaot 298 (inside 26:2, the basket), 299 (inside 26:3, the declaration) and 303 (inside 26:13-15, twenty rows — the confession of the tithe) joined WHOLE from the export, 26:16-19 without a row; %d outside rows over the three chapters — twenty-five read before at chapters 6, 8, 11-17 and 22-25, one fresh (347:3 on 27:20); the lean measure %d bytes read in four slices), THE INK (%d asserts typed from the six prints; %d fell on the first pass — 301:1, a spine row citing 27:14, listed by chapter 27\'s dump among ITS outside rows and returned to the spine by the split: the leg retyped from the print; %d on the second; the parser\'s FALSE HIT asserted — 28:63\'s "rejoiced" (sas) read as SIX), THE DESIGN in the map ("Sitting 18 — CHAPTERS 26-28 … LEAN", %d bytes, lint 0 — FIVE units deu_26_bikkurim_close, deu_27_ebal_curses, deu_28_blessings, deu_28_curses_a, deu_28_curses_b; TWENTY-ONE claims predicted, the fold 239 -> 244 and 2308 -> 2329; TWO RUNS + THE TAIL; the risks named — the spineless stretch\'s grain, the false six, the ketiv/qere, the seven blank "I" glosses), THE ROWS OF CHAPTER 26 typed and checked (%d Sifrei rows in four files %s — 301 in two halves; %d Onkelos rows %s; %d bytes of prose; the cuts\' misses %s ON THE FIRST RUN — every consonantal token found); the fold UNMOVED at %d/%d (NOT frozen); %d timed steps; the tree UNCOMMITTED. NEXT: RUN 2 after the compaction — the twenty-six outside rows read whole and typed (ch26_outside_rows.txt), Onkelos 27 (26 verses) and 28 (69 verses) read whole from ch27_onkelos.txt and ch28_onkelos.txt and typed in slices, the import check B; THE_STEPS Step 2 and Step 5 reread; the ledger (write_ch26_ledger.py from the forms\' write_ch22_ledger.py — five units, one ledger deu_26_28_ki_tavo_2026-09-26.md, coverage COMPUTED), the manifests (write_ch26_manifest.py — twenty-one claims; every middah code checked in MIDDOT.md before it is typed), the seat (seat_ch26.py from derive_ch22_seat.py\'s form), the fold, build_world, THE GATES CHAIN LAUNCHED at RUN 2\'s end (the forms\' ch22_gates_wrap.sh, ch22_gates.sh, ch22_chain.sh, ch22_fold.sh derived — seat, verify_text, ritual x5, the fold, build_world, the journal gate, the register gate --strict; the DONE file), the clean point #224; then THE TAIL (the summary once, the display patch — the seven anokhi glosses probed first, verify_claims, the labels census, the four records, the debt line (8), the message folding commit_msg_ch22b.txt, the forms); then the commit on his word ("Commit" = no push; "commit push" = both). POST-COMPACTION REREADS: the recovery page, the map\'s newest section ("Sitting 18 — CHAPTERS 26-28 … LEAN" — the design; THE ORDER paragraph names RUN 2\'s steps), MEMORY.md; then this checkpoint.'
        % (NV, TOK, MIS[28], HEADS, TOT, TOTN, NOUT, MSZ, NA, F[0], F[1], DBYTES, NS, VS, NO, VO, PB, FAILS, U0, S0, NT))
# ---- the recovery page (section 2 rewritten whole, under its cap) ----
rec = rd(REC); i, j = rec.index('## 2. WHERE IT STANDS'), rec.index('## 3. THE STANDING LAWS'); assert 0 < i < j
SEC2 = ('## 2. WHERE IT STANDS (2026-09-26; #223 sitting 18 RUN 1 newest)\n'
        '- NUMBERS CLOSED. DEUTERONOMY 1:1-25:19 ON THE TAPE (PUSHED through f730559 — 1-16; 17-25 uncommitted).\n'
        '- %d frozen units, standing %d, hash 8b8fff1fa28953af. 74 runners, 79 daemons; 1212 kinds / 1249 effects.\n'
        '- THE TAPE at RUN (1382, 96, 88, 0, 12, 1833, 50, 319, pairs, 127); 10/10 (DK1-DK5); checkpoint_check 336 rows, 18 known misses.\n'
        '- ⚠ THE LEAN PASS (#208): 16-34 in 8 lean sittings — core shelf, 4 records, chain once; full process OWED.\n'
        '- SITTINGS 15-17b (ch 17-25 READ + COMPILED, LEAN): chains green; UNCOMMITTED since f730559; the message at <scratch>/commit_msg_ch22b.txt.\n'
        '- SITTING 18 (ch 26-28 READ, LEAN, five units; the Sifrei\'s spine for 26 ALONE) RUN 1 at #223: ink %d/0; design; ch 26\'s rows (%d + %d) checked, 0 misses; NOT frozen. NEXT: RUN 2 — the %d outside rows, Onkelos 27-28, the ledger, the freeze, the chain; the tail; the commit on his word.\n\n\n'
        % (U0, S0, NA, NS, NO, NOUT))
rec2 = rec[:i] + SEC2 + rec[j:]
# ---- the memory ----
mm = rd(MM)
OLDL = 'UNCOMMITTED; NEXT: the commit on his word, then 18 (the reading from 26:1, lean)'
NEWL = 'UNCOMMITTED; 18 (ch 26-28 READ, lean, five units — the Sifrei\'s spine for 26 alone, 27-28 Onkelos and the outside rows) RUN 1 at #223 2026-09-26 (the ink %d/0, the design, ch 26\'s rows checked — 0 cut misses); NEXT: RUN 2 (the %d outside rows, Onkelos 27-28, the ledger, the manifests, the freeze, the chain launched), the tail, then the commit on his word' % (NA, NOUT)
assert mm.count(OLDL) == 1, mm.count(OLDL); mm2 = mm.replace(OLDL, NEWL)
mw = rd(MW)
DESC_OLD = 'description: "SITTING 17b DONE 2026-09-26 ('
assert mw.count(DESC_OLD) == 1
mw2 = mw.replace(DESC_OLD, 'description: "SITTING 18 RUN 1 AT ITS CLEAN POINT 2026-09-26 (chapters 26-28 READ lean, five units — the Sifrei spine for 26 alone, 27-28 without a piska; the ink %d/0; the design; chapter 26\'s rows typed and checked with 0 cut misses; NOT frozen; NEXT RUN 2: the %d outside rows, Onkelos 27-28, the ledger, the manifests, the freeze, the chain launched; then the tail; then the commit) — SITTING 17b DONE 2026-09-26 (' % (NA, NOUT), 1)
NOTE = ('\n\nSITTING 18 RUN 1 AT ITS CLEAN POINT 2026-09-26 — CHAPTERS 26-28\'s READING IN THE LEAN FORM (the ninth sitting of [[lean-pass-ruling]], the first on chapters WITHOUT A SPINE PISKA; opened on the owner\'s "Continue" after 17b\'s tail without a compaction; the tree UNCOMMITTED since f730559, 15 through 17b riding): one derive and three dumps with THE SPINE GUARDED (the Sifrei heads %s — four in 26, none in 27-28: it runs 303 on 26:15 to 304 on 31:14), the split (%d rows in piskaot 297-303 — the THREE HEADLESS 298, 299, 303 read WHOLE from the export; %d outside rows over the three chapters, one fresh), the lean measure (%d bytes), the ink\'s %d asserts (%d/%d — a spine row citing 27:14 listed among chapter 27\'s outside rows; the parser\'s false six at 28:63 asserted), the design (%d bytes — 21 claims over five units; TWO RUNS + the tail), the rows of chapter 26 typed and checked (%d + %d; 0 cut misses on the first run). LESSONS SO FAR: a chapter with no spine piska needs the dump\'s SPINE guarded (an empty list indexed); a spine row citing a sister chapter falls into that chapter\'s outside set and comes back at the split; the consonantal phrase search misses prefixed forms (me-reshit, be-har, be-sefer) — the prefixed seat asserted beside. NEXT: RUN 2 (the outside rows, Onkelos 27-28 in slices, check B, THE_STEPS Step 2 and 5, the ledger, the manifests, the seat, the chain launched, #224), the tail, then the commit on his word.\n'
        % (HEADS, TOTN, NOUT, MSZ, NA, F[0], F[1], DBYTES, NS, NO))
mw2 = mw2.rstrip('\n') + NOTE
rec_bytes = len(rec2.encode()); mm_bytes = len(mm2.encode())
assert rec_bytes <= 10240, ('the recovery page over its cap', rec_bytes)
assert mm_bytes < 17000, ('MEMORY.md over its cap', mm_bytes)
assert not re.search(r'[֐-׿]', P223 + SEC2 + NOTE + NEWL), 'no Hebrew script in the new texts'
home = os.path.expanduser('~'); assert home not in P223 + NOTE + NEWL + SEC2 and SP not in P223 + NOTE + NEWL + SEC2
print('THE POINT CHECKED: #223 %d bytes; the recovery page %d; MEMORY.md %d; the walk note %d' % (len(P223.encode()), rec_bytes, mm_bytes, len(mw2.encode())))
if not CHECK:
    open(SD, 'w', encoding='utf-8').write(sd.rstrip('\n') + P223 + '\n')
    open(REC, 'w', encoding='utf-8').write(rec2); open(MM, 'w', encoding='utf-8').write(mm2); open(MW, 'w', encoding='utf-8').write(mw2)
    for f in (SD, REC, MM, MW):
        out = subprocess.run(['python3', f'{ROOT}/logic/solo_tools/gloss_lint.py', f], capture_output=True, text=True).stdout.strip().split('\n')[-1]
        print('  lint', os.path.basename(f), out)
    print('THE POINT WRITTEN: #223, the recovery page (%d bytes), MEMORY.md (%d bytes), the walk note' % (rec_bytes, mm_bytes))
