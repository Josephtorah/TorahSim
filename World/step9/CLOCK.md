# CLOCK.md — THE CLOCK SITTING: the implementation record (2026-09-07)

The SPECIFICATION is the design thread's ARCHITECTURE/THE_CLOCK.md (sections 0-11 and its consensus
block A-H; the evidence quoted whole in ARCHITECTURE/TIME.md) — read, never edited. This file is OURS:
the engine change as built, by the two-thread consensus of 2026-09-07 (round one A-G, round two's
eight amendments — the state doc's entries "THE CLOCK CONSENSUS" and "THE CLOCK CONSENSUS — ROUND TWO").
The owner's word: "ok do the clock sitting." Order of work: this design FIRST, the fire-probes SECOND
(written to fail against the unchanged engine), the engine code THIRD, the library edit FOURTH, the five
year-grain scenes RE-TYPED FIFTH under print-then-type, the gates and the sweep and the records SIXTH.

## 0. Scope (round two, point 1)

The ENGINE sitting only. Leviticus 23 and 25 are already compiled (cold_run_moadim.py, cold_run_yovel.py;
Exodus 23:10-19 and 34:18-26 as law_calendar in cold_run_calendar.py); Numbers 28-29 has no frozen unit —
the compiler law puts the derivation before the cold function, so the festival boundary timers wait for
Numbers. The moadim runner keeps its own month arithmetic until its own sitting. Only checkpoints a
current tape carries run: the seventy years on the tochacha tape (2 Chronicles 36:21 by Megillah 11b-12a),
the seventeenth of Tammuz on the erection tape (day 47, Taanit 28b). The flood's 150 days (OPEN-4) run as
an ENGINE PROBE against the calendar function, not as a scene: the pre_sinai tape carries the flood's
oath, not its dates. Sub-day (hours, the named slots, the twilight doubt flag) is OUT — OPEN-5.

## 1. The base unit and the derived year (B, and round two's point 8)

- `Clock.day` is the counter — the only counter. `advance(to_day)` walks it one day at a time and fires
  every timer at its due (unchanged walker, world_engine.py). No set, no jump, no UNKNOWN value.
- `Clock.year` is DERIVED through the world's EPOCH ROW by the Calendar: `calendar.year(day)`; a world
  with no epoch declared has `year = None` — an honest "no era declared", never a guess (round two, 6).
- Log tuples carry the DAY as their second element (unchanged position, so the erection's `fires[0] == 47`
  reads as before); ledger entries carry BOTH `day` and `year`. A day-grain slot that read `entry['year']`
  as the counter is re-typed to `entry['day']` with that one explanation (the ledger's `year` is now the
  derived year, `None` in a world without an epoch); no graded value moves by it.
- Every daemon that read `world.clock.year` as the DAY counter (the day-grain runners: `due=day + 1`,
  `event.get('day', world.clock.year)`) now reads `world.clock.day` — a rename, not a literal move.
- A daemon that computed a due in YEARS (`world.clock.year + 6`, `yr + ytj`) now asks the Clock:
  `world.clock.after(n, 'year')` (the same date n years on — the servant's six, the tree's three, the
  debt's years) or `world.clock.at_year(y)` (the first day of the era's year y — the field's return at
  the jubilee, the release timer at the seventh). The year-grain scenes' `advance(N)` (N a year) becomes
  `advance(w.clock.at_year(N))`; their events no longer carry a `year` field — the value comes from the
  calendar instead of the script (the smuggled parameter retired, THE_CLOCK.md section 6).

## 2. The Calendar — an ENGINE construct over a DATA file (E, round two's point 2)

The period re-arm fires inside `advance()`, and the engine cannot import a runner (every runner imports the
engine): so the calendar function lives in world_engine.py as `class Calendar`, held by the Clock, reading
`World/step9/calendar_parameters.yaml` — the THIRD registry beside the event and effect registries. The
Calendar is the file's ONLY reader (the code/data law). No daemon is named "the calendar law": the boundary
timers are set by the daemons whose verses command the count, at the start event the ink names.

The mechanism from ink (code): Genesis 1:5's evening-then-morning (the day boundary — the calendar's day
ends at evening; OPEN-5 holds the Temple's day-then-night, Chullin 83a); Exodus 12:2's "this month is for
you the head of months" (month one); Leviticus 25:8's seven sabbaths of years, forty-nine (the cycle);
Leviticus 25:10-11's fiftieth year. The DATA rows (received / rounding / modeled / OPEN, each with channel,
source, and teacher): the four new years (Mishnah Rosh Hashanah 1:1 — a received table, not mechanism);
the month's length (Rosh Hashanah 25a:10, "thus I have received from my father's father's house: not less
than twenty-nine days and a half and two-thirds of an hour and seventy-three parts"); its rounding at the
day grain (months alternate thirty and twenty-nine — the half-day rounds to whole days; the parts'
accumulation is OPEN-6, settled on the tape by the court's declarations, Mishnah Rosh Hashanah 3:1, where
recorded); the intercalation ground (Sanhedrin 11b:5's three grounds, two of three; the equinox ground
alone modeled — Sanhedrin 13a:1 on Exodus 34:22 "the festival of ingathering at the turn of the year";
the recorded THRESHOLD Sanhedrin 13a:4 — the year is intercalated only if the season falls short by "most
of the month": sixteen days by the Sages, twenty by Rabbi Yehuda — two recorded settings); the solar year
(the season's length — see the parameters file for the shelf row); the regnal rounding (Rosh Hashanah 2b:1
"one day in a year counts as a year" — UNEXERCISED, no tape carries a reign); the count-start after entry
(OPEN-1 — Arakhin 12b:5 "seventeen jubilees Israel counted from when they entered until they went out, and
you cannot say they counted from the moment they entered", 13a:7-8 seven of conquest and seven of division
from Caleb's ages — two recorded settings: zero, the rows' own frame; fourteen, the historical tape); the
fiftieth year in the sabbatical cycle (Rosh Hashanah 9a:1 the Sages: "you count the fiftieth year and you
do not count the fifty-first", against Rabbi Yehuda "the fiftieth year counts for both" — Arakhin 12b:4;
two recorded settings, the period key `sabbatical`'s re-arm after a jubilee runs on it — UNEXERCISED: the
yovel scene runs one period); the jubilee's sanctification (Rosh Hashanah 8b:12 "the fiftieth year you
sanctify", the status from the first of the seventh month; the horn on the tenth — 8b:8, Leviticus 25:9).

The Calendar's API (the whole of it):
- `year(day)`, `date(day) -> (year, month, day_of_month)`, `day_of(year, month=1, dom=1)`,
- `next(day, key)` — the first boundary of `key` strictly after `day`: 'day', 'week', 'month', 'year'
  (the era's new-year month), 'sabbatical' (every seventh count-year), 'jubilee' (the fiftieth),
- `add(day, n, key)` — n units of `key` later, the same date (a calendar key moves under intercalation).
- The Clock wraps them: `clock.at_year(y)`, `clock.after(n, key)`, `clock.next(key)`, `clock.date`.

The ERA TABLE (D as amended — data now, code paths only where a tape exercises them): `eras:` rows in the
parameters file — `count` (Leviticus 25:8 "you shall count for yourself": day 0 = the first of the seventh
month of count-year 1; the new year at the seventh month, Mishnah Rosh Hashanah 1:1 — the five year-grain
worlds), `exodus` (Exodus 12:2; 40:17 "in the first month of the second year"; the new year at the first
month — declared, UNEXERCISED until the erection tape's own sitting), `life_years` (Genesis 7:11 "in the
six hundredth year of Noah's life" — UNEXERCISED), `regnal` (Rosh Hashanah 2b's rounding — UNEXERCISED),
`exile_greek` (Avodah Zarah 10a — UNEXERCISED). A world declares `World(era=..., epoch='count')`; the
day-grain worlds declare none. The unexercised rows are visible in the parameters lint the way an unfired
daemon is.

## 3. Timers: the period field and the close pairing (G)

- `period` on a timer effect is OPT-IN: absent means one-shot (every existing literal untouched); an
  INTEGER means that many days; a CALENDAR KEY re-arms through `calendar.next(due, key)`. The re-arm
  happens in `advance()` at the fire: the fired effect is written, then a new timer is appended at the
  next due and logged `('TIMER-SET', day, {..., 'rearmed_from': due})` — a chain the diff engine can
  count. The bound (section 4) rides the chain.
- A recurrence ENDS on a text event only — `cancel_timers(subject, effect, note)` when a daemon consumes
  the event that ends it (the tamid "taken away": Mishnah Taanit 4:6, Daniel 8:11-13) — never on a count.
- THE CLOSE PAIRING: a recurring DEBIT's discharging act must CLOSE the open entry — `world.close(eid,
  effect, note)` exists and no daemon called it. The erection's tamid: `tamid_offered` closes the altar's
  open `tamid_owed` before setting tomorrow's (Exodus 29:38-42 "day by day continually"); the investiture's
  tamid likewise (cold_run_incense_shekel.py). The tuples count effects, not open entries: no literal
  moves; the open ledger shrinks by the closed debits (printed, not graded).

## 4. Markers, the bound, the retrograde marker (C, round two's point 7)

- `world.marker(verse, day, value=None)` — a MARKER log class: `('MARKER', day, {'verse': verse, 'value':
  value, 'retrograde': bool})`; a marker at or after the counter walks `advance(day)` (nothing fires late);
  `advance()` stays public for the harness (day 47 is a timer's due, the scene's advance walks to it).
- THE BOUND: `submit()` stamps every event `bound = [last_marker_day, None]` (open); the next non-
  retrograde marker CLOSES the open bound on every event, timer, and ledger entry between; the engine
  copies the bound onto each effect during consumption (it knows the event through `_consuming`), onto
  each fire and each re-arm. No daemon touches it. `checkpoint(name, declared, computed, bound=None)`
  tests an interval when given one and prints the interval; against a still-open bound it tests
  `[lo, now]` and says so.
- THE RETROGRADE MARKER (Pesachim 6b:7 — "let it write of the first month first and then of the second
  month: Rav Menashya bar Tachlifa in the name of Rav: this tells us there is no earlier and later in the
  Torah"; Numbers 9:1 after 1:1): a marker EARLIER than the counter is logged with `retrograde: True`; the
  counter does not move; the world's `dated` is set to the stated day so the next event carries `dated`
  (the text's day) beside `day` (the counter) and NO bound; a daemon's timer computes its due from the
  stated day (`event.get('dated', world.clock.day)`) — a due already past writes at submission through
  `_write`'s existing immediate branch (due not greater than now writes at once), logged
  `('RETRO-WRITE', day, ...)`; checkpoints read `dated`. The tape in verse order, the clock monotone, the
  date the text's.

## 5. The jubilee: three layers, act-forked, three conditions (F as amended — round two's points 3, 4)

Both arms of the Sifra's dispute condition the jubilee's VALIDITY on an ACT performed in the fiftieth year
(Sifra Behar Chapter 2 4 — Rabbi Yehuda: a jubilee even though they did not release and did not sound the
horn, but not without the servants sent free; Rabbi Yose: even though they did not release and did not
send the servants, but not without the horn); a fire wakes no daemon; so the fork runs in the daemon that
consumes the act, never on a due.
1. THE COUNT'S TIMER writes the UNDISPUTED fact. `law_yovel` consumes `entered_the_land` (Leviticus 25:2
   "when you come into the land" — its own verse; the type already registered) and sets two recurring
   status timers on the land: `sabbath_of_the_land` (25:4 "a sabbath of the land", period 'sabbatical',
   first due the seventh count-year's first day) and `jubilee_year` (25:13 "this year of the jubilee",
   period 'jubilee', first due the fiftieth count-year's first day — sanctified from the New Year, Rosh
   Hashanah 8b:12). `land_sown` reads the LAND's status, not the event's year (the cascade through ledger
   state); the compiled `cycle()` cell still grades the arithmetic.
2. THE SALE'S TIMER writes the ENTITLEMENT: `goes_out_in_the_jubilee` (25:28 "it shall go out in the
   jubilee", 25:31, 25:33, 25:54) — a status on the field or the servant, due at the fiftieth year's first
   day, computed by the Clock at the sale.
3. THE RELEASE is written by `law_yovel` consuming `jubilee_proclaimed` (KEPT — Leviticus 25:9-10 the
   horn sounded and liberty proclaimed on the tenth of the seventh month, the text's own act; its `year`
   field retired — the day is the calendar's). The daemon reads THREE conditions: `horn_sounded` and
   `servants_sent_free` as the act's own fields (the Sifra's "even though they did not" rows), and ALL
   THE INHABITANTS as a STATE read off the ledger — Arakhin 32b:16 "from when the tribe of Reuben, the
   tribe of Gad and half the tribe of Manasseh were exiled, the jubilees ceased, as it is said 'proclaim
   liberty in the land to ALL its inhabitants' — when all its inhabitants are upon it, and not when some
   of them were exiled": the people's `scattered_among_nations` entry (written by law_tochacha consuming
   `people_exiled`, registered beside on the fork's world), never a scene field. The verdict per arm is a
   VALUE on `jubilee_release` (the land) and on each entitled holding's `returns_to_holding` / servant's
   `goes_free`: where the arms agree one entry, where they differ one entry per arm with the arm named —
   the "no jubilee" arm a named value, never a silence, never a fire. On the historical tape no
   proclamation is narrated: the engine writes the year and the entitlements and NO release — what the
   tradition records (Arakhin 32b).
- The library's `law_slave_term`: `slave_pierced` retires the `jubilee_year` field for a due computed by
  the Clock (`clock.next('jubilee')`) — the calendar instead of the script; `jubilee_proclaimed` cancels
  each freed servant's pending six-year timer (THE PENDING TERM, REPORT_WRAP_W5.md finding 1) and defers
  to the land's `jubilee_holds` status when a jubilee daemon registered before it has written one (the
  yovel scene's order), else the proclamation itself is the liberty (the skeleton's own scene).
- New effects, registered first under the effects law: `sabbath_of_the_land`, `jubilee_year`,
  `goes_out_in_the_jubilee`, `jubilee_holds` — the tradition's own vocabulary, each with its ink.

## 6. The fire-probes (written before the engine code; each expected to FAIL on the old engine)

World/step9/clock_probes.py: (1) the day counter and the derived year through an epoch; (2) `year` is None
with no epoch; (3) a calendar-key period re-arms and logs the chain; (4) an integer period; (5) a
recurrence ends by `cancel_timers` on a text event, never by count; (6) the bound stamped at submit,
closed by the next marker, inherited by the fire; (7) the derived year at an intercalated boundary (a
thirteen-month year exists under the modeled equinox ground and the year still increments at the new-year
month); (8) the retrograde marker — logged, counter unmoved, `dated` carried, a past due written at
submission; (9) the jubilee fork's three conditions on the act; (10) `after(6, 'year')` lands on the
same date six years on; (11) the flood's 150 days (Genesis 7:11 → 8:4) against the received month —
OPEN-4 expected to DIVERGE and say so; (12) the close pairing: a discharged recurring debit stands closed.

## 7. The re-type rule for the five year-grain scenes (print-then-type)

calendar, holiness_b, tochacha, yovel, mishpatim (and the engine's own `run()`): the world declares
`epoch='count'`; every `advance(N)` becomes `advance(w.clock.at_year(N))`; every `'year': N` field on a
submit is REMOVED (the registry's `fields` lines updated by script); the daemons read `world.clock.year`
and compute dues through the Clock. The TUPLE prediction is written by script from the calendar function
BEFORE each runner runs: the derived years must equal the old year literals (the same events at the same
count-years), the counts unchanged, the timers set and fired unchanged except where a move is explained
(THE PENDING TERM adds a cancel on the yovel tape; the count's two period timers add sets and fires on the
yovel tape). A miss is evidence, never a retype.

## 8. What stays OPEN (H), with its settler

OPEN-1 the count-start (Arakhin 12b-13a — a parameter with two recorded settings); OPEN-2 intercalation
before the fixed calendar (the equinox ground alone, modeled, labeled — the grain and fruit observations are
not on the tape); OPEN-3 conflicting markers (DIVERGE reports; no Prophets tape yet); OPEN-4 the flood's
thirty-day months (the probe's DIVERGE); OPEN-5 the two day boundaries (Chullin 83a); OPEN-6 the month's
parts beyond the half day (Rosh Hashanah 25a — settled on the tape by the court's declarations where
recorded); the fiftieth year in the sabbatical cycle (Rosh Hashanah 9a:1 against Arakhin 12b:4 — two
settings, unexercised). OPEN-7 (the sequential run's: which creation day is the first of Tishrei) SETTLED ON THE
SHELF at O1 (2026-09-07): Vayikra Rabbah 29:1 in Rabbi Eliezer's name — the world created on the twenty-fifth of
Elul, Adam on Rosh Hashanah; the creation era's row carries `day_one_offset` 5 (the plain reading of Rosh Hashanah
27a:15 the other setting, 0), and the Calendar lays a STUB MONTH before the first new-year month — Elul of year 0, its
start negative so that day 0 is its twenty-fifth; the world's own era view opens at the first new-year start and the
days before it read the calendar's year 0 (SEQUENTIAL_RUN.md section 12 e). Also O1's: a post-Exodus-12:2 month name
is addressed by the CALENDAR'S OWN numbering (Nisan 1, Tishrei 7), never by the creation era's ordinal — the ordinal
seventh from Tishrei is Adar II in a thirteen-month year; the sojourn fork's descent-literal world caught it.

## 9. As built (the sitting's close)

The engine: world_engine.py — Calendar (the third registry's only reader), Clock(day, epoch) with the derived `year`
and `date`, `at_year`, `after`, `next`; World(era, epoch) with `marker`, the bound stamp in `submit`, `day` + `year` (+
`dated`) on every ledger entry, `RETRO-WRITE`, the period re-arm in `advance`, `checkpoint(bound=)`; the library's
law_slave_term re-typed (the calendar dues, THE PENDING TERM cut, the deferral to `jubilee_holds`), law_installation's
counter read as the day. The registries: four effects added (246), `tamid_owed` timer → debit; twelve event entries'
`year` fields retired, the proclamation's three condition fields, the piercing's field retired, the tape lines current;
calendar_parameters.yaml born (18 rows, 5 eras; 6 unexercised rows visible). The runners: twenty-five day-grain renamed,
five year-grain re-typed on the count epoch, the yovel daemon carrying the count, the entitlement and the act-forked
release with the fork's three worlds as graded rows; the erection's close pairing. The gates: the daemon gate 248 / 0 / 7
of 255; the dependency gate 167 edges (yovel → tochacha filed, transfer, Arakhin 32b:16); the events lint 0; the probes
12/12 (0/12 before), the gate probes 5/5 and 12/12. Modeled and OPEN as section 8 lists; the fork's reach to Leviticus
27:21 and 27:24 filed OPEN (a direct timer at the fiftieth's arrival meanwhile). The account: REPORT_CLOCK.md.

THE SEQUENTIAL RUN's extension (2026-09-07, the next sitting; the design SEQUENTIAL_RUN.md section 2, the account
REPORT_SEQUENTIAL_RUN.md): an ERA is a view on the one month table — `Era(epoch_day, new_year_month)` set by a marker
(`world.marker(..., era=, new_year_month=)`), `clock.year_in / date_in / day_in` with ORDINAL months from the era's first
month; a LIFE era (no new-year month) turns at the New Year — its year is the calendar years' difference (Gen 8:13) and
"the Nth year of X's life" is the year of age N under the row `life_year_reading`; a third marker class, PROLEPTIC (a
paragraph's closing total: logged, the counter unmoved, no dated stretch); THE DATED DAY IS THE EVENT'S DAY inside a
retrograde stretch (`event.setdefault('day', dated)`); `World(registry=)` resolves scene tokens to the one registry's
entity ids at `entity()`; `law_installation` reads the event's day. A new era row `creation` and the data row
`life_year_reading`; the rows exodus and life_years now exercised.
