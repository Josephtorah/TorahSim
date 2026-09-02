# How the Machine Works

*A plain-language tutorial on the architecture of the Torah
simulation project — written for readers with no programming
background. Every technical word is explained the first time it
appears, and again in the glossary at the end.*

## Before we begin: what this is, and the one promise

This project is building a working model of the Torah's law — a
machine you can ask questions, which answers with the tradition's own
verdicts and shows exactly where every answer came from.

That sentence contains the whole project, but every word of it needs
unpacking, and that is what this tutorial does. You do not need to
know anything about computers to read it. You also do not need to be
a Torah scholar: the books of the Jewish library are introduced from
scratch too, because the architecture only makes sense once you see
what each book on the shelf actually *is*.

The one promise of this document: **nothing is assumed.** Earlier
reports from this project were written for readers who had followed
along; they used terms like "unit," "claim," "compile," "exam," and
"runtime log" without stopping to explain them. This tutorial stops
and explains. If you read it in order, by the end you will understand
the whole architecture — including the newest discovery, which
changed how we see the entire Hebrew Bible.

One more thing before we start. This machine involves no guessing and
no artificial-intelligence "creativity." It is closer to very careful
bookkeeping. Every fact in it was put there by hand, from a named
source, with a paper trail. The computer's job is not to invent
anything; its job is to *hold* what the tradition recorded, *connect*
it the way the tradition connected it, and *replay* it on demand. Keep
that picture — a vast, honest ledger that can answer questions — and
the rest of this document is just the details.

## The library: the books this project runs on

Everything in this project comes from a specific shelf of books.
Here is that shelf, in plain terms.

**The Hebrew Bible — 24 books.** The Jewish count groups the Bible
into twenty-four books in three sections. The **Torah** is the first
five (Genesis through Deuteronomy) — the foundation document. The
**Prophets** (Joshua, Judges, Samuel, Kings, Isaiah, Jeremiah,
Ezekiel, and the twelve short prophetic books) carry Israel's history
and the prophets' speeches. The **Writings** (Psalms, Proverbs, Job,
and the rest, ending with Ezra-Nehemiah and Chronicles) carry poetry,
wisdom, and the records of the return from Babylonian exile. Keep
this three-part division in mind — the newest discovery in this
project is precisely about what the second and third sections turn
out to be.

**Onkelos — the ancient authorized translation.** Nearly two
thousand years old, this is the word-by-word translation of the Torah
into Aramaic, the everyday language of that era. It matters to us
because it is the tradition's oldest complete *reading* of every
single verse: when the Hebrew is ambiguous, Onkelos had to commit to
one meaning, and those commitments are evidence of how the chain of
tradition understood the text. We read Onkelos beside every verse we
process.

**The midrash collections — verse-by-verse commentary.** "Midrash"
means the tradition's recorded expounding of the text. These
collections walk through the Torah verse by verse and record what the
early rabbis derived from each one. Different collections cover
different books: Genesis Rabbah walks through Genesis; the Mekhilta
walks through the law chapters of Exodus; Midrash Tanchuma covers the
tabernacle-building chapters where the Mekhilta ends; Sifra walks
through Leviticus. In this project, one such collection is chosen as
the "spine" for each book of the Torah — the main commentary read in
full beside the verses.

**The Mishnah — the law code.** Compiled around the year 200 by
Rabbi Judah the Prince, the Mishnah is something very different from
commentary: it is a *rulebook*, organized by topic, not by verse.
Sixty-three tractates (topical volumes) covering blessings, Sabbath,
festivals, marriage, damages, courts, sacrifices, purity. Its basic
unit is the case: a short paragraph that says "in this situation, the
ruling is this" — often with a recorded disagreement ("Rabbi Meir
says this; the sages say that"). Crucially, the Mishnah almost never
explains *why*. It states inputs and outputs and moves on.

**The Tosefta.** A companion collection from the same era, in the
same style — additional case rulings arranged alongside the Mishnah's
topics.

**The Talmud — the discussion record.** Two of them: the Babylonian
Talmud (the larger, finished around the year 500) and the Jerusalem
Talmud. The Talmud takes the Mishnah's terse rulings and asks, page
after page, one recurring question: *"From where do we know this?"*
— and then it answers, walking the ruling back to a verse, testing it
against edge cases, and recording every disagreement along the way.
If the Mishnah is the rulebook, the Talmud is the record of the
rulebook being cross-examined.

