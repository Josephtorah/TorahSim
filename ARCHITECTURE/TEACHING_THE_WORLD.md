# Teaching the World — the plan for the public explanation, with the examples that prove it

*Written 2026-09-21 by the main thread on the owner's word ("come up with a plan to teach the world about this architecture ... put it in a long form markdown and epub"), after reading a note from Grok on design recovery and the how-it-works report. A plan, not a ruling: nothing here changes the engine, and every step in section 11 opens on the owner's word. Every count is dated and its source is named in section 13.*

## 0. The recommendation in one paragraph

Lead with the thing that is demonstrated, not the thing that is believed. What is demonstrated is this: the law in the five books of Moses has been compiled, function by function, into code that runs on one simulated world, and the tradition's own worked cases (the Mishnah) grade that code. What is believed, and only believed, is that the text was built to be run. The public explanation must keep those two apart on every page, or readers who doubt the second will throw out the first. Teach it in this order: one picture; six worked examples, each generated from the running machine and each with the command that reproduces it; then the how-it-works report of the machine in the standard form (arc42 with C4 pictures); then the design-recovery report of the text (what the text says it does against what it does when run, the gaps being the findings); then a page that says "run it yourself". Before any of it, fix the language: a vocabulary table and a jargon gate, so that no page uses a word of ours without its plain word beside it. The examples are the proof. The reports are the map. The vocabulary is what makes either readable.

## 1. The problem to solve

Two problems, and they compound.

The first is that the project speaks its own language. Tape, daemon, runner, cell, effect, ledger, marker, checkpoint, readback, freeze, docket, sitting, gate, sweep: each has a precise meaning inside the workshop and none outside it. A reader who meets "the daemon writes an effect on Israel's ledger at the counter's own day" has met five undefined words in one clause. The writing came out that way because it was written for the people doing the work, and the records had to be exact. The owner's diagnosis is right: the machine's voice talks as if everyone already knows. The public voice must not.

The second is that two claims of different strength travel together. "The law can be compiled and run as a simulation" is a claim about our machine, and it is proven the way software is proven: it runs, its tests pass, anyone can run it. "The Torah was meant to be a computer system" is a claim about the text's intent, and it is a hypothesis with evidence. When the two share a sentence, a reader who rejects the hypothesis rejects the demonstration with it, and a reader who accepts the demonstration may think the hypothesis is proven. Neither is what we want.

## 2. Two claims, kept apart

| | Claim A | Claim B |
|---|---|---|
| what it says | The law compiles and runs. | The text was designed to be run. |
| kind | a demonstration | a hypothesis |
| how a reader checks it | clone the repository, run the event list, run the tests | read the evidence and judge |
| what stands behind it | 67 compiled files of law, one event list of 1,327 lines, 7,007 graded cases, every automatic check green | the retellings graded against the record, the receipts inside the code, the ten words as a table of contents, the eras written as a table |
| where it lives now | the machine and its records | THE_BOOKS_AS_A_PROGRAM.md, THE_TEN_AS_A_SCHEMA.md, DATABASE_SPECULATION.md, the install hypothesis in the Deuteronomy map |
| its public headline | "We compiled the law, and it runs." | "The text may have been built to run. Here is what we found." |

The rule for every public page: Claim A is the headline, Claim B is a labeled chapter, and no sentence carries both.

## 3. What to take from Grok's note

The note names the standard family: design recovery (understand what a program does, how, and why), redocumentation (write the missing description), architecture recovery, program comprehension; the report standards IEEE 1016 and ISO 42010; the practical skeletons arc42 and C4. Most of it fits as written, some fits after a turn, and one part is the project's own twist.

What fits as written:

- The split between what the software is supposed to do and what it actually does. The note says tests are executable intent. In our case the Mishnah is exactly that: the tradition's own worked cases, written down as the answers a reader of the law should reach. We run them as tests, and 7,007 of them pass.
- The zoom rule: the system in its surroundings first, then the running parts, then the parts inside one of them, code only where an algorithm needs it. That is the C4 model, and section 7 draws our machine in it.
- The arc42 skeleton for the machine's report. Section 8 maps its twelve sections onto files we already keep.
- An evidence index and an open-questions list on top. We have both in raw form: the research log, the forms folders, the debt file, the proposals.
- Interpret, do not dump. The records dump by design; the public pages must not.

