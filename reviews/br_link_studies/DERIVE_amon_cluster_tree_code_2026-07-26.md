# Derive code: first BR cluster (amon → Gen 1:1)

**Date:** 2026-07-26  
**Kind:** tree-derived logic · show work · **not** binding law  
**Cluster:** BR 1:1 — Prov 8:30 · Num 11:12 · Lam 4:5 · Esth 2:7 · Nah 3:8 · Prov 8:22 · **Gen 1:1**  
**Unit file:** `logic/units/br_1_1_amon_cluster_tree_logic_2026-07-26.yaml`  
**Trees JSON:** `_amon_cluster_trees.json`  
**Method:** same as Gen boot — **top etnachta split → one STEP per verse**  
**Note:** Prov/Lam used `force_prose` (v1 poetry ranks not ready)

---

## 0. What we did

You asked: we already have Gen tree-code; now derive the **same kind of code** for the verses BR links to Gen, and see if Gen is **calling a function**.

So for each verse:

1. Parse the **cantillation tree**  
2. Take the **main split** (etnachta)  
3. Read LEFT / RIGHT as the verse’s two big jobs  
4. Name an **op** (hypothesis)  
5. Ask: does Gen 1:1’s tree **point at** any of those ops?

---

## 1. Gen 1:1 — the candidate “caller” (already derived)

**Full:** בְּרֵאשִׁית בָּרָא אֱלֹהִים אֵת הַשָּׁמַיִם וְאֵת הָאָרֶץ  
*be-reishit bara Elohim et ha-shamayim ve-et ha-aretz*  
“In/as **reishit** God **created** — **et** the heavens and **et** the earth.”

| Arm | Hebrew (plain) | Job in the “code” |
|-----|----------------|-------------------|
| **LEFT** | reishit + created + God | **WHEN / frame:** create under `reishit` |
| **RIGHT** | et heavens + et earth | **WHAT:** include two domains |

```text
OP_Gen_1_1 ≈ CREATE_AT_REISHIT_WITH_ET_DOMAINS
  frame:  reishit
  agent:  Elohim
  objects: heavens ∪ earth   (את…ואת)
```

Nothing in this tree says the word *amon*.  
So Gen is **not** literally calling the amon lattice by shared surface word.

---

## 2. Remote verses — tree code (one card each)

### Prov 8:30 — open (“I was beside Him as *amon*”)

| Arm | Plain job |
|-----|-----------|
| **LEFT** | I **was beside Him as אָמוֹן / amon**; I was delights day by day |
| **RIGHT** | playing before Him at all times |

```text
OP_Pr_8_30 ≈ PRIOR_BESIDE_AS_AMON
  role_label: amon
  relation: beside Him (not "create earth")
  mode: continuous delight/play
```

**Hint:** This is a **prior companion role**, not a create-verb.  
If anything “runs before” Gen’s create, this verse *states* prior presence — under the name *amon*.

---

### Num 11:12 — foster-nurse sense

| Arm | Plain job |
|-----|-----------|
| **LEFT** | Did **I** conceive / birth this whole people? (no) |
| **RIGHT** | You say “carry them…” **as the אֹמֵן / omen carries the nursing child** |

```text
OP_Nu_11_12 ≈ CAREGIVER_ANALOGY_OMEN
  role: omen = foster-carrier of dependent child
```

**Hint:** Defines **caregiver/foster** load of the א־מ־ן family.  
Tree puts the *omen* simile on the **RIGHT** (how to carry), after rejecting biological parenthood on the LEFT.

---

### Lam 4:5 — “reared” sense

| Arm | Plain job |
|-----|-----------|
| **LEFT** | those who ate delicacies → desolate in streets |
| **RIGHT** | **הָאֱמֻנִים / ha-emunim** (reared on scarlet) → embrace ash-heaps |

```text
OP_La_4_5 ≈ EMUNIM_REARED_THEN_FALL
  status: once-reared / covered elite → ruin
```

**Hint:** *emunim* as **reared/nurtured** people — another family sense BR wants.

---

### Esth 2:7 — foster-father sense

| Arm | Plain job |
|-----|-----------|
| **LEFT** | He **was אֹמֵן / omen** to Hadassah/Esther (no father/mother) |
| **RIGHT** | Mordecai **took her as daughter** |

```text
OP_Es_2_7 ≈ OMEN_FOSTER_THEN_ADOPT
  assign foster → outcome daughter
```

**Hint:** Tree is almost a mini-program: **role assignment ‖ adoption outcome**.

---

### Nah 3:8 — great-name sense

| Arm | Plain job |
|-----|-----------|
| **LEFT** | Are you better than **נֹא אָמוֹן / No-Amon**, city on waters? |
| **RIGHT** | sea as her wall |

```text
OP_Na_3_8 ≈ PROPER_NAME_NO_AMON
  amon as place-name / great city
```

**Hint:** Proper-name overload of the same consonants.

---

### Prov 8:22 — land cable into Gen

| Arm | Plain job |
|-----|-----------|
| **LEFT** | YHWH **acquired me as רֵאשִׁית / reishit** of His **way** |
| **RIGHT** | **before** His works of old |

```text
OP_Pr_8_22 ≈ ACQUIRE_AS_REISHIT_BEFORE_WORKS
  define: reishit = acquired beginning of path
  when: prior to works (mif'alav)
```

