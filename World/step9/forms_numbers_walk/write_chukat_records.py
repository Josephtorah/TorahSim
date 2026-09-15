import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE NUMBERS WALK sitting 6 — CHUKAT (2026-09-11): THE RECORDS, written once, after the rituals and the corpus bake — gated on the
# fold's PREDICTED numbers read back from CORPUS_TRUTH (units 196, standing 2023) and on the chain log's three RITUAL COMPLETE lines.
# Every insertion checks its anchor and its absence first (append-only; never twice).
import re, os, sys
ROOT = _ROOT
SP = os.path.dirname(os.path.abspath(__file__))
MEM = '<memory>'
truth = open(f'{ROOT}/logic/corpus/CORPUS_TRUTH.py', encoding='utf-8').read()
assert 'assert len(W["units"]) == 196' in truth and 'assert len(W["standing"]) == 2023' in truth, 'the fold is not at the predicted numbers — read the bake before writing records'
log = open(f'{SP}/chukat_chain.log', encoding='utf-8').read()
assert 'ALL_DONE' in log and 'SEAT FAILED' not in log, log[-600:]
rit = ''.join(open(f'{SP}/chukat_ritual_{u}.out', encoding='utf-8').read() for u in ('num_19_parah', 'num_20_meribah_edom_aaron', 'num_21_snakes_conquest'))
assert rit.count('RITUAL COMPLETE for') == 3 and '(194 frozen units)' in rit and '(195 frozen units)' in rit and '(196 frozen units)' in rit
bake = open(f'{SP}/chukat_corpus_bake.out', encoding='utf-8').read()
U = re.search(r'THE WORLD — (\d+) units', bake).group(1)
FA, EV, NA, ST = re.search(r'facts (\d+) · events (\d+) · names (\d+) · standing (\d+)', bake).groups()
DE, DO = re.search(r'demands (\d+): .*?, (\d+) OPEN', bake).groups()
HS = re.search(r'state hash (\w+)', bake).group(1)
assert 'CORPUS TRUTH GREEN' in bake
assert (U, ST) == ('196', '2023'), (U, ST)
FOLD = f'units {U}, facts {FA}, demands {DE} ({DO} open), events {EV}, names {NA}, standing {ST}, hash {HS}'
print('FOLD', FOLD)

def insert_before(path, anchor, text, marker):
    s = open(path, encoding='utf-8').read()
    assert marker not in s, (path, marker)
    assert s.count(anchor) == 1, (path, anchor[:60], s.count(anchor))
    open(path, 'w', encoding='utf-8').write(s.replace(anchor, text + anchor)); print('inserted into', path)
def insert_after(path, anchor, text, marker):
    s = open(path, encoding='utf-8').read()
    assert marker not in s, (path, marker)
    assert s.count(anchor) == 1, (path, anchor[:60], s.count(anchor))
    open(path, 'w', encoding='utf-8').write(s.replace(anchor, anchor + text)); print('inserted into', path)
def append(path, text, marker):
    s = open(path, encoding='utf-8').read()
    assert marker not in s, (path, marker)
    open(path, 'a', encoding='utf-8').write(text); print('appended to', path)

# ---- THE STAMP ROW ----
append(f'{ROOT}/logic/findings/STAMP_LEDGER.md',
       "| 2026-09-11 | num_19_parah, num_20_meribah_edom_aaron, num_21_snakes_conquest | DELEGATED | FULL RULE | Numbers 19:1-21:35 derivation 2026-09-11 (THE NUMBERS WALK sitting 6 — CHUKAT; the owner: \"Go\" after the #127 rereads, on the ruling READ THEN COMPILE; the THIRTY-FIRST through THIRTY-THIRD NUMBERS UNITS, read at the PARASHAH GRAIN in one pass, the ledgers per block; the portion's last verse 22:1 opens the next draft and is read with it): declared reading COMPLETE on every block — Onkelos Numbers 19, 20, 21 whole, 86 verses (22 / 29 / 35), and the Sifrei on Numbers piskaot 123-130 FOUND BY POSITION (19 rows at the shelf's row grain; NO piska on chapters 20-24 — computed on every head of the export, the shelf's silence on the two narrative chapters as on the spies and the rebellion; every head of 123-130 in order, none mistyped; the export's ENGLISH reverses 123's frame against its own Hebrew row — RESEARCH_LOG.md; no prior ledger had read any of the 19 or the 86); coverage COMPUTED by script against the shelf's own row counts, 105 of 105, missing 0, extra 0; the ink facts computed (chukat_ink.py — 0 failing asserts after the measurement pass, thirty-two on the first typed pass, each a measurement; the parser measured RIGHT at five verses, SILENT on the date-ordinals — a class named and left — and ONE GAP, the dual \"twice\" of 20:11 by the patach); 34 claims (CH19A ×12, CH20A ×10, CH21A ×12) with every check cut from the store's bytes — verify_claims 34 VERIFIED / 0 FAILED, claim_labels_census --strict GREEN (Numbers 245 labeled 245, debt 0); 34 WITNESS_READ operators seated at the claims' first verses (seat_chukat.py, step E, the scenarios in the anchor form); verify_text GREEN ×3; three rituals COMPLETE — 194, 195, 196 frozen units; the corpus refolded " + FOLD + " — the fold PREDICTED before it ran (units 196, standing 1989 + 34 = 2023, the rest unmoved) and matched; CORPUS TRUTH GREEN. Delegated under the 2026-09-01 stamp delegation; the owner may overrule. |\n",
       '| 2026-09-11 | num_19_parah, num_20_meribah_edom_aaron, num_21_snakes_conquest |')

