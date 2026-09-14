
## Step 7 THE LOOP THAT WAITS — part (c) THE PORT: the design (2026-09-14; the owner: "ok go c. keep up with what we need to do to
## finish this. go"; written AFTER the measurements and BEFORE the probes, the probes before the code — the loop's own order)

THE OWNER'S FRAME (section 19 of the recovery file, his words): no hand inputs; the data from a second or third pass, maybe self-made;
"we will decide what those are later". So THE PORT DECIDES NOTHING ABOUT WHAT THE INPUTS ARE. It is the DOOR and the WAITING: a queue
outside the code, read at the pause of part (b), every item entering through World.submit — the one door — and journaled like any line.
The text is the first producer: the tape's own lines are the port's default input, taken whenever the queue holds nothing due.

THE MEASUREMENTS (2026-09-14):
  1. THE INPUT FORM THAT EXISTS: World/step9/scenarios.yaml (step 5; primary in git) — an entry has a cursor verse and a list of events
     (a registered CASE kind, a subject, the fields the daemon reads, a case_source, a label); cold_run_sequence --cursor submits them
     through world_journal.scenario, which marks the EVENT line prov.unit 'scenario'. The port's item is that shape with a position.
  2. THE ONE DOOR REFUSES UNREGISTERED KINDS: World.submit calls events_layer.validate — an unregistered kind is a SystemExit before
     any line is logged. The registry carries a `fields` list per kind, HARVESTED from what the tape submitted (a census, not a
     contract): estate_claimed's list is decedent, survivors, claimant, claimant_degree, property, scenario — the last a scenario's
     own mark. So the port refuses an UNKNOWN field (a misspelling) and prints a registered field the item lacks as a warning; the
     daemon's own read is the honest failure, at submit, on the tape.
  3. THE PAUSE OF PART (b) IS THE SEAM: the stepper's step loop stands before each tape call with the NEXT call's verse known (the
     generator yields it) — an item positioned at a verse can enter at that verse's left edge exactly, before the tape's own line.
  4. THE AUDIT OF (b) CANNOT SURVIVE AN INPUT: an input changes the future (a timer it sets fires at a later marker; an entry it opens is
     what a later close finds), so from the first input on the session's lines are no longer the base's — a world with inputs is a
     NEW WORLD. The prefix up to the first input is still the base's, byte for byte.
  5. THE JOURNAL'S HEADER writes its extra fields only on an appended segment (worldledger.Segment.write: `if self.start_chain`); a
     whole-world segment that forks from the base needs the fields without a start chain — a one-line change in worldledger.

