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

## D38 — THE VERIFIED-IMPORT CACHE

THE RECORDER RUNS WITH THE CACHE OFF (THE DEUTERONOMY WALK 7b, 2026-09-19 — read at the first stitch of chapter 9's tape): seq_record.py captures every runner's
scene by instrumenting submit/advance/close and IMPORTING every cold_run_*.py — a module restored from the cache never runs its scene, so its submits never happen:
the first recording held 118 records of 2,983 and the stitcher wrote a 241-line tape into the sequence file (rerun native, 1,682 lines). Every instrument that
needs a scene to RUN (the recorder, the sweep, --full) runs under INK_CACHE=0; every instrument that reads a module's STATE (the probes, the callees' print, the
runner's own asserts) may take the cache. The rule stands beside the sweep's and --full's in this section.

THE NINETEENTH SLIP (THE DEUTERONOMY WALK 8b, 2026-09-20 — the cache's OWN ERROR REPORT): when a node raises on the cached path the cache reports which node
by `ast.get_source_segment(src, node)` — and `src`, the module's source text, had been REBOUND TO A MODULE a few lines above in the restore loop (an alias's home
module; a patch's source module), so the report itself crashed ('expected string or bytes-like object, got module') and masked the real error at the positions
table's eight workers. The two rebindings renamed srcm (patch_ink_cache_src_ch10.py); the report and the slow-node record read the source text again; FORM
unmoved. The positions table measured by FOUR workers (7b's way) — the eight-worker step has failed two sittings running (the watchdog at 7b, a cached-path raise
here) and four is its standing form until the eight are measured. The slips are nineteen.

THE EIGHTEENTH SLIP (the same sitting, found by C2 at the first chain): a runner that READS THE SEQUENCE FILE at import (`_SRC = open(HERE/cold_run_sequence.py)
.read()` — the INK block exec'd the stitcher's way) was keyed on its own source and the shared files alone, so after the tape was re-stitched the cached path
restored the OLD text of the sequence file (the parser block unchanged, the value not — C2 fell on `_SRC` in every such module, NOTHING set aside). THE KEY NOW
CARRIES the sequence file's digest for every module whose source names it (patch_ink_cache_key_ch9.py; FORM unmoved): those modules re-harvest once per tape
change, the others keep their blobs. The slips are eighteen. (2026-09-19, the same day; on the owner's "ok do it make it permanent")

THE MEASUREMENT THAT RULED IT: after the cut, the chain's long steps were still the ones that LOAD the sixty-three runners — the tape 155 s, the
probes 151 s, the journal gate 166 s, the checkpoint suite 205 s, each of the positions' eight workers a load — and a profile of the import
(stmt_profile.py, importtime.txt; the forms) put the load at 135 s, ALL of it the runners' own self-checks at module level (the whole-text scans,
the censuses, the asserts, the honest-pairing guards): good_land 14.3 s, joseph 9.0, hear_o_israel 8.8, obey_horeb 8.4, seven_nations 7.8 …
twenty runners over 2 s each; the replay of the world itself 1.7 s. The owner asked "Do we really need to rebuild everything on every run?" and
then, on the explanation of steps 8 and 9, ruled "ok do it make it permanent". THE LAW: a runner's checks run in full when its source or the
text it reads has moved, and always in the sweep; every other loader restores what the checks verified.

THE FORM — World/step9/ink_cache.py (its header the full statement; installed by world_engine.py, so every loader of the engine has it): a
meta-path finder for the cold_run_* modules. A MISS (the runner's source digest or the SHARED KEY moved — the text store, the shelf's files,
the snapshot store, the engine's modules, the registries — or no stamp) runs the module statement by statement and harvests, after EACH
statement, every name it bound or may have mutated, every name a function of the module may mutate (a static scan of its defs), every small
container, every container whose length moved, every object with attributes — each value that pickles into a content-addressed blob
(World/journal/data/ink_cache/, gitignored), recorded on that statement when its content changed; the other runners whose functions ran inside
the statement (a call tracer, one event per code object per statement) have their mutables re-examined and a change recorded as module::name;
an object that IS another name's live object is recorded as an alias, an element of a value that is one as a nested alias with its path; the
index is written only if nothing raised. A HIT walks the statements: one that only binds recorded names (an assignment, a loop, a with-block, a
branch), an assert, a print, a method call on a recorded name is SKIPPED and its names bound from the cache at that point — a fresh object for a
binding, IN PLACE for a name a call had mutated, the live object for an alias, the callee's container in place for a module::name entry, a name
passed to a call and unchanged left as it stands; everything else runs as written — imports, defs, classes, calls into modules, an alias
assignment, ANY BLOCK HOLDING AN IMPORT (the modules load in the full path's order), statements binding what does not pickle; the fixpoint
un-skips a skipped statement binding a name some running statement reads without a recorded value. INK_CACHE=0 turns it off for a process.

THE HONESTY GUARDS: (1) the sweep (run_cold_all.py) runs every runner with INK_CACHE=0 — the checks in full every time it grades; (2) the chain's
--full sets INK_CACHE=0 for every step; (3) THE PROBE ink_cache_probes.py, in the chain's probes step, imports the whole engine twice in two fresh
processes — full and cached — and asserts EIGHT things: C1 the same runners; C2 every picklable module value equal in canonical form, NOTHING SET
ASIDE; C3 no name lost; C4 the daemons by module and name in order; C5 the registry map; C6 the same sharing groups (no alias gained or lost);
C7 the cached load at least three times faster; C8 the engine's own modules (world_engine, effects_layer, events_layer, compile_guards,
world_journal) hold the same state — no registration lost to a restored statement; (4) a stamp is written only by an import that raised
nothing; (5) a cached-path statement that raises names the module, the line and the values it read, and says to run INK_CACHE=0.

AS BUILT — MEASURED BY THE PROBE: the full load 169 s (two processes: the import and the sequence's own load), the harvest on a cold cache 211 s
(the first load after a clear, or after a shared piece moved), the cached load 35 s; 7,542 statements restored and 2,386 run (the slowest run
pre_sinai's with-block 1.7 s, incense_shekel's 1.1 s — the blocks holding imports); about 4,600 blobs, 41 MB. THE PROBE 8/8 on its last run; the
tape 10/10 through the cache with the same print. THE SEVENTEEN SLIPS, each found by the probe or by the engine refusing on the cached path, and
each a rule now: 1. comprehension variables read as bound names (KeyError 'kv' on the cached path) — the walker skips comprehension, lambda and def scopes. 2. a def's locals read as bound names (NameError 'n') — a def binds its own name only. 3. the module's FINAL state harvested for a name bound twice (mishpatim_3's `failed`) — the harvest is per statement, each name's value AS OF that statement. 4. one empty list shared by every runner (foreign trails in the zero-report exits) — a fresh object for every binding. 5. a mutation through an attribute or subscript chain missed (pre_sinai's TOK empty) — the base of the chain is the touched name. 6. two statements on one line collided by line number (balak's PLENE_KIN lost) — the index is by statement position. 7. a touched name that does not pickle (a connection) forced the statement to run — only recorded names are restore targets. 8. the probe's byte compare tripped by the hash seed's set order — a canonical form (sets and dicts sorted, objects by class and attributes). 9. the probe timed a cold harvest as the cached load — the warm load first, the hit timed. 10. the probe's pickle bytes memoize repeated objects and two processes intern strings differently (fifty-four scene worlds 'differed') — the hash over the canonical form's TEXT. 11. a name passed to a call and unchanged was restored fresh, breaking every alias (seventeen sharing groups lost: erection's VS_E29 is vestments' E29_ORDER) — recorded as KEPT, and an object that is another name's live object recorded as an ALIAS the cached path binds. 12. a length heuristic missed a same-length change (mishpatim's counter, a trail cleared and refilled) — the static scan of every name a function of the module may mutate, re-examined after every statement; every small container too. 13. a callee's trail mutated by the CALLER's statement (the residue of the last caller: twenty-one runners' P) — invisible to the caller's source: the call tracer (sys.monitoring, one event per code object per statement) names the runners whose functions ran, their mutables re-examined, a change recorded as module::name and restored IN PLACE. 14. a self-test's result tuple holding the callee's trail BY REFERENCE (clocks' `_r`, korach's V5_ASHAM) — nested aliases with their paths, patched into the restored value. 15. a with-block holding the imports SKIPPED (pre_sinai's) — the modules loaded in another order than the full path's, so the calendar's trail and the family alias came out different — ANY BLOCK HOLDING AN IMPORT RUNS. 16. the tracer's set clobbered by the whole harvests an import nests inside one statement — a stack of sets, each level merged upward on exit. 17. the probe's lost-name check flagged a case table of functions (tzav's CASES) the fixpoint rightly dropped — the check on picklable names.

THE THIRD CHAIN (AS RUN, with the cache in place; world_engine.py moved, so the sweep FULL): the tape 27 s (against 155 before the cache), the probes 237 s (the cache probe inside them), the daemon and dependency gates 5 s, build 61 s, the journal gate 34 s (against 166), the register gate 2 s, the positions 229 s (eight workers, each a cached load), the checkpoint suite 75 s (against 205), the sweep 312 s (the stamp written: /Users/Shared/TorahSim/World/step9/sweep_stamp.json (62 runners, 12 shared pieces)), the unmoved check 1 s — THE TOTAL 983 s (16 min 23 s) against 18 min 27 s before the cache and ninety minutes before the cut; every verdict the same.

THE STEADY STATE: a chain of a compile sitting now pays the load only where the checks must run — the moved runner's own harvest (its miss, once)
and the sweep (always full, eight at a time, only the moved runners and their importers); every other step loads in about half a minute.

THE LESSONS: A CACHE'S PROBE IS THE CACHE — the definition of "the same" was made strict eight times, and each time it found a slip the tape's
10/10 had not (the tape reads what a case needs; the probe reads everything); THE RESIDUE A CALLEE LEAVES IS PART OF THE STATE — a trail, a counter,
a returned reference; THE ORDER OF THE IMPORTS IS PART OF THE STATE; PICKLE BYTES ARE NOT THE STATE (a memo, an interning) — compare the canonical
form's text; A TOUCHED NAME IS KEPT, A BOUND NAME IS FRESH, AN ALIAS IS THE LIVE OBJECT; THE FULL PATH IS ALWAYS ONE VARIABLE AWAY (INK_CACHE=0).

## THE CACHE LAW (owner-ruled 2026-09-20; COST_AUDIT_2026-09-20.md)
The chain's minutes cost nothing; the WAIT across them on a big context does — the prompt cache dies at five minutes and the next call re-writes the whole context (169 such re-writes were a third of nine days' bill). So the chain is LAUNCHED IN THE BACKGROUND AT THE END OF ITS RUN, with its readers already written (the records writer, the forms copier, the message extender parse its prints); the clean point is written; the owner compacts; THE TAIL — a small run — reads the SUMMARY once, files any demand, reruns `--from` the step (a wait on a small context is cheap), runs the writers. The positions table by eight workers is killed by the session's memory watchdog on this machine (7b, 9b): measure it by four (`checkpoint_positions.py --jobs 4`) outside the chain and resume `--from checkpoint`.
