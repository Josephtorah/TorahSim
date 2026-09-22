import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE DEUTERONOMY WALK sitting 12b — THE COMPILE OF CHAPTER 14: THE CLEAN COMPACTION POINT at the close of RUN A (the design in the map) — the state doc's #205
# block appended, the recovery page's section 2 edited under its cap, the memory index line edited under its cap; every text built whole before a file is
# opened; sizes asserted. write_ch13b_cleanpoint.py's form. RUN FROM THE REPO ROOT.
import os, re, subprocess
ROOT = _ROOT
SP = os.path.dirname(os.path.abspath(__file__))
HOME = os.path.expanduser('~')
MEM = f'{HOME}/.claude/projects/-Users-Shared-TorahSim/memory'
rows = [l.rstrip('\n').split('\t') for l in open(f'{SP}/ch14b_timing.tsv', encoding='utf-8') if l.strip()]
T12B = '; '.join(f'{name} {secs}s (at {hhmm}, rc {rc})' for hhmm, name, secs, rc in rows if name.startswith('12b'))
assert T12B.count(';') >= 5, T12B
D = f'{ROOT}/logic/pre_logic_methods_2026-07-28/PROMPT_continue_solo_era_2026-08-06.md'
s = open(D, encoding='utf-8').read()
assert '#204 ADDENDUM 1 — NOTE' in s
DONE = 'COMPACTION POINT #205' in s   # never twice
BLOCK = ('═══ COMPACTION POINT #205 (2026-09-21 — THE COMPILE OF CHAPTER 14, sitting 12b of THE DEUTERONOMY WALK: RUN A CLOSED, on the owner\'s "Go" after sitting 12\'s tail, his "/context" read 365.5k mid-run before the design; the rereads THE_STEPS\' compiler block whole, Step 2\'s head and Step 5\'s head, the sitting-12 AS BUILT and the 12b box (a)-(o), the 11b design and AS BUILT as the form — read BEFORE any derive). '
 'THE STATE: sittings 11b and 12 UNCOMMITTED since fb797a1 (the commit on his word — ONE message at <scratch>/commit_msg_ch14.txt; 12b\'s records will extend it). RUN A AS RUN (the timing rows in the scratchpad\'s ch14b_timing.tsv — ' + T12B + '): '
 'THE MEASUREMENTS — ch14_compile_recon.py derived from 11b\'s by asserted line-based block substitutions (derive_ch14_recon.py; the forms folder\'s copy with its portable header stripped, ROOT from git restored; 18 s; 535 KB read by its seven sections): THE TWIN CHAPTER IS A CLASSIFIER (shemini.classify — the four its own exception rows; the bird blacklist by name), THE CARCASS\'S BAN NAMED AT 14:21 BY THE LEVITICUS RUNNER ITSELF (sanctions.carcass\'s lashed cell: "the ban is Deut 14:21 / Exod 22:30"), THE KID\'S THREE READINGS ALREADY ONE CELL (calendar.kid_in_milk — cook, eat, benefit; the three seats machine-verified there), THE POOR TITHE POINTED AT 14:28 FROM LEVITICUS 19 (holiness.gifts\' import table), rejoicing_before_the_lord_commanded and levite_forsaking_barred ON FILE ONCE each (12:7, 12:19 — the two reuses; DD2, DD4 and Q32\'s tuple the stale literals), treasured_people ONE UNMOVED, tithe_granted ONE on the Levites UNMOVED; RUN (1327, 96, 88, 0, 12, 1634, 44, 319, the four pairs, 127), CENSUS (2520, 1319, 1327, 1185, 6, 10, 9, 0, 71, 172, 131, 15, 26, 872, 272), markers 172, the D series at DE — the next DF, 73 daemons, kinds 1155, effects 1056, 68 spans, 669 edges, 208 pointers (none naming Deut 14; ONE edge names 14:1 already — priesthood -> holiness_b, the baldness analogy both ways), NO register seat at Deut 14, the probes Q1-Q36 (the next Q37); '
 'ch14_docket_scan.py derived from 11b\'s (derive_ch14_docket_scan.py — chapter 13\'s folded line removed; the first derive fell on the header block\'s suffix, retyped; 241 s): 144 LINK rows in 38 works (14:21 the most cited — 32 rows; 14:9 and 14:14-18 cited by no one), 817 TOPIC rows (eighteen folio ranges — Chullin 59a-66b 178, 113a-116b 135 and the rest; the ninety Mishnah rows — Maaser Sheni 1-5 whole, Bekhorot 9 whole), Tosefta Peah 4 (20 rows) and Kilayim 1 (11), Tosefta Sanhedrin 3 EMPTY in the export, 992 addresses, 288 CREDITED by address (chapter 12\'s docket 157 — Chullin 113a-116b 118 of 135 carried; the Korach docket 28; the Exodus triage 27; chapter 10\'s 21 …) — some 700 to read whole: TWO DOCKET RUNS by the ~700 clause, the clean point after the first half UNCONDITIONALLY (sitting 12\'s lesson 1); '
 'THE DESIGN in the map ("Sitting 12b — THE COMPILE OF CHAPTER 14 … THE DESIGN", 57,366 bytes, lint 0; two step-times typed from memory (40 s, 141 s) CORRECTED to the timer\'s rows (18 s, 241 s) before this block — a number is read from its print, never typed): cold_run_food_tithe.py the 69th runner, law_food_tithe the 74th daemon (given_at Deut 14:1, installed_by boot; EIGHT WRAPPED — seven cells F1-F7 and the_readback); FIVE OWN-DAY LINES, NO MARKER (sons_and_mourning_declared 14:1-2, food_law_declared 14:3-20, carcass_and_kid_declared 14:21, second_tithe_declared 14:22-27, third_year_tithe_declared 14:28-29) and SEVEN WRITES at the statutes — five new (cuttings_for_the_dead_barred, abomination_eating_barred, carcass_eating_barred — block; second_tithe_owed, poor_tithe_owed — status) and TWO REUSES (rejoicing_before_the_lord_commanded, levite_forsaking_barred — second entries on israel_people); FIVE PARAMETERS (the_birds_signs FROM THE ANSWER SHEET — Mishnah Chullin 3:6, the code/data separation law\'s own case; the_carcass_table — the Sages / R. Judah; the_moneys_form — two arms; the_removal_date and the_tithes_new_year — CLOCK DATA, the years read from the cycle by CALL); THE KID NO NEW WRITE (the case kind and the cell on file — the third seat\'s gain the assignment of the three readings); THE SOJOURNER TWO PERSONS BY SEAT (the resident alien at 14:21, the convert at 14:29 — no parameter); RUN predicted (1332, 96, 88, 0, 12, 1641, 45, 319, the four pairs, 127), PREVIOUS_RUN 11b\'s exactly, kinds 1155 -> 1161, effects 1056 -> 1061, I5 73 -> 74, EIGHTEEN CALL edges predicted (the census decides), NO pointer, DECLARED 98 unmoved; the checkpoints DF1-DF9; the probes Q37-Q39 to FAIL first. '
 'NOT COMMITTED (since fb797a1): sittings 11b and 12 whole, the design, this block, the recovery page\'s and the memory\'s lines. NOTHING MID-FLIGHT — A CLEAN COMPACTION POINT. '
 'NEXT ON HIS WORD (after a compaction: "Reread", then "Go"): THE DOCKET D1 — the dump ch14_docket_dump.txt (2,978 lines; the 288 credited addresses marked): the 144 link rows, Chullin 59a-66b and the ninety Mishnah rows (412 addresses), the carry (ch13_credit_carry.py derived — the credited rows with their ledgers\' own verdict lines), the uncredited rows read whole in chunk files (the cap 64,000 bytes), the parts (ch13_docket_A.py\'s form; ch13_docket_U.py ONE SHARED FILE for the unresolved rows), the verdicts on disk, its clean point; then D2 (the seventeen other ranges and the two Tosefta chapters — 580 addresses), the writer (write_ch13_docket.py derived; the eighteen ranges asserted against the scan\'s print), the docket\'s records (COMPILE_DEBT\'s box (o), MIDDOT with every code checked before typed, MISHNAH_TOPICS, the state doc\'s checkpoint), its clean point; then RUN B (the probes Q37-Q39 to FAIL first; the types; the callees\' print; the runner in parts; the recorder with the cache off; the stitcher; DF1-DF9; the tape; the chain LAUNCHED); then THE TAIL. '
 'POST-COMPACTION REREADS: the recovery page, the map\'s "Sitting 12b — THE COMPILE OF CHAPTER 14 … THE DESIGN" (the newest section), MEMORY.md.\n')
