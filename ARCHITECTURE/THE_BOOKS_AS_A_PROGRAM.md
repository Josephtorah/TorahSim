# The Books as a Program — what each book does, measured

*Written 2026-09-18 by the main thread from its discussion with the owner between 2026-09-15 and 2026-09-18, on his word: "this whole
observation needs to be recorded in architecture." A discussion document: nothing in it is a ruling, nothing in it was compiled, and
every number in it was read off the Tanakh database (Data/tanakh.sqlite) or the local shelf by a script; the scans are reproducible from
logic/oral_triage/ezek_prelude_2026-09-15.md and the commands quoted below. Its companion is
[THE_TEN_AS_A_SCHEMA.md](THE_TEN_AS_A_SCHEMA.md), the walk thread's tutorial on the Decalogue finding, written 2026-09-16; that file
is not moved or changed by this one.*

---

## 1. The two principles (the owner's words, 2026-09-15)

**"Law is code. Let's keep that in mind."** A legal passage in any book is a procedure to compile, never a description to summarize.
The prophets' rules included. A later book's rule is a spec with its own constants, to be run and diverge-checked against the Torah's,
as the tradition did for Ezekiel (Shabbat 13b, the three hundred barrels of oil; Menachot 45a, "Elijah will interpret").

**"Law is code and narrative is data, variables, and whatever else it does."** On the machine as built, "whatever else" is a fixed
list. Narrative is the tape's event stream (data). Its numbers are the variables the code reads (the census counts, the spoil's halves,
the ages, the dates). Its date stamps are the clock's markers, the only thing that moves time. Its acts are the calls that fire the code
(Deuteronomy 24:16 does nothing until Amaziah acts) and the switches that install it (the erection, the investiture, entering the land).
Its receipt formulas are the closes ("as the LORD commanded Moses"; "you have kept all that Moses commanded you"). The one reverse flow
is the tent: a case with no standing law produces a rule in its own name (the blasphemer, the second Passover, the wood-gatherer, the
daughters of Zelophehad).

---

## 2. The map of the books by function

