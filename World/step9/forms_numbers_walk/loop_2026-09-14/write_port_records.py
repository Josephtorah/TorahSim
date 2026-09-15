#!/usr/bin/env python3
"""write_port_records.py — THE LOOP step 7 (c) THE PORT: the records at the close, and TO FINISH THE LOOP — THE LIST (2026-09-14).
Every anchor asserted once; idempotent. {TAPE} is filled from the tape's print before the run."""
import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
import sys

def patch(path, pairs):
    t = open(path, encoding='utf-8').read(); done = 0
    for old, new in pairs:
        n = t.count(old)
        if n == 0 and new in t:
            continue
        assert n == 1, (path, n, old[:70]); t = t.replace(old, new); done += 1
    open(path, 'w', encoding='utf-8').write(t)
    print('%s: %d replacement(s)' % (path.split('/')[-1], done))

def append(path, text, marker):
    t = open(path, encoding='utf-8').read()
    if marker in t:
        print('%s: already appended' % path.split('/')[-1]); return
    if not t.endswith('\n'):
        t += '\n'
    open(path, 'w', encoding='utf-8').write(t + text)
    print('%s: appended %d chars' % (path.split('/')[-1], len(text)))

R = _ROOT
M = '<memory>'
TAPE = sys.argv[1] if len(sys.argv) > 1 else '{TAPE}'

ASBUILT = '''
## As built — step 7 (c) THE PORT (2026-09-14, the same sitting; the owner: "ok go c. keep up with what we need to do to finish this. go";
## the design above first, the probes to FAIL 0/9, then the code, then 9/9 with one probe index corrected on the engine's own order)

THE PROBES FIRST: World/step9/port_probes.py P1-P9 written from the design and run on the unchanged tree — 0/9 (P1 "No module named
world_port", P2-P9 the stepper refusing a queue); then 8/9 after the code, the one miss P5's hand-typed index (it put the marker's line
between the fire's two — the walk fires inside the marker's call and the marker's own line follows, as part (a)'s L3 measured), corrected
on the engine's order and noted in the probe; then 9/9.
THE CODE: World/step9/world_port.py — class Port (the queue file read once and validated at open: an unregistered kind, an unknown field, a
bad position, a position already passed by a session starting later REFUSED and named; a registered field the item lacks a WARNING; due()
the items entering at a pause in file order; event_of() the item's event with the port's mark; pending); the stepper's hooks in
world_stepper.py (Stepper(queue=…) → the source cold_run_sequence/port@<queue>; _enter() at every pause — before the text's line, at every
pause inside a multi-line step, and at the end; the audit stops at the first input, THE FORK recorded by ordinal and item; the report's
inputs / fork / forked_by; the header {base, fork, forked_by, queue, pending} at close; --queue on the command line; the session's own
source named in the prints); world_journal._append_log's EVENT branch marks prov.unit 'port:<queue>' beside 'scenario' and 'tape';
worldledger.Segment.write writes the header's extra fields whenever given. No engine change. The queue folder World/journal/port/ is
tracked (an input is PRIMARY, as scenarios.yaml is); its first queue daughters.yaml carries the two horns of the daughters' argument
(scenarios.yaml's step-5 exemplar) positioned at the left edge of Num 27:5. Lints 0 on every file.
THE PROBES AFTER: port 9/9, step 9/9, live 7/7, journal 7/7, cursor 6/6 (the base untouched).
THE REAL SESSION (`--from 'Num 27:1' --to 'Num 28:1' --by verse --queue World/journal/port/daughters.yaml --show custody`): the queue read at
open — 2 items, first_horn@Num 27:5 and second_horn@Num 27:5, no warnings; THE REPLAY 3,221 lines to the left edge of 27:1, audited; STEP 1
(27:1 with 27:1-4: marker + event + write) audited; STEP 2 AT THE LEFT EDGE OF 27:5 — THE TWO INPUTS ENTERED FIRST, then the text's line: 6
sealed (event 3, write 3) — first_horn's event and its answer holding_owed on the daughters at Num 27:8 (seq 3226, law_zelophehad),
second_horn's event and its answer exempt = child_of_any_kind on the widow at Deut 25:5 (seq 3228, law_zelophehad — the oracle's row,
Mishnah Yevamot 2:5), then the judgment brought near with the court's custody row (seq 3230); FORKED AT ORDINAL 3225 BY first_horn — no
audit past the fork; STEP 3 (27:6-11) the statute declared, the custody closed; the left edge of 28:1 reached; SEALED 3,233 lines in 1,497
blocks, the chain VERIFIED, the fresh conversion EQUAL but the right edge, the rebuilt index EQUALS the live rows; the header
{"base": the running world's segment, "fork": 3225, "forked_by": "first_horn", "queue": "daughters", "pending": []}; the world askable under
--world cold_run_sequence/port@daughters (the daughters' two holding_owed rows; the widow's exempt).
THE TAPE AFTER: %s.
A FINDING, filed in the list below: the second horn's case_source cites Deuteronomy 25:5 and the engine's VERSE REACHED moved to (Deut, 25, 5)
inside Numbers 27 — an input's citation moves the position the installation gate reads (harmless under boot; the from_event setting would
read it). The port's position and the input's citation are two things; which the engine's position follows is part of the inputs' own
definition, the owner's.
WHAT THE LOOP IS NOW: a running world with memory that WRITES AS IT RUNS (a), PAUSES BETWEEN CALLS (b) and READS ITS NEXT INPUT FROM OUTSIDE
ITSELF (c) — the text its first producer, a queue its second; every input through the one door, journaled, audited to the fork, the world
with inputs its own world in the one database. What the inputs are is not decided; the port does not decide it.
''' % TAPE

