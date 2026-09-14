# THE TOUR — what this program is, taught by one story

**A tutorial (rewritten 2026-09-07 for readers who know nothing about
this project; section 9, the fourth book, added 2026-09-13 with the
counts brought current).** This is the front door to the ARCHITECTURE folder.
Read it first. It gives you one picture and one story, and every
other document here hangs off those two. You do not need to know
the Bible's chronology, the Talmud, or any programming. Every term
is explained the first time it appears.

*Verses are given in plain modern English, rendered from the Hebrew
and checked against it. Every verse cited is quoted whole.*

---

## 1. What this program does

The laws in the Bible are written as cases: *when* this happens,
*then* do that. And they do not stop at "do that" — they say what
changes. He pays. He goes free. The land must rest. This program
takes the events the Bible itself narrates, runs the Bible's own laws
on them, and keeps the accounts those laws open and close: who owes
what, who is free, what is due on which day.

Think of it as a bookkeeper who has read the whole text and applies
its rules as the story unfolds. If the program vanished, you would
still have the laws as words on a page. What you would lose is the
running picture of what those laws *do* over time — a servant's
six-year clock ticking, an ox becoming a known danger after its third
attack, a debt on the land collecting centuries later. The program
exists to show the law alive.

## 2. Where it sits in the world

```
   THE BIBLE  ─── events, in the order the verses stand ───▶  ┌─────────────┐
   (the text is the clock)                                   │ THE PROGRAM │ ──▶  THE LEDGER
                                                             └─────────────┘      (accounts, over time)
                                                                    ▲
   THE TRADITION'S COMMENTARIES (Mishnah, Talmud) ─── the source     │
   each ruling cites; the answer sheet the program was graded against
```

What to notice: the program has one input and one output. The input
is the text itself, read as a stream of events in the order the
verses stand — the text is the clock. The output is a LEDGER: a set of
accounts on people, land, and institutions, changing as the verses go
by. The tradition's commentaries sit beside the program, not inside
it: every ruling the program makes carries a note saying where the
tradition recorded that reading, and before any rule was allowed in
it was graded against the tradition's own tables of decided cases.
But when it runs, the program reads verses and writes accounts —
nothing else.

If you can say that picture back in thirty seconds, go on.

## 3. The seven parts

```
   ┌──────────┐    ┌──────────────────┐    ┌─────────────┐    ┌──────────────┐
   │ THE TAPE │ ─▶ │ THE LAW LIBRARY  │ ─▶ │  THE RULES  │ ─▶ │  THE LEDGER  │
   │ (events) │    │ (57 programs)    │    │ (62 watchers)│    │ (accounts)   │
   └──────────┘    └──────────────────┘    └─────────────┘    └──────────────┘
                            │                      │                  ▲
                            ▼                      ▼                  │
                   ┌──────────────────┐   ┌────────────────┐  ┌──────────────┐
                   │ THE LINKS        │   │ THE CLOCK      │  │ THE EFFECTS  │
                   │ (calls between   │   │ (days; dates   │  │ (1012 allowed│
                   │  programs)       │   │  from the text)│  │  changes)    │
                   └──────────────────┘   └────────────────┘  └──────────────┘
```

Seven parts. One sentence each; the details come later, when the
story needs them.

- **The tape** is the Bible's events, one after another: "a man
  buys a Hebrew servant," "an ox gores," "the horn is sounded for
  the jubilee." Each event names the verse it comes from.
- **The law library** is the laws themselves, turned into programs:
  fifty-seven of them as of 2026-09-13 (the count grows with every
  stretch compiled), one per stretch of the text (Exodus 21,
  Leviticus 5, Leviticus 24, Numbers 35, and so on). Each holds the stretch's
  cases — when this, then that — with a ruling and a consequence for
  each case.
- **The rules** are the laws that watch. Each is a small program that
  sits and waits, and acts on its own the moment its event appears
  on the tape. There are sixty-two of them as of 2026-09-13.
  (Programmers call such a watcher a "daemon"; this document will
  just say rule.)
