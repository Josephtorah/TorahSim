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
| 6 THE READBACK (named 2026-09-09, D12; no design yet) | the text re-read against the ledger the run left — the third pass the shelf records (the repetition in the plains of Moab; understanding after the forty-year run): Deuteronomy's repetition of the laws read against the run's ledger first, the prophets' indictments against the open entries after (the effects law's target) | its design section waits for Deuteronomy | unsized |

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
  unconsumed count stays the separate tripwire it is today.
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

## Standing duty

Every compaction point from #107 on carries THE LOOP as a named item until step 4 lands; every "NEXT" line in the
state doc and memory names it beside T1. CHRONICLE.md (the design thread's screen) reads the index of step 2 when
it is built; that folder is not ours to edit — the design thread reads this file.
