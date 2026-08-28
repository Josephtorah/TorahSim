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
THE SPINE DEFAULT (owner, 2026-08-27 — narrows the above; effective
at parashat Vayera): declared reading per span = the Torah book's ONE
SPINE + Onkelos. The spines: Genesis — Bereshit Rabbah; Exodus — the
Mekhilta of Rabbi Yishmael; Leviticus — the Sifra; Numbers — the
Sifrei on Numbers; Deuteronomy — the Sifrei on Deuteronomy. The
Mishnah and Talmud leave the reading pass and return at Step 9 as the
exam (see THE TWO SHELVES, Step 4). Unchanged riders: canon
pattern-rules fire on grammar; ink claims never credited unopened;
FULL enumeration with the remainder marked outside declared scope;
dual-track on disputes. Dependency on record: the sugya case-file
machinery must exist before Exodus's law spans — the thin-reading
deal is "the exam tests it." Full table + reasoning:
logic/CORE_SHELF.md.
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
THE TWO SHELVES (owner ruling 2026-08-27): the oral library splits by
which end of the bridge a book starts from, and the two kinds have two
different jobs. VERSE-ANCHORED books (Onkelos; the midrash
collections — the verse-by-verse expounding books — including the
law-midrash like the Mekhilta on Exodus)
start at the verse and walk toward the law — they are organized like
our units, so they are the READING SHELF: they feed Steps 3-4.
CASE-ANCHORED books (the Mishnah, with the Tosefta beside it) start
from the case and barely cite verses — they cannot be read at a verse
span, so they are the TESTING SHELF: their input→output rows are the
exam the machine faces at Step 9, routed by topic. The TALMUD is the
bridge between the two directions: it takes a Mishnah rule that looks
like pure addition and walks it back to the verse ("from where do we
know this?"). MEASURED on our deepest block (the goring ox — 35
witnessed claims, the expansion test of 2026-08-27): 22 of 35 walk
back to the verse's own ink or an argued analogy; exactly TWO are
additions with no compiled derivation behind them, and the tradition
labels both itself as decrees ("a king's decree"). One breath: the
Mishnah writes as if it is adding; the Talmud shows most of it was
derived; the true remainder arrives self-labeled.
SPEED RULINGS (owner, 2026-08-25, binding for the Genesis walk):
(a) READ AT THE PARASHAH GRAIN — one sequential pass over a weekly
portion's primaries covers all its blocks; the ledgers stay
per-block. WHY (measured in the sweeps, owner-confirmed): the reading
itself costs the same either way — batching cuts the OVERHEAD
(setup runs once, not per block; neighboring blocks share sources
that get read once and verdicted everywhere; credits compound
inside the sitting). Four blocks swept in ~23 minutes vs one block
the old way in over an hour. Never fall back to block-by-block.
(b) STANDING-VERDICT CREDITS — a source already verdicted
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
reading). The case-anchored books are this step's home shelf — see
THE TWO SHELVES in Step 4.
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
stamp awaiting the owner's word.

THE SWEEP ERA REACHES LECH LECHA (2026-08-25): the speed rulings
proved out at full scale. Parashat Noach went first (gen_16 through
gen_26 — eleven blocks in one workshop sitting), then parashat Lech
Lecha (gen_27 through gen_33, Genesis 12:1-17:27 — seven blocks, 660
declared sources read in about 35 minutes, 268 material findings).
All eighteen LANDED IN CANON the same day on the owner's word ("bring
torahsim up to date"): every declared source verdicted, every ledger
past the completion gate, every unit at rev 2 with its reading-pass
record, chips live from Genesis 1:1 to 17:27. TWENTY-FIVE blocks —
gen_09 through gen_33 — now stand read and green, waiting UNSTAMPED:
one batch word per weekly portion stamps them, ritual once per batch.
Genesis stands at 33 of 73 blocks read; 40 remain; the next sweep is
parashat Vayera, opening at gen_34 (Genesis 18:1), awaiting the
owner's word. [Superseded same week — Vayera ran; see the paragraph
after the plan.]

