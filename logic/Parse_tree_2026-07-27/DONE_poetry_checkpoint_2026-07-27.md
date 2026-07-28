# DONE — Poetry / ta’amim checkpoint closed

**Date:** 2026-07-27  
**Rule set:** `v3` (`logic/taamim_rules/CURRENT`)  
**Status:** **CLOSED** for this arc  
**Kind:** checkpoint declaration · **not** binding religious law  

---

## How trees are displayed (contract) — **PERMANENT**

**Canonical:** **`logic/TREE_DISPLAY.md`** · `Agents.md` · STANDING §6  
**Owner order:** top-down **B# · GLUE|ATOM** with **English brick glosses** (saved in every memory file).

```text
### TREE  Gen.1.3  ·  taamim v3  ·  pure binary + glue
words=6 · bricks=3 · leaf_complete=yes · pure_binary=yes · system=prose
en: "And God said, Let there be light, and there was light."

PHRASE  (6w · binary)
├── PHRASE  (4w · binary)
│   ├── B0 [0–1] · GLUE  "and God said"
│   └── B1 [2–3] · GLUE  "let there be light"
└── B2 [4–5] · GLUE  "and there was light"
```

CLI `--tree` = secondary debug / unit `tree_ascii` only — **not** the primary chat tree.

---

## Closure pack results

### Structural smokes (v3)

| Corpus | Verses | unique | leaf_complete | pure_binary | system | ok_all |
|--------|-------:|-------:|--------------:|------------:|--------|-------:|
| **Proverbs** | 915 | 915 | 915 | 915 | poetry | **915/915** |
| **Psalms** | 2527 | 2527 | 2527 | 2527 | poetry | **2527/2527** |
| **Job frame** (chs 1–2, 42) | 52 | 52 | 52 | 52 | **prose** | **52/52** |
| **Job body** (chs 3–41) | 1018 | 1018 | 1018 | 1018 | **poetry** | **1018/1018** |
| **Job total** | 1070 | 1070 | 1070 | 1070 | split OK | **1070/1070** |

Machine JSON:

- `_smoke_prov_v3_2026-07-27.json`
- `_smoke_ps_job_v3_2026-07-27.json`

### Goldens

```text
python3 taamim_tree_parse.py --test   →  23/23 pass (v3)
```

### Pre-Code poetry logic units

| Unit | Refs | Pattern | TIR |
|------|------|---------|-----|
| `prov_03_trust_know` | 3:5–6 | dual trust ‖ no-lean; know → He straightens | 023, 024 |
| `prov_14_way_death` | 14:12 // 16:25 | path before man → end death | **025 tested** |
| `prov_15_soft_harsh` | 15:1 | soft answer ‖ harsh word | **023 tested** (2nd locus) |

All units **`status: draft`** (honest; not frozen law).

### TIR poetry block

| ID | Pattern | Confidence after closure |
|----|---------|--------------------------|
| **TIR-023** | Poetry dual A‖B (imperative or parallel cause→effect) | **tested** (3:5 + 15:1) |
| **TIR-024** | Command → divine result (`ו/הוא` …) | **hypothesis** (3:6 only) |
| **TIR-025** | Path-claim → end-result | **tested** (14:12 // 16:25) |

---

## Explicitly still open (future research — not unfinished repair)

| Item | Why not blocking |
|------|------------------|
| Freeze units to `status: frozen` | Ritual choice; draft is correct until re-read |
| Promote **TIR-024** | Needs a second divine-result dual |
| Wickes / hand-parse fidelity audit | Scholarship depth; not structural smoke |
| Full Tanakh bulk parse | Deferred by design |
| More wisdom units (Ps logic, etc.) | New arcs, not this checkpoint |

---

## Certainty statement (stop line)

> Under ta’amim **v3**, every verse of **Proverbs, Psalms, and Job** parses **unique + leaf_complete + pure_binary** with the correct **poetry/prose system** (Job frame prose). **23** goldens lock shapes. Three draft Pre-Code units derive logic from locked trees. Poetry TIRs **023** and **025** are **tested**; **024** remains **hypothesis**. Trees in chat use **permanent top-down B# GLUE|ATOM English** (`logic/TREE_DISPLAY.md`). **Not** binding religious law. **Not** full Tanakh. **This poetry checkpoint is CLOSED.**

---

## Reproduce

```bash
python3 taamim_tree_parse.py --test
python3 taamim_tree_parse.py Prov.15.1 --tree
python3 taamim_tree_parse.py Job.1.1 --tree   # prose frame
python3 taamim_tree_parse.py Job.3.3 --tree   # poetry body
python3 taamim_tree_parse.py Ps.1.1 --tree
```