What fits after a turn:

- The note's method examines one software package. We have two: the machine we built, which is ordinary software and takes arc42 directly, and the text the machine runs, which is three thousand years old and whose design recovery is the whole project. So there are two reports, not one, and they must not be merged. Section 8 is the first, section 9 the second.
- "Interview the maintainer." There is none. The nearest thing is the commentary library: the Mishnah, the Talmud, the Targum and the Midrash, which is the tradition's own account of how the program is to be read. The Talmud's disputes are the issue tracker: each is a logged edge case with the arguments on both sides. We already read it that way; the public should hear it that way.
- "Dynamic analysis: run the primary scenarios and trace control and data flow." Our event list is that trace. The player plays it. The log keeps it.

The twist that is ours: in ordinary design recovery, the recovered design is a description. Here the recovered design runs, and the fifth book of the program (Deuteronomy) reads the running state back and is graded against it. No software report has that chapter. It is our strongest evidence and it gets its own example (number 4 in section 6).

## 4. The vocabulary rule

The fix for "talks as if everyone knows" is the fix the project already uses for Hebrew: nothing appears without its plain word beside it, and an automatic check refuses the page if it does.

### 4.1 The translation table

Every public document carries this table or links to it, uses the plain word in its prose, and gives the machine's word in parentheses the first time only.

| the machine's word | the plain word | what it means |
|---|---|---|
| the program | the Bible read as a program | the 24 books, read as instructions (law) and events (narrative) |
| law, code | a rule | a verse that tells someone what to do; compiled into a function |
| narrative, data | an event | a verse that tells what happened; it becomes one line in the event list |
| the tape | the event list | every event in the Bible's own order, one line each (1,327 lines today) |
| a line | an event | one entry in the event list |
| a runner | a compiled stretch of law | one program file holding the functions for one stretch of law (67 files) |
| a cell | a function | one question of the law and its answer, as code |
| a daemon | a law that is switched on | after its verse, it watches every event and writes on the accounts when an event matches |
| installed, given | switched on | a law switches on at the verse where it is given, or at the start |
| an effect | an entry | what a law writes on someone's account |
| a ledger | an account | the running record of one person, tribe, place, or the nation |
| an entity | an account holder | anyone or anything with an account (319 today) |
| a debit, a close | a debt and its payment | something owed, and the later event that pays it |
| a timer | a due date | an entry that comes due later and fires on its day |
| a marker | a date in the text | a place where the text gives a time; the calendar moves by it |
| the clock, the eras | the calendar | days counted from the text's own dates |
| a checkpoint | a count check | a number the text gives (a census) that the running world must match; MATCH or DIVERGE, never repaired |
| the readback | a retelling, graded | a later book retells an earlier event or law; the retelling is graded against the record |
| a freeze, a unit | a locked reading | one chapter's reading, locked and hashed (227 today) |
| the shelf | the commentary library | the local copy of the Mishnah, Talmud, Targum and Midrash |
| the docket | the reading list | the commentary passages read for one chapter |
| a sitting | a working session | one session on one chapter, either its reading or its compile |
| a gate | an automatic check | a test that refuses the work when a number does not match |
| the sweep | the full test run | every test of every compiled file, run again (7,007 cases) |
| the journal | the log | every event as it was written, chained by hash, in one database |
| the board | the player | a web page that plays the event list step by step |
| the port | the input door | how an outside input enters a copy of the world |
| reference, transfer, hypothesis | a named link, a taught link, a guessed link | the verse names its source; a teacher named the link; our own guess, labeled as such |
| the Mishnah as the answer sheet | the test cases | the tradition's worked cases; the compiled law must give their answers |
| the Talmud as the compile rules | the reading rules | the tradition's rules for how a law verse is read into a rule |

### 4.2 The jargon gate

Build a jargon lint on the pattern of the Hebrew gloss lint (logic/solo_tools/gloss_lint.py): a list of the machine's words; for each public document, every first use of a word must have its plain word in the same sentence, or the lint flags it. Run it on every public page before it goes out, with a baseline of zero. One small sitting, and it changes everything downstream, because the rule becomes mechanical instead of a matter of remembering.

### 4.3 The writing rules for public pages

