# The Ten Words as the Program's Table of Contents — a tutorial

*Written 2026-09-16 at the owner's request ("I need a longform tutorial"), after chapter 4 of Deuteronomy was compiled. This is a
discussion document. Nothing in it is a ruling; the decisions it names at the end wait on the owner's word.*

---

## 1. Start with what the machine already is

Forget the ten commandments for a moment. Here is the machine as it stands today, in five sentences.

1. **The Bible is the program.** We read it in order, verse by verse, from Genesis 1:1. We are now at Deuteronomy 4:49.
2. **Narrative is everything except the code.** When a verse tells a story, the machine writes a line on a tape: "Isaac was born,"
   "the sea split," "Aaron died." Each line has a date from the text's own clock. The tape is now 3,523 lines long.
3. **Law is code.** When a verse gives a law, the machine writes a small function and installs it as a watcher on the tape. We call
   these watchers *daemons*. There are 64 of them. A daemon watches for the kind of event it governs and, when one appears, writes a
   verdict onto a ledger: this person owes that, this status is now in force, this debt is closed.
4. **The Mishnah is the answer sheet.** Each function is tested against the Mishnah's decided cases. A function that gets the
   Mishnah's answers is a compiled function. The Talmud is the teacher: when the bare verse leaves a gap, a recorded argument in the
   Talmud fills it, and we label the move.
5. **The Talmud's own accounting says how many functions there should be.** Makkot 23b: 613 commandments, 365 prohibitions, 248
   duties.

So today the code is a list of 64 functions. Each was installed by the verse that gave it. The list works. But it is a flat list.

## 2. The problem a flat list has

Ask the machine a simple question: *what does the program say about making images?*

Today the answer is: search the runners. Grep. Read. And when you do, you find something we only learned this week: nothing. The
second of the ten words, "you shall not make yourself a graven image," was never compiled as a function. The runner for Exodus 20
compiled the altar rules that follow the ten and the ten as a list of names, and no later chapter forced the point, until Deuteronomy 4
restated the image law with its full list of forbidden forms (figure, male, female, beast, bird, creeping thing, fish, sun, moon, stars).
Only then did the hole show.

That is the flat list's problem. It cannot tell you what is missing, because it has no idea what the complete set looks like. It knows
what it has. It does not know what it should have.

A table of contents fixes that. A book with a table of contents can be checked for missing chapters. The ten words are the table of
contents the text itself gives.

## 3. What the text says about the ten

The ten words are not one law among the laws. The text treats them differently from every other passage, and the difference is the
whole point.

- They are the only words God speaks to the whole people directly (Exodus 20:1; Deuteronomy 4:12, "you heard the voice of words").
- They are the only laws written by God's own hand, on stone (Exodus 31:18).
- They have a life story. Spoken at Sinai on the seventh of Sivan. Written on two tablets forty days later, on the seventeenth of
  Tammuz. Broken that same day (Exodus 32:19). Rewritten on a second pair (Exodus 34:1, 34:28). Placed inside the ark (Exodus 40:20;
  Deuteronomy 10:5). Restated by Moses forty years later, word for word with a handful of changes (Deuteronomy 5). Then the whole book
  of the law is placed beside the ark (Deuteronomy 31:26) and read aloud to the people every seventh year (Deuteronomy 31:10-13).
- The tradition says all 613 commandments are contained in them. Rashi on Exodus 24:12, quoting Saadia Gaon, says exactly this, and
  Saadia wrote out the table: every one of the 613 filed under one of the ten.

Read that as a programmer. The ten are the program's ten top-level sections. The 613 are the functions, and the tradition kept the
table that says which function lives in which section. The tablets are the source file: written, corrupted, rewritten, stored, archived
beside the running copy, and reread on a schedule.

We already have the tape line for "spoken at Sinai." It was the one line missing from the tape until chapter 4's compile put it there,
dated the seventh of Sivan, and the tablets' line beside it, dated the seventeenth of Tammuz. The machine can now point at the day the
table of contents came into force.

## 4. What the schema is, concretely

The schema is one table with ten rows. Each row is a section of the program. A row holds:

| column | what goes in it | where it comes from |
|---|---|---|
| the header | the commandment's name and its verse in Exodus 20 | the ink |
| the second copy | the same commandment's verse in Deuteronomy 5 | the ink |
| the parameter table | the data the section's functions read | the ink (chapter 4's list of forbidden forms is the second word's) |
| the functions | the daemons filed under this header | the tradition's table (Saadia, Rashi), as data with its source |
| the expected count | how many of the 613 the tradition files here | the tradition's table |
| the tests | the Mishnah rows that grade this section | the exam dockets we already keep |
| the install date | the tape line that brought the section into force | the tape (the seventh of Sivan) |

In files, that is: one registry (a yaml file with ten rows), one new field on every daemon (`header:` naming its section), and one gate
that checks every daemon has a header and every header's count against what is compiled.

Nothing else changes. No verdict moves. No function is added or removed. That last point is itself a law in the text: Deuteronomy 4:2,
"you shall not add to the word, nor take from it." Chapter 4's compile turned that verse into a function this week, and the Talmud's
cases for it (the priest who adds a fourth blessing, the elder who adds a fifth compartment to the tefillin) are all attempts to add a
function to the program without a teacher. The schema does not add functions. It indexes them.

## 5. A worked example: the second word

