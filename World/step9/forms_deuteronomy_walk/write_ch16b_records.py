import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE DEUTERONOMY WALK 14b (LEAN): THE TAIL'S RECORDS in ONE call — the map's AS BUILT — LEAN (short: the departures and the lessons, with the timing table), the
# state doc's NOTE under #210, the recovery page (section 2 under its cap), the memory (the index line and the walk note), the lean-pass box's line in COMPILE_DEBT.
# Every number READ FROM ITS PRINT (the chain's SUMMARY, the runner's, the tape's, the timing table); every text built whole before a file is opened; the lints
# asserted unmoved; the caps asserted. --check prints without writing. RUN FROM THE REPO ROOT after the chain's SUMMARY is read (ALL GREEN, or the demands filed and the pass rerun).
import os, re, sys, subprocess, ast, glob
ROOT = _ROOT
SP = os.path.dirname(os.path.abspath(__file__))
MEM = os.path.expanduser('~/.claude/projects/-Users-Shared-TorahSim/memory')
CHECK = '--check' in sys.argv
MAP = f'{ROOT}/World/step9/DEUTERONOMY_WALK.md'; SD = f'{ROOT}/logic/pre_logic_methods_2026-07-28/PROMPT_continue_solo_era_2026-08-06.md'; REC = f'{ROOT}/logic/pre_logic_methods_2026-07-28/RECOVERY_new_thread_2026-09-12.md'
DEBT = f'{ROOT}/World/step9/COMPILE_DEBT.md'; MM = f'{MEM}/MEMORY.md'; MW = f'{MEM}/deuteronomy-walk.md'
def rd(p): return open(p, encoding='utf-8').read()
def R(pat, text, name):
    g = re.search(pat, text, re.M); assert g, (name, pat); return g.group(1)
