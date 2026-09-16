# THE LOOP — the running world with memory (owner-ruled PERMANENT, 2026-09-09)

## The ruling, verbatim

The owner, 2026-09-09, after the ARCHITECTURE folder's clock, links, effects and events docs were examined against
the engine and the question "when you say ledger, are we updating a database?" was answered honestly (no — the
step-9 ledger is in memory, rebuilt every run, and nothing writes it anywhere):

> "I thought we agreed to store events in a database."
> "remember we said we don't know what this program does yet. If it runs twice, one time to build the world, a
> second time to read all verses and run the world, this requires a database doesn't it?"
> "how does a simulation work? it is running, not a one or two pass right? how would that look in this setting"
> "If we assume this is a simulation then we have to assume it loops right?"
> "this is what we need. how do we add it on? how long will it take"
> "ok record this so we don't forget it after compact. This is a permanent decision to build the architecture. I
> meant for this to be built when it was added last month. We slipped somehow. Lets not forget it again. I need to
> compact but this is more than a compact memory"

THE DECISION: the step-9 engine becomes a RUNNING SIMULATION WITH MEMORY — a loop that keeps its state between
inputs, writes every event to the world journal, is indexed for questions, resumes at a cursor in the text, gates
its laws on installation, and takes scenarios at any verse. Permanent. Not a compaction note: it lives here, in
THE_WORLD.md's idea log, THE_STEPS.md, COMPILE_DEBT.md's standing map, THE_BRIEFING.md, and memory.

## How it slipped (named so it cannot slip the same way twice)

- 2026-08-24, THE_WORLD.md: the DATABASE-NOW-AS-INDEX ruling. The journal is the truth (append-only JSONL, one
  event per line, hash-chained); sqlite is the INDEX, rebuilt from the journal, never written directly; single
  writer; registry-grade entity ids on every event. BUILT the same day in the mockups folder's `world_journal/`: `worldledger.py`
  (envelope {s, op, layer, kind, subj, data, prov, chain}), build_world.py, three segments (L0 scripture 3,027,
  L1 structure 545, L2 cases 43 from the Exodus 21 chapter machine of that era), world.sqlite, world_tree.json.
  Its files have not changed since 2026-08-24 (measured by `ls -la` on 2026-09-09).
- 2026-09-03, the effects law: "this will now build a simulation instead of a ledger" — and the simulator skeleton
  world_engine.py was built FRESH in World/step9 with its own in-memory World (entities as objects, the ledger a
  list per entity, timers a list, the log a list). The engine's only file access reads calendar_parameters.yaml.
  No line of it writes the journal or any sqlite (measured by grep on 2026-09-09).
- World/world.sqlite (the World folder, rebuilt 2026-09-08) indexes the READING era's corpus world — 557 narrative
  events, 1,809 facts — not the engine's tape (1,058 events after O8 S4) nor its ledger.
- THE CAUSE: the August journal lived in grok-mockups (the never-commit set) and the September engine had no line
  in the standing map tying it to the journal. The ruling sat in THE_WORLD.md's idea log; the map (COMPILE_DEBT's
  sequence line) never carried it as a box to tick. ⚠ LESSON: an architecture decision is carried in the MAP as a
  checkbox with a home file, never only in an idea log.

## The journal moved into the repo (the owner, 2026-09-09: "also we need to add it to github so move it if it makes sense")

MOVED the same sitting: the mockups folder's `world_journal/` → **World/journal/** (worldledger.py, build_world.py,
run_cases.py, registers/ — event_kinds, kinds, classes — and primary/scenes.yaml TRACKED; data/ — the L0/L1/L2
segments, world.sqlite, the two views — DERIVED and gitignored, `World/journal/data/`). Both scripts find the repo
root two levels up, as before; their two view writes were redirected from the mockups' player folder into data/.
REBUILT IN PLACE from the 163 frozen units: 6,601 rows indexed (L0 + L1 + the 43 L2 case events), the chain
verified, DETERMINISM byte-identical across two processes — GREEN. ONE CHECKLIST LINE FAILS: "forming/filling
symmetry — day 4 fills day 2's vault, day 5 fills day 2's waters + vault, day 6 fills day 3's land" — the August
world-tree assertion (green over 97 units on 2026-08-24) against the units as frozen today; not the move's doing
(no logic line changed), a drift of the August tree model filed for THE LOOP's first sitting, where step 1 uses
worldledger's ENVELOPE and INDEX, not build_world's tree. So the plan's "copied, never imported" is retired: the
sink IMPORTS worldledger from World/journal. The mockups folder stays on the never-commit list; the journal no
longer lives there. The commit waits for the owner's "commit push".

## What a simulation is, here

