# REPORT — W1 THE EXODUS LAW (D9-iii THE WRAPS, the first wrap sitting, 2026-09-07)

The owner's word: "Reread first then go" (the first sitting after compaction #74; the mandatory rereads
done first). The campaign's ruled order (COMPILE_DEBT.md D9): the seeding sitting, the daemon-edge gate,
then THE WRAPS by engine family — W1 first, the Exodus law: mishpatim, mishpatim_2, guardians (already
law_guardians), ordinances, decalogue, lev24.

## What a wrap is (the rhythm, run for the first time)

1. THE TYPES FIRST. Every case head the six runners compiled — the law's own כִּי / אִם ("when" / "if")
   clause, or the participial head ("he who strikes", "a sorceress") — registered in
   event_vocabulary.yaml as a `case`-form type BEFORE any daemon was written: 38 types, each with its
   consonantal witness found CONTIGUOUS in its verse of the Tanakh DB and its pointed form extracted
   from the verse's own words by script (scratchpad w1_registry_gen.py), never typed. Two existing types
   amended from the ink: ox_gores gained the slave clause (21:32) and bailment_claim the borrower's
   (22:13). The registry lint: 122 types, 191 witness runs verified, 0 flags; the case form 6 → 44.
2. THE DECLARATION SECOND. The five daemons declared in daemon_dispositions.yaml with their watches
   (kind → effects), and the seventeen functions flipped OWED → WRAPPED, before a line of daemon code
   existed. The gate then FAILED 23 ways — five daemons undefined, seventeen wraps pointing at nothing,
   one library branch missing — exactly the contract: the declaration is the spec the code must meet.
3. THE CODE THIRD. A `law_<runner>(event, world)` in each runner, thin over the compiled logic (the
   Mishpatim daemon CALLS cold_run_lev24.talion() live on the tape; the ordinances daemon carries the
   decalogue's altar rule at its call site and the offering, sanctions, jubilee, and Passover engines'
   values), every branch naming its effects literally so the gate's parse equals the declaration.
4. THE SCENE FOURTH. Each runner's `scene()` replays the RECORDED cases — the answer sheet's rows as the
   tape, never invented history — and returns a tuple of ledger counts, timer sets and fires, and the
   absolute clock. THE PRINT-THEN-TYPE RULE held: every scene's value was printed by the engine before
   its literal was typed, and all three probes (ordinances, decalogue, lev24) matched the values predicted
   from the Mishnah rows beforehand. The literal sits in the runner's own test table under the
   honest-pairing guard; the tripwires measured and set (21, 10, 128, 13, 19).
5. THE GATE AND THE SWEEP. daemon_census.py satisfied; run_cold_all.py 33/33 through both gates.

## The decision at the sitting: the skeleton's daemons are the LIBRARY

