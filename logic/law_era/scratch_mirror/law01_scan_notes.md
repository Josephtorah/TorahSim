# LAW ERA — Block 1 scan notes: Exod 21:1-11 (slave-term laws)

RESUME STATE (SCAN COMPLETE, 2026-08-10): LAW ERA block 1 = Exod 21:1-11 full oral scan — DONE.
- Census: 3,286 listings | 1,936 READABLE + 26 TANAKH = 1,962 required | 1,324 OUT | 0 UNRULED.
- READ: 1,962/1,962 (100%) in 84 bites. BLOCK-1 GATE GREEN (verified mechanically: required set fully ledgered, 0 unread). Chapter-wide oral_coverage gate for exo_21_the_ordinances remains FAIL by design — 2,943 unread rows anchor at 21:12-37 (blocks 2-3) and accumulate in the SAME ledger (logic/oral_audit/ledgers/Exod_21.jsonl, now 1,962 rows).
- All 84 batch digests below (CONFIRM/ADD/MAJOR/fork tags). Major-finds registry spans digests 1-84; the marquee items: night-get (Ohr Zarua), rights-notice + consent-symmetry (Or HaChaim), king-track cluster (Pardes Yosef), Ralbag's 31 roots, Rashbam's two-layer manifesto, Hirsch's lecture-notes manifesto + no-prison thesis + proportionality gate, the triad permutation table (Yalkut 321), the sale-proportionality sugya (342:6), הלכה עוקרת מקרא three-places row closed (898:7), Moses-as-nirtza (814:3), kiddushin-by-money founded on our אין כסף (936:5), Tractate Avadim's unwaivable yiud, the Rogatchover's formalisms, TDbE's women's-law charter, Toledot Yitzchak's market-clearing analysis.
- NEXT PHASE (owner word required): derivation/coding — the exo_21 block-1 slice under the law ("we will code later" — full coverage now achieved for 21:1-11). Blocks 2 (21:12-27) and 3 (21:28-36) scans extend this same census/ledger machinery; law01_dump.py --tanakh patched (he_plain->he) for the new-Mac tanakh.sqlite.
- Scan kit mirrored at logic/law_era/scratch_mirror/ (notes, dump, census, queue).
- Frozen baseline: exo_21_the_ordinances.yaml (21:1-37, FWD-8, v1 thin-oral)
  — comparison target for the re-derivation; drift drafts (Jul 24) ignored.

Block-1 verses: 21:1 mishpatim header; 21:2-6 Hebrew slave six-year term,
ear-rite; 21:7-11 amah (maidservant) laws: designation (yi'ud), three
obligations שארה כסותה וענתה ("her food, her clothing, her marital rights"),
free release "without money".

v1 baseline highlights to test against the chain (from the frozen YAML, to
be checked as reading proceeds): case-cascade encoding, six-year timer,
ear-rite state flag, the three-obligation clause, "goes out free" handlers.

## Batch digests
(gen_08 format: per batch — work, refs, findings tagged CONFIRM / ADD /
MAJOR / diverge; scope notes for owner; every batch flushed to disk before
the next dump.)

### Batch 1 digest (Torah Temimah 21:1:1 - 21:6:9 — 52 listings, ~46 findings)
21:1 HEADER ואלה המשפטים ("and these are the ordinances"):
- TT 1:1 (Mekhilta): vav of ואלה = APPEND operator — "adds to the first:
  as the former are from Sinai, so these from Sinai" — provenance operator
  tying the civil code to the Sinai source; Marah-vs-Sinai resolved as
  klal at Marah ("courts" in general) / prat here (each law detailed) —
  two-phase legislation — MAJOR ADD.
- TT 1:2-3 (San 7b): ADJACENCY operator across the chapter boundary — "do
  not ascend by steps" (Exod 20:23) + this header -> judges deliberate
  (מתונים בדין "deliberate in judgment") + no stepping over the people's
  heads — semikhut-derivation EDGE Exod 20:23 -> 21:1 — ADD.
- TT 1:4 (Yer.San): the MISHNAH'S ordering of monetary law follows THIS
  parshah's own order — the decompiler's TOC mirrors the source — ADD.
- TT 1:5: Sanhedrin seated BESIDE THE ALTAR — textual adjacency compiled
  into ARCHITECTURAL adjacency (court next to altar; Prov 21:3 rationale:
  justice > sacrifice) — MAJOR ADD.
- TT 1:6 (San 7b): תשים ("you shall place") not "teach" = the JUDGES'
  INSTRUMENTS (strap, lash, rod, shofar, sandal) — enforcement toolkit
  encoded in verb choice — ADD.
- TT 1:7 (Eruv 54b): teacher must set reasons like a SET TABLE (שלחן
  ערוך) — the relay must include RATIONALE, not bare rulings — transmission
  protocol (joins the לאמר relay-operator dossier from gen_08) — ADD.
- TT 1:8 (Kid 35a): לפניהם ("before them") -> WOMEN EQUATED TO MEN for all
  monetary law — gender-universal scope operator at the header — MAJOR ADD.
- TT 1:9 (Git 88b): "before THEM" — NOT gentile courts (even if same law),
  NOT laymen; semikhah chain to Moses; today's courts = AGENTS of the
  ordained — THE HEADER DEFINES THE RUNTIME ENVIRONMENT: authorized
  interpreter chain required by the verse itself — MAJOR MAJOR (the
  chain-of-transmission thesis stated by the source text).
- TT 1:10-11: תשים as סימה ("treasure") — teach only the worthy; set-table
  again (Mekhilta) — ADD.
21:2 SIX-YEAR TERM:
- TT 2:1: TWO ENTRY PATHS — court-sold thief (here) vs self-seller (Lev
  25) with DIFFERENCE TABLE (self-seller: no piercing, no Canaanite
  maidservant, 6+ yrs allowed, no severance) — case-class split — MAJOR.
- TT 2:2: dignity protocol — never call him עבד ("slave") in disgrace;
  brotherhood one-way asymmetric — ADD.
- TT 2:3: עבד עברי parsed "slave who IS a Hebrew" (not "slave OF a
  Hebrew") — construct-ambiguity resolved by gezerah shavah w/ Deut 15 —
  ADD.
- TT 2:5 (Kid 17a): runaway COMPLETES the term; sick STILL EXITS in yr 7
  — the two clauses = two constraint types (exact-count vs hard deadline)
  disambiguated by FAULT (Yer.: "in his control" vs not); sick >3 yrs
  completes (majority threshold, Rambam) — MAJOR ADD (timer semantics).
- TT 2:6: term passes to the SON as heir, not daughter/brothers —
  obligation-inheritance scope — ADD.
- TT 2:7 (Arakh 18b): the six years are מעת לעת ("time to time") —
  ANNIVERSARY CLOCK, not world calendar — per-contract clock — MAJOR ADD;
  + method note: words parsed across the pause-accent boundary (doubling
  service of a word to both clauses).
- TT 2:8 (Yer.Kid): exit at START of yr 7; LEAP-YEAR EDGE CASE — term
  ending in Adar I extends to end of Adar II (year boundary = Nisan) —
  calendar edge computed — MAJOR.
- TT 2:10: "seventh of the SALE, not of the WORLD" — shemittah does NOT
  free him (vs yovel which does) — TWO CLOCKS disambiguated — MAJOR.
- TT 2:11-12: חנם ("for nothing") = no document needed + ZERO exit cost —
  master's medical outlays non-recoverable — ADD.
21:3:
- TT 3:1 (Kid 20a): בגפו — Hebrew slave does NOT exit on limb-loss (vs
  Canaanite's tooth/eye exit); gets damages as free man — per-class exit
  conditions — MAJOR-ish ADD.
- TT 3:2: maidservant provision CONDITIONAL on his having wife+kids —
  rationale = anti-permanent-enslavement DESIGN (attachment-risk analysis
  of the lonely slave) — MAJOR ADD (mechanism-design rationale).
- TT 3:4 (Kid 22a): "his wife goes out with him — was SHE sold?!" ->
  master owes her MAINTENANCE — absurdity-detection derives an obligation
  — MAJOR.
- TT 3:5: אשתו עמו two word-filters — אשתו excludes levirate-widow, עמו
  excludes betrothed — word-level scope filters — MAJOR method.
21:4:
- TT 4:1: אם ("if") = OPTION not duty, proven from the אם of v.3 —
  local mood-consistency rule (the LET? mood question, law-side) — ADD.
- TT 4:4: the given wife = Canaanite, back-derived from v.4's consequence
  clause (Israelite children could never be master's) — ADD.
- TT 4:5-9 (Yev/Kid): האשה וילדיה תהיה לאדוניה ("the woman and her
  children are her master's") = MATRILINEAL DESCENT RULE -> cascade: no
  levirate bond via slave-brother; no incest liability via slave-mother
  line; no terumah-disqualifying "seed"; R. Tarfon's MAMZER-PURIFICATION
  ALGORITHM (mamzer + slavewoman -> child is slave -> manumit -> FREE
  CLEAN LINEAGE) — an intentional lawful exploit through the descent rule
  — MAJOR MAJOR (one clause powers a family-status computation system).
- TT 4:10: וילדיה includes tumtum/androginos — "children" sex-neutral
  where "son/daughter" is not — type-inclusiveness — ADD.
21:5:
- TT 5:1 (Kid 22a): אמר יאמר doubling = DECLARE TWICE — start of six AND
  within the last שוה פרוטה (perutah's-worth) of service — two-timepoint
  protocol with value threshold — MAJOR (doubling = literal repetition
  count here; contrast gen_08 mot-tamut semantics fork — doubling
  operator is CONTEXT-TYPED).
- TT 5:2: העבד excludes the maidservant from piercing — ADD.
- TT 5:4: declaration content = PRECONDITION CHECKLIST — "my master, my
  wife, my children" each must EXIST or no piercing — quoted speech as
  existence-checked parameter list — MAJOR.
21:6:
- TT 6:1: אל האלהים = TO THE JUDGES (his sellers) — the elohim token
  overloaded (God/judges), chain rules judges here — MAJOR (registry).
- TT 6:2: door must be STANDING (witnesses stand — Deut 19:17 join);
  Onkelos או-as-אם text note; Yer. alt rationale: public shaming — ADD.
- TT 6:3 (Kid 22b): WHY door+doorpost: THEY WERE THE WITNESSES IN EGYPT
  (Passover blood, Exod 12) when God said "My slaves — not slaves of
  slaves"; he bought himself a master -> pierced BEFORE THEM — instrument
  selection by WITNESS-HISTORY; cross-book join to Exod 12 — MAJOR MAJOR.
- TT 6:4: piercing = penalty + continuation, not fresh acquisition
  (Rambam's wording analyzed) — ADD.
- TT 6:5 (Yer.): אדוניו — the master PERSONALLY, no agent — pronoun
  emphasis = NO-DELEGATION operator (family: chalitzah, sotah, semikhah)
  — MAJOR method.
- TT 6:6: self-seller never pierced (אזנו "his ear" — of the court-sold)
  — CONFIRM class-split.
- TT 6:7: WHICH ear -> RIGHT, by gezerah shavah from the leper's rite —
  parameter filled by cross-procedure analogy — ADD.
- TT 6:9 (Kid 22b + Mekhilta + Yer.): why the EAR: the organ that HEARD
  at Sinai ("My slaves" / "do not steal" / Yer.: "no other gods") and
  violated what it received — organ selected by INFORMATION-HISTORY; TT
  prefers Yerushalmi's version on source-critical grounds (Israel heard
  only the first two utterances directly!); Tosafot: מרצע ("awl")
  gematria 400 = the 400 Egypt years — MAJOR.
SCOPE NOTES: none new; 0 UNRULED at census. Ledger: 52 read, 1,884 readable
remain.

### Batch 2 digest (TT 21:6:10 - 21:11:5 + 21:26:5 — 34 listings; TT LAYER DONE)
21:6 tail:
- TT 6:11: מרצע ("awl") must be METAL (Rabbi vs R. Yose any-material;
  halakhah = Rabbi) — instrument parameter spec — ADD.
- TT 6:12 (Kid 15a): ועבדו לעולם ("he shall serve him FOREVER") — לעולם =
  "the era of the JUBILEE": forever compiles to BOUNDED-BY-YOVEL — MAJOR;
  plus ועבדו = him alone: pierced-term does NOT pass to heirs (inverse of
  the six-year term which passes to the SON — contrast pair!); love-was-
  person-specific rationale; two-verse redundancy-justification method.
21:7 (amah entry):
- TT 7:1 (Kid 20a): "better sell your daughter than borrow at interest" —
  her term MONOTONICALLY DECREASES (deduct-and-exit) vs interest GROWS —
  comparative finance-semantics of two debt instruments — ADD.
- TT 7:2/7:5: father sells daughter (not mother, not son) — the sale-right
  rides the RIGHTS-BUNDLE (vows, earnings) — coherence rule — ADD.
- TT 7:4 (Arakh 29b): entry bounded by exit via KAL VACHOMER — if the
  already-sold exits at puberty-signs, the unsold can't newly enter —
  exit-rule constrains entry-rule — MAJOR method.
- TT 7:6: לאמה hekesh -> daughter's earnings to father (naarah scope) — ADD.
- TT 7:7: לאמה = sellable to PASULIM (marriage-ineligible) for service
  only — ADD.
- TT 7:8 (Kid 16a): לא תצא כצאת העבדים — NOT the Canaanite tooth/eye exit
  (gets damages instead) BUT acquired by DOCUMENT like slaves; kinyan
  type-hierarchy (Canaanite≡land: cash/doc/chazakah; אותם excludes Hebrews
  from chazakah); + Mahari Bruna RESPONSUM applying the verse to a Jewish
  housemaid (serves inside, not sent out) — LIVE MEDIEVAL CASE LAW — MAJOR.
21:8 (redemption):
- TT 8:3: no designating TWO at once — mapik-heh (singular "her") + no-
  bundling-of-mitzvot principle — anti-batching rule — ADD.
- TT 8:4 (Bekh 13a): verse ORDER = PRIORITY: designation precedes
  redemption — sequence encodes preference — ADD.
- TT 8:5-6 (Kid 14b): והפדה = GRADUATED REDEMPTION — price prorated by
  years served (amortization), master OBLIGATED to cooperate; proves
  cash-acquisition (TT AUDITS Rashi's proof and rebuilds it — the
  compiler auditing its own derivation); extended to male slave by the
  עברי/עבריה analogy; two-perutot minimum edge — MAJOR.
- TT 8:7: לעם נכרי ("to a foreign people") = NO-TRANSFER rule; Onkelos
  לגבר אוחרן ("to another man") -> Rambam: master may not resell/transfer
  AT ALL; Gra variant: warning to the FATHER (idolater) — live fork on
  the addressee — MAJOR + dual-track candidate.
- TT 8:8 (Kid 18b): בבגדו בה — garment-spread (marriage) = ONE-WAY DOOR:
  after designation, father can never re-sell — absorbing state — MAJOR.
21:9:
- TT 9:1 (Yer.): designation to SON not BROTHER — delegation follows the
  INHERITANCE line, not the levirate line — ADD.
- TT 9:2: כמשפט הבנות ("per the law of the daughters") — "came to teach,
  ended up learning": the referenced daughters'-law ISN'T WRITTEN
  anywhere — a FORWARD-REFERENCE TO UNWRITTEN LAW; the chain derives the
  general husband's-duties FROM this pointer — MAJOR MAJOR (the written
  text cites the oral spec's existence!).
21:10:
- TT 10:1-2: STANDARD MARRIAGE ACQUISITION (document — Kid 16a; cash —
  Yer.) derived BY ANALOGY FROM THE AMAH LAWS — kiddushin's mechanics
  bootstrapped from the slave block — MAJOR.
- TT 10:3: marry-off-minor-son — Mekhilta pro vs Bavli San 76b contra —
  TT flags the intra-chain contradiction — divergence-candidate.
- TT 10:4 (Ket 47b): שארה כסותה ועונתה = food / clothing / conjugal-time
  — the three-field obligation record, with root-analysis of ענה (time-
  root; withholding = affliction, Yoma join; per-profession timing table
  Ket 61b) — MAJOR.
- TT 10:5 (Ket 48a): clothing CONTEXT-INDEXED — per her age, per season
  (new in winter...) — obligation with runtime parameters — MAJOR.
- TT 10:6 (Ned 15b): vow-vs-duty interface — "konam my use of you" VOID
  against this verse's lien (duty defeats private speech-act; phrased as
  her-benefit can bind) — joins the Num 30 block — MAJOR.
- TT 10:7: לא יגרע subject fork (bat-Yisrael vs amah; R. Yonatan / R.
  Yoshiyah) — recorded fork — ADD.
21:11 (exit):
- TT 11:1: "these THREE" referent resolved = designation/son-designation/
  redemption (NOT the three duties); Gra text variant — pointer
  disambiguation between candidate triples — MAJOR.
- TT 11:2 (Ket 46b): אין כסף ("no money") — "none for THIS master, but
  there IS for ANOTHER — the father": kiddushin-money right derived from
  NEGATION SCOPE (implied complement) — MAJOR method.
- TT 11:3 (Kid 4a): the double phrase = TWO exit-times (naarut, bagrut)
  INCLUDING the aylonit edge (no-naarut path) — degenerate-case coverage
  — MAJOR.
- TT 11:5 + 21:26:5: exit needs a DOCUMENT where designated (get) /
  manumission-doc (שילוח gezerah shavah w/ divorce) — TT audits Rashi
  again — ADD.
PACE: bite 2 = 34 listings / 20k chars. Ledger 86 read; 1,850 readable
remain. TT map layer COMPLETE. Next stratum: Mekhilta (both, 38 rows).

### Batch 3 digest (TT Lev 25:13 + Mekhilta DeRabbi Shimon 21:1-11 FULL +
### MdRY Nezikin 1:1,1:2,1:7 — 15 listings)
- TT Lev 25:13 (Kid 20a): THE FALL-CASCADE — shemittah-produce trading ->
  sells movables -> fields -> house -> DAUGHTER (21:7!) -> interest ->
  self -> gentile -> idolatry-service: our verse = STAGE 4 of a canonical
  degradation state machine rooted in denying God's land-ownership; the
  habituation mechanism ("repeated sin becomes as permitted") named —
  MAJOR (block 1 <-> block 7 Lev 25 linked as one cascade).
MdRS 21:1 (header):
- R. Yehudah: mishpatim at MARAH, repeated at Sinai; R. Yishmael's rule
  FORMALIZED: אלה = break, ואלה = APPEND (w/ Malachi+Nehemiah proofs) —
  CONFIRM+ (both Mekhiltas).
- R. Akiva: TRANSMISSION PROTOCOL from verb distribution — teach ->
  repeat (2nd/3rd/4th) -> ordered-in-the-mouth (שימה בפיהם) -> SHOW THE
  REASONING ("set table", אתה הראת לדעת join) — the relay spec — MAJOR.
- לפניהם = "the INNER ones": no teaching monetary law to the unqualified
  — ACCESS CONTROL on the legal source — ADD.
- R. Yishmael: THE COMPLETE 13 MIDDOT LISTED HERE — the hermeneutical
  INSTRUCTION SET attached to THIS verse as what Moses received at Sinai
  ("which you shall place before them" = the derivation rules
  themselves) — MAJOR MAJOR MAJOR (the law-code header carries the ISA;
  ties to the owner's Formula Census doc-39 list #2).
MdRS 21:2:
- Dorshei reshumot: the slave-term as NATIONAL PROPHECY — serve no more
  than SIX KINGDOMS (Babylon/Media/Persia/Greece/Assyria/Rome), "in the
  seventh free FOR NOTHING" (grace); בגפו = eagle-wings (Lam 4:19) —
  the law doubles as the exile-arc schema — MAJOR (corpus-world; joins
  gen_08's exile-allegory of the rivers).
- BOTH entry paths in one clause — "the text speaks CONDENSED LANGUAGE"
  (לשון קצרה) — the chain NAMES the compression operator — MAJOR method.
- עברי etymology fork: Eber / Abraham beyond-the-river / Hebrew LANGUAGE
  kept in Egypt — registry attribute — ADD.
- Job-content limits: master may NOT hire out his craft / impose public
  bathhouse/barber/baker/money-changer duty unless his prior trade; R.
  Yose: no NEW trade at all — occupational scope-of-service — MAJOR ADD.
- Sick-in-bed time COUNTS toward the term (עולה לו מן המנין) — CONFIRM
  w/ mechanism.
- Exit at START of yr 7 via COMPETING-ANALOGY ADJUDICATION (yovel-start
  vs debt-release-end; resolved by shared-dependency + ת"ל) — the
  dialectic shown in full — MAJOR method.
- צא speech-act: master must SAY "go out" but exit not conditional on it
  — required-not-constitutive — ADD.
- חנם: no doc, no sick-cost recovery, BUT severance grant (הענק תענק)
  STILL DUE — zero-cost exit keeps the mandatory parting package — ADD.
- The five-exit summary table (years/yovel/deduction/document/master's-
  death-no-son) + two acquisitions (cash/doc) stated as מכאן אמרו — the
  Mishnah's table shown AS OUTPUT of this derivation — MAJOR.
MdRS 21:3:
- בגפו mood-check: "could it be a DECREE (stay single)? ת"ל אם — only
  permission" — the אם mood operator applied — CONFIRM.
- Full RIGHTS MATRIX: maintenance covers pre-purchase wife AND post-
  purchase wife taken with master's consent (הוא = מדעת רבו); excludes
  betrothed/levirate-widow/INVALID unions ("fit to stand with him");
  master owns HIS labor only — NOT wife/children's earnings; slave keeps
  own finds+inheritance (ועבדך "only work"); husband-rights RESTORED via
  middah #10 (החזירו הכתוב לכללו בפירוש) — one of the 13 rules APPLIED
  on-page — MAJOR.
- Family-unity directive: don't separate from wife (here) / children
  (Lev) — ADD.
MdRS 21:4:
- Master MAY COMPEL the union (כופה אותו) — even a KOHEN slave despite
  the zonah-ban — servitude provision vs personal-status restriction —
  MAJOR (flag for careful encoding; dual-track w/ TT's Kid 22a reading).
- One wife not two; never one-to-two (vs Canaanite slaves where allowed)
  — class dignity boundary — ADD.
- She exits WITHOUT document; master may sell her+children over the
  slave's objection — CONFIRM/ADD.
MdRS 21:5:
- "Until he says AND REPEATS AND TRIPLES" — THREE declarations variant
  (vs Bavli's two) — intra-chain fork on the repetition count — fork.
- Amah: no piercing BUT severance-grant yes — per-provision scoping —
  ADD.
- BILATERAL LOVE PRECONDITION: he loves master AND master loves him
  (כי אהבך); household asymmetry blocks (he has family, master none ->
  no piercing); either party SICK -> no piercing (כי טוב לו עמך — the
  good must be actual and mutual) — the rite's precondition is a
  VERIFIED RELATIONSHIP STATE — MAJOR.
MdRS 21:6:
- Door not doorpost: the kal vachomer FOR doorpost (it has the mezuzah-
  mitzvah!) BLOCKED by explicit ונתת באזנו ובדלת — A-FORTIORI DEFEATED
  BY TEXT = operator precedence — ADD/method.
- ורצע אדוניו: "RIBUI AFTER RIBUI = MIUT" (inclusion-doubling excludes)
  — master not son/slave/agent — no-delegation CONFIRMED via a different
  formal route than TT (meta-rule vs pronoun-emphasis) — derivation
  diversity noted.
- Right ear, UPPER part; the kohen-blemish debate: pierce the lobe lest
  a kohen-slave be DISQUALIFIED from service by the wound vs "a kohen is
  never pierced" — rite-vs-priestly-status interaction — MAJOR ADD.
- ועבדו לעולם: full INFERENCE LATTICE — competing a-fortioris on
  piercing-for-the-son BOTH blocked (והיה לך "yours, not the son's");
  yovel frees the pierced (ושבתם); לעולם = the pierced one's own era
  (even 30-40 yrs); עולם/עולם gezerah shavah syncing Exod<->Deut —
  derivation-graph gold — MAJOR.
MdRS 21:7:
- Woman never sold for her own OR her father's theft (כי יגנב איש —
  gendered, personal) — entry paths bounded — ADD.
- Sale only while MINOR; father must be DESTITUTE ("found nothing to
  eat" — Rambam's rule sourced here); only to a marriage-possible buyer
  (kiddushin must be able to hold) — THE SALE IS MARRIAGE-TRACK BY
  DESIGN — MAJOR.
MdRS 21:8:
- בעיני ("in the eyes of") = SUBJECTIVITY operator — "bad" even if
  beautiful; son's eyes count; R. Eliezer adds pesulim — ADD.
- מכלל לאו הין — negation implies permission (named operator) — ADD.
- CONSENT IN MARRIAGE derived HERE: designation requires HER consent
  (מדעתה), generalized by kal vachomer to ALL WOMEN ("if the subjugated
  amah needs consent — free women all the more") + the procedure (two
  witnesses, purchase-money CONVERTS to kiddushin-money) — MAJOR MAJOR.
- Court may redeem her AGAINST THE MASTER'S WILL (בעל כרחו) —
  compulsory-redemption power — MAJOR-ish ADD.
- Designation right EXPIRES with the term (only within six yrs, even at
  the last perutah; after six — none) — ADD.
- The no-alienation clause EXHAUSTIVE: no sale, no GIFT (לא ימשול), not
  to relatives; both words proven necessary (non-redundancy); extended
  to the male slave by kal vachomer; attempted sale VOID but not
  lashable — void-not-punishable classification — MAJOR.
MdRS 21:9:
- Son-designation only IN THE FATHER'S LIFETIME — the right dies with
  him — ADD.
- כמשפט הבנות BIDIRECTIONAL: amah teaches all daughters (duties not
  withheld) AND daughter-law teaches the designated amah (capital
  liability for adultery; exit only by divorce-doc) — mutual spec-
  inheritance — MAJOR.
MdRS 21:10:
- לא יגרע typed as a LO TAASEH (negative commandment class) — ADD.
- THE PROFESSION-INDEXED CONJUGAL TIMETABLE in the tannaitic layer
  (leisure/craft/donkey/camel/sailor/scholar) — the runtime table is
  Mekhilta-level, not just Mishnah — MAJOR.
- "She ASCENDS with him and does not descend" (עולה ואינה יורדת) —
  living-standard RATCHET (monotonic non-decrease) — MAJOR ADD.
MdRS 21:11:
- שלש אלה fork is tannaitic BOTH ways: R. Eliezer = the three duties;
  R. Akiva = designation/son/redemption — fork-confirm (TT chose Akiva).
- "The amah EXCEEDS the slave: exits by signs" — delta-table stated —
  CONFIRM.
MdRY Nezikin 1:1-2, 1:7: append-rule; pedagogy ladder; court-sold
subject serving "him and the son" — CONFIRM (canonical recension).
PACE: bite 3 = 15 listings / 20.4k chars. Ledger 101 read; 1,835 remain.
Next: MdRY Nezikin continues (~24 rows).

### Batch 4 digest (MdRY Nezikin rest + Sifra Behar + Sifrei Bamidbar 2:1 +
### Sifrei Devarim 118-122 + Bartenura/Mishnah opens — 63 listings)
MdRY (canonical Mekhilta):
- 1:18/2:1: אם-mood rule applied SYMMETRICALLY (v.4's permission proven
  from v.3's אם) — R. Yishmael's mood-consistency — CONFIRM.
- 1:20 + 2:17: the ELIMINATION DIALECTIC form (לשון ראשון/אחרון): candidate
  readings weighed, one blocked by cross-text, "you must say like the
  first" — reading-selection procedure shown twice — method.
- 2:9: sick counts, runaway doesn't — the operative test NAMED: ראוי
  לעבד ("fit to serve") — CONFIRM w/ criterion.
- 2:10: TWO declarations (vs MdRS THREE) — recension fork explicit.
- 3:7: KIDDUSHIN BOOTSTRAP in canonical Mekhilta — father's kiddushin
  right (a-fortiori from sale); CASH from Canaanite-shefachah kal
  vachomer; DOCUMENT from Deut 24:2 והלכה והיתה — DIVORCE TEACHES
  MARRIAGE (departure≈becoming hekesh); R. Akiva: cash from OUR אם אחרת
  — multi-derivation recorded — MAJOR.
- 3:8: R. Yose HaGlili's TRANSITION MATRIX — kiddushin-after-kiddushin
  OK, kiddushin-after-amahood OK, amahood-after-kiddushin NEVER,
  amahood-after-amahood never — monotone-upward state ordering (the
  one-way door generalized) — MAJOR.
- 3:16: בבגדו בה third reading — BETRAYAL (bagad=deceit, Malachi/Jer
  proofs): because he betrayed her he may not keep her — fork now
  garment/betrayal dual-track — ADD.
- 5:23, 11:1, 13:9 (cross-block): curser-of-parents gender-inclusive;
  goring covers minors/tumtum/gerim (via כמשפט הזה); thief-sale bounded
  to six by OUR 21:2 — blocks 2/3/4 joins ledgered — ADD.
Sifra Behar (self-seller regime):
- 7:1: self-sale ONLY if destitute — and NOT to fill his purse / buy
  beast / tools / house — illegitimate-purpose list enumerated — MAJOR.
- 7:3: THE PARITY SPEC (כי טוב לו עמך): "WITH YOU in food, drink, clean
  clothing — not fine bread for you and coarse for him, old wine/new
  wine, cushions/straw"; same-day wage; same-locality rule (ויצא מעמך —
  not you in village, he in city); craft-protection w/ R. Yose's prior-
  trade exception; wife+children maintenance w/ master-consent condition
  — "עמך" as an EQUALITY OPERATOR — MAJOR.
Sifrei Bamidbar 2:1:
- THE DIFF-ONLY RESTATEMENT RULE stated as a named מדה: "any passage
  stated once with an element missing and restated elsewhere — restated
  ONLY for the missing element" — incremental-patch semantics of
  repeated passages + R. Akiva: every לאמר demands exposition — MAJOR
  MAJOR (machine-grade: re-statements are deltas).
Sifrei Devarim 118-122:
- 118:7: sick idle-time NOT recoverable — חנם shields the slave — CONFIRM+.
- 121:3: bilateral love + household symmetry (כי אהבך ואת ביתך) — 2nd
  witness — CONFIRM.
- 122:1: ⚠ R. YISHMAEL'S THREE OVERRIDES — "in three places the
  HALAKHAH BYPASSES (עוקפת) THE SCRIPTURE: dust->anything that grows
  plants; sefer->anything detached; AWL->anything" — the oral layer's
  documented override authority, with its 3-item registry, ONE OF THEM
  OUR VERSE — MAJOR MAJOR MAJOR.
- 122:4: במרצע = "anything that MARKS" — parameter relaxation — ADD.
- 122:8: עולם = the MASTER's lifetime (recension variant vs MdRS) both
  yovel-bounded; pierced serves neither son nor daughter — CONFIRM+var.
- 213:8: captive-wife rights via our three-duties clause — Deut 21 join.
Mishnah/Bartenura opens:
- M.Eduyot 4:10 / Ketubot 5:6: conjugal-vow TOLERANCE WINDOW quantified
  — Beit Shammai 2 weeks / Beit Hillel 1 — house-fork on the breach
  threshold before forced divorce; timetable Mishnah (Ket 5:6) matches
  Mekhilta's — CONFIRM.
- M.Ketubot 4:4 + Bartenura: father's rights list (kiddushin-money from
  אין כסף; earnings from לאמה hekesh) — CONFIRM (mishnaic layer).
- Bartenura Kid 1:2: the amortization ARITHMETIC example (six manim /
  six years = one maneh per year deduction); master's-death table
  (pierced freed at death; regular serves SON only, not daughter/
  brother); amah freed at master's death like the pierced (ואף לאמתך) —
  CONFIRM.
- Bartenura Kid 3:12 / Yev 2:5: descent-rule PAIR completed — shefachah
  matrilineal from our verse + NOKHRIT matrilineal from Deut 7 כי יסיר
  — the two-source matrilineal system — MAJOR.
- M.Bekhorot 1:7: THE PRIORITY-LIST MISHNAH — designation > redemption
  (our verse cited), redemption > neck-breaking, yibbum > chalitzah
  ORIGINALLY then REVERSED "now that intent is not for the mitzvah" —
  DOCUMENTED RUNTIME RE-PRIORITIZATION keyed to population intent-
  quality — MAJOR.
- M.Ketubot 3:2: NO-DOUBLE-LIABILITY (capital absorbs monetary — כל
  המתחייב בנפשו אין משלם ממון) rooted at 21:22 ולא יהיה אסון — block 2
  preview — MAJOR.
- Melekhet Shelomoh Yev 11:7: hit/curse hekesh ACROSS an intervening
  verse (noted explicitly) — long-range adjacency — ADD.
PACE: bite 4 = 63 listings / 20.2k chars. Ledger 164 read (8.4%); 1,772
remain. Midrash-halakhah stratum ~done; Mishnah/Tosefta next, then
Kiddushin (Bavli, 56 rows).

### Batch 5 digest (Mishnah rest + Tosefta + Yerushalmi Kiddushin opens +
### 2 apparatus rows — 30 listings)
Mishnah:
- M.Ket 5:7: THE REBELLION PENALTY SCHEDULE — moredet loses 7 dinars/WEEK
  off her ketubah (R. Yose: decreases indefinitely, collectible from
  future inheritance — negative balance allowed); rebellious HUSBAND
  pays +3/week INTO it — asymmetric weekly accrual rates on the 21:10
  duties — MAJOR.
- M.Ket 7:1: vow-off-benefit GRACE PERIOD — ≤30 days he must appoint a
  maintenance AGENT (parnas), beyond -> divorce+ketubah; parameterized
  by class (Israelite 1mo, priestly wife 2 — she can't return to him) —
  delegation workaround with class-indexed windows — MAJOR.
- M.Kid 3:12: THE FOUR-CASE DESCENT ALGORITHM — (a) valid kiddushin, no
  sin -> follows FATHER; (b) valid + sin -> follows the DEFECTIVE parent;
  (c) invalid with him, valid with others -> MAMZER; (d) invalid with all
  -> follows MOTHER (shefachah from OUR verse / nokhrit) — the complete
  lineage-assignment function; our clause powers branch (d) — MAJOR MAJOR.
- M.Niddah 6:11: TWO HAIRS = the maturity signal spec (the אין כסף exit
  trigger): all-mitzvot onset, chalitzah/yibbum, ben-sorer window (two
  hairs -> beard-circle, ~3 months), no more refusal-right; "the sages
  spoke in clean language" euphemism note — the signal defined — ADD.
- Rambam Intro 15:11: THE MISHNAH'S SIX-ORDER ARCHITECTURE follows OUR
  CHAPTER's verse order — Nashim before Nezikin because daughter-sale
  (21:7) precedes the pregnant-woman fight (21:22) precedes the goring
  ox (21:28) — the codebase directory structure mirrors this block —
  MAJOR.
- TosYT BB 8:1: the FIELD-NAME PERMUTATION fork — which word (שאר/עונה)
  maps to which duty (food/conjugal/closeness) — tannaitic assignment
  dispute over the record's field names — ADD.
- TosYT Kid 1:1: kiddushin-cash directionality — כי יקח (HE takes; she
  cannot initiate the formula) + ויצאה חנם (father's money) both needed;
  קיחה קיחה gezerah shavah to Abraham's FIELD PURCHASE (Efron join) —
  CONFIRM+.
- TosYT Kid 1:7: women's-equality TRIPLE-SOURCE necessity — each of the
  three verses blocks a different narrow rationale (atonement-only /
  livelihood-only / life-only) — redundancy-elimination method — MAJOR.
- TosYT San 7:4 + 8:1: Mishnah-list ordering rationale vs Torah order
  (המכשף deferral); ben-sorer ≤3-month window (pregnancy-recognition
  bound); our איש usage cited — ADD (compiler-ordering analyses).
Tosefta:
- Tos.Arakhin 5:4: the fall-cascade, Tosefta recension (ends: becomes a
  komer of idolatry) — CONFIRM (3rd witness).
- Tos.BK 7:2 (+Lieberman): RYbZ's chomer-set — the ear "that did not
  KEEP what it HEARD" (relay-failure verb!); the LUCHOT-AS-KETUBAH
  parable: first tablets = God's own writing (King writes the document),
  second = Moses' (her copy after the sin); exile-to-Babylon = sent back
  to father's house — covenant-as-marriage-document jurisprudence —
  MAJOR.
- Tos.Parah 1:5: the CLOCK-TYPE REGISTRY — walled-city year, ancestral-
  field years, THE SLAVE'S SIX, child-age years: all מיום ליום
  (anniversary clocks) — cross-domain table — CONFIRM+.
- Tos.Sotah 2:8: the MALE/FEMALE ASYMMETRY TABLE — man sold AND re-sold,
  woman never; man pierced/self-sells, woman not; woman may not ACQUIRE
  a male Hebrew slave — complete gender difference-table — MAJOR.
Yerushalmi Kiddushin:
- 1:1:19: BEIT SHAMMAI vs BEIT HILLEL minimum-kiddushin (dinar vs
  perutah) BOTH derived from OUR AMORTIZATION CURVE — BS reads the START
  of her sale, BH reads the END of her deduction (last perutah) — the
  two houses sampling the same function at opposite endpoints; R. Bun's
  boundary argument (year-six start is already perutah-scale) — MAJOR
  MAJOR.
- 1:1:33: 21:8 SUBJECT FORK — R. Akiva: half-shefachah-half-free
  betrothed to a free man; R. Yishmael: Canaanite shefachah married to
  the slave — new fork on who the verse's woman IS — fork.
- 1:2:2: THE DERIVATION-DEPTH META-RULE (למד מן הלמד) — amah learns
  from free-woman, slave learns from amah = "the learner became a
  teacher": R. Akiva permits CHAINED INFERENCE, R. Yishmael forbids it
  and needs a direct gezerah shavah route (שילוח/מכירה) with objection-
  repair (to-herself vs to-others) — a formal constraint on inference-
  graph depth, disputed by school — MAJOR MAJOR.
- 1:2:6: start-of-seven w/ the SWAP OBJECTION ("say it's reversed!")
  answered from the doubled ובשביעית spelling; yovel-in-the-week
  calendar question; Caesarea: "the seventh frees SLAVES, yovel frees
  the PIERCED" — division of labor between clocks — CONFIRM+.
Apparatus (sorted in):
- Ben Yehoyada Kid 22b: אוזן-דלת-מזוזה initials = אדם ("human") — the
  rite's instruments spell the title he forfeited; divine-name filling
  = 45 = אדם — ADD (registry poetry).
- Chidushei Agadot Kid 20a: Maharsha's POSITION-AS-SEQUENCE argument —
  daughter-sale's placement in Mishpatim (not after the interest
  passage) proves the cascade's order — ADD.
PACE: bite 5 = 30 listings / 20.6k chars. Ledger 194 read (9.9%); 1,742
remain. Next: Yerushalmi Kiddushin continues, then Bavli Kiddushin (56).

### Batch 6 digest (Yer.Kid 1:2:7-3:12 + Bavli Kiddushin 3b-69a opens +
### Penei Yehoshua/Ran/Rashba — 74 listings)
Yerushalmi:
- 1:2:7: COMPOSITE FAULT-SEQUENCING — fled-then-sick: completes ("had
  you been with me you'd not have fallen ill"); sick-then-fled: also
  completes ("had you stayed you'd have healed quickly") — BUT-FOR
  COUNTERFACTUAL reasoning deciding mixed sequences; moredet-during-
  niddah analogy (rebellion pre-dated the disability) — MAJOR.
- 1:2:13: two-exit-phrase necessity (Yer. version); R. Tanchuma's
  COMPLEMENTARITY rule: "wherever the father has money-rights the
  master has none" — authority partition — CONFIRM+.
- 1:2:14: DESIGNATION DEADLINE — R. Yose bR Yehudah: enough day left
  for redemption + earnings ≥ perutah + deduction ≥ perutah; rabbis:
  until sunset; at the boundary R. Zeira: he designates BY WORDS ALONE
  (מייעדה בדברים) — the money-conversion degrades gracefully to a pure
  speech-act — MAJOR.
- 1:2:20 + Bavli 19a: minor-son designation fork (R. Yochanan any son /
  Resh Lakish adult+aware; בנו כל דהו vs בנו דומיא דידיה) — fork.
- 1:2:25: ⚠ THE ANTI-OVERRIDE RULE — sale "on condition of no
  designation": rabbis VOID it — "one who stipulates against what is
  written in the Torah, the condition is void"; R. Meir validates
  (fulfillable-at-end principle); THE WAIVABILITY TYPOLOGY: money-rights
  (food/clothing) waivable, BODY-rights (עונה) not (תניי גוף) — private
  contract cannot patch statute; field-level waivability flags — MAJOR
  MAJOR.
- 1:2:26: RShbY: בבגדו בה = "he may betray her ONCE, not twice" — a
  BETRAYAL BUDGET (counter) vs rabbis' absorbing-state reading — fork.
- 1:2:27: marriage-frees-amah kal vachomer met by R. Yochanan's "I have
  only the Mishnah" — CANON-CLOSURE against valid inference — MAJOR
  method; Bar Pedaya: freed at master's death (nirtza hekesh); one
  tanna: amah serves the DAUGHTER not son (gender-mirrored heir-service)
  — fork-table.
- 1:2:28: TWO-DOORS ALLOCATION — court-sold brought אל האלהים (judges),
  SELF-sold brought אל הדלת (the door) — the verse's two clauses split
  across the two entry-paths; night-service lawfulness solved via the
  shefachah mechanism; kohen-buyer question + retraction — ADD/MAJOR.
- 1:2:29-30: kohen-piercing (cartilage vs lobe; vetch-size blemish
  threshold; ושב לאחוזתו "intact to his estate"); ⚠ THE OVERRIDE
  REGISTRY, YER. RECENSION: "in three places the halakhah bypasses the
  MIKRA and in ONE place the MIDRASH" — 4th entry: leper's shaving,
  where halakhah ("shave him like a GOURD") overrides the KLAL-U-FRAT-
  U-KLAL OUTPUT — the oral layer overrides even derivation-rule results
  — MAJOR MAJOR; instrument forks (Rabbi: the great drill; the chisel).
- 1:2:32: piercing preconditions + NEW ONE: "until the property has been
  BLESSED through him" (עד שיתברכו הנכסים על ידיו, from כי טוב לו עמך)
  — a measurable prosperity-attribution check — MAJOR ADD.
- 2:1:4: THE AGENCY BATTLEFIELD — our ורצע miut ("his master, not his
  agent") read as an EXCEPTION proving the general agent=principal rule;
  but one tanna: ורצע INCLUDES the agent; R. Yishmael: "אדוניו = anyone
  acting on the master's behalf" — the שליחות meta-theory contested ON
  OUR VERSE — MAJOR.
- 3:1:8: delayed-acquisition purchase — FOUR tannaitic permutations of
  the day-or-two liability (21:21) between seller/buyer (כספו vs died-
  under-his-hand criteria) — block 2 fork ledgered — ADD.
Bavli Kiddushin (mother-sugya, first pass):
- 4a:16 (Abaye): REDUNDANCY-TOLERANCE PRINCIPLE — "a matter derivable
  by kal vachomer — the text TROUBLES ITSELF and writes it anyway"
  (מילתא דאתיא בק"ו טרח וכתב לה קרא) — counterweight to the yitur
  principle; explicit text may lawfully duplicate derivable rules —
  MAJOR method.
- 6a + Ran 2a: THE BETROTHAL-FORMULA LEXICON — the uncertain formulas
  incl. מיועדת לי ("my designated one" — from OUR אשר לא יעדה!) and
  עזרתי/נגדתי/סגורתי/צלעתי — from GEN 2:18-21 (gen_08's vocabulary!);
  לקוחתי resolved valid from כי יקח — Eden's registry + the amah's
  yiud as the legal formula-space of marriage — MAJOR (cross-block).
- 12a: SALE VALIDITY REQUIRES EXECUTABLE ESCAPE-CLAUSES — "wherever she
  cannot deduct/be designated, the sale is NO SALE" (לא הוו זבינא
  זביני) — transaction valid only with its exit-paths intact — MAJOR.
- 16a: derivation-allocation debates (Ulla's אחרת hekesh vs R. Acha's
  כצאת "acquired LIKE slaves"; שמע מינה תרתי — one clause, two rules) —
  CONFIRM.
- 17a: sick-time CAPACITY TEST — Rav Sheshet: sick counts when he can
  still do NEEDLE-WORK (מעשה מחט); sick-all-six completes — partial-
  capacity threshold — MAJOR.
- 18b: designation = BETROTHAL (eirusin) not marriage — INFERRED FROM
  THE RULE'S OWN STRUCTURE (were it marriage, father's resale-bar would
  be moot since his rights would already have ended) — institutional
  stage deduced from presupposed rights-transitions — MAJOR method.
- 19b: waivability fork Bavli version (R. Meir: void; R. Yehudah:
  money-conditions valid); Chizkiyah's לאמה "sometimes ONLY an amah"
  supporting the condition — CONFIRM.
- 22a: redundancy-analysis of the two-sayings rule vs the love-checklist
  (why need לא אצא when the checklist would fail?) — CONFIRM+.
- 22b: PIERCING GEOMETRY — the two verses collated: "bore through the
  ear until reaching the door" (דוקר והולך עד שמגיע אצל דלת) — physical
  procedure derived by verse-synthesis — ADD.
- 45a: R. Yose bR Yehudah — "the first monies were NOT given for
  kiddushin": the conversion-mechanism fork (does sale-money convert
  retroactively or is designation a new act?) — fork.
- 68b-69a: descent-rule edge case — "you are free, your child a slave":
  R. Yose HaGlili child-follows-her vs rabbis' words-stand (our verse);
  the maxim "a fetus in a shefachah's womb is like a fetus in an
  ANIMAL's womb" (conception-vs-birth status assignment) — MAJOR.
Rishonim on the sugya:
- Penei Yehoshua 16a: כצאת העבדים plural = BOTH slave-classes — the
  designated amah exits like NEITHER (not six/yovel/deduction, not
  tooth/eye) — the plural as two-class pointer; Rashbam peshat cited —
  ADD.
- Rashba 50a: coerced-consent doctrine — forced SALE valid (tliyuhu
  ve-zavin) but coerced GET in gentile courts invalid FROM OUR HEADER
  (לפניהם ולא לפני גוים) — the jurisdiction rule inside the coercion
  theory; mental-reservation (דברים שבלב) analysis — ADD.
PACE: bite 6 = 74 listings / 20.9k chars. Ledger 268 read (13.7%); 1,668
remain. Bavli Kiddushin partially read; remaining tractate rows + codes
next.

### Batch 7 digest (Rashi/Rashba/Tosafot on Kid + Arakhin + Yevamot +
### Ketubot + Bava Kamma strata — 64 listings)
Kiddushin apparatus:
- Rashba 68b: derivation-NECESSITY analysis — without our verse the
  shefachah's mitzvah-status would imply lineage (child follows father);
  the verse BLOCKS the default inference (fetus-like-animal rule) — why
  the rule needed writing — ADD.
- Tosafot 5a: kal-vachomer from amah BLOCKED by who-writes-the-
  instrument — the FATHER writes the amah's document (not the acquirer)
  so the husband-written kiddushin-document can't be derived from it —
  instrument-authorship as formal differentiator — ADD.
- Sha'arei Torat EY: the Yer. emendation — R. Yishmael's direct route =
  חפשי (21:2) <-> חופשה (Lev 19:20, the designated shefachah) gezerah
  shavah — ADD.
Arakhin:
- 18b: the מעת לעת clock-registry braita (Bavli home; adds the kodashim
  year) — CONFIRM.
- 30b: fall-cascade Bavli version ("PREFERABLE to sell one's daughter
  than borrow at interest") — CONFIRM (4th witness).
- 33a: R. Nachman b. Yitzchak — "SIX for the sold, SEVEN for the
  pierced": resolves Jeremiah 34's מקץ שבע שנים — the emancipation-
  covenant episode runs on OUR clocks; canon-history join (Zedekiah's
  violation = the law's enforcement event) — MAJOR-ish ADD.
Yevamot:
- 22b/23a/70a/78a: descent-rule's four applications; Rav Yosef's
  objection answered "there it is different — the VERSE said": the rule
  does NOT generalize beyond its domain — anti-generalization guard —
  CONFIRM+.
- Yer.Yev 12:2:6 + Rashi 104a: THE PARAMETER SERVER — the leper-rite
  verse is מופנה (fully free) and distributes RIGHT-side to three
  procedures: יד יד to the handful, רגל רגל to chalitzah, אזן אזן to
  OUR piercing — one free verse binding a parameter across three
  rituals; R. Eliezer's two-braita consistency problem — MAJOR.
- NY/Rashi 55a: Lev 19:20's shefachah charufah DEFINED by our 21:4
  provision (the one woman permitted to the Hebrew slave) — cross-block
  definition dependency — ADD.
- Ben Yehoyada 63b: Lurianic layer — ויצאה אשתו עמו as gilgul-return
  for the husband's sake; בגפו = ג' פ"ו (3×86, the katnut-names; גוף
  as soul-treasury) — kabbalah-track registry — ADD.
Ketubot:
- Yer.Ket 3:9 / Bavli 29a: R. MEIR'S DISJOINTNESS THEOREM — "wherever
  there is SALE there is no FINE; wherever FINE, no SALE" — minor/
  naarah/bogeret partition her timeline into mutually exclusive
  regimes — MAJOR.
- 40b/46b/47a: DOMAIN-CROSSING INFERENCE BARS — "money-law is not
  derived from prohibition-law; money-law is not derived from fine-law"
  (ממונא מאיסורא/מקנסא לא ילפינן) — normative domains walled; the
  מסתברא tiebreak (father controls her marriage — earnings follow);
  46b:10 "the miut excludes only a LIKE-KINDED exit" — typed exclusion
  scope — MAJOR method.
- Yer.Ket 5:7:5: the שאר/עונה PERMUTATION fork fully displayed (both
  assignments w/ prooftexts incl. the manna-join כעפר שאר) + each
  permutation RECOVERS the missing field by kal vachomer — error-
  correcting redundancy: the three-field record reconstructible from
  any two — MAJOR.
- Yer.Ket 5:8:2: the 7:3 PENALTY-RATE PROPORTIONALITY — she owes seven
  duty-categories, he owes three, rates match duty-counts (R. Yose bR
  Chanina); degradation cases (brought slaves -> owes nothing;
  stipulated away -> owes nothing); R. Yochanan's competing rationale
  ("the man's pain is greater", Samson proof) — MAJOR.
- Yer.Ket 6:1:3: finds-ownership rule GENERATED by the occupational-
  scope limit — Hebrew slaves/adult children keep their finds because
  the master "cannot re-task them" — job-scope limit as property-rights
  criterion — MAJOR-ish.
- Tosafot 2a: definite-article diction analysis (verse-anchored vs
  free-standing mishnah style) — compiler style-note — ADD.
Bava Kamma:
- Yer.BK 1:3:2: damage-assessment PROCEDURE from the header (court,
  land-assets default, witnesses, seizure exception; women via R.
  Yishmael's header rule) — CONFIRM+.
- Yer.BK 4:3:2: gentile-ox asymmetry — four rationales incl. R.
  Yochanan's כדיניהן ("BY THEIR OWN LAWS" — they lack tam/muad, so
  their system applies to them) — CONFLICT-OF-LAWS analysis — ADD
  (block 3).
- Yer.BK 4:5:2 + PY 54a + ChHaRim 86b: block 2-3 forks ledgered (נקי
  allocations; pit-exclusion selection problem; blind-man capacity-at-
  act vs capacity-at-trial) — ADD.
PACE: bite 7 = 64 listings / 22.1k chars. Ledger 332 read (16.9%); 1,604
remain.

### Batch 8 digest (BK/BM/BB/Gittin/Sotah/Makkot strata + apparatus — 24)
- Shita Mekubetzet BK 2a: FIVE THEORIES OF THE MISHNAH'S SORT KEY — why
  the four damage-categories are ordered as they are: source-order
  (Rashi; refined to "only the Nezikin-parshah items are order-bound"),
  frequency (R. Tam/Rashba), danger, doctrinal-dependency (the ox split
  into two passages TO teach bur's ransom-exemption — R. Yehonatan),
  comparison-structure (bur placed mid-list to serve the לא-הרי
  dialectic) — the apparatus debating the decompiler's ORDER-BY clause
  — MAJOR.
- Tosafot BK 15a: לפניהם carries THREE allocated functions (women-
  equality / not-gentiles-not-laymen / coercion-enforcement powers) —
  the conflict (women equal yet can't judge) resolved by anchor-
  analysis (the exclusion reading anchors to אלהים); Devorah explained
  by acceptance — ADD.
- Gittin 84b (R. Ada bR Ika): WAIVER REFINEMENT — the void-condition
  rule applies where HE uproots (obligor-imposed condition on שאר/
  כסות/עונה); where SHE uproots (right-holder's own waiver) — different
  analysis — who-waives distinguished from what-is-waived — MAJOR ADD.
- Ben Yehoyada BM 62a: THE עמך OPERATOR-OVERLOAD RESOLVED — וחי אחיך
  עמך = "your life FIRST" (canteen case) vs our כי טוב לו עמך = "the
  slave gets the only pillow" — reconciled by DOMAIN: life-vs-life
  favors self (pikuach nefesh), property/comfort may favor the other;
  + Alshich: the slave-privileges are a DESIGN FEATURE proving the
  acquisition is not true ownership — MAJOR.
- Petach Einayim BM 86a (Chida): THE AUTHORITY STACK — Rabbah bar
  Nachmani's death-scene (heavenly academy vs the Holy One on a
  leprosy-doubt; his "tahor, tahor" verdict); the doctrine assembled:
  49-faces-pure/49-impure given to the GENERATION'S MAJORITY, לא בשמים
  היא ("not in heaven") — even the Author's runtime ruling defers to
  the delegated interpreter majority; can-an-author-interpret-his-own-
  ruling debate (Maharam Mintz vs R. Yitzchaki) — MAJOR (the
  decentralized-authority doctrine in full apparatus).
- Rashbam BB 108b + Yad Ramah: inheritance-priority (son over brother)
  from OUR yiud + the dedicated-field rule — the yibbum counter-
  criterion dismantled as CIRCULAR ("is there yibbum where there's a
  son?!") — MAJOR-ish.
- Rashbam BB 109b: שארו = wife from Gen 2:24 one-flesh + our שארה —
  gen_08 join (Eden grounding the legal kinship term) — CONFIRM.
- Gittin 88b: THE RULE SELF-APPLIES — Abaye catches Rav Yosef coercing
  divorces: "but we are LAYMEN!" (our header's exclusion aimed at the
  amoraic court itself); resolved by agency-of-the-ordained — the
  runtime questioning its own authorization — MAJOR-ish ADD.
- Ben Yehoyada Sotah 2a: the Ari via SABA DEMISHPATIM (the Zohar
  treatise ON OUR PARSHAH = the soul-transmigration tract!): second-
  match difficulty = the same wife re-descending via ויצאה אשתו עמו —
  kabbalah track — ADD.
- Yer.Sotah 3:8:7: THEFT-INDIVIDUATION — sold for the PRINCIPAL only
  (בגניבו ולא בכפילו ולא בזמימו — never for penalty-multiples or
  false-witness liability); one theft: no resale, two thefts: resale;
  edge cases: partnership theft; serial nightly extraction split into
  two thefts by OWNERS' AWARENESS in between — the transaction-
  splitter criterion — MAJOR.
- Sotah 8a: the anti-batching list's Bavli home — no piercing two
  slaves at once (with sotah/leper/calf) — CONFIRM.
- Yer.Makkot 2:6:8: JOAB DEBUGGED — fled to the altar on a refuge-
  scope ERROR ("only the six cities refuge; not the altar"); R.
  Tanchuma: he fled to the SANHEDRIN (adjacent to the altar — our
  semikhut!); forum-selection for estate-planning (court-executed ->
  heirs inherit; king-executed -> crown confiscates) — a Kings
  narrative debugged via our block's institutions — MAJOR (corpus-
  world; Elijah-docket-adjacent material).
- Ben Yehoyada San 7b: the deliberation rule's parable (fast-vs-slow
  judge, the ring-deposit test, the varied retest exposing the
  guesser) — "do not ascend by steps" = your ignorance revealed on the
  same case varied — ADD.
PACE: bite 8 = 24 listings / 22.8k chars. Ledger 356 read (18.1%); 1,580
remain. Codes (Rambam/Chinukh/Tur) approaching in the priority line.

### Batch 9 digest (Sanhedrin/Bekhorot/Niddah/Nedarim/Shevuot/Temurah +
### Yer. scattered + first code rows — 34 listings)
- MT SANHEDRIN 26:7 (the code deploys the jurisdiction rule): litigating
  in gentile courts = "wicked, as if he blasphemed and RAISED A HAND
  against the Torah of Moses" (our header cited); THEN the licensed
  exception — violent opponent who won't come: TAKE PERMISSION from the
  beit din and rescue your property through their courts — principle +
  permission-token escalation path — MAJOR.
- Yer.San 1:1:6 + KhE: RShbY — the header teaches THE PLAIN SENSE
  suffices: a judge need not know all derived law; the written pshat
  rules (thefts/injuries) = MINIMUM-COMPETENCE spec — ADD.
- Yer.San 9:4 (block 2): THE INTENT-TRANSFER MATRIX — aimed-at-animal/
  gentile/nonviable killed viable = exempt; intent×force×target grid w/
  the sufficient-force diagonal LIABLE; R. Shimon: any this-one/that-one
  transfer exempt — the mens-rea calculus in mishnaic form — MAJOR
  (ledgered for block 2).
- Tosafot San 2b + Rashi-in-Gittin: לפניהם ANTECEDENT = THE SEVENTY
  ELDERS of Exod 24 (end of Mishpatim!) — the header's pronoun points
  forward to the Sanhedrin's founding body; coercion-powers vs plain
  adjudication allocated between אלהים and לפניהם — ADD.
- Bekhorot 34a: our בבגדו inside the yesh-em-la-mikra META-RULE debate
  (read-form garment vs written-form betrayal governs) — ADD.
- NIDDAH 45b-46a: THE AGE-GATE SPEC in full — vow-examination windows
  (girl 11->12, boy 12->13: the mufla-samukh-le-ish year — valid IF
  they understand); תוך-זמן fork (within-year = before, Rava rules);
  two-hairs before age = mole (שומא) not signal; R.Yose bRY: signal if
  STILL PRESENT; presumption reached-years-implies-signs, rebuttable;
  שמא נשרו (fell-out) worry split by stakes (chalitzah strict, miun
  lenient) — the complete transition-window semantics behind the אין
  כסף exit-signal — MAJOR.
- Yer.Shevuot 6:1: BS/BH minimum from the amortization curve — 3rd home
  (claim-minimum context; the מחלפה consistency-audit across domains) —
  CONFIRM+.
- Yer.Shevuot 7:8:2: OATH-ROLLUP LIMIT — additional claims roll onto an
  oath "until he says 'you are my SLAVE'"; punchline: "is there a slave
  NOWADAYS?" — the rollup capped at the slavery-claim AND the
  institution flagged OBSOLETE — a deprecation notice in the runtime —
  MAJOR.
- Temurah 30a + Rashi: shefachah-compulsion = GEZERAT HA-KATUV (decree-
  class, underivable) — the compulsion typed — CONFIRM+.
- Ben Yehoyada RH 16a: Saba deMishpatim AGAIN — "King of Israel, not of
  the nations": direct-rule (mercy-mode teshuvah works) vs delegated
  rule under the ministers (strict law) — governance architecture —
  ADD (corpus-world).
- Yer.AZ 2:7: staged disclosure — "students small: SUPPRESS the words;
  grown: reveal the MYSTERIES" joined to the סימה-treasure header
  reading — access control WITH release schedule — CONFIRM+.
- Yer.Eruvin 7:6 (=Maaser Sheni 4:3): THE CAPACITY LADDER — nut-and-
  pebble test battery (throws nut keeps pebble = trash-finder; keeps
  nut = peace-ways theft; hoards both = real theft); minor's gift NEVER
  valid (כי יתן איש "when a MAN gives" — block 4 anchor); full theft-
  liability only at two hairs — empirical developmental staging for
  legal capacity — MAJOR.
- Yer.Shabbat 6:9:9: Bar Kappara's omen — child reciting OUR בגפו verse
  taken as oracle ("nothing but this bruise") — verse-as-oracle folk
  runtime — ADD.
- Yer.Terumot 7:1: single-sanction rule (כדי רשעתו — one liability not
  two; lash-vs-pay exclusivity, eidim-zomemim precedent) — pairs w/
  no-double-liability — ADD.
- Kessef Mishneh Slaves 2:12 (citing RALBAG on Mishpatim): master may
  not sell/transfer the slave — code citing philosopher-commentator —
  ADD; Kiryat Sefer: the hefker-seed doctrine (אפקריה רחמנא לזרעיה)
  possibly rooted in OUR האשה וילדיה — ADD; Lechem Mishneh Rebels 5:4:
  the curse-liability STACKING analysis (judge+prince+father multi-
  count) around אלהים לא תקלל (block 4) — ADD.
PACE: bite 9 = 34 listings / 24.2k chars. Ledger 390 read (19.9%); 1,546
remain.

### Batch 10 digest (heavy code-apparatus: Lechem Mishneh + Mishneh
### LaMelech on MT Slaves; MT Issurei Biah 12:11; MT Yibbum 1:4 — 5)
- LM Slaves 3:9: TWO-STAGE PROCEDURE DECOMPOSITION — door OR doorpost
  valid for the STANDING stage (our verse, הגשה); DOOR ONLY for the
  piercing stage (Deut) — the mezuzah's mention allocated to stage 1;
  resolves the Mizrachi's redundancy objections — MAJOR.
- MnL Slaves 2:3: THE SLAVE/HIRELING ONTOLOGY — עבד גופו קנוי (the
  slave's BODY is acquired: no quitting, needs manumission-doc, "MY
  slaves" applies) vs hireling (labor only — even 6+ years is NOT
  slavery; Maharam's 3-year caution); self-seller default-term dispute
  (Rashi: 6 default / Ritva: NO default, term = contract, verse gives
  no shiur) w/ Mahari"t proving the default FROM JEREMIAH 34; the
  swallowed-value rule: if his 6-year price EXCEEDS the theft, he is
  not sold (דמיו מובלעין בגניבתו) — sale blocked on overvaluation —
  MAJOR MAJOR.
- MnL Slaves 3:9: THE DERIVATION-MODE META-DISPUTE — Rambam rules
  klal-u-frat here (metal awl) but ribui-u-miut in oaths/leprosy: "how
  does he certify the deed to both parties?!"; Ritva's doctrine: each
  tanna received PER-VERSE mode-assignments from his teacher (mode =
  per-verse annotation) vs the school-consistency view (mode = global
  compiler flag; R. Yishmael/klal-u-frat, Akiva/ribui-u-miut lineages)
  — MAJOR MAJOR; bore-size back-derived from the kohen-blemish
  threshold (vetch-size) — parameter recovered from an interaction
  effect; + THE THREE-VERSES RULE: yevamah+semikhah+eglah = "three
  verses coming as one DO NOT TEACH" — 3+ parallel exceptions stop
  generalizing (redundancy-count as generalization-blocker); batching
  combinatorics (one-court/two-courts × one-master/two-masters; even
  co-summoning barred per Tosafot) — MAJOR.
- MT Issurei Biah 12:11: the shefachah's INTERMEDIATE TYPE — "left the
  gentile class, did not enter Israel's class"; forbidden to the free
  (rabbinic lashes), PERMITTED to the Hebrew slave BY OUR VERSE (the
  explicit-Torah proof of the class boundary) — CONFIRM+.
- MT Yibbum 1:4: deployed descent edge case — his own shefachah's son,
  later freed + mother freed + married + died childless: she REQUIRES
  yibbum though her son by him lives — status-at-conception locked
  forever ("conceived pre-manumission never counts as his seed") —
  MAJOR.
PACE: bite 10 = 5 listings / 20.5k chars. Ledger 395 read (20.1%); 1,541
remain.

### Batch 11 digest (THE RAMBAM CODE STRATUM — MT Slaves/Marriage/Yibbum/
### Vows + mitzvah-registry + Tzafnat Pa'neach — 37 listings, 46k chars)
- MT Yibbum 4:33: THE KETUBAH TEMPLATE itself — full boilerplate (200
  zuz "which befit you MIN HA-TORAH", the everything-lien "even the
  cloak on my shoulders", non-asmakhta clause) — the deployed legal
  instrument descending from our 21:10 — MAJOR-ish.
- MT Marriage 2:1-2: age-gate constants codified (minor <12; two hairs
  + 12yr1day = naarah; +6 months EXACTLY = bogeret) — CONFIRM.
- MT Marriage 12:2: THE TEN-OBLIGATION RECORD — 3 Torah fields (our
  שאר/כסות/עונה) + 7 court fields (ketubah, medical, ransom, burial,
  widow-maint., daughters-maint., sons-inherit-ketubah) — source-tag
  per field — MAJOR (deployed schema).
- MT Marriage 14:7/14:15: sickness grace = SIX MONTHS then permission-
  or-divorce; rebel-husband increment (36 barley-weights silver/week);
  WHY no lashes on לא יגרע — no-ACTION negative isn't lashed —
  enforcement-type classification — ADD.
- MT Neg. 261-262 + Pos. 232-234: THE BLOCK'S API IN THE COMMAND-COUNT
  — five numbered mitzvot (judge-slave-by-his-laws / designate /
  redeem / no-resale / no-withholding, "and likewise ALL wives") —
  MAJOR.
- MT Rest 7:11: piercing on the court-agents' chol-hamoed public-needs
  docket — scheduling — ADD.
- MT Slaves 1:1-3:13: the deployed machine — entry paths (thief-only
  court-sale; destitution-only self-sale); master's-death table; the
  five exits; maintenance w/ fitness filter (excludes even rabbinic-
  secondary unions); shefachah provision (court-sold only, master OR
  MASTER'S SON gives her, compulsion); rite fully proceduralized
  (court of three, end-of-six, standing door/doorpost split, right-ear
  cartilage, metal awl through to door, master personally, no
  batching); declaration windows (twice, last-perutah); THE BILATERAL
  CHECKLIST with per-row verse tags ("until BOTH are in good state");
  sanctioned-force edge (master wounds the refusing pierced slave at
  yovel = exempt, to sever him from the now-forbidden shefachah) —
  CONFIRM+ (the whole sugya-layer compiled down).
- MT Slaves 4:5-4:10: THE PESAK LAYER VISIBLE — forks RESOLVED in
  deployment: purchase-money CONVERTS ("first monies were given for
  kiddushin" — rules the conversion view); son-designation requires
  ADULT son's permission (rules Resh Lakish); HER consent required
  (מדעתה) though father took the money; yiud = eirusin (no mourning/
  inheritance/vow-annulment until chuppah); "three things" per the
  Akiva line; signs even day-after-purchase free her; no-transfer
  void; Rambam's FIRST-PERSON derivation note (ויראה לי — why the
  verse needed the amah's case) — MAJOR MAJOR (fork-resolution table
  extractable by diffing code vs sugya).
- MT Vows 12:9: vow-interface deployed (his vow null — he is LIENED by
  our verse; her self-vow needs annulment else "we don't feed a person
  what's forbidden to him") — CONFIRM.
- Tzafnat Pa'neach (Rogatchover, 30k-char row, READ IN FULL): ontology
  treatise anchored on OUR yiud-to-minor Mekhilta ("even to a minor" —
  harmonized as reached-years-but-hairs-incomplete with RETROACTIVE
  adulthood once signs complete); the composite-type distinction
  (הרכבה מזגית "blended" vs שכונית "adjacent" composition) run through
  dozens of domains; boundary-kiddushin validates retroactively — the
  chain's most type-theoretic text, formalizing the age-gate boundary
  — ADD/MAJOR-ish.
PACE: bite 11 = 37 listings / 46.2k chars (one 30k row). Ledger 432 read
(22.0%); 1,504 remain.

### Batch 12 digest (Sefer HaMitzvot + Shorashim + SMaG Neg 81 — 15
### listings, 37k chars)
- Shorashim 8:4 + Marganita Tava: THE STATEMENT-TYPE DOCTRINE — Rambam's
  Root 8: לא תצא כצאת העבדים is a NEGATION (שלילה, information) not a
  PROHIBITION (אזהרה, command) — with the parallel set (לא יומתו, ולא
  יהיה כקרח = negations; the contrary Sanhedrin reading = asmakhta);
  the apparatus: a tanna who reads it as a real lav; hekesh-vs-kal-
  vachomer precedence war (no-partial-hekesh; hekesh defeats KV) —
  DECLARATIVE-vs-IMPERATIVE token classification as formal doctrine,
  our verse the test case — MAJOR MAJOR.
- ShM Neg 262 + Katzar 42: no-withholding generalized to ALL wives via
  the bootstrap (Rambam walks "came to teach, found learning"
  explicitly); the RECIPROCAL CONSIDERATION TABLE — her earnings FOR
  food, property-fruits FOR ransom, finds against enmity, inheritance
  FOR burial — each right priced against a duty — MAJOR.
- ShM Neg 318: curse-of-parents azharah by BINYAN AV from three sources
  (judge/prince/deaf; common side "among your people") — the מה-הצד
  common-denominator machine — ADD.
- ShM Pos 233: ⚠ MODULE DEPENDENCY — "the law of the Hebrew slave and
  amah operates ONLY WHEN THE JUBILEE OPERATES" — the block's runtime
  gated on the yovel clock (institution enable-flag) — MAJOR.
- Shorashim 9:6: ENUMERATION SEMANTICS — lav-shebikhlalut rules: our
  triple counts as ONE command (vs the maaser-triple split to per-item
  lashes when קרא יתירא proves לחלק) — when one verse = one command vs
  many — MAJOR method.
- SMaG Neg 81 (giant): THE FULLY-QUANTIFIED DEPLOYED SYSTEM — weekly
  flour schedule (2 kav wheat / 4 barley w/ the Edom-barley locale
  note), legumes/oil/figs, bed+mat, 3 pairs shoes/year per-festival,
  50-zuz annual clothing, new-in-winter, maah-per-week allowance, 3
  Sabbath meals; THE TANNA-WAS-LOCAL PRINCIPLE -> modern re-binding
  ("TODAY: two average meals per the city's standard") — locale-
  parameterized constants with explicit re-binding rule — MAJOR MAJOR;
  Rav Yosef: שאר = bodily closeness ("not like the Persians who serve
  their beds clothed"; R. Huna: 'I-in-my-garment' -> divorce+ketubah);
  six-year child support + public-shaming enforcement ("a raven wants
  its young!") + forced charity if assessable; away-husband 3-month
  presumption; custody (daughter with mother always, son to six);
  ALIYAH OVERRIDE (compel ascent to Israel even good->bad dwelling,
  never compel leaving); moredet procedures incl. RAV SHERIRA'S
  EMERGENCY PATCH (no 12-month delay "lest the daughters go out to bad
  culture" — Geonic runtime hotfix); widow regime incl. ברכת הבית
  ברובה (household economies-of-scale: five together need 4 kav not 5)
  and the medical split (unlimited-treatment = maintenance-class;
  capped = from her ketubah — chronic/acute insurance boundary) —
  MAJOR.
PACE: bite 12 = 15 listings / 37.1k chars. Ledger 447 read (22.8%);
1,489 remain.

### Batch 13 digest (SMaG Neg 179 + Pos 83/85/86/102 + SMaK 276 — 11)
- SMaG Neg 179: the בבגדו fork with TEXTUAL-VARIANT sensitivity — "per
  the OLD MANUSCRIPTS, and so reads Rabbeinu Yaakov (R. Tam)" — the
  law fork riding a manuscript reading; Rambam's male-slave extension
  quoted — CONFIRM+.
- SMaG Pos 83 (2nd deployed slave-code, diffable vs MT): convert can't
  be Hebrew-slave (ושב אל משפחתו — needs a FAMILY; teacher's
  harmonization: convert-via-Israelite-mother has one); sale to
  idolatry-service VALID after the fact + MITZVAH TO REDEEM (kin in
  kinship order); worked deduction arithmetic (60/4yrs -> pay 20;
  40/10yrs -> 4/yr); sold-to-gentile reckons TO YOVEL, cash-only
  redemption; ⚠ RAVA: master's WAIVER of remaining money does NOT free
  — a manumission DOCUMENT still required since "his body is acquired"
  — debt-waiver works, STATUS-change requires the instrument — MAJOR;
  kohen-slave GETS the shefachah (rules like Rav); kohen never pierced
  + "returns to the PRESUMPTION of his family"; cartilage upper-ear
  per rabbis; the entry-path difference-table printed — MAJOR.
- SMaG Pos 85: COMPULSORY REDEMPTION of the amah against the FATHER's
  will "because of family blemish" (פגם משפחה); the document-writer
  fork (R. Chisda father / R. Huna master) PRESERVED OPEN in the code
  — ADD.
- SMaG Pos 86: yiud formula list includes הרי את מיועדת לי (Kid 6a's
  doubtful formula ruled usable in yiud context) — CONFIRM.
- SMaG Pos 102 (block 2): the FOUR EXECUTIONS as positive commandments
  (procedures); severity ordering; ⚠ THE VENUE-DEPENDENCY DOCTRINE —
  Sanhedrin exiled itself 40 yrs pre-destruction and capital law
  SUSPENDED "because the PLACE causes" — capital jurisdiction gated on
  the Chamber-by-the-altar (our adjacency derivation cited as source)
  — a second module-dependency flag (like the yovel gate) — MAJOR;
  stoning/burning/strangulation procedures; idolater stoned at "the
  gate where he served" — ledgered for block 2.
- SMaK 276: popular-code deployment — locale re-binding restated;
  enforcement ladder (public shaming -> forced charity if assessable);
  "even the wealthiest works wool — idleness breeds melancholy and
  sin"; the intimacy-duties list reserved to the wife — CONFIRM.
PACE: bite 13 = 11 listings / 18.4k chars. Ledger 458 read (23.3%);
1,478 remain. Codes stratum largely done; next: Tur rows, Onkelos/
Targums, Rashi, then the bench (IE/Ramban/Chizkuni...).

### Batch 14 digest (SMaK remez + Chinukh 42-47/63/552 + ONKELOS 21:1-11 + Minei Targuma 21:10 — 35)
- Chinukh 42 (Hebrew slave): the mitzvah is ON THE COURT — "to judge
  the law of the Hebrew slave as written" — the statute compiles to a
  JUDICIAL API, not private duty; release-path enum restated (7th yr /
  yovel / money-deduction / master's death w/o male heir) — CONFIRM.
- Chinukh 43 (yiud): designation-beats-redemption priority rule
  (מצות יעוד קודמת למצות פדיה "designation precedes redemption",
  Bekhorot 19a) — CONFIRM; 43:4 yovel-gate restated (Gittin 65a) AND
  ⚠ NON-COERCIBLE POSITIVE COMMAND: "one should not force him — the
  Torah left it to his will," from ואם שלש אלה לא יעשה ("if he does
  not do these three") — a soft-obligation type (recommended, blessed,
  unenforced) vs hard court-enforced commands — ADD to statement-type
  doctrine.
- Chinukh 44 (redemption): the pro-rata algorithm with a WORKED
  NUMERIC EXAMPLE — bought 60 dinars/6 yrs, worked 3, saved 30 → take
  30 and free her; forbidden counter-claims enumerated ("complete your
  term", "my money sat idle — pay a premium") — a TEST VECTOR in the
  code + rejected-inputs list — CONFIRM+ (matches SMaG's 60/4 and
  40/10 vectors; three independent vectors now).
- Chinukh 45 (no resale): לעם נכרי "to a foreign people" resolved PER
  ONKELOS as לגבר אחרן "to another MAN" — any third party; "foreign
  people" is rhetoric of severity, not scope — the TARGUM cited as the
  binding resolver by a 13th-c code — CONFIRM.
- Chinukh 46 (three duties): Ketubot 47b triple restated; the
  amah→all-wives extension via "comes to teach, ends up taught"
  (בא ללמד ונמצא למד) on כמשפט הבנות "per the law of the daughters" —
  Mekhilta's inversion operator NAMED in the code — CONFIRM; 46:2-3:
  waiver question (Ketubot 56a) flagged; standard-of-living floor
  עולה עמו ואינה יורדת "she rises with him and does not descend" =
  max(her family's standard, his) — ADD; onah schedule by occupation
  (sailor 2/yr, camel-driver 1/mo, scholar weekly) — locale/occupation
  parameterization CONFIRM; violation = lav but NO LASHES because
  אין בו מעשה "it has no act" — enforcement typology: actless
  prohibitions are non-floggable — CONFIRM.
- Chinukh 47 (block 2, ledgered): DEFAULT-VALUE RULE — "every
  unspecified death in the Torah is strangulation" (Sanhedrin 52b) — a
  language-level default parameter; capital liability excludes payment
  (אין כסף "no money", Mekhilta) — no-double-liability — ADD.
- Chinukh 552 (marriage): cash-kiddushin bootstrap from אין כסף "no
  money" (21:11) restated in the codes — "no money for THIS master,
  but there is for ANOTHER master — the father" — multi-witness with
  Kiddushin 3b — CONFIRM.
- Chinukh 63/260/298/336/343/477/478/479/486/518/540/587: back-pointer
  rows — "I wrote it in Mishpatim (mitzvah N)" — the codes are a
  HYPERLINKED GRAPH rooted at the Mishpatim entries; periphery.
- ⚠ ONKELOS 21:1-11 — the RESOLVER LAYER read verse-by-verse. Fork
  resolutions baked into the translation: 21:1 תסדר "you shall ARRANGE"
  (the set-table/curriculum verb); 21:2 עבדא בר ישראל "a slave, a son
  of Israel" — resolves the עברי fork to Israelite-slave; 21:3
  בלחודוהי "alone" for בגפו; 21:6 לקדם דיניא "before the JUDGES" for
  אל האלהים "to the elohim" — THE classic resolver call (God/judges
  fork → judges); 21:8 reads the qere לו "for himself" (דיקימה לה "who
  designated her for himself") resolving the ketiv/qere fork, and
  בבגדו בה → במשלטה בה "by his dominion over her" (a THIRD reading vs
  the Mekhilta's betrayal/garment fork); 21:9 כהלכת בנת ישראל "per the
  HALAKHAH of the daughters of Israel" — משפט rendered as הלכה; 21:10
  שארה → זיונה "her SUSTENANCE" — resolves שאר to food/maintenance.
  BUT 21:6 לעלם kept literal "forever" — the yovel-override NOT
  applied in translation; the targum resolves some forks and leaves
  others surface-literal for the oral law to override at runtime —
  MAJOR (selective early-binding).
- ⚠ MINEI TARGUMA on 21:10 (9k-char super-commentary, READ IN FULL):
  the שאר mega-fork — THREE readings (food/Rambam+Rashi+Onkelos;
  flesh-closeness/Ramban+Rav Yosef "not like the Persians who have
  relations clothed"; bed-linen/Ran's reading of Ramban) — and each of
  the three duties INDEPENDENTLY toggles biblical-vs-rabbinic. The
  psak cascade EXPLICITLY rides the targum: Rambam/Tur/Rashba rule
  maintenance biblical "וכן תרגם אונקלוס" ("and so Onkelos
  translated") — a ONE-WORD TRANSLATION CHOICE is load-bearing
  authority for a millennium of law — MAJOR (the translation layer is
  an authoritative binding, not display). Plus derivation-type
  doctrine: the same kal-vachomer can be REAL derivation (→ biblical)
  or asmakhta/mnemonic (→ rabbinic) — the inference's TYPE TAG changes
  the output's authority level (SMaG: REbY's K"V is asmakhta like the
  Megillah K"V) — MAJOR; and the מלתא דאתיא בק"ו טרח וכתב לה קרא
  "what's derivable by K"V Scripture writes anyway" fork (does the
  compiler emit redundant code?) — tannaim split — ADD.
PACE: bite 14 = 35 listings / 22.3k chars (Chinukh rows short, one 9k
mega-row). Ledger 493 read (25.1%); 1,443 remain. Codes stratum DONE;
Onkelos DONE. Next: other Targums (Yonatan/Yerushalmi), Tur, Rashi.

### Batch 15 digest (Minei Targuma 21:10:2-3 + Tg Jerusalem + TARGUM JONATHAN 21:1-11 + Divrei David/Taz — 23)
- Minei Targuma :2 — ⚠ LAW FORK RIDING A PRINTING ERROR: the SMaG line
  "per REbY food+onah are rabbinic" ruled a SCRIBAL ERROR (טעות סופר)
  by internal-consistency analysis of the SMaG's own structure (its
  opening counts all three as commanded; "they disputed only the
  VERSE's exegesis, not the law") + variant printings with marginal
  "this is not [right]" + Parashat Derakhim concurring — text-critical
  adjudication of a code's source — MAJOR. Plus K"V-strength doctrine:
  "a person derives kal-vachomer ON HIS OWN" (Niddah 19b) — a real
  inference engine, valid unless a rebuttal (פירכא) fires; sole
  carve-out אין עונשין מן הדין "no PUNISHMENT from inference" (Makkot
  5b); the Megillah K"V was OPERATIVE (prophets added the reading on
  its strength) — against the asmakhta reading — CONFIRM
  derivation-type doctrine, now with the validity conditions.
- Minei Targuma :3 — the amoraic fork WHICH DUTY IS PRINCIPAL (מזוני
  עיקר "maintenance is principal" / Rav Huna-Rav vs מעשה ידיה עיקר
  "handiwork is principal" / Resh Lakish) decides the wife's
  UNILATERAL WAIVER right ("I won't be maintained and won't work") —
  waivability rides on which side of the exchange is the rabbinic
  add-on — CONFIRM waivability typology; baraita EMENDED (אימא "say:
  they enacted handiwork in exchange for maintenance" — direction
  flipped) to harmonize — runtime patching of a source — ADD.
- Tg Jerusalem 21:10: "her FOOD, her ORNAMENTS, her CLOAK, her
  conjugal visit" — food reading + ORNAMENTS added (the rabbinic
  add-on inlined) — ADD.
- ⚠ TARGUM JONATHAN 21:1-11 — the ORAL LAW COMPILED INTO the
  translation (vs Onkelos's minimal resolver — two compilation
  strategies side by side): 21:2 "when you buy FOR HIS THEFT" —
  court-sale-for-theft ruling inlined; 21:3 "husband of an ISRAELITE
  wife" — which wife exits with him resolved; 21:6 court grants
  PERMISSION (ויסב מנהון רשותא "he takes authority from them"), RIGHT
  ear, pierced WITH A NEEDLE (במחטא — vs the awl!), and serves עד
  יובלא "UNTIL THE YOVEL" — TJ inlines the yovel-override that Onkelos
  left literal (לעלם "forever") — the two targums BIND AT DIFFERENT
  TIMES — MAJOR; 21:7 "his LITTLE daughter" (minor only) + "not like
  CANAANITE slaves freed by tooth-and-eye, but by shemittah-years, by
  SIGNS (puberty), by yovel, by master's death, by money" — the
  complete exit-enum including pure-oral סימנים inlined, resolving the
  Mekhilta's comparison fork — MAJOR; 21:11 "these three" RESOLVED
  inline = designate-for-self / for-son / let-be-redeemed (the
  Mekhilta's first opinion chosen) + ברם גט פטורין יהיב לה "but he
  gives her a RELEASE DOCUMENT" — a TJ-specific instrument add — ADD.
- Divrei David (Taz) 21:1:2 — Rashi's "set table" decompiled AS THE
  STACK: verse-phrases mapped to מקרא scripture → שימה בפיהם "place in
  their mouths" = MISHNAH → אשר תשים לפניהם = TALMUD "that explains
  everything with its reason" — the curriculum verse read as the
  layered oral-torah architecture itself — CONFIRM+.
- Taz 21:2:1 — the REJECTED ALTERNATIVE MODEL: without our verse, a
  Hebrew slave would work off his PURCHASE PRICE (amortization, yovel
  as outer bound, per Behar); the verse legislates the FIXED SIX-YEAR
  TERM instead — statutory constant vs debt-amortization algorithm —
  ADD; 21:2:2 meta-rule of the calculus: one may ask why a word is
  present, never demand "let Scripture have written it otherwise"
  (לכתוב רחמנא לא אמרינן) — permissible compiler-critiques — ADD;
  21:2:4 the Mekhilta's "the Torah called him 'slave' AGAINST ITS
  WILL" — עבד is a technical STATUS TAG required for rule-application,
  not a permitted insult (Taz against the Ra'em) — ADD.
- Taz 21:3:1 — ⚠ PERMISSION-vs-POWER analysis: "his master does not
  give him a shefachah" limits the MASTER'S COERCIVE AUTHORITY (בעל
  כרחו), not the slave's own option — proven from R. Tarfon's
  mamzer-purification advice (Kiddushin 69a; the advice collapses if
  an issur existed) — a Hohfeld-style rights decomposition inside the
  17th-c apparatus — MAJOR; the בגפו etymology fork (בגופו "his body
  alone" / REbY → wife AND children required; בכנפו "his garment" /
  Targum-Rashi → wife suffices) carries the precondition-set — ADD.
PACE: bite 15 = 23 listings / 21.4k chars. Ledger 516 read (26.3%);
1,420 remain. Targums DONE. Next: more Rashi-apparatus, Rashi, Tur.

### Batch 16 digest (Taz on 21:3-11 + Rashi Deut 15 + Rashi 21:1-3 — 29)
- Taz 21:4:1 — the Mekhilta's Canaanite-wife proof RECONSTRUCTED: "the
  woman and her children belong to the master" only typechecks if the
  mother is a Canaanite shefachah (offspring-status follows HER); an
  Israelite mother's children follow the father — the DESCENT
  ALGORITHM used as type-inference to force the fork — CONFIRM+.
- Taz 21:6:2 — verse-to-case ALLOCATION BY ELIMINATION: self-seller
  has "until yovel he works", court-sold has "he returns to his
  family", so ואיש אל משפחתו "each MAN to his family" must be the
  PIERCED slave — plus the gendered-word inference (what runs for men
  not women? piercing) — CONFIRM.
- Taz 21:7:3 — ⚠ DUELING-INFERENCE DEADLOCK: male slave exits by
  limb-loss? K"V from the Canaanite says YES, K"V from the amah says
  NO — "the two sides are balanced, a complete K"V each way" → the
  engine DEADLOCKS and Scripture must supply the explicit hekesh
  (עבריה↔עברי) to decide; אין היקש למחצה "no half-hekesh" (it decides
  everything it covers) — inference-conflict needs ground truth —
  MAJOR; plus rebuttal-licensing is BROAD (a pirka may cite a trait
  structurally inapplicable to the target — Yevamot 71a precedent).
- Taz 21:8:1-2 — yiud mechanics: purchase-money RETROACTIVELY becomes
  kiddushin-money — designation is "mere preparation," no new act
  (הכנה בעלמא) — CONFIRM; the mitzvah rides the QERE (read לו "for
  him" with vav — "fitting for him to designate her", Tosafot).
- Taz 21:8:3 — ⚠ FLAT-RATE vs MARKET-RATE: the amah's deduction is
  DETERMINISTIC LINEAR — "every year counts a sixth of the maneh,
  lenient or stringent alike" — vs the worker rules (appraise done/
  remaining, Bava Metzia 76b) and vs the sold-to-gentile whose TWO
  verses give a PRO-SLAVE DIRECTIONAL rule (many years remain → count
  by purchase-money; few → by years — always the lenient branch) —
  three different amortization functions in one statute-family —
  MAJOR; also: any worker may quit mid-day (כי לי בני ישראל עבדים
  "they are MY slaves" — no specific performance) except where loss
  results; the amah's deduct-and-leave overrides even that — ADD; the
  שכיר-שכיר gezerah-shavah + vav-of-addition (וי"ו מוסיף על ענין
  ראשון) chain wiring cash-purchase across the four sale-modes traced
  in full — CONFIRM.
- Taz 21:8:4 — scope fork on the resale bar: Ramban/Mekhilta = two
  prohibitions (to a gentile; slavery-after-slavery); Rambam =
  slavery-after-slavery OK, only after MARRIAGE no resale; Taz proves
  עם "people" can denote an individual ("given to another עם" = the
  step-mother darshah) — ADD.
- Taz 21:9:1 — son STEPS INTO the father's designation right (קם
  תחתיו): mere designation, no new money from the son — delegation
  inherits the paid consideration — CONFIRM.
- Taz 21:11:1 — ⚠ ABSORBING-STATE analysis: the three remedies differ
  in TERMINALITY — yiud (to him/son) is absorbing (signs/bogeret no
  longer free her — she is WIFE); the redemption path leaves the
  signs-exit LIVE — the exits form a state machine with one absorbing
  branch — MAJOR-adjacent ADD.
- Taz 21:11:2-3 — the בא זה ולימד על זה "this came and taught on that"
  redundancy mechanism on חנם (bogeret window) + אין כסף (naarah
  window): both words needed to block even strained misallocation;
  Rabbah's תושב/שכיר parallel; the yes-money-for-the-father דיוק —
  CONFIRM age-gate windows + redundancy semantics.
- Rashi Deut 15:12/17: Re'eh's two novelties (amah exits in six —
  father-sold minor, before signs; severance grant); piercing is
  MALE-ONLY ("the slave" masc., Sifrei) — CONFIRM.
- ⚠ Rashi 21:1 (three comments): Sinai-continuity (ואלה adds — civil
  law same revelation as the Decalogue) + SANHEDRIN BESIDE THE ALTAR
  (venue doctrine at the block's front door) + the SET-TABLE (teach
  REASONS, not rote) + FORUM EXCLUSIVITY — "not before gentiles, even
  if you know they'd rule identically": outcome-identity does NOT
  license forum substitution — same output from a different engine is
  not the same law; taking cases there "honors idolatry" — MAJOR.
- Rashi 21:2-3: the two disambiguations (Hebrew-slave-not-
  slave-of-Hebrew via אחיך "your brother"; court-sold-not-self-seller
  via Behar allocation); בגפו per targum "alone"/garment; wife=
  Israelite; "who brought her in that she should exit?" → master owes
  MAINTENANCE of wife AND children — CONFIRM.
PACE: bite 16 = 29 listings / 18.1k chars. Ledger 545 read (27.8%);
1,391 remain. Next: Rashi 21:4-11, then Tur, then the bench.

### Batch 17 digest (Rashi 21:4-11 + Rashi crossrefs + Midrash Aggadah + Lekach Tov opening — 70)
- Rashi 21:6:1 — the piercing court = "he must consult THE ONES WHO
  SOLD HIM to him" (שימלך במוכריו) — same-court requirement — CONFIRM.
- Rashi 21:6:2 — the mezuzah is INVALID as piercing target ("in the
  door, not the mezuzah") and appears ONLY to donate its parameter
  (standing → the door must stand) — the parameter-server pattern in
  miniature — CONFIRM.
- Rashi 21:6:3 — right ear via the אזן-אזן verbal analogy from the
  leper; the two rationale homilies (the EAR that heard "do not steal"
  / "they are My slaves" at Sinai; door+mezuzah as EGYPT WITNESSES —
  pierced "before them") — penalty targets the offending organ,
  instruments chosen as witnesses — CONFIRM rationale layer.
- Rashi 21:6:4 — לעלם: "fifty years ARE CALLED olam" — SEMANTIC
  REBINDING, not override (the word's meaning is redefined as a
  bounded epoch), and "until yovel whether near or far" — ADD nuance
  to the override registry.
- Rashi 21:7:2 — ⚠ explicit MIN() OVER EXIT-EVENTS: "works six, or to
  yovel, or until she brings signs — WHICHEVER COMES FIRST precedes to
  free her" (כל הקודם קודם לחרותה); injury compensation still owed
  (eye/tooth VALUE) — freedom and damages decoupled — CONFIRM+.
- Rashi 21:8:3 — THIRD test vector: maneh(100)/6 yrs, worked 2 → each
  year 1/6, refund two-thirds and she leaves — flat linear again —
  CONFIRM; 21:8:4 resale bar binds MASTER AND FATHER both; 21:8:5
  בבגדו dual-subject (master betrays by no-yiud; father betrayed by
  the sale).
- Rashi 21:9 — the son's yiud FORMULA quotes the retroactive
  consideration: "you are designated to me WITH THE MONEY YOUR FATHER
  RECEIVED as your price" — CONFIRM formula+money mechanic.
- Rashi 21:11:2 — ⚠ ADVERSARIAL-ROBUSTNESS rationale for redundancy:
  both חנם and אין כסף written "so as not to give the LITIGANT an
  opening to distinguish" (שלא ליתן פתחון פה לבעל הדין לחלק) — extra
  words exist to defeat hostile parsing — ADD (redundancy semantics'
  stated purpose).
- Rashi 31:18 — the TRANSMISSION PROTOCOL at source: Moses heard from
  the Almighty and "they BOTH REPEATED the halakhah TOGETHER"
  (read-back verification at the first hop); לדבר אתו = the statutes
  of THIS parashah; no earlier-and-later (narrative order ≠ command
  order) — ADD.
- Rashi Lev 22:10 (crossref): even the PIERCED slave's body is NOT
  owned for terumah-eating ("tosahv" = pierced, "sachir" = six-year;
  neither eats) — acquisition-scope limit vs the Canaanite slave; note
  against Rava's גופו קנוי "his body is acquired" (different sense:
  status-change needs an instrument, yet no terumah-ownership) — ADD
  fork-flag; Menachot 10a: the אזן-אזן analogy rides the RICH leper's
  redundant verse — a gezerah-shavah needs a VACANT (מופנה) word —
  CONFIRM vacancy rule; Lev 25:10 דרור = residence-choice liberty.
- ⚠ Midrash Aggadah 21:1 — המשפטים decompiled as NOTARIKON: "the
  judges are commanded to attempt SETTLEMENT BEFORE judgment"
  (ה-מ-ש-פ-ט-י-מ acrostic) — pre-trial mediation encoded in the
  block's first word — MAJOR; forum-exclusivity escalated (gentile-
  court plaintiff "has no share in the world to come"); true judge =
  partner in Creation; Jerusalem fell over perverted justice (the
  corrupt-judge narrative: "steal and split with us", reciprocal-favor
  שלמונים, the orphan/widow denial cascade) — the enforcement stakes.
- Midrash Aggadah rest: shefachah is PERMISSION not duty (21:3); say-
  and-repeat (21:5); R. Natan b. Avtilemos — disgrace-custom FORFEITS
  the yiud right (21:8); Israel-as-amah allegory (periphery); the
  three duties extended to all daughters (21:10).
- ⚠ Lekach Tov 21:1 — TEN justice-prohibitions mirroring the TEN
  Commandments (structural 10↔10) — ADD; Marah precedent (חק ומשפט
  BEFORE Sinai — R. Yehudah: these ADD to Marah's laws) — ADD; why
  civil law first: adjudication MAKES PEACE (RSHb"Y); ⚠ COERCED-GET
  rule: coerced by a JEWISH court = valid, by gentiles = invalid, BUT
  gentiles may beat him saying "do what the Israelite court tells
  you" — foreign muscle under domestic authority IS domestic —
  jurisdiction+agency composition — MAJOR; R. Chanan: אשר תשים = the
  JUDGES' TOOLKIT (strap/lashes, shofar/ban, sandal/chalitzah) — the
  enforcement instruments enumerated; "the FATHERS of the laws are
  written, their DERIVATIVES oral" (אבות/תולדות as parent/child rule
  classes; covenant "by the mouth of") — CONFIRM architecture.
- Lekach Tov 21:2 — buyer-permission gated on court-sale (כי תקנה =
  "when", not a command); GER sold for theft exits in six "his law is
  like Israel's" — ⚠ fork-flag vs SMaG's convert-can't-be-Hebrew-slave
  (different sale-mode? track); serves the SON on master's death (בן
  קם תחת אביו — with yiud + ancestral-field as the rule's two other
  sites; the BROTHER does not inherit the office); RUNAWAY completes
  his years; יעבד written DEFECTIVE → no slave-customs (no
  foot-washing/sandal/bathhouse-gear), with the STUDENT exception
  gated on PUBLIC KNOWLEDGE ("where they don't know him — forbidden,
  lest they say he's a Hebrew slave; where known — permitted") —
  reputation-context parameter — ADD; no trade-change; "the SEVENTH is
  of the SALE, not of the years" — per-contract clock — CONFIRM; NO
  manumission document at term-expiry (auto-release; vs Rava: the
  instrument is needed only for EARLY status-change) — CONFIRM+.
PACE: bite 17 = 70 listings / 18.1k chars (Rashi+midrash rows short).
Ledger 615 read (31.3%); 1,321 remain. Next: rest of Lekach Tov, Tur,
the bench (Ibn Ezra/Ramban/Sforno/Chizkuni).

### Batch 18 digest (Lekach Tov 21:2-11 complete + Sekhel Tov + Midrash Mishlei + Tanchuma Mishpatim — 66)
- LT 21:3:3-4 — maintenance derived "from the EXIT you learn the
  ENTRY" (מכלל יציאה אתה למד כניסה — the exit-clause reveals the
  entry-state); WHICH wife qualifies: excludes the levirate-widow-in-
  waiting (שומרת יבם) and the betrothed (ארוסה "who is not WITH him")
  — precise predicate on the maintained wife — ADD.
- LT 21:4 — the shefachah assignment must be EXCLUSIVE ("designated to
  him — not an ownerless shefachah"); offspring enum explicitly covers
  TUMTUM and ANDROGYNOS (ambiguous-sex children — "her children, in
  any case") — edge-case inclusion — ADD; even the MASTER's own child
  from his shefachah is a slave (offspring-follows-mother, K"V for the
  gentile woman); she needs NO GET (no kiddushin attach — hekesh
  slave↔shefachah); the SICK slave exits ON TIME ("even though he was
  sick and didn't work, he goes out") — downtime doesn't toll the
  clock — ADD.
- LT 21:6:3 — ⚠ AGENCY-OVERRIDE: the piercing must be by the master
  PERSONALLY — "HE and not his agent, even though everywhere a
  person's agent is as himself, HERE he and not his agent" — an
  explicit carve-out disabling the general delegation doctrine
  (שלוחו של אדם כמותו) — MAJOR.
- LT 21:6:5 — ⚠ THE OVERRIDE FORMULA VERBATIM: הלכה עוקבת (את) המקרא
  "the halakhah CIRCUMVENTS the Scripture — the Torah said 'with an
  awl' and the halakhah: with anything" — the awl-registry entry
  stated in the code's own words — CONFIRM+; then the narrowings
  PRESERVED as forks: Rabbi — metal only (awl-LIKE, דומיא constraint
  on the override's range); lobe (R. Yehudah) vs even-cartilage (R.
  Meir) with the kohen-piercing consequence wired to hole-location
  (R. Meir: NO kohen pierced; sages: pierced) — ⚠ ATTRIBUTION FORK vs
  SMaG/Kiddushin wiring (who holds cartilage) — fork-flag.
- LT 21:6:10 — the AUTHOR'S OWN father's rationale: piercing sited at
  the door = PUBLIC WAY so passersby ask "why stay enslaved? the Torah
  freed you" — publicity as standing advertisement of the choice
  (door ~ mezuzah: both at the public way) — ADD.
- LT 21:6:11-12 — bounded-olam SECOND WITNESS: Samuel's "dwell there
  ad olam" = the Levite fifty (Rabbi's proof); service-inheritance
  table: ordinary slave serves the SON (not daughter); the PIERCED and
  the AMAH serve neither — CONFIRM diff-table.
- LT 21:7 — ONLY the father sells (not mother, not for a son); minor-
  only via hekesh to VOW-ANNULMENT (the father's-house window shared
  across modules — בנעוריה בית אביה); bondage-power → kiddushin-power
  K"V; R. Yishmael's ALTERNATE cash-kiddushin route (K"V from the
  shefachah: acquired by cash though not by intercourse → the bat
  Yisrael a fortiori) — second bootstrap path — ADD; sold ONCE never
  twice + ⚠ POWER-EXHAUSTION: "orphan in her father's lifetime" —
  father married her off, she divorced while minor → his kiddushin-
  power is CONSUMED, never returns — one-shot authority semantics —
  MAJOR-adjacent ADD; MIUN rules (mother/brothers-marriage refusable;
  matured+consented → no refusal; error-kiddushin refusable "even with
  her child on her shoulder") — CONFIRM.
- LT 21:8 — לעם נכרי read as a WARNING TO THE COURT (אזהרה לב"ד) that
  the father not sell to a gentile — the prohibition's ADDRESSEE is
  the enforcement layer — ADD; בגידה = deception (שיקור, per "Judah
  dealt falsely"); the R. Yishmael (master took-to-designate and
  didn't → no resale) / R. Yonatan b. Avtolemos (disgrace forfeits
  keeping her) fork restated.
- LT 21:10:4 — R. Yonatan: clothing FITTED to age and season ("young
  woman's clothes for the young… NEW in the rainy season, worn in the
  dry") — the spec parameterized even on the non-food reading —
  CONFIRM; food = life-sustenance (K"V), intimacy = "what she was
  married for."
- LT 21:11:2 — ⚠ "FREE of MONEY, not free of the GET" (חנם מן הכסף
  ולא חנם מן הגט) — the exit is fee-free but NOT instrument-free —
  the doctrine behind TJ's "he gives her a release document" — ADD
  (applies where yiud made her a wife); 21:11:3-4 the חנם/אין-כסף
  allocation fork PRESERVED with attributions (R. Natan: bogeret/
  naarut; Abba Chanan-R. Eliezer: bogeret/signs+deduction).
- LT crossrefs — Gen 16:6: ABRAHAM JUDGED BY THE BLOCK'S RULE (may not
  re-enslave Hagar once made a mistress — cites our 21:8 + Deut 21:14)
  — settlement-link candidate Gen 16 ↔ Exod 21:8 for the corpus world
  — ADD; Lev 21:2: שארו = his WIFE (kohen mourning) — the block's
  word שאר resolving consistently across modules; descent rules
  restated from our 21:4 as the proof-text.
- Midrash Mishlei 2:7 — the STRUCTURAL SANDWICH: "laws before it and
  laws after it" — Marah's statute BEFORE Sinai, Mishpatim after — the
  Decalogue sandwiched between civil-law layers (double-edged sword
  image) — ADD.
- Tanchuma Mishpatim 1-4 — two-tier enforcement: "if there is
  judgment BELOW there is no judgment ABOVE" (human courts preempt
  divine intervention); God SELF-BOUND: "were I to step past the din
  once, the world would burn… My hand grasps justice" — the authority
  stack's top: God outvoted below (לא בשמים) AND self-bound above —
  CONFIRM+; world-stands-on-justice (flood generation); ואלה adds to
  MARAH (R. Abbahu); Ki Tisa 17: the WRITTEN/ORAL SPLIT BY DESIGN —
  God foresaw the nations taking the written text, so "Mikra in
  writing; Mishnah, Aggadah, Talmud BY MOUTH — they distinguish Israel
  from the nations" + Moses taught even "what a seasoned student will
  one day ask" — the oral layer as the distinguishing covenant —
  CONFIRM architecture; Tanchuma Behar 8:2: the POVERTY CASCADE state
  machine (sin → sells field → house → DAUGHTER → himself) — our 21:7
  positioned as stage three — ADD.
PACE: bite 18 = 66 listings / 19.3k chars. Ledger 681 read (34.7%);
1,255 remain. Lekach Tov/midrash-on-block largely done. Next: Tur
rows, the bench (Ibn Ezra/Ramban/Sforno/Chizkuni/Radak), formalizers.

### Batch 19 digest (Tanchuma both recensions + Midrash Tannaim + Midr. Tehillim + Shemot Rabbah 30:1-6 — 32)
- Tanchuma Mishpatim 6:1 (embedded Aramaic she'ilta + R. Shimon
  baraita) — forum exclusivity DOUBLED: "before them and not before
  gentiles, before them and NOT BEFORE LAYMEN (הדיוטות)" — the second
  exclusion bars untrained/unordained judges, not just foreign courts
  — CONFIRM+ (authorization requirement on the bench itself).
- Tanchuma Mishpatim 6:2 + Shemot Rabbah 30:2 — the ADJACENCY
  derivation: "do not ascend My altar by STEPS" sits next to "and
  these are the laws" → הוו מתונין בדין "be DELIBERATE in judgment"
  (R. Avina: as priests walk heel-beside-toe on the ramp, judges take
  no big steps) — the semukhin operator producing a procedural rule —
  CONFIRM.
- Tanchuma Mishpatim 2 — the civic-duty rule: one who withdraws from
  the judicial commons ("what do I care for their courts — peace upon
  you, my soul") DESTROYS the world (ואיש תרומות יהרסנה — sets himself
  aside like terumah in the corner) — participation obligation — ADD.
- Tanchuma Vaetchanan 4-5 — ⚠ the block LITIGATED AGAINST GOD: Moses
  pleads ואם אמר יאמר העבד "if the slave shall SAY: I love my master…
  I will not go free… he shall serve forever" — "I love You, Your
  Torah, Your children; I do not wish to go free (die) — and You did
  not keep ועבדו לעולם with me!"; God's answer is PROCEDURAL: "your
  ADVERSARY-AT-LAW (בעל דין, Adam) already obtained the decree" — the
  statute runs even in the heavenly court, and a prior judgment
  controls — ADD (with the leviathan עבד עולם "eternal slave" parallel
  from Job 40).
- Midrash Tannaim Deut 15 — ⚠ PATCH SEMANTICS: the Re'eh passage
  "comes to teach the things MISSING in it" (דברים המחוסרין בו) — the
  second passage is a diff supplying omitted fields (severance) on the
  Exodus base — ADD; the SICK slave: "ill and recovered — could you
  think he repays the wage of his idle time? יצא לחפשי חנם 'he goes
  out free FOR NOTHING'" — downtime is on the master, חנם kills the
  repayment claim — CONFIRM+ (second witness w/ explicit anchor); no
  PRIVATE piercing ("could I think he pierces him between themselves?
  — 'his master shall bring him to the elohim' = the judges"); master
  must himself have wife+children (his declared love-objects must
  exist); amah: severance yes, piercing no.
- Midrash Tannaim Deut 32:41 — two-tier enforcement WITH DELEGATION
  LANGUAGE: "if those below do the din, I do not judge My world — MY
  JUDGMENTS I HAVE ALREADY HANDED OVER TO THEM (משפטי כבר מסרתיו
  להם)" + God self-bound (one step past the din → the world burns) —
  CONFIRM+ the authority stack's transfer instrument.
- Maharzu on ShR 30:19 — "the Decalogue, the Torah's GENERAL form,
  DEPENDS on the civil laws" — the Ten as interface, Mishpatim as
  implementation — ADD.
- Shemot Rabbah 30:1 — divine self-binding as the compliance MODEL:
  "as I could override the din and do not — My hand grasps it — so you
  shall not step outside the din" — CONFIRM.
- ⚠ Shemot Rabbah 30:5 — SELF-REFERENTIAL APPLICATION: God runs the
  block's own laws on Himself — "I ACQUIRED you in Egypt (כי תקנה);
  as you may not work your brother past six years, I made the world in
  six days"; "I had one daughter (the Torah) and SOLD her to you (כי
  ימכור איש את בתו) — take her out only enclosed in the ARK"; לא תצא
  כצאת העבדים "treat her with dignity, for you captured her from Me" —
  the amah-statute typed onto the Torah itself, the giver as first
  party — MAJOR-adjacent ADD; plus the light-from-heavy ladder (Ham
  only SAW and was enslaved; striker/curser a fortiori; ten tribes =
  the ten rebellious sons).
- Shemot Rabbah 30:3 — the אלה/ואלה OPERATOR AUDIT across all of
  Scripture (each site: what disqualified, what added) + the plene/
  defective תולדות audit (full only at Creation and Peretz) — a
  systematic operator sweep in the source — CONFIRM; the armed-escort
  image of the sandwich (laws before her, laws behind her, she in the
  middle).
- Periphery: Tanchuma Terumah 1 (knowledge-exchange is non-rivalrous —
  trade Zeraim for Nezikin, both end with two); Noach 15:4 (Shem's
  slaves exit in the seventh, Ham's never — the curse mapped onto the
  two-tier system); ShR 30:4 (laws NAMED for Moses); ShR 30:6 (fetus
  case granularity — block 2, ledgered); Midr. Tehillim 99 (justice
  makes peace).
PACE: bite 19 = 32 listings / 18.1k chars. Ledger 713 read (36.3%);
1,223 remain. Next: Shemot Rabbah 30:7+, then Tur/bench.

### Batch 20 digest (Shemot Rabbah 30:7-24, the Mishpatim petichta cycle — 17)
- ShR 30:9 — GOD'S OWN COMPLIANCE PROVED TECHNICALLY: the heretic asks
  "why doesn't God keep Shabbat?" — answer: carrying in one's OWN
  courtyard is permitted, and "heaven and earth are His courtyard"
  (the whole earth is full of His glory) — a private-domain argument
  showing the legislator compliant with His own statute — ADD
  (self-application, second witness w/ halakhic mechanics); the
  mitzvah-count ladder (Adam 6 → Noah 7 → Abraham 8 → Jacob 9 →
  Israel all) — incremental releases; the son gets the whole table.
- ShR 30:10 — STAFFING COMPROMISE: Yitro's judge-spec had FOUR traits;
  Moses "found only one" (men of valor, Exod 18:25 vs 18:21) — spec
  degraded in deployment; and the training gap: "you appointed them
  and they do not KNOW — go teach them" → ואלה המשפטים as the
  curriculum — ADD.
- ShR 30:11 — ⚠ PROMULGATION PRECEDES LIABILITY: David's "do not enter
  into judgment with Your servant" holds only "until the laws were SET
  IN ORDER before him"; the craftsman/layman arena pair — the layman
  is hurt "because no one taught him"; and the drunk-thug parable: Job
  retracts on seeing the governor JUDGE matrona/eparch/dux = Miriam,
  Moses, Isaac, Abraham, Jacob — even the patriarchs sat under the
  same din — equality-before-law + no-liability-without-promulgation —
  MAJOR-adjacent ADD.
- ShR 30:13 — the qualified scholar who REFUSES to judge ("I'm busy
  with my learning") is charged "as if you destroyed the world" —
  civic duty sharpened to the credentialed — CONFIRM+; creation ran on
  the judgment-name (אלהים throughout Genesis 1).
- ShR 30:15 — ⚠ EXECUTOR-OVERREACH doctrine: Egypt executed a DECREED
  servitude yet is punished for EXCEEDING its terms — "I was a little
  angry and THEY helped toward evil" (Zech 1:15) — an agent of a
  decree is liable for the excess beyond scope — MAJOR-adjacent ADD;
  the six-days/six-years parallel restated as the term's rationale.
- ShR 30:16 — IGNORANCE NO DEFENSE once promulgated: the killer "did
  not look in the Torah" where bloodshed's law is written; the king's
  edict parable ("did you not READ my diatagma?"); even a high priest
  executed for intentional murder; ⚠ CLAIM-HOLDING: Saul's blood-debt
  collected by the GIBEONITES — "the priests forgave him, the
  Gibeonites did not" — the injured class holds the claim; a state/
  clergy pardon cannot extinguish the victim's demand — ADD.
- ShR 30:18 — the MIRRORED-COURT architecture: "as the Sanhedrin sits
  on high before God" (Daniel: the court sat, the books were opened) —
  heavenly and earthly instances synchronized — ADD.
- ShR 30:19 — the whole Torah HANGS on justice; Sodom and Jerusalem
  each fell only on trespassing the din; ⚠ JUDAH'S CROWN: kingship
  awarded for the SELF-ADVERSE VERDICT (צדקה ממני "she is more right
  than I" — ruling against himself in Tamar's case while his elders
  covered for him) — judicial integrity as the qualification for the
  crown — ADD.
- ShR 30:20 — R. Yehoshua's encoding claim: every matter in the
  parashah has "its PENALTY at its side and its REWARD at its side"
  (ענשה בצדה ושכרה בצדה) — sanction and incentive shipped inline with
  each rule — ADD.
- ShR 30:23 — ⚠ THE CONDITIONAL GRANT: "God gave you the Torah only ON
  CONDITION that you practice the dinim (על מנת שתעשו את הדינין) — if
  you do not, He takes it back; if you do — 'I will RESTORE your
  judges as at first'" — the whole gift is a conditional contract
  whose condition is the judiciary; restoration ties to the venue
  doctrine — MAJOR-adjacent ADD.
- ShR 30:24 — the Shekhinah SITS BESIDE the true judge ("the Lord was
  with the judge") and withdraws + draws the sword on the partial one
  (שדון read "that there IS din"); charity DELAYS a decree
  (Nebuchadnezzar's 12 months, fell the moment he closed the
  storehouses); justice ADVANCES redemption (Jehoshaphat: appointed
  judges → "the battle is God's"); the cycle closes straight into
  כי תקנה עבד עברי.
- Periphery: 30:7 (5-oxen/4-sheep publicity calculus — chapter tail,
  ledgered); 30:12 Aquilas; 30:14 sin-fear storehouse; 30:17 the
  yetzer as self-prosecutor; 30:21-22 (idolatry-vs-zenut; the
  two-patients parable on Ezek 20:25's "statutes not good").
PACE: bite 20 = 17 listings / 22.5k chars. Ledger 730 read (37.2%);
1,206 remain. Next: rest of Shemot Rabbah + Tur + the bench.

### Batch 21 digest (IBN EZRA both recensions, 21:1-11 + crossrefs — 34)
- ⚠ IE Katzar 21:1 — the PARASHAH LAYOUT TOUR: "each law stands on its
  own, yet there is a semblance of connection" — then a full
  dependency-ordered walk of Mishpatim: the design principle is an
  ANTI-COERCION GRADIENT ("the principle: do no violence, coerce none
  weaker") running body → property → the powerless → HIDDEN violence
  (secret cursing, bribery, false report) → the calendar; the slave
  law is the ROOT CASE because "nothing is harder for a man than being
  in the power of a man like himself" — a medieval module-layout
  rationale with our block as entry point — MAJOR.
- IE 21:2 (both recensions) — the עברי-IDENTITY APOLOGETIC: documents
  the DENIERS (עברי = any Eber/Abraham line → Ishmael/Edom/Moab would
  qualify) and refutes: Scripture uses עברי only of Jacob's sons; Jer
  34's העברי defined by "his brother the YEHUDI"; Yonah's "I am an
  עברי" answers "of what PEOPLE"; the reductio — why would a non-
  Israelite serve six years when an Israelite serves to yovel?; "the
  confusions arose from האשה וילדיה, ועבדו לעולם, אם עבד יגח" — the
  rejected reading RECORDED WITH ITS REFUTATION; "on the sages we rely
  in all the commandments" — CONFIRM type-resolution method.
- IE Katzar 21:2:2 — plain sense would include the SELF-SELLER here
  ("or himself — for so it is written ונמכר לך — WERE IT NOT FOR THE
  TRANSMISSION") — pshat-vs-kabbalah divergence flagged, transmission
  wins — ADD.
- IE Katzar 21:2:4 — חנם extends to EXPENSES: "if his master spent on
  him — if he fell ill, on MEDICINES — he does not repay" — medical
  costs on the master, non-recoverable — CONFIRM+ (illness rule, third
  witness, now with expenses).
- IE Katzar 21:5 — the piercing preconditions are CONJUNCTIVE: "no
  piercing if even ONE condition is missing — love of master, house,
  wife, sons, good-for-him — like the rebellious son; AND THEIR WORDS
  ARE CORRECT" — all-conditions semantics endorsed from the pshat
  bench — CONFIRM+.
- IE Katzar 21:6 — אלהים = judges as GOD'S OFFICERS (פקידי אלהים) on
  earth — the delegation title etymologized; IE's OWN rationale: the
  piercing MARKS him (נסמן) and happens at the CITY GATE where judges
  sit — "to do the thing IN PUBLIC" (Boaz, rebellious son parallels;
  דלת = city-gate via דלתים ובריח) — converges w/ Lekach Tov's
  passersby rationale — ADD; pierced slave FREED ON MASTER'S DEATH
  ("HIM he serves" — no passing to the son) — CONFIRM.
- ⚠ IE Katzar 21:8 (+ 23:2) — THE ASMAKHTA MODEL stated as method:
  "there are known places the sages set as a KIND OF ASMAKHTA — while
  the PRINCIPLE they knew [by transmission]" — husband-inherits-wife,
  eldest-does-yibbum, one-sale-only, and even HALAKHAH-FOLLOWS-THE-
  MAJORITY are all: oral law known independently, the verse attached
  as SIGN AND MARKER (לאות ולזכר) — drash as mnemonic INDEXING, not a
  derivation engine — a competing compilation theory vs the Talmud's
  own derivation realism — MAJOR (project-level fork: derivation-
  realism vs anchor-nominalism; keep both models in the dual track).
- IE Katzar 21:10 — the pshat yields the FIELDS, the transmission the
  CONSTANTS: כסות "as it sounds — and the MEASURES we know from the
  words of transmission (דברי קבלה)" — shiurim live in the oral layer
  even where pshat is plain — CONFIRM; שאר bread-vs-flesh and עונה
  dwelling-vs-time etymologies recorded as lexical forks.
- IE Katzar 21:11 — the community as ENFORCER: בבגדו בה read "if the
  father betrays her, WE do not abandon her — we remove her from his
  power" (לא ימשול as directive to the court) — addressee-to-court,
  second witness — CONFIRM; early-exit loss on the BUYER: she matures
  before term → "he shall not seek money from the father for the
  remaining months" — no clawback — ADD.
- IE Deut 15:17-18 — long-range clause binding ("also for your amah
  do likewise" binds to the SEVERANCE clause though distant — "and
  many are thus"); משנה = the slave worked DOUBLE (day + night); the
  term ends at the START of the seventh year — argued from shemittah/
  Shabbat boundary structure — ADD (term-boundary semantics).
- IE long 21:1 + 20:21 — the laws are the covenant's CONDITIONS
  (תנאים): taught first, "if they accept them, He cuts the covenant"
  (Exod 24 ceremony after); נעשה ונשמע split mapped: "we will do" =
  the do/don't commands, "we will hear" = the mishpatim (case law) —
  acceptance typed by command-class; promulgation → ratification
  pipeline from the pshat side — ADD.
- Periphery: IE's attack on the word-swapper ("his book deserves
  burning"); the name-taxonomy (proper/species/collective); Yedei
  Moshe apparatus row.
PACE: bite 21 = 34 listings / 18.2k chars. Ledger 764 read (38.9%);
1,172 remain. Next: rest of the bench (Ramban expected), Tur.

### Batch 22 digest (IE long recension complete + asmakhta series + Ramban opens — 45)
- IE long 21:2 — "six years AND NO MORE"; exit at the START of the
  7th year OF HIS SALE "whatever year it be" — per-contract clock,
  bench witness; the two-ended קץ semantics (Jeremiah's "at the end of
  seven" harmonized: every span has two ends); tradition: MALES sold
  for theft, never females — CONFIRM.
- IE long 21:8 — ⚠ QERE-PRIORITY DOCTRINE stated generally: against
  the Gaon's "both ketiv and qere hold," IE rules "the second (the
  qere) alone is the truth — AND SO IN ALL OF THEM"; the grammarian's
  point: לא and לו are indistinguishable in speech — "as they are
  READ, so is their meaning" — a global rule for the ketiv/qere fork
  class — MAJOR-adjacent ADD; redemption priced against the NEAREST
  exit: "count the years worked and the distance to the seventh OR to
  the time she enters her own power — per the count is the redemption"
  — min() applied to PRICING — ADD.
- IE long 21:8 (asmakhta cont.) — the one-sale rule "we know FROM THE
  TRANSMISSION," the verse a marker; the Gaon's "עם = one man"
  rejected on collectivity grounds (עם/גוי/קהל never denote an
  individual — הגוי גם צדיק = the whole kingdom) — IE keeps the pshat
  "foreign PEOPLE" and the halakhah by kabbalah, in parallel — CONFIRM
  the dual-layer model.
- IE long 21:8:2 — bench fork on לא תצא כצאת העבדים: IE reads "she
  exits SOONER than the men" (before six, at her majority) — opposite
  polarity to the Mekhilta's no-tooth/eye-exit reading — fork-flag.
- IE long 21:11 — THREE READINGS of אין כסף tabled: the Talmud's
  yes-money-for-the-father דיוק; the Gaon's medical-expense reading
  ("she repays nothing for the medicines"); IE's "explanatory
  addition" (emphasis, like 'you shall die and not live') — plus his
  structural refutation of the triple-reading of "three" (the
  captive-wife a fortiori: even SHE can't be sold) — fork-table ADD.
- IE Lev 19:20 — cross-module identification fork: the designated
  shefachah (שפחה נחרפת) read as OUR amah pre-yiud, an Israelite
  ("not freed" = not yet in her own power) — vs the halakhah's
  half-freed Canaanite — fork-flag.
- IE asmakhta corpus mapped (Lev 22:7 sunset-purity, 23:40 etrog,
  21:2 kohen-mourns-wife, Num 27:11 husband-inherits) — "we BELIEVE
  the transmitters, for they do not contradict Scripture" + the
  anti-Sadducee etrog polemic — the model's breadth — CONFIRM.
- IE Exod 34:26 — AUDIENCE-SCOPED PROMULGATION: the mishpatim are the
  HIGH PRIEST's and the JUDGE-KING's required curriculum ("obligated
  to learn and know them"); the public's duties are the ones after —
  two-tier training spec — ADD.
- IE Lev 26:25/46 — the Sinai covenant = the Mishpatim book-of-
  covenant (the נעשה ונשמע day); covenant-corpus = Mishpatim + Behar —
  CONFIRM covenant frame.
- ⚠ Ramban Deut 16:18 — THE ORDINATION COLLAPSE: judges required in
  every city (in the Land; by district abroad, per Makkot) — but "in
  this time, since SEMIKHAH ceased, all Torah judgments are VOID —
  'before them and not before laymen,' AND WE ARE LAYMEN (אנן הדיוטות
  אנן); judgments abroad run only on the enactment 'WE ACT AS THEIR
  AGENTS' (שליחותייהו עבדינן)" — the entire post-ordination judiciary
  operates on an agency fiction delegating from the ordained — a
  degraded compatibility mode described by the system itself — MAJOR;
  Rambam-vs-Ramban fork on city-courts abroad preserved.
- Ramban Deut 15:1 — boundary precision: debt claimable on the LAST
  DAY of the seventh year, release fires at nightfall (pruzbul written
  on the eve of the following Rosh Hashanah, Tosefta) — instantaneous
  year-end trigger for the term-boundary registry — ADD (shemittah
  body = block 7, ledgered).
- Periphery: respect-morphology on אדונים (plural-of-majesty barred
  for God in certain forms); the "Canaanite"-wife = any resident
  nation (the seven are banned from being kept alive — label-vs-type
  refined); IE's שאר synthesis "food that SUSTAINS her flesh"; עונה
  from עת "time" with nun-elision grammar.
PACE: bite 22 = 45 listings / 18.1k chars. Ledger 809 read (41.2%);
1,127 remain. Next: Ramban on the block proper (Exod 21), then
Sforno/Chizkuni/Radak, Tur.

### Batch 23 digest (RAMBAN on the block — 14 long rows)
- Ramban Deut 19:19 (crossref) — ⚠ THE DIVINE CO-PROCESSOR ASSUMPTION
  DERIVES LAW: conspiring witnesses die for what they SCHEMED, not
  what was DONE — if the accused was already executed they go FREE,
  because the human verdict carries a heaven-backed correctness
  guarantee ("had he been righteous, God would not abandon him to
  their hand"; "God stands in the congregation of judges — He
  vindicates, He condemns") — a counterintuitive rule DERIVED from the
  runtime-assistance axiom; source-anchored at OUR 21:6 אל האלהים
  (Ramban says so explicitly) — MAJOR.
- Ramban 21:1 — ⚠ CIVIL LAW IMPLEMENTS "DO NOT COVET": "if a man does
  not KNOW the law of house/field/money, he thinks it his, covets and
  takes" — the property code gives the tenth commandment its
  boundary — MAJOR-adjacent (pairs w/ Maharzu's Decalogue-depends);
  לפניהם addressed to THE JUDGES ("should have said להם") — the
  ordained chain "the expert judges SEMUKHIM UP TO MOSHE RABBEINU";
  ⚠ CONSENT SEMANTICS SPLIT: both parties may ACCEPT a lay judge
  (קבלוהו עלייהו — his ruling binds); before gentiles NEVER, "even if
  their law matches ours in that matter" — arbitration-by-consent
  cures lay jurisdiction, nothing cures foreign jurisdiction — MAJOR.
- Ramban 21:2 — why the slave law LEADS the code: the 7th-year release
  commemorates the Exodus (the First Commandment's preamble), the
  creation-Shabbat, and yovel — "the seventh is chosen in days, years,
  and shemittahs — ALL ONE MATTER, the secret of the days of the world"
  — the 7-clock as a fractal constant at every scale; Jeremiah's
  breach → exile parallel to the land's shemittah-exile — CONFIRM+;
  his ordering tour ("all the sections in correct order and intent").
- Ramban 21:3 — ⚠ THE SUBSTITUTION MODEL in full: the master "ENTERS
  IN THE HUSBAND'S PLACE" — takes handiwork, owes maintenance, the
  husband's exact package; the wife keeps her walk-away right; and the
  master's statutory duty EXCEEDS the husband's baseline (husband's
  maintenance-duty is rabbinic per Ketubot 49 — "but since it is the
  way of all the land, God commanded the buyer to be LIKE A MERCIFUL
  FATHER"); Mekhilta deRashbi's exclusion table quoted: arusah,
  shomeret-yavam, a wife FORBIDDEN to him (fit-to-remain predicate),
  a wife taken WITHOUT the master's consent (consent parameter);
  children's handiwork NOT the master's (הוא blocks the K"V); and the
  AUTONOMY FLOOR: "do not separate him from his wife" — the master
  cannot force the shefachah over the wife, "the matter is in the
  SLAVE'S power" — MAJOR.
- Ramban 21:6:1 — אלהים at our verse = "God is WITH THEM in judgment —
  He vindicates, He condemns" (Yehoshafat; ShR 30:24 cited) — the
  co-processor doctrine anchored at the block — CONFIRM+ (source of
  the Deut 19:19 back-reference).
- Ramban 21:6:2 — the mystical layer under the olam-rebinding: "the
  ENLIGHTENED will understand — לעולם is AS IT SOUNDS: one who serves
  to yovel has served all the days of the WORLD" (olam = the 50-year
  world-cycle; Rabbi: "olam is fifty years") — the word's true
  referent, not an override; jab at IE ("forgot what he himself wrote
  elsewhere") — ADD.
- Ramban 21:7 (via BeHaG) — ⚠ THE EXIT-CLAUSE INVERTED INTO A
  PROTECTIVE LAV, riding a meta-rule: Canaanite tooth/eye release is a
  PENALTY and "WE DO NOT DERIVE FROM PENALTIES" (אין למדין מן
  הקנסות) — so לא תצא instead WARNS THE MASTER: he may not expel her
  with the injury as her payout — he pays limb-damages AND keeps her
  toward designation ("often the damages exceed her remaining
  work-value"); possibly expulsion itself forbidden until term; "per
  this view לא תצא counts among the 365 prohibitions" — damages
  decoupled from release + anti-expulsion — MAJOR.
- Ramban 21:8 — the Mekhilta's court-warning read as a REAL
  GENTILE-SALE BAR (needed because the MALE can be sold to a ger
  toshav, Lev 25:47): it blocks the workaround of a father selling her
  to a gentile "for a year or two" to force her out of the
  non-designating master's hands — "this is CERTAINLY the pshat"; the
  no-second-sale rule then rides the REDUNDANT בבגדו בה; the
  re-punctuation method paralleled (Deut 14:21); the AILONIT edge case
  — no naarut window ever, so the bogrut-exit needs its own source
  (the two-exits derivation, Kiddushin 4a) — ADD; ⚠ HIS OWN pshat:
  the purchase IS presumptive marriage — "she is designated to him BY
  DEFAULT (מן הסתם)"; once he says 'I do not desire her' it is
  FORBIDDEN to leave her in his hand — the father MUST redeem; "every
  sale of a daughter is a betrayal" — yiud as the sale's default
  state — MAJOR.
- Ramban 21:9 — pshat option: yiud-to-son = betrothal arrangement and
  כמשפט הבנות = DOWRY ("as a man does for his daughters… like the
  severance grant — all kindness from Him"); "per our rabbis — AND IT
  IS THE TRUTH"; then the שאר essay AT SOURCE: his lexicon (שאר =
  kin-flesh), the pshat critique ("man lives on BREAD — why name
  flesh?"), conclusion: all three words = one intimacy-protection
  clause (closeness of flesh / bed-covering / timed visit; "Scripture
  speaks of intimacy in clean, brief language"); food+clothing =
  rabbinic enactments — the mega-fork's Ramban side confirmed at
  source (three duties → one duty in three aspects).
- Ramban Deut 21:13 (crossref) — the captive-wife: "the TORAH ACQUIRED
  her to him" — statute-as-kinyan, marriage created by law without an
  instrument; Bavli (first-biah permitted) vs Yerushalmi R. Yochanan
  ("neither first nor second — only after ALL the procedures")
  preserved; her wife-status glossed by OUR שארה כסותה ועונתה — ADD.
PACE: bite 23 = 14 listings / 19.5k chars. Ledger 823 read (41.9%);
1,113 remain. Next: Ramban 21:10-11 tail if any, Sforno, Chizkuni,
Radak, Tur, formalizers.

### Batch 24 digest (Ramban covenant/compilation rows + Sforno opens — 18)
- Ramban Exod 24:1 — THE ENACTMENT CEREMONY in order (against Rashi's
  out-of-order reading): Decalogue → same day Mishpatim to Moses →
  recounted to the people (ויספר "recounts" only NEW content — lexical
  proof these aren't the Marah/Noahide laws) → oral consent ("we
  believe in your words") → WRITTEN that day → next morning altar,
  sacrifices, blood HALVED, the book READ ALOUD, second consent
  (נעשה ונשמע) → blood sprinkled — "the sign of the covenant: the two
  enter in EQUAL PARTS" — promulgate → consent → write → public
  reading → ratify → bilateral blood-seal — CONFIRM+ the ratification
  pipeline with the equal-halves bilateralism.
- Ramban Lev 25:1 — ⚠ THE TWO-PASS COMPILATION MODEL: "what has
  shemittah to do with Sinai?" — its GENERALITIES (כללות) stand in
  Mishpatim (Exod 23:11), its DETAILS (פרטים ודקדוקים) in Behar — and
  the verse teaches ALL commandments follow this pattern; Torat
  Kohanim tail: "NO PROPHET MAY INNOVATE ANYTHING FROM NOW ON" — the
  canon CLOSED at Sinai (the freeze rule at source, pairs w/ לא
  בשמים) — CONFIRM+; plus COVENANT VERSIONING: v1 (blood, equal
  halves) voided by the calf "as if annulled," v2 at the second tablets
  with OATHS AND CURSES (same laws + the shemittah details, harsher
  enforcement), v3 at Moab — re-ratification after breach — MAJOR-
  adjacent ADD.
- Ramban Lev 18:4 — the mishpatim's PURPOSE FUNCTION: "given for the
  LIFE of man, the SETTLEMENT of lands, the PEACE of man"; וחי בהם →
  pikuach nefesh overrides Shabbat (life-preservation as top override
  priority); the rationally-required class ("had they not been
  written, right to write them"); four-tier incentive model by intent
  — ADD.
- Ramban Lev 21:12 — even the derivation-realist files some rules
  under ASMAKHTA: the HP-funeral-procession rule is "a rabbinic
  elevation, attached to the verse in the way of the Talmud's
  asmakhtot" — the two compilation theories COEXIST PER-RULE, not
  per-school — ADD (key nuance for the IE-fork).
- Ramban Num 11:16 — WHY SEVENTY(+1) JUDGES: the Sanhedrin's size
  mirrors the seventy angel-princes + the One ("that the Shekhinah
  rest on them as in the upper camp"; explicitly back-referenced to
  our 21:6); Psalm 82 read as the judges' charter: "you are elohim…
  pervert justice → die like Adam, FALL like a prince" — the court's
  SIZE as a mirror-constant of the heavenly host — ADD.
- Ramban Num 30:3 — (block 9, ledgered) the vow/oath TYPE SYSTEM:
  NEDER binds the OBJECT (חפצא), SHEVUAH binds the PERSON — so vows
  can attach to mitzvah-objects (passively overriding positive
  commands) while oaths never touch mitzvot; vows need a real object
  (none on intangibles); oath-to-keep-a-mitzvah = self-spurring only —
  ADD.
- Sforno 21:1 — third witness on covet-implementation: the mishpatim
  are how "a man KNOWS what is 'all that belongs to your fellow'";
  ⚠ 21:1:2 TYPE DISTINCTION: the mishpatim contain "no positive or
  negative command — rather, WHEN THE NEED TO JUDGE ARISES, judge in
  this manner" — commands are imperatives, mishpatim are CONDITIONAL
  PROCEDURES (if-then handlers) — MAJOR-adjacent ADD.
- Sforno 21:7-8 — the ETHICAL OVERLAY above the legal floor: "not
  fitting for a DECENT man to buy an עבריה except to marry her (self
  or son), the purchase-money as kiddushin"; and anti-forced-marriage:
  if she displeases him he should NOT marry her "lest he hate her" —
  father and master strive to redeem instead; בבגדו glossed by Rachel/
  Leah's "we are counted as FOREIGNERS, for he has SOLD us" (Gen
  31:15) — the sale estranges the father — ADD (+ Gen 29 mohar
  economics as settlement-link candidate: Jacob's seven years = the
  bride-price custom, cites our 22:16).
- Sforno 21:9-10 — the son owes the triple "though HE did not buy nor
  betroth her" (duties attach to the inherited designation); ⚠ the
  POLYGAMY-CAPACITY RULE: "one may not multiply wives except where he
  can SUSTAIN them (Yevamot 65a) — such that he not diminish what is
  due the first" — אם אחרת as a resource-constraint precondition —
  CONFIRM+.
- Ramban 21:11 — brief: the three = yiud/son/redemption; her free-exit
  "like the exit of the slaves mentioned."
PACE: bite 24 = 18 listings / 18.5k chars. Ledger 841 read (42.9%);
1,095 remain. Next: Sforno tail, Chizkuni, Radak, Bekhor Shor, Tur.

### Batch 25 digest (Sforno tail + Radak crossrefs + CHIZKUNI complete — 55)
- Sforno Num 6:13 (+Lev 13:2) — GRAMMATICAL VOICE AS POWER-MARKER:
  passive "brought" (מובא) marks one acted on by a superior — the
  leper, the sotah, OUR SLAVE (והגישו אדוניו — "no prisoner frees
  himself"); the nazir alone "brings himself" — our verse cited as the
  type case — ADD.
- Radak Ps 34:18 — our block's clauses as the GRAMMAR-BOOK examples of
  non-adjacent antecedent resolution ("refers to the righteous
  mentioned earlier — like ואף לאמתך תעשה כן and ואם שלש אלה לא יעשה
  לה") — long-range binding canonized — CONFIRM+; Radak lexicon:
  אלהים = judges (even "the nations judging Israel in exile"); לעולם
  = long-bounded time.
- Chizkuni 21:1 — the אלה/ואלה operator given an EXCEPTION CLASS
  ("don't object from terminal אלה המצות — there the topic CONCLUDES,"
  סליק ענינא — scope-end vs scope-open semantics) — ADD; Decalogue =
  prohibitions WITHOUT penalties, Mishpatim = the SANCTIONS TABLE
  ("returned and specified their punishments") — CONFIRM; his
  compilation claim: the slave block "belongs with Behar" (ואלה adds
  on the Behar laws).
- Chizkuni 21:1:2 — ⚠ enforcement-delegation GENERALIZED: "not before
  Canaanites even if EXPERTS; but if Israel judged first and he did
  not OBEY (לא ציית דינא), it is permitted to coerce him VIA the
  Canaanites until he does what Israel's judges decreed" — foreign
  muscle as execution layer for ANY domestic judgment — CONFIRM+
  (third witness, now general).
- Chizkuni 21:2:4 — ⚠ SENIORITY OF LIENS as the release's legal
  theory: "I brought them out — they are MY slaves, not free to sell
  themselves — MY DOCUMENT PRECEDES ANY OTHER DOCUMENT (שטרי קודם
  לשטר אחרים)" — God's prior lien makes every slave-sale a junior
  encumbrance that must terminate — MAJOR-adjacent ADD.
- Chizkuni 21:2:5 — the three exit-instruments contrasted: Hebrew male
  leaves with NOTHING required; Canaanite needs a manumission
  document; the amah's exit carries the deduction — CONFIRM.
- Chizkuni 21:3:2 — ⚠ INCENTIVE-DESIGN reading of the no-shefachah-
  for-singles rule: "lest he grow attached to the shefachah and say
  'I love my master and my wife' and serve to yovel — the married one
  longs for his Jewish wife and won't say it" — the precondition
  engineered to keep the perpetuity branch unattractive — MAJOR-
  adjacent ADD.
- Chizkuni 21:3:3 — the cross-lending operator BY NAME: wife's
  maintenance written here, children's in Behar — "learn this from
  that and that from this, GIVE WHAT IS SAID OF THIS IN THAT" (ליתן
  את האמור של זה בזה) — CONFIRM.
- Chizkuni 21:4 — contradiction FLAGGED and left standing (חז"ק): the
  shefachah permission vs Onkelos's לא יהיה קדש = "no Israelite shall
  take a slave-woman" — fork-flag; יתן לו as ownership-predicate
  (could not "give" an Israelite — no such power) — CONFIRM.
- Chizkuni 21:6:2 — ⚠ THE PIERCING AS TAMPER-EVIDENT CREDENTIAL: ear
  and door pierced TOGETHER form a height-matched LOCK-AND-KEY pair —
  "if he flees, the ear's bore proves him his master's WHEN IT MATCHES
  THE DOOR'S; and the master cannot claim another slave, for the two
  bores' heights will not both match" — a physical ID with a
  verification protocol — MAJOR (Chizkuni's own mechanical reading);
  21:6:4 anti-spoofing ("he cannot say 'I injured myself'"); 21:6:3
  status-legibility (so none mistake him for a Canaanite); text-
  critical precision on WHICH commandment the ear heard (must be the
  PLURAL לא תגנבו — property theft, sale-triggering — not לא תגנוב
  kidnapping) + the re-purchase reading fixing the Sinai-timing bug —
  ADD; מרצע gematria 400 = the shortened-decree rationale (periphery).
- Chizkuni 21:7 — ⚠ DEAD-CODE ANALYSIS answers the half-hekesh
  question: why doesn't the male exit by signs? — the clause is
  UNINSTANTIABLE: a minor's self-sale is void, the father cannot sell
  a son, a grown self-seller has already brought signs — no reachable
  state can fire the rule, so the hekesh needn't carry it — MAJOR-
  adjacent; pshat layer: "the Torah taught DEREKH ERETZ — she shall
  not be an errand-runner like a slave sent about day and night; her
  work is INSIDE ('the king's daughter's honor is within'), and she is
  a minor" — dignity-of-work rule — ADD; alt-pshat: she exits WITH
  standing — "if you want offspring from her, YOU marry her — she
  leaves only with GET AND KETUBAH like the other daughters."
- Chizkuni 21:8:4 — the flat-deduction rule stated AGAINST the value
  curve: she is worth MORE in the last three years (grown, skilled)
  than the first (small child), yet "do not reckon her later worth —
  deduct 1/6 per year served" — anti-appraisal made explicit,
  completing the Taz's three-function point — CONFIRM+.
- Chizkuni 21:10-11 — עונתה = DWELLING fork recorded (food, clothing,
  RESIDENCE as the alternate triple, the מעון etymology); "three" —
  BOTH allocations recorded side by side; אין כסף via the YERUSHALMI:
  "if she fell ill at the end of six and he provided her food — she
  repays NOTHING" — the illness-expense rule, Yerushalmi witness —
  CONFIRM.
- Genesis joins (settlement-link candidates): Sforno Gen 30:6 — the
  matriarchs' DECLARATION freed the handmaids (overriding האשה
  וילדיה, so all twelve sons inherit); Chizkuni Gen 21:14 — Abraham
  SENT Hagar away, could not SELL her having lain with her (the
  captive-wife rule applied) — Gen 16/21/30 ↔ Exod 21:4/8 — ADD.
- Chizkuni 21:9 — כמשפט הבנות = ceremony standard ("fine betrothal,
  fine wedding, fine bridal home like the land's daughters — not
  shefachah-marriage") — variant recorded.
PACE: bite 25 = 55 listings / 18.1k chars. Ledger 896 read (45.7%);
1,040 remain. Next: rest of Chizkuni crossrefs, Bekhor Shor, Tur,
formalizers.

### Batch 26 digest (Kitzur Ba'al HaTurim + Tur HaArokh + TUR EH 70/72/76 deployed code — 39)
- ⚠ Kitzur Ba'al HaTurim — the ENCODING-LAYER claim as such: legal
  metadata read from letters, numbers, masorah-concordance, and
  adjacency — MAJOR cluster: the notarikon PIPELINE in 21:1 (ואלה =
  "investigate the law"; המשפטים = settlement-first [2nd witness];
  אשר = "if BOTH parties CONSENT" — the consent condition on
  settlement in the next word; final letters spell מרמה "deceit" — the
  judge's FRAUD-PROBE duty); ועבדו by gematria+atbash = "not the son,
  not the daughter" (service-inheritance encoded numerically); אין
  כסף gematria = בסימנין "by signs" (the puberty-exit in the numeric
  value); וענתה DEFECTIVE → "the principal onah is Shabbat"; masorah
  concordance as hekesh-carrier: ויצאה pairs with the divorce-verse →
  amah acquired by document; בבגדו pairs with Potiphar's wife —
  R. Eliezer reads literal garment FROM there, R. Akiva maps betrayal
  BACK onto it (two-way semantics); כצאת 3× → the worker's day starts
  at SUNRISE (labor-law from a concordance); adjacency אין כסף ↔ מכה
  איש = no-double-liability (קם ליה בדרבה מיניה) — the LAYOUT carrying
  the rule.
- ⚠ Tur HaArokh 21:1 (R. Yosef Kimchi) — PROMULGATION AS CONTRACT
  FOUNDATION: "it says SET BEFORE them, not JUDGE them — that they
  know the law IN ADVANCE, so none can say 'had I known the slave
  serves only six years I would not have bought him,' or that the
  goring ox costs 30 shekels though the slave was worth 100" —
  published defaults underwrite price-formation; no ignorance-based
  rescission — MAJOR.
- Tur HaArokh 21:3 — second incentive-design witness + the SELF-SALE
  temptation: "a bachelor seeing a beautiful shefachah might SELL
  HIMSELF for her — the married man is not suspected of this" — the
  no-shefachah-for-singles rule guards the entry as well as the exit —
  CONFIRM+; his door-readings collect Chizkuni's bore-matching as one
  of three (public gate / guard-sign / anti-fraud).
- ⚠ TUR EVEN HAEZER 70 — the maintenance module DEPLOYED: eats with
  him what he eats; family-standard floor operationalized (עולה עמו
  "rises with him, never descends" — if ALL her family keep the
  standard he must match it; only the rich ones → not owed while she
  eats with him); the delegated-provision RATION (2 kav wheat/week,
  oil, legumes, figs, a silver ma'ah, Shabbat-eve together; her
  ration-savings HIS, surplus handiwork HERS) as a POOR-MAN'S FLOOR
  scaled by wealth; Rambam's locale-parameterized MEDIAN ("two daily
  meals of that city's bread — neither sick nor glutton"; wine only
  where the local women drink); CANNOT-PROVIDE → compelled divorce,
  ketubah as standing debt; the work-duty fork (R. Eliyahu: must hire
  himself out — from the ketubah's אפלח "I will work"; R. Tam: home
  estate-work only; Ramah middle: no compulsion, but earnings owed);
  the away-husband protocol (3-month presumption, award without
  death-proof or oath, no cosmetics allowance); volunteer feeder gets
  nothing ("placed his money on the deer's horn"); borrowed-with-
  witnesses → he pays, w/ the pre/post-award split and the "she could
  have pinched" defense the court will NOT raise for him (אין פותחין
  לו בטענה זו — the court does not argue the husband's case); the
  returning-husband oath-splits (Rashi/R"I/Rambam three-way); silence
  = consent to "your handiwork for your maintenance" (Rambam) — the
  block's first duty as a complete economic subsystem — MAJOR
  (deployment witness, forks preserved).
- ⚠ TUR EH 72 — VOWS CANNOT DEFEAT THE DUTY: "he vowed her benefit
  away — the vow does NOT take effect to void her maintenance, for he
  is ALREADY OBLIGATED (משועבד) and cannot expropriate it" — the
  pre-existing lien defeats the vow (anti-override registry, deployed
  witness); the 30-day bridge is a BROADCAST not an agency ("whoever
  feeds her loses nothing" — he may NOT appoint a direct agent);
  beyond 30 days → divorce + ketubah (lash-compulsion fork R"I vs
  R. Chananel) — CONFIRM+.
- ⚠ TUR EH 76 — the onah module DEPLOYED: the occupation table (idle
  rich nightly; in-town workers 2/wk; out-of-town weekly; donkey-
  drivers weekly; camel-drivers monthly; sailors 6-monthly; scholars
  Shabbat-eve); health-scaling (Ramah: per assessed capacity); TRAVEL
  NEEDS HER PERMISSION (and even then month-out/month-home; Ramah two
  home); JOB-CHANGE CONSTRAINT (no switching to a farther-onah trade
  without her leave, though it pays more — except to Torah study); the
  scholar-absence fork (Raavad/Ramah/Rosh, with the Rosh's "her tear
  is frequent, her wounding near"); waivable once procreation
  fulfilled (the waiver gate); polygamy "even a hundred — IF he can
  give each her three duties," sages cap at FOUR so each gets monthly
  onah — THE SCHEDULE ARITHMETIC DRIVES THE CAP; withholding onah to
  pain her violates the lav (Rambam); illness tolls six months max;
  the impossible-condition divorce cases — the third duty as a
  complete scheduling subsystem — MAJOR.
- Periphery: Chizkuni Behar-first compilation claim repeated; Num
  1:53/8:18 distributive-reading template ("one of these three");
  Kitzur BhT masorah on Joseph's garment.
PACE: bite 26 = 39 listings / 20.1k chars. Ledger 935 read (47.7%);
1,001 remain. Next: more Tur code sections / Bekhor Shor /
formalizers.

### Batch 27 digest (Tur OC 240 + Tur YD 267 — 2 giant rows, READ IN FULL)
- Tur OC 240 (conduct layer of the onah module): the INTENT GRADIENT
  (Raavad's four intentions, reward-scaled: procreation > fetal
  welfare > her desire/his departure = "the Torah's onah" > sin-
  avoidance); the debt framing ("not for his pleasure but as one
  PAYING A DEBT — he is obligated in her onah"); ⚠ the NINE TRAITS
  taxonomy of forbidden intents (coercion, hatred, ban, substitution,
  rebellion, quarrel, drunkenness, divorced-heart, confusion,
  brazenness) incl. the MARITAL-RAPE BAR ("one who compels his wife is
  called evil — he must appease first"); the consent floor: scheduled
  onot may never be REDUCED without her consent, INCREASE at her need
  is obligatory (Rava: gladden her even off-schedule); famine-year
  abstinence WITH THE CHILDLESS EXCEPTION (system-wide austerity
  overridden by unfulfilled procreation duty); modesty/timing/health
  interlocks (Rambam's excess warnings, readiness signs) — the third
  duty's conduct layer deployed — CONFIRM+.
- ⚠ TUR YD 267 — the COMPLETE deployed slave module (41k chars):
  * THE DORMANCY FLAG IN THE CODE: "the Hebrew slave DOES NOT OPERATE
    NOW, since it operates only when yovel operates" — module offline;
    and the Ramah's SHIM: a Jew war-captured and bought under דינא
    דמלכותא (the king's law) yields a THIRD TYPE — handiwork acquired,
    BODY NOT ("neither Hebrew-slave in full nor Canaanite in full") —
    quits by repaying like a worker; peacetime seizure → free, no
    payment — degraded compatibility type via secular law — MAJOR.
  * Circumcision decision TREE by acquisition mode (8th-day vs
    immediate; the R. Abba fork ruled BOTH WAYS STRINGENT — 8th-day
    for delay AND no Shabbat-override unless immersed-before-birth) —
    dual-stringency tiebreak on an unresolved fork — ADD.
  * Recalcitrant-slave protocol: condition-at-purchase permits
    keeping; consented-then-retracted → 12-month window then sell
    (Rashi vs Rav Hai INVERTED — fork preserved); forced-immersion
    validity fork (Rashi/Alfasi).
  * Rambam's ethics overlay: "TO SLAVERY Scripture gave them, NOT to
    humiliation… speak gently and HEAR HIS ARGUMENTS" — the dignity
    floor above the legal floor — CONFIRM.
  * Maintenance asymmetry: master may say "work for me and I won't
    feed you" (charity feeds him) — EXCEPT melog-slaves and famine
    years — vs the Hebrew slave's full-maintenance package — ADD.
  * No property capacity ("what the slave acquires, the master
    acquires") with the sole carve-out "on condition you go FREE with
    it"; chazakah-acquisition requires BODY-service (shoe/bathe/dress
    — sewing does NOT acquire) — the personal-service criterion.
  * LIMB-RELEASE casuistry: the 24 limb-tips enum; visible-deficit
    criterion (gouged blind eye frees — "he lacks a limb"; dimmed
    usable one doesn't); INTENT REQUIRED (stone-at-animal → no
    release; "paint my eye" doctor-master → frees; Tosafot contra);
    EXCLUSIVITY predicate (joint-owned/half-free don't limb-exit);
    and the DORMANCY AGAIN: limb-release = penalty → needs ordained
    judges → "we do not judge it today" (the seizure/confession
    workaround forked Raavad/Ramban/Rosh) — MAJOR (two dormant
    subsystems named in one code section).
  * The manumission-DOCUMENT sublanguage: valid performatives ("you
    are free / your own / I have no business in you") vs invalid
    ("permitted to all men"); TENSE SEMANTICS — עשיתי "I have made"
    valid, אעשנו "I will make" = promise, invalid; Ramah: יהא בן
    חורין "he SHALL BE free" valid despite future form — performative
    analysis in the code — ADD; freedom = benefit → acquirable for him
    without his knowledge (זכין), unless he protests.
  * All-property-grant poison pill: the slave frees himself inside the
    grant, but ANY reservation voids it all (he may be the reserved
    part); two slaves in one document → neither; property to TWO
    slaves → each half-free and THEY MUST FREE EACH OTHER — ADD.
  * Half-slave rules: by document void, by MONEY valid; pregnant-
    shefachah split (mother-free/fetus-slave VALID, inverse VOID);
    the half-slave COMPELLED manumission ("can marry neither → force
    the master, note for half his value") — human-flourishing
    overriding property — CONFIRM+ (block's marriage-capacity logic).
  * DEADLOCK STATE flagged: heirless convert dies, minor slaves not
    seized before maturity → "they have NO REMEDY" (no master's death
    to lapse the issur, no owner to free) — the code names its own
    unreachable-release state — ADD.
  * Conduct-based manumission: master MARRIES him to a free woman /
    lays tefillin on him / calls him to the Torah → FREED (acts by the
    master implying free status execute manumission); waived coercion
    on a slave-invalid vow → freed; Rambam generalizes: any utterance
    implying no remaining lien + resolved intent → compelled document.
  * Penalty releases: SALE TO A GENTILE → free, master fined up to 10×
    to redeem + document (evasion via forfeiture-loan closed —
    "flouted the enactment"); SALE ABROAD → free, buyer eats the loss
    ("he should have known"); "THIS RULE OPERATES EVEN NOW" — the
    land-tie stays LIVE while the Hebrew module sleeps; the ALIYAH
    compulsions (slave wants the Land → compel master to go or sell;
    master leaving → cannot drag the slave; runaway TO the Land NEVER
    returned — "even if the master says 'I'll serve him there,' we
    don't listen, lest he lure him back") — territorial supremacy
    dissolving foreign-held title — MAJOR.
PACE: bite 27 = 2 listings / 32.7k chars (paged via cut/python).
Ledger 937 read (47.8%); 999 remain. Next: more Tur/codes rows, then
formalizers.

### Batch 28 digest (Taz CM 348 + Rabbeinu Bahya — 14)
- Taz CM 348 — the theft-verse allocation defended by דבר הלמד
  מענינו (context-inference): the Decalogue's singular לא תגנוב sits
  among capital crimes → kidnapping; the plural לא תגנובו = property
  theft; had only one been written it would read as property — the
  doubling forces the split — CONFIRM (pairs w/ Chizkuni's precision
  on which verse the pierced ear heard).
- ⚠ Rabbeinu Bahya Bamidbar 12:14 — the COMPLETE 13-middot catalog
  with worked examples, and middah #9's canonical case IS OUR BLOCK:
  the amah "left the general rule to assert a new claim unlike its
  context — to LIGHTEN and to WEIGHTEN" (lighter: exits within six by
  signs/master's-death; heavier: "her master betroths her against her
  will") — subclassing with override documented, our block as the
  textbook example — CONFIRM+; middah #6: slaves excluded from
  bailment/oath law because "COMPARED TO LAND" (והתנחלתם — slaves
  typed as real property for those modules) — ADD.
- ⚠ RB Shemot 21:1:4-5 — the forum rule's SEVERITY MODEL: gentile-
  court litigation = a root sin containing two worse-than-murder
  components — (a) chillul Hashem ("our enemies as judges" = tribute
  to their god; repentance+Kippur+suffering only SUSPEND, death alone
  scrubs), (b) ⚠ THE UNRETURNABLE-THEFT TRAP: "whatever he extracts
  via their courts is full THEFT — and he does not even THINK it
  theft, so he never returns it, SO HE IS NEVER FORGIVEN" — a sin
  unrepentable BY CONSTRUCTION (no restitution because no awareness)
  — MAJOR; Rashi's לפניהם = the SEVENTY who stood at the mountain
  BEFORE Sinai (the pre-revelation court) + "we are laymen acting as
  their agents" (4th witness on the agency fiction).
- ⚠ RB 21:1:5 (end) — THE REASONED-OPINION REQUIREMENT from תשים:
  the judge must set the RATIONALE before the litigant — "'write for
  me from what REASON you judged me' — they write and give him"
  (כתבו לי מאיזה טעם דנתוני) — written appealable judgments in the
  code — MAJOR.
- RB 21:1 (Solomon) — the Writings as SANCTIONS-SUPPLEMENT: "the
  Torah warned (no favoritism) but did not punish; Solomon came and
  taught the penalty" (cursed by the peoples, both worlds) — a
  post-Torah layer adding enforcement to bare prohibitions — ADD;
  justice = the Throne's foundation; judgment reserved to the SAGES.
- RB 21:1:7 — תשים read as סם: right judgment = ELIXIR OF LIFE, wrong
  = DEADLY POISON (סם חיים/סם המות) — the code as pharmakon, keyed to
  execution quality — ADD.
- RB 21:2:4 — ⚠ CROSS-CORPUS CONSTANT-FETCH: the sick slave owes
  nothing (no idle-fee, food, or doctor — חנם) UNLESS the illness
  exceeded THREE YEARS — the cap imported via the hekesh-to-hireling
  from ISAIAH 16:14 "in three years, AS THE YEARS OF A HIRED HAND" —
  a numeric parameter fetched from a prophetic verse — MAJOR-adjacent
  ADD; יעבוד = dignified work (hired-hand hekesh: at his TRADE, by
  DAY not night) — CONFIRM.
- RB Devarim 15:17 — the THREE canonical non-adjacent bindings listed
  together (לאמתך → severance; שלש אלה → yiud/redemption; זרחה השמש
  → the five-oxen clause) — the long-range binding class — CONFIRM+;
  15:12 the Re'eh patch reading (3rd witness); Moses-as-slave
  litigation (3rd witness, w/ "the book of Adam's generations" as the
  controlling decree-document); Tamar's three pledge-items allegorized
  as the triple (Gen 38 ↔ 21:10 — settlement-link candidate,
  periphery).
PACE: bite 28 = 14 listings / 18.0k chars. Ledger 951 read (48.5%);
985 remain. Next: rest of Rabbeinu Bahya on the block, Bekhor Shor,
formalizers.

### Batch 29 digest (Rabbeinu Bahya block-rows complete + R. Yonah Avot + BEKHOR SHOR — 36)
- RB 21:3:2 — the EXIT TABLE tabulated: male slave self-acquires by
  FOUR (six years / yovel / master's death / deduction); the PIERCED
  by TWO (yovel / master's death); the AMAH by FIVE (adds signs; never
  pierced) — clean numeric table — CONFIRM.
- RB 21:5 — the bilateral-love MATRIX with per-word anchors: master
  loves him, he doesn't → no piercing; he loves, master doesn't → no
  (כי טוב לו); master ill, he well → no (עמך); he ill → no — four
  conjunctive rows each tied to its word — CONFIRM+; "while a SLAVE"
  timing predicate (saying it after exit is void).
- RB 21:6:2 — personal-performance extended: "not his son, not his
  agent, NOT THE COURT'S AGENT" — even the court officer excluded —
  CONFIRM+ (3rd witness); "his ear, not hers"; the definite-article
  instrument spec ("THE awl — the designated one of awls");
  piercing-by-anesthetic (סם) VALID post-facto though blood usually
  flows — the blood is rationale (answers the doorpost-blood of
  Egypt, measure-for-measure), not requirement — ADD.
- ⚠ RB 21:8:2 — the DEEPEST statement of the two-channel text: the
  R. Eliezer/R. Akiva fork on בבגדו runs on WHICH CHANNEL IS
  AUTHORITATIVE — יש אם למקרא (the vowel-READING rules: בְּבִגְדוֹ "in
  his GARMENT" — spread his tallit = kiddushin; betrayal would demand
  the בְּבָגְדוֹ vocalization) vs יש אם למסורת (the CONSONANTAL
  skeleton rules: betrayal, as a מקור form); R. Shimon rules BOTH
  channels operative (אם למקרא ולמסורת) → both laws derived —
  pointing and skeleton as separate authority layers with a
  both-channels ruling — MAJOR-adjacent CONFIRM.
- RB 21:9 — the master IN LOCO PARENTIS: if yiud goes to the son, the
  MASTER gives her a dowry "like the virgins' mohar, for she is a bat
  Yisrael and the master stands in her FATHER'S place" — kindness-
  class command like the severance — CONFIRM+.
- RB 21:11 — the BIDIRECTIONAL no-claims parse: חנם bars the master's
  refund-claim against the father at signs-exit; אין כסף bars HER
  money-claim against him ("no ketubah — he never married her") — the
  double negation allocated to the two claim-directions — ADD.
- RB Vayikra 24:22 — justice-abandonment = "removing oneself from
  God's divinity, denying the Root"; ⚠ "all the nations' faiths and
  their laws are COMMENTARY ON THE TORAH (פירוש התורה הן)" — gentile
  legal systems as derivative works; bystander-liability ("those who
  can protest and don't — profane the Name") — ADD.
- R. Yonah Avot 1:1 — the judicial NEGLIGENCE STANDARD: the hasty
  ruler is "close to WILLFUL" (שגגת תלמוד עולה זדון — study-error
  counts as intent); the FERMENT method (מחמיצין את הדין — delay
  breeds the insight the first pass missed); judging the poor = "THAT
  is knowing Me" (Jer 22:16) — CONFIRM+ deliberateness rule.
- BEKHOR SHOR (pshat bench): 21:1 — office-eligibility parallel: as
  the KING must be "from among your brothers, not a foreigner," so no
  gentile JUDGE over Israel — ADD; pshat addressee = Yitro's
  just-appointed judges; 21:2 — the lien doctrine from the pshat bench
  (קדם שטרי לשטר אחרים, 2nd witness); ובשביעית economic pshat: "in
  the seventh he doesn't plow/sow/reap — little work needed" — the
  release timed to agricultural idleness — ADD; 21:6:2 — ⚠ the
  MASONRY pshat: houses are STONE, an awl cannot pierce stone — the
  door/doorpost specified as the pierceable WOOD substrate (+
  publicity) — material-constraint reading — ADD; piercing = the
  PERPETUITY MARKER ("sign he won't exit at the sevenths"); 21:7 —
  childless-exit reading 2nd witness ("she does not leave WITHOUT her
  children — want offspring? marry her; she leaves only by get and
  ketubah"); לעם נכרי = no breeding her to his CANAANITE slave (the
  symmetry-bar, 2nd witness); 21:10 — ⚠ the EQUAL-TREATMENT
  rationale: "let him not say 'this one I bought as a slave, that one
  came free — I'll honor the free one' — her triple may not be
  diminished from the other wife's" — anti-discrimination across
  wives of different origins — CONFIRM+.
- RB exit-cosmology: עולם=50 via the LEVITE window (Num 8:24, 25→50,
  Samuel's 52 computed) + the 49,000-year cosmic yovel (all returns
  to the Source) — the constant 50 as cosmology — ADD-periphery.
PACE: bite 29 = 36 listings / 18.0k chars. Ledger 987 read (50.3%) —
PAST HALFWAY. 949 remain. Next: formalizers (Malbim/HKV/Netziv),
acharonim, apparatus.

### Batch 30 digest (Bekhor Shor tail + MINCHAT SHAI masorah + Abarbanel crossrefs — 20)
- ⚠ Minchat Shai 21:8 — the KETIV/QERE REGISTRY ENTRY: אשר לא יעדה is
  "one of THREE in the Torah written alef (לא 'not'), read vav (לו
  'to him'), recorded in the masorah at Shemini — AND ALL OF THEM COME
  FOR DERIVATION (וכולהו אתו לדרשא)"; the derivation mechanics: the
  לא is REDUNDANT (obviously she wasn't designated — else get needed
  and no father-redemption) → "since Scripture deviated, learn" — the
  deviation-triggers-derivation principle applied to the two-channel
  text, with a MAINTAINED INDEX of members (+ Nakh parallels) —
  MAJOR-adjacent CONFIRM (the fork tracked since Onkelos now has its
  registry).
- ⚠ Minchat Shai Zech 2:12 — the TIKKUN SOFERIM essay: the EIGHTEEN
  "scribal emendations" listed in full, and the corpus's own debate
  over its amendment history: (a) the Great Assembly ACTUALLY CHANGED
  the text (R. Natan/Arukh/Yelamdenu) vs (b) Rashba et al.: "far be it
  that the scribes add or subtract even ONE letter — they DISCERNED
  that Scripture itself wrote euphemistically" (annotation, not
  patching); the Ikkarim's "no forger announces his forgery"; R. Yosef
  Karo's royal-scribe protocol (the transcriber adjusts dictation to
  honorific form); סופרים etymologized as COUNTERS of letters — the
  source-integrity question debated inside the apparatus itself —
  MAJOR.
- Minchat Shai block rows — letter-level checksums on our verses:
  cantillation (zakef on המשפטים), dagesh collations (ובשבעת, וילדה
  לו vs the Michlol), vowel/accent manuscript comparisons (יתן לו),
  kamatz-chatuf (שלש), no-makkef (לא יעשה); the doubled-form
  morphology rule (ענה תענה, נקה לא ינקה: first kamatz, second
  patach, per an old grammar MS) — the apparatus maintaining the
  block at single-mark resolution — CONFIRM.
- Bekhor Shor 21:11:3 — the AILONIT edge case from the pshat bench
  ("no naarut when she reaches bogeret age" — אין כסף covers her) —
  2nd witness of the Kiddushin 4a derivation.
- Abarbanel II Sam 13 — the block's DESCENT RULE deployed in
  narrative-legal criticism: against the sages' Tamar-dodge
  (conceived pre-conversion → not Amnon's legal sister), he argues
  "the woman and her children shall be her master's" holds because
  the mother REMAINS in slave status — a child BORN after conversion
  in holiness cannot be judged a gentile; plus the physicians'
  objection; his own resolution (both post-conversion; Tamar's plea
  was evasion) — ADD.
- Abarbanel misc — Ralbag: kingship "עד עולם" = bounded-olam "like
  ועבדו לעולם" (the constant in political theory); the Tekoa woman's
  לעם נכרי cited by "some grammarians" for עם-as-individual (the
  collectivity fork from the other side); אדונים קשה honorific-plural
  anchored on our אם אדוניו; the Guide's אלהים taxonomy (judges +
  separate intelligences as "judges/influencers") sourced at OUR
  והגישו אל האלהים — CONFIRM delegation-title ontology.
PACE: bite 30 = 20 listings / 19.8k chars. Ledger 1,007 read (51.3%);
929 remain. Next: more acharonim/apparatus, formalizers.

### Batch 31 digest (Abarbanel essays — 4 long rows)
- ⚠ Abarbanel Deut 24:1 — CANONICAL-SOURCE SELECTION: kiddushin law is
  NOT new in Deut 24 — it already stands IN OUR BLOCK (אשר לא יעדה /
  ואם לבנו ייעדנה: cash/document sale, yiud as positive command, the
  betrothal formula) — yet the sages derived marriage law from Deut 24
  "because they found the commandment COMPLETE and self-contained
  there, with all its conditions — not so in Mishpatim, where only
  parts appear (the amah, the seduced girl)" — derive from the most
  complete instantiation, not the earliest — a source-selection
  heuristic — MAJOR-adjacent ADD; plus the word-by-word divorce
  mechanics map (וכתב → he/agent writes; לה → hers; ספר כריתות →
  severing content; ושלחה → no further seclusion) and the consent
  asymmetry read from actor-attribution ("betrothed WITH her consent,
  divorced without").
- Abarbanel Exod 20:1 — the TWO SINAI CHANNELS: all ten heard and
  understood (with IE and "the rabbis" against Rambam/Ramban's
  degradation models), but only the first two verses (necessary
  existence + unity — the metaphysical axioms) were NEVER re-taught by
  Moses; everything else was RE-STATED in the legislation (his
  re-statement table: each Decalogue clause ↔ its Mishpatim/Leviticus
  echo) — direct broadcast for axioms, mediated restatement for law —
  ADD.
- Abarbanel Exod 21:1 essay (chapter-anchored; blocks 3-4 ledgered) —
  the GENUS/SPECIES compilation model from the philosopher bench:
  "the Torah stated the GENERA (סוגים); the SPECIES beneath them,
  unwritten for brevity, MOSES RECEIVED AT SINAI — and that is the
  ORAL TORAH" (אב/תולדה as genus/species with the oral law as the
  species table) — CONFIRM+; דבר הכתוב בהווה (rules generalize past
  their literal nouns); ⚠ deterrence economics endorsed (the Guide):
  the 5-ox/4-sheep fine scales with EASE OF THEFT (cattle disperse
  unguarded, sheep flock under a shepherd) — enforcement calibrated
  to detection probability; the rival talionic-compounding theory
  (each additional act — binding, driving, slaughtering, selling — a
  separate offense, proved from Achan's five-fold וגם) recorded;
  sale-term PROPORTIONALITY ("if the theft is small, he is sold only
  for the matching time"); sold for the PRINCIPAL only, never the
  penalty-multiples; his comparative-law polemic (nations hang or
  crop ears for theft; "God's law fines money for money, exactly
  measured"); the four-bailee walk with the oath as
  evidence-substitute BEFORE the elohim-court ("God stands in the
  congregation" — the co-processor again) and "the swearers do not
  collect" from ולקח בעליו.
PACE: bite 31 = 4 listings / 31.6k chars. Ledger 1,011 read (51.5%);
925 remain. Next: rest of Abarbanel, then formalizers/long tail.

### Batch 32 digest (Abarbanel on 21:2 and 21:7 + crossrefs — 5 rows)
- ⚠ Abarbanel 21:2 — the TERM AS THEOLOGICAL SIGNATURE: why six years
  and not ten or three? — the seven-structure is the Creation
  signature: "this law is not among the absolute rational rules — it
  has a DEEP SECRET in the world's creation… not so the Noahide laws
  nor the nations' laws" — the constant is deliberately NON-DERIVABLE
  from reason, marking revealed law off from rational law — MAJOR-
  adjacent; structural mirroring: as the Torah opens with Creation
  and closes with wonders, the mishpatim open with a Creation-
  memorial and close likewise.
- Abarbanel 21:2 — ⚠ DECALOGUE-PARENT FORK: he files the slave block
  under לא תרצח — "enslavement is MURDER IN LIFE" (as charity is
  called life, subjugation is killing; Jeremiah 34's measure-for-
  measure cited) — vs Ramban (under DO-NOT-COVET) vs Chizkuni
  (sanctions-table for the whole Decalogue) — the block's parent
  assignment is itself forked on the bench — ADD; his contrarian
  אלהים reading: "Scripture never calls the JUDGES elohim — rather
  THE PLACE where God's judgments are done" — a bench fork on the
  delegation title; self-seller MAY set any term (the fixed six binds
  only the court-sale); the comparative-law coda ("no nation makes
  the master feed the slave's wife and children").
- Abarbanel 21:7 — THIRD reading of לא תצא כצאת העבדים: she doesn't
  get the male's exit-PACKAGE (no husband-maintenance clause, no
  breeding assignment "for he may designate her only to himself or
  his son") — the clause as a DIFF STATEMENT on the marriage-related
  rules (vs Mekhilta's no-injury-exit and IE's exits-sooner) — the
  bench now holds three readings — ADD; the PURCHASE-PURPOSE
  presumption with the incapacity argument ("a man does not buy a
  little girl for labor — she cannot work, for the weakness of her
  mind and limbs — but to designate her; on that condition her father
  sold her"); resale carries the ORIGINAL term ("she exits at six
  from the FIRST sale"); the SUBJECTIVE-FOREIGNNESS variant of עם
  נכרי ("since this one sent her away, every other man is in her
  eyes like a foreign people"); both "three" readings recorded with
  priority ("the received one is the true one"), the grammatical
  alternative carrying BREACH-TERMINATES-CONTRACT ("if he diminishes
  her three duties she exits before the six, at any time, free");
  sides with Ramban: food is rabbinic.
- Abarbanel 32:33 — covenant-amendment history (the Mishpatim
  angel-clause withdrawn at the Tabernacle command, reinstated as
  punishment after the calf); a rare bench ATTACK on the resolver
  layer's motive: Onkelos's rendering of "I will not go up in your
  midst" criticized — "he aimed only to avoid corporeality and did
  not heed the verses' sense" — translation policy vs meaning — ADD.
PACE: bite 32 = 5 listings / 22.7k chars. Ledger 1,016 read (51.8%);
920 remain. Next: long tail (Abarbanel remainder, formalizers,
acharonim, apparatus).

### Batch 33 digest (Abarbanel tails + ADERET ELIYAHU/GRA + Eybeschutz + Alshekh — 17)
- ⚠⚠ THE GRA'S OVERRIDE MANIFESTO (Aderet Eliyahu 21:6:2): "the pshat
  of the verse — the MEZUZAH TOO IS VALID for piercing; but THE
  HALAKHAH UPROOTS THE SCRIPTURE (הלכה עוקרת את המקרא) — AND SO IN
  MOST OF THIS PARASHAH, AND SO IN MANY PARASHIOT OF THE TORAH; and
  this is of the GREATNESS of our Oral Torah, halakhah to Moses from
  Sinai, WHICH TURNS LIKE CLAY UNDER THE SEAL (מתהפכת כחומר חותם)…
  so with piggul, and MOST OF THE TORAH — therefore one must know the
  pshat, TO KNOW THE SEAL; and so with the awl" (Makkot 22b cited —
  "how foolish are they who stand for the scroll [and not the sage]")
  — the override declared THE NORM, not the exception; the same
  material reshaped by the oral seal; an exception class noted (the
  commandments "that came with straight final letters" unchanged);
  and the DUTY of pshat-knowledge exists precisely to see the
  transform's input — the strongest single law-as-code statement of
  the scan — MAJOR.
- ⚠ Gra 21:6:3 — the YOVEL AS GLOBAL OVERRIDE PASSAGE: לעלם "means
  literally forever — only the yovel passage RELEASES every
  'forever'-sale; the Torah legislated it in its own separate passage
  GOVERNING EVERYTHING" — not a word-rebinding but a cross-cutting
  release clause defined once, applying to all perpetuities —
  MAJOR-adjacent.
- Gra 21:7-8 — the TWO-LAYER doctrine in action: pshat layer — לאמה =
  the PILEGESH (concubine), יעדה = mere designation WITHOUT kiddushin,
  והפדה = the father takes redemption from a second pilegesh-taker;
  halakhah layer — yiud IS kiddushin; "and THIS is the poskim's
  dispute whether a pilegesh needs kiddushin" — the ketiv aleph read
  "he has NOT YET betrothed her"; both layers maintained in parallel —
  ADD; 21:11 — אין כסף pshat: no IOU — "she leaves completely and at
  once; she does not write a debt-note for her value (as the
  half-slave does)" — ADD.
- ⚠ Alshekh Deut 4:8 (+7:12) — the TWO-IMPLEMENTATIONS claim with its
  metaphysics: the nations' law-codes achieve the same civil ORDERING
  ("you could order society with either") but carry no
  holiness-quality; God's mishpatim, run as revealed code, EMIT — one
  who executes a judgment of God's "kindles a holy light above,
  CREATES a holy angel" — identical I/O, different side-effects; the
  reward is for choosing THESE (האלה) — the forum-exclusivity
  rationale given its ontology — MAJOR-adjacent ADD.
- Alshekh Deut 16:21 — the GRADIENT-ATTACK model: "who appoints an
  unfit judge — as one who PLANTS AN ASHERAH BESIDE THE ALTAR" (the
  judges sit by the altar — the venue doctrine); the escalation
  chains traced (favoritism → tilting → bribery; tree-by-altar →
  matzevah → blemished offering → idolatry) — corruption as
  incremental encroachment entering at the unfit judge — ADD.
- Eybeschutz (Ahavat Yehonatan) — the angels' claim fails on the
  block's DOMAIN ("have you an ox, a shefachah, a slave?"): the
  executable surface-law is the GARMENT that makes the Torah
  human-owned ("had He given only the inner part, the angels' claim
  would stand") — the applicable layer as title-deed — ADD-periphery.
- Aggadat Bereshit 78 — "God is KNOWN in His world only through
  judgment"; the flood generation destroyed for rejecting the
  mishpatim — periphery CONFIRM.
PACE: bite 33 = 17 listings / 21.1k chars. Ledger 1,033 read (52.7%);
903 remain. Bites 24-33 complete. Next strata: remaining acharonim
(Alshekh Exodus rows, Kli Yakar?, formalizers Malbim/HKV/Netziv),
apparatus long tail, then the 26 Tanakh crossrefs.

### Batch 34 digest (Alshekh on 21:1-4 — 3 long rows)
- ⚠ Alshekh 21:1:3-4 — COMPOSITION-CONSISTENCY as the divine code's
  distinguishing property (משפטי ה' אמת צדקו יחדיו "true, righteous
  TOGETHER"): the nations' laws look fine SEPARATELY but fail when
  composed ("the murderer dies AND the petty thief dies — set them
  side by side and the heart rebels: this took a life, that took
  money — why equal punishment?"); God's laws stay proportional under
  composition (life for life; the thief disgorges the mina he sought
  plus one of his own, "as he schemed") — laws must be valid jointly,
  not just pairwise-separately — MAJOR.
- ⚠ Alshekh 21:1:5 — TWO-COURT SYNCHRONIZATION extended to CIVIL
  outcomes: the Rosh-Hashanah decree allocates each person's wealth;
  a Torah-court ruling EXECUTES the allocation ("as He judged above,
  so it comes out below"); winning in a gentile court what Torah law
  denies = "the supreme judgment comes out PERVERTED — they overturn
  His judgment"; and the state reconciles anyway ("He makes WINGS for
  money taken against His judgment") — the lower court as executor of
  the upstream decree — MAJOR-adjacent.
- Alshekh 21:1:6 — the block as the PIETY CURRICULUM: Bava Kamma 30a
  "he who would be pious fulfills the laws of DAMAGES" — accepting
  Torah-ruled losses (freeing the slave at cost, shemittah wiping
  loans, "the Satan taunts Israel over these laws") trains the whole
  practice — ADD.
- ⚠ Alshekh 21:1:9 — the CO-SLAVES doctrine from the person-switch:
  the buyer addressed in SECOND person (כי תקנה — "you did a mitzvah:
  through you he repays his theft"), the thief kept in third; and "you
  are not acquiring a free man — you acquire one ALREADY A SLAVE [of
  God]; like one slave of a king buying his fellow — the purchase
  confers no ownership of the body, for both are one Master's
  slaves"; the six years are a divine GRANT ("by command he serves —
  otherwise he'd owe nothing"), and the release is SELF-EXECUTING
  ("you do not release him — HE GOES OUT of himself") — CONFIRM+
  auto-release with the agency analysis; the created-alone dignity
  derivation ("the world is created for EACH man — even this slave").
- Alshekh 21:3 — the INCOMPLETE-KINYAN argument: the owner's two
  possible benefit-streams (handiwork, offspring-via-shefachah) are
  BOTH blocked from fullness — no shefachah for the single man, and
  the handiwork isn't fully his, "for if it were, he would be exempt
  from feeding the wife" — the maintenance duty as structural proof
  the acquisition is partial (and the slave fares BETTER than an
  ordinary debtor, who repays while his family starves) — ADD.
- Alshekh 21:4 — the love-list as ESCALATION SEQUENCE: "first he says
  only 'I love my master'; from that follows 'my wife,' then 'my
  children,' then 'I will not go free'" — the verse's word-order as
  the yetzer's gradient (3rd witness on the incentive design); מרצע
  gematria = כנעני ×2 ("he became a Canaanite twice"); the TWO-BLOODS
  rationale (Pesach doorpost-blood + covenant-blood — he disowned
  both → his blood at the door); the timing answer (piercing punishes
  the CHOICE to stay, not the possibly-forced sale); body-soul
  allegory overlay (the nefesh as buyer, mitzvot as the master's
  children, the second-soul reading of אם אחרת) — periphery-plus.
PACE: bite 34 = 3 listings / 22.6k chars. Ledger 1,036 read (52.8%);
900 remain.

### Batch 35 digest (Ateret Zekenim + Avi Ezer + Bach + BARTENURA on Rashi — 31)
- ⚠ BACH CM 349 — the GENDER-PARITY CLAUSE anchored on our header
  verse: "one law for man and woman — from ואלה המשפטים אשר תשים
  לפניהם: SCRIPTURE EQUATED WOMAN TO MAN FOR ALL THE LAWS OF THE
  TORAH (Bava Kamma 15a)"; where איש is written it excludes the
  MINOR, not the woman — the parity rule for the whole civil code
  rides the block's opening — MAJOR.
- ⚠ Bartenura 21:2 — HERMENEUTIC PRESSURE analysis: why did Rashi
  entertain "slave OF a Hebrew"? — because the Hebrew-slave reading
  FORCES the shocking shefachah-permission ("the Torah permitted him
  a Canaanite woman forbidden to every Israelite — if we COULD read
  it as a Canaanite slave, we would") — the harder reading stands
  only because אחיך compels it; readings are chosen AGAINST
  interpretive comfort under evidence — MAJOR-adjacent ADD; the
  proportionality temptation for the self-seller reading (court-sale
  should scale to the theft — "if small, sell him a year or two");
  the two-passages necessity rule stated ("what this one omitted,
  that one revealed" — מה שחסרה זו גלתה זו); the son-not-brother
  rationale by COUNTING standings-in (son stands in for TWO — yiud +
  field-redemption; brother only for yibbum) — CONFIRM+.
- Bartenura 21:3 — FOUR independent rationales collected for
  no-shefachah-for-singles: (a) first-love protection (אהבת נעורים
  not to be set on a Canaanite), (b) the wife-as-instigator theory
  ("perhaps SHE incited him to steal — Scripture brings her rival
  into her house"), (c) habituation, (d) psychological cost ("leaving
  his firstborn strength in the master's house — bearable only for
  one already anchored") — the WHY-registry pattern — ADD; the
  fit-wife predicate 2nd witness (עמו excludes forbidden unions — no
  maintenance for one under "stand and divorce"); the עמו/עמו
  gezerah-shavah formalizing family-maintenance across both
  sale-modes (3rd witness).
- Bartenura 21:6 — the door must be MOUNTED ("standing — excluding
  tilting it off its hinges to pierce on it"); the מופנה analysis of
  אזן-אזן (the leper-verse's repetition is FREE — could have said
  "do as the first" — redundancy licenses the analogy); the לעולם
  candidate-readings dance (slave's lifetime impossible — K"V
  redundancy; ADON's lifetime proposed; rebutted by the doubly-
  redundant ואיש אל משפחתו).
- ⚠ Bartenura 21:7:2 — the GET-FOR-THE-AMAH K"V with the
  DIRECTION-OF-ANALOGY rule: she needs a manumission document — "a
  wife, who exits neither by years nor money, exits by document; the
  amah, who exits by both — all the more so"; and the tiebreak: "more
  reasonable to learn WOMAN from WOMAN than woman from slave" —
  type-proximity governs analogy choice (source-selection principle,
  2nd form) — ADD.
- Bartenura misc — the אלה-operator's own name etymologized two ways
  (פסל = cut-off vs prepared); אשר תשים from ויושם לפניו לאכול (the
  set-table as FOOD-SERVICE etymology); day/night double-wage
  arithmetic (days for the master, nights begetting); designated-
  needs-no-new-kiddushin from word-choice (יעדה vs לקחה); the
  Rambam's age-windows quoted (minor to 12; naarah = two hairs + six
  months; bogeret after).
- Periphery: Ateret Zekenim — the SHOVAVIM calendar ends at our
  verse ("not completed until כי תקנה — 'in his body he comes, in
  his body he goes out' — they left Egypt repaired"); Ba'alei Brit
  Avram — the Torah-scroll HANDLING protocol from the כצאת masorah
  trio (taken out only for great need, with honor, all rise); Avi
  Ezer grammar apparatus (honorific plural "as the nations today
  address a lord"; עת/ענת nun-elision defended).
PACE: bite 35 = 31 listings / 18.1k chars. Ledger 1,067 read (54.4%);
869 remain.

### Batch 36 digest (Bartenura tail + Beit HaLevi + BEIT YOSEF CM 26 + Ben Ish Chai + Ben Yehoyada — 19)
- Bartenura 21:10:1 — verse-ORDER constrained by the waivability
  typology: had אם אחרת come after שלש אלה one would read the triple
  as fully stipulable at kiddushin — but the halakhah splits: MONEY
  duties (food/clothing) may be conditioned away, ONAH never (צערא
  דגופא) — the placement argued from the waiver rules — CONFIRM;
  21:11 the get-argument against the triple-reading ("she is his
  WIFE — she cannot exit 'free', she needs a get"); 21:8:2 flat-rate
  3rd witness; 21:8:3 the pshat/drash split of לא ימשול (pshat=master,
  the father-bar from the clause-sequence).
- Beit HaLevi Terumah 1 — SEQUENCING AS DEPENDENCY: Mishpatim before
  Terumah because donations must pass the justice-filter first —
  "before a man gives charity, his money must hold no theft — else it
  is a mitzvah-born-of-sin (like the stolen lulav)"; "when justice
  recedes, charity stands far off — useless" (Isa 59:14) — clean
  inputs before offerings — ADD.
- ⚠ BEIT YOSEF CM 26 — the forum rule's CODIFICATION CHAIN complete:
  Gittin baraita → Rambam ("whoever litigates before their judges is
  WICKED, as if he blasphemed and RAISED A HAND against the Torah of
  Moses") → Ramban (both-parties' consent does not help, even where
  their law matches ours) → Rivash/Alfasi ENFORCEMENT: excommunicate
  (נידוי/חרם) the one who goes AND whoever strengthens his hand —
  Mekhilta → Talmud → rishonim → Tur → Beit Yosef → Shulchan Arukh,
  consent-invariance and sanctions intact the whole way — CONFIRM+.
- Ben Ish Chai Drashot 1 — the JUDGE-RELUCTANCE rebuke: R. Assi wept
  at death "for I could have judged Israel's cases and withdrew" —
  declining the bench while qualified = "destroying the world" (the
  civic-duty rule's deathbed witness); ONE av-beit-din per generation
  (דבר אחד לדור — the single-head rule) — CONFIRM; Drashot 4 — the
  wealthy called "faces": "if the judgments are not accepted and
  executed ON THE RICH TOO, what use are they to the world?" — equal
  application to the powerful — ADD; the teshuvah/Torah allegory
  series (the triple as the ORAL LAW'S OWN survival needs: the
  received TRADITION is her FOOD — "without it, the Karaites, holding
  nothing"; DEEDS her clothing; FIXED TIMES her onah) — meta-allegory,
  periphery-plus.
- Ben Yehoyada AZ 3a — the Alshekh root-doctrine OPERATIONALIZED:
  God "untied the KNOT between the physical deed and its upper root"
  for the nations (עמד והתירן reread as un-BINDING) — their deeds
  then run without the rooted side-effect, paid only here — the
  two-implementations claim given its mechanism (the binding is
  detachable) — ADD; Eruvin 73a — the duties-counts encoded in the
  gender-words (yud=10 husband-duties per Rambam 3+7; heh=5 personal
  services never delegable) — periphery; Pesachim 49b — the Zohar's
  בבגדו בה (garment-of-impurity torn to free trapped sparks) —
  periphery.
PACE: bite 36 = 19 listings / 21.0k chars. Ledger 1,086 read (55.4%);
850 remain.

### Batch 37 digest (Bereshit Rabbah + Chanukat HaTorah + CHATAM SOFER — 18)
- ⚠ Bereshit Rabbah 26:6/31:5 — the SUB-THRESHOLD THEFT ATTACK: the
  flood generation's method — "one came and took LESS THAN A PERUTAH,
  and another, and another — until no court could reach it" (חמס =
  sub-perutah, גזל = over; gaming the justiciability threshold); God's
  answer: "you acted outside the line — I too will act outside the
  line" — when the system is gamed below its granularity, enforcement
  escalates OUTSIDE the system (the flood as extra-judicial response);
  מבלי משים = "without the setting-of-law" (from our אשר תשים) —
  MAJOR-adjacent ADD; "where there is no din below there IS din
  above" (5th witness).
- Chanukat HaTorah 85-86 — (a) why entertain the LEFT ear: at Sinai
  "the speech went from God's RIGHT to Israel's LEFT" — the ear that
  heard לא תגנוב WAS the left one; the gezerah-shavah must overcome
  the geometry of revelation — ADD; (b) the version-precision rescued
  by the Decalogue-as-HEADERS doctrine: each commandment was spoken
  WITH its sub-clauses ("with לא תגנוב came property-theft and
  deception-theft") — the ear heard property-theft as a sub-item of
  the kidnapping headline — ADD (3rd witness on the theft-verse
  problem).
- ⚠ Chanukat HaTorah 150 — the Moses-litigation CLOSED ON A
  TECHNICALITY: the slave-clause requires SAYING IT TWICE (אמר
  יאמר); God's רב לך "do not speak to Me FURTHER of this" = estopping
  the second declaration — "if you say it once more, by law you must
  remain alive — therefore: do not add" — the heavenly court prevents
  the procedural trigger from completing — MAJOR-adjacent ADD (4th
  witness of the litigation, now with the procedural close).
- Chatam Sofer 1 — the mirrored-courts COSMOLOGY of the forum rule:
  "opposite Israel's courts sit the holy angels; opposite the
  idolaters' courts, THEIR PRINCES — going before their court gives
  glory to the idols" literally, by invoking the counterpart —
  CONFIRM+ (pairs w/ ShR 30:18, Alshekh).
- ⚠ Chatam Sofer 2 — EXIT-RIGHTS ANALYSIS: a worker may quit mid-day
  ("they are MY slaves — not slaves of slaves"), yet hiring oneself
  is permitted and SELLING oneself is not — via the Ran's
  money-deficiency principle: the slave's exit requires REFUNDING
  (who says he will have the funds?) — a liquidity-gated option is
  not an option; the employment contract's permissibility depends on
  the exit being unconditionally exercisable — MAJOR-adjacent ADD.
- ⚠ Chatam Sofer 4 — CROSS-MODULE CONSISTENCY PROOF: why "his wife
  goes out with him" HERE but "he and his CHILDREN" in Behar — the
  substitution model caps the master's duty at the father's, and a
  father's maintenance runs only to AGE SIX; at a six-year term's
  end every child alive at the sale has passed six → no child-clause
  here; Behar's yovel can cut the term short with children still
  under six → "he and his children with him" — the two verses'
  difference COMPUTED from the interaction of two constants (term=6,
  maintenance-window=6) — MAJOR.
- Chatam Sofer 5-6 — why not pierced at sale: "the buyer of a Hebrew
  slave ACQUIRES A MASTER FOR HIMSELF" — the sale doesn't violate
  "they are My slaves" (he is adon-to-his-adon); staying for the
  shefachah-family "descends from his level" → only then is he truly
  mastered → pierce; and the self-seller carve-out sharpened: the
  very verse כי לי בני ישראל עבדים DECLARES the brother-sale
  non-slavery — the self-seller's act was semantically innocent, so
  the homily (and piercing) runs only on the court-sold — ADD.
- Periphery: Chatam Sofer 9 (the pierced one's "forever" relocated
  into the offspring-lineage — his shefachah-children remain the
  master's, and he, calling them "my sons," is bound through them);
  BR 45:6 the Hagar join at source; Brit Moshe (daily-prayer
  frequency derived from bread-and-water's consumption cycle — the
  parameter fetched from the petition-object); Ben Yehoyada Shabbat
  97b (39-melachot gematria on שלש אלה); Binyan Yehoshua (mishpatim
  = גופי תורה "bodies of the Torah").
PACE: bite 37 = 18 listings / 18.2k chars. Ledger 1,104 read (56.3%);
832 remain.

### Batch 38 digest (Chomat Anakh/Chida + R. PERLA on Rasag's count — 14)
- ⚠ R. Perla, Communal Laws 12 — the COMMAND-ADDRESSEE TAXONOMY: why
  Saadia counts the slave-release among the COMMUNAL commandments —
  "the slave is under the master's power; his exit will normally be
  against the master's will, requiring COERCION by the community and
  court, for only they can bring the law to light — the duty lies on
  THEM"; the double-listing explained: Re'eh's תשלחנו = the ADON's
  individual positive duty; OUR verse = the COURT's duty — one
  release, TWO addressees, counted at each — the block assigned to
  the court-facing side (matches Chinukh's judicial-API + LT's
  אזהרה לב"ד) — MAJOR.
- ⚠ R. Perla Neg 13:2 — SYNTAX DETERMINES COMMAND-INDIVIDUATION: all
  counters treat כמשפט הבנות יעשה לה as the mere OPENING of the lav
  לא יגרע (no independent positive command) because NO VAV splits the
  clause — vs מעקה (ועשית... ולא תשים: the vav splits → both
  counted); parallels (ark-poles, altar-stones); Saadia the exception
  (he counted it as an עשה) — the mitzvah-count rides the
  conjunction — MAJOR-adjacent ADD; Intro ch.5 — the 613-methodology
  problem (the midrash's "sixty/seventy mitzvot in Mishpatim" vs
  actual counts; the counting needs its own spec of fences and
  roots) — ADD.
- R. Perla Neg 275 — Saadia's coinage for the resale-bar: לא תסלה
  "shall not be EXCHANGED" (from Job's לא תסלה בכתם אופיר, Targumic
  שלחף "swap") — the bar phrased as a no-exchange rule; the עם נכרי
  fork mapped formally (Rashi/Onkelos/Rambam "another man" vs
  Ramban's literal-gentile Mekhilta) with the source-checking rebuke
  ("the Lechem Mishneh clearly never saw the Mekhilta ITSELF —
  whoever looks inside sees Ramban's reading explicit") — CONFIRM;
  Neg 91:42 — the Mekhilta-deRashbi variant apparatus (attributions
  swapped between recensions; "the matter hangs on variant readings,
  no decision from there") — text-critical method again.
- Chomat Anakh (Chida) — the angels' claim run as DINA D'VAR METZRA
  (the abutter's pre-emption right!) — defeated on the loss-to-seller
  exception: the angels can use only the SOD layer, Israel both — a
  Choshen-Mishpat doctrine adjudicating the Torah's transfer — ADD;
  לחפשי note ("even during servitude he is free"); the exit-vs-entry
  maintenance question answered via the handiwork fork (no איבה here
  — he WANTS her fed — so the enactment's exchange never engages, and
  "she is one foot in, one foot out"); Vidal Tzarfati: the stayer
  breaks לא יהיה קדש (the shefachah permitted ONLY during the six) —
  staying = choosing the violation — ADD-variant.
PACE: bite 38 = 14 listings / 18.9k chars. Ledger 1,118 read (57.0%);
818 remain.

### Batch 39 digest (R. Perla cont. + Da'at Zekenim/Tosafists — 8)
- ⚠ R. Perla Pos 62:2 — GRAMMATICAL PERSON AS ADDRESSEE-SELECTOR: our
  verse is the COURT's command because it is NOT imperative — "it
  does not say 'in the seventh YOU SHALL RELEASE him' but יצא לחפשי
  'HE SHALL GO OUT' — for the command is on the court, who must
  SUPERVISE that he goes free"; Re'eh's second-person תשלחנו = the
  ADON's own duty ("if the court overlooked it, the master violates
  the עשה by retaining him") — the verb's person encodes which
  institution owns the obligation — MAJOR (completes the addressee
  taxonomy).
- ⚠ R. Perla Pos 64:11 — the YOVEL DEPENDENCY-GRAPH: the court's
  shofar-blast GATES all yovel commands (none fire till blown; then
  they fire RETROACTIVELY from the year's start); the sages' three
  blocking conditions ANDed (shofar + slave-release + land-return),
  with MAJORITY-COMPLIANCE as a runtime dependency — "if most of the
  public did not free their slaves… the yovel's sanctity is void and
  nothing fires" — mass non-compliance DISABLES the module (the
  mechanism behind the yovel enable-flag) — MAJOR-adjacent.
- R. Perla Pos 25:2 — a canonical command flagged as hanging on a
  minority derivation: the Mekhilta's "lending is OBLIGATION not
  option" rests on R. Yehudah's reading of תעביטנו; per the accepted
  sages' view the proof falls — yet all counters kept the command —
  ADD; Pos 61:20 — the shemittah-biur fork (destroy vs re-hefker)
  hanging on a Mishnah girsa (block 7, ledgered).
- Da'at Zekenim 21:1 — the Tosafist refinement of the אלה operator
  (פסל = "detached": bare אלה would mark what follows as DISJOINT
  from Sinai; the vav rejoins; scope-START exception for Devarim —
  2nd witness of the exception class); the two-patients parable
  attached directly to לפניהם (2nd witness); the ב"ל wordplay
  (משפטים בַּל ידעום — the Torah runs bet-to-lamed; the nations
  "cannot learn it" — first/last letters as exclusion-mark) —
  encoding-layer periphery.
- Da'at Zekenim 21:2 — the Tosafist RESCUE of Rashi's court-sale
  line: the Mekhilta's alternative concerns SERVING THE HEIR, not the
  six-year exit — the ribui/miut allocation (unqualified יעבוד
  includes an heir; ועבדך excludes) resolved SON-yes/BROTHER-no by
  the standings-count tiebreak (Kiddushin's "what did you see") —
  CONFIRM of the allocation machinery from the Tosafist bench.
PACE: bite 39 = 8 listings / 18.0k chars. Ledger 1,126 read (57.4%);
810 remain.

### Batch 40 digest (Da'at Zekenim tail + MAHARAL + Em LaMikra + Eretz Chemdah + Gur Aryeh — 30)
- ⚠ Derekh Chayyim (Maharal, Avot 1:1) — PROTECTION SCALED TO
  OPACITY: the three command-types mapped to the Great Assembly's
  three sayings — משפטים (rational) get "be DELIBERATE" (haste is the
  rational rules' failure mode); מצוות (knowable-by-study) get "raise
  many STUDENTS"; חוקים (opaque) get "make a FENCE" — "because their
  reason is unknown, one may stumble; what is not understood needs
  the fence MOST" (the seconds/gates built where introspection fails)
  — MAJOR-adjacent ADD; 1:18 — din and altar-service as the two
  God-owned functions (המשפט לאלהים; unfit judge = asherah by the
  altar) — CONFIRM.
- ⚠ Em LaMikra (Benamozegh) — the MODERN COMPARATIVE-LAW LAYER: the
  pierced-ear servitude-mark "transferred from us to the GREEKS —
  see MONTESQUIEU, Book 2 ch. 12"; the additive vav paralleled in
  LATIN ("Sicut ET nos") — 19th-century comparative jurisprudence
  entering the shelf on our verse — ADD.
- Gur Aryeh (Maharal on Rashi) — the REDUNDANCY-RESOLUTION ORDER
  rule: "the LATER extra word reveals the EARLIER one" (יתור בתרא
  מגלה איתור קמא), citing his own Mishpatim analysis at ויצאה חנם —
  ADD; the אלה operator's DEIXIS ("not like אלה המשפטים, which
  points to what FOLLOWS" — down-pointing vs up-pointing); the
  G"S-authorization rule ENFORCED polemically: the Rae"m's
  gezerah-shavah on Joseph's slanders (via our אם רעה) rejected —
  "his G"S I do not accept; NO ONE DERIVES A G"S ON HIS OWN" — the
  licensing requirement applied against a fellow commentator — ADD.
- Eruvin 54b (at source) — the fourth teaching duty from our header:
  "whence that one must SHOW THE FACE [the reasons] of the law? —
  אשר תשים לפניהם" — the pedagogy anchor — CONFIRM.
- Da'at Zekenim tail — children-maintenance G"S ("for one who lacks
  it — mere disclosure"); the dead-code argument 2nd witness with the
  rebuke ("a father cannot sell his son; a minor's act is nothing;
  the court does not punish a minor"); IE's indoor-work rule 2nd
  witness; value-curve 4th witness; מרצע-400 3rd; Levite-olam 3rd;
  ailonit 3rd; two-ended קץ 2nd.
- Eretz Chemdah — the WORKED CALENDAR self-application: the ten
  plagues' days (each a quarter-month, darkness doubled, firstborn
  extended to the sea = ~75) matched against the 86 servitude-years
  MINUS THE SEVENTH-YEAR EXEMPTIONS ("take the sevenths out of 86 →
  74") — God applying the slave-law's sabbatical rule to His own
  punishment schedule, with arithmetic — ADD-periphery.
- Eshkol HaKofer (Ruth) — the Zohar on OUR אם אחרת יקח לו: the
  widow-remarriage two-spirits doctrine ("who marries a widow enters
  the great sea without oars; the first husband's spirit remains and
  the two war"); chalitzah's spit as releasing the resident spirit —
  the mystical reading of the second-wife clause — periphery.
PACE: bite 40 = 30 listings / 25.0k chars. Ledger 1,156 read (58.9%);
780 remain.

### Batch 41 digest (Gur Aryeh/Maharal on the block — 12)
- GA Devarim 15:12 — the WHAT-COUNTS-AS-CHIDDUSH rule: a repeated
  passage is re-taught only for content "we would not have said from
  our own reasoning"; the no-limb-exit clause is NOT a chiddush — it
  merely BLOCKS a would-be K"V (restores the default) — innovation =
  counter-inferential content; inference-blocking isn't innovation —
  ADD.
- GA Devarim 25:5 + our אין כסף — the semantic theory of אין: the
  yud marks EXHAUSTIVE-SEARCH semantics ("even if you search, none
  found" — hence עיין עליו "search further" at yibbum, and "no money
  for THIS master but YES for another" at our verse; the אן/מאן
  orthography parallels) — the דיוק's grammatical foundation —
  CONFIRM+.
- ⚠ GA Shemot 20:1 — the ATOMICITY claim: all ten in one utterance →
  "the whole Torah is ONE UTTERANCE — like a single point, it has no
  parts; one who denies part denies all" (Sanhedrin 99a; the
  unity-metaphysics: what descends fragments) — no partial
  acceptance; the license is all-or-nothing — MAJOR-adjacent ADD.
- GA 21:1:1 — the אלה operator DECOMPOSED: "אלה implies EXCLUSION;
  the vav ADDITION — read together: THESE (only) add to the first";
  alt: ואלה adds IN RANK (equates importance, beyond a plain vav);
  the repetition model: the Torah is indivisible, so at each covenant
  locus (Sinai/Ohel Moed/Moab) the WHOLE was re-stated, anchored by
  the commands belonging there ("parts cannot be given in different
  places") — full re-transmission at each milestone — MAJOR-adjacent
  ADD.
- GA 21:1:3 — Sanhedrin-by-the-altar as EQUIVALENCE + TOPOLOGY: the
  altar makes peace above, the din below — "all bound together"; the
  Chamber of Hewn Stone at the world's CENTER "as the navel is the
  body's center — the center binds all the parts" — the court as the
  system's integration point — CONFIRM+.
- GA 21:1:4-5 — the pedagogy-stack formalized (four sources: repeat /
  until-learned / fluent recitation / THE REASONS as set table); the
  epistemology of לפנים (what is before-and-SEEN = fully known —
  vision-as-knowledge); the double-derivation defended (שלחן ערוך
  from לפנים, the exclusions from ־הם); Maharal's antecedent: the
  ORDAINED ("every judge was appointed from Moses, hence expert") —
  CONFIRM.
- ⚠ GA 21:1:7 — THE CORRUPTION-OF-DEPLOYMENT RECORD: Maharal
  documents his own era's failure — "in some communities they
  appointed IGNORANT CHIEFS who know no law and darshened the verse
  FOR DISGRACE ('before laymen' DAVKA); they took judgment from those
  who know and gave it to the ignorant; the learned watch perversion,
  powerless to save orphan or widow; they transgress 'plant no
  asherah beside the altar' continually — the letters of אשרה spell
  הראש, 'the CHIEF whom God hates'; money-appointed judges are אלהי
  כסף, and it is a MITZVAH to slight their honor (per Choshen
  Mishpat; the Yerushalmi's R. Mani)" — the living system's
  governance failure described and sanctioned by its own maintainer —
  MAJOR.
PACE: bite 41 = 12 listings / 19.0k chars. Ledger 1,168 read (59.5%);
768 remain.

### Batch 42 digest (Gur Aryeh on 21:2-8 — 23)
- ⚠ GA 21:2:3 — the ANTI-TELEOLOGICAL CONSTRAINT stated as method:
  "for the sake of a verse's REASON we do not reject the verse's
  READING — when we know what it speaks of, we interpret the reason;
  we never dislodge the sense on account of a rationale, for that is
  not the Torah's interpretive method" (בשביל טעם המקרא אין לדחות
  משמעות של מקרא) — rationale cannot override semantics —
  MAJOR-adjacent ADD; the Canaanite-from-Israelite taxonomy (already
  mitzvah-bound like a woman → cannot become a permanent holding);
  "from THEM you may buy — they may not buy each other" (gentile
  self-sale only).
- GA 21:2:4 — WHY the word עבד: it marks the VIOLATION ("had it said
  'when you acquire an ivri' we would think six-year service is not
  slavery and carries no wrong") — the status-tag enabling the
  piercing's rationale; the worker-contrast codified (poal retracts
  mid-day; the eved cannot until he pays — exit-rights 2nd witness);
  the Mekhilta-girsa flag against the Rae"m ("ours reads the
  OPPOSITE — one may NOT call him slave for disgrace").
- GA 21:2:6 — the proportionality intuition as the REJECTED DEFAULT
  (3rd witness: "the court should sell him per the theft — stole
  much, sold longer"); passive-voice semantics (ימכר covers unwilling
  self-sale — "what is not done willingly takes the nifal").
- GA 21:3:2 — maintenance-צריכותא (wife can't beg; children can't
  work); and the WELFARE-CLAUSE derivation: though the husband owes
  no Torah-maintenance, "since it is GOOD for him that they eat — and
  Scripture says כי טוב לו עמך — the master owes it" — the duty
  derived from the good-for-him clause, bypassing the
  husband-baseline problem — ADD.
- GA 21:4:1 — the PAIR-doctrine as 4th rationale: with an Israelite
  wife the shefachah is "not his PAIR (זוג), merely his shefachah —
  permitted; without one she becomes his full pair — and a shefachah
  may not be the pair of an Israelite" — ADD; 21:4:3 — תהיה durative
  ("SHALL BE — forever") excludes any term-limited reading (so not a
  self-selling woman; Maharal's structural proof vs the Rae"m's
  Mekhilta cite).
- GA 21:6:2 — the donor-clause given a real referent (the verse
  commands the HAGASHAH to door-or-mezuzah; piercing then on the
  valid one — answering "would Scripture name a legally-empty
  object?"); RSHb"Y harmonized: the STANDING requirement itself
  encodes the witness-rationale ("the door must be worthy of a
  mezuzah — for door and mezuzah were witnesses in Egypt").
- GA 21:6:3 — the headers-doctrine attributed: "the whole Torah is
  included in the Ten Commandments, AS RABBENU SAADIA GAON FOUNDED"
  (the azharot-by-Decalogue); the perpetuity-threshold answer to the
  piercing-timing (serving-to-yovel = "acquiring a master," six years
  is not); Maharal's synthesis: the piercing is a SLAVERY-MARK — the
  homily explains only WHY THE EAR carries it (organ-selection vs
  punishment) — ADD.
- ⚠ GA 21:8:4 — the DEDUCTION FORK sharpened: Maharal argues the
  deduction is a legislated CONCESSION AGAINST the ownership-logic
  ("by strict law no deduction — her body is acquired; a master who
  waives his deduction, it is not waived (Kid 16a); the Torah's
  והפדה makes him ASSIST, counting her work as received money") and
  REJECTS the value-curve reading ("if early years are worth less,
  why count them as the later? no reason"); plus the YIUD-PREMIUM
  option-pricing argument (the amah-buyer pays extra for the
  designation option — deduction strips the premium — hence her
  deduction needed its own verse, underivable from the male's) —
  MAJOR (the fork: value-curve vs concession-against-ownership, plus
  option-pricing).
- GA 21:8:1 — רעה graded via the Mekhilta: "no CHESED before him"
  (rah = the absence of excess-kindness, not mere dislike); the
  yiud-mitzvah inferred from CAUSAL syntax ("since Scripture gives a
  REASON for the non-designation, designation is the expected
  default").
PACE: bite 42 = 23 listings / 19.9k chars. Ledger 1,191 read (60.7%);
745 remain.

### Batch 43 digest (Gur Aryeh completes the block — 12)
- GA 21:8:5 — the עם-נכרי fork CLOSED with an intent-translation
  doctrine: Onkelos's "to another man" defended not as lexicon but as
  CAPTURED INTENT ("he explained the verse's intention") — the
  narrative-logic argument (if she displeased him, no Israelite
  resale makes sense either; the Kiddushin 19b רעה=disqualified
  reading; and since בבגדו בה is given as THE REASON, the bar covers
  any resale) — ADD.
- ⚠ GA 21:10:3 — MAHARAL'S RECONCILIATION of the maintenance fork:
  the verse read at face value EVEN per maintenance-is-rabbinic —
  "not that the Torah obligates the three, but SUCH IS THE WAY OF
  MANKIND; the verse presupposes them as custom and forbids the
  DEROGATION (he may not, having taken another, treat her as
  un-wifed)"; proof: the Torah makes the MASTER feed the slave's
  family — "were it not universal practice, why would it fall on
  him?" — the triple as PRESUPPOSED CUSTOM, positive law protecting a
  descriptive baseline rather than creating duties — the deoraita/
  derabbanan fork retyped — MAJOR.
- GA 21:11:2 — the חנם/אין-כסף allocation INVERSION explained as a
  TWO-PASS READ: "the later verse comes to REVEAL the earlier" — had
  only חנם stood, it would mean bogrut; אין כסף forces a re-parse
  (חנם → naarut, itself taking bogrut) — the addition re-parses the
  base (harmonized w/ תושב/שכיר; Tosafot's alternative — the
  TOSEFET takes the added case — recorded; the ailonit resolution;
  and the K"V-tempering rule: "invoke 'Scripture writes what a K"V
  yields' only when no other resolution exists") — MAJOR-adjacent
  CONFIRM (deepest procedural account of the pair).
- GA 21:11:1 — "one of three" defended from MUTUAL EXCLUSIVITY (he
  cannot designate her to himself AND his son — the conjunctive
  reading is unsatisfiable → disjunction) — ADD.
- GA Vayikra 18:9 (crossref) — the incest-law's SIBLING-PREDICATE
  imports our descent rule: "his sister from the shefachah/gentile"
  excluded via האשה וילדיה תהיה לאדוניה (+ כי יסיר) — cross-module
  reach of 21:4 — CONFIRM.
- Periphery: the angel-courier refusal ("even as a פרוונקא I'll not
  accept him") back-referenced to his Mishpatim comment; the
  בשר-בחלב naming theory (the whole offense called BISHUL — the
  root-act naming; the offense-individuation aside: cooker-then-eater,
  one count or two).
PACE: bite 43 = 12 listings / 18.1k chars. Ledger 1,203 read (61.3%);
733 remain. Bites 34-43 complete. Gur Aryeh DONE. Next: remaining
acharonim (HaAmek Davar/Netziv? HaKtav VeHaKabbalah, Malbim, Meshekh
Chokhmah expected), apparatus tail, then --tanakh mode.

## Batch 44 digest (16 listings; Gur Aryeh Vayikra tail + HaKtav VeHaKabbalah opens)

- **Gur Aryeh Lev 19:2:4** — CONFIRM: "be holy" = separation from forbidden unions AND the other sins, "as we already wrote in parashat Mishpatim"; holiness of the arayot voided if other sins remain.
- **Gur Aryeh Lev 25:10:3** — CONFIRM (full topology): Kiddushin 15a derivation web for yovel-frees-the-pierced — ואיש אל משפחתו תשובו ("each man shall return to his family") must be the pierced slave by elimination (court-sale already has ושב אל משפחתו, self-seller has עד שנת היובל); gender-selector: "a matter practiced in a man and not a woman — that is piercing" (ולא אזנה "and not HER ear" per R. Eliezer; העבד "the slave-MAN" not the amah per the first Tanna). Then the tzerikhuta: pierced-case and court-sale-case mutually necessary; ועבדו לעולם ("he shall serve forever") needed lest six-years-after-piercing free him; ושבתם needed lest לעולם be literal. The yovel-override chain shown as a 4-verse mutually-locking derivation.
- **HKV Deut 11:27** — CONFIRM (grammarian states the axiom): אנכי מצוה אתכם glossed "I EXPLAIN to you" — the Oral Torah is the Torah's built-in explanation (cites Rambam's introduction); "see what I wrote at the end of Mishpatim."
- **HKV Deut 16:7 / 24:13 / Exod 2:5 / 19:10** — periphery: בשול = "making fit to eat" (roast included); day/night collateral-return via Yerushalmi's two-valued "coming of the sun"; אמתה = the honored maidservant "as at the head of Mishpatim"; Sinai chronology with Exod 24 displaced (אין מוקדם ומאוחר "no earlier-and-later in the Torah").
- **HKV Exod 21:1** — CONFIRM+lexical ADD: תשים לפניהם ("set before them") — לפניהם glossed as the mind's interior ("to their insight", German gloss in text); R. Akiva Eruvin 54: judge must "show them the faces/reasons." The show-the-reasons doctrine grounded in the WORD, not just homiletics.
- **HKV Exod 21:2** — CONFIRM: חנם ("free") = master cannot bill a slave who fell ill for idle-time, food, or doctor (via Rabbeinu Bahya). Sick-leave clause.
- **HKV Exod 21:3:1** — MAJOR fork-map: Canaanite bondwoman for a wife-less slave — Tzeidah LaDerekh's "permitted by the slave's consent" DEFENDED via Ritva Kiddushin 15a (who refutes the stricter "some say" from two proofs: the self-seller needs a writ of manumission only if a kinyan-issur exists; and the self-seller-not-pierced derivation would be superfluous if he were barred anyway). Two permission TRACKS: master-compulsion (needs wife+children) vs slave-consent (free-standing). Temurah 6 atnan case resolved on exactly that split: Sages count the lamb as harlot's-hire because the MASTER'S grant is forbidden even where the slave's consent would permit. Mishneh LaMelekh's צ"ע dissolved (he missed Ritva at 15a).
- **HKV Exod 21:3:2** — MAJOR lexical mechanism for maintenance: ויצאה אשתו עמו — the verb יצא also means EXPENDITURE (ויוציאוהו לחרשי עץ "they paid it out to the carpenters," II Kings 12; rabbinic הוצאה "outlay"); so "her outlays shall be WITH him" = equal to his, עמו as "like him" (עם מלכים "like kings," Job 3:14). Maintenance is IN the verse's verb, not only in the "who brought her in?" midrash. Plus Ritva Kiddushin 22 rationale: Torah preserves the family's expectation — "had he not been sold he would have fed them," so the master feeds them. Expectation-preservation principle for the maintenance module.
- **HKV Exod 21:6:1** — CONFIRM+shim: או ("or") read as אם ("if") — "to the door IF it stands at the doorpost" (R. Zalman of Vilna); Rambam: presentation at door or doorpost standing in place, piercing reaches the DOOR only (from Deut ובדלת "and into the door"). Kills Re'em's objection that a Torah word can't exist solely for a hekesh.
- **HKV Exod 21:6:2** — MAJOR counter-GRA lexical essay: עולם from על ("above") = perpetual ASCENT; the world called עולם because everything climbs rung to rung (elements→plant→animal→man); yovel called עולם because in it every lowered thing RISES to first station — "the slave equals his master, the bondwoman her mistress, the debtor his creditor — one ascent for all." Alternative (RSh"P): עלם = removal/concealment → לעולם = "to the year of release of all servitudes." Either way ועבדו לעולם MEANS until-yovel from the lexicon itself — the halakhic reading built into the word, no uprooting needed. Direct structural answer to the GRA's הלכה עוקרת את המקרא ("the halakhah uproots the Scripture").
- **HKV Exod 21:7** — CONFIRM: amah vs shifchah rank (light duties/housekeeping vs hard labor), now with Raaya Mehemna (Zohar) soul-level anchor.
- **HKV Exod 21:8:1** — ADD third yiud lexical model: beyond Rashi's appointment and Onkelos' establishment-from-עד, HKV derives יעד from עדה ("community/joining") — designation = incorporation into one flesh (והיא חברתך ואשת בריתך "she is your companion and covenant-wife," Malachi 2:14). Ketiv לא ("not")/qere לו ("to him") noted with both reasons.
- **HKV Exod 21:8:2** — MAJOR apologetic layer on the עם נכרי fork: full grammarian's defense that עם ("people") denotes a single person in rabbinic usage (עם הארץ for one ignoramus); or the household (Ralbag — sale to the buyer's WHOLE HOUSE, aggravating the betrayal: instead of one husband's wife she serves the many); or distributive lamed ("to each of the people," like three tenths PER bull). Closes: "I wrote at length to silence the scoffers who stammer against the word עם — for the daughter is not sold to a nation." The fork now carries an explicit anti-critic defense essay.

## Batch 45 digest (20 listings; HKV core verses + Netziv/Haamek Davar opens)

- **HKV Exod 21:8:3** — MAJOR meta-hermeneutic (via R. Wolf Heidenheim): the בבגדו בה dispute (Kiddushin 18) — R. Akiva "spread his garment over her" (יש אם למקרא, the vocalized reading decides) vs R. Eliezer "since he betrayed her" (יש אם למסרת, the consonantal skeleton decides) — is NOT a conflict between reading and writing: the rule-pair only applies to a word that weight, derivation, and conjugation all fail to disambiguate; then one side resolves toward the skeleton (tolerating slight irregularity), the other toward ordinary usage. Full dagesh/rafeh and missing-yod evidence marshalled both ways, plus two harmonizations (denominative verb from "garment"; bet meaning "upon"). The ikkar-mikra/ikkar-masoret pair reframed as an ambiguity-resolution POLICY, not textual rivalry.
- **HKV Exod 21:11** — MAJOR lexical mechanism for the puberty exit: חנם from חן ("grace") with appended mem — ויצאה חנם = "she goes out at her GRACE-time," when the ornaments that draw grace appear (Ezek 16:7 "breasts formed, hair grown"; Zohar Yitro: "these are a woman's beauty"). The signs-exit derivation is IN the word; no redundancy with אין כסף ("without money"). Same move as his עולם essay: the halakhah found inside the lexicon, no uprooting.
- **HKV Exod 34:23 / Gen 6:13 / Gen 26:20 / Lev 22:28 / Lev 23:15** — periphery: the see/be-seen (יראה/יראה) two-eyes exemption with the GRA's re-anchoring to Gen 22; פנים = intent/awareness network (crossrefs תשים לפניהם); the mistaken-intent actor (מתעסק) category; שור as gender-inclusive term (Onkelos renders fem תורתא for mother-and-young — block-3 lexicon); omer-counting quality essay.
- **HKV Lev 25:41** — CONFIRM+parentage: ויצא מעמך הוא ובניו ("he shall leave you, he and his children") = master owes the CHILDREN's maintenance (עמך = the with-you food obligations); and per Korban Aharon this Behar verse is the derivation PARENT that taught the reading of ויצאה אשתו עמו as WIFE-maintenance — Exod 21:3 mentions no food at all. Direction of inference settled: Behar → Mishpatim.
- **HKV Num 35:19/21** — block-10/2 adjacency: בפגעו בו = "when judgment is decreed on him" (פגע ב־ = execution of sentence; Onkelos "when condemned by law"; Sifrei: only through court and witnesses) — avenger locked to the court channel; באיבה הכהו בידו = the constrainer (מצמצם, pinning under water) derived from בידו vs באגרוף (fist — the stone-fist hekesh from our chapter: both must suffice to kill).
- **Netziv Deut intro** — repetition doctrine: Deuteronomy repeats but never redundantly; notes Ki Tisa repeats Mishpatim's own closing block (שמר לך through בחלב אמו) — the Exod 23/34 doublet flagged from inside the tradition.
- **Netziv Exod 21:1:1** — CONFIRM juxtaposition family, blessing-causality spin: altar pericope ("I will come and bless you") → justice, because administered justice BRINGS blessing (cf. the מלאתך ודמעך midrash); same seam Re'eh→Shofetim.
- **Netziv Exod 21:1:2** — CROWN-adjacent: תשים לפניהם = "explain thoroughly" (Eruvin 54), and why HERE above all: "parashat Mishpatim is written with extreme compression, and some sections have NO comprehension at all without the received explanation." The compressed-code + oral-decompiler thesis stated flat by the Netziv.
- **Netziv Exod 21:2:1** — CONFIRM Decalogue-parent (4th parent variant): the header "who brought you out of the house of SLAVES" + Behar "they are My slaves — they shall not be sold as slaves are sold" make full slavery impossible for an Israelite; the pericope exists to define the NON-slave treatment of a sold Israelite.
- **Netziv Exod 21:2:2** — ADD to the עברי naming fork: "Hebrew" not "Israelite" because the sold man is "an exceedingly cheap man" who carries only the bare ethnonym (his Exod 5:3 note) — the name itself encodes lowered status.
- **Netziv Exod 21:2:3** — MAJOR: חנם ("free") in Torah diction = no PROCESS, not no payment: the exit needs no writ of manumission. Contrast marriage: even a one-day betrothal needs a get (Nedarim 29a) because marriage is sanctity-of-the-body that never lapses on its own; the slave's body IS acquired (Kiddushin ch. 1 — even "profaned" to permit the Canaanite bondwoman), so one would think ending it needs a document — the verse teaches the acquisition is non-absolute: term expires, he walks, DOCUMENTLESS. Auto-expiry semantics vs sanctity-acquisition semantics. "This is the depth of the plain sense, and the sages' derivation is derived nonetheless."
- **Netziv Exod 21:3:1** — ADD pshat layer on בגפו ("in his single state"): he may not marry a FREE woman mid-term — new marriage would idle him from work; procreation duty does not override others' money or his servitude.
- **Netziv Exod 21:3:2** — MAJOR fork-ADD on ויצאה אשתו עמו: the wife exits WITH him even against her own drift — accustomed to serving and being fed in the master's house, she might prefer staying to sharing her husband's poverty; the verse FORBIDS the master to retain her. Exit as anti-capture rule severing the household's gravity over the slave's family; same warning for the children in Lev 25:41. Stands alongside (not against) the maintenance reading.
- **Netziv Exod 21:4:1** — CONFIRM derivation topology of בנים או בנות ("sons or daughters"): both needed — sons alone, you'd say a daughter follows the father even more (from "and Dinah his daughter"); daughters alone, you'd say the son needs the father's guidance more (Ketubot: "the daughter with the mother"). Both written → all children stay with mother → master.
- **Netziv Exod 21:6:1** — ADD pre-piercing stage: והגישו אדניו אל האלהים ("his master shall bring him to the judges") = the court REBUKES first — "is love of a Canaanite woman and foreign children worth marring your honor? after piercing he never returns to his fathers' lineage and is blemished FOREVER" — only on refusal does the awl proceed. Lineage-permanence claim attached to the piercing.

## Batch 46 digest (39 listings; Netziv 21:7-11 + method intros + Haamek Sheilah + Hadar Zekenim 21:1-9)

- **Netziv 21:7:1** — MAJOR pshat: לא תצא כצאת העבדים ("she shall not go out as the slaves go out") = NO slave-exit applies to her at all, because the amah's default purchase-intent is marriage; and post-yiud she remains quasi-amah — unlike a full wife (owes no labor min haTorah) she still serves the house, "like a pilegesh (concubine)" per Rambam Melakhim 4:4 (commoner forbidden a concubine EXCEPT the designated amah); yet for exit she is full wife: only a get releases. Purchase-intent → status-hybrid.
- **Netziv 21:8:2** — purchase-intent asymmetry drives the redemption duty: the male was bought for service only (no reason the will should change); the amah was bought partly FOR designation — if she now displeases, she must not sit as mere servant, hence והפדה ("he shall let her be redeemed"); and if the father can't pay, the master might resell to recoup — לעם נכרי forbids.
- **Netziv 21:9-11** — כמשפט הבנות = wedding honor per local custom, enforceable (Rosh Ketubot 1); novelty: designating to the SON (who owns nothing) still obligates the FATHER to fund. יקח לו = a wife per his own rank, as life-companion — unlike the amah whose essence stays service. ויצאה חנם אין כסף pshat: post-yiud she's a wife — no redemption money owed, but a get IS required; חנם alone might have implied no-get, so the verse glosses itself: chinnam MEANS no-money-only. (Mirror of his 21:2:3: for the male chinnam = no-document.)
- **Netziv Exod 35:1** — ADD tiered promulgation: Mishpatim through Tisa relayed immediately post-descent to those able to understand; the common folk heard general outlines from the learned; the Vayakhel assembly (men AND women) was the special full-public session for Shabbat.
- **Netziv Gen Kidmat HaEmek 6** — MAJOR decompiler primitive: words functioning as if WRITTEN TWICE (distributive double-reading), with our chapter as flagship — Exod 22:8 על כל דבר פשע reads as two virtual verses with two endings ("whom the judges condemn pays double" / "both parties' claim comes to the judges"), "and so Chazal expounded"; plus end-letter-to-next-word, ותמנע read into the prior verse (GRA), ויהי בארבעים שנה reading up and down. "This is the nature of the Torah." Lev 15:11 note repeats the tool ("two things from one verse — as we wrote in Mishpatim and everywhere").
- **Netziv Lev 25:39** — MAJOR distribution-of-protections theorem: why no-slave-labor and no-rigor warnings sit in Behar (self-seller) not Mishpatim (court-sold): the court-sold thief presumptively works the FIELD (fixed, known tasks — no scope for degrading make-work); the self-seller enters a rich man's HOUSE (task-dignity varies, needs warnings); עמך = someone familiar/trusted (else "suspect him" — Derekh Eretz). Workplace type explains the pericope split.
- **Netziv Lev intro 12 + Haamek Sheilah II 6:3** — CONFIRM recompilation thesis: his diyukim RECOVER received halakhot from verse-precision (e.g. Rava's hekdesh-releases-liens shown in the verse; the Sheiltot did likewise); "seek her as silver, as hidden treasures" = refine halakhah from the verse in place AND dig cross-refs elsewhere, then arrange as a SET TABLE (Mekhilta on תשים לפניהם; Eruvin 54 "ordered in their mouths").
- **Haamek Sheilah III 8:6** — MAJOR export-control on the reasoning layer: gentiles may learn fixed halakhot; the TALMUD — the derivation logic — is "betrothed to Israel"; ומשפטים בל ידעום ("and judgments, they knew them not") = the modes of judging-reasoning withheld; written Torah was even INTENDED for the nations (70 languages on Joshua's stones, Sotah 7), the חקירות never. Written = public interface; oral reasoning = licensed source. Joins show-the-reasons/promulgation cluster.
- **Hadar Zekenim 21:1:1** — CONFIRM+refined meta-rule: אלה ("these") at a section's HEAD sets apart what precedes (sometimes to praise, sometimes to blame — covenant at Moav vs the curses; "generations of heaven and earth" disqualifies the tohu), ואלה ("and these") adds — these too from Sinai; אלה הדברים opening Deuteronomy can't disqualify (book-initial). Scope-conditioned typed rule, defended against "nonsense objections."
- **Hadar Zekenim 21:1:2-3** — Sanhedrin-beside-altar with a standing Tosafist objection (ובאת אל הכהנים הלוים — the judge is at the chosen place anyway); and לפניהם chained BACKWARD to the Decalogue as sanctions table: they who murder/commit adultery/steal end HERE — the thief's terminus is ונמכר בגניבתו ("sold for his theft"). CONFIRM sanctions-table parent.
- **Hadar Zekenim 21:2:1** — MAJOR topology repair (the holy master of Dreux, via Mekhilta): the או אינו dialogue re-anchored as being about WHICH HEIRS the slave serves, not the six-year exit (Tosafist objections: Re'eh already gives six for other-sold; "self-seller is stated" proves nothing since כי ימוך gives only yovel). Result: Mishpatim's bare יעבוד (broad — would include son AND brother) + Re'eh's ועבדך ("shall serve YOU" — restrictive) compose as ribbui+miut → the SON inherits the remaining term, the brother does not (Kiddushin 17b: the son stands in his father's place for yiud). Heir-service module with its two-verse derivation engine.
- **Hadar Zekenim 21:2:2** — ADD: Hebrew slave bought FROM a gentile — how did the gentile acquire him ("you buy from them, not they from you")? Resolution: the gentile master owns only his LABOR (מעשה ידיו), never his body.
- **Hadar Zekenim 21:2:3** — ADD-color exile-typology: ובשביעית ("in the seventh") = in the SEVENTH exile Israel exits free-chinnam (Babylon, Chaldea, Media, Greece, Persia, Ishmael, Edom); "I will search (אחפש) Jerusalem with lamps" read from חפשי (free); lamps = Torah.
- **Hadar Zekenim 21:3-4** — maintenance web named: children's food from Behar's ויצא הוא ובניו עמו; wife for court-sold via the hired-hired gezerah shavah; for who lacks it — גלוי מילתא (plain-sense disclosure). Shifchah permission rationale: an Israelite wife anchors him so he isn't drawn after the Canaanite woman. והוא יצא בגפו kills the hava-amina that the permitted union needs a GET to dissolve (בגפו = לבדו, alone).
- **Hadar Zekenim 21:5-6** — say-it-twice VARIANT: declare at the START of six and at the END of six. Door must STAND like the doorpost — the door is a WITNESS, and witnesses testify STANDING (the declaration is testimony; the furniture is proceduralized). או as אם again; piercing at door only; WHY the door: it caused his sale (he broke doors to steal) + the ear-height hole is a PERMANENT PUBLIC RECORD ("the slave's stature aligned, ear-hole against door-hole, proves he was pierced" — the Chizkuni lock-and-key credential in Tosafist form). Ear-at-Sinai quibble: Sinai's לא תגנוב is kidnapping! — answered: the ear heard the MONETARY theft ban too. Gematria: מרצע = 400 — God shortened the decreed 400 years to 210 out of love; this man CHOSE bondage, so the 400-instrument pierces him. ועבדו לעולם = the LEVITE's forever = 50 years, from Samuel's עד עולם (Samuel of Ramah dedicated "forever" = the Levite span).
- **Hadar Zekenim 21:7** — minor-only proof topology (the kal vachomer vs the alternative from לאמה = earnings-to-father, which presupposes she can't self-sell); and MAJOR pshat protection: לא תצא כצאת העבדים = she cannot be forced to OUTDOOR labor (water-drawing, grinding) — "all the honor of the king's daughter is within"; halakhic layer: not limb-exit like Canaanites, hekesh of עברי/עבריה; and WHY the male has no signs-exit: a male minor cannot be in servitude AT ALL (father can't sell a son; minor's self-sale void; court doesn't sell a minor — not punishable). The signs-exit asymmetry closed by the no-male-minor-slave theorem.
- **Hadar Zekenim 21:8:1** — fork-ADD (minority reading): לעם נכרי = an actual GENTILE (from לנכרי תשיך "to the foreigner you may charge interest") — the verse bans selling her to a gentile. Against the consensus "another man."
- **Hadar Zekenim 21:8:2** — MAJOR pro-rata engine (R. Yaakov of Orleans): objection — flat pro-rating is no "assistance," it's default (a laborer quits mid-day). Answer: the amah is bought YOUNG (~6, exits ~12); her labor-value curve RISES steeply — one day of the last three years outweighs all the first three; yet redemption is computed FLAT per-year, so the master genuinely SUBSIDIZES her exit. Plus payment-medium rules: redemption in CASH not goods (Kiddushin — the Torah repeated כסף); but REDUCTION works even in goods; R. Yudan: goods valued-as-money at transfer count as cash (valuation-at-exit vs at-transfer). The Orleans value-curve is the amah-side twin of the deduction-fork value-curve.
- **Hadar Zekenim 21:9:1** — MAJOR fork-ADD on the שלש אלה triple: כמשפט הבנות = a KETUBAH; and the three things = (1) yiud to self as full wife, (2) yiud to son, (3) taking her as PILEGESH (concubine, no ketubah — permitted to him, from אם אחרת יקח לו); redemption-reduction is excluded from the triple because it binds him regardless — proof: one who exits by reduction receives NO severance ("he is not 'sent from with you'" — Kiddushin). Pilegesh as the third option; severance denied on reduction-exit.

## Batch 47 digest (17 listings; Hadar Zekenim closes + Ketzot HaChoshen + Kli Yakar 21:1 essay opens)

- **Hadar Zekenim 21:11** — CONFIRM two-exit mapping topology: chinnam = full maturity, אין כסף = puberty — and why not reversed: from אין כסף we derive "no money to THIS master but money to ANOTHER master — the father," which only works at puberty (at full maturity the father has no rights in her at all).
- **Harchev Davar Deut 17:1** — ADD altar-judge isomorphism: blemished-sacrifice ban juxtaposed to judges = no appointing a scholar who is a SINNER ("blemish" = the corruptions of idolatry/sexual sin); "forty lashes on his shoulders" disqualifies the bench.
- **Keli Chemdah Yitro 9:6** — block-2 adjacency, zomemin calculus: the "you'd nullify the law of scheming witnesses" objection blocks a kal-vachomer only where SOME death-liability would remain; a k"v that exempts entirely (false witness against a Noahide; witnesses against a tereifah) does apply — with Tosafot Rid BK 83b.
- **Ketzot HaChoshen CM 3:1** — MAJOR mechanics for the ordination-collapse module: Rambam — one judge suffices min haTorah (בצדק תשפוט עמיתך), three is rabbinic; yet the sugyot run admissions/loans on שליחותייהו (agency of the ordained). Resolution via Tosafot Sanhedrin 2b: JUDGMENT and COERCION split — plain adjudication may sit with one/laymen, but מילי דכפייה (coercion: compelled get, beatings-to-compliance, seizure) always needs the ORDAINED, because אשר תשים לפניהם = "the instruments of the judges" (כלי הדיינים) and לפניהם points at the SEVENTY ELDERS (Rashi, Gittin). The אנן הדיוטות אנן exchange was precisely about coercing a get; R. Yosef: agency — as with debt-coercion ("he says the mitzvah doesn't suit me — beat him until his soul departs"; Ramban: even property-seizure is coercion-law). Bach's split defended against the Tumim: bare judgment needs ordination only where the pericope writes אלהים; coercion always. תשים לפניהם = the coercion toolkit vested in ordination; modernity runs it all on the agency fiction.
- **Kli Yakar Deut 12:4** — ADD lexical: שימה ("placing") = durable INSTALLATION, "a fixed thing that never departs" (from ולמדה...שימה בפיהם and Rashi on our header) — the set-table as permanent installation, not casual placement.
- **Kli Yakar Deut 16:21** — CONFIRM+expand asherah-judge doctrine: many-stones altar vs single-pillar ↔ the bench must be MANY ("only the One judges alone," Avot 4); unfit judge = planted asherah, beside-the-altar = "in the place of scholars"; earthen altar = humility; arrogance-in-ruling as the root corruption; asherah wordplay (the honor-seeker wants to be מאושר); "whoever has haughtiness deserves felling like an asherah" — judge and idol share one law of felling.
- **Kli Yakar Exod 15:23** — MAJOR-color Marah acrostic: the dinin were commanded at MARAH before Sinai, and the header verse's final letters encode it — ואלה המשפטים אשר, sof-tevot spell מרה ("Marah"); likewise חק ומשפט at Marah = the heifer-statute + the judgments (פרה minus its mem = מרה). Pre-Sinai promulgation stamped into the verse's final letters.
- **Kli Yakar Exod 20:22 + 21:1:1-7** — the grand altar-judge essay: sword = pride (חרבך גאותך), steps = ascent-arrogance, nakedness-pride link ("the arrogant is as one who committed all the arayot"). Sanhedrin 7b parsed by TAGGING: bar Kappara's deliberateness-lesson is labeled דרש; R. Elazar's don't-step-on-heads is NOT — it's pshat via kal-vachomer from the stones (stones cannot resent disgrace, yet Torah shields them; your fellow, in the Creator's image, how much more) — and the juxtaposition is still needed to extend it to JUDGES (else: a judge must cast fear, maybe he MAY step; or "the judge outranks the priest — dayo"). Deliberateness reading: judging without deliberation IS the pride-ascent — he wants to show mastery, won't consult the book; Rashi's במרוצה = hasty cutting. Harmonization: על מזבחי = "BESIDE my altar" (like וזבחת עליו = אצלו), and the vav of ואלה proves judge-rules were already given above — so BOTH amoraim presuppose the Sanhedrin sits beside the altar; Rashi's comment is their common denominator, not a third opinion.
- **Kli Yakar 21:1:6-7** — MAJOR: the bribery-as-acceleration model. Against "שוחד because giver and taker become one (חד)": the money is what's called shochad, not the person — rather חד = SHARP: judgment-completion is "CUTTING the din"; the deliberate judge cuts with a dull knife (slowly, toward truth); a bribe WHETS the blade — the judge cuts instantly, deliberation dead, "his mind has already agreed to vindicate the giver." Or: the bribe is sharp AS THE SWORD, for "the sword comes to the world for delay and perversion of justice" (Avot 5). Bribery = an acceleration attack on due process.
- **Kli Yakar 21:1:8** — MAJOR: forum exclusivity (לפניהם — not before gentiles even where their law matches, Gittin 88b) opens into the Solomon's-throne midrash: six steps, six inscribed prohibitions — three judicial (don't pervert, don't favor, no bribes) + three cultic (no asherah, no pillar, no blemished offering). Why cultic laws on a judgment throne? Because all six ARE judgment-laws: Solomon learned from the Mishpatim-altar juxtaposition that WHATEVER DISQUALIFIES AT THE ALTAR DISQUALIFIES ON THE BENCH — the throne is the isomorphism's monument, "specifically the matters listed at the end of Yitro."

## Batch 48 digest (20 listings; Kli Yakar 21:1 grand essay + 21:2, 21:4)

- **Kli Yakar 21:1:9-11** — MAJOR isomorphism completed: the altar-pericope was commanded early (no Mishkan yet!) PURELY to precede Mishpatim — "whatever disqualifies at the altar disqualifies the bench." Yevamot 101: "as the court is clean in righteousness, so clean of every blemish" (מום אין בך); Solomon derived it from juxtaposition — and in Deuteronomy ALL expound juxtaposition (even those who don't elsewhere), hence the throne's לא תזבח inscription. Blemish theory: a bodily blemish signals an inner trait; typed mapping — the bribe-taker goes BLIND, the bias-perverter goes LAME ("hops between the boughs"; "he who took no bribe shall never totter" → the taker totters).
- **Kli Yakar 21:1:12** — MAJOR singleton-judge diachrony: pillar-of-one-stone = judging alone ("none judges alone but the Holy One"); the מצבה was BELOVED in the patriarchs' days — Shem, Ever, Abraham, Isaac, Jacob, Judah ("take her out and burn her"), Moses pre-Yitro all judged ALONE, being whole minds unafraid of error; "when hearts diminished, God commanded not to judge alone." Institutional plurality as decay-adaptation.
- **Kli Yakar 21:1:13-14** — whole-stones ↔ judges needing no external repair (the axe's boast: "I appointed you — by yourself you're unfit"); judge-protection k"v: the stones make peace and iron may not touch them — the judge makes peace between man and man, so the bench sits BESIDE the altar to teach him no harm will befall him (answer to fear of the condemned's revenge). Asherah-judge: the unfit judge is planted "for the fortune of his relatives" (אשרה from אשרוני "call me fortunate") — many-branched tree, kin in his shade, "and truly their shade departs." Gentile disqualification GROUNDED: Israel diminish themselves (Chullin 89), the nations are haughty — ומשפטים בל ידעום because arrogance destroys deliberation. Forum exclusivity = humility-capacity requirement.
- **Kli Yakar 21:1:15-18** — MAJOR deliberation model: the king-orchard midrash re-read (the "many sons" = all Israel; the beloved LITTLE one = the self-diminishing humble man — he is chosen for the bench); "if you keep (משמרים) the din, I am exalted" via WINE-LEES (שמרים) theory: judgment must be SOURED/aged (מחמיץ הדין) — let the lees (error, confused notions) settle until the intellect stands clear; judgment ferments, charity must NOT ("do the poor man's request at once"); pursuit-language (צדק צדק תרדף) belongs to charity. Orchard point: the owner hides which planting he prizes so ALL get equal care = כקטן כגדול תשמעון — equal attention to small claims.
- **Kli Yakar 21:1:19** — לא לפני הדיוטות from the same table: the ordained are WHOLE stones; laymen are hewn — need repair "and perhaps it will help"; the commoner has MORE arrogance than the distinguished — disqualified like the nations, same axis.
- **Kli Yakar 21:1:20-24** — MAJOR institutional-response reading: arrogance-in-ruling yields three corruptions (fool — won't deliberate, ashamed to ask; wicked — imitates the One by judging ALONE; haughty — in everything); the MEN OF THE GREAT ASSEMBLY, seeing the First-Temple judicial collapse ("the daughters of Zion grew haughty"), answered with their three dicta AS PATCHES: be deliberate in judgment / raise many students (no one need judge alone) / make a fence (arrogance is the one trait with no middle way — "very, very lowly of spirit"). Psalm 75 then mapped verse-by-verse as the judicial-ethics codex: three אל's against three כי's; no pride from origin (putrid drop), from sunset (dust and worm), or from Torah (given in the WILDERNESS that all tread — Eruvin 54: make yourself a wilderness and Torah is a gift); God's cup is lees-free, the wicked drink lees-mixed = un-deliberated rulings; "I speak hard-as-sinews (אגיד) to BOTH litigants — both as wicked before me until the verdict"; then vindication sorts them. "All this psalm is compressed into the short words לפניהם — not before gentiles, not before laymen."
- **Kli Yakar 21:2:1** — MAJOR-color + settlement-link candidate (Gen 37 ↔ Exod 21:2): opening with slave-release because the Decalogue opens "who brought you out of the house of slaves" — and the NATION ITSELF was sold for a theft: the brothers' sale of Joseph rolled Israel down to Egypt's slave-house, yet you went free — so free your thief-slave. The Joseph-sale as national precedent for thief-slavery-with-release.
- **Kli Yakar 21:2:2** — MAJOR ivri-fork enrichment: עברי = from beyond-the-river, where Abraham's ancestors served idols; entering the Shekhinah's wings they became "Israel"; the thief REGRESSED to the pre-covenant name — and עברי puns on עובר עבירה (transgressor) — yet "your BROTHER the Hebrew": still a brother. Distribution is precise: the sinner is ivri; the blameless self-seller (Behar) is אחיך plain, never ivri.
- **Kli Yakar 21:2:3** — MAJOR: "he is a slave ALREADY before you bought him — the deed of the Holy One is PRIOR" (שטרו של הקב"ה קודם, from כי עבדי הם "for they are My slaves") — the seniority-of-liens principle applied to God's title (joins the שטרי קודם find); the repeat-fool loses even the name ivri ("the slave" in v.5). Six-year term fork, four rationales: standard hire = 3 years (Isaiah) doubled as the double-payment fine; rejected (a hire-year is one); his own — THREE thefts (the owner's money, the owner's mind, the Supreme Mind) → 3 years, doubled by the fine → 6; or the seventh-chosen-for-rest cosmology (Sabbath/shemittah/yovel — "most correct").
- **Kli Yakar 21:4:1** — MAJOR economic-symmetry model of the shifchah permission: three rationales for the wife-first condition — (a) attachment-anchor (won't say "I love my slave-wife"); (b) COMPENSATION PRICING: a married slave saddles the buyer with wife-and-children maintenance — nobody would buy him; the Torah compensates the master with the breeding right; the unmarried slave sells fine without it; (c) procreation: married, the mitzvah runs with the Israelite wife, the shifchah-liaison tolerable; unmarried, his seed would terminate in the disqualified line. The maintenance liability and the breeding right as a priced exchange.

## Batch 49 digest (16 listings; Kli Yakar 21:5-12 + crossrefs, Leket Yosher, Levush HaOrah opens)

- **Kli Yakar 21:5:1-2** — MAJOR piercing-timing logic: R. Yochanan b. Zakkai's "ear that heard do-not-steal" faces "then pierce him at the sale!" Grounding via BK 79b: the thief treats the Eye Above as unseeing, the Ear Above as unhearing — struck in the EAR he denied; not the eye, for blinding would unfit him for service (practical constraint). Why not immediate: NO DOUBLE JEOPARDY ("a man is not judged with two judgments") — payment quits him; court-sale IS the penalty; the self-seller acted under poverty's duress. At six the Torah opens a duress-free exit; choosing servitude FREELY discloses RETROACTIVELY (אגלאי מלתא למפרע) that the servitude never punished him — so the outstanding debts for "do not steal" AND "they are MY slaves, not slaves-of-slaves" (BK 116) both come due, and one piercing settles both. Retroactive-disclosure + single-penalty-for-two-counts mechanism.
- **Kli Yakar 21:5:3** — MAJOR-color door/mezuzah semantics: the door turns on its hinge and stands OPEN (the sluggard-prisoner refuses the opened exit); the mezuzah carries "you shall LOVE the LORD" while he declares "I love my master, my wife" — loves swapped, so the awl pins him at the choice-point: "your choice is fixed here; you shall not move." Plus Proverbs inverted: he keeps vigil at his MASTER's doors, not God's.
- **Kli Yakar 21:5:4** — ADD: Kiddushin 70 "who marries an unfit wife — Elijah binds him and the Holy One רוצעו" read literally as PIERCES (not lashes), learned FROM our slave: freely keeping the disqualified union = pierced in the ear, the only organ that senses the disgrace ("hearing the public: this is your unfit wife, these your blemished sons").
- **Kli Yakar 21:5:5** — ear as whole-body proxy: deafening = full body-value damages (BK 85b), so the one organ carries what strictly the whole body owed — mercy-economics. Then the everyman allegory: the acquisitions-slave who "cannot leave because of wife and children" is the true nirtza; at death they escort him only to the grave's DOOR (Pirkei deR. Eliezer's three friends) and turn back — hence והגישו אל האלהים, the Judgment where none enters with him.
- **Kli Yakar 21:7:1-3** — MAJOR exit-regime ↔ teleology mapping: the Canaanite slave exits by TOOTH AND EYE — his own liberation from acquisitiveness comes only when appetite (tooth) and insatiable eye fail in old age, measure for measure; the Hebrew exits at SIX/YOVEL — Israel's freedom is Torah (the seventh day, the fiftieth), "none is free but who engages in Torah," so he needn't wait for decay; the amah exits at SIGNS — her essence is continuation of the species: able to bear, she must be freed to be matched. Numeric architecture: the seventh set apart at the parashah's head (ובשביעית), middle (60 mitzvot to shemittah per the Yalkut), and end (+10 in shemittah = 70) — man's seventy years, "free among the dead" at the seventh decade.
- **Kli Yakar 21:12:1** — MAJOR structure claim: the parashah mirrors ALL TEN commandments — cattle opens against אנכי (the God-facing tablet), מכה איש against לא תרצח heading the five interpersonal ("even the monetary wrongdoer smites a soul"); rejects Toledot Yitzchak's orderings. Thief-penalties: man-stealer dies (sale = delivery to death; captivity contains all); money-thief pays DOUBLE because desire doubles ("has a maneh, craves two hundred" — hint: ממון written out is all doubled letters); robbers don't covet the double; and the thief commits TWO thefts (owner's money + Owner's mind) vs the robber's one.
- **Kli Yakar 28:17 + crossrefs** — bench-symbolism in the vestments: breastplate rows of THREE (no court under three), stones "inside as outside" (transparency), some cheap some dear (a perutah's case = a hundred maneh), tribes by BIRTH-ORDER (no favoritism, כקטן כגדול); Aharon's non-envy earned the breastplate on the heart. Cloud/glory separation harmonizing Exod 24 with Exod 40; humility network confirms (Lev 6 ash; Num 17 staff; Num 32 the pride-essay re-applied: money = a wilderness, external to the man).
- **Leket Yosher OC 116** — ADD-color liturgical deployment: the SHOVAVIM-TAT leap-year fast-cycle — eight Thursday fasts named by the initials of the portions Shemot through Tetzaveh (Mishpatim the acronym's mem); accepted by rav and community in the synagogue courtyard on Shabbat Vayechi; a teacher with six teaching-hours exempt.
- **Levush HaOrah 21:1** — MAJOR two-channel promulgation topology (defending Re'em's Rashi against the Gur Aryeh): the Decalogue went to the WHOLE assembly (first two from the Almighty, eight via Moses empowered — "Moses spoke and God answered him in a voice"); afterward the thunders CONTINUED and Israel stood in place while God spoke the MISHPATIM to Moses alone in the fog — Israel did not hear; Moses relayed them only after descending, once the thunders ceased; then "return to your tents" and the forty days of the remaining mitzvot. So Mishpatim shares Sinai's SETTING (thunder, assembly standing) but not its AUDIENCE — squaring "the ten words He spoke to your whole assembly — and no more." "The former" excludes the altar-pericope (כה תאמר, not thunder-given); out-of-order placement proven by the vav; juxtaposition = Sanhedrin in the Chamber of Hewn Stone beside the altar.

## Batch 50 digest (21 listings; Levush HaOrah core + Malbim opens)

- **Levush HaOrah 21:2:1** — MAJOR compilation principle (against Re'em AND Gur Aryeh): why כי תקנה must be court-sold — NOT via the repeated-pericope-for-a-novelty rule, but because the two pericopes share NO content (here: six years, wife-giving, piercing; Behar: no-slave-labor, yovel, family exit) and "it is no way of the Torah to split one person's law into two pericopes, each holding unique content" — were both the self-seller, the Torah would have merged them. One-subject-one-pericope; disjoint content proves distinct subjects; the wife/children maintenance split (wife here, children there) is deliberate CROSS-RELIANCE, each pericope leaning on the other.
- **Levush 21:3:1 / 21:5:1** — wife-first rationale: slave-children have NO lineage (עבד אין לו ייחוס), so a wifeless slave would void procreation entirely. Defense of Rashi's "my wife = the shifchah": were it the Israelite wife (maintenance argument), "I love MY MASTER" would be false — he'd stay even hating him, for the food; the love-clause forces the shifchah reading.
- **Levush 21:6:1** — fork-ADD on the piercing mechanics (against Gur Aryeh): from our verse alone the awl pierces the EAR only, door/doorpost merely PRESENTED as witnesses (R. Shimon's "door and doorpost that were witnesses in Egypt"); Deut's ונתת באזנו ובדלת adds THROUGH-piercing into the wood — and the Levush extends the same through-pierce to the DOORPOST if he wishes (against the standard door-only ruling).
- **Levush 21:8:1** — MAJOR fourth reading of לעם נכרי, solving Ramban's "no parallel for עם = one man": עם נכרי = the CONVERT COMMUNITY (קהל גרים). Setup: אם רעה בעיני אדוניה = "bad in her MARRIAGE" — e.g. she's a mamzeret, barred from Israel proper but PERMITTED to marry converts ("a congregation, though not the LORD's congregation"; עם and קהל are synonyms — proof-verses paired). The verse: even to that permitted pool he may not sell her — the father (no servitude-after-servitude) nor the master (never granted resale power). Sale-ban extends to the halakhically-available marriage market. Fork now four-way: gentile / another man / the buyer's household / the convert community.
- **Malbim Ayelet HaShachar 84 / 561** — MAJOR precision gate: "the seventh YEAR" WITH the word שנה = world-calendar years (from Rosh Hashanah); ובשביעית WITHOUT it (our verse) = the seventh of HIS OWN term-clock (from the sale). Term-clock vs calendar-clock encoded in one word's presence. Also: חופשה לא ניתן לה (Lev 19:20) = the manumission DOCUMENT (normal idiom is יצא לחפשי).
- **Malbim Deut 2:4 / 23:1** — periphery: the gradual-conquest principle from Mishpatim's close (מעט מעט "little by little, lest the land turn desolate") governs why Edom/Ammon/Moab stood; the garment-possession scale — full wife = garment spread over her (בבגדו בה, Kiddushin 18b), yevamah-in-waiting = only the garment's CORNER (כנף), Ruth's request as completion. Our verse anchors the possession-metric.
- **Malbim Exod 18:14/24/26** — MAJOR promulgation-before-adjudication: Moses appointed NO judges until Mishpatim was taught — Marah gave only fragments; judges ruling by private reasoning (סברא) would not be ACCEPTED ("every loser would come back to Moses"); Yitro mistook Moses' own method for reasoning; שמע לקול = he weighed the advice but implemented only after the fixed law was public; then appointed courts handled even GREAT matters by the arranged law (כקטן כגדול), sending up only the HARD case (no resolution derivable from the arrayed rules). Fixed public law as the precondition of decentralized courts and litigant acceptance.
- **Malbim 21:1:1-2** — MAJOR four-grade knowledge stack on the header: דבור (say once) → למוד (repeat till grasped; the fourfold teaching order, Eruvin 54) → שימה בפיהם (able to teach others) → אשר תשים לפניהם = knowledge ARRAYED like a thing seen directly (דעת = visual-grade clarity, אתה הראית לדעת). Plus the אשר-rule (his Shemini §63): commands opening with זה/אלה never take אשר; אשר signals the command already given in GENERAL — so אשר תשים proves the mishpatim were given at MARAH in general form, now detailed. The Marah precedent grammaticalized. Ramban: לפניהם = before the JUDGES (parties stand "before" the bench); Gittin 88 both exclusions; R. Shimon: civil law precedes cult because din-truth-peace sustain the world.
- **Malbim 21:2:1** — MAJOR full three-verse assignment matrix: Behar = self-seller; Mishpatim + Re'eh = court-sold; per-difference rationales (self-seller: no six-year cap [Ritva: to yovel unless stipulated; Rashi: six default], no shifchah → nothing to stay for → NO PIERCING, term may be one year → severance inapplicable, his children ALWAYS exit with him — unlike the court-sold's shifchah-children). The יעבוד (bare) vs ועבדך (you-suffix) tension resolved by the middle term: he serves the SON (who stands in the father's place for yiud and field-holdings), not daughter/grandson/brother; the Mekhilta's dialogue re-read as choosing assignments to dissolve that contradiction; in Behar יעבוד עמך restricts more weakly, son included there too.
- **Malbim 21:2:2-3** — עברי parsed as ADJECTIVE ("a slave who is a Hebrew"), not construct ("a Hebrew's slave" = a Canaanite bought from an Israelite — excluded); the ethnic-scope challenge (עברי = beyond-the-river, would include Esau/Ishmael/Keturah — "could the Edomite serve six and the Israelite to yovel?!") reduced. MAJOR asymmetric-address principle (Sifra Behar §79): "YOU treat him as a brother; HE treats himself as a slave" — sale-side verses say אחיך (addressed to the master's conduct), the purchase verse says עבד exactly ONCE (to found the body-title), and only once "so as not to call him slave by way of insult"; GRA's variant adds: "you may not CALL him 'slave' as a taunt."
- **Malbim 21:2:4** — MAJOR convert-slave title-theory: עברי includes the CONVERT (R. Yishmael — "Israel" would exclude him); against BM 71 ("a convert is not acquired as eved ivri — he has no family to return to"): the convert IS sold, but as MONEY-TITLE only (kinyan mamon), never body-title — like one sold to a non-Jew, he serves NO heir; Rambam 1:2/2:12 harmonized (Semag's alternative: a convert with an Israelite mother's family); plus the pilpul construction of a convert WITH a family (via the half-slave-half-free kiddushin chain), against Rava. Title-degree determines heir-service.

## Batch 51 digest (17 listings; Malbim 21:2:5-21:6:1 — the dense technical run)

- **Malbim 21:2:5-6** — our verse fixes the six-year cap ABSOLUTELY (Re'eh's ועבדך שש שנים could read conditionally: severance only if six served; and theft>six-years'-labor might extend the sale — ונמכר בגנבתו); verb lexicon: עבד = committed toil (vs שרת/מלאכה); slave-labor sense needs עבד בו or the hiphil — hence Behar's dignity clauses (no foot-washing; no work outside his trade — כשכיר; not farmed out — יהיה עמך) read onto the court-sold too.
- **Malbim 21:2:7** — MAJOR state/domain distinction: number-first (שש שנים יעבד, Ayelet rule 78) = exact — a RUNAWAY completes six; but ILLNESS counts (Sifrei Re'eh 118; no repayment of medical outlays, from חנם) — because עבד names the bound STATE (sick and idle, he is still "a slave, ready"), while the runaway left the master's DOMAIN entirely. Sick-time accrues, flight-time doesn't.
- **Malbim 21:2:8** — MAJOR shemittah-doesn't-free gate, full topology: ובשביעית without שנה = seventh of the SALE-clock (Ayelet 84; Eruvin 18 day-to-day); against the shemittah reading (which is ALSO "the seventh" bare — והשביעית תשמטנה): R. Huna's redundancy argument ("then what would yovel come to free?"), which itself DEPENDS on the dispute whether yovel counts within the shemittah-week (if yovel can occur without shemittah-counting, the argument fails — R. Yehudah vs rabbis, Nedarim 62/Sifra Behar 14); rabbis of Caesarea bypass: בשנת היובל הזאת — THIS one frees slaves, shemittah never (Sifra Behar 27; Rambam Avadim 2:2).
- **Malbim 21:2:9** — pronouncement vs auto-exit: Re'eh's תשלחנו = mitzvah to SAY "go"; ours = he exits regardless, documentless; חנם attached HERE because in self-exit you might bill him for medical outlays — no; Re'eh omits חנם because the willing sender forgives.
- **Malbim 21:3:1** — MAJOR fork-mapping to first principles: R. Yishmael (free Israelite PERMITTED the shifchah — his לא יהיה קדש reads elsewhere): בגפו = alone, needed to demote אם אדוניו יתן to PERMISSION (Malbim's rule: a "command" where prohibition was assumable is really a license); R. Akiva (free men FORBIDDEN the shifchah): permission-status obvious, so בגפו = בגופו, WITH HIS BODY — the limb-exit doctrine; R. Eliezer b. Yaakov: alone-in/alone-out = the wife-and-children precondition. The בגפו fork is a projection of the underlying shifchah-prohibition dispute.
- **Malbim 21:3:2** — MAJOR redundancy-composition for the male's no-limb-exit: from בגפו alone — master PAYS for the limb (entered whole, exits whole) but might also free him like a Canaanite; from לא תצא alone — maybe free AND paid; together: payment established, so לא תצא would be redundant unless it teaches NO freedom-exit at all (Rambam shoresh 8's sevara made explicit; BeHaG/Ramban dissent — no kenas-transfer, לא תצא as plain prohibition).
- **Malbim 21:3:3-4** — the two-wives assignment via the repeated-noun rule (Ayelet 138: a re-named noun is a NEW referent — had the second clause meant the same woman it would use a pronoun): first clause Israelite wife, second Canaanite. Maintenance-scope carved by the עם-parity lexeme (עמו = full equality, אתו = subordination — kedoshim §32): the ARUSAH (betrothed) and the forbidden wife are excluded from maintenance — not yet "WITH him"; the yevamah-in-waiting excluded by name (יבמתו never אשתו). Sifra/Kiddushin 22; Rambam pesak.
- **Malbim 21:4:1-2** — exclusivity from לו (she is designated to HIM, not licensed generally), mapped to the shifchah-charufah dispute (R. Yishmael: full shifchah betrothed to an eved ivri — asham proves exclusivity; R. Akiva: half-free woman). MAJOR R. Natan ribbui: the redundant וילדה לו בנים או בנות teaches THE MASTER WHO FATHERS FROM HIS OWN SHIFCHAH — the children are slaves; mechanics: אדוניו יתן לו = grants PERMISSION (יתן as license — even ANOTHER's shifchah, per Temurah 30's atnan case; hence תהיה לאדוניה, "HER master," possibly a third party); and the Kiddushin 68b clash (child-follows-shifchah derived from וילדו לו — yet OUR verse says וילדה לו of a shifchah!) dissolved: לו here is PROPERTY-relation (the slave owns his own shifchah; the children are "his" as chattel), not paternity. Possession-לו vs lineage-לו.
- **Malbim 21:4:3** — MAJOR grammar-agreement as status-carrier: תהיה SINGULAR (not יהיו) marks the mother as PRINCIPAL — "her children are like her and follow her" (like ותשר דבורה וברק; ותכתוב אסתר); child-status-follows-mother read from verb agreement. Parallel derivation routes (Yevamot 23 via כי יסיר for R. Shimon; Kiddushin 68 via כי תהיין for the rabbis); R. Yose HaGelili's split-formula case.
- **Malbim 21:4:4** — והוא יצא בגפו (redundant): R. Yishmael — the BOND DISSOLVES at exit, no get (a get-requiring tie would mean he doesn't leave "alone"); needed precisely because his shifchah-charufah carries asham-liability (quasi-tie); hekesh extends: a slave contracts no kiddushin with an Israelite woman. Other view: even the NIRTZA has no limb-exit; R. Yitzchak's a-fortiori on exit-difficulty (six-year slave with EASY exit — six/deduction/document/yovel — gains nothing by limbs; the nirtza with HARD exit surely not) vs the tanna kamma's counter (the nirtza's exit is easy in one way: the master's DEATH frees him — he serves no son).
- **Malbim 21:5:1-3** — אמור יאמר = repetition (Ayelet 38). Symmetric-household requirement: he must love wife-and-children he HAS (here) and Re'eh's כי אהבך ואת ביתך requires the MASTER to have a household too (בית = wife and children); the three עמך's (Sifra Behar): equal food and drink, no public-farmed trade, dwells with him; טוב לו עמך conditions piercing on SHARED prosperity and mutual love ("if the master hates him, how do we force him to keep him?"); neither may be lame, blind, or sick (Kiddushin 22).
- **Malbim 21:6:1** — ADD piercing-venue fork: Rabbi — והגישו אל האלהים = to his SELLERS (the court); and the DOUBLED presentation (to the judges, then to the door) proves the piercing happens NOT in court but at the master's house, "between himself and him."

## Batch 52 digest (16 listings; Malbim 21:6:2-21:9:2)

- **Malbim 21:6:2** — MAJOR word-order jurisprudence on door/mezuzah: rule 199 (novelty LAST — "not this alone but also this") is violated (door, the bigger novelty since unfit for the mitzvah, comes FIRST) → triggers rule 200: when a term TEACHES about its neighbor it comes last — mezuzah teaches the door must be STANDING AND ATTACHED (a door on the ground disqualified). Full Mekhilta dialogue reconstructed: our verse can't cover the piercing itself (else Deut's ובדלת redundant); the through-piercing counter killed by ורצע את אזנו — the EAR ALONE is pierced (against the Levush's through-pierce). Ours = presentation; Deut = piercing at the DOOR only.
- **Malbim 21:6:3** — ADD no-agency rule: אדוניו REPEATED (rule 15: no needless re-naming) → the master pierces PERSONALLY, no agent; אזנו = the RIGHT ear via the metzora chain (Kiddushin 15; Menachot 10).
- **Malbim 21:6:4** — MAJOR pierceability→sellability dependency: R. Yehudah — pierce the LOBE (no blemish → a PRIEST slave is pierceable); R. Meir — the CARTILAGE (blemish → a priest is never pierced → per the Yerushalmi a priest can't even be SOLD; the Mekhilta's parallel: the daughter isn't sold for theft BECAUSE she isn't pierceable — non-pierceable → non-sellable); GRA deletes the priest-not-sold line; Rambam splits (not pierced, yet sold); Malbim defends the girsa via Kiddushin 21b's inquiry.
- **Malbim 21:6:5** — MAJOR CONFIRM of the override registry with tannaitic pedigree: awl-material dispute mapped to systems — Rabbi (kelal-uferat) → METAL only; R. Yose b. Yehudah (ribbui-umiut) → anything (stick, thorn, glass); and R. Yishmael counts our מרצע among the THREE PLACES WHERE HALAKHAH UPROOTS THE VERSE (הלכה עוקבת מקרא: the divorce ספר, the sotah's עפר, our מרצע — Yerushalmi Kiddushin; Sotah 16) — pshat says metal-awl, the received law overrides to any-instrument; Rabbi rejects the override doctrine entirely. The GRA crown-find's citation confirmed at its source.
- **Malbim 21:6:6-7** — CONFIRM the לעולם/ושבתם mutual lock (Kiddushin 15) + Rabbi's two-olam semantics: עולם = a long FIXED span — the yovel (50; Samuel's עד עולם = 50) or a LIFETIME → the nirtza also exits at the MASTER'S DEATH ("yovel arrives — he exits; the master dies — he exits"). ועבדו with suffix (against rule 151's bare form) → serves HIM, not the son; blocks the exit-difficulty a-fortiori; extends to the amah via ואף לאמתך תעשה כן.
- **Malbim 21:7:1** — MAJOR female-servitude exclusion topology, four derivations: (1) only the MINOR is sellable (bogeret excluded a-fortiori from the vows-domain — answering "money from prohibition we don't infer": it's a k"v, not a transfer; na'arah via "already-sold EXITS at signs — unsold shall she be SOLD?!", Nedarim 76/Arakhin 29); (2) איש excludes the MOTHER as seller; (3) בתו not בנו; (4) no self-sale (the law written only on the father — כי תקנה אמה unwritten); the Re'eh symmetric reading (עבריה sold for theft) collapsed: signs release her from the GRAVER sale, all the more from the LIGHTER piercing — non-pierceable → not sold for theft (same inference engine as the priest case).
- **Malbim 21:7:2-4** — father's kiddushin power a-fortiori from the sale-power; amah's money-acquisition via k"v from the Canaanite shifchah with the R. Yishmael/R. Akiva system-split (their קדש positions gate which k"v is available); document-acquisition from ויצאה והיתה. לאמה redundant → the four-way dispute: R. Meir (stipulated no-yiud sale valid), rabbis (sale to PESULIM), R. Eliezer (to relatives), our tanna/R. Akiva: ONE amahood only — no amahood-after-amahood (nor after kiddushin — R. Yose HaGelili; RSHB"Y: none after marriage or servitude).
- **Malbim 21:8:1** — MAJOR revealed-intent trigger: והפדה addresses the FATHER; but the master has six years to designate — when does the father's redemption duty bite? From לא ייעד לשתים כאחת ("he shall not designate two as one"): the moment the master designates ANOTHER, his refusal of THIS one is disclosed → redemption duty fires. Yiud is the pericope's core mitzvah.
- **Malbim 21:8:2** — CONFIRM yiud-mechanism fork: R. Yose b. Yehudah — purchase-money NOT kiddushin; yiud rides on the remaining perutah of service (so an interloper's interim kiddushin binds to the SECOND man; no sale-on-condition-of-retroactive-yiud); vs מעות הראשונות לקדושין נתנו — the sale-money IS kiddushin money (master's later yiud defeats the interloper).
- **Malbim 21:8:3** — the עם-problem again: Onkelos "another man" fails the noun (עם ≠ one man) → Ramban: a VOID-sale warning to father and court — to a GENTILE he has no power at all (לא ימשול = if sold, unsold); plus Malbim's unification: reselling her even to an Israelite FEELS like sale to a foreign people — she has become native to the master's house, and after betrayal every new house is a foreign nation. Psychological-foreignness bridges the fork's readings.
- **Malbim 21:8:4** — MAJOR system-level integration of the בגידה fork: R. Yonatan — the FATHER betrayed (daughters belong at home; cf. Rachel and Leah's "are we not counted to him as foreigners? for he has SOLD us" — settlement-link candidate Gen 31:15 ↔ Exod 21:8); R. Yishmael — the father is blameless (sells only in destitution, Rambam 4:2): the MASTER betrayed the yiud-understanding. Ketiv/qere mapped to systems: R. Eliezer follows the MASORET (לא — never designated), FORCED by his Shammaite divorce law (no divorce without ervat davar → the "designated-then-displeased-then-divorced" scenario unavailable) and his kiddushin-holds-in-lav-unions view ("bad in her marriage" = sold to pesulim); R. Akiva follows the MIKRA (לו — designated, then displeased, then divorced — open to him who permits divorce "even for a prettier one"), and for him lav-unions take no kiddushin, so the pesulim reading is unreadable. The textual fork is a projection of divorce-law and kiddushin-law commitments.
- **Malbim 21:9:1-2** — son-not-brother from word order: fronted noun (ואם לבנו ייעדנה) where the clauses share neither noun nor verb (so no "division" licenses fronting) → לבנו is EXCLUSIVE: not the brother (whom yibbum-succession would otherwise promote — and the son's yiud-succession is the SOURCE of his field-holding succession, Sifra Bechukotai 98, so the brother would ride along everywhere). כמשפט הבנות circularity resolved by the explicit-in-itself rule (Tzav §85): R. Yoshiyah (the maintenance triad written of the AMAH) → the verse "comes to teach and turns out taught" — the triad extends FROM her to ALL daughters of Israel; R. Yonatan (triad written of the Israelite wife) → the verse teaches the AMAH from her. Two-directional teaching confirmed with the formal rule.

## Batch 53 digest (11 listings; Malbim 21:10-11 + the doublet-delta and cosmology crossrefs)

- **Malbim 21:10:1** — MAJOR dependent-son economics: אם אחרת יקח לו = the FATHER takes another wife FOR THE SON who designated the amah; puzzle — the new wife's upkeep is the son's, the amah's is the master's, so what does "not diminish" add? Forced: the son is DEPENDENT ON THE FATHER'S TABLE, so the father funds BOTH women equally. From here: the duty to marry off one's minor son (Sanhedrin 76 "near their season"; age-13 debate; "adult but dependent = minor," BM 12b) and the grandchildren duty (והודעתם לבניך ולבני בניך).
- **Malbim 21:10:2-3** — MAJOR the three-obligations fork mechanized: שאר lexicon (the PERMANENT flesh → food-that-becomes-flesh / unmediated kin / one-flesh union); עונתה from affliction (deprivation of food or bed) or from עת (season). The tannaitic three-way (R. Yoshiyah: food/clothing/conjugal; Rabbi: conjugal/clothing/food; R. Yonatan: ALL THREE terms = clothing, fitted to her body and the season) mapped to (a) WHOSE triad it is — amah (R. Yoshiyah) vs the new Israelite wife (R. Yonatan), (b) whether wife-maintenance is deoraita (Rabbi) or rabbinic (R. Yonatan — so שאר can't be food for him; Ketubot 47b, Semag, Yereim), and (c) the novelty-last ORDER rule generating each list's sequence. לא יגרע ("diminish") argues R. Yoshiyah's side: גרע = reducing an ALREADY-FIXED quota — the amah has one, the new wife doesn't (else the verb would be "withhold").
- **Malbim 21:11:1-2** — MAJOR שלש אלה assignment closed: the triple = yiud-self / yiud-son / redemption, NOT the marital triad — because post-yiud she is a WIFE exiting only by get, so ויצאה חנם (signs-exit) would be impossible; and "free from the GET" is killed by the self-gloss אין כסף = free means no-MONEY. Post-yiud hybrid (Kiddushin 18): the amah-exits aren't annulled for her — designated, she may still leave by six/yovel/master's death without a get (לא לבטלה הלכתא מינה). Two-exits topology completed: אין כסף negates even the kiddushin-money-return hava-amina (in naarut the father holds kiddushin rights and the master's money was quasi-kiddushin — you'd think it returns; NO money) — whence "no money to THIS master, but money to ANOTHER master: the father"; Rabbah/Abaye (does one body allow "this-teaches-that"? bogeret needed only for the AYLONIT who skips naarut) mapped onto the Mekhilta's tannaim; R. Natan's boundary: pre-signs redemption costs (והפדה), post-signs costless — the תן-כסף/אין-כסף line.
- **Malbim Exod 32:1** — ADD-color settlement-link candidate (Exod 24:10 ↔ 32:4): the calf as corrupted copy of the OX-FACE — the elders (Mishpatim's end) saw the Throne-channel (לבנת הספיר, providence), the nobles saw only the lower ox-face from the left; the masses, expecting Moses to bring a Presence-bearing form (the cherubim), fashioned the ox they'd glimpsed. Two-grade Sinai vision as the calf's epistemic root.
- **Malbim Exod 34:13** — MAJOR doublet-delta mechanism: why Mishpatim's parallel (23:24) omits asherah-BURNING and Ki Tisa (34:13) adds it — before the calf Israel could not prohibit what wasn't theirs ("none forbids what he doesn't own," AZ 53); by worshipping the calf "they revealed their mind that idolatry pleased them," making the gentiles their AGENTS (שליחותא דידהו) — the asherot became forbidden, hence burnable. The Exod 23↔34 delta explained by an agency-state change caused by the calf.
- **Malbim Behar 7:1** — MAJOR-color cosmological quantification: shemittah completes the SABBATHS the land worked through (your ox rests weekly, the land doesn't — one year in seven repays the six years' sabbaths; hence Mishpatim juxtaposes Sabbath and shemittah, 23:10-12); human days (daily spin) vs "days of the earth" (annual orbit) — earth-days aggregate to an earth-year at FIFTY, called עולם: ועבדו לעולם = one earth-year = the yovel-span; 120 yovels in 6000 years ↔ "his days shall be 120"; the seventh millennium the earth's sabbath.
- **Malbim Behar 27:1 / 58:1** — the demonstrative gate: הזאת (restrictive "this," Tzav §23) — בשנת היובל הזאת excludes SHEMITTAH from slave-release (explicitly guarding ובשביעית from the shemittah reading); וזה דבר השמיטה conversely excludes yovel from debt-release. And the ketiv/qere doctrine: "the QERE is always primary; the KETIV comes for derivation, never the reverse" — the masorah's three Torah alef-written/vav-read cases (אשר לא יעדה OURS — yiud precedes redemption; לא כרעים; לא חומה), the walled-city sanctification dispute, and the Rambam-Raavad riddle resolved (even the annulment-view concedes the derivation for First-Temple times). CONFIRM Minchat Shai's registry with the qere-primacy rule.

## Batch 54 digest (4 listings; Malbim Leviticus grammar-theory crossrefs)

- **Malbim Tazria 4:1** — lexical: בן (from בנה, "builds the father's house") = a VIABLE completed child; זכר/נקבה = any sexed birth, completion not implied; our chapter supplies the בן-pattern proofs (בנים או בנות 21:4; בן יגח או בת יגח 21:31 — block-3 vocabulary).
- **Malbim Tzav 132:1** — ADD intent-gate on soul-penalties: הנפש (singular) excludes the COMMUNITY from karet (never communal — nine Sifra sites + Mekhilta Mishpatim/Tisa); ההוא excludes the coerced/inadvertent/misled — karet strikes the SOUL, and an act without knowledge-and-will is not a soul-act ("the self that sinned in error was the body, not the person"). The 36-karet census with the עונו-ישא / ערירי / מיתה equivalence derivations.
- **Malbim Vayikra 12:1** — MAJOR: the conditional-syntax system with OUR laws as paradigm. Five conditional markers (כי / אם / אשר / participle+article / infinitive+ב-כ); structure rule: a multi-branch statute OPENS with כי and forks with אם — flagship: "כי תקנה עבד עברי… אם בגפו… אם אדוניו יתן… ואם אמר יאמר" and "וכי ימכור… אם רעה… ואם לבנו… ואם שלש אלה" — the case-tree syntax formalized (כי = "when"/certainty; אם = fork/doubt; all four markers denote OPTIONALITY; only infinitive+ב marks obligatory conditions). And the ORDER theorem: Leviticus/Numbers (God-facing) put the NOUN before כי ("a man, when he would offer" — the person under duty is the topic); MISHPATIM and Deuteronomy (interpersonal) put the VERB first ("when a man strikes…") because the law rides on the EVENT — "the matter hangs on the happenstance of deeds and men's dealings." Subject-first vs verb-first as the grammatical signature of God-facing vs man-facing law.
- **Malbim Vayikra 148:1** — CONFIRM+mechanics of the three-obligatory-אם registry (R. Yishmael, Mekhilta Yitro/Mishpatim): stone altar; אם כסף תלוה (ours, 22:24); the omer's אם תקריב — with R. Yehudah's time-contingency theory (אם fits duties "destined to pause and return" — Temple and settlement losable; likewise ואם יהיה היובל) and R. Shimon's as-if-freely-willed pedagogy (perform the compelled offering as a gift); plus the fulcrum rule: the word after אם is the division's pivot (proof-set includes Behar's ואם מעט נשאר בשנים — our pro-rata clause family).

## Batch 55 digest (29 listings; Malbim tail + Psalms 119 cycle + Marot HaTzoveot + Maskil LeDavid)

- **Malbim Vayikra 381:2** — ADD-lexical: the passive-prefix vocalization split — kamatz-form = CONTINUATIVE state, shuruk = the act-moment; והפדה (our 21:8) listed in the kamatz-continuative registry (the redemption-duty as a STANDING state); the payoff modeled on אשר הפקד אתו: "as long as it REMAINS with him he returns it in kind; not with him — he pays value."
- **Malbim Nehemiah 9:13** — ADD taxonomy: the verse's four law-kinds mapped onto our chapter — משפטים = interpersonal judgments (the pericope's core), תורת אמת = belief-matters, חוקים = kid-in-milk (23:19), מצות טובים = the lending law (22:24). Sinai's grant = "the Decalogue and the whole stretch through the end of Mishpatim."
- **Malbim Psalms 119 cycle (~18 mishpat-verses)** — the mishpat-epistemology essays: משפטים = the REASON-ACCESSIBLE law, known first by binah (אודך ביושר לבב) then matured to visual-grade daat (בשפתי ספרתי); the materialism barrier (greed resists property-justice — the husk to be peeled); faith balances the theodicy ledger; 119:102 — though mishpatim are rational norms "one might think to judge otherwise by reason — I did not depart from YOUR judgments, for You taught me": divine positive law overrides private reason (the promulgation module's epistemic twin); 119:106 — the judge's oath and its two obstacles (power-lack, knowledge-lack); 119:160 — human legislation CHANGES with time and opinion, God's משפט צדק "stands forever, true in all times and all cases."
- **Marot HaTzoveot I Kings 2:28** — MAJOR settlement-link candidate (I Kings 2:28-34 ↔ Exod 21:14): Joab's three asylum ERRORS (the tent shelters only a priest at service; only the Temple; only its roof) — then, seeing his error, he left the horns and STOOD BESIDE THE ALTAR = the Sanhedrin's seat ("for thus they said: Mishpatim was juxtaposed to the altar to set the judges beside it") — the flight re-read as a demand for TRIAL. Block-2's מעם מזבחי תקחנו למות running live in Kings, threaded through the beside-the-altar doctrine.
- **Maskil LeDavid Deut 15:18** — CONFIRM the compulsion/permission split on the shifchah: אם אדוניו יתן לו אשה gives only PERMISSION; משנה שכר שכיר ("double a hireling's hire" — day AND night service) gives the master power to COMPEL; each verse teaches what the other lacks.
- **Maskil LeDavid 21:1:1** — MAJOR Marah-core vs Sinai-details layering: the pericope IS a separate divine speech, but God omitted the וידבר header so the altar-juxtaposition would stand unbroken; having therefore to write אלה (to mark the new speech), the VAV became necessary lest one expound "אלה disqualifies the former" as CHRONOLOGY — "THESE came first, at Marah (שם שם לו חק ומשפט), and the Decalogue later" (no earlier-and-later in the Torah); the vav teaches: their CORE is Sinai's like the Decalogue's. Marah gave only the ESSENTIAL dinin (per Sanhedrin 57: = the Noahide-grade dinim; fines and injury-law NOT given at Marah); every detail here is Sinai. Dissolves Re'em's forced chronology.
- **Maskil LeDavid 21:1:2-3** — the set-table TRIGGER identified: not the word שימה (common with words — proofs listed) nor the tools-drash, but the REDUNDANCY plus the crediting of MOSES as placer though he is only the interpreter → the command is PEDAGOGY: no rote recitation; explain reason and sense "until the small and the great understand." לפניהם double-loaded (else write בפניהם or בפיהם): show-the-faces AND not-before-gentiles; Yitro's וישם לפניהם = "he enlightened their eyes" + honoring the elders first.

## Batch 56 digest (19 listings; Maskil LeDavid core + Mechokekei Yehudah + Megalleh Amukkot)

- **Maskil LeDavid 21:2:1-2** — CONFIRM+forks: the naming-license fork — per his Mekhilta reading it is PERMITTED to call him "slave" even by way of disparagement ("the Torah called him slave against his will"), against Malbim's "only once, never as insult." Acquisition-source analysis (bought from a Hebrew = already circumcised → והתנחלתם inapplicable); the עברי-עברי gezerah shavah with the mufneh-on-one-side objection, and the CONTEXT fallback (דבר הלמד מעניינו: a Canaanite slave would wreck בגפו יצא — his shifchah-wife is his own kind — and the ear-at-Sinai drash); כי תקנה עבד (not לעבד): he is a slave BEFORE purchase — the court-sale made him one; the hava-amina that the court-sold's term tracks THEFT-SIZE (no six-cap) killed by our verse.
- **Maskil 21:3:1 / 21:5:1** — ויצאה with the verb on HER = her maintenance was the master's until now; and the clean defense of Rashi's shifchah-wife: this verse-pair mentions only אשתו (children's food comes from Behar), so ואת בני in the declaration can't be Israelite children — they must be the shifchah's, hence אשתי = the shifchah.
- **Maskil 21:6:1-2** — venue fork variant: Rashi (self-seller also pierced) reads Rabbi as: court-sold pierced [via the court]; the SELF-SELLER pierced privately "between himself and him." Mezuzah-side question (two doorposts — which?): unanswerable by gezerah shavah (מזוזה vs מזוזות, non-mufneh) — dissolved because the mezuzah exists only for the HEKESH (door standing like it), never for practice; Rambam's two-stage structure answers Re'em; maybe המזוזה = the distinguished one (bearing the scroll, like הירך המיומנת) — or even the left is kosher for presentation.
- **Maskil 21:6:3** — MAJOR timing-by-repetition + doorway epistemology: the "why the ear" question only bites AFTER the metzora gezerah shavah fixes the CARTILAGE (painful) — else the lobe-choice reads as mercy ("choose him a fine piercing," where women wear earrings). Text-correction: Rashi's "heard לא תגנוב" must be לא תגנבו (Kedoshim, property-theft — the Decalogue's is kidnapping; proof: כי לי בני ישראל עבדים is Behar, and "Sinai" covers all Torah). Why pierce only at SIX: he SECONDED the sin (R. Elazar HaKappar's nazir logic) — the court-sold thief now REVEALS contentment in slavehood ("who multiplies slaves multiplies theft" — his choice discloses the thieving affinity), or violates "they are MY slaves" atop the theft. Why the doorway even for the court-sold: the thief works in darkness as if the Eye above doesn't see; the Passover blood went INSIDE the lintel and doorposts ("a sign for YOU, not for others") — all is open before Him; the thief refused the doorway's lesson, so the doorway takes his ear.
- **Maskil 21:6:4 / 21:7:1 / 21:8:1 / 21:10-11** — לעולם must mean yovel because it is written of ONE MAN's span ("is he alive forever?!") unlike the collective לעולם בהם תעבדו (a standing rule for Israel) — referent-scope fixes olam's sense. Minor-only from hanging the law on the FATHER. בבגדו as PRESENT participle proves BOTH father and master addressed (a past form would fix the father alone; master-alone yields the absurd resale-after-divorce license). לא יגרע = from the PRE-EXISTING standard. And the grammar trigger on the triple: שלש with SHVA (construct, "the three of…") not kamatz — so it points back to named acts (yiud-self/son/redemption); לה ("for her") proves amah-specific duties (the marital triad fits any wife); the chinnam-from-get hava-amina dissolved — the triple's OMISSION drives the exit, so she was never designated; chinnam = money-free.
- **Karnei Ohr (Mechokekei Yehudah) Exod 21:3** — CONFIRM Decalogue-mirror with Abarbanel's exact partition: TEN mishpatim under "do not murder" (slave-purchase through the pit), EIGHT under "do not steal" (pit through the seducer), FIVE under "do not commit adultery" (seducer to false-witness), TWO under "do not testify falsely," FOUR under "do not covet."
- **Karnei Ohr Gen 1:19** — MAJOR fork on the אלהים lexeme: Abarbanel against Rambam/Onkelos — judges are NEVER themselves called elohim (Torah says shofetim); אל האלהים = "to the DIVINE JUDGMENT": the name designates the JURISDICTION, not the men (like "the king's court" where the king is absent); ibn Ezra's middle way ("the holy ones below who execute God's judgments"). Institutional metonymy vs title-of-office.
- **Yahel Ohr 8:55 / Gen 31:84** — CONFIRM lexical pedigree: Radak (root חנן): ויצאה חנם — the mem is suffixal (like ריקם), "she exits with GRACE, having found favor… every חנם in Scripture interprets as חן." HKV's grace-time etymology (bite 45) has a Radak source.
- **Megalleh Amukkot Beshalach 3** — MAJOR settlement-link reinforcement (Gen 37 ↔ Exod 21:2, kabbalistic-causal form): at Marah, Justice objected to the exodus — the JOSEPH-SALE stood unatoned ("for selling the righteous for silver" — all four exiles from it); Shabbat given as its atonement (Joseph kept Shabbat in Egypt), the red heifer as pre-emptive remedy for the calf (itself traced to the sale via the עלה שור plate), and the DININ = ואלה המשפטים opening with כי תקנה עבד עברי — "the secret of Joseph's sale." The slave-law's opening as the sale's juridical echo; רד"ו arithmetic (10 × 22 − 10 = 210). Behar 6 kabbalistic color: וכי ימכור איש את בתו read on the soul sold into the worlds; onaah as fraud against the soul.

## Batch 57 digest (7 listings; Megalleh Amukkot kabbalistic cycle)

- **MA Mishpatim 2** — ADD-color: eschatological reading — כי תקנה עבד עברי on JOSEPH the near-redeemer; six years = six millennia, "in the seventh he exits free" = Israel leaves the exile chinnam-without-mitzvot; cites עירוב פרשיות כתיב כאן (the interleaved-pericopes doctrine on כי הוא זה, Sanhedrin 2b) and Rav Huna's sovereignty-gate on gentile property ("you may consume the nations WHEN they are delivered into your hand" — when Israel is off its land, even their spoil is forbidden: the High-Table condition).
- **MA Terumah 7** — ADD-color: the Yitro→Mishpatim→Terumah triad as אמ"ת (initials אנכי-משפטים-תרומה — "truth sprouts from the earth"); the midrash "the Torah was Mine and I gave it to you; the MISHPAT was Mine and you took it — now take ME"; three crowns mapped: Torah / kingship (מלך במשפט יעמיד ארץ — mishpat IS the kingship-crown) / priesthood-service.
- **MA Toldot 11 / Vayeshev 54** — color: Isaac's wells as the four worlds with the THIRD well = "the sod of the amah ivriah in the Throne" (וכי ימכור איש את בתו לאמה); עבד כנעני ↔ Sandalfon, עבד עברי ↔ Metatron — the slave-taxonomy on the angelic ladder; בבגדו בה per the Sabba of Mishpatim = the soul's garment (אלוה), לא ימשול למכרה read on the soul.
- **MA Vayeshev 47** — ADD: the marital triad as the soul's CURRICULUM — שארה כסותה ועונתה = Scripture, Mishnah, Talmud ("the soul's food, clothing, and seasons"); Talmud demands גבורה ("the sons of the giant").
- **MA Vayeshev 52** — CONFIRM the Zohar's yoke-rationale in circulation: the brothers called the maidservants' sons "slaves who bear no yoke of the Kingdom of Heaven" — and the slave who refuses the Kingdom's yoke has his EAR pierced (Zohar Mishpatim); Joseph's slander-cycle as the frame.
- **MA Vayetzei 23** — ADD settlement-link candidate (Gen 28:20 ↔ Exod 21:10): Jacob's vow maps the maintenance triad — "bread to eat" ↔ שארה, "garment to wear" ↔ כסותה, "and the LORD will be my God" (the Shekhinah taken with him) ↔ עונתה; the convert's two-tier grant (Deut 10:18 "bread and garment" — no third) contrasted.

## Batch 58 digest (26 listings; Meshekh Chokhmah core + Metzudot lexicon + Minchat Ani)

- **Meshekh Chokhmah Emor 123** — MAJOR compilation-placement principle: נפש תחת נפש for animal-killing sits in Emor, NOT Mishpatim, because Emor's case-law covers even a GENTILE's animal (gentile-damage is GEZEL, forbidden — vs loan-evasion, permitted; the payment clause even licenses handing over an animal though that strips its gizzah/firstling sanctities, Yerushalmi AZ) and the striker of a gentile is judged by HEAVEN (bare יומת; Mekhilta, Isi b. Akavya) — while OUR pericope's header אשר תשים לפניהם — NOT BEFORE GENTILES — bars gentile-party case-law from the chapter. The addressee-header constrains what the chapter may contain.
- **MC Ki Tetze 20** — MAJOR doublet-delta by moral state-change: Exod 23:5 says your ENEMY's donkey (pre-calf: all "a holy kingdom," licensed hatred of a seen sinner, Pesachim 113b); Deut 22 says your BROTHER's — after the failures, whoever searches himself finds his own stumbles, so none is clean enough to hate. Same delta-engine as Malbim's asherah-burning.
- **MC Mishpatim 2-5** — heir-service gated by OWNER's gender (a woman's estate: son = mere heir per R. Zechariah b. HaKatzav → the slave serves neither son nor daughter — reading the Yerushalmi so); the shifchah-union's two-goods analysis (procreation vs sin-avoidance — she supplies only the latter: "a wife whose benefit is only to HIM, not to the creation's completion"); R. Akiva's "designated to him, not ownerless" vs R. Yishmael's compulsion-reading mapped to their shifchah-charufah systems; and the DARK counter-reading of תהיה singular: the master may force the shifchah to nurse OTHERS' infants and not her own — "if the master wishes, her children are not with her" (inverse of Malbim's mother-as-principal).
- **MC Mishpatim 6** — MAJOR consent-scope theory of the nirtza: not-serving-the-son is no leniency but a CONSENT-BOUNDARY — his declaration named the MASTER ("I love my master… for it is good for him WITH YOU"); the son was never consented to ("who knows whether it will be good with him?"). Two hava-aminas dispelled by והוא יצא בגפו: cruelty-exit (nirtza beaten to limb-loss exits like a Canaanite) and nirtza-as-self-seller for shifchah-compulsion.
- **MC Mishpatim 7** — MAJOR yovel-lapse contingency: sold while yovel operates, yovel then ABOLISHED mid-term (ten tribes exiled) — does servitude dissolve or persist? For the nirtza the pshat of ועבדו לעולם becomes LITERAL: he serves all the master's life UNLESS a yovel intervenes — the release-clock can vanish out from under the slave. (Tosafot Arakhin 33; Ramban on pruzbul.) Feeds the yovel dependency-graph module.
- **MC Mishpatim 8-10** — כמשפט הבנות = KETUBAH (for ketubah-deoraita holders); עונתה = "an ANSWER (מענה) to nature's question." MAJOR: ibn Ezra's marital-triad reading of שלש אלה rehabilitated halakhically — post-yiud the amah-exits persist (Kiddushin 18), and per Rava (multiple wives only if he can maintain them) the verse teaches: designated her, married another, cannot supply her triad → COMPELLED to release her; all the more if he withholds in rebellion — "from here, a broad source for ALL the sages' compelled divorces" (כופין אותו להוציא). Per R. Ami it also innovates: the designated amah may be over-married WITHOUT her consent (she was designated without her own da'at — even to a minor son, per the Yerushalmi).
- **MC Shoftim 5** — the isomorphism's shared invariant named: BENEFIT-FREE action. Judgment is God's; the true judge takes nothing — like the Creator, who gained nothing ("who judges truly-to-its-truth becomes God's partner in creation" = both act gratuitously); sacrifices atone the God-facing side, MISHPAT alone the man-facing; the self-serving judge = the asherah by the altar = "saying to the wood: you are my father."
- **Metzudot lexicon set (10 rows)** — CONFIRM: Exod 21 is the Metzudot's STANDARD proof-text across Nakh — ועבדו לעולם cited to gloss every bounded-"forever" (Daniel 7:18, Isa 32:14, Eccl 1:10; Meiri Ps 13 likewise for נצח); כמשפט הבנות glossed "need/custom" (I Kings 8:59); יצא לחפשי חנם for חפשי (Isa 58:6, Job 3:19 "the slave free from his master"); משפטים in Jeremiah = "disputation" (the covenant lawsuit sense).
- **Minchat Ani Mishpatim 1-16** — homiletic cycle: the four avot nezikin as the four sin-drivers (pride-ox, sloth-pit, appetite-tooth, yetzer-fire); the resurrection-allegory of 21:2-3 — man serves six DECADES after childhood's first, exits in the seventh; אם בגפו יבוא = never refined his body (his "wife") → בגפו יצא, the body has no share in resurrection; mastered it → ויצאה אשתו עמו, body rises with soul. And the matron-with-guards midrash on the compilation: dinim BEFORE the Decalogue (Yitro's judges) and AFTER (our pericope) = armed escort fore and aft — judges ahead against the tempting satan, penalties behind against the accusing one ("when there is judgment below, there is none above").

## Batch 59 digest (13 listings; Mizrachi/Re'em core)

- **Mizrachi Deut 15:12/17** — ADD rule-refinement: the repeated-pericope-novelty registry counts only novelties EXPLICIT in the text (the ivriah's six, severance) — hekesh-derived novelties (no-limb-exit) don't qualify. And CONFIRM Gur Aryeh's topology: the עבד עולם assignment can't be swapped because איש selects what applies to a man and not a woman = PIERCING (sale-name applies to women, piercing-name never).
- **Mizrachi 21:1:1** — CONFIRM at source: Rashi's ordering (vav before juxtaposition) decoded — only R. Abahu's אלה/ואלה rule (through R. Yishmael's "as the former from Sinai, so these") proves the pericope OUT OF ORDER, and Rashi comments on juxtaposition only for out-of-order pericopes; the ordinary connective vav (ואם מן הצאן) wouldn't prove Sinai-parity — ואלה = "these are LIKE those in dignity"; אלה alone would DISQUALIFY the former (real disqualification — tohu, the flood generation); the altar-pericope is a separate revelation (every speech had its call), so context alone can't order them; and if neither אלה nor ואלה were written nothing would signal — hence the written ואלה must carry the addition-inference. The essay the Levush defended and Maskil rebuilt.
- **Mizrachi 21:1:2** — set-table micro-mechanics: the trigger is לפניהם where להם would do (the table arrayed before the EATER), atop the שימה-בפיהם fluency duty; the Mekhilta's four stages closing in דעת ("like אתה הראית לדעת — knowing = the reasons"), vs Eruvin 54's show-the-faces version.
- **Mizrachi 21:1:3** — MAJOR consent-curability split formalized: the layman-exclusion bars COMPULSION only — if both parties agree, a layman's judgment stands; the gentile-exclusion holds EVEN WITH consent — "who brings Israel's cases before gentiles profanes the Name and honors idols." The "even where their law matches" clause is needed either because the mismatch-case is banned anyway as GEZEL, or against the thought that דינא דמלכותא דינא legitimizes the match-case — the verse excludes even that.
- **Mizrachi 21:2:1-3** — MAJOR title-amplification on transfer: the construct-reading hava-amina ("a Hebrew's slave" = a Canaanite bought FROM an Israelite, who would then exit at six/yovel, while only the gentile-bought falls under perpetual inheritance) — the SELLER's identity setting the exit-regime, rationalized (the Israelite-bought Canaanite already accepted mitzvot, obligated like a woman); killed by the gezerah shavah. And the ownership puzzle: a gentile owns only his slave's LABOR ("you buy from them, not they from you") — yet when he sells to an Israelite, the Israelite acquires the BODY: "Israel's power is stronger — you acquire from them even the body" (Yevamot; Rambam; Tur). The buyer acquires more title than the seller held.
- **Mizrachi 21:2:4-5** — naming-license at source: עבד written to PERMIT the name ("the Torah called him slave against his will"), freeing Re'eh's העברי as mufneh for the gezerah shavah; the write-neither objection answered by idiom-rule (לכתוב we argue, לשתוק we don't). Text-criticism: "but the court-sold would not exit at six" and "of him it says six years" are NOT in the Mekhilta — Rashi-manuscript accretions; without them the baraita runs per the tanna kamma of R. Eliezer (self-seller sells for six OR MORE); the והגישו "consult his sellers" reading is דרשא בעלמא, not a blocking derivation (absent the miut, both tannaim would pierce a self-seller).

## Batch 60 digest (16 listings; Mizrachi 21:2:6-21:7:2)

- **Mizrachi 21:2:6 / 21:3:1-3** — lexical: לחפשי — the yod is suffixal ("to freedom," not "to a freedman"), chosen because יצא marks state-to-state transition; בגפו = בכנפו ("in his garment-corner" — the single man "has only his clothing"; Aramaic גפא = wing). The מגיד logic: the second בגפו must SWITCH referent (first: no Israelite wife; second: no Canaanite given) — else the verse would just say "as he came, so he exits."
- **Mizrachi 21:3:4-5 / 21:4:2** — MAJOR hava-amina economics: the Mekhilta's "maybe בעל אשה means an Israelite" entertained because BEFORE the maskana, (a) the yiud-restriction might bar only MARRIAGE-transfers, leaving the master free to hand her to the slave for BREEDING (zenut) — like the maskana's own shifchah-license despite לא יהיה קדש; (b) an Israelite wife's children might belong to the master AS WORK-PRODUCT of two bonded workers — child-follows-shifchah is only known FROM HERE. Ramban's objections (how could the master transfer her at all; the children prove Canaanite) answered stage-wise; Rashi argues from the WOMAN (six/signs-exit — "she too exits at six" = the father-sold minor) rather than the children. Maintenance tzerikhuta: children too young to work-and-eat / wife able but modesty bars her begging / children beg by habit.
- **Mizrachi 21:4:1** — fork-ADD left open BY the Re'em: is the master's shifchah-provision PERMISSION or DUTY? The Mekhilta's "permission not obligation" from בגפו runs only for R. Yishmael; on Rashi's own line (R. Eliezer b. Yaakov — the wife-and-children precondition) neither is derivable — perhaps with wife-and-children it is an OBLIGATION (to breed for והתנחלתם, like the obligatory אם of the lending verse): "I do not know whence Rashi says permission."
- **Mizrachi 21:4:3 / 21:6:1** — the love-parallel forcing אשתי = the shifchah (all three declared loves must be the same TYPE — inseparability; the Israelite-wife reading turns "love" into provision-anxiety, and post-exit he isn't separated from her anyway). Two-track piercing: the court-sold — court-presentation ("consult his sellers") + the do-not-steal ear; the self-seller — pierced via the gezerah shavah, possibly with NO court-presentation ("between himself and him"), rationale switched to "heard THEY ARE MY SLAVES and went and acquired a master."
- **Mizrachi 21:6:2** — CONFIRM the fork's origin: the Re'em's standing צריך עיון — why not read our verse as EXTENDING piercing to the mezuzah (Deut's בדלת as base-case, ribbui-chain like chametz/se'or; R. Shimon's "door AND mezuzah were witnesses in Egypt" implies both); and the structural anomaly — NO other Torah word exists solely for a hekesh with no self-referential content, as מזוזה does here.
- **Mizrachi 21:6:4** — MAJOR third resolution of the piercing-timing puzzle: the ear-rationale selects the ORGAN, not the penalty — the piercing itself is גזרת הכתוב whose timing rides the acquired-a-master rationale (fires only at six). The Sinai-verse problem solved by NESTING (the Decalogue's kidnapping-לא תגנוב contains property-theft in its generality — all Torah nested in the Ten, per R. Saadia); the לא תגנבו emenders "err — only the Decalogue was heard at Sinai by all."
- **Mizrachi 21:6:5 / 21:7:1-2** — CONFIRM the עבד עולם tzerikhuta with the sale-name/piercing-name gender split (Tosafot Kiddushin). Derivation-economy on the minor-only k"v: without it, לאמה would be re-purposed (bogeret per Tosafot; or the stipulated-amah/pesulim sales) — the k"v is load-bearing. The hekesh's two-way cargo: עבריה→עברי all exits (yovel), עברי→עבריה money-acquisition AND no-limb-exit ("no hekesh by halves"); the limb-exit hava-amina powered by a-fortiori from the Canaanite; the male-signs-exit closed by the three-route no-minor-male-slave theorem.

## Batch 61 digest (21 listings; Mizrachi tail + Nachal Kedumim/Chida + Nachalat Avot)

- **Mizrachi 21:7:3** — ADD open question (his צ"ע): hekesh normally defeats kal-vachomer when they CONTRADICT — but here both could coexist (hekesh → money-acquisition only; k"v from the Canaanite → limb-exit) — why read the hekesh to kill the k"v? Left unresolved.
- **Mizrachi 21:8:1-3** — CONFIRM yiud-mechanics at the Rashi source: the diyuk — Scripture calls her kiddushin "yiud" (לא יעדה, not לא קדשה) → no new kiddushin; purchase-money = kiddushin-money. והפדה (not ונפדתה) = the master ENABLES redemption; and the load-bearing need for it beyond the hekesh: the FORCED redemption — מפדין אותה בעל כרחו של אב, they redeem her AGAINST THE FATHER'S WILL for the family's blemish (new module: compelled redemption against the seller). Money-acquisition itself from the אחרת-hekesh, both directions.
- **Mizrachi 21:8:4** — MAJOR rhetoric-of-equivalence on לעם נכרי: the received reading (Onkelos, from R. Eliezer/R. Yehoshua "man from man back to Moses") is "another MAN," and the verse's gentile-word is deliberate — reselling her to ANY Israelite "is counted as if selling her to a GENTILE"; the Mekhilta's court-warning (no actual gentile-sale) then DERIVES from the equivalence (if resale is "like" gentile-sale, the real thing is surely barred) — one warning, not two (against Ramban; hence the poskim's silence).
- **Mizrachi 21:9-11** — succession-mechanics: the son's yiud-formula "you are designated to me by the money my father received in your purchase" — he stands in the father's place, so money he never paid serves as HIS kiddushin. אם אחרת יקח לו only post-designation ("no onah except for a wife"); לא יגרע from the PRE-QUOTA holder; the deoraita-maintenance pedigree massed (Rambam/Semag/Rashba/Tur deoraita vs Ramban's rabbinic; Semag's asmakhta-reading of the k"v like the Megillah k"v). שלש אלה = ANY ONE of the three (all-three-at-once impossible; designated-but-unmaintained is a full wife, get-only). The naarut/bagrut ORDER inversion: Rashi reads the written verses in textual order (chinnam=naarut, ein-kesef=bagrut ribbui); the gemara's counterfactual runs the other way (Rava's this-teaches-that vs Abaye's aylonit — and the Mekhilta sides with Abaye).
- **Nachal Kedumim (Chida) 21:1** — ADD tiered-promulgation, esoteric version: the vav read "and-these IN ADDITION to the secrets you know — but set before the MASSES only the plain laws (all levels of pshat); the sodot only to elect holy individuals." Secrecy-policy on the header.
- **Chida 21:2 + 21:7** — color: R. Ephraim's cipher — תקנה = הנך in the אטב"ח pairing (the unpaired letters witness God's Oneness; the self-seller forgot the One; joins Sukkah 52b's מנון cipher); Maharchav: עברי = "a passer-by" (Jonah's עברי אנכי — this world a corridor, hence the fear of Heaven); the seasonal stamp — final letters of וכי ימכור איש את = תשרי (autumn, flax-maids hired), initials of אם בגפו יבא = אביב (spring, field-hands hired). MAJOR-color: R. Ephraim's full scholar's-biography allegory of the pericope — sixty years' service, the seventh decade free; אשה = Torah; children = students; NOT-lishmah → "the woman and her children are her MASTER's" (the Torah stays God's, not his); the declaration = the scholar refusing even the grave's rest; the door = "this is the gate of the LORD"; ועבדו לעולם = the resurrection-world.
- **Nachalat Avot (Abarbanel) 3:6** — CONFIRM the divine co-processor doctrine via Psalm 82: "in the midst of ELOHIM He judges" = when THREE judges (titled elohim from OUR והגישו אדוניו אל האלהים) convene, GOD JUDGES AMONG THEM; the psalm's rebuke flows from that Presence ("I said you are elohim… but you shall die like ADAM" — like the first man forfeiting immortality); when the bench fails, "Arise, O God, judge the earth" — the jurisdiction reverts.

## Batch 62 digest (20 listings; Nachalat Ya'akov + Netinah LaGer + Od Yosef Chai + Ohel Ya'akov)

- **Nachalat Avot 4:21** — ADD-lexical deployment: Abarbanel uses our bounded-olam (ועבדו לעולם) to argue Daniel's "everlasting life" doesn't prove the resurrected immortal — the slave-verse as the standard cite for finite-forever even in eschatology.
- **Nachalat Ya'akov 21:1** — ADD the COLORLESS-JUDGE model: "the wise shall shine as the RADIANCE of the sky" (BB 8b) — radiance = the tintless (the hyle-glass taking every form): the judge must carry NO hue of his own, so each litigant's inside shows true and the FRAUDULENT CASE (דין מרומה) is detected; same for the charity-warden's allocations; teachers = stars (light-givers). Neutrality as optical transparency.
- **Netinah LaGer (Onkelos analysis)** — MAJOR cluster, the Targum as posek: (1) Onkelos renders עברי as "Jew" EVERYWHERE except עבד עברי (21:2) and אחיך העברי (Deut 15:12) = בר ישראל — a deliberate fence EXCLUDING the beyond-the-river reading (Ishmael/Esau/Keturah) from the slave-law's scope; (2) at 21:6 he renders לעלם bare, not "to the yovel" — literalism where the received law diverges from pshat; (3) at 21:8 he follows the QERE (דיקימה לה, "whom he designated") though a manuscript Targum reads the KETIV (דלא מקימא) — the ketiv/qere fork replicated inside the Targum tradition; his והפדה sits on the MASTER (yiud-precedes-redemption), so "another man" must mean no resale even ON CONDITION of yiud; במשלטה aligns with the since-he-betrayed reading; (4) at 21:10 שארה = זיונה (SUSTENANCE) — the Targum rules maintenance-DEORAITA (with Rav Ashi's Mekhilta line; Rambam/Rashba per the Maggid Mishneh concur; against Ramban's rabbinic reading, quoted at length); זיונא = any food vs מזונא = the satiating (Berakhot 44a with Rashi). Also בספי (Deut 6:9) = "on ONE of the posts," explicitly parallel to אם שלש אלה = "one of three."
- **Od Yosef Chai (Ben Ish Chai derashot)** — ADD promulgation-color: teach the mishpatim ON SHABBAT — the rest-day is when the people absorb and retain the law (his cipher on לפניהם/שבתכם); the SHOVAVIM cycle again in six-portion form (Shemot–Mishpatim; 42 days = the 42-letter Name; covenant-repair by Torah-study, not fasting alone) — variant of Leket Yosher's eight-portion custom. Color: חנם = "from the eighth" (Binah, in whose authority all freeing of slaves lies — the Idra); בגפו = גוף inverted (the soul-treasury; the penitent exits through it); the learned-daughter parable reading בנים או בנות as WORK-PRODUCTS (male-typed and female-typed crafts as "sons" and "daughters" — resonates with the Mizrachi hava-amina of children-as-work-product); מרצע split מר-צע — the awl names the UNDONE covenant-letters (צ"ע ciphers to ל"י of כי לי בני ישראל עבדים: he untied the to-Me bond).
- **Ohel Ya'akov (Dubno Maggid) Ki Tisa 5:12** — MAJOR-color enabling-condition theorem: "You established uprightness" — God PARTITIONED PROPERTY (each his share) precisely so that mishpat and tzedakah could EXIST: were all things God's undivided, there could be no justice (respecting another's holding) and no charity (giving one's own). Ownership as the created substrate of the entire law of the parashah. Masei: Zion's thief's-brother parable — ציון במשפט תפדה = Zion alone can claim redemption by strict JUDGMENT (punished beyond desert), the exiles only by charity.

## Batch 63 digest (2 listings; Ohel Ya'akov Yitro + the giant Ohr Zarua I 744 responsum — READ IN FULL, 32k chars, paged in 4 chunks)

- **Ohel Ya'akov Yitro 7:6** — ADD predictability doctrine: the bribe-free judge rules CONSISTENTLY, so litigants LEARN law from his precedents ("the loser learns for the next occasion; the rulings agree and are jointly right"); the bribed judge "turns like a door on its hinge," flipping ruling to ruling — no precedent, no teachable law. Consistency as the precondition of law's teachability.
- **Ohr Zarua I 744 (R. Yitzchak of Vienna, responsum)** — MAJOR cluster, four holdings:
  (1) Authentication theory: min haTorah NO document needs kiyyum — signed witnesses are "as if examined in court" (even a known robber's document: forgers fear detection); kiyyum is rabbinic; once a court has READ the document (הוחזק בב"ד) even the signers can't retract ("having spoken, one does not re-speak" applied to signatures; Yerushalmi Shevi'it on antedated notes); hence the kiddushin-document case: she stays married deoraita though the witnesses deny their hands — a get is required.
  (2) MAJOR gentile-document validity matrix (forum-exclusivity's civil-recognition boundary): the mishnah's valid "erka'ot documents" = only FORMAL courts with judges KNOWN bribery-immune (Rach: "the fixed seat of judgment… judges far from falsehood and bribery"; Alfasi: their ordinary fixed judges are NOT mishnaic erka'ot absent that knowledge; Rambam's checklist — money paid in their presence, drafted in the formal court, Israelite witnesses attesting the gentile witnesses AND judge take no bribes — "else it is a potsherd"). A deed made in a mere gentile GATHERING (כינופיא דארמאי) is void even if gentile judges later ruled and awarded possession on it; דינא דמלכותא דינא runs only through the king's ordained formal channel (Rashbam: the subjects willingly accept the king's laws — hence full law) — never validates the informal notariat. Recognition of gentile legal ACTS strictly narrower than the bar on gentile FORUMS.
  (3) The wall-niche ark ruling (storage-built vs honor-built: לנטורי עביד carries no tashmishei-kedushah status; a niche that damages the scrolls "is not their servant but their damager") — periphery.
  (4) MAJOR MAJOR — the header-verse as FAMILY-LAW PROCEDURE GENERATOR: get-delivery at NIGHT is VOID, because ואלה המשפטים אשר תשים לפניהם "speaks also of GITTIN" (from Gittin 88b — the compelled-get scene with אנן הדיוטות אנן and R. Tarfon's not-before-gentiles/not-before-laymen baraita): get-procedure is a משפט; judgment BEGINS only by day ("day for the din's start, night for its completion" — ושפטו את העם בכל עת vs ביום הנחילו); delivery = the din's START (it opens her ketubah-claim and her permission), so night-delivery fails even POST FACTO — like night-chalitzah (pesak: invalid — R. Eliezer's line, Rambam, Alfasi's seder chalitzah, the Geonim); kal-vachomer from conversion (גר has "mishpat" → no night immersion though no money rides on it — a get, which activates ketubah/inheritance, all the more). Yet ONE judge suffices deoraita (the three of get-authentication are rabbinic; R. Acha b. R. Ika; Rav Nachman's "like me, one judges alone"); the two delivery-witnesses must know how to READ the get; witness-becomes-judge if he saw by day; authentication itself MAY run at night (rabbinic, gemar-din-like). Signed with the humility-close: "I will not act on this until my masters of the Rhineland and France answer."
  (5) The get's TOREF (his name, her name) is deoraita-core (the topes/toref analysis; Yerushalmi "from its invalidation learn its validation"; R. Simchah's pesak); sotah-scroll contrast (her name unneeded — stam is valid there, stam is invalid in a get).

## Batch 64 digest (35 listings; OR HACHAIM opens — 21:1-7 + crossrefs)

- **OC Deut 15:12** — CONFIRM-refine with fork-note: the illness/flight split assigned to the verse-pair — שש שנים יעבד carries illness-completion, ובשביעית (Re'eh's phrasing) carries the runaway's completion (even one year's flight) — the reverse assignment from Malbim's (who hung the runaway on number-first שש and illness-forgiveness on חנם).
- **OC Deut 21:11 (Zohar II 97a)** — color CONFIRM of the soul-reading: לעם נכרי לא ימשל למכרה on the soul — "who could sell his own soul?" — בכסף read as כוסף (CRAVING): through craving men sell their souls to the enemy.
- **OC 21:1:1-5** — the ואלה dispute mapped onto Zevachim 115b: R. Yishmael (generalities at Sinai, details at Ohel Moed) NEEDS ואלה to make these laws' DETAILS Sinai-given — an exception; R. Akiva (all details Sinai anyway) must read it as set-table pedagogy. Rashi's split loyalty (R. Yishmael here, R. Akiva at Behar) left in צריך עיון; the Re'em's thunders-reading rejected ("who would say God thundered more than the Ten? — a third revelation-mode without parallel").
- **OC 21:1:6** — MAJOR rights-notice principle: Torah divides into universally-obligatory knowledge (kashrut, Passover — covenant-membership basics) and specialist law (procedure, calendar, sacrifices) where lay ignorance is tolerable. Slave-law LOOKS specialist, but תשים לפניהם commands it set before ALL: the buyer must know what he acquires, the SOLD MAN must know God freed him after six — else he cannot claim it — and the judges can't track every sale; hence the direct address כי תקנה, every buyer personally spoken to. A release-right unpublished is a release-right void.
- **OC 21:1:7** — ADD consent-engineering: the six-year release cuts against buyers' interests; "set it before them" = present the law so each accepts it as HIS OWN insurance — every Hebrew slave was once solvent, "the wheel turns," and each buyer should see himself as the possible slave. Law-presentation as consent-building.
- **OC 21:2:1-6** — CONFIRM cluster: buy-Hebrew-FIRST priority (given the choice, don't prefer the perpetual Canaanite); עברי avoids fixing "slave" on Israel and signals TRANSIENCE (עובר, passing); sin-origin note (even the self-seller "reached this only through prior sins" — R. Ami); word-order = slave BEFORE purchase (heaven's court already ruled); עבד explains the cap (he is already GOD's slave, your title is derivative); יעבד bare → serves the son; ובשביעית = may serve into the seventh calendar year (mid-year sale, day-to-day completion; found in Rambam's Mishnah-commentary).
- **OC 21:3:1-5** — the entry-timestamp doctrine: the WIFE must exist at ENTRY (בגפו יבא), children may arrive later; wife died mid-term → permission stands (the verse fixed the entry-moment); without the received tradition he'd have read אם בעל אשה as requiring her until exit. MAJOR split-filter: for the SHIFCHAH-PERMISSION even a lav-forbidden wife counts (Rambam 3:4); for MAINTENANCE only the fitting wife (arusah and shomeret-yavam excluded by אשתו/עמו). One word אשה, two clauses, two different tests.
- **OC 21:4:1-3** — MAJOR anti-retention rationale for the wife-first condition: a lifelong-single slave given a shifchah faces TWO losses at exit (family severed + renewed solitude) and will refuse freedom — the Torah forbids the master to engineer that attachment; the shifchah goes only to the already-married, whose exit stays easy (his free wife awaits). The condition as a ban on golden-handcuffs retention. The person-shift (כי תקנה direct → אם אדוניו third person) serves the rationale-narrative; אמר יאמר doubled = he insists DESPITE the built-in tikkun.
- **OC 21:4:4-10** — MAJOR-color, the third full-pericope allegory (body/soul): עבד עברי = the BODY, the soul's passing servant (עברי = transient); sixty-year term, the seventh decade exit; חנם = by the hand of SAMAEL's hosts — "freeness" itself is the impure side's signature (holiness costs dearly; impurity comes free); בגפו from גף = WING — mitzvot as the wings of resurrection; אם בעל אשה = he who EARNED his soul and became its "husband" (it stays with him past death — "the righteous in death are called living"); the unearned soul (אם אדוניו יתן) with its deed-children (בנים = high-intensity mitzvot, בנות = lesser; or the angel-advocates) reverts to its Owner — האשה וילדיה תהיה לאדוניה — yet והוא יצא בגפו, he still rises by his merits; the devoted declaration = the saint refusing death's freedom; ועבדו לעולם = credited as serving forever + the 400 worlds of yearning (מרצע = 400, Zohar I 123).
- **OC 21:7:1-3** — sale framed on the SELLER (father only — no self-sale, no court-sale of a female); וכי's vav = the sale-power rides ON TOP of his kiddushin-power; איש excludes the mother; את read distributively ("sells himself AND his daughter" — the man's self-sale carried by את); לאמה = even an AYLONIT (unmarriageable but serviceable) is sellable — or: only determinate sex (no tumtum/androginos sale, Tosefta Bikkurim).

## Batch 65 digest (31 listings; Or HaChaim closes + Paaneach Raza + Pardes Yosef opens)

- **OC 21:7:4-6** — ADD new exit-reading + interpretive-license doctrine: pshat of לא תצא כצאת העבדים — the amah exits at the MASTER'S DEATH even before six (males continue serving the son; she doesn't); or she "acquires her place" on the yiud-track (stays past six for marriage — exits only by death or get). Method statement: "we are licensed to construe verses otherwise than the halakhic reading, so long as we never contradict the LAW — all of which came from Sinai." Rationale for shen-ve'ayin being Canaanite-only: the Hebrew slave collects DAMAGES for the eye (often worth more than his remaining term); the body-owned Canaanite gets the known generosity-custom instead.
- **OC 21:8:1** — MAJOR consent-symmetry from the double text: yiud needs HER consent (Kiddushin 19) — so the qere לו יעדה covers HIS refusal (אם רעה בעיני אדוניה) and the ketiv לא יעדה covers HERS ("she did not consent — the thing was not with her da'at"); either blocks → והפדה. The woman's veto written in the ketiv.
- **OC 21:9-11:1** — dual-layer typed explicitly: his pshat reads שלש אלה as the marital triad with a GET required (אין כסף = "money no — but a get yes, for she is his betrothed"); "and our rabbis said the three are yiud-him/yiud-son/redemption — and these are HALAKHOT SAID AT SINAI which they ATTACHED to the verse (וסמכום)." The Mekhilta's triple classified as Sinai-law + asmakhta.
- **OC 21:11:2-9** — MAJOR-color: the exile's own lawsuit, argued FROM our statute — Israel the daughter-sold-as-amah pleads "why is her law worse than the slaves' who exit at six? we are sold 1,672 years!" (he dates himself); the ketiv on the exile ("now He designates her not, for her deeds"); והפדה = she cannot be JUDGED while enslaved — her captors force the evil, "her being bad in exile proves nothing; redeem first, then assess"; לעם נכרי לא ימשל = no sale to the nations is permanent ("He set an end to the darkness"); the Zohar's two redemption-modes mapped (merit-driven fiery-pillar vs end-driven pauper-on-donkey; אם רעה = even unworthy at the end, והפדה regardless); אם אחרת יקח לו = the abundance meanwhile spilling to the nations through broken conduits; and the crown-line: if Israel lacks even the triad, ויצאה חנם — THE SUFFERING ITSELF REDEEMS, "her torments suffice for her ransom" — even without Torah, mitzvot, or longing (אין כסף).
- **OC Gen 29:18 / 30:15** — settlement-link candidates: Jacob's SEVEN years for Rachel measured against the slave's SIX ("he priced her by exceeding the eved-ivri's term") — Gen 29 ↔ Exod 21:2; the Rachel/Leah onah-difference justified from לא יגרע (Leah's claim = the Torah's onah only — he never chose her) — Gen 30 ↔ Exod 21:10.
- **Paaneach Raza (Tosafist)** — CONFIRM the Marah acrostic at its earlier source (ואלה המשפטים אשר final letters = מרה; din-avodah adjacency = two of the world's three pillars); the double-source resolution for the gentile-court ban (כי לא כצורנו צורם covers their-law courts; לפניהם extends to when they judge BY OUR LAW; משפטים בל ידעום re-assigned to non-din mitzvot); the "Canaanite-from-Israelite" hava-amina defended against לא תחיה כל נשמה ("Canaanite" = generic slave-name from the curse, stock from other nations); מרצע = 400 tied to the 400-year bondage decree; the ownership-defection answer to "why only this sin pierces" (this sin alone exits God's title entirely); ויצא"ה חנ"ם gematria = סימנים ("signs") — the signs-exit encoded numerically.
- **Paaneach Raza Mishpatim 5** — MAJOR the anti-retention rationale at its Tosafist source, PLUS a new second rationale: (a) the single slave will love the given shifchah ("a man finds contentment only in his FIRST wife" — for him she is first) and refuse exit → pierced forever, against "they are MY slaves"; (b) a single man might SELL HIMSELF deliberately to obtain a beautiful shifchah — the permission itself as a perverse incentive to voluntary enslavement, blocked by the wife-precondition.
- **Pardes Yosef 21:1 (mega-row)** — MAJOR double cluster: (1) the gender-parity clause (השוה הכתוב אשה לאיש לכל דינין, Kiddushin 35a) at its source with Tosafot's objection (לפניהם = judges, the drash needs litigants) resolved by the TAV-PREFIX grammar: tav-initial verbs serve masculine second-person AND feminine third-person — תשים itself is the dual-gender marker (deployed across מילה exemption, the Chinukh's women-in-haggadah, the מצה/סוכה derivations). (2) The KING-track constitutional cluster hung on our header: לפניהם vests the FIXED law in the judges; the king (Moses was a king) holds the second track — hora'at sha'ah (Derashot HaRan's two-mishpat theory; Yitro's plan = fixed judges below, Moses keeps emergency justice); the king punishes outside procedure (no warning, one witness) but CANNOT pardon a court-convict (he sits under the Sanhedrin; no royal pardon from the refuge-cities either); mechilah-analysis (future-honor waivers void, past-insult waivers valid — Shimi; Saul punished; Rambam vs Ran/Rama); royal executions by SWORD ONLY (Tosefta Sanhedrin 9; the legion-oath midrash; the Zohar's Name-engraved sword — Solomon killed Shimi by the NAME on the blade; David's rebuke re-read: Uriah deserved Sanhedrin-process or, as rebel, the royal SWORD — not Ammonite arrows); the king's fence-breaking right (Rashi's for-himself vs Rambam's wartime-only; the Zohar on Navot: the TAKING was lawful, only the killing sinned).

## Batch 66 digest (8 listings; Pardes Yosef 21:1:2-21:3:1 — the compilation mega-rows)

- **PY 21:1:2** — the thunders fork DOCUMENTED both ways: Rashi Taanit 21b says all the mitzvot were given "with thunders and torches" through the Mishkan-winter (supporting the Re'em's reading!) vs Tosafot Beitzah 5b (thunders ceased after the Ten). Plus the guarding-transfer note on the terumah-midrash (terumah needs GUARDING — the scholar who shirks the community's burdens destroys; Rambam's terumah-only-to-scholar-priests explained as shomer-to-shomer transfer law — handing to a worse guardian is negligence, CM 291:26).
- **PY 21:1:3** — MAJOR administrative isomorphism + deterrence-display: per Rambam Biat Mikdash 6:11 the Great Court's MAIN work in the Chamber of Hewn Stone was VETTING PRIESTS (genealogy and blemishes, Middot 5:4) — the bench sits by the altar to certify who may serve at it. And the tools-doctrine: the judges' staff, strap, shofar, and sandal stand VISIBLE so the litigant "sees what lies before them and fears to defy the ruling" — לפניהם as deterrence-by-display.
- **PY 21:1:5** — MAJOR ger-judge and get-court cluster: converts can't judge (Kiddushin 76b) yet a convert judges WITH THE PARTIES' CONSENT (Sema CM 7:4) while a gentile never (CM 26) — Shemayah and Avtalyon handled four ways (greatest-of-their-era per the Tashbetz; not-personally-converts per Tosafot Yom Tov; appointed by Hasmonean KINGS whose power needs no process; or they sat to clarify law, not to judge capital cases). Then the get-is-a-din debate: the Noda BiYehudah BACKING the Ohr Zarua's night-get position (our bite-63 find, alive in the literature); the split — Gittin 88b objected only to the COERCION (laymen may ARRANGE a get, ordination-honor being waivable; compulsion never); willing get needs no court, FORCED get needs three (Onag Yom Tov 155); Targum Yonatan's "before the court" with the Chida's authenticity caveat; Kiddushin 62b's "who says three will convene" as counter-proof. And the modern fault-line on the gentile-court license (Rambam 26:7/CM 26:2: beit din may license erka'ot against a refusing defendant): the Kol-Chai's objection (how license a Torah-violation? agency works only where they judge OUR law); the NESIVOS (the author's ancestor): forbidden until the defendant was ADJUDGED liable and refuses; Yeshuot Yisrael: practice ignores the Nesivos; the self-help analogy (one may enforce by blows — maybe the לפניהם-violation also yields to loss-prevention; Rama bars erka'ot-rescue; left צ"ע).
- **PY 21:2:1** — wild ADD: how did the Canaanite-slave hava-amina survive the ear-heard-at-Sinai rationale? Gilyonei HaShas: the slaves' GUARDIAN-STARS were at Sinai (מזלייהו הוו, Shabbat 146a; Shevuot 39a includes slaves via "those not here") — even the Canaanite's mazal heard the command.
- **PY 21:2:3** — MAJOR the worker/slave liberty analytics running LIVE: a hired worker quits even mid-day (כי לי בני ישראל עבדים — ולא עבדים לעבדים, CM 333:3), so self-HIRE is permitted while self-SALE is forbidden; Chatam Sofer's money-mechanics (the slave must REFUND to exit — "who says he'll have the money" — so sale is real bondage; the worker collects only at term's end, no refund-barrier); CS's practical pesak: a town may not bind a RABBI beyond THREE years (the hireling-standard from משנה שכר שכיר) — structure the contract so his leaving costs him nothing (the penalty payable by the TAKING town), preserving worker-status. The block's law governing 19th-century rabbinic contracts. Plus: Targum Yonatan's ובמעלי שביעתא ("on the EVE of the seventh") girsa-puzzle vs exit at the seventh's start (Rambam 2:2; Yerushalmi; Erkhin 18b day-to-day; leap-year exit at Adar II's end); the Maggid Meisharim's "the seventh is HIS OWN shemittah" (personal sabbath-clock); the slave is MUCHZAK IN HIS OWN BODY (Maharit via the Rosh) — so no coercion once the seventh arrives, and the Minchat Chinukh's calendar-edge: term ending Rosh Chodesh Nisan bars work already on 29 Adar, lest the court sanctify the month and he prove retroactively free. And the buy-Israel-first excursus: the Rama's prefer-the-Jew-even-at-higher-price responsum vs Tosafot's small-difference-only, threaded through the lending-priority sugya.
- **PY 21:3:1** — the kohen-slave module: from the Ramban-Mekhilta (the widow-to-high-priest wife earns no maintenance) it follows even a HIGH PRIEST can be sold as eved ivri; against משתמש בכהונה מעל ("who uses the priesthood trespasses"): the kohen may WAIVE for his livelihood (as he may labor); minor kohanim (no waiver-capacity) — custom defended via וקדשתו not covering minors (Magen Avraham), challenged from the blemished-kohen ribbui (Torat Kohanim); the line drawn: slave-type service forbidden, mutual FAVORS permitted (Binyan Tzion), and payment cures all (Rava's paid kohen-attendant, Chullin 133a). Also the self-permission fork (Rambam's phrasing: only the MASTER can't GIVE a shifchah to the wifeless slave — by his own consent he's permitted; Mishneh LaMelekh).

## Batch 67 digest (19 listings; Pardes Yosef 21:3:2-21:10)

- **PY 21:3:2 / 21:4:1** — CONFIRM the entry-timestamp doctrine deciding the Mishneh LaMelekh's doubt: Rashi's "not married AT FIRST" implies the widowed slave (married at entry, wifeless now) still receives the shifchah. The Zohar on אם אדוניו: "the Master of all the earth gives him the wife — pairing is not in man's power."
- **PY 21:5:1** — MAJOR-color settlement-link (Deut 3:26 ↔ Exod 21:5): the midrash has MOSES argue FROM OUR LAW against dying — "I love my Master (God), my wife (the Torah, מאורסה), my children — I will not go free" (death = "free among the dead") — claiming the nirtza's yovel-term, 50 more years; God's רב לך = "the 50 (לך) was already GIVEN — your 120 includes it." Moses as the slave refusing exit, answered in term-arithmetic. Also: declaration binds at the END of six, not the start.
- **PY 21:5:2** — the house-lexeme analytics: the MASTER needs wife AND children (כי אהבך ואת ביתך; Rambam 3:11); a betrothed-but-uncohabiting wife is NOT "his house" (Yoma 13) — yet for the SLAVE's אשתו the arusah may count (get-language precedent, Chacham Tzvi 124) even though the maintenance-Mekhilta excludes her via עמו; Beit Shammai's ervat-davar divorce-bar limited to the married (ושלחה מביתו — the arusah isn't in his house).
- **PY 21:6:1-4** — CONFIRM no-agency at its Yerushalmi source (ורצע — he and not his agent; like chalitzah's "they and not their agents," semikhah's "his hand") + the DISGRACE rationale ("he stands pierced in public view against the people"); or as אם again; the right-ear puzzle sharpened (all mitzvot right-sided, but the Word went from God's RIGHT to Israel's LEFT — hava-amina for the left ear; the Sefer-Yetzirah orifice-map where ת=400 points at the LEFT ear, forcing Rashi's "right"); the Makneh's cipher (the letters around מרצע spell the lintel and the Passover-blood stations — "he expounded it like CHOMER," matter enclosing form); the ear-as-handle image (the organ through which all limbs live — the mitzvah-system's intake pierced); and the Makneh's nugget: a self-sale by one who CAN feed himself may be VOID as a transaction-in-sin (CM 208).
- **PY 21:6:4 (the adon-analytics)** — MAJOR equal-provision jurisprudence: "who buys a Hebrew slave buys a MASTER for himself" read as role-inversion PENALTY (the buyer enabled the defection from God's service — Chashek Shlomo); resolves the festival-appearance question (his "master" doesn't compete with אל פני האדון ה'); the one-pillow rule (give it to the SLAVE — Yerushalmi/Tosafot) against חייך קודמין: Maharam Schiff's split — in COMFORT the slave precedes, in SURVIVAL your life first; PY's own reading: "the buyer is LIKE the slave" — parity, not superiority.
- **PY 21:6:6** — ADD-lexical: the לעולם concordance built off our verse — the Beit Yaakov responsum (a house rented עד עולם: heirs cannot evict — our sugya proves לעולם can mean life-long); whose life? (muchzak-analytics); the Mekhilta's "olam = 50" deployed for the 50-year memorial-prayer limit (with the Munkatcher's protest); then ~80 Talmudic לעולם-maxims catalogued to sort the perpetual from the bounded senses.
- **PY 21:7:1** — MAJOR live labor-law precedent (Mahari Bruna 241): a hired MAIDSERVANT sent to the market refused — "you hired me to serve in the house, not outside" — and CANNOT be compelled, "and there is even a prohibition, as it says לא תצא כצאת העבדים," citing the Tur's reading (indoor service only). The block's protection running in 15th-century employment. Plus לא תצא typed as SHELILAH not prohibition (Rambam shoresh 8 debate); the Beit Yitzchak's unilateral-manumission question (can the master free HER by writ as with the male? why doesn't Kiddushin list the difference?); the eviction-analytics (Minchat Chinukh vs Yam-Shel-Shlomo on "work-for-your-food").
- **PY 21:8:1** — MAJOR the poverty-gate harmonization: Kiddushin 41a forbids betrothing one's minor daughter (until she says "I want X") — yet yiud is a MITZVAH; via Rambam 4:2 (the father sells only in TOTAL destitution): the sages' ban binds the solvent father, the destitute father's yiud stays mitzvah (with the Taz-principle — what Torah explicitly permits the sages cannot forbid — and Tosafot's exile-practice defense of minor-betrothals).
- **PY 21:8:2 / 21:9-10** — ADD the no-bundling rationale: לא ייעד לשתים כאחת = not two AMAHOT at once — yiud is a mitzvah and מצות אין עושין חבילות חבילות (Beit HaOtzar); the who-speaks question on the son's formula (Rashi: the son; Rambam: the father as his agent; Lechem Mishneh harmonizes); the marry-off-the-minor-son duty with the Sanhedrin 76b tension; the maintenance-triad pesak map (Onkelos deoraita; Ramban's rabbinic-mezonot system with the Ran's cascade; the Yerushalmi's DWELLING-obligation deoraita even where food isn't; Maggid Mishneh's kav-venaki); the motzi-shem-ra/ketubah-derabanan puzzle resolved via written-custom, oath, or the anusah case.

## Batch 68 digest (13 listings; Pardes Yosef 21:11 appendix + Penei David/Chida + source-rows)

- **PY 21:11 appendix (mega-row)** — a mini-code of edge-rules: court sells ONLY the insolvent thief (assets → forced payment, sale invalid even post facto; sale for PRINCIPAL never the double; the Makneh's allocation-question); stole from a GENTILE or HEKDESH → not sold (OC's source: the juxtaposition to the double-payment pericope — Israel-theft only; likewise slave/document/land theft); confession-based sale impossible (witnesses required); women don't buy male slaves (suspicion; the under-nine carve and its critics); if the SLAVE has money they force HIM to self-redeem (family blemish); the לעם נכרי transfer-ban binds only AGAINST HIS WILL — with the slave's consent a transfer stands; self-sale only in destitution and only to Israel — not even for a mitzvah (Tosafot BB 13a) BUT Kiddushin 69a's "steal and be sold" advice implies mitzvah-sale allowed — resolving JACOB's seven-year self-hire (beyond the three-year cap): for MARRIAGE it is permitted (the Gen 29 ↔ Exod 21:2 link closed halakhically); the auction and rescue-bid question; resale to the master's SON as inheritance-analog (rashut-yoresh; the Ralbag's inheritance→sale inference; the no-resale rule imported from the ivriah's לא ימשל via Kiddushin 18's shared-defaults); the Kessef Mishneh's צע"ג (Rambam "possibly learned" the amah's no-limb-exit — it's explicit in the sources); Maharsha's own-shifchah-only novelty softened by the Noda BiYehudah (any shifchah, but with the master's license); two sisters in one purchase (one undesignatable); sale to cheresh/shoteh void; and the compelled-CURRENT-VALUE redemption: no forced subsidy, but the master must accept the שומא and she exits against his will.
- **PY Lev 25:41** — CONFIRM the Chatam Sofer computed-delta via the Torat Moshe: master's children-maintenance mirrors the father's (till SIX, EH 71); in Mishpatim's six-year term every child alive at sale outgrows six before exit → only the WIFE named; in Behar yovel may cut the term → under-sixes may remain → הוא ובניו named.
- **Penei David (Chida) 1:2** — MAJOR-color the bar-metzra defense: the ANGELS claimed the Torah as NEIGHBORS (dina d'var metzra); but "who judges truly becomes God's PARTNER in creation" — and a partner DEFEATS the neighbor's preemption; hence the Torah rides ringed by dinim (ואתה תחזה before, our header after): Israel's judging-partnership is its TITLE to the Torah.
- **Penei David 3:2** — ADD-color sovereignty-inalienability allegory (Amrei Noam + Chida): בגפו = under the Shekhinah's WING into exile and out; the refusing slave = the assimilator ("I love my wife" = the nation-given Sitra Achra); והגישו אל האלהים = the nation's own PRINCE must himself deliver him to the divine court — no other sovereign can hold title in Israel; מרצע = the 400 of Egypt; הדלת = the dalet of אחד; המזוזה = 70, the Sanhedrin above; ועבדו לעולם — to GOD. The Chida frames the header as Moses addressing the NATIONS' princes: "work their bodies, never their Torah."
- **Penei David 5-13** — color: grandfather Azulai's remez (שארה כסותה וענתה לא initials = שכול — the bereaved should take another wife); the chaser-vav onah-mysticism (Friday-after-midnight; the responsive-onah rule — her signal obligates even weekdays; immersion night); R. Yeshayah di Trani's block-2/4 previews (the ladder staging of אנה לידו; kidnapping placed between striker and curser because the STOLEN CHILD grows up to strike and curse the parents he never knew — R. Natan b. Menachem's causal chain; shen-ve'ayin selected because Canaan sinned by tooth-telling and eye-seeing — Ham's וירא; אם כופר excluded from the three obligatory-אם's as duty-not-mitzvah; the pledge-return צעקה read as a prayer FOR the returner).
- **Peri Megadim OC 137 / Pesachim 72b / PdRK 12:8** — liturgical: Shekalim can host in MISHPATIM week only in a plain year (the reader-division analytics, Megillah 30). The talmudic anchor שמחת עונה — conjugal duty as JOY. And the matron-with-weapons midrash at its SOURCE (Pesikta DeRav Kahana): "dinim before her — שם שם לו חק ומשפט (MARAH); dinim after her — ואלה המשפטים" — note the Pesikta's fore-guard is Marah, not Yitro's judges (variant registered).

## BATCH 69 (14 listings, 29,388 chars) — PdRK 12:11, Petach Einayim, RALBAG COMPLETE (Beur HaMilot + the 31-root Torah commentary)

**Pesikta DeRav Kahana 12:11** — CONFIRM+ADD: the Yitro jewel-parable SOURCE: the king fills his son's lap with gems himself "so my son won't say: were it not for father's friend, he'd have nothing to give me" — so God, lest Israel say "were it not for Yitro who taught you the laws (הדינים)," gives the Torah כולה דינים ("ENTIRELY laws"), prooftext = OUR HEADER ואלה המשפטים אשר תשים לפניהם ("and these are the ordinances you shall set before them"). ADD: Torah-as-all-law via our header — the header verse recruited to characterize the WHOLE Torah as ordinances. Also: the courtship-gift parables (manna/well/quail/honey as the suitor's gifts before Sinai-marriage) and the kartisin (boundary-edict) annulment — "Rome shall not go down to Syria" repealed at Sinai: heaven-earth traffic opens (Moses up, God down). Marriage-covenant frame for the mishpatim CONFIRMED from the PdRK side (12:8 read at bite 68).

**Petach Einayim on Avodah Zarah 26a:1** (Chida) — peripheral CONFIRM: gentile wet-nurse sugya; cites Rabbeinu Bachya on OUR PERICOPE (Mishpatim) that forbidden foods dull the heart (מטמטם הלב). Link to block is via the Bachya-Mishpatim citation only. Read in full.

**Ralbag Beur HaMilot (word-glosses), 8 rows** — Deut 7:3:1: MAJOR-adjacent: the intermarriage ban's LOGIC derived FROM our shifchah-law — since even the half-entered Canaanite bondwoman's children follow HER (האשה וילדיה תהיה לאדוניה, "the wife and her children shall belong to her master") and no marriage-bond attaches, all the more so full gentiles — our block as the halakhic ENGINE of Deut 7:3. Deut 15:16:1: cross-pointer ("we already explained piercing in Mishpatim"). Exod 21:3: בגפו ("alone/in his cloak") = came single, nothing but the wing of his garment (cf. במקלי "with my staff" Gen 32:11). 21:4: the given wife = Canaanite bondwoman ONLY — inconceivable for a daughter of Israel. 21:6: אל האלהים ("to the judges") = judges; slave stands AT the attached door. 21:8: לו יעדה = designate for MARRIAGE; לעם נכרי ("to a foreign people") = ANY other household — עם = gathering, every other HOUSE is a "foreign people" (radical reading: the sale-ban is total, not ethnic). 21:10: שארה = her food (from שאר rain-of-flesh Ps 78:27); עונתה = her conjugal due.

**Ralbag on Torah, Exod 21:1:1-37 (the full pericope essay + 31 roots)** — MAJOR, law-as-code in the medieval original: method = running paraphrase (ביאור), then purposes (תועלות), then numbered ROOTS (שרשים) — legal axioms each closed with a verification tag ("already established in Kiddushin ch. 1" etc.). The machine shape: axiom + citation-witness, exactly our demand-ledger form. Headline roots:
- CHILD-SUPPORT SIX-YEAR FLOOR: master feeds slave's wife+children (ויצאה אשתו עמו, "his wife goes out with him") because the slave owed them maintenance; term = 6 years → "from this place it is established the father owes his minor children maintenance until age SIX at minimum" (root 9, to Ketubot 5) — the sale-term length GENERATES the child-support duration. Beyond six = only via charity-coercion rules. [MAJOR: term-length → obligation-length inference]
- ILLNESS INTERPOLATION: כשכיר כתושב ("like a hireling, like a resident") = the eved is the MIDPOINT type between hired-worker (loses pay when sick) and resident (loses nothing) → sick ≤3 years exits on time, sick 4+ (over half) must repay (root 3). A formal interpolation between two legal types. Flight = always repay (never "in the class of a worker"). [MAJOR]
- אמור יאמר ("if the slave shall SAY, SAY") = the doubling read as REPETITION-REQUIREMENT; "the least of plurality is two" — declaration must be said twice, while still a slave, with a perutah's worth of term remaining. The first-plurality argument is explicitly arithmetic. [CONFIRM of the two-sayings rule with Ralbag's mathematical derivation]
- THREE JUDGES FROM THE PLURAL: אלהים is plural → at least two → two can deadlock with no tiebreaker → THREE required (root-level in the paraphrase). The court-size derived by parity-argument from morphology. [MAJOR: arithmetic derivation of the three-judge bench]
- KOHEN NOT PIERCED: piercing = permanent blemish = unfit for Temple service = cannot "return to his standing" at yovel (ושב אל משפחתו, "he returns to his family") — the yovel-return clause BLOCKS piercing for priests (root 13). [CONFIRM with sharpened mechanism]
- CAUSAL-LAPSE PRINCIPLE: pierced slave serves the master but NOT the heir — his love for THIS master moved him; "when the cause lapses, the caused lapses" (ובסור הסבה יסור המסובב) — ועבדו ("he shall serve HIM") = him alone (roots 6, 12). Legal effect tracks its motivating cause. [MAJOR]
- USUAL-CASE CANON: inheritance of slave-service passes to the SON only (not brother/daughter) because "the Torah's laws follow the customary course" (משפטי התורה... לפי הנהוג) — the yiud-to-son clause as the witness (root 6). [ADD: explicit legislative-defaults canon]
- FRUIT-SALE TEMPORAL-TITLE ANALOGY: father sells only during minority because one who owns a field's fruit for two years cannot sell three — YOU CANNOT SELL MORE TIME THAN YOU OWN; when she becomes a naarah (pubescent girl) she leaves his jurisdiction, so the sale term auto-truncates at signs (paraphrase + root 8). [MAJOR: temporal property-rights formalism]
- TUMTUM/ANDROGINOS EXCLUDED from both eved-ivri sale (unfit for the shifchah-assignment scheme, root 11) and amah sale (unfit to be wife to master or son, amah root 4) — eligibility for the law's remedial scheme is a precondition of the sale itself.
- SELF-SELLER NOT PIERCED + not given shifchah: else a man would sell himself OUT OF LUST for a bondwoman (end of essay) — same perverse-incentive attack as Paaneach Raza's (bite 65) — CONFIRM from the philosopher's side.
- PURPOSE (תועלת 1): anti-permanent-poverty design — "so no man or woman of Israel remains in lasting lowliness"; the 7th-year/yovel exits are consolation-timers for the poor. Piercing before judges = deliberate PUBLIC DISGRACE engineered to deter choosing slavery (root-purpose). [CONFIRM of the deterrence-by-shame design]
- AMAH ROOTS: sale only to one eligible to betroth her (root 12); YIUD PRIORITY over pedah because delay breeds suspicion she was abused in the house — reputation-protection rationale (root 11); father may sell twice ("shpachut after shpachut") but NEVER after marriage — marriage extinguishes the father's body-title entirely, servitude does not (root 13, title-algebra); amah never pierced (no rule stated for her, and marriage-to-slave unthinkable); NOT freed by tooth/eye like the Canaanite slave — body not owned (root 14).
- ONAH ROOTS: maintenance/clothing scale with the husband's wealth (poor = necessities, rich = per his wealth); onah is OCCUPATION-RELATIVE — camel-driver, sailor frequencies differ — "the onah APPROPRIATE to her FROM HIM" (root 15): the duty is indexed, not absolute. Withholding-onah's harm stated in population terms (drives to zenut, civic damage). [CONFIRM of Ketubot 5's schedule with Ralbag's relativity formula]
- Also: אהבתי read doubly — "better reading": I AND my wife AND children all love the master (the Hebrew-wife family, who experienced his goodness — so children must predate entry); door must be STANDING by its post; master alone pierces, one slave one ear at a time; no gentile as eved ivri (no family to return to at yovel, root 13 end); עם נכרי sale-ban covers GIFT too (same reason, root 7); if master dies amah goes FREE even from the son — the household turns "foreign gathering" at his death (root 7 — matches his radical עם=house gloss).

All 14 read in full. [69 bites: 1,673/1,962 = 85.3%]

## BATCH 70 (32 listings, 19,130 chars) — RASHBAM complete, RAV HIRSCH opens (Deut rows + Exod 21:1)

**Ralbag Exod 25:1:18** — peripheral: showbread essay; priests supported so they stay free for Torah and ביאור משפטים ("clarifying the ordinances") — priests as משפט-teachers (יורו משפטיך ליעקב, "they shall teach Your ordinances to Jacob"). Read in full.

**RASHBAM on Exod 21 (15 rows) + 3 crossrefs** — the peshat layer, openly two-compiler:
- 21:1:1 MAJOR: the PROGRAMMATIC MANIFESTO at our header: "I have not come to explain halakhot though THEY are the essence (עיקר)... halakhot are heard from the superfluities of the verses (מיתור המקראות)... I come to explain the plain sense; nevertheless the halakhot are the essence, as the rabbis said הלכה עוקרת משנה [v.l. for הלכה עוקבת מקרא — 'the halakhah uproots/overrides the text']." The dual-layer doctrine — a peshat channel and a binding oral channel that can OVERRIDE it — declared at OUR HEADER VERSE. Joins the GRA-manifesto מרצע registry (bites 40s): Rashbam is the peshat-side witness of the same two-channel architecture.
- 21:2:2 CONFIRM (peshat-side) of the term-clock gate: ובשביעית = "seventh of his SALE, not the shemittah seventh" — Malbim's sale-clock ruling was already Rashbam's peshat.
- 21:2:3 grammar: לחפשי vocalization proves it's the abstract noun (freedom), not the adjective (a free man).
- 21:3:1 ADD text-structure rule: כולל ואח"כ מפרש ("states generally, then specifies") — v. 3 is the general clause the next verses unpack; the given wife = Canaanite bondwoman.
- 21:6: judges; piercing לעין כל ("in the sight of all") as a PUBLIC MARK of slavery (סימן עבדות — deterrence-by-visibility, CONFIRM); מזוזה works even in stone houses since doorposts are wood.
- 21:6:3 MAJOR FORK-WITNESS: לעולם "according to the PESHAT: all the days of his life" (citing וישב שם עד עולם, I Sam 1:22) — peshat says FOREVER, halakhah says until yovel; Rashbam records the divergence without flinching. The clean two-layer fork on ועבדו לעולם.
- 21:7: לא תצא כצאת העבדים = she does NOT exit at six like the male slaves — rather (as the text goes on) he is to marry her. Peshat gives the verse an expectation-of-marriage reading.
- 21:8: רעה = displeasing/plain in his eyes (מכוערת); בבגדו בה = "since he BETRAYS her by not designating" — prooftext MALACHI 2:14-15 אשר בגדת בה... אשת בריתך ("whom you betrayed... the wife of your covenant") — ADD crossref: the amah-betrayal glossed by the prophets' marriage-betrayal oracle; והפדה = pro-rated redemption.
- 21:10 MAJOR FORK: the triad per peshat = מזון וכסות ומעון — food (שאר from Micah 3:3), clothing, and DWELLING: ועונתה from מעון ("habitation"), the מ being non-root as in מקום/מלון. Halakhah's third member = conjugal right; Rashbam's = HOUSING. The classic peshat/halakhah fork on עונתה, logged.
- 21:11: the three = marry her, designate to son, allow redemption; ויצאה חנם "through the court"; "and the sages explained: at signs of puberty, even before six and before yovel" — both layers recorded again.
- Gen 38:9:2 (grammar crossref): ואם שלש אלה cited in a chataf-kamatz/makaf vocalization rule. Gen 48:20:2: לשון שימה "falls on speech" — our header's תשים cited as proof שימה = verbal setting (CONFIRM of שימה-as-teaching). Lev 19:20:1: נחרפת = assigned to a Hebrew slave per OUR 21:4 (אם אדוניו יתן לו אשה) — the shifchah-charufah law wired to our block.

**RAV HIRSCH opens (9 rows: Deut 15:12-18, 22:8, 22:13, 23:1, 31:22, Exod 21:1:1-2)**:
- Deut 15:12 cluster: the haanakah (severance-outfit) duty COMPLETES our block — the thief sold by court must not leave empty-handed; "under the regime of Jewish zedaka no man in our midst is driven to crime out of dire necessity" — the social-net design thesis. Woman never sold for theft, never pierced; עבריה appears in Deut only to extend 7th-year exit + severance to her. The Deut retzia paragraph is "in brackets" — subsidiary to the severance law (compilation-structure claim).
- Deut 15:18: משנה שכר שכיר = DOUBLE a day-laborer's wage — the slave lives in and serves after hours, so the master received more than he paid for; hence don't begrudge the outfit. Kiddushin 15a ties it to the Exod 21:4 shifchah-authorization. CONFIRM of the Chatam Sofer 3-year-cap source sugya from Hirsch's side.
- Deut 22:8:3 CONFIRM+ADD: semikhah (ordination, from OUR אלהים 21:6) gates Babylonian jurisdiction — agency doctrine (עבדינן שליחותייהו) covers only common, actual-loss money cases; NO penalty cases (כפל double-payment, חצי נזק half-damage) outside the Land; ADD the carve-out — danger-removal (לסלק הזיקא, vicious dog / shaky ladder from לא תשים דמים) courts CAN coerce everywhere. Ketzot's power-split confirmed with the safety exception.
- Deut 22:13:2: the three maturity stages (קטנה minor / נערה pubescent / בוגרת adult) "already noted on Ex. 21:7" — OUR AMAH PERICOPE as the source of the maturity-stage system; plus the erusin/nisuin two-stage marriage doctrine and its sanctity-of-personal-acceptance thesis.
- Deut 23:1:3: son-takes-father's-place is known to Torah at exactly TWO institutions — YIUD (our 21:9) and שדה אחוזה — our yiud-to-son clause as the paradigm of filial substitution (used to explain why the yevamah is expressly barred to the son).
- Deut 31:22:5: the written Torah = "notes for reference and remembrance to a given lecture" — Hirsch's lecture-notes doctrine of the Written Torah, ANCHORED "on Ex. 21:1."
- Exod 21:1:1: the ו of ואלה joins the altar-law: justice and humaneness are the state's foundation BEFORE the sanctuary; the sword banned; mishpatim precede the Mishkan (CONFIRM of the altar-juxtaposition cluster).
- Exod 21:1:2 MAJOR — the SET-TABLE PHILOLOGY: שום לפני in all Tanakh usage (outside law-transmission) means exactly one thing — SERVING PREPARED FOOD to a guest (Gen 24:33, I Sam 9:24, 28:22). Hence the Mechilta's כשולחן ערוך ("like a set table") is the LITERAL sense of תשים לפניהם; and hence the header itself declares that the written mishpatim are "short naked sentences" whose full application lives in oral transmission — "we do not see the Law in its completeness [in writing]; the whole total Law comes only from the תורה שבעל פה (Oral Torah)." The header verse as the CHARTER of the Oral Torah, proven from the idiom's usage-distribution. The thesis of this entire scan, stated by Hirsch philologically.

All 32 read in full. [70 bites: 1,705/1,962 = 86.9%]

## BATCH 71 (19 listings, 18,382 chars) — RAV HIRSCH Exod 21:2-6: the lecture-notes manifesto + the no-prison thesis

**Hirsch 21:2:1-3 — THE MANIFESTO IN FULL** (MAJOR): nothing proves the Oral Law like the fact that the nation's rights-code OPENS with "when a man sells a man / when a man sells his daughter" — exceptional edge-cases, an "unthinkable enormity" if the written word were the sole source; but the book was handed over only after 40 YEARS of the law being lived; the written Torah : Oral Torah = short notes : full lecture — "a word, a dot, the underlining" recalls whole thought-trains TO THE INITIATED, "stares at the uninitiated as unmeaning sphinxes"; the truths are REPRODUCED from the text, not produced out of it. Edge-cases are chosen deliberately: from the exceptional case the normal principle is "more strikingly realised." [The scan's charter, stated at our block's opening verse.]

**21:2:4-5** — God's rights-idea demonstrated ON THE CRIMINAL first; בגנבתו ("for HIS theft"): sold for principal only, never for the double-fine, and his-not-her theft = women never sold; כי תקנה עבד עברי = he is ALREADY an eved when you buy (court-declared, court-sold only); Mechilta: התורה קראתו עבד בעל כרחה — "the Torah called him 'slave' AGAINST ITS WILL" (you may not call him that to demean him). MAJOR: the Torah's own reluctant terminology — the label is coerced by the case, not endorsed.

**21:2:6-9** — triangulation: here יעבד (no "you") → service survives the master (to the son); Deut's ועבדך → ONLY the son, no other heir (Kiddushin 17b) — the two verses jointly pin the inheritance rule. Wording-analysis of שש שנים יעבד ובשביעית יצא: the actual formulation (vs two rejected alternatives) makes BOTH the six-service-years and the seventh-year factors, yielding the illness-adjustment rule (incapacitated more than half = make up; else exits on time) — CONFIRM of Ralbag's interpolation with Hirsch's counterfactual-drafting method. Work fixed to his prior trade (אי אתה רשאי לשנותו מאומנותו, "you may not shift him from his craft"); עבודת עבד ban covers even services a son would gladly render. חנם = no reparation even for the master's medical outlays on him (ADD: sick-cost sits with the master).

**21:3-4** — גף from גפף = body (cf. גב back); the wife ENTERS with him, never as slave (women never sold, a fortiori not for another's crime); master boards wife and children; FORK LOGGED: Rambam vs Ramban on whether the master, bearing her maintenance, takes the wife's earnings the husband would have taken (Rambam no, Ramban yes — maintenance-earnings linkage). 21:4: אדניה "HER master" proves the shifchah kenaanit; the ONE licensed shifchah-union in the law, and only for an already-married slave; יתן לו אשה = a formal, exclusive union for the term — לו אשה המיוחדת לו, שלא תהא כשפחת הפקר ("a wife designated to him — that she not be an ownerless bondwoman", Mechilta); children follow the mother wherever no true spiritual marriage exists (Kiddushin 66b).

**21:5 — the declaration conditions as DECISION THEORY** (MAJOR): the repeated saying must fall at the last-perutah moment (בתחלת פרוטה אחרונה ובסוף פרוטה אחרונה — start and end of the final perutah's worth); the Kiddushin 22a conditions — both master and slave have wife+children, both healthy, love on both sides — each RATIONALIZED as a hasty-decision guard: later-arriving family = intolerable conditions unforeseen; own illness = decision from weakness that passes; master's illness = self-sacrifice regretted too late; one-sided affection = "unnaturally emotional mood"; both ailing = left undecided (the sugya's teyku). טוב לו עמך = the EQUALITY NORM: food, clothing, bedding equal to the master's — "who buys a Jewish slave has bought himself a master"; the dual norm את נוהג בו באחוה והוא נוהג בעצמו בעבדות ("you treat him as a brother; he carries himself as a slave").

**21:6** — אלהים-judges must be מומחין וסמוכין (proven experts, ordained), the semikhah chain reaching back to Moses, conferrable only in the Land (CONFIRM of the ordination cluster, cited to Rambam Sanhedrin 4). והגישו repeated → the court-visit has its OWN purpose: Mechilta's שימלך במוכריו ("he consults those who sold him") — FORK: is the subject the slave (judges dissuade him) or the master (court must authorize retention)? Rashi reads the master. Piercing into the DOOR not the post (Deut's ונתת באזנו ובדלת), ear pierced UP TO the door, not through into it. ועבדו = him, not the son; לעולם = "forever AS FAR AS HIS OWN POWER goes" — he loses self-redemption (the גרעון כסף right, which — ADD — applies to the male slave too, imported from the amah's והפדה); only the master's death or yovel frees him.

**21:6:5-6 — THE NO-PRISON THESIS** (MAJOR): this is the Torah's ONLY deprivation of freedom — and it is not even punishment: the criminal is placed INTO a family, self-confidence preserved, family maintained at the beneficiary's expense. "Punishments of imprisonment, with all the despair and moral degeneration behind prison bars... are unknown in Torah jurisprudence. Where its power holds sway, prison for criminals does not exist" — only briefest remand, guaranteed by the rejection of circumstantial evidence. The whole penology of the block stated as system.

All 19 read in full. [71 bites: 1,724/1,962 = 87.9%]

## BATCH 72 (12 listings, 18,424 chars) — HIRSCH 21:6:7-21:8:3: proportionality gate, six/seven theology, the anti-forced-marriage law

**21:6:7-8 — REPAYMENT ≠ PUNISHMENT + THE PROPORTIONALITY GATE** (MAJOR): sale covers principal only (never the double-fine) → motive cannot be punitive; repayment merely "does away with the effects of the crime." Why only theft? Theft is contempt of property EXACTLY when the owner entrusts it to fellow-men's honesty — property-respect being the entry-ticket to civilised society, the thief's whole PERSONALITY is committed to repayment. And the gate: the court may sell ONLY if the theft ≥ the estimated value of six years' work; if his labor-value exceeds the theft, the court impounds his EARNINGS and freedom is untouched (Kiddushin 18a); Mechilta: the VICTIM MAY RENOUNCE the sale and take a signed promise-to-pay for better days. Freedom as "holy treasure" with an explicit proportionality test + victim's veto.

**21:6:9 — THE SIX/SEVEN THEOLOGY OF THE TERM** (MAJOR): the shifchah-union is the single engineered degradation — a physical, non-spiritual union (אין קידושין תופסין, "betrothal does not take hold") to show him how far he fell. And WHY six years: crime = relapse into the "six" (the visible material world) by ignoring the "Seventh" (the invisible One); so he invests his material existence six years and the seventh frees — "Six enslaves you, Seven makes you a free man." The term-length is the week's theology run as penology: subordinating the six to the One = freedom. [The numeric structure of the whole block explained.]

**21:6:10 — DOOR vs DOORPOSTS** (CONFIRM + full apparatus): מזוזות = the independent home (Pesach blood on the posts = every soul called to build free homes); דלת = mere BELONGING to a home. He who has no ear for freedom is bored to the DOOR — the badge of belonging — in the presence of the posts. Kiddushin 22b quoted whole: "door and doorpost were My witnesses in Egypt when I said 'Mine are the children of Israel as servants' — servants, NOT servants of servants — and this one went and acquired a master for himself: let him be pierced before them."

**21:6:11 — JEREMIAH: THE RELEASE-LAW AS THE STATE'S FALL** (MAJOR): the seventh year warns the MASTERS — there is One above masters and slaves; Jeremiah 34 makes disregard of this principle the FINAL CAUSE of the state's fall; Yerushalmi Rosh Hashanah: the slave-release pericope was THE FIRST LAW Moses and Aaron brought Israel (wired to ויצום אל בני ישראל, Exod 6:13) as the precondition of redemption. Halakhic reconciliation: self-seller serves full contract (Kiddushin 14b) vs Rashi/Ritva (default six unless contracted longer); Arachin 33a reads Jeremiah's מקץ שבע שנים as seven SHEMITOT = yovel. The redemption-charter cluster (Seder Eliyahu, bites 30s) now carries its legal mechanics.

**21:7:1-3 — THE SALE WINDOW + THE ANTI-FORCED-MARRIAGE LAW** (MAJOR): sale valid only in קטנות (full minority) though the father's earnings/marriage rights run to bagrut — the asymmetry proves MARRIAGE is the sale's predominant idea (marriageable ⇒ marry her or free her). Poverty gate CONFIRMED at its strongest: house, land, LAST SHIRT sold first (Kiddushin 20a; Rambam Avadim 4:2). Then the stunner: אסור לאדם שיקדש את בתו כשהיא קטנה עד שתגדל ותאמר בפלוני אני רוצה ("it is forbidden to betroth one's daughter while a minor, until she grows up and says: THIS is the man I want," Kiddushin 41a) — Hirsch: even PERSUADING her is in the same class as force; intimacy thrives only on completest free will. The Torah grants the legal POWER but labels its exercise בגידה ("betrayal," v. 8) — power kept on the books for salvation-emergencies (Tosafot; the medieval rescues), morally condemned in normal use. The law's own power/practice split, self-documented.

**21:7:4 — כצאת העבדים = the CANAANITE slaves' exits** (injury-release, ראשי איברים): Hebrew slaves (male AND female — Deut equalizes) never exit by injury — they receive FULL damages like any free Jew and service continues; the injured amah "would expect, without consideration of the crippling — or just because of it with greater confidence — that the master would marry her." ADD: injury → compensation-not-release fork, and the remarkable confidence-line: the conditional marriage-promise BINDS HARDER after her injury.

**21:8:1 — יעד/יחד PHILOLOGY + THE CONSENT FORK**: יעד (cognate יחד, "union"; הועד mutual agreement; מועד the fixed meeting) — the WORD itself encodes mutual decision → אין יעוד אלא מדעת דידה ("no designation except with HER consent," Kiddushin 19a; Rambam Avadim 4:8 rules so) vs Tosafot: consent not required. FORK logged, Hirsch siding with Rambam on philological grounds. Qere/ketiv formalized: qere לו dominant (he HAD designated her — the purchase-money was a conditional betrothal-gift, מעות ראשונות לקידושין נתנו), ketiv לא modifies (he now refuses) — and since qere rules, מצות יעוד קודמת: MARRIAGE IS THE PRIMARY DUTY. CONFIRM+sharpen of the bite-64/68 consent-symmetry find.

**21:8:2-3 — FATHER AS SUBJECT + עם-AS-CIRCLE**: והפדה addresses the FATHER (same subject as לא ימשל): if he has acquired means the COURT FORCES him to redeem her; failing him, the FAMILY is responsible (Kiddushin 18a); master must accept pro-rated deduction (מגרע פדיונה ויוצאה). ADD: coerced family-redemption. עם נכרי: עם = any CIRCLE within the nation (sailors, soldiers, merchants, students — each an עם; hence עמיו/עמיך plurals); עם נכרי = a family-circle that must remain permanently strange = the forbidden-marriage relatives (אין מוכרה לקרובים, "he may not sell her to close kin," Kiddushin 18b); nor sell on express no-marriage condition. Ralbag's any-other-house reading CONFIRMED via Hirsch's circle-sociology; the master, of course, can never resell at all.

All 12 read in full. [72 bites: 1,736/1,962 = 88.5%]

## BATCH 73 (19 listings, 18,651 chars) — HIRSCH 21:8:4-21:11 + the Leviticus/Numbers spokes

**21:8:4 — בגד = THE EMPTY GARMENT**: wearing clothes grants every passerby the right to expect a human inside; failing that trust = being a בגד, an empty garment — hence בגידה (betrayal); parallel מעל/מעיל (the priestly robe / sacrilege — an empty priestly cloak). The father who sells without securing her marriage "proved himself a mere cloak of a father." ADD: the betrayal-etymology closing the loop on Rashbam's Malachi crossref (bite 70).

**21:9 — THE EXTREME-EXAMPLE CANON**: כמשפט הבנות read (with Rashi/Mechilta, against Rambam's unattested bridal-outfit reading) as the son owing her every wife's right; stated at the SON and not the father because there disrespect is MOST likely (she enters as a slave his father rejected) — "the concise way of the Torah: quote only the extreme example, where we could least expect the law to apply." The drafting canon behind the whole block's edge-case style, named explicitly.

**21:10:1 — THE HAIRBREADTH MAXIM** (MAJOR): the ONLY place the Torah legislates a husband's duties — and it chooses the beggar's child (father sold his shirt, master refused her, maybe disfigured) set beside the free rich bride: "not by one hairbreadth may the treatment differ." Hence עולה עמו ואינה יורדת עמו ("she rises with him and does not fall with him") — station-rights independent of dowry; a higher-born wife keeps her accustomed standard unless she waived it.

**21:10:2 — MAINTENANCE FORK + THE TRUST ARGUMENT**: Ramban, Maggid Mishneh, Ran: שאר ≠ food; מזונות only rabbinic (תקנת חכמים) — vs the deoraita reading (Onkelos/Netinah LaGer, bite ~50s). Hirsch flips the weaker reading into the STRONGER claim: the Torah no more needed to legislate feeding one's wife than feeding one's children (ALSO only rabbinic!) — it "quietly entrusts" both to natural love. FORK logged with the trust-rationale attached.

**21:11 — THE DOUBLED EXIT + THE AILONIT CLAUSE**: שלש אלה = the three service-enders (master weds, son weds, redemption), NOT the wife-duties — proof: a wife exits only by גט, and no money could free her anyway. Then Kiddushin 4a formalized: ויצאה חנם אלו ימי בוגרות, אין כסף אלו ימי נערות — חנם encodes the bogrut-exit (father cannot transfer rights he lacks), אין כסף encodes the EARLIER naarut-exit with zero compensation though the father's own rights run six months longer. ADD: the "redundant" חנם clause carries a real case — the אילונית (no puberty signs ever) who passes straight from minority to bogrut: her exit is the חנם exit. Edge-case encoded in apparent redundancy.

**21:11:4 — THE HEAD-OF-THE-CODE THESIS** (MAJOR, the block's epitaph): "Crime and poverty — the two factors which bring the respect due a human being down to zero. The Torah takes THE CRIMINAL and THE CHILD OF EXTREMEST PENURY and places them at the head of its laws of human rights." Respect is measured at the bottom of society; that is why our two paragraphs open the code. Plus the structural map of vv. 12-32 (life / body / animal injuries).

**The Leviticus/Numbers spokes (8 rows)**: Lev 19:20 — shifchah charufah = the half-freed bondwoman betrothed to an eved ivri UNDER OUR 21:4 license; betwixt-and-between status (kiddushin neither void nor capital). Lev 19:26:8 — ADD philology: עונן (divination by times) rooted in עון = time-segment, the root of OUR עונתה — with the spring/eye/time meditation (עין: succession perceived) — the conjugal-period word as the Torah's core "time" root. Lev 21:13 — high-priest marriage bounded by the naarah stage "see on Ex. 21:7" — our amah pericope again the source of the maturity system. Lev 22:10 (MAJOR-adjacent): in the terumah law, תושב = the PIERCED slave (acquisition-forever) and שכיר = the SIX-YEAR slave (acquisition-of-years) — our two slave-states ARE the priestly food-law's category pair (Yevamot 70a); neither eats terumah — labor is owned, the man is not (לא קני ליה רביה) — though even he exits by a formal writ (Tosafot). Lev 25:10:7 — yovel frees self-seller, court-sold, and pierced alike (Kiddushin 14b). Lev 25:15:4 — the reckoning canon: the slave's six years run day-to-day (מעת לעת) like sanctified-animal years and walled-city-house years — never the Elul-calendar year (sale-clock CONFIRMED inside the full taxonomy, Arachin 18b). Lev 25:39:5 — the equality norm literalized to the ONE-BED case (Tosafot Kiddushin 20a): if there is one bed, the SLAVE gets it and the master takes the floor — forced by כופין על מדת סדום ("we coerce against Sodom-conduct": he benefits, you lose nothing) — the buys-himself-a-master proverb as enforceable law. Lev 25:39:6, 25:41 — self-seller default six years (Ritva), yovel absolute, service to son only; master boards wife+children. Num 27:9 — inheritance: משפחה runs through the father only; the SON substitutes for the father in exactly two institutions — YIUD (our 21:9) and שדה אחוזה (Bava Batra 108b-109b) — CONFIRM of the filial-substitution pair from the inheritance side.

All 19 read in full. [73 bites: 1,755/1,962 = 89.4%]

## BATCH 74 (26 listings, 21,280 chars) — RIVA (Tosafist dialectic), ROSH, Rasag's count, Sefer Yereim, RAV KOOK, SHEILTOT 58

**Hirsch Num 30:4:3** — vows: father's authority runs to bogrut "see Ex. 21:7" — the maturity system's fourth spoke (vows now, after marriage/priesthood/sale). **Rav Peninim Prov 8:6** — ADD: the THREE SUPERIORITIES of Torah over conventional law-codes (דתות נמוסיות), the third anchored "as we wrote in Parashat Mishpatim": (1) inner holiness (the whole Torah = Names of God) beyond mere social ordering; (2) human-reason codes misjudge (per the Ikkarim's true-law/conventional-law distinction); (3) even correct human reason cannot CALIBRATE measure-for-measure — משפטי ה' אמת צדקו יחדו ("the Lord's judgments are true, righteous TOGETHER"): only the divine code is right jointly and severally.

**RIVA on Mishpatim (6 rows) — the Tosafist cross-examination**:
- 21:1:1 MAJOR: why exclude gentile courts by verse when even CONVERTS can't judge? Resolution (R. Moshe of Coucy): a convert is disqualified only where qualified Israelites exist; where none — he judges: SHEMAYA AND AVTALYON, converts, judged Israel "because none in Israel was as great as they." The convert-judge carve-out with the nasi-precedent. Alt peshat: כי לא כצורנו צורם ואויבינו פלילים read as a rhetorical question — since their Rock is not ours, how should our enemies be judges? Going to them testifies for their god (CONFIRM of the idolatry-testimony reading).
- 21:2:1: why hypothesize a pierced Canaanite? "He is lowlier still" (זיל טפי). Where do gentiles get slaves if מהם תקנו bars them selling each other? — WAR CAPTIVES (וישב ממנו שבי) or self-hire. Grammar excursus: nifal ימכר can be reflexive (cf. ה' ילחם, נסתרה) — so the Torah needed וכי ימוך to pin Deut's כי ימכר to the court-sale; verse-assignment settled by GRAMMAR plus the Leviticus anchor.
- 21:6:1: door standing like the post (hekesh; Targum Yerushalmi as proof; או read as אשר — "the door WHICH is by the post").
- 21:6:2: כמין חומר philology (Tosafot/Rabbeinu Tam: חומר = "deed," cognate Arabic; the drasha is act-mirroring); the לא תגנוב vs לא תגנובו variant fight — Hizkuni: must be לא תגנובו (money-theft; the capital kidnapper isn't sold) vs Hara"h: keep לא תגנוב — he should have guarded against ALL theft "for from money-theft one comes to person-theft" (gateway argument). Self-seller piercing: why only at term's end? Because THEN he re-acquires a master by free choice; and the שכיר-שכיר gezerah shavah view (Kiddushin) does pierce the self-seller. FORKS logged.
- 21:7:1-2: the sale-window dialectic in full — R. Tam's challenge to the kal-vachomer, the לאמה derivations (earnings-transfer readings, shpachut-after-shpachut tannaitic split, אם אינו ענין transfer to bogrut-earnings); the hekesh עברי/עבריה runs ALL exits both ways, but signs-exit can't apply to males (impossible-case analysis: adult self-seller already has signs; a minor's sale is void — בתו ולא את בנו) and the ראשי-איברים kal-vachomer attempts are dismantled ("one goodness begets another" refutation-pattern). Read in full.
- 21:8:1 MAJOR: why write והפדה if gierion follows from the שכיר-שכיר gezerah shavah + the hekesh? (a) FORCED REDEMPTION: מפדין אותה בעל כרחו של אב משום פגם משפחה — "we redeem her against the FATHER's will, for the family's blemish" — the coerced-redemption tannaitic source (Hirsch's court-forced father, bite 72, now sourced). (b) The דומיא דיעוד sugya: the amah cannot be bought for one perutah BECAUSE the gierion-mechanism must be operable from day one — like yiud: a sale to a relative (yiud impossible) is NO SALE — acquisition is VALID ONLY IF ITS RELEASE-MECHANISM WORKS. [MAJOR principle: no purchase without a functioning exit — the release-clause as a validity condition of the sale itself.]
- 21:11:1: the Rashi-vs-Kiddushin-4a SWAP on חנם/אין כסף (which term = naarut, which = bagrut); Hara"A: order-of-mention follows life-order; the sugya's own derivation — אין כסף לאדון זה אבל יש כסף לאדון אחר ("no money for THIS master, but there is for another master" = the FATHER, who still takes betrothal-money in naarut); the bagrut clause exists for the AILONIT (CONFIRM: Hirsch's find is the sugya's own resolution); R. Binyamin's redundancy challenge + two resolutions. The doubled-exit machinery fully cross-examined.
- Lev 27:3 crossref: R. Yehudah HeChasid — Haman's 10,000 talents = the erech-shekalim of 600,000 Israelites aged 20-60 (50 shekels each); "I explained in Mishpatim how much the shekel is."

**ROSH on Torah (5 rows + Rosh David header)**:
- 21:3:1: wife's board proven here; children's from Lev 25's ויצא מעמך הוא ובניו עמו (R. Baruch the Frenchman).
- 21:6:1 ADD: gematria מרצע = 400 = the DECREED four hundred years of servitude (Gen 15:13) — the awl carries Egypt's number: choosing bondage re-enters the term the Exodus closed.
- 21:6:2 MAJOR (bitachon-reading of the awl): why pierced at the END and not at first sale? At the sale poverty compelled — "what could he do." But after six years — master feeding him, his wife, his children — he must have saved SOMETHING; saying "I love my master" now is a free purchase of a master and a failure of trust: "he did not place his trust in the One who feeds and sustains every creature." The awl punishes misplaced reliance, not servitude.
- 21:6:3 ADD: עולם = 50 years proven from Samuel (וישב שם עד עולם: lived 52, less 2 nursing years = 50) — the yovel-span read out of the Samuel verse Rashbam used for the OPPOSITE (lifetime) reading. The same prooftext powering both forks — logged.
- 21:8:1 MAJOR-adjacent (the appreciation subsidy): what "help" is pro-rated redemption — isn't the master just refunded the unused years? No: she was bought WEAK (a small child) and is now grown and stronger — each remaining year is worth MORE than the purchase-rate, yet the deduction runs at the ORIGINAL per-year price: the master genuinely subsidizes, hence causative והפדה ("he shall CAUSE her redemption") not reflexive ונפדית. Deduction at cost, not at market.
- 21:11:1: שלש אלה cannot be the triad — once betrothed "like another" she is a full wife and exits ONLY by a get; no free-exit clause could apply (CONFIRM of Hirsch's proof from the geonic-Ashkenazi side).

**The count + codes rows**: Rasag's mitzvah-list: slave laws to be "revealed"; negative 275 = the לעם נכרי sale-ban as its own negative; positives 70-72 = שארה, כסותה, ועונתה AS THREE SEPARATE POSITIVE COMMANDMENTS (ADD: the triad individually enumerated). Sefer Yereim 117: "the Creator DECREED in the pericope ואלה המשפטים: the husband owes שאר כסות ועונה" — deoraita codification from אם אחרת יקח. Sha'arei Ephraim 6:22 masorah: ייעדנה spelled with ONE yod — "do not produce another" (scribal ruling on OUR word).

**Shabbat HaAretz, Intro 18 — RAV KOOK** (MAJOR-adjacent): individuals who fell from the nation's free, holy life "and forgot their noble worth" — OUR sugya-line quoted whole ("the ear that heard at Sinai 'Mine are the children of Israel as servants — My servants, not servants of servants' — and this one went and acquired a master") — are restored by SHEMITTAH (personal honor and freedom, דרור) while YOVEL re-equalizes the landed base (תשבו איש אל אחוזתו). Our block's micro-release wired into the macro-restoration architecture of the sabbatical system, in the shemittah treatise's own charter.

**SHEILTOT D'RAV ACHAI 58 — the geonic sheilta ON OUR HEADER** (MAJOR): the whole court-constitution codified as the Mishpatim sheilta: forbidden to litigate before gentile courts AND before laymen (לפניהם ולא לפני עו"ג, ולא לפני הדיוטות); THREE judges — the full derivation duel (R. Yoshiyah's three אלהים-mentions vs R. Natan's two + "no even-numbered court, add one"); Rava: three LAYMEN valid for admissions/loans so the door isn't locked before borrowers (שלא תנעול דלת בפני לווין), as agents of the ordained; Rav Acha b. Ika: deoraita ONE judge suffices (בצדק תשפוט עמיתך) — three is rabbinic, against the corner-sitters; the two-who-judged split (valid-but-insolent vs invalid); ERROR LIABILITY: mishnah-error reverses the case, discretion-error (defined: two-vs-two with practice one way, he ruled the other) stands and he pays from his house; arbitration timing — before the case is clear you MAY say "go compromise," after clarity you may not (ולפני התגלע הריב נטוש); the weak-vs-strong recusal rule and its limit (לא תגורו מפני איש); the student must not stay silent seeing merit for the poor; judges and witnesses stand before God (אלהים נצב בעדת אל); true judgment brings the Shechinah, theft-judgment costs the judge his SOUL (וקבע את קובעיהם נפש); the sword-between-shoulders and open-Gehinnom image; "judge only what is morning-clear" (דינו לבקר); Rav Huna's TEN colleagues ("splinters off the beam"); Rav's going-out-to-court prayer; the retinue-ego warning; "the judge has only what his eyes see"; and R. Yehoshua b. Korchah: it is a MITZVAH to offer compromise — the only "judgment that contains peace" (אמת ומשפט ושלום). The geonic curriculum hung our header with the complete judicial ethics corpus.

All 26 read in full. [74 bites: 1,781/1,962 = 90.8%]

## BATCH 75 (47 listings, 18,375 chars) — Shev Shmateta, Shir HaShirim Rabbah's esoteric fork, SHULCHAN ARUKH rows, SIFTEI CHAKHAMIM cluster

**Shev Shmateta, Intro 25** (MAJOR — institutional-resilience theory): the Sifrei says appointing qualified judges "suffices to keep Israel alive and settled on their land" — how "suffices," when the Torah itself was given only on condition of the dinim (midrash on OUR header + ועוז מלך משפט אהב, "the King's strength loves justice")? Resolved via Akedat Yitzchak/Ramban on Sodom vs Gibeah: a city WALLED with good statutes, though foxes breach the fences at times, is near healing — one reprover arises and they return; but a city whose wall itself is evil statutes (Sodom: wickedness ENACTED as law, fixed with penalties) cannot heal. So the Sifrei means the APPOINTMENT ITSELF — the standing institution, even under imperfect compliance — is what keeps the nation recoverable. Law-on-the-books vs compliance distinguished; the judiciary as the city-wall; legislated evil (Sodom) vs breached good law (Gibeah) as the two failure modes.

**Shir HaShirim Rabbah 1:2:6 — THE ESOTERIC FORK ON OUR HEADER** (MAJOR fork): R. Shimon b. Yochai: ואלה המשפטים אשר תשים לפניהם — "just as this שימה is not revealed to every person, so are words of Torah" (שימה read as buried treasure, סימה). Context: R. Yehoshua deflects young R. Yishmael on the gentile-cheese decree; "when your students are small, PRESS Torah words (מכבש); grown — reveal to them סתרי תורה (the Torah's secrets)"; the five undecidable word-attachments (הכרעות: שאת, ארור, מחר, משקדים, וקם + R. Tanchuma's כשמעם); things God told Moses "between Me and him" vs to transmit; David concealing while his teacher Ira lived. FORK against the promulgation readings of the SAME verse (Mechilta's set-table, PdRK's all-laws gift, Or HaChaim's rights-notice): universal publication vs GRADED CONCEALMENT — both hung on תשים. Logged as a live fork on the header's transmission-model.

**Shulchan Arukh rows (6)**: CM 1:1 — the agency doctrine CODIFIED: today's judges try admissions, loans, ketubot, inheritances, gifts, property damage (common + actual loss); NOT uncommon cases (beast goring beast) nor penalty cases (double-payment, ear-blast תוקע, cheek-slap סוטר, any overpayment or half-damage) — EXCEPT half-damage of pebbles (צרורות), which is compensation not penalty (ADD: the carve-out). CM 7:4 — "a woman is disqualified to judge" (terse; the Deborah problem lives in the commentaries). CM 22:2 — consent CANNOT cure a gentile judge: accepting a gentile as witness binds like any disqualified witness, but accepting him as JUDGE — even with a formal kinyan — is void and litigating before him forbidden (Rema: a completed judgment stands) — Mizrachi's consent-curability split now in the codified words. EH 76:11 — withholding onah to pain her violates לא יגרע; illness buys SIX MONTHS ("no onah-interval greater"), then her permission or divorce+ketubah. EH 77:1 — the מורד (rebellious husband: "I'll support but not approach — I hate her"): 36 barley-weights of silver ADDED TO HER KETUBAH WEEKLY while she chooses to stay, he in standing violation of לא יגרע; she can instead force immediate divorce+ketubah; dissents logged (Rambam-based: instant-divorce willingness stops the meter; Mechaber: then no לא-יגרע violation either). The rebellion-fine system runs on OUR verse. EH 80:1 — her handiwork per local custom; surplus-work to the husband ONLY against the weekly maah, and SHE may unilaterally opt out ("no maah, no surplus") while HE may not — Rema citing the Ran and THE SHEILTOT, PARASHAT MISHPATIM: the sheilta we read at bite 74 is the codified source of the wife's one-sided option.

**Siftei Chakhamim (the Rashi super-commentary), ~30 rows**: Deut 15 rows — nifal-grammar defense of the court-sale assignment (standard nifal = by others; ונמכר לך pinned reflexive only by כי ימוך; or the עברי-עברי gezerah shavah); the repetition-canon applies only to EXPLICIT novelties (hekesh-derived rules like no-limb-release don't count — Re'em); the amah-tokhiach refutation restated; Deut 15:18 — the master hands him the shifchah EVEN AGAINST THE SLAVE'S WILL (the Deut doubling adds coercion to 21:4's permission). Exod 21:1 — ואלה-additive defended against every אלה counterexample (פסל את הראשונים only where a prior LIST exists); תשים must mean טעמי תורה (the reasons layer) since דבר-ואמרת already covers double delivery (CONFIRM of set-table from the drafting side); לפניהם = the seventy elders (Rashi via Gittin) or the coming אלהים (Tosafot) — ordained either way; gentile courts excluded ABSOLUTELY (even ruling identically) while laymen who know a given din like experts MAY be used (the competence carve-out). 21:2 — the ear-drasha DEPENDS on the ivri-assignment (on the rejected Canaanite reading, piercing would be bare גזירת הכתוב — no Sinai-ear rationale). 21:3 — בגפו=בכנפו (Targum), the single man "who has only his cloak"; the wife who exits = ISRAELITE (the Canaanite stays by האשה וילדיה); wife's board from here, children's from Lev 25 (Kiddushin reconciles). 21:4 — ADD: a woman CANNOT sell herself — אחיך ולא אחותך ("your brother, not your sister"); and the zenut hava-amina (hand her to his slave outside marriage) blocked. 21:5 — the love-list coheres only with the shifchah-wife (an Israelite wife would exit WITH him — nothing to stay for). 21:6 — the two-ears assignment formalized (theft-ear for the court-sold, servants-ear for the self-seller via שכיר-שכיר); ADD grammar: עולם bare would mean a 50-YEAR SPAN of service; לְעולם with the lamed means UNTIL the epoch-marker = yovel. 21:7 — the hekesh imports YOVEL specifically (six is explicit in Deut); the male signs-exit impossibility (three-case analysis) restated. 21:8 — "if she is BAD in his eyes" implies the mitzvah when she is not (yiud hinted); yiud-not-kiddushin language proves the purchase-money WAS the betrothal; והפדה = the master "reckons with her" (subsidy CONFIRMED); לא ימשול bars THE FATHER (the master never had sale-power to bar — Re'em). 21:9 — yiud-to-son is the MASTER's act; no new kiddushin for the son either (יעדנה not יקדשנה); and the Mechilta's inversion NAMED: כמשפט הבנות = though the daughters-of-Israel's triad-entitlement "is written nowhere, it comes to teach and ends up taught" (בא ללמד ונמצא למד) — the amah-clause is the SOURCE of every Jewish wife's rights [MAJOR CONFIRM of the hairbreadth-maxim mechanics]. 21:10 — לא יגרע protects the ALREADY-designated first wife against the new match. 21:11 — "ONE of the three" (all three at once impossible — to him AND his son?); triad-reading refuted again by the get-requirement; exit at SIGNS, not immediately. Gen 37:2:13 — ADD crossref: Joseph's slave-slander runs on a רעה-רעה gezerah shavah with OUR אם רעה בעיני אדוניה (רעה = slavery-context) — a second Gen 37 ↔ our-block wire beside the sale-precedent. Lev 25:1:1 — the canonical בהר-סיני proof: shemittah's generalities sit IN PARASHAT MISHPATIM and it is NOT repeated at Arvot Moav → "generalities AND details from Sinai" as the בנין אב for the whole Torah — our pericope inside the Sinai-origin proof. Lev 25:40:1 — the FOUR yovel-verses mapped to cases (self-seller / court-sold / pierced-before-six / pierced-after-six = ועבדו לעולם) per Kiddushin 15. Num 35:14 — Gilead's three refuge cities via the inn-parable of OUR 21:13 (block-2 material, chapter ledger absorbs it).

All 47 read in full. [75 bites: 1,828/1,962 = 93.2%]

## BATCH 76 (16 listings, 18,523 chars) — SIFTEI KOHEN (the kabbalistic layer): Decalogue-map, judge-virtue compensation, the Torah-as-amah allegory

**Siftei Chakhamim Num 35:31** — no-ransom-for-murderer needed because OUR pericope's goring-ox כופר creates the hava-amina (if ox-caused death is ransomable, why not self-caused — blocked). Block-3 spillover, ledgered.

**Siftei Kohen Deut 16:18** — ADD: judges "in all your gates" = the SEVEN BODY-GATES (two eyes, two ears, nose, mouth, genitals) — an officer over each organ; Bachya's sevens-election; pointer back to OUR block ("in Mishpatim we expanded on bribery"): שוחד blinds THE EYES ABOVE — the taker imagines God unseeing; Onkelos ויסלף = מקלקל, bribery shifts the Throne from mercy to judgment; the three-pillars cosmology (earth held over water by din/emet/shalom — remove one and the waters rise).

**Siftei Kohen on Exod 21:1 (8 rows)**:
- Gematria layer: ואלה = 42 — the world created by the 42-letter Name STANDS ON JUSTICE; ואלה spelled full = ד"ר — God DWELLS (דר) among true judges (אלהים נצב בעדת אל), else רד"ו-descent to Gehinnom.
- 21:1:2 MAJOR — the DECALOGUE→MISHPATIM EXPANSION MAP (via Ramban's no-וידבר continuity): the pericope re-specifies all ten: מכה איש = murder-ban; גונב איש = theft-ban (person-theft); מקלל אביו = honor-父; זובח לאלהים = the first two; לא תשא שמע שוא = false-witness; ששת ימים = Shabbat; and OUR CLAUSES — ואם לבנו ייעדנה + שארה כסותה ועונתה = the לא תנאף expansion ("so that he not come to zenut"): the yiud/onah laws as the adultery-commandment's positive machinery. Plus: משפטים answer לא תחמוד — without property-law one thinks the coveted thing ownable; Rashi careful at 24:3 that "all the mishpatim" there = Noahide+Marah, not ours.
- 21:1:3: at כה תאמר they said only נעשה (God's words need no "hearing" — they enter the 248 limbs self-understood); at Moses' BOOK-reading they said נעשה ונשמע (human transmission needs comprehension). Dinim-judging = partnership in creation; the altar-juxtaposition = judges sustain the world as the offerings do.
- 21:1:4 ADD — the PHYSICIAN-PARABLE: Torah = the king's bread and wine; the dinim = the DIGESTIVES (מרקחת) that make the meal assimilable (רפאות תהי לשרך; worthy = elixir of life, unworthy = of death). And לפניהם (plural) vs כי תקנה (singular): TWO CLASSES of dinim — the interpersonal AND the private-conduct laws (marital timing, niddah, the privy, foods) — the code governs the intimate sphere too.
- 21:1:5: never judge alone (only the Unique One judges alone); לפניהם = לפני ה' — the bench sits BEFORE GOD.
- 21:1:6 MAJOR-adjacent — WHY תשים AND NOT תלמדם: God showed Moses every generation with its leaders, its scribal minutiae, "and what a seasoned student is destined to innovate" — the souls are ALREADY TAUGHT "from before Me" (from the six days); you need only SET the law before them. The pre-taught-souls transmission model joins the set-table/concealment forks on the header.
- 21:1:7 CONFIRM+ADD — the Yitro jewel-parable with the Marah deconfliction: Marah's "dinim" were the Noahide seven (habitual since Noah), Shabbat (habitual from Egypt), and the parah-statute; Yitro added only ADMINISTRATION (סדר הנהגה — the court-pyramid); hence "THESE mishpatim" — not Yitro's.
- 21:1:8 MAJOR — THE JUDGE-VIRTUE COMPENSATION MAP: Yitro specified four judicial virtues (אנשי חיל, יראי אלהים, אנשי אמת, שונאי בצע); Moses FOUND ONLY ONE (אנשי חיל, Exod 18:25 omits the rest). God: "I gave you the mishpat — go teach them." The code's sections map to the missing virtues: the CAPITAL clauses need אנשי חיל (strength to execute); the FOUR DAMAGE-FATHERS need יראי אלהים (only fear makes one pay for his unthinking ox/pit/fire); the FOUR BAILEES (oath-based exits) need אנשי אמת (true swearing); the interest/pledge/first-fruits/shemittah/Shabbat/festival cluster needs שונאי בצע. The written code as a COMPENSATOR for the bench's virtue-shortfall — structure explained by staffing.

**Siftei Kohen on 21:2-7 (the kabbalistic-allegorical layer)**:
- 21:2:1 (Bachya) CONFIRM: the FIRST din is the slave-law because it carries the two great memorials — Exodus (כי לי בני ישראל עבדים, mirroring אשר הוצאתיך opening the Decalogue) and Creation (the sevens: 7th day, 7th year, yovel — the slave's seventh = his Shabbat).
- 21:2:2-3 ADD (gematria homiletics): עברי read as עבר ר"י ("transgressed the 210" — Egypt's years — or the theft/servitude bans); שש שנים = the 6,000-year world-term (the cosmic slave-term; after it, exit to the First Cause); עברי BACKWARDS = ירעב ("he hungers") — he stole from hunger, אל יבוזו לגנב... כי ירעב (Prov 6:30) — the palindrome-apology: do not despise him; in the seventh he goes out.
- 21:2 the ZOHAR on חנם (MAJOR, kabbalistic-legal): "the fish we ate in Egypt חנם" = WITHOUT THE YOKE FROM ABOVE — SLAVES ARE EXEMPT FROM THE YOKE OF THE KINGDOM OF HEAVEN (servitude displaces it; the ox-parable: no yoke accepted, no plowing; hand-tefillin first); so the slave's works are חנם (yoke-less), and יצא לחפשי חנם = he exits INTO rest, and only then "they give him the yoke of the One who freed him." The deep structure under "My servants, not servants of servants": human mastery and divine Kingship are mutually exclusive occupancies. (Plus מ"ט+מ"ט letters of Shema evening/morning = חנם gematria.)
- 21:3-4 allegories: ויצאה אשתו עמו = the mastered TRACTATE personified — the dead student's tractate as the weeping wife escorting him to the grave (the famous tale); master-given wife = Torah come without toil (ancestral merit), teaching-for-pay = wife-and-children that stay with the Master; the reformed teacher's לא אצא חפשי = the Great Assembly's "raise many students"; אדוניו = 71 = THE GREAT SANHEDRIN (gematria) — והגישו אל האלהים allegorized as certification before the 71, הדלת = the gate-court, מרצע = 400 = הנשמה ("the soul," same count) and mispar-katan 22 = the alphabet — the awl of the 22 letters pierces and SAVES his soul; teachers-of-children exempt from Dumah.
- 21:7:1 (Bachya's midrash) MAJOR ALLEGORY — THE TORAH AS THE AMAH: "I had one daughter and I sold her to you — and you take her out only enclosed in the ARK (חבושה בארון)"; לא תצא כצאת העבדים = carry her with honor, for you CAPTURED her from Me (עלית למרום שבית שבי); אם רעה בעיני אדוניה = Israel keeping her badly → והפדה = the Shechinah withdraws; לעם נכרי לא ימשול למכרה = the Torah is UNTRANSFERABLE to the nations even when Israel betray her (בבגדו בה); ואם לבנו ייעדנה = the Torah designated (מיועדת) to Israel-the-sons from the six days (מורשה→מאורשה, betrothed); כמשפט הבנות = the daughter's tenth — Israel received only the seven nations' land; and God "judges them as a daughter" (mercifully, as of light mind — the calf as feminine lapse). The entire amah pericope as the Torah's own biography: God the selling father, Israel the master, yiud the betrothal, the Ark the honored litter.

All 16 read in full. [76 bites: 1,844/1,962 = 94.0%]

## BATCH 77 (20 listings, 18,372 chars) — Siftei Kohen close, TAFSIR RASAG (Saadia's Arabic), Tanna DeBei Eliyahu 4

**Siftei Kohen 21:10-11 (the scholar's-regimen allegory)**: the triad for the WORKING learner (Torah-with-labor per Avot): שארה = arayot-vigilance (שאר בשר) while at work + "leave a remainder" for Torah; כסותה = kilayim/tzitzit-covering (the Menachot tzitzit-slap story) + clothing the naked; ועונתה = FIXED TIMES FOR TORAH — the judgment-day's FIRST question (פוטר מים ראשית מדון) — plus Shabbat/festivals and the fixed Shema/prayer times ("annul your will before His"); defective וענתה → learn ALOUD; the whisper-then-aloud Amidah doctrine (Zohar: whisper past the accusers; Sandalphon's crown, ר"ם = ראש מלך). Then the amen-excursus (אמן=91=הוי"ה+אדנ"י; answerer greater than blesser; the Yehei-Shmeih-Rabba AMNESTY midrash — God expounds the Messiah's new Torah, Zerubbabel says kaddish, the wicked ANSWER AMEN FROM GEHINNOM and Michael+Gabriel haul them out, bathe and dress them for Eden). Close: ואם שלש אלה לא יעשה לה = he who does none of the study-triad ויצאה חנם מן העולם — EXITS THE WORLD EMPTY, אין כסף = אין כוסף (no longing left); then block-2 verses run as REINCARNATION LAW (והאלהים אנה לידו = God books the gilgul; ושמתי לך מקום = gilgul as the refuge-city; מזיד gets Gehinnom not gilgul; repeat = the kippah). The Sabba-crossref (Lev 13:46:2): the ZOHAR'S SABBA DEMISHPATIM — the Old Man's discourse set IN OUR PERICOPE — quoted on the mamzer as עשוק ("the oppressed"): excluded at death from the holy people, he weeps "if my fathers sinned, what did I do?" — דמעת העשוקים ואין להם מנחם, the tear with NO possible comforter; garment-tzaraat as gilgul-map. [Flag: Sabba deMishpatim = the pericope's own Zoharic layer; its gilgul doctrine is the mystical inversion of our slave-release mechanics.]

**Gematria acrostics (24:18:3-5)** — ADD: לעולם וכי ימכור initials = לוי (the Levite's 50-year עולם); וכי ימכור איש את בתו FINAL letters = ירשתו — "sell his INHERITANCE before his daughter" (the poverty-gate encoded in sofei tevot!); ויצאה חנם אין finals = המן — "in Haman's days sold for nothing, redeemed without silver" (חנם נמכרתם ולא בכסף תגאלו, Isa 52:3) — the national amah-redemption typology.

**TAFSIR RASAG, Exod 21:1-11 (Saadia's Judeo-Arabic)** — ADD, translation-layer forks: v.1 תשים = תתלוהא ("you shall RECITE before them" — oral-recitation reading of the header!); v.6 אלהים = אלחאכם (THE JUDGE, singular — the office not the bench); רצע rendered יוסם...במיסמה ("BRANDS his ear with the marking-iron" — piercing as branding/ownership-mark); לעולם = ללדהר ("for the AGE" — the epoch/yovel reading); v.8 גדר בהא ("he betrayed her"); v.10 עונתה = אוקאתהא ("her TIMES", plural — Saadia sides with the time-reading, converging with Hirsch's עון=time philology and the Rashbam-fork's third member); v.11 מג'אנא בלא ת'מן ("gratis, without price"). The geonic translation as a ruling-layer: recite-header, single-judge, brand-not-pierce, times-not-onah.

**Tanna DeBei Eliyahu Rabbah 4:1** — two block-relevant finds inside the Moses-encomium: (1) MAJOR-adjacent — Moses INVENTED the כה אמר ה' at the calf executions "for I testify heaven and earth that the Holy One never told him" — because Israel would have quoted HIS OWN LAW back: "a sanhedrin that kills once in seven years is called DESTRUCTIVE (מחבלנית) — and you kill three thousand in a day?" — the taught mercy-norm colliding with emergency power (the king-track / hora'at-sha'ah cluster from Pardes Yosef gets its narrative locus classicus). (2) ADD/fork — the DOUBLED-TORAH catalog dates our verse: "נזיקין נאמרו לפני הר סיני... כי תקנה עבד עברי נאמר לפני הר סיני, כי ימכר לך אחיך העברי נאמר בספר תוכחות" — Tanna DeBei Eliyahu assigns כי תקנה to the PRE-SINAI stratum (the Marah dinim), doubled later in Deuteronomy — a chronology fork against the post-Decalogue placement (joins the Marah-scene cluster: Megalleh Amukkot bite ~50s, Siftei Kohen's Marah-deconfliction bite 76). Rest of the passage (mourning measures, the hidden-firstborn parable, the yetzer exiled to the wilderness, the two Temples) read in full.

All 20 read in full. [77 bites: 1,864/1,962 = 95.0%]

## BATCH 78 (5 long listings, 18,740 chars) — TANNA DEBEI ELIYAHU 22-23 (the women's-law charter + professional liability), TOLEDOT YITZCHAK's market-clearing analysis

**TDbE 22:1** — ADD (pericope-position): the king arrives with terrifying hosts, then sits and PROVISIONS every householder, pauper, blind and lame — so at Sinai: terror first (the myriads, the trembling), then Moses APPEASED them (אל תיראו) "and afterwards ARRANGED before them nezikin and all the measures of din" — ואלה המשפטים as the provisioning that calms the terror. Even the theft-sold wicked receive the severance-grant (העניק תעניק) — kal vachomer the righteous; the palace-ledge (זיז) parable (from the visible ledge infer what is within: from the righteous's sufferings infer Gehinnom, from the wicked's ease infer the stored reward); the Torah-seeker must give himself to the yoke LIKE THE OX (רב תבואות בכח שור) — converging with the Zohar's yoke-of-Heaven ox-parable (bite 76).

**TDbE 23:1 — THE WOMEN'S-LAW CHARTER** (MAJOR): "Come, let us go to the measure of WOMEN — as it says next: וכי ימכור איש את בתו לאמה..." Eliyahu in the Jerusalem beit-midrash: one may NOT treat the amah ivriah like a Canaanite shifchah — "he may not say to her: take money and bring me vegetables from the market" — THE AGGADIC SOURCE OF THE MAHARI BRUNA RULING (bite 66: the hired maidservant not sendable to market). The reason is the famine-exploitation analysis: in hunger a woman "pays with herself for a meal and says it is nothing" (עורנו כתנור נכמרו juxtaposed with נשים בציון ענו) — economic desperation converts to sexual exploitation; FROM THAT HOUR the sages enacted: estate small → THE DAUGHTERS ARE FED AND THE SONS BEG AT THE DOORS (Admon: "because I am male I lose?!"; Rabban Gamliel: "I see Admon's words" — the Ketubot 13:3 rule) — the daughters-first maintenance takkanah DERIVED from our block's protective logic. Then: "any house containing an amah ivriah has QUARREL in it" (the juxtaposition וכי ימכור / וכי יריבון — the fight-verse follows the amah-verse). And the PROFESSIONAL-LIABILITY midrash (MAJOR): from the chapter's juxtapositions (ורפא ירפא beside the slave-death verses) — the physician who killed a patient, the court-flogger whose forty strokes killed, the teacher who struck a student dead, the judge, the altar-priest — if deliberate: ALL LEAVE THEIR PROFESSION for another trade; repentance restores them ("they are healed"), otherwise punished even in their property; likewise the MIDWIFE (חיה) who killed. Occupational-license revocation read out of our chapter. Coda: the covenant-in-Egypt aggadah (language kept, circumcision under the drowning-decree, the seven feast-days defiance — "we will circumcise, and then do to us as you please").

**Tevat Gome, Mishpatim 5** (Peri Megadim's aggadic ledger) — allegory: the NESHAMAH "does not go out as the slaves go out" — it flees BEFORE the sin (only nefesh and ruach see Gehinnom; נשמה שנתת בי טהורה); בנים/בנות = positive/negative commandments; the resisted-temptation reward doctrine (non-transgression earns active reward per Kohelet's סוף דבר) and the reward-timing jurisprudence (night-laborer collects by day; reward as gift — מי הקדימני) hung on our verses. Minor, read in full.

**The Sabbath Epistle (Ibn Ezra) 20** — ADD (philological spoke for the Jeremiah crux): Tishrei-year proven from shemittah's לא תזרע→לא תקצור sequence, yovel on 10 Tishrei, hakhel at Sukkot; and the TWO-ENDED קץ doctrine: "every span has TWO ENDS (שנים קצוות יש לכל דבר)" — מקץ שבע שנים can denote EITHER end — Ibn Ezra reads Deut 31:10 as the START (vs the Mishnah's motzaei-sheviit "end"), with Jeremiah 34:14's מקץ שבע שנים תשלחו as the standing parallel — the grammatical machinery under the Arachin 33a yovel-reading of OUR release-oracle (bite 72).

**TOLEDOT YITZCHAK on 21:3 — the FIVE DOUBTS and the market-clearing resolution** (MAJOR): R. Yitzchak Karo poses: (1) the single slave gets no shifchah but the married one does — "the poor man gets no charity and the rich man does?!"; (2) how license a Canaanite union against לא תתחתן; (3) the reason of door/doorpost/ear; (4) how could God empower a father to SELL HIS CHILD — "even the Ishmaelites in the kingdom of GUINEA do not sell their children" (the contemporary slave-trade invoked!) and person-theft is capital — a fortiori one's own flesh; (5) what is לא תצא כצאת העבדים, and why is no-limb-exit taught on HER not him. Resolution — PRICING, not welfare: the married thief is a TERRIBLE purchase (the buyer must board wife and children — "who would buy such a man? and if none buy, from what is the theft repaid?"); the shifchah-assignment exists to make the married thief SALEABLE (the buyer's return = her children); the single thief sells easily — hence NO license where not needed. Second asymmetry-reason: the married man will not covenant with the shifchah (a man's bond is to his first wife — in time he sends her off), but for a single man she would be the FIRST love — an improper attachment. (4): the sale is FOR HER GOOD — the yiud-track (purchase-money = betrothal money, or the son weds her with שאר כסות ועונה undiminished). (5): she also "never exits" INTO the slave-class — no gentile sale by father OR master, no shpachut sale in betrayal. And the door/ear original (MAJOR color): a THIEF IS NEVER TRUSTED — yet the retention requires in effect the master's "I love my slave" (who would compel him to keep a thief six years in his house?) — so the declaration certifies the man is TRANSFORMED, now trustworthy; and that is the door's own measure: an OPEN door is thievish (lets the house be emptied), a CLOSED one is faithful; and the ear's: hard cartilage, soft lobe — hear the improper, fold the lobe in and close; hear the proper, stay open — DOOR, EAR, AND THIS MAN SHARE ONE MEASURE: certified gatekeepers. His timing-objection to RSbY/RYbZ (why not pierce at day one?) answered by the transformation-reading.

All 5 read in full. [78 bites: 1,869/1,962 = 95.3%]

## BATCH 79 (15 listings, 18,100 chars) — TRACTATE AVADIM (the minor tractate), Soferim's qere-ketiv triple, THE ROGATCHOVER, Tzror HaMor's Shechinah-triad

**Tosafot Meilah 13a:10:1** — the suckling-prohibition web: sanctified-animal milk barred via the אמו-אמו gezerah shavah with the FIRSTBORN verse of our parashah (שבעת ימים יהיה עם אמו, Exod 22:29); the Tosafist rule extracted: this gezerah shavah "is given to be expounded ONLY for matters dependent on the mother" (suckling, birth) — scoped-transfer doctrine. Peripheral (block-4 territory), read in full.

**TRACTATE AVADIM (the extra-canonical minor tractate), 5 rows** (MAJOR set):
- 1:2 the acquisition table: eved ivri ACQUIRED by money/document, ACQUIRES HIMSELF by years, yovel, deduction; the amah exceeds him — also by SIGNS; the NIRTZA is "acquired BY PIERCING" and self-acquires by yovel and the master's death — ADD: רציעה listed as a formal KINYAN-mode in the table.
- 1:5 MAJOR: sale "on condition the master not designate her" — SALE VALID, CONDITION VOID: "he stipulated against what is written in the Torah, and whoever stipulates against the Torah — his condition is void" (מתנה על מה שכתוב בתורה) — the yiud-track is NOT waivable by contract; the marriage-purpose is mandatory law (the Kiddushin 18b rule, here with the general contract-doctrine attached).
- 1:6 the priority algebra: master vs son both wanting yiud → MASTER first; son wanting yiud vs master accepting redemption → SON'S YIUD WINS, "for the mitzvah of designation precedes the mitzvah of redemption — אשר לא יעדה והפדה" (yiud > pedah even across persons). No designating two at once.
- 1:7 the BROTHER cannot designate — the kal vachomer from yibbum (the son, no yibbum-substitute, designates; the brother, THE yibbum-substitute, surely!) BLOCKED by ואם לבנו ייעדנה — "his son," not his brother. The yiud/yibbum substitution-pair split formalized (CONFIRM of Hirsch's Deut 23:1 pairing, now as the tractate's own derivation).
- 3:1 the nirtza protocol with TWO tannaitic forks: say-and-repeat required; R. YISHMAEL — the condition-matching gate (he has wife+children and the master hasn't, or reverse → NOT pierced) vs R. AKIVA — "either way he is pierced"; pierce with anything (even a thorn-point) but the MITZVAH is the מרצע; upper-ear (R. Meir) vs the lobe (R. Yehudah); RIGHT ear only; before the court; door standing like the doorpost.

**Tractate Soferim 6:5** — the scribes' canonical THREE written-לא-read-לו cases: אשר לא כרעים (Lev 11), אשר לא חומה (Lev 25), and OUR אשר לא יעדה — the 21:8 qere/ketiv crux sits in the official scribal triple (the consent-veto/duty fork's textual base certified).

**TZAFNAT PA'NEACH (the Rogatchover) 4 rows** — the formal-jurisprudence layer:
- 21:6: WHY piercing admits no agent (Mechilta: "he and not his messenger"): acts whose duty is the RESULT admit agency; רצע demands the ESSENTIAL ACTOR (פועל עצם) — "that HE pierce from beginning to end" — personal performance constitutive.
- 21:8: "no designating two at once" + "no selling to two" grounded in BODY-TITLE metaphysics: kinyan-haguf cannot vest by halves (the half-slave "half a man" of Yevamot 68a, the two-erech problem of Arachin 8a, the one-belly of Ketubot 103) — hence the Mechilta's separate exclusions.
- 21:10 MAJOR: from אם אחרת יקח לו the Mechilta rules "A MAN IS OBLIGATED TO MARRY OFF HIS MINOR SON" — and the Rogatchover derives the WHOLE yiud-to-son architecture from that duty: yiud-to-minor-son valid (Yerushalmi), retroactive-kiddushin when his signs complete (קדושין למפרע); NO yiud by the son's son (the duty doesn't cascade) and NO yiud by a WOMAN owner (no marry-off duty on her) — the son-not-brother rule explained structurally by the paternal duty, not just the verse.
- 21:11: FOUR stacked readings of אין כסף — (a) Mechilta: "free of money but NOT of the GET"; per the view that the support-triad runs FROM PURCHASE (the Torah's standing yiud-entitlement makes her quasi-espoused), the unredeemed amah exits by a manumission-type WRIT with NO KETUBAH = אין כסף; (b) the deduction-exit carries NO SEVERANCE-GRANT (אין שילוחה מעמך — Kiddushin 16b) — yiud-exit likewise = אין כסף; (c) for ketubah-deoraita: yiud makes only ERUSIN and a betrothed has no ketubah = אין כסף; (d) yiud-by-words (הרי את מיועדת לי, Rashi/Rashbam) vs the Bavli. Plus the identification: Rambam Hilkhot Melakhim's commoner's PILEGESH = exactly amah-yiud grade (needs the release-writ, no mamzerut-taint). The Rogatchover treating our clauses as a formal system — title-halves, essential actors, duty-derived powers.

**Tzror HaMor, Deut 22:6:3 (Midrash HaNe'elam)** — MAJOR-allegory: inside the bird's-nest discourse, OUR TRIAD OWED TO THE SHECHINAH: the shameless pray "like dogs — give, give" for their own מזון וכסות ועונה, but none provides HERS — her שאר = the Shechinah's food, her כסות = the mitzvah-garments (tzitzit-wrap, hand-tefillin — תפלה לעני כי יעטוף), her עונה = SHEMA IN ITS APPOINTED TIME (קריאת שמע בעונתה); "ואם שלש אלה לא יעשה לה — לשכינה — ויצאה חנם אין כסף": he stands shameless before her. The three garments (כסותה / שמלתו / במה ישכב, 22:26) = THREE GILGULIM, keyed to the three annual appearances; the 50 gates of understanding = חירות העבדים ("the slaves' freedom" — the FIFTY Exodus-mentions in the Torah); God Himself חבוש with Israel ("no prisoner frees himself" applied to the Shechinah in exile); the four judge-virtues (אנשי חיל...שונאי בצע) reappear as what the praying generation LACKS. The mystical inversion of the wife-rights triad, converging with Siftei Kohen's scholar-regimen (bite 77) — the triad as Israel's service-contract with the Shechinah.

All 15 read in full. [79 bites: 1,884/1,962 = 96.0%]

## BATCH 80 (12 listings, 19,267 chars) — TZROR HAMOR (guards-and-vineyard, flee-from-din), Vayikra Rabbah's 60-mitzvot census, YALKUT sweep (flood-lawlessness, Hagar, Moses' commission)

**Tzror HaMor 21:1:1** — "dinim BEFORE the Torah and dinim AFTER": Marah's שם שם לו חק ומשפט in front, ואלה המשפטים behind — the king walks with a guard before and behind, HE in the middle; dinim = the vineyard's FENCE (a trespasser strikes the fence, not the vines; עשו משמרת למשמרתי); first-in-thought and last-in-deed; world-sustainers (אלמלא מוראה). Dinim CLEAVE to Torah (unlike Cuthite law) hence eternal-as-truth (משפטי ה' אמת); NO judge may deviate from Torah-din by his own lights — except COMPROMISE with the parties' consent. ADD — the header as a PROCEDURAL ACROSTIC: ואלה = witness-examination; המשפטים = the duty to OFFER COMPROMISE before judging; אשר = if both parties consent; תשים = judge both together, promptly; לפניהם = no deference to the eminent — "all the ways of judgment and compromise are contained in this one verse."

**21:1:2 — THE FLEE-FROM-DIN THEOLOGY** (MAJOR): din is deep — one must FLEE it toward compromise, as we ourselves beg Heaven for mercy not judgment (David before sin: בצדק אחזה פניך; after: ואל תבא במשפט); משפט itself = mercy MIXED with din; הישר והטוב = compromise; the SANHEDRIN SITS BESIDE THE ALTAR (Chamber of Hewn Stone) so the Temple's awe drives them toward compromise — they "leaven the din" overnight (מלינין... ומחמיצין); gentile courts = PURE din (Esau, איש אדום), no mercy or compromise — litigating there magnifies wrath-worship and profanes the Merciful (CONFIRM of the idolatry-testimony reading with the din/rachamim metaphysic); and the HEDYOT-COMPROMISE RULE (ADD): the layman is excluded not only from din but because he chases compromise WITHOUT KNOWING THE DIN — "the compromise must sit NEAR the din" (קרובה לדין) or it is robbery — compromise-competence requires din-competence. The ו of ואלה ties the code to the altar-rules (no iron, no steps — the ramp of mercy); slave-release opens the code because the freed slaves' FIRST commandment ought to be mercy on slaves; שש שנים = the 6,000-year sign (ועבד חפשי מאדוניו at the seventh — the eschatological clock again, CONFIRM of Siftei Kohen bite 76).

**21:2:1** — exile as measure-for-measure for UNRELEASED slaves (freed from Egypt yet enslaving their brothers → back to bondage; the Jeremiah 34 causation, CONFIRM); the court-appearance PUBLICIZES that the master did not coerce the stay; and ADD (novel gloss): בגפו read as the ARTISAN'S TOOL-KIT — "a term of craft-implements: if he brought his tools in with him, he takes them out with him — the master may not retain them." The tools-exit property rule.

**21:7 + Lev 1:2:13** — the a-fortiori (the BOUGHT slave must be freed — surely no one may sell his own daughter "like the slaves"; the sale survives only as the yiud/pedah track); Midrash HaNe'elam (MAJOR-allegory): the pericope = BODY AND SOUL — the neshamah is the king's daughter (כבודה בת מלך פנימה) who must never exit כצאת העבדים; even if her deeds are רעה — REDEEM HER, lest she be lost בעם נכרי (the alien realm); אם אחרת יקח לו = "from OTHER dust he sprouts" — GILGUL; ואם שלש אלה = Job 33:29's הן כל אלה יפעל אל פעמים שלש עם גבר — THE THREE LIVES; yibbum as soul-pedion, eglah arufah as pedion for the slain — hence the murder-verses follow. And the PIKADON NO-SET-OFF rule (ADD): a bailee must return the deposit and may NOT retain it against a debt owed him from elsewhere — grounded in בידך אפקיד רוחי: God returns the morning soul-deposit though the depositor owes Him everything (פדית אותי ה' אל אמת); Lev 5's ומעלה מעל בה' = the deposit's only witness is God — denying a bailment denies the Witness. Plus the calf-as-stolen-deposit midrash (the rings given to Aaron; ישלם שנים = Nadav and Avihu).

**Vayikra Rabbah 24:5** — ADD (the census row): R. Yudan in RSbY's name: Moses wrote THREE pericopes of SIXTY mitzvot each — PESACHIM, NEZIKIN (ours), KEDOSHIM; R. Levi: seventy each — reconciled: nezikin-70 counts the SHEMITTAH pericope with it. The 60-mitzvot census of our parashah in the classical count.

**Yalkut sweep (5 rows)**: 44:4 + 51:2 (MAJOR lexeme-anchor): "אין משים אלא דין" — משים MEANS JUDGMENT, prooftext OUR HEADER — so Job's מבלי משים = "for want of justice they perish": the FLOOD read as the anti-mishpatim catastrophe; with the engineered-immunity theft (each takes UNDER a perutah — "to where the court cannot reach" — de-minimis abuse as the flood-crime: gaming the jurisdictional threshold); "you acted outside the line — I will too." 79:6 ADD crossref (Gen 16 ↔ 21:8): Abraham to Sarah on Hagar — לא תתעמר בה and OUR לעם נכרי לא ימשול למכרה — "having made her a mistress we cannot re-enslave her": the betrayal-ban applied as PATRIARCHAL PRACTICE to Hagar (the amah whose status cannot be degraded back; and the angel still sends her back to submit — the two-sided aggadah). 89:2 — the acquisition-modes sugya: a wife is acquired by intercourse (ובעלה) but the AMAH IS NOT — the blocked hekesh from OUR אם אחרת יקח לו ("like the 'other' by biah, so the amah?" — קמ"ל no); our clause inside Kiddushin's opening derivations. 100:2 — the matrilineal-status law: the shifchah's child follows her FROM OUR האשה וילדיה תהיה לאדוניה (the nokhrit's from כי יסיר); plus the R. Yose HaGalili fork ("you are free, your child a slave": child follows the mother per האשה וילדיה; the sages: his words stand). 167:6 (MAJOR color — the commission-reversal): Datan and Aviram taunted Moses מי שמך לאיש שר ושופט — God: "with שימה they mocked you; WITH שימה I MAKE YOU: ואלה המשפטים אשר תשים לפניהם" — the header's verb as the divine answer to the Egypt-era delegitimization; with the overseer-adultery aggadah behind מכה איש עברי (Moses saw "what he did to him at home and what he was about to do in the field") and the three views on וירא כי אין איש.

All 12 read in full. [80 bites: 1,896/1,962 = 96.6%; 40 readable rows remain + 26 Tanakh crossrefs]

## BATCH 81 (16 listings, 20,225 chars) — YALKUT SHIMONI remazim 224-319: the Mechilta/Kiddushin weave in full

**224:1 — the PRIORITY LADDER** (CONFIRM+ADD): pediyah > arifah (firstling donkey); YIUD > PEDIYAH from OUR אשר לא יעדה והפדה; and the historical FLIP logged beside it — yibbum > chalitzah "at first, when they intended for the mitzvah; NOW that they do not intend for the mitzvah, chalitzah precedes yibbum" — priority rules indexed to the agent's intent-quality across history; master's-redemption-first (Lev 27). Our yiud-priority sits in the canonical precedence table.

**273:1** — the Sinai-marriage cluster in Yalkut form (apple-blossom before leaves = doing before hearing; the jewel-parable; courtship-gifts; kartisin annulled; ויחן singular — ONE association, "the Torah is all peace, to the peace-loving nation I give it"; make yourself ownerless as the desert; "this day" = ever-fresh). CONFIRM.

**306:3** — ADD (the peacemaker parable): two enemy donkey-drivers; one's animal collapses, the other passes — then remembers כי תראה חמור שנאך and turns back to load with him; they enter the inn, eat, drink, make peace — "who made peace between them? that he understood this in the Torah" (אתה כוננת מישרים). The mishpatim as the peace-ENGINE, not just constraint. Plus ועז מלך משפט אהב (the Strong One who loves the judgment He could override); מלך במשפט יעמיד ארץ; ואלה mosif on MARAH's chok umishpat; "I gave them the Torah — you give them the mishpatim."

**307:2 — the four-times transmission protocol AT OUR HEADER** (CONFIRM): R. Akiva — the duty to repeat until learned (שימה בפיהם) and the duty to SHOW THE REASONS (להראות לו פנים) from ואלה המשפטים אשר תשים לפניהם; the seder-mishnah baraita (Moses from the Almighty → Aaron → his sons → the elders → all Israel; each ends holding FOUR passes; hence "teach your student four times"; and the kavod-distribution rationale for the rotation).

**308:2** — the Amoraim applying our header to THEMSELVES: Abaye to Rav Yosef (coercing gittin): "we are HEDYOTOT" (no semikhah in Babylonia); R. Tarfon's baraita — wherever there are gentile courts, "even though their law is as Israel's law, you may not resort to them" — לפניהם ולא לפני כותיים (Gittin 88b). The identical-law-still-forbidden rule CONFIRMED in the Yalkut's row.

**310-313 — the Mechilta chain on 21:2-4**: court-sold serves the SON (vs Deut's לך ולא לאח — the son-in/brother-out with the tie-breaker "yibbum only exists where there is NO son," so son-substitution outranks); Rabbi: התורה קראתו עבד על כרחה (the Torah called him slave AGAINST ITS WILL — the Yalkut original of Hirsch's quote); the CONVERT included as eved ivri — R. Eliezer by verse, R. Yishmael by the formal DAYO principle (דיו לבא מן הדין להיות כנדון — the convert serves six, not twelve). 311:1 the עבודת-עבד ban unpacked: no foot-washing, sandal-tying, bathhouse-carrying, hip-support on stairs, no litter/chair/sedan — "as slaves do"; BUT בבנו ובתלמידו רשאי — a son or student MAY do these (fork vs Hirsch's stricter reading at bite 71 logged); trade-protection: the master may not teach him a public-serving trade (bath-keeper, barber, tailor, butcher, baker) nor SWITCH him from his craft (R. Yose: if it was already his trade, he may practice it); sale-clock CONFIRM (שביעית למכירה ולא לשנים); exit needs no writ and no money. 311:2 the illness table + ADD the NEEDLE-WORK carve: Rav Sheshet — "sick all six" still exits IF he could do needle-work (light-duty capability keeps the term running); sick 4 = must complete. 311:3 the מעת-לעת reckoning baraita; R. Shimon's board-derivations ("if HE is sold — are his wife and children sold?!" — hence the master feeds them) with the tzricha; R. YISHMAEL vs R. AKIVA on אם בגפו: permission-reading vs the LIMB-reading ("entered whole-limbed, exits whole-limbed" — Rava: בגופו יצא = not released by limb-loss, against the pay-her-eye-value hava-amina; R. Eliezer b. Yaakov: יחידי — single → no shifchah). 312:1: the union מיוחדת לו — "that she not be an ownerless bondwoman"; children INCLUDING tumtum/androginos follow her (מכל מקום); R. Natan — וילדה לו extends to the MASTER's own children by his shifchah: slaves. 313:2: the nirtza inherits the whole pericope-regime (והוא יצא בגפו / R. Yitzchak's a-fortiori); SELF-SELLER fork: tanna kamma — no shifchah for him (לו ולא למוכר עצמו) vs R. Eliezer — yes, from משנה שכר שכיר: ADD the gem — "a hireling works by day; the eved ivri by day AND night — and how, given טוב לו עמך? Said R. Yitzchak: HIS NIGHT-WORK IS THE SHIFCHAH" (the double-wage = the breeding-service, derived); the shifchah/nokhrit sons create no yibbum-bond (האשה וילדיה + כי יסיר, with the tzricha).

**315-316 — the declaration machinery**: two sayings; the crosswise conditions table as baraita (his/master's family, mutual love, either sick → not pierced; BOTH sick → Rav Bibi's teyku); "his master loves him — that his property was BLESSED through him"; equality — לא ישנה רבו עליו, feeds him from his own; אף לאמתך תעשה כן = for the SEVERANCE-GRANT, not piercing (העבד ולא אמה — the amah never pierced; the תעשה double-duty); and RAVA'S PERUTAH-WINDOW formalized: the saying must fall inside the LAST PERUTAH's span — said before it began or after it ended = not pierced even if doubled (כשהוא עבד + סמוך ליציאה jointly pin the window). KOHEN-SHIFCHAH FORK: Rav yes / Shmuel no; with the internal proof-attempt — the sages' "no kohen is pierced (he'd be blemished)" presupposes the kohen CAN reach the piercing scenario, i.e., he must have been given a shifchah (else he could never say "I love my wife").

**317:1 — the piercing protocol + THE MARQUEE LINE** (MAJOR): consult-his-sellers (שימלך במוכריו); Rabbi's minority — pierced בינו לבין עצמו (privately, no court act); door-standing hekesh; the blocked mezuzah-k"v (door unfit-for-mitzvah yet fit → mezuzah surely — blocked by ונתת באזנו ובדלת: DOOR ONLY); הוא ולא שלוחו; RIGHT ear by the אזנו-אזנו gezerah shavah FROM THE METZORA (Lev 14:14); the lobe (R. Yehudah) vs even-the-cartilage (R. Meir) fork TIED to the kohen-question (Meir: no kohen pierced/sold at all, so no blemish-avoidance needed); RYbZ's ear-that-heard; and then verbatim: **התורה אמרה במרצע והלכה אמרה בכל דבר — "the TORAH said 'with an awl,' and the HALAKHAH said: with anything"** — the halakhah-overrides-text formulation stated in so many words ON OUR מרצע, the GRA-manifesto registry item (bites 40s, Rashbam bite 70) in the Yalkut's own row.

**319:1 — the amah lattice**: the sale-window via the vows-analogy + the signs-k"v; the eight-way din-and-refutation net (mother sells neither daughter nor herself; the daughter neither sold for her theft nor pierced — "if He extracts her from the HARSH sale, a fortiori from the light piercing"); father's kiddushin-power k"v from his amahood-power; her acquisition by money (R. Yishmael's k"v from the shifchah kenaanit) and by document (והלכה והיתה); R. AKIVA: acquisition-by-money from OUR אם אחרת יקח לו — "the Scripture likened the LOWER one to the UPPER one: as the 'other' (wife) by money, so the amah" — the אחרת-hekesh running in the acquisition direction too; sold to ONE amahood never two; R. Yose HaGlili's ladder: kiddushin-after-kiddushin and kiddushin-after-amahood YES, amahood-after-kiddushin NO, amahood-after-amahood surely not — the other side of the shpachut-after-shpachut tannaitic split (Riva, bite 74). 

All 16 read in full. [81 bites: 1,912/1,962 = 97.5%; 24 readable remain]

## BATCH 82 (17 listings, 18,810 chars) — YALKUT 320-925: the triad permutation table, the sale-proportionality sugya, Moses as the nirtza, the three-places row CLOSED

**320:2-3** — the father's-rights architecture rooted in OUR verse: daughter's earnings to the father DERIVED from the amah (מה אמה מעשה ידיה לרבה אף בת... לאביה — needed for the NAARAH; the minor is obvious "he can sell her — her earnings?!"); the learning-blocks en route (money not learnable from ritual-law nor from fines); kiddushin-money to the father from OUR אין כסף ("no money for THIS master, but there is for ANOTHER master — the father"); the exit-comparison refined (kiddushin ≠ amah-exit — she still lacks chuppah; vow-annulment shows the shared jurisdiction); find-rights from enmity-prevention; get-reception by hekesh. The complete father's-rights table hanging off our block.

**320:4 — three-way fork on בבגדו בה**: R. Yonatan b. Avtolmos — the BETRAYAL reading: having betrayed her (disgraced her, not as befits daughters) he may NOT now keep her (בגידה = falsehood, prooftext MALACHI בגדה יהודה — the Rashbam crossref bite 70 is this tanna's); R. Yishmael — the MASTER who bought on designation-terms and reneged; R. Akiva — the GARMENT reading: "after he spread his cloak over her" (marital canopy). Plus: רעה glossed as failure-of-favor; אשר לא יעדה = the master's clause, והפדה = the father's; NO yiud-condition sale per R. Yose HaGlili vs R. AKIVA — he MAY sell on the no-yiud condition and designate anyway if he wishes (the tnai fork, other side of Tractate Avadim 1:5); and ADD: לעם נכרי read as a warning TO THE COURT (אזהרה לבית דין שלא ימכרנה לגוי) — the addressee of לא ימשול is the bench itself.

**320:6-7, 321:1 — THE TRIAD PERMUTATION TABLE** (MAJOR): son-not-brother din with the achuzah-vs-yibbum tie-breaker; the בא ללמד ונמצא למד row in its tannaitic original (R. Yoshiyah: the amah-clause ends up teaching ALL Israel's daughters; R. Yonatan: the ivriah, with אם אחרת carrying the bat-yisrael). Then the three tannaitic semantics of שארה כסותה ועונתה: R. YOSHIYAH — food (Micah's אכלו שאר עמי) / clothing / conjugal (from וישכב אותה ויענה); R. YONATAN — AGE-appropriate clothing (not an old woman's garb for a girl) / SEASON-appropriate clothing ("not summer's in the rains — each in its עונה=SEASON"), with food and conjugal then derived by kal vachomer ("things she was not married for you may not withhold — things she WAS married for, surely"); REBBI — conjugal (שאר בשרו!) / clothing / FOOD (עונה from ויענך וירעיבך). Every member of the triad migrates across all three readings. Plus Rav Yosef: שאר = BODY-CLOSENESS — "he must not treat her in the Persian manner, who serve their beds clothed"; Rav Huna: the "I in my garment, she in hers" husband DIVORCES AND PAYS THE KETUBAH. And the מכאן אמרו: "a man must marry off his minor son" + "when do you merit seeing grandchildren? when you marry your children young." לא יגרע assigned per the Yoshiyah/Yonatan fork (the already-designated amah vs the bat-yisrael).

**321:2** — שלש אלה = designate-you/son/redeem ("the passage speaks only of the ivriah"); חנם מן הכסף ולא מן הגט — free of MONEY, not of the WRIT (this view requires a get for the timed-out amah — the Rogatchover's source, bite 79); the double-exit written twice שלא יתן לבעל דין לחלק ("give the litigant no opening to split"); Abba Chanan: חנם = bagrut, אין כסף = SIGNS (teaching gierion); "give money before signs came — give none after."

**342:6 — the SALE-PROPORTIONALITY SUGYA** (MAJOR): sold for his theft — "not less and not more"; R. Yehudah: stole under his worth — NOT SOLD; over his worth — THE VICTIM'S OPTION: "if he wishes to sell, he sells; if not, he writes a NOTE" (the Mechilta original of Hirsch's victim's-veto, bite 72); the 1000/500 table: theft 1000 / worth 500 → sold; theft 500 / worth 1000 → NOT sold — נמכר כולו ולא חציו ("sold WHOLE, never half") — no partial-term sales; R. Eliezer: only at exact parity; his-theft-not-hers; the amah's three exclusives (signs-exit, forced redemption, NEVER SOLD TWICE) vs the eved's resale — Abaye: no resale to the same man [for the same theft], resale across two men stands (בגנבתו ולא בכפלו ולא בזממו — never for the fine, never for false-witness liability); and the RECIDIVISM ASYMMETRY: why not coerce the eved's family to redeem him as we coerce for her? "he would go and sell himself again" — and she? "she CANNOT be sold again" — the incentive-analysis inside the sugya. Also the burglar day/night rule imported via the naarah-hekesh (בא ללמד ונמצא למד again; block-2).

**627:1, 665:11, 667:4** — the gender-exclusion catalog (man sells daughter, woman doesn't; man sold for theft, woman never — inside the priestly/stoning list); the PREVENTIVE-WELFARE parable on וכי ימוך (the load still ON the donkey — one man steadies it; fallen — five cannot lift: hold your brother BEFORE he falls; "supported him four and five times — support him again"; עמך = your life takes precedence); the GER/WOMAN acquisition rules: a ger is not acquired as eved ivri (no family for ושב אל משפחתו) and acquires only symmetrically (Rav Nachman b. Yitzchak: he acquires under the NOKHRI regime — serving neither son nor daughter); ADD — a WOMAN does not acquire a male eved ivri (לאו אורח ארעא — propriety; converging with the Rogatchover's no-yiud-by-woman from the duty side); the RSbG fork on women owning Canaanite slaves (ivri צניע, kenaani פריץ; Rav Yosef's widow-rules with the dog/meat-scrap simile); gentile-acquisition rules (you from them, never they from you or each other; war-captives — the sugya answering Riva's bite-74 question; slaves acquired like landholdings: money, document, chazakah).

**814:3 — MOSES AS THE NIRTZA** (MAJOR crossref, the Deut 3 ↔ 21:5 settlement-link's locus): Moses at the Jordan pleads OUR piercing-formula against his death-decree: "You called me servant... You wrote in Your Torah ואם אמור יאמר העבד אהבתי את אדוני — I LOVE YOU, YOUR TORAH, AND YOUR CHILDREN — לא אצא חפשי, I do not wish to die; והגישו אדוניו אל האלהים... ועבדו לעולם — but with me You did not fulfill it!" God answers רב לך. Exit-to-freedom = death; eternal service = life — the declaration inverted into Moses' own prayer. [Settlement-link candidate Deut 3:23-26 ↔ Exod 21:5 CONFIRMED at its midrashic locus.]

**898:2-3 — the severance-grant eligibility table** (MAJOR): the עברי/עבריה difference-table ("in him what is not in her, in her what is not in him — both needed"); לך ולא ליורש with the son-in/brother-out tie-breaker; self-seller term fork (six-or-more vs R. Eliezer's six-only); fled-and-returned completes; SICK-AND-HEALED — the master is NOT reimbursed for the idle time (יצא לחפשי חנם — ADD: the idleness-wage hava-amina killed by חנם); haanakah extended to yovel-exit, master's-death-exit, and the amah's signs-exit (the תשלחנו ribbuyim) but DENIED to the fleer and the deduction-exiter ("his sending is not from you") — R. MEIR flips the deduction-exiter to YES; Rava's fled-met-yovel case (no grant even so); self-seller: no grant (the לו-exclusion) vs R. Eliezer — his לו excludes THE CREDITOR instead (לו ולא לבעל חובו, tied to the R. Natan debt-assignment doctrine).

**898:7 — THE THREE-PLACES ROW, CLOSED** (MAJOR — registry item at its source): R. Shimon: "In THREE places the HALAKHAH UPROOTS THE SCRIPTURE (הלכה עוקרת את המקרא): the Torah said 'cover the blood in DUST' — the halakhah: anything that grows plants; the Torah said 'a BOOK of severance' — the halakhah: anything detached; the Torah said 'WITH AN AWL' — the halakhah: with anything. And Rabbi says: at the door or doorpost STANDING." The GRA-manifesto registry (bites 40s; Rashbam 70; Yalkut 317 bite 81) now closed at its Sifrei/Yalkut locus — our מרצע as one of the canonical three overrides.

**899:2, 925:1** — עבד עולם = "all the days of the YOVEL'S WORLD" (עולמו של יובל — the epoch-reading; "even sold 30-40 years before yovel"); the עולם-עולם gezerah shavah transferring the two passages' rules; אף לאמתך = grant not piercing. And the yefat-toar close (ADD crossref Deut 21 ↔ 21:10): the captive's forks (nails/hair cut-vs-grow; 30/90 days; the deliberate disfigurement design "the Israelite daughter rejoices while she weeps"); ending: ובעלתה... והיתה לך לאשה — "AS IT SAYS: שארה כסותה ועונתה לא יגרע" — even the war-captive's marriage terminates in OUR TRIAD: the hairbreadth maxim reaches the battlefield bride.

All 17 read in full. [82 bites: 1,929/1,962 = 98.3%; 7 readable remain]

## BATCH 83 (7 listings, 5,350 chars) — THE READABLE CENSUS CLOSES: kiddushin's fountainhead, the right-side triple, Maharshal's two-witness door

**Yalkut 936:5** (MAJOR CONFIRM — the Bavli locus of the 320:3 row): the OPENING derivation of tractate Kiddushin — a wife is acquired by MONEY from OUR ויצאה חנם אין כסף ("no money for THIS master — but there IS money for another master," the father); the parallel קיחה-קיחה from Ephron's field; the mechanics (he gives and he speaks = valid; she speaks = void); R. Shimon's lost-object parable (the man courts because "the owner of the loss searches for his loss"); the document-derivation with Abaye's advocate-turned-accuser objection ("money brings in AND casts out?" — "this coin is one matter, that coin another — and the COINAGE is one"); Rava's וכתב לה; and the amah-grounded kal-vachomer for money-acquisition (with the yevamah-tokhiach, closed by כי יקח). The whole institution of kiddushin-by-money FOUNDED on our exit-clause.

**Yalkut 938:17 + Zevachim 24b** (CONFIRM with dialectic): the right-side gezerah-shavah system — the sages: רגל-רגל from the metzora for chalitzah; R. ELAZAR: אזן-אזן from the metzora for OUR PIERCING (right ear); R. Yochanan: "the attribution is reversed"; Rava: no reversal — אזן-אזן is vacant-for-exposition (מופני), רגל-רגל is not (the metzora's cedar-hyssop-scarlet block). And Rava's canonical triple at Zevachim 24b: יד-יד for kemitzah, רגל-רגל for chalitzah, אזן-אזן FOR RETZIAH — our rite in the Bavli's own right-side list. **Zevachim 82b**: the baraita תושב = קנוי קנין עולם (the pierced), שכיר = קנוי קנין שנים (the six-year man) — the Lev 22:10 category-pair (Hirsch, bite 73) at its Bavli locus.

**Yeriot Shlomo (Maharshal)**: 21:1 — the altar-juxtaposition resolved as "PLACE THE SANHEDRIN BESIDE THE ALTAR" (the addition-to-Sinai reading forces the question, the Temple-bench answers it); 21:6 ADD (the two-witness door): the ו of ובדלת makes ear+door a strict pair (ordered out-of-sequence to lean on our verse), and the design-reason — "there is NO DOOR WITHOUT A DOORPOST, so the door counts as TWO WITNESSES; a doorpost is found without a door" — the piercing-scene requires a two-witness assembly, hence door (which implies its post) and not post alone; the R. Shimon Egypt-witnesses drasha thereby gets its mechanism. 21:7 — the amah-tokhiach defense of the hekesh (לרווחא דמילתא).

**READABLE CENSUS COMPLETE: 1,936/1,936 read-and-ledgered in 83 bites. Remaining: the 26 TANAKH-VERSE crossrefs (--tanakh mode).**

## BATCH 84 — THE 26 TANAKH CROSSREFS (--tanakh mode; dump script patched he_plain->he for the new-Mac tanakh.sqlite schema)

The block's canonical intertext ring, read in the Hebrew: **Deut 15:12-18** (the parallel law: תשלחנו חפשי "send him out free," the awl-verse with ואף לאמתך, the double-wage משנה שכר שכיר, the blessing-close); **Exod 6:6 + 7:4** (בשפטים גדולים "with great JUDGMENTS" — the שפטים wordplay: the Exodus itself executed as a court-act, the redemption oracle behind the block's first-law placement); the block's own self-linked verses (21:3, 4, 8 — with the לא/לו ketiv visible in the plain text, 10, 26-27 the tooth/eye releases); **Exod 22:2** (ונמכר בגנבתו — the sale-source); **Exod 24:3** (כל המשפטים in the covenant-reading, the people's one-voice נעשה); **Exod 30:23** (מר דרור — "freedom myrrh" heading the anointing oil: דרור the release-word in the sanctuary's own perfume); **Exod 31:18** (the tablets written by the finger of אלהים); **Lev 19:20** (the shifchah charufah — בקרת תהיה לא יומתו כי לא חפשה); **Lev 22:10-11** (תושב כהן ושכיר — our two slave-grades in the terumah law, and the kohen's money-purchase WHO DOES EAT — קנין כספו הוא יאכל בו); **Lev 25:10** (וקראתם דרור — yovel: each to his holding, each to his family), **25:39-40** (no slave-labor, כשכיר כתושב, until yovel), **25:55** (כי לי בני ישראל עבדים — the sugya-anchor of the entire block, in situ); **II Kgs 4:1** (the prophets'-widow: והנשה בא לקחת את שני ילדי לו לעבדים — the creditor coming for the two children as slaves: the LIVE ABUSE-CASE of debt-slavery that Elisha's oil-miracle reverses — the prophetic counter-story to our block's protections); **I Chr 16:14 = Ps 105:7** (בכל הארץ משפטיו — His judgments in ALL the earth: the universality claim); **Ps 119:137** (צדיק אתה ה' וישר משפטיך). All 26 read in full and ledgered.

# ═══════════════════════════════════════════════════════════
# BLOCK 1 SCAN COMPLETE — 2026-08-10
# 84 bites. 1,962/1,962 required listings read-and-ledgered
# (1,936 readable + 26 Tanakh). 0 unread. 0 unruled.
# Mechanical check: BLOCK-1 GATE GREEN (oral_coverage chapter
# gate still FAIL as designed — 2,943 rows anchored at 21:12-37
# belong to blocks 2-3 and accumulate in this same ledger).
# The FULL ORAL TORAH LAW's first full-inversion scan is done.
# Next: derivation/coding phase on owner word.
# ═══════════════════════════════════════════════════════════
