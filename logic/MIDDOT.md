# THE MIDDOT — the tradition's own inference rules

The middot (מִדּוֹת, "measures/rules") are the chain's OWN numbered
rulebook for deriving meaning from the text — the original catalog,
two millennia before ours. They are NOT the same layer as the TIR:
TIR maps grammar → logic inside one verse; the middot license
inferences FROM verses — cross-case, cross-passage. The sources we
read in Step 4 argue BY middot constantly; this file gives the
process its names for those arguments.

Three collections (Tannaitic tradition):
- the SEVEN of Hillel (H1–H7) — included in the thirteen;
- the THIRTEEN of Rabbi Ishmael (I1–I13) — for LAW (halakhah);
  Maimonides holds legal reasoning closed under these;
- the THIRTY-TWO of Rabbi Eliezer ben Yose ha-Gelili (E1–E32) —
  for NARRATIVE (aggadah).

Enumeration below follows Schumann, *Talmudic Logic*
(Data/reference_books/talmudic_logic.pdf), to be verified against the
Baraita texts themselves when they are read under Step 4. Model
layer — freely revisable, dated notes per change.

## The thirteen of Rabbi Ishmael (law)

- **I1 — qal wa-chomer** ("light and heavy", a-fortiori): transfer a
  ruling from the lesser case to the greater (or reverse). HARD
  CONSTRAINTS the tradition itself states: the **dayo cap** — the
  conclusion may never exceed the premise's severity; genus match
  required (the Mishnah's Sadducees exchange is the recorded failure
  case); not applied in penal law; never from received law to new law.
  → future operator QAL_WACHOMER with dayo assertion.
- **I2 — gezerah shavah** ("equal decree"): analogy licensed by the
  SAME WORDING in two passages — "the indefinite is explained by the
  definite." → mechanically a join over our word-level data.
- **I3 — binyan av** ("build a father"): generalize a rule from one
  verse (or two) to all cases sharing its essential feature.
- **I4 — kelal u-frat** (general then particular): the particular
  RESTRICTS the general to itself.
- **I5 — prat u-kelal** (particular then general): the general
  EXTENDS beyond the listed particulars.
- **I6 — kelal u-frat u-kelal**: general–particular–general → include
  only what resembles the particular.
