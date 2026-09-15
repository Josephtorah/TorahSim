#!/usr/bin/env python3
"""write_merge_records.py — D7'S MERGE: the records at the close (2026-09-14). Every anchor asserted once; idempotent.
argv[1] = the journal gate's line, argv[2] = the probes' line (both from prints)."""
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

def prepend(path, text, marker):
    t = open(path, encoding='utf-8').read()
    if marker in t:
        print('%s: already prepended' % path.split('/')[-1]); return
    open(path, 'w', encoding='utf-8').write(text + t)
    print('%s: prepended %d chars' % (path.split('/')[-1], len(text)))

R = _ROOT
M = '<memory>'
GATE = sys.argv[1] if len(sys.argv) > 1 else '{GATE}'
PROBES = sys.argv[2] if len(sys.argv) > 2 else '{PROBES}'

ASBUILT = '''
## As built — D7'S MERGE, ONE DATABASE (2026-09-14, the same sitting; the owner: "ok go the merge"; the design above first, the probes to FAIL
## 0/8, then the code in six files, then 8/8 after four probe corrections on the tool's and the registry's own forms)

THE PROBES FIRST: World/step9/merge_probes.py M1-M8 written from the design and run on the unchanged tree — 0/8; after the code 4/8, then
6/8, then 8/8 — every miss the probe's own: a hand-derived kind key ("standin" for standing — the builder's own map used instead), the
design's one named exception (`fold_events`, since `events` is the journal's table) missing from the probe's list of views, a who-span
lacking the book on both sides (the tool splits on the dash; its own docstring's example lacks it), and the earth's id typed as its token
(the registry maps aretz to the_earth; the heavens keep their token). No code changed for a probe.
THE CODE: World/journal/build_world.py rewritten (L0 the operators as before; L1 THE FOLD — 6,558 items of the ten lists, 3,015 fold.ref
rows of the spine, one fold.meta; the header with the counts and the hash; the August files removed; no index step; the determinism
self-test kept); World/journal/fold_views.sql (the fourteen views + meta, with the old columns; `fold_events` the one renamed view;
entities, relations, entity_state and event_themes computed as views with window functions and json_each); World/build_world.py
rewritten as the merge's entry (build → reindex → views → reconcile; --check; World/world.sqlite deleted); World/ask.py (the path, the one
view name); World/run_genesis.py RETIRED with a guard; World/journal/registers/event_kinds.yaml (12 fold kinds added before first use; the
22 August L1 kinds marked retired); World/step9/world_journal.py (views() runs the fold views beside the run views at every reindex and
attach; pinned_truth() reads CORPUS_TRUTH's literals; fold_gate(); --gate prints the fold layer's line). No engine, runner or unit change.
THE REAL MERGE (`python3 World/build_world.py`, one run): the fold 29 s; L0 4,902 operators; L1 9,574 rows; the index 31,204 rows over 10
segments; the fourteen fold views and the five run views created; World/world.sqlite retired (deleted); THE RECONCILIATION over the views
against a fresh fold ALL GREEN — units 210, facts 1,809, events 557, demands 341, open demands 191, mentions 1,167, names 81, standing 2,163,
tests 14, the state hash 8b8fff1fa28953af. The data folder holds L0, L1_fold, L2, the L3 segments and the one world.sqlite (15.6 MB);
L1_structure.jsonl and world_tree.json are gone.
THE ONE DATABASE ASKED (World/ask.py over World/journal/data/world.sqlite): `at Gen.30.24` — 216 entities known, 736 facts standing, 507
events so far, 153 demands raised, 593 standing law, two demands outstanding (Rachel's at 30:3 and 30:14); `entities` — God 216 mentions,
Abraham 104, Noah 46; `called jacob` — yaaqov from Gen.25.26, yisrael from Gen.35.10, still. The run's tool beside it: `--ask population
reuben` 11 rows. run_genesis.py answers with its retirement.
THE GATE: %s.
THE PROBES AFTER: %s.
WHAT THE DATABASE IS NOW: one file, World/journal/data/world.sqlite, four layers — the operators, the fold (what exists and what the
reading found), the cases, the runs (what happened) — and nineteen views over them; every layer rebuilt from its segments, the fold layer
proven against a fresh fold by the entry and against the pinned truth by the gate; a frozen unit moves the hash and the gate says the layer
is stale until it is rebuilt. The board's births come from the entities view.
OBSERVED, not this sitting's: a stray body file L3_run_cold_run_sequence_stepper.jsonl.live in the data folder — a stepping session that
died mid-run (the owner's own run in a runner without a keyboard); the design's trace, harmless; the next session with that source
overwrites it.
LESSONS: THE VIEW MAY NOT WEAR THE TABLE'S NAME (`events` is the journal's — the fold's events are `fold_events`; the design named the
exception and the probe learned it); A PROBE'S EXPECTATION FROM A TOOL'S OWN DOCSTRING IS STILL A HAND-TYPED CLAIM (the who-span);
THE REGISTRY'S ID IS NOT THE TOKEN (the_earth, not aretz); A DERIVED KEY IS THE BUILDER'S MAP, NEVER A SLICE (standing[:-1]);
A COMMENT INSIDE A BRACKET SWALLOWS THE LINE (twice — write the comment after the closing bracket).
''' % (GATE, PROBES)
patch(R + '/World/step9/THE_LOOP.md', [
    ("  4. D7'S MERGE — one database: the World folder's corpus world (the reading era's 557 events, World/world.sqlite) as a journal layer, its\n     tables views over the journal, the reconciliation gate upstream; the August tree retired with it (D10). A SITTING.\n",
     "  4. D7'S MERGE — one database: the World folder's corpus world (the reading era's 557 events, World/world.sqlite) as a journal layer, its\n     tables views over the journal, the reconciliation gate upstream; the August tree retired with it (D10). DONE 2026-09-14 — the design\n     and the as-built below (D19-D21): the fold is the L1 layer, the old tables are views over the one database, the gate moved twice.\n"),
])
append(R + '/World/step9/THE_LOOP.md', ASBUILT, "## As built — D7'S MERGE, ONE DATABASE")

