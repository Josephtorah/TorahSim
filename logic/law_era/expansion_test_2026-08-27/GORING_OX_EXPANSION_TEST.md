# The Expansion Test: the Goring Ox

**Date:** 2026-08-27
**Ordered:** the owner — "lets look at the mishnah and talmud as not just
a execution trace but expansion of existing code derived from the logic...
run the test, document it for my learning purposes."
**Material:** Exodus 21:28-37 (the goring ox, the pit, ox-versus-ox, the
theft tail) — the block this project read deepest: the whole-chapter oral
inversion, 4,903 ledger rows, 35 witnessed claims, and a running machine
(logic/law_era/exo_21_v2_block3_DRAFT.py).
**Kind:** analysis for learning. Hypothesis-grade classifications.
Not derived stone; not binding religious law.

---

## Part I — What the discussion found (recorded here on the owner's order)

Before the test, the discussion established five things worth keeping:

**1. Two readings of the same text, both true.** The oracle lens reads a
Mishnah paragraph as a *test fixture* — inputs, expected output — grading
a machine that must already contain the law. The expansion lens reads the
same paragraph as *code*: law the tradition derived from the verse-kernel,
covering input space the verses never explicitly address. The tradition's
own claim about the Oral Torah is the second lens: it is the law's
fullness, not commentary on it.

**2. The tradition's vocabulary is already an object model.** Mishnah,
First Gate (בבא קמא, Bava Kamma) 1:1 opens the torts tractate by declaring
אבות נזיקין ("fathers of damage" — parent categories): the ox, the pit,
the grazer, the fire — and everything else is a תולדה (toladah,
"offspring" — a subclass). The gemara then asks, subclass by subclass,
whether each behaves *like its father* — inheritance with argued
overrides. The ox itself carries three subclasses — horn, tooth, foot —
with different liability parameters per domain. And one of the thirteen
inference rules of Rabbi Ishmael is בנין אב (binyan av — literally
"building the father"): constructing the general category from one
verse's case. The tradition's own name for generalization is class
construction.

