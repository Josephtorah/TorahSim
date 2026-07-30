# Oral Coverage Report — Units 1–3 vs. the Sefaria Link Index

**Date:** 2026-07-30 · **Infrastructure:** `fetch_oral_links.py` (rate-limited, resumable) →
`Data/sefaria_links/` (34 verses, fetched 2026-07-30) → `index_oral_links.py` → `oral_links`
table (13,940 links, 2,226 tier-1).
**Purpose:** answer the owner's question — "how do we know we are considering all relevant
Oral commentary?" — with numbers instead of hope, and review the three frozen units against
what the systematic index surfaced. Not binding religious law.

**Tier policy (PROPOSED, pending owner sign-off):** tier 1 = Midrash · Talmud · Mishnah ·
Targum · Halakhah (Oral proper — must be enumerated and triaged per unit); tier 2 =
Commentary/Quoting Commentary (Rishonim/Acharonim); tier 3 = Kabbalah/Chasidut/Musar/etc.

## Coverage numbers (the honest baseline)

| unit | span | total links | distinct tier-1 | cited in unit | coverage |
|------|------|------------:|----------------:|--------------:|----------|
| gen_01_creation_boot | Gen 1:1–5 | 4,383 | 483 | 1 (BR 3:7) | ~0.2% |
| gen_02_raqia_day | Gen 1:6–8 | 903 | 99 | 4 | ~4% |
| gen_03_double_build | Gen 1:9–13 | 1,405 | 175 | 2 | ~1% |

Reading of these numbers: our citations were *verified but sparse* — chosen by targeted
search, not enumeration. The index is now the checklist; "coverage" here means cited/anchored,
and triage (reviewed-but-not-relevant) will raise the honest denominator over time.

**Cross-validation both ways:** every Bereshit Rabbah citation in our units appears in the
index at the expected anchor (BR 3:7→1:5 span; 4:2/4:6/4:7→1:6–8; 5:8/5:9→1:10–11) ✓.
Conversely, our Chagigah 12a citation for the *shamayim* etymology is NOT anchored by Sefaria
to 1:8 (they anchor 12a to the 1:1–5 span) — proof that neither method subsumes the other:
**the discipline is the union** (link enumeration + phrase search + accumulated citations).

## Review findings (what changes)

### Day 3 — MATERIAL: the delta is two-way (amendment recommended)

The index surfaced **Chullin 60a–b** (local corpus, verified). Chullin 60a, R. Chanina bar
Papa: *be-sha'ah she-amar HKB"H le-minehu ba-ilanot, nas'u desha'im kal va-chomer be-atzman* —
"when the Holy One said 'by its kind' about the TREES, the grasses drew an a-fortiori upon
themselves." That reading rests on a textual fact **our own word data confirms**: the spec
(1:11) places the kind-key *le-mino* on the tree ONLY (*esev mazria zera* — no kind-key);
the delivery (1:12) has *le-minehu* on BOTH (*esev mazria zera le-minehu … ve-etz oseh-peri
… le-minehu*). So the spec/delivery delta runs in BOTH directions:
- trees LOST *peri* (recorded in the frozen unit ✓, BR 5:9)
- herbs GAINED *le-minehu* (NOT recorded — surfaced by this review; named source Chullin 60a)
Also verified in the same sugya: Rav Assi's resolution of 1:12 vs 2:5 (grasses stood at the
soil's mouth until Adam prayed for rain — "the Holy One desires the prayers of the
righteous"). **Recommended amendment:** second NOTE_SPEC_DELTA operator line + oral_note in
`gen_03_double_build` via documented derive-pass (owner approval required; frozen units are
never silently edited).

### Day 1 — upgrade available: or-ha-ganuz verified (amendment recommended)

The frozen unit carries ORAL_or_haganuz at **observation tier** ("NOT verified in local dump
this pass — fetch before use"). The index anchors **Chagigah 12a** to the day-1 span, and the
local text verifies: *or she-bara HKB"H be-yom rishon adam tzofeh bo mi-sof ha-olam ve-ad
sofo … amad u-genazo* (R. Elazar — the day-one light saw world's-end to world's-end; hidden
from the corrupt generations). **Recommended amendment:** upgrade the note observation →
verified with the exact quote.

### Day 2 — enrichments only (optional; no operator changes)

The uncited remainder of BR parashah 4 (4:1, 4:3, 4:4, 4:5 — all local) was read: 4:1
(roofing the world with water), 4:3 (R. Tanchuma's grammar-based argument that *be-tokh
ha-mayim* = exactly midway), 4:4 (the Kuti and R. Meir: the upper waters stand suspended
**by the ma'amar** — by the word — a striking Oral echo of our INVARIANT/standing-job
machine reading), 4:5 (the raqia as pool-with-dome). Candidates for optional oral_notes;
none alters an operator.

### Across all units — the machine layer stands

No finding changes any operator, TIR citation, register semantics, or scenario. The
grammar-driven derivation layer survived contact with 2,226 enumerated sources; every
change is on the Oral-notes track. This is the expected shape: Written drives logic,
Oral is cited witness.

## Unreviewed remainder (honest ledger)

Enumerated but not yet read: the large Midrash blocks (Midrash Lekach Tov's verse-by-verse
runs, Tanchuma, PDRE 3–5, Yalkut Shimoni — mostly NOT in local corpus), Yerushalmi anchors,
Targumim (5 versions per verse — systematically relevant for translation comparison),
Halakhah anchors (mostly liturgical/calendar uses of the verses). These stay on the
checklist; future passes shrink the list and record triage verdicts.

## Process going forward

1. Each new unit derivation starts by querying `oral_links` for its span (the checklist).
2. Unit oral policy line gains: "Oral coverage: N anchored tier-1; cited k; triaged m."
3. Whole-Torah link fetch proceeds in small polite batches (per-chapter invocations of
   `fetch_oral_links.py`), never a whole book in one run (owner's rate-limit order).
4. Tier policy above goes to the method charter upon owner sign-off.
