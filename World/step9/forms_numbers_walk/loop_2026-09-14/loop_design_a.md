
## Step 7 THE LOOP THAT WAITS — part (a) WRITE AS YOU GO: the design (2026-09-14; the owner: "ok go 1" on the three-part
## recommendation of the section above; written AFTER the measurements and BEFORE the probes, the probes before the code — the loop's own order)

THE WORD AND THE FOUR CALLS: the owner's "ok go 1" opens the loop that waits, three parts one sitting each — (a) WRITE AS YOU GO
(this sitting), (b) THE STEPPER, (c) THE PORT. The four calls listed in the section above ride as recommended, each open to his
overruling: the three in that order; the grain of a step THE EVENT (measured below to be the engine's own atomic block); "current
state" the five views as they are, the entities, the installed laws and the checkpoints owed to (b); before Deuteronomy.

THE MEASUREMENTS (2026-09-14; the scripts in World/step9/forms_numbers_walk/loop_2026-09-14/ — loop_measure_mutation.py; the tape
timed; the index and file costs benchmarked; every number below from a print):
  1. THE TAPE: a full run 93 s wall, of which the running world's own run is 0.8 s and the module import 81.8 s (every runner's
     guards and probes at import). The four worlds' segments 3,362 / 3,362 / 3,358 / 3,362 lines; the index 20,049 rows over 8
     segments; the running world's ten classes: event 1,279, write 1,527, retro_write 12, timer_set 66, timer_fire 52,
     timer_cancel 0, marker 157, skip 0, row 148, close 121 (= 3,362).
  2. THE PAYLOADS MOVE AFTER THE ENGINE LOGS THEM — measured line by line on the running world with three snapshots of every log
     line: at append, at the end of the OUTERMOST ENGINE CALL (submit, marker, advance, close, row, cancel_timers returning at depth
     0 — THE BLOCK), and at the run's end (what the sink writes today):
       - INSIDE the block one key changes: EVENT.fired_by on 1,140 lines — the consumers are stamped as the daemons run, after the
         line is appended and before the call returns;
       - AFTER the block one key changes: `bound`, its RIGHT EDGE, closed by the next forward marker — EVENT 1,195, WRITE 1,391,
         TIMER-SET 50, TIMER-FIRE 37 lines; MARKER, CLOSE, ROW and RETRO-WRITE never move;
       - 26 lines differ from the masked run-end form because their bound was ALREADY CLOSED when sealed — {THE_26}.
     So: A LINE IS FINAL AT THE END OF ITS BLOCK, except its bound's right edge, which is a later marker's fact.
  3. NO READER OF THE JOURNAL READS `bound`: not world_journal.py, not run_views.sql, not the probe files (sequence_probes P4 and
     clock_probes read the IN-MEMORY event's bound; the tape's checkpoints C3c, C3c-literal and C9 test the in-memory interval —
     the engine's close of the shared list stays as it is). The ARCHITECTURE docs describe the bound (the design thread's).
  4. THE COSTS: 3,362 index inserts with a commit per line 1.55 s (per ten 0.11 s; one commit 0.01 s); 3,362 line appends with
     the file held open and flushed per line 0.01 s (opened and fsynced per line 0.12 s). A commit per line on four worlds is about
     six seconds on a ninety-three-second run — the grain is affordable at the line.
  5. THE FOURTEEN PENDING TIMERS at the tape's end (day 908,718): seven of Midian's purification (the third day 908,721 and the
     seventh 908,725, the corpse uncleanness of seven days — on the men of war and the captives, Num 31:19-20) and seven of the
     altar's musaf period timers (908,725 to 908,988; Num 28:1-29:39). The nearest due is three days past the tape's end and nothing
     walks the clock there — the open question "time without a marker" stays open, now with its list.

THE DECISION D14 — THE SEAL (this sitting's one design decision, taken on measurement 2; the owner may overrule): A JOURNAL LINE IS
SEALED AT THE END OF ITS BLOCK and never changes after. Its bound is written AS IT STOOD AT THE SEAL — [the last marker, null] for a
line sealed inside an open bound — and the right edge is THE NEXT FORWARD MARKER LINE'S DAY in the same segment: a DERIVED fact,
never written back, exactly as a ledger entry's close has been its own line since THE CLOSE LINE. This pays the debt THE CLOSE LINE
named ("the event's shared bound list kept by design" — a design sentence naming a mutation of the past): after this sitting nothing
in the journal moves after it is written. THE COST, said plainly: the base segments' bytes change ONCE (about 2,647 lines of the
running world lose a right edge that the marker line after them carries; the data is derived and gitignored); the RUN and REST
tuples count lines, not bytes, and do not move; the cursor's audit is re-run after the tape (the standing watch). The engine's
in-memory bound list keeps closing as before — the checkpoints read it.

