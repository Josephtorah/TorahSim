# THE DEPENDENCY AUDIT — are the compiled spans calling each other where the ink points?
# 2026-09-06, on the owner's question ("how many of these have we missed during our compile?
# are we compiling correctly or overlooking all of these dependencies"), raised after the
# peer thread found Lev 5:10's "as prescribed" pointer standing as a note, not a call.
# Measured by script (scratchpad/pointer_census.py, pointer_deps2.py), verified by hand at
# every flagged seat. No code changed. Assessment only.

## The short answer
Three layers were measured. (1) The ink's EXPLICIT procedure pointers ("as prescribed",
"as he did with", "like the sin offering") that cross a runner boundary inside a compiled
span: SIX. None is fully live — one is a call into a callee that lacks the referenced
procedure, two are provenance notes, three are silent. (2) The IMPLICIT type-name
dependencies (a verse in runner A names an offering type or institution whose home is
runner B): 33 real edges after false positives were removed — 9 are live calls, 4 are
notes, 20 are silent. (3) SUB-SPANS never compiled inside spans marked done: four,
verified by token — and they are the reason most of the silent edges have nothing to call.
The process has no step that censuses a span's cross-references before compiling it;
every live call so far was wired where the answer sheet forced it (a Mishnah row naming
the other type), and the rest were left as notes or silence. The first-call standard
(Lev 24 into Exod 21) exists as a precedent, not as a gate.

## Layer 1 — the explicit pointers (68 verses censused in Exod 12-13, 20-40, Lev 1-27)
Forms scanned: כְּמִשְׁפָּט ("as prescribed / by the ordinance"), כַּאֲשֶׁר ("as / when" before a
procedure verb), the comparative kaf on an offering noun (כַּחַטָּאת "like the sin offering",
כָּאָשָׁם "like the guilt offering", כַּמִּנְחָה "like the meal offering"), תּוֹרָה אַחַת ("one law").
Of the 68: 27 are RUN CITATIONS ("as the LORD commanded Moses" — Exod 39-40 sixteen times,
Lev 8 seven times, Lev 9-10 four, 16:34, 24:23, 12:28, 12:50: the spec/run pairs the debt
already plans to grade at E2-E5, and Lev 8's run is the Tzav engine's scene 6); 20 are
non-pointers or same-runner internals (21:31's "as this judgment", 4:20-21's "as he did to
the first bull", 16:15's "as the bull's blood", 24:19-20's talion formula, כֹּפֶר "ransom"
matched by the kaf scan); 15 sit in spans not yet compiled (Exod 26:30, 27:8, 29:41, 40:15
— E2/E4/E5). The SIX that cross a runner boundary inside a compiled span:

| # | verse | pointer | target | runner | status |
|---|---|---|---|---|---|
| 1 | Exod 23:15 | כַּאֲשֶׁר צִוִּיתִךָ "as I commanded you" (the matzah) | Exod 12:15-20, 13:6-7 (pesach) | calendar | SILENT — calendar imports nothing |
| 2 | Lev 4:10, 4:26, 4:31, 4:35 | "as it is lifted from the ox / the goat / the lamb of the peace offering" | Lev 3:3-4, 3:9-10, 3:14-15 (the fat inventory; the lamb's fat tail at 3:9) | chatat | CALL INTO AN EMPTY SEAT — chatat calls offerings.dispatch('shelamim'), but the callee returns place, applications, eater, eat-place, window, raised: NO fat list; Lev 3:3-17 is cited by no cell in any runner |
| 3 | Lev 5:10 | כַּמִּשְׁפָּט "as prescribed" (the second bird as a burnt offering) | Lev 1:14-17 (minchah.bird) | vayikra5 | NOTE — "the ink's own POINTER to the bird-olah rite" in the reason text; no call (the call runs the other way, minchah into vayikra5) |
| 4 | Lev 5:13 | כַּמִּנְחָה "as the meal offering" (the remainder to the priest) | Lev 2:3, 2:10 (minchah) | vayikra5 | SILENT — no cell, no Lev 2 address in the source |
| 5 | Lev 10:15, 10:18 | כַּאֲשֶׁר צִוִּיתִי "as I commanded" (breast and thigh; the eaten sin offering) | Lev 7:30-34; 6:19, 6:23 (tzav) | chatat | NOTE — fourteen Lev 6/7 addresses in the reasons, no call into tzav |
| 6 | Lev 14:13 | כַּחַטָּאת הָאָשָׁם הוּא "as the sin offering, so the guilt offering" (slaughtered in the north) | Lev 1:11, 4:24, 6:18, 7:2 | negaim | SILENT — and the whole of 14:1-32 is uncompiled (layer 3) |

Beside them, Lev 9:16's כַּמִּשְׁפָּט (Aaron's burnt offering "as prescribed") is Lev 9 citing
Lev 1 as its spec: the eighth-day narrative is the RUN of Leviticus 1-4, the same
demonstrate-by-run shape E2/E3 grade for the sanctuary. COMPILE_DEBT lists lev_09 as
"narrative, no function owed"; it is a candidate line item (spec vs run inside one book).

