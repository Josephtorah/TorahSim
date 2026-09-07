# REPORT — THE DAEMON-EDGE GATE (D9-ii, THE DAEMON CAMPAIGN's first deliverable, 2026-09-07)

The owner's word: "Go d9 2". The campaign's ruled order (COMPILE_DEBT.md D9): the seeding sitting
(D9-i, the event-type registry — done the same day), then THE DAEMON-EDGE GATE as the first
deliverable, then the wraps by engine family, then the deliverable rule amended.

## What it is

The dependency gate (dependency_census.py, 2026-09-06) made the ink's cross-references between
compiled spans a declared, verified graph: every edge dispositioned, every CALL live, the OWED ones
a generated worklist. This gate does the same for the simulator's other graph — what a compiled
function FIRES ON and what it WRITES:

- **World/step9/daemon_census.py** — run by run_cold_all.py after the dependency gate, before any
  cell is graded. It parses every runner and the engine BY SCRIPT (the seeding's harvester moved
  into the repo): every daemon (`def law_*(event, world)`) with the kinds it watches and the effects
  each branch writes; every `.submit(` on a scene tape (explicit dicts, tuple tapes, loop sources);
  every compiled function that writes the world (a top-level def naming a registered effect, or the
  module itself for a table-shaped runner).
- **World/step9/daemon_dispositions.yaml** — the declarations the gate verifies: each daemon's
  file, the runner it wraps, and its WATCHES `{kind: [effects]}`, which must EQUAL the parse; each
  compiled function's disposition — WRAPPED (by a declared daemon sharing at least one effect: the
  wrap's live check, as CALL's is the live import), OWED (why names a wrap worklist line of
  COMPILE_DEBT.md), or NONE (reserved); the watched-never-fired and fired-never-watched kinds with
  their whys.
- **World/step9/DAEMON_INDEX.md** — generated each run (documentation, never runtime).
- **world_engine.py** — `World.submit` now refuses an unregistered event kind (events_layer.validate,
  as effects_layer refuses an unregistered effect), keeps every daemon's WATCH COVERAGE (events
  seen, events fired on, the kinds), prints it (`print_coverage`), and carries THE FENCE'S DEPTH
  BOUND: a daemon consumes events and writes the ledger — it never emits one — so no event is ever
  submitted while another is being consumed; the bound is 1, and a re-entry is reported loudly with
  the daemon's name, never truncated silently.
- **COMPILE_DEBT.md** — THE WRAP WORKLIST: seven lines W1-W7 by engine family, the addresses the
  OWED dispositions name.

## The census (coverage first)

| the gate's coverage line | |
|---|---|
| modules scanned | 34 (33 runners + the engine) |
| daemons | 12, watching 82 kinds |
| submit records on the tapes | 100, firing 82 kinds |
| compiled functions writing effects | 251 in 33 runners |
| WRAPPED (verified by a shared effect) | 49 |
| OWED (on the worklist) | 202 |
| NONE | 0 (reserved for the wraps) |
| unfired kinds (watched, no tape) | 1 — jubilee_proclaimed |
| unconsumed kinds (tape, no daemon) | 1 — overflow_reported |
| open aliases (the registry's aliases_in_code) | 9 entries, five pairs |
| registries | 84 event types, 242 effects |

The 251 is at the FUNCTION grain: every top-level def that names a registered effect, plus the
module for the four table-shaped runners (guardians, mishpatim, mishpatim_2, offerings). The
architecture thread's earlier "54 compiled functions not yet wrapped" was a coarser count; the
gate's grain is the function that writes the world, and its number is the measurement.

## What is wrapped, and by which tape

- **Genesis, whole**: family (six functions → law_family), pre_sinai (six → law_pre_sinai).
- **The sanctuary's spec/run pairs**: the making's functions by the construction daemon
  (law_sanctuary_build: offering, ark, curtains, boards, veil, court, books); the SPEC functions
  whose act is the ERECTION's by the erection daemon across files (table, menorah, lamp; the laver
  and the tamid of Exod 30) — the spec wrapped by the run that executes it; the vestments' making
  by law_vestments (breastplate, robe, tunics, completion) and the vestments' USES by the
  investiture daemon (office, ephod, plate, investiture — worn at Lev 8:7-9); the ordination's
  functions by law_investiture (persons, bull, rams, meal, seven_days); the erection's own by
  law_erection (command, execution, initiations, cloud); the eighth day's by law_eighth_day (day,
  ram, peace, fire, eras).
