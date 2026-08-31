# STEP 9 PILOT — REPORT (2026-08-31, owner: "ok run it give me a full report")

Ten case rows from three Mishnah passages faced the machine. Two modules
were then compiled into the first working rules and re-examined. Everything
below is from the run itself; the raw per-case record is cases_pilot.yaml,
the sources consulted are in EXAM_LEDGER.md.

## The headline numbers

| | count |
|---|---|
| cases faced | 10 |
| BEFORE the engine — Class A (machine answers) | **0** |
| Class B (rule held as witness text, unappliable) | **7** (one partial) |
| Class C (held nowhere — the Mishnah's pure addition) | **3** |
| AFTER compiling two modules — answered correctly | **8 of 8, 0 mismatches** |

The prediction held exactly: the machine held most of the law as TEXT and
could apply none of it. Compilation — turning witness rows plus the
Mishnah's case grid into functions — is what makes it answer.

## What the Mishnah added (measured, not theorized)

1. **The case grid itself.** Gen 7:22 gives WHERE life is tested; only the
   Mishnah says what to DO on Shabbat under triple doubt (clear the
   debris), what to do finding him alive (continue), dead (stop).
2. **Three verdicts the machine held nowhere** (Class C): the dead->stop
   leg, the miscarriage-restart clause, the gehinom duration. These entered
   the engine as imports, and their provenance rows SAY so.
3. **The exam's own correction.** The spec said male+female discharges the
   duty for both houses; the compiled Shammai rule (two males) disagreed at
   first run, and the Mishnah's plain text adjudicated FOR the engine. The
   case shelf corrected the exam — first live instance of the oracle doing
   its job against our own writing.

## What the Talmud added (per case, the bridge column)

- **Yoma — the clean specimen of the anatomy theory:** the Mishnah rules
  WHAT; the gemara (85a) supplies the MECHANISM (dig to the nose) and hangs
  it on OUR verse, Gen 7:22. Verdict and derivation live on different
  shelves, exactly as the owner's oracle-anatomy ruling says.
- **Yevamot — the counter-specimen:** the verse bridge sits INSIDE the
  Mishnah row (Hillel citing Gen 5:2, R. Yochanan ben Beroka citing Gen
  1:28). The bridge column must allow both shapes.
- **The ten-years law — the richest find:** the exam anchored it at Gen
  5:2; the machine held it at **Gen 16:3** (Sarai's ten years, G32-16, four
  seats) — the module map is real, and cases route to verses the exam
  didn't predict. The machine also held RIDERS the exam didn't know (years
  outside the Land don't count; sickness and imprisonment excluded) AND the
  tradition's own epistemic grade: **"no proof, but a hint"** (Tosefta
  Yevamot 8:4). A compiled rule can carry more than the oracle row asked.
- **The woman's obligation — a dispute held by ink:** the machine holds the
  exemption side from the LEAN KETIV of Gen 1:28 — וְכִבְשֻׁהָ written
  short reads 'and subdue HER', the man commanded (G06-03, Yevamot 65b) —
  while the dissent (R. Yochanan ben Beroka) was absent and entered as an
  import. One side derived from the skeleton of the written text, the other
  from the case shelf: the dual verdict now carries both, labeled.

## What the exam decided about how the code must be written

1. **Uncertainty is first-class input** — Yoma's case cannot even be STATED
   without it (three stacked doubts, verdict unchanged).
2. **A verdict is a LIST with labeled authorities** — two disputes in one
   Mishnah forced it; single-answer functions would have been wrong on day
   one.
3. **Provenance is part of the return type** — every engine verdict carries
   its Mishnah row, its Talmud bridge, its Genesis anchor, and either the
   machine claim that held it or an explicit imported_from. A verdict that
   cannot say where it came from does not exist in this system.
4. **Rules may know more than the exam** — riders and epistemic grades ride
   in the verdict's basis. The engine repeats the tradition's own honesty
   ("no proof, but a hint") instead of laundering it into certainty.
5. **The Mishnah's organization is the code's organization** — modules
   routed cleanly by topic; the uncompiled module (judgment_durations)
   stands beside the compiled ones as the visible contrast.

## Files

- cases_pilot.yaml — the spec, now carrying before/after classes, engine
  answers with full provenance, and the corrected row with its correction
  note kept visible.
- engine.py — the first two compiled modules (life_override,
  procreation_measure); judgment_durations deliberately left uncompiled.
- run_exam.py — the examiner; re-runnable anytime.
- EXAM_LEDGER.md — every case-shelf row consulted, append-only.

## Honest limits

- Ten cases, three passages, two compiled modules — the SHAPE is
  established, not the architecture. engine.py is a throwaway draft whose
  lessons survive it.
- The Class B "held as text" judgments were made by reading the holdings
  (quoted in the ledger), not by a mechanical semantic match — a future
  exam at scale needs a sturdier holdings-search than keyword hunting.
- EDU_2_10_a is the nearest miss to Class A the machine has: it holds the
  twelve-month ruling, the census membership, AND the date-facts to compute
  the duration — only arithmetic application is missing. When the
  judgment_durations module is compiled, that case should be the first
  whose verdict is COMPUTED from the machine's own date operators rather
  than imported.
