# Roadmap — the simulation direction

The instrument so far is a **judge**: you bring it a case, it rules
(step 7 of `PROCESS_OVERVIEW.md`). The next stage turns the same laws into
**physics**: a world where every event passes through every law
automatically, where liability persists as state across years and
generations, and where the computed consequences can be checked against
what the narrative itself reports.

## The purpose (owner ruling 2026-08-25 — the missing why, now ruled)

Owner verbatim: **"we will use the talmud as our source of truth."**
Ruled after a four-purposes discussion (prove the law computable / a
concordance of state / run the tradition's own hypotheticals / the
canon's open-demand queue): the MISSION is the third — **run the
tradition's own hypotheticals**. The Talmud's case-discussions (each
sugya — a Talmudic case-discussion) pose cases AND record their
answers; those recorded answers are the ORACLE — the expected outputs
the simulator's computed verdicts are tested against.

Precision, so "truth" stays honest: the STONE (derived logic) remains
the machine's program — the only truth about what the verses say. The
Talmud's recorded answers are the GROUND TRUTH FOR TESTING — what the
machine's outputs are measured against. Two different jobs for the
word, both kept.

What the ruling buys: (a) computability is PROVEN as this mission's
passing grade — a verdict without an oracle proves nothing; (b) the
state concordance gets BUILT as its substrate; (c) the hypotheticals
are INTEGRATION TESTS — "the ox gored on the Sabbath" needs two laws
loaded in one world; single-unit derivation never exercises law-on-law
interaction; (d) DISAGREEMENT IS THE PRODUCT — a machine-vs-sugya
mismatch means either a missed claim (→ a specific reading target) or
an input not in the written verses (→ a documented Oral Torah
finding); the flywheel: read → derive → run the sugya → mismatch →
told what to read next; (e) DISPUTES ARE RUNTIME OUTPUTS — a machloket
(recorded dispute) returns two rulings with attribution, and teiku
("let it stand" — the Talmud's own unresolved) returns unresolved; a
single-answer machine would be wrong about the Talmud; (f) underived
law blocks a case honestly — the sketch tier stands in, labeled, and
blocked cases RANK the next derivation targets.

Follow-on, queued not designed: the sugya CASE FILE (inputs + the
tradition's recorded answer + citation) as a first-class runnable
artifact that reading passes collect. THE_STEPS stays untouched until
that design is ruled.

## The oracle's anatomy — how the Mishnah fits (owner, 2026-08-25)

The owner's words on this insight: "this is the greatest insights of
this entire project." "Talmud as source of truth" contains the Mishnah
automatically — the Talmud physically IS Mishnah paragraphs plus the
discussion around them. The two layers do different jobs, and the
split is the one THE_STEPS Step 4 already teaches (a Mishnah paragraph
is a RULING — input→output, no reason shown; a Talmud passage is a
DERIVATION, DISPUTE, or TEST):

**The Mishnah is the verdict table.** Each paragraph is a test
fixture: declared inputs, expected output, derivation stripped. Six
orders, 63 tractates of settled cases — organized BY SUBSYSTEM, not
narrative: Seeds (agricultural law), Festival (the calendar — the
world clock's own test suite), Women (marriage law), Damages (torts),
Holy Things (the sanctuary), Purities. The Torah is source code in
narrative order; the Mishnah is the API organized by module — it hands
the simulator its MODULE MAP. The routing table already exists:
`logic/MISHNAH_TOPICS.md`, all 525 chapters topic-labeled.

**The Gemara is everything around the table** — three jobs:
(1) TRACEABILITY — menalan ("from where do we know this?") hooks each
Mishnah row to its verses: WHICH STONE EACH TEST EXERCISES; a failing
case's own gemara points at the verse span to derive next — the
tradition wrote the traceability matrix for us; (2) EDGE CASES — the
hypotheticals probe each row's boundaries: the generated edge tests
around each core fixture; (3) DISPUTE FLAGS — contested / resolved /
teiku ("let it stand"): the metadata telling the oracle to expect one
output, two attributed outputs, or unresolved.

Consequences, standing: case files anchor on the MISHNAH ROW (the
gemara supplies the verse hooks = which units must be loaded, the
hypothetical variants, the dispute status); a Mishnah row WITHOUT
gemara still stands — a black-box test (the gemara turns black-box
into glass-box); the Mishnah's internal disputes (the houses of Hillel
and Shammai) are DUAL EXPECTED OUTPUTS; Tosefta (the supplement
collection) rows are VARIANT oracle rows, dual-tracked. Precedent
proven in-house: the Exodus 21 machine's 64 scenes leaned on Mishnah
Bava Kamma's ox taxonomy; its standing-verdict mechanics rode Mishnah
Keritot 6:2.

One breath: Mishnah = the expected-output table, organized by module.
Gemara = the traceability, the edge cases, and the dispute flags.
Talmud = both — which is why the purpose ruling names the whole.

### How the books are used (owner's word in the canon window, 2026-08-25)

The shapes of the two books say how they were meant to be read, and
the project follows the same grain.

**The Mishnah is a practitioner's reference, not a reading book.** Its
users were judges and teachers who needed the law of a domain, now —
an ox case routes to Damages, a sabbatical question to Seeds, a
wedding to Women. That is why it stands in subject order, why its rows
are terse (input → output, reasons stripped), and why it almost never
quotes a verse: it PRESUMES the Torah known and hands the operator the
settled law, arranged for memorization and retrieval. The deployed
system's manual, organized by module, written for operators — not for
the compiler.

**Two runs, not one.** BUILDING runs in Torah order — the walk from
Genesis 1:1 — because state accumulates: creation installs the world,
covenants install standing rules, Sinai switches the law on; "the ox
that gores" cannot load into a world that does not yet exist. USING
runs in subject order — a case never replays Genesis; it routes to the
module, and the Mishnah IS the routing. The simulator needs both at
once: the narrative-order world and the subject-order verdict table.

**The verse hook is asked, not printed.** The Mishnah row does not
name its verse; the Gemara's signature move is exactly that question —
menalan ("from where do we know this?") — answered with a verse and
its derivation chain, row by row: the tradition wrote its own
traceability matrix. Where the Gemara is silent, the midrash halakha
collections (verse-ordered legal exposition: Mekhilta on Exodus, Sifra
on Leviticus, Sifrei on Numbers and Deuteronomy) hold the SAME law
body in SOURCE order — the transposed matrix. Mishnah = law by module;
midrash halakha = law by verse; together they are the join in both
directions, and the verse-ordered side is the natural future reverse
map beside `logic/MISHNAH_TOPICS.md`'s topic map.

**The gaps are data.** Sometimes the hookup is contested — two sages
propose two source verses, and the derivation itself is a machloket
(recorded dispute). Sometimes the Gemara rejects every proposed verse
and the rule stands on received tradition — halakha le-Moshe mi-Sinai
("a law to Moses from Sinai") — or on rabbinic decree, de-rabbanan
("from the rabbis"). Those are the purpose ruling's category (d) made
concrete: an input not in the written verses, a documented Oral Torah
finding, never a failure. A row whose gemara gives no hook stays a
black-box test; the row stands.

**The pipeline the books themselves suggest:** route by topic
(`logic/MISHNAH_TOPICS.md`, built) → read the Mishnah rows as fixtures
→ read each row's gemara for the verse hooks (which units must load),
the edge-case variants, and the dispute flag. Done once by hand
already: the Exodus 21 machine's 64 scenes were graded against Mishnah
Bava Kamma's ox taxonomy.

### The two shelves, and the measured bridge (owner rulings 2026-08-27)

The library split became law: books divide by WHICH END OF THE BRIDGE
they start from. The READING SHELF is the verse-anchored books —
Onkelos and the midrash collections, the law-midrash included —
organized like our units; they feed Steps 3–4. The TESTING SHELF is
the case-anchored books — the Mishnah, the Tosefta beside it — which
start from the case, barely cite verses, and cannot be read at a
verse span; their rows are the Step 9 exam, routed by topic. The
TALMUD IS THE BRIDGE, walking a Mishnah rule back to its verse. The
register now carries the split as a `shelf:` field on every rule
(reading 41 / testing 38 / bridge 26), orthogonal to chain status,
with the owner's Sifrei-on-Numbers row added the same day.

And the bridge was MEASURED, on the project's deepest block — the
goring ox, 35 witnessed claims (the workshop's expansion test,
2026-08-27): 22 of 35 walk back to the verse's own ink or an argued
analogy; exactly two are additions whose derivation never compiles —
and the tradition labels both itself as decrees. The owner-stamped
sharpening: even those two carry verse ANCHORS (the pit's exclusions
read off the verse's own named animals; the 4-and-5 tariff's numbers
sit in the verse, with the cross-verse double found inside it) — so
the decree tier splits anchored-without-compiled-reason from
no-hook-at-all, and on this block the no-hook class is EMPTY. The
sharpened finding, one breath: every claim has a verse anchor; only
REASONS ever fail to compile. The Mishnah writes as if it is adding;
the Talmud shows most of it was derived; the true remainder arrives
self-labeled.

The spine default follows from all of it (Step 3; the table lives in
`logic/CORE_SHELF.md`): one verse-anchored spine per Torah book plus
Onkelos; the Mishnah and Talmud leave the reading pass and return as
the exam. Retro-tested against the 18 finished sweep ledgers before
adoption: ~94% of the 451 fresh material findings return through the
plan's own channels; the honest remainder is marked and recoverable
by depth order. Effective at parashat Vayera. DEPENDENCY ON RECORD:
the sugya case-file machinery must be designed and proven — on the
Exodus 21 material in hand — during the Genesis remainder, before the
walk reaches Exodus's law spans; the thin-reading deal is "the exam
tests it," so the exam must be real by then. Design inputs already
banked in the workshop: the tier field and tier-profiled verdicts
from the coded expansion run, the hook-not-fence discovery rule with
its no-cantillation caution, and the doubt layer (Mishnah Bava Kamma
— the First Gate — 5:1, verdict under uncertainty) as the first
missing subsystem.

*(Both sections ruled in the workshop window 2026-08-25 and mirrored
here on the owner's order — "mirror the purpose and anatomy to
torahsim"; the workshop's THE_WORLD.md holds its own copy under "The
goal." This document is their canon home.)*

## The prototype that exists

`sim/house_of_david.py` — run it (`python3 sim/house_of_david.py`). It
loads the real Exodus 21 machines, registers three laws as physics
(homicide, the theft tariff, collection), and folds the recorded events
of the house of David through them: the taking of Bathsheba as the ewe of
Nathan's parable, the killing of Uriah, the four discharges, Joab's
murders, Solomon's execution of Joab.

Its first run surfaced two findings, both kept in the file's header:

1. **The correct ledger ends OPEN.** After the fourfold discharges,
   David's Heaven-debt stands at 1 — and that is right, not a bug: the
   four answer the *ewe*; the open 1 is the blood of Uriah, which the
   text never closes ("the sword shall never depart from your house").
   The naive balance check expected zero; the doctrine says one. Lesson:
   validation must encode doctrine, not arithmetic.
2. **A live dispute surfaced by itself.** Joab's blood-debts sit on
   Heaven's docket; the coded execution clears only the court docket —
   which is exactly the recorded dispute between the Vilna Gaon and the
   Netziv on whether the crown collects Heaven's ledger (Solomon's own
   words: "the LORD shall RETURN his blood"). The simulation reproduced
   a centuries-old machloket ("division," a recorded dispute) as a
   design decision, uninvited.

## The nine components of the full simulation

The design of record. Each names what exists and what is missing.

1. **The clock and the era table.** World-time with named eras; laws gate
   on era (before Sinai, only the Genesis 9 blood-charter physics
   operates). Exists: chronology keys on the catalog scenes. Missing:
   the era table as a first-class object.

2. **Entities with persistent identity.** People, **houses** (debts
   attach to houses across generations — David's, Saul's, Ahab's),
   animals with legal state (the תם/מועד, "innocent/forewarned," ox),
   property, places. Missing: the house-lineage layer.

3. **The ledgers — liability as state.** The court docket, Heaven's
   docket, ownership, slave-term clocks, standing verdicts, covenant
   states (the broken release-covenant of Jeremiah 34 as a breachable
   world object). The sketch's two dockets are the seed. This is the
   simulation's heart.

4. **The law layer — chapter machines as pluggable physics.** Every
   event passes through every registered law, unasked. Each further
   chapter derived under the method laws becomes a new physics module
   (the Leviticus 13 quarantine timers, the Leviticus 25 land
   schedulers, the Numbers 35 refuge system). Exists: one chapter of
   roughly ten planned. **The simulation and the derivation program are
   the same project** — deriving law *is* building the world.

5. **The jurisdiction router.** Every event routes to its forum: court
   (witnesses + warning + a seated court), crown, war, foreign, ban, or
   Heaven. The Tanakh run proved routing is load-bearing — several of
   its hardest cases were routing questions, not verdict questions.
   Missing: one explicit router all laws consult.

6. **Institutional state flips.** The law's own runtime flags change
   with narrative events: refuge exists only after the conquest;
   Shiloh's asylum lapses; the Temple turns capital jurisdiction on; the
   high court's exile from its chamber turns it off; the jubilee
   stopping puts the Hebrew-slave module to sleep (the machines already
   carry the flag). Same act, different century — lawfully different
   process.

7. **The prophet channel.** Prophets read Heaven's ledger aloud — Nathan
   announces exactly what the dockets already hold. As a component: an
   observer that reports open ledger state at narrative moments, and the
   validation it enables — does every prophetic indictment in the corpus
   match an open entry in the simulated ledger?

8. **The diff engine.** Computed state vs. declared state, sharpened by
   the sword-clause lesson above: balance checks must encode doctrine —
   a ledger that ends OPEN can be the correct ending.

9. **The validation harness and display.** The 64 scene stamps as a
   regression baseline (any simulation change that flips a CONFIRM must
   answer for it); the web app as the window; every surface glossed per
   method law 8.

## The fence

**No invented events — ever.** The simulation computes law over the
text's own events; it never generates history. A what-if sandbox may
exist someday, fenced and labeled, never mixed into the record. This is
method law 6, and it is what keeps the simulation an instrument of
verification rather than of fiction.
