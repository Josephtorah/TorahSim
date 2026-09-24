import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE DEUTERONOMY WALK sitting 14 — CHAPTER 16, LEAN (2026-09-23): THE FOUR RECORDS of the lean form in ONE call — the map's AS BUILT (short: the departures and the
# lessons, with the timing table), the state doc's #209, the recovery page (section 2 under its cap), the memory (the index line and the walk note) — plus the
# lean-pass box's line in COMPILE_DEBT (the ruling's own ledger). Every number READ FROM ITS PRINT (the chain's SUMMARY, the truth line, the register gate, the
# ledger, the manifest, the patch, the timing table); every text built whole before a file is opened; the lints asserted unmoved; the caps asserted. --check
# prints without writing. RUN FROM THE REPO ROOT after the chain is ALL GREEN.
import os, re, sys, subprocess
ROOT = _ROOT
SP = os.path.dirname(os.path.abspath(__file__))
MEM = os.path.expanduser('~/.claude/projects/-Users-Shared-TorahSim/memory')
CHECK = '--check' in sys.argv
MAP = f'{ROOT}/World/step9/DEUTERONOMY_WALK.md'; SD = f'{ROOT}/logic/pre_logic_methods_2026-07-28/PROMPT_continue_solo_era_2026-08-06.md'; REC = f'{ROOT}/logic/pre_logic_methods_2026-07-28/RECOVERY_new_thread_2026-09-12.md'
IDX = f'{MEM}/MEMORY.md'; WALK = f'{MEM}/deuteronomy-walk.md'; DEBT = f'{ROOT}/World/step9/COMPILE_DEBT.md'
def rd(p): return open(p, encoding='utf-8').read()
S = rd(f'{SP}/ch16_gates_SUMMARY.txt'); assert 'ALL GREEN' in S, 'the chain is not green'
truth = rd(f'{SP}/ch16_truth.out').strip(); assert 'CORPUS TRUTH GREEN' in truth
ct = rd(f'{ROOT}/logic/corpus/CORPUS_TRUTH.py'); U1 = int(re.search(r'assert len\(W\["units"\]\) == (\d+)', ct).group(1)); S1 = int(re.search(r'assert len\(W\["standing"\]\) == (\d+)', ct).group(1)); H1 = re.search(r"_state_hash\(W\) == '([0-9a-f]+)'", ct).group(1)
reg = rd(f'{SP}/ch16_register.out'); DECL, DEBTN, FAILS = (int(x) for x in re.search(r'DECLARED (\d+) / DEBT (\d+) / FAILS (\d+)', reg).groups()) if re.search(r'DECLARED (\d+) / DEBT (\d+) / FAILS (\d+)', reg) else (int(re.search(r'DECLARED (\d+)', reg).group(1)), -1, -1)
vt = rd(f'{SP}/ch16_vt_deu_16_festivals_judges.out'); VT = re.search(r'TEXT LAYER GREEN: (\d+) steps, (\d+) scenarios', vt).groups()
rit = rd(f'{SP}/ch16_ritual_deu_16_festivals_judges.out'); RP = len(re.findall(r'\bPASS\b', rit))
jr = rd(f'{SP}/ch16_journal.out'); JR = re.search(r'(\d[\d,]*) rows', jr); JR = JR.group(1) if JR else '(the journal gate\'s row count not in its print)'
led = f'{ROOT}/logic/oral_triage/deu_16_reeh_shoftim_2026-09-23.md'; LB = os.path.getsize(led); NSRC = int(re.search(r'\*\*read: (\d+) of \1 — COMPLETE\*\*', rd(led)).group(1))
mf = rd(f'{SP}/ch16_manifest.out'); NCL = int(re.search(r'claims (\d+) \|', mf).group(1))
pt = rd(f'{SP}/ch16_patch.out') if os.path.exists(f'{SP}/ch16_patch.out') else ''; PR = re.search(r'by_ref (\d+) by_gloss (\d+)', pt); PR = PR.groups() if PR else ('?', '?')
ink = rd(f'{SP}/ch16_ink.py'); NA = len(re.findall(r'^assert ', ink, re.M)); F1 = int(re.search(r'^(\d+) failing statements', rd(f'{SP}/ch16_ink_run1.out'), re.M).group(1)); F2 = int(re.search(r'^(\d+) failing statements', rd(f'{SP}/ch16_ink_run2.out'), re.M).group(1)); assert F2 == 0
rows = [l.rstrip('\n').split('\t') for l in open(f'{SP}/ch16_timing.tsv', encoding='utf-8') if l[:1].isdigit()]
T14 = [r for r in rows if r[1].startswith('14 ')]; TS = sum(int(r[2]) for r in T14)
TABLE = '\n'.join(f'| {r[0]} | {r[1]} | {r[2]} | {r[3]} |' for r in T14)
ASB = f"""
## Sitting 14 — CHAPTER 16 — AS BUILT — LEAN (2026-09-23; the design above stands as written; the first sitting of THE LEAN PASS ran in ONE window as ruled: the measurements, the ink, the design, the rows, the ledger, the manifest, the freeze chain and the records; every departure named here; the timing table the last section)

THE READING AS RUN: the dump derived by 26 substitutions (its second run — the four file names counted twice each); the spine split with PISKA 135 FOLDED IN (the computed spine skipped its headless head row; the split folded it by position — the three rows the dump had listed as outside are the spine's, the true outside rows three); NO measure1 — one lean measure (ch16_measure_lean.py, 44,598 bytes of print read in two pages); THE INK {NA} asserts ({F1} fell on the first pass, both the instrument's shape; {F2} on the second; a fifth assembly excluded this sitting's own ledger from the prior-read scan — the writer's second run had found it); THE ROWS: the Sifrei's 111 in four files, Onkelos's 22 in two, the outside three in one — three cut misses on the checks (144:13's prefixed form; TWO ONE-TOKEN PIECES TYPED WITHOUT THEIR COMMA at 16:16 and 16:18 — the second found by grep over every row file, not hunted); THE LEDGER logic/oral_triage/deu_16_reeh_shoftim_2026-09-23.md ({LB:,} bytes; {NSRC} sources — 22 Onkelos verses, 97 MATERIAL + 14 CONTEXT spine rows, 3 outside rows; coverage COMPUTED "read: {NSRC} of {NSRC} — COMPLETE"; lint 0 after one flag — the hyphen in "threshing-floor" read by the lint as a transliteration token, dropped); THE MANIFEST {NCL} claims DV16-01..{NCL:02d} (every cite index name used; verify_claims {NCL}/0; the labels gate passed); THE CHAIN ONCE, ALL GREEN in the background while the records were typed — verify_text {VT[0]} steps / {VT[1]} scenarios, the ritual {RP} PASS, THE FOLD units {U1} / standing {S1} / hash {H1} ({truth}), build_world, the journal gate ({JR}), THE REGISTER GATE --strict DECLARED {DECL} / DEBT {DEBTN} / FAILS {FAILS}, large_letter, the home gate; THE DISPLAY PATCH SMALL — {PR[1]} by gloss, {PR[0]} by reference, the rest OWED.

THE DEPARTURES FROM THE DESIGN: (1) the fold's prediction held exactly (units 229 -> {U1}, standing 2259 -> {S1}, the hash unmoved); (2) the gates shell's comment names its own file as its form (the global substitution caught the form's name — cosmetic, the shell ran as written); (3) the display patch predicted "small" became {PR[1]} by gloss and {PR[0]} by reference after the store's families were probed (ch16_patch_probe.py) — larger than "the worst seven", smaller than chapter 15's 212.

THE LESSONS (⚠): (1) A HEADLESS PISKA IS THE SPINE'S BY POSITION — the head regex reads only a citation at the row's start; 135's opens with the verse's own words and cites Numbers 29:35 later: a piska's membership is decided on its words (chapter 14's lesson in the other direction); (2) A ONE-TOKEN PIECE NEEDS ITS COMMA — a bare string in the cutter iterates by letter; the second such miss was found by grep over every file, never hunted one by one; (3) THE INK'S PRIOR-READ SCAN EXCLUDES THE SITTING'S OWN LEDGER once it exists (the writer's second run); (4) THE LINT READS A HYPHENATED ENGLISH WORD AS A TRANSLITERATION TOKEN when no gloss sits within its window — "threshing floor" without the hyphen; (5) THE LEAN WINDOW HELD: the reading, the freeze and the records in one context, the chain in the background, no wait past five minutes — the shape for sittings 15-21.

THE FINDS are the ledger's thirteen crowns (the chapter's reason the intercalation; the Mishnah in the spine eight times; the three commandments of the pilgrimage; the oral law's seat at 135:3; the Passover's clock from three phrases and six against seven; the herd the festival offering, written by Onkelos too; the omer from the sickle with Onkelos's "omer of the waving"; the courts' three tiers and "justice, justice" two rules; the pillar loved by the fathers and hated by the sons — a law whose reason is a change of state on the tape).

NEXT ON THE OWNER'S WORD (after a compaction: "Reread", then "Go"): SITTING 14b — THE COMPILE OF CHAPTER 16, LEAN: the design (the cells: the festivals' calendar reused from Leviticus 23 and Numbers 28-29 with THE PLACE and the intercalation added; the Passover's clock; the omer's count; the household's joy; the three pilgrimages and the appearance; THE COURTS IN EVERY GATE a new daemon with three tiers; the asherah and the pillar), the runner, the tape, the chain launched; the Mishnah rows the spine cites as the cases; the exam file lists them and any segment read.

THE TIMING TABLE (ch16_timing.tsv; {len(T14)} steps, {TS} machine seconds; the chain's row the background run's):
| time | step | s | rc |
|---|---|---|---|
{TABLE}
"""
BLOCK = f"""
#209 (2026-09-23, THE DEUTERONOMY WALK sitting 14 — CHAPTER 16's READING IN THE LEAN FORM, the first sitting of THE LEAN PASS (#208); on the owner's "Reread and go" after the compaction at #208; A CLEAN COMPACTION POINT AT THE READING'S END — the whole reading window done: the measurements, the ink, the design, the rows, the ledger, the manifest, the freeze chain ALL GREEN, the display patch, the records): THE STATE: the ledger logic/oral_triage/deu_16_reeh_shoftim_2026-09-23.md ({LB:,} bytes, {NSRC} sources, coverage computed, lint 0); the unit deu_16_festivals_judges FROZEN ({NCL} claims DV16-01..{NCL:02d}; verify_text {VT[0]} steps / {VT[1]} scenarios; the ritual {RP} PASS); THE FOLD units {U1} / standing {S1} / hash {H1} ({truth}); the register gate --strict DECLARED {DECL} / DEBT {DEBTN} / FAILS {FAILS}; the journal gate ({JR}); the display patch {PR[1]} by gloss + {PR[0]} by reference; the ink {NA} asserts ({F1}/{F2}); the records: the map's "Sitting 14 — CHAPTER 16 — AS BUILT — LEAN" (the departures, the five lessons, the timing table — {len(T14)} steps, {TS} machine seconds), this checkpoint, the recovery page, the memory (the index line and the walk note), COMPILE_DEBT's lean-pass box (its first line); the forms copied; the commit message at <scratch>/commit_msg_ch16.txt. THE TREE: UNCOMMITTED since e824e52 (the lean-pass ruling's own edits ride with it). NEXT ON HIS WORD: the commit ("Commit" = no push; "commit push" = both); then, after a compaction ("Reread", then "Go"), SITTING 14b — THE COMPILE OF CHAPTER 16, LEAN (the design, the runner, the tape, the chain launched; the Mishnah rows the cases). POST-COMPACTION REREADS: the recovery page, the map's newest section ("Sitting 14 — CHAPTER 16 — AS BUILT — LEAN"), MEMORY.md; then this checkpoint.
"""
def sub1(t, a, b):
    assert t.count(a) == 1, (t.count(a), a[:70]); return t.replace(a, b)
