# THE MIDDOT — the tradition's own inference rules

The middot (מִדּוֹת, "measures/rules") are the chain's OWN numbered
rulebook for deriving meaning from the text — the original catalog,
two millennia before ours. They are NOT the same layer as the TIR:
TIR maps grammar → logic inside one verse; the middot license
inferences FROM verses — cross-case, cross-passage. The sources we
read in Step 4 argue BY middot constantly; this file gives the
process its names for those arguments.

Three collections (Tannaitic tradition):
- the SEVEN of Hillel (H1–H7) — included in the thirteen;
- the THIRTEEN of Rabbi Ishmael (I1–I13) — for LAW (halakhah);
  Maimonides holds legal reasoning closed under these;
- the THIRTY-TWO of Rabbi Eliezer ben Yose ha-Gelili (E1–E32) —
  for NARRATIVE (aggadah).

Enumeration below follows Schumann, *Talmudic Logic*
(a reference scan held outside this repository), to be verified against the
Baraita texts themselves when they are read under Step 4. Model
layer — freely revisable, dated notes per change.

## The thirteen of Rabbi Ishmael (law)

- **I1 — qal wa-chomer** ("light and heavy", a-fortiori): transfer a
  ruling from the lesser case to the greater (or reverse). HARD
  CONSTRAINTS the tradition itself states: the **dayo cap** — the
  conclusion may never exceed the premise's severity; genus match
  required (the Mishnah's Sadducees exchange is the recorded failure
  case); not applied in penal law; never from received law to new law.
  → future operator QAL_WACHOMER with dayo assertion.
- **I2 — gezerah shavah** ("equal decree"): analogy licensed by the
  SAME WORDING in two passages — "the indefinite is explained by the
  definite." → mechanically a join over our word-level data.
- **I3 — binyan av** ("build a father"): generalize a rule from one
  verse (or two) to all cases sharing its essential feature.
- **I4 — kelal u-frat** (general then particular): the particular
  RESTRICTS the general to itself.
- **I5 — prat u-kelal** (particular then general): the general
  EXTENDS beyond the listed particulars.
- **I6 — kelal u-frat u-kelal**: general–particular–general → include
  only what resembles the particular.
- **I7 — kelal ha-tzarich li-frat** ("a general that needs the
  particular"): general and particular that each
  need the other to be understood.
- **I8** — a particular singled out from a general TEACHES about the
  whole general, not only itself.
- **I9** — singled out to discuss a similar provision: LIGHTENS, does
  not burden.
- **I10** — singled out for a dissimilar provision: lightens AND
  burdens.
- **I11** — singled out for a new provision: the original general no
  longer applies unless the text restores it.
- **I12 — davar ha-lamed me-inyano** : meaning decided from CONTEXT
  (and from the passage's end).
- **I13** — two verses that contradict stand until a THIRD verse
  decides between them. → our dispute/fork discipline has this shape.

Layer notes: I4–I7 (and the ribui/miut particles) OVERLAP the TIR's
particle territory (TIR-014/015). Policy: the TIR rule stands and
CITES the middah + chain sources as authority (the day-one amendment
pattern — Bereshit Rabbah 1:14 + Chagigah 12a on the et-inclusions).
I1–I3, I8–I13 are claim-layer inference licenses, not grammar.

## The thirty-two of Rabbi Eliezer (narrative)

For narrative (aggadic) derivation; several repeat the thirteen at
narrative strength. By cluster:
- **Particles**: E1 ribui (extension: et, gam, af, kol), E2 miut
  (restriction: akh, raq, min), E3 extension-after-extension (which
  restricts), E4 restriction-after-restriction (which extends).
- **A-fortiori & analogy**: E5 explicit qal wa-chomer, E6 implicit
  qal wa-chomer, E7 gezerah shavah, E8 binyan av.
- **Textual economy**: E9 abbreviation, E10 repeated expression
  (repetition signifies), E11 divided/reordered sequence.
- **Scope moves** (E12–E25): particular↔general teaching relations,
  mutual elucidation of passages, two verses contradicting until a
  third decides (E15 = I13's narrative twin), the rare-usage rule,
  statements said here but applying to a fellow passage, and more.
- **Literary devices**: E26 mashal (parable), E27 symmetry, E28
  from-the-preceding, E29 gematria (letter-values), E30 notarikon
  (words as acronyms), E31 earlier-that-is-later within a passage,
  E32 earlier-that-is-later between portions (the Torah is not
  strictly chronological — cf. our order-carries-no-claim finding,
  Mekhilta on Gen 1:1).

## How the middot enter the process (THE_STEPS.md)

- **Step 4 (read and log):** when a source ARGUES by a middah, the
  ledger note names it (e.g. "argues I1 qal wa-chomer from the paid
  keeper").
- **Step 5 (extract claims):** every claim carries a `middah:` field
  when the source's inference form is identifiable — I-rules in law
  spans, E-rules in narrative spans; absent = plain-statement claim.
- **Step 6 (write the logic):** claims licensed by a middah keep the
  middah's own constraints as assertions (dayo cap, genus match,
  third-verse resolution). Where TIR and a middah overlap, the TIR
  rule cites the middah as chain authority.
- The book's worked example for I1 is the BAILEE ladder of Exodus 22
  (Bava Metzia 95a) — TOP10 block 4's own territory; first real
  workout for QAL_WACHOMER when block 4 opens.
