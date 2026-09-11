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
  definite." → mechanically a join over our word-level data — BUT THE
  JOIN IS NOT OURS TO RUN. ⚠ THE RECEPTION RULE (read on the local
  shelf at sitting LR1, 2026-09-07; the link review the owner ruled
  the same day): אֵין אָדָם דָּן גְּזֵרָה שָׁוָה מֵעַצְמוֹ ("a person does not
  derive a verbal analogy on his own") — Babylonian Talmud Pesachim
  66a:12, the gemara on Hillel's Passover analogy ("granted the
  analogy you had not received... but the a-fortiori, which a person
  derives on his own, you should have derived yourselves"), and Niddah
  19b:12 ("a person derives an a-fortiori on his own and does not
  derive a verbal analogy on his own"); Jerusalem Talmud Pesachim 6:1,
  where the elders of Beteira refuse Hillel's analogy BY this rule,
  accept him only on "thus I heard from Shemaiah and Avtalyon," and
  R. Abba bar Mamal states the REASON: deriving on one's own from
  "garment of skin" / "garment of skin" (Lev 11, Num 31) would make a
  creeping thing defile in a tent — the shared word is an UNBOUNDED
  GENERATOR; Rashi on both Bavli seats, narrower: "perhaps the verse
  came for another matter." Two riders from the same Jerusalem
  passage: an analogy may UPHOLD a received learning, never overturn
  it; one refutes an a-fortiori, never a received analogy. Tosefta
  Pesachim 4:11: Hillel's "and further, I have received from my
  teachers" as a fourth, separate argument beside the three
  inferences. THE COUNTERPART: I1, the a-fortiori a person MAY derive
  alone — but never a warning or a penalty from it (Rashi on Pesachim
  24a, Makkot 5b: "one does not warn from an inference"). THE
  MACHINE'S FORM: a verbal analogy is a DATA channel (received), not a
  compile rule; the lemma scan may ENUMERATE shared-token candidates,
  it may not LICENSE one. Every link the machine's shape makes — a
  seat, a dependency edge, a unification, a type grouping — answers
  THE TWO QUESTIONS before it is written, the answer beside it: (1)
  REFERENCE or TRANSFER? A reference is the ink naming an institution
  and the edge calling its definition ("the sin offering" at Lev 5
  calls Lev 4's engine) — licensed by ink alone. A transfer is a rule
  moving between contexts on a shared word or a topic — this middah.
  (2) If a transfer, TAUGHT BY WHOM? A sugya, a Sifra passage, or a
  catalogued move WITH its exemplar named. An untaught transfer stands
  only as a labeled HYPOTHESIS (class H): the value kept, the flag
  changed, never counted as compiled. The contract is a field: `link:`
  (reference / transfer / hypothesis / none / UNCLASSIFIED) and
  `taught_by:` on every edge and pointer of
  World/step9/dependency_dispositions.yaml and on every multi-seat type
  of World/step9/event_vocabulary.yaml; the dependency gate and the
  registry lint refuse a transfer without a teacher and a new entry
  without the field; the claim verifier refuses a claim seated after
  LR1 without a middah label. RECORDED AS A CHOICE: the tradition has
  two licensing regimes — reception, and FREENESS (מֻפְנֶה, mufneh: the
  token has no other job in its verse; Ramban on Niddah 22b, "an
  analogy not free at all is not derived from") — and Haggahot
  Ya'avetz on Niddah 22b reads the Tannaim as divided on whether
  reception is required at all. Freeness is the one machine-checkable
  property and only RANKS an analogy; this project gates on reception.
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
- **A verbal analogy that lands on a machine census** (Keritot 25b:4
  and Horayot 11a:20-11b:1, opened at sitting L1 of the compile debt,
  2026-09-05): the cold compile of Lev 4 counted the domain phrase —
  a "commandments" token with "which shall not be done" — at five
  seats across two chapters (4:2, 13, 22, 27; 5:17), and "his God"
  at 4:22 alone among the four tiers; then the Talmud was opened per
  gap and Rava's derivation of the suspended ram's domain runs on
  מצות מצות ("commandments"-"commandments," the second of the
  thirteen, a verbal analogy) between 5:17 and the fat sin offering
  of chapter 4, while the king's identity runs on ה' אלהיו ("the LORD
  his God") between 4:22 and Deut 17:19. The middah's two pegs are the
  census's own tokens: a gezerah shavah (verbal analogy) is, in the
  machine's terms, a shared-token edge — one the lemma scan can
  ENUMERATE but only the tradition's reception LICENSES (the reception
  rule under I2, corrected at sitting LR1, 2026-09-07: the scan finds
  candidates, the teacher names the link; the order is reception first
  and token pair second, never the reverse) — the demonstrate/compile/link finding
  (the nose-predicate specimen) repeated on a law chapter, with R.
  Zeira's third instance beside it (Keritot 26a:19: "knowledge" at
  4:14, 23, 28 — the tokens that keep the known sin from lapsing at
  the Day of Atonement).

- **A building block checked against the census that grounds it** (Sifra,
  Kedoshim, Chapter 9 14, graded at sitting L3 of the compile debt,
  2026-09-05): the Sifra's FORMULA DECODER — "their blood is upon them"
  means STONING wherever it stands — is a binyan av (a building block,
  the third of the thirteen) stated from one exemplar. The cold compile
  of Lev 20 censused the formula first: דמיהם בם ("their blood is upon
  them") at 20:11, 12, 13, 16, 27 and דמיו בו ("his blood is upon him")
  at 20:9 — six seats — and found that exactly ONE of them, 20:27,
  stands beside a mode the verse itself names (באבן ירגמו "with stone
  they shall stone them"), and that mode is stoning. The building block
  is therefore not a leap but a generalization from the formula's single
  self-labeled seat to its five unlabeled ones, and the machine's matrix
  carries the decoded seats as [MOVE] with the co-occurrence as their
  ground. Beside it, the second engine of the same sitting: Mishnah
  Yevamot 1:1's fifteen women and 1:3's six were reproduced not by any
  middah but by COMPOSITION — each Lev 18 relation seen from the
  paternal brother and normalized by the ink's own identities (my
  brother's mother is my father's wife, 18:8) — the Sifra's "a rival
  exists only from a brother" (Chapter 12 12) being that computation's
  own sentence. Two honest catches the census made before any cell was
  graded: בבהמה ("with a beast") locates two clauses (20:15 and the
  species clause 20:25), and למלך ("to Molech") three (20:2, 3, 4) — a
  union is located by its full phrase, never by one shared token.

- **The acronym rule doing law work — a narrative middah on a legal
  noun** (sitting L4b of the compile debt, 2026-09-06): E30 notarikon
  (a word read as an acronym) is listed among the thirty-two of the
  narrative set, yet Mishnah Kilayim 9:8 = Sifra, Kedoshim, Chapter 4
  18 reads the single noun of Leviticus 19:19, shaatnez (the wool-
  and-linen mixture), out as its three letters' predicates — carded,
  spun, woven — and the LAW of the garment is the conjunction: only
  what is all three is forbidden to wear, the felts coming in "by the
  name" (they are carded). The cold runner carries the three as the
  cell's value. Recorded beside the two-constraint solve of the same
  chapter (the razor, move M-21 in logic/MOVE_CATALOG.md): one noun =
  three conjoined predicates there, two verses = one intersected
  predicate here — the tradition builds conjunctions from letters
  and from verses alike.

- THE VERBAL ANALOGY RUN IN BOTH DIRECTIONS AT ONCE (I2, gezerah shavah — "an equal decree", the shared-token
  analogy; recorded 2026-09-06, sitting L5, the priesthood compile). The Sifra on Lev 21:5 lays the priests'
  mourning marks beside Israel's (Lev 19:27-28) on two shared tokens — קרחה ("baldness") with קרחה, and שרטת ("a gash")
  with שרט ("gash", the verb's root at Lev 19:28) — and moves law BOTH ways across each: per-spot and whole-head travel from the priests to Israel, and
  for-the-dead-only travels from Israel to the priests (Sifra, Emor, Chapter 1 3 and 1 5). The same shape at
  Section 7 13 on the two BLEMISH LISTS: גרב ("garav") with garav and ילפת ("yalefet") with yalefet carry the beast's
  wart to the man and the man's dak and tevallul to the beast — and the compile measured that the two lists share
  exactly those two tokens and one more (שרוע, "sarua"), so the middah runs on tokens the ink already shares. The
  governance point: the analogy is not a one-way import of a stringency but a MERGE of two partial tables into one,
  each side keeping what only it wrote; the machine form is a union of the two seats' predicates keyed on the shared
  token. Beside it, the amplification by the repeated subject — "man... man" (Lev 21:17-18; 22:4; 22:18) — is the
  Sifra's standard inclusion move (Chapter 3 2: the Kushite class UNFIT in man by "man... man" against the beast; Section
  7 2: gentiles vow by "man, man"), a ribbui (an inclusion by a repeated or extra token) that the compile verified as a
  doubled token at each seat before reading the inclusion off it.

- WHICH SEATS MAY TEACH: THE HOUR AGAINST THE GENERATIONS (a governance rule on the verbal analogy and the
  inclusion when the source seat is a NARRATED ONE-TIME ACT; recorded 2026-09-06, sitting D8, the eighth day's run).
  The tradition derives standing law from Leviticus 9's narrative — the right hand from כפו ("his palm", 9:17) with
  Leviticus 14:15's "the left palm" (Menachot 9b:17), hand-laying for the obligatory burnt offering from כמשפט ("as
  prescribed", 9:16) read as "as the freewill's law" (Menachot 93b:3), the blessing's posture and timing from 9:22
  (Sotah 38a:6, 38b:7) — and then argues about whether such a seat may teach at all: Rav takes 9:17's repeated fistful
  as an indispensability marker; Shmuel refuses, דורות משעה לא ילפינן ("generations are not learned from the hour",
  Menachot 19b:4), and the sugya presses Shmuel with his own ruling from Numbers 7:13's basins. The governance point:
  the SEAT TYPE of a source verse (law paragraph or narrated execution) is a parameter on the middah, with two recorded
  settings, beside the adjacency-validity parameter recorded at the Exodus campaign; the compile carries the fork as a
  two-arm value and registers the direction as move M-22 in logic/MOVE_CATALOG.md. The same sitting measured the
  reverse direction as a gate: the run's 'as the LORD commanded' stamps (9:7, 9:10) are RUN_CITATION pointers the
  dependency census requires and the scene grades — verification runs run-to-spec, legislation spec-from-run.

- THE VERSE SPEAKS OF THE COMMON CASE (דבר הכתוב בהווה, "Scripture spoke of what is usual" — a reading rule that
  narrows nothing; recorded 2026-09-06, sitting E1, the ordinances compile). The Mekhilta names the rule on Exodus 22:30's
  "flesh IN THE FIELD torn" — the field is the ordinary place a beast is torn, the house is included by the carcass analogy
  — and cites it on three parallels; Mishnah Bava Kamma 5:7 applies the same rule to 23:4-5's "ox or donkey" ("why ox or
  donkey? Scripture spoke of the usual"), extending the return and the unloading to every beast; the Mekhilta on 22:17
  reads the feminine "sorceress" the same way (man and woman alike, the woman named because she is the usual case). The
  governance point: a concrete noun in a case clause is a SPECIMEN, not a scope limit, unless a second token fixes the
  scope (22:24's "My people... the poor with you" is read as a ladder, not a specimen, because the Mekhilta pairs it with
  Deut 23:21's foreigner) — the machine form is a predicate over the class the specimen belongs to, with the specimen kept
  as the exemplar on the cell; the compile carries the rule at the torn, the enemy's animals, and the sorceress.

- **The minimum plural is two** (2026-09-06, sitting E2 — Menachot
  29a:1 on the lampstand's knobs): where the ink writes a bare plural
  with no number — כַּפְתֹּרֶיהָ ("its knobs", Exod 25:34) — the count is
  read as TWO, the least a plural can carry; so the lampstand's knobs
  are eleven (six on the branches, three under the pairs, two on the
  shaft) and its flowers eight from Exodus alone, the ninth fetched
  from Numbers 8:4's "to its flower". A counting rule of the law
  channel, applied whenever a Mishnah row gives a total the verse's
  numerals do not reach; recorded as a MOVE, never as ink.
- **The run may correct the spec's order** (2026-09-06, sitting E2 —
  Berakhot 55a:12 against Midrash (midrash: "expounding") Tanchuma, Vayakhel 6:5): when a
  narrated execution builds in a sequence the command did not write
  (the house before the ark, Exod 36:8 before 37:1, against 25:10
  before 26:1), the tradition may rule the RUN's order the original
  and the SPEC's written order the messenger's inversion — the second
  form of M-22 (at D8 the run gave the spec a column; here its order).
  The two recensions assign the argument to opposite speakers; both
  tracks are carried, the direction itself a recorded parameter.

- **Adjacency across a chapter boundary** (2026-09-06, sitting E3 —
  Babylonian Talmud Zevachim 88b:5, Arakhin 16a:13): R. Inini bar
  Sasson — 'why is the offerings section (Exod 29) juxtaposed to the
  priestly garments section (Exod 28)? to tell you: as offerings atone,
  so the priestly garments atone.' The adjacency middah licensed by the
  SECTION order across the chapter break, giving the garments the
  offerings' predicate; the eight functions then keyed each to a token
  or a position (the tunic by Joseph's tunic in blood, the breeches by
  28:42's own clause, the robe by 28:35's sound, the plate by the
  forehead-word's two seats). The ink's five function clauses and the
  tradition's three fill one column.
- **The homograph is the derivation's engine** (2026-09-06, sitting E3
  — Yoma 71b:6): the sixfold thread of the priestly garments is derived
  from five tokens of שש ("fine linen") at Exod 39:27-28 — and the count
  SIX is the word itself, שש ("six"), in the unpointed text. A written
  form carrying two words (as זר, "stranger" / "crown" at the ark's
  rim, E2) is read as BOTH: the material-word supplies the numeral. And
  the tokens are the RUN's, not the spec's (the spec writes 'fine
  linen' twice at 28:39) — move M-22's parameter form.
- **The particle test: 'not' is not 'so that not'** (2026-09-06,
  sitting E3 — Yoma 72a:8-9): Rav Acha bar Yaakov's objection at the
  robe's 'it shall not be torn' and the breastplate's 'it shall not be
  detached' — 'perhaps a design spec: make a border SO THAT it not
  tear?' — answered 'is it written שלא ("so that not")? it is written
  לא ("not")': a bare negative is a standing prohibition (lashes), a
  purpose clause would be a manufacturing instruction. The same test
  the ark's staves passed at E2 (25:15); the three bans one family.
- **Which neighbor scopes a clause is itself a recorded fork**
  (2026-09-06, sitting E4 — Zevachim 83b:12): Exod 29:37 'whatever
  touches the altar becomes holy' (כל הנגע במזבח יקדש, "whatever touches
  the altar becomes holy") — fit or unfit? R. Yosei HaGelili takes the
  scope from the NEXT verse ('lambs', 29:38), R. Akiva from an EARLIER
  one ('a burnt offering', 29:18): both reach Mishnah Zevachim 9:1's
  'what is fit for it', by two different neighbors. The parse-direction
  meta-rule (a verse expounded on what precedes it — Zevachim 24b, the
  vestments block) has a sibling: the DIRECTION of a scope-import is a
  parameter of the reading, recorded per authority. And the clause's
  two seats (29:37 the altar, 30:29 the vessels — כל הנגע בהם יקדש,
  "whatever touches THEM becomes holy") are two Mishnah rows (9:1,
  9:7; Zevachim 87a:11): a clause repeated with a new subject is a new
  row, not a restatement.
- **The spec/run delta is where the tradition argues** (2026-09-06,
  sitting E4 — Yoma 5b:9): the command girds Aaron AND his sons in ONE
  verb (Exod 29:9 וחגרת אתם, "and you shall gird them"); the doing
  girds him and then them in TWO (Lev 8:7 ויחגר אתו, "and he girded
  him"; 8:13 ויחגר אתם, "and he girded them") — and the dispute over
  the dressing order runs on exactly that split (Abaye: 'in the
  command and in the doing Aaron precedes' for the garments where both
  agree; the sash disputed where they differ). A reading rule for the
  spec/run pairs: the alignment's unmatched token is the first place to
  look for a sugya. Move M-22's fourth form.
- **One written form defines a unit across spans** (2026-09-06,
  sitting E4 — Zevachim 18b:15; Exod 30:13): the incense recipe's 'PART
  FOR PART' (בד בבד, "part for part", once in the Bible) is the phrase
  the Talmud uses to define the vestments' LINEN (בד, "linen" — 'each
  alone', as flax grows) — one token serving two engines; and 'twenty
  gerah the shekel' (עשרים גרה השקל, "twenty gerah the shekel") at Exod
  30:13 is the unit every later 'shekel of the sanctuary' (twenty-five
  seats) and Lev 27:25's restatement runs on, while the gerah-word's
  other eight seats are the ruminant's CUD (גרה, "cud"). A definition
  written once binds the whole code; a homograph of the unit-word is
  not the unit.

- THE SECOND SEAT'S DELTA (2026-09-06, sitting E5 — Exod 34:18-26
  against 23:12-19): a law the same book writes twice is read by the
  tradition seat against seat, and the second writing's every
  addition, drop, move, and doubling is a sugya's ground — 'in plowing
  and in harvest' (בחריש ובקציר, "in plowing and in harvest") read
  three ways (Makkot 8b:3, Menachot 72a:12, Shabbat 70a:4); 'the
  firstling of a donkey' at the two seats counted as TWICE (Bekhorot
  5b:7); the clause 'they shall not appear before Me empty' moved
  between the seats and read where it now stands (Bekhorot 51b:8);
  the inserted 34:17 legislating by adjacency (Makkot 23a:4). A
  repeated seat is a repeated token (ribbui across chapters); a moved
  clause is read at its new neighbor; an inserted verse is a
  juxtaposition the first seat never had. Move M-23.
- WHICH RECENSION OF A VERSE THE PARSE FOLLOWS IS THE CANTILLATION'S
  (Chagigah 6b:12-14, opened at E5): Rav Chisda asks whether 'bulls'
  at Exod 24:5 governs both offerings or the peace offerings alone,
  'what difference does it make? — for the PAUSING OF THE CANTILLATION'
  (לפיסוק טעמים, "for the pausing of the accents"), and the sugya
  leaves it TEIKU. The front end's accent on 'burnt offerings' (the
  etnachta) answers the named difference one way; the tradition's own
  verdict-state is carried beside it, not overwritten — the machine's
  parse and the recorded open question are two rows, both kept.
- A CLAUSE OF THE TORAH RECORDED AS ANNULLED BY A LATER BOOK (Makkot
  24a:30, opened at E5): 'Moses said (Exod 34:7) visits the iniquity
  of fathers on children; Ezekiel came and annulled it — the soul that
  sins, it shall die' — one of four decrees a prophet overrode. The
  twenty-four books demonstrate by RUN; here the run rewrites the spec
  at the register of the canon itself, and the tradition records the
  override as an override: the compile carries both seats and the
  tradition's own reconciliation beside them (Berakhot 7a:26: 'when
  they hold their fathers' deeds').

- THE FIRST CHAPTER'S OWN DELTAS ARE THE SUGYOT'S GROUND (sitting G1,
  2026-09-06): Genesis 1's nine commands against their executions —
  the tradition dates creation to Tishrei from the SPEC's 'fruit tree'
  and to Nisan from the RUN's 'tree making fruit' (Rosh Hashanah
  11a:3-6), reads the grasses' a-fortiori off the run's added 'after
  its kind' (Chullin 60a:10-12), the moon's diminishing off 1:16's
  'two great' against 'the great and the small' (Chullin 60b:2-4), the
  heretics' refutation off 'let US make' against 'and God CREATED'
  (Sanhedrin 38b:14), and the one-or-two creations off 'created HIM'
  against 'created THEM' (Ketubot 8a:9, Eruvin 18a:23, Berakhot
  61a:14): the middah at work is the same as at the tabernacle's
  spec/run pairs (M-22) — the deviation between a command and its
  execution is read as legislating, and the machine measures the
  deviation first. Beside it the counts the answer sheet rides: ten
  'and God said' against nine plus 'in the beginning' (Megillah 21b:10
  — a recorded count that does not take one of the ink's ten), 'good'
  absent on day two (Pesachim 54a:13), the article on the sixth day
  alone (Shabbat 88a:6 — a condition read off one letter).
- THE REPETITION TEST AS A SCOPE MIDDAH (Sanhedrin 59a:11-12, sitting
  G1): 'every command said to the sons of Noah and REPEATED at Sinai
  was said to both; not repeated — to Israel alone' — a law's
  addressees are decided by counting its seats across the eras, with
  a rider the sugya itself supplies: a second seat whose added job
  exhausts it (Lev 12:3 'on the day' came to permit the Sabbath,
  59b:1-2; Deut 5:27 came for the counted-body principle, 59b:3-4)
  does not widen the scope. Registered as move M-24; the machine's
  form is the dependency gate — the edge exists where the repetition
  does — and the Tzav engine's own cell states the negative boundary
  ('Israel exhorted, not the sons of Noah', Sifra Tzav Section 10 1).
- THE THIRD SEAT'S ADDED TOKEN LEGISLATES (Beitzah 16a:12, sitting G1):
  the creation-rest clause at Gen 2:2-3 ('ceased'), Exod 20:11
  ('rested'), Exod 31:17 ('ceased and was REFRESHED') — the one token
  only the third seat carries is the extra soul: M-23's delta at a
  third writing, diffed against both earlier seats; the watch set at
  E5 for Deuteronomy's third seats has its first exemplar in Exodus.

- THE ARTICLE AS THE DISTINGUISHED MEMBER (Chullin 91a:12, sitting
  G2): Rava — 'the verse says THE thigh: the distinguished of the
  thigh' — the definite article on Gen 32:33's 'the thigh' (a hapax
  articled form, measured) read as 'the best of its kind' (the right),
  a rule the tradition exports in its own words to three other
  institutions (the priestly gift's arm, Chullin 134b:16; the anointed,
  Horayot 12a:16; the pierced slave's awl, Kiddushin 21b:11).
  Registered as move M-25; the rival reading carried (Mishnah Chullin
  7:1's 'right and left'; R. Yehoshua b. Levi's embrace geometry).
- A VERBAL ANALOGY CONSIDERED AND REFUSED (Yevamot 59a:8, sitting G2):
  'a widow he shall not take' (Lev 21:14) — 'lest you say: learn
  WIDOW-WIDOW FROM TAMAR (Gen 38:11), as there from marriage so here —
  it teaches us no': the tradition names a gezerah shavah on the widow
  token between the family code and the priesthood's ban and REFUSES
  it — governance on the second middah: a verbal analogy is not free
  to make; the dependency census's family-to-priesthood edge on the
  same token is the tradition's own attempted analogy, recorded with
  its refusal.
- THE EXCEPTION AS AN ABSENCE (Mishnah Chullin 7:6, Chullin 100b:3 and
  101a:3, sitting G2): the repetition test's one stated exception (the
  sinew — 'said at Sinai, written in its place') appears in the machine
  as a MISSING EDGE — the census homes the sinew's token at the family
  runner alone and requires nothing; R. Yehuda's 'forbidden to the sons
  of Jacob' and the sages' 'the nation's clause' are two readings of one
  subject, and the subject is the ink's own anachronism ('the sons of
  Israel' — the phrase's first seat in the Bible at 32:33, four verses
  after the name is given); Rava derives the pure-only scope from the
  verse's own restriction ('one whose sinew is forbidden and flesh
  permitted').
- NO DECISION BESIDE THE MACHINE'S PARSE (Yoma 52b:4, sitting G2):
  'cursed' (Gen 49:7) is one of Issi b. Yehuda's five verses 'with no
  decision' — whether the word closes 49:6 ('they houghed an ox —
  cursed') or opens 49:7 ('cursed be their anger') — where the verse
  division (the front end's parse) has already placed it at 49:7's
  head: the second exemplar of the TEIKU-beside-a-parse watch (E5's
  Exod 24:5); the tradition's recorded indecision and the Masoretic
  division's decision both kept, neither converted into the other.
- THE RECEPTION RULE AT HILLEL'S OWN ANALOGY (Pesachim 66a:11-12, Niddah
  19b:12, Jerusalem Talmud Pesachim 6:1, Tosefta Pesachim 4:11 — read on
  the local shelf at sitting LR1, 2026-09-07, the link review the owner
  ruled after W5): the tradition's governance on the second middah
  stated as LAW, not only as a refusal (compare the widow-widow entry
  above) — the verbal analogy must be RECEIVED; the a-fortiori may be
  derived alone and is the refutable one (Hillel's a-fortiori refuted
  first as constant-and-wholly-burnt, his analogy accepted on
  reception). The machine's own record of the breach: the dependency
  gate's "shared type token = required edge" ENUMERATES analogies at
  scale (154 edges, 72 pointers), and the registry's levirate type was
  given a second seat at Lev 18:18 with no teacher joining it to Gen
  38:8 — a transfer by topic, ours (W5). The correction is the `link:` /
  `taught_by:` contract on every edge, pointer, and multi-seat type and
  the HYPOTHESIS class for what no teacher taught; the review LR1-LR3
  records the classification. The reason on the page (R. Abba bar
  Mamal's garment-of-skin absurdity) is the overfitting guard the
  two-verses-as-one limit above states from the other side: analogy
  propagation is bounded by reception at its birth and by the two-verse
  limit at its extension.
- THE SIFREI'S OWN CASE LAW ON NASO (Sifrei Bamidbar piskaot 1-58, read
  at THE NUMBERS WALK sitting 2, 2026-09-09 — the rows named by piska
  and row): (1) THE RULE OF REPETITION (2:1, on Num 5:6): "any section
  stated in one place, missing one thing, and repeated in another place
  is repeated only for the thing originated" — the tradition's own
  statement of M-23 (the second seat's delta), with R. Akiva's rival
  "everything in it is expounded" carried; (2) WE DO NOT PUNISH BY AN
  A-FORTIORI (1:3, on 5:3): the verse that the first middah would have
  made redundant is written BECAUSE the inference cannot carry a
  penalty — with R. Yehudah's dissent, who does punish by it and reads
  the clause for separate camps; (3) THE GENERAL-PARTICULAR AGAINST THE
  A-FORTIORI (8:1, on 5:15): "whenever a general-particular defeats an
  a-fortiori — if both can be satisfied, the a-fortiori is not
  defeated" — a PRECEDENCE RULE between I4 and I1, and its output a
  parameter: merit suspends the bitter waters (three, nine, twelve
  months; or not at all — R. Shimon b. Yochai); (4) A GENERAL THAT ADDS
  TO THE PARTICULAR (24:1, on 6:4): what is derived need not match the
  particular's nature unless Scripture specifies, as it does with the
  kernels and the skin — a variant resolution of I4; (5) THE THREE-FACET
  PARADIGM (6:1, on 5:10): "I learn a thing of three facets from a thing
  similar in three facets, not from one similar in one or two" — the
  paradigm's (I3) strength graded by shared facets, the refutations by
  the heave-offering and the first fruits answered by the count; (6) THE
  CIRCULAR A-FORTIORI FAILS, THE IDENTITY ON AN EXTRA WORD DECIDES (25:1,
  31:3, on 6:5 and 6:12/6:20): wine, shaving and corpse-uncleanness each
  refute the other's inference — "and the argument goes round and round
  ... I have not succeeded with my a-fortiori" — and 6:20's superfluous
  "nazirite" ("may a nazirite drink wine?" — the clause's one seat,
  computed) carries the verbal analogy that decides: a recorded failure
  mode of I1 and a reception of I2 on a word MEASURED extra; (7) THE
  ELEVENTH AND THIRTEENTH RULES STATED ON THEIR VERSES (37:1 on 6:20:
  "whatever was included in a general and departed for a new learning
  may not be returned until Scripture returns it" — the breast and
  thigh kept out of the nazirite's shoulder-law; 58:1 on 7:89: "two
  verses which contradict each other remain in their place until a
  third comes and reconciles them" — Lev 1:1 against Exod 25:22,
  7:89 the third) — the Sifrei's own words for I11 and I13 at their
  Naso seats; (8) THE CROSSED PARAMETER (28:1, on 6:9): the suspected
  wife equates doubt with certainty but not inadvertence with intent;
  the nazirite the reverse — each a-fortiori refuted by the other
  engine's difference: a paired setting on two laws, recorded as such.
- THE SIFREI'S OWN CASE LAW ON BEHA'ALOTCHA (Sifrei Bamidbar piskaot
  59-63, 72-106, read at THE NUMBERS WALK sitting 3, 2026-09-10 — the
  rows named by piska and row): (1) DAYO — THE A-FORTIORI'S CAP (106:1, on
  Num 12:14): "if her father had spat in her face, would she not be
  ashamed seven days?" — the father's seven would give Him who spoke and
  made the world fourteen, "BUT IT SUFFICES THAT WHAT IS DERIVED FROM AN
  A-FORTIORI BE AS THAT FROM WHICH IT IS DERIVED": seven — I1's ceiling
  stated by the tradition on the verse the Talmud derives it from (Bava
  Kamma 25a; Mishnah Bava Kamma 2:5); (2) THE THREE-FACET PARADIGM AGAIN
  (60:1, on 8:3): the sons equated with the father for the incense by
  three shared terms — service in the tent, golden vestments,
  "continually" — the refutations (Yom Kippur's linen; the anointed
  priest's bull) answered by the count, "not from a thing similar in one
  or two": Naso's 6:1 rule stated a second time; (3) TWO MIRROR
  A-FORTIORIS EACH REFUSED BY THE VERSE'S OWN CLAUSE (62:1, 63:1, on
  8:24-26): the Levites' blemishes ("this is what applies to the
  Levites") and the priests' years ("thus shall you do with the Levites"
  — and not with the priests) — the verse written to cap the inference,
  as at Naso's 1:3; (4) THE IDENTITY ACROSS BOOKS AND A MEMORY REPAIRED
  (73:2, 75:1, on 10:5-8): "teruah" here / "teruah" there carries the
  desert's tekiah-teruah-tekiah to Rosh Hashanah (I2), and "priests" /
  "priests" with Lev 3:2 decides the blemished — where R. Tarfon's
  TESTIMONY (his lame uncle blowing) is answered by R. Akiva's
  reconstruction of the day (the shofar of Rosh Hashanah or the
  Jubilee's Yom Kippur): "Tarfon saw and forgot; Akiva expounded of
  himself and matched the halakhah" — a witnessed memory yielding to a
  derivation, the tradition recording its own memory failure and repair
  (as at Shevuot 20b); (5) THE PROTOTYPE ON A SUPERFLUOUS WORD (73:2):
  "second" (10:6) as a binyan av (I3) placing the tekiah after the
  teruah; and the induction "blowing" / "blowing" for the princes'
  gathering place (73:1); (6) TWO VERSES RECONCILED BY A MODEL, NO THIRD
  VERSE (84:2, 84:5, on 10:35-36 against 9:23): "by the word of the LORD
  they journeyed" and "Moses said: Rise, LORD" — the cloud folded until
  Moses spoke — a reconciliation by an analogy (the king and his lover),
  the form beside I13 without its third verse; and 10:2's trumpets kept
  beside 9:23's cloud (72:1); (7) THE LEXICAL RULES WITH PROOF-SEATS: "unto
  Me" = forever at ten seats (92:1 — every one machine-checked on the ink);
  "the people" = the wicked, "My people" = the upright (85:1); dibbur is
  harsh speech, amirah imploration (99:1); "na" implores (80:1, 103:1);
  "Cushite" = exceptional (99:1); "vayehi" = a return to a former state
  (85:1) — the shelf's lexicon as law, each with its verses; (8) THE NAME
  BY THE EVENT (86:1): Taberah, Massah-Meribah, the graves of lust — "I
  might think it was its name before; it says 'because'" — a naming rule
  read off the causal clause; (9) SCRIPTURE'S EUPHEMISMS (84:4): the
  tradition's list of the ink's transmitted euphemisms includes two of
  this portion's verses — 11:15 "my evil" (for "their"), 12:12 "his
  mother... his flesh" (for "our") — recorded as the tradition's claim
  about the ink, Onkelos resolving the second; (10) THE SPEAKER SPLIT
  (88:1, on 11:6-7): adjacent clauses of one verse assigned to two
  speakers — Israel's "only the manna" and God's "like coriander seed" —
  with seven parallels; the catalog held no such move: REGISTERED as
  M-27 (MOVE_CATALOG.md); (11) MEASURE FOR MEASURE (106:1, on 12:15 =
  Mishnah Sotah 1:9): "with the measure a man measures" — Miriam waited
  a short while, Israel waited seven days — E27 with the answer sheet's
  own row on the verse.
- THE TALMUD'S CASE LAW ON NASO, READ AT THE COMPILE (THE NUMBERS WALK
  sitting 2b, 2026-09-10 — the exam docket's crowns, logic/oral_triage/
  num_04_07_naso_exam_2026-09-10.md; the three now RUN in
  cold_run_naso.py's cells): (1) THE METHOD FORK'S FOURTH SEAT (Nazir
  34b:5-7 on Num 6:4 "from all that is made of the grapevine, from seeds
  to skin"): the Rabbis run general–detail–general (I5) — the middle
  terms limit to the fruit and its refuse, the leaves and shoots free;
  R. Elazar runs amplified–limited–amplified — everything but the leaves
  and shoots... the fork named on the verse and the two arms both
  recorded; the nazirite cell's ate('leaves') returns the Rabbis' arm
  with R. Elazar's beside it (the fourth exemplar of the fork after
  rounds 25, 26, 28 — the middah choice a model parameter, as ruled);
  (2) THE HALAKHAH UPROOTS THE VERSE (Sotah 16a:6, R. Yishmael): "in
  three places the halakhah supersedes the verse — the Torah says WITH
  DUST (Lev 17:13) and the halakhah says with anything; the Torah says
  WITH A RAZOR (Num 6:5, 6:9's shaving) and the halakhah says with
  anything; the Torah says A SCROLL (Deut 24:1) and the halakhah says any
  detached thing" — a received rule OVERRIDING the ink's own word, the
  tradition naming the override and counting its seats: for the machine
  the razor is the data row (the ink), the override a recorded setting
  ON the row, never a silent replacement — the nazirite cell's
  shaving_means('plucked_any') / final_shaving_tool carry both; (3) THE
  A-FORTIORI REFUSED BY A HALAKHAH TO MOSES FROM SINAI (Mishnah Nazir
  7:4; Nazir 57a): R. Akiva argued that a quarter-log of blood, which
  defiles by tent, should certainly negate the nazirite's count (a
  barley-grain bone negates and does not defile by tent); R. Eliezer:
  "what is this, Akiva? — we do not argue here from an a-fortiori" (the
  quarter-log's exemption is a halakhah to Moses from Sinai), and R.
  Akiva reports that even Rabbi Yehoshua "did not approve my inference"
  — I1 BLOCKED by an oral datum with no verse: the machine's
  impurity_kinds('quarter_log_blood') returns the halakhah's verdict with
  the refused inference recorded as its provenance. Beside these the
  docket recorded the middot's smaller case law at their seats: the
  equating rule "a woman equals a man for all punishments" (Bava Kamma
  15a:4 on 5:6 — a binyan av, I3, from "man or woman"); R. Natan's rule
  (5:7's "he shall restore" — the confession's verse as the seat of the
  guilt-offering's rule of repetition, Sifrei 2:1); the attribution of
  one teaching VARYING BY TRACTATE (Nazir 38b:4 gives Rava one set of
  lashes for a seed, Pesachim 41b:5 the same dispute with the names
  crossed — recorded as a variant, both arms kept); and the Targum
  deciding a lexical dispute (Nazir 39a:2 — chartzan the seed and zag
  the skin by Onkelos's rendering, against R. Yosei's reversal).
- THE TALMUD'S CASE LAW ON BEHA'ALOTCHA, READ AT THE COMPILE (THE
  NUMBERS WALK sitting 3b, 2026-09-10 — the exam docket's crowns,
  logic/oral_triage/num_08_12_beha_exam_2026-09-10.md; each now runs in
  cold_run_beha.py's cells): (1) THE ARTICLE BLOCKS THE IDENTITY (Yoma
  76a:1): "man" (Num 27:18) is matched to "man" and reads Joshua; it is
  NOT matched to "THE man Moses" (12:3) — "we can learn 'man' from
  'man', not 'man' from 'the man'": a rule about I2's token-matching —
  the article is part of the token the identity compares, so a bare
  noun and an articled noun are different keys. For the machine: the
  verbal analogy's key is the surface form with its prefix, not the
  lemma (the corpus' identity edges are matched on the consonantal
  token; this seat says the rule is the tradition's own). (2) THE
  IDENTITY CARRIES AN ORDER, NOT ONLY A VALUE (Rosh Hashanah 34a:6-8;
  Sifrei 73:2): "teruah" in the wilderness (Num 10:5-6) / "teruah" at
  Rosh Hashanah (Lev 23:24) — what moves through I2 is the WHOLE SHAPE
  tekiah-teruah-tekiah, built on the superfluous "second" (10:6) by a
  binyan av (I3) first and then carried by the identity; and the two
  readings of the shape — R. Yehuda's one unit against the Rabbis' three
  sounds (Arakhin 10a; Sukkah 53b) — argued from the tekiah-root verb
  standing on the teruah: a MORPHOLOGICAL premise (the verb's root
  names the other sound) deciding a procedural count. (3) DAYO AT FOUR
  SEATS, ONE OF THEM THE ANSWER SHEET (Bava Kamma 25a:3, 25a:8; Bava
  Batra 111a:5; Zevachim 69b:6; Mishnah Bava Kamma 2:5): the a-fortiori's
  cap proved from Miriam's seven days is TORAH LAW (the baraita of the
  principles), made GENERAL by the run verse 12:15 (else one might say
  "out of respect for Moses"), and applied on the Mishnah's own row to
  the goring ox — R. Tarfon's two inferences each capped by "it
  suffices"; sitting 3 entered the rule on its home verse, the compile
  entered its four seats and the machine's data row (7 of 14). (4) "WITH
  YOU" READ FOUR WAYS FROM ONE TOKEN (Sanhedrin 17a:1-2; Horayot 4b:14;
  Kiddushin 76b:6; Sanhedrin 36b:4, 36b:10): 11:16-17's "with you" is
  the Sages' count (Moses among the seventy-one), R. Yehuda's "like you"
  (fit to rule; whole in body; of fit lineage) — one preposition with a
  pronoun yielding a numeral, a competence rule, a bodily rule and a
  lineage rule at four tractates: the same seat returning four verdicts,
  each recorded with its authority (the cell's with_you). (5) THE
  SPINE'S TWO ARMS ON THE ANSWER SHEET (Sanhedrin 17a:12-13 against
  Onkelos 11:25): "they prophesied and did not continue" — the gemara
  proposes the very reading the Targum chose ("did not cease", from
  Deut 5:19's great voice), rejects it for the seventy, and settles the
  two by the PARTICIPLE at 11:27 ("Eldad and Medad ARE prophesying"):
  a grammatical form (the durative participle against the perfect)
  deciding between two readings of one verb — sitting 3's dual-track row
  resolved by the exam's own argument, both arms kept as the setting
  continued. (6) THE HALAKHAH'S ALLUSION VERSUS ITS PROOF (Moed Katan
  16a:20): admonition's seven days "has no proof but an allusion" from
  12:14 — the tradition grading its own derivation's strength (a hint,
  not a source): the label class the corpus' claim labels carry as
  'plain' against a middah-derived claim.
- THE SIFREI'S OWN CASE LAW ON SHELACH (the Sifrei on Numbers piskaot
  107-112, read at THE NUMBERS WALK sitting 4, 2026-09-10 — no piska on
  chapters 13-14; logic/oral_triage/num_15_offerings_laws_2026-09-10.md):
  (1) THE SPECIFIED INSTANCE TEACHES THE FORMULA (107:1, R. Yishmael):
  "comings" stand unqualified through the Torah and one seat (Deut
  17:14) specifies "and you inherit it and settle in it" — so every
  "when you come to the land" means after inheritance and settlement:
  I8's form applied to a FORMULA rather than a case (the one specified
  member teaches the class); R. Akiva's objection from the Sabbath's
  "settlings" (Lev 23:3 — the word's seat, computed) answered by an
  a-fortiori (I1: the lighter obtain everywhere, the graver the more so),
  and the same word then DISPUTED — bars libations on a private altar
  (Yishmael) or permits them (Akiva). (2) THE VARIED FORMULA READ AS LAW
  (110:1, R. Yishmael): every other "coming" reads "when you come" /
  "when the LORD brings you"; 15:18 alone reads "UPON your coming" — so
  challah devolves at once on entry. MEASURED: "upon your coming to the
  land" is the form's one Torah seat against Exod 12:25, 13:5; Lev 23:10,
  25:2; Deut 6:10, 11:29, 17:14 — a lexical variation at one seat of a
  formula legislating; entered as M-23's exemplar (12). (3) THE ANALOGY'S
  TARGET IS CHOSEN BY THE INK, NOT THE ARGUER (110:1): R. Yoshiyah likens
  challah to the threshing-floor's terumah for its whole law; R. Yonathan
  "whispers" — why that terumah, whose measure is unstated, and not the
  tithe's terumah (Num 18:26) whose tenth is explicit? — answered by the
  clause's own naming: "as the terumah of the THRESHING FLOOR" (15:20 —
  the phrase's one seat, computed): a governance row — when two analogues
  are available, the verse's own word picks the base; the arguer may not.
  (4) THE A-FORTIORI REFUSED BY THE WORD "ONE" (111:2) — twice on one
  verse: the congregation's second bull (from Lev 4:14) and Yom Kippur's
  two goats would follow a fortiori; "ONE young bullock", "ONE kid of
  goats" refuse both (the parser reads the two ones); and REFUSED BY "TO
  ALL THE PEOPLE" (111:3) — the high priest's bull would follow from Lev
  4:3 and 16:3; the clause excludes him (he brings the individual's
  she-goat). The lamb/ram differentiation likewise HELD against the
  a-fortiori from the undifferentiated calf and ox (107:2). Four seats
  where I1 runs and the clause's own token caps it — the dayo family's
  cousin: not "it suffices" but "the text said one". (5) THE REFUTATION
  CHAIN RUN TO EXHAUSTION (107:2, Issi b. Akiva): the Shavuot lambs, the
  Yom Kippur goats, the sin-offering proposed in turn as the paradigm for
  "one kind suffices", each refuted by "Scripture expanding / limiting
  its bringing", until "it must therefore be written" closes it — the
  common-side test (I3) cycled to failure and the verse deciding: the
  shelf's own record that a paradigm is TRIED, not assumed. (6) THE
  PROTOTYPES (I3 as binyan av): no donated meal-offering under an
  issaron (107:2, R. Nathan — the ink's "a tenth" its unit); wherever
  "goat" is written, of the first year (112:1 — on the delta against
  Lev 4:28's ageless she-goat, computed); wherever "native-born",
  proselytes included (112:1 — Lev 23:42's sukkah pair with 15:13,
  computed). (7) TWO VERSES RECONCILED BY A THIRD (I13, 107:2): "for
  libations" (15:10) cannot mean on the fire, for Lev 6:6's perpetual
  fire would be quenched — so on bowls; and "as ordained" (15:24) names
  the libation table of 15:4-11 as the burnt-offering's, none for the
  sin-offering (111:2). (8) "ALL" / "ALL" (I2, Rebbi, 111:1): "all these
  commandments" (15:22) and "all likeness" (Deut 5:8) — the identity
  fixing the section's subject as idolatry, beside the ink's own delta
  against Lev 4:13-14 (the bull for a burnt-offering, the goat added —
  computed) that the Sifrei's whole reading rests on; and "bread" /
  "bread" (Deut 16:3) fixing the five species (110:1). (9) THE ANSWER
  SHEET'S ROWS WITH THEIR DERIVATIONS: Mishnah Horayot 1:5's tribe table
  (one, two, twelve bulls — Meir, Yoshiyah, Shimon b. Yochai) on 15:25
  (111:3); Mishnah Keritot 1:2's principle — karet for the willful, a
  sin-offering for the unwitting, for EVERY such act — derived by R.
  Yehudah b. Beteira from idolatry as the paradigm (I3) on 15:29 (112:1);
  Mishnah Menachot 9's mixing rule from "according to their number"
  (107:2); Menachot 12:4's three-four-six logs from "shall do thus"
  (107:3); Shekalim 7:6's gentile from the same clause; Challah 2:7's
  twenty-fourth and forty-eighth from "give" (110:2). (10) THE DOUBLED
  INFINITIVE'S FORK ON ITS CLASSIC SEAT (112:2): "cut off, shall be cut
  off" (15:31 — the pair's one seat, computed): R. AKIVA expounds the
  doubling (this world and the world to come); R. YISHMAEL refuses — 15:30
  already said "cut off": "are there three worlds? the Torah speaks in the
  language of men" — the governance rule on whether a grammatical
  doubling is expounded at all, recorded here on the verse the Talmud
  runs it on (Sanhedrin 64b, 90b; Keritot 7a; Shevuot 13a); the
  translation KEEPS the doubling. For the machine: a doubling is a
  candidate operator only under Akiva's setting; under Yishmael's it is
  the language's emphasis and no cell — two settings, the dispute
  carried. (11) THE INFERENCE RULES UNDER THE KARET CLAUSE (112:2): "the
  word of the LORD he has despised" includes one who accepts the whole
  Torah "except for this inference, this a-fortiori" (the exam's Sanhedrin
  99a) — the middot themselves inside the law they serve; and "its
  iniquity is in it" LIMITS Exod 20:5's "upon the sons" — the Decalogue's
  clause parameterized at this seat (R. Yishmael). (12) THE FOUR STRATA
  OF COMMAND FROM FOUR CLAUSES (111:1): "which the LORD spoke to Moses" =
  the ten words; "all that the LORD commanded you by the hand of Moses" =
  Moses'; "from the day the LORD commanded" = the forefathers', FROM ADAM
  (Gen 2:15 — the Eden unit's first command, the shelf's own reading of
  it); "and onward throughout your generations" = the prophets' — one
  verse's clauses as a census of the covenant's layers.

- THE EXAM'S CASE LAW ON SHELACH (the docket logic/oral_triage/num_13_15_shelach_exam_2026-09-10.md, THE NUMBERS WALK sitting 4b, 2026-09-10 — 313 rows, 141 LAW): (1) THE VERBAL ANALOGY BOUNDS A SET (Bava Batra 121b:11, Rav Acha bar Yaakov): "and upward" (Num 14:29) / "and upward" (Lev 27:7, the valuations) — the decree's set closed ABOVE SIXTY as the valuations' class is; the ink's own floor (twenty) stands, the ceiling is the analogy's: I2 TAUGHT, a transfer between a narrative decree and a law table (Yair son of Manasseh the exemplar). (2) THE DOUBLE ANALOGY BUILDS A QUORUM (Berakhot 21b:5 — Rabbenai's baraita; Megillah 23b:8; Sanhedrin 74b:3 — Rav Yannai): "among" / "among" (Lev 22:32 → Num 16:21) and "congregation" / "congregation" (16:21 → 14:27) — ten from the ten spies (the twelve less Joshua and Caleb: Mishnah Sanhedrin 1:6): a chain of two I2 links, each with its teacher, and the count computed on the spies' own list. (3) THE JUXTAPOSITION AS THE CLASS RULE (Horayot 8a:14, R. Yehoshua ben Levi to his son; Keritot 3a:20; Shabbat 69a:1; Yevamot 9a:9): 15:29 "one Torah for the one who acts unwittingly" beside 15:30 "with a high hand... cut off" — the whole Torah likened to idolatry: intentional karet (the cutting-off), unwitting sin offering — the adjacency reading the chatat engine carries by CALL; Munbaz (Shabbat 68b:6) reads the same adjacency for prior knowledge. (4) THE DOUBLED INFINITIVE DISPUTED AT THREE SEATS (Sanhedrin 64b:21-22, 90b:18; Shevuot 13a:2): R. Akiva's two worlds, R. Yishmael's "the Torah spoke in the language of men", Rabbi's before-and-after Yom Kippur — the fork this file holds from the Sifrei (112:2), now with the Babylonian Talmud's three seats and a third reading. (5) AN ANALOGY PROPOSED AND REFUSED ON THE RECORD (Makkot 13b:12): R. Abba bar Memel's "from the eyes" (Num 15:24) / "before your eyes" (Deut 25:3) would flog the executed — rejected: I2 needs a teacher, and the record keeps the refusal. (6) THE VERSE'S OWN ORDER AS LAW (Horayot 13a:4 — Rava bar Mari, Rava; Zevachim 90b:6 — Ravina): "according to the ordinance" read as the sequence written, the bull before the goat; the aleph-less "for a sin offering" (once in the Bible — sitting 4's crown, computed) the second ground: an ink-level fact carrying a rule. (7) THE REVOCALIZATION AT THE SPIES' WORD (Sotah 35a:7; Arakhin 15a:12; Menachot 53b:9 — R. Chanina bar Pappa): "stronger than us" read "stronger than Him" — the same consonants, the pronoun's referent turned: M-16's class with its teacher named at three seats; Arakhin 15a:13 then rules the punishment was for the report, not this blasphemy — the move recorded and its verdict bounded. (8) THE INCLUSION FROM THE DEFINITE ARTICLE (Menachot 91b:9 — R. Natan; 91b:20): "for THE one lamb" includes the woman-after-childbirth's olah, "THE one" the animal tithe's eleventh, "for THE one bull" the calf — I8's specified-member form on a token the parser had left silent (THE DEFINITE ONE, taught this sitting): the tradition reads the very word.

- THE SIFREI'S OWN CASE LAW ON KORACH (the Sifrei on Numbers piskaot
  116-122, read at THE NUMBERS WALK sitting 5, 2026-09-10 — no piska on
  chapters 16-17; logic/oral_triage/num_18_priest_levite_dues_2026-09-10.md):
  (1) AN A-FORTIORI OVERRIDDEN BY A DECREE ON THE RECORD (117:2): R.
  Yehudah in Netzivim to R. Yochanan b. Bag Bag — the maidservant's money
  causes her to eat terumah (Lev 22:11), so the betrothed daughter of an
  Israelite the more (I1 stated in full) — "BUT WHAT CAN I DO? THE SAGES
  SAID: not until she enters the chuppah" (Mishnah Ketubot 5:2-3): the
  inference valid and set aside by a decree, both kept on the page. (2)
  "FROM IT" IS MUFNEH — the gezerah shavah's license named (120:1): "from
  it" at 18:26 is free (not needed for its own clause) and so may carry
  the tithe's mourner-ban to the Paschal lamb's "from it" (Exod 12:9) —
  I2's own condition (the shared word must be spare) stated on the verse,
  and the direction of transfer recorded (tithe → lamb). (3) THE
  ANALOGY'S TARGET CONTESTED AND FIXED BY A REDUNDANT CLAUSE (118:1,
  Kerem Beyavneh): first-born "as the wave-breast" — the peace-offering's
  (two days and a night; Tarfon, Akiva) or the thank-offering's (one day;
  Yossi HaGelili)? — "for you shall it be" adds a second day (Akiva), and
  R. Yishmael's bar: "you would learn from what is itself learned?" (the
  thank-offering's breast is derived from the peace-offering's — a
  derived seat cannot be a paradigm): I3's choice of paradigm decided by
  the extra word, and a governance rule on second-hand paradigms. (4) THE
  A-FORTIORI PROTOCOL RUN IN FULL (118:1, the one application of blood):
  the inference (fats decrease, so blood decreases), ITS CONVERSE, the
  converse REFUTED by a third verse (Lev 1:11 "roundabout"), THE RETURN
  to the original — "I have reasoned a fortiori and adduced the converse;
  the converse has been rejected and I return" — I1 with reversal and
  refutation as a recorded procedure. (5) THREE READINGS OF ONE CLAUSE,
  EACH TAKING THE JOB THE OTHERS' VERSES LEAVE OPEN (118:1, "they are
  consecrated"): Yoshiyah — the one spilling; Yitzchak — Deut 12:27 gives
  the spilling, so the fats; Abba Chanan — the fats follow a-fortiori, so
  the spilling: a verdict table built by elimination across three verses.
  (6) THE GENERAL-PARTICULAR-GENERAL ON THE REDEMPTION MONEY (118:1, I6):
  "his redemption" / "money, five shekels" / "you shall redeem" — like the
  particular, movable and worth money: not bondsmen, writs or land (Rebbi:
  not writs) — and the objection that the particular might revert to the
  FIRST general (Exod 13:13) refused by distance. (7) THE SECTION'S SHAPE
  NAMED (118:1, I7): "general at the beginning (18:8) and at the end
  (18:19), particular in the middle" — the form itself catalogued beside
  general-then-particular and particular-then-general. (8) FOUR "NO
  MORE"S EACH PAID BY A PRIOR EVENT (116:1): "no more wrath" (18:5) by
  17:11, "no more a flood" by the flood, "no more to the goat-demons" by
  Egypt, "shall no more draw near" (18:22) by 16:35 — a lexical rule on
  the adverb, and the ink confirms the first: 18:5 is 1:53's clause with
  ONE TOKEN ADDED (computed; MOVE_CATALOG M-23 exemplar 15). (9) TWO
  DEATH-MODES FROM TWO IDENTITIES OF WORDING (116:2): "shall be put to
  death" (18:7) with 17:28's "shall die" — at the hands of Heaven (R.
  Yishmael) — or with Deut 13:6's false prophet — by strangulation (R.
  Akiva): each I2 choosing its own second seat, the fork carried (Mishnah
  Sanhedrin 9:6's row). (10) A LIKENESS THAT "COMES TO TEACH AND ENDS UP
  LEARNED" (121:1): terumat ma'aser accounted "as corn from the threshing
  floor" (terumah gedolah) — the likeness read back: as the Levite's is
  obligatory, so the Israelite's — I3's reciprocity named. (11) THE
  SPECIFIED-INSTANCE RULE ON THE FIRSTLING OF AN ASS (118:1): "the
  firstborn of the unclean beast you shall redeem" narrowed by Exod
  13:13's ass, and the REPETITION at Exod 34:20 read as a second
  exclusion (the others not redeemed at all) — and the freed clause
  REASSIGNED to Temple-dedications (M-18's form on the shelf). (12) THE
  JUXTAPOSITION'S REASON STATED TWICE (117:2, 119:2): the king who writes,
  seals and records the gift once contested — "wherefore this section is
  juxtaposed with Korach"; and "for Aaron's good did Korach come" — the
  adjacency of chapters 16-18 read as a deed's registration (E-class, the
  order of sections as evidence). (13) "BECAUSE KORACH CAME, SCRIPTURE
  REITERATED THE ENTIRE EXHORTATION" (116:1, Rebbi): the demarcation
  verses of 1:51, 3:38, 4:18-19 already fence every crossing — "both they
  and you" (18:3) is a REPETITION EXPLAINED BY EVENT, the rule against
  redundancy answered by the narrative (M-24's form on a warning).
- THE SIFREI'S OWN CASE LAW ON CHUKAT (the Sifrei on Numbers piskaot
  123-130 on the heifer, THE NUMBERS WALK sitting 6, 2026-09-11 — the
  ledger logic/oral_triage/num_19_parah_2026-09-11.md): (1) THE
  A-FORTIORI'S FULL PROTOCOL RUN THREE TIMES IN ONE CHAPTER, its formula
  verbatim — "I have reasoned a fortiori and I have transposed; the
  transposition has been refuted and I return to the original": on the
  yoke and the other labors (123:1, the heifer against the eglah arufah),
  on the sheretz and "that shall die" (125:1 — the dead confers no tumah
  until dead, the lighter the less), on the grave's open sides (126:1,
  the tent the paradigm) — the protocol the Korach sitting recorded on one
  clause is the chapter's standing instrument (I1 with reversal and
  refutation). (2) "A DERIVATION FROM A DERIVATION?" (127:4) — the bar on
  second-hand paradigms stated as a question when the open grave's
  evening tumah would be learned from the tent's, itself an a-fortiori:
  the Korach sitting's "you would learn from what is itself learned?"
  (118:1) at its second seat in the walk. (3) A VERDICT BY ELIMINATION
  (129:5): the sprinkler graver than the toucher — three rival readings
  (sprinkler/toucher, clean/unclean, fit/unfit) each REFUSED by an
  a-fortiori, "you must perforce accept the first": the water's measure —
  the a-fortiori used as the exclusion tool, not the derivation tool. (4)
  THE IDENTITY LICENSED BY A DEPARTED WORD (127:5, R. Shimon): "is it
  earth? is it not ashes? Scripture departs from its usual meaning to
  formulate an identity" — "earth" at 19:17 against "ashes" at 19:9-10,
  measured on the tokens: the gezerah shavah's mufneh condition met by a
  word the text changed on purpose (I2's license named on the ink's own
  delta, as the Korach sitting's "from it"). (5) THE SAME CLAUSE READ
  NARROW AND WIDE (125:1): "the soul of a man" EXCLUDES the blood (R.
  Yishmael), "ALL the soul of a man" INCLUDES it (R. Akiva) — I4 against
  I5 on one phrase, the dispute carried. (6) THE SECTION'S SHAPE NAMED ON
  THE OPENING (123:1): general at the head ("the statute of the Torah"),
  particular after ("a red heifer, whole"), with Exod 19:3-6 and 12:43 as
  the two other shapes and the rule stated — "there exists in the general
  only what is found in the particular" (the Korach sitting's "general at
  both ends" its sibling). (7) THE PUNISHMENT SPLIT BY TWO VERSES (125:1,
  129:3): "if he is not cleansed on the third day he shall not be clean
  on the seventh" gives the omission's punishment — uncleanness, not
  karet — and 19:20's karet is for entering the sanctuary: two effects
  read off two clauses, the compile's two verdicts. (8) THE THIRD VERSE
  FIXING THE SCHEDULE (125:1, 129:2): 19:12's "third and seventh" might
  read "if on the third, clean on the seventh"; 19:19's "and he shall
  cleanse him ON THE SEVENTH DAY" repeats to void it — I13's form on a
  timer. (9) THE TEACHER'S DELIBERATE ERROR (123:1): R. Yochanan b.
  Zakkai's "golden vestments" against his own teaching of the white,
  "to strengthen the disciples" — a recorded pedagogic falsehood, the
  tradition naming its own device. (10) THE ACADEMY'S DISPUTE READ AS A
  VISION (124:1): the cow that drank the waters — thirty-two elders, R.
  Yossi HaGelili's return, and R. Tarfon reading Daniel 8:4-7 with the
  ram as R. Akiva and the goat as R. Yossi — the shelf's aggadah (the
  lore, not the law) verdicted with the law it sits on. (11) TWO BONES AT
  TWO SEATS (127:2, 129:1): "the bone of a man" (19:16) the limb from the
  living, "him who touched a bone" (19:18) the barley-corn — and the ink
  REORDERS the four sources between the two verses, the bone moved to
  the head (computed). (12) THE VESSEL CENSUS BY THREE VERSES (126:1):
  "all that is in the tent" bounded by 19:18's "vessels", Num 31:20's four,
  31:22's metal and 19:15's earthenware — six classes, and "whatever is
  subject to cleansing is subject to tumah" as the closing rule. No new
  move; MOVE_CATALOG unchanged.