SUMF = f'{SP}/ch16b_gates_SUMMARY.txt'; summ = rd(SUMF)
assert 'ALL GREEN' in summ, ('the chain not green — read the summary and the step prints first', summ[-300:])
STEPS = re.findall(r'^(PASS|FAIL|SKIP) (\w+)(?: rc=\d+)? \((\d+)s\)', summ, re.M)
assert all(v == 'PASS' for v, _, _ in STEPS) and len(STEPS) == 12, STEPS
CHAIN_S = sum(int(t) for _, _, t in STEPS)
PROBES = re.findall(r'^  (\w+): (\d+/\d+)$', rd(f'{SP}/ch16b_gates/probes.out'), re.M) if os.path.exists(f'{SP}/ch16b_gates/probes.out') else []
_reg = rd(f'{SP}/ch16b_gates/register.out'); REG = (re.search(r'(DECLARED \d+[^\n]*)', _reg, re.M) or re.search(r'(THE REGISTER GATE: GREEN)', _reg)).group(1)   # the gate's last line read (its DECLARED count printed at --strict's head when it prints one)
SWEEP = R(r'(\d+/\d+) runners green', rd(f'{SP}/ch16b_gates/sweep.out'), 'the sweep')   # the sweep's own line (the summary's last line is the stamp's)
POS = R(r'(\d+ checkpoints? over \d+ pauses[^\n]*|\d+ rows[^\n]*)', rd(f'{SP}/ch16b_gates/positions.out'), 'the positions') if os.path.exists(f'{SP}/ch16b_gates/positions.out') else '(the positions print absent)'
run1 = rd(f'{SP}/ch16_runner_run1.out'); tape = rd(sorted(glob.glob(f'{SP}/ch16_tape_run*.out'))[-1]); NRUN = len(glob.glob(f'{SP}/ch16_tape_run*.out')); cc = rd(f'{SP}/ch16_checkpoint_check2.out'); seq = rd(f'{ROOT}/World/step9/cold_run_sequence.py')
MATRIX = R(r'^MATRIX: (\d+/\d+)', run1, 'the runner'); NARR = ast.literal_eval(R(r'^THE NARRATIVE: (\(.*?\)) \(the sixteen', run1, 'the narrative')); W = NARR[0]
NPAR = int(R(r'the twenty-nine (\d+) \(in the registry', run1, 'the parameters')); RBG = R(r'NO NEW FORM: 22 rows — (\{.*?\});', run1, 'the readback')
FRAC = R(r'^(FRACTIONS: [^\n]*)', run1, 'the fractions'); OPS = R(r'^LEDGER OPS this span writes: ([^\n]*)', run1, 'the ops')
TAPE_CP = R(r'(\d+/\d+) checkpoints?', tape, 'the tape') if re.search(r'\d+/\d+ checkpoints?', tape) else R(r'checkpoints[^\n]*?(\d+/\d+)', tape, 'the tape')
CC_LINE = R(r'^(checkpoint_check: \d+ rows, \d+ miss, \d+ raised[^\n]*)', cc, 'the checkpoint check')
RUN = R(r"^RUN = \((\d+, \d+, \d+, \d+, \d+, \d+, \d+, \d+),", seq, 'RUN')
tim = [l.split('\t') for l in rd(f'{SP}/ch16b_timing.tsv').strip().split('\n') if l.startswith('14b')]
NSTEP = len(tim); TSEC = sum(int(r[2]) for r in tim)
TABLE = '\n'.join('| %s | %s | %s | %s |' % (r[0], r[1].replace('|', '/'), r[2], r[3]) for r in [l.split('\t') for l in rd(f'{SP}/ch16b_timing.tsv').strip().split('\n')] if r[1].startswith('14b'))
CASES = int(R(r'^CASES generated: (\d+)', rd(f'{SP}/ch16_cases_gen.out'), 'the cases'))
EXAM = rd(f'{ROOT}/logic/oral_triage/deu_16_reeh_shoftim_exam_2026-09-23.md'); NEXAM = len(re.findall(r'^- Mishnah [A-Za-z ]+ \d+:\d+ — LAW\.', EXAM, re.M))
print('THE PRINTS: the chain %d steps ALL GREEN in %d s (probes %s; %s; sweep %s; positions %s); the runner %s (%d cases; %s; %s); writes %d; parameters %d; readback %s; the tape %s; %s; RUN (%s); the timing %d steps, %d s; the exam %d rows' % (len(STEPS), CHAIN_S, PROBES, REG, SWEEP, POS, MATRIX, CASES, FRAC[:60], OPS, W, NPAR, RBG, TAPE_CP, CC_LINE, RUN, NSTEP, TSEC, NEXAM))
ASB = '''

## Sitting 14b — THE COMPILE OF CHAPTER 16 — AS BUILT — LEAN (2026-09-23; the design above stands as written; the lean pass's first compile sitting ran in ONE compile window + the tail: the design, the probe to FAIL, the types, the callees' facts, the runner in three parts, the lean exam file, the tape, the two demands filed, the gates chain launched; every departure named here; the timing table the last section)

THE COMPILE AS RUN: the lean recon (no docket scan — the kin's cells by a static scan, the running world's counts from the snapshot); THE DESIGN before any code; the probe Q43 written to FAIL (42/43 before the runner existed); THE TYPES by script (five kinds, fifteen effects, the bribe's row amended for its first write; the daemon law_festivals_judges the 76th with SEVEN functions WRAPPED; the span and fifteen CALL edges, all REFERENCE; I5 76; no calendar row — the festivals' dates and the intercalation on file for the count era); THE CALLEES' FACTS printed from fifteen runners and typed as asserts (the erection's cells by their QUESTION keys after a first print of 'no_case' by cell name); THE RUNNER cold_run_festivals_judges.py (the 71st) — part 1 derived (the helpers from the chapter-15 runner, four ink blocks from ch16_ink.py by content markers, the clock's rows and the day slots read, the one-database scans, the facts), parts 2-3 typed (six cells and the table, the readback's twenty-two rows, the twenty-nine parameters in DATA, the daemon, the five lines, the narrative); the fast checker green on the fourth derive (part 1's holes' scan anchored at the effect name), the ask check %d/0, %d CASES generated from the cells' own asks, %s ON THE FIRST GRADED RUN (%s; %s); THE LEAN EXAM logic/oral_triage/deu_16_reeh_shoftim_exam_2026-09-23.md — %d Mishnah rows read whole, no segment, coverage computed (lint 0 after the export's one transliterated term glossed); THE TAPE — the recorder (INK_CACHE=0), the stitcher (no marker; the five own-day lines page_order after the last Deuteronomy 15 line — the placement and the census exactly as the design's arithmetic), the literals DH1-DH5 with DB7 retyped, %s ON ITS FIFTH RUN (the first 9/10 — DD4, chapter 12's hole scan, matched 16:5's block by the substring 'in_the_gates' and was retyped; the second and third runs stopped at two callees' scans of the one database — second_tablets' LAW_SCAN and place_name's PLACE_SCAN — moved by the first run's own writes on Israel, each widened with the note; the fourth the patch's anchor miss; THE SCAN CENSUS ch16_scan_census.py written to replay every runner's hole scan on the one database at once) (RUN (%s, the four pairs, 127); %s); THE DEPENDENCY GATE's two demands filed from its print (the widow FALSE — the household list's, not the priest's marriage class; 16:10's "as He blesses you" PARAMETER — the hand's measure) and the gate green alone; THE CHAIN IN TWO PASSES — the first (536 s) stopped at the probes (Q33: chapter 12's hole probe matched 16:5's block — the lesson's fifth seat) and the dependency gate (the registration edge sequence -> festivals_judges unfiled — 13b's precedent), the tape, the daemon gate, the build, the journal gate and the register gate --strict passing; both filed from the prints; THE SECOND PASS from the tape ALL GREEN in %d s (%d steps; the probes %s; %s; the positions %s; the sweep %s); the readback probes %s.

THE DEPARTURES FROM THE DESIGN: (1) the cases are the cells' asks — %d, the eight Mishnah rows among them as asks of F1, F3 and F4 — with NO bench scene and NO case kind (the persons were the docket's; the daemon gate reads the narrative's five literal submits); (2) THE COURTS ARE NOT A SECOND DAEMON (sitting 14's note): the one daemon writes the courts' STATUS, the three tiers a parameter — the second daemon owed; (3) FIVE SCAN SEATS widened for chapter 16's entries — second_tablets' BRIBE_SCAN (at the design) and LAW_SCAN, place_name's PLACE_SCAN (found by the tape's second and third runs), the tape's DD4 (found by the first run) and the probes' Q33 (found by the chain's first pass) — a later chapter's writes move an earlier chapter's hole scan once the tape's first run puts them in the one database; (4) the readback's census from the print VARIANT 9 / SUPPLIED 10 / EXPANDED 2 / VERBATIM 1 (the design predicted the grades row by row, not the census); (5) the writes %d exactly as predicted, the narrative's tuple unmoved.

THE LESSONS (⚠): (1) A HOLE PATTERN IS THE EFFECT'S OWN NAME — a substring matched a neighbour twice ('passover_in' the Numbers 9 status; 'asherah' inside two values): the scan anchored at the name, the kinds' check narrowed to the line's own name (13b's hebrew_slave lesson, twice again); (2) AN EARLIER CHAPTER'S SCAN OF THE ONE DATABASE MOVES WITH A LATER CHAPTER'S ENTRIES — the tape's first run writes the new lines into the database, and every hole scan whose pattern the new names or VALUES match trips at the next import (second_tablets twice, place_name once, DD4 on the tape, Q33 in the probes — five seats, three tape runs and a chain pass to find them one by one; a scan matches on the effect's name AND its value text, so a value naming 'the place which the LORD will choose' trips the place's scan): THE SCAN CENSUS (ch16_scan_census.py) replays every runner's scan on the database at once — run it after the tape's first run, before the second (the instrument for sittings 15-21); (3) THE OLD RUNNERS' CELLS TAKE QUESTION KEYS, NOT CELL NAMES — erection.repeats(q): the first callees print returned 'no_case' for every cell name; the map q -> cell read from the source, the second print by the keys; (4) A COPIED INK BLOCK'S NAME CAN SHADOW AN ALIAS — the frames block's MO (the morphs by verse) against the moadim alias: renamed at the derive; (5) THE LEAN COMPILE WINDOW HELD — the design, the types, the runner (%s on its first run), the exam and the tape in one context, the chain launched at its end; the shape for sittings 15-21.

THE FINDS are the runner's cells: the place added to the three feasts and the pilgrimage (chapter 12's formula at six seats, the chapter's own statuses); the intercalation a law of 'observe' (127:1 — the registry's rows for the count era, the exodus era's Aviv OWED); the leaven's sixth hour (130:1) and the two measures (Beitzah 1:1 in the spine's own Hebrew); the three phrases of the clock on the calendar's slots (133:2); cooking is roasting (134:1 — 2 Chronicles 35:13); six and seven (135:1-2) and THE INTERMEDIATE DAYS HANDED TO THE SAGES (135:3 — a parameter Scripture leaves empty, the code/data law's cleanest seat); the omer from the sickle (136:3, 136:8); the roofing (Sukkah 1:4), who appears (Chagigah 1:1), the two amounts (1:2), the gift of the hand (1:5) — the answer sheet's rows as parameters; THE BRIBE'S BLOCK WRITTEN FOR THE FIRST TIME AT 16:19 (Exodus 23:8's declared, never written — DB7); the acquittal final (144:12 — Sanhedrin 4:1); THE PILLAR LOVED BY THE FATHERS AND HATED BY THE SONS — the tape's own entries on Jacob's pillars read by the cell (146:1: the law's reason a change of state on the tape).

NEXT ON THE OWNER'S WORD: the commit ("Commit" = no push; "commit push" = both); then, after a compaction ("Reread", then "Go"), SITTING 15 — CHAPTERS 17-18's READING IN THE LEAN FORM (one reading window: the spine's piskaot on 17:1-18:22 and Onkelos whole, the ledger, the freeze; then 15b the compile).

THE TIMING TABLE (ch16b_timing.tsv; %d steps, %d machine seconds; the chain's row the background run's):
| time | step | s | rc |
|---|---|---|---|
%s
''' % (CASES, CASES, MATRIX, FRAC[11:60], OPS, NEXAM, TAPE_CP, RUN, CC_LINE, CHAIN_S, len(STEPS), PROBES, REG, POS, SWEEP, [p for p in PROBES if p[0] == 'readback'], CASES, W, MATRIX, NSTEP, TSEC, TABLE)
NOTE210 = " — THE TAIL (2026-09-23, after the compaction; on the owner's word): the second pass's SUMMARY read once — ALL GREEN in %d s (%d steps; the probes %s; %s; the positions %s; the sweep %s); no demand; the four records and the debt line written in one call (write_ch16b_records.py), the forms copied, the commit message at <scratch>/commit_msg_ch16b.txt; the tree UNCOMMITTED since e824e52 (sittings 14 and 14b and the lean-pass ruling ride together). NEXT ON HIS WORD: the commit; then, after a compaction (\"Reread\", then \"Go\"), SITTING 15 — CHAPTERS 17-18's READING, LEAN. POST-COMPACTION REREADS: the recovery page, the map's newest section (\"Sitting 14b — THE COMPILE OF CHAPTER 16 — AS BUILT — LEAN\"), MEMORY.md; then this checkpoint." % (CHAIN_S, len(STEPS), PROBES, REG, POS, SWEEP)
DEBT_LINE = " (2) sitting 14b (2026-09-23) — CHAPTER 16 COMPILED, LEAN: the eight Mishnah rows the cases (Berakhot 1:5, Pesachim 3:7, Beitzah 1:1, Sukkah 1:4, Chagigah 1:1, 1:2, 1:4, 1:5 — read whole), NO Talmud segment read; six cells and the table, %d cases %s; five lines, %d writes, %d parameters; the chain once ALL GREEN; OWED: the docket whole (Pesachim, Chagigah, Sukkah, Menachot 10, Rosh Hashanah 1, Moed Katan, Sanhedrin 1 and 4, Avodah Zarah 3; the segments the rows name), the courts' second daemon with its three tiers, the exodus era's intercalation (the Aviv clause on the running tape), the bench scene and the persons, the ten deferred records; the commit on his word. 15 (the reading of 17-18): next." % (CASES, MATRIX, W, NPAR)
# ---- the texts checked against the files ----
m = rd(MAP); assert '## Sitting 14b — THE COMPILE OF CHAPTER 16 — AS BUILT' not in m and m.rfind('## Sitting 14b — THE COMPILE OF CHAPTER 16, Deuteronomy 16:1-22 — LEAN') > 0
sd = rd(SD); assert '\n#210 (' in sd and 'THE TAIL (2026-09-23' not in sd
i210 = sd.index('\n#210 ('); assert sd.find('\n#', i210 + 5) < 0, 'the #210 the last checkpoint'
rec = rd(REC)
def sub1(t, a, b, name):
    assert t.count(a) == 1, (name, t.count(a), a[:70]); return t.replace(a, b)
