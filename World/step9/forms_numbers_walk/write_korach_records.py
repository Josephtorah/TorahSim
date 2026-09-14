#!/usr/bin/env python3
# THE NUMBERS WALK 5b — the records (the as-built, the research log, the move catalog, the docket's correction, THE_STEPS, COMPILE_DEBT,
# RESUME, THE_BRIEFING); the state doc and memory follow after the journal gate and the sweep. Every anchor asserted once; append-only files
# appended.
import re
def rep(path, a, b):
    s = open(path, encoding='utf-8').read()
    assert s.count(a) == 1, (path, a[:80], s.count(a))
    open(path, 'w', encoding='utf-8').write(s.replace(a, b))
def app(path, text, must_end=None):
    s = open(path, encoding='utf-8').read()
    if must_end: assert s.endswith(must_end), (path, s[-120:])
    open(path, 'a', encoding='utf-8').write(text)

# ---- 1. NUMBERS_WALK.md — the as-built ----
app('<repo-old>/World/step9/NUMBERS_WALK.md', r'''
## Sitting 5b — AS BUILT (2026-09-10; the order above run end to end)

THE DOCKET (logic/oral_triage/num_16_18_korach_exam_2026-09-10.md, 316 rows — 209 link rows in 36 works, 107 topic rows by address; LAW
195, DERIVATION 46, DISPUTE 42, CONTEXT 33; 94 CREDITED prior reads with their ledgers named on the row, each given its quick look; the 33
long ranges sized from the scan's own print; gloss lint 0 after one flag read — a hyphenated compound). Its crowns: KORACH'S DEATH ARGUED
ON THE SHELF (Sanhedrin 110a:13-14 — R. Yochanan reads 16:32 as NOT Korach and 26:10 as not him either, the plague; the baraita (the outside
teaching) both burned and swallowed: the ink's silence at 16:32 is the tradition's own open question); THE TRANSLATION LOAD-BEARING AGAIN
(Zevachim 91a:19 cites Onkelos' "for greatness" by name as the ground for how the priests eat); THE DECREE OVER THE A-FORTIORI ON THE ANSWER
SHEET (Mishnah Ketubot 5:3's "a court that convened after them said: not until she enters the canopy" against Sifrei 117:2's argument);
THE STRANGER'S DEATH BY TWO IDENTITIES (Sanhedrin 84a:13; Mishnah Sanhedrin 9:6 — the row zar_who_served already Bamidbar's at 1:51, read by
CALL); THE TITHE OF THE TITHE ONE IN A HUNDRED with THE LEVITE WHO PRECEDED THE PRIEST at six seats (on the stalks the tithe's terumah only,
after the pile the great terumah too); BY ESTIMATE AND BY THOUGHT (Abba Elazar ben Gomel's plural "your terumah" at five Talmud seats — Sifrei
121:1's own row); THE COAL PANS ELEVATED (Menachot 99a:11 — "one elevates in sanctity" derived from 17:3); THE COURT'S SUMMONS READ OFF THE
CHAPTER (Moed Katan 16a:3-5); THE FIRSTBORN'S WINDOW BY JUXTAPOSITION (two days and a night; one placement on the base); THE STAFF BESIDE
THE ARK ("for safekeeping" / "for safekeeping"); A CONGREGATION IS TEN, FROM KORACH. One correction APPENDED to the docket after the runner's
first import: the terumah's measure ROW is this runner's own (Shelach carried a placeholder copy marked OWED); the naso engine's cell is the
floor — the docket's "naso's row CALLED" notes read that way.

THE PARSER: census_probes rows G1-G7 and the regression rows R22-R34 typed to FAIL (G1-G5 failed as designed: 16:35 [200], 38:28 [7, 75],
31:54 [2100], 26:5 [50, 51], 36:12 [50, 51, 1, 1]; every regression row passed), then the rules built in cold_run_sequence.py's INK block —
(17) THE DEFINITE NUMERAL AT THE HEAD OF A COMPOUND (the article-bearing numeral before plain 'and' + a bare numeral opens the chain), (17b)
the article on the hundreds-word after a unit multiplies, (17c) the article-bearing PLURAL thousands / hundreds with no unit before it is a
noun, (18) THE DEFINITE ONE'S JOIN GATED BY THE ACCENT (a conjunctive joins, 12:18's darga; a disjunctive closes, 26:5's and 36:12's segolta,
25:32's and 37:18's zaqef). THE CORPUS-WIDE DIFF (korach_parser_diff.py, the 4b parser as its base) read verse by verse: SEVEN moved — the
three the design named (16:35 → [250], 38:28 → [1775], 31:54 → []) and the four definite-one seats (26:5, 36:12 → [50, 1, 50, ...]; 25:32,
37:18 → [6, 3, 1, 3]). THE HAND'S PROBE EXPECTATIONS WERE WRONG FOR THE FOUR: typed [50, 50] and [6, 3, 3] from the neighbor rule, where
4b's own rule (14) counts the definite one as ONE (26:4, 26:10, 25:33 the same class) — retyped from the reading of the class, 130/130
after. Two of the seven were 4b's diff rows ACCEPTED WRONG at that sitting (26:5, 36:12 read [50, 51] off the F34 join) and two more of the
same class the 4b census had shown and the hand read past (25:32, 37:18 [6, 3, 4]): the class's own census at this sitting surfaced them —
RESEARCH_LOG 2026-09-10 (the seventh entry).

THE TYPES (add_types_korach.py, idempotent; the `he` the whole verse from the pointed DB, no anchor word typed): 31 kinds (25 tape kinds +
6 case kinds — stranger_service_case and priestly_gifts_case named apart from the existing stranger_case and gifts_case, the registry
checked before the names were typed), 12 effects, 7 registry rows (korach, dathan, abiram, on_son_of_peleth, eleazar_son_of_aaron,
the_two_hundred_fifty re-homing the tape's raw token, aarons_staff as an object), the daemon block law_korach (the 52nd, installed_by boot),
the functions block (5 WRAPPED), the span + 11 edges (bamidbar / incense_shekel / pesach / temurah / tzav / naso / holiness_b / zelophehad /
priesthood / offerings CALL; shelach -> korach CALL — THE OWED ROW OF 4b FLIPPED, 15:20's pointer PAID; the registration), I5 52. The gates
to FAIL: the daemon gate 2 (the def missing; the functions undeclared), the dependency gate 12 (eleven CALLs without their import; the
registration).

THE RUNNER (World/step9/cold_run_korach.py, written in five parts and joined — 155 cells F1-F5, 100 probes, 36 DATA rows): FOUR
import-time asserts read and retyped before the first grade — the floor-word's seats counted on the bare token found 18:27 alone (the
STEM has three prefixed forms: 15:20, 18:27, 18:30 — counted by the stem), the covenant-of-salt census by LIKE on the pointed bytes found
nothing (the census runs on the stripped tokens: 2 Chr 13:5 and Num 18:19 alone), the terumah-measure row's KeyError (the row's home
moved to this runner), the priesthood engine's household cell wanting its member named (who='wife'), the festival engine's two loaves a
dict of cells (no 'v'). THE FIRST GRADED RUN 155/155; THE SCENE matched its prediction (eleven rows, eleven entities); THE NARRATIVE
matched its prediction IN EVERY SLOT — forty-two slots, twenty-five events, thirty-seven writes (the thirty-five at the lines + the two
fires), two timers set and fired at (2, 5, 10), twelve entities — the first narrative prediction of the walk to match without a retype.
The guard's tripwire typed at 155. THE CELL NAMES THE DOCKET USES CHECKED BY SCRIPT against the runner's asks (92 named, 155 asks, 0
missing). cold_run_shelach's challah('as_terumah') now CALLS cold_run_korach.the_tithe('terumah_measure') — its answer-sheet row retyped
to "PAID", 172/172.

THE GATES' FIRST FAILS READ: the daemon gate parses `if k == '...'` branches only and kind names of letters and underscores — the two
`if k in (...)` branches leaked the next branch's effects into the parsed set (plague_staff_case parsed with watch_owed and stranger_barred)
and the digit kind fire_consumed_the_250 read as '?UNRESOLVED?': the branches split, the kind renamed fire_consumed_the_two_hundred_fifty
in the runner, the registry and the daemon block; the five case kinds' declared sets brought to the cells' written sets. The dependency
gate's token census named SIX MORE EDGES and THREE POINTERS: chatat (18:9's sin offering — CALL by domain(unwitting); 16:26's "their sins"
the homograph named in the row), minchah (18:9's meal offering — CALL by adjuncts(sinner); 16:15's "their offering" Cain's word, the
homograph), moadim (18:13's first fruits — CALL by two_loaves()), vayikra5 (18:9's guilt offering — CALL by pointers(asham_procedure)),
yovel (18:16's "by your valuation" — CALL by field_valuation(49)['shekel'] = 20, Lev 27:25's second seat; the tithe tokens VIA temurah),
family VIA zelophehad (the inheritance tokens at 16:14, 18:20-26); the AS_WHEN pointers 17:5, 17:12, 17:26 INTERNAL (the span's own
citations). Both gates GREEN after: 52 daemons, 366 functions WRAPPED, 0 unconsumed; the link census 334 reference / 47 transfer / 9
hypothesis / 117 none of 357 edges + 150 pointers.

THE RECORDER AND THE STITCHER: korach 36 submits — 25 HISTORY, 11 case (no statute). No marker row (the stretch undated in the ink and on
the shelf — Seder Olam Rabbah searched by script). THE CENSUS typed from its print (1919, 1126, 1161, 777, 6, 10, 7, 0, 71, 152, 120, 15, 17,
706, 255) — on tape +25, kinds +25, subjects +5 (korach, dathan, the-two-hundred-fifty now a subject, eleazar, aarons-staff), markers
UNMOVED; the twenty-five lines placed page_order at the running clock's (2, 5, 9) around the incense runner's standing Num 16 line.

THE RUN (cold_run_sequence.py): the tuple PREDICTED before the run — (1161, 51, 50, 0, 12, 1369, 23, 288, the four pairs, 104) — and
MATCHED ON THE FIRST TAPE RUN; THE REST reproduced sitting 4b exactly. The ten checks: NINE OF TEN on the first run — the one MISS the
PLACEMENT literal (events page_order 995 -> 1020: the twenty-five lines page_order, as designed; typed from the stitcher's print and the
run's own reading), 10/10 after. CK1 MATCH the definite numeral (16:35 [250] = 16:2; 38:28 [1775]; 31:54 []); CK2 MATCH the two morrows
FIRED at (2, 5, 10), the return marker + 1; CK3 MATCH the plague's 14,700 on Israel's ledger, the 250 on their own entity; CK4 DIVERGE AS
EXPECTED, OPEN — 26:10 adds "and Korach", 16:32 does not name him (the ledger's put_to_death on Korach carries the OPEN row korach_death_
mode with Sanhedrin 110a's two arms); CK5 MATCH the twelve staffs with Levi among them, Aaron's staff budded and kept; CK6 MATCH the staff
beside the jar (omer_kept and kept_for_a_sign both on the ledger); CK7 MATCH "no more wrath" — the one token added (עוד, "more") and the
1:53 guard and the 18:5 watch both on the Levites' ledger; CK8 MATCH the arithmetic (1/100; [5, 20] at the shekel engine's seat; the
twenty-four); CK9 MATCH the three closes and the pointer's edge flipped. CB8, CN1, CE1-CE9, CF1-CF9 unmoved; 5.2 s. The gates after the
run: installation 6/6 (52 daemons, pending law_pesach), clock, sequence 4/4, cursor 6/6, view 6/6 — GREEN.

OWED FORWARD from this sitting: Korach's death-mode row OPEN (CK4 — the retelling at 26:10 is Pinchas's census, its compile); the Levites'
tithe given to the priests by Ezra's penalty (Yevamot 86b — the Writings' run); the twenty-four gifts' border items with their own seats
(the first shearing, the shoulder-cheeks-maw — Deut 18; the field of holding — Lev 27 by CALL); the exclusion table's 26:53-55 clauses at
Pinchas; Shelach's placeholder DATA row terumah_measure retired at a registry pass (its values the same, its home here); CF2's one day,
CF6's ten and the forty-year timer's fire (due (40, 5, 9)) at Chukat's markers; the other bare measure nouns named and left at 4b.

⚠ LESSONS (5b): THE PROBE'S EXPECTATION IS TYPED FROM THE CLASS'S OWN READING — the four definite-one rows typed from the neighbor rule
([50, 50], [6, 3, 3]) where 4b's rule (14) counts the definite one as ONE; the run read it. A CLASS'S CENSUS SURFACES THE PREVIOUS DIFF'S
ACCEPTED ROWS (26:5, 36:12 [50, 51]; 25:32, 37:18 [6, 3, 4] — accepted or read past at 4b): the accent decides, and the previous sitting's
diff is reread when a class is re-measured. THE STORE'S BARE TOKEN IS NOT THE STEM (the floor-word at three seats under three prefixes —
count by the stem). A LIKE ON THE POINTED BYTES FINDS NOTHING — a census runs on the stripped tokens. THE ROW'S HOME IS WHERE THE INK IS
(the terumah measure's row was Shelach's placeholder, the design had typed "naso's row"; the KeyError read). A CALLEE'S KWARGS AND SHAPE
ARE READ AT THE FIRST IMPORT (who='wife'; a dict of cells without 'v'). THE DAEMON GATE PARSES `if k == '...'` ONLY AND LETTERS-AND-
UNDERSCORES KIND NAMES — no `if k in (...)`, no digits (a leaked branch, an unresolved kind). THE TOKEN CENSUS NAMES THE HOMOGRAPHS INSIDE
A CALL ROW (16:26's "their sins" beside 18:9's sin offering; 16:15's Cain's word beside 18:9's meal offering) — one edge per pair, the
homograph in the why. THE PLACEMENT LITERAL IS TYPED FROM THE PRINT, AGAIN (the tenth check's MISS was the literal, not the tape). THE
NARRATIVE PREDICTION CAN MATCH FIRST RUN when the timer lesson is applied (writes = effects less timers plus fires): forty-two slots.
''', must_end="THE_BRIEFING, RESUME, memory).\n")

