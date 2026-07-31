# Middot detector — retroactive calibration against the five frozen units
**2026-07-31 · run over the completed triage record (gen_01–gen_05)**

*Middot* = "measures," the classical interpretive rules. Question tested: had this
detector existed before our triage reads, how many of the chain's rule-applications
that we found by reading would it have surfaced or verified?

**Honest counters:** cache scanned = 706 files (everything fetched to date — chain-side
coverage is bounded by this); invocations found = 55 formula hits in 43 sources
(52 in already-triaged sources); corpus-side join candidates = 1,347 rare-lemma keys
(961 cross-book).

## Chain side — the six rule-applications our ledgers recorded, rechecked

| # | known application (from our ledgers/notes) | rule | detected? |
|---|--------------------------------------------|------|-----------|
| 1 | Chullin 60a:10-11 — the grasses draw an inference from the trees' *le-minehu* ("by its kind") | *kal va-chomer* ("light and heavy" — how much more so) | **YES** — both formula forms hit — but only AFTER we cached the passage: it had been verified-local without a cache file. Lesson: detector coverage = cache coverage, exactly as the README warns. |
| 2 | Bava Kamma 55a:12 — lashes for crossbreeding sea-kinds, derived *le-minehu*–*le-minehu* from the land | *gezerah shavah* ("equal decree" — verbal analogy), announced by *atya* ("it is derived") | **YES** — the *atya* formula fires. |
| 3 | Chullin 27b:11 — "one verse says [fowl] from the waters… another says from the ground" | rule 13 (*katuv echad omer* — "one verse says": contradiction until a third decides) | **YES**. |
| 4 | Niddah 22b:21 — hunting which creation-verb occurrences are *mufneh* ("free") enough to carry an analogy | the *mufneh* availability check | **YES**. |
| 5 | Lekach Tov on Gen 1:24 — "…living being — GENERAL (*klal*); beast, creeper, land-animal — PARTICULAR (*prat*)" | *klal u-frat* ("general and particular") | **NO — known v1 gap.** The anthology uses the terms as separated labels, not the connected formula the needle list matches. v2: detect the label form (*klal* + *prat* within a short window). |
| 6 | JT Kilayim 1:6:4 / Mishnah Yevamot 6:6 — rule-applications made WITHOUT announcing a formula | (silent applications) | **NOT DETECTABLE by formula search** — silent applications need the corpus side (shared-key match) or a human read. Recorded as a structural limit, not a bug. |

**Score: 4 of 5 announced applications detected; silent applications are out of
formula-scan's reach by design.** Bonus finds the reading pass had NOT singled out:
*kal va-chomer* ("light and heavy") invocations in BR 6:1, 6:3, 6:4 — the day-4
diminution dossier argues in that form throughout — and a triple invocation
(*binyan av* "prototype" + *gezerah shavah* "verbal analogy" + *kal va-chomer*) in
Lekach Tov's introduction to Leviticus, sitting in our cache from an earlier fetch:
the anthology's own preface on the rules themselves.

## Corpus side — do our known join keys appear in the candidate table?

| lemma | word | total in Torah | in join table? |
|-------|------|----------------|----------------|
| 6754 | *tzelem* ("image") | 6 | YES — grade A (cross-book) |
| 8415 | *tehom* ("the deep") | 8 | YES — grade A |
| 8317 | *sharatz* ("swarm") | 12 | YES — grade A (at the rarity cap) |
| 3999 | *mabbul* ("flood") | 12 | YES — grade B |
| 8435 | *toledot* ("generations-of") | 29 | NO — correctly excluded (a structural header, too common to be a join key) |
| 4327 | *min* ("kind") — the key of the chain's most famous join on our span | ~30+ | **NO — the honest finding.** |

**The *le-minehu* lesson (the calibration's most valuable result):** the chain's
verbal analogy on "by its kind" — the very one that touched our day-5 unit — uses a
key that FAILS global rarity. The classical constraint was never global: it is
*mufneh* ("free") **within the relevant domains** — "by its kind" said of sea
creatures joined to "by its kind" said of land species, each occurrence unclaimed in
its own context. Global rarity is a good first filter (it caught image/deep/swarm)
but it is not the chain's operative criterion. **v2 requirement: domain-scoped
availability** (rarity within genre/section pairs), not corpus-wide counts.

## How this now plugs into the process (per the owner-approved design)

1. **Pre-derivation watch lists:** before deriving a unit, list its join-grade
   tokens + all cached invocations anchored nearby → Tier-A routing for the triage.
2. **Triage verification:** every announced application in a source we read gets its
   textual substrate machine-checked (tokens shared? rare? free?) — ledger notes can
   then say "join verified from our corpus."
3. **Register feed:** chain-applied + text-verified joins → written-echo register
   with origin `chain-citation`; text-possible + chain-silent keys → observation
   tier, forever, per *ein adam dan me-atzmo* ("one may not derive on his own").
4. **Never:** auto-resolution, law generation, or register edges without owner
   sign-off.

## v2 backlog (evidence-driven, from this calibration)

- Domain-scoped *mufneh* ("free") grading (the *le-minehu* lesson).
- Label-form *klal/prat* ("general/particular") detection + cantillation-tree
  brackets for the scope candidates.
- Formula list growth as new corpora enter the cache (Aramaic variants; *Sifra* —
  "The Book," the legal commentary on Leviticus — uses its own announcement style).
- Silent-application hunting via corpus-side matches surfaced INTO triage reading
  lists (the only way to catch rule 6-class cases).
