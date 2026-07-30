# Resume prompt — build the Written↔Written echo graph · continue oral triage · 2026-07-30

Paste the block below into the compacted session to resume exactly where we left off.

---

Continue work on Torah_Grok (private GitHub `Josephtorah/Torah_Grok`, clean at the latest
main commit; local web server may still be on port 8011 — restart with
`cd web/scroll && python3 -m http.server 8011` if needed).

**Read these first, in order:**
1. `logic/pre_logic_methods_2026-07-28/METHOD_language_logic_derivation_2026-07-30.md` — the method charter (incl. §4 human-vs-Oral clarification)
2. `logic/oral_provenance/v1/works.yaml` — provenance register, **APPROVED**: policy governs what each source class may do (material=chain_primary only; anthologies resolve to primaries; outside-chain=observation only)
3. `logic/oral_triage/gen_01_creation_boot_2026-07-30.md` — triage ledger, **29/483 read** (BR parashiyot 1–3 done; 5 material finds: BR 1:9, 1:14, 3:2, 3:6, 3:9)
4. `logic/pre_logic_methods_2026-07-28/ORAL_COVERAGE_review_gen01-03_2026-07-30.md` — coverage method + first review findings
5. `Data/FETCHLOG.md` — what's been fetched (caches gitignored; re-fetch = restore)

**State:** Stages A–D done; 3 frozen units (gen_01_creation_boot, gen_02_raqia_day,
gen_03_double_build) — ALL SCENARIOS GREEN, each with amendment_log entries from the
oral_links coverage review. Web scroll app live (whole Torah, JPS 1917 verse lines, search,
browse arrows). oral_links table: creation week indexed (13,940 links, 2,226 tier-1).
Day-1 source texts: 483/483 fetched to `Data/sefaria_texts/` (gitignored cache, on disk).

**TASK 1 — build the Written↔Written ECHO GRAPH (owner: "if we don't build it now I will forget"):**
The insight (owner-confirmed): when midrash cites a later Tanakh verse on a Genesis verse,
the later verse often IS early exegesis of Genesis (inner-biblical allusion). Flagship case:
tohu va-vohu ("formless and void") occurs EXACTLY twice in Tanakh — Gen 1:2 and Jer 4:23
(un-creation vision); also Isa 45:7 ("creates darkness" — closing Gen's presupposed-darkness
gap); Ps 104 (creation-week retelling); Prov 8 (reshit). Design, Pre-Code shape:
- **Detector (machine):** rare-phrase candidates via the DB — n-gram/word-pair signatures
  shared between Torah verses and the rest of Tanakh. NOTE: our DB covers Torah only; for
  whole-Tanakh echo detection either (a) start with Sefaria's link index "Tanakh" category
  (curated verse↔verse links — extend fetch_oral_links to keep category=Tanakh rows; they
  are already IN Data/sefaria_links, currently tier 3) or (b) fetch Tanakh text later.
  Start with (a): reclassify/ingest Tanakh-category links as echo CANDIDATES.
- **Register (human):** `logic/written_echo/v1/edges.yaml` — per-edge verdict:
  `allusion` (later verse deliberately reuses the earlier) / `idiom` (shared stock phrase) /
  `homiletic` (midrash's pairing only) / `open`. Each edge: both refs he+translit+en,
  the shared signature, evidence (rarity count via FTS), verdict, confidence. Owner signs
  off like TIR/provenance. Candidates surfaced by machine; verdicts NEVER auto-assigned.
- **Checker:** golden-style guard like `logic/oral_provenance/check_coverage.py`.
- Seed edges from day-1 reading: Gen 1:2↔Jer 4:23 (tohu-vohu, rarity=2 — verify via FTS),
  Gen 1:3-5↔Isa 45:7, Gen 1:2↔Ps 104:2 (or-as-garment context), Gen 1:1↔Prov 8:22.
  Verify rarity counts with real queries before writing evidence lines.

**TASK 2 — continue the day-1 oral triage reading (standing):**
Next batch = remaining local BR anchors (4:2 done/cited; 8:1, 8:12, 12:3, 12:6, 12:8,
13:12, 14:1, 17:1, 42:3, 92:6), then the Bavli block (Chagigah 12a:6/10/16/20 + 12b:1,
Megillah cluster, Berakhot 2a, Tamid 32a, Pesachim, RH 32a, Shabbat 10a, Sotah 12a,
Sukkah 49a, Taanit, Yoma 38b, Nazir 7a, BK 55a/60b, Arakhin 17a, AZ 29a, Chullin 83a),
Yerushalmi, Mekhilta, Mishnah ×4, Onkelos ×5, VR ×8, PDRK ×3, Eikhah petichta. Read from
`Data/sefaria_texts/` (filename = ref slug + hash). Append ledger rows with verdicts,
update the read counter, commit per batch. THEN: propose amendments for accumulated
material finds (BR 1:9 → NOTE_PRESUPPOSED note; BR 3:9 → echad [OPEN] note; BR 1:14 →
TIR-014/015 evidence line; BR 3:2 → RESULT latency-0 note; BR 3:6 → registry label≠entity
note) — owner approval required before touching frozen units (amendment_log pattern).

**TASK 3 — reference-tracking system (owner asked "how do we keep up"):** implement the
recommended promotion step: `index_triage.py` — parse `logic/oral_triage/*.md` ledger
tables into a DB `triage` table (unit, source_ref, status, verdict, note) so every
source-ever-read + verdict is queryable and can surface in the web app later ("N sources
read on this verse, k material"). Ledgers stay canonical (Pre-Code: DB = derived index).

**Standing rules (non-negotiable):**
- Pre-Code rule: logic authored in frozen YAML/markdown; code only interprets. Frozen units
  change only via owner-approved documented amendments (amendment_log) or new derive pass.
- Hebrew: every Hebrew/transliterated term in CHAT gets an inline English gloss (owner is
  English-only — memory: chat-hebrew-glossing). Files: he + translit + en always.
- Oral: named location only, verified from local corpus when possible, tier per the
  APPROVED provenance register; never silent-merge. Honest counters everywhere:
  enumerated / fetched / READ are three different numbers.
- Derivation narratives: one per unit (dev + beginner sections) in
  `derivation-narrative_2026-07-30/`; ASK OWNER FIRST before each addition (memory).
- Sefaria fetches: sequential, 0.5s delay, small ranges — never a whole book at once;
  log every fetch in `Data/FETCHLOG.md`. Caches are gitignored.
- Commit only when owner says; trailer: `Co-Authored-By: Claude Fable 5 <noreply@anthropic.com>`.
  Untracked `Disclosure/` and `reviews/architecture/NARRATIVE_theory_of_disclosure_*.md`
  are NOT mine — leave uncommitted unless owner orders.
- Repo stays PRIVATE (Sefaria licensing). Data/ is read-only source except owner-ordered
  additions. gh account on this machine = Josephtorah.
