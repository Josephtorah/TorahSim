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