- **I7 — kelal ha-tzarich li-frat** ("a general that needs the
  particular"): general and particular that each
  need the other to be understood.
- **I8** — a particular singled out from a general TEACHES about the
  whole general, not only itself.
- **I9** — singled out to discuss a similar provision: LIGHTENS, does
  not burden.
- **I10** — singled out for a dissimilar provision: lightens AND
  burdens.
- **I11** — singled out for a new provision: the original general no
  longer applies unless the text restores it.
- **I12 — davar ha-lamed me-inyano** : meaning decided from CONTEXT
  (and from the passage's end).
- **I13** — two verses that contradict stand until a THIRD verse
  decides between them. → our dispute/fork discipline has this shape.

Layer notes: I4–I7 (and the ribui/miut particles) OVERLAP the TIR's
particle territory (TIR-014/015). Policy: the TIR rule stands and
CITES the middah + chain sources as authority (the day-one amendment
pattern — Bereshit Rabbah 1:14 + Chagigah 12a on the et-inclusions).
I1–I3, I8–I13 are claim-layer inference licenses, not grammar.

## The thirty-two of Rabbi Eliezer (narrative)

For narrative (aggadic) derivation; several repeat the thirteen at
narrative strength. By cluster:
- **Particles**: E1 ribui (extension: et, gam, af, kol), E2 miut
  (restriction: akh, raq, min), E3 extension-after-extension (which
  restricts), E4 restriction-after-restriction (which extends).
- **A-fortiori & analogy**: E5 explicit qal wa-chomer, E6 implicit
  qal wa-chomer, E7 gezerah shavah, E8 binyan av.
- **Textual economy**: E9 abbreviation, E10 repeated expression
  (repetition signifies), E11 divided/reordered sequence.
- **Scope moves** (E12–E25): particular↔general teaching relations,
  mutual elucidation of passages, two verses contradicting until a
  third decides (E15 = I13's narrative twin), the rare-usage rule,
  statements said here but applying to a fellow passage, and more.
- **Literary devices**: E26 mashal (parable), E27 symmetry, E28
  from-the-preceding, E29 gematria (letter-values), E30 notarikon
  (words as acronyms), E31 earlier-that-is-later within a passage,
  E32 earlier-that-is-later between portions (the Torah is not
  strictly chronological — cf. our order-carries-no-claim finding,
  Mekhilta on Gen 1:1).

## The middot's own case law (consolidated 2026-09-04, from the
- **The two-verses-as-one limit** (Zevachim 57a:3-4, opened at the
  Lev 1-8 offering consolidation 2026-09-04): שני כתובין הבאין
  כאחד אין מלמדין ("two verses arriving as one do NOT teach
  onward") — a law stated twice in parallel (the around-token at
  both the burnt offering and the sin-offering) is BARRED from
  extending to a third case; the firstborn keeps ONE blood
  application because the extension route is closed. The rule has
  a recorded dissent arm (the school that lets two teach), and the
  sugya's closer: with the guilt-offering the tokens are THREE,
  and three certainly do not teach. A recorded LIMIT on analogy
  propagation — the inference engine's own overfitting guard.

## Exodus block campaign — owner's word "Do 3")

The campaign's exam rounds banked RULES-ABOUT-RULES on the corpus's
own seated verses: the tradition regulating its own inference
machinery, recorded where the machinery runs. Three rows, each
compiled into the exam engine and seated in a frozen unit:

- **ADJACENCY VALIDITY (round 25, the capital block — Yevamot 4a:4-5
  = Berakhot 21b:10, on Exod 22:17-18).** Is juxtaposition
  (semukhin, "adjacent verses") a licensed derivation channel? The
  witch was PLACED beside the beast-lier to teach: as he is stoned,
  so she — and Rav Yosef's meta-rule stands beside it: even one who
  rejects adjacency arguments GENERALLY expounds them in
  DEUTERONOMY. A channel-validity rule with a per-book parameter,
  stated as law. (Compiled: capital_rules.py
  juxtaposition_validity; seated at exo_22 / the capital round's
  claims.) Relation to the catalog: adjacency is the law-side use
  of E28's from-the-preceding family; the tradition itself disputes
  its license and records the settlement.

- **THE METHOD FORK (rounds 25, 26, 28 — three seats).** The two
  rival inference ENGINES — the general-and-particular school
  (kelal u-frat, I4–I7) and the amplify-and-limit school (ribui
  u-miut, the E1–E4 particles at law strength) — are both on the
  record processing THE SAME verse, yielding DIFFERENT tables, with
  the fork itself named in the text:
  (1) the witch-verse adjacency dispute (round 25);
  (2) the candelabrum's valid materials (Sukkah 50b:5-7 on Exod
  25:31): Rebbi runs general–detail–general → like the detail, all
  METALS; R. Yosei b. R. Yehuda runs amplified–limited–amplified →
  ALL materials except earthenware — two valid-materials tables
  from one verse, the fork named at 50b:5 (seated EX25-14);
  (3) the eleven spices (Keritot 6b:7-8 on Exod 30:34): Rav Huna
  counts the list from the verse's own plural tokens while the
  rival general-detail read derives what-rises-in-smoke-and-smells
  (seated EX30-11).
  Consequence for the machine: middah choice is a MODEL PARAMETER
  with recorded arms, never a silent default — where the fork is
  recorded, the engine returns both arms with authorities, exactly
  like any dispute.

- **PARSE DIRECTION (round 27, the vestments block — Zevachim
  24b:2-3 on Exod 29:12).** מקרא נדרש לפניו ("a verse is expounded
  on what PRECEDES it — not before-the-before, and not after"): a
  limiting clause binds the phrase it follows, not the whole
  sentence — "with your finger" binds the PLACING, the collection
  stays free. A parsing-direction meta-rule stated as law on the
  verse's own syntax — the precision layer of I12 (context), fixed
  to adjacency range. (Compiled: vestments_rules.py
  finger_placement; seated EX29-14.)

- **THE VOIDED FORM (Tazria sweep 2026-09-05 — Sifra, Tazria
  Parashat Yoledet, Section 1 5).** "Any inference that BEGINS to be
  stringent and ENDS to be lenient is NO inference" — an a-fortiori
  rejected on its FORM alone (R. Yehuda's stillbirth argument), the
  conclusion then re-derived from a written token instead. A
  validity precondition on I1 itself, stated as law.
- **DAYO ARGUED IN FULL (same sweep — Sifra, Tazria Parashat
  Yoledet, Chapter 2 4).** R. Eliezer holds the a-fortiori's
  limiting rule against every rephrasing of the hard-labor argument:
  "even if you answer me ALL DAY — enough for the derived to be like
  its source." The dayo cap exercised as a live defense, not a
  footnote — I1's ceiling at its own case.
- **THE INDUCTION LIMIT (same sweep — Sifra, Metzora, Section 1
  3).** Munbaz's regress before R. Akiva: granting the completion
  days seven makes them counting days, which grants seven more —
  "you would ADD FOREVER." An infinite-regress rebuttal recorded as
  the argument's formal stopper: an a-fortiori whose conclusion
  re-feeds its premise is void.
- **THE QUANTITY-READING TRIPLE (same sweep — Sifra, Metzora
  Parashat Zavim, Section 5 5-7).** Three rules for reading bare
  plurals, argued together at "days... many": R. Akiva's MINIMAL
  SEIZURE ("grasp the many — you did not grasp; grasp the few — you
  GRASPED"); R. Yehuda b. Beteira's BOUNDED MEASURE (measure the
  measure that ends, never the endless); R. Nechemya's OPEN-NOT-LOCK
  (the verse comes to open — "else say a hundred! a thousand! a
  myriad!"). The minimum-quantity parser's three independent
  derivations, one seat.
- **THE TWO-VERSES REFRAIN (same sweep — Sifra, Metzora, Chapter 4
  3, 6, 8-9; Section 4 1).** Four times in one chapter and again at
  the poverty scale: "until TWO verses say it, we have not heard" —
  a double-witness floor for exegesis itself: one token licenses
  nothing when a rival reading survives it; two convergent tokens
  close.

**THE OPEN TEACHES THE CLOSED (Sifra, Acharei Mot, Section 1 5;
2026-09-05).** R. Yishmael's school on the paired utterances of Lev
16:1-2 and the wine command: two utterances side by side, one OPEN
(naming its recipient chain) and one CLOSED — the open one teaches
the closed one's chain. A parse meta-rule about the text's own
TRANSMISSION HEADERS, joining the parse-direction and order
meta-rules in the rules-about-rules family.

**THE ORDER META-RULE (Sifra, Acharei Mot, Chapter 6 2;
2026-09-05).** "The WHOLE passage is said in order EXCEPT THIS
VERSE" — sequence and scroll-placement split explicitly at Lev
16:23, and the closing frame ("he did as the LORD commanded," 16:34)
re-asserts order for everything else. The tradition marking its own
program counter; compiled as the one relocation in
cold_run_yoma.py's service order.

**DAYO'S THIRD EXEMPLAR (Sifra, Acharei Mot, Chapter 12 9;
2026-09-05).** R. Meir's a-fortiori (bird-pinching should purify
the bird's torn-state as slaughter purifies the beast's) cut by R.
Yosei — "ENOUGH for it to be like the beast carcass": slaughter
yes, pinching no. The bounded-conclusion rule now three deep on the
walk (the hard-labor seat, the Munbaz table, this).

**THE INDUCTION LIMIT, DOUBLY ATTESTED (Sifra, Acharei Mot, Chapter
8 6 = Mishnah Yoma 1:1; 2026-09-05).** The conditional-wife regress
stopped by "if so, THE MATTER HAS NO END" — the same exchange
standing in the Sifra AND the Mishnah word for word: the
regress-stopper's second exemplar now carried by two independent
records of one argument.

**THE ANTI-INFERENCE FENCE, STATED COMPLETE (Sifra, Acharei Mot,
Chapter 13 14 + Sifra, Kedoshim, Chapter 11 10; 12; 2026-09-05).**
Three refusals on one subject: forbidden unions are NOT derivable
by reasoning (the general-and-particular closing the class at Lev
18:6), NO PUNISHING FROM INFERENCE, and NO WARNING FROM INFERENCE
(both stated on the both-parent sister clause) — the a-fortiori's
jurisdiction fence: it may find law but never found a penalty. The
inference engine's hardest governance row, now standing in full.

**THE JOINT-VS-SEVERAL DEFAULT (Sifra, Kedoshim, Chapter 10 5;
2026-09-05).** R. Yonatan: a conjoined pair ("his father and his
mother") means EITHER ONE ALONE unless the verse says יחדיו
("together") — a default rule for reading conjunctions, argued
against R. Yoshiyah's needs-a-verse position. A grammar-level
dispatch rule recorded as case law.

**THE REGISTER META-RULE, SECOND SEAT (Sifra, Kedoshim, Section 4
1 + Mishnah Bava Kamma 5:7; 2026-09-05).** R. Yosei: the Torah
spoke AS PEOPLE SPEAK, IN MANY TONGUES — "and ALL of them require
exposition"; the Mishnah's twin at the exam: "ox or donkey — the
Scripture spoke of the COMMON CASE." Human register and full
expoundability asserted together — the double verdict that guards
both against over-reading and against waiving the reading.

**THE FREED-TOKEN CLOSE ON THE THREE-SOURCE ARGUMENT (Sifra,
Kedoshim, Chapter 10 7; 2026-09-05).** The judge-prince-deaf
common-denominator argument run at full depth — each source
refuted alone, the pairs refuted, the triple closed by "in your
people" — and the final trim executed by REASSIGNMENT: "'judge' is
free — if not needed for itself, GIVE IT to the father." The
building-block engine and the freed-clause operator working as one
recorded machine.

**THE TWO-WAY TRANSFER (Sifra, Emor, Chapter 1 3 and 5; 2026-09-05).**
One verbal analogy — "baldness"-"baldness", "gash"-"gash" between
the priests (Lev 21:5) and Israel (Deut 14:1, Lev 19:28) — carries
per-spot and whole-head FROM the priests TO Israel and
for-the-dead-only FROM Israel BACK to the priests in the same
breath: the gezerah shavah (verbal analogy) as a BIDIRECTIONAL edge,
each side supplying the parameter the other lacks. Recorded twice
in five rows; claim LV21A-05.

**THE PROFANATION TRIPLE-IMPORT (Sifra, Emor, Section 4 2;
2026-09-05).** "Profanation"-"profanation" (Lev 22:2 to Lev 19:8)
imports THREE parameters at once — time-disqualification, death,
and acceptance-dependence — and R. Yehuda's rival analogy on "I the
LORD" imports KARET: one edge, three payloads, with a recorded
alternative edge carrying a fourth. The analogy's payload is not
one law but the whole parameter block of the source clause; claim
LV22A-01.

**THE STRICT-TO-LENIENT META-RULE (Sifra, Emor, Chapter 17 10;
2026-09-05).** R. Yehuda argues the sukkah must be built of the four
species (an a-fortiori from the lulav); the Sages refuse it by a
rule about reasoning itself: "any reasoning whose beginning is
STRICT and whose end is LENIENT is no reasoning" — for a man who
found no species would then sit in no sukkah at all. An inference
is rejected not on its premises but on the SIGN of its consequence:
a stringency that would produce a leniency is invalid as a form.
The fence's cousin (no punishing from inference) generalized to
direction; claim LV23B-11.

**THE THREE-CONSTRAINT PIN (Sifra, Emor, Chapter 18 3;
2026-09-05).** The showbread's arrangement: "two rows" alone admits
eight-and-four; "six the row" alone admits six-six-six; "twelve"
alone admits four-four-four — "until THREE verses say it, we have
not heard": the reading is pinned only when three independent
constraints stand together, each closing a solution the others
leave open. A recorded statement of how many tokens a determination
needs — the tradition counting its own degrees of freedom; claim
LV24A-03.

**THE UNWRITTEN WARNING FROM A REDUNDANT PUNISHMENT (Sifra, Emor,
Chapter 14 9; 2026-09-05).** Yom Kippur's work carries a written
warning and a written punishment; its affliction carries a written
punishment and NO warning. The punishment for work is REDUNDANT
(derivable a fortiori from affliction's), so it is written to teach:
as work's punishment follows a warning, so affliction's punishment
follows one — the warning for the fast EXISTS though unwritten. The
rule "no punishment without a warning" run backward as a derivation
engine: a redundant punishment is the evidence of a missing warning;
claim LV23B-05.

**THE DEMONSTRATIVE FENCE (Sifra, Emor, Chapter 2 5; Chapter 7 2-3;
Chapter 11 2; Section 12 2; 2026-09-05).** Four refusals of inference
by a demonstrative token in one parashah: "THESE he shall not take"
— the niddah's seed is not profaned though the a-fortiori from karet
says it should be; "THESE you shall not offer" — the animal worked
with is offered though the heifer a-fortiori says not; "THIS day"
needs matzah and Sukkot does not; "THIS festival" needs a sukkah and
Passover does not. The anti-inference fence (Acharei Mot) has a
lexical form — זה/אלה ("this/these") closes the class against
extension; claims LV21A-13, LV22B-03, LV23A-04, LV23B-06.

**THE TWO-VERSE PIN (Behar-Bechukotai, 2026-09-05).** "Until both
verses are said we would not know" — the Sifra's own formula for a
rule that NEITHER verse yields alone: "seven sabbaths of years" and
"seven years seven times" together fix the count (Sifra, Behar,
Section 2 1); "to the buyer" and "to his generations" together fix
the perpetuity's holder (Section 4 9). A middah of joint sufficiency:
each verse a necessary premise, the rule the conjunction; claims
LV25A-08, LV25B-08.

**THE WENT-OUT-TO-TEACH CLASS RULE (Behar).** "Sowing and pruning
were inside the class and went out — to teach the class: labor in
the land and in the tree" (Sifra, Behar, Section 1 6): R. Ishmael's
eighth rule run as a classifier — the named members define the
predicate that admits or excludes the unnamed (loosening under
olives out; plowing in); claim LV25A-04.

**THE HEART-CLAUSE META-RULE (Behar, two seats).** "Of everything
given to the heart it says 'you shall fear your God'" (Sifra, Behar,
Chapter 4 2 on verbal wronging; Section 6 2 on needless commands as
rigor): the fear clause marks the cases whose deciding fact is an
intent no court can observe — a rule about which rules the court can
run; claims LV25A-16, LV25C-05.

**THE A-FORTIORI REFUSED BOTH WAYS BY TWO TEXTS (Behar).** The
seventh releases money, the Jubilee frees slaves; each inference to
the other's object is blocked by its own verse — "in THIS Jubilee
year" and "this is the matter of the release" (Sifra, Behar, Chapter
3 6): a two-by-two whose diagonals the ink closes; claim LV25A-13.

**ARGUMENT OVERRULED BY INK (Bechukotai).** "You have answered the
argument — what do you answer the VERSE?" (R. Akiva to R. Yochanan
b. Nuri, Sifra, Bechukotai, Chapter 9 11): a valid distinction
defeating an analogy does not defeat a text; the verse "it and its
substitute shall be holy" decides the firstborn; claim LV27-05.

**THE BOUNDARY YEAR BY VERBAL ANALOGY, LENIENT AND STRICT ALIKE
(Bechukotai).** The sixtieth year counts below (a stringency); the
fifth and twentieth cannot be inferred from it because there it
would be a leniency — so "year"-"year" carries the rule as a verbal
analogy, which runs "whether lenient or strict" (Sifra, Bechukotai,
Section 3 10-11): the a-fortiori's direction-sensitivity against the
gezerah shavah's direction-blindness, stated on the page; claim
LV27-02.

**THE PARTICLE FOR THE MATRIARCHS (Bechukotai).** אֶת (et, the
object marker) in "My covenant with Jacob... Isaac... Abraham"
includes the matriarchs by Genesis 49:31's "Abraham AND Sarah"
(Sifra, Bechukotai, Chapter 8 8): the amplifying particle run on the
covenant list; and the reversed order read as a FALLBACK CHAIN
(Chapter 8 6); claim LV26-27.

Watch item, not yet a row: WILL-INDEXED DISPATCH stands at TWO
recorded exemplars in the campaign; per the Move Catalog's standing
rule a third exemplar registers it as a move (M-family), not a
middah. SECOND WATCH (2026-09-05): THE DEMOTION OPERATOR — "the
verse DETACHED him from the severe impurity and brought him to the
light" (Sifra, Metzora Parashat Zavim, Chapter 7 3, the menstruant's
partner) — a grade-shift instruction in the tradition's own words;
ONE exemplar, watching for a second.

## How the middot enter the process (THE_STEPS.md)

- **Step 4 (read and log):** when a source ARGUES by a middah, the
  ledger note names it (e.g. "argues I1 qal wa-chomer from the paid
  keeper").
- **Step 5 (extract claims):** every claim carries a `middah:` field
  when the source's inference form is identifiable — I-rules in law
  spans, E-rules in narrative spans; absent = plain-statement claim.
- **Step 6 (write the logic):** claims licensed by a middah keep the
  middah's own constraints as assertions (dayo cap, genus match,
  third-verse resolution). Where TIR and a middah overlap, the TIR
  rule cites the middah as chain authority.
- The book's worked example for I1 is the BAILEE ladder of Exodus 22
  (Bava Metzia 95a) — TOP10 block 4's own territory; first real
  workout for QAL_WACHOMER when block 4 opens.