THE DECISIONS (mine, on the measurements; the owner may overrule each):
  D16 THE PORT IS A QUEUE, NEVER A PROMPT — a file of items (YAML: id, at, label, event{kind, subject, case_source, the fields}), read
      ONCE when the session opens and validated then (an unregistered kind, an unknown field, a bad position, a position already passed
      by a session starting later: REFUSED at open, named); at every pause the items DUE enter in file order through World.submit; an
      item's EVENT line carries prov.unit 'port:<queue>' and data.port {queue, id, label}; the queue file is never rewritten — the
      journal records what entered. Nothing is typed at a prompt; a program or a hand may write the file, the port cannot tell and
      does not care. --pause of part (b) stays a control word.
  D17 A WORLD WITH INPUTS IS ITS OWN WORLD — the session journals WHOLE under the queue's name (source cold_run_sequence/port@<queue>;
      the segment L3_run_cold_run_sequence_port_<queue>.jsonl; every line from Gen 1:5 on, the chain from genesis), its header naming
      the base and THE FORK (the ordinal of the first input's line); the prefix up to the fork audited against the base at every call
      as in (b); after the fork no audit — the report says "forked at ordinal N by item <id>"; the base is never touched; D9's appended
      form stays the cursor's. The database then holds each world whole and askable under its own name (--world).
  D18 THE ORDER OF A PAUSE — the queue first, then the text: at every pause the items due at that position enter in file order, then the
      next tape line runs; an item with no position enters at the FIRST pause of the session (the session's start, or the left edge of
      --from); an item positioned at a verse enters at that verse's left edge; an item positioned past the tape's last verse, or with
      no position and queued after the text ended, enters at THE END — the end of the text is a pause too, before the seal.

THE DESIGN — World/step9/world_port.py + the stepper's hooks (no engine change; two one-line changes outside it):
  (1) THE QUEUE FILE: World/journal/port/<queue>.yaml (tracked — an input is PRIMARY, as scenarios.yaml is; the folder new) — `items:` a
      list of {id, at (a verse or null), label, event {kind, subject, case_source, ...the fields}}. The probe queues live in temp dirs.
  (2) class Port(path): load, validate (measurement 2), due(next_key, at_end) → the items to submit now, in file order; consumed ids.
  (3) THE STEPPER TAKES A QUEUE: Stepper(queue=path) → the source cold_run_sequence/port@<name>; before every tape call and at the end,
      the due items are submitted (each a block: sealed by (a), a step's report lists them under `inputs`); the audit runs until the
      first input's line, then records the fork; the seal writes the header {base, fork, forked_by, queue}; --queue on the command line.
  (4) THE JOURNAL: _append_log's EVENT branch marks a port item prov.unit 'port:<queue>' (beside 'scenario' and 'tape'); worldledger
      writes the header's extra fields whenever given.
  (5) THE TEXT THE FIRST PRODUCER: a session with no queue is the stepper's plain session — the same loop, the tape its only input, the
      segment the base's body byte for byte (the probe of (b) still holds).
  (6) NOT BUILT, owed: what the inputs ARE (the owner's decision, later); a second pass writing a queue (the pass's own sitting); the
      grading of an input's answer against an oracle (scenarios do that; the port only opens the door); the interface over the database.

THE PROBES (World/step9/port_probes.py; written BEFORE the code and run to FAIL — every one a FAIL first; the probe tape and daemons of
step_probes and live_probes; the queues written into temp dirs):
  P1 THE QUEUE READS AND REFUSES: a queue of two items loads with their positions; an unregistered kind is REFUSED at open, named; an
     unknown field is REFUSED, named; a bad position is REFUSED; a registered field the item lacks is a printed warning, not a refusal.
  P2 THE ONE DOOR: an item with no position enters at the first pause through World.submit — the daemon fires, its lines are sealed
     (event + the write) in the session's segment and rows, the EVENT line prov.unit 'port:<queue>' and data.port {queue, id, label}.
  P3 THE POSITION: an item at 'Exod 24:1' enters at the left edge of Exod 24:1 — after the tape's fourth line (19:16) and before its
     fifth (24:1) in the sealed order; a session started with --from past the item's verse REFUSES the queue at open, named.
  P4 THE FORK: the prefix before the first input is audited against the base (audited: yes at those steps); from the input on the report
     says forked, naming the ordinal and the item; the sealed header carries base, fork, forked_by and queue.
  P5 THE FUTURE CHANGES: an item that sets a timer (installation_commanded through the port at the first pause) fires at the later
     marker — the session seals MORE lines than the base and is not refused (the audit stopped at the fork).
  P6 DETERMINISM: two sessions over the same queue in two directories seal byte-identical segments and identical rows.
  P7 THE END IS A PAUSE: an item positioned past the tape's last verse enters after the last tape line and before the seal; the last
     report lists it under inputs; the segment's last lines are its.
  P8 THE TEXT ALONE: a session with no queue through the same loop seals the base's body byte for byte (the stepper's contract kept).
  P9 THE ORDER: at one pause with two items due and a tape line, the sealed order is item 1, item 2, then the tape line.
  After the code: step_probes 9/9, live_probes 7/7, journal_probes 7/7, cursor_probes 6/6 (the base untouched); THE REAL SESSION: a queue
  with the daughters' first horn (scenarios.yaml's estate_claimed, positioned at 'Num 27:5') run `--from 'Num 27:1' --to 'Num 28:1'
  --by verse --queue World/journal/port/daughters.yaml`: the item enters at the left edge of 27:5 after the plea and before the
  judgment, the daemon's answer on the ledger, the session forked at that ordinal, sealed under its own name; the tape 10/10 after.

TO FINISH THE LOOP — THE LIST (the owner, 2026-09-14: "keep up with what we need to do to finish this"; kept current at every loop sitting,
the section below this design's as-built; echoed in memory).

THE ORDER: this design → the probes to FAIL → world_port.py, the stepper's hooks, the two one-line changes → the probes → the real session
→ the tape → the records, with the list.
