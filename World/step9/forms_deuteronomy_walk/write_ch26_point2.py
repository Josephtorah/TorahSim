import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE DEUTERONOMY WALK 18 (LEAN, 2026-09-26): THE CLEAN COMPACTION POINT at RUN 2's end — the state doc's #224, the recovery page (section 2 rewritten under its cap),
# the memory (the index line and the walk note) — written in ONE call after the ledger, the manifests and the seat are on disk and THE GATES CHAIN IS LAUNCHED; every
# number READ FROM ITS PRINT (check A's and B's, the ledger's, the manifest's, the seat derive's, CORPUS_TRUTH's literals before the fold, the timing); every text built
# whole before a file is opened; the lints and the caps asserted. --check prints without writing. write_ch26_point.py's form (RUN 1's) carried to RUN 2. RUN FROM THE REPO ROOT.
import os, re, sys, subprocess
ROOT = _ROOT
SP = os.path.dirname(os.path.abspath(__file__))
MEM = os.path.expanduser('~/.claude/projects/-Users-Shared-TorahSim/memory')
CHECK = '--check' in sys.argv
SD = f'{ROOT}/logic/pre_logic_methods_2026-07-28/PROMPT_continue_solo_era_2026-08-06.md'; REC = f'{ROOT}/logic/pre_logic_methods_2026-07-28/RECOVERY_new_thread_2026-09-12.md'
MM = f'{MEM}/MEMORY.md'; MW = f'{MEM}/deuteronomy-walk.md'
def rd(p): return open(p, encoding='utf-8').read()
def R(pat, text, name):
    g = re.search(pat, text, re.M); assert g, (name, pat); return g.group(1)
