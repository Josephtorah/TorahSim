# THE STEPS — from verse to proven logic

One span of text (a verse, a block, a chapter) moves through these steps,
in order. Steps 1–2 are already done for the entire Hebrew Bible but are
part of the process. The scroll's labels report exactly which step a
verse has reached — never more. (As of 2026-08-21; the RE-era
constitution governs.)

## Step 1 — Parse the verse  ✅ done, whole Bible
The reading marks (the cantillation) split the verse like brackets:
the strongest pause first, down to the leaves — the word-bricks. Every
one of the 23,213 verses parses to exactly one legal tree under rules
v3. This is the verse's STRUCTURE.
   → shows as: the verse tree window and the leaf rows on every verse.

## Step 2 — Apply the morphology  ✅ done, whole Bible
Every word in every leaf is tagged with its grammar: verb form, tense,
person, noun state, prefixes split out — with the dictionary number for
each root. This is each word's IDENTITY.
   → shows as: the morph table on every verse.

## Step 3 — Declare the reading
Choose how much of the oral tradition to read for this span — everything
(the full inversion), one work (just the Talmud), one verse's worth, a
block. Owner's choice, per item. The scope is DECLARED up front and
never silently narrowed.

## Step 4 — Read and log
Actually read each chosen source against the text. Every source gets one
ledger row with a verdict: material (bears on the logic) / context /
enrichment / duplicate / not-bearing. The ledger is append-only forever.
When a source ARGUES by one of the middot — the tradition's own
numbered inference rules (see logic/MIDDOT.md) — the note names it
(e.g. "argues I1 qal wa-chomer from the paid keeper").
The two big Oral books read differently, and the note says which you
got: a Mishnah paragraph is a RULING — an input→output case, no reason
shown; a Talmud passage is a DERIVATION (hooking verses), a DISPUTE,
or a TEST. Find the implementing tractates by topic in
logic/MISHNAH_TOPICS.md (all 63 mapped).
   → shows as: chip "in reading 39/63" or "read through"; grid cell fill.

## Step 5 — Extract claims
Each material finding becomes a claim: an ID, the statement, the source
that witnesses it. Nothing enters code without a claim; no claim without
a read source. Each claim carries a `middah:` field when the source's
inference form is identifiable — the 13 rules of Rabbi Ishmael for LAW
spans, the 32 of Rabbi Eliezer for NARRATIVE spans; absent = the source
states plainly rather than infers.
Claims come from TWO inputs, checked as a list: the reading's material
rows, AND the standing canon rules that pattern-match the span — the
utterance census fires on every qualifying va-yomer ("and He said");
middah tagging fires on every argued inference. (Lesson of the day-4
blind compare, 2026-08-21: each session missed exactly one of the two.)

## Step 6 — Write or amend the logic
Four inputs combine to produce each verse's logic step:
a. THE TREE (Step 1) gives the SHAPE — which words group together, what
   the verse's halves are (e.g. Gen 1:1 splits [the creation event |
   the two objects]).
b. THE MORPHOLOGY (Step 2) picks the OPERATOR TYPE: a narrative-past
   verb = an EVENT that happened; a "let there be" mood = a COMMAND
   issued; a participle = an ONGOING condition; a verbless clause = a
   STATE.
c. THE RULE CATALOG — TIR = the Tree-to-logic Interpretation Rules,
   the living catalog at logic/TREE_INTERPRETATION_RULES.md — maps
   recurring grammar patterns to operators the same way every time.
   Every operator line cites its rule, so nothing is a one-off
   judgment call. (The catalog itself stays flexible — model layer.)
d. THE CLAIMS from the reading (Step 5) correct and extend what
   grammar alone can see — e.g. the tradition counts Gen 1:1 as an
   utterance though the "said" verb is absent; disputes are carried
   as recorded disputes, testimony as witness-tier state. A claim
   licensed by a middah keeps that middah's own constraints as
   assertions (the dayo cap on a-fortiori transfer, genus match,
   two-verses-await-the-third). Where a TIR rule and a middah cover
   the same ground (the particle/list rules), the TIR rule stands
   and CITES the middah as chain authority — the day-one pattern.
The output is the unit: steps with operators, each citing its rule
and/or claim, plus the assertions and scenarios that become the tests
of Step 7. Every edit takes one changelog line and a rev bump. Free to
do any time; the gates are the only tax.
   → shows as: unit page "MODEL · REV N", operator rows citing sources.

## Step 7 — Run the gates
One command, all green or the change doesn't ship: unit assertions,
renderings reprinted, world refolded to its hash, scenes vs baseline,
changelog check. (Deleting or rebaselining a TEST takes owner word.)

## Step 8 — The stamp (owner word only)
When a span's declared reading is COMPLETE and its logic was rebuilt
from that reading, the owner may order the full-rule stamp.
   → shows as: chip "full rule" (until then: "first pass").

## Step 9 — Prove against cases (where the text records cases)
Compile the logic to a machine; run the recorded cases against it,
every miss printed. Recorded cases include the tradition's own case
tables: the Mishnah's input→output rows, graded at the reading, join
the scene list (the Exodus 21 pattern — 64 scenes from its chapter
reading).
   → shows as: chip "proven"; drops automatically if a test goes red.

## Step 10 — Publish
Export, parity check against the public repo, deploy. Owner's word.

## The chip, decoded
  ⓘ read through · 10 material · first pass · proven
  [--- Step 4 status ---]           [Step 6/8]   [Step 9]
- oral track: unopened → in reading n/m → read through
- derivation: underived → first pass (logic predates its reading)
  → full rule (logic rebuilt FROM a completed reading, stamped)
- proven: recorded cases run green against the compiled machine

## Where to look
- every verse: the chip (hover for the full sentence)
- the whole map: ▦ coverage (torahsimulation.org/scroll/coverage/)
- the logic + citations: click the unit chip → unit page
- the receipts: this repository's scans/ ledgers (append-only)

## Creation week, honestly (as of 2026-08-21)
| Day | Verses  | Step 4 (reading) | Step 6 (applied) | Stamp |
|-----|---------|------------------|------------------|-------|
| 1   | 1:1-5   | complete         | YES — rev 2      | eligible, not stamped |
| 2   | 1:6-8   | partial          | no               | —     |
| 3   | 1:9-13  | partial          | no               | —     |
| 4   | 1:14-19 | complete         | YES — rev 2      | eligible, not stamped |
| 5   | 1:20-23 | complete         | no (findings logged) | eligible, not stamped |
| 6   | 1:24-31 | partial          | no               | —     |
| 7   | 2:1-3   | partial          | no               | —     |

623 sources remain unread, all on days 2, 3, 6, 7. The original seven
units (July 28) were built BEFORE the reading standard existed — that is
what "first pass" means, and why the redo era exists. Days one and four
have walked the full path (read → claims → amend → gates) — day four
twice, independently, blind-compared, then unified. That is the pattern
for the rest.
