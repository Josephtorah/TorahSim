# THE SANCTUARY SPEC GRADED AGAINST ITS OWN CONSTRUCTION RUN — sitting E2 of THE COMPILE DEBT (Exod 25:1-27:21 the SPEC;
# Exod 35:30-38:31 the RUN). 2026-09-06 (owner: "go e2"): six frozen units in ONE runner — World/step9/cold_run_sanctuary_build.py,
# 257 of 257 ON THE FIRST GRADED RUN; the fifth runner compiled under THE DEPENDENCY GATE's rule (the span declared, a stub placed,
# `dependency_census.py --emit` run, three required edges and two pointers dispositioned BEFORE the first cell, four more declared
# for the live calls the compile made) — and the gate's VOCABULARY EXTENDED: the run builds the incense altar, the laver, the
# anointing oil, and counts the half-shekel silver, whose spec is Exod 30 (E4); the census could not see them, so four type
# tokens were added (incense, laver, shekel, anointing oil — home cold_run_incense_shekel.py) and the edge dispositioned OWED:
# `--debt` now prints ONE owed edge, honestly, until E4 compiles the callee.

## The headline
THE RUN BUILDS THE HOUSE BEFORE THE ARK, AND THE TRADITION SAYS THE RUN IS RIGHT. The spec writes the vessels first — the ark at
25:10, the table, the lampstand — and the house after (the curtains at 26:1); the run builds the curtains first (36:8), the boards,
the veil, and reaches the ark only at 37:1. No verse of either stratum explains the reversal, so the gap was taken to the Talmud per
gap: Berakhot 55a:12 — God told Moses 'make Me a TABERNACLE, an ARK, and VESSELS'; Moses went and REVERSED it; Bezalel: 'the custom
of the world is that a man builds a house and then brings vessels into it... perhaps the Holy One said tabernacle, ark, vessels?' —
'perhaps you were in God's shadow and knew.' The RUN's order is the original command; the SPEC's written order is the messenger's
inversion. The spine's recension (Midrash — midrash: "expounding" — Tanchuma, Vayakhel 6:5; Buber 8:3) carries the roles REVERSED — Bezalel ark-first against
Moses house-first — a two-recension dispute over which scheduling argument the exchange carried; both tracks carried, the ink of
36-37 beside them. Move M-22 (the run read back into the spec) takes a new form: at D8 the run gave the spec a COLUMN; here the run
gives the spec its ORDER.

Beside it, THE RUN IS THE MAKING ALONE. The alignment engine matched every run verse to its spec verse by normalized token overlap,
block by block: 89 spec verses, 74 run verses, 65 spec matched, 24 dropped — and the dropped are of one kind: every clause that
USES a vessel (the staves never removed, the testimony put in, the meeting at the cover, the bread set, the lamps lit, the veil
dividing, the placements north and south, the oil) and every SHOWN-PATTERN clause (four seats, each phrase once in the Bible). What
the run ADDS is as telling: 'the overlay of their heads silver' at 38:17 and 38:19 with no 'their heads' anywhere in Exod 27, and
38:28's accounts confirming it; the lamps counted in the making verse; 'one to one' at five seats where the spec wrote 'a woman to
her sister' at five — the construction chapters replace the kinship idiom with the numeral at every seat; and ONE named maker among
thirty-seven subjectless 'and he made' — 'and Bezalel made the ark' (the spine: his hands on the ark alone).

