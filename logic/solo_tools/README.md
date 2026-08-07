# solo_tools — the solo-era derivation pipeline

One unit, start to finish (run everything from anywhere; scripts resolve
the repo root themselves):

```
# 0. PRE-STAGE — one call, everything: shape, token map, volitives,
#    debuts, every in-span career (no hand-picked strong lists)
python3 logic/solo_tools/prestage.py Gen 31:22-31:54 > /tmp/prestage_gen54.txt

# 1. AUTHOR the content module: copy an existing module from
#    logic/solo_tools/content/ as a template; set UID/BOOK/SPAN/META/
#    DRAFT_NOTE/STEPS/SCENS (+EXTRA_SUBS for span-specific translit).
#    Scenario bookkeeping (queue depth, REGISTRY counts, WORLD installs)
#    is CHECKED BY SIMULATION at build time — write it, but the builder
#    will catch any drift.

# 2. BUILD (draft yaml lands in logic/units/<UID>.yaml)
python3 logic/solo_tools/build_unit.py logic/solo_tools/content/<UID>.py

# 3. VERIFY text layer (independent recomputation) + PREFLIGHT
python3 logic/solo_tools/verify_text.py <UID>
python3 logic/solo_tools/preflight.py <UID>

# 4. LINT for absolutes, DB-check or fence every listed line BEFORE review
python3 logic/solo_tools/superlative_lint.py logic/units/<UID>.yaml

# 5. ADVERSARIAL REVIEW (standing law): spawn a fresh-context subagent
#    pointed at logic/solo_tools/REVIEW_BRIEF.md + the unit path + a
#    boldest-claims list. FAIL -> amend the CONTENT MODULE (never the
#    yaml directly), rebuild (2), re-verify (3), send the diff back for
#    AMENDMENTS CONFIRMED — PASS FOR FREEZE.

# 6. FREEZE RITUAL — one idempotent call: text check, flip, frozen run,
#    parallel full regression, py render + self-proof, undated HTML,
#    both indexes, ALL_UNITS insert + corpus proof
python3 logic/solo_tools/freeze_ritual.py <UID>

# 7. MANUAL (judgment): watchlist in logic/middot_scan/, state-doc
#    update (PROMPT_continue_*), owner's commit word.
```

Conventions encoded in the builder (do not re-implement by hand):
plain `he:` = accents+meteg stripped, slashes stripped, maqqef ־ per
snapshot; tree halves = accented, slash-stripped, space-joined, split at
etnachta with earliest-strongest-disjunctive fallback (gen_03 1:13);
ketiv (unvocalized written-form) tokens appear in `he` lines, never in
translit (gen_43 25:23); scenario value_he = accented, maqqef→space.

Translit cleanup: `subs.py` GLOBAL_SUBS (append-only, unambiguous forms
only) + per-module EXTRA_SUBS for context-dependent tokens (e.g. et-y =
oti or iti) and for pinning a frozen unit's historical form.

Reproducibility: every frozen solo-era unit's content module lives in
`content/`; `build_unit.py` regenerates its yaml byte-identically
(modulo the status/dry_run flip). Proven for gen_51/52/53 on
2026-08-07.
