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
- THE INCLUSION READ WIDE, THEN FOUR EXCLUSIONS BY FOUR VERSES (Sifrei Bamidbar 132:1 on Numbers 26:53, THE NUMBERS WALK sitting 8, 2026-09-11): "to these shall
  the land be apportioned" — "I would understand that ALL are included: Israelites, priests, Levites, proselytes, women, bondsmen, the indeterminate, the
  hermaphrodite"; then each class is put out by its own verse — the priests by 18:20 ("in their land you shall not inherit"), the Levites by 18:24 ("in the midst
  of the children of Israel they shall not inherit"), proselytes and bondsmen by 26:55 ("by the names of the tribes of their fathers"), women and the rest by
  26:54 ("to a MAN according to his numbers"): the ribui-and-miut ladder (an inclusion and a limitation) run on four seats, and the ink carries the first two
  exclusions' reason in its own sentence — 26:62's two "for"s ("for they were not counted... for no inheritance was given them"). The women's exclusion is the
  premise the daughters of 27 plead against, and 26:33 is the roster's row for it.
- WHO "THESE" ARE — THE FOUR-WAY DISPUTE AS A PARAMETER ROW (Sifrei Bamidbar 132:1; Bava Batra 117a): R. Yoshiyah — the land was apportioned to THOSE WHO LEFT
  EGYPT ("by the names of the tribes of their fathers"; "to these" excludes minors); R. Yonatan — to THOSE WHO ENTERED ("to these"; "by the names of their
  fathers" teaches that God CHANGED THIS INHERITANCE from every other: "everywhere the living inherit the dead, here THE DEAD INHERIT THE LIVING"), with Rebbi's
  parable of the two priest-brothers at the granary (the portions pass UP to the dead fathers and are re-divided); R. Shimon b. Elazar — to THESE AND TO THESE,
  each man with his class, a man of both with both, "so that both verses are satisfied" (I13's form: two verses that pull apart, a third view that keeps both).
  In the engine: land_divided_among = left_egypt / entered / both — a data row, the dispute carried, no arm chosen.
- "ONLY" EXCLUDES THE TWO THE CENSUS EXCEPTS (Sifrei Bamidbar 132:3 on 26:55, E2 — the restrictor as a limitation): "ONLY by lot" — Joshua and Caleb took their
  portions "by the mouth of the LORD" (Joshua 15:13, 19:49-50; Judges 1:20), not by the lot; and 26:65's "except Caleb son of Jephunneh and Joshua son of Nun" —
  14:30's clause verbatim — names the same two: the land's restrictor and the roll's exception are one pair (the export's "Judges 15:13" is Joshua's; the head
  "26:25" is 26:55's — recorded).
- THE ESTIMATE — "BETWEEN MANY AND FEW" READ AS WORTH (Sifrei Bamidbar 132:4 on 26:56; Bava Batra 122a): the land was apportioned "by estimate" — a kor's-space
  of poor land against a seah's-space of good — so that "many and few" is a second axis (value) beside the count's (size): the shelf reads one clause on two
  axes, and the ink's "by the mouth of the lot" keeps the placing apart from the sizing (Joshua 19:50 giving the mouth its owner).
- THE LOT HAS A MOUTH (the ink's own phrase, 26:56, one seat; Onkelos keeps it; Bava Batra 122a's lot that "cries out" is the shelf's reading of it): "by the
  mouth of the lot shall his inheritance be divided" — a mouth given to the lot as to the LORD ("by the mouth of the LORD", 9:18-23): recorded as the ink's, the
  lore the exam's.
- THE IDENTITY ON A FREED TERM (Sifrei Bamidbar 142:2 on Numbers 28:2, THE NUMBERS WALK sitting 9, 2026-09-11; I2): "in its appointed time" stands at the tamid
  (28:2) and at the Pesach (9:2, 9:3) — the phrase's three Torah seats, computed; R. Yoshiyah: the tamid's "in its appointed time" is not needed for the tamid's
  own Sabbath (28:9 already gives the Sabbath its lambs), so the term is FREED (מופנה, "free") for the identity — as the tamid overrides the Sabbath, so the Pesach;
  R. Yonatan's objection ("in this sense we have not heard it") answered by the freeing argument itself; the English row drops the answering speaker (recorded).
  The rule of the freed term: an identity of expression teaches only when one of its two terms is redundant in its own verse — Pesachim 66a's Hillel the exam's seat.
- "TWO PER DAY" READ AS "OPPOSITE THE DAY" (Sifrei 142:3 on 28:3, ben Azzai): a phrase whose plain job is done by the next verse (28:4 gives the morning and the
  evening) is freed for a second content — the slaughter's place fixed by the sun's position; the two rows name different corners (recorded); Tamid 4:1 the exam.
- THE ONE SPECIFICATION GOVERNS EVERY UNQUALIFIED SEAT (Sifrei 142:5 on 28:5, I3 — the generalization from one case): "flour" is wheat because Exodus 29:2 says
  "wheat flour" once — "since flours are said in the Torah unqualified and Scripture specified at one of them, so every flour in the Torah is wheat"; the same form
  extends "beaten oil" from the meal offering to the lamp (Leviticus 24:2). The ink: "beaten oil" at the tamid's two seats alone, computed.
- THE LIKENING DISPUTED IN ITS SCOPE (Sifrei 143:1 on 28:6): "the continual burnt offering made at Mount Sinai" likens Sinai's olah to the tamid — the anonymous
  row for the libations, R. Yossi HaGelili only for "a pleasing aroma": a hekkesh (likening by juxtaposition in one verse) whose REACH is the dispute, the law agreed.
- "X ON ITS X" — THE DAY PASSED, THE OFFERING PASSED (Sifrei 144:2 on 28:10, 145:2 on 28:14): "the burnt offering of the Sabbath on its Sabbath" and "of the month
  in its month" (one seat each; their pair together at Isaiah 66:23, computed) read as limits — not the eve's on the day, not this day's on another: the possessive
  as a restrictor (E-class), the general rule "once its day passed, its offering is void" drawn from two seats; Berakhot 26a the exam's.
- OUT OF THE CLASS FOR A STRINGENCY, TWICE (Sifrei 144:1 on 28:9, 145:1 on 28:11; I10): the Sabbath and the new moon were both inside "the one lamb in the
  morning" and are each taken out for a stringency — the musaf; and the analogy "learn the new moon's number from the Sabbath's two" is REFUSED by the verse's
  "another number" (two bulls, a ram, seven lambs): the refused analogy the Sifrei's standing form (147:2 refuses "Sukkot's decline for Pesach" by "as these").
- THE COMMUNAL, NOT THE INDIVIDUAL (Sifrei 144:1): "the service overrides the Sabbath" proved from the Sabbath's musaf is limited by context — "in what does the
  passage speak? the communal" — the individual's offering does not override; the context rule (I12) closing an inference's reach.
- THE MINIMUM OF A PLURAL IS TWO (Sifrei 145:2 on 28:14): "for the months of the year" against the reading of "your months" as the plural's minimum, two — the
  counting rule the shelf applies to every bare plural; the ink's phrase two seats (Exodus 12:2 the calendar's first verse, computed).
- THE AVAILABILITY LADDER, FOUR TIMES FROM ONE LEVITICUS VERSE (Sifrei 147:1, 149:1, 150:1, 151:2 on 28:19, 28:27, 29:13, 29:36): "bulls found and no rams, rams
  and no lambs — offer what is found, even one; when all are found, the full number" — the "I might think... it is therefore written" ladder stated at every
  table of the calendar, the Hebrew's proof-text LEVITICUS 23:8 / 23:36 each time (the English rewrites it as the Numbers verse at two seats — recorded): the
  Sifrei on Numbers proving Numbers' tables from Leviticus — a cross-book TEACHER for the compile's edge 28-29 → Leviticus 23 (the link review law's reference
  class); Menachot 4:4 the exam's.
- THE IDENTITY "HOLY CONVOCATION" FOR THE FOOD-WORK (Sifrei 147:1 on 28:18; I2): the Hebrew derives the festival's food-preparation permission by identity with
  Exodus 12:16's "holy convocation" ("only what every soul must eat"); the English cites the verse without the middah (recorded). The ink: "laborious work" at
  the six festival days against "any work" at Yom Kippur, the Sabbath and Leviticus 23:31 — the permission written as a delta of two phrases, computed.
- THREE SOURCES, ONE LAW — THE WATER LIBATION (Sifrei 150:1 on 29:12-33; Taanit 2b): R. Akiva by induction from the seasons (the omer for the grain, the firstfruits
  for the trees, water for the rains), R. Yehudah ben Beteira by THE LETTER READ (the second day's "and their libations", the sixth's "and its libations", the
  seventh's "according to their ordinance" — mem, yod, mem, "water"; M-28 registered, the letters VERIFIED on the tokens of all fifteen verses), R. Nathan by the
  doubled verb "pour a pouring" (28:7; E10-class): a dispute on the SOURCE with the law agreed — the dual track carries the three, the compile holds the letters as a
  checked row and the law as the exam's (Sukkah 4:9). The English shortens R. Yehudah ben Beteira to "R. Yehudah" (recorded).
- THE WORD'S SENSE FROM ITS USE ELSEWHERE (Sifrei 151:1 on 29:35): "assembly" (עצרת, "withholding") read as CONFINEMENT from Jeremiah's "I am confined" (36:5)
  and "while he was still confined" (33:1) — the pilgrim withheld from leaving; and the first day the same by the shared "holy convocation" (an "it follows" on the
  common term). The ink: the word's three Torah seats — Sukkot's eighth day twice and Pesach's seventh (Deuteronomy 16:8), computed; Onkelos "a gathering".
- THE FRAME AS A CLOSER (Sifrei 152:1 on 29:39-30:1, R. Yishmael): "and Moses said to the children of Israel according to all that the LORD commanded Moses" (30:1)
  is read as PUNCTUATION — it closes the calendar so that 30:2's "and Moses spoke to the heads of the tribes" opens the vows and is not read with 29:39's "besides
  your vows": a structural rule about the ink's own paragraph boundaries — the "these" footer (29:39) and the receipt-frame (30:1) closing a register, the form the
  architecture measurement counted (ARCHITECTURE/DATABASE_SPECULATION.md section 4).
- BEN AZZAI'S NAME CENSUS (Sifrei 143:3 on 28:8): "with all the offerings in the Torah it is not written Elohim or El or Shaddai or Tzevaot but the Tetragrammaton
  alone — no opening for the heretics"; a claim about the whole Torah's offering-verses, checkable — in the two chapters "to the LORD" at every offering and Elohim
  never (computed); the compile's row for the whole Torah.
- THE EXAM DOCKET OF 28-29 (THE NUMBERS WALK sitting 9b, 2026-09-11; logic/oral_triage/num_28_29_musafim_exam_2026-09-11.md — 1,280 rows): the rules-about-rules
  the Babylonian Talmud states while running these verses, logged where the machinery runs:
  · A VERBAL ANALOGY PREFERS THE IDENTICAL FORM (Menachot 45b:18-20; I2): "they shall be" (Lev 23:20) is learned from "they shall be" (23:17), not from "there
    shall be" (23:18) — non-identical forms serve only where no identical term exists (the school of R. Yishmael's veshav / uva the counter-case); the
    preference order inside the second middah.
  · ONE AMPLIFICATION AFTER ANOTHER RESTRICTS (Menachot 89a:3; the amplification-and-restriction family): "with oil" twice at the thanks offering's loaves —
    a half-log, not more; the rule's seat beside the three log of the tamid's oil.
  · THE METHOD FORK NAMED AS A TANNAITIC DISPUTE (Sukkah 50b:5): Rebbi expounds by GENERALIZATIONS AND DETAILS (I4-I8's family), R. Yosei b. Yehuda by
    AMPLIFICATIONS AND RESTRICTIONS — the two rival engines on one verse (the sanctuary block's fork at its Sukkah seat).
  · JUXTAPOSITION YIELDS TO THE VERBAL ANALOGY WHEN BOTH STAND (Rosh Hashanah 34a:5): "if there were no verbal analogy I would have derived by juxtaposition;
    now that it is derived by the analogy the juxtaposition is not needed" — the same baraita changing its method; a precedence rule between I2 and the
    adjacency reading.
  · NO JUXTAPOSITION FROM A JUXTAPOSITION IN CONSECRATED MATTERS (Shevuot 10a:9, R. Yochanan): the festivals' goats are not learned each from its
    neighbour (Pesach's from the new moon's, Shavuot's from Pesach's) — every goat runs DIRECTLY to the first; the "and a goat" conjunction the device
    (Shevuot 9b:2, 10a:8), and Shavuot's and Yom Kippur's goats WITHOUT the conjunction (10a:11) — the token fact the runner computes off the ink (28:30, 29:11).
  · THE TWO BARS ON A BINYAN AV (Chagigah 6a:11, 6a:13): an INDIVIDUAL'S offering is not learned from the COMMUNAL (Shavuot's set), and a matter FOR ALL
    GENERATIONS is not learned from a ONE-TIME matter (the princes' dedication) — Beit Hillel and Beit Shammai each closing the other's analogy.
  · THE LAMED'S DOUBLE YIELD (Shevuot 9a:8-9): "a sin offering TO the LORD" (28:15) yields both Reish Lakish's "an atonement for My diminishing the moon" and
    "a sin the LORD alone knows" — "of the LORD" would serve the one, "for the LORD" the other: one preposition, two conclusions (the E-class on a particle).
  · THE FIXED-TIME ANALOGY (Shevuot 9a:10, the school of R. Yishmael): the new moon's goat and Yom Kippur's are both brought AT A FIXED TIME, so they atone
    alike — the period timers' own property as a middah's ground.
  · GRASPED MANY, GRASPED NOTHING (Rosh Hashanah 4b:15; Chagigah 17a:8): between two analogies (Shavuot to Pesach's seven or to Sukkot's eight) the SMALLER
    number is taken — seven is inside eight; the tie-breaker between rival identities.
  · THE COUNT'S UNIT IS THE SANCTIFICATION'S SPAN (Rosh Hashanah 5a:4; Chagigah 17b:7, Rabba b. Shmuel): count thirty days and sanctify the month with
    offerings — a day; count from Pesach and sanctify Shavuot — a week: the redress's length read off the counting unit.
  · THE FREED TERM AT ITS EXAM SEAT (Pesachim 66a:3-12): Hillel's "in its appointed time" / "in its appointed time" — the identity the Sifrei 142:2 stated
    (the entry above) run by the Talmud on the Pesach's override of the Sabbath, "more than two hundred" the year's count computable from the tables.
- THE VOWS' CHAPTER (THE NUMBERS WALK sitting 10, 2026-09-12; the Sifrei on Numbers 153-156 on 30:2-17; logic/oral_triage/num_30_vows_2026-09-12.md):
  the Sifrei's own case law read on the chapter's rows —
  · THE HEADS FIRST BY THE IDENTITY "BLOWING" (153:1): I2 on 10:3-4 supplies the princes' gathering-place; the one specified speech (30:2 "to the heads of
    the tribes") governs every unqualified speech (the I3 form); R. Yonatan finds the order at Exodus 34:31-32 and FREES the phrase — which then teaches
    "the release of vows is by experts alone": a rule the ink never states, the Sifrei's own addition on a freed term (the data channel, labeled).
  · "THIS IS THE THING" AS A LIMITER AGAINST TWO A-FORTIORI (153:2): the husband annuls, the sage permits — each inference would give the one the other's
    office; the formula refuses both (the verse refusing the inference, as at 145:1 and 147:2).
  · THE MINOR EXCLUDED, THE AGE FIXED BY THE IDENTITY WITH THE NAZIRITE (153:3, I2 "vow"-"vow" with 6:2): thirteen years and a day — the export's two
    files differing on the identity's content (the English carrying the Mishnah's distinct utterance, the Hebrew "a vow with a freewill offering").
  · "IN ANY EVENT" (מכל מקום, "in any case" — 153:3, 153:4, 154:1): a second clause read to strip a condition the first might carry — "to bind a bond, in
    any event" (no "to the LORD" needed); "in her husband's house, in any event" (even the forbidden marriage of a widow to a high priest).
  · A HINT, NOT A PROOF (זכר לדבר, "a remembrance for the matter" — 153:3): vows as by the king's life, oaths as by the King — "though there is no proof, a
    hint" from 2 Kings 2:2: the shelf grading its own evidence.
  · THE REFUSED A-FORTIORI OF R. ELIEZER (153:3, 153:10): annulling the wife's vows before she makes them — refused by "on his soul" and "which is upon
    her"; the sages' second ground the PARALLEL REACH of two verbs on one object (30:14): what can come to confirmation can come to annulment, what cannot,
    cannot.
  · TWO TRANSGRESSIONS ON ONE VOW (153:4): "he shall not profane" here and "you shall not delay" at Deuteronomy 23:22 — a cross-book count of the
    prohibitions one act breaks.
  · THE WOMAN LIKENED TO THE MAN BY ADJACENCY (153:4): "and a woman" following 30:3 — both transgress both (the E-class likening by juxtaposition).
  · THE AGE BY TWO EXCLUSIONS (153:4): "a woman" excludes the minor, "in her youth" excludes the mature — "how is this resolved?" the middle band, twelve
    years and a day.
  · THE CHAPTER GLOSSES ITSELF (153:4, 153:7, 153:9, 154:1): "a bond" is an oath from 30:11's "by an oath"; "restraint" is annulment from 30:9's adjacent
    pair; 30:7 is the betrothed because 30:11 has the married; "the utterance" is an oath by I2 with Leviticus 5:4's "to utter with the lips" (one seat).
  · THE THREE LIMITERS ON HEARING (153:5, 153:8, 154:2): the deaf excluded from "hear"; the report by others counted from the neighbor verse's "on the day
    of his hearing"; "to her" — he must intend her.
  · CONFIRMED FOR ONE HOUR, NEVER ANNULLED (153:5, 153:8, 154:2): the "how do I uphold both verses?" form resolving "shall stand" against "restrain" —
    the confirmation irreversible, the annulment's window the day.
  · THE ENGINE OF THE FOOTER (153:6, 153:7, 155:1, 156:3): the induction refused ("no — this may be true of the husband, who..."), the a-fortiori refused
    by a difference (the husband annuls in her maturity; the father's authority becomes exclusive), and THE LIKENING (hekkesh) OF 30:17 "you are compelled
    to liken" (על כרחך, "against your will") the father to the husband and the husband to the father — the chapter's rule-about-rules: where reasoning
    fails between two parties, the verse that names both decides; run at four rows.
  · "I REASONED AND REVERSED" (דנתי וחלפתי, "I judged and I exchanged" — 155:1): the Sifrei NAMES ITS OWN MOVE — the induction run both ways, the reversal
    refuted by "in her youth in her father's house", the first reasoning "merited" back, itself refuted, then the hekkesh.
  · THE FORGIVENESS A-FORTIORI AND ITS PARABLE (153:6): the vow annulled unknown to her and broken willfully needs forgiveness — all the more the standing
    vow; one who meant to eat swine and ate lamb.
  · THE MESSENGER DISPUTE (153:6, 154:3): R. Yoshiyah — "her father restrained her": his act, not her assurance, not a caretaker's; R. Yonatan — "in every
    place a man's messenger is as himself" (Kiddushin 41b): a general principle against a verse's restrictor, carried dual-track.
  · THE TWO SILENCES (154:2, 156:1): the single "was silent to her" the silence to confirm, the doubled "silent, silent ... from day to day" the silence
    to vex — two forms, two laws (the E10 class on a doubled verb).
  · THE DEADLINE'S TWO SETTINGS (156:1): "from day to day" — to nightfall by the verse's own close "on the day of his hearing", or twenty-four hours
    (R. Shimon ben Yochai reading the same words) — the dispute the compile carries as the annulment clock's parameter.
  · THE AFFLICTION FILTER (155:1): 30:14 restricts 30:9's "the vow upon her" to vows of self-affliction; 30:17 adds "between him and her"; R. Yoshiyah's
    common feature (vows no one else can release for her) against R. Yonatan's case-list (the fruits of the world; of the province; of this shopkeeper).
  · THE PART IS THE WHOLE ON A DOUBLED OBJECT (155:1): R. Akiva from "he shall confirm IT ... he shall annul IT" — as a part confirms the whole, a part
    annuls the whole; R. Yishmael: the annulment whole only; the bound — one vow ("figs and grapes") against two ("figs — and again grapes").
  · "AFTER HIS HEARING" FREED BY ITS NEIGHBOR (156:2): 30:15 already carries the hearing, so 30:16's "after his hearing" means after his confirmation.
  · THE MEASURE OF GOOD EXCEEDS THE MEASURE OF PUNISHMENT (156:2): the a-fortiori's standing ratio (the one who causes his fellow to stumble takes his
    place; all the more the one who brings him merit) — a recorded parameter of the tradition, not of the ink.
  · THE FATHER'S REACH BOUNDED BY "IN HER YOUTH IN HER FATHER'S HOUSE" (156:3): the restriction that keeps the two-way likening from reaching her maturity
    in his house; R. Yishmael — the betrothed maiden, her father and her husband annulling together.

- THE VOWS' DOCKET (THE NUMBERS WALK sitting 10b, 2026-09-12; logic/oral_triage/num_30_vows_exam_2026-09-12.md — 1,047 rows; the rules about rules the
  Talmud states while running chapter 30's clauses, read in Shevuot, Nedarim, Rosh Hashanah and Yoma):
  · THE METHOD FORK WITH ITS LINEAGES (Shevuot 26a:6-9): the oath of utterance's scope run by BOTH engines on one verse — R. Yishmael's school (the general
    and the particular) against R. Akiva's (amplification and restriction), each teacher's derivation traced to his master (R. Yishmael served R. Nechunya
    ben HaKanah who expounded the whole Torah by the general-and-particular; R. Akiva served Nachum of Gimzo who expounded it by amplification-and-restriction)
    — the middah choice a LINEAGE, recorded as a model parameter beside the verdicts (the fork's third seat after the sanctuary constants and the capital
    modes blocks).
  · "I WILL REVERSE IT" (Shevuot 26a:11): the Sifrei's reversed induction of 155:1 ("I reasoned and reversed") answered in the Talmud's own idiom — the
    a-fortiori's terms exchanged to test it, the exchange refuted by the verse's restrictor: the tradition's named test on an inference, at a second seat.
  · TWO VERSES AS ONE (Shevuot 26b:18): "for evil or for good" — the two clauses read as ONE verse for the oath's scope (the past and the future both in it);
    a clause pair counted as a single teaching unit — the E-class rule on what a "verse" is for a count.
  · THE PROFANE IS NOT LEARNED FROM THE SACRED (Shevuot 26b:20): the oath of utterance (a profane matter) cannot be learned from the oath of testimony's
    sacred setting — a bar on the analogy by the domain of its source; the vows' machine keeps its own verbs.
  · R. YOSHIYAH AND R. YONATAN ON THE CONJUNCTION (Shevuot 27a:15-16): "his father and his mother" — the vav read as AND (both together, R. Yoshiyah) or as
    OR (either, R. Yonatan) — the same pair that splits the messenger's annulment (Sifrei 153:6, 154:3): one dispute on a particle, two chapters' law.
  · THE IDENTICAL-FORM PREFERENCE (Yoma 76a:1; at 9b's docket for the calendar, here for the affliction-root): "afflict" at 30:14 learned from Leviticus
    23's "you shall afflict your souls" — the identity taken between two seats of the SAME form before any other.
  · GRASPED MANY, GRASPED NOTHING (Rosh Hashanah 4b:15): the delay ban's clock (Deuteronomy 23:22 by the vow_deadline row) — the three festivals, not the
    year; the tie-breaker as at 9b, here bounding a TIMER's period.
  · THE VERSE JUXTAPOSES ANNULMENT TO CONFIRMATION (Nedarim 87b:1-2): the same juxtaposition read by R. Akiva to carry "part of it" from the confirming verb
    to the annulling one, and by the Rabbis to keep each verb to its own act — a hekkesh (the likening; no I-code) argued in both directions on one pair of
    words (M-16's tenth exemplar in MOVE_CATALOG.md).
  · CONFIRMED FOR ONE HOUR, NEVER ANNULLED (Nedarim 69a-70a; the Sifrei 153:5): the state machine's irreversibility as the tradition's own rule — the
    machine's vow_confirmed status has no cancel; the dilemmas of 70a:4 (the "and I" after her naziriteship) UNRESOLVED and left so.
  · THE HEARING IS THE INK'S OWN TRIGGER (Nedarim 72b:3-73a:1, TEIKU): "on the day of his hearing" — whether he may annul without hearing left open on the
    page; the machine requires the hearing and records the open (the row hearing_required = unresolved).

- MIDIAN'S CHAPTER (THE NUMBERS WALK sitting 11, 2026-09-12; the Sifrei on Numbers 157-158 on 31:1-24 — no row from 31:25 to 35:8;
  logic/oral_triage/num_31_midian_2026-09-12.md): the Sifrei's own case law read on the chapter's rows —
  · THE NAME READ TWICE AND THE PRIORITY ASKED (157:1): "from the Midianites" — but Moab began (22:4, 22:7)? the old feud read off Genesis 36:35 and the
    parable of the two dogs; the gentilic's letters read as "contended" and "counseled" — the narrative middot's name-reading; the ink's own fact beside it:
    "the Midianites" with the article at the command (25:17) and the run (31:2) alone in the Bible.
  · "ARM" BY THE LEXICAL IDENTITY (157:2): the imperative's one seat fixed by Deuteronomy 3:18's "armed shall you pass over" — I2's lexical form (a word's
    sense from its other seat); "afterward you shall be gathered" read as the plain sequence: Moses' death contingent on the war.
  · THE DOUBLED NUMERAL DISPUTE (157:3): "a thousand to a tribe, a thousand to a tribe" — R. Yishmael reads the doubling twice (24,000), R. Akiva once (12,000,
    the ink of 31:5's own sum; the parser's distributive [1000, 1000]); "for ALL the tribes" the E-class amplifier — to include the tribe of Levi (the Hebrew;
    the English reversed); the passive "were delivered" read for its agent three ways (the men, others, conscription). The export's defects at this row
    (RESEARCH_LOG).
  · "THE HOLY" AND "HIS HAND" BY IDENTITY (157:4): the holy vessels = the ark from 4:20; "in his hand" = his domain from 21:26 and Genesis 24:10 — I2 on a
    common word at two seats; the ancestor by descent (the Hebrew's Joseph, the English's Jethro inserted).
  · THE SECOND NAMING, THE RETELLING FOR THE MODE, THE FRAME FOR A CAUSE (157:5): "the five kings" named again — as one in counsel, one in punishment (the
    "why repeated" form); Balaam's mode read off Joshua 13:22 (R. Natan: by a court — the Hebrew); "Moses and Eleazar went out" read for its cause (the
    youths snatching); "Moses was wroth" — the stigma hangs on the great; "by the word of Balaam" — the counsel spelled out.
  · THE REFUSED A-FORTIORI ON A PENALTY (157:6): "every woman who has known a man" — fit for intercourse, by the "uphold both verses" form on 31:18; the
    second "kill" read two ways: R. Yishmael — a repeated verb CLOSES THE SUBJECT (a structural rule: the paragraph's boundary); the other reading — the
    a-fortiori (the fit one killed, the one who has lain all the more) is barred, for WE DO NOT PUNISH BY INFERENCE (ain onshin min ha-din, the rule about
    rules at Sanhedrin 54a and Makkot 5b): the penalty must be written — the English drops it whole; R. Shimon ben Yochai's proselyte under three from "keep
    alive for yourselves".
  · THE TENT'S STRAW EXCLUDED, THE CAPTIVES LIKENED (157:7): 19:14's "all that is in the tent" — straw and twigs do not enter the category (piska 126's
    exclusion repeated); "you and your captives" — as you are children of the covenant, so your captives, for the sprinkling (an analogy on the pronoun pair).
  · THE FREED-WORD IDENTITY RUN TWO WAYS (157:8): Leviticus 11:32's "skin or sack" against 31:20's "garment, skin, goat-work, wood" — the a-fortiori refused
    both ways ("do we derive from the stringent to be lenient and stringent with it?"), "garment" declared FREED (mufneh — unneeded in its own verse) to form
    the gezerah shavah (the verbal identity): goat-work like sack carried to the creeping thing's law, "spun and woven" carried to the dead's — the band, the
    belt and the ass's girth in, cords and ropes out. The Hebrew's first leg runs backward (goat-work is 31:20's word); the English the way the ink allows.
    The identity's license: the freed word (MIDDOT.md under I2 — Pesachim 66a: no identity of one's own).
  · ANGER BEGETS ERROR AT THREE PLACES, AND "IN THE NAME OF ITS SAYER" (157:9): why Eleazar speaks the heifer's statute — Moses came to anger and to error
    (Leviticus 10:16, Numbers 20:10, 31:14 — R. Elazar; the wrath-verb with Moses as subject stands at Exodus 16:20, Leviticus 10:16, 31:14: two shared),
    or Moses gave him leave, or R. Yoshiyah's attribution rule from Esther 2:22 (the English drops the name) — rules about the lawgiver and the teacher.
  · "ONLY" DIVIDES, AND THE ANALOGY ON A SHARED FEATURE (158:1): the metals as vessels not lumps — Israel's dead and Midian's slain both defile, so both
    defile vessels only (the "you reason" form on a common feature); R. Yose HaGelili: the E-class limiter "only".
  · THE LISTS AS SPECIFICATION, THE IMMERSION BY A-FORTIORI (158:2): the vessels of fire and of water listed (the Sifrei's data channel — "because of the
    gentiles' absorptions"); if what needs no sprinkling needs immersion, what needs sprinkling all the more — I1; the English supplying the Mishnah's
    whitening / boiling.
  · THE TWO-WAY LIKENING OF THE CAMP AND THE EVENING (158:3): the sword unclean seven days from "slain by the sword" (19:16); vessels-man-vessels from the
    garments' washing; 31:24 and 19:19 likened BOTH WAYS (the camp's bar exported, the evening imported) — the likening (hekkesh, no I-code) as the vows'
    footer used it; the Hebrew's misquoted lemma and the English's wrong book (RESEARCH_LOG).

- MIDIAN'S DOCKET (THE NUMBERS WALK sitting 11b, 2026-09-12; logic/oral_triage/num_31_midian_exam_2026-09-12.md — 451 rows; the rules about rules the
  docket found at their Talmud seats):
  · THE FREE-WORD CONDITION OF THE VERBAL ANALOGY (Shabbat 64a:16-19): a verbal analogy (the second middah, I2) on FREE terms cannot be refuted; on terms
    free from ONE side only the Sages dispute whether it can — "garment and leather" freed on the creeping animal's side by Leviticus 22:4-5's
    juxtaposition to Leviticus 15:17 and on the corpse's side too (the priesthood docket's rows credited): the analogy between Leviticus 11:32 and
    Numbers 31:20 run BOTH WAYS (64a:7-8, 64a:15; Bava Kamma 25b:6) — the teacher of the edge midian -> shemini (link: transfer), the Sifrei 157:8's
    freed-word identity at its Talmud seat.
  · WE DO NOT PUNISH BY INFERENCE (Makkot 5b:11-16; Sanhedrin 54a:17): no penalty on an a-fortiori (I1's limit) — "you have taught us, our teacher, that
    one does not administer punishment based on an a-fortiori inference; the punishment must be stated" (the sister of both parents, Leviticus 20:17);
    nor a prohibition by inference (5b:14), nor lashes (the verbal analogy "wicked / wicked", Numbers 35:31 / Deuteronomy 25:2 — 5b:15), nor exile
    ("murderer / murderer", 35:21 / 35:11 — 5b:16); Abaye and Rava's fork on the father's brother (Sanhedrin 54a:17). The Sifrei 157:6's reading of
    31:17's doubled "kill" (R. Yoshiyah) at its seat, against R. Yishmael's structural "to close the subject" — the runner's DATA row punish_by_inference.
  · IN THE NAME OF ITS SAYER (Megillah 15a:20): whoever reports a saying in the name of its sayer brings redemption to the world (Esther 2:22) — the
    Sifrei 157:9's closing rule at its Talmud seat; the export dropped R. Yoshiyah's name at that very row (the reading's finding).
  · ANGER BEGETS ERROR (Pesachim 66b:6-9): the angry scholar's wisdom departs (Moses — 31:14 "and Moses was wroth", then 31:21's statute in Eleazar's
    mouth), the angry prophet's prophecy (Elisha, 2 Kings 3:14-15), whoever is angry is lowered (Eliab, 1 Samuel 17:28 / 16:7), the haughty too (Hillel,
    66b:6) — the Sifrei 157:9's three seats of Moses' anger at their Talmud seat; and ELEAZAR LOWERED FOR RULING BEFORE HIS TEACHER (Eruvin 63a:24 —
    "commanded to my father's brother, not to me"): the priest's relay read by the shelf as a fault, the installed_by class's own witness.
  · "NEVERTHELESS" DIVIDES, "AND IT SHALL BE PURE" ADDS (Avodah Zarah 75b:7-11): the particle אַךְ "only / nevertheless" at 31:23 EXCLUDES the third and
    seventh day's sprinkling for the vessels (Bar Kappara) — the Sifrei 158:1's move at its seat; "and it shall be pure" ADDS immersion in forty se'ah
    (Rava); both clauses needed (75b:10-11) — a particle read as an exclusion beside a clause read as an addition; "the water of niddah" split from the
    heifer's water to the menstruant's (75b:9) — the DATA row immersion_source.
  · THE NOVELTY THAT TEACHES NOTHING (Pesachim 44b:14-16): the Rabbis refuse to derive "the taste as the substance" from the vessels of Midian because
    their purging is itself a NOVELTY (a taste that taints, forbidden here alone) — a rule about sources: no principle is drawn from a chiddush (a
    novelty); R. Akiva derives from it (44b:13; Nazir 37b:1); R. Meir's detriment principle on the same verses (Avodah Zarah 67b:6).
  · ITS COUNTERPART REVEALS ABOUT IT (Avodah Zarah 76a:7-8): two mishnayot each stating part of a rule supply each other (Abaye, on the spit whitened
    here and purged for sacrificial meat at Zevachim 97a) — refused by Rava when each has only part; a rules-about-rules form on supplementing texts.
  · THE ONE-TIME LAW IS NO SOURCE (Menachot 77b:20): Midian's teruma "not one of ten, and not practiced for all generations" — no rate derived from it:
    the temporal scope of a verse as a bar on transfer (the daemon's installed_by class witnessed — the division's rates instruct this spoil alone).
  · ALL YOU TAKE ELSEWHERE SHALL BE LIKE THIS (Jerusalem Talmud Terumot 4:3:2): R. Levi reads 31:30's one of fifty as the terumah's AVERAGE — a rate
    carried from a one-time instruction to a standing measure (Mishnah Terumot 4:3's fiftieth); the Torah's own measure NONE (R. Mana, 4:3:8) — a
    TRANSFER taught, the reading's "one of fifty" on the local shelf after all.

  · FROM A NEGATIVE STATEMENT THE POSITIVE — R. MEIR'S REFUSAL (Nedarim 11a:2; Shevuot 36a:25-29; the Numbers walk 12b, 2026-09-12): R. Meir does not
    infer the unstated arm ("from a negative you may not infer the positive") — the corollary of his doubled-condition rule from Gad and Reuben's
    stipulation (Mishnah Kiddushin 3:4); its SCOPE disputed: monetary matters only, ritual matters inferred (36a:27), or nowhere — the sotah's
    "hinnaki" written and "chinnaki" read supplying the second arm (36a:29; Kiddushin 62a:2-3): a rule about inference with its own two settings.
  · THE DOUBLED FORM'S CENSUS ACROSS THE BOOKS (Kiddushin 61b:9-62a:7): the exemplar's kin read one by one — Cain's IF (Genesis 4:7), Eliezer's oath
    (24:41), the blessings and the curses (Leviticus 26:3 / 26:15), Isaiah 1:19-20, the sotah (Numbers 5:19), the heifer's third and seventh day (19:12):
    on R. Meir's view each teaches the doubling; on R. Chanina ben Gamliel's each second arm is needed for its own sake — a form read the same way at
    every seat, the two readings kept.
  · "ON CONDITION" IS "FROM NOW" (Gittin 75b:2 — Rav Huna in Rav's name): an act stated "on condition" takes effect at once, the condition fulfilled
    later — the grant of 32:33 given before the crossing, the exemplar's own timing; a rule about the reach of a clause in time.
  · A CONDITION COUNTER TO THE TORAH (Mishnah Bava Metzia 94a:2; R. Yehuda 94a:5): void on a non-monetary matter; in monetary matters the parties may
    agree — the reach of stipulation against the written law, the bailees' case.
  · THE ONE-TIME LAW, AGAIN — THE EXODUS GENERATION'S TITLE (Bava Batra 119b:3-4, credited): Exodus 6:8's "heritage" read both ways — an inheritance
    from the fathers AND a generation that bequeaths without inheriting, "You will bring THEM in" (Exodus 15:17) — the scope of a promise read on its
    own grammar; the shelf's frame for chapter 32's oath retold.
- THE JOURNEYS' DOCKET (THE NUMBERS WALK sitting 13b, 2026-09-12; logic/oral_triage/num_33_journeys_exam_2026-09-12.md — 196 rows; the rules about rules the
  docket carries, each at its row):
  · THE VERBAL ANALOGY AT A DATE — "THE FORTIETH YEAR" / "THE FORTIETH YEAR" (Rosh Hashanah 2b:10-11; I2, the gezerah shavah — the shared word): 33:38's
    date names its epoch ("of the going out from the land of Egypt"), Deuteronomy 1:3's does not; the tradition carries the epoch across by the shared
    phrase in Rav Pappa's form ("the twentieth year" / "the twentieth year") — a TRANSFER with its teacher named; the engine's Calendar reads both dates
    in one year by its own registered epoch, so the transfer is reproduced without being assumed.
  · TWO VERSES THAT COME AS ONE TEACH NO PRECEDENT (Kiddushin 37b:6-9 — the king's "when you come … and inherit and settle" and the first fruits' the same
    form; a rule about rules, no I-code among the thirteen): when the Torah states a qualification at two seats, the pair does not generalize to a third
    — the two schools of R. Yishmael split on whether the pair was necessary (each seat needed for its own sake) or superfluous (and so teaching).
  · THE FOUR SENSES OF "KI" AND "DO NOT READ" (Rosh Hashanah 3a:2 — Reish Lakish's four: if, perhaps, but, because; R. Abbahu's "do not read 'and they
    saw' but 'and they were seen'"): a lexical rule and a vocalization rule read together on 20:29 to place the clouds' departure at Aaron's death — the
    ground of the chukat runner's row arad_heard.
  · THE HEH FOR THE LAMED (Yevamot 13b:6 — R. Nechemya and the school of R. Yishmael: a word needing a lamed at its head takes a heh at its end — Elimah,
    Mitzraimah, Diblathaimah): a grammar rule of the ink, its examples the itinerary's own tokens (33:9, 33:46); the list keeps the ending.
  · A DATE COMPUTED BACKWARD FROM A RUN'S MARKER (Kiddushin 38a:5-6; Seder Olam Rabbah 10:2): Moses' death on the seventh of Adar from the tenth of Nisan
    (Joshua 4:19) less thirty days' mourning and three days' preparation — the shelf's own retrograde marker (Pesachim 6b:7's kin), with "this day"
    (Deuteronomy 31:2) closing the count to the day (38a:7; Exodus 23:26 "the number of your days I will fill").
  · THE RETREAT (Seder Olam Rabbah 9:2 — M-30): two seats of one death reconciled by a movement the ink does not narrate, the list's own count the check.
  · THE PRIVATE ALTAR'S ERAS DECIDE A SENSE (Mishnah Zevachim 14:4-8): "high places" in the Mishnah are Israel's own altars by era — permitted, forbidden,
    permitted, forbidden, forbidden forever; 33:52's "their high places" the Canaanites' to demolish (Leviticus 26:30's curse in the same verb): one word,
    two objects, the docket's topic rows read to tell them apart and the gemara cut as another runner's.
- THE BORDERS' DOCKET (THE NUMBERS WALK sitting 14b, 2026-09-13; logic/oral_triage/num_34_borders_exam_2026-09-13.md — 171 rows; the rules about rules the
  docket carries, each at its row):
  · THE ADJACENT VERSE CLASSES THE COMMANDMENTS (Kiddushin 37a:4-6 — the baraita on Deuteronomy 12:1-2; the adjacency rule, the case law's own family):
    "in the land" would confine every commandment, "all the days that you live upon the earth" would extend every one — "go and learn from what is stated
    in the next verse": the idolatry's ban is an obligation of the body and applies everywhere, so every obligation of the body applies everywhere and
    every obligation of the land inside the border alone (Rav Yehuda's classing, 37a:3); the exceptions by tradition (orlah and diverse kinds, 37a:1),
    the new crop disputed (37a:7-15 — R. Eliezer's "even" read two ways, decided by Abaye's "who disagrees with R. Eliezer? R. Yishmael"). The chapter's
    border is the rule's OBJECT; the classing is Deuteronomy's and the readback's.
  · "ONLY" EXCLUDES THE TWO WHO DIVIDE (Bava Batra 122a:12 on 26:55, read whole at this docket; E2 — the restrictor as a limitation): "ONLY by lot" — Joshua
    and Caleb took not by the lot they administer but by the LORD's word (Timnath-serah, Joshua 19:50) and by Moses' oath (Hebron, Joshua 14:13); the
    two dividers of 34:17 and 34:19 the two the restrictor excepts — the exclusion read against its own administrators.
  · THE LAW OF AGENCY ASKED OF A VERSE AND REFUSED (Kiddushin 42a:6-8 on 34:18): Rav Giddel in Rav's name founds agency on "one prince from each tribe you
    shall take to divide the land" — refused, "how can you understand this as agency? minors have no agency, and the princes divided for adults and
    minors alike"; the verse kept for another rule (the court's steward for orphans, "to their disadvantage and to their benefit"): a derivation tested
    against a case it cannot cover and re-seated — the form of a refused source.
  · A VERBAL ANALOGY NOT RECEIVED IS NOT USED (Sanhedrin 16a:7-9): the false prophet before the seventy-one by "presumptuously" / "presumptuously" (Deuteronomy
    18:20; 17:12) — but the elder's presumptuousness is a death penalty by twenty-three; Reish Lakish's "word" / "word" (17:10; 18:20) instead; and why
    not return the elder to seventy-one by the first analogy? "this tanna derives by 'word' / 'word' and not by 'presumptuously' / 'presumptuously', as he
    did not receive it as a tradition" — I2's own constraint (Pesachim 66a: no verbal analogy of one's own) stated inside a sugya on the courts.
  · ONE WORD READ TWO WAYS ON A BORDER (Gittin 8a:4-7 on 34:6): "and its border" — R. Yehuda: the sea itself directly across the land is the land; the
    Rabbis: the word teaches the islands within a string from Turei Amnon to the River of Egypt (the Tosefta Terumot 2:12's picture) — the same word
    the ground of both arms, each side's reading stated with what the other does with the word ("and the Rabbis, what do they do with 'and its
    border'?").
  · ONE BORDER ROUND ABOUT AGAINST THE JORDAN CANAAN'S (Bekhorot 55a:10 on 34:12; 55a:14 on 34:15): the tithe's flocks on both banks — "this shall be your
    land by its borders round about" makes the land one border with the tribes' demarcations inside it; R. Shimon ben Yochai reads "beyond the Jordan
    AT JERICHO" — as Jericho is Canaan's, the river is Canaan's: the inclusio's closer and the "at Jericho" pair each carried as a rule.
  · THE LOTTERY'S TWO RECEPTACLES (Bava Batra 122a:3-6, credited, read whole here): "only by lot" (26:55) and "by the mouth of the lot" (26:56) reconciled by
    the picture — Eleazar with the Urim, Joshua and all Israel before him, the tribes' names in one receptacle and the twelve regions' boundaries in the
    other, the lot of each confirming the Urim's word: two verses' instruments made one procedure; the dividers of 34:17 the procedure's persons.
  · A LIKENESS REFUSED BY WHAT THE FIRST CASE NEEDED (Sanhedrin 16a:2-3): Ulla's "as the beginning was by seventy-one, so a border dispute" — refused
    because the beginning also needed the lots, the Urim and all Israel present, which a later dispute does not: a likeness tested against every
    feature of its exemplar, not the one feature named.
  · WE DO NOT PUNISH BY INFERENCE, A SECOND INSTANCE (Sifrei Bamidbar 160:3 on 35:16): "if the stone and the wood make him liable, iron the more —
    except that one does not punish from an inference; therefore 'iron' is written": the a-fortiori (I1) refused on a penalty, the verse supplying what
    the inference may not — sitting 11's rule (157:6) at a second seat; the export's English drops the sentence both times.
  · THE INDUCTION FROM THREE FATHERS AND ITS LIMIT (Sifrei Bamidbar 160:5 Hebrew, 160:6 on 35:16-20): "stone is not like wood, wood not like stone,
    neither like iron, iron not like the two — the common feature: it can kill, and if he killed, the commandment is in the avenger's hand — so
    anything that can kill" (the building-block prototype from three verses, I3's form); and the same induction used to EXCLUDE — pushed into water
    or fire, a dog or a snake set on him: the three kill by the killing things themselves, so the indirect killing is not in the class, "his judgment
    is given to Heaven" — the heaven entry's own case; the English carries the induction one row down from the Hebrew.
  · THE JUXTAPOSITION THAT DISQUALIFIES, CARRIED BY A LIKENESS AND AN A-FORTIORI (Sifrei Bamidbar 160:8 on 35:23-24): "he was not his enemy" beside "the
    congregation shall judge" — haters unfit to judge (I12, the adjacent clause); kin from "between the smiter and the avenger"; and witnesses by the
    likeness of the two "kill by" clauses (kill by judges, kill by witnesses) and by I1 — judges do not decide the facts and are unfit, witnesses decide
    them, all the more.
  · THE COURT'S NUMBER FROM THE TOKENS (Sifrei Bamidbar 160:8 on 35:24-25): "the congregation shall judge", "the congregation shall deliver" — ten and
    ten (Numbers 14:27's ten spies the congregation, the exam's Sanhedrin 2a); and three more from Exodus 23:2's inclining, "as witnesses are two, so
    the judges, and a court is not even — add one": twenty-three; the Hebrew's number, the English's "thirty" a defect.
  · THE PROTOTYPE "WITNESS MEANS TWO" (Sifrei Bamidbar 161:1 on 35:30): "and one witness — this builds a father: wherever 'witness' is written, two are
    meant, unless Scripture specifies 'one'" (I3 from the specified case to the bare word); the ink's bare plural "witnesses" at 35:30 the seat.
  · THE RANSOM REFUSED BY A CONTRAST OF HANDS (Sifrei Bamidbar 161:1 on 35:31): Exodus 21:30's ransom is for a death at Heaven's hand (the ox's owner);
    "I might think the same for a death by man's hand — 'you shall not take ransom'": the verse read against its kin, the kin's setting named.
  · THE NOTARIKON ON A VERB (Sifrei Bamidbar 161:3 on 35:33): "for the blood, it pollutes (יַחֲנִיף) the land" — R. Yoshiyah splits the verb into two words,
    "it rests wrath (יחון אף) on the land": E30 (the word read as an abbreviation of two) on a verb of the ink — the exemplar beside the compile
    debt's noun (MIDDOT's sitting L4b entry).
  · THE A-FORTIORI ACROSS THE TWO MEASURES (Sifrei Bamidbar 160:10 on 35:26): R. Elazar ben Azariah — "if under the lesser measure, punishment, one step
    beyond the border forfeits the soul, how much more under the greater measure, reward": I1 with the tradition's own premise that the measure of good
    exceeds the measure of punishment (the exam's Sanhedrin 100b), the doubled infinitive "going out he goes out" the seat.
  · THE STEM READ (Sifrei Bamidbar 161:5 on 35:34): Deuteronomy 30:3 "the LORD will RETURN (וְשָׁב) with your captivity" — "'and he will bring back' is not
    written but 'and he will return'": the simple stem against the causative (the ink's form the simple, computed), the Presence read as one of the
    returning captives; the grammar of the stem as the ground of a reading (M-27's kin — the form decides).
  · THE TWO-WAY UNCERTAINTY (Sifrei Bamidbar 160:8 on 35:23): Issi ben Akiva on "without seeing ... not his enemy" — "his stringency is his leniency and
    his leniency his stringency: you cannot make him liable to death — perhaps unwitting; you cannot make him liable to exile — perhaps wilful": a
    case that no verdict reaches from the facts, carried as a row with neither (the TEIKU shape without the word).
  · THE TIMING READ FROM THE CONTEXT (Sifrei Bamidbar 159:1 on 35:10-11): "you shall appoint cities" — after inheritance and settlement, not at the entry,
    by Deuteronomy 19:1's "when the LORD your God cuts off the nations" (the refuge chapter's own opening; the English cites 12:29, the clause's other
    seat): I12, the adjacent law's timing clause read into this one; and the Jordan's status a dispute of two readings of one phrase (R. Yonatan: not
    of Canaan; R. Shimon ben Yochai: as Jericho, so the Jordan — 36:13).
- THE REFUGE CITIES' DOCKET (THE NUMBERS WALK sitting 15b, 2026-09-13; logic/oral_triage/num_35_refuge_cities_exam_2026-09-13.md — 666 rows; the rules about
  rules the docket carries, each at its row):
  · A CHAIN OF VERBAL ANALOGIES WITH ONE END IN THIS CHAPTER (Eruvin 51a:8 — Rav Chisda; the Sabbath block's own row, credited here): place (Exodus 16:29) /
    place (21:13) / flee (21:13) / flee (35:26) / border (35:26) / border (35:27) / outside (35:27) / OUTSIDE (35:5 — "you shall measure from outside the city
    two thousand cubits"): eight links, each pair a shared token, the Sabbath limit's measure fetched from the Levite city's; and 51a:9's refusal of the
    ninth — "outside" from "outside", not from "outward" (35:4's thousand): a chain is only as long as its exact tokens.
  · TEN AND TEN AND THREE — A COUNT BUILT FROM TWO TOKENS AND A THIRD VERSE (Sanhedrin 2a:14-2b:1; Mishnah Sanhedrin 1:6; the Sifrei 160:8): "the
    congregation shall judge" (35:24) and "the congregation shall deliver" (35:25) — a congregation is ten (14:27's ten spies); a majority of two to convict
    ("after the many to incline", Exodus 23:2, read with 23:2's "do not follow the many for evil") and one so the court is odd: twenty-three. The exemplar of
    the count of mentions joined to an arithmetic rule: the Sifrei states the sum, the Mishnah its parts, the Gemara the third verse.
  · WHERE A MEASURE IS WRITTEN AND WHERE IT IS NOT (Sanhedrin 76b:12-13 on 35:16-18): "in hand … whereby he may die" at the stone and the wood, absent at the
    iron — Shmuel: iron of any size kills; Rebbi's baraita: "revealed and known before Him who spoke and the world came to be … therefore the Torah gave it
    no measure"; the Gemara's edge: only when he stabbed. THE SILENCE READ AS A RULE, and bounded — the omitted clause teaches by its absence, but only as far
    as the reason for the absence reaches.
  · THE INDUCTION FROM THREE (the Sifrei 160:3-5; the binyan av): the stone, the wood, the iron — "what is common to the three: they can kill" — extended to
    every instrument that can kill; its limit stated in the same breath: the water, the fire, the snake, whose judgment is Heaven's. A father built from
    three verses names the feature it carries and the class it leaves.
  · A RESTRICTION AFTER A RESTRICTION AMPLIFIES (Makkot 9b:5-8; Bava Kamma 86b:17-19): "without seeing" (35:23) and "without knowledge" (Deuteronomy 19:4) —
    R. Yehuda reads the first as excluding the blind; R. Meir reads the two together as amplifying and includes him. The rule's exemplar at a case whose
    two arms are both on the shelf (the DATA row the_blind_killer).
  · TWO VERSES THAT COME AS ONE TEACH NOTHING (Sanhedrin 45b:12): the murderer ("the avenger of blood shall put him to death", 35:19-21) and the avenger —
    no principle of "the one obligated in the deed's first stage completes it" is drawn from their pair; and the court appoints an avenger where there is
    none ("when he meets him", 45b:13). The constraint on generalization stated inside the chapter's own two rows.
  · "THE TORAH SPOKE IN THE LANGUAGE OF MEN" ON A DOUBLED INFINITIVE (Makkot 12a:13-15 on 35:26 "if going out he goes out"): the doubled verb read as
    deliberate-or-unwitting exit by one baraita, refused by Abaye for the other — the end is not severer than the beginning; the same mark (Genesis 27:30's
    twin) that teaches elsewhere teaches nothing here because the rule it would yield contradicts the law's shape.
  · WE DO NOT PUNISH BY INFERENCE — A THIRD SEAT (Makkot 5b:15-16; the Sifrei 157:6 and 160:3): the lashed excluded by "wicked" / "wicked" (35:31; Deuteronomy
    25:2) and the exiled by "murderer" / "murderer" (35:21; 35:11) from an a fortiori's reach — the analogies stand in for the inference the rule refuses;
    the chapter's two halves joined by its one root at the rule's own seat.
  · THE COUNT OF MENTIONS (Makkot 11a:12; Mishnah Makkot 2:6): "the death of the high priest" three times — 35:25, 35:28 twice — the three high priests
    whose deaths return the exile (the anointed, the many-garmented, the relieved); R. Yehuda's fourth from 35:32's bare "the priest". A count of a phrase's
    seats read as a count of the law's subjects, the fourth from a variant form.
  · THE PLURAL'S MINIMUM IS TWO UNLESS "ONE" IS WRITTEN (the Sifrei 161:1 on 35:30; Sanhedrin 33b:15): "by the mouth of witnesses" — two by the prototype;
    "one witness shall not testify against a soul to die" — and R. Yosei son of R. Yehuda's "to die": not to convict, but he may answer to acquit. The
    prototype rule for a bare plural stated at its seat, the exception cut by the verse's own last word.
  · THE OFFICE THAT SHOULD HAVE PLEADED (Makkot 11a:14; 11b:11 — Rava): why does the high priest's death release the exile? the high priests should have
    pleaded for mercy that no one kill unwittingly in their days, and did not; the second high priest — he should have pleaded for the verdict. A reason
    supplied for a term the ink states without one; the reason then decides the cases the ink does not (the priest appointed after the verdict).
  · HEAVEN'S DEATH IS COMMUTED, MAN'S NEVER (Ketubot 37b:12 — R. Yishmael son of R. Yochanan ben Beroka): "you shall take no ransom for the life of a
    murderer" (35:31) against the ox's owner's ransom (Exodus 21:30) — those executed at Heaven's hand give money and are atoned; those the court executes,
    never ("dedicated of men shall not be redeemed", Leviticus 27:29). Two seats reconciled by the agent of the death, not by the deed.
  · THE HEIFER YIELDS TO THE FOUND KILLER (Mishnah Sotah 9:7; Sotah 47b:2; Ketubot 37b:6): the heifer broken and then the murderer found — he is executed:
    "except by the blood of him who shed it" (35:33); a procedure completed does not spend the atonement the verse assigns to the shedder's blood.
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
