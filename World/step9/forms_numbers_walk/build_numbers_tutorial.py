import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# The tutorial WHAT NUMBERS DOES FOR THE SIMULATION (the owner, 2026-09-11: "take this last reply... make a tutorial... as big as it needs to
# be... use full verses... a markdown and epub"). Every verse is pulled from the shelf by reference (Onkelos' English as the local export gives
# him, HTML stripped, never retyped); verses outside the Torah are the reading's own plain English, labeled; every machine line is pulled from
# the tape run's own output (scratchpad korach_seq2.txt) or from the probes' live run. The template below carries markers:
#   @@V Book c:v[-v]          the shelf's Onkelos English, one verse per line
#   @@P key                   a plain-English verse from PLAIN (outside the Torah)
#   @@CK CODE,CODE            the tape run's CHECKPOINT lines, verbatim, in a code fence
#   @@PROBE N1,G1             census_probes.py's rows, verbatim, in a code fence
import json, re, subprocess, sys, os
R = (_ROOT + '/Data/sefaria_export')
OUT_MD = (_ROOT + '/What_Numbers_Does_For_The_Simulation.md')
OUT_EPUB = (_ROOT + '/What_Numbers_Does_For_The_Simulation.epub')
S = '<scratch>'
strip = lambda s: re.sub(r'<[^>]+>', '', s).replace(' ', ' ').strip()
BOOKS = {'Gen': 'Onkelos_Genesis', 'Exod': 'Onkelos_Exodus', 'Lev': 'Onkelos_Leviticus', 'Num': 'Onkelos_Numbers', 'Deut': 'Onkelos_Deuteronomy'}
NAMES = {'Gen': 'Genesis', 'Exod': 'Exodus', 'Lev': 'Leviticus', 'Num': 'Numbers', 'Deut': 'Deuteronomy'}
TEXT = {b: json.load(open(f'{R}/{d}/en.json', encoding='utf-8'))['text'] for b, d in BOOKS.items()}
def verse(b, c, v):
    t = strip(TEXT[b][c - 1][v - 1]); assert t, (b, c, v); return t
def V(spec):
    m = re.fullmatch(r'(Gen|Exod|Lev|Num|Deut) (\d+):(\d+)(?:-(\d+))?', spec); b, c, a, z = m.group(1), int(m.group(2)), int(m.group(3)), int(m.group(4) or m.group(3))
    return '\n'.join('> **%s %d:%d** %s' % (NAMES[b], c, v, verse(b, c, v)) for v in range(a, z + 1))
PLAIN = {  # the reading's own plain English, following the Hebrew word order (verses outside the Torah — Onkelos does not reach them)
 '1Chr 23:24-27': ["**1 Chronicles 23:24** These were the sons of Levi by their fathers' houses, the heads of the fathers' houses by their counted ones, by the number of names by their skulls, doing the work for the service of the house of the LORD, from twenty years old and upward.",
                   "**1 Chronicles 23:25** For David said: the LORD, the God of Israel, has given rest to His people, and He dwells in Jerusalem forever.",
                   "**1 Chronicles 23:26** And also the Levites: there is no more carrying of the tabernacle and all its vessels for its service.",
                   "**1 Chronicles 23:27** For by the last words of David, these were the number of the sons of Levi from twenty years old and upward."],
 'Ps 95:8-11': ["**Psalm 95:8** Do not harden your heart as at Meribah, as on the day of Massah in the wilderness,",
                "**Psalm 95:9** when your fathers tested Me, tried Me, though they had seen My work.",
                "**Psalm 95:10** Forty years I loathed a generation, and I said: a people of straying heart are they, and they have not known My ways;",
                "**Psalm 95:11** so I swore in My anger: they shall not come into My rest."],
 'Ps 106:16-18': ["**Psalm 106:16** And they were jealous of Moses in the camp, of Aaron the holy one of the LORD.",
                  "**Psalm 106:17** The earth opened and swallowed Dathan, and covered the company of Abiram.",
                  "**Psalm 106:18** And a fire burned in their company; a flame consumed the wicked."],
 'Neh 10:39': ["**Nehemiah 10:39** And the priest, the son of Aaron, shall be with the Levites when the Levites take the tithe; and the Levites shall bring up the tithe of the tithe to the house of our God, to the chambers of the treasure house."],
 '2Chr 13:5': ["**2 Chronicles 13:5** Is it not for you to know that the LORD, the God of Israel, gave the kingdom to David over Israel forever, to him and to his sons, a covenant of salt?"],
 'Josh 14:10-11': ["**Joshua 14:10** And now, behold, the LORD has kept me alive, as He spoke, these forty-five years from when the LORD spoke this word to Moses, when Israel walked in the wilderness; and now, behold, I am today a son of eighty-five years.",
                   "**Joshua 14:11** I am still today as strong as on the day Moses sent me: as my strength then, so my strength now, for the war, and to go out and to come in."],
}
CK = {}
for ln in open(f'{S}/korach_seq2.txt', encoding='utf-8'):
    m = re.match(r'\s*CHECKPOINT (C[A-Z]?\d+[a-z]?(?:-[a-z0-9]+)?) (.*)$', ln)
    if m: CK[m.group(1)] = m.group(1) + ' ' + m.group(2).strip()
