# THE MOVE CATALOG — the teacher's compile moves, registered

**Standing law (owner-ruled 2026-09-02).** The owner's words: "I like
the catalogue registry. This is probably going to be one of the more
important records to keep because we are in discovering deep logic...
it needs to be updated when we find this logic." And on adoption:
"Yes, make this change. This is very exciting. We are finding deep
logic now."

This file is the canonical registry of TEACHER MOVES — the recorded
reasoning forms by which the Mishnah/Talmud layer compiles the
24-book code: fills the gaps the bare ink leaves open, and gets from
the text's mechanisms to the answer key's tables. It is updated THE
SITTING a new move (or a new exemplar of a known move) is
discovered — a standing duty, no owner approval per update; every
machine-administered update is labeled delegated, and the owner can
overrule any entry. Entries are never deleted; corrections append.

Relation to the other registries: logic/MIDDOT.md holds the
tradition's own numbered inference rules (13 law / 32 narrative) —
the tradition's names for its logic. THIS catalog holds the moves as
the COMPILER meets them: operational forms, each with measured
exemplars, machine-replayed where a cold run exists. Where a move IS
one of the middot, the entry says so. World/step9/RULE_CATALOG.md
holds the compiled output rules (R-numbers); this file holds the
moves that produce them.

Format per entry: the move, in plain words; what gap it fills; the
recorded exemplars (each with its source rows and, where run, the
cold-run cell it filled); middah correspondence if any; date found.

---

## M-01 — THE DIFF (recover a hidden parameter from branch outputs)

**The move:** two near-identical code passages never state what
distinguishes them; feed both the same input, compare the outputs,
and infer the hidden configuration from which one is stricter —
anchored by the principle that liability tracks benefit.
**Fills:** hidden parameters the ink never names.
**Exemplars:** the paid/unpaid keeper — both paragraphs say only "to
keep"; on theft, paragraph one exempts by oath, paragraph two pays;
stricter = compensated (Babylonian Talmud Bava Metzia 94b:7-10, with
the double-payment objection raised and answered). Cold-run:
cold_run_guardians.py, role-assignment step, 12/12.
**Middah:** none of the thirteen — this is SEVARA, reasoned analysis,
which the Talmud holds as a source in its own right ("it stands to
reason," and elsewhere: why do I need a verse? it is reasoning).
**Found:** 2026-09-02 (the code hunt).

## M-02 — THE A-FORTIORI (generate a missing cell from a stronger one)

**The move:** if the rule holds in the harder case, it holds all the
more in the easier one — the tradition's own qal va-chomer (light-
and-weighty), first of the thirteen middot.
**Fills:** cells absent from the ink entirely.
**Exemplars:** LOSS never appears in the keepers' nine verses; "if
theft, which is near to circumstances beyond control, pays — loss,
near to negligence, all the more so" (Bava Metzia 94b:15, "they say
in the West"). Cold-run: the paid keeper's loss cell.
**Middah:** #1, QAL VA-CHOMER (light-and-weighty) — an EXACT match:
this move IS the first of the thirteen, machine-replayed.
**Found:** 2026-09-02.

## M-03 — THE COMPARISON (carry a rule between passages by their shared frame)

**The move:** two passages about the same institution share structure;
what one states explicitly is carried to the other through the shared
frame ("just as below... so too here").
**Fills:** rules stated in one variant but needed in a sibling.
**Exemplars:** the borrower's theft/loss liability, carried from the
paid keeper's passage (Bava Metzia 94b:19), sealed by
all-benefit-is-his (94b:10). Cold-run: borrower theft/loss cells.
**Middah:** the #2/#3 family — the "just as below" frame-comparison
works like the founding-case and verbal-analogy forms; the gemara
runs it as structural comparison rather than naming a middah.
**Found:** 2026-09-02.

## M-04 — THE ROUTING (classify an unnamed input onto an existing branch)

**The move:** a case type the code never names arrives; the teacher
files it under an existing branch's rules — and logs the recorded
dispute over which branch.
**Fills:** the gap between the code's N variants and the world's N+1
case types.
**Exemplars:** the RENTER — the code defines three keepers; the
answer key lists four; the renter follows the paid keeper's row
(Mishnah Bava Metzia 7:8; the four-fold division affirmed and the
routing disputed at Bava Metzia 93a:17), hooked on the ink's own
hire-clause ending Exodus 22:14. Cold-run: the renter row, 3 cells.
**Middah:** none named — this is the classification practice the
Talmud performs when sorting derivatives under primaries (the
avot/toladot sorting that opens Bava Kamma).
**Found:** 2026-09-02.

