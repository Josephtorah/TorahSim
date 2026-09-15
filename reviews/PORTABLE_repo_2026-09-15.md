# THE PORTABLE REPO — the rename to TorahSim and the root computed from each file's own place (2026-09-15)

The owner's words: "If I change the name from Torah grok to something else will it break the code" (yes — measured); "How does it work if
someone else downloads this repo, what directory will it use" (it does not run — measured); "Let's compact then do this rename and relative
path to make it work as a clone. Get ready"; the name: "TorahSim"; the shelf: "Yes create a fetch script"; and "commit push" first
(d398857). The sitting runs on the loop's own order: the measurements, this design before a line moves, the probes to FAIL, the pass,
every gate, the records, then the rename itself as the last act.

## THE MEASUREMENTS (2026-09-15, by grep, git and a scan of every string literal in the code)

- The absolute path <repo-old> is written into 352 Python files at 474 places: all 57 sweep runners, the tape
  (cold_run_sequence.py: the registry at two places, the store, the dispositions), World/build_world.py (REPO), three other World/step9
  tools, 18 tools under logic/, 285 forms under World/step9/forms_numbers_walk (the walk's templates — reused, so rewritten too), and 83
  non-form Python files in all; six non-Python carriers outside the forms (LEV_CODE.html, RESEARCH_LOG.md, the state doc, the recovery file,
  World/RESUME.md, .claude/settings.local.json). The engine, the journal, the stepper, the board, ask.py, corpus_world.py and CORPUS_TRUTH.py
  carry no absolute path.
- The symlink <world-link> -> <repo-old>/World. The remote https://github.com/Josephtorah/Torah_Grok.git. The memory
  folder ~/.claude/projects/<project-folder-old> is named after the working directory; ~/.claude/projects/<project-folder> already
  exists (the retired public site's two sessions and 14 memory files, 52 MB) — its memory is archived, never merged.
- THE DATA WALLS: of the 249 data paths the non-form code opens, eight are on disk but untracked — one matters: elijah_docket/tanakh.sqlite
  (26 MB; 59 references in non-form code, 121 with the forms), inside the nested elijah_docket git (a gitlink, no remote); the rest are the
  never-commit set, old-era tools' databases, and derived files. The shelf Data/sefaria_export (2.3 GB, 6,364 files) is gitignored but for
  MIRROR_MANIFEST.txt, whose 6,412 fetched rows name each file's source path in Sefaria's export (134 rows name files no longer on disk;
  89 rows are marked skip; every file on disk has a row). World/journal/data is derived. A fresh clone: 3,552 tracked files, no sitting.
- The name TorahSim is free on this Mac (the owner: "I deleted the torahsim that was on there") and on GitHub under Josephtorah (the old
  TorahCode repository's redirect points at a TorahSim that no longer resolves).

## THE DECISIONS

P1 ONE ROOT FROM THE FILE'S OWN PLACE. Every Python file under the repo (the forms included — they are the walk's templates) computes
   `_ROOT` from its own `__file__` (the pattern the World/step9 tools already use), and every string literal that carries the old absolute
   path becomes `_ROOT + '<the rest>'` (a literal that is only the path becomes `_ROOT`); `import os` is added where absent, after the
   docstring; comments and docstrings keep their text with the new absolute name. ONE SCRIPT does the pass — logic/solo_tools/portable_pass.py,
   kept as the record of it: `--dry` counts, the pass rewrites, a second run finds nothing to do. The six non-Python carriers: the shell
   forms compute their root with `git rev-parse --show-toplevel`; the two records and RESEARCH_LOG keep their history (append-only — the old
   paths in old entries stand) and the recovery file's LAWS (section 3: the staging form, the cd rule) are amended by appending;
   World/RESUME.md's head note and LEV_CODE.html carry the new name; .claude/settings.local.json's four permission lines carry the new path.
P2 THE STORE LIVES IN THE REPO. elijah_docket/tanakh.sqlite is copied to Data/tanakh.sqlite and TRACKED (a .gitignore exception); every
   reference in code — the 121 — is rewritten to `_ROOT + '/Data/tanakh.sqlite'` by the same pass; the nested elijah_docket stays as it is
   (the docket's own research; its gitlink never staged) with its own copy; the memory note names the new home.
P3 THE SHELF BY A FETCH SCRIPT. Data/fetch_shelf.py: reads Data/sefaria_export/MIRROR_MANIFEST.txt — REGENERATED in this pass by script as
   `source path | destination | bytes | sha256` for every file on disk (6,363 rows; the 134 rows of files no longer on disk dropped; the skip
   rows kept) — and fetches each missing or mismatched file from https://raw.githubusercontent.com/Sefaria/Sefaria-Export/master/<source>;
   `--check` verifies every file's size and hash with no network; `--sample N` fetches N files into a temporary folder and compares their
   hashes (the network proven on a sample, never on the whole 2.3 GB). The manifest is the check.
P4 THE PROBE IS A CLONE AT ANOTHER PATH. World/step9/portable_probes.py: T1 no literal of the old absolute path in any tracked .py, .sh or
   .json; T2 every tracked .py compiles; T3 the tracked tree copied to a temporary path (the store with it, the shelf symlinked, no derived
   data) and run THERE with that path as the working directory — one runner green, World/build_world.py building the one database from
   nothing and reconciling ALL GREEN, the tape 10/10, the board's gate and the positions' gate GREEN; T4 the fetch script's --check on the
   real shelf, every file matching; T5 the fetch script's --sample 2 matching Sefaria's bytes. Today T1 and T3 fail at the first absolute
   path, T4 and T5 fail for want of the script and the manifest's hashes.
P5 THE ORDER AND THE LAST ACT. The probes to fail → the pass (dry, then applied) → the store copied and tracked → the manifest regenerated
   and the fetch script → the probes green → the standing gates in place (the sweep 57/57 in the background, the journal gate, the register
   gate, every probe file) → SETUP.md at the root (a clone's steps: clone, fetch the shelf, build the database, run the tape, open the board)
   → the records → the owner's "commit push" → the GitHub rename (`gh repo rename TorahSim`, the remote re-pointed, the push form amended)
   → the memory folder copied to ~/.claude/projects/<project-folder>/memory (the old site's memory archived beside it) → the folder
   renamed and the symlink remade AS THE LAST ACT of the session, on the owner's word, after which he restarts Claude Code in
   <repo>. Nothing here touches the corpus, the hash, the units, the ledgers or the engine.

## AMENDED BY THE RUN (2026-09-15, before the records — what the probes and the clone taught, each fixed the same hour)

- P2 AMENDED, A SECOND STORE: the runners also open torah_grok.SNAPSHOT-main-51801ca.sqlite at the root (154 MB; 22 non-form files, 53
  forms) — my scan had missed it because its literal ends in `?mode=ro`, not `.sqlite`. GitHub refuses a file over 100 MB, so it cannot
  ride in git: it is published as an asset of the TorahSim release `stores-2026-09-15` and fetched by `python3 Data/fetch_shelf.py --stores`
  against Data/STORES_MANIFEST.txt (asset | destination | bytes | sha256). The 3.5 GB torah_grok.sqlite is read only by the July-August
  era's tools (build_db.py, export_web.py, the index_* scripts, the law-era drafts) — no gate, no runner — and is not shipped.
- P3 AMENDED, THE SOURCE MOVED: in September 2026 Sefaria moved its text files out of the Sefaria-Export git repository (the history
  rewritten, the old commits unreachable, the raw URLs 404) into a public bucket, https://storage.googleapis.com/sefaria-export/<source
  path>, the same paths the manifest carries; the fetch script reads the bucket; three sampled files match the mirror byte for byte.
- THE EXEC'D NAMESPACE: the Numbers runners exec the tape's INK block from the sequence file's source into a namespace of their own; the
  block now reads the store through `_ROOT`, which that namespace lacked — every runner and form that execs it (27 files) sets `_ROOT` in
  the namespace first. A path is an expression now, and an exec'd source needs the name the expression uses.
- THE PATH BUILT FROM PIECES: `os.path.join(ROOT, 'elijah_docket', 'tanakh.sqlite')` carries the store's path in two literals, so the
  pass's substring rule never saw it — three files (the register gate, the dependency census, the guardians runner) rewritten by a second
  rule; the clone's tape then 10/10.
- THE THREE FORMS THAT NEVER COMPILED (an unterminated string literal each) had their paths renamed by text, and say so in a first line.

## AS BUILT (2026-09-15; every number from a print)

THE PASS: logic/solo_tools/portable_pass.py --dry then --apply — 367 files rewritten: 558 Python occurrences (code strings 462, docstrings
  1, comments 1, f-string pieces 73, store-only 21) and 44 shell occurrences in 16 scripts; a second run finds 0; three forms that never
  compiled renamed by text; then the two rules the run taught (27 exec sites given `_ROOT`; three path-from-pieces files). The staged diff:
  386 files, 8,386 insertions, 7,234 deletions; 7 files new (SETUP.md, Data/tanakh.sqlite, Data/STORES_MANIFEST.txt, Data/fetch_shelf.py,
  logic/solo_tools/portable_pass.py, World/step9/portable_probes.py, this map).
THE STORES: Data/tanakh.sqlite copied from the nested folder and tracked (26,574,848 bytes; the .gitignore exception); the snapshot store
  torah_grok.SNAPSHOT-main-51801ca.sqlite (153,755,648 bytes, sha256 55b577bd06f21f69…) named in Data/STORES_MANIFEST.txt for the release
  `stores-2026-09-15`, `fetch_shelf.py --stores --check` GREEN on this machine.
THE SHELF: the manifest regenerated — 6,363 files hashed, 89 skip rows kept, 134 stale rows dropped; `--check` GREEN; `--sample 3` and
  `--sample 2` against Sefaria's bucket GREEN, every sampled file byte for byte.
THE PROBES: portable_probes.py 0/5 → 5/5 — T3's clone at a temporary path ran a runner, built the one database from nothing (ALL GREEN),
  ran the tape to 10/10, passed the board's and the positions' gates. T2 first failed on my own probe (a compile method), fixed.
THE GATES IN PLACE: the sweep 57/57 at 6,378 graded cells (a first sweep, started before the exec fix, died on that very error and was
  rerun); the journal gate GREEN (the fold layer 12 kinds, 9,574 rows; the hash 8b8fff1fa28953af); the register gate GREEN. The lint 0
  on every new file.
THE RECORDS: this map; SETUP.md; THE_STEPS "Where to look"; THE_BRIEFING; World/README.md and World/RESUME.md; the recovery file's laws
  (section 3) and section 28; the state doc's #179; memory.
THE SECOND SCAN (the owner: "can you scan each file again for links that we might have missed" — every tracked file, every type, eight
  forms of the old name): the old memory-folder segment <project-folder-old> stood in 81 scripts (the record-writing forms and their
  scratchpad paths) — renamed to <project-folder>; the guardians runner reached the store through the FOLDER'S NAME
  (`'..', '..', 'Torah_Grok', ...`) — now two levels up to the root, whatever its name; LEV_CODE.html's two listed path literals and two
  comments renamed. LEFT AS HISTORY, NAMED: the old Mac's zip name and a dead July scratchpad path (<old-mac-project-folder>),
  a July artifact's provenance text, the law-era epub builders' creator name, two docstrings that say "runs in Torah_Grok", the baked
  epubs, a tracked session output, and every record (the state doc, the recovery file, RESEARCH_LOG, the ledgers — append-only).
WHAT REMAINS, IN ORDER, ON THE OWNER'S WORD: "commit push" → `gh repo rename TorahSim` and the remote → the release `stores-2026-09-15`
  with the snapshot store as its asset (`fetch_shelf.py --stores` then real for a clone) → the memory folder copied to
  ~/.claude/projects/<project-folder>/memory (the old site's memory archived beside it) → .claude/settings.local.json's four lines →
  the folder renamed and the symlink remade as the last act → the owner restarts Claude Code in <repo>.

## NOT IN THIS SITTING, NAMED
The never-commit set stays where it is; the old-era tools (build_db.py, fetch_oral_texts.py, the SNAPSHOT readers) keep their databases as
they are (untracked, unread by any gate); the nested elijah_docket is not merged into the repo; the public site is not rebuilt.
