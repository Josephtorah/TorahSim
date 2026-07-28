# Tutorial for beginners — the pre-code logic methods

**Date:** 2026-07-28
**Audience:** English-first beginner; no logic or Hebrew background assumed
**Companion:** `TUTORIAL_precode_logic_methods_AUDIO_2026-07-28.md` — same lesson as flowing narration for an audio reader (no tables or symbols)
**Applied example:** `EXPERIMENT_precode_logic_gen_1_1_to_2_3_2026-07-28.md` (Gen 1:1–10 done with these methods)
**Status:** teaching document · methods are lenses, labeled hypothesis when applied · not binding religious law

---

## 0. What "pre-code logic" means here

All of these methods are ways of writing **precise statements on paper** — with a pencil, centuries or decades before (or simply without) computers. None of them require running anything. In this project, that matters because of a standing rule: **Torah logic is derived by hand into documents; code may only interpret those documents later.** These methods are the hand tools.

Every method below answers one question well. None answers every question. The skill is knowing which tool a verse is asking for.

The running example throughout is Genesis 1:3, the shortest complete "fiat" in the Torah:

> וַיֹּאמֶר אֱלֹהִים יְהִי אוֹר וַיְהִי־אוֹר
> va-yomer Elohim yehi or va-yehi or
> "And God said: let there be light — and there was light."

---

## 1. Predicate logic — the foundation under everything

**One idea:** a sentence can be split into a *predicate* (the claim) and its *arguments* (the things the claim is about). "Light exists" becomes `exists(light)`. "God created the heavens" becomes `created(God, heavens)`.

**Where it comes from:** Gottlob Frege, 1879 — the single biggest step in logic since Aristotle. Pure paper.

**Why we need it:** every other method writes its statements *in* this form. It is the grammar of all the layers.

**Torah use:** each leaf of a ta'amim tree tends to supply either a predicate (usually the verb) or an argument (usually a noun phrase). The tree tells you which pieces belong together; predicate logic gives you the slots to put them in.

**A special trick — set-builder:** the Hebrew word אֲשֶׁר / asher / "which" opens a defining clause. "The waters *which were under* the firmament" is, in paper logic, a defined set: all x such that x is water and x is under the firmament. Genesis 1:7 uses two of these to turn vague "waters and waters" into two precisely defined sets.

**Limit:** predicate logic states facts. It cannot express commands, time, or purpose by itself. That is what the other layers add.

---

## 2. Speech act theory — saying as doing

**One idea:** some sentences do not *describe* the world; they *change* it by being said. "I now pronounce you married" doesn't report a marriage — it performs one.

**Where it comes from:** J. L. Austin's Oxford lectures, 1950s (*How to Do Things with Words*).

**Torah use — two places:**
1. **The fiats.** וַיֹּאמֶר / va-yomer / "and he said" opens a *performative* — the saying is the doing. We write it `DECLARE(Elohim, …)`, a speech-act wrapper around whatever is commanded inside.
2. **The namings.** וַיִּקְרָא / va-yiqra / "and he called" is not a truth claim; it *installs a name*. Calling the light יוֹם / yom / "day" writes an entry into a registry. It cannot be true or false — only done or not done.

**Limit:** speech act theory tells you *that* an utterance changes the world, not *what* the new state is. The content inside the DECLARE needs the other layers.

---

## 3. Deontic logic — the logic of commands

**One idea:** ordinary logic handles "it is raining." Deontic logic handles "it *ought to* rain" — obligation, permission, prohibition. Its basic operator is O(p): "it is obligatory that p."

**Where it comes from:** Georg Henrik von Wright, 1951, building on medieval and even ancient roots. The name comes from the Greek *deon*, "duty."

**Torah use:** Hebrew verbs carry *mood* in their form, and the moods map directly onto deontic operators:

| Hebrew form | Example | Our operator | Reading |
|---|---|---|---|
| jussive | יְהִי / yehi / "let there be" | LET(p) | directive: let it be that p |
| imperative | דַּבֵּר / dabber / "speak!" | CMD! | direct order to the addressee |
| imperfect (in command speech) | יִשְׁרְצוּ / yishretzu / "let them swarm" | LET?(p) | probably a directive — labeled hypothesis |
| weqatal | וְהָיוּ / ve-hayu / "and they shall be" | THEN(p) | obligation sequenced after another |

