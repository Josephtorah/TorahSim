# THE RECOVERY PAGE — a new thread's ONE READ (rewritten at every sitting's close; under 10 KB)

THE RULE OF THIS PAGE (the owner, 2026-09-16: "go"): a new thread or the first
sitting after a compaction reads THIS PAGE, the map's NEWEST section (World/step9/DEUTERONOMY_WALK.md), and the memory index — nothing else
unasked. The history (sections 1-35 that older records cite as "the recovery file's section N") is RECOVERY_addenda_2026-09-12.md beside
this file, append-only, opened on purpose by the READ ON DEMAND list below. This page is REWRITTEN whole at each sitting's close (a record on
the sheet World/step9/RECORD_FORMS.md), never appended.

## 1. WHO AND WHAT
The owner is Brian LeBlanc (never "Ben"; GitHub Josephtorah). He is terse. Replies SHORT, in PLAIN PICTURES; depth in the files; CHAPTER
NUMBERS, never portion names; decisions ONE AT A TIME. He compacts at ~700k-900k tokens; a clean compaction point is announced at every milestone. The mission: the 24 books are the PROGRAM, the Talmud holds the COMPILE RULES, the Mishnah is the ANSWER SHEET; ONE world runs on a
tape of events in verse order; every verse adds a line or installs a law (a daemon) writing EFFECTS on ledgers; LAW IS CODE, NARRATIVE IS
EVERYTHING ELSE IN A COMPUTER PROGRAM (his frame, 2026-09-16). The repo <repo> = /Users/Shared/TorahSim, public under CC0 at
github.com/Josephtorah/TorahSim.

## 2. WHERE IT STANDS (2026-09-16, after THE DEUTERONOMY WALK sitting 2b; the state doc's #186 + addendum 1)
- NUMBERS CLOSED (1:1-36:13 on the tape). DEUTERONOMY 1:1-4:49 READ, FROZEN, COMPILED AND ON THE TAPE (sittings 1, 1b, 2, 2b; the map).
- 218 frozen units, standing 2191, hash 8b8fff1fa28953af. 59 runners, 64 daemons, 441 functions; registries 1119 kinds / 1019 effects.
- THE TAPE: RUN (1300, 96, 88, 0, 12, 1588, 35, 319, the four pairs, 126); markers 165; entities 319; closes 126; the population table 148;
  the counter at (40, 11, 1). The sweep 59/59 at 6,527 cells; every probe suite and gate GREEN; the register gate DECLARED 100 / DEBT 0.