TOFINISH = '''
## TO FINISH THE LOOP — THE LIST (the owner, 2026-09-14: "keep up with what we need to do to finish this"; A STANDING DUTY: this section is
## brought current at every loop sitting, and the reply at every loop sitting's close echoes it; the boxes above are its ledger)

BUILT: steps 1-5 (the sink; the index with the five views and the ask tool; installation; the cursor; scenarios), step 1's amendment (the
close line), step 7 (a) write as you go, (b) the stepper, (c) the port — 2026-09-14.

OPEN, each with its home and its size (the owner's items marked; nothing moves before his word):
  1. THE INPUTS THEMSELVES — the owner's decision ("we will decide what those are later"): what a second or third pass produces, in what
     form, at what positions; the port takes any registered kind now, from any file. OWNER. Then: a queue writer for that pass (a sitting).
  2. THE SECOND PASS — D2 (2026-09-09): the installed run (installed_by from_event) after Deuteronomy, on the whole program; its findings a
     queue for the port. AFTER DEUTERONOMY; a sitting.
  3. STEP 6 THE READBACK — D12: the text re-read against the ledger the run left (Deuteronomy's repetition first, the prophets after); its
     design at Deuteronomy. AFTER DEUTERONOMY; the design a sitting, then per book.
  4. D7'S MERGE — one database: the World folder's corpus world (the reading era's 557 events, World/world.sqlite) as a journal layer, its
     tables views over the journal, the reconciliation gate upstream; the August tree retired with it (D10). A SITTING.
  5. THE CHECKPOINTS AS THEY FALL — the checkpoints are computed after the run from the marker table (part (b)'s measurement 2); the stitcher
     places each at its verse in the tape so a pause shows them. A SITTING (the stitcher's rewrite; the base's bytes unchanged).
  6. TIME WITHOUT A MARKER — may the loop advance a day with no verse? Fourteen timers wait past the tape's end (Midian's third and seventh
     days, the altar's daily offering). OWNER's decision; the mechanism half a sitting if yes (the stepper never moves the clock today).
  7. THE POSITION OF AN INPUT — part (c)'s finding: an input's citation moves the engine's verse reached (the installation gate's position);
     whether the engine follows the port's position or the input's citation. OWNER's, inside item 1; the code one line either way.
  8. THE CURSOR'S OWN LINES LIVE — the cursor's appended segment is converted late (part (a)'s (5)); the stepper with a queue does the
     same job live, so the cursor may retire into the stepper (--from with a queue). SMALL; the owner's call whether the cursor stays.
  9. THE WINDOW — CHRONICLE (ARCHITECTURE/CHRONICLE.md, the design thread's, design only): the observation deck over the live database now
     that it is live. THE DESIGN THREAD'S; the main thread reads it.
 10. THE INTERFACE — "later we will create an interface to the database that will show the current states at all times": over the five
     views and the sessions' sources; the ask tool is its first form. LATER, the owner's word; its own design.
 11. A GRADED INPUT — an input's answer against an oracle through the port (scenarios grade against Mishnah rows at a cursor; the port only
     opens the door). WITH ITEM 1.
 12. THE OTHER WORLDS STEPPED — the stepper runs the running setting only; the sojourn forks and THE REST run whole in the tape. SMALL, if
     ever wanted.
'''
patch(R + '/World/step9/THE_LOOP.md', [
    ("(c) [ ] THE PORT — NEXT on the owner's word (its design section here first, the probes to FAIL, then the code).",
     "(c) [x] THE PORT — BUILT 2026-09-14 (D16-D18; World/step9/world_port.py + the stepper's --queue; the first queue World/journal/port/daughters.yaml; the design and the as-built below). THE LOOP THAT WAITS IS BUILT; what remains is TO FINISH THE LOOP — THE LIST, the section after the as-built, kept current."),
])
append(R + '/World/step9/THE_LOOP.md', ASBUILT + TOFINISH, '## As built — step 7 (c) THE PORT')

