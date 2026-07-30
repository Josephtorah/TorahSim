# METHOD — How Language Logic Derives the Verses

**Date:** 2026-07-30
**Kind:** the project's method charter — a living document (see §6 for how to revise it)
**Status:** describes the practice as owner-approved through TIR-033 and the Stage C/D pilot
**Rule that governs everything:** logic is authored by hand in frozen, reviewable documents; code only interprets (Pre-Code rule, `AGENTS.md` / `logic/SYSTEM.md`). Hebrew is the sole derivation source; every Hebrew string travels with transliteration + English aid. Nothing here is binding religious law.

---

## 0. The claim, stated carefully

The project's working claim is narrow and testable: **the grammatical machinery of Biblical Hebrew — cantillation structure, verb morphology, and a small set of particles — visibly performs operations that twentieth-century formal logic later named.** A jussive verb issues a directive; a wayyiqtol chain ticks a narrative clock; the particle *et* points at an event's patient; a *ki*-plus-imperfect clause opens a legal condition. We read those operations with the formal vocabularies built for them — and we label every such reading a **hypothesis with stated limits**, never doctrine. The evidence that this is the text's own machinery rather than our projection is distributional: the verb-form census across the five books (§1.2) shows the forms partitioning by genre at corpus scale, in exactly the pattern the operator readings predict.

Two research families feed the method: the **language research** (what the Hebrew forms are — a thousand-year tradition) and the **logic research** (formal systems for command, event, time, correctness, speech, and law — mostly 1930s–1960s). This report details both, then shows precisely how they combine, verse by verse.

---

## 1. The language research (the Hebrew side)

### 1.1 Masoretic cantillation — the ta'amim (structure research)

**Source tradition:** the Masoretes of Tiberias, ~7th–10th c. CE; encoded in the Leningrad Codex (1008 CE), which our `Data/*.xml` files carry via the Open Scriptures Hebrew Bible.

Every word bears one mark from two families: **conjunctive** marks (munach, mercha, mahpach…) that bind a word forward to the next, and **disjunctive** marks in ranked degrees of pause — the medieval grammarians' emperors (silluq, etnachta), kings (zaqef, tifcha), dukes (revia, pashta, tevir), and below. The maqqef hyphen fuses words into one accent unit.

**What we derive from it:** rule set v3 (`logic/taamim_rules/`) glues conjunctive runs into *bricks* (leaves), then splits recursively at the strongest internal disjunctive into a **pure binary tree** per verse. The tree is the verse's own outline of its logic: the etnachta cut in Gen 1:1 separates *event* from *theme inventory*; in Gen 1:3 it separates *the demand* from *the result*. Whole-Torah validation: **all 5,853 verses parse unique** under v3 — zero per-verse exceptions, which is the discipline that makes the layer trustworthy.

### 1.2 Morphology — stems and forms (grammar research)

**Source tradition:** Tiberian vowels made morphology legible; Judah Hayyuj (~1000 CE) established the triliteral root; Jonah ibn Janah and David Kimchi (Radak) systematized the **binyanim** (verb stems); James Strong (1890) numbered the lexicon; the OSHB project tagged every morpheme digitally. The tags are labeled **#IMPOSED** — a modern scholarly aid, never part of the received text.

The two axes that carry logical weight:

| axis | values | logical signal |
|------|--------|----------------|
| **stem** (voice) | qal, niphal, piel, pual, hifil, hofal, hitpael | niphal/pual in directive position = **agentless** constraint — the doer slot is deliberately empty |
| **form** (mood/aspect) | perfect, imperfect, wayyiqtol, weqatal, imperative, jussive, cohortative, infinitive construct, participle | **this is the operator selector** — see §2 and the TIR rules |

**The genre fingerprint** (whole-Torah counts by query, recorded in `PROPOSAL_TIR_026_033`): wayyiqtol — Genesis 2,107 vs Leviticus 189; weqatal — Leviticus 707 and Deuteronomy 632 vs Genesis 164; jussive — 193 in the whole Torah (rare = high-signal). Narrative runs on and-then; law runs on and-you-shall. The distribution is the argument that the forms are genre machinery, not our party trick.

