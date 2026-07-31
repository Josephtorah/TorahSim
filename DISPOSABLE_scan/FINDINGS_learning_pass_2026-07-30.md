# FINDINGS MEMO — the learning-pass scan of the whole Torah
**2026-07-30 · branch brian-speed-test · owner order: "write the findings memo… with
details on how the later parts actually use the earlier parts. How will the system set
up databases and track across verses and books"**

Provenance: everything below is machine-measured from the DB (5,853 verses, 80,052
words, OSHB morphology, Strong-keyed lemmas, v3 ta'amim trees) by
`DISPOSABLE_scan/fast_scan.py`. No Oral sources were read; no unit logic was derived or
touched. This is a survey, not logic (Pre-Code intact). The scan directory is
disposable; this memo is the artifact intended to survive it.

---

## 1. The headline measurement: the Torah is a program that increasingly reads its own earlier output

Treating every content lemma (noun/verb, Strong-keyed) as a *symbol*, first occurrence
as its *definition site*, and each later occurrence as a *read*:

| book | content tokens | NEW lemmas (book debut) | tokens reading earlier books | read% |
|------|---------------|--------------------------|------------------------------|-------|
| Gen  | 14,301 | 1,625 | 0 | 0% |
| Exod | 11,736 | 608   | 9,020  | 76% |
| Lev  | 8,098  | 270   | 7,333  | 90% |
| Num  | 11,799 | 461   | 10,744 | 91% |
| Deut | 9,706  | 313   | 9,198  | 94% |

Genesis is the declaration block: 1,625 symbols defined from nothing. Every later book
runs mostly on inherited symbols, and the new-vocabulary budget shrinks monotonically.
Deuteronomy — traditionally *Mishneh Torah*, "the repetition of the Torah" — is 94%
re-reads by measurement, not just by reputation.

Inside Genesis the same gradient exists at chapter grain: ch. 1 = 0% reads (76 new
symbols — the boot); ch. 2 = 45%; ch. 3 = 71%; and **ch. 7, the flood's peak, is 90%
reads** — the destruction chapter defines almost nothing. Un-creation is written in
creation's own vocabulary (see §2.4).

## 2. The mechanisms: HOW later parts use earlier parts

The scan shows at least eight distinct reuse mechanisms. Each is listed with its
measured evidence (all refs machine-extracted; nothing below is interpretive beyond
naming the pattern).

### 2.1 Registry reads — entities installed once, referenced everywhere
The Gen-1 installs are read across the whole corpus: *eretz* (earth, defined 1:1) —
291 later uses in Genesis alone, then 136/82/123/197 across the other four books;
*yom* (day, 1:5), *shamayim* (heavens, 1:1), *mayim* (waters, 1:2), *natan* (the
install verb, 1:17) — all five-book symbols. The machine's `read_before_install` flag,
which we invented for gen_02's presupposed *mayim*, is in fact the corpus's dominant
mode: nearly everything after Genesis 1 is a presupposition read.

### 2.2 Formula re-runs — earlier output invoked as a callable
- **The pru-u-rvu mandate** (parah 6509 + ravah 7235 adjacent): 12 verses —
  Gen 1:22 (fish) → 1:28 (humans) → 8:17, 9:1, 9:7 (post-flood) → 17:20 (Ishmael) →
  28:3, 35:11 (patriarchal El-Shaddai blessings) → 47:27, 48:4 → **Exod 1:7** (Israel
  in Egypt: fulfilled at national scale, with *va-yishretzu* spliced in) → **Lev 26:9**
  (covenant promise: "I will make YOU fruitful and multiply you" — the formula moves
  into God's contractual first person). The BLESS operator we modeled as a *standing*
  mandate (WORLD facts, not SPECS) is corroborated by the whole corpus: the directive
  is re-invoked at every reboot, covenant, and national milestone.
- **The genealogy template**: Gen 5 and Gen 11 share exact 4-grams
  (`מאות שנה ויולד בנים` 11x across exactly those two chapters) — two ledger chapters
  running one literal template, centuries of content through a fixed formula. Gen 5
  needed only 13 new symbols; the digest identifies ledger chapters numerically.
- **Recurring social/narrative formulas** (from the 4-gram concordance):
  "if I have found favor in your eyes" (5x: 18:3, 30:27, 33:10, 47:29, 50:4);
  the etiology formula "therefore his name is called" (25:30, 29:34, 31:48);
  the section-boot token "and it was after these things" (22:1, 39:7, 40:1).
- **The inventory formula** `ha-romes al-ha-aretz` ("that creeps on the earth"):
  coined in the creation charter (1:26), re-run at flood boarding (7:14) and flood
  exit (8:17) — the same manifest language used to load and unload the world.

### 2.3 Re-issue after reset — the reboot re-runs the boot
After the flood, the system restarts by re-running day-5/6 output nearly verbatim:
8:17 re-issues the mandate WITH the swarm verb (*ve-shartzu*), 9:1 and 9:7 re-run
*peru u-revu* to Noah's line, and 9:6 re-reads *tzelem* (image, 1:26-27) as the legal
ground for the bloodshed prohibition. The tov-test does NOT return after the flood —
the QA gate of the first creation is conspicuously not re-run at the second.

### 2.4 Reversal-by-same-symbols — un-doing uses the original's registry
- ***Tehom*** (the deep, 1:2): re-opened at 7:11 ("the fountains of the great *tehom*
  burst"), closed at 8:2, then dormant until the blessings-poetry (49:25; Exod 15:5,8;
  Deut 8:7, 33:13). Day-2/3 partition infrastructure is operated in reverse, by name.
- ***Bara*** (create): 8 Genesis uses, all in chs. 1–6, and the last is its own
  cancellation — 6:7 "I will blot out … whom I have *created*." After that, exactly
  three returns in the Torah: Exod 34:10 (covenant wonders "not *created* in all the
  earth"), Num 16:30 ("if the LORD *creates* a creation" — the earth's mouth opening:
  the creation verb summoned for a swallowing), Deut 4:32 ("since the day God
  *created* adam"). The strongest verb is rationed to world-scale interventions and
  its own retrospective.

### 2.5 Operator migration — divine operators handed to (or seized by) creatures
- **The tov-test escapes containment**: *saw-that-good* runs 7 times in Gen 1 as the
  oracle's gate; its next two occurrences are **Gen 3:6** (the woman "saw that the
  tree was good" — a creature running the divine predicate on the forbidden object)
  and **Gen 6:2** ("the sons of God saw that the daughters were good" — immediately
  before the flood decision). Both fall-points are marked by unauthorized runs of the
  QA predicate. Its single Exodus occurrence: **2:2 — Moses's mother "saw him, that he
  was good"** — the creation-test formula opening the redemption arc.
- **Naming is delegated, then reclaimed**: *qara-shem* runs 86 times Torah-wide. What
  ends at day 3 (our EXPORT_naming_series_ends) is only *God naming cosmic entities*;
  the operator passes to the human at 2:19-20 (Adam names the animals — explicitly
  brought "to see what he would CALL them") and to parents/founders for 60+ runs; God
  re-takes it precisely at covenant re-identifications — Abraham 17:5, Sarah 17:15,
  Israel 35:10 — and self-invokes it at Exod 33:19/34:5 ("proclaimed the NAME"). The
  [OPEN] flag on gen_04's export was correct but half the story.
- **The mashal (dominion) trail**: assigned to the luminaries at 1:18 (our ASSIGN
  precursor), it is next applied to the husband (3:16), then to sin at the door
  ("you shall RULE over it," 4:7), then dormant until Joseph (37:8 "will you RULE over
  us?"; 45:8,26 — he does). The office vocabulary of day 4 becomes the book's language
  of human power.

### 2.6 Symbols hardening into law — Genesis vocabulary becomes legal category
- ***Sharatz*** (swarm, day 5's delegation verb): Gen 1:20-21 → flood (7:21 death,
  8:17/9:7 re-issue) → Exod 1:7 (Israel) / 7:28 (frogs) → **Leviticus 11 (five
  verses)**: *ha-sheretz* becomes a purity CATEGORY with statutory force. Day 5's
  cognate product ends as a defined legal term.
- **Kind-keys** (*le-min-*): delivered in Gen 1 (added at delivery on days 3/5 —
  our spec-delta finding), they resurface as the classification key of the Lev 11 /
  Deut 14 dietary lists — the partition system becomes the law's own index. (The Oral
  chain had already read them as law: kilayim from *le-minehu*, BK 55a; the scan shows
  the Written text does the same move in Leviticus.)
- ***Tzelem*** (image): 1:26-27 → 5:3 (transmitted to Seth) → **9:6 as legal ground**
  (bloodshed) → Num 33:52 (idol-images to be destroyed — the same word on the other
  side of the law).
- ***Shabbat***: the NOUN never occurs in Genesis — Gen 2:2-3 uses only the verb
  *shavat* (ceased). The institution vocabulary debuts at Exod 16:23 and the command
  form at Exod 20:8-11 — which explicitly re-reads the creation week ("for in six days
  the LORD made…"). A case where later code doesn't just use earlier output — it
  CITES it as precedent text.

### 2.7 Late poetry as symbol-table dump
Gen 49 (Jacob's blessing) is the corpus's most concentrated re-reader of the primeval
chapters. From the long-range table alone: *reshit* (1:1 → 49:3), *tehom* (1:2 →
49:25), *arur* (cursed: 3:14 → 49:7), *aqev* (heel: 3:15 → 49:17,19 — WITH *nachash*,
serpent, 3:1 → 49:17: Dan as "a serpent by the way… that bites the horse's HEELS" —
the Eden pair re-run inside one blessing line), *ravatz* (crouch: 4:7 → 49:9,14,25),
*mashal*, *chamas* (violence: 6:11 → 49:5). Exod 15 (the Sea song) re-reads *tehom*
twice. Deut 32–33 re-read *tehom* and the creation stock. Pattern: the poems at the
seams of the corpus are deliberately built from the oldest symbols — closing sections
by quoting the boot.

### 2.8 Self-segmentation carried forward
The *toledot* ("generations-of") header runs 13 times in Genesis, then continues at
Exod 6:16,19 and Num (13x, incl. ch. 3's Aaron/Moses header and the census lists) —
the corpus's own section-header device is cross-book infrastructure, and the natural
unit boundary for the real pass.

## 3. Genre signatures — the digest's numbers separate the Torah's languages

The mood columns alone classify genre with no human judgment:

- **Narrative**: wayyiqtol-dominant (Gen 1: 50 wayyiqtol; Gen 5: 60 — but with the
  genealogy template's n-grams; Lev 8, the ordination NARRATIVE inside the law book:
  63 wayyiqtol vs 1 weqatal).
- **Law**: weqatal-dominant, wayyiqtol near zero (Lev 1: **2 wayyiqtol vs 27
  weqatal**; Lev 4: 1 vs 53; Lev 5: 2 vs 46). TIR-029's THEN-chain is the law genre's
  backbone, exactly as the charter's Leviticus-1 worked example predicted.
- **Sermon** (Deut): imperative-heavy (ch. 1: 14 CMD! forms) over a weqatal
  substrate with high read% — commanded memory of already-defined symbols.
- **Ledger**: near-zero verb variety + template n-grams (Gen 5 ∥ Gen 11).

Consequence for the real pass: the scanner can pre-classify every chapter's genre and
hand each unit the right operator kit before derivation starts (narrative kit: EVENT/
RESULT/NAME/COMMIT; law kit: protasis/THEN/sanction; sermon kit: CMD!/motive-clause;
ledger kit: template instantiation). Genre misfit (a wayyiqtol block inside Leviticus)
is itself machine-detectable and always meaningful.

## 4. What the real pass's operator vocabulary will need (gap list, evidence-based)

Observed in the scan but not yet in the interpreter's vocabulary (days 1–5 kit):
1. **Dialogue/question ops** — second-person exchanges explode from Gen 3 on
   (the digest's speech-verb counts with non-divine speakers).
2. **Curse** (*arur* trail from 3:14) — the anti-BLESS; same speech-act family,
   inverse polarity, similar standing-directive semantics.
3. **Covenant ops** (*brit*: 76 verses, all five books) — a persistent bilateral
   contract object with signs, parties, and re-invocations; SPECS/LEDGER analogs
   won't fit it; it needs its own register or object class.
4. **Oath/promise** (nishba trails through the patriarch cycles into Deut's
   "the land I swore" — a promise ledger read constantly by later books).
5. **Law casuistics** — protasis/apodosis (im/ki + weqatal chains), sanction
   clauses, measure-for-measure riders (the Lev/Deut bulk).
6. **Itinerary ops** (va-yisa/va-yachan chains in Exod/Num — journey ledger).
7. **Quotation/precedent ops** — later text CITING earlier text as ground
   (Exod 20:11 citing the creation week; Deut re-citing Exodus law with variations —
   the variations being exactly the spec-delta method's next domain).
8. **Re-issue/renewal markers** — formal re-runs of earlier formulas (§2.2/2.3)
   deserve an operator (REISSUE(formula, new_recipients)) rather than fresh DECLAREs,
   so the ledger records lineage.

## 5. System design: databases and cross-verse/cross-book tracking

### 5.1 What exists now
- `verses/words/trees`: the whole Torah, osis-keyed (book+chapter+verse) — already
  global; nothing book-local anywhere in the schema.
- Frozen units are **standalone by contract**: cross-unit reads surface as
  `read_before_install` flags (mayim, raqia, aretz…). The flags ARE the import
  statements — currently unresolved by design ("cross-unit chaining is Stage E").
- `units/steps/unit_scenarios/triage/echo_candidates/oral_links`: derived, rebuildable.

### 5.2 Proposed derived tables (all rebuildable by indexers; Pre-Code safe)
1. **`symbols`** — one row per content lemma: strong key, display Hebrew, translit,
   kind (entity/verb/proper), first_osis (definition site), install_kind
   (bara/asah/yatzar/qara/narration/presupposed-at-boot).
2. **`symbol_uses`** — (lemma, osis, slot) for every content-word occurrence, with
   use_kind where classifiable: read / reissue (inside a detected formula re-run) /
   reversal (co-occurring with negation-destruction verbs) / legal (inside a law-genre
   chapter). This is the defined-at/used-at index made permanent — the scan's symbol
   table as first-class data.
3. **`formulas` + `formula_members`** — curated n-gram families (mandate, commit,
   genealogy template, courtesy, etiology, inventory) with every member verse.
   Machine proposes (the concordance); the curated list itself is a hand-authored
   YAML under `logic/` (owner-approved), indexer-loaded — same canonical/derived split
   as everything else.
4. **`trails`** — named lemma-trails (tehom, bara, mashal, aqev…) as curated YAML +
   derived member table. Trails feed `echo_candidates` with origin `scan-trail`, so
   the written-echo register's human-verdict pipeline (machine surfaces → human
   verdicts → owner sign-off) absorbs them without new process.
5. **`unit_links`** — the linker table: for every frozen unit's
   `read_before_install` flag, the resolving earlier unit + install step
   (gen_04 reads raqia ← installed gen_02 STEP_Gn_1_7). Populated automatically by
   joining flags to installs; verified by hand-authored link assertions (below).

### 5.3 Stage E — the linker (cross-unit execution)
- `run_unit.py --linked <unit>`: topologically load `depends_on` ancestors, seed the
  Machine's WORLD/REGISTRY from their `state_after` instead of empty registers; every
  `read_before_install` flag that finds its symbol upstream becomes a
  `resolved_import` record instead of a flag; unresolved ones REMAIN flags (that
  asymmetry is itself a finding — what does the text presuppose that no unit ever
  installed? e.g. *tehom*, never created on-page: a genuine boot-time presupposition).
- Standalone mode stays the default contract (units must stay green alone — that
  discipline caught real errors); linked mode is an additional check, not a
  replacement.
- **Cross-unit scenarios**: a new hand-authored file class `logic/links/*.yaml` —
  e.g. "gen_04's DECLARE reads registry labels yom/lailah written by gen_01's NAME at
  STEP_Gn_1_5; linked-mode REGISTRY must contain them before STEP_Gn_1_14 executes."
  Same grammar discipline as unit scenarios; machine-checked in linked mode.

### 5.4 Cross-book tracking
Nothing new is needed structurally — osis keys are already global and the symbol
table built Torah-wide in one pass (this scan did it in ~2s). The additions that make
it *meaningful*:
- **Definition-site authority**: when a unit eventually derives Exod 1:7, the linker
  should resolve its *sharatz*/*peru-u-revu* reads back to gen_05's installs — unit
  imports across books work exactly like within-book, via the symbols table.
- **The echo register remains the judgment layer**: scan trails are candidates, never
  verdicts. Rarity checks (verify_rarity.py) and owner sign-off unchanged.
- **Book-level dashboards** (scroll-app extension, later): per-chapter read% and
  trail-hit badges — the same honest-counter pattern as the oral badges.

### 5.5 What stays canonical vs derived (unchanged principle)
Hand-authored + owner-gated: unit YAMLs, link assertions, curated formula/trail
lists, TIR rulebook. Derived + rebuildable: every table above, all dashboards. The
147MB DB remains gitignored and snapshot-protected; nothing in this design changes
the return-to-main procedure.

## 6. Proposed unit map for the real Genesis pass

Follow the book's own headers: creation week (done: 5 units + day 6-7 pending) then
the eleven toledot blocks — 2:4 (Eden/fall/Cain), 5:1 (Adam ledger), 6:9 (flood),
10:1 (nations), 11:10 (Shem ledger), 11:27 (Abraham cycle), 25:12 (Ishmael), 25:19
(Jacob cycle), 36:1+36:9 (Esau), 37:2 (Joseph cycle). The big cycles subdivide at
scene boundaries (the digest's speech-density and wayyiqtol-tempo columns give the
cut points mechanically). Estimated real-pass shape: ~55-70 lite units for Genesis,
per the option-B plan, now with genre kits and skeletons available from this scan.

## 7. Disposition

Scanner + per-book reports: disposable with the branch, regenerable in seconds.
Worth porting to main (owner decision): this memo; the trail/formula curation as the
seed of `logic/` YAML lists; the Stage-E linker design (§5.3) as the spec for
cross-unit chaining when the owner orders it.