## Layer 2 — the implicit type dependencies
Tokens scanned per verse of every compiled span, each mapped to its home runner: burnt
offering (עֹלָה), the bird pair (תֹּרִים / בְּנֵי יוֹנָה "turtledoves / young pigeons"), meal
offering (מִנְחָה), peace offering (שְׁלָמִים), sin offering (חַטָּאת), guilt offering (אָשָׁם),
Passover (פֶּסַח), firstborn (בְּכוֹר), tithe (מַעֲשֵׂר), valuation (עֶרְכְּךָ), jubilee (יֹבֵל), the
seventh year, installation (מִלֻּאִים), leprosy (צָרַעַת), the discharger (זָב), the menstruant
(נִדָּה), interest (נֶשֶׁךְ / תַּרְבִּית), the Hebrew slave, the ghost and familiar spirit, the
talion formula (תַּחַת "for"). 43 edges by token; 10 removed by hand as false positives
(עָלָה "went up / a leaf" at Exod 12:38 and Lev 26:36; תַּחַת "under / in place of" at 14:42,
16:32, 27:32; שְׁלֹמִית the name at 24:11; בִּכּוּרִים "first fruits" is not the firstborn at
23:16, 23:19, 2:14, 23:17, 23:20; וְאָשְׁמוּ "and they are guilty" at 4:13; הַשְּׁבִיעִת "the
seventh [sabbath]" at 23:16). The 33 real edges:

LIVE (9): mishpatim → lev24 (talion, 8 verses); chatat → offerings, minchah, vayikra5;
clocks → chatat, minchah (the bird pair), vayikra5; sanctions → clocks (the menstruant at
18:19, 20:21); temurah → yovel (tithe, valuation, 7 verses), temurah → pesach (the
firstling at 27:26). Not caught by the token scan but live: offerings → pesach (the
Zevachim 5 paschal row), minchah → vayikra5 (the sinner's adjuncts), holiness → tzav,
vayikra5, yovel, sanctions → chatat, shemini.
NOTES (4): minchah → offerings (the bird burnt offering under Lev 1's frame); clocks →
offerings (the childbirth LAMB burnt offering, 12:6 — the bird is called, the lamb is
noted); chatat → tzav (layer 1 #5); yovel → calendar (the seventh year, one Exod 23 cite).
SILENT (20), clustered in six runners:
- tzav imports NOTHING, and its only importer is holiness (the peace offering's window at
  19:5-8) — while naming the burnt, meal, sin, peace, and guilt offerings at more than
  thirty verses (6:2-6 the burnt offering's law, 6:7-16 the meal offering's, 6:17-23 the
  sin offering's, 7:1-7 the guilt offering's, 7:11-34 the peace offering's). The Lev 1-8
  engine is FIVE runners (offerings, minchah, chatat, vayikra5, tzav) with calls among
  four of them and none between the fifth and the other four. (Corrected 2026-09-06: the
  first draft of this line said "zero importers"; the holiness call was missed.)
- yoma: the bull and goat sin offerings whose blood enters (16:3-27) are Lev 4:5-12's
  inner-altar procedure, 6:23's burn-not-eat, and 4:12/4:21's "outside the camp" (16:27
  names it) — chatat.py already holds the effect burned_outside_camp; the two rams (16:3,
  5, 24) are Lev 1:10's flock burnt offering. No call.
- negaim: the cleansed leper's eighth day (14:10-32) names the guilt, sin, burnt, and meal
  offerings and the bird pair — nothing to call from, because the sub-span is uncompiled.
- moadim: 23:5 "the LORD's Passover" never calls the Passover engine (offerings.py did,
  for Zevachim 5's row); 23:12-13 and 23:18-19 name the omer's lamb and Shavuot's seven
  lambs, bull, two rams, goat sin offering, two lambs peace offering; 23:37 the general
  offering clause. The omer lamb's meal offering IS compiled from 23:13's ink; the
  animals are not.
- vayikra5, the earliest Leviticus compile (09-03): its graded sin offering (5:6-13, the
  female lamb or goat) IS Lev 4:27-35's procedure; its guilt offering cases (5:14-26) run
  on 7:1-7's procedure; its bird pair (5:7-10) on minchah.bird(). Every later engine calls
  INTO vayikra5; vayikra5 calls nothing, because nothing existed when it was written.
- calendar: 23:15 → pesach (layer 1 #1); 23:10-11 the seventh year ↔ yovel 25:1-7.
- sanctions: 17:5 (profane slaughter converted to peace offerings) and 17:8 (a burnt
  offering outside) name the types without calling offerings — the ban's verdict does not
  need the procedure; recorded as minor.

FOUR INSTITUTIONS COMPILED TWICE WITH NO CALL EITHER WAY: the seventh year (calendar
23:10-11 / yovel 25:1-7); the first fruits (calendar 23:16, 23:19 / moadim 23:17, 23:20);
the omer (minchah 2:14 / moadim 23:9-14); the Day's fast (yoma 16:29-31 / moadim
23:27-32). E5 already plans Exod 34's repeats "as the same functions called twice"; the
rule was never applied backward to these four.

## Layer 3 — sub-spans uncompiled inside spans marked done (verified by token, not by address)
- negaim: Lev 14:1-32, the leper's cleansing — the two birds, cedar, scarlet, hyssop, the
  living water, the shaving twice, the seven days, the eighth day's guilt offering with the
  log of oil on the right ear-lobe, thumb, and toe, the sin, burnt, and meal offerings, the
  poor man's scale. The runner holds the six-track state machine (Lev 13) and the ten
  houses (14:33-53); 14:37-45 are its only chapter-14 addresses.
- offerings: Lev 3:3-17, the peace offering's fat inventory (the fat covering the entrails,
  the two kidneys with their fat on the loins, the lobe of the liver, and the lamb's
  whole fat tail "close by the backbone") — the target of four pointers from Lev 4.
- tzav: Lev 7:1-7 (the guilt offering's law: north, the blood around, the fat parts, eaten
  by the priests' males in the holy place, "as the sin offering") and 6:7-11 (the meal
  offering's law: the fistful, the remainder unleavened in the holy place). The runner's
  six machines (altar, vessel purge, chavitin, rejection, karet, dues) and the
  installation cover the rest.
- moadim: Lev 23:18-19, Shavuot's animal offerings (seven lambs, one bull, two rams, a
  goat sin offering, two lambs peace offering with the loaves).
Checked and CLEARED (the address proxy under-reported them; the tokens are compiled):
shemini's contact impurity 11:24-40, yovel's land redemption 25:23-28, mishpatim's pit
and fire (cited as the range "21:28-22:5"), pesach's firstborn 13:13.

## Are we compiling correctly?
The five motions are executed per span and the honest-pairing guard holds every runner.
What is missing is a step: motion (1) compiles the span's ink but never CENSUSES the
span's cross-references, so a dependency becomes a call only when a Mishnah row happens
to name the other type. The measured result: 0 of 6 explicit pointers fully live; 20 of
33 type edges silent; one call resolving into a callee that lacks the referenced
procedure; one runner an island; four institutions compiled twice; four sub-spans
uncompiled behind a check mark. The peer thread's bird-olah question was one instance of
a pattern, and the pattern is systematic, not occasional.

## What would close it (the owner's call; nothing done at the time of the audit)
1. A GATE, not a habit: the pointer census (pointer_deps2.py, moved into World/step9 and
   run by run_cold_all) prints every cross-runner edge a span's ink requires and fails
   when an edge is SILENT without a recorded disposition — CALL (live), OWED (the callee
   is not compiled yet: a COMPILE_DEBT line), or PARAMETER (the ink points to a quantity,
   not a procedure). Motion (1) gains the sentence "census the span's pointers first."
2. A repair sitting before L4b or after L5 — THE DEPENDENCY DEBT: compile the four
   sub-spans (Lev 3:3-17, 7:1-7 with 6:7-11, 14:1-32, 23:18-19), wire the six pointers
   as live calls, give tzav its imports and importers (the Lev 1-8 engine becomes one
   call graph), unify the four twice-compiled institutions as one function called twice.
3. COMPILE_DEBT.md line items for the four sub-spans and for Lev 9 as the run of Lev 1-4.

## THE REPAIR — done the same day (the owner: "can we fix all of the overlooked sections,
## then make sure we code properly going forward")
**The ledger first.** logic/oral_triage/dependency_debt_docket_2026-09-06.md — 59 rows:
Mishnah Negaim 14, Tamid 4, and Chullin 8 read WHOLE (22) with the 26 link rows on the four
sub-spans and the topic rows (37 outside); coverage computed against the shelf (missing 0,
extra 0); LAW 11 / CREDIT 34 (every one verified by script) / ROUTED 10 / CONTEXT 4; 368
Talmud addresses indexed and none opened.
**The four sub-spans compiled.**
- Lev 3:3-17 THE FAT INVENTORY into cold_run_offerings.py (45 → 57 cells, 54% ink): the
  parts read per species from each species' own verses; the fat-tail token at exactly two
  seats of Leviticus 1-8 (3:9 the lamb, 7:3 the ram) — the ox and the goat (its own
  paragraph, Sifra Nedavah Chapter 20 1) have none; 'all fat is the LORD's' as the reason
  sacrilege rides the fat (Chullin 8:6); the ban's species (7:23), karet (7:25), lashes
  (Makkot 3:2), all dwellings (3:17).
- Lev 7:1-7 THE GUILT OFFERING'S LAW and 6:7-11 THE MEAL OFFERING'S LAW into
  cold_run_tzav.py (33 → 53 cells): the asham's place, blood, and eater by call into the
  offerings row (north, two-that-are-four, male priests); its fat list graded against the
  lamb's by call and matching part for part; 'one law' (Chapter 9 1); Zevachim 8:11's
  three-way dispute carried; wrong intent stays fit by 7:5's 'it' after the smoking; the
  leper's blood below (Section 5 1-2); the meal offering's fistful and remainder by call
  into the meal-offering engine (Menachot 6:1 lists the sinner's — Lev 5:13's pointer).
  The Tzav runner, which imported nothing, now imports the offerings and meal-offering
  engines.
- Lev 14:1-32 THE LEPER'S CLEANSING — a new runner, cold_run_metzora.py, 77 of 77 ON THE
  FIRST GRADED RUN (27% ink / 28% moves / 21 answer-sheet / 3 data / 10 imports): the day
  and the priest, the kit of four with the coupled fates and the quarter-log (data), the
  seven sprinklings, the sending geography, the first shave and the week outside his tent
  (his wife), the second shave's three sites and 'all his hair' twice, THE THREE PURITIES
  on the purity verb's four seats (14:7, 8, 9, 20), the eighth day — the asham waved alive
  with its log, north by call, most holy and blood-below by call into the Tzav engine,
  the three right members (the census: 'the right' at six verses, the priest's right FINGER
  at 16 and 27 corrected the compiler's own draft), the oil on the blood's PLACE, the
  head-oil dispute, the sin offering (the commoner's animal by call) then the burnt
  offering (by call), the poor scale sampled at the asham (Section 4 13; Negaim 14:11),
  the reach-forms censused. Five engines called.
- Lev 23:18-19 SHAVUOT'S ANIMALS into cold_run_moadim.py (24 → 41 cells): the three kinds
  by their numerals; the burnt offerings, the goat, and the two lambs by call — the lambs
  resolving to the COMMUNAL peace offering's row (most holy, north, male priests), which
  23:20's 'holy to the LORD, for the PRIEST' states; the waving geometry; the bread and
  the lambs (Menachot 4:3); the two sets (Emor Chapter 13 6). Plus the Passover of 23:5,
  the omer's lamb, and the first fruits by call.
**The six pointers, live.** Exod 23:15 → the Passover engine (calendar.matzah); Lev 4:10,
4:26, 4:31, 4:35 → the fat inventory (chatat.fat — THE POINTER NAMES THE SPECIES: the
lamb's tail comes with 4:35, not with 4:10's ox); 5:10 → minchah.bird; 5:13 →
minchah.remainder; 10:15 → tzav.dues_machine; 14:13 → tzav.asham_law. The Lev 5 engine,
which every later engine called and which called nothing, now calls the sin-offering,
meal-offering, and Tzav engines through function-local imports.
**The four duplicates, one function at two seats.** calendar.sabbatical → yovel.sabbatical
(Exod 23:10-11 = Lev 25:1-7); moadim → calendar.first_fruits and pilgrimage (Lev 23:17-20 =
Exod 23:16-19); moadim → minchah.omer (Lev 23:9-14 = Lev 2:14); yoma → moadim.yom_kippur
(Lev 16:29-31 = Lev 23:27-32). Also wired: yoma → offerings (the inner sin offerings, the
rams) and chatat (the burnt pair); sanctions → offerings (17:5, 17:8); clocks → offerings
(the lamb of 12:6); minchah → offerings (the bird under Lev 1's frame).
**The gate.** World/step9/dependency_census.py with dependency_dispositions.yaml, run
FIRST by run_cold_all.py: 23 runners declared their spans; 905 verses scanned for 22 type
tokens and 5 pointer forms; 48 required edges and 42 required pointers, every one
dispositioned (CALL verified live against the source / OWED naming a debt line / REVERSE
verified / VIA verified / PARAMETER / INTERNAL / RUN_CITATION / FALSE with the homograph
named); 40 live import edges; a live edge the file understates fails. Three homograph
classes the census itself surfaced and the file now names: 'commandments' for 'unleavened
bread' (Lev 4:2, 26:14), 'first fruits' for 'firstborn', 'the seventh sabbath' for 'the
seventh year' (23:16), and the prepositions 'under / in place of / for' for the talion
formula (14:42, 16:32, 21:26, 27:32).
**Effects (109 → 117).** smoked_to_the_lord (HEAVEN), sprinkled_seven, shaved_whole,
oil_on_the_blood (BODY), sent_over_the_field (TRANSFER), outside_his_tent (TIMER),
declared_pure, waved (STATUS).
**Seats.** F-217 L04-20 (lev_04_inadvertence_case_tree, 4:35), F-218 LV14A-08
(lev_14_metzora_cleanse, 14:8), F-219 LV07A-07 (lev_07_asham_procedure, 7:7), F-220
LV23A-14 (lev_23_spring_festivals, 23:20), F-221 LV03-11 (lev_03_shelamim, 3:9).
**Numbers.** run_cold_all 23/23 runners, 1297 → 1444 cells; the guard tripwires moved with
the tables (offerings 45 → 57, tzav 33 → 53, chatat 187 → 194, vayikra5 27 → 31, calendar
14 → 16, moadim 24 → 41 with the guard newly wired, yoma 18 → 22, metzora 77 new); the
percent rewriter lifted 22 formats across nine runners before their first runs.
## THE CONSENSUS (2026-09-06, the two-thread design discussion the owner ordered; ruled "your call")
The other thread proposed a late-binding registry (every span registers its exports under a
stable name; callers resolve at call time), typed edges generated FROM the code, raising stubs
for uncompiled callees, and named the daemon gap as the real campaign. It withdrew the
registry-as-runtime on two points: (a) a raw import runs the callee's own grading at load, so
a regressed or missing callee fails the CALLER before it grades a cell, where late binding
defers that to runtime and lets a caller pass every cell that never exercises the missing
key; (b) the gate derives the REQUIRED edges from the ink and checks the code against them in
both directions — generating from code alone cannot find a silent edge, and the twenty
silent edges were the proof. Consensus, adopted on my call: (1) imports plus the ink-driven
gate stay the mechanism; (2) the ungated `carries:` field (value / count / procedure /
status / window / place / inventory / verdict — the scroll's own distinction between a
fetched number and a censused count, kept beside the verified kind, while the cell's
provenance tag is where the honest fractions count an import) and the `--debt` listing (the
OWED edges printed as the worklist — today none) — BUILT; (3) LATE binding reserved per
proven cycle, its own disposition kind, verified like CALL — not built, no cycle exists; (4)
a generated index, World/step9/DEPENDENCY_INDEX.md, written by the gate each run from the
dispositions and the live scan, documentation and the site's dependency view only, never a
runtime path — BUILT; (5) the daemon campaign is its own future order. THE RIDER for that
campaign (recorded as COMPILE_DEBT D9): a daemon's trigger events and emitted effects deserve
the same census-and-disposition treatment as these edges — the effects registry is the
emitted half, the trigger-event vocabulary the unbuilt half.
**What stays open.** Lev 9 as the run of Lev 1-4 (COMPILE_DEBT D8 — one short sitting after
L5, on my recommendation); the
advisory list of verses no address cites is printed by the gate each sweep and not gated
(address styles vary); the vocabulary of type tokens grows as Numbers and Deuteronomy
bring theirs (the tithe of Deut 14, the nazirite, the red heifer, the cities of refuge).