PROBES = {}
pr = subprocess.run([sys.executable, (_ROOT + '/World/step9/census_probes.py')], capture_output=True, text=True).stdout
for ln in pr.splitlines():
    m = re.match(r'\s*(PASS|FAIL)\s+(N\d+|R\d+|D\d+|E\d+|F\d+|G\d+|O\d+)\s', ln)
    if m: PROBES.setdefault(m.group(2), []).append(ln.strip())
RUN_LINE = [ln.strip() for ln in open(f'{S}/korach_seq2.txt', encoding='utf-8') if ln.startswith('OK   the run')][0]
def expand(text):
    out = []
    for ln in text.split('\n'):
        if ln.startswith('@@V '):
            out.append(V(ln[4:].strip()))
        elif ln.startswith('@@P '):
            out.append('\n'.join('> ' + x for x in PLAIN[ln[4:].strip()]))
        elif ln.startswith('@@CK '):
            codes = [c.strip() for c in ln[5:].split(',')]
            for c in codes: assert c in CK, c
            out.append('```\n' + '\n'.join(CK[c] for c in codes) + '\n```')
        elif ln.startswith('@@PROBE '):
            codes = [c.strip() for c in ln[8:].split(',')]
            rows = []
            for c in codes: assert c in PROBES, c; rows += PROBES[c]
            out.append('```\n' + '\n'.join(rows) + '\n```')
        elif ln.strip() == '@@RUN':
            out.append('```\n' + RUN_LINE + '\n```')
        else:
            out.append(ln)
    return '\n'.join(out)

