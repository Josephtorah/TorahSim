# PROPOSAL — TIR-026…TIR-033: verb-form → logic-operator rules

**Date:** 2026-07-28
**Status:** **APPROVED by owner 2026-07-28** — merged into `logic/TREE_INTERPRETATION_RULES.md`
as TIR-026…033 (+ TIR-014 amendment). The operator names LET / CMD! / LET? / THEN /
PURPOSE / ONGOING / CMD-US are now citable in unit `tree_coverage` / derivation logs.
This document remains as the evidence record (corpus counts + cross-book examples).
**Derivation source:** Hebrew verb morphology (OSHB codes, #IMPOSED labeled aid) as it
appears in our v3 ta'amim leaves. English = aid only.
**Evidence base:** whole-Torah index (`torah_grok.sqlite`, 5,853 verses): corpus counts
per book + cross-book examples below were pulled by query, not hand-picked from Genesis.
**Origin:** the Gen 1:1–2:3 pre-code logic experiment
(`EXPERIMENT_precode_logic_gen_1_1_to_2_3_2026-07-28.md`); these rules generalize what
that experiment used, so far informally.

---

## 0. The genre fingerprint (evidence before rules)

Verb-form counts per book (all verb segments, whole Torah):

| form | Gen | Exod | Lev | Num | Deut | total | reading |
|------|-----|------|-----|-----|------|-------|---------|
| wayyiqtol (w) | **2107** | 889 | 189 | 752 | 255 | 4192 | narrative EVENT |
| weqatal (q) | 164 | 524 | **707** | 408 | **632** | 2435 | legal THEN-chain |
| imperfect (i) | 537 | 755 | **879** | 639 | **971** | 3781 | modal/casuistic space |
| imperative (v) | 300 | 196 | 41 | 137 | 110 | 784 | direct order |
| inf. construct (c) | 435 | 346 | 196 | 310 | 452 | 1739 | purpose/gerund |
| participle (r) | 330 | 287 | 205 | 255 | 395 | 1472 | ongoing state |
| perfect (p) | 940 | 559 | 208 | 444 | 544 | 2695 | completed state |
| jussive (j) | 77 | 40 | 16 | 31 | 29 | 193 | rare, high-signal LET |

The distribution is itself the argument: narrative books run on wayyiqtol; the legal
books invert to weqatal + imperfect. The operators below aren't a Genesis-1 party trick
— they are the Torah's own genre machinery. *confidence: tested (counts are mechanical)*

---

## The proposed rules

Format per rule: statement · cross-book Written examples (he / translit / en) · logic
mapping · limits (what the rule must NOT claim) · confidence.

### TIR-026 — jussive → LET(p) (directive on a third party or state)

**Statement:** a verb in jussive form inside divine/authorized speech maps to the
directive operator LET(p) — "let it be the case that p." With the negative particle
אַל / al, it maps to LET-NOT(p) (prohibition).

| Where | he / translit / en |
|-------|--------------------|
| Gen 1:3 | יְהִי אוֹר / yehi or / "let there be light" |
| Num 6:25 | יָאֵר ה' פָּנָיו / ya'er … panav / "may He make His face shine" — **blessing register** |
| Deut 2:9 (neg.) | אַל־תָּצַר / al-tatzar / "do not harass" — LET-NOT |

**Logic mapping:** deontic O(p) issued at a DECLARE site; in blessings, the same
operator in optative register (wish rather than command) — register noted per unit.
**Limits:** jussive is sometimes morphologically identical to imperfect (Gen 1:6 yehi is
*coded* imperfect); OSHB's coding is the authority, and ambiguous cases fall to TIR-028's
question mark, never silently up-graded. **confidence: tested**

### TIR-027 — imperative → CMD!(p) (direct order to the addressee)

**Statement:** imperative form maps to CMD!(p): a second-person directive to a present
addressee. Marks the speech as *commissioning* (someone must now act).

| Where | he / translit / en |
|-------|--------------------|
| Lev 1:2 | דַּבֵּר / dabber / "speak!" |
| Deut 6:4 | שְׁמַע יִשְׂרָאֵל / shema Yisrael / "hear, O Israel" |
| Gen 1:28 | פְּרוּ וּרְבוּ / peru u-revu / "be fruitful and multiply" — imperative *inside a blessing* |

**Logic mapping:** deontic obligation with named addressee slot (tun-sollen: obligation
to *do*). **Limits:** Gen 1:28 shows imperative and blessing co-occur; the operator
records mood, not tone. **confidence: tested**

### TIR-028 — imperfect in directive context → LET?(p) (hypothesis-marked directive)

**Statement:** imperfect form inside command speech maps to LET?(p) — probably a
directive, and the `?` is part of the rule: the form alone cannot distinguish
command / future / permission. Resolution is per-unit work, never automatic.

| Where | he / translit / en |
|-------|--------------------|
| Gen 1:20 | יִשְׁרְצוּ הַמַּיִם / yishretzu ha-mayim / "let the waters swarm" |
| Lev 1:2 | כִּי־יַקְרִיב / ki-yaqriv / "when he brings near" — casuistic trigger clause |
| Deut 6:5 | וְאָהַבְתָּ (weqatal, see TIR-029) vs. the law codes' יַעֲשֶׂה-type "he shall do" imperfects |

**Logic mapping:** deontic-modal with explicit uncertainty flag; in casuistic frames the
protasis (ki-clause) imperfect is the IF-condition, the apodosis imperfect the THEN-duty.
**Limits:** this rule *forbids* silently reading every imperfect as command (the exact
overreach the ? prevents). **confidence: tested as flag · resolution = per-unit**

### TIR-029 — weqatal → THEN(p) (sequenced obligation/consequence)

**Statement:** weqatal (ve- + perfect in instructional context) maps to THEN(p): an
obligation or outcome *sequenced after* a prior condition or act. This is the backbone
operator of the legal corpus (707× Lev, 632× Deut).

| Where | he / translit / en |
|-------|--------------------|
| Lev 1:2 | וְאָמַרְתָּ אֲלֵהֶם / ve-amarta aleihem / "and-you-shall-say to them" |
| Deut 2:19 | וְקָרַבְתָּ / ve-qaravta / "and you shall come near" |
| Gen 1:14–15 | וְהָיוּ לְאֹתֹת / ve-hayu le-otot / "and they shall be for signs" — spec clause |

**Logic mapping:** temporal-deontic composition: after(q, prior) ∧ O(q). Chains of
weqatal = ordered procedure (the korban procedures are THEN-chains).
**Limits:** in prophetic/narrative future contexts THEN(p) is sequence without
obligation; the unit labels which. **confidence: tested**

### TIR-030 — ל + infinitive construct → PURPOSE(p)

**Statement:** the prefix ל / le + infinitive construct maps to PURPOSE(p) — "in order
to p" — attaching a goal slot to the governing verb or object.

| Where | he / translit / en |
|-------|--------------------|
| Gen 1:14 | לְהַבְדִּיל / le-havdil / "to divide" — the luminaries' job spec |
| Exod 2:16 | לְהַשְׁקוֹת / le-hashqot / "to water (the flock)" — narrative purpose |
| Gen 2:3 | לַעֲשׂוֹת / la'asot / "to make/do" — the open-ended final purpose of the week |

**Logic mapping:** teleological annotation on events/objects (the postcondition an
action serves). **Limits:** bare infinitive constructs without ל (temporal "when…"
uses, e.g. בְּ/כְּ + inf.) are NOT purpose — separate mapping, out of scope here.
**confidence: tested**

### TIR-031 — participle → ONGOING(p) / INVARIANT(p)

**Statement:** participle form maps to ONGOING(p): a standing state or job rather than
an event. Inside a spec (after a directive), it installs an INVARIANT — a condition
required to keep holding.

| Where | he / translit / en |
|-------|--------------------|
| Gen 1:2 | מְרַחֶפֶת / merachefet / "hovering" — scene invariant |
| Gen 1:6 | מַבְדִּיל / mavdil / "dividing" — the firmament's standing job |
| Deut 1:4 | יוֹשֵׁב בְּחֶשְׁבּוֹן / yoshev be-Cheshbon / "dwelling in Heshbon" — ongoing state in narrative frame |

**Logic mapping:** stative predicate with temporal extent (holds-during), vs. the
point-events of wayyiqtol. **Limits:** participles also serve as plain nouns/adjectives
("inhabitant"); the rule applies to *predicate* position — leaf context decides, and
nominal uses stay NP. **confidence: tested**

### TIR-032 — niphal/pual in directive or outcome position → agentless constraint

**Statement:** passive stems (niphal/pual) in directive or outcome clauses map to
**agentless state-constraints**: the text obligates or reports an end-state without
naming a doer (sein-sollen — "ought to BE" — vs. tun-sollen "ought to DO").

| Where | he / translit / en |
|-------|--------------------|
| Gen 1:9 | יִקָּווּ הַמַּיִם / yiqqavu ha-mayim / "let the waters BE gathered" |
| Lev 1:4 | וְנִרְצָה לוֹ / ve-nirtza lo / "and it shall BE accepted for him" — korban outcome, no agent |
| Gen 2:1 | וַיְכֻלּוּ / va-yekhullu / "and they WERE completed" — pual completion, agentless |

**Logic mapping:** constraint on state, doer unspecified — deliberately: Lev's
acceptance/forgiveness outcomes (ve-nirtza, ve-nislach) are *never* performed by the
priest; the passive stem carries that theology structurally. **Limits:** ordinary
narrative passives (something just happens to be passive) are plain events; the rule
bites in directive/outcome slots. **confidence: tested (forms) · significance = hypothesis**

### TIR-033 — cohortative (1st person) → CMD-US(p) (self-directive)

**Statement:** cohortative/1st-person volitive maps to CMD-US(p): the speaker directs
*themself/ourselves* — deliberation or resolve, not command over another.

| Where | he / translit / en |
|-------|--------------------|
| Gen 1:26 | נַעֲשֶׂה אָדָם / na'aseh adam / "let US make a human" (coded imperfect 1cp — the ? applies) |
| Gen 11:7 | הָבָה נֵרְדָה / hava nerda / "come, let us go down" — the Babel echo of the same operator |

**Logic mapping:** deontic operator with speaker ∈ agents; in Gen 1:26 the plural is
the famous anomaly (named Oral: BR 8:3 consultation; Sanhedrin 38b) — the operator marks
it; interpretation stays with the sources. **confidence: tested (form) · rare**

### Amendment note (no new number) — TIR-014 refinement

TIR-014 (את = object/patient marker) gains an event-semantics reading: in role terms,
et marks the **Theme slot** of the leaf's event frame; multiple et in one clause = the
complete Theme inventory (Gen 1:1; 1:16's three-part list). No behavior change — a
vocabulary bridge between the particle rules and the operator rules above.

---

## Sign-off asks (owner)

1. Approve TIR-026…033 as stated (or edit statements/limits inline) → I merge them into
   `logic/TREE_INTERPRETATION_RULES.md` with these numbers.
2. Decide whether LET / CMD! / LET? / THEN / PURPOSE / ONGOING / CMD-US become the
   canonical operator names in unit derivation logs (they're the experiment doc's
   vocabulary; naming is owner's call).
3. Note: role_rules v1 already *implements* these mappings mechanically as display
   labels; sign-off here upgrades them from display heuristics to citable
   interpretation rules for derivation work. The two stay versioned independently.

**Not claimed:** that the Torah "is" deontic logic etc. — these are disciplined reading
rules for what the forms visibly do, each with limits stated. Not binding religious law.