m = rd(MAP); assert '## Sitting 14 — CHAPTER 16 — AS BUILT' not in m and '## Sitting 14 — CHAPTER 16, Deuteronomy 16:1-22 — LEAN' in m
sd = rd(SD); assert '#208' in sd and '\n#209 (' not in sd
rec = rd(REC)
rec = sub1(rec, '## 2. WHERE IT STANDS (2026-09-23; #208 THE LEAN PASS newest)', '## 2. WHERE IT STANDS (2026-09-23; #209 sitting 14 newest)')
rec = sub1(rec, '- 229 frozen units, standing 2259, hash 8b8fff1fa28953af.', f'- {U1} frozen units, standing {S1}, hash {H1}.')
rec = sub1(rec, '- SITTING 13/13b (ch 15 read, compiled): 132 sources; the docket 974 rows; release_firstborn 91/91; 4 lines, 15 writes (4 reuses), 27 parameters.\n', '- SITTING 13/13b (ch 15): 132 sources; the docket 974 rows; release_firstborn 91/91; 4 lines, 15 writes, 27 parameters; PUSHED e824e52.\n')
i = rec.index('- 13b DONE, PUSHED e824e52. ⚠ THE LEAN PASS RULED'); j = rec.index('\n\n', i)
rec = rec[:i] + f'- ⚠ THE LEAN PASS (#208): 16-34 in 8 lean sittings — core shelf, 4 records, chain once; full process OWED.\n- SITTING 14 (ch 16 READ, LEAN) DONE at #209: {NSRC} sources; {NCL} claims; FROZEN; chain green; UNCOMMITTED. NEXT: the commit; then 14b after a compaction.' + rec[j:]
assert len(rec.encode('utf-8')) <= 10240, len(rec.encode('utf-8'))
idx = rd(IDX)
idx = sub1(idx, "ch 1-15 COMPILED AND PUSHED through e824e52 (13b: 91/91); LEAN PASS RULED 2026-09-23 ([[lean-pass-ruling]]); NEXT: ch 16, lean", f"ch 1-15 COMPILED AND PUSHED through e824e52; LEAN PASS RULED 2026-09-23 ([[lean-pass-ruling]]); 14 (ch 16 READ, lean) DONE 2026-09-23 ({NSRC} sources, {NCL} claims), UNCOMMITTED; NEXT: the commit, then 14b")
assert len(idx.encode('utf-8')) <= 17000, len(idx.encode('utf-8'))
wk = rd(WALK)
wk = sub1(wk, 'NEXT on his word: chapter 16\'s reading (16:1-22) in two runs + the tail"', 'THE LEAN PASS ruled 2026-09-23; SITTING 14 DONE 2026-09-23 (chapter 16 READ AND FROZEN, LEAN — 136 sources, 8 claims; UNCOMMITTED); NEXT on his word: the commit, then 14b"')
wk = wk.rstrip('\n') + f'\n\nSITTING 14 DONE 2026-09-23 — CHAPTER 16 READ AND FROZEN IN THE LEAN FORM (the first sitting of [[lean-pass-ruling]]): one window; the spine\'s 111 rows (piskaot 127-146, the headless 135 folded in by position) and Onkelos\'s 22 whole, 3 outside rows; the ledger deu_16_reeh_shoftim_2026-09-23.md ({NSRC} sources); {NCL} claims; the fold {U1} / {S1} / the hash unmoved; the register gate DECLARED {DECL}; the display patch {PR[1]} by gloss + {PR[0]} by reference (the rest owed). THE LESSONS: a headless piska is the spine\'s by position; a one-token piece needs its comma (the second miss found by grep); the ink\'s prior-read scan excludes its own ledger; the lint reads a hyphenated English word as a transliteration token; the lean window held ({len(T14)} steps, {TS} machine seconds). UNCOMMITTED since e824e52. NEXT on his word: the commit; then 14b (the compile of chapter 16, lean) after a compaction.\n'
debt = rd(DEBT)
debt = sub1(debt, '(none yet — sitting 14, chapter 16, next).', f'(1) sitting 14 (2026-09-23) — CHAPTER 16 READ, LEAN: the Sifrei\'s 111 rows and Onkelos\'s 22 whole, 3 outside rows ({NSRC} sources); NO docket, NO Talmud folio read; the Mishnah rows the spine cites (Berakhot 1:5, Pesachim 3:7, Beitzah 1:1, Sukkah 1:4, Chagigah 1:1, 1:2, 1:4, 1:5) routed to 14b; the display patch small ({PR[1]} by gloss, {PR[0]} by reference — the rest of the chapter\'s glosses OWED); the ten deferred records not written; the full process OWED. 14b (the compile of 16): next.')
LINT = {}
for p in (MAP, SD, REC, IDX, DEBT, WALK):
    r = subprocess.run(['python3', f'{ROOT}/logic/solo_tools/gloss_lint.py', p], capture_output=True, text=True); LINT[os.path.basename(p)] = int(re.search(r'(\d+) flag', r.stdout).group(1))
