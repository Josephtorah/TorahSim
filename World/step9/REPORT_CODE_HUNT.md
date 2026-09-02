# THE CODE HUNT — tracking a Talmud function to its code in the Bible (2026-09-02)

The owner's order: "Look for code, not counts. Look at a function in
the Talmud and track it through the Bible and find the code. The
logic in the Talmud should help us understand how the code runs in
the Bible."

Executed this sitting. Every citation below was pulled from the
local corpus at the exact row named. The find: the code is there —
CONTROL FLOW, not counts — written in a two-keyword case syntax the
machine can detect, and the Talmud behaves precisely as the code's
engineering documentation: it names the structure, reverse-engineers
a hidden parameter from branch outputs, routes a new input type onto
an existing branch (dispute recorded), maintains a dictionary entry
for the conditional keyword, and reads a state-machine's transition
threshold out of a verse's own temporal tokens.

## THE SYNTAX: the code's two conditional keywords

The law sections of Exodus are written in a case structure built
from two words: כִּי ("when" — the case opener) and אִם ("if" — the
sub-branch), with אוֹ ("or") as the alternative marker. A machine
scan of Exodus 21–22 (every word, keyword tokens extracted) returns
the shape directly:

- Exodus 21:2 KI — the Hebrew slave case OPENS. 21:3 IM, IM (came
  alone / came married); 21:4 IM (master gave him a wife); 21:5 IM
  (the slave declares he loves his master — the branch with the ear
  ceremony and the serve-forever outcome). Then 21:7 KI — a NEW case
  opens (the daughter sold), with its own IM ladder at 21:8, 9, 10,
  11.
- Exodus 21:28 KI — the goring ox opens; 21:29 IM (the state flag —
  see the state machine below); 21:30 IM (ransom); 21:32 IM (the
  victim is a slave).
- Exodus 22:6 KI, 22:9 KI, 22:13 KI — three consecutive custody
  paragraphs (the bailees), each with its own IM branches inside
  (22:7–8; 22:10–12; 22:14).

Across the two chapters the pattern holds: KI verses are the section
heads (21:2, 7, 14, 18, 20, 22, 26, 28, 33, 35, 37; 22:4, 5, 6, 9,
13...), IM verses sit inside them. The nesting is real, mechanical,
and was recovered by a scan that knows nothing but the two tokens.

