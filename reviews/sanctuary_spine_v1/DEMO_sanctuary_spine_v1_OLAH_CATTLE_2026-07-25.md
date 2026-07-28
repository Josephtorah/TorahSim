# Sanctuary spine V1 — Step 4: Cattle olah procedure (Lev 1:1–9)

**Date:** 2026-07-25  
**Kind:** demo procedure logic from Hebrew + trees — experimental, **not** binding religious law  
**Status:** **Step 4 done**  
**Folder:** `reviews/sanctuary_spine_v1/`  
**Charter:** `DEMO_sanctuary_spine_v1_CHARTER_2026-07-25.md`  
**Writes / Uses:** `…_WRITES_…` · `…_USES_…`  
**Next:** Step 5 — cloud stay/go FSM  

**Scope:** Lev **1:1–9** only (cattle path). Flock/bird deferred.  
**Source:** `Data/Lev.xml` · `taamim_tree_parse.py` v1 (all verses `unique`).  
**English:** `[EN-AID]` gloss; derivation from Hebrew structure.

On substantive update: rename to today’s date and fix links.

---

## 0. What this step is

Turn Lev 1:1–9 into an **ordered procedure** a full-stack developer can read as:

```text
boot speech from installed Tent
  → open offering type menu
  → IF cattle olah with guards
  → bring to installed entrance
  → bringer acts (lean, slaughter, flay, cut, wash)
  → priest acts (blood, fire, arrange, smoke)
  → close formula
```

Each step cites **verse + top tree split (and key leaves)** + **free names** from Steps 2–3.

**Not:** full Sifra densification · flock/bird · executable VM.

---

## 1. Agents and environment (resolved symbols)

| Role | Hebrew | Translit | English | Resolved from |
|------|--------|----------|---------|---------------|
| Speech source | מֵאֹהֶל מוֹעֵד | *me-ohel mo’ed* | from Tent of Meeting | `SYM_ohel_moed` WRITE Exod 27:21 / 40:34 |
| Bring-to place | פֶּתַח אֹהֶל מוֹעֵד | *petach ohel mo’ed* | entrance of Tent | `SYM_petach_ohel` WRITE Exod 29:4+ |
| Operators | בְּנֵי אַהֲרֹן הַכֹּהֲנִים | *benei Aharon ha-kohanim* | sons of Aaron the priests | `SYM_benei_aharon` / `SYM_kohen` Exod 28:1 |
| Altar | הַמִּזְבֵּחַ | *ha-mizbeach* | the altar | `SYM_mizbeach` Exod 27:1 / 40:6 |
| Bringer | אָדָם / implied subject | *adam* / he | person who offers | Lev 1:2 open |
| Type | עֹלָה מִן הַבָּקָר | *olah min ha-bakar* | burnt offering from cattle | local + type family |

**Program shape:** environment is **imported**; procedure runs against it.

---

## 2. Pipeline overview

```text
[1:1]  CALL / SPEECH from SYM_ohel_moed
[1:2]  OPEN menu: person → korban to YHWH; from behemah → bakar | tzon
[1:3]  IF olah from bakar + male + tamim → BRING to SYM_petach_ohel (before YHWH)
[1:4]  BRINGER: lean hand on head of olah → acceptance / kipper aim
[1:5]  BRINGER: slaughter before YHWH
       PRIESTS: present blood; dash blood on SYM_mizbeach around; at petach
[1:6]  BRINGER: flay olah; cut into pieces
[1:7]  PRIESTS: put fire on altar; arrange wood on fire
[1:8]  PRIESTS: arrange pieces + head + suet on wood/fire on altar
[1:9]  BRINGER: wash innards/legs
       PRIEST: turn all to smoke on altar
       CLOSE: olah / isheh / re'ach nichoach to YHWH
```

---

## 3. Ordered steps (with tree grounding)

### STEP_0 — Boot speech (Lev 1:1)