ca = rd(f'{SP}/ch26_rows_check_a.out'); assert 'THE RUN-1 IMPORT CHECK GREEN' in ca
NS = int(R(r'^THE SIFREI ROWS TYPED \(chapter 26\): (\d+) \|', ca, 'sifrei A')); NO1 = int(R(r'Onkelos typed: (\d+) ==', ca, 'onkelos A'))
cb = rd(f'{SP}/ch26_rows_check_b.out'); assert 'THE RUN-2 IMPORT CHECK GREEN' in cb
NX = int(R(r'^THE OUTSIDE ROWS TYPED: (\d+) \|', cb, 'outside')); VX = R(r"^  the verdicts: Counter\((\{[^}]*\})\)$", cb, 'outside verdicts'); NRR = int(R(r'the REREAD marks: (\d+) \|', cb, 'reread'))
EX = R(r'^  the EXCLUDED rows: (\[.*?\]) \|', cb, 'excluded'); NO2 = int(R(r'^ONKELOS TYPED \(27-28\): (\d+) \|', cb, 'onkelos B')); BYC = R(r'\| by chapter: (\{[^}]*\}) \|', cb, 'by chapter')
VO = R(r"^ONKELOS TYPED.*\n  the verdicts: Counter\((\{[^}]*\})\)$", cb, 'onkelos verdicts'); PB = int(R(r'bytes of prose: (\d+)', cb, 'prose')); FAILS = R(r"the cuts' misses \(FAIL\): (\[.*?\])$", cb, 'fails'); assert FAILS == '[]', FAILS
lg = rd(f'{SP}/ch26_ledger.out'); LB = int(R(r'THE LEDGER WRITTEN: .* — ([\d,]+) bytes;', lg, 'ledger bytes').replace(',', '')); NSRC = int(R(r'; sources (\d+) \(', lg, 'sources')); LK = R(r'the kin (\d+ ledgers / \d+ rows) computed', lg, 'kin'); LLINT = R(r'lint: gloss_lint: (\d+) flag', lg, 'lint'); assert LLINT == '0', LLINT
NEXC = int(R(r'; (\d+) excluded\)', lg, 'excluded'))
mf = rd(f'{SP}/ch26_manifest.out'); NCL = int(R(r'^claims (\d+) \|', mf, 'claims')); assert 'used by exactly one claim: True' in mf; NMF = len(re.findall(r'^wrote ', mf, re.M))
sd_ = rd(f'{SP}/ch26_seat_derive.out'); SEATS = R(r'five units, ([\d +]+) seats', sd_, 'seats')
ct = rd(f'{ROOT}/logic/corpus/CORPUS_TRUTH.py'); U0 = int(R(r'assert len\(W\["units"\]\) == (\d+)', ct, 'U0')); S0 = int(R(r'assert len\(W\["standing"\]\) == (\d+)', ct, 'S0')); assert (U0, S0) in ((239, 2308), (244, 2329)), (U0, S0)   # before the chain's fold step, or the tripwire already set to the prediction by it
NT = len([l for l in rd(f'{SP}/ch26_timing.tsv').split('\n') if l.startswith(('0', '1', '2'))])
LAUNCHED = os.path.exists(f'{SP}/ch26_gates.log') and not os.path.exists(f'{SP}/ch26_gates.DONE')
print('THE PRINTS: check A %d + %d; check B outside %d %s (reread %d, excluded %s), Onkelos %d %s %s, %d bytes, FAIL %s; the ledger %d bytes, %d sources (%d excluded), the kin %s, lint %s; the manifests %d files / %d claims; the seats %s; the tripwire %d/%d; %d timed steps; the chain launched: %s' % (NS, NO1, NX, VX, NRR, EX, NO2, BYC, VO, PB, FAILS, LB, NSRC, NEXC, LK, LLINT, NMF, NCL, SEATS, U0, S0, NT, LAUNCHED))
assert LAUNCHED or CHECK, 'the chain is not running — launch it before the point is written'
# ---- #224 ----
sd = rd(SD); assert '\n#224 ' not in sd and '\n#223 (' in sd
P224 = ('\n\n#224 (2026-09-26, THE DEUTERONOMY WALK sitting 18 — CHAPTERS 26-28\'s READING IN THE LEAN FORM, RUN 2 of two; on the owner\'s "Reread and go" after the compaction at #223 — no commit word said, the tree UNCOMMITTED since f730559 with sittings 15 through 17b riding and 18 on it; A CLEAN COMPACTION POINT AT RUN 2\'s END WITH THE GATES CHAIN RUNNING: THE REREADS done (the recovery page, the map\'s design section, MEMORY.md, #223; THE_STEPS Step 2 and Step 5 before the ledger); THE OUTSIDE ROWS (%d read WHOLE in two slices and typed — the verdicts %s, %d REREAD WHOLE as computed, the fresh 347:3; THE DEPARTURE FROM THE DESIGN: %s EXCLUDED — 291:6 and 291:7 cite "Dt.27:9" in the English alone for 25:9\'s own words, the translator\'s misprint (27:9 is "be silent and hear"), sitting 17\'s 352 precedent; the design had listed 291:5-7 as three rows on 27; ch26_ink.EXCLUDED retyped); ONKELOS 27 AND 28 (%d verses read WHOLE — 27 in one slice, 28 in three with the parse lines dropped — and typed %s, the verdicts %s; the ketiv/qere at 28:27 and 28:30 read by Onkelos as the QERE; THE FALSE SIX of 28:63 resolved by the Aramaic\'s "rejoiced" (chadi)); THE IMPORT CHECK B GREEN (%d bytes of prose; the cuts\' misses %s; every key inside OUTSIDE and SPAN); THE LEDGER logic/oral_triage/deu_26_28_ki_tavo_2026-09-26.md (%s bytes; %d sources = 114 Onkelos + 77 spine + 24 outside kept, %d excluded; coverage COMPUTED; the kin %s; the citation counts parsed from the dumps\' prints; lint %s — one flag on the first write, a HYPHENATED English gloss the lint reads as a transliteration, retyped and the ledger rewritten by its own writer under DEU_REWRITE=1); THE MANIFESTS (%d files, %d claims DV26-01..03, DV27-01..04, DV28A-01..04, DV28B-01..05, DV28C-01..05 — every cite index name used by exactly one claim; the middah codes checked in MIDDOT.md and typed only where a row argues by them: I2 at 297:4-5, 301:1, 36:2, 64:2, 69:1, 107:16, 138:1, 291:5, 302:1 and 109:3, none elsewhere — "no middah code typed" said; 104:8 seated by its covenant verse 28:69, an override named in the writer; every check piece cut from the store\'s own bytes); THE SEAT derived (seat_ch26.py from the forms\' seat_ch22.py — %s seats at the claims\' first verses); THE CHAIN SCRIPTS derived (ch26_chain.sh, ch26_fold.sh with the tripwire 239 -> 244 and 2308 -> 2329, ch26_gates.sh, ch26_gates_wrap.sh, ch26_vc.sh); THE GATES CHAIN LAUNCHED at RUN 2\'s end (ch26_gates_wrap.sh — seat x5, verify_text x5, the ritual x5, the fold, build_world, the journal gate, the register gate --strict, large_letter, the home gate; the DONE file ch26_gates.DONE; its SUMMARY ch26_gates_SUMMARY.txt read ONCE at the tail, never polled); the fold\'s tripwire at %d/%d when this point was written (the prediction 244/2329, the hash unmoved — the chain\'s fold step had already set it: the seats, verify_text and the five rituals ran in minutes; the bake\'s own truth print read at the tail); %d timed steps; the tree UNCOMMITTED. NEXT: THE TAIL after the compaction — read the SUMMARY once (if red: the demands filed from the prints, the pass resumed from the failed step — a pass after any source change starts at the seat); verify_claims (ch26_vc.sh); the display patch (the seven anokhi "?" glosses at 27:1, 4, 10 and 28:1, 13, 14, 15 probed first — ch26_patch_probe.py, then the overrides); the labels census --strict; THE FOUR RECORDS (the map\'s AS BUILT — LEAN with the departures, the lessons and the timing table; the state doc\'s NOTE under this checkpoint; the recovery page; the memory) + COMPILE_DEBT\'s lean box line (8) replacing the anchor " 18 (the reading from 26:1): next." and adding " 18b (the compile of 26-28): next."; the commit message write_ch26_commit_msg.py folding commit_msg_ch22b.txt (the trailers once); the forms; then THE COMMIT ON HIS WORD ONLY ("Commit" = no push; "commit push" = both). POST-COMPACTION REREADS: the recovery page, the map\'s newest section ("Sitting 18 — CHAPTERS 26-28 … LEAN"), MEMORY.md; then this checkpoint.'
        % (NX, VX, NRR, EX, NO2, BYC, VO, PB, FAILS, f'{LB:,}', NSRC, NEXC, LK, LLINT, NMF, NCL, SEATS, U0, S0, NT))