assert not re.search(r'/Users/(?!Shared/)', BLOCK) and HOME not in BLOCK and not re.search(r'[֐-׿]', BLOCK)
if not DONE: open(D, 'a', encoding='utf-8').write('\n' + BLOCK)
# 2. THE RECOVERY PAGE — section 2 under its cap (10,240; 10,231 now)
P = f'{ROOT}/logic/pre_logic_methods_2026-07-28/RECOVERY_new_thread_2026-09-12.md'
t = open(P, encoding='utf-8').read()
old1 = '## 2. WHERE IT STANDS (2026-09-21, after sitting 12; the state doc #204 addendum 1 the newest)'
new1 = '## 2. WHERE IT STANDS (2026-09-21, 12b RUN A closed; the state doc #205 the newest)'
old2 = ("- SITTING 12 (ch 14; TIMED; THE CAP PASSED BY /context A SECOND TIME — A READING IS TWO RUNS + THE TAIL NOW): the twin chapter\n"
        "  diffed; the birds' signs the answer sheet's; 143 sources whole; 7 claims seated.\n"
        "- UNCOMMITTED since fb797a1 (NOT PUSHED): 13's compile and 14 (<scratch>/commit_msg_ch14.txt carries both). NEXT ON HIS\n"
        "  WORD: the commit; then 12b.")