# ---- MIDDOT.md: the Sifrei's own case law on the heifer ----
MIDDOT = """- THE SIFREI'S OWN CASE LAW ON CHUKAT (the Sifrei on Numbers piskaot
  123-130 on the heifer, THE NUMBERS WALK sitting 6, 2026-09-11 — the
  ledger logic/oral_triage/num_19_parah_2026-09-11.md): (1) THE
  A-FORTIORI'S FULL PROTOCOL RUN THREE TIMES IN ONE CHAPTER, its formula
  verbatim — "I have reasoned a fortiori and I have transposed; the
  transposition has been refuted and I return to the original": on the
  yoke and the other labors (123:1, the heifer against the eglah arufah),
  on the sheretz and "that shall die" (125:1 — the dead confers no tumah
  until dead, the lighter the less), on the grave's open sides (126:1,
  the tent the paradigm) — the protocol the Korach sitting recorded on one
  clause is the chapter's standing instrument (I1 with reversal and
  refutation). (2) "A DERIVATION FROM A DERIVATION?" (127:4) — the bar on
  second-hand paradigms stated as a question when the open grave's
  evening tumah would be learned from the tent's, itself an a-fortiori:
  the Korach sitting's "you would learn from what is itself learned?"
  (118:1) at its second seat in the walk. (3) A VERDICT BY ELIMINATION
  (129:5): the sprinkler graver than the toucher — three rival readings
  (sprinkler/toucher, clean/unclean, fit/unfit) each REFUSED by an
  a-fortiori, "you must perforce accept the first": the water's measure —
  the a-fortiori used as the exclusion tool, not the derivation tool. (4)
  THE IDENTITY LICENSED BY A DEPARTED WORD (127:5, R. Shimon): "is it
  earth? is it not ashes? Scripture departs from its usual meaning to
  formulate an identity" — "earth" at 19:17 against "ashes" at 19:9-10,
  measured on the tokens: the gezerah shavah's mufneh condition met by a
  word the text changed on purpose (I2's license named on the ink's own
  delta, as the Korach sitting's "from it"). (5) THE SAME CLAUSE READ
  NARROW AND WIDE (125:1): "the soul of a man" EXCLUDES the blood (R.
  Yishmael), "ALL the soul of a man" INCLUDES it (R. Akiva) — I4 against
  I5 on one phrase, the dispute carried. (6) THE SECTION'S SHAPE NAMED ON
  THE OPENING (123:1): general at the head ("the statute of the Torah"),
  particular after ("a red heifer, whole"), with Exod 19:3-6 and 12:43 as
  the two other shapes and the rule stated — "there exists in the general
  only what is found in the particular" (the Korach sitting's "general at
  both ends" its sibling). (7) THE PUNISHMENT SPLIT BY TWO VERSES (125:1,
  129:3): "if he is not cleansed on the third day he shall not be clean
  on the seventh" gives the omission's punishment — uncleanness, not
  karet — and 19:20's karet is for entering the sanctuary: two effects
  read off two clauses, the compile's two verdicts. (8) THE THIRD VERSE
  FIXING THE SCHEDULE (125:1, 129:2): 19:12's "third and seventh" might
  read "if on the third, clean on the seventh"; 19:19's "and he shall
  cleanse him ON THE SEVENTH DAY" repeats to void it — I13's form on a
  timer. (9) THE TEACHER'S DELIBERATE ERROR (123:1): R. Yochanan b.
  Zakkai's "golden vestments" against his own teaching of the white,
  "to strengthen the disciples" — a recorded pedagogic falsehood, the
  tradition naming its own device. (10) THE ACADEMY'S DISPUTE READ AS A
  VISION (124:1): the cow that drank the waters — thirty-two elders, R.
  Yossi HaGelili's return, and R. Tarfon reading Daniel 8:4-7 with the
  ram as R. Akiva and the goat as R. Yossi — the shelf's aggadah (the
  lore, not the law) verdicted with the law it sits on. (11) TWO BONES AT
  TWO SEATS (127:2, 129:1): "the bone of a man" (19:16) the limb from the
  living, "him who touched a bone" (19:18) the barley-corn — and the ink
  REORDERS the four sources between the two verses, the bone moved to
  the head (computed). (12) THE VESSEL CENSUS BY THREE VERSES (126:1):
  "all that is in the tent" bounded by 19:18's "vessels", Num 31:20's four,
  31:22's metal and 19:15's earthenware — six classes, and "whatever is
  subject to cleansing is subject to tumah" as the closing rule. No new
  move; MOVE_CATALOG unchanged.
"""
insert_before(f'{ROOT}/logic/MIDDOT.md', "\n## Exodus block campaign — owner's word \"Do 3\")", MIDDOT, "THE SIFREI'S OWN CASE LAW ON CHUKAT")

# ---- RESEARCH_LOG.md ----
RL = """

## 2026-09-11 — THE EXPORT'S ENGLISH REVERSES A FRAME, THE DATE-ORDINALS ARE SILENT, THE DUAL "TWICE"
## IS A HOMOGRAPH OF "TIMES", AND ONE CONSONANTAL SKIN HOLDS MIRIAM, THE BITTER WATERS AND THE REBELS
## (THE NUMBERS WALK sitting 6 — Chukat's reading)

(1) THE SIFREI ON NUMBERS HAS EIGHT PISKAOT ON CHAPTER 19 AND NONE ON 20-24 — asserted on
every head of the export: 123 on 19:1 (headed "19:1-2"), 124 on 19:5, 125 on 19:11, 126 on
19:14, 127 on 19:16, 128 on 19:17, 129 on 19:18, 130 on 19:22, every head in order, none
mistyped; the next head, 131, is Balak's close at 25:1. Miriam's death, Meribah, Edom,
Aaron's death, Arad, the serpents, the well, Sihon and Og are read on Onkelos alone — the
walk's third whole-narrative stretch without the spine (13-14, 16-17, 20-24).

(2) A NEW DEFECT CLASS IN THE EXPORT: THE TRANSLATOR REVERSES THE FRAME'S ADDRESSEES. Piska
123:1's English opens "And the L-rd spoke to Aaron and to Moses"; the export's own Hebrew
row (he.json, the same piska and row) reads "and the LORD spoke to Moses and Aaron", as the
verse does (19:1: to Moses and to Aaron — computed on the DB). Measured on the two files
side by side (chukat_ink.py's assert): a transposition in the English alone. Read as the
Hebrew has it; the ledger names it. The class joins the mistyped heads (four found) and the
mistyped citations inside rows (three found at Korach).

(3) THE PARSER ON CHUKAT'S NUMBERS: RIGHT at 19:4 [7], 19:11 [7], 19:14 [7], 19:16 [7],
20:29 [30]; SILENT ON THE DATE-ORDINALS — 19:12 and 19:19's "on the third day and on the
seventh day" read [], 20:1's "in the first month" [], 21:26's "the first king" [] (right —
an adjective), and the itinerary's date for Aaron's death, "in the FORTIETH year... in the
FIFTH month, on the FIRST of the month" (33:38), reads [1] alone. A class named and left:
the ordinal day-words the compile's timers must read by their own rule (or the parser is
taught them at 6b with probes to FAIL). ONE GAP ON THE PORTION'S OWN NUMBER: 20:11 "he
struck the rock with his staff TWICE" reads [] — THE DUAL pa'amayim, the same consonants as
19:4's plural pe'amim "seven TIMES" (read by its "seven"), told apart by the PATACH under the
pe against the SHEVA (computed on the DB's bytes): the Torah's dual "twice" stands at Gen
27:36 (Esau: "these two times"), 41:32 (the dream "doubled twice"), 43:10 (Judah: "we could
have returned twice") and Num 20:11 — the four seats of the class, owed to the compile with
a probe to FAIL. The translation reads it as a numeral and a noun, "two times". 19:6's
"scarlet" (ushni tola'at) carries the consonants of "two of" and is silent by the chiriq
under the nun — right. The retellings' numbers right: Aaron's 123 (33:39), the thirty-eight
years (Deut 2:14), Og's bed 9 by 4 (Deut 3:11), Moses' thirty days (Deut 34:8).

(4) ONE CONSONANTAL SKIN, FOUR WORDS, TOLD BY THE POINTS: Miriam (20:1, the chiriq under
the mem), the BITTER waters of Marah ("for they were bitter", Exod 15:23, the qamats), the
sotah's "bitter waters that curse" (5:18, 19, 23, 24, the qamats with the article), and
"the REBELS" of Moses' rebuke nine verses after her death (20:10, the cholam) — measured on
the DB's bytes (chukat_ink.py: vowels_on, the marks compared as a SET on the consonant, never
as a typed string — the marks' order in the DB is not the hand's). Psalm 106:33 reads the
sin at Meribah as this speech, "he spoke rashly with his lips", and turns the rebel-verb
onto the people ("they embittered his spirit").

(5) THE TWO ROCK-WORDS AND THE TRANSLATION'S TWO: Exodus' rock at Horeb is tzur ("you shall
STRIKE the tzur", 17:6); Numbers' is sela ("SPEAK to the sela", 20:8, 10, 11; Balaam's Kenite
nest 24:21 its other Torah seat); Deut 32:13 alone carries both; the Psalms, Isaiah and
Deuteronomy retell the water-rock as tzur (Ps 78:20, 105:41, 114:8; Isa 48:21; Deut 8:15).
Onkelos renders tzur TINARA and sela KEFA — measured on both books' bytes.

(6) THE POLE-WORD'S HOMOGRAPHS: nes with the tsere (the pole, the banner) stands in the
Torah at Exod 17:15 (YHWH-nissi), Num 21:8-9 and 26:10 (Korach's 250 "became a sign");
"fled" (Deut 34:7, the qamats) and "to flee" (Deut 4:42, Num 35:6 — the manslayer's, the
same consonants with the lamed) are its homographs, told by the points; the translation
gives the serpent's pole and Korach's sign one Aramaic word (at). Likewise "Bamoth" the
station (21:19-20, the qamats) against "in the DEATH of" (26:10, Gen 21:16, the sheva).

(7) THE STORE'S GLOSS LAYER ON A HAPAX: 21:30's "we shot them" (a hapax) is glossed by the
snapshot store's words.gloss as "and-flow-as-water-them" — the display layer's reading of
another root; the ink's word stands, Onkelos reads "their KINGDOM ceased". Recorded as the
store's, not the ink's (the gloss layer is the overrides file's business).

(8) THE FORM'S OWN LESSONS: thirty-two asserts failed on the first typed pass even after the
measurement pass — the compound asserts hid which leg had failed, and a diagnostic printing
EACH LEG resolved them in one run (the leg-by-leg print joins the form); a typed pointed
form is never compared by string (five asserts fell on the marks' order — vowels_on); an
exact-token census needs EVERY prefixed and spelled form (hyssop's article, "in waters of
niddah", "at Hormah", usury's "at bite", Meribah's plural, Chemosh spelled with a yod at Jer
48:7) — the forms typed from the print; a check word's stem piece under six code points
four times in one pass (the store splits the prefix: "by one slain", "at the brook", "to spy
out", "from before") — the stem-bearing word chosen before typing; the lint's window on
four long cuts in chapter 21, split into glossed pieces; and the cd at the head of a
compound command persisted to its tail TWICE MORE (the lint loop's relative paths printed
nothing; verify_claims from the scratchpad's cwd found no file) — the repo-root tools with
absolute paths in their own call, never after a cd.
"""
append(f'{ROOT}/RESEARCH_LOG.md', RL, "THE EXPORT'S ENGLISH REVERSES A FRAME")

