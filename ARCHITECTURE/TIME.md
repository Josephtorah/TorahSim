# TIME — every verse and every Talmud passage about clocks and calendars, quoted whole

**The evidence file behind THE_CLOCK.md (searched 2026-09-07; note
for the general reader added the same day).** THE_CLOCK.md teaches
how the machine keeps time. This file is where its claims come from:
every verse in the Bible that says how time is to be kept, and every
passage in the tradition that shows the calendar being built and
operated. You do not need to read it start to finish. It is here so
that any sentence in THE_CLOCK.md can be checked against the text it
rests on.

**How to read this file.** Each section takes one part of a clock —
the unit, the starting point, the counters, the cycles — and quotes
the verses that specify it, in plain modern English rendered from
the Hebrew. The counts ("stands at exactly two places in the whole
Bible") are machine counts: a program searched every word of the
twenty-four books, and each search was first tested on a verse
known to contain the phrase, so a count of zero could never be an
error of the search. Section 11 does the same for the tradition's
own writings (the Mishnah, the Talmud, the Sifra). The last section
says what was built from all this.

**The question that started it.** The owner asked whether running
the Bible's verses in order would tick the machine's timers. It would
not: verse order is an order, not a duration, and the timers are
keyed to days. So the question became: does the text itself say how
time is to be kept? It does — in enough detail to specify the clock.

*Verses are given in plain modern English, rendered from the Hebrew
and checked word by word against it. Where one Hebrew word matters
it is shown once, with its English beside it. Every verse cited is
quoted whole.*

---

## 1. The hardware: what keeps time, and for what

The clock is specified on the fourth day of creation, with its
purposes listed. Genesis 1:14:

> "And God said: Let there be lights in the expanse of the sky, to
> separate the day from the night; and they shall serve as signs,
> and for appointed times, and for days and years."

Four purposes: signs, appointed times (מוֹעֲדִים — mo'adim, the
word the law later uses for the festivals), days, and years. Those
are exactly the units the law will count in. The Psalms restate
the division of labor between the two lights — Psalm 104:19:

> "He made the moon for appointed times; the sun knows its going
> down."

The moon keeps the calendar of appointed times (months and
festivals); the sun keeps the day. The phrase "for appointed times"
stands at three places in the whole Bible: the creation verse, the
psalm, and Nehemiah 10:34 (the wood offering "at its appointed
times"). A two-instrument clock — solar day, lunar month — declared
before any law uses it.

## 2. The base unit: a day is evening, then morning

The unit is defined by its boundary, six times in one chapter —
Genesis 1:5, 8, 13, 19, 23, 31, each ending "and there was
evening and there was morning": the day begins at evening. The
law inherits this without restating it: the impurity timers below
expire "until the evening," and the Sabbath and the Day of
Atonement run evening to evening. Everything sub-day in the law is
positioned inside this unit.

## 3. The epoch: a command that resets the calendar's origin

Exodus 12:2, spoken in Egypt before the exodus:

> "This month is for you the head of months; it is the first for
> you of the months of the year."

The phrase "head of months" — in Hebrew רֹאשׁ חֳדָשִׁים (rosh chodashim, "head of months") — stands
at exactly ONE place in the Bible. It is a command, on the tape,
that redefines where the year begins — the calendar is itself
state, written by an event. Every later date in the Torah counts
from this origin: the tabernacle raised "in the first month of the
second year" (Exodus 40:17), the second-year census (Numbers 1:1),
and the Temple begun "in the four hundred and eightieth year after
the children of Israel went out of the land of Egypt" (1 Kings
6:1, quoted whole in section 7). For the program: the clock needs
an origin that can be moved, and the exodus is the first era.

## 4. Counters: the law's own timer syntax

The clearest programming instruction in the text is the command
"you shall count." It stands, as a command, at five law seats —
Leviticus 23:15, 23:16, 25:8, Deuteronomy 16:9, and the personal
form at Leviticus 15:13 and 15:28 — and each one supplies the
four fields a timer needs: a START EVENT, a UNIT, a LENGTH, and
what happens at EXPIRY.

The omer — a fifty-day counter started by a physical act.
Leviticus 23:15-16:

> "And you shall count for yourselves from the day after the
> sabbath, from the day you bring the sheaf of waving: seven
> complete weeks they shall be; until the day after the seventh
> week you shall count fifty days; and you shall bring a new grain
> offering to the LORD."

Start event: the day the sheaf is brought. Unit: days, grouped in
weeks. Length: fifty. At expiry: bring the new grain offering.
Deuteronomy restates the same counter with the start event
described as the act in the field — Deuteronomy 16:9:

> "Seven weeks you shall count for yourself: from when the sickle
> begins on the standing grain you shall begin to count seven
> weeks."

The jubilee — a forty-nine-year counter. Leviticus 25:8:

> "And you shall count for yourself seven sabbaths of years, seven
> times seven years; and the days of the seven sabbaths of years
> shall be for you forty-nine years."

And its start event, six verses earlier — Leviticus 25:2:

> "Speak to the children of Israel and say to them: When you come
> into the land that I am giving you, the land shall keep a
> sabbath for the LORD."

"When you come into the land" is the start event for a whole
family of counters: it stands at five law seats (Exodus 12:25,
Leviticus 19:23, 23:10, 25:2, Deuteronomy 17:14). The sabbatical
and jubilee cycles begin at entry — not at creation, not at the
exodus. A counter with a start event that is itself a narrated
moment (Joshua's crossing).

The personal impurity counter — a seven-day timer started by a
bodily event. Leviticus 15:13:

> "And when the man with the discharge is cleansed of his
> discharge, he shall count for himself seven days for his
> cleansing, and wash his clothes and bathe his body in running
> water, and be clean."

The same form recurs for the woman at 15:28. Start: the discharge
stops. Unit: days. Length: seven. Expiry: wash, and be clean —
a status change, which is exactly what the engine's timers write.

## 5. Cycles: the recurring schedule

Four periods, each with its seat:

- **Seven days** — the sabbath, from creation; and "seven days" as a
  duration stands 76 times across the Bible (feasts, mourning,
  quarantine, consecration).
- **Monthly** — "at the heads of your months" (Numbers 10:10, 28:11):
  the new-moon offering, "the burnt offering of each month at its
  month, for the months of the year" (Numbers 28:14). Numbers 10:10:

  > "And on the day of your rejoicing, and at your appointed
  > times, and at the heads of your months, you shall blow the
  > trumpets over your burnt offerings and your peace offerings;
  > and they shall be a reminder for you before your God: I am the
  > LORD your God."

  The trumpet is the clock's alarm: a signal sounded when a
  calendar boundary arrives.
- **Annual** — the appointed times of Leviticus 23 and the offering
  calendar of Numbers 28-29, each fixed to a month and a day of
  the month.
- **Seven years and fifty years** — "in the seventh year" stands at
  three law seats (Leviticus 25:4, 25:20, Deuteronomy 15:12);
  "the fiftieth year" at two (Leviticus 25:10, 25:11). The release
  has a deadline form of its own — Deuteronomy 15:1:

  > "At the end of seven years you shall make a release."

  "At the end of seven years" stands at three places: this verse,
  Deuteronomy 31:10 (the public reading), and Jeremiah 34:14 — the
  prophet quoting the servant law to a nation that had stopped
  counting.

## 6. Inside the day: named slots

The day has scheduled positions. "Between the evenings"
(בֵּין הָעַרְבַּיִם — bein ha-arbayim, the late-afternoon slot)
stands at eleven seats, all of them scheduling: the Passover lamb
(Exodus 12:6, Leviticus 23:5, Numbers 9:3, 9:5, 9:11), the
afternoon daily offering (Exodus 29:39, 29:41, Numbers 28:4, 28:8),
the evening incense (Exodus 30:8), the quail (Exodus 16:12). And
"until the evening" stands 42 times, the bulk of them in Leviticus
11 and 15 — the impurity that expires at the day boundary, the
shortest timer in the law. So the program needs a within-day
clock with at least three positions: morning, between the
evenings, evening.

## 7. Elapsed time, stated: the checkpoints

The text does not only start clocks; it reports them finishing,
with arithmetic. These are the assertions a diff engine checks the
computed clock against.

Exodus 12:40-41:

> "And the dwelling of the children of Israel, which they dwelt in
> Egypt, was four hundred and thirty years. And it was at the end
> of four hundred and thirty years — on that very day — all the
> hosts of the LORD went out of the land of Egypt."

Deuteronomy 2:14 — the forty years' wandering, restated as the
thirty-eight that remained after the spies:

> "And the days we walked from Kadesh-barnea until we crossed the
> brook Zered were thirty-eight years, until all that generation,
> the men of war, were gone from the camp, as the LORD had sworn
> to them."

1 Kings 6:1 — an era count and a regnal count in one verse:

> "And it was in the four hundred and eightieth year after the
> children of Israel went out of the land of Egypt, in the fourth
> year, in the month Ziv — that is the second month — of Solomon's
> reign over Israel, that he built the house for the LORD."

And 2 Chronicles 36:21, the seventy years discharged (quoted whole
in THE_EFFECTS.md). "Seventy years" stands at twelve seats, five
of them this one timer (Jeremiah 25:11, 25:12, 29:10, 2 Chronicles
36:21, Daniel 9:2) and two more the prophets reading it (Zechariah
1:12, 7:5).

## 8. Eras and their synchronization

"In the Nth year" — in Hebrew בִּשְׁנַת (bishnat, "in the year of") — stands 77 times, and 44 of
those are the regnal synchronisms of Kings and Chronicles — "in
the third year of Asa king of Judah, Baasha became king over
Israel." Two kingdoms, two counters, and the text aligns them at
every accession. For the program this is an era table with
constraints: two clocks that must agree at each recorded
synchronism, which is a diff-engine job the text sets up itself.
Full date stamps — year, month, and day — appear early and often:
the flood is dated to the day (Genesis 7:11):

> "In the six hundredth year of Noah's life, in the second month,
> on the seventeenth day of the month — on that day all the
> springs of the great deep burst open and the windows of the sky
> were opened."

Moses' last address is dated the same way (Deuteronomy 1:3):

> "And it was in the fortieth year, in the eleventh month, on the
> first of the month, that Moses spoke to the children of Israel
> according to all that the LORD had commanded him for them."

"On the Nth day of the month" — the Hebrew marker לַחֹדֶשׁ (lachodesh,
"of the month") — stands 97 times across the Bible. The text is dense with timestamps; they
are simply not on every verse.

## 9. Unit conversion, stated in the text

Two conversions are written out, and the program may use only
these — never one it invents.

A day for a year — Numbers 14:34:

> "By the number of the days you scouted the land, forty days — a
> day for a year, a day for a year — you shall bear your guilt
> forty years; and you shall know My opposition."

The same rule, applied the other direction, in Ezekiel 4:6:

> "And when you have completed these, you shall lie a second time
> on your right side, and bear the guilt of the house of Judah
> forty days: a day for a year, a day for a year, I have set it
> for you."

"A day for a year" stands at exactly these two seats. And a week
of years — Genesis 29:27, Laban to Jacob:

> "Complete the week of this one, and we will give you the other
> one too, for the service you will serve with me another seven
> years."

"Complete the week of this one" stands at Genesis 29:27-28 only:
"week" meaning seven years, the unit Daniel's seventy weeks later
rides on.

## 10. The honest gap: order without duration

"After these things" — in Hebrew אַחַר הַדְּבָרִים הָאֵלֶּה (achar hadevarim haeleh, "after these things") — stands twelve times — Genesis 15:1, 22:1, 22:20, 39:7,
40:1, 48:1, Joshua 24:29, 1 Kings 17:17, 21:1, Ezra 7:1, Esther
2:1, 3:1. It says "next"; it never says "how long." Between a
marker and the next marker, the text gives sequence only. A
program that assumed zero elapsed time there would be inventing
history; one that assumed any particular number would be inventing
it too. The clock must be able to hold a value of UNKNOWN, and a
timer due inside an unmarked stretch fires at the next marker that
proves the year has passed — no earlier.

---

## 11. What the tradition adds: the calendar as an engineered system

The 24 books specify the clock; the Oral Torah shows it built and
operated. The same census run over the local shelf — every Mishnah
tractate, the Babylonian Talmud, the Tosefta, the Sifra (90,056
rows) — finds the calendar treated as machinery: constants,
protocols, decision procedures, error bounds. The rows below were
read whole.

**The era table.** The first Mishnah of tractate Rosh Hashanah is a
table of counters with different epochs (Mishnah Rosh Hashanah 1:1):

> "There are four new years. The first of Nisan is the new year
> for kings and for festivals. The first of Elul is the new year
> for the animal tithe (Rabbi Eleazar and Rabbi Shimon say: the
> first of Tishrei). The first of Tishrei is the new year for
> years, for sabbatical years and jubilees, for planting and for
> vegetables. The first of Shevat is the new year for trees,
> according to the school of Shammai; the school of Hillel says:
> the fifteenth of it."

Four epochs, each owned by a different class of counter — the
era table the engine needs, written as the tractate's opening row.
And the purpose of the kings' epoch is stated in the Talmud's first
question on it (Rosh Hashanah 2a): "'For kings' — for what law?
Rav Chisda said: for deeds." Documents are dated by the king's
year, and a misdated deed is void: the calendar is a legal
instrument before it is anything else.

**The rounding rule.** Rosh Hashanah 2b: "one day in a year counts
as a year" — a king who took the throne a day before the first of
Nisan is in his second year the next day. This is the rule that
makes the 44 regnal synchronisms in Kings computable: two kingdoms'
counters can only be reconciled if the program knows how a partial
year rounds. The tradition states the rounding; the program must
not invent one.

**A received constant — the length of the month.** Rosh Hashanah
25a: when the court was about to declare the new month on the
twenty-ninth day because the moon's shape appeared through clouds,
Rabban Gamliel stopped them:

> "Thus I have received from my father's father's house: the
> renewal of the moon is not less than twenty-nine days and a half,
> and two-thirds of an hour, and seventy-three parts."

An astronomical constant, transmitted, with the hour divided into
parts (1,080 to the hour, so that seventy-three parts is a
fraction the tradition names). It is not derived on the page; it
is received — the data channel, exactly as the code/data law
describes it. For the engine: the month length is a parameter with
a source, never a number computed from the verses.

**The month boundary is an event, declared by an institution.**
The new month begins when the court says so (Mishnah Rosh Hashanah
3:1): witnesses are examined, and the head of the court declares
"sanctified," and all the people answer "sanctified, sanctified."
If the court saw the moon itself but darkness fell before it could
say the word, the month is intercalated — the boundary waits for
the declaration. Rabban Gamliel kept drawings of the moon's phases
on a tablet and on the wall of his upper room, and tested witnesses
against them (Mishnah Rosh Hashanah 2:8): a validation device for
the input. For the engine this settles a design question: a
calendar boundary is a TIME EVENT emitted by an institution, not a
value computed from astronomy alone. The court writes the calendar
the way a verdict writes the ledger.

**The distribution protocol.** Once declared, the boundary had to
reach the diaspora. Mishnah Rosh Hashanah 2:2-4: at first they lit
bonfires, relayed from the Mount of Olives to Sarteba to Grofina to
Hauran to Beit Biltin, where the signaler waved "until he saw the
whole diaspora before him like a bonfire"; when the Samaritans
corrupted the signal, they switched to messengers. Mishnah 1:3:
messengers go out for six of the months, each named with the
festival it serves. A broadcast network with a known latency — and
the second festival day of the diaspora is the tradition's
handling of that latency.

**Intercalation is a decision procedure with stated inputs.**
Mishnah Sanhedrin 1:2: the month is intercalated by three judges;
the year by three, who begin, five who deliberate, seven who
conclude. Sanhedrin 11b:

> "The year is intercalated on three grounds: on the spring grain,
> on the fruit of the trees, and on the season. On two of them they
> intercalate; on one of them alone they do not."

Two agricultural observations and one astronomical one — the
season (תְּקוּפָה — tekufah, the equinox) — with a two-of-three
rule. Sanhedrin 13a grounds the astronomical input in a verse of
its own: Exodus 34:22, "the festival of ingathering at the turn of
the year" — the ingathering must fall in the new season, and the
sages divide over whether all of the festival or part of it must.
The lunar calendar is held to the solar year by a rule whose
source is a verse.

**The solar cycle, computed.** Eruvin 56a sets out the four
seasons by where the sun rises and sets ("at the season of Nisan
and the season of Tishrei the sun rises at the half of east and
sets at the half of west"), and Berakhot 59b fixes the long cycle:
one who sees the sun at the point of its creation blesses — "and
when is that? Abaye said: every twenty-eight years, when the cycle
returns and the season of Nisan falls in Saturn's hour." An
algorithm with a period.

**Inside the day, in hours.** The between-the-evenings slot of the
verses is given a number (Pesachim 58a, the Mishnah): "the daily
offering is slaughtered at eight and a half hours and offered at
nine and a half; on the eves of Passover it is slaughtered at seven
and a half and offered at eight and a half" — and earlier still
when Passover eve falls on a Friday. The day is twelve hours from
sunrise; the slots are scheduled to the half hour, and the
schedule shifts when two events compete for the same afternoon.
The evening boundary is defined by an observable (Mishnah Berakhot
1:1): the time for the evening Shema begins "from the hour the
priests enter to eat their heave offering" — that is, when the
stars are out — and the night is divided into watches, three or
four (Berakhot 3a).

**The boundary has an error bound.** Shabbat 34b asks "what is
twilight?" and gives three answers: "from sunset, as long as the
eastern face is reddish… when the lower sky has darkened and the
upper has not — twilight; when the upper has darkened and evened
with the lower — night," says Rabbi Yehuda; "the time to walk half
a mil from sunset," says Rabbi Nehemiah; "the blink of an eye —
this one enters and that one leaves, and it cannot be fixed," says
Rabbi Yose. The day boundary is treated as an INTERVAL OF DOUBT
with a measured width, and the law is stringent on both sides of
it. For the engine: the clock needs a boundary-doubt state, not
just a tick.

**The jubilee counter is kept by an institution, and fires
regardless of the acts.** The Sifra reads the count command itself
(Sifra Behar, Section 2, row 1): "'You shall count for yourself' —
in the court." The counter is institutional state, not a private
tally. And the Sifra records a dispute over whether the fiftieth
year is a jubilee if the acts were not performed (Sifra Behar,
Chapter 2, row 4): "'Jubilee' — even though they did not release
the land, even though they did not blow the shofar; or perhaps even
though they did not send the servants free? The verse says 'it is'
— the words of Rabbi Yehuda. Rabbi Yose says: … even though they
did not send the servants free; or perhaps even though they did not
blow the shofar? The verse says 'it is.'" That is the question a
timer designer must answer — does the clock fire on the date, or
only when the institution performs the act — argued on the page,
with the shofar and the servants' release as the two candidate
conditions.

**The era of the exile.** Avodah Zarah 10a: "In the exile we count
only by the kings of Greece" — the Seleucid era, adopted for
documents after the kingdom ended, with the gemara first asking
whether the count might be from the exodus instead. An epoch
change recorded with its alternatives, the last of the era table's
rows.

**And the tradition does the arithmetic on the checkpoints.** The
seventy years are computed three times with three starting epochs
(Megillah 11b-12a), and the seventeen jubilees from entry to exile,
with the cycle-year of both destructions, are worked out in
Arakhin 12b-13a — the rows the Leviticus 26 compile already used
as its grader.

What the shelf adds to the design, in one line each: the era table
with four epochs and a stated rounding rule; the month length as a
received constant with a source; the month boundary as an event
declared by the court; the year held to the sun by a two-of-three
decision on named inputs; the day divided into hours with the
offering slots scheduled to the half hour; the day boundary as a
measured interval of doubt; the jubilee counter as court state,
with the question of whether it fires without the acts recorded as
a dispute. None of it needs inventing.

---

## 12. The fourth book's evidence (added 2026-09-13, after Numbers was run on the clock)

THE_CLOCK.md's section "The fourth book: the clock in the wilderness"
rests on the verses and passages below. Each is quoted whole, and
each is followed by the sentence it supports. Verses are the
reading's plain English, rendered from the Hebrew and checked against
it; the Talmud and the Sifrei are given in the shelf's own English.

**The page runs backward.** Numbers 1:1 (quoted in section 3 above)
dates the book's opening to the first of the second month of the
second year. Numbers 9:5:

> "And they kept the Passover in the first month, on the fourteenth
> day of the month, between the evenings, in the wilderness of Sinai;
> according to all that the LORD commanded Moses, so the children of
> Israel did."

Numbers 7:1:

> "And it was on the day Moses finished setting up the tabernacle,
> and anointed it and sanctified it and all its vessels, and the altar
> and all its vessels, and anointed them and sanctified them —"

Babylonian Talmud Pesachim 6b (the passage the backward marker rests
on, the shelf's English):

> "The Gemara asks: If so, let the Torah write first that which
> occurred in the first month and then let it write that which
> occurred in the second month, as the portion of the Paschal lamb
> preceded the beginning of the book of Numbers chronologically. Rav
> Menashiya bar Taḥlifa said in the name of Rav: That is to say that
> there is no earlier and later, i.e., there is no absolute
> chronological order, in the Torah, as events that occurred later in
> time can appear earlier in the Torah."

Supports: the Passover of chapter 9 and the dedication of chapter 7
are dated before the census that opens the book, and the counter is
not moved back.

**A schedule written into the past.** Numbers 7:11-12:

> "And the LORD said to Moses: one prince per day, one prince per
> day, they shall bring near their offering for the dedication of the
> altar. And he who brought near his offering on the first day was
> Nahshon son of Amminadab, of the tribe of Judah."

Babylonian Talmud Moed Katan 9a (the twelve days one continuous run):

> "With regard to the proof itself, the Gemara asks: And from where
> do we derive that the offerings brought at the dedication of the
> Tabernacle overrode Shabbat? If we say it is as it is written with
> regard to the offerings brought by the tribal princes: 'On the
> first day' (Numbers 7:12) and 'on the seventh day' (Numbers 7:48),
> this is not a conclusive proof, as perhaps this refers not to the
> seventh day of the week but to the seventh day of sacrificial
> offerings. Perhaps they skipped Shabbat and did not sacrifice
> offerings connected to the dedication of the Tabernacle on that
> day. Rav Naḥman bar Yitzḥak said: The verse also states: 'On the day
> of the eleventh day' (Numbers 7:72). The repetition of the word day
> indicates that just as a day is all one continuous period of time,
> so too, the eleven days were all one continuous period of time,
> with no break in the middle, even for Shabbat."

> "The Gemara asks: But perhaps this refers only to days that are fit
> for an individual's offerings, i.e., the offerings were sacrificed
> on eleven consecutive days that were suitable for sacrificing the
> offerings of an individual, but not on Shabbat. The Gemara answers:
> In another verse it is written: 'On the day of the twelfth day'
> (Numbers 7:78), indicating that just as a day is all one continuous
> period of time, so too, the twelve days were all one continuous
> period of time."

Supports: the twelve dues run through one Sabbath without a gap.

**The departure, and the era's year.** Numbers 10:11:

> "And it was in the second year, in the second month, on the
> twentieth of the month, that the cloud lifted from over the
> tabernacle of the testimony."

Babylonian Talmud Rosh Hashanah 3a (Exodus 40:17 and Numbers 10:11
both "the second year"):

> "The Gemara rejects this proposal: It should not enter your mind to
> say this, as it is written: 'And it came to pass in the first month
> in the second year, on the first day of the month, that the
> Tabernacle was established' (Exodus 40:17), and it is written: 'And
> it came to pass in the second year, in the second month, on the
> twentieth day of the month, that the cloud was taken up from over
> the Tabernacle of the testimony' (Numbers 10:11). It may be argued
> as follows: From the fact that when the Bible speaks of Nisan, which
> is the first month, it calls it 'the second year,' and when it
> speaks of the following Iyyar, which is the second month, it also
> calls it 'the second year,' by inference, Rosh HaShana is not at the
> beginning of Iyyar. Were it the case that the New Year begins in
> Iyyar, Nisan and the following Iyyar would not occur in the same
> year, as the year would have changed in Iyyar."

Supports: the departure is forty-nine days after the tabernacle was
raised, inside one year of the exodus era.

**The tradition's day-table.** Numbers 10:33:

> "And they journeyed from the mountain of the LORD a three days'
> journey, and the ark of the covenant of the LORD journeyed before
> them a three days' journey, to seek out a resting place for them."

Numbers 11:19-20:

> "You shall not eat one day, nor two days, nor five days, nor ten
> days, nor twenty days — but a month of days, until it comes out of
> your nostrils and becomes loathsome to you, because you have
> rejected the LORD who is among you, and wept before Him, saying: why
> did we come out of Egypt?"

Numbers 12:14-15:

> "And the LORD said to Moses: if her father had spat in her face,
> would she not be ashamed seven days? Let her be shut out of the camp
> seven days, and after that she shall be brought in. And Miriam was
> shut out of the camp seven days, and the people did not journey
> until Miriam was brought in."

Numbers 13:25:

> "And they returned from spying out the land at the end of forty
> days."

Babylonian Talmud Taanit 29a (the day-table, and the page's own
"forty days minus one"):

> "And it is further written: 'And they set forward from the mount of
> the Lord three days' journey' (Numbers 10:33). Rabbi Ḥama bar Ḥanina
> said: That very day, they turned away from God by displaying their
> anxiety about leaving Mount Sinai. And it is written: 'And the mixed
> multitude that was among them fell a lusting, and the children of
> Israel also wept on their part, and said: Would that we were given
> flesh to eat' (Numbers 11:4). And it is written that the Jews ate
> the meat 'for an entire month' (Numbers 11:20). If one adds to the
> first twenty days an additional three days' journey, these are
> twenty-three days. Consequently, the subsequent month of twenty-nine
> days of eating meat ended on the twenty-second of Sivan."

> "After this, the Jews traveled to Hazeroth, where Miriam was
> afflicted with leprosy, and it is written: 'And Miriam was shut out
> of the camp for seven days, and the people did not journey until
> Miriam was brought in again' (Numbers 12:15). Including these seven
> days, they remained in Hazeroth until the twenty-ninth of Sivan
> before traveling on to Paran, and it is written immediately
> afterward: 'Send you men, that they may spy out the land of Canaan'
> (Numbers 13:2)."

> "And this calculation is taught in a baraita: On the twenty-ninth of
> Sivan, Moses sent the spies. And it is written: 'And they returned
> from spying out the land at the end of forty days' (Numbers 13:25),
> which means that they came back on the Ninth of Av. The Gemara asks:
> These are forty days minus one. The remaining days of the days of
> Sivan, the entire month of Tammuz, and eight days of Av add up to a
> total of thirty-nine days, not forty."

> "Abaye said: The month of Tammuz of that year was a full month of
> thirty days. Accordingly, there are exactly forty days until the
> Ninth of Av. And this is alluded to in the following verse, as it is
> written: 'He has called an appointed time against me to crush my
> young men' (Lamentations 1:15). This indicates that an additional
> appointed day, i.e., a New Moon, was added so that this calamity
> would fall specifically on the Ninth of Av."

Supports: the four reading-placed markers of the spring, the four
timers run between them, the two that match and the two that miss by
the inclusive count, and Abaye's full month as the calendar row's
other arm.

**A day for a year, and the fortieth year's markers.** Numbers 14:34
and Deuteronomy 2:14 are quoted in sections 9 and 7 above. Numbers
20:1:

> "And the children of Israel, the whole congregation, came to the
> wilderness of Zin in the first month, and the people stayed in
> Kadesh; and Miriam died there, and was buried there."

Numbers 20:22:

> "And they journeyed from Kadesh, and the children of Israel, the
> whole congregation, came to Mount Hor."

Numbers 20:28-29:

> "And Moses stripped Aaron of his garments and put them on Eleazar
> his son; and Aaron died there on the top of the mountain, and Moses
> and Eleazar came down from the mountain. And all the congregation
> saw that Aaron had expired, and they wept for Aaron thirty days, all
> the house of Israel."

Numbers 21:4:

> "And they journeyed from Mount Hor by the way of the Red Sea, to go
> around the land of Edom; and the soul of the people grew short on
> the way."

Numbers 33:38-39:

> "And Aaron the priest went up to Mount Hor at the mouth of the LORD
> and died there, in the fortieth year after the children of Israel
> came out of the land of Egypt, in the fifth month, on the first of
> the month. And Aaron was a hundred and twenty-three years old when
> he died on Mount Hor."

Seder Olam Rabbah 9 (the year of the arrival at Zin, the shelf's
English, its own spellings kept):

> "They [the Israelites]--the entire congregation--came to the
> wilderness of Tzin in the first month, and the nation settled there,
> and Miriam died there and was buried there, and therre was not water
> for the congregation, and they gathered against Moses and Aaron
> (Numbers 20:1-2). When the well disappeared, it was Year 40, and it
> was the first of the month of Nissan, there in the episode when
> Moses sent messengers from Kadesh to the King of Edom (ibid. 20:14),
> and Israel made [themselves] there for 3 months. Aaron the Priest
> went up etc., and Aaron was 123 years old when he died at the hill
> of the mountain (ibid. 33)."

Babylonian Talmud Rosh Hashanah 2b (Aaron's date with Deuteronomy
1:3 — the era's year does not turn in the autumn):

> "The Gemara answers: It should not enter your mind to say this, as
> it is written: 'And Aaron the priest went up to Mount Hor at the
> commandment of the Lord, and died there, in the fortieth year after
> the children of Israel were come out of the land of Egypt, in the
> fifth month, on the first day of the month' (Numbers 33:38), and it
> is later written: 'And it came to pass in the fortieth year, in the
> eleventh month, on the first of the month, that Moses spoke to the
> children of Israel' (Deuteronomy 1:3). From the fact that when the
> Bible speaks of the month of Av, which is the fifth month, it calls
> that year 'the fortieth year,' and when it speaks of the following
> Shevat, it also calls that year 'the fortieth year,' the implication
> is that the New Year does not begin in Tishrei. Were it the case
> that the New Year begins in Tishrei, Av and the following Shevat
> would not be in the same year because the year would have changed
> in Tishrei."

> "The Gemara raises an objection: Granted, in this case of Aaron's
> death it is explicitly stated that the year is counted from the
> exodus from Egypt, as it states: 'In the fortieth year after the
> children of Israel were come out of the land of Egypt.' But with
> regard to this other incident of Moses' oration, from where is it
> known that the year is counted from the exodus from Egypt? Perhaps
> it is forty years since the establishment of the Tabernacle in the
> wilderness."

> "The Gemara answers: In accordance with what Rav Pappa said in a
> different context, that the meaning of one instance of the
> expression 'the twentieth year' may be inferred from another
> instance of the expression 'the twentieth year' by way of a verbal
> analogy, here too, the meaning of one instance of the expression
> 'the fortieth year' may be inferred from another instance of the
> expression 'the fortieth year' by way of a verbal analogy: Just as
> here, with regard to Aaron's death, the count is from the exodus
> from Egypt, so too, here, with regard to Moses' oration, although
> this is not stated explicitly, the count is from the exodus from
> Egypt."

Supports: the four markers of the fortieth year — two placed by the
tradition, one fixed by 33:38, one computed from 20:29's thirty days
— and the thirty-eight-year timer firing between the third and the
fourth. Miriam's tenth of the first month is the tradition's (Seder
Olam Rabbah 10); the text gives the month alone, and the machine
prints the nine-day divergence.

**Morrows, thirds and sevenths.** Numbers 16:7:

> "and put fire in them and lay incense on them before the LORD
> tomorrow; and it shall be that the man whom the LORD chooses, he is
> the holy one. You take too much upon you, sons of Levi."

Numbers 17:23:

> "And it was on the morrow that Moses came into the tent of the
> testimony, and behold, the staff of Aaron for the house of Levi had
> budded: it brought forth buds, and blossomed blossoms, and bore ripe
> almonds."

Numbers 19:12:

> "He shall purify himself with it on the third day and on the
> seventh day, and he shall be clean; and if he does not purify
> himself on the third day and on the seventh day, he shall not be
> clean."

Numbers 9:11:

> "In the second month, on the fourteenth day, between the evenings,
> they shall keep it; with unleavened bread and bitter herbs they
> shall eat it."

Supports: the one-day timers on the undated stretch, the third-and-
seventh timers, and the second Passover's due computed by the
calendar.

**Duties keyed to the calendar's words.** Numbers 28:10:

> "The burnt offering of the Sabbath on its Sabbath, beside the
> continual burnt offering and its libation."

Numbers 28:14:

> "And their libations shall be half a hin for the bull, and a third
> of a hin for the ram, and a quarter of a hin for the lamb, of wine.
> This is the burnt offering of the month in its month, for the months
> of the year."

Numbers 29:39:

> "These you shall offer to the LORD at your appointed times, besides
> your vows and your freewill offerings, for your burnt offerings and
> for your meal offerings and for your libations and for your peace
> offerings."

Supports: the eight period timers on the altar, each keyed to a
calendar word.

**An end without a length, and a day that ends at dark.** Numbers
35:25:

> "And the congregation shall deliver the manslayer from the hand of
> the avenger of blood, and the congregation shall return him to his
> city of refuge, where he had fled; and he shall dwell in it until
> the death of the high priest, who was anointed with the holy oil."

Numbers 30:15:

> "But if her husband is altogether silent to her from day to day,
> then he has confirmed all her vows or all her bonds that are upon
> her; he has confirmed them, because he was silent to her on the day
> he heard."

Sifrei Bamidbar 156 (the two readings of "from day to day", the
shelf's English):

> "(Bamidbar 30:14) 'And if her husband be silent, silent to her from
> day to day': This is the silence of taunting. You say this, but
> perhaps it is the silence of confirmation (of the vow)? (This is not
> so, for Ibid. 12) 'and he was silent to her' already speaks of the
> silence of confirmation. How, then, is 'and he be silent, silent' to
> be understood? As referring to the silence of taunting. 'from day to
> day': I might think, from time to time (i.e., for a twenty-four hour
> period); it is, therefore, written 'which are upon her. He has
> confirmed them for he was silent to her on the day of his hearing'
> (i.e., until the night). R. Shimon b. Yochai says: 'from time to
> time (i.e., a twenty-four hour period),' it being written 'from day
> to day.'"

Supports: the manslayer's term as an open entry with no timer, and
the vow's hearing day as a timer to the evening boundary with the
twenty-four-hour reading as the row's other arm.

## What was built from this

Everything above was written before the clock existed. On the same
day, the two working sessions argued the design through two rounds,
the owner ruled, and the clock was built — then Genesis, Exodus, and
Leviticus were run in order on it. In plain words, this is what the
evidence in this file became:

1. **The text's dates move the clock, and nothing else does.** The
   sixty-eight dates the three books state — the begettings of
   Genesis 5 and 11, the flood's dates, the ages at events, "this
   month is for you the head of months," the Sinai dates, the raising
   of the Tabernacle — are the only things that advance the counter.
   Between two dates the clock stands still and the machine says so.
2. **Every number is read from the Hebrew by a program**, and read
   again on every run — sections 4 and 7 supplied the verses.
3. **The calendar's constants are data with sources**, one row each
   in a file the machine reads: the received month length of Rosh
   Hashanah 25a (section 11), the four new years of Mishnah Rosh
   Hashanah 1:1, the leap-year rule of Sanhedrin 11b-13a, the jubilee
   count's start from Arakhin 12b-13a. Where the shelf has nothing —
   the length of a season — the row is marked MODELED, and every date
   that depends on it carries that label.
4. **A person's year turns at the New Year**, as a king's does
   (section 8's regnal rows, and the flood's dates in section 8) —
   the rule Genesis 8:13 forced.
5. **A date stated out of page order leaves the clock unmoved** —
   the rule of Pesachim 6b, "there is no earlier and later in the
   Torah."
6. **The jubilee is decided by the act, not the date** — section 11's
   Sifra dispute and the Talmud's "all its inhabitants."
7. **The text's stated totals are checkpoints** (section 7): the
   machine computes, the text declares, and every mismatch is
   printed — the flood's 150 days against 147; the 430 years against
   210 — never repaired.
8. **The fourth book ran on the same clock** (section 12, added
   2026-09-13): its backward dates, the tradition's day-table as
   reading-placed markers with the text's durations run as timers
   between them, the thirty-eight years fired in the fortieth year off
   the itinerary's own date, the dues keyed to the calendar's words,
   and the two states that end without a number of days.

THE_CLOCK.md teaches all of this from three examples; the build
record is World/step9/CLOCK.md; the account of the first full run,
with its chronology table and fourteen checkpoints, is
World/step9/REPORT_SEQUENTIAL_RUN.md.