append(R + '/THE_WORLD.md', '''
### 2026-09-14 — STEP 7 (c) THE PORT BUILT: THE LOOP READS ITS NEXT INPUT FROM OUTSIDE ITSELF (the owner: "ok go c. keep up with what we need to do to finish this. go"; the map: World/step9/THE_LOOP.md "Step 7 ... part (c)" design + as-built + TO FINISH THE LOOP — THE LIST)

The loop that waits is whole: it writes as it runs (a), pauses between calls (b), and now reads its next input from a QUEUE outside the code
(c) — a file of items, read once at open and validated against the registry (an unregistered kind or an unknown field refused; the one door),
each item entering at its position (a verse's left edge, the first pause, or the end) in file order before the text's own line, journaled
with prov.unit 'port:<queue>'. A world with inputs is its own world (D17): the session audits against the base up to the first input, forks
there, and seals whole under the queue's name with the fork in its header — askable in the one database. The text is the first producer (a
session with no queue is the base byte for byte); the port decides nothing about what the inputs are. The first real queue: the daughters'
two horns (Bava Batra 119b:10) at the left edge of Num 27:5 — both answered by the daemon (the daughters' holding owed; the widow exempt, a
child of any kind), the session forked at ordinal 3,225. port_probes.py 0/9 → 9/9. THE LIST of what finishes the loop is in the map and is
kept current from now on: the inputs themselves (yours), the second pass and the readback (after Deuteronomy), the merge, the checkpoints as
they fall, time without a marker (yours), the position of an input (yours), the cursor's lines, the window, the interface, a graded input.
''', '### 2026-09-14 — STEP 7 (c) THE PORT BUILT')

