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
EXEMPLARS FROM THE DEPENDENCY-DEBT SITTING (2026-09-06 — the audit
that found the ink's own cross-references standing as notes or
silence, and the repair): (g) THE POINTER NAMES THE SPECIES — Lev
4:35 "as the fat of the LAMB is removed from the peace offering"
imports Lev 3:9-10's inventory, tail included, while 4:10's "as it is
lifted from the OX" imports 3:3-4's, no tail: the fat-tail token
stands at two seats of Leviticus 1-8 (3:9, 7:3), so the pointer's
own species word decides the list (cold_run_chatat.fat, by call into
cold_run_offerings.dispatch('fat:lamb')). (h) Lev 5:10's "as
prescribed" imports the bird burnt offering's rite (Lev 1:14-17;
cold_run_vayikra5.pointers into cold_run_minchah.bird) and 5:13's
"as the meal offering" imports Lev 2's remainder rule. (i) Exod
23:15's "as I commanded you" imports Exod 12-13's matzah window
(cold_run_calendar.matzah into cold_run_pesach). (j) Lev 14:13's "as
the sin offering, so the guilt offering" imports the guilt offering's
law of 7:1-7 (cold_run_metzora into cold_run_tzav.asham_law —
compiled the same sitting; the north through the offerings row).
(k) Lev 10:15's "as the LORD commanded" imports 7:30-34's breast and
thigh (cold_run_chatat.table into cold_run_tzav.dues_machine). (l)
ONE FUNCTION AT TWO SEATS — the seventh year (Exod 23:10-11 calls Lev
25:1-7's), the first fruits (Lev 23:17-20 calls Exod 23:16-19's), the
omer (Lev 23:9-14 calls Lev 2:14's), the fast (Lev 16:29-31 calls Lev
23:27-32's): an institution written twice is compiled once and called
from both seats. And the move became a GATE: World/step9/
dependency_census.py requires every cross-reference the ink makes to
carry a disposition (CALL verified live, OWED, REVERSE, VIA,
PARAMETER, INTERNAL, RUN_CITATION, FALSE) before a span is called
compiled — recorded in THE_STEPS Step 5, motion (1).
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
EIGHTH EXEMPLAR (2026-09-06, sitting L5 of the compile debt, cold_run_priesthood.py — the Emor spine's own seat): the castration ban's reach to HUMANS read by ben Chakinai from וּבְאַרְצְכֶם ("and in your LAND," Lev 22:24) re-heard as וּבָכֶם ("and in YOU") — Sifra, Emor, Chapter 7 11; the same clause's "you shall not DO" already widening the ban past offering to the act itself, and the human's crushed testicle then defined by the beast's verse (Mishnah Yevamot 8:2, "even one of them"). The compiled cell carries the revocalization as one arm beside the plain reading.
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

## M-20 — THE WARNING COMPLETION (a punishment written in one place is armed by a warning written in another)
The teacher holds the tradition's own rule that no penalty runs
without a written WARNING (אַזְהָרָה, the warning clause) beside its
written punishment — עֹנֶשׁ (the penalty clause) — and when a clause carries the one and
not the other, it goes looking across the books for its twin, and
pairs them: the compile's cross-book edge stated as a requirement,
not a convenience. The tradition's own formula is עֹנֶשׁ שָׁמַעְנוּ,
אַזְהָרָה מִנַּיִן ("the punishment we have heard — the warning, from
where?").
**Exemplars (registered 2026-09-06 at sitting L4a of the compile
debt, from seats already on the record):** (1) Leviticus 19:11 "you
shall not steal" — supplied as the WARNING for Exodus 22:3's double
payment, whose clause writes the penalty alone (Sifra, Kedoshim,
Section 2 1: the row's whole job); (2) 19:11's "you shall not deny,
you shall not lie" and 19:12's "you shall not swear by My name
falsely" — the warnings for Leviticus 5:21-24's fifth and guilt ram
(Section 2 3); the cold compile fetched those punishments by live
call into the Lev 5 engine while this chapter supplied the arming
clause (claim LV19L-03); (3) the ghost-pit's three-verse completion
— punishment at 20:27, warning at 19:31, karet at 20:6 — assembled
by Sifra, Kedoshim, Chapter 10 1 (sitting L3, claim LV20-09); (4) the
warning for offering outside found at Deuteronomy 12:13 "guard
yourself lest you offer" for Leviticus 17:8-9's penalty (Sifra,
Acharei Mot, Chapter 9 3); (5) the sister-clause pair of Kedoshim
Chapter 11 10 and 11 12 — "no punishing from inference" AND "no
warning from inference": both halves must be WRITTEN, which is why
the search is a search and not a derivation; (6) (sitting L4b,
2026-09-06) Leviticus 19:26 "you shall not eat OVER the blood" —
the fifth of the Sifra's five laws on the one clause is the WARNING
for the wayward son's gluttony, whose penalty stands at Deuteronomy
21:21 (Sifra, Kedoshim, Chapter 6 1, R. Yosei son of R. Chanina);
and the ghost-pit triple of exemplar (3) now runs as a live call —
the second-half runner holds the warning and fetches the bearer's
stoning from the sanctions engine (cold_run_holiness_b.py).
**Distinct from** M-07 (the import edge — a clause fetched to fill a
local gap of CONTENT) and M-18 (a surplus clause pushed to a
neighboring gap): here the fetched clause fills a gap of FORM — the
penalty exists and is complete, but may not run until its warning is
located. **Machine form:** a compiled sanction cell carries two
addresses, (warning verse, punishment verse); the matrix of sitting
L3 (cold_run_sanctions.py) already stores them as a pair, and this
sitting's warning() cells return the pair explicitly.
**Middah correspondence:** not one of the thirteen — a governance
rule over the whole set (the fence of Chapter 11 10/12 forbids
deriving either half), sitting beside the parse-direction and
adjacency meta-rules in logic/MIDDOT.md's case law.


## M-21 — THE INTERSECTION SOLVE (two bans on one act, each too wide alone; the liable act is their intersection)
Registered 2026-09-06 (sitting L4b of the compile debt,
cold_run_holiness_b.py) from two exemplars in one chapter. The
teacher holds two written prohibitions that fall on the same act
from different sides, each of which read alone would reach too
far, and defines the LIABLE act as the region both cover — the
tradition's own pincer, run across two verses instead of inside
one clause. Exemplar (1), THE RAZOR: Leviticus 19:27 "you shall not
DESTROY the corner of your beard" (could be even with scissors?)
and Leviticus 21:5 "they shall not SHAVE the corner of their
beard" (could be even with tweezers or a plane?) — Sifra, Kedoshim,
Chapter 6 4 intersects them: scissors-like-a-razor is shaving
without destruction, tweezers and the plane are destruction without
shaving, and the act that is BOTH shaving and destruction is the
razor — Mishnah Makkot 3:5 "not liable unless he takes it with a
razor" (R. Eliezer's dissent kept beside it, 6 6). The second
constraint lives in the priests' law — COMPILED AT ITS HOME at
sitting L5 (2026-09-06, cold_run_priesthood.py): the priests' cell
for 21:5 "they shall not SHAVE" now fetches the solve by LIVE CALL
from the holiness engine's razor cell, the corners and the gash
multipliers with it, and the dependency gate carries the edge
(priesthood -> holiness_b, CALL, verdict) — the intersection's two
verses are two runners, joined by an import edge in the direction
the ink reads (the priests' verse calls the people's). Exemplar (2), THE TATTOO:
Leviticus 19:28 "an inscribed tattoo" — one noun-phrase, two verbs;
"wrote and did not engrave, engraved and did not write — not liable
until he writes AND engraves" (Chapter 6 10; Mishnah Makkot 3:6),
which Onkelos renders as the two-word noun "engraved markings".
**Distinct from** M-17 (the tension resolution): there two tokens in
ONE clause pull opposite ways and the law is a construction that
satisfies both (the corner hit that is both a throw and a circuit);
here two BANS, each complete in itself, are laid over one act and
the liable region is their overlap — set intersection, not
geometry. Distinct from M-20 (the warning completion): there the
second verse supplies the missing HALF of a penalty; here both
verses are prohibitions and the pairing NARROWS rather than arms.
**Machine form:** a predicate on the act is the conjunction of the
two verses' predicates (shaving AND destroying; writing AND
engraving); the cold runner's razor cell takes the tool and returns
liable only where both hold, the dissent as a second arm.
**Middah correspondence:** the form is the talmud-lomar pincer
("could you say X? the verse says A; then Y? the verse says B") of
the thirteen's own idiom, applied to two prohibitions; beside it the
sitting's other letter-level move — the acronym rule (E30 of the
thirty-two) reading the one noun "shaatnez" as three conjoined
predicates, carded, spun, woven (Mishnah Kilayim 9:8 = Sifra,
Kedoshim, Chapter 4 18) — which is a conjunction read OUT of one
word rather than built across two verses, and is logged in
logic/MIDDOT.md's case law rather than here.

## M-22 — THE RUN READ BACK INTO THE SPEC (a narrated execution of a law legislates a column the law's own text leaves open)
⚠ A GENERALIZATION (the link review law, LR3, 2026-09-07): this move is
our name for a shape the teachers used at the exemplars below; it is a
TEACHER for a new verse pair ONLY when a recorded exemplar is named
beside the application (`taught_by: M-22, exemplar Menachot 93b:3 ...`).
Applied to a pair no teacher used, it is a HYPOTHESIS (class H), never
a license — a person does not derive a verbal analogy on his own.
Registered 2026-09-06 (sitting D8 of the compile debt,
cold_run_shemini_day.py) from five exemplars in one chapter. The
teacher holds a SPEC (a law paragraph) and a RUN (the narrative of that
law's first execution) and reads a term of the run — a pointer, a
token, a preposition, a sequence — back into the spec as a rule the
spec never wrote. The compile's own direction is the reverse (the run
graded against the spec by live call, the divergences named); this
move is the tradition's, and it is the demonstrate-by-run form of the
24 books (THE_STEPS: Torah by SPEC, the Prophets and Writings by RUN)
turned into a compile step. Exemplar (1), THE POINTER: Leviticus 9:16
"and he brought the burnt offering and did it AS PRESCRIBED (כמשפט)" —
"as the law of the FREEWILL burnt offering: teaches that the
OBLIGATORY burnt offering requires hand-laying" (Menachot 93b:3 =
Beitzah 20a:5, inside Beit Hillel's arm of Mishnah Beitzah 2:4): the
run's pointer into Leviticus 1 gives Leviticus 1 a column (Lev 1:4's
hand-laying extended to a class the chapter does not name). Exemplar
(2), THE TOKEN: 9:17 "and he filled HIS PALM (כפו) from it" — R. Zeira:
'palm', I do not know what it is; Leviticus 14:15 alone writes "the
LEFT palm", hence wherever 'palm' stands unmarked it is the RIGHT
(Menachot 9b:17; Rava's hand-hand analogy beside it, 10a:6) — Mishnah
Menachot 1:2's left-hand fistful invalid by a token of the run; the
meal-offering engine's cell now fetches the derivation from this verse
by call. Exemplar (3), THE PREPOSITION: 9:10 "the lobe FROM (מן) the
liver" resolves Lev 3:4's "the lobe ON (על) the liver" — from the liver
onto the lobe (Sifra, Vayikra Dibbura DeNedavah, Section 14 8).
Exemplar (4), THE SEQUENCE: 9:22 "and Aaron lifted his hands to the
people and blessed them, and came down from doing the sin offering, the
burnt offering, and the peace offerings" — the blessing's posture
(lifted palms, by verbal analogy to Num 6:23, Sotah 38a:6), its timing
(in the service, Sotah 38b:7), its place in the prayer (after the
thanksgiving, Megillah 18a:3), and the high priest's hands (R. Yehuda,
Mishnah Sotah 7:6) all read off one verse of the run. Exemplar (5), THE
CLASS: 9:4 and 9:18 "an ox and a ram for peace offerings FOR THE
PEOPLE" — "from here they learned peace offerings for the public"
(Sifra, Shemini, Mechilta d'Miluim 2 13); and Menachot 59a:11 puts the
eighth day's meal offering into the frankincense column by an inclusion
on Lev 2:1. **The fork inside the move (recorded, Menachot 19b:2-4):**
Rav — wherever Scripture REPEATED 'meal offering' it is indispensable,
and 9:17's fistful is the fistful repeated; Shmuel — "GENERATIONS ARE
NOT LEARNED FROM THE HOUR" — דורות משעה לא ילפינן ("generations from an hour we do not learn"): a one-time act does
not legislate. The direction of inference between run and spec is
itself a model parameter with two recorded settings, like THE METHOD
FORK's rival engines; the compile carries both arms. **Distinct from**
the RUN_CITATION pointer (the run citing its spec — "as the LORD
commanded", 9:7 and 9:10 — which the dependency gate dispositions and
the scene grades: that direction is verification, this one is
legislation) and from M-16 (the revocalization read — a consonant
string reheard; here the tokens are read as written, in a narrative
seat). **Machine form:** a run cell whose value is fetched from the
spec engine by call carries beside it a spec cell whose value is READ
FROM THE RUN'S token — the runner's people('palm_is_right') cell holds
the right hand derived from 9:17 and calls the meal-offering engine's
left-hand verdict as its check; the fork is carried as a two-arm value.
**Middah correspondence:** the verbal analogy (I2) on 'palm' with 'the
left palm' and on 'so shall you bless' with 'and Aaron lifted'; the
inclusion by the repeated term (Rav's arm) against the governance rule
that bars learning from the hour (Shmuel's arm) — logged in
logic/MIDDOT.md's case law as a rule about which seats may teach.

Exemplar (6), THE ORDER — the second form (2026-09-06, sitting E2,
cold_run_sanctuary_build.py): the SPEC writes the vessels first (the
ark, Exod 25:10) and the house after (the curtains, 26:1); the RUN
builds the house first (36:8) and reaches the ark at 37:1, and no
verse of either stratum says why. Berakhot 55a:12 — God told Moses
'make Me a TABERNACLE, an ARK, and VESSELS'; Moses reversed it;
Bezalel: 'the custom of the world is that a man builds a house and
then brings vessels into it... perhaps the Holy One said tabernacle,
ark, vessels?' — 'perhaps you were in God's shadow (בְּצֵל אֵל, "in
the shadow of God") and knew.' The run's order is the ORIGINAL
command and the spec's written order the messenger's inversion: the
run gives the spec not a column but its SEQUENCE. The spine's
recension (Midrash Tanchuma, Vayakhel 6:5; Buber 8:3) carries the
roles reversed — Bezalel ark-first against Moses house-first — a
two-recension dispute over which scheduling argument the exchange
carried; both tracks carried, the ink of 36-37 beside them. The
alignment engine that surfaced the gap (every run verse matched to
its spec verse by token; the order of first mention computed in each
stratum) is the compile's own instrument for this move: the run's
divergences from the spec are the seats where the tradition's
reading is sought per gap.

(7) THE PARAMETER (2026-09-06, sitting E3 — the vestments' spec Exod 28
graded against its run Exod 39): the spec's tunic verse (28:39) writes
'fine linen' (שש, "fine linen") twice — the tunic, the turban — and
gives the sash no material; the run's 39:27-29 writes it FIVE times.
Babylonian Talmud Yoma 71b:6 derives the SIXFOLD THREAD from the run's
five tokens ('one for flax, one for sixfold, one for twined, one for
the other garments, one to make it indispensable'), and the number is
the word's own homograph: שש "fine linen" IS שש "six" in the unpointed
text — the material-word read as its numeral. The run's 39:24 ADDS
'twined' (משזר, "twined") to the pomegranates the spec's 28:33 lacks,
and Yoma 71b:10 derives the twined EIGHT from that added token. The
run's 39:3 — 'they beat the gold plates and cut threads to work into
the blue, into the purple...' — has no spec counterpart and four of its
tokens stand nowhere else in the Bible; Yoma 72a:6-7 derives the gold
thread's count (four) and its placement (one into each color) from it,
closing the breastplate and ephod at twenty-eight. The tradition's
thread counts run on Exod 39, not Exod 28: THE RUN SUPPLIES THE SPEC'S
PARAMETER — the third form of the move (a column at D8, an order at
E2, a parameter here). Zevachim 88b:2 does it in citation form: 'the
robe was wholly of blue, AS IT IS SAID (Exod 39:22) and he made the
robe...' — the run verse cited for the spec's fact. The compile's
instrument is the same alignment engine: the run's ADDED tokens (found
by the per-block token diff) are the seats where the recorded
derivation is sought.

(8) THE DELTA (2026-09-06, sitting E4 — the investiture spec Exod 29
graded against its run Lev 8 across books): the spec girds Aaron AND
his sons in ONE verb — 29:9 'and you shall gird THEM with the sash,
Aaron and his sons' (וחגרת אתם, "and you shall gird them") — and the
run girds HIM twice at 8:7 (the sash, then the ephod's band: ויחגר
אתו, "and he girded him") and THEM once at 8:13 (ויחגר אתם, "and he
girded them"). Babylonian Talmud Yoma 5b:9 argues the dressing order
on exactly that split: Abaye — for the tunic and the turban all agree
Aaron then his sons, 'for both in the COMMAND and in the DOING Aaron
precedes'; the SASH is disputed — one says Aaron then his sons from
the run's two verbs, one says together from the spec's one verb. The
alignment engine's dropped token (29:9, no run verse matched) is the
sugya's ground: THE SPEC/RUN DELTA IS WHERE THE TRADITION ARGUES — the
fourth form of the move (a column at D8, an order at E2, a parameter
at E3, the delta here). The run's other deltas of the same sitting
carry the same shape: it INSERTS another spec's run (Lev 8:10-11, the
anointing list of Exod 30:26-29, with a sevenfold sprinkling the spec
never states), ADDS its own limiters (8:35 'keep the LORD's charge...
for so I was commanded' — Yoma 5b:2's two indispensability tokens),
and DROPS the laws for the generations (the dues 29:27-28, the
succession 29:29-30, the tamid and the Presence 29:38-46). The
compile's instrument: the per-block alignment with a BOOK field, and
the per-verse token diff at the blocks that match least.

(9) THE PARAMETER AGAIN, AND THE ADDED CLAUSE (2026-09-06, sitting E5 —
the erection Exod 40 as the whole spec's run; the craftsmen's call
Exod 31:1-11 against its run 35:30-35): the laver's spec (30:18-21)
writes NO measure, and its run adds one token to the spec's washing
verse — 40:31 'and MOSES and Aaron and his sons washed from it'
(ורחצו ממנו משה ואהרן ובניו, "and Moses and Aaron and his sons washed
from it") matches 30:19 at 0.89 with the one name added — and the
tradition computes the vessel's MINIMUM from the added subject:
'a laver without enough water to sanctify FOUR priests from it — one
does not sanctify from it' (Babylonian Talmud Zevachim 21b:12; Moses,
Aaron, and the plural's minimum two), with the high priest's rule
beside it, 'what is indispensable in his sons is indispensable in
him' (19b:9). And the run of the craftsmen's call ADDS a clause the
spec lacks — 35:34 'and TO TEACH He put in his heart' (ולהורת נתן
בלבו, "and to teach He put in his heart"), absent from 31:6 — the
sanctuary engine's teaching cell reads it from the run. The compile's
instrument: the alignment's per-verse token diff at the pair that
matches BEST (the one-token delta is the parameter's seat).

Exemplar (10), registered 2026-09-06 (sitting G1, cold_run_pre_sinai.py)
— THE FIRST CHAPTER IS THE FIRST SPEC/RUN PAIR: Genesis 1's nine
commands ('and God said') each against its execution clause, aligned
by token, and every deviation a sugya's ground — 'fruit tree making
fruit' (1:11, the spec) against 'tree making fruit' (1:12, the run) is
R. Eliezer's Tishrei and R. Yehoshua's Nisan, each dating creation
from ONE of the two seats and answering the other's token (Rosh
Hashanah 11a:3-6), and the run's second 'after its kind' the grasses'
own a-fortiori (Chullin 60a:10-12); 'the TWO GREAT lights' against
'the great... the SMALL' inside 1:16 the moon's diminishing (Chullin
60b:2-4); 'in OUR image, after our likeness' (1:26) against 'in HIS
image' with the likeness dropped and 'male and female' added (1:27)
the heretics' refutation by the singular beside the plural (Sanhedrin
38b:14) and the one-or-two creations (Ketubot 8a:9, Eruvin 18a:23,
Berakhot 61a:14); the beasts' order swapped (1:24/1:25); the waters'
command executed by 'and it was so' alone (1:9); 'let the WATERS
swarm... fowl' (1:20) against 'formed from the GROUND every fowl'
(2:19) resolved 'from the mud' (Chullin 27b:11). The machine's form:
the alignment engine's per-pair token delta as the cell's value, the
sugya on each delta on a [MOVE] line. The move's oldest exemplar sits
in the Torah's first chapter.

Exemplar (11), registered 2026-09-06 (sitting G2, cold_run_family.py)
— THE RETOLD RUN AS A THIRD SEAT: the servant's commission (Gen 24:2-9,
the spec), its run at the well (24:10-27), and the servant's own
RETELLING of both (24:34-49) aligned by token, and the retelling's
deltas are the sugyot's ground — 'perhaps' written PLENE at the
commission (24:5, אולי, "perhaps") and DEFECTIVE at the retelling
(24:39, אלי, "perhaps" spelled as "to me"), read by the spine (Bereshit
Rabbah 59:9) as the agent's own daughter and legislated by Mishnah
Kiddushin 3:1's agent who takes the bride for himself; 'the girl' (24:14,
הנער) retold as 'the maiden' (24:43, העלמה — Isaiah 7:14's token); the
ring given and THEN the lineage asked (24:22-23) retold as asked and
THEN given (24:47); the God clause retold with 17:1's walk; the double
condition's two seats (24:8 and 24:41 — Kiddushin 61b:10-12). The
machine's form: the alignment engine on three seats of one chapter —
cold_run_family.commission('retold_prayer', 'retold_commission',
'perhaps_two_spellings', 'gifts_two_moments', 'retold_god_clause') —
the retold run diffed against both the spec and the run.

Exemplar (7), THE MODE — added 2026-09-09 (THE TENT sitting 3, the
wood-gatherer): Exodus 31:14 "its profaners shall surely be put to
death" names a death and no mode; Numbers 15:35 "die shall die the
man; stone him with stones" is that law's first execution, and the
run's mode is read back into the spec — Bava Batra 119a:8 (R. Chidka
in Shimon HaShikmoni's name: Moses knew he was liable to death from
'its profaners shall die' but not by which death), Sanhedrin 78b:7,
Sifrei Bamidbar 114:1 ("die shall die" FOR THE GENERATIONS, "stone
him" for the hour). The compile's own shape: the Sabbath engine's
cell sabbath('death_run') in cold_run_incense_shekel.py imported this
run BY NAME on 2026-09-07, before Numbers had a reading; the gatherer's
runner (cold_run_mekoshesh.py) gives the import its home, and the tent's
output installs it as THE RULE INSIDE A LAW (rule_installed naming the
cell, not a daemon — World/step9/THE_TENT.md section 3).

Exemplar (12), registered 2026-09-09 (THE NUMBERS WALK sitting 1b,
cold_run_bamidbar.py — the exam docket of Numbers 1:1-4:20): THE
PREPOSITION AGAIN, read from the CAMP into the TABLE. The camp's order
writes "and BESIDE him (עָלָיו, 'upon him') the tribe of Manasseh" (Num
2:20) — a tribe cannot pitch upon another, so the preposition means
beside; Abba Shaul carries that reading into the showbread's law, "you
shall place pure frankincense UPON (עַל) each arrangement" (Lev 24:7):
the frankincense sits beside the arrangements, not on them (Menachot
96a:11, against the Sages' literal 'upon'). A term of a narrated
disposition of the camp legislates a column of the table's rite — the
move's shape with its teacher named; and the same preposition stands
as a TEIKU on "upon the wood" (Menachot 27a:2), the tradition's own
open question carried unresolved. The compiled cell camp('al') returns
both.

## M-23 — THE SECOND SEAT'S DELTA (a law written twice is diffed seat against seat, and the second writing's additions, drops, moves, and doublings legislate)
⚠ A GENERALIZATION (the link review law, LR3, 2026-09-07): the diff of
two seats is the machine's ENUMERATION; what a delta LEGISLATES is the
teacher's — this move is a teacher for a new pair only with a recorded
exemplar named beside it; otherwise the reading is a HYPOTHESIS (class H).
Registered 2026-09-06 (sitting E5 of the compile debt,
cold_run_erection.py) from EIGHT exemplars in one span. The teacher
holds a law at TWO SEATS — the same institution written twice by the
same book (Exodus 34:18-26 repeating 23:12-19 and 13:12-13) — and
reads the SECOND writing against the FIRST: what the second seat
ADDS is a new clause, what it DROPS narrows, what it MOVES is read
where it now stands, and what it DOUBLES (a token once at each seat)
is counted as a repetition. Move M-22 found that the spec/run delta
is where the tradition argues; this move is the same finding at the
register of law written twice — spec against spec. The compile's own
direction: the calendar and Passover engines' functions are CALLED
TWICE (the same cold functions at the second seat), the clause-pairs
aligned by token overlap (Jaccard: the kid clause 1.0, the matzah and
the appearing 0.7, the rest and the feasts about 0.25), and the
per-verse token diff typed as the cell's value. Exemplar (1), THE
ADDED TOKENS: 34:21 'in PLOWING and in HARVEST you shall rest'
(בחריש ובקציר תשבת, "in plowing and in harvest you shall rest"),
absent from 23:12 — read three ways: R. Akiva's added sabbatical (the
plowing of the eve that enters the seventh, Makkot 8b:3, Moed Katan
3b:13), R. Yishmael's omer harvest excluded (Menachot 72a:12), the
labors divided (Shabbat 70a:4) — Mishnah Sheviit 1:4 carrying both
readings. Exemplar (2), THE DOUBLING ACROSS SEATS: 'the firstling of a
donkey' (פטר חמר, "peter chamor") at 13:13 and (ופטר חמור) at 34:20 —
'peter chamor, peter chamor, TWICE: until the bearer is a donkey and
the born a donkey' (Bekhorot 5b:7, Mishnah Bekhorot 1:2; 6a:1: not
horses and camels); and 'you shall redeem' (תפדה, "tifdeh") three
times at each seat — 'tifdeh tifdeh: at once, with any amount' (10b:27),
'includes' (12a:3). Exemplar (3), THE MOVED CLAUSE: 'and they shall
not appear before Me empty' (ולא יראו פני ריקם, "and they shall not
appear before Me empty") at exactly two seats — closing the matzah
feast at 23:15, closing the firstborn's redemption at 34:20 — read at
its NEW seat: the son's redemption a standing liability like the
appearance offering, the heirs liable (Bekhorot 51b:8, 51b:11); the
clause ORDER 'redeem, then appear' (Kiddushin 29b:5); and exported to
the Hebrew slave's severance gift, five selas (Kiddushin 17a:7).
Exemplar (4), THE REVOCALIZED VERB of the moved verse: 'tifdeh' read
'tipadeh' — he redeems himself, sons not daughters (Kiddushin 29a:17;
move M-16 riding this one). Exemplar (5), THE ADDED NOUN: 34:22 'the
first fruits of the WHEAT harvest' (בכורי קציר חטים) fixes the two
loaves' grain, the first seat's 'the first fruits of your labors'
covering the barley (Menachot 84b:4). Exemplar (6), THE ADDED
NOUN-CHAIN: 34:25 'the SACRIFICE of the FEAST of the Passover shall not
remain to the morning' (זבח חג הפסח) for 23:18's 'the fat of My feast'
— ben Teima's chagigah of the fourteenth (Pesachim 70a:5); and 'My
sacrifice' (זבחי) at the two seats read as ONE DOUBLED TOKEN —
'zevach zevachai' (Pesachim 64a:6; R. Yehuda's tamid from the same
token, 64a:5; Mishnah Pesachim 5:4's two arms). Exemplar (7), THE
INSERTED NEIGHBOR: 34:17 'molten gods you shall not make' stands
before 34:18's feast where 23:14-15 has no idol clause — 'whoever
despises the festivals is as an idolater, for it is written... and
NEXT TO IT' (Makkot 23a:4, Pesachim 118a:12): the second seat's added
adjacency legislates. Exemplar (8), THE GENERAL AND ITS PARTICULARS on
the second seat's own tokens: 34:19-20 'ALL your cattle... ox and
sheep... and a donkey' — only those three (Bekhorot 6a:6). **Distinct
from** M-14 (the doubling arithmetic within one passage — here the
doubling is the repetition of a whole seat), from M-18 (the freed
token given to a neighbor — here the clause is MOVED by the ink
itself, not reassigned by the reader), and from M-22 (spec against
run — here spec against spec). **Machine form:** the runner's
repeats() cells hold the per-pair token diff as their value (the
alignment engine's delta), the calendar engine's cells fetched by call
beside them, and the sugya on each delta on a [MOVE] line; the
census also records what the second seat's spelling changes (the
ingathering plene, 'as I commanded you' without the comparative kaf).
**Middah correspondence:** the inclusion by repetition (the doubled
token as ribbui), the general-and-particular (I4), the juxtaposition
(semukhin) at the inserted neighbor, and the word-order read (M-11)
at the moved clause — four middot riding one diff.

Exemplar (9), registered 2026-09-06 (sitting G1) — THE THIRD SEAT:
the creation-rest clause written THREE times — Genesis 2:2-3 'He
CEASED' (וישבת, "and He ceased"), Exodus 20:11 'He RESTED' (וינח, "and
He rested"), Exodus 31:17 'He ceased and WAS REFRESHED' (שבת וינפש,
"He ceased and was refreshed") — diffed pairwise by the alignment
engine (the Decalogue's seat a retelling: added 18, dropped 22; the
sign's seat: added 8, dropped 14), and the ONE token the third seat
adds is Beitzah 16a:12's extra soul ('since He ceased — woe, the soul
is lost'). The watch the E5 tail set for Deuteronomy's third seats
answered a book early: a clause's third writing is diffed against
BOTH earlier seats, and what only the third seat carries legislates.
Machine form: cold_run_pre_sinai.sabbath('delta_20_11', 'delta_31_17',
'extra_soul_by_call') — the third seat's cell fetched from the sign
chapter's engine by live call.

Exemplar (10), registered 2026-09-06 (sitting G2, cold_run_family.py)
— THE DELTA ON AN INSTITUTION'S PARAMETER: the levirate at its first
seat (Gen 38:8, 'raise up SEED for your brother' — זרע, "seed", once at
38:8 and twice at 38:9) against its Sinai seat (Deut 25:5-6, 'shall rise
on the NAME of his brother' — שם, "name", at 25:6 and 25:7, no 'seed'):
the OBJECT changes (seed to name, resolved to inheritance by the family
runner's own 48:6 — Yevamot 24a:6), the KIN-SCOPE narrows (the kinsman —
Judah the father-in-law, Ruth 4's redeemer — to the brother: 'brothers
dwell together', the daughter-in-law an ervah among Yevamot 1:1's
fifteen), and a RELEASE FORM is added (the shoe — Ruth 4:7's 'formerly
in Israel' the run citing a custom the first seat never wrote). Two more
of the same shape in the sitting: the deed (23:17-20) restated at
49:29-32 and 50:13 (the record's tokens kept, the buried named), and
the firstborn's phrase 'the beginning of my vigor' (49:3) at Deut 21:17
with the DOUBLE added. Machine form:
cold_run_family.levirate('seed_vs_name', 'levirate_alignment',
'kin_scope_narrowed', 'no_release_form'); purchase('deed_restated',
'deed_alignment'); testament('firstborn_alignment').

Exemplar (11), registered 2026-09-09 (THE TENT sitting 4, cold_run_zelophehad.py)
— THE SECOND OUTPUT ON THE SAME CASE: the daughters' statute at its first
seat (Num 27:8-11 — the ladder for the generations, 'a statute of judgment')
against its second (Num 36:5-9 — the tribes' plea answered RELAYED, 'and
Moses commanded... by the mouth of the LORD'): the second seat ADDS a limit
on the heiress ('only to the family of the tribe of their father', 36:6),
a bar on the transfer ('shall not go around from tribe to tribe', 36:7, 36:9)
and a REACH clause the first seat never carried — 'THIS is the thing that
the LORD commanded' (36:6), read by Rava as this generation alone (Bava
Batra 120a:10) with the silence test at 120b:2 (a formula that teaches
nothing else limits the generation) and its LAPSE dated to the fifteenth
of Av (121a:7: the tribes permitted to intermarry). The delta is the ink's
own frame too: the first output 'and the LORD said to Moses, saying', the
second Moses' own command by the Word (computed: 'by the mouth of the LORD'
at eighteen Torah seats, Lev 24:12's halt clause among them). The engine's
form: the second seat installs a CELL of the case-born law (rule_installed
naming law_zelophehad:tribe_transfer — sitting 3's rule-inside-a-law on a
case-born law), so the statute stands amended on the ledger with a reach.
Machine form: cold_run_zelophehad.the_daughters('second_output', 'reach',
'lapse'); the row tribe_transfer_reach (this_generation / all_generations —
the second arm refused at 120b:2); the tent daemon's command_relayed branch.

## M-24 — THE REPETITION TEST (a law's scope across eras is decided by whether the code writes it twice; the second writing is the edge)
⚠ A GENERALIZATION (the link review law, LR3, 2026-09-07): the rule is
the tradition's own (Sanhedrin 59a:11-13) and its seven exemplars are
taught; but "the machine's form is the dependency gate itself" below
describes an ENUMERATION of shared tokens, which a person may do, not a
license to transfer law on one — a repetition edge is a teacher for a
new pair only with Sanhedrin 59a's list or another recorded exemplar
named beside it; otherwise the pairing is a HYPOTHESIS (class H).
Registered 2026-09-06 (sitting G1 of the compile debt,
cold_run_pre_sinai.py) from the tradition's own stated rule and five
exemplars. R. Yosei son of R. Chanina (Sanhedrin 59a:11-12): 'every
command said to the sons of Noah and REPEATED at Sinai was said to
both; said to the sons of Noah and NOT repeated at Sinai — to Israel
and not to the sons of Noah; and we have only the sinew, per R.
Yehuda.' The rule decides SCOPE by COUNTING SEATS: a pre-Sinai law
binds the nations only if the code writes it a second time at Sinai;
a law written once before Sinai and never again passes to Israel
alone. The machine's form is the dependency gate itself — an edge from
the pre-Sinai runner into a Sinai engine exists exactly where the law
was repeated, and the repetition's seat is what the cell fetches by
live call: the seven laws each to their Sinai home (the courts to the
ordinances engine's Exod 23:2, blasphemy to Lev 24:15-16, idolatry to
the ordinances engine's Exod 22:19, the unions to the sanctions
engine's Lev 18/20 rows, bloodshed to Exod 21:12 and Lev 24:17,
robbery to the holiness engine's Lev 19:11-13, the limb to the
sanctions engine's Lev 17:14 — 'its blood in its life' at Gen 9:4 and
Lev 17:14 alone in the Tanakh, the two tokens swapped, the census's
edge in both directions). Exemplar (1), THE REPETITION WITH A JOB:
circumcision, said to Abraham (17:9 'and YOU shall keep My covenant')
and repeated at Sinai (Lev 12:3 'on the eighth day') — yet Israel's
alone, because 'that repetition came to PERMIT THE SABBATH: on the
DAY, even the Sabbath' (59b:1-2): a second seat whose added job
exhausts it does not widen the scope. Exemplar (2), the same shape at
procreation: said to Noah (9:7) and repeated at Sinai (Deut 5:27
'return to your tents') — the repetition came for the counted-body
principle (59b:3-4); Israel's by the framework. Exemplar (3), THE
NEVER-REPEATED: the sinew (Gen 32:33), never written again — Israel's
alone (59a:12; Mishnah Chullin 7:6 'said at Sinai, written in its
place' the sages' reverse account: sitting G2's). Exemplar (4), THE
SCOPE READ OFF THE ADDRESSEE: 'you and your seed after you' (17:9) —
no one else (59b:9); the seed narrowed by 'in Isaac' (21:12) and 'in
Isaac, not all of Isaac' (59b:10-11), widened by 'he has broken'
(17:14) to the sons of Keturah (59b:12). Exemplar (5), THE NEGATIVE
BOUNDARY STATED BY THE CODE'S OWN LAW: the fat (Lev 7:23-25) — 'Israel
exhorted, NOT the sons of Noah; the a-fortiori from the limb refuted
by the children of Israel' (Sifra Tzav Section 10 1, the Tzav
engine's cold cell fetched by call): a Sinai law with no pre-Sinai
seat stays Israel's, and the tradition says so at the law's own seat.
**What separates it:** from M-23 (the second seat's DELTA legislates
content; here the second seat's EXISTENCE legislates scope), from
M-07 (an import across spans; here the rule about which spans may
import at all), and from M-22 (the run teaches the spec; here the
repetition teaches the addressee). **Middah correspondence:** the
'general and particular' family read across ERAS rather than clauses;
the counted-body principle (59b:4) as its own recorded exception.

Exemplar (3) CONFIRMED, 2026-09-06 (sitting G2, cold_run_family.py):
the sinew's token homed at the family runner alone — the dependency
census required NO edge for it, and the absence is the exception's
machine form; the ink writes the anachronism the sages read ('said at
Sinai, written in its place'): 'the SONS OF ISRAEL shall not eat' (Gen
32:33, בני ישראל, "the sons of Israel") is the phrase's FIRST seat in
the Bible, four verses after the name is given (32:29). The forward
half of the same test: the levirate and the birthright ARE repeated at
Sinai (Deut 25:5-10, 21:15-17) and the runner declares those edges
OWED to runners that do not exist yet — `--debt` prints them.

## M-25 — THE ARTICLE READ AS THE DISTINGUISHED MEMBER (a definite article on a noun for a body part or an instrument is read as 'the distinguished one of its kind')
Registered 2026-09-06 (sitting G2 of the compile debt,
cold_run_family.py) from Rava's rule and its four recorded seats. 'And
what is the reason? Rava said: the verse says THE thigh — the
DISTINGUISHED thigh' (Chullin 91a:12, on Gen 32:33, הירך, "the thigh"):
the article on the sinew's thigh is read as 'the best of its kind' —
the right — and the tradition exports the reading to three other
institutions in its own words ('as Rava said of THE thigh, so here'):
'THE arm' of the priestly gifts — the distinguished arm, the right
foreleg (Deut 18:3, Chullin 134b:16); 'THE anointed' — the
distinguished among the anointed, the high priest (Horayot 12a:16);
'THE awl' of the pierced slave — the large awl (Exod 21:6, Kiddushin
21b:11 — the Mishpatim engine's seat). Measured: 'the thigh' with the
article is a HAPAX form in the Tanakh — Rava's rule runs on the
article's only seat. The rival reading carried: the Mishnah's own 'the
right thigh and the left' (Chullin 7:1) against R. Yehuda's right only,
and R. Yehoshua b. Levi's embrace geometry for the right (91a:14).
**What separates it:** from the pre-Sinai runner's 'THE sixth' (Shabbat
88a:6 — the article as the KNOWN one, a specific day), from M-11 (the
word order), and from the general-and-particular family (I4) — here the
article itself restricts to the superlative member. **Machine form:**
cold_run_family.sinew('the_thigh_articled', 'article_as_distinguished',
'right_thigh'). **Middah correspondence:** a restriction (miut) read
off the definite article; the four seats the rule's own census.