# ---- NUMBERS_WALK.md: Sitting 6 ----
NW = """

## Sitting 6 — CHUKAT, Numbers 19:1-21:35 (2026-09-11; the owner: "Go" after the #127 rereads, on the ruling READ THEN COMPILE): the reading and the units

THE DRAFTS: three cover the span — computed: 86 of 86 verses (22 + 29 + 35); the portion's last verse (22:1) opens the next draft
(num_22_balak_bilam_call, 22:1-41) and is read with it. The three: num_19_parah 19:1-22, num_20_meribah_edom_aaron 20:1-29,
num_21_snakes_conquest 21:1-35.

THE SHELF, BY POSITION (chukat_ink.py's asserts): the Sifrei on Numbers has EIGHT piskaot on chapter 19 — 123 on 19:1 (headed "19:1-2"),
124 on 19:5, 125 on 19:11, 126 on 19:14, 127 on 19:16, 128 on 19:17, 129 on 19:18, 130 on 19:22 — NINETEEN rows at the shelf's row grain
(123: 2, 124: 2, 125: 1, 126: 1, 127: 5, 128: 2, 129: 5, 130: 1), every head asserted between its neighbors and none mistyped; and NO PISKA
on chapters 20, 21, 22, 23 or 24 (computed on every head — the next head, 131, is Balak's close at 25:1): the walk's third whole-narrative
stretch read on the translation alone. A NEW DEFECT CLASS: the export's ENGLISH reverses 123:1's frame ("to Aaron and to Moses") where its
own Hebrew row reads "to Moses and Aaron" — measured on the two files (RESEARCH_LOG.md). Onkelos 19, 20, 21 whole: 86. No prior ledger had
read any of the 19 rows or the 86 verses (grepped — the sitting's own ledgers excluded; the Sifrei's 132-134 read at THE TENT's daughters
are Pinchas's).

THE READING (six modules — scratchpad chukat_ink.py the ink with every fact an assert, chukat_rows_onkelos.py (19-20) and
chukat_rows_onkelos21.py the rows, chukat_rows_sifrei.py, write_chukat_ledgers.py the writer → three ledgers logic/oral_triage/<uid>_2026-09-11.md;
chukat_measure1.py the measurement pass): 105 sources opened and verdicted — Onkelos MATERIAL 73 / CONTEXT 13 (21/1, 25/4, 27/8 by chapter);
the Sifrei MATERIAL 18 / CONTEXT 1 (the script's Counters); coverage computed, missing 0, extra 0; every quotation CUT by consonants — NO MISS
on the first run of the writer (the first sitting with none); every narrative verb glossed by the store's own words.gloss; gloss_lint 0 on
all three after six flags on the first draft (two jargon words glossed, four long cuts in chapter 21 split into glossed pieces).

THE INK, COMPUTED (the measurement pass FIRST — chukat_measure1.py printed every candidate fact; the asserts typed from the print;
assert_driver.py then listed THIRTY-TWO failures on the first typed pass — the compound asserts hid which leg, and a diagnostic printing
each leg resolved them: five on the marks' order (a typed pointed form against the DB's bytes — the vowel helper vowels_on compares the
marks as a set on the consonant), a dozen on the union of forms (hyssop's article, "in waters of niddah", "at Hormah", usury's "at bite",
Meribah's plural, Chemosh with a yod), the rest the hand's slices and counts; then two, then one, then 0 failing):
- THE PARSER MEASURED AGAIN (the standing rule): RIGHT at five verses — 19:4 [7], 19:11 [7], 19:14 [7], 19:16 [7], 20:29 [30]; SILENT ON
  THE DATE-ORDINALS — the third and the seventh day (19:12, 19:19), the first month (20:1), the fortieth year / fifth month / first day
  of Aaron's death (33:38 → [1]) — a class named and left for the compile's timers; "scarlet" silent by the chiriq (the consonants of
  "two of") — right; ONE GAP ON THE PORTION'S OWN NUMBER: 20:11 "TWICE" — the dual pa'amayim, the consonants of 19:4's plural "times", told
  by the patach under the pe; the Torah's four (Gen 27:36, 41:32, 43:10, Num 20:11) — the compile's probe list.
- THE FRAMES 6 (19:1, 20:7, 20:12, 20:23, 21:8, 21:34; four "said"; THREE TO MOSES AND AARON TOGETHER — the heifer's law, the sentence,
  Aaron's death-sentence); THE REGISTER 47 verses (chapter 19: 1 — the frame alone; 20: 22; 21: 24); 20:1 (Miriam's death) and 20:28
  (Aaron's) the densest at four verbs each.
- THE HEIFER (chapter 19): "the statute of the Torah" two seats (19:2, 31:21); THE HEIFER-NOUN's Torah seats all in this chapter (Gen 35:11
  "be fruitful", Deut 29:17 "bearing" the homographs); "whole" feminine at eight — Psalm 19:8's Torah among them; THE YOKE CLAUSE at two
  seats — the heifer and the Philistines' ark-cows (1 Sam 6:7), the eglah arufah's "drawn" another verb; Eleazar at 19:3-4 and 20:25-28;
  "with his finger" nine; THE BURN-LIST the sin-bull's (Exod 29:14, Lev 4:11, 16:27) WITH THE BLOOD ADDED; the leper's three in the LEPER'S
  order (shni tola'at ×3); HYSSOP PLENE at Passover, the heifer, Solomon, Psalm 51, DEFECTIVE at the leper's five; "a clean man" 19:9, 19:18
  alone; "for a KEEPING" the Torah's eight — the lamb, the manna, the Levites' post, AARON'S STAFF, the ashes; THE WATERS OF NIDDAH six seats
  in the MENSTRUANT'S word; "it is a sin-offering" Exod 29:14's formula; "a human soul" the blasphemer's Lev 24:17; the reflexive sin-verb
  ten; "the third and the seventh" 19:12 ×2, 19:19, RUN at 31:19; MISHKAN (19:13) and MIKDASH (19:20) the Sifrei's pair on the ink; "tzamid
  patil" — Rebekah's BRACELETS, Elijah's YOKE, the frontplate's and the fringe's CORD; "one slain by the sword" singular the Bible's one seat;
  "a human bone" with Gog's burial; THE FOUR SOURCES REORDERED (19:16 → 19:18, the bone to the head); ASHES 19:9-10 / DUST 19:17 (the sotah's
  5:17); "living water" Isaac's well; "take hyssop and dip" the PASSOVER'S verbs; "clean in the evening" the chapter's one; "from the midst
  of the assembly" KORACH'S 16:33 and this.
- MIRIAM, MERIBAH, EDOM, AARON (chapter 20): "the first month" NO YEAR; "and she was buried" — Deborah, Rachel, Miriam; ONE CONSONANTAL
  SKIN — Miriam, the bitter waters (Exod 15:23; 5:18-24), the rebels (20:10); "they assembled against" KORACH'S 16:3; "the people strove with
  Moses" EXODUS 17:2; "why did you bring us up" Exod 17:3, 20:5, 21:5; "the assembly of the LORD" Korach's; the glory's four; "the staff from
  before the LORD" — 17:24-25's place; THE TWO ROCK-WORDS (tzur / sela; tinara / kefa); "with his staff" Exod 8:13; TWICE the dual; MERIBAH
  eleven seats; "He was sanctified in them" — Lev 10:3's verb; Ps 106:33; "the hardship that FOUND" Exod 18:8; THE FIRSTFRUITS DECLARATION'S
  two clauses (Deut 26:6-7) in the Edom letter; messengers / angel one noun, two Aramaic; THE TWO MESSAGES measured (thirteen shared;
  plural and plene against singular and defective); "the highway" the Torah's one; "with a strong hand" the Exodus's (Exod 6:1 ×2); "lest
  with the sword" Esau's Gen 27:40; "refused" Jacob's; TWO MOUNT HORS; THE GATHER-VERB — the ashes and Aaron; "clothe them" Exod 29:8, the
  spec 29:29-30 RUN; Deut 10:6 Moserah; "on the top of the mountain" Exod 24:17; 33:38-39 the date and the age; "thirty days" Aaron's and
  Moses'; "all the house of Israel" Lev 10:6 — the mourners of his sons.
- ARAD, THE SERPENT, THE WELL, SIHON AND OG (chapter 21): Arad 33:40; Atharim → the SPIES' road in Onkelos; "vowed a vow" Jacob / Israel /
  Jephthah; HORMAH named (14:45's use closed), Judah's second naming; 14:25's command RUN at 21:4; "the soul shortened" Samson's; "to die in
  the wilderness" the sea's; the light bread → the MANNA; the fiery serpents = the heifer's burn-word; THE BITE = usury's; "Moses prayed"
  11:2; the serpent singular; THE POLE-WORD — YHWH-nissi, KORACH'S SIGN (one Aramaic word), "to flee" the homograph; THE LOOK — Lot's wife;
  NEHUSHTAN (2 Kgs 18:4); the two itineraries; DEUTERONOMY 2:14 DATES THE ZERED (thirty-eight years; the Word resuming 2:16-17); the Book of
  the Wars; the unrecorded saying (21:16); "then sang" the SEA'S formula; "answer it" MIRIAM'S verb (Exod 15:21; Isa 27:2); the LAWGIVER Judah's
  (Gen 49:10 — Onkelos SCRIBES at both); MATTANAH the gift-word (18:6-7); the translation's travelling well; BAMOTH / the high places / "in the
  death of"; Pisgah Moses' death-view; Sihon's message singular; Deut 2:30's HARDENING, Judg 11:20's distrust; Jabbok Jacob's ford; Ammon
  STRONG (here) / COMMANDED (Deut 2:19, 37); the PARABLE-TELLERS = Balaam's word; JEREMIAH 48:45-46 quotes 21:28-29; Chemosh to Ammon (Judg
  11:24); the hapaxes; "to SPY OUT" (ragal) Caleb's verb (Josh 14:7) against 13:2's "tour"; DEUTERONOMY 3:1-3 = 21:33-35 WITH THE PRONOUNS
  SHIFTED (3:2 one token); "do not fear him" Joshua's Ai and Gibeon; "no survivor left" JOSHUA'S REFRAIN born; Og's bed 9 × 4.
- THE TRANSLATION'S OWN WORDS, cut from the shelf's bytes (the ledgers' full lists): "statute" → DECREE; the dung → ITS FOOD; the scarlet →
  DYED and the washing the same DYE-verb; the niddah → SPRINKLING; "purify himself" → SPRINKLE upon himself; the tent → the TABERNACLE-word;
  "every open vessel" → OF EARTHENWARE inserted; "living water" → SPRING water; Kadesh → REKAM; the sela → KEFA (Exodus' tzur TINARA);
  rebels / refused / rebelled → one root; "twice" → TWO TIMES; the Memra; Meribah → the waters of STRIFE; messengers → ENVOYS, the angel kept;
  "we cried" → we PRAYED; "lest with the sword" → THOSE WHO KILL; "nothing" → no EVIL thing; Atharim → THE SPIES; the vow → a COVENANT; the
  light bread → THIS MANNA; the pole → a SIGN (= Korach's); the serpent's pun lost; Iye-abarim translated; Vaheb → the LORD's deeds; Ar →
  LECHAYATH; Beer → the well GIVEN; "sang" → PRAISED; the lawgiver → THE SCRIBES; Mattanah, Nahaliel, Bamoth → the well descending and
  ascending WITH THEM; Pisgah → the height; the fire → an EAST WIND, the flame → WARRIORS, the lords → IDOL-PRIESTS; "we shot them" → the
  KINGDOM ceased; Bashan → MATNAN; survivor → ESCAPER.

THE SIFREI'S OWN CASE LAW (twelve entries appended to MIDDOT.md "The middot's own case law"): the a-fortiori's protocol run three times in
one chapter with its formula verbatim (the yoke, the sheretz, the grave); "a derivation from a derivation?" at its second seat; a verdict
by elimination (the sprinkler's water-measure); the identity licensed by a departed word ("earth" for "ashes"); the same clause read narrow
and wide; the section's shape named on the opening; the punishment split by two verses; the third verse fixing the schedule; the teacher's
deliberate error; the academy's dispute read as Daniel's vision; two bones at two seats on the ink's reordering; the vessel census by three
verses. No new move.

THE CLAIMS (write_chukat_manifests.py → three manifests, 34 claims — CH19A ×12, CH20A ×10, CH21A ×12 — every check cut from the store's bytes,
four check words switched when the stem piece fell under six code points; the ID prefixes asserted absent from every manifest and unit; every
source cite checked against its ledger's CITE INDEX): verify_claims 34 VERIFIED / 0 FAILED; claim_labels_census --strict GREEN (Numbers 245
labeled 245, debt 0). THE SEATS (seat_chukat.py): 34 WITNESS_READ operators at the claims' first verses, step E, the scenarios in the anchor
form; verify_text GREEN ×3. THE RITUALS (three in sequence, in the background): every gate PASS — RITUAL COMPLETE ×3: 194, 195, 196 frozen
units. THE CORPUS REBAKED (predicted before the fold: units 196, standing 1989 + 34 = 2023, facts, demands, events, names and hash unmoved):
""" + FOLD + """ — the prediction matched; CORPUS TRUTH GREEN. THE STAMP: one delegated FULL RULE row for the three
(logic/findings/STAMP_LEDGER.md). No engine file changed at this sitting — the sweep and the journal gate stand as at 5b's close.

OWED TO THE COMPILE (sitting 6b; also in COMPILE_DEBT's THEN NUMBERS box): (a) THE PARSER — THE DUAL "TWICE" (20:11; the patach under the
pe; the class's four Torah seats — a probe to FAIL, the corpus-wide diff read); THE DATE-ORDINALS as a design choice at 6b (teach "the third
day", "the seventh day", "the first month", "the fortieth year / fifth month / first of the month" with probes, or read them as the timers'
data by their own rule — decided at the design, recorded either way); (b) THE FUNCTIONS — THE HEIFER'S RITE as a state machine (the
conditions: the standing tent, the adjutant, work invalidating from the slaughter to the ashes, the blood returned; the parameters as data:
the age's three settings, the hairs, the blemish that passed, the tvul yom; the Sadducees' row); THE CORPSE-TUMAH ENGINE — contact, tent,
field (the four sources, the two bones), the removes table (Oholot 1:1-3 as data: seven days / until evening / not by moving), the vessel
census (six classes), the lid (earthenware, tzamid patil), the sprinkling schedule (THE THIRD AND THE SEVENTH DAY AS TIMERS, the four
failure states, the punishment SPLIT — uncleanness for the omission, karet for the entry), the sprinkler's water-measure; THE OWED EDGES
naso → heifer (5:2's corpse-unclean sent out) and beha → heifer (8:7's water of sprinkling) PAID by the heifer engine's cell, and the RUN at
the Midian war (31:19-24) filed forward; THE MERIBAH SENTENCE (a HEAVEN entry on Moses and Aaron — not to enter — closed at Aaron's death
20:28 and at Deut 34; 27:14 and Deut 32:51 as run citations); THE SUCCESSION (Exod 29:29-30's spec RUN — the garments transferred, Aaron's
in_force priesthood ended and Eleazar's begun by the priesthood engine's CALL; Deut 10:6's Moserah as the shelf's DIVERGE); EDOM'S REFUSAL
(a block on the road; Deut 2's purchase arm a DISPUTE row); THE VOW AND THE CHEREM (21:2 a debit, 21:3 its close; Hormah's naming closing
CF9's proleptic row); THE SERPENT (the plague a HEAVEN entry on the people; the copper serpent an object row whose run ends at 2 Kgs 18:4);
THE CONQUEST (Sihon and Og — the land east of the Jordan possessed: a status the Reubenites' chapter 32 reads); the exam docket by the
union rule (the link scan + the topic windows BY ADDRESS: Parah whole; Oholot whole; Kelim 1-2, 9-10; Mikvaot 1-2; Keritot 1; Shevuot 1-2;
Eduyot 1, 6; Rosh Hashanah 3:8; Avot 5:6; Taanit 9a; Moed Katan 28a; Chullin 60b; Berakhot 54a-b; Nedarim 55a; Bava Batra 14b; Seder Olam
9-10); (c) THE TAPE — the markers: Miriam's death "in the first month" of the FORTIETH year (33:38's year for the same stretch — placed at
(40, 1, 1) with the shelf's tenth of Nisan as the reading arm), Aaron's death (40, 5, 1) TEXT-CONSTRAINED by 33:38 — the book's one full
death-date; the thirty days' mourning a TIMER (due (40, 6, 1)); THE THIRTY-EIGHT-YEAR TIMER (sitting 4b's CF3, due (40, 5, 9)) FIRING on the
walk from Aaron's death to the Zered (21:12 — Deut 2:14 makes the crossing the generation's end): the sitting's checkpoint; 14:25's
turn-back debit RUN at 21:4 (the open debit closed); the entities miriam (dies), aaron (dies — the priesthood transfers), eleazar (in
force), edom, arad, sihon, og (peoples and kings), the copper serpent (an object), the well; the six frames; A DIVERGE TO RECORD: the
shelf's thirty-eight years without the Word to Moses (Taanit 30b on Deut 2:16-17) against the ink's frames in chapters 16-19 — the tape
counts the frames between the decree and 20:7; the edges chukat → naso (5:2 paid), beha (8:7 paid), leper (Lev 14's living water, the
finger, the bird), yoma (the finger, the vestments), chatat (the sin-bull's list), tzav / offerings (me'ilah), pesach (the hyssop), sotah
(the dust), priesthood (the succession), shelach (the turn-back run; Hormah), korach (the staff from before the LORD; Korach's phrases),
bamidbar (Zin, Kadesh), sequence → chukat; the retellings as run citations (27:14, Deut 1-3, 10:6, 26:6-7, 32:51, 33:8; Judg 11; Josh 14:7;
Ps 78, 106; Jer 48; 2 Kgs 18:4).

⚠ LESSONS (6): THE MARKS' ORDER IS NOT THE HAND'S — compare the points as a SET on the consonant (vowels_on), never a typed pointed form by
string (five asserts fell on it). THE LEG-BY-LEG DIAGNOSTIC — a compound assert's failure names nothing; print each leg once and retype from
the print (thirty-two → two → one → 0 in three passes). THE UNION OF FORMS — an exact-token census needs every prefixed and spelled form,
typed from the print (a dozen misses in one pass). THE CHECK WORD'S STEM PIECE UNDER SIX, FOUR TIMES — the store splits the prefix; choose
the stem-bearing word before typing. THE LONG CUT SPLIT, AGAIN (four in chapter 21). THE EXPORT HAS TWO FILES — the English head is checked
against the Hebrew row (the translator reversed a frame's addressees: a new defect class). THE cd AT THE HEAD OF A COMPOUND COMMAND
PERSISTED TO ITS TAIL TWICE MORE (the fourth and fifth instances: the lint loop's relative paths printed nothing; verify_claims from the
scratchpad's cwd) — the repo-root tools with absolute paths in their own call. THE WRITER'S FIRST RUN WITH NO CUT MISS — the form holds
when the tokens are typed from the dump. THE PARSER'S NEW GAP SITS ON THE PORTION'S OWN NUMBER AGAIN (20:11's "twice") — and a CLASS CAN BE
NAMED AND LEFT (the date-ordinals) when the compile's own instrument will read it.

NEXT on the ruling: THE COMPILE OF CHUKAT (6b) on 1b's order — the docket, the dual probe to FAIL, the heifer's state machine and the
corpse-tumah engine, the removes, the sentence, the succession, the serpent, the conquest, the tape's fortieth-year markers and the
thirty-eight-year timer's fire — before chapter 22 (Balak), never the next reading first.
"""
append(f'{ROOT}/World/step9/NUMBERS_WALK.md', NW, '## Sitting 6 — CHUKAT, Numbers 19:1-21:35')