# ---- the recovery page (section 2 rewritten whole, under its cap) ----
rec = rd(REC); i, j = rec.index('## 2. WHERE IT STANDS'), rec.index('## 3. THE STANDING LAWS'); assert 0 < i < j
SEC2 = ('## 2. WHERE IT STANDS (2026-09-26; #224 sitting 18 RUN 2 newest)\n'
        '- NUMBERS CLOSED. DEUTERONOMY 1:1-25:19 ON THE TAPE (PUSHED through f730559 — 1-16; 17-25 uncommitted).\n'
        '- units %d / standing %d (the tripwire set; the truth at the tail), hash 8b8fff1fa28953af. 74 runners, 79 daemons; 1212 kinds / 1249 effects.\n'
        '- THE TAPE at RUN (1382, 96, 88, 0, 12, 1833, 50, 319, pairs, 127); 10/10 (DK1-DK5); checkpoint_check 336 rows, 18 known misses.\n'
        '- ⚠ THE LEAN PASS (#208): 16-34 in 8 lean sittings — core shelf, 4 records, chain once; full process OWED.\n'
        '- SITTINGS 15-17b (ch 17-25 READ + COMPILED, LEAN): chains green; UNCOMMITTED since f730559; the message at <scratch>/commit_msg_ch22b.txt.\n'
        '- SITTING 18 (ch 26-28 READ, LEAN, five units) RUN 2 at #224: ledger %d sources, %d claims, the seat; THE CHAIN LAUNCHED — <scratch>/ch26_gates_SUMMARY.txt read ONCE at the tail. NEXT: the tail (summary, verify_claims, the display patch, 4 records, debt line (8), the message), then the commit on his word.\n\n\n'
        % (U0, S0, NSRC, NCL))
