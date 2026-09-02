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

## From the Noahide exam block, 2026-09-01 (World/step9/cases_noahide.yaml;
## owner: "open the noahide block")

**F-012 · OPEN — the token-assignment dispute on Gen 2:16 is one-track.**
Claim G08-28 (gen_08_toledot_garden_first_rule) carries ONE assignment of
the disputed token pair — ויצו ("and He commanded") = idolatry, אלהים
("God") = courts — its Bereshit Rabbah 16:6 source's side, which is R.
Yitzchak's inversion (Babylonian Talmud Sanhedrin 56b:8). The Talmud's
mainline (56b:5-6) assigns the pair the OTHER way: ויצו = courts (via Gen
18:19 "he will command his children"), אלהים = idolatry. A recorded
dispute half-held is against the dual-track law (the F-003 shape).
Candidate seat: amend G08-28 (or a beside-claim) to carry both
assignments labeled. Sources: Sanhedrin 56b:5-6 (triage, read), 56b:8
(read today, noahide_exam_reading_2026-09-01.md).

**F-013 · OPEN — three procedure legs of Gen 9:5-6 are unseated.** Claim
G21-11 (gen_21_blessing_blood_law) holds the murder procedure word by
word (one judge, one witness, no forewarning, agent, fetus, mode) but not
these recorded legs: (a) a woman's TESTIMONY not accepted — מיד איש
("from the hand of a man," Gen 9:5; Sanhedrin 57b:2/4); (b) a RELATIVE's
testimony accepted — אחיו ("his brother," same verse); (c) a woman WHO
KILLS is liable — שופך דם האדם ("WHOEVER sheds," Gen 9:6; Rav Yehudah's
resolution, 57b:9). Candidate seat: extend G21-11 or a beside-claim.
Sources: Sanhedrin 57b:2/57b:4/57b:9 (read today).

**F-014 · OPEN — the gentile-Sabbath law on Gen 8:22 is held nowhere.**
The round's one clean class-C hole: Resh Lakish — a gentile who kept a
full day of rest is liable, from ויום ולילה לא ישבותו ("and day and night
they shall not CEASE," Gen 8:22 read onto them), with Rav Nachman bar
Yitzchak's principle (their prohibition is their death-liability,
Sanhedrin 57a:12) and Ravina's sharpening (even a Monday). gen_20's 8:22
claims hold the termination-condition reading (G20-18) and the Masorah
pair (G20-11), not this law. Candidate seat: gen_20_exit_altar beside
G20-18. Sources: Sanhedrin 58b:25 (triage, read), 57a:12 (read today).