# ---- COMPILE_DEBT.md ----
CD = """
## OWED TO THE COMPILE — SITTING 6b (THE NUMBERS WALK sitting 6, CHUKAT 19:1-21:35 READ AND FROZEN 2026-09-11; NUMBERS_WALK.md "Sitting 6"): (a) THE PARSER — THE DUAL
## "TWICE" (20:11, pa'amayim by the patach; the class's four Torah seats Gen 27:36, 41:32, 43:10, Num 20:11 — a probe to FAIL, the corpus diff read); THE DATE-ORDINALS (the
## third / seventh day, the first month, 33:38's fortieth year / fifth month / first day) — teach them with probes or read them as the timers' data: decided at 6b's design;
## (b) THE FUNCTIONS — THE HEIFER'S RITE as a state machine (the standing tent, the adjutant, work from the slaughter to the ashes, the blood returned; the age's three
## settings, the hairs, the blemish that passed, the tvul yom as data); THE CORPSE-TUMAH ENGINE (contact, tent, field; the four sources and the two bones; the removes
## table — Oholot 1:1-3 as data; the vessel census's six classes; the lid; THE THIRD AND SEVENTH DAY AS TIMERS with the four failure states; the punishment SPLIT —
## uncleanness for the omission, karet for the entry; the sprinkler's water-measure); THE OWED EDGES naso → heifer (5:2) and beha → heifer (8:7) PAID; the Midian war's
## run (31:19-24) filed forward; THE MERIBAH SENTENCE (a HEAVEN entry on Moses and Aaron, closed at 20:28 and Deut 34); THE SUCCESSION (Exod 29:29-30 RUN — the
## priesthood engine's CALL; Deut 10:6 Moserah a DIVERGE); EDOM'S REFUSAL (a block; Deut 2's purchase a DISPUTE); THE VOW AND THE CHEREM (21:2-3; Hormah's naming closes
## CF9's proleptic row); THE SERPENT (a HEAVEN entry; the copper serpent an object ending at 2 Kgs 18:4); THE CONQUEST (the land east of the Jordan a status); the docket
## by the union rule (Parah, Oholot, Kelim 1-2, 9-10, Mikvaot 1-2, Keritot 1, Shevuot 1-2, Eduyot 1, 6, Rosh Hashanah 3:8, Avot 5:6, Taanit 9a, Moed Katan 28a, Chullin
## 60b, Berakhot 54a-b, Nedarim 55a, Bava Batra 14b, Seder Olam 9-10); (c) THE TAPE — Miriam's death in the fortieth year's first month (33:38's year; the shelf's tenth
## of Nisan the reading arm), AARON'S DEATH (40, 5, 1) TEXT-CONSTRAINED by 33:38, the thirty days a TIMER, THE THIRTY-EIGHT-YEAR TIMER (CF3, due (40, 5, 9)) FIRING on the
## walk to the Zered (21:12 — Deut 2:14's end), 14:25's turn-back debit RUN at 21:4, the entities (miriam, aaron, eleazar, edom, arad, sihon, og, the copper serpent, the
## well), the six frames, the DIVERGE on the shelf's thirty-eight silent years against the ink's frames; the edges chukat → naso, beha, leper, yoma, chatat, tzav,
## offerings, pesach, sotah, priesthood, shelach, korach, bamidbar, sequence → chukat; the retellings as run citations.
"""
append(f'{ROOT}/World/step9/COMPILE_DEBT.md', CD, 'OWED TO THE COMPILE — SITTING 6b')

