# CHRONICLE — a screen for watching the program run (design, not yet built)

**Rewritten 2026-09-07 for the general reader.** This document
describes something that does not exist yet: a screen for watching
the program described in THE_TOUR.md as it runs. It was designed in
a conversation between the owner and two working sessions, and the
design was tightened after the first full run of the three books
gave it real data to show. Nothing here is code.

## The problem

The program reads the Bible's events in order and keeps accounts —
who owes what, who is free, what duty is due on which day. Today
the only way to see what it did is to read a printed log: thousands
of lines like "day 604900: EVENT the flood begins" and "WRITE goes
free on the servant." That is fine for the person who wrote the
program and useless for anyone else. The owner's request was plain:
"I need to see when anything is created, when it changes, but in
summary, with the ability to expand."

## What every such screen has

Anyone who builds a simulation — a flight simulator, a traffic
model, a factory's digital twin — ends up with the same five panes,
because they answer the four questions a viewer always has: What is
the state now? How did we get here? What can I change? Is anything
important happening?

1. **A clock bar** — play, pause, step, and the current time.
2. **A main picture** of the world as it stands.
3. **An inspector** — click one thing and see everything about it.
4. **A few numbers** that are always visible.
5. **An event log** — a scrolling list of what just happened.

Our version of each, in plain words:

- **The clock bar** shows the day, the year (counted from creation,
  and in the exodus era once that begins), and the verse the program
  is at. Because the text is the clock, "step" means "read the next
  event." There are two step sizes: one verse, or one consequence
  inside a verse — because a single event can set off a chain of
  consequences, and you need to walk the chain.
- **The main picture** is the ledger board: a card for every person,
  animal, field, and institution the text has named so far, showing
  its flags and its open duties. When an event touches a card, the
  card lights up. Click any change and you see its cause: the verse,
  the rule that fired, the effect it wrote.
- **The inspector** is one account's whole life: born at this verse,
  bought at that one, pierced, freed at the jubilee.
- **The numbers** — five, no more: the day; how many accounts exist;
  how many duties are open; how many timers are pending; and how
  many consequences the last event set off. The last one is the
  "how alive is the machine" gauge.
- **The event log** is the program's own five kinds of line — event,
  write, timer set, timer cancelled, timer fired — plus the dates
  the text states, in one scrolling list.

## The one rule that shapes the screen

Two kinds of thing appear on the screen, and they must never look
alike. Things the TEXT says happened — a man bought a servant, the
flood began — are the input. Things the PROGRAM computed — a term
opened, a timer fired, a debt closed — are the output. The whole
point of the program is the second kind: the consequences the law
implies but the text never spells out. So the screen colors them
differently, everywhere, always. A reader should be able to look at
any line and know: did the Bible say this, or did the machine work
it out?

## What there is to show, now

The design used to be hypothetical. Since the three books ran in
order on one world, there is a real record to display: 141 events on
the tape, 68 dates stated by the text moving the clock, 2,450 years
of the world's count from creation to the raising of the Tabernacle,
29 accounts whose birth the text dates, 38 rules watching, 246 kinds
of change in the vocabulary — and fourteen checkpoints where the
program's arithmetic was tested against the text's own totals, with
each match and each divergence recorded. The first version of the
screen should simply render that run: one page, built once from the
printed log, no live connection. A live version can come later.

## Two more things worth showing

**The vocabulary of changes, as a page of its own.** The 246
effects are the only changes the program is allowed to make. A page
listing them — when each was added, the verse it comes from, which
rules use it, and how many times it has actually fired — would show
which parts of the law are load-bearing and which never fire. An
effect that never fires across a run that should have used it is a
sign something is wrong, and this page would make that visible.

**The chains.** When one law's consequence triggers another law —
the servant freed because the land's account says "this is the
fiftieth year" — the screen should let you click the last link and
walk back to the first. The program can loop forever if two laws
keep triggering each other; it has a depth limit and stops with an
error if that happens, and the screen should show that error as a
first-class event, not bury it.

## Status

Design only. The owner has not ordered a build. When he does, the
first version is a single web page rendered from one run of the
sequential tape, in the folder this document sits in.
