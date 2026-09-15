import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE CLOCK AND TIME UPDATED WITH THE FOURTH BOOK (2026-09-13; the owner: "Update clocks"). THE_CLOCK.md: the head and title,
# Example 1's count, the four-gaps section retitled with each item's as-built line, the new section spliced before
# "## What is still open", the open items and the closing section extended. TIME.md: section 12 spliced before
# "## What was built from this", an eighth item added there. Every replacement asserted unique; refuses to run twice.
import re
SP = '<scratch>/'
C = (_ROOT + '/ARCHITECTURE/THE_CLOCK.md')
T = (_ROOT + '/ARCHITECTURE/TIME.md')

def splice(path, edits, marker):
    t = open(path, encoding='utf-8').read()
    assert marker not in t, ('already spliced', path)
    for old, new in edits:
        n = t.count(old); assert n == 1, ('not unique', n, path, old[:70]); t = t.replace(old, new)
    open(path, 'w', encoding='utf-8').write(t)
    print('spliced', path, len(t.split('\n')), 'lines')

clock_sec = open(SP + 'clock_numbers_section.md', encoding='utf-8').read()
splice(C, [
 ("# THE CLOCK — how the machine keeps time, taught from three examples",
  "# THE CLOCK — how the machine keeps time, taught from three examples and a fourth book"),
 ("**A tutorial (rewritten 2026-09-07 after the clock was built and the\nthree books were run in order).**",
  "**A tutorial (rewritten 2026-09-07 after the clock was built and the\nthree books were run in order; the fourth book's section added\n2026-09-13, after Numbers ran on the same clock).**"),
 ("read again each time the program runs. Sixty-eight numbers in all,\nacross the three books.",
  "read again each time the program runs. Sixty-eight numbers on the\nfirst run of the three books; 157 by the end of the fourth, every\none re-read at each run — and the fourth book, which counts a\npeople, taught the parser a whole grammar of its own (THE_TOUR.md,\nsection 9)."),
 ("## What the next look found: four more gaps\n\nThe day after the first run, a third working session read the\nengine and the run with the owner and named four things the account\nof time still lacks. The two sessions that built the clock argued\neach one through and agreed; all four are scheduled as the next\nclock sitting, pending the owner's word. In plain words:",
  "## What the next look found: four more gaps, and how each was built\n\nThe day after the first run, a third working session read the\nengine and the run with the owner and named four things the account\nof time still lacked. The two sessions that built the clock argued\neach one through and agreed, and all four were built the next day,\n2026-09-08, as the clock's open-items sitting. In plain words, the\ngap as it was named, and then what was built:"),
 ("arms, printed as a fork, like the jubilee.\n\n**2. Undated scenes",
  "arms, printed as a fork, like the jubilee.\n*As built:* every law now declares two verses — the one that speaks\nit and the act that switches it on — and the installing acts write\n\"in force\" on the institutions' accounts; sixty-two rules today,\ntwenty-two on from the start, thirty-nine by an act, one pending.\n\n**2. Undated scenes"),
 ("to his seventieth — printed as the tradition's fork, not ours.\n\n**3. Two ways",
  "to his seventieth — printed as the tradition's fork, not ours.\n*As built:* every marker and every event carries its placement —\nfixed by the text, placed by a recorded reading, or by page order —\nand the covenant runs at both readings, the seventieth year meeting\nthe exodus to the day and the eighty-fifth missing by fifteen,\nprinted. On the running world today: 102 markers fixed by the text,\n40 placed by a reading; 1,133 events by page order.\n\n**3. Two ways"),
 ("compared, and the \"one year lower\" remark becomes a matching\ncheckpoint instead of a note.\n\n**4. The text keeps",
  "compared, and the \"one year lower\" remark becomes a matching\ncheckpoint instead of a note.\n*As built:* two columns from one day count — the label and the\nelapsed year — and the Talmud's own numbers (Avodah Zarah 9a:\nAbraham fifty-two in the year two thousand) match under the elapsed\ncolumn.\n\n**4. The text keeps"),
 ("two events to \"the twentieth year\" in an order that only works if\nthe king's year begins in autumn — and the Talmud reads it exactly\nthat way.\n\n## What is still open",
  "two events to \"the twentieth year\" in an order that only works if\nthe king's year begins in autumn — and the Talmud reads it exactly\nthat way.\n*As built:* the text's own day-words — evening, night, midnight,\ndawn, morning, noon, between the evenings, sunset — are stamped on\nthe events that carry them, in the order Genesis 1:5 gives; the\nTalmud's two day-orders are data; and the counting idioms for\npeople, kings, animals and trees are rows with their sources.\n\n---\n\n" + clock_sec + "## What is still open"),
 ("- **Which day of creation is the first of the year**, and **whether\n  \"the six hundredth year\" means the year of age 600 or 599** — two\n  readings each, both recorded, the running one named, the other\n  printed beside it.",
  "- **Which day of creation is the first of the year**, and **whether\n  \"the six hundredth year\" means the year of age 600 or 599** — two\n  readings each, both recorded, the running one named, the other\n  printed beside it.\n- **The inclusive count.** Three places in the fourth book where the\n  tradition counts a span with its first day in and the machine's\n  timer counts the days that pass: the month of flesh, the spies'\n  forty days, and the forty-nine days from the tabernacle to the\n  departure. Abaye's full month is the calendar row's other arm,\n  recorded and not run; the misses stay printed.\n- **Miriam's day.** The text gives the month, the tradition the tenth\n  (Seder Olam Rabbah 10); the tape buries her on the arrival's day and\n  prints the nine-day divergence.\n- **The vow's twenty-four hours.** Rabbi Shimon ben Yochai's reading\n  of \"from day to day\" is the row's second arm, named and never run.\n- **A replay inside a bound.** The cursor stands only at a stated\n  date or after the last one; a stop between two dates is refused by\n  construction, and a design for it waits on the readback (THE_LOOP.md,\n  step 6).\n- **Korach's days.** The chapters carry no date in the text and none\n  on the shelf; their lines sit at the counter's day, by page order,\n  labeled so.\n- **The jubilee east of the Jordan.** Whether the fiftieth year's\n  release reaches the land Gad and Reuben took is filed as a\n  parameter for the book of Joshua's runs."),
 ("chronology table and all fourteen checkpoints, is\nWorld/step9/REPORT_SEQUENTIAL_RUN.md; the verses and Talmud rows this\ndesign rests on are quoted whole in TIME.md in this folder.",
  "chronology table and all fourteen checkpoints, is\nWorld/step9/REPORT_SEQUENTIAL_RUN.md; the fourth book's walk, sitting\nby sitting, with every clock decision written before its code, is\nWorld/step9/NUMBERS_WALK.md; the verses and Talmud rows this design\nrests on are quoted whole in TIME.md in this folder, the fourth\nbook's in its section 12."),
], '## The fourth book: the clock in the wilderness')

time_sec = open(SP + 'time_numbers_section.md', encoding='utf-8').read()
splice(T, [
 ("## What was built from this\n", time_sec + "## What was built from this\n"),
 ("7. **The text's stated totals are checkpoints** (section 7): the\n   machine computes, the text declares, and every mismatch is\n   printed — the flood's 150 days against 147; the 430 years against\n   210 — never repaired.",
  "7. **The text's stated totals are checkpoints** (section 7): the\n   machine computes, the text declares, and every mismatch is\n   printed — the flood's 150 days against 147; the 430 years against\n   210 — never repaired.\n8. **The fourth book ran on the same clock** (section 12, added\n   2026-09-13): its backward dates, the tradition's day-table as\n   reading-placed markers with the text's durations run as timers\n   between them, the thirty-eight years fired in the fortieth year off\n   the itinerary's own date, the dues keyed to the calendar's words,\n   and the two states that end without a number of days."),
], '## 12. The fourth book')