patch(R + '/World/step9/COMPILE_DEBT.md', [
    ("OWED on the owner's word: (c) THE PORT — its design section first; and the checkpoints as they fall (the stitcher's rewrite), named.\n",
     "OWED on the owner's word: (c) THE PORT — its design section first; and the checkpoints as they fall (the stitcher's rewrite), named.\n"
     "      STEP 7 (c) THE PORT BUILT 2026-09-14 (the owner: \"ok go c. keep up with what we need to do to finish this. go\"; THE_LOOP.md \"Step 7 ... part (c)\" design + as-built; D16 a queue never a prompt, D17 a world with inputs its own world, D18 the queue first then the text — World/step9/world_port.py + the stepper's --queue; the first queue World/journal/port/daughters.yaml, the two horns at the left edge of 27:5, both answered; port_probes.py 0/9 → 9/9). THE LOOP THAT WAITS IS BUILT. WHAT FINISHES THE LOOP: THE_LOOP.md \"TO FINISH THE LOOP — THE LIST\" (twelve items, kept current at every loop sitting; the owner's: the inputs themselves, time without a marker, the position of an input; after Deuteronomy: the second pass, the readback; sittings: the merge, the checkpoints as they fall; small: the cursor's lines, the other worlds; the design thread's: the window; later: the interface, a graded input).\n"),
])

patch(R + '/THE_STEPS.md', [
    ("owner's word, is the only door for inputs.\n",
     "owner's word, is the only door for inputs.\n"
     "\n"
     "STEP 7 (c) THE PORT (2026-09-14, the owner's \"ok go c. keep up with what\n"
     "we need to do to finish this. go\"; THE_LOOP.md \"Step 7 ... part (c)\"\n"
     "design + as-built; World/step9/world_port.py): the loop reads its next\n"
     "input from a QUEUE outside the code — a file of items (World/journal/\n"
     "port/<queue>.yaml, primary), read once at open and validated against the\n"
     "registry (an unregistered kind or an unknown field refused — the one\n"
     "door), each entering at its position in file order before the text's\n"
     "own line, journaled as 'port:<queue>'. A world with inputs is its own\n"
     "world: audited against the base to the first input, forked there,\n"
     "sealed whole under the queue's name. The text is the first producer;\n"
     "the port decides nothing about what the inputs are. THE LOOP THAT\n"
     "WAITS IS BUILT; what finishes the loop is THE LIST in THE_LOOP.md,\n"
     "kept current at every loop sitting.\n"),
])

patch(R + '/THE_BRIEFING.md', [
    ('## SCOREBOARD (as of 2026-09-14, latest)\n',
     '## SCOREBOARD (as of 2026-09-14, latest)\n'
     '- **THE LOOP THAT WAITS IS BUILT — STEP 7 (c) THE PORT: THE LOOP READS ITS NEXT INPUT FROM A QUEUE OUTSIDE THE CODE, EVERY INPUT THROUGH THE ONE DOOR, AND A WORLD WITH INPUTS IS ITS OWN WORLD** (2026-09-14, on your "ok go c. keep up with what we need to do to finish this. go"; World/step9/THE_LOOP.md "Step 7 ... part (c)" and "TO FINISH THE LOOP — THE LIST"): a queue file read once and validated at open (an unregistered kind or an unknown field refused), its items entering at their positions in file order before the text\'s line, journaled as port:<queue>; the session audited against the base to the first input and forked there, sealed whole under the queue\'s name with the fork in its header; the text the first producer (no queue = the base byte for byte); the first real queue the daughters\' two horns at the left edge of 27:5, both answered by the daemon; port_probes.py 0/9 then 9/9; every probe file green; the tape after. The port decides nothing about what the inputs are. THE LIST of what finishes the loop is in the map, twelve items, kept current: three are yours (the inputs themselves, time without a marker, the position of an input), two wait for Deuteronomy (the second pass, the readback), two are sittings (the merge, the checkpoints as they fall), the rest small or later.\n'),
    ('## ENTRIES (newest first)\n',
     '## ENTRIES (newest first)\n'
     '\n'
     '### 2026-09-14 — THE PORT: THE LOOP READS FROM OUTSIDE ITSELF, AND THE LIST OF WHAT FINISHES IT\n'
     '\n'
     'What changed: the loop now takes inputs from a queue outside the code. A\n'
     'queue is a file of items, each a registered event at a position in the\n'
     'text. It is read once when a session opens, checked against the\n'
     'registry (an unregistered kind or a misspelled field is refused before\n'
     'anything runs), and at every pause the items due enter through the\n'
     'same door every tape line enters, in file order, before the text\'s own\n'
     'line. The journal marks them as the queue\'s. Nothing is typed at a\n'
     'prompt; the port cannot tell a program\'s file from a hand\'s and does\n'
     'not care.\n'
     '\n'
     'Why a world with inputs is its own world: an input changes the future —\n'
     'a timer it sets fires later, an entry it opens is what a later close\n'
     'finds. So the session is audited against the base run only up to the\n'
     'first input, forks there, and is sealed whole under the queue\'s name\n'
     'with the fork in its header. The base is never touched. The first real\n'
     'queue put the daughters\' two horns at the left edge of 27:5; the daemon\n'
     'answered both as the Mishnah does.\n'
     '\n'
     'Going forward: the loop that waits is built. What remains to finish the\n'
     'loop is a list in the map, kept current from now on. Three items are\n'
     'yours to decide: what the inputs are, whether time may move without a\n'
     'verse, and whether an input\'s position or its citation moves the\n'
     'engine\'s place in the text. Two wait for Deuteronomy: the second pass\n'
     'and the readback. Two are sittings: the merge of the two databases and\n'
     'the checkpoints placed in the tape. The rest are small or later.\n'),
])