- **The clock** counts days. It moves only when the text states a
  date. The year, the month, and the special cycles are worked out
  from the day count by a calendar whose every number has a source.
- **The ledger** is the state of the world: every person, animal,
  field, or institution the text names is an ENTITY — an account —
  with flags on it (free, forewarned, unclean) and a list of entries
  (debts, duties, clocks) written by the rules.
- **The effects** are the fixed list of changes a rule is allowed to
  make — 1,012 of them as of 2026-09-13, every one a verb the text
  itself uses: "goes free," "pays," "burned outside the camp." A rule cannot write a
  change that is not on the list.
- **The links** are how the law programs call one another, because
  the text itself refers across books: Exodus 21's injury law gets
  its meaning from a verse in Leviticus 24.

## 4. How the parts are wired

```
   Exodus 21 program ──calls──▶ Leviticus 24 program        (a definition lives elsewhere)
   Leviticus 5 program ──points to──▶ Leviticus 1 program   ("as prescribed": a reference)
   Exodus 22 program ──fetches from──▶ Deuteronomy 22        (one number, stored elsewhere)
```

What to notice: the arrows are not all the same kind. A **call**
moves a ruling: Exodus 21 does not contain the meaning of "eye for
eye"; it runs a function that lives in the Leviticus 24 program and
gets the answer back. A **reference** moves a procedure: Leviticus 5
says "as prescribed" and the program follows the pointer to chapter
1's rite. A **fetch** moves one number: Exodus 22 fines a seducer
"like the dowry of the virgins," and the fifty shekels are fetched
from Deuteronomy.

None of these arrows are ours. Each one is in the text — a phrase
repeated in two books, a pointer word, a formula naming a number
stored elsewhere — and the program only transcribes it. Every link
is labeled (the counts here are as of 2026-09-13, over 482 edges
and 173 pointers): 455 are references (the text points, the program
follows) and 48 are transfers (a law carried from one passage to
another on a shared word — and each of those names the teacher in
the tradition who made that transfer, because the tradition's own
rule forbids inventing one). Nine are marked as hypotheses: links
we believe but cannot yet source, kept visible and never counted as
proven. A hundred and forty-three more connections carry no law
across them at all — a test registering another program's rules, a
word that merely looks the same in two places — and are labeled so,
to keep the list complete. THE_LINKS.md in this folder walks the links one at a time.

## 5. Follow one event from birth to rest

The most ordinary event in the library: a man buys a Hebrew servant.
Exodus 21:2:

> "When you buy a Hebrew servant, he works six years; in the seventh
> he goes out free, owing nothing."

Here is the program's own record of that event, as it prints it —
five kinds of line and nothing else: an EVENT arrives; a rule
WRITES the ledger; a TIMER is SET; a TIMER is CANCELLED; a TIMER
FIRES. (A sixth kind, CLOSE — an open entry closed by an event — was
added with the fourth book; section 9 shows it.)

```
   day 0        EVENT        a Hebrew servant is bought   (the servant; the master)
                ── the servant rule fires ──
   day 0        WRITE        a six-year term   on the servant          [Exodus 21:2]
   day 0        TIMER-SET    goes free         on the servant   due: the same date, six years on
   day 1 …      (nothing; the servant carries the flag "Hebrew servant")
   six years    TIMER-FIRE   goes free         on the servant
   six years    WRITE        goes free         on the servant   status → free
```

Walk it in time:

1. **The event arrives.** The tape delivers "a Hebrew servant is
   bought," naming the servant and the master. The program hands it
   to every rule at once.
2. **One rule fires.** Only the servant rule recognizes this event.
   It runs the case from Exodus 21:2 and returns two consequences.
3. **The first consequence is written now:** a six-year term on the
   servant's account, with the master named as the other party. The
   servant's account gets the flag "Hebrew servant."
4. **The second consequence is scheduled:** "goes free," due six years
   on. The clock counts days, so the program asks its calendar for
   the day that is the same date six years later — it does not guess
   at 365 times six. Because it is due in the future, nothing is
   written yet; a TIMER is set. This is the moment a ledger becomes a
   simulation: the program now owes something to the future.