| | |
|--|--|
| **Hebrew linear** | ויקרא אל משה וידבר יהוה אליו מאהל מועד לאמר |
| **Translit** | *va-yiqra el Mosheh va-yedabber YHWH elav me-ohel mo’ed lemor* |
| **EN-AID** | He called to Moses; YHWH spoke to him **from the Tent of Meeting**, saying |
| **Top tree** | **L:** call to Moses · **R:** YHWH speaks to him **from ohel mo’ed**, saying |
| **Key leaves** | `RRL`–`RRLR` מאהל מועד / *me-ohel mo’ed* (mercha→tifcha) |
| **Logic** | `SPEECH_SOURCE = SYM_ohel_moed` (must already be live — Exod 40) |
| **Op** | `OPEN_ORACLE` / law speech begins |
| **Resolve** | USE → WRITE Exod 27:21 · 40:34–35 · **PASS** (Step 3) |

---

### STEP_1 — Open type menu (Lev 1:2)

| | |
|--|--|
| **Hebrew** | … אדם כי יקריב מכם קרבן ליהוה מן הבהמה מן הבקר ומן הצאן … |
| **Translit** | *adam ki yaqriv mikkem korban la-YHWH min ha-behemah min ha-bakar u-min ha-tzon* |
| **EN-AID** | When a person from you brings an offering to YHWH: from animals — from cattle or from flock you shall bring your offering |
| **Top tree** | **L:** speak to Israel; person brings **korban** to YHWH · **R:** **from** behemah / bakar / tzon — bring your korban |
| **Key structure** | L ends etnachta on ליהוה; R = type list (מן glue → class nouns) |
| **Logic** | `DECLARE_LOCAL korban`; `TYPES = {behemah → {bakar, tzon}}` (bird later 1:14, out of V1) |
| **Op** | `OPEN_MENU` |
| **Note** | `קרבן` first major legal surface here = **LOCAL declare** (Phase B / charter) |

**Pseudo:**

```text
on speech_from(SYM_ohel_moed):
  tell Israel:
    when person.brings(korban → YHWH):
      source ∈ {behemah.bakar, behemah.tzon, …}
```

---

### STEP_2 — Case header: cattle olah (Lev 1:3 L)

| | |
|--|--|
| **Hebrew (L)** | אם עלה קרבנו מן הבקר זכר תמים יקריבנו |
| **Translit** | *im olah korbano min ha-bakar zakhar tamim yaqrivenu* |
| **EN-AID** | If his offering is a burnt offering from cattle: male, unblemished, he shall bring it near |
| **Top tree** | **L:** IF olah + from cattle + male + tamim + bring · **R:** (place — next step) |
| **Guards on L** | `עלה` type · `מן הבקר` source · `זכר` male · `תמים` unblemished |
| **Logic** | `IF offering.type == olah AND animal.class == bakar AND male AND tamim` |
| **Op** | `CASE_OPEN` / condition bundle (tree keeps guards on same half as IF) |

**Marker:** **אם** / *im* / “if” opens casuistic case (logic glue, not a free name).

---

### STEP_3 — Bring to installed entrance (Lev 1:3 R)

| | |
|--|--|
| **Hebrew (R)** | אל פתח אהל מועד יקריב אתו לרצנו לפני יהוה |
| **Translit** | *el petach ohel mo’ed yaqriv oto li-rtzono lifnei YHWH* |
| **EN-AID** | To the entrance of the Tent of Meeting he shall bring it, for its acceptance, before YHWH |
| **Key multi-leaf** | `RLL*` פתח אהל מועד (paths RLLLR…RLLRR) |
| **Logic** | `bring(animal, to=SYM_petach_ohel)`; aim acceptance before YHWH |
| **Op** | `BRING_TO_PLACE` |
| **Resolve** | `SYM_petach_ohel` → Exod 29:4 / 29:42 / 40:6 · **PASS** |
| **Glue** | **אל** / *el* / “to” points at place variable |

**Tree insight:** conditions **LEFT**; **place** **RIGHT** — IF/THEN geography without English invention.

---

### STEP_4 — Lean hand (Lev 1:4)

| | |
|--|--|
| **Hebrew** | וסמך ידו על ראש העלה ונרצה לו לכפר עליו |
| **Translit** | *ve-samakh yado al rosh ha-olah ve-nirtsah lo le-khapper alav* |
| **EN-AID** | He shall lean his hand on the head of the burnt offering, and it shall be accepted for him to atone for him |
| **Top tree** | **L:** lean hand on head of the olah · **R:** accepted for him to atone |
| **Key** | L ends etnachta on **העלה**; act **וסמך** on L |
| **Agent** | **Bringer** (not priest wording here) |
| **Logic** | `bringer.lean(hand, on=head_of(olah))` → acceptance/kipper aim |
| **Op** | `IDENTIFY` / hand-lean |
| **Prior pattern** | Exod 29:10 lean in investiture (Step 2 related procedure seed) |

