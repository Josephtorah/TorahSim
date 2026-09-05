# CHRONICLE — the simulation's observation deck (design)

Written 2026-09-05 from the owner's two-thread design conversation
(the UI thread and the walk thread, relayed between sessions the
same day). This file describes a DESIGN; nothing in it is built,
and nothing outside this file was changed to make it. Like the
rest of this folder it describes — it is not the code.

## What it is

A read-only PROJECTION of the world engine's two truths: the TAPE
(events in verse order) and the LEDGER (statuses, debts, timers
written by effects). The Chronicle renders them; it never touches
the physics. The trade's name for our shape is EVENT SOURCING — an
append-only event log is the truth, every view is a projection —
and the monitoring problem is universal. Precedents the design
leans on: the five-pane simulation control room (flight sims,
NetLogo, factory digital twins all converge on it), trace viewers,
and Dwarf Fortress's Legends mode (the canonical browsable
per-entity world history).

A control room answers four questions at a glance, and the screen
works only while all four stay visible:
1. What is the current state?
2. How did we get here?
3. What can I change?
4. Is anything important happening right now?

## The owner's founding correction: not ledger-only

"We should not look at this as ledger only. We don't know what
will happen when this is all compiled. We may have recursive
inputs we can't predict." (Owner, 2026-09-05.)

The input tape is known — the text is the event source, so the run
is a REPLAY and every tick is ink. But the COMPUTED side is
emergent: an effect changes state, the changed state satisfies
another law's condition, that daemon fires unasked; timers fire
with no local text event; and the program itself grows at runtime
(the Leviticus 24 code-request pattern — the first call). The
cascade is the show. The first star witness arrived the same day
the correction was spoken: the land_repays_sabbaths TIMER
(discovered compiling Leviticus 26) whose discharge the text
records books later at 2 Chronicles 36:21 — a payoff with no local
trigger, exactly the class the design must make visible.

Consequences, each load-bearing:
- TWO EVENT CLASSES, visually distinct everywhere: EXOGENOUS
  (from the text — the input tape) vs ENDOGENOUS (computed —
  effects, cascades, timer firings). The endogenous stream is the
  simulation's actual output; the UI must never blur the two.
- THE VIEWPORT IS A CAUSAL TRACE, not just a ledger board: click
  any fired effect and see its whole chain — text event → daemon
  → effect → daemon → effect. "Why did this fire" is the core
  question of an unpredictable system.
- THE CLOCK HAS TWO GRAINS: step one VERSE, or micro-step one
  EFFECT inside the verse's cascade. One verse may expand into a
  long computed chain; the operator must be able to walk it.

## The five panes, mapped to what exists

| Pane      | Ours                                                    |
|-----------|---------------------------------------------------------|
| Clock     | Verse-order replay; play / pause / step-verse /         |
|           | micro-step-effect; t = a verse address plus the era     |
| Viewport  | The ledger board first (entity cards whose statuses,    |
|           | debts, timers visibly change as the tape plays), the    |
|           | causal-trace view behind every fired effect             |
| Inspector | One selected entity → its whole life as ledger rows     |
| Telemetry | FIVE numbers, no more: t · entities on stage · open     |
|           | demands · active timers · endogenous-event rate (or     |
|           | max cascade depth this tick — the "how alive is the     |
|           | machine" gauge)                                         |
| Event log | The tape lines themselves, in the two event classes     |

The model (world_engine.py + the compiled law daemons) stays
hidden beneath all five. Controls — posing scenarios through
pose_case — are a later pane, after the picture works.

## The registry page: the physics vocabulary is monitored too

The effects registry (World/step9/effect_vocabulary.yaml — 71
effects at this writing) is the allow-list, and effects_layer.py
refuses unregistered effects at emission; but an allow-list is not
a monitor. The Chronicle gives the vocabulary its own page: one
row per effect — birth date, its three witness layers, the
functions that emit it, and its FIRED-COUNT from the tape
(effects_layer.summarize() already tallies fired ledger ops per
run, so the column has a source today). Registry changes become
events in their own lane beside world events: the physics
vocabulary keeps its own append-only history. The tripwire this
buys: an effect registered but never fired across work that
should fire it is a defect report, not a constant — the standing
instrument rule applied to the physics itself.

## Design rules carried over from the method

- READ-ONLY PROJECTION: the UI reads state and sends nothing but
  view commands; it never knows the domain rules and never
  instruments the engine.
- EVERY NUMBER EXPANDS TO ITS ROWS: a summary figure with no
  click-through is a recital — the zero-report law applied to UI.
- ONE SELECTED OBJECT; everything else is context.
- COLOR MEANS ONE THING (event class / effect family), never a
  rainbow.
- STEP BEFORE REAL-TIME: if a single tick cannot be stepped and
  explained, the visualization is lying. Ours can — every tick
  is ink.
- EMPTY STATE MATTERS: before the first run the screen says
  "press play," it does not look broken.

## The engine watch this design surfaced (not built)

Recursion can loop — law A's effect re-arming law B re-arming A.
Before the whole Bible compiles, the world engine needs
CASCADE-DEPTH LIMITS and CYCLE DETECTION, and the Chronicle needs
an anomaly lane ("cycle detected," "cascade depth N," "runaway
timer"). You monitor precisely because you cannot predict.
Recorded as a watch for the engine; nothing changed in it.

## Build shape

Static export first: fold once, render one web page from the real
tape (we skip the "fake it" phase every first-time builder needs —
the real data already exists). Live view later. One page, five
panes, five numbers.

## Status

Design only, owner-directed 2026-09-05 ("ok do it" — this file).
Idea-log history: THE_WORLD.md, the two 2026-09-05 Chronicle
entries. Nothing is built; the build waits on the owner's word.
