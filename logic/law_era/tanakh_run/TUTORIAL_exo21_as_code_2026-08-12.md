# Is Exodus 21 computer code? — a tutorial for a non-programmer

**Who this is for:** the owner, who is not a programmer, and who needs
enough grounding to JUDGE the claim himself — not to take my word for it.
Every piece of Python in this document is quoted from the real machine
files in `logic/law_era/`, and every claim about the text points at
verses you can read in the app's verse panel. Nothing here asks for
trust; everything here can be checked.

**The one-sentence claim being tested:** Exodus 21, read the way the
tradition reads it, has the *structure* of a computer program — and to
test that, we actually built the program, and then ran the rest of the
Hebrew Bible through it to see if the Bible itself behaves like a world
where that program is in force.

---

## Part 1 — What computer code actually is

Strip away the mystique and code is three things:

1. **Rules written so precisely that a machine with no judgment can
   apply them.** A machine cannot wink, cannot "know what you meant,"
   cannot bend. If the rule says *six years*, the machine frees the
   slave on day 2,190 and not one day later.
2. **Rules that take INPUT and produce OUTPUT, the same way every
   time.** Give the rule the same facts twice, you get the same verdict
   twice. This is called *determinism*.
3. **Rules that can FAIL.** Real code can be run, and therefore can be
   caught being wrong. Prose can only be argued with; code can be
   *executed* against test cases and refuse to work.

Keep those three in mind — precision, determinism, failability —
because they are the standard we will hold the chapter to.

A few words of Python (the programming language used here), so the
excerpts below read as sentences and not hieroglyphics:

| You'll see | It means |
|---|---|
| `def name(...):` | "Here I define a rule called *name*, taking these facts as input." |
| `if X: return Y` | "If fact X holds, the verdict is Y — stop here." |
| `TERM_YEARS = 6` | "A constant: a number the law fixes forever." |
| `{"key": value}` | "A record card with labeled fields." |
| `assert X, "msg"` | "SELF-TEST: X must be true. If it is not, CRASH and print msg." |
| `ox["gorings"]` | "Look up the *gorings* field on the ox's record card." |
| `b3.status(ox)` | "Run the rule called *status* from block 3 on this ox." |

That last row is the important one for your question: **one rule using
another rule is called a "call."** When we ask "how does a verse call
another verse," we are asking: does verse A *use a definition, a
boundary, or a constant that lives in verse B* — the way one piece of
code uses another?

---

## Part 2 — The shape of the chapter: why anyone would say "this is code"

Open Exodus 21 and look at the grammar of the laws themselves. Almost
every law has this skeleton:

> **כי** ("when/if") — *condition* — then *consequence*.
> **אם** ("if") — *sub-condition* — then *different consequence*.

That is not a poem's grammar. It is the grammar of a **case statement**
— the most basic structure in all of programming: *if this, do that; but
if that, do this other thing.* Watch it in the chapter's own words
(21:2-4, condensed):