# ---- THE_STEPS.md: the sitting-6 paragraph in ## THE NUMBERS WALK ----
TS = """
THE SIXTH SITTING, CHUKAT (Numbers 19:1-21:35, 2026-09-11, on Brian's
"Go" after the rereads; the portion's last verse, 22:1, opens the next
draft and is read with it), read the red heifer, Miriam's death and
the waters of Meribah, Edom's refusal, Aaron's death on Mount Hor, the
serpents, the well and the two kings in one pass — three ledgers, 105
sources, thirty-four claims, three units frozen, the corpus refolded
exactly as predicted (196 units, standing 2023, the hash unmoved). It
taught the walk five more things. THE SHELF SPEAKS ON THE HEIFER AND
IS SILENT ON THE ROAD: the Sifrei's eight piskaot sit in order on
chapter 19 with no mistyped head, and no piska at all stands on
chapters 20 through 24 — the third whole stretch of story read on the
translation alone; and the export's English reverses the first frame's
addressees ("to Aaron and to Moses") where its own Hebrew row has
Moses first — a new class of defect, caught by checking the head
against the Hebrew file. THE HEIFER IS WRITTEN IN OTHER RITES' WORDS,
MEASURED: its burn-list is the sin-bull's list of Exodus 29 and
Leviticus 4 and 16 with the blood added; its cedar, hyssop and scarlet
are the leper's bundle in the leper's word order; "take hyssop and dip"
are the Passover's two verbs, blood there and water here; its ashes are
kept "for a keeping" in the manna jar's and Aaron's staff's word; "a
human soul" is the blasphemer chapter's murder clause; and the yoke
clause "upon which no yoke has come" has one other seat in the Bible —
the Philistine cows that carried the ark home. ONE CONSONANTAL SKIN
HOLDS FOUR WORDS: Miriam's name, the bitter waters of Marah and of the
suspected wife, and "the rebels" Moses shouts nine verses after her
burial — told apart only by the vowel points, and the Psalm reads the
sin at the rock as that speech. THE PARSER FOUND ITS GAP ON THE
PORTION'S OWN NUMBER AGAIN: "he struck the rock TWICE" is a dual with
the same consonants as "seven TIMES", told by one vowel, and the machine
read nothing; the ordinal day-words ("the third day", "the seventh day",
"the first month", the itinerary's "fortieth year, fifth month, first
day" for Aaron's death) are silent too — a class named and left for the
compile's timers. And THE RETELLINGS DATE AND REPEAT THE TEXT: the
itinerary gives Aaron's death its full date, Deuteronomy 2 dates the
brook Zered as the end of the thirty-eight years, and Deuteronomy 3
repeats the Og verses with the pronouns shifted and one word changed,
while Jeremiah quotes the parable-tellers' song and Joshua inherits
"until no survivor was left" as his refrain. The Sifrei ran the
a-fortiori's full protocol three times in one chapter and refused "a
derivation from a derivation"; twelve entries went into the middot
file. Next: Chukat's compile (6b), then chapter 22.
"""
insert_after(f'{ROOT}/THE_STEPS.md', "green. Next: chapter 19, the heifer's reading.\n", TS, 'THE SIXTH SITTING, CHUKAT')