A loop with memory: take the state as it stands, accept the next input, fire every rule against it, write what
changed, move the clock if the input carries a date, KEEP the state, wait for the next input. "Passes" are the
replay you get when the whole stream is fed at once and the state is thrown away — what the engine does today.
The four rules already kept make new loops safe to discover later: every change enters through World.submit; time
moves only at markers (no tick events); rules are registered daemons with their verses; consequences write the
ledger and never the tape (THE FENCE). The loops found so far, each by running the text: the verse loop, the timer
loop, the recurrence loop (the period field — the Sabbath, the daily lamb), the cancellation loop (the pierced
servant), the close loop (the daily offering's paired act), the cascade loop (depth one), the calendar loops, the
exam loop. Named and not built: the prophets read against the open ledger (the effects law's target), the history
books as run logs, Heaven's ledger closing across books, the land's rest debt collected in Chronicles.

## The five steps (the plan of 2026-09-09; design file and fire-probes FIRST at the sitting that builds each)

| step | what | touches | cost |
|---|---|---|---|
| 1 THE SINK | the engine's log (EVENT, WRITE, TIMER-SET, TIMER-CANCEL, TIMER-FIRE, MARKER — ordered, no timestamps) written as a journal SEGMENT in the August envelope: subject = the registry entity id, provenance = the verse and the daemon, the hash chain across lines; one segment per run | a NEW module World/step9/world_journal.py IMPORTING Segment and index_sqlite from World/journal/worldledger.py (moved into the repo 2026-09-09); the sequence runner; a probe | half a sitting |
| 2 THE INDEX | sqlite rebuilt from the segments on the World folder's drop-and-rebuild pattern, never written directly: events, ledger writes with open and close days, timers, markers, the clock; a check script comparing the index's counts to the run's tuple; the ask-tool queries (an entity's ledger at a day; open timers at a verse; who wrote this) | a schema beside World/schema.sql, a builder, the check | half a sitting |
| 3 INSTALLATION (T1) | per-daemon `installed_by:`; the installing act's daemon writes `in_force` on an institution entity; World.submit consults it before the call and logs SKIPPED-NOT-IN-FORCE; the two settings (from boot; "Abraham kept the whole Torah", Yoma 28b / Kiddushin 82a) as a printed fork — the design already in CLOCK.md section 8 and COMPILE_DEBT's THEN NUMBERS line | 43 daemon rows, the dispatch gate, probes, the sweep's moved tuples predicted by the stitcher first | one to two sittings |
| 4 THE CURSOR | resume by REPLAYING the journal to a verse and handing back a live world — no saved state file, the journal the only truth; the tape stored as a segment with verse addresses so a position in it is a position in the text; new submissions append a new segment whose chain continues from the last line | the sequence runner split into stitch-the-tape and run-from-a-cursor; the tape segment | one sitting |
| 5 SCENARIOS | the existing case files injected as labeled SCENARIO events into the live world at a chosen verse, the Mishnah row the expected answer — the world as the oracle | the case files routed through the live world | one sitting |
| 6 THE READBACK (named 2026-09-09, D12; THE FIRST FORM designed and BUILT 2026-09-15/16 at THE DEUTERONOMY WALK 1b on the owner's "Yes 1. Go" — DEUTERONOMY_WALK.md "Sitting 1b" (R1)-(R6) and the as-built) | the text re-read against the ledger the run left — the third pass the shelf records (the repetition in the plains of Moab; understanding after the forty-year run): THE NARRATIVE HALF BUILT — a retelling a REFERENCE ROW (the DATA table the_readback: forty-two rows graded VERBATIM / TURNED / SHORTENED / EXPANDED / SUPPLIED / DISAGREES, every row's tape entry found on the running world by kind and verse — CA4), an act told only in the retelling written ONCE at its own time by a retrograde marker and, where the tape holds its run, CLOSED AT ONCE BY THE PRIOR RUN inside the daemon; a disagreement an OPEN row; a receipt a run citation (the gate's CHAPTER); THE LAWS' HALF (chapters 5-26 re-read against the ledger) and the prophets' indictments after — OWED to their own sittings | cold_run_opening_speech.py (the_readback, the closes by a prior run), readback_probes.py 6/6, the tape's CA4-CA8; cold_run_obey_horeb.py (chapter 4 on the same form, 2026-09-16 — eleven rows; THE TAPE'S HOLE: the ten words spoken and the tablets given, told only in the retelling, written once at their own days by two retrograde markers with a forward marker closing the stretch; the bar's third telling a second open row; readback_probes 9/9, CC4-CC6) | the laws' half a sitting when chapter 5 opens |
| 7 THE LOOP THAT WAITS (opened 2026-09-14, the owner: "ok go 1"; the design sections below) | (a) WRITE AS YOU GO — every journal line on disk and in the index at the end of its block (D14 THE SEAL); (b) THE STEPPER — the tape driven at the event grain with a pause; (c) THE PORT — a queue the loop reads between steps, the text its first producer | world_engine.py (one hook), world_journal.py (the live sink, the audit), the sequence runner (attach), live_probes.py | one sitting each |

ORDER: 1 → 2 → 3 → 4 → 5. The sink first because it is cheapest and makes every run auditable at once;
installation before the cursor, because a resumable world with every law in force from creation would save the
wrong state; the cursor last because replay-to-cursor is nearly free once the journal exists. TOTAL: three to four
sittings for the loop with memory, five with scenarios; installation the only uncertain cost.

THE GATES: (a) a second run reproduces the segment BYTE FOR BYTE and the chain verifies — the replay is the audit,
the running world is the instrument; (b) the index's counts equal the run's tuple; (c) the daemon gate demands
`installed_by` on every daemon; (d) every moved sweep tuple predicted before the run. THE HOMES under the truth
split: the run segments and the index are DERIVED caches — uncommitted, gitignored beside World/world.sqlite;
scenario inputs are PRIMARY records in git. The August folder stays where it is, untouched, on the never-commit
list.

SEQUENCING against the standing map: O11's B5 (484 labels) is independent and still owed. THE LOOP takes NUMBERS'
OPENING BLOCK together with T1 (already Numbers' first item), or the sitting just before it — the owner's call.
The first sitting's script: the design file for step 1 (a section added to THIS file), the probe written to FAIL
on the unchanged engine, the module, the runner's hook, the byte-identical gate, the records.

## Step 1 THE SINK — the design (2026-09-09, the loop's first sitting; written before the probe, the probe before the code)

WHAT A LINE IS. The engine logs SEVEN classes, not the six the ruling's memory listed — RETRO-WRITE was missing (a due already
past, written at submission inside a retrograde stretch; CLOCK.md section 4): EVENT, WRITE, RETRO-WRITE, TIMER-SET, TIMER-FIRE,
TIMER-CANCEL, MARKER, each a tuple (class, day, payload) in World.log. The sink writes every line as one journal event in the
August envelope {s, op, layer, kind, subj, data, prov, chain}:
- `s`: the line's ordinal in the run (the segment's own counter) — the log's order IS the run's order.
- `op`: the clock DAY the line was logged at (the tuple's second field) — the world clock as the order axis, the corpus
  world's `ord` in the engine's unit. Inside a retrograde stretch a line carries the counter's day here and the text's date
  in its payload's `dated`.
- `layer`: `L3` — a RUN of the law engine (L0 scripture, L1 structure, L2 cases are the August fold's).
- `kind`: run.event, run.write, run.retro_write, run.timer_set, run.timer_fire, run.timer_cancel, run.marker — added to
  World/journal/registers/event_kinds.yaml BEFORE first use (the register's own rule, 2026-08-24).
- `subj`: the REGISTRY entity id — the payload's subject resolved through World._registry (the one who-is-who), so a scene
  token and its registry name write one subject; a marker's subject is `clock`; a line without a subject writes `world`.
- `data`: the payload dict AS IT STANDS AT THE RUN'S END, canonical JSON (sorted keys, no spaces, non-ASCII kept). A fact the
  sink records rather than hides: a WRITE line holds the same dict object as the ledger entry, so a later close (`closed_by`)
  is visible in its own line, and an event's bound list is closed by the marker that closes it — the segment is the audit
  of the run as it stands when the run ends, not a stream captured mid-run (the cursor of step 4 replays the tape through
  the engine; it never reads a payload back into state). Any non-JSON leaf is coerced to a string and COUNTED; the count is
  printed and must be zero on the tape (measured on the baseline run before the code).
- `prov`: {unit: the daemon that wrote it (`source_law`), or `tape` for an event, or `marker`; ref: the verse (`case_source`,
  or the marker's verse)} — the index's unit and ref columns.
- `chain`: sha256(previous + canon(event))[:16] from `genesis`, worldledger's own.
No timestamps anywhere. The header line: {segment: L3, source: <runner>/<world>, events: N, chain_head}.

WHERE. One segment per WORLD per run, a fixed path overwritten by the next run: World/journal/data/L3_run_<runner>_<world>.jsonl
— the sequence runner writes four (the running setting, the sojourn fork's two other settings, THE REST). The directory is
World/journal/data/ (gitignored, derived) or WORLD_JOURNAL_DIR when set — the August selftest's own pattern, for the two-process
gate. The sink is called at the end of run_world() and rest_world(); the sweep's subprocess invocation (cwd World/step9) is
unaffected, every path absolute. Step 4 turns the fixed paths into appended segments whose chain continues.

THE MODULE. World/step9/world_journal.py: KINDS (the seven, class → kind), sink(world, source, out_dir=None) → (path, lines,
coerced), verify(path), index(db_path, paths), counts(db_path) → {kind: n}, and the cross-process gate (below). It IMPORTS
Segment and index_sqlite from World/journal/worldledger.py — the envelope has one home.

THE PROBES. World/step9/journal_probes.py, written to FAIL on the unchanged engine, all in-process on a small probe world (a
probe daemon, a registry map, a marker, a timer that fires, a cancel, a retrograde stretch) so they run in a second: J1 a run
writes a segment whose line count equals the log's length; J2 the chain verifies, and a line mutated in place is DETECTED; J3
every kind the sink writes is in the register; J4 the subject is the REGISTRY id (a scene token mapped to its registry name);
J5 two sinks of one world are byte-identical; J6 (step 2's first gate) the index rebuilt from the segment counts each kind
exactly as the world's log does, and answers "who wrote this" (the daemon by unit) and "what is written on this subject".

THE GATE. `python3 World/step9/world_journal.py --gate` runs the sequence runner twice in two subprocesses with
WORLD_JOURNAL_DIR set to two fresh directories, then for each of the four segments: the bytes identical, the chain verified,
the index rebuilt and its per-kind counts equal to the RUN tuple the runner printed (events, timers set, fired, cancelled,
retro-writes, writes). GREEN = the replay is the audit, the running world is the instrument.

STEP 2 THE INDEX, minimal in this sitting: worldledger's events table (seq, op = the day, layer, kind, subj, data, unit = the
daemon, ref = the verse, chain) rebuilt from the L3 segments — drop-and-rebuild, never written directly — with the counts
check and the two questions above as queries. The richer tables (a ledger view with open and close days, the timers' set,
fire and cancel joined, the clock's markers) are step 2's remainder, filed, not built, until step 1's gate is green.

## As built — step 1 THE SINK, and step 2's first gate (2026-09-09, the loop's first sitting; the owner: "then the loop")

THE ORDER HELD: the design section above first; the seven kinds registered in World/journal/registers/event_kinds.yaml (34
kinds now); the probes second — World/step9/journal_probes.py, six probes on a small world exercising all seven log classes,
0/6 on the unchanged engine (every FAIL the module's absence, after one probe kind was swapped for a registered one — the
tape's registry refuses a probe-only event type, so the breaking of the tablets stands in for a refusal); the code third —
World/step9/world_journal.py (sink, verify, index, counts, reindex, the gate) importing Segment and index_sqlite from
World/journal/worldledger.py, and ONE additive line in the engine: World.submit stamps `written_by` (the consuming daemon's
name) on every effect before it is written, so the journal's prov.unit answers "who wrote this" — the baseline had found only
594 of 1,306 effect lines naming a source_law; the runner's hooks fourth — run_world() and rest_world() sink each world, run()
rebuilds the index at its close; then 6/6 probes; then the gate.

THE BASELINE (measured on the unchanged engine before the code, scratchpad loop_baseline.py): the tape's log 2,494 lines —
EVENT 1,058, WRITE 1,224, MARKER 130, TIMER-SET 43, TIMER-FIRE 39, no cancel and no retro-write on the tape (the classes exist;
the probe world exercises them); no non-JSON leaf; no payload dict shared by two log lines; every EVENT carrying subject and
case_source; the running world 0.5 seconds.

THE RUN with the sink live: four segments in World/journal/data/ — the running setting (seed_isaac), the sojourn fork's two
other settings, and THE REST — 2,494, 2,494, 2,494 and 1,844 lines, coerced 0 on every one; the ten checkpoints unmoved; the
runner 1.9 seconds; the index rebuilt from all seven segments on disk: 15,927 rows (L0 4,517, L1 2,041, L2 43, L3 9,326).

THE GATE (`python3 World/step9/world_journal.py --gate`): the runner twice in two processes and two directories — all four
segments byte-IDENTICAL, all four chains VERIFIED, the running world's index counts equal to the RUN tuple the runner printed.
GREEN. Clock probes 22/22, sequence probes 4/4, the daemon gate and the dependency gate satisfied after the engine's line;
THE SWEEP 39/39 at 4,518 cells — no graded value moved by the writer stamp.

THE TWO QUESTIONS ANSWERED BY THE INDEX (step 2's first gate, on the real world.sqlite): who wrote this — 0 of 4,579 run.write
rows unattributed across the four segments, the writers by daemon (law_mamre 1,488, law_joseph 942, law_primeval 896,
law_exodus_story 436, law_erection 212, law_pre_sinai 193, law_family 136 …); what is written on this subject — 252 distinct
subjects on the ledger (the entity count), israel_people's lines by kind on request; a verse asked (Exod 12:2) returns its
marker lines. STEP 2 REMAINS for its richer tables (the ledger view with open and close days, the timers joined, the markers as
the clock) and the ask-tool; its first gate is inside the loop's gate.

FACTS THE SINK RECORDS: the segment is the audit of the run AS IT STANDS WHEN THE RUN ENDS (74 WRITE lines carry closed_by;
every bound closed by its marker); a fixed path per world, overwritten per run, until step 4 appends; the register grew before
first use; the sweep's subprocess invocation unaffected (absolute paths). ⚠ LESSON: A cd IN A COMMAND BREAKS THE NEXT COMMAND'S
RELATIVE PATH — the gate and the probes were run once from the wrong directory before the absolute-path rerun; and A
PROBE-ONLY EVENT TYPE IS REFUSED BY THE REGISTRY — reuse a registered kind on the probe world.

NEXT: step 3 INSTALLATION (T1) — the design in CLOCK.md section 8 and COMPILE_DEBT's THEN NUMBERS line; its own design section
here first, its probes to fail, the daemon gate's `installed_by` demand, the moved sweep tuples predicted by the stitcher.

## What the teachers say about passes (read on the local shelf, 2026-09-09; the owner: "does the oral torah, the teachers,
## recommend a two pass run? look for hints, it won't say directly")

Searched by script across twelve works of the local export (Data/sefaria_export, English; the export's Talmud index 0 is folio
1a, so a page is index // 2 + 1 — measured on Yoma before any address was typed), the hits read whole at their standard
addresses. The teachers never say "run it twice." They describe a Torah that is GIVEN, TAUGHT, STUDIED and RUN in repeated
passes at every level, each pass adding detail or understanding without changing what the earlier pass produced. The hints, by
strength for the loop:

1. THE GIVING IN PASSES — Sotah 37b:3 and Chagigah 6b:1 (the Tosefta's dispute): Rabbi Yishmael — the GENERAL statements were said
   at Sinai and the DETAILS later in the Tent of Meeting; Rabbi Akiva — general and details at Sinai, REPEATED in the Tent, and a
   THIRD time in the plains of Moab, "as recorded in the book of Deuteronomy." Three passes over one law: the general, the detail,
   the repetition. And the sugya's own constraint at Chagigah 6b:2: "it is not plausible that the details of a mitzva would change
   over time" — a procedure cannot differ between the pass that installed it in general and the pass that gave its details, which
   is why the daily offering could not have run before its details were given. That is THE INSTALLATION QUESTION (step 3) argued
   on the page: whether a law ran before its detailed giving, decided by whether its details could have changed.
2. THE PASS AFTER THE RUN — Avodah Zarah 5b:2 (Rabba): "a person does not understand the opinion of his teacher until after forty
   years," from Moses' own words at Deuteronomy 29:3-4 — the understanding pass comes after the whole run; Deuteronomy is the
   Torah re-read after forty years of running it. Shabbat 63a:15 (Rav Kahana, eighteen and the whole Talmud learned): "a person
   should first learn and then understand the rationale"; Avodah Zarah 19a:10 (Rava): study and review "even though he may
   afterward forget, and even though he does not understand what it is saying." Two passes of study: acquire, then reason.
3. THE FOUR REPETITIONS — Eruvin 54b:11-13: the order of teaching the Oral Law — Moses from the Almighty, Aaron, the sons, the
   elders, the people, then each teaches the next — "everyone heard the lesson four times"; Rabbi Eliezer: a person must teach
   his student four times. The transmission itself is a multi-pass protocol, and the count is a rule.
4. WORLDS BEFORE THIS ONE — Bereshit Rabbah 3:7 and 9:2 (Rabbi Abbahu): "He continuously created worlds and destroyed them,
   until He created the current one, and said: This one pleases Me, those did not" — the run iterated until a world was kept.
   THE PROGRAM BEFORE THE WORLD — Bereshit Rabbah 8:2 (Reish Lakish): the Torah preceded the world by two thousand years;
   Pesachim 54a:8-11: seven things created before the world, the Torah first; and Pesachim 54a:14's split between a thing whose
   THOUGHT arose on the eve of the Sabbath and its creation after it — the plan and the execution as two moments. THE WORLD BUILT
   WHOLE — Rosh Hashanah 11a:6 and Chullin 60a:9 (Rabbi Yehoshua ben Levi): "all the acts of Creation were created with their full
   stature, full capacity, full form" — the first pass builds the initial state complete; time runs after it.
5. INCREMENTAL OR WHOLE — Gittin 60a:14-15: Rabbi Yochanan, the Torah was given scroll by scroll (each portion taught, then written,
   then the next); Reish Lakish, given as a complete book; and even for Rabbi Yochanan "the Torah after it was joined together to
   form a single unit" — the passes end in one sealed record. Our own two forms: the frozen units one by one, the journal joined.
6. READING ORDER IS NOT RUN ORDER — Pesachim 6b:7 (Rav): "there is no earlier and later in the Torah" — the text must be read whole
   and then run in time order (our stitcher); against it Yoma 32a:2: the Day of Atonement's portion "was stated in the order in
   which it is performed except for this verse" — where the text IS the run order, the tradition says so and names the exception.
7. WRITTEN, THEN SEALED — Rosh Hashanah 16b:12: three books opened on the New Year, the righteous "immediately written and sealed"
   — the year's ledger in two acts, the entry and its close, which is the ledger's open-and-closed field.
8. THE SAME CORPUS IN THIRDS — Kiddushin 30a:10: a person divides his days into Bible, Mishnah, Talmud — three passes over one
   text, which is the compiler law's three layers (the program, the answer sheet, the compile rules).
9. IN FORCE BEFORE THE GIVING — Yoma 28b:9-10 and Kiddushin 82a:10: Abraham kept the whole Torah before it was given, "even the
   joining of cooked foods"; Rav Shimi bar Chiyya's counter, "say he kept only the seven Noahide commandments" — the two settings
   of step 3's fork, on the page as a dispute.

THE TENT OF MEETING MEASURED IN THE INK (the owner: "where does the tent of meeting occur in the torah"; torah_grok.sqlite, the
two words adjacent with points and prefixes stripped): 135 tokens — Genesis 0; Exodus 34 in ten chapters, the first at 27:21
inside the tabernacle's spec (named before it exists), twice at 33:7 for the tent Moses pitched OUTSIDE the camp before the
tabernacle stood, twelve in chapter 40 at the erection; Leviticus 43 in fourteen chapters, opening the book at 1:1 ("the LORD
called to Moses and spoke to him from the tent of meeting" — the Sifra's first rows, LV01A-01/02); Numbers 56 in nineteen chapters,
the densest, 4 and 18 the service chapters; Deuteronomy 2, both at 31:14, Moses and Joshua at the handover. So the three passes
sit on the ink: the general pass at Sinai (Exodus 19-24) has NO tent token; the detail pass "in the Tent of Meeting" is
Leviticus and Numbers (99 of the 135); the repetition in the plains of Moab names the tent only to close it. The tent is itself
an INSTITUTION with a spec, a provisional stand-in, an erection, a service life, and a handover — step 3's own shape.
IS THE TENT A PROGRAM (the owner's next question)? No — two other things, both in its own verses. (1) THE CHANNEL the detail
pass is delivered through, declared in its spec: "I will meet with you there and speak with you from above the cover, from
between the two cherubim, all that I command you" (Exod 25:22; Num 7:89 the same address heard; Exod 29:42 "at the entrance
of the tent of meeting, before the LORD, where I will meet with you to speak with you there"). (2) A COORDINATE FRAME the laws
compute against once it stands: "before the LORD," "the north," "the entrance," "outside the camp" name no place until the
tent gives them one — our compiled rows already run so (the corner algorithm resolving 'before the LORD' with 'in front of
the altar' to the southwest, LV06-07; the north absent on a private altar, LV01C-02; the three camps from the three
outside-the-camp verses, L04-19; the entry ban graded house-wide against the cover's face, LV16A-01). The new information is
the LAWS' output given the tent's state, not the tent's; the tent is the first institution whose erection installs a book.

THE TENT AS THE RUN'S INTERRUPT — THE CASES THE CODE DID NOT COVER (the owner, 2026-09-09: "is the tent the place we learn
new information based on the code running? does it output something we don't know of yet? This could change the way we think
of runs or passes"). YES, and the ink names the mechanism. Four times in the run a case arises that the standing law does not
decide, the run HALTS on it, the case is carried to the tent, and what comes out is new: (a) the blasphemer — "they put him in
guard, to be declared to them by the mouth of the LORD" (Lev 24:12), the output Lev 24:13-23 (the verdict AND the blasphemy law
with talion restated); (b) the wood-gatherer — "they put him in guard, because it had not been declared what should be done to
him" (Num 15:34), the output 15:35-36; (c) the unclean men at Passover — "stand, and I will hear what the LORD commands
concerning you" (Num 9:8), the output the second Passover, 9:10-14, code complete (RESEARCH_LOG's own example); (d) the daughters
of Zelophehad — standing "at the entrance of the tent of meeting" (27:2), "Moses brought their judgment before the LORD" (27:5),
the output the inheritance order 27:8-11, then the tribes' counter-case and 36:5 "by the mouth of the LORD." Beside them: the
princes' order (Sifrei Bamidbar 47:1 — Moses did not know until told), the rods deposited "in the tent of meeting before the
testimony, where I meet with you" (Num 17:19 — an output no one knew: which house), and the standing device, the Urim "before
the LORD; by his mouth they go out and by his mouth they come in" (Num 27:21).
THE TEACHERS READ EXACTLY THIS. Sanhedrin 8a:4: Moses "did not know the answer himself and was compelled to ask God," and Rav
Nachman bar Yitzchak's gloss on "I will hear" — "if I have learned the halakha, I have learned it; and if not, I will go and
learn it" (a lookup, then a fetch). Sanhedrin 8a:5 and Sifrei Bamidbar 80:1: the law "would have been fitting to be written by
attributing it to Moses" but is written IN THE CASE'S NAME — the daughters', the wood-gatherer's, Jethro's — the case that
raised it earns the credit line. Sanhedrin 78b:4-7: the two uncertainties told apart — the wood-gatherer known liable, the
MODE unknown; the blasphemer not known liable at all — and incarceration itself derived from the halt. Bava Batra 110b:4:
"after God spoke to Moses, the Torah was given and a halakha was initiated." Bava Batra 119b:10: the daughters' own ARGUMENT
at the tent — an inference on the levirate law already on the books ("if we are each like a son, give us an inheritance; if
not, our mother should enter levirate marriage") — the case arrived carrying a computation for the tent to grade. And THE
OUTPUT'S TWO PARTS split on the page: Sifrei Bamidbar 114:1 on Num 15:35 — "die, shall die the man: this is the judgment for
ALL THE GENERATIONS; stone him with stones: in THIS PARTICULAR INSTANCE"; Sanhedrin 80b:5 the dispute over which part is which
— the first tanna deriving a general rule (forewarning) from the wood-gatherer, Rabbi Yehuda calling his execution "a
provisional edict based on the word of God," not code.
WHAT IT CHANGES. The code is not fixed before the run. The run produces inputs the code does not cover; the text records the
halt (custody — an open entry on the court's docket), the submission, and an output that is part VERDICT on the instance and
part NEW RULE that joins the code and runs forward, written at the verse where the case arose. So the one sequential run in
verse order IS the loop the owner was asking about: read a verse — if it is a case no rule consumes, the engine's own
"unconsumed" count (the daemon gate's instrument, today 0) gets its ink name, "it had not been declared," and the world writes
custody — then the tent's output verse INSTALLS the rule (step 3's installation by a case event, not only by a command) and the
run continues. For NUMBERS' OPENING BLOCK the four uncovered cases are the marquee: the engine must (1) recognize a submitted
case with no consuming daemon and write the custody entry instead of silence; (2) consume the output verse as the installation
of a new law (law_inheritance at Num 27:8-11 is a forward debt on this file's own map; the second Passover's code at 9:10-14
already compiled); (3) carry the Sifrei's split — the generations' rule and the instance's verdict — as two effects, and
Sanhedrin 80b's fork (code or a one-time edict) as two settings; (4) at the daughters' case, RUN THEIR ARGUMENT on the
compiled levirate function before reading the answer, and grade the tent's output against it — the world as the oracle, step
5's own shape, arrived at from the ink rather than designed.

WHAT IT SAYS TO THE DESIGN. Two passes is an undercount. The tradition's own structure of the law is THREE: the general giving,
the detailed giving, the repetition after the run (Sinai, the Tent, the plains of Moab) — and Rabbi Akiva's rule that each pass
restates the WHOLE, not a delta. Mapped onto the loop: pass one builds the world whole with the program already present (the
Torah before the world; full stature); pass two runs the text in time order with each law installed where the text installs it
(step 3), its details never changing what an earlier run produced (Chagigah 6b:2 — the gate that a re-run is byte-identical);
pass three re-reads the text against the ledger the run left (Deuteronomy's pass, the prophets against the open entries — the
effects law's target). The teaching protocol adds the rule that the passes are counted (four) and that understanding is the
LAST pass, not the first. Nothing here licenses a design of ours; it is what the shelf says when asked about passes, recorded
so the loop's later steps can cite it.

## Decisions not yet made (listed for the owner 2026-09-09, "what are the decisions we didn't make yet"; each is the owner's call
## or a design section's first paragraph — none is decided by this list)

INSTALLATION (step 3):
- D1 Which worlds track installation. DECIDED (the owner, 2026-09-09): ONLY THE SEQUENCE WORLD opts in; the 38 exam worlds keep
  every law in force from boot — a test bench is not history; the sweep's 38 scores stay put, only the sequence tuple moves.
- D2 Which setting is the running one — in force from boot ("Abraham kept the whole Torah", Yoma 28b) or in force from its
  installing event — and whether the other runs as a fork world beside it, as the sojourn fork does. DECIDED (the owner,
  2026-09-09, on his own fourth option — "we are still guessing until we finish the last two books"): BUILD THE MECHANISM,
  DEFER THE SETTING. Every daemon carries installed_by = boot, a verse, or PENDING (its installing or repeating verse lies in a
  book not yet compiled — M-24's second writing); pending behaves as boot and is COUNTED as debt; the main run stays
  everything-from-boot until the five books are compiled; the installed run is the second pass after Deuteronomy, and the
  from-boot / from-its-event fork is decided then, on the whole program.
  ⚠ A NOTE ON D2'S LABEL (2026-09-14, the owner's question "why do you think the saying 'Abraham kept the whole Torah' means every law runs
  from the start"; his word: "note it"): IT DOES NOT. Yoma 28b (Rav on Genesis 26:5) says one man KEPT the whole Torah before it was given —
  the laws' content existed and he observed it; it says nothing of the world being BOUND. Being bound begins with the giving: Chagigah
  6b:2 (the daily offering did not run before its details were given), Sanhedrin 59a:11-12 (a law stated to the sons of Noah and
  repeated at Sinai binds all; stated at Sinai alone binds Israel from Sinai) — that is the from_event setting, and it is the one with
  a teacher behind it. The boot setting is THE ENGINE'S BASELINE — no gating, every watcher on, the state before installation existed —
  and the saying was reached for as the nearest thing on the shelf that made laws exist before Sinai; existing and binding are two
  claims and the label conflated them. THE DECISION STANDS as ruled (the mechanism built, the setting deferred to the second pass after
  Deuteronomy, the would-be skips counted); THE LABEL IS CORRECTED: boot = the baseline without a teacher, from_event = the tradition's
  own rule. The second pass compares the baseline to the tradition's rule, not two readings of the tradition.
- D3 What counts as an installing event: the command verse (the spec), the act (the erection, the investiture), or a case's
  output from the tent (the four uncovered cases). DECIDED (the owner, 2026-09-09): TWO FIELDS on every daemon — given_at (the
  verse where the law is spoken, always in the ink) and installed_by (the ACT that switches it on: a registered act kind such
  as the erection, the investiture, the giving at Sinai, or a tent's output; or boot; or pending). In force needs both — spoken,
  and its institution standing (Chagigah 6b:2's rule that the daily offering did not run before its details were given).
- D4 Which entity carries `in_force` for each institution (the tent, the priesthood's office, the covenant, the court, the
  land) — and whether the tent becomes a registry entity with a daemon of its own that consumes a case brought before the LORD.
  DECIDED (the owner, 2026-09-09): INSTITUTION ENTITIES, THE TENT INCLUDED, WITH A TENT DAEMON — one registry entity per
  institution, in_force a status on its ledger written by the installing act's daemon and read by World.submit before a law is
  called; the tent's own daemon consumes a case brought before the LORD and installs the case-born law from the output verse.
  Everything in the ledger, visible in the journal.
THE TENT'S OUTPUT:
- D5 Whether an event no daemon consumes writes CUSTODY (a new effect, on the court's docket) instead of silence — and what
  closes it (the output verse). DECIDED (the owner, 2026-09-09): CUSTODY ON THE COURT'S DOCKET, CLOSED BY THE OUTPUT VERSE —
  the tent daemon writes the new effect in_custody on the court's docket entity when the case's event fired no law; it stays
  open until the output verse's rule or verdict closes it; open custody at the run's end is a printed finding; the engine's
  unconsumed count stays the separate tripwire it is today. (The docket entry's REGISTERED name is declaration_owed — at step
  3's registration in_custody was found already registered as Joseph's body status on the held person, Gen 40:3, and a name
  reused is a miss; the person's state at the halt is that existing effect, the docket's debit is the ink's own second phrase,
  "to be declared to them" — the design section below.)
- D6 Whether the output is carried as two effects (the generations' rule and the instance's verdict, Sifrei Bamidbar 114:1)
  and Sanhedrin 80b's code-or-edict fork as two settings. DECIDED (the owner, 2026-09-09): TWO EFFECTS AND THE DISPUTE AS A
  PARAMETER ROW — the output verse writes the instance's verdict on the person (the existing vocabulary) and rule_installed
  on the institution (the generations' rule, the installation of the case-born law); the code-or-edict dispute a data row
  with two settings, the first tanna's the running one, Rabbi Yehuda's provisional edict recorded and printed as a fork.
THE JOURNAL (steps 2 and 4):
- D7 One database or two: the World folder's world.sqlite (the reading era's corpus world, 557 events) and the journal's
  world.sqlite (the engine's runs) — merge into one index, or keep the two with a stated boundary. DECIDED (the owner,
  2026-09-09; his question "does this replace the database" answered: no — the journal replaces the FOLD as the database's
  source, the database stays the one place to ask): ONE DATABASE, BUILT FROM THE JOURNAL; THE MERGE INSIDE STEP 2 as its own
  sitting — the corpus world's fold becomes a journal layer (L0 already is the frozen units' operators), the World folder's
  tables become views rebuilt from the journal, the reconciliation gate moves upstream (the journal's scripture layer must
  reproduce the fold's counts and the hash). Until the merge, the boundary is stated: World/world.sqlite = the reading era's
  model, the journal's index = the runs.
- D8 Step 2's tables beyond the generic events table: the ledger view with open and close days, the timers joined, the markers
  as the clock; and what the ask-tool answers first. DECIDED (the owner, 2026-09-09): THE FOUR RUN VIEWS AND FOUR QUESTIONS —
  views rebuilt from the events table: the LEDGER (entity, effect, day written, day closed, closed by), the TIMERS (set, fired
  or cancelled, joined by subject and effect), the CLOCK (the markers in order with their class), the DOCKET (custody open and
  closed); the ask-tool answers an entity's ledger at a day, what stands open at a verse, who wrote this, what waits in
  custody. Built at step 2's remainder, before the merge.
- D9 When a new segment starts once step 4 appends: per run, per world, per cursor position; and whether the exam worlds are
  journaled too (today only the sequence runner sinks). DECIDED (the owner, 2026-09-09): BASE SEGMENT PLUS AN APPENDED SEGMENT
  PER RESUMED RUN; EXAM WORLDS NOT JOURNALED — the full tape's run is the BASE segment (fixed path, byte-identical, the gate); a
  resumed run replays to the cursor without re-journaling and appends its new submissions as a NEW segment whose chain
  continues from the base's chain head, named by the cursor verse; the 38 exam worlds stay unjournaled test benches (D1).
- D10 The August tree checklist's forming/filling line, failing against today's units: fix the tree model or retire it.
  DECIDED (the owner, 2026-09-09): RETIRE IT AT THE MERGE; A PRINTED KNOWN-FAIL UNTIL THEN — D7's merge replaces the August
  fold with the corpus world's own fold as a journal layer, and the tree and its checklist go with it; until then the line
  prints FAIL and gates nothing; no reading sitting on a model being superseded.
SEQUENCING:
- D11 Steps 4 and 5 before Numbers, or interleaved with Numbers' opening block where the four cases need them. DECIDED (the
  owner, 2026-09-09): STEP 3, THEN STEP 2'S VIEWS, THEN NUMBERS OPENS; STEPS 4 AND 5 WHEN THE CASES CALL FOR THEM — Numbers'
  opening block builds the tent daemon, custody and the case-born installation on real verses; the cursor and scenarios arrive
  at the daughters' case, where running their argument before the answer is step 5's shape. The standing duty (the loop named
  at every compaction point until step 4 lands) holds throughout.
- D12 Whether the third pass — the text re-read against the ledger the run left (Deuteronomy's pass, the prophets against the
  open entries) — becomes a named step of the loop with a box on the map, or stays the effects law's target. DECIDED (the owner,
  2026-09-09): NAMED NOW AS STEP 6, THE READBACK, WITH A BOX ON THE MAP AND A ROW IN THE TABLE, NO DESIGN YET — its first
  exemplar Deuteronomy's own repetition of the laws read against the run's ledger, the prophets against the open entries
  after; its design section waits for Deuteronomy.
- D13 The commit ("commit push"): everything since b4b40ce is uncommitted. DECIDED (the owner, 2026-09-09): "Commit push now" —
  one commit carrying the closed campaign, the loop's first step, the journal's move, the shelf readings and these decisions,
  pushed as Josephtorah; a clean point to compact from.

## Step 3 INSTALLATION — the design (2026-09-09, the loop's second sitting; the owner: "ok step 3 go"; written under D1-D6
## BEFORE the registers, the probes and the code; the shelf seats re-opened first: Yoma 28b:9-10, Kiddushin 82a:10, Chagigah 6b:1-2,
## Sanhedrin 80b:5)

WHAT IS INSTALLED. A law is IN FORCE when two things hold (D3; Chagigah 6b:2 — "it is not plausible that the details of a mitzva
would change over time," so the daily offering did not run before its details were given in the tent): it has been SPOKEN — the
run's position in the text has reached the verse where the law is given — and the INSTITUTION its clause presupposes STANDS — the
act that erects that institution has fired and written its status. So every daemon carries TWO FIELDS in daemon_dispositions.yaml:
- `given_at:` — the verse where the law is spoken, always in the ink: the first verse of the daemon's wrapped span (by script from
  dependency_dispositions.yaml's `spans`; the library's five from the function each wraps: Exod 21:2, 21:28, 22:6, Lev 5:20, 8:1).
- `installed_by:` — the ACT that switches it on, one of three values: `boot` (in force from creation — the story daemons and the
  Noahide code, whose "law" is the deed the text records); a REGISTERED ACT KIND that erects an institution (the table below); or
  `pending` — the installing act is not yet on the tape or in the registry (a verse of a book not yet compiled, or a tent's output
  verse that registers with Numbers' opening block), with a `why:`; pending BEHAVES AS BOOT and is COUNTED as debt (D2).
THE 43 ROWS, decided by hand, each from the clause's own precondition (the count by value, summed to 43 before the file is touched):
- boot 7: law_pre_sinai, law_primeval, law_mamre, law_joseph, law_family, law_exodus_story, law_erection — the history's daemons;
  the laws written inside the story (the calf's bans, the covenant's own clauses) are written at their acts.
- covenant_blood_thrown 13 (Exod 24:8 "the blood of the covenant which the LORD has cut with you UPON ALL THESE WORDS" — the ink
  binding the words to the act; Rabbi Yishmael, Chagigah 6b:1: the general statements at Sinai): law_slave_term, law_goring_ox,
  law_guardians, law_decalogue, law_ordinances, law_mishpatim, law_mishpatim_2, law_mishpatim_3, law_calendar, law_sabbath,
  law_sanctuary_build, law_vestments (the spec's makings run before any erection — the covenant is their institution), law_tochacha
  (the covenant's own sanctions, Lev 26:9, 15, 42, 44-45; the exile's land condition is read off the land's ledger inside the code).
- erected 3 (Exod 40:17 הוּקַם הַמִּשְׁכָּן, "the tabernacle was erected"): law_installation (Lev 8:3-4 "at the entrance of the tent
  of meeting" — the tent must stand; in TAPE order the erection precedes Lev 8's retrograde stretch), law_investiture (Exod 29:4 the
  same entrance), law_eighth_day (Lev 9:1 — the service's first day is the erection's day).
- called_from_the_tent 16 (Lev 1:1 וַיִּקְרָא אֶל מֹשֶׁה וַיְדַבֵּר יְהוָה אֵלָיו מֵאֹהֶל מוֹעֵד, "and He called to Moses and the LORD
  spoke to him from the tent of meeting" — the DETAIL PASS opens, Chagigah 6b:1): law_deposit_oath, law_offerings, law_minchah,
  law_chatat, law_vayikra5, law_tzav, law_shemini, law_clocks, law_negaim, law_metzora, law_yoma, law_sanctions, law_holiness,
  law_holiness_b, law_moadim, law_temurah — every Leviticus law spoken from the tent.
- milluim_blood_sprinkled 1 (Lev 8:30; the Sifra, Mekhilta DeMiluim I 34 — the office consummated at the blood): law_priesthood
  (Lev 21-22, 24:1-9 — the priest's file presupposes a priest invested).
- entered_the_land 1 (Lev 25:2 "when you come into the land which I give you, the land shall keep a sabbath" — the ink's own
  condition; the count's timers are set at the entry): law_yovel. The kind is registered (a case form, submitted by exam scenes)
  and NEVER FIRES on the sequence tape — so under the deferred setting the jubilee's daemon would stand not-in-force through the
  whole run, which is the truth of the three books.
- pending 2: law_pesach (the Passover's giving at Exod 12:1-2 is not an EVENT on the tape — the stitcher carries Exod 12:2 as the
  epoch MARKER only; the tape's Exodus 12 events begin at 12:29; the installing act registers when the Passover's own acts, 12:3
  the lamb taken and 12:28 "they did," join the tape); law_lev24 (the blasphemer's law is CASE-BORN — its installing act is the
  tent's output at Lev 24:13, whose kind registers at Numbers' opening block with the four cases; THE_LOOP.md "The tent as the
  run's interrupt"). Sum: 7 + 13 + 3 + 16 + 1 + 1 + 2 = 43.

THE INSTITUTIONS (D4) — one registry entity each, `kind: institution` in logic/corpus/entity_registry.yaml with a step9-scenes
member, so a scene token and the institution write one ledger: the_tent_of_meeting (the-tabernacle — its existing writes,
tabernacle_erected among them, re-home to it), the_priesthood (the-priesthood — the OFFICE, not the persons aaron-and-sons who
carry invested_office), the_covenant_at_sinai (the-covenant), the_court (the-court — the ordinances' majority_decides re-homes to
it), and THE LAND = the standing entity the_land_of_canaan (the-land-of-canaan; the runners' generic 'the-land' is NOT re-homed — O8
S3's lesson stands; the join of the two lands is filed for the merge sitting, D7). The table of INSTALLING ACTS lives in a FOURTH
REGISTRY, World/step9/installation_parameters.yaml, keyed by the act kind (one institution may be switched on by two acts — the
tent by its erection and again by its first speech): erected → the_tent_of_meeting; called_from_the_tent → the_tent_of_meeting;
milluim_blood_sprinkled → the_priesthood; covenant_blood_thrown → the_covenant_at_sinai; judges_appointed → the_court (Exod 18:25-26
"and they judged the people at all times"); entered_the_land → the_land_of_canaan. The same file carries the two PARAMETER ROWS in
calendar_parameters.yaml's shape: `installation_setting` — value `boot` (Yoma 28b:9-10, Kiddushin 82a:10: Abraham kept the whole
Torah before it was given; Rav Shimi bar Chiyya's counter, the seven alone, recorded), the other setting `from_event` (Chagigah
6b:2), channel OPEN under D2, the running value decided at the second pass after Deuteronomy; and `case_output` — value
`rule_for_the_generations` (the first tanna, Sanhedrin 80b:5, forewarning derived from the wood-gatherer; Sifrei Bamidbar 114:1 "this
is the judgment for all the generations" / "in this particular instance"), the other setting `provisional_edict` (Rabbi Yehuda,
Sanhedrin 80b:5 — "a provisional edict based on the word of God; the halakha throughout the generations cannot be derived from
it"), UNEXERCISED until Numbers' opening block and printed so.

THE EFFECTS (three, registered in effect_vocabulary.yaml BEFORE any daemon names them, each with the ink's own words machine-read
from the Tanakh DB — the tradition's vocabulary, never designed):
- `in_force` (status, on the institution; value = the installing act): the ink's own binding "upon all these words" (Exod 24:8) and
  the Mishnah's own word for a law's being in force conditioned on an institution — נוֹהֵג בִּפְנֵי הַבַּיִת ("in force while the
  House stands," Mishnah Chullin 5:1; מִצְוָה הַתְּלוּיָה בָּאָרֶץ, "a commandment dependent on the land," Mishnah Kiddushin 1:9).
- `declaration_owed` (DEBIT, on the court's docket, the case's person the counterparty; OPEN until the output verse closes it —
  a debit because the docket OWES a declaration, and World.close finds only open entries): the ink's own words for the halt —
  לִפְרֹשׁ לָהֶם עַל פִּי יְהוָה "to be declared to them by the mouth of the LORD" (Lev 24:12), כִּי לֹא פֹרַשׁ מַה יֵּעָשֶׂה לוֹ
  "because it had not been declared what should be done to him" (Num 15:34); Sanhedrin 78b:4-7 derives the incarceration from the
  halt. THE NAME CAUGHT BY THE REGISTRY: the design first named this entry in_custody, and the appender found `in_custody` ALREADY
  REGISTERED — Joseph's engine's BODY status on the held person (Gen 40:3, the same word מִשְׁמָר, the guard, at 43 Torah seats
  machine-counted, Lev 24:12 and Num 15:34 among them). A name reused is a miss (O9's lesson): the person's state at the halt is
  that existing effect, written beside the docket's debit; the docket's entry takes the ink's own second phrase.
- `rule_installed` (status, on the institution; value = the daemon the output verse installs — THE GENERATIONS' RULE): וְהָיְתָה
  לִבְנֵי יִשְׂרָאֵל לְחֻקַּת מִשְׁפָּט "and it shall be to the children of Israel a statute of judgment" (Num 27:11 — the daughters'
  output; the phrase's only other Torah seat Num 35:29, the refuge cities, machine-verified), שָׁם שָׂם לוֹ חֹק וּמִשְׁפָּט "there He
  set for him a statute and an ordinance" (Exod 15:25 — Marah, the ink's own installation verb, ALREADY ON THE TAPE as statute_set),
  חֻקָּה אַחַת "one statute" (Num 9:14, the second Passover's output).
The instance's verdict stays the existing vocabulary (stoned, karet_cut_off …), written by the case's own compiled daemon (D6).

THE ENGINE (World.submit; the dispatch gate NEVER at registration — CLOCK.md section 8): a world OPTS IN with `installation=` (D1:
the sequence runner's four worlds; the 38 exam worlds pass nothing and are untouched — no field read, no line logged, no write).
On opt-in the engine loads the two fields for every registered daemon from daemon_dispositions.yaml (a daemon without both fields
is refused at once) and the setting from the parameter row unless the caller names one. The engine tracks THE VERSE REACHED — the
canonical maximum over every marker's verse and every event's first cited verse (Gen < Exod < Lev < Num < Deut; a retrograde
stretch never lowers it). Before each daemon is called the engine asks NOT-IN-FORCE: boot or pending → in force; else NOT GIVEN if
the verse reached is before given_at; else the act's institution entity must carry an `in_force` entry whose value is that act,
OR any institution must carry a `rule_installed` entry naming this daemon (installation BY A CASE EVENT — the tent's output, D5/D6);
else NOT IN FORCE. Under `from_event` a daemon not in force is SKIPPED: an eighth LOG CLASS, ('SKIP', day, {daemon, kind, subject,
case_source, why: not_given | not_in_force, needs}) — registered in the journal as run.skip before first use, counted per daemon in
the watch coverage, printed in the RUN line as "skipped n", and the journal gate's counts parse it. Under `boot` (the running
setting, D2) NOTHING IS SKIPPED and NO LINE IS LOGGED; the engine counts what WOULD have been skipped and the runner prints it — an
instrument for the deferred decision, not a graded cell. THE CONSUMERS STAMPED: submit records on the event itself which daemons
fired on it (`fired_by`, beside the engine's own bound/dated/placement stamps), so the journal's EVENT line names its consumers and
an unconsumed case is readable off the tape — the custody rule's own input at Numbers.

THE TENT DAEMON (D4) — `law_tent`, the library's sixth, in world_engine.py, REGISTERED FIRST in the sequence runner's daemon order
so that an installing act switches on its laws INSIDE ITS OWN DISPATCH (Lev 25:2: the entry itself starts the count — the
consumers of the installing act run after the tent daemon in the same submit). Today it consumes the six installing acts and writes
`in_force` on the act's institution (a literal branch per kind — the daemon gate's parser reads branches; the entity from the
fourth registry). At Numbers' opening block it gains the custody branch — consuming the ink's own custody ACT ("and they placed
him in the guard" is a narrated deed on the tape, in the story's own "and he did" form, not a computed consequence): in_custody on the person and declaration_owed on
the court's docket, with `covered_by` read off the person's LEDGER (the daemons that already wrote on the case's verse — under
the boot setting the blasphemer's compiled law fires before the halt, and the docket entry records that the code decided what
the ink says was not yet declared: the installation setting's own evidence, printed) — and the output branch (the verse "by the
mouth of the LORD" → rule_installed on the institution + the docket's debit closed by World.close), on the real kinds registered
with their witnesses then. Today those two paths are exercised on the PROBE world by a probe daemon over registered kinds (the
blasphemer's own case kind cursed_the_name, consumed by no law on the probe world; Joseph's custody_three_days standing in for
the custody act; Marah's statute_set as the output act).

THE DAEMON GATE (daemon_census.py) demands both fields on every declared daemon: given_at a verse the engine's parser reads;
installed_by boot, pending (with a why), or a key of the fourth registry's installing acts, each of which must itself be a
registered event kind. The sequence runner's own assertion keeps DAEMON_ORDER equal to the declared set (law_tent joins both).

THE PROBES, written to FAIL on the unchanged engine — World/step9/installation_probes.py, six, in-process on a small world:
I1 under from_event a law whose installing act has not fired is SKIPPED (a SKIP line, no write, the daemon's skipped count 1);
I2 after the act fires the institution's ledger carries in_force (written by law_tent, prov the act's verse) and the same law FIRES;
I3 in force needs BOTH — a law whose institution stands but whose given_at the tape has not reached is skipped as not_given;
I4 under boot nothing is skipped, no SKIP line exists, the would-skip count is reported; a world that did not opt in has no
installation, no SKIP line and no in_force write (the exam bench, D1);
I5 the gate refuses a daemon missing either field or naming an unregistered act (the check as an importable function);
I6 custody and the case-born installation: a case no daemon consumed carries fired_by [] (a SKIP line for the law not in force);
the custody act writes in_custody on the person and declaration_owed OPEN on the court's docket; the output act writes
rule_installed naming a law whose own act never fires, closes the docket's debit, and that law fires on the next case —
installation by a case event.

THE PREDICTION (print-then-type, written BEFORE the run). The main run stays on `boot` (D2), so the graded sequence cells move only
by the tent daemon's own writes: the five installing acts on the tape (judges_appointed Exod 18:25, covenant_blood_thrown 24:6-8,
erected 40:17, called_from_the_tent Lev 1:1, milluim_blood_sprinkled Lev 8:30; entered_the_land never fires) = FIVE in_force WRITES
on every sequence world, TWO NEW ENTITIES (the-covenant, the-priesthood; the tent and the court re-home onto existing ledgers), ONE
MORE DAEMON FIRED. RUN: (1058, 43, 39, 0, 0, 1224 → 1229, 12 → 13, 252 → 254, the overlap and the closes unchanged); PREVIOUS_RUN
(THE REST, the tape minus joseph, which holds all five acts): (749, 31, 27, 0, 0, 907 → 912, 11 → 12, 219 → 221, unchanged,
unchanged); skipped 0 on every world; the pending count printed 2; the would-skip count MEASURED (not predicted — the instrument's
first reading); the 38 exam runners' cells unchanged, the sweep 39/39 at 4,518; the journal gate byte-identical with the counts
parsing the new class; the ten checkpoints unmoved.

## As built — step 3 INSTALLATION (2026-09-09, the loop's second sitting; the owner: "ok step 3 go")

THE ORDER HELD: the four shelf seats re-opened at their addresses; the design section above; the registers before any code — run.skip
into World/journal/registers/event_kinds.yaml (35 kinds), the three effects into effect_vocabulary.yaml by an appender in the E5 form
with the `he` read from the pointed Tanakh DB (908 effects), the FOURTH REGISTRY World/step9/installation_parameters.yaml (two
parameter rows, six installing acts), the four institution entities into logic/corpus/entity_registry.yaml with a changelog line
(272 entities; a new `kind: institution`); the probes second — World/step9/installation_probes.py, six, 0/6 on the unchanged engine
(every FAIL the construct's absence: no law_tent, no check_installation); the 43 rows third by scratchpad/step3_rows.py (given_at by
script from the spans, installed_by from the design's table, the count re-summed to 43 before the write; two corrections caught by
the script's own asserts — the tabernacle's Sabbath clause is given at Exod 31:12, not its file's first span, and a daemon key may
carry a trailing comment); the code fourth — world_engine.py (the fourth registry loaded; verse_key; World.install /
installation_report / _reach / not_in_force / skips; the dispatch gate and the consumers' stamp in submit; the marker reaching; the
tent daemon law_tent with six literal branches), daemon_census.py (check_installation, wired into the gate, the index line carrying
both fields), world_journal.py (the eighth class and its unit; the tuple parse), cold_run_sequence.py (law_tent first in
DAEMON_ORDER; the four worlds opted in; the RUN line's "skipped"; the INSTALLATION print), daemon_dispositions.yaml (law_tent
declared, six watches); then the gates.

THE NAME CAUGHT BY THE REGISTRY: the design's docket effect was first named in_custody; the appender found in_custody ALREADY
REGISTERED — Joseph's body status on the held person (O8 S4, Gen 40:3, the same word מִשְׁמָר, the guard). A name reused is a miss:
the docket's entry became declaration_owed (a DEBIT — the docket owes a declaration, and World.close finds only open entries), the
person's state stays the existing effect, D5's line carries the note.

THE PROBES: 4/6 on the first run after the code — I3 and I6 were written TOO NARROW, not the engine wrong: a law given later is
skipped as not_given on EVERY earlier event (the law does not exist yet), and a law consulted once its verse is reached is skipped
not_in_force on every event until its act or its rule_installed lands — including the output act's own dispatch, since the probe's
tent daemon writes rule_installed after the case law was consulted. The probes now read the skip AT THE VERSE and the silence
after; 6/6. Journal probe J3 moved with the sink's eighth class (its "seven" is now KINDS less run.skip, every class registered, and
run.skip's own exercise is I1's sunk and indexed from_event world); 6/6. Clock 22/22, sequence 4/4, the daemon gate satisfied with
44 daemons and 908 effects.

THE PREDICTION MET ON THE FIRST RUN: RUN (1058, 43, 39, 0, 0, 1229, 13, 254, …, 74) and THE REST (749, 31, 27, 0, 0, 912, 12, 221,
…, 56) — writes +5, daemons fired +1, entities +2 on both, exactly as the design section typed them before the run; the two
literals then retyped, 10/10 checkpoints; skipped 0 on every world; the running setting boot. THE INSTRUMENT'S FIRST READING:
"would be skipped under from_event: 34,729 calls" of the 46,552 the tape makes (44 daemons × 1,058 events) — most of them
Leviticus laws not yet given during Genesis and Exodus, the rest laws consulted before their institution stood; the reading the
second pass after Deuteronomy will decide on (D2). THE INSTITUTIONS IN FORCE on the tape, as the tent daemon wrote them: the court
by judges_appointed at Exod 18:25-26; the covenant by covenant_blood_thrown at Exod 24:6-8; the tent by erected at Exod 40:17-18
and again by called_from_the_tent at Lev 1:1; the priesthood by milluim_blood_sprinkled at Lev 8:30; the land never (its act is
not on the three books' tape). The 44 daemons by value on the sequence world: boot 8 (the seven story daemons and the tent daemon
itself), by an act 34, pending 2 (law_pesach, law_lev24 — the debt, named in the file and printed every run).

THE JOURNAL: every segment +5 lines (2,499 / 2,499 / 2,499 / 1,849), coerced 0; every EVENT line now carries `fired_by`; the index
15,947 rows over the seven segments; the two-process gate GREEN — four segments byte-identical, four chains verified, the running
world's counts equal to the RUN tuple with run.skip 0 parsed. THE SWEEP after the gates: 39/39 runners green, 4,518 graded cells —
UNMOVED (the 38 exam worlds opted into nothing; the sequence runner 10/10 inside it), both gates satisfied at its head.

⚠ LESSONS: A NAME IS CHECKED IN THE REGISTRY BEFORE THE DESIGN NAMES IT (in_custody). A LATER-GIVEN LAW IS SKIPPED ON EVERY
EARLIER EVENT — a probe counts the skip at the verse, never all skips. THE OUTPUT ACT'S OWN DISPATCH DOES NOT SWITCH ON THE LAW
IT INSTALLS unless the installer runs before the consumer — the tent daemon is first for the installing acts; the case-born
rule takes effect from the next event. A KEY MAY CARRY A TRAILING COMMENT (the row inserter's regex). THE FILE'S FIRST SPAN IS NOT
EVERY DAEMON'S VERSE (law_sabbath).

NEXT (D11): step 2's remainder — the four run views (ledger, timers, clock, docket) and the four questions, before Numbers opens;
then NUMBERS' OPENING BLOCK on the tent's four cases, where the tent daemon gains its custody and output branches on real kinds.

## Step 2 THE INDEX — the remainder: the four views and the four questions (the design, 2026-09-09, the loop's third sitting;
## the owner: "No need to compact. Continue"; under D7 (the boundary stated, the merge its own sitting) and D8; written before
## the probes, the probes before the code)

WHAT THE INDEX LACKS, measured: worldledger's events table (seq, op, layer, kind, subj, data, unit, ref, chain) carries no
SEGMENT column — the four L3 worlds' rows are mixed and their seq restarts per segment; a WRITE row's data carries the day it was
written (`day`) and, if closed, `closed_by`, but NOT THE DAY IT CLOSED — World.close records the note alone. Two additive
changes, each with a probe that fails first: (1) the events table gains `source` (the segment header's own field, read where the
builder discards the header line today) — D9's appended segments need it too; (2) World.close stamps `closed_day` (the clock's day
at the closing act) beside `closed_by`.

THE FOUR VIEWS (D8) are SQL VIEWS over the events table, declared in ONE file, World/journal/run_views.sql, created at every
reindex after the table is rebuilt — "rebuilt from the events table" literally, never written directly, json_extract over `data`:
- run_ledger — one row per run.write / run.retro_write: source, seq, entity (subj), effect, ledger_op, day_written (op), year,
  value, counterparty, open, day_closed, closed_by, written_by (unit), verse (ref), kind.
- run_timers — one row per run.timer_set, joined LEFT to its fire and to its cancel on (source, entity, effect, due = the fire's
  or cancel's day): day_set, due, outcome fired | cancelled | pending, day_fired, day_cancelled, cancelled_by, rearmed_from,
  written_by, verse. A period timer's re-arm is its own set row.
- run_clock — one row per run.marker in seq order: day (op), verse (ref), value, class forward | retrograde | proleptic, stated,
  placement.
- run_docket — run_ledger where effect = declaration_owed: entity (the court), the person (counterparty), day_written, open,
  day_closed, closed_by — today ZERO rows on the tape (the custody act joins it at Numbers), rows on the probe world.

THE FOUR QUESTIONS (the ask-tool, `python3 World/step9/world_journal.py --ask … [--world <source>]`, the running setting's world
the default), each one SQL over the views:
1. an entity's LEDGER AT A DAY — `--ask ledger <entity> [<day>]`: the entries written at or before the day, each with its state AS
   OF that day (open unless day_closed is at or before it);
2. WHAT STANDS OPEN AT A VERSE — `--ask open <verse>`: the day is the verse's own (the first marker or event whose ref opens with
   it); the open-capable entries (debit, heaven, body) written at or before that day and not closed by it, by entity;
3. WHO WROTE THIS — `--ask who <entity> <effect>`: the writing daemon, the verse and the day of every such entry (step 1's
   question, now a view);
4. WHAT WAITS IN CUSTODY — `--ask custody`: the open docket rows.

THE GATE, inside `--gate` after the counts check and standing alone as `--views`: for EVERY source in the index, run_ledger's rows
= run.write + run.retro_write; run_timers' rows = run.timer_set; its fired rows = run.timer_fire and its cancelled rows =
run.timer_cancel (the joins 1:1 — a duplicate join or an orphan fire moves a count); run_clock's rows = run.marker; run_docket's
rows = run_ledger's declaration_owed rows. Every view count is DERIVED from the events table's own counts, never typed.

THE PROBES, written to FAIL on the unchanged code — World/step9/view_probes.py, six, on a small world exercising all eight
classes plus a close and a custody (the journal probes' tape extended by registered kinds): V1 the index carries each row's
source, and a closed entry carries closed_day; V2 run_ledger's rows equal the write rows and the closed entry shows its day and
its closer; V3 run_timers joins every fire and every cancel to exactly one set and shows the pending one; V4 run_clock lists
the markers in order with all three classes; V5 run_docket shows the declaration owed open, then closed at the output; V6 the
four questions answer on the probe world (the ledger at a day before and after the close; what stands open at a verse; who
wrote this; what waits in custody — one row, then none).

THE PREDICTION: no graded cell moves (the views read; the engine's one stamp is a field on a closed entry); the four segments'
bytes change by the closed_day field alone and stay byte-identical across two processes; the index's row count is unchanged
(15,947); the sweep 39/39 at 4,518.

## As built — step 2's remainder: the four views and the four questions (2026-09-09, the loop's third sitting)

THE ORDER HELD: the design section above; the probes second — World/step9/view_probes.py, six on a small world exercising all eight
log classes, a close and a custody (the journal probes' tape extended by Joseph's custody_three_days as the custody act, Marah's
statute_set as the output act, a law skipped under from_event until the output installs it, a third timer left pending, a
proleptic marker), 0/6 on the unchanged code (every FAIL the module's absence); the code third — World/journal/worldledger.py
(the events table gains `source` from the segment header it discarded, with its index), world_engine.py's one stamp
(World.close writes closed_day beside closed_by), World/journal/run_views.sql NEW (the four views as SQL VIEWS with json_extract over
`data`), World/step9/world_journal.py (views, view_counts, views_gate, ask, the CLI `--views` and `--ask … [--world …]`; reindex
creates the views; the two-process gate runs the views gate after the counts check); then 6/6, journal 6/6, installation 6/6,
clock 22/22, sequence 4/4.

THE VIEWS ON THE REAL INDEX (every count derived from the events table's own, on every world — MATCH): the running world ledger
1,229 = writes 1,229; timers 43 = sets 43 (fired 39 = fires 39, cancelled 0, pending 4 — the joins 1:1); clock 130 = markers 130;
docket 0 (the custody act joins the tape at Numbers); skips 0; the fork's two worlds the same; THE REST 912 / 31 / 27 / 130. The
index 15,947 rows, unchanged; the segments byte-identical across two processes with the closed_day field aboard (74 closed
entries now carry the day they closed); GATE GREEN with the views inside it.

THE FOUR QUESTIONS ANSWERED ON THE TAPE: "who wrote this" — the covenant's in_force: law_tent at Exod 24:6-8, day 894379, value
covenant_blood_thrown; "an entity's ledger at a day" — the tent of meeting at the erection's day (894698): eight entries, made_one
and work_completed from the spec's run (day 894460), in_force by erected and tabernacle_erected and veil_divides at 40:17-21, the
glory's HEAVEN entry OPEN at 40:34, in_force again by called_from_the_tent at Lev 1:1; "what stands open at a verse" — at Exod
40:17, 141 open entries across the world, Abel's regarded offering and Abraham's promised nation among them (the open promises
the effects law aims the prophets at); "what waits in custody" — none, as the three books' tape has no halt.

THE AUGUST TREE MEASURED AGAIN (D10 — a printed known-FAIL that gates nothing): build_world.py's checklist fails FOUR lines on
today's units (roots born at Gen 1:1; garden inside Eden inside earth; ark has dimensions + manifest; forming/filling symmetry),
not the one recorded at the move — and NOT this sitting's doing: the build was run with the committed index builder and, separately,
with the committed registry, and fails the same four both times. The tree retires at the merge (D7/D10); no reading sitting on it.

THE SWEEP after the gates: 39/39 runners green, 4,518 graded cells — UNMOVED, as the prediction said (the views read; the engine's
one stamp is a field on a closed entry); the sequence runner 10/10 inside it; both gates satisfied at its head.

⚠ LESSONS: THE INDEX MUST NAME THE SEGMENT (source) BEFORE A VIEW CAN SCOPE A WORLD. A CLOSE RECORDS ITS DAY OR THE LEDGER VIEW
CANNOT SHOW IT. A JOIN'S 1:1 IS PROVED BY COUNTS DERIVED FROM THE TABLE, NEVER TYPED. A PROBE WORLD STOPPED MID-TAPE (`upto`) IS HOW
AN OPEN ENTRY IS SEEN OPEN. A "KNOWN-FAIL" IS RE-MEASURED WHEN TOUCHED — the move's one line was four, and the two negative tests
(stash each change, rerun) say which changes are not the cause.

NEXT (D11): NUMBERS' OPENING BLOCK on the tent's four cases — the tent daemon's custody and output branches on real kinds, the
docket view filling; steps 4 and 5 when the cases call.

## Step 4 THE CURSOR — the design (2026-09-09, THE TENT sitting 4; the owner: "Continue"; under D9 and D11; written
## before the probes, the probes before the code — the cases called for it: the daughters' argument runs BEFORE their answer)

WHAT A CURSOR IS HERE: a position in the TEXT that hands back a LIVE world — the tape replayed to the verse and stopped
there, every daemon registered, every ledger entry and pending timer as the run left them at that line, ready for new
submissions. NO SAVED STATE FILE (the ruling's own words): the world is rebuilt by replay each time, and the journal is
the AUDIT of the replay — the replayed prefix must be byte-identical to the base segment's prefix, or the cursor refuses.

THE MECHANISM (three small pieces on three files, each named here before it is written):
1. World.stop_before — an optional verse key on the engine (world_engine.py). World.submit and World.marker already
   compute the position each line names (THE VERSE REACHED, step 3's `_reach`); with stop_before set, a line whose verse
   is AT OR AFTER the cursor raises CursorReached before it is logged. The tape function is unchanged: the stitcher's
   straight-line code runs until the engine refuses the next line. (The alternative — the stitcher emitting a guard per
   line — was weighed and declined: the engine already knows every line's verse; a second parser of the same fact is a
   second place to be wrong.) A marker AT the cursor verse belongs to the cursor's future (the position it sits at is the
   verse), so `run_to('Num 27:1')` stops BEFORE the daughters' marker and their plea: the cursor is the line's left edge.
2. cold_run_sequence.run_to(verse) — the runner's second entry (the first is run()): the running world built exactly as
   run_world builds it (the registry map, the daemons, installation=True, the running setting), the tape executed under
   stop_before, the exception caught, the world returned with its FORK — the count of log lines replayed. It journals
   nothing itself. The audit lives in world_journal (piece 3). A cursor beyond the tape's last line is the whole tape
   (the running world; fork = every line). A cursor at a verse no line reaches still stops correctly at the first line
   past it (the verse key's order is total); a cursor before the first line is an empty world (fork 0).
3. world_journal.cursor_segment(world, fork, verse) — THE AUDIT AND THE APPEND (D9's shape): (a) the base segment on disk
   (the running world's, L3_run_cold_run_sequence_seed_isaac.jsonl) is read; its first `fork` events must equal, byte for
   byte, the sink of the replayed world's first `fork` log lines — else the cursor is REFUSED (the base has moved, or the
   engine has: rerun the tape, then resume); (b) the world's lines AFTER the fork are written as a NEW segment
   L3_run_cursor_<verse>.jsonl (source 'cold_run_sequence/cursor@<verse>') whose CHAIN CONTINUES from the base's chain at
   the fork line — worldledger.Segment gains an optional start_chain (default 'genesis': every existing segment
   byte-identical) and the segment header records the base's name and the fork; (c) the base is never rewritten. The
   index admits the appended segment as its own source (drop-and-rebuild, as ever) and the four views count it; the
   ask-tool takes it as a --world.

THE CLI: `python3 World/step9/cold_run_sequence.py --cursor "Num 27:5"` prints the cursor world's position, its open
entries and pending timers at that line (the ask-tool's questions over the live world), and — with scenarios registered
for that verse (step 5) — runs them and appends the segment; without scenarios it appends nothing (a cursor with no new
submission writes no segment: nothing to audit but the replay, which it reports).

THE GATES (this step's, beside the loop's standing four): the replayed prefix byte-identical to the base's prefix and
the base's chain verified through the fork; the appended segment's chain verified from the base's chain at the fork;
two cursors at the same verse with the same scenarios produce byte-identical appended segments; the reindex counts the
appended segment's lines exactly; the base's bytes unchanged before and after. cursor_probes.py, written FIRST and run
to FAIL on the unchanged engine (0 of 6), then the code, then 6 of 6.

WHAT IT COSTS: a replay is a run of the tape's prefix — seconds. What it saves is the ruling's own reason: you can ASK
the world at any verse, resume there, branch there, and continue into a new book without restarting from creation.

## Step 5 SCENARIOS — the design (2026-09-09, THE TENT sitting 4; under D9 and D11; the first exemplar the daughters'
## own argument, Bava Batra 119b:10, run before the output at Num 27:6-11 is read)

WHAT A SCENARIO IS HERE: one of the exam's CASE events (a registered kind of form `case` — the shape the Mishnah's rows
taught the input schema; never a probe-only kind: the registry refuses those) submitted on a LIVE world at a cursor,
carrying a LABEL (`scenario`: the row's name and its oracle) — the world as the oracle's bench. The daemons answer it
as they answer the tape's acts: by writing the ledger. The expected answer is the Mishnah's row, and the grade is read
off what the world wrote (an effect present or absent, a value) — printed, never repaired.

THE RECORD: scenario inputs are PRIMARY (D9's homes): World/step9/scenarios.yaml — one entry per scenario: id, the cursor
verse, the events (kind + fields, the persons by scene token), the oracle rows named, the expected reading of the ledger
(effect, entity, value or absence). The runner reads the file for the cursor's verse. The appended segment is derived
(uncommitted, as the base).

THE JOURNAL'S MARK: an EVENT line for a scenario carries prov.unit = 'scenario' (the tape's lines carry 'tape') and the
label in its data — the journal's own way of telling a submitted hypothetical from the text's act. The tape's segments
are untouched; the stitcher never sees a scenario (it records runners' scenes, and a scenario is submitted at a cursor,
not in a scene).

THE FIRST EXEMPLAR — THE DAUGHTERS' LEVIRATE DILEMMA (Bava Batra 119b:10; Sifrei 133:4's "wise, and expounding"): the cursor
at Num 27:5 — after the plea (27:1-4, the code's holding_owed on the ledger under boot), before the halt is answered. Moses
was expounding the levirate (Deut 25:5 "if brothers dwell together and one dies and HAS NO SON... her husband's brother
shall come to her"); the daughters: "if we are as a son, give us an inheritance as a son; if not, let our mother enter
levirate marriage". TWO CASE EVENTS ON ONE CLAUSE (the family engine's census: "and he has no son" at Deut 25:5 and Num
27:8 alone): estate_claimed {decedent zelophehad, survivors: daughters only, claimant: the daughters} — the first horn,
oracle Mishnah Bava Batra 8:2 (no son, no son's line: the daughter inherits — the ledger's holding_owed stands, the cell's
verdict 'the daughters inherit'); levirate_claimed {widow: zelophehad's wife, children: daughters, brothers: true} — the
second horn, oracle Mishnah Yevamot 2:5 / Yevamot 22b:6 (a CHILD of any kind exempts the father's wife — a daughter is a
child: the ledger writes `exempt` on the widow, no levirate_owed). The two horns agree on the one clause's reading: the
daughters are offspring in both institutions — and the output at 27:6-11, read AFTER, says the same ("rightly"). That is
the ruling's picture at its first live seat: the argument run on the world before the text's answer, the answer then read
as the oracle's confirmation. The grade printed by the runner under --cursor "Num 27:5"; the probes' P6 the mark.

## As built — steps 4 THE CURSOR and 5 SCENARIOS (2026-09-09, THE TENT sitting 4; the probes first, 0/6 then 6/6)

THE ORDER HELD: the two design sections above, then cursor_probes.py (six probes over the running world's base segment ON DISK —
never rewritten; every append in a temporary directory) run to FAIL on the unchanged engine (0/6: no run_to), then the code in
three files, exactly as designed — (1) the engine: World.stop_before and CursorReached, raised by submit() and marker() at a
line whose verse is at or after the cursor (the left edge); (2) the runner: run_to(verse) building the running world as
run_world does and catching the stop, cursor_main() for --cursor reading World/step9/scenarios.yaml (the PRIMARY record of the
scenarios: id, cursor, events, oracle, expect) and grading the ledger after each labeled submission; (3) the journal: the sink's one
conversion factored into _append_log, cursor_segment (THE AUDIT — the replayed prefix converted must equal the base's event lines
byte for byte, else CURSOR REFUSED; THE APPEND — a new segment L3_run_cursor_<verse>.jsonl whose chain continues from the base's
chain at the fork, its header naming the base, the fork and the cursor), scenario (the label on the event; prov.unit 'scenario' on
its EVENT line), and worldledger.Segment's optional start_chain and header (the default 'genesis' keeps every base segment
byte-identical; verify reads the header's start). Then 6/6: K1 the replay of sitting 3's 2,538 lines byte-identical to its base on
disk (the tent daemon's refactor into a verdict table changed no byte); K2 the appended segment's first chain = sha256(the base's
chain at the fork + the event) and its header the fork and the start; K3 a cursor beyond the tape's end = the whole tape; K4 two
cursors byte-identical; K5 the reindex admits the appended source and the views gate counts it; K6 the scenario's EVENT line
carries prov.unit 'scenario' and its label, the base unchanged before and after.

THE FIRST EXEMPLAR RAN (`python3 World/step9/cold_run_sequence.py --cursor "Num 27:5"`): 2,543 lines replayed to the left edge of
27:5 — the daughters' plea on the ledger (holding_owed, written by the case law under boot), the halt and the output not yet
submitted; the daughters' own argument (Bava Batra 119b:10) as two case events on one clause: estate_claimed → holding_owed PRESENT
(Mishnah Bava Batra 8:2), levirate_claimed → exempt PRESENT valued child_of_any_kind on the widow (Mishnah Yevamot 2:5; Yevamot
22b:6), levirate_owed ABSENT — 3/3, the text's answer at 27:6-11 then read as the oracle's confirmation ('rightly'); the appended
segment four lines (its start chain the base's at 2543, verified), the reindex 8 segments / 16,805 rows, the views gate MATCH on the
cursor world, the ask-tool answering on it with --world. The shelf-named person (the widow — 'our mother', named by the Talmud
alone, the ink naming no wife of Zelophehad) entered the registry LABELED as such.

WHAT THE STEP PROVES: the world can be asked at any verse and resumed there without a saved state, and the journal is the audit of
the resumption (the same bytes or a refusal); a hypothetical can be put to the world before the text answers it, and the text's
answer read against the ledger's — the ruling's picture at its first live seat. THE STANDING DUTY ENDS HERE: step 4 is on the
record; from this compaction point the loop is named as any other box (step 6 THE READBACK and D7's merge still owed).
THE CURSOR'S BOUND RULE (found 2026-09-09 at THE NUMBERS WALK sitting 1b, NUMBERS_WALK.md "Sitting 1b" as built): an
event's journal line carries its BOUND [the last forward marker's day, the next forward marker's day], and the right edge
is written when the NEXT marker arrives (the engine's shared list, closed in marker()). The cursor check sat first in
marker(), before that closing — so a replay stopped AT a marker left the previous bound open ([day, None]) where the base
had it closed, and the audit refused the bamidbar lines (K1-K2, K4-K6 failed at the 27:1 cursor once 1:1's bound reached
it). THE FIX: a FORWARD marker at the cursor closes the bounds behind it (its own day, known at the call) before the world
stops — as the full run would; a retrograde or proleptic marker at the cursor closes nothing, as in the run. cursor_probes
6/6 again. THE LIMIT THAT REMAINS, measured: a cursor INSIDE a bound whose closing marker lies beyond it (Num 15:32 —
between 1:1's marker and 27:1's) is REFUSED, because the base's line for every event of that bound already carries the
right edge the replay cannot know, and the chain hashes those bytes: the audit cannot be normalized without breaking the
chain's continuity at the fork. So the cursor stands at a forward marker's verse, or anywhere after the last marker before
it has had its bound closed (the scenario's Num 27:5 — after the tape's last marker — is such a place). A cursor elsewhere
is refused with the base named; the refusal is the honest answer until a design that journals the bound's right edge as
its own later line (a candidate for step 6's sitting).

OPEN ITEM (2026-09-12, THE NUMBERS WALK sitting 11b — Midian's compile; RESEARCH_LOG 2026-09-12 item 5; COMPILE_DEBT's sitting-11b box (i)):
THE CURSOR'S AUDIT AND THE LATER CLOSE. cursor_probes.py fell from 6/6 to 1/6 (K3 alone passes) with no line of the cursor or the journal
changed. The cause: the first close on the tape AFTER the probes' cursor (Num 27:1) of an entry written BEFORE it — moses' the_trumpets
(written at 10:2, closed by value at 31:6) and israel_people's harass_the_midianites (25:17, closed at 31:7). Step 1's sink journals the
engine's log after the run, and the log holds each ledger entry BY REFERENCE (world_engine._write appends the entry dict itself); World.close
writes closed_by / closed_day INTO THAT DICT, so the base segment's run.write line for the trumpets carries a close the replay to Num 27:1
has not reached — the prefix differs at event 2635 and every chain after it (474 of 3,108 lines; "the base or the engine has moved" — and a
rerun of the tape reproduces the same base). Ten sittings passed because every earlier close of an older entry lay on the same side of the
cursor as the entry. Not the runner's fault and not the gate's: step 1's assumption that a write line is immutable meets step 4's audit at
the first backward close. THE DECISION IS THE OWNER'S — (a) snapshot the entry at write time (log a copy) and journal the close as ITS OWN
LINE (run.close, a tenth log class registered in World/journal/registers/event_kinds.yaml; the ledger view's closed_by / day_closed read from
it; the journal gate's counts gain a column; the RUN tuple's closes slot unchanged — it reads the ledger), or (b) the audit modulo the
close fields (which empties the chain's meaning at those lines). Recommended (a): the close IS an act of the tape and belongs in the journal
as a line of its own, as the RUN tuple already counts it. Until the word: the cursor gate RED, every other gate green.
RESOLVED THE SAME DAY (2026-09-12; the owner: "I accept your recommendation"): (a) built — the design and the as-built follow.

## Step 1's amendment — THE CLOSE LINE (the design, 2026-09-12; the owner: "I accept your recommendation" on the open item above;
## written BEFORE the register's row, the probes and the code — the loop's own order)

WHAT CHANGES, IN ONE PICTURE. A debt opened in one chapter and paid in a later one is TWO moments of the run. Step 1 recorded them
as one line — the write line holding the ledger entry itself, so the payment's note landed inside the line written at the debt
(the design of step 1 said so plainly: "the payload as it stands at the run's end"). Step 4's audit assumed the opposite — that a
line, once written, never changes — and the first backward close (Num 31:6 paying Num 10:2) proved the two designs cannot both
hold. The amendment: A WRITE LINE IS A SNAPSHOT AT WRITE TIME, AND A CLOSE IS A LINE OF ITS OWN.

1. THE ENTRY'S OWN ORDINAL. Every ledger entry is stamped at write with `seq` — the world's write counter (0, 1, 2 … in the order
   of _write's calls, retro-writes and timer fires included). It is the entry's name inside the run: the write line carries it in
   its data, the close line names it. Deterministic (the log's order is the run's order), so two runs stamp the same ordinals and
   the replay reproduces them.
2. THE WRITE LINE A SNAPSHOT. World._write logs a COPY of the entry (dict(entry)) — the entry's state at the moment of writing:
   effect, subject, value, op, day, year, open (True for a debit / heaven / body entry), written_by, seq. Nothing written later
   reaches it. The one deliberate exception: the event's BOUND list, shared by the event and its effects and closed by the next
   forward marker — the copy is shallow and the list stays shared, exactly as step 1 designed it (the cursor's bound rule of
   sitting 1b already forbids a cursor inside a bound, so the audit never sees a half-closed bound).
3. THE CLOSE LINE. World.close, when it finds and closes an entry, still writes closed_by / closed_day / open=False INTO THE LEDGER
   ENTRY (the daemons and the checkpoints read the ledger — that contract is untouched) and THEN logs a tenth class, ('CLOSE', day,
   payload): {subject: the entity's registry id, effect, entry_seq: the closed entry's seq, value: the entry's value, note: the
   closer (the closing act's verse note — the same string closed_by holds), written_day: the entry's day, written_by: the entry's
   writer, closed_by_daemon: the daemon consuming when the close was made (None for a scene's own close)}. A close that finds no
   entry logs nothing (it returns False, as before) — the runner's own world stays silent where the tape's world closes.
4. THE JOURNAL. world_journal.KINDS gains ('CLOSE', 'run.close') — registered in World/journal/registers/event_kinds.yaml BEFORE the
   probe (the register's own rule); _append_log converts it: subj the entity through the registry, prov.unit the closing daemon (or
   `tape` for a scene's close), prov.ref the note (it opens with the closing verse). The gate's tuple gains run.close from the
   runner's own class census (the "log classes" line, as run.row entered at 8b). The RUN tuple is UNTOUCHED — its closes slot
   reads the ledger, as before; the journal's run.close lines must equal the world's closed entries, and the gate says so.
5. THE LEDGER VIEW. run_ledger becomes a LEFT JOIN of the write rows to the close rows on (source, subj, data.seq = data.entry_seq):
   `open` = 0 when a close row exists, else the write's own open; `day_closed` = the close row's op; `closed_by` = the close row's
   note; two new columns `entry_seq` and `close_seq`. run_docket, the ask-tool's four questions (`ledger`, `open`, `who`,
   `custody`) and _state read the view and change not one line. The views gate gains the pair `closed` (ledger rows carrying a
   close) = `closes` (run.close lines whose write lies in the same source), printed per source; a close whose write lies in ANOTHER
   source (a cursor segment paying a base entry — the legitimate case this whole item is about) is counted as `foreign` and must
   find its write somewhere in the index (a global check), never a per-source failure.
6. THE CURSOR'S AUDIT — NOT ONE LINE CHANGES. The replay to a verse now reproduces the base's prefix byte for byte because the base's
   write lines are snapshots; the close lines of later chapters lie past the fork. cursor_probes K1-K6 are this amendment's
   acceptance test, unchanged.
7. THE PROBES, WRITTEN FIRST AND RUN TO FAIL: journal_probes.py J7 — on a small world with one debt and its payment across a marker,
   (a) the write line's data carries `seq` and NO closer, `open` true; (b) exactly one run.close line, its entry_seq the write's seq,
   its day the payment's, its subject the registry id, its note the closer; (c) a sink taken BEFORE the payment is a byte-identical
   PREFIX of the sink taken after (the audit's own property, on the smallest world); (d) the index counts run.close and the ledger
   view shows the entry closed with the day and the closer from the join; J3's exclusion set names run.close as J7's class (as
   run.row is P6's). view_probes.py V1 RETYPED to the new invariant (the write row without a closer; the close row with the day and
   the closer; the view joining them) — it PASSES on the old code today and must FAIL before the code lands. Every other probe
   (V2-V6, the population, installation, sequence, clock and register probes) must pass UNCHANGED — they read the views or the
   ledger, never the write line's close fields.
8. WHAT IS NOT DONE HERE. D7's merge (one database from the journal) and step 6 THE READBACK stay owed; the ask-tool's per-source
   worlds stay per source (a cursor world's ledger question reads its own segment — the merge's business). The entry ordinal is a
   RUN-LOCAL name, not a corpus id.

## As built — step 1's amendment THE CLOSE LINE (2026-09-12, the same sitting; the owner: "I accept your recommendation"; the design
## above first, then the register's row, the probes to FAIL, then the code in three files)

THE ORDER HELD: the design section; run.close registered in World/journal/registers/event_kinds.yaml (the tenth run kind; 37 kinds);
journal_probes.py J7 written and run to FAIL on the engine that logged the entry itself (6/7 — its note: no `seq` on the write line, no
close line, the prefix differing on the closer), J3's exclusion set naming run.close as J7's class (as run.row is P6's); view_probes.py V1
RETYPED to the new invariant and run to FAIL (5/6); cursor_probes.py 1/6 as the day's baseline. THE CODE, exactly as designed: (1)
world_engine.py — World._entry_seq (the write counter), entry['seq'] stamped in _write, the log line a dict(entry) SNAPSHOT (the shallow
copy keeping the event's shared bound list, as step 1 designed), World.close logging ('CLOSE', day, {subject, effect, entry_seq, value,
note, written_day, written_by, closed_by_daemon, case_source}) AFTER writing closed_by / closed_day / open into the ledger entry (the
daemons' and checkpoints' contract untouched; a close that finds nothing logs nothing); (2) world_journal.py — KINDS ('CLOSE',
'run.close'); _append_log's branch (subj through the registry, prov.unit the closing daemon or `tape`, prov.ref the note); _tuple_of
reading run.close from the runner's own "log classes" line; view_counts / views_gate the pair closed = closes (the source's own) with the
foreign count printed; (3) World/journal/run_views.sql — run_ledger the LEFT JOIN of the write rows to the close rows on (source, subj,
data.seq = data.entry_seq): open 0 on a join, day_closed the close row's day, closed_by its note, entry_seq and close_seq the two lines'
names; run_docket, the ask-tool's questions and _state unchanged.

THEN THE PROBES: journal_probes 6/7 → 7/7 after ONE HONEST RETYPE of J7's own form — its first sink stood INSIDE an open bound (after the
event at day 30, before the marker at 33) and the prefix differed on the shared bound list, exactly as the design's item 2 says it must;
the first sink moved to the marker (the cursor's bound rule of sitting 1b), the second sink three lines longer; view_probes 6/6 (V2-V6
unchanged — they read the view); population 9/9, installation 6/6, sequence 4/4, clock green, unchanged. THE TAPE RERUN: RUN (1259, 66,
52, 0, 12, 1505, 29, 311, the four pairs, 120) UNMOVED, 10/10; the running segment 3,187 → 3,307 lines (+120 close lines = the RUN tuple's
closes slot; the "log classes" census now names CLOSE 120). cursor_probes 0/6 against the OLD base on disk (a base the old engine wrote
differs from the new replay from its first close — "rerun the tape, then resume", as the refusal says) → 6/6 against the regenerated
base: K1 the prefix of 3,221 lines byte-identical below Num 27:1; K2 the appended segment chained at the fork; K3 the whole tape 3,307;
K4 two appends identical; K5 the views gate counting the cursor segment (closed 0 = closes 0, foreign 0 — the daughters' scenario closes
nothing); K6 the scenario line. THE JOURNAL GATE GREEN — four segments byte-identical across two processes, chains verified, the index
13,168 rows, the running world's counts MATCH the RUN tuple with run.close 120, the views gate per source closed 120 = closes 120 (foreign
0) on the three seed worlds and 114 = 114 on THE REST. The register gate --strict GREEN (DECLARED 103; register_probes 7/7 — the ledger's
closed_by untouched), census 187/187, the daemon and dependency gates GREEN; the sweep (53 runners) after — its count in NUMBERS_WALK.md
"Sitting 11b — AS BUILT". WHAT IT COST: three files, one new probe, one retyped probe, one register row; no runner touched, no tuple
moved. WHAT IT TAUGHT: step 1's own design note ("a WRITE line holds the same dict object as the ledger entry, so a later close is
visible in its own line") was the seed of the fault, written down on 2026-09-09 and read past for ten sittings — a design sentence
that names a mutation of the past is a debt, not a feature; and a probe's first sink must stand at a marker, because the bound is the one
shared thing the snapshot keeps by design.

## Numbers' opening block — THE TENT (opened 2026-09-09; the block's own file World/step9/THE_TENT.md)

The four cases the code did not cover run on the tape one sitting each, the blasphemer first (Leviticus, already derived and
compiled). SITTING 1 DONE 2026-09-09: the tent daemon's custody and output branches are REAL — at Lev 24:12 the halt writes
in_custody on the person and declaration_owed on the court's docket with `covered_by` read off the ledger (under the boot setting
['law_lev24']: the code had decided at 24:11 before the halt — the installation setting's evidence, now a ledger field); at
24:13-14 the output writes rule_installed on the tent naming law_lev24 under case_output's running setting (the fork printed) and
closes the docket; at 24:23 the execution closes the person's two body entries. The recorder learned that a daemon's close is not
a tape line; the ask-tool's first reading moved the design (a body entry is closed by the deed). The docket view holds its first
row. Sittings 2-4 (Num 9, 15, 27/36) need their units derived first — THE_TENT.md's sections 2-4 as they come.

SITTING 2 DONE 2026-09-09 — THE UNCLEAN MEN AT PASSOVER (Num 9:1-14; THE_TENT.md section 2 + 2a): the first Numbers reading (the
Sifrei on Numbers 64-71 + Onkelos, 33 sources, coverage computed), the first Numbers unit frozen (num_09_pesach_cloud, eleven claims,
the dotted heh machine-verified, 164 units, standing 1789, hash unmoved), the first Numbers span compiled in its own runner
(cold_run_pesach_sheni.py 26/26 first run — the map's "already in the Passover engine" was measured false) and the SECOND CASE-BORN LAW:
the halt of a STANDING case (no guard — the men WAIT, a body entry closed by the word; the docket's covered_by read off the ledger AND
the pending timers, since under boot the code's decision was a due to the second month, filed as a timer), the output as the STATUTE
ITSELF (statute_declared, the tent output's second form — the rule wider than the question, Sifrei 69:1), rule_installed naming
law_pesach_sheni, the docket view's second row. THE TAPE LEARNED THE FOURTH BOOK (the recorder, the stitcher, the runner's regex; one
marker row walked the counter past the erection's day for the first time and the erection's morrow timers fired — the table entering
the ledger at its first due) and admitted the incense runner's Korach line at Num 16, which exposed and fixed an unguarded branch of
the erection daemon. RUN (1067, 44, 43, 0, 0, 1242, 15, 258, four pairs, 79), THE REST reproduced exactly under its amended rule, the
journal gate GREEN, the sweep 40/40 at 4,544; pending 1 (law_pesach); the men's second Passover a PENDING timer at the run's end — the
readback's open item. Sittings 3-4 (Num 15:32-36; Num 27 + 36, where steps 4 and 5 arrive) next.

SITTING 3 DONE 2026-09-09 — THE WOOD-GATHERER (Num 15:32-36; THE_TENT.md section 3 + 3a): the second Numbers reading (the Sifrei on
Numbers 113-115 + Onkelos 15:32-41, 14 sources, coverage computed, the ink facts computed beside), the unit num_15_wood_tzitzit frozen
(eight claims, four machine checks; 165 units, standing 1797, hash unmoved), and A MEASUREMENT BEFORE THE DESIGN: the death mode the map
named as this sitting's compile was ALREADY COMPILED — the Exodus Sabbath engine's cell imported it from this span's run on 2026-09-07,
before Numbers had a reading. So the compile was the case's own procedure (cold_run_mekoshesh.py 34/34 first run: the forewarning that
names the labor, the custody rule, the stoning protocol from the platform to the grave, the two verses reconciled, the hanging fork, the
labor and the identity as data rows) and the mode's import given its home. THE THIRD CASE-BORN LAW — and a new installation shape: the
output installs THE RULE INSIDE A LAW (rule_installed names the cell law_sabbath:death_run, not a daemon; the cell's own gate is the
second pass's, D2). The three tent kinds took their SECOND SEATS (placed_in_custody with the uncertainty the MODE, sentence_declared in
its leaner form — "said" without "saying", no statute in the speech — stoned_as_commanded with the ink's "and he died"), each a
REFERENCE by shared lemma. law_sabbath fired on the tape for the FIRST time (an Exodus law waiting for a Numbers act); the docket's
covered_by names two daemons — the code held the mode the ink says was undeclared. RUN (1071, 44, 43, 0, 0, 1249, 17, 259, four pairs,
83) on the second run — the first matched every predicted slot, then the ask-tool showed the death sentence OPEN and the execution's
branch was amended to close it (the close pairing, sitting 1's lesson found again); THE REST exact; the journal gate GREEN; pending 1.
OWED FORWARD: the fringes' law layer (15:37-41, a spec — Menachot 3:7, 4:1); Deut 17:7 and 21:22-23 (the witnesses' hand, the
hanging, the same-day burial) to Deuteronomy. Sitting 4 (Num 27 + 36, where steps 4 and 5 arrive) next.

## Standing duty

Every compaction point from #107 on carries THE LOOP as a named item until step 4 lands; every "NEXT" line in the
state doc and memory names it beside T1. CHRONICLE.md (the design thread's screen) reads the index of step 2 when
it is built; that folder is not ours to edit — the design thread reads this file.

## The ninth class, the fifth registry, the fifth view and the fifth question — THE POPULATION TABLE (as built at THE NUMBERS WALK
## sitting 8b, 2026-09-11; the design in World/step9/NUMBERS_WALK.md "Sitting 8b"; the speculation ARCHITECTURE/DATABASE_SPECULATION.md)

The loop's memory gained a TABLE beside its ledger. The owner's recommendation taken 2026-09-11 ("Ok go"): the population table built
inside the compile of the second census, minimal and honest, the backward seeding filed.
- THE ENGINE: World.tables — the tables of the FIFTH REGISTRY World/step9/population_schema.yaml (the columns the ink's own words: tribe,
  family, gentilic, level, count, threshold, person, father, mother, status, the delta's from/to/explained/unexplained; three grains —
  counted, named, delta — each with its required and optional columns). World.row(table, row): a daemon writes a row WHILE CONSUMING AN
  EVENT — a row written by hand is refused (the law in code); the row validated against the schema (a known table, a known grain, every
  required column, no unknown column), stamped written_by / day / year / table, appended to the table, logged as the class ROW.
  World.population(**where): the daemons' query by equality — the census daemon reads its own chapter-1 rows to declare the deltas at 26.
  A row is not a ledger entry (no op, no open, no close, no counterparty) and moves no count of the RUN tuple; a subject of a row is not an
  entity (the tribes and the families stay names; the persons the roll names enter the table, the registry unchanged).
- THE JOURNAL: the NINTH log class ROW → run.row (world_journal.KINDS; the register World/journal/registers/event_kinds.yaml); the sink's
  line for a row — subj the row's subject through the registry (a named row's person id, a counted row's tribe name), unit the writing
  daemon, ref the verse the row was written from, data the row as stamped.
- THE FIFTH VIEW run_population (World/journal/run_views.sql): one row per run.row — grain, as_of (the census the row belongs to), tribe,
  family, level, person, father, status, count, delta, unexplained, day, year, written_by, verse; the views gate's population check (the
  view's rows = the run.row lines, derived from the table's own counts on every world).
- THE FIFTH QUESTION `population [<tribe>]` (world_journal.ask): every row of the running world in the run's order, or one tribe's — the
  ask-tool's fifth answer beside ledger / open / who / custody.
- THE PROBES: population_probes.py (P1-P9 — written first, 0/9 on the unchanged engine, 9/9 after: the rows and their writer, the refusal
  by hand, the three schema refusals, the query, the daemon's own delta rows from its rows, the sink's run.row lines, the view and the gate,
  the question, the RUN counts unmoved); journal_probes J3 amended (the seven engine classes the probe world exercises are KINDS less
  run.skip and run.row — the ninth class exercised by P6); journal 6/6 and view 6/6 unmoved.
- THE FIRST WRITER AND THE FIRST READERS: law_second_census (cold_run_second_census.py) writes the first roll's rows on the SHARED kinds
  census_taken and levites_counted (rows only, no effect — an empty watch), the second roll's rows, the deltas (declared: the tape's
  explanations by CALL beside the ink's number, the remainder labeled unexplained) and the named rows at its lines; the daughters' row
  (26:33 — "had no sons, only daughters" on the table BEFORE the plea at 27:1) and Jochebed's row (26:59 — CJ3b's ink witness) are the
  table's first consumers; the sequential run's CP1-CP9 grade the table on the tape.
- FILED: the backward seeding (the ark's kind table, Genesis 10's nations, Genesis 46's roster by name) — a COMPILE_DEBT line naming the
  consumer that would call for it (a daemon querying a person before Numbers 1); the second pass after Deuteronomy the natural seat.

## THE REGISTER GATE — the design (2026-09-11, the sitting after the discussion step; the owner: "Yes let's do 1,3 then 2 in the next
## sitting" → "Does 2 build the database structure?" (no — a checker) → "Ok go"; written after the measurements and BEFORE the probes, the
## probes before the code — 1b's order)

THE IDEA (ARCHITECTURE/DATABASE_SPECULATION.md section 4): the text writes its own test oracle — footers carrying checksums, receipts closing
commands, footers stamping law blocks, headers opening registers — and the machine was not running it. The gate reads those formulas OFF THE
TANAKH DB (the lemma column; the numerals by the step-9 parser) and checks what the engine already holds: the population table, the ledger,
the installation registry. It ADDS NO TABLE, NO ROW, NO COLUMN. Its one new file is a dispositions registry in the daemon gate's form.

THE MEASUREMENTS (scratchpad register_gate_measure.py on the running world, before this paragraph): 1,481 ledger entries, 114 of them CLOSED
(a close flips `open` on the debit and stamps closed_by — a note beginning with the closing verse — and closed_day; every closed_by names a
verse); the table's 136 rows at five as_of values (Num 1:17-19, 3:16, 26:5-51, 26:57-62, 26:63-65 — THE EVENT'S verse, not the count line's);
81 lines carry a numeral beside "the counted" (6485) or "souls" (5315) — 12 with a ROW at the same chapter (Num 26's tribes and the Levites),
27 with the row at ANOTHER as_of (Num 1:21-43 whose rows sit at as_of 1:17-19; Num 2's restatements of chapter 1; Num 3:22, 3:34, 3:39), 41
with NONE; and the ink VARIES ITS COUNT-NOUN — Num 3:28's 8,600 sits beside "the number" (4557), not "the counted", and Simeon's 22,200 at
26:14 beside NO count-noun (the bare footer "these are the families of the Simeonites, 22,200"); the 58 receipts on the running world:
9 CLOSE-AT-VERSE (Lev 24:23, Num 1:19, 3:42, 3:51, 8:3, 8:22, 15:36, 20:27, 27:11), 18 WRITE-AT-VERSE (the act on the ledger, no command-debit
closed — the sanctuary's and the milluim's receipts), 5 EVENT-AT-VERSE, 5 CLOSE-IN-CHAPTER, 21 NONE (13 inside the compiled books — Exod 7:6,
7:10, 39:1, 40:19, Lev 8:4, 9:7, 10:15, 16:34, Num 31:7, 31:31, 31:41, 31:47, 36:10 — and Deuteronomy's 8); the nine "these are the statutes /
commandments / judgments / words / testimonies" lines: two are HEADERS by their verb ("which you shall set before them" Exod 21:1; "which you
shall observe" Deut 12:1), seven FOOTERS; the blocks by the daemons' given_at: (start, Exod 21:1] 11, (Exod 21:1, Lev 26:46] 32, (Lev 26:46,
27:34] 1, (Lev 27:34, Num 30:17] 11, (Num 30:17, 36:13] 0, Deuteronomy's four 0; the 68 register headers fall in eighteen chapters, three of
which have rows (Num 1: 12, Num 3: 4, Num 26: 120).

THE FOUR CENSUSES (each read off the DB; each seat classified by the world; GREEN classes need nothing, every other class needs a declared why):
- A. THE COUNT LINES — a line carrying a count-noun ("the counted" 6485, "the number" 4557, "souls" 5315) OR a register footer ("these are the
  families / sons / counted of" with a numeral). Each numeral on the line is classed by THE UNIT RULE, the ink's own grammar of a number followed
  by its noun: a numeral run (the NUMY words) followed within two tokens by a UNIT NOUN — year 8141, day 3117, month 2320, gerah 1626, talent
  3603, shekel 8255, city 5892, man 376 — is a MEASURE (an age, a threshold, a duration, a rate, a headcount of men), not a count; the rest are
  COUNTS. The parser's values are paired to the runs in order; when the pairing fails (a year-word holding a phrase open) every value is a COUNT
  (it surfaces as debt rather than dropping silently). A line whose numerals are all measures is MEASURE-ONLY (listed, no why). A count is
  ROW when a counted row of the population table carries that count with its as_of in the line's chapter, LEDGER when a `counted` status on
  the ledger carries that value (the totals live there since 8b — Israel 603,550 / 601,730, the firstborn 22,273, the Levites), ELSEWHERE when
  the row or status exists but at another chapter (Num 2's restatements; Exod 38:26's 603,550), NONE otherwise. GREEN: ROW, LEDGER.
- B. THE RECEIPTS — a line with כַּאֲשֶׁר צִוָּה יְהוָה ("as the LORD commanded": k/834 + 6680 + 3068 within three tokens). CLOSE when a ledger
  entry is closed by a closed_by naming the verse or a closed entry's case_source contains it; ACT when an entry's case_source contains the
  verse and none closed (the act on the ledger, no command-debit); EVENT when an event's case_source contains the verse and nothing was written;
  CHAPTER when a close sits in the chapter but not at the verse; NONE. GREEN: CLOSE.
- C. THE FOOTERS — the "these are the statutes / commandments / judgments / words / testimonies" lines (428 + 2706 / 4687 / 4941 / 1697 / 5713).
  HEADER when the line's verb is a second-person imperfect (you shall set / observe), else FOOTER. A footer's block is (the previous footer or
  header, this footer]; a header's block (this header, the next footer]. The block's STAMP is the place word on the line (Sinai 5514, Moab 4124,
  the Jordan 3383, none). DAEMONS when at least one daemon's given_at lies in the block (the daemons listed with their installed_by beside the
  stamp — a listing, the registry's own), EMPTY otherwise. GREEN: DAEMONS.
- D. THE REGISTERS — the 68 "these are + generations / names / sons / families / the counted" headers grouped by chapter (eighteen registers).
  ROWS when the table has rows whose as_of chapter is that chapter; NONE otherwise. GREEN: ROWS.

THE DISPOSITIONS (World/step9/register_dispositions.yaml — four maps counts / receipts / footers / registers, keyed by the seat — a verse for A-C,
a chapter for D — each {class, why}): the gate VERIFIES the declared class equals the computed one — a declaration that differs is a LIE and
FAILS; a declaration on a seat the world has since paid (computed GREEN) is STALE and FAILS (the daemon gate's exactness: the file may never
overstate or understate the world); an undeclared non-green seat is DEBT — printed, exit 0 — until `--strict`, when the debt itself fails
(claim_labels_census.py's form). `--emit` prints yaml stubs for every undeclared seat with its computed class, the why left to be typed
FROM THE READING of the print, never generated.

THE OUTPUT: coverage first (the four tallies by class), then the seats by census, then the DEBT list, then THE REGISTER GATE: GREEN | FAILED.
Writes World/step9/REGISTER_INDEX.md each run (documentation, never runtime). Exit 0 on green or debt-only (non-strict), 1 on a lie, a stale
declaration, or debt under --strict. Run from the repo root: `python3 World/step9/register_census.py [--strict] [--emit] [--no-index]`.

WHERE IT RUNS: at every compile sitting's gates step, beside the daemon, dependency, installation and journal gates (THE_STEPS' compile
checklist gains the line) — NOT in run_cold_all.py: the sweep's contract is unchanged this sitting (the gate builds the running world, ~90 s).

THE PROBES (register_probes.py, R1-R6, written BEFORE the code and run to FAIL — ImportError, 0/6 — then 6/6 after): R1 the count-line census
and the unit rule (Gen 46:15's 33 a COUNT; Num 1:3's 20 a MEASURE — "years" follows; Num 26:14's 22,200 a COUNT with no count-noun, by the
footer form; Exod 38:26's 20 a MEASURE and 603,550 a COUNT); R2 the receipts (58 seats; Num 1:19 CLOSE, Exod 39:5 EVENT, Num 31:7 NONE on the
running world); R3 the footers (nine lines; Exod 21:1 and Deut 12:1 HEADER; Lev 26:46 stamped sinai, Num 36:13 moab and EMPTY); R4 the registers
(68 headers, eighteen chapters; Num 26 ROWS, Gen 46 NONE); R5 the dispositions' law (a lie FAILS; a stale declaration FAILS; an undeclared debt
seat passes non-strict and FAILS strict — on synthetic files); R6 the whole gate on the running world non-strict exits 0 with the tallies as
literals typed from the first run's print. The running world built ONCE per probe run (CS.run_world).

THE PREDICTION (typed here, checked at the first run): count lines 81 by the two count-nouns + Num 3:28 and its kin by "the number" + the
footers' bare seats (26:14) — the census larger than 81, the exact count read at the run; receipts 58 with 9 CLOSE; footers 9 (7 + 2), blocks
with daemons 4, EMPTY 5; registers 18 with 3 ROWS. The first run is a FINDING, not a failure to fix by hand: an ACT without a close is the
ledger's own debt (the command never written as a debit, or never closed) — declared with its why, never faked closed.

## As built — THE REGISTER GATE (2026-09-11; the owner: "Ok go" on the recommendation's item 2; the design above written first, the probes
## to FAIL 0/6 before the code, then 6/6; the gate GREEN under --strict with 104 declared seats)

THE FILES: World/step9/register_census.py (the gate — read_ink / running_world / count_lines / receipts / footers / register_headers, the four
class_* functions, verify, gate; --strict / --emit / --no-index), register_probes.py (R1-R6), register_dispositions.yaml (the 104 whys),
REGISTER_INDEX.md (written each run). Nothing built into the engine: no table, no row, no column, no daemon.

THE FIRST RUN READ (non-strict, --emit): 118 debt seats, 0 fails — and the reading found the finder's own faults before the world's: ten count
lines UNPAIRED because the run-finder matched number-word stems inside PROPER NAMES and ORDINALS (Issachar's שש "six" inside יששכר "Issachar",
ושנים "and second" at Num 2:16, ושני "and the years of" at Exod 6:16, השבעי "the seventh" at Exod 12:15) — the token census's homograph lesson at a
third seat. THE FIX: the finder now runs on THE PARSER'S OWN TOKENS (cold_run_sequence.verse_words, aligned one-to-one with the DB's words), whose
markers decide — a STAR is a homograph the points refused (not a numeral), a percent sign a fraction, an at sign the unit noun as one, the hash /
caret / tilde forms their own keys in UNITS — and two rules of the ink joined the unit rule: THE DUALS carry their unit inside the token
("two years" שנתים, "two days", "two cubits", "twice") and are measures; and ONE IS NEVER A CHECKSUM ("one soul", "one man for his father's house",
"on the first of the month" — a register's total is never one). Second run: no UNPAIRED line; 104 debt seats — counts NONE 21 / ELSEWHERE 14
(41 MEASURE-ONLY, 29 ROW, 3 LEDGER green), receipts NONE 21 / ACT 18 / EVENT 5 / CHAPTER 5 (9 CLOSE green), footers EMPTY 5 (4 DAEMONS), registers
NONE 15 (3 ROWS). Every why typed from the reading of the print (scratchpad write_register_dispositions.py — the classes taken from the gate's
computation, never typed; verify() clean before the write); the strict run GREEN; the probes 6/6.

WHAT THE GATE FOUND ON THE WORLD (the ledger's honest state, now declared, not fixed by hand):
- THE SPEC'S COMMANDS ARE NOT DEBITS — 18 receipts whose act is on the ledger at the verse (the veil hung, the bread set, the lamps, the incense,
  the tamid, the washing, the garments' blocks, the milluim's blood, the eighth day's acceptance, the omer jar, the tablets, Aaron's staff) with
  NOTHING CLOSED, because the command each answers is a specification (Exodus 25-31, Leviticus 8's instructions) the tape never wrote as a
  debit; plus 5 receipts whose event fires and writes nothing at the verse. The command-and-receipt pair closes only where the command was
  itself an EVENT (Num 1:19, 3:42, 3:51, 8:3, 8:22, 20:27, and the tent's cases 24:23, 15:36, 27:11) — nine CLOSE. Filed as a debt CLASS
  (COMPILE_DEBT.md): a debit per spec command would let these receipts close.
- THE STORY'S SCENE GAPS — receipts with no event at the verse: Exod 7:6, 7:10 (the staff-serpent), 39:1 (the garments' heading), 40:19 (the tent
  spread), Lev 8:4 (the assembly); Lev 16:34's "and he did as the LORD commanded" with no narrated rite; Num 36:10's receipt ONE VERSE BEFORE the
  act (the marriage fires at 36:11-12 — declared, not moved).
- THE RECEIPT INSIDE A COMMAND — Lev 9:7, 10:15, Num 26:4: the formula quoted inside a command or a speech, not a receipt of an act.
- THE REGISTERS THE TABLE DOES NOT HOLD: the camps (Num 2 — the Bamidbar runner's four sums as cells), the service roll (Num 4 — Naso's cells),
  the shekel account (Exod 38 — a metals ledger), Genesis 46's four sub-totals and the 66 / 70 (the Joseph runner's ROSTERS and CJ3b), the
  spies' and the princes' name lists; Genesis' eight name trees (the named grain on the tape and in the entity registry); chapters 30-36 and
  Deuteronomy not yet walked. Each a declared seat; the seeding stays FILED.
- THE PARSER'S NEXT HOMOGRAPH — Gen 41:34 וְחִמֵּשׁ ("and let him take a fifth") read as FIVE: the tithe-verb class (a verb on a numeral stem);
  filed for the parser's next teaching (RESEARCH_LOG.md).

THE LAW OF THE DISPOSITIONS IN FORCE: a declared class that differs from the computed one FAILS (a lie); a declaration on a seat the world has
since paid FAILS (stale — delete the line when a runner pays the seat); an undeclared non-green seat is debt, FAIL under --strict. The gate
runs at every compile sitting's gates step (THE_STEPS' compile checklist), not in run_cold_all.py.

## THE LIVING DATABASE AND THE LOOP THAT WAITS — the discussion of 2026-09-14 (NO RULING YET; recorded in the map so it cannot slip a fifth time — the lesson of "How it slipped" above; the owner: "we really need to get this done right. make sure you record")

THE OWNER'S WORDS (2026-09-14, after the project review; DISCUSSION, NO RULING YET — the owner's law: discussion is not a ruling): "What I want to
do now is review our discussion about creating the real time inputs that make this a simulation, period. We keep putting it off." Then, on the
shell I proposed: "I don't want to input anything, I want it to update a living database. Later we will create an interface to the database that
will show the current states at all times. I'm not ready to input any data. In fact, I think the data will come from a second pass or even a third
pass. It may even create its own data. We just don't know. But I need a live database showing the current state of things. What I might want is a
step through process." Then: "I know a simulation needs inputs. We will decide what those are later. But assuming this is a simulation what
components do I need that we don't have now." Then: "I think we had this very discussion and partially built a loop didn't we? scan the files."
And at the close: "we really need to get this done right. make sure you record."

THE SCAN (2026-09-14; the files read: THE_WORLD.md's idea log, World/step9/THE_LOOP.md whole, the state doc, ARCHITECTURE/DATABASE_SPECULATION.md,
ARCHITECTURE/CHRONICLE.md, World/step9/world_journal.py and World/journal/worldledger.py): THE SAME DISCUSSION FOUR TIMES, A PART BUILT EACH TIME,
THE SAME PIECE LEFT OUT EACH TIME.
  1. 2026-08-24/25 (THE_WORLD.md): the ruling "the journal is the truth, the database an index rebuilt from it"; a world player built in the
     mockups folder (two passes, compile then run, one world; retired at D10); the idea log names "the gap between replay and live simulation" and
     "the world clock as the loop's heartbeat, not yet mounted". Never mounted.
  2. 2026-09-03 (THE_WORLD.md, the night rider, the owner's words): "a simulator is a LOOP that runs whether or not anyone asks"; FIVE constructs
     named as missing — (1) a main loop over TIME, (2) mutable state, (3) laws as daemons, (4) timers, (5) the diff engine as a checkpoint stream.
     Four of the five exist today (the ledgers change; 62 daemons fire unasked; 66 timers set, 52 fired; 208 checkpoints). THE FIRST WAS NOT
     BUILT: the engine drives over the tape's rows and exits.
  3. 2026-09-05: CHRONICLE, the observation deck — design only, by the owner's word (ARCHITECTURE/CHRONICLE.md "Status").
  4. 2026-09-09 (THE_LOOP.md, the PERMANENT ruling): "a loop that keeps its state between inputs" — steps 1-5 built (the sink, the index with
     its five views, installation, the cursor, scenarios); thirteen decisions D1-D13 taken; step 6 THE READBACK named with no design; the step-4
     row chose REPLAY, NO SAVED STATE FILE. The resident world was never on the decision list. 2026-09-13 (the peer thread): "never deferred, only
     never decided".
  MEASURED TODAY: world_journal.py writes the segment ONCE, at the run's end (seg.write; "data — the payload as it stands at the run's end");
  the index is drop-and-rebuilt after (--reindex; the gate). So inside a run there is no "now" on disk. The five run views (run_population,
  run_ledger, run_timers, run_clock, run_docket in World/journal/run_views.sql) already DEFINE the current state; they are only ever fed a
  finished run. Fourteen timers stand pending at the tape's end and nothing can fire them (time moves only at a verse's marker).

THE PICTURE AGREED IN DISCUSSION (a simulation needs six things; we have three whole, one in half, two not at all):
  HAVE — a state (entities, ledgers, timers, the clock, the population table, the docket, the installed laws); rules that fire on inputs through
  ONE DOOR (World.submit; consequences to the ledger, never the tape — THE FENCE); a history you can trust (the journal, chained, replayable,
  audited byte for byte).
  HALF — memory between moments: the journal written at the end, the database rebuilt after; the views that define "now" exist but are never
  current.
  MISSING — (a) A LOOP THAT WAITS: today the tape is a script that runs to the end; a simulation takes one step, writes the state, PAUSES, takes
  the next. (b) A PORT FOR INPUTS: today only the runners' own lines enter, from inside the code; a simulation reads its next input from a place
  outside itself, a queue checked between steps — the text the first producer, a second pass the second, whatever the owner decides the third;
  the port decides nothing about what the inputs are.

THE RECOMMENDATION (mine, for the owner's word; each one sitting; no runner's logic moves; the audit stays):
  1. WRITE AS YOU GO — the journal line on disk the moment the engine logs it, and the database updated line by line with the same rows the
     rebuild makes, so at any pause the database IS the state; at the end the gate still rebuilds from scratch and must match byte for byte.
  2. THE LOOP WITH A PAUSE (the stepper) — the same tape driven at the grain of ONE EVENT, grouped by verse or day when watching; the cursor is
     already replay-to-a-verse, the stepper is the cursor with a pause instead of a stop; at the pause the database is current and anything can
     read it (the ask tool now, the interface later).
  3. THE PORT — the queue the loop reads between steps, with the text as its only producer for now; every later pass writes to the same database
     under its own run name (the index already carries `source`); a pass that creates its own data enters through the same one door.
  TO LEAVE OPEN (two questions, decided later): whether time may advance without a verse's marker (the fourteen pending timers); the window to
  watch it all (CHRONICLE's design). NOT TO BUILD: a saved state file, a hand-input shell, a second database beside the journal.
  THE ORDER when the word comes: the loop's own — the design section in THE_LOOP.md first, the probes to FAIL, then the code; before Deuteronomy
  or after is the owner's call.

WHAT THE OWNER MUST DECIDE (nothing moves before the word): (i) build the three, in that order, or a different cut; (ii) the grain of a step —
I would take the event as the atom; (iii) what "current state" shows — the five views as they are, plus the entities, the installed laws and the
checkpoints as they fall; (iv) before or after Deuteronomy.

- [ ] THE LOOP THAT WAITS (opened 2026-09-14, the owner: "ok go 1"; step 7 in the table): (a) [x] WRITE AS YOU GO — BUILT 2026-09-14 (D14 THE SEAL; the design and the as-built below); (b) [x] THE STEPPER — BUILT 2026-09-14 (D15 THE TAPE AS A GENERATOR; World/step9/world_stepper.py; the design and the as-built below); (c) [x] THE PORT — BUILT 2026-09-14 (D16-D18; World/step9/world_port.py + the stepper's --queue; the first queue World/journal/port/daughters.yaml; the design and the as-built below). THE LOOP THAT WAITS IS BUILT; what remains is TO FINISH THE LOOP — THE LIST, the section after the as-built, kept current.

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
       - 26 lines differ from the masked run-end form because their bound was ALREADY CLOSED when sealed — thirteen TIMER-FIRE lines and their thirteen WRITE lines, every one a timer fired inside a LATER marker's walk (the fire's block is that marker's advance) carrying the bound of the event that SET the timer, closed long before the fire — e.g. line 656 [747874, 747875], lines 2585-2592 the four fires of day 894698 with a bound of one day [894698, 894698]; the print in loop_measure_mutation2.out.
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
in the journal moves after it is written. THE COST, said plainly: the base segments' bytes change ONCE (2,673 lines of the
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

## As built — step 7 (a) WRITE AS YOU GO (2026-09-14, the same sitting; the owner: "ok go 1"; the design above first, the probes to FAIL
## 0/7, then the code in four files, then 7/7 with no probe changed)

THE PROBES FIRST: World/step9/live_probes.py L1-L7 written from the design and run on the unchanged engine — 0/7 (six on "world_journal has no
attribute attach", L7 on the missing World.journal), then 7/7 after the code.
THE CODE (the forms in World/step9/forms_numbers_walk/loop_2026-09-14/ — loop_measure_mutation.py the measurement, patch_live_sink.py the patch
with every replacement asserted once):
  - world_engine.py: `import functools`; World.journal = None; the decorator _sealed on submit, marker, advance, close, row, cancel_timers —
    after the call returns at depth 0, in a finally, the attached sink's flush(); nothing else in the engine moved (the daemon gate and the
    dependency gate GREEN after it: 62 daemons, 427 WRAPPED, open aliases 3; the link census 455 / 48 / 9 / 143 of 482 + 173, 224 live edges on file).
  - World/journal/worldledger.py: row_of(ev, source) — the index's row has ONE home; index_sqlite uses it.
  - world_journal.py: LiveSink (attach; flush — the one conversion, the chain, the body file <segment>.live appended and flushed, the rows
    INSERTed and committed per block; seal — the header + the same bytes, the body removed, the world detached, THE AUDIT), attach,
    ensure_index (the table built from every segment on disk when absent, the views), rows_of, l3_sources, verify_body (a headerless body's
    chain), audit ((i) the chain, (ii) lines = the log, (iii) the independent conversion equal on every field but the bound's right edge with
    its count, (iv) the rebuilt index equal to the live rows), live_report; sink() kept for every old caller — a live sink seals, the
    cursor's in-memory sink writes its sealed lines, a world that ran with no sink takes THE LATE SEAL and says so; cursor_segment's audit
    reads the in-memory sink's sealed lines; the gate reads the live rows of both processes BEFORE its rebuild and demands them identical
    and equal to the rebuilt rows.
  - cold_run_sequence.py: WJ.attach before the tape in run_world, run_to (memory_only) and rest_world; the closing reindex retired for
    live_report (--reindex stays by hand).
THE TAPE UNDER THE SEAL (one run, 98.4 s wall): 10/10 — every seal LIVE: the running world 3,362 lines in 1,533 blocks, the chain VERIFIED,
the fresh conversion EQUAL on every field but the right edge (closed after the seal: 2,673 — the measurement's own count; the 26 already-closed
lines were never among the differing ones), the rebuilt index EQUALS the live rows; descent_literal 3,362 / 1,533 / 2,673; covenant_pieces
3,362 / 1,533 / 2,639; THE REST 3,358 / 1,531 / 2,673; JOURNAL INDEX (live): 20,049 rows, every source current (the four worlds and the old
cursor segment's 4 rows). RUN unmoved (1279, 66, 52, 0, 12, 1527, 33, 318, the four pairs, 121); THE REST exact.
THE PROBES AFTER: live 7/7; journal 7/7 (J7's "earlier sink a prefix of the later" holds by construction now); cursor 6/6 after the tape (K1's
prefix from the in-memory sink's sealed lines, byte-identical to the new base); view 6/6; installation 6/6; population 9/9; sequence 4/4;
clock 22/22.
THE JOURNAL GATE: GREEN — four segments byte-identical across two processes, chains VERIFIED; THE LIVE INDEX line new: 4 sources, 13,444 rows written line by line at their blocks, the two processes' rows IDENTICAL, the rebuilt index EQUALS the live rows; the running world's counts MATCH the RUN tuple; the five views MATCH on every source (ledger 1,539 = writes; timers 66 = sets, fired 52, pending 14; clock 157; docket 4; population 148; closed 121 = closes).
THE SWEEP: 57/57 runners green, 6,378 graded cells (unchanged from 15b's close; the dependency gate 251 required edges / 174 pointers, 338 live import edges, 482 + 173 on file; the daemon gate 62 daemons, 427 WRAPPED, open aliases 3).
WHAT THE DATABASE IS NOW: World/journal/data/world.sqlite is written line by line as the tape runs — at any block's end the events rows of the
running world are the lines sealed so far and the five views over them are current; `--ask` answers between blocks. The run's closing rebuild
is gone; the rebuild is the audit, in a temporary file, at every seal and in the gate.
THE COST PAID: the base segments' bytes changed once — the bound's right edge null on 2,673 lines of the running world, the marker line after
them carrying the day; no reading, no verdict, no count moved; the cursor's audit re-run and green.
OWED TO (b) THE STEPPER: the pause between blocks (the flush is the seam); the import cost (81.8 s) the stepper's fixed price — the pause lives
inside one process; the cursor's own appended lines live (late-converted today); a bounds view if "current state" needs it; the checkpoints
on the journal (printed lines today).
LESSONS: A PAYLOAD MOVES AFTER THE LOG — before a sink writes early, take three snapshots of every line (at append, at the block's end, at
the run's end) and read which keys move; the block is the seal's grain, and the late-moving key becomes a derived fact read from the later
line. A COUNT DERIVED FROM A MEASUREMENT IS RETYPED FROM THE INSTRUMENT'S OWN PRINT — "about 2,647" (2,673 less the 26) was wrong: the 26
were never among the differing lines; the seal printed 2,673 and the design was corrected before the record.

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
     entries, 0 pending timers, audited against the base: yes; then THREE STEPS by verse through the chapter — 27:1 (the reading-placed marker
     and the daughters' approach 27:1-4, one verse: marker + event + write, 3 lines); 27:5 the judgment brought near (event + write) with
     the court's CUSTODY ROW appearing in --show custody (the_court, the daughters, law_tent, open); 27:6-11 the statute declared (event +
     close + write), the custody row gone — and the session STOPPED AT THE LEFT EDGE OF Num 28:1, sealed as a partial segment of 3,229 lines
     in 1,495 blocks, the audit ok (the first run of the session, before the quoting fix below, showed four steps: the None labels split 27:1
     from 27:1-4).
  B. `--by marker --quiet`: the whole tape in 158 steps (157 markers; the last step 41 lines from the last marker to Num 36:11), 3,362 lines
     sealed as the whole tape; THE BODIES COMPARED — the session's segment against the base line for line after the header: IDENTICAL, 3,362
     lines each, the same chain head 5c482e02f82ea462 (the headers differ in the source's name alone).
  THE MISS THE FIRST SESSIONS FOUND: thirty-two of the tape's sources are written in DOUBLE QUOTES (the stitcher's repr when the text holds
  an apostrophe) and the stepper's verse pattern read single quotes only — "the world stands before None" at 27:1-4 and 27:6-11; the three
  patterns now read either quote; S9 added AFTER the miss (every call of the real tape yields a verse — no None; 1,507 yields by book);
  session A rerun clean (the state doc's #172 has both prints).
THE TAPE AFTER THE SESSIONS: 10/10; the live report lists the session as a fifth source — cold_run_sequence/stepper 3,362 rows = 3,362 lines
MATCH beside the four worlds (23,411 rows in the one database after session B; after session A's rerun the same source 3,229 rows =
3,229 lines MATCH, 23,278 rows — the live report reprinted). THE PROBES AFTER: live 7/7, journal 7/7, cursor 6/6 (the base untouched by
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
THE TAPE AFTER: green by the runner's own exit (the live report prints only after the grade passes) — the live report 26,511 rows: the port's world cold_run_sequence/port@daughters 3,233 rows = 3,233 lines MATCH beside the four worlds (3,362 / 3,362 / 3,358 / 3,362), the stepper's session (3,229) and the cursor's segment (4), every source current.
A FINDING, filed in the list below: the second horn's case_source cites Deuteronomy 25:5 and the engine's VERSE REACHED moved to (Deut, 25, 5)
inside Numbers 27 — an input's citation moves the position the installation gate reads (harmless under boot; the from_event setting would
read it). The port's position and the input's citation are two things; which the engine's position follows is part of the inputs' own
definition, the owner's.
WHAT THE LOOP IS NOW: a running world with memory that WRITES AS IT RUNS (a), PAUSES BETWEEN CALLS (b) and READS ITS NEXT INPUT FROM OUTSIDE
ITSELF (c) — the text its first producer, a queue its second; every input through the one door, journaled, audited to the fork, the world
with inputs its own world in the one database. What the inputs are is not decided; the port does not decide it.

## TO FINISH THE LOOP — THE LIST (the owner, 2026-09-14: "keep up with what we need to do to finish this"; A STANDING DUTY: this section is
## brought current at every loop sitting, and the reply at every loop sitting's close echoes it; the boxes above are its ledger)

BUILT: steps 1-5 (the sink; the index with the five views and the ask tool; installation; the cursor; scenarios), step 1's amendment (the
close line), step 7 (a) write as you go, (b) the stepper, (c) the port — 2026-09-14.
THE BOARD (item 10, the interface) — 2026-09-14 on "lets build it"; THE CHECKPOINTS AS THEY FALL (item 5) — 2026-09-14 on "Ok do it";
nine items remain open, three of them the owner's.

OPEN, each with its home and its size (the owner's items marked; nothing moves before his word):
  1. THE INPUTS THEMSELVES — the owner's decision ("we will decide what those are later"): what a second or third pass produces, in what
     form, at what positions; the port takes any registered kind now, from any file. OWNER. Then: a queue writer for that pass (a sitting).
  2. THE SECOND PASS — D2 (2026-09-09): the installed run (installed_by from_event) after Deuteronomy, on the whole program; its findings a
     queue for the port. AFTER DEUTERONOMY; a sitting.
  3. STEP 6 THE READBACK — D12: the text re-read against the ledger the run left (Deuteronomy's repetition first, the prophets after); its
     design at Deuteronomy. AFTER DEUTERONOMY; the design a sitting, then per book.
     THE FIRST FORM BUILT 2026-09-15/16 (THE DEUTERONOMY WALK 1b, the owner's "Yes 1. Go"): the narrative retellings of Deuteronomy 1-3 as
     reference rows graded against the tape (forty-two), the supplied acts written once at their own time and closed by the prior run, the
     disagreements open (DEUTERONOMY_WALK.md "Sitting 1b" (R1)-(R6); readback_probes.py 6/6). OPEN STILL: THE LAWS' HALF — chapters 5-26
     re-read against the ledger (a sitting when chapter 5 opens; per book after), and the prophets' indictments against the open entries.
  4. D7'S MERGE — one database: the World folder's corpus world (the reading era's 557 events, World/world.sqlite) as a journal layer, its
     tables views over the journal, the reconciliation gate upstream; the August tree retired with it (D10). DONE 2026-09-14 — the design
     and the as-built below (D19-D21): the fold is the L1 layer, the old tables are views over the one database, the gate moved twice.
  5. THE CHECKPOINTS AS THEY FALL — the checkpoints are computed after the run from the marker table (part (b)'s measurement 2); the stitcher
     places each at its verse in the tape so a pause shows them. A SITTING (the stitcher's rewrite; the base's bytes unchanged).
     THE OWNER'S WORD (2026-09-14): "Yes, after the board" — the board's page first, then this.
     BUILT 2026-09-14 on "Ok do it" (after "What is checkpoints" was answered) — the design and the as-built sections after this list:
     D27-D30; the block a function of the world (cold_run_sequence.checkpoints), the partial executor, the fall of every checkpoint
     measured by stepping the base (checkpoint_positions.py → checkpoint_positions.yaml, 199 rows), the stepper's --show checkpoints;
     checkpoint_probes.py 0/7 → 7/7; the tape 10/10 and the journal gate GREEN unmoved. Not by the stitcher's rewrite as first named:
     the tape's lines never moved — only the block's home did, and the fall was measured.
  6. TIME WITHOUT A MARKER — may the loop advance a day with no verse? Fourteen timers wait past the tape's end (Midian's third and seventh
     days, the altar's daily offering). OWNER's decision; the mechanism half a sitting if yes (the stepper never moves the clock today).
  7. THE POSITION OF AN INPUT — part (c)'s finding: an input's citation moves the engine's verse reached (the installation gate's position);
     whether the engine follows the port's position or the input's citation. OWNER's, inside item 1; the code one line either way.
  8. THE CURSOR'S OWN LINES LIVE — the cursor's appended segment is converted late (part (a)'s (5)); the stepper with a queue does the
     same job live, so the cursor may retire into the stepper (--from with a queue). SMALL; the owner's call whether the cursor stays.
     THE OWNER'S WORD (2026-09-14): "Both, when a sitting has room" — this and item 12 folded into a later loop sitting, no sitting of their own.
  9. THE WINDOW — CHRONICLE (ARCHITECTURE/CHRONICLE.md, the design thread's, design only): the observation deck over the live database now
     that it is live. THE DESIGN THREAD'S; the main thread reads it.
 10. THE INTERFACE — "later we will create an interface to the database that will show the current states at all times": over the five
     views and the sessions' sources; the ask tool is its first form. LATER, the owner's word; its own design.
     THE AGREED SHAPE (2026-09-14, the two threads on the owner's word — "I want to see when a new event takes place… a world forming"; a
     mockup of the panel form published the same day, the forms folder's mockup_state_page.html; the feed below is what the threads agreed):
     A FEED, one line per event as it happens, newest at the bottom: the day (and the calendar date once one exists), the verse, the act in
     the verse's own few words, then what changed in the tradition's words. STATE AS A STAMP, not prose — one colored word per line: NEW when
     an entity appears, OPEN when an entry is owed, CLOSED when the text pays it, TIMER when one is set or fires (its due as a day and, once
     a calendar exists, as a date in words). THE CLOCK MOVING IS ITS OWN LINE in its own color. EVERY LINE SAYS WHAT CHANGED — a line that
     writes nothing says so or is no line. FEW COLORS, A KEY, NO GREY: five colors at most, each one meaning, a one-line key at the bottom.
     GENERATED, NEVER TYPED: every line read from the journal's rows (the seal makes the rows current), the day from the clock, the counts
     from the world. A strip above: the day, the position in the text, how many things exist. A 'next' control beside any auto-play; the
     page scrolls as a page, no panes scrolling inside. NOT SHOWN: daemon names, ledger ops, ordinals, statuses that only restate.
     Creation week reads as seven dated lines and the human appearing on the sixth. On the owner's word; its own sitting, display only.
     THE OWNER'S WORD (2026-09-14, asked item by item): "lets refine the mockup first. I like it we are close" — THE BOARD mockup
     (the forms folder's board_mockup.py; the artifact "The Board of Things") is refined on his notes before the page is built; the page
     then reads the one database while the stepper runs (a small local server; the page polls for lines newer than the last drawn).
     THE OWNER'S FIRST NOTE (2026-09-14, the sitting after compaction #175): "put a small screen to the left, in it place the box that was created in the right as a stepper. the heavens box, then the earth box below it, then light below. The left box will scroll from bottom up as more boxes are added. When I click on any box it will bring me back to that step in the process." — repeated back, then "yes do it":
     VERSION 3 DRAWN — THE LEFT SCREEN: every tile, the moment it is created on the board, copied small into a strip on the left, oldest
     at the top, newest at the bottom, the strip scrolled to the bottom as it grows (the heavens, the earth, light the first three);
     a click on any small tile replays the rows from the start to the step that created it — the board, the clock, the feed and the step
     count as they stood then; the tiles ahead of that step stay in the strip dimmed so the click walks forward again (my reading of
     'bring me back', named in the reply); the births now read from the entities view of the one database (the retired rows gone, 0
     left) — 40 births, 340 rows, Genesis 1 to 11:2 unchanged; the artifact republished at the same link as version 3.
     HIS SECOND NOTE (the same sitting): "on the top right wher you have next, put a back button there. also when a new box is created make the browser display the first created box in the middle of the broswer screen" — VERSION 4 DRAWN: a Back button beside Next (one step back, the same replay);
     when a step creates tiles the page scrolls so the first of them sits mid-screen (the strip's own scroll centers the step's small
     tile, never moving the page).
     HIS THIRD NOTE (the same sitting, seen in Chrome): "open in chrome. when I click next and get the river out of eden it doesn't show it, it scrolls below to what came after. i want it to show the first boxes created then I will navagate down to see the rest" — the cause read off the rows: at Genesis 2:20's step (step 18)
     eight things are born at once across three groups, and the first by creation order (the tree of life, Plants) sits below the rivers
     (Places) on the board, so centering it pushed the rivers above the fold. VERSION 5 DRAWN: the page scrolls to the topmost new tile on
     the board and puts it at the top of the screen under the header, its group's heading with it; the rest below. Stepped to 18 in
     Chrome by the tools: the river out of Eden first under the header, the trees and the beasts below, the strip's eight lit at the
     bottom.
     HIS FOURTH NOTE: "once a title (places, times, plants, etc) fills up three rows, make the full 3 rows turn into a scrollable window. all titels should display 3 rows at all times" — VERSION 6 DRAWN: every group's tile area a window exactly three rows tall (one fixed row height;
     a long line in a tile clipped to two lines, the whole in its tooltip), scrolling inside itself past three rows; at a birth the
     window scrolls so the first new tile is its top row and the page scrolls the group's heading under the header. THIS AMENDS THE
     AGREED SHAPE above ("no panes scrolling inside") on the owner's word. Seen in Chrome: Places' seven tiles in a three-row box at
     step 18; People's fifteen in a three-row box with its own scrollbar at step 60. The generator's lint 3 → 6, all CSS words
     (three more style-sheet property names beside the three it had). The next note on the owner's word.
     BUILT 2026-09-14 on "lets build it" — THE BOARD (the design and the as-built sections after this list: decisions D22-D26; World/step9/
     world_board.py + world_board.html + board_names.yaml, the stepper's --pace; board_probes.py 0/8 → 8/8; the gate GREEN; run beside
     the paced stepper and seen forming in Chrome). Remaining under this item: the owner's notes on the real page as they come.
 11. A GRADED INPUT — an input's answer against an oracle through the port (scenarios grade against Mishnah rows at a cursor; the port only
     opens the door). WITH ITEM 1.
 12. THE OTHER WORLDS STEPPED — the stepper runs the running setting only; the sojourn forks and THE REST run whole in the tape. SMALL, if
     ever wanted. THE OWNER'S WORD (2026-09-14): "Both, when a sitting has room" — with item 8.

## THE BOARD — item 10's build: the design (2026-09-14; the owner: "lets build it", after six versions of the mockup on his notes)

THE OWNER'S WORDS THAT RULE IT: "a stationary display… one window within the browser… I want to see what is being created"; "a living
database showing the current state at all times"; "no hand inputs"; the six notes on the mockup (item 10). THE MOCKUP IS THE PICTURE; this
sitting builds the picture over the one database, display only — the board never drives the engine and never writes a row.

THE MEASUREMENTS (read off the database and the code before a line was written):
  - the one database holds every session's lines as rows of `events` with a rowid, `source` the session's name (cold_run_sequence/stepper
    the stepper's; port@<queue> a world with inputs; seed_isaac the base): 3,362 L3 rows for the base; the live sink INSERTs and commits
    at every seal, so a reader sees a session grow block by block (rowid the order; `DELETE FROM events WHERE source = ?` at attach —
    a new session under the same name starts at zero, a reader sees the count fall);
  - the stepper pauses on a keyboard (--pause) or runs N steps (--steps); there is no way to run at a pace without a keyboard;
  - the registry carries an English name (`en`) for all 338 of its entities; the entities view holds 273 things with a first mention, of
    which 149 are the units' own tokens (transliterations, not in the registry: shamayim the heavens, choshekh darkness …) with no
    English anywhere in the data; of the base tape's 360 subjects, 280 are registry ids and 80 the runners' own English ids (the-world,
    bezalel, nemuel-son-of-eliab), nine of them carrying "ben" (son of).

THE DECISIONS:
  D22 THE BOARD IS A READER — one Python file World/step9/world_board.py: a small local server (the standard library's http.server) over the
      one database opened READ-ONLY, three routes and the page; no route writes; the port stays the one door (D16). Runs beside the stepper:
        python3 World/step9/world_board.py [--source cold_run_sequence/stepper] [--port 8765] [--db path]
        GET /                          the page (World/step9/world_board.html, beside the script)
        GET /api/status                the sources in the database with their row counts, the default source
        GET /api/rows?source=S&after=R&known=N   the source's rows after rowid R, shaped as the mockup shapes them, with the births
                                       due before each row merged in; `last` the newest rowid; `count` the source's rows;
                                       `reset` true when count < N (the session started over — the page starts over)
        GET /api/names                 every id's English name and group (the registry's `en` first, then the board's own names table)
  D23 A THING APPEARS AT ITS FIRST MENTION — the births are the entities view's first mention per entity (the fold's rows; the August
      node.born rows are retired), every one, placed before the first marker or event row at or after its verse — the mockup's own rule,
      computed on the server so a row's births ride with it; the tile's word is "appears" (the mockup said "created" of its forty; the
      view says mentioned, not made — darkness and the deep appear at Genesis 1:2 without being created).
  D24 NAMES ARE DISPLAY, AND EVERY ONE IS ENGLISH — the registry's `en` names its entities; the units' tokens are named in
      World/step9/board_names.yaml (display only, edited in place as the gloss law allows; each with its group on the board); a runner's
      own dashed id reads as English by the id itself (the-world → the world); an underscored token with no name is REFUSED by the gate
      (a token is a transliteration — the law: never without its English). The tape's groups by the registry's kind (person People;
      people/collective/compound Peoples and groups; place Places; object Things; creature Creatures; institution Institutions; divine Heaven).
  D25 THE PAGE FOLLOWS, THE CONTROLS REPLAY — the page polls /api/rows once a second and appends what arrives to its own tape; FOLLOWING,
      it steps through every new block as it lands (the world forming at the stepper's pace); Next, Back, the left screen's click and
      Auto-play replay over what has arrived (the page's own tape, never the engine — the mockup's replay unchanged); "Follow" jumps back
      to the live end. The strip says which: LIVE with the source, or REPLAY at step n of N. A reset (D22's `reset`) empties the page.
  D26 THE PACE — the stepper's --pace S: a step every S seconds with no keyboard (S = 0 as fast as the engine goes), the watch mode the
      board needs; the pause's own report printed as before; one change in main(), none in the engine.
  AMENDED 2026-09-15 (the owner, watching the board live — "what does the follow button do" → "remove the folow button"): the
      Follow button REMOVED. The return to LIVE is the replay reaching the end of what has arrived — Next or Auto-play to the
      newest block, or a click on the newest tile — and the board rides live again by itself (step() and rewind() set following
      at the end; the message reads "riding live"). One page edit (world_board.html); the gate GREEN; board_probes 8/8. The
      as-built below describes the page as first built, with Follow. A LESSON the same hour: board_probes' B7 runs its own
      stepper session under the same source name and deletes the live session's rows (D22's reset) — NEVER run the board probes
      or a second stepper while a live stepper runs. THE SAME DAY, AFTER THIS: THE BOARD DRIVES THE ENGINE (D31-D33; the design and
      the as-built at the end of this file) — the engine waits and the page's Next and Auto-play/Stop step it.
THE GATE — python3 World/step9/world_board.py --gate [--source S]: (a) every id the source or the births would show has an English name
  by D24's rule (the unnamed listed, the gate red); (b) the board's shaping of the base's first 300 lines equals the mockup's embedded rows
  field for field, and the forty things the mockup called births are placed at the same rows (the mockup is the agreed picture); (c) the
  births' first three at Genesis 1:1: God, the heavens, the earth; light the eighth, at 1:3, after darkness, the waters, the spirit and
  the deep at 1:2 (AS TYPED IN THIS DESIGN: the heavens, the earth, light — the mockup's forty; B2's first run found God first,
  mentioned at 1:1 as the agent, and its second found darkness before light; the data's order stands and the gate demands it);
  (d) the page carries no embedded rows (it reads the routes).
THE PROBES — World/step9/board_probes.py B1-B8, written before the code and run to FAIL: B1 the shaping equal to the mockup's; B2 every
  entity of the view a birth at its first mention, placed by the rule; B3 every id named (the table complete for the base and the view);
  B4 the server answers the three routes over the real database read-only; B5 rows after a rowid are only the newer ones, with the births
  due before them; B6 a session starting over is reported as a reset; B7 the stepper runs three steps at --pace 0 with no keyboard; B8 the
  gate green and the page without embedded rows.
THE RUN: the stepper at a pace beside the server, the board opened in Chrome by the tools, the world forming from Genesis 1:5 on.
NOT IN THIS SITTING: the feed page and the panel page as real pages (the board is the one the owner chose); a page that drives the
  stepper (the owner: no hand inputs; display only); the design thread's window (item 9).

## THE BOARD — as built (2026-09-14; the owner: "lets build it")

THE CODE: World/step9/world_board.py — the server (`serve`: the standard library's threading HTTP server on 127.0.0.1:8765, the database
  opened read-only by URI with a busy timeout, one connection per request; the routes /, /api/status, /api/names, /api/rows); `shape` the
  one home for a row's shape (the mockup generator's functions moved in — head, own, short, words); `load_names`, `name_of`, `unnamed`,
  `all_names` (D24: the registry's `en` with its kind's group, a parenthesized dash-note trimmed for display; then board_names.yaml; then a
  runner's own dashed id read as English; an underscored token without a name raises Unnamed); `births` (D23: every entity of the entities
  view at its first mention, ordered by the fold's own mention rows — the text's order inside a verse; cached per database); `rows_after`
  (the API's answer: the source's light rows read whole for the anchors, the heavy rows only after R; a birth rides before the first marker
  or event row at or after its verse and only when the text reaches it; `reset` when the source's first rowid changed or its count fell);
  `status`; `gate`. World/step9/world_board.html — the mockup's sixth version with the rows fetched: FOLLOWING, every block that lands is
  stepped and drawn; Next, Back, the left screen and Auto-play replay over the page's own tape; Follow returns to the live end; the strip
  says LIVE or REPLAY and how many lines have arrived; a reset empties the page; no row embedded, nothing typed, nothing written.
  World/step9/board_names.yaml — 162 display names: the 149 tokens of the view, the nine runner ids with "ben", the three the mockup named
  by hand, and the_earth filed beside the heavens (the registry's kind puts it under Places). World/step9/world_stepper.py — `--pace S`
  (D26): one line in main's loop (`time.sleep`), the pace announced; the engine untouched.
THE PROBES: World/step9/board_probes.py 0/8 → 8/8. Corrected on the data's own order twice before they passed — B2 as typed wanted the
  mockup's forty (the heavens, the earth, light); the data's first three are God, the heavens, the earth at 1:1 (God the agent of 1:1),
  and light is the eighth, after darkness, the deep, the waters and the spirit at 1:2; the design and the gate carry the correction. Two
  hand-typed checks fixed: a born row carries no rowid (it rides with its anchor); my pace line's own words "no keyboard" tripped the check
  meant for the EOF message.
THE RUN: the server on 8765; python3 World/step9/world_stepper.py --by verse --pace 1 --steps 150 — 150 steps to the left edge of Genesis
  12:20 in 392 lines, 70 entities, 15 open entries, no pending timer, day 738,887, audited against the base (yes); the board opened in
  Chrome by the tools and seen following: step 18 at Genesis 2:20 with 43 things, ten seconds later step 29 at 3:17-19 with 48; a click on
  darkness in the left screen → REPLAY at step 1 with 8 things, the strip's 89 kept and the future dimmed; Follow → LIVE at step 140,
  Genesis 9:7, day 605,269, 90 things, 342 lines arrived; the paced session sealed while the board watched.
THE FINDING OF THE FIRST LIVE RUN: 274 things at step 7 of Genesis 1. Two flaws of mine — a new session under the same name deleted the
  old rows and outran their count between two polls, so `reset` by count alone was blind and the page kept the old lines; and my leftover
  rule appended every unreached birth after a sealed session's last row (the mockup's convenience, wrong on a live source). Fixed the same
  hour: `reset` by the source's first rowid (B6 extended to a session written anew with more rows), and no tail — a thing appears only when
  the text reaches it. The lesson under the standing ones: a rule copied from a mockup is a rule to re-derive on the live source.
THE GATE: python3 World/step9/world_board.py --gate — GREEN: every id named for the base and the stepper's source; the base's first 300
  lines EQUAL the mockup's rows field for field; the mockup's 40 births placed before the same rows; 273 things appear over the base, the
  first three God, the heavens, the earth at Genesis 1:1; the page reads the routes with no embedded rows.
THE STANDING GATES AT THE CLOSE (after the paced session and the probes wrote their sessions): step_probes.py 9/9; port_probes.py 9/9;
  world_journal.py --gate GREEN — the fold layer 12 kinds, 9,574 rows matching the header, the hash 8b8fff1fa28953af pinned and matched
  (the replay is the audit); the board's own gate GREEN; board_probes.py 8/8. The sweep not rerun: no runner and no engine line changed.
DISPLAY CHOICES (mine, display only, named here): the registry's `en` shown before its dash-note; the earth beside the heavens; the tile's
  word "appears"; a group's window three rows tall as the owner's fourth note ruled.
HOW TO WATCH: in one window `python3 World/step9/world_board.py` (the address printed); in another `python3 World/step9/world_stepper.py
  --by verse --pace 1` (or by chapter, marker, day; `--from <verse>`; `--queue <name>` for a world with inputs — the board follows
  `?source=cold_run_sequence/port@<name>`); open http://127.0.0.1:8765/ — the world forms; any other world in the database by `?source=`.
NOT IN THIS SITTING, NAMED: the feed and the panel as real pages (the owner chose the board); a page that drives the stepper (ruled out:
  no hand inputs, display only); a token of a future unit without a name — the gate names it, the table takes it; the server is one local
  process on 127.0.0.1 with no access control (a workshop tool, not the site).

## THE CHECKPOINTS AS THEY FALL — item 5's build: the design (2026-09-14; the owner: "Ok do it", after "What is checkpoints" was answered:
## a checkpoint is a test the tape carries with it, checked today only at the very end; item 5 asks each check at the verse where it belongs)

THE MEASUREMENTS (read off the code before a line was written):
  - THE BLOCK: cold_run_sequence.py's run() carries the checkpoints as one straight-line block, 416 statements (lines 2642-3062 today), 197
    `cp(...)` calls plus c3()'s (the 430's, already a function of the world); every cp is `w.checkpoint(name, declared, computed, bound)`;
    the engine's checkpoint PRINTS and RETURNS ok — it writes no log line and no journal line, so the base's bytes cannot move by asking;
  - the block reads eleven names of the run — w, M (the marker table), reg, C, D, markers, mF, events, fires, tset, closes_done — every one
    derivable from the world and its marker table; and it imports ten runner modules, the register gate and two stdlib names inside itself;
  - c3() is the precedent: the 430's checkpoints as a function of (w, M, R), already run on the fork's other worlds;
  - the stepper holds the world, the marker table and the tape's generator (self.w, self.M, self.gen); a pause has everything the block needs;
  - a checkpoint on a PARTIAL world can raise (M['ark_rested'] before the flood; w.clock.eras['exodus'] before the exodus; rel[0] on an
    empty list) — one raise in a preparatory line would abort every checkpoint after it.

THE DECISIONS:
  D27 THE CHECKPOINTS ARE A FUNCTION OF THE WORLD — the block moves VERBATIM into a module-level `checkpoints(w, M, reg)` that recomputes
      the run's derived names from the world's own log and returns rows (name, declared, computed, ok); run() calls it and grades exactly
      as before (the verdict list, THE GRADE's 10 tests, the RUN tuple, the base's bytes — unchanged; proven by the tape's own grade and the
      journal gate's two processes).
  D28 A PARTIAL WORLD RUNS THE BLOCK ONE STATEMENT AT A TIME — `checkpoints_partial(w, M, reg)` executes the SAME function's source
      statement by statement (its AST read from the module; no second copy of the block exists); a statement that raises is recorded and
      the run continues, its names unbound; a checkpoint that cannot be computed yet is NOT YET, never a DIVERGE; the prints silenced.
  D29 THE FALL IS MEASURED, NEVER TYPED — World/step9/checkpoint_positions.py steps the base by MARKER (the marker table's own grain) with
      the stepper's generator and evaluates the partial block at every pause; a checkpoint FALLS at the first pause from which its verdict
      and its computed value equal their final ones and stay so to the end; the script writes World/step9/checkpoint_positions.yaml
      (name → the pause's verse, the ordinal, the day, the pause index, the final verdict) — a record written by script, regenerated at
      every compile sitting whose block gains a checkpoint (a step of the compile shape, in the background like the sweep). The gate
      (`--check`) is cheap: every checkpoint of the block has a row and no row is stale; the positions themselves are re-measured when
      the block changes.
  D30 A PAUSE SHOWS THE CHECKPOINTS THAT FELL — the stepper's `--show checkpoints`: at each pause the partial block runs on the STEPPED
      world (live, never recited); printed: every checkpoint whose measured position is at or before the pause's ordinal, with its live
      verdict (MATCH / DIVERGE / NOT YET) and NEW on the ones that fell since the previous pause; the report line carries the counts.
      Opt-in — the block costs seconds — so a paced run for the board stays fast.
THE PROBES — World/step9/checkpoint_probes.py K1-K7, written before the code and run to FAIL: K1 the function exists and on the base world
  its verdict list equals VERDICTS (the tape's pinned expectation); K2 the partial executor on the whole base world gives the same verdicts;
  K3 on a partial world (run_to a verse) the executor never raises and reports NOT YET for what the tape has not reached; K4 the table has
  one row per checkpoint of the block and no other; K5 the positions read off the base segment — the flood's C1 falls no earlier than the
  ark-rested marker's line, the refuge cities' CR1 no earlier than the chapter's first event line; K6 the stepper stepped to a verse shows
  exactly the table's checkpoints at or before that ordinal with live verdicts; K7 asking the checkpoints writes nothing — the world's log
  and the sink's lines unchanged by a call.
THE ORDER: the probes to fail → D27 the extraction (the tape's grade unchanged) → D28 the executor → D29 the measurement in the background
  and the table → D30 the stepper's show → the probes green → the tape 10/10 → the journal gate → the records.
NOT IN THIS SITTING, NAMED: a checkpoint on the board (item 10's remainder — a tile that lights green as the world passes it); a checkpoint
  line in the journal (the ten classes stay; the base's bytes are this design's promise); the compile sittings' own checkpoint blocks
  rewritten into any other form (they stay as written; only their home moves).

## THE CHECKPOINTS AS THEY FALL — as built (2026-09-14; the owner: "Ok do it")

THE CODE: World/step9/cold_run_sequence.py — `checkpoints(w, M, reg)`: the block moved VERBATIM out of run() by a script that located it
  by its AST (the statement printing THE CHECKPOINTS through the `verdicts` assignment: 416 statements, 193 cp calls plus c3's six) and
  put it before run() with the run's derived names recomputed from the world (C, D, markers, mF, events, fires, tset, closes_done);
  every cp a row (name, declared, computed, ok) beside the tuple c3 appends; returns (rows, {yE}) — the one name run() reads after the
  block rides back with the rows; run() calls it and grades exactly as before. `checkpoint_names()`: the block's literal names read from
  the file's own source (197 — c3's join rows, C3d-70 and C3d-85, are named by the run). `checkpoints_partial(w, M, reg)` (D28): the
  same function's source one statement at a time in a namespace of the module, a raise recorded and the run continued, a checkpoint not
  produced a NOT YET row at its place in the block's order (the executor keeps R's order exactly, so on a whole world it equals the
  function's list — K2), nothing printed. World/step9/checkpoint_positions.py (D29): the base stepped by MARKER under its own session
  name (cold_run_sequence/positions), the partial block asked before the first line and at every pause, the fall computed, the table
  written by script; `--check` the cheap gate. World/step9/checkpoint_positions.yaml: 199 rows. World/step9/world_stepper.py (D30):
  `--show checkpoints` — the block asked LIVE on the stepped world at each pause; the rows those whose measured fall is at or before the
  pause's ordinal, each with its live verdict and NEW since the last pause; the summary line with the counts; `self.reg` kept at open.
THE MEASUREMENT (checkpoint_positions.py, 944 s): 199 checkpoints over 159 pauses on 3,362 lines; 48 hold from before the first line
  (pure ink — C0's Genesis 5 arithmetic, the parser's readings, the letters — or an absence the tape never fills: CR7's has_blood NONE);
  the last fall at pause 158, Numbers 36:11, the tape's last line (CR1's clause "before the tribes' plea" holds only there); the finals
  MATCH 181, DIVERGE 18 — the eighteen the design expects (VERDICTS). Read off the table: C1 the flood's 150 days falls at Genesis 8:4,
  ordinal 221, the ark-rested marker's own line; C2 Noah's 600 and C10 Methuselah's seven days at 6:3; CR5 the refuge cities' term at
  Numbers 21:4 — the pause after Eleazar's investiture (20:28), where its state settles, thirteen chapters before its own chapter.
THE PROBES: checkpoint_probes.py 0/7 → 4/7 → 7/7. Two hand-typed expectations corrected: K3's partial world was typed at Genesis 8:5,
  past the ark-rested marker (there C1 is computed, a DIVERGE as the tape's own gap says) — moved to the flood marker's left edge, 7:11;
  and three probes read the function's (rows, exported) pair as the rows — the as-built's honest form, the probes adapted.
THE RUN: `python3 World/step9/world_stepper.py --by chapter --steps 8 --show checkpoints --quiet` — at the first pause the 48 that hold
  from the start; Genesis 5: CG9 Adam's 930; Genesis 6: C2 MATCH and C10 DIVERGE at 6:3; Genesis 7: CG2 the reprieve's timer and CG3 the
  seven days' timer at 7:11; Genesis 8: C1 DIVERGE at 8:4, CG4 the dove at 8:13, CG1 Eduyot's twelve months at 8:14 — every one asked live.
THE GATES: the tape 10/10 (the verdict list, THE REST, the RUN tuple unmoved; 13.0 s); the journal gate GREEN (the fold layer 12 kinds,
  9,574 rows; the hash 8b8fff1fa28953af); the positions gate GREEN (197 literal names, 199 rows, missing none, stale none); K7 the base's
  bytes: a call of the block leaves the log and the sink at 3,362 lines. The lint: the sequence file at its baseline 7; the rest 0.
NOT DONE, NAMED: a floor on the 48 that hold from the start (a display choice — the block's own verse — not taken: the measurement says
  what is true); a checkpoint on the board (item 10's remainder); the stepper's report line counts the checkpoints only under --show.
THE LESSON: a checkpoint falls where its STATE settles, not where its chapter is — CR5 at Numbers 21:4 — and the measurement, not the
  hand, is what could say so.

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
  (6) The board's births come from the entities view (a note in the mockup's generator; PAID the same day at the mockup's version 3 —
      the generator reads the view; item 10 of the list).

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
THE GATE: GREEN — the four segments byte-identical across two processes, chains verified; the live index 13,444 rows identical between the processes and equal to the rebuild; the five run views MATCH on every source; THE FOLD LAYER's new line: units 210, facts 1,809, demands 341, events 557, names 81, standing 2,163, open demands 191 and the state hash 8b8fff1fa28953af each MATCH the pinned truth, 12 kinds and 9,574 rows in the index MATCHING the header.
THE PROBES AFTER: journal 7/7, live 7/7, step 9/9, port 9/9, cursor 6/6 after the journal module's change.
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


## THE BOARD DRIVES THE ENGINE — the design (2026-09-15; the owner, watching the board live: "it seems to keep running no matter what button I push" → "the buttons should control the engine, it should not run on auto pilot behind the scenes. is there a reason it should?" → "put a stop button also. if I click autoplay it shoudl change to stop. one button two options. built it")
THE QUESTION ANSWERED FIRST: no reason for the board — the autopilot (D26's --pace) was the reader's design, the page forbidden to write;
the only use for an engine that runs unattended is the gates (the tape check, the positions' measurement), which stay a command-line
mode with no page.
  D31 THE BOARD DRIVES THE ENGINE — the engine in --board mode (world_stepper.py) takes exactly one step per ask and waits between asks;
      it never runs on its own under the board. On the page, Next at the live end asks one step; Next behind the live end walks the view
      forward as before; Back and the left screen replay what has happened (an engine cannot un-run a verse — to stand at an earlier
      step for real is the cursor's job: the engine started over and walked there).
  D32 ONE BUTTON, TWO WORDS — Auto-play runs the page's clock at the speed dial: while the view is behind the live end each tick steps
      the view; at the live end each tick asks the engine for one step; the button reads Stop while the clock runs; Stop stops the clock
      and the engine waits (nothing more is asked). No Follow button (removed the same day, before this: the return to LIVE is reaching
      the end of what has arrived).
  D33 THE STEP SIGNAL — two small files beside the database, one writer each way: board_asks.json (the server: a count of asks, written
      whole and replaced) and board_engine.json (the engine: pid, source, done, opened_at, waiting, sealed, next, end, a heartbeat). The
      server's one control route, POST /api/control {"cmd": "step"}, is the only thing the board writes — never the database, which
      stays read-only. The engine consumes only asks made after it opened (opened_at); one ask outstanding at a time on the page (no
      pile-up); the page's header shows ENGINE: "waits at <verse>" / "stepping" / "none" (no heartbeat within five seconds, or sealed) /
      "the end of the tape"; with no engine, Next and Auto-play say so and stop. Ctrl-C seals the session.
THE PROBES — World/step9/drive_probes.py X1-X5, written before the code and run to FAIL, each in ITS OWN journal folder (WORLD_JOURNAL_DIR)
on its own port — never over the live session: X1 the engine announces itself and takes no step unasked in three seconds; X2 the control
route counts an ask and the status reports the engine; X3 three asks are exactly three steps and the engine waits after them; X4 Ctrl-C
seals and the board sees no engine; X5 the page carries Stop, the control route and --board, no Follow, and the gate is green.

## THE BOARD DRIVES THE ENGINE — as built (2026-09-15, the same sitting)
THE FAIL RUN: X1 FAIL (no --board: the engine ran the whole tape, 3,362 rows unasked); the probe itself crashed at X2 because the old server
closes a POST without answering — its catch widened (an unexpected error is a FAIL, not a crash). THE CODE: world_stepper.py — BoardControl
(the two files; asked(), pending(), beat() once a second or on a change), --board in main() (the loop waits 50 ms at a time while nothing
is pending; KeyboardInterrupt seals; the SIGINT handler restored explicitly), the usage paragraph; world_board.py — control_paths,
engine_state, ask_step (a lock; write whole, replace), the engine in /api/status and /api/rows, /api/engine, do_POST /api/control, the
serve() line; world_board.html — the ENGINE word in the header, askStep/tick/postJSON/drawEngine, Next asks at the live end, Auto-play
and Stop one button, the messages. THE SECOND RUN: 4/5 — X4 FAIL: the engine ignored Ctrl-C (started in the background from a shell
without job control, SIGINT arrives ignored and the child inherits it) → the handler restored in --board mode → 5/5. THE LIVE CHECK in
Chrome: the engine announced "waits at Gen 1:5"; Auto-play → the button read Stop and the engine took one ask a tick (done 7 in four
seconds at medium, waiting between); Stop → the count held at 11 across two reads; Next → 12, the page at step 20, Genesis 2:21-22, the
engine waiting at 2:23. The gate GREEN; board_probes.py 8/8 (run in its own journal folder — B7 runs a stepper of its own); the lints at
baseline; the home-path gate GREEN. THE RECORDS: SETUP.md's section 4, World/README.md, World/RESUME.md, THE_STEPS.md's board paragraph,
the recovery file's section 30, the state doc's #180 addendum 2, THE_BRIEFING's scoreboard and entry, memory. LESSONS: A PROBE RUNS
NOTHING UNDER THE LIVE SESSION'S NAME (its own journal folder, its own port — board_probes' B7 wiped the live session once this day; run
those probes with WORLD_JOURNAL_DIR set while an engine is live); A BACKGROUND CHILD MAY INHERIT SIGINT IGNORED (restore the handler where
Ctrl-C must mean something); A CATCH THAT NAMES THE EXPECTED ERRORS LETS THE UNEXPECTED ONE CRASH THE PROBE.
