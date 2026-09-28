import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE DEUTERONOMY WALK 20 (LEAN, 2026-09-27): THE CLEAN COMPACTION POINT at RUN 1's end — the state doc's #231, the recovery page (section 2 rewritten under its cap),
# the memory (the index line and the walk note) — written in ONE call after the design; every number READ FROM ITS PRINT (the dump's, the split's, the measure's size and
# its F section, the ink runs', CORPUS_TRUTH's literals, the map's own section); every text built whole before a file is opened; the lints and the caps asserted.
# --check prints without writing. write_ch29_point.py's form (RUN 1 rowless — the window opened at 332k). RUN FROM THE REPO ROOT.
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
D = rd(f'{SP}/ch32_dump0.out')
NV = int(R(r'^  DB verses (\d+) \|', D, 'verses')); TOK = int(R(r'^  token count chapter 32 : (\d+)', D, 'tokens')); COST = int(R(r'^  the alignment cost (\d+) \|', D, 'cost'))
MIS = ast.literal_eval(R(r"verses whose store token count differs from the DB: (\[.*?\])$", D, 'mismatch')); HEADS = len(ast.literal_eval(R(r'^  heads whose chapter is 32 : (\[.*?\]) \|', D, 'heads')))   # the list ends at the first ' |' (the line carries the heads by chapter after it)
sp_ = rd(f'{SP}/ch32_split.out'); TOT = int(R(r'\| totals \{32: (\d+)\} \d+$', sp_, 'the split')); NOUT = int(R(r'^the outside rows \[.*?\] (\d+) \|', sp_, 'outside')); BYT = int(R(r'\| total (\d+)$', sp_, 'bytes')); PLAN = R(r"^the run plan under \d+ bytes a slice: (\[.*\]) \| slices (\d+)$", sp_, 'plan'); NSL = int(R(r'\| slices (\d+)$', sp_, 'slices'))
ms = rd(f'{SP}/ch32_measure_lean.out'); MSZ = len(ms.encode()); SPR = int(R(r'^  spine rows read before: (\d+) \[', ms, 'spine prior')); PRIOR = len(ast.literal_eval(R(r'outside rows read before: (\{.*\}) \| fresh:', ms, 'prior'))); FRESH = len(ast.literal_eval(R(r'\| fresh: (\[.*\])$', ms, 'fresh')))
F = [int(R(r'^(\d+) failing statements', rd(f'{SP}/ch32_ink_run{i}.out'), f'run{i}')) for i in (1, 2, 3)]; assert F[1:] == [0, 0], F
NA = sum(len(re.findall(r'^assert ', rd(f'{SP}/{f}'), re.M)) for f in ('ch32_ink_body.py', 'ch32_ink_body_b.py'))
ct = rd(f'{ROOT}/logic/corpus/CORPUS_TRUTH.py'); U0 = int(R(r'assert len\(W\["units"\]\) == (\d+)', ct, 'U0')); S0 = int(R(r'assert len\(W\["standing"\]\) == (\d+)', ct, 'S0'))
m = rd(MAP); i = m.index('## Sitting 20 — CHAPTER 32'); DBYTES = len(m[i:].encode()); assert '## Sitting 20 — CHAPTER 32, THE SONG — AS BUILT' not in m and m.find('\n## ', i + 10) < 0
NT = len([l for l in rd(f'{SP}/ch32_timing.tsv').split('\n') if l.startswith(('0', '1', '2'))])
assert (NV, TOT, NOUT, SPR, PRIOR, FRESH, NA, HEADS, NSL) == (52, 249, 11, 37, 8, 3, 39, 36, 5), (NV, TOT, NOUT, SPR, PRIOR, FRESH, NA, HEADS, NSL)
print('THE PRINTS: verses %d (cost %d); tokens %d; mismatches %s; heads %d; the split %d rows in %d bytes, outside %d (read before %d, fresh %d), spine seats read before %d, the plan %s; the measure %d bytes; the ink %d asserts (%d/%d/%d); the fold %d/%d; the design %d bytes; %d timed steps' % (NV, COST, TOK, MIS, HEADS, TOT, BYT, NOUT, PRIOR, FRESH, SPR, PLAN, MSZ, NA, F[0], F[1], F[2], U0, S0, DBYTES, NT))
sd = rd(SD); assert '\n#231 ' not in sd and '\n#230 (' in sd
P231 = ('\n\n#231 (2026-09-27, THE DEUTERONOMY WALK sitting 20 — CHAPTER 32\'s READING IN THE LEAN FORM, THE SONG, the lean pass\'s thirteenth sitting, its seventh reading and THE FIRST WITH THE SPINE IN FORCE since chapter 26, RUN 1 of four + the tail; on the owner\'s "Continue" after sitting 19b\'s tail and the push c4b14ce with NO compaction between (/context 332k at the open) — the tree CLEAN at c4b14ce; A CLEAN COMPACTION POINT AT RUN 1\'s END — NO ROWS TYPED IN THIS RUN (sitting 19\'s shape): THE MEASUREMENTS (the dump derived from the forms\' chapter-22 dump by sitting 19\'s derive — the verses %d, the tokens %d, THE TWO DIVISIONS the identity (cost %d); the store differs from the DB at %s alone; the Sifrei\'s heads in the chapter %d — THE SPINE IN FORCE, piskaot 306-341 with %d rows in %d bytes, 306 alone thirty-seven rows and 95,532 bytes; ONE HEAD MISPRINTED — 328 cited 32:35 in the Hebrew row\'s own marker, its words 32:38\'s; %d outside rows (%d read before, %d fresh — 346:2, 356:5, 357:27); %d seats of the spine\'s rows read before over twenty-four ledgers, every one to be REREAD WHOLE; the lean measure %d bytes — the song\'s vocabulary its own (eleven verses with no two-token kin), 32:36 whole in Psalm 135:14, twenty phrases once in the Bible, THE SONG NEVER SAYS "THE LORD YOUR GOD", Onkelos\'s Torah school at 32:10 and the world to come at 32:12, the Rock "the Mighty One" eight times; THE PARSER\'s FALSE EIGHT at 32:15 ("you grew fat") and the joined thousand at 32:30 ([1, 1002]) — the compile\'s two guards; the ink %d asserts in three passes (%d/%d/%d — 328\'s marker in the Hebrew row); THE DESIGN in the map (%d bytes — two units deu_32_haazinu 32:1-43 and deu_32_song_aftermath 32:44-52, the claim prefixes DV32 and DV32A, 16 claims predicted, the fold %d -> 249 units and %d -> 2360 standing predicted; THE RUN PLAN BY BYTES from the split\'s print: %s — FOUR RUNS + THE TAIL: RUN 2 Onkelos 52 + the outside 11 + piska 306 whole; RUN 3 piskaot 307-322 (141 rows); RUN 4 piskaot 323-341 (71 rows) + the ledger, the manifests, the seat, the fold, build_world, the chain launched; the tail). %d timed steps so far (ch32_timing.tsv). NEXT: the owner compacts; RUN 2 on "Reread" then "Go" — THE_STEPS Step 2 and Step 5 reread, the rows of the first slice typed whole into per-slice files, the import check, the clean point #232. POST-COMPACTION REREADS: the recovery page, the map\'s newest section ("Sitting 20 — CHAPTER 32, THE SONG, Deuteronomy 32:1-52 — LEAN"), MEMORY.md; then this checkpoint.'
        % (NV, TOK, COST, MIS, HEADS, TOT, BYT, NOUT, PRIOR, FRESH, SPR, MSZ, NA, F[0], F[1], F[2], DBYTES, U0, S0, PLAN, NT))