rec2 = rec[:i] + SEC2 + rec[j:]
# ---- the memory ----
mm = rd(MM)
OLDL = R(r'(RUN 1 at #223 2026-09-26 \(the ink 41/0, the design, ch 26\'s rows checked — 0 cut misses\); NEXT: RUN 2 \(the 26 outside rows, Onkelos 27-28, the ledger, the manifests, the freeze, the chain launched\), the tail, then the commit on his word)', mm, 'the walk line')
NEWL = 'RUN 2 at #224 2026-09-26 (the ledger %d sources, lint 0; %d claims; the chain LAUNCHED — the seat, the freeze x5, the fold 239->244, the gates; its summary read at the tail); NEXT: the tail (the summary once, verify_claims, the display patch, the four records, the debt line (8), the message), then the commit on his word' % (NSRC, NCL)
assert mm.count(OLDL) == 1; mm2 = mm.replace(OLDL, NEWL)
mw = rd(MW)
DESC_OLD = 'description: "SITTING 18 RUN 1 AT ITS CLEAN POINT 2026-09-26 ('
assert mw.count(DESC_OLD) == 1
mw2 = mw.replace(DESC_OLD, 'description: "SITTING 18 RUN 2 AT ITS CLEAN POINT 2026-09-26 (chapters 26-28 READ lean — the ledger %d sources, %d claims, the seat derived, THE CHAIN LAUNCHED; the tail next: the summary, the records, the message; then the commit on his word) — SITTING 18 RUN 1 AT ITS CLEAN POINT 2026-09-26 (' % (NSRC, NCL), 1)
NOTE = ('\n\nSITTING 18 RUN 2 AT ITS CLEAN POINT 2026-09-26 — the twenty-six outside rows read whole (%s; 291:6-7 EXCLUDED for the English\'s "Dt.27:9" misprint — a departure from the design, which counted 291:5-7 as three rows on 27), Onkelos 27 and 28 read whole and typed in four files (%d rows), check B green (%d bytes, 0 cut misses), the ledger (%d sources, lint 0 after one hyphenated gloss retyped), the manifests (%d claims — I2 typed only where a row argues by it; 104:8 seated by 28:69 by a named override), seat_ch26.py derived, the chain scripts derived, THE GATES CHAIN LAUNCHED (the DONE file; the SUMMARY read once at the tail). LESSONS OF RUN 2: (1) an outside row\'s citation of the chapter is checked against the HEBREW\'S OWN WORDS before it counts — the English\'s verse numbers misprint (291:6-7 here, 352 at sitting 17); (2) a hyphenated English word beside Hebrew reads as a transliteration to the lint — no hyphens in a gloss; (3) an outside row is seated in a manifest by the verse it TEACHES ON, not by its first cite (104:8\'s covenants at 28:69) — the override named in the writer; (4) a parser\'s false numeral is settled by Onkelos\'s verb (28:63); (5) the spineless stretch reads at Onkelos\'s grain — every verse a row, the outside rows the shelf\'s voice. NEXT: the tail, then the commit on his word.\n'
        % (VX, NO2, PB, NSRC, NCL))
mw2 = mw2.rstrip('\n') + NOTE
rec_bytes = len(rec2.encode()); mm_bytes = len(mm2.encode())
assert rec_bytes <= 10240, ('the recovery page over its cap', rec_bytes)
assert mm_bytes < 17000, ('MEMORY.md over its cap', mm_bytes)
assert not re.search(r'[֐-׿]', P224 + SEC2 + NOTE + NEWL), 'no Hebrew script in the new texts'
home = os.path.expanduser('~'); assert home not in P224 + NOTE + NEWL + SEC2 and SP not in P224 + NOTE + NEWL + SEC2
print('THE POINT CHECKED: #224 %d bytes; the recovery page %d; MEMORY.md %d; the walk note %d' % (len(P224.encode()), rec_bytes, mm_bytes, len(mw2.encode())))
if not CHECK:
    open(SD, 'w', encoding='utf-8').write(sd.rstrip('\n') + P224 + '\n')
    open(REC, 'w', encoding='utf-8').write(rec2); open(MM, 'w', encoding='utf-8').write(mm2); open(MW, 'w', encoding='utf-8').write(mw2)
    for f in (SD, REC, MM, MW):
        out = subprocess.run(['python3', f'{ROOT}/logic/solo_tools/gloss_lint.py', f], capture_output=True, text=True).stdout.strip().split('\n')[-1]
        print('  lint', os.path.basename(f), out)
    print('THE POINT WRITTEN: #224, the recovery page (%d bytes), MEMORY.md (%d bytes), the walk note' % (rec_bytes, mm_bytes))