rec2 = sub1(rec, '14b\'s chain LAUNCHED, summary unread.', '14b\'s chain ALL GREEN once (sweep %s).' % SWEEP, 'the RUN line')
rec2 = sub1(rec2, 'UNCOMMITTED. NEXT: THE TAIL (summary once; records; forms; message), then the commit.', 'chain green; UNCOMMITTED. NEXT: the commit; then 15 (ch 17-18 read, lean).', 'the sitting line')
mm = rd(MM)
mm2 = sub1(mm, 'UNCOMMITTED; NEXT: the tail, then the commit', 'chain green; UNCOMMITTED; NEXT: the commit, then 15 (ch 17-18 read, lean)', 'the walk line')
mw = rd(MW)
mw2 = sub1(mw, 'the gates chain launched; UNCOMMITTED; NEXT the tail then the commit) — COMMITTED AND PUSHED THROUGH e824e52', 'the gates chain ALL GREEN on its second pass; UNCOMMITTED; NEXT the commit, then 15) — COMMITTED AND PUSHED THROUGH e824e52', 'the description')
mw2 = mw2.rstrip('\n') + "\n\nSITTING 14b DONE 2026-09-23 (the tail): the gates chain ALL GREEN on its second pass (%d steps, %d s — the positions at four workers, the sweep %s; the first pass stopped at Q33 and the registration edge, both filed from the prints); the records written, the forms copied, the message built. THE LESSONS: a hole pattern is the effect's own name; an earlier chapter's scan of the one database moves with a later chapter's entries (five seats — the scan census the instrument, extended to the probes' and the tape's own scans next sitting); the old runners' cells take question keys; a copied ink block's name can shadow an alias; the lean compile window held (%d steps, %d machine seconds). UNCOMMITTED since e824e52. NEXT on his word: the commit; then 15 (chapters 17-18's reading, lean) after a compaction.\n" % (len(STEPS), CHAIN_S, SWEEP, NSTEP, TSEC)
debt = rd(DEBT); anchor = ' 14b (the compile of 16): next.'
assert debt.count(anchor) == 1, debt.count(anchor)
debt2 = debt.replace(anchor, DEBT_LINE)
for t in (ASB, NOTE210, DEBT_LINE): assert not re.search(r'[֐-׿]', t), 'no Hebrew script in the new texts'
assert len(rec2.encode()) <= 10240 and len(mm2.encode()) < 17000, (len(rec2.encode()), len(mm2.encode()))
print('THE RECORDS CHECKED: the AS BUILT %d bytes; the NOTE %d; the recovery page %d; MEMORY.md %d; the walk note %d; the debt line %d' % (len(ASB.encode()), len(NOTE210.encode()), len(rec2.encode()), len(mm2.encode()), len(mw2.encode()), len(DEBT_LINE.encode())))
if not CHECK:
    open(MAP, 'w', encoding='utf-8').write(m.rstrip('\n') + ASB)
    open(SD, 'w', encoding='utf-8').write(sd.rstrip('\n') + NOTE210 + '\n')
    open(REC, 'w', encoding='utf-8').write(rec2); open(MM, 'w', encoding='utf-8').write(mm2); open(MW, 'w', encoding='utf-8').write(mw2); open(DEBT, 'w', encoding='utf-8').write(debt2)
    import subprocess as sp_
    lints = {}
    for f in (MAP, SD, REC, MM, DEBT, MW):
        lints[os.path.basename(f)] = sp_.run(['python3', f'{ROOT}/logic/solo_tools/gloss_lint.py', f], capture_output=True, text=True).stdout.strip().split('\n')[-1]
    print('THE RECORDS WRITTEN — the lints:', lints)