# ---- THE_BRIEFING.md ----
BR_BULLET = "- **CHUKAT READ AND FROZEN — SITTING 6 DONE: THE SHELF SPEAKS ON THE HEIFER AND IS SILENT ON THE ROAD, THE HEIFER IS WRITTEN IN OTHER RITES' WORDS, AND ONE CONSONANTAL SKIN HOLDS MIRIAM, THE BITTER WATERS AND THE REBELS** (2026-09-11, on your \"Go\"; World/step9/NUMBERS_WALK.md \"Sitting 6\"). Numbers 19 to 21 read at the parashah grain: 105 sources (Onkelos whole, the Sifrei's eight piskaot on the heifer found by position, none on 20-24), three ledgers, 34 claims verified and labeled, three units frozen — 196 units, standing 2023, the hash unmoved, the fold predicted and matched. The parser right at five verses, silent on the ordinal day-words, and blind to \"he struck the rock TWICE\" — the dual with the consonants of \"seven TIMES\", one vowel apart — the compile's next probe. The export's English reversed a frame's addressees against its own Hebrew — a new defect class caught. Next: Chukat's compile (6b), then chapter 22.\n"
insert_before(f'{ROOT}/THE_BRIEFING.md', "- **KORACH COMPILED — SITTING 5b DONE:", BR_BULLET, 'CHUKAT READ AND FROZEN — SITTING 6 DONE')
s = open(f'{ROOT}/THE_BRIEFING.md', encoding='utf-8').read()
assert s.count('## SCOREBOARD (as of 2026-09-10, latest)') == 1
open(f'{ROOT}/THE_BRIEFING.md', 'w', encoding='utf-8').write(s.replace('## SCOREBOARD (as of 2026-09-10, latest)', '## SCOREBOARD (as of 2026-09-11, latest)'))
BR_ENTRY = """### 2026-09-11 — THE HEIFER IS WRITTEN IN OTHER RITES' WORDS, AND THE MACHINE CANNOT YET READ "TWICE"

Sitting 6 read Numbers 19 to 21 on your "Go" (World/step9/NUMBERS_WALK.md
"Sitting 6"): the red heifer, Miriam's death and the rock, Edom's refusal,
Aaron's death and the garments passed to Eleazar, the serpents, the well's
song, Sihon and Og. The shelf's spine speaks on the heifer alone — eight
piskaot in order, no mistyped head — and is silent on the two chapters of
road, so the story ran on the translation and the ink's own census, as the
spies and the rebellion did. Three things to carry. First, the heifer's law
is built from the vocabulary of other rites, and the measurements say so:
its burn-list is the sin-bull's with the blood added; its cedar, hyssop and
scarlet are the leper's bundle in the leper's word order; its "take hyssop
and dip" are the Passover's verbs with water for blood; its ashes are kept
in the manna jar's and Aaron's staff's "for a keeping"; its "human soul" is
the blasphemer chapter's murder clause; and its yoke clause stands at one
other seat in the Bible, the Philistine cows that drew the ark home. Second,
the vowel points carry meaning the letters do not: Miriam's name, the bitter
waters of Marah, the suspected wife's bitter waters and "the rebels" of
Moses' outburst are one string of consonants, and the parser's new gap sits
on the same fact — "he struck the rock TWICE" is a dual spelled like "seven
TIMES", one vowel apart, and the machine read nothing; the ordinal
day-words ("the third day", "the seventh day", "the first month", the
itinerary's full date for Aaron's death) are silent too, a class named and
left for the compile's timers. Third, the later books date and repeat this
one: Numbers 33 gives Aaron's death its year, month and day; Deuteronomy 2
dates the brook Zered as the end of the thirty-eight years, so the
decree's timer has its end-marker in the retelling's ink; Deuteronomy 3
repeats the Og verses with the pronouns shifted and a single word changed;
Jeremiah quotes the parable-tellers' song; Joshua inherits "until no
survivor was left" as his refrain. The export's English reversed a frame's
addressees against its own Hebrew row — a new defect class, caught by
checking the head against the Hebrew file. Thirty-four claims verified,
three units frozen, the corpus refolded exactly as predicted. Next:
Chukat's compile (6b), then chapter 22.

"""
insert_after(f'{ROOT}/THE_BRIEFING.md', "## ENTRIES (newest first)\n\n", BR_ENTRY, "THE HEIFER IS WRITTEN IN OTHER RITES' WORDS, AND THE MACHINE")

