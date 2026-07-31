# Bacher's lexicon vs our cache — what the 1899 census adds to the detector

**The work.** Wilhelm Bacher, *Die exegetische Terminologie der juedischen
Traditionsliteratur* ("The Exegetical Terminology of Jewish Traditional
Literature"), Leipzig, 2 volumes: I (1899) — the terminology of the
**Tannaim** (the Mishnah-era teachers); II (1905) — the terminology of the
**Amoraim** (the Talmud-era teachers). It is the scholarly census of exactly
what our detector hunts: the chain's technical vocabulary, catalogued
alphabetically as a LEXICON — hundreds of entries, each with definition and
source citations. Bacher's thesis is our finding stated 130 years early:
the Oral chain speaks a **closed, formulaic, technical language**.

**Provenance (honest).** The archive.org scan
([dieexegetischet00bachgoog](https://archive.org/details/dieexegetischet00bachgoog))
was fetched 2026-07-31 (1.3 MB OCR text, scratchpad only — not cached in
Data/). The Google OCR preserved **zero Hebrew characters** — every headword
is destroyed, so the entry list cannot be machine-extracted from this copy.
The Hebrew translation (*Erkhei Midrash*, "Entries of Midrash," A.Z.
Rabinovitz) is NOT on Sefaria (name-API checked, logged in FETCHLOG). The
candidate list below is therefore **reconstructed from scholarship on
Bacher's entries, not OCR-extracted** — and every candidate was tested
empirically against OUR OWN 708-source cache
(`logic/middot_scan/bacher_scan.py`), which is this project's honest
instrument. Survey tier only; nothing here mints a rule (*ein adam dan
me-atzmo* — "one may not derive on his own").

## A. NEW devices with real yield (not in the detector's lexicon)

| # | term (glossed) | sources | why it matters to us |
|---|---|---|---|
| 1 | **keneged** ("corresponding to" — the correspondence/typology operator) | **69** | The biggest blind spot found so far: third-highest-yield device in the whole cache (behind *yakhol/talmud lomar* 76 and *davar acher* 60). It is the aggadic MAPPING operator — "X was created keneged (corresponding to) Y" — the chain's way of declaring two structures isomorphic. For a project whose thesis is cross-referenced architecture, the chain's own isomorphism-declaration operator is core instrumentation. |
| 2 | **ma'aseh be-** ("an incident concerning") | **68** | The case/precedent marker — narrative cited as evidence. The chain's unit-test-by-example. |
| 3 | **ve-omer** ("and it says" — stacked additional prooftext) | 66 | Bacher catalogues it as the tannaitic multi-witness citator (second prooftext when one does not suffice). Needle is noisy (also plain dialogue); document-frequency use only. |
| 4 | **minayin** ("from where [is this derived]?") | **51** | The derivation QUESTION — the interrogative that opens a sourcing demand. We scan the answers (*talmud lomar* etc.) but were blind to the question form. |
| 5 | **tanya / tanu rabbanan** ("it was taught / the Rabbis taught") | 27 | Stratum markers: Tannaitic material quoted inside Amoraic text. This is Bacher's own two-volume split operating INSIDE our sources — see section C. |
| 6 | **le-mah ha-davar domeh** ("to what may the matter be compared") | 20 | The parable ANNOUNCEMENT formula — the execution form of rule 26 (*mashal*, "parable") of the 32. We scanned the rule name; this is how it actually fires. |
| 7 | **ktiv hakha u-khtiv hatam** (Aramaic: "written HERE and written THERE") | 17 | The Bavli's Aramaic executor of *gezerah shavah* ("equal decree" — verbal analogy). We scan the Hebrew form (*ne'emar kan ve-ne'emar lehalan*, 9 sources); the Aramaic twin was invisible — adding it nearly triples executor coverage. |
| 8 | **bo u-re'eh** ("come and see") | 17 | Demonstration summons — the aggadic sibling of the Bavli's *ta shema* ("come hear"). |
| 9 | **mah ra'ah** ("what did he see [to prompt this]?") | 8 | The motivation question — asked of a speaker or of Scripture's phrasing. |
| 10 | **eino omer … ela** ("it does NOT say … but rather") | 4 | A variant of our star diff operator *ein ketiv kan ela* ("it is not written here… but rather") — same minimal-pair move, spoken-form needle. Should be folded into that entry's needle list. |

Tail (real but small in this cache): *mai dikhtiv* ("what is [the meaning
of] what is written?") 5; *shema tomar* ("lest you say") 6; *ka-yotze bo*
("similarly") 4; *haynu dikhtiv* ("this is what is written," Aramaic) 3;
*ein li ela* ("I have only…") 2; *mena hani mili* ("from where are these
words?") 2; *ta shema* 2; *u-mah ani mekayyem* ("how do I uphold [the other
verse]") 1; *lo ba ha-katuv ela* ("the verse comes only to…") 1; *ein mikra
yotze midei peshuto* ("a verse never leaves its plain sense") 1.

**Baseline meter:** *she-ne'emar* ("as it is said") appears in **317 of 708
sources** — the plain prooftext citator saturates ~45% of the cache. Worth
recording as a DENSITY baseline (how citation-heavy is a source), not as a
discovery.

## B. The zeros are a coverage instrument (again)

Absent from the cache entirely: *ribah/miet ha-katuv* ("Scripture
included/excluded" — the inclusion-exclusion execution verbs of the Akiva
school), *klal amru* ("they stated a general rule"), *dibber ha-katuv
ba-hoveh* ("Scripture speaks of the usual case"), *dibberah Torah ki-lshon
benei adam* ("the Torah speaks in human language"), *ein mukdam u-me'uchar
ba-Torah* ("no earlier-and-later in the Torah" — the policy phrase; the
32's rule 31/32 announcements we do scan). These are **legal-midrash and
sugya devices** — their absence measures the cache's Genesis-narrative
bias, exactly like the seven absentees of the first discovery run
(*semukhin* "adjacency," *asmakhta* "support text," …). Their arrival is a
tripwire for when Leviticus/Exodus triage begins.

## C. What Bacher adds beyond needles: STRATIFICATION

Bacher's two-volume split (Tannaitic vs Amoraic terminology) is a DATING
instrument we have not been using: the chain's technical vocabulary has
layers, and the layers are distinguishable by formula. Concretely for v2:

1. Tag every detector formula by stratum — **tannaitic** (*talmud lomar*,
   *shomea ani* "I might understand", *melamed* "it teaches", *minayin*,
   *ein li ela*) vs **amoraic** (*hada hu dikhtiv*, *kemah de-at amar*,
   *mai dikhtiv*, *ktiv hakha u-khtiv hatam*, Aramaic generally) vs
   **both**.
2. A source's formula profile then estimates its layer — and *tanya / tanu
   rabbanan* (27 sources) marks the exact seams where an early text is
   quoted inside a later one: the chain's own provenance system, visible
   to the scanner.
3. This gives the public report a load-bearing point: the technical
   language was STABLE ACROSS CENTURIES and across two languages (Hebrew
   -> Aramaic twins of the same operators: *ne'emar kan* / *ktiv hakha*;
   *hada hu dikhtiv* / *haynu dikhtiv*; *zeh she-amar ha-katuv* / *mai
   dikhtiv*) — catalogued by Bacher in 1899, re-found empirically by our
   miner in 2026 with no access to his headword list. Two independent
   instruments, same closed vocabulary: the coordination argument in
   miniature.

## D. Recommendation — ADOPTED 2026-07-31 (owner order "yes add them to the detector")

Rows 1-9 of table A folded into the detector lexicon tagged `bacher`, the
*eino omer ela* needles merged into the existing *ein ketiv kan ela* entry,
and *she-ne'emar* added as a density baseline. Detector rebuilt (v1.3):
totals moved from 574 invocations in 277 of 706 sources to **1,249
invocations in 458 of 717** — cache coverage from 39% to 64% of sources
showing at least one detected device. Per-device yields at adoption:
she-ne'emar 317 · keneged 69 · ma'aseh be- 67 · ve-omer 66 · minayin 61 ·
tanya/tanu rabbanan 30 · le-mah ha-davar domeh 21 · ktiv hakha u-khtiv
hatam 17 · bo u-re'eh 17 · mah ra'ah 8. Stratum tags (section C.1) remain
middot-v2 work.
