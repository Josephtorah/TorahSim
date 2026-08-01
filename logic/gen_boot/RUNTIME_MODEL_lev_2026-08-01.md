# How the Torah runs: Leviticus as installed code — the execution model

Written 2026-08-01 at owner order, capturing the answer to: *"how would the
Torah code run on its own with this Lev code? Would it compile in order,
run in order, use Numbers, Deuteronomy? Does it run sequentially?"*

Status honesty: eight units are DERIVED AND FROZEN (gen_01..gen_07 — the
creation week; lev_13_intake_quarantine — Lev 13:1-8, the first law unit).
The book-level gradient, receipt system, and genre census are MEASURED
(DISPOSABLE_scan reports, 2026-07-30). Every verse quoted below was
verified against our own DB before being cited. The rest is the model
those instruments support — and the Stage E linker (planned, owner-gated)
is what will make cross-unit execution real inside the machine. Every
Hebrew term carries its English gloss — absolute rule.

---

## 1. COMPILE: yes — sequential, single-pass, declared-before-used

Measured: each book reads previously-installed symbols at a rising rate —
Genesis installs nearly everything new; Exodus reads ~76% inherited
symbols; Leviticus ~90%; Numbers ~91%; Deuteronomy ~94%. Symbols are
declared before use corpus-wide; the runtime demo made this executable
(its linker resolved all 13 of Lev 13's imports from strictly-earlier
installs, zero misses — `torah_runtime_demo_2026-07-31.py`, PART 3).

The rare early uses are *forward declarations*, not violations: *tahor*
("pure") appears at Gen 7:2 — Noah's clean animals — four books before
Lev 11-15 specifies the purity system. The symbol is used first, fully
defined later: a prototype.

## 2. RUN: no — execution is event-driven, in three interleaved modes

1. **Narrative executes immediately.** The *wayyiqtol*
   ("and-then-he-did") spine runs once, in order, where it stands. The
   creation week is the boot sequence; boot logs are linear (which is why
   the seven-days rendering is all definitions and no branches).
