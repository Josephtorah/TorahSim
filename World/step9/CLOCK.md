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

## 10. O5 — THE MOADIM RE-TYPE (2026-09-07; the open-items campaign's fifth sitting; the plan: the state doc's compaction point #90)

Declared BEFORE the code. THE DEFECT: the appointed-times runner (cold_run_moadim.py) dates its own scene by hand —
`advance(178)` for the first of the seventh month, `advance(187)` for the tenth, `advance(192)`, `advance(199)` — month
arithmetic the runner did itself with the 30/29 lengths typed as comments ("the month lengths 30/29 the data channel"),
a world with NO epoch, and `day` fields on its case events (`'day': 16`, `'day': 65`, `'day': 192`) that the daemon read
as timer bases. The erection runner's three worlds are day-grain too: the Sinai world counts "day 7 + forty = day 47,
the seventeenth of Tammuz" by a relative count with `'day': 7`, `'day': 47`, `'day': 48` on its acts; the installation
world counts 23 Adar + 7 = 1 Nisan by hand. The era row `exodus` is exercised by the sequence alone.

THE RULE (THE_STEPS convention (12)): a FESTIVAL IS A CALENDAR KEY read from Leviticus 23's own dates, held in the third
registry as ink rows, and a scene walks to a festival by `clock.next(key)` — never by month arithmetic of its own; a
festival's recurrence ("an everlasting statute throughout your generations", 23:14, 23:21, 23:31, 23:41; the week of
23:3) is a PERIOD timer keyed by the festival, re-armed through the Calendar; an act's `day` is never a scene literal —
the daemon reads the clock (or the engine's `dated` day inside a retrograde stretch).

(a) THE DATA ROWS (calendar_parameters.yaml, exercised_by [moadim]): `festival_dates` — channel INK, the dates in the
calendar's own numbering (Exod 12:2 — Nisan the first), keyed by the convocation names the scene already uses so the
event's `day` value IS the key: passover {1, 14} (23:5 "in the first month, on the fourteenth of the month, between the
evenings"); passover_1 {1, 15} (23:6 "on the fifteenth day of this month", 23:7 "on the first day a holy convocation");
passover_7 = passover_1 + 6 (23:8 "on the seventh day" of 23:6's seven); atzeret = omer + 49 (23:15-16 "seven complete
weeks... until the morrow of the seventh Sabbath you shall count FIFTY days" — the omer day counted first, the fiftieth
sanctified: the runner's own count_length); rosh_hashanah {7, 1} (23:24); yom_kippur {7, 10} (23:27); sukkot_1 {7, 15}
(23:34); shemini = sukkot_1 + 7 (23:36 "on the eighth day"); sabbath → the Calendar's own `week` key (23:3 "six days...
on the seventh day"). And `omer_day` — channel RECEIVED: 23:11 "on the morrow of the SABBATH" read as the morrow of the
FESTIVAL, the sixteenth of the first month (Sifra Emor Chapter 12; Menachot 65a-66a; the runner's OM['morrow_reading']
= 'festival' graded on Mishnah Chagigah 2:4), with the refused setting beside it (the Boethusians' Sunday, Menachot 65a).

(b) THE ENGINE (world_engine.Calendar): the festival keys read from the rows beside the six standing keys; a row of the
form {month, day} resolves by `day_of(y, m, dom)`, a row {from, plus} by the named key's day plus the ink's count, a row
{key: week} by the week; `next(day, key)` for a festival key is the first occurrence strictly after `day` — this year's
if still ahead, else next year's; an unknown key still refuses, naming the keys. `advance()`'s re-arm already takes a
string period through `calendar.next` — nothing changes there.

(c) THE DAEMON (law_moadim): a holy convocation proclaimed writes what it wrote (the class, the sanctity, the rest) AND
sets the festival's PERIOD timer — `sanctify_day` on the people, value the day's name, due the next occurrence, period
the key (the week for the Sabbath) — the recurrence the ink commands "throughout your generations"; the omer's count and
the booths' seven days stay DAY timers from the clock (23:16's fifty, 23:42's seven — the ink's own numbers), their
`day` fields retired; the two loaves' `day` retired. The registry's fields lines follow (omer_brought, two_loaves_brought,
booths_dwelt) by script.

(d) THE SCENE (moadim): `World(..., epoch='exodus')`; the Sabbath on the seventh day of the year (`day_of(1, 1, 7)` —
the scene's own anchor, as before); then `advance(clock.next('passover'))`, `next('passover_1')`, `next('omer')`,
`next('passover_7')`, `next('atzeret')` (the omer's timer fires that day), `next('rosh_hashanah')`, `next('yom_kippur')`,
`next('sukkot_1')`, `next('shemini')` (the booths' timer fires that day). Not one month length in the runner.

(e) THE ERECTION on the epoch: the installation world declares `epoch='exodus'` and dates itself from the ink — the
erection at `day_of(2, 1, 1)` (Exod 40:17 "in the first month of the second year, on the first of the month"), the
take-list SEVEN DAYS BEFORE it (Lev 8:33's seven, 9:1's eighth — the same shape as the second ascent = Yom Kippur − 40),
the first Sabbath's bread at `day_of(2, 1, 7)`; the Sinai world declares the epoch too — the covenant day 1 Sivan
(`day_of(1, 3, 1)`, Shabbat 86b:5 as the sequential run dates it), the ascent 7 Sivan (24:16), the breaking at the
timer's own fire (7 Sivan + 40), THE SECOND ASCENT BY THE ROW `second_tablets_given` − 40 (the O1 dating, now on the
erection's own world too — the row exercised by [sequence, erection]), the second tablets firing on Yom Kippur; the
`day` fields on moses_ascended and tablets_broken retired (the daemon already reads `event.get('day', clock.day)` — the
engine sets `day` inside a retrograde stretch, the scenes stop typing it). The W7 tuple gains TWO DATE SLOTS: the
calendar date of the first fire and of the last — the seventeenth of Tammuz and the tenth of Tishrei COMPUTED, not
counted. The craftsmen's world stays undated (day-grain).

(f) THE PROBES (clock_probes.py 13-16, written first; 12/12 stand): 13 the festival keys resolve from the row on the
exodus epoch (yom_kippur = day_of(1,7,10); passover_7 = day_of(1,1,21); shemini = day_of(1,7,22); atzeret = the omer +
49; after Yom Kippur the next is year 2's); 14 a period timer keyed sukkot_1 re-arms to year 2's fifteenth of the
seventh month with the TIMER-SET chain; 15 the ink's count meets the date — the omer + 49 = the Calendar's atzeret =
the sixth of the third month under the modeled lengths; 16 an unknown festival key refuses, naming the keys (a guard —
it passes on the old engine too). Expected against the unchanged engine 13/16; after the code 16/16.

THE PREDICTIONS, computed by script from the Calendar BEFORE the runners run (scratchpad o5_predict.py), typed here
from the arithmetic the script must reproduce: year 1 of the exodus epoch has twelve months (the modeled season ground
lays no thirteenth), so 1 Nisan = day 0, 14 Nisan = 13, the omer 15, the fiftieth 64, 1 Tishrei 177, Yom Kippur 186,
Sukkot 191, the eighth day 198; 1 Nisan of year 2 = 354, 7 Nisan 360; 1 Sivan 59, 7 Sivan 65, 17 Tammuz 105, 29 Av 146.
THE MOADIM TUPLE: the Sabbath's week period set on day 6 fires 27 times within the year (13, 20, ... 195), each fire
re-arming; the seven festival periods set once, none firing (their next occurrence lies in year 2): sanctify_day on
israel 8 → 35, timers set 2 → 37, fired 2 → 29, the clock 199 → 198, every other slot unchanged — (1, 1, 8, 35, 5, the
eight classes, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 37, 29, 198). THE ERECTION TUPLES: the installation world's
clock 13 → 360, its five fires unchanged; the Sinai world's first fire 47 → 105, its clock 88 → 186, its three sets and
three fires and thirty-two events unchanged, the two new date slots (1, 4, 17) and (1, 7, 10); the craftsmen's world
unchanged. The sequence tape UNCHANGED (the stitcher drops the erection's `day` fields already; no moadim row is
history) — the recorder and the stitcher rerun to prove it. The registry: 20 → 22 rows (festival_dates INK, omer_day
RECEIVED); the era row exodus exercised_by [sequence, moadim, erection]; the row second_tablets_given by [sequence,
erection]. The gates unchanged (the daemon gate's parser reads the same literal submits; five `day` fields leave the
registry's fields lines); the sweep 34/34 at 3,633; the hash unmoved.

AS RUN (O5's close). The probes 13/16 against the unchanged engine (13, 14, 15 FAIL — the keys unknown; 16 the guard passes
either way), 16/16 after the Calendar's festival keys. THE PREDICTIONS BY SCRIPT (scratchpad o5_predict.py) reproduced the
arithmetic typed above to the day — year 1 twelve months, the fiftieth on the sixth of the third month (day 64), the eighth
day 198; the erection 354, the take-list 347, the bread 360; the breaking 105 = (1, 4, 17), the second ascent 146 = (1, 5,
29), Yom Kippur 186 — and the ink's counts met the keys inside the script (the omer + 49 = atzeret, sukkot + 7 = shemini,
the morrow to the second ascent forty days). THE RUNS: moadim 42/42 FIRST RUN with the predicted tuple (1, 1, 8, 35, 5,
the eight classes, ..., 37, 29, 198) — the Sabbath's period fired 27 times (13, 20, ... 195), the seven festivals armed for
year 2 at (2, 1, 15), (2, 1, 21), (2, 3, 6), (2, 7, 1), (2, 7, 10), (2, 7, 15), (2, 7, 22); erection 287/287 FIRST RUN with
(..., 5, 360) and (..., 3, 3, 105, 32, 186, (1, 4, 17), (1, 7, 10)) — the seventeenth of Tammuz and the tenth of Tishrei
read off the Calendar. TWO CORRECTIONS beside the declaration: the registry is 22 → 24 rows, not 20 → 22 (the
prediction miscounted the standing rows — the census prints 24: ink 8, received 13, modeled 2, rounding 1); and the
sequence tape's EVENTS are unchanged as declared, but its CENSUS moved — re-based 3 → 0, because the three `day` fields
the stitcher used to drop (the erection's ascents and the breaking) no longer exist to drop; the stitcher's count typed,
the sequence runner 7/7 with every verdict as before. The events lint 0 (the five fields retired); the daemon gate 244 /
0 / 0; the dependency gate satisfied; the sweep 34/34 at 3,633 (scratchpad sweep_o5.txt, SWEEP-EXIT 0); CORPUS TRUTH
GREEN, hash 8b8fff1fa28953af unmoved. The parameters census: 24 rows, eras 6; unexercised regnal_rounding,
fiftieth_in_cycle, era:regnal, era:exile_greek (as before — the exodus era now exercised by sequence, moadim, erection).

## 11. O6 — THE FORK'S REACH TO LEVITICUS 27:21 AND 27:24 (2026-09-07; the open-items campaign's sixth sitting; the plan: the state doc's compaction point #90)

Declared BEFORE the code, after the shelf was read by script. THE OPEN ITEM (section 5's own note in the runner):
the consecrated field's going out — 27:21 וְהָיָה הַשָּׂדֶה בְּצֵאתוֹ בַיֹּבֵל ("and the field, in its going out in the
jubilee, shall be holy to the LORD, as the devoted field; to the priest shall be its holding") and 27:24 בִּשְׁנַת
הַיּוֹבֵל יָשׁוּב הַשָּׂדֶה ("in the year of the jubilee the field shall return to him from whom he bought it") — ran as
TIMERS to the fiftieth (`due_to_priest`, `returns_to_holding` due `clock.next('jubilee')`), fired by the date alone,
while the sold field and the sold man of Leviticus 25 wait on the PROCLAMATION's fork. The question: do the three
recorded conditions govern the consecrated field too?

THE READING (every row resolved on the local shelf by script — the Mishnah, Sifra and Babylonian files):
(a) THE THIRD CONDITION REACHES 27:21 — TAUGHT. Arakhin 29a:15-17, a baraita: אֵין עֶבֶד עִבְרִי נוֹהֵג אֶלָּא בִּזְמַן
    שֶׁהַיּוֹבֵל נוֹהֵג ("the Hebrew slave applies only when the jubilee is in effect" — 25:40), the field of the holding
    likewise from 25:28 "it shall go out in the jubilee", the walled-city houses from 25:30; and RABBI SHIMON BEN
    YOCHAI on our clause itself:
    אֵין שְׂדֵה חֲרָמִין נוֹהֲגִין אֶלָּא בִּזְמַן שֶׁהַיּוֹבֵל נוֹהֵג ("devoted fields apply only when the jubilee is in effect")
    שֶׁנֶּאֱמַר וְהָיָה הַשָּׂדֶה בְּצֵאתוֹ בַיֹּבֵל ("as it is said: and the field in its going out in the jubilee" — 27:21). What "in effect" means is the standing condition: Sifra Behar Chapter 2 3 and
    Arakhin 32b:16 — לְכָל יֹשְׁבֶיהָ ("to ALL its inhabitants", 25:10): when all are upon it, and not when some were
    exiled; the jubilees ceased with Reuben, Gad and half of Manasseh. So with the exile on the people's ledger, the
    consecrated field's going out does not run: no priest's due, no return — the entitlement stands unreleased.
(b) THE FIRST AND SECOND CONDITIONS REACH IT BY REFERENCE. 27:21 בַיֹּבֵל ("in the jubilee") and 27:24 בִּשְׁנַת
    הַיּוֹבֵל ("in the year of the jubilee") NAME the institution whose validity the proclamation's fork decides — יוֹבֵל
    הִוא ("it is a jubilee", 25:10-12, the word both of the Sifra's arms read); the clause calls the definition, no
    rule crosses: a REFERENCE under the link review law, licensed by the ink alone (the shared content lemma יובל
    "jubilee" at 25:10-13 and 27:21, 27:24). Its timing is the Sifra's: Behar Chapter 2 1, Rabbi Yochanan ben Beroka —
    the fields did not return to their owners until the Day of Atonement arrived; הִגִּיעַ יוֹם הַכִּפּוּרִים תָּקְעוּ
    שׁוֹפָר חָזְרוּ שָׂדוֹת לְבַעֲלֵיהֶם ("the Day arrived — they sounded the horn, the fields RETURNED to their owners") —
    the release ON THE ACT. And Rosh Hashanah 9b:2-3 = Sifra Behar Chapter 2 4: both arms hold a jubilee אַף עַל פִּי
    שֶׁלֹּא שָׁמְטוּ ("even though they did not release" the fields) — the fields' release is an ACT the year commands,
    never a condition of the year.
(c) THE GOING-OUT'S OWN FORK, read at 27:20-21 (new rows). Mishnah Arakhin 7:4 = Sifra Bechukotai Chapter 11 2:
    הִגִּיעַ הַיּוֹבֵל וְלֹא נִגְאֲלָה ("the jubilee arrived and it was not redeemed") — Rabbi Yehuda: the priests enter it
    and PAY its value (the Sifra's ground, Chapter 11 1: "holy" here as "holy" at 27:14 — it goes out only by
    redemption); Rabbi Shimon: they enter and do not pay; Rabbi Eliezer: they neither enter nor pay — נִקְרֵאת שְׂדֵה
    רְטוּשִׁים עַד הַיּוֹבֵל הַשֵּׁנִי ("it is called an ABANDONED FIELD until the second jubilee"), and again until the
    third; the priests never enter until ANOTHER redeems it. Rabbi Eliezer's ground by Rava, Arakhin 26a:16: בְּצֵאתוֹ
    מִיַּד אַחֵר ("in its going out — from the hand of ANOTHER"): 27:20 וְאִם מָכַר אֶת הַשָּׂדֶה לְאִישׁ אַחֵר ("and if he sold
    the field to another man") precedes 27:21's going out — where the treasurer sold it to another, every arm agrees
    it goes out to the priests. The receiving priests: Arakhin 28b:4 — נוֹתְנָהּ לַמִּשְׁמָר שֶׁפָּגַע בּוֹ יוֹבֵל ("he gives it
    to the WATCH the jubilee met"). Mishnah Arakhin 7:3 (Arakhin 25a:16-17; Sifra Bechukotai Chapter 11 3): redeemed by
    the OWNER — it does not go out from his hand; by his SON — it goes out to his father in the jubilee (the heir
    adds the fifth with the sanctifier, Sifra Bechukotai Chapter 10 11 "to include the heir"); by ANOTHER and the
    owner redeemed it from his hand — it does not go out (the Mishnah file's text; the Talmud's Mishnah at 25a:16
    reads "it goes out to the priests" — the variant recorded beside, not graded); by a PRIEST —
    לֹא יֹאמַר הוֹאִיל וְהִיא יוֹצְאָה לַכֹּהֲנִים בַּיּוֹבֵל ("let him not say: since it goes out to the priests in the jubilee")
    וַהֲרֵי הִיא תַּחַת יָדִי הֲרֵי הִיא שֶׁלִּי ("and it is under my hand, it is mine") — it goes out to all his brother priests (27:21's
    אֲחֻזָּתוֹ "HIS holding" — a holding of his own, and this is not his: Arakhin 25b:14-16). Mishnah Arakhin 7:5
    (Arakhin 26b:14-16; Sifra Bechukotai Chapter 11 4): the field bought from his father — the father died, then he
    consecrated it: a field of the holding; he consecrated it, then the father died: a purchased field (Rabbi Meir) /
    a field of the holding (Rabbi Yehuda and Rabbi Shimon — 27:22's "which is not of the field of his holding" excludes
    a field not FIT to be a holding, and this one is fit); and the closing rule,
    שְׂדֵה מִקְנָה אֵינָהּ יוֹצְאָה לַכֹּהֲנִים בַּיּוֹבֵל ("a purchased field does not go out to the priests in the jubilee")
    שֶׁאֵין אָדָם מַקְדִּישׁ דָּבָר שֶׁאֵינוֹ שֶׁלּוֹ ("for a man does not consecrate what is not his") — 27:24's return, the ink's own clause.

THE RULE (THE_STEPS Step 5, motion (6)'s clock sentence): a clause that names an institution's year — "in the
jubilee", "in the year of the jubilee" — is a REFERENCE to that institution's verdict: the timer to the year writes
the ENTITLEMENT, the act's daemon writes the RELEASE on the fork's arms, and the shelf's "applies only when the
jubilee is in effect" (Arakhin 29a) is the exile's reach, taught. No consecrated field goes out by the date alone.

THE CODE (cold_run_yovel.py, law_yovel — no engine edit, no new import edge):
(i) `field_consecrated` writes the ENTITLEMENT: `goes_out_in_the_jubilee` on the field, due `clock.next('jubilee')`,
    its VALUE the route the ink and the rows give — to_the_priests (27:21, the holding unredeemed);
    to_the_priests_from_the_hand_of_another (27:20-21, the field `sold_to_another`); to_him_from_whom_he_bought_it
    (27:24, the purchased field); to_his_father (7:3, `redeemed_by: son`); to_all_his_brother_priests (7:3,
    `redeemed_by: priest`); and NO entitlement for the owner's redemption or the owner's re-redemption from another
    (7:3 — the field does not go out). The fifth on the owner and on the heir (7:2; Sifra Bechukotai Chapter 10 11),
    on no one else. The `due_to_priest` and `returns_to_holding` timers RETIRE from this branch.
(ii) `jubilee_proclaimed`'s release loop, on every arm that HOLDS, routes each entitled field by its value: the
    purchased field and the son's field → `returns_to_holding` (27:24 to him from whom he bought it — Sifra
    Bechukotai Chapter 11 7, never to the treasurer; 7:3 to his father); the priest-redeemed field → `due_to_priest`
    to all his brother priests; the field from the hand of another → `due_to_priest` to the watch the jubilee met,
    one entry, the arms agreed; the holding UNREDEEMED → THE 7:4 FORK as values on `due_to_priest` (Rabbi Yehuda —
    the priests enter and pay: `pays` by the priests to the treasury, its value; Rabbi Shimon — enter, no payment;
    Rabbi Eliezer — no entry: `abandoned_field` written on the field and the ENTITLEMENT RE-ARMED to the next jubilee,
    "until the second jubilee"), each value carrying the holding arm's name beside its own. On no arm holding (the
    exile — (a)): nothing on the field; the land's verdict names the arm, the entitlement stands.
(iii) NEW EFFECT, registered first: `abandoned_field` (שְׂדֵה רְטוּשִׁים "an abandoned field", Mishnah Arakhin 7:4; ledger
    op status; its ink 27:20 לֹא יִגָּאֵל עוֹד "it shall not be redeemed again" — Rabbi Eliezer's ground by Abaye at
    Arakhin 26a:5 and by Rava at 26a:16). NEW FIELDS on `field_consecrated`: `redeemed_by` (owner / son / another /
    priest / another_then_owner) and `sold_to_another` (27:20's clause).
(iv) THE DAEMON DECLARED FIRST (daemon_dispositions.yaml): field_consecrated → [gives_fixed_sum, adds_fifth,
    goes_out_in_the_jubilee]; jubilee_proclaimed → [jubilee_holds, jubilee_release, returns_to_holding, goes_free,
    due_to_priest, pays, abandoned_field, goes_out_in_the_jubilee]; the gate run to FAIL on the unchanged code.
(v) THE CELLS graded (thirteen new rows): the five routes (27:21, 27:24, 27:20-21 with Arakhin 26a:16), the four
    7:3 rows, the 7:4 arms, the two 7:5 rows, the in-effect reach (Arakhin 29a:17), the watch (28b:4), the release
    on the act (Sifra Behar Chapter 2 1). The answer sheet gains Mishnah Arakhin 7:3, 7:4, 7:5 and the Sifra/Talmud
    rows above, each verified by a token in its own ink. The scene gains four fields at count-year 44: sold to
    another (field-7), redeemed by the son (field-8), redeemed by a priest (field-9), redeemed by another and then
    the owner (field-10); the fork's three worlds each consecrate one field (field-c).

THE PREDICTIONS (scratchpad o6_predict.py — the standing literals parsed from the runner, the declared deltas applied,
the new literals printed BEFORE the runner is typed): the main scene's slot 35 (field-4's `due_to_priest` years)
[50] → [50, 50, 50] (the three arms at the proclamation); timers set 20 → 24 (three new entitlements + Rabbi
Eliezer's re-arm), fired 17 → 20 (the three new entitlements at the fiftieth's first day; the re-arm waits for the
hundredth); ten slots APPENDED: field-4's entitlement entries 1, the priests' `pays` 1, field-4's `abandoned_field`
1, field-7's `due_to_priest` [50], field-8's `returns_to_holding` [50], the father-sanctifier's fifth [25] (the
heir's, bid 20 → 25), field-9's `due_to_priest` [50], the priest-redeemed sanctifier's fifth 0, field-10's
entitlement 0 and `due_to_priest` 0; every other slot unchanged. The fork tuple gains four slots: field-c's
`due_to_priest` count 3 (wa: the holding arm × the 7:4 arms), 3 (wb), 0 (wc — the exile), and field-c's entitlement
standing on wc 1. Tests 77 → 90; the guard's count follows. The sweep 34/34; the registry 247 effects; the daemon
gate 244 / 0 / 0; the hash unmoved.

AS RUN (O6's close). The shelf read by script first (the Mishnah, Sifra and Babylonian files; the whole Babylonian shelf
searched for the "in effect" phrase — Arakhin 29a alone carries it for the fields). The daemon declared first: the gate
failed the two declared ways on the unchanged code (jubilee_proclaimed's and field_consecrated's watches ≠ the parse),
then — after the code — flagged THREE MORE, honestly: `going_out`, `arrival_unredeemed` and `field_kind_by_father` are
top-level functions writing effects and were laws to the gate (the W3 lesson); dispositioned WRAPPED by law_yovel, the
census 244 → 247 of 247. The registries before the code: `abandoned_field` the 247th effect (its ink לֹא יִגָּאֵל עוֹד
"it shall not be redeemed again" machine-verified at 27:20 alone in the chapter), the two fields on field_consecrated,
the tape lines rewritten; the events lint 0. THE PREDICTIONS BY SCRIPT (scratchpad o6_predict.py) exactly as typed
above; THE RUN: 90/90 FIRST RUN, both tuples as printed — field-4's three arms at the proclamation's year, the priests'
payment once, the abandoned field once, the re-armed entitlement pending at day 36,156 (the hundredth count-year, the
Calendar's), field-7 one entry, field-8 to his father with the heir's twenty-five, field-9 to all his brother priests,
field-10 nothing; the fork's consecrated field 3 / 3 / 0 with its entitlement standing on the exile's world. The answer
sheet 42 Mishnah rows + 29 Sifra/Talmud rows, each verified by a token in its own ink. THE GATES AND THE SWEEP: DEPENDENCY
GATE satisfied (162 live; 231 + 72 — no new edge); DAEMON GATE 247 / 0 / 0 of 247, unfired 0, unconsumed 0, open aliases
0; the probes 5/5 + 11/11 + 12/12 + 8/8 + clock 16/16 + sequence 4/4; THE SWEEP 34/34 at 3,646 (scratchpad sweep_o6.txt,
SWEEP-EXIT 0); CORPUS TRUTH GREEN, hash 8b8fff1fa28953af UNMOVED. One correction beside the declaration: none — the
counts held; one addition: the three function dispositions the declaration had not foreseen.