rec = rd(REC); i, j = rec.index('## 2. WHERE IT STANDS'), rec.index('## 3. THE STANDING LAWS'); assert 0 < i < j
SEC2 = ('## 2. WHERE IT STANDS (2026-09-27; #231 — sitting 20 RUN 1, newest)\n'
        '- NUMBERS CLOSED. DEUTERONOMY 1:1-31:30 ON THE TAPE, ALL PUSHED through c4b14ce (2026-09-27); 32 in reading.\n'
        '- units %d / standing %d, hash 8b8fff1fa28953af. 76 runners, 81 daemons; 1253 kinds / 1399 effects.\n'
        '- THE TAPE at RUN (1423, 102, 94, 0, 12, 2003, 52, 319, pairs, 127); 10/10; MARKERS 173 — Moses\' last day (40, 12, 7) at 31:1; checkpoint_check 346 rows, 18 miss.\n'
        '- ⚠ THE LEAN PASS (#208): 16-34 in 8 lean sittings — core shelf, 4 records, chain once; full process OWED. A MARKER sitting splits RUN B (19b).\n'
        '- SITTING 20 (ch 32 READ, LEAN — THE SONG; the spine IN FORCE 306-341, %d rows) RUN 1 at #231: dump, split, measure, ink %d/0, design (FOUR RUNS + THE TAIL by bytes); NO ROWS YET. NEXT: RUN 2 after the compaction — Onkelos 52, outside %d, piska 306 whole; RUN 3 307-322; RUN 4 323-341 + ledger, manifests, freeze, chain; the tail; the commit.\n\n\n'
        % (U0, S0, TOT, NA, NOUT))