That is the whole shelf. Now the big idea.

## The big idea: three literatures, three jobs

Here is the discovery that named this architecture — the owner
stamped it "the biggest news ever" when it was first measured, and
everything since has confirmed it.

Start with an everyday picture. Imagine a country's legal system as
three kinds of document:

1. **The founding archive** — the original events, precedents, and
   worked examples. Not organized for lookup; organized as history.
2. **The codified rulebook** — everything from the archive distilled
   into numbered rules: "in situation X, the ruling is Y."
3. **The annotated cross-reference** — the scholarly apparatus that
   proves each numbered rule actually came from the archive, with
   page citations and recorded objections.

The three Jewish literatures divide the labor exactly this way:

| Literature | Its job | In plain words |
|---|---|---|
| The 24 books of the Bible | **DEMONSTRATE** | show the law in action — definitions, precedents, worked examples |
| The Mishnah | **COMPILE** | turn the demonstrations into a rulebook of input-and-verdict cases |
| The Talmud | **LINK** | walk each compiled rule back to the verse that licensed it |

We borrow the word **compile** from computing, and it is worth
defining plainly, because it is the key word of the whole
architecture. To compile is to take material in one form and
translate it into a *runnable* form — the way a recipe compiles a
grandmother's demonstrated cooking into a card anyone can execute.
The demonstration shows the dish being made once; the recipe card
makes it repeatable. The Mishnah is the recipe box of the Torah.

And one more borrowed word: a **function**. In computing, a function
is a named, reusable piece of procedure — a recipe card with a name,
so it can be used again and again wherever it is needed. When this
document says "the carrying function" or "the audit function," it
means: a rule of the tradition, stated as a repeatable procedure.

Now a real example, small enough to hold in one hand.

**The breath-at-the-nose rule.** Genesis 2:7 says God breathed into
the first man's nostrils the breath of life — in the Hebrew, נִשְׁמַת
חַיִּים ("the breath of life"). Genesis 7:22 repeats the definition
during the flood: everything with the breath of life *in its
nostrils* died. So the Torah has **demonstrated** a definition: life
is located at the nose.

Some two thousand years later, the Mishnah (tractate Yoma, chapter 8)
rules on a life-and-death emergency: if a building collapses on the
Sabbath and a person may be buried in the rubble, you dig — the
Sabbath is set aside. And how do you check whether the person you
uncover is alive? *You check the nose.* The Mishnah has **compiled**
the Genesis definition into an executable rule: situation, procedure,
verdict. It does not say why the nose. It never says why.

Then the Babylonian Talmud (tractate Yoma, page 85a) asks its
signature question about this very rule: from where do we know that
life is at the nose? And it answers by naming Genesis 7:22. The
Talmud has **linked** the compiled rule back to its demonstration.

One rule, three literatures, three jobs — and the connection between
them is not our invention. The tradition itself recorded every link
in that chain. Our machine's job is to hold the chain.

## What the machine actually is

So what did we build? Not a chatbot, and not a search engine.
Here are its actual parts, each in plain language.

**Units.** The Torah is processed in passages — a story, a law
section, a chapter of building instructions. Each processed passage
becomes a *unit*: a structured file that holds the passage's Hebrew
text, its translation, and — most importantly — its *logic*: every
claim the reading established, written out formally. As of today
there are **117 frozen units**, covering the books of Genesis and
Exodus completely, end to end.

**Claims.** A claim is a single checkable statement with a source.
Not "the flood was forty days, roughly" — but "the reading of this
verse, witnessed at this source, establishes this fact," with the
source cited so exactly that a computer program can verify the
citation letter for letter. The corpus currently carries over two
thousand claim rows, and an automated verifier confirms them against
the source texts: at the last full audit, **zero had failed**.

**The world.** All the facts from all the units pool into one shared
world — one consistent model where Genesis's facts and Exodus's facts
coexist and must not contradict. Today the world holds **1,809
standing facts**.