- THE SIFREI'S OWN CASE LAW ON BALAK (the Sifrei on Numbers piska 131 on
  25:1-13 — its one piska on the portion; THE NUMBERS WALK sitting 7,
  2026-09-11 — the ledger logic/oral_triage/num_25_peor_pinchas_2026-09-11.md):
  (1) THE ADJACENCY RULE DISPUTED ON THE VERSE (131:1). R. AKIVA: "every
  section juxtaposed with another is to be learned from it" — 24:14's
  "come, I will counsel you" stands above 25:1's daughters of Moab, so
  the counsel is the harlotry (E28, from-the-preceding); REBBI: "there
  are many adjoining sections in the Torah as far from each other as
  east from west" — Exod 6:12-13, Lev 21:9-10, Hos 1:9-2:1, Hos 14:1-2,
  each gap closed by a PARABLE (E26): the centurion who fled before his
  promotion, the king who doubled the ketubah (the marriage settlement)
  instead of the divorce, the general who told the province "send me
  something to relay to the king". The Numbers seat of the file's
  ADJACENCY-VALIDITY parameter (the Exodus campaign's Yevamot 4a
  entry): here the two sides are named tannaim (the Mishnah's
  teachers) on a narrative seat, and the ink carries the link itself —
  31:16 "by the word of Balaam... in the matter of Peor" (computed).
  (2) THE GOD'S OWN SERVICE AS THE OFFENCE'S DEFINITION (131:2): "the
  sages ruled that baring oneself to Peor is its mode of worship" —
  the rite's form read off the story (the harlot's "bare yourself
  before him"), Mishnah Sanhedrin 7:6 the answer sheet; the three
  anecdotes of gentiles' own scorn beside it. (3) A LAW'S INSTALLATION
  DATED BY THE SHELF (131:2): "the pitcher was full of Ammonite wine,
  the wine of idolaters having NOT YET BEEN FORBIDDEN to Israelites" —
  the decree's time-stamp relative to the event, a data row for the
  installation ledger (Avodah Zarah 36b). (4) A THREE-GENERATION TITLE
  READ AS THREE DEEDS (131:3): "Phinehas son of Eleazar son of Aaron
  the priest" — priest son of priest, zealot son of zealot (Levi at
  Shechem, Gen 34:25), turner-away of wrath son of a turner-away
  (Aaron, 17:13) — and the ink pairs them itself: "and the plague was
  stayed" at 17:13 and 25:8, "and he atoned for" at 17:12 and 25:13
  (computed). (5) THE TENSE READ OFF THE VAV-FORM (131:5): "it is not
  written 'to atone' (the infinitive) but 'and he will atone'" — the
  form read as a future ("he stands and atones until the revival of
  the dead") where the morphology tags the narrative past and Onkelos
  renders a past: a dispute on one word's tense, recorded. One move
  exemplar added: M-22 (the run teaches the spec) — Exod 34:15-16's
  "they whore after their gods... and call you and you eat of their
  sacrifice... and their daughters whore after THEIR gods" run clause
  by clause at 25:1-2, the feminine "their gods" at the two seats alone
  (MOVE_CATALOG.md).

- THE ZEALOTS' RULE AND ITS FOUR LIMITS — THE COMPILE OF BALAK (the exam docket of 2026-09-11, THE NUMBERS WALK sitting 7b; Mishnah
  Sanhedrin 9:6; Sanhedrin 81b-82b; Avodah Zarah 36b): "one who cohabits with an Aramean woman — zealots strike him" is a rule the Torah
  writes no death for, and the tradition fences it with four rules ABOUT the rule: it holds DURING THE ACT only (separated, the zealot is a
  murderer — Sanhedrin 82a:10); the pursued may kill the zealot in self-defense, a pursuer (82a:10); IT IS NOT TAUGHT — one who asks the court is
  not instructed, and the law eluded Moses himself while the Sanhedrin wept (82a:12); and its source-class is a law to Moses from Sinai, not a
  decree (Avodah Zarah 36b:9). On the tape the rule enters as rule_installed by a DEED (Num 25:7-8) ratified by the output (25:10-13) — no halt,
  no docket: THE TENT's form at a second seat, the installing act a deed instead of a sentence.
