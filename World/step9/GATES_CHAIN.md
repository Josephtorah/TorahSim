# THE GATES CHAIN — the design of THE GATES CUT (2026-09-19)

The gates step of every compile sitting runs as ONE chain in the background (`sh World/step9/gates_chain.sh <out_dir>`; World/step9/gates_chain.sh;
the summary `<out_dir>/SUMMARY.txt` read once when the harness says the job ended — never polled). This file records what the chain is, what it
cost before the cut, why, and the six cuts with their honesty guards. The owner's words: "What is gate chain and why does it take so long" →
"Yes make that change. It's too long as it is" (2026-09-19, after sitting 6b's second chain). DISCUSSION IS NOT A RULING; this was a ruling.

## What the chain is

Twelve steps in the design's order, each its own process, each print in `<out_dir>/<step>.out`, a line per step in the summary:

| step | the command | what it proves |
|---|---|---|
| tape | `cold_run_sequence.py` | the three books replayed on one world, 10/10 checkpoints, THE REST; and now the SNAPSHOT saved |
| probes | the eleven suites (census installation readback register clock sequence view population journal cursor large_letter) | the machine's own tests, each suite N/N |
| daemon | `daemon_census.py` | every law a daemon, every function WRAPPED |
| dependency | `dependency_census.py` | every edge declared, no pointer demanded |
| build | `World/build_world.py` | the fold layer of the one database current |
| journal | `world_journal.py --gate` | the tape's journal byte-identical on two fresh replays; the twelve kinds; the row count |
| register | `register_census.py --strict` | every "as He commanded" seat DECLARED, debt 0, fails 0 |
| positions | `checkpoint_positions.py --jobs 8` | where every checkpoint falls on the tape (the table checkpoint_positions.yaml), by eight workers |
| checkpoint | `checkpoint_probes.py` | the table's own probes 7/7 |
| stamp | `world_journal.py --stamp <file>` | a digest of the live journal's rows, taken BEFORE the sweep |
| sweep | `run_cold_all.py --changed --jobs 8 --skip cold_run_sequence.py` | every runner's graded cells green |
| unmoved | `world_journal.py --unmoved <file>` | the live rows' digest after the sweep equals the stamp — the sweep wrote nothing on the live journal |

## What it cost, and why (measured 2026-09-19 on sitting 6b's second chain)

| step | seconds before | the cost's cause |
|---|---|---|
| tape | 156 | the import of the sixty-three runners (135.9 s measured alone) + the replay (1.7 s) + the checkpoints |
| probes | 609 | eleven suites in SEQUENCE, each paying the same import; the readback and register suites REPLAYING the world besides |
| daemon, dependency | 5 | — |
| build | 60 | the fold |
| journal | 316 | TWO fresh replays in SEQUENCE (two temp dirs), each paying the import |
| register | 141 | the import + a replay (and the gate REWROTE the live source rows on the way) |
| positions | 1562 | 169 pauses × the checkpoints block RE-PARSED from the 750 KB file at every pause (253 checkpoints) |
| checkpoint | 205 | the import + two run_to + a stepper |
| sweep | 2011 | sixty-three runners in SEQUENCE, the sequence runner (154 s) among them |
| journal2 | 315 | the two replays again |
| **total** | **~5,400 (ninety minutes)** | |

THE FINDING: the replay is cheap (two seconds); the IMPORT of the runners is dear (two minutes) and every step paid it, some more than once.
The running world pickles to 1.5 MB (daemons stripped) and reloads in one second. Sixteen CPUs stood idle while one worked.

## The six cuts

1. THE SNAPSHOT. The tape's run saves the running world after the replay (`WJ.save_snapshot(w)` in `cold_run_sequence.run()`; the file
   World/journal/data/running_world.pickle with a sidecar running_world.json; the daemons stripped — they are functions of the runners' modules and
   a reader needs none; the journal handle dropped). The sidecar carries `sources_key()` — a digest of every source the replay depends on (the sequence,
   the engine, the effects layer, the journal, the vocabularies and dispositions, the calendar and population parameters, the entity registry,
   the registries' yaml, and the DB's size and mtime). A reader (`register_census.running_world()` — the register gate, readback_probes,
   register_probes) loads the snapshot when its key is the CURRENT key, else replays and saves. `register_census.Ink` execs the sequence file's INK
   block instead of importing the module (the import was the cost). The write is atomic (tmp + os.replace).
   THE GUARD: a stale key is a miss — any moved source replays. The register gate no longer rewrites the live source rows.