# ---- 2. RESEARCH_LOG.md ----
app('<repo-old>/RESEARCH_LOG.md', r'''
## 2026-09-10 — THE DEFINITE NUMERAL AT THE HEAD OF A COMPOUND TAUGHT, AND THE CLASS'S CENSUS SURFACING
## THREE FALSE READINGS (ONE OF THEM THE PREVIOUS SITTING'S OWN ACCEPTED DIFF)

At THE NUMBERS WALK sitting 5b (the compile of Korach, Numbers 16:1-18:32), the
parser's gap measured at the reading — 16:35 "THE fifty and two hundred men" read
[200], the article on the first numeral silencing it — was censused as a CLASS on
the whole Tanakh DB before the rule was typed: every article-bearing numeral word
with the word after it (korach_compile_measure.py). Findings:

1. The class is small: nineteen tokens in the Bible where a vav-NUMERAL follows
   (fifteen in the Torah), sixty-four where a vav-other word follows, 270 with no
   vav. Of the fifteen, twelve are THE DEFINITE ONE (4b's class — "under the ONE
   board, and two sockets"), one is Num 16:35, two are Exod 38:28's "THE thousand
   and seven THE hundreds and five and seventy" — which the engine had read as
   [7, 75] since the parser's first day: the article silenced the head, and the
   article on the hundreds-word inside the chain silenced the multiplier. The
   ink's own 1,775 (Exod 38:25's number, probe R4 since 1b) at its second seat,
   never read. Rule (17): an article-bearing numeral before plain "and" + a bare
   numeral opens the chain; (17b): the article on the hundreds-word after a unit
   multiplies.
2. The vav-other class held a fourth false reading: Num 31:54 "the captains of
   THE THOUSANDS and of THE HUNDREDS" read [2100] — 1b's "and the" chain rule
   (Num 3:46's "the three and the seventy and the two hundred") firing on two
   plural unit-nouns after "captains of". Rule (17c): the article-bearing plural
   thousands / hundreds with no unit numeral before it is a noun.
3. THE PREVIOUS SITTING'S OWN DIFF, ACCEPTED WRONG: 4b's rule (14) for the
   definite one joined "the ONE and twentieth" (Exod 12:18 — F34, read off that
   sitting's diff). The same join fired at Exod 26:5 and 36:12 "in the ONE
   curtain, and FIFTY loops" → [50, 51], and the 4b diff listed the rows as moved
   and the hand accepted them; and at 25:32 and 37:18 "from its ONE side, and
   three branches" → [6, 3, 4], which the 4b census had printed beside the rule
   and the hand read past. THE ACCENT DECIDES: 12:18's "the one" carries a darga
   (conjunctive) and joins; 26:5's and 36:12's carry a segolta, 25:32's and
   37:18's a zaqef — disjunctives, the number closes. Rule (18): the definite
   one's join is gated by the accent — M-26 (the accent read) extended to the
   definite one; the exemplar appended to the catalog.
4. THE HAND'S PROBE EXPECTATIONS FOR THE FOUR WERE WRONG TOO: typed [50, 50]
   and [6, 3, 3] from the neighbor rule's shape, where 4b's rule (14) counts the
   definite one as ONE (26:4, 26:10, 25:33 the same class, read [50, 1, 50] and
   [3, 1, 3, 1, 6] since 4b). The run read it; the rows retyped from the class's
   reading: [50, 1, 50], [50, 1, 50, 1, 1], [6, 3, 1, 3].
5. The corpus-wide diff (the 4b parser as base): SEVEN verses moved — exactly the
   three the design named and the four definite-one seats; nothing else. 130/130
   probes after (the seven G rows and thirteen regression rows R22-R34 added).
Beside the parser, two census lessons at the runner's import: the threshing-
floor word counted on the bare token found one seat where the stem has three
(15:20 "the terumah of the floor" bare in the construct, 18:27 "THE floor",
18:30 "the produce of the floor") — count by the stem; and a LIKE on the
pointed bytes for "salt" found nothing — a census runs on the stripped tokens
(the covenant of salt at two seats in the Bible, 2 Chr 13:5 and Num 18:19, then
confirmed).
''')

