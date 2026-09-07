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