- A LAW'S INSTALLATION DATED BY THE SHELF, A SECOND SEAT (Sanhedrin 106a:10; the Jerusalem Talmud Sanhedrin 10:2:15; the Sifrei 131:2): "neither
  Ammonite wine nor gentile wine had been prohibited yet" at Shittim — the decree on gentile wine (Avodah Zarah 36b) is later than Peor: three
  shelves date one law after one event.
- THE RETELLING AS THE RULE'S PROOF (Avodah Zarah 4b:4-5; Berakhot 7a:13; Sanhedrin 105b:6): Micah 6:5 "know the righteous acts of the LORD" is
  read as the proof that God was not angry all Balaam's days — a prophet's retelling standing as evidence for the narrative's hidden parameter
  (the moment of anger), beside the ink's own back-reference at 31:16 for the counsel.
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

**AN INCLUSION AFTER AN INCLUSION COMES ONLY TO LIMIT (Vayikra, the
Lev 2 compile — sitting B of the audit, 2026-09-05).** Lev 2:1 writes
two adjunct clauses in parallel — "and he shall pour oil ON IT, and
put frankincense ON IT" — and the Sifra reads the oil as covering ALL
of the offering and the frankincense only PART of it, by a rule about
rules: שֶׁאֵין רִבּוּי אַחַר רִבּוּי בַּתּוֹרָה אֶלָּא לְמַעֵט ("an
inclusion after an inclusion in the Torah comes only to limit" —
Sifra, Vayikra Dibbura DeNedavah, Chapter 10 14-16, the row-grain
addresses). The same Sifra then records a SECOND, functional
derivation of the same verdict (Chapter 10 17: the oil blends and is
scooped with the flour, the frankincense neither) — the two routes to
one verdict recorded side by side, the parse rule and the mechanism.
The rule is the ribui-school's counterpart to the kelal-u-frat
family's limiting move: where the amplify-and-limit school reads two
inclusions in a row, the second narrows. Compiled at the adjunct
cells of cold_run_minchah.py; claim LV02-02 carries both derivations.

