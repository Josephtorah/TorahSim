#!/usr/bin/env python3
# THE DEUTERONOMY WALK sitting 13b — THE COMPILE OF CHAPTER 15: THE CLEAN COMPACTION POINT at the close of RUN A (the design in the map) — the state doc's #207
# block appended (#206's form), the recovery page's section 2 edited under its cap, the memory index line edited under its cap, the walk note appended; every
# text built whole before a file is opened; sizes asserted. write_ch14b_cleanpoint.py's form. RUN FROM THE REPO ROOT.
import os, re, subprocess
ROOT = subprocess.check_output(['git', 'rev-parse', '--show-toplevel'], text=True).strip()
SP = os.path.dirname(os.path.abspath(__file__))
HOME = os.path.expanduser('~')
MEM = f'{HOME}/.claude/projects/-Users-Shared-TorahSim/memory'
rows = [l.rstrip('\n').split('\t') for l in open(f'{SP}/ch15b_timing.tsv', encoding='utf-8') if l.strip()]
T13B = '; '.join(f'{name} {secs}s (at {hhmm}, rc {rc})' for hhmm, name, secs, rc in rows if name.startswith('13b'))
assert T13B.count(';') >= 5, T13B
MAP = open(f'{ROOT}/World/step9/DEUTERONOMY_WALK.md', encoding='utf-8').read()
i = MAP.index('## Sitting 13b — THE COMPILE OF CHAPTER 15'); DESIGN_BYTES = len(MAP[i:].encode())
D = f'{ROOT}/logic/pre_logic_methods_2026-07-28/PROMPT_continue_solo_era_2026-08-06.md'
s = open(D, encoding='utf-8').read()
assert '#206 ADDENDUM 3 — THE COMMIT NOTE' in s
DONE = '\n#207 (' in s   # never twice
BLOCK = ('#207 (2026-09-22, THE DEUTERONOMY WALK sitting 13b — THE COMPILE OF CHAPTER 15, TWO RUNS + THE TAIL under THE COST RULES with THE DOCKET ITS OWN TWO RUNS by the ~700 clause; on the owner\'s "Go" after sitting 13\'s commit b0eaa56; A CLEAN COMPACTION POINT AT RUN A\'s END — the rereads, the measurements and the design done, NO DOCKET ROW TYPED): '
 'THE STATE: chapter 15 read, frozen and COMMITTED b0eaa56 (not pushed; the commit\'s records ride 13b\'s commit). RUN A AS RUN (the timing rows in the scratchpad\'s ch15b_timing.tsv — ' + T13B + '): '
 'THE REREADS — the recovery page, the map\'s "Sitting 13 — CHAPTER 15 — AS BUILT", MEMORY.md, #206 addendum 3 with its NOTE and the commit note; THE_STEPS\' compiler block whole, Step 2 whole and Step 5\'s head; COMPILE_DEBT\'s 13b box (a)-(o); the 12b design\'s opening, its checkpoints and its order as the compile\'s form (the persisted design writer read in three cuts). '
 'THE MEASUREMENTS — ch15_compile_recon.py TYPED in two parts on 12b\'s form (663,317 bytes; read by a digest of 316,692 — sections 1 and 3-7 whole, section 2 cut to the kin\'s nineteen modules; nine Read pages): THE JUBILEE ENGINE ALREADY ROUTES THE MONEY RELEASE HERE (cold_run_yovel.py\'s cell debt_release = routed_deut_15; its "release ON THE ACT" from Rosh Hashanah 9b), THE SLAVE\'S TERM CLOCK IS EXODUS 21\'S (mishpatim\'s F1 with its IMPORT row "written even for the pierced forever"; mishpatim_3.maidservant\'s cell already citing Deut 15:12; the fire goes_free six years on), THE ORDINANCES\' LOAN CELL NAMES 15:8 (lending_is_obligation; the priority ladder on file), THE SEVERANCE GIFT PRICED IN erection.repeats (Kiddushin 17a — Deut 15:13), THE FIRSTLING\'S CELLS IN korach.the_gifts (sixty-one asks) with consecrated_firstborn "written at birth", temurah\'s probe list carrying 15:19 as its IMPORT against 27:26, priesthood.acceptable\'s closing rule "one list serves the firstling (Deut 15:21 [IMPORT])", place_name\'s blood and gates cells, sanctions\' blood and covering, holiness\' poor and wage, food_tithe\'s the_year_passed (106:5\'s cell on file); THE COUNTER at day 908865 (entities 319, log 3616), the tape\'s last lines chapter 14\'s five, its last marker Deut 10:12; RUN (1332, 96, 88, 0, 12, 1641, 45, 319, the four pairs, 127); markers 172 (108 / 49); events 110 / 1164 / 58; CENSUS (2520, 1319, 1332, 1185, 6, 10, 9, 0, 71, 172, 131, 15, 26, 877, 272); 69 spans, 74 daemons, 1161 kinds, 1061 effects; 689 edges, 208 pointers — NONE naming Deut 15; NO register seat at Deut 15; THE FINDER\'S FORMS READ (a receipt "commanded" 6680; a header "these" 428 + a footer noun) — 15:2 and 15:6 each outside by one token; the D series at DF — THE NEXT NAME DG; the readback probes Q1-Q39 — the next Q40; THE REGISTRY\'S HOMOGRAPHS to guard: the-servant (Abraham\'s), the-place (Bethel), the-flock; THE SABBATICAL COUNT: the count era\'s epoch in calendar_parameters.yaml, yovel.cycle the year\'s class, the world before the entry (law_yovel installed_by entered_the_land) — "no count" on the bare world, the date read through year_in at RUN B (the recon\'s render fell on the clock\'s date attribute — a measurement, not a defect). '
 'ch15_docket_scan.py derived from 12b\'s by asserted substitutions (derive_ch15_docket_scan.py; the box\'s (o) ranges and four Tosefta chapters sized): 118 LINK rows in 29 works (15:19 the most cited — 22; 15:15 cited by no one), 857 TOPIC rows (eleven folio ranges — Kiddushin 14b-22b 305, Bekhorot 33a-37b 189, 25a-28b 121, Gittin 36a-37b 64, Arakhin 32b-33a 39, Rosh Hashanah 8b-9a 20, Bava Metzia 71a 20, Ketubot 67b 18, Makkot 3b 17, Bekhorot 53b 17, Bava Metzia 31b 15; the forty-six Mishnah rows; Tosefta Sheviit 8, Kiddushin 1, Bekhorot 1-2 — 36 rows); 975 addresses, 249 CREDITED (deu_14\'s exam 75, EXOD_TALMUD 57, deu_12\'s exam 48, the priesthood docket 17, the korach exam 16 …; thirty-eight Mishnah rows among them); the dump 636,267 bytes. '
 'ch14_aramaic_nfkc.py (COMPILE_DEBT\'s (m)): ZERO presentation-form letters in the Onkelos export\'s 956 rows; 0 of ch14_ink.py\'s 27 onk_seats literals move under NFKC; 0 of 956 verses differ — CHAPTER 14\'S ARAMAIC COUNTS STAND, SITTING 13\'S LESSON 4 CORRECTED (the export is clean; the needy word\'s five seats found by the plain substring; the earlier miss on the typing side): the correction owed to 13b\'s AS BUILT, a CORRECTION row on the reading\'s ledger at the tail, the memory\'s walk note. '
 'THE DESIGN in the map ("Sitting 13b — THE COMPILE OF CHAPTER 15 … THE DESIGN", ' + str(DESIGN_BYTES) + ' bytes, lint 0): cold_run_release_firstborn.py the 70th runner, law_release_firstborn the 75th daemon (given_at Deut 15:1, installed_by boot); FOUR OWN-DAY LINES on (40, 11, 1), NO MARKER — release_law_declared (15:1-6), hand_opening_commanded (15:7-11), hebrew_slave_law_declared (15:12-18), firstling_law_declared (15:19-23); SEVEN CELLS on the seven claims\' spans and the readback table; THE RELEASE AN EFFECT ON THE DEBTS AT THE SEVENTH YEAR\'S END — debt_release_owed a STATUS with the date a CLOCK DATUM by call to the cycle, the onset and the territory PARAMETERS, the object loans only, THE PROZBUL A PARAMETER FROM THE ANSWER SHEET, exaction_barred the BLOCK; THE TWO VERSES 15:4 / 15:11 a STATE VARIABLE with two arms, blessings_for_hearing REUSED, THE POINTER ROW WITH ITS REFERENT AHEAD (15:6 -> 28:3) graded H; THE HAND OPENED — the ranks a PRECEDENCE PARAMETER (the ordinances\' ladder by call), the measure of need, the pledge dispute, base_thought_barred by the labeled transfer from 13:14, cry_heard and bears_sin REUSED, work_of_the_hand_blessed; THE HEBREW SLAVE — the three cases, the term by call to Exodus 21\'s clock, the exits\' two tables, furnishing_commanded and empty_sending_barred, severance_gift_owed the case\'s DEBIT priced by call, the memory row on the tape\'s close; THE AWL — the ear by the labeled transfer from the leper\'s, serves_for_ever with THE JUBILEE\'S OVERRIDE ON FILE, "likewise" the gift not the awl (the DISAGREES row against Exodus 21:7 OPEN), the double hire a dispute of two spines; THE FIRSTLING — consecrated_firstborn REUSED, "sanctify" for its value against 27:26 (the DISAGREES row resolved as DATA), the work and the shearing a BLOCK, THE FIRSTLING\'S YEAR A CLOCK DATUM with its two-day edge, the place by call, holy_things_in_the_gates_barred REUSED; THE BLEMISH the list by call to the priests\' table, THE BLOOD by call to chapter 12\'s cells and the sanctions\' ban — no new write; twelve new effects, twenty-seven parameters, five new kinds; twenty REFERENCE edges and TWO TRANSFER edges labeled with their teachers; DG1-DG9; Q40-Q42; the arithmetic (events +4, writes +W read from the print, daemons +1, markers 172 unmoved; the reuses\' counts read from the running world before the tape). '
 'NOT COMMITTED (since b0eaa56): the commit\'s own records, the design, this block, the recovery page\'s and the memory\'s lines, the forms\' timing table. NOTHING MID-FLIGHT — A CLEAN COMPACTION POINT. '
 'NEXT ON HIS WORD (after a compaction: "Reread", then "Go"): THE DOCKET D1 — THE SMALL WORKS: the dump ch15_docket_dump.txt (2,927 lines; the 249 credited addresses marked) — every address outside Kiddushin 14b-22b and Bekhorot 25a-28b (the link rows of the other twenty-seven works, the forty-six Mishnah rows, the four Tosefta chapters, Gittin 36a-37b, Arakhin 32b-33a, Makkot 3b, Rosh Hashanah 8b-9a, Bava Metzia 31b and 71a, Ketubot 67b, Bekhorot 33a-37b and 53b — some 575 addresses, the count computed from the dump), the carry (ch14_credit_carry.py derived — the credited rows with their ledgers\' own verdict lines), the uncredited read whole in chunk files (the cap 64,000), the parts on 12b\'s whole-row instruments, the writer derived from write_ch14_docket.py, the docket\'s records, its own clean point; then D2 — Kiddushin 14b-22b whole, THE CLEAN POINT after it UNCONDITIONALLY, Bekhorot 25a-28b whole; then RUN B. '
 'POST-COMPACTION REREADS: the recovery page, the map\'s "Sitting 13b — THE COMPILE OF CHAPTER 15 … THE DESIGN" (the newest section), MEMORY.md.\n')