append(R + '/THE_WORLD.md', '''
### 2026-09-14 — D7'S MERGE BUILT: ONE DATABASE (the owner: "ok go the merge" — item 4 of the list; the map: World/step9/THE_LOOP.md "D7'S MERGE — ONE DATABASE" design + as-built)

The two databases are one. The reading's world — what exists and what the reading found, the fold of the 210 frozen units — is now the
journal's own L1 layer (D19): one row per item of the fold's ten lists, one per verse of the spine, one carrying the counts and the state
hash; the August tree model is retired (D10). The World folder's sixteen tables are views over those rows with their old names (D20; one
exception, the fold's events are fold_events), so the old ask tool answers over the same file the runs write into — "the world as of
Gen.30.24: 216 entities, 736 facts, 507 events, 153 demands, two outstanding." The reconciliation moved upstream twice (D21): the entry
proves the views against a fresh fold on nine counts and the hash; the journal gate proves the fold layer's header against the pinned truth
without refolding. World/world.sqlite is deleted; run_genesis.py is retired — the stepper is the player. merge_probes.py 0/8 → 8/8. The
board's births now come from the entities view. THE LIST: item 4 done; eleven remain, three of them yours.
''', "### 2026-09-14 — D7'S MERGE BUILT")

patch(R + '/World/step9/COMPILE_DEBT.md', [
    ("      STEP 7 (c) THE PORT BUILT 2026-09-14",
     "      D7'S MERGE DONE 2026-09-14 (the owner: \"ok go the merge\"; THE_LOOP.md \"D7'S MERGE — ONE DATABASE\" design + as-built; D19 the fold is the L1 layer, D20 the old tables are views with their old names, D21 the gate moved upstream twice; World/journal/build_world.py rewritten, fold_views.sql, World/build_world.py the entry, ask.py over the one database, run_genesis.py retired, World/world.sqlite deleted, the August tree retired (D10); merge_probes.py 0/8 → 8/8; the reconciliation ALL GREEN on nine counts and the hash). THE LIST: item 4 done.\n"
     "      STEP 7 (c) THE PORT BUILT 2026-09-14"),
])

