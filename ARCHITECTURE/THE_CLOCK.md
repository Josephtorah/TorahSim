# THE CLOCK — how the machine keeps time, taught from three examples and a fourth book

**A tutorial (rewritten 2026-09-07 after the clock was built and the
three books were run in order; the fourth book's section added
2026-09-13, after Numbers ran on the same clock).** This used to be a design proposal.
The design was argued out between two working sessions, ruled on by
the owner, and built the same day (the record of the build is
World/step9/CLOCK.md; the record of the first full run is
World/step9/REPORT_SEQUENTIAL_RUN.md). What follows explains what
was built, for a reader who knows nothing about this project, the
Bible's chronology, or programming.

*Verses are given in plain modern English, rendered from the Hebrew
and checked against it. Where one Hebrew word matters it is shown
once, with its English beside it. Every verse cited is quoted whole.*

---

## The problem, in one paragraph

This project has turned the laws of the Bible into a program: a set
of rules that watch events and write down what each event changes —
who owes what, who is free, what is due when. Many of those laws are
about TIME. A servant works six years and goes free in the seventh.
A newborn boy is circumcised on the eighth day. Every fiftieth year
is a jubilee, when land goes back to its family. So the program needs
a clock. But the Bible is a text, not a calendar: it tells you the
order things happened in, and only sometimes tells you how much time
passed. The question this document answers is: **how can a machine
keep an honest clock when its only source of time is a book?**

The short answer, which the rest of this document unpacks: **the
machine's clock moves only when the text states a date.** Between two
stated dates the clock stands still, the machine says so, and
nothing is invented.

---

## Example 1 — reading a number off the Hebrew

Before a clock can move, the machine must read the numbers the text
gives, in Hebrew, without a person typing them in. This sounds
trivial and is not. Genesis 5:6 says, in the Hebrew word order:

> "And Seth lived five years and a hundred years, and he begot
> Enosh."