Also load-bearing: Hebrew's **morpheme granularity**. Prefix letters (ve=and, ha=the, le=to, be=in, mi=from, ke=like) and pronoun suffixes each get their own database row — because *le-* + infinitive is the PURPOSE operator, *la-* marks the receiver of a naming, and the double *et* enumerates a Theme inventory. The connective logic of the Torah lives substantially in single letters.

---

## 2. The logic research (the six borrowed formalisms)

Each entry: origin → core idea → the Hebrew feature it reads → operator vocabulary → limits. The form→operator mappings are frozen as owner-approved rules TIR-026…033 in `logic/TREE_INTERPRETATION_RULES.md`; particle rules TIR-014/015/022 cover *et*, double-*et*, and the prefix frames.

### 2.1 Hoare logic — precondition · operation · postcondition (C.A.R. Hoare, 1969)

Program correctness as a triple: state before, operation, state guaranteed after. **Hebrew hook:** mood alone splits demanded-state from achieved-state — jussive *yehi or* (let light BE) vs wayyiqtol *va-yehi or* (light WAS), same root, same letters. Gen 1:2 is a pure precondition block (zero narrative verbs — we counted); 1:3 is the operation and its postcondition in one verse. **Vocabulary:** TRIPLE, RESULT, the day-unit transaction (spec → build → RESULT → PASS → name → COMMIT). **Limits:** the triple structure is observed for creation-week fiats; elsewhere it is applied only where spec-and-result pairs actually appear.

### 2.2 Deontic logic — obligation, permission, prohibition (G.H. von Wright, 1951)

The logic of *ought*. German legal theory adds the distinction the Torah needs: **tun-sollen** (ought-to-DO, laid on an agent) vs **sein-sollen** (ought-to-BE, laid on a state). **Hebrew hook — the volitional forms:**

| form (OSHB code) | operator | rule | example |
|---|---|---|---|
| jussive (…j…) | **LET(p)** | TIR-026 | *yehi or* — Gen 1:3, `Vqj3ms` |
| jussive + *al* | **LET-NOT(p)** | TIR-026 | *al-tatzar* — Deut 2:9 |
| imperative (…v…) | **CMD!(p)** | TIR-027 | *dabber* — Lev 1:2; *peru u-revu* — Gen 1:28, `Vqv2mp` |
| imperfect in command speech (…i…) | **LET?(p)** — the ? is mandatory | TIR-028 | *yaqrivenu* — Lev 1:3, `Vhi3ms` |
| cohortative / 1st-person volitive | **CMD-US(p)** | TIR-033 | *na'aseh adam* — Gen 1:26, `Vqi1cp` |
| niphal/pual in directive slot | **agentless LET** (sein-sollen) | TIR-032 | *yiqqavu* — Gen 1:9, `VNj3mp` |

**The question-mark discipline is the method's conscience:** the imperfect alone cannot distinguish command / future / permission, so LET? keeps its ? until a *per-unit human ruling with citation* resolves it — enforced in code (the interpreter refuses uncited upgrades; scenario S7). **Limits:** register is recorded, not inferred — Gen 1:28 shows imperative *inside* a blessing; the operator records mood, not tone.

### 2.3 Event semantics — events with role slots (Donald Davidson, 1967)

