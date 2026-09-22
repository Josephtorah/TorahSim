import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE DEUTERONOMY WALK sitting 11b — THE COMPILE OF CHAPTER 13: THE CLEAN COMPACTION POINT at the close of RUN A (the design in the map) — the state doc's #203
# block appended, the recovery page's section 2 edited under its cap, the memory index line edited under its cap; every text built whole before a file is
# opened; sizes asserted. write_ch13_cleanpoint.py's form.
import os, re, subprocess
ROOT = _ROOT
SP = os.path.dirname(os.path.abspath(__file__))
HOME = os.path.expanduser('~')
MEM = f'{HOME}/.claude/projects/-Users-Shared-TorahSim/memory'
rows = [l.rstrip('\n').split('\t') for l in open(f'{SP}/ch13_timing.tsv', encoding='utf-8') if l.strip()]
T11B = '; '.join(f'{name} {secs}s (at {hhmm}, rc {rc})' for hhmm, name, secs, rc in rows if name.startswith('11b'))
D = f'{ROOT}/logic/pre_logic_methods_2026-07-28/PROMPT_continue_solo_era_2026-08-06.md'
s = open(D, encoding='utf-8').read()
assert '#202 ADDENDUM 1 — THE ONE SLIP AT THE RECORDS' in s
DONE = 'COMPACTION POINT #203' in s   # never twice
BLOCK = ('═══ COMPACTION POINT #203 (2026-09-21 — THE COMPILE OF CHAPTER 13, sitting 11b of THE DEUTERONOMY WALK: RUN A CLOSED, on the owner\'s "Go" after sitting 11\'s tail; his check "Did you reread first" answered — THE_STEPS\' compiler block whole, Step 2\'s head and Step 5\'s head read BEFORE any derive, the 10b design and AS BUILT read as the form). '
 'THE STATE: sitting 11 UNCOMMITTED since 2b0c9c8 (the commit on his word — ONE message at <scratch>/commit_msg_ch13.txt; 11b\'s records will extend it). RUN A AS RUN (the timing rows in the scratchpad\'s ch13_timing.tsv, the sitting\'s table continued — ' + T11B + '): '
 'THE MEASUREMENTS — ch13_compile_recon.py derived from 10b\'s by asserted line-based block substitutions (derive_ch13_recon.py; its own guard caught the one header line not retyped — section (7)\'s — and the derive was patched once): THE HEADER\'S TWIN IS A CELL (obey_horeb.the_exhortation, 4:2) with adding_barred ON FILE ONCE on israel_people (CC3 a COUNT literal — moves ONE -> TWO at the reuse), cleaving_commanded ON FILE ONCE (10:20 — the four verbs; 13:5\'s six a second entry), pity_barred ON FILE ONCE (7:16 — the nations; 13:9\'s inciter a second entry), THE STONING\'S RITE ALREADY A CELL (mekoshesh.capital_procedure — the stones and the stone), the four deaths\' census a cell (sanctions.census; NO effect named strangled — put_to_death carries the mode), the ban\'s first seat a cell (ordinances.capital — Exod 22:19; destroyed the effect), the court\'s rule a cell (ordinances.courts), the five prohibitions\' duties cells (holiness.conduct, ordinances.courts), the cloud\'s line on the tape (cloud_lifted Num 10:11 — 85:1\'s run citation), the calf\'s (calf_made Exod 32:4), the testing\'s (tested Gen 22:1), the stonings\' (stoned_as_commanded Lev 24:23, Num 15:36), Hormah\'s (Num 21:3), Peor\'s anger (hanging_commanded Num 25:4); the registry\'s homographs (the_heap Laban\'s, ahuzzath Abimelech\'s friend, the_cities_around_shechem; purge_commanded Jacob\'s, purge_deadline the leaven\'s); no seat, edge or pointer naming Deut 13; the D series DD -> DE next; RUN (1323, 96, 88, 0, 12, 1626, 43, 319, the four pairs, 127), 72 daemons, kinds 1150 / effects 1049, the seven planned effect names asserted absent; '
 'ch13_docket_scan.py derived from 10b\'s (derive_ch13_docket_scan.py — the English numbering\'s 12:32 folded to 13:1; its first launch fell on a chapter past an export\'s end — Tosefta Zevachim holds five — guarded; the second run 135 s): 91 LINK rows in 31 works, 463 TOPIC rows, twelve whole-chapter rows (Tosefta Sanhedrin 11, 12, 14; the Sifrei on Numbers 103, 113, 114; Tosefta Bava Kamma 9 EMPTY), 566 addresses, 196 CREDITED by address (chapter 4\'s docket 83 — Sanhedrin 88b and Rosh Hashanah 28b whole; chapter 7\'s 32 …) — some 370 to read whole: ONE DOCKET RUN under the ~700 clause; '
 'THE DESIGN in the map ("Sitting 11b — THE COMPILE OF CHAPTER 13 … THE DESIGN", 59,677 bytes, lint 0): cold_run_seducers.py the 68th runner, law_seducers the 73rd daemon (given_at Deut 13:1, installed_by boot; seven wrapped); FOUR OWN-DAY LINES, NO MARKER (word_sealed 13:1, prophet_test_declared 13:2-6, inciter_law_declared 13:7-12, condemned_city_law_declared 13:13-19) and EIGHT WRITES at the statutes — five new (false_prophet_hearing_barred, devoted_thing_cleaving_barred — block; tested_by_the_lord, israel_hears_and_fears, condemned_city_inquiry_required — status) and THREE REUSES (adding_barred, cleaving_commanded, pity_barred — second entries on israel_people); the case\'s writes evil_purged_from_the_midst (THE PURGE FORMULA\'S FIRST SEAT OF NINE — a body effect named at 13:6, reused ahead) and city_devoted (destroy) beside stoned / put_to_death (the prophet\'s mode a PARAMETER — the Sifrei\'s stoning, Mishnah Sanhedrin 11:1\'s strangling); four PARAMETERS (the_signs_status, the_prophets_death, the_execution_timing, the_inquiries); the readback nineteen T4 rows by CALL and eleven T1 rows by kind, no marker, no state row; RUN predicted (1327, 96, 88, 0, 12, 1634, 44, 319, the four pairs, 127); DE1-DE9; Q34-Q36; nineteen CALL edges predicted; the pointer at 13:18 ("as He swore") if the census demands; the homographs FALSE if matched. '
 'NOT COMMITTED (since 2b0c9c8): sitting 11 whole, the design, this block, the recovery page\'s and the memory\'s lines. NOTHING MID-FLIGHT — A CLEAN COMPACTION POINT. '
 'NEXT ON HIS WORD (after a compaction: "Reread", then "Go"): THE DOCKET IN ONE RUN — the dump ch13_docket_dump.txt (1,700 lines; the 196 credited addresses marked), the carry (ch12_credit_carry.py derived — the credited rows with their ledgers\' own verdict lines), the some 370 uncredited rows read whole in chunk files (the cap 64,000 bytes), the parts (ch12_docket_A.py\'s form; SPEC = CREDITED_SPEC + OWN), the writer (write_ch12_docket.py derived; the fourteen ranges asserted against the scan\'s print), the docket\'s records (COMPILE_DEBT\'s box (l), MIDDOT with every code checked before typed, MISHNAH_TOPICS, the state doc\'s checkpoint), its clean point; then RUN B (the probes Q34-Q36 to FAIL first; the types; the callees\' print; the runner in parts; the recorder with the cache off; the stitcher; DE1-DE9; the tape; the chain LAUNCHED); then THE TAIL. '
 'POST-COMPACTION REREADS: the recovery page, the map\'s "Sitting 11b — THE COMPILE OF CHAPTER 13 … THE DESIGN" (the newest section), MEMORY.md.\n')
