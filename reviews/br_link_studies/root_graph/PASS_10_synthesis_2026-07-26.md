# Pass 10 — Synthesis: what is the “link graph”?

**Date:** 2026-07-26 · **Status:** working model after 10 searches

## Search path (what we did)
1. Inventory all BR co-cite edges  
2. Rank root hubs  
3–6. Deep packages: light, head/beginning, hide/deep, amon, mute  
7. Early/mid/late BR  
8. Components / islands  
9. Petihah vs body  
10. This synthesis  

Also: multi-root edges (share ≥2 roots) = 374; top root-pairs (noise-aware) in data file.

## Section cliques (≥3 verses sharing one root in one BR unit)

| BR locus | Root | # verses | Sample verses | Petihah? |
|----------|------|--------:|---------------|----------|
| 88:5 | כוס | 8 | Gen 40:11, Gen 40:13, Jer 25:15, Jer 51:7, Ps 116:13, Ps 11:6… | False |
| 12:6 | אור | 7 | Gen 1:4, Isa 30:26, Job 37:3, Job 38:15, Prov 13:9, Prov 4:18… | False |
| 25:3 | רעב | 7 | 2Kgs 6:25, 2Sam 21:1, Amos 8:11, Gen 12:10, Gen 26:1, Gen 45:6… | False |
| 41:3 | מואב | 7 | 2Chr 20:1, Deut 23:4, Ezek 25:11, Isa 15:1, Josh 24:9, Mic 6:5… | False |
| 56:2 | שחה | 7 | 1Sam 1:28, Exod 24:1, Exod 4:31, Gen 22:5, Isa 27:13, Ps 95:6… | False |
| 64:2 | רעב | 7 | 2Kgs 6:25, 2Sam 21:1, Amos 8:11, Gen 12:10, Gen 45:6, Prov 10:3… | False |
| 64:8 | באר | 6 | Gen 26:18, Gen 26:19, Gen 26:20, Gen 26:21, Gen 26:22, Gen 26:33 | False |
| 84:20 | קרע | 6 | 1Kgs 21:27, 2Kgs 6:30, Esth 4:1, Gen 37:34, Gen 44:13, Josh 7:6 | False |
| 89:6 | חכמ | 6 | Gen 41:39, Gen 41:8, Isa 10:13, Obad 1:8, Prov 14:6, Prov 29:11 | False |
| 91:6 | יספ | 6 | Gen 41:55, Gen 42:25, Gen 42:3, Gen 42:36, Gen 42:7, Gen 42:9 | False |
| 92:4 | יספ | 6 | Gen 43:15, Gen 43:16, Gen 43:17, Gen 43:19, Gen 43:25, Gen 43:26 | False |
| 1:15 | שמימ | 5 | Gen 1:1, Gen 2:4, Isa 48:13, Isa 66:1, Ps 102:26 | False |
| 12:6 | עצה | 5 | Gen 3:17, Gen 3:24, Gen 3:8, Isa 65:22, Prov 3:18 | False |
| 17:1 | שמימ | 5 | Gen 1:1, Gen 1:14, Gen 1:20, Gen 1:26, Gen 1:9 | False |
| 35:3 | אהל | 5 | 1Kgs 8:66, 2Chr 7:10, Josh 22:6, Josh 22:7, Josh 22:8 | False |

Examples show **package teaching**: light clique (BR 12:6), famine clique, cup/kos clique, Moab clique, bow/worship clique.

---

## What we think the link graph **is**

```text
BR LINK GRAPH (working model)
═════════════════════════════

NODES
  - Written verses (Tanakh)
  - optionally: root-family nodes (packages)

EDGES (several types, not one)
  Type R  ROOT-FAMILY share     (~16% of co-cites)   T9a
  Type S  STRONG'S ID share     (~19%, overlaps R)
  Type P  POLYROOT / root-only  (~2%, high value)    T9a flagship
  Type U  SURFACE/SOUND play    (T9b; No-Amon; noisy if automated)
  Type O  OPCODE EXPAND         same family, new params (T6)
  Type D  DUAL-RAIL             complementary jobs, no shared root (T4)
  Type B  BLOCK/STORY/NAME      narrative co-occurrence
  Type M  METHOD/SCHOOL         particles, hermeneutic

STRUCTURE
  - Many small/medium ISLANDS (components), not one giant web
  - HUB PACKAGES: אור, רעב, אמנ, סתר, חכמ, names…
  - Petihot emphasize Type P (root-only literacy)
  - Body narrative emphasizes Type B/S (same names/words)

ROLE OF BR
  Selects packages and draws temporary multi-edges
  in one teaching section (cliques of 3–8 verses on one root)
```

## Relationship to “Bible as code”

| Graph idea | Code analogy |
|------------|--------------|
| Root family | Package / namespace |
| Verse | Symbol export / call site |
| BR section clique | Tutorial that imports a package and shows several symbols |
| Island components | Separate libraries (light lib, famine lib, …) |
| Type P edges | Same package, different class members (polymorphism) |
| Type D edges | Two packages composed in one feature |

## What we did **not** find
- A single global root that ties all BR cites  
- Root share as majority of edges  
- Petihot having the *highest* raw root-share (they have highest *root-only* quality)

## Confidence
| Claim | Label |
|-------|--------|
| Multi-type link graph model | **strong hypothesis** |
| Package islands (light, amon, famine…) | **tested** (cliques + hub counts) |
| Petihah trains root-only literacy | **tested** (rate split) |
| Automated surface-only edges | **noisy** — manual T9b only for now |

## Recommended next (future, not blocking)
1. Curated package graphs (human-filtered hubs: אור, אמנ, סתר, בדל, ברא)  
2. T9b homograph pass for same letters / different Strong’s parent  
3. Overlay T6 expand parameters on אור package edges  
