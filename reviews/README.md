# Project reviews

Fast notes on other folders under `~/code` (and elsewhere) while consolidating into Torah_Grok.

**Torah_Grok architecture (this project):**  
- **Hub:** `architecture/INDEX.md`  
- `architecture/SCAN_post_torah_books_computer_model_2026-07-26.md` — every book after Torah in the computer model  
- `architecture/ARCHITECTURE_discussion_2026-07-19.md` — sequential run + data + pointers  
- `architecture/ARCHITECTURE_pass1_five_books_2026-07-19.md` … `pass5_…` — five-book roles, pointers, registries, sanctuary, genres  
- `architecture/ARCHITECTURE_genesis_stack_2026-07-21.md` · `architecture/Gods_Intention_2026-07-21.md`  


**Oral corpus framing:**  
- `RESEARCH_valid_oral_torah_2026-07-19.md` — core docs, chronology, schools, validity; MH = **possible Oral** (none ruled out)  

**Genesis Build:**  
- `GENESIS_BUILD_2026-07-20.md` — Gen as boot/init logic for a full system run (vs Lev app templates)  
- `architecture/ARCHITECTURE_genesis_stack_2026-07-21.md` — Genesis package map (full-stack lens) + Sefer Yetzirah comparison  
- `../logic/gen_boot/INDEX.md` — **Genesis boot tutorials** (plain leaf step-through 1:1–2:3 + older day-1 build tutorial)  
- `../logic/SHOW_WORK_TREES_2026-07-20.md` — **show all work:** record ta'amim trees in unit `binary_trees` (not chat-only) · standing §6a  
- `../logic/TUTORIAL_DERIVING_LOGIC_SHOW_WORK_2026-07-20.md` — **long tutorial:** how we derive logic (pipeline + day 4 trees + boot steps)  
- `NOTES_progress_observations_2026-07-20.md` — session observations: Gen whole-book, Gen→Lev variables, Exodus Oral, narrative vs law  
- `EXODUS_BUILD_2026-07-21.md` — Exodus track full draft (1–40; Mekhilta on law spine)
- `BOOK_torah_grok_journey_so_far_2026-07-21.md` — long narrative book of the project journey (audio-friendly, no tables)
- `BOOK_torah_grok_journey_so_far_2026-07-21.epub` — same book as EPUB (TOC; for readers / TTS apps)
- `LEVITICUS_BUILD_2026-07-21.md` — Leviticus track **full draft** (50 blocks / 859 vv; Sifra on law)
- `RESEARCH_narrative_model_br_ops_2026-07-21.md` — narrative as generative-model hypothesis; BR as verse-operations (not system diagram)
- `architecture/Gods_Intention_2026-07-21.md` — progressive-revelation / buried info-system frame; BR + *et* density vs Sefer Yetzirah
- `Bereshit_Rabbah_Plan_for_Genesis_2026-07-21.md` — BR plan for Genesis (gates, models, ops, pipeline)
- `BR_Genesis_Interface_2026-07-23.md` — hub for **sequential** BR-on-Genesis packets (ch.1 complete)
- `br_genesis_packets/` — individual BR openings (BR 1:1–1:15)  
- `TUTORIAL_torah_pointers_2026-07-23.md` — **beginner tutorial:** four pointer types (Written THIS, link-keys, BR citation-jumps, shown-visions) + BR *lo parash* addendum  
- `br_name_scans/` — 10-pass BR person-name scan; full report `PASS_10_synthesis_REPORT_2026-07-23.md`  
- `br_structure_scans/` — 10-pass BR **master structure** bird’s-eye; report `PASS_10_master_REPORT_2026-07-23.md`  
- `br_link_studies/` — **verse-link manual** track: petihah protocols, bridge operators (Prov 4:18 / Job 38:15), BR-as-manual theory · start `br_link_studies/INDEX.md` · summary `SUMMARY_what_we_know_2026-07-26.md`  
- `SCAN_BR_petihah_shared_refs_2026-07-25.md` — multi-cite root keys (K1/K2/K3) on BR ch.1–3  

Dated files; rename on update.

**Research placement (2026-07-26):** never put research in the **repo root**. Use **topic subfolders** under `reviews/<topic>/` (see `STANDING_DECISIONS.md` §0a).

## Speed rule (default)

| Step | Time | Do |
|------|------|-----|
| **L0 only** | ~5–10 min | Map + scorecard from **English docs**. **Stop.** |
| **Decide** | 1 min | `archive` / `cherry-pick` / `later` / `skip` |
| **L1+** | only if you say so | Deeper inventory or import |

Do **not** deep-audit every folder. Most get L0 + decision only.

### L0 is English-only (default)

- Read READMEs, SPEC/HIGHLIGHTS, CHANGELOG, ASSUMPTIONS, scorecards, session summaries — **not** a full code re-run.
- **Do not** recompile old pipelines or re-prove headline metrics unless the user asks.
- If the other project already wrote an honest English Q&A or audit, **prefer that** over inventing a 20-question interrogation.
- Optional: note hub file paths for later cherry-pick; skip SHA hashes and live metrics unless requested.
- Full 20-question technical questionnaires are **out of band** for routine audits (Torah-v6 was a one-off handoff).

## How to review the next folder

1. User pastes path: e.g. `<old-home>/code/SomeProject`
2. Create `reviews/<ShortName>/` (short name = folder basename unless collision)
3. Agent fills **only**:
   - `SOURCE.md` — absolute path, size, date if known
   - `SCORECARD.md` — template below (one page max)
   - `PURSUE.md` — ideas worth pursuing (required; table, max ~6 rows)
4. User decides. Optional: `CANDIDATES.md` only if cherry-pick files; `AUDIT-*.md` / `REVIEW-*.md` for full pastes
5. Update `PURSUE_ROLLUP.md` with any **new** cross-cutting ideas
6. Move on.

## SCORECARD template (copy)

```markdown
# <ShortName>

**Path:**  
**Size (ex venv/node_modules):**  
**Reviewed:** YYYY-MM-DD  
**Depth:** L0 | L1 | L2  
**Decision:** archive | cherry-pick | later | skip | undecided

## What it is (3–5 bullets)

## Hub files (paths worth opening later)

## Worth saving (max 5 bullets)

## Dead ends / ignore

## Open questions (max 3)

## Next action
```

## Layout

```
reviews/
  README.md                 ← this file
  PURSUE_ROLLUP.md          ← merged ideas across all projects
  Torah/                    ← one folder per source project
    SOURCE.md
    SCORECARD.md
    PURSUE.md               ← ideas worth pursuing (required)
    CANDIDATES.md           ← optional: files to port
    AUDIT-YYYY-MM-DD.md     ← optional: full audit dumps
    REVIEW-YYYY-MM-DD.md    ← optional: insight briefs
  <NextProject>/
```

### PURSUE.md template

```markdown
# Ideas worth pursuing — <Name>

| # | Idea | Why | Confidence |
|---|------|-----|------------|
| 1 | … | … | high/medium/low |

**Do not pursue from this folder:** …
```

## Naming

- One directory per source project
- Use the folder basename (`Torah`, `Torah-v4`, `Chagigah`)
- If duplicate names, append parent: `code-Torah` (rare)
- Store **each audit** as `AUDIT-YYYY-MM-DD.md` (or `AUDIT-<topic>.md`) inside that project’s folder — never mix projects in one file
