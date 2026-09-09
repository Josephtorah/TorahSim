# REPORT — THE CLOCK SITTING (2026-09-07; the first ENGINE sitting since the skeleton's first spin)

The owner's word: "ok do the clock sitting" — after the two-thread consensus (round one A-G, round two's eight amendments,
both recorded in the state doc) on the design thread's specification ARCHITECTURE/THE_CLOCK.md (read, never edited). The
implementation record is World/step9/CLOCK.md; this report is the sitting's account. The order held as the wrap rhythm
fixes it: the design FIRST (CLOCK.md, sections 0-8), the fire-probes SECOND (World/step9/clock_probes.py — twelve probes,
0/12 against the unchanged engine, 12/12 after), the engine code THIRD, the library edit FOURTH, the five year-grain scenes
RE-TYPED FIFTH under print-then-type (the predictions in the scratchpad's clock_predictions.txt before any runner ran),
the gates and the sweep and the records SIXTH.

## What the engine is now

1. **THE DAY IS THE BASE UNIT; THE YEAR IS DERIVED.** `Clock.day` is the only counter; `Clock.year` is computed through
   the world's EPOCH ROW by a Calendar, and is `None` where no epoch is declared (the twenty-eight day-grain worlds).
   The walker is unchanged: `advance(to_day)` steps one day and fires every timer at its due.
2. **THE CALENDAR IS AN ENGINE CONSTRUCT OVER A DATA FILE.** `world_engine.Calendar` lays the months out from the epoch
   and answers `year`, `date`, `day_of`, `next(day, key)`, `add(day, n, key)` for the keys day, week, month, year,
   sabbatical, jubilee. It is the ONLY reader of the THIRD REGISTRY, World/step9/calendar_parameters.yaml — eighteen rows
   (ink 6, received 9, rounding 1, modeled 2) and five era rows, each with its channel, its source resolved on the local
   shelf by script at the sitting, and its teacher. The mechanism is ink (Genesis 1:5's evening, Exodus 12:2's month one,
   Leviticus 25:4, 25:8, 25:10's seven, forty-nine, fifty); the quantities are the rows: the received month of Rosh
   Hashanah 25a:10 rounded to thirty and twenty-nine alternating (OPEN-6 the parts), the four new years of Mishnah Rosh
   Hashanah 1:1 as DATA (the design thread's flag, accepted), the intercalation by the season ground alone (Sanhedrin
   11b:5's three grounds; the recorded threshold of Sanhedrin 13a:4 — sixteen days by the Sages, twenty by Rabbi Yehuda;
   Sanhedrin 12b:8 only the twelfth month intercalated) over a MODELED solar year and equinox (OPEN-2: the season's length is
   named by TIME.md at Eruvin 56a and was NOT FOUND on the local shelf under the searched forms — held modeled until read),
   the regnal rounding of Rosh Hashanah 2b:1 UNEXERCISED, the count-start of Arakhin 12b:5 and 13a:7-8 as two recorded
   settings (OPEN-1), the fiftieth's place in the cycle (Rosh Hashanah 9a:1 against Arakhin 12b:4) UNEXERCISED.
   No daemon is named "the calendar law": the boundary timers are set by the daemons whose verses command the count.
3. **THE PERIOD FIELD AND THE CLOSE PAIRING.** A timer effect may carry `period` — opt-in; an integer of days or a calendar
   key re-armed through the Calendar at the fire, each re-arm logged `TIMER-SET` with `rearmed_from` (a chain the diff
   engine counts); a recurrence ends by `cancel_timers` on a text event, never on a count. The erection's daemon now CLOSES
   the altar's open `tamid_owed` when the tamid is offered (Exodus 29:38) before setting tomorrow's — and `tamid_owed`'s
   ledger op moved from `timer` to `debit` in the registry, with the reason: a timer op opened no entry to close.
4. **THE MARKER, THE BOUND, THE RETROGRADE MARKER.** `world.marker(verse, day)` logs the text's own date stamp and walks
   the clock; every event between markers carries `bound = [the last marker, open]`, closed by the next marker on every
   event, effect, timer and fire that shares it (the engine copies it during consumption; no daemon touches it);
   `checkpoint(..., bound=)` tests an interval and says when the bound is still open. A marker EARLIER than the counter
   (Pesachim 6b:7 — "there is no earlier and later in the Torah"; Numbers 9:1 after 1:1) is logged retrograde, the counter
   unmoved, the following events `dated` by the text beside the counter's `day`, their timers computed from the stated
   day, a due already past written at submission as `RETRO-WRITE`.
5. **THE JUBILEE IN THREE LAYERS, ACT-FORKED.** `law_yovel` consumes `entered_the_land` (Leviticus 25:2 — its own verse) and
   sets two recurring status timers on the land: `sabbath_of_the_land` (period 'sabbatical') and `jubilee_year` (period
   'jubilee'); the sowing reads the land's status off the ledger, never the event's year. A sale's timer writes the
   ENTITLEMENT `goes_out_in_the_jubilee` (25:28) at the fiftieth year's first day. The RELEASE is written when the
   proclamation (25:9-10 — the act KEPT, its `year` field retired, its day the Calendar's tenth of the seventh month) is
   consumed, forked on the tradition's three recorded conditions: the horn sounded and the servants sent free off the act's
   own fields (Sifra Behar Chapter 2 4 — Rabbi Yehuda against Rabbi Yose), all the inhabitants upon the land off the
   people's ledger (Arakhin 32b:16 — the exile of Reuben, Gad and half of Manasseh), the arms as VALUES on the land's
   `jubilee_release` and `jubilee_holds`, the "no jubilee" arm named, never a silence. Four effects registered first.
6. **THE LIBRARY.** `law_slave_term`: the six years a calendar due (the same date six years on); the pierced servant's
   jubilee the Calendar's next fiftieth (the `jubilee_year` field retired from `slave_pierced`); the proclamation CANCELS
   each freed servant's pending term (THE PENDING TERM of REPORT_WRAP_W5.md finding 1, fixed) and defers to the land's
   `jubilee_holds` where a jubilee daemon registered before it has written one. `law_installation`'s seven days read the
   counter as the day.
7. **THE RENAME.** Twenty-five day-grain runners: `clock.year` → `clock.day` (fifty sites) and `entry['year']` →
   `entry['day']` (six scenes) — mechanical, no literal moved. The five year-grain runners re-typed: the count epoch
   declared, `advance(N)` → `advance(w.clock.at_year(N))`, thirty-five `'year'` fields removed from the submits and from
   twelve registry entries (the smuggled parameter retired), the dues computed through the Clock.

## The predictions against the machine (print-then-type)

| scene | slots | predicted before the run | result |
|---|---|---|---|
| yovel SCENE | 51 (the old 45 + six) | tset 14 → 20, fired 13 → 17, one cancel, eight re-arms, the sabbaticals [7, 14, 21, 28, 35, 42, 49], every other slot the old literal | MATCHED first run |
| yovel SCENE_FORK | 9 | the arms' values per world, the field returned only on a holding arm | 8 of 9 — see finding 1 |
| calendar | 16 | unchanged | MATCHED (17/17) |
| holiness_b | 44 | unchanged | MATCHED (183/183) |
| tochacha | 19 | unchanged | MATCHED (38/38) |
| mishpatim | 22 | unchanged | MATCHED (24/24) |
| the skeleton | 6 checkpoints | scene 1 re-typed to years 6 and 7; scene 5 the jubilee at the fiftieth | 6/6 |

## Findings

1. **THE VERDICT'S ORDER.** The fork's world with the servants not sent free predicted the land's verdict as beginning
   "jubilee" (Rabbi Yose's arm holds); the machine wrote "no jubilee (Rabbi Yehuda...); jubilee (Rabbi Yose...)" — the
   arms joined in the Sifra's order, and the library's deferral reads the head of the string. The prediction stood; the
   daemon was corrected to name the holding arm first. Probe 9 had passed because it read the per-arm entries, not the
   joined verdict: the scene's row caught what the probe did not.
2. **THE LIBRARY READ THE COUNTER BY THE OLD NAME.** After the rename the skeleton's sixth scene crashed: `law_installation`
   computed its seven days from `clock.year`, now `None` in a day-grain world. The skeleton's own run is a probe of the
   library; fixed to `clock.day`.
3. **THE SEASON'S LENGTH IS NOT ON THE SHELF.** The whole Babylonian shelf was searched by script for the season-to-season
   phrase and the ninety-one days; nothing. The solar year is MODELED, labeled, OPEN-2 — and with the recorded threshold it
   produced nineteen thirteen-month years in the first fifty (count-years 2, 4, 7, 10, 12, 15, 18, 20, 23, 26, 28, 31, 34,
   36, 39, 42, 44, 47, 50): seven in nineteen, the frequency of the tradition's later fixed cycle, from the threshold and
   the solar year alone — never counted as ink.
4. **OPEN-4 ON THE ENGINE.** The flood's second-month-seventeenth to seventh-month-seventeenth is 147 days under the received
   month against the text's 150 (Genesis 7:11, 8:3-4): the checkpoint prints DIVERGE and says so (probe 11).
5. **THE WITNESS CHECK AND THE MORPHEME BAR.** The Tanakh DB's words carry morpheme separators; a consonantal witness check
   must strip them, and a query over one cursor inside another's iteration returns nothing — two false "not found" results
   read before believed. Every new effect's Hebrew was then machine-verified (25:6, 25:10-13, 25:28, 25:30-33, 25:54).
6. **A FUNCTION-LEVEL IMPORT IS INVISIBLE TO THE DEPENDENCY CENSUS.** The fork's world registers the tochacha runner's daemon
   through an import inside the scene; the gate's live-edge list does not show it, though its CALL check accepts it. The
   edge yovel → tochacha is filed as a TRANSFER taught by Arakhin 32b:16 (167 edges on file).
7. **THE FORK'S REACH TO LEVITICUS 27 IS OPEN.** The consecrated field's going out in the jubilee (27:21, 27:24) stays a
   direct timer at the fiftieth's arrival; whether the Sifra's conditions govern it too is filed OPEN.
8. **THE COUNT-START AS TWO SETTINGS.** The year-grain scenes replay rows stated by count-year ("the seventh", "the
   fiftieth"), so they run the rows' own frame (offset 0); Arakhin 12b-13a's fourteen is the historical tape's setting.

## The census (coverage first)

| | before | after |
|---|---|---|
| effects | 242 | 246 (sabbath_of_the_land, jubilee_year, goes_out_in_the_jubilee, jubilee_holds) |
| event types / witness runs | 266 / 640 | 266 / 640 (twelve entries' `year` fields retired; the proclamation's three conditions; lint 0) |
| registries | 2 (events, effects) | 3 (+ calendar_parameters.yaml: 18 rows, 5 eras; 6 UNEXERCISED rows visible) |
| daemons / functions | 38 / 248 wrapped, 0 owed, 6 none of 254 | 38 / 248 wrapped, 0 owed, 7 none of 255 (the fork's count helper) |
| dependency edges | 166 | 167 (yovel → tochacha, transfer, Arakhin 32b:16) |
| worlds with a derived year | 0 | 6 (the five year-grain scenes and the skeleton, epoch 'count') |
| the clock probes | — | 12/12 (0/12 on the old engine) |
| the gate probes | 5/5, 12/12 | 5/5, 12/12 |

## The sweep at the sitting's close

33 of 33 runners green, 3,626 graded cells (3,625 + the fork's row), both gates satisfied first (scratchpad sweep_clock.txt,
SWEEP-EXIT 0): DEPENDENCY GATE 167 edges / 72 pointers, every CALL live; DAEMON GATE 248 wrapped / 0 owed / 7 none of 255,
unfired 0, unconsumed 0, open aliases 1; the events lint 0 (266 types, 640 witness runs); the clock probes 12/12; the gate
probes 5/5 and 12/12; the skeleton 6/6. No frozen unit touched. The day is the base unit; the year is derived; the jubilee is
decided by the act. Next: Numbers (its first sitting reads the standing map — THE_STEPS whole, the spine default Sifrei Bamidbar
and Onkelos, the oral-first pipeline memory, the deliverable rule as amended).

## O5 — THE MOADIM RE-TYPE (2026-09-07; the open-items campaign's fifth sitting; the owner: "Go 05")

The design: CLOCK.md section 10, declared before the code. THE DEFECT was a runner doing the calendar's work: the
appointed-times scene advanced to hand-typed day numbers (178, 187, 192, 199) with the month lengths in a comment and
no epoch, and copied those numbers onto its events for the daemon's timers; the erection's worlds counted relative days
the same way ("day 47 = the seventeenth of Tammuz"). THE CHANGE: Leviticus 23's dates became the third registry's ink
row `festival_dates`, keyed by the convocation names the scene already used (the event's `day` value is the key), with
the omer's morrow a received row (Sifra Emor Chapter 12; Menachot 65a-66a) carrying the refused Boethusian reading as a
setting; the Calendar answers `next(day, key)` for a festival key — this year's occurrence if still ahead, else next
year's — and a {from, plus} row resolves by the ink's own count (the fiftieth from the omer, the eighth from the first);
the daemon sets each proclaimed festival's recurrence as a PERIOD timer on that key ("throughout your generations"), the
Sabbath's on the week; the omer's and the booths' day timers read the clock; the scene declares the exodus epoch and
walks from festival to festival by asking the Calendar. The erection's installation world and Sinai world declare the
epoch too: the erection at day_of(2, 1, 1) with the take-list seven days before it, Sinai on the first of Sivan, the
breaking at the timer's own fire, the second ascent forty days before the row second_tablets_given — and the W7 tuple
carries the calendar DATES of its first and last fires.

### Print-then-type

Every number typed into the two runners was computed first by scratchpad o5_predict.py from the Calendar: the moadim
tuple (…, 35, …, 37, 29, 198) with the Sabbath's twenty-seven fires, the erection's 360 and the Sinai world's (105, 186,
(1, 4, 17), (1, 7, 10)). Both runners matched on their first run — 42/42 and 287/287. The four probes failed on the old
engine and pass on the new (16/16 with the twelve standing).

### Findings

1. **THE SEVENTEENTH OF TAMMUZ IS NOW A DATE, NOT A COUNT.** The first tablets' timer fires at day 105 and the Calendar
   reads it as the seventeenth of the fourth month — Sivan's thirty days under the received month, seven plus forty.
   Taanit 28b's arithmetic reproduced by the engine's own months, not by a comment.
2. **THE INK'S COUNTS MEET THE CALENDAR'S KEYS.** The omer's fifty (23:16) lands on the sixth of the third month; the
   booths' seven (23:42) on the eighth day (23:36); the morrow of the breaking to the second ascent is exactly forty —
   three independent counts agreeing with three dated keys, asserted in the prediction script before any run.
3. **A RECURRENCE COMMANDED BY THE INK RUNS AS A PERIOD.** "An everlasting statute throughout your generations" is a
   timer that re-arms through the Calendar; the Sabbath's week re-armed twenty-seven times in the test year and the seven
   festivals armed themselves for year 2 at the dates the Calendar computed — (2, 1, 15) through (2, 7, 22).
4. **RETIRING A FIELD MOVES A CENSUS.** The sequence tape's events did not change, but the stitcher's re-based count
   went 3 → 0: the fields it used to drop no longer exist. The prediction said "unchanged"; the script's count was
   typed and the prediction corrected beside it.
5. **THE ROW COUNT WAS MISREAD.** The declaration said 20 → 22 rows; the census prints 24. A number typed from memory,
   caught by the census the same sitting.

### The sweep at the sitting's close

34 of 34 runners green, 3,633 graded cells, both gates satisfied first (scratchpad sweep_o5.txt, SWEEP-EXIT 0):
DEPENDENCY GATE 162 live edges, 231 + 72 on file; DAEMON GATE 38 daemons / 267 kinds / 776 submit records, 244 WRAPPED /
0 OWED / 0 NONE, unfired 0, unconsumed 0, open aliases 0; the events lint 0; the clock probes 16/16; the sequence runner
7/7. Registry: 24 rows (ink 8 / received 13 / modeled 2 / rounding 1), eras 6, the exodus era exercised by sequence,
moadim and erection; five `day` fields retired. No frozen unit touched; the corpus regression green, hash
8b8fff1fa28953af unmoved.

## O6 — THE FORK'S REACH TO LEVITICUS 27:21 AND 27:24 (2026-09-07; the open-items campaign's sixth sitting; the owner: "Next go")

The design: CLOCK.md section 11, declared before the code, after the shelf was read by script. THE OPEN ITEM was
the clock sitting's own note in the runner: the field a man consecrates (Leviticus 27:16-24) went out to the
priests, or returned to its holder, on a plain TIMER to the fiftieth year — `due_to_priest` and
`returns_to_holding` due at the date — while the sold field and the sold servant of Leviticus 25 waited on the
PROCLAMATION act and the fork's three recorded conditions. The question was whether those conditions govern the
consecrated field too. THE ANSWER, from the shelf: (a) the third condition reaches it, TAUGHT — Arakhin 29a:15-17's
baraita (the Hebrew slave, the field of the holding, the walled-city houses "apply only when the jubilee is in
effect") with Rabbi Shimon ben Yochai reading it off our clause, וְהָיָה הַשָּׂדֶה בְּצֵאתוֹ בַיֹּבֵל ("and the field in
its going out in the jubilee", 27:21); "in effect" is Sifra Behar Chapter 2 3 / Arakhin 32b:16's "to ALL its
inhabitants"; (b) the first and second conditions reach it by REFERENCE — 27:21 "in the jubilee" and 27:24 "in the
year of the jubilee" NAME the institution whose validity the fork decides, the clause calling the definition, no
rule crossing (the link review law's first answer; the shared content lemma יובל "jubilee"); its timing the Sifra's,
Behar Chapter 2 1 — the fields returned to their owners when the Day's horn sounded, the release ON THE ACT; and
both of the Sifra's arms hold a jubilee "even though they did not release" the fields (Rosh Hashanah 9b:2-3) — the
fields' release is an act the year commands, never a condition of the year; (c) the going out carries a fork of ITS
OWN the engine had never held — Mishnah Arakhin 7:4 = Sifra Bechukotai Chapter 11 2: the jubilee arrived and the
field unredeemed — Rabbi Yehuda: the priests enter and pay its value; Rabbi Shimon: enter and do not pay; Rabbi
Eliezer: neither — an ABANDONED FIELD (שְׂדֵה רְטוּשִׁים) until the second jubilee, his ground Rava's at Arakhin 26a:16,
"in its going out — from the hand of ANOTHER" (27:20's "and if he sold the field to another man" precedes 27:21).

THE CHANGE (cold_run_yovel.py; no engine edit, no new import edge): the consecrated field's going out is an
ENTITLEMENT — `goes_out_in_the_jubilee` on the field, a timer to the fiftieth, its VALUE the route the ink and the
rows give (to the priests, 27:21; to him from whom he bought it, 27:24; from the hand of another, 27:20 with Rava;
to his father, Mishnah Arakhin 7:3; to all his brother priests, 7:3 with Arakhin 25b:14-16 on "HIS holding") — and
the RELEASE is the proclamation daemon's, on every arm that holds, routed by that value: the purchased field and the
son's field return (`returns_to_holding`, not to the treasurer — Sifra Bechukotai Chapter 11 7), the priest's field
and the field from the hand of another go to the priests (`due_to_priest`, the counterparty the WATCH the jubilee
met — Arakhin 28b:4), and the holding unredeemed runs the 7:4 fork as three named VALUES on `due_to_priest` (Rabbi
Yehuda's arm with the priests' `pays` to the treasury; Rabbi Shimon's; Rabbi Eliezer's "no entry" a named value,
never a silence) plus the new effect `abandoned_field` and the entitlement RE-ARMED to the next jubilee the Calendar
computes. On no arm holding — the exile — nothing is written on the field: the land's verdict names the arm and the
reach, the entitlement stands. The owner's redemption and the owner's re-redemption from another write no entitlement
(7:3 — the field does not go out); the fifth on the owner and on the heir (7:2; Sifra Bechukotai Chapter 10 11).

### Print-then-type

The two scene literals were parsed from the runner as it stood and the declared deltas applied by name in scratchpad
o6_predict.py before a line of the runner was typed: field-4's `due_to_priest` years [50] → [50, 50, 50]; timers set
20 → 24 and fired 17 → 20; ten slots appended (1, 1, 1, [50], [50], [25], [50], 0, 0, 0); the fork tuple's four
(3, 3, 0, 1). The runner matched on its FIRST RUN — 90/90, both tuples exactly as printed: the three arms on field-4
dated the proclamation's year; the priests' payment once; the abandoned field once; the re-armed entitlement pending
at day 36,156 = the hundredth count-year; field-7 (sold to another) one entry, the arms agreed; field-8 to his father
with the heir's fifth of twenty-five; field-9 to all his brother priests, no fifth; field-10 nothing; the fork's
consecrated field three entries on each holding world and none on the exile's, its entitlement standing there.

### Findings

1. **THE REACH WAS ON THE SHELF, NAMED, AT OUR OWN VERSE.** Arakhin 29a:17 has Rabbi Shimon ben Yochai derive "only
   when the jubilee is in effect" from 27:21's "in its going out in the jubilee" — the exile's condition reaches the
   consecrated field by a recorded teacher, not by our inference. The plan had called this a reading sitting; the
   reading settled it in one baraita.
2. **THE INK NAMES THE INSTITUTION, SO THE ARMS REACH BY REFERENCE.** "In the jubilee" and "in the year of the
   jubilee" are the same word the Sifra's two arms read at 25:10-12; a clause that names the year calls the year's
   verdict. And the Sifra records the timing — the fields returned when the Day's horn sounded (Behar Chapter 2 1):
   the release is written on the act, the timer only entitles. The runner's timer-only release had been fiction by
   the shelf's own account.
3. **THE GOING OUT HAD A FORK OF ITS OWN.** Mishnah Arakhin 7:4's three arms at the moment the jubilee arrives were
   not in the engine at all; Rabbi Eliezer's arm turned out to be a TIMER — "abandoned until the second jubilee" is
   the entitlement re-armed to the next fiftieth, and "abandoned of the abandoned until the third" is the same
   re-arm again. The tradition's word for the state became the effect; the model was already in the engine.
4. **THE MISHNAH FILE AND THE TALMUD'S MISHNAH DISAGREE ON ONE ROW.** 7:3's "another redeemed it and the owner
   redeemed it from his hand" reads "it does not go out" in the Mishnah file and "it goes out to the priests" at
   Arakhin 25a:16. The file's text is graded; the variant is recorded beside the cell, not resolved by us.
5. **THREE NEW TOP-LEVEL FUNCTIONS WERE LAWS TO THE GATE.** The daemon gate flagged `going_out`, `arrival_unredeemed`
   and `field_kind_by_father` as compiled functions writing effects with no disposition — the W3 lesson firing
   honestly; dispositioned WRAPPED by law_yovel, 244 → 247 of 247.

### The sweep at the sitting's close

34 of 34 runners green, 3,646 graded cells (thirteen new), both gates satisfied first (scratchpad sweep_o6.txt,
SWEEP-EXIT 0): DEPENDENCY GATE 162 live edges, 231 + 72 on file, no new edge; DAEMON GATE 38 daemons / 267 kinds / 781
submit records, 247 WRAPPED / 0 OWED / 0 NONE of 247, unfired 0, unconsumed 0, open aliases 0; the events lint 0; the
effects registry 247; the probes 5/5, 11/11, 12/12, 8/8, clock 16/16, sequence 4/4. The yovel runner 90/90 on its first
run, the answer sheet 42 Mishnah + 29 Sifra/Talmud rows. No frozen unit touched; the corpus regression green, hash
8b8fff1fa28953af unmoved.


## O9 — THE CLOCK'S OPEN ITEMS (2026-09-08; the open-items campaign's ninth sitting; the owner: "Let continue")

The design: CLOCK.md section 12, written before a probe or a line of engine — the time consensus's three (T3, T2, T4), the
open items read again, and OPEN-5 as an engine sitting. The tape's side is SEQUENTIAL_RUN.md section 14 with its account in
REPORT_SEQUENTIAL_RUN.md's O9 section; this is the engine's and the registry's.

THE SHELF FIRST, BY SCRIPT — and the sitting's first lesson came from the reading itself: Bereshit Rabbah's file is POINTED
and the clock sitting's OPEN-2 search had run an unpointed phrase against it. With the points stripped the shelf gave up
what the design had called missing: Eruvin 56a:10 — "between one season and the next only ninety-one days and seven and a
half hours" (Samuel's table, 56a:8-9), the row solar_year_days re-channeled RECEIVED with its teacher and the value unmoved
(OPEN-2 closed as far as the length goes; the equinox's date at the epoch stays modeled — the shelf gives the hours of the
day, not the epoch); Bereshit Rabbah 33:7 — the forty days of rain Marcheshvan and Kislev, the hundred and fifty days FIVE
THIRTY-DAY MONTHS from Tevet to Iyar, the ark's "seventh month" Sivan counted from the rains' end (OPEN-4: the tradition's
reading found and filed as the row flood_months; the machine runs its alternation, so C1's DIVERGE stands as the modeled
calendar's beside the shelf's reading); the covenant between the pieces with TWO local teachers (Bereshit Rabbah 46:2
eighty-five; the Mekhilta on Exodus 12:40 row 1 seventy) where the sojourn row had said "not on the local shelf"; Avodah
Zarah 9a:7-8 as the elapsed column's shelf numbers; Chullin 83a:15-16 the two day-orders; Berakhot 2a:1-4, Pesachim 58a:1-5
and Shabbat 34b:2-6 the slots' bounds; Mishnah Parah 1:3 with Rosh Hashanah 10a:4-6, 2b:1-7, 3a:14-15, 3b:2-4 and 9b:13 the
counter idioms. OPEN-1, OPEN-3 and OPEN-6 were read again and stand as recorded.

THE ENGINE (world_engine.py), after four probes written to fail (18/22 on the old engine, each for its own missing
construct): Calendar.elapsed and Era.elapsed with the Clock's elapsed and elapsed_in — the label less one at the year grain,
a life era's age as it stands; first_verse() beside seat(); World.marker(placement=) carrying the class on the MARKER log and
World.submit stamping event['placement'] — the marker's class on the event at the marker's own verse, the retrograde stretch
as one, page_order for every other event; advance() ordering one day's fires by the timer's opt-in boundary (the calendar's
evening first, consecrated things' morning after, the due unmoved); Calendar.slot_rank and crosses_day over the registry's
new day_slots block. 22/22 after; the sequence probes 4/4; four runners green on the spot.

THE THIRD REGISTRY: seven rows (covenant_pieces_year with both settings; flood_months; temple_day_boundary — Chullin 83a:16;
night_start — Berakhot 2a:1; between_the_evenings_from — Pesachim 58a:3 and Rava's 58a:5; twilight_doubt — Shabbat 34b:2,
its three definitions and Shmuel's measure, UNEXERCISED: no narrated act of the three books stands at twilight;
solar_year_days re-channeled; day_boundary's teacher Chullin 83a:15 named at last), the placement keys `places` / `refines`
on fourteen rows the markers read (gen6_3_reading deliberately without one: the decree's date is the ink's own two numbers),
the DAY SLOTS block (eight names in the calendar day's order from Genesis 1:5, the ink's own word forms censused by script —
morning 32 seats and 29 bare, evening 14 and 17, night 12 and 16, between the evenings 6, dawn 3, noon 2, midnight 1), and the
COUNTER IDIOMS block (people, kings, animals, trees, inclusive day counts, the jubilee's boundary year — six rows, three
unexercised and visible). The parameters census prints both blocks: 54 rows, ten unexercised, named.

THE TAPE: the covenant's marker at 15:1 (reading-placed, the spine's eighty-five on the running world; the Mekhilta's seventy
retrograde on the fork's world, the stretch closed at 16:1), the two position calls (21:2, 45:5), the placement classes
COMPUTED per row and injected, the slots stamped and verified again against the verse, C3d the join under both settings, C12 and C13 under the
elapsed column — every literal typed from the stitcher's print by script; the first run 9/10 (a variable name reused in the
runner's own fork loop — the world had no retro-write and the header said so), the second 10/10. The account and the
findings: REPORT_SEQUENTIAL_RUN.md's O9 section.

### Findings

1. **THE POINTS HID THE SHELF.** Two "not found" rows of the clock sitting were on the local shelf all along; the search had
   not stripped the vowel points. A search strips them now, and the memory carries it.
2. **THE TWO DAY-ORDERS ARE ONE MISHNAH AND ITS GEMARA.** Chullin 83a:15-16 gives the calendar's day (the day follows the
   night, ben Zoma from Genesis 1:5) and consecrated things' day (the night follows the day) on one page — the engine's
   `boundary` field is that page, and the eating windows' "until morning" have their construct waiting.
3. **THE SLOT IS A WORD, NOT AN HOUR.** Eight slot names cover every day-word in the three books; the hours the shelf gives
   (the sixth and a half; three quarters of a mil) stay on the rows. The day stays the unit, as the consensus fixed.
4. **THE IDIOMS DIFFER BY SUBJECT CLASS, AND THE SHELF SAYS SO ROW BY ROW.** People complete years at the New Year; kings
   count a day as a year (and the nations' kings from Tishrei — the Nehemiah collision the template); animals count from day
   to day (Parah 1:3) with the bull's two settings; a planting counts thirty days before the New Year. Data now; the
   generator waits for a join no hand can write.
5. **A NAME REUSED IS A MISS** (the tape's one miss; REPORT_SEQUENTIAL_RUN.md O9, finding 6).

### The sweep at the sitting's close

39 of 39 runners green, 4,518 graded cells (two new: the placement and the slot censuses on the sequence runner), both gates
satisfied first (scratchpad o9_sweep.txt, SWEEP-EXIT 0): DEPENDENCY GATE 191 live import edges, 285 edges + 128 pointers on
file, 112 beyond the census all on file (rule 9); DAEMON GATE 43 daemons watching 791 kinds, 327 WRAPPED / 0 OWED / 0 NONE of
327, unfired 0, unconsumed 0, open aliases 0; the events lint 0 on 791; the clock probes 22/22, the sequence probes 4/4; the
sequence runner 10/10 (51.7s in the sweep). No frozen unit touched; the corpus regression green, hash 8b8fff1fa28953af
unmoved. Next: O10 THE PEOPLE-TOKENS IN THE ONE REGISTRY, O11 THE CLAIMS LABEL DEBT, then NUMBERS (T1 installation first).