HONESTY NOTE — the keyword is overloaded, and the TRADITION
DOCUMENTS THE OVERLOAD: some KI hits in the scan are not case
openers (Exodus 21:21's closing כִּי כַסְפּוֹ הוּא — "FOR he is his
money" — is the "because" sense). And the Talmud maintains exactly
the dictionary entry needed to disambiguate: Reish Lakish,
Babylonian Talmud Gittin 90a — "the term ki has four distinct
meanings: if, perhaps, rather, because." A language-reference row
for the code's conditional keyword, held in the teaching layer. The
same layer holds the semantics table for the OTHER keyword: Rabbi
Yishmael, Mekhilta DeRabbi Yishmael (Tractate Bachodesh 11:11) —
"Every 'if' (אִם) in the Torah connotes optionality, EXCEPT FOR
THREE" — and lists the three mandatory ones. A corpus-wide keyword
census with its exceptions enumerated. This is what a language
manual is.

## SPECIMEN 1 — the four-guardians function (the main exhibit)

**THE CODE (Exodus 22:6–14).** Three consecutive KI paragraphs, each
a variant of one function — custody of another's property — with
the branches diverging on the same events:

- Paragraph 1 (KI, 22:6): a man gives his fellow money or vessels
  TO KEEP, and it is stolen. IM the thief is found → double payment.
  IM not found → the householder approaches the judges and swears
  he did not put his hand to his fellow's property → EXEMPT.
- Paragraph 2 (KI, 22:9): a man gives his fellow an animal TO KEEP;
  it dies, is injured, or is captured, no witness seeing. → The oath
  of the LORD between them → exempt. IM STOLEN from him → HE PAYS.
  IM torn by beasts → he brings the evidence → exempt.
- Paragraph 3 (KI, 22:13): a man BORROWS from his fellow; it is
  injured or dies → HE PAYS, even for the accident. IM its owner is
  with it → exempt. IM it was hired → "it came in its hire."

Same function, three configurations. Note what the code does NOT
say: the first two paragraphs never state what distinguishes them.
Both say "to keep." The differing input — whether the keeper is
PAID — is nowhere in the ink. The parameter is hidden.

**THE TEACHER, move by move (Babylonian Talmud Bava Metzia 94b).**

Move 1 — it NAMES THE STRUCTURE (94b:6): "The verses in the Torah
about bailees can be divided into THREE PASSAGES. The first
(Exodus 22:6–8) is stated about an unpaid bailee; the second
(22:9–12) about a paid bailee; the third (22:13–14) about a
borrower." The Talmud's division is EXACTLY the machine scan's
three KI blocks. The teacher and the scanner found the same
structure — the scanner mechanically, the teacher eighteen
centuries ago.

Move 2 — it RECOVERS THE HIDDEN PARAMETER FROM THE OUTPUTS
(94b:7–10). The gemara asks its own question: granted the third
paragraph says "borrows" explicitly — but where do the first two
get their labels, when neither says paid or unpaid? Answer: DIFF
THE BRANCHES. Feed both paragraphs the same input — theft — and
compare outputs: paragraph 1 exempts with an oath; paragraph 2
PAYS. So paragraph 2 carries the stricter liability, and liability
tracks benefit — therefore paragraph 2 is the keeper who is
compensated. The gemara even records the objection (paragraph 1
carries the double payment — isn't THAT the stringency?) and
answers it (double payment fires only on a false oath; paying
principal unconditionally is stricter), then seals the principle
with the borrower: "ALL BENEFIT is his" — so his is the severest
liability of all, paying even for accidents. This is
reverse-engineering: same input, different outputs, infer the
hidden configuration — objection and resolution preserved in the
log.

**THE ANSWER KEY (Mishnah Shevuot 8:1; Mishnah Bava Metzia 7:8).**
"There are FOUR types of bailees" — unpaid keeper, borrower, paid
keeper, and RENTER — with the full liability matrix: the unpaid
keeper takes an oath over every outcome and is exempt; the borrower
pays for every outcome, even beyond his control; the paid keeper
and the renter take an oath over the accidents (injured, captured,
dead) but PAY for loss and theft.

And here is the third teaching move: the code has THREE paragraphs;
the answer key has FOUR rows. The fourth role — the renter, who
pays for the USE of the item — appears nowhere in Exodus 22. Move
3 — ROUTE THE NEW INPUT TYPE ONTO AN EXISTING BRANCH: the Mishnah
files the renter under the paid keeper's rules, and the gemara
(Bava Metzia 93a) records that the four-fold division itself is
universal ("is there any Sage who does not accept the four
bailees?") while the routing of the renter — which branch's rules
he follows — is the recorded dispute between named authorities.
The code defines three variants; a case type the code never names
arrives; the teacher classifies it into the existing structure and
logs the disagreement about the classification. That is exactly
how a maintained system absorbs a new input class without a new
paragraph of code.

## SPECIMEN 2 — the goring ox: a state machine, threshold parsed from the ink

**THE CODE (Exodus 21:28–32, 35–36).** The ox carries a STATE
VARIABLE. Default state — the tradition's word is תָּם ("innocuous,"
literally "innocent"): the ox that gores pays half the damage, and
only out of its own body (21:35 — the live ox is sold and the
proceeds split). Elevated state — מוּעָד ("forewarned"): the owner
was warned and did not guard; now the payout is FULL, ox for ox
(21:36), and in the killing case the liability reaches the owner
himself (21:29). Two states, two output schedules.

**THE TEACHER reads the transition threshold out of the verse's own
temporal tokens.** The verse's state test (21:36): "or if it is
KNOWN that the ox was a goring ox מִתְּמֹל שִׁלְשֹׁם ('from yesterday
and the day before'), and its owner has not secured it." Babylonian
Talmud Bava Kamma 23b, two named readings of the same tokens:

- Abaye (23b:17): "yesterday" — one; "from yesterday" — two; "the
  day before" — three...
- Rava (23b:18): "from yesterday" — one day; "the day before" —
  two; "and its owner has not secured it" — NOW, the third goring,
  for which he is liable as forewarned.

Two recorded TOKENIZATIONS of one phrase, both arriving at the
threshold: THREE gorings flip the state. The constant is not
decreed from outside — it is parsed out of the code's own words,
and the parse dispute is preserved with the engineers' names.

**The full machine in the answer key (Mishnah Bava Kamma 2:4, with
the discussion at Bava Kamma 23b–24a):** "Which is innocuous and
which forewarned? Forewarned — where witnesses testified that it
gored on three different days. And it REVERTS to innocuous when it
refrains from goring for three days" (the accompanying tradition at
24a: children pet it and it does not gore). A forward transition, a
threshold, and a REVERSE transition — and the gemara then debates
the SEMANTICS of the counter (24a:9): are the three days about the
OX's nature, or about warning the OWNER? — a preserved argument
over what the state variable means, with practical differences
downstream. The teaching layer holds not just the machine but the
recorded debate about its meaning.

## WHAT THE HUNT PROVES

The owner asked for code, and the code is there — visibly,
mechanically, in the ink:

1. A CASE SYNTAX (KI opens, IM branches, O alternates) that a
   keyword scan recovers without any tradition loaded — and the
   scan's three custody blocks coincide exactly with the three
   passages the Talmud names.
2. HIDDEN PARAMETERS recovered the way an engineer recovers them —
   same input, diffed outputs — by the Talmud, on the record, with
   the objection preserved.
3. A STATE MACHINE with its transition threshold encoded in the
   verse's own temporal tokens, parsed by two named teachers in two
   recorded ways.
4. A LANGUAGE MANUAL in the teaching layer: the four senses of the
   when-keyword (Gittin 90a), the corpus-wide census of the
   if-keyword with its three mandatory exceptions (Mekhilta
   DeRabbi Yishmael, Bachodesh 11:11).
5. INPUT ROUTING: a case type the code never names (the renter)
   classified onto an existing branch, the universality of the
   four-fold table affirmed, the routing dispute logged.

This is the teacher hypothesis at code grain: the Bible's law
sections are structured programs; the Talmud's logic is HOW TO READ
THEM — structure identification, parameter inference, keyword
semantics, state analysis, input routing. None of it is our
imposition; every move above is the tradition's own, at a pulled
row.

## WHAT IT SETS UP

The cold-run experiment now has its natural target upgraded: the
four-guardians function is BETTER than the carrying function for
the first cold run, because its code is self-contained in nine
verses, its hidden parameter is recovered by an argument the
machine can replay (diff the theft branch), and its answer-key
matrix (Mishnah Shevuot 8:1) is already in our compiled modules
from the Mishpatim exam. A machine that parses the three KI blocks,
diffs the branches, and emits the four-row liability matrix would
be running the code the way the teacher teaches it to be run.

STATUS: investigation only; nothing ruled; no unit touched. The
keyword scanner ran read-only over the word database; all citations
pulled at the row this sitting.
