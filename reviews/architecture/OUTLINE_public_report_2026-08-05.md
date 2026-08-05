# OUTLINE — The Public Education Report (approved decisions + structure)

**Date:** 2026-08-05 · **Status:** awaiting owner approval of this outline;
nothing drafts until approved, nothing publishes without explicit owner order.
**Supersedes** the 15-topic outline of 2026-07-31 (corpus was 5 units; now 34).
**Rule:** Hebrew never without English inline — in every piece, every caption.

## Locked decisions (owner, 2026-08-05)

| decision | owner's call |
|---|---|
| Audience | Layered for all three: plain spine + [Tradition] sidebars + [Technical] sidebars |
| Origin thesis | FRONT AND CENTER — argued openly from the start |
| Form | Written + interactive pair |
| Narrative | Findings-first |
| Flagship findings | (1) the landed predictions, (2) the clock that stops, (3) Gen 1:28 paid at Exod 1:7 |
| Counterargument | Steelman the deflationary reading, then answer it |
| Interactive scope | Step-through walkthrough + live prediction board |
| Length | Short + long pair: ~3-page executive piece + document of record |

## The register discipline (governs every sentence in both pieces)

Three registers, kept fanatically distinct so the front-and-center thesis
never contaminates a measurement:

- **MEASURED** — counted in the database; anyone can reproduce (verse counts,
  token ordinals, verb-form censuses).
- **DERIVED** — readings produced by the frozen rules over the text
  (demands pushed/settled, flags, registry writes); reproducible given the
  rules, which are themselves published.
- **ARGUED** — the thesis and all interpretation. Clearly marked, never load-
  bearing for a MEASURED or DERIVED claim.

Executive piece: registers carried by phrasing ("we counted / we derived /
we argue"). Document of record: explicit margin tags.

---

## PIECE A — the executive piece (~3 pages, shareable anywhere)

1. **The claim** (ARGUED, stated in the first paragraph): the Torah —
   Written text and Oral tradition together — behaves like one coordinated,
   engineered system, and the coordination is measurable.
2. **Flagship 1 — predictions that landed** (MEASURED + the timestamp story):
   the frozen Genesis-14 note that named "GOD says take next" before
   Genesis 15 was derived; take-verb tokens 29–30; the kings at 17:6/17:16
   called by number; the two deep sleeps. Dated freezes, commit hashes.
3. **Flagship 2 — the clock that stops** (MEASURED): one chart — narrative
   ticks ('and-then' verbs) 2,107 → 189 into Leviticus while duty-chains
   ('and-you-shall' verbs) mirror 164 → 707. Narrative runs on and-then;
   law runs on and-you-shall.
4. **Flagship 3 — a command paid a book later** (MEASURED): Genesis 1:28's
   be-fruitful / multiply / fill answered verb-for-verb at Exodus 1:7,
   plus the swarm-verb borrowed from the creatures' blessing.
5. **What we built** (one paragraph): a register machine, explicit
   grammar-to-operation rules, 34 frozen unit derivations covering
   Genesis 1:1–17:27 gapless, every unit runnable and self-proving.
6. **The coordination claim** (ARGUED, one paragraph) + pointers to the
   document of record and the interactive walkthrough.
7. **The honesty box:** the three decisions we are leaving open in public
   view; the standing falsifiable predictions; what result would prove us
   wrong.

## PIECE B — the document of record (the full report behind Piece A)

Each section: plain-language spine, then [Tradition] and [Technical]
sidebars. Section map with content sources:

1. **The claim, in full** — the thesis stated with its register discipline
   explained up front.
2. **Findings you can check today** — the three flagships expanded with
   full evidence trails (debut-map ordinals, commit dates, chart data).
3. **How we read** — grammar becomes operations: the take/took link
   (yehi/va-yehi, bo/va-yavo, qechah/va-yiqach); created vs presupposed
   entities; the demand queue. Built from the item-1/item-2 chat
   walkthroughs (owner-tested plain language). [Tradition]: Masoretes'
   accents, Onkelos's rulings. [Technical]: the TIR rule catalog,
   morphology codes, run_unit.py.
4. **The famous absences** — day 2's missing 'good', day 7's missing
   commit, flagged-never-fixed as policy; the machine rediscovering what
   readers saw for millennia.
5. **The catalog of what 34 units found** — settled cycles 1–9; the
   believe-verb's fifteen-token arc; female speech returning at Hagar;
   Hagar naming God; the twin name-retirements; 5,853/5,853 verses parsing
   under one rule set.
6. **The whole-Torah picture** — the bootloader reading: allocation
   front-loaded (debut-rate curve), the I/O channel, the great install,
   the verdict engine, the recompilation, the two open transactions
   bracketing the five books, the final 'I HAVE GIVEN life and death.'
   (Source: STUDY_full_torah_machine_projection, committed.)
7. **The Oral Torah's own technical language** — the 13 law-side + 32
   narrative-side interpretive rules; ein ketiv kan ('it is not written
   here… but rather') as the chain's own diff operator (39 sources); the
   Memra-arc in Onkelos (shield→Word, naming→prayer, covenant→Word).
8. **The coordination problem — the thesis argued.** Steelman first, at
   full strength: formal logic was invented to describe command,
   obligation, and speech-that-acts; a text about command will fit it;
   pattern-hunting finds patterns. Then the answer: pre-registered
   predictions that landed; corpus-scale distributional discipline no
   single author-generation controls; the Oral chain independently
   developing the same operator vocabulary centuries later; one symbol
   table, one command voice, no partners. (ARGUED throughout, and says so.)
9. **How we keep ourselves honest** — freeze-after-review; quotes verified
   verbatim; censuses re-counted; flags never auto-resolve; the three open
   owner triages PRINTED IN THE REPORT as open; the falsification terms.
10. **See for yourself** — run instructions (ALL_UNITS.py: one file, 34
    units, every assertion re-proven on run); the interactive companion;
    invitation to check any number in the report.
11. **What this is not** — not religious law (ein adam dan me-atzmo, 'one
    may not derive on his own' — the chain remains the authority); not
    numerology; not a claim about the metaphysics of reality; the
    experimental-model disclaimer that heads every generated file.

## PIECE C — the interactive companion (walkthrough + prediction board)

- **Walkthrough:** Genesis 1:1–5 in the browser — one button per operation;
  panels for WORLD / queue / TESTS / LEDGER updating live; Hebrew shown
  with gloss at every step; the day-2 missing-test moment as the closer.
  Implementation: pre-computed state snapshots exported from the frozen
  unit (no live interpreter in the page — Pre-Code holds: the page only
  displays derived artifacts).
- **Prediction board:** each standing prediction with status (LANDED — with
  freeze date and commit hash — or OPEN), data-driven from a small YAML
  maintained by the freeze ritual. Launches with the take-verb, kings,
  deep-sleep, afflict-arc landings and the seven whole-Torah predictions.
- Hosted beside the scroll app; public deployment is a separate
  owner-gated decision (repo is private).

## Production order (each step returns to owner)

1. Owner approves this outline (emphasis edits welcome) →
2. Draft Piece A → owner review →
3. Draft Piece B section-by-section → owner review →
4. Build Piece C → owner review →
5. Publication: owner order only.

## Cautions

- Owner's Disclosure/ documents and the theory-of-disclosure narrative are
  NOT sources for the public pieces unless the owner explicitly directs.
- Licensing block required: Leningrad Codex via Open Scriptures (open),
  JPS 1917 (public domain), Sefaria texts (attribution per license).
- The report never claims the machine derives law or overrides the chain.