**3. The tradition tags its own code provenance,** in four tiers: law
derived from verses with the derivation shown; oral law from Sinai with
no verse hook (installed axioms, by the tradition's own admission);
rabbinic legislation with named authors and eras (versioned patches);
and custom (configuration). The tiers carry different runtime behavior:
doubt in a Torah-tier law resolves strictly, doubt in a rabbinic-tier
law resolves leniently — error-handling policy keyed to provenance.

**4. Expansions can override the kernel's surface.** The famous exhibit
is "eye for eye" (Exodus 21:24), which the Babylonian Talmud, First Gate
83b-84a, resolves to monetary compensation through a battery of
independent derivations — a documented method override, reasons shown.
The test below found the same class *inside our own block*.

**5. Our v2 machine is already kernel-plus-expansion, blended and
untagged.** The thirty-shekel tariff is verse; the three-gorings
threshold is expansion; the standing-verdict timing rides Mishnah
Keritot 6:2. The machine works because expansions were quietly imported.
This test makes the quiet part explicit.

---

## Part II — The test

**Method.** The chapter reading of 2026-08-12/20 left a witness manifest:
35 claims for this block, each with its verse reference and its sources
(logic/oral_audit/manifests/law03_exo_21_28_37_claims.json — quoted, not
modified). The test classifies every claim by *how its law relates to
the verse-kernel*, using eight tiers defined for this purpose:

- **K — kernel-stated:** the verse itself states it (a number, a rule).
- **I — ink-derivation:** compiled from the kernel's own ink — a word
  choice, a particle, a grammatical form, a word-count, a missing word.
- **M — middah/analogy expansion:** built by a named inference move —
  analogy between clauses, redundancy geometry, structural composition.
- **C — case-table expansion:** definitions, procedures, and constants
  supplied by the Mishnah, Tosefta, or the tannaitic midrash (the
  verse-order expounding books) — law the verse does not contain but
  the tradition derives and tabulates.
- **D — dispute-parameter:** a recorded machloket (dispute) that rides
  as a configuration choice with runtime consequences.
- **G — declared decree:** law the tradition itself labels a decree —
  גזרת מלך (gezerat melekh, "a king's decree") or scripture's own
  decree — an install, self-tagged as such.
- **O — override:** the expansion replaces the kernel's surface
  behavior, derivation shown.
- **R — rationale/witness record:** reasons and resonances that change
  no output (kept dual-track, as ever).

**The classification, all 35 claims.** (Sources quoted from the
manifest; abbreviations decoded: Torah Temimah is the verse-order
anthology that spined the chapter reading; Mekhilta de-Rabbi Shimon bar
Yochai is the second tannaitic midrash on Exodus; First Gate = Bava
Kamma.)

| Claim | The law | Tier | Why |
|---|---|---|---|
| L28-01 | Goring = the horn only; forewarned-for-beasts is not forewarned-for-man | **I** | Two verbs in the ink — יגח (yigach, "gores," act-word, man-victim) vs יגף (yigof, "strikes," effect-word, beast-victim) — compile into a context-indexed state machine |
| L28-02 | Whose ox is included — seven ownership categories, even the ownerless | **I** | The word שור (shor, "ox") appears seven times; the count is the scope |
| L28-03 | The ox is tried by a court of 23, convictable by one vote | **M** | Analogy: "as the death of the owner, so the death of the ox" — full capital process transferred |
| L28-04 | Intent conditions — the ox must have intended this victim | **I+D** | The particle את איש (et ish, "that man") read as inclusion; aimed-at-beast disputes recorded |
| L28-05 | The benefit ban lands at sentencing, not at stoning | **C** | Mishnah Keritot 6:2 fixes the timing the verse leaves open |
| L28-06 | "The owner is clear" — clear even in Heaven's court (the tam) | **I** | The word נקי (naki, "clear") expanded to its full depth |
| L29-01 | Three gorings vest the forewarned state; on three days; one clean petting day reverts | **I+D+C** | "From yesterday and the day before" = three (ink); days-vs-times is Rabbi Yehudah against Rabbi Meir (dispute); the petting-reversion definition is case-table (Tosefta First Gate 4:5) |
| L29-02 | The five written tam/forewarned differences | **C** | The Mekhilta's own tabulated block — the verse-order law book expanding the split |
| L29-03 | Two evidentiary regimes: capital-style for ox-kills-man, money-style for ox-kills-ox | **I** | Two different words in the ink — והועד (ve-hu'ad, "testified in the owner's presence") vs נודע (noda, "it was known") — two procedures |
| L29-04 | "Its owner also shall die" = death by Heaven, not the court | **O** | The override inside our own block: the recorded filing is that the received law "UPROOTS the verse" — surface says execution, law says Heaven's court, derivation shown |
| L29-05 | Reduced guarding suffices for the forewarned ox | **I** | The bound verb-suffix (ve-lo yishmerennu) graded as the reduced guarding — grammar as parameter |
| L30-01 | Ransom mechanics: obligatory, only after death, full per partner, the victim's value, to the heirs | **I+C** | אם (im, "if") read as obligation (ink); the mechanics tabulated by the case tables |
| L30-02 | Ransom is for negligence only — never for a killing act, none for the pit | **I** | Cross-verse patch pair with Numbers 35:31 — kernel linked to kernel |
| L31-01 | Son or daughter: no vicarious liability either direction | **I** | "According to this judgment shall it be done" — the same law, expanded to say only the same law |
| L32-01 | The thirty shekels for the gored slave | **K+C** | The number is kernel; the type assignment is expansion — atonement-payment, not price, payable above worth |
| L32-02 | Six stacked rationales for the flat thirty | **R** | Reasons, not outputs |
| L32-03 | The tariff as the canon's slave-price constant (the thirty pieces echo) | **R** | Cross-corpus resonance — witness tier |
| L33-01 | Pit depths: ten handbreadths for death, nine for injury, six for impact | **I+C** | The missing word ומת ("and it dies") in the pit clause is the ink hook; the numeric floors are case-table constants |
| L33-02 | The pit's exclusions — an ox, not a man; a donkey, not vessels | **G** | The tradition's own class: scripture's decree — an exclusion installed, labeled as decree by the sources themselves |
| L33-03 | The cover law and the guarding economy | **I+C** | The consequence-clause read closely; procedures tabulated |
| L33-04 | Pit liability transfers to buyer and donee, not the heir | **C** | Pure case-table liability theory — no verse states it |
| L34-01 | The carcass goes to the victim, counted into damages | **I** | Whose "it shall be his"? — the pronoun resolved, and Onkelos's "the VALUE of the dead" carrying load |
| L35-01 | The tam split is valid only between equal-value oxen | **M** | Mekhilta de-Rabbi Shimon's structural argument on what "halving" can mean |
| L35-02 | Half-damage: compensation or fine? — and fines are not collected in Babylonia | **D** | Rav Papa against Rav Huna son of Rav Yehoshua — a dispute-parameter with enforcement geography as its runtime consequence |
| L35-03 | The remedy reshapes ownership: victim and damager become partners in the ox | **C** | Rabbi Akiva's received law — partnership theory the verse does not state |
| L36-01 | The forewarned ox pays in full from the best land | **M** | "He shall surely pay" hooked to the best-of-his-field clause — analogy between payment verbs |
| L36-02 | The Temple-property and gentile asymmetries | **I** | The word רעהו (re'ehu, "his fellow's") scoping the parties |
| L37-01 | The theft tariff covers ox and sheep only | **I** | Redundancy geometry — the extra ox and sheep of the tail close the class |
| L37-02 | Disposal conditions: all of it; partners who steal | **I+C** | Ink ("and slaughter it" — all of it) plus Mishnah First Gate 7:5's cases |
| L37-03 | The agency exception: slaughter by an agent convicts the thief | **M** | The Torah's lone agent-for-sin liability, built from the slaughter-or-sell redundancy — an argued exceptional install |
| L37-04 | The four/five tariff contains the double: where the double dies, the whole dies | **M** | Structural composition — one tariff proven to be built of another |
| L37-05 | The four-and-five constants themselves | **G+R** | Declared גזרת מלך (gezerat melekh, "a king's decree") by the sources — yet derived four ways anyway: the tradition dual-tags its own constant |
| L37-06 | Enforcement: whose the fine is, oath consequences | **C** | Court procedure from the case tables |
| L0-01 | The forewarned-state template exported system-wide — plague, recurring events | **E** | The class, reused across the corpus: inheritance beyond the chapter (an export tier the test had to add) |
| L0-02 | King Yannai summoned to the court through this block's clauses | **R** | Witness-tier narrative riding the law |

---

## Part III — The tally and the finding

Counting each claim by its primary tier (composites counted at their
leading tier):

**[CORRECTED 2026-08-27, same day — by the run. The hand count first
written here said I:15 and C:7; when the classification was coded and
machine-counted (Part V), the true tally of this document's own table
came back I:16, C:5, K:1. The check caught its author — the recurring
lesson of this project, arriving on schedule. Corrected figures:]**

- **Ink-derivation (I): 16 claims** — the largest tier by far.
- **Kernel-stated (K): 1 claim** (the thirty shekels).
- **Case-table expansion (C): 5 claims.**
- **Middah/analogy expansion (M): 5 claims.**
- **Rationale/witness (R): 3 claims.**
- **Declared decree (G): 2 claims.**
- **Dispute-parameter as primary (D): 1 claim** (several more ride as
  secondary parameters inside I and C rows).
- **Override (O): 1 claim.**
- **Export (E): 1 claim.**

Kernel-compiled (K + I + M together): **22 of 35.**

**The finding, stated for the record:** in the block this project read
deepest, the Oral Torah's expansion of the written law **overwhelmingly
compiles from the kernel's own ink**. Fifteen of thirty-five claims are
direct ink-derivations — a verb choice, a particle, a word-count, a
missing word — and five more are argued analogy. The case-table tier
supplies definitions, constants, and procedures the verse leaves open,
but almost always anchored to a hook the ink provides. The pure
installs — the decree tier — number exactly two in the whole block,
**and the tradition labels both itself**: the pit's exclusions as
scripture's decree, the four-and-five tariff as "a king's decree." The
expansion layer is not freewheeling; it is a disciplined compiler with
a tiny, self-declared axiom set.

**Three exhibits found during the test, worth the owner's eye:**

1. **The override lives in our own block.** L29-04: "its owner also
   shall die" is read as death by Heaven's court, and the recorded
   filing says in so many words that the received law *uproots the
   verse*. This is the same class as eye-for-eye — the expansion
   replacing the kernel's surface behavior with the derivation shown —
   and we had already encoded its output in the machine without naming
   the class.
2. **The tradition dual-tags its own constants.** L37-05's sources
   declare the four-and-five tariff a king's decree — an install — and
   then derive it four ways anyway. Provenance tag and rationale stack,
   side by side, in the sources themselves. Our tier field has a native
   precedent.
3. **The machine is half-tagged already.** Every constant and rule in
   the block-3 draft carries its claim-ID; every claim carries its
   sources. The only missing piece of the expansion lens is the tier
   letter itself — one field, and the kernel/expansion boundary becomes
   machine-readable.

---

## Part IV — What this means, and what it does not

**For the oracle mission:** the two lenses compose. A Mishnah row read
as expansion becomes an op with provenance; read as fixture, the same
row tests the op it became — install and test, one text. The
failing-case triage gains its third branch: not only "bug in our stone"
or "read more," but "this is expansion — install it, cited, at its
tier."

**For the case-file design (queued in THE_WORLD.md):** the schema
should carry the tier field from birth. The gemara's own from-where-
do-we-know discussions supply the value per law; this test shows the
classification is tractable — thirty-five claims took one sitting on
paper.

**For honesty:** the tier assignments above are this test's model-layer
judgments, hypothesis-grade, made by reading the manifest's own source
strings. Nothing was re-derived; no unit, ledger, or machine was
touched. Where a composite claim carries several tiers, the table says
so. The owner's word can reclassify any row.

**Not done here (deliberately):** no code, per the order. The natural
next steps, when and if ordered: (a) add the tier letter to the block-3
claim annotations; (b) run the same classification on blocks 1 and 2
(the slave laws and the injury laws — block 2 holds the eye-for-eye
override); (c) fold the tier field into the sugya case-file design.

---

## Part V — The test coded and run (same day, on the owner's word)

The owner asked whether to code it or keep learning. The answer taken:
code the small piece now — it was fully defined by Parts II-III — and
hold the big pieces (the case-file schema, the standing-rules table,
the world clock) for more learning. Two files joined this folder, each
tier-labeled per the README's rule:

- **claim_tiers.json** — MODEL tier: the 35 classifications as data,
  joining the witness manifest by claim id. The manifest itself was
  never touched.
- **expansion_report.py** — MILL tier: reads the manifest, the tier
  table, and the block-3 machine's source; gates the join both ways;
  tallies; maps every machine definition to its cited claims and their
  tiers; then instruments the machine and RUNS a scene.

**What the run found:**

1. **It corrected this document.** The hand tally in Part III was
   wrong (I:15, C:7 as first written); the machine count of this
   document's own table is I:16, C:5, K:1. Corrected above with a
   dated note. The finding stands and sharpens: 22 of 35 claims are
   kernel-compiled (kernel-stated + ink + analogy), and the
   self-declared decree tier stays at exactly 2.
2. **The machine's constants now split visibly by tier.** The slave
   tariff (thirty) is K — the verse states it. The theft tariffs
   (four and five) are G — the tradition's own "king's decree." The
   forewarning thresholds and pit depths are I — compiled from ink.
   One constants block, three provenances, now machine-readable.
3. **A verdict now carries a provenance profile.** The live scene —
   three gorings on three days with the owner warned, the ox kills a
   slave, then one clean petting day — computed: forewarned state
   vests, the flat thirty is owed, one petting day reverts the ox to
   innocent. The claims on the actual code path: nine. Their tiers:
   **seven ink-derivations, one kernel constant, one override** (the
   owner's death-by-Heaven filing). That line — a verdict with its
   provenance breakdown — is the expansion lens running live, and it
   is exactly what the sugya case files should emit per case.
4. All gates green: the tier table covers the manifest exactly both
   ways; all 31 machine-cited claim ids resolve; the scene's asserts
   hold. No unit, ledger, manifest, or machine file was modified.

**The learning, one breath:** coding the small piece immediately paid
twice — it caught the analyst's own arithmetic, and it produced a new
output kind (the tier-profiled verdict) that the case-file design was
going to need anyway. The big pieces still wait, better informed.

---

## Part VI — The owner's question refines the decree tier (2026-08-27)

The owner asked: could the two "pure additions" actually derive from
other verses we didn't notice? The close look answers: **both already
have verse anchors, and the earlier phrase "no verse behind them" was
too strong — corrected here.**

- The pit exclusions are read off THIS verse's own named animals ("an
  ox or a donkey," 21:33 — ox, not a man; donkey, not vessels). The
  decree label marks a rule with a SOURCE but no compilable REASON —
  the gemara itself notes the cut defies the system's usual
  stronger-case logic.
- The four/five tariff's numbers are in the verse (21:37), and the
  tradition itself already ran the owner's proposed move: claim L37-04
  proves the tariff CONTAINS the double payment of Exodus 22:3 plus an
  increment — cross-verse composition. The decree label covers only
  the unexplained remainder (why this increment; why sheep less), with
  four rationales recorded at rationale tier.

**Refinement adopted:** the G tier splits into G-ink (ink-anchored
decree, reason uncompiled) and G-nohook (no verse at all — received
oral law; exists in the tradition, e.g. the received measures, but
ZERO instances on this block). Sharpened finding: on this block,
ALL 35 claims carry a verse anchor; only REASONS ever fail to
compile. If a future reading grounds either remainder, the ledger
records it and the tier flips with its citation — the append-only
design expects exactly that discovery.
