# TORAH_GROK PROCESS — ORAL-FIRST ERA (rewritten 2026-08-08, owner order)

Owner orders this rewrite encodes (2026-08-08): (1) "get rid of our own
search for crowns" — NO self-directed crown mining, ever; (2) insights
come from the Oral Torah — LOCAL-FIRST from the Data/sefaria_export/
mirror ("download and do these searches on our machine"), web as
gap-filler — verified against SNAPSHOT; (3) "If the oral torah doesn't reveal it then maybe we don't
need it"; (4) the word CROWN is KEPT, REDEFINED: **a crown is a
chain-attested, DB-verified letter-fact** — attested by a named Oral
Torah source, verified by script against the SNAPSHOT databases;
(5) NOT forward-only: ALL frozen blocks get a retro Oral audit,
starting with gen_08 (the first block after the creation week);
(6) failed verifications file to the watchlist as discrepancies.

Pilot evidence: gen_08 audit (Gen 2:4-17) — the tradition attested ~8
of our mined finds, surfaced letter-facts we missed (the toledot
full-spelling unique at 2:4; the be-hibbaram/be-Avraham anagram; the
chotam "seal" acrostic in 2:7), and the Kitzur Baal HaTurim +
Minchat Shai census-class claims scored 10/10 on SNAPSHOT
verification. Blind mining was ~60-70% of unit cost and the only
review-FAIL class (5 units running). This rewrite deletes that cost.

## What is DELETED

- Blind career-mining of prestage dumps for patterns.
- Speculative census queries hunting whole-careers / debuts / firsts.
- Free-form crown prose with hand-verified [VERIFIED] counts.
- Speculative "armed career bridge" watchlist arms.

## What is UNCHANGED (all standing laws)

- Machine derivation: prestage.py -> content module -> build_unit.py ->
  verify_text.py -> preflight.py -> superlative_lint.py; byte-identity
  of frozen units after any GLOBAL subs append; interpreter regression.
- EXTERNAL REVIEW LAW: no freeze without fresh-context whole-unit
  adversarial review (REVIEW_BRIEF.md). Structure gets full rigor.
- Freeze ritual (freeze_ritual.py, idempotent), auto-freeze on green
  preflight + review PASS; py render; indexes; corpus proof.
- Triage law: interpretive READINGS are filed named-only, never merged
  into machine state, never pushed for rulings. "Written trees first."
- Owner gates: commit/push, amendments to frozen units, derivation
  narratives (per-unit ask FIRST), Disclosure. Hebrew-glossing absolute
  rule (English inline, every time).

## NEW-UNIT PIPELINE (per block)

0. Prestage: `python3 logic/solo_tools/prestage.py <Book> ch:v-ch:v` —
   still required (token map, anchors, subs census, volitive census,
   register evidence). Read for MACHINE needs only.
1. Derive machine structure (registers, cases/handlers/statutes/cards,
   per-verse step plan). Facts the machine derivation touches for its
   own reasons (volitive census, frame-signature, re-typing witnesses)
   are MACHINE EVIDENCE, not crowns — they stay, unhunted.
2. ORAL SCAN (replaces crown-hunting) — LOCAL-FIRST (2026-08-08, owner
   order: "download and do these searches on our machine"). The curated
   Sefaria-Export mirror lives in Data/sefaria_export/ (fetched by
   logic/solo_tools/fetch_sefaria_export.py, MIRROR_MANIFEST.txt lists
   every file; refresh optional — the bucket regenerates monthly).
   Indexed into torah_grok.sqlite by
   logic/solo_tools/index_sefaria_export.py:
     export_links — every Sefaria citation anchored to a Torah verse
       (query the block's span first: what does the tradition SAY here);
     export_texts — FTS5 full-text over the mirror (read the RAW
       sources — Hebrew + English, no paraphrasing model in the loop;
       verbatim quotes come from here).
   Per block: span query on export_links -> read the loci in
   export_texts -> harvest. WEB (Sefaria API/WebFetch) is the
   GAP-FILLER only — for works absent from the mirror — and every web
   fetch still logs to Data/FETCHLOG.md. Legacy web reference set per
   block (now local where mirrored):
   - Rashi on <Book> <span>
   - Kitzur Baal HaTurim on <Book> <span>  (census-class conduit)
   - Minchat Shai on Torah, <Book> <span>  (Masorah spellings/pointing)
   - The block's midrash chapters (Bereshit/Shemot/Vayikra/Bamidbar
     Rabbah; Sifra for Leviticus, Sifrei for Numbers/Deuteronomy;
     Mekhilta for Exodus law)
   - Talmud loci NAMED by the above or by Sefaria's related-links API.
   Sefaria reference formats that work (chapter fetch returns only the
   first segment — use VERSE RANGES):
   `api/texts/Kitzur_Baal_HaTurim_on_Genesis.2.4-2.17`,
   `api/texts/Minchat_Shai_on_Torah,_Genesis.2.4-2.17`,
   `api/texts/Rashi_on_Genesis.2.4-2.9`, `api/texts/Bereshit_Rabbah.14`,
   `api/related/Genesis.2.4` (lists which commentaries exist).
   NOTE: `Baal_HaTurim_on_Genesis` is an EMPTY index — use Kitzur.
