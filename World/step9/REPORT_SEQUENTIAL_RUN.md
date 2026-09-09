# REPORT — THE SEQUENTIAL RUN: the three books on ONE world of the law engine (2026-09-07)

The owner's ruling after THE CLOCK SITTING ("are the first three books done to the point that we can run them in
sequence" — the recommendation: run them in sequence BEFORE Numbers; "ok lets do that but first I need to compact. get
ready"; after the compaction: "reread 88 and go"). The design is World/step9/SEQUENTIAL_RUN.md; the probes
World/step9/sequence_probes.py (0/4 against the unchanged engine, 4/4 after); the runner World/step9/cold_run_sequence.py
(the sweep's 34th); the stitcher scratchpad/seq_stitch.py over the recorder scratchpad/seq_record.py. The order of work
held as the wrap fixes it: the design FIRST, the fire-probes SECOND, the engine extension THIRD, the stitcher and the tape
FOURTH, the gates, the sweep and the records FIFTH.

## What ran

ONE world, `epoch='creation'` (day 0 = the first day of the world's first month, the seventh — Rosh Hashanah 10b:10,
27a:15; Rabbi Yehoshua's Nisan the other setting, unexercised), with ALL 38 DAEMONS registered (the library's five
first, then the 33 runners' in the canonical order of their spans) and a tape of 141 HISTORY events stitched by script
from the 33 runners' scenes in canonical verse order, the clock walked by 68 MARKERS — the text's own stamps, every
number parsed from the ink and re-verified at run time (68 re-checks), in three classes: 51 forward, 16 proleptic (the
lifespan totals), 1 retrograde (Leviticus 8 after Exodus 40:17). Twenty-nine eras set by markers (the creation era, the
exodus era at Exodus 12:2, twenty-seven life eras at the births). The clock ends at the erection's day: creation-year
2450, the first of Nisan, the exodus era's (2, 1, 1).

THE FILTER (every test computed, the census printed by the stitcher): of 827 submits scanned across the 33 runners,
670 are CASE rows by the registry's own form (the exam, off the tape); 7 acts are sourced to a tractate or another book
(off, named); 5 acts fail THE WAYYIQTOL TEST — the register test off the Tanakh DB's morphology (a narrative verb within
ten verses of the cited verse in its chapter; a speech verb frames a speech, not an act): the priesthood runner's three
law-clause rows (Leviticus 21:10, 24:2, 24:5) and the incense runner's two (Exodus 30:7-8) — law clauses dressed as
acts; 145 are HISTORY, 4 deduped (Leviticus 8:2 and 8:30 submitted by three scenes each), 141 on the tape; 4 scene-clock
fields re-based (three `day` fields dropped for the clock, Tamar's `until` made relative); 8 closes carried.

## The chronology, reproduced from the ink alone (the days predicted by the stitcher before the run, matched by the run)

| stamp | the machine's day | creation year, month, day | note |
|---|---|---|---|
| Seth born (Gen 5:3) | 47490 | 131, Tishrei 1 | the year grain is ink; the day within the year modeled at the year's first day |
| Noah born (5:28) | 385704 | 1057, Tishrei 1 | |
| the flood (7:11) | 604900 | 1657, Marcheshvan 17 | Rabbi Eliezer's second month (Rosh Hashanah 11b:7); the ordinal reading 1656 printed beside |
| the ark rested (8:4) | 605047 | 1657, Nisan 17 | 147 days after — C1 |
| the waters dried (8:13) | 605208 | 1658, Tishrei 1 | the 601st year's first month: THE LIFE-YEAR TURNS AT THE NEW YEAR |
| the earth dry (8:14) | 605264 | 1658, Marcheshvan 27 | a year and ten days after the flood began (364 days) — the ink's own interval |
| Abram born (11:26) | 711522 | 1949, Tishrei 1 | |
| Isaac born (21:5 at 21:2) | 748032 | 2049, Tishrei 1 | |
| Jacob born (25:26) | 769962 | 2109 | |
| the descent (47:9) | 817422 | 2239 | |
| the exodus (12:41) | 894323 | 2449, Nisan 15 | 400 years after Isaac's birth (15:13 by 21:12); 210 after the descent |
| Sinai (19:1) | 894368 | 2449, Sivan 1 | the new moon (Shabbat 86b:5) |
| the ascent (24:18) | 894374 | 2449, Sivan 7 | Taanit 28b:9 |
| the tablets broken (32:19) | 894414 | 2449, Tammuz 17 | the forty-day timer's fire — C6 |
| the erection (40:17) | 894693 | 2450, Nisan 1 | Shabbat 87b:6 |
| Leviticus 8:2 (dated) | 894686 | 2450, Adar II 24 | retrograde; the modeled intercalation makes 2450 a thirteen-month year — the tradition's twenty-third of Adar assumes a twenty-nine-day Adar |

The tradition's anno-mundi count (Seder Olam, not on the local shelf) runs ONE YEAR LOWER than the machine's creation-year
throughout (the flood 1656, Abraham 1948, the exodus 2448 there; 1657, 1949, 2449 here): it counts Adam's creation year
as year 0. Printed as a remark, never a checkpoint. Every other relation the tradition computes falls out of the ink's
numbers under one declared convention (a life-year turns at the New Year — Genesis 8:13; "the Nth year of X's life" is
the year of age N — 7:6, 9:28-29; the day within a year modeled at the year's first day — Rosh Hashanah 10b:10 "in
Tishrei the patriarchs were born").

## The checkpoints (declared by the text or the shelf; computed by the engine; a mismatch reported, never repaired)

| # | declared | computed | verdict | note |
|---|---|---|---|---|
| C0 | Genesis 5's nine totals = begot + after | 9 of 9 | MATCH | the ink's own arithmetic, parsed |
| C1 | 150 days (7:24, 8:3) | 147 | DIVERGE | OPEN-4, now on a tape |
| C2 | Noah 600 at the flood (7:6); 950 − 350 | 600, 600 | MATCH | the ordinal reading 599 printed (OPEN-8) |
| C3a | 430 years in Egypt (Exod 12:40) | 210 | DIVERGE | Megillah 9a:16 — the elders wrote "and in other lands" (OPEN-3) |
| C3b | 400 years of the seed (15:13 by 21:12) | 400 | MATCH | |
| C3c | the lifespans' bound ≤ 350 (46:11; Exod 6:18, 6:20, 7:7) | 210 within [0, 350] | MATCH | the descent-literal setting's 430 DIVERGES from the ink's own lifespans |
| C4 | Shem 100 at Arpachshad (11:10) vs Noah 500 (5:32) | 102 | DIVERGE | Sanhedrin 69b:15 — Shem born at Noah's 502 |
| C5 | the second year at Nisan and at Iyar (40:17; Num 10:11) | 2, 2 | MATCH | Rosh Hashanah 3a:5 — the exodus era's new year |
| C6 | the seventeenth of Tammuz (Mishnah Taanit 4:6) | (1, 4, 17) | MATCH | Sivan of thirty days; Taanit 28b:9's arithmetic reproduced |
| C7 | seven days, the eighth = the erection's day (Lev 8:33, 9:1; Shabbat 87b:6) | 7, equal | MATCH | the release written on the erection's day from the dated Leviticus 8:2 |
| C8 | Isaac on the eighth day (21:4, the birth day the first) | 8 | DIVERGE | the pre_sinai daemon counts born + 8 — a finding |
| C9 | Sarah 127 (23:1; 17:17) within the purchase's bound | in [748039, 762642] | MATCH | the bound the tape gave Genesis 23:16 |
| C10 | Methuselah's seven days (Sanhedrin 108b:5, Rav) | 46 | DIVERGE | the same creation year (1657); the day within the year is modeled |

## Findings

1. **THE LAST OPEN ALIAS CLOSED BY COLLISION.** The first full run crashed at Genesis 17:5: law_family consumed the
   pre-Sinai `renamed` and read a `name` it never carried — the "two contracts" of D9-i's seeding, harmless on two worlds,
   a fault on one. The ink states the names (17:5 "your name shall be Abraham", 17:15 "Sarah is her name"); the pre_sinai
   scene now carries them; the registry's alias entry is marked resolved; the daemon gate prints open aliases 0.
2. **THE UNDATED-STRETCH TIMER.** Two of the tape's eight closes found nothing open: Isaac's circumcision_due (21:4) and
   Tamar's wait (38:26). A timer set inside an undated stretch fires only when the next marker walks the clock — AFTER
   the stretch's own closing act; the scenes' advance() calls had hidden it. On the one world the eighth-day timer fires
   a day after the ink's eighth day (C8: the daemon counts born + 8, the inclusive ordinal is born + 7) and Tamar's
   four-day wait fires at the next marker, sixty years on. Filed: the eighth-day count is a one-line fix on the pre_sinai
   daemon and its scene literal (its own sitting); the wait's fire is the scene's own invented interval.
3. **THE LIFE-YEAR TURNS AT THE NEW YEAR.** The design had the life era on birthday anniversaries; the marker table's
   own arithmetic refused it — Genesis 8:13's "601st year, first month, first day" follows 7:11's "600th year, second
   month, seventeenth" by ten and a half months, and 8:14 closes a year and ten days. The engine's life era is
   calendar-aligned (the age is the calendar years' difference), and the whole chronology then falls into the
   tradition's shape from the ink alone.
4. **THE INTERCALATION DATES LEVITICUS 8.** Creation-year 2450 is a thirteen-month year under the modeled season ground,
   so the installation's dated first day is the twenty-fourth of Adar II, not the twenty-third of Adar — the day grain
   of OPEN-2 made visible on the tape.
5. **ONE EVENT, TWO DAEMONS.** Nine of thirty-eight daemons fired (the nine narrative daemons; every law daemon saw 141
   events and fired on none — the zero-report instrument for the whole). The repeated writes are the overlaps the design
   named: law_installation and law_investiture on Leviticus 8:30 (Aaron invested FOUR times — one act under two subjects
   and two daemons), law_pre_sinai and law_family on every renaming, law_erection and law_priesthood on the lamps,
   law_investiture and law_erection on the incense; and the ink's own repeats (two mornings of Exodus 36:3). Each an
   alias question of its own, reported, none fixed here.
6. **THE PARSER'S THREE LESSONS** (caught by the stitcher's ink check before any tape was written): a year-word keeps a
   number phrase open across its parts (Genesis 5:6 "five years and a hundred years") but a units multiplier does not
   carry across it; "forty days and forty nights" are two numbers (Exodus 24:18); Genesis 8:5 names the tenth month
   twice. 44 verses at the design, two misses (שתים, "two", wrongly skipped) — corrected; 68 marker verses at the sitting,
   every one matched.
7. **THE REGISTER TEST WORKS AT THE VERSE.** The corpus world's events table covers Genesis and Exodus 1-20 only; the
   wayyiqtol test off the morphology decided every row — and the scenes' own citation forms ("Exod 24:1, 24:9"; ranges)
   had to be parsed whole, or the second verse was lost.
8. **THE SHELF FINDER'S NIKUD.** Some tractate files are vocalized; a substring search reports a false "not found"
   unless it strips the points — Shabbat 86b:5, 87b:6 and Pesachim 6b:7 were "missing" until it did.
9. **THE GAPS, PRINTED.** Genesis 2 → 9 (1657 years), 9 → 17, 24 → 32, 38 → 48, and Genesis 50 → Exodus 24 (193 years:
   no runner compiles the narrative of Exodus 1-11, and the Passover runner's rows are cases) carry no events.

## The census (coverage first)

| | before | after |
|---|---|---|
| runners in the sweep | 33 | 34 (cold_run_sequence.py — a tape runner, its span empty) |
| daemons | 38 | 38, all on one world |
| calendar_parameters.yaml | 18 rows, 5 eras | 19 rows (life_year_reading), 6 eras (creation); exercised now: creation, exodus, life_years |
| the engine | Calendar, Clock, World | + Era (a view: epoch day, new-year month; the life era calendar-aligned); Clock.eras / year_in / date_in / day_in; marker(era=, proleptic=); the dated day as the event's day; World(registry=) |
| entity_registry.yaml | | + israel_people (3 scene tokens); noach, the_human, servant_of_abraham gain a scene member |
| event_vocabulary.yaml | open aliases 1 (renamed) | open aliases 0; 90 tape lines carry the sequential tape |
| daemon gate | 248 / 0 / 7 of 255 | 248 / 0 / 8 of 256 (sequence.tape NONE) |
| dependency gate | 33 runners, 96 live import edges | 34 runners, 129 live import edges (the sequence's 33 beyond the census, listed) |
| probes | 12/12 clock | 12/12 clock + 4/4 sequence + 6/6 skeleton + 5/5, 12/12 gate probes |
| the sequence runner | — | 6/6 checkpoints (three census rows, the 28 predicted days, the 14 verdicts, the run tuple) |

## The sweep at the sitting's close

34 of 34 runners green, 3,632 graded cells (3,626 + the sequence runner's six), both gates satisfied first (scratchpad
sweep_seq.txt, SWEEP-EXIT 0): DEPENDENCY GATE 34 runners declared, 1,888 verses scanned, 130 required edges and 73 pointers
dispositioned, 129 live import edges (the sequence's 33 beyond the census, listed); DAEMON GATE 38 daemons watching 266
kinds, 775 submit records, 248 WRAPPED / 0 OWED / 8 NONE of 256, unfired 0, unconsumed 0, OPEN ALIASES 0; the events lint
0; the sequence runner 6/6 in 37.5 seconds. No frozen unit touched. The three books ran in sequence on one world; the
clock walked by the text's own stamps; the tradition's chronology came out of the ink's numbers under one declared
convention; the text's own gaps reported where they fall. Next: NUMBERS — its first sitting reads the standing map and
SEQUENTIAL_RUN.md section 9's conventions; its narrative scenes join the tape by rerunning the stitcher.

## O1 — THE SMALL FIXES (2026-09-07; the open-items campaign's first sitting, after compaction #90; the design: SEQUENTIAL_RUN.md section 12)

Six items, declared before the code, every citation resolved on the local shelf by script. What changed on the tape:

| item | before | after | the shelf |
|---|---|---|---|
| (a) the eighth day (C8) | the pre_sinai daemon's timer born + 8; the fire a day late | born + 7, the inclusive ordinal; the fire on 21:4's own marker; C8 MATCH | Gen 21:4, 17:12 (ink) |
| (b) Tamar's wait | a four-day timer the scene invented; its fire sixty years on at the next marker | no timer: the wait written open at 38:11, the levir's duty written OWED on Shelah at 38:14's own act (`shelah_grown`, registered with its witness), Tamar's wait closed at 38:26, Shelah's debit left open — the ink's silence | Gen 38:11, 38:14, 38:26 (ink) |
| (c) the second ascent | the breaking + 1, the scene's own dating | two markers: 32:30 "on the morrow" (ink, the word verified) for the intercession's ascent; 34:4 at Yom Kippur − 40 — the last tablets given on Yom Kippur; C11 MATCH | Taanit 30b:8; Bava Batra 121a:6 |
| (d) the births' days | every birth at the year's first day (modeled) | Isaac on Passover, the fifteenth of the first month (both arms of the baraita); Abraham, Jacob, Esau in Tishrei (Rabbi Eliezer's arm; Rabbi Yehoshua's Nisan the other setting); C3b-day MATCH — the exodus "on that very day" 400 years after Isaac's birth TO THE DAY | Rosh Hashanah 10b:10, 11a:2, 11a:7, 11a:9, 11a:13 |
| (e) OPEN-7 | day one = the first of Tishrei (the plain reading of 27a:15, a placeholder) | day one = the twenty-fifth of Elul, the sixth day (Adam) = the first of Tishrei: the era row's day_one_offset 5, a stub month laid before the first Tishrei; the plain reading the other setting | Vayikra Rabbah 29:1 (found); Bereshit Rabbah 22:4 (the month only) |
| (f) the sojourn's settings | one world; the other settings reported by arithmetic | THREE WORLDS, all 38 daemons on each: seed_isaac (running), descent_literal, covenant_pieces — each graded on the 430's checkpoints | Megillah 9a:16; the covenant's date not on the shelf |

The chronology after O1 (the day numbers all +5 after day 4 — the stub month; the dates unchanged except Isaac's):
Isaac born 15 Nisan 2049 (day 748228), circumcised 22 Nisan (748235); the exodus 15 Nisan 2449 (894328) = Isaac + 400 years
to the day; the breaking 17 Tammuz (894419); the morrow 18 Tammuz (894420); the second ascent 29 Av (894460); the second
tablets 10 Tishrei 2450 (894500); the erection 1 Nisan 2450 (894698). Day 0 = 25 Elul of year 0; Adam's day = day 5 = 1
Tishrei of year 1.

The checkpoints after O1: C8 MATCH (was DIVERGE); C3b-day MATCH (new); C11 MATCH (new); the fork's worlds — descent_literal
C3a MATCH / C3b DIVERGE (620) / C3c DIVERGE (430 beyond the lifespans' 350); covenant_pieces C3a DIVERGE / C3b MATCH / C3c
MATCH / C3d DIVERGE (the covenant implied by 430 before the exodus falls at Abraham's 70, five years before 12:4's marker —
the tradition's resolution, Seder Olam's earlier stay in Canaan, not on the local shelf). The running world's other
verdicts unchanged.

### Findings of the sitting

1. **THE FORK CAUGHT A LATENT FAULT.** The descent-literal world's exodus landed on the fifteenth of ADAR II: its exodus
   year (2669) is a thirteen-month year under the modeled season ground, and the tape had addressed Nisan as "the creation
   era's ordinal seventh month from Tishrei" — Adar II when a thirteenth month follows Adar. The running world never
   showed it (2049 and 2449 are twelve-month years). A post-12:2 month name is now addressed by the calendar's OWN
   numbering (Exod 12:2 "the first month" = Nisan — the INK block's cal_day); the era view's ordinal months serve the
   pre-12:2 ink and the exodus era's own count. The other settings are not a report beside the running world; they are
   worlds, and a world runs into what a remark cannot.
2. **THE THREE FORTIES ARE CONTIGUOUS BY THE DAY ARITHMETIC.** With the second ascent placed forty days before Yom Kippur,
   the machine's own interval from the morrow of the breaking (32:30) to the second ascent is EXACTLY forty days — the
   middle forty of Deuteronomy 9:18 falls out of the Exodus ink and the shelf's Yom Kippur row without being used: 7
   Sivan + 40 = 17 Tammuz; 18 Tammuz + 40 = 29 Av; 29 Av + 40 = 10 Tishrei (the modeled month lengths). The tradition's
   first of Elul for the third ascent counts inclusively at the seam; that date is not on the local shelf — a remark.
3. **THE UNDATED-STRETCH TIMER CLOSED ON BOTH COUNTS.** The tape's closes now perform 8 of 8: Isaac's timer fires on the
   ink's own eighth-day marker (born + 7, the day the close arrives), and Tamar's wait carries no timer at all — the
   ink's act at 38:14 does the timer's job. Two findings of the first run repaired by the text's own stamps, not by an
   advance.
4. **THE OPEN DEBIT THE INK NEVER CLOSES.** Shelah's levirate_owed (38:14) stays open at the tape's end among the 43 open
   entries — the ink records no act of his (46:12 gives him his own line; the seed was raised through the father-in-law).
   Printed, not closed by hand.
5. **THE PREDICTION MISSED BY ONE.** Section 12 predicted 52 tape subjects; the stitcher counted 51 — Shelah is the act's
   `levir` FIELD (its subject Tamar) and joins the LEDGER as an entity (79), not the tape's subjects. The script's number
   is the one typed; the design carries the correction beside its prediction. Every other predicted number matched: the
   census, the 30 marker days, the verdicts, the fork's lists, the two scenes' tuples, and the RUN tuple (142 events, 11
   timers set, 4 fired, 205 writes, 9 daemons, 79 entities, closes 8) — read from the first run and typed as predicted.
6. **THE INK RE-CHECKS ARE PER WORLD.** The first O1 run counted 207 re-checks — three worlds × 69; the runner now
   counts each world's own (69, 69, 69) and grades the running world's.

### The census after O1

| | before O1 | after O1 |
|---|---|---|
| the tape | 141 events, 68 markers (51 F / 16 P / 1 R), 8 closes performed 6 | 142 events, 69 markers (52 F / 16 P / 1 R), closes 8 of 8 |
| the checkpoints | 14 (C8 DIVERGE) | 16 + the fork's 7 (C8, C3b-day, C11 MATCH) |
| calendar_parameters.yaml | 19 rows, 6 eras | 22 rows (isaac_birth_date, patriarch_birth_month, second_tablets_given), the creation era's day_one_offset with two settings |
| the engine | Era, Clock, World | + the stub month (Calendar.day_one_offset, first_year_start); the world's own era opens at the first new-year start, the days before it read year 0 |
| event_vocabulary.yaml | 266 types | 267 (shelah_grown, act, Gen 38:14); widow_sent without `until` |
| daemon_dispositions.yaml | law_family 22 kinds | 23 (shelah_grown → levirate_owed); the gate failed first, then passed |
| the runner's parameters | 4 rows | 1 (sojourn_start; the three retired rows named in the file) |
| the scenes | pre_sinai's clock 18; family's timer 1 | pre_sinai 17; family's timer 0, Shelah's debit (1, 1) — both tuples printed before typed, both as predicted |
| the fork | — | three worlds, 0.2 s each; FORK_VERDICTS graded |

### The sweep at O1's close

34 of 34 runners green, 3,633 graded cells (+1: the sequence runner's seventh test, the fork), both gates satisfied first
(scratchpad sweep_o1.txt, SWEEP-EXIT 0): DEPENDENCY GATE 34 runners, 1,888 verses, 130 required edges and 73 pointers
dispositioned, 129 live import edges; DAEMON GATE 38 daemons watching 267 kinds, 777 submit records, 248 WRAPPED / 0 OWED /
8 NONE of 256, unfired 0, unconsumed 0, open aliases 0; the events lint 0 (267 types); the clock probes 12/12, the sequence
probes 4/4, the skeleton standing; the three touched runners green on their own lines (pre_sinai 212/212, family 228/228,
erection 287/287); the sequence runner 7/7 in 37.5 s (the three worlds 0.2 s each; the imports the rest). No frozen unit
touched; the corpus regression green, the world hash 8b8fff1fa28953af unmoved. Next: O2 THE ALIASES.

## O2 — THE ALIASES SITTING (2026-09-07; the open-items campaign's second sitting; the design: SEQUENTIAL_RUN.md section 13)

THE RULE FIXED: one act, one writer per effect. A daemon consumes an act narrated in its own span (the dependency census's
declared span) or a recorded run of its own statute; an act in another engine's span is that engine's, and the ledger is
written once. Two daemons may consume one act when each writes ITS OWN effect from its own verses — one type under two
law layers, declared in the registry. The scope reads the event's first cited verse (world_engine.seat), never a string
typed into a verdict.

| kind | the contract | the double write it ends |
|---|---|---|
| milluim_blood_sprinkled (Lev 8:30) | the party is `aaron-and-sons` — "Aaron and his sons" one party in nine verses of Lev 8, counted by script; the library's law_installation writes the COMMIT (invested_office on the party, Sifra Mekhilta DeMiluim I 34); law_investiture writes the spec's own entry, consecrated on the garments (Exod 29:21) | the office on Aaron ×4 and the sons ×2 |
| milluim_leftover (8:31-32) | the library's — burn_remainder, a duty on the holders (the effect's own row); the investiture's watch empty; the tzav scene's source reads 8:31-32 (one command, two clauses) so the tape carries one event | the remainder ×2 |
| confined (8:33-35) | the library's confinement and release timer from 8:2; the investiture's watch empty | the confinement on two names (hidden from the first list by the different entities) |
| head_anointed (8:12 the run; Lev 21:10 the statute) | law_priesthood within Lev 21; the run's 8:12 is the investiture's anointing | the office on Aaron at 8:12 |
| incense_burned, lamps_raised, bread_arranged (Exod 40:27, 40:25, 40:23) | law_erection owns the erection's acts (the initiation, Mishnah Menachot 4:4, and their timers); law_investiture within Exod 30 and the recorded runs; law_priesthood within Lev 24 | incense_continual ×2, lamp_arranged ×2, the loaves' entries at 40:23 |
| offering_brought (36:3 ×2; 35:22-28) | NOT AN ALIAS — one type under two law layers with one field contract: law_sanctuary_build writes 25:2's trigger (set apart before Me), law_erection writes 35:5/21/29's heart; the two mornings of 36:3 are the ink's own repeat, named apart in the runner | — |
| renamed (Gen 17:5, 17:15; 32:29) | each seat's owner by span: law_pre_sinai on Gen 17, law_family on Gen 32; both write the ink's name as the value | name_changed ×2 on Abraham, Sarah, Jacob |

### Findings of the sitting

1. **THE PARTY IS THE INK'S COMPOUND.** Leviticus 8 names "Aaron and his sons" as one party in nine of its verses (8:2, 6,
   14, 18, 22, 27, 30, 31, 36) and Aaron alone in four; the incense runner's `aaron` on 8:30, 8:31-32 and 8:33-35 was a
   scene's shorthand, and the shorthand is what made one act two subjects. With the ink's party on every scene, the tape's
   dedup (kind, subject, first verse) collapses the three scenes' rows to one.
2. **A WRAP'S VERIFIER CAN MOVE.** vestments.office was WRAPPED by law_investiture on their shared effect invested_office;
   when the office's writer became the library's commit, the gate refused the stale wrap — re-pointed to law_installation.
   The gate's function-level check did its job the moment a contract changed hands.
3. **THE LOOP'S LIST MUST END ITS LINE.** The gate's submit parser reads a `tape = [...]` list up to a closing bracket that
   ends its line; a trailing comment made the loop's submit UNRESOLVED. The lesson joins the parser's standing ones.
4. **THE RUN'S DELTAS ARE THE CONTRACTS' ARITHMETIC.** Timers set 11 → 8 (the priesthood's three at Exod 40), writes 205 →
   186, daemons fired 9 → 8 (law_priesthood off the erection's acts — its rows are Lev 24's, off the tape), entities 79 →
   76 (the sons, the remainder, the loaves' entries gone as separate ledgers), the double writes ten pairs → the two
   mornings. Every one read from the run before it was typed.
5. **THE PREDICTION MISSED BY ONE AGAIN, ON THE SAME SHAPE.** Section 13 predicted deduped 6; the stitcher counted 7 — the
   incense scene's added 8:2 command dedups against the erection's. Subjects stayed 51 (Aaron is still a subject at 8:6-12
   and 8:36). The script's numbers are the ones typed.

### The census after O2

| | after O1 | after O2 |
|---|---|---|
| the tape | 142 events, deduped 4 | 140 events, deduped 7 |
| REPEATED WRITES | ten pairs (six overlap kinds + the renamings) | the two mornings of Exod 36:3 only |
| daemon_dispositions.yaml | law_investiture 22 watched kinds writing the office, the remainder, the confinement | the same 22 kinds: milluim_blood_sprinkled → consecrated; milluim_leftover, confined → empty watches; vestments.office re-pointed to law_installation |
| the daemons | four consume across spans | law_investiture, law_priesthood, law_pre_sinai, law_family read their own span by world_engine.seat |
| the incense scene | its own daemon alone; the party's acts on `aaron` | the library registered beside; the party `aaron-and-sons`; the tuple (…, 1, 1, 1, 1, 2, 16) |
| event_vocabulary.yaml | 267 types | 267; eight tape lines carry the contracts |
| the run | (142, 11, 4, 0, 0, 205, 9, 79, ten pairs, 8) | (140, 8, 4, 0, 0, 186, 8, 76, the two mornings, 8) |

### The sweep at O2's close

34 of 34 runners green, 3,633 graded cells, both gates satisfied first (scratchpad sweep_o2.txt, SWEEP-EXIT 0): DEPENDENCY
GATE 129 live edges; DAEMON GATE 38 daemons watching 267 kinds, 776 submit records, 248 WRAPPED / 0 OWED / 8 NONE of 256,
unfired 0, unconsumed 0, open aliases 0; the events lint 0; the gate fire-probes 5/5 and 12/12; the clock probes 12/12, the
sequence probes 4/4, the skeleton standing; the touched runners green on their own lines (incense_shekel 301/301, priesthood
252/252, pre_sinai 212/212, family 228/228, tzav 54/54, erection 287/287, vestments 196/196); the sequence runner 7/7. No
frozen unit touched; the corpus regression green, hash 8b8fff1fa28953af unmoved. Next: O3 THE GATE ITEMS.


## O9 — THE CLOCK'S OPEN ITEMS ON THE TAPE (2026-09-08; the open-items campaign's ninth sitting; the design: CLOCK.md section 12 and SEQUENTIAL_RUN.md section 14)

THE QUESTION THE TAPE ANSWERED: what the consensus's two tape-borne items look like on the one world — the placement class
beside the bound (T2), with Genesis 15 as its test, and the elapsed rendering (T3) where a local shelf number can be compared.

THE COVENANT BETWEEN THE PIECES joined the marker table with two readings from the local shelf, both read by script before a
line was typed: Bereshit Rabbah 46:2 (the Genesis spine — eighty-five, "at the hour He spoke with him between the pieces")
and the Mekhilta on Exodus 12:40 row 1 (seventy — "thirty years before Isaac was born the decree was decreed between the
pieces"). The running world places it at eighty-five: a forward marker at 15:1 on the day the ten years of 16:3 already
stood at, so the counter did not move and no count on the tape did either — the RUN tuple and THE REST reproduced exactly.
The sojourn fork's covenant_pieces world places it at seventy, EARLIER than the counter at 12:4's seventy-five: the engine's
own rule made the marker retrograde without a line written for it, the Gen 15 events carried the text's date (creation year
2019), and the stretch closed at the ten-years marker moved to 16:1 — the first verse outside Genesis 15. That world's exodus,
computed from its placed covenant plus the ink's four hundred and thirty, fell on the SAME day as the running world's
(Isaac's hundred plus the seed's four hundred): the Mekhilta's thirty IS the join, and its C3b matched for that reason, not by
construction; its C3a printed the tradition's own two hundred and ten years in Egypt as the DIVERGE from the four hundred and
thirty.

C3d AS THE JOIN ran on the running world under both settings: seventy plus four hundred and thirty MATCHES the exodus marker
at creation year 2449; eighty-five plus four hundred and thirty lands at 2464 — a DIVERGE of fifteen years, printed as the
evidence it is. The old C3d (the implied covenant inside Gen 15's bound) was retired from the fork world, where it would now
match by construction.

THE ELAPSED COLUMN met two local shelf numbers: Avodah Zarah 9a:7 ("the souls they made in Haran — Abraham at that hour was
fifty-two", the two thousand years of Torah opening there) and 9a:8 (four hundred and forty-eight from there to the giving of
the Torah). C12: Abraham's elapsed birth year plus fifty-two = 2000 (the label column says 2001); C13: the giving's elapsed
year less 2000 = 448. Both MATCH — "the tradition's count one lower" was the elapsed column all along; the Seder Olam numbers
(1656, 2448) stay a remark, not on the local shelf.

THE PLACEMENT STAMPS: 31 reading-placed markers and 84 text-constrained (the fifteen proleptic carry none); on the events 86
text-constrained, 31 reading-placed, 941 page_order — the unlabeled prior of every undated verse now labeled, predicted by
the stitcher from the engine's rule replayed on the tape's order and read back from the logs. THE SLOTS: 37 events carry the
ink's own day-word at their first verse (morning 14, night 12, sunset 3, evening 3, noon 3, dawn 2), each re-verified
against the verse after the run; the stitcher reported two day-crossings the tape has not marked (Gen 19:27 morning -> Gen 19:33 night; Gen 28:11 sunset -> Gen 28:18 morning) — evidence for a
later sitting, never a fix by the engine.

### Print-then-type

Every literal was typed FROM the stitcher's print by script (the CENSUS tuple, DAYS, PLACEMENT, SLOTS), the four new verdicts
as CLOCK.md 12g declared them. The first run 9/10: one miss, the RUN tuple's retro-writes 3 against 0 — and the same run's
header said "retro-writes 0" with no RETRO-WRITE in its log classes. The reading found the hand, not the world: the fork
loop's new print had reused the name `retro` for the covenant world's retrograde markers (three: 6:3, 15:1, Lev 8:2),
clobbering the running world's list before the tuple was built. Renamed, the second run 10/10. A miss is evidence — here of a
variable name.

### Findings

1. **THE MEKHILTA'S THIRTY IS THE JOIN.** Placing the covenant at seventy and adding the ink's four hundred and thirty lands
   on the very day Isaac's hundred and the seed's four hundred land on: the fork world's exodus did not move by a day. The
   reading the tradition wrote for Exodus 12:40 is arithmetic on the ink's own numbers, and the machine reproduces it.
2. **THE SPINE'S READING DIVERGES, AND THAT IS THE RECORD.** Bereshit Rabbah 46:2's eighty-five is inside the page-order bound
   and needs no retrograde, but its join with the four hundred and thirty misses the exodus by fifteen years. The running
   world keeps the spine's reading; the checkpoint prints the disagreement. Neither reading is smoothed into the other.
3. **THE ENGINE'S RETROGRADE RULE NEEDED NO NEW LINE.** The same marker row, under the other setting, fell earlier than the
   counter and the engine dated the stretch by itself; the design's one addition was the closing marker's position (16:1),
   7:4's lesson generalized.
4. **THE ELAPSED COLUMN IS WHERE THE SHELF COUNTS.** Two joins written by hand on two Avodah Zarah rows matched under the
   elapsed rendering and would have missed by one under the label — the generator over checkpoint() has its shape.
5. **THE INK'S DAY-WORDS CROSS THE BOUNDARY TWICE WITHOUT A MARKER** on the Genesis tape (Gen 19:27 morning -> Gen 19:33 night; Gen 28:11 sunset -> Gen 28:18 morning): the slot census found what
   the marker table had not, and the engine's counter stays where the markers put it — OPEN-12.
6. **A NAME REUSED IS A MISS.** The one miss of the sitting was a variable shadowed in the runner's own fork loop; the
   header line printed the true count beside the false tuple, and the reading took the header.