patch(R + '/THE_STEPS.md', [
    ("kept current at every loop sitting.\n",
     "kept current at every loop sitting.\n"
     "\n"
     "D7'S MERGE — ONE DATABASE (2026-09-14, the owner's \"ok go the merge\";\n"
     "THE_LOOP.md \"D7'S MERGE — ONE DATABASE\" design + as-built): the reading's\n"
     "world — the fold of the frozen units, what exists and what the reading\n"
     "found — is the journal's own layer now, one row per item, and the World\n"
     "folder's old tables are views over it with their old names, so the old\n"
     "ask tool and the run's tool read one file: World/journal/data/\n"
     "world.sqlite. The reconciliation moved upstream: the entry proves the\n"
     "views against a fresh fold on nine counts and the state hash; the\n"
     "journal gate proves the layer's header against the pinned truth. The\n"
     "August tree model and the old world.sqlite are retired; the stepper is\n"
     "the player.\n"),
])

patch(R + '/THE_BRIEFING.md', [
    ('## SCOREBOARD (as of 2026-09-14, latest)\n',
     '## SCOREBOARD (as of 2026-09-14, latest)\n'
     '- **ONE DATABASE — THE MERGE DONE: THE READING\'S WORLD IS A LAYER OF THE JOURNAL, THE OLD TABLES ARE VIEWS OVER IT, AND THE OLD FILE IS GONE** (2026-09-14, on your "ok go the merge"; World/step9/THE_LOOP.md "D7\'S MERGE — ONE DATABASE"): the fold of the 210 frozen units written as the journal\'s L1 layer — 6,558 items, 3,015 verses of the spine, the counts and the hash in its header (D19); the World folder\'s sixteen tables now views over those rows with their old names (D20), so `World/ask.py at Gen.30.24` answers over the same file the runs write into; the reconciliation upstream twice (D21) — the entry against a fresh fold on nine counts and the hash, all green; the journal gate against the pinned truth; merge_probes.py 0/8 then 8/8; the August tree model retired; run_genesis.py retired. THE LIST: item 4 done, eleven remain.\n'),
    ('## ENTRIES (newest first)\n',
     '## ENTRIES (newest first)\n'
     '\n'
     '### 2026-09-14 — ONE DATABASE: THE READING\'S WORLD AND THE RUN\'S WORLD IN ONE FILE\n'
     '\n'
     'What changed: there were two database files. One held the reading\'s\n'
     'world — every thing the frozen chapters created and every fact,\n'
     'demand and naming the reading found — built in August and stale since.\n'
     'The other held the runs. Now the reading\'s world is a layer of the\n'
     'journal, rebuilt from today\'s 210 chapters, and the old tables are\n'
     'views over it with their old names. One file. The old one is deleted.\n'
     '\n'
     'Why it matters: a question like "what existed at Genesis 2:7, and what\n'
     'was owed on it" has one answer now, from one place. The board reads\n'
     'both kinds of rows from the same file. And a frozen chapter that moves\n'
     'the corpus\'s hash makes the gate say the layer is stale until it is\n'
     'rebuilt, so the two can never drift apart quietly again.\n'
     '\n'
     'What it took: a rewrite of the journal\'s builder, a file of views, an\n'
     'entry script that builds, reindexes and reconciles, and the gate\'s new\n'
     'line. No engine, runner or chapter changed. The August tree model and\n'
     'the slow teaching player are retired; the stepper is the player.\n'),
])

prepend(R + '/World/README.md',
        "> **MERGED 2026-09-14 (D7'S MERGE; World/step9/THE_LOOP.md \"D7'S MERGE — ONE DATABASE\").** `world.sqlite` in this folder is gone. THE ONE\n"
        "> DATABASE is `World/journal/data/world.sqlite` — the journal's index: L0 the operators, L1 THE FOLD (this folder's world, one row per item),\n"
        "> L2 the cases, L3 the runs — and the tables below are VIEWS over it with their old names (`World/journal/fold_views.sql`; the fold's\n"
        "> events are `fold_events`). `python3 build_world.py` builds the layer, reindexes, creates the views and reconciles; `--check` reconciles\n"
        "> alone; `python3 ask.py …` answers over the one database. `run_genesis.py` is retired — the player is `step9/world_stepper.py`.\n"
        "> The rules below (read-only over the corpus; never invent a row; reconcile against the fold) are unchanged.\n\n",
        'MERGED 2026-09-14')
