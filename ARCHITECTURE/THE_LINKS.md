# THE LINKS — how the laws are wired to each other, taught from two examples and a fourth book

**A tutorial (rewritten 2026-09-07 for the general reader; five
examples from the fourth book added 2026-09-13).** This
document shows one thing: that the laws of the Bible depend on each
other across books, in ways a program can follow and a machine can
check. Thirteen dependencies are worked in full — eight from the
first three books, five from the fourth — one of each kind. The
complete list — 455 references, 48 transfers, 9 open hypotheses, and
143 edges that carry no rule at all, over 482 edges and 173 pointers
as of 2026-09-13 — lives in the program's own records; this document
teaches you how to read one.

*Verses are given in plain modern English, rendered from the Hebrew
and checked against it. Where one Hebrew word matters it is shown
once, with its English beside it. Every verse cited is quoted whole.*

---

## The idea in one paragraph

Real programs are never one long file of instructions. They are built
in parts, and the parts depend on each other: one part calls a
procedure defined in another, fetches a number stored in another, or
points at a recipe written once and reused. The proof that something
is ONE designed system — and not a pile of separate documents — is
exactly this: a part that is incomplete without a definition written
somewhere else, where the somewhere else exists, matches, and
answers. The Bible's laws have that structure, and this document
shows you two places where a verse in one book cannot be run without
a verse in another.

---

## Example 1 — "eye for eye": a verse in Exodus that gets its meaning from Leviticus

**The story, in plain words.** In Exodus, among the first laws given
after the Ten Commandments, there is a famous list: life for life,
eye for eye, tooth for tooth. Read alone, it sounds like a rule about
maiming the person who maimed you. But the verse never says what
"for" means — take the eye, or pay what the eye was worth? The answer
is not in Exodus at all. It is three books away, in Leviticus, where
the same list appears again — this time sitting right next to a
verse about PAYING for an animal you killed, and followed by a verse
saying the law must be one and the same for everyone. The teachers
of the tradition read those neighbors and concluded: it means money.
The Exodus verse is a call to a definition that lives in Leviticus.
Take the Leviticus verses away, and the Exodus verse cannot be run.

**What crosses the link, one line each.**
- Exodus names the tariff — the list of injuries.
- Leviticus supplies the meaning of "for": payment, not maiming.
- Leviticus also adds one injury Exodus lacks — "fracture for
  fracture" — the mark of the place where the list is defined.

**The verses.** The call first. Listen for "in exchange for" — one
Hebrew word, repeated. Exodus 21:23-25:

> "But if harm does follow, then you give life in exchange for life,
> eye in exchange for eye, tooth in exchange for tooth, hand in
> exchange for hand, foot in exchange for foot, burn in exchange for
> burn, wound in exchange for wound, bruise in exchange for bruise."

