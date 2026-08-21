# Tree → logic interpretation rules (living catalog)

**Goal:** Build a **consistent, reusable rule set** for reading each verse’s **binary / ta'amim tree** into pre-code logic—so interpretation is not ad hoc per chapter.

**Aspiration:** **100% word use** — every Hebrew word in the verse tree is assigned a logic role (condition, outcome, number, reference, header, glue, etc.) under an explicit interpretation rule. Early units will fall short; gaps are logged and drive better rules.

**Status:** Seed catalog + particle/set-ops (TIR-014–022) + poetry block (TIR-023–025, 2026-07-27) + **form→operator block (TIR-026–033, owner-approved 2026-07-28)** + TIR-034 (prohibitive lo + imperfect in command frame; provisional, gen_08 freeze 2026-08-01). Rules below are provisional unless marked; promote only when they re-run cleanly on multiple units.

**Status note (2026-08-21, owner ruling):** this catalog is **model layer** under the re-derivation constitution — freely revisable, never owner-word class ("I think these rules should stay flexible"). It moved from the received-record class back to its born path `logic/TREE_INTERPRETATION_RULES.md` and is gloss-gated forward; the only edits made at reclassification were inline English glosses on citations that predated the gloss law. Discipline per rule change from here: a dated status note in this block, changelog-style — the gates catch any citing unit a change breaks.

**TIR-014 amendment (2026-07-28):** in event-frame vocabulary, את / et marks the **Theme slot** of the leaf's event; multiple et under one verb = the complete Theme inventory (Gen 1:1; 1:16). No behavior change — vocabulary bridge to TIR-026–033.

**Related:** `logic/SYSTEM.md`, `logic/units/lev_12_childbirth.yaml`, `logic/TUTORIAL_BEGINNERS.md`, `reviews/STANDING_DECISIONS.md` §6b–6c, `reviews/SCAN_gen_particles_et_gam_akh_raq_2026-07-25.md`, `logic/pre_logic_methods_2026-07-28/PROPOSAL_TIR_026_033_form_operators_2026-07-28.md` (evidence + corpus counts for 026–033)

---

## Principles

1. **Hebrew tree is primary** — roles come from OSHB `n=` structure + Hebrew content, not English paraphrase.
2. **Every word gets a role** — even if the role is “structure_header” or “glue_only.” Unused/unclassified words are **coverage failures**, not silent omissions.
3. **Consistent mapping** — the same tree pattern (e.g. etnachta pivot = condition head) should mean the same logical job across verses, unless a documented exception applies.
4. **Improve the rulebook, don’t hide gaps** — when a word doesn’t fit, add an `[OPEN]` note and a candidate rule; don’t pretend coverage is 100%.
5. **Always** `he` + `he_translit` + `en` on every word/role.

---

## Coverage targets

| Level | Meaning |
|-------|---------|
| **Accounted** | Word has a role tag (including pure structure) |
| **Logic-bearing** | Role feeds WHEN / THEN / state / restriction / ritual / reference |
| **100% use (aspiration)** | Every word is **accounted**; maximize **logic-bearing** where the text supports it; no silent leftovers |

Early phase: require **100% accounted**. Stretch toward richer logic-bearing use as the rule set grows.

---

## Seed interpretation rules (provisional)

IDs are stable so units can cite them (`interp_rule: TIR-001`).