The #74 tail left it open whether law_slave_term / law_goring_ox / law_guardians go home to their runners
or stay in world_engine.py. They STAY, as the library: the Mishpatim scene registers
`[WE.law_slave_term, WE.law_goring_ox, law_mishpatim]` on one world, and the runner's own daemon takes
the case heads the library does not. No duplicated verdict logic, no circular import (world_engine.py
importing a runner would run the runner's grading at import). The gate verifies either shape; this one
was chosen for the code's sake. And the census found the library short one branch: the SLAVE GORED
(Exod 21:32 — thirty shekels to his master, the ox stoned) was a compiled cell of cold_run_mishpatim.py
but no branch of law_goring_ox; added at the library, the declaration amended, the skeleton still 6/6.

## The census (coverage first)

| | before W1 | after W1 |
|---|---|---|
| event types (case form) | 84 (6) | 122 (44) |
| witness runs verified | 127 | 191 |
| daemons | 12 watching 82 kinds | 17 watching 120 kinds |
| submit records on the tapes | 100 firing 82 | 162 firing 120 |
| WRAPPED / OWED / NONE of 251 | 49 / 202 / 0 | 66 / 185 / 0 |
| W1 functions on the worklist | 17 | 0 |
| the sweep | 33/33, 3585 cells | 33/33, 3599 cells (five scene cells; mishpatim_2's score line made visible) |
| unfired / unconsumed / open aliases | 1 / 1 / 9 | 1 / 1 / 9 (none of W1's) |

## The tapes (the recorded cases each daemon fired on)

- **law_mishpatim** (+ the library's two): Kiddushin 1:2 — acquired by years, then REDEEMED BY DEDUCTION
  (the buy-out CANCELS the year-7 timer; year 7 passes with no fire); Bava Kamma 2:4 — three gorings
  half, half, half + FOREWARNED, then 1:4 full; 4:5 — the slave gored: stoned + thirty; 8:1 — the five
  indemnities (three pays, the idleness sum, the tariff CALLED from Lev 24 → substitution); 1:1 — the
  pit, the tooth from the best of the land, the fire; 7:1 — five for the ox, four for the sheep, double
  for the theft found in hand. Coverage: law_slave_term 1 of 14, law_goring_ox 5, law_mishpatim 8.
- **law_mishpatim_2**: Ketubot 3:4 — the seducer three, the rapist four; Kiddushin 24a — the eye and the
  tooth free the slave, the regenerating limb reaches no exemplar (no write); Bava Kamma 5:4 — the
  difference before/after by the judges, the ox exempt. 6 of 7 fired (the hair the honest silence).
- **law_ordinances**: 21 kinds, 30 of 30 fired — Middot 3:4 (hewn disqualified, whole accepted), the two
  offerings by their engines, Sanhedrin 7:4/7:11 (the doer stoned, the deceiver of the eyes exempt),
  7:4 the beast, 7:6 the idolater's row, Mekhilta 22:22-23 (the widow's cry on Heaven's docket and the
  oppressor's sword), Bava Metzia 4:10 (words: exempt), 5:1 (the bite), 9:13 (the pledge's SUNSET TIMER
  set day 3, FIRED day 4), Shevuot 4:13 (by the Name lashed; the euphemism exempt), Terumot 3:6 (the
  order), Bekhorot 8:7-8 (the five sela's THIRTY-DAY TIMER, fired at 35), Exod 22:29 + Lev 22:27 (the
  EIGHTH-DAY TIMER, fired at 12), 13:13 (the donkey's fork by call), Chullin 3:1 + Makkot 3:2 (the torn
  to the dog, its eater lashed), Sanhedrin 7b (one party heard), Sanhedrin 4:1 — THE COURT SPLIT THREE
  WAYS (12-11 capital ACQUITTED, 13-10 CONVICTED, 12-11 money CONVICTED: the asymmetry as code),
  Bava Metzia 2:9 (return), 2:10 (unload WITH HIM; the sitting owner's exemption), Sanhedrin 33b (never
  retried), Peah 8:9 + Ketubot 105a (the bribe and Heaven's entry), Avodah Zarah 3:1 (the pillars),
  23:29-30 (the LAND's desolation flag held OFF), 23:25 (bread and water blessed). Four timers set, four
  fired; the clock at 40.
- **law_decalogue**: Shevuot 3:10-11 and 20b (the vain and the broken oath lashed), Pesachim 106a (the
  day sanctified), 20:10 (the household barred; Shabbat 120b causing NOT written; 153b the laden beast
  barred), Sanhedrin 11:1 (the kidnapper who SOLD strangled; the one who did not sell — no write).
  6 of 8 fired, the two silences the law's own.
- **law_lev24**: the chapter's OWN CASE (24:11 → custody → the sentence → stoned at 24:23) with Sanhedrin
  7:5's Name gate; 24:15 without the Name bears sin; Niddah 44b the day-old; 24:18 pays; Bava Kamma 8:1
  the tariff through the export talion(). 5 of 5.

## Findings (none seat: no unit touched; the sitting's findings are the gate's and the debt's)

1. **THE LIBRARY WAS SHORT A BRANCH** — the slave gored (21:32), compiled as a cell since the
   re-compilation pass, watched by no daemon until the census put the ink's case tokens beside the code.
   Fixed at the library; the declaration amended; the yaml's own contract caught the mismatch first.
2. **THE HONEST-CALLS GUARD RESOLVES A NAME TO ITS LAST BINDING** — compile_guards.check_honest_calls
   maps `cells` to the LAST `cells = [...]` in the file, so every grade(fn, oracle, cells) call is checked
   against that one list: mishpatim's tripwire "20" was F5's four rows counted five times, lev24's "18"
   the one-law's three rows counted six times. The guard still refuses a non-literal in the last-bound
   list, but the earlier lists are unchecked. Not touched this sitting (a gate edit is its own sitting
   under the mechanical-gates discipline); the wraps' rows use a distinct name (`wrap_cells`) so the
   tripwire counts them once. OPEN: resolve the binding in effect at the call's line.
3. **THE EXODUS LAW'S UNCOMPILED CASE HEADS** — the census of Exod 21-22's case tokens against the six
   runners' functions leaves these heads with exam-era rules but NO cold function: 21:7, 21:9-11 (the
   maidservant beyond 21:8's redemption), 21:13-15, 21:17 (the refuge, the deliberate killer, striking
   and cursing parents), 21:20-21 (the slave struck dead), 22:1-2 (the burglar), 22:16 (the father's
   refusal). Declared as compile debt (COMPILE_DEBT.md), not wrap debt.
4. **A SCORE LINE THE SWEEP NEVER READ** — cold_run_mishpatim_2.py printed "PASS 2: 9/9" without the
   word the sweep's regex needs, so it had been counted rc-only since the sweep opened; one word added,
   the sweep's cell count is now honest by ten.

## Lessons banked

- Declaring first is not ceremony: the gate failing 23 ways before the code existed is what made the
  code's shape unarguable, and it caught the library's missing branch.
- Print, predict, then type: three of three probes matched the prediction; the fourth and fifth (the
  two Mishpatim scenes) were typed from the answer sheet's rows and matched first run.
- A tuple of counts is a literal the guard accepts and a reader can audit line by line against the
  tape — the scene's checkpoint, not a hash.
- zsh expands a bare `===`/`====` as a glob (the third time); the Bash `echo` separator must be quoted
  or avoided.