"Five years and a hundred years" is ONE number: 105. The Hebrew
writes the units first, then the hundreds, with the word "years"
after each part. A reader knows this instantly; a machine has to be
told that the word "years" keeps the number open across its parts.
But not every "and" joins numbers. Exodus 24:18 says Moses was on the
mountain "forty days and forty nights" — that is two numbers, not
eighty of something. And Genesis 8:5 names the tenth month twice in
one verse ("the waters kept decreasing until the tenth month; in the
tenth month, on the first of the month, the tops of the mountains
appeared"), so a careless reader counts a date that is stated once.

The machine has a small reader for these number-words — a PARSER —
and every number it uses is read from the Hebrew by that parser and
read again each time the program runs. Sixty-eight numbers on the
first run of the three books; 157 by the end of the fourth, every
one re-read at each run — and the fourth book, which counts a
people, taught the parser a whole grammar of its own (THE_TOUR.md,
section 9). When the parser was first written it got two
wrong (it skipped a feminine word for "two"); those were caught by
checking every verse before any date was trusted. The lesson for the
whole design: **a date the machine uses must be read from the text
by a program, never typed by a person.** A typed number cannot be
checked; a parsed one is checked every run.

---

## Example 2 — the flood's dates: how the clock moves

Now the clock itself. The story of Noah's flood is the first place
the Bible gives dates to the day. Genesis 7:11:

> "In the six hundredth year of Noah's life, in the second month, on
> the seventeenth day of the month — on that day all the springs of
> the great deep burst open and the windows of the sky were opened."

That is a full date: a year (counted by Noah's life), a month, and a
day. The machine calls such a stated date a MARKER. A marker is the
only thing that moves the clock. When the program reaches this verse
it advances its counter to that day, and every duty that was due
before that day comes due as the counter passes it.

The next markers in the story:

> Genesis 8:4 — "And the ark rested, in the seventh month, on the
> seventeenth day of the month, on the mountains of Ararat."

> Genesis 8:13 — "And it was in the six hundred and first year, in
> the first month, on the first of the month, that the waters dried
> from off the earth."

> Genesis 8:14 — "And in the second month, on the twenty-seventh day
> of the month, the earth was dry."

Look at what these four dates force. From the second month, day 17,
to the seventh month, day 17, is five months. The text says elsewhere
(Genesis 7:24, 8:3) that the waters prevailed "a hundred and fifty
days" — five months of thirty days each. But the tradition's received
length of a month (explained below) is twenty-nine and a half days,
which the machine rounds to months of thirty and twenty-nine days
alternating — and five of those months come to 147 days, not 150. The
machine reports this as a DIVERGENCE: the text's own arithmetic and
the tradition's month length disagree by three days here. The gap is
real, the tradition itself knows it, and the machine prints it rather
than hiding it. That is the whole method in miniature: the text
supplies a number, the machine computes, and a mismatch is reported,
never repaired.

The dates also settled a design question nobody had asked. "The six
hundredth year of Noah's life, second month" is followed, ten and a
half months later, by "the six hundred and first year, first month."
If a person's year turned on his birthday, that could not happen —
the year would turn wherever the birthday fell, not at the first
month. So the machine counts a person's age the way the text counts a
king's reign: **a person's year turns at the New Year**, not on a
birthday. That one rule, forced by these verses, made the entire
chronology of Genesis come out in the tradition's shape.

---

## Example 3 — Isaac's eighth day: what a timer is, and a mistake it exposed

A TIMER is a duty that falls due on a later day. Genesis 21:4:

> "And Abraham circumcised Isaac his son when he was eight days old,
> as God had commanded him."

When the machine reads Isaac's birth, the rule for circumcision sets
a timer: due on the eighth day. When the day arrives the timer
fires, and the duty is written in the ledger as due. When the act
itself is read from the text — Abraham circumcised him — the duty is
closed. Open, then closed: that is what a ledger of duties looks
like.

Here is what happened when all three books were run in order on one
clock. Before that run, each story had run in its own little test
world, and the test scripts had lines like "move ahead eight days"
typed by hand between the birth and the circumcision. On the one
shared clock there is no such line — the clock moves only at a
marker, and Isaac's birth and circumcision fall in a stretch with no
stated date between them. The result: the act arrived before the
timer fired, and the duty stayed open. The machine reported it. On
inspection, the rule had counted the eighth day one day late — birth
plus eight, when "the eighth day" counts the birthday itself as day
one, so the due day is birth plus seven. The hand-typed "move ahead
eight days" had hidden the error for weeks. A second case was worse:
Tamar's wait "until Shelah grows up" (Genesis 38:11) has no number in
the text at all, and an old script had simply invented "four days."
On the shared clock that invented four-day duty came due at the next
stated date — sixty years later.

Two lessons, both now rules: **the eighth day counts the first day**
(a one-line fix, scheduled); and **never advance the clock by a typed
interval** — if the text gives no number, the machine must leave the
duty open and say so, and an invented interval now shows up as a
hole instead of passing silently.

---

## The rules, now that you have seen them work

**1. The clock counts days.** One counter, in days, from a starting
day. Years, months, and the special cycles are computed FROM the day
count by a calendar inside the machine. Before this was built, the
counter had a different unit in each test world (some counted days,
some years), and a servant's six-year term could not exist in the
same world as a seven-day purification. Now they can.

**2. Every number in the calendar has a source.** The calendar's
numbers are not written into the program; they sit in a separate
data file, nineteen rows, each with where it comes from and which
kind of source it is. The important ones:

- *The length of a month.* Received, not computed: "Thus I have
  received from my father's father's house: the renewal of the moon
  is not less than twenty-nine days and a half, and two-thirds of an
  hour, and seventy-three parts" (Babylonian Talmud, Rosh Hashanah
  25a — a teacher named Rabban Gamliel stopping a court from
  declaring a new month a day early, and citing the number his family
  had handed down). The machine rounds this to months of thirty and
  twenty-nine days, alternating, and labels the rounding as its own.
- *The month a year begins.* From the text: "This month is for you
  the head of months; it is the first for you of the months of the
  year" (Exodus 12:2, spoken in Egypt before the exodus). But the
  tradition keeps four different new years for four different
  purposes — kings and festivals from the spring month, the count of
  years and jubilees from the autumn month, and two more (Mishnah
  Rosh Hashanah 1:1, "There are four new years"). The machine carries
  that table as data, not as a rule of its own.
- *Leap years.* A lunar year is eleven days shorter than a solar
  one, so a thirteenth month is added some years. The tradition's
  rule: the court added it on three grounds — the spring grain, the
  fruit of the trees, and the season — needing two of the three
  (Sanhedrin 11b). The machine cannot see grain ripen, so it runs the
  season ground alone, from a modeled solar year, and marks every
  date that depends on it as MODELED. (The old fixed formula this
  produces — seven leap years in every nineteen — is the frequency
  the tradition later adopted; the machine arrived at it from the
  threshold alone.)
- *The jubilee's cycle.* From the text: "seven sabbaths of years,
  seven times seven years… forty-nine years" (Leviticus 25:8) and
  "you shall sanctify the fiftieth year" (25:10).

Anything the machine could not find on its shelf of sources is
marked OPEN, and the document says what would settle it.

**3. Time is counted from several starting points at once.** The
text dates things "in the six hundredth year of Noah's life," "in
the second year after leaving Egypt," "in the fourth year of
Solomon's reign." These are different ERAS — different starting
points on the one line of days. The machine keeps a table of them:
the creation (its own day zero), the exodus (set when the text says
"this month is for you the head of months"), and a life era for every
person whose birth the text dates — twenty-nine eras were set on the
three-book run, all by markers, never by a typed day. Two more (the
years of kings, and the count "by the kings of Greece" used in
exile) are in the table with their sources, marked as not yet used
because no run reaches them.

**4. Three kinds of marker.** A FORWARD marker moves the clock
ahead: "Seth lived a hundred and five years and begot Enosh."
A CLOSING marker is a life's total — "all the days of Seth were nine
hundred and twelve years, and he died" (Genesis 5:8) — which the text
places at the end of a paragraph even though the next paragraph
starts earlier in time; the machine logs it at its computed day
without moving the clock. And a BACKWARD marker is a date earlier
than the clock already stands: the book of Numbers dates chapter 9
to the first month and chapter 1 to the second, though chapter 1
comes first on the page. The Talmud has a rule for this (Pesachim
6b): "there is no earlier and later in the Torah" — the order of the
page is not the order of time. The machine leaves the clock where it
is, gives the event the date the text states, and computes any
duties from that stated date.

**5. Between two markers, time is undated.** An event that falls
between two stated dates is given the earliest possible day and
carries a note: "somewhere between year 2049 and year 2089." Any duty
it sets carries the same note. When a checkpoint tests such a date,
it tests against the interval, not a point.

**6. The clock never invents an event.** A rule may write duties and
statuses and set timers; it may never put a new event on the tape.
Events come from the text only. When a timer fires, it writes a
status (say, "this is the fiftieth year") that other rules can read —
that is how one law's consequence can trigger another law without
anyone inventing history.

---

## The jubilee: decided by the act, not the date

This one deserves its own section because it changed the design
twice. Every fiftieth year is a jubilee: land sold since the last one
goes back to its family, and Hebrew servants go free. Leviticus
25:9-10:

> "Then you shall sound a loud horn, in the seventh month, on the
> tenth of the month; on the Day of Atonement you shall sound the
> horn throughout your land. You shall make the fiftieth year holy,
> and proclaim freedom throughout the land to everyone living in it.
> It is a jubilee for you: each of you returns to his family land,
> each to his family."

The obvious design: a timer fires in the fiftieth year and frees
everyone. The tradition says it is not that simple. The oldest
commentary on Leviticus records a dispute over what makes the year
count as a jubilee at all: one teacher says it is a jubilee even if
the land was not released and the horn was not sounded — but not if
the servants were not sent free; another says the reverse: not
without the horn (Sifra Behar, Chapter 2, row 4). And the Talmud adds
a condition of a different kind: the jubilee ceased when the tribes
east of the Jordan were exiled, because the verse says "freedom to
ALL its inhabitants" — all, not most (Arakhin 32b). So whether a
given fiftieth year is a jubilee depends on ACTS done in that year
and on the STATE of the people — things a timer set fifty years
earlier cannot know.

The machine now does it in three layers. The count's timer writes
only the fact nobody disputes: "the fiftieth year has arrived."
A sale's timer writes only the ENTITLEMENT: "this field is due to go
back." The RELEASE itself is written only when the proclamation — a
real act in the text — is read, and the rule that reads it checks
the three conditions: was the horn sounded, were the servants sent
free, are all the inhabitants on the land. Where the teachers
disagree, the machine writes both answers side by side with each
teacher's name, never a silence. And on the real history there is no
verse that says a jubilee was ever proclaimed — so the machine writes
the years and the entitlements and no release. That is exactly what
the tradition records happened.

---

## What came out when the three books ran in order

With the clock built, Genesis, Exodus, and Leviticus were run
start to finish on one world, every rule watching (thirty-eight at
that first run; forty-three by the next day, when the rest of
Genesis's stories joined the tape), the clock walked by the dates
the text states — sixty-eight on the first run, 129 by the next. The
tradition's whole chronology came out of the text's numbers alone,
under the one convention the flood forced (a life's year turns at
the New Year):

- The flood in the world's year 1657. The tradition's count says
  1656 — one year lower everywhere, because it counts Adam's first
  year as year zero. The machine prints the difference once and
  moves on.
- The ark resting 147 days after the flood began (the text says 150 —
  the divergence above).
- The earth dry a year and ten days after the flood began — the
  text's own interval, reproduced.
- The exodus 400 years after Isaac's birth, as Genesis 15:13 promises
  for "your seed" and 21:12 defines the seed ("in Isaac shall seed be
  called to you"); and 210 years after Jacob's descent into Egypt.
  Exodus 12:40 says 430 years "in Egypt." The machine reports the
  divergence, and the Talmud records the explanation: the elders
  translating for King Ptolemy wrote "in Egypt and in other lands"
  (Megillah 9a).
- The tablets broken exactly forty days after Moses went up on the
  seventh of the third month — landing on the seventeenth of the
  fourth month, the fast day the Mishnah names for it (Taanit 4:6),
  the arithmetic the Talmud works out (Taanit 28b).
- The priests' seven days of installation ending on the very day the
  Tabernacle was raised (Exodus 40:17; Leviticus 8:33, 9:1) — the
  Talmud's "that day took ten crowns" (Shabbat 87b).

Fourteen checkpoints of this kind were declared before the run and
computed by it; every one came out as the design predicted, the
divergences included. The Isaac and Tamar findings above came from
the same run.

---

## What the next look found: four more gaps, and how each was built

The day after the first run, a third working session read the
engine and the run with the owner and named four things the account
of time still lacked. The two sessions that built the clock argued
each one through and agreed, and all four were built the next day,
2026-09-08, as the clock's open-items sitting. In plain words, the
gap as it was named, and then what was built:

**1. Laws should switch on when the text gives them.** Today every
rule watches from the first day of creation. Nothing turns the law
of circumcision on at Abraham's covenant, or the ordinances on at
Sinai. That has been harmless only by accident — and not entirely:
the program already pays for it by hand, with a naming trick that
stops the eighth-day rule from firing on the genealogies of Genesis.
The fix fits the design: the installing act (the covenant's blood,
the priests' sprinkling) writes "in force" on an institution's
account, and a rule reads that before it fires. And because the
tradition records the opposite position too — "Abraham kept the
whole Torah before it was given" — it will be a setting with both
arms, printed as a fork, like the jubilee.
*As built:* every law now declares two verses — the one that speaks
it and the act that switches it on — and the installing acts write
"in force" on the institutions' accounts; sixty-two rules today,
twenty-two on from the start, thirty-nine by an act, one pending.

**2. Undated scenes are placed by page order, silently.** An event
with no stated date is put at the last stated date before it — a
reasonable guess, but an unlabeled one. The covenant between the
pieces (Genesis 15) is dated by the tradition to a time *before* the
chapter that precedes it on the page, and the machine flagged that
reading as a divergence when the real fault was its own unlabeled
guess. The fix: every placement gets a label (by page order; fixed
by the text; placed by a recorded reading), and the covenant's year
becomes a setting with the two readings the shelf records — one
commentary dates it to Abraham's eighty-fifth year, the chronology
to his seventieth — printed as the tradition's fork, not ours.
*As built:* every marker and every event carries its placement —
fixed by the text, placed by a recorded reading, or by page order —
and the covenant runs at both readings, the seventieth year meeting
the exodus to the day and the eighty-fifth missing by fifteen,
printed. On the running world today: 102 markers fixed by the text,
40 placed by a reading; 1,133 events by page order.

**3. Two ways of counting a year.** The machine's year is an ordinal
label ("in the six hundredth year"); the tradition's count of years
from creation is completed years ("a son of six hundred years") —
and the text itself uses both idioms side by side. The fix is the
cheapest of the four: keep both renderings from the one day count,
print the completed count where the tradition's numbers are
compared, and the "one year lower" remark becomes a matching
checkpoint instead of a note.
*As built:* two columns from one day count — the label and the
elapsed year — and the Talmud's own numbers (Avodah Zarah 9a:
Abraham fifty-two in the year two thousand) match under the elapsed
column.

**4. The text keeps several counting systems at once.** Kings'
years, people's ages, animals' ages, the jubilee's boundary year,
"the eighth day" counting the first day — each has its own rule for
where a year or a day begins and ends, and the tradition records
each rule. The fix: every date and duration carries its counting
system as a tag, the tags enter as data rows with their sources,
and every place a count in one system is joined to a count in
another becomes a checkpoint the machine generates. The template
is a famous collision the tradition itself resolved: Nehemiah dates
two events to "the twentieth year" in an order that only works if
the king's year begins in autumn — and the Talmud reads it exactly
that way.
*As built:* the text's own day-words — evening, night, midnight,
dawn, morning, noon, between the evenings, sunset — are stamped on
the events that carry them, in the order Genesis 1:5 gives; the
Talmud's two day-orders are data; and the counting idioms for
people, kings, animals and trees are rows with their sources.

---

## The fourth book: the clock in the wilderness

Between 2026-09-09 and 2026-09-13 the book of Numbers was walked from
its first verse to its last and put on the same tape as the three
books before it, and the clock walked with it — from the second year
after the exodus to the fortieth. Numbers is the book where the clock
is hardest: it dates a chapter before the chapter that precedes it,
it leaves whole stretches undated, it counts a span in days and then
turns the days into years, and it ends one of its terms at an event
nobody can date. Here is what it did to the clock, in eight parts,
each with its verse. The Talmud passages named are quoted whole in
TIME.md, section 12.

**1. The page runs backward, and the tradition says so.** The book
opens on the first day of the second month of the second year — day
894,728 of the world's count, the marker that rule 4 above already
uses. Eight chapters later:

> "And they kept the Passover in the first month, on the fourteenth
> day of the month, between the evenings, in the wilderness of
> Sinai; according to all that the LORD commanded Moses, so the
> children of Israel did." (Numbers 9:5)

That is seventeen days *before* the book's opening date. The Talmud
puts the question on exactly these two verses and answers it in one
sentence (Pesachim 6b): "there is no earlier and later in the Torah."
The machine's BACKWARD marker is that sentence made mechanical: the
Passover's events are dated to the fourteenth of the first month, and
the counter, already standing on the first of the second, is not
moved. Chapter 7 does it again, a month earlier still:

> "And it was on the day Moses finished setting up the tabernacle,
> and anointed it and sanctified it and all its vessels, and the
> altar and all its vessels, and anointed them and sanctified them —"
> (Numbers 7:1)

"The day Moses finished setting up" is Exodus 40:17's day, the first
of the first month; the machine found the phrase at exactly one seat.
So the chapter is dated a month before the census, and its twelve
day-heads — "on the first day," "on the second day," through "on the
twelfth day" — are twelve more backward markers. On the whole tape
today, 157 stated dates move the clock: 102 fixed by the text itself,
40 placed by a recorded reading of the tradition, 15 closing totals
of the kind rule 4 calls closing markers — and among them seventeen
backward: one in Genesis, one in Leviticus, and fifteen in Numbers.

**2. A schedule written into the past.** Numbers 7:11-12:

> "And the LORD said to Moses: one prince per day, one prince per
> day, they shall bring near their offering for the dedication of the
> altar. And he who brought near his offering on the first day was
> Nahshon son of Amminadab, of the tribe of Judah."

When the machine reads that command its counter already stands past
all twelve days. The rule for the command asks the clock for the
anointing day and writes twelve dues, one per prince, at that day
plus its count — every due already past — with the counter unmoved.
The machine's log keeps a class for such a line, a RETRO-WRITE, and
the tape carries exactly twelve. The check: each due equals the day
the text itself stamps on the verse, 7:12 through 7:78. The Talmud
(Moed Katan 9a) reads the twelve day-heads as one continuous run
with a Sabbath inside it, and the machine's twelve dues run through
one.

**3. The tradition's day-table as data, and the miss it exposes.**
The book's next date is the departure from Sinai:

> "And it was in the second year, in the second month, on the
> twentieth of the month, that the cloud lifted from over the
> tabernacle of the testimony." (Numbers 10:11)

Forty-nine days after the tabernacle was raised — thirty of the first
month and nineteen of the second. The design had typed fifty; the
first run read forty-nine, and the record keeps both, because the
difference is the whole lesson of this part. The Talmud (Rosh
Hashanah 3a) uses this verse with Exodus 40:17 to prove that the
exodus era's year does not turn in the second month — both dates are
"the second year" — and the machine's era table says the same.

From here the text gives no date for a long stretch, and the
tradition supplies one. A page of the Talmud (Taanit 29a) lays the
spring end to end: the twentieth of the second month, three days'
journey, a month of eating flesh, seven days for Miriam, the spies
sent on the twenty-ninth of the third month and back on the ninth of
Av. The machine takes those days as READING-PLACED markers — labeled
so, never as the text's own — and runs the text's own durations as
timers between them:

> "And they journeyed from the mountain of the LORD a three days'
> journey, and the ark of the covenant of the LORD journeyed before
> them a three days' journey, to seek out a resting place for them."
> (Numbers 10:33)

> "You shall not eat one day, nor two days, nor five days, nor ten
> days, nor twenty days — but a month of days, until it comes out of
> your nostrils and becomes loathsome to you, because you have
> rejected the LORD who is among you, and wept before Him, saying:
> why did we come out of Egypt?" (Numbers 11:19-20)

> "And Miriam was shut out of the camp seven days, and the people did
> not journey until Miriam was brought in." (Numbers 12:15)

> "And they returned from spying out the land at the end of forty
> days." (Numbers 13:25)

Two of the four timers land on the tradition's day exactly: the three
days' journey fires on the twenty-third of the second month, and
Miriam's seven on the twenty-ninth of the third. Two land late: the month of flesh by
two days, the forty days by one. The reason is one reason, and the
page confesses it about itself. The tradition counts a span with its
first day in; a timer counts the days that pass. The Talmud's own
arithmetic on the spies comes to "forty days minus one," and Abaye
repairs it by making that year's fourth month a full thirty days.
The machine carries Abaye's full month as the other arm of a calendar
row and does not run it — it would move every later date of that year
by a day — and prints the two misses as DIVERGE with the reason,
never smoothed.

**4. A day for a year: the timer that ran across the book.** The
spies' forty days become forty years:

> "By the number of the days in which you spied out the land, forty
> days, a day for a year, a day for a year, you shall bear your
> iniquities, forty years, and you shall know My displeasure."
> (Numbers 14:34)

Deuteronomy 2:14 subtracts for itself — "thirty-eight years" from
Kadesh-barnea to the brook Zered — and the difference is the two
years already gone when the decree fell, which is exactly the era's
year at that verse. The machine set the timer at the decree, due on
the ninth of Av of the fortieth year by the calendar's own
arithmetic, and it stood PENDING through the next two sittings of the
walk, because the tape's last marker then stood eight days short of
it. It fired
when the fortieth year arrived, and the fortieth year arrived on four
markers in one chapter:

> "And the children of Israel, the whole congregation, came to the
> wilderness of Zin in the first month, and the people stayed in
> Kadesh; and Miriam died there, and was buried there." (Numbers
> 20:1)

> "And they journeyed from Kadesh, and the children of Israel, the
> whole congregation, came to Mount Hor." (Numbers 20:22)

> "And Moses stripped Aaron of his garments and put them on Eleazar
> his son; and Aaron died there on the top of the mountain, and Moses
> and Eleazar came down from the mountain. And all the congregation
> saw that Aaron had expired, and they wept for Aaron thirty days,
> all the house of Israel." (Numbers 20:28-29)

> "And they journeyed from Mount Hor by the way of the Red Sea, to go
> around the land of Edom; and the soul of the people grew short on
> the way." (Numbers 21:4)

The first month of which year? The verse does not say, and the
tradition does (Seder Olam Rabbah 9): the fortieth. So the arrival at
Zin and the arrival at Mount Hor are reading-placed, at the first of
the first month and the first of the fourth. Aaron's death is fixed by
the text — thirteen chapters later, in the itinerary:

> "And Aaron the priest went up to Mount Hor at the mouth of the LORD
> and died there, in the fortieth year after the children of Israel
> came out of the land of Egypt, in the fifth month, on the first of
> the month. And Aaron was a hundred and twenty-three years old when
> he died on Mount Hor." (Numbers 33:38-39)

The machine reads that date whole — the fortieth year, the fifth
month, the first day — and marks 20:28 with it. The departure is
that day plus the thirty days of weeping. On the walk between those
two markers, eight days after Aaron's death, the thirty-eight-year
timer set in the second year fell due and fired. Aaron's hundred and
twenty-three is eighty-three plus forty (Exodus 7:7), and Moses'
hundred and twenty is eighty plus forty, both by the same reader.
One thing in the chapter the machine leaves open: the text gives
Miriam's death a month and no day, the tape buries her on the
arrival's day, and the tradition (Seder Olam Rabbah 10) names the
tenth — a DIVERGE by nine days, printed. The Talmud (Rosh Hashanah
2b) uses Aaron's date with Deuteronomy 1:3 — the fifth month and the
eleventh month both "the fortieth year" — to prove that this era's
year does not turn in the autumn; the machine's era table already
said so, and the run reproduces the proof.

**5. Morrows, thirds and sevenths on an undated stretch.** Korach's
chapters carry no date in the text and none on the shelf — the
machine searched the tradition's chronology by script and found no
row — so their lines take the counter's day, labeled PAGE-ORDER. Two
timers inside them are a single day long:

> "and put fire in them and lay incense on them before the LORD
> tomorrow; and it shall be that the man whom the LORD chooses, he is
> the holy one. You take too much upon you, sons of Levi." (Numbers
> 16:7)

> "And it was on the morrow that Moses came into the tent of the
> testimony, and behold, the staff of Aaron for the house of Levi had
> budded: it brought forth buds, and blossomed blossoms, and bore
> ripe almonds." (Numbers 17:23)

Both fire the day after the page-order day, the same rule that
governed "the third day" in Genesis. The heifer's law gives the
machine a longer pair:

> "He shall purify himself with it on the third day and on the
> seventh day, and he shall be clean; and if he does not purify
> himself on the third day and on the seventh day, he shall not be
> clean." (Numbers 19:12)

Those are timers at the day plus three and the day plus seven, and
the war with Midian set six of them on the men of war and the
captives; all six stand PENDING at the tape's end, due three and
seven days past its last marker. And the men unclean at Passover, in
chapter 9, were owed a second Passover "in the second month, on the
fourteenth day" (9:11): the due was set by the calendar at the case's
day, and it fired on the walk to the next marker — the machine's
arithmetic, not a typed day.

**6. Duties keyed to the calendar's own words.** Story 8 of
THE_EFFECTS.md gave the daily lamb a timer with a period of one day.
Chapters 28 and 29 add an offering on every Sabbath, new moon and
festival:

> "The burnt offering of the Sabbath on its Sabbath, beside the
> continual burnt offering and its libation." (Numbers 28:10)

> "And their libations shall be half a hin for the bull, and a third
> of a hin for the ram, and a quarter of a hin for the lamb, of wine.
> This is the burnt offering of the month in its month, for the
> months of the year." (Numbers 28:14)

These periods are not numbers of days; they are calendar words. The
rule sets eight timers on the altar's account, each keyed to a word
the calendar knows — the Sabbath, the month, the first day of
Passover, the day of firstfruits, the first of the seventh month, the
tenth, the first of Sukkot, the eighth day — and each asks the
calendar for its next date when it fires. From the tape's last day,
the first of the sixth month of the fortieth year, the eight dues
fall on the eighth of the sixth month, the first of the seventh, the
fifteenth of the first month of the forty-first year, the sixth of
the third, the first of the seventh, the tenth, the fifteenth and the
twenty-second of the seventh: the same arithmetic the festival rule
of Leviticus 23 uses, asked both ways and matching.

**7. An end without a length, and a day that ends at dark.** Two of
the book's laws end a state without giving a number of days.

> "And the congregation shall deliver the manslayer from the hand of
> the avenger of blood, and the congregation shall return him to his
> city of refuge, where he had fled; and he shall dwell in it until
> the death of the high priest, who was anointed with the holy oil."
> (Numbers 35:25)

The manslayer's term ends at a death nobody can date, so the machine
sets no timer at all: it writes an open entry carrying the name of
the priest in office and closes it when the text records that
priest's death (Story 12 of THE_EFFECTS.md). The vow's law does the
opposite — it gives a clock, but the clock is a boundary, not a
count:

> "But if her husband is altogether silent to her from day to day,
> then he has confirmed all her vows or all her bonds that are upon
> her; he has confirmed them, because he was silent to her on the day
> he heard." (Numbers 30:15)

The Sifrei reads "from day to day" two ways and keeps both: until
nightfall, because the verse itself says "on the day he heard"; or a
full twenty-four hours, Rabbi Shimon ben Yochai's reading of "from day
to day." The machine's timer for the hearing day falls due at the
day's evening boundary — the same boundary as "impure until the
evening" — and the twenty-four-hour reading is the row's other arm,
named and never run.

**8. Replaying the clock to a verse.** The tape can be replayed from
its beginning to the left edge of any verse and stopped there, and
the record the replay writes must be byte-for-byte the same as the
full run's up to that point, or the replay is refused. Two things
about the clock came out of building that. First, every undated
event carries a BOUND — the day of the last stated date before it
and the day of the next one after it — and the right edge is only
known when the next marker arrives; so a replay stopped at a stated
date must close the bounds behind it as the full run would, and a
replay stopped inside a bound is refused, because the full run's
record already holds a right edge the replay cannot know. Numbers
15:32 is such a place; Numbers 27:5, where the daughters bring their
case, is not, and the first scenario ran there. Second, the audit
caught the ledger rewriting its own past: a close was being written
into the entry's original line, so a replay could never match a run
that had closed something later. Since 2026-09-12 a close is a line
of its own in the log, dated, naming the entry and the verse that
closed it, and the original line is a snapshot of the day it was
written. That is what lets the clock say not only when a duty was
opened but when it was closed.

**What the fourth book left the clock with.** 157 stated dates, 29
eras, 66 timers set and 52 fired on the running world, 12 dues
written into the past, and a last day on the first of the sixth month
of the fortieth year — the year 2488 from creation. Of the 135
checkpoints the fourth book declares, eight print DIVERGE, every one
declared before its run: the two inclusive-count misses above,
Miriam's day, and five that are not the clock's.

---

## What is still open, and what would settle each

- **Where the jubilee count starts.** At the entry into the land, or
  fourteen years later, after the conquest and division? The Talmud
  records both (Arakhin 12b-13a). The machine carries both settings;
  a run of the book of Joshua will exercise the historical one.
- **Leap years before the fixed calendar.** The court's grain and
  fruit observations are not in the text. The machine runs the
  season rule alone and labels every dependent date MODELED. Nothing
  on the shelf can settle it; it stays labeled.
- **The flood's 150 days** against the received month length — the
  divergence stays printed.
- **Conflicting numbers between books** (1 Kings 6:1's 480 years
  from the exodus against the periods in Judges). The tradition's
  reconciliation is in a work not on the local shelf. They will run
  as reported divergences when those books are reached.
- **Two definitions of a day.** The calendar's day runs evening to
  evening (Genesis 1: "there was evening and there was morning"); the
  Temple's day for offerings runs day then night (Chullin 83a). The
  machine uses the first and notes the second.
- **Which day of creation is the first of the year**, and **whether
  "the six hundredth year" means the year of age 600 or 599** — two
  readings each, both recorded, the running one named, the other
  printed beside it.
- **The inclusive count.** Three places in the fourth book where the
  tradition counts a span with its first day in and the machine's
  timer counts the days that pass: the month of flesh, the spies'
  forty days, and the forty-nine days from the tabernacle to the
  departure. Abaye's full month is the calendar row's other arm,
  recorded and not run; the misses stay printed.
- **Miriam's day.** The text gives the month, the tradition the tenth
  (Seder Olam Rabbah 10); the tape buries her on the arrival's day and
  prints the nine-day divergence.
- **The vow's twenty-four hours.** Rabbi Shimon ben Yochai's reading
  of "from day to day" is the row's second arm, named and never run.
- **A replay inside a bound.** The cursor stands only at a stated
  date or after the last one; a stop between two dates is refused by
  construction, and a design for it waits on the readback (THE_LOOP.md,
  step 6).
- **Korach's days.** The chapters carry no date in the text and none
  on the shelf; their lines sit at the counter's day, by page order,
  labeled so.
- **The jubilee east of the Jordan.** Whether the fiftieth year's
  release reaches the land Gad and Reuben took is filed as a
  parameter for the book of Joshua's runs.

---

## How this design was settled

The clock was specified in this document, tested against the engine
by the session that owns the engine, and argued through two rounds
until both sessions agreed; the owner then ruled and the build ran.
The agreed points, in plain words: no invented "tick" events — time
enters only through the text's dates and the calendar's computed
boundaries; the day is the base unit and the year is derived; every
calendar number is data with a source; a stated date out of page
order leaves the clock unmoved; the jubilee is decided by the act;
duties that recur (the daily offering) re-arm themselves through the
calendar and stop only when the text records them stopping. The
implementation record with every line of the build is
World/step9/CLOCK.md; the account of the first full run, with the
chronology table and all fourteen checkpoints, is
World/step9/REPORT_SEQUENTIAL_RUN.md; the fourth book's walk, sitting
by sitting, with every clock decision written before its code, is
World/step9/NUMBERS_WALK.md; the verses and Talmud rows this design
rests on are quoted whole in TIME.md in this folder, the fourth
book's in its section 12.