new2 = ("- SITTING 12 (ch 14 read and frozen; past the cap — A READING IS TWO RUNS + THE TAIL): 143 sources; 7 claims. 12b RUN A\n"
        "  CLOSED — the design in the map (5 lines, 7 writes, 2 reuses, 5 parameters; the docket TWO RUNS).\n"
        "- UNCOMMITTED since fb797a1: 13's compile, 14, the design. NEXT ON HIS WORD: the docket D1 (the link rows, Chullin\n"
        "  59a-66b, the Mishnah rows), D2, RUN B.")
old3 = 'the newest instances: the map\'s "Sitting 12" and "Sitting 11b")'
new3 = 'the newest instances: the map\'s "Sitting 12b" and "Sitting 12")'
for a, b in ((old1, new1), (old2, new2), (old3, new3)):
    assert t.count(a) == 1, a[:60]; t = t.replace(a, b)
assert len(t.encode()) <= 10240, len(t.encode())
open(P, 'w', encoding='utf-8').write(t)
# 3. THE MEMORY INDEX LINE — under 17,000 bytes
M = f'{MEM}/MEMORY.md'
m = open(M, encoding='utf-8').read()
oldm = 'ch 1-13 COMPILED (PUSHED through 2b0c9c8); 14 READ AND FROZEN (sitting 12; A READING IS TWO RUNS + THE TAIL now); 13b + 14 uncommitted; NEXT: the commit, then 12b'
newm = 'ch 1-13 COMPILED (PUSHED through 2b0c9c8); 14 READ AND FROZEN (12); 12b RUN A CLOSED (the design in the map; the docket TWO runs); 13b + 14 uncommitted; NEXT: the docket D1'
assert m.count(oldm) == 1; m = m.replace(oldm, newm)
assert len(m.encode()) < 17000, len(m.encode())
open(M, 'w', encoding='utf-8').write(m)
print('the clean point written: the state doc #205', 'appended' if not DONE else 'already there', len(BLOCK.encode()), 'bytes | the recovery page', len(t.encode()), 'bytes | MEMORY.md', len(m.encode()), 'bytes')
