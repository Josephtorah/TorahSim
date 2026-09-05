# FUNCTION CATALOG — one card per compiled span

Fourteen files in `World/step9/` compile law spans cold from the ink and
grade themselves against Mishnah rows. Every card below was built from
the file's own header and from its printed output on 2026-09-05, when
all of them were rerun read-only for this catalog. Verse numbering is
the Hebrew numbering the word database uses (so the guardians are
Exodus 22:6-14, and the theft clauses are 22:2-3).

**Card fields.** Span and opener: the verses and the word in the ink that
opens the case. Functions: what the file compiles, each with its answer
sheet. Score: the printed matrix line. Provenance: how many cells come
from ink, from a named recorded move, from data, from routing or import.
Effects: the registry effects the source names, and the ledger operations
the run writes. Imports: what the span reaches for outside itself.
Moves: the catalog moves the file's labels name.

**Provenance vocabulary.** INK: read from the span's own tokens. MOVE or
RECORDED: a recorded argument replayed with its source row. DATA: a
transmitted quantity the ink leaves unstated. FENCE: a rabbinic boundary
the answer sheet itself labels. ROUTED: an input class filed onto an
existing branch as the answer sheet files it. IMPORT: a rule from another
span or book.

Totals across the fourteen: 59 compiled functions, 294 graded cells, all
matching on the latest run.

---

## Exodus

### 1. cold_run_guardians.py — the four guardians

- **Span and opener.** Exodus 22:6-14. Three paragraphs opened by
  verse-initial כִּי ("when"): כִּי יִתֵּן ("when [a man] gives", 22:6 and
  22:9) and כִּי יִשְׁאַל ("when [a man] borrows", 22:13). The medial senses
  of the same word (the Gittin 90a dictionary) are excluded by position.
- **Function.** One liability matrix: four roles (unpaid keeper, paid
  keeper, renter, borrower) by three event classes (accidents, loss,
  theft). Answer sheet: Mishnah Shevuot 8:1, with Bava Metzia 7:8 for the
  renter.