prepend(R + '/World/RESUME.md',
        "# ⚠ MERGED 2026-09-14 (D7'S MERGE, the owner's \"ok go the merge\"; step9/THE_LOOP.md \"D7'S MERGE —\n"
        "# ONE DATABASE\" design + as-built): world.sqlite in this folder is DELETED. The one\n"
        "# database is journal/data/world.sqlite — the fold of the frozen units is its L1 layer\n"
        "# (journal/build_world.py), the tables named below are VIEWS over it (journal/fold_views.sql;\n"
        "# the fold's events are `fold_events`), build_world.py is the entry (build, reindex, views,\n"
        "# reconcile; --check), ask.py reads the one database, run_genesis.py is RETIRED (the player is\n"
        "# step9/world_stepper.py). The August tree model (L1_structure, world_tree, its checklist) is\n"
        "# retired (D10). \"Where it stands\" below is the record as it stood before the merge.\n\n",
        'MERGED 2026-09-14')
append(R + '/World/RESUME.md',
       "SITTING D7'S MERGE DONE 2026-09-14 (ONE DATABASE; THE_LOOP.md \"D7'S MERGE — ONE DATABASE\" design + as-built; the owner: \"ok go the merge\"): the fold as the journal's L1 layer (D19; 6,558 items + 3,015 refs + meta), the old tables as views with their old names (D20; fold_events the one exception), the reconciliation upstream twice (D21; ALL GREEN on nine counts and the hash 8b8fff1fa28953af); World/world.sqlite deleted, run_genesis.py retired, the August tree retired; merge_probes.py 0/8 → 8/8; `ask.py at Gen.30.24` over the one database. THE LIST: item 4 done.\n",
       "SITTING D7'S MERGE DONE 2026-09-14")

