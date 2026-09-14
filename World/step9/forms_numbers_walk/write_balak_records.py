#!/usr/bin/env python3
# THE NUMBERS WALK sitting 7 — BALAK (2026-09-11): THE RECORDS — every anchor read from its file and asserted before a byte is written;
# every entry appended (the ledgers append-only; the maps' sections added at their tails; the index lines rebuilt whole).
import re, os
ROOT = '<repo-old>'
MEM = '<memory>'
def rd(p): return open(p, encoding='utf-8').read()
def wr(p, t): open(p, 'w', encoding='utf-8').write(t)
def insert_before(p, anchor, block):
    t = rd(p); assert t.count(anchor) == 1, (p, anchor[:60], t.count(anchor)); wr(p, t.replace(anchor, block + anchor)); print('inserted before', anchor[:50], 'in', os.path.basename(p))
def insert_after(p, anchor, block):
    t = rd(p); assert t.count(anchor) == 1, (p, anchor[:60], t.count(anchor)); wr(p, t.replace(anchor, anchor + block)); print('inserted after', anchor[:50], 'in', os.path.basename(p))
def append(p, block):
    t = rd(p); wr(p, t + ('' if t.endswith('\n') else '\n') + block); print('appended to', os.path.basename(p))
def replace_once(p, old, new):
    t = rd(p); assert t.count(old) == 1, (p, old[:60], t.count(old)); wr(p, t.replace(old, new)); print('replaced in', os.path.basename(p), ':', old[:50])