2. **Law installs; it does not run where it appears.** The *weqatal*
   ("and-he-shall-do", TIR-029) chains are standing handlers awaiting
   triggers. Lev 13:1-8 installs a *ki* ("when") case and six handlers —
   and narrates ZERO executions (machine state: seven standing facts,
   every other register untouched). Some handlers fire on TIMERS, not
   cases: the Sabbath weekly ("an eternal covenant, throughout their
   generations"), the festivals yearly.
3. **Standing state persists** — mandates (the day-5/6 blessings),
   covenants, statuses (*kadosh* "holy", *tamei/tahor* "impure/pure") —
   conditioning all later execution.

Textual position = **installation site**. Execution site = wherever a
matching case occurs in narrative time, afterward.

## 3. NUMBERS: the runtime log — and the exception log

Installed law meets moving narrative in Numbers.

**A handler fires — Miriam (Num 12:10-15), the corpus's own test case for
Lev 13** (DB-verified): *ve-hineh Miriam metzora'at… va-yifen Aharon…
VE-HINEH* ("and BEHOLD… and Aaron turned… and BEHOLD" — the Lev 13
inspection deictic, twice, with Lev 13:2's named inspector beholding);
*shivat yamim TISAGER… michutz la-machaneh* ("seven days she shall BE
SHUT UP… outside the camp") answered by *va-TISAGER Miriam* ("and Miriam
WAS shut up") — command-imperfect popped by execution-wayyiqtol, the same
verb-echo receipt pattern the creation units documented (*yihyeh* →
*va-yehi*). The whole system blocks on the timer: "the people did not
journey until Miriam was gathered back."

**Four times, a case arrives with NO handler installed** — and the text
records the escalation, twice in its own formula *lo forash* ("it had not
been specified"):

| case | verse (DB-verified) | the escalation | the patch |
|---|---|---|---|
| the blasphemer | Lev 24:12 — "in custody, TO HAVE IT DECLARED by the mouth of the LORD" | ruling requested | Lev 24:13ff |
| the impure at Passover | Num 9:8 — "stand, and I will HEAR what the LORD commands for you" | ruling requested | Pesach Sheni (Num 9:9-14) — a whole new law |
| the wood-gatherer | Num 15:34 — "in custody, for it had NOT BEEN SPECIFIED (lo forash) what should be done to him" | ruling requested | Num 15:35-36 |
| Zelophehad's daughters | Num 27:5 — "and Moses BROUGHT their case before the LORD" | case escalated | inheritance statute (Num 27:6-11) |

And Numbers 36 — the book's final chapter — **amends the Num 27 patch**
when the tribes surface a conflict it created: exception → escalation →
hotfix → regression → second hotfix, narrated in canonical order.

## 4. DEUTERONOMY: the re-release

Deuteronomy re-states the law with deltas (the diff project is planned
instrumentation), reading ~94% inherited symbols, addressed to the next
runtime — the generation entering the land. Deut 24:8-9 shows the
mechanism in two verses (DB-verified): it does NOT re-legislate
*tzara'at* — it **points**: "take care… to do all that the priests
instruct you" (a reference to the installed Lev 13-14 module) and
"remember what the LORD did to Miriam" (a reference to the Num 12
execution log). Module pointer + test-case pointer: **the law citing its
own regression test by name.**

## 5. Not even the narrative is strictly chronological

The chain made a rule of it: *ein mukdam u-me'uchar ba-Torah* ("there is
no earlier-and-later in the Torah" — rules 31/32 of the 32 middot,
"measures"/interpretive rules). Numbers opens dated month two; Num 9
backs up to month one. Textual order is **dependency order**, not
timestamp order — what you would expect of code, where installation
order matters and the log may be presented out of sequence.

## 6. Termination: it doesn't

Day 7's open transaction (gen_07: blessed, sanctified, never committed —
`LEDGER stays EMPTY`, machine-checked) generalizes: the timers fire
forever, per-case loops spawn as cases arrive, and the program ends not
with an exit but a **handover** — Moses dies with the re-stated code
delivered to the next host. The Torah compiles once and runs as a daemon.

## 7. What Leviticus IS in this model

The installed-code library. Its genre signature, measured at book scale
(Lev 1: two narrative verbs vs twenty-seven *weqatal* handlers) and now
at operator scale (lev_13_intake_quarantine: ONE *wayyiqtol* frame verb,
then a case + six handlers), is the signature of a module: almost no
events, almost all definitions. Its vocabulary is either **imported**
(the intake's opening five words carry four imports: *adam* — day 6;
*or* "skin" — Gen 3:21; *basar* "flesh" — Gen 2:21; *nega* "mark" — Gen
12:17) or **chapter-owned** (*baheret* "bright spot", *mispachat* "scab",
*pasah* "spread" live almost nowhere else — a bounded lexical domain,
like a module's private names). Its verdict axis is not the narrative's
*tov* ("good") but *tamei/tahor* ("impure/pure") — the axis seeded at the
ark and assigned to the priests at Lev 10:10 with the creation week's own
partition operator (*havdil*, "divide": God divides, day 1 → fixtures
divide, day 4 → officers divide, Lev 10:10).

## 8. Where the files live

| layer | files |
|---|---|
| source text (the only authority) | `Data/Lev.xml` (with `Data/Gen.xml` … `Data/Deut.xml`); parsed into `torah_grok.sqlite` (gitignored, rebuildable) |
| derived logic — FROZEN | `logic/units/lev_13_intake_quarantine.yaml` (Lev 13:1-8; frozen 2026-08-01) beside `logic/units/gen_01_*.yaml` … `gen_07_*.yaml` (the week) |
| interpreter | `run_unit.py` (Stage D; law operators CASE/HANDLER added at the lev_13 freeze) |
| old-era segmentation maps | `logic/units/lev_13_skin_initial.yaml`, `lev_13_boil_burn.yaml`, `lev_13_head_isolation.yaml`, `lev_13_garment.yaml` + ~60 more `lev_*` (pre-derivation format; not run by the interpreter) |
| learning renderings (sketch tier) | `logic/gen_boot/torah_runtime_demo_2026-07-31.py` (the combined end-to-end demo), `seven_days_2026-07-31.py`, `lev13_imports_2026-07-31.py`, `lev13_decision_tree_2026-07-31.py`, and this document |
| detector instrumentation | `logic/middot_scan/WATCHLIST_lev13_intake_prospective_2026-07-31.md` |
| translation cache + provenance | `Data/sefaria_texts/Onkelos_Leviticus_13_*.json` (gitignored) · `Data/FETCHLOG.md` (tracked) |

Next in the pipeline, all owner-gated: the Lev 13 triage (Sifra Tazria +
Mishnah Negaim enter the cache — the middot detector's legal-device
tripwire test), unit two of the pilot (Lev 13:9-17, the chronic case),
the Num 12 derivation (Miriam — the regression test the law itself
cites), and Stage E (the linker that makes this document's model run
inside the machine instead of beside it).

*Experimental model — not binding religious law.*