THE PLAN FROM HERE (2026-08-27, under the spine default): the rest of
the Genesis walk — Vayera (gen_34) through the end (gen_73), about 40
blocks — runs one parashah sweep at a time under ONE spine + Onkelos:
Bereshit Rabbah is Genesis's book. Everything else stays enumerated,
marked outside declared scope, recoverable on order. In parallel,
during the Genesis remainder, the sugya case-file machinery gets
designed and proven on the Exodus 21 material already in hand — so
that when the walk reaches Exodus, the law spans read thin (the
Mekhilta as spine) and the Mishnah/Talmud exam does the heavy testing,
per the two-shelves ruling. The spine default was retro-tested against
the 18 finished Noach and Lech Lecha ledgers before adoption: of 451
fresh material findings, 38% would have been kept by the spine, 43%
return through the exam's own channels, 13% wait for the OTHER books'
spines, and about 5.5% — the compilations that are never a spine —
stay honestly outside scope, recoverable only by depth order. Roughly
94% retention through the plan's own channels; the known soft spot
(Talmud NARRATIVE on Genesis, which no failed law case will summon)
is the next measurement in the workshop's queue.

VAYERA RAN FIRST UNDER THE SPINE (2026-08-28, landed in canon on the
owner's relayed word): five blocks — Mamre and the laughter and the
plea (gen_34, 102 of 102), the overthrow of Sodom and the cave
(gen_35, 74 of 74, with two same-sitting ink corrections caught by the
text gate: the yod spelling of 19:20's first ve-hi, a new member of
the three-scrolls census, and 19:16's defective vayachaziku), Gerar
and the dream and the prophet (gen_36, 41 of 41), the laughter and
the wilderness and the oath (gen_37, 71 of 71), and Moriah, the
binding, and the oath (gen_38, 62 of 62). The whole sweep: 27 minutes
53 seconds, 350 declared under the spine, 91 fresh material findings,
the outside-scope remainder carried with its shelf split marked.
Genesis 1:1 through 22:24 now reads READ THROUGH — 38 of 73 blocks;
THIRTY blocks (gen_09-38) stand honestly unstamped; Chayei Sarah
(gen_39, Genesis 23:1) is next on the owner's go.

THE SECOND SWEEP — CHAYEI SARAH (2026-08-27): gen_39 through gen_42
(Genesis 23:1-25:18 — the purchase, the mission, the meeting, the
end of Abraham; four blocks, 105 verses) in one sitting: 8,717
enumerated, 182 declared = 32 fresh Bereshit Rabbah + 41 standing
credits + 4 in-sitting + 105 Onkelos verses; 26 of the 32 fresh
sections material, some fifteen credits upgraded to material at their
home seats (the mourner's exemption claiming 23:3; the first-aging
census at 24:1; Isaac's afternoon prayer at 24:63), and 18 Onkelos
delta rows — the largest: 24:67 where the received translation
absorbs the deeds-like-Sarah midrash into the verse itself. The
sweep's exhibits: the double Ephron ink dossier VERIFIED against our
own tree (the defective "sitting," the dropped vav at the payment);
the triple-track seam at 25:3 where the midrash disputes "the
Aramaic translators" by name while our Onkelos renders a third way —
the two-shelves model's seam on exhibit; and the "it was after the
death" regression rule with its ink-guarded boundary, a
standing-rules-table candidate. The text gate caught NINE pre-recorded
draft defects across the three old-layout units (plene spellings
against defective verse ink, a written-form hi, two tree spans) — all
fixed and changelogged. All gates green; four ledgers, four rev-2
units. Genesis stands at 42 of 73 blocks read; THIRTY-FOUR blocks
(gen_09 through gen_42) green and unstamped, one batch word per
parashah stamps them. Next sweep: parashat Toledot, opening at gen_43
(Genesis 25:19).

THE THIRD SWEEP — TOLEDOT (2026-08-27, same sitting as Chayei Sarah):
gen_43 through gen_47 (Genesis 25:19-28:9 — the twins, Gerar, the
wells, the blessing, the flight; five blocks, 106 verses) in about
thirty minutes: 11,679 enumerated, 230 declared = 78 fresh Bereshit
Rabbah + 40 credits + 6 in-sitting + 106 Onkelos; 67 of the 78 fresh
material, with the blessing chapter alone carrying 93 declared
sources. The sweep's exhibits: the tomim and avdah DEFECTIVE-INK
claims both verified against our own trees; THE WELLS ARE THE BOOKS
(the chain mapping the Torah's own structure — seven books by Ben
Kappara's division — onto our well names); the tradition mapping its
own four-part canon (Scripture, Mishnah, Talmud, narrative lore) onto
the blessing's dew-fat-grain-wine at 27:28; Onkelos's two great
convergences — the matriarch-prophecy insert at 27:13 and the
when-Israel-casts-off-the-Torah condition written into 27:40 — beside
its dissent (the straight rendering of "I am Esau your firstborn"
where the midrash equivocates); the first-suffering census at 27:1
twinning the first-aging census at 24:1; and the
ratified-only-by-its-signatories and slave-property maxims arriving
from the case shelf as narrative logic. The text gate caught FOURTEEN
pre-recorded draft defects across the three old-layout units (tree
spans off the snapshot, paseq marks, plene spellings, a skipped word,
two fragments in an unrecognized notation) — all fixed and
changelogged. All gates green; five ledgers, five rev-2 units.
Genesis stands at 47 of 73 blocks read; THIRTY-NINE blocks (gen_09
through gen_47) green and unstamped. Next sweep: parashat Vayetze,
opening at gen_48 (Genesis 28:10).

THE FOURTH SWEEP — VAYETZE (2026-08-27, the day after Toledot):
gen_48 through gen_54 (Genesis 28:10-31:54 — the ladder, the well,
the switched bride, the twelve births, the rods, the flight, the
pursuit and the heap; seven blocks, 145 verses — the parashah's last
three verses, 32:1-3, live inside gen_55's whole-chapter block and
read with Vayishlach, because blocks are the ledger unit) in about
forty minutes: 13,534 enumerated, 287 declared = 84 fresh Bereshit
Rabbah + 47 credits + 11 in-sitting + 145 Onkelos — the biggest
sweep yet, with the credits compounding hard (Toledot's flight
arithmetic row turned out to have its home seat here and was
credited, not re-read). The sweep's exhibits: the WELL SEVEN WAYS
(one narrative frame instantiated over seven institutional schemas,
Sinai's completeness gate included — the strongest simulation-facing
find so far); the LABOR-OVER-MERIT doctrine at 31:42 ("merit
salvaged money, labor saved lives"); the vow's whole legal lifecycle
born at Bethel (first vow, the four-vows ledger, the delayed-vow
audit); the hire-law defaults derived at 30:16 and the bailment
rebuild of 31:39 — two testing-shelf wires the case-file machinery
will want; Rachel's theft solved two ways (the midrash defends her
intent, Onkelos demotes the verb from stole to hid — the cleanest
two-track exhibit yet); Leah's eyes (the midrash reads
tender-from-weeping, Onkelos renders beautiful — the buffer taking a
side in a recorded quarrel); the mixing-of-joys law born at 29:27;
the three-keys doctrine with Onkelos rebuilding 30:22 as petition
language; the truncated-prophecy doctrine double-witnessed at 31:24;
the treaty's commerce carve-out argued before David's Sanhedrin
centuries later; the Aramaic dignity row at the two-tongues verse;
and Elijah settling his own tribal-provenance dispute in person.
The text gate found ZERO pre-existing defects — all seven draft
units were already clean, the first defect-free sweep. All gates
green; seven ledgers, seven rev-2 units. Genesis stands at 54 of 73
blocks read (Genesis 1:1-31:54 continuous); FORTY-SIX blocks (gen_09
through gen_54) green and unstamped. Next sweep: parashat
Vayishlach, opening at gen_55 (Genesis 32:1 — the whole chapter,
carrying Vayetze's three-verse tail).

THE FIFTH SWEEP — VAYISHLACH (2026-08-27, same sitting as Vayetze —
the first two-parashah day): gen_55 through gen_59 (Genesis
32:1-36:43 — the camps and the wrestling, the meeting, Dina's
chapter, Beit El and the three deaths, Edom's roster; five
chapter-aligned blocks, 156 verses, gen_55 carrying Vayetze's
three-verse tail) in about forty minutes: 12,293 enumerated, 294
declared = 67 fresh Bereshit Rabbah + 63 credits + 8 in-sitting +
156 Onkelos — the largest declared count yet, and the leanest fresh
load: the credit engine now pre-answers half the parashah (rows read
in the morning's Vayetze sweep came back as afternoon credits at
their home seats). The sweep's exhibits: the sciatic-nerve law at
its birth verse with the which-leg dispute; the who-won honesty
("we do not know — but who was filled with dust?") beside Onkelos
refusing "you strove with God" and turning Peniel's seen God into
seen angels; the EIGHT-ADONI arithmetic — eight "my lords" spoken to
Esau at gen_55, eight Edomite kings counted at gen_59 (a numeric
claim minted in one block and cashed in another, four chapters
apart); the dotted-kiss rule's hard case at 33:4 (script and dots
equal — kissed or bit, the marble neck); the Seir audit resolving
the unpaid promise eschatologically; the barrel exchange at Dina's
chapter recorded open (muddied-vs-clarified — the moral verdict as
a standing dual); the third-day danger sugya quoted whole at 34:25
(a testing-shelf cluster running into the reading); the fondness
table — God's covenant vocabulary learned from the violator's own
verses; the delayed-vow enforcement closing the arc Bethel opened,
with Onkelos's bookkeeping complete (promise, recall, discharge all
in the accepted-prayer/Word-as-support vocabulary); the hidden death
of Rebecca under Alon Bakhut; the two-language seam at Ben Oni
marked by the chain itself ("in Aramaic… in the sacred tongue" —
and the buffer IS the Aramaic seat); Rachel's grave sited on the
road to plead for the exiles, against the anti-monument maxim; and
the mamzer audit of Edom's roster. The text gate again found ZERO
pre-existing defects — the second defect-free sweep, same day. All
gates green; five ledgers, five rev-2 units. Genesis stands at 59
of 73 blocks read (Genesis 1:1-36:43 continuous, 1,084 of 1,533
verses — 71%); FIFTY-ONE blocks (gen_09 through gen_59) green and
unstamped. Next sweep: parashat Vayeshev, opening at gen_60
(Genesis 37:1).

THE SIXTH SWEEP — VAYESHEV (2026-08-28, one sitting). Parashat
Vayeshev read at the parashah grain under the spine default:
gen_60 through gen_63 (Genesis 37:1-40:23, 112 verses, four
chapter-aligned blocks — the coat and the sale, Judah and Tamar,
Potiphar's house, the two prison dreams). 10,547 sources
enumerated; 226 declared read = 45 fresh Bereshit Rabbah + 58
standing credits + 11 in-sitting + 112 Onkelos verses; 163 chain
primaries recorded outside declared scope (the levirate chapter
alone pulls 41 bridge sources to the border — enumerated, held
for the exam). The flywheel's best day yet: gen_63 closed on TWO
fresh reads — seven of its ten midrash sources were owned upstream
in the same sitting. The sweep's exhibits: the three-slanders /
three-repayments scales that run blocks three and four (the goat,
the slavery, the she-bear); the dream as a DEED — Joshua
commanding the sun as "my father's purchase"; the dream logged
with a quill (day, hour, place); the firstborn-redemption five
sela'im and the beka-per-head priced from the twenty silver; the
four cups of Passover seated at the butler's cup; Judah initiating
the levirate marriage with the second-permission rule quoted whole
(testing-shelf machinery at the narrative seat); the three pledges
decoded as the dynasty's three crowns (signet-kingship,
cord-Sanhedrin, staff-Messiah); the Divine Spirit in three courts
("you attest the revealed, I attest the concealed") beside the
buffer SPLITTING the same word into verdict-plus-paternity; the
crown dual at 39:11 — the chain's three-way on "to do his work"
(accounts / indeed / not-a-man) and Onkelos VOTING for the
account-books; the Memra-support formula transferred to Joseph
and Joseph's own memra governing the prison; the Psalm-146 duel;
Benjamin's ten sons as a ten-name memorial of the lost brother;
the two-years-for-two-words trust audit at the parashah's last
verse; and one idiom rendered three ways — "lift your head" as
take, remove, remember — the interpretation written into the
translation. The text gate found ZERO pre-existing defects — the
third defect-free sweep in a row. All gates green; four ledgers,
four rev-2 units. Genesis stands at 63 of 73 blocks read (Genesis
1:1-40:23 continuous, 1,196 of 1,533 verses — 78%); FIFTY-FIVE
blocks (gen_09 through gen_63) green and unstamped. Next sweep:
parashat Miketz, opening at gen_64 (Genesis 41:1 — Pharaoh's
dreams; the seam gen_63's ledger already names: the elevation
routed through the dream).

