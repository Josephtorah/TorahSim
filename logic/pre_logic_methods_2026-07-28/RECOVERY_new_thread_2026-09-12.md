# THE RECOVERY PAGE — a new thread's ONE READ (rewritten at every sitting's close; under 10 KB)

THE RULE OF THIS PAGE (the owner, 2026-09-16: "go"): a new thread or the first
sitting after a compaction reads THIS PAGE, the map's NEWEST section (World/step9/DEUTERONOMY_WALK.md), and the memory index — nothing else
unasked. The history (sections 1-35 that older records cite as "the recovery file's section N") is RECOVERY_addenda_2026-09-12.md beside
this file, append-only, opened on purpose by the READ ON DEMAND list below. This page is REWRITTEN whole at each sitting's close (a record on
the sheet World/step9/RECORD_FORMS.md), never appended.

## 1. WHO AND WHAT
The owner is Brian LeBlanc (never "Ben"; GitHub Josephtorah). He is terse. Replies SHORT, in PLAIN PICTURES; depth in the files; CHAPTER
NUMBERS, never portion names; decisions ONE AT A TIME. He compacts after each RUN; a clean point is announced at every run's end. The mission: the 24 books are the PROGRAM, the Talmud holds the COMPILE RULES, the Mishnah is the ANSWER SHEET; ONE world runs on a
tape of events in verse order; every verse adds a line or installs a law (a daemon) writing EFFECTS on ledgers; LAW IS CODE, NARRATIVE IS
EVERYTHING ELSE IN A COMPUTER PROGRAM (his frame, 2026-09-16). The repo <repo> = /Users/Shared/TorahSim, public under CC0 at
github.com/Josephtorah/TorahSim.

## 2. WHERE IT STANDS (2026-09-18, after 5b; the state doc #195 addendum 9)
- NUMBERS CLOSED. DEUTERONOMY 1:1-7:26 READ, FROZEN, COMPILED AND ON THE TAPE (1-6 at 64a8362, PUSHED; chapter 7 sittings 5 and 5b).
- 221 frozen units, standing 2209, hash 8b8fff1fa28953af. 62 runners, 67 daemons, 460 functions; registries 1129 kinds / 1029 effects.
- THE TAPE at RUN (1307, 96, 88, 0, 12, 1602, 38, 319, the four pairs, 127), markers 167, closes 127; the sweep 62/62; every gate GREEN;
  the register gate DECLARED 100 / DEBT 0. The readback's fourth form (5b): the laws' form on the kin's cells.
- Uncommitted since 64a8362: sittings 5 and 5b, the tutorial, the design thread; the message at <scratch>/commit_msg_ch7.txt.
- NEXT ON HIS WORD: the commit; then CHAPTER 8 (8:1-20) or the schema sitting (on the table).

## 3. THE STANDING LAWS (owner-ruled; verbatim in spirit — the long forms in the addenda's section 3)
- NO AGENTS EVER; main thread only; a sitting opens on his word. DISCUSSION IS NOT A RULING. READ THEN COMPILE PER PORTION, never read ahead.
- HEBREW NEVER WITHOUT ITS ENGLISH INLINE, EVERYWHERE, EVER — the script first, the gloss within ninety characters; book names in FULL. The
  lint `python3 logic/solo_tools/gloss_lint.py <file>`; BASELINES: the state doc 146, THE_STEPS 1, MIDDOT 1, THE_WORLD 5, STAMP_LEDGER 1,
  MOVE_CATALOG 5, RESEARCH_LOG 52, MEMORY.md 4, cold_run_sequence.py 7, census_probes.py 1, world_board.html 6; everything else 0.
- LEDGERS ARE APPEND-ONLY; registries rewritable with the gates green. COVERAGE IS COMPUTED, NEVER RECITED; a gate's FAIL is READ; retype from
  the print. NEVER Write a record without ls first; AN APPEND BUILDS ITS WHOLE TEXT BEFORE OPENING THE FILE.
