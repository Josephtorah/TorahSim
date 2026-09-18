# THE RECOVERY ADDENDA — the history behind the recovery page (2026-09-16: the one-read entry became the short page RECOVERY_new_thread_2026-09-12.md,
# rewritten each sitting; this file keeps its sections 1-35 as written and APPENDS from here; older records' "the recovery file's section N" means this file)

# RECOVERY FILE FOR A NEW THREAD (written 2026-09-12 at THE NUMBERS WALK sitting 10b's close, on the owner's word)

Read this file FIRST in a new thread, whole. It is the one-read entry point. The long chronicle is the state doc
(logic/pre_logic_methods_2026-07-28/PROMPT_continue_solo_era_2026-08-06.md, 17,000+ lines; read its TAIL with an offset,
the Read tool caps at 25k tokens). The memory index (MEMORY.md, auto-loaded) points to the rest.

## 1. WHO AND WHAT

The owner is Brian LeBlanc (never "Ben"; the mac username <user> is a red herring; GitHub Josephtorah). He is terse.
Replies are SHORT; depth goes in the files; explanations in PLAIN PICTURES; CHAPTER NUMBERS, never portion names.
He compacts at ~700k-900k tokens and expects a clean compaction point announced at every milestone.

The mission: the 24 books of the Hebrew Bible are the PROGRAM, the Talmud holds the COMPILE RULES, the Mishnah is the
ANSWER SHEET. ONE world runs on a tape of events in verse order (Genesis 1 to the current verse). Every verse either
adds a line to the tape or installs a law (a daemon) that watches the tape. Laws write EFFECTS on ledgers (never the
event stream). Code comes only from the written 24 books; Mishnah and Talmud rows are TEST DATA at runtime.
Repo: <repo-old> (sole truth). The public mirror TorahSim is downstream, relay only at owner direction.

## 2. WHERE IT STANDS (2026-09-12, the state doc's COMPACTION POINT #144)

- NUMBERS 1:1-30:17 READ, FROZEN, COMPILED AND ON THE TAPE (chapter 27 done at THE TENT; the case chapters 9,
  15:32-41, 27, 36 were run first as THE TENT and are SKIPPED on the walk).
- 205 frozen units, standing 2103, world hash 8b8fff1fa28953af UNMOVED.
- 52 cold runners, 57 daemons, 397 functions WRAPPED; the sweep 52/52 at 6,045 graded cells.
- The tape: RUN = (1246, 60, 52, 0, 12, 1470, 28, 302, the four pairs, 114); 157 markers; 302 entities; the
  population table 136 rows; the counter at (40, 6, 1) = the fortieth year, sixth month, first day.
- THE REGISTER GATE --strict GREEN (DECLARED 112, DEBT 0); the journal gate GREEN; every probe gate green.
- LAST COMMIT a42f518 (2026-09-11; sittings 2 through 7b, pushed as Josephtorah). EVERYTHING SINCE IS UNCOMMITTED
  (sittings 8, 8b, the discussion step, the register gate, 9, 9b, 10, 10b). Commit ONLY on the owner's "commit push".
- NEXT: CHAPTER 31 — Midian's reading (sitting 11), then its compile (11b). Never the next reading first.
  Remaining after it: chapters 32, 33, 34, 35 (36 already run). Then Deuteronomy. Then the second pass.

## 3. THE STANDING LAWS (owner-ruled; keep verbatim in spirit)

- NO AGENTS EVER. Main thread only. No task lists. Owner-directed blocks: a sitting opens on his word ("Go").
- DISCUSSION IS NOT A RULING (2026-09-11): never change direction on a remark; discuss first, act on the explicit word.
- READ THEN COMPILE PER PORTION (2026-09-10 "Finish compiling before moving on"); never read ahead.
- HEBREW NEVER WITHOUT ITS ENGLISH INLINE, EVERYWHERE, EVER. Hebrew SCRIPT first, the gloss FOLLOWS within ninety
  characters. The lint: `python3 <repo-old>/logic/solo_tools/gloss_lint.py <file>`. Every term in the
  lint's own JARGON list (the vowel-point, accent, scribal and rabbinic-genre terms; read the list in gloss_lint.py,
  never retype it into a record) and every hyphenated non-English compound needs a gloss marker ("(", a quote, "="
  or ", the/a/an") within 90 characters AFTER; inside a Python double-quoted string use SINGLE quotes as the
  marker. Transliterations avoided or glossed. Book names in FULL (Babylonian Talmud, never Bavli).
- LINT BASELINES (a record is at baseline or the new content is fixed): the state doc 147, THE_STEPS 1, MIDDOT.md 1,
  THE_WORLD.md 5, STAMP_LEDGER 1, MOVE_CATALOG 5, RESEARCH_LOG 52, memory step9-exam-era.md 7, MEMORY.md 5,
  cold_run_sequence.py 7, census_probes.py 1; everything else 0 (THE_BRIEFING, COMPILE_DEBT, THE_LOOP, THE_TENT,
  NUMBERS_WALK, SEQUENTIAL_RUN, RESUME, MISHNAH_TOPICS, REGISTER_INDEX, numbers-in-order-ruling.md, every ledger,
  manifest, docket, runner, probe file, registry).
- LEDGERS ARE APPEND-ONLY (corrections APPENDED; a record regenerated only inside its own writing step).
  Registries (the yaml files) are rewritable with the gates green.
- COVERAGE IS COMPUTED, NEVER RECITED. Every "measured" claim goes through a script. A gate's FAIL is READ. A miss is
  evidence: read it, then retype from the print. THE MEASUREMENT PRINT HAS THE INDEX (type every index and slice
  width from the print). A STACK IS SUMMED FROM THE PAGE, never from memory.