**The fingerprint.** Here is a computing idea worth thirty seconds:
a *hash*, or fingerprint, is a short code computed from a body of
content, with the property that if even one letter of the content
changes, the code changes completely. It works like a wax seal on an
envelope — you cannot open and reseal it undetected. Our whole world
of facts has a fingerprint (currently the code 8b8fff1fa28953af), and
here is the remarkable part: it did not move through the entire
derivation of the book of Exodus. Forty chapters of new material
entered the corpus, and not one previously established fact shifted.
The seal held.

**Asking it questions.** The machine can be *posed a case*: you
describe a situation using registered terms (a wall collapsed; it is
the Sabbath; the person's status is uncertain) and the machine
returns the verdict — and not just the verdict, but its full
pedigree: which Mishnah row ruled it, which Talmud page linked it,
which verse anchored it, which of our units holds it. When the rabbis
themselves disagreed, the machine does not pick a winner: it returns
*both* verdicts with each authority's name attached, because the
disagreement is part of the record, and the record is the point.

That is the machine: units holding claims, claims pooling into one
sealed world, and a question-answering layer that always shows its
work.

## The assembly line: how a passage becomes part of the machine

Every passage goes through the same process — think of it as an
assembly line with quality-control gates between stations. Here it
is, station by station, in the plain vocabulary we use internally.

**1. Choose the portion.** Work proceeds at the grain of the weekly
portion — the *parashah*, the traditional division that synagogues
read one per week. One portion per sitting is the proven pace.

**2. Gather the reading list.** For each portion there is a declared
reading scope called the **core shelf**: Onkelos (the ancient
translation) plus the spine (that book's chosen verse-by-verse
midrash collection), read *in full*. Everything else the tradition
wrote on the passage — later commentators, mystical works, thousands
of rows per portion — is enumerated and honestly marked "outside the
declared scope." We never pretend to have read what we have not; the
coverage numbers are printed beside every stamp.

**3. Read and log.** Every source on the list is actually read, and
every source gets exactly one row in a **ledger** — a log file that
is *append-only*, meaning nothing in it may ever be erased or
edited, only added to (like a bound accounting book where corrections
get new lines, never erasers). Each row carries a verdict: does this
source bear on the logic, or provide context, or duplicate another,
or not bear at all?

**4. Build the logic.** From the material rows, the passage's claims
are written, each citing its source. Here stands one of the strictest
gates in the system, the **cite gate**: every citation must be an
exact, letter-for-letter substring of the reading ledgers. In plain
terms — *you cannot cite what you did not read.* The machine checks
this mechanically. A paraphrased or misremembered citation fails the
gate and blocks the whole unit.

**5. Freeze.** The finished unit is frozen — sealed against
accidental change, its text verified against the source database, all
its gates run. From now on, changes require a formal amendment with
its own paper trail.

**6. Render.** Each frozen unit generates a runnable rendering — a
program that re-asserts every claim, so anyone can run the unit and
watch it verify itself.

**7. Examine.** The unit faces the exam (the whole next chapter is
about this).

**8. Stamp.** When the reading is complete, the logic rebuilt from
it, and every gate green, the unit receives a **full rule** stamp.
Stamps were originally granted personally by the project's owner;
under a standing delegation they are now administered by the machine
against fixed criteria — but every delegated stamp is *labeled*
delegated, forever, so the record of what the owner personally
approved never blurs.

## The safety rules: how we keep ourselves honest

An architecture is only as good as its honesty. These are the
standing laws that keep this one honest — each born from a real
episode, several from real mistakes.

**Recorded, never assigned.** The machine only encodes connections
the tradition itself made. When our tools *discover* a possible
connection (and they do — you will see one in the worked example),
it enters the machine as law only if the tradition's own record
confirms it. The machine proposes; the record disposes.

**Evidence is immutable; tools are improvable.** The project's
constitution splits everything into two piles. *Evidence* — texts,
ledgers, test records — is append-only forever. *Tools and models* —
the programs that measure and verify — may be freely improved, as
long as every gate stays green and the change is logged. During the
last audit two measuring instruments were found to be crashing or
measuring the wrong pocket; both were repaired openly, with the fix
and its date commented in the file. The law was being followed; the
instrument was wrong. That distinction matters.

**A report of zero is worth only the coverage line above it.** This
one deserves its analogy. Suppose a metal detector sweeps a field and
reports "no metal." Should you trust it? Only if you first waved it
over a known coin and heard it beep. Our standing law: any automated
check that reports an *absence* must first prove, on a known
specimen, that it is capable of finding what it claims is absent —
and must print what it actually scanned beside its result. This law
fired live during the recent canon experiment: a scan for
Sabbath-carrying verses returned zero, the law refused the zero, the
probe exposed a flaw in the search pattern, and the corrected scan
found exactly six verses — the right answer, which the broken scan
would have silently missed.

**Count what you report, and let independent counters disagree.**
During the full audit, one sweep reported 95 units while the master
record said 117. The disagreement was not smoothed over; it was
chased, and the cause found (a pattern that read only one of the two
formats the files use). Twenty-two units had been silently skipped;
they were then checked separately, and all were green. The lesson is
standing law: two independent counts that disagree are a gift — one
of them is wrong, and now you know to look.

**The vocabulary is discovered, not designed.** Every term the
machine's cases use — "private domain," "eve of the Sabbath,"
"tree-product" — must have been introduced by a source we actually
read, and each is registered with the source that introduced it and
its own Hebrew wording. We are not free to invent convenient
categories; the case language grows only as the reading grows. The
registry currently holds 145 such input dimensions.

**Findings are filed, never patched.** When an exam reveals a gap in
the machine, the gap is written up as a *finding* and then repaired
through the full normal path — claim, citation, gates, freeze,
paper trail — never quietly fixed on the spot. Speed is allowed;
shortcuts are not.

**Disputes are outputs, not errors.** Worth repeating: when the
tradition recorded a disagreement, our machine's correct answer *is
the disagreement*, both sides, names attached.

## The exam: how the Mishnah became our test suite

In computing, a **test suite** is a collection of questions with
known correct answers, used to check whether a program actually
works: feed in the question, compare the program's answer to the
known one, and any mismatch is printed in red. Good test suites are
precious and expensive to write.

Here is the insight that created this project's exam era: **the
Mishnah already is one.** It is a book of thousands of cases — each
with inputs (the situation) and an output (the verdict) — organized
by topic, sitting there for eighteen centuries. It cannot be read
verse-by-verse, because it isn't organized by verse; for a long time
that felt like a debt we owed it. The resolution was a ruling that
split the oral library into two shelves: the verse-anchored books
(Onkelos, the midrash collections) feed the *reading*, and the
case-anchored books (the Mishnah, the Tosefta) are the *testing*
shelf. We don't owe the Mishnah a read-through. We owe it an exam.

So the exam works like this. After a portion of the Torah is derived,
we collect every Mishnah case that the tradition's own citation
records tie to those chapters. Each case is quoted into an exam
paper *before* any answering machinery is built — inputs, expected
verdict, recorded dispute if any, and whether the Talmud links it
back to our verses. Each case is then classified honestly: can the
machine already answer it? Does the machine hold the rule as text but
not yet in runnable form? Or does it hold nothing? The gaps become
findings. Then the rules are compiled into modules (topical bundles
of runnable rules — the module names follow the Mishnah's own
tractates), and the exam is run: every case posed, every answer
compared against the Mishnah's recorded verdict, every miss printed.

The running score, across nine exam rounds so far: **329 cases
posed, 329 answered correctly** — where "correctly" means matching
the tradition's recorded verdict, including returning both sides of
every recorded dispute. The compiled rulebook currently holds 124
rules.

Three moments from the exam era are worth telling.

*The engine corrected the exam.* In the very first round, one case
came back mismatched — and on inspection, the error was in our exam
paper, not the machine. The Mishnah's own plain text adjudicated in
the engine's favor. A test suite that catches errors in its own
questions is working.

*The reading anticipated the exam.* Round after round, the majority
of the Mishnah's cases turned out to be *already held* by the machine
before the exam was written — because the morning's careful reading
of the verse-by-verse sources had already seated the same law the
Mishnah compiles. In the most recent round (the chapters that close
Exodus), the exam produced **zero** findings: every case the docket
posed, the derivation had already answered. The two shelves are
converging on each other exactly as the architecture predicts.

*Verdicts computed from the verse's own numbers.* Some disputed
rulings turned out to be calculations. The rabbis' two different
sizes for the tabernacle's table are the same verse's dimensions run
through two different cubit conversions — they disagree about a
conversion constant, not about the text. The machine now computes
both sides of such disputes live from the verse's own numbers. In
another case, a rabbi's claim of thirteen covenants over
circumcision was checked by simply counting the covenant-word's
occurrences in Genesis 17: exactly thirteen.

## The newest discovery: the rest of the Bible is the logbook

Everything so far involved the Torah (demonstrations), the Mishnah
(compiled rules), and the Talmud (links). That left a giant open
question, and the owner posed it directly: *we know about the Torah —
but what about the rest of the 24 books?* Take some of the Mishnah's
compiled functions and hunt for them in the Prophets and the
Writings. The suspicion: the functions will be found there.

One more computing term, the last big one: a **runtime log**. When a
machine actually runs — a ship's engine, a factory line, a computer
system — its operation leaves a written trail: startup entries,
routine operations, unusual incidents, repairs. That trail is the
runtime log. It is not the machine's blueprint and not its rulebook —
it is the *evidence that the machinery actually ran*, and how it
behaved when it did.

Five compiled functions were hunted across the Prophets and the
Writings, using only links the tradition itself recorded. The result
was five for five — and a sharpened picture: **the Torah demonstrates
the law as specification; the Prophets and the Writings demonstrate
it as operation.** They are the runtime log of the very functions the
Mishnah compiles. Here are the five finds, each a story.

**The carrying rule, re-stated and then enforced.** The Torah seats
the rule that carrying between domains is a forbidden Sabbath labor.
Four centuries later, the prophet Jeremiah (chapter 17) re-issues it
— carry no מַשָּׂא ("burden") on the Sabbath day, none out of your
houses, none in through the gates — and then cites his own source:
"as I commanded your fathers." A prophet quoting the Torah's seat.
And a century after that, Nehemiah (chapter 13) *runs* the rule with
police powers: merchants warned, the gates of Jerusalem shut before
the Sabbath, guards posted. A statement, then an enforcement action —
log entries.

**The audit waiver, called twice.** Our Exodus reading had found the
tabernacle's financial constitution: public money handled under
witnesses, accounts published — with one exception, a waiver of
audit for the *proven faithful*. In II Kings 12, King Joash's temple
repair fund is disbursed without a reckoning "for they dealt in
faithfulness." In II Kings 22, about a century later, King Josiah's
repair fund uses the *same waiver in nearly the same words*. The same
function invoked twice, generations apart, near-verbatim — and the
Babylonian Talmud (Bava Batra 9a) later compiles that very verse into
standing law about charity collectors. Meanwhile Ezra 8:34 records
the full protocol running: everything transferred "by number, by
weight... and all the weight was written."

**The half-shekel's floating rate.** The Torah sets a flat half-
shekel head tax — everyone equal, rich no more, poor no less. The
Mishnah records that the *coin* changed across eras while the
*equality* held. And Nehemiah 10 shows the variable actually moving
in the canon's own ink: the impoverished returnees establish a
*third* of a shekel — a different rate, same flat structure. In
computing terms: the parameter drifted; the invariant held. The
Writings recorded exactly the behavior the Mishnah's discussion
presupposes.

**The corrupted trial.** The Mishnah compiles capital-court
procedure: two witnesses, a formal charge, execution outside the
city. In I Kings 21, Queen Jezebel has Naboth judicially murdered —
and the chilling thing is that *every form is correct*: two witnesses
seated opposite him, the formal blasphemy charge (phrased in the same
euphemism the Mishnah's own procedure uses), taken outside the city,
stoned. Valid procedure, false inputs — what an engineer would call
the corrupt-run edge case, preserved in the canon as a warning. The
tradition wired this trial directly into its law: the Mishnah's
chapter on examining witnesses links to Naboth's verse, and Sifra —
the Leviticus commentary we are about to start reading — cites Naboth
in its treatment of Leviticus 24. Remember that address; it returns
in the final chapter.

And in the same courtroom register: at Jeremiah's own trial for
prophesying against the Temple (Jeremiah 26), the elders rise and
quote the prophet Micah *verbatim* — word for word — as precedent
for acquittal, since King Hezekiah had not executed Micah for the
same speech. A court citing case law, inside the Bible itself.

**The reading instrument's own charter.** Nehemiah 8:8 describes the
great public Torah reading after the return: they read from the book
מְפֹרָשׁ ("made distinct") — and the Talmud identifies that word as
the public translation itself, the very institution of reading the
Hebrew with its Aramaic rendering. The instrument this whole project
reads with — Onkelos — has its installation record in the Writings.

**The taxonomy.** Across the five hunts, the runtime log shows at
least seven distinct record types: re-statements (Jeremiah 17),
enforcement actions (Nehemiah 13), repeated calls (the two Kings
audits), step-by-step traces (Ezra 8), parameter drift (the third-
shekel), corrupt-run edge cases (Naboth), and precedent citations
plus instrument charters (Jeremiah 26; Nehemiah 8).

**Why this matters for the build.** The remaining 22 books are not a
mountain of new law waiting to be derived. They are the *test log* of
functions the Torah already seats — which makes them the inexpensive,
high-confirmation layer of the project's first pass. Reading them
will mostly *confirm* the machine, entry by entry.

## A worked example, end to end: carrying on the Sabbath

Let's walk one function through the entire architecture, so every
layer appears in a single story.

**The demonstration (Torah).** In Exodus 36, the tabernacle donations
overflow, and Moses orders a halt proclaimed through the camp: let no
man or woman bring any more material from the tents. The tradition
reads this halt as a demonstration about *carrying*: bringing from a
private tent to the public work could be forbidden — therefore
carrying between domains is a labor, the kind the Sabbath rests.

**The compilation (Mishnah).** Tractate Shabbat opens — its very
first paragraph — with the carryings-out between domains, counted in
the Mishnah's compressed style as "two that are four." Householder
and beggar, an object passing from the private domain to the public:
who is liable in each permutation. Inputs and verdicts, no reasons
given. The rule has become a recipe card.

**The link (Talmud).** The Babylonian Talmud's opening discussions of
tractate Shabbat connect the carrying prohibition to its scriptural
seats — the tradition's own recorded wiring between the rulebook and
the verses.

**The runtime log (Prophets and Writings).** Jeremiah 17 re-states
the rule and cites its source; Nehemiah 13 enforces it with shut
gates and posted guards. The function's operational history.

**The machine (us).** Our Exodus units hold the demonstration as
claims; our compiled modules hold the Mishnah's carrying cases and
answer them; the exam confirms the answers against the recorded
verdicts.

**And the discovery layer.** Here is the part that shows where this
is going. We keep a database of the entire Hebrew Bible — all 23,213
verses — in which every word is tagged with its dictionary root, so
the computer can search by *root* rather than by surface spelling.
We asked it a blind question: in which verses do the root for
"burden" and the root for "Sabbath" occur together? First answer:
zero — and the zero-report law refused it, forced a probe on a verse
known to contain both, exposed the flawed search pattern, and the
corrected scan returned **exactly six verses: Jeremiah 17:21, 22, 24,
27 and Nehemiah 13:15, 19** — precisely the carrying function's canon
career, and nothing else. The machine *found* the function's call
sites on its own; the tradition's recorded links, checked afterward,
confirmed every one. That is "recorded, never assigned" working as
designed: the scanner proposes, the record confirms.

One pass of a mechanical scan reassembled, from the Bible's own
words, the same web the tradition recorded by hand. The owner's
instinct — "maybe we piece the functions together from the verses
that are referenced" — is now a working method.

## Where we stand, and what happens next

**The scoreboard, in plain terms.** Two books of the Torah — Genesis
and Exodus — are complete: read under the declared scope, their logic
derived, frozen, examined, and stamped, end to end. That is 117
units, 1,809 standing facts in one sealed world whose fingerprint has
not moved through an entire book's worth of new derivation, over two
thousand verified claims with zero failures, nine exam rounds at 329
of 329, and a compiled rulebook of 124 rules speaking a
145-dimension vocabulary that the sources themselves introduced.

**Next: Leviticus** — with a new spine (Sifra, the ancient
verse-by-verse law commentary on Leviticus) beside Onkelos, same
assembly line, same exam rhythm.

And one address in Leviticus deserves its own paragraph, because the
whole architecture has been building toward it. One last computing
term: a **call site** is the place in a program where a prepared
function is actually *used* — where the machinery that was carefully
built finally gets invoked on a live input.

The book of Exodus *builds the machine*: the court is chartered, the
priesthood vested, the oracle's access rules published, the audit
constitution demonstrated. But in all of Exodus, no live case walks
in. **Leviticus 24 is the first recorded call.** A fight breaks out
in the camp; a man blasphemes; and for the first time, a live case is
brought *into* the institutions Exodus built — placed in custody
while the court seeks the verdict from the oracle. The blueprint era
ends and the operating era begins, in the text's own narrative. And
the tradition already wired this call site into the runtime log:
Sifra's commentary on this very chapter cites Naboth's corrupted
trial — the edge case pointing back at the procedure's first clean
run.

That is where the machine stands: two books built, the rulebook
passing every exam, the rest of the Bible newly understood as the
operating record — and the first customer about to walk through the
door.

## Glossary

**Append-only.** A record that may only be added to, never erased or
edited — like a bound accounting ledger. All our reading logs work
this way.

**Call site.** The place where a prepared rule or procedure is
actually invoked on a live case. Leviticus 24 is the Torah's first
recorded call into the institutions Exodus built.

**Claim.** A single checkable statement established by reading, with
an exact citation. The corpus holds over two thousand.

**Compile.** To translate material into runnable form — as a recipe
card compiles a cooking demonstration. The Mishnah compiles the
Bible's demonstrations into case rules.

**Core shelf.** The declared reading scope for each passage: Onkelos
plus the spine commentary, read in full; everything else enumerated
and honestly marked outside the declared scope.

**Dispute.** A recorded disagreement between authorities. The
machine returns both verdicts with names attached — a dispute is a
correct answer, not an error.

**Exam.** Running the Mishnah's recorded cases against the machine
and comparing every answer to the recorded verdict. Nine rounds so
far: 329 of 329.

**Finding.** A gap or error surfaced by an exam or audit — always
filed in writing first, then repaired through the full normal
process, never patched quietly.

**Fingerprint (hash).** A short code computed from the whole world of
facts; any change to any fact changes the code. Our seal — currently
8b8fff1fa28953af — held unmoved through the entire book of Exodus.

**Freeze.** Sealing a finished unit against casual change; further
edits require a formal, logged amendment.

**Function.** A named, reusable procedure — a recipe card. "The
carrying function," "the audit function."

**Ledger.** An append-only reading log: one row per source read, with
a verdict.

**Mishnah.** The rabbinic law code (about the year 200): cases and
verdicts organized by topic, reasons omitted. Our testing shelf.

**Module.** A topical bundle of compiled rules, named for the
Mishnah's own tractates.

**Runtime log.** The written trail a running machine leaves —
operations, incidents, repairs. The Prophets and Writings are the
Torah's runtime log: the record of the law operating in history.

**Spine.** The one verse-by-verse commentary read in full beside
Onkelos for a given book: Genesis Rabbah for Genesis, the Mekhilta
(then Midrash Tanchuma) for Exodus, Sifra for Leviticus.

**Stamp.** The formal mark that a unit is complete — reading done,
logic rebuilt from it, every gate green. Machine-administered stamps
are labeled "delegated" forever.

**Talmud.** The discussion record (Babylonian and Jerusalem) that
links the Mishnah's rules back to their verses, tests edge cases, and
preserves disputes. The bridge between the shelves.

**Test suite.** A collection of questions with known correct answers
used to verify a program. The Mishnah is ours — it was one all along.

**Unit.** One processed passage of the Torah: its text, translation,
and formal logic, frozen and verified. 117 exist today.

**Vocabulary.** The registry of every input term the machine's cases
may use; each term must have been introduced by a source actually
read. Discovered, never designed. Currently 145 dimensions.

**World.** The single pool of all established facts from all units —
one consistent model under one fingerprint.

**Zero-report law.** No automated check may report an absence unless
it first proved, on a known specimen, that it could detect a
presence — and it must print what it scanned. The metal detector must
beep on the known coin before "no metal" means anything.