assert not re.search(r'/Users/(?!Shared/)', BLOCK) and HOME not in BLOCK
if not DONE: open(D, 'a', encoding='utf-8').write('\n' + BLOCK)
# 2. THE RECOVERY PAGE — section 2 under its cap (10,240; 10,235 now — the lines trimmed)
P = f'{ROOT}/logic/pre_logic_methods_2026-07-28/RECOVERY_new_thread_2026-09-12.md'
t = open(P, encoding='utf-8').read()
old1 = '## 2. WHERE IT STANDS (2026-09-21, after sitting 11; the state doc #202 addendum 1 the newest)'
new1 = '## 2. WHERE IT STANDS (2026-09-21, 11b RUN A closed; the state doc #203 the newest)'
old2 = ('- SITTING 11 (ch 13, one run + the tail, EVERY STEP TIMED; the run past the cap by /context): the seducers\' one formula at three\n'
        '  cases; the header\'s twin 4:2; the purge\'s first seat; 122 sources whole; piska 96:9-12 are 14:1\'s (chapter 14 splits it).\n'
        '- UNCOMMITTED since 2b0c9c8: sitting 11 (<scratch>/commit_msg_ch13.txt). NEXT ON HIS WORD: the commit; then 11b.')
new2 = ('- SITTING 11 (ch 13 read and frozen, timed; past the cap): the seducers\' one formula; the header\'s twin 4:2; the purge\'s\n'
        '  first seat; piska 96:9-12 are 14:1\'s. 11b RUN A CLOSED — the design in the map (4 lines, 8 writes, 3 reuses).\n'
        '- UNCOMMITTED since 2b0c9c8: sitting 11 + the design. NEXT ON HIS WORD: THE DOCKET, one run (566 addresses, 196 credited); RUN B.')
old3 = 'the newest instances: the map\'s "Sitting 11" and "Sitting 10b")'
new3 = 'the newest instances: the map\'s "Sitting 11b" and "Sitting 11")'
for a, b in ((old1, new1), (old2, new2), (old3, new3)):
    assert t.count(a) == 1, a[:60]; t = t.replace(a, b)
assert len(t.encode()) <= 10240, len(t.encode())
open(P, 'w', encoding='utf-8').write(t)
# 3. THE MEMORY INDEX LINE — under 17,000 bytes
M = f'{MEM}/MEMORY.md'
m = open(M, encoding='utf-8').read()
oldm = 'ch 1-12 COMPILED, PUSHED 2b0c9c8; ch 13 READ AND FROZEN (sitting 11, one run + the tail, timed; uncommitted); NEXT: the commit, then 11b'
newm = 'ch 1-12 COMPILED, PUSHED 2b0c9c8; ch 13 READ AND FROZEN (sitting 11, uncommitted); 11b RUN A CLOSED (the design in the map); NEXT: the docket, one run'
assert m.count(oldm) == 1; m = m.replace(oldm, newm)
assert len(m.encode()) < 17000, len(m.encode())
open(M, 'w', encoding='utf-8').write(m)
print('the clean point written: the state doc #203', 'appended' if not DONE else 'already there', len(BLOCK.encode()), 'bytes | the recovery page', len(t.encode()), 'bytes | MEMORY.md', len(m.encode()), 'bytes')