# ---- 3. MOVE_CATALOG.md — M-26's exemplar ----
rep('<repo-old>/logic/MOVE_CATALOG.md', "\n## M-27 — THE SPEAKER SPLIT",
    r'''
Exemplar (2), THE NUMBERS WALK 5b (2026-09-10 — the compile of Korach): THE
DEFINITE ONE'S JOIN GATED BY THE ACCENT. 4b's rule (14) had joined הָאֶחָד ("the
one") to a following "and TENS" — right at Exod 12:18 "the ONE and twentieth
day", wrong at Exod 26:5 and 36:12 "in the ONE curtain, and FIFTY loops" (read
[50, 51]) and at 25:32 and 37:18 "from its ONE side, and THREE branches" (read
[6, 3, 4]). The marks decide: 12:18's "the one" carries a darga (a conjunctive)
and joins; 26:5's and 36:12's carry a segolta, 25:32's and 37:18's a zaqef —
disjunctives, the number closes and the definite one counts one. Rule (18) in
the parser; the corpus-wide diff moved exactly those four (with the three seats
of the compound class). The accent read's second exemplar after Naso's "one
pan, ten of gold".

## M-27 — THE SPEAKER SPLIT''')

# ---- 4. the docket — the correction appended ----
app('<repo-old>/logic/oral_triage/num_16_18_korach_exam_2026-09-10.md',
    "\n## CORRECTION (appended 2026-09-10 at the runner's first import, append-only): the rows on Mishnah Terumot 4:3 and Num 18:12 say \"naso's row CALLED\" — the ROW terumah_measure (1/40, 1/50, 1/60) is cold_run_korach.py's OWN (Shelach's challah cell carried a placeholder copy marked OWED at 4b, paid by its live call into this runner); the naso engine's CELL restitution(terumah_measure) supplies the FLOOR (Mishnah Terumot 4:5: some must remain common) and is CALLED for that. The verdicts stand; the attribution corrected here.\n")