rec2 = rec[:i] + SEC2 + rec[j:]
mm = rd(MM)
OLDL = "NEXT: 20 (the reading of 32, the song, lean) after a compaction"
NEWL = "20 (ch 32 READ, lean — THE SONG; the Sifrei's spine IN FORCE 306-341, %d rows, 358 KB; two units) RUN 1 at #231 2026-09-27 (the dump, the split, the measure, the ink %d/0, the design — FOUR RUNS + THE TAIL by the split's bytes; NO rows yet — the window opened at 332k); NEXT: RUN 2 after a compaction (Onkelos 52, the outside %d, piska 306 whole), RUN 3 (307-322), RUN 4 (323-341 + the ledger, the manifests, the freeze, the chain launched), the tail, then the commit" % (TOT, NA, NOUT)
assert mm.count(OLDL) == 1, mm.count(OLDL); mm2 = mm.replace(OLDL, NEWL)
mw = rd(MW)
DESC_OLD = 'description: "SITTINGS 18b + 19 + 19b PUSHED c4b14ce 2026-09-27 on \'Commit push\' ('
assert mw.count(DESC_OLD) == 1
mw2 = mw.replace(DESC_OLD, 'description: "SITTING 20 RUN 1 AT ITS CLEAN POINT 2026-09-27 (chapter 32 READ lean — the song; the Sifrei spine in force 306-341, %d rows; the ink %d/0; the design: FOUR RUNS + THE TAIL by bytes; NO rows yet — the window opened at 332k; NEXT RUN 2 after a compaction) — SITTINGS 18b + 19 + 19b PUSHED c4b14ce 2026-09-27 on \'Commit push\' (' % (TOT, NA), 1)
NOTE = ('\n\nSITTING 20 RUN 1 AT ITS CLEAN POINT 2026-09-27 — CHAPTER 32\'s READING IN THE LEAN FORM, THE SONG (the thirteenth sitting of [[lean-pass-ruling]], the first with the spine in force since chapter 26; opened on the owner\'s "Continue" after 19b\'s tail and the push c4b14ce without a compaction at 332k): the dump (the verses %d, THE TWO DIVISIONS the identity; the Sifrei\'s heads %d — piskaot 306-341, %d rows in %d bytes, 306 alone thirty-seven rows; 328\'s head misprinted in the Hebrew row\'s marker), the split (%d outside rows — %d read before, %d fresh; the run plan by bytes %s), the lean measure (%d bytes), the ink\'s %d asserts (%d/%d/%d), the design (%d bytes — two units, 16 claims, FOUR RUNS + THE TAIL). THE FINDS: the song\'s vocabulary is its own (eleven verses with no two-token kin; the twins by sense share nothing); 32:36 whole in Psalm 135:14; twenty phrases once in the Bible; the song never says "the LORD your God"; Onkelos: the Rock "the Mighty One", the desert the Torah\'s school (32:10), the world to come (32:12), "I will remove My Shekhinah" (32:20); the parser\'s FALSE EIGHT at 32:15 and the joined thousand at 32:30 — the compile\'s guards; Hoshea\'s old name at 32:44. NEXT: the owner compacts; RUN 2 (Onkelos 52, the outside 11, piska 306 whole), RUN 3 (307-322), RUN 4 (323-341 + the ledger, the manifests, the freeze, the chain launched), the tail; then the commit.\n'
        % (NV, HEADS, TOT, BYT, NOUT, PRIOR, FRESH, PLAN, MSZ, NA, F[0], F[1], F[2], DBYTES))
mw2 = mw2.rstrip('\n') + NOTE
rec_bytes = len(rec2.encode()); mm_bytes = len(mm2.encode())
assert rec_bytes <= 10240, ('the recovery page over its cap', rec_bytes)
assert mm_bytes < 17000, ('MEMORY.md over its cap', mm_bytes)
assert not re.search(r'[֐-׿]', P231 + SEC2 + NOTE + NEWL), 'no Hebrew script in the new texts'
home = os.path.expanduser('~'); assert home not in P231 + NOTE + NEWL + SEC2 and SP not in P231 + NOTE + NEWL + SEC2
print('THE POINT CHECKED: #231 %d bytes; the recovery page %d; MEMORY.md %d; the walk note %d' % (len(P231.encode()), rec_bytes, mm_bytes, len(mw2.encode())))
if not CHECK:
    open(SD, 'w', encoding='utf-8').write(sd.rstrip('\n') + P231 + '\n')
    open(REC, 'w', encoding='utf-8').write(rec2); open(MM, 'w', encoding='utf-8').write(mm2); open(MW, 'w', encoding='utf-8').write(mw2)
    for f in (SD, REC, MM, MW):
        out = subprocess.run(['python3', f'{ROOT}/logic/solo_tools/gloss_lint.py', f], capture_output=True, text=True).stdout.strip().split('\n')[-1]
        print('  lint', os.path.basename(f), out)
    print('THE POINT WRITTEN: #231, the recovery page (%d bytes), MEMORY.md (%d bytes), the walk note' % (rec_bytes, mm_bytes))