| Book | Function on the machine | The measured signature |
|---|---|---|
| Genesis to Numbers | The spec and the laws, and the first run of both | 57 runners, 62 daemons at Numbers' close; "the LORD spoke to Moses" 45 times in Numbers |
| Deuteronomy | The release: the program read back, finalized, written, deposited, the installer named, the install script attached | "the LORD spoke to Moses" once; the book written and put beside the ark (31:9, 24-26); Joshua charged (3:28; 31:7, 23); the stones and the altar on Ebal ordered "when you cross" (27:2-8) |
| Joshua | The install: the acts that switch the Torah's laws on, executed end to end with receipts and a grade | the receipt formula changes to "as Moses commanded" (6 seats; 0 in Numbers and Deuteronomy); "written in the book of the law" at 8:31, 8:34, 23:6; the audit chain at 11:15; the grade at 21:45 and 23:14; the lot in 24 verses, inheritance in 43; Joshua writes into the book at 24:26 |
| Judges | The main loop run without the operator, with two installations pending | the pattern stated at 2:11-19 before any instance; "did evil in the eyes of the LORD" 3:12, 4:1, 10:6, 13:1; "the land had rest" 3:11, 3:30, 5:31, 8:28 and never after Gideon; the refrain quotes Deuteronomy 12:8 by phrase |
| The Prophets and the Writings | The event stream: each case reaching the one function that was waiting for it | Jephthah's vow (Numbers 30, Leviticus 27); Ruth (Leviticus 25, Deuteronomy 25); Hannah and Samson (Numbers 6, 30); Naboth (false witness, inheritance); Amaziah (Deuteronomy 24:16, quoted word for word at 2 Kings 14:6, a phrase at three seats in the Bible) |
| Ezekiel | A second spec written against the first, with a run in front of it | chapters 1-39 a run (fourteen dates; "you shall know that I am the LORD" 58, the prophets' receipt); chapters 40-48 a spec (343 number words against 120 in the rest; a unit defined at 40:5; constants at 45:9-12) |

The machine's own rule already says the same in fewer words: the Torah demonstrates by spec, the Prophets and Writings by run.

---

## 3. Deuteronomy is not the install; it is the release

The question was put in the walk's thread ("is Deuteronomy the install?") and answered no there. The reason, on the numbers: the
giving voice is nearly silent in Deuteronomy, and what the book does is read the program back (the walk's own third pass, the readback),
write it down, deposit it, name the successor and hand him the first-run instructions. A program shipped with its installer named and
its install script attached is a release. The install is the next book.

---

## 4. Joshua is the install

**The acts that switch laws on are Joshua's.** In the machine's vocabulary a law is spoken in one place (given_at) and switched on by an
act (installed_by). The acts: crossing the Jordan; circumcision at Gilgal and the first Passover in the land (chapter 5, the receipt for
Exodus 12's "when you come into the land"); the manna ceasing when the produce is eaten (5:12); the altar of whole stones and the stones
written "as it is written in the book of the law of Moses" (8:30-35, Deuteronomy 27's script run); the division by lot, which arms the
sabbatical count (Arakhin 12b: the count begins after seven years of conquest and seven of division); the refuge cities set apart "of
which I spoke by Moses" (chapter 20); the Levite cities given (21); the tent set up at Shiloh (18:1).

**The audit trail changes form.** Joshua's receipts cite the written book and Moses, not the voice. 11:15 is the audit line whole: "as
the LORD commanded Moses his servant, so Moses commanded Joshua, and so Joshua did; he left nothing undone of all that the LORD
commanded Moses." Spec, relay, execution, completeness. The grade follows at 21:45 and again at 23:14: "not one word fell of all the
good the LORD had spoken; all came to pass."

**Its output is a table.** The allocation: the lot and the inheritance, the land register Numbers 34 declared as a schema, now filled.
And at 24:26 Joshua writes into the book of the law: the first append to the journal by a hand other than Moses'.

**What fires and what stays silent.** Joshua does not call every law; a program runs by events reaching the functions whose triggers
they match, and Joshua's events are entry, war and allocation. Measured by distinctive three-word phrases (six seats or fewer in the
Tanakh) recurring in Joshua, the land laws dominate: the borders of Numbers 34 (35 phrases), the refuge law (28), the second census (21),
Gad and Reuben's condition (21), the daughters of Zelophehad (20). Eight compiled law spans have no distinctive phrase in Joshua at all:
the offering calendar, the vows chapter, the second block of Exodus 21, the guardians, the offerings, the eighth day, the clocks, the
second holiness block. Purity, damages, the courts' procedures and the priestly service are installed, in force, and silent. If Joshua
ran as a tape, the watch coverage line would print those daemons as seen many, fired none: the zero-report law working as designed.
By seat, the laws that do fire: the ban (Deuteronomy 7 and 20) at Jericho, Ai and 10:40; Achan under Deuteronomy 13 and the devoted thing
(7:25); the hanged body taken down by sunset, Deuteronomy 21:23, at 8:29 and 10:27; the Gibeonites' oath binding even under fraud, the
vow law's one run (9:18-20); Caleb's grant (14:6-15); the Levites' no inheritance (13:14, 33; 14:3-4; 18:7); Zelophehad's daughters
receiving their portion "as the LORD commanded" (17:4, the Tent's own case closed a book later); Gad and Reuben released (22:4); the one
altar of Deuteronomy 12 adjudicated as a case (22:10-34, Phinehas, the altar declared a witness); Joseph's bones (24:32).

**So how does the entire program run?** In two senses, and Joshua supplies only the first. The install: entering the land flips the
condition every "when you come into the land" law was waiting on, so after Joshua every law is live; 11:15 and 21:45 assert completeness
for what was commanded for this run, the conquest and the division, not for every law. The runtime: the events that fire the remaining
laws come one at a time in the books after.

---

## 5. Judges is the main loop without the operator

**The loop is written out before any instance.** Judges 2:11-19: they did evil, the LORD sold them into the hand of spoilers, they
cried, He raised a judge, the land had rest, the judge died, they returned "and corrupted more than their fathers." The last clause is
the accumulator: each pass ends worse than it began. Then the pattern runs: "did evil in the eyes of the LORD" at 3:12, 4:1, 10:6, 13:1;
"sold them into the hand" at 2:14, 3:8, 10:7; "the land had rest" at 3:11, 3:30, 5:31, 8:28. After Gideon there is no rest line at all:
Abimelech, Jephthah and Samson run with the loop still turning and the recovery gone. The degradation is measurable in the formula's
disappearance.

**The loop is a Torah daemon firing.** "I will deliver you into the hand of your enemies" is Leviticus 26 and Deuteronomy 28. Judges is
the first run of the covenant's curse-and-return law, cycle by cycle, on idolatry events; the compiled tochacha runner is the code and
Judges is its event stream.

**The refrain names the missing installations.** "There was no king in Israel; every man did what was right in his own eyes" (17:6,
18:1, 21:25). The second half is Deuteronomy 12:8 word for word (the phrase "right in his eyes" stands in Deuteronomy at 12:8, 12:25,
12:28, 13:19, 21:9 and in Judges at 17:6, 21:25), the Torah's own description of the time before the rest and the chosen place. So the
refrain is a reference by phrase to two laws whose installing acts have not happened: the king of Deuteronomy 17, waiting on "when you
come in and say, I will set a king," and the one place of Deuteronomy 12, with Shiloh standing in. In the machine's field both are
installed_by pending, and Judges is the book that keeps saying so.

**Its years are a timer chain with a checkpoint.** Oppressions of eight, eighteen, twenty, seven and forty years; rests of forty, eighty,
forty and forty; the judges' terms (twenty-three, twenty-two, six, seven, ten, eight, twenty). 1 Kings 6:1 declares four hundred and
eighty years from the exodus to the temple. Summed naively, Judges plus the wilderness, Joshua, Eli, Samuel, Saul and David overrun it,
and the tradition reconciles by overlapping the oppressions with the terms (Seder Olam). That is a checkpoint of the kind the machine
already prints for the four hundred and thirty years: declared by the text, computed by the engine, a bound, with the shelf's
reconciliation as a data row.

**Its cases feed the laws Joshua left silent.** Jephthah's vow runs Numbers 30 and Leviticus 27 on the hardest input, and the tradition's
verdict is that he should have gone to Phinehas (the sage's release, a data row the vows runner already carries). Samson runs Numbers 6
as the Mishnah's own named type, the Samson nazirite (Nazir 1:2). Micah's hired Levite runs the Levite laws in breach. The oath at Mizpah
and the daughters of Shiloh run vows again. The war on Benjamin runs the city led astray against a whole tribe. Abimelech is a king with
no Deuteronomy 17 behind him.

---

## 6. The Decalogue is the schema, and how the pass missed it

The finding is written up as a tutorial in [THE_TEN_AS_A_SCHEMA.md](THE_TEN_AS_A_SCHEMA.md); what follows is the record of how it was
found and why it was not found earlier.

**The tradition's answer.** Rashi on Exodus 24:12: all six hundred and thirteen commandments are included in the ten, and Rabbenu
Saadia's warnings file each under the utterance it depends on. The Mekhilta on the tablets: five on one tablet, five on the other,
paired across, "I am the LORD" opposite "you shall not murder." And Makkot 23b:18 to 24a:3 and onward, the seat that would have caught
it: Rabbi Simlai's 613 (365 prohibitions as the days of the solar year, 248 commands as the limbs), Rav Hamnuna's arithmetic at 24a:1
(the word "Torah" counts 611, plus "I am" and "you shall have no other" heard from the Almighty), then David on eleven, Isaiah on six,
Micah on three, Isaiah on two, Habakkuk on one: five outlines over one list, each with fewer headers than the last.

**What the machine shows.** The two copies: Exodus 20:2-17 has 620 letters and 172 words on the database's division; Deuteronomy
5:6-21 has 708 and 189 (the Onkelos export divides chapter 5 into thirty verses against the database's thirty-three, so any count on that
passage must name its division). 620 is the received count the tradition ties to 613 plus the seven rabbinic laws. Thirteen "not"s in
sixteen verses, two positives: the ten are constraints and the codes are the procedures. The key from a header to its rows is topical,
not lexical: the sabbath's root recurs in twenty-one law verses, murder's in eighteen, witness in ten, theft in six, but image, the Name
in vain, honor, adultery and covet each recur once. So the dependency census, which works by shared words, can never demand the schema,
and every header-to-row tie is a transfer with a teacher, never a reference. The Tent's first two cases, the blasphemer and the
wood-gatherer, sit under headers three and four: constraints whose procedures did not yet exist.

**How the pass missed it.** The Decalogue was read on 2026-09-04 as "Exodus exam block 5 of 18," exam-first: fifteen law rows from the
Talmud's pages that judge the verse, and four cells compiled where the chapter's own ink carries a consequence (the vain name, the sabbath
clauses, theft as the kidnapper, the altar rules); the rest were left to the spans that carry their procedures. The Mekhilta's chapter on
the tablets was never opened, because Exodus 20 was never read spine-by-position the way Numbers was read on the Sifrei. Rashi is off by
default on the core shelf. Makkot 24a:1 and Horayot 8a:21 stand in the Exodus triage ledger as credits, "standing verdict in a prior
ledger": the credit guard passed them as verdicts and their structure was never read. Makkot 24a:30 was read on 2026-09-14 for the
fathers-and-children illustration with 23b:18 unread twenty-nine segments above it, because the cell being served asked about Ezekiel.
The mechanism: a seat is read for the question the cell asks and graded by the docket's classes (law, derivation, dispute, context); a
passage about the list itself is none of those for any cell, so it falls through, and the credit guard keeps it shut. The compiler law
compiles spans; a structure across every span has no span, so no sitting was ever owed it. The one pass that looks for structure, the
register gate, was built at Numbers 26 and looks for headers, footers, checksums and receipts, not for a schema.

**The Talmud's example gives more than a mapping.** Five outlines over one list, from ten headers down to one, and a count with its own
arithmetic. That is a data row of the kind the machine already keeps for disputes: the list, the count, the outlines as settings, each
with its teacher named.

---

## 7. Ezekiel, scanned before its walk

The full note is logic/oral_triage/ezek_prelude_2026-09-15.md, with the scans at its end. In brief: two books in one, a run (1-39) and a
spec (40-48). "A day for a year" as one four-word phrase stands at exactly two seats in the Bible, Numbers 14:34 and Ezekiel 4:6; the
Torah compresses forty days into years, Ezekiel decompresses 390 and 40 days into years, in the same words. The gates of chapter 40 are
stored once and referenced six times ("according to these measures"); the visions after chapter 1 are pointers ("like the vision which
I saw"). Chapter 18 is a function called over three generations with a base case, called again at 3:17-21 and in chapter 33; chapter 20
runs one cycle three times over the nation and ends with a filter (20:37-38, "pass under the rod"). The spec re-instantiates records inside
the Torah with new constants, not the Torah whole: 40-43 share 40 of 136 rare words with the tabernacle spec and 42 appear nowhere in the
Torah; 45:9-12 declares its constants before the schedule; 40:5 defines its unit; 46:17 calls Leviticus 25's "year of liberty" by name.
The ledger in the ink: 24:2 orders a marker written; 33:21 closes it; 29:18-20 reassigns an unpaid debt (Tyre's wages paid in Egypt).
The tent form at three seats: 14:1-8, 18:2, 44:1-3. The river of 47:1-12, four measured thousands with one rising depth until "waters to
swim in," then "he brought me back to the bank": the owner's reading, the data leaving the code until the reader cannot wade it and the
seeing done from the bank (the board and the database over the ledger); the shelf read the depths as a scale of crossing before us
(Yoma 77b:12-15; Sanhedrin 100a:6). If run, Ezekiel's output is the Torah's own tables re-instantiated for a prince, and the divergences
from the first spec are the list the tradition handed to Elijah.

---

## 8. What this would change in the build (proposals; none ruled)

1. **A header on every law.** A registry row per commandment naming the law spans and cells filed under it, taught by Saadia, the
   Mekhilta and Makkot, never inferred; a `header:` field on every daemon; a gate refusing a compiled law with no header; the count
   613 = 365 + 248 and the five outlines (10, 11, 6, 3, 2, 1) as a data row with its settings; the tablets' pairing as the join. The
   decisions are listed in THE_TEN_AS_A_SCHEMA.md and wait on the owner's word, seated at Deuteronomy 5.
2. **A docket class for structure.** A passage about the list itself (Makkot 23b-24a; Berakhot 12a on the ten read daily in the Temple
   and abolished outside it; Shevuot 20b and Rosh Hashanah 27a on "remember and keep in one utterance") is read as structure, never
   credited as a verdict; the credit guard does not apply to it.
3. **Exodus 20 read spine-by-position** on the Mekhilta, the tablets' chapter included, with Rashi at 24:12 pulled in by the pointer.
4. **The pending installations printed per book.** Judges' refrain is the text saying which daemons' institutions do not stand; the
   installation report already counts pending; a per-book line would show the king and the place pending through Judges and Samuel.
5. **The receipt census gains the later books' forms.** "As Moses commanded" (Joshua), "you shall know that I am the LORD" (Ezekiel), and
   the grade lines "not one word fell" (Joshua 21:45, 23:14) as receipt seat classes.
6. **The chronology checkpoint at 1 Kings 6:1.** The four hundred and eighty years declared, the sum of the recorded periods computed
   as a bound, Seder Olam's overlaps as the data row, printed MATCH or DIVERGE like the four hundred and thirty.
7. **The Prophets by run.** Each case in the later books submitted through the port as an event to the world, so that Jephthah's vow
   fires the vows daemon and Amaziah's verdict fires Deuteronomy 24:16, with the watch coverage naming what never fires.

---

## 9. Where the measurements live

The Ezekiel scans: logic/oral_triage/ezek_prelude_2026-09-15.md (section 7 reproduces them). The Decalogue counts and the Joshua and
Judges formula counts were run 2026-09-16 to 18 in the main thread against Data/tanakh.sqlite with the same method: a verse's lemma
sequence read off the `words` table, a phrase's seats counted as the verses in which its lemmas stand adjacent, rare set at six seats
or fewer for three-word phrases and thirty for pairs; the shelf searched in Data/bavli_<tractate>_he.json with the vowel points stripped.
The illustration pages built from the same method stand in grok-mockups/illustrations (never committed) with their generator.