- NO MACHINE USERNAME, NO HOME PATH, ANYWHERE IN THE PROJECT (the owner, 2026-09-15; reviews/PORTABLE_repo_2026-09-15.md "THE USERNAME
  SCRUB"): a path in a record is written with the markers <repo>, <world-link>, <scratch>, <memory>, <home>; the gate
  `python3 logic/solo_tools/scrub_home_paths.py --check` runs as the pre-commit hook and refuses a commit that carries one; the one pass
  over the records that installed this rule was the append-only law's single exception, on the owner's word.
- NEVER Write a new record to a path without `ls` first. AN APPEND BUILDS THE WHOLE TEXT BEFORE IT OPENS THE FILE FOR WRITING
  (2026-09-15: `open(p, 'w').write(read(p) + text)` truncates p before read runs — the state doc and this file were emptied to their
  newest section and rebuilt from the commit plus a replay of the session's own scripts; read into a variable, then open to write).
- Keep ALL records current UNPROMPTED: the state doc checkpoint at EVERY milestone; THE_STEPS.md and THE_BRIEFING.md
  (root) current; World/RESUME.md; memory (numbers-in-order-ruling.md, MEMORY.md under 17,000 bytes,
  step9-exam-era.md's STANDING LESSONS head). Announce clean compaction points.
- THE NEVER-COMMIT SET: Data/discord_backup_codes.txt (SECRETS), DISPOSABLE_scan/*.zip, open_ledger/ (own nested git),
  elijah_docket (nested gitlink, never stage), grok-mockups/ (a folder of mockups), logic/gork/, cases_pilot.yaml; ARCHITECTURE/* is the
  design thread's (READ, never edit, never stage; except ARCHITECTURE/DATABASE_SPECULATION.md, ours to APPEND, still
  unstaged); World/journal/data/ is gitignored derived data.
- STAGING BY EXCLUSION: `cd <repo-old> && git add -A -- . ':!logic/gork' ':!grok-mockups' ':!open_ledger'
  ':!DISPOSABLE_scan' ':!Data/discord_backup_codes.txt' ':!cases_pilot.yaml' ':!elijah_docket' ':!ARCHITECTURE'`.
  Commit message via `git commit -F <scratchpad file>`; trailers `Co-Authored-By: Claude Fable 5.1
  <noreply@anthropic.com>` and `Claude-Session: <the session url>`. Push: `gh auth switch --user Josephtorah`,
  `git push origin main`, `gh auth switch --user PeerloopLLC`.
- SINCE THE PORTABLE REPO (2026-09-15, reviews/PORTABLE_repo_2026-09-15.md): THE FOLDER IS <repo>, the repository
  https://github.com/Josephtorah/TorahSim.git, the symlink <world-link> -> <repo>/World; every path in the code is
  computed from the file's own place (`_ROOT`), never typed absolute again — a new script computes its root the same way; the staging form
  and the cd rule below read with the new folder name; the store is Data/tanakh.sqlite (tracked), the snapshot store
  torah_grok.SNAPSHOT-main-51801ca.sqlite a release asset (`python3 Data/fetch_shelf.py --stores`), the shelf fetched from Sefaria's
  bucket (`python3 Data/fetch_shelf.py`); SETUP.md at the root is a clone's first read. The old paths in old entries stand as history.
- ABSOLUTE PATHS ALWAYS. Every git command begins `cd <repo-old> &&` (since 2026-09-15: <repo>). THE cd LESSON (eight instances):
  the cwd persists across Bash calls and a cd at the head of a compound command reaches its tail; run each repo-root
  tool in its own `(cd <repo-old> && python3 /abs/path ...)` subshell.
- zsh treats `echo ====` as a glob (use `----`). macOS has no `timeout`. Any script importing cold_run_sequence takes
  40-90 s. The sweep (`python3 World/step9/run_cold_all.py`, ~15 min, 52 runners) runs in the BACKGROUND; the journal
  gate (`python3 World/step9/world_journal.py --gate`) NEVER concurrently with the sweep. THE REGISTER GATE
  (`python3 World/step9/register_census.py --strict`, ~90 s) at every compile sitting's gates step, NOT in the sweep;
  `--emit` prints yaml stubs for undeclared seats; a paid seat's entry is DELETED from register_dispositions.yaml
  (the key AND its indented body); the yaml is parsed before it is trusted (double single quotes inside a
  single-quoted scalar). SINCE 2026-09-14 (section 23): the journal gate carries THE FOLD LAYER's line — after any freeze run
  `python3 World/build_world.py` before it, or it refuses the stale layer.
- Corpus bake: set the tripwire's literals to the PREDICTION first, then `python3 <repo-old>/corpus_world.py`
  and `python3 <repo-old>/logic/corpus/CORPUS_TRUTH.py`. Freeze automatically on green pre-flight.
  Every frozen unit gets logic/py_units/<uid>.py. A SEARCH OF THE SHELF STRIPS THE VOWEL POINTS.
- THE LINK REVIEW LAW (2026-09-07): no link of our own unless a teacher taught it (Pesachim 66a). REFERENCE (the ink
  names it) vs TRANSFER (needs a teacher, else a labeled HYPOTHESIS). Every edge in dependency_dispositions.yaml
  carries `link:`.
- THE EFFECTS LAW: every compiled function's verdicts carry effects from World/step9/effect_vocabulary.yaml, writing the
  LEDGER never the event stream. CODE/DATA SEPARATION: Mishnah/Talmud rows are DATA rows with settings, never code.
- THE COMPILER LAW: MOVE_CATALOG.md (M-01..M-28) updated UNPROMPTED; findings AUTO-SEAT; a cold-compiled function per
  law span (five motions + WRAP); the checklist World/step9/COMPILE_DEBT.md.
- A MIDDAH CODE IS CHECKED IN logic/MIDDOT.md BEFORE IT IS TYPED (the likening, hekkesh, has NO I-code).
- THE ENGLISH SUPPLIES THE MISHNAH: read the Hebrew row of the Sifrei before crediting content to it.
- THE MODULE-NAME COLLISION GUARD: never name a helper law_*. THE SEQUENCE FILE'S `import cold_run_X` LINE IS THE LIVE
  EDGE the dependency gate reads. THE DAEMON GATE READS LITERAL SUBMITS ONLY (`if k == '...'` branches, effects from
  literal W dicts). THE HONEST-PAIRING GUARD READS LITERALS ONLY (a Name as an expected value is refused; inline the
  tuple). A PROBE HARNESS CATCHES BaseException. THE ORDINALS ARE NOT CARDINALS (ink_ordinals holds the month-ordinals).
  A PROBE TOKEN IS THE WHOLE WORD WITH ITS PREFIX. A PENDING TIMER IS NOT A LEDGER ENTRY. A CONSTANT READ IS NO CALL
  FORM. A RETYPE COVERS EVERY LINE OF A MULTI-LINE LITERAL. THE OLD CHECKPOINT KEEPS ITS VERSES. THE STORE'S SHORT
  STEMS (a manifest check word is the word's longest store-piece taken whole; never a prefix fragment).
- THE TOKEN CENSUS SEES PAST THE IMPORTS: the dependency gate can demand an edge the runner never imports; read the
  token's homes, declare (CALL / VIA / FALSE / OWED / PARAMETER / REVERSE) with a why and a link.
- A TEIKU IS A ROW VALUE 'unresolved': the tradition's open question is carried, never forced to a verdict.
- POST-COMPACTION RULE: the FIRST sitting after any compaction (or a new thread) rereads THE_STEPS Step 2 + Step 5 +
  the compiler block, memory's STANDING LESSONS head (step9-exam-era.md from line 959), NUMBERS_WALK.md's last two
  sections, and the state doc's last checkpoint BEFORE deriving.
- LAW IS CODE, NARRATIVE IS DATA (the owner, 2026-09-15, verbatim in the design thread, on the record on his "Yes" there; relayed to the
  main thread the same day): "Law is code. Let's keep that in mind." / "law is code and narrative is data, variables, and whatever else it
  does." A legal passage in ANY book (the prophets' rules included) is a procedure to compile, never a description to summarize; a later
  book's rule is a spec with its own constants, run and diverge-checked against the Torah's; narrative is the tape's event stream — its
  numbers the variables, its dates the markers, its acts the calls and the installing switches, its receipts the closes; the tent the one
  reverse flow. The full text in THE_STEPS.md's compiler-law block and THE_WORLD.md's idea log.

## 4. THE FILE MAP

Root: THE_STEPS.md (the plain-language process, Brian's reference; its vocabulary is ours), THE_BRIEFING.md (the big
picture + the scoreboard, newest first; entries only at process upgrades), THE_WORLD.md (the simulation's master
file), RESEARCH_LOG.md (the findings log), corpus_world.py, cases_pilot.yaml (never commit).
logic/: MIDDOT.md (13 law middot, 32 narrative, "the middot's own case law" section), MOVE_CATALOG.md, CORE_SHELF.md
(the standing shelf + the book-name decoder), MISHNAH_TOPICS.md, units/ (frozen yaml), py_units/, oral_audit/manifests/,
oral_triage/ (reading ledgers and exam dockets, e.g. num_30_vows_2026-09-12.md and num_30_vows_exam_2026-09-12.md),
corpus/CORPUS_TRUTH.py, solo_tools/gloss_lint.py, pre_logic_methods_2026-07-28/ (the state doc; this file).
World/step9/: THE_LOOP.md (the running simulation with memory, steps 1-5 built, THE REGISTER GATE design), THE_TENT.md,
NUMBERS_WALK.md (every Numbers sitting's design + as-built; read "Sitting 10" for the reading shape and "Sitting 10b"
for the compile shape), COMPILE_DEBT.md, SEQUENTIAL_RUN.md (section 9 = the conventions for Numbers), world_engine.py,
cold_run_sequence.py (THE TAPE: the INK block, DAEMON_ORDER, the tape section between `# ==== TAPE BEGIN` and
`# ==== TAPE END ====`, the literals CENSUS / PLACEMENT / SLOTS / RUN / PREVIOUS_RUN / NEWEST_RUNNER / VERDICTS, the
cp() checkpoints), cold_run_<span>.py (52 runners; cold_run_vows.py the newest, the form to copy), the five registries
(event_vocabulary.yaml, effect_vocabulary.yaml, daemon_dispositions.yaml, dependency_dispositions.yaml,
calendar_parameters.yaml, population_schema.yaml, register_dispositions.yaml), the gates (daemon_census.py,
dependency_census.py, register_census.py, world_journal.py --gate, claim_labels_census.py, run_cold_all.py), the probes
(census_probes.py 174, installation_probes.py, register_probes.py, sequence_probes.py, cursor_probes.py, view_probes.py,
population_probes.py, journal_probes.py, clock_probes.py), the gate-written indexes (DAEMON_INDEX.md,
DEPENDENCY_INDEX.md, REGISTER_INDEX.md), World/journal/ (the sink; data/ gitignored), World/RESUME.md (the World folder's
own resume; append a SITTING line each sitting), forms_numbers_walk/ (the working scripts copied from the old
scratchpad on 2026-09-12, the backup copies of records pruned: seq_record.py, seq_stitch.py, add_types_*.py, write_*_docket.py, *_dump.py, *_measure*.py,
*_ink.py, *_rows_*.py, write_*_ledger.py, the docket parts; copy the latest to the new scratchpad and edit there).
elijah_docket/tanakh.sqlite: the full-Tanakh lemma database (nested git, never commit from inside) — SINCE 2026-09-15 the code reads its
copy Data/tanakh.sqlite, tracked in the repo; the nested folder keeps its own. The Talmud shelf is
LOCAL (the export's segments "Tractate 12a:3"; Mishnah "Mishnah Nedarim 11:6"; the Sifrei on Numbers by piska and row;
Onkelos by verse). The old scratchpad (may still exist on disk):
<scratch>.
Memory: <memory>/ (MEMORY.md the index; numbers-in-order-ruling.md
the walk's running record; step9-exam-era.md the lessons; the-loop-ruling.md; standing_orders_torah_grok.md).

## 5. THE TWO SITTING SHAPES

THE READING SITTING (sitting 10's form, one chapter or portion): measure first (the dump of Onkelos whole + the Sifrei's
piskaot BY POSITION from the local shelf; the export's heads checked against the rows' own quotations, the
mistyped-head class is real) → the parser measured on every number verse of the span (cold_run_sequence.verse_words'
marks: star = refused homograph; ink_numbers / ink_ordinals) BEFORE any claim is typed → the ink asserts script (the
Hebrew facts computed on the DB; asserts 1 fell → 0) → the rows files → the ledger writer with coverage COMPUTED (no cut
miss; lint 0) → the unit yaml + manifest (check words verified by the store) → the claims seated (the ritual, 13 PASS)
→ the fold predicted and matched (units +1, standing + the claims, hash unmoved) → the records (NUMBERS_WALK "Sitting
N", RESEARCH_LOG, MIDDOT's case-law entries from the Sifrei, THE_STEPS, THE_BRIEFING, RESUME, memory, the state doc
checkpoint). SINCE D7'S MERGE (2026-09-14, section 23): after the freeze, `python3 World/build_world.py` — the fold layer of the
one database rebuilt and reconciled; the journal gate at the next compile sitting refuses a stale layer (the hash moved, the header did not).

THE COMPILE SITTING (1b's order, as at 10b): the measurements (the tape's state, the callees live, the registries'
counts, the register gate's seats in the span) → THE DESIGN written into NUMBERS_WALK.md BEFORE any code (the name, the
cells F1…, the state machine or tables, the DATA rows, the daemon with given_at and installed_by, the tape lines and
markers, the checkpoints C?1-C?9, THE PREDICTION'S ARITHMETIC for RUN / CENSUS / PLACEMENT, the probes, the types, THE
ORDER) → the probes to FAIL first (census_probes for the parser; register_probes if the gate changes) → the state doc's
checkpoint (the docket may cross a compaction) → THE DOCKET by the union rule (the scan script sizes it; the dump read
in chunks; ONE VERDICT PART PER CHUNK on disk; the writer with coverage COMPUTED and the cite index; verdicts LAW /
DERIVATION / DISPUTE / CONTEXT / OUTSIDE) → the types by script (kinds, effects, the daemon block, the functions block,
the span, the edges, calendar rows) → the gates to FAIL (daemon, dependency) → the runner (the honest-pairing guard;
the INK block exec'd from the sequence file; zero-report probes; cells returning out(verdict, effects); the daemon with
literal W dicts; scene() and narrative() with the tuples PREDICTED BY SCRIPT; CASES with literal expecteds; the guard's
count typed after the first graded run) → the recorder (seq_record.py: globs runners, writes seq_recording.json) → the
stitcher (seq_stitch.py: SPAN_ORDER, writes the tape section, prints the CENSUS / PLACEMENT / SLOTS literals) → the
literals and the checkpoints typed into cold_run_sequence.py (every line of a multi-line literal; NEWEST_RUNNER;
PREVIOUS_RUN = the last sitting's RUN) → the tape run (`python3 World/step9/cold_run_sequence.py`, THE GRADE 10 TESTS
incl. THE REST) → the probe gates → the daemon and dependency gates GREEN → the journal gate → THE REGISTER GATE
--strict (the span's seats declared from the print) → the sweep in the background → SINCE ITEM 5 (2026-09-14): a sitting whose
checkpoint block gained a checkpoint reruns `python3 World/step9/checkpoint_positions.py` in the background (the fall of every checkpoint
measured, the table rewritten; `--check` the cheap gate) → the records (NUMBERS_WALK "AS
BUILT", COMPILE_DEBT's box PAID + new debts, MOVE_CATALOG, MIDDOT, MISHNAH_TOPICS, RESEARCH_LOG, THE_STEPS,
THE_BRIEFING, RESUME, memory, the state doc's checkpoint at the close).

## 6. CHAPTER 31, THE NEXT SITTING (from the state doc's #144)

Midian's reading, 31:1-54, as one draft (or two at the spoil's division, 31:25; decided at the measurements). The
Sifrei on Numbers piskaot 157-158 BY POSITION; Onkelos whole (54 verses). THE PARSER measured on the chapter's number
verses BEFORE any claim: the spoil's census 31:32-47 (675,000 sheep, 72,000 cattle, 61,000 donkeys, 32,000 persons),
the halves and the tributes (one soul of five hundred, one of fifty: THE FRACTION CLASS at 31:28-30), the 16,750
shekels of 31:52. The register gate's seats in the chapter are declared NONE now (the receipts 31:7, 31:31, 31:41,
31:47; the count lines 31:35, 31:36, 31:40, 31:46) with the why "chapters 31-36 are NOT YET WALKED": the compile pays
them (delete each paid seat's key and body). The crowns to look for: Balaam's death (31:8), the Midianite women and
Peor (31:16, the sotah runner's and Balak's seats), the purification of the warriors (31:19-24: the heifer runner's
water of separation by CALL; the kashering of vessels 31:22-23, the fire-passing rule), the spoil's arithmetic as
checksums (the halves and the tributes summing exactly), the atonement offering of the officers (31:48-54). Then its
compile (11b) on 1b's order.

## 7. THE OWED ITEMS (not on the walk's path; the full lists in COMPILE_DEBT.md)

The second pass after Deuteronomy: the installed_by settings (D2; laws in Moses' voice at 30:2 and 36:6 are boot now),
D7's merge, STEP 6 THE READBACK. Deuteronomy 23:22-24 (the delay ban's own compile). Numbers 32:24 (chapter 32's seat
for the utterance rule). Num 35:5's cubits (Masei). The altar token's two seats (a registry sitting). The musaf debit's
lapse rule. The dotted tenth at 29:15 and the store's dropped large letters (the DB lacks the marks). The receipt
finder's third form with the other Name (Gen 6:22, 7:9, 7:16). The two TEIKU rows of the vows. Elijah / Ezekiel
deferred until Ezekiel is derived. bamidbar → minchah's call. The narrative census, the fringes, the cursor inside a
bound.

## 8. ADDENDUM (2026-09-12, at sitting 11's close — the new thread's first sitting, on the owner's "ok go")

SITTING 11 DONE: CHAPTER 31 (Midian) READ AND FROZEN — 206 units, standing 2114, hash 8b8fff1fa28953af unmoved; the state doc's COMPACTION POINT
#145 is the current tail (its NEXT and its REREADS govern); NUMBERS_WALK.md "Sitting 11" the record; COMPILE_DEBT.md's sitting-11 box (a)-(n) the
compile's checklist. Section 2 above now reads: NUMBERS 1:1-31:54 READ (27 by THE TENT), 1:1-30:17 COMPILED AND ON THE TAPE; 31 NOT YET COMPILED.
Section 6 above is DONE; its compile (11b) is NEXT, on section 5's compile shape, with the fraction class ("one of the N", six Bible seats measured)
taught to the parser first and the register gate's eight chapter-31 seats paid. The scratchpad of this thread:
<scratch> (the midian_*.py forms, midian_legs.py the leg
diagnostic, write_midian_*.py). Still UNCOMMITTED since a42f518; commit only on "commit push".

## 9. ADDENDUM (2026-09-12, at sitting 11b's close and THE CLOSE LINE — the state doc's COMPACTION POINT #148; this supersedes section 2's
## "where it stands" and section 6's plan, which are kept as written)

WHERE IT STANDS: NUMBERS 1:1-31:54 READ, FROZEN, COMPILED AND ON THE TAPE (27 by THE TENT) — 206 units, standing 2114, hash unmoved; 53
runners (cold_run_midian.py the 53rd, 99/99), 58 daemons (law_midian the 58th); RUN (1259, 66, 52, 0, 12, 1505, 29, 311, the four pairs, 120);
the sweep 53/53 at 6,144 graded cells; EVERY GATE GREEN (the tape 10/10, the journal gate, the register gate --strict with DECLARED 103, the
daemon and dependency gates, census 187/187, cursor 6/6). The parser carries rule (28) THE RATIO "one of the N" (Fraction(1, N), the
denominator starred). UNCOMMITTED since a42f518: sittings 8 through 11b and THE CLOSE LINE — commit only on "commit push", staged by the
exclusion command in section 3.

THE CLOSE LINE (THE LOOP step 1's amendment, the owner: "I accept your recommendation"; THE_LOOP.md "Step 1's amendment — THE CLOSE LINE"
design + as-built): a ledger entry's close is its OWN journal line (run.close, the tenth log class, naming the entry by its write ordinal
`seq`); the write line is a SNAPSHOT at write time (the event's shared bound list kept by design); run_ledger joins the two; the journal gate
demands closed = closes. Three watches from it: a probe's first sink stands at a MARKER; after any engine change rerun the tape BEFORE the
cursor probes (a base the old engine wrote refuses the new replay); a design sentence that names a mutation of the past is a debt.

NEXT: CHAPTER 32 — GAD AND REUBEN'S READING (32:1-42) on the reading shape of section 5 (the measurement pass first; the Sifrei on Numbers
has NO row from 31:25 to 35:8 — Onkelos alone unless a piska is found by position; one ledger script with coverage computed, one manifest
script with checks cut from the store's bytes, one seat script, the ritual, the corpus rebaked, the stamp row), THEN its compile (12b) on the
compile shape of section 5 with the register gate at the gates step — NEVER THE NEXT READING FIRST. The forms for the walk's scripts are in
World/step9/forms_numbers_walk/ (copy to the scratchpad and adapt the paths — seq_record.py's recording path and seq_stitch.py's SPAN_ORDER
are this thread's; never run them from the forms folder). Before the reading: reread NUMBERS_WALK.md "Sitting 11 — MIDIAN" (the reading's
form) and "Sitting 11b — AS BUILT" (the compile's), THE_STEPS Step 2 + Step 5 + the compiler block, memory's STANDING LESSONS head.

## 10. ADDENDUM (2026-09-12, at sitting 12's close — the state doc's COMPACTION POINT #149; this supersedes section 9's NEXT, which is kept as written)

SITTING 12 DONE: CHAPTER 32 (Gad and Reuben) READ AND FROZEN — 207 units, standing 2124, hash 8b8fff1fa28953af unmoved; NUMBERS_WALK.md "Sitting 12" the
record (the shelf's silence proved by position and the three cross-citing rows credited; no divine frame in the chapter; the hinder-root the vows' verb;
the utterance rule's second seat 32:24 = 30:3 — 10b's filed seat found; the condition doubled twice, Kiddushin 3:4's exemplar; Onkelos's "before the
people of the LORD" at six martial seats, all of Onkelos Numbers'); COMPILE_DEBT.md's sitting-12 box (a)-(o) the compile's checklist. The engine, the
tape, the sweep (53/53 at 6,144) and every gate stand as at 11b's close. THE FORMS of sittings 11, 11b and 12 are now IN THE REPO —
World/step9/forms_numbers_walk/ (midian_*, gad_*, write_*_ledger.py, write_*_manifest.py, seat_*.py, *_chain.sh, seq_record.py, seq_stitch.py,
assert_driver.py): copy the latest to the scratchpad and adapt (the recording path and SPAN_ORDER are the thread's). Still UNCOMMITTED since a42f518
(106 paths); commit only on "commit push".

NEXT: SITTING 12b — THE COMPILE OF GAD AND REUBEN (32:1-42) on the compile shape of section 5, with the register gate at the gates step: the
measurements (the tape's state; the callees live — vows, shelach, chukat, census2, zelophehad, balak, bamidbar; the register gate's seats in the chapter),
THE DESIGN in NUMBERS_WALK.md before any code — THE STIPULATION'S LEDGER SHAPE (the two tribes' debit to cross armed, the possession entitled on the
condition, the negative arm's outcome a data row, the grant at 32:33 as transfers to three parties, the RELEASE at Joshua 22:1-9 a RUN OUTSIDE THE TORAH —
the entry open on the tape by design), the checkpoints CG1-CG9, THE PREDICTION'S ARITHMETIC; then the probes to FAIL, the docket by the union rule
(Kiddushin 3:4 + 61a-62a, Shekalim 3:2 + Yoma 38a, Bava Batra 117a-122a, Sotah 34b-35a, Sanhedrin 111a + the link rows), the types, the gates to FAIL,
the runner, the recorder, the stitcher, the literals, the tape, the probe gates, the daemon and dependency gates, the journal gate, THE REGISTER GATE
--strict, the sweep, the records — THEN CHAPTER 33 (the journeys' reading; the Sifrei silent to 35:8) — NEVER THE NEXT READING FIRST. Before the
compile: reread NUMBERS_WALK.md "Sitting 11b — AS BUILT" (the compile's form) and "Sitting 12" (the reading and the owed list), THE_STEPS Step 2 + Step 5
+ the compiler block, memory's STANDING LESSONS head, THE_LOOP.md "Step 1's amendment — THE CLOSE LINE".

## 11. ADDENDUM (2026-09-12, at sitting 12b's close — the state doc's COMPACTION POINT #151; this supersedes section 10's NEXT, which is kept as written)

SITTING 12b DONE: CHAPTER 32 (Gad and Reuben) COMPILED AND ON THE TAPE — NUMBERS 1:1-32:42 READ, FROZEN, COMPILED AND ON THE TAPE (27 by THE TENT); 54 runners
(cold_run_gad_reuben.py the 54th, 74/74), 59 daemons (law_gad_reuben the 59th, given_at 32:20, installed_by boot with the class named); RUN (1271, 66, 52, 0,
12, 1518, 30, 318, the four pairs, 121); the sweep 54/54 at 6218; EVERY GATE GREEN (the tape 10/10, the journal gate, the register gate --strict with nothing
to pay in the chapter, the daemon and dependency gates, every probe file). NUMBERS_WALK.md "Sitting 12b" (design + as-built) the record; COMPILE_DEBT.md's
sitting-12b box (i)-(viii) the owed items (the release at Joshua 22 outside the Torah — THE READBACK's; the jubilee's reach east; D2's class; Deuteronomy 3
and Joshua 1, 22; Caleb's stepfather; the Tanchuma; the display layer; Jair's lineages). THE FORMS of 12b are in World/step9/forms_numbers_walk/ (gad_compile_
recon.py, gad_compile_measure.py, gad_docket_scan.py, gad_docket_A-E.py, write_gad_docket.py, add_types_gad.py, gad_runner_measure.py, gad_part1-4.py — the
runner assembled by cat, patch_seq_literals_gad.py, gad_design.md, seq_record.py, seq_stitch.py). Still UNCOMMITTED since a42f518; commit only on "commit push".

NEXT: CHAPTER 33 — THE JOURNEYS' READING (33:1-56) on section 5's reading shape (the measurement pass first: the forty-two stations by the parser; the
Sifrei silent to 35:8 — found by position again, the whole export scanned for rows citing 33; Onkelos whole; one ledger script with coverage computed, one
manifest script with checks cut from the store's bytes, one seat script, the ritual, the corpus rebaked, the stamp row), THEN its compile (13b) on section
5's compile shape with the register gate at the gates step — NEVER THE NEXT READING FIRST. Before the reading: reread NUMBERS_WALK.md "Sitting 12" (the
reading's form) and "Sitting 12b — AS BUILT" (the compile's), THE_STEPS Step 2 + Step 5 + the compiler block, memory's STANDING LESSONS head.

## 12. ADDENDUM (2026-09-12, at sitting 13's close — the state doc's COMPACTION POINT #152; this supersedes section 11's NEXT, which is kept as written)

SITTING 13 DONE: CHAPTER 33 (the journeys) READ AND FROZEN — 208 units, standing 2136, hash 8b8fff1fa28953af unmoved; NUMBERS_WALK.md "Sitting 13" the record
(the shelf's silence proved by position and the cross-citing scan WIDENED to the English "Ibid." and the Hebrew gershayim after a first scan reported zero —
one row credited; the parser's five number verses every one read, 33:38's date (40, 5, 1) THE TAPE'S OWN MARKER at 20:28; the forty-two on the ink's own
verbs; the run of Exodus 12:12 recorded only at 33:4; Deuteronomy 10:6-7's order observed); COMPILE_DEBT.md's sitting-13 box (a)-(n) the compile's checklist.
The engine, the tape, the sweep (54/54 at 6218) and every gate stand as at 12b's close. THE FORMS of sitting 13 are in World/step9/forms_numbers_walk/
(jou_dump.py, jou_measure1.py, jou_measure2.py, jou_ink.py, jou_legs.py, jou_rows_onkelos_a.py / _b.py, write_jou_ledger.py, write_jou_manifest.py,
seat_jou.py, jou_chain.sh, write_jou_records.py, assert_driver.py): copy the latest to the scratchpad and adapt. Still UNCOMMITTED since a42f518; commit only
on "commit push".

NEXT: SITTING 13b — THE COMPILE OF THE JOURNEYS (33:1-56) on the compile shape of section 5, with the register gate at the gates step: the measurements (the
tape's state and its markers at the dated stations; the callees live — exodus_story, beha, shelach, chukat, balak, second_census, zelophehad, gad_reuben,
tochacha, holiness, the calf's runner; the register gate's seats in the chapter at 33:2 and 33:38), THE DESIGN in NUMBERS_WALK.md before any code — THE
STATIONS' SHAPE (a data list of forty-two places with their first tellings, or lines for the itinerary's own stations; a retelling never writes an act
twice), THE RUN OF EXODUS 12:12 closed by value at 33:4 if a debit stands open, THE DATE CHECKPOINT (33:38 against the marker; 33:39 against Exodus 7:7),
THE COMMAND'S DAEMON (given_at 33:50, installed_by the verse — the divine voice; the dispossession a debit OPEN BY DESIGN to Joshua's runs; the three
objects' bans; the lot by CALL; the negative arm as data), the checkpoints (the prefix grepped first), THE PREDICTION'S ARITHMETIC; then the probes to FAIL,
the docket by the union rule (Rosh Hashanah 2b-3a, Kiddushin 37b-38a, Megillah 22b, Zevachim 112b-119b, Bava Batra 117a-122a credited, the link rows), the
types, the gates to FAIL, the runner, the recorder, the stitcher, the literals, the tape, the probe gates, the daemon and dependency gates, the journal gate,
THE REGISTER GATE --strict, the sweep, the records — THEN CHAPTER 34 (the borders' reading, 34:1-29; the Sifrei silent to 35:8) — NEVER THE NEXT READING
FIRST. Before the compile: reread NUMBERS_WALK.md "Sitting 12b — AS BUILT" (the compile's form) and "Sitting 13" (the reading and the owed list), THE_STEPS
Step 2 + Step 5 + the compiler block, memory's STANDING LESSONS head, THE_LOOP.md "Step 1's amendment — THE CLOSE LINE".

## 13. ADDENDUM (2026-09-12, at sitting 13b's close — the state doc's COMPACTION POINT #154; this supersedes section 12's NEXT, which is kept as written)

SITTING 13b DONE: CHAPTER 33 (the journeys) COMPILED AND ON THE TAPE — NUMBERS 1:1-33:56 READ, FROZEN, COMPILED AND ON THE TAPE (27 by THE TENT); 55 runners
(cold_run_journeys.py the 55th, 53/53), 60 daemons (law_journeys the 60th, given_at 33:50, installed_by boot with the class named — the divine voice in the
plains of Moab); RUN (1274, 66, 52, 0, 12, 1522, 31, 318, the four pairs, 121); the sweep 55/55 at 6271; EVERY GATE GREEN (the tape 10/10, the journal gate,
the register gate --strict with nothing to pay, the daemon and dependency gates, every probe file, vocab_lint 0). NUMBERS_WALK.md "Sitting 13b" (design +
as-built) the record; COMPILE_DEBT.md's sitting-13b box (i)-(vii) the owed items (Leviticus 26:1-2's own compile — the figured stone's ban, the edge
OWED; the dispossession and the images OPEN to Joshua's runs — THE READBACK's; D2's class beside law_musafim's setting; Deuteronomy's seats; Joshua 5's
morrow and the manna's end; the two homographs; the display layer). THE DESIGN'S DECISION: THE FORTY-TWO STATIONS ARE A DATA ROW built from the DB, not
tape lines — a retelling never writes an act twice. THE FORMS of 13b are in World/step9/forms_numbers_walk/ (jou_compile_recon.py, jou_compile_measure.py,
jou_docket_scan.py, jou_docket_A-D.py, write_jou_docket.py, add_types_jou.py, jou_runner_measure.py, jou_part1-4.py — the runner assembled by cat,
patch_seq_literals_jou.py, jou_asbuilt.md, write_jou_compile_records.py, seq_record.py, seq_stitch.py). Still UNCOMMITTED since a42f518; commit only on
"commit push".

NEXT: CHAPTER 34 — THE BORDERS' READING (34:1-29) on section 5's reading shape (the measurement pass first: the parser on 34:13's nine and 34:15's two;
the Sifrei silent to 35:8 — found by position again, the whole export scanned for rows citing 34 with the "Ibid." and gershayim forms; Onkelos whole; one
ledger script with coverage computed, one manifest script with checks cut from the store's bytes, one seat script, the ritual, the corpus rebaked, the
stamp row), THEN its compile (14b) on section 5's compile shape with the register gate at the gates step (the Num 34 headers seat, the land's princes by
name, declared NONE — paid or held) — NEVER THE NEXT READING FIRST. Before the reading: reread NUMBERS_WALK.md "Sitting 13" (the reading's form) and
"Sitting 13b — AS BUILT" (the compile's), THE_STEPS Step 2 + Step 5 + the compiler block, memory's STANDING LESSONS head.

## 14. ADDENDUM (2026-09-12, at sitting 14's close — the state doc's COMPACTION POINT #155; this supersedes section 13's NEXT, which is kept as written)

SITTING 14 DONE: CHAPTER 34 (the borders) READ AND FROZEN — 209 units, standing 2149, hash 8b8fff1fa28953af unmoved; NUMBERS_WALK.md "Sitting 14" the record
(the shelf's silence proved by position — it ends at 35:9; the cross-citing scan in FOUR forms, the Hebrew "ibid." (the word "there" before the chapter
mark) the fourth; one row credited — 1:2, the one "command" without expense, the ink's five seats the row's five; the parser's three number verses every one
read, the distributive doubling as two ones; the border's own verb three Bible seats all here; the goings-out the Torah's five all here; Judah's south border
in Joshua 15 the land's; the spies walked the border's length; one tribe-noun; the intensive stem's three other seats Joshua's runs; Caleb's five words from
13:6; the roster's order matching no other; eight pointed comparisons met by NFC on both sides); COMPILE_DEBT.md's sitting-14 box (a)-(k) the compile's
checklist. The engine, the tape, the sweep (55/55 at 6271) and every gate stand as at 13b's close. THE FORMS of sitting 14 are in
World/step9/forms_numbers_walk/ (bor_dump.py, bor_measure1.py, bor_measure2.py, bor_ink.py, bor_legs.py, bor_rows_onkelos_a.py / _b.py,
write_bor_ledger.py, write_bor_manifest.py, seat_bor.py, bor_chain.sh, patch_overrides_bor.py, write_bor_records.py, assert_driver.py): copy the latest to the
scratchpad and adapt. Still UNCOMMITTED since a42f518; commit only on "commit push".

NEXT: SITTING 14b — THE COMPILE OF THE BORDERS (34:1-29) on the compile shape of section 5, with the register gate at the gates step: the measurements (the
tape's state; the callees live — second_census, gad_reuben, shelach, chukat, bamidbar, naso, korach, zelophehad, journeys, the erection runner, the sotah
runner; the register gate's Num 34 headers seat at 34:17 and 34:19), THE DESIGN in NUMBERS_WALK.md before any code — THE FOUR SIDES AS A DATA ROW of named
points with their kin seats (Joshua 15, Ezekiel 47) and the two Mount Hors, THE LOT by CALL into the second census's cell (VIA second_census), THE NINE AND A
HALF as a run citation of the Gad runner's grant on the tape (Joshua 14:2's receipt outside the Torah — THE READBACK's), THE COMMISSION's shape (a list-valued
line, no entity for a named party), the checkpoints (the prefix grepped first), THE PREDICTION'S ARITHMETIC; then the probes to FAIL (measured — likely
zero), the docket by the union rule (Gittin 8a, Kiddushin 36b-37a, Mishnah Sheviit 6:1 and 9:2, Bava Batra 117a-122a credited, Sanhedrin 16a, the link rows),
the types, the gates to FAIL, the runner, the recorder, the stitcher, the literals, the tape, the probe gates, the daemon and dependency gates, the journal
gate, THE REGISTER GATE --strict, the sweep, the records — THEN CHAPTER 35 (the refuge cities' reading, 35:1-34; THE SIFREI RETURNS at 35:9, piskaot
159-161 by position) — NEVER THE NEXT READING FIRST. Before the compile: reread NUMBERS_WALK.md "Sitting 13b — AS BUILT" (the compile's form) and "Sitting
14" (the reading and the owed list), THE_STEPS Step 2 + Step 5 + the compiler block, memory's STANDING LESSONS head, THE_LOOP.md "Step 1's amendment — THE
CLOSE LINE".

## 15. ADDENDUM (2026-09-13, at sitting 14b's close — the state doc's COMPACTION POINT #157; this supersedes section 14's NEXT, which is kept as written)

SITTING 14b DONE: CHAPTER 34 (the borders) COMPILED AND ON THE TAPE — NUMBERS 1:1-34:29 READ, FROZEN, COMPILED AND ON THE TAPE (27 by THE TENT); 56 runners
(cold_run_borders.py the 56th, 56/56), 61 daemons (law_borders the 61st, given_at 34:1, installed_by boot with the class named — a law in the divine voice
relayed at 34:13 in 36:5's form, D2's question); RUN (1277, 66, 52, 0, 12, 1525, 32, 318, the four pairs, 121); the sweep 56/56 at 6327; EVERY GATE GREEN
(the tape 10/10, the journal gate with population 148 = rows 148, the register gate --strict with THE NUM 34 SEAT PAID BY ROWS and its declaration
deleted, the daemon and dependency gates, every probe file, vocab_lint 0). NUMBERS_WALK.md "Sitting 14b" (design + as-built) the record; COMPILE_DEBT.md's
sitting-14b box (i)-(viii) the owed items (the dividers' debit OPEN to Joshua 14:1, 17:14, 19:51 — THE READBACK's; the relay's form D2's; Numbers 27:12-23
uncompiled met again; Deuteronomy's and Joshua's seats; the shelf's own border lines as DATA; the homographs filed; the display layer). THE DESIGN'S FOUR
DECISIONS: the four sides ONE STATUS ON THE LAND (a DATA row, nothing on the people); the lot by CALL; THE RESTATEMENT WRITES NOTHING (a run citation of
the grant on the tape); the dividers a status and a debit on the standing party of 32:28 AND TWELVE NAMED ROWS in the population table — the first register
paid by rows since the table was built at 26. THE FORMS of 14b are in World/step9/forms_numbers_walk/ (bor_compile_recon.py, bor_compile_measure.py,
bor_docket_scan.py, bor_docket_A-D.py, write_bor_docket.py, add_types_bor.py, bor_runner_measure.py, bor_part1-4.py — the runner assembled by cat,
patch_seq_literals_bor.py, bor_design.md, bor_asbuilt.md, write_bor_compile_records.py, seq_record.py, seq_stitch.py). Still UNCOMMITTED since a42f518;
commit only on "commit push".

NEXT: CHAPTER 35 — THE REFUGE CITIES' READING (35:1-34) on section 5's reading shape (the measurement pass first: the parser on 35:4-5's cubits — 4b's
owed line — and the cities' counts at 35:6-7 and 35:14; THE SIFREI RETURNS at 35:9, piskaot 159-161 by position with the heads checked against the rows'
own citations, the export scanned in the four citation forms for rows on 35:1-8; Onkelos whole; one ledger script with coverage computed, one manifest
script with checks cut from the store's bytes, one seat script, the ritual, the corpus rebaked, the stamp row), THEN its compile (15b) on section 5's
compile shape with the register gate at the gates step (the chapter's count lines declared at the reading, paid or held at the compile) — NEVER THE NEXT
READING FIRST. Before the reading: reread NUMBERS_WALK.md "Sitting 14" (the reading's form) and "Sitting 14b — AS BUILT" (the compile's), THE_STEPS Step 2
+ Step 5 + the compiler block, memory's STANDING LESSONS head.

## 16. ADDENDUM (2026-09-13, at sitting 15's close — the state doc's COMPACTION POINT #158; this supersedes section 15's NEXT, which is kept as written)

SITTING 15 DONE: CHAPTER 35 (the refuge cities) READ AND FROZEN — THE WALK'S LAST READING IN NUMBERS (36 frozen at THE TENT) — 210 units, standing 2163,
hash 8b8fff1fa28953af unmoved; NUMBERS_WALK.md "Sitting 15" the record (THE SIFREI RETURNS at 35:9 — piskaot 159-161 by position, sixteen rows at the
English file's grain each read in both files; the Hebrew file DUPLICATES A BLOCK (160:11-14 = 161:1-4), the English 160:5 is not the Hebrew 160:5, "thirty"
for twenty-three, the rule "we do not punish by inference" dropped a second time, the citations and the colophon; two rows of piska 1 credited; the parser's
seven number verses read and ONE GAP — THE BARE DUAL THOUSAND at 35:5, the class named for the compile; the four sides in the camp's order; the measure-verb's
three Torah seats; the refuge-word never Deuteronomy's; Joshua 21 summing the forty-eight; "shall surely die" five times; the murder-root twenty, one root
for four agents; the high priest defective only here; "he has no blood" the burglar's; the sixth and the ninth commandments' verbs in one verse; the
ransom's root three times; the pollute-root's only Torah seat; the book's inclusio 5:3 / 35:34; eleven MIDDOT entries; the display layer's 152 rows);
COMPILE_DEBT.md's sitting-15 box (a)-(m) the compile's checklist. The engine, the tape, the sweep (56/56 at 6327) and every gate stand as at 14b's close.
THE FORMS of sitting 15 are in World/step9/forms_numbers_walk/ (ref_dump.py, ref_measure1.py, ref_measure2.py, ref_ink.py, ref_rows_onkelos_a.py / _b.py,
ref_rows_sifrei.py, write_ref_ledger.py, write_ref_manifest.py, seat_ref.py, ref_chain.sh, patch_overrides_ref.py, write_ref_records.py,
assert_driver.py — the reading shape WITH the Sifrei block): copy the latest to the scratchpad and adapt. Still UNCOMMITTED since a42f518; commit only on
"commit push". The loop question (a resident world against the replayed journal) stays under discussion with the main thread — nothing on the walk moves
until Brian's word.

NEXT: SITTING 15b — THE COMPILE OF THE REFUGE CITIES (35:1-34) on the compile shape of section 5, with the register gate at the gates step: the
measurements (the tape's state; the callees live — exodus (the burglar's blood, the place to flee), lev24, shelach, vayikra5, naso, second_census,
journeys, borders, zelophehad, gad_reuben, chukat (the priesthood's holder), the primeval runner; the register gate with nothing to pay), THE DESIGN in
NUMBERS_WALK.md before any code — THE BARE DUAL THOUSAND's probes to FAIL (35:5 ×4, Joshua 3:4, 7:3, Judges 20:45, 1 Samuel 13:2, 1 Kings 7:26, 2 Kings
18:23, Isaiah 36:8; the plural unmoved; the corpus diff read), THE LEVITE CITIES' TABLE (48 = 6 + 42; the measures as DATA with the exam's settings; the
proportional rule by CALL; Joshua 21 outside the Torah — THE READBACK's), THE SIX CITIES as a DATA row and the appointment a debit OPEN BY DESIGN to Joshua
20, THE MURDERER'S AND THE MANSLAYER'S CASE TABLE (the size clause a PARAMETER; the verdicts and the effects — exiled, put to death, the burglar's
has_blood reused; the court of twenty-three as DATA), THE TERM as a TIMER on the high priest's office (Eleazar's death outside the Torah — OPEN by design),
the border case, THE WITNESSES (two by the prototype), NO RANSOM against the ox's cell by CALL, THE LAND (a status; "in whose midst I dwell" by REFERENCE to
5:3), the checkpoints (the prefix grepped first), THE PREDICTION'S ARITHMETIC; then the probes to FAIL, the docket by the union rule (Makkot 2:1-8 with
7a-13a, Sanhedrin 1:4 with 2a-b, 9:1-2 with 76b-79a, 3:4 with 27b, 45b, Bava Kamma 4:5 with 40a-41a, Ketubot 37b, Eruvin 4:3 and 5:1-5 with 51a, Sotah 27b
and 9:7, Arakhin 9:8 with 33b, Shevuot 4:1, Yoma 23a, Megillah 29a, Yevamot 46b, the link rows), the types, the gates to FAIL, the runner, the recorder,
the stitcher, the literals, the tape, the probe gates, the daemon and dependency gates, the journal gate, THE REGISTER GATE --strict, the sweep, the
records — AND WITH IT NUMBERS CLOSES (1:1-36:13 read, frozen, compiled and on the tape; 27 and 36 by THE TENT): the next book on the owner's word. Before
the compile: reread NUMBERS_WALK.md "Sitting 14b — AS BUILT" (the compile's form) and "Sitting 15" (the reading and the owed list), THE_STEPS Step 2 +
Step 5 + the compiler block, memory's STANDING LESSONS head, THE_LOOP.md "Step 1's amendment — THE CLOSE LINE".

## 17. ADDENDUM (2026-09-13, at sitting 15b's close — the state doc's COMPACTION POINT #160; this supersedes section 16's NEXT, which is kept as written)

SITTING 15b DONE: CHAPTER 35 (the refuge cities) COMPILED AND ON THE TAPE — NUMBERS 1:1-36:13 READ, FROZEN, COMPILED AND ON THE TAPE (27 and 36 by THE TENT):
NUMBERS IS CLOSED. 57 runners (cold_run_refuge.py the 57th, 51/51), 62 daemons (law_refuge the 62nd, given_at 35:1, installed_by boot with the class named —
the divine voice in the plains of Moab); RUN (1279, 66, 52, 0, 12, 1527, 33, 318, the four pairs, 121); the sweep 57/57 at 6378; EVERY GATE GREEN (the tape
10/10 first run, the journal gate with population 148 = rows 148, the register gate --strict with nothing to pay and its tilde test taught, the daemon and
dependency gates after one honest fire each read and repaired at the runner and the yaml, every probe file, vocab_lint 0). NUMBERS_WALK.md "Sitting 15b"
(design + as-built) the record; COMPILE_DEBT.md's sitting-15b box (i)-(ix) the owed items (the two debits OPEN to Joshua 20-21 and Deuteronomy 4:41 — THE
READBACK's; the term's closer Joshua 24:33 outside the Torah; the thousand thousands R73; Deuteronomy's seats; the size that can kill a parameter; the
twenty-three as DATA; the rent and the sojourner's exile; the display layer; the register gate's tilde). THE DESIGN'S DECISIONS: RULE 29 THE BARE DUAL
THOUSAND (the sheva under the lamed); the Levite cities ONE debit + DATA (the four sides THE CAMP'S ORDER); the six cities DATA + ONE debit; the case table
from the tokens (the size a PARAMETER); THE TERM AN EVENT-KEYED OPEN ENTRY closed by the death act — NOT a timer; the border's no-blood reused; the
witnesses by the prototype; no ransom by the live call; the land polluted a STATUS on the land; the inclusio 5:3 / 35:34 READ. THE FORMS of 15b are in
World/step9/forms_numbers_walk/ (ref_compile_recon.py, ref_runner_measure.py, ref_docket_scan.py, ref_compile_measure.py, ref_design.md, patch_probes_ref.py,
ref_parser_diff.py, ref_docket_A-H.py, write_ref_docket.py, add_types_ref.py, ref_part1-4.py — the runner assembled by cat, patch_seq_literals_ref.py,
ref_asbuilt.md, write_ref_compile_records.py, seq_record.py, seq_stitch.py). Still UNCOMMITTED since a42f518; commit only on "commit push".

NEXT on the owner's word: THE NEXT BOOK — nothing opens before the word. When it comes, the walk's shape holds: READ THEN COMPILE PER PORTION at the
parashah grain; the reading shape and the compile shape in section 5 (the forms the ref_* set); the spine Sifrei Devarim (memory spine-default) with
Onkelos whole; the register gate at every compile sitting's gates step; the owed forward seats filed across Numbers' walk (Deuteronomy 4:41-43, 19:1-13,
21:1-9, 17:6 and 19:15, 25:2, 12:1-2, 4:42) met at their chapters; THE READBACK (step 6) its own design when Joshua's runs are reached. Before the first
sitting: reread NUMBERS_WALK.md "Sitting 15" (the reading's form) and "Sitting 15b — AS BUILT" (the compile's), THE_STEPS Step 2 + Step 5 + the compiler
block, memory's STANDING LESSONS head.

## 18. ADDENDUM (2026-09-13, THE PROJECT REVIEW — reviews/REVIEW_project_2026-09-13.md; the owner walking its findings one at a time)

TWO RULES OF SECTION 3 CHANGED ON THE OWNER'S WORD: (a) "Ok add them" — THE NEVER-COMMIT SET is in .gitignore now as well as in the
staging command (two doors; a path added to the set goes into both); (b) "Let's add it to all commits going forward" — ARCHITECTURE/ RIDES
EVERY COMMIT. THE STAGING FORM IS NOW: `cd <repo-old> && git add -A -- . ':!logic/gork' ':!grok-mockups' ':!open_ledger'
':!DISPOSABLE_scan' ':!Data/discord_backup_codes.txt' ':!cases_pilot.yaml' ':!elijah_docket'` — the `':!ARCHITECTURE'` exclusion is GONE.
The design thread still writes there; the main thread still edits there only on the owner's word. Section 3's lint-baseline sentence
"everything else 0" is also FALSE for thirteen files (the review's finding 3: cold_run_temurah.py 11, cold_run_moadim.py 7,
cold_run_minchah.py 5, cold_run_yovel.py 2, cold_run_tzav.py 2, cold_run_pesach_sheni.py 1, cold_run_mekoshesh.py 1, dependency_census.py 8,
daemon_census.py 1, DEPENDENCY_INDEX.md 8 (gate-written), EXAM_LEDGER.md 7, REPORT_CANON_HUNT.md 8, REPORT_FESTIVALS.md 2, CORE_SHELF.md 1);
every NAMED baseline holds. Commit still ONLY on "commit push"; sittings 8-15b, the ARCHITECTURE work and the review are uncommitted since a42f518.

THE STAGING FORM, FINAL (2026-09-13, finding 7; the owner: "Keep them tracks and narrow"): DISPOSABLE_scan's twenty tracked .md files ride like
any other file; only its zips stay out. AND A GIT FACT MEASURED: once a path is in .gitignore, naming it in the staging command's exclusions makes
`git add` print "The following paths are ignored" and EXIT 1 (the adds still happen, but a `&&` chain stops) — so the exclusions of ignored paths
are DROPPED and the ignore list alone holds them. THE FORM: `cd <repo-old> && git add -A -- . ':!elijah_docket'
':!DISPOSABLE_scan/*.zip'` (dry-run 2026-09-13: exit 0, 667 adds, none of the set, none of the gitlink, ARCHITECTURE's 32 files aboard).
The two doors for the zips (ignored AND excluded), one door for the rest (ignored), the gitlink by exclusion only (a gitlink cannot be ignored).

LINT BASELINES MOVED AT THE REVIEW (2026-09-13): memory step9-exam-era.md 0 (was 7), MEMORY.md 4 (was 5 — the four are the index's own
"- [Title](file.md)" links whose hyphenated file names sit right before ".md", unpayable under the window's period rule); the seven pre-walk
runners, dependency_census.py, daemon_census.py and DEPENDENCY_INDEX.md now 0 (finding 13's code side); the state doc stays 147.

A RULING AT THE REVIEW (2026-09-14, the owner: "ok first one go"): A GLOSS IS DISPLAY, NOT CONTENT — an English gloss beside a Hebrew word
in a ledger may be edited IN PLACE (the one exception to LEDGERS ARE APPEND-ONLY); the 49 older reading ledgers and four reports were brought to
0 flags that way (forms: flag_places.py, patch_gloss_ledgers.py). The gloss backlog left in the current era: logic/py_units (~350 dictionary
words, its own sitting) and MEMORY.md's four file-name links.

## 19. THE LIVING DATABASE AND THE LOOP THAT WAITS — the discussion of 2026-09-14 (NO RULING YET; the owner: "we really need to get this done right. make sure you record")

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

## 20. ADDENDUM (2026-09-14, THE LOOP STEP 7 (a) WRITE AS YOU GO — the owner: "ok go 1" on section 19's recommendation; the state doc's COMPACTION POINT #171)

BUILT: THE_LOOP.md "Step 7 THE LOOP THAT WAITS — part (a) WRITE AS YOU GO: the design" + "As built" (the table's row 7; the box's part (a)
ticked). D14 THE SEAL: a journal line is sealed at the end of its BLOCK (the engine's outermost call returning — world_engine._sealed on the six
entry points submit / marker / advance / close / row / cancel_timers) and never changes after; written to <segment>.live and INSERTed into
World/journal/data/world.sqlite in the same act (a commit per block); the run's seal writes the header + the same bytes and removes the body;
THE AUDIT at every seal and in --gate (the chain; lines = the log; an independent conversion equal on every field but the bound's right edge,
its count printed; the rebuilt index = the live rows). The bound's right edge is written as it stood at the seal — the next forward marker
line's day is the derived fact (the debt THE CLOSE LINE named, paid; the base segments' bytes changed once, 2,673 lines of the running world;
the engine's in-memory bound list still closes — the checkpoints read it). MEASURED FIRST: fired_by moves inside the block (1,140 lines), the
bound's right edge after it (EVENT 1,195 / WRITE 1,391 / TIMER-SET 50 / TIMER-FIRE 37); MARKER, CLOSE, ROW, RETRO-WRITE never; 26 fires and
their writes inside a later marker's walk carry a bound already closed; the import 81.8 s of a 93 s run, the running world's own run 0.8 s.
THE CODE: world_engine.py (functools; World.journal; the decorator), World/journal/worldledger.py (row_of — the index's row has one home),
world_journal.py (LiveSink, attach, ensure_index, rows_of, l3_sources, verify_body, audit, live_report; sink() kept — a live sink seals, the
cursor's in-memory sink writes its sealed lines, a world with no sink takes THE LATE SEAL and says so; cursor_segment's audit from the
in-memory sink; the gate's live-rows check), cold_run_sequence.py (attach in run_world / run_to (memory_only) / rest_world; the closing reindex
retired for live_report; --reindex by hand). THE FORMS: World/step9/forms_numbers_walk/loop_2026-09-14/ (loop_measure_mutation.py,
patch_live_sink.py, write_loop_records.py). THE PRINTS: live_probes.py 0/7 → 7/7; journal 7/7, view 6/6, installation 6/6, population 9/9,
sequence 4/4, clock 22/22; the tape 10/10 (98 s; the seals LIVE — the running world 3,362 lines in 1,533 blocks with 2,673 right edges closed
after, descent_literal 3,362 / 1,533 / 2,673, covenant_pieces 3,362 / 1,533 / 2,639, THE REST 3,358 / 1,531 / 2,673; the live index 20,049
rows, every source current); cursor 6/6 on the new base; the daemon gate 62 daemons / 427 WRAPPED / open aliases 3; the dependency gate
455 / 48 / 9 / 143 of 482 + 173; THE JOURNAL GATE GREEN — four segments byte-identical across two processes, chains VERIFIED; THE LIVE INDEX line new: 4 sources, 13,444 rows written line by line at their blocks, the two processes' rows IDENTICAL, the rebuilt index EQUALS the live rows; the running world's counts MATCH the RUN tuple; the five views MATCH on every source (ledger 1,539 = writes; timers 66 = sets, fired 52, pending 14; clock 157; docket 4; population 148; closed 121 = closes); the sweep 57/57 runners green, 6,378 graded cells (unchanged from 15b's close; the dependency gate 251 required edges / 174 pointers, 338 live import edges, 482 + 173 on file; the daemon gate 62 daemons, 427 WRAPPED, open aliases 3). LINTS: the engine, the journal, worldledger, live_probes, THE_LOOP 0; cold_run_sequence.py 7 (baseline); every
record at its baseline. NEW WATCHES (memory's STANDING LESSONS head): a payload moves after the log — three snapshots before an early write;
a count derived from a measurement is retyped from the instrument's print; a world that ran with no sink takes the late seal — attach before
the first block; a .live body file beside a segment means a run in progress or one that died mid-run; after any engine change rerun the tape
before cursor_probes.

NEXT on the owner's word: (b) THE STEPPER — the design section in THE_LOOP.md first (the pause at the flush seam; one process, the import
81.8 s its fixed price; what a pause shows — the five views, the entities, the installed laws, the checkpoints; the cursor's own appended lines
live), the probes to FAIL, then the code; then (c) THE PORT. The four calls of section 19 ride as recommended (the three in order; the event —
the block — the grain; the five views now, the rest owed to (b); before Deuteronomy), each open to the owner's overruling. Still UNCOMMITTED
since a42f518; commit only on "commit push" with the staging form of section 18.

## 21. ADDENDUM (2026-09-14, THE LOOP STEP 7 (b) THE STEPPER — the owner: "ok go b"; the state doc's COMPACTION POINT #172)

BUILT: THE_LOOP.md "Step 7 THE LOOP THAT WAITS — part (b) THE STEPPER: the design" + "As built" (the box's part (b) ticked; (c) THE PORT the
one left). D15 THE TAPE AS A GENERATOR: World/step9/world_stepper.py transforms the stitched tape at load (every engine-call line prefixed
with `yield (verse, ordinal); ` — one call per line asserted, 1,507 on today's tape) and runs it as a generator: each next() runs one tape
line and yields the NEXT call's verse before running it — the pause between two lines, the left edge of a verse exact, the tape resumable.
No engine, journal, registry or runner file moved (two new files: the stepper and step_probes.py). THE SESSION journals under its own source
cold_run_sequence/stepper (the base untouched); a partial session seals a partial segment; THE REPLAY IS THE AUDIT at every call (a sealed
line differing from the base's at the same ordinal REFUSES the session there). GRAINS: call | verse | chapter | marker | day | a verse
address (--to stops at a left edge). THE REPORT at every pause: the lines run and sealed, the next verse, the clock (the day, the creation
date, the exodus date), the entities, the open entries, the pending timers, audited yes/no; --show open | ledger <entity> | custody |
timers reads the rows FROM THE DATABASE under the session's source; --pause waits for Enter (a control word, never a data event).
MEASURED FIRST: 1,507 calls on 1,507 lines (1,279 submits, 157 markers, 71 closes; 0 multi-line calls); THE CHECKPOINTS ARE NOT ON THE TAPE
(computed in run() after it from M — "as they fall" owed to the stitcher); the 1,533 blocks of (a) = 1,507 lines + 26 walks with fires; the
import 81.8 s the session's fixed price; a thread considered and refused (it cannot stop before a line). THE PRINTS: step_probes.py 0/8 →
8/8, then S9 added after the first real session's miss (32 double-quoted sources read as no verse; the patterns read either quote now) →
9/9; SESSION A `--from 'Num 27:1' --to 'Num 28:1' --by verse`: the replay 3,221 lines (the cursor's fork), three steps by verse (27:1 with
27:1-4, 3 lines; 27:5, the court's custody row shown; 27:6-11, the row gone), stopped at the left edge of 28:1, a partial segment of 3,229
lines in 1,495 blocks, audited; SESSION B `--by marker --quiet`: 158
steps, 3,362 lines, the body IDENTICAL to the base (chain head 5c482e02f82ea462); the tape 10/10 after with the session a fifth source
(23,411 rows after session B; after session A's rerun the stepper source 3,229 rows = 3,229 lines MATCH, 23,278 rows, every source
current); live 7/7, journal 7/7, cursor 6/6. THE FORMS: forms_numbers_walk/loop_2026-09-14/ (loop_design_b.md,
loop_sessions.sh, write_stepper_records.py). LINTS: world_stepper.py 0, step_probes.py 0, every record at its baseline. THE GATES: unchanged
files — the daemon, dependency and journal gates and the sweep stand as at (a)'s close.

NEXT on the owner's word: (c) THE PORT — the design section in THE_LOOP.md first (the queue the loop reads at the pause; the text the first
producer; a later pass under its own run name; every input through World.submit alone — the one door; the registry refuses an unregistered
kind; what a queued input looks like and where it lives — primary in git or derived; the stepper's pause the seam), the probes to FAIL, then
the code. Still UNCOMMITTED since a42f518; commit only on "commit push" with the staging form of section 18.

COMMITTED 08fa06e (2026-09-14, the owner: "commit push"; 821 files, everything since a42f518 — sittings 8-15b, the ARCHITECTURE folder, the review, the gloss patches, THE LOOP's step 7 (a) and (b); pushed to Josephtorah/Torah_Grok main). ⚠ THE PUSH LESSON: the GitHub tool is /opt/homebrew/bin/gh, not /usr/bin/gh — a wrong path skips the account switch silently and the push fails on credentials; the form is `GH=/opt/homebrew/bin/gh; $GH auth switch --user Josephtorah; git push origin main; $GH auth switch --user PeerloopLLC` (a fetch under PeerloopLLC fails — that account has no credentials on the owner's repo; the push's own line is the confirmation). Section 3's push line stands corrected by this.

## 22. ADDENDUM (2026-09-14, THE LOOP STEP 7 (c) THE PORT — the owner: "ok go c. keep up with what we need to do to finish this. go"; the state doc's COMPACTION POINT #173). THE LOOP THAT WAITS IS BUILT.

BUILT: THE_LOOP.md "Step 7 THE LOOP THAT WAITS — part (c) THE PORT: the design" + "As built" + "TO FINISH THE LOOP — THE LIST" (the box's (c)
ticked). D16 THE PORT IS A QUEUE, NEVER A PROMPT: World/journal/port/<queue>.yaml (tracked, primary) — `items:` {id, at, label, event{kind,
subject, case_source, the fields}}, read ONCE at open and validated (an unregistered kind, an unknown field, a bad position, a position already
passed by a session starting later: REFUSED, named; a missing registered field a WARNING — the registry's field list is a census, not a
contract); at every pause the items due enter in file order through World.submit — the one door — the EVENT line prov.unit 'port:<queue>' and
data.port {queue, id, label}; the queue file never rewritten. D17 A WORLD WITH INPUTS IS ITS OWN WORLD: the session journals whole under
cold_run_sequence/port@<queue>, audited against the base to the first input, THE FORK recorded (ordinal + item; the header {base, fork,
forked_by, queue, pending}); the base untouched; D9's appended form stays the cursor's. D18 THE ORDER OF A PAUSE: the queue first, then the
text's line; an unpositioned item at the first pause (the session's start or the left edge of --from); a positioned one at its verse's left
edge; one past the tape's end at the end, before the seal. THE CODE: World/step9/world_port.py (Port: load, validate, due, event_of, pending);
world_stepper.py (Stepper(queue=…), _enter() at every pause and at the end, the audit stopping at the fork, the report's inputs / fork /
forked_by, the header at close, --queue, the session's own source in the prints); world_journal._append_log's EVENT branch ('port:<queue>');
worldledger.Segment.write (the header's extra fields whenever given). No engine change. THE PRINTS: port_probes.py 0/9 → 8/9 → 9/9 (P5's
hand-typed index corrected on the engine's order: the fire's lines precede the marker's own line); step 9/9, live 7/7, journal 7/7, cursor
6/6; THE REAL SESSION `--from 'Num 27:1' --to 'Num 28:1' --by verse --queue World/journal/port/daughters.yaml --show custody`: 2 items at
Num 27:5, no warnings; the replay 3,221 audited; step 1 (27:1 with 27:1-4) audited; step 2 at the left edge of 27:5 — THE TWO INPUTS FIRST
(first_horn → holding_owed on the daughters at Num 27:8, seq 3226; second_horn → exempt = child_of_any_kind on the widow at Deut 25:5, seq 3228;
both law_zelophehad), then the text's 27:5 line (the custody, seq 3230), FORKED AT 3225 BY first_horn; step 3 (27:6-11) the custody closed;
stopped at the left edge of 28:1; sealed 3,233 lines in 1,497 blocks, the audit ok; the header {base, fork 3225, forked_by first_horn, queue
daughters, pending []}; askable under --world cold_run_sequence/port@daughters. THE TAPE AFTER: green by the runner's own exit (the live report prints only after the grade passes) — the live report 26,511 rows: the port's world cold_run_sequence/port@daughters 3,233 rows = 3,233 lines MATCH beside the four worlds (3,362 / 3,362 / 3,358 / 3,362), the stepper's session (3,229) and the cursor's segment (4), every source current. A FINDING: the second horn's citation
(Deut 25:5) moved the engine's VERSE REACHED to Deuteronomy inside Numbers 27 — an input's citation moves the position the installation gate
reads; the port's position or the input's citation: the owner's, inside the inputs' definition (list item 7). LINTS 0 on every new and
changed file; every record at its baseline. THE FORMS: forms_numbers_walk/loop_2026-09-14/ (loop_design_c.md, write_port_records.py).

⚠ A STANDING DUTY FROM THIS SITTING: THE_LOOP.md "TO FINISH THE LOOP — THE LIST" is brought current at every loop sitting and echoed in the
reply at its close. THE LIST NOW (twelve): the owner's — 1 the inputs themselves, 6 time without a marker, 7 the position of an input; after
Deuteronomy — 2 the second pass (D2), 3 step 6 the readback (D12); sittings — 4 D7's merge, 5 the checkpoints as they fall (the stitcher);
small — 8 the cursor's lines live (the cursor may retire into the stepper), 12 the other worlds stepped; the design thread's — 9 the window
(CHRONICLE); later — 10 the interface, 11 a graded input. NEXT on the owner's word: one of the list's items (his three decisions first), or
THE NEXT BOOK (Deuteronomy, as #160), or the py_units gloss sitting. UNCOMMITTED since 08fa06e: this sitting's files and the post-commit notes;
commit only on "commit push" with the staging form of section 18 (the GitHub tool at /opt/homebrew/bin/gh).

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
jacob`: yaaqov from Gen.25.26, yisrael from Gen.35.10; THE GATE: GREEN — the four segments byte-identical across two processes, chains verified; the live index 13,444 rows identical between the processes and equal to the rebuild; the five run views MATCH on every source; THE FOLD LAYER's new line: units 210, facts 1,809, demands 341, events 557, names 81, standing 2,163, open demands 191 and the state hash 8b8fff1fa28953af each MATCH the pinned truth, 12 kinds and 9,574 rows in the index MATCHING the header; THE PROBES AFTER: journal 7/7, live 7/7, step 9/9, port 9/9, cursor 6/6 after the journal module's change. LINTS 0 on every changed file; every record at its
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

COMMITTED 376d304 (2026-09-14, the owner: "commit push"; 33 files, everything since 08fa06e — step 7 (c) the port, the interface's shape and four mockups, D7's merge, the freeze-time rebuild in the steps; pushed to Josephtorah/Torah_Grok main as a42f518 → 08fa06e → 376d304).

## 24. ADDENDUM (2026-09-14, at the owner's compaction after D7's merge — the state doc's COMPACTION POINT #175; "Make sure you save all of these decisions so we can continue")

THE DECISIONS SAVED: the board — "lets refine the mockup first. I like it we are close" (THE BOARD mockup refined on the owner's notes, then the
page over the one database); the checkpoints in the tape — "Yes, after the board"; the cursor's lines live and the other worlds stepped —
"Both, when a sitting has room". THE ORDER: the mockup refined on his notes → the board page → the checkpoints → DEUTERONOMY. D2's label
corrected on his "note it" (the boot setting the engine's baseline without a teacher; from_event the tradition's own rule; the decision
stands). COMMITTED 376d304 and pushed. THE FORMS of the board: World/step9/forms_numbers_walk/loop_2026-09-14/board_mockup.py (the generator —
refine it, never the HTML; it reads the journal's rows and the reading's births from the one database) → mockup_board.html; the artifact
"The Board of Things" (republish to the same URL from the same file path). THE FIRST SITTING AFTER COMPACTION: #175's rereads, then the
owner's notes on the board.
HIS FIRST NOTE (2026-09-14, after the compaction): "put a small screen to the left, in it place the box that was created in the right as a stepper. the heavens box, then the earth box below it, then light below. The left box will scroll from bottom up as more boxes are added. When I click on any box it will bring me back to that step in the process." — VERSION 3 DRAWN on "yes do it": the left screen (a strip of every tile in
creation order, newest at the bottom, auto-scrolled; a click replays the rows to that step; the tiles ahead dimmed, the click walks both ways);
the births from the entities view (the retired rows gone). HIS SECOND NOTE: "on the top right wher you have next, put a back button there. also when a new box is created make the browser display the first created box in the middle of the broswer screen" — VERSION 4: Back beside Next; the first tile created
in a step scrolled to mid-screen. HIS THIRD NOTE (the river out of Eden hidden above the fold at step 18, eight births at once): VERSION 5 — the
topmost new tile on the board at the top of the screen under the header, the rest below; verified in Chrome by the browser tools. The generator's
docstring carries the notes verbatim. HIS FOURTH NOTE: VERSION 6 — every group a window exactly three rows tall, scrolling inside itself past
three rows (amends 'no panes scrolling inside' on his word); verified in Chrome. NEXT: his next note, or his word for the page.

## 25. ADDENDUM (2026-09-14, THE BOARD BUILT — the owner: "lets build it" after six versions of the mockup on his notes; the state doc's COMPACTION POINT #176)

THE BOARD IS REAL (World/step9/THE_LOOP.md "THE BOARD — item 10's build: the design" + "as built"; decisions D22-D26): World/step9/
world_board.py — a small local server over the one database, READ-ONLY, three routes and the page (D22); the births = the entities view's
first mention per entity in the text's own order, placed before the first marker or event row at or after their verse and only when the
text reaches them (D23); every name English — the registry's `en` (a dash-note trimmed), then World/step9/board_names.yaml (162 display
names for the units' tokens; the_earth beside the heavens), then a runner's own dashed id; an underscored token without a name REFUSED by
the gate (D24); the page follows and the controls replay (D25); the stepper's --pace S runs with no keyboard (D26). board_probes.py 0/8 →
8/8 (B2 corrected twice on the data's order: God first at 1:1, light eighth after the four of 1:2); world_board.py --gate GREEN. THE RUN:
150 paced steps by verse to Genesis 12:20 (392 lines, 70 entities, 15 open, day 738,887, audited) watched forming in Chrome by the tools;
the first live run's two flaws (reset by count blind to a session outrunning the old count; the mockup's leftover births on a sealed
board) fixed and probed the same hour. HOW TO WATCH: `python3 World/step9/world_board.py` in one window, `python3 World/step9/
world_stepper.py --by verse --pace 1` in another, http://127.0.0.1:8765/ in Chrome (`?source=` for another world) [SUPERSEDED 2026-09-15 — section 30: the engine runs `--board` and the page drives it]. THE LIST: item 10
built; ten open (the owner's three; the second pass and the readback after Deuteronomy; the checkpoints; the cursor's lines and the other
worlds when a sitting has room; the graded input; the design thread's window). THE ORDER NOW: the owner's notes on the real board as they
come → the checkpoints in the tape ("Yes, after the board") → DEUTERONOMY. THE GATES AT THE CLOSE: step_probes 9/9, port_probes 9/9, the journal gate GREEN (hash 8b8fff1fa28953af), the board's gate GREEN, board_probes 8/8. Uncommitted since 376d304:
everything of this sitting and the six mockup versions; commit only on "commit push".

## 26. ADDENDUM (2026-09-14, THE CHECKPOINTS AS THEY FALL — the owner: "Ok do it" after "What is checkpoints"; item 5 of THE LIST; the state doc's COMPACTION POINT #177)

ITEM 5 BUILT (World/step9/THE_LOOP.md "THE CHECKPOINTS AS THEY FALL — item 5's build: the design" + "as built"; decisions D27-D30): the
tape's checkpoint block (416 statements, 193 cp calls + c3's six) moved VERBATIM out of run() into cold_run_sequence.checkpoints(w, M, reg)
— a function of any world of the tape, returning (rows, {yE}); run() calls it and grades as before (D27); checkpoints_partial(w, M, reg)
runs the same source one statement at a time and answers NOT YET where the text has not arrived (D28); checkpoint_positions.py steps the
base by MARKER under its own session name and measures the FALL of every checkpoint — the first pause from which its verdict and value
are final — into checkpoint_positions.yaml (199 rows; 944 s; `--check` the cheap gate) (D29); the stepper's `--show checkpoints` asks the
block live at a pause and prints the fallen with NEW since the last pause (D30). MEASURED: 48 hold from before the first line; C1 the flood
falls at Genesis 8:4 (ordinal 221); CR5 the refuge term at Numbers 21:4 where Eleazar is invested. checkpoint_probes.py 0/7 → 7/7 (K3's
partial world moved from 8:5 to 7:11 — past the ark-rested marker C1 is computed; three probes read the function's pair as the rows);
the tape 10/10; the journal gate GREEN (hash 8b8fff1fa28953af); the positions gate GREEN. THE COMPILE SHAPE (section 5) gained the step:
a sitting whose block gains a checkpoint reruns checkpoint_positions.py in the background. THE LIST: items 4, 5 and 10 done; NINE open
(the owner's three — 1, 6, 7; after Deuteronomy — 2, 3; small/later — 8, 9, 11, 12). NEXT on the owner's word: DEUTERONOMY, chapters 1
to 3 first, the reading sitting (section 5's shape; the 41 July drafts deu_*.yaml the pre-cut blocks as Numbers' 47 were; the spine the
Sifrei on Deuteronomy — 357 sections, 2,357 rows, eight times Numbers' — beside Onkelos whole; the store's 959 verses against Onkelos'
956, three joins to read; the owed seats in chapters 4, 12, 17, 19, 21, 25). Uncommitted since 376d304: the board, the mockups, item 5,
every record; commit only on "commit push".

## 27. ADDENDUM (2026-09-15, at the owner's compaction before THE PORTABLE REPO sitting — the state doc's COMPACTION POINT #178; "Let's compact then do this rename and relative path to make it work as a clone. Get ready")

THE PORTABLE REPO — THE NEXT SITTING (the owner, 2026-09-15: "Let's compact then do this rename and relative path to make it work as a clone. Get ready"), on the loop's own order: MEASURE → THE DESIGN in a map BEFORE any code → PROBES TO FAIL → the pass → every gate → the records.
THE MEASUREMENTS TAKEN (2026-09-15, by grep and git, before compaction): the absolute path <repo-old> is written into 352 Python files at 474 places — all 57 sweep runners (World/step9/cold_run_*.py), the tape (cold_run_sequence.py: the registry at 146 and 2705, the store _DB at 157, dependency_dispositions at 2722), World/build_world.py (REPO at 26), 3 other World/step9 tools, 18 tools under logic/, 285 forms (copies of past sittings — records, may stay as written), 22 non-Python files (sh/yaml/json/md/html); the engine, the journal, the stepper, the board, ask.py, corpus_world.py and CORPUS_TRUTH.py carry NO absolute path. The symlink <world-link> -> <repo-old>/World. The remote https://github.com/Josephtorah/Torah_Grok.git. The memory folder ~/.claude/projects/<project-folder-old> is NAMED AFTER THE CWD PATH (a renamed folder opens an EMPTY memory — the files must be copied to the new folder's name). THE DATA WALLS a clone hits: the Bible store elijah_docket/tanakh.sqlite (26 MB) lives in the nested elijah_docket git (a gitlink, never staged; *.sqlite gitignored) — every runner reads verses from it; the shelf Data/sefaria_export (6,364 files) is gitignored but for MIRROR_MANIFEST.txt; World/journal/data is derived (the tape run + build_world rebuild it, once the store and the shelf exist). A fresh clone: 3,552 tracked files, the code, the 210 frozen units, every ledger and record — and it cannot run one sitting.
THE DECISIONS THE OWNER MAKES (ask ONE AT A TIME after compaction, before the design): (1) THE NEW NAME (the folder, the GitHub repo — he renames it on GitHub, the remote is then re-pointed; the symlink remade); (2) THE STORE AND THE SHELF for a clone — tracked in the repo (the 26 MB store; the exports), or a fetch script that rebuilds them from their sources with the manifest as the check (the store's own git has no remote printed — its origin to be found); (3) COMMIT FIRST — recommended: "commit push" before the pass so the rename's diff is one clean commit (uncommitted since 376d304: the six mockup versions, the board, item 5, every record).
THE DESIGN'S SHAPE (to be written into its map — proposed home reviews/PORTABLE_repo_2026-09-15.md, the record; a root SETUP.md the deliverable for a clone): ONE ROOT — every file computes the repo root from its own location (the pattern already in the tools: HERE/ROOT from __file__), the 474 occurrences rewritten by ONE script in one pass (the forms excluded by rule, they are records); the runners' registry/store/dispositions paths through the root; THE PROBE THAT PROVES IT: `git clone` the repo into a temporary folder at ANOTHER path (with the store and the shelf provided as decision 2 says) and run there a runner, the tape's grade, the journal gate and the register gate — today it fails at the first absolute path, after the pass it is green; then every standing gate in place (the sweep 57/57, the tape 10/10, the journal gate, the daemon and dependency gates, the register gate, the probe files, the board's and the positions' gates); the symlink, the remote, the memory folder copied; the records (the recovery file's laws — the staging form and the paths in section 3 rewritten to the new name; THE_STEPS; THE_BRIEFING; README; memory's standing orders). NOT TOUCHED: the corpus, the hash, the units, the ledgers (append-only; old paths in old records stand).
THE BOARD'S SERVER: left running on 127.0.0.1:8765 (a stray process; kill before the rename: `lsof -ti :8765 | xargs kill`).
THE FIRST SITTING AFTER COMPACTION: #178's rereads, then decision (1) asked — the new name — then (2), then (3); the design written into its map before a line moves; the probe of the clone at another path written to FAIL first.

## 28. ADDENDUM (2026-09-15, THE PORTABLE REPO — the owner's three decisions: the name TorahSim, a fetch script for the shelf, "commit push" first (d398857); the state doc's COMPACTION POINT #179)

THE PASS DONE (reviews/PORTABLE_repo_2026-09-15.md design + AMENDED BY THE RUN + AS BUILT; decisions P1-P5): every path in the code
computed from the file's own place (`_ROOT`, by logic/solo_tools/portable_pass.py — 367 files, 558 Python occurrences, 44 shell; two more rules
the run taught: 27 exec sites given `_ROOT`, three path-from-pieces files); the Bible store Data/tanakh.sqlite tracked; the snapshot store
torah_grok.SNAPSHOT-main-51801ca.sqlite (154 MB, over GitHub's file limit) a release asset named in Data/STORES_MANIFEST.txt; the shelf's
manifest regenerated with sizes and hashes (6,363 files) and Data/fetch_shelf.py fetching it from Sefaria's bucket (the texts left the git
repository in September 2026); SETUP.md at the root. portable_probes.py 0/5 → 5/5 (the clone at another path runs); the sweep 57/57 at
6,378; the journal gate GREEN (hash 8b8fff1fa28953af); the register gate GREEN. THE LAST ACTS ON THE OWNER'S WORD: "commit push" → the
GitHub rename (`gh repo rename TorahSim -R Josephtorah/Torah_Grok`; `git remote set-url origin https://github.com/Josephtorah/TorahSim.git`)
→ the release stores-2026-09-15 with the snapshot asset → the memory folder copied to ~/.claude/projects/<project-folder>/memory (the
old site session's 14 memory files archived beside it as memory_site_archive_2026-09-15) → .claude/settings.local.json's four path lines →
`mv <repo-old> <repo>` and the symlink `<world-link> -> <repo>/World` → the owner restarts
Claude Code in <repo>. THE NEW THREAD'S FIRST LINE: this file is at the same relative path in the renamed folder.
THEN: DEUTERONOMY, chapters 1 to 3, the reading, on the owner's word.
THE LAST ACTS DONE 2026-09-15 (the owner: "commit push"): (1) COMMITTED 9e6c81a (400 files; pushed); (2) the repository RENAMED on GitHub — https://github.com/Josephtorah/TorahSim (private; the old address redirects), the remote re-pointed, `git ls-remote` answering 9e6c81a; (3) the release stores-2026-09-15 created with torah_grok.SNAPSHOT-main-51801ca.sqlite (153,755,648 bytes) as its asset — a plain download is refused while the repository is private, so fetch_shelf.py now falls back to `gh release download` under the reader's login (a change AFTER the commit, uncommitted), and an empty temporary clone fetched the store through the script in 4 s, GREEN; (4) the memory folder: the old site session's 14 files archived as ~/.claude/projects/<project-folder>/memory_site_archive_2026-09-15, our 49 copied to ~/.claude/projects/<project-folder>/memory; (5) .claude/settings.local.json's four path lines renamed. PENDING, THE LAST ACT ON THE OWNER'S WORD: `mv <repo-old> <repo> && ln -sfn <repo>/World <world-link>` — then the owner restarts Claude Code in <repo>; the first commit there carries fetch_shelf.py's change and these notes.
THE LAST ACT DONE (2026-09-15, the owner's "go", the two lines run by him): the folder is <repo>, the symlink <world-link> -> <repo>/World, the old folder gone; THIS THREAD RESUMED IN THE NEW FOLDER (its transcript copied under the new project name; the memory there, 49 files); at the new path the board's gate, the positions' gate, the builder's reconciliation and the stores' check GREEN first try. Uncommitted here: 40 files — the third scan's rewrites, fetch_shelf.py's gh fallback, these notes; the next "commit push" carries them.
LAYER 2 DONE (2026-09-15): the whole history rewritten by git filter-repo --replace-text over the same sixteen forms — 261 commits in 31 s, no commit touching either login after (git log -S on both: 0); the remote re-added and main FORCE-PUSHED (4f077a0 became b159293); the release tag stores-2026-09-15 existed only on GitHub and still pointed at the old tip, so it was created locally at the rewritten commit and force-pushed (9e6c81a became 7c18242) — the release keeps its asset (153,755,648 bytes) and no old id is referenced on the remote; the bundle of the old history stays in the session's scratch folder as the backup. THE COMMIT MAP: reviews/COMMIT_MAP_2026-09-15.txt — every id before and after; the ids the records name are OLD ids and read through it: 08fa06e → 601b496, 376d304 → d1c7997, d398857 → cbd523a, 9e6c81a → 7c18242, 4f077a0 → b159293, a42f518 → 6fbc9cd, 0a98276 → 609c2ff, aff58ff → 7e45f6d. A CAVEAT NAMED: GitHub keeps unreachable objects for a time and serves a commit by its full id to anyone who has it — on a private repository a small matter; a support request purges them. The old project folders under the home's .claude (the earlier sessions' transcripts, the old memory) are outside the project and carry the login in their names by Claude Code's own rule — the owner's to delete.
LAYER 3 DONE (2026-09-15, the owner's own hands): the repo moved to /Users/Shared/TorahSim — a path with no username — the symlink <world-link> remade to /Users/Shared/TorahSim/World, the old folder gone; this thread resumed there with the memory under the project name -Users-Shared-TorahSim (49 files) and the settings' four lines pointing at the shared folder; at the new path the home-path gate, the board's gate, the positions' gate, the builder's reconciliation and the stores' check GREEN, then the tape and the stepper run (their prints in the reply). THE USERNAME SCRUB IS COMPLETE IN ALL THREE LAYERS. Left to the owner: the two old project folders under the home's .claude (their names carry the login by Claude Code's rule) and the old TorahCode repository's note that points at the now-private TorahSim. NEXT on the owner's word: DEUTERONOMY, chapters 1 to 3, the reading.
THE PUBLIC REPO (2026-09-15): Josephtorah/TorahSim is PUBLIC under CC0 1.0 (LICENSE; DATA_SOURCES.md the terms of what others wrote); the copyrighted book purged from the tree and the history by a second rewrite (the commit map three columns now); TorahCode's note retired; the release asset answers by its plain address. A CLONE ANYWHERE: SETUP.md. NEXT on the owner's word: DEUTERONOMY, chapters 1 to 3.

## 29. ADDENDUM (2026-09-15, at the owner's compaction after THE PUBLIC REPO — the state doc's COMPACTION POINT #180; "we need to compact get ready")

EVERYTHING COMMITTED at f320660 and pushed; the repository PUBLIC under CC0 (github.com/Josephtorah/TorahSim); the folder /Users/Shared/TorahSim;
no username anywhere; a clone anywhere runs by SETUP.md. THE FIRST SITTING AFTER COMPACTION: #180's rereads, then DEUTERONOMY chapters 1 to 3 on
the owner's word — the reading sitting (section 5's shape; the July drafts deu_01 through deu_03 the pre-cut blocks; the Sifrei on Deuteronomy
beside Onkelos whole; the store's 959 verses against Onkelos' 956), then its compile. The forms of the last Numbers sittings (World/step9/
forms_numbers_walk/, the ref_* set the newest) are the templates; a new form computes its root from its own file and writes to a scratch
folder computed at run time — never a typed absolute path (the gate refuses one).

## 30. ADDENDUM (2026-09-15, THE BOARD DRIVES THE ENGINE — the owner, watching the board live: "it seems to keep running no matter what button I push" → "the buttons should control the engine, it should not run on auto pilot behind the scenes. is there a reason it should?" → "put a stop button also. if I click autoplay it shoudl change to stop. one button two options. built it"; THE_LOOP.md "THE BOARD DRIVES THE ENGINE" design + as built, D31-D33)
WHAT CHANGED: the engine (world_stepper.py --board) waits and takes exactly one step per ask from the page; Next at the live end asks one;
Auto-play asks one per tick of the speed dial until Stop — one button, two words; the Follow button is gone (the return to LIVE is
reaching the end of what has arrived); Back and the left screen replay. THE STEP SIGNAL: two files beside the database, one writer each
way — board_asks.json (the server) and board_engine.json (the engine: heartbeat, next verse, done, sealed); POST /api/control
{"cmd": "step"} the board's only write, never the database. HOW TO WATCH NOW: `python3 World/step9/world_board.py` in one window,
`python3 World/step9/world_stepper.py --board` in another, http://127.0.0.1:8765/ (the hands-free form `--by verse --pace 1` still runs
the engine on its own; the section-25 line above is superseded). THE ENGINE'S FIXED PRICE: about 90 s of import before its first step
(python3 -u when its stdout is a file, else the log fills only at the end). drive_probes.py X1-X5 5/5 (each in its own journal folder,
WORLD_JOURNAL_DIR, on its own port); the gate GREEN; board_probes 8/8 in its own folder. ⚠ LAWS LEARNED: NEVER RUN A PROBE OR A SECOND
STEPPER UNDER THE LIVE SESSION'S SOURCE NAME (board_probes' B7 wiped the live session once — while an engine is live, run those probes
with WORLD_JOURNAL_DIR set to a scratch folder); A BACKGROUND CHILD MAY INHERIT SIGINT IGNORED (the engine restores its handler).
UNCOMMITTED at this writing (with #180, section 29 and #180's addenda): the three code files, drive_probes.py, the records named in the
as-built — the owner's next "commit push" carries them.

## 31. ADDENDUM (2026-09-15, THE DEUTERONOMY WALK sitting 1 — THE OPENING SPEECH, Deuteronomy 1:1-3:29 READ AND FROZEN; the owner: "lets plan for deut next. where do we start" → "commit push" (29d477a) → "I don't need to compact. read what you need to get ready" → "start with deuteronomy"; the state doc's COMPACTION POINT #182)

THE BOOK OPENED. The map is World/step9/DEUTERONOMY_WALK.md (NEW — the head carries the walk's form and the shelf measured; "Sitting 1" the
reading's record and the owed list (a)-(l)). The rulings are the Numbers walk's (section 13-14 above; the memory numbers-in-order-ruling.md):
READ THEN COMPILE PER PORTION, CHAPTER NUMBERS, the parashah grain, the spine Onkelos + the Sifrei on Deuteronomy BY POSITION. The forms are the
Numbers walk's sitting-15 forms edited (World/step9/forms_deuteronomy_walk/ — deu_dump0 / parser0 / measure0-2, deu_ink with the driver and the
legs, the rows files, write_deu_ledger, patch_overrides_deu, write_deu_manifest, seat_deu (STEP_Dt_ ids), deu_chain.sh, copy_deu_forms,
write_deu_records). THE STATE: 216 frozen units (210 + 6), standing 2184 (2163 + 21), hash 8b8fff1fa28953af UNMOVED; CORPUS TRUTH, build_world,
the journal gate, the register gate GREEN; no engine file changed; the ledger logic/oral_triage/deu_01_03_devarim_2026-09-15.md (259 sources);
the six manifests (21 claims DV01A..DV03B); the display layer +275 rows. THE READING'S SHAPE HELD on the new book (the section-5 shape): dump →
parser → measure (three passes) → asserts (8, 22, 11, 12 fell on the typed passes → 0) → rows (112 + 147) → the writer (0 misses; the lint 1 → 0)
→ the patch → the manifests (21/21, the strict census GREEN) → the seat → six rituals (13 PASS each) → the fold predicted and matched. THE
SHELF: the Sifrei on Deuteronomy's 357 piskaot / 2,357 rows in BOTH files, equal grains; piskaot 1-25 on 1:1-1:28 and 26-30 on 3:23-3:29, NO piska
on 1:29-3:22; the English rows carry the translator's apparatus and the "(Dt.1:1)" form with no space; seven outside Hebrew rows (nine English:
36:10 and 37:2 added on 1:4, 199:5 mis-cited) credited; the one "ibid" resolving to Song of Songs (the measurement's hit corrected); six rows read
before by topic in Genesis ledgers (1:13, 6:1, 8:1, 11:1, 25:4, 27:3) named. THE FINDS (the ledger's twenty crowns; the map's THE INK): the two
islands; Onkelos writing the Sifrei into 1:1; the receipt of the rules (1:3); one clock, two readers; the officers' arithmetic; the judges' charge as
Avot 1:1 and Sanhedrin 4:1; the hard matter THE TENT's; the spies' words retold; the spy-verb against the tour-verb; "enough" plural and singular;
the retellings' disagreement on Edom (2:29 — the compile's open question, a hypothesis row); 2:33's written and read; Numbers 21:33-35 turned; Og's
bed; Joshua plene once; the plea's names; Lebanon the Temple at 3:25; the four directions in three orders; the run against the spec at Ai; the
valley Peor's. THE LESSONS (nine, the map's ⚠ list): the ibid to the nearest book named; the English apparatus; the prior-read census's strict
row form; a count from a looser regex is a different number; the lemma's letter; MIDDOT's own label codes (E4 → E7); a written-once guard fires on
the rerun — scope it to the first pass and swap a rewritten ledger in whole by a temp path; grep the override file's keys before a by-gloss list;
the shape held. NEXT on the ruling: SITTING 1b — THE COMPILE OF DEUTERONOMY 1-3 (the owed list (a)-(l) in DEUTERONOMY_WALK.md; THE READBACK's design
on the owner's word FIRST — the speech as the tape read back, the diffs against Numbers 13-14, 20-21, 32 its specimens; the register gate's four
seats paid; the officers' table; the judges' spec; the fraction's probes; the one clock; the retellings by reference; the docket by the union rule)
— the design in the map before any code; then chapter 4's reading. UNCOMMITTED at this writing: everything of this sitting (the state doc's #182
names every path) and #180's addenda 3-4 and #181 — the owner's next "commit push" carries them.

## 32. ADDENDUM (2026-09-16, THE DEUTERONOMY WALK sitting 1b — THE OPENING SPEECH COMPILED, Deuteronomy 1:1-3:29 with Numbers 27:12-23 as its callee; the owner: "Go 1b right" → "Yes 1. Go" (THE READBACK'S FIRST FORM, option 1); the state doc's COMPACTION POINTS #183 (mid-sitting) and #184 (the close))

THE SITTING RAN IN THE COMPILE SHAPE (section 5) WITH ONE STEP ADDED — THE READBACK: World/step9/DEUTERONOMY_WALK.md "Sitting 1b" (the design:
(R1)-(R6), the decisions (a)-(l), the cells, the twenty-four DATA rows, the daemon, the types, the tape, CA1-CA9, the prediction's arithmetic, the
probes, THE ORDER) and "Sitting 1b — AS BUILT" (the departures, the misses, the lessons). THE STATE: cold_run_opening_speech.py the 58th runner
(97/97; sixteen tape lines; forty-two readback rows; the exam's thirty-three persons); law_opening_speech the 63rd daemon (given_at Deut 1:16,
installed_by boot with the class named); the tape 10/10 — RUN (1295, 96, 88, 0, 12, 1583, 34, 319, the four pairs, 126), PREVIOUS_RUN 15b's,
THE REST reproducing it; entities 319 (the sons of Ammon), closes 126 (five inside the daemon, none a tape line), markers 161 (Deut 1:1 forward at
(40, 11, 1); 1:6, 1:9, 2:2 retrograde), the population 148 unmoved; the hash 8b8fff1fa28953af unmoved (no unit changed); every probe suite and gate
GREEN (the journal gate after the timers view's fix; the register gate --strict with DECLARED 100, DEBT 0 — Num 27:22 CLOSE and Deut 4:45 DAEMONS
green, Deut 1:3 ACT, 1:19 and 1:41 CHAPTER declared, 1:1 EMPTY refreshed); the docket logic/oral_triage/deu_01_03_devarim_exam_2026-09-15.md (864
rows — LAW 83 / DERIVATION 93 / DISPUTE 29 / CONTEXT 631 / OUTSIDE 28; credited 250; Sanhedrin 23a-31b whole). THE ENGINE CHANGED TWICE, both fixes
found by the speech's clock walk and recorded: cold_run_sequence.slot_of strips the parser's marks before the slot match (rule 30's fraction mark had
stamped Exodus 12:29's plague line 'night'); World/journal/run_views.sql's run_timers joins the fire on the timer's value too (two period timers of one
effect on one day doubled the join). RULE (30) THE HALF OF A NAMED WHOLE taught (fifteen Torah tokens in fourteen verses moved; "my arrows" excluded
by the hataf-patach); the seven runners retyped from the sweep's print; census_probes 224/224. THE READBACK'S FIRST FORM: a retelling a REFERENCE
ROW (never a second act), graded and found on the running world (CA4, Q2); an act told only in the retelling written ONCE at its own time by a
retrograde marker; the four supplied debits CLOSED AT ONCE BY A PRIOR RUN inside the daemon (the engine writes a daemon's effects after it returns —
the daemon writes the one-block debit itself); the two disagreements OPEN (2:29 Edom, 1:37 the bar's ground); the receipts run citations (the gate's
CHAPTER); the frame the book's one act of its own day. THE LAWS' HALF OWED (THE_LOOP.md step 6's row and list item 3). THE LESSONS: twelve on the map
(the fast checker; the CASES generated; literal submits; the daemon's write order; sum the watches; the clock walk moves the timer checkpoints; a
mark is not a word; the CHAPTER class; the value-keyed join; ROOT by git and _ROOT in the INK namespace; a probe's verse a tape position; fires by
day number). THE FORMS: World/step9/forms_deuteronomy_walk/ (72 files — the reading's 27, the compile's 45 scripts and prints). THE RECORDS current: the map, COMPILE_DEBT (the sitting-1 box PAID; the 1b
box), MOVE_CATALOG (M-16's eleventh exemplar), MIDDOT, MISHNAH_TOPICS (nine rows), RESEARCH_LOG, THE_STEPS, THE_BRIEFING, THE_LOOP, THE_WORLD, RESUME,
the memory, the state doc's #184. NEXT on the ruling: chapter 4's reading, then its compile; the laws' readback at chapter 5. UNCOMMITTED at this
writing: sitting 1's forty paths and every path of this sitting — COMMITTED b8b721d (2026-09-16, on the owner's "Commit" — 139 files; NOT PUSHED, the push waits on his word). AT THE VERY CLOSE: the positions table 208 rows; checkpoint_probes 7/7 after its beyond-the-tape verse moved
(the thirteenth lesson); the tape 10/10 on the final bytes; the sweep 58/58 at 6,475 graded cells (cold_run_opening_speech.py 97/97), then the journal gate ALONE after the sweep's process ended — GREEN (the state doc's #184 addendum 2). SITTING 1b CLOSED.


## 33. ADDENDUM (2026-09-16, THE DEUTERONOMY WALK sitting 2 — CHAPTER 4, Deuteronomy 4:1-49 READ AND FROZEN; the owner: "Reread what is next" → the rereads → "Go"; the state doc's COMPACTION POINT #185)

THE SITTING RAN IN THE READING SHAPE (section 5) on a chapter WITH NO PISKA: World/step9/DEUTERONOMY_WALK.md "Sitting 2". THE STATE: 218 frozen
units (216 + 2 — deu_04_obey_horeb 4:1-40, deu_04_refuge_east 4:41-49), standing 2191 (2184 + 7 as predicted), hash 8b8fff1fa28953af UNMOVED;
CORPUS TRUTH, build_world, the journal gate (12 kinds, 9,646 rows), the register gate --strict (DECLARED 100, DEBT 0, FAILS 0) GREEN; no engine file
changed; the ledger logic/oral_triage/deu_04_vaetchanan_2026-09-16.md (55 sources — Onkelos 49 fresh, the Sifrei's six rows citing the chapter fresh,
two credited from sitting 1); the two manifests (7 claims DV04A-01..05, DV04B-01..02); the display layer +144 rows. THE SHELF: the Sifrei on
Deuteronomy has NO piska on chapter 4 (30 on 3:29, 31 on 6:4; the heads by chapter computed on all 357) — the found-by-citation scan the whole spine:
eight rows (seven Hebrew, eight English; 301:21 the English's alone — THE EXPORT'S THIRD CITATION FORM, an unpointed abbreviated Hebrew, "(Devarim
4:34)" with a space); Onkelos Deuteronomy's export gives CHAPTER 5 THIRTY VERSES against the DB's thirty-three (the one disagreeing chapter — the
next reading measures the mapping first). THE READING'S SHAPE HELD: dump (one script for the three first-pass scripts) → measure (three passes: the
retellings diffed, the phrase censuses, the Onkelos seats, the gloss families) → asserts (6 fell on the first typed pass → 0) → rows (49 + 6; the
Sifrei cuts fell seventeen at once for being typed pointed) → the writer (0 misses; lint 0 on the first write) → the patch (81 by reference with the
indices computed from the store, 63 by gloss) → the manifests (7/7; the labels gate after two labels re-closed with their parenthesis) → the seat
→ two rituals (13 PASS each) → the fold predicted and matched. THE FINDS (seventeen crowns): the shelf's silence and the third citation form; ONE LAW
(4:2 add / diminish, no case token) and ONE CASE (4:25 "when you beget sons"); LEARN AND TEACH ONE WORD (4:10's two ילמדון "they shall learn /
teach" — qal and piel by the pointing alone); the TABLETS PLENE (4:13); the THIRD TELLING OF THE BAR (4:21 "on your account" with an oath — 1b's open
row widened); the RECEIPT IN MOSES' OWN VOICE (4:5, the register's seat); the translation's FEAR, MEMRA AND SHEKHINAH (4:4, 20, 24, 29-30, 33, 36-37,
39), "prepared" for "apportioned" (4:19), the idolaters for the idols (4:28), the miracles for the question (4:34), the Name for "God" (4:32), "see"
plural (4:5); the number switching by verse; the Decalogue's image recast (4:16-19); "you were shown" / "that saw" one spelling; the creed twice
(4:35, 39); the one "created" (4:32); THEN MOSES SET APART (4:41 — the refuge runner's debit appoint_six_cities_of_refuge OPEN since Numbers 35:14,
the compile's to close); the two frames (1:1, 4:45) and the speech's borders retold verbatim (1:4, 2:36, 3:8, 3:17); the Sifrei 306:1's witnesses;
the Haggadah's row (301:21). THE LESSONS (nine, the map's ⚠ list): the cutter takes consonants; a label ends with its parenthesis; the scratch
scripts run from the repo root; the DB's verse order is alphabetical by book; the export's chapter division is not the DB's; a substring census is
not a token census; a family already rewritten is caught by the ink's assert; a step block carries two comment lines; the reading shape held on a
chapter with no piska. THE FORMS: World/step9/forms_deuteronomy_walk/ (+ the sitting's scripts and prints). THE RECORDS current: the map, COMPILE_DEBT
(the sitting-2 box (a)-(l); the 1b box's item (ii) is its (d)), RESEARCH_LOG, MIDDOT (six rows), STAMP_LEDGER, THE_STEPS, THE_BRIEFING, RESUME, the
memory, the state doc's #185. NEXT on the ruling: SITTING 2b — THE COMPILE OF CHAPTER 4 (the design in the map before any code: the one law's cell,
the one case's arms, the receipt's seat 4:5, the three cities closing the refuge debit, the chapter's readback rows on the first form, the two frames'
day, the no-image list as DATA, the docket by the union rule), then chapter 5's reading (the Decalogue; the export's division measured first; the
laws' readback opens with it). UNCOMMITTED at this writing: everything of this sitting and the three records that named b8b721d — the owner's next
commit word carries them (the last commit b8b721d, not pushed).

AT THE CLOSE (2026-09-16, the owner: "ok get ready to compact. then we finish 4"): the frame restated — "law is code and narrative is everything else in a computer program" (the memory compiler-law.md); the peer thread's Decalogue-schema finding ON THE TABLE, not a ruling (the state doc's #185 addendum 1; its natural seat chapter 5, AFTER 2b); THE WORD FOR 2b GIVEN — after the compaction and the rereads, the compile of chapter 4 begins on section 5's compile shape with the map's "Sitting 1b" as the form on this book and "Sitting 2"'s owed list (a)-(l) as the checklist. The tree uncommitted since b8b721d.

## 34. ADDENDUM (2026-09-16, THE DEUTERONOMY WALK sitting 2b — THE COMPILE OF CHAPTER 4, Deuteronomy 4:1-49 COMPILED AND ON THE TAPE; the owner: "ok get ready to compact. then we finish 4" — the word given before the compaction; the state doc's COMPACTION POINT #186 + ADDENDUM 1)

THE SITTING RAN IN THE COMPILE SHAPE (section 5; "Sitting 1b" the form on this book): World/step9/DEUTERONOMY_WALK.md "Sitting 2b" (the design, written
before any code) and "Sitting 2b — AS BUILT" (the departures and the lessons). THE STATE: cold_run_obey_horeb.py the 59th runner (52/52 — six cells,
nineteen DATA rows, the readback's eleven rows, 96 token probes), law_obey_horeb the 64th daemon (given_at Deut 4:2, boot with the vows' class named;
64 daemons, 441 functions), event_vocabulary +6 (1119), effect_vocabulary +4 (1019), dependency_dispositions +16 edges +2 pointers (521 edges, 192 pointers
on file), register_dispositions Deut 4:5 ACT; THE TAPE 10/10 WITH THE REST — RUN (1300, 96, 88, 0, 12, 1588, 35, 319, the four pairs, 126) as predicted,
PREVIOUS_RUN 1b's, NEWEST_RUNNER obey_horeb, markers 165 (F 128 / P 15 / R 22), entities 319, closes 126, the population table 148, CC1-CC9 MATCH; the
docket logic/oral_triage/deu_04_vaetchanan_exam_2026-09-16.md (327 rows — link 68 / topic 259; LAW 76; credited 98; the nine ranges whole). THE GATES:
the probe suites census 224/224, installation 6/6 (I5 64), readback 9/9, register 7/7, clock 22/22, sequence 4/4, view 6/6, population 9/9, journal 7/7, cursor 6/6, checkpoint 7/7; the daemon gate GREEN (64 daemons, 441 functions); the dependency gate GREEN (521 edges and 192 pointers on file — the link census reference 498 / transfer 48 / hypothesis 9 / none 158; required 261 edges and 193 pointers, live import edges 369); build_world ALL GREEN (standing 2191, hash 8b8fff1fa28953af unmoved); the journal gate GREEN twice — before and after the sweep (12 kinds, 9646 rows in the index); THE REGISTER GATE --strict GREEN (DECLARED 100, DEBT 0, FAILS 0 — Deut 4:5 ACT declared, its write adding_barred on Israel; Deut 4:45 DAEMONS green with daemons 2: law_opening_speech@Deut 1:16 and law_obey_horeb@Deut 4:2); the positions table 217 checkpoints over 167 pauses (CC1-CC9 in it; checkpoint_probes 7/7 after the rebuild); the sweep 59/59 at 6,527 graded cells; the home-path gate GREEN.

WHAT THE SITTING FOUND (RESEARCH_LOG 2026-09-16, the compile entry): THE TAPE'S HOLE — no line for Exodus 20:1 (the ten words spoken) nor 31:18 (the
tablets given): both told first in the retelling and written ONCE at their own days by retrograde markers at Deut 4:10 (1, 3, 7) and 4:13 (1, 4, 17);
A RETROGRADE STRETCH RUNS TO THE NEXT MARKER (forward markers at 4:1 and 4:25 — four, not the design's two); A LAW SENTENCE WITH NO NARRATIVE VERB is a
statute-form line (add_nothing_commanded); A KIND SHARED ACROSS BOOKS is selected by verse (lord_descended at Genesis 11:5 and Exodus 19:18); THE
SECOND WORD (Exodus 20:3-6, the image law) has NO CELL in any runner — 4:16-19's list DATA, the debt named at the edge obey_horeb → decalogue, OWED to
chapter 5's sitting; THE REFUGE DEBIT LEFT OPEN on Mishnah Makkot 2:4 (Moses' three a STATUS; the close Joshua 20:7-8, outside the Torah); the bar's
third telling (4:21-22) a second DISAGREES row OPEN beside 1:37's. THE ELEVEN LESSONS in the map's AS BUILT (the stretch's forward marker; the chapter's
opening marker; the statute form; the marker row's numbers; the doubly escaped apostrophe; the callee's ask from the recon's print; the census's tape
kinds; a shared kind by verse; the eras on the clock; a write script never gates on an unverified assertion; the fast checker's tags from the print).

THE FILES CHANGED BY 2b: World/step9/cold_run_obey_horeb.py (new), cold_run_sequence.py (the tape section, the literals, CC1-CC9, CA1/CC1/CC9's
retypes, CP6), event_vocabulary.yaml, effect_vocabulary.yaml, daemon_dispositions.yaml, dependency_dispositions.yaml, register_dispositions.yaml,
readback_probes.py (Q7-Q9; Q4 narrowed), checkpoint_probes.py (beyond_the_tape()), installation_probes.py (I5 64), checkpoint_positions.yaml (rebuilt),
the docket (new), the forms folder (copy_ch4b_forms.py), the records (the map, COMPILE_DEBT, MIDDOT, MISHNAH_TOPICS, RESEARCH_LOG, THE_STEPS,
THE_BRIEFING, THE_LOOP, RESUME, this file, the state doc, memory). NOT COMMITTED — the tree uncommitted since b8b721d; commit on the owner's word only.

NEXT ON THE RULING: SITTING 3 — CHAPTER 5's READING: measure the export's thirty-verse chapter 5 against the DB's thirty-three FIRST (the Decalogue's
division), then the reading in the reading shape (section 5). ON THE TABLE, NOT A RULING: the Decalogue-schema sitting (the ten as headers over the
laws; the state doc's #185 addendum 1; the map's tail) — after 2b on the owner's word, its natural seat chapter 5. THE FRAME (the owner, 2026-09-16):
law is code, narrative everything else in a computer program.

## 35. THE COST CUTS (2026-09-16, after sitting 2b; the owner: "what is taking so long and costing so much money" → "lets do all 3")

THE DIAGNOSIS HE ACCEPTED: every tool call re-sends the whole conversation, so the bill is the NUMBER OF TURNS, never the size of a batch; smaller
runs would cost more. At 2b: ~20 turns were wait loops on background gates (positions 21 min, the sweep 15 min, the journal gate's replay); six tape
runs at ~4 min each, one checkpoint fault apiece; ~10 reads to learn the record files' shapes. THE THREE CUTS, BUILT: (1) NEVER POLL — the gates step
is ONE chain, `sh World/step9/gates_chain.sh <out_dir> [--from STEP] [--skip A,B]` (tape → the ten probe suites → daemon → dependency → build_world →
the journal gate → the register gate --strict → positions → checkpoint_probes → the sweep → the journal gate again; the long steps skipped after a
failure; each print in <out_dir>/<step>.out; ONE summary <out_dir>/SUMMARY.txt) run in the background with the harness's notification, the summary
read once; (2) ONE FAST CHECK BEFORE THE TAPE — `python3 World/step9/checkpoint_check.py <PREFIX>` (the stepper to the tape's end under its own
session name, then checkpoints_partial: every miss with its tuples and every raised statement with its line in one print; exit 1 on any); (3) THE
RECORD FORMS SHEET — World/step9/RECORD_FORMS.md (every record's path, mode, anchor, head form and lint baseline; the writer built from it, --check
then write; the form write_ch4b_records.py). THE SITTING SHAPE OF SECTION 5 AMENDED BY THESE: "the tape run 10/10" is preceded by the fast check;
"the probe gates … the sweep … the journal gate alone" is one chain call; "the records" is one writer call from the sheet. Memory:
cost-rules-no-polling.md.

## 36. ADDENDUM (2026-09-16, THE DEUTERONOMY WALK sitting 3 — CHAPTER 5, Deuteronomy 5:1-33 READ AND FROZEN; the owner: "reread", "go"; the state doc's #187 addendum 1)
THE STATE: chapter 5 read and frozen as one unit (deu_05_decalogue, the 219th); the corpus 219 units, standing 2197 (2191 + 6 as predicted), hash
8b8fff1fa28953af unmoved; the tape UNMOVED (no engine file changed — RUN (1300, 96, 88, 0, 12, 1588, 35, 319, the four pairs, 126), markers 165);
the journal gate GREEN (12 kinds, 9660 rows); the register gate --strict GREEN (DECLARED 100, DEBT 0, FAILS 0); uncommitted since 834602b.
WHAT THE SITTING FOUND: the two divisions mapped by alignment (the export's 17 = the DB's 17-20); the second copy of the ten words diffed verse by
verse — five verbatim, one letter at 5:8, the ketiv at 5:10, KEEP for REMEMBER at 5:12 with the receipt "as the LORD your God commanded you" (5:12,
5:16 — the register gate's seats), the two beasts and the servants' rest at 5:14, the ground changed whole at 5:15, "and" on the four short words,
the vain witness for the false, the wife first and a second verb at 5:21; the Sifrei 233:1's "remember and keep in one utterance" (the Mekhilta
named, the first copy's spine unopened by any ledger); face to face the Bible's one seat, Onkelos "speech with speech"; the ten words in the
singular; the third generation starred by the parser; "added no more" read "did not cease"; the mob and the elders (1:22, 5:23); "hear and do"
against "do and hear"; Moses standing (357:40).
THE FILES CHANGED: logic/oral_triage/deu_05_vaetchanan_2026-09-16.md (new); logic/units/deu_05_decalogue.yaml (draft → frozen, six operators, step E,
the scenarios in the anchor form) and logic/py_units/deu_05_decalogue.py; logic/oral_audit/manifests/deu_05_decalogue_claims.json (new);
logic/glosses/word_gloss_overrides.yaml (+58 by reference, +54 by gloss); logic/corpus/CORPUS_TRUTH.py (219, 2197); the records (the map,
COMPILE_DEBT, MIDDOT, RESEARCH_LOG, THE_STEPS, THE_BRIEFING, RESUME, the state doc, the recovery page, this file, STAMP_LEDGER, the memory);
World/step9/forms_deuteronomy_walk/ (the sitting's scripts and prints).
NEXT ON THE RULING: the compile of chapter 5 (3b) — or the Decalogue-schema sitting first — on the owner's word.

## 37. ADDENDUM (2026-09-16, THE DEUTERONOMY WALK sitting 3b — THE COMPILE OF CHAPTER 5, Deuteronomy 5:1-33 COMPILED AND ON THE TAPE; the owner: "go"; the state doc's #188 addendum 2)

THE SITTING RAN IN THE COMPILE SHAPE (section 5; "Sitting 2b" the form): World/step9/DEUTERONOMY_WALK.md "Sitting 3b" (the design, written before any
code) and "Sitting 3b — AS BUILT" (the departures and the lessons). THE STATE: cold_run_covenant_at_horeb.py the 60th runner (49/49 — seven cells,
twenty DATA rows, the readback's twenty-one rows), law_covenant_at_horeb the 65th daemon (given_at Exod 20:3, installed_by covenant_blood_thrown; 65
daemons, 448 functions), event_vocabulary +3 (1122), effect_vocabulary +4 (1023), dependency_dispositions +12 edges +3 pointers (533 edges, 195 pointers on
file), register_dispositions Deut 5:12 / 5:16 / 5:32 CHAPTER; THE TAPE 10/10 WITH THE REST — RUN (1302, 96, 88, 0, 12, 1593, 36, 319, the four pairs,
127) as predicted, PREVIOUS_RUN 2b's with ONE DECLARED DELTA (the daemon's two blocks on THE REST), NEWEST_RUNNER covenant_at_horeb, markers 167 (F 129 /
P 15 / R 23), entities 319, closes 127, the population table 148, CI1-CI9 MATCH; the docket logic/oral_triage/deu_05_vaetchanan_exam_2026-09-16.md (275
rows — link 43 / topic 232; LAW 77; credited 94; the ten ranges whole). THE GATES: the probe suites census 224/224, installation 6/6 (I5 65), readback 12/12, register 7/7, clock 22/22, sequence 4/4, view 6/6, population 9/9, journal 7/7, cursor 6/6, checkpoint 7/7; the daemon gate GREEN (65 daemons, 448 functions); the dependency gate GREEN (533 edges and 195 pointers on file — the link census reference 512 / transfer 48 / hypothesis 9 / none 159; required 263 edges and 196 pointers, live import edges 381); build_world ALL GREEN (standing 2197, hash 8b8fff1fa28953af unmoved — no freeze this sitting); the journal gate GREEN twice — before and after the sweep (12 kinds, 9660 rows in the index); THE REGISTER GATE --strict GREEN (DECLARED 100, DEBT 0, FAILS 0 — Deut 5:12, 5:16, 5:32 CHAPTER declared, the receipts inside the code run citations of the giving; Deut 4:45 DAEMONS green with daemons 2); the positions table 226 checkpoints over 168 pauses (CI1-CI9 in it; checkpoint_probes 7/7 after the rebuild); the sweep 60/60 at 6,576 graded cells; the home-path gate GREEN.

WHAT THE SITTING FOUND (RESEARCH_LOG 2026-09-16, the compile entry): THE LAWS' READBACK — sixteen rows on the code, each naming its cell, VARIANT the
grade the code's copy adds; THE CODE'S HOLE — the second and the tenth words had NO CELL in any runner: compiled here from both copies, their blocks
written at the giving's line (1, 3, 7), THE REST's one declared delta; THE TAPE'S SECOND HOLE — Exodus 20:18-21 (the request for a mediator) has no line:
the request and the answer (told only here) written once at (1, 3, 7) by the retrograde marker at Deut 5:23, the forward marker at 5:32; THE CHARGE TO
TEACH a debit on Moses closed by the prior run (the frame's line 1:1-5 the closer); THE RECEIPT'S TWO REFERENTS (the giving; Marah — Sanhedrin 56b) at
the seats and the pointers; THE SHELF'S TWO NUMBERINGS — the quoted words fix the verse; A CLOSE MOVES EVERY OLD COUNT — eight REST literals retyped.
THE NINE LESSONS in the map's AS BUILT.

THE FILES CHANGED BY 3b: World/step9/cold_run_covenant_at_horeb.py (new), cold_run_sequence.py (the tape section, the literals, CI1-CI9, the retypes
CP6 / CA1 / CA9 / CC8 / CC9 and the eight closes literals), event_vocabulary.yaml, effect_vocabulary.yaml, daemon_dispositions.yaml,
dependency_dispositions.yaml (the span, twelve edges, three pointers; the 2b OWED why amended PAID), register_dispositions.yaml, readback_probes.py
(Q10-Q12), installation_probes.py (I5 65), checkpoint_positions.yaml (rebuilt), the docket (new), the forms folder (copy_ch5b_forms.py), the records
(the map, COMPILE_DEBT, MIDDOT, MISHNAH_TOPICS, RESEARCH_LOG, THE_STEPS, THE_BRIEFING, THE_LOOP, RESUME, the recovery page, this file, the state doc,
memory). NOT COMMITTED — the tree uncommitted since 834602b; commit on the owner's word only.

NEXT ON THE RULING: the commit on the owner's word; then CHAPTER 6's READING (6:1-25 — the Shema, the words on the heart, the reading shape on sitting 3's
forms). ON THE TABLE, NOT A RULING: the Decalogue-schema sitting (the ten as headers over the laws; its seat chapter 5 — the exhibits the Sifrei 233:1,
remember-and-keep in one utterance, the ten as one reading) — on the owner's word.

## 38. ADDENDUM (2026-09-17, THE DEUTERONOMY WALK sitting 4 — CHAPTER 6, Deuteronomy 6:1-25 READ AND FROZEN in four runs; the owner: "ok lets start the next chapter", "go", "Continue", "Go"; the state doc's #190 and its addenda 1-3)
THE STATE: chapter 6 read and frozen as one unit (deu_06_shema, the 220th); the corpus 220 units, standing 2203 (2197 + 6 as predicted), hash
8b8fff1fa28953af unmoved; the tape UNMOVED since 3b (RUN (1302, 96, 88, 0, 12, 1593, 36, 319, the four pairs, 127), markers 167, closes 127); the
journal gate GREEN (12 kinds, 9674 rows); the register gate --strict GREEN (DECLARED 100, DEBT 0, FAILS 0); uncommitted since 7c8554e.
WHAT THE SITTING FOUND: the Sifrei's piskaot 31-36 on 6:4-9, one per verse of the Shema (the first heads on the chapter since piska 30 on 3:29); the
creed's first utterance Jacob's sons' answer at his deathbed (31:6); "the LORD is one" at 6:4 and Zechariah 14:9 alone (the parser [1] / [1, 1]); the
store drops 6:4's two large letters (a HYPOTHESIS on the owner's word, PARKED); "might" the Bible's one seat, read as money, measure, thanks (Onkelos
"your property"); the two sets recited and bound with the ten words in neither; THE EXPORT'S TWO FILES DIVERGE at 36:10 (the Hebrew's parable, the
English's own 37:2 repeated — a credit is a credit on the file read); THE SHELF'S COUNT FROM THE SPELLINGS needs 11:18 "frontlets" defective where the
ink is plene (the compile's open row); the verbal analogy with two candidates (36:2); extension after extension on the one-letter pair 6:9 / 11:20;
the spoil permitted by 6:11 (201:3); the son's question verbatim with Exodus 13:14 and the answer in the first person plural; the receipt without the
Name at 6:25. THE FOUR-RUN RULE'S FIRST SITTING: the runs' edges held; the reread after the one compaction three files.
THE FILES CHANGED: logic/oral_triage/deu_06_vaetchanan_2026-09-17.md (new); logic/units/deu_06_shema.yaml (draft → frozen, six operators, step E, the
scenarios in the anchor form) and logic/py_units/deu_06_shema.py; logic/oral_audit/manifests/deu_06_shema_claims.json (new);
logic/glosses/word_gloss_overrides.yaml (+24 by reference, +33 by gloss); logic/corpus/CORPUS_TRUTH.py (220, 2203); World/step9/large_letter_probes.py
(new) and gates_chain.sh; the records (the map, COMPILE_DEBT, MIDDOT, RESEARCH_LOG (three entries of this date), THE_STEPS, THE_BRIEFING, RESUME, the
state doc, the recovery page, this file, STAMP_LEDGER, the memory); World/step9/forms_deuteronomy_walk/ (the sitting's scripts and prints).
NEXT ON THE RULING: the commit; then the compile of chapter 6 (4b) in four runs — or the Decalogue-schema sitting first — on the owner's word.

## 39. ADDENDUM (2026-09-17, THE WHOLE-ROW RULE — owner-ruled between 4b's RUN 2 and RUN 3 on "OK, never ever cut corners with the Talmud go back and fix the ones where the shortcut was taken and write it in the rules forever")

THE WHOLE-ROW RULE (owner-ruled 2026-09-17: "never ever cut corners with the Talmud"): EVERY ROW OF THE SHELF — Talmud, Mishnah, Tosefta, the spine's books (the Sifrei and its kin), Onkelos — IS READ WHOLE BEFORE ITS VERDICT IS TYPED. No character cap on a row, ever; no verdict from a row's opening; a range read is every row of the range whole. The four-run rule's "short cut" clause (2026-09-16) is STRUCK: a docket takes as many runs as its whole reading needs (the run count yields, the clean point after each run stands); a prior sitting's SCRIPT is still derived by sed and read where it differs — that economy is on our own text, never on the shelf's. THE CUTS TAKEN ARE REREAD WHOLE AND CORRECTED: a corrected verdict on an uncommitted docket by an overlay in its part (the cut's verdict kept beside it as the record); a correction to a committed ledger or docket by an APPENDED section (append-only); a cell typed from a cut row retyped from the whole one. THE MEASURE THAT RULED IT: the first forty rows of chapter 6's docket reread whole against their 170-character verdicts — two verdicts wrong, one row carrying another row's content, nine notes short of the row's point.

The cuts measured and the fix's order: the map's tail section "THE WHOLE-ROW RULE"; the memory talmud-rows-whole.md; the state doc's #191 addendum 1.

## 40. ADDENDUM (2026-09-17, THE DEUTERONOMY WALK sitting 4b — THE COMPILE OF CHAPTER 6, Deuteronomy 6:1-25 COMPILED AND ON THE TAPE in four runs; the owner: "Go", "One more run", "Next go", "Ok go"; the state doc's #193 addendum 1)

THE SITTING RAN IN THE COMPILE SHAPE IN FOUR RUNS (section 5; "Sitting 3b" the form; the whole-row rule of §39 ruled between its runs 2 and 3 and paid
inside it): World/step9/DEUTERONOMY_WALK.md "Sitting 4b" (the design, written before any code) and "Sitting 4b — AS BUILT" (the departures and the
ten lessons). THE STATE: cold_run_hear_o_israel.py the 61st runner (42/42 — six cells, eighteen DATA rows, the readback's seven rows, fourteen exam
persons), law_hear_o_israel the 66th daemon (given_at Deut 6:4, installed_by boot; 66 daemons, 454 functions), event_vocabulary +3 (1125), effect_vocabulary
+2 (1025), dependency_dispositions +12 edges +4 pointers (545 edges, 199 pointers on file); THE TAPE 10/10 WITH THE REST ON ITS FIRST RUN — RUN (1304, 96,
88, 0, 12, 1595, 37, 319, the four pairs, 127) as predicted, PREVIOUS_RUN 3b's EXACTLY (no declared delta), NEWEST_RUNNER hear_o_israel, markers 167
UNMOVED, entities 319, closes 127, the population table 148, CO1-CO9 MATCH; the docket logic/oral_triage/deu_06_vaetchanan_exam_2026-09-17.md (747 rows —
link 95 / topic 652; LAW 346; credited 174; EVERY ROW READ WHOLE). THE GATES: the probe suites census 224/224, installation 6/6 (I5 66), readback 15/15 (Q13-Q15 the third form), register 7/7, clock 22/22, sequence 4/4, view 6/6, population 9/9, journal 7/7, cursor 6/6, large_letter 6/6, checkpoint 7/7; the daemon gate GREEN (66 daemons, 454 functions WRAPPED); the dependency gate GREEN (545 edges and 199 pointers on file — the link census reference 526 / transfer 48 / hypothesis 9 / none 161; required 264 edges and 200 pointers, live import edges 392); build_world ALL GREEN (220 units, standing 2203, hash 8b8fff1fa28953af unmoved — no freeze this sitting); the journal gate GREEN twice — before and after the sweep (12 kinds, 9674 rows in the index); THE REGISTER GATE --strict GREEN (DECLARED 100, DEBT 0, FAILS 0 — no seat in chapter 6: the finder blind to 6:25 as measured; Deut 5:12, 5:16, 5:32 CHAPTER and 4:45 DAEMONS unmoved); the positions table 235 checkpoints over 169 pauses (CO1-CO9 in it; checkpoint_probes 7/7 after the rebuild); the sweep 61/61 at 6,618 graded cells; the home-path gate GREEN.

WHAT THE SITTING FOUND (RESEARCH_LOG 2026-09-17, the compile entry): THE READBACK'S THIRD FORM — a retelling inside a law, the grades the cell's verdicts
(T1), the shelf's own seat at Pesachim 116a; THE SHEMA'S LAW compiled for the first time at the chapter's own day, STATUTE BY FORM (the stitcher's
register test); THE RECEIPT WITHOUT THE NAME — the finder blind at 6:25, asserted by calling it; THE COMPARTMENTS A PARAMETER over the spellings' open
row; THE CENSUS AND A HOMOGRAPH ("eat" at 6:11 FALSE; the oath's pointers not demanded); THE WHOLE-ROW MEASURE (one verdict in ten wrong at 170
characters; a cut row ends before the answer). THE ELEVEN LESSONS in the map's AS BUILT (the eleventh from the gates step: two probes retyped from the
chain's first print — Q13's key, H5's exhibit moved by the tape's growth).

THE FILES CHANGED BY 4b: World/step9/cold_run_hear_o_israel.py (new), cold_run_sequence.py (the two lines under "# ---- Deut 6 ----", the literals,
CO1-CO9), cold_run_obey_horeb.py (the fifth-compartment cell retyped under the rule), event_vocabulary.yaml, effect_vocabulary.yaml,
daemon_dispositions.yaml, dependency_dispositions.yaml (the span, twelve edges, four pointers), readback_probes.py (Q13-Q15; Q13 retyped at RUN 4),
large_letter_probes.py (H5 retyped — the creed classed, the hypothesis parked), installation_probes.py (I5 66), checkpoint_positions.yaml (rebuilt — 235), DAEMON_INDEX.md and DEPENDENCY_INDEX.md (regenerated), the docket (new; rewritten whole), the four
appended REREAD WHOLE sections (the chapter-6 ledger, the 3b, 2b and 1b dockets), the forms folder (copy_ch6b_forms.py), the records (the map, COMPILE_DEBT,
MIDDOT, MISHNAH_TOPICS, RESEARCH_LOG, THE_STEPS, THE_BRIEFING, THE_LOOP, RESUME, RECORD_FORMS, the recovery page, this file, the state doc, memory).
NOT COMMITTED — the tree uncommitted since a7955cc; commit on the owner's word only.

NEXT ON THE RULING: the commit on the owner's word; then CHAPTER 7's READING (7:1-26 — the seven nations and the ban, the chosen people, the reward; the
reading shape in four runs, every row whole). ON THE TABLE, NOT A RULING: the Decalogue-schema sitting — on the owner's word.
