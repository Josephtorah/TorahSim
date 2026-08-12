# TANAKH RUN — pass-1 harvest report (2026-08-12)

**Status:** PASS 1 COMPLETE. Owner word "pass one harvest go" → all three
channels run, scene catalog on disk. Experimental standing (gork-class),
commits on owner word.

## The funnel

929 chapters / 23,213 verses / 305,507 tagged words (the 24 books,
`elijah_docket/tanakh.sqlite`) →

| Channel | Method | Yield |
|---|---|---|
| 1 — link graph | `export_links` Tanakh-category rows anchored Exod 21, filtered to true verse refs (`tanakh_ref`-resolved; the category also holds commentaries-on-Tanakh, hence the filter) | **70 verse crossrefs** (`harvest_ch1_links.json`) |
| 2 — the scans | the law01/02/03 oral-scan digests' narrative crossrefs (166k+ chars of notes, 27 bites + 2 tanakh closes for block 3+tail alone), grep-mined + tail-digest memory | the nine plan flagships confirmed + Zech 11's thirty, the calf-five-fold triple, 1 Kgs 20:35's strike-refuser, Job 31's manifesto, SeMaG's borrowed-axe pointer to 2 Kgs 6:5 |
| 3 — the lexicon | all 31 statute-derived lemmas with whole-Tanakh frequency ≤ 90 swept in FULL via the words-table lemma index + 5 surface patterns (`harvest_ch3_lexical.json`) | ~700 candidate verses |

→ **`scene_catalog_tanakh_run_2026-08-12.json` — 57 scenes** (21 P0 / 22
P1 / 14 P2), 157 verse refs, 50 chronology-keyed for the REPLAY fold + 7
achronic doctrine scenes; 5 scenes touch FORWARD (block-4) stubs —
reported, never faked.

Modes: binding 17, prophetic_figurative 14, doctrine 7,
pre_sinai_typology 6, foreign_comparative 5, lexicon 4, patch 3,
gen9_noahide 1.

## Channel-3 design note

The lemma list was derived FROM the statute: every word of Exod 21:1-37
(+ the 22:1-3 border) was lemma-tagged by the DB, and every lemma rare
enough to sweep exhaustively (≤ 90 hits) was swept — no hand-picked root
list, so nothing operative was missed by my choosing. Homographs excluded
by hand: כפר as village/henna/pitch, שבעתים at 2 Sam 21:9 ("the seven of
them"), גף at Prov 9:3 ("heights"); Strong's 4835 (מרוצה "oppression",
Jer 22:17) initially mislabeled as the awl — the real awl is 4836, 2 hits
(Exod 21:6, Deut 15:17), fixed in the script.

## Headline finds (beyond the nine planned flagships)

- **Josh 7:24-25 — Achan's OX is stoned with him**: the theft-verb (גנב
  "steal") indicts the nation, and beasts die for the owner's crime —
  the exact inversion of 21:28 (beast dies for its own act, owner pays).
  Jurisdiction-flag showcase (cherem/sacrilege track overrides the
  theft track).
- **Exod 19:12-13 — Sinai runs the goring-ox protocol on itself**: beast
  or man that touches the mountain is STONED (סקל), no hand touches the
  carcass — the statute's first deployment is God's own perimeter,
  BEFORE 21:28 is spoken.
- **1 Sam 12:3 — Samuel's clearance audit**: "whose OX (שור) have I
  taken… from whose hand a RANSOM (כפר)?" — the judge audits himself in
  the statute's own nouns; Amos 5:12 (לקחי כפר "takers of ransom") is
  the same audit failed.
- **Jer 2:34 — the burglar clause as indictment**: לא במחתרת מצאתים
  ("NOT in the breaking-in did you find them") — the lemma's ONLY
  non-statute hit; Jeremiah cites the clause's LIMITS as the measure of
  guilt.
- **Zech 5:3-4 — the flying scroll**: the curse enters the house of the
  THIEF and the FALSE-SWEARER — the theft parashah's own pair (21:37 +
  22:10) — heavenly enforcement exactly where the Tur's
  jurisdiction-decay (tail digest B25) leaves courts powerless.
- **Esth 7:4 — Esther pleads the sale-scale**: "had we been sold merely
  as slaves I would have kept silent" — the plea works only because
  slave-sale is a bounded, regulated institution: the statute's premise
  argued in a Persian court.
- **2 Kgs 11:2 — Yehosheba STEALS (גנב) baby Joash to SAVE him** (+ the
  Jabesh men stealing Saul's bones for honor): the verb's actus without
  the mens — intent-sensitivity test for the machine.
- **Gen 44 — the goblet plant grades theft-verdicts**: death (brothers'
  offer) → slavery-for-all → Joseph's ruling: only the one FOUND (נמצא,
  the statute's idiom) with it, and Judah's תחת ("in place of")
  self-substitution — an Egyptian court converging on 21:37/22:2.
- **Negative finding CONFIRMED mechanically**: נגח ("gore") = 13 hits in
  all Tanakh; outside the statute every one is blessing, oracle, vision,
  or psalm — **no ox ever gores a person in Tanakh narrative.** Block
  3's case-law runs on zero narrative instances; reported as a result,
  per plan.

## Replay hooks worth flagging

The catalog's strongest state-persistence tests: Nathan's fourfold as a
debt DISCHARGED ACROSS FOUR LATER EVENTS (child/Amnon/Tamar/Absalom);
the Gibeonite famine reading a DECADES-OLD massacre state; Naboth's
blood-debt discharged two books later at Jehu's purge; Jer 34's
release-state written, reverted, sanctioned. Parallel-account merge test
rows: 1 Kgs 22:11 = 2 Chr 18:10 (clean), 2 Kgs 11:2 = 2 Chr 22:11
(clean) — calibration before the hard Araunah case.

## Next (owner-paced, per the reordered plan)

Step 2: **block-3 coding day** (the תם/מועד machine, pit, ox-vs-ox, +
now the 21:37 tariff from the tail scan) → step 3 block-2 coding day →
step 4 chapter assembly → step 6 PASS 2: fixture runner + replay fold
over these 57 scenes, per-scene CONFIRM / DIVERGE / NO-VERDICT-IN-TEXT.
Early option: run the block-1 scenes (Joseph, Jer 34, Neh 5, 2 Kgs 4:1,
Hagar, goblet) against the EXISTING block-1 machine before the coding
days.
