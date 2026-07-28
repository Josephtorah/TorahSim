# Round 5 report — ten real structure passes

**Date:** 2026-07-23  
**Corpus:** `Data/bereshit_rabbah_he.json` — **100 chapters · 1036 sections · ~1.35M chars · 5133 marked cites**  
**Stance:** open mind; structural map; not finished codec; not binding law  

**Pass files (detail):** `round5_passes/PASS_01_…` … `PASS_10_…`  
**Machine data:** `round5_passes/_round5_scan_data.json`  

This round **actually ran ten separate analyses** (each with its own question, counts, and pass write-up). This file is the **main-folder report** only.

---

## What each pass asked

| # | Pass | Core question |
|--:|------|----------------|
| 1 | Text mass | Where is the *page weight* (chars/words), not only section counts? |
| 2 | Citation load | How heavy is the proof load per section/chapter? |
| 3 | Formula stack | Which operators dominate? Which chapters are operator-hot? |
| 4 | Divine titles | How is God staged (Elohim vs HKBH vs Shekhinah…)? |
| 5 | Actor heat | Do persons light up on the Genesis spine? |
| 6 | Import books | Which biblical books feed BR early vs late? |
| 7 | Linkage machinery | Mashal-apply vs verse-proof dual track? |
| 8 | Multi-view / multi-voice | Where are alternate readings vs rabbi chorus? |
| 9 | Anomalies | Which chapters are outlier *types*? |
| 10 | Verse co-citation | Hub verses and verse/book pairs that travel together? |

---

## Executive findings (all ten)

### 1. Mass is late-weighted; hubs are real
Late chapters (61–100) carry the highest average text mass. Heaviest chapters include **98, 65, 44, 91, 1, 84, 68, 70** — Joseph/tribal end + patriarch hubs + creation boot. Section-count ≠ mass (some chapters are few-but-fat).

### 2. Proof-saturated client
~**96%** of sections have ≥1 marked citation; avg ~**5 cites/section**. Load **rises** early→late (avg 3.6 → 5.8). Extreme unit: **BR 42:3** with **36** marked cites. Late BR almost never goes without a proof tag.

### 3. Shared operator middleware
Top glue: identity/restrictive (*zeh*, *ela*), proof (*shene’emar*, *hada hu*), attribution (*beshem*), parable (*mashal*). Composite hot chapters: **98, 99, 1, 44, 65, 84, 75**. Ch **1** and **99** are especially dense *per section* (boot + export).

### 4. Divine title stack (not one string)
| Register | Shape |
|----------|--------|
| **HKBH** (~417 secs) | Default midrash narrator-God |
| **Elohim** (~257) | **Front-heavy** creation texture |
| **Shekhinah / ha-Makom** (~30s) | Thinner; mid→late presence/place |
| **Ribono** (~34) | Occasional address |

### 5. Cast graph tracks Genesis
Adam early → Noah mid → Abraham mid → Jacob/Esau late → **Joseph almost only late** (122/137). Moses/David are **import cast** across the book for proof/typology—not spine-locked only.

### 6. Import graph flips over time
| Band | Genesis fraction of cites |
|------|--------------------------:|
| Early | ~**29%** (more Psalms/Isaiah/Job petihah library) |
| Mid | ~48% |
| Late | ~**52%** |

Front = **library bootloader**; bulk/late = **Genesis-native app** still calling shared Nakh packages.

### 7. Dual linkage engines
- **Proof highway:** *shene’emar* / *dikhtiv* / *hada hu* (hundreds of sections)  
- **Parable apply:** *mashal* (~280) with *kakh* co-present in ~**121** sections (~43% of mashal secs)  
- *Keneged* / *lefikakh* / *talmud lomar* secondary but real  

### 8. Multi-view rare; multi-voice common
- *Davar aher* in **160** sections; **only ~10** with 3+ stacks (true multi-resolver rarity)  
- **~578** sections have 3+ rabbi-tokens — **chorus book**  
- Multi-voice ≠ multi-view  

### 9. Chapter modes (outliers are features)
| Mode | Examples |
|------|----------|
| Narrative bulk (mass ↑, cite density not max) | 65, 44, 84, 70, 12… |
| Proof-dense compact | 62, 95, 25, 92… |
| Install / multi-view hub | ch.1 (mass + formula); ch.65 (DA z extreme) |

### 10. Hub-and-spoke citation graph
- **3009** unique labels; **~63%** appear once; only **8** labels hit ≥10 times  
- Top reused: Gen **32:4, 18:19, 12:1, 27:33, 3:17, 25:23, 22:2, 28:11…** (story nodes, not only creation)  
- Strongest book edge: **Gen+Psalms** (213 co-sections), then Gen+Isa, Gen+Deut, Gen+Prov  

---

## Combined architecture picture (Rounds 1–5)

```text
GENESIS ORDERED SPINE
        ↑
BR MONOREPO
  BOOT (early): wide Nakh imports, Elohim texture, operator install, ch.1 mass+formula
  MIDDLEWARE: zeh/ela · shene'emar/hada · beshem · mashal→kakh · questions
  VOICE: multi-rabbi chorus common; stacked davar aher rare
  TITLE STACK: HKBH default · Elohim creation · Shekhinah/Makom presence
  CAST: lights on spine + import cast (Moses/David)
  MASS: late-weighted story apps
  PROOF: density rises late; hub verses power-law; Gen↔Psalms bridge
  CHAPTER MODES: bulk app | proof compressor | install hub
  SHUTDOWN: tribal/Joseph mass (98…) + dense ops (99)
```

---

## How this round was run (honesty)

| Item | Detail |
|------|--------|
| Pass count | **10 separate analyses** |
| Pass write-ups | `round5_passes/PASS_01` … `PASS_10` |
| Shared compute | One corpus load; each pass uses its own metrics/questions |
| Report | This file in **main** `br_structure_scans/` |
| Clutter rule | Detail stays in subfolder; reports stay upstairs |

Not ten independent process restarts—but **ten real passes with ten files**, not “ten insights from one vague glance.”

---

## One sentence

**Round 5 shows BR as a late-mass, proof-rising, spine-cast, dual-linkage monorepo with a divine title stack, a power-law verse graph (Gen↔Psalms strongest), rare true multi-view, common multi-rabbi chorus, and distinct chapter modes—installed early with a wide library, executed mid/late as Genesis-native applications.**

---

## Next options

- Another **10 real passes** (new angles: e.g. petihah graph, gender markers, messiah language, Aramaic density, chapter-to-Gen mapping precision)  
- Resume **sequential BR** packets (~3:2)  
- Deep-dive one pass (e.g. verse co-citation packages or actor heat) into a tutorial page  
"""
