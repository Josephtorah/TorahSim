#!/usr/bin/env python3
"""write_stepper_records.py — THE LOOP step 7 (b) THE STEPPER: the records at the close (2026-09-14). Every anchor asserted once; idempotent."""

def patch(path, pairs):
    t = open(path, encoding='utf-8').read(); done = 0
    for old, new in pairs:
        n = t.count(old)
        if n == 0 and new in t:
            continue
        assert n == 1, (path, n, old[:70]); t = t.replace(old, new); done += 1
    open(path, 'w', encoding='utf-8').write(t)
    print('%s: %d replacement(s)' % (path, done))

def append(path, text, marker):
    t = open(path, encoding='utf-8').read()
    if marker in t:
        print('%s: already appended' % path); return
    if not t.endswith('\n'):
        t += '\n'
    open(path, 'w', encoding='utf-8').write(t + text)
    print('%s: appended %d chars' % (path, len(text)))

R = '<repo-old>'
M = '<memory>'

ASBUILT = '''
## As built — step 7 (b) THE STEPPER (2026-09-14, the same sitting; the owner: "ok go b"; the design above first, the probes to FAIL 0/8,
## then the code in ONE new file, then 8/8 — and a ninth probe after the first real session's miss)

THE PROBES FIRST: World/step9/step_probes.py S1-S8 written from the design and run on the unchanged tree — 0/8 ("No module named
world_stepper"), then 8/8 after the code with one probe expectation corrected BEFORE the code on the engine's own rule (S7: a timer's
subject is not an entity until the fire writes it — the court alone after three calls, not two entities).
THE CODE: World/step9/world_stepper.py — transform(source) (the yield prefix on every engine-call line, one call per line asserted),
tape_section(path), class Stepper (the real tape or a source text; the world built as run_to builds it; the live sink of part (a) attached
under the session's own source cold_run_sequence/stepper; the generator; step(by, until) with the six grains; the audit against the base at
every call; the report; show(open | ledger | custody | timers) from the database; close() the seal), print_report, main (--from --to --by
--steps --show --pause --quiet). No engine, journal, registry or runner file moved: the sitting's whole diff is two new files (the
stepper and its probes) and the records. Lints 0 on both.
THE REAL SESSIONS (World/step9/forms_numbers_walk/loop_2026-09-14/loop_sessions.sh; the prints in the state doc's #172):
  A. `--from 'Num 27:1' --to 'Num 28:1' --by verse`: THE REPLAY to the left edge of Num 27:1 — 1,465 lines run, 3,221 sealed (the cursor's own
     fork, K1's 3221), the world standing before Num 27:1 at day 908,718 = (2488, 6, 1) creation / (40, 6, 1) exodus, 301 entities, 181 open
     entries, 0 pending timers, audited against the base: yes; then FOUR STEPS by verse through the chapter — 27:1 the reading-placed marker
     (1 line); 27:1-4 the daughters' approach (event + write); 27:5 the judgment brought near (event + write); 27:6-11 the statute declared
     (event + close + write) — and the session STOPPED AT THE LEFT EDGE OF Num 28:1, sealed as a partial segment of 3,229 lines, the audit ok.
  B. `--by marker --quiet`: the whole tape in 158 steps (157 markers; the last step 41 lines from the last marker to Num 36:11), 3,362 lines
     sealed as the whole tape; THE BODIES COMPARED — the session's segment against the base line for line after the header: IDENTICAL, 3,362
     lines each, the same chain head 5c482e02f82ea462 (the headers differ in the source's name alone).
  THE MISS THE FIRST SESSIONS FOUND: thirty-two of the tape's sources are written in DOUBLE QUOTES (the stitcher's repr when the text holds
  an apostrophe) and the stepper's verse pattern read single quotes only — "the world stands before None" at 27:1-4 and 27:6-11; the three
  patterns now read either quote; S9 added AFTER the miss (every call of the real tape yields a verse — no None; 1,507 yields by book);
  session A rerun clean (the state doc's #172 has both prints).
THE TAPE AFTER THE SESSIONS: 10/10; the live report lists the session as a fifth source — cold_run_sequence/stepper 3,362 rows = 3,362 lines
MATCH beside the four worlds (23,411 rows in the one database). THE PROBES AFTER: live 7/7, journal 7/7, cursor 6/6 (the base untouched by
the sessions), step 9/9. THE GATES: no engine, journal or runner file moved — the daemon gate, the dependency gate, the journal gate and the
sweep stand as at part (a)'s close (57/57 at 6,378).
WHAT A PAUSE IS NOW: between two tape lines the world stands still, every line so far is on disk and in the database, the five views are
current under the session's source, and the report says where the world stands (the next call's verse), what day it is, what is open and
what is pending; --show reads the rows from the database. The port of part (c) hangs at exactly this pause.
OWED, named: the checkpoints as they fall (the stitcher's rewrite of run()'s checkpoint block into the tape); the cursor's own appended
lines live; time without a marker (the stepper never moves the clock); the window (CHRONICLE); the import (81.8 s) as every session's
fixed price.
LESSONS: A GENERATOR BEATS A THREAD for a pause — it yields BEFORE the call it is about to make, so the left edge is exact and the tape
resumes; measure the tape's shape (one call per line) and make it the contract, asserted at every load. A PATTERN READS THE STITCHER'S OWN
QUOTING — the repr writes double quotes when the text holds an apostrophe; a real session showed the None the probe tape could not.
'''
patch(R + '/World/step9/THE_LOOP.md', [
    ("(b) [ ] THE STEPPER — NEXT on the owner's word (its design section here first, the probes to FAIL, then the code); (c) [ ] THE PORT — after (b).",
     "(b) [x] THE STEPPER — BUILT 2026-09-14 (D15 THE TAPE AS A GENERATOR; World/step9/world_stepper.py; the design and the as-built below); (c) [ ] THE PORT — NEXT on the owner's word (its design section here first, the probes to FAIL, then the code)."),
])
append(R + '/World/step9/THE_LOOP.md', ASBUILT, '## As built — step 7 (b) THE STEPPER')