| ID | Pattern (tree) | Maps to logic | Confidence | Notes / Lev 12 check |
|----|----------------|---------------|------------|----------------------|
| TIR-001 | Top split `n=1` head vs `n=0` head (typical etnachta / final) | First half often **condition/setup cluster**; second half often **consequence/status cluster** (verify per genre) | hypothesis | v2: `זָכָר` n=1 vs `תִּטְמָא` n=0 |
| TIR-002 | Strong pivot word at half-verse head that names a case feature (gender, animal type, …) | **WHEN / case pivot** | tested (Lev 12 male) | `זָכָר` / zakhar / "male" |
| TIR-003 | Number-word + time-unit under consequence subtree | **THEN duration** (numeric gloss from Hebrew only) | tested | `שִׁבְעַת יָמִים` → 7 |
| TIR-004 | Dual/plural time morphology (e.g. dual “weeks”) | Duration via morphology, not English “14” first | tested | `שְׁבֻעַיִם` → 14 |
| TIR-005 | Additive number pairs (thirty+three, sixty+six) | Sum gloss after reading both Hebrew number words | tested | 33, 66 |
| TIR-006 | Comparison phrase “as / like …” under reference subtree | **Reference link**, not a second independent counter unless text adds numbers | tested | niddah comparison |
| TIR-007 | Divine/relay address subtree (speak to… saying) | **Header only** — never IF | tested | v1–v2a |
| TIR-008 | Words with **no** `n=` | **Bound** into neighboring phrase; inherit that phrase’s role; still listed individually for 100% accounting | tested | `כִּי`, `שִׁבְעַת`, … |
| TIR-009 | Status verbs (impure / pure / sit) | **State** or THEN-status | tested | `טָמְאָה` / tam'ah / "she-is-impure", `תֵּשֵׁב` / teshev / "she-shall-sit", `טָהֲרָה` / tohorah / "purification" |
| TIR-010 | Restriction clauses “do not … until …” | **Guards / rules** until completion event | tested | v4 holy / sanctuary |
| TIR-011 | Parallel case marker (`וְאִם` / ve-im / "and-if" + alternate feature) | New decision-table **row** | tested | female path v5 |
| TIR-012 | Shared close “for X or for Y” | Unifies prior case rows under one ritual/outcome | tested | v7 male or female |
| TIR-013 | Poverty / inability branch | Alternate THEN on same outcome class | tested | v8 two birds |
| TIR-014 | Standalone **את** / *et* / object marker (and **ואת** / *ve-et* / "and-[object marker]") before a definite NP | Role **`glue_object_marker`**: binds verb → definite patient; **not** a free name; following NP is the payload (person, domain, blood, *kol*-total, …) | tested (Lev 1:5 ×3; Gen inventory verses) | See Gen scan `SCAN_gen_particles_et_gam_akh_raq_2026-07-25.md` |
| TIR-015 | **את X ואת Y** (parallel *et* … *ve-et* …) or multi-*et* under one verb | Role **`set_include_list`**: build **object inventory** / dual domains (creation pairs, plunder, genealogy children, family staging) | tested (Gen 1:1; 36:6; 25:2; …) | Written include-by-listing; BR *ribui* dual-track only when cited |
| TIR-016 | **את כל** / *et kol* / “et all …” | Role **`set_maximize`**: patient = entire class/total under the verb | tested (Gen *et kol* high frequency) | Maximizer, not ordinary NP |
| TIR-017 | **גם** / **וגם** / *gam* / *ve-gam* (“also/even”) | Role **`set_add`**: add agent, patient, time, or goods to a set already in play; **וגם את** = also + object-mark another patient | tested (Gen ~92 hits) | Written ribui-like; not object marker itself |
| TIR-018 | **אך** / *akh* (“but/only/just”) | Role **`set_limit` / `focus_restrict`**: narrow survivors, conditions, timing, kinship, or claims | tested (Gen 13 hits, e.g. 7:23, 9:4, 34:15) | School *mi’ut*; dual-track BR when named |
| TIR-019 | **רק** / *raq* (“only/except”) | Role **`set_except` / `exclusive_only`**: exception set or exclusive property (often near לא) | tested (Gen 11 hits, e.g. 24:8 *raq et beni*, 47:22) | BR 59:10 dual-track on 24:8 |
| TIR-020 | **את** + divine name (יהוה / אלהים) sparse | Role **`special_et_relation`**: do **not** auto-apply domain-expand; may be accompaniment/fence — verify per verse; Oral dual-track for BR school loci only (4:1, etc.) | hypothesis | Blocks false “every *et* expands domains” |
| TIR-021 | Same NP re-marked with **את** under a **new verb** | Role **`re_object_bind`**: new verb frame re-licenses object (not redundant waste) | tested (Lev 1:5 הדם under present + dash) | Gold Lev 1:5 |
| TIR-022 | Morph prefix on content word (ו- sequence, ה- definite, מ-/ל-/ב- prep) | Role **`morph_*`**: account under the leaf; prefix has a job; base may be free name | tested (מאהל / me-ohel / "from-the-tent", המזבח / ha-mizbeach / "the-altar", ושחט / ve-shachat / "and-he-slaughtered") | Letter-level only when morph job exists |
| TIR-023 | **Poetry dual A‖B** — top etnachta (or equivalent rank-1) split into two parallel instruction clusters: (a) dual imperative (positive ‖ `אל`-prohibition), or (b) parallel cause→effect ‖ cause→effect | Map to **dual instruction row(s)** (not path→end TIR-025; not single casuistic gender WHEN). Sub-bricks may be cause / effect / manner | **tested** (Prov 3:5 + Prov 15:1) | Units `prov_03_trust_know`, `prov_15_soft_harsh`; dehi often opens first brick before etnachta |
| TIR-024 | **Poetry command → divine result** — etnachta left = human imperative/jussive (often `דע` / know, `ב/כל דרכיך`…); right = 3sg agent (`והוא` / *ve-hu* / "and He") + result verb | Map to **WHEN command / THEN result** decision row (or COMMAND_THEN_RESULT step). Agent may be discourse-linked to prior divine name | **hypothesis** (Prov 3:6 only) | Distinct from TIR-023 and TIR-025. Pair with 3:5 in `prov_03_trust_know` |
| TIR-025 | **Poetry path-claim → end-result** — etnachta left = existence/appearance path (`יש דרך ישר` … `ל/פני איש`); right = end pivot (`אחרית` / acharit / "end") + outcome (`דרכי מות` / darkhei mavet / "ways of death" …) | Map to **WHEN path-as-before-man / THEN its-end**. Death (or other end) must stay in **THEN**, not smuggled into left arm via English. Exact // copies share **one** rule | **tested** (Prov 14:12 + // 16:25 same bracket) | Unit `prov_14_way_death`. Not dual imperative (TIR-023). Not divine-agent straighten (TIR-024) |
| TIR-026 | **Jussive verb** in divine/authorized speech: יְהִי / yehi / "let-there-be"; negated אַל־תָּצַר / al-tatzar / "do-not-harass" | **LET(p)** — directive on third party/state; אל + jussive → **LET-NOT(p)** prohibition; blessing register = same operator, optative tone | **tested** (whole-Torah, 193 hits) | Gen 1:3 · Num 6:25 יָאֵר / ya'er / "may-He-shine" (priestly blessing) · Deut 2:9. Approved 2026-07-28 |
| TIR-027 | **Imperative**: דַּבֵּר / dabber / "speak!" | **CMD!(p)** — direct order with addressee slot (tun-sollen) | **tested** (784 hits) | Lev 1:2 · Deut 6:4 שְׁמַע / shema / "hear!" · Gen 1:28 פְּרוּ / peru / "be-fruitful!" — imperative can sit inside a blessing; operator records mood, not tone |
| TIR-028 | **Imperfect inside command speech**: יִשְׁרְצוּ / yishretzu / "let-swarm"; casuistic frames with כִּי / ki / "when" | **LET?(p)** — the `?` is part of the rule: form alone can't split command/future/permission. In casuistic law: protasis imperfect = IF-condition, apodosis imperfect = duty | **tested as flag**; resolution per-unit | Gen 1:20 · Lev 1:2 כִּי־יַקְרִיב / ki-yaqriv / "when-he-brings". **Forbids** silently upgrading imperfects to commands |
| TIR-029 | **Weqatal** (ve- + perfect, instructional): וְאָמַרְתָּ / ve-amarta / "and-you-shall-say" | **THEN(p)** — obligation/consequence sequenced after a prior condition or act; weqatal chains = ordered procedure | **tested** | Legal genre signature (Lev 707× · Deut 632× vs Gen 164×) · Deut 2:19 וְקָרַבְתָּ / ve-qaravta · Gen 1:14 וְהָיוּ / ve-hayu (spec clause). Narrative-future weqatal = sequence w/o obligation — unit labels which |
| TIR-030 | **ל + infinitive construct**: לְהַבְדִּיל / le-havdil / "to-divide" | **PURPOSE(p)** — goal slot on governing verb/object | **tested** | Gen 1:14 · Exod 2:16 לְהַשְׁקוֹת / le-hashqot / "to-water" · Gen 2:3 לַעֲשׂוֹת / la'asot (open-ended). ב/כ + inf. (temporal "when…") is NOT purpose — out of scope |
| TIR-031 | **Participle in predicate position**: מַבְדִּיל / mavdil / "dividing" | **ONGOING(p)** — standing state, not event; inside a spec → **INVARIANT(p)** (condition that must keep holding) | **tested** | Gen 1:2 מְרַחֶפֶת / merachefet / "hovering" · Gen 1:6 · Deut 1:4 יוֹשֵׁב / yoshev / "dwelling". Nominal participles ("inhabitant") stay NP — leaf context decides |
| TIR-032 | **Niphal/pual in directive or outcome slot**: יִקָּווּ / yiqqavu / "be-gathered"; וְנִרְצָה / ve-nirtza / "shall-be-accepted" | **Agentless state-constraint** — obligates/reports an end-state with doer unspecified (sein-sollen: ought-to-BE vs ought-to-DO) | **tested** (forms) · significance hypothesis | Gen 1:9 · **Lev 1:4 ve-nirtza — korban acceptance never priest-performed; the stem carries that structurally** · Gen 2:1 וַיְכֻלּוּ / va-yekhullu / "were-completed". Plain narrative passives = ordinary events |
| TIR-033 | **Cohortative / 1cp volitive**: נַעֲשֶׂה / na'aseh / "let-US-make" | **CMD-US(p)** — self-directive, speaker ∈ agents (deliberation/resolve) | **tested** (form) · rare | Gen 1:26 (coded imperfect → TIR-028's `?` applies) · Gen 11:7 נֵרְדָה / nerda / "let-us-go-down" (Babel echo). Plural anomaly stays with named Oral (BR 8:3; Sanhedrin 38b) |
| TIR-034 | **לֹא / lo + imperfect 2nd-person INSIDE an explicit command frame** (a governing צוה / tzavah / "command" verb + לֵאמֹר / le-mor / "saying"): לֹא תֹאכַל / lo tokhal / "you shall not eat" | **LET-NOT(p)** — the ABSOLUTE prohibition (vs TIR-026's אל + jussive vetitive: immediate/particular). The command FRAME is the disambiguator TIR-028 says the bare form lacks — without a frame, negated imperfect stays flagged (forecast vs directive undecidable from form). CONTRACT: LET-NOT is not a ?-mood — it has NO resolution path; no citation flips a prohibition (run_unit.py contract_let_not_never_resolves) | **provisional** (gen_08 freeze, 2026-08-01; promote on re-run over the Decalogue's ten lo-forms) | **Gen 2:17 — the corpus's FIRST prohibition** (first lo + Vqi2ms token; DB-verified); second token Gen 3:17 quotes it back in the sentence. The corpus's own proof of the form ambiguity: the serpent's Gen 3:4 לֹא־מוֹת תְּמֻתוּן / lo mot temutun re-reads the construction as (false) FORECAST. The Decalogue's prohibitions are this form (Exod 20:3-17) |