append(R + '/World/RESUME.md',
       'SITTING THE LOOP STEP 7 (c) DONE 2026-09-14 (THE PORT; THE_LOOP.md "Step 7 ... part (c)" design + as-built + "TO FINISH THE LOOP — THE LIST"; the owner: "ok go c. keep up with what we need to do to finish this. go"): D16 a queue never a prompt, D17 a world with inputs its own world, D18 the queue first then the text; World/step9/world_port.py + the stepper\'s --queue; port_probes.py 0/9 → 9/9; the first queue World/journal/port/daughters.yaml (the two horns at the left edge of 27:5, both answered; the session forked at 3,225, sealed 3,233 lines); the tape after. THE LOOP THAT WAITS IS BUILT. NEXT on the owner\'s word: the list\'s items (his three decisions first), or THE NEXT BOOK.\n',
       'SITTING THE LOOP STEP 7 (c) DONE 2026-09-14')

append(M + '/the-loop-ruling.md', '''
**2026-09-14 — STEP 7 (c) THE PORT BUILT (the owner: "ok go c. keep up with what we need to do to finish this. go"; THE_LOOP.md "Step 7 ...
part (c)" design + as-built; the state doc's #173). THE LOOP THAT WAITS IS BUILT.** D16 THE PORT IS A QUEUE, NEVER A PROMPT: World/journal/
port/<queue>.yaml (tracked, primary) — items {id, at, label, event}, read ONCE at open and validated (an unregistered kind, an unknown field, a
bad position, a position already passed: REFUSED, named; a missing registered field a warning); at every pause the items due enter in file
order through World.submit, the EVENT line prov.unit 'port:<queue>', data.port {queue, id, label}. D17 A WORLD WITH INPUTS IS ITS OWN WORLD:
the session journals whole under cold_run_sequence/port@<queue>, audited against the base to the first input, THE FORK recorded (the header
{base, fork, forked_by, queue, pending}); the base untouched. D18 THE ORDER OF A PAUSE: the queue first, then the text; an unpositioned item at
the first pause; a positioned one at its verse's left edge; one past the end at the end. THE CODE: World/step9/world_port.py; the stepper's
--queue (_enter at every pause; the audit stops at the fork); world_journal's EVENT branch; worldledger's header. port_probes.py 0/9 → 9/9
(P5's index corrected on the engine's order: the fire's lines precede the marker's). THE REAL SESSION: daughters.yaml — the two horns at the
left edge of Num 27:5, entered before the text's line, both answered (holding_owed on the daughters at Num 27:8; exempt = child_of_any_kind on
the widow at Deut 25:5), forked at ordinal 3,225, sealed 3,233 lines, askable under --world cold_run_sequence/port@daughters. A FINDING: an
input's citation moves the engine's verse reached (Deut 25:5 inside Numbers 27) — the position or the citation, the owner's, inside the inputs'
definition. ⚠ A STANDING DUTY FROM THIS SITTING: THE_LOOP.md "TO FINISH THE LOOP — THE LIST" (twelve items) is brought current at every loop
sitting and echoed in the reply: the owner's three (the inputs themselves; time without a marker; the position of an input), after
Deuteronomy two (the second pass D2; step 6 the readback D12), sittings two (D7's merge; the checkpoints as they fall), small (the cursor's
lines live — the cursor may retire into the stepper; the other worlds stepped), the design thread's (the window, CHRONICLE), later (the
interface; a graded input).
''', '2026-09-14 — STEP 7 (c) THE PORT BUILT')
patch(M + '/MEMORY.md', [
    ('— NEXT (c) THE PORT, its design section first;',
     '; STEP 7 (c) THE PORT BUILT 2026-09-14 on "ok go c" — D16-D18 (World/step9/world_port.py + the stepper\'s --queue: a queue file read once and validated, its items through the one door at their positions before the text\'s line; a world with inputs its own world, forked at the first input; the first queue World/journal/port/daughters.yaml; port_probes.py 0/9 → 9/9). THE LOOP THAT WAITS IS BUILT. ⚠ STANDING DUTY: THE_LOOP.md "TO FINISH THE LOOP — THE LIST" (12 items: the owner\'s three — the inputs themselves, time without a marker, the position of an input; after Deuteronomy — the second pass, the readback; sittings — the merge, the checkpoints as they fall; small, later) kept current at every loop sitting and echoed in the reply;'),
])
patch(M + '/step9-exam-era.md', [
    ('⚠ THE LOOP step 7 (b) THE STEPPER (2026-09-14): A GENERATOR BEATS A THREAD',
     '⚠ THE LOOP step 7 (c) THE PORT (2026-09-14): THE PORT DECIDES NOTHING ABOUT THE INPUTS — a queue read once and validated at open (the registry\'s fields are a census, not a contract: an unknown field refused, a missing one warned); a world with inputs is ITS OWN WORLD — the audit against the base stops at the first input and the fork goes in the header; THE FIRE\'S LINES PRECEDE THE MARKER\'S OWN LINE (a hand-typed index corrected on the engine\'s order — the second time this sitting); AN INPUT\'S CITATION MOVES THE VERSE REACHED (filed for the inputs\' definition); THE LIST OF WHAT FINISHES THE LOOP LIVES IN THE MAP and is echoed at every loop sitting\'s close.\n'
     '⚠ THE LOOP step 7 (b) THE STEPPER (2026-09-14): A GENERATOR BEATS A THREAD'),
])

