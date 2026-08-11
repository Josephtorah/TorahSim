# TORAH_GROK PROCESS — ORAL-FIRST ERA (rewritten 2026-08-08, owner order)

## ⚠ FULL ORAL TORAH LAW (2026-08-10, owner — ABSOLUTE, supersedes any
## narrower scan practice anywhere below)

Owner, verbatim: "this effort is useless without the full use of the
oral torah. I need to re derive every verse using the full oral torah
as insight into the logic. ... We need the whole oral torah reference.
And we can never allow this drift again."

1. FULL INVERSION, EVERY BLOCK: the oral scan inverts export_links for
   the whole span and reads EVERY locally-readable listing — all
   categories. No anchor-only shortcuts, no sampling. The Oral Torah
   is insight into the LOGIC (the machine derivation: ops, cases,
   demands), not only a letter-claim source.
2. MECHANICAL COVERAGE GATE: per-block coverage (linked /
   locally-readable / read-and-logged) is counted by script and
   recorded in the audit. A readable-but-unread listing = a FAILED
   gate = no freeze. Same standing as verify_claims 0-FAILED.
3. WHOLE-SHELF DUTY: the mirror must hold the whole Oral Torah
   reference. Works the link graph cites that are absent from the
   shelf are surfaced to the owner by name — never silently skipped.
4. RE-DERIVATION ORDERED: every v1 frozen unit (97 as of this law) is
   to be re-derived under this law; order and pacing owner-directed.
5. NO NARROWING EVER without an explicit owner ruling recorded in the
   state doc BEFORE proceeding. The 2026-08-08..10 drift (two anchor
   works standing in for the full inversion) is the forbidden pattern.

## FORWARD ERA (2026-08-08, owner order: "continue with the rest of the
## books as I direct")

The RETRO AUDIT PROGRAM IS COMPLETE (run 8, 2026-08-08): all 62 frozen
units carry a chain-attested, DB-verified oral layer — zero FAILED
rows across all eight runs. The retro pipeline section below is kept
as HISTORY; the NEW-UNIT PIPELINE is now the sole forward path.

Forward-era rules:
- BLOCK ORDER IS OWNER-DIRECTED. No self-scheduled queue, no canon
  order by default: wait for the owner to name the next span/book;
  derive exactly that block, report, stop.
- Standing orders (owner, 2026-08-08, runs 7-8) apply to all forward
  work: NO subagents ever (the coordinator does every block directly,
  one at a time); NO task-list tool; LEAN-RECORD MODE for audit
  records and notes. Machine-derivation rigor and ALL gates are
  unchanged by lean-record.
