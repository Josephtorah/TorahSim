# REPORT — O3 THE GATE ITEMS: the value/effect homograph and the last-binding resolution (2026-09-07)

The open-items campaign's third sitting (the plan: the state doc's compaction point #90; the owner: "O3 go"). Two gate
edits, each its own OPEN note in COMPILE_DEBT.md since W1 and W3. The rhythm of a gate edit: the fire-probes written
FIRST to fail against the unchanged gate (scratchpad o3_gate_fires.py — ten probes), the edit, the probes fired, the
standing probes rerun (d9ii_gate_fires.py 5, lr1_gate_fires.py 12), the census remeasured and every disposition read,
the sweep.

## The declaration (written before the code)

(a) THE VALUE/EFFECT HOMOGRAPH. daemon_census.parse_functions read EVERY registered-effect-named string in a function's
source as an effect the function writes. A string that spells an effect is not a write: the tier name 'anointed' (the
chatat engine's `who == 'anointed'`), a cell VALUE ('anointed' — the wafers anointed with oil), a verdict VALUE ('exempt'
returned by a verdict function), a ledger READ (`e['effect'] == 'buried'` in a scene's count helper), a tape's close
note. Eight functions stood on the worklist as NONE for a spelling. THE FIX: a function's written effects are read
from the forms that WRITE — the fx argument of its cell(...) calls (any expression: a list, a conditional, a sum, a
local name resolved to its assignments in the function), the effects argument of out(...), the effect of an E_(...)
call, an effect dict literal; a bare string as a cell's fourth argument is a note (the yoma shape), not fx. A runner with
no such form and a module-level attachment (vayikra5's effect_of; the table-shaped runners) is the `<module>` shape the
gate already knows. EXPECTED: the census drops — the eight NONE workarounds retire (chatat identity and sprinklings,
minchah oil_ops, the four scene-count helpers, sequence.tape); lev24.main and negaim.main (scenes reading the ledger)
and shemini.touch_effect (a helper RETURNING effect names the daemon writes) leave the census, their WRAPPED entries
removed as overstated; vayikra5's three verdict functions and yoma's main (its cell's fourth argument a note) become
their runners' `<module>` entries; twenty-five functions lose homograph strings from their effect sets — and any WRAPPED
verification that rested on a homograph alone will FAIL at the gate and be re-pointed honestly. The counts are read
from the gate's own run, never predicted as literals.

(b) THE LAST-BINDING RESOLUTION. compile_guards.check_honest_calls resolved a cells NAME to its LAST assignment in the
file, so `cells = [...]; grade(f, o, cells); cells = [...]; grade(f, o, cells)` checked the last list twice and the
earlier lists never (mishpatim's tripwire 21 was F5's rows counted again; lev24's 19 the one-law's rows counted
twice; the OPEN note since W1). THE FIX: the binding in effect at the call's line — the nearest assignment to that name
BEFORE the call in source order. EXPECTED: the five tripwires remeasured (mishpatim 21, mishpatim_2 10, lev24 19,
negaim 19, yoma 23) — each printed by the guard, then typed; the counts that change are the lists the old guard never
read, and any non-literal expectation they hide will refuse the run.

## As run

THE PROBES FIRST: eleven probes (scratchpad o3_gate_fires.py) — against the unchanged gates 4 of 11 fired (the four
regression guards: a conditional fx, a local-name fx, out(), an effect dict — shapes the old parse also read); the seven
target behaviors were SILENT, as a probe of an unfixed gate must be. After the two edits 11 of 11 fire; the standing
probes 5/5 (d9ii) and 12/12 (lr1) unchanged.

(a) THE HOMOGRAPH. `daemon_census.written_effects(fn)` reads the writing forms only. The gate's census: 256 → 244 compiled
functions in 33 runners (was 34 — the sequence runner leaves: its tape writes nothing); 244 WRAPPED verified / 0 OWED / 0
NONE (was 248 / 0 / 8). The gate's first run after the edit failed EIGHTEEN ways, every one of the expected kinds and
read before repaired: fourteen dispositions overstated — the eight NONE workarounds (chatat identity and sprinklings,
minchah oil_ops, the four scene-count helpers of erection, incense_shekel and yovel, sequence.tape) and six WRAPPED
entries that had rested on homograph strings (lev24.main and negaim.main — scenes reading the ledger; shemini.touch_effect
— a helper RETURNING the names the daemon writes; vayikra5's graded_offering, sacrilege, deposit_restitution — 'exempt' a
verdict VALUE; yoma.main — its cell's fourth argument a note); three runners re-shaped as `<module>` (vayikra5 — the
effects attached by effect_of; shemini; negaim) and given module-level wraps; the sequence block removed. Twenty-five
functions lost homograph strings from their effect sets and NOT ONE WRAPPED verification broke: every wrap had a genuine
shared effect beside the spelling. law_deposit_oath's wrap of vayikra5's deposit_restitution folds into the module entry
(the library daemon's adds_fifth and atoned_forgiven are law_vayikra5's by call).

(b) THE BINDING. `compile_guards.check_honest_calls` resolves a cells NAME to the nearest assignment before the call.
The five tripwires remeasured by the guard itself: mishpatim_2 10 (unchanged), yoma 23 (unchanged — its shape carries no
name), lev24 19 → 24, negaim 19 → 27 (TEN's 10 + the grade calls' 17), and mishpatim REFUSED OUTRIGHT at line 106: the
four-damages class map's cells were a COMPREHENSION over the computed openers plus an append — a list the old guard never
read because the file's last binding was a literal. The honest repair is in the runner, not the guard: the four rows
typed as literals (the openers' order asserted beside them), and the guard then counts 24 (was 21). Every changed count is
the lists the old guard never read; no non-literal expectation hid in them but the one the guard named.

### Findings

1. **A CENSUS THAT COUNTS SPELLINGS OVERSTATES BY TWELVE.** Eight NONE entries existed only to excuse the parser; six
   WRAPPED entries were verified on a value that spelled an effect. The honest count is 244, every one a writer.
2. **THE GUARD THAT READS THE LAST BINDING PROVES THE LAST LIST.** Three of five tripwires moved; one runner's rows had
   never been read at all. A guard's count that never changes across work that should change it is the defect report
   THE_STEPS names — here the same literal held through four wrap sittings.
3. **THE FIRE WAS THE RUNNER'S, NOT THE GATE'S.** The comprehension at mishpatim's four-damages map graded a constant
   against itself; typing the rows is the answer-sheet rule applied to rows that had stood unread since the Mishpatim
   compile.
4. **THE MODULE SHAPE IS THE TRUTHFUL ONE FOR THREE RUNNERS.** vayikra5, shemini and negaim attach their effects at the
   module level (a verdict-to-effect map, a touch table, the daemon's own tables); the per-function wraps were the
   homograph's fiction.

## The sweep at the sitting's close

34 of 34 runners green, 3,633 graded cells (unchanged — the four typed rows replace four generated ones), both gates
satisfied first (scratchpad sweep_o3.txt, SWEEP-EXIT 0): DEPENDENCY GATE 129 live edges; DAEMON GATE 38 daemons watching
267 kinds, 776 submit records, 244 WRAPPED / 0 OWED / 0 NONE of 244 (was 248 / 0 / 8 of 256), unfired 0, unconsumed 0,
open aliases 0; the probes 11/11 (o3) + 5/5 (d9ii) + 12/12 (lr1); the five guarded runners green on their remeasured
tripwires (mishpatim 24, mishpatim_2 10, lev24 24, negaim 27, yoma 23). No frozen unit touched; the corpus regression
green, hash 8b8fff1fa28953af unmoved. Next: O4 THE EDGE FILING.