- NO MACHINE USERNAME, NO HOME PATH anywhere in the project or the memory (markers <repo> <scratch> <memory> <home>; the gate
  `python3 logic/solo_tools/scrub_home_paths.py --check` is the pre-commit hook). NEVER an absolute repo path in code: repo scripts compute
  `_ROOT` from `__file__`; scratch scripts take ROOT from git (the repo's top folder), run from the repo root with PYTHONPATH the scratchpad.
- KEEP ALL RECORDS CURRENT UNPROMPTED (the sheet RECORD_FORMS.md names them); MEMORY.md under 17,000 bytes; this page rewritten.
- COMMIT ONLY ON HIS WORD: "commit push" = commit and push; "Commit" alone = no push. Staging `git add -A -- . ':!elijah_docket'
  ':!DISPOSABLE_scan/*.zip'`; `git commit -F <scratchpad file>` with the trailers Co-Authored-By: Claude Fable 5.1 <noreply@anthropic.com> and
  Claude-Session: <the session url>; push `GH=/opt/homebrew/bin/gh; $GH auth switch --user Josephtorah; git push origin main; $GH auth switch
  --user PeerloopLLC`. The never-commit set in .gitignore; elijah_docket a gitlink never staged; World/journal/data/ gitignored.
- THE COST RULES (2026-09-16): the bill is TURNS and CONTEXT. NEVER POLL a background job (the harness notifies). The gates ONE chain
  (`sh World/step9/gates_chain.sh <out_dir>`, the SUMMARY read once); ONE fast check before the tape (`checkpoint_check.py --all`); the
  records from the sheet in ONE call; independent reads batched. ⚠ A SITTING IS FOUR RUNS, a clean compaction point after each (owner-ruled
  2026-09-16): (1) the rereads, the measurements, the design; (2) the docket; (3) the types, the runner, the stitch, the tape to 10/10; (4) the
  gates chain, the records, the forms — each near 150-200k, never 600k; a reading sitting the same; a prior form by sed, read where it differs.
  ⚠ EVERY SHELF ROW READ WHOLE, NEVER A CUT (owner-ruled 2026-09-17); a docket takes the runs it needs.
- NEVER a probe or a second stepper under the live session's source name; the journal gate never concurrently with the sweep; after any
  freeze `python3 World/build_world.py` before the journal gate. The register gate `--strict` at every compile sitting's gates step.
- THE LINK REVIEW LAW: no link of our own unless a teacher taught it (REFERENCE vs TRANSFER vs a labeled HYPOTHESIS; every edge carries
  `link:`). THE EFFECTS LAW: verdicts write ledger EFFECTS from effect_vocabulary.yaml, never the event stream. CODE/DATA SEPARATION: Mishnah
  and Talmud rows are DATA. THE COMPILER LAW: MOVE_CATALOG.md updated UNPROMPTED; findings AUTO-SEAT; one cold function per law span (five
  motions + WRAP); COMPILE_DEBT.md the checklist. A MIDDAH CODE IS CHECKED IN MIDDOT.md BEFORE IT IS TYPED. THE ENGLISH SUPPLIES THE MISHNAH.
- THE GATES READ LITERALS: the daemon gate literal submits; `import cold_run_X` in the sequence file the live edge; the token census demands
  edges the runner never imports (CALL / VIA / FALSE / OWED / PARAMETER / REVERSE / RUN_CITATION, a why and a link); a retype covers every
  line of a literal.
- THE RETELLING RULES (the readback, THE_LOOP step 6): a retelling is a REFERENCE ROW graded against the tape, never a second act; an act
  told only in the retelling is written ONCE at its own day by a RETROGRADE marker; a retrograde stretch runs to the NEXT marker (a forward
  marker closes it; a chapter after a stretch opens with one); a disagreement an OPEN row; a receipt a run citation.
- zsh globs `====` (use `----`); importing cold_run_sequence costs 40-90 s. The peer thread is never a ruling.

## 4. THE FILE MAP
Root: THE_STEPS.md (Brian's plain-language process; its vocabulary is ours), THE_BRIEFING.md (the big picture + the scoreboard, newest
first), THE_WORLD.md, RESEARCH_LOG.md, SETUP.md. logic/: MIDDOT.md, MOVE_CATALOG.md, MISHNAH_TOPICS.md, CORE_SHELF.md, units/, py_units/,
oral_triage/ (ledgers + dockets), corpus/CORPUS_TRUTH.py, solo_tools/, pre_logic_methods_2026-07-28/ (the state doc
PROMPT_continue_solo_era_2026-08-06.md — its newest COMPACTION POINT; this page; the addenda).
World/step9/: DEUTERONOMY_WALK.md (the walk's map — every sitting's design + AS BUILT), NUMBERS_WALK.md, THE_LOOP.md, THE_TENT.md,
COMPILE_DEBT.md, RECORD_FORMS.md (the records sheet), cold_run_sequence.py (THE TAPE), cold_run_<span>.py (62 runners;
cold_run_seven_nations.py the newest form), the registries (*_vocabulary.yaml, *_dispositions.yaml, calendar_parameters, population_schema),
the gates (daemon_census, dependency_census, register_census --strict, world_journal --gate, run_cold_all — gates_chain.sh runs them all), the
probes (*_probes.py), checkpoint_check.py, world_stepper.py, world_board.py, forms_deuteronomy_walk/ (the walk's scripts and prints — derive the
newest sitting's form by sed). World/journal/data/world.sqlite the one database; Data/tanakh.sqlite the text store. Memory: <memory>/ — MEMORY.md the
index; deuteronomy-walk.md; cost-rules-no-polling.md; step9-exam-era.md.

## 5. THE SITTING SHAPES (the long forms: the addenda's section 5; the newest instances: the map's "Sitting 5" and "Sitting 5b")
THE READING: measure first (Onkelos whole + the spine by position; the parser on every number verse) → the ink asserts → the rows → the ledger
with coverage COMPUTED → the unit yaml + manifest → the claims seated → the fold predicted and matched → build_world → the records from the sheet.
THE COMPILE: the measurements → THE DESIGN in the map before any code → probes to FAIL → the docket by the union rule → the types by script →
the gates to FAIL → the runner (parts; the fast checker; CASES generated) → the recorder → the stitcher → the literals → the tape 10/10
with THE REST → `gates_chain.sh` (one summary) → the records from the sheet in one call — the four runs' edges after the design, the docket, the tape.

## 6. READ ON DEMAND (open these only when the sitting touches the subject)
- The standing laws in full, the old staging form, the corpus bake: the addenda §3-4; the two sitting shapes in full: §5.
- THE LOOP (the sink, the index, installation, the cursor, scenarios, the readback, the stepper, the port, the board, D1-D33): THE_LOOP.md.
- Numbers' sittings and lessons: NUMBERS_WALK.md; the addenda §8-17. §18 the project review.
- The one database (D7's merge), the portable repo: the addenda §23-24, §27-29; reviews/PORTABLE_repo_2026-09-15.md.
- Deuteronomy's sittings: the map; the addenda §31-42 (§39 the whole-row rule). The cost cuts: §35.
- ON THE TABLE: the Decalogue-schema question (the state doc's #185 addendum 1); THE INSTALL HYPOTHESIS (the map's tail section).
- THE_STEPS Step 2, Step 5 and the compiler-law block: before a READING sitting's ledger is written.
- THE OTHER THREAD (Torah Grok Main — relay and illustration only): its state in the memory folder's main-thread-checkpoint-2026-09-18.md; a relayed finding is never a ruling.

## 7. IF THIS COMPACTS MID-SITTING
The state doc's newest COMPACTION POINT names the step in flight; the scratchpad holds the sitting's scripts. Reread this page, the map's
newest section, the memory index — then continue the step named.