append(R + '/logic/pre_logic_methods_2026-07-28/RECOVERY_new_thread_2026-09-12.md', '''
## 22. ADDENDUM (2026-09-14, THE LOOP STEP 7 (c) THE PORT — the owner: "ok go c. keep up with what we need to do to finish this. go"; the state doc's COMPACTION POINT #173). THE LOOP THAT WAITS IS BUILT.

BUILT: THE_LOOP.md "Step 7 THE LOOP THAT WAITS — part (c) THE PORT: the design" + "As built" + "TO FINISH THE LOOP — THE LIST" (the box's (c)
ticked). D16 THE PORT IS A QUEUE, NEVER A PROMPT: World/journal/port/<queue>.yaml (tracked, primary) — `items:` {id, at, label, event{kind,
subject, case_source, the fields}}, read ONCE at open and validated (an unregistered kind, an unknown field, a bad position, a position already
passed by a session starting later: REFUSED, named; a missing registered field a WARNING — the registry's field list is a census, not a
contract); at every pause the items due enter in file order through World.submit — the one door — the EVENT line prov.unit 'port:<queue>' and
data.port {queue, id, label}; the queue file never rewritten. D17 A WORLD WITH INPUTS IS ITS OWN WORLD: the session journals whole under
cold_run_sequence/port@<queue>, audited against the base to the first input, THE FORK recorded (ordinal + item; the header {base, fork,
forked_by, queue, pending}); the base untouched; D9's appended form stays the cursor's. D18 THE ORDER OF A PAUSE: the queue first, then the
text's line; an unpositioned item at the first pause (the session's start or the left edge of --from); a positioned one at its verse's left
edge; one past the tape's end at the end, before the seal. THE CODE: World/step9/world_port.py (Port: load, validate, due, event_of, pending);
world_stepper.py (Stepper(queue=…), _enter() at every pause and at the end, the audit stopping at the fork, the report's inputs / fork /
forked_by, the header at close, --queue, the session's own source in the prints); world_journal._append_log's EVENT branch ('port:<queue>');
worldledger.Segment.write (the header's extra fields whenever given). No engine change. THE PRINTS: port_probes.py 0/9 → 8/9 → 9/9 (P5's
hand-typed index corrected on the engine's order: the fire's lines precede the marker's own line); step 9/9, live 7/7, journal 7/7, cursor
6/6; THE REAL SESSION `--from 'Num 27:1' --to 'Num 28:1' --by verse --queue World/journal/port/daughters.yaml --show custody`: 2 items at
Num 27:5, no warnings; the replay 3,221 audited; step 1 (27:1 with 27:1-4) audited; step 2 at the left edge of 27:5 — THE TWO INPUTS FIRST
(first_horn → holding_owed on the daughters at Num 27:8, seq 3226; second_horn → exempt = child_of_any_kind on the widow at Deut 25:5, seq 3228;
both law_zelophehad), then the text's 27:5 line (the custody, seq 3230), FORKED AT 3225 BY first_horn; step 3 (27:6-11) the custody closed;
stopped at the left edge of 28:1; sealed 3,233 lines in 1,497 blocks, the audit ok; the header {base, fork 3225, forked_by first_horn, queue
daughters, pending []}; askable under --world cold_run_sequence/port@daughters. THE TAPE AFTER: %s. A FINDING: the second horn's citation
(Deut 25:5) moved the engine's VERSE REACHED to Deuteronomy inside Numbers 27 — an input's citation moves the position the installation gate
reads; the port's position or the input's citation: the owner's, inside the inputs' definition (list item 7). LINTS 0 on every new and
changed file; every record at its baseline. THE FORMS: forms_numbers_walk/loop_2026-09-14/ (loop_design_c.md, write_port_records.py).

⚠ A STANDING DUTY FROM THIS SITTING: THE_LOOP.md "TO FINISH THE LOOP — THE LIST" is brought current at every loop sitting and echoed in the
reply at its close. THE LIST NOW (twelve): the owner's — 1 the inputs themselves, 6 time without a marker, 7 the position of an input; after
Deuteronomy — 2 the second pass (D2), 3 step 6 the readback (D12); sittings — 4 D7's merge, 5 the checkpoints as they fall (the stitcher);
small — 8 the cursor's lines live (the cursor may retire into the stepper), 12 the other worlds stepped; the design thread's — 9 the window
(CHRONICLE); later — 10 the interface, 11 a graded input. NEXT on the owner's word: one of the list's items (his three decisions first), or
THE NEXT BOOK (Deuteronomy, as #160), or the py_units gloss sitting. UNCOMMITTED since 08fa06e: this sitting's files and the post-commit notes;
commit only on "commit push" with the staging form of section 18 (the GitHub tool at /opt/homebrew/bin/gh).
''' % TAPE, '## 22. ADDENDUM (2026-09-14, THE LOOP STEP 7 (c)')