**The passive discovery:** day 3's commands are in the *niphal* (passive) stem — יִקָּווּ / yiqqavu / "let the waters **be gathered**." No agent is named. Deontic logic has a classic distinction for exactly this: an obligation that someone *do* something versus an obligation that something *be the case*. The Hebrew stem system encodes that distinction natively.

**Limit:** deontic logic states what is demanded. It does not say whether the demand was fulfilled — that's the next method's job.

---

## 4. Hoare triples — specification and verification

**One idea:** wrap any operation in two conditions: `{P} operation {Q}` — "if P holds before, and you do the operation, then Q holds after." P is the precondition, Q the postcondition. It reads as three beats: *before / do / after*.

**Where it comes from:** C. A. R. Hoare, 1969. Yes, it was invented to reason about programs — but the method itself is pure paper annotation: you never run anything; you *argue* that the triple holds.

**Torah use:** the creation days are shaped exactly like verified transactions:

- **{P}** — Genesis 1:2 is a pure state description (formless, dark, waters). Zero events happen in it. It is the precondition block.
- **operation** — the fiat: LET(exists(light)).
- **{Q}** — וַיְהִי־אוֹר / va-yehi or / "and there was light": the postcondition asserted.
- **verify** — וַיַּרְא… כִּי־טוֹב / va-yar… ki-tov / "saw that it was good": the acceptance test.
- **commit** — evening, morning, day count: the transaction closes.

Once you see the shape, its *exceptions* become findings: day 2 commits **without** the "good" test; day 3 runs the test **twice**. A form, plus deviations from the form — that's where interpretation gets traction.

**Limit:** the test predicate טוֹב / tov / "good" is an oracle — the text never defines it. Hoare logic can mark *where* the test runs, never *what* goodness is.

---

## 5. Event semantics — events as things with role slots

**One idea:** treat an event as an object with labeled slots: who did it (**Agent**), what it was done to (**Theme**), where (**Location**). "God created the heavens" becomes: there is an event e; e is a creating; Agent of e is God; Theme of e is the heavens.

**Where it comes from:** Donald Davidson, 1967; extended by the "neo-Davidsonians." Linguists call the practical craft *semantic role labeling*.

**Torah use — the gift of את / et:** Hebrew has a little word whose entire job is to point at the Theme — the thing the verb lands on. It has no translation. When Genesis 1:1 says אֵת הַשָּׁמַיִם וְאֵת הָאָרֶץ / et ha-shamayim ve-et ha-aretz, the doubled et hands you the complete Theme inventory: two objects, explicitly marked. (This is TIR-014 in the project's rule set — the particle-as-set-operator work.) Most languages make you guess the object; Hebrew flags it.

**Limit:** role slots describe single events. Relations *between* events (order, purpose, consequence) need the temporal and deontic layers.

---

## 6. Temporal logic — the logic of before and after

**One idea:** add time operators to logic — "p holds *now*," "p will hold *next*," "p holds *until* q." Statements get truth values *at times*, and sequence itself becomes something you can reason about.

**Where it comes from:** Arthur Prior, 1950s — a logician-priest, incidentally, motivated partly by ancient questions about foreknowledge.

**Torah use:** Genesis 1 is scaffolded by explicit clock structure: וַיְהִי־עֶרֶב וַיְהִי־בֹקֶר / va-yehi erev va-yehi voqer / "and there was evening, and there was morning" — a repeating cycle that closes each unit, followed by a day label. We write the close as COMMIT(day n). One curiosity the layer surfaces: day 1's label is the *cardinal* אֶחָד / echad / "one," while later days use *ordinals* ("second," "third") — a marked difference sitting in plain sight.

**Limit:** temporal logic orders states; it doesn't cause them. It's the ledger, not the engine.

---

## 7. Invariants — conditions that must keep holding

**One idea:** an *invariant* is a condition that is supposed to stay true across time, as opposed to an event that happens once. "The wall was painted" is an event. "The wall holds up the roof" is an invariant.

**Where it comes from:** engineering and mathematics generally; the word is old, the idea older.

**Torah use:** Hebrew participles are the invariant-marker. מַבְדִּיל / mavdil / "dividing" in Genesis 1:6 does not narrate one act of division — it assigns the firmament a *standing job*: keep the upper and lower waters apart, indefinitely. Day 1 demanded a thing; day 2 demanded a thing **with a job**. The participle form alone carries that difference. Likewise מְרַחֶפֶת / merachefet / "hovering" in 1:2 — an ongoing condition, not an event.

**Limit:** the text doesn't say what happens if an invariant fails. (Later texts arguably do — the flood reads like invariant failure — but that is a labeled hypothesis, not this tutorial's claim.)