- **Score.** 12/12 cells match the Mishnah's table.
- **Provenance.** INK 6 (22:7, 22:8 twice, 22:9-10, 22:11, 22:13), moves
  3 (the a-fortiori at Bava Metzia 94b:15 for the paid keeper's loss; the
  comparison at 94b:19 with the benefit seal at 94b:10 for the borrower's
  loss and theft), routed 3 (the renter, on the hire-clause hook of 22:14,
  as Mishnah Bava Metzia 7:8 routes it, Rabbi Yehuda's arm).
- **Effects.** oath_imposed, pays. Ledger ops: debit x7, status x5.
- **Imports.** None. The hidden paid/unpaid parameter is recovered by the
  diff (Bava Metzia 94b:8-9), not imported.
- **Moves.** M-01 the diff, M-02 the a-fortiori, M-03 the comparison,
  M-04 the routing, M-09 the keyword dictionary.
- **Engine.** Wrapped as `law_guardians` with the matrix as a table.

### 2. cold_run_mishpatim.py — the ordinances, pass one

- **Span and opener.** Exodus 21:2-22:3, five case blocks each opened by
  verse-initial כִּי: כִּי תִקְנֶה ("when you acquire", 21:2), כִּי יִגַּח
  ("when [an ox] gores", 21:28), כִּי יִגְנֹב ("when [a man] steals",
  21:37), and the damages openers of 21:33-22:5.
- **Functions and scores.**
  | Function | Answer sheet | Cells |
  |---|---|---|
  | slave-release: by years (the timer), by deduction, by jubilee | Mishnah Kiddushin 1:2 | 3/3 |
  | four-damages class map: ox, pit, grazing, fire; common output "from the best" | Mishnah Bava Kamma 1:1 | 5/5 |
  | goring-ox state machine: half from the body, full, the threshold, the reversal, the human victim, the slave victim | Mishnah Bava Kamma 1:4 and 2:4 | 6/6 |
  | injury indemnities: medical, livelihood, damage, pain, humiliation | Mishnah Bava Kamma 8:1 | 5/5 |
  | theft multiples: double, fivefold ox, fourfold sheep, the restricted scope | Mishnah Bava Kamma 7:1 | 4/4 |
- **Score.** MISHPATIM PASS: 23/23 cells across 5 functions.
- **Provenance.** INK 15, RECORDED 5, ROUTED/IMPORT 3.
- **Effects.** forewarned, gives_fixed_sum, goes_free, jubilee_release,
  pays, pays_double, pays_four_five, ransom_imposed, stoned, substitution,
  term_clock. Ledger ops: body x1, debit x14, status x5, timer x2.
- **Imports.** The damage cell of the injury function is not computed
  here: it CALLS `cold_run_lev24.talion()` and resolves through Leviticus
  24:18-22 (Bava Kamma 83b:10, 84a:1; move M-07 exemplar c, executed).
  Jubilee release imports Leviticus 25 (Kiddushin 15a:19: written even
  for the pierced "forever"). Humiliation imports Deuteronomy 25:11-12,
  the recorded source in the sugya.
- **Moves.** M-05 the threshold-parse (three gorings from "yesterday and
  the day before", Bava Kamma 23b:17-18), M-07 the cross-module import,
  M-04 the routing.
- **Engine.** Slave release and the goring ox are wrapped as
  `law_slave_term` and `law_goring_ox`.

### 3. cold_run_mishpatim_2.py — the ordinances, pass two

- **Span and opener.** Exodus 21:22 (כִי יִנָּצוּ, "when men strive"),
  21:26-27 (the struck slave's eye and tooth), 22:15-16 (כִי יְפַתֶּה, "when
  [a man] seduces").
- **Functions and scores.**
  | Function | Answer sheet | Cells |
  |---|---|---|
  | the seducer's fine: a fine exists and goes to the father; the amount is a pointer, not a number; the payments table | Mishnah Ketubot 3:4 | 3/3 |
  | the freed slave's limbs: eye, tooth, the class of limb-tips that do not regenerate | Kiddushin 24a with Mishnah Negaim 6:7 | 3/3 |
  | the miscarriage valuation: through the judges; the before-and-after algorithm; a person pays, an ox is exempt | Mishnah Bava Kamma 5:4 | 3/3 |
- **Score.** PASS 2: 9/9. Running total with pass one and the guardians:
  44/44.
- **Provenance.** INK 5, RECORDED 1, ROUTED/IMPORT 3.
- **Effects.** exempt, fined_by_assessment, gives_fixed_sum, goes_free,
  pays, released. Ledger ops: debit x3, status x5.
- **Imports.** The fifty-shekel amount is fetched from Deuteronomy 22:29
  through the ink's own pointer "like the dowry of the virgins" (22:16).
- **Moves.** M-10 the pointer-fetch, M-06 the generalization (the
  limb-tip class), M-04 the routing.

### 4. cold_run_decalogue.py — the Decalogue's law layer

- **Span and opener.** Exodus 20: the utterances that carry case law in
  their own ink, the vain Name, the Sabbath clauses, the theft
  commandment, and the altar rules at the chapter's tail (20:22-23 in this
  database's numbering). Openers are the imperatives, זָכוֹר ("remember",
  20:8) and לֹא ("you shall not").
- **Functions.** vain_name, sabbath_clauses, theft_commandment,
  altar_rules. Answer sheets: Mishnah Shevuot 3:10-11, Sanhedrin 11:1,
  Middot 3:4, with Shabbat 120b and 153b, Zevachim 54a, Sanhedrin 7b.
- **Score.** MATRIX: 12/12 cells match the answer sheet.
- **Provenance.** Pure ink 1/12 (8%), named moves 11/12 (92%). The
  lowest ink fraction of any span: the Decalogue states duties, and the
  case law that grades them lives in the tradition's readings.
- **Effects.** disqualified, labor_barred, lashes, put_to_death,
  rest_required, sanctify_day. Ledger ops: block x3, body x3, heaven x1,
  timer x1.
- **Imports and routing.** Money theft and the person-to-person capital
  laws are routed to the ordinances span, where their code lives. Mishnah
  Sanhedrin 11:1 reads the Decalogue's theft as theft of persons.
- **Moves.** M-04 the routing, M-09 the keyword dictionary.

### 5. cold_run_calendar.py — the festival calendar

- **Span and opener.** Exodus 23:10-19, the code's clock chapter: שֵׁשׁ
  שָׁנִים ("six years", 23:10), שֵׁשֶׁת יָמִים ("six days", 23:12), שָׁלֹשׁ
  רְגָלִים ("three times", 23:14).
- **Functions.** sabbatical (the seventh-year land timer), weekly_rest,
  pilgrimage (the three appearings and who owes them), offering_windows,
  first_fruits, kid_in_milk. Answer sheets: Mishnah Sheviit's frame,
  Chagigah 1:1, Pesachim 5:4, Bikkurim 1:3, Chullin 8:4; Sukkah 44b,
  Yevamot 48b, Pesachim 59b.
- **Score.** MATRIX: 14/14 cells match the answer sheet.
- **Provenance.** Pure ink 4/14 (29%), named moves 9/14 (64%), data
  1/14 (7%).
- **Effects.** appearance_owed, barred_from_it, disqualified, exempt,
  land_release, rest_required, restores. Ledger ops: block x6, heaven x1,
  status x3, timer x3, transfer x1. The first timer on a LAND entity, and
  the appearance duty on Heaven's docket.
- **Imports.** The kid-in-milk clause is a census across its three seats,
  the third being Deuteronomy 14:21; the three-fold reading (cooking,
  eating, benefit) follows Mishnah Chullin 8:4.
- **Moves.** M-08 the exemplar-generalization, M-12 the
  grammatical-number hook.

### 6. cold_run_pesach.py — the Passover engine

- **Span and opener.** Exodus 12-13: הַחֹדֶשׁ הַזֶּה ("this month", 12:2),
  זֹאת חֻקַּת הַפָּסַח ("this is the ordinance of the Passover", 12:43),
  קַדֶּשׁ ("sanctify", 13:2). The first span compiled after the effects law.
- **Functions.**
  | Function | What it decides | Answer sheets |
  |---|---|---|
  | leaven_machine | eating in the window (karet), the purge deadline (midday of the 14th), the window's bounds, leaven after Passover | Mishnah Keritot 1:1, Pesachim 1:4, 2:2; Pesachim 5a |
  | paschal_procedure | eating time (night, until midnight), preparation (roast only), leftover (burn on the 16th), the bone, the disqualified lamb | Mishnah Zevachim 5:8, Pesachim 7:10-11, 5:2 |
  | access_filter | the apostate stranger, the sojourner and hireling, the uncircumcised, the bought slave, the father with uncircumcised sons, the convert | Mishnah Pesachim 5:3; Yevamot 71a; the Mekhilta |
  | registration | joining households by count, slaughter for non-registrants or non-eaters, withdrawal | Mishnah Pesachim 8:3, 5:3; Pesachim 61a, 89a |
  | firstborn | the donkey (redeem with a lamb, else break the neck), the human (five sela as data), the caesarean | Mishnah Bekhorot 1:7, 2:9; Niddah 40a |
- **Score.** MATRIX: 24/24 cells match the answer sheet.
- **Provenance.** Pure ink 7/24 (29%), named moves 16/24 (67%), data
  1/24 (4%).
- **Effects.** barred_from_it, burn_remainder, consecrated_firstborn,
  disqualified, eating_window, exempt, karet_cut_off, lashes, pays,
  purge_deadline, redeem_or_break, registered_to_lamb. Ledger ops: block
  x10, body x1, debit x1, heaven x1, status x8, timer x3, transfer x2. The
  first karet on Heaven's docket.
- **Imports.** None inward. The offerings dispatcher routes its Passover
  row here.
- **Moves.** M-15 the voice read and M-16 the revocalization read were
  registered from this span's exam blocks; the compile itself uses M-04
  and M-05.

---

## Leviticus

### 7. cold_run_vayikra5.py — Leviticus 5

- **Span and opener.** Leviticus 5, opened by וְנֶפֶשׁ כִּי תֶחֱטָא ("and a
  soul, when it sins", 5:1) and its thirteen verse-initial case openers
  (verses 1, 2, 3, 4, 7, 11, 14, 15, 17, 20, 21, 22, 24). The first
  compile under the Step-5 deliverable rule.
- **Functions.** graded_offering (5:1-13: the sliding-scale offering, its
  four triggers and three tiers), sacrilege (5:14-19: trespass on sancta
  and the suspended guilt-offering), deposit_restitution (5:20-26: the
  deposit oath and its payment algebra, principal plus a fifth plus the
  ram). Answer sheets: Mishnah Shevuot 2:1, 2:5, 3:1, 3:5, 3:8, 4:3, 4:8-12,
  5:1; Keritot 5:2; Bava Kamma 9:5, 9:7, 9:9; Meilah 18a; Bava Metzia 54a;
  Sifra Sections 9 to 13 and Chapter 22.
- **Score.** MATRIX: 27/27 cells match the answer sheet.
- **Provenance.** Pure ink 7/27 (26%), named moves 15/27 (56%),
  data and dispute 5/27 (19%). Disputes fork with both arms labeled (the
  day-of-guilt valuation).
- **Effects.** adds_fifth, atoned_forgiven, exempt, pays, restores.
  Ledger ops: debit x9, heaven x13, status x11, transfer x4.
- **Imports.** None.
- **Moves.** M-01 the diff (Bava Metzia 54a's four-value fifth), M-02,
  M-04.
- **Engine.** The deposit oath is wrapped as `law_deposit_oath`.

### 8. cold_run_tzav.py — the offering-torah span

- **Span and opener.** Leviticus 6-8, the priests' law layer, opened by
  the procedure headers זֹאת תּוֹרַת ("this is the law of", 6:2, 6:7, 6:18,
  7:1, 7:11) and by the installation narrative of chapter 8.
- **Functions.**
  | Function | What it decides |
  |---|---|
  | altar_machine | the one-way altar and its night windows, retention classes, dislodged before midnight, the extinguish ban, the pile count as data |
  | vessel_purge | earthenware broken, copper scoured and rinsed, the garment laundered, the absorption rule |
  | chavitin_machine | the perpetual griddle offering's halving, the successor and no-successor pair, twelve loaves as data, Onkelos' conversion layer at 6:13 |
  | rejection_machine | the thanksgiving window with its fence, the vow and gift window, third-day burning, out-of-time and out-of-place, the no-permitters list, the impure eater |
  | karet_machine | the congregational exemption, the fat karet, the Noahide negative boundary, the lifeblood |
  | dues_machine | the olah hide, the minchah to the household, breast and thigh after smoking, the consent gate, and the sons of Eli at 1 Samuel 2:15-17 checked against that gate |
  | installation | atomicity over bullock, two rams, and basket; the commit at the blood sprinkling; the seven-day template; the leftover burned |
  Answer sheets: Mishnah Zevachim 2:2, 4:3, 5:6, 9:1, 9:6, 11:1-8, 12:2,
  13:2; Menachot 3:6, 4:5, 5:8, 6:5; Yoma 1:1, 4:6; Pesachim 9:4; Keritot
  1:1, 5:1; Chullin 10:1; the Sifra throughout.
- **Score.** MATRIX: 33/33 cells match the answer sheet.
- **Provenance.** Pure ink 2/33 (6%), named moves 29/33 (88%), data
  2/33 (6%).
- **Effects.** Fifteen, the most of any span: break_earthen_vessel,
  burn_remainder, confined_seven_days, due_to_priest, eating_window,
  exempt, invested_office, karet_cut_off, labor_barred,
  launder_blood_spot, not_accepted, perpetual_fire_duty, purge_deadline,
  sanctified_by_contact, scour_and_rinse. Ledger ops: block x3, heaven x4,
  status x6, timer x5, transfer x6.
- **Imports.** Numbers 5:31 and Leviticus 19:7 are cited inside the
  rejection and karet cells. The dues machine runs one narrative log,
  1 Samuel 2:15-17, against its after-smoking gate.
- **Moves.** M-13 the clause-position read and M-14 the doubling
  arithmetic were born in this compile.
- **Engine.** The installation is wrapped as `law_installation`; engine
  scene 6 replays Leviticus 8 itself as the tape.

### 9. cold_run_offerings.py — the Leviticus 1-8 offering dispatcher

- **Span and opener.** The whole of Leviticus 1-8 as one type dispatcher.
  The place link is the doubled slaughter verb at 6:18 and 7:2 (the sin
  and guilt offerings are slaughtered "in the place where the olah is
  slaughtered", the verb written twice in each verse), and the olah's
  place is 1:11's own צָפֹנָה ("northward").
- **Function.** `dispatch(offering)` returning, for each offering class,
  its slaughter place, blood applications, remainder, eater, eating place,
  and window, with effects. The per-chapter compiles (Leviticus 5 and Tzav)
  remain the case-law layer beneath it.
- **Answer sheet.** Mishnah Zevachim 5:1-8 read whole from the local
  shelf, sixteen grid tokens verified in the Mishnah's own ink: the
  innermost sin offerings (5:1), the burned bulls and goats (5:2), the
  sin offering (5:3), the olah (5:4), communal peace offerings and the
  guilt offering (5:5), the thanksgiving and the nazirite's ram (5:6),
  peace offerings (5:7), firstborn, tithe, and Passover (5:8).
- **Score.** MATRIX: 40/40 cells match the answer sheet on the first
  graded run.
- **Provenance.** Pure ink 15/40 (37%), named moves 12/40 (30%), fence
  3/40, data 5/40, imports 5/40.
- **Effects.** accepted, burn_remainder, due_to_priest, eating_window,
  on all eight rows.
- **Imports.** Five import cells; the file's own verse references name
  Exodus 12:4, 12:8, 27:2, Leviticus 16:14, and Leviticus 27:32. Row 8's
  Passover regime is ROUTED to `cold_run_pesach.py`, and the run asserts
  that engine is present before routing. The midnight cap arrives
  self-labeled as a fence (Mishnah Berakhot 1:1's tail).
- **Moves.** M-17 the tension resolution was born here: the blood counts
  from the pull between סָבִיב ("around") and וְזָרְקוּ ("and they shall
  throw") in Leviticus 1:5 (Zevachim 53b:5). Also the two-verses-as-one
  limit (Zevachim 57a:3-4), entered in MIDDOT.md as the inference
  engine's overfitting guard.

### 10. cold_run_shemini.py — the species classifier

- **Span and opener.** Leviticus 11, opened by זֹאת הַחַיָּה ("these are
  the living things", 11:2).
- **Functions.** `classify(kind)`: the land predicate (split hoof AND
  cud, the conjunction enforced by the ink's four counter-stated
  exceptions), the water predicate (fins and scales), the bird blacklist
  (twenty named kinds, no signs given), the locust clause, the eight
  swarmers by name. `touch_effect(event)`: the carcass status machine,
  touch and carry.
- **Answer sheet.** Mishnah Chullin 3:6-7 read whole, and it labels its
  own layers: "the signs of the beast were said from the Torah; the signs
  of the bird were not said, but the sages said...". Plus Mishnah Niddah
  6:9 (every scale-haver has fins) and Makkot 3:2's list for the lashes.
- **Score.** MATRIX: 19/19 cells match the recorded classifications.
- **Provenance.** Pure ink 17/19 (89%), the sages' self-labeled layer
  2/19, data 0. The highest ink fraction of any span.
- **Effects.** impure_until_evening (the 49th registered effect,
  harvested from the chapter's eightfold clause), lashes.
- **Imports.** None. One open toolchain item: the Leviticus 11:42 belly
  word is truncated in the word database at its large letter; the probe
  targets the current line and the repair is deferred to the owner.
- **Moves.** M-08 the exemplar-generalization (the Sifra's training
  route for birds), M-06.

### 11. cold_run_negaim.py — the affliction state machine

- **Span and opener.** Leviticus 13-14, opened by אָדָם כִּי יִהְיֶה ("a
  person, when there is [on his skin]", 13:2). Diagrammed in
  [STATE_MACHINES.md](STATE_MACHINES.md).
- **Functions and scores.**
  | Function | Answer sheet | Cells |
  |---|---|---|
  | the track table: skin, boil, burn, scall, bald, garment, house, each with its signs and weeks | Mishnah Negaim 3:3-3:8 | 7/7 |
  | the day arithmetic: two weeks are thirteen days, three weeks are nineteen | Mishnah Negaim 3:3 and 3:8; Sifra | 2/2 |
  | verdict machinery: shades two-that-are-four, the state guard, released versus burned, the bloom inversion, doubt polarity | Mishnah Negaim 1:1 and the Sifra's guards | 5/5 |
  | the transition runs: the ten houses walk, the deltas row | Sifra Metzora Section 7 12; Mishnah Megillah 1:7 | 2/2, with the houses 10/10 |
- **Score.** NEGAIM PASS: 16/16 cells across 4 functions, plus the
  ten-houses walk 10/10.
- **Provenance.** INK 7, RECORDED 9, ROUTED/IMPORT 0.
- **Effects.** burned_in_fire, confined_seven_days, demolished,
  impure_until_evening, isolated_outside_camp, released. Ledger ops:
  destroy x2, status x3, timer x2. Three effects (isolated_outside_camp,
  burned_in_fire, demolished) were registered from this compile.
- **Imports.** None. The one-week boil and burn track comes from the
  ink's own silence: no second shutting is written there, and the
  shut-again census stands at 13:5, 13:33, and 13:54.
- **Moves.** M-05 the threshold-parse (the shared-junction day), M-06.

### 12. cold_run_yoma.py — the Yom Kippur service machine

- **Span and opener.** Leviticus 16, opened by בְּזֹאת יָבֹא אַהֲרֹן ("with
  this shall Aaron come", 16:3). Uncommitted at the time of writing.
- **Functions.**
  | Function | What it decides | Answer sheet |
  |---|---|---|
  | route(known_start, known_end, deliberate, sin_class) | the atonement routing table: which goat or offering covers which knowledge state | Mishnah Shevuot 1:3 and 1:6; Sifra Acharei Mot Chapter 5 |
  | day_atones(between, appeased) | the fellow gate: the day atones between man and God; between man and fellow only once appeased | Mishnah Yoma 8:9 |
  | service_order() | eighteen steps in verse order, with 16:23 executed late by the Sifra's order meta-rule | the ink's own sequence; Sifra Acharei Mot Chapter 6 |
  | dispatch_goat() | the goat bears all iniquities to a cut-off land | 16:22 with Onkelos |
- **Score.** YOM KIPPUR MACHINE: 18/18 cells.
- **Provenance.** INK 9, RECORDED 6, ANSWER-SHEET 3.
- **Effects.** atoned_forgiven, dispatched_to_wilderness, suspends.
- **Imports.** None. Ink censuses inside the run: four linen tokens at
  16:4, three Azazel seats, five lot tokens, two seven-stroke seats, one
  written confession with two more derived.
- **Moves.** M-11 the word-order read (the verse sequence as the program
  counter), M-12.

### 13. cold_run_lev24.py — the first call

- **Span and opener.** Leviticus 24:10-23. The opener is a narrative
  event, the blasphemer, and the span records the runtime code request:
  the case held in custody (24:12), the code arriving, and the run log
  grading itself (24:23, "as the LORD commanded"). Pulled ahead of the
  walk because Exodus 21's talion cell depends on it.
- **Functions and scores.**
  | Function | Answer sheet | Cells |
  |---|---|---|
  | runtime code request: undefined case held, the run log grades itself | the span's own execution report | 2/2 |
  | curse gate: cursing without the Name bears sin; death needs the Name by the Name; piercing is the cursing; the sojourner included | Mishnah Sanhedrin 7:5; Sanhedrin 56a | 4/4 |
  | stoning protocol: outside the camp, the hearers lay hands, all the congregation, the stripping dispute | Mishnah Sanhedrin 6:1 and 6:3; Sanhedrin 45a | 4/4 |
  | killing pair: any human soul, a day-old victim counts, a beast is paid for, the juxtaposed pair, life-under-life at exactly two seats | Mishnah Niddah 5:3; Makkot 1:6 | 5/5 |
  | THE TARIFF, exported as `talion(blemish)`: as he did so shall be done; fracture, eye, tooth; money not body; a man not his ox; the per-status rows | Mishnah Bava Kamma 8:1-8:3; Bava Kamma 83b-84a | 5/5 |
  | one law: sojourner equals native, one procedure floor, equal across bodies | Mishnah Sanhedrin 4:1; Bava Kamma 84a | 3/3 |
- **Score.** LEV 24 PASS: 23/23 cells across 6 functions.
- **Provenance.** INK 16, RECORDED 6, ROUTED/IMPORT 1 (70% pure ink).
- **Effects.** bears_sin (the 50th registered effect), pays,
  put_to_death, stoned, substitution. Ledger ops: body x3, debit x2,
  status x1.
- **Exports.** `talion()` is imported by `cold_run_mishpatim.py` and
  resolves its damage cell. This is the compiled Bible's first
  inter-span function call.
- **Imports and routing.** The epithet arm of the curse gate is routed to
  the Noahide block (Sanhedrin 56a:20). The machine census confirms
  eye-under-eye at exactly two seats in the canon, Exodus 21:24 and
  Leviticus 24:20.
- **Moves.** M-07 the cross-module import (exemplar c, executed), M-03
  the comparison (the juxtaposed pair), M-14.

### 14. cold_run_moadim.py — the appointed times engine

- **Span and opener.** Leviticus 23, opened by אֵלֶּה מוֹעֲדֵי יְהוָה ("these
  are the appointed times of the LORD", 23:4, with the frame at 23:2).
  The Emor sweep's compile, uncommitted at the time of writing, and the
  first compiled after this catalog's first draft.
- **Functions.**
  | Function | What it decides | Answer sheets |
  |---|---|---|
  | work_class(day) | the two work-ban classes read off token forms: כָּל מְלָאכָה ("all work") at verses 3, 28, 30, 31 against מְלֶאכֶת עֲבֹדָה ("servile work") at 7, 8, 21, 25, 35, 36; festival and Sabbath differ only in food work | Mishnah Megillah 1:5 |
  | yom_kippur() | the affliction with its two sanctions, karet at 23:29 and destruction at 23:30; the five afflictions; the eater and the worker among the lashed | Mishnah Yoma 8:1, Keritot 1:1, Makkot 3:2 |
  | omer() | seven whole weeks plus fifty days; the morrow of the Sabbath read as the festival; the new-grain gate "until you bring"; the whole-day ban without the Temple | Mishnah Chagigah 2:4, Menachot 5:3, 10:5 |
  | two_loaves() | equal and mutually indispensable; no oil, no frankincense | Mishnah Menachot 3:6, 5:3 |
  | rosh_hashanah() | the day's instrument is a shofar, imported from the Jubilee | Mishnah Rosh Hashanah 3:3 |
  | sukkot() | dwell seven days; the four species by their grammatical numbers at 23:40 (one citron, one palm branch, two willows, three myrtles by Rabbi Yishmael or one by Rabbi Akiva); the palm branch seven days before the LORD, one day in the provinces, seven even on a Sabbath; women exempt | Mishnah Sukkah 4:1, 3:12, 4:2, 3:4, 2:8 |
  | sabbath_vs_festival() | the Sabbath bars all work | Mishnah Megillah 1:5 |
  | passover() | "between the evenings" at 23:5: slaughtered before midday is invalid | Mishnah Pesachim 5:3 |
  Fifteen Mishnah rows read whole from the shelf, each verified by a token
  in its own ink.
- **Score.** MATRIX: 24/24 cells match the answer sheet.
- **Provenance.** Pure ink 14/24 (58%), recorded moves 8/24 (33%),
  answer-sheet 2/24, data 0.
- **Effects.** accepted, barred_from_it, counts_omer, destroyed,
  dwells_in_booths, exempt, karet_cut_off, labor_barred, rest_required,
  sanctify_day, takes_four_species. Three were discovered in the span's
  own verbs and registered before the run: counts_omer (a timer),
  dwells_in_booths (a timer), takes_four_species (a status). The registry
  stands at 58.
- **Imports.** The shofar from Leviticus 25:9 (Sifra Emor Section 11 6).
  Onkelos writes "after the festival day" into 23:11 and 23:15, the
  reading witness for the morrow-of-the-Sabbath route, which the Sifra
  (Emor Chapter 12) derives four ways.
- **Moves.** M-12 the grammatical-number hook (the four species'
  singular and plural tokens), M-07 the cross-module import (the shofar),
  M-09 the keyword dictionary (the two work classes).

---

## Reading the fractions together

| Span | Cells | Pure ink | Named moves | Other |
|---|---|---|---|---|
| guardians | 12 | 6 | 3 | 3 routed |
| mishpatim pass 1 | 23 | 15 | 5 | 3 routed or imported |
| mishpatim pass 2 | 9 | 5 | 1 | 3 routed or imported |
| decalogue | 12 | 1 | 11 | |
| calendar | 14 | 4 | 9 | 1 data |
| pesach | 24 | 7 | 16 | 1 data |
| vayikra5 | 27 | 7 | 15 | 5 data or dispute |
| tzav | 33 | 2 | 29 | 2 data |
| offerings | 40 | 15 | 12 | 3 fence, 5 data, 5 imports |
| shemini | 19 | 17 | 2 self-labeled | |
| negaim | 16 | 7 | 9 | |
| yoma | 18 | 9 | 6 | 3 answer sheet |
| lev24 | 23 | 16 | 6 | 1 routed |
| moadim | 24 | 14 | 8 | 2 answer sheet |
| **total** | **294** | **125** | **132** | **37** |

Two shapes stand out. Classification, calendar, and procedure spans (the
species classifier, the appointed times, Leviticus 24) run high on ink. Duty
and cult spans (the Decalogue, Tzav) run high on recorded moves, because
their ink states obligations and the case law that grades them lives in
the tradition's readings. Neither is a defect. The fraction is a
measurement of where each span keeps its logic.