# 1. NUMBERS_WALK.md — the sitting's section
append(f'{ROOT}/World/step9/NUMBERS_WALK.md', '''
## Sitting 7 — BALAK, Numbers 22:1-25:19 (2026-09-11; the owner: "Continue" after the #130 rereads, on the ruling READ THEN COMPILE): the reading and the units

THE DRAFTS: four cover the span — computed: 115 of 115 verses (41 + 30 + 25 + 19). THE DRAFT'S GRAIN GOVERNS AT BOTH ENDS on sitting 6's own
rule: the portion Balak is 22:2-25:9, but 22:1 (Chukat's last verse) opens the draft num_22_balak_bilam_call and was read with it, and 25:10-19
(Pinchas's opening — the covenant of peace and the Midian command) closes the draft num_25_peor_pinchas and was read with it; the next draft
(num_26_second_census) opens at 26:1. The four: num_22_balak_bilam_call 22:1-41, num_23_oracles_1_2 23:1-30, num_24_oracles_3_4 24:1-25,
num_25_peor_pinchas 25:1-19.

THE SHELF, BY POSITION (balak_ink.py's asserts): the Sifrei on Numbers has NO PISKA on chapters 22, 23 or 24 (computed on every head — the
walk's fourth whole-narrative stretch after 13-14, 16-17, 20-21, read on the translation alone) and ONE piska on 25 — 131 on 25:1, FIVE rows
(rows 1-2 on 25:1-6, rows 3-5 on 25:11-13; the next head, 132, is the second census's 26:53); no piska of its own on 25:10-19. TWO CITATIONS
INSIDE ROW 2 ARE MISTYPED in the export ("Bereshit 48:9" for Genesis 49:9's lion-whelp of Judah; "Devarim 33:32" for Deuteronomy 33:22's Dan —
the chapter has twenty-nine verses), read to their verses (RESEARCH_LOG.md). A NEW DEFECT CLASS: THE EXPORT'S VERSE DIVISION — the Onkelos
export gives chapter 25 EIGHTEEN verses and opens its 26:1 with "It was after the plague": the Masoretic 25:19 (three words, the etnachta — the
mid-verse pause — on its last word and no verse-end mark on the DB's bytes: a paragraph break inside a verse) is joined into the next chapter;
the 25:19 row is cut from 26:1's head (measured on both files). Onkelos 22-25 whole: 115. No prior ledger had read 131 or any verse of 22-25
(grepped — the sitting's own ledgers excluded; 132-136 were read at THE TENT's daughters).

THE READING (seven modules — scratchpad balak_dump.py the first measurement pass; balak_ink.py the ink with every fact an assert (102 asserts);
balak_measure1.py the second pass printing every candidate fact; balak_rows_onkelos22.py, balak_rows_onkelos23.py (23-24), balak_rows_onkelos25.py
the rows; balak_rows_sifrei.py; write_balak_ledgers.py the writer → four ledgers logic/oral_triage/<uid>_2026-09-11.md): 120 sources opened and
verdicted — Onkelos MATERIAL 98 / CONTEXT 17 (34/7, 23/7, 24/1, 17/2 by chapter); the Sifrei MATERIAL 5 / CONTEXT 0 (the script's Counters);
coverage computed, missing 0, extra 0; every quotation CUT by consonants — FIVE misses on the writer's first run, all the shelf's own Aramaic
spellings (the staff, the way, "to speak" twice, "his eyes" — the hand had normalized what the dump printed), none on the second; every
narrative verb glossed by the store's own words.gloss; gloss_lint 0 on all four ledgers on the writer's first successful run.

THE INK, COMPUTED (the measurement pass FIRST — balak_measure1.py printed every candidate fact; the asserts typed from the print; assert_driver.py
then listed THIRTY failures on the first typed pass, the leg-by-leg diagnostic (balak_legs.py) naming forty legs: TWELVE the marks' order in
typed pointed forms (the standing lesson, now met by Unicode normalization on BOTH sides — the diagnostic prints the two codepoint sequences
and their NFC equality), the rest the hand's slices, one FINAL-LETTER miss (Midian's final nun against the regular nun inside "the Midianite"),
and one prefixed form ("in Midian"); then two, then 0):
- THE PARSER MEASURED AGAIN (the standing rule): RIGHT at ten verses — 22:22 [2], 22:28 [3], 22:33 [3], 23:1 [7, 7, 7], 23:4 [7], 23:14 [7],
  23:29 [7, 7, 7], 24:10 [3], 25:8 [2], 25:9 [24000]; SILENT AND RIGHT at three homographs — 23:10's "the fourth part" (rova, the quarter's
  consonants), 24:8's "his arrows" (the half's), 25:18's "their sister" (the feminine one's); ONE GAP ON THE PORTION'S OWN NUMBER — 22:32's "these
  THREE times" written PLENE (shalosh with the vav) reads NOTHING where 22:28 and 22:33's defective spelling read 3: the Torah's three plene seats
  (22:32, Deut 16:16, 19:2), forty-one in the Bible — the compile's probe to FAIL; AND A SECOND GAP FOUND BY THE CROSS-CHECK — the calf's "about
  three thousand men" (Exod 32:28, ki-shloshet alfei) reads 3: the approximation prefix on a construct plural, owed likewise.
- THE FRAMES 3, ALL IN CHAPTER 25 (25:4 "said"; 25:10, 25:16 "spoke"): chapters 22-24 carry NO word of the LORD to Moses — God's nine
  approaches are to Balaam and his ass (came, said, came, was angry, opened the mouth, uncovered the eyes, met, put a word, met), the tenth to
  Moses at 25:4; THE REGISTER 82 verses (22: 38; 23: 21; 24: 10; 25: 13) and SILENT on 33 — the oracles' and the speeches' verses carry no
  narrative verb; 22:23 (the ass sees, turns, goes, is struck) the densest at four.
- THE NAMES OF GOD BY CHAPTER: 22 — the LORD 16, God 6; 23 — the LORD 8, God 2, EL 4; 24 — the LORD 5, God 1, EL 4, SHADDAI 2, THE MOST HIGH 1;
  25 — the LORD 5 alone (El told by the tsere — the long e vowel — from the preposition). El eight times in the oracles and nowhere else in the
  portion; Shaddai the patriarchs' name, Balaam's two the Torah's only other seats; THE MOST HIGH at Melchizedek's four, Balaam's one, Deut 32:8
  — the Torah's two gentile priests share the name; "vision" (machazeh) Abraham's Gen 15:1 and Balaam's two; the UTTERANCE-word in the Torah at
  the Akedah's oath, the decree and Balaam's four verses — "the utterance of the man" is DAVID'S LAST WORDS' form (2 Sam 23:1) and Agur's.
- CHAPTER 22: the plains of Moab the book's last camp (nine datelines to 36:13; Moses climbs from them to die); Moab FEARED (the sojourn-verb's
  consonants) and LOATHED (the manna-loathing verb of 21:5); the ox licking (one seat); Midian's thread (22:4, 7 → 25:6-18); Pethor — Onkelos
  inserts Aram and the Euphrates; "covered the eye of the land" THE LOCUSTS' CLAUSE (Exod 10:5) twice, Onkelos adding "the sun"; THREE
  CURSE-ROOTS, twenty tokens, and ONE SKIN WITH FOUR POINTINGS — Balak's "curse for me", Balaam's "has not cursed", THE ALCOVE and HER BELLY
  (25:8), the four seats this portion's alone; "God came to" — Abimelech, Laban, Balaam twice, three gentiles by night; "the LORD REFUSES" —
  Pharaoh's verb; the house full of silver and gold twice with its deltas; THE AKEDAH'S MORNING (Gen 22:3's saddling and two young men at
  22:21-22); THE SATAN-WORD's two Torah seats both here; "the angel of the LORD" ten times, in the Torah only at Hagar's, the Akedah's and the
  bush's besides; "his sword drawn" PLENE at 22:23, DEFECTIVE at 22:31; THE FOOT AND THE TIMES (Balaam's foot, the ass's "three FEET", Balak's
  "three TIMES" — the two festival-words); "made sport" Egypt's verb; "would there were a sword" — he dies by it; "uncovered the eyes" → his
  title; "I have sinned" Pharaoh's; THE WORD-FORMULA six times, the verb turning and the restrictors akh / efes; the Arnon border 21:13 drew;
  BAMOTH-BAAL the well-song's station.
- CHAPTERS 23-24: seven altars three times, "on the altar" four (Onkelos "every"); "a bare height" (one seat, Onkelos "alone"); GOD MET (the
  chance-verb of Exod 3:18, Gen 24:12, Deut 23:11); THE WORD PUT IN THE MOUTH — Deut 18:18's prophet-clause; "took up his parable" SEVEN — THE
  PARABLE-TELLERS' WORD PAID; Jacob/Israel in six verses; "dwells alone" the leper's words; "who has counted the dust" Abraham's; rova — Reba's
  consonants; the end-word three times, "the end of days" Jacob's; PISGAH — Moses' death-view; "God is not a man" — Samuel over Agag; Onkelos's
  twenty-seven-word sermon; "the shout of a king" — the teruah made the Shekhinah (a wail at 10:5); 23:22 → 24:8 one letter; THE SERPENT AND
  THE OMEN ONE WORD (24:1 = 21:6 in consonants and vowels); Judah's beasts and 24:9 = Gen 49:9 but two words; THE TOP OF PEOR = 21:20's clause
  — the three stands are the last three stations, Peor's thirteen seats to Moses' grave; "as time after time" Samson's; "the spirit of God was
  upon him" — Onkelos "prophecy"; "how goodly" — Psalm 84:2; aloes = tents; "many waters" Meribah's; Agag → Saul → Haman; the crush-verb
  Levi's; Isaac's blessing reversed; Balak claps (one seat); the honor revoked; "I will counsel you" → 31:16; THE STAR AND THE SCEPTER —
  Judah's, Jeremiah 48:45 fusing 21:28 and 24:17, Onkelos "a KING... the MESSIAH"; "shall rule" the creation's verb; the Kenite's nest in the
  SELA (sitting 6's rock-word closed); Kayin; Kittim — DANIEL 11:30 quotes; Eber; Onkelos "the ROMANS... beyond the EUPHRATES"; the retellings.
- CHAPTER 25: SHITTIM the tabernacle's timber; "began" one token three verbs; THE SPEC AND ITS RUN — Exod 34:15-16 at 25:1-2 with the feminine
  "their gods" at both alone; "yoked" — the heifer lid's word PAID; the third anger; HANG them to the LORD before the sun — Saul's sons' verb,
  David's clause; Onkelos inserts the court; the judges of Israel first named; "brought near" the offering-verb; the door of the tent; Phinehas
  born at Exod 6:25; "from the midst" Korach's phrase; the Torah's one spear; "pierced" the Torah's one; "both of them" Deut 22:24's; AND THE
  PLAGUE WAS STAYED — Aaron's incense clause, and "he atoned for" Aaron's verb (17:12-13 ↔ 25:8, 13): the Sifrei's father-son title measured on
  the ink; 24,000 and 14,700 the formula's two seats; Simeon 59,300 → 22,200; the zeal-root the sotah's; the covenant of peace (Malachi's Levi);
  everlasting priesthood Exod 40:15 narrowed; THE FORM TAGGED PAST WHERE THE SIFREI READS A FUTURE; Zur of the five kings; "head of the peoples"
  Ishmael's word; HARASS — the trumpets' root and HAMAN THE AGAGITE's title in Esther; "wiles" Joseph's brothers'; "after the plague" the broken
  verse.
- THE TRANSLATION'S OWN WORDS, cut from the shelf's bytes (the ledgers' full lists): a Word from before the LORD for every coming; no will for
  the refusing; the decree of the Word for the mouth; Aram and the Euphrates at Pethor; the sun on the land's eye; three TIMES for the feet;
  "every altar"; "alone" for the height; the Word met; the sermon at 23:19; the Shekhinah for the shout; strength for the wild-ox; land for the
  tents, spices for the aloes, the Euphrates for the river; a king for the buckets; a KING and the MESSIAH for the star and the scepter; the
  Shalmaite for the Kenite; the Romans for Kittim, beyond the Euphrates for Eber; errors for gods; judge and kill for hang; a decree for the
  giving; twenty and four for four and twenty; 25:19 at 26:1's head.

THE SIFREI'S OWN CASE LAW (five entries appended to MIDDOT.md "The middot's own case law"): THE ADJACENCY RULE DISPUTED ON THE VERSE — R. Akiva's
"every juxtaposed section is learned from its neighbor" (24:14's counsel → 25:1's daughters) against Rebbi's "many adjoining sections are as far
apart as east from west" with three counter-exemplars each closed by a parable (131:1) — the Numbers seat of the file's adjacency-validity
parameter, and the ink's own back-reference at 31:16 beside it; the god's own service as the offence's definition (baring to Peor, 131:2 —
Mishnah Sanhedrin 7:6); a law's installation DATED by the shelf (the wine of idolaters "not yet forbidden", 131:2); a three-generation title read
as three deeds (131:3); "not 'to atone' but 'and he will atone'" — the tense read off the vav-form against the morphology's tag (131:5). ONE
MOVE EXEMPLAR ADDED: M-22 (the run teaches the spec) gains Exod 34:15-16 → Num 25:1-2 (MOVE_CATALOG.md).

THE CLAIMS (write_balak_manifests.py → four manifests, 40 claims — BK22A ×10, BK23A ×10, BK24A ×10, BK25A ×10 — every check cut from the
store's bytes; the ID prefixes asserted absent from every manifest and unit; every source cite checked against its ledger's CITE INDEX):
verify_claims 40 VERIFIED / 0 FAILED; claim_labels_census --strict GREEN (Numbers 285 labeled 285, debt 0; the labels ink, E10, E2, E28, M-22).
THE SEATS (seat_balak.py): 40 WITNESS_READ operators at the claims' first verses, step E, the scenarios in the anchor form; verify_text GREEN ×4.
THE RITUALS (four in sequence): every gate PASS — RITUAL COMPLETE ×4: 197, 198, 199, 200 frozen units; the Python rendering layer written for
each. THE CORPUS REBAKED (predicted before the fold: units 200, standing 2023 + 40 = 2063, hash unmoved): units 200, facts 1809, demands 341
(191 open), events 557, names 81, standing 2063, hash 8b8fff1fa28953af — the prediction matched; CORPUS TRUTH GREEN. THE STAMP: one delegated
FULL RULE row for the four (logic/findings/STAMP_LEDGER.md). No engine file changed at this sitting — the sweep and the journal gate stand as
at 6b's close.

OWED TO THE COMPILE (sitting 7b; also in COMPILE_DEBT's box): (a) THE PARSER — THE PLENE "THREE" (22:32; Deut 16:16, 19:2; forty-one seats in
the Bible — a probe to FAIL, the corpus-wide diff read) and THE APPROXIMATION PREFIX ON A CONSTRUCT PLURAL (Exod 32:28's "about three thousand"
read 3 — a probe to FAIL; the class measured over the four books); (b) THE FUNCTIONS — THE WORD-FORMULA AND ITS RESTRICTORS as a compiled
restrictor class (akh / efes — 13:5's export-operator kin), the three curse-roots as data; THE THREE STANDS as a state machine on the stations
of 21:19-20 (Bamoth, Pisgah, Peor by CALL to chukat's well cell), the offerings (seven altars × three, forty-two beasts — Zevachim 116a's
gentile burnt offering the exam's row); THE BLESSING FORMULA by CALL to the Genesis engines (Gen 12:3, 27:29 — the reversal a data row);
THE PEOR ENGINE — the sin as the RUN of Exod 34:15-16's spec (the family engine's intermarriage clause by CALL), the hanging by the judges
(Sanhedrin 35a; Jethro's 78,600 × 2 the exam's arithmetic — the courts engine by CALL), THE ZEALOUS-SMITE RULE INSTALLED BY A DEED (Mishnah
Sanhedrin 9:6 — "the law is not taught": rule_installed by an act, the second seat of THE TENT's form), Phinehas's priesthood by the deed
(Zevachim 101b — the priesthood engine's status change by CALL), the covenant of peace a HEAVEN entry in force forever, THE PLAGUE a heaven
entry on the people CLOSED at 25:8 by the spear (the count 24,000 a data row; Simeon's delta a checkpoint at the second census, 26:14 by CALL
at the next sitting), the Midian command (25:17) a DEBIT on Israel closed at 31:7 (Matot), Balaam's death (31:8) the ass's sword-clause closed,
the decree on gentile wine DATED after Peor (the shelf's own data row, Avodah Zarah 36b); (c) THE TAPE — no date in the ink (the fortieth year
continues from 21:35; Seder Olam places Balaam after Aaron's death; the plague's day undated; 25:19's "after the plague" the second census's
marker — the next reading's); the entities balak, balaam, the she-ass (an entity by the LORD's opening of its mouth), moab, midian, phinehas,
zimri, cozbi, the plague; the three angers as three writes; the edges balak → chukat (21:13's border, the stations, 19:15's lid, 21:6's
serpents), → pre_sinai (Gen 12:3; 20:3's "God came"), → family (Gen 27:29, 49:9-10, 34:25), → pesach (Exod 10:5's locusts), → the courts
(Exod 18:21), → sotah (5:14's zeal), → korach (16:21, 17:12-13), → erection / vestments (Exod 40:15, 29:8), → priesthood, → sanctions
(Deut 22:24's "both"), → holiness (Lev 18:23, 18:18, 13:46), → moadim (the teruah; Exod 23:14, 17's three times), → bamidbar (Simeon's
census), sequence → balak; the retellings as run citations (Deut 4:3, 23:5-6, 34:6; Josh 13:22, 22:17, 24:9-10; Judg 11:25; 1 Sam 15:29;
2 Sam 21:6-9, 23:1; Jer 48:45; Mic 6:5; Ps 106:28-30; Dan 11:30; Neh 13:2); the exam docket by the union rule (Sanhedrin 105a-106b whole;
Mishnah Sanhedrin 7:6, 9:6, 10:2; Sanhedrin 35a, 60b-64a, 81b-82b, 90a; Avot 5:6, 5:19; Berakhot 7a, 12b, 21b; Avodah Zarah 4a-b, 36b;
Makkot 10b; Nazir 23b; Sotah 47a; Horayot 10b; Niddah 31a; Bava Batra 14b-15a, 60a; Zevachim 101b, 116a; Bava Kamma 110b; Yoma 9a, 18a;
Taanit 20a; Yevamot 4a; Yerushalmi Taanit 4:5, Sanhedrin 10:2; Seder Olam 9-10).

⚠ LESSONS (7): THE MARKS' ORDER, A THIRD TIME — twelve of thirty asserts fell on typed pointed forms whose codepoints the DB orders otherwise;
THE INSTRUMENT IS NORMALIZATION ON BOTH SIDES (NFC), and the leg diagnostic now prints the two sequences and their NFC equality. THE FINAL LETTER
INSIDE A GENTILIC — a substring test on "Midian" (final nun) misses "the Midianite" (regular nun); the census names its forms. THE EXPORT'S VERSE
DIVISION CAN DIFFER FROM THE MASORETIC (25:19 joined into 26:1) — the row is cut from the neighbor's head and the class named; the DB's
etnachta without a verse-end mark is the half-verse's own signature. THE DRAFT'S GRAIN GOVERNS AT BOTH ENDS (22:1, 25:10-19) — sitting 6's rule
applied to a tail as to a head. THE PARSER'S NEW GAP ON THE PORTION'S OWN NUMBER, A FOURTH TIME (the plene three) — AND A CROSS-CHECK ON A
PLAGUE COUNT FOUND AN OLD ONE (the calf's 3,000 read 3 since the parser's first day). THE WRITER'S CUT MISSES WERE THE SHELF'S SPELLINGS — five
Aramaic tokens the hand normalized (plene for defective, a doubled letter): type the Aramaic from the plain-token print, never re-spell it.
THE SHELF'S CITATIONS INSIDE A ROW MISTYPED AGAIN (two in one row — the fourth and fifth of the walk). THE SHELF DISAGREES WITH ITSELF ON A
NUMBER (eighty high priests against three hundred) AND WITH THE MORPHOLOGY ON A TENSE (25:13's vav-form) — both recorded as disputes, neither
adjudicated. THE READING SITTING'S SHAPE HELD: dump → ink asserts (30 → 2 → 0 by the leg diagnostic) → rows → writer (5 misses → 0, lint 0
first run) → manifests (40/40) → seats → rituals (4/4) → the fold predicted and matched.

NEXT on the ruling: THE COMPILE OF BALAK (7b) on 1b's order — the docket, the two parser probes to FAIL, the stands, the formula's restrictors,
the Peor engine with the rule installed by a deed, the plague closed by the spear, the Midian debit, the tape's undated stretch — before
chapter 26 (the second census), never the next reading first.
''')