- LAST COMMIT b8b721d (2026-09-16, NOT pushed). UNCOMMITTED: sittings 2 and 2b, the three cost tools, this page. Commit on his word only.
- ON THE TABLE, NOT A RULING: the Decalogue as a SCHEMA over the law (the state doc's #185 addendum 1).
- NEXT ON THE RULING: sitting 3 — CHAPTER 5's reading; FIRST measure the export's thirty-verse chapter 5 against the DB's thirty-three.

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
- THE COST RULES (2026-09-16): every tool call re-sends the whole conversation — the bill is the NUMBER OF TURNS. NEVER POLL a background job
  (run_in_background; the harness notifies). The gates step is ONE chain: `sh World/step9/gates_chain.sh <out_dir>`, its SUMMARY read once.
  ONE fast check before the tape: `python3 World/step9/checkpoint_check.py <PREFIX>`. The records from the sheet in ONE call. Batch
  independent reads into one call.
- NEVER a probe or a second stepper under the live session's source name; the journal gate never concurrently with the sweep; after any
  freeze `python3 World/build_world.py` before the journal gate. The register gate `--strict` at every compile sitting's gates step.
- THE LINK REVIEW LAW: no link of our own unless a teacher taught it (REFERENCE vs TRANSFER vs a labeled HYPOTHESIS; every edge carries
  `link:`). THE EFFECTS LAW: verdicts write ledger EFFECTS from effect_vocabulary.yaml, never the event stream. CODE/DATA SEPARATION: Mishnah
  and Talmud rows are DATA. THE COMPILER LAW: MOVE_CATALOG.md updated UNPROMPTED; findings AUTO-SEAT; one cold function per law span (five
  motions + WRAP); COMPILE_DEBT.md the checklist. A MIDDAH CODE IS CHECKED IN MIDDOT.md BEFORE IT IS TYPED. THE ENGLISH SUPPLIES THE MISHNAH.
- THE GATES' READING RULES: the daemon gate reads LITERAL submits only; `import cold_run_X` in the sequence file is the live edge; the token
  census can demand an edge the runner never imports (CALL / VIA / FALSE / OWED / PARAMETER / REVERSE / RUN_CITATION, a why and a link);
  the honest-pairing guard reads literals only; a retype covers every line of a literal.
- THE RETELLING RULES (the readback, THE_LOOP step 6): a retelling is a REFERENCE ROW graded against the tape, never a second act; an act
  told only in the retelling is written ONCE at its own day by a RETROGRADE marker; a retrograde stretch runs to the NEXT marker (a forward
  marker closes it; a chapter after a stretch opens with one); a disagreement an OPEN row; a receipt a run citation.
- Tool facts: zsh globs `====` (use `----`); importing cold_run_sequence costs 40-90 s. The peer thread is never a ruling.

## 4. THE FILE MAP
Root: THE_STEPS.md (Brian's plain-language process; its vocabulary is ours), THE_BRIEFING.md (the big picture + the scoreboard, newest
first), THE_WORLD.md, RESEARCH_LOG.md, SETUP.md. logic/: MIDDOT.md, MOVE_CATALOG.md, MISHNAH_TOPICS.md, CORE_SHELF.md, units/, py_units/,
oral_triage/ (ledgers + dockets), corpus/CORPUS_TRUTH.py, solo_tools/, pre_logic_methods_2026-07-28/ (the state doc
PROMPT_continue_solo_era_2026-08-06.md — its newest COMPACTION POINT; this page; the addenda).
World/step9/: DEUTERONOMY_WALK.md (the walk's map — every sitting's design + AS BUILT), NUMBERS_WALK.md, THE_LOOP.md, THE_TENT.md,
COMPILE_DEBT.md, RECORD_FORMS.md (the records sheet), SEQUENTIAL_RUN.md, world_engine.py, cold_run_sequence.py (THE TAPE), cold_run_<span>.py
(59 runners; cold_run_obey_horeb.py the newest form), the registries (event_vocabulary, effect_vocabulary, daemon_dispositions,
dependency_dispositions, register_dispositions, calendar_parameters, population_schema), the gates (daemon_census, dependency_census,
register_census --strict, world_journal --gate, run_cold_all; gates_chain.sh runs them all), the probes (*_probes.py), checkpoint_check.py,
checkpoint_positions.py, world_stepper.py, world_board.py, forms_deuteronomy_walk/ (the walk's scripts and prints — copy the newest sitting's
form to the scratchpad). World/journal/data/world.sqlite the one database; Data/tanakh.sqlite the text store. Memory: <memory>/ — MEMORY.md the
index; deuteronomy-walk.md; cost-rules-no-polling.md; step9-exam-era.md.

## 5. THE SITTING SHAPES (the long forms: the addenda's section 5; the newest instances: the map's "Sitting 2" and "Sitting 2b")
THE READING: measure first (Onkelos whole + the spine by position; the parser on every number verse) → the ink asserts → the rows → the ledger
with coverage COMPUTED → the unit yaml + manifest → the claims seated → the fold predicted and matched → build_world → the records from the sheet.
THE COMPILE: the measurements → THE DESIGN in the map before any code → probes to FAIL → the docket by the union rule → the types by script →
the gates to FAIL → the runner (parts; the fast checker; the guard; CASES generated; scene and narrative predicted) → the recorder →
the stitcher → the literals and checkpoints → `checkpoint_check.py <PREFIX>` (every fault in one print) → the
tape 10/10 with THE REST → `gates_chain.sh` in the background (one summary) → the records from the sheet in one call.

## 6. READ ON DEMAND (open these only when the sitting touches the subject)
- The whole standing-law text, the old staging form, the corpus bake: the addenda §3-4. The two sitting shapes in full: the addenda §5.
- THE LOOP (the sink, the index, installation, the cursor, scenarios, the readback, the stepper, the port, the board, D1-D33): THE_LOOP.md.
- Numbers' sittings and lessons: NUMBERS_WALK.md; the addenda §8-17. The project review: §18.
- The one database (D7's merge), the portable repo: the addenda §23-24, §27-29; reviews/PORTABLE_repo_2026-09-15.md.
- Deuteronomy's sittings: the map; the addenda §31-34. The cost cuts: §35 and memory cost-rules-no-polling.md.
- The Decalogue-schema question: the state doc's #185 addendum 1 and the map's tail (ON THE TABLE).
- THE_STEPS Step 2, Step 5 and the compiler-law block: before a READING sitting's ledger is written.

## 7. IF THIS COMPACTS MID-SITTING
The state doc's newest COMPACTION POINT names the step in flight; the scratchpad holds the sitting's scripts. Reread this page, the map's
newest section, the memory index — then continue the step named.