2. THE PROBES IN PARALLEL. The eleven suites each in their own process at once, each print its own file (`<out_dir>/probe_<suite>.out`), the
   fractions gathered when all have ended. None writes the live journal: the readers take the snapshot, the cursor's and the journal suite's replays
   sink into temp dirs under their own source names, the steppers write their own sources. The checkpoint suite stays a step of its own (it needs the
   positions table).
3. THE JOURNAL GATE CONCURRENT. `world_journal.gate()` runs its two fresh replays at once (two threads, two temp dirs, two subprocesses). The
   comparison is what it was: byte-identical or refused.
4. THE POSITIONS BY WORKERS. The checkpoints block is parsed and compiled ONCE per process (`_cp_block`) — but the parse was not the cost:
   the block's execution is (~8 s at each of 169 pauses, 1,400 s in all). `checkpoint_positions.py --jobs N` measures the WHOLE table by N
   workers: each steps the whole tape in its own journal folder (the live base segment copied in, so the replay is still the audit) and asks
   the block at pause i where i mod N is its number; the parent merges the pauses (every pause asked by exactly one worker; the workers'
   verses, ordinals and days asserted equal) and takes the falls exactly as before. The table carries `jobs`. THE GUARD: none needed — the
   measure is always whole. (The incremental form by regions that this item first described was built, tested and STRUCK the same day — the
   record in "THE FORM THAT WAS STRUCK" below.)
5. THE SWEEP PARALLEL AND INCREMENTAL. `run_cold_all.py --jobs N` runs the runners N at a time (default min(8, cpu/2)); `--changed` grades only the
   runners whose digest moved since the stamp World/step9/sweep_stamp.json PLUS their transitive importers (the reverse import graph over
   `import cold_run_x` / `from cold_run_x`); `--skip cold_run_sequence.py` leaves the chain's own first step out of the sweep. THE GUARD: a SHARED
   piece moved (a vocabulary, a dispositions file, the calendar or population parameters, world_engine, effects_layer, compile_guards,
   world_journal, the entity registry) = FULL; no stamp = FULL; the stamp is written by a GREEN sweep only, and carries the mode, the digests and
   the graded count. The stamp is TRACKED in git: it is the record of the last green sweep, like the positions table.
6. THE UNMOVED CHECK. The second journal gate (D21's "upstream twice") proved one thing — that the sweep wrote nothing on the live journal. That is now
   proved directly: `--stamp` takes a digest of the live L3 rows (every source, every row) before the sweep; `--unmoved` compares after. The full
   gate still runs once (step 6). D21 stands: the tape's journal is checked upstream before anything else writes.

## What does not change

Every gate is still run; nothing is skipped on a guess. A full sweep is one flag away (`--full`); the positions table is always the whole measure. The
snapshot and the stamp are keyed on the SOURCES' digests, not on dates or names: a moved source is a miss, and a miss
falls back to the full work. The summary's form is the same; the records writer parses the same prints (the tape's 10/10, the daemon and
dependency counts, the journal's kinds and rows, the register's DECLARED/DEBT/FAILS, the positions' checkpoints over pauses, the sweep's N/N).

## The expected times (to be replaced by the first measured chain — see the AS RUN section below)

tape ~160 s (the import, once); probes ~150 s (the slowest suite); the small gates ~70 s; journal ~160 s; register ~5 s; positions: full ~200 s
(the parse once), incremental ~100 s; checkpoint ~200 s; stamp/unmoved ~2 s; sweep: full ~15 min at 8 jobs, incremental ~3 min (one runner
and its importers). About seventeen to twenty minutes in all against ninety. THE PREDICTION MISSED ON THE POSITIONS: the parse was never the
cost, the block's execution was (1,400 s at 169 pauses, unchanged by the cache) — which is why the workers replaced the regions (item 4).

## AS RUN — two chains after the cut (2026-09-19, the same day; ALL GREEN both times)

The first chain: everything measured in full (no sweep stamp yet; the positions by the old sequential measure). The second chain, run after the
positions measure was rebuilt by workers and with NOTHING MOVED: the steady state a compile sitting will see.