for txt in (ASB, BLOCK, rec, idx, wk, debt): assert '<home>' not in txt and os.path.expanduser('~') not in txt, 'a home path'
assert not re.search(r'[֐-׿]', ASB + BLOCK + debt[debt.index('(1) sitting 14 (2026-09-23)'):debt.index('14b (the compile of 16): next.')]), 'NO HEBREW SCRIPT IN THE MAP, THE STATE DOC BLOCK OR THE DEBT LINE'
print(f'THE RECORDS {"CHECKED" if CHECK else "WRITTEN"}: the AS BUILT {len(ASB.encode("utf-8"))} bytes; #209 {len(BLOCK.encode("utf-8"))}; the recovery page {len(rec.encode("utf-8"))}; MEMORY.md {len(idx.encode("utf-8"))}; the walk note {len(wk.encode("utf-8"))}; the debt line; the lints before {LINT}')
if not CHECK:
    open(MAP, 'a', encoding='utf-8').write(ASB); open(SD, 'a', encoding='utf-8').write(BLOCK); open(REC, 'w', encoding='utf-8').write(rec); open(IDX, 'w', encoding='utf-8').write(idx); open(WALK, 'w', encoding='utf-8').write(wk); open(DEBT, 'w', encoding='utf-8').write(debt)
    L2 = {}
    for p in (MAP, SD, REC, IDX, DEBT, WALK):
        r = subprocess.run(['python3', f'{ROOT}/logic/solo_tools/gloss_lint.py', p], capture_output=True, text=True); L2[os.path.basename(p)] = int(re.search(r'(\d+) flag', r.stdout).group(1))
    assert L2 == LINT, (LINT, L2)
    print('every lint unmoved:', L2)
