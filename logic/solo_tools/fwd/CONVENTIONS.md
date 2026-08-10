# Forward-era toolchain — logic/solo_tools/fwd/

Moved into the repo 2026-08-10 (owner order, run-FWD-8 timing review:
kills the ~6-minute block-1 scratchpad-reload tax and version-controls
the scripts that built the frozen units). Everything runs FROM REPO
ROOT. This directory changes NO gate and NO law — it is the tooling
that feeds the unchanged pipeline in logic/solo_tools/PROCESS.md.

## The library

- `unitgen.py` — the unit skeleton generator (verse trees, tokens,
  scenarios, YAML emission — every Hebrew string sliced from the
  SNAPSHOT, never retyped). Import from a build script with:
  `import sys; sys.path.insert(0, "logic/solo_tools/fwd"); import unitgen`
- `prestage_dump.py <Book> <ch>` — the per-chapter word/accent/rank dump
  (Book = Gen/Exod/Lev/Num/Deut).
- `oral_dump.py <BookEnglish> <ch>` — Kitzur + Minchat Shai from the
  LOCAL mirror (zero fetches); other works (Rashi etc.) ad hoc, see the
  file's docstring for the mirror's ref formats.
- `probes.py` — census / adjacency / hp / he / vlen / gematria helpers.
  PROBE BEFORE CLAIMING: every manifest row's check is confirmed against
  the SNAPSHOT before it is written (the FWD-8 law — five manifests,
  65 rows, all first-run clean).

## The per-block pipeline (unchanged; see PROCESS.md for the law)

prestage → oral dump + read → probes → manifest script →
verify_claims.py (0 FAILED) → unit build script →
gloss_lint.py --no-translit → verify_text.py → preflight.py →
freeze_ritual.py → audit md. Run-end: registry/settlement appends →
corpus_world.py → CORPUS_TRUTH.py → corpus_world.py verify →
FETCHLOG → state doc.

## builds/ — the archive

Byte-exact copies of the per-unit build scripts as they ran (exo_14
template through exo_21), plus the FWD-4-era dumpers and a probe-script
example. NOTE: the archived scripts carry their original session
scratchpad `sys.path.insert` line — to re-run one, point that line at
`logic/solo_tools/fwd` instead. They are records first, templates
second; the newest pair (build_exo21_*.py) is the current convention
reference (CASE/HANDLER/STATUTE law-genre; build_exo20 for the
statute-count Decalogue pattern; build_exo17 for NAME/registry
patterns; build_exo16 for TEST/perpetual-card patterns).

## gloss_lint self-check (adopted FWD-8, the three recurring flags)

Before the first build, sweep authored prose for: (1) hyphenated
compounds that scan as transliteration — use Hebrew script with an
inline English gloss instead; (2) a jargon word's FIRST occurrence
(masorah, midrash, maqqef...) without a gloss marker within the same
sentence — the linter wants `(`, a quote, `=`, or `, the/a/an`
within ~90 chars; (3) any bare Hebrew run without `("...")` right
after it. Every Hebrew span everywhere carries inline English —
absolute owner rule.
