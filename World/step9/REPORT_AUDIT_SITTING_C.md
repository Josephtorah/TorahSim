# THE AUDIT, SITTING C — the hygiene pass (2026-09-05; owner: "go sitting c")
# Five items from the audit list; every one closed, one with a counted
# remainder. No unit's machine truth moved; no claim was added; standing
# 1715 and the hash unmoved.

**The headline is the shelf.** The Lev 11:42 large-vav truncation the
Shemini round had found and deferred was not one word. A census of every
word carrying inner markup in the shelf's own source (Data/*.xml, 39
books) against elijah_docket/tanakh.sqlite found ELEVEN, and all eleven
were cut at the mark — the parser had dropped every `<seg>` inside a
word, whatever its kind: the large letters (Lev 11:42 "belly", Num 27:5
"their judgment", Deut 6:4 "Hear" and "one"), the small letters (Isa
44:14, Jer 39:13, Prov 16:28), the suspended letters (Judg 18:30's
"Manasseh", Job 38:13 and 38:15 "the wicked", Ps 80:14 "the forest").
The Shema's two great letters were missing from the machine's copy of
the verse. All eleven restored to their source text on the owner's
standing word; the re-census reads 11 of 11 matching; the eighteen cold
runners' probes did not move (18/18, 522 cells). The nested repository
elijah_docket/ now carries the modified database uncommitted.

## 1. The honest-pairing guard covers every cold runner
compile_guards.py learned the two older table shapes — a literal dict
of expectations (the guardians' ORACLE) and expectations at call sites
(grade(fn, sheet, cells) in the Mishpatim, Lev 24, and Negaim runners;
cell(name, got, want) in the Yom Kippur runner) — and its command line
takes --table/--dict/--calls. The eleven runners that had no guard now
carry one, each with its verified count as a tripwire (14, 12, 24, 33,
27; 12; 18; 18, 20, 9; 18). 18 of 18 runners guarded; every expected
value a literal from its answer sheet.

## 2. The renders, fixed at the renderer
Every render shared one trait: the step header emitted the verse's two
Hebrew arms bare, and the tree-era EN-AID line repeated them — the
absolute glossing rule broken thousands of times (ALL_UNITS.py alone
carried 3,778 flags). Three fixes in render_unit_py.py and one in
gloss_db.py: the arms emitted in three-word chunks, each its own
‹span› ("gloss") line; a Hebrew token in a step's op name glossed; the
EN-AID repeat elided to «…»; and the gloss layer no longer takes a
tree-era structural label ("leaf 3 (ומקדשי)" — a position marker, not
English) as a word's gloss — it had been displacing the dictionary's
real English in every tree-era header. All 163 renders regenerated,
every self-proof green, ALL_UNITS.py rebuilt in its standing order and
green. Hebrew-without-English in the renders: 0. Remaining: 334 lines
in 70 renders where a machine token's gloss falls back to a
transliteration joined by hyphens (no authored English for the token)
— content work, counted, left open.

## 3. The vocabulary, linted and repaired
World/step9/vocab_lint.py — the structural lint the inline rule cannot
give a YAML: empty or placeholder glosses, a Hebrew copied into more
than four values of a dimension, a gloss in Hebrew alone. Three defects
repaired in place: round 44's generator had written the docket TOPIC as
79 values' Hebrew and gloss (a false attribution — cleared, the topic
kept as context); 57 Exodus-round query values carried "exam query
(date)"; three glosses were quote-wrapped. 1779 values, 150 dimensions,
0 flags; the 48 exam runners green after.

## 4. The four lev_04 drafts, decided
Drafts by design on the exo_21 precedent; the frozen home is
lev_04_inadvertence_case_tree (whole chapter). Written into each
draft's file with a changelog line; the owner may overrule.

## 5. The shelf repair — above; and the parse sweep
full_tanakh_parse_sweep.py had a dead output path (an earlier session's
scratchpad); it now writes to the current scratchpad. Re-run after the
repair to confirm the parse count of Step 1 (23,213 verses): RESULT
23,213 of 23,213 unique and leaf-complete under rules v3, no failures —
the eleven restored words changed no tree.

Numbers: corpus 163 · standing 1715 · hash 8b8fff1fa28953af · 18/18 cold
runners, 522 cells, all guarded · 48/48 exam runners · vocab 1779 / 0
flags · renders 163 regenerated, Hebrew-unglossed 0, translit-fallback
334 open · shelf 11/11 marked-up words matching. Both audit review files
closed; sitting D waits on Seder Olam; NUMBERS is next.
