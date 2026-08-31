# FINDINGS QUEUE — append-only intake for everything the process surfaces
# (Set up 2026-08-31 on the owner's order: "we need to setup this process to
# allow for updates when we find them, even on the stamped code.")
#
# THE LOOP: SURFACE (exams, audits, derivations file here) -> RULE (owner:
# seat / import-only / reject) -> SEAT (rev bump + claim + operator + gates +
# ritual, the 2026-08-31 seat-the-two-claims path) -> CLOSE (resolution
# appended here; the next exam run shows the case flipping to machine-held).
# Rows are never edited — resolutions are appended under the finding.
# PROPOSED STAMP LAW (awaiting owner word): an amended stamped unit keeps its
# stamp, records that the stamp predates the new rev, and joins a
# re-affirmation queue the owner batch-stamps — the gen_08 precedent.

## From the Step 9 pilot exam, 2026-08-31 (World/step9/REPORT.md)

**F-001 · OPEN — the dead->stop leg of the rockslide rule is unseated.**
Mishnah Yoma 8:7's third verdict (found dead mid-clearing -> stop; Shabbat
is not desecrated for the dignity of the dead) is held nowhere in the
machine. Candidate seat: gen_18_the_rise beside claim G18-05 (Gen 7:22),
whose claim already carries the first two legs. Source: Mishnah Yoma 8:7
(read, exam ledger row 1). Engine carries it as imported_from meanwhile.

**F-002 · OPEN — the miscarriage-restart clause is unseated.** Mishnah
Yevamot 6:6: the ten-year childless count restarts from a miscarriage. The
ten-years law itself is seated (G32-16, Gen 16:3, four seats) but no claim
carries the restart clause. Candidate seat: gen_32_hagar_angel beside
G32-16. Source: Mishnah Yevamot 6:6 (read, exam ledger row 2); Yevamot
64a:5 is already among G32-16's cited seats.

**F-003 · OPEN — the dissent on the woman's obligation is unseated.** The
machine holds the exemption side in ink (G06-03, the lean ve-khivshuha
ketiv of Gen 1:28 — 'and subdue HER', the man commanded) but not R.
Yochanan ben Beroka's dissent (commanded — 'God blessed THEM', Gen 1:28).
A recorded dispute half-held is against the corpus's own dual-track law.
Candidate seat: gen_06_land_adam_dominion beside G06-03. Source: Mishnah
Yevamot 6:6 (read, exam ledger row 2).

**F-004 · OPEN — engine work, not corpus: compute the flood's twelve
months.** EDU_2_10_a is the machine's nearest Class-A miss: it holds the
twelve-month ruling, the five-census membership, AND the date-facts
(G17-11). Compile judgment_durations so the duration is COMPUTED from the
machine's own date operators — the first end-to-end derived verdict. No
corpus change involved.

**F-005 · REJECTED-CANDIDATE — the gehinom duration is off-book.** Mishnah
Eduyot 2:10's disputed member (twelve months vs Passover-to-Shavuot) has no
Genesis anchor; it belongs to the census's later members. Recommend:
import-only forever, revisit when the relevant books are derived. Awaiting
owner confirmation.

## RESOLUTIONS — 2026-08-31 (owner: "ok I approve the stamp law. seat F-001 through F-003")

**STAMP LAW APPROVED (standing):** an amended stamped unit keeps its stamp,
records that the stamp predates the new rev, and joins REAFFIRM_QUEUE.md for
the owner's batch word.

**F-001 · SEATED** — claim G18-10 + WITNESS_READ beside the rescue-law
operator; gen_18 rev 4; the first verdict to enter the corpus through the
Step 9 door. Gates green, ritual green.

**F-002 · SEATED** — claim G32-22 + WITNESS_READ beside the ten-years
operator; gen_32 rev 4. Gates green, ritual green.

**F-003 · SEATED, WITH A CORRECTION TO THE FINDING ITSELF** — the dissent
was NOT absent: it has been held in gen_06's BLESS operator prose since the
2026-08-23 law-table amendment. The exam's holdings-search reads claims and
witness rows, not operator prose — a blind spot now on record (see F-006).
Seated at the audit layer: claim G06-12 records the dual, the operator now
carries the tag; no operator added; gen_06 rev 4. Gates green, ritual green.