**Related research:**  
- Genesis full scan: `reviews/SCAN_gen_particles_et_gam_akh_raq_2026-07-25.md`  
- Spine glue scan: `reviews/sanctuary_spine_v1/SCAN_glue_morph_patterns_2026-07-25.md`  
- BR school: `reviews/RESEARCH_BR_particles_2026-07-21.md`  
- Gold coverage: `reviews/sanctuary_spine_v1/GOLD_lev_1_5_full_word_coverage_2026-07-25.md`  
- Poetry units: `logic/units/prov_03_trust_know.yaml`, `logic/units/prov_14_way_death.yaml`

**Not yet rules (open research):** multiple-etnachta (etnachta, the major mid-verse pause accent) edge cases; how far header nesting depth ever becomes logic; automatic *et* “with God” vs object sense classifier; full Exod–Deut particle density comparison; promote TIR-023 after a second dual-imperative unit (e.g. Prov 15:1); promote TIR-024 after another divine-result dual.

**Poetry structure note:** ta’amim parse ranks live under `logic/taamim_rules/v3/` (CURRENT); interpretation roles (this file) are separate from parse ranks.

---

## Per-unit requirement: `binary_trees` first, then `tree_coverage`

**Structure record (required):** unit section **`binary_trees`** — `rule_set_version`, top split, full `tree_ascii` from the parser, `maps_to` logic ids.  
See `logic/SHOW_WORK_TREES_2026-07-20.md` and `reviews/STANDING_DECISIONS.md` §6a.  
`tree_coverage` is the **role layer** on those leaves; it does **not** replace storing the tree.