**Hint:** This is the **same keyword** as Gen’s LEFT (*reishit*), plus explicit **prior-to-works**.

---

## 3. Put the code side by side

```text
Gen 1:1
  L: reishit + CREATE + God
  R: et heavens + et earth

Prov 8:22          ← same word "reishit"
  L: acquire me AS reishit of His way
  R: BEFORE works

Prov 8:30          ← BR open (not same word as Gen)
  L: beside Him AS amon + daily delight
  R: play always

Num 11:12 / Esth 2:7 / Lam 4:5 / Nah 3:8
  = sense-table for amon family (care / foster / reared / great-name)
```

---

## 4. Is Gen “calling a function”?

### Written-only answer (tree + shared Hebrew)

**Yes, one clear candidate call:**

```text
Gen 1:1 LEFT uses:  reishit
Prov 8:22 DEFINES:  reishit = (wisdom) acquired as beginning of His way, before works

≈  reishit = CALL resolve_reishit()  
   resolve_reishit() implemented at Prov 8:22
```

That is **lemma resolve**, not a programming language `call` opcode — but as structure it is:

- Gen **uses** a term  
- Prov 8:22 **supplies a prior-time definition** of that term  

Gen’s RIGHT side (`et` dual domains) stays **local** (TIR-015 include-list). It does not need Prov 8:30.

### What Gen does *not* call (from Written trees alone)

| Remote | Shared with Gen 1:1 tree? |
|--------|---------------------------|
| Prov 8:30 *amon* | **No** shared lemma with Gen 1:1 |
| Num 11:12 *omen* | **No** |
| Lam 4:5 *emunim* | **No** |
| Esth 2:7 *omen* | **No** |
| Nah 3:8 *No-Amon* | **No** |

So the **amon multi-sense bundle is not a Gen tree import**.  
It is a **BR dispatch table** that *opens* the unit, then **lands** on Gen via *reishit* (Prov 8:22).

```text
BR MANUAL FLOW (Oral):
  OPEN  Prov 8:30 (amon)
  DISPATCH senses → Num / Lam / Esth / Nah
  LAND  Prov 8:22 (reishit) → Gen 1:1

WRITTEN CALL EDGE (code):
  Gen 1:1.reishit  ──resolve──►  Prov 8:22
```

---

## 5. What the trees hint about “Bible as code”

### A) Gen 1:1 is a **short boot instruction**

Tree: **frame+create ‖ domain inventory**.  
Very dense. Needs **external define** for `reishit` if “beginning” means more than clock-time.

### B) Prov 8:22 is a **definition module** for that frame word

Tree: **acquire-as-reishit ‖ before works**.  
Looks like a **header file** for `reishit`.

### C) Prov 8:30 is a **prior-agent module**

Tree: **beside-as-amon ‖ continuous play**.  
If the system has “plan/wisdom before build,” this is that process **named**, not Gen’s create verb.

### D) The four proofs are **overload cases** for one opcode family

Each tree is a **self-contained micro-op** (foster, reared, name…).  
BR wires them as **cases** of `amon`, not as Gen callees.

### E) Combined picture

```text
        [Prov 8:30] prior companion (amon)
              │
              │  BR only (polyroot manual)
              ▼
        [sense table: Num, Lam, Esth, Nah]
              │
              │  same speech (Prov 8) / BR land
              ▼
        [Prov 8:22] DEFINE reishit (before works)
              │
              │  Written lemma + BR land
              ▼
        [Gen 1:1] USE reishit → CREATE + et domains
```

**Gen “calls” (resolves) reishit.**  
**BR also “calls” amon senses, then jumps to that reishit path.**

---

## 6. Confidence

| Claim | Label |
|-------|--------|
| Trees/top splits for all 7 verses | **tested** (poetry force_prose provisional) |
| Gen 1:1 = create@reishit + et domains | **tested** (matches existing boot unit) |
| Prov 8:22 defines reishit prior to works | **hypothesis** from tree arms |
| Gen Written-call → Prov 8:22 via reishit | **hypothesis** (strongest Written edge in cluster) |
| Amon lattice = Gen tree call | **failed** (no shared lemma) |
| Amon lattice = BR dispatch into land | **tested** as midrash structure |

---

## 7. What to do next (if this direction works)

1. Same method on **light twin** (Job 38:15, Prov 4:18) next to Gen 1:3–4.  
2. Add real **poetry ranks** so Prov trees are not force_prose.  
3. Try a second cluster (e.g. *reishit* inventory BR 1:4) — pure Written lattice.

---

## 8. Bottom line (simple)

We derived **tree-code** for the first BR set.

- **Gen 1:1** = “create under *reishit*, include heavens+earth.”  
- **Prov 8:22** = “I am *reishit* of His way, **before** works” → best **function/define** Gen can call.  
- **Prov 8:30 + four proofs** = **role-library for *amon***, used by BR to open, **not** wired into Gen’s tree by shared words.  
- So: **yes, Gen may call a remote define for *reishit***; **no, Gen does not call the amon sense-table in Written** — BR does that in the manual layer.

Files:  
`logic/units/br_1_1_amon_cluster_tree_logic_2026-07-26.yaml`  
`reviews/br_link_studies/DERIVE_amon_cluster_tree_code_2026-07-26.md`  
`reviews/br_link_studies/_amon_cluster_trees.json`