append(R + '/logic/pre_logic_methods_2026-07-28/PROMPT_continue_solo_era_2026-08-06.md', '''
═══ COMPACTION POINT #173 (2026-09-14 — written at the close of THE LOOP STEP 7 (c) THE PORT, the owner's "ok go c. keep up with what we need to do to finish this. go"; THE LOOP THAT WAITS IS BUILT; A CLEAN COMPACTION POINT) ═══
BUILT: THE_LOOP.md "Step 7 ... part (c) THE PORT: the design" + "As built" + "TO FINISH THE LOOP — THE LIST"; the box's (c) ticked. THREE DECISIONS (mine, on the measurements; the owner may overrule): D16 THE PORT IS A QUEUE, NEVER A PROMPT (World/journal/port/<queue>.yaml, tracked — read once at open and validated: an unregistered kind, an unknown field, a bad position, a position already passed REFUSED and named; a missing registered field a warning; the items due at each pause through World.submit in file order, the EVENT line prov.unit 'port:<queue>', data.port {queue, id, label}); D17 A WORLD WITH INPUTS IS ITS OWN WORLD (the session whole under cold_run_sequence/port@<queue>, audited against the base to the first input, forked there, the header {base, fork, forked_by, queue, pending}; the base untouched); D18 THE ORDER OF A PAUSE (the queue first, then the text; the first pause / the verse's left edge / the end). THE CODE: World/step9/world_port.py; world_stepper.py's --queue (_enter at every pause and the end; the audit stops at the fork; the report's inputs / fork / forked_by; the header at close); world_journal's EVENT branch; worldledger's header. No engine change.
THE PRINTS: port_probes.py 0/9 → 8/9 → 9/9 (P5's hand-typed index corrected on the engine's order — the fire's lines precede the marker's own line); step 9/9, live 7/7, journal 7/7, cursor 6/6; THE REAL SESSION over chapter 27 with World/journal/port/daughters.yaml (the two horns at Num 27:5): the replay 3,221 audited; the two inputs entered at the left edge of 27:5 before the text's line — the daughters' holding_owed at Num 27:8 (seq 3226), the widow's exempt = child_of_any_kind at Deut 25:5 (seq 3228), then the custody (seq 3230); FORKED AT 3225 BY first_horn; sealed 3,233 lines in 1,497 blocks, the audit ok; the header {base, fork 3225, forked_by first_horn, queue daughters, pending []}; askable under --world cold_run_sequence/port@daughters. THE TAPE AFTER: %s. A FINDING: an input's citation moves the engine's verse reached (Deut 25:5 inside Numbers 27) — list item 7. RUN unmoved; the hash 8b8fff1fa28953af untouched. Lints 0 on every new and changed file; the state doc 147; THE_WORLD 5; MEMORY.md 4; THE_STEPS 1.
THE RECORDS: THE_LOOP.md, THE_WORLD.md (the fourth 2026-09-14 entry), COMPILE_DEBT.md's loop box, THE_STEPS's loop section, THE_BRIEFING (the scoreboard + an entry), World/RESUME.md, memory (the-loop-ruling.md, MEMORY.md's loop line with the standing duty, step9-exam-era.md's lessons head), the recovery file's section 22; the forms in forms_numbers_walk/loop_2026-09-14/.
⚠ A STANDING DUTY: THE_LOOP.md "TO FINISH THE LOOP — THE LIST" (twelve items) brought current at every loop sitting and echoed in the reply — the owner's three (1 the inputs themselves; 6 time without a marker; 7 the position of an input), after Deuteronomy (2 the second pass; 3 the readback), sittings (4 D7's merge; 5 the checkpoints as they fall), small (8 the cursor's lines; 12 the other worlds), the design thread's (9 the window), later (10 the interface; 11 a graded input).
NEXT on the owner's word, ONE OF: an item of the list (his three decisions first — nothing on them moves before his word); THE NEXT BOOK (Deuteronomy, as #160); the py_units gloss sitting. UNCOMMITTED since 08fa06e: this sitting's files and the post-commit notes; commit only on "commit push" with the staging form (the GitHub tool at /opt/homebrew/bin/gh).
POST-COMPACTION REREADS (mandatory, first sitting): as #170's, plus THE_LOOP.md's step 7 (a), (b), (c) designs + as-builts and "TO FINISH THE LOOP — THE LIST", and the recovery file's sections 20-22 (read before any word on the loop).
''' % TAPE, '═══ COMPACTION POINT #173')
print('records written')
