# REVIEW — the Behar-Bechukotai sweep, code missed (2026-09-05)
# Owner: "can you do a short review and detect any obvious missed
# code? discuss, don't do it yet" → "yes but first we need to compact."
# The six findings, ranked by value; the owner's decision: items 1 and
# 2 run as ONE SITTING after the compaction, BEFORE Numbers.

## 1. Leviticus 26 has no compiled function (the biggest miss)
The covenant chapter is the ledger's indictment schedule. Its
sabbath-debt clause has a recorded RUN in the canon: 2 Chronicles
36:21 — עַד רָצְתָה הָאָרֶץ אֶת שַׁבְּתוֹתֶיהָ (until the land was paid
its sabbaths) כָּל יְמֵי הָשַּׁמָּה שָׁבָתָה (all the days of desolation
it rested) לְמַלֹּאות שִׁבְעִים שָׁנָה (to fill seventy years) — quoting
Lev 26:34 word for word, with Jeremiah 25:11's seventy years beside
it. That is the demonstrate-by-RUN form the compiler law names
(Torah demonstrates by spec, the Writings by run), and the
whole-Tanakh indictment check is the stated target. Seated as prose
(LV26-21) and never compiled; the run never linked.
PLAN: cold_run_tochacha.py — the conditional cascade as a state
machine (the Sifra's seven-step descent, the sevenfold rule, the
good/harsh measures), the SABBATH-DEBT as a land-entity timer whose
missed firings accumulate, and the RUN cell: the unkept sabbaticals
computed against the recorded seventy (2 Chr 36:21 / Jer 25:11) —
the answer sheet here is the Writings' own log, not the Mishnah.
Effects to discover from the chapter's verbs: exile / scattering /
desolation entries and the land-debt timer.

## 2. The docket is link-driven, so a whole tractate never met the engine
Mishnah Sheviit (10 chapters, 89 rows) is the answer sheet for Lev
25:1-7 and 25:20-22 and barely quotes verses — the links produced
ZERO rows. THE TWO SHELVES ruling (owner 2026-08-27) routes the
testing shelf BY TOPIC, not by citation. Smaller, same pattern:
Arakhin 50 rows / 16 graded; Temurah 35 / 3; Bekhorot 9 (the animal
tithe chapter) mostly unread; Bava Metzia 5 (interest, 11 rows) 2
graded.
PLAN: a topic-routed docket supplement — read Sheviit whole, and
the unread rows of Arakhin, Temurah, Bekhorot 9, Bava Metzia 5 —
verdicted LAW/CONTEXT/CREDIT in an append-only ledger; new modules
for the seventh-year engine (the labor list, the eater list, the
field-clock, the aftergrowth, the export border); extend
cold_run_yovel.py's sabbatical cell into a function graded against
Sheviit's rows. Enumerate by topic from logic/MISHNAH_TOPICS.md so
the gap is closed mechanically, not by memory.

## 3. Lev 27 is half-compiled
The valuation table and the field are in the Jubilee engine.
Substitution (27:9-13), the house and its fifth (27:14-15), the
firstborn and the impure beast (27:26-27), devotion (27:28-29), and
the tithes (27:30-33) live only as exam scaffold cells. The error
rule at 27:32 (the ninth/tenth/eleventh naming machine) was never
written. PLAN (later): a second compile pass on Lev 27's remainder.

## 4. Effects not discovered where the ink has verbs
25:35 "strengthen him" — a support duty with no obligation entry;
27:10 "it and its substitute shall be holy" — a status on a second
animal with no effect; Lev 26's exile / desolation / scattering
verbs — no entries and no land-debt timer (item 1 needs them).

## 5. Gaps inside the Jubilee engine
The sabbatical year is one cell (no labor list, no eater list, no
field-clock); overreaching is two cells; the master's duty to feed
the slave's wife and children, the auction-stone ban, and the
"in your sight" bound have no cells. Item 2 covers the first.

## 6. Method: the dishonest-pairing trap
Two consecutive compiles' first drafts graded a cell against a value
computed from the cell itself (round 45's date cell; round 46's
priest count). Caught in self-review both times. A MECHANICAL check
— refuse any test whose expected value is derived from the graded
cell — would close it. Add to effects_layer or a shared test helper
when the next compile is written.

Standing items unchanged: the four lev_04 chatat drafts, the
py-render gloss flags, the vocabulary YAML never linted (all on the
deferred audit's list, REVIEW_LEV1-8_2026-09-05.md).

## ITEMS 3, 4, 5 CLOSED — sitting B of the audit (2026-09-05)
3. cold_run_temurah.py — Lev 27:9-15 and 27:26-33 as their own cold
   function: 40/40 at 60% pure ink against Mishnah Temurah, Arakhin 8,
   Bekhorot 9, Menachot 12:1; substitution's formulas from the two
   written verbs; the house's fifth; the firstborn's value-consecration;
   devotion; the tithe under the rod; three calls into the Jubilee and
   Passover engines. Effect: consecrated.
4. The 25:35 support duty: supports_kinsman registered (a DEBIT on the
   kinsman), three cells in cold_run_yovel.py on the Sifra's falling-load
   row. (27:10's "it and its substitute shall be holy" is the temurah
   engine's consecrated + substitution pair.)
5. The auction-stone ban (25:42, Sifra Behar Section 6 1) and the
   in-your-sight bound (25:53, Chapter 8 8) — cells in cold_run_yovel.py
   (75/75). Items 1, 2, 6 were round 47's. Every item of this review is
   now closed.