Take the row for the second commandment and walk it.

- **Header:** "You shall not make yourself a graven image" (Exodus 20:4).
- **Second copy:** Deuteronomy 5:8, the same words.
- **Parameter table:** Deuteronomy 4:16-19's list of forms. Chapter 4's compile already stored this as a data row. It sits in the runner
  as data, not as code, exactly because the code it belongs to does not exist yet.
- **Functions:** what should be here, by the tradition's table, is the image law itself and its neighbors (no idols, no bowing, no
  serving). What is here today: nothing.
- **Expected count vs compiled:** some vs zero.
- **Tests:** the docket already holds them. Mishnah Avodah Zarah 3:1-3 (which statues are forbidden), Rosh Hashanah 24a-24b (Rabban
  Gamliel's pictures of the moon, used to examine witnesses: are teaching instruments images?).
- **Install date:** the seventh of Sivan, the tape's line for the ten words.

With the schema in place, this row would have read "compiled 0 of N" from the day the registry was written. That is the difference
between a list and a table of contents. The list is silent about what it lacks. The table names it.

## 6. What the schema buys at chapter 5, where we are going next

Deuteronomy 5 is the second copy of the ten. Moses restates them, and the restatement differs from Exodus 20 in known places: "remember
the Sabbath" becomes "keep the Sabbath"; the Sabbath's reason changes from the creation to the exodus; "as the LORD your God commanded
you" appears twice; the order of the coveting changes and "his field" is added.

At chapters 1 through 4 we built the readback: a retelling is graded against the tape's own line, row by row, and the grade is
VERBATIM, TURNED, SHORTENED, EXPANDED, SUPPLIED or DISAGREES. That was narrative graded against narrative: Moses' account of the spies
against the spies' chapter.

Chapter 5 is the first time code is graded against code. Each of the ten in Deuteronomy 5 is graded against its header row in the
schema. The schema is what makes that possible: without it, "which earlier law is this a copy of" is a guess each time. With it, the
row says. And the tradition's own commentary on each difference ("remember" and "keep" said in one utterance; the exodus as the second
reason) becomes the test data for the grade, the same way the Mishnah is test data for a verdict.

The same mechanism then runs through chapters 12 to 26, the law code of Deuteronomy. Each law there either has an earlier seat under
its header (a restatement, graded) or has none (new code, and the schema says so, rather than us deciding it).

## 7. What the schema buys for installation

The loop has an open question called installation: does a law exist from the beginning of the world, or from the moment its verse is
given? We built the mechanism (each daemon has an `installed_by`) and left the setting open. Most daemons say "boot."

The schema gives the installation a shape the text supports. The ten sections come into force at Sinai, on the tape's line for the
seventh of Sivan. Each function under a section comes into force at its own verse, most of them later (Exodus 21's ordinances a chapter
after the ten; Leviticus's laws a book after). Before Sinai, only the pre-Sinai laws run. That is a two-level install: the section at
Sinai, the function at its verse. The decalogue daemon's `installed_by` can point at the tape's own line now that the line exists.

## 8. What the schema buys for you, looking at it

The board and the ask tool can show the program as a program: pick a section, see its functions, see each function's effects on the
ledger, see the Mishnah rows that grade it, see the install date. Ten rows on the left, the rest unfolding to the right. Today the
board shows the tape and the ledger; it cannot show the law as a whole because the law has no whole to show.

## 9. What it does not do

- It does not make any verdict different.
- It does not add a law. Deuteronomy 4:2 forbids exactly that, and the machine's link review law is the same rule in our own words: no
  link of our own unless a teacher taught it.
- It does not decide anything about the text. It records the tradition's own table and measures our code against it.

## 10. The one decision it needs first

The table that files each function under a header comes from the tradition (Saadia's list, Rashi's note on Exodus 24:12). Our link law
says a connection between two passages is either a REFERENCE (the text itself names it), a TRANSFER (a teacher taught it, and we cite
the teacher), or a HYPOTHESIS (ours, and labeled as ours).

Filing "you shall not steal" under the eighth word is a reference: the words are the same. Filing the laws of weights and measures under
the eighth word is a transfer: Saadia taught it, and the row must cite him. The decision is whether the registry requires a citation on
every row (the strict reading of the link law) or lets the plain cases stand as references and cites the teacher only where the header
is not named in the function's own verse.

That is the first thing to rule on, because it sets what the registry's rows look like before any are written.

## 11. What the sitting would build, in order

1. The registry: ten rows, the columns above, every non-obvious filing cited to its teacher.
2. The `header:` field on all 64 daemons, and the gate that refuses a daemon without one.
3. The coverage line in the gate's print: for each of the ten, the tradition's count against the compiled count, the holes named.
4. The decalogue daemon's install pointed at the tape's line for the seventh of Sivan.
5. Chapter 5's reading and compile on the readback's law form: each of the ten graded against its header row.

The second word's function is not on this list. It is a debt of its own, filed in COMPILE_DEBT, and the schema is what will keep it
from being forgotten.

---

*Related: THE_LOOP.md (the tape, the daemons, installation, the readback), DEUTERONOMY_WALK.md "Sitting 2b" (the tape's hole and the
second word's debt), COMPILE_DEBT.md (the owed items), MOVE_CATALOG.md (the labeled moves), the state doc's #185 addendum 1 (where the
schema question was first put on the table).*
