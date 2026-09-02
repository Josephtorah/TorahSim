# THE MISHPATIM RE-COMPILATION PASS (2026-09-02, under the compiler law)

The owner's order, after the discussion of reviewing Genesis and
Exodus under the compiler law: "Ok run it and report what you find."
Target: the law code of the portion Mishpatim (Exodus 21:1–23:19) —
already derived, already examined; now RE-COMPILED cold from the
ink, graded against the Mishnah's answer sheets. Runner:
World/step9/cold_run_mishpatim.py (26 token probes, zero-report law
enforced in code; read-only; no unit touched). Companion:
cold_run_guardians.py (the sixth function, 12/12, same day).

## THE SCORE

**35/35 cells across six functions.** This pass: 23/23 over five
functions. With the guardians: 35/35.

| function | answer sheet | cells | result |
|---|---|---|---|
| four guardians | Mishnah Shevuot 8:1 | 12 | 12/12 |
| slave-release list | Mishnah Kiddushin 1:2 | 3 | 3/3 |
| four-damages class map | Mishnah Bava Kamma 1:1 | 5 | 5/5 |
| goring-ox state machine | Mishnah Bava Kamma 1:4 + 2:4 | 6 | 6/6 |
| five injury indemnities | Mishnah Bava Kamma 8:1 | 5 | 5/5 |
| theft multiples | Mishnah Bava Kamma 7:1 | 4 | 4/4 |

## THE MEASURED FRACTIONS — the number the compiler law asked for

Every cell carries provenance. Across all 35:

- **INK: 21 cells (60%).** Straight from the bare text — the six-year
  timer with its free-token, the four class openers, the half-by-
  division and full-payment rules, the ransom branch, the thirty
  shekels, the medical and idleness clauses, the double/fourfold/
  fivefold constants WITH their scope restriction, the oath
  signature, the best-of-field payment.
- **RECORDED INFERENCE: 8 cells (23%).** Filled by a Talmud argument
  replayed with its source row — the paid/unpaid theft-diff, the
  loss a-fortiori, the borrower comparison, the deduction from "let
  her be redeemed," the three-goring threshold from the temporal
  tokens, the best-of-land generalization, the tariff-to-money
  conversion, pain from "wound for wound."
- **ROUTED / CROSS-MODULE IMPORT: 6 cells (17%).** The renter row,
  the Jubilee release, the reversal-to-innocuous rule, humiliation
  from Deuteronomy 25.

Sixty percent of the Mishnah's tables sit in the bare ink of this
code. Nobody would have guessed the fraction was that high before
measuring — and the remaining forty percent is not mystery: every
cell of it names the recorded row that supplies it.

## THE FIND OF THE PASS: the compiler needs the call site

The one discovery that reorders the roadmap. The DAMAGE indemnity —
eye-for-eye as MONEY — is the heart of Mishnah Bava Kamma 8:1, and
the Talmud's derivation of it (Bava Kamma 83b–84a, pulled at the
rows) does not run on Exodus 21 alone. The sugya's operative verses
are **Leviticus 24:21–22** — "one who strikes an animal shall pay
... and you shall have ONE MANNER OF LAW" — which is THE CALL SITE:
the second and only other occurrence of the exact eye-for-eye
formula in the entire canon (our whole-Bible scan found the pair:
Exodus 21:24 and Leviticus 24:20). The blasphemer chapter's
restatement of the tariff, with its equal-law rider, is what fixes
the seat's semantics as compensation rather than maiming.

Consequence, stated plainly: **compiling the seat requires the call
site.** Exodus 21's tariff cannot be finished from Exodus alone —
the teacher compiles it through Leviticus 24. Which means the next
book is not merely "the first recorded call into the machine we
built" — it is a MISSING COMPILE DEPENDENCY of the book we already
finished. The pass measured that dependency; it did not assume it.

## THE SYNTAX BOUNDARY, MEASURED

