# How do we know something is a link? (logic for discovery)

**Date:** 2026-07-26  
**Kind:** method · plain + technical · **not** binding law  
**Status:** **tested** on sample ta'amim of absolute ports + controls; **hypothesis** for full discovery pipeline  

---

## 0. Direct answers

| Question | Answer |
|----------|--------|
| Do absolute links become “obvious” after you find them? | **Often yes in hindsight** (unique Hebrew password). They were not labeled with a neon sign. |
| Do they stand out in the ta'amim tree? | **The tree structures the verse.** It does **not** paint “this word is a hyperlink to Job 38:15.” Ports have normal, readable splits — so do ordinary verses. |
| Is there one cantillation mark that means “link”? | **No** (not found; not in our TIR catalog). |
| Is there one letter that means “link”? | **No** universal link-letter. Some letters/particles are **operators inside a verse** (*et*, *gam*, *akh*, *raq*), not cross-book hyperlinks. |
| How do we discover **all** links? | Run **typed discovery rules** (below), not hope for a single magic mark. |

---

## 1. Three different kinds of “link” (do not mix them)

```text
TYPE A — Inside one verse (structure)
  Tool: ta'amim tree + particles
  Example: etnahta splits Gen 1:4 into "saw light good" | "divided light/dark"
  Example: את / et marks object list (TIR-014–016)

TYPE B — Across verses, same codebase (Tanakh)
  Tool: rare lemma pairs / unique multi-lemma signatures / name continuity / "as commanded"
  Example: only Job 38:15 has withhold+wicked
  Example: only Prov 4:18 has path+radiant-light

TYPE C — Manual teaching (BR and friends)
  Tool: midrash quotes + minayin ("from where do we know?")
  Example: BR says: for stored light, call Job 38:15 + Prov 4:18
```

**Cantillation is Type A.**  
**Absolute ports we found are Type B.**  
**BR is Type C pointing at Type B.**

---

## 2. What the tree actually does (show work)

We parsed ta'amim on absolute ports and on ordinary control verses.

### Absolute ports — meaningful splits, but normal marks

| Verse | Etnahta (main) split (plain) |
|-------|------------------------------|
| Gen 1:4 | saw the light that it was good **‖** He divided light and dark |
| Exod 10:23 | Egyptians couldn’t see/rise three days **‖** for Israel there was light |
| Job 38:15 | He withheld from wicked their light **‖** and raised arm is broken |
| Prov 4:18 | path of righteous like radiant light **‖** going and light until day set |
| Prov 8:22 | LORD acquired me as *reishit* of His way **‖** before His works of old |
| Ps 119:160 | head of Your word is truth **‖** and forever all Your just rulings |

The **split lines up with the logic** of the verse (claim ‖ result, or group A ‖ group B).  
That makes the **payload** easier to read once you care about the verse.

### Controls — same mark types

| Verse | Also has etnahta, munah, tifha, etc. |
|-------|--------------------------------------|
| Gen 12:1 | normal prose split |
| Prov 3:5 | normal split |
| Job 1:1 | normal split |

**Conclusion:**  
There is **no special “link ta'am”** that appears only on absolute ports.  
Trees help you **parse the sentence**. They do **not** by themselves say “join me to verse X.”

---

## 3. What *does* identify a Type B (cross-verse) link?

### Primary signal we can automate: **uniqueness of Hebrew glue**

```text
IF  lemma_set S co-occurs in ≤ K verses in all Tanakh
AND S is not pure high-frequency junk (e.g. only "YHWH"+"said")
THEN those verses are CANDIDATE absolute ports / absolute edges
```

| Strength | K | Example |
|----------|---|--------|
| **Hard absolute** | K = 1 | Prov 4:18 path∩light; Job 38:15 withhold∩wicked; Prov 8:30 H525 *amon* |
| **Strong** | K ≤ 3 | Gen 1:4/1:18 light∩dark∩badal; light∩wicked (3 verses) |
| **Family / soft** | K large | light alone (~161); *emet* alone (~125) |