# 2. COMPILE_DEBT.md — the 7b box
append(f'{ROOT}/World/step9/COMPILE_DEBT.md', '''
## OWED TO THE COMPILE — SITTING 7b (THE NUMBERS WALK sitting 7, BALAK 22:1-25:19 READ AND FROZEN 2026-09-11; NUMBERS_WALK.md "Sitting 7"): (a) THE PARSER — THE
## PLENE "THREE" (22:32 shalosh with the vav; Deut 16:16, 19:2; forty-one seats in the Bible — a probe to FAIL, the corpus-wide diff read) and THE APPROXIMATION
## PREFIX ON A CONSTRUCT PLURAL (Exod 32:28 "about three thousand men" reads 3 — found by the plague-count cross-check; a probe to FAIL, the class measured over the
## four books); (b) THE FUNCTIONS — the word-formula's restrictors (akh / efes) as a compiled class and the three curse-roots as data; the three stands on 21:19-20's
## stations by CALL to chukat's well cell; the seven altars × three (Zevachim 116a's gentile burnt offering the exam's row); the blessing formula by CALL to the
## Genesis engines (Gen 12:3, 27:29 — the reversal a data row); THE PEOR ENGINE: the sin as the RUN of Exod 34:15-16 (the family engine by CALL), the hanging by the
## judges (Sanhedrin 35a — the courts engine; Jethro's 78,600 × 2 the exam's arithmetic), THE ZEALOUS-SMITE RULE INSTALLED BY A DEED (Mishnah Sanhedrin 9:6 —
## rule_installed by an act, THE TENT's form at a second seat), Phinehas's priesthood by the deed (Zevachim 101b — the priesthood engine's status change), the
## covenant of peace a HEAVEN entry in force forever, THE PLAGUE a heaven entry on the people CLOSED at 25:8 (24,000 a data row; Simeon's delta a checkpoint at the
## second census), the Midian command (25:17) a DEBIT on Israel closed at 31:7 (Matot), Balaam's death at 31:8 closing the ass's sword-clause, the decree on gentile
## wine DATED after Peor (Avodah Zarah 36b — the shelf's own data row); (c) THE TAPE — no date in the ink (the fortieth year continues; no text-constrained marker;
## the plague undated; 25:19's "after the plague" the second census's marker at the next reading); the entities balak, balaam, the she-ass, moab, midian, phinehas,
## zimri, cozbi, the plague; the three angers; the edges balak → chukat / pre_sinai / family / pesach / the courts / sotah / korach / erection / vestments /
## priesthood / sanctions / holiness / moadim / bamidbar, sequence → balak; the retellings as run citations (Deut 4:3, 23:5-6, 34:6; Josh 13:22, 22:17, 24:9-10;
## Judg 11:25; 1 Sam 15:29; 2 Sam 21:6-9, 23:1; Jer 48:45; Mic 6:5; Ps 106:28-30; Dan 11:30; Neh 13:2); the exam docket by the union rule (Sanhedrin 105a-106b whole;
## Mishnah Sanhedrin 7:6, 9:6, 10:2; Sanhedrin 35a, 60b-64a, 81b-82b, 90a; Avot 5:6, 5:19; Berakhot 7a, 12b, 21b; Avodah Zarah 4a-b, 36b; Makkot 10b; Nazir 23b;
## Sotah 47a; Horayot 10b; Niddah 31a; Bava Batra 14b-15a, 60a; Zevachim 101b, 116a; Bava Kamma 110b; Yoma 9a, 18a; Taanit 20a; Yevamot 4a; Yerushalmi Taanit 4:5,
## Sanhedrin 10:2; Seder Olam 9-10). The two Chukat rows this reading PAID on the ink: the parable-tellers' word (21:27 → Balaam's seven) and 19:15's lid (→ 25:3).
''')

