# SEQUENTIAL_RUN.md — THE SEQUENTIAL RUN: the three books on ONE world of the law engine (2026-09-07)

The owner's ruling (the state doc, after THE CLOCK SITTING; compaction point #88 the plan): "are the first three books
done to the point that we can run them in sequence" — not as one run on the law engine: the narrative world folds every
frozen unit in canonical order, but the 38 daemons ran on 33 separate test worlds, each narrative stretch in its own
world. So, BEFORE NUMBERS: the three books in verse order on ONE world — the test of the whole; its lessons shape
Numbers' wraps. The order of work is the wrap's: this design FIRST; the fire-probes SECOND (World/step9/
sequence_probes.py, written to fail against the unchanged engine); the engine extension THIRD; the stitching script and
the tape runner FOURTH (World/step9/cold_run_sequence.py, the sweep's 34th runner); the gates, the sweep and the records
FIFTH (REPORT_SEQUENTIAL_RUN.md, COMPILE_DEBT, THE_STEPS — a process upgrade, THE_BRIEFING, the state doc, memory).
Every number below that the ink supplies was PARSED FROM THE INK by script at this sitting (the numeral parser of
section 4) and every citation resolved on the local shelf by script (scratchpad shelf_find.py — its lesson: some
tractate files are VOCALIZED; a substring search strips nikud or reports a false "not found").

## 0. What runs, and what stays off

ON the tape: every event the existing scenes submit that is HISTORY — the registry's own form (act / speech / statute),
sourced to a verse of the three books, at a narrative verse by the ink's own grammar (section 3). OFF the tape: every
CASE ROW (the Mishnah's rows, the sugyot's exemplars — the exam is a test, not history), and every act the scenes
sourced to a tractate. The exam's rows stay in their own worlds (the 33 runners are unchanged; the sequence runner
imports them and registers their daemons). The count epoch (the jubilee) is the ENTRY into the land — not on this tape:
law_yovel is registered and never fires; the zero-report law's instrument prints it. Sub-day stays OUT (OPEN-5).

## 1. The one world and its epoch

`World(era='THE SEQUENTIAL RUN — the three books on one world (clock unit: days; the creation epoch)', epoch='creation')`.
A NEW era row `creation` in calendar_parameters.yaml: day 0 = the first day of the world's first month — the seventh
month (Tishrei) by Rabbi Eliezer, "in Tishrei the world was created" (Rosh Hashanah 10b:10 the baraita; 11a:3 his
derivation from Genesis 1:11 "let the earth sprout"; 8a:15 Rav Chisda's season by him; 27a:15 "as whom do we pray today
'this day is the beginning of Your works, a memorial of the first day'? — as Rabbi Eliezer"); the other setting Rabbi
Yehoshua's, "in Nisan the world was created" (11a:1; 11a:4 from Genesis 1:12 "and the earth brought forth") — recorded,
UNEXERCISED. OPEN-7: WHICH creation day is the first of Tishrei — the shelf's 27a:15 read plainly puts "the first day"
there (day 0 = day one, Genesis 1:5); the later reading that sets Adam's creation on the New Year is NOT on the local
shelf — held as the plain reading, labeled. The seasons: equinox_offset_days 0 aligns the autumn equinox with day 0
(modeled, OPEN-2 — the same alignment the count epoch runs).

The derived year `clock.year` is the creation era's. The tradition's own anno-mundi count (Seder Olam, not on the local
shelf) runs one year lower than this machine's creation-year under the completed reading of section 2 — it counts Adam's
first year as year 0; printed as a remark, never a checkpoint.

## 2. THE ENGINE EXTENSION — eras as counters set by markers

The world's MONTH TABLE is the physics (one moon; the Calendar of THE CLOCK SITTING lays it from the epoch, thirty and
twenty-nine alternating, the thirteenth month by the season ground). An ERA is a VIEW on it: `(epoch_day, new_year_month)`
— its year turns at the first day of its new-year month after the epoch; its months are counted ORDINALLY from its
new-year month. Before Exodus 12:2 names month one, the ink's "second month" (Genesis 7:11) counts from the era's first
month — Rabbi Eliezer's seventeenth of Marcheshvan (Rosh Hashanah 11b:7) and Rabbi Yehoshua's seventeenth of Iyar (11b:6)
fall out of the ONE parameter (the creation era's new-year month), both printable. After Exodus 12:2 the exodus era's
ordinal months count from Nisan (Rosh Hashanah 3a:5 — Exodus 40:17 "the first month of the second year" and Numbers
10:11 "the second year, the second month": Nisan and Iyar in one year, the new year for the exodus count is Nisan).

- `Clock.eras`: `{name: Era}`; `Era(epoch_day, new_year_month)`; `clock.year_in(name)`, `clock.date_in(name)` →
  `(year, ordinal_month, day_of_month)`, `clock.day_in(name, y, m, dom)`; the world's own era is `eras['creation']`
  (epoch_day 0), and `clock.year` / `clock.date` read it (the API of THE CLOCK SITTING unchanged).
- A LIFE era (`new_year_month` None — the row `life_years` of the parameters file, now EXERCISED): its year turns on the
  birthday's anniversary [CORRECTED AT THE SITTING before the tape ran: the life-year turns at the NEW YEAR — Genesis 8:13's
  "601st year, first month, first day" follows 7:11's "600th year, second month, seventeenth" by ten and a half months;
  the age is the calendar years' difference; the day of a birth within its year is modeled at the year's first day
  (Rosh Hashanah 10b:10) — section 11 and REPORT_SEQUENTIAL_RUN.md finding 3]. THE TWO IDIOMS (OPEN-8): "X was a son of N years" = N completed (Genesis 12:4, 16:16, 17:1,
  17:24-25, 21:5, 25:26 — the chain 86 + 13 = 99 closes on it); "in the Nth year of X's life" (7:11) — the RUNNING
  setting reads it as N completed too, because the ink's own witnesses agree with that reading (7:6 "Noah was a son of
  six hundred years and the flood came"; 9:28-29 "three hundred and fifty years after the flood... all his days nine
  hundred and fifty"); the strict ordinal reading (N − 1 completed) is the other setting, its numbers printed beside.