## M-05 — THE THRESHOLD-PARSE (read a numeric constant out of the verse's own tokens)

**The move:** a state-transition constant is encoded in the verse's
wording; the teacher tokenizes the phrase and counts — and preserves
rival tokenizations by name.
**Fills:** numeric thresholds the code states as idiom.
**Exemplars:** the goring ox's "from yesterday and the day before,
and its owner has not secured it" → THREE gorings flip innocuous
(תָּם "innocent") to forewarned (מוּעָד) — Abaye's count and Rava's
count both preserved (Bava Kamma 23b:17-18); the counter's
SEMANTICS debated at 24a:9 (about the ox, or warning the owner?).
Cold-run: the threshold cell.
**Middah:** not of the thirteen — this is the REDUNDANCY EXPOSITION
of the Akiva school (every seemingly extra word load-bearing); the
Abaye/Rava split is literally a dispute over whether the doubled
idiom is expounded word-by-word — a recorded parser-settings
disagreement.
**Found:** 2026-09-02.

## M-06 — THE GENERALIZATION (one ink instance becomes the class rule)

**The move:** the code states an output rule inside one case; the
teacher generalizes it across the sibling classes that share the
interface.
**Fills:** common-output rules stated once.
**Exemplars:** "the best of his field and the best of his vineyard
shall he pay" (Exodus 22:4, in the grazing case) → damages are paid
from the best, across all four primary categories (Mishnah Bava
Kamma 1:1's common-denominator clause; the discussion at Bava Kamma
6b:11). Cold-run: the best-of-land cell.
**Middah:** #3, BINYAN AV (the founding case) — one stated instance
founds the rule for the class sharing its feature; the Mishnah's own
"common denominator" is this middah's vocabulary.
**Found:** 2026-09-02.

## M-07 — THE CROSS-MODULE IMPORT (a rule from another book reaches in)

