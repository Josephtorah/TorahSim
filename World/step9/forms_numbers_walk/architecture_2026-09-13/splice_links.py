import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE LINKS UPDATED WITH THE FOURTH BOOK (2026-09-13; the owner: "Ok the links go"). Five examples spliced before
# "## How the links are found"; the head and the rule section brought current from dependency_dispositions.yaml
# and the gate's print (455 / 48 / 9 / 143 over 482 edges + 173 pointers; the fourth book's 178 edges 151 / 1 / 26,
# 45 pointers; CALL 129 / VIA 15 / PARAMETER 3 / OWED 5 / FALSE 26). Every replacement asserted unique; refuses twice.
P = (_ROOT + '/ARCHITECTURE/THE_LINKS.md')
S = '<scratch>/links_numbers_examples.md'
t = open(P, encoding='utf-8').read()
assert '## Example 9' not in t, 'already spliced'
sec = open(S, encoding='utf-8').read()
def rep(old, new):
    global t
    n = t.count(old); assert n == 1, ('not unique', n, old[:70]); t = t.replace(old, new)
rep("# THE LINKS — how the laws are wired to each other, taught from two examples",
    "# THE LINKS — how the laws are wired to each other, taught from two examples and a fourth book")
rep("**A tutorial (rewritten 2026-09-07 for the general reader).** This\ndocument shows one thing:",
    "**A tutorial (rewritten 2026-09-07 for the general reader; five\nexamples from the fourth book added 2026-09-13).** This\ndocument shows one thing:")
rep("check. Eight dependencies are worked in full, one of each kind. The complete list — 162\nreferences, 31 transfers, 6 open hypotheses, and 40 edges that carry\nno rule at all — lives in the program's own records; this document teaches you how to read one.",
    "check. Thirteen dependencies are worked in full — eight from the\nfirst three books, five from the fourth — one of each kind. The\ncomplete list — 455 references, 48 transfers, 9 open hypotheses, and\n143 edges that carry no rule at all, over 482 edges and 173 pointers\nas of 2026-09-13 — lives in the program's own records; this document\nteaches you how to read one.")
rep("## How the links are found — and a rule the tradition insists on\n", sec + "## How the links are found — and a rule the tradition insists on\n")
rep("rather than a teacher) and undid it. Today the count is 162\nreferences, 31 transfers with teachers, 6 hypotheses — and 40 edges\nof a fourth kind, NONE:",
    "rather than a teacher) and undid it. Today the count is 455\nreferences, 48 transfers with teachers, 9 hypotheses — and 143 edges\nof a fourth kind, NONE:")
rep("that nobody mistakes them for a law crossing.\n",
    "that nobody mistakes them for a law crossing.\n\nThe fourth book, read and compiled between 2026-09-09 and 2026-09-13,\nadded 178 edges and 45 pointers to that list: 151 references, one\ntransfer with its teacher (Example 10), 26 homographs refused\n(Example 11), and no hypothesis. Beside the label, every edge now\ncarries a DISPOSITION saying how the link is wired: a live CALL (129\nof the fourth book's), a path VIA another program (15), a PARAMETER\ncarried rather than a procedure (3), a call OWED with its debt named\n(5), or FALSE (26). A gate reads the records before every run of the\nprogram and refuses an edge without both.\n")
rep("THE_EFFECTS.md shows what happens when a linked law fires — the\nchange it writes. THE_CLOCK.md shows how \"forever\" in the servant law\nreached into Leviticus 25 for its clock.",
    "THE_EFFECTS.md shows what happens when a linked law fires — the\nchange it writes. THE_CLOCK.md shows how \"forever\" in the servant law\nreached into Leviticus 25 for its clock. THE_TOUR.md's section 9\nwalks the fourth book whole, and World/step9/NUMBERS_WALK.md is the\nrecord of every link read there, sitting by sitting.")
open(P, 'w', encoding='utf-8').write(t)
print('spliced', len(t.split('\n')), 'lines')