An action sentence asserts an event-thing with labeled participants: Agent, Theme, Instrument, Location. **Hebrew hook:** wayyiqtol/perfect verbs assert events; the untranslatable particle ***et* marks the Theme slot** (TIR-014), and repeated *et* enumerates the complete Theme inventory (TIR-015): *et ha-shamayim **ve-et** ha-aretz*. **Vocabulary:** EVENT(verb, Agent, Themes…), THEME, partition events (*bein X u-vein Y* as one two-place relation). **Limits:** the set-partition reading of *divide* is labeled hypothesis; *et* before time expressions and the homograph *et* ("with", Strong's 854) are separate lemmas, distinguished by tag, not guessed.

### 2.4 Temporal logic — the order of times (Arthur Prior, 1950s–60s)

Operators for before/after/until. **Hebrew hook:** the wayyiqtol chain is a formal clock — each *va-y…* verb one tick; the weqatal chain is its instructional mirror — obligations *sequenced after* a trigger (TIR-029, **THEN(p)**): *ve-samakh… ve-nirtza* — and-he-shall-lean… and-it-shall-be-accepted. The evening-morning formula is the **COMMIT** boundary closing each day-transaction — and its absence on day 7 is machine-visible (the famous open transaction). **Named-Oral convergence:** Bereshit Rabbah 3:7 derives *seder zemanim* (an order of times) precisely from the wayyiqtol (not jussive!) mood of *va-yehi erev* — the tradition doing mood-sensitive parsing, verified from local corpus. **Limits:** in prophetic/narrative contexts weqatal is sequence without obligation; units label which.

### 2.5 Speech-act theory — words that do (J.L. Austin, 1955 lectures / 1962)

Performatives change the world by being said. **Hebrew hook:** *va-yomer … yehi* — the saying IS the making; every divine speech wraps its payload in **DECLARE(speaker, …)**. Naming is the second performative: *va-yiqra Elohim la-or yom* — a **REGISTRY write**, receiver marked by the dative *la-* prefix (TIR-022), label = the bare word after. Registry writes are how the machine caught both collisions (*shamayim* re-issued in 1:8, *eretz* in 1:10 — each with named Oral resolutions). **Limits:** performative force is claimed for the formulaic frames (saying, naming, blessing), not for all speech.

### 2.6 Casuistic vs. apodictic law (Albrecht Alt, 1934)

Form-criticism's split: **casuistic** case law — IF (protasis: *ki/im* + imperfect) THEN (apodosis: weqatal duties) — the ancient Near Eastern standard; vs **apodictic** absolutes — *shema!*, you-shall-not — unconditioned. **Hebrew hook:** Leviticus's frames: *adam ki-yaqriv* (when a person brings-near, `Vhi3ms`) opens the case; *im olah qorbano* (if his offering is a burnt-offering) selects the branch; the weqatal chain delivers the procedure. **The two faces of *ki*:** complementizer "that" (Gen 1:4 *ki-tov* — NOT a condition) vs casuistic "when" — disambiguated per-verse and recorded in `reviews/STANDING_DECISIONS.md` §3, never auto-resolved. **Limits:** Alt's sharp two-type scheme is a lens; mixed forms exist and are flagged.

---

## 3. The seventh construct: the dry-run machine (ours, not borrowed)

The six lenses needed a harness, so the project defined a register machine — first on paper, now as the Stage D interpreter (`run_unit.py`):

| register | holds |
|----------|-------|
| TIME | clock anchor (t0 = *reshit*) and marks |
| WORLD | entities (created vs presupposed), facts, invariants, partitions |
| REGISTRY | installed names (or→yom, choshekh→layla…) + write count |
| SPECS | queue of open demands — every LET pushed, popped when a RESULT satisfies it |
| TESTS | acceptance checks passed (PASS(tov, …)) |
| LEDGER | committed day-transactions (spec ✓ / test / names / label form) |

plus a FLAGS side-channel for pattern deviations. Reading a passage = executing its operators against these registers. The machine's two standing contracts, enforced in code: a commit with empty TESTS is **FLAGGED, never blocked** (day 2 is data, not an error — scenario S6); **LET? never auto-upgrades** (S7).

---

## 4. How the research is applied — the derivation pipeline

Every unit walks the same eight steps; the human/machine division of labor is the whole point.

1. **Parse** (machine): ta'amim v3 → glue bricks → pure binary tree. Provenance recorded (rule version).
2. **Attach morphology** (machine): OSHB codes joined per morpheme; lexicon vN supplies EN-AID glosses.
3. **Role hints** (machine, versioned `logic/role_rules/`): form-frames + particle rules label each brick — CMD(be), THEN(prop), OBJ_FRAME, BETWEEN… *Display heuristics, illustrative; golden tests pin them.*
4. **Operator lines** (HUMAN): per leaf, the derivation proper — pick the operator, cite the TIR rule, anchor the Hebrew, state confidence. This is where the six lenses are consciously applied, and where anything ambiguous gets ? or [OPEN], never silently resolved.
5. **Registers & scenarios** (HUMAN): trace the machine state per verse; write the expected deltas as scenarios — the unit's own test suite; deviations from the day-ledger pattern become findings.
6. **Oral lookups** (HUMAN, named-only): where the pattern breaks (missing test, collision, open transaction), search the indexed corpus (119,903 segments FTS), quote the named location, verify against local text, tier-label (verified / observation). Dual-track — never merged into the Written derivation.
7. **Freeze** (OWNER): review → `status: frozen`. Changes henceforth require a new derive pass.
8. **Machine verification** (machine): `run_unit.py <unit> --scenarios` replays the derivation mechanically; red = fix the YAML or version the rulebook — never a code hack.

Discipline rules that hold the pipeline honest: versioned rulebooks with golden regression tests (parser v1→v3, lexicon v1→v2, role rules v1); per-verse *ki* rulings; confidence labels on every claim (tested / established / hypothesis / OPEN); flag-don't-fix for textual anomalies; English never drives a conclusion.

**Clarification — what "human" means here (and what it does not).** The human side of this
division of labor is the project's own deriver and owner, working today: choosing operators,
citing TIR rules, ruling on each *ki*, resolving or refusing to resolve a LET?, writing
scenarios, signing the freeze. It is **not** a reference to the Oral Torah. The Oral tradition
enters the pipeline at step 6 only, as a **source the human consults**: named witnesses whose
readings we quote by exact location, verify against the local corpus where possible,
tier-label, and keep on a second track — never merged into the Written derivation and never
part of the machine. That said, one resonance is worth recording as a labeled observation
(observation, not doctrine): the project's architecture — frozen written structure, plus a
living human interpretive authority that may never be automated, plus changes made only on
the record — structurally rhymes with the Written/Oral relationship itself. The Masoretes
froze structure in marks and left interpretation with humans; we freeze structure in
versioned parsers and leave interpretation in signed documents. The rhyme explains why the
Pre-Code rule fits this material so naturally; it claims nothing more.

### 4.1 The Oral coverage protocol (calibrated on day 1, 2026-07-30)

Step 6 says *what* an Oral lookup is; this subsection says *how much* to read per unit.
It replaces intuition with measurement: for the pilot span (Gen 1:1–5) we ran the
exhaustive experiment once — **every** tier-1 source Sefaria's link index anchors to the
span was enumerated, fetched, and read: **483 of 483**, eleven batches, one row per source
in `logic/oral_triage/gen_01_creation_boot_2026-07-30.md`, honest counters throughout
(enumerated / fetched / read are three different numbers, and all three must be reported).

**What the calibration measured.**

- Signal rate: ~40 of 483 sources (~8%) changed or strengthened anything — 16 material
  finds, ~12 strong enrichments, a handful of machine-verifiable text claims (the first
  *tet* ("ט") landing in *tov* ("good"); exactly 80 letters before the first *va-yomer*
  ("and He said"); 7 words / 28 letters in 1:1; 14 words in 1:2 — every count checked
  against our own corpus and found true).
- Provenance held empirically, not just by policy: **100% of material finds came from
  chain primaries and authorized translations.** No anthology, halakhic code, geonic
  work, late targum, or outside-chain source produced material a primary didn't already
  contain. All 148 duplicate-resolutions pointed at primaries we had read.
- The best witnesses were not where fame predicts: the strongest operator-level evidence
  came from *translations and grammar-adjacent works* (Onkelos's *yat* object-marker and
  *yemama*/*yoma* label split; Saadia's dependent-clause parse of 1:1; Ibn Ezra's Sabbath
  Epistle on the *yom* polysemy) — because our derivation is grammatical, sources that
  make grammatical commitments outweigh sources that make homiletic ones.

**The standing protocol for units after the pilot (two tiers plus a filter):**

1. **Tier A — full read** (read the whole passage, verdict every source):
   (a) all chain-primary sources anchored to the unit's span;
   (b) all translations, of every era — Onkelos, Saadia's Tafsir, the late targumim —
       because a translation is forced to *rule* on every parse question;
   (c) any source of any class anchored to a token where the unit carries an [OPEN]
       flag, a ? mood, or a FLAG — open questions buy full reads wherever they point.
   On day 1 this tier contained 100% of the material finds at roughly a third of the work.
2. **Tier B — snippet triage** (everything else): read the opening of the passage,
   identify what it compiles or which primary it parallels, and verdict it —
   `dup-of:<primary>` / `context` / `not-bearing` — in one ledger line. Promote to a
   Tier-A full read on any trigger: the snippet doesn't resolve to a known primary, it
   makes a checkable claim about our tokens, or it engages a form (mood, particle,
   word order, letter count) rather than a theme.
3. **Anchor-artifact filter** (before reading at all): a source whose anchor to our span
   is one incidental citation inside a passage about something else is presumptively
   `not-bearing`; the pattern is detectable cheaply (the source is anchored across many
   unrelated verses, or the anchor verse is quoted once deep in a long text). It still
   gets its ledger row — presumption is not exemption from the count.

**Unchanged disciplines.** The three honest counters; named-location-only citations
verified against the local corpus; the provenance register bounds what any class may do
(material = chain_primary only); verdicts are human, one row per source, ledgers stay
canonical and the DB `triage` table stays derived; and any machine-checkable claim a
source makes about our tokens gets checked, dated, and recorded — that habit produced
some of day 1's best rows.

**When to go exhaustive again.** A full 483-style pass is a *calibration instrument*,
not a routine: repeat it only when the corpus shifts under us (a new span with a
categorically different link profile — e.g., first legal unit in Leviticus, first
narrative unit outside creation) or when a Tier-B pass starts surfacing material-grade
content where the calibration said none should exist. Either event means the yield
model above is stale — recalibrate once, then re-cheapen.

---

## 5. Worked examples — complex verses through the full stack

Verb codes below were pulled from the database for this report (2026-07-30). English verse lines are JPS 1917 (public domain).

### 5.1 Leviticus 1:3–4 — the casuistic-deontic-agentless stack (the densest logic in the pilot corpus)

*Im olah qorbano min ha-baqar, zakhar tamim yaqrivenu; el petach ohel moed yaqriv oto, li-retzono, lifnei YHWH. Ve-samakh yado al rosh ha-olah; ve-nirtza lo, le-khaper alav.*
JPS: "If his offering be a burnt-offering of the herd, he shall offer it a male without blemish… And he shall lay his hand upon the head of the burnt-offering; and it shall be accepted for him to make atonement for him."

| leaf (translit) | code | lens → operator |
|---|---|---|
| *im olah qorbano* | — (verbless) | **casuistic (Alt):** IF-branch selector inside the *ki-yaqriv* case opened in 1:2 — a nested protasis |
| *zakhar tamim yaqrivenu* | `Vhi3ms` hifil imperfect + suffix | **deontic (TIR-028): LET?(bring-near(it))** — spec constraints male + unblemished ride the clause; ? stays: casuistic apodoses are duty-reading *candidates*, resolved per-unit |
| *yaqriv oto … li-retzono* | `Vhi3ms` + *et* | second **LET?**, Theme marked by *et* (TIR-014); *li-retzono* = purpose/acceptance frame on the *le-* prefix |
| *ve-samakh yado…* | `Vqq3ms` **weqatal** | **temporal-deontic (TIR-029): THEN(lean(hand, head-of-olah))** — obligation sequenced after the offering procedure begins |
| *ve-nirtza lo* | `VNq3ms` — **niphal weqatal** | **THEN + agentless (TIR-029 + TIR-032):** and-it-shall-BE-accepted — sequenced outcome with the doer slot empty. The priest never performs acceptance; the passive stem carries that structurally |
| *le-khaper alav* | `Vpc` — piel infinitive + *le-* | **PURPOSE(atone) (TIR-030)** — the telos slot of the whole chain |

Machine reading: a decision table opens (case: person brings offering → branch: burnt-offering, herd), duties queue as sequenced THEN-obligations, and the chain terminates in an agentless guaranteed state whose purpose is atonement. Four lenses in two verses — casuistic frame, deontic duties, temporal sequencing, agentless sein-sollen — plus event-semantic *et* marking. This is why Leviticus is the roadmap's payoff target.

### 5.2 Genesis 1:14–15 — a spec with jobs, purposes, and a THEN-chain

*Va-yomer Elohim yehi me'orot bi-rqia ha-shamayim, le-havdil bein ha-yom u-vein ha-layla; ve-hayu le-otot u-le-mo'adim, u-le-yamim ve-shanim. Ve-hayu li-m'orot… le-ha'ir al ha-aretz; va-yehi khen.*
JPS: "Let there be lights in the firmament of the heaven to divide the day from the night; and let them be for signs, and for seasons, and for days and years… and it was so."

| leaf | code | lens → operator |
|---|---|---|
| *va-yomer Elohim* | `Vqw3ms` | **speech act: DECLARE(Elohim, …)** |
| *yehi me'orot* | `Vqj3ms` jussive | **LET(exist(lights))** (TIR-026) — the fiat |
| *le-havdil bein…u-vein* | `Vhc` hifil inf + *le-* | **PURPOSE(divide(day\|night))** (TIR-030) — the lights' job spec, with the *bein…u-vein* pair relation |
| *ve-hayu le-otot u-le-mo'adim…* | `Vqq3cp` **weqatal** | **THEN(serve-as(signs, seasons, days, years))** (TIR-029) — spec clauses sequenced onto the fiat: not events, *standing assignments* |
| *ve-hayu li-m'orot… le-ha'ir* | `Vqq3cp` + `Vhc` | second THEN + second PURPOSE(give-light(earth)) |
| *va-yehi khen* | `Vqw3ms` | **RESULT("khen")** — generic summary discharge of the whole spec (contrast day 1's verbatim echo) |

Note the Hoare shape at scale: one LET carrying **two PURPOSE annotations and a THEN-chain of role assignments** — a specification document, closed by a one-line result. SPECS gets one demand with four riders; the machine records the pop at *va-yehi khen*.

### 5.3 Genesis 1:26 + 1:28 — self-directive, delegation, and imperatives inside a blessing

*Va-yomer Elohim na'aseh adam be-tzalmenu ki-dmutenu; ve-yirdu…* then *va-y'varekh otam Elohim… peru u-rvu u-mil'u et-ha-aretz ve-khivshuha; u-rdu…*
JPS: "Let us make man in our image… and let them have dominion…" / "Be fruitful, and multiply, and replenish the earth, and subdue it; and have dominion…"

| leaf | code | lens → operator |
|---|---|---|
| *na'aseh adam* | `Vqi1cp` — imperfect, 1st plural | **CMD-US?(make(adam))** (TIR-033 + the TIR-028 ?): volitive reading probable, but the form is *coded imperfect*, so the ? is mandatory. The plural is the famous anomaly — operator marks it; interpretation stays with the named sources (BR 8:3 consultation; Sanhedrin 38b), dual-track |
| *ve-yirdu vi-dgat ha-yam…* | `Vqj3mp` — **jussive plural** | **LET(rule-over(adam; fish, birds, livestock, all-earth, creepers))** (TIR-026) — a clean delegation issued about a third party, before that party exists in WORLD (machine flags the forward reference) |
| *ha-romes al ha-aretz* | `Vqrmsa` participle | **ONGOING(creep)** (TIR-031) — the domain described by standing behavior, not event |
| *va-y'varekh otam* | `Vpw3ms` piel wayyiqtol | **EVENT(bless, Theme=them)** — performative frame opens |
| *peru · u-rvu · u-mil'u · ve-khivshuha · u-rdu* | `Vqv2mp` ×5 — five imperatives | **CMD!(be-fruitful) ∧ CMD!(multiply) ∧ CMD!(fill(earth)) ∧ CMD!(subdue) ∧ CMD!(rule-over)** (TIR-027) — direct orders to present addressees, *inside* a blessing: the operator records mood, not tone, and the co-occurrence is itself a finding |

Contrast captured mechanically: 1:26 delegates by **jussive about them** (*ve-yirdu*, before they exist); 1:28 commissions by **imperative to them** (*u-rdu*, same root, now addressable). Same verb, two moods, two operators — morphology doing the work English translation erases.

### 5.4 Deuteronomy 6:4–5 — apodictic command, verbless identity, sequenced love

*Shema Yisrael, YHWH Eloheinu, YHWH echad. Ve-ahavta et YHWH Elohekha, be-khol levavkha u-v-khol nafshekha u-v-khol me'odekha.*
JPS: "Hear, O Israel: the LORD our God, the LORD is one. And thou shalt love the LORD thy God with all thy heart…"

| leaf | code | lens → operator |
|---|---|---|
| *shema Yisrael* | imperative | **CMD!(hear, addressee=Israel)** (TIR-027) — pure apodictic (Alt): no protasis, no condition |
| *YHWH Eloheinu YHWH echad* | — verbless | **identity/uniqueness assertion** — no verb, no event: a stative NP equation; the machine records a fact, and flags that *echad* here is predicate, not day-count |
| *ve-ahavta et YHWH…* | `Vqq2ms` **weqatal** | **THEN(love(YHWH))** (TIR-029), Theme marked by *et* (TIR-014): love as the obligation *sequenced after* hearing — command-chain, not sentiment report; the three *be-khol* phrases attach intensity riders |

The most famous verse in the liturgy is, formally: an apodictic CMD!, a verbless identity claim, and a weqatal THEN whose object carries the *et* Theme-marker. Every piece machine-visible; every theological question left exactly where it belongs.

---

## 6. Editing this process (the living-document protocol)

This method is designed to be revised as the Torah teaches us more — but never silently:

1. **New form→operator readings** enter as *proposals* with corpus counts and cross-book examples → owner sign-off → merged into `TREE_INTERPRETATION_RULES.md` with a new TIR number (the TIR-026..033 path is the template).
2. **Mechanical layers** (parser, lexicon, role rules) change by *new version directory + golden tests*, `CURRENT` pointer bump, full rebuild — never in-place edits (v1→v3 parser, lexicon v1→v2 are the precedents).
3. **Per-verse rulings** (like the two faces of *ki*) accumulate in `reviews/STANDING_DECISIONS.md`.
4. **Units** freeze; corrections require a fresh derive pass with a new derivation log.
5. **This charter** is revised by dated edits noted in a changelog line below; if the method itself changes materially, write `METHOD_…_v2` and keep this file as the record of where we stood.

## 7. Source map

`logic/TREE_INTERPRETATION_RULES.md` (TIR catalog) · `logic/taamim_rules/` (parser versions + goldens) · `logic/lexicon/`, `logic/role_rules/` (versioned aids + goldens) · `logic/units/*.yaml` (derivations; `gen_01_creation_boot` = frozen pilot) · `run_unit.py` (Stage D interpreter) · `logic/pre_logic_methods_2026-07-28/EXPERIMENT_precode_logic_gen_1_1_to_2_3_2026-07-28.md` (the creation-week evidence run) · `PROPOSAL_TIR_026_033_form_operators_2026-07-28.md` (corpus counts behind §2.2) · `reviews/STANDING_DECISIONS.md` (standing rulings).

**Changelog:** 2026-07-30 — v1, written at owner's order to document the core method.
2026-07-30 — §4 clarification added at owner's order: "human" = the project's deriver/owner,
not the Oral Torah; Oral = named, tiered source consulted at step 6; Written/Oral resonance
recorded as labeled observation.
2026-07-30 — §4.1 added at owner's order ("yes write it up"), after the day-1 exhaustive
read completed 483/483: the calibrated Oral coverage protocol — Tier-A full read
(primaries, translations, OPEN-flag anchors), Tier-B snippet triage with promotion
triggers, anchor-artifact filter; exhaustive passes reserved for recalibration.