append(R + '/THE_WORLD.md', '''
### 2026-09-14 — STEP 7 (b) THE STEPPER BUILT: THE TAPE ONE CALL AT A TIME, AND THE STATE READ FROM THE DATABASE AT EVERY PAUSE (the owner: "ok go b"; the map: World/step9/THE_LOOP.md "Step 7 ... part (b)" design + as-built)

The step-through the entry of 2026-09-14 asked for exists: World/step9/world_stepper.py runs the stitched tape as a GENERATOR (decision D15 —
every engine-call line yields the verse it is about to run, so the pause falls between two lines and the stepper can stop at a verse's left
edge exactly as the cursor does, and resume), one call per step, or by verse, chapter, marker, day, or to a verse; at every pause the world
stands still, every line so far is on disk and in the one database under the session's own source, and the report reads the state from the
database. The replay is the audit: every sealed line must equal the base's at the same ordinal or the session is refused there. Measured
first: the tape is 1,507 engine calls on 1,507 lines, and the checkpoints are computed after the run, not on it (owed to the stitcher). The
real sessions: chapter 27 stepped by verse from the left edge of 27:1 (the replay 3,221 lines, four steps, stopped at the left edge of 28:1);
the whole tape by marker in 158 steps, its segment the base's body byte for byte. step_probes.py 0/8 → 9/9. NEXT on the owner's word:
(c) THE PORT — the queue the loop reads at this pause, the text its first producer.
''', '### 2026-09-14 — STEP 7 (b) THE STEPPER BUILT')

patch(R + '/World/step9/COMPILE_DEBT.md', [
    ("OWED on the owner's word: (b) THE STEPPER, then (c) THE PORT — each its design section first.\n",
     "OWED on the owner's word: (b) THE STEPPER, then (c) THE PORT — each its design section first.\n"
     "      STEP 7 (b) THE STEPPER BUILT 2026-09-14 (the owner: \"ok go b\"; THE_LOOP.md \"Step 7 ... part (b)\" design + as-built; D15 THE TAPE AS A GENERATOR — World/step9/world_stepper.py, one call per step or by verse / chapter / marker / day / to a verse's left edge; the state read from the database at every pause; the replay the audit at every call; step_probes.py 0/8 → 9/9; the real sessions: chapter 27 by verse, the whole tape by marker with its segment the base's body byte for byte). OWED on the owner's word: (c) THE PORT — its design section first; and the checkpoints as they fall (the stitcher's rewrite), named.\n"),
])