THE DESIGN:
  (1) THE HOOK IN THE ENGINE — one additive construct: World.journal (None by default) and a decorator on the six entry points
      that, AFTER the call returns at depth 0 (in a `finally`, so a refusal mid-block still seals the lines logged before it),
      calls self.journal.flush(). The exam worlds attach nothing and pay nothing (D9). No verdict, no write, no count moves.
  (2) THE LIVE SINK — world_journal.LiveSink, attach(world, source, out_dir=None):
        the BODY FILE <segment>.live in the data dir — the segment's lines only, appended and flushed at every seal; the header
          is written at the seal of the run (the segment file as today: header + the same bytes; the body file removed);
        the SEGMENT in memory — worldledger.Segment, the chain computed per line as today; ONE conversion (_append_log, unchanged);
        the LIVE INDEX — the one database World/journal/data/world.sqlite (or the run's WORLD_JOURNAL_DIR): the events table and
          the five views as they are; at attach the table is built from every segment on disk if it is absent (a fresh checkout)
          and THIS SOURCE'S old rows are deleted; at every seal each new line is INSERTed with the row the rebuild makes and
          COMMITTED — the single writer is the sink, and the rebuild must reproduce it (the audit).
      flush(): the log's new lines (world.log[n:]) converted, chained, appended, inserted, committed. seal(): the header + the
      lines written as the segment file; the audit run; returns (path, lines, coerced) as sink() does. sink(world, source, out_dir)
      is kept for a world that ran WITHOUT a sink (the probes' small worlds): it attaches now and seals the whole log at once —
      a LATE SEAL, the bounds as they stand — so every old caller still works and says which form it got.
  (3) THE AUDIT, at every seal and inside the gate — RED on any miss:
        (i) the chain verifies from genesis over the sealed file;
        (ii) the lines equal the log's length, one journal line per log line;
        (iii) THE INDEPENDENT CONVERSION: the same log converted afresh at the run's end equals the sealed lines on EVERY field but
             the bound's right edge — the one named exception, its count printed (the lines whose bound closed after their seal);
        (iv) the index rebuilt from the sealed segment into a temporary database equals the live rows of that source, row for row,
             every column;
        (v) the gate's two processes stay byte-identical (segments and, new, the live rows).
  (4) THE DATABASE IS THE STATE: at any seal the events rows of the running source are exactly the lines sealed so far and the five
      views over them are current — `--ask` answers between blocks with nothing new to build. The run's closing reindex of the
      whole database is REPLACED by audit (iv) on the run's own sources; the L0-L2 layers and the older L3 sources stay as indexed.
  (5) THE CURSOR under the seal: run_to attaches a sink IN MEMORY (no file, no index — the audit's form); the replayed lines are
      sealed at their blocks; cursor_segment compares them to the base's prefix (byte-identical or refused, as before) and writes
      the appended segment from the lines after the fork — one sealing rule on both sides of the fork.
  (6) NOT BUILT HERE, owed to (b) and (c): the pause; the port; a bounds view (derivable from the marker lines; built if "current
      state" needs it); the checkpoints on the journal (printed lines today); the import cost (81.8 s) as the stepper's fixed price —
      the pause must live inside one process.

THE PROBES (World/step9/live_probes.py; written BEFORE the code and run to FAIL on the unchanged engine — every one a FAIL first):
  L1 THE BODY FILE IS LIVE: a probe world with a live sink; after each of three blocks (a marker, a submit that writes a debit, a
     submit whose daemon closes it) the body file holds exactly the lines sealed so far and its chain verifies from genesis.
  L2 THE INDEX IS LIVE: at the same three points the events rows for the source equal the lines so far, and run_ledger shows the
     debit OPEN after the second block and CLOSED after the third — the ask tool's answer between blocks.
  L3 THE SEAL'S FORM: the sealed EVENT line carries fired_by complete and its bound [x, null]; the marker line closing it follows
     with the right edge as its day; a timer fired inside a later marker's walk carries its bound closed (the 26's form).
  L4 THE SEAL AND THE AUDIT: seal() writes the segment (header + the same bytes), removes the body file, verify() passes, and the
     audit passes — lines = the log; the fresh conversion equal on every field but the right edge, with the count of closed-after
     lines printed; the rebuilt index equal to the live rows.
  L5 DETERMINISM THROUGH THE LIVE PATH: two live runs of one probe world in two directories are byte-identical (segments and rows).
  L6 THE CRASH-SAFE TRACE: a refusal raised inside a daemon mid-block leaves the lines sealed before it on disk, the body file's
     prefix verifying — the run's history survives the run.
  L7 THE EXAM WORLDS PAY NOTHING: a World with no journal logs as before — no attribute, no file, no row.
  After the code: journal_probes 7/7, cursor_probes 6/6 AFTER the tape is re-run (the standing watch), view_probes, installation
  probes, population_probes, sequence_probes, clock_probes as they stand; the tape 10/10; the journal gate GREEN with the audit
  lines; the register gate untouched (no compile); the sweep 57/57 in the background.

THE ORDER: this design → the probes to FAIL → the engine's hook → the sink and the audit → the runner's attach line (run_world) and
the cursor's → the tape run → the probes → the gates → the sweep → the records (this file's as-built and the table's row 7,
THE_WORLD.md, COMPILE_DEBT.md's box, THE_STEPS's loop section, THE_BRIEFING, RESUME, memory, the recovery file, the state doc).
