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
Jubilee, humiliation, and damage-as-money cells. EXEMPLAR (c)
EXECUTED 2026-09-05: the callee compiled — cold_run_lev24.py,
23/23 at 70% pure ink, exporting talion() — and the Exodus
runner's damage cell now resolves through the LIVE IMPORT
(cold_run_mishpatim.py calls cold_run_lev24.talion()): the first
inter-span function call of the compiled Bible. The censuses
re-confirmed and extended: fracture-under-fracture is UNIQUE to
Leviticus 24:20 — the callee extends the caller's tariff.
EXEMPLAR (a) RUN FROM THE OTHER END (2026-09-05, the Behar-
Bechukotai compile): cold_run_yovel.py — THE JUBILEE ENGINE — states
the Hebrew slave's exits from Lev 25's own ink (the Jubilee, with his
children; the deduction of money by hireling-days) and takes the
SIX-YEAR exit as an IMPORT from Exodus 21:2's term clock, labeled
M-07, for the one sold to an Israelite only; for the one sold to a
gentile the Sifra denies it ("from the year of his sale until the
Jubilee" — Behar, Chapter 8 4). Mishnah Kiddushin 1:2's three exits
(years, Jubilee, money) thus grade against two spans joined by one
edge — the same wiring exemplar (a) recorded from the Exodus side,
now closed from the Leviticus side.
EXEMPLARS FROM THE SEVENTH-YEAR SUPPLEMENT (2026-09-05, round 47):
(e) THE FOREIGNER'S INTEREST — Lev 25:36-37 bars the bite and the
increase toward "your brother" and says nothing of anyone else; the
scope's other half is fetched from Deuteronomy 23:21, "to the
foreigner you may lend at interest, and to your brother you shall
not" — Mishnah Bava Metzia 5:6's iron sheep accepted from gentiles
(cold_run_yovel.py, interest_scope). (f) THE CREATION-SABBATH ANALOGY
— the pre-year addition's ABOLITION by Rabban Gamliel's court is
warranted from Genesis 2's Sabbath by a verbal analogy
"sabbath"-"sabbath": as that day is forbidden itself and free before
and after, so the land's (Babylonian Talmud Moed Katan 4a:7); the
Sifra's thirty days (Behar Chapter 1 1) thereby keyed to the standing
Temple (4a:9); claim LV25A-19. And a form worth naming beside the
import, not as a move: THE RUN LOG AS ANSWER SHEET — Lev 26:34-35's
sabbath-debt clause is QUOTED by 2 Chronicles 36:21 at the timer's
discharge, and the seventy-year timer is run three times in the
Babylonian Talmud (Megillah 11b-12a) from three recorded epochs with
two logged failures — the tradition's second recorded EXPERIMENT on
the record after the spit materials of round 16 (claim LV26-30;
cold_run_tochacha.py).

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

## M-13 — THE CLAUSE-POSITION READ (where an operand sits in the procedure decides what it binds)
The teacher resolves a restrictive token's SCOPE by which service
clause carries it: the sin-offering and the Pesach carry their
"it" (הוא) AT THE SLAUGHTER clause — wrong intent at the slaughter
unfits them; the guilt-offering's "it" sits AFTER THE SMOKING of
the devoted portions, and since even unsmoked portions leave it
kasher, the token cannot be an intent-gate at all — it is re-bound
to the exchange rule ("IT is sacrificed, its exchange is not").
Sifra, Tzav, Section 5 8, answering R. Eliezer's analogy; the
Mishnah's table rides it (Zevachim 1:1 — all fit except Pesach and
chatat, R. Eliezer's asham dissent preserved beside it). Distinct
from M-11: there the WORD order inside a clause is the condition
order; here the CLAUSE's position among the procedure's stations
assigns the operand its object. Found 2026-09-03, the Tzav sweep +
cold compile (cold_run_tzav.py F4's neighbor argument; the exam's
wrong_intent_tzav module).
**Middah correspondence:** the context family again (a thing
understood from its place) — position in the RITE as the context.

## M-14 — THE DOUBLING ARITHMETIC (repetition counts as increase/decrease operators)
The teacher reads REPEATED tokens as arithmetic on a quantity:
R. Akiva's rule at the thanksgiving's oil — the second "with oil"
is an increase after an increase, WHICH DENOTES DECREASE (the log
drops to half); the third mention, an increase after a decrease,
INCREASES again (the soaked kind takes its own quarter). Sifra,
Tzav, Chapter 11 4-6. The output constant lands exactly where R.
Elazar b. Azaryah's recorded dissent puts it by the OTHER channel —
"a halachah to Moses on Sinai": the same half-log, derived vs
transmitted, the two-channel doctrine arguing over one number in
one row. Found 2026-09-03, the Tzav sweep (the exam's todah oil
rows ride it via Menachot 7:1's twenty-tenths table).
**Middah correspondence:** ribbui achar ribbui (inclusion after
inclusion restricts) — the tradition's own named operator, here
running as arithmetic on a measure.

## M-15 — THE VOICE READ (the verb's grammatical voice widens or narrows the ban)
The teacher reads the PASSIVE form itself as a scope operator:
Chizkiya at the leaven ban — לֹא יֵאָכֵל ("it shall not be EATEN,"
Exodus 13:3, the passive) means there shall be NO PERMITTED
CONSUMPTION of it at all, benefit included, since benefit converts
to food money; had the Torah written the active ("you shall not
eat"), only eating would be banned. Pesachim 21b:5 — the Gemara's
own precision note makes the grammar the whole argument. The rival
rule is R. Abbahu's (every eat-ban bans benefit regardless of
voice, unless the verse releases it as at the carcass), and the
routes divide by the carcass baraita's tannaitic split (R. Meir /
R. Yehuda, Pesachim 21b:7-11) — so the move's yield is live only
where the voice is the operative token, and the tradition itself
records both readings. Found 2026-09-04, the leaven block (round
12, the first Exodus Talmud-first exam block; the machine's own
derivation prose at exo_13's step 13:3 had already flagged "the
leaven-ban restated in the passive" before the sugya was opened —
the ink's grammar layer anticipating the compile move).
**Middah correspondence:** the dictionary family (M-09's neighbor)
— but the entry here is a FORM, not a word: the binyan (verb
pattern) carries the law.

## M-16 — THE REVOCALIZATION READ (the consonants held, the vowels re-pointed, and the second reading is law)
The teacher reads the SAME consonantal skeleton under a different
pointing and derives law from the second reading, keeping the first:
al RIV ("in a cause") heard as al RAV ("over the master") — the king
off the bench and capital opinions opening from the side (Sanhedrin
18b:9, 36a:14); lo TISSA ("you shall not bear") read lo TASSI ("you
shall not deliver") — one verse addressing judge AND litigant
(Sanhedrin 7b:15); lo TINAF ("you shall not commit adultery") read
lo TANIF ("you shall not CAUSE adultery") — the accessory read in
(Shimon ben Tarfon, Shevuot 47b:4); and יְעָדָהּ ("designate her")
read as inform-her — the maidservant's consent in the word's own
letters (Abaye son of R. Abbahu, Kiddushin 19a:8). Four exemplars
found in one sitting (2026-09-04, the courts / persons / oaths
blocks). FIFTH EXEMPLAR at the campaign's finale (2026-09-04,
round 29, the Decalogue block): לא תעשון אתי ("you shall not make
WITH ME," Exod 20:23) read לא תעשון אותי ("you shall not make
ME") — the human-face ban derived from the image clause's own
consonants (Rav Huna son of Rav Idi from Abaye's lecture, Rosh
Hashanah 24b:4): the move lands on the Decalogue itself. The move's own meta-question is RECORDED IN THE TRADITION:
the vocalization-authority dispute at Sanhedrin 4a:15 — is the read
text or the received consonants authoritative — block 15's docket;
the front end's vowel measurement answered the machine's side of
that question. Distinct from M-15 (the voice read): there the
grammatical FORM as written carries the law; here a SECOND pointing
of the same skeleton is added to the first.
SIXTH AND SEVENTH EXEMPLARS (2026-09-05, the Acharei Mot-Kedoshim sweep) — and the move's first seats in the SIFRA ITSELF: the male-lying warning for the passive read by R. Akiva from the ban verb re-pointed in the passive voice (Sifra, Kedoshim, Chapter 10 11), and the beast clause's passive warning the same way (שכבתך re-heard — Sifra, Kedoshim, Chapter 11 2): the move now attested in the tannaitic midrash layer, not only the Babylonian Talmud.
**Middah correspondence:** the al-tikrei family ("do not read X but
Y") — the tradition's own name for the operation.


**Exemplar 8 (2026-09-05, the Emor sweep — a CONSONANT-FRAGMENT
cousin, logged here with its difference named):** the castration ban
"in your land you shall not do" (Lev 22:24) — ben Chakinai reads
וּבְאַרְצְכֶם ("and in your land") as וּבָכֶם ("and in YOU"): the ban
extended to HUMANS by re-hearing the token with its middle letters
dropped (Sifra, Emor, Chapter 7 11; claim LV22B-05). Not a
re-pointing of held consonants but a re-cutting of them — the
same family (the sound of the token re-heard as a second law), one
step further from the ink; a third such consonant-fragment exemplar
would register its own move.

## M-17 — THE TENSION RESOLUTION (two tokens in one clause pull opposite ways; the law is the geometry satisfying both)
Registered 2026-09-04 (the Lev 1-8 offering-engine consolidation,
cold_run_offerings.py). Exemplar: Lev 1:5 writes both וזרקו ("and
they shall THROW" — a discrete cast) and סביב ("AROUND" — a full
circuit) of the same blood. The recorded compile (Zevachim 53b:5):
one throw? — the verse says AROUND; a thread-circuit? — the verse
says THROW. The law is the construction satisfying BOTH
constraints at once: the corner hit shaped like a gamma, TWO
applications that are FOUR — each corner feeding two sides, four
sides from two casts. The same page carries the recorded
alternative route (53b:6, R. Yishmael's verbal analogy to the
installation's own סביב at Lev 8:15 — inside the derived span),
so the move stands beside a named second derivation, both kept.
Distinct from M-14 (doubling arithmetic): there repetition is an
operator; here two DIFFERENT tokens constrain one act. Distinct
from the middah of two contradicting VERSES resolved by a third
(I13): the tension lives inside ONE clause and resolves by
construction, not by a third verse.
**Middah correspondence:** the two-verses middah's in-clause
little sibling; the tradition's own form is the talmud-lomar
pincer ("could you say X? the verse says A; then Y? the verse
says B; how then? ...").


## M-18 — THE FREED-TOKEN REASSIGNMENT (a clause not needed for its own matter is GIVEN to a neighboring gap)
The teacher finds a clause REDUNDANT where it stands — its own
matter already taught — and instead of discarding it, REASSIGNS it
to the nearest untaught gap: the tradition's own formula is אם אינו
ענין... תנהו ענין ("if it does not bear on its own matter, give it
to the matter of...").
**Exemplars:** THREE IN ONE SITTING (2026-09-05, the Acharei
Mot-Kedoshim sweep): (1) the third-day eating clause, redundant for
wrong-TIME, given to wrong-PLACE (Sifra, Kedoshim, Chapter 1 4);
(2) the freed token closing the three-source common-denominator
argument — "'judge' is not needed for itself — GIVE IT to the
father's curse" (Sifra, Kedoshim, Chapter 10 7); (3) Exodus 22:18's
whoever-lies-with-a-beast clause, not needed for the ACTIVE (taught
at Lev 20), given to the PASSIVE (Sifra, Kedoshim, Chapter 11 2).
PRECEDENT on the walk: round 19's EXPORT OPERATOR (Exod 13:5's
freed restrictor tokens reassigned to their recorded jobs) ran the
same shape at chapter scale before the form had a name.

**Exemplars 4-5 (2026-09-05, the Emor sweep — the operator recurring
in the very next parashah):** (4) "on that day it shall be eaten"
(Lev 22:29) — redundant for EATING (Lev 7:15 already teaches it) —
"if it does not bear on eating, GIVE IT to slaughter": the slaughter
itself must be on condition of one-day eating, extended to every
one-day offering (Sifra, Emor, Chapter 9 1-2; claim LV22B-09);
(5) Numbers 28:26's "a new grain offering" — not needed for the
WHEAT offering (Lev 23:16 has it) — "GIVE IT to the BARLEY offering"
(Sifra, Emor, Chapter 12 9; claim LV23A-10): the omer's barley
minchah made "new" by a freed clause from another book — the
reassignment crossing the span boundary, M-07's import walked as
M-18's push.
**Exemplars 6-7 (2026-09-05, the Behar-Bechukotai sweep — the
operator's third consecutive parashah):** (6) "if his hand has not
found" (Lev 25:28) — not needed for the field's OWNER, whose
redemption was already taught — "GIVE IT to the REDEEMER, that he
redeem by this same order" (Sifra, Behar, Chapter 5 5; claim
LV25B-06): the kinsman-redeemer's constraints (no borrowing, no
halves) supplied by a freed clause; (7) the doublets of Lev 26:31-32
— "your cities a waste" not needed for the people ("I will desolate
the land" says that) — given to the PASSERS-BY; "your sanctuaries
desolate" not needed for the offerings ("I will not smell" says
that) — given to the PILGRIM BANDS (Sifra, Bechukotai, Section 1 4;
claim LV26-20's neighbor row): the reassignment as object-partition
across a doublet.
**Distinct from** M-07 (the import edge): there a clause is FETCHED
from another span to fill a local gap; here a LOCAL surplus clause
is PUSHED to the gap. The two are the same graph edge walked in
opposite directions.
**Middah correspondence:** im eino inyan — the tradition's own
name; a governed special case of "a matter learned from its
context," running on redundancy rather than adjacency.

## M-19 — THE TEMPLATE BROADCAST (one kind's clause is carried across every kind of the class)
The teacher finds a clause written on ONE member of a class — one
kind of meal offering, one species of burnt offering — and reads it
as the class's template: the tradition's own formula is לִתֵּן אֶת
הָאָמוּר כָּאן בְּכָל הַמְּנָחוֹת וְאֶת הָאָמוּר בְּכָל הַמְּנָחוֹת כָּאן ("to
give what is said HERE to all the meal offerings, and what is said
of all the meal offerings HERE" — Sifra, Vayikra Dibbura DeNedavah,
Chapter 10 1, the row-grain address). The ink states the rule once
and the compiler broadcasts it; the fraction stays honest because the
broadcast cell is labeled MOVE and the source cell INK.
**Exemplars:** (1) THE NORTH FOR EVERY OLAH — Lev 1:11 states "northward"
for the flock alone; the Sifra generalizes it to the herd by the
include-then-exclude sort — "the north obtains in every burnt
offering" (Nedavah Chapter 7 6-7): sitting A's olah row graded twice,
flock INK, herd MOVE (cold_run_offerings.py, 2026-09-05). (2) THE
ADJUNCTS AND THE BREAKING ACROSS THE FIVE KINDS — frankincense is
written at 2:1 (the fine flour) and 2:15 (the first fruits) only;
breaking at 2:6 (the griddle) only; the three oil forms one per kind
(pour 2:1/2:6, mix 2:4-5, made-in-oil 2:7): the Sifra's Chapter 10 1
carries each across all five, and Mishnah Menachot 5:3, 6:3, 6:4
("ALL the meal offerings made in a vessel require...") are the
broadcast's output (cold_run_minchah.py, sitting B, 2026-09-05).
(3) THE SALT ON EVERY OFFERING — written at the meal offering (2:13)
with its own broadcast clause in the ink, "on ALL your offerings":
the bird burnt offering is "rubbed with salt" at Zevachim 6:5 — the
one case where the broadcast is the verse's own word, so the cell is
INK (the same runner).
**Middah correspondence:** binyan av — "a father built from one
verse" (the third of R. Yishmael's thirteen) — run as a class
operation rather than an analogy: the clause is not argued across,
it is declared the class's own. The Sifra's formula is the
declaration.