# 3. RESEARCH_LOG.md — the sitting's entry
append(f'{ROOT}/RESEARCH_LOG.md', '''
## 2026-09-11 — THE EXPORT JOINS A HALF-VERSE INTO THE NEXT CHAPTER, TWO MISTYPED CITATIONS IN ONE ROW, THE PLENE THREE,
## THE CALF'S THREE THOUSAND READ THREE, AND THE MARKS' ORDER MET BY NORMALIZATION
## (THE NUMBERS WALK sitting 7 — Balak's reading, Numbers 22:1-25:19; the four ledgers logic/oral_triage/num_22..25_*_2026-09-11.md)

(1) THE EXPORT'S VERSE DIVISION DIFFERS FROM THE MASORETIC AT 25:19. The Onkelos Numbers export gives chapter 25 EIGHTEEN verses (the
Tanakh DB and the snapshot store nineteen) and opens its 26:1 with "It was after the plague. And the LORD said to Moses and to Eleazar...":
the Masoretic 25:19 — "and it was after the plague", three words, whose last carries the ETNACHTA (the mid-verse pause accent) and NO
verse-end mark on the DB's bytes (the Masorah's paragraph break inside a verse; the store's tokens "and-be", "hind-part", "the-pestilence")
— is joined into the next chapter. Measured on both export files; the 25:19 row was cut from 26:1's head with the join named in the row. A
FOURTH DEFECT CLASS beside the mistyped heads, the mistyped citations and the reversed frame: the verse grid itself can differ, and a
reader that indexes the export by (chapter, verse) falls off the end of chapter 25 (the first dump did, with an IndexError).

(2) TWO CITATIONS MISTYPED INSIDE ONE SIFREI ROW (131:2): "Bereshit 48:9" for "a lion's whelp is Judah" — the verse is GENESIS 49:9 (the
clause 24:9 quotes word for word but two); "Devarim 33:32" for "Dan is a lion's whelp" — the verse is DEUTERONOMY 33:22, the chapter having
twenty-nine verses. Read to their verses; the fourth and fifth mistyped citations of the walk (three at Korach).

(3) THE PLENE THREE — A PARSER GAP ON THE PORTION'S OWN NUMBER, THE FOURTH TIME. 22:32 "these three times" writes "three" PLENE (with the vav)
where 22:28 and 22:33 write it defective; the engine reads 3 at the two defective seats and NOTHING at the plene one. The plene form's
seats in the Torah are three (Num 22:32, Deut 16:16 "three times a year", Deut 19:2 "three cities"), forty-one in the Bible (Chronicles,
Daniel, Esther, Ezekiel, Job the bulk) — computed on every verse. Owed to the compile with a probe to FAIL.

(4) THE CALF'S THREE THOUSAND READ THREE. The plague-count cross-check (17:14's 14,700, 25:9's 24,000, 2 Sam 24:15's 70,000 all read right)
ran Exod 32:28 "and there fell of the people that day about three thousand men" — and the parser returned [3]: "about three thousands of
men" (ki-shloshet alfei ish) carries the approximation prefix on a construct plural, and the class has been misread since the parser's
first day. Owed to the compile with a probe to FAIL and the class measured over the four books.

(5) THE MARKS' ORDER MET BY NORMALIZATION. Twelve of the thirty first-pass assert failures were typed pointed forms whose combining marks
the DB orders otherwise (a dagesh before or after the vowel, a shin-dot before or after the sheva); the leg-by-leg diagnostic printed the
two codepoint sequences and their NFC equality (True at every one), and the module now compares after Unicode normalization on BOTH sides
(npt / ptn / NL). The same fact was met at sitting 6 by a set-comparison of the marks on one consonant; NFC is the general instrument.

(6) THE FEMININE "THEIR GODS" AT TWO SEATS. Exodus 34:16 ("their daughters whore after THEIR gods", the feminine plural suffix) and Numbers
25:2 ("the sacrifices of THEIR gods", the daughters') are the only two seats of the form in the Bible — the spec's rare word at its run.

(7) JEREMIAH 48:45 FUSES TWO NUMBERS VERSES. "For a fire went out from Heshbon and a flame from the midst of Sihon, and devoured the corner
of Moab and the crown of the sons of tumult": the first half is 21:28 (the parable-tellers' fire — four exact tokens shared, sitting 6), the
second 24:17 ("crushes the corners of Moab and breaks down all the sons of Sheth" — "the corner of Moab" the phrase's only other seat). One
prophetic verse built from the poets' line and Balaam's.

(8) THE SERPENT AND THE OMEN IN ONE POINTED SKIN. 24:1's "divinations" (nechashim) and 21:6's "the serpents" (ha-nechashim) share consonants
AND vowels — only the article and the story tell the fiery serpents from the diviner's art; 23:23's "no divination in Jacob" is the same
consonants with other points. Measured on the DB's bytes.

(9) THE SHELF AGAINST THE MORPHOLOGY, AND AGAINST ITSELF. 25:13's "and he atoned" is tagged by the morphology as the intensive stem's
narrative past (the "and he did" form) and rendered past by Onkelos; the Sifrei (131:5) reads it as a FUTURE ("it is not written 'to atone'
but 'and he will atone': he stands and atones until the revival of the dead"). And the Sifrei's "eighty high priests in the second Temple"
(131:4) stands against Yoma 9a's "more than three hundred". Both recorded as disputes, neither adjudicated.

(10) THE WRITER'S FIVE CUT MISSES WERE THE SHELF'S SPELLINGS: the Aramaic tokens for the staff (defective), the way (plene), "to speak"
(twice, one lamed not two) and "his eyes" (defective) — the hand had re-spelled what the dump printed. The rule: the Aramaic is typed from
the plain-token print, never from memory of the pointed line.
''')