# ---- 5. THE_STEPS.md — the 5b paragraph ----
rep('<repo-old>/THE_STEPS.md', "Sifrei ranks. Next: Korach's compile (5b), then chapter 19.\n",
    r'''Sifrei ranks. Next: Korach's compile (5b), then chapter 19.

THE COMPILE OF KORACH (sitting 5b, 2026-09-10, on Brian's "Go" after
the rereads) paid the fifth portion's compile on the same order. The
exam docket first: 316 rows, ninety-four of them already read in
earlier ledgers and credited with a quick look. Then the parser was
taught the definite numeral at the head of a compound — "THE fifty and
two hundred men" reads 250 — and the census of that class over the
whole Bible found three readings that had been wrong all along: Exodus
38:28's "THE thousand and seven THE hundreds" had read as seven and
seventy-five instead of 1,775 (the same number the parser reads right
three verses earlier), "the captains of THE thousands and of THE
hundreds" had read as 2,100, and the previous sitting's own rule for
"the one" had joined it to a following "and fifty" — "in the ONE
curtain, and fifty loops" as fifty-one — which the cantillation
settles: a joining mark on "the one" joins (the twenty-first day), a
dividing mark closes (the loops). The whole-corpus diff moved exactly
seven verses, all of them these. Then the runner: five cells — the
rebellion, the plague and the staffs, the watch, the gifts, the tithe —
calling ten earlier engines (the firstborn's redemption is Bamidbar's
own cell, the stranger's death mode Bamidbar's own row, the ass the
Passover engine's, the devotions the temurah engine's, the breast and
thigh the tzav engine's, the terumah's floor the naso engine's, the
hundred-and-one the holiness engine's, the exclusion by sin the
inheritance engine's, the household's eaters the priesthood engine's,
the peace offering's window the offerings engine's), 155 of 155 on the
first graded run, and — for the first time in the walk — the tape's
narrative prediction matched in every slot without a retype: twenty-
five lines, thirty-seven writes, two one-day timers ("tomorrow", "on
the morrow") firing the day after the running clock's day on a stretch
that carries no date in the ink or on the shelf. Korach's own death
stays an open row on the ledger: the earth's verse names "every person
who belonged to Korach" and not Korach, the census's retelling adds
him, and the Talmud argues both ways. The dependency gate's token
census named six more engines the span touches and three "as the LORD
spoke" pointers, each read and filed; the daemon gate taught the
machine that it reads only one branch form. Every gate and the sweep
green. Next: chapter 19, the heifer's reading.
''')