assert not re.search(r'/Users/(?!Shared/)', BLOCK) and HOME not in BLOCK and not re.search(r'[֐-׿]', BLOCK)
if not DONE: open(D, 'a', encoding='utf-8').write('\n' + BLOCK)
# 2. THE RECOVERY PAGE — section 2 under its cap (10,240; 10,239 now)
P = f'{ROOT}/logic/pre_logic_methods_2026-07-28/RECOVERY_new_thread_2026-09-12.md'
t = open(P, encoding='utf-8').read()
old1 = "## 2. WHERE IT STANDS (2026-09-22, after sitting 13 and its commit; the state doc #206 addendum 3's commit note the newest)"
new1 = '## 2. WHERE IT STANDS (2026-09-22, 13b RUN A closed; the state doc #207 the newest)'
old2 = ("- SITTING 13 (ch 15; TWO RUNS + THE TAIL as ruled; TIMED): the one calendar; the two verses upheld by a condition; the prozbul\n"
        "  inside the spine; the receipt pointing forward; 132 sources whole; 7 claims seated; +168 / +44.\n"
        "- COMMITTED b0eaa56 (2026-09-22, no push; 1-14 pushed through 049f55c). NEXT ON HIS WORD: 13b.")
new2 = ("- SITTING 13 (ch 15 read and frozen; two runs + the tail): 132 sources; 7 claims. 13b RUN A CLOSED — the design in the map\n"
        "  (4 lines, 12 effects, 27 parameters; the docket TWO RUNS; the NFKC lesson corrected: the export is clean).\n"
        "- NEXT ON HIS WORD: the docket D1 (the small works), D2 (Kiddushin 14b-22b, Bekhorot 25a-28b), RUN B.")