5. **Time passes.** The clock moves forward as the text states dates.
   Nothing happens to this servant; his open term sits in the ledger.
6. **The timer fires.** When the due day arrives, the program writes
   "goes free": a status change, the servant's flag flipped to free.
7. **Rest.** The event is over. The account holds two rows — a term
   opened, a freedom written — and anyone reading the ledger later can
   see both and where each came from.

That is the whole program in one path: **event → rule → ledger, with
time in between.** Everything else is a variation on those three
arrows.

## 6. The same event, when the path bends

Now the servant does not want to leave. Exodus 21:5-6:

> "But if the servant says outright: I love my master, my wife, and
> my children; I will not go out free — then his master brings him
> before the judges, and brings him to the door or the doorpost, and
> his master pierces his ear with an awl; and he serves him forever."

```
   day 0        EVENT         a Hebrew servant is bought   (the pierced one)
   day 0        TIMER-SET     goes free      due six years on
   day 0        EVENT         the servant is pierced
                ── the servant rule fires again ──
   day 0        TIMER-CANCEL  goes free                  [Exodus 21:5-6 "forever"]
   day 0        TIMER-SET     free at the jubilee        due: the next fiftieth year, from the calendar
   six years                  (nothing fires — the six-year timer is gone)
   the jubilee  TIMER-FIRE    free at the jubilee
```

Two things the plain path never showed:

**A later event can cancel a scheduled change.** The piercing is an
event like any other. The servant rule fires on it and, instead of
adding a row, *cancels* the pending "goes free" timer. This ability
was discovered here: the first version of the program had no way to
take back a future it had already promised, and the pierced
servant's "forever" forced it.

**"Forever" is a link.** The verse says forever; the program does not
schedule nothing. It schedules a *different* release, at the jubilee,
because the tradition reads "forever" as running out at the fiftieth
year — and the fiftieth year is defined three books away, in
Leviticus 25:10:

> "You shall make the fiftieth year holy, and proclaim freedom
> throughout the land to everyone living in it. It is a jubilee for
> you: each of you returns to his family land, each to his family."

And here is the most important rule in the whole design, visible in
this trace. A rule may write the ledger, set a timer, or cancel one.
It may **never put a new event on the tape**. If a rule tried to, the
program stops with an error — the code calls this THE FENCE. Events
come from the text only. Consequences are computed; history is never
invented. When one law's consequence must trigger another law, it
happens the only allowed way: the first law writes something in the
ledger, and the second law's condition reads that ledger. That is how
a chain of consequences runs without anyone making anything up.

## 7. A second event that collides with the first

The jubilee is not only a date. It is an act the text describes —
the horn sounded, freedom proclaimed — and when that act appears on
the tape, it touches every servant in the world at once.

```
   the fiftieth year   EVENT   the jubilee is proclaimed   (the horn sounded; the servants sent free)
                       ── the servant rule fires ──
                       WRITE   goes free   on every account carrying the flag "Hebrew servant"
```

What to notice: two clocks were running on two different scales. The
six-year term is *personal* — it started when this man was bought.
The jubilee is *institutional* — it runs on the land's count and does
not care when anyone was bought. When they collide, the jubilee wins:
a servant bought in year forty-six, with two years left, walks out in
year fifty with everyone else. The tradition's own table of rulings
lists exactly these exits as the ways a servant's term can end — by
the years, by the jubilee, by paying off the balance — and the trace
above is that list, running.

One more subtlety the tradition insisted on: whether a fiftieth year
really is a jubilee depends on what was *done* that year — was the
horn sounded, were the servants sent free — and the teachers
disagreed about which acts are essential. So the program does not
free anyone merely because the fiftieth year arrived. The count's
timer writes only "the fiftieth year has come"; the release is
written when the proclamation act is read, and where the teachers
disagree the program writes both answers with each teacher's name.
THE_CLOCK.md tells that story in full.

## 8. The three books, run in order

