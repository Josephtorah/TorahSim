# DOES ONKELOS CHANGE GENRE IN GENESIS 49? — the measurement

**Date:** 2026-08-30 · **Status:** evidence for an owner ruling. **Nothing in
CORE_SHELF.md has been touched.** · **Occasioned by:** claim G72-30, raised at
the Vayechi derivation and recorded as a "CORE_SHELF candidate — raised, not
acted on."

## The claim under test

G72-30, from the gen_72 ledger's Onkelos track:

> Through forty-eight chapters Onkelos translates, deviating only at named
> points. Here it becomes an INTERPRETIVE PARAPHRASE... **the declared
> translation stops being a translation for the length of one chapter, and
> any weight this project puts on it as a witness must be adjusted here and
> nowhere else.**

That claim was written from reading. This is the same question put to the ink.

## Method

Onkelos is on disk for all five books (`Data/sefaria_export/Onkelos_*/he.json`).
Our Hebrew is the frozen parse DB. Two metrics, per verse:

- **EXPANSION** = Onkelos word count ÷ Hebrew word count. A translation tracks
  its source's length; a paraphrase expands.
- **RETENTION** = fraction of Hebrew stems (3+ letters) whose consonantal
  skeleton survives into the Aramaic. A translation keeps the word.

Both are read **against Onkelos's own prose baseline**, never against 1.0.
Aramaic spends extra particles and shifts consonants as a matter of course;
that offset is constant across prose, so only deviation FROM the baseline is
evidence.

**Two corrections applied before any number was believed:**

1. **Ketiv/qere rows double-count.** Where the received text is written one way
   and read another, our DB carries two rows for one word (the written form
   carries no vowel points). 67 such rows across the Torah, dropped.
2. **Three chapters are versified differently** between our Hebrew and this
   Onkelos edition, so pairing verse N to verse N would compare unrelated
   sentences. **Excluded and named:** Exodus 20 (Hebrew 26 verses vs Onkelos
   23), Deuteronomy 5 (33 vs 30), Numbers 25 (19 vs 18). Before this filter,
   the two Decalogue chapters ranked #1 and #2 in the whole Torah — a pure
   artifact of misalignment. **184 of 187 chapters survive.**

**Probe (per Step 4's coverage rule — a check that reports must first prove it
fires):** the metrics were tested against verses the ledger already identified
as paraphrase (Genesis 49:3, 4, 5, 6, 10, 27) versus the Genesis 5 and 11
genealogies. Paraphrase 1.59 expansion / 0.21 retention; genealogy 0.96 / 0.39.
Both metrics separate. The probe passes, so the numbers below are reportable.

## Result 1 — the claim's core is TRUE, and stronger than it knew

Genesis 49 is **rank 1 of 184 aligned Torah chapters** by expansion (1.538
against a Genesis prose baseline of 1.035). The ledger called it the largest
translation-layer finding of the walk. Measured across the whole Torah, it is
the largest anywhere in the Torah.

## Result 2 — but "and nowhere else" is FALSE

The six Torah poems were named **in advance, from genre, not picked from the
ranking.** All six land in the top nine of 184:

| rank | chapter | expansion | |
|---|---|---|---|
| 1 | Genesis 49 | 1.538 | Jacob's blessings |
| 2 | Deuteronomy 33 | 1.368 | the Blessing of Moses |
| 3 | Deuteronomy 32 | 1.229 | the Song of Moses |
| 4 | Numbers 24 | 1.156 | Balaam, oracles 3–7 |
| 8 | Numbers 23 | 1.137 | Balaam, oracles 1–2 |
| 9 | Exodus 15 | 1.134 | the Song of the Sea |

Mean over all 184 aligned chapters: 1.040. Four of the six take the top four
places. **This is not a Genesis 49 fact. It is a POETRY fact, and Genesis 49 is
its maximum** — the top of a gradient, not a singularity.

## Result 3 — it is the POEM, not the chapter

Genesis 49 splits cleanly, and so does every other poem tested. The narrative
frame around a poem translates at the book's ordinary rate; the poem body
expands:

| | poem body | narrative frame | poem ÷ frame |
|---|---|---|---|
| Genesis 49 (blessings vs gathering/burial/death) | 1.698 | 0.944 | **1.80** |
| Deuteronomy 32 (Song vs the charge to ascend) | 1.281 | 0.981 | 1.31 |
| Numbers 24 (oracles vs Balak's rage) | 1.203 | 1.058 | 1.14 |
| Exodus 15 (Song vs Miriam, Marah, the statute) | 1.179 | 1.043 | 1.13 |

In Genesis 49 the burial charge (49:29–33) is word-for-word — 49:31 has
expansion 1.00 and the **highest retention in the chapter, 0.80**. Onkelos did
not change genre for a chapter. It changed genre for a poem and changed back
within the same chapter, twice.

## Result 4 — a finding against our own ledger row, for appending

The gen_72 ledger filed 49:11–12 under row **O9, "buffer-consistent where it
still translates"** — with the hedge "though even these carry expansions."
The measurement says those are among the most rewritten verses in the chapter:
49:11 expansion **2.08**, retention **0.09**; 49:12 expansion 1.83, retention
0.00. Opened, the hedge is an understatement. The Hebrew of 49:11 binds a foal
to a vine and washes a garment in wine. Onkelos writes: *"Israel will travel
round to his city, the people will build his temple, the righteous will be
round about him, and the doers of the Torah in learning with him."* There is
no lexical contact at all — it is a different sentence, not an expanded one.

**Ledgers are append-only.** This is offered as an APPENDED note to the gen_72
Onkelos track, correcting nothing and rewriting nothing: O9 named these two
verses as still-translating, and the ink says they belong with O1–O7.

## What this means for the reading shelf

Under the spine default (owner, 2026-08-27) the declared reading of any Genesis
span is Bereshit Rabbah **plus Onkelos** — so Onkelos is half the shelf, and
what kind of witness it is at a given span is a CORE_SHELF question.

The honest statement is not "Onkelos is unreliable in poetry." It is that
**Onkelos answers a different question in poetry**, and the project must know
which question it is reading:

- **In prose** Onkelos is a translation. Where it smooths the Hebrew, the
  roughness it smooths is evidence **about the verse** — that is the "minimal
  resolver" role CORE_SHELF already gives it.
- **In poetry** Onkelos delivers the tradition's *reading*. A deviation there
  is evidence about **how the chain understood the line**, not about the
  Hebrew's roughness. It is not noise — at 49:10 it names the messianic
  identification, at 49:27 it puts the Temple in Benjamin's portion, and both
  became material findings that Bereshit Rabbah independently corroborated.

Read as a translation, poetic Onkelos would generate false claims about the
Hebrew. Discarded, it would throw away genuine chain testimony. It needs to be
**re-labelled, not re-weighted.**

## Why this cannot wait for Exodus

Exodus 15, the Song of the Sea, is rank 9 of 184 and already frozen as exo_15.
Whatever is ruled here governs the Exodus walk's first poem.

## Reproduce

```bash
python3 logic/onkelos_genre_2026-08-30/onkelos_genre.py   # probe + Genesis + poems
python3 logic/onkelos_genre_2026-08-30/onkelos_rank2.py   # alignment audit + Torah rank
```