append(M + '/the-loop-ruling.md', '''
**2026-09-14 — D7'S MERGE BUILT: ONE DATABASE (the owner: "ok go the merge" — THE LIST's item 4; THE_LOOP.md "D7'S MERGE — ONE DATABASE"
design + as-built; the state doc's #174).** D19 THE FOLD IS THE STRUCTURE LAYER: World/journal/build_world.py rewritten — L0 the operators
(4,902), L1 THE FOLD (one row per item of corpus_world.fold()'s ten lists — 6,558 — one fold.ref per verse of the spine (3,015) and one
fold.meta with the counts and the state hash; the header the same; the August tree model retired, D10). D20 THE OLD TABLES ARE VIEWS WITH
THEIR OLD NAMES: World/journal/fold_views.sql — refs, units, facts, fold_events (the one exception: `events` is the journal's table),
event_themes, demands, mentions, names, standing, tests, checkpoints, meta, entities, relations, entity_state — created by world_journal.views()
at every reindex and attach beside the five run views. D21 THE GATE MOVED UPSTREAM TWICE: World/build_world.py (rewritten) builds →
reindexes → creates the views → RECONCILES them against a fresh fold on nine counts and the hash (--check alone); world_journal.py --gate
reads the fold layer's header against CORPUS_TRUTH's pinned literals and the index's own rows (fold_gate; a frozen unit moves the hash →
"stale — run World/build_world.py"). World/ask.py reads the one database (World/journal/data/world.sqlite); World/world.sqlite DELETED;
World/run_genesis.py RETIRED (the stepper is the player); the register: 12 fold kinds added, 22 August L1 kinds marked retired.
merge_probes.py 0/8 → 8/8 (four probe corrections, no code changed for a probe). THE REAL MERGE: the index 31,204 rows over 10 segments;
the reconciliation ALL GREEN (units 210, facts 1,809, events 557, demands 341, open 191, mentions 1,167, names 81, standing 2,163, tests 14,
hash 8b8fff1fa28953af). `ask.py at Gen.30.24`: 216 entities, 736 facts, 507 events, 153 demands, 593 standing law, two outstanding. THE LIST
after: eleven items remain — the owner's three (the inputs; time without a marker; the position of an input), after Deuteronomy two (the
second pass; the readback), a sitting (the checkpoints as they fall), small (the cursor's lines; the other worlds), the design thread's
(the window), later (the interface; a graded input).
''', "2026-09-14 — D7'S MERGE BUILT")
patch(M + '/MEMORY.md', [
    ('THE LOOP THAT WAITS IS BUILT. ⚠ STANDING DUTY: THE_LOOP.md "TO FINISH THE LOOP — THE LIST" (12 items:',
     'THE LOOP THAT WAITS IS BUILT. D7\'S MERGE DONE 2026-09-14 on "ok go the merge" — ONE DATABASE World/journal/data/world.sqlite (D19 the fold the L1 layer; D20 the old tables views with their old names, fold_events the exception; D21 the gate upstream twice; World/world.sqlite deleted; run_genesis.py retired; merge_probes.py 0/8 → 8/8; the reconciliation ALL GREEN). ⚠ STANDING DUTY: THE_LOOP.md "TO FINISH THE LOOP — THE LIST" (11 items open:'),
    ('- [The World folder](the-world-folder.md) — <world-link>: standalone queryable world; read its RESUME.md first',
     '- [The World folder](the-world-folder.md) — <world-link> (a symlink to the repo\'s World/): read its RESUME.md head first — MERGED 2026-09-14: world.sqlite deleted, the one database is World/journal/data/world.sqlite (ask.py over it), run_genesis.py retired'),
])
append(M + '/the-world-folder.md', '''
**2026-09-14 — MERGED (D7's merge; THE_LOOP.md "D7'S MERGE — ONE DATABASE").** World/world.sqlite is DELETED. The one database is
World/journal/data/world.sqlite — the journal's index; this folder's world (corpus_world.fold()) is its L1 layer, built by
World/journal/build_world.py; the folder's old tables are VIEWS over it (World/journal/fold_views.sql; the fold's events are `fold_events`);
World/build_world.py is the entry (build, reindex, views, reconcile; --check); ask.py reads the one database; run_genesis.py is RETIRED
(the player is World/step9/world_stepper.py). The rules (read-only over the corpus; never invent a row; reconcile against the fold) stand.
''', '2026-09-14 — MERGED')
patch(M + '/step9-exam-era.md', [
    ('⚠ THE LOOP step 7 (c) THE PORT (2026-09-14): THE PORT DECIDES NOTHING',
     "⚠ D7'S MERGE (2026-09-14): THE VIEW MAY NOT WEAR THE TABLE'S NAME — `events` is the journal's own table, so the fold's events are `fold_events` (the design names the exception, the probe learns it); A PROBE'S EXPECTATION FROM A TOOL'S DOCSTRING IS STILL HAND-TYPED (the who-span needs the book on both sides); THE REGISTRY'S ID IS NOT THE TOKEN (the_earth, not aretz); A DERIVED KEY IS THE BUILDER'S MAP, NEVER A SLICE (standing[:-1] = standin); A COMMENT INSIDE A BRACKET SWALLOWS THE LINE (twice in one sitting — write it after the closing bracket); THE GATE MOVES UPSTREAM AS TWO CHECKS — the entry refolds and reconciles, the gate compares headers to the pinned truth without refolding.\n"
     '⚠ THE LOOP step 7 (c) THE PORT (2026-09-14): THE PORT DECIDES NOTHING'),
])