patch(R + '/THE_STEPS.md', [
    ("reads between steps).\n",
     "reads between steps).\n"
     "\n"
     "STEP 7 (b) THE STEPPER (2026-09-14, the owner's \"ok go b\"; THE_LOOP.md\n"
     "\"Step 7 ... part (b)\" design + as-built; World/step9/world_stepper.py):\n"
     "the tape runs as a GENERATOR — every engine-call line yields the verse\n"
     "it is about to run, so a session steps one call at a time, or by\n"
     "verse, chapter, marker, day, or to a verse's left edge, and resumes;\n"
     "at every pause the world stands still, every line so far is on disk\n"
     "and in the database under the session's own source, and the report\n"
     "reads the state from the database (--show open | ledger | custody |\n"
     "timers). The replay is the audit: a sealed line that differs from the\n"
     "base's at the same ordinal refuses the session there. The pause is a\n"
     "control word, never a data event — the port of part (c), owed on the\n"
     "owner's word, is the only door for inputs.\n"),
])

patch(R + '/THE_BRIEFING.md', [
    ('## SCOREBOARD (as of 2026-09-14, latest)\n',
     '## SCOREBOARD (as of 2026-09-14, latest)\n'
     '- **THE STEP-THROUGH EXISTS — THE LOOP\'S STEP 7 (b) THE STEPPER BUILT: THE TAPE RUNS ONE CALL AT A TIME, STOPS AT ANY VERSE\'S LEFT EDGE, RESUMES, AND AT EVERY PAUSE THE STATE IS READ FROM THE DATABASE** (2026-09-14, on your "ok go b"; World/step9/THE_LOOP.md "Step 7 ... part (b)"; World/step9/world_stepper.py): measured first — the tape is 1,507 engine calls on 1,507 lines and the checkpoints are computed after the run, not on it — so the tape runs as a generator that yields the verse of each call before making it (decision D15; no thread, no engine change); step by call, verse, chapter, marker, day, or to a verse; the replay is the audit at every call; step_probes.py 0/8 then 9/9 (the ninth added after the first real session read a double-quoted source as no verse); the real sessions: chapter 27 stepped by verse from the left edge of 27:1, the whole tape by marker in 158 steps with its segment the base\'s body byte for byte; the tape 10/10 after, every probe file green. Next on your word: (c) the port — the queue the loop reads at the pause, the text its first producer.\n'),
    ('## ENTRIES (newest first)\n',
     '## ENTRIES (newest first)\n'
     '\n'
     '### 2026-09-14 — THE STEP-THROUGH: THE TAPE ONE CALL AT A TIME, THE STATE READ FROM THE DATABASE AT EVERY PAUSE\n'
     '\n'
     'What changed: the tape used to run start to end and exit. Now a session\n'
     'runs it one engine call at a time — or by verse, chapter, date, day, or\n'
     'to any verse\'s left edge — and between two calls the world stands\n'
     'still. Every line so far is on disk and in the database, and the\n'
     'report reads what is open, what is pending and what day it is from the\n'
     'database itself. A session can stop early; its segment is sealed and\n'
     'audited like any run.\n'
     '\n'
     'How: the stitched tape is one engine call per line (measured: 1,507\n'
     'calls on 1,507 lines), so at load every call line is prefixed with a\n'
     'yield of the verse it is about to run. The function becomes a generator;\n'
     'the pause is between two next() calls; no thread, no change to the\n'
     'engine. Because the yield comes before the call, the session can stop\n'
     'exactly at a verse\'s left edge, as the cursor does, and unlike the\n'
     'cursor it resumes. The replay is the audit: every line the session\n'
     'seals must equal the base run\'s line at the same ordinal, or the\n'
     'session is refused there.\n'
     '\n'
     'Going forward: the port — the queue the loop reads at this pause, with\n'
     'the text as its first producer — is the last of the three, on your\n'
     'word, design first. The checkpoints as they fall are owed to the\n'
     'stitcher (today they are computed after the run).\n'),
])

append(R + '/World/RESUME.md',
       'SITTING THE LOOP STEP 7 (b) DONE 2026-09-14 (THE STEPPER; THE_LOOP.md "Step 7 ... part (b)" design + as-built; the owner: "ok go b"): the measurement before the design (the tape one engine call per line, 1,507 calls; the checkpoints computed after the run), D15 THE TAPE AS A GENERATOR (no thread, no engine change), World/step9/world_stepper.py (step by call / verse / chapter / marker / day / to a verse\'s left edge; the state read from the database at every pause; the replay the audit at every call), step_probes.py 0/8 → 9/9, the real sessions (chapter 27 by verse from the left edge of 27:1; the whole tape by marker in 158 steps, the segment the base\'s body byte for byte), the tape 10/10 after. NEXT on the owner\'s word: (c) THE PORT.\n',
       'SITTING THE LOOP STEP 7 (b) DONE 2026-09-14')