Until recently each story above ran in its own small test world. On
2026-09-07 Genesis, Exodus, and Leviticus were run start to finish
on ONE world, every rule watching, the clock moved only by the
dates the text itself states — sixty-eight of them on that first
run; by the next day, with all of Genesis's stories added to the
tape, 129 dates and more than a thousand events. What came out:

- The tradition's entire chronology — the flood's year, the exodus
  four hundred years after Isaac's birth, the tablets broken on the
  seventeenth of the fourth month, the priests' seven days ending on
  the day the Tabernacle was raised — came out of the text's numbers
  alone. Every date is one year above the tradition's traditional
  count, for one reason the machine states: the tradition counts
  Adam's first year as year zero.
- Where the text and the tradition disagree, the machine reports it
  and does not paper over it: the flood's 150 days come out as 147
  under the tradition's month length; the "430 years in Egypt" come
  out as 210 (the Talmud itself records that the elders translating
  for King Ptolemy wrote "in Egypt and in other lands").
- Two errors that only one shared clock could expose: a rule that
  counted "the eighth day" one day late, and a test script that had
  invented a four-day wait the text never gives. Both had been hidden
  by hand-typed "move ahead" lines in the old separate worlds.

A second look the following day found four more gaps in the
account of time — laws that should switch on only when the text
gives them, undated scenes placed by their position on the page, two
ways of counting a year that the text uses side by side, and the
several counting systems the text keeps at once. All four were
built the next day: every law now declares the verse that speaks it
and the act that switches it on, every undated event says what
placed it (the text, a reading of the tradition, or the page's
order), the tradition's year count is a rendering of the machine's,
and the text's own day-words are read. Section 9 shows them at work
on the fourth book.

THE_CLOCK.md teaches how the clock does this, from three examples.

## 9. The fourth book: Numbers, where the laws are asked to act

Between 2026-09-09 and 2026-09-13 the fourth book was walked from
its first verse to its last, one weekly portion at a time — each
portion read on its shelf, frozen, and compiled before the next was
opened — and its acts were put on the same tape as the three books
before it. Numbers is a different kind of book from those three.
Genesis put the story on the tape. Exodus and Leviticus put the laws
in the library. Numbers is where the laws are *performed*: the count
Exodus commanded is taken, the Passover Exodus specified is kept, the
altar Exodus raised is dedicated — and it is where the laws meet
facts they cannot answer. Here is what it taught the program, one
thing at a time, each with its verse.

**The machine could not count a census.** Numbers 1:21:

> "Their numbered ones, of the tribe of Reuben: six and forty
> thousand and five hundred."

On the first day of the walk the program's number-reader — the piece
that turns a verse's number-words into a number — read that verse as
1,546. It added six, forty, a thousand and five hundred. It had been
built on Genesis and Exodus, where the numbers are ages and days, and
the census writes its numbers in a grammar of its own: a thousand
multiplies the group before it, "and a thousand" adds, "five, five"
means five each, and the word for "from" shares its letters with the
word for "a hundred of". Each rule was written first as a test that
had to fail, then taught, and then the old reader and the new were
run over every verse of the Bible and every verse that changed was
read by hand. That last step is where the real finds came from — a
place-name meaning "town of the four" that had been counted as four,
"the plenty" read as "the seven", "rulers of thousands" read as two
thousand. By the book's last law chapter the reader carries
twenty-nine such rules, the last of them for Numbers 35:5, whose
"two thousand" it had read as nothing at all:

> "And you shall measure outside the city, on the east side two
> thousand by the cubit, and on the south side two thousand by the
> cubit, and on the west side two thousand by the cubit, and on the
> north side two thousand by the cubit, with the city in the middle;
> this shall be for them the pasture-lands of the cities."

The tests as they run today, three of the 208:

```
  PASS  N1  Num 1:21 = 46,500   got [46500]
  PASS  N2  Num 1:46 = 603,550   got [603550]
  PASS  D1  Num 35:5 = [2000, 2000, 2000, 2000]  ("two thousand by the cubit" four times — the prefixed cubit no unit-noun mark; was [])   got [2000, 2000, 2000, 2000]
208/208 probes
```