append(R + '/logic/pre_logic_methods_2026-07-28/RECOVERY_new_thread_2026-09-12.md', '''
## 23. ADDENDUM (2026-09-14, D7'S MERGE — ONE DATABASE; the owner: "ok go the merge", THE LIST's item 4; the state doc's COMPACTION POINT #174)

BUILT: THE_LOOP.md "D7'S MERGE — ONE DATABASE: the design" + "As built"; THE LIST's item 4 marked done. THE DECISIONS D19 THE FOLD IS THE
STRUCTURE LAYER (the journal's L1 = corpus_world.fold()'s ten lists as rows — 6,558 items — plus 3,015 fold.ref rows of the spine and one
fold.meta; the header carries the counts and the state hash; the August tree model — L1_structure.jsonl, world_tree.json, its checklist —
RETIRED as D10 ruled), D20 THE OLD TABLES ARE VIEWS WITH THEIR OLD NAMES (World/journal/fold_views.sql: refs, units, facts, fold_events —
the ONE exception, `events` being the journal's table — event_themes, demands, mentions, names, standing, tests, checkpoints, meta,
entities, relations, entity_state; created by world_journal.views() at every reindex and attach beside the five run views), D21 THE GATE
MOVED UPSTREAM TWICE (World/build_world.py the entry: build → reindex → views → reconcile against a fresh fold on nine counts and the hash,
--check alone; world_journal.py --gate: fold_gate() — the fold layer's header against CORPUS_TRUTH's pinned literals and the index's own
rows, no refold; a frozen unit moves the hash → "stale — run World/build_world.py"). THE CODE: World/journal/build_world.py (rewritten),
World/journal/fold_views.sql (new), World/build_world.py (rewritten), World/ask.py (the path; fold_events), World/run_genesis.py (RETIRED with
a guard), World/journal/registers/event_kinds.yaml (12 fold kinds added; 22 August L1 kinds marked retired), World/step9/world_journal.py
(views; pinned_truth; fold_gate; the gate's line), World/step9/merge_probes.py (new). No engine, runner or unit change. THE PRINTS:
merge_probes.py 0/8 → 4/8 → 6/8 → 8/8 (four probe corrections on the tool's and the registry's own forms — no code changed for a probe);
THE REAL MERGE: the fold 29 s, L0 4,902, L1 9,574 rows, the index 31,204 rows over 10 segments, the fourteen fold views + the five run
views, World/world.sqlite deleted, THE RECONCILIATION ALL GREEN (units 210, facts 1,809, events 557, demands 341, open 191, mentions 1,167,
names 81, standing 2,163, tests 14, hash 8b8fff1fa28953af); `World/ask.py at Gen.30.24` over the one database: 216 entities, 736 facts, 507
events, 153 demands, 593 standing law, two outstanding (Rachel's, 30:3 and 30:14); `entities`: God 216, Abraham 104, Noah 46; `called
jacob`: yaaqov from Gen.25.26, yisrael from Gen.35.10; THE GATE: %s; THE PROBES AFTER: %s. LINTS 0 on every changed file; every record at its
baseline. THE FORMS: forms_numbers_walk/loop_2026-09-14/ (loop_design_merge.md, write_merge_records.py). NEW COMMANDS: `python3
World/build_world.py` (the merge whole; `--check` the reconcile alone — run it after any freeze, the gate says when); `python3 World/ask.py
at|open|who|career|entities|called|names|sql …` over the one database. THE DATA FOLDER after: L0_scripture.jsonl, L1_fold.jsonl,
L2_cases.jsonl, the L3 segments, world.sqlite (15.6 MB); a stray .live body file of a stepping session that died mid-run — the design's
trace, harmless.

⚠ THE STANDING DUTY (the list): eleven items remain — the owner's three (1 the inputs themselves; 6 time without a marker; 7 the position of
an input), after Deuteronomy (2 the second pass; 3 the readback), a sitting (5 the checkpoints as they fall), small (8 the cursor's lines;
12 the other worlds), the design thread's (9 the window), later (10 the interface — its shape agreed with the main thread and three mockups
drawn: the panel, the feed, the output-only feed, THE BOARD; 11 a graded input). NEXT on the owner's word: an item of the list (his three
decisions first; the board as a real page over the one database is item 10's build), THE NEXT BOOK (Deuteronomy, as #160), or the py_units
gloss sitting. UNCOMMITTED since 08fa06e: step 7 (c), the merge, the mockups' forms and the post-commit notes; commit only on "commit push".
''' % (GATE, PROBES), "## 23. ADDENDUM (2026-09-14, D7'S MERGE")