## Per-unit requirement: `tree_coverage`

Each new (or revised) unit should include a **tree_coverage** section (or table) that, for every word in every verse tree:

| Field | Purpose |
|-------|---------|
| `he` / `he_translit` / `en` | Identity |
| `oshb_n` | Tree address or `null` if bound |
| `role` | e.g. `when_pivot`, `then_number`, `header`, `glue`, `glue_object_marker`, `set_add`, `set_limit`, `set_include_list`, `set_maximize`, `re_object_bind`, `morph_vav_seq`, `morph_ha_def`, `reference`, `restrict`, `ritual`, `open` |
| `interp_rule` | TIR-xxx or `none` |
| `feeds` | Logic ids (row/rule/state) or empty |
| `confidence` | hypothesis / tested / … |

**Metrics to record:**

- `% accounted` (target: 100% always)  
- `% with interp_rule` (grows over time)  
- `% logic-bearing` (grows where justified)  
- list of `role: open` words → backlog for new TIR rules  

---

## How the catalog grows

1. Derive a unit with binary trees — **write them into `binary_trees`** (show all work).  
2. Fill `tree_coverage` for **every** word.  
3. Any `open` or inconsistent mapping → propose a new **TIR-xxx** (or revise an existing one).  
4. Re-test the rule on at least one prior unit (e.g. Lev 12) before calling it `tested`.  
5. Prefer **consistent** rules over one-off cleverness.

---

## Honest baseline (Lev 12 first pass)

First Lev 12 unit: strong use of pivots + numbers + ritual; headers/glue accounted as structure; **not** yet 100% logic-bearing, and not every word cited a TIR id.  
That gap is **expected** and is the reason this catalog exists.