- **The skeleton's four**: tzav.installation → law_installation; vayikra5.deposit_restitution →
  law_deposit_oath (verified at the module level — the older shape attaches effects by a
  module-level mapping); guardians (the module) → law_guardians; mishpatim's F1 and F3 are wrapped
  in the skeleton's law_slave_term and law_goring_ox, but the module holds the injuries, the
  multiples, the pit, the grazing, the fire and the seducer unwrapped — OWED to W1 with the note.

## The worklist (`daemon_census.py --debt`)

202 functions in 29 runners, by family: W1 THE EXODUS LAW (ordinances 9, decalogue 4, lev24 2,
mishpatim, mishpatim_2); W2 THE CALENDAR (calendar 7, moadim 8, pesach 5, the Sabbath's law
layer, the covenant laws' second seat); W3 THE OFFERING ENGINE (chatat 36, minchah 10, tzav 8,
offerings, vayikra5 2, shemini 1, shemini_day 3); W4 THE PURITY CLOCKS (clocks 7, negaim 1,
metzora 6, yoma 4); W5 HOLINESS, SANCTIONS, THE LAND (sanctions 22, yovel 14, holiness 8,
holiness_b 6, priesthood 5, tochacha 8, temurah 7); W6 THE SANCTUARY'S REMAINDER (sanctuary_build
1, incense_shekel 5, erection 2); W7 THE SINAI NARRATIVE LAWS (erection 6). Plus the unfired
jubilee_proclaimed (W5 fires it from Lev 25:10), the unconsumed overflow_reported, and the five
alias pairs the wraps must close.

## The gate fires honestly (five probes, scratchpad d9ii_gate_fires.py)

1. A daemon's declared watches missing a kind → FAIL ("declared watches ... != parsed").
2. A function declared WRAPPED by a daemon sharing no effect → FAIL. This probe was SILENT on the
   first pass: the module-level fallback (meant for the older shape, where a module-level mapping
   attaches the effects) let chatat.domain pass as wrapped by law_family because the chatat module
   somewhere names 'buried'. The rule was sharpened: a function that carries its own cells must
   share an effect at the FUNCTION level; the module level stands in only for a function with no
   cell call or for the `<module>` candidate. Then it fired.
3. An unfired kind removed from `unfired:` → FAIL ("submitted on NO tape").
4. `World.submit` with an unregistered kind → SystemExit from the registry.
5. A daemon that emits an event (re-entry) → SystemExit naming THE FENCE and the daemon.

The skeleton's six scenes stand at 6/6 with the new submit, and print their watch coverage:
law_slave_term fired 3 of 10 events on two kinds, law_goring_ox 4 of 10, law_guardians 2,
law_deposit_oath 1, law_installation 3 of 4 — the first time a daemon has printed what it saw.

## What the wraps do next (D9-iii)

Each wrap sitting, by the rhythm: the daemon DECLARED FIRST in daemon_dispositions.yaml (its
watches), the conditions read from the ink's case tokens (the `case` form of the registry —
every wrapped כִּי/אִם ("when"/"if") clause is a case-form event), the tape's kinds registered with
their witnesses, the scene replay with literal checkpoints under the honest-pairing guard, the
aliases the daemon touches unified and their registry entries cleared, the function's disposition
flipped OWED → WRAPPED, the gate green, the sweep green. The order proposed: W1 (the Exodus law,
where the skeleton's daemons go home), W2, W3, W4, W5, W6, W7.

## Lessons banked

- A gate that never fails proves nothing: the five probes are the gate's own test, and one was
  silent on the first pass — the fallback meant for one runner shape was reachable from the other.
- The engine is not a runner: the module-candidate rule (a table-shaped runner's effects at module
  level) must be scoped to cold_run_*.py, or the skeleton's test tape becomes an "unwrapped law."
- The declaration equal to the parse is the contract, not a tautology: written from the parse on
  the day the gate opens, it fails the sweep the day a daemon is edited without it — the same
  discipline as CALL against the live import.