append(M + '/the-loop-ruling.md', '''
**2026-09-14 — STEP 7 (b) THE STEPPER BUILT (the owner: "ok go b"; THE_LOOP.md "Step 7 ... part (b)" design + as-built; the state doc's
#172).** D15 THE TAPE AS A GENERATOR: World/step9/world_stepper.py transforms the stitched tape at load — every engine-call line prefixed
with `yield (verse, ordinal); ` (one call per line asserted; 1,507 on today's tape) — and runs it as a generator: each next() runs one tape
line (the marker with the timers it fires; the event with its consequences; a close) and yields the NEXT call's verse before running it, so
the pause is between two lines, the left edge of any verse is exact (as the cursor), and the tape RESUMES (unlike the cursor). No thread, no
engine change. The session journals under its own source cold_run_sequence/stepper (the base untouched); a partial session seals a partial
segment; THE REPLAY IS THE AUDIT — every sealed line must equal the base's at the same ordinal or the session is REFUSED there. Grains:
call | verse | chapter | marker | day | a verse address. The report at every pause: the lines run and sealed, the next verse, the clock, the
entities, the open entries, the pending timers; --show open | ledger <entity> | custody | timers reads the rows FROM THE DATABASE. --pause
waits for Enter (a control word, never a data event). MEASURED FIRST: the checkpoints are NOT in the tape (computed after the run from M —
"as they fall" owed to the stitcher). step_probes.py 0/8 → 9/9 (S9 added after the first real session read the tape's 32 double-quoted
sources as no verse — the patterns read either quote now). THE REAL SESSIONS: chapter 27 by verse from the left edge of 27:1 (the replay
3,221 lines = the cursor's fork; four steps; stopped at the left edge of 28:1; a partial segment of 3,229 lines); the whole tape by marker in
158 steps, 3,362 lines, the segment's body IDENTICAL to the base (chain head 5c482e02f82ea462). The tape 10/10 after (the session a fifth
source in the live report); live 7/7, journal 7/7, cursor 6/6. NEXT on the owner's word: (c) THE PORT — the queue read at the pause, the
text its first producer, every later pass under its own run name, through World.submit alone.
''', '2026-09-14 — STEP 7 (b) THE STEPPER BUILT')
patch(M + '/MEMORY.md', [
    ('— NEXT (b) THE STEPPER then (c) THE PORT, each its design section first;',
     '; STEP 7 (b) THE STEPPER BUILT 2026-09-14 on "ok go b" — D15 THE TAPE AS A GENERATOR (World/step9/world_stepper.py: one call per step or by verse / chapter / marker / day / to a verse\'s left edge; the state from the database at every pause; the replay the audit; step_probes.py 0/8 → 9/9; the real sessions green) — NEXT (c) THE PORT, its design section first;'),
])
patch(M + '/step9-exam-era.md', [
    ('⚠ THE LOOP step 7 (a) WRITE AS YOU GO (2026-09-14): A PAYLOAD MOVES AFTER THE LOG',
     '⚠ THE LOOP step 7 (b) THE STEPPER (2026-09-14): A GENERATOR BEATS A THREAD FOR A PAUSE — it yields BEFORE the call it is about to make, so a left edge is exact and the tape resumes; measure the tape\'s shape first (one engine call per line, 1,507 on 1,507) and assert it as the contract at every load. A PATTERN READS THE STITCHER\'S OWN QUOTING — its repr writes double quotes when the text holds an apostrophe (32 sources); the probe tape could not show it, the first real session did: a real session after the probes, always. AN EXPECTATION TYPED BY HAND IS CHECKED AGAINST THE ENGINE\'S OWN RULE BEFORE THE CODE (a timer\'s subject is not an entity until the fire writes it). THE CHECKPOINTS ARE NOT ON THE TAPE — computed after the run from the marker table; "as they fall" is the stitcher\'s.\n'
     '⚠ THE LOOP step 7 (a) WRITE AS YOU GO (2026-09-14): A PAYLOAD MOVES AFTER THE LOG'),
])