**THE PRECONDITION ON GENERAL-PARTICULAR-GENERAL (Behar, round 47).**
Whether plowing in the seventh year incurs lashes turns, the Talmud
says, on R. Avin's rule in R. Ila'i's name: "wherever a general is
stated in a POSITIVE command and a particular in a NEGATIVE, it is not
run as general-particular-general" — Lev 25:4's general ("a sabbath of
rest for the land," positive) and its particulars ("your field you
shall not sow," negative) fail the precondition, so plowing cannot be
derived by that middah and its lashes stay disputed (R. Yochanan and
R. Elazar, Babylonian Talmud Moed Katan 3a:12-16; the derivative
labors ruled rabbinic with the verse a mere support, 3a:9). A rule
about when a middah may run at all, stated on this book's own ink;
claim LV25A-19. Beside it the same page's WENT-OUT-TO-TEACH classifier
(3a:8) restates the Sifra's class rule, and the ABOLITION of the
pre-year addition is warranted by a verbal analogy "sabbath"-"sabbath"
from the creation week (4a:7) — with Rav Ashi's objection that an
analogy cannot uproot a received halakhah or a verse (4a:8), resolved
by keying the halakhah to the standing Temple (4a:9).

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
  SINCE O11 (opened 2026-09-08 and CLOSED 2026-09-09 — the backfill of
  the 2,813 unlabeled claims complete, 2,838 of 2,838 labeled;
  the record World/step9/CLAIM_LABELS.md, the gate
  logic/solo_tools/claim_labels_census.py) the field is MANDATORY on
  the manifest row and its leading code is one of: `ink` (the claim
  reads its own verse — the written form, a count, the received
  translation's rendering; the Masorah's notes and Onkelos are ink by
  nature), I1..I13 / E1..E32 (the twins by the claim's conclusion — a
  rule of conduct takes the I code), `plain` (a teacher's statement
  with no form the catalog names), `M-NN` (a catalogued compile move
  with no middah twin — logic/MOVE_CATALOG.md), `H` (an untaught
  transfer of our own, the link review's class); a parenthesized
  English note may follow the code and name a second form that rides
  beside the leading one. The gate refuses an empty label, an unknown
  code, and Hebrew letters in the note.
- **Step 6 (write the logic):** claims licensed by a middah keep the
  middah's own constraints as assertions (dayo cap, genus match,
  third-verse resolution). Where TIR and a middah overlap, the TIR
  rule cites the middah as chain authority.
- The book's worked example for I1 is the BAILEE ladder of Exodus 22
  (Bava Metzia 95a) — TOP10 block 4's own territory; first real
  workout for QAL_WACHOMER when block 4 opens.