1. A plain word beside every machine word at first use. The lint enforces it.
2. Every example is generated from the running machine, never typed from memory. The illustration pages taught this: four links typed from the English turned out to have no Hebrew under them, and the generator now refuses such a link. A public example a scholar can falsify is worse than none.
3. Every number has its command beside it.
4. What the text says and what the machine did are two labeled columns. The gap between them is the finding, and it is labeled as such.
5. The demonstration and the hypothesis never share a sentence.
6. Chapter numbers, full English book names, and Hebrew always with its English beside it.
7. One picture before any list. A reader should be able to draw the machine after one page.

## 5. The example form

Every example has the same five parts in the same order, so a reader learns the form once.

1. THE VERSE. The English, and the Hebrew phrase that carries the link, with its English beside it.
2. IN PLAIN WORDS. What the rule tells someone to do, or what happened.
3. WHAT THE MACHINE DID. The line in the event list and the entry on the account, quoted from the running world by a command.
4. WHAT GRADED IT. The test case, the count check, or the retelling that had to match, and whether it did.
5. RUN IT. The one command that reproduces parts 3 and 4.

### 5.1 The form filled in: Gad and Reuben's account

THE VERSE. Numbers 32:20-24. Moses to the two tribes who want the land east of the Jordan: "If you will do this thing: if you will arm yourselves before the LORD for the war, and every armed man of you will pass over the Jordan ... then afterward you shall return and be guiltless ... Build cities for your little ones and folds for your sheep." The word that carries the story across the books is the return: וְשַׁבְתֶּם ("and you shall return"), which Joshua 22:4 answers with "turn and go to your tents".

IN PLAIN WORDS. Two tribes ask to settle early. Moses lets them, on a condition: fight with everyone else first, then come home. And build your towns before you go. Two debts are opened.

WHAT THE MACHINE DID. At Numbers 32:20-24 the compiled law for the chapter writes two debts on the account of the two tribes, both under the heading "commanded": one to cross armed before the LORD until the land is subdued, one to build cities and folds. The entries are dated day 908,718 of the calendar, year 2,488 counted from the text's own dates. At Numbers 32:34-38 the tribes build, and the second debt is closed the same day by that event. The first stays open. At Numbers 32:28-30 a third debt is written on the account of the men who will divide the land (Eleazar, Joshua and the heads): give them Gilead if they cross. That one stays open too.

WHAT GRADED IT. The build's entry had to be found and closed by the building verses, and it was. Deuteronomy 3:18-20, where Moses retells the condition in his own voice, sits on the event list as a retelling. The payment lies in Joshua 22:1-4 ("you have kept all that Moses the servant of the LORD commanded you ... turn and go to your tents"), which is past the end of today's event list: the page shows that step as projected, and the crossing debt stands open on the running world until Joshua runs. That is the demonstration: a debt opened in one book, retold in a second, paid in a third, and the machine carries it open across the gap.

RUN IT. `python3 World/step9/cold_run_sequence.py --cursor "Num 33:1"` replays the event list to the left edge of that verse; the account is then read from the one database (the ledger view, entity `the_sons_of_gad_and_reuben`).

## 6. The six examples to publish

Chosen for what a reader with no background can see, and ranked by how much already exists.

