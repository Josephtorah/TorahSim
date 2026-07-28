# Experiment — Gen 1:1–2:3 (the full creation week) in well-known pre-code logic

**Date:** 2026-07-28 (first written 2026-07-27 for vv. 1–10; extended to the full week 2026-07-28)
**Kind:** formalization experiment · **hypothesis** · not binding law · no code — paper logic only
**Scope:** all 34 verses of the week — Gen 1:1–31 + 2:1–3 (day 7 crosses the chapter break)
**Input:** the auto roles of `GEN_1_1_to_2_3_flat_ledger_morph_2026-07-28.html` (ta'amim v3 leaves — all 34 parse `unique` · pure binary — + OSHB morph frames, 237 bricks, full coverage)
**Source of truth:** Hebrew only; all logic lines below are *readings of* the Hebrew roles, in English notation as an aid
**Formalisms used (all established, none invented here):**

| Layer | Formalism | Age / origin |
|-------|-----------|--------------|
| Speech acts | Austin performatives; DECLARE | 1950s |
| Directives | von Wright deontic logic; LET(p) ≈ O(p) | 1951 |
| Events + roles | (neo-)Davidsonian event semantics; Agent/Theme/Location | 1967 |
| Sequence | Prior temporal logic; timeline + COMMIT | 1950s |
| Spec / verify | Hoare triples {P} op {Q} — paper annotation logic | 1969 |
| Legal IF/THEN | casuistic law form (Alt's biblical-law distinction) | ancient / 1930s scholarship |

**Notation legend (fixed for this document):**

| Notation | Meaning |
|----------|---------|
| `DECLARE(a, φ)` | speech act: agent a utters directive φ |
| `LET(φ)` | directive from **jussive** form ("let it be that φ") ≈ deontic O(φ) |
| `LET?(φ)` | directive from **imperfect** form — command reading is hypothesis |
| `∃e P(e) ∧ Agent(e,a) ∧ Theme(e,x)` | event e of type P, doer a, done-to x (את-marked → Theme) |
| `HOLDS(σ, t)` | state σ obtains at time t |
| `INVARIANT(φ)` | standing condition from **participle** (ongoing, not one event) |
| `{P} op {Q}` | Hoare triple: precondition, operation, postcondition |
| `RESULT ✓` | ויהי־כן / va-yehi khen — postcondition asserted true |
| `PASS(tov, x)` | acceptance test: God sees x is good (tov = oracle, not defined in-text) |
| `name(x) := "N"` | performative naming — registry assignment, not a truth claim |
| `COMMIT(day n)` | evening+morning cycle closes and labels the unit |
| `t₀ < t₁ < …` | timeline order |

Hebrew below is always he / translit / English (owner rule: never bare Hebrew).

---

## Verse 1 — the root event

> **he:** בְּרֵאשִׁית בָּרָא אֱלֹהִים אֵת הַשָּׁמַיִם וְאֵת הָאָרֶץ
> **tr:** be-reshit bara Elohim et ha-shamayim ve-et ha-aretz
> **en:** "In the beginning God created the heavens and the earth."
> **roles:** PREP(in·beginning) · CREATE · OBJ_FRAME(heavens) · OBJ_FRAME(earth)

```text
L1  t₀ := reshit                                  — timeline origin installed by the PREP frame
L2  ∃e₁ create(e₁) ∧ Agent(e₁, Elohim)
        ∧ Theme(e₁, shamayim) ∧ Theme(e₁, aretz)
        ∧ Time(e₁, t₀)                            — perfect form = completed narrative event
L3  exists(shamayim) ∧ exists(aretz)   after e₁   — the two את/et frames give the full Theme
                                                    inventory (TIR-014: et = patient marker)
L4  registry := { shamayim "heavens", aretz "earth" }
```

**Note:** the two et-phrases are a closed list — event semantics makes the double-Theme
explicit where English "the heavens and the earth" hides it. *confidence: tested (structure), hypothesis (registry reading)*

---

## Verse 2 — the precondition block

> **he:** וְהָאָרֶץ הָיְתָה תֹהוּ וָבֹהוּ וְחֹשֶׁךְ עַל־פְּנֵי תְהוֹם וְרוּחַ אֱלֹהִים מְרַחֶפֶת עַל־פְּנֵי הַמָּיִם
> **tr:** ve-ha-aretz hayta tohu va-vohu ve-choshekh al-penei tehom ve-ruach Elohim merachefet al-penei ha-mayim
> **en:** "The earth was formless and void, darkness over the deep, God's spirit hovering over the waters."
> **roles:** DOMAIN(earth) · BECOME/WAS · NP(void) · DOMAIN(darkness) · PREP(over·face·deep) · NP(spirit·God) · ONGOING(hovering) · PREP(over·face·waters)

```text
L1  HOLDS( tohu(aretz) ∧ vohu(aretz), t₀ )        — perfect "hayta": state, not action
L2  HOLDS( over(choshekh, face(tehom)), t₀ )      — verbless clause = pure state predicate
L3  INVARIANT( hover(ruach-Elohim,
               face(mayim)) ) during t₀           — participle = ongoing condition, no event
```

**This whole verse is P** — the precondition block for the first triple. It contains **zero
events** (no wayyiqtol anywhere); the morphology alone shows v2 is a state description.
*confidence: tested*

---

## Verse 3 — the minimal fiat (the cleanest triple in the corpus)

> **he:** וַיֹּאמֶר אֱלֹהִים יְהִי אוֹר וַיְהִי־אוֹר
> **tr:** va-yomer Elohim yehi or va-yehi or
> **en:** "God said: let there be light — and there was light."
> **roles:** SPEAK(agent=Elohim) · CMD(be) · RESULT(light)

```text
L1  DECLARE( Elohim, LET(exists(or)) )            — speech act wrapping a jussive directive
L2  { ¬exists(or) }   yehi or   { exists(or) }    — Hoare triple; P from v2's darkness state
L3  HOLDS( exists(or), t₁ )                       — wayyiqtol: postcondition asserted
```

**Grammar echo:** spec and result are the *same root, same letters* — יְהִי / yehi (jussive,
the spec) vs וַיְהִי / va-yehi (wayyiqtol, the event). The mood morpheme alone carries
the difference between "{Q} demanded" and "{Q} holds." *confidence: tested*

---

## Verse 4 — acceptance test + partition

> **he:** וַיַּרְא אֱלֹהִים אֶת־הָאוֹר כִּי־טוֹב וַיַּבְדֵּל אֱלֹהִים בֵּין הָאוֹר וּבֵין הַחֹשֶׁךְ
> **tr:** va-yar Elohim et-ha-or ki-tov va-yavdel Elohim bein ha-or u-vein ha-choshekh
> **en:** "God saw the light, that it was good, and God divided the light from the darkness."
> **roles:** SEE/ASSESS · LIGHTS +et-obj · EVAL(good) · DIVIDE · BETWEEN(light) · BETWEEN(darkness)

```text
L1  ∃e₂ see(e₂) ∧ Agent(e₂, Elohim) ∧ Theme(e₂, or)
L2  PASS( tov, or )                                — acceptance test; tov is an oracle predicate
                                                     (no definition of "good" appears in-text)
L3  ∃e₃ divide(e₃) ∧ Agent(e₃, Elohim)
        ∧ between(e₃, or, choshekh)                — the two bein-frames are one 2-place relation
L4  after e₃:  or ∩ choshekh = ∅                   — separation read as set partition
```

**Note:** L2 is *epistemic* — "saw **that** good" wraps evaluation inside perception
(K_Elohim(tov(or))). Logic can mark where the test happens; it cannot compute tov.
*confidence: L1–L3 tested · L4 hypothesis*

---

## Verse 5 — naming + first commit

> **he:** וַיִּקְרָא אֱלֹהִים לָאוֹר יוֹם וְלַחֹשֶׁךְ קָרָא לָיְלָה וַיְהִי־עֶרֶב וַיְהִי־בֹקֶר יוֹם אֶחָד
> **tr:** va-yiqra Elohim la-or yom ve-la-choshekh qara layla va-yehi erev va-yehi voqer yom echad
> **en:** "God called the light Day, and the darkness he called Night; evening, morning — day one."
> **roles:** NAME · DOMAIN(day/night) · PREP(to·darkness) · NAME · TIME-STAMP · DAY-COUNT(one)

```text
L1  name(or)       := "yom"                        — performative: registry write, not assertion
L2  name(choshekh) := "layla"                      — the ל/la dative marks the naming target
L3  cycle( erev → boqer )                          — temporal frame closes
L4  COMMIT( day 1 )                                — note: אחד/echad = cardinal "one",
                                                     not ordinal "first" (unlike days 2–4)
```

**Day-1 unit is now a complete verified transaction:** P (v2) → fiat (v3) → test PASS +
partition (v4) → naming + commit (v5). *confidence: tested (pattern); naming-as-registry = hypothesis*

---

## Verse 6 — a spec with an invariant (day 2 opens)

> **he:** וַיֹּאמֶר אֱלֹהִים יְהִי רָקִיעַ בְּתוֹךְ הַמָּיִם וִיהִי מַבְדִּיל בֵּין מַיִם לָמָיִם
> **tr:** va-yomer Elohim yehi raqia be-tokh ha-mayim vi-yhi mavdil bein mayim la-mayim
> **en:** "God said: let there be a firmament amid the waters, and let it be a divider between waters and waters."
> **roles:** SPEAK(agent=Elohim) · CMD(be) · PREP(in·midst·waters) · CMD?(be) · ONGOING(divide) · BETWEEN(waters)

```text
L1  DECLARE( Elohim,
      LET( exists(raqia) ∧ loc(raqia, midst(mayim)) )      — jussive: the object
      ∧ LET?( INVARIANT( separates(raqia,
                          mayim_upper, mayim_lower) ) ) )   — imperfect+participle: its JOB
```

**This is a two-part spec: existence + standing function.** The participle מַבְדִּיל /
mavdil / "dividing" makes the divider role an *invariant* — a condition that must keep
holding — not a one-time act. Day 1 demanded a thing; day 2 demands a thing **with a job**.
*confidence: tested (forms) · LET? flagged as hypothesis by its own morphology*

---

## Verse 7 — implementation of the v6 spec

> **he:** וַיַּעַשׂ אֱלֹהִים אֶת־הָרָקִיעַ וַיַּבְדֵּל בֵּין הַמַּיִם אֲשֶׁר מִתַּחַת לָרָקִיעַ וּבֵין הַמַּיִם אֲשֶׁר מֵעַל לָרָקִיעַ וַיְהִי־כֵן
> **tr:** va-yaas Elohim et-ha-raqia va-yavdel bein ha-mayim asher mi-tachat la-raqia u-vein ha-mayim asher me-al la-raqia va-yehi-khen
> **en:** "God made the firmament and divided the waters under it from the waters above it — and it was so."
> **roles:** MAKE +et-obj · DIVIDE · REL(waters-under) · REL(waters-above) · RESULT(so)

```text
L1  ∃e₄ make(e₄) ∧ Agent(e₄, Elohim) ∧ Theme(e₄, raqia)     — execution event (wayyiqtol)
L2  W_under := { x : water(x) ∧ under(x, raqia) }            — the אשר/asher REL-clauses are
    W_above := { x : water(x) ∧ above(x, raqia) }              set-builder definitions
L3  ∃e₅ divide(e₅) ∧ between(e₅, W_under, W_above)
L4  RESULT ✓        — va-yehi khen: spec of v6 now holds     — postcondition check passes
```

**Spec vs implementation:** v6 is DECLARE+LET (directive mood), v7 is make+divide
(narrative mood) on the *same objects*. The relative clauses upgrade v6's vague
"waters ↔ waters" into two **defined sets**. *confidence: tested*

---

## Verse 8 — commit without the test

> **he:** וַיִּקְרָא אֱלֹהִים לָרָקִיעַ שָׁמָיִם וַיְהִי־עֶרֶב וַיְהִי־בֹקֶר יוֹם שֵׁנִי
> **tr:** va-yiqra Elohim la-raqia shamayim va-yehi erev va-yehi voqer yom sheni
> **en:** "God called the firmament Heavens; evening, morning — a second day."
> **roles:** NAME · TIME-STAMP · DAY-COUNT(second)

```text
L1  name(raqia) := "shamayim"                      — aliasing note: same label installed
                                                     for a v1 registry entry (see below)
L2  cycle( erev → boqer );  COMMIT( day 2 )
L3  ⚠ no PASS(tov, ·) anywhere in day 2            — the acceptance test is ABSENT
```

**Two honest observations the formalism surfaces:** (1) day 2 commits **without** an
EVAL step — the only day in 1:1–10 missing its test (a gap the Oral tradition also
noticed; named-Oral only, not merged here); (2) the label "shamayim" now points at the
raqia — either an alias or a re-binding of v1's registry entry. Logic can state the
collision; it cannot resolve it. *confidence: observation (absence is in the text)*

---

## Verse 9 — agentless directives (day 3 opens)

> **he:** וַיֹּאמֶר אֱלֹהִים יִקָּווּ הַמַּיִם מִתַּחַת הַשָּׁמַיִם אֶל־מָקוֹם אֶחָד וְתֵרָאֶה הַיַּבָּשָׁה וַיְהִי־כֵן
> **tr:** va-yomer Elohim yiqqavu ha-mayim mi-tachat ha-shamayim el-maqom echad ve-tera'e ha-yabasha va-yehi-khen
> **en:** "God said: let the waters under the heavens be gathered to one place, and let the dry land be seen — and it was so."
> **roles:** SPEAK(agent=Elohim) · CMD(be-gathered) · PREP(from·heavens) · NP(place·one) · CMD?(be-seen) · DRY-LAND · RESULT(so)

```text
L1  DECLARE( Elohim,
      LET( gathered(W_under, into: one(maqom)) )    — niphal jussive: PASSIVE directive;
      ∧ LET?( visible(yabasha) ) )                    no gathering agent is named
L2  RESULT ✓                                        — both postconditions asserted at once
```

**What the niphal adds:** these are constraints on *end states*, not commands to an
actor — "let the waters BE gathered", "let the dry land BE seen." Deontic logic has
exactly this distinction (obligation-to-be vs obligation-to-do, *sein-sollen* vs
*tun-sollen*), and the Hebrew stem system encodes it natively. Note also there is **no
creation verb in day 3a** — only rearrangement and revelation of what exists.
*confidence: tested (voice) · reading as sein-sollen = hypothesis*

---

## Verse 10 — double naming + test PASS

> **he:** וַיִּקְרָא אֱלֹהִים לַיַּבָּשָׁה אֶרֶץ וּלְמִקְוֵה הַמַּיִם קָרָא יַמִּים וַיַּרְא אֱלֹהִים כִּי־טוֹב
> **tr:** va-yiqra Elohim la-yabasha eretz u-le-miqveh ha-mayim qara yamim va-yar Elohim ki-tov
> **en:** "God called the dry land Earth, and the gathering of waters he called Seas; and God saw that it was good."
> **roles:** NAME · DRY-LAND · PREP(to·gathering·waters) · NAME · SEE/ASSESS · EVAL(good)

```text
L1  name(yabasha)      := "eretz"                  — second label collision: "eretz" was
L2  name(miqveh-mayim) := "yamim"                    installed in v1 for the whole domain
L3  PASS( tov, ⟨gathering-arrangement⟩ )           — test runs mid-day: day 3 gets TWO
                                                     evaluations (here + v12), zero in day 2
```

*confidence: tested (structure) · label-collision resolutions: see §Named Oral below (was [OPEN])*

---

## Day 3b — flora (vv. 11–13): delegation and the first spec deviation

> **v11 he:** וַיֹּאמֶר אֱלֹהִים תַּדְשֵׁא הָאָרֶץ דֶּשֶׁא עֵשֶׂב מַזְרִיעַ זֶרַע עֵץ פְּרִי עֹשֶׂה פְּרִי לְמִינוֹ אֲשֶׁר זַרְעוֹ־בוֹ עַל־הָאָרֶץ וַיְהִי־כֵן
> **tr:** va-yomer Elohim tadshe ha-aretz deshe, esev mazria zera, etz peri oseh peri le-mino asher zar'o-vo al-ha-aretz — va-yehi khen
> **en:** "God said: let the earth sprout grass, seed-bearing herb, fruit-tree making fruit by its kind with its seed in it — and it was so."
> **roles:** SPEAK · CMD(sprout) · ONGOING(yield-seed) · KIND · REL(seed) · RESULT(so)

```text
L1  DECLARE( Elohim, LET( sprout(aretz, flora) ) )      — the EARTH is the commanded agent:
                                                          first delegated execution of the week
L2  spec(flora): esev with INVARIANT(yield-seed)         — participle: self-replication built in
    ∧ etz-PERI by KIND(min) with seed-in-it (asher = set-def)
L3  RESULT ✓ same verse — but see v12 for what actually grew
```

> **v12 he:** וַתּוֹצֵא הָאָרֶץ דֶּשֶׁא עֵשֶׂב מַזְרִיעַ זֶרַע לְמִינֵהוּ וְעֵץ עֹשֶׂה־פְּרִי אֲשֶׁר זַרְעוֹ־בוֹ לְמִינֵהוּ וַיַּרְא אֱלֹהִים כִּי־טוֹב
> **tr:** va-totze ha-aretz deshe, esev mazria zera le-minehu, ve-etz oseh-peri asher zar'o-vo le-minehu — va-yar Elohim ki-tov
> **en:** "The earth brought forth grass, seed-bearing herb by kind, and tree MAKING fruit with its seed in it by kind; and God saw that it was good."
> **roles:** BRING_FORTH (Agent = aretz!) · ONGOING(yield-seed) · KIND · REL(seed) · SEE/ASSESS · EVAL(good)

```text
L1  ∃e bring-forth(e) ∧ Agent(e, ARETZ)                 — the earth executes, not God
L2  DELTA(spec, result):  spec עֵץ פְּרִי / etz PERI / "fruit-tree"
                          got  עֵץ עֹשֶׂה־פְּרִי / etz OSEH-peri / "tree MAKING fruit"
    — the only day where the delivered product's wording differs from the spec
L3  PASS( tov, flora )                                   — the test passes DESPITE the delta
```

**v13** — cycle(erev→boqer); **COMMIT(day 3)** — the only day with two PASS entries (v10, v12).
*confidence: tested (forms; the delta is in the letters) · significance of delta = named Oral (§ below)*

---

## Day 4 — luminaries (vv. 14–19): a job-heavy spec, and no names

> **v14–15 he:** וַיֹּאמֶר אֱלֹהִים יְהִי מְאֹרֹת בִּרְקִיעַ הַשָּׁמַיִם לְהַבְדִּיל בֵּין הַיּוֹם וּבֵין הַלָּיְלָה וְהָיוּ לְאֹתֹת וּלְמוֹעֲדִים וּלְיָמִים וְשָׁנִים · וְהָיוּ לִמְאוֹרֹת … לְהָאִיר עַל־הָאָרֶץ וַיְהִי־כֵן
> **tr:** yehi me'orot bi-rqia ha-shamayim le-havdil bein ha-yom u-vein ha-layla, ve-hayu le-otot u-le-mo'adim u-le-yamim ve-shanim; ve-hayu li-m'orot … le-ha'ir al-ha-aretz — va-yehi khen
> **en:** "Let there be lights in the firmament of the heavens to divide day from night; and they shall be for signs, seasons, days, years; and they shall be lights … to give light on the earth — and it was so."
> **roles:** CMD(be) · PURPOSE(divide) · BETWEEN(day/night) · THEN(be) ×2 · PURPOSE(give-light) · RESULT(so)

```text
L1  DECLARE( Elohim, LET(exists(me'orot) ∧ loc(rqia-ha-shamayim))
      ∧ PURPOSE(divide(yom, layla))
      ∧ THEN(serve-as: signs, seasons, days, years)
      ∧ THEN(be-lights) ∧ PURPOSE(give-light(aretz)) )
L2  RESULT ✓ (v15) — four distinct JOBS in one spec: divide, mark-time, shine, (rule: added at build)
```

> **v16–18 he:** וַיַּעַשׂ אֱלֹהִים אֶת־שְׁנֵי הַמְּאֹרֹת הַגְּדֹלִים אֶת־הַמָּאוֹר הַגָּדֹל לְמֶמְשֶׁלֶת הַיּוֹם וְאֶת־הַמָּאוֹר הַקָּטֹן לְמֶמְשֶׁלֶת הַלַּיְלָה וְאֵת הַכּוֹכָבִים · וַיִּתֵּן אֹתָם … · וְלִמְשֹׁל … וּלֲהַבְדִּיל … וַיַּרְא אֱלֹהִים כִּי־טוֹב
> **tr:** va-ya'as Elohim et-shnei ha-me'orot ha-gedolim — et ha-ma'or ha-gadol le-memshelet ha-yom, ve-et ha-ma'or ha-qaton le-memshelet ha-layla — ve-et ha-kokhavim; va-yiten otam …; ve-limshol … u-la-havdil … va-yar Elohim ki-tov
> **en:** "God made the two great lights — the greater for dominion of day, the smaller for dominion of night — and the stars; God set them …; and to rule … and to divide …; and God saw that it was good."
> **roles:** MAKE +et-obj · RULE/DOMINION · SET/PLACE · PURPOSE(give-light) · PURPOSE(rule) · PURPOSE(divide) · EVAL(good)

```text
L1  ∃e₆ make(e₆) ∧ Theme(shnei-ha-me'orot) — three et-frames give the full inventory (2 lights + stars)
L2  DELTA(spec, build): the spec never said TWO, never ranked them, never mentioned stars.
    Execution introduces: hierarchy (gadol/qaton → dominion roles) + an appended Theme (kokhavim)
L3  ∃e₇ set(e₇, loc: rqia-ha-shamayim) ∧ PURPOSE ×3 read back (give-light · rule · divide)
L4  PASS( tov ) — v18
```

**v19** — **COMMIT(day 4)**. Two registry silences worth logging: **the luminaries are never
named** (descriptors only — "the great one," "the small one"), and there is **no blessing**.
The naming formula has not fired since v10. *confidence: tested*

---

## Day 5 — sea and sky life (vv. 20–23): bara returns, RESULT vanishes, blessing appears

> **v20 he:** וַיֹּאמֶר אֱלֹהִים יִשְׁרְצוּ הַמַּיִם שֶׁרֶץ נֶפֶשׁ חַיָּה וְעוֹף יְעוֹפֵף עַל־הָאָרֶץ עַל־פְּנֵי רְקִיעַ הַשָּׁמָיִם
> **tr:** yishretzu ha-mayim sheretz nefesh chayah, ve-of ye'ofef al-ha-aretz al-penei reqia ha-shamayim
> **en:** "Let the waters swarm with swarms of living beings, and let flyers fly over the earth across the face of the firmament of the heavens."
> **roles:** SPEAK · CMD?(swarm) · LIVING · CMD?(fly) · PREP(over·face)

```text
L1  DECLARE( Elohim, LET?(swarm(mayim, sheretz-nefesh-chayah)) ∧ LET?(fly(of, over aretz)) )
    — both directives imperfect-form (CMD?), both aimed at domains, not agents
L2  ⚠ NO va-yehi khen anywhere in day 5 — the RESULT ✓ operator is absent
```

> **v21 he:** וַיִּבְרָא אֱלֹהִים אֶת־הַתַּנִּינִם הַגְּדֹלִים וְאֵת כָּל־נֶפֶשׁ הַחַיָּה הָרֹמֶשֶׂת אֲשֶׁר שָׁרְצוּ הַמַּיִם לְמִינֵהֶם וְאֵת כָּל־עוֹף כָּנָף לְמִינֵהוּ וַיַּרְא אֱלֹהִים כִּי־טוֹב
> **tr:** va-yivra Elohim et-ha-taninim ha-gedolim ve-et kol-nefesh ha-chayah ha-romeset asher shartzu ha-mayim le-minehem ve-et kol-of kanaf le-minehu — va-yar Elohim ki-tov
> **en:** "God created the great sea-creatures, and every living creeping being with which the waters swarmed by their kinds, and every winged flyer by its kind; and God saw that it was good."
> **roles:** CREATE +et-obj · SEA-MONSTERS · ONGOING(creep) · KIND · SEE/ASSESS · EVAL(good)

```text
L1  ∃e₈ CREATE(e₈) — בָּרָא / bara returns for the first time since 1:1;
    in place of the missing RESULT ✓, the strongest creation verb appears
L2  three et-frames = full Theme inventory (taninim · every living mover · every winged flyer)
L3  PASS( tov )
```

> **v22 he:** וַיְבָרֶךְ אֹתָם אֱלֹהִים לֵאמֹר פְּרוּ וּרְבוּ וּמִלְאוּ אֶת־הַמַּיִם בַּיַּמִּים וְהָעוֹף יִרֶב בָּאָרֶץ
> **tr:** va-yevarekh otam Elohim lemor: peru u-revu u-mil'u et-ha-mayim ba-yamim, ve-ha-of yirev ba-aretz
> **en:** "God blessed them, saying: be fruitful, multiply, fill the waters in the seas — and let the flyers multiply on the earth."
> **roles:** BLESS +et-obj · CMD!(be-fruitful) · CMD!(fill) · CMD(multiply)

```text
L1  ∃e₉ bless(e₉, Theme: them) ∧ DECLARE( …, CMD!(peru) ∧ CMD!(revu) ∧ CMD!(mil'u) ∧ LET(yirev, of) )
L2  FIRST second-person imperatives of the week — addressees now exist that can receive commands.
    The blessing = delegated self-replication, spoken TO the creatures (flora got it as a silent
    INVARIANT in v11; fauna get it as an address)
```

**v23** — **COMMIT(day 5)**. *confidence: tested (forms) · "bara replaces vayehi-khen" as pattern = hypothesis*

---

## Day 6 — land life and the human (vv. 24–31): agent swap, the plural spec, triple bara

> **v24 he:** וַיֹּאמֶר אֱלֹהִים תּוֹצֵא הָאָרֶץ נֶפֶשׁ חַיָּה לְמִינָהּ בְּהֵמָה וָרֶמֶשׂ וְחַיְתוֹ־אֶרֶץ לְמִינָהּ וַיְהִי־כֵן
> **tr:** totze ha-aretz nefesh chayah le-minah: behemah va-remes ve-chayto-eretz le-minah — va-yehi khen
> **en:** "Let the earth bring forth living beings by their kind: livestock, creepers, wild animals of the earth by kind — and it was so." · **roles:** CMD?(bring-forth) · LIVESTOCK · CREEPERS · KIND · RESULT(so)

> **v25 he:** וַיַּעַשׂ אֱלֹהִים אֶת־חַיַּת הָאָרֶץ לְמִינָהּ וְאֶת־הַבְּהֵמָה לְמִינָהּ וְאֵת כָּל־רֶמֶשׂ הָאֲדָמָה לְמִינֵהוּ וַיַּרְא אֱלֹהִים כִּי־טוֹב
> **tr:** va-ya'as Elohim et-chayat ha-aretz le-minah ve-et ha-behemah le-minah ve-et kol-remes ha-adamah le-minehu — va-yar Elohim ki-tov
> **en:** "God MADE the wild animals … the livestock … every creeper of the ground; and God saw that it was good." · **roles:** MAKE +et-obj ×3 · KIND · EVAL(good)

```text
L1  AGENT SWAP: v24 delegates to the earth (as v11 did) — but v25's executor is GOD (va-ya'as Elohim).
    Mirror image of day 3b: there, earth executed and the product drifted;
    here, delegation is issued and God executes directly. No blessing for land animals.
```

> **v26 he:** וַיֹּאמֶר אֱלֹהִים נַעֲשֶׂה אָדָם בְּצַלְמֵנוּ כִּדְמוּתֵנוּ וְיִרְדּוּ בִדְגַת הַיָּם וּבְעוֹף הַשָּׁמַיִם וּבַבְּהֵמָה וּבְכָל־הָאָרֶץ וּבְכָל־הָרֶמֶשׂ הָרֹמֵשׂ עַל־הָאָרֶץ
> **tr:** na'aseh adam be-tzalmenu ki-dmutenu, ve-yirdu vi-dgat ha-yam u-ve-of ha-shamayim u-va-behemah u-ve-khol-ha-aretz u-ve-khol-ha-remes ha-romes al-ha-aretz
> **en:** "Let US make a human in OUR image, after OUR likeness; and let them rule the fish of the sea, the flyers of the heavens, the livestock, all the earth, and every creeper that creeps on the earth."
> **roles:** SPEAK · CMD?(make) · IMAGE/LIKENESS · CMD(rule-over) · dominion list ×5

```text
L1  DECLARE( Elohim, LET?( make(WE, adam, attr: OUR-image, OUR-likeness) )
      ∧ LET( rule-over(THEY, [fish, flyers, livestock, all-earth, creepers]) ) )
L2  ⚠ the ONLY first-person-plural spec of the week: na'aseh "let US", tzalmeNU "OUR image".
    Every other fiat is impersonal ("let there be"). Who is "us"? → §Named Oral
L3  note the number plan: make (sg object "adam") … and let THEM rule (plural) — plurality
    is already inside the spec before v27 executes it
```

> **v27 he:** וַיִּבְרָא אֱלֹהִים אֶת־הָאָדָם בְּצַלְמוֹ בְּצֶלֶם אֱלֹהִים בָּרָא אֹתוֹ זָכָר וּנְקֵבָה בָּרָא אֹתָם
> **tr:** va-yivra Elohim et-ha-adam be-tzalmo, be-tzelem Elohim bara oto, zakhar u-neqevah bara otam
> **en:** "God created the human in his image; in the image of God he created HIM; male and female he created THEM."
> **roles:** CREATE +et-obj ×3 · IMAGE/LIKENESS · MALE+FEMALE

```text
L1  bara ×3 in one verse — the densest creation clause of the week (elsewhere bara appears
    once per verse: 1:1, 1:21, 2:3)
L2  DELTA(spec, build): spec said be-tzalmeNU "in OUR image" → build says be-tzalmO "in HIS
    image" — the plural collapses to singular at execution
L3  NUMBER FLIP inside the verse: bara otO ("him", singular) → bara otAM ("them", plural),
    with zakhar u-neqevah / male-and-female between them → §Named Oral (du-partzufin)
L4  no naming formula: "adam" enters as a species term, not a conferred name
```

> **v28 he:** וַיְבָרֶךְ אֹתָם אֱלֹהִים וַיֹּאמֶר לָהֶם אֱלֹהִים פְּרוּ וּרְבוּ וּמִלְאוּ אֶת־הָאָרֶץ וְכִבְשֻׁהָ וּרְדוּ בִּדְגַת הַיָּם וּבְעוֹף הַשָּׁמַיִם וּבְכָל־חַיָּה הָרֹמֶשֶׂת עַל־הָאָרֶץ
> **tr:** va-yevarekh otam Elohim va-yomer LAHEM Elohim: peru u-revu u-mil'u et-ha-aretz ve-khivshuha, u-redu bi-dgat ha-yam u-ve-of ha-shamayim u-ve-khol-chayah ha-romeset al-ha-aretz
> **en:** "God blessed them and God said TO THEM: be fruitful, multiply, fill the earth and subdue it, and rule the fish of the sea, the flyers of the heavens, and every living thing that creeps on the earth."
> **roles:** BLESS · SPEAK · CMD!(be-fruitful · fill · subdue · rule-over)

```text
L1  bless + va-yomer LAHEM — first time the week's speech has a named human ADDRESSEE
L2  five imperatives (CMD!): peru, revu, mil'u, kivshuha, redu — v22's triple plus
    SUBDUE (new) and RULE (the v26 spec's jussive now handed over as a direct order)
```

> **v29–30 he:** הִנֵּה נָתַתִּי לָכֶם אֶת־כָּל־עֵשֶׂב זֹרֵעַ זֶרַע … לָכֶם יִהְיֶה לְאָכְלָה · וּלְכָל־חַיַּת הָאָרֶץ … אֶת־כָּל־יֶרֶק עֵשֶׂב לְאָכְלָה וַיְהִי־כֵן
> **tr:** hinneh natati lakhem et-kol-esev zorea zera … lakhem yihyeh le-okhlah; u-le-khol-chayat ha-aretz … et-kol-yereq esev le-okhlah — va-yehi khen
> **en:** "Behold, I have GIVEN you every seed-bearing herb … for you it shall be for food; and to every wild animal … every green herb for food — and it was so."
> **roles:** PRESENT(behold) · SET/PLACE (perfect) · FOOD-GRANT · RESULT(so)

```text
L1  GRANT( to: humans, what: seed-herb + fruit-trees, as: food )
    GRANT( to: all land/sky life, what: green herb, as: food )
L2  natati is PERFECT form — "I have (already) given": a performative transfer, effective
    at utterance (the deed is the saying, like the namings)
L3  RESULT ✓ closes the whole speech — the last va-yehi khen of the week
```

> **v31 he:** וַיַּרְא אֱלֹהִים אֶת־כָּל־אֲשֶׁר עָשָׂה וְהִנֵּה־טוֹב מְאֹד וַיְהִי־עֶרֶב וַיְהִי־בֹקֶר יוֹם הַשִּׁשִּׁי
> **tr:** va-yar Elohim et-kol-asher asah ve-hinneh-tov ME'OD; va-yehi erev va-yehi voqer yom HA-shishi
> **en:** "God saw ALL that he had made — and behold: VERY good. Evening, morning — THE sixth day."
> **roles:** SEE/ASSESS · EVAL(good) · **INTENSIFIER(very)** · TIME-STAMP · DAY-COUNT(sixth)

```text
L1  PASS( tov+, scope: KOL — everything made, not just day 6's output ) — the only GLOBAL test
L2  מְאֹד / me'od / "very" is its OWN brick and carries the verse's etnachta — the ta'amim
    put the week's main structural rest on the intensifier. Grammar underlines "very."
L3  COMMIT( day 6 ) — yom HA-shishi: the FIRST day label with the definite article
    (days 1–5: "one/second/…"; day 6: "THE sixth") — marked form at the week's last commit
```

*confidence: tested (all forms verified) · interpretations of the deltas = §Named Oral / hypothesis*

---

## Day 7 — Shabbat (2:1–3): no fiat, no test, no name — and no close

> **2:1 he:** וַיְכֻלּוּ הַשָּׁמַיִם וְהָאָרֶץ וְכָל־צְבָאָם
> **tr:** va-yekhullu ha-shamayim ve-ha-aretz ve-khol-tzeva'am
> **en:** "The heavens and the earth were COMPLETED, and all their host." · **roles:** COMPLETE (pual) · HOST

```text
L1  completed(shamayim ∧ aretz ∧ kol-tzeva'am) — PUAL (passive) wayyiqtol: completion happens
    to the world, agentless; צָבָא / tzava / "host" = the full inventory, sealed as a totality
```

> **2:2 he:** וַיְכַל אֱלֹהִים בַּיּוֹם הַשְּׁבִיעִי מְלַאכְתּוֹ אֲשֶׁר עָשָׂה וַיִּשְׁבֹּת בַּיּוֹם הַשְּׁבִיעִי מִכָּל־מְלַאכְתּוֹ אֲשֶׁר עָשָׂה
> **tr:** va-yekhal Elohim BA-yom ha-shevi'i melakhto asher asah, va-yishbot ba-yom ha-shevi'i mi-kol-melakhto asher asah
> **en:** "God COMPLETED on the seventh day his work which he had made, and he CEASED on the seventh day from all his work which he had made."
> **roles:** COMPLETE · DAY-COUNT(seventh) · WORK · CEASE/REST

```text
L1  ∃e₁₀ complete(e₁₀, melakhah) ∧ Time(e₁₀, day-7)     — completing ON day 7: what act
    remained? (paradox flagged; → §Named Oral, observation tier)
L2  ∃e₁₁ CEASE(e₁₁) — an event whose content is the STOPPING of events; the week's
    machine gets a halt instruction, stated twice ("on the seventh day" ×2)
```

> **2:3 he:** וַיְבָרֶךְ אֱלֹהִים אֶת־יוֹם הַשְּׁבִיעִי וַיְקַדֵּשׁ אֹתוֹ כִּי בוֹ שָׁבַת מִכָּל־מְלַאכְתּוֹ אֲשֶׁר־בָּרָא אֱלֹהִים לַעֲשׂוֹת
> **tr:** va-yevarekh Elohim et-yom ha-shevi'i va-yeqaddesh oto, ki vo shavat mi-kol-melakhto asher-bara Elohim LA'ASOT
> **en:** "God blessed the seventh day and SANCTIFIED it, because on it he ceased from all his work which God had created TO MAKE."
> **roles:** BLESS +et-obj · DAY-COUNT(seventh) · **SANCTIFY** · CEASE/REST · CREATE · PURPOSE(make)

```text
L1  ∃e₁₂ bless(e₁₂) ∧ Theme(e₁₂, yom-ha-shevi'i)        — first blessing whose Theme is a
    unit of TIME, not a creature (et marks the day as a full object)
L2  SANCTIFY(yom-7):  qadosh(day-7) := true             — a NEW operator: the week's first
    holiness predicate; a property write, not a name write
L3  ki vo shavat — the reason clause: the property is grounded in the ceasing
L4  bara … LA'ASOT — the week's final infinitive: "created TO MAKE/DO" — an open PURPOSE
    with no object: creation handed off as ongoing task (reading = hypothesis)
L5  ⚠⚠ NO COMMIT: day 7 has no "va-yehi erev va-yehi voqer." The closing formula that
    sealed days 1–6 never fires. In the ledger, the seventh day's transaction REMAINS OPEN.
```

*confidence: tested (the absences are in the text) · open-transaction reading = hypothesis (an old one — "the seventh day has no evening")*

---

## The pattern matrix (what formalizing buys you)

Every day-unit is the same transaction shape; the matrix shows exactly where the
instances differ — which is where the interesting theology/logic lives. Full week
(day 3 and day 6 each run two spec→build cycles, so they get two columns):

| Step | D1 (v2–5) | D2 (v6–8) | D3a (v9–10) | D3b (v11–13) | D4 (v14–19) | D5 (v20–23) | D6a (v24–25) | D6b (v26–31) | D7 (2:1–3) |
|------|-----------|-----------|-------------|--------------|-------------|-------------|--------------|--------------|------------|
| DECLARE + spec | ✓ v3 | ✓ v6 +INVARIANT | ✓ v9 passive | ✓ v11 **delegated to earth** | ✓ v14–15, 4 jobs | ✓ v20 (CMD? ×2) | ✓ v24 delegated | ✓ v26 **plural "US"** | **✗ no fiat** |
| Executor | — (direct) | God v7 | — (none named) | **EARTH v12** | God v16–18 | God v21 **bara** | **God v25 (swap!)** | God v27 **bara ×3** | — (pual: agentless) |
| RESULT ✓ (va-yehi khen) | ✓ v3 verbatim* | ✓ v7 | ✓ v9 | ✓ v11 | ✓ v15 | **✗ absent** | ✓ v24 | ✓ v30 (grant) | ✗ |
| Spec↔build delta | — | build splits waters | — | **etz peri → oseh-peri** | +hierarchy +stars | — | agent swap | **-nu → -o; oto → otam** | — |
| PASS(tov) | ✓ v4 | **✗ absent** | ✓ v10 | ✓ v12 | ✓ v18 | ✓ v21 | ✓ v25 | ✓ v31 **global +me'od** | **✗ absent** |
| BLESS | — | — | — | — | — | ✓ v22 **first** (to creatures) | — | ✓ v28 (+ spoken TO them) | ✓ 2:3 (**of TIME**) + **SANCTIFY** |
| name(x) := "N" | ✓✓ v5 | ✓ v8 collision | ✓✓ v10 collision | ✗ | **✗ luminaries unnamed** | ✗ | ✗ | ✗ ("adam" = species term) | ✗ (property, not name) |
| COMMIT (erev–boqer) | ✓ v5 cardinal "one" | ✓ v8 | (shared) | ✓ v13 | ✓ v19 | ✓ v23 | (shared) | ✓ v31 **HA-shishi (definite!)** | **✗✗ never fires — unit open** |

\* day 1's result phrase repeats the spec's own words instead of the generic *khen* /
"so" — the only day whose RESULT is verbatim. [OPEN: is verbatim-result a marked form?]

**What the full matrix shows that the 3-day version couldn't:** the naming formula runs
only in vv. 5–10 and never again; blessing enters exactly where naming exits (v22);
va-yehi-khen and bara trade places on day 5; both "delegated" specs (earth, days 3b/6a)
resolve differently — one executed by the delegate with a product delta, one taken back
by God; the two tests that are missing (day 2, day 7) bracket the two days whose objects
the tradition marks as unfinished or other-worldly; and the week's two definite-article
day labels (ha-shishi, ha-shevi'i) sit exactly at the boundary where the pattern breaks.
*confidence: matrix cells = tested; the "shows" sentences = hypothesis*

---

## Naming ledger — every defining verse, with the words being defined (added 2026-07-28)

Two mechanisms install names in 1:1–10: **installation by narration** (the word enters
existence in the story) and the explicit **naming formula** וַיִּקְרָא לְ־X Y / va-yiqra
le-X Y / "he called to-X, Y" — the לְ / le prefix marks the *receiver* of the name; the
bare word after it is the *label*.

**Gen 1:1 — first installs (narration + et, no formula):**
> he: בְּרֵאשִׁית בָּרָא אֱלֹהִים אֵת **הַשָּׁמַיִם** וְאֵת **הָאָרֶץ**
> tr: be-reshit bara Elohim et **ha-shamayim** ve-et **ha-aretz**
> en: "In the beginning God created **the heavens** and **the earth**."
> defines: שָׁמַיִם / shamayim / "heavens" · אֶרֶץ / eretz / "earth" — the two labels later re-used.

**Gen 1:5 — the naming formula's template (clean):**
> he: וַיִּקְרָא אֱלֹהִים **לָאוֹר** **יוֹם** וְ**לַחֹשֶׁךְ** קָרָא **לָיְלָה**
> tr: va-yiqra Elohim **la-or** **yom** ve-**la-choshekh** qara **layla**
> en: "God called **the-light** '**Day**', and **the-darkness** he called '**Night**'."
> defines: or := "yom" · choshekh := "layla" — fresh labels, no conflict.

**Gen 1:6 — collision-receiver 1 installed (fiat):**
> he: יְהִי **רָקִיעַ** בְּתוֹךְ הַמָּיִם · tr: yehi **raqia** be-tokh ha-mayim · en: "let there be a **firmament** amid the waters"
> defines: רָקִיעַ / raqia / "firmament" — the referent that will receive the recycled label. (BR 4:2 sits here.)

**Gen 1:8 — COLLISION 1:**
> he: וַיִּקְרָא אֱלֹהִים **לָרָקִיעַ** **שָׁמָיִם**
> tr: va-yiqra Elohim **la-raqia** **shamayim**
> en: "God called **the-firmament** '**Heavens**'."
> defines: raqia := "shamayim" — label already bound in 1:1. (BR 4:7 + Chagigah 12a sit here.)

**Gen 1:9 — collision-receiver 2 installed (revealed, not created):**
> he: וְתֵרָאֶה **הַיַּבָּשָׁה** · tr: ve-tera'e **ha-yabasha** · en: "let **the dry land** be seen"
> defines: יַבָּשָׁה / yabasha / "dry land". Note this verse's הַשָּׁמַיִם / ha-shamayim already reads ambiguously — v1's heavens or v8's firmament? The collision does work one verse after it happens.

**Gen 1:10 — COLLISION 2 + a clean third naming:**
> he: וַיִּקְרָא אֱלֹהִים **לַיַּבָּשָׁה** **אֶרֶץ** וּ**לְמִקְוֵה הַמַּיִם** קָרָא **יַמִּים**
> tr: va-yiqra Elohim **la-yabasha** **eretz** u-**le-miqveh ha-mayim** qara **yamim**
> en: "God called **the-dry-land** '**Earth**', and **the-gathering-of-waters** he called '**Seas**'."
> defines: yabasha := "eretz" — label bound in 1:1 (BR 5:8 sits here) · miqveh ha-mayim := "yamim" — clean, but odd plural (also BR 5:8).

**Gen 1:17 — the fusing construct (Chagigah's prooftext; usage, not naming):**
> he: וַיִּתֵּן אֹתָם אֱלֹהִים **בִּרְקִיעַ הַשָּׁמַיִם**
> tr: va-yiten otam Elohim **bi-rqia ha-shamayim**
> en: "God set them **in the firmament OF the heavens**."
> The Written text itself compounds the two colliding words into a possessive — raqia as part/member of shamayim. Anchor of Chagigah 12b's namespace reading.

| Verse | Referent (marked לְ) | Label | Mechanism | Status |
|-------|---------------------|-------|-----------|--------|
| 1:1 | — | shamayim "heavens" · eretz "earth" | narration + et | first bindings |
| 1:5 | or "light" | yom "Day" | formula | clean |
| 1:5 | choshekh "darkness" | layla "Night" | formula | clean |
| 1:8 | raqia "firmament" (inst. 1:6) | shamayim | formula | **collision w/ 1:1** |
| 1:10 | yabasha "dry land" (inst. 1:9) | eretz | formula | **collision w/ 1:1** |
| 1:10 | miqveh ha-mayim "water-gathering" | yamim "Seas" | formula | clean (odd plural) |
| 1:17 | — | — (construct fuses both) | usage | Chagigah 12b anchor |

**Pattern:** both collisions have the same shape — a label first installed *by narration*
in v1 is re-issued *by the formal naming formula* to an entity created later inside the
domain it originally covered. The clean namings (Day, Night, Seas) never touch a v1
label. *confidence: tested (the pattern is in the text)*

**Week addendum (2026-07-28):** after v10 the naming formula **never fires again** in the
entire week. The luminaries get ranked descriptors, not names (הַגָּדֹל / ha-gadol / "the
great one", הַקָּטֹן / ha-qaton / "the small one" — v16); the human enters as a species
term (אָדָם / adam, never conferred by qara); and day 7 receives a **property**
(קָדוֹשׁ / qadosh / "holy", via וַיְקַדֵּשׁ / va-yeqaddesh — 2:3), not a name. All seven
formula-namings live inside vv. 5–10, and blessing (v22, v28, 2:3) begins exactly where
naming ends. *confidence: tested (absence verified across all 34 verses)*

---

## Named Oral — how the tradition resolves the two collisions (added 2026-07-28)

Named locations only; quotes verified against local `Data/` (bavli_chagigah_he.json,
bereshit_rabbah_he.json) unless marked observation. Never merged into the Written layer.

### Collision 1 — shamayim (1:1 → 1:8): three resolutions

**(a) Two-phase creation — v8 is commissioning, not a new install.** Bereshit Rabbah 4:2 (on 1:6) · *verified*:
> רב אמר לחים היו מעשיהם ביום הראשון ובשני קרשו. יהי רקיע — יחזק הרקיע
> Rav amar: lachim hayu ma'aseihem ba-yom ha-rishon u-va-sheni karshu. Yehi raqia — yechezak ha-raqia
> "Rav said: their works were **fluid** on day one, and on the second they **solidified**. 'Let there be a raqia' — let the raqia be **strengthened**."

One entity, two states: v1 creates the heavens fluid; day 2 hardens them; v8 names at
completion. Registry reading: v1 = declaration, v8 = binding finalized at commissioning.
(Rashi on 1:6–8 adopts this — *observation*, not in local Data.)

**(b) Namespace — shamayim is a family name; raqia is one member.** Bavli Chagigah 12b · *verified*:
> ריש לקיש אמר שבעה: וילון רקיע שחקים זבול מעון מכון ערבות … רקיע שבו חמה ולבנה כוכבים ומזלות קבועין שנאמר ויתן אותם אלהים ברקיע השמים
> Resh Lakish amar shiv'ah: Vilon, Raqia, Shechakim, Zevul, Ma'on, Machon, Aravot … Raqia she-bo chamah u-levanah kokhavim u-mazalot kevu'in
> "Resh Lakish said seven [heavens]… **Raqia: in which sun, moon, stars and constellations are fixed**, as it says (Gen 1:17)…"

Shamayim = a seven-layer namespace; "Raqia" is layer two — proof-texted from Gen 1:17
itself. BR 4:2 has a version too: the middle drop congealed into הַשָּׁמַיִם הַתַּחְתּוֹנִים /
ha-shamayim ha-tachtonim / "the lower heavens" vs שְׁמֵי שָׁמַיִם הָעֶלְיוֹנִים / shmei
shamayim ha-elyonim / "the upper heaven-of-heavens."

**(c) The name is a job description — reuse is precision.** Bavli Chagigah 12a · *verified*:
> מאי שמים? א"ר יוסי בר חנינא ששם מים. במתניתא תנא אש ומים — מלמד שהביאן הקב"ה וטרפן זה בזה ועשה מהן רקיע
> Mai shamayim? … she-**sham mayim**. Be-matnita tana: **esh u-mayim** — melamed she-hevi'an HKBH u-terafan zeh ba-zeh ve-asah mehen **raqia**
> "What is shamayim? R. Yosi bar Chanina: '**there is water there**.' A beraita: '**fire and water** — He whipped them into each other and made from them the **raqia**.'"

The Bavli's etymology of *shamayim* terminates in the raqia — the two referents fused in
one sentence. If the name means "water-place"/"fire+water," applying it to the
water-handling object in v8 is functionally exact labeling. BR 4:7 (on 1:8 itself) says
the same: נטל הקב"ה אש ומים ופתכן זה בזה ומהן נעשו שמים / natal HKBH esh u-mayim
u-fetakhan zeh ba-zeh u-mehen na'asu shamayim / "He took fire and water, kneaded them
into each other, and from them shamayim were made." · *verified*

### Collision 2 — eretz (1:1 → 1:10): an earned rename

Bereshit Rabbah 5:8 (on 1:10) · *verified*:
> ויקרא אלהים ליבשה ארץ — למה נקרא שמה ארץ? שרצתה לעשות רצון קונה
> lamah niqra shemah **eretz**? she-**ratzta** la'asot **retzon** konah
> "Why is its name *eretz*? Because it **willed** (*ratzta*) to do the **will** (*ratzon*) of its Owner."

The v10 naming is *motivated*: the dry land earns the title by instant obedience to the
gathering command (wordplay eretz ↔ ratzon). v1's eretz = raw label for the whole lower
domain; v10 confers it on the dry part as a merit-title — whole→part narrowing, second
write deliberate. (Ramban on 1:10 makes whole→part explicit — *observation*.) Same BR
piece resolves the yamim plural: one sea, but "the taste of a fish from Akko differs
from one from Sidon" — each name a functional description.

### Week additions (2026-07-28) — named Oral on the full-week anomalies

**Day 2's missing test.** Bereshit Rabbah 4:6 (on 1:7) · *verified*:
> למה אין כתיב בשני כי טוב? רבי יוחנן תני לה בשם רבי יוסי בן רבי חלפתא: שבו נבראת גיהנם
> lamah ein ketiv ba-sheni ki tov? … she-bo nivre'at Gehinnom
> "Why is 'that it was good' not written on the second day? R. Yochanan taught in the name of R. Yosi b. R. Chalafta: because on it Gehinnom was created."
The same piece continues (division began on day 2 / the waters' work was unfinished until
day 3 — hence day 3's double PASS). The empty matrix cell has a dedicated Oral discussion.

**Day 3b's product delta (etz peri → oseh peri).** Bereshit Rabbah 5:9 (on 1:11) · *verified*:
> תני בשם רבי נתן: שלשה נכנסו לדין וארבעה יצאו מחיבין … ונתקללה הארץ עמהן, שנאמר: ארורה האדמה בעבורך
> tani be-shem Rabbi Natan: sheloshah nikhnesu la-din ve-arba'ah yatze'u mechuyavin … ve-nitqallelah ha-aretz immahen
> "It was taught in R. Natan's name: three entered for judgment and four came out condemned … and the earth was cursed with them, as it says: 'cursed is the ground because of you.'"
The midrash reads the earth's deviation from the spec (tree-as-fruit commanded; tree-bearing-fruit
delivered) as real non-compliance, later judged. The DELTA row of the matrix is exactly what
this passage is about.

**Day 5's taninim.** Bavli Bava Batra 74b · *verified*:
> ויברא אלהים את התנינים הגדולים … ר' יוחנן אמר זה לויתן נחש בריח ולויתן נחש עקלתון
> … Rabbi Yochanan amar: zeh livyatan nachash bariach ve-livyatan nachash aqallaton
> "'And God created the great sea-creatures' … R. Yochanan said: this is Leviathan the fleeing serpent and Leviathan the twisting serpent."
The one creature class singled out by name inside a bara-verse gets its own identification tradition.

**Day 6's plural spec (na'aseh / "let US make").** Bereshit Rabbah 8:3 · *verified*:
> נעשה אדם — במי נמלך? רבי יהושע בשם רבי לוי אמר: במלאכת השמים והארץ נמלך … רבי שמואל בר נחמן אמר: במעשה כל יום ויום נמלך
> na'aseh adam — be-mi nimlakh? … bi-mlekhet ha-shamayim ve-ha-aretz nimlakh … be-ma'aseh kol yom va-yom nimlakh
> "'Let us make a human' — with whom did He consult? R. Yehoshua in R. Levi's name: with the works of heaven and earth… R. Shmuel bar Nachman: with the works of each and every day."
And Bavli Sanhedrin 38b · *verified*:
> בשעה שבקש הקב"ה לבראות את האדם ברא כת אחת של מלאכי השרת, אמר להם: רצונכם נעשה אדם בצלמנו?
> … bara kat achat shel mal'akhei ha-sharet, amar lahem: retzonkhem na'aseh adam be-tzalmenu?
> "When the Holy One sought to create the human, He created one company of ministering angels and said to them: is it your will that we make a human in our image?"
Both traditions read the plural as **consultation** — the CMD-US operator taken literally as a
multi-party spec review before the build.

**Day 6's number flip (oto → otam).** Bavli Eruvin 18a · *verified*:
> אמר רבי ירמיה בן אלעזר: דיו פרצוף פנים היה לו לאדם הראשון, שנאמר: אחור וקדם צרתני
> du partzuf panim hayah lo le-adam ha-rishon
> "R. Yirmiyah b. Elazar said: the first human had two faces (du-partzufin), as it says: 'behind and before you formed me.'"
(Parallel: Bereshit Rabbah 8:1.) The tradition resolves the singular/plural oscillation of
v27 by making the referent literally both at once — one creature, dual-faced, later divided.

**Day 6's tov ME'OD.** Two verified readings of the intensifier brick:
> Bereshit Rabbah 9:5: בתורתו של רבי מאיר מצאו כתוב: והנה טוב מאד — והנה טוב מות
> be-torato shel Rabbi Meir matz'u katuv: ve-hinneh tov me'od — ve-hinneh tov MAVET
> "In R. Meir's Torah scroll they found written: 'behold, very good' — 'behold, DEATH is good.'"
> Bereshit Rabbah 3:7 (R. Abbahu): מלמד שהיה בורא עולמות ומחריבן … אמר דין הנין לי
> melammed she-hayah bore olamot u-machrivan … amar: dein hanyan li
> "…He created worlds and destroyed them, until He created these; He said: these please Me" —
> with וירא אלהים את כל אשר עשה והנה טוב מאד (v31) as the prooftext.
The global PASS with its own intensifier brick is exactly where the tradition parks both its
darkest reading (me'od ≈ mavet) and its widest one (this world passed where others failed).

**Day 7's completion paradox and blessing.** Bereshit Rabbah 11:2 (on 2:3) · *verified*:
> רבי ישמעאל אומר: ברכו במן וקדשו במן
> Rabbi Yishmael omer: berkho ba-man ve-qiddesho ba-man
> "R. Yishmael says: He blessed it with manna and sanctified it with manna" (double portion
> before, none on it — the property write cashed out in later provision).
And Bereshit Rabbah 11:8 · *verified*:
> שאין לו בן זוג … שבתא לית לה בן זוג
> she-ein lo ben zug … shabbeta let lah ben zug
> "…it has no partner: Sunday has Monday, Tuesday has Wednesday… Shabbat has no mate."
The day outside the pairing structure is the day whose transaction our ledger shows as
never closed. On *what was created on day 7* (the va-yekhal paradox), the classic answer —
the world lacked מנוחה / menuchah / "rest," and Shabbat brought it (Bereshit Rabbah 10:9,
cited by Rashi on 2:2) — did not verify in the local Data dump · *observation*.

### Day 7's missing close — three named readings (added 2026-07-28, same day)

The fact is tested: the erev–boqer COMMIT formula never fires for day 7. *Why* is
interpretation; the tradition offers three families of answers, all verified from local
Data, and they are strikingly compatible:

**(a) Still running — the day hasn't ended.** Bavli Rosh Hashanah 31a (= Mishnah Tamid 7:4) · *verified*:
> בשביעי היו אומרים מזמור שיר ליום השבת — ליום שכולו שבת
> ba-shevi'i hayu omrim "mizmor shir le-yom ha-shabbat" — le-yom she-kullo shabbat
> "On the seventh day [the Levites] would sing 'A psalm, a song for the Shabbat day' — for the day that is ENTIRELY Shabbat."
Day 7 points past itself at an unended epoch; the seventh day has no evening because its
frame is still open.

**(b) Handoff — closing is delegated.** Bavli Shabbat 119b · *verified*:
> כל המתפלל בערב שבת ואומר ויכולו — מעלה עליו הכתוב כאילו נעשה שותף להקדוש ברוך הוא במעשה בראשית, שנאמר ויכולו — אל תקרי ויכולו אלא ויכלו
> kol ha-mitpallel be-erev shabbat ve-omer va-yekhullu — … ke-ilu na'asah SHUTAF le-HKBH be-ma'aseh bereshit … al tiqrei va-yekhullu ella VA-YEKHALLU
> "Whoever prays on Shabbat eve and says vayekhullu — Scripture accounts it as if he became a PARTNER of the Holy One in the work of creation… read not 'they were completed' but 'they completed.'"
The wordplay flips 2:1's **pual passive** (our agentless COMPLETE) into an active plural —
God *and the reciter* complete it. Pairs with the text's own tail: אֲשֶׁר בָּרָא אֱלֹהִים
לַעֲשׂוֹת / asher bara Elohim LA'ASOT / "created TO MAKE" — the open infinitive as
deliberate handoff.

**(c) Conditional commit — the close awaits a future ACK.** Bavli Shabbat 88a · *verified*:
> ויהי ערב ויהי בקר יום הששי — ה' יתירה למה לי? מלמד שהתנה הקדוש ברוך הוא עם מעשה בראשית ואמר להם: אם ישראל מקבלים התורה — אתם מתקיימין, ואם לאו…
> yom HA-shishi — heh yeterah lamah li? melammed she-hitnah HKBH im ma'aseh bereshit: im Yisrael meqabbelim ha-Torah — atem mitqayymin, ve-im lav [ani machzir etkhem le-tohu va-vohu]
> "'THE sixth day' — why the extra letter heh? It teaches the Holy One made a CONDITION with the works of creation: if Israel accepts the Torah, you endure; if not, [I return you to tohu va-vohu]."
Reish Lakish hangs this on **exactly the definite article our matrix flagged** (yom
HA-shishi, the week's marked final commit): creation's whole transaction was provisional,
its final acknowledgment scheduled for Sinai, with a documented rollback target (tohu
va-vohu — the v2 precondition state).

**Developer-analogy mapping (hypothesis; lenses, not doctrine — Standing Decisions §8):**
the three readings correspond to the three standard reasons a transaction shows as open
in a distributed system: (a) the process is still executing (days 1–6 = setup scripts
that exit and commit; day 7 = the long-running service we are inside); (b) ownership was
transferred (shavat = vendor code-freeze; la'asot = the API left open; saying vayekhullu
= contributing — Shabbat 119b's partner); (c) two-phase commit awaiting its ACK (Sinai),
with rollback state specified. And וַיְקַדֵּשׁ / va-yeqaddesh installs the recurrence:
sanctifying day 7 registers a weekly re-entry into the unclosed day — a standing
change-freeze window (no melakhah) every seventh day. *confidence: quotes verified ·
mappings = hypothesis*

### Meta-point

The tradition's four strategies map onto known binding-resolution moves:
declaration-then-finalization (BR 4:2) · namespacing (Chagigah 12b) · functional
overloading — the name *is* a spec (Chagigah 12a, BR 4:7) · annotated rebinding — the
name is earned (BR 5:8). And the dry-run flagged exactly two registry anomalies in ten
verses; the Oral corpus has dedicated discussion sitting on precisely those two verses —
external validation that the trace anomalies are textual features, not method artifacts.
*confidence: quotes verified · mappings = hypothesis*

---

## Status and honest limits

| Claim | Label |
|-------|-------|
| Verb-form → logic-operator mapping (jussive→LET, participle→INVARIANT, wayyiqtol→event, perfect→state, niphal/pual→passive constraint, cohortative→CMD-US, weqatal→THEN, ל+inf→PURPOSE) | **tested** on all 34 verses of 1:1–2:3 |
| Day-unit = Hoare-style transaction (spec → execute → verify → name/bless → commit) | **tested as pattern** across 9 cycles, hypothesis as *intent* |
| Matrix deviations (missing tests, missing RESULT, agent swaps, spec deltas, open day-7) | **tested** (each absence/delta verified in the letters) |
| tov = acceptance oracle; registry naming; collisions/deltas meaningful; day-7 "open transaction" | **hypothesis** — each with named Oral discussion where found |
| Any of this as binding religious law | **no** — experiment only |

Done 2026-07-28: full-week extension (all 34 verses); pattern matrix across all 9
spec→build cycles; named Oral fetched and verified for both registry collisions, day-2
missing test, day-3b product delta, na'aseh consultation, oto/otam flip, tov me'od,
taninim, and the Shabbat blessing (menuchah = observation only — not in local dump).

Next steps if pursued (owner call): propose TIR rules for the eight form→operator
mappings; write day 1 (v2–5) as a `binary_trees`-backed unit with these logic lines in
the derivation log; run the same treatment on Gen 2:4ff (the second creation account) and
diff the two machines; day-7 open-commit reading against further named Oral; hand-polish
the auto transliterations in the HTML report.

**Related:** `GEN_1_1_20_flat_ledger_morph_2026-07-27.html` (roles) ·
`MOCKUP_flat_ledger_oshb_morph_2026-07-27.md` (format spec) ·
`logic/TREE_INTERPRETATION_RULES.md` (TIR) · `logic/SYSTEM.md` (unit pipeline)