append(R + '/logic/pre_logic_methods_2026-07-28/RECOVERY_new_thread_2026-09-12.md', '''
## 21. ADDENDUM (2026-09-14, THE LOOP STEP 7 (b) THE STEPPER — the owner: "ok go b"; the state doc's COMPACTION POINT #172)

BUILT: THE_LOOP.md "Step 7 THE LOOP THAT WAITS — part (b) THE STEPPER: the design" + "As built" (the box's part (b) ticked; (c) THE PORT the
one left). D15 THE TAPE AS A GENERATOR: World/step9/world_stepper.py transforms the stitched tape at load (every engine-call line prefixed
with `yield (verse, ordinal); ` — one call per line asserted, 1,507 on today's tape) and runs it as a generator: each next() runs one tape
line and yields the NEXT call's verse before running it — the pause between two lines, the left edge of a verse exact, the tape resumable.
No engine, journal, registry or runner file moved (two new files: the stepper and step_probes.py). THE SESSION journals under its own source
cold_run_sequence/stepper (the base untouched); a partial session seals a partial segment; THE REPLAY IS THE AUDIT at every call (a sealed
line differing from the base's at the same ordinal REFUSES the session there). GRAINS: call | verse | chapter | marker | day | a verse
address (--to stops at a left edge). THE REPORT at every pause: the lines run and sealed, the next verse, the clock (the day, the creation
date, the exodus date), the entities, the open entries, the pending timers, audited yes/no; --show open | ledger <entity> | custody |
timers reads the rows FROM THE DATABASE under the session's source; --pause waits for Enter (a control word, never a data event).
MEASURED FIRST: 1,507 calls on 1,507 lines (1,279 submits, 157 markers, 71 closes; 0 multi-line calls); THE CHECKPOINTS ARE NOT ON THE TAPE
(computed in run() after it from M — "as they fall" owed to the stitcher); the 1,533 blocks of (a) = 1,507 lines + 26 walks with fires; the
import 81.8 s the session's fixed price; a thread considered and refused (it cannot stop before a line). THE PRINTS: step_probes.py 0/8 →
8/8, then S9 added after the first real session's miss (32 double-quoted sources read as no verse; the patterns read either quote now) →
9/9; SESSION A `--from 'Num 27:1' --to 'Num 28:1' --by verse`: the replay 3,221 lines (the cursor's fork), four steps (27:1 the marker;
27:1-4; 27:5; 27:6-11), stopped at the left edge of 28:1, a partial segment of 3,229 lines, audited; SESSION B `--by marker --quiet`: 158
steps, 3,362 lines, the body IDENTICAL to the base (chain head 5c482e02f82ea462); the tape 10/10 after with the session a fifth source
(23,411 rows, every source current); live 7/7, journal 7/7, cursor 6/6. THE FORMS: forms_numbers_walk/loop_2026-09-14/ (loop_design_b.md,
loop_sessions.sh, write_stepper_records.py). LINTS: world_stepper.py 0, step_probes.py 0, every record at its baseline. THE GATES: unchanged
files — the daemon, dependency and journal gates and the sweep stand as at (a)'s close.

NEXT on the owner's word: (c) THE PORT — the design section in THE_LOOP.md first (the queue the loop reads at the pause; the text the first
producer; a later pass under its own run name; every input through World.submit alone — the one door; the registry refuses an unregistered
kind; what a queued input looks like and where it lives — primary in git or derived; the stepper's pause the seam), the probes to FAIL, then
the code. Still UNCOMMITTED since a42f518; commit only on "commit push" with the staging form of section 18.
''', '## 21. ADDENDUM (2026-09-14, THE LOOP STEP 7 (b)')