# ---- 6. COMPILE_DEBT.md — the sitting-5 line PAID + the STILL OWED line ----
rep('<repo-old>/World/step9/COMPILE_DEBT.md',
    "## export's translator STOPS inside 121), 30 claims seated, three rituals → 193 units, standing 1989, hash unmoved. OWED TO THE COMPILE (5b): (a) THE",
    "## export's translator STOPS inside 121), 30 claims seated, three rituals → 193 units, standing 1989, hash unmoved. PAID AT 5b (2026-09-10; NUMBERS_WALK.md \"Sitting 5b\" design + as-built — every item below paid unless the STILL OWED line names it: the parser's rules (17), (17b), (17c), (18) with 130/130 probes and the corpus diff's seven verses read; cold_run_korach.py F1-F5, 155/155 first graded run, ten engines CALLED, the docket 316 rows; the tape's twenty-five lines, two morrow timers, law_korach the 52nd, the RUN tuple predicted and matched first run, THE REST exact, CK1-CK9 as designed; 15:20's pointer PAID by shelach -> korach CALL): (a) THE")
rep('<repo-old>/World/step9/COMPILE_DEBT.md',
    "## chatat / terumah, zelophehad, sequence → korach; NO DATE IN THE INK (undated on the shelf — recorded).\n",
    "## chatat / terumah, zelophehad, sequence → korach; NO DATE IN THE INK (undated on the shelf — recorded).\n"
    "## STILL OWED (5b): Korach's death-mode row OPEN (CK4 — 16:32 against 26:10; the retelling at Pinchas's census, its compile); the Levites' tithe to the priests by Ezra's penalty (Yevamot 86b — the Writings' run); the twenty-four gifts' border items at their own seats (the first shearing and the shoulder-cheeks-maw at Deut 18; the field of holding Lev 27 by CALL); the exclusion table's 26:53-55 clauses at Pinchas; Shelach's placeholder DATA row terumah_measure (its home now cold_run_korach.py) retired at a registry pass; CF2's one day, CF6's ten and the forty-year timer's fire at Chukat's markers; the bare measure nouns named and left at 4b.\n")