# 4. MIDDOT.md — the case-law entry before the Exodus campaign header
insert_before(f'{ROOT}/logic/MIDDOT.md', '## Exodus block campaign — owner\'s word "Do 3")', '''- THE SIFREI'S OWN CASE LAW ON BALAK (the Sifrei on Numbers piska 131 on
  25:1-13 — its one piska on the portion; THE NUMBERS WALK sitting 7,
  2026-09-11 — the ledger logic/oral_triage/num_25_peor_pinchas_2026-09-11.md):
  (1) THE ADJACENCY RULE DISPUTED ON THE VERSE (131:1). R. AKIVA: "every
  section juxtaposed with another is to be learned from it" — 24:14's
  "come, I will counsel you" stands above 25:1's daughters of Moab, so
  the counsel is the harlotry (E28, from-the-preceding); REBBI: "there
  are many adjoining sections in the Torah as far from each other as
  east from west" — Exod 6:12-13, Lev 21:9-10, Hos 1:9-2:1, Hos 14:1-2,
  each gap closed by a PARABLE (E26): the centurion who fled before his
  promotion, the king who doubled the ketubah (the marriage settlement)
  instead of the divorce, the general who told the province "send me
  something to relay to the king". The Numbers seat of the file's
  ADJACENCY-VALIDITY parameter (the Exodus campaign's Yevamot 4a
  entry): here the two sides are named tannaim (the Mishnah's
  teachers) on a narrative seat, and the ink carries the link itself —
  31:16 "by the word of Balaam... in the matter of Peor" (computed).
  (2) THE GOD'S OWN SERVICE AS THE OFFENCE'S DEFINITION (131:2): "the
  sages ruled that baring oneself to Peor is its mode of worship" —
  the rite's form read off the story (the harlot's "bare yourself
  before him"), Mishnah Sanhedrin 7:6 the answer sheet; the three
  anecdotes of gentiles' own scorn beside it. (3) A LAW'S INSTALLATION
  DATED BY THE SHELF (131:2): "the pitcher was full of Ammonite wine,
  the wine of idolaters having NOT YET BEEN FORBIDDEN to Israelites" —
  the decree's time-stamp relative to the event, a data row for the
  installation ledger (Avodah Zarah 36b). (4) A THREE-GENERATION TITLE
  READ AS THREE DEEDS (131:3): "Phinehas son of Eleazar son of Aaron
  the priest" — priest son of priest, zealot son of zealot (Levi at
  Shechem, Gen 34:25), turner-away of wrath son of a turner-away
  (Aaron, 17:13) — and the ink pairs them itself: "and the plague was
  stayed" at 17:13 and 25:8, "and he atoned for" at 17:12 and 25:13
  (computed). (5) THE TENSE READ OFF THE VAV-FORM (131:5): "it is not
  written 'to atone' (the infinitive) but 'and he will atone'" — the
  form read as a future ("he stands and atones until the revival of
  the dead") where the morphology tags the narrative past and Onkelos
  renders a past: a dispute on one word's tense, recorded. One move
  exemplar added: M-22 (the run teaches the spec) — Exod 34:15-16's
  "they whore after their gods... and call you and you eat of their
  sacrifice... and their daughters whore after THEIR gods" run clause
  by clause at 25:1-2, the feminine "their gods" at the two seats alone
  (MOVE_CATALOG.md).

''')

# 5. MOVE_CATALOG.md — the M-22 exemplar, before the M-23 header
t = rd(f'{ROOT}/logic/MOVE_CATALOG.md')
m = re.search(r'\n## M-23 ', t); assert m, 'M-23 header'
insert_before(f'{ROOT}/logic/MOVE_CATALOG.md', t[m.start():m.end()], '''
A NUMBERS EXEMPLAR (2026-09-11, THE NUMBERS WALK sitting 7 — Balak's
reading): THE SPEC Exodus 34:15-16 — "lest you make a covenant with the
inhabitants of the land, and they whore after their gods and sacrifice to
their gods, and one CALLS you and you EAT of his sacrifice, and you take
of their DAUGHTERS for your sons, and their daughters whore after THEIR
gods" — and THE RUN Numbers 25:1-2: "the people began to whore after the
DAUGHTERS of Moab; and they CALLED the people to the sacrifices of THEIR
gods, and the people ATE and bowed to their gods" — the spec's clauses
run in order (the daughters, the whoring, the calling, the sacrifices,
the eating), and the spec's rare word, the FEMININE plural "their gods"
(the daughters' gods), stands in the Bible at the spec (34:16) and the
run (25:2) alone (computed on every verse). The Sifrei's teacher on the
pair is the juxtaposition reader of piska 131:1 (R. Akiva); the pair
itself is the ink's — filed as the run-teaches-spec form's Numbers
exemplar, the claim BK25A-01 labeled M-22 with this exemplar named.
''')

# 6. STAMP_LEDGER.md — the row
append(f'{ROOT}/logic/findings/STAMP_LEDGER.md', "| 2026-09-11 | num_22_balak_bilam_call, num_23_oracles_1_2, num_24_oracles_3_4, num_25_peor_pinchas | DELEGATED | FULL RULE | Numbers 22:1-25:19 derivation 2026-09-11 (THE NUMBERS WALK sitting 7 — BALAK; the owner: \"Continue\" after the #130 rereads, on the ruling READ THEN COMPILE; the THIRTY-FOURTH through THIRTY-SEVENTH NUMBERS UNITS, read at the PARASHAH GRAIN in one pass, the ledgers per block; the draft's grain governing at both ends — 22:1 Chukat's last verse and 25:10-19 Pinchas's opening read with their drafts): declared reading COMPLETE on every block — Onkelos Numbers 22, 23, 24, 25 whole, 115 verses (41 / 30 / 25 / 19; the export's 25:19 cut from its 26:1 head — the export joins the half-verse into the next chapter, RESEARCH_LOG.md), and the Sifrei on Numbers piska 131 FOUND BY POSITION (5 rows at the shelf's row grain on 25:1-13; NO piska on chapters 22-24 — computed on every head of the export, the shelf's silence on the whole Balaam story as on the spies, the rebellion and Chukat's road; two citations inside row 2 mistyped, read to their verses; no prior ledger had read the row or the verses — grepped); coverage COMPUTED by script against the shelf's own counts (missing 0, extra 0 on every block); every quotation cut from the DB's and the shelf's bytes by consonants (five misses on the writer's first run, the shelf's own spellings, none on the second); the ink facts computed and asserted (102 asserts, thirty failures on the first typed pass read leg by leg — the marks' order met by normalization on both sides); the engine's parser measured on the portion's numbers (right at ten, silent-and-right at three homographs, ONE GAP the plene three, and the calf's three thousand found read three by the cross-check); 40 claims VERIFIED 0 FAILED (verify_claims, every check cut from the store's bytes), claim_labels_census --strict GREEN (Numbers 285 labeled, debt 0), 40 WITNESS_READ operators seated by script with every cite checked against the ledgers' cite indexes, verify_text GREEN ×4, freeze_ritual PASS on every gate ×4 (RITUAL COMPLETE — 197, 198, 199, 200 frozen units), the corpus rebaked (200 units, standing 2063 = 2023 + 40 as predicted, hash 8b8fff1fa28953af unmoved), the Python rendering layer written ×4, gloss_lint 0 on all four ledgers. Machine-administered under the 2026-09-01 delegation; labeled DELEGATED; the owner may overrule. |\n")