---

## 8. Casuistic law — the original IF/THEN

**One idea:** law can be written two ways. **Casuistic**: "IF a person does X, THEN Y follows" — case-based, conditional. **Apodictic**: "You shall not X" — absolute, unconditional. This two-form analysis of biblical law is standard scholarship (Albrecht Alt, 1930s), and the casuistic form itself is as old as written law — Hammurabi's code is built from it.

**Torah use:** the trigger word is כִּי / ki / "when/if." Leviticus 1:2 — אָדָם כִּי־יַקְרִיב / adam ki-yaqriv / "a person, WHEN he brings near…" — is a textbook casuistic opening: it sets up a *case frame* that the following chapters fill with sub-cases (from the herd… from the flock… from the birds…). The project's YAML decision tables are this ancient form, resurrected. Apodictic form maps to the bare imperative/prohibition — deontic logic without a trigger condition.

**Why this matters most for Leviticus:** narrative (Genesis) mostly wants events + specs; law (Leviticus) mostly wants case frames. Recognizing which form you're in tells you which methods to reach for.

---

## 9. The registry — naming as installation

**One idea:** a name, once given, is a stable pointer to a thing (philosophers say "rigid designator" — Saul Kripke, 1970s). Giving the name is a speech act; *having* the name is a registry entry: `name(light) := "yom"`.

**Torah use:** Genesis 1 performs seven namings in its first ten verses' span (Day, Night, Heavens, Earth, Seas…). Tracking them as registry writes exposes two **label collisions**: שָׁמַיִם / shamayim / "heavens" is installed in verse 1 and installed *again* onto the firmament in verse 8; אֶרֶץ / eretz / "earth" likewise in verses 1 and 10. Paper logic can flag the collision precisely; resolving it is interpretation (and the Oral tradition discusses exactly these) — kept separate, per project rules.

---

## 10. The dry run — hand-executing the logic

**One idea:** once verses are written as logic, you can *walk through them by hand*, keeping a little state on paper — no computer, just bookkeeping. This is how programs were traced on paper, and how a proof is checked line by line.

**The machine we use** (all registers are just columns on a page):

| Register | Holds |
|---|---|
| TIME | current point on the timeline |
| WORLD | what exists + current facts and invariants |
| REGISTRY | name → thing bindings |
| SPECS | directives issued but not yet satisfied |
| TESTS | acceptance-test log |
| LEDGER | committed day-units |

**What running Gen 1:1–10 revealed** (see the experiment doc for the full trace):
- Verse 2 executes **zero events** — pure precondition.
- Three different **spec-fulfillment latencies**: instant (v3), cross-verse with an explicit build step (v6→v7), same-verse with no agent (v9).
- WORLD splits into **created** entities and **presupposed** ones — darkness, deep, waters are used but never installed.
- Day 2's missing test and the two registry collisions surface as machine warnings, not opinions.

---

## 11. How the layers stack

For any verse, ask in order:

1. **Is anyone speaking?** → speech-act wrapper (DECLARE).
2. **What mood are the verbs?** → deontic layer (LET / CMD! / LET? / THEN) or narrative events.
3. **What are the slots?** → event semantics (Agent, Theme via et, Location).
4. **Any participles?** → invariants (standing jobs).
5. **Any asher-clauses?** → defined sets.
6. **Any ki-triggers?** → casuistic case frame (especially in law).
7. **Any namings?** → registry writes.
8. **Where does the clock tick?** → temporal commits.
9. **Then:** run the dry run and compare the unit to the standard pattern. **The deviations are the findings.**

## 12. Epistemics (always)

These methods are **lenses, not claims**. The text is not "really" Hoare logic; Hoare logic is a disciplined way to write down what the Hebrew forms are visibly doing, so that patterns and exceptions become checkable. Hebrew remains the only derivation source; every mapping stays labeled (tested / hypothesis / open); nothing here is binding religious law.

**Glossary of our operator names:** DECLARE (speech act) · LET / LET? / CMD! / THEN (deontic, from verb mood) · {P} op {Q} (Hoare triple) · Agent / Theme / Location (event roles) · INVARIANT (participle) · RESULT ✓ (va-yehi khen postcondition check) · PASS(tov, x) (acceptance oracle) · name(x) := "N" (registry write) · COMMIT(day n) (temporal close).