The case-keyword census over the whole law code (21:1–23:19):
verse-initial כִּי ("when") case openers at 21:2, 7, 14, 18, 20, 22,
26, 28, 33, 35, 37; 22:4, 5, 6, 9, 13, 15, 26; 23:4, 5. The אִם
("if") branch count by chapter: 15 in chapter 21, 17 in chapter 22,
**zero in chapter 23.** The case machine is densest from 21:2 to
22:15 and the code then shifts to command-style (apodictic) law —
"you shall not..." — a different syntax family the parser must not
force into case form. The compiler's casuistic front end has a
measured domain.

## HONEST LIMITS OF THE PASS

1. Cell grain is coarser here than in the guardians run — these are
   function-level verdicts (the release list, the class map, the
   state machine's rules), not full input-by-input matrices. The
   guardians matrix remains the depth standard.
2. The teacher moves are still hand-encoded replays of the recorded
   arguments, each labeled — middot-as-data remains the standing
   next rung.
3. Coverage: six functions spanning eleven of the code's twenty
   case openers. NOT yet compiled (enumerated, not hidden): the
   maidservant's own designation ladder (21:7–11, only her
   redemption clause used), the altar-murderer (21:14), the struck
   slave (21:20–21), the miscarriage clause with its life-for-life
   rider (21:22–25 as its own case), the freed slave's eye and
   tooth (21:26–27), the seducer (22:15–16), the garment pledge
   (22:26), the enemy's straying animal (23:4–5), and the whole
   command-style tail (22:17–23:19).

## WHAT THE PASS SETTLES ABOUT "REVIEWING" GENESIS AND EXODUS

The question that launched this run was whether the finished books
need review under the new law. The answer the run gives: nothing in
them is WRONG — the stamps stand, the exams stand — but re-compiling
them is cheap, fast, and yields exactly what the compiler needs:
the measured ink/recorded/routed fractions and the growing catalog
of teacher-move types (diff, a-fortiori, comparison, routing,
threshold-parse, generalization, cross-module import — seven
distinct move types observed across 35 cells). The pass also
surfaced one real dependency (Leviticus 24) that the derivation
order alone would never have flagged. Recommendation standing from
the discussion, now with evidence: continue the re-compilation over
the remaining Mishpatim openers, then the rest of Exodus's law
sections, while Leviticus reading proceeds — and let Leviticus 24
close the tariff's open dependency when we reach it.

STATUS: model-layer experiment; read-only; nothing ruled beyond the
standing compiler law; both runners re-runnable at any time.

## PASS 2 (same day, owner: "feel free to find a few more") — 9/9

Runner: cold_run_mishpatim_2.py (6 probes, all fired). Three more
functions:

- **The seducer's fine (Exod 22:15-16) — 3/3 vs Mishnah Ketubot
  3:4.** The find: the ink holds a POINTER, not a number — "money
  like the dowry of the virgins" — and the constant (fifty silver)
  lives in Deuteronomy 22:29; the link is recorded (Ketubot 29b:3
  parses the triple mention). A cross-book constant fetch: one book
  names the price, the other holds the price list.
- **The freed slave's limbs (21:26-27) — 3/3 vs Kiddushin 24a +
  Mishnah Negaim 6:7.** Eye and tooth are INK; the gemara itself
  says "granted, a tooth and an eye are WRITTEN" and generalizes
  the exemplars to the class — limb-tips that do not regenerate —
  which the Mishnah enumerates as twenty-four members. The
  EXEMPLAR-GENERALIZATION move, the eighth teacher-move type
  catalogued.
- **The miscarriage valuation (21:22) — 3/3 vs Mishnah Bava Kamma
  5:4.** The court-assessment is INK ("by the judges"); the
  valuation ALGORITHM (appraise her worth before and after, pay the
  difference) is the answer key's, with Rabban Shimon ben Gamliel's
  objection recorded beside it; the person-pays/ox-exempt actor
  split rides the ink's own case opener ("when MEN strive").

**RUNNING TOTAL: 44/44 across nine functions.** Combined fractions:
INK 26 (59%), RECORDED 9 (20%), ROUTED/IMPORT 9 (20%). Eight
teacher-move types now catalogued (diff, a-fortiori, comparison,
routing, threshold-parse, generalization, cross-module import,
exemplar-generalization). Listening deliverable baked at the
owner's word: The_Day_We_Ran_The_Law.md + .epub (repo root) — the
whole pass told as a conversation between two non-programmers.
