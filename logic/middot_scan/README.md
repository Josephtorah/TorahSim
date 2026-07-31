# Middot detector — machine-surfaced candidates for the classical interpretive rules

*Middot* = "measures" — the thirteen interpretive rules of Rabbi Yishmael (listed in
the introduction to the *Sifra*, "The Book," the early legal commentary on Leviticus)
by which the Oral chain derives conclusions from the Written text.

**What this tool does (v1):**
1. **Corpus side** — surfaces *candidate substrates* for *gezerah shavah* ("equal
   decree" — verbal analogy): rare lemmas (dictionary words) shared across separate
   passages of the Torah, with an overload grade (the classical *mufneh* — "free" —
   constraint: a join key already used in many places is a poor analogy carrier).
2. **Chain side** — scans our locally cached Oral sources for the classical rule-
   announcement formulas of BOTH rulebooks (v1.1): the **13 middot of Rabbi
   Yishmael** — the LAW-side rules (*kal va-chomer* — "light and heavy," the
   how-much-more-so argument; *gezerah shavah* — "equal decree," verbal analogy;
   *atya* — "it is derived"; *katuv echad omer* — "one verse says," the
   contradiction protocol; *mufneh* — "free") — and the **32 middot of Rabbi
   Eliezer ben Rabbi Yose the Galilean** — the NARRATIVE-side (aggadah, "telling")
   rules (*mashal* — "parable"; *ribbui/mi'ut* — "inclusion/exclusion" via the
   particles; *gematria* — "letter-arithmetic"; *notarikon* — "acronym reading";
   *al tikrei* — "do not read X but Y," revocalization; *lashon nofel al lashon* —
   wordplay; *mukdam u-me'uchar* — "earlier and later," order displacement) —
   plus the standing midrashic citation operators (*hada hu dikhtiv* — "this is
   what is written"; *davar acher* — "another interpretation"). The two rulebooks
   mirror the corpus's two measured modes: law-as-code, narrative-as-log.
3. **Calibration** — joins the two sides against the triage ledgers: which chain
   rule-applications did our completed triage already read, and would the corpus
   side have predicted their join keys.

**Discipline (absolute):**
- Survey tool only. Interprets nothing, freezes nothing, touches no unit YAML
  (Pre-Code rule). Its DB tables are derived and rebuildable.
- Output classes: (a) chain-applied and text-verified — strongest, may be cited in
  ledgers/notes; (b) chain-applied but text-discrepant — recorded dual-track with
  care; (c) text-possible but chain-silent — observation tier FOREVER unless the
  chain is found to apply it. The machine never generates law: the Oral Torah's own
  rule (*ein adam dan gezerah shavah me-atzmo* — "one may not derive a verbal
  analogy on his own," Pesachim 66a) reserves rule-application to the received
  chain; we detect and verify, we do not derive.
- Chain-side coverage is bounded by the local cache (honest counters printed in
  every report): we can only scan what we have fetched.
- Every Hebrew term in every output carries its English counterpart inline
  (owner's absolute glossing rule).

**v2 (planned, not built):** *klal u-frat* ("general and particular") scope
candidates using the cantillation-tree brackets; contradiction-pair candidates on
the corpus side.

Run: `python3 logic/middot_scan/middot_detector.py` (writes the two derived DB
tables `middot_joins` and `middot_invocations` + the reports in this directory).