- כי תקנה עבד עברי ("WHEN you acquire a Hebrew slave") — the case opens.
- שש שנים יעבד ("six years he shall serve") — a **constant**: 6.
- ובשבעת יצא לחפשי חנם ("and in the seventh he goes out free, for
  nothing") — a **timer expiring**, and a second constant: exit price 0.
- אם בגפו יבא ("IF he came in alone...") — branch one.
- אם בעל אשה הוא ("IF he is a husband...") — branch two.
- אם אדניו יתן לו אשה ("IF his master gave him a wife...") — branch
  three, with a different data-outcome (the wife and children stay).

Condition, constant, timer, branch, branch, branch. The chapter
continues like this for thirty-seven verses: homicide with four
intent-grades, an injury schedule with five separate payment heads, an
ox whose LEGAL STATUS CHANGES based on its recorded history, a pit
whose liability depends on its depth, a theft tariff with two different
multipliers. These are the working parts of a legal *machine* — and the
question is whether they actually mesh, or only look like they do.

The only honest way to find out: **build it and run it.** A machine
that meshes will execute; a machine that doesn't will crash on its own
contradictions.

---

## Part 3 — One law, walked from Hebrew to running code

Take the most machine-like law in the chapter: the goring ox
(21:28-29). First the verses, word by word.

**Verse 28:** וכי יגח שור את איש ("and WHEN an ox gores a man") — ומת
("and he dies") — סקול יסקל השור ("the ox shall surely be STONED") — ולא
יאכל את בשרו ("and its flesh shall not be eaten") — ובעל השור נקי ("and
the ox's OWNER is CLEAR").

**Verse 29:** ואם שור נגח הוא מתמל שלשם ("but IF it was a GORING ox
from YESTERDAY AND THE DAY BEFORE") — והועד בבעליו ("and its owner was
WARNED") — ולא ישמרנו ("and he did not guard it") — והמית איש ("and it
killed a man") — השור יסקל וגם בעליו יומת ("the ox is stoned AND its
owner too shall die").

Read verse 29 again slowly, because it contains the single most
code-like idea in the whole chapter: **the same act — ox kills man —
produces a different verdict depending on the ox's recorded HISTORY.**
"From yesterday and the day before" means: this ox has a *track
record*, the owner was formally *notified*, and from that moment the
ox carries a different legal STATUS. The tradition names the two
states: תם ("innocent" — the default) and מועד ("forewarned" — the
escalated state). Programmers have a name for exactly this pattern: a
**state machine** — a thing whose response to an event depends on what
state its past has put it in.

The oral tradition then supplies the parameters the written verse
compresses: three gorings vest the state; on three separate DAYS (R.
Yehudah's rule); the warning must happen in the owner's presence; and
one day of children safely petting the ox breaks the state again
(because breaking a habit is proof, where forming one is slow). Here is
that entire paragraph as it now exists in the machine — this is real,
running code from `exo_21_v2_block3_DRAFT.py`, followed by a plain-
English reading of every line:

```python
def status(ox, species="ox", context="weekday", victim_is_man=False):
    if ox["clean_pet_days"] >= REVERSION_CLEAN_DAYS:
        return "tam"
    hits = [g for g in ox["gorings"] if g[2] == context]
    if victim_is_man:
        hits = [g for g in hits if g[1] == "man"]
    if len(hits) < MUAD_GORINGS:
        return "tam"
    if MUAD_DAYS_RULE and len({d for d, s, c in hits}) < MUAD_GORINGS:
        return "tam"
    if not ox["warned_in_owner_presence"]:
        return "tam"
    return "muad"
```

Line by line, in English:

1. *"Define the rule STATUS: give me an ox's record card, and I will
   tell you its legal state."*
2. *"If the ox has had even one clean petting-day, it is תם
   ('innocent'). Stop."* — the hysteresis rule.
3. *"Collect only the gorings that happened in the SAME context"* —
   because an ox forewarned for Sabbaths is not forewarned for
   weekdays (the tradition's context-indexing, encoded as a filter).
4. *"If we're asking about goring a MAN, count only its attacks on
   men"* — beast-kills never escalate it toward man (אדם אית ליה מזלא,
   "a man has protective fortune" — the two tracks never merge).
5. *"Fewer than three? Still innocent."* — the constant MUAD_GORINGS=3.
6. *"Three gorings but not on three separate DAYS? Still innocent."* —
   R. Yehudah's days-rule, encoded.
7. *"No formal warning in the owner's presence? Still innocent."* —
   והועד בבעליו ("and its owner was warned"), verse 29's own word.
8. *"Otherwise: מועד ('forewarned')."*

Now the payoff question: **is that code, or is that my paraphrase
dressed up?** The answer is checkable: the file ends with a battery of
`assert` self-tests that run the tradition's own worked cases through
this rule — gore it three times in one day: still tam; on three days:
muad; one petting day after: tam again; three Sabbath gorings: muad on
Sabbath, tam on Tuesday. Run the file and the machine either produces
every one of those answers or it crashes on the spot:

```
python3 logic/law_era/exo_21_v2_block3_DRAFT.py
→ BLOCK 3 (+21:37 tail) DRAFT: all asserts GREEN.
```

Prose cannot do this. Only code can pass or fail a test run.

---

## Part 4 — How a verse calls another verse (your question, six ways)

In programming, "calling" means one piece of code USING something —
a definition, a boundary, a constant — that lives somewhere else. The
Torah does this constantly, and the tradition's reading methods are,
seen through this lens, the *linking mechanisms*. Here are the six
mechanisms, each with a worked example you can check in the app.

### Mechanism 1 — the keyword call (the tradition calls it gezerah shavah, "verbal analogy")

Two verses share a distinctive WORD; the tradition reads the shared
word as a license to carry a definition from one to the other. That is
precisely how a *function name* works: writing `status(...)` in one
file runs the definition written in another.

**Worked example — the 2,000-cubit Sabbath limit.**
Exodus 21:13 (refuge): ושמתי לך מקום ("I will appoint you a PLACE" —
the word מקום, *makom*). Exodus 16:29 (the manna, one chapter's world
away): אל יצא איש ממקומו ביום השביעי ("let no man go out of his PLACE
on the seventh day") — same word. The tradition (Issi ben Akiva) joins
them: the refuge "place" is a city plus its 2,000-cubit surround —
therefore "his place" on the Sabbath is ALSO 2,000 cubits. The Sabbath
walking-limit that observant Jews keep to this day is *computed off
the refuge verse* through a keyword link. In the machine this is the
constant `TECHUM_CUBITS = 2000` in block 2, and the link is a declared,
machine-checked edge to Exod 16:29.

**Second example — the payment proof.** Exodus 21:24 says עין תחת עין
("eye IN PLACE OF — *tachat* — eye"). Does תחת mean retaliation or
payment? Verse 21:36, eight verses later, uses the same word about
oxen: שלם ישלם שור תחת השור ("he shall surely PAY an ox in place of
the ox") — there תחת is undeniably *payment*. Rav Ashi's argument:
same keyword, same meaning — the eye-clause pays. One verse's clear
case supplies the other verse's disputed meaning, *by keyword*. In the
assembled machine this became the seam-law `seam_tachat_anchor()`: a
block-2 rule proven by a block-3 verse, now supplied internally.

### Mechanism 2 — the imported definition

A law uses a word it never defines; the definition lives in a
NARRATIVE, books away. In code: using a term defined in another file.

**Worked example — אסון ("calamity").** The brawl-law (21:22-23) turns
entirely on this word: ולא יהיה אסון ענוש יענש ("if there is NO
calamity, he shall surely be fined") — ואם אסון יהיה ("but if there IS
calamity — life in place of life"). The statute never says what אסון
is. The word's home is Genesis 42:38 — Jacob refusing to send
Benjamin: פן יקראנו אסון ("lest CALAMITY befall him"). The tradition
imports Jacob's word to define the statute's word — and then builds on
the link: Jacob feared what HEAVEN might do, so the law's אסון also
covers Heaven-inflicted liability, which is why a Heaven-liable act
cancels co-owed payments just as a court-death does (the kim leih
rule, "he already stands in the greater liability"). A Genesis
narrative is functioning as the *definitions file* for an Exodus
statute. In the machine: a declared edge, Gen 42:38 → and it RESOLVES,
because Genesis 42 is inside the already-derived corpus
(`gen_65_first_descent`).

### Mechanism 3 — the imported boundary

A rule's LIMIT is stated in a different book, and without that limit
the rule misfires. In code: a boundary condition imported from another
module.

**Worked example — why the eye pays money but the murderer dies.**
Read 21:23-24 flat and you get a paradox: נפש תחת נפש ("life in place
of life") sits right next to עין תחת עין ("eye in place of eye") — if
one is literal, why not the other? The boundary lives in Numbers
35:31: ולא תקחו כפר לנפש רצח ("you shall take NO ransom for the LIFE
of a murderer"). The tradition reads the precision: no ransom for a
murderer's *life* — "but you DO take ransom for limbs." That one verse
is the type-boundary that splits the list: nefesh literal, everything
below it monetary. The machine encodes this as `tachat_payment(item)` —
try it in the app's Custom Facts tab — and declares Numbers 35:31 as a
FORWARD demand: a boundary the machine consumes from a book not yet
derived. The dependency is not hidden; it is a ledger entry.

### Mechanism 4 — the exported constant

A NUMBER fixed in the statute surfaces elsewhere in the Bible — in a
prophet's mouth, in a king's verdict — still carrying its legal
meaning. In code: a constant defined once, referenced everywhere.

**Worked example A — the thirty.** Exodus 21:32 fixes the ox-kills-
slave tariff: כסף שלשים שקלים יתן לאדניו ("THIRTY shekels of silver he
shall give to his master") — a flat statutory constant. Zechariah
11:12, centuries later: וישקלו את שכרי שלשים כסף ("they weighed out my
wage: THIRTY of silver") — and God's bitter comment calls it "the
majestic price I was priced by them": the slave-tariff constant,
quoted as an insult with its legal meaning intact. The machine:
`SLAVE_TARIFF = 30`, with Zech 11:12 as a declared demand.

**Worked example B — the four.** Exodus 21:37: וארבע צאן תחת השה
("FOUR sheep in place of the sheep"). Second Samuel 12: Nathan tells
David the ewe-parable; David erupts: ואת הכבשה ישלם ארבעתים ("and the
ewe he shall repay FOURFOLD"). The king, ruling from the bench, outputs
the statute's exact constant for the statute's exact case (sheep,
stolen, disposed). And the detail that proves the tradition understood
the SYSTEM and not just the number: Nathan left the *murder* out of
the parable — because for a death the law awards no payment (the
absorption rule), so the parable only charges what the tariff can
collect. In the machine: `theft_tariff("sheep")["multiplier"] == 4`,
and the app runs this call live on the Nathan scene.

### Mechanism 5 — the seam (verse ORDER as syntax)

Sometimes the link is pure POSITION: the last words of one law touch
the first words of the next, and the tradition reads the juxtaposition
itself as carrying a rule. In code: the program's *layout* is
meaningful — think of how one instruction falls through into the next.

**Worked example — "no money: he dies."** Block 1 ends (21:11) with
the amah's exit: ויצאה חנם אין כסף ("she goes out for nothing — NO
MONEY"). Block 2 opens (21:12): מכה איש ומת מות יומת ("one who strikes
a man and he dies shall surely be put to death"). The tradition
(Lekach Tov, and the Tur independently) reads the seam: **"no money —
he dies"**: where a court gives death, it does not ALSO award payment.
That is the kim leih absorption principle — one of the deepest rules
in the whole system — derived from the CONTACT POINT between two laws.
In the machine: `kim_leih(death_class=True)` returns payment ABSORBED,
and the edge "Exodus 21:11" is classified INTERNAL in the assembled
chapter: a link the chapter supplies to itself.

### Mechanism 6 — the explicit quotation

The rarest and plainest: a later book QUOTES the statute and applies
it. In code: calling the function by its full name.

**Worked example — Jeremiah 34.** Zedekiah's Jerusalem frees its
slaves, then re-enslaves them. Jeremiah's indictment quotes the
release law verbatim: מקץ שבע שנים תשלחו איש את אחיו העברי ("at the
end of seven years you shall release each his Hebrew brother") — ועבדך
שש שנים ("and he shall serve you six years") — Jer 34:14, citing the
composed Exodus/Deuteronomy release law. Then the sentence, measure
for measure: "you did not proclaim release — behold, I proclaim a
release FOR you: to the sword, to pestilence, to famine" (34:17). The
machine's side: `term_status(slave, 6*365)` returns FREE — the
narrative's breach is judged BY the statute's own clock, and the
prophet says so in the statute's own words.

**Those six mechanisms are the answer to your question.** A verse
"calls" another verse by keyword (shared distinctive word), by
definition-import (a word defined in a narrative), by boundary-import
(a limit stated in another book), by constant-export (a number reused
with meaning intact), by seam (position as syntax), and by quotation.
The machine does not invent these links — the tradition asserted them
for two thousand years. What the machine adds is that every asserted
link is now a DECLARED, CHECKED edge.

---

## Part 5 — The dependency ledger: how the links are checked

Every machine file ends with a table called `DEPENDS`. One real row:

```python
("the ason-genus import", "Genesis", 42, 38, "back", "L12-05",
 "פן יקראנו אסון — Jacob's word welds Heaven's docket to man's"),
```

Read it as a sentence: *"This machine element imports something from
Genesis 42:38; I declare that verse is BEHIND me (already derived);
the claim justifying this is L12-05 in the witness manifest; here is
what is imported."*

Then a checking function (`verify_dependencies`) opens the project's
database of already-derived, frozen units and tests every row:

- A row declared **"back"** must land inside a frozen unit — or the
  program CRASHES. (The declaration is not allowed to lie.)
- A row declared **"fwd"** (forward) must NOT land — it is an honest
  IOU: "this rule consumes a verse we have not derived yet."

For the assembled chapter the ledger reads: **60 edges — 2 internal
(the chapter supplying itself), 31 resolved across 28 verses in 17
frozen units, 27 forward across 26 open verses.** That sentence is the
inheritance-and-dependency claim in checkable form: not "the Bible is
interconnected" as a slogan, but sixty specific, named, machine-
verified connections — each one either PROVEN against the corpus,
self-supplied, or honestly marked open.

---

## Part 6 — Watching state change: the before and after

You asked earlier what the "before state and after state" are. Here is
the cleanest demonstration, from the assembly's World — the part you
were stepping through in the debugger:

| World-day | Event | Ox status BEFORE | Ox status AFTER |
|---|---|---|---|
| 1 | gores (owner warned, present) | תם ("innocent") | תם — one strike |
| 2 | gores again | תם | תם — two strikes |
| 3 | gores a third time, third day | תם | **מועד ("forewarned")** |
| 4 | children pet it safely all day | מועד | **תם again** — the habit is broken |

Same ox, same act on day 3 as on day 1 — different legal consequence,
because the STATE changed. And the money follows the state: the תם
owner pays half-damages, capped at the ox's own body; the מועד owner
pays in full, from the best of his land. Then the second state-write:
when a court CONDEMNS the ox, the flesh becomes forbidden at the
verdict — before any stone is thrown — and if the ox is executed, the
verdict is "spent" and the carcass may be used. Verdicts themselves
are events that write state. This is why the project says **"verdicts
are per-scene; facts are sequential"** — each judgment is computed
fresh, but the world it consults accumulates.

---

## Part 7 — The self-tests: why "all asserts green" is the whole ballgame

Scattered through the machine are ~150 `assert` lines. Each one is a
worked example FROM THE TRADITION turned into a trap: if my encoding
of the law ever disagrees with the tradition's own answer, the program
refuses to run. Three real ones:

```python
assert theft_tariff("sheep")["multiplier"] == 4, \
    "Nathan's lamb: ארבעתים ('fourfold') — the catalog's flagship constant"

assert status(sab, context="sabbath") == "muad", "mu'ad for Sabbaths"
assert status(sab, context="weekday") == "tam",  "tame on weekdays"

assert OX_TARIFF == SHEEP_TARIFF + 1 == KEFEL * KEFEL + 1, \
    "R. Meir's arithmetic: double-of-double, +1 for the labor"
```

That last one is worth savoring: Rabbi Meir explains the 5-for-ox /
4-for-sheep asymmetry as *composed arithmetic* — the tariff is the
double (2), doubled again (4), plus one for the ox's lost labor (5).
The machine ASSERTS his equation: 5 == 2×2+1. If the constants were
arbitrary, no such equation would hold.

**And here is the experiment I invite you to run** — the single most
convincing thing a non-programmer can do. Open
`logic/law_era/exo_21_v2_block3_DRAFT.py`, find the line
`SHEEP_TARIFF = 4`, change the 4 to a 5, save, and run:

```
python3 logic/law_era/exo_21_v2_block3_DRAFT.py
```

The machine will CRASH — twice over: first on the Nathan assert
(David's fourfold no longer matches), then on R. Meir's equation. Then
change it back and watch it go green. That crash is the proof of
code-ness: **the system contains enough internal cross-bracing that a
one-digit lie is caught from two independent directions** — once by a
king's verdict in 2 Samuel, once by a rabbi's arithmetic. Prose absorbs
errors; code rejects them.

---

## Part 8 — What the 57-scene run actually established

The app took the compiled chapter and executed 57 scenes harvested
from all 24 books — every place the sweep found the chapter's laws,
words, or constants operating. Result of the first full run:

- **37 CONFIRM** — the text behaves as the machine rules. David's
  fourfold. The Gibeonites refusing money for murdered lives (the
  Numbers 35:31 boundary, spoken by non-Israelites). Solomon executing
  the altar-clause on Joab in its own words. Jeremiah 34's breach
  judged by the release-clock. Joseph's brothers exempt on the kidnap
  statute's own element-checklist.
- **5 DIVERGE** — and each divergence, examined, is a *finding with a
  reason*: Achan's oxen die under cherem (the ban — a different
  jurisdiction than damages-law); Samson's eye-for-eye is war, not
  court; Naboth's trial is the protocol *abused* (exposing exactly the
  gap the plotting-witness law of Deut 19 — a declared forward demand
  — exists to close); the Tekoa widow gets CROWN clemency the court
  machine deliberately lacks; Jacob-under-Laban shows the pre-statute
  world the statute exists to fix.
- **6 FORWARD** — scenes needing laws from the next block (the
  borrowed axe-head that cries "and it was BORROWED!" needs Exod
  22:13's borrower-liability — not yet derived, never faked).
- **9 NO-VERDICT-IN-TEXT** — figures and doctrines where no case runs.

The number to hold onto is not 37; it is **5**. A test that CANNOT
diverge proves nothing. This one diverged five times, and each
divergence classified cleanly instead of breaking the model. That is
what an honest instrument looks like.

---

## Part 9 — Where the code came from (and where interpretation lives)

Total honesty about the pipeline, because you should know what is
text, what is tradition, and what is me:

1. **The verses** fix the skeleton: the cases, the constants (6 years,
   30 shekels, 5-and-4), the branch structure, the state-change of the
   forewarned ox.
2. **The oral tradition** supplies the parameters the written text
   compresses: that "yesterday and the day before" = three; that the
   window is 24 hours; that the warning needs the owner present. This
   project READ that tradition exhaustively first — 4,903 witness-
   texts for this one chapter, every one logged in a ledger — and
   distilled 110 claims, each carrying its named sources. The machine
   encodes THE TRADITION'S reading, not my invention; where the
   tradition itself preserves a live dispute (does the altar shield
   from the king? is transferred intent capital?), the machine returns
   BOTH positions as data rather than silently picking one.
3. **The programmer's hand** (mine) chose names, order, and phrasing —
   and every choice is audit-able: each rule carries a claim-ID, each
   claim carries its sources, and the asserts punish me if I drifted.

What this does NOT prove: who wrote the text, or any theological
claim. What it DOES prove is structural: **the chapter compiles** (its
rules mesh without contradiction under ~150 self-tests), **its links
resolve** (60 declared edges, checked), and **the wider text runs on
it** (37 confirmations, 5 classified divergences). Whether a legal
text from the ancient world *should* be able to do that is the
question the result leaves you with.

---

## Part 10 — Try it yourself: ten minutes at the machine

Open the Cursor terminal (⌃`), make sure you're in the project
(`cd ~/Torah_Grok`), then run Python in *interactive* mode — the `-i`
flag means "run the file, then leave me at a prompt with everything
loaded":

```
python3 -i logic/law_era/exo_21_v2_DRAFT.py
```

You'll watch all the batteries run green, then get a `>>>` prompt.
Now the machine is live under your fingers. Type these one at a time
(press Enter after each; `>>>` is the prompt, don't type it):

```python
>>> b3.theft_tariff("sheep")["multiplier"]        # David's verdict
4
>>> b3.theft_tariff("ox")["multiplier"]           # the ox premium
5
>>> b2.tachat_payment("eye")["mode"]              # eye for eye =
'money'
>>> b2.tachat_payment("nefesh")["mode"]           # but a life =
'death'
>>> b3.kofer_admissible("human_murderer")         # ransom a murderer?
False
>>> b2.joseph_case()                              # the brothers' trial
{'verdict': 'exempt', 'missing': ['his domain (ונמצא בידו \'found in
his hand\')', 'use (והתעמר בו)']}
>>> w = World()                                   # an empty world
>>> ox = w.register_ox("test")
>>> for day in (1, 2, 3):
...     w.day = day
...     w.goring(ox, owner_present_testimony=True)
...
>>> w.ox_status(ox)                               # after three days
'muad'
>>> w.petting_day(ox)
>>> w.ox_status(ox)                               # the habit broken
'tam'
>>> exit()
```

Every answer you just got is the tradition's answer, produced by rules
a judgment-free machine executed. That — nothing more mystical — is
what it means that Exodus 21 is code.

---

*Written 2026-08-12 at the owner's request, part of the learning
narrative. Companion files: the session log (the how-it-was-built
story), the plan doc (the test's design), and the app
(`python3 logic/law_era/tanakh_run/app.py` → http://127.0.0.1:8021).
Experimental model — not binding religious law.*