What to notice: two of the rules cannot be found in the letters at
all. The vowel points under the letters separate "two" from "years",
and "from" from "a hundred of". And in one chapter the *accents* on
the words decided. Numbers 7:14 reads "one spoon, ten of gold", and
by its letters alone that is how Hebrew writes "eleven". The accent
on "one" is a stopping mark at all twelve spoon-verses, and it joins
forward at every true eleven in the Bible; the chapter's own total,
a hundred and twenty for twelve spoons, closes only at ten each. The
marks on the page are a parse instrument, and the text's own
arithmetic is the proof.

**The clock runs backward on the page, and the tradition says so.**
Numbers opens on the first day of the second month of the second
year. Eight chapters later:

> "And the LORD spoke to Moses in the wilderness of Sinai, in the
> second year after their going out of the land of Egypt, in the
> first month, saying:" (Numbers 9:1)

The first month comes before the second, and the page has them the
other way round. The Talmud states the rule on exactly these two
verses: "there is no earlier and later in the Torah" (Pesachim 6b).
The program's clock, which moves only on a date the text states,
meets this as a *retrograde* marker: the Passover of chapter 9 is
dated in the first month, and the counter, already standing in the
second, is not moved back. Chapter 7 does the same a month earlier
still — "on the day Moses finished setting up the tabernacle" — so
the twelve princes' offerings are twelve dues written into a past the
counter has already walked. On the whole tape, 157 dates now move
the clock: 125 forward, 15 stated as a paragraph's closing total, 17
backward.