# ---- World/RESUME.md ----
RS = "SITTING 6 DONE 2026-09-11 (CHUKAT 19:1-21:35 READ AND FROZEN; NUMBERS_WALK.md \"Sitting 6\"): the Sifrei's eight piskaot on the heifer in order, none on 20-24 (computed), the export's English reversing a frame against its own Hebrew; 105 sources, three ledgers, 34 claims verified and labeled, three rituals → 196 units, standing 2023, hash unmoved; the parser RIGHT at five, the date-ordinals SILENT (a class named and left), ONE GAP — the dual \"twice\" (20:11 → []); the crowns: the heifer in other rites' words (the sin-bull's list with the blood, the leper's bundle in the leper's order, the Passover's verbs, the keeping-word, the blasphemer's clause, the ark-cows' yoke), one consonantal skin for Miriam / the bitter waters / the rebels, the two rock-words, the firstfruits declaration in the Edom letter, Deuteronomy 2:14 dating the Zered, Deuteronomy 3 repeating the Og verses, Jeremiah quoting the parable-tellers, Joshua's refrain born. Next: THE COMPILE OF CHUKAT (6b), then chapter 22.\n"
insert_after(f'{ROOT}/World/RESUME.md', "NEXT: chapter 19 (the heifer's reading).\n", RS, 'SITTING 6 DONE 2026-09-11')