---

### STEP_5 — Slaughter then priest blood (Lev 1:5)

| | |
|--|--|
| **Hebrew** | ושחט את בן הבקר לפני יהוה והקריבו בני אהרן הכהנים את הדם וזרקו את הדם על המזבח סביב אשר פתח אהל מועד |
| **Translit** | *ve-shahat et ben ha-bakar lifnei YHWH ve-hiqrivu benei Aharon ha-kohanim et ha-dam ve-zarku et ha-dam al ha-mizbeach saviv asher petach ohel mo’ed* |
| **EN-AID** | He shall slaughter the cattle-young before YHWH; the sons of Aaron the priests shall present the blood and dash the blood on the altar around, which is at the entrance of the Tent of Meeting |

**Top tree (critical split):**

| Arm | Content | Agent |
|-----|---------|-------|
| **LEFT** | slaughter *ben ha-bakar* before YHWH | Bringer |
| **RIGHT** | priests + blood + dash on altar + at petach | Priests |

**Key leaves:**

| Path | Hebrew | Role |
|------|--------|------|
| `LLL` | ושחט | slaughter act |
| `LLRC*` | בן הבקר | animal instance |
| `LR` | לפני יהוה | before YHWH |
| `RLLRC*` | בני אהרן הכהנים | operators |
| `RLRR` / blood spans | הדם | substance |
| `RRLLC*` | וזרקו … על המזבח | dash on altar |
| `RRR*` | פתח אהל מועד | place of altar layout |

**Logic:**

```text
bringer.slaughter(animal, where=before_YHWH)
priests.receive_blood(dam)
priests.dash(dam, on=SYM_mizbeach, around=true, at=SYM_petach_ohel)
```

**Resolve:** priests + altar + petach → Exod install · **PASS** (Step 3).  
**Op:** `SPLIT_AGENTS` (tree enforces bringer vs priest halves).

---

### STEP_6 — Flay and cut (Lev 1:6)

| | |
|--|--|
| **Hebrew** | והפשיט את העלה ונתח אתה לנתחיה |
| **Translit** | *ve-hifshit et ha-olah ve-nittah otah li-ntakheha* |
| **EN-AID** | He shall flay the burnt offering and cut it into its pieces |
| **Top tree** | **L:** flay the olah · **R:** cut it into pieces |
| **Agent** | Bringer (no priest subject) |
| **Op** | `PREPARE_BODY` (two sequential acts, L then R) |

---

### STEP_7 — Fire and wood on altar (Lev 1:7)

| | |
|--|--|
| **Hebrew** | ונתנו בני אהרן הכהן אש על המזבח וערכו עצים על האש |
| **Translit** | *ve-natnu benei Aharon ha-kohen esh al ha-mizbeach ve-arkhu etsim al ha-esh* |
| **EN-AID** | Sons of Aaron the priest shall put fire on the altar and arrange wood on the fire |
| **Top tree** | **L:** priests put fire on altar · **R:** arrange wood on the fire |
| **Agent** | **Priests** |
| **Key** | L ends etnachta on **המזבח**; multi-leaf בני אהרן הכהן |
| **Logic** | `priests.put(fire, on=SYM_mizbeach)`; `priests.arrange(wood, on=fire)` |
| **Op** | `PREPARE_FIRE` |
| **Resolve** | altar + priests → install · **PASS** |

---

### STEP_8 — Arrange pieces on fire (Lev 1:8)

| | |
|--|--|
| **Hebrew** | וערכו בני אהרן הכהנים את הנתחים את הראש ואת הפדר על העצים אשר על האש אשר על המזבח |
| **Translit** | *ve-arkhu benei Aharon ha-kohanim et ha-netahim et ha-rosh ve-et ha-pader al ha-etsim asher al ha-esh asher al ha-mizbeach* |
| **EN-AID** | Sons of Aaron the priests shall arrange the pieces, the head, and the suet on the wood that is on the fire that is on the altar |
| **Top tree** | **L:** priests + pieces/head/suet · **R:** on wood on fire on altar (nested *asher al*) |
| **Agent** | Priests |
| **Logic** | `priests.arrange([pieces, head, suet], on=wood_on_fire_on(SYM_mizbeach))` |
| **Op** | `ARRANGE_PARTS` |
| **Glue** | **את** marks definite objects (pieces, head, suet) — payloads, not install symbols |