# 7. THE_STEPS.md — the sitting paragraph
replace_once(f'{ROOT}/THE_STEPS.md', "to be the house's dipping order, not the takings'. Next: chapter 22\n(Balak's reading), then its compile.\n\n## THE FINDINGS LOOP",
             "to be the house's dipping order, not the takings'.\n\nSITTING 7 — BALAK (Numbers 22:1-25:19, 2026-09-11, on Brian's\n\"Continue\" after the #130 rereads; NUMBERS_WALK.md \"Sitting 7\"). The\nshelf was silent on the whole Balaam story — no piska on chapters 22,\n23 or 24, computed on every head — and spoke once on 25 (piska 131, five\nrows on Shittim, Peor, Phinehas and the covenants), so the seer's four\nchapters were read on the translation alone; the draft's own edges\ngoverned the span (22:1, Chukat's last verse, and 25:10-19, Pinchas's\nopening, read with their drafts). The ink's finds computed on every verse:\nthe Akedah's morning at Balaam's (rose, saddled, two young men); the\nsatan-word's only two Torah seats; God coming by night to three gentiles;\nPharaoh's verbs in Balaam's story (refuses, made sport, I have sinned);\nthe word-formula six times with its verb turning and its restrictors;\nthe ass struck \"three feet\" and the blessings counted \"three times\" — the\ntwo festival-words; the three stands on the last three stations of the\nwell's road, the third the god of the sin; the parable-tellers' word paid\nseven times over; Samuel's verse over Agag restating Balaam's; the\nserpent and the omen one pointed word; Judah's blessing quoted but two\nwords; Jeremiah fusing the poets' fire with Balaam's corner; the tents\nmade land and the star made a king in the translation; Kittim quoted in\nDaniel; Shittim the tabernacle's timber; Exodus 34's warning run clause\nby clause with its feminine \"their gods\" at both seats alone; the curse\nBalak asked for spelled into the alcove where the plague stopped; Aaron's\nincense-clause at Phinehas's spear; the sotah's jealousy-word in the\npriest's deed; Cozbi's father among Midian's five kings; the harass-word\nthat is Haman's title. The parser read ten numbers right and missed the\nplene \"three\" (a new gap on the portion's own number) — and the\nplague-count cross-check found the calf's \"about three thousand\" read as\nthree since the parser's first day. The shelf's export joined the\nhalf-verse 25:19 into its 26:1 (a new defect class) and mistyped two\ncitations in one row; the Sifrei's adjacency rule was found disputed on\nthe verse between R. Akiva and Rebbi, and its reading of \"and he atoned\"\nas a future recorded against the morphology. Four units frozen (200),\nforty claims seated and checked, the fold matching its prediction. Next:\nBalak's compile (7b), then chapter 26 (the second census).\n\n## THE FINDINGS LOOP")

# 8. THE_BRIEFING.md — the scoreboard entry and the count line
insert_after(f'{ROOT}/THE_BRIEFING.md', '## SCOREBOARD (as of 2026-09-11, latest)\n\n', "- **BALAK READ AND FROZEN — SITTING 7 DONE: THE SHELF SILENT ON THE WHOLE BALAAM STORY, THE AKEDAH'S MORNING AT BALAAM'S, THE CURSE BALAK ASKED FOR SPELLED INTO THE TENT WHERE THE PLAGUE STOPPED, AND THE EXPORT JOINING A HALF-VERSE INTO THE NEXT CHAPTER** (2026-09-11, on your \"Continue\" after the #130 rereads; NUMBERS_WALK.md \"Sitting 7\"). Numbers 22:1-25:19 read at the parashah grain with the drafts' own edges (22:1 and 25:10-19 read with their drafts): the Sifrei has no piska on 22-24 (computed on every head) and one on 25 — 131, five rows — so the seer's chapters were read on Onkelos alone; 120 sources, four ledgers, coverage computed. THE FINDS, computed: Balaam's morning is Abraham's (Gen 22:3's saddling and two young men); the satan-word's two Torah seats both here; God comes by night to Abimelech, Laban and Balaam alone; the LORD \"refuses\" in Pharaoh's verb, Balaam \"has sinned\" in Pharaoh's confession; the word-formula six times, its verb turning; the ass struck \"three feet\", the blessings counted \"three times\"; the three stands are the well-road's last three stations, the third the god of 25:3; the parable-tellers' word paid; Samuel over Agag restates \"God is not a man\"; the serpent and the omen one pointed word; 24:9 is Judah's blessing but two words; Jeremiah 48:45 fuses 21:28 and 24:17; Onkelos makes the tents land and the star a king; Daniel quotes \"ships from Kittim\"; Shittim is the tabernacle's timber; Exodus 34:15-16 runs at 25:1-2 with its feminine \"their gods\" at both seats alone; Balak's \"curse for me\" and the alcove of 25:8 one skin; Aaron's plague-clause and atonement-verb at Phinehas's; the sotah's jealousy-word in the priest's deed; Zur among Midian's five kings; \"harass\" is Haman the Agagite's title. The parser: ten right, the plene \"three\" a new gap, and the calf's 3,000 found read 3. The shelf: 25:19 joined into 26:1 by the export (a fourth defect class), two mistyped citations in one row, the adjacency rule disputed on the verse (R. Akiva against Rebbi), \"and he atoned\" read future against the tag. 40 claims verified, 40 operators seated, four rituals green, 200 frozen units, standing 2063 as predicted, hash unmoved; gloss_lint 0 on the ledgers first run. Next: Balak's compile (7b), then chapter 26.\n")
replace_once(f'{ROOT}/THE_BRIEFING.md', '196 units, standing 2023, hash unmoved; 53 daemons; the sweep 48/48 runners green at 5,613 cells; Numbers 1:1-21:35', '200 units, standing 2063, hash unmoved; 53 daemons; the sweep 48/48 runners green at 5,613 cells; Numbers 1:1-25:19 read and frozen, 1:1-21:35')

# 9. World/RESUME.md
append('<world-link>/RESUME.md', "SITTING 7 DONE 2026-09-11 (BALAK 22:1-25:19 READ AND FROZEN; NUMBERS_WALK.md \"Sitting 7\"; the draft's grain at both ends — 22:1 and 25:10-19 read with their drafts): the Sifrei's one piska 131 on 25:1-13 (five rows; none on 22-24, computed; two citations inside row 2 mistyped; the export joining 25:19 into its 26:1 — a fourth defect class) + Onkelos whole (115) = 120 sources in four ledgers (seven modules; 102 asserts, thirty failures on the first typed pass — twelve the marks' order, met by NFC on both sides; five cut misses the shelf's spellings, none on the second run); 40 claims verified and labeled, 40 operators seated, four rituals → 200 units, standing 2063, hash unmoved, the fold matching its prediction; the parser right at ten, ONE GAP the plene \"three\" (22:32), and the calf's \"about three thousand\" found read 3 by the cross-check; the crowns in the file (the Akedah's morning, the satan-word's two seats, the three gentiles' night visits, Pharaoh's verbs, the word-formula's six, the feet and the times, the three stands on the stations, the parable-tellers' word paid, Samuel over Agag, the serpent and the omen, Judah's blessing but two words, Jeremiah's fusion, the translation's king and Messiah, Daniel's Kittim, Shittim's timber, Exodus 34's run with the feminine \"their gods\", the curse-word's alcove, Aaron's clause at Phinehas's, the sotah's zeal-word, Zur of the five kings, Haman's title). NEXT: THE COMPILE OF BALAK (7b), then chapter 26 — never the next reading first.\n")

