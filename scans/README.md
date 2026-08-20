# The scan record

This tree is the evidence layer: the proof that the machines' rules were
*read out of the sources*, not invented. Three layers, from mechanical to
human-readable.

## `ledgers/` — the coverage proof

`Exod_21.jsonl`: 4,903 rows, one per source listing read during the
Exodus 21 scans — each row a citation (work, exact reference, timestamp).
The census target for the chapter was 4,903; the ledger holds 4,903. This
is method law 1 (full inversion) made checkable: every listing the link
index cataloged for these verses was opened and read. The ledger contains
citations only — no source text.

## `manifests/` — the witnessed claims

One JSON file per derivation unit: every legal or structural claim
extracted during that unit's scan, each with an ID, the verse it attaches
to, the claim stated in English, and the source citation that witnesses
it. The three law-block manifests are the witness layer of the Exodus 21
machines — `law01` (21:1–11, 39 claims), `law02` (21:12–27, 43 claims),
`law03` (21:28–37, 35 claims): 117 claims, and every constant and branch
in `machines/` cites one of them. The remaining files are the witness
layers of the 97 narrative units in `units/`.

## `notes/` — the scan notes

The working notes of the three Exodus 21 scanning days: batch-by-batch
digests of what each source said, the disputes found, the design decisions
they forced. This is the richest human-readable layer of the record — read
these to watch the claims being won from the sources.

## Preserved-record status

The notes and the narrative-unit manifests are **preserved working
records**: they ship exactly as written during the scans, and they predate
the repository-wide gloss lint gate. Their marquee items carry English
glosses, but the compressed digest style leaves some quoted Hebrew lemmas
untranslated — the lint reports these honestly (several hundred across the
tree) rather than the records being retouched to hide them. Everything
else in this repository — docs, machines, units, tools, and the three
law-block manifests — holds the strict zero-flag standard. See
`METHOD_LAWS.md`, law 8.

## Quotation and licensing

The scan record quotes sources the way scholarship does: by citation
(work, chapter, section), with brief quoted phrases and Hebrew/Aramaic
lemmas from the public-domain originals, analyzed in the project's own
words. No modern edition or translation is reproduced at length. See
`ATTRIBUTION.md` at the repository root.

## The census queues (added 2026-08-20)

`queues/law01_queue.json` (3,286 entries), `law02_queue.json` (2,450),
`law03_queue.json` (1,702): the enumeration side of the reading — for
each block of the chapter, every readable oral source the census found,
keyed source → work, category, class, segment count. The ledger above is
the reading's receipt; these are its to-read lists, preserved as written.
Together they close the loop the front page describes: the census set the
target, the ledger holds the 4,903 rows read against it.