| step | seconds before | the first chain | the second chain | the second chain's last line |
|---|---|---|---|---|
| tape | 156 | 156 | 155 | THE THREE BOOKS RAN IN SEQUENCE ON ONE WORLD — the clock walked by the text's own stamps, the eras s |
| probes | 609 | 152 | 151 | large_letter: 6/6 |
| daemon | 3 | 3 | 3 | DAEMON GATE: every daemon declared and its watches verified; every kind and effect registered; every |
| dependency | 2 | 2 | 2 | DEPENDENCY GATE: every required edge and pointer dispositioned; every CALL live; every OWED on the d |
| build | 60 | 61 | 61 | ALL GREEN — the one database agrees with the fold |
| journal | 316 | 167 | 166 | GATE GREEN — the replay is the audit, the running world is the instrument |
| register | 141 | 2 | 2 | THE REGISTER GATE: GREEN |
| positions | 1562 | 1537 | 356 | THE FALLS: 253 checkpoints over 169 pauses in 357 s (8 workers); at pause 0 (before any line) 50; th |
| checkpoint | 205 | 211 | 205 | 7/7 probes |
| stamp | — | 0 | 1 | THE JOURNAL STAMPED: 9 sources, digest 94476de5dd71b49e… (/private/tmp/claude-501/-Users-Shared-Tora |
| sweep | 2011 | 311 | 5 | run_cold_all: NOTHING TO GRADE — the stamp stands: 62 runners green at 2026-09-19 10:50 (every sourc |
| unmoved | 315 | 1 | 0 | THE JOURNAL UNMOVED: the live rows' digest equals the stamp's (9 sources; stamped 2026-09-19 11:45)  |
| **total** | **5380 (89 min 40 s)** | **2603 (43 min 23 s)**, wall 43 min 13 s | **1107 (18 min 27 s)**, wall 17 min 49 s | |

THE FIRST CHAIN: the sweep FULL (no stamp at /Users/Shared/TorahSim/World/step9/sweep_stamp.json — the full sweep writes it) — no stamp existed, so every runner was graded (62 of 62 at 8 jobs; 6714 graded cells; 306 s) and the stamp
written (62 runners, 12 shared pieces); the positions by the old sequential measure (253 checkpoints over 169 pauses, 1,400 s of the block at 169
pauses). THE SECOND CHAIN: the sweep CHANGED (0 runner(s) moved since the stamp (2026-09-19 10:50): ; with their importers 0) — NOTHING TO GRADE; the positions by 8 workers, 253 checkpoints over 169 pauses in 357 s. Both chains:
the probes in parallel (census 224/224, clock 22/22, cursor 6/6, installation 6/6, journal 7/7, large_letter 6/6, population 9/9, readback 21/21, register 7/7, sequence 4/4, view 6/6); THE JOURNAL UNMOVED across the sweep (9 sources); the register gate from the snapshot (DECLARED 100, DEBT 0,
FAILS 0); every verdict the last chain before the cut gave — the tape 10/10 checkpoints, the daemon gate 68 daemons / 466 functions, the dependency gate 574 edges
/ 200 pointers, the journal gate 12 kinds / 9702 rows, the sweep whole, the positions whole.

THE STEADY STATE is the second chain: a compile sitting moves one runner (graded with its importers, a minute or two) and the positions are
always the whole measure by workers, so the chain stays near the second chain's total.

## THE FORM THAT WAS STRUCK — the incremental positions by regions (built, tested and struck 2026-09-19)

The design above first cut the positions table INCREMENTALLY: the block's statements split into REGIONS (a prefix's letters — CU — its cp calls
and the helper statements beside them), each region with a digest, the table's rows kept while their region, the block's preamble and the tape
prefix (the lines minus the newest runner's) stood, only the moved regions asked at every pause. THE TEST: CU's digest altered in the table and
`--incremental` run — seven of CU's nine rows came out NOT YET: the region's checkpoints read helper names bound in OTHER regions (a partial run
skipped their binders). A dependency closure was added (every earlier statement binding a name the region reads, transitively) and measured
statically: CU's closure is 429 of the block's 630 statements, CC's 336 — the block is one chained computation, and a "partial" run is nearly
the whole run. The form was struck the same day, with its regions, digests and guards; what remains is the parse-once cache (`_cp_block`) and
the WHOLE measure by N workers (D36). THE LESSON: an incremental cut is only as good as the independence it assumes — measure the dependency
before building the guard.
