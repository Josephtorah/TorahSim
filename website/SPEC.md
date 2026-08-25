# SPEC — the scroll-presentation redesign

The settled rulings for the rebuild of the public scroll page. All
owner-ruled (2026-08-23 through 2026-08-25) unless marked OPEN; the
build implements these without re-litigating them, and surfaces the
open item to the owner rather than deciding it. The worked example
throughout is day 2 — Genesis 1:6–8, `gen_02_raqia_day` — as drawn in
`front_door_mockup_v5_2026-08-25.html`.

## The shape

One set of content per step of THE_STEPS.md. Summary visible on the
page; details open BELOW, in-page — never a separate page. The live
site's exact look and sequential flow are kept: cream/tan/olive
palette, the site mast with its three tabs, the chapter banner, and
the left rail (book/chapter/verse selects with ◀▶ steppers, Go,
☰ units, ▦ coverage, search, the "reading" locator — replicated from
the deployed dress, not the undressed reader).

## The nine settled rulings (2026-08-23)

1. **Site-replica look.** Existing palette, nav, chapter banner. The
   1:6 verse tree must be the EXACT live-site tree — mark pills,
   five-line leaf cards with ROLE lines, the zoom cluster. The
   mockups' 1:7/1:8 trees are simplified sketches; the build brings
   them to the 1:6 standard.
2. **Verses grouped in a block with a vertical spine label** reading
   top-down ("BLOCK · DAY 2 · GENESIS 1:6–8"). REVISED at the build
   (owner, 2026-08-25, choosing the uniform-blue variant over the
   rotating colors): ONE BLUE everywhere — spine, step buttons, and
   the per-verse shades of ruling 8 all derive from the day-2 blue
   (#5a7ca6); block boundaries are marked by the spine label, not by
   hue. The rotating-color original stands in the v4/v5 mockups as
   history.
3. **Each verse collapses to a label row** — the STEP 1·2 split-button
   chip, the reference, the JPS quote. ONE click anywhere on the card
   opens tree and morphology together; a header click closes.
   Transliteration is removed from the pill rows.
4. **One clickable style everywhere** — the blue split button with the
   big-arrow end cap (the owner's pick: option C in
   `buttons_mockup_2026-08-23.html`).
5. **Steps labeled explicitly.** STEP 1·2 on every verse row; STEPS
   3–8 sit once at the block's foot: Declare (its own card, never
   nested), Read and log (teachings table + full-ledger expander),
   Extract claims (every chain as a teaching card: SAID → CLAIMED
   with middah → MACHINE), Write the logic (verse-shaded operator
   sketch + full record + runnable proof), Run the gates, The stamp.
6. **Band header wording verbatim** — "every declared source read ·
   seven teachings from the tradition are built into this unit · full
   rule · stamped 2026-08-23"; the record line ("gen_02_raqia_day ·
   rev 3") as fine print. No unit pill or status chips on verse rows.
7. **Accordion discipline** — one item open at a time; the opened item
   aligns to the top with collapse-compensated smooth scroll;
   open-state is the arrow/word swap (▸ open / ▾ close), a lit
   header, and a thin tan line down the open body.
8. **Per-verse color shades** inside STEP 6 mark which code belongs to
   which verse.
9. **Hebrew never without English inline** — absolute, throughout
   (method law 8; the gloss lint gates this folder like any shipped
   file).

## The STEP 5 teaching layer (ruled 2026-08-25)

- **Rules-intro box: YES.** A small box atop STEP 5 — about four
  sentences — explaining that the tradition keeps its own numbered
  rulebook of inference moves (13 rules of Rabbi Ishmael for law, 32
  of Rabbi Eliezer for narrative), so the middah names on the cards
  (E7 wording-analogy, E30 word-splitting) mean something to a
  first-time reader.
- **Cross-links as PEEKS, not navigation.** A thread mention (the
  utterance census, the repaid "good", a typed anchor) carries a
  dotted underline; tapping it opens a one-to-two-line popover in
  place — the thread's next stitch and its unit tag, with a dismiss —
  NEVER the full sibling card, and never a jump off the page. The
  one-block focus survives.
- **The kept-out card: YES.** After the claims, one dashed card
  showing a source that was read and changed nothing (the worked
  example: the king-who-roofed-with-water parable, verdicted
  enrichment) — reading means filtering, and the filter is on the
  record.

## Spacing (owner ruling 2026-08-25, "lets go with compact")

The COMPACT density from `spacing_mockup_2026-08-25.html` variant C is
the shipped spacing — text size unchanged, roughly a third less air:
line-height 1.4; verse cards .45/.8rem padding, .4/.55rem gaps in
bands; band heads .3/.75rem; accordion heads 5/10px, bodies 8/12px;
table cells .18/.45rem; chips 3/7px. The mockup's four variants stand
as the comparison record (D — dense with 108% text — was liked and
remains the recorded runner-up).

## Vocabulary (owner ruling 2026-08-24, canon 2026-08-25)

In page copy, "machine" names only the steps-derived law programs —
the operator sketch and interpreter (the SAID → CLAIMED → MACHINE
rows are exactly this use). The fold/transform engine is "the mill,"
never "machinery." See the three-tiers bullet in CLAUDE.md.

## OPEN — the owner has not ruled

- Whether the morphology table's transliteration column goes the way
  of the pill rows. Surface at build; do not decide.

## Status copy is a prop

The mockups freeze real figures from their drawing dates (the 34-of-733
declaration, "stamped 2026-08-23", nine gates). The BUILD computes all
of it from the records at export time, as the site already does —
nothing in a mockup is a source for a shipped number.
