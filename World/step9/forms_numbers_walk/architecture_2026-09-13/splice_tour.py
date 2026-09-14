#!/usr/bin/env python3
# THE TOUR UPDATED WITH THE NUMBERS INSIGHTS (2026-09-13; the owner: "Update the tour document with the numbers insights").
# Every replacement asserted unique; the new section spliced before the mini-lab; the two later sections renumbered; the counts
# brought current from the prints (57 runners by ls; 62 daemons by DAEMON_INDEX.md; 1,012 effects by the registry's keys;
# the link census 455 / 48 / 9 / 143 of 482 + 173 by ref_dep_gate3.out). Idempotent: refuses to run twice.
import re, sys
P = '<repo-old>/ARCHITECTURE/THE_TOUR.md'
S = '<scratch>/tour_section9.md'
t = open(P, encoding='utf-8').read()
assert '## 9. The fourth book' not in t, 'already spliced'
sec = open(S, encoding='utf-8').read().rstrip('\n') + '\n\n'

def rep(old, new, count=1):
    global t
    n = t.count(old)
    assert n == count, ('not unique', n, old[:60])
    t = t.replace(old, new)

# the head note
rep("**A tutorial (rewritten 2026-09-07 for readers who know nothing about\nthis project).**",
    "**A tutorial (rewritten 2026-09-07 for readers who know nothing about\nthis project; section 9, the fourth book, added 2026-09-13 with the\ncounts brought current).**")
# the seven parts — the diagram and the bullets
rep("│ (39 programs)    │", "│ (57 programs)    │")
rep("│ (43 watchers)│", "│ (62 watchers)│")
rep("│ (905 allowed │", "│ (1012 allowed│")
rep("thirty-nine of them as of 2026-09-08 (the count grows with every\n  stretch compiled), one per stretch of the text (Exodus 21,\n  Leviticus 5, Leviticus 24, and so on).",
    "fifty-seven of them as of 2026-09-13 (the count grows with every\n  stretch compiled), one per stretch of the text (Exodus 21,\n  Leviticus 5, Leviticus 24, Numbers 35, and so on).")
rep("There are forty-three of them as of 2026-09-08.", "There are sixty-two of them as of 2026-09-13.")
rep("make — 905 of them as of 2026-09-08, every one a verb the text",
    "make — 1,012 of them as of 2026-09-13, every one a verb the text")
# the links' census
m = re.search(r"Every link\nis labeled \(the counts here are as of 2026-09-07\):.*?complete\.", t, re.S)
assert m, 'the links paragraph'
t = t[:m.start()] + ("Every link\n"
    "is labeled (the counts here are as of 2026-09-13, over 482 edges\n"
    "and 173 pointers): 455 are references (the text points, the program\n"
    "follows) and 48 are transfers (a law carried from one passage to\n"
    "another on a shared word — and each of those names the teacher in\n"
    "the tradition who made that transfer, because the tradition's own\n"
    "rule forbids inventing one). Nine are marked as hypotheses: links\n"
    "we believe but cannot yet source, kept visible and never counted as\n"
    "proven. A hundred and forty-three more connections carry no law\n"
    "across them at all — a test registering another program's rules, a\n"
    "word that merely looks the same in two places — and are labeled so,\n"
    "to keep the list complete.") + t[m.end():]
# section 8's tail
rep("All four were\nargued out between the working sessions and are scheduled as the\nnext clock sitting, pending the owner's word.",
    "All four were\nbuilt the next day: every law now declares the verse that speaks it\nand the act that switches it on, every undated event says what\nplaced it (the text, a reading of the tradition, or the page's\norder), the tradition's year count is a rendering of the machine's,\nand the text's own day-words are read. Section 9 shows them at work\non the fourth book.")
# the splice and the renumbering
rep("## 9. Mini-lab: add a third event to the same map", sec + "## 10. Mini-lab: add a third event to the same map")
rep("## 10. Where to look next", "## 11. Where to look next")
rep("- **CHRONICLE.md** — the design for watching all of this run on one\n  screen.",
    "- **CHRONICLE.md** — the design for watching all of this run on one\n  screen.\n"
    "- **World/step9/NUMBERS_WALK.md** — the fourth book's walk, one\n  section per sitting: the design written before the code, and the\n  record as built after it. **World/step9/THE_TENT.md** holds the\n  four cases; **World/step9/THE_LOOP.md** is the running simulation's\n  own map — the journal, the installation of laws, the cursor,\n  scenarios, the register gate.\n"
    "- **What_Numbers_Taught_The_Machine.md** and\n  **What_Numbers_Does_For_The_Simulation.md**, at the repository's\n  root, each with a listening copy beside it — two long tutorials on\n  the fourth book, every verse quoted whole and the machine's own\n  lines beside them.")
rep("the thirty-four span\n  programs beside it", "the fifty-seven span\n  programs beside it")
open(P, 'w', encoding='utf-8').write(t)
print('spliced', len(t.split('\n')), 'lines')