**After discovery, does it feel obvious?**  
Yes, for hard absolutes: once you know “path+radiance exists only once,” the link *feels* inevitable.  
Before the search, nothing in the cantillation shouted “I am unique in Tanakh.”

### Secondary signals (Written content pointers — Pass 2)

Not cantillation; **words of continuity**:

| Kind | Hebrew cue (examples) | Job |
|------|------------------------|-----|
| Same name | person / place / object name reappears | resolve earlier WRITE |
| “As commanded” | כַּאֲשֶׁר צִוָּה / *ka’asher tzivvah* | command pointer |
| Memory | זָכַר / *zakhar* “remember” | memory pointer |
| Same rare lemma lattice | *reishit* set (~49) | thematic module |

### Tertiary: BR Type C

When BR quotes A then B with *shene’emar*, that is a **manual edge**.  
Validate against Type B uniqueness when possible.

---

## 4. What identifies a Type A (inside-verse) link / operator?

These **are** often marked by **specific Hebrew words** (and structured by ta'amim):

| Mark | Kind | Rule home |
|------|------|-----------|
| **את / ואת** | object / include list | TIR-014–016 |
| **גם / וגם** | set add | TIR-017 |
| **אך** | limit | TIR-018 |
| **רק** | except / only | TIR-019 |
| **etnahta** (and ranked disjunctives) | binary phrase tree | `taamim_tree_parse.py` |
| Morph prefixes ו/ה/ב/ל/מ | glue on leaves | TIR-022 |

So: **particles and ta'amim = logic inside the verse.**  
**Rare lemma co-occurrence = logic between verses.**

---

## 5. Discovery pipeline — how to find *all* links of each type

### Pipeline B — absolute cross-verse ports (Tanakh-wide)

```text
1. Load full Tanakh with lemmas (morphhb / OSHB).
2. For every verse, build Strong’s set S_v.
3. Enumerate interesting pairs/triples from a seed lexicon
   (or all pairs with frequency filters).
4. Keep signatures with count ≤ K (start K=1, then K=3).
5. Human/logic filter: drop garbage (function-word-only sets).
6. Cluster ports that share a domain lemma (e.g. light family).
7. Optional: check BR citations as manual edges between ports.
8. Store: signature → list of refs → confidence.
```

**Output:** catalog of hard/strong ports (like Prov 4:18, Job 38:15).  
**Not yet done fully** — we sampled light/reishit/truth/amon domains.

### Pipeline A — inside-verse structure (every verse)

```text
1. Parse ta'amim tree (prose/poetry rules).
2. Assign TIR roles (particles, headers, WHEN/THEN candidates).
3. tree_coverage 100% accounted.
4. Links *within* verse = tree edges + particle ops — not cross-ref marks.
```

### Pipeline C — BR manual edges

```text
1. Extract co-citations in BR sections.
2. Prefer edges where both ends are Type-B hard ports.
3. Label as dual-track Oral documentation, not Written rewrite.
```

---

## 6. Honest limits

1. **No single “link glyph”** found in cantillation for cross-verse hyperlinks.  
2. **Uniqueness is necessary evidence for hard ports, not complete theology** — two unique verses can still be about different subjects; domain filter still needed.  
3. **Poetry books** use a different te'amim system; our prose ranks are incomplete for full Nakh automation.  
4. **Strong’s** can merge senses — always check Hebrew.  
5. “All links” is an **aspiration**; the pipeline is the path, not a finished dump.

---

## 7. One sentence

**Cantillation and particles tell you how a verse is built; rare shared Hebrew lemmas tell you which verses are absolute ports of each other; BR tells you which ports teachers wire together.**

---

## 8. Related

- Absolute scan: `SCAN_tanakh_absolute_links_2026-07-26.md`  
- Particles: `../SCAN_gen_particles_et_gam_akh_raq_2026-07-25.md`  
- Content pointers: `../ARCHITECTURE_pass2_pointers_2026-07-19.md`  
- Trees: `../../logic/TAAMIM_TREE_PARSER.md` · TIR: `../../logic/TREE_INTERPRETATION_RULES.md`