3. HARVEST: sort the take into (a) letter-CLAIMS (counts, spellings,
   anagrams, acrostics, accents, phrase-rules, adjacencies) -> claims
   manifest; (b) interpretive READINGS -> watchlist, named-only,
   unclaimed; (c) instrument-gap items (letter size, manuscript
   pointing variants) -> watchlist, flagged UNCHECKABLE.
4. VERIFY: manifest at `logic/oral_audit/manifests/<uid>_claims.json`;
   `python3 logic/solo_tools/verify_claims.py <manifest>` must show
   zero FAILED. A FAILED row either kills the claim or files to the
   watchlist as a DISCREPANCY observation (tradition vs SNAPSHOT —
   itself reportable); it never enters the unit as a crown.
5. AUTHOR the content module: machine layer as before; the insight
   layer = VERIFIED manifest rows only, one or two prose lines each,
   citing source + claim id. Per-op prose cap: ~5 lines unless a
   verified crown lands on that verse. DRAFT_NOTE carries the
   structure/probe story, not crown narratives.
6. Build/verify/preflight/lint as before.
7. REVIEW per REVIEW_BRIEF.md (structure full rigor; crowns = re-run
   verify_claims.py + spot-check manifest rows against claim_en text).
8. Freeze ritual; watchlist (slim: arms only from the sources' own
   cross-references or machine needs); state doc; owner commit word.

## RETRO AUDIT PIPELINE (all frozen blocks, owner order — not forward-only)

Per frozen unit, in canon order starting gen_08:
1. Oral scan + harvest + manifest + verify_claims.py (steps 2-4 above).
2. Write `logic/oral_audit/AUDIT_<uid>_<date>.md`: the audit RECORD
   (sources, attestation map, timing, process notes).
3. FOLD the crowns into the unit yaml (STANDING OWNER ORDER 2026-08-08,
   gen_08 precedent: "update the existing derivation... I want one
   source of truth"): add/extend the meta block `oral_audit_note_en` —
   verified crowns with sources + manifest ids, instrument gaps,
   mined-only claims kept where they do not conflict, readings
   named-only. MACHINE LAYER UNTOUCHED (steps/scenarios byte-identical;
   diff must show pure insertion). AMENDMENT GATES (all mechanical —
   the EXTERNAL FRESH-CONTEXT CHECK IS ON HOLD, owner order 2026-08-08
   "it's costing me too much time"; resume only on owner word; the
   new-unit FREEZE review law is untouched by this hold):
     (a) `git diff --numstat` = pure insertion, all inside
         oral_audit_note_en;
     (b) interpreter + scenarios ALL GREEN;
     (c) verify_claims.py = 0 FAILED;
     (d) `python3 logic/solo_tools/gloss_lint.py <yaml>` clean — the
         glossing linter (built 2026-08-08; both prior external checks
         FAILed round 1 on exactly this class).
   Scope discipline the held checker used to enforce, now self-applied:
   Torah-frame every count claim (the DB is Torah-only — never say
   "in Scripture" unless the tradition's own count is being quoted
   with its source); spelling-check patterns must not cross morpheme
   slashes; count-claims lock expect_refs. Re-render the unit HTML.
   The yaml is the one source of truth; the audit file is the record.

## Era-1 Oral infrastructure (kept, superseded for scans)

The pre-solo era left fetch_oral_texts.py / fetch_oral_links.py /
index_oral.py / index_oral_links.py and the oral_texts / oral_refs /
oral_links tables (coverage: Gen 1-2 only; tied to the triage ledger).
They are KEPT — triage history lives there — but per-block scans use
the export_* tables. Do not extend the era-1 tables; extend the mirror.

## Timing discipline

Every audit and every new unit logs elapsed wall time in its audit
file / freeze note. Watch for further process fat and report it.