# ---- 7. World/RESUME.md ----
app('<world-link>/RESUME.md' if False else '<repo-old>/World/RESUME.md',
    "SITTING 5b DONE 2026-09-10 (THE COMPILE OF KORACH 16:1-18:32; NUMBERS_WALK.md \"Sitting 5b\" design + as-built): the docket 316 rows (94 credited); the parser taught the definite numeral at the head of a compound, the hundreds-word's article, the plural unit noun and the definite one's accent gate (seven probes to FAIL, 130/130; the corpus diff's seven verses read — three false readings surfaced, one of them 4b's own accepted diff); cold_run_korach.py 155/155 first graded run, ten engines CALLED, law_korach the 52nd daemon; the tape's twenty-five lines with two one-day timers on the undated stretch, RUN (1161, 51, 50, 0, 12, 1369, 23, 288, four pairs, 104) predicted and matched first run, THE REST exact, CK1-CK9 (CK4 Korach's death-mode OPEN); the two gates' first fails read (the branch form, the digit kind, six token edges, three pointers); 15:20's terumah pointer PAID. Numbers 1:1-18:32 read, frozen, compiled and on the tape. NEXT: chapter 19 (the heifer's reading).\n")

# ---- 8. THE_BRIEFING.md — the scoreboard bullet + the entry ----
rep('<repo-old>/THE_BRIEFING.md', "## SCOREBOARD (as of 2026-09-10, latest)\n\n",
    "## SCOREBOARD (as of 2026-09-10, latest)\n\n"
    "- **KORACH COMPILED — SITTING 5b DONE: THE PARSER READS \"THE FIFTY AND TWO HUNDRED\", ITS CENSUS CATCHES THREE OLD MISREADINGS (ONE OF THEM YESTERDAY'S OWN), AND THE TAPE'S PREDICTION MATCHES IN EVERY SLOT FIRST RUN** (2026-09-10, on your \"Go\"; World/step9/NUMBERS_WALK.md \"Sitting 5b\"). The exam docket 316 rows (195 laws; 94 credited from earlier ledgers). The parser taught the definite numeral at the head of a compound with seven probes written to fail first; the class censused over the whole Bible found Exodus 38:28's 1,775 read as seven and seventy-five since the parser's first day, Numbers 31:54's captains read as 2,100, and the previous sitting's join of \"the one\" firing where the cantillation says stop — the whole-corpus diff moved exactly seven verses. cold_run_korach.py: five cells, 155 of 155 on the first graded run, ten engines called (the firstborn's redemption and the stranger's death-mode row are Bamidbar's own, read by call, never retyped). The tape took twenty-five lines and no marker — the stretch is undated in the ink and on the shelf — with two one-day timers (\"tomorrow\", \"on the morrow\") firing the day after the running clock; the run tuple predicted and matched first run, the tape without Korach reproducing the previous sitting exactly, and the narrative prediction matching in all forty-two slots without a retype. Korach's own death stays an OPEN row (the earth's verse does not name him; the census's retelling does; the Talmud argues both ways). The two gates' first fails read and paid: the daemon gate reads one branch form only; the dependency gate's token census named six more engines and three pointers. 15:20's terumah pointer paid by a live call from the Shelach runner. Numbers 1 through 18 is read, frozen, compiled and on the tape. Next: chapter 19.\n")
