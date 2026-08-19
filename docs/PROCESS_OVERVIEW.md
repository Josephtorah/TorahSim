# TorahSim — process overview

TorahSim is a verification instrument. It takes the laws of the Hebrew
Bible, as explained by the oral tradition, rewrites them as running computer
code, and then tests that code against the rest of the Hebrew Bible — feeding
it the recorded cases of the Prophets and Writings and checking whether the
machine's verdicts match the verdicts the text itself records.

One chapter — Exodus 21, the first chapter of biblical civil and criminal
law — has been taken to full depth: every word of the oral tradition on it
read and logged, every legal claim extracted and cited, every rule coded,
every test drawn from the tradition's own worked examples. Around it stand
97 derivation units covering Genesis 1 through Exodus 21 continuously, which
the chapter's dependency proof resolves against.

This document describes the process. The companion documents are:

* `CHAIN_OF_TRANSMISSION.md` — the works this project computes with, listed
  in the order they occur.
* `METHOD_LAWS.md` — the binding rules the work was done under.

## The premise: three valid works

The project takes three things as given inputs — valid works in the sense
that we treat them as data to compute with, not as hypotheses to defend:

1. **The Written Torah** — תורה שבכתב ("the Torah that is in writing"): the
   Five Books, and around them the complete Tanakh (the 24-book Hebrew
   Bible) in its three divisions — Torah (the Five Books), Nevi'im ("the
   Prophets"), Ketuvim ("the Writings").

2. **The Oral Torah** — תורה שבעל פה ("the Torah that is upon the mouth"):
   the explanation transmitted alongside the written text. The written verse
   says "six years he shall serve"; the oral explanation says how the years
   are counted, who sells, who buys, what frees early. Without it, the
   written law is not executable; with it, it turns out to be — that is,
   in a real sense, what this project demonstrates.

3. **The chain of transmission** — the ordered sequence of works through
   which the oral explanation was carried and progressively written down,
   from the Mishnah ("the repeated teaching," ~200 CE) through the Talmud
   ("the learning") to the later codes and commentators. Each work in the
   chain is listed, with dates and its role here, in
   `CHAIN_OF_TRANSMISSION.md`.

We do not argue for these premises. We compute with them, and report what
happens when you do.

## The pipeline

Every block of law goes through the same eight steps, in order, with
mechanical gates between them.

### Step 1 — the full scan (oral inversion)

Choose a block of verses (for example Exodus 21:1–11, the slave laws). Then
read **every word** the oral tradition says about that block — not a
selection, not a skim. Coverage is counted row by row in a scan ledger
(block 1 of Exodus 21: 1,962 source rows, 1,962 read), and an incomplete
scan mechanically blocks every later step. The direction matters: we do not
start from the verse and look up support; we start from the tradition's
full record and invert it back onto the verse — which is why this step is
called the oral inversion.

### Step 2 — witnessed claims

Every legal statement found in the scan is extracted as a **claim** with an
identifier (`L12-03` = block on verses 12 and following, claim 3) and a
citation of the work in the chain that witnesses it. Exodus 21 carries 117
witnessed claims across its three blocks. Nothing enters the code without a
claim ID; nothing carries a claim ID without a source.

### Step 3 — machine coding

Claims become code: constants (the sale price, the tariff multipliers, the
term of years), functions (one per legal mechanism — `homicide_verdict`,
`five_heads_award`, `theft_tariff`), and branches. Where the tradition
records a live dispute — a machloket ("division," a recorded disagreement
between authorities) — the code returns **both positions as a data fork**
and decides nothing silently.

### Step 4 — the assert battery

The tests are not invented. They are the tradition's own worked examples —
the cases the sources themselves compute, with the answers the sources
themselves give. The machine must reproduce every one or it does not ship.
This is the step that makes the code falsifiable: change one constant (make
the sheep tariff five instead of four) and the battery fails on the very
verses that witness it.

### Step 5 — chapter assembly

The blocks of a chapter merge into one machine with a shared runtime — one
world clock, shared registries (persons, animals, standing verdicts), and
the seam laws that connect block to block (the verse that ends the slave
laws hands its subject directly to the verse that opens the capital laws).

### Step 6 — the dependency proof

Every place the chapter's law **relies on another verse** is declared as an
edge: this constant inherits from Genesis, this definition imports from
Deuteronomy, this rule is quoted forward by Jeremiah. The proof then checks
every edge mechanically: backward edges must resolve against an actually
derived unit (one of the 97), and forward edges must *not* resolve — a
claim of inheritance from a verse we never derived is a build failure.
Exodus 21 carries 60 proven edges. This is the project's demonstration that
the Hebrew Bible is interconnected as a *system*: the connections are not
asserted in prose, they are checked by a program that can fail.

### Step 7 — the Tanakh run

The assembled machine is then taken to the other 23 books. Recorded cases —
David and Uriah, Amaziah's measured vengeance, the goring-ox patterns, the
kidnapping of Joseph — are encoded as fact patterns and fed to the machine,
and each machine verdict is labeled against the text's own verdict:

* **CONFIRM** — the machine's verdict matches the verdict the text records.
* **DIVERGE** — the machine and the text disagree (reported, never hidden).
* **FORWARD** — the case depends on law not yet derived.
* **NO-VERDICT-IN-TEXT** — the text records no ruling to compare against.

The current scoreboard, across 64 scenes drawn from all 24 books:
**43 CONFIRM / 5 DIVERGE / 7 FORWARD / 9 NO-VERDICT-IN-TEXT.** The run is
served by a small web application (`app/`) so anyone can replay every scene
and inspect every call.

### Step 8 — the simulation direction

The rules engine answers when asked. The next stage — sketched, not yet
built — turns the same laws into *physics*: every event passes through
every law automatically, liability persists as ledger state across years
and generations, and the computed consequences are checked against what the
narrative reports. The first prototype run (the house of David) surfaced
real doctrine on its first execution. See `ROADMAP_SIMULATION.md` and
`sim/`.

## What the results mean — and what they do not

**Certified: consistency.** The law chapter, read through the oral
tradition, forms a coherent computable system; its declared inheritances
from Genesis resolve mechanically; and when its rules are applied to cases
written down centuries later in other books, the machine agrees with the
recorded verdict in the overwhelming majority of decidable cases — including
cases where the later text explicitly says the judge ruled "as it is
written" in the law of Moses.

**Not claimed: agency.** The machine does not decide anything the text left
undecided, does not generate history, and does not prove any theological
proposition. Where the text records no verdict, the machine reports
NO-VERDICT-IN-TEXT rather than inventing one. The honest one-line summary,
which this project adopted as its scope statement: **consistency certified,
agency absent.** This is an experimental model of a legal tradition — not
binding religious law, and not a substitute for studying the sources.

## Repository map

```
docs/       this overview, the chain of transmission, the method laws,
            the source manifest, the simulation roadmap
data/       the Tanakh database (Hebrew text + lemma tags), the English
            gloss lexicon, the index of the 97 derivation units
machines/   the Exodus 21 block machines and the assembled chapter
units/      the 97 derivation units, Genesis 1 – Exodus 21
scans/      the scan ledgers, notes, and witnessed-claim manifests
app/        the Tanakh-run web application (standard library only)
viz/        the inheritance visualizer (which verse feeds which law)
sim/        the simulation sketch (the house of David run)
```

Every program in this repository runs with a stock Python 3 installation —
no packages to install. Start by running the app and clicking through the
64 scenes yourself; open `viz/inheritance.html` to see the chapter's
inheritance drawn as a flow.
