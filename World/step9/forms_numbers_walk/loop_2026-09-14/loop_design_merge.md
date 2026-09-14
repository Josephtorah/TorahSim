
## D7'S MERGE — ONE DATABASE: the design (2026-09-14; the owner: "ok go the merge" — item 4 of TO FINISH THE LOOP; decided in principle 2026-09-09
## as D7 with D10; written AFTER the measurements and BEFORE the probes, the probes before the code — the loop's own order)

THE MEASUREMENTS (2026-09-14):
  1. TWO DATABASE FILES. World/world.sqlite (2 MB, 2026-09-08; gitignored) is the reading era's model: sixteen tables projected from
     corpus_world.fold() by World/build_world.py (278 lines), reconciled against the fold on nine counts and the state hash, asked by
     World/ask.py (names, called, at, open, career, who, entities, sql) and replayed slowly by World/run_genesis.py (the teaching run,
     writing a narration table). <world-link> is a symlink to the repo's World folder. World/journal/data/world.sqlite is the
     journal's index over every segment: L0 scripture (one row per operator), L1 structure, L2 cases, L3 the runs.
  2. THE JOURNAL'S READING LAYERS ARE STALE AND ARE THE AUGUST TREE. World/journal/build_world.py (541 lines) reads the frozen units
     through corpus_world and writes L0 (scripture.op) and L1 (the August tree model: node.born, partition.split, edge.insert, name.set…)
     with a twenty-one-line checklist. Built 2026-09-09 from 163 units: L0 4,517, L1 2,041. Run today into a temporary folder on the
     210 units: L0 4,902, L1 2,426, 2,033 nodes (37 unclassified), and the checklist FAILS four lines (the roots at Gen 1:1, the garden
     inside Eden, the ark's slots, the forming/filling symmetry) — the same four as on 2026-09-09; D10 retires this tree at the merge. Its
     index step drops the events table and indexes its own two segments alone — run against the data folder it would erase the runs'
     rows until the next reindex.
  3. THE FOLD IS THE READING'S TRUTH. corpus_world.fold(write=False) takes 29 s and yields ten lists: units 210, facts 1,809, events 557
     (each with its themes), demands 341 (191 open), mentions 1,167 (273 entities; roles agent 461, speaker 341, presupposed 162, install
     98, named 69, assigned / blesser / blessee 12 each), names 81, standing 2,163 (WITNESS_READ 1,770, WITNESS_STATE 116, STATUTE 75,
     HANDLER 64 …), tests 14, checkpoints 210, ledger 6 (the creation days); the state hash 8b8fff1fa28953af — the numbers
     logic/corpus/CORPUS_TRUTH.py pins as tripwires. The World folder's tables are exactly these lists plus four DERIVED ones (refs — the
     spine of distinct verses in canonical order; entities — first mention and weights; relations — events × themes, names, demands;
     entity_state — names with validity ranges) and event_themes.
  4. WHO READS WHAT. ask.py reads refs, mentions, facts, events, demands, standing, relations, entity_state, entities. Nothing in
     World/step9 reads World/world.sqlite; the run layer's tools read the journal's index. The board mockup read the August tree's
     node.born rows — the births it wants are the fold's first mentions.