| # | the example | what it shows | what exists | what is needed |
|---|---|---|---|---|
| 1 | Gad and Reuben's account (Numbers 32; Deuteronomy 3; Joshua 1, 4, 22) | an event opens a debt that later books carry and pay | the page, generated; the entries on the running world (section 5.1) | the run command on the page; the Joshua steps marked projected |
| 2 | Two men at the altar (Exodus 21:12-14; Numbers 35; Deuteronomy 19; 2 Samuel 3 and 20; 1 Kings 1-2) | a law given at Sinai decides two cases four books later: Adonijah is let go from the altar, Joab is not | the page, generated; every link measured, four typed links refused | the run command; the Samuel and Kings steps marked projected |
| 3 | The vows (Numbers 30) | a law with a due date: a father or husband may annul a vow only on the day he hears it; the machine sets the due date and the Mishnah's cases grade the answers | the compiled file, its cases from Mishnah Nedarim chapters 10-11, the count checks | a page through the generator; one case walked in the five parts |
| 4 | The retelling graded (Deuteronomy 5 against Exodus 20; Deuteronomy 9's forty days against the calendar) | the fifth book reads the record back: sixteen rows graded, and two of the ten words found with no code behind them until that chapter | the graded rows in the Deuteronomy map | a page; the sixteen rows in a table with plain labels for VERBATIM, VARIANT, EXPANDED and TURNED |
| 5 | The count check (Numbers 1 and 26) | the text gives a census; the world must match it; some checks diverge and are recorded, not repaired | the checkpoints and their positions table (298) | a page; the honest list of the known diverges |
| 6 | Seven where Exodus had six (Deuteronomy 7:1) | the machine reads a list and counts it; the Girgashite is in no Exodus list | the sitting's finds | a page; the eleven six-name lists and the three seven-name lists shown |

Two more pages already exist (the land's sabbaths, Leviticus 25; the debt that does not pass, Deuteronomy 15) and join the series after the six.

Each page is built through the generator (the script illustrate.py, today in the mockups folder outside the repository; it should move in as a tool once the owner decides to publish it). The generator's refusals are part of what we teach: a link is shown only when the same Hebrew word or an adjacent phrase stands in both verses, or a named teacher in the commentary taught the link, or it is labeled in red as our guess. A reader should be told that the page refused links its author typed. That is the credibility of the series.

## 7. The machine in four pictures (C4)

The C4 model from the note: the system in its surroundings; then the running parts; then the parts inside one of them; code only where it matters.

### 7.1 Context: who and what touch the machine

```
   a reader ─────► the website, the pages, the player
                          │
   the text ───────┐      ▼
   (24 books;      │   THE MACHINE  ◄──── the commentary library
    23,213 verses; └──►  reads the text,     (Mishnah = the test cases;
    305,507 words)       compiles the law,    Talmud = the reading rules;
                         runs the events,     Targum and Midrash = the readings)
                         grades the result
                          │
                          ▼
                    the records, open under CC0 on GitHub
```

### 7.2 Containers: the parts that run

```
  THE READING          THE COMPILE            THE RUN                  THE GRADING
  ┌──────────────┐     ┌────────────────┐     ┌──────────────────┐     ┌───────────────────┐
  │ locked       │     │ compiled files │     │ the event list   │     │ test cases 7,007  │
  │ readings 227 │────►│ of law: 67     │────►│ 1,327 lines      │────►│ count checks 298  │
  │ one per      │     │ laws switched  │     │ one world:       │     │ retellings graded │
  │ chapter, the │     │ on: 73         │     │ 319 accounts,    │     │ automatic checks  │
  │ commentary   │     │                │     │ a calendar,      │     │ that refuse on    │
  │ read whole   │     │                │     │ due dates        │     │ any mismatch      │
  └──────────────┘     └────────────────┘     └──────────────────┘     └───────────────────┘
                                                      │
                                                      ▼
                                THE LOG: every line hash-chained, in one database
                                THE PLAYER: the event list step by step, in a browser
                                THE INPUT DOOR: an outside input enters a copy of the world
```

### 7.3 Components inside the run

```
   a verse arrives ──► the event list puts its line ──► every switched-on law looks
                                                              │  does the event match?
                                                              ▼
                     it writes an entry on an account: a status, a block, a debt, a due date
                                                              │
                     due later?            ──► a due date; the calendar fires it on its day
                     pays an earlier debt? ──► that entry is closed
                     a date in the text?   ──► the calendar moves
                     a count in the text?  ──► MATCH or DIVERGE, written down, never repaired
                                                              │
                                                              ▼
                                       the log seals the line; the player shows it
```

### 7.4 Code: one function, once

One compiled function belongs in the public report, and only one: a short function from one compiled file, with its verse above it and its test case below it. That is enough for a programmer to believe the rest is the same shape, and it is all a non-programmer needs to see.

## 8. The how-it-works report of the machine (arc42)

The arc42 skeleton from the note, mapped onto what we already keep. This report is about our software and can be written now, mostly by re-cutting existing pages through the vocabulary rule.

| arc42 section | what the public page says | drawn from |
|---|---|---|
| 1 Introduction and goals | one world runs the Bible's events in order; the law is compiled and graded by the tradition's own cases | THE_WORLD.md, THE_TOUR.md |
| 2 Constraints | code only from the 24 books; the commentary is data, never code; no link without a teacher; every number computed; Hebrew always with English | the standing laws (the recovery page, section 3) |
| 3 Context and scope | picture 7.1; what is in (the five books so far) and what is not yet (the Prophets and Writings run later) | THE_BOOKS_AS_A_PROGRAM.md, section 2 |
| 4 Solution strategy | law is code, narrative is data; one event list, one world, laws as watchers, accounts as memory, the text's own dates as the calendar | THE_LOOP.md's decisions; the compiler law |
| 5 Building-block view | picture 7.2; the files by container | FUNCTION_CATALOG, DAEMON_INDEX, DEPENDENCY_INDEX (670 rows) |
| 6 Runtime view | picture 7.3 walked on one real verse: Numbers 32:20 opening the crossing debt; Deuteronomy 7:2 opening the ban's debt to Joshua | the walk maps' AS BUILT sections |
| 7 Deployment view | a clone anywhere; the commentary fetched by manifest; the player on a local port | SETUP.md, DATA_SOURCES.md |
| 8 Crosscutting concepts | the calendar; the entry vocabulary; the three link classes; the automatic checks; the log's chain | THE_CLOCK.md, TIME.md, THE_EFFECTS.md, THE_LINKS.md |
| 9 Architectural decisions | the numbered decisions, each with its why, in plain words | THE_LOOP.md (38 numbered decisions), CHRONICLE.md |
| 10 Quality requirements | reproducibility (a byte-identical replay), refusal on mismatch, every claim measured | the gates chain, the journal gate |
| 11 Risks and technical debt | the owed items; the known diverges; the holes found in the code | COMPILE_DEBT.md, the checkpoint positions |
| 12 Glossary | the translation table of section 4 | this file |

Plus the cover the note recommends: an executive summary (the purpose in one paragraph, how it works in one paragraph, the risks), an evidence index (the commands, the files, the test runs), and the open questions.

## 9. The design-recovery report of the text (the claim)

The second report and the harder one, because it is about intent. The note's split gives it its shape: what the text says it is supposed to do, against what it does when run, and the gaps.

### 9.1 What the text says it does (intent)

The evidence for intent is in the text's own words about itself: the receipts ("as the LORD commanded Moses"; the short form is כַּאֲשֶׁר צִוָּה "as He commanded", counted at its seats by the register gate); the retellings, which say "remember" and then retell; the tables (the journeys of Numbers 33, the borders of Numbers 34, the eras); the ten words as a table of contents (the schema finding); the fifth book's own frame, "these are the words". A public page lists these and says: the text repeatedly describes itself as a record to be checked.

### 9.2 What it does when run (implementation)

The event list runs. The laws switch on where the text gives them and write where the events match. The count checks match where the text counts. The retellings find their entries. In numbers: 1,327 events, 73 laws switched on, 319 accounts, 127 debts paid, 298 count checks, and the fifth book's rows graded against the record chapter by chapter.

### 9.3 The gaps (the findings)

Where intent and implementation disagree, the report says so, because that is where a reader learns the most and trusts us most:

- The second and the tenth of the ten words had no code anywhere in the machine until Deuteronomy 5 retold them; the retelling exposed the hole, and the words were compiled at the giving's own day.
- Deuteronomy 7:1 lists seven nations where Exodus lists six; the seventh is in no Exodus list.
- Deuteronomy 6:25's receipt has no Name in it, and the register's finder, built on the two forms with the Name, cannot see it.
- The token census read "king" in "Pharaoh king of Egypt" as Molech: the same consonants. A homograph, filed as a false edge with its reason.
- Some count checks diverge and stay recorded as diverging.
- The ban of Deuteronomy 7 opens a debt that no verse in the five books pays; the payment is in Joshua. So does the crossing debt of Numbers 32.

### 9.4 The hypothesis, labeled

Only after 9.1 to 9.3 does the page say what we think it means: that the text was built to be run, with Deuteronomy the release, Joshua the install, Judges the loop without the operator, the Prophets the event stream, Ezekiel a second specification. THE_BOOKS_AS_A_PROGRAM.md holds this in full with its eight proposals, none ruled. The public page carries it under the heading "What we think, and why we cannot yet say we know."

## 10. Verify it yourself

The page every skeptic goes to first. It quotes SETUP.md and nothing else:

```
git clone https://github.com/Josephtorah/TorahSim.git
cd TorahSim
python3 Data/fetch_shelf.py                  # the commentary library, by manifest, hashed
python3 World/build_world.py                 # the locked readings folded into one database
python3 World/step9/cold_run_sequence.py     # the event list runs: 10/10 at the end
python3 World/step9/world_board.py           # the player, at a local address
python3 World/step9/world_stepper.py --board # in a second window: Next and Auto-play
python3 World/step9/run_cold_all.py          # every test of every compiled file
```

With, beside each command, one sentence on what a reader should see. The page also says what a reader must take on trust (nothing about the machine; the readings' verdicts on the commentary are ours and are recorded row by row for anyone to dispute) and what a reader can check without trusting us (every count, every link, every test).

## 11. The order of work

Each item is a sitting or two in this thread, in ARCHITECTURE/, and opens on the owner's word. The walk thread keeps walking Deuteronomy; nothing here touches the engine.

1. THE VOCABULARY. The translation table (section 4.1) as its own page, and the jargon lint. One sitting. Everything after runs through it.
2. THE SIX EXAMPLES. The generator moved into the repository as a tool (the owner's decision, since it lives outside the repository today); the six pages built through it with their run commands; the two existing extra pages added. Two to three sittings.
3. THE MACHINE REPORT. The arc42 report of section 8, written from the existing architecture pages re-cut through the lint, with the pictures of section 7 and the one function of 7.4. Two sittings.
4. THE TEXT REPORT. The design-recovery report of section 9, written from THE_BOOKS_AS_A_PROGRAM.md, THE_TEN_AS_A_SCHEMA.md and DATABASE_SPECULATION.md, in the intent / implementation / gaps form. Two sittings.
5. THE VERIFY PAGE. Section 10, tested by running it in a fresh clone. One sitting.
6. THE SITE. The pages, the reports and their epubs on torahsimulation.org; a recording of the player playing one chapter; three doors on the front page: the curious reader (the examples), the programmer (the machine report and the verify page), the scholar (the text report and the readings' ledgers). The owner's call on the site's shape.

What should not wait: the Prophets do not need to run before the series is published. An open debt on an account that visibly closes when Joshua runs is itself the demonstration, and the pages say "projected" where the machine has not yet reached.

What waits on the owner: whether the generator goes public; the series' name; the site's front page; whether the install hypothesis and the Decalogue schema are named in the public text at all, or held until they are ruled.

## 12. What not to do

- Do not lead with the hypothesis. It is the most interesting thing we have and the least proven.
- Do not type an example. The pages that were typed had four bad links in them; the generated pages have none.
- Do not show a number without its command, or a link without its Hebrew.
- Do not use the machine's words bare. The lint exists for this.
- Do not argue theology or the text's authorship. The pages describe what the text does when run; the reader brings the rest.
- Do not promise what has not run. The event list ends at Deuteronomy 13 today.
- Do not re-explain from scratch each time. The existing architecture pages (the tour, the effects, the clock, the links, the Deuteronomy tutorial) are the material; they need the vocabulary pass, not a rewrite.

## 13. Where the counts came from

Measured on 2026-09-21 in the workshop: the compiled files (67 files matching `World/step9/cold_run_*.py`, the event list's own file excluded); the event list's length (the RUN literal in cold_run_sequence.py: 1,327 events); the dependency file's rows (670 rows naming a source); the text (Data/tanakh.sqlite: 23,213 verses, 305,507 words); the illustration pages (4 built, 4 specifications); the architecture pages (15); the Gad and Reuben entries of section 5.1 (the ledger view of World/journal/data/world.sqlite, read on the date). Read from the recovery page of the same date, its section 2: 227 locked readings, 73 laws switched on, 498 functions, 319 accounts, 127 debts paid, 172 dates, 298 count checks, 7,007 graded cases, the log's 9,772 rows; the 38 numbered decisions counted in THE_LOOP.md. The graded rows (sixteen on Deuteronomy 5, twenty-one on Deuteronomy 7) from the commit messages 7c8554e and 29c189b. Every count in a public page is to be re-measured on the day the page is built.
