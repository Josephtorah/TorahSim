# Sources — building your own shelf

To *run* everything in this repository you need nothing beyond what is
already in `data/` — the Hebrew text, the word tags, and the English gloss
lexicon all ship here, self-contained.

To *continue the derivation work* — scan a new block of law and code it —
you additionally need the oral-law library itself: the works of the chain
of transmission (see `CHAIN_OF_TRANSMISSION.md`). Those texts are not
redistributed in this repository. Instead, this repository ships the same
mechanism the original project used: **fetchers** that build you a local
shelf, block by block, from the open digital library at
[Sefaria](https://www.sefaria.org).

You do not need the whole library up front. A derivation consumes sources
*per block of verses*: pick your block, fetch its sources (a few minutes),
scan, derive. The original project's shelf grew to gigabytes only as
months of such blocks accumulated.

## The three commands

```
# step 1 — the link index: which sources speak about these verses?
python3 tools/fetch_links.py Exodus "21:1-11"

# step 2 — the texts of those sources, by category
python3 tools/fetch_texts.py Exodus.21.1 Exodus.21.11

# step 3 (optional) — the whole-work corpus, for cross-book scans
python3 tools/fetch_corpus.py
```

All three write into `shelf/` (gitignored — the shelf is a cache; the
permanent record of a derivation is its scan ledger, claims, and
citations). All are resumable: already-fetched files are skipped. And all
observe the **politeness contract** hard-coded in them: sequential
requests, half a second apart, small ranges per invocation. Sefaria
provides this library as a public service — treat its servers
accordingly. (The corpus builder is the one sanctioned exception to
"never a whole book at once": it reads Sefaria's *bulk export bucket*,
published exactly for whole-work downloads, not the live site API.)

## What the fetchers bring you, work by work

The default categories fetched map onto the chain of transmission like so:

| Chain work | Sefaria category | Examples of what arrives |
|---|---|---|
| The Targumim, the early Aramaic translations | Targum ("translation") | Targum Onkelos on your verses |
| The Mishnah ("the repeated teaching") | Mishnah | the tractates citing your verses |
| The Tosefta ("the supplement") | Tosefta | parallel passages |
| The legal expositions — midrash ("exposition") on the law | Midrash | the Mekhilta ("rule, measure") on Exodus, Sifra ("the book") on Leviticus, Sifrei ("the books") on Numbers/Deuteronomy |
| The two Talmuds ("the learning") | Talmud | every passage of the Babylonian and Jerusalem Talmuds anchored to your verses |
| The law codes — halakha ("the law, the way to walk") | Halakhah | Rambam's Mishneh Torah, the Shulchan Aruch |
| The commentators | Commentary (not fetched by default — add it: `python3 tools/fetch_texts.py Exodus.21.1 Exodus.21.11 Commentary`) | Rashi, Ramban, and the rest |

`all` as the third argument fetches every category Sefaria links to the
verse — the widest possible scan base.

## The whole-work corpus (step 3)

Span fetching answers "what speaks about *these verses*?" Some questions
run the other way — "where does *this phrase* occur across the whole
canon?", "read this tractate end to end" — and for those
`tools/fetch_corpus.py` mirrors complete works into `shelf/corpus/`, one
JSON file per work per language: both Talmuds, the Mishnah, the Tosefta,
Rambam's Mishneh Torah, the halakhic midrash (both Mekhiltas, Sifra,
Sifrei), Bereshit and Vayikra Rabbah, Minchat Shai (the Masoretic
apparatus), the Zohar ("Radiance"), Sefer Yetzirah ("Book of Formation" —
both recensions, the letter-classification system compared against the
word-tag layer), the JPS 1917 English Torah, Sefaria's cross-reference
link shards, and Strong's Hebrew lexicon. `--plan` lists what would be
fetched without downloading; `--only <substring>` restricts to matching
works (for example `--only yetzirah`).

## Licensing of what you fetch

The ancient Hebrew and Aramaic texts are in the public domain. The
*editions and translations* Sefaria serves carry per-version licenses —
some public domain, some Creative Commons with conditions (for example,
some English translations are licensed for non-commercial use). Every file
the text fetcher saves records the version titles and license fields
Sefaria reported, so the information is in your hands.

For the derivation workflow this rarely matters: scanning, reading, and
citing sources by reference (tractate, chapter, section) — as every scan
record in `scans/` does — is ordinary scholarship. Check a version's
license before *redistributing its text*; do not commit your `shelf/` into
a public repository.

## Verifying the Hebrew Bible data itself

`data/tanakh.sqlite` derives from the Westminster Leningrad Codex text with
Open Scriptures Hebrew Bible tags (see `ATTRIBUTION.md`). To verify or
rebuild it from the source of truth, the upstream project is:

  https://github.com/openscriptures/morphhb   (CC BY 4.0)

## The press databases (since 2026-08-20)

The derivation press in `press/` reads a fuller database than
`data/tanakh.sqlite`: `data/derivation.sqlite` (~3.2 GB, uncommitted),
which indexes the whole Torah — words, marks, morphology, trees, roles —
together with the frozen units, their steps, the triage ledger, and the
oral-link index. It is a derived, rebuildable artifact. The chain, run
from the repo root, in order:

```
python3 press/build_db.py          # shelf/sources/*.xml + logic/ rules -> data/derivation.sqlite
python3 press/index_units.py       # logic/units/*.yaml -> units/steps/coverage tables
python3 press/index_triage.py      # logic/oral_triage/ -> triage table
python3 press/index_oral_links.py  # shelf/sources/sefaria_links/ -> oral_links table
python3 press/export_web.py        # -> scroll/data/ (189 files, byte-reproducible)
```

`shelf/sources/` holds the Tier-A source files the build reads (OSHB
XML, the JPS 1917 JSON, the Sefaria link shards); `logic/FETCHLOG.md` is
the append-only log of how each arrived. Two further database files are
*pinned snapshots*, cited by the frozen derivations and not rebuildable:
`data/source-snapshot.sqlite` (the gloss layer's fixed text) and
`data/debut-snapshot.sqlite` (the word-debut census). They stay out of
git for size — keep a private backup. `data/world.sqlite` is the world
fold's state, regenerated by `python3 press/corpus_world.py`.