# ---- the memory: numbers-in-order-ruling.md ----
p = f'{MEM}/numbers-in-order-ruling.md'
s = open(p, encoding='utf-8').read()
assert 'SITTING 6 DONE' not in s
old_desc = 'NEXT CHAPTER 19 — the heifer\'s reading, then its compile"'
assert s.count(old_desc) == 1
s = s.replace(old_desc, 'SITTING 6 CHUKAT 19:1-21:35 READ AND FROZEN 2026-09-11 (196 units; 34 claims; the Sifrei\'s eight piskaot on the heifer, none on 20-24; the dual \\"twice\\" a new parser gap, the date-ordinals a class named and left); NEXT THE COMPILE OF CHUKAT (6b), then chapter 22"')
s = s.rstrip('\n')
assert s.endswith('Related: [[the-loop-ruling]], [[step9-exam-era]], [[spine-default]].')
s = s.replace('Related: [[the-loop-ruling]], [[step9-exam-era]], [[spine-default]].',
"""SITTING 6 DONE 2026-09-11 — CHUKAT 19:1-21:35 READ AND FROZEN (NUMBERS_WALK.md "Sitting 6"; the owner: "Go" after the #127 rereads; the
portion's last verse 22:1 opens the next draft and is read with it): the Sifrei's EIGHT piskaot on chapter 19 by position (19 rows; every
head in order, none mistyped; NO PISKA on 20-24 — computed; THE EXPORT'S ENGLISH REVERSES 123:1's FRAME against its own Hebrew row — a new
defect class, RESEARCH_LOG.md) + Onkelos whole (86) = 105 sources in three ledgers (six modules: chukat_ink.py, the three rows files, the
writer, the measurement pass; thirty-two failures on the first typed pass — the leg-by-leg diagnostic; the writer's first run with NO cut
miss); 34 claims verified and labeled, 34 operators seated, three rituals → 196 units, standing 2023, hash unmoved, the fold matching its
prediction; THE PARSER RIGHT at five, SILENT on the date-ordinals (a class named and left for the compile's timers), ONE GAP — THE DUAL
"TWICE" (20:11 pa'amayim by the patach; Gen 27:36, 41:32, 43:10 its kin); the crowns in the file (the heifer in other rites' words; one
consonantal skin for Miriam, the bitter waters and the rebels; the two rock-words and the translation's two; the firstfruits declaration in
the Edom letter; the staff from before the LORD; the gather-verb for the ashes and for Aaron; Deut 2:14 dating the Zered; Deut 3 = Num 21:33-35
with the pronouns shifted; Jeremiah quoting the parable-tellers; Joshua's refrain born; Nehushtan). UNCOMMITTED since 0a98276. NEXT: THE
COMPILE OF CHUKAT (6b) on 1b's order (COMPILE_DEBT's sitting-6 box: the dual probe, the date-ordinals decided, the heifer's state machine
and the corpse-tumah engine, the sentence, the succession, the serpent, the conquest, the fortieth-year markers and the thirty-eight-year
timer's fire), THEN chapter 22 (Balak) — never the next reading first.
Related: [[the-loop-ruling]], [[step9-exam-era]], [[spine-default]].""")
open(p, 'w', encoding='utf-8').write(s + '\n'); print('updated', p)

# ---- the memory: step9-exam-era.md (the sitting-6 line at the STANDING LESSONS head) ----
p = f'{MEM}/step9-exam-era.md'
s = open(p, encoding='utf-8').read()
assert 'THE NUMBERS WALK sitting 6 — CHUKAT' not in s
anchor = "## STANDING LESSONS AND WATCHES (moved verbatim from the MEMORY.md index line on 2026-09-07 to keep the index under its size limit; the W4/W3/W2/W1/D9/G/E lesson tail as it stood)\n"
assert s.count(anchor) == 1
line = "⚠ THE NUMBERS WALK sitting 6 — CHUKAT'S READING (2026-09-11): THE MARKS' ORDER IS NOT THE HAND'S — compare the points as a SET on the consonant (chukat_ink.py's vowels_on), never a typed pointed form by string equality (five asserts fell on it). THE LEG-BY-LEG DIAGNOSTIC — a compound assert's failure names nothing; print each leg once and retype from the print (thirty-two failures → two → one → 0 in three passes, after the measurement pass). THE UNION OF FORMS — an exact-token census needs every prefixed and spelled form, typed from the print (hyssop's article, \"in waters of niddah\", \"at Hormah\", usury's \"at bite\", Meribah's plural, Chemosh with a yod). THE CHECK WORD'S STEM PIECE UNDER SIX, FOUR IN ONE PASS (\"by one slain\", \"at the brook\", \"to spy out\", \"from before\" — the store splits the prefix): choose the stem-bearing word before typing. THE LONG CUT SPLIT, AGAIN (four in chapter 21). THE EXPORT HAS TWO FILES — check the English head against the Hebrew row (the translator REVERSED a frame's addressees at 123:1: a new defect class beside the mistyped heads and citations). THE cd AT THE HEAD OF A COMPOUND COMMAND PERSISTED TO ITS TAIL TWICE MORE (the fourth and fifth instances — the lint loop's relative paths printed nothing; verify_claims from the scratchpad's cwd found no file): the repo-root tools with ABSOLUTE paths in their own call, never after a cd. THE WRITER'S FIRST RUN WITH NO CUT MISS — the tokens typed from the dump hold. THE PARSER'S NEW GAP SITS ON THE PORTION'S OWN NUMBER AGAIN (20:11's dual \"twice\", the consonants of \"seven times\", the patach against the sheva) — and A CLASS CAN BE NAMED AND LEFT when the compile's own instrument will read it (the date-ordinals: the third and seventh day, the first month, 33:38's fortieth year). THE SHELF SILENT ON FIVE MORE CHAPTERS (20-24) and the reading form holding on the translation alone, a third time.\n"
open(p, 'w', encoding='utf-8').write(s.replace(anchor, anchor + line)); print('updated', p)

# ---- MEMORY.md index line ----
p = f'{MEM}/MEMORY.md'
s = open(p, encoding='utf-8').read()
old = "NUMBERS 1:1-18:32 ON THE TAPE. ALL UNCOMMITTED since 0a98276. NEXT: CHAPTER 19 — the heifer's reading (19:1-22, the Sifrei's piska 123 by position), THEN its compile (6b) — never the next reading first."
assert s.count(old) == 1, s.count(old)
new = "NUMBERS 1:1-18:32 ON THE TAPE. 19:1-21:35 READ AND FROZEN (sitting 6, 2026-09-11: 105 sources, 34 claims, 196 units, standing 2023, hash unmoved; the Sifrei's eight piskaot on the heifer, none on 20-24; the dual \"twice\" a new parser gap, the date-ordinals a class named and left; 22:1 read with Balak's draft). ALL UNCOMMITTED since 0a98276. NEXT: THE COMPILE OF CHUKAT (6b) on 1b's order (COMPILE_DEBT's sitting-6 box), THEN chapter 22 (Balak) — never the next reading first."
open(p, 'w', encoding='utf-8').write(s.replace(old, new)); print('updated', p, len(s.replace(old, new).encode()), 'bytes')
print('RECORDS WRITTEN')
