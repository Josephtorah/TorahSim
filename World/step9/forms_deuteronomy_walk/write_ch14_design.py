import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE DEUTERONOMY WALK sitting 12 — CHAPTER 14: THE DESIGN appended to the map (World/step9/DEUTERONOMY_WALK.md) after the measurements and the ink, before a
# row is typed — the section built whole before the file is opened; the map's last section asserted to be 11b's AS BUILT; the lint run after (baseline 0).
# Sitting 11's form (write_ch13_design.py). RUN FROM THE REPO ROOT.
import os, re, subprocess, sys
ROOT = _ROOT
M = f'{ROOT}/World/step9/DEUTERONOMY_WALK.md'
t = open(M, encoding='utf-8').read()
heads = re.findall(r'^## .*$', t, re.M)
assert heads[-1].startswith('## Sitting 11b — THE COMPILE OF CHAPTER 13 — AS BUILT'), heads[-1]
assert '## Sitting 12 — CHAPTER 14' not in t
SEC = '''

## Sitting 12 — CHAPTER 14, Deuteronomy 14:1-29 (2026-09-21; the owner: "Go" after 11b's tail — the commit of chapter 13 still on his word): the reading and the unit — THE DESIGN, written after the measurements and the ink, before a row is typed; ONE RUN + ITS TAIL under THE COST RULES, every step timed; THE ROWS IN TWO HALVES (sitting 11's lesson 4)

THE ONE RUN (timed step by step in the scratchpad's ch14_timing.tsv; the table in the AS BUILT): the rereads (the recovery page, the map's "Sitting 11b … THE
DESIGN" with its docket paragraph, the memory index; THE_STEPS' compiler block, Step 2's head and Step 5's head; the map's "Sitting 11" — the reading's newest
instance, its design and AS BUILT; the 11b box's items owed to 14), the measurements (ch14_dump0.py derived from the forms' ch13_dump0.py by twenty-six asserted
substitutions — chapter 13's fold of the English's 12:32 dropped, the English's chapter 14 counting as the Hebrew's, A0 the identity at cost 17; the spine split
with piska 96's tail folded in — 96:10 fetched from the export by the consonant rule; ch14_measure1.py — chapter 13's helpers and register block by substitution,
its sections chapter 14's own: THE KIN FOUND BY COMPUTATION beside THE LAW KIN NAMED and THE TWIN CHAPTER Leviticus 11 diffed verse by verse, the phrase
censuses, the parser, Onkelos's renderings, the brackets, the store's gloss families, the prior reads, THE REGISTER'S FINDER), THE INK (ch14_ink.py — the generic
helpers COPIED from the forms' ch13_ink.py by content markers, the kin by computation recomputed inside it, 100 asserts typed from the prints: 27 fell on the
FIRST typed pass — every one the INSTRUMENT'S SHAPE, not a fact: the ink's word table holds (token, morph) pairs where the measure's held five, the ink's
Aramaic helper returns a string where the measure's returned tokens, the book-alone name DT is the measure's — and three lists typed from memory against the
print (the antelope's letters Ezekiel 40's cells, the ra'ah's the verb "see", the desire clause's vav); 2 on the second (the ra'ah's two homograph seats, the
sojourner's rendering at 28:43 misassigned from the print's tuple); 0 on the third), THIS DESIGN, then the rows IN TWO HALVES — the food laws (96:9-12, 97-103;
Onkelos 14:1-20; 312:1 and 228:5) and the carcass, the kid and the tithe (104-110; Onkelos 14:21-29; 76:7) — with the clean point taken between them if the
counter nears the cap, else after the ledger; the ledger; THE CLEAN COMPACTION POINT; THE TAIL after the compaction: the display patch, the manifest, the seat,
the chain LAUNCHED with its readers written, the records from the sheet in one call, the forms, the commit message, the timing table.

THE DRAFT: deu_14_food_tithe 14:1-29 — 29 of 29 verses, missing 0 (computed from the DB's verse table: the export's chapter 14 = the DB's, the identity, cost
17; NO fold of the English's numbering this chapter), depends_on deu_13_seducers (frozen) and lev_11_animals_water_birds (frozen — THE TWIN CHAPTER, the draft's
own edge), 36 scenarios and 33 comment lines (the dump's G print), the claim prefix DV14 absent from every unit and manifest (computed). The chapter the unit,
per the ruling CHAPTER NUMBERS; NO PORTION EDGE inside it (Re'eh 11:26-16:17 holds it whole): the ledger deu_14_reeh_2026-09-21.md.

THE SPINE ON THE CHAPTER: the Sifrei on Deuteronomy heads FOURTEEN piskaot in chapter 14 (97 on 14:2, 98 on 14:6, 99 on 14:3, 100 on 14:4, 101 and 102 on
14:6, 103 on 14:11, 104 on 14:21, 105 on 14:22, 106 on 14:23, 107 on 14:24, 108 on 14:27, 109 on 14:28, 110 on 14:29; 96 on 13:17 before, 111 on 15:1 after) —
THE HEADS ARE NOT IN VERSE ORDER (98 on 14:6 sits before 99 on 14:3 and 100 on 14:4; three piskaot head on 14:6), 107 rows in both files (HE = EN at every
piska); AND PISKA 96's TAIL, rows 9-12 on 14:1, which sitting 11 left (96:9 opens with 14:1's citation, 96:11 and 96:12 by their citations, 96:10 by ITS
CONSONANTS — "you shall not cut yourselves … do not make factions" with Amos 9:6 alone in its brackets; chapter 11's lesson 2 a sixth time), so ONE HUNDRED AND
ELEVEN spine rows are read here. The union of both files' citations is 100 rows — 94 inside piskaot 97-110, 96's three by citation, THREE outside: 76:7 (on
12:23 — "you shall not eat it", to include flesh in milk; the English cites 14:21) READ BEFORE at chapter 12's sitting and REREAD WHOLE here, 228:5 (on 22:7
— the bird's nest, "send away the clean"; the English cites 14:11), 312:1 (on 32:9 — "the LORD's portion is His people", the Hebrew cites 14:2); NONE
excluded, no interpolation, no "ibid.", NO slip of the English found. The spine rows without a citation in either file: five (98:4, 100:3, 104:6, 105:2,
110:5). THE PRIOR READS, computed: two reads of two spine rows — 104:8 at chapter 6's sitting (the kid in its mother's milk said three times — the three
covenants), 106:5 at chapter 12's (the firstling whose year passed) — each REREAD WHOLE and marked; 96's first eight rows chapter 13's (asserted from its ledger).

THE KIN, CREDITED BY NAME (the counts computed from the ledgers): THE TWIN CHAPTER — Leviticus 11 read at its sitting in two ledgers (6 and 5 Onkelos rows: the
beasts 11:2-8 (2), the water (1), the birds (1), the swarming fowl (1), the close 11:41-47 (1)); the cuts and the baldness — Leviticus 19:27-28 (2) and 21:5
(1); the holy people — 7:6 (1) at chapter 7, Leviticus 20:26 (1); the carcass and the torn — Leviticus 17:15 (1), 22:8 (1), Exodus 22:30 (1); the kid in its
mother's milk — Exodus 23:19 (1); the tithe — Leviticus 27:30-33 (4), Numbers 18:21-32 (12), 12:6, 12:11, 12:17-19 (5) at chapter 12; the Levite's portion —
10:9 (1), 12:12 (1), Numbers 18:20-24 (3); THE PLACE FORMULA — 12:5, 11, 14, 18, 21, 26 (6); the far place and the desire — 12:15, 20-22 (4); the sojourner,
the fatherless and the widow — 10:18 (1), Leviticus 19:10 (1), 23:22 (1); NO Onkelos row of Genesis 7, 14 or 28, of Exodus 19, 23:10-11 or 34:26 in any ledger
— read through their spines before the Onkelos standing (asserted); NEVER READ AHEAD — no ledger holds an Onkelos row of Deuteronomy 15-26 or of the Prophets
(asserted): 15:1's release, 16:11's and 16:14's rejoicing with the four, 18:1's Levite, 24:19-21's gleanings, 26:12-13's tithe confession wait for their sittings.

THE MEASUREMENTS' FINDS (the design's predictions for the rows; every one asserted in the ink): "YOU ARE CHILDREN OF THE LORD" ONE seat (Exodus 4:22's "My
son, My firstborn" the kin); "YOU SHALL NOT CUT YOURSELVES" the Torah's ONE seat of the root's six (Baal's prophets at Carmel the run's case, 1 Kings 18:28;
Jeremiah's mourners), "baldness" the Torah's two (the priests' 21:5 and this), "BETWEEN YOUR EYES" THE FRONTLETS' PHRASE at its fifth seat, "for the dead" the
Torah's two (26:14 ahead); "A HOLY PEOPLE" THREE in the Bible — 7:6, 14:2, 14:21: the chapter holds two, and 14:2 IS 7:6 with the second "your God" dropped
(18 of 19 tokens in order), "treasure" eight in the Bible (Exodus 19:5 the first; Psalm 135:4 the shelf's own citation at 97:3); "ABOMINATION" the chapter's
one of the book's seventeen — and LEVITICUS 11'S WORD IS "DETESTABLE" (eight seats), this chapter's "abomination" and "unclean": THE TWIN CHAPTER'S VOCABULARY
DIFFERS; "THIS IS THE BEAST" against 11:2's "this is the living thing" — the list's header; THE TEN NAMED HERE AND NOT IN LEVITICUS 11 — the roebuck at
Solomon's table (1 Kings 5:3, 14:5's ONE kin in the Bible by computation), the wild goat and the mountain-sheep hapax, the antelope Isaiah's net (its letters
Ezekiel 40's cells — a homograph), the pygarg a Horite's name; THE TWO SIGNS — 14:6 IS 11:3 with "TWO HOOFS" for "hoofs" (the number the parser reads; ONE seat),
"THE CLEFT ONE" ONE seat (14:7 — the shelf's creature, Chullin 60b at the exam), 14:7 FOLDS 11:4-6's THREE INTO ONE (the camel, the hare and the rock-badger in
one verse), the swine the Torah's two, "of their flesh … their carcass you shall not touch" 11:8's clause verbatim; THE WATER — "fins and scales" five seats,
14:9 12 of 12 tokens of 11:9 in order; THE BIRDS — "every clean bird" before and "every clean fowl" after: THE PERMITTED BIRDS HAVE NO SIGN IN THE INK (the exam's
four signs the shelf's), 14:15 IS 11:16 TO THE LETTER, THE RA'AH AND THE DA'AH — resh for dalet (14:13's three names against 11:14's two: the dayyah added;
the ra'ah's letters the verb "see" at two seats — the shelf's reading of the name), the shalach and the tinshemet moved, the racham spelled rachamah, "after
its kind" four in each; "THEY SHALL NOT BE EATEN" the chapter's one third-person form; LEVITICUS 11:21-22'S LOCUSTS ARE NOT IN THIS CHAPTER; THE CARCASS — 14:21
shares no clause with its three kin (Leviticus 17:15's eater washes, 22:8's priest, Exodus 22:30's dog): THE CARCASS GIVEN TO THE SOJOURNER, NOT CAST TO THE DOG,
"to the sojourner within your gates" ONE seat, "to a foreigner" the Torah's two (23:21 ahead); "THE KID IN ITS MOTHER'S MILK" — THE THIRD AND LAST SEAT (Exodus
23:19 and 34:26 identical verses), "a holy people" the clause before it; THE INFINITIVE ABSOLUTES two — "sell" at 14:21 (the tagger's) and "TITHE, YOU SHALL
TITHE" at 14:22 (the doubling ONE seat; Jacob's vow the form's first seat, Genesis 28:22; the king's tithe the run's, 1 Samuel 8), "year by year" ONE seat, "the
tithe" the Torah's seventeen tokens; THE PLACE FORMULA at its fourth and fifth seats — "to cause His name to dwell" (14:23) and "to put His name" (14:24), both
of chapter 12's forms reused; 12:17's list said again with the firstlings; "LEARN TO FEAR" 4:10's and 17:19's kin, the closest verse in order 16:11's
rejoicing; "THE WAY TOO LONG" — 19:6's refuge road the twin, "THE PLACE TOO FAR" 12:21's clause verbatim (twelve tokens in order): THE FAR PLACE RELEASES THE
FLESH THERE AND THE MONEY HERE, four "when/for" in one verse; "BIND UP THE MONEY IN YOUR HAND" ONE seat (the bundles of Genesis 42:35, Naaman's talents);
"whatever your soul desires" — chapter 12's noun three times, this chapter's verb once (Jeroboam's and Abner's the Prophets' two); "STRONG DRINK" the Torah's
six — the priests' bar, the Nazirite's, the libation's, and HERE PERMITTED; "rejoice, you and your household" ONE seat of the book's eight rejoicings; THE LEVITE
— 12:19's warning said again in a new form (NO token in order), 12:12's clause reused, "portion and inheritance" the Bible's six (Rachel and Leah's the first);
"AT THE END OF THREE YEARS" — Samaria's fall (2 Kings 18:10) the phrase's one kin, "the tithe of your produce" 26:12's clause (THE THIRD YEAR'S TITHE, its
confession ahead); THE FOUR AT THE GATE the formula's first seat (16:11, 16:14 ahead; the "to" form at 24:19-21 and 26:12), "eat and be satisfied" ONE seat in
this form; "THAT THE LORD MAY BLESS YOU IN ALL THE WORK OF YOUR HAND" — 24:19's forgotten sheaf the twin (seven tokens in order). THE REGISTER SPLITS THE
CHAPTER IN TWO: the food laws PLURAL (14:1, 4-20), the tithe SINGULAR (14:22-29), 14:2-3 singular and 14:21 both (the carcass plural, the sojourner and the kid
singular); NO "IF" — the one case on "when" (14:24), the eight "for"s reasons; fifteen negations in ten verses, "you shall eat" fourteen times; no first
person, no imperative, no narrative verb, no "saying", no divine frame — Moses' voice alone, Moses, Israel and Egypt never named; THE NAME eleven tokens, "the
LORD your God" singular five times, plural never; the law's consecutive perfects in the tithe's half alone. THE PARSER: TWO NUMBER VERSES (14:6 "two hoofs"
[2], 14:28 "three years" [3]) and THE STARRED TITHE TOKENS (the number word "ten" inside "tithe" marked at 14:22, 23, 28 and at 12:17, 26:12 — no number read);
the kin's numbers 15:1's and 31:10's seven, Exodus 23:10's six. ONKELOS: "you shall not make incisions" (the Aramaic's own root), "children BEFORE the LORD",
"BELOVED" for "treasured" at its four seats, "abomination" as "what is removed" at eleven, THE SEVEN WILD IN ARAMAIC NAMES (ya'ala, rema, turbala, ditsa — the
Talmud's identifications the exam's, Chullin 80a), "two hoofs" carried, "fins and scales" the Aramaic's own pair, the ra'ah "the daughter of the wing",
"YOU SHALL NOT EAT FLESH WITH MILK" — Onkelos writes the law, not the verse (the English's bracket "[milk with meat]"), "to the UNCIRCUMCISED sojourner" (the
resident alien supplied), "tithe, you shall tithe" doubled, THE SHEKHINAH AT THE PLACE at the formula's nine seats (the chapter's two), "NEW WINE AND OLD" for
wine and strong drink, "portion and inheritance" at the Levite's five, no Memra, no parenthesis. THE STORE = THE DB (351 = 351; NO KETIV); 197 distinct glosses,
25 already rewritten (the "try" of the store "choose", "wealth" "treasure", "goad" "teach"); THE DISPLAY PATCH predicted from the G print at the tail — the
beasts' and birds' names ("and-gazelle" for the mountain-sheep, "and-kind-of-deer" for the roebuck, "and-leaper" for the pygarg), the hoof and the cud
("claw", "break-in-pieces"), the carcass ("flabby-thing"), the money ("and-cramp" for bind, "and-deposit" for lay up), the strong drink ("intoxicant").

THE CLAIMS (seven, DV14-01..07, one manifest; the spine's rows distributed by piska from the CITE INDEX): 01 THE CHILDREN AND THE CUTS (14:1-2 — Onkelos 1-2,
Sifrei 96:9-12, 97, 312:1; the check "you shall not cut yourselves" at 14:1); 02 THE ABOMINATION AND THE BEASTS (14:3-8 — Onkelos 3-8, Sifrei 98, 99, 100,
101, 102; "parts the hoof" at 14:6); 03 THE WATER AND THE BIRDS (14:9-20 — Onkelos 9-20, Sifrei 103, 228:5; "every clean bird" at 14:11); 04 THE CARCASS AND
THE KID (14:21 — Onkelos 21, Sifrei 104, 76:7; "a kid in its mother's milk" at 14:21); 05 THE TITHE AT THE PLACE (14:22-23 — Onkelos 22-23, Sifrei 105, 106;
"tithe, you shall tithe" at 14:22); 06 THE WAY, THE MONEY AND THE LEVITE (14:24-27 — Onkelos 24-27, Sifrei 107, 108; "bind up the money" at 14:25); 07 THE
THIRD YEAR (14:28-29 — Onkelos 28-29, Sifrei 109, 110; "at the end of three years" at 14:28). Seated as seven WITNESS_READ operators at 14:1, 3, 9, 21, 22, 24,
28 with step E. THE FOLD predicted: units 227 -> 228, standing 2245 -> 2252, the hash 8b8fff1fa28953af unmoved (the law layer moves no narrative fact). THE
REGISTER GATE at the reading: no receipt, no header, no footer, no count line in chapter 14 (the finder run — 14:4's "this is the beast" a list's header, not a
register's; the number verses 14:6 and 14:28 no count lines) — GREEN expected, --strict, DECLARED 98 unmoved (the two seats of the block (12:1, 28:69] DAEMONS
since 11b).

THE TESTING SHELF routed to 12b's docket (the union rule at the compile): Mishnah Chullin 3:6-7 and Chullin 59a-66b (the signs of the beasts, the fish, the
birds and the locusts — the shesuah at 60b, the ra'ah at 63b, the seven wild identified at 80a; Sifrei 100-103's own citations); Mishnah Chullin 8:1-4 with
Chullin 113a-116b (flesh in milk — the three seats read three ways, 115b; the kid, the milk, the mother); Mishnah Chullin 4:4 and Chullin 72b-73a (the carcass);
Mishnah Makkot 3:5-6 with Makkot 20a-21a (the cuts and the baldness — the counts of lashes; "for the dead" and the frontlets' "between your eyes"); Yevamot
13b-14a (lo titgodedu — "do not make factions", 96:10's reading); Kiddushin 36a (children of the LORD — R. Judah and R. Meir, 96:9's dispute); Mishnah Maaser
Sheni 1-5 with Kiddushin 54b (the second tithe — the money, its binding, the desire, the wine and strong drink, the redemption, the confession); Mishnah
Maasrot 1:1 (the yield liable); Rosh Hashanah 12b-13a and Bekhorot 53b ("year by year" — not from one year on another; the tithe's new year); Mishnah Peah
8:5-9 and Yevamot 86a-b (the poor man's tithe and the Levite's — Ezra's penalty); Bava Metzia 87b-88b? (the eating in the field — the tithe's onset); Avodah
Zarah 66a? ; the Sifrei's own Mishnah citations read at the rows; the Sifra on Leviticus 11 and 19 credited from their sittings — every row whole; a docket past
~700 rows its own run.

THE ORDER (the rest of the one run): the 111 spine rows WHOLE in both files piska by piska (ch14_spine_p96.txt (rows 9-12) … p110.txt) — THE FIRST HALF 96-103
with Onkelos 14:1-20 and the outside rows 312:1 and 228:5 → ch14_rows_sifrei_96_101.py, _102_103.py, ch14_rows_onkelos.py (14:1-20 typed), ch14_rows_outside.py
→ the clean point if the counter nears the cap; THE SECOND HALF 104-110 with Onkelos 14:21-29 and 76:7 → ch14_rows_sifrei_104_106.py, _107_110.py (chapter
13's form; the cuts by consonants SP_) → write_ch14_ledger.py (from write_ch13_ledger.py's form — the prior reads marked REREAD WHOLE, 76:7 among the outside
rows) → lint 0, coverage computed (the Sifrei 111 + 3; Onkelos 29; the kin's credits by name) → THE CLEAN COMPACTION POINT (the state doc; the recovery page's
section 2; the reread the map's "Sitting 12 … THE DESIGN" — this section) → THE TAIL: ch14_patch_overrides.py (by gloss and by reference from the G print;
the anchors sitting 11's last rows), the ink rerun PATCHED with ch14_ink_body_c.py → write_ch14_manifest.py (seven claims) → seat_ch14.py (seven WITNESS_READ at
14:1, 3, 9, 21, 22, 24, 28; step E) → ch14_gates.sh LAUNCHED in the background (ch14_chain.sh: the seat, verify_text, the ritual; ch14_fold.sh: 228 / 2252 /
the hash unmoved; build_world; the journal gate; the register gate --strict; large_letter_probes; the home-path gate) with write_ch14_records.py and
copy_ch14_forms.py written first → the summary read once → the records from the sheet in one call → the forms copied → the commit message → the timing table →
the report.
'''
assert SEC.count('\n## ') == 1 and 'DV14' in SEC
open(M, 'a', encoding='utf-8').write(SEC)
t2 = open(M, encoding='utf-8').read(); assert t2.endswith(SEC) and t2.count('## Sitting 12 — CHAPTER 14') == 1
print('THE DESIGN appended:', len(SEC), 'bytes; the map', len(t2), 'bytes')
r = subprocess.run(['python3', f'{ROOT}/logic/solo_tools/gloss_lint.py', M], capture_output=True, text=True); print('lint:', r.stdout.strip().split('\n')[-1]); assert r.returncode == 0, r.stdout[-800:]