THE DECISIONS (mine, on the measurements; the owner may overrule each):
  D19 THE FOLD IS THE STRUCTURE LAYER. The journal's L1 becomes THE FOLD — one row per item of the fold's ten lists, the kinds fold.unit,
      fold.fact, fold.event, fold.demand, fold.mention, fold.name, fold.standing, fold.test, fold.checkpoint, fold.ledger, and one row per
      verse of the spine, fold.ref (the ordinal computed once, deterministically); each row's data the item as the fold holds it, its
      prov {unit, ref}, its op the operator's ordinal; the segment L1_fold.jsonl, its header carrying the fold's counts and the state
      hash. The August tree (L1_structure.jsonl, world_tree.json, the checklist) is RETIRED as D10 ruled; its kinds keep their register
      entries marked retired. L0 (the operators) stays as it is, rebuilt from today's units.
  D20 THE OLD TABLES ARE VIEWS WITH THEIR OLD NAMES. World/journal/fold_views.sql creates, over the events table's fold rows, the
      views refs, units, facts, events, event_themes, demands, mentions, names, standing, tests, checkpoints, entities, relations and
      entity_state with the columns World/schema.sql gave them — so World/ask.py runs unchanged but for its path, which becomes the
      journal's index. World/world.sqlite is deleted; World/run_genesis.py is RETIRED with a guard (the loop's stepper is the player now);
      World/schema.sql stays as the record of the columns the views keep.
  D21 THE GATE MOVES UPSTREAM, TWICE. (a) World/build_world.py becomes the merge's entry: build the fold layer, reindex the whole journal,
      create the views, RECONCILE the views against a fresh fold on the nine counts and the hash (the old reconcile, now over the journal)
      — and `--check` reconciles alone. (b) The journal gate (world_journal.py --gate) reads the fold layer's header and refuses the index
      when the header's hash and counts differ from CORPUS_TRUTH's pinned tripwires or from the index's own rows — no refold inside the
      gate, the corpus gate's literals the reference. A frozen unit moves the hash; the gate then says "the fold layer is stale — run
      World/build_world.py" until it is rebuilt.

THE DESIGN — the code, no engine, runner or unit change:
  (1) World/journal/build_world.py rewritten: L0 as now; L1 the fold (D19) with the spine; no checklist; no index step of its own (the
      index is world_journal's, over every segment); the determinism self-test kept over both segments.
  (2) World/journal/fold_views.sql — the fourteen views (D20); world_journal.views() creates them beside the five run views at every
      reindex and at every attach; entities' births for the board = the entities view's first mention.
  (3) World/build_world.py rewritten as the entry (D21 a): build → reindex → views → reconcile; `--check`.
  (4) World/ask.py: the path; World/run_genesis.py: the retirement guard; the register: fold.* kinds added before first use, the August
      kinds marked retired; World/journal/data: L1_structure.jsonl and world_tree.json removed; World/world.sqlite removed.
  (5) world_journal.py --gate: the fold layer's header against CORPUS_TRUTH's literals and the index's counts (D21 b).
  (6) The board's births come from the entities view (a note in the mockup's generator; the mockup itself stands as drawn).

THE PROBES (World/step9/merge_probes.py; written BEFORE the code and run to FAIL — every one a FAIL first; one build into a temporary folder
shared by the probes, the fold's 29 s paid once):
  M1 THE FOLD LAYER: the build writes L0 and L1_fold.jsonl; the L1 rows per kind equal the fold's list lengths (units 210, facts 1,809,
     events 557, demands 341, mentions 1,167, names 81, standing 2,163, tests 14, checkpoints 210, ledger 6) plus one fold.ref per distinct
     verse; the header carries the counts and the hash 8b8fff1fa28953af; every row's data equals its fold item.
  M2 DETERMINISM: a second build in a second process is byte-identical on both segments.
  M3 THE VIEWS: over an index of the two segments the fourteen views exist and the old reconcile passes — nine counts and the hash.
  M4 THE GATE: the header's hash equals CORPUS_TRUTH's pinned hash and its counts the pinned counts; a header with another hash is refused.
  M5 THE ASK TOOL: ask.py's `at`, `open`, `who`, `entities`, `called` run over the index and answer (rows, no error).
  M6 THE RUNS UNTOUCHED: an index over the fold's two segments and one L3 segment holds every L3 row and the five run views MATCH.
  M7 THE AUGUST TREE RETIRED: the build leaves no L1_structure.jsonl and no world_tree.json; the register marks the August kinds retired.
  M8 THE BIRTHS: the entities view gives the heavens and the earth their first mention at Gen.1.1 and light at Gen.1.3.
  After the code: the real build into the data folder; the tape 10/10; the journal gate GREEN with its new fold line; live 7/7, step 9/9,
  port 9/9, cursor 6/6; `World/ask.py at Gen.30.24` and `open Gen.30.24` answering over the one database; the sweep 57/57.

THE ORDER: this design → the probes to FAIL → the code → the real build → the gates → the records (the list's item 4 ticked; the World
folder's README and RESUME; the recovery file; the state doc).