# 10. Memory files
p = f'{MEM}/numbers-in-order-ruling.md'
replace_once(p, '; NEXT chapter 22 (Balak)"', '; SITTING 7 DONE 2026-09-11 (Balak 22:1-25:19 read and frozen: 120 sources, 40 claims, 200 units, standing 2063, hash unmoved; the Sifrei\'s one piska 131 on 25:1, none on 22-24; the plene three a new parser gap and the calf\'s 3,000 found read 3; the export joins 25:19 into 26:1); NEXT the compile of Balak (7b), then chapter 26"')
replace_once(p, 'THEN its compile\n— never the next reading first.\nRelated:', 'THEN its compile\n— never the next reading first.\nSITTING 7 DONE 2026-09-11 — BALAK 22:1-25:19 READ AND FROZEN (NUMBERS_WALK.md "Sitting 7"; the owner: "Continue" after the #130 rereads; THE\nDRAFT\'S GRAIN AT BOTH ENDS — 22:1 Chukat\'s last verse and 25:10-19 Pinchas\'s opening read with their drafts, the next draft opening at 26:1): the\nSifrei\'s ONE piska 131 on 25:1-13 (five rows; NO piska on 22, 23, 24 — computed on every head; two citations inside row 2 mistyped, read to their\nverses) + Onkelos whole (115; THE EXPORT JOINS 25:19 INTO ITS 26:1 — the half-verse with the etnachta and no verse-end mark, a fourth defect class)\n= 120 sources in four ledgers (seven modules; 102 asserts, thirty failures on the first typed pass — TWELVE THE MARKS\' ORDER, met by NFC on both\nsides, one the final nun inside "the Midianite"; five cut misses the shelf\'s own Aramaic spellings, none on the second run; gloss_lint 0 on all\nfour first run); 40 claims verified and labeled (ink, E10, E2, E28, M-22), 40 operators seated, four rituals → 200 units, standing 2063, hash\nunmoved, the fold matching its prediction; THE PARSER RIGHT at ten, silent-and-right at three homographs, ONE GAP — THE PLENE "THREE" (22:32; Deut\n16:16, 19:2; forty-one seats), AND A CROSS-CHECK FOUND THE CALF\'S "ABOUT THREE THOUSAND" READ 3 (Exod 32:28 — the approximation prefix on a\nconstruct plural); the crowns in the file; the Sifrei\'s adjacency rule disputed on the verse (R. Akiva against Rebbi — MIDDOT.md), M-22\'s\nNumbers exemplar (Exod 34:15-16 → 25:1-2). UNCOMMITTED since 0a98276. NEXT: THE COMPILE OF BALAK (7b) on 1b\'s order (COMPILE_DEBT\'s sitting-7\nbox: the two parser probes, the stands, the formula\'s restrictors, the Peor engine with the rule installed by a deed, the plague closed by the\nspear, the Midian debit, the undated tape), THEN chapter 26 (the second census) — never the next reading first.\nRelated:')
p = f'{MEM}/MEMORY.md'
t = rd(p)
lines = t.split('\n')
i = [k for k, l in enumerate(lines) if l.startswith('- [⚠ NUMBERS IN ORDER FROM 1:1](numbers-in-order-ruling.md)')]
assert len(i) == 1, i
lines[i[0]] = ('- [⚠ NUMBERS IN ORDER FROM 1:1](numbers-in-order-ruling.md) — OWNER-RULED 2026-09-09: the chapter walk from 1:1 at the parashah grain (map World/step9/NUMBERS_WALK.md; the four case chapters 9, 15:32-41, 27, 36 frozen at THE TENT and SKIPPED); ⚠ OWNER-RULED 2026-09-10 "Finish compiling before moving on" — READ THEN COMPILE PER PORTION, never read ahead; the owner wants CHAPTER NUMBERS, not portion names. DONE, all read, frozen, compiled and on the tape: 1:1-4:20 (committed 0a98276), 4:21-7:89, 8 + 10-12, 13:1-15:31, 16:1-18:32 (sittings 5 + 5b: 193 units; korach 155/155 first run; CK4 OPEN), 19:1-21:35 (sittings 6 + 6b: 196 units, standing 2023; chukat 159/159 first graded run; four fortieth-year markers, RUN (1198, 52, 52, 0, 12, 1412, 24, 295, four pairs, 110) matched first tape run; 53 daemons; the sweep 48/48 at 5,613; CM5 open; a BLOCK can never close) — the details in the file. NUMBERS 1:1-21:35 ON THE TAPE. SITTING 7 DONE 2026-09-11 — 22:1-25:19 READ AND FROZEN (Balak, with the drafts\' own edges 22:1 and 25:10-19: 120 sources, 40 claims, 200 units, standing 2063, hash unmoved; the Sifrei\'s one piska 131 on 25:1, none on 22-24; the plene three a new parser gap, the calf\'s 3,000 found read 3; the export joins 25:19 into 26:1; twelve asserts fell on the marks\' order — NFC on both sides). ALL UNCOMMITTED since 0a98276. NEXT the compile of Balak (7b), then chapter 26 (the second census) — never the next reading first.')
t2 = '\n'.join(lines); wr(p, t2); print('MEMORY.md bytes', len(t2.encode('utf-8'))); assert len(t2.encode('utf-8')) < 17000
p = f'{MEM}/step9-exam-era.md'
insert_after(p, '## STANDING LESSONS AND WATCHES (moved verbatim from the MEMORY.md index line on 2026-09-07 to keep the index under its size limit; the W4/W3/W2/W1/D9/G/E lesson tail as it stood)\n', "⚠ THE NUMBERS WALK sitting 7 — BALAK'S READING (2026-09-11): THE MARKS' ORDER, A THIRD TIME — twelve of thirty asserts fell on typed pointed forms whose combining marks the DB orders otherwise; THE INSTRUMENT IS NFC ON BOTH SIDES (npt / ptn / NL in balak_ink.py), and the leg diagnostic (balak_legs.py) prints the two codepoint sequences and their NFC equality. THE FINAL LETTER INSIDE A GENTILIC — \"Midian\" (final nun) is not a substring of \"the Midianite\" (regular nun): a census names its forms. THE EXPORT'S VERSE DIVISION CAN DIFFER FROM THE MASORETIC — Onkelos's chapter 25 has eighteen verses, 25:19 joined into its 26:1; the row is cut from the neighbor's head and the class named (a naive (chapter, verse) index falls off the end); the DB's etnachta with no verse-end mark is the half-verse's signature. THE DRAFT'S GRAIN GOVERNS AT BOTH ENDS (22:1 and 25:10-19 read with their drafts). THE PARSER'S NEW GAP ON THE PORTION'S OWN NUMBER, A FOURTH TIME (the plene \"three\" at 22:32; Deut 16:16, 19:2) — AND A CROSS-CHECK ON A PLAGUE COUNT FOUND AN OLD ONE (Exod 32:28's \"about three thousand\" read 3 since the parser's first day: the approximation prefix on a construct plural). THE WRITER'S CUT MISSES WERE THE SHELF'S SPELLINGS — five Aramaic tokens the hand re-spelled (plene/defective, a doubled letter): type the Aramaic from the plain-token print. THE SHELF'S CITATIONS INSIDE A ROW MISTYPED AGAIN (two in one row). THE SHELF AGAINST ITSELF ON A NUMBER (eighty high priests / three hundred) AND AGAINST THE MORPHOLOGY ON A TENSE (25:13's vav-form) — recorded, not adjudicated. THE SHELF SILENT ON THREE MORE CHAPTERS (22-24) and the reading form holding on the translation alone, a fourth time. THE READING SITTING'S SHAPE HELD END TO END (dump → asserts 30 → 2 → 0 → rows → writer 5 misses → 0, lint 0 first run → manifests 40/40 → seats → rituals 4/4 → the fold predicted and matched).\n")