**F-015 · OPEN — the repeated-at-Sinai framework is held nowhere as a
rule, and two circumcision-scope legs are unseated.** R. Yose son of R.
Chanina (Sanhedrin 59a:11): said to the sons of Noach AND repeated at
Sinai — both bound; not repeated — Israel only; the reverse instance is
the sinew (59a:12 — G55-35 holds that instance already). Unheld: the
framework itself, and on gen_33_shaddai_covenant_flesh the two scope
legs — the restriction אתה וזרעך ("YOU and your seed," Gen 17:9, no one
else — 59b:9) and the Keturah inclusion את בריתי הפר ("My covenant he
has broken," Gen 17:14 — R. Yose bar Avin, 59b:12). The Ishmael/Esau
exclusions are already held (G37-25). Candidate seats: the framework as
a beside-claim where the owner rules it lives; the two legs on gen_33.
Sources: Sanhedrin 59a:10-12, 59b:2, 59b:4, 59b:9, 59b:11 (read today);
59b:1/59b:3/59b:12 (triage, read).

**F-016 · OPEN — the maternal-sister ban and our 20:12's deflected-proof
role are unseated.** Sanhedrin 58b:5 presses Gen 20:12 ("my father's
daughter, NOT my mother's") to prove the maternal sister banned to
Noahides; 58b:6 DEFLECTS the proof (she was his brother's daughter —
kinship talk, not sister-law). The law stands on the baraita; our
verse's recorded role is attempted-and-deflected evidence. gen_36 holds
neither. IMPORT-ONLY CANDIDATE (the deflection weakens the Genesis
anchor to a dialectic appearance). Sources: Sanhedrin 58b:5 (triage,
read), 58b:6 (read today).

## RESOLUTIONS — the Noahide seats, 2026-09-01 (owner: "seat f-012
## through f-016")

**⚠ NEW STANDING LAW (owner, same sitting, verbatim): "the findings that
are not yet derived (verse) should automatically be seated. you don't
need my rulings going forward."** From this point the loop's RULE step is
automatic for verse-side unheld legs: a finding whose content is an
unheld or half-held leg on an already-derived unit SEATS by the normal
path (claim + operator + rev bump + gates + ritual) without waiting for a
per-finding word. Everything else about the loop stands: findings are
still FILED first (never fixed mid-exam), resolutions still append here,
the STAMP LAW still routes every amended stamped unit to the
re-affirmation queue for the owner's batch word, and import-only /
reject remain available to him — the default flipped from "wait" to
"seat," the record and the stamps stayed owner-gated.

**F-012 · SEATED.** Claim G08-30 + one WITNESS_READ beside the crown op:
the token-assignment dispute carried both ways (mainline courts/idolatry
vs R. Yitzchak's inversion — the side G08-28's own Bereshit Rabbah
source stood on). gen_08 rev 5.

**F-013 · SEATED.** Claim G21-17 + one WITNESS_READ beside G21-11: the
witness-gender bar, the relative's admission, and the woman-killer's
liability, each on its own word of Gen 9:5-6. gen_21 rev 4.

**F-014 · SEATED.** Claim G20-19 + one WITNESS_READ beside G20-18: the
gentile-rest prohibition on Gen 8:22's clock-clause with the
their-prohibition-is-their-death principle and Ravina's any-full-day
scope. The exam's one clean class-C hole, closed. gen_20 rev 4.

**F-015 · SEATED, TWO UNITS.** Claim G33-31 (gen_33 rev 5): the
line-scope legs — the you-and-your-seed restriction and the Keturah
inclusion, with the partitive cross-reference to G37-25. Claim G55-36
(gen_55 rev 6): the repeated-at-Sinai framework itself, seated where its
named reverse instance lives (the sinew, beside G55-35's provenance
dispute).

**F-016 · SEATED (as a kept record, not a law source).** Claim G36-19 +
one WITNESS_READ in the 20:12 step: the maternal-sister proof attempted
from our verse and deflected — the verse's recorded role carried
honestly as attempted-and-deflected evidence. The import-only
recommendation in the finding was superseded by the owner's blanket
"seat f-012 through f-016". gen_36 rev 5.

## From the Mishpatim exam, 2026-09-01 (owner: "run step 9 on mishpatim";
## AUTO-SEAT ERA — filed and seated the same sitting per the standing law)

**F-017 · FILED + AUTO-SEATED — four exo_22 legs the derivation pass
skipped, all in the morning's own reading.** (a) INTEREST PARTIES: the
five violators (lender, borrower, guarantor, witnesses; the scribe
disputed) — Mekhilta on Exod 22:24, met by Mishnah Bava Metzia 5:11
verbatim. (b) THE SERVICE PARADIGM: zevichah left-the-rule-to-teach —
Temple-style services liable for any idol, its-own-way otherwise
(Mekhilta on Exod 22:19; Mishnah Sanhedrin 7:6 is its case table).
(c) THE CURSE CLAUSES: judge and prince each their own liability, the
four-liabilities utterance, be-amkha (Mekhilta on Exod 22:27; Mishnah
Shevuot 4:13 the case row). (d) SELF-CONVICTION EXCLUDED: אשר ירשיען
אלהים — 'whom the JUDGES convict,' not the self-convicter — the
admission-pays-no-fine rule (Mishnah Ketubot 3:9; Bava Kamma 9:8's
fifth-and-asham branch). Seated as EX22-09 (one claim, one WITNESS_READ
beside EX22-04's court op). exo_22_property_social.

**F-018 · FILED + AUTO-SEATED — three bikkurim legs on exo_23_justice.**
(a) NOT BEFORE SHAVUOT: the Tzevoim-mountain offering refused, quoting
our 23:16 (Mishnah Bikkurim 1:3 + Challah 4:10). (b) RESPONSIBILITY
UNTIL THE TEMPLE MOUNT from 23:19's bring-verb (Mishnah Bikkurim 1:9).
(c) THE GROWER-CLASSES DELTA: the Mekhilta re-includes sharecroppers
and seizers as bring-but-not-read; Mishnah Bikkurim 1:2 excludes them
from bringing at all ('until all growth is from YOUR land') — a
recorded two-seat split on the same clause, carried dual-track. Seated
as EX23-09 (one claim, one WITNESS_READ beside EX23-08's op).
exo_23_justice_calendar.

**F-019 · FILED + AUTO-SEATED — the unnamed-elders court doctrine on
exo_24.** R. Dosa ben Harkinas (Mishnah Rosh Hashanah 2:9): why were
the seventy elders of our 24:9 left UNNAMED? So that every three that
ever stands as a court over Israel is AS THE COURT OF MOSES — the
institutional-authority rule that decides the Rabban Gamliel calendar
case, derived from this unit's silence about names. Seated as EX24-07
(one claim, one WITNESS_READ at the 24:9 step). exo_24_covenant_ascent.

**F-020 · FILED + AUTO-SEATED — the gift-order clauses of Exod 22:28 on
exo_22.** The exam's Terumot rows quote our verse directly: reordered
gifts — the act STANDS though forbidden (מלאתך ודמעך לא תאחר, Mishnah
Terumot 3:6 = the Mekhilta's mah-she-asah-asui row verbatim); and the
ORDER itself derived by the names-count argument (firstfruits first,
four titles; Mishnah Terumot 3:7). Read in the morning's spine, met by
the case shelf the same day, skipped by the derivation pass's eight ops.
Seated as EX22-10 (one claim, one WITNESS_READ at the 22:28 step's
area). exo_22_property_social.

## From the Exodus 1-21 backfill exam, 2026-09-01 (owner: "lets run
## step 9 on exodus 1 - 21 again"; AUTO-SEAT ERA — filed and seated the
## same sitting per the standing law). Ledger:
## logic/oral_triage/exodus_backfill_mishnah_2026-09-01.md.

**F-021 · FILED + AUTO-SEATED — the Passover statute's implementing
rows on exo_12.** Six legs, all bare-Mishnah, all on the chapter's own
ink: (a) SERVICE LAWS — for-its-name required (זבח פסח הוא, 12:27,
Pesachim 5:2), the eater/registration teleology (לפי אכלו 12:4,
Pesachim 5:3 + 7:4), the midday window (בין הערבים 12:6, Pesachim 5:3),
and THE THREE-COHORT INK-CENSUS: assembly-congregation-Israel, three
nouns in 12:6 → three slaughter cohorts (Pesachim 5:5) — with the
agency doctrine's seat on the same verse (all slaughter, one
slaughters — Kiddushin 2:1 via Kiddushin 41b). (b) EATING REGIME —
liquids as cooking (12:9, Pesachim 2:8), the innards dispute (7:1),
the helmeted-kid fence (Beitzah 2:7), midnight window (10:9), the
leftover-lash asymmetry (repaired-by-burn, Makkot 3:3). (c) LEAVEN
BAN implementing rows — THE FRONTIER DEBT AT 12:19: lamplight search
(Pesachim 1:1), the lecha ownership scope (2:2 on 13:7), the measures
dispute (Beitzah 1:1), the eating lash (Makkot 3:2), second-Passover
contrast (9:3). (d) SEDER DUTIES — the Rabban Gamliel trio with its
verse-reasons + five grains (10:5, 2:5). (e) TWO-ERA TABLE — Egypt's
Passover vs the generations', clause by clause (9:5). (f) CALENDAR
COMMISSION — sanctification procedure, the relatives dispute,
no-Nisan-in-Nisan (Rosh Hashanah 3:1 + 1:7, Pesachim 4:9 on 12:1-2);
plus the arel-terumah extension (12:48, Yevamot 8:1). Seated as
EX12-17..EX12-22 with WITNESS_READ ops. exo_12_passover_and_exodus.

**F-022 · FILED + AUTO-SEATED — the firstborn cluster + tefillin form
on exo_13.** (a) FIRSTBORN: the doubled peter-chamor token → both must
be donkeys (Bekhorot 1:2); redemption-precedes-neck-breaking from
13:13's own clause order (1:7); the twin-males dispute on the plural
of 13:12 (2:6); the caesarean womb-opener definition (2:9); the
dual-track priest/inheritance split with the Israel-womb reading of
13:2 (8:1); the any-amount prohibition class (Avodah Zarah 5:9).
(b) TEFILLIN FORM: four compartments the scribal datum (five = liable,
Sanhedrin 11:3), round = danger, forehead/palm = sectarian (Megillah
4:8) — the received form of 13:9+16 beside the EX13-04 crown. Seated
as EX13-14..EX13-15. exo_13_consecration_and_pillars.

**F-023 · FILED + AUTO-SEATED — the manna chapter's three law legs on
exo_16.** The boundary QUANTIFICATION dispute (2000 cubits vs 4,
Eruvin 4:5) + the carrying grid as the labor prototype (Shabbat 1:1)
+ the partial-uprooting example (Horayot 1:3), all on the EX16-10
crown's verse; the challah measure derived from the omer-per-head of
16:16 (Eduyot 1:2); the manna's membership in the canonical
twilight-creation table (Pirkei Avot 5:6 — the table gen_22 already
witnesses at G22-09). Seated as EX16-14..EX16-15 (+ the 20:10 rest-
roster leg noted at exo_20). exo_16_manna_and_sabbath.

**F-024 · FILED + AUTO-SEATED — the court tiers on exo_18 and the
utterances' implementing rows on exo_20.** exo_18: the seventy-one
docket (Sanhedrin 1:5) + capital court composition and side-first
opening (4:2) + the money/capital asymmetry table (4:1) as the
institutional heirs of the 18:22 routing — EX18-14. exo_20: the
plotting-witnesses rows at the ninth utterance (pay-not-lash;
80-vs-40 — Makkot 1:2/1:3) — EX20-14; father-mother equal weight from
the reversed order of Leviticus 19:3 against 20:12 (Keritot 6:9) —
EX20-15; the altar ground-status dispute on 20:21 (Chagigah 3:8), the
one-student Presence warrant on the Name-mention clause (Pirkei Avot
3:6), the Decalogue's daily Temple reading (Tamid 5:1), and the
rest-roster gentile-out reading of 20:10 (Shabbat 24:1) — EX20-16.
exo_18_jethro_and_the_judges + exo_20_the_ten_utterances.

**F-025 · FILED + AUTO-SEATED — two Song-chapter legs on exo_15.** The
performance-mode dispute on the doubled saying-token of 15:1 (R. Akiva
responsive like Hallel / R. Nechemiah together like Shema — Sotah 5:4)
— EX15-14; the healing verse 15:26 fenced from magical use (R. Akiva's
whisperer, Sanhedrin 10:1) — EX15-15. exo_15_the_song_and_marah.

**F-026 · FILED + AUTO-SEATED — the readiness interval on exo_19.**
The three-days preparation of 19:15 read as the standing viability
window of seed for impurity (Shabbat 9:3's מנין question) — EX19-14.
exo_19_sinai_and_the_covenant.

**F-027 · FILED + AUTO-SEATED — the raised-hands doctrine on exo_17.**
Did Moses' hands make war? — instrument, not cause: Israel looking
upward and subjecting their heart (Rosh Hashanah 3:8 on 17:11, with
the Num 21 serpent as its pair), and the law tail — only the obligated
discharge the many — EX17-14. exo_17_massah_and_amalek.

**F-028 · FILED + AUTO-SEATED — the plague census closes on exo_11.**
Ten plagues in Egypt, ten at the Sea (Pirkei Avot 5:4) — the census
closing at our 11:1's ONE MORE plague (the clause presupposes nine);
the frontier's plague-chronology slot paid — EX11-14.
exo_11_one_more_plague.

**F-029 · FILED + AUTO-SEATED — two narrative-as-law legs.** exo_04:
circumcision suspended not even an hour over righteous Moses — the
lodging episode of 4:24-26 as law-evidence (Nedarim 3:11, R. Yehoshua
ben Korcha) — EX04-14. exo_05: the document rule — the ruler written
ABOVE the Name on the page's order, from Pharaoh's own progression
(מי ה' at 5:2 → ה' הצדיק at 9:27; Yadayim 4:8, the Pharisees' retort)
— EX05-14, citing exo_09's confession op. exo_04_signs_and_firstborn +
exo_05_bricks_without_straw.

**F-030 · FILED + AUTO-SEATED — two opening-chapters legs.** exo_01:
the maror reason — the bitter herb eats the verb וימררו of 1:14
(Pesachim 10:5's third clause) — EX01-14. exo_02: the good-measure
table — Miriam's hour at 2:4 repaid seven days (Sotah 1:9; the Moses/
Joseph's-bones leg rides EX13-01's marquee) — EX02-14.
exo_01_names_and_midwives + exo_02_drawn_from_the_water.

**F-031 · FILED + AUTO-SEATED — two new legs on the ordinances unit.**
(a) THE STONED ROOSTER: R. Yehudah ben Bava's testimony that a rooster
was stoned in Jerusalem for killing a person (Eduyot 6:1) — the
ba-hoveh canon (ox = any killer) carried as an EXECUTED PRECEDENT, not
a hypothetical. (b) THE PLOTTING-WITNESS TIMING at our 21:23: both
sides of the Sadducee dispute quote nefesh-tachat-nefesh — killed
after the VERDICT, not after execution (Makkot 1:6). Seated as EX21-14.
exo_21_the_ordinances.

**F-032 · FILED + AUTO-SEATED — the showbread's form-laws on exo_25.**
The dimension table under the recorded cubit-conversion dispute:
Mishnah Menachot 11:5's ten-by-five (R. Yehudah) and twelve-by-six
(R. Meir) are BOTH our 25:23's own two-cubits-by-one under the two
recorded constants (five vs six handbreadths to the cubit) — a
verse-times-constant computation, with the fold geometry, the
wind-gap, and Abba Shaul's frankincense placement (על as ADJACENT,
from Numbers 2:20) riding; and Ben Zoma's form-requirement from
25:30's own name — לחם פנים ("bread of the FACE"), שיהא לו פנים
("it must have faces") (Menachot 11:4, with the loaf/two-loaves
table and R. Yehudah's letter-numeral mnemonic). Seated as EX25-11.
exo_25_ark_table_menorah.

**F-033 · FILED + AUTO-SEATED — the continuity-token's operational
dispute on exo_25.** Mishnah Menachot 11:7 quotes our 25:30 (לפני
תמיד — "before Me continually") as the proof for the simultaneous
exchange (withdrawing and placing hands a handbreadth apart); R. Yose:
even placed later the same day, that too is תמיד ("continually") —
the token's operational meaning is a recorded dispute (strict
simultaneity vs no vacant night). Riding: מעלין בקדש ולא מורידין
("we ascend in holiness and do not descend") — the marble-then-gold
table order as the principle's exhibit; and the rod-arrangement's
Sabbath deference (11:6). Seated as EX25-12. exo_25_ark_table_menorah.

**F-034 · FILED + AUTO-SEATED — the way-of-growth law on exo_26.** The
Talmud (Babylonian Talmud Sukkah 45b) derives from our 26:15's own
token — עצי שטים עמדים ("acacia wood, STANDING") — that mitzvah
objects are taken דרך גדילתן ("the way they grow"): upright as they
stood. The boards' standing-word becomes a general orientation law for
commandment objects (the lulav rows its case neighborhood — Mishnah
Sukkah 3:14's enumeration anchor rides this bridge). Talmud-only
provenance: no Mishnah row states the rule. Seated as EX26-06.
exo_26_curtains_boards.

**F-035 · FILED + AUTO-SEATED — the ash-vessel's second service on
exo_27.** Our 27:3's סירתיו לדשנו ("its pots for its ashes") has a
case-side face: the פסכתר ("psakhter-pot," the large bronze
ash-vessel — Mishnah Tamid 5:5 lists its services) is overturned over
a dead creeping thing found in the sanctuary (Mishnah Eruvin 10:15),
where the removal disputes run: belt vs wooden tongs (impurity must
not linger vs must not spread), and the zones bounded by
cut-off-liability (R. Shimon ben Nannas vs R. Akiva). The altar
vessel running in purity law. Seated as EX27-06. exo_27_altar_court.

**F-036 · FILED + AUTO-SEATED — the oracle's access list on exo_28.**
Mishnah Yoma 7:5: the Urim and Tummim are consulted only IN the eight
garments, and only for three petitioner classes — the KING, the
COURT, and one whom the COMMUNITY needs. The portable judgment organ
of EX28-03 carries an authorization layer: full uniform and a
qualified petitioner, or no query. Seated as EX28-09.
exo_28_priest_garments.

**F-037 · FILED + AUTO-SEATED — fiscal plurality on exo_28.** Mishnah
Shekalim 5:2: no fewer than three treasurers and seven trustees, and
no authority over public money with fewer than TWO officers (the
recorded exceptions majority-accepted) — anchored at our 28:5's own
plural take-verb (ואנון יסבון — "and THEY shall take the gold").
Seated as EX28-10. exo_28_priest_garments.

**F-038 · FILED + AUTO-SEATED — the plate's jurisdiction on exo_28.**
Mishnah Zevachim 8:12's close: הציץ מרצה על הטמא ואינו מרצה על היוצא
("the plate propitiates the IMPURE and does not propitiate the
TAKEN-OUT") — EX28-06's acceptance function scoped: impurity yes,
exit no. Seated as EX28-11. exo_28_priest_garments.

**F-039 · FILED + AUTO-SEATED — the shamir at the stones on exo_28.**
Mishnah Pirkei Avot 5:6's twilight census (held at exo_16's EX16-15)
assigns the SHAMIR — and the Talmud's bridge (Babylonian Talmud Sotah
48b) puts it at THIS chapter's engraving: the stones written
בְּמִלֻּאֹתָם ("in their fullness"), whole and uncut. Seated as
EX28-12. exo_28_priest_garments.

**F-040 · FILED + AUTO-SEATED — the waving's computed motions on
exo_29.** Mishnah Menachot 5:6 quotes our 29:27 as its proof: the
four motions — forward-back (from אשר הונף, "which was WAVED") and
up-down (from אשר הורם, "which was LIFTED") — the procedure computed
from the verse's own two verbs; with the waving census (men and women
alike, Israel not others) and the geography (waving east,
bringing-near west, wavings first). Seated as EX29-13.
exo_29_investiture.

**F-041 · FILED + AUTO-SEATED — the kalbon on exo_30.** Mishnah
Shekalim 1:6: because the verse fixed a HALF-coin, change-making
generates surcharge law — who owes the kalbon, the exempt classes,
the joint-payment dispute (one kalbon or two, R. Meir), two kalbons
for sela-in-shekel-out. The flat rate's transaction friction,
legislated. Seated as EX30-09. exo_30_incense_shekel.

**F-042 · FILED + AUTO-SEATED — the equality invariant on exo_30.**
Mishnah Shekalim 2:4: the denomination FLOATED across the eras
(darkonot → selaim → teva'in → the dinar proposal) and R. Shimon's
answer holds: יד כולן שוה ("ALL HANDS ARE EQUAL") at any coin — the
constant is the equality, not the denomination; against the
sin-offering's by-his-means. The case shelf's own statement of the
conversion-layer Onkelos performs at 30:13 (shekel rendered sela).
Seated as EX30-10. exo_30_incense_shekel.

**F-043 · FILED + AUTO-SEATED — the liability-aggregation algebra on
exo_31.** Mishnah Shabbat 7:1's GREAT PRINCIPLE: liability groups by
knowledge-state — forgot the PRINCIPLE, one offering for everything;
forgot the DAYS, one per Sabbath; forgot the LABORS, one per
labor-category; many of one kind, one. Hung from the very
juxtaposition EX31-03 seats at 31:13. Seated as EX31-05.
exo_31_craftsmen_shabbat.

**F-044 · FILED + AUTO-SEATED — the precedence table on exo_34.**
Mishnah Bekhorot 1:7: redemption PRECEDES neck-breaking; designation
precedes redemption — quoting our own Exod 21:8; yibbum formerly
preceded chalitzah and the order FLIPPED when intention decayed; the
owner precedes all in redemption. A cross-domain duty-ordering
algebra with a recorded historical flip. Seated as EX34-07.
exo_34_second_tablets.
