# What Numbers Taught The Machine

A tutorial on the lessons of the Numbers walk, with the verses in full and the machine's own output beside them.

Written 2026, September 10, the morning after Naso was read and frozen.

This tutorial is written to be read slowly. Each chapter is one lesson. Every verse is quoted in full. Every number that the text says was measured by a script, and the script's output is printed as it came. Where the Hebrew matters, the verse is laid out word by word, with the accent on each word and the store's gloss beside it, because the accents turned out to be the whole story of one chapter.

Two conventions. English renderings of verses inside Naso are Onkelos's, as the shelf's English gives him. Renderings elsewhere are the reading's own plain English, made to follow the Hebrew word order. And every Hebrew word carries its English beside it, always, because that is the project's oldest rule.

Here is the promise of the whole tutorial in one breath.

Genesis, Exodus and Leviticus taught the machine to read law and story. Numbers is a fourth kind of book. It is arithmetic written in ink. Censuses, work-counts, twelve identical offerings, totals that must close. The machine had to be taught to read a number as a number, and then it had to be told that it still could not, and the proof came from the accents on the words and from a total that only closes one way.

## Chapter One. The Fourth Book Is Arithmetic.

The walk through Numbers began on the owner's word: "Let's go to the start of numbers and go through it in order." The book had been entered before through its four interrupts, the cases of the blasphemer, the unclean men, the wood-gatherer and the daughters of Zelophehad. Now it is walked from the first verse, one weekly portion at a time.

Each portion gets two sittings. A reading sitting, where the shelf is read at the portion's grain, the units are frozen, and every fact about the ink is computed by a script. Then a compile sitting, where the portion's law and arithmetic become cold functions and its acts go on the tape.

Two portions are read. Bamidbar, Numbers 1:1 to 4:20, is read and compiled. Naso, Numbers 4:21 to 7:89, is read and frozen, and its compile is owed.

What made Numbers different showed on the first verse of the first census.

Numbers 1:21, the reading's English: "Their numbered ones, of the tribe of Reuben, six and forty thousand and five hundred."

The old parser, built on Genesis and Exodus, read that verse and returned 1,546. It had added six, forty, a thousand and five hundred. The ink had meant six-and-forty, multiplied by a thousand, plus five hundred. The machine could count years and days. It could not count a census.

## Chapter Two. The Parser Learns The Census.

The numeral parser lives in the engine, in the function that reads a verse's number phrases. Before Numbers it knew a few rules. A unit before "hundred" multiplies. Every other numeral adds. A year-word keeps a phrase open, so that "five years and a hundred years" is one number, 105. Any other noun closes a phrase, so that "forty days and forty nights" is two numbers.

Here are those two rules on their own verses, with the parser's live output.

Genesis 5:6, the reading's English: "And Seth lived five years and a hundred years, and he begot Enosh."