---

### STEP_9 — Wash + smoke + close formula (Lev 1:9)

| | |
|--|--|
| **Hebrew** | וקרבו וכרעיו ירחץ במים והקטיר הכהן את הכל המזבחה עלה אשה ריח ניחוח ליהוה |
| **Translit** | *ve-kirbo u-khra‘av yirhats ba-mayim ve-hiqtir ha-kohen et ha-kol ha-mizbechah olah isheh re’ach nihoah la-YHWH* |
| **EN-AID** | He shall wash its innards and legs in water; the priest shall turn it all to smoke on the altar — a burnt offering, a fire-offering, soothing aroma to YHWH |

**Top tree:**

| Arm | Content | Agent |
|-----|---------|-------|
| **LEFT** | wash innards/legs in water | Bringer |
| **RIGHT** | priest smokes all on altar + formula | Priest |

**Key R leaves:** הכהן · המזבחה · עלה · אשה · ריח ניחוח · ליהוה  

**Logic:**

```text
bringer.wash(innards_and_legs, in=water)
priest.burn_smoke(all, onto=SYM_mizbeach)
assert type_tags ⊆ {olah, isheh, re'ach_nichoach → YHWH}
```

**Op:** `WASH` + `SMOKE` + `CLOSE_FORMULA`  
**Disambig:** עלה / אשה cleared as offering terms (Onkelos/OSHB prior pass).

---

## 4. Agent swimlane (who does what)

| Step | Bringer | Priests | Environment free names |
|------|---------|---------|------------------------|
| 1:1 | — | — | ohel mo’ed (speech) |
| 1:2 | may bring | — | — |
| 1:3 | bring to entrance | — | petach ohel mo’ed |
| 1:4 | lean | — | olah |
| 1:5 | slaughter | blood present + dash | mizbeach, petach, kohanim |
| 1:6 | flay, cut | — | olah |
| 1:7 | — | fire + wood | mizbeach |
| 1:8 | — | arrange parts | mizbeach |
| 1:9 | wash | smoke all | mizbeach, kohen |

**Tree repeatedly separates bringer acts from priest acts** (esp. 1:5, 1:9) — finite structure, not our invention.

---

## 5. State sketch (procedure FSM)

```text
S0  idle / after speech open
S1  menu open (korban types known)
S2  case cattle-olah selected + guards ok
S3  animal at petach (brought)
S4  identified (hand leaned)
S5  slaughtered; blood available
S6  blood applied on altar
S7  body prepared (flayed, cut)
S8  fire ready on altar
S9  parts arranged on fire
S10 washed
S11 smoked / closed (formula)
```

Transitions follow verse order 1:2→1:9; guards fail → case not entered (1:3 IF).

**Confidence:** state ids = **hypothesis** packaging; verse order and agent splits = **tested** from Hebrew/trees.

---

## 6. Free-name dependency (this procedure)

```text
Requires BEFORE run:
  SYM_ohel_moed     live (Exod 40)
  SYM_petach_ohel   defined (Exod 29/40)
  SYM_mizbeach      placed (Exod 27/40)
  SYM_benei_aharon  appointed (Exod 28)

Declares/uses locally:
  korban menu, olah, bakar, zakhar, tamim, dam, acts…
```

If install missing, Lev 1 free names have **nowhere to resolve** — that is the spine demo claim.

---

## 7. Limits

| Done | Not done |
|------|----------|
| Ordered steps 1:1–9 with tree L/R and key leaves | Flock/bird paths |
| Agent split bringer/priest | Full TIR every leaf role |
| Link to Step 2–3 symbols | Sifra dual-track densification |
| FSM sketch | Binding law / executable code |

---

## 8. Step status

| Step | Status |
|------|--------|
| 1–3 | done |
| **4 Cattle olah** | **done** (this file) |
| 5 Cloud FSM | pending |
| 6 Hub | pending |

---

## Changelog

- 2026-07-25: Step 4 cattle olah procedure Lev 1:1–9 from trees + free-name resolves.