rep('<repo-old>/THE_BRIEFING.md', "### 2026-09-10 — THE SHELF STOPS MID-ROW, AND THE INK RUNS ON CAIN'S VERSES",
    r'''### 2026-09-10 — THE PARSER'S CENSUS CATCHES YESTERDAY'S OWN MISTAKE, AND A PREDICTION MATCHES WHOLE

Sitting 5b compiled Numbers 16 to 18 on your "Go" (World/step9/NUMBERS_WALK.md
"Sitting 5b"). What changed, in plain words:

- **A parser rule is measured as a class, and the class's census re-reads the
  previous sitting.** The reading had found one gap ("THE fifty and two hundred"
  reading 200). Before the rule was typed, every article-bearing numeral in the
  Bible was listed with its neighbor. That list held three readings that had
  been wrong all along and nobody had asked about — including two that the
  previous sitting's own corpus diff had shown and the hand accepted. The rule
  now is: when a class is re-measured, the previous diff's rows in that class
  are reread, and a probe's expectation is typed from the class's own reading,
  not from the neighboring rule's shape (four of the hand's expectations were
  wrong the same way; the run read them).
- **The cantillation decides a number's cut for "the one" too.** "The one and
  twentieth day" joins; "in the one curtain, and fifty loops" does not — the
  difference is a joining mark against a dividing mark on the same word. The
  accent read (registered at Naso as M-26) has its second exemplar.
- **A prediction can match whole.** The tape's narrative tuple — forty-two
  slots — matched on the first run with no retype, the first time in the walk,
  because the timer lesson from the previous sitting was applied before the
  prediction was typed. The run tuple and the tape-minus-the-newest-runner test
  matched first run as well.
- **The gates keep teaching the machine's own grammar.** The daemon gate reads
  one branch form and kind names of letters and underscores — two of my branch
  forms leaked effects into the wrong kind and a name with a digit read as
  unresolved. The dependency gate's token census named six engines the span
  touches that the design had not listed; each was read and filed, with the
  homographs named inside the rows (16:26's "their sins" beside 18:9's sin
  offering).
- **What stays open, honestly.** Korach's own death is an OPEN row on the ledger:
  the verse of the earth's mouth names "every person who belonged to Korach"
  and not Korach; the census's retelling adds "and Korach"; the Talmud argues
  both ways. The checkpoint records the divergence rather than choosing.

### 2026-09-10 — THE SHELF STOPS MID-ROW, AND THE INK RUNS ON CAIN'S VERSES''')
print('records written: NUMBERS_WALK as-built, RESEARCH_LOG, MOVE_CATALOG, the docket correction, THE_STEPS, COMPILE_DEBT, RESUME, THE_BRIEFING')