**The move:** an event or constant declared in a different book of
the code overrides or completes the local passage; the teacher
documents the wiring — including that the code "needed to write"
the connection.
**Fills:** local gaps whose answer lives in another module.
**Exemplars:** (a) the JUBILEE (Leviticus 25) releases the Hebrew
slave — even the pierced one whose ink says "forever" (Mishnah
Kiddushin 1:2; Kiddushin 15a:19). (b) HUMILIATION, the fifth
indemnity, sourced from Deuteronomy 25:11-12. (c) THE CALL-SITE
DEPENDENCY, the pass's largest find: eye-for-eye-as-MONEY is derived
through Leviticus 24:21-22 — the formula's only other exact
occurrence in the canon (machine scan: Exodus 21:24 + Leviticus
24:20 and nowhere else) — so the Exodus seat cannot be finished
without the Leviticus call (Bava Kamma 83b:10, 84a:1). Cold-run:
Jubilee, humiliation, and damage-as-money cells.
**Middah:** mixed — the call-site derivation runs on #2 (GEZERAH
SHAVAH, the verbal analogy on the shared striking-word) with the
harmonization family (#13, two passages resolved together) behind
it; the Jubilee wiring is the Talmud's NECESSITY ANALYSIS ("it was
needed to write both"), practice rather than a numbered rule.
**Found:** 2026-09-02.

## M-08 — THE EXEMPLAR-GENERALIZATION (named instances imply the category)

**The move:** the code names two concrete instances; the teacher asks
"granted, these are WRITTEN — what of the rest?" and derives the
category they exemplify; the answer key then enumerates the
category's members.
**Fills:** the gap between the ink's examples and the law's class.
**Exemplars:** the freed slave's EYE and TOOTH (Exodus 21:26-27) →
the class "limb-tips that do not regenerate" (Kiddushin 24a:6) →
twenty-four members enumerated (Mishnah Negaim 6:7). Cold-run: the
class cell, pass 2.
**Middah:** #3, BINYAN AV FROM TWO VERSES — the thirteen explicitly
distinguish the founding-case from ONE verse and from TWO; eye and
tooth are the two-verse form (the common-feature argument).
**Found:** 2026-09-02.

## M-09 — THE KEYWORD DICTIONARY (the language manual for the code's own words)

**The move:** the teacher maintains corpus-wide semantic entries for
the code's operator words — the senses of a keyword, and the
enumerated exceptions to its default.
**Fills:** disambiguation the parser needs before any case can be
cut correctly.
**Exemplars:** (a) כִּי ("when/if") "has four distinct meanings: if,
perhaps, rather, because" — Reish Lakish (Gittin 90a:10). (b) "Every
'if' (אִם) in the Torah connotes optionality, EXCEPT FOR THREE" —
Rabbi Yishmael, with the three enumerated (Mekhilta DeRabbi
Yishmael, Tractate Bachodesh 11:11). Used by: the verse-initial-KI
parse rule in both cold runners.
**Middah:** none — this is the LEXICON, the layer beneath the
middot: the thirteen presuppose that the keywords are already
correctly read, and these entries are the tradition doing that
reading corpus-wide.
**Found:** 2026-09-02.

## M-10 — THE POINTER-FETCH (a label in one book, the constant in another)

**The move:** the code states a value by NAME rather than number; the
named constant is defined in a different module; the teacher records
the link that resolves the pointer.
**Fills:** unpriced fines, unspecified measures.
**Exemplars:** the seducer pays "money like the dowry of the
virgins" (Exodus 22:16) — a label, no number; the constant, fifty
silver, lives in Deuteronomy 22:29; the link recorded (Ketubot
29b:3 parsing the triple mention; the payments table at Mishnah
Ketubot 3:4). Cold-run: the FETCH-50 cell, pass 2. Distinct from
M-07: the import brings a RULE in; the fetch resolves a NAMED VALUE.
**Middah:** #2-family — the recorded resolution runs through the
verbal-analogy machinery on the shared dowry/virgin ink (with the
Akiva-school triple-mention inclusion at Ketubot 29b beside it).
**Found:** 2026-09-02.

---

RUNNING COUNT: 10 moves, all exemplified at pulled rows, 9 of 10
exercised by a cold run (M-09 is used by the parser itself).

THE MIDDAH CORRESPONDENCE, measured (2026-09-02, owner's question):
roughly half the moves ARE numbered middot — M-02 is #1 exactly
(qal va-chomer); M-06 and M-08 are #3 (binyan av, one-verse and
two-verse forms); M-07 and M-10 run on #2 (gezerah shavah) with the
#13 harmonization family behind the call-site. The other half is
the Talmud's DOCUMENTED PRACTICE beyond the numbered list: sevara
(M-01), classification (M-04), the Akiva-school redundancy parser
(M-05), necessity analysis (inside M-07), and the lexicon (M-09).
Reading: the thirteen middot are the PUBLISHED instruction set —
the formally licensed derivation forms — while this catalog records
the FULL observed instruction set in use, which is larger. The
published subset is the natural first target for middot-as-data. The
compile-dependency graph so far: Exodus 21 ← Leviticus 24 (M-07c);
Exodus 22 ← Deuteronomy 22 (M-10); Exodus 21 ← Leviticus 25 (M-07a);
Exodus 21 ← Deuteronomy 25 (M-07b).

## M-11 — THE WORD-ORDER READ (the clause sequence itself is the condition order)
The teacher reads the ORDER of the ink's clauses as executable
sequence: at Lev 5:1 "and he heard the voice of an oath AND HE IS a
witness" — the witness-state is evaluated AT the oath, so an oath
that precedes the knowledge finds no witness and exempts (Mishnah
Shevuot 4:9 falls straight out of the word order); at Lev 2:14 the
placement of "with fire" between the parch-word and the groats-word
rules parch-before-grind (the Sifra names the hiatus itself). Found
2026-09-03, the Vayikra sweep + the Leviticus 5 cold compile
(cold_run_vayikra5.py — the S4_9 cell graded pure ink).
**Middah correspondence:** the near of Rabbi Eliezer's #12 family
(a thing understood from its context) — sequence as context.

## M-12 — THE GRAMMATICAL-NUMBER HOOK (a plural or suffix carries the loop)
The teacher hangs an iteration or a set-rule on the ink's NUMBER
morphology: Lev 5:24 writes "its FIFTHS" (vachamishtav, plural,
written defective beside 5:16's plene singular) — the recursion hook
for fifth-upon-fifth down to the perutah floor (Mishnah Bava Kamma
9:7); Exod 35's plural logs yield the TWO afternoon logs (Mishnah
Shekalim 6:6's floor); Lev 1:2's plural "shall you offer" yields
partnership. The hook is a LETTER; the loop's semantics are the
recorded move; the floor is data. Found 2026-09-03, the Leviticus 5
cold compile.
**Middah correspondence:** Rabbi Ishmael's ribbui (inclusion) family
— the inclusive token read as an iterator, not just an extra member.