append(R + '/logic/pre_logic_methods_2026-07-28/PROMPT_continue_solo_era_2026-08-06.md', '''
═══ COMPACTION POINT #174 (2026-09-14 — written at the close of D7'S MERGE, ONE DATABASE, the owner's "ok go the merge" on THE LIST's item 4; A CLEAN COMPACTION POINT) ═══
BUILT: THE_LOOP.md "D7'S MERGE — ONE DATABASE: the design" + "As built"; the list's item 4 done. DECISIONS (mine, on the measurements; the owner may overrule): D19 THE FOLD IS THE STRUCTURE LAYER (World/journal/build_world.py rewritten — L0 the operators, L1 THE FOLD: 6,558 items of corpus_world.fold()'s ten lists + 3,015 fold.ref + fold.meta, the header with the counts and the hash; the August tree retired, D10); D20 THE OLD TABLES ARE VIEWS WITH THEIR OLD NAMES (World/journal/fold_views.sql — fourteen views + meta; `fold_events` the one exception since `events` is the journal's table); D21 THE GATE MOVED UPSTREAM TWICE (World/build_world.py rewritten as the entry: build → reindex → views → reconcile against a fresh fold, --check; world_journal.py --gate's fold_gate against CORPUS_TRUTH's pinned literals and the index's rows). World/ask.py over the one database; World/world.sqlite DELETED; World/run_genesis.py RETIRED; the register's 12 fold kinds added, 22 August L1 kinds retired. No engine, runner or unit change.
THE PRINTS: merge_probes.py 0/8 → 8/8 (four probe corrections, none in code); THE REAL MERGE: L0 4,902, L1 9,574, the index 31,204 rows over 10 segments, the reconciliation ALL GREEN (units 210, facts 1,809, events 557, demands 341, open 191, mentions 1,167, names 81, standing 2,163, tests 14, hash 8b8fff1fa28953af); `ask.py at Gen.30.24` 216 entities / 736 facts / 507 events / 153 demands / 593 standing law, two outstanding; THE GATE: %s; THE PROBES AFTER: %s. RUN unmoved; the hash untouched. Lints 0 on every changed file; the state doc 147; THE_WORLD 5; MEMORY.md 4; THE_STEPS 1.
THE RECORDS: THE_LOOP.md, THE_WORLD.md (the fifth 2026-09-14 entry), COMPILE_DEBT.md's loop box, THE_STEPS's loop section, THE_BRIEFING (the scoreboard + an entry), World/README.md and World/RESUME.md (the merge's head notes + a sitting line), memory (the-loop-ruling.md, MEMORY.md's loop and World-folder lines, the-world-folder.md, step9-exam-era.md's lessons head), the recovery file's section 23; the forms in forms_numbers_walk/loop_2026-09-14/.
ALSO THIS WINDOW (after #173): the interface's shape agreed with the main thread ("Torah Grok Main" — the feed, stamps, the clock its own line, five colors, generated never typed) and recorded under THE LIST's item 10; three mockups published as artifacts and kept in the forms folder — the panel page (mockup_state_page.html), the feed (feed_mockup.py), the output-only feed (feed_mockup_output.py), THE BOARD (board_mockup.py — every thing a tile, stepped from the journal's rows with the reading's creations merged in; the owner: "I love it").
⚠ THE STANDING DUTY: THE LIST (eleven open) — the owner's three (1 the inputs themselves; 6 time without a marker; 7 the position of an input), after Deuteronomy (2 the second pass; 3 the readback), a sitting (5 the checkpoints as they fall), small (8 the cursor's lines; 12 the other worlds), the design thread's (9 the window), later (10 the interface — the board as a real page over the one database; 11 a graded input).
NEXT on the owner's word, ONE OF: an item of the list (his three decisions first; or the board as a real page — item 10's build, one sitting, display only); THE NEXT BOOK (Deuteronomy, as #160); the py_units gloss sitting. UNCOMMITTED since 08fa06e: step 7 (c), the merge, the mockups' forms, the post-commit notes; the staging form `git add -A -- . ':!elijah_docket' ':!DISPOSABLE_scan/*.zip'`; commit only on "commit push" (the GitHub tool at /opt/homebrew/bin/gh).
POST-COMPACTION REREADS (mandatory, first sitting): as #170's, plus THE_LOOP.md's step 7 (a)-(c) and "D7'S MERGE" designs + as-builts and "TO FINISH THE LOOP — THE LIST", and the recovery file's sections 20-23 (read before any word on the loop or the interface).
''' % (GATE, PROBES), '═══ COMPACTION POINT #174')
print('records written')
