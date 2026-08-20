# The method laws

These are the binding rules the work in this repository was done under.
They are not aspirations; each one is enforced by a mechanical gate
somewhere in the pipeline, and a violation blocks the work from shipping.

## 1. Full inversion — read everything

A derivation walks the **complete** record of what the oral tradition says
on its verses. Coverage is counted word by word in a scan ledger, and an
incomplete scan mechanically blocks every later step. No skimming, no
sampling, no "the relevant passages." Narrowing a scan's scope is never
permitted silently.

## 2. Witnessed claims only

No constant, branch, or rule enters a machine without a claim ID, and no
claim ID exists without a citation of the work in the chain of transmission
that witnesses it. The code's citation graph is checkable: every number in
the machines can be traced to a tractate, chapter, and section.

## 3. Disputes are data, never decisions

Where the tradition records a live disagreement — a machloket ("division,"
a recorded dispute between authorities) — the machine returns **both
positions as a fork**. The code never silently picks a side, and a fork is
never flattened for convenience. (The settled-practice branch may be
*marked*, with a citation, but the other branch rides along.)

## 4. The tests are the tradition's own worked examples

The assert battery is drawn from cases the sources themselves compute, with
the answers the sources themselves give. We do not invent test cases for
the law; we transcribe them. A machine that cannot reproduce the
tradition's own arithmetic does not ship.

## 5. Dependency edges must prove

Every claimed reliance on another verse is a declared edge, and the proof
checks all of them mechanically: backward edges must resolve against an
actually derived unit, and forward edges must fail to resolve. An
inheritance that cannot be proven is a build failure, not a footnote.

## 6. No invented events

Simulations and test scenes replay events the text records — never events
we imagine. We simulate the *law*; we do not generate history. Where a
fact needed by the law is absent from the text, the scene says so rather
than supplying one.

## 7. Honest verdict labels

Every machine verdict on a Tanakh case is labeled against the text:
CONFIRM, DIVERGE, FORWARD (depends on law not yet derived), or
NO-VERDICT-IN-TEXT. Divergences are reported on the same scoreboard as
confirmations, at the same size. A verification project that hides its
misses is not one.

## 8. Hebrew never appears without English

Every Hebrew word or phrase, everywhere in this repository — code comments,
documents, web pages, output — carries an English gloss inline. Hebrew
script is the display form (not transliteration), and the English is always
beside it. This is enforced by a lint program (`tools/gloss_lint.py`) over
every shipped file. The project must be fully readable by someone with no
Hebrew at all.

One declared exception: the scan notes and narrative-unit manifests in
`scans/` are preserved working records, shipped exactly as written during
the scans, and they predate this gate. Their marquee items are glossed but
their compressed digest style leaves some quoted source lemmas
untranslated; the lint reports these honestly rather than the records
being retouched. See `scans/README.md`. The derivation review pages in
`scroll/units/` are the same class — generated renderings of the
derivation records, carried across from the workshop with their
verification citations structurally intact, under one documented
redaction: the workshop's own name and its private filenames were
neutralized at copy time (a snapshot database and two working notes,
cited by neutral description in eight pages). They ride under the same
rule: reported, never gated, never retouched further.

The 2026-08-20 capability transfer widened this class once, the same way.
When the canonical unit YAMLs, the triage ledgers, the parser rule notes,
the method documents, and the append-only fetch log crossed from the
workshop into `logic/`, the same border redaction was applied and is
recorded in `logic/README.md`: the workshop's name, its database
filenames, and its private working-note filenames were neutralized to the
forms this repository uses (`derivation.sqlite`, `source-snapshot.sqlite`,
`debut-snapshot.sqlite`, `provenance/`, "the interim coordinator") —
thirty-seven references across the crossing, zero remaining. The received
prose records under `logic/docs/`, `logic/oral_triage/`,
`logic/taamim_rules/`, and `logic/FETCHLOG.md` keep their original gloss
discipline and are reported, never gated, never retouched. The canonical
YAMLs themselves are gated forward: any future edit to them is new
derivation work and answers to every law here.

## 9. Scope honesty

The project's claims end where its mechanism ends. The machines verify
consistency; they possess no agency — they decide nothing the text left
undecided and prove no theological proposition. The standing summary is
**consistency certified, agency absent**, and every document that presents
results carries the scope it was measured under. This is an experimental
model of a legal tradition, not binding religious law.