AND THE ARITHMETIC CLOSES FROM THE INK ALONE. Ten curtains of four cubits = forty = the tabernacle's thirty (twenty boards of a
cubit and a half) plus its ten of height; eleven goat-hair curtains of four = forty-four, the extra four exactly 26:9's doubled front
and 26:12's hanging half; thirty against twenty-eight exactly 26:13's cubit on each side — the spec's own overhang clauses verified
by its numbers (and those two clauses are what the run drops). Ninety-six sockets under the boards (forty, forty, sixteen — the
ink's own sum) plus the veil's four = the accounts' hundred, 'a talent a socket' a hapax. The court: two hundred and eighty cubits
of hangings plus the twenty-cubit screen = three hundred = the perimeter; sixty pillars; five thousand square cubits whose root is
Eruvin 2:5's 'seventy and a remainder'. THE TALENT COMPUTED: 603,550 half-shekels = 301,775 shekels = a hundred talents and 1,775,
so a talent = 3,000 shekels — no tradition consulted; the bronze's 2,400 = ninety-six maneh of twenty-five, and Bekhorot 5a:18
(credited) reads the refusal to round as the sanctuary maneh doubled. The veil under the clasps at twenty cubits makes the Holy of
Holies a cube of ten; Solomon's inmost room is a cube of twenty (1 Kgs 6:20) — the tabernacle doubled. The table's two cubits by one
under Kelim 17:10's two cubits (five and six handbreadths) reproduce Menachot 11:5's two arms by the same two names.

## The docket (motion 2 — the ledger first)
logic/oral_triage/sanctuary_build_docket_2026-09-06.md (scratchpad/gen_sanctuary_build_ledger.py): 109 rows = Mishnah Middot WHOLE
(34 — the descendant floor plan as DATA), Shekalim 4-6 (21 — the surplus law, the officers and the two-signatory rule, the thirteen
tables and the ark's hiding), Yoma 5 (7), Kelim 1 (9 — the ten sanctities), Menachot 11 and Tamid 3 (18 — read whole at L5, credited
and quick-looked) + ten topic rows (the cubit as data, Kelim 17:9-10; the three olives; the five who may not separate; the horns'
blood; the collector's dress; the veil's numbers; who pays the shekel; the thirty-nine labors' referent) + the ten link rows outside.
Coverage COMPUTED (missing 0, extra 0; 51 rows self-checked by a token). LAW 12 (fresh) / CREDIT 35 (verified by script) / DATA 9 /
ROUTED 11 / CONTEXT 42. 133 Talmud addresses indexed; 20 opened PER GAP with verdicts (Berakhot 55a:11-13 the order fork; Zevachim
59b:4-10, 60a:1-2 the altar's width-and-height fork; Menachot 96a:6-7, 96b:1, 97a:5 the table's faces and vessels; Menachot 28b:17,
29a:1-2 the lampstand's counts; Shabbat 96b:1-2 the carrying labor); 54 credited from the sanctuary block of round 26. Tosefta
enumerated (three on the shelf, not read).

## The census first (the gate)
Span declared (`sanctuary_build: 25:1-40, 26:1-37, 27:1-21, 35:30-35, 36:1-38, 37:1-29, 38:1-31`), a stub placed, `--emit` run:
THREE required edges — lev24 FALSE (eleven 'under' tokens, the spatial preposition), offerings CALL carries place (38:1's 'altar of
the burnt offering' — the run names the altar by its use, the spec never does; the blood geography by call; 25:37's and 27:20's
'cause to ascend' the verb, homographs), tzav CALL carries verdict (25:7's 'stones of setting' a homograph of the installation; the
live call the perpetual fire on the wooden altar — Tanchuma Terumah 11's objection) — and TWO pointers (26:30 'according to its
fashion' and 27:8 'as He showed you' — INTERNAL: the shown pattern). FOUR more declared for the live calls the compile made: chatat
(the upper bloods on the horns), priesthood (the lamp and the table at their law seat — one function at two seats), ordinances (the
ramp, the earth fill of the hollow box, the hewn ban). And the vocabulary extended (incense, laver, shekel, anointing oil → home
incense_shekel) with the edge OWED to E4's line. The gate after the run: 28 runners, 1260 verses, 26 type tokens, 68 edges + 48
pointers, 67 live edges, 82 edges + 46 pointers on file, ONE owed; the sweep 28 of 28 at 2365 cells.

## The five motions
(1) ink: 44 probes; 70 censuses as tripwires incl. the whole-Tanakh index (the four shown clauses each once; the pattern-word's
Torah seats the blueprint and Deut 4:16-18's image ban; 'and I will meet', 'not removed', 'and it shall divide' hapaxes; 'standing'
at two Torah seats; beaten work at eight; the crown's consonants at 28 seats mixing crown and stranger; 'square' at six; the altar
named 'of the burnt offering' first at 30:28; the base at no seat of the span and six of the offering code; the stamp at 0 verses of
36-38 and 14 of 39-40; 'and he made' 37 times with one named maker; the census number with Num 1:46, 2:32; 'a beka' with Gen 24:22;
'restrained' with Gen 8:2's rain; the assembling women with 1 Sam 2:22 in two spellings) and the ALIGNMENT ENGINE (block-wise
token matching; the order of first mention in each stratum). (2) 39 sheet rows verified by their own tokens. (3) 257 of 257 on
the first graded run. (4) 20 segments opened per gap, recorded in the ledger. (5) fractions 142 ink (55%) / 65 recorded (25%) /
26 answer-sheet / 6 data / 18 imports — the highest ink share of any runner, because the spec's cells are measures and the run's
are verbs.

## What compiled
Twelve functions: offering (35 cells — the three tokens, the five present, the segments, the plural making-verb, the dwell phrase,
the shown clauses, the extension constitution, the craftsmen's pay and the surplus's arms, the workforce, the two mornings, the halt
and the carrying labor, the surplus), ark (29 — the dimensions equal token for token, the named maker, three chests, the crown's
consonants, the staves and their lashes, the testimony and the meeting dropped, the cherubim, the whereabouts), table (19 — the
cubit reference and the two settings, faces, the frame, four vessels and the props, continually, the exchange and loaves by call,
thirteen tables), menorah (19 — the method fork as a parameter, no dimensions, 7/7/22/11/8+1, the western lamp by call), curtains
(23 — the arithmetic, the exposed cubit by the taper parameter, made one, the idiom shift, the tachash), boards (17 — 96 + 4,
twins, the taper fork, the middle bar, the interior, its halakhah), veil (17 — at twenty, the cube, Solomon's doubling, divides,
one or two, the ladder's three rungs, the floor plan, the heads added), altar (30 — the name, the red line by two calls, the base
by Leviticus, the indispensables, the ramp and earth fill by call, the perpetual fire, the fork of 59b), court (17 — the perimeter,
the area and its root, the silver heads, the descendant enclosures), lamp (11 — the thirteen tokens, the sons dropped, the oil
and grades by call), books (27 — the formula, two signatories, the talent, the balance, the sockets, the maneh, the mirrors' two
tracks, E4's tokens owed), build (13 — the two orders, the fork, the alignment, the dropped, the verbs, the metals, the scene).

## Effects (the registry 145 → 154)
set_apart_before_me, surplus_to_the_house (TRANSFER); presence_dwells, meeting_appointed (HEAVEN — PROMISED at the spec, UNFIRED:
the run stops at 38:31, the erection fires them at E5); staves_fixed, bringing_halted (BLOCK); made_one, veil_divides,
accounts_rendered (STATUS). scratchpad/add_effects_e2.py. THE SCENE on the world engine: two mornings brought (set apart), the
halt (the camp blocked), twelve vessels made — the curtains write made_one, the ark staves_fixed, the veil veil_divides, the rest
and E4's three write nothing — the accounts rendered and the surplus transferred; checkpoint (2, 1, 1, 1, 1, 1, 1, 0, 0, 17).

## Seats (scratchpad/seat_e2.py; 137 cites pre-checked as verdicted ledger rows; anchors checked — two moved to steps carrying
## operators lists: 26:1 for the curtains, 38:26 for the accounts)
EX25-15 (F-237) at STEP_Ex_25_10 — THE SPEC GRADED AGAINST ITS OWN CONSTRUCTION RUN. EX26-08 (F-238) at STEP_Ex_26_1 — THE
CURTAINS' ARITHMETIC CLOSES, THE HUNDRED SOCKETS, THE CUBE. EX27-11 (F-239) at STEP_Ex_27_5 — THE ALTAR'S BASE BY LEVITICUS AND
THE RED LINE BY CALL. EX36-09 (F-240) at STEP_Ex_36_6 — THE HALT AND THE SURPLUS. EX37-07 (F-241) at STEP_Ex_37_1 — BEZALEL'S ONE
VERB. EX38-09 (F-242) at STEP_Ex_38_26 — THE TALENT COMPUTED FROM THE CENSUS. Rituals COMPLETE ×6 (163 frozen units); verify 0
failed ×6; ALL_UNITS rebuilt; corpus_world standing 1746 → 1752, hash 8b8fff1fa28953af UNMOVED; gloss_lint 0 on the ledger, the
runner, the six units, the two registries, this report.

## Numbers
257/257 · guard 257 (the parser's count) · 44 probes · 70 censuses · 39 sheet rows · 109 docket rows · 20 Talmud segments opened
per gap · 9 effects · 6 seats · sweep 28/28 at 2365 cells · gate 68 edges + 48 pointers, 67 live, 1 owed (E4) · standing 1752 ·
hash unmoved · E2 checked off.