old3 = 'the newest instances: the map\'s "Sitting 13" and "Sitting 12b")'
new3 = 'the newest instances: the map\'s "Sitting 13b" and "Sitting 13")'
for a, b in ((old1, new1), (old2, new2), (old3, new3)):
    assert t.count(a) == 1, a[:60]; t = t.replace(a, b)
assert len(t.encode()) <= 10240, len(t.encode())
open(P, 'w', encoding='utf-8').write(t)
# 3. THE MEMORY INDEX LINE — under 17,000 bytes
M = f'{MEM}/MEMORY.md'
m = open(M, encoding='utf-8').read()
oldm = '15 READ, FROZEN AND COMMITTED b0eaa56, NOT PUSHED (sitting 13 — two runs + the tail; 132/132; the 229th unit); NEXT: 13b'
newm = '15 READ AND FROZEN, COMMITTED b0eaa56 (13; not pushed); 13b RUN A CLOSED (the design; the docket TWO runs); NEXT: the docket D1'
assert m.count(oldm) == 1; m = m.replace(oldm, newm)
assert len(m.encode()) < 17000, len(m.encode())
open(M, 'w', encoding='utf-8').write(m)
# 4. THE WALK NOTE — appended
W = f'{MEM}/deuteronomy-walk.md'
w = open(W, encoding='utf-8').read(); assert w.endswith('\n')
NOTE = ('SITTING 13b RUN A DONE 2026-09-22 (on "Go" after the commit b0eaa56; the state doc #207): the rereads; the recon TYPED on 12b\'s form (the jubilee engine\'s cell\n'
        'routed_deut_15 already names the chapter; the term clock Exodus 21\'s; the severance gift priced in erection; the blemish table naming 15:21; no seat, no edge at\n'
        'Deut 15; DG next, Q40 next); the scan (975 addresses, 249 credited, 118 link in 29 works; 15:15 uncited); THE NFKC RE-MEASURE — 0 presentation forms in the\n'
        'export\'s 956 rows, chapter 14\'s counts STAND, sitting 13\'s lesson 4 CORRECTED (the miss was on the typing side); THE DESIGN in the map (four own-day lines, no\n'
        'marker; seven cells; the release an effect at the seventh year\'s end by the cycle by call, the prozbul a parameter, the needy\'s ranks a precedence parameter,\n'
        'the state variable 15:4/15:11, the pointer row with its referent ahead graded H, the slave\'s three cases and the exits\' tables, the severance gift\'s debit,\n'
        'serves_for_ever with the jubilee\'s override, the firstling\'s year a clock datum, "sanctify" for its value, the blemish list by call; twelve new effects,\n'
        'twenty-seven parameters; DG1-DG9; Q40-Q42; two transfer edges labeled — Belial\'s word and the leper\'s ear); THE DOCKET TWO RUNS (D1 the small works ~575, D2\n'
        'Kiddushin 14b-22b + Bekhorot 25a-28b ~456, the clean point between them unconditional). NEXT on "Reread" then "Go": D1.\n')
assert not re.search(r'[֐-׿]', NOTE) and HOME not in NOTE
open(W, 'a', encoding='utf-8').write(NOTE)
print('the clean point written: the state doc #207', 'appended' if not DONE else 'already there', len(BLOCK.encode()), 'bytes | the recovery page', len(t.encode()), 'bytes | MEMORY.md', len(m.encode()), 'bytes | the walk note +', len(NOTE.encode()))
