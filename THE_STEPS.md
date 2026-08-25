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
The MINIMUM shelf per track — which books ground material findings,
law and narrative, with the full-name decoder for the tradition's
shorthand — is logic/CORE_SHELF.md.
STANDING DEFAULT (owner, 2026-08-23): the declared scope IS the core
shelf unless the owner orders otherwise. The full source list is still
enumerated and recorded in the ledger, its unread remainder marked
outside declared scope; depth passes run only on the owner's order,
for a named reason.
PRE-ENUMERATION (owner, 2026-08-25, speed ruling): the enumeration and
register classification for every remaining block is computed AHEAD in
one mechanical pass — each sitting starts with its declared list
already printed, never re-deriving it by hand.

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
SPEED RULINGS (owner, 2026-08-25, binding for the Genesis walk):
(a) READ AT THE PARASHAH GRAIN — one sequential pass over a weekly
portion's primaries covers all its blocks; the ledgers stay
per-block. (b) STANDING-VERDICT CREDITS — a source already verdicted
in any prior ledger is CREDITED, never re-read; duplicate clusters
are precomputed so dup rows are verdicted without being opened.
(c) TERSE NON-MATERIAL ROWS — every declared source still gets its
verdict (that is what read-through means), but only material rows
take full-finding prose; enrichment / dup / no-bearing rows are one
line. The work is NOT split across windows — one derivation stream
(owner, same ruling).
CREDIT GUARDS (owner, 2026-08-25, "I will accept your changes" — amending
(b) on the workshop's proposal): (1) a credited source whose standing row
says nothing about the current block's ops gets a QUICK LOOK, not a blind
credit; (2) a dup cluster is credited unopened only after at least ONE
member has been fully read in some ledger; (3) sources carrying NUMBERS
or ink-level claims — counts, spellings, written-vs-read forms — are
NEVER dup-credited without opening: that is the class where seats
diverge (the canopy counts 9/10/11 vs 13/11/10 are the standing
exhibit).
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
BATCH STAMPS (owner, 2026-08-25): the word may cover a batch — a
parashah, a section — in one utterance; per-block stamps are not
required. The freeze ritual and the landing overhead (index → render
→ export → gates) then run once per batch, not once per block.
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
| 1   | 1:1-5   | complete         | YES — rev 3      | ✔ STAMPED 2026-08-23 |
| 2   | 1:6-8   | complete (core shelf) | YES — rev 3 | ✔ STAMPED 2026-08-23 |
| 3   | 1:9-13  | complete (core shelf) | YES — rev 3 | ✔ STAMPED 2026-08-23 |
| 4   | 1:14-19 | complete         | YES — rev 3      | ✔ STAMPED 2026-08-23 |
| 5   | 1:20-23 | complete         | YES — rev 3      | ✔ STAMPED 2026-08-23 |
| 6   | 1:24-31 | complete (core shelf) | YES — rev 3 | ✔ STAMPED 2026-08-23 |
| 7   | 2:1-3   | complete (core shelf) | YES — rev 3 | ✔ STAMPED 2026-08-23 |

THE CREATION WEEK IS WHOLE (2026-08-23): all seven days stand at FULL
RULE — Genesis 1:1 through 2:3, read through under the declared law,
logic rebuilt from the readings, stamped on the owner's word, end to
end. The week's story in one breath: day four walked the path twice,
blind-compared, then unified; day five ran the two-inputs law solo;
day two was the timing race that made the narrow scope law; day three
put Onkelos under load; day six read a hundred sources and closed the
census at the tenth utterance; day seven — the speech-less day, zero
utterances confirmed — finished fastest, and rest itself entered the
witness tier as a thing created. The original seven units (July 28)
were built BEFORE the reading standard existed; twenty-six days later
the redo era re-derived every one of them from the tradition's own
pages — that is what "first pass" meant, and why the redo era exists.
The walked path (read → claims → amend → gates → stamp) now turns to
the rest of the Torah.

THE EDEN BLOCK OPENED (2026-08-24): gen_08 (Genesis 2:4-17, the
garden and the first rule) became the first July v1 unit carried
end-to-end by the RE-era path — 146 of 146 declared sources read, 48
material (the project record), the Noachide laws derived word-by-word
from our 2:16, the 2:15 extra-yod corrected to the ink, stamped full
rule on the owner's "gen_08 good" and landed in canon.

PARASHAT BERESHIT READS THROUGH (2026-08-25): the speed rulings above
carried the walk through the whole first portion in two days — gen_09
through gen_11 (the helper, the serpent, the sentences) derived in
the workshop and landed; gen_12 (Cain and Abel, 77 of 77 declared
sources verdicted, 37 material) the first sitting ever run in the
canon window itself; gen_13 through gen_15 (the two lines and the
flood prologue) swept in from the workshop's first true
parashah-grain pass. Genesis 1:1 to 6:8 now reads READ THROUGH end to
end — full rule through 2:17, the rest honestly first pass, the batch
stamp awaiting the owner's word. REMAINING: 58 blocks (gen_16 through
gen_73 — the July partition covers the whole book, 50 chapters, no
gaps) under the speed rulings above, walking onward by parashah —
Noach next.