Where the text gives no date, the tradition's own day-tables are
taken as data and graded. A page of the Talmud (Taanit 29a) lays the
wilderness spring end to end — three days' march, a month of quail,
seven days for Miriam, the spies back on the ninth of Av — and the
program runs the text's own durations as timers between those days.
Two land exactly. Two land a day or two late, because the tradition
counts a span with its first day in and a timer counts the days that
pass; the page confesses the same slip about itself ("forty days
minus one"). The program reports each miss as a DIVERGE with the
reason, and never smooths it.

And the book's largest timer runs across the whole book. Numbers
14:34:

> "By the number of the days in which you spied out the land, forty
> days, a day for a year, a day for a year, you shall bear your
> iniquities, forty years, and you shall know My displeasure."

Deuteronomy 2:14 subtracts for itself — "thirty-eight years" from
Kadesh to the brook Zered — and the difference is the two years
already gone when the decree fell, which is exactly the clock's year
at that verse. The timer was set in the second year and fired in the
fortieth, on the walk from Aaron's death, whose date the itinerary
of chapter 33 states to the day. The tape's clock ends on the first
day of the sixth month of the fortieth year, in the year 2488 from
creation.

**The run halts on a case no rule decides — and the answer becomes
law.** Numbers 15:34:

> "And they put him in custody, because it had not been declared
> what should be done to him."

Four times in the Torah the story stops because the library cannot
answer: the blasphemer (Leviticus 24), the men unclean at Passover
(Numbers 9), the man gathering wood on the Sabbath (Numbers 15), and
the daughters of Zelophehad (Numbers 27 and 36). The text says so in
its own words each time — "until it be declared", "stand and I will
hear", "Moses brought their judgment near". The program was built to
halt there. It has a DOCKET: when a case arrives that no rule
decides, the case is written on the docket and the man in custody,
and nothing more is written until the text's answer verse arrives.
That verse installs a rule — sometimes a whole new law, sometimes a
cell inside a law that already stood (the Sabbath's death penalty
was Exodus's; only the *mode* was missing) — and the ledger records
which case installed which law. The program's own answer to "what
rules has the tent installed", as it prints today:

```
case_output = rule_for_the_generations (the running setting): rules installed 7 — law_lev24 on the_tent_of_meeting at Lev 24:13-14; law_pesach_sheni on the_tent_of_meeting at Num 9:9-14; law_sabbath:death_run on the_tent_of_meeting at Num 15:35; law_balak:zealot on the_tent_of_meeting at Num 25:10-13; law_zelophehad on the_tent_of_meeting at Num 27:6-11; law_zelophehad:tribe_transfer on the_tent_of_meeting at Num 36:5-9; law_korach:stranger_incense on the_priesthood at Num 17:1-5; THE FORK provisional_edict: no rule_installed would be written — the instance's verdict alone
```

Seven rows. Four are the four cases. A fifth is the tribe's second
plea about the daughters (Numbers 36), which does *not* halt — the
rule is already in force and the plea only bounds it. A sixth is the
zealots' rule at Phinehas's spear, installed by a deed with no halt
and no docket. The seventh is the ban on strangers' incense, written
into the priesthood's own account from Korach's censers. And the
last clause records the tradition's own dispute about what such an
output is — a rule for the generations, or an edict for the instance
— as a setting, with the other arm named.

```
   THE TAPE ──▶ a case no rule decides ──▶ THE DOCKET   (custody; "stand and wait")
                                                │
                                   the text's answer verse
                                                │
                                                ▼
                                  RULE INSTALLED  (a new law, or a cell in an old one)
                                                │
                                                ▼
                            the next such case is decided by the library
```

This is the point at which the program stopped being a list of
specifications and became a loop with memory: the code is not fixed
before the run. A case the run cannot answer changes the library,
and the next such case is answered by the library.

Two instruments came with it. The CURSOR replays the tape from the
beginning to the left edge of a verse that carries a date, and
stops; the record it writes must be byte-for-byte the same as the
full run's up to that point, or the replay is refused. And a
SCENARIO is a case put to the live world at such a point *before*
the text's answer is read: the daughters' own argument (the
Talmud's, at Bava Batra 119b) was run at the left edge of Numbers
27:5 and graded against the answer sheet before 27:6 was on the
tape.

**A law from one book acts in another.** Exodus 31:14:

> "And you shall keep the Sabbath, for it is holy to you; those who
> profane it shall surely be put to death, for whoever does work on
> it, that soul shall be cut off from among its people."

The Sabbath rule was installed at that verse. Through the rest of
Exodus and all of Leviticus no act on the tape profaned a Sabbath.
At Numbers 15:32 one did, and the Exodus rule fired for the first
time; the case's output supplied only the mode. The ledger row says
who wrote it (the row as the program prints it, its verse text cut
short):

```
effect=labor_barred | ledger_op=block | value=detaching | written_by=law_sabbath | verse=Num 15:32-33
```

The incense altar's "no strange incense" (Exodus 30:9) wrote on
Korach's two hundred and fifty men the same way. If the rules worked
only inside their own book, the program would be a shelf of separate
programs; Numbers is the proof that they are one.

**A debt can wait a whole book.** The servant of section 5 owed six
years, and the program set a timer. A command owes a *run*, and the
program writes it as an open entry — a debit — closed when the text
narrates the doing. Exodus 30:12's "when you take the count" is
closed at Numbers 1:19. "Tomorrow turn and journey by the way of the
Red Sea" (14:25) waits seven chapters and is closed at 21:4. And two
commands in the book's last law chapter wait past the Torah's end:

> "And the cities shall be for you a refuge from the avenger, so
> that the manslayer does not die until he stands before the
> congregation for judgment." (Numbers 35:12)

The Levites' forty-eight cities and the six cities of refuge are
given in Joshua 20 and 21; Caleb's Hebron and the daughters'
holding are given there too. On the tape at Numbers' end, Israel's
account carries fourteen commands, seven of them open — open *by
design*, each with the verse that will close it named on the entry.
The ledger holds a promise against a run in a later book, as it
holds the promises of Exodus 6:6-8 against the verses that keep
them.

**A term that ends at a death is not a timer.** Numbers 35:25 and
35:28:

> "And the congregation shall deliver the manslayer from the hand of
> the avenger of blood, and the congregation shall return him to his
> city of refuge, where he had fled; and he shall dwell in it until
> the death of the high priest, who was anointed with the holy oil."

> "For in his city of refuge he shall dwell until the death of the
> high priest; and after the death of the high priest the manslayer
> shall return to the land of his possession."

Compare the servant. His term had a length, so the program could ask
the calendar for the day and set a timer. The manslayer's term has
an *end* but no length: nobody knows when the high priest will die.
So the program sets no timer. It writes an open entry that carries
the name of the priest in office — Eleazar, named by a call into the
law of chapter 20, where he took the office at Aaron's death — and
the entry is closed when the event "the high priest died" arrives,
and only the entries carrying *that* priest's name close. Here is the
program's own record, from the refuge law's test world (its clock
counts days from the exodus; the case is the Talmud's at Makkot 11a):

```
   day 14224   EVENT   a killer's case is brought      (the manslayer; the term asked)              [Numbers 35:24-25]
               ── the refuge rule fires ──
   day 14224   WRITE   dwells in refuge   on the manslayer   value: eleazar (the high priest in office)   open
               (no timer is set — the text gives no day)
   day 14231   EVENT   the high priest died            (Eleazar)                                    [Joshua 24:33]
               ── the refuge rule fires again ──
   day 14231   CLOSE   dwells in refuge   on the manslayer   closed by the death, by the name the entry carried
   day 14231   WRITE   returns to the land of his possession   on the manslayer                     [Numbers 35:28]
```

A second manslayer in the same test, sentenced under Phinehas, stays
in his city through Eleazar's death and goes home only at Phinehas's
— the Mishnah's own row (Makkot 2:6), and the reason the entry is
keyed by a name rather than by the office.

**The world's headcount is a table the rules write, and the text
audits itself.** The book is called Numbers because it counts the
people twice, in the second year and in the fortieth. The program
keeps the count as a table — tribe by tribe, family by family — and
only a rule consuming a verse may write a row; a hand may not. The
two totals, 603,550 and 601,730, come off the verses by the reader
above, and the difference per tribe is *declared*, never explained
away: Simeon falls by 37,100; the plague at Peor (25:9) accounts for
24,000 by a call into the Balak law; the remaining 13,100 is written
down as unexplained. Then the text's own audit clause:

> "And among these there was not a man of those numbered by Moses
> and Aaron the priest, who numbered the children of Israel in the
> wilderness of Sinai." (Numbers 26:64)

> "For the LORD had said of them: they shall surely die in the
> wilderness. And there was not left of them a man, except Caleb son
> of Jephunneh and Joshua son of Nun." (Numbers 26:65)

The program checks that clause against its ledger: of the first
roll's named dead, five carry a death entry, and two — Nadab and
Abihu — have no account at all, because the fire that took them
wrote on no person. The gap is named, not filled.

The text audits itself in more places than this. It writes its
registers with a header and a footer; it closes a command with a
receipt — "as the LORD commanded Moses", with its longer form,
sixty-nine times in the Torah; and it states a sum after a list.
The program has a gate that reads every one of those off the text
(110 count lines, 69 receipts, 9 footers, 18 register headers) and
checks the ledger and the table against them. Nine such sums were
measured: seven close, and two differ where the tradition supplies
a hidden row — both already on the record as declared divergences.

**Where the text is divided, the machine holds the row open.**
Numbers 16:32 says the earth swallowed "every person who belonged to
Korach" and does not name Korach; 26:10 names him among the
swallowed; 16:35 has the fire take the two hundred and fifty. The
Talmud argues both ways on one page (Sanhedrin 110a). The program
does not choose. Korach's death entry carries a row with three arms
and the value *open*, and the check on it prints DIVERGE, declared
in advance. The same for the "ten times" the people tested the LORD
(14:22): the ledger's counter stands at seven, because the calf and
the quail were written under other effects, and the check says so.
OPEN is a status the program is allowed to hold; it is never allowed
to pretend. Of the 135 checkpoints on the fourth book, 127 match and
8 diverge, every one of the eight declared before its run and filed
with its reason.

**The hand miscounts; the script counts.** Every sitting of the walk
logged the same lesson. Before each run the ten numbers of the run —
events, timers set, fired, cancelled, past dues, ledger writes,
rules fired, accounts, allowed double writes, closes — were
predicted in the design and typed into the runner, and the run had
to reproduce them. Then the tape was run a second way, with the
newest chapter's lines removed, and had to reproduce the previous
sitting's ten exactly. Where a prediction missed, the miss was read
as evidence: an account the model thought new had been on the ledger
since the golden calf; a party that is only the *other side* of an
entry gets no account of its own. At Numbers' close the running
world holds 1,279 events, 1,527 ledger writes, 121 closes and 318
accounts, and the whole tape's 208 checkpoints print 185 MATCH and
23 DIVERGE, each divergence declared.

If you take one thing from the fourth book: **the library is not
finished before the run.** A rule from an earlier book fires on a
later book's act; a case the library cannot answer installs a rule
into it; a command's run may lie a book away; and a term may end at
an event nobody can date. The ledger holds all of that as open
entries with their closing verses named — and reports, without
smoothing, where the text and the tradition disagree.

## 10. Mini-lab: add a third event to the same map

Twenty minutes with a pencil. The event is "an ox gores," and the
law is Exodus 21:35-36:

> "And when one man's ox injures another's ox and it dies, they sell
> the live ox and split the money, and they also split the dead one.
> But if it was known that the ox was a gorer from before, and its
> owner did not guard it — he must pay ox for ox, and the dead one is
> his."

On the map from section 3, draw the path of this event, and answer
four questions:

1. **Which box holds "known to be a gorer"?** It is not in the event
   and not in the law. (Hint: it is a flag, and flags live on
   accounts.)
2. **Which account carries it — the owner or the ox?** The text says
   "the ox was a gorer." Follow the text.
3. **What does the third goring change?** The tradition's rule is
   that an ox becomes a known gorer after three times. Draw three
   arrivals of the same event. What is written the first two times,
   and what is written after the third that was not there before?
4. **What does the fourth goring write, and why is it different?**

When you have drawn it, compare with the program's own test: the
goring event is submitted four times for the same ox. The first
three each write a half payment on the owner's account; the third
also flips a flag on the ox — "forewarned"; the fourth writes a full
payment, because the law now reads the flag. That is a machine with
memory: the same event, arriving into a different ledger, producing
a different ruling — and the memory lives on the ox, exactly where
the text put it. You have now drawn every kind of thing in the
program: an event, a rule, a flag, an entry, and a ruling that
depends on what was written before.

## 11. Where to look next

Now open the drawers, in this order:

- **THE_CLOCK.md** — how the machine keeps time, taught from the
  flood's dates, Isaac's eighth day, and a Hebrew number-word.
- **THE_EFFECTS.md** — the ledger side: what a ruling is allowed to
  change, one effect at a time, with the verse for each. The
  servant's clock and the land's overdue rests are worked in full.
- **THE_LINKS.md** — the wiring side: how the law programs call one
  another, with the verses on both ends and the tradition's record
  of each link.
- **TIME.md** — the evidence for the clock: every verse and every
  Talmud row about calendars, quoted whole.
- **CHRONICLE.md** — the design for watching all of this run on one
  screen.
- **World/step9/NUMBERS_WALK.md** — the fourth book's walk, one
  section per sitting: the design written before the code, and the
  record as built after it. **World/step9/THE_TENT.md** holds the
  four cases; **World/step9/THE_LOOP.md** is the running simulation's
  own map — the journal, the installation of laws, the cursor,
  scenarios, the register gate.
- **What_Numbers_Taught_The_Machine.md** and
  **What_Numbers_Does_For_The_Simulation.md**, at the repository's
  root, each with a listening copy beside it — two long tutorials on
  the fourth book, every verse quoted whole and the machine's own
  lines beside them.
- **The other files in this folder** (README, NARRATIVE,
  FUNCTION_CATALOG, DEPENDENCIES, STATE_MACHINES) are the engineering
  map, written for the record rather than for a first reading.
- **The code itself:** World/step9/world_engine.py (the clock, the
  accounts, the rules, the timers, the fence); the fifty-seven span
  programs beside it; the effects registry; the calendar's parameter
  file.

If you take one thing from this tour: the whole program is
**event → rule → ledger, with time in between**, and every rule in
the library is written so that a verse supplies the event, a verse
supplies the law, and a verse supplies the change.