**F-006 · OPEN (new, from the F-003 seat)** — the exam's holdings-search
has a third stratum it does not read: operator prose. Any future Class-C
verdict must be checked against operator text before being called unheld.
Fix belongs in the exam tooling (World/step9), not the corpus.

World state after the batch: standing 907 -> 909 (exactly the two new
operators), hash 8b8fff1fa28953af unmoved, rituals green on all three units.

## RULING — 2026-08-31 (owner: "ok import only for F-005. recent changes good.")

**F-005 · IMPORT-ONLY (owner's word).** The gehinom duration stays the
engine's labeled guest — quoted from Mishnah Eduyot 2:10 with its dispute,
nothing seated, Genesis untouched. Re-openable if Isaiah is ever derived
(its proof text is Isaiah 66:23). Takes effect inside the engine when
F-004 compiles the judgment_durations module.

## RESOLUTIONS — 2026-08-31 evening (owner: "build F-004 and F-006")

**F-004 · CLOSED — the first end-to-end derived verdict.** The
judgment_durations module is compiled, and the flood's twelve months is now
COMPUTED, not looked up: the engine reads the machine's own date rows —
standing seq 499 (Gen 7:11, year 600 month 2 day 17), standing seq 577
(Gen 8:13, year 601), fact seq 583 (Gen 8:14, month 2 day 27) — and derives
12 months + 10 days, naming all three rows in the verdict. The gehinom
member answers as the labeled import-only guest per the F-005 ruling. All
ten pilot cases now answered by compiled modules, 0 mismatches.

**F-006 · CLOSED — the exam sees all three strata.** World/step9/holdings.py
searches claims manifests, witness rows, AND operator prose (5,779 blocks,
YAML-walked); run_exam.py now prints the three-strata check for every case
once classed C or partial. Proof against the original blind spot: "ben
beroka" lands on gen_06's BLESS operator. And the check's own output is the
loop closing in miniature: the three seated findings show HELD across
strata; gehinom shows "held nowhere — verified in all three strata," the
honest guest it was ruled to be. THE QUEUE STANDS EMPTY of open corpus
findings.

## From the Genesis sweep, 2026-08-31 (owner: "I want to run all of the
## remaining Mishnah Talmud references for gen" → "Go" → "Finish";
## World/step9/cases_gen_sweep.yaml + GEN_SWEEP_LEDGER.md)

**F-007 · OPEN — the seas-as-mikveh dispute is unseated.** Mishnah Mikvaot
5:4 (verbatim = Mishnah Parah 8:8) hangs a three-way tannaitic dispute on
our Gen 1:10 naming operator — וּלְמִקְוֵה הַמַּיִם קָרָא יַמִּים ('and the
GATHERING of the waters He called SEAS'): R. Meir (all seas are as a
mikveh, from our verse), R. Yehudah (the Great Sea only), R. Yosei (seas
purify as flowing, invalid for zavim/metzoraim/purification-waters).
gen_03_double_build holds the naming as its NAME operator; no claim holds
the law. Seat candidate: claim + WITNESS_READ on gen_03's NAME op.

**F-008 · OPEN — the forgiveness law is unseated.** Mishnah Bava Kamma 8:7
derives BOTH legs from our Genesis 20 ink: payment does not atone until
forgiveness is sought (וְעַתָּה הָשֵׁב אֵשֶׁת — 'now restore the man's wife...
and he will pray for you', Gen 20:7), and the wronged must not be cruel
(וַיִּתְפַּלֵּל אַבְרָהָם — 'and Abraham prayed... and God healed Abimelech',
Gen 20:17). gen_36_gerar_dream_prophet holds both events as operator prose
(THE_PROPHET_AND_THE_RETURN_COMMAND, THE_PRAYER_AND_THE_HEALING); the LAW
read off them is unheld. Seat candidate: one claim on gen_36.

**F-009 · OPEN — the thirteen-covenants count, VERIFIED against our ink,
is unseated.** Mishnah Nedarim 3:11, R. Yishmael: גְּדוֹלָה מִילָה שֶׁנִּכְרְתוּ
עָלֶיהָ שְׁלֹשׁ עֶשְׂרֵה בְרִיתוֹת ('great is circumcision — THIRTEEN covenants
were cut over it'). Machine census of Genesis 17's ink: exactly 13
covenant-word tokens (vv. 2, 4, 7×2, 9, 10, 11, 13×2, 14, 19×2, 21). A
numeric ink claim of the class that is never credited unopened — and it
was opened, and it holds. The engine computes it live (_covenant_count).
Seat candidate: claim on gen_33_shaddai_covenant_flesh.

**F-010 · OPEN — two of the three Genesis members of the world-to-come
census are unseated.** Mishnah Sanhedrin 10:3: the FLOOD member is already
held whole (G15-10 — no share AND no judgment, from לֹא יָדוֹן, four
tannaitic parses). The DISPERSION member (the scattering doubled — this
world and the next, on our Gen 11:8-9) and the SODOM member (רָעִים this
world, וְחַטָּאִים the next, on our Gen 13:13 — with R. Nechemiah's dispute
over standing in judgment) are unheld: gen_25_babel holds the scattering,
gen_29_separation_promise holds the verse as THE_SODOM_VERDICT, neither
holds the eschatological ruling. Seat candidates: one claim each.

**F-011 · OPEN — the Sinai-provenance dispute on the sinew is unseated.**
Mishnah Chullin 7:6: R. Yehudah — the sinew was forbidden from the sons of
Jacob, while impure animals were still permitted them; the sages —
בְּסִינַי נֶאֱמַר אֶלָּא שֶׁנִּכְתַּב בִּמְקוֹמוֹ ('it was said at SINAI, but written
in its place'). A dispute about WHEN Genesis's one narrator-voice food law
(our Gen 32:33) took effect — the machine's own provenance-dispute
pattern, and gen_55_two_camps_wrestled_name (G55-31 holds the scope
dispute and the self-stringency) does not hold this one. Seat candidate:
claim + WITNESS_STATE beside G55-31.

## RESOLUTIONS — 2026-08-31 (owner: "Yes update", after the Genesis sweep)

**F-007 · SEATED, THE F-003 PATTERN AGAIN.** The three-way seas-as-mikveh
dispute had been held in gen_03's NAME operator PROSE since the 2026-08-23
amendment — the sweep's holdings check read the claim stratum and called
it unheld. Seat is claim-visibility only: claim G03-12 + inline tag in
the existing prose, the Parah 8:8 verbatim dup credited in the cites. No
new operator. gen_03 rev 4.

**F-008 · SEATED.** Claim G36-18 + one WITNESS_READ beside the
heal-event operator: payment insufficient until forgiveness is asked
(Gen 20:7's restore-command), the forgiver must not be cruel (Gen 20:17's
prayer). gen_36 rev 4.

**F-009 · SEATED, MACHINE-CHECKED.** Claim G33-30 + one WITNESS_READ
beside G33-29's wholeness op (same Mishnah row): thirteen covenants over
circumcision = exactly 13 covenant-word tokens in Genesis 17's own ink,
verified at the sweep and computed live by the Step 9 engine. gen_33
rev 4.

**F-010 · SEATED, WITH A CORRECTION TO THE FINDING ITSELF.** The Sodom
no-share leg was WRONG — claim G29-23 held it all along (the sweep's
probe grepped case-sensitively for 'world to come' and the op writes
'WORLD TO COME': the unfalsifiable-zero lesson repeating at the probe
level). What was truly unheld: the DISPERSION verdict (seated as G25-16
on gen_25's doubled scatter-tokens, rev 4) and the Sodom
stands-in-judgment DISPUTE (seated as G29-25 beside G29-23, rev 4 — first
opinion vs R. Nechemiah vs the sages' rejoinder).

**F-011 · SEATED.** Claim G55-35 + one WITNESS_STATE beside G55-31's op:
R. Yehudah (forbidden from the sons of Jacob, reaching impure species)
against the sages ('said at Sinai, but written in its place') — the
effective-date dispute on the corpus's first narrator-law. gen_55 rev 5.

GATES: all six rituals green (the cite gate first refused the new Mishnah
cites — resolved by the sweep's reading ledger landing in
logic/oral_triage/gen_sweep_mishnah_2026-08-31.md, the honest record that
all 48 rows were read today); preflight ALL SCENARIOS GREEN on all six;
renderings regenerated by the rituals; world refolded, hash
8b8fff1fa28953af UNMOVED; gloss_lint 0 flags; both exams re-run green
(28/28, 0 mismatches) with every engine UNHELD marker now flipped to its
seated claim. Six units joined the re-affirmation queue. THE QUEUE STANDS
EMPTY of open corpus findings.
