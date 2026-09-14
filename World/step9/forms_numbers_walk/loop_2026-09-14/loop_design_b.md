
## Step 7 THE LOOP THAT WAITS — part (b) THE STEPPER: the design (2026-09-14; the owner: "ok go b" after part (a)'s close and his question
## "is that a simulation?" — answered: the history never changes, the state changes with every line, and nothing yet WAITS; written AFTER the
## measurements and BEFORE the probes, the probes before the code — the loop's own order)

THE MEASUREMENTS (2026-09-14; the census by grep over the tape section of cold_run_sequence.py, lines 687-2316; part (a)'s prints):
  1. THE TAPE IS ONE ENGINE CALL PER LINE: 1,630 lines between the sentinels — 1,507 engine calls (w.submit 1,279, w.marker 157, w.close 71),
     118 comment lines, no multi-line call (0 lines end in a comma or a bracket); a marker's line carries its assert_ink and its M entry
     before the call; no advance, row, cancel or checkpoint call in the tape.
  2. THE CHECKPOINTS ARE NOT IN THE TAPE: they are computed in run() AFTER the tape from the marker table M and the finished world (c3() and
     the block at line 2641 on) — "the checkpoints as they fall" would be a rewrite of that block into the stitched tape (the stitcher's), OWED
     and named here; a pause shows the state, not the checkpoints.
  3. THE BLOCKS OF PART (a) ON THE RUNNING WORLD: 1,533 flushes that sealed lines = 1,507 tape lines + 26 marker walks whose advance() fired
     timers (the fires sealed by advance's own flush inside the marker's call). So a TAPE LINE is the natural step: the marker with the timers
     it fires is one line and one step; an event with its consequences is one line and one step; a close is one line and one step.
  4. THE COST: the import 81.8 s of a 93 s run; the running world's own run 0.8 s — the replay to any verse costs under a second, and a stepping
     session is ONE PROCESS (the import its fixed price, paid once).
  5. A THREAD WAS CONSIDERED AND REFUSED: the seal's flush is a seam where a worker thread could wait on a gate, but a paused thread can never
     stop BEFORE a line (it learns of a line after the engine ran it), needs a call-depth flag in the engine to make a marker one step, and
     brings threads into a deterministic instrument. A GENERATOR does all of it with no engine change (below).

THE DECISION D15 — THE TAPE AS A GENERATOR (this sitting's one design decision; the owner may overrule): the stitched tape's source is
transformed at load — every engine-call line is prefixed with `yield (<the verse of the call>, <the line's ordinal>); ` — and executed as a
GENERATOR: each next() runs exactly one tape line (one outermost engine call, the seal of part (a) writing its lines to disk and into the
database inside it) and then yields the verse of the NEXT call before running it. The pause is between two next() calls: no thread, no
event, no engine change; the world stands still, every line so far sealed, the database current. Because the generator yields BEFORE a
call, the stepper can stop at the LEFT EDGE of a verse exactly as the cursor does (the cursor's stop_before is not used — it aborts the
tape; the stepper resumes it). The transform is guarded: the yields must equal the calls counted (1,507 on today's tape) and the
transformed source must compile; the stitcher's one-call-per-line form (measurement 1) is the contract, asserted at every load.

THE DESIGN — World/step9/world_stepper.py (no runner's logic moves; the engine untouched; the journal untouched):
  (1) THE WORLD: built as run_to builds it (the registry map, every daemon, installation on the running setting, the creation epoch), the live
      sink of part (a) attached under ITS OWN SOURCE `cold_run_sequence/stepper` (the segment L3_run_cold_run_sequence_stepper.jsonl, the rows
      under that source) — the base run's rows and segment are never touched by a stepping session; a session that ends early seals a PARTIAL
      segment (a valid segment: its header counts its lines) and the audit of part (a) runs on it.
  (2) THE GENERATOR: transform(source_text) → the tape's function as a generator; the stepper reads the same tape section rest_world reads
      (between the sentinels), transforms it, executes it in the runner's namespace, and holds the generator.
  (3) THE STEP — step(by='call' | 'verse' | 'chapter' | 'marker' | 'day' | a verse address): next() until the criterion is met, then pause:
        call     one tape line;
        verse    every line at the current call's verse (the next line's verse differs);
        chapter  every line in the current call's (book, chapter);
        marker   through the next marker line (the date with the timers it fires);
        day      until the clock's day has moved (a marker that walked it);
        a verse  until the NEXT call's verse is at or after it — THE LEFT EDGE, the cursor's own position.
      from_verse at construction replays to that left edge with no pause (under a second). run() steps to the end. close() seals.
  (4) THE REPORT at every pause (the state, from the live database and the world): the step's ordinal; the lines run (their verses and
      kinds) and the lines sealed (the journal classes); the NEXT call's verse (the left edge the world stands at); the clock (the day, the
      creation date, the exodus-era date); the entities, the open entries, the pending timers, the docket's open custody; and on request
      (--show open | ledger <entity> | custody | timers) the rows read FROM THE DATABASE under the stepper's source through the five views —
      the database is the state, shown from the database.
  (5) THE AUDIT — THE REPLAY IS THE AUDIT, at every step: when the base segment of the running setting is on disk, every line the stepper
      seals must equal the base's line at the same ordinal (the sink's sealed event against the base's canon) — a difference REFUSES the
      session at that ordinal, named, exactly as the cursor is refused; a session run to the end leaves a segment whose lines are the base's
      byte for byte (the header names its own source). No base on disk: no audit, said so in every report.
  (6) THE COMMAND LINE: `python3 World/step9/world_stepper.py [--from <verse>] [--to <verse>] [--by call|verse|chapter|marker|day] [--steps N]
      [--show open|ledger <entity>|custody|timers] [--pause]` — prints a report per step; --pause waits for Enter between steps (a CONTROL
      word, never a data event — the port of part (c) is the only door for inputs; this is not a hand-input shell); without --to or --steps
      it runs to the end as a watch.
  (7) THE SEAM FOR (c) THE PORT: between two next() calls the loop will read its queue and submit what it finds through World.submit — the
      same one door — before the next tape line; the stepper's `between` hook is where the port will hang. Not built here.
  (8) NOT BUILT, owed: the checkpoints as they fall (measurement 2 — the stitcher's rewrite); time without a marker (the fourteen pending
      timers stand; the stepper never moves the clock); the window (CHRONICLE).

THE PROBES (World/step9/step_probes.py; written BEFORE the code and run to FAIL — every one a FAIL first, S1-S8; the probe tape a SOURCE
TEXT of six lines over live_probes' daemons, transformed like the real tape):
  S1 THE GENERATOR: transform(source) yields once per engine-call line, BEFORE the call, with the call's verse; the yields equal the calls
     (6); one next() runs exactly one call (the log grows by that call's lines and no more).
  S2 STEP BY CALL: six steps seal 1, 2, 2, 1, 3, 3 lines (a marker; a submit with a timer set; a submit with a debit; a marker; a marker
     whose walk fires the timer; a submit whose daemon closes the debit); at every pause the body file and the live rows hold exactly the
     lines so far; the seventh step reports the end; the segment sealed, the audit ok.
  S3 THE GRAINS: by 'verse' the two calls at Exod 19:5 are one step; by 'marker' the calls through each marker are one step; by 'day' a step
     ends when the clock moved; by the verse address 'Exod 24:1' the stepper stops at the LEFT EDGE — four lines run, the day 12, the next
     call Exod 24:1, nothing of it run.
  S4 FROM A VERSE: Stepper(from_verse='Exod 24:1') replays to the left edge with no pause; its first report shows the position, six lines
     sealed, and the debit OPEN in the live database under the stepper's source.
  S5 THE AUDIT: a base written by a straight run of the same probe tape through the live sink; a stepper with that base reports every step
     audited; a stepper over a CHANGED tape (one subject altered) is REFUSED at the step where they diverge, the ordinal named.
  S6 THE EARLY CLOSE: close() after two steps seals a partial segment of three lines, the audit ok, the body file gone, the base untouched,
     the live rows three.
  S7 THE STATE FROM THE DATABASE: at a pause the report carries the clock day, the verse reached, the next verse, the entities, the open
     entries and the pending timers; `ledger the_court` read from the live database under the stepper's source shows the debit OPEN after the
     third line and CLOSED (day 20) after the sixth.
  S8 THE REAL TAPE'S CONTRACT: the transform of cold_run_sequence's own tape section (read as text, never imported) compiles and yields
     exactly 1,507 times — 1,279 submits + 157 markers + 71 closes, the census of measurement 1.
  After the code: live_probes 7/7, journal 7/7, cursor 6/6 (the base unchanged by a stepping session), the others as they stand; the tape
  10/10; the journal gate GREEN; the sweep 57/57; THE REAL RUN: a session from the left edge of Num 27:1 stepped by verse through chapter 27
  and a session run to the end, its segment's lines the base's byte for byte.

THE ORDER: this design → the probes to FAIL → world_stepper.py → the probes → the real sessions → the gates → the sweep → the records.