The repeated word is תַּחַת (tachat, "in exchange for," "in place
of"). Now the definition, in Leviticus. Listen for "pay," then the
same list, then "one law." Leviticus 24:18-22:

> "Whoever kills an animal must pay for it: life in exchange for
> life. When a man injures his fellow, what he did is done to him:
> fracture in exchange for fracture, eye in exchange for eye, tooth
> in exchange for tooth; the injury he gave a person is given to him.
> Whoever kills an animal pays for it; whoever kills a person is put
> to death. You shall have one law, the same for the foreigner and
> the native-born; for I am the LORD your God."

The argument the tradition draws from these neighbors: the list is
bracketed on both sides by PAY verbs about animals; and a law that
must be "one and the same for everyone" cannot be literal maiming,
because taking a blind man's eye and a healthy man's eye are not the
same penalty — money is what makes it equal.

**What the tradition says.** The tradition's table of decided cases
— the Mishnah — states the verdict and, in the same breath, how the
amount is figured (Mishnah Bava Kamma 8:1):

> "Someone who injures another person owes him for five things: the
> damage, the pain, the medical care, the lost time, and the
> humiliation. The damage — how? If he blinded his eye, cut off his
> hand, or broke his leg: we look at the injured man as if he were a
> slave being sold in the market, and estimate what he was worth
> before and what he is worth now."

And the Talmud — the recorded discussion behind the rulings — records
the very moment the reading reaches into Leviticus for the meaning
(Babylonian Talmud Bava Kamma 83b):

> "You might think it means: he blinded his eye, so we blind his eye;
> he cut off his hand, so we cut off his hand; he broke his leg, so
> we break his leg. The verse teaches otherwise: 'whoever strikes a
> person' and 'whoever strikes an animal' — just as striking an
> animal means payment, striking a person means payment."

The next lines of that page are the teachers arguing over WHICH
Leviticus verse the link binds to — one objects that verse 21 is
about killing, and the answer moves the anchor to verse 18, which
sits right beside verse 19. It reads like two programmers reviewing
where a reference points.

**What the link answers, and what it does not.** The link settles
the KIND of answer: money, never maiming. It does not settle the
AMOUNT. The Mishnah's five payments each have their own source:
- Medical care and lost time are stated outright two verses earlier.
  Exodus 21:19: "If he gets up and walks around outside on his cane,
  the one who struck him is cleared; he pays only for the man's lost
  time, and sees that he is fully healed."
- The damage is figured by the market estimate in the Mishnah's own
  words above — a procedure, not a fixed number.
- The pain is drawn from "wound in exchange for wound."
- The humiliation comes from yet another book. Deuteronomy 25:11-12:
  "When men are fighting, one with another, and the wife of one comes
  up to rescue her husband from the man hitting him, and reaches out
  her hand and grabs him by his private parts — you cut off her hand;
  show no pity." The tradition reads "cut off her hand" as a money
  payment for the shaming (Babylonian Talmud Bava Kamma 28a: "cut off
  her hand — money").

And the text shows it knows how to state an amount when it means
one. Seven verses after the tariff, Exodus 21:32: "If the ox gores a
male or female slave, the owner pays their master thirty shekels of
silver, and the ox is stoned." A fixed sum for the slave; an estimate
for the free man. Where a number is the law, the number is written;
where the answer must fit the case, a procedure is written instead.

**Now the program's terms, in one paragraph.** One part of a program
CALLS another when it says: run the procedure defined over there and
bring me its answer. The program for Exodus 21 does not contain the
damage verdict. It calls a function named talion ("retaliation" —
the traditional name for this law), which lives in the program for
Leviticus 24, and the answer — pay money — comes back through the
call. Delete the Leviticus file and the Exodus file stops working.
That is not a design choice of ours; it is the text's own structure,
transcribed.

**For the record.** The phrase "eye in exchange for eye" — with the
word tachat — stands at exactly TWO places in the whole Bible,
Exodus 21:24 and Leviticus 24:20; "fracture in exchange for fracture"
at exactly ONE, the Leviticus side. The same list of injuries appears
once more with a different connecting word, in the law of false
witnesses — Deuteronomy 19:21: "Show no pity: life for life, eye for
eye, tooth for tooth, hand for hand, foot for foot." There the word
is בְּ (be-, "for"), not tachat; it is a different case (a witness's
plot, not an injury), and the tradition treats it as its own law.

---

## Example 2 — "as prescribed": one word in Leviticus 5 that stands for a whole procedure in Leviticus 1

**The story, in plain words.** Leviticus 5 describes a sin offering
for a poor person who cannot afford a lamb: two birds instead, one as
a sin offering and one as a burnt offering. For the first bird, the
verses spell out exactly what the priest does. For the second bird,
they do not. They say only: make it a burnt offering "as prescribed."
Prescribed where? Four chapters earlier, in Leviticus 1, where the
burnt offering of a bird is laid out step by step — and nowhere else
in the Bible. One word in chapter 5 stands in for a whole procedure
in chapter 1. A recipe book does the same thing when it says
"prepare crust as on page 12" instead of reprinting the crust recipe.

**What crosses the link, one line each.**
- Chapter 5 names the type of offering — a burnt offering — and says
  "as prescribed."
- Chapter 1 holds the only written procedure for a bird burnt
  offering.
- The two birds get DIFFERENT procedures, which is exactly why
  chapter 5 needed to point outward for the second one.

**The verses.** The pointer first. Listen for "as prescribed."
Leviticus 5:10:

> "And the second bird he makes a burnt offering, as prescribed; the
> priest makes atonement for him for the sin he committed, and he is
> forgiven."

"As prescribed" is one Hebrew word: כַּמִּשְׁפָּט (ka-mishpat,
"according to the rule"). Now the procedure it points to. Listen for
what happens to the head, the blood, and the wings. Leviticus
1:15-17:

> "The priest brings it to the altar, pinches off its head, and burns
> it on the altar; its blood is pressed out against the wall of the
> altar. He removes its crop with its feathers and throws it beside
> the altar, on the east side, where the ashes go. He tears it open by
> its wings without splitting it apart, and the priest burns it on
> the altar, on the wood that is on the fire. It is a burnt offering,
> a fire offering, a pleasing aroma to the LORD."

"Pressed out" is וְנִמְצָה (ve-nimtzah, "and it is pressed out"). Now
the near miss — the FIRST bird's procedure, written right before the
pointer. Listen for how the blood is handled differently. Leviticus
5:8-9:

> "He brings them to the priest, who offers the sin-offering bird
> first: he pinches off its head at the back of the neck without
> separating it, and sprinkles some of the sin offering's blood on the
> wall of the altar; the rest of the blood is drained out at the base
> of the altar. It is a sin offering."

Both birds are pinched, and both touch the altar's wall — but the
first bird's blood is SPRINKLED, with the rest DRAINED at the base;
the second bird's blood is PRESSED OUT on the wall, and no base is
mentioned. The tradition reads that difference as a height: the sin
offering's blood below the altar's red line, the burnt offering's
above it. So "as prescribed" cannot mean "like the bird just
described" — that was the other bird — and the only prescription for
a bird burnt offering is chapter 1's.

**What the tradition says.** The Mishnah tests exactly this link: a
burnt-offering bird done by the sin offering's procedure fails
(Mishnah Zevachim 7:2):

> "A bird burnt offering done above the line, by the burnt offering's
> procedure and in the name of a burnt offering — valid… Done by the
> sin offering's procedure — invalid. Done below the line, by any
> procedure — invalid."

The second bird of chapter 5, run with the wrong procedure, fails
their test. "As prescribed" binds to chapter 1's rite, and they
graded it.

**Now the program's terms, in one paragraph.** Programmers call this
CALLING BY REFERENCE: state a procedure once, then point to it by
name. The pointer resolves the way a name is looked up in an index:
the verse gives the type name (a burnt offering, of a bird), and the
whole Bible contains exactly one definition of that procedure, so
the name plus the single definition settles it with no guessing. The
program for Leviticus 5 checks that the word "as prescribed" really
stands at 5:10 before it grades anything, then, when it reaches the
second bird, calls the function that holds chapter 1's rite — the
place, the count, and the burning all come back through the
reference, exactly as the single word intended.

**For the record.** The burnt-bird procedure's distinctive words —
"pressed out," "its crop," "with its feathers" — each stand at
exactly ONE place in the whole Bible, Leviticus 1:15-16. And the
pointer word itself, "as prescribed," stands 24 times in the Bible,
twelve of them in the Torah; the tradition's reading of this one
taught us the move, and the machine then asked every one of the 24
the same question — prescribed where?

---

## Example 3 — a number stored in another book: the seducer's fine

**The story, in plain words.** Exodus has a law about a man who
seduces an unmarried girl: he must marry her, and if her father
refuses the match, he must pay anyway — "money like the bride-price
of virgins." How much is that? Exodus never says. The number is in
Deuteronomy, in the neighboring law about a man who forces a girl:
fifty pieces of silver. The tradition's oldest commentary on Exodus
says exactly this in its own voice: "but we have not heard how much"
— and goes to Deuteronomy for the figure. The Exodus law names a
price tag that is kept in another book.

**What crosses the link, one line each.**
- Exodus states the duty and points at a price ("like the
  bride-price of virgins").
- Deuteronomy holds the price: fifty pieces of silver.
- The tradition supplies the step that connects them.

**The verses.** The duty first. Listen for the word "bride-price."
Exodus 22:15-16:

> "When a man seduces a virgin who is not betrothed and lies with
> her, he must pay the bride-price to make her his wife. If her
> father flatly refuses to give her to him, he weighs out money like
> the bride-price of virgins."

"Bride-price" is מֹהַר (mohar). Now the number, in the other book.
Listen for "fifty." Deuteronomy 22:28-29:

> "When a man finds a virgin girl who is not betrothed, and seizes
> her and lies with her, and they are found — the man who lay with
> her gives the girl's father fifty pieces of silver, and she becomes
> his wife, because he violated her; he may not divorce her all his
> days."

**What the tradition says.** The Mekhilta — the oldest running
commentary on Exodus — on the words "he weighs out money":

> "'Money he shall weigh' — but we have not heard how much. I reason:
> it says here 'money' and it says there 'money'; just as there it is
> fifty, so here it is fifty."

And the Mishnah lists what the seducer owes (Mishnah Ketubot 3:4):
"The seducer pays three things, the one who forces her pays four.
The seducer pays for the shame, the injury, and the fine; the one
who forces her adds the pain."

**Now the program's terms, in one paragraph.** This is a FETCH: the
program for Exodus 22 holds only the pointer, and when it reaches
the fine it fetches the number from the Deuteronomy verse. Because
the step from "money" here to "money" there is a teacher's analogy,
not something the text says outright, the link is labeled a transfer
and the Mekhilta is named as its teacher.

**For the record.** "Like the bride-price of virgins" is the only
place in the Bible where a fine is set by pointing at another fine.
The tradition's own name for this move — a stated case whose number
lives elsewhere — is what our records call a pointer-fetch.

---

## Example 4 — a law that depends on counting: the kid in its mother's milk

**The story, in plain words.** One short sentence — "you shall not
boil a kid in its mother's milk" — appears three times in the Torah,
word for word: twice in Exodus, once in Deuteronomy. On its face it
forbids one thing: cooking. But the tradition reads the number of
times as the law: three appearances, three prohibitions — cooking
the two together, eating the mixture, and benefiting from it in any
way. Here the link is not to a particular verse. It is to a COUNT:
how many times the sentence stands in the whole text.

**What crosses the link, one line each.**
- The sentence itself, identical at each seat.
- The number of seats: three.
- The reading that turns three seats into three laws — or, on
  another teacher's reading, three exclusions.

**The verses.** Listen for the same closing sentence each time.
Exodus 23:19:

> "The first of the first fruits of your land you shall bring to the
> house of the LORD your God. You shall not boil a kid in its
> mother's milk."

Exodus 34:26 — the same words:

> "The first of the first fruits of your land you shall bring to the
> house of the LORD your God. You shall not boil a kid in its
> mother's milk."

Deuteronomy 14:21:

> "You shall not eat any animal that died of itself; you may give it
> to the stranger in your gates to eat, or sell it to a foreigner —
> for you are a holy people to the LORD your God. You shall not boil
> a kid in its mother's milk."

**What the tradition says.** The Talmud (Chullin 115b):

> "The school of Rabbi Yishmael taught: 'You shall not boil a kid in
> its mother's milk' — three times: one for the prohibition of
> eating, one for the prohibition of benefit, and one for the
> prohibition of cooking."

And the Mishnah shows a second teacher reading the same count a
different way (Mishnah Chullin 8:4): "Rabbi Akiva says: wild animals
and birds are not included by the Torah, as it says 'you shall not
boil a kid in its mother's milk' three times — to exclude wild
animals, birds, and unclean animals." The count is the fact both
teachers start from; what it means is the argument.

**Now the program's terms, in one paragraph.** This is a CENSUS
link. The program does not follow a pointer; it counts. Its word
database finds every seat of the sentence, confirms there are
exactly three, and the law's code carries that count as its input.
The machine can count; only a teacher can say what a count means,
and the program carries both teachers' readings with their names.

**For the record.** The sentence stands at exactly three places in
the whole Bible, and nowhere else. A fourth would break both
readings.

---

## Example 5 — a headline handed to the code beneath it: "you shall not steal"

**The story, in plain words.** The Ten Commandments say "you shall
not steal" in two words. Everyone knows the line; almost nobody
notices that it sits between "you shall not murder," "you shall not
commit adultery," and "you shall not bear false witness" — all crimes
against a person, and in the tradition's law all capital crimes. So
the tradition reads the two words from their neighbors: this "steal"
means stealing a PERSON — kidnapping — which is a capital crime. The
everyday theft of money or goods is a different law with a different
penalty, and it lives elsewhere: in the ordinances of Exodus 21-22
(the thief pays back double, or four- and fivefold), and in
Leviticus 19. The headline points at a case; the code for that case
is kept in another chapter.

**What crosses the link, one line each.**
- The Ten Commandments state the headline.
- Its neighbors settle which crime the headline means.
- The ordinances hold the code for the other crime, money theft,
  and the case is handed to them.

**The verses.** The headline. Listen for how short it is. Exodus
20:15 (in the Hebrew verse division, 20:13):

> "You shall not steal."

Now the money law it does NOT mean. Leviticus 19:11:

> "You shall not steal, and you shall not deal falsely, and you shall
> not lie to one another."

And the code that prices money theft, Exodus 21:37:

> "When a man steals an ox or a sheep and slaughters it or sells it,
> he pays five cattle for the ox and four sheep for the sheep."

**What the tradition says** (Babylonian Talmud Sanhedrin 86a):

> "The rabbis taught: 'You shall not steal' — the text speaks of one
> who steals persons. You say persons; or is it only one who steals
> money? Go and learn from the thirteen rules by which the Torah is
> expounded: a matter is learned from its context. What does the
> text speak of? Of persons. So here too: persons."

**Now the program's terms, in one paragraph.** This is a ROUTE. The
program for the Ten Commandments does not contain the law of money
theft; when a case of theft of goods arrives, it hands the case to
the program for the ordinances, where that law's code lives, and
keeps for itself only the kidnapping case. Routing is how one part
of a program says: this is not mine, it belongs over there.

**For the record.** The reading by neighbors — "a matter learned
from its context" — is one of the thirteen rules the tradition
lists for reading law from the text, and this verse is the rule's
textbook case.

---

## Example 6 — a story used to test a law: the sons of Eli

**The story, in plain words.** Leviticus lays down the order of a
peace offering: first the fat is burned on the altar, and only then
does the priest take his share, the breast and the thigh. Centuries
later, the book of Samuel tells of two priests, the sons of Eli, who
sent their servant to grab meat from the pot before the fat was
burned — and, if the worshipper objected, to take it by force. The
story is not a law. It is a record of the law being broken, and the
program uses it exactly that way: as a test. Run the law on the
story, and the law must find the breach the text describes.

**What crosses the link, one line each.**
- Leviticus states the order: fat first, then the priest's share.
- Samuel narrates a priest taking his share before the fat.
- The program runs the narrated act against the law's gate.

**The verses.** The law first. Listen for the order of the two
verbs. Leviticus 7:31:

> "The priest burns the fat on the altar; and the breast belongs to
> Aaron and his sons."

And Leviticus 3:16: "The priest burns them on the altar, food of a
fire offering for a pleasing aroma; all fat is the LORD's." Now the
story. Listen for "before." 1 Samuel 2:15-17:

> "Also, before the fat was burned, the priest's servant would come
> and say to the man offering the sacrifice: give meat for roasting
> to the priest — he will not take boiled meat from you, only raw.
> And the man would say to him: let them first burn the fat, as is
> done today, then take for yourself whatever you like. And he would
> say: no, give it now; if not, I take it by force. And the sin of
> the young men was very great before the LORD, for the men treated
> the LORD's offering with contempt."

Notice that the worshipper in the story states the law correctly —
"let them first burn the fat" — and the priest's servant overrides
him. The text records the breach and the correct rule in the same
breath.

**Now the program's terms, in one paragraph.** This is a RUN LOG
link: a narrative used as a test tape. The program for Leviticus 7
has a gate — the priest's due opens only after the smoking. It reads
the demand from 1 Samuel 2 as an event and checks it against the
gate: the demand comes before the smoking, so no due exists yet, and
the ledger shows an open entry — the text's own "very great sin"
in the machine's terms.

**For the record.** The later books of the Bible are, for this
program, the record of the law running. Where they narrate a breach,
the program must reproduce the breach; where they narrate a
fulfillment (the seventy years, in THE_EFFECTS.md), it must
reproduce the fulfillment.

---

## Example 7 — a transfer with a teacher, and one the tradition refused

**The story, in plain words.** This example shows the rule from the
section below in action, twice. Leviticus 5 describes a guilt
offering and sets a minimum value on the ram: it must be worth
"silver shekels" — shekels plural, so at least two. Leviticus 19
describes another guilt offering, for a different sin, and calls its
animal "a ram of guilt" — with no value stated. May the minimum be
carried across from the one to the other, because both say "ram of
guilt"? A teacher in the tradition says yes, in so many words. That
is a permitted transfer: received, not invented. Then the second
case: Tamar in Genesis is told to "stay a widow"; the high priest in
Leviticus may not marry "a widow." May the meaning of "widow" be
carried from Tamar's story to the priest's law? The Talmud raises
exactly that link — and refuses it. The program carries the refusal
too.

**The accepted transfer.** Leviticus 5:15:

> "When a person commits a trespass and sins unintentionally against
> the LORD's holy things, he brings his guilt offering to the LORD: a
> ram without blemish from the flock, valued in silver shekels by the
> sanctuary shekel, as a guilt offering."

Leviticus 19:21:

> "He brings his guilt offering to the LORD, to the entrance of the
> tent of meeting: a ram of guilt."

The Sifra — the oldest running commentary on Leviticus — on that
verse (Sifra Kedoshim, chapter 5, row 6):

> "'He brings his guilt offering to the LORD, to the entrance of the
> tent of meeting, a ram of guilt' — it says here 'a ram of guilt'
> and it says there 'a ram of guilt'; just as the ram said there is
> in silver shekels, so here it is in silver shekels."

**The refused transfer.** Genesis 38:11:

> "Judah said to Tamar his daughter-in-law: stay a widow in your
> father's house until my son Shelah grows up — for he said, lest he
> too die like his brothers. And Tamar went and stayed in her
> father's house."

Leviticus 21:14, the high priest's marriage law:

> "A widow, a divorced woman, a profaned woman, a harlot — these he
> shall not take; only a virgin of his people shall he take as a
> wife."

The Talmud (Yevamot 59a):

> "The rabbis taught: 'a widow he shall not take' — whether a widow
> from betrothal or a widow from marriage. Is that not obvious? — You
> might have thought to learn 'widow' from 'widow' from Tamar: just
> as there she was a widow from marriage, so here only from marriage.
> It teaches us otherwise."

The link was considered on this very word — and declined.

**Now the program's terms, in one paragraph.** Both edges are in the
program's records with the label TRANSFER and a teacher's name. The
first carries a value across (the two-shekel floor) with the Sifra
as its teacher. The second carries a refusal: the program for
Tamar's story calls the program for the priests' law, and the record
says in its own words that the "widow-widow" analogy was "considered
and refused" — so the priest's law is applied on its own terms, not
Tamar's. A transfer's teacher can teach no.

**For the record — what a wrong link looks like.** The review of
every link in the program found one transfer made without a
teacher. Genesis 38:8 — "Judah said to Onan: go in to your brother's
wife and perform the duty of a brother-in-law to her, and raise up
seed for your brother" — is the first appearance of the levirate
law, the duty to marry a dead brother's childless widow. The program
had wired that verse to Leviticus 18:18 — "You shall not take a
woman together with her sister, to be a rival to her, uncovering her
nakedness beside her in her lifetime" — on the strength of the
topic alone: both are about marriage within a family. No teacher
makes that link. The review cut it, gave each verse its own place,
and re-wired the levirate through the passages that do teach it (the
Talmud's discussion of the rival wife at Yevamot 3b and 8b, and the
commentary's line "Judah began the levirate commandment first,"
Bereshit Rabbah 85:5). One wrong link, found by the rule, fixed by
the rule.

---

## Example 8 — a link we believe but cannot source: Tamar's pledge

**The story, in plain words.** In Genesis, Tamar asks Judah for a
pledge — his seal, his cord, and his staff — to hold until he sends
the payment he promised. In Exodus, there is a law about pledges: if
you take your neighbor's garment as security for a loan, you must
give it back by sunset. The two look like the same institution: a
thing held as security until a debt is paid. But the Hebrew uses two
different words — עֵרָבוֹן (eravon) in Genesis, חָבֹל (chavol) in
Exodus — and no teacher in the tradition joins the two passages. So
the program records the link as a HYPOTHESIS: kept in view, labeled,
and never counted as proven. This is what honesty looks like in the
records.

**The verses.** Genesis 38:17-18:

> "He said: I will send a kid from the flock. She said: if you give a
> pledge until you send it. He said: what pledge shall I give you?
> She said: your seal, your cord, and the staff in your hand. He gave
> them to her and went in to her, and she conceived by him."

Exodus 22:25:

> "If you take your neighbor's garment in pledge, you must return it
> to him by sunset."

**Now the program's terms, in one paragraph.** The program for
Tamar's story calls the program for the ordinances when it reaches
the pledge, because the institution looks the same. The review
searched the tradition for a teacher who makes that connection and
found none. The link therefore carries the label HYPOTHESIS, the
cell that depends on it is marked the same way, and every report
that counts the program's proven results lists it separately —
"hypotheses: 1" — rather than folding it into the total. Six links
in the whole program carry this label today.

**For the record.** A hypothesis is not an error; it is a claim
waiting for a teacher. If a passage in the tradition is found that
joins the two words, the label changes to transfer and the teacher's
name is written beside it. If none is ever found, it stays a
hypothesis forever, visibly.

---

## Example 9 — a call that brings back a count: the decree reads the census

**The story, in plain words.** The book of Numbers opens with a
census: six hundred and three thousand five hundred and fifty men of
twenty and upward. Thirteen chapters later the people refuse the land
and the decree falls: everyone counted in that census will die in the
wilderness. The decree does not restate the number. It says "all your
counted ones, by all your number, from twenty years old and upward" —
the census's own formula, word for word — and by that formula it
names the set. The program for the decree does not carry the number
either. It calls the program for the census and gets the set back:
the same 603,550 the census read off its verses. Later in the book
the pattern repeats with a table instead of a sum: the grant to Gad,
Reuben and half of Manasseh is valued at the count of those tribes,
read off the population table the second census wrote — 110,580 —
and nowhere typed.

**What crosses the link, one line each.**
- The census program reads twelve tribal counts off the verses and
  sums them.
- The decree's program calls it and receives the set the decree
  falls on.
- The grant's program reads three of the second census's rows and
  receives the count the grant is valued at.

**The verses.** The census's total. Numbers 1:46:

> "And all the counted ones were six hundred thousand and three
> thousand and five hundred and fifty."

The decree, using the census's own words. Listen for "counted" and
"number." Numbers 14:29:

> "In this wilderness your carcasses shall fall — all your counted
> ones, by all your number, from twenty years old and upward, who have
> murmured against Me."

And the grant, valued by the second census. Numbers 32:33:

> "And Moses gave to them — to the sons of Gad and to the sons of
> Reuben and to the half tribe of Manasseh son of Joseph — the kingdom
> of Sihon king of the Amorite and the kingdom of Og king of Bashan:
> the land with its cities in their borders, the cities of the land
> round about."

**What the tradition says.** The Talmud asks the census's own
arithmetic on the shelf (Babylonian Talmud Bekhorot 5a): the Levite
houses add to 22,300 and the verse writes 22,000 — where did the
three hundred go? Its answer, that they were firstborn Levites who
could redeem no one, is the census program's own row; the decree
program never needs it, because the decree's set is the men of
twenty, and the Levites were never in it.

**Now the program's terms, in one paragraph.** This is a CALL that
carries a VALUE rather than a verdict. The decree's program holds no
number; when it reaches "all your counted ones" it calls the census
program's function and the set comes back computed. The check on the
tape prints it: the census set equals 603,550 by call. The grant's
program reads the population table — the rows the second census's
rule wrote, tribe by tribe — and the count of the two and a half
tribes comes to 110,580 from three rows, matched against the
program's own arithmetic. A number the text states once is read
once, by one program, and every other program that needs it asks.

**For the record.** The receipt formula "as the LORD commanded
Moses" is a pointer class of its own in the records — a RUN
CITATION, the doing citing its order — and the fourth book carries
sixteen of them, from the census at 1:19 to the daughters' marriage
at 36:10. Each names the command it closes; none carries a rule
across.

---

## Example 10 — a transfer with its teacher, in the fourth book: the vessels of Midian

**The story, in plain words.** After the war with Midian, the spoil
must be purified before it comes into the camp: garments, vessels of
skin, work of goats' hair, vessels of wood. Leviticus 11 has a list
almost the same — vessel of wood, garment, skin, sack — for a
different impurity, a dead creeping thing. The two lists share three
of their four words. May the rule of the one be carried to the other:
which objects take impurity, and by what grade? The Talmud says yes,
in so many words, on exactly these words — "garment and skin" here,
"garment and skin" there — and runs the analogy both ways. That is a
transfer with a teacher, and the program carries it as one: the
machine found the three shared words on its database; the tradition
licensed the carrying; the grade of the impurity comes back by call
from the Leviticus program.

**What crosses the link, one line each.**
- Numbers lists the materials to be purified after the war.
- Leviticus lists the materials a creeping thing's carcass defiles,
  with the grade: unclean until the evening.
- The Talmud's verbal analogy carries the definition of the
  materials across, in both directions; the program carries the
  grade by call, and names the teacher.

**The verses.** The spoil. Listen for the four materials. Numbers
31:20:

> "And every garment, and every vessel of skin, and every work of
> goats' hair, and every vessel of wood — you shall purify."

And the metals, two verses on. Numbers 31:22-23:

> "Only the gold and the silver, the copper, the iron, the tin and
> the lead — everything that goes through fire you shall pass through
> fire and it shall be clean, only it shall be purified with the water
> of sprinkling; and everything that does not go through fire you
> shall pass through water."

Now the other list, three books back. Listen for the same four
materials and the grade at the end. Leviticus 11:32:

> "And everything on which any of them falls when they are dead shall
> be unclean — any vessel of wood, or garment, or skin, or sack, any
> vessel with which work is done; it shall be put into water, and it
> shall be unclean until the evening, and be clean."

The shared words are בֶּגֶד (beged, "garment") and עוֹר (or, "skin").

**What the tradition says.** The Talmud (Shabbat 64a), the shelf's
own English:

> "The term garment and leather is stated with regard to ritual
> impurity imparted by a creeping animal: 'And whatever any of them
> falls upon when they are dead will be impure whether it be any
> vessel of wood, or a garment, or leather, or sack, whatever vessel
> it be with which any work is done it must be put into water and it
> will be impure until evening, then it will be clean' (Leviticus
> 11:32). And garment and leather is stated with regard to ritual
> impurity imparted by a corpse. Just as garment and leather stated
> with regard to a creeping animal only rendered impure objects that
> are spun and woven, so too, garment and leather stated with regard
> to a corpse only rendered impure objects that are spun and woven."

> "Utilizing the same verbal analogy, one could say: And just as
> garment and leather stated with regard to a corpse rendered impure
> any object that is the work of goats' hair, so too, garment and
> leather stated with regard to a creeping animal rendered impure any
> object that is the work of goats' hair."

The Sifrei on Numbers (157) says why the word "garment" is written in
the Numbers verse at all — it is "extra," there to make the analogy —
and the Talmud elsewhere (Bava Kamma 25b) uses the same pair to bring
a mat under the corpse's impurity.

**Now the program's terms, in one paragraph.** The program for the
war with Midian compares the two lists on the word database and finds
the three shared words; that is finding, and the machine may do it.
It then calls the Leviticus 11 program for the grade — unclean until
the evening — and that is the transfer, which the machine may not
make on its own. So the edge is labeled TRANSFER, its teacher named
in the record: Shabbat 64a's verbal analogy, run both ways, with the
Sifrei's line that the word was written to be spare. It is the
fourth book's one transfer among 178 edges; every other edge the
book's programs make is a reference — the text naming an
institution — or a homograph refused (the next example).

**For the record — a chain of transfers, every link taught.** The
same chapter's measure, two thousand cubits around a Levite city, is
where the tradition finds the distance one may walk on the Sabbath.
The Talmud (Eruvin 51a) reaches it by a chain of eight verbal
analogies, each on a shared word: "place" in the Sabbath verse ("let
no man go out of his place," Exodus 16:29) to "place" in the
manslayer's law ("I will appoint you a place to which he shall flee,"
Exodus 21:13); "flee" there to "flee" at Numbers 35:26; "border" in
that verse to "border" at 35:27; "outside" there to "outside" at
35:5, "you shall measure from outside the city two thousand by the
cubit." And the page refuses a shorter chain to the thousand cubits
of 35:4: "outside" is learned from "outside," not from "outward." The
program carries the two thousand as this chapter's measure, and the
chain as its teacher.

---

## Example 11 — a link the machine proposed and the reading refused: the king who is not Molech

**The story, in plain words.** The machine finds links by counting
words, and it counts blind. Hebrew is written in consonants; the
vowel points beneath them are a second layer, and two different words
can share every consonant. So when the machine scanned the fourth
book for the words that name the institutions its programs hold, it
matched the "king" of Moab to the idol Molech — same three letters —
and demanded an edge from Balak's story to the law that forbids
passing children to Molech. The reading looked, and refused: the
points differ, the words differ, no law crosses. The refusal is
written down with the same care as an accepted link, so that nobody
mistakes the spelling for the link.

**What crosses the link, one line each.**
- Nothing. That is the finding.
- The machine's demand is kept in the record, labeled a homograph,
  with the vowel points that decide it.
- Twenty-six such refusals stand in the fourth book's records.

**The verses.** The king. Numbers 22:4:

> "And Moab said to the elders of Midian: now this crowd will lick up
> all around us, as the ox licks up the grass of the field. And Balak
> son of Zippor was king of Moab at that time."

The idol. Leviticus 18:21:

> "And of your seed you shall not give to pass over to Molech, and
> you shall not profane the name of your God: I am the LORD."

The king is מֶלֶךְ (melekh, "king"); the idol is מֹלֶךְ (Molekh, the
idol's name). The
consonants are the same three letters; the first vowel differs, and
the machine's word database carries the vowel and the dictionary
entry, so the refusal is measured, not argued.

**The same refusal at other words.** "Instead of every firstborn"
(Numbers 3:12) shares its word with "eye in exchange for eye"
(Example 1): the same preposition, the substitution and not the
retribution — the machine matched it at a dozen seats across six
chapters, and the reading refused every one. "The heads of the
fathers" (Numbers 31:26, 32:28) shares its consonants with "the
mediums" of Leviticus 19:31 — a vowel apart. "The commandments"
(Numbers 15:22) shares its consonants with "the unleavened bread." A
yoke that never "came up" on the red heifer (19:2) shares its
consonants with "burnt offering." The prince Shelumiel and the family
name Shillem share theirs with "peace offerings." In every case the
points, or the dictionary, or the sense, told the two words apart,
and the record says which.

**Now the program's terms, in one paragraph.** The census that
demands edges works on consonants and is deliberately over-eager: it
would rather demand a link that is not there than miss one that is.
Each demand is answered at the reading, and an answer of no is a
disposition of its own — FALSE — with the label NONE, meaning no rule
crosses. The gate that checks the records refuses to run the program
until every demand has an answer, so a homograph cannot be left
silently unanswered, and it cannot be silently accepted either.
Twenty-six of the fourth book's 178 demanded edges were answered no.

**For the record.** The vowel points that decide these are not our
reading; they are the received text's second layer, carried in the
same database as the letters. Where two words differ only in a
point, the machine reads the point.

---

## Example 12 — a link through another program, and a link that carries a place

**The story, in plain words.** Not every link goes straight from the
verse to the definition. Sometimes the text names an institution
whose home is a program this program already reaches through
another. The land is to be divided "as an inheritance" — Numbers says
so at the second census, at Gad and Reuben's grant, at the
itinerary's close, at the borders, at the Levite cities. The
inheritance law lives in the family program compiled from Genesis;
but the LAND's inheritance, by lot and by the number of names, is a
cell of the second census's program, which itself calls the family
program. So the borders' program reaches the family law VIA the
census, and the machine checks that the path is live. And sometimes
the text does not point at a procedure at all, but at a thing — a
place, a date, a quantity. "Let this land be given to your servants
for a holding," say Gad and Reuben, using the jubilee's own word for
tenure. That word does not call the jubilee's procedure; it names
the land east of the Jordan as the holding the grant conveys, and
whether the jubilee's release reaches that land is a question filed
for the book of Joshua.

**What crosses the link, one line each.**
- "Inheritance," at five chapters, reaches the family law through
  the second census's cell for the land — a reference, via another
  program.
- "For a holding," at four verses, carries a PLACE, not a procedure —
  a reference that carries a datum.

**The verses.** The lot. Numbers 26:53:

> "To these the land shall be divided as an inheritance, by the
> number of names."

The borders, naming the same institution. Numbers 34:2:

> "Command the children of Israel and say to them: when you come into
> the land of Canaan, this is the land that shall fall to you as an
> inheritance, the land of Canaan by its borders."

And the holding. Numbers 32:5:

> "And they said: if we have found favor in your eyes, let this land
> be given to your servants for a holding; do not bring us across the
> Jordan."

"For a holding" is לַאֲחֻזָּה (la-achuzzah, "for a holding"), the word of Leviticus
25:10 — "each of you returns to his holding" — the jubilee's tenure
word.

**Now the program's terms, in one paragraph.** VIA is a disposition
in the records: the edge is a reference, the text names the
institution, and the definition is reached through a program this one
already calls — the machine verifies the intermediate call is live,
so the path cannot go stale unnoticed. Fifteen of the fourth book's
edges run this way, most of them the land's inheritance through the
second census. PARAMETER is another: the text points at a quantity
or a datum, not a procedure — a date ("in its appointed time," at
the second Passover), a place (the holding east of the Jordan) — and
the edge carries that datum with its label. Three of the fourth
book's edges are parameters. Neither kind carries a law across, and
neither needs a teacher; both are the text naming its own things.

**For the record.** The word "holding" stands at exactly three
places in the refuge cities' chapter — the Levites' cities are taken
"from the holding of the children of Israel," and the manslayer
returns "to the land of his holding" — and the same word carries the
same label there: a place, filed with the jubilee's reach.

---

## Example 13 — a call the text demands that is not yet made, and a link whose far end is a later book

**The story, in plain words.** Among Eleazar's charges, the census
chapter lists "the continual meal offering." The meal offering has a
program; the continual one — the priest's daily tenth, Leviticus 6 —
is that program's own object. So the text names an institution, the
program exists, and the call is owed. It is not yet made, and the
record says so: the disposition is OWED, and it names the line in the
debt ledger where the call waits. The gate that checks the records
will not let the program run with an owed edge that has no such
line. And some links reach past every book compiled so far. The
cities for the Levites, the six cities of refuge, the daughters'
holding, Caleb's Hebron: the fourth book orders them, and the book of
Joshua does them. Those edges cannot be dispositioned at all until
Joshua is read; the debts they close stand open on the ledger with
the closing verse named (Story 9 of THE_EFFECTS.md), and the seats
are filed for the readback.

**What crosses the link, one line each.**
- Numbers names an institution defined in Leviticus; the program for
  Leviticus exists; the call waits, and the debt is named.
- Numbers orders a doing that Joshua narrates; the edge waits on the
  reading of Joshua, and the debt is named on the ledger.

**The verses.** The charge. Listen for "continual." Numbers 4:16:

> "And the charge of Eleazar son of Aaron the priest: the oil for the
> light, and the incense of spices, and the continual meal offering,
> and the anointing oil — the charge of all the tabernacle and all
> that is in it, in the sanctuary and in its vessels."

The trumpets over the offerings, another owed call. Numbers 10:10:

> "And on the day of your gladness, and at your appointed times, and
> at the heads of your months, you shall blow the trumpets over your
> burnt offerings and over the sacrifices of your peace offerings; and
> they shall be for you a remembrance before your God: I am the LORD
> your God."

And an order whose doing is a book away, with its receipt there.
Numbers 35:2 and Joshua 21:3:

> "Command the children of Israel that they give to the Levites, from
> the inheritance of their possession, cities to dwell in; and
> pasture-land for the cities around them you shall give to the
> Levites."

> "And the children of Israel gave to the Levites from their
> inheritance, at the mouth of the LORD, these cities and their
> pasture-lands."

**Now the program's terms, in one paragraph.** OWED is the honest
disposition for a link the text demands and the program has not yet
wired: the reference is real, the callee exists, and the call is a
debt with a named line. Five of the fourth book's edges stand owed
today — the continual meal offering, the Levites' bulls and their
meal offering, the trumpets over the offerings, and the figured
stones of the itinerary's close, whose ban in Leviticus 26:1 has no
compiled cell yet. The gate counts them and refuses a sweep whose
owed edge names no debt. The links into Joshua and Deuteronomy are
of a different kind: their far end is not compiled because the book
is not read, so they live on the ledger as open entries and in the
records as forward seats — Deuteronomy 4:41-43 and 19:1-13 for the
refuge law's twin, 21:1-9 for the heifer, 17:6 and 19:15 for the
witnesses, Joshua 20 and 21 for the cities — to be answered at the
reading, never before it.

**For the record.** A link is never invented to close a debt early.
The record would rather show an owed edge for a week than a call
made before the sitting that reads its verses.

---

## How the links are found — and a rule the tradition insists on

Three different witnesses find the links, and they have different
strengths.

**The verses themselves declare some links.** The text has its own
link syntax: pointer words like "as prescribed," a phrase repeated in
two books, a formula that names a number stored elsewhere. A program
scans the bare text for these forms and lists which links MUST exist
— no tradition consulted.

**The Talmud records links with the argument attached.** Its
signature question is "from where do we know this?" and its answer
is a link: a shared word between two verses, or one verse standing
next to another. But the Talmud gives worked examples, not a
complete index. Its examples are CITED — it names its verses — and
its method is in plain view. What we take from an example is
narrower than it may sound: we learn what KIND of thing a link is
(a pointer word, a repeated phrase, a stored number) and then the
machine finds every place that kind of thing occurs in the
twenty-four books. Finding is all it does. Whether a found
repetition carries a law across — the step the tradition calls a
transfer — is never decided by the machine; that decision must come
from a teacher, as the rule below explains. The example supplies the
insight; the sweep supplies the coverage; the tradition supplies the
license.

**The machine counts, exhaustively and blind.** A database of every
word in the Bible lets a program find every place a rare phrase
stands, and demand an account of each. It is complete where the
Talmud is selective — but shallow where the Talmud is deep: it can
find that a phrase stands at exactly two places; it cannot say what
the link MEANS. That takes the recorded argument.

**The rule.** Here the tradition draws a line, and the program now
draws it too. There are two kinds of link. A REFERENCE is the text
pointing at itself — "as prescribed," a name that has one definition.
Anyone may follow a reference; the machine follows all of them. A
TRANSFER is different: carrying a LAW from one passage to another
because the two share a word — the way "eye for eye" in Exodus takes
its meaning of money from Leviticus. The tradition's rule, stated in
two places in the Talmud (Pesachim 66a, Niddah 19b), is that a
person may not make such a transfer on his own; he may only pass on
one he received from his teacher. The Jerusalem Talmud gives the
reason with a vivid example: if anyone could transfer laws on a
shared word, then because the phrase "garment of skin" appears in
two unrelated laws, a dead lizard could be made to defile a whole
house the way a corpse does — the method has no natural limit. So
after a review of every link in the program (finished 2026-09-07),
every link now carries a label: reference or transfer; and every
transfer names the teacher — the passage in the tradition that made
it. A transfer with no teacher is refused as a link and kept only as
a labeled HYPOTHESIS, never counted as proven. The review found one
transfer the program had made on its own (a law about marrying a
dead brother's widow, carried from Genesis to Leviticus on a topic
rather than a teacher) and undid it. Today the count is 455
references, 48 transfers with teachers, 9 hypotheses — and 143 edges
of a fourth kind, NONE: connections that carry no rule across them
at all (a program registering another's rules for a test, a word
that merely looks the same in two places, a number handed over as a
setting). Those are listed so that nothing is hidden, and labeled so
that nobody mistakes them for a law crossing.

The fourth book, read and compiled between 2026-09-09 and 2026-09-13,
added 178 edges and 45 pointers to that list: 151 references, one
transfer with its teacher (Example 10), 26 homographs refused
(Example 11), and no hypothesis. Beside the label, every edge now
carries a DISPOSITION saying how the link is wired: a live CALL (129
of the fourth book's), a path VIA another program (15), a PARAMETER
carried rather than a procedure (3), a call OWED with its debt named
(5), or FALSE (26). A gate reads the records before every run of the
program and refuses an edge without both.

---

## Where to go from here

THE_EFFECTS.md shows what happens when a linked law fires — the
change it writes. THE_CLOCK.md shows how "forever" in the servant law
reached into Leviticus 25 for its clock. THE_TOUR.md's section 9
walks the fourth book whole, and World/step9/NUMBERS_WALK.md is the
record of every link read there, sitting by sitting. The program's own list of
every link, with its label and its teacher, is in
World/step9/dependency_dispositions.yaml; the engineering map of the
same links is DEPENDENCIES.md in this folder.