| Hebrew | gloss | accent |
|---|---|---|
| וַֽיְחִי | "and he lived" | joined by a maqqef (a hyphen) |
| שֵׁ֕ת | "Seth" | zaqef gadol (a pause) |
| חָמֵ֥שׁ | "five" | merkha (joining) |
| שָׁנִ֖ים | "years" | tifcha (a pause) |
| וּמְאַ֣ת | "and a hundred of" | munach (joining) |
| שָׁנָ֑ה | "year" | etnachta (the verse's middle pause) |

The parser's output: `[105]`. The year-word held the phrase open across the "and".

Exodus 24:18, the reading's English: "And Moses came into the midst of the cloud and went up the mountain, and Moses was on the mountain forty days and forty nights."

The parser's output: `[40, 40]`. The noun "days" closed the first phrase.

Then the census arrived and the parser needed five new rules. Each was written into the code with the verse that forced it. Here they are, verse by verse.

**Rule one. A thousand without "and" multiplies the group before it.**

Numbers 1:21 again, word by word:

| Hebrew | gloss | accent |
|---|---|---|
| פְּקֻדֵיהֶ֖ם | "their numbered ones" | tifcha (a pause) |
| לְמַטֵּ֣ה | "of the tribe of" | munach (joining) |
| רְאוּבֵ֑ן | "Reuben" | etnachta (the middle pause) |
| שִׁשָּׁ֧ה | "six" | darga (joining) |
| וְאַרְבָּעִ֛ים | "and forty" | tevir (a pause) |
| אֶ֖לֶף | "thousand" | tifcha (a pause) |
| וַחֲמֵ֥שׁ | "and five" | merkha (joining) |
| מֵאֽוֹת | "hundreds" | silluq (the verse's end) |

The parser's output now: `[46500]`. The group "six and forty" is multiplied by the thousand that follows it. Then "five hundreds" adds.

Numbers 1:46, the reading's English: "And all the numbered ones were six hundred thousand and three thousands and five hundred and fifty."

The parser's output: `[603550]`. Two thousands-words, each closing its own group.

Numbers 2:9, the reading's English: "All the numbered ones of the camp of Judah: a hundred thousand and eighty thousand and six thousands and four hundred, by their hosts. First shall they journey."

The parser's output: `[186400]`.

**Rule two. "And a thousand" adds.**

Numbers 3:50, the reading's English: "From the firstborn of the children of Israel he took the silver: five and sixty and three hundred and a thousand, by the shekel of the sanctuary."

| Hebrew | gloss | accent |
|---|---|---|
| חֲמִשָּׁ֨ה | "five" | qadma (joining) |
| וְשִׁשִּׁ֜ים | "and sixty" | geresh (a pause) |
| וּשְׁלֹ֥שׁ | "and three" | merkha (joining) |
| מֵא֛וֹת | "hundreds" | tevir (a pause) |
| וָאֶ֖לֶף | "and a thousand" | tifcha (a pause) |

The parser's output: `[1365]`. The conjunction on the thousand makes it an addend, not a multiplier. And 1,365 is 273 times five, which is the redemption price the chapter has just computed, so the number is checked by the chapter itself.

**Rule three. A doubled numeral is distributive, one number.**

Numbers 3:47, the reading's English: "And you shall take five, five shekels per skull; by the shekel of the sanctuary shall you take, twenty gerah (the smallest weight) the shekel."

| Hebrew | gloss | accent |
|---|---|---|
| חֲמֵ֧שֶׁת | "five" | darga (joining) |
| חֲמֵ֛שֶׁת | "five" | tevir (a pause) |
| שְׁקָלִ֖ים | "shekels" | tifcha (a pause) |

The parser's output: `[5, 20]`. "Five, five" is five each, not ten. The same rule reads Genesis 7:2's "seven, seven" as seven.

**Rule four. The article on each part is one chain.**

Numbers 3:46, the reading's English: "And the redemption of the three and the seventy and the two hundred who exceed, of the firstborn of the children of Israel, over the Levites."

The parser's output: `[273]`. Three words, each carrying "the", read as one number because each is joined to the next by "and the".

**Rule five. "From" is not "a hundred of."**

This is the rule that led to the next chapter. The consonants מאת ("from", or "a hundred of") can be read two ways. Pointed מְאַת they mean "a hundred of". Pointed מֵאֵת they mean "from". The old parser saw the consonants and counted a hundred at every "from".

Numbers 3:49, the reading's English: "And Moses took the silver of the redemption from those who exceeded over the redeemed of the Levites."

The parser's output: `[]`. No number. The word arrives from the verse reader already marked as the preposition, and the parser never sees a numeral there.

Genesis 23:20, the reading's English: "And the field and the cave that was in it were established to Abraham as a holding for a grave, from the sons of Heth."

The parser's output: `[]`. The same word in Genesis, silenced the same way.

All of these were written first as probes that had to fail. The probe file was run against the unchanged parser and passed 3 of 17. Then the code was taught, and the file runs 17 of 17. Here is the run as it prints today:

```
THE CENSUS GRAMMAR — the numeral parser's fire-probes
  PASS  N1  Num 1:21 = 46,500   got [46500]
  PASS  N2  Num 1:46 = 603,550   got [603550]
  PASS  N3  Num 2:9 = 186,400   got [186400]
  PASS  N4  Num 3:39 = 22,000   got [22000]
  PASS  N5  Num 3:43 = 22,273   got [22273]
  PASS  N6  Num 3:46 = 273   got [273]
  PASS  N7  Num 3:47 = [5, 20]   got [5, 20]
  PASS  N8  Num 3:50 = 1,365   got [1365]
  PASS  N9  Num 3:49 = []   got []
  PASS  N10 Exod 38:26 = [20, 603550]   got [20, 603550]
  PASS  N11 Num 3:22 = 7,500   got [7500]
  PASS  N11 Num 3:28 = 8,600   got [8600]
  PASS  N11 Num 3:34 = 6,200   got [6200]
  PASS  R1  Gen 5:6 = [105]   got [105]
  PASS  R2  Exod 24:18 = [40, 40]   got [40, 40]
  PASS  R3  Gen 23:20 = []   got []
  PASS  R4  Exod 38:25 = [100, 1775]   got [100, 1775]
17/17 probes
```

The last four rows are regression probes. They are the Genesis and Exodus grammar, and they had to stay unmoved.

**The lesson under the lesson: a parser is taught against the whole corpus.**

The probes prove the census. They do not prove that nothing else moved. So after the code, the old parser and the new one were run over every verse of the four books and the differences read one by one. The first diff showed 131 verses moved, and reading them found five more wrong readings the probes had not seen. Here are the ones that matter, with the parser's output today.

Genesis 35:27, the reading's English: "And Jacob came to Isaac his father, to Mamre, Kiriath-arba, which is Hebron, where Abraham and Isaac had sojourned."

The name Kiriath-arba means "the town of the four". The article form had counted it. Today's output: `[]`.

Genesis 41:53, the reading's English: "And the seven years of plenty that were in the land of Egypt ended."

The word הַשָּׂבָ֑ע ("the plenty") shares its consonants with "the seven". Today's output: `[7]`, the seven years only.

Genesis 42:13, the reading's English: "And they said: twelve are your servants, brothers are we, sons of one man in the land of Canaan; and behold, the youngest is with our father today, and the one is not."

The closing וְהָאֶחָ֖ד ("and the one", meaning the other brother) had been counted as a number. Today's output: `[12, 1]`, the twelve brothers and the "one man", the last "one" silenced.

Exodus 18:21, the reading's English: "And you shall see, out of all the people, men of worth, fearing God, men of truth, hating gain, and set them over them as rulers of thousands, rulers of hundreds, rulers of fifties and rulers of tens."

The dual "thousands" had been counted as two thousand. Today's output: `[100, 50, 10]`. The thousands are silenced. The hundreds, fifties and tens still read as numbers there, a shape no marker on the tape depends on and the walk has not yet needed.

Genesis 6:16, the reading's English: "A light shall you make for the ark, and to a cubit shall you finish it from above, and the door of the ark in its side shall you set; lower, second and third decks shall you make it."

The word שְׁנִיִּ֥ם ("second ones") had been read as "two", and the verse as thirty-two. Today's output: `[30]`. The "two" is silenced by its vowels, which is the next chapter. The "thirds" still read as thirty. That is what the parser says today, and it is printed here as it is.

Numbers 26:51, the reading's English: "These are the numbered ones of the children of Israel: six hundred thousand and a thousand, seven hundred and thirty."

Today's output: `[601730]`. "And a thousand" adds, as rule two says.

Exodus 12:37, the reading's English: "And the children of Israel journeyed from Rameses to Succoth, about six hundred thousand on foot, the men, besides children."

The old parser had read 1,600. Today's output: `[600000]`.

The final diff after the fixes showed 155 verses moved, none of them a marker. The stitcher re-verified every one of the tape's 133 markers. That is the shape of the lesson: probes for what you meant to change, a full diff for what you did not.

## Chapter Three. The Points On The Stem Decide A Homograph.

A homograph is one spelling with two words in it. Hebrew consonants make many. The vowel points, the small marks under and inside the letters, separate them. The census forced two.

**"From" against "a hundred of".** The consonants מאת ("from", or "a hundred of"). With a short a under the mem, מְאַת, "a hundred of". With a long e under both the mem and the alef, מֵאֵת, "from".

Numbers 2:9 has the first: מְאַ֨ת אֶ֜לֶף ("a hundred thousand"). Numbers 3:49 and 3:50 have the second: מֵאֵת֙ הָעֹ֣דְפִ֔ים ("from those who exceeded"). Genesis 5:4 has a third form, מֵאֹ֖ת ("hundreds", the plural with its own long o), which the first version of the regex caught by mistake and silenced. The first diff found that: the "after" verses of Genesis 5 had lost their hundreds, and the creation checkpoint diverged. The regex was narrowed to the two long e's.

**"Two" against "years".** The consonants שנים ("two", or "years"). With a sheva (the silent half-vowel) under the shin, שְׁנַיִם, "two". With a qamats (the long a) under the shin, שָׁנִים, "years". With a hiriq (the short i) under the nun, שְׁנִיִּם, "second ones".

Numbers 3:39, the reading's English: "All the numbered ones of the Levites whom Moses and Aaron numbered at the mouth of the LORD by their families, every male from a month old and upward: two and twenty thousand."

| Hebrew | gloss | vowel under the shin |
|---|---|---|
| שְׁנַ֥יִם | "two" | a sheva (the silent half-vowel) |
| וְעֶשְׂרִ֖ים | "and twenty" | |
| אָֽלֶף | "thousand" | |

The parser's output: `[22000]`.

Genesis 5:6's שָׁנִ֖ים ("years") carries a qamats (the long a). The verse reader marks it with a star so the parser keeps the phrase open on it as on any year-word. Genesis 6:16's שְׁנִיִּ֥ם ("second ones") carries a hiriq (the short i) under the nun. Starred the same way, it is no number.

The lesson was in how the rule was found. The regex was written only after the code points of the store's own words were printed and read. The shin-dot comes right after the shin, then the vowel. A dagesh (the doubling dot) may sit between the letter and its vowel. A rule typed from a grammar book without that measurement would have matched nothing.

## Chapter Four. Naso Measures The Parser Again: Four Gaps.

The standing rule after Bamidbar is that a parser taught at one portion is measured at the next. Naso's ink module ran the engine's parser over every number of Numbers 4:21 to 7:89 and asserted what it read.

First, what it read right.

Numbers 4:36, Onkelos: "Their numbers, according to their families were two thousand seven hundred and fifty."

| Hebrew | gloss | accent |
|---|---|---|
| אַלְפַּ֕יִם | "two thousand" (the dual) | zaqef gadol (a pause) |
| שְׁבַ֥ע | "seven" | merkha (joining) |
| מֵא֖וֹת | "hundreds" | tifcha (a pause) |
| וַחֲמִשִּֽׁים | "and fifty" | silluq (the verse's end) |

The parser's output: `[2750]`.

Numbers 4:40, Gershon: `[2630]`. Numbers 4:44, Merari: `[3200]`. Numbers 4:48, Onkelos: "Their numbers were eight thousand five hundred and eighty." The parser: `[8580]`. And 2,750 plus 2,630 plus 3,200 is 8,580. The three work-counts sum to the written total, and the module asserts it.

The dedication totals of chapter 7 came out right too.

Numbers 7:84, Onkelos: "This was the dedication of the altar on the day that it was anointed, given by the leaders of Israel; twelve silver trays twelve silver bowls and twelve golden spoons." The parser: `[12, 12, 12]`. The word מֵאֵ֖ת ("from") at "from the leaders" is silenced by rule five.

Numbers 7:85, Onkelos: "One hundred thirty shekolim (shekels) was the weight of each silver tray and each bowl weighed seventy shekolim (shekels). All the silver vessels weighed two thousand four hundred shekolim (shekels) according to sanctuary weights." The parser: `[130, 70, 2400]`. And twelve times 130 plus twelve times 70 is 2,400.

Numbers 7:87: `[12, 12, 12, 12]`. Numbers 7:88: `[24, 60, 60, 60]`, which is twelve times each prince's two, five, five and five of 7:17.

Then the gaps. Seven verses were read wrong, in four shapes. The module records the wrong readings as the measurement and the true readings beside them.

| verse | the parser read | the ink says | the shape |
|---|---|---|---|
| 7:3 | `[6, 10, 1]` | 6, 12, 2, 1 | "two of" and "twelve" |
| 7:7 | `[4]` | 2, 4 | "two of" |
| 6:10 | `[]` | 2, 2 | "two of" |
| 7:13 | `[131, 1, 70]` | 1, 130, 1, 70 | "one" fused to the weight |
| 7:14 | `[11]` | 1, 10 | "one, ten" read as eleven |
| 7:72 | `[10]` | 11 | the word for eleven |
| 7:78 | `[12]` | 12 | right |

**"Two of."** Numbers 7:7, Onkelos: "Two of the wagons and four of the oxen he gave to the sons of Gershon, according to the needs of their work."

| Hebrew | gloss | accent |
|---|---|---|
| אֵ֣ת | the object marker | munach (joining) |
| שְׁתֵּ֣י | "two of" (the feminine construct) | munach (joining) |
| הָעֲגָלֹ֗ת | "the wagons" | revia (a pause) |
| וְאֵת֙ | "and" plus the object marker | pashta (a pause) |
| אַרְבַּ֣עַת | "four of" | munach (joining) |
| הַבָּקָ֔ר | "the oxen" | zaqef qatan (a pause) |

The parser read `[4]`. It knows "two" only in its absolute forms and before "ten" or "and twenty". The construct שְׁתֵּי ("two of") and its masculine שְׁנֵי ("two of") are not in its list. Numbers 6:10's "two turtledoves or two young pigeons" returned nothing for the same reason.

**"One" fused to the weight.** Numbers 7:13, Onkelos: "His offering was one silver tray, its weight was one hundred thirty shekolim (shekels); one silver bowl that weighed seventy shekolim (shekels) according to sanctuary weights. Both were filled with fine flour kneaded with olive oil, for a meal-offering."

| Hebrew | gloss | accent |
|---|---|---|
| קַֽעֲרַת | "a tray of" | joined by a maqqef (a hyphen) |
| כֶּ֣סֶף | "silver" | munach (joining) |
| אַחַ֗ת | "one" | revia (a pause) |
| שְׁלֹשִׁ֣ים | "thirty" | munach (joining) |
| וּמֵאָה֮ | "and a hundred" | zinor (a pause) |
| מִשְׁקָלָהּ֒ | "its weight" | segol (a pause) |

The parser read `[131, 1, 70]`. It added the tray's "one" to the tray's weight, because nothing but a noun closes a phrase and the noun "tray" came before the "one", not after. The ink says one tray, weighing a hundred and thirty.

**"One, ten" read as eleven.** This is the gap that became a move, and it has a chapter of its own.

**The word for eleven.** Numbers 7:72, Onkelos: "On the day of the eleventh day, the leader of the sons of Asher, Pagiel the son of Ochran."

| Hebrew | gloss | accent |
|---|---|---|
| בְּיוֹם֙ | "on the day" | pashta (a pause) |
| עַשְׁתֵּ֣י | "eleven" (the first half of the word) | munach (joining) |
| עָשָׂ֣ר | "ten" | munach (joining) |
| י֔וֹם | "day" | zaqef qatan (a pause) |

The parser read `[10]`. Hebrew has a special word for eleven, עַשְׁתֵּי ("eleven's first half") followed by עָשָׂר ("ten"), and it sits at seven seats in the Torah: Deuteronomy 1:3, Exodus 26:7, 26:8, 36:14, 36:15, Numbers 29:20 and this one. The parser had never met it, because Genesis and Exodus never needed its value.

All four shapes are owed to Naso's compile sitting, where probe rows for each will be written to fail first, then the parser taught, then the corpus-wide diff read again.

## Chapter Five. The Accent Read.

Numbers 7:14, Onkelos: "One spoon of ten gold shekolim (shekels), filled with fragrant incense."

Here is the verse, every word:

| Hebrew | gloss | accent | the store's own label |
|---|---|---|---|
| כַּ֥ף | "a spoon" | merkha | conjunctive (joining) |
| אַחַ֛ת | "one" | tevir | disjunctive (a pause) |
| עֲשָׂרָ֥ה | "ten" | merkha | conjunctive (joining) |
| זָהָ֖ב | "gold" | tifcha | disjunctive (a pause) |
| מְלֵאָ֥ה | "full" | merkha | conjunctive (joining) |
| קְטֹֽרֶת | "incense" | silluq | disjunctive (the verse's end) |

The parser read `[11]`. And by the consonants alone it was right to. "One" followed by "ten" is how Hebrew writes eleven: אַחַת עֶשְׂרֵה ("one ten") is "eleven", the way "four ten" is fourteen. A parser that reads consonants has no way to tell "one spoon, ten shekels" from "eleven".

The accents can tell. Every word in the Hebrew Bible carries a cantillation mark, and each mark is one of two kinds. A conjunctive mark joins its word to the next. A disjunctive mark ends a phrase. The store records the kind on every word, and the table above prints the store's own labels.

The "one" of 7:14 carries a tevir, a disjunctive. It ends a phrase. The phrase is "one spoon". A new phrase begins at "ten". One spoon; ten of gold.

The ink module then asked the whole Tanakh. Every seat where a word for "one" is followed directly by a word for "ten" was listed with the accent on the "one". The list came back with sixteen seats.

Twelve of them are the twelve spoon-verses of Numbers 7, from 7:14 to 7:80, one for each prince. At every one, the "one" carries a tevir. The module asserts all twelve.

The other four are every true eleven in the Bible written as "one ten". Here they are with the accent on the "one".

Deuteronomy 1:2, the reading's English: "Eleven days from Horeb, by way of Mount Seir, to Kadesh-barnea."

| Hebrew | gloss | accent | the store's own label |
|---|---|---|---|
| אַחַ֨ד | "one" | qadma | conjunctive (joining) |
| עָשָׂ֥ר | "ten" | merkha | conjunctive (joining) |
| יוֹם֙ | "day" | pashta | disjunctive (a pause) |

Genesis 32:23, the reading's English: "And he rose that night, and took his two wives and his two maidservants and his eleven children, and crossed the ford of the Jabbok."

| Hebrew | gloss | accent | the store's own label |
|---|---|---|---|
| אַחַ֥ד | "one" | merkha | conjunctive (joining) |
| עָשָׂ֖ר | "ten" | tifcha | disjunctive (a pause) |
| יְלָדָ֑יו | "his children" | etnachta | disjunctive (the middle pause) |

Second Kings 9:29, the reading's English: "And in the eleventh year of Joram son of Ahab, Ahaziah became king over Judah."

| Hebrew | gloss | accent |
|---|---|---|
| אַחַ֣ת | "one" | munach (joining) |
| עֶשְׂרֵ֣ה | "ten" | munach (joining) |
| שָׁנָ֔ה | "year" | zaqef qatan (a pause) |

Joshua 15:51, the reading's English: "And Goshen and Holon and Giloh: eleven cities with their villages."

| Hebrew | gloss | accent |
|---|---|---|
| אַֽחַת | "one" | no accent of its own; joined to the next word |
| עֶשְׂרֵ֖ה | "ten" | tifcha (a pause) |

In all four, the "one" joins forward. In all twelve spoon-verses, the "one" stops. The accents sort the sixteen seats into exactly the two piles the meaning requires, with no exceptions.

There is a second witness inside Naso. Numbers 7:13's "one tray" carries a revia on its "one", also a disjunctive. That "one" stops too, and it is the same shape: one vessel, then its weight.

And there is the proof that needs no grammar at all. Numbers 7:86, Onkelos: "Twelve golden spoons filled with fragrant incense; each spoon weighed ten shekolim (shekels) according to sanctuary weights. The total of the golden spoons is one hundred twenty shekolim (shekels)."

| Hebrew | gloss | accent | the store's own label |
|---|---|---|---|
| כַּפּ֨וֹת | "spoons" | qadma | conjunctive (joining) |
| זָהָ֤ב | "gold" | mahapakh | conjunctive (joining) |
| שְׁתֵּים | "two" | joined by a maqqef (a hyphen) | |
| עֶשְׂרֵה֙ | "ten" (so: twelve) | pashta | disjunctive (a pause) |
| מְלֵאֹ֣ת | "full of" | munach | conjunctive (joining) |
| קְטֹ֔רֶת | "incense" | zaqef qatan | disjunctive (a pause) |
| עֲשָׂרָ֧ה | "ten" | darga | conjunctive (joining) |
| עֲשָׂרָ֛ה | "ten" | tevir | disjunctive (a pause) |
| הַכַּ֖ף | "the spoon" | tifcha | disjunctive (a pause) |
| עֶשְׂרִ֥ים | "twenty" | merkha | conjunctive (joining) |
| וּמֵאָֽה | "and a hundred" | silluq | disjunctive (the verse's end) |

The parser's output: `[12, 10, 120]`. The "ten, ten" is distributive by rule three, ten per spoon. Twelve spoons at ten each is a hundred and twenty. If each spoon had weighed eleven, the total would be a hundred and thirty-two, and the ink says a hundred and twenty. The total closes only one way, and it is the way the accents read.

That is move M-26, THE ACCENT READ, registered in the move catalog: when the consonants leave two readings, the accents on the words are a parse instrument, and the accent's kind decides. It is owed to the parser at Naso's compile.

## Chapter Six. Three Words In One Spelling.

Bamidbar taught that the vowel points separate homographs. Naso found three more, and measured each across the whole Bible.

**Trespass against from-upon.** The consonants מעל ("trespass", or "from upon"). Pointed מַעַל, "trespass", 13 seats. Pointed מֵעַל, "from upon", 191 seats.

Numbers 5:6, Onkelos: "Speak to the children of Israel: When a man or a woman commits any of the sins against man, acting treacherously against the LORD, and that person is guilty."

| Hebrew | gloss | accent |
|---|---|---|
| לִמְעֹ֥ל | "to commit" | merkha (joining) |
| מַ֖עַל | "a trespass" | tifcha (a pause) |
| בַּיהוָ֑ה | "against the LORD" | etnachta (the middle pause) |

Onkelos renders the trespass as lying, "acting treacherously", at 5:6, 5:12 and 5:27, and the reading recorded that as the translation's own insertion.

**Steeping against minister.** The consonants משרת ("steeping", or "minister"). Pointed מִשְׁרַת with a hiriq (the short i) under the mem, "steeping", one seat, Numbers 6:3. Pointed מְשָׁרֵת with a sheva (the silent half-vowel), "minister", seven seats.

Numbers 6:3, Onkelos: "From new or old intoxicating wine, he must abstain. Vinegar made from new wine and vinegar made from old wine he shall not drink; anything steeped in grapes he shall not drink; moist grapes or dried grapes he shall not eat."

| Hebrew | gloss | accent |
|---|---|---|
| וְכָל | "and any" | joined by a maqqef (a hyphen) |
| מִשְׁרַ֤ת | "steeping of" | mahapakh (joining) |
| עֲנָבִים֙ | "grapes" | pashta (a pause) |

The module found the one seat by counting the pointed forms: eight tokens with those consonants, seven with the sheva, one with the hiriq, and the one is here.

**The Voice speaking itself.** The consonants מדבר ("wilderness", "speaking", or "speaking itself"). Three words live in them. Pointed מִדְבָּר, "wilderness", 45 seats. Pointed מְדַבֵּר with a sheva under the mem, "speaking", 26 seats. Pointed מִדַּבֵּר with a hiriq under the mem, a dagesh (the doubling dot) in the dalet and a tsere (the long e) under the bet, the reflexive "speaking itself", 8 seats.

Numbers 7:89, Onkelos: "When Moses would enter the Tent of Meeting to speak with Him, he would hear the Voice being spoken to him from above the Ark-cover which is atop the Ark of the Testimony from between the two cherubim; and He spoke to him."

| Hebrew | gloss | accent |
|---|---|---|
| וַיִּשְׁמַ֨ע | "and he heard" | qadma (joining) |
| אֶת | the object marker | joined by a maqqef (a hyphen) |
| הַקּ֜וֹל | "the Voice" | geresh (a pause) |
| מִדַּבֵּ֣ר | "speaking itself" | munach (joining) |
| אֵלָ֗יו | "to him" | revia (a pause) |

Onkelos hears the reflexive and renders it "being spoken", and he renders the verse's closing active verb the same way, "and He spoke to him" as a voice speaking of itself. The module classified every token of those consonants in the Bible by a small parser over the consonant groups and their marks, and the reflexive came to exactly eight: this verse, Exodus 34:33 ("and Moses finished speaking with them"), Ezekiel 2:2, Ezekiel 43:6 and four more.

The lesson repeats Bamidbar's. A typed pointed form is not the database's bytes. The marks on a letter can be stored in more than one order. So the module compares by consonant groups, each letter with the set of marks attached to it, and never by string equality on a form typed by hand.

## Chapter Seven. The Clock Runs Backward Twice.

The world has a clock. It counts days. Day zero is the first day of the world's own era, and every event on the tape is stamped with the day it happened. A year is derived from the day through the era's calendar, so the ask-tool prints a year on every row.

The clock moves by markers. A marker is a verse that states a date, and the engine stamps the clock at that verse. Most markers move forward, because most of the Bible is told in order. A few state a day earlier than the clock already stands. Those are retrograde markers. The counter does not move back. The marker is logged with its stated day and a flag, and the events it governs are dated by it.

The tradition names this shape on its own page, on exactly these verses. Pesachim 6b:7, in the Talmud's words: "Rav Menashiya bar Tachlifa said in the name of Rav: That is to say that there is no earlier and later, i.e., there is no absolute chronological order, in the Torah, as events that occurred later in time can appear earlier in the Torah." The Gemara asks it about Numbers 1:1 and Numbers 9:1, the first month and the second, written in the wrong order.

Here are the three dates.

Exodus 40:17, the reading's English: "And it was in the first month, in the second year, on the first of the month, the tabernacle was set up."

| Hebrew | gloss |
|---|---|
| בַּחֹ֧דֶשׁ | "in the month" |
| הָרִאשׁ֛וֹן | "the first" |
| בַּשָּׁנָ֥ה | "in the year" |
| הַשֵּׁנִ֖ית | "the second" |
| בְּאֶחָ֣ד | "on the first" |
| לַחֹ֑דֶשׁ | "of the month" |

On the tape this is day 894,698 of the world, the date (2, 1, 1) of the exodus era: year two, month one, day one. Leviticus 9:1, the eighth day of the installation, stamps the same day.

Numbers 1:1, the reading's English: "And the LORD spoke to Moses in the wilderness of Sinai, in the tent of meeting, on the first of the second month, in the second year of their going out of the land of Egypt, saying."

| Hebrew | gloss |
|---|---|
| בְּאֶחָד֩ | "on the first" |
| לַחֹ֨דֶשׁ | "of the month" |
| הַשֵּׁנִ֜י | "the second" |
| בַּשָּׁנָ֣ה | "in the year" |
| הַשֵּׁנִ֗ית | "the second" |

On the tape this is day 894,728, the date (2, 2, 1). Thirty days after the erection, as Nisan has thirty days. It is a forward marker, and the journal's line on it says so:

```
"kind":"run.marker", "verse":"Num 1:1", "placement":"text_constrained", "retrograde":false,
"value":"... the tape's FORWARD marker whose successor in the text, 9:1-5, is earlier in time (Pesachim 6b:6-8)"
```

Numbers 9:5, the reading's English: "And they kept the Passover in the first month, on the fourteenth day of the month, between the evenings, in the wilderness of Sinai; according to all that the LORD commanded Moses, so did the children of Israel."

| Hebrew | gloss |
|---|---|
| בָּרִאשׁ֡וֹן | "in the first" |
| בְּאַרְבָּעָה֩ | "on the four" |
| עָשָׂ֨ר | "ten" (so: fourteenth) |
| י֥וֹם | "day" |
| לַחֹ֛דֶשׁ | "of the month" |

The fourteenth of the first month is day 894,711, thirteen days after the erection and seventeen days before Numbers 1:1. The text reaches it eight chapters after 1:1. So on the running world the journal's line reads:

```
"kind":"run.marker", "verse":"Num 9:5", "retrograde":true, "stated":894711, "op":894728
```

The counter stayed at 894,728. The stated day 894,711 is carried on the marker, and the flag is set. That is the first retrograde marker inside Numbers.

The second was found at Naso's reading and is owed to its compile. Numbers 7:1, Onkelos: "It came to pass, on the day Moses finished erecting the Tabernacle, and he anointed it and consecrated it and all of its utensils, and the Altar and all its utensils, and he anointed them and consecrated them."

| Hebrew | gloss | accent |
|---|---|---|
| וַיְהִ֡י | "and it was" | pazer (a pause) |
| בְּיוֹם֩ | "on the day" | telisha qetana (joining) |
| כַּלּ֨וֹת | "of the finishing of" | qadma (joining) |
| מֹשֶׁ֜ה | "Moses" | geresh (a pause) |
| לְהָקִ֣ים | "to set up" | munach (joining) |
| אֶת | the object marker | joined by a maqqef (a hyphen) |
| הַמִּשְׁכָּ֗ן | "the tabernacle" | revia (a pause) |

"The day Moses finished setting up" is Exodus 40:17's day. The ink module found the phrase "on the day of the finishing of Moses" at exactly one seat, this one, and the verb "and Moses finished" at three: Exodus 40:33, the erection's own finishing, Exodus 34:33 and Deuteronomy 32:45. So 7:1 is dated (2, 1, 1), day 894,698, a month before 1:1's (2, 2, 1). The twelve days of the princes, 7:12 to 7:83, are the first twelve days of Nisan, and the unclean men of Numbers 9:6 come on the fourteenth. One month of tape, three markers, two of them backward.

## Chapter Eight. Events, Bounds And The Cursor.

Every event on the tape carries a bound: the day of the last forward marker before it and the day of the next forward marker after it. The bound is the audit's instrument. It says between which two dated verses this event must sit. The right edge is written when the next marker arrives.

Here is a real line from the running world's journal, the census law's write when the count is taken, with its bound:

```
"kind":"run.write", "effect":"counted", "day":894728, "bound":[894728, 908688],
"ref":"Num 1:17-19 — and Moses and Aaron took these men... and he counted them in the wilderness of Sinai;
       1:46 six hundred thousand and three thousand and five hundred and fifty"
```

The bound runs from 894,728, Numbers 1:1's own day, to 908,688, the daughters' plea in the fortieth year, the next forward marker after it. Every event of the census, the camp and the Levites' service carries that same pair, because no verse between them states a date. On the running world, 46 of the 70 Numbers lines carry a bound. The other 24 are the lines a retrograde marker dates, the second Passover's, and those carry the stated day 894,711 instead of a pair, because a retrograde marker closes no bound.

The cursor is the loop's replay instrument. It runs the tape from the beginning to the left edge of a named verse and stops, and the journal it writes must be a byte-identical prefix of the base's journal, or the replay is refused.

Bamidbar's compile found the cursor's bound rule. The cursor check had sat in the marker function before the bound-closing step. So a replay stopped at a marker left the previous bound open where the base had it closed, and the audit refused the Bamidbar lines. The fix: a forward marker at the cursor closes the bounds behind it before the world stops, as the full run would. A retrograde marker at the cursor closes nothing, as in the run.

And the limit that remains, measured and recorded rather than hidden: a cursor inside a bound whose closing marker lies beyond it is refused. Numbers 15:32 is such a place. It sits between 1:1's marker and 27:1's. The base's line for every event of that bound already carries the right edge, 908,688, which a replay stopped at 15:32 cannot know, and the chain hashes those bytes. So the cursor stands at a forward marker's verse, or anywhere after the last marker. The daughters' plea at Numbers 27:5 is such a place, and the first scenario ran there.

## Chapter Nine. The Shelf's Heads Are Found By Position.

The reading shelf for Numbers is the Sifrei on Numbers, read beside Onkelos. Its export comes as numbered sections, piskaot (sections), each headed by the verse it opens on. Three of those heads are wrong, and each was caught by the ledger script's assert, never by eye.

**Piska 62, headed "3:24".** By position it sits between piska 61, headed 8:4, and piska 63, headed 8:25. By its own words it opens on 8:24. Here is the row as the export has it:

"(Bamidbar 3:24) 'This is what applies to the Levites. From the age of twenty-five, etc.' ... (Bamidbar 8:24) 'From the age of twenty-five and up, etc.': One verse states 'From the age of twenty-five and up,' and another (Ibid. 4:23) 'From thirty years and up.' How are these two verses to be reconciled? From the age of twenty-five for learning the Levitical service, and from the age of thirty, for serving."

A mistyped chapter digit, 8 written as 3. Bamidbar's ledger script asserted that no head lies inside chapters 1 to 4 and found this one. The row was read where its subject is, at 4:3's thirty, and filed in the research log.

**Piska 19, headed "5:298".** Between piska 18 on 5:27 and piska 20 on 5:29. Its first words: "'And if the woman had not been defiled and she be clean': What is the intent of this?" That is Numbers 5:28, with a stray digit.

**Piska 34, headed "6:150".** Between piska 33 on 6:14 and piska 35 on 6:18. Its first words: "'And a basket of unleavened bread': general (any kind); 'fine flour, cake mixed with oil': particular." That is Numbers 6:15.

Naso's ink module carries a head-fix table naming both, and asserts that with the two digits corrected the fifty-eight piskaot (sections) of Naso head in monotone order from 5:1 to 7:89. The export itself is evidence and is never edited. The heads are found by position and asserted between their neighbors.

The tent's fourth sitting had found the same class one more way. Inside the daughters' stretch sits a piska headed with a Deuteronomy verse, the shelf's own excursus, and it is read with the stretch. And the shelf's end is computed: there is no piska on chapter 36, and that is recorded as the shelf's shape, not as a gap of ours.

## Chapter Ten. The Sifrei States Its Own Inference Law.

The middot (the rules of inference) are how the tradition gets from a verse to a ruling. The project keeps them in a file with their case law. On Naso, the Sifrei says its rules out loud, on the verses, and eight entries went into that file. Here are the Sifrei's own words for each, with the verse.

**The rule of repetition.** On Numbers 5:6, piska 2: "This is a rule in the Torah: Any section stated in one place in the Torah, missing one thing, and repeated in a different place is repeated only for the sake of the thing that is originated. R. Akiva says: Everything stated therein must be expounded."

The section is the trespass law of Leviticus 5, repeated in Numbers 5. The new thing is the stolen property of a convert who died without heirs. The tradition's own statement of a move the project already had, the second seat's delta, and the rival reading is carried beside it.

**No punishment by an a fortiori.** On Numbers 5:3, piska 1: "But even if this were not mentioned, I could derive it a fortiori ... If so, why is 'and they shall not make unclean their camps' needed? To teach that we do not punish by an a fortiori argument. R. Yehudah says: There is no need for the verse to teach that they are sent out of the camp of the Shechinah (the Divine Presence), for it follows a fortiori."

The verse the inference would have made redundant is written because the inference cannot carry a penalty. And R. Yehudah's dissent, who does punish by it, is carried.

**The general-particular against the a fortiori.** On Numbers 5:15, piska 8. The Sifrei sets a precedence rule between two of the thirteen: when a general-and-particular reading and an a fortiori collide and both can be satisfied, the a fortiori is not defeated. Its output is a parameter the machine now carries: merit suspends the bitter waters for three, nine or twelve months, or not at all, by named authorities.

**A general that adds to the particular.** On Numbers 6:4, piska 24: "'of all that is made from the grape-vine': I might think that leaves and sprouts, too, are included; it is, therefore, written 'from the kernels to the husk': Just as the specific instance is of fruit and residue of fruit, so, only these are included, to exclude leaves and sprouts. R. Eliezer says: Leaves and sprouts are also subsumed."

**The three-facet paradigm.** On Numbers 5:10, piska 6. The Sifrei grades a paradigm's strength by the facets it shares: "I learn a thing of three facets from a thing similar in three facets, not from one similar in one or two." The refutations from the heave-offering and the first fruits are answered by the count.

**The circular a fortiori fails; the identity on an extra word decides.** On Numbers 6:5 and 6:20, piskaot 25 and 31. Wine, shaving and corpse-uncleanness each refute the other's inference. The Sifrei on 6:6, piska 31: "You reason as follows: Since a Nazirite is forbidden to drink wine and to become tamei (unclean), then if I have learned re wine that the days after his Naziritism are equated with the days in the midst of his Naziritism until he brings the offering, so, re tumah (uncleanness). And, furthermore, it follows a fortiori ... No, this may be so with wine, where no act in its category is permitted to a Nazirite ... as opposed to tumah (uncleanness), where an act in its category is permitted." The argument goes round. What decides is a word measured extra: 6:20's "the nazirite may drink wine" names the nazirite where the clause needs no subject, and the ink module computed that clause's one seat. A recorded failure mode of the a fortiori, and a verbal analogy received on a superfluous word.

**The eleventh and thirteenth rules, stated on their verses.** On 6:20, piska 37, the eleventh: whatever was included in a general and departed for a new learning may not be returned until Scripture returns it. The breast and thigh are kept out of the nazirite's shoulder-law. And on 7:89, piska 58, the thirteenth, in the Sifrei's words: "It is impossible to say from the tent of meeting, for it is already written 'from above the kaporeth (the ark cover),' and it is impossible to say 'from above the kaporeth,' for it is already written 'from the tent of meeting.' How, then, are these two verses to be reconciled? This is a rule in the Torah: Two verses which contradict each other are to remain in their place until a third verse comes and reconciles them." Leviticus 1:1 against Exodus 25:22, and Numbers 7:89 the third.

**The crossed parameter.** On 6:9, piska 28: "If in the instance of sotah (the suspected wife), where inadvertency was not equated with wilfullness, doubt was equated with certainty, then here, in the instance of the Nazirite, where inadvertency was equated with wilfullness, how much more so should doubt be equated with certainty! It is, therefore, written 'And if one died on him', to exclude an instance of doubt."

The suspected wife's law equates doubt with certainty but not inadvertence with intent. The nazirite's law is the reverse. Each a fortiori is refuted by the other engine's difference. It is recorded as a paired setting on two laws.

The lesson for the machine: the rules about the rules are data on the shelf's own pages, and they are read at the verses where the shelf states them, not imported from a list.

## Chapter Eleven. A Case Installs A Rule Into A Law.

The tent's cases are the places where the run halts because the ink says the law was not yet declared. Numbers has three of them, and they have three forms.

**The first form: custody and a declaration owed.** Leviticus 24:12, the reading's English: "And they placed him in the guard, to declare to them at the mouth of the LORD."

**The second form: stand and wait.** Numbers 9:8, the reading's English: "And Moses said to them: stand, and I will hear what the LORD commands concerning you."

**The third form: the judgment brought near.** Numbers 27:5, the reading's English: "And Moses brought their judgment near before the LORD."

The Talmud reads the third exactly so. Sanhedrin 8a:4: "In this instance, when Zelophehad's daughters presented their case to Moses, he did not know the answer himself and was compelled to ask God." And it records the other reading beside it: "If I have learned the halakha (the law), I have learned it. And if not, I will go and learn it."

The wood-gatherer is the case that taught the sharpest lesson, because the law already existed.

Exodus 31:14, the reading's English: "And you shall keep the Sabbath, for it is holy to you; those who profane it shall surely be put to death, for whoever does work on it, that soul shall be cut off from among its people."

The liability was declared at Sinai. What was not declared was the mode of death. Then Numbers 15:32 to 36, the reading's English, verse by verse:

"And the children of Israel were in the wilderness, and they found a man gathering wood on the Sabbath day." (15:32)

"And they brought him near, those who found him gathering wood, to Moses and to Aaron and to all the congregation." (15:33)

"And they placed him in the guard, for it had not been declared what should be done to him." (15:34)

"And the LORD said to Moses: die shall die the man; stone him with stones, all the congregation, outside the camp." (15:35)

"And all the congregation brought him outside the camp and stoned him with stones, and he died, as the LORD commanded Moses." (15:36)

The Sifrei on 15:34 and 15:35, piska 114: "But is it not written (Shemot 31:14) 'He who profanes it shall be put to death'? What, then, is the intent of 'For it was not made clear'? He did not know with what specific type of death until it was told to Him by the Holy One. 'And the L-rd said to Moses: Die, shall die the man': this is the judgment for all the generations. 'stone him with stones': in this particular instance."

So the tent's output at 15:35 installs a mode into a law that predates the case. The machine records that as a rule installed into an existing law's cell, not as a new law. The ask-tool shows the tent's installed rules as they stand today:

```
ASK who the_tent_of_meeting rule_installed — the world cold_run_sequence/seed_isaac: 5 rows
  Lev 24:13-14 | day=894698 | value=law_lev24
  Num 9:9-14   | day=894728 | value=law_pesach_sheni
  Num 15:35    | day=894728 | value=law_sabbath:death_run
  Num 27:6-11  | day=908688 | value=law_zelophehad
  Num 36:5-9   | day=908688 | value=law_zelophehad:tribe_transfer
```

Five rows. Three are whole laws born of a case. Two are cells inside a law, named with a colon: the Sabbath law's death mode at 15:35, and the tribal-transfer rule inside the daughters' law at 36:5 to 9, the second output on the same case, relayed in Moses' mouth.

And the companion lesson: an Exodus law can wait for a Numbers act. The Sabbath law had been on the tape since the covenant, and no act on the tape had ever profaned the Sabbath. At Numbers 15:32 it fired for the first time. The ledger row says who wrote it:

```
effect=labor_barred | written_by=law_sabbath | verse=Num 15:32-33 | value=detaching
```

The daemons-fired count moved by two on that sitting, and the prediction had to be retyped from the stitcher's print.

## Chapter Twelve. Ask The Ledger After The First Run.

The run's tuple is a fingerprint: event counts, entity counts, open timers, closes. Before every run the tuple is predicted, and a match is the first gate. The wood-gatherer's first run matched. Then the ledger was asked, and the match had hidden an open entry.

Here is the ask-tool's answer today, the whole ledger of the wood-gatherer:

```
ASK ledger the_wood_gatherer — the world cold_run_sequence/seed_isaac: 5 rows
  labor_barred                 | block  | written_by=law_sabbath   | state=written
  put_to_death                 | body   | written_by=law_sabbath   | closed_by=Num 15:36 | state=closed
  stoned                       | body   | written_by=law_sabbath   | closed_by=Num 15:36 | state=closed
  warned_specifying_the_labor  | status | written_by=law_mekoshesh | state=written
  in_custody                   | body   | written_by=law_tent      | closed_by=Num 15:36 | state=closed
```

On the first run the second row, the death sentence, stood open. The Sabbath law had written it as a body entry, the way the blasphemer's law never had, and "and he died" at 15:36 closed the stoning and the custody but nobody had told the execution branch to close a death sentence too. The tuple could not see it, because the tuple counts closes and the prediction had counted what the hand expected.

The fix was one branch: the tent's execution now closes the death sentence, and the close returns false where no such entry stands, so the blasphemer, who never carried one, is unharmed. The predicted closes were retyped from 82 to 83 before the second run, and the second run matched.

The lesson has a name in the record: a body entry is closed by the deed. Read the ledger with the ask-tool after the first run, every body entry the deed performs, before trusting a "nothing to write".

## Chapter Thirteen. The Hand Miscounts, The Script Counts.

This is the lesson every sitting of Numbers logged, and the record keeps the numbers so that the pattern cannot be argued with.

| sitting | the hand said | the instrument said |
|---|---|---|
| the wood-gatherer's guard | 33 expectations | 34 |
| the daughters' guard | 46 expectations | 55 |
| the daughters' docket | 107 rows, verdicts 10/56/22 | 101 rows, verdicts 11/57/26 |
| Bamidbar's guard | 62 expectations | 66 |
| Bamidbar's debits on the Levites | three | four |
| Bamidbar's entity count | 262 | 261 |
| Naso's claims | 52 | 51 |
| Naso's Pedahzur at 10:23 | one token | two |
| Naso's princes at 7:10 | one spelling | two |

The last two need the ink. Numbers 7:10, Onkelos's sense: "The leaders brought the dedication of the altar on the day it was anointed, and the leaders brought their offering before the altar."

| Hebrew | gloss | accent |
|---|---|---|
| וַיַּקְרִ֣יבוּ | "and they brought near" | munach (joining) |
| הַנְּשִׂאִ֗ים | "the leaders" (spelled without the yod) | revia (a pause) |
| ... | | |
| וַיַּקְרִ֧יבוּ | "and they brought near" | darga (joining) |
| הַנְּשִׂיאִ֛ם | "the leaders" (spelled with the yod, without the second) | tevir (a pause) |

Two spellings of one word in one verse. The hand had typed the first spelling where the second stands. The cut by consonants missed, the miss was appended to the failure list, and the fact was retyped from the shelf's own bytes.

The fix that stuck was structural. Naso's ink module holds every fact as an assert. A small driver executes the module statement by statement and lists every failing assert at once instead of stopping at the first. On its first run nine asserts failed, and each was a measurement: an ordinal indexed off the wrong word, a token count, a spelling, a sort order, a pointed form whose marks were stored in a different order than the hand had typed. None was a typo in the ink. All were typos in the hand.

The rule as recorded: every "measured" claim goes through a script, and a miss is evidence. Read it, then retype from the instrument.

## Chapter Fourteen. "Already Compiled" Is Measured Before It Is Believed.

Twice the map said a span was done, and twice a grep found otherwise.

At the tent's second sitting the map said the second Passover's code was already at 9:10 to 14 in the Passover engine's cells. A grep of the runners found no Numbers 9 cell. The whole process ran in one sitting instead: reading, unit, compile, wrap, tape.

At the third sitting the map said "the compile" of the wood-gatherer was owed. A grep of the runners for the span's verses found that the Exodus engine's Sabbath cell had already imported the mode from this verse's run, on September 7, before Numbers had a reading. The runner's own header records it: "the Exodus engine's cell sabbath('death_run'), which imported it from this span's run ... measured, and given its home here." The compile sitting then compiled only what no runner held: the forewarning that names the labor, the custody rule, the stoning protocol, the hanging fork, the labor and the identity as data rows.

The lesson is symmetric. A map's "already compiled" and a map's "the compile" are both claims. Grep the runners for the span's verses before either is believed. A forward import by name may already hold the answer.

## Chapter Fifteen. The Store Drops The Large Letters.

The snapshot store is the immutable evidence layer. Every frozen unit's text gate is checked against its bytes, and every frozen hash depends on them. At the daughters' sitting a claim's own check found that the store is missing letters.

The Masorah (the scribal tradition) marks a few letters in the Torah to be written large. The Torah XML carries them as a marked segment. The store's builder dropped every such segment. Four segments in the five books, three words broken.

Leviticus 11:42, as the store reads it: גָּח֜ for גָּחוֹן ("belly"). The large vav, the Torah's middle letter, and its nun are gone.

Numbers 27:5, as the store reads it: מִשְׁפָּטָ֖ for מִשְׁפָּטָן ("their judgment"). The large final nun is gone. It is the store's only token ending in a bare slash, one of 80,052.

Deuteronomy 6:4, as the store reads it: שְׁמַ֖ יִשְׂרָאֵ֑ל יְהוָ֥ה אֱלֹהֵ֖ינוּ יְהוָ֥ה אֶחָֽ, "Hear, Israel, the LORD our God, the LORD is one", with the large ayin of "hear" and the large dalet of "one" absent.

It was found because claim NM27-04 counted the tokens of "their judgment" on the store and got zero, while the ledger script's count on the Tanakh database got one. The ink itself explained the delta. The consequences are recorded, not patched: the unit's step at that verse mirrors the truncated token with the finding on it, the manifest checks run on the stem, the counts run on the Tanakh database. The snapshot is not touched, because rebuilding it moves every frozen hash, and that is the owner's word.

The daughters' halt verse is the one case verse of the four that carries a majuscule (a large letter) in the ink.

## Chapter Sixteen. What Is Owed.

The compile of Naso, on Bamidbar's order. The measurements first. Then the design written in the walk map before any type. The exam docket by the union rule. Probe rows for the four parser gaps, written to fail. The types, the declaration, the gates to fail. Then the parser: the accent rule of M-26, the construct "two of", the word for eleven, the "one" before a weight; the stitcher's marker verification; the corpus-wide diff read again. Then the runner: the send-out from the camp, the trespass and its fifth, the priestly gifts, the suspected wife's engine with its parameters, the nazirite's engine, the blessing's form table, the wagons two and four and four and eight, the dedication's twelve days as timers with the totals as checkpoints, the Voice's thirteen exclusions. The recorder, the stitcher, and Numbers 7:1's marker placed retrograde at (2, 1, 1). The predicted tuple, the run, the gates, the journal gate, the sweep, the records.

Behind it, in order: Beha'alotcha, Numbers 8:1 to 12:16, with chapter 9 frozen and skipped. And the smaller debts the walk has named: the continual meal-offering's call from Numbers 4:16 into the meal-offering engine, the two thousand cubits of Numbers 35:5 that the parser leaves silent until Masei, and the cursor inside a bound.

The walk's own sentence for all of it: the ledger is written before the seats, the design before the types, the probes before the code, the tuple before the run, and the hand's number is never the record's until the instrument has said it.