# 11. The state doc — COMPACTION POINT #131
append(f'{ROOT}/logic/pre_logic_methods_2026-07-28/PROMPT_continue_solo_era_2026-08-06.md', '''
═══ COMPACTION POINT #131 (2026-09-11 — written at THE NUMBERS WALK sitting 7's close; BALAK 22:1-25:19 READ AND FROZEN; NUMBERS 1:1-25:19 READ AND FROZEN, 1:1-21:35 ON THE TAPE) ═══
STATE: 200 frozen units (num_22_balak_bilam_call, num_23_oracles_1_2, num_24_oracles_3_4, num_25_peor_pinchas the four new — the draft's grain governing at
both ends: 22:1 Chukat's last verse and 25:10-19 Pinchas's opening read with their drafts, the next draft num_26_second_census opening at 26:1), standing 2063
(2023 + 40, predicted and matched), hash 8b8fff1fa28953af UNMOVED, CORPUS TRUTH GREEN (facts 1809, demands 341 / 191 open, events 557, names 81). THE ENGINE
UNTOUCHED this sitting (48 runners, 53 daemons, the sweep 48/48 at 5,613, the journal gate GREEN as at #130). THE READING: the Sifrei on Numbers piska 131 on
25:1-13 (five rows; NO piska on 22, 23, 24 — computed on every head; two citations inside row 2 mistyped, read to their verses) + Onkelos 22-25 whole (115; THE
EXPORT JOINS 25:19 INTO ITS 26:1 — the half-verse with the etnachta and no verse-end mark, a fourth defect class) = 120 sources in four ledgers
logic/oral_triage/num_22..25_*_2026-09-11.md (seven modules in the scratchpad: balak_dump.py, balak_ink.py — 102 asserts, balak_measure1.py, the three rows
files, balak_rows_sifrei.py, write_balak_ledgers.py; thirty assert failures on the first typed pass read leg by leg — twelve the marks' order met by NFC on
both sides, one the final nun inside "the Midianite"; five cut misses the shelf's own spellings, none on the second run; gloss_lint 0 on all four first run);
four manifests (BK22A/BK23A/BK24A/BK25A ×10) — verify_claims 40/0, claim_labels_census --strict GREEN (Numbers 285/285); seat_balak.py 40 operators, step E,
the anchor scenarios; verify_text GREEN ×4; freeze_ritual COMPLETE ×4 (197-200); the py_units written ×4; the stamp row (DELEGATED, FULL RULE). THE PARSER:
right at ten (22:22, 28, 33; 23:1, 4, 14, 29; 24:10; 25:8, 9), silent-and-right at three homographs (23:10 rova, 24:8 his arrows, 25:18 their sister), ONE
GAP — THE PLENE "THREE" at 22:32 (Deut 16:16, 19:2 the Torah's other two; forty-one seats), AND THE CROSS-CHECK FOUND Exod 32:28's "about three thousand"
READ 3. THE RECORDS: NUMBERS_WALK.md "Sitting 7" (the drafts, the shelf, the reading, the ink, the case law, the claims, OWED TO THE COMPILE 7b, LESSONS);
COMPILE_DEBT.md's 7b box; RESEARCH_LOG.md's ten findings; MIDDOT.md's five Balak entries (the adjacency rule disputed on the verse — R. Akiva against Rebbi
— the Numbers seat of the adjacency-validity parameter); MOVE_CATALOG.md's M-22 Numbers exemplar (Exod 34:15-16 → 25:1-2); THE_STEPS, THE_BRIEFING's
scoreboard entry and count line, World/RESUME.md, the three memory files (the sitting-7 lesson paragraph first in step9-exam-era.md; MEMORY.md under 17,000
bytes). LAST COMMIT 0a98276; UNCOMMITTED: #130's 163 paths + this sitting's (four units, four manifests, four py_units, four ledgers, the six records, the
stamp ledger, the memory files) — commit only on "commit push".
THE CROWNS (computed, in the ledgers): the Akedah's morning at 22:21-22; the satan-word's two Torah seats; "God came to" — Abimelech, Laban, Balaam, by
night; Pharaoh's verbs (refuses, made sport, I have sinned); the word-formula six times with akh / efes; the ass's "three feet" and Balak's "three times";
the three stands on 21:19-20's stations (Bamoth, Pisgah, Peor); "took up his parable" seven — the parable-tellers' word PAID; Samuel over Agag (1 Sam
15:29 ↔ 23:19); the teruah made the Shekhinah; 23:22 → 24:8 one letter; the serpent and the omen one pointed word (24:1 = 21:6); 24:9 = Gen 49:9 but two
words; Isaac's blessing reversed; the top of Peor = 21:20's clause; the spirit of God → prophecy; Ps 84:2 ↔ 24:5; "many waters" Meribah's; Jeremiah 48:45
fusing 21:28 + 24:17; Onkelos's KING and MESSIAH, ROMANS and EUPHRATES; Daniel 11:30's Kittim; Shittim the tabernacle's timber; Exod 34:15-16 RUN at 25:1-2
with the feminine "their gods" at both alone (M-22); "yoked" — 19:15's lid PAID; hang them to the LORD (2 Sam 21:6); Onkelos's court; "brought near" the
offering-verb; Phinehas born Exod 6:25; "from the midst" Korach's; the one spear; the alcove = "curse for me"; "both of them" Deut 22:24; "and the plague
was stayed" + "and he atoned for" = Aaron's 17:12-13; 24,000 / 14,700; Simeon 59,300 → 22,200; the zeal-root the sotah's; the covenant of peace; everlasting
priesthood = Exod 40:15; the vav-form's tense (the Sifrei future, the tag past); Zur of the five kings; "head of the peoples" Ishmael's; "harass" = Haman's
title; "wiles" Joseph's brothers'; 25:19's half-verse.
NEXT on the owner's word: THE COMPILE OF BALAK (7b) on 1b's order — the docket by the union rule (the list in COMPILE_DEBT's box), the two parser probes to
FAIL (the plene three; the approximation prefix on a construct plural), the cells (the stands on the stations by CALL to chukat's well cell; the
word-formula's restrictor class; the blessing formula by CALL to the Genesis engines; the Peor engine — the sin as Exod 34:15-16's RUN by CALL to the
family engine, the hanging by the judges by CALL to the courts engine, THE ZEALOUS-SMITE RULE INSTALLED BY A DEED (rule_installed by an act — THE TENT's
form at a second seat), Phinehas's priesthood by the deed, the covenant of peace a HEAVEN entry, THE PLAGUE a heaven entry CLOSED at 25:8, the Midian
command a DEBIT closed at Matot), law_balak the 54th daemon, the tape's undated stretch (no marker; the entities; the three angers), THEN chapter 26 (the
second census — its 25:19 marker) — never the next reading first. Commit only on "commit push".
POST-COMPACTION REREADS (mandatory, first sitting): numbers-in-order-ruling.md + this entry + NUMBERS_WALK.md "Sitting 7" (OWED TO THE COMPILE + LESSONS)
+ NUMBERS_WALK.md "Sitting 6b — AS BUILT" (the compile's form) + THE_STEPS Step 2 + Step 5 + the compiler block; memory's STANDING LESSONS head (the
sitting-7 paragraph first, the 6b paragraph second). WATCHES: as #130's + NFC ON BOTH SIDES FOR EVERY POINTED COMPARISON + THE FINAL LETTER INSIDE A
GENTILIC + THE EXPORT'S VERSE GRID CHECKED AGAINST THE DB'S BEFORE A DUMP (ONK_LEN per chapter) + THE ARAMAIC TYPED FROM THE PLAIN-TOKEN PRINT + THE
PLAGUE-COUNT CROSS-CHECK'S CALF GAP (a probe to FAIL at 7b).
''')
print('records done')