append(R + '/logic/pre_logic_methods_2026-07-28/PROMPT_continue_solo_era_2026-08-06.md', '''
═══ COMPACTION POINT #172 (2026-09-14 — written at the close of THE LOOP STEP 7 (b) THE STEPPER, the owner's "ok go b" after part (a) and his question "is that a simulation?" — answered: the history never changes, the state changes with every line, and nothing yet WAITS; A CLEAN COMPACTION POINT) ═══
BUILT: THE LOOP THAT WAITS, part (b) — THE_LOOP.md "Step 7 THE LOOP THAT WAITS — part (b) THE STEPPER: the design" + "As built"; the box's (b) ticked, (c) THE PORT the one left. DECISION D15 THE TAPE AS A GENERATOR (mine, on the measurement; the owner may overrule): World/step9/world_stepper.py transforms the stitched tape at load — every engine-call line prefixed with `yield (verse, ordinal); ` (one call per line asserted; 1,507 on today's tape) — and runs it as a generator: each next() runs one tape line (the marker with the timers it fires, the event with its consequences, a close) and yields the NEXT call's verse before running it — the pause between two lines, a verse's left edge exact (as the cursor), the tape resumable (unlike it). No engine, journal, registry or runner file moved. THE SESSION under its own source cold_run_sequence/stepper (the base untouched; a partial session a partial segment, audited); THE REPLAY IS THE AUDIT at every call (a differing line refuses the session at its ordinal). GRAINS call | verse | chapter | marker | day | a verse address; THE REPORT at every pause (the lines run and sealed, the next verse, the clock, the entities, the open entries, the pending timers, audited); --show open | ledger | custody | timers FROM THE DATABASE; --pause a control word only.
MEASURED FIRST: 1,507 calls on 1,507 lines (1,279 / 157 / 71; no multi-line call); the checkpoints NOT on the tape (computed after the run from M — owed to the stitcher); the 1,533 blocks of (a) = 1,507 lines + 26 walks with fires; a thread refused.
THE PRINTS: step_probes.py 0/8 → 8/8 (S7's hand-typed entity count corrected before the code on the engine's rule), S9 added after the first real session's miss (32 double-quoted sources read as no verse) → 9/9; SESSION A `--from 'Num 27:1' --to 'Num 28:1' --by verse`: the replay 3,221 lines (the cursor's fork), the world before Num 27:1 at day 908,718 = (2488, 6, 1) / exodus (40, 6, 1), 301 entities, 181 open, 0 pending; four steps by verse (27:1 the marker; 27:1-4 event + write; 27:5 event + write; 27:6-11 event + close + write); stopped at the left edge of 28:1; a partial segment of 3,229 lines, the audit ok. SESSION B `--by marker --quiet`: 158 steps, 3,362 lines, the whole tape; the body IDENTICAL to the base line for line (chain head 5c482e02f82ea462; the headers differ in the source's name alone). AFTER: the tape 10/10 (the session a fifth source: 3,362 rows = 3,362 lines MATCH; 23,411 rows); live 7/7, journal 7/7, cursor 6/6, step 9/9; the gates and the sweep unchanged from (a)'s close. RUN unmoved; the hash 8b8fff1fa28953af untouched. Lints: world_stepper.py 0, step_probes.py 0, THE_LOOP 0; the state doc 147; THE_WORLD 5; MEMORY.md 4; THE_STEPS 1.
THE RECORDS: THE_LOOP.md, THE_WORLD.md (the third 2026-09-14 entry), COMPILE_DEBT.md's loop box, THE_STEPS's loop section, THE_BRIEFING (the scoreboard + an entry), World/RESUME.md, memory (the-loop-ruling.md, MEMORY.md's loop line, step9-exam-era.md's lessons head), the recovery file's section 21; the forms in forms_numbers_walk/loop_2026-09-14/.
LESSONS: a generator beats a thread for a pause (it yields before the call — the left edge exact, the tape resumes); a pattern reads the stitcher's own quoting (32 double-quoted sources; the probe tape could not show it, the real session did — a real session after the probes, always); a hand-typed expectation is checked against the engine's rule before the code; the checkpoints are not on the tape.
NEXT on the owner's word, ONE OF: (a) THE PORT — part (c): the design section in THE_LOOP.md first (the queue the loop reads at the pause; the text the first producer; a later pass under its own run name; every input through World.submit alone, the registry refusing an unregistered kind; what a queued input looks like and where it lives; the stepper's pause the seam), the probes to FAIL, then the code; (b) THE NEXT BOOK (as #160); (c) the py_units gloss sitting. Still UNCOMMITTED since a42f518 (sittings 8-15b, the ARCHITECTURE folder, the review, the gloss patches, the loop's step 7 (a) and (b)); the staging form `git add -A -- . ':!elijah_docket' ':!DISPOSABLE_scan/*.zip'`; commit only on "commit push".
POST-COMPACTION REREADS (mandatory, first sitting): as #170's, plus THE_LOOP.md's "Step 7 ... part (a)" and "part (b)" designs + as-builts and the recovery file's sections 20 and 21 (read before any word on the port).
''', '═══ COMPACTION POINT #172')
print('records written')