T = r'''# What Numbers Does For The Simulation

A tutorial on the function the book of Numbers serves in the running world, with the verses in full and the machine's own output beside them.

Written 2026, September 11, the morning after the compile of Korach (Numbers 16 to 18) closed. Numbers 1:1 through 18:32 is read, frozen, compiled and on the tape; the rest of the book waits.

This tutorial grew out of a one-screen answer to the question "what function does Numbers provide for the simulation." That answer named seven functions. Here each becomes a chapter, and each claim is placed beside the verses it rests on and the machine line that checks it. Read it slowly. Nothing here is a summary of the text; the text is quoted whole, and the machine's lines are printed as they came out of the run of 2026, September 10.

Three conventions.

First, the verses. The shelf holds Onkelos, the Aramaic translation of the Torah, with an English rendering of him, and that English is what the tutorial quotes for every verse inside the Torah, exactly as the shelf gives it, brackets and all. The rendering keeps Hebrew names in their Hebrew shape. A short decoder: Adonoy is the LORD, the four-letter Name; Moshe is Moses; Aharon is Aaron; Bnei Yisroel is the children of Israel; Mishkon is the tabernacle; Kohen is a priest; Levi'im are the Levites; Mitzrayim is Egypt; Sinai is Sinai. Verses outside the Torah, where Onkelos does not reach, are given in the reading's own plain English, made to follow the Hebrew word order, and are labeled so.

Second, the machine's lines. Every line printed in a box is copied from the tape run's output or from the probes' live run, unedited. A line ending in MATCH means the ink and the machine agreed. A line ending in DIVERGE means they did not, and the divergence is filed open on purpose. OPEN is a status the machine is allowed to hold; it is never allowed to pretend.

Third, Hebrew. When a Hebrew word appears it is glossed in English at once, every time. Where the shelf's rendering of a verse uses a hyphenated Hebrew term, the tutorial adds a gloss in parentheses marked "gloss:"; those parentheses are the tutorial's, the square brackets are the shelf's own.

## Chapter One. What The Simulation Is, In Five Words.

Before the book can be given a function, the machine it serves needs a picture. Five words carry it.

The tape. Every narrated act of the twenty-four books, in verse order, on one running world. An act is submitted as an event: who did what, at which verse. The tape today runs from the first day of creation to the daughters of Zelophehad in the fortieth year, and Korach's twenty-five lines joined it yesterday.

The clock. A day counter with eras laid over it. A verse that carries a date is a marker: it sets the counter. Markers come in three placements. Text-constrained, when the verse itself gives the day. Reading-placed, when the tradition places the day and the ink does not. Page-order, when neither does, and the line simply takes the counter's current day. Some markers are retrograde: the verse is later on the page but earlier in time, and the counter is not moved backward; the event is dated where it belongs, the counter stays.

The ledger. Every entity (a person, a people, an object, an institution) has entries: statuses, debits, blocks, timers. A debit is a command that waits for its run; when the run comes, the debit is closed and the close is dated. A timer is a due day; when the counter passes it, the timer fires and writes its entry then. A status is a standing fact the later law may consult.

The daemons. Each compiled law is a small program installed at the verse where the law is given. It watches the tape for the kinds of event it governs and writes the ledger. It never emits an event of its own. Once installed it stays in force across books, which is the thing this tutorial keeps testing.

The checkpoints. Named checks the run must reproduce: an arithmetic the ink states, a date the tradition places, a count on the ledger. The run prints each with MATCH or DIVERGE. The run tuple, ten numbers, is predicted before each sitting's run and compared after.

And the law behind all of it, ruled by the owner on 2026, September 2: the twenty-four books are the program; the Talmud holds the compile rules; the Mishnah is the answer sheet. Nothing from the Talmud enters the code as logic. It enters as the test the code is graded against, and as the record of who taught which reading.

With that picture, the question has a shape. Genesis put the story on the tape. Exodus and Leviticus put the specifications into the code. What does Numbers do?

## Chapter Two. The Book Of Runs.

The first function is the plainest to show. Exodus and Leviticus state what should be done. Numbers is where it is done, and the machine records the doing as the closing of a debt.

Take the half-shekel. The specification is in Exodus:

@@V Exod 30:11-16

The verse says "when you take the sum," and the counting has not happened yet. The machine writes this as a debit on the people: a count commanded, open. The run comes at the start of Numbers:

@@V Num 1:1-3

And the count closes:

@@V Num 1:44-46

The number is the same one the accounts gave at the end of Exodus, when the silver from that very half-shekel was weighed:

@@V Exod 38:25-26

The machine reads both numbers from the verses with its own parser (Chapter Seven shows how), adds the twelve tribes, and checks the two seats against each other:

@@CK CB1,CB2

The pattern repeats through the first four chapters. The camp is commanded and then set; the Levites are counted and then given; the firstborn are counted and then redeemed. Each is a debit closed by its run, and the machine counts the closes:

@@CK CB8

Here is the redemption, whose arithmetic the ink states in three steps. The firstborn are counted:

@@V Num 3:40-43

The Levites stand in their place, and the excess is named:

@@V Num 3:44-48

And the money is collected and handed over:

@@V Num 3:49-51

Three numbers, three checks. The excess is the firstborn count less the Levite count; the money is the excess times five; the five shekels are the Exodus 30 shekel of twenty gerah, which the machine fetches from the Exodus engine rather than restating:

@@CK CB3,CB4,CB5

Notice the gap the third check records. The Levite houses, summed one by one, come to 22,300; the verse writes 22,000. The machine does not correct the verse. It reads the sum, reads the total, and reports the three hundred. The Talmud asks the same question in the same words (Bekhorot 5a: "where did the three hundred go?") and answers that the three hundred were firstborn Levites, who could redeem no one. The machine carries that answer as a data row and the gap as a MATCH, because the check was written to expect three hundred.

The Passover is the same shape at a larger scale. Its specification is the whole of Exodus 12; here is the command's head:

@@V Exod 12:1-6

And its run, a year later:

@@V Num 9:1-5

The princes' dedication of the altar is the run of the erection:

@@V Exod 40:17

@@V Num 7:1

@@V Num 7:10-11

The twelve days are then written out, one prince per day, and the chapter closes on totals the machine checks against twelve times one prince's gift:

@@V Num 7:84-88

@@CK CD3,CD6

And the Levites' service is commanded with an age, run with a different age, and re-parametered again by a later book in its own ink. Numbers 4 says thirty:

@@V Num 4:1-3

Numbers 8 says twenty-five:

@@V Num 8:23-26

And Chronicles says twenty, and gives the reason:

The reading's plain English:

@@P 1Chr 23:24-27

There is no more carrying. The Levite's age is a parameter of the law, and the later run rewrote it in its own words. The machine carries the three settings with their seats and the stated reason, and does not choose.

That is the first function. Numbers is where the specifications of the earlier books become closed debts on the ledger, and the closes are what the checkpoints count.

## Chapter Three. The Clock Of The Wilderness.

The second function is time. Exodus opened the era; Numbers runs it.

The era opens on a verse that names its own month:

@@V Exod 12:2

The machine takes that as the exodus epoch: year one, month one. The end of Exodus dates the tabernacle:

@@V Exod 40:17

And Numbers opens with a date of its own:

@@V Num 1:1

The second year, the second month, the first day. That is a text-constrained marker: the ink gives the day, the counter is set. The machine checks it:

@@CK CB6

Now the first surprise of the book. Chapter 9 is dated before chapter 1:

@@V Num 9:1-5

The first month of the second year is earlier than the second month of the second year, and the page order is the other way round. The tradition states the rule: "there is no earlier and later in the Torah" (Pesachim 6b). The machine implements it as a retrograde marker. The event is dated in the first month; the counter, already at the second month, is not moved back. The check:

@@CK CB7

Chapter 7 does it again. The day Moses finished setting up the tabernacle is the first day of the first month (Exodus 40:17 above), a month before the census that opens the book:

@@V Num 7:1

So the twelve days of the princes are twelve retrograde markers, and the offerings are not tape lines at all. They are twelve dues written by the command of 7:11, every one already past when written, each checked against the day the text stamps on it:

@@CK CD5,CD6

Then the march. The ink dates the departure:

@@V Num 10:11-12

@@CK CE1

From here the ink stops giving dates for a stretch, and the tradition supplies them. A page of the Talmud (Taanit 29a) lays the days end to end: the twentieth of the second month, three days' journey, a month of flesh, seven days for Miriam, the spies sent on the twenty-ninth of Sivan, returned on the Ninth of Av. The machine takes those days as reading-placed markers, and runs the ink's own durations as timers between them. The ink's durations:

@@V Num 10:33

@@V Num 11:19-20

@@V Num 12:14-15

@@V Num 13:25

Two of the three timers land exactly on the shelf's days. The month of flesh lands two days late, and the forty days one day late:

@@CK CE2,CE3,CE4,CF1,CF2

The reason is the same both times and the machine files it rather than absorbing it. The tradition counts a span inclusively, the first day in; the machine's timers count the days that pass. The Talmud page confesses the same slip on its own arithmetic: it counts the spies' forty days and finds "forty days minus one," then has Abaye make the month of Tammuz full to repair it. The machine carries Abaye's full Tammuz as the other arm of a calendar parameter, unexercised, and the divergence stays OPEN.

The decree turns days into years:

@@V Num 14:33-34

And Deuteronomy, in its own ink, subtracts:

@@V Deut 2:14

Forty years from the decree by 14:34; thirty-eight from Kadesh by Deuteronomy 2:14; the difference is the two years already elapsed when the decree fell, which is exactly the era's year at that point. The machine sets the decree's timer by the Calendar and reports where it lands:

@@CK CF3

The tape's last marker in Numbers so far is the daughters of Zelophehad in the fortieth year, and the decree's due falls eight days past it, so the timer is pending. It will fire when the next reading places its markers. The verse that will place them is already known:

@@V Num 33:38-39

Korach's own stretch, chapters 16 to 18, carries no date in the ink and none on the shelf; the tutorial's own sitting searched Seder Olam Rabbah by script and found no row. So its twenty-five lines take the running counter's day, page-order, and its two one-day timers ("tomorrow" at 16:7 and 16:16; "on the morrow" at 17:23) fire the day after:

@@V Num 16:7

@@V Num 17:22-23

@@CK CK2

That is the second function. Numbers supplies the markers that run the clock from the second year to the fortieth, the retrograde rule that keeps the page order honest, and the durations that the tradition's day-stack is graded against.

## Chapter Four. The Cases.

The third function is the one the running world was built for. A case is a moment where the installed law meets a fact it cannot answer. The ink says so in its own words: the case is brought, the answer is awaited, the answer comes, and the answer is a rule for the generations. Numbers holds three of the four such moments; Leviticus holds the first.

Here is the first, the blasphemer:

@@V Lev 24:10-14

"Until it would be clarified for them." The machine writes that as a halt: a declaration owed on the court, the man in custody. The output comes at 24:15 to 22 as a law for the generations, and the machine records the case's output as a rule installed. Then the execution:

@@V Lev 24:23

Numbers 9 is the second case, and the ink's own vocabulary is the clearest of the four:

@@V Num 9:6-8

"Stand and I will listen." The halt again. The output:

@@V Num 9:9-14

The output installs a rule: a second Passover, in the second month, for the unclean and the far. On the tape, the men's own second Passover is a timer set at the case's day and due the fourteenth of the second month, and it fires on the walk to the next marker:

@@CK CN1

The third case is the wood-gatherer, and here the halt has a reason the ink states:

@@V Num 15:32-36

"Since it was not specified, what was to be done to him." The Sabbath law was in force; its death penalty was written in Exodus (the next chapter shows the verse); what was not specified was the mode. The output at 15:35 supplies it, stoning, and the machine records this as a rule installed into an existing law rather than a new law: the Sabbath daemon, installed in Exodus, gains a cell.

The fourth case is the daughters, and it has two pleas and two outputs:

@@V Num 27:1-5

@@V Num 27:6-11

The output is the inheritance order for the generations, and the tape carries the daughters' own holding as a debt still open, since the ink pays it only in Joshua. The second plea, from the tribe, comes nine chapters later:

@@V Num 36:1-4

@@V Num 36:5-9

The machine's finding at that plea was that it does not halt: the answer "the tribe of the sons of Joseph speaks rightly" is delivered at once, because the rule from the first case is already in force and the second case only bounds it. The tape carries the daughters' marriage within the tribe as the close:

@@V Num 36:10-12

Four cases, four shapes of halt, and the machinery for all of them was built on these verses: the docket that opens when the law cannot answer, the output verse that installs a rule, and the ledger entry that records which case installed which law. That is the third function, and it is the one that made the simulation a loop with memory rather than a list of specifications.

## Chapter Five. Laws That Stay In Force Across Books.

The fourth function is a test that only a fourth book can run. A law installed in Exodus must still be in force when a Numbers act touches it. If the daemons only worked inside their own book, the simulation would be a shelf of separate programs. Numbers proves they are one.

The Sabbath's death penalty is written in Exodus, twice:

@@V Exod 31:14-15

@@V Exod 35:2-3

The Sabbath daemon was installed at those verses. Its first fire on the whole tape is the wood-gatherer of Numbers 15, quoted in the last chapter. When the gatherer's line was submitted, it was the Exodus daemon that wrote the labor barred and the death on his ledger; the case's output only supplied the mode. The sitting's own note at the time: "an Exodus law can wait for a Numbers act."

The incense altar's block is also Exodus:

@@V Exod 30:7-9

"No foreign incense." When Korach's two hundred and fifty men offered incense before the LORD, the line was submitted with the burners named as strangers:

@@V Num 16:17-18

@@V Num 16:35

The daemon that wrote on the two hundred and fifty was the investiture daemon of Exodus, installed at the tabernacle's consecration. The machine noted at the time that the two hundred and fifty entered the ledger as an entity because an Exodus law wrote on them, a full sitting before Korach's own chapter was compiled. And the case's output, in chapter 17, then installs the ban as a rule for the generations in the priesthood's own ledger:

@@V Num 17:1-5

"As Adonoy spoke to him through Moshe." That clause is the output's citation of its own installation, and the machine files it as an internal pointer.

The manna jar was laid up in Exodus with a formula:

@@V Exod 16:32-34

Aaron's staff is laid up in Numbers with the same formula:

@@V Num 17:25-26

The Talmud reads the shared words "for a keeping" as a verbal analogy and concludes the two objects were hidden together with the ark (Keritot 5b; Horayot 12a; Yoma 52b). The machine has the jar's entry from Exodus and the staff's entry from Numbers, and checks that both stand:

@@CK CK6

And the Levites' guard, commanded in the first chapter with a purpose clause:

@@V Num 1:50-53

is restated in chapter 18 with one word added:

@@V Num 18:1-5

The machine computed the two clauses word by word and found the one token added, the Hebrew עוֹד ("more"): no MORE wrath. The Sifrei reads the same clause and counts four "no more"s in the Torah, each paid by a prior event. The check requires the first chapter's guard and the eighteenth chapter's watch both to stand on the Levites' ledger:

@@CK CK7

That is the fourth function. Numbers is the book where a law from an earlier book is asked to act, and the ledger shows that it did.

## Chapter Six. The Standing Statuses.

The fifth function is quieter. Some of what Numbers gives is not an act and not a case but a standing fact that every later offering and every later tithe will consult. The machine calls these statuses. They are written once, dated, and never closed.

The Levites are given, three times, in three forms:

@@V Num 3:5-10

@@V Num 8:14-19

@@V Num 18:6-7

The watch is the two-way fence, and the ink states both sides:

@@V Num 18:2-4

"Both they and you." The Sifrei reads it as two fences: the priests inside, the Levites outside, and each kept out of the other's work. The machine writes one status on Aaron and one on the Levites, and its scene reproduces the Mishnah's picture of the watch (Middot 1:1: the priests in three places, the Levites in twenty-one; the priests above and the Levites below at the gate).

The gifts are granted as a covenant:

@@V Num 18:8-11

@@V Num 18:19

The Talmud counts twenty-four gifts in this passage, given "by a generalization and a detail and a covenant of salt" (Chullin 133b), and the machine carries the list as data, twelve in the sanctuary and twelve in the borders, summing to twenty-four. The covenant of salt is a phrase with exactly two seats in the Bible, Aaron's and David's; the machine censused the whole Tanakh for it:

The reading's plain English:

@@P 2Chr 13:5

The portion is declared, and the inheritance barred:

@@V Num 18:20-24

Deuteronomy runs the same clause:

@@V Deut 18:1-2

And the tithe of the tithe is commanded as arithmetic:

@@V Num 18:25-28

A tenth of a tenth is one part in a hundred. The machine computes it as a fraction, not a stored constant, and Nehemiah's run of the same duty is the reading's other seat:

The reading's plain English:

@@P Neh 10:39

@@CK CK8

That is the fifth function. Numbers writes the priesthood's and the Levites' standing entitlements on the ledger, and the later law reads them there.

## Chapter Seven. The Population.

The sixth function is the one that gave the book its name. Numbers carries the world's headcount, and the machine refuses to type it.

Here is how the ink writes a count:

@@V Num 1:20-21

Six and forty thousand and five hundred. The engine's parser, built on Genesis and Exodus, read that verse on the first day of the walk and returned 1,546, adding six, forty, a thousand and five hundred. The book has its own grammar for numbers: a thousand multiplies the group before it; "and a thousand" adds; a doubled numeral is distributive; a word that reads "from" and a word that reads "a hundred of" share their letters and are told apart by vowels. Each rule was written as a probe that failed first, and the probes stand as tripwires. Here are the census rows of the probe file as they ran today:

@@PROBE N1,N2,N7,N8,N9

The totals close on three seats:

@@V Num 2:32

The count is then used. It is the set the decree falls on, and the machine does not restate it there; it calls the census engine:

@@V Num 14:29-30

@@CK CF4

The book will count again, after the forty years, and the second census is already on the tape's horizon:

@@V Num 26:1-4

@@V Num 26:51

@@V Num 26:63-65

When that portion is compiled, the second total will be read by the same parser and checked against the first, and the exclusion the last verse states, the men of the first count all gone save two, will be checked against the decree's own set.

Korach's chapters added one more grammar rule, and its census across the whole Bible caught three old misreadings. The rule: a numeral carrying the definite article at the head of a compound. The verse:

@@V Num 16:35

The engine read "the fifty and two hundred" as two hundred, because the article on "the fifty" had silenced it since the parser's first day. The class was listed over the whole Bible before the rule was typed, and the list held Exodus 38:28, whose 1,775 shekels (the same number the parser reads right at 38:25 above) had been read as seven and seventy-five all along, and Numbers 31:54, whose "captains of the thousands and of the hundreds" had been read as two thousand one hundred. The probe rows:

@@PROBE G1,G2,G3

@@CK CK1

That is the sixth function. Numbers gives the world its population in a grammar the machine had to learn, and every later span that needs the count calls it rather than restating it.

## Chapter Eight. The Murmurings As Trials.

The seventh function is the hardest to grade, and the machine grades it by recording where it cannot.

The ink counts the trials itself:

@@V Num 14:22-23

Ten times. The machine keeps a counter on Israel's ledger, an entry written each time the tape narrates a test. The Exodus story wrote six; the spies' night wrote the seventh. The tradition lists all ten (Arakhin 15a and 15b): two at the sea, two at the water, two at the manna, two at the quail, the calf, the spies. The calf and the quail sit on the ledger under other effects, so the counter reads seven against the ink's ten, and the check is filed open:

@@CK CF6

Here are the Numbers trials the tape carries, in their own verses. Taberah:

@@V Num 11:1-3

The quail:

@@V Num 11:4-6

@@V Num 11:33-34

The night of the spies:

@@V Num 14:1-4

And the murmur after Korach, which is not among the ten:

@@V Num 17:6-7

@@V Num 17:11-15

The plague's count is read by the parser, and the machine writes it on Israel's ledger with the ink's own qualification, "besides those who died over the matter of Korach":

@@CK CK3

Deuteronomy retells the list in its own order:

@@V Deut 9:22-24

And the Psalm names the two that opened it:

The reading's plain English:

@@P Ps 95:8-11

That is the seventh function. Numbers narrates the trials that the ink itself counts, and the machine keeps the count on the ledger and reports honestly that it has not yet matched the ink's ten.

## Chapter Nine. Korach's Death, An Open Row.

One row of the ledger deserves its own chapter, because it shows what the machine does when the ink itself is divided.

The earth's mouth:

@@V Num 16:31-34

Read the second verse again. "All the people who were with Korach." The verse names every person who belonged to Korach and does not name Korach. The reading's measurement confirmed it on the letters: the name is absent from the verse's tokens. Then the fire:

@@V Num 16:35

Two hundred and fifty men, and again Korach is not named. The census in chapter 26 retells the event and adds him:

@@V Num 26:9-11

Deuteronomy and the Psalm retell it with Dathan and Abiram alone:

@@V Deut 11:6

The reading's plain English:

@@P Ps 106:16-18

The Talmud argues both ways on one page (Sanhedrin 110a). Rabbi Yochanan reads 16:32 as "but not Korach himself" and 26:10's two hundred and fifty as "but not Korach" and concludes he died in the plague. A baraita reads 26:10's "with Korach" and 16:35's fire and concludes he was both burned and swallowed. The machine holds this as a parameter row with three arms, and the entry it writes on Korach carries the row's value: open. The checkpoint declares what the retelling says and computes what the earth's verse says, and reports the disagreement:

@@CK CK4

The sons of Korach did not die, the census says, and the machine carries that too, as a data row, with the eleven Psalm headings that bear their name as its run.

This is the machine's discipline in one row. It does not choose between the verse and its retelling. It does not choose between the two rabbis. It records the ink's silence, the retelling's addition, the shelf's two arms, and marks the row open.

## Chapter Ten. What The Rest Of The Book Will Do.

Numbers 19 to 36 is read next, portion by portion, each portion compiled before the next is opened. Here is what each stretch will give the simulation, with its opening verses.

The heifer. Two earlier portions already point at it: the camp's purity law at 5:2 sends the corpse-unclean out, and the Levites' cleansing at 8:7 uses "the water of purification." Both edges are filed as owed to chapter 19. The heifer will give the machine a purity clock, seven days with a third and a seventh:

@@V Num 19:1-2

@@V Num 19:11-13

The waters of Meribah and the sentence on Moses and Aaron:

@@V Num 20:7-12

The turn back, which closes a debt left open since the decree: the machine wrote "tomorrow turn and journey by the way of the Red Sea" (14:25) as a command on Israel, and its run is here:

@@V Num 21:4-6

Balaam, whose words are the tradition's own witness that the book's story is spoken as well as written:

@@V Num 22:1-6

@@V Num 23:19-20

Phinehas, whose plague is stayed like Aaron's, and whose covenant the Talmud pairs with the covenant of salt:

@@V Num 25:10-13

The second census, which recounts the world after the forty years and closes the decree:

@@V Num 26:51-56

The commission of Joshua, the run of Moses' own sentence:

@@V Num 27:12-14

@@V Num 27:18-23

The offerings calendar, which the festival engine has waited for since Leviticus 23 and Exodus 29: the daily lamb's libation is already computed from these verses at three seats, and the whole table will be compiled here:

@@V Num 28:1-8

Vows, a new kind of ledger entry, a self-imposed debt with its own release rules:

@@V Num 30:2-3

Midian, whose spoil is an arithmetic the parser will have to read: one soul in five hundred for the warriors, one in fifty for the congregation:

@@V Num 31:25-30

Reuben and Gad, a conditional grant that the tape must hold open across the Jordan:

@@V Num 32:20-24

The itinerary, forty-two stations, some of them dated, which will place the markers the pending timers are waiting for:

@@V Num 33:1-2

@@V Num 33:38-39

The borders and the cities of refuge, institutions with a geometry the parser has already met once, the two thousand cubits:

@@V Num 34:1-2

@@V Num 35:4-5

@@V Num 35:9-15

And the daughters again, the case that closes the book and already sits on the tape.

Caleb's holding, written as a debt on his ledger at the decree, is paid outside the book, and the machine has the payment on file:

The reading's plain English:

@@P Josh 14:10-11

## Chapter Eleven. The Run That Checks It All.

Every claim above was graded in one run of the tape on 2026, September 10, after Korach's lines joined. The run's ten numbers were predicted from the design before the run and typed into the runner; the run reproduced them:

@@RUN

The ten numbers are: events on the tape; timers set; timers fired; timers cancelled; retro-writes; ledger writes; daemons that fired; entities on the ledger; the four double-write pairs the tape is allowed; closes performed. For Korach's sitting they were 1161, 51, 50, 0, 12, 1369, 23, 288, the four pairs, 104.

The tape was then run a second way: with the newest runner's lines removed. That run must reproduce the previous sitting's ten numbers exactly, and it did. This is how the machine knows a new portion joined without touching another span's count.

And the checkpoints of the whole Numbers stretch, in order, as they printed:

@@CK CN1,CB1,CB2,CB3,CB4,CB5,CB6,CB7,CB8,CD1,CD2,CD3,CD4,CD5,CD6,CD7,CD8,CE1,CE2,CE3,CE4,CE5,CE6,CE7,CE8,CE9,CF1,CF2,CF3,CF4,CF5,CF6,CF7,CF8,CF9,CK1,CK2,CK3,CK4,CK5,CK6,CK7,CK8,CK9

Forty-four checks. Thirty-eight match. Six diverge, and every one of the six is a divergence the design declared in advance and filed open: the Sifrei's thirteen utterances against the ink's frames, the inclusive count twice, the eleven descents against the tradition's ten, the ten trials against the ledger's seven, and Korach's death.

## Chapter Twelve. The Function, In One Paragraph.

Genesis put the story on the tape and taught the machine to read narrative. Exodus and Leviticus put the specifications into the code and taught it to read law. Numbers is the book where the specifications are performed, where the clock runs from the second year to the fortieth, where the installed laws are asked to act on new facts and are seen to act, where the law meets four cases it cannot answer and is extended by their outputs, where the priesthood's and the Levites' entitlements are written once and consulted ever after, where the world is counted in a grammar the machine had to learn, and where the people's trials are narrated in a count the machine has not yet matched. It is the book that turns a specification into a running world with memory. That is its function.

## Glossary.

The tape: the sequence of narrated acts of the twenty-four books on one running world, in verse order.

A marker: a verse that sets the day counter. Text-constrained when the verse gives the day; reading-placed when the tradition places it; page-order when the line takes the counter's current day.

Retrograde: a marker whose day is earlier than the counter; the event is dated where it belongs and the counter stays.

The ledger: each entity's entries. A status stands; a debit waits for its run and is closed by it; a block bars; a timer fires on its due day and writes its entry then.

A daemon: a compiled law installed at its verse, watching the tape for the kinds of event it governs and writing the ledger. It never emits an event.

A case: a halt where the installed law cannot answer; the docket opens, the output installs a rule.

A checkpoint: a named check the run must reproduce, printed MATCH or DIVERGE.

The run tuple: ten numbers predicted before a sitting's run and compared after.

The rest: the tape with the newest runner's lines removed, which must reproduce the previous sitting's tuple exactly.

The answer sheet: the Mishnah's rows, used as test data. The compile rules: the Talmud's derivations, used as provenance. The program: the twenty-four books.
'''
md = expand(T)
# the shelf's rendering uses a few hyphenated Hebrew terms; the tutorial glosses them in parentheses marked "gloss:" (the brackets stay the shelf's)
GLOSS = [('terumah-offering', 'terumah-offering (gloss: the priests\' portion)'), ('terumah-gifts', 'terumah-gifts (gloss: the priests\' portions)'),
         ('terumah-gift ', 'terumah-gift (gloss: the priest\'s portion) '), ('non-kohein', 'non-kohein (gloss: a non-priest)')]
lines = md.split('\n')
for i, ln in enumerate(lines):
    if ln.startswith('> '):
        for a_, b_ in GLOSS: ln = ln.replace(a_, b_)
        lines[i] = ln
md = '\n'.join(lines)
assert '@@' not in md, [l for l in md.split('\n') if '@@' in l][:3]
open(OUT_MD, 'w', encoding='utf-8').write(md)
print('wrote', OUT_MD, len(md), 'chars,', md.count('\n## '), 'chapters,', md.count('> **'), 'verse lines')
r = subprocess.run([sys.executable, f'{S}/md_to_epub_pre.py', OUT_MD, OUT_EPUB, 'What Numbers Does For The Simulation'], capture_output=True, text=True)
print(r.stdout.strip()[-300:], r.stderr.strip()[-300:])
print('epub bytes', os.path.getsize(OUT_EPUB))
