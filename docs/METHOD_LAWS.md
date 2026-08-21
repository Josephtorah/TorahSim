# The method laws

These are the binding rules the work in this repository was done under.
They are not aspirations; each one is enforced by a mechanical gate
somewhere in the pipeline, and a violation blocks the work from shipping.

## 1. Declared reading, honest ledgers

*(Rewritten 2026-08-21 by owner ruling; the original law mandated complete
inversion on every derivation. The owner's words: "I might want to only
read the Talmud on one verse or block of verses — that law is too rigid.")*

Reading depth is a **per-item choice** — a verse, a block, a chapter may
be read to any declared depth, from one targeted source to the complete
inversion. Three things remain law: the chosen scope is **declared up
front and never silently narrowed** (the 2026-08-10 drift stands as the
warning); the reading ledgers are **append-only**; and the labels stay
honest — "read through" is claimed only where every enumerated source
carries a logged verdict, whatever scope was chosen. Every oral citation
in a unit must name a source actually read in a ledger.

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

## The constitution of the re-derivation era (owner ruling, 2026-08-21)

**"RE is the approach."** The project runs as reverse engineering: the
text is the binary, the recorded outcomes are the traces, the worked
cases are the test vectors, and the Oral Torah is the recovered
engineering documentation. From that frame, three standings:

**Immutable** — the text itself; the reading ledgers (append-only,
always); the test corpus — unit assertion batteries, the scene-stamp
baselines, the case gradings. Tests only accumulate; deleting a test or
re-freezing a baseline takes the owner's word.

**Freely rewritable** — unit logic, the world engine, the renderers,
and the TIR catalog (`logic/TREE_INTERPRETATION_RULES.md`, the
tree-interpretation rulebook; owner clarification 2026-08-21: "I think
these rules should stay flexible" — its discipline is its own born one:
provisional unless proven, promoted on multi-unit re-runs, a dated
status note per rule change, and the gates catch any citing unit a
change breaks). Any edit, for any reason, under two conditions: **all gates stay
green**, and the edited unit gains a one-line `changelog:` entry with a
bumped `rev:` (absence of the field means rev 1 — the 97 shipped units
need no retroactive edits). A gate refuses any unit diff that arrives
without its changelog line. The freeze ritual is demoted to one job:
issuing full-rule stamps. The unit YAMLs' `status: frozen` field is
historical vocabulary meaning *shipped model* — the code it marks is
rewritable under this law, and the public pages say "model, revision N,"
never "frozen," of code.

**Owner's word required** — method-law changes, test deletion or
rebaselining, full-rule stamps, and publishing.

The amendment-receipts design of 2026-08-20 (bd9642a) stands as history
and precedent for witnessed amendment, but per-edit receipts are no
longer required — the changelog line and the green gates are the
record.

## The verse-status labels (settled 2026-08-20)

Every verse on the public scroll carries a status — two tracks and one
flag — and these definitions are written once, here, so no level can
quietly weaken. Labels are computed from the records on every build and
a gate re-derives all of them from the records and refuses drift; none
is ever set by hand.

**The oral track** — how much of the tradition has been walked on the
verse. *Unopened*: no tier-1 sources enumerated. *In reading*: sources
enumerated, verdicts logged for some; always displayed with the honest
fraction. *Read through*: every enumerated source carries a logged
verdict — the full check. Attribution carries a grain: verse-grain where
the counts come from the per-verse join of the link index against the
triage ledger; chapter-grain where a law-era reading ledger in
`scans/ledgers/` covers the chapter — its rows anchor to the chapter's
law, so per-verse fractions there would undercount and are never shown.

**The derivation track** — what has been built on the verse.
*Underived*. *First pass*: inside the declared span of a shipped unit
whose `tree_derive_version` is absent or any v1 value — absence means
first pass by definition. *Full rule*: inside the span of a unit stamped
with the full-rule value by the stamp ritual, which refuses the stamp
unless the unit's whole span is read through by the records. The
ninety-seven shipped units are first pass; the recital says so and the
grid shows it.

**Proven** — an orthogonal flag, not the top of the ladder: the verse's
covering span lies inside a chapter compiled to machines whose recorded
cases run green against the frozen baseline. The flag computably drops
if that baseline ever goes red. Exodus 21 today reads chapter-grain
read-through, first pass, proven — the flagship itself mid-process by
the law's own standard, which is the era's honest story.
