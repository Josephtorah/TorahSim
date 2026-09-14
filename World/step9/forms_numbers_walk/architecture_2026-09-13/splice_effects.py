#!/usr/bin/env python3
# THE EFFECTS UPDATED WITH THE FOURTH BOOK (2026-09-13; the owner: "Update the effects"). Five stories spliced before
# "## How to read the registry"; the head, the registry section and the closer brought current from the prints
# (1,012 effects and the eight kinds' census by the registry's keys; 140 citing Numbers). Every replacement asserted
# unique; refuses to run twice.
P = '<repo-old>/ARCHITECTURE/THE_EFFECTS.md'
S = '<scratch>/effects_numbers_stories.md'
t = open(P, encoding='utf-8').read()
assert '## Story 9' not in t, 'already spliced'
sec = open(S, encoding='utf-8').read()
sec = sec.replace("five rows,\nthe verse texts cut short:", "five rows, the\nother columns cut:")
assert "other columns cut" in sec
def rep(old, new):
    global t
    n = t.count(old); assert n == 1, ('not unique', n, old[:60]); t = t.replace(old, new)
rep("# THE EFFECTS — what a ruling changes, taught from eight stories",
    "# THE EFFECTS — what a ruling changes, taught from thirteen stories")
rep("**A tutorial (rewritten 2026-09-07 for the general reader).**",
    "**A tutorial (rewritten 2026-09-07 for the general reader; five\nstories from the fourth book added 2026-09-13).**")
rep("fires — the change it writes down. Eight stories are worked in full,\ntogether covering every kind of change the program can make. The\ncomplete list of changes (905 of them as of 2026-09-08 — the number\ngrows with every stretch of text compiled)",
    "fires — the change it writes down. Thirteen stories are worked in\nfull — eight from the first three books, five from the fourth —\ntogether covering every kind of change the program can make. The\ncomplete list of changes (1,012 of them as of 2026-09-13 — the number\ngrows with every stretch of text compiled)")
rep("## How to read the registry\n", sec + "## How to read the registry\n")
rep("The effects — 905 as of 2026-09-08 — live in one file (World/step9/effect_vocabulary.yaml)",
    "The effects — 1,012 as of 2026-09-13, 140 of them citing a verse of\nNumbers — live in one file (World/step9/effect_vocabulary.yaml)")
rep("- **what kind of change it is:** a STATUS — a flag on an account.\n  Other kinds: a DEBIT (a debt opens), a TRANSFER (a location moves),\n  a TIMER (a change due later), and a few rarer ones — an entry on\n  Heaven's account for wrongs no court collects, a penalty on the\n  body, a thing destroyed.",
    "- **what kind of change it is:** a STATUS — a flag on an account.\n  The registry has eight kinds, counted as of 2026-09-13: STATUS 650;\n  HEAVEN 99 (an entry on Heaven's account for wrongs no court\n  collects); DEBIT 64 (a debt opens); TRANSFER 59 (a location moves);\n  TIMER 50 (a change due later); BLOCK 40 (an act barred); BODY 39 (a\n  penalty on the body); DESTROY 11 (a thing removed from the world).")
rep("Obligations are computed; acts come from the text.\n",
    "Obligations are computed; acts come from the text.\n\nThree lines in the program's own log sit beside the effects without\nbeing effects, and the fourth book brought each of them into use: a\nRETRO-WRITE, a write dated behind the clock (Story 10); a ROW, a line\nin the population table (Story 9); and a CLOSE, which since 2026-09-12\nis a line of its own, so the ledger can say on which day an entry was\nclosed and by which verse (Stories 9, 11, 12 and 13).\n")
rep("reached into Leviticus for its meaning. The registry file itself is\nthe full list.",
    "reached into Leviticus for its meaning. THE_TOUR.md's section 9\nwalks the fourth book whole, and World/step9/NUMBERS_WALK.md is its\nrecord, sitting by sitting. The registry file itself is the full\nlist.")
open(P, 'w', encoding='utf-8').write(t)
print('spliced', len(t.split('\n')), 'lines')