- FREEZE REVIEW WAIVED (owner, 2026-08-08: "I don't want to do the
  review step. lets keep on like we did in retro runs"): new units
  freeze on the mechanical gates alone — verify_claims.py 0 FAILED +
  preflight ALL GREEN + gloss_lint clean — no external review, no
  subagents. The gates are absolute: a unit with any FAILED row or
  red scenario never freezes.
- The oral layer is built IN-PIPELINE at derivation time (steps 2-4
  below) — new units freeze with their oral_audit manifest verified
  (zero FAILED) and the insight layer sourced from it; no retro pass
  needed ever again.
- MIRROR COVERAGE CONFIRMED all five books (checked 2026-08-08):
  Minchat Shai, Kitzur Baal HaTurim, Rashi, all five Rabbah
  collections, Mekhilta, Sifra, both Sifrei, Tanchuma, Onkelos — all
  present in export_texts for Genesis through Deuteronomy. Web
  remains gap-filler only (FETCHLOG discipline).
- LEGACY DRAFTS: logic/units/ holds ~212 status:draft yamls across
  all five books (tree_derived_v1, the superseded pre-logic era —
  e.g. exo_01..., num_01..., deu_...). They are NOT current-method
  units: treat them as span-planning reference only. A new derivation
  for a span supersedes its legacy draft; do not freeze, fold, or
  render legacy drafts.
- Lev 25 (three draft units) remains ON HOLD until the owner resumes
  it.
- Verifier wish-list (unordered; would green recent UNCHECKABLEs):
  gematria/letter-count check, span-restricted count check,
  not-contains check.

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
  rule (English inline, every time) — AMENDED 2026-08-08: HEBREW SCRIPT
  is the display form going forward, transliteration RETIRED from all
  new prose — write ויסגר ("and He closed"), not va-yisgor. English is
  the only translation layer. Unchanged: the DB translit column stays
  the QUERY layer (manifest "where" clauses); frozen machine tokens
  stay; already-folded blocks are not rewritten without owner order.
  New audit blocks lint with `gloss_lint.py --no-translit`.

## NEW-UNIT PIPELINE (per block)

0. Prestage: `python3 logic/solo_tools/prestage.py <Book> ch:v-ch:v` —
   still required (token map, anchors, subs census, volitive census,
   register evidence). Read for MACHINE needs only.
1. FULL-INVERSION ORAL SCAN — FIRST, before any machine derivation
   (Full Oral Torah Law 2026-08-10; the Oral Torah is insight into
   the LOGIC, so the chain is read before the machine is built).
   Tools (all read chain_scope.yaml — scope changes ONLY by owner
   ruling recorded there):
     `chain_scan.py <Book> <ch> [--to <ch>] --list`  classification
       census: READABLE / TANAKH-VERSE / OUT(ruling named) / UNRULED.
       Any UNRULED work -> STOP, surface to owner (gate will not pass).
     `chain_scan.py ... --works` then `--work "<Work>"` per work —
       dump and READ every chain-readable listing, He+En. Each dumped
       listing is logged to the DISK ledger incrementally
       (logic/oral_audit/ledgers/<span>.jsonl — compaction/crash
       survivable; re-runs skip already-logged refs).
     `chain_scan.py ... --tanakh` — Bible cross-refs, resolved from
       elijah_docket/tanakh.sqlite.
   Reading order per block: Torah Temimah first (the per-verse Talmud
   concordance — it maps the sugyot), then Talmud/Mishnah/Tosefta,
   midrash halakhah, midrash aggadah, targums, rishonim, acharonim,
   codes. WEB fetch = gap-filler only, FETCHLOG discipline unchanged.
2. HARVEST, two streams:
   (a) LOGIC NOTES — the chain's reading of the span's cases,
       conditions, consequences, and derivations (who is liable, what
       fires when, what a word's presence/absence teaches), named per
       source, written to the audit BEFORE machine derivation. These
       feed the ops/cases/demands directly.
   (b) letter-CLAIMS (counts, spellings, anagrams, acrostics, accents,
       adjacencies) -> claims manifest, probe-before-claim as always;
       interpretive readings -> watchlist named-only; instrument-gap
       items -> watchlist UNCHECKABLE.
3. Derive machine structure (registers, cases/handlers/statutes/cards,
   per-verse step plan) WITH the logic notes in view. Machine-evidence
   facts stay unhunted, as before. Divergence between the chain's
   case-logic and the machine's derivation is RECORDED in the audit
   (named, both sides) — never silently resolved either way.
4. VERIFY, two gates:
   (a) `verify_claims.py <manifest>` — zero FAILED (unchanged; FAILED
       kills the claim or files as DISCREPANCY, never enters a unit).
   (b) `oral_coverage.py <Book> <ch> [--to <ch>]` — the COVERAGE GATE:
       every READABLE + TANAKH-VERSE listing in the ledger, zero
       UNRULED. Exit 1 = NO FREEZE. Paste its COVERAGE block into the
       audit. Same standing as 0-FAILED.
   [HISTORY: the 2026-08-08..10 anchor-scan step text (KB+MS per
   chapter + ad hoc pulls, Sefaria API verse-range formats) is
   preserved in git history at commit 68a1553 — it is the drift-era
   procedure the Full Oral Torah Law forbids.]
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

## RETRO AUDIT PIPELINE — **COMPLETE 2026-08-08 (kept as history)**
## (all frozen blocks, owner order — not forward-only)

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