- THE MARKER'S THREE CLASSES: FORWARD (walks the counter, closes every open bound — THE CLOCK SITTING); RETROGRADE
  (earlier than the counter: logged, the counter unmoved, the following events `dated` — Pesachim 6b:7, "there is no
  earlier and later in the Torah", read on the shelf); and NEW, PROLEPTIC: a paragraph's CLOSING TOTAL — "all the days of
  X were N years, and he died" (Genesis 5:5, 5:8, ..., 9:29, 11:32, 25:7, 25:17, 35:28, 50:26) — is the text's summary
  of a life, placed by the text before the next paragraph opens at an EARLIER time; it is logged at its computed day
  with `proleptic: True`, the counter unmoved, NO dated stretch opened (nothing follows it in its own paragraph). The
  rule is uniform: a begetting or an age-at-event is a clock stamp; a lifespan total is a closing stamp. Without it
  Genesis 5 would be a chain of retrograde stretches and the derived year would stand at Adam's death through Seth's
  begetting — the wrong picture.
- `world.marker(verse, day, value=None, era=None, new_year_month=None, proleptic=False)`: `era` names an era whose
  epoch the marker SETS at `day` (Exodus 12:2 sets `exodus`; a birth sets `life:<entity>`); THE ERA COUNTER IS SET BY A
  MARKER, NEVER BY A LITERAL DAY.
- THE DATED DAY IS THE EVENT'S DAY: inside a retrograde stretch an event that carries no `day` of its own receives
  `day = dated` from the engine at submit, so every daemon that reads the event's day (`event.get('day',
  world.clock.day)` — the day-grain runners' idiom) reads the text's date. The library's `law_installation` reads the
  event's day the same way (a library edit: the five fire-probes rerun, the skeleton rerun).
- THE ONE WHO-IS-WHO AT THE ENGINE: `World(..., registry=<token → id>)` — `entity(eid)` resolves a scene token to the
  registry's entity id (`cancel_timers` resolves both sides). The map is read from logic/corpus/entity_registry.yaml —
  the one registry, never a second: its members carry the scene tokens with `units: [step9-scenes]`. The 33 runners'
  worlds pass no map (unchanged).

## 3. THE TAPE — stitched by script

(a) THE RECORDER (scratchpad seq_record.py): every runner imported with `World.submit / advance / close / cancel_timers`
instrumented, so each scene's events are captured with their full literal values (the loops expanded at runtime) and
attributed to the runner whose scene submitted them (the first cold_run_*.py frame on the stack — a leaf caller's import
of another runner is attributed to the callee). The five runners whose scenes run under `main()` alone (guardians,
negaim, pesach, vayikra5, yoma) are re-run explicitly. MEASURED: 33 modules, 0 failed; 741 submits, 875 records.

(b) THE FILTER — three tests, each computed, the census printed by runner:
  1. FORM — the registry's own (event_vocabulary.yaml): act (59 types) / speech (30) / statute (1) stay; case (176) is
     the exam. 584 case-row submits off.
  2. SOURCE — the submit's `case_source` cites a verse of Genesis, Exodus or Leviticus FIRST; an act sourced to a
     tractate is a case dressed as an act. Seven off, named: the two strangers at the incense altar (2 Chronicles 26,
     Numbers 16 — other books), the convert's rite (Keritot 9a), the worshipped calf (Mishnah Avodah Zarah 4:4), the
     unrepentant and the vain swearer (Yoma 86a), the silent resolver (Shevuot 26b).
  3. REGISTER — THE WAYYIQTOL TEST off the Tanakh DB's own morphology (elijah_docket/tanakh.sqlite, the OSHB code with
     the consecutive-imperfect marker — the "and he did" form the registry's act definition names): an ACT needs a
     non-speech wayyiqtol in its cited verse or the one before (Genesis 17:24's age note carries 17:23's "and he took";
     Leviticus 24:2's "and the LORD spoke" is a speech frame, not an act — the three priesthood rows at Leviticus 21:10,
     24:2, 24:5 are law clauses dressed as acts: OFF); a SPEECH needs any wayyiqtol within the three verses before
     (Genesis 17:10's command is framed by 17:9 "and God said"; 9:11 by 9:8; 49:3 by 49:1); the STATUTE by its form
     (Genesis 32:33, the narrator's own law sentence). Measured at the design: the test fires on the samples as stated.
  The corpus world's own events table was tried first and covers Genesis and Exodus 1-20 only (436 verses) — the
  morphology test covers every verse.
  EXPECTED HISTORY: 150 − 3 = 147 events from nine runners (pre_sinai 25, family 25, erection 38, sanctuary_build 17,
  vestments 11, incense_shekel 17, shemini_day 11, tzav 3, priesthood 0). The stitcher prints the number; the runner
  grades it.

(c) DEDUP — exact (kind, subject, verse) repeats ACROSS runners are one act: Leviticus 8:2 `installation_commanded`
and 8:30 `milluim_blood_sprinkled` on `aaron-and-sons` from tzav, shemini_day and erection → one each (4 removed; the
tape's first in canonical runner order kept). Repeats WITHIN a runner are the ink's own (Exodus 36:3 "morning by
morning" — two mornings; 39:28's two garments). ONE ACT, TWO SUBJECTS is KEPT and reported: Leviticus 8:30 on `aaron`
(incense_shekel) and on `aaron-and-sons` (the library's tape) — the open alias of D9-i's seeding ("Lev 8:30 + 8:31-32
one act two names"), now visible on one world as a double write.

(d) ORDER — canonical verse order by the first cited verse (book, chapter, verse); a stable sort keeps each scene's own
order within a verse; a marker at a verse precedes the events of that verse.

(e) FIELDS — the scene-clock fields re-based: `day` DROPPED where the runner's daemon reads it as the clock (the idiom
`day = event.get('day', world.clock.day)` — erection, incense_shekel, priesthood, holiness, metzora, negaim, clocks; and
pesach/tzav/chatat/offerings/ordinances read `event['day']` as a day — none of their history rows carry it) and KEPT
where it is a VALUE (pre_sinai's `evening_and_morning` day count, the ink's own "day one... the sixth day"); `until`
(family's `widow_sent`) re-based RELATIVE to the clock at submission (+4 days — the scene's own interval; the ink has no
number at 38:11 "until Shelah grows"; labeled). The stitcher prints every re-based field.

(f) ENTITIES — the scene tokens on the ONE registry: tokens that already ARE registry ids (abraham, sarah, isaac,
ishmael, jacob, joseph, rebekah, tamar, moses, aaron, reuben, simeon, levi, judah, dinah...) resolve to themselves;
three tokens join existing entities as members (`noah` → noach, `adam` → the_human, `the-servant` →
servant_of_abraham); the people's three tokens (`israel`, `the-people`, `the-sons-of-israel`) become ONE new entity
`israel_people` — the only cross-runner unification the tape needs (the presence dwells on `the-people` at Exodus 40:34,
the covenant is cut on `israel` at 34:27, the sinew is barred on `the-sons-of-israel` at Genesis 32:33: one ledger).
Every other token is its own singleton by the registry's default rule. The daemons keep their hardcoded names (the
engine resolves them, section 2). The registry's note marks UNCERTAIN whether the frozen units' own people-tokens should
join the entity — the fold's own sitting, not this one.

(g) THE CLOSES carried in verse order (pre_sinai's five closes at Genesis 17:23-27 and 21:4; family's three at 38:10,
38:26, 50:12; the erection's tamid close runs inside its daemon).

(h) THE REGISTRY'S TAPE LINES: every history kind's `tape:` line in event_vocabulary.yaml gains "; resubmitted on the
sequential tape by cold_run_sequence.py" by script; the events lint reruns.

(i) THE TAPE FILE: the stitcher (scratchpad seq_stitch.py) writes the runner's tape section between two sentinel
comments as LITERAL `w.marker(...)`, `w.submit({...})`, `w.close(...)` lines in verse order — the daemon gate's parser
reads literal submits only. The stitcher is the instrument to rerun after any narrative scene changes; Numbers' scenes
join the tape by rerunning it.

## 4. THE MARKERS — the text's own stamps, every number parsed from the ink

THE NUMERAL PARSER (in the runner; the stitcher writes each literal from its output, the runner re-parses the verse at
run time and refuses a mismatch): the ink's numeral words with their ב/ל/ו prefixes; units one to nine before מאת/מאות
("hundred/hundreds") MULTIPLY (תשע מאות nine hundred; שמנה מאת eight hundred), every other numeral word ADDS (שלשים ומאת
thirty and a hundred); שתים ("two", feminine) counts; שנים counts as "two" only before עשר ("ten" — twelve), else it is
"years" (Genesis 11:32 חמש שנים ומאתים five years and two hundred); the ordinals (הראשון ("the first") ... העשירי ("the tenth"),
בראשון ("in the first")) name months. Measured at the design on 44 verses: two misses, both שתים ("two") wrongly skipped
(Genesis 5:18, 5:20) — the rule above is the corrected one; the stitcher re-measures.

Classes: F forward · P proleptic · R retrograde. Days: `born[x]` the life era's epoch; `+Ny` the same date N years on
(the modeled anniversary — the ink gives YEARS, the day within the year is the engine's anniversary, labeled); `D(y, m,
dom)` the day of creation-year y, ordinal month m from Tishrei, day dom; `X(y, m, dom)` the same in the exodus era.

| verse | the ink's number(s) | class | the day | sets |
|---|---|---|---|---|
| Gen 1:5, 1:8, 1:13, 1:19, 1:23, 1:31, 2:2 | day one ... the sixth, the seventh | F | day 0 ... 6 (the ordinal − 1) | `life:the_human` at day 5 (1:27, the sixth day) |
| Gen 5:3, 5:6, 5:9, 5:12, 5:15, 5:18, 5:21, 5:25, 5:28, 5:32 | 130, 105, 90, 70, 65, 162, 65, 187, 182, 500 | F | `born[father] + Ny` | `life:seth` ... `life:noach`, `life:shem` |
| Gen 5:5, 5:8, 5:11, 5:14, 5:17, 5:20, 5:23, 5:27, 5:31 | 930, 912, 905, 910, 895, 962, 365, 969, 777 | P | `born[x] + Ny` | (Enoch "taken", 5:24) |
| Gen 7:11 | the 600th year of Noah's life, the second month, the seventeenth | F | `born[noach] + 600y`, then the first 17th of ordinal month 2 (Marcheshvan under Rabbi Eliezer) | — |
| Gen 8:4 | the seventh month, the seventeenth | F | the next 17th of ordinal month 7 | — |
| Gen 8:5 | the tenth month, the first | F | the next 1st of ordinal month 10 | — |
| Gen 8:13 | the 601st year, the first month, the first | F | the next 1st of ordinal month 1 | — |
| Gen 8:14 | the second month, the twenty-seventh | F | the next 27th of ordinal month 2 | — |
| Gen 9:29 (with 9:28) | 950 (350 after the flood) | P | `born[noach] + 950y` | — |
| Gen 11:10 | Shem a son of 100; Arpachshad two years after the flood | F | `flood + 2y` | `life:arpachshad`; `life:shem` re-derived = the marker − 100y (checkpoint C4) |
| Gen 11:12, 11:14, 11:16, 11:18, 11:20, 11:22, 11:24, 11:26 | 35, 30, 34, 30, 32, 30, 29, 70 | F | `born[father] + Ny` | `life:shelah` ... `life:terah`, `life:abraham` |
| Gen 11:32 | Terah 205 | P | `born[terah] + 205y` | — |
| Gen 12:4 | Abram a son of 75 | F | `born[abraham] + 75y` | — |
| Gen 16:16 | Abram a son of 86 | F | `+ 86y` | `life:ishmael` |
| Gen 17:1 | Abram a son of 99 | F | `+ 99y` | — |
| Gen 17:24-25 | 99; Ishmael 13 | — | checkpoint C-ink: `born[ishmael] + 13y` = the counter | — |
| Gen 21:5 | Abraham a son of 100 | F | `+ 100y` | `life:isaac` |
| Gen 21:4 | the eighth day | F | `born[isaac] + 7` (the inclusive ordinal: the birth day is the first) | checkpoint C8 |
| Gen 25:7 | Abraham 175 | P | `born[abraham] + 175y` | — |
| Gen 25:17 | Ishmael 137 | P | `born[ishmael] + 137y` | — |
| Gen 25:20 | Isaac a son of 40 | F | `born[isaac] + 40y` | — |
| Gen 25:26 | Isaac a son of 60 | F | `+ 60y` | `life:jacob`, `life:esau` |
| Gen 26:34 | Esau a son of 40 | F | `born[esau] + 40y` | — |
| Gen 35:28 | Isaac 180 | P | `born[isaac] + 180y` | — |
| Gen 41:46 | Joseph a son of 30 (placed by 45:6's two years of famine after the seven of plenty, 41:53, and 47:9's descent) | F | `descent − 9y` | `life:joseph` = the marker − 30y |
| Gen 47:9 | Jacob a son of 130 | F | `born[jacob] + 130y` — THE DESCENT | — |
| Gen 47:28 | Jacob 147 (17 in Egypt) | F | `born[jacob] + 147y` (the deathbed chapters follow: 48-49; 49:33 the death) | — |
| Gen 50:26 | Joseph 110 | P | `born[joseph] + 110y` | — |
| Exod 7:7 | Moses a son of 80, Aaron 83 at the speaking | P (era only) | the speaking undated within the exodus year; the eras set from the exodus day | `life:moses` = exodus − 80y, `life:aaron` = exodus − 83y |
| Exod 12:2 | "this month is for you the head of months" | F | the first of the exodus month — creation-year `Y(born[isaac] + 400y)`, ordinal month 7 (Nisan), day 1 | `exodus` (new-year month 1) |
| Exod 12:41 (12:6, 12:29, 12:37) | "on that very day" — the fifteenth of the month | F | `X(1, 1, 15)` | checkpoint C3 |
| Exod 16:1 | the second month, the fifteenth | F | `X(1, 2, 15)` | — |
| Exod 19:1 | the third month, "on this day" | F | `X(1, 3, 1)` — the new moon by Rava's verbal analogy with 12:2 (Shabbat 86b:5: TRANSFER, taught) | — |
| Exod 24:18 | forty days and forty nights | F | `X(1, 3, 7)` — Moses ascended on the seventh of Sivan (Taanit 28b:8-9: the Torah given on the sixth, the Sages, or the seventh, Rabbi Yose; "twenty-four of Sivan and sixteen of Tammuz make forty"; TRANSFER, taught) | checkpoint C6 |
| Exod 34:4 | "he rose early in the morning" | F | the breaking's day + 1 — the scene's own dating (no shelf row; labeled) | — |
| Exod 40:17 | the first month of the second year, the first | F | `X(2, 1, 1)` (Shabbat 87b:6 "that day took ten crowns") | checkpoint C5 |
| Lev 8:2 | the seven days (8:33) and the eighth (9:1) | R | `X(2, 1, 1) − 7` = the twenty-third of Adar — the identification of the eighth day with 40:17's day is Shabbat 87b:6's "first for the priesthood" (TRANSFER, taught); the arithmetic the ink's | the retrograde stretch |
| Lev 9:1 | the eighth day | F | `X(2, 1, 1)` | the stretch ends; checkpoint C7 |

THE SOJOURN SETTING (OPEN-3; a parameter row `sojourn_start` with three settings, the running one named): the 400
years of Genesis 15:13 run from the SEED, and the ink defines the seed — "in Isaac shall seed be called to you"
(21:12): a REFERENCE licensed by ink; the exodus "on that very day" (12:41) is then the day the 400 complete, and the
shelf's own row agrees — "on Passover Isaac was born" (Rosh Hashanah 10b:10). The 430 of Exodus 12:40 ("the dwelling
which they dwelt in Egypt") read literally from the descent is the second setting; the tradition records the gap itself:
the elders wrote for Ptolemy "in Egypt AND IN OTHER LANDS" (Megillah 9a:16, read on the shelf). The third setting, the
covenant between the pieces, is the tradition's (not on the local shelf under the searched forms — labeled). The tape
RUNS the first; the machine reports the others (checkpoint C3).

The gaps the tape has no event for are printed, not hidden: Genesis 50:26 → Exodus 12:2 (no runner compiles Exodus
1-11's narrative), Exodus 12 → 24 (the Passover runner's rows are cases), Leviticus 10 → 27.

THE CENSUS'S GRAMMAR (THE NUMBERS WALK sitting 1b, 2026-09-09; NUMBERS_WALK.md "Sitting 1b"): the parser above was
Genesis's and Exodus's — no thousands beyond a bare אלף ("thousand") that added 1,000, no plural אלפים ("thousands"),
'two' told from 'years' by position, and מאת read as a hundred wherever its consonants stood. Bamidbar's reading measured
it unable to read a census (Num 1:21 → 1,546 for 46,500) and the compile taught it, with census_probes.py written first
(3/17 → 17/17), the stitcher's marker verification rerun at every pass, and the whole-corpus diff old-against-new read
verse by verse (155 verses moved, none a marker). The rules now in ink_numbers and verse_words: אלף/אלפים without the
conjunction multiply the group since the last thousands-word (an empty group: a bare thousand; the dual 'two thousand'
only before a numeral — before a noun it is the plural "thousands", Exod 18:21); וְאֶלֶף ("and a thousand") adds; a
numeral repeated as the SAME raw word is distributive (3:47 "five, five"; Gen 7:2 "seven, seven"), with the conjunction
two numbers; the article on a numeral counts at the head of a chain of "and the N" (3:46) and "and the N" only inside a
chain — "and the OTHER" (Gen 42:13) is no number; and TWO HOMOGRAPHS BY THE POINTS ON THE STEM, measured on the DB's own
code points: מֵאֵת ("from", the tsere under both letters) is emitted מ-את and is no number, against מְאַת ("a hundred
of") and מֵאֹת ("hundreds"); the numeral שנים ("two") has a sheva under the shin (שְׁנַיִם, שְׁנֵים, the pausal
שְׁנָיִם), "years" a qamats (שָׁנִים) and "second ones" a hiriq under the nun (שְׁנִיִּם, Gen 6:16) — the non-numeral is
emitted with a star and keeps the phrase open like שנה ("year"). Convention 4 stands: every marker's numbers verified again at
stitch time and at run time; a changed parse on a marker verse is an INK MISMATCH that stops the stitch and is read.

## 5. THE DAEMONS — all 38 on one world

Registered in this order: the library's five first (law_slave_term, law_goring_ox, law_guardians, law_deposit_oath,
law_installation — the runners register them first on their own scenes), then the 33 runners' daemons in the canonical
order of their spans (Genesis → Exodus → Leviticus; a file with two daemons keeps its own order). The coverage printed:
every daemon's events seen / fired / kinds. Most law daemons see 147 events and fire on none — the zero-report law's
instrument for the whole. THE OVERLAPS: 28 kinds are watched by more than one daemon (computed from
daemon_dispositions.yaml at the design); the history kinds among them fire BOTH on one world — `milluim_blood_sprinkled`
and `milluim_leftover` (law_investiture + law_installation), `incense_burned` (law_erection + law_investiture),
`bread_arranged` and `lamps_raised` (law_erection + law_priesthood), `offering_brought` (law_erection +
law_sanctuary_build), `renamed` (law_family + law_pre_sinai — the last open alias). The double writes are FINDINGS
printed with their counts, never suppressed and never fixed at this sitting (each is an alias question of its own).

## 6. THE CHECKPOINTS — declared by the text (or the shelf), computed by the engine, a mismatch reported never repaired

| # | declared | computed | expected | OPEN |
|---|---|---|---|---|
| C0 | Genesis 5's nine totals (5:5 ... 5:31) | begetting age + the years after (5:3 + 5:4 ...) | 9 MATCH — the ink's own arithmetic | — |
| C1 | the flood's 150 days (7:24, 8:3) | 8:4's day − 7:11's day | DIVERGE (147 under the received month) | OPEN-4 |
| C2 | Noah a son of 600 at the flood (7:6); 350 after, 950 in all (9:28-29) | the life era's reading of "the 600th year" (7:11) | MATCH under the completed reading; the ordinal reading DIVERGES by a year (printed) | OPEN-8 |
| C3a | 430 years in Egypt (Exod 12:40) | the exodus − the descent (47:9) | DIVERGE: 210 (Megillah 9a:16 the elders' "and in other lands") | OPEN-3 |
| C3b | 400 years of the seed (Gen 15:13, the seed by 21:12) | the exodus − `born[isaac]` | MATCH: 400 | — |
| C3c | the lifespans' bound: Kohath came down (46:11), Kohath 133 (Exod 6:18), Amram 137 (6:20), Moses 80 (7:7) | the descent-to-exodus interval ≤ 350 | MATCH within the bound (210); the descent-literal setting's 430 DIVERGES from the ink's own lifespans | OPEN-3 |
| C4 | Shem a son of 100 two years after the flood (11:10) | `born[shem]` by 5:32 (Noah 500) against 11:10 | DIVERGE by two years (Sanhedrin 69b:15: Shem born at Noah's 502, the list by wisdom) | — |
| C5 | Exod 40:17 (the first month, the second year) and Num 10:11 (the second month, the second year) | `year_in('exodus')` at both dates | MATCH: 2 and 2 (Rosh Hashanah 3a:5) | — |
| C6 | the tablets broken on the seventeenth of Tammuz (Mishnah Taanit 4:6; Taanit 28b:8-9) | the forty-day timer's fire, dated in the exodus era | MATCH: (1, 4, 17) | — |
| C7 | seven days (Lev 8:33), the eighth day (9:1) = the erection's day (Shabbat 87b:6) | the release's fire − Lev 8:2's dated day; the fire's day against 40:17's | MATCH: 7; equal | — |
| C8 | Isaac circumcised on the eighth day (21:4) | the marker at `born + 7` against the daemon's timer at `day + 8` | DIVERGE by one day — a FINDING on the pre_sinai daemon's count (the scene's own advance hid it) | filed |
| C9 | Sarah 127 (23:1) with 17:17 (Sarah 90 at Abraham's 100) | her death's year against the BOUND the tape gives the purchase (Gen 23:16: between 21:5's marker and 25:20's) | MATCH within [2049, 2089] | — |
| C10 | Methuselah's seven days before the flood (Sanhedrin 108b:5, Rav) | `born[methuselah] + 969y` against the flood's day | DIVERGE (41 days under the running reading; the same year) — Rav's reading is not the arithmetic's | — |

## 7. THE FIRE-PROBES (World/step9/sequence_probes.py; 0/4 against the unchanged engine)

P1 an era SET BY A MARKER, its year counting new-year boundaries: the exodus era set at a Nisan; `year_in` = 2 at the
   next Nisan's first and still 2 at the following Iyar's twentieth (Rosh Hashanah 3a:5), and `date_in` reads ordinal
   months from Nisan while the world's own year is unchanged.
P2 `year_in` across an INTERCALATED boundary: a thirteen-month creation-year exists under the modeled season ground and
   the exodus-era year still turns once per Nisan.
P3 a LIFE era: "the 600th year" (completed) and "a son of N years" agree; the ordinal setting differs by one year;
   `day_in` finds the first 17th of ordinal month 2 inside the life-year.
P4 on a stitched stretch: the PROLEPTIC marker's log class (counter unmoved, no dated stretch); the DATED DAY as the
   event's day inside a retrograde stretch; the registry map merging two tokens on one ledger; a checkpoint against the
   bound an event inherits between two markers.

## 8. THE GRADED LITERAL — what is predicted first, what is typed from the first run

PREDICTED BY SCRIPT before the runner runs (the stitcher prints them; typed as literals): the tape census (submits
scanned, history kept, cases off, acts-on-tractate off, law-clause acts off, deduped, re-based fields), the markers by
class (F / P / R counts), the daemons registered (38), the markers' DAYS from the calendar arithmetic (the flood's,
the exodus', Sinai's, the erection's, Lev 8:2's dated day), and every checkpoint's verdict as section 6 expects.
TYPED FROM THE FIRST RUN, labeled so (the standing practice for a scene tuple): the run-derived counts — timers set /
fired / cancelled, retro-writes, ledger writes, daemons that fired, entities on the ledger, the double writes of section
5. A first-run value is EVIDENCE to be read before it is typed (a double write, a timer that never fires, a close that
closes nothing); the second run must reproduce it. A miss thereafter is evidence, never a retype.

## 9. THE CONVENTIONS Numbers must follow (for THE_STEPS)

1. A narrative span's scene submits LITERAL events in the text's order, dated by the text's own stamps as MARKERS —
   never by a scene number; an event's `day` field is a VALUE only when the ink counts it (the creation days).
2. The registry's FORM decides what is history: acts, speech and statutes on a narrative verse (the wayyiqtol test);
   the Mishnah's rows are the exam and stay off the tape.
3. A lifespan total is a PROLEPTIC stamp; a begetting or an age-at-event a FORWARD one; a stated date earlier than the
   counter a RETROGRADE one (Pesachim 6b:7).
4. Every number on a marker is parsed from the ink by the numeral parser and verified again at run time.
5. Entity names resolve through the ONE registry at the engine; a new scene's tokens join it as members with
   `units: [step9-scenes]`; a people-token joins `israel_people`.
6. The sequence tape is RE-STITCHED after every new narrative scene (scratchpad seq_stitch.py → the runner's sentinel
   section); the sweep grades the stitched tape as its 34th runner.
7. A timer whose due the ink states as "the Nth day" counts the first day inclusively (C8's lesson).

## 10. OPEN

OPEN-3 the sojourn's three settings (the tape runs the seed's 400); OPEN-4 the flood's 150; OPEN-7 which creation day
is the first of Tishrei; OPEN-8 the two idioms of the life-year; the second ascent's morning (the scene's own dating);
the eighth-day count (C8 — a one-line fix on the pre_sinai daemon and its scene literal, its own sitting); ONE ACT TWO
SUBJECTS at Leviticus 8:30 and the six overlapping history kinds (aliases, each its own question); the frozen units'
people-tokens' membership in `israel_people` (the fold's sitting); the tape's gaps (Exodus 1-11, 12-23, Leviticus 10-27
carry no narrative events — the runners compile law there, or nothing yet) [O8 S1, 2026-09-08: Exodus 1-19's story is ON the
tape — NARRATIVE_GAPS.md; the gaps line now reads the Genesis stretches (S2-S4) and the ink's own silences inside Exodus 2-7] [O8 S2, 2026-09-08:
Genesis 2:4-16:16 is ON the tape (183 events, 7 markers, the reprieve decree the tape's second retrograde-dated marker); the gaps line now reads Genesis
18-20, 22, 25-31, 33-37, 39-47 (S3-S4) and Exodus's own silences]; Numbers 33:3's fifteenth (the exodus day's
own verse, off the three books — 12:6, 12:29, 12:37 carry it here). THE REST (O8 S3, 2026-09-08): the sequence runner's eighth checkpoint — the tape minus the newest runner's lines, run as its own world, reproduces the previous sitting's RUN exactly (NEWEST_RUNNER / PREVIOUS_RUN move forward each sitting); Avot 5:3's ten trials against the ink's one (CH1 DIVERGE, the list's shelf absent). THE FOURTH SITTING (O8 S4, 2026-09-08): NEWEST_RUNNER = 'joseph', PREVIOUS_RUN = S3's tuple — THE REST reproduced it on the first tape run; the seventy's missing one (46:15's thirty-three against thirty-two living named — CJ3b DIVERGE, the shelf's answers none the ink's, OPEN); the register test set four of Joseph's events aside (the roster's perfect "took" at 36:2-3, the nominal famine clause of 43:1) — the tape carries what a narrative verb carries; the third day INCLUSIVE with its own marker (convention 23), one marker per row (convention 22).

## 11. As built (the sitting's close, 2026-09-07)

The engine: `Era` (a view on the one month table — epoch day + new-year month; the LIFE era calendar-aligned, its year the
calendar years' difference, Genesis 8:13 having refused the birthday-anniversary design of section 2's first draft);
`Clock.eras`, `set_era`, `year_in`, `date_in`, `day_in(..., reading=)`; `World.marker(era=, new_year_month=, proleptic=)`;
the dated day as the event's day at submit; `World(registry=)` resolving at `entity()` and `cancel_timers`;
`law_installation` reading the event's day. The registries: calendar_parameters.yaml + `creation` (6 eras) +
`life_year_reading` (19 rows); entity_registry.yaml + `israel_people` and three scene members; event_vocabulary.yaml's 90
tape lines, the `renamed` alias RESOLVED (open aliases 0); daemon_dispositions.yaml `functions: sequence: tape NONE`;
dependency_dispositions.yaml `spans: sequence: []`. The tape: 827 scanned, 145 history, 141 on the tape (4 deduped, 4
fields re-based, 8 closes), 68 markers (51 forward / 16 proleptic / 1 retrograde), 90 kinds, 51 subjects, 29 eras set.
The probes 4/4 (0/4 before); the clock probes 12/12; the skeleton 6/6; the gate probes 5/5 and 12/12. The runner
cold_run_sequence.py 6/6 checkpoints: every predicted day and every expected verdict matched; the run tuple typed from
the first run after its evidence was read (finding 2 of the report). The findings, the census and the sweep line:
REPORT_SEQUENTIAL_RUN.md. The pre_sinai scene's two renamings now carry the ink's names (17:5, 17:15) — the one runner
edit of the sitting, its 212/212 unmoved.

## 12. O1 — THE SMALL FIXES (2026-09-07, the open-items campaign's first sitting; the plan: the state doc's compaction point #90)

Declared BEFORE the code; every citation resolved on the local shelf by script (scratchpad shelf_find.py, nikud stripped; the
Rabbah files searched by a script of the same shape). The rhythm: the data rows and the event type first, the daemon's
watch declared, the gate run to fail, the code, the scenes' tuples re-predicted and printed before typed, the tape
re-stitched, the sweep, the records.

(a) C8 THE EIGHTH DAY — law_pre_sinai's timer `due = day + 7`: the inclusive ordinal, the birth day the first (Gen 21:4
"on the eighth day"; 17:12 "a son of eight days"). The pre_sinai scene advances to day 17 (born on day 10); its tuple's
clock 18 → 17. The sequence's C8 expected MATCH (the fire at born + 7). The runner's row eighth_day_count retires — the
convention is section 9's rule 7.

(b) TAMAR'S WAIT BY THE TEXT'S OWN ACT — a new act type `shelah_grown` registered at Gen 38:14 (the witness כי ראתה כי
גדל שלה "for she saw that Shelah had grown", found contiguous in the verse, the pointed form extracted by script).
law_family writes the wait OPEN at 38:11 with NO due — the ink gives no number ("until Shelah my son grows"), so no timer
— and at 38:14 writes `levirate_owed` on Shelah (counterparty Tamar): the ink's own statement of the duty due and unpaid
("and she was not given to him as a wife"). Tamar's wait closes at 38:26 as before; Shelah's debit stays OPEN — the ink
never records his act (46:12 gives him his own line; the seed was raised through the father-in-law): the open entry at
the tape's end is the ink's silence, printed. The family scene's advance-to-fire is replaced by the act's submit; its
tuple gains (n, open) for Shelah's debit and its timer count drops to zero. The runner's row tamar_wait_days retires;
the registry's widow_sent loses its `until` field. Shelah is a singleton token (not in entity_registry.yaml — the default
rule of section 3(f)).

(c) THE SECOND ASCENT DATED BY THE SHELF — two markers replace the scene's +1. Exod 32:30 FORWARD, "and it was on the
morrow" (ויהי ממחרת) = the breaking + 1, the ink's own word (assert_ink extended with `words=` — the word verified in
the verse); it dates the intercession's ascent (32:31 "and Moses returned to the LORD"), whose length is Deuteronomy's
(9:18's forty) — owed to that book, not on this tape. Exod 34:4 FORWARD, positioned at 34:2 before the ascent's event:
the last tablets were given on Yom Kippur — "the day on which the last tablets were given" (יום שניתנו בו לוחות
האחרונות: Taanit 30b:8; Bava Batra 121a:6, both read by script) — a data row `second_tablets_given` {month 7, day 10} in
the exodus era (Lev 23:27's date the ink's), so the ascent = that day − 40 (Exod 34:28's forty, ink-verified; the timer's
own arithmetic — the same shape as Lev 8:2 = the erection − 7). The machine's date of the ascent is PRINTED (the
twenty-ninth of Av under the modeled month lengths); the tradition's own date of the ascent (the first of Elul — Seder
Olam, Pirkei deRabbi Eliezer) is NOT on the local Babylonian shelf (ראש חדש אלול "the new moon of Elul" searched: no row)
— a remark, never a checkpoint. NEW CHECKPOINT C11: the second tablets' fire dated (1, 7, 10) in the exodus era — MATCH
expected by construction; it guards the timer's arithmetic across the months between Av and Tishrei. The erection
runner's own W7 test world keeps its relative days (a comment at its 34:4 submit says where the date lives).

(d) THE BIRTHS' DAYS FROM THE SHELF'S ROWS — Rosh Hashanah 10b:10 (Rabbi Eliezer) and 11a:2 (Rabbi Yehoshua) BOTH say
"on Passover Isaac was born" (בפסח נולד יצחק); 11a:13 derives it from Gen 18:14 "at the appointed time I will return to
you" (למועד אשוב אליך — the annunciation at the festival, the birth at Passover). The two arms differ on the patriarchs'
month: "in Tishrei the patriarchs were born" (10b:10; 11a:7 from 1 Kings 8:2's "month of the mighty ones") against "in
Nisan" (11a:2; 11a:9 from 1 Kings 6:1's "month of Ziv"). Two data rows: `isaac_birth_date` {month 1 — the calendar's own
first, Nisan, Exod 12:2's numbering; day 15 — the feast's day, Lev 23:6 / Exod 12:18 the ink's}, EXERCISED; `patriarch_birth_month`
value 7 (Tishrei) with the settings r_eliezer 7 / r_yehoshua 1, the day within the month MODELED at the first (as
before), applied to Abraham, Jacob and Esau; every other birth stays modeled at the year's first day (section 4's rule).
The INK block's `birth_day(w, year, who)` reads the rows; every begetting and birth marker runs through it. NEW
CHECKPOINT C3b-day: the exodus "on that very day" (12:41) = Isaac's birth + 400 years TO THE DAY through the Calendar —
MATCH expected: the day grain is now the shelf's row, not the model's.

(e) OPEN-7 SEARCHED AND FOUND — the Genesis spine carries the MONTH dispute only (Bereshit Rabbah 22:4: Rabbi Eliezer "in
Tishrei the world was created", Rabbi Yehoshua "in Nisan" — Abel's lifetime from the festival to Hanukkah, or from
Passover to Shavuot) and no row for the DAY; the local shelf's Vayikra Rabbah 29:1 (on Lev 23:24, the seventh month's
first day) has it, in Rabbi Eliezer's own name: "on the twenty-fifth of Elul the world was created" (בעשרים וחמשה באלול
נברא העולם), and it reads the very liturgy line 27a:15 cites — "this day is the beginning of Your works, a memorial of
the first day" — of ADAM'S day: "on the day of Rosh Hashanah, in the first hour it arose in thought... in the seventh He
blew a soul into him". So the sixth day of creation is the first of Tishrei, and the design's plain reading of 27a:15
(day one = the first of Tishrei) was a placeholder pending the search: the shelf's own row RUNS. The era row `creation`
gains `day_one_offset` 5 with the settings {vayikra_rabbah_29_1: 5, rosh_hashanah_27a_plain: 0}; the Calendar lays a
STUB MONTH before the first Tishrei — Elul of year 0, its last five days: day 0 = the twenty-fifth of Elul, day 5 = the
first of Tishrei of year 1, Adam's day (his life era's epoch by the tape's own 1:31 marker, unchanged); the world's own
era view opens at the first new-year start (day 5), and the five days before it read the calendar's year 0. Every
absolute day on the tape after day 4 moves by +5; every year, date and interval is unchanged — the stitcher re-predicts
the days. The anno-mundi remark stands (the machine's creation-year is still one higher than the tradition's count;
OPEN-8's ordinal reading is where that difference lives).

(f) THE SOJOURN FORK AS THREE WORLDS — the tape runs three times, each world with all 38 daemons (the tape costs a
fifth of a second; the imports are the runner's time): seed_isaac (the running setting — the exodus = Isaac's birth +
400 to the day); descent_literal (the exodus = the descent + 430, Exod 12:40 read literally); covenant_pieces (the
exodus by the seed's 400 — the tradition's arithmetic fixes the covenant between the pieces at 430 before the exodus,
thirty years before Isaac, Abraham at 70 — and the covenant's IMPLIED year is checked against the chapter's own bound:
Gen 15 sits between 12:4's marker, Abram 75, and 16:16's, 86). Expected: world 1 as section 6 with C8, C3b-day and C11
MATCH; world 2: C3a MATCH (430), C3b DIVERGE (430), C3c DIVERGE (430 beyond the lifespans' 350); world 3: C3a DIVERGE
(210), C3b MATCH, C3c MATCH, C3d DIVERGE (the implied covenant at Abraham's 70 falls before the bound's 75 — the
tradition's resolution, an earlier stay in Canaan and a return to Haran, Seder Olam 1, NOT on the local shelf: בין
הבתרים "between the pieces" searched across the Babylonian shelf, no row). Each world prints its exodus year and its C3
verdicts; the grade's TESTS gain the fork's verdict lists. THE FORK'S FIRST RUN CAUGHT A LATENT FAULT: the descent-literal
world's exodus landed on the fifteenth of ADAR II — its exodus year (2669) is a thirteen-month year under the modeled
season ground, and the tape had addressed Nisan as 'the creation era's ORDINAL seventh month from Tishrei', which is Adar II
when a thirteenth month follows Adar. The running world never showed it (2049 and 2449 are twelve-month years). The fix:
a post-12:2 month name is addressed by the CALENDAR'S OWN numbering (Exod 12:2 'the first month' = Nisan, Tishrei the
seventh — the INK block's cal_day); the era view's ordinal months serve the pre-12:2 ink (Gen 7:11's 'second month' from
Tishrei) and the exodus era's own count from Nisan. The data rows are written in the calendar's numbering.

THE PREDICTIONS, written before the run. CENSUS: scanned 828, history 146, on the tape 142, case 670, source-off 7,
register-off 5, deduped 4, re-based 3 (Tamar's `until` gone), closes 8, markers 69 (F 52 / P 16 / R 1), kinds 91,
subjects 52 (Shelah) [THE STITCHER'S COUNT: 51 — Shelah is the act's `levir` FIELD, its subject Tamar; he joins the LEDGER as
an entity (79), not the tape's subjects. The script's number is the one typed; the prose prediction missed by that one]. DAYS: every day after day 4 = the old + 5, except born:isaac (the fifteenth of Nisan of the same
year), eighth_day (born:isaac + 7), second_ascent (Yom Kippur − 40), and the new keys morrow and second_tablets.
VERDICTS: C8 MATCH; + C3b-day MATCH; + C11 MATCH; the fork's lists as (f). RUN (typed from the first run after its
evidence is read; predicted here from the standing run's timer census — 12 set, 5 fired): events 142; timers set 11
(Tamar's gone); fired 4 (Isaac's now at 21:4, the tablets twice, the face); cancelled 0; retro-writes 0; writes 205
(Shelah's debit added; Tamar's fire-write replaced by the immediate write); daemons fired 9; entities 79; the double
writes unchanged (O2's sitting); closes performed 8 of 8. The scenes: pre_sinai's tuple ends 17 (was 18); family's
gains (1, 1) after Tamar's (1, 0) and its timer count reads 0.

## 13. O2 — THE ALIASES SITTING (2026-09-07; the open-items campaign's second sitting; the plan: the state doc's compaction point #90)

Declared BEFORE the code. The sequential run's REPEATED WRITES list named six overlap kinds and the renamings: one event
consumed by two daemons, each writing the same effect. The rule this sitting fixes, and the contract each kind receives:

THE RULE — ONE ACT, ONE WRITER PER EFFECT. A daemon consumes an act narrated in ITS OWN SPAN (the span the dependency
census declares for its runner), or a recorded run of its own statute (a case row citing a tractate or another book);
an act narrated in another engine's span is that engine's, and the ledger is written once. Two daemons may still consume
one act when each writes ITS OWN effect from its own compiled verses — ONE TYPE UNDER TWO LAW LAYERS, the W3 form — and
that is declared in the registry, not left to be discovered on the tape. The scope reads the event's first cited verse
(world_engine.seat — the book and chapter), never a string typed into a verdict. The ink's own repeats (two mornings)
are named apart in the runner's expectation.

| kind | the seats | the double write on the tape | THE CONTRACT |
|---|---|---|---|
| milluim_blood_sprinkled | Lev 8:30 | invested_office on Aaron ×4 (law_installation + law_investiture on two events, two subjects; law_priesthood's 8:12) and on the sons ×2 | THE PARTY IS THE COMPOUND — Lev 8 names "Aaron and his sons" as one party in nine verses (8:2, 6, 14, 18, 22, 27, 30, 31, 36 — counted by script) and 8:30 sprinkles and sanctifies both: the subject is `aaron-and-sons` on every scene (the incense runner's `aaron` was its shorthand). The library's law_installation (the Lev 8 engine, Tzav's F7) writes the COMMIT — invested_office on the party (Sifra, Mekhilta DeMiluim I 34); law_investiture (the Exod 29 spec's daemon) writes the spec's own entry at the run — consecrated on the garments (29:21 "he and his garments, his sons and his sons' garments") — and no longer the office. One event on the tape (the dedup by kind, subject, verse). |
| milluim_leftover | Lev 8:31-32 | burn_remainder on the remainder ×2 (law_investiture on two events) beside the library's on the holders | the library owns it (8:32, Tzav's leftover clause; the effect's own row: "a duty on the object's HOLDER" — the subject the party, as the library writes); law_investiture's branch retires to an empty watch (its cell already CALLS the Tzav engine for the leftover). The tzav scene's source reads 8:31-32 like the registry's ink line (one command, two clauses), so the tape carries one event. |
| confined (8:33-35) | Lev 8:33 | confined_seven_days on Aaron and the sons (law_investiture) beside the library's on the party with the release timer from 8:2 | the library owns the confinement and the release (the timer from the take-list's day, the seven days of 8:33); law_investiture's branch retires to an empty watch. Not on the first run's list — different entities hid it; the same overlap. |
| head_anointed (8:12) | Lev 8:12 the run; Lev 21:10 the statute | invested_office on Aaron from law_priesthood (21:10 "on whose head the anointing oil was poured") beside law_investiture's anointed | law_priesthood consumes the kind within its own span (Lev 21 — its scene's row); the run's 8:12 is the investiture's act: anointed. |
| incense_burned | Exod 40:27 the act; 30:7-8 the statute; 2 Chr 26, Num 16-17 the runs | incense_continual on the golden altar ×2 (law_erection + law_investiture) | law_erection owns the erection's act (E5: the golden altar initiated with the incense — Mishnah Menachot 4:4 — and the next morning's timer); law_investiture consumes the kind within its own span (Exod 30) and the recorded runs, not Exod 40. |
| lamps_raised | Exod 40:25; Lev 24:2-4 | lamp_arranged ×2 (law_erection + law_priesthood) | law_erection owns 40:25 (the evening arrangement and the morning's timer); law_priesthood consumes within Lev 24. |
| bread_arranged | Exod 40:23; Lev 24:5-9 | bread_set_weekly, the frankincense, the loaves' due (law_priesthood at 40:23) beside law_erection's weekly timer | law_erection owns 40:23 (the first Sabbath's timer); law_priesthood consumes within Lev 24. |
| offering_brought | Exod 36:3 ×2; 35:22-28 | given_by_the_heart ×2 and set_apart_before_me ×2 on the people | NOT AN ALIAS: ONE TYPE UNDER TWO LAW LAYERS with one field contract (the subject is the giver; `giver` optional) — law_sanctuary_build writes 25:2's trigger (set apart before Me, Onkelos), law_erection writes 35:5/21/29's heart; the ×2 is the ink's own two mornings (36:3 "morning by morning"). Declared in the registry; the runner names the two mornings apart. |
| renamed | Gen 17:5, 17:15; Gen 32:29 | name_changed ×2 on Abraham, Sarah, Jacob (law_pre_sinai + law_family) | each seat's owner by span: law_pre_sinai on Gen 17, law_family on Gen 32; both write the ink's name as the value (the one field contract the sequential run closed). |

THE PREDICTIONS, written before the run. The scenes: the incense runner's world registers the library's law_installation
beside its own (the tzav / shemini_day / erection pattern) with the party's subject on 8:30, 8:31-32, 8:33-35 — its tuple
re-shaped: invested_office and confined_seven_days on `aaron-and-sons` (1, 1), consecrated on the garments 1, burn_remainder
on the party 1, released 1 after the seven days; every other scene's tuple UNCHANGED (tzav's source string only; the
priesthood's rows are Lev 21/24; pre_sinai's and family's renamings sit in their own spans; the erection's world has no
statute daemon; the skeleton untouched). The tape: 142 → 140 events (the incense runner's 8:30 and 8:31-32 rows dedup
against the erection's and tzav's), deduped 4 → 6, kinds 91, subjects 51 → 50 (`aaron` leaves the Lev 8 rows — the
stitcher's count decides). The run: REPEATED WRITES = the two mornings only — (israel_people, given_by_the_heart) 2 and
(israel_people, set_apart_before_me) 2; timers set 11 → 10 (the priesthood's loaves' due at 40:23 gone — the stitcher's
recording and the run decide; read before typed), writes fewer by the retired doubles; daemons fired 9 → 8 (law_priesthood
no longer fires on Exod 40's acts — its rows are off the tape); entities 79 → the run's count. The gate: law_investiture's
declared watches change FIRST (milluim_blood_sprinkled → consecrated; milluim_leftover, confined → empty) and the gate
fails on the code until the branches match.

AS RUN (O2's close). The gate failed three ways on the declared watches (confined, milluim_leftover, milluim_blood_sprinkled),
then passed on the code — with two more honest fires along the way: the incense scene's tape list had gained a comment after
its closing bracket and the gate's parser read the loop's submit as UNRESOLVED (the bracket must end its line — the comment
moved above the list); and vestments.office, WRAPPED by law_investiture on the shared effect invested_office, lost its
verifier when the investiture daemon stopped writing the office — re-pointed to law_installation, whose commit IS the
office's run. The incense scene's tuple printed before typed: (1, 1, 1, 1, 3, 2, 1, 1, 1, 1, 1, 1, 1, 1, 2, 16) — the party's
office, remainder, confinement and RELEASE from the library beside; sixteen events with 8:2's command; every other scene
unchanged. The recorder 829 submits; the stitcher (829, 147, 140, 670, 7, 5, 7, 3, 8, 69, 52, 16, 1, 91, 51) — deduped 7,
not the predicted 6 (the incense scene's new 8:2 command dedups too), subjects 51 (Aaron stays a subject at 8:6-12, 8:36);
the predicted days unchanged. The run, read then typed: (140, 8, 4, 0, 0, 186, 8, 76, the two mornings, 8) — timers set 8
(the priesthood's three at Exod 40 gone), writes 186, 8 of 38 daemons, 76 entities, REPEATED WRITES = the two mornings of
36:3 under the donation's two law layers and nothing else. 7/7.


## 14. O9 — THE CLOCK'S OPEN ITEMS ON THE TAPE (2026-09-08; the open-items campaign's ninth sitting; the design: CLOCK.md section 12)

What the sequence runner takes from O9 (the engine's part is CLOCK.md 12a-12e; this section is the tape's), declared before
the stitcher ran and the literals were typed:

- THE COVENANT BETWEEN THE PIECES joins the marker table (12b): Genesis 15 carries no date — the bound [12:4 Abram seventy-five,
  16:3 the ten years]; the row covenant_pieces_year holds the two readings on the local shelf (Bereshit Rabbah 46:2 eighty-five;
  the Mekhilta on Exodus 12:40 row 1 seventy); the RUNNING world places it at eighty-five — a forward marker at 15:1 on the
  same day as the ten years (75 + 10, both modeled at the year's first day: the counter does not move), class reading_placed;
  the sojourn fork's `covenant_pieces` world places it at seventy — the same row EARLIER than the counter, so the engine's own
  rule makes it RETROGRADE: the Gen 15 events dated at Abraham's seventy, the stretch closed by the ten-years marker MOVED from
  16:3 to 16:1 (the first verse outside Genesis 15; the numbers still checked at 16:3) — 7:4's lesson generalized. That world's
  exodus is computed FROM its placed covenant (Exodus 7:7's row gains the branch: the covenant + 430), the Mekhilta's own
  arithmetic; the runner's PARAMS gains `covenant_placement` (the running setting the spine's, overridden in that world).
- THE MARKER'S VERSE IS ITS POSITION (12b): the engine stamps the placement class on the event whose first verse is the
  marker's verse, so a marker's call names where it sits — 21:5's number is called at 21:2 (the birth), 45:6's at 45:5 (the
  speech's first verse); assert_ink keeps the numbers' verse.
- THE PLACEMENT CLASS is COMPUTED by the stitcher per row (12b: a `places` row read, a typed shelf number, or propagation
  through the M keys in tape order) and injected into the marker's call; the events' stamps are PREDICTED by replaying the
  engine's rule on the tape's order (the class at the marker's verse, the retrograde stretch as one, page_order else) — a new
  graded literal PLACEMENT (markers by class, events by stamp) read from the logs.
- THE SLOT (12e): the stitcher stamps `slot` on an event from the ink's own day-word at its first verse (the runner's
  slot_of, one copy, over the registry's day_slots table — exactly one slot's word present, else nothing); the runner
  RE-VERIFIES every slotted event against its verse after the run; a new graded literal SLOTS; the stitcher's SLOT-REGRESSION
  REPORT names the ink's own day-crossings the tape has not marked — evidence, never a fix (the counter moves by markers
  only; no marker row is added for them this sitting: OPEN-12, a year-grain marker met inside its own year).
- C3d AS THE JOIN (12b) on the running world under both settings — C3d-70 MATCH (the ink's own five hundred), C3d-85 DIVERGE
  (515 — the evidence); the fork world's old C3d (the implied covenant within the bound) retired — it would match by
  construction; FORK_VERDICTS['covenant_pieces'] = C3a DIVERGE (the tradition's two hundred and ten in Egypt), C3b MATCH (the
  Mekhilta's thirty IS the join), C3c MATCH.
- C12 and C13 under the ELAPSED column (12a): Avodah Zarah 9a:7 — Abraham fifty-two at the year two thousand; 9a:8 — 448 from
  there to the giving of the Torah; the runner's remark prints both columns (the Seder Olam numbers not on the local shelf).
- PREDICTED: the marker table 130 (F 113 / P 15 / R 2 on the running world); CENSUS otherwise unmoved; DAYS gains
  `covenant_pieces` = hagar_given's day; the RUN tuple and THE REST UNMOVED (the placement and slot stamps write nothing; the
  covenant marker walks the clock to the same day the ten years did, ten verses earlier — the fires' days unchanged).


### As run (2026-09-08)

The stitcher's print first (scratchpad o9_stitch1.txt): 130 markers, F 113 / P 15 / R 2, every number verified against the ink;
the placement classes computed with a reason per row — 31 reading-placed markers (ten typed shelf numbers, seven rows read
from the registry's `places` rows, fourteen propagated: the binding's third day, the whole road from the departure to Hebron
riding Megillah 17a's fourteen and its eighteen and six months, Shur riding the sea, the morrow riding the breaking) and 84
text-constrained; the events' stamps predicted 86 / 941 / 31; the slots 37 events on six slot names; TWO slot regressions
reported (Gen 19:27 morning -> Gen 19:33 night; Gen 28:11 sunset -> Gen 28:18 morning) — the ink's own day-crossings the tape has not marked, filed OPEN-12 beside the year-grain marker met
inside its own year; the DAYS literal gaining covenant_pieces = hagar_given's day, every other key unmoved. The literals were
typed FROM the print by script (the CENSUS tuple, DAYS, PLACEMENT, SLOTS), the four verdicts as the design declared.

THE FIRST RUN 9/10: every prediction held — the markers, the placement classes, the slots (re-verified against the verse,
zero mismatches), the events, the days, the verdicts (C3d-70 MATCH, C3d-85 DIVERGE at 2464 against the exodus's 2449, C12 and
C13 MATCH under the elapsed column), the fork (the covenant_pieces world's exodus computed FROM its placed covenant at creation
year 2019, its Gen 15 events dated at day 737087 with three retrograde markers on that world — 6:3, 15:1, Lev 8:2 — and its
exodus − descent = 210, the tradition's own two hundred and ten), THE REST — and ONE miss on the RUN tuple: retro-writes 3
against 0, while the same run's header and log classes showed no RETRO-WRITE at all. The reading: the runner's own hand — the
fork loop's new print had reused the name `retro` for the covenant world's retrograde MARKERS, clobbering the running world's
retro-write list before the tuple was built. Renamed; nothing typed anew. THE SECOND RUN 10/10 (1.8s on the tape). The two date
columns as printed: the flood 1657 / 1656, Abraham born 1949 / 1948, the exodus 2449 / 2448 — the label and the elapsed rendering, the
tradition's anno mundi the second.
