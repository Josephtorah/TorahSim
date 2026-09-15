import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE NUMBERS WALK sitting 14 — THE BORDERS (2026-09-12): the records — the stamp row, NUMBERS_WALK.md "Sitting 14", the state doc's #155,
# World/RESUME.md, THE_STEPS' paragraph, THE_BRIEFING's bullet, COMPILE_DEBT's box, RESEARCH_LOG's entry, the three memory files, the recovery file's
# section 14, and the forms copied into World/step9/forms_numbers_walk/. The counts below are the tools' own prints (the ritual's PASS lines, the
# bake's hash, the truth's units), typed from them; the corpus tripwire and the ritual's print are read back before a byte is written. Every insert
# lands on a unique anchor asserted present once. The gloss override rows were written by patch_overrides_bor.py at the ink step (asserted present by
# bor_ink.py) — verified here, not rewritten. MIDDOT.md, MOVE_CATALOG.md and MISHNAH_TOPICS.md UNCHANGED (no Sifrei row on the chapter — no case law
# read; no move; no Mishnah opened at a reading sitting). Sitting 13's form (write_jou_records.py).
import os, re, yaml, shutil, glob
ROOT = _ROOT
SP = os.path.dirname(os.path.abspath(__file__))
MEM = '<memory>'
truth = open(f'{ROOT}/logic/corpus/CORPUS_TRUTH.py', encoding='utf-8').read()
assert 'assert len(W["units"]) == 209' in truth and 'assert len(W["standing"]) == 2149' in truth and "== '8b8fff1fa28953af'" in truth, 'the fold is not the predicted one'
rit = open(f'{SP}/bor_ritual_num_34_borders.out', encoding='utf-8').read()
assert 'RITUAL COMPLETE for num_34_borders (209 frozen units)' in rit and rit.count('PASS ') >= 13, 'the ritual is not complete'
assert os.path.exists(f'{ROOT}/logic/oral_triage/num_34_borders_2026-09-12.md') and os.path.exists(f'{ROOT}/logic/oral_audit/manifests/num_34_borders_claims.json') and 'status: frozen' in open(f'{ROOT}/logic/units/num_34_borders.yaml', encoding='utf-8').read()
d_ov = yaml.safe_load(open(f'{ROOT}/logic/glosses/word_gloss_overrides.yaml', encoding='utf-8'))
assert len([k for k in d_ov['by_ref'] if k.startswith('Num.34.')]) == 31 and d_ov['by_gloss']['cord'] == 'border' and d_ov['by_gloss']['inherit--mode-of-descent)'] == 'inherit', 'the override rows are not the ink\'s'
def append(path, text):
    assert os.path.exists(path), path
    with open(path, 'a', encoding='utf-8') as f: f.write(text)
    print('appended %d bytes -> %s' % (len(text.encode()), path))
def insert_before(path, anchor, text):
    s = open(path, encoding='utf-8').read(); assert s.count(anchor) == 1, (path, anchor[:40], s.count(anchor))
    open(path, 'w', encoding='utf-8').write(s.replace(anchor, text + anchor)); print('inserted %d bytes before %r -> %s' % (len(text.encode()), anchor[:30], path))
def insert_after(path, anchor, text):
    s = open(path, encoding='utf-8').read(); assert s.count(anchor) == 1, (path, anchor[:40], s.count(anchor))
    open(path, 'w', encoding='utf-8').write(s.replace(anchor, anchor + text)); print('inserted %d bytes after %r -> %s' % (len(text.encode()), anchor[:30], path))

STAMP = ('| 2026-09-12 | num_34_borders | DELEGATED | FULL RULE | Numbers 34:1-29 derivation 2026-09-12 (THE NUMBERS WALK sitting 14 — THE BORDERS; the owner: "Go" after the #154 rereads, on the ruling READ THEN COMPILE; the FORTY-SIXTH NUMBERS UNIT — the portion Masei\'s second chapter as one draft, the next draft opening at 35:1): declared reading COMPLETE — Onkelos Numbers 34:1-29 whole, 29 verses fresh; the Sifrei on Numbers found BY POSITION to have NO piska on the chapter (158 on 31:22 followed by 159 on 35:9 — the shelf silent from 31:25 to 35:8, 165 verses computed at sitting 11), the whole export scanned in both files for a row citing chapter 34 in FOUR forms (the English "Bamidbar" and "Ibid.", the Hebrew chapter mark with the gershayim and the Hebrew "ibid.", the word "there" before the mark — a fourth form the scan now takes): ONE row of another chapter cites 34:2 (1:2 on 5:2 — Rabbi Shimon ben Yochai\'s "command" everywhere entails expense EXCEPT this one, "impel them to the division of the land"; the census meets the row: the five seats of "command the children of Israel" in the Torah are the row\'s five), read whole at sitting 2 and CREDITED with a quick look; the English "Ibid. 34" false hits Exodus 34:30 and Deuteronomy 34:1-3, each read to its verse. Ledger logic/oral_triage/num_34_borders_2026-09-12.md (29 sources; coverage computed — missing 0, extra 0; the ink facts computed from the Tanakh DB and the snapshot store, every fact an assert — eighteen fell on the first typed pass and one on the second, each retyped from the leg print; every quotation cut by consonants in glossed pieces, no cut miss; the lint clean on the first write). 13 claims MS34A-01..13 verified 13/13 by verify_claims, labeled, seated as WITNESS_READ operators at their first verses; verify_text GREEN (29 steps, 7 scenarios); freeze ritual 13 PASS, RITUAL COMPLETE (the 209th frozen unit); the corpus rebaked to the prediction — units 209, standing 2149 (2136 + 13), hash 8b8fff1fa28953af UNMOVED; CORPUS TRUTH GREEN. The finds: the border\'s own verb "you shall mark out" three Bible seats all here; the goings-out word the Torah\'s five all here; Judah\'s south border is the land\'s (twenty of thirty-three tokens with Joshua 15:1-4); the spies walked the border\'s length (two words at two seats each, 13:21 and here); the sea as the west, split by Onkelos; the blotting verb on the border; Caleb\'s five words from 13:6; one tribe-noun; the intensive stem that runs three times in Joshua; a roster order matching no other. Stamp delegated under the AUTO-SEAT ruling; the owner may overrule. |\n')

WALK = '''
## Sitting 14 — THE BORDERS, Numbers 34:1-29 (2026-09-12; the owner: "Go" after the #154 rereads, on the ruling READ THEN COMPILE): the reading and the unit

THE DRAFT: one — num_34_borders 34:1-29 (29 of 29 verses, computed): the portion Masei's second chapter whole; the next draft, num_35_refuge_cities, opens
at 35:1 (asserted). Read in ONE pass, one ledger. The forms copied from sitting 13's scripts in World/step9/forms_numbers_walk/ and edited (bor_dump.py,
bor_measure1.py, bor_measure2.py, bor_ink.py, bor_legs.py, bor_rows_onkelos_a.py / _b.py, write_bor_ledger.py, write_bor_manifest.py, seat_bor.py,
bor_chain.sh, patch_overrides_bor.py, write_bor_records.py; every one copied into the forms folder at the close).

THE SHELF, BY POSITION (bor_ink.py's asserts): the Sifrei on Numbers has NO piska on the chapter — 158 (31:22) is followed by 159 (35:9): the shelf is
SILENT from 31:25 to 35:8 (165 verses, computed at sitting 11), and this chapter is the fourth and last stretch of that silence read on the translation
alone (the shelf RETURNS at 35:9). THE "FOUND BY POSITION" CLAUSE run on the whole export in FOUR FORMS — the English's "(Bamidbar 34:n)" and "(Ibid.
34:n)", the Hebrew's chapter mark with the gershayim (the double-stroke mark), and A FOURTH FORM sitting 13's scan had not looked for: the Hebrew's own
ibid., the word "there" before the chapter mark. ONE row of another chapter cites Numbers 34 — 1:2 (on 5:2, the sending out of the unclean): Rabbi Shimon
ben Yochai's reading of "command" — everywhere it entails expense (Leviticus 24:2 the oil, 35:2 the Levites' cities, 28:2 the offerings) EXCEPT ONE, 34:2
"command the children of Israel and say to them: when you come to the land of Canaan" — "impel them to the division of the land"; the Hebrew row cites it
as "ibid. 34"; THE CENSUS MEETS THE ROW: "command the children of Israel" stands five times in the Torah (Leviticus 24:2; Numbers 5:2, 28:2, 34:2, 35:2),
exactly the row's five. The English "Ibid. 34" hits are EXODUS 34:30 (1:8 — Aaron and Israel afraid of Moses' shining face; the Hebrew row 1:7 carries it
as "ibid. 34" after Exodus 24:17) and DEUTERONOMY 34:1-3 (135:1 on Deuteronomy 3:26 — the LORD showing Moses "all that is called the land of Israel"); the
Hebrew's third "ibid. 34" (118:1, unparenthesized) is Exodus 34:20's firstborn donkey — each read to its verse; the abbreviation's book is the row's
last-named one. The credited row was READ WHOLE at sitting 2 (the Naso ledger num_05_camp_pure_theft — "four readings of 'command'", the exception 34:2
named there) and is CREDITED with a QUICK LOOK. Onkelos 34 whole: 29. No prior ledger had read a row of the chapter; two ledgers NAME a verse of it (the
sotah ledger 34:11 — the border's "reach" verb beside the sotah's "blot"; the vows' exam 34:18): names, not reads — FRESH.

THE READING (ten modules — bor_dump.py the first measurement pass; bor_measure1.py and bor_measure2.py the second and third, printing every candidate
fact (the third for what the second lacked: the Hebrew "ibid." hits read to their books, the pointed forms of the chapter's consonantal homographs, the
full seat lists, the store's gloss families censused); bor_ink.py the ink with every fact an assert (assert_driver.py: EIGHTEEN failures on the first typed
pass, ONE on the second, NONE on the third — bor_legs.py printing every failing leg, each retyped from the print: SIX slice indices (Onkelos 34:4's
"Rekem Geah", Exodus 23:31, Joshua 21:1, 21:6, Numbers 17:21, Onkelos 17:21 — the sixth instance of the lesson), a Joshua-filtered list typed as the
whole-Bible census (the shoulder's twenty-eight seats), a token list's count typed for a verse set's (Samuel's 125 tokens are 120 verses), two hand
tallies against the machine's columns (Joshua's fourteen goings-out typed fifteen; Genesis 46's Manasseh-first missed in the rosters' comparison), the
by-gloss census reaching "according" through the letters of "cord" (the six rewritten glosses' tokens asserted, never a substring family), a prefix
tuple missing the article's forms, and EIGHT POINTED COMPARISONS that fell on THE MARKS' ORDER — the DB's raw order of the vowel points differs from the
canonical at the dagesh and the meteg (sitting 7's lesson on the ledger's cuts, now on the ink's asserts: every pointed comparison made on NFC-normalized
strings on both sides, the meteg kept where the print shows it) — then 0) and the piece-wise cutters HP / AP; bor_rows_onkelos_a.py and _b.py the 29
rows (a prince() helper for the roster's ten, each still carrying its computed note); write_bor_ledger.py the writer → ONE ledger
logic/oral_triage/num_34_borders_2026-09-12.md (29 sources: Onkelos MATERIAL 29 / CONTEXT 0 — every verse a datum, the two frames the speech-spans';
one Sifrei row credited; coverage computed, missing 0, extra 0; NO cut miss on the writer's first run; gloss_lint 0 on the first write); the display
layer's rows written at the ink step by patch_overrides_bor.py (thirty-one by reference, twenty-eight by gloss — the by-gloss families censused first).

THE INK, COMPUTED (the measurement passes FIRST, the asserts typed from the print):
- THE PARSER MEASURED FIRST (the standing rule): THREE number verses in twenty-nine, every one read — 34:13 "to the nine tribes and the half tribe" [9]
  (the construct numeral); 34:15 "the two tribes and the half tribe" [2] (the construct "two of" by its points, the caret); 34:18 "one prince, one
  prince from a tribe" [1, 1] — THE DISTRIBUTIVE DOUBLING read as two ones (the same at 13:2's spies and 7:11's dedication, [1, 1, 12] at 17:21's rods;
  Joshua 3:12's stones [12, 1, 1], 22:14's embassy [10, 1, 1]); "half" no numeral before a tribe (34:14 silent, 32:33 silent; Joshua 14:3-4 [2] each);
  no starred homograph; 35:1 empty. NO GAP — the walk's third reading with none. No line of the tape names the chapter.
- THE FRAMES AND THE REGISTER: TWO divine frames — 34:1 (the borders, 34:2-12) and 34:16 (the dividers, 34:17-29), the same five words at both — with
  MOSES' OWN COMMAND between them (34:13-15; the form's two Torah seats 34:13 and 36:5, both in the plains of Moab); THREE narrative verbs; the chapters
  without a frame unchanged (22-24, 29, 30, 32, 36), twelve with exactly two. The border runs on TWENTY "and-it-shall" verbs (34:2-12: "be" 4 + "they
  shall be" 4, "go down" 3, "turn" 2, "pass" 2, "go out" 2, "say", "mark out for yourselves", "reach") and four second-person imperfects; "to you"
  twelve times, and JOSHUA 15:4 KEEPS ONE "TO YOU" inside Judah's border — the spec's pronoun in the run.
- 34:2 THE HEADING: "command the children of Israel" FIVE Torah seats = the Sifrei's five; "when YOU ARE COMING" the participle one seat; "THE LAND
  CANAAN" (the article on the land, none on Canaan) one seat; "THIS IS THE LAND" three Torah seats (34:2, 34:13, Deuteronomy 34:4 from Nebo); THE LOT'S
  VERB "shall fall" with the inheritance at this one Torah seat (Joshua 13:6; Judges 18:1; Ezekiel 47:14 carries the clause; Psalm 16:6) — ONKELOS "shall
  be DIVIDED", one Aramaic verb for 34:2's "fall" and 26:53, 55, 56's "divide"; "BY ITS BORDERS" four Bible seats — the chapter's inclusio (34:2, 12) and
  Joshua's two closers (18:20, 19:49); the border-word SIXTEEN times here, half of Numbers' thirty-two, sixty in the Torah; "as an inheritance" three
  Torah seats, all the land's.
- 34:3-5 THE SOUTH SIDE AND JOSHUA 15:1-4: twenty of the three verses' thirty-three tokens stand in Judah's south border; JOSHUA SPLITS HAZAR-ADDAR (one
  seat) into "Hezron" and "Addar"; Azmon defective here, plene in Joshua. THE SIDE-WORD IS THE TABERNACLE'S (eighteen Torah seats, twelve the court's
  and the boards' sides — Exodus 27:9 "the south side" of the court; Ezekiel gives every side that word, Numbers the south alone). THE SPIES WALKED THE
  BORDER'S LENGTH: "from the wilderness of Zin" with that prefix and the defective "Lebo-hamath" each at exactly two seats — 13:21 and this chapter
  (34:3, 34:8). "On the hands of Edom" one seat, Onkelos "on the borders of"; the Salt Sea nine seats (Genesis 14:3 "that is the Salt Sea" the identity
  idiom); "eastward, toward the sunrise" (34:15) the court's and the camp's phrase; "and it shall turn" the chapter's two and Joshua's five; Kadesh-barnea
  ten seats — ONKELOS "Rekem Geah" at both Numbers seats, apart from Kadesh's "Rekem"; "ITS GOINGS-OUT" — the border's outlet-word: THE TORAH'S FIVE
  SEATS ALL IN THIS CHAPTER, fourteen in Joshua's borders; THE ONE WRITTEN SINGULAR READ PLURAL — 34:4's "and it shall be" the chapter's one
  written-and-read pair (the store's two tokens, the DB's written one), the clause's four other seats written plural, Joshua 15:4 the same clause with
  the written singular; "THE BROOK OF EGYPT" — the bare brook five seats (1 Kings 8:65 "from Lebo-hamath to the brook of Egypt", the border's two ends
  as the kingdom's measure), the covenant's "RIVER of Egypt" another word, and no river, Euphrates, Lebanon or "western sea" of the four promised
  extents stands in the chapter; THE BROOK'S CONSONANTS ARE THE INHERITANCE'S (34:5 against 34:2 — the morphology, the points, Onkelos's two words).
- 34:6-7 THE WEST: the sea-token SEVEN times — the west twice, the great sea twice, the Salt Sea twice, Chinnereth once; ONKELOS SPLITS IT ("the west"
  against "the sea"); "and the west border" two seats (34:6, Joshua 15:12 with the same tail); THE GREAT SEA PLENE at 34:6 AND DEFECTIVE at 34:7 (the
  defective phrase's one seat; the covenant's "great river" defective too); Onkelos adds the possessive to 34:6's second "border".
- 34:7-10 THE NORTH: "YOU SHALL MARK OUT" — THE VERB'S THREE BIBLE SEATS ALL HERE (34:7, 8 Piel; 34:10 Hitpael); its consonants Proverbs' "do not
  DESIRE" (23:3, 6; 24:1), told apart by the points and the morphology; Joshua marks with another verb; ONKELOS "direct yourselves". "The north border"
  two seats, both here. MOUNT HOR twelve Torah seats — ten Aaron's, TWO the north border's (34:7, 8): THE SECOND MOUNT HOR (the chukat runner's data
  row); ONKELOS SPELLS HOR TWO WAYS IN ADJACENT VERSES (without the vav 34:7 and chapters 20-21, with it 34:8 and chapter 33). Zedad two seats (Ezekiel
  47:15), Ziphron one, Hazar-enan four in two spellings; Shepham two, its consonants the leper's "upper lip" (Leviticus 13:45) — the shin's dot against
  the sin's.
- 34:11-12 THE EAST AND THE LOOP: "the Riblah" with the article one seat (the exile's Riblah ten without it); Ain a name at two Torah seats; "AND IT
  SHALL REACH" IS THE BLOTTING VERB — the token's four Bible seats: the sotah's scroll blotted into the water (5:23), a name blotted out (Deuteronomy
  29:19), tears wiped away (Isaiah 25:8), and this border — one pointing at all four; ONKELOS "reach" here, "blot" at 5:23. "THE SHOULDER" — fifteen
  Torah tokens: the court's gate-sides (four), the ephod's shoulder-pieces (nine), the Kohathites' carrying (7:9), and this shore; Joshua's borders say
  it eight times. The sea of Chinnereth two seats, the name seven; ONKELOS "the sea of Gennesar", its one seat. "To the Jordan" with the article and the
  ending the Torah's one seat. THE LOOP: the south opened "from the end of the Salt Sea eastward" (34:3) and the east closes "its goings-out shall be
  the Salt Sea" (34:12); "by its borders round about" the inclusio with 34:2; ONKELOS "round, round" (fifteen seats). EZEKIEL'S BORDERS (47:13-20; 48:1,
  28) share twenty-three tokens, open with 34:13's "you shall inherit" and 34:2's "shall fall to you as an inheritance", and run the sides NORTH, east,
  south, west where Numbers runs south, west, north, east — OBSERVED.
- 34:13-15 MOSES' RESTATEMENT: ONE TRIBE-NOUN — the staff-word "tribe" EIGHTEEN times in the chapter, the other tribe-word NEVER (32:33 gave "the half
  tribe of Manasseh" with the other word; the book's six seats of it; the staff-word 103 times in Numbers); JOSHUA 14:2 QUOTES 34:13's six words "to the
  nine tribes and the half tribe" whole under "as the LORD commanded by the hand of Moses" — the run citing the spec outside the Torah — and 13:7 says
  them with the other word; "NINE" in the construct three Bible seats, every one the nine tribes; "you shall inherit" the reflexive stem's Torah seats
  (Leviticus 25:46; 32:18; 33:54 twice; 34:13), Ezekiel 47:13 the same; "by lot" four Torah seats, fifteen in the Bible; "THE REUBENITE ... THE GADITE"
  — THE PAIR'S FIRST SEAT, thirteen in the Bible; "the half tribe of Manasseh" with the staff-word here and in the Levite cities' rows (Joshua 21:5, 6,
  27; 1 Chronicles 6:56); "THEY TOOK THEIR INHERITANCE" four Bible seats — 34:14, 34:15, Joshua 13:8, 18:7 — always the two and a half; "beyond the
  Jordan at Jericho" two seats (22:1, 34:15). ONKELOS: one Aramaic tribe-word for both Hebrew words (eighteen here; 32:33's "half tribe" rendered as
  34:14's), "tribes" in the plural at 34:13 and 34:15 alone.
- 34:16-18 THE COMMISSION: "THESE ARE THE NAMES OF THE MEN" four Bible seats, all Numbers' rosters (1:5, 13:16, 34:17, 34:19); THE ONE ROOT IN THREE
  STEMS — "inherit" eight times in the chapter: the reflexive (34:13), the plain (34:17, 18), the INTENSIVE (34:29), the nouns (34:2, 14, 15 — and
  34:5's brook); THE INTENSIVE STEM'S FOUR BIBLE SEATS — 34:29 and three RUNS in Joshua (13:32 Moses'; 14:1 and 19:51 "which Eleazar the priest and
  Joshua son of Nun ... divided"); the plain stem's "to divide the land" runs at Joshua 19:49 ("they finished dividing the land by its borders"); THE
  OBJECT SWITCHES WITH THE STEM — the land at 34:17-18, the people at 34:29. "ELEAZAR THE PRIEST AND JOSHUA SON OF NUN" as one phrase three seats —
  34:17 and Joshua's two runs (14:1, 19:51). "ONE PRINCE, ONE PRINCE from a tribe" — THE DISTRIBUTIVE DOUBLING of the spies (13:2), the rods (17:21), the
  dedication (7:11), Joshua's stones (3:12, 4:2, 4:4) and Phinehas's embassy (22:14). ONKELOS: "one chief, one chief" as at 7:11 and 17:21 — and one
  Aramaic word, "great", for the great sea (34:6, 7) and the prince (34:18, 22-28); one form for the plain and the intensive stems; the possession-root
  at all seven inheritance tokens.
- 34:19-28 THE ROSTER: "FOR THE TRIBE OF JUDAH, CALEB SON OF JEPHUNNEH" — 34:19's five words are 13:6's five, the spy's line repeated at the dividers';
  Caleb son of Jephunneh eight Torah seats, Caleb thirty-six in the Bible; THE TWO SURVIVORS OF THE SPIES are the only persons of chapter 13's roster in
  this chapter's — Joshua son of Nun (34:17; 13:8 "Hoshea son of Nun") and Caleb; NO PRINCE OF CHAPTER 1 among the ten, one father's name shared —
  AMMIHUD (Ephraim's Elishama at 1:10; Simeon's Shemuel; Naphtali's Pedahel): three tribes, nine Bible seats. EIGHT NAMES STAND NOWHERE ELSE (Elidad,
  Jogli, Ephod, Shiphtan, Parnach, Azzan, Ahihud, Pedahel); SHEMUEL the first seat of the prophet Samuel's name (one hundred twenty verses, the
  prophet's but for this prince and an Issacharite); Kemuel Nahor's son's name, Elizaphan the Kohathite prince's, Bukki a priest's, Paltiel Michal's
  husband's, Hanniel an Asherite's, Shelomi a Nethinim family's, CHISLON a place on Judah's north border ("Mount Jearim, that is Chesalon", Joshua 15:10);
  SEVEN of the ten carry God's name, none of the fathers; "son" eleven times. THE TITLE DROPPED FOR THREE ("prince" at seven rows, not at Judah's,
  Simeon's, Benjamin's; "the children of" absent at Judah's and Benjamin's; the conjunction absent at Benjamin's and at Joseph's heading, 1:10's form).
  THE ORDER — Judah, Simeon, Benjamin, Dan, Manasseh, Ephraim, Zebulun, Issachar, Asher, Naphtali — MATCHES NO OTHER ROSTER OF THE TORAH (computed on
  twelve): Manasseh before Ephraim as in the second census and Genesis 46:20 alone, Zebulun before Issachar as in Jacob's and Moses' blessings alone,
  and the four northern tribes in the order Joshua's lots fall (19:10, 17, 24, 32) — the cause unnamed, the declared shelf silent.
- 34:29 THE CLOSER: "these are they whom the LORD commanded" — the closer's form without a noun, one seat; NO receipt "as the LORD commanded" in the
  chapter — the run's receipt is Joshua 14:2's "by the hand of Moses", outside the Torah, quoting 34:13. Deuteronomy 34:1-3 (the Sifrei 135:1's
  citation) shows Moses the land BY TRIBES — the other description, OBSERVED.
- THE STORE'S GLOSSES READ BACK: "mouth-in-a-figurative-sense" (the side), "cord" (the border — six gloss forms, every token the border-word),
  "the-powder" (the salt), "from-pasture", "and-revolve", "?" and "to-?" at Hazar-, Kadesh- and the ascent, "and-bring-forth" (the border going out),
  "exit-him/its" (the goings-out), "stream-suffix" (the brook), "hidden" (the north), "come/bring" (Lebo-), "and-stroke" (the reaching), "circle",
  "the-seas" and "seas" (the sea and the west), "in-pebble" (the lot), "Daniel" (Dan), "Non" (Nun), "front-suffix" and "sunrise-suffix" (the east),
  "from-region-across" (beyond), and the broken "inherit--mode-of-descent)" family with its stray parenthesis — THIRTY-ONE rows by reference and
  TWENTY-EIGHT by gloss (each gloss family censused: every token the one word) added to the display layer's override file; the frozen unit untouched.

THE SIFREI'S OWN CASE LAW: none — no row of the spine on the chapter (MIDDOT.md unchanged; MOVE_CATALOG unchanged). The one credited row carries one
clause on 34:2 (its dispute on "command" is Naso's, read there).

THE CLAIMS (write_bor_manifest.py → one manifest, 13 claims MS34A-01..13, every check the word's LONGEST STORE-PIECE WHOLE — the floor of four code
points refused four words whose longest piece is three letters (the reaching, the tribe, the inheritance's root, "two of"), another word of the verse
chosen each time; the ID prefix asserted absent; every cite checked against the ledger's CITE INDEX; every verse of the chapter cited by the nine span
claims, asserted; four whole-chapter claims — the parser and the frames, the promised extents, Onkelos, the display layer): verify_claims 13 VERIFIED /
0 FAILED (from the repo root on the manifest's path); claim_labels_census --strict GREEN (Numbers 371 labeled 371, debt 0; every label ink). THE SEATS
(seat_bor.py num_34_borders): 13 WITNESS_READ operators at the claims' first verses (steps 1, 2, 3, 5, 6, 7, 11, 13, 16, 19, 29 — eleven steps, two
carrying two), step E, the scenarios in the anchor form; verify_text GREEN (29 steps, 7 scenarios). THE RITUAL (bor_chain.sh): every gate PASS (13 PASS)
— RITUAL COMPLETE for the 209th frozen unit; the Python rendering layer written and self-proved. THE CORPUS REBAKED (predicted before the fold: units
209, standing 2136 + 13 = 2149, hash unmoved — the tripwire's literals set to the prediction before the bake): units 209, standing 2149, hash
8b8fff1fa28953af — the prediction matched; CORPUS TRUTH GREEN. THE STAMP: one delegated FULL RULE row (logic/findings/STAMP_LEDGER.md). No engine file
changed at this sitting — the sweep, the journal gate and the register gate stand as at 13b's close.

OWED TO THE COMPILE (sitting 14b; the box in COMPILE_DEBT.md, items (a)-(k)): THE FOUR SIDES AS A DATA ROW — the border's named points in order (the
south's, the west's, the north's, the east's) with their kin seats in Joshua 15 and Ezekiel 47 and the two Mount Hors (the chukat runner's row); no act
on the tape for a border spoken, unless the design places the spec as one line; THE LOT by CALL into the second census's cell (VIA second_census, as at
32:18 and 33:54); THE NINE AND A HALF against the Gad runner's grant (32:33's transfers on the ledger — "they took their inheritance" a run citation of
the tape's own lines; Joshua 14:2's receipt outside the Torah, THE READBACK's); THE COMMISSION 34:16-29 — the dividers named (Eleazar, Joshua, the ten
princes) as a DATA row or a tape line whose value is the list (the journeys' shape), no entity for a named-but-not-written-on party; THE REGISTER GATE'S
NUM 34 HEADERS SEAT ("these are the names" at 34:17, 34:19 — declared NONE now, paid or held with the why refreshed at the compile's gates step; no count
line, no receipt in the chapter); the distributive doubling as the parser's reading (no rule owed); the edges the census will demand — second_census
(26:52-56), gad_reuben (32:33), shelach (13:6, 13:21, 14:30, 38), chukat (20:22 the other Hor), bamidbar (1:5-15, 1:10), naso (7:11), korach (17:21),
zelophehad (27:19-22), journeys (33:51, 33:54), the erection's court sides (Exodus 27:9, 13 — reference), the sotah's blotting verb (5:23 — FALSE, a
homograph by sense), Genesis 14:3, 15:18 OBSERVED; Joshua 13-19, 21, Ezekiel 47-48, 1 Kings 8:65 forward; THE DOCKET by the union rule — Gittin 8a (34:6's
"and its border"), Kiddushin 36b-37a, Mishnah Sheviit 6:1 and 9:2, Bava Batra 117a-122a (credited), Sanhedrin 16a, the link rows for 34:2, 34:6, 34:13,
34:18, the Tosefta of the boundaries if local; Ezekiel's order and the four promised extents as DATA rows with no verdict; the display layer done at the
reading (fifty-nine rows), the store's "seas" family beyond the chapter a display sitting's.

⚠ LESSONS (9): THE HEBREW IBID IS "THERE" — the export's Hebrew rows cite a verse of the last-named book as "there" plus the chapter mark, a FOURTH form
the scan now takes beside "(Bamidbar n:m)", "(Ibid. n:m)" and the gershayim mark (the row that cites 34:2 was found by the English form; the Hebrew form
would have found it alone). THE MARKS' ORDER MET BY NFC ON BOTH SIDES — eight pointed comparisons fell because the DB's raw order of the points differs
from the canonical at the dagesh and the meteg (sitting 7's lesson on the ledger's cuts, now on the ink's asserts): normalize both sides, keep the meteg
the print shows. THE SLICE INDEX FROM THE PRINT, A SIXTH INSTANCE — six slices typed one off; print the verse, then slice. THE SCOPE OF A PRINT IS PART OF
THE NUMBER, AGAIN — a Joshua-filtered list typed as the whole-Bible census. A SET COUNTS VERSES, A LIST COUNTS TOKENS — Samuel's 125 tokens are 120
verses. THE HAND'S TALLY AGAINST THE MACHINE'S COLUMN — fourteen typed fifteen; a roster fact read off half the print (Genesis 46 also puts Manasseh
first). A BY-GLOSS ROW IS CENSUSED FIRST, AND ON THE EXACT GLOSSES — "according" carries the letters of "cord": assert the rewritten glosses' tokens,
never a substring family; the article's forms belong in the stem tuple. THE FLOOR OF FOUR CODE POINTS — a check word whose longest store-piece is three
letters cannot be a manifest check; choose another word of the verse. THE READING SITTING'S SHAPE HELD: dump → measure (three passes) → asserts (18 → 1
→ 0) → rows → writer (0 misses; lint 0 first write) → manifest (13/13) → seat → ritual (13 PASS) → the fold predicted and matched.

NEXT on the ruling: THE COMPILE OF THE BORDERS (14b) on 1b's order — the measurements (the tape's state; the callees live: second_census, gad_reuben,
shelach, chukat, bamidbar, naso, korach, zelophehad, journeys, the erection runner, the sotah runner; the register gate's Num 34 headers seat), THE
DESIGN in this file before any code (the four sides as data; the lot by CALL; the nine and a half against the grant; the commission's shape; the
checkpoint prefix grepped first), the probes to FAIL, the docket by the union rule, the types, the runner, the tape, every gate with THE REGISTER GATE
--strict at the gates step, the sweep — before chapter 35, never the next reading first.
'''

STATE = '''
═══ COMPACTION POINT #155 (2026-09-12 — written at THE NUMBERS WALK sitting 14's close; THE BORDERS 34:1-29 READ AND FROZEN; NUMBERS 1:1-34:29 READ, 27 BY THE TENT; 1:1-33:56 COMPILED AND ON THE TAPE; 34 NOT YET COMPILED; A CLEAN COMPACTION POINT) ═══
STATE: 209 frozen units (208 + 1), standing 2149 (2136 + 13 as predicted), hash 8b8fff1fa28953af UNMOVED; 55 runners, 60 daemons, the sweep 55/55 at 6271 UNMOVED (no runner changed); the journal gate, the register gate and the cursor probes GREEN as at 13b's close; RUN (1274, 66, 52, 0, 12, 1522, 31, 318, the four pairs, 121). LAST COMMIT a42f518; UNCOMMITTED: sittings 8 through 13b's paths, THE CLOSE LINE's, and this sitting's (logic/units/num_34_borders.yaml FROZEN; logic/oral_triage/num_34_borders_2026-09-12.md NEW; logic/oral_audit/manifests/num_34_borders_claims.json NEW; logic/py_units/num_34_borders.py NEW; logic/py_units/ALL_UNITS.py; logic/pre_logic_methods_2026-07-28/UNIT_INDEX.html; logic/corpus/CORPUS_TRUTH.py (209 / 2149); corpus_world.sqlite; logic/glosses/word_gloss_overrides.yaml (+31 by reference, +28 by gloss); logic/findings/STAMP_LEDGER.md; World/step9/NUMBERS_WALK.md ("Sitting 14"); World/step9/COMPILE_DEBT.md (the sitting-14 box); RESEARCH_LOG.md; THE_STEPS.md; THE_BRIEFING.md; World/RESUME.md; World/step9/forms_numbers_walk/ (this sitting's scripts copied in); the recovery file's section 14; this doc) — commit only on "commit push" (the NEVER-COMMIT set and the staging-by-exclusion form as before; ARCHITECTURE excluded).
THE SITTING (the owner: "Go" after the #154 rereads; NUMBERS_WALK.md "Sitting 14"): chapter 34 read as ONE draft (num_34_borders 34:1-29; 35:1 the next draft's) from sitting 13's forms: the Sifrei on Numbers found BY POSITION to have NO piska on the chapter (158 on 31:22 followed by 159 on 35:9 — the shelf's silence ends at 35:9); the whole export scanned in FOUR citation forms (the English "Bamidbar" and "Ibid.", the Hebrew gershayim mark and the Hebrew "ibid." — the word "there" before the mark, a fourth form found this sitting): ONE row of another chapter cites 34:2 (1:2 — Rabbi Shimon ben Yochai's "command" everywhere entails expense EXCEPT this one, "impel them to the division of the land"; the census meets the row — the five "command the children of Israel" seats of the Torah are the row's five), credited with a quick look (read whole at sitting 2); the false "Ibid. 34" hits Exodus 34:30 and Deuteronomy 34:1-3 read to their verses. Onkelos whole (29) = 29 sources in one ledger (EIGHTEEN asserts fell on the first typed pass, one on the second, none on the third — six slice indices, a scope, a set-against-list count, two hand tallies, a substring census, a prefix tuple, and EIGHT POINTED COMPARISONS on THE MARKS' ORDER met by NFC on both sides; no cut miss; lint 0 first write); 13 claims verified 13/13 and labeled, 13 operators seated, the ritual COMPLETE (13 PASS) → 209 units, standing 2149, hash unmoved (predicted); THE PARSER three number verses, every one read — 34:13 [9], 34:15 [2] (the construct "two of"), 34:18 [1, 1] (the distributive doubling as two ones); NO GAP. THE FINDS: the border's own verb "you shall mark out" three Bible seats all here (Proverbs' "desire" its homograph); the goings-out word the Torah's five seats all here (fourteen in Joshua); 34:4 the one written singular read plural; Judah's south border is the land's (twenty of thirty-three tokens with Joshua 15:1-4; Hazar-addar split into two places); the spies walked the border's length (two words at two seats each — 13:21 and 34:3, 34:8); the side-word the tabernacle's; the sea as the west, one token seven times, split by Onkelos; the great sea plene and defective in adjacent verses; the second Mount Hor and Onkelos's two spellings; the blotting verb on the border (the sotah's 5:23 token); the shoulder the ephod's word on a shore; the Salt Sea at both ends of the loop, "by its borders" the inclusio; Ezekiel's sides from the north; ONE TRIBE-NOUN (eighteen staff-words, no other; 32:33's the neighbor); Joshua 14:2 quoting 34:13's six words under "by the hand of Moses"; "nine" in the construct three seats, all the nine tribes; the Reubenite-and-Gadite pair's first seat; the one root in three stems, the intensive's other three seats Joshua's runs, the object switching from the land to the people; the distributive doubling (the spies, the rods, the dedication, Joshua's stones and embassy); Caleb's five words from 13:6, the two survivors the only persons of the spies' roster here, no prince of chapter 1, Ammihud three tribes' fathers' name, eight names only here, Shemuel the first of the prophet's name, seven of ten El-names, the title dropped for three, the order matching no other roster (Manasseh before Ephraim as 26 and Genesis 46; Zebulun before Issachar as the two blessings; the four northern in Joshua's lot order); no receipt in the chapter — Joshua 14:2's outside the Torah; Onkelos's splits and merges (the lot's fall made "divide"; the brook from the inheritance; Rekem Geah; "great" for the sea and the prince; one tribe-word); the store's fifty-nine gloss rows (by reference and by gloss, each family censused).
THE RECORDS: NUMBERS_WALK.md "Sitting 14"; the ledger, manifest and py rendering; RESEARCH_LOG.md's entry; COMPILE_DEBT.md's sitting-14 box (a)-(k); STAMP_LEDGER's row; THE_STEPS' sitting-14 paragraph; THE_BRIEFING's scoreboard bullet; the gloss override rows; World/RESUME.md; the forms copied into World/step9/forms_numbers_walk/; memory (numbers-in-order-ruling.md, MEMORY.md, step9-exam-era.md's lessons head); the recovery file's section 14; this entry.
NEXT on the ruling: SITTING 14b — THE COMPILE OF THE BORDERS on 1b's order (COMPILE_DEBT's sitting-14 box (a)-(k): the measurements first — the tape's state, the callees live (the second census's the_land('by_lot'); the Gad runner's grant and the two and a half's rows; shelach's 13:6, 13:21, 14:30, 38; chukat's 20:22 and its two-Hors row; bamidbar's 1:5-15; naso's 7:11; korach's 17:21; zelophehad's 27:19-22; the journeys' 33:51, 33:54; the erection's court sides; the sotah's 5:23 — FALSE), the register gate's Num 34 headers seat; THE DESIGN in NUMBERS_WALK.md before any code — the four sides as a DATA row of named points with their kin seats, the lot by CALL (VIA second_census), the nine and a half against the grant (a run citation of the tape's own transfers; Joshua 14:2's receipt outside the Torah), the commission's shape (the dividers as a list-valued line, no entity for a named party), the checkpoint prefix grepped first, THE PREDICTION'S ARITHMETIC; then the probes to FAIL (measured — likely zero), the state doc's checkpoint, the docket by the union rule (Gittin 8a, Kiddushin 36b-37a, Mishnah Sheviit 6:1 and 9:2, Bava Batra 117a-122a credited, Sanhedrin 16a, the link rows), the types, the gates to FAIL, the runner, the recorder, the stitcher, the literals, the tape, the probe gates, the daemon and dependency gates, the journal gate, THE REGISTER GATE --strict, the sweep, the records), THEN CHAPTER 35 — the refuge cities' reading (35:1-34; THE SIFREI RETURNS at 35:9 — piskaot 159-161 by position) — NEVER THE NEXT READING FIRST.
POST-COMPACTION REREADS (mandatory, first sitting): the recovery file logic/pre_logic_methods_2026-07-28/RECOVERY_new_thread_2026-09-12.md whole (its section 5 THE COMPILE SITTING; its sections 13 and 14) + numbers-in-order-ruling.md + this entry + NUMBERS_WALK.md "Sitting 13b — AS BUILT" (the compile's form) + NUMBERS_WALK.md "Sitting 14" (this reading's record and the owed list) + THE_STEPS Step 2 + Step 5 + the compiler block; memory's STANDING LESSONS head (the sitting-14 paragraph first); THE_LOOP.md "Step 1's amendment — THE CLOSE LINE" before any journal or cursor work. WATCHES: as #154's + THE HEBREW IBID IS "THERE" + THE MARKS' ORDER MET BY NFC ON BOTH SIDES + THE SLICE INDEX FROM THE PRINT (a sixth instance) + A SET COUNTS VERSES, A LIST COUNTS TOKENS + THE FLOOR OF FOUR CODE POINTS.
'''

RESUME = '''SITTING 14 DONE 2026-09-12 (THE BORDERS 34:1-29 READ AND FROZEN; NUMBERS_WALK.md "Sitting 14"; the owner: "Go" after the #154 rereads): the Sifrei on Numbers found BY POSITION to have no piska on the chapter (the shelf silent 31:25-35:8, returning at 35:9; the cross-citing scan in FOUR forms — the Hebrew "ibid.", the word "there" before the chapter mark, a fourth form found this sitting — one row of another chapter, 1:2 citing 34:2 as the one "command" without expense, credited with a quick look; the census meets the row: the Torah's five "command the children of Israel" seats are the row's five) + Onkelos whole (29) = 29 sources in one ledger (eighteen asserts fell on the first typed pass, one on the second, none on the third — six slice indices, a print's scope, a set-against-list count, two hand tallies, a substring census, a prefix tuple, and eight pointed comparisons on THE MARKS' ORDER met by NFC on both sides; no cut miss; lint 0 first write); 13 claims verified and labeled, 13 operators seated, the ritual COMPLETE → 209 units, standing 2149, hash unmoved (predicted); THE PARSER three number verses, every one read — the nine, the construct "two of", the distributive doubling as two ones; NO GAP; THE BORDER'S OWN VERB "you shall mark out" three Bible seats all here; THE GOINGS-OUT the Torah's five all here, 34:4 the one written singular read plural; JUDAH'S SOUTH BORDER IS THE LAND'S (twenty of thirty-three tokens with Joshua 15:1-4; Hazar-addar split in two); THE SPIES WALKED THE BORDER'S LENGTH (two words at two seats each, 13:21 and here); the side-word the tabernacle's; the sea as the west, split by Onkelos; the great sea plene and defective in adjacent verses; the second Mount Hor and Onkelos's two spellings; the blotting verb on the border; the shoulder the ephod's word; the Salt Sea at both ends of the loop; ONE TRIBE-NOUN (eighteen, no other; 32:33's the neighbor); Joshua 14:2 quoting 34:13's six words; "nine" in the construct three seats; the one root in three stems, the intensive's three other seats Joshua's runs; the distributive doubling; CALEB'S FIVE WORDS FROM 13:6, the two survivors the only persons of the spies' roster here, no prince of chapter 1, eight names only here, Shemuel the first of the prophet's name, the title dropped for three, an order matching no other roster; the store's fifty-nine gloss rows. NEXT: 14b — THE COMPILE OF THE BORDERS (COMPILE_DEBT's sitting-14 box (a)-(k); the four sides as data; the lot by CALL; the nine and a half against the grant; the commission's shape; the register gate's Num 34 headers seat), THEN chapter 35 (the refuge cities; the Sifrei returns at 35:9) — never the next reading first.
'''

STEPS = '''SITTING 14 — THE BORDERS, Numbers 34:1-29 (2026-09-12, on Brian's "Go" after the #154 rereads; World/step9/NUMBERS_WALK.md "Sitting 14"). The
chapter read as one draft (35:1 the next draft's) on Onkelos whole — the Sifrei on Numbers has no piska on it, found by position (its silence ends at
35:9), and the whole export was scanned for any row citing the chapter in four forms, one of them new this sitting: the Hebrew rows say "there" before a
chapter mark where the English says "Ibid." — the one row that cites 34:2 reads "command" everywhere as a cost except here, where it means "impel them to
divide the land", and the ink agrees: the five seats of "command the children of Israel" in the Torah are the row's five. Every quotation cut from the
bytes by consonants in glossed pieces, no cut miss, the lint clean on the first write. The parser measured first: three number verses, every one read —
the nine tribes, the construct "two of", and "one prince, one prince" read as two ones — no gap. The finds: the verb "you shall mark out" stands three
times in the Bible, all in this chapter (Proverbs' "do not desire" wears its letters); "its goings-out" has five Torah seats, all here, and 34:4 is the
one written singular read plural; Judah's south border in Joshua 15 is this chapter's south side almost word for word, with one place split into two;
the spies' range (13:21) began where the south side begins and ended at the north's point, in two words that stand nowhere else; the side-word is the
tabernacle's; the sea is also the west, one token seven times, which Onkelos splits into two words; the north border's Mount Hor is a second Mount Hor;
the verb that "reaches" the shoulder of the sea of Chinnereth is the verb that blots the sotah's scroll into the water; the chapter says "tribe" with
one noun eighteen times and never the other, and Joshua 14:2 quotes its six words "to the nine tribes and the half tribe" under "as the LORD commanded
by the hand of Moses"; "inherit" runs in three stems and the strong stem's other three seats are Joshua's runs of this commission; "one prince, one
prince from a tribe" is the doubling that sent the spies and gave the rods; Caleb is seated among the dividers in the five words that sent him as a spy,
and the two survivors are the only men of the spies' roster here; the ten princes' order matches no other roster of the Torah. Eighteen typed facts fell
on the first pass — six slice indices, and eight pointed comparisons that fell on the order of the vowel points, met by normalizing both sides — and
none on the third. Thirteen claims verified, seated, the ritual complete, the corpus rebaked to the predicted count with the hash unmoved. Next: the
compile (14b), then chapter 35 — never the next reading first.

'''

BRIEF = '''- **THE BORDERS READ AND FROZEN — SITTING 14 DONE: THE CHAPTER'S OWN VERB STANDS NOWHERE ELSE, JUDAH'S BORDER IN JOSHUA IS THIS CHAPTER'S SOUTH SIDE, THE SPIES WALKED THE BORDER'S LENGTH, AND CALEB IS SEATED AMONG THE DIVIDERS IN THE WORDS THAT SENT HIM AS A SPY** (2026-09-12, on your "Go"; World/step9/NUMBERS_WALK.md "Sitting 14"). Chapter 34 read as one unit on Onkelos whole — the Sifrei has no piska on it, and the one row elsewhere that cites it (on "command", credited) agrees with the ink's count of five. The parser read its three number verses, no gap. Thirteen claims, the 209th frozen unit, the corpus at 2149 with the hash unmoved. Next: the compile (14b), then chapter 35 (the refuge cities — the Sifrei returns at 35:9).
'''

DEBT = '''
## SITTING 14 — THE BORDERS' READING (2026-09-12; NUMBERS_WALK.md "Sitting 14"; logic/oral_triage/num_34_borders_2026-09-12.md; the unit
## num_34_borders FROZEN) — OWED TO THE COMPILE (14b, on 1b's order with the register gate at the gates step): (a) THE FOUR SIDES AS A DATA ROW — the
## border's named points in order (the south 34:3-5: the wilderness of Zin, Edom, the Salt Sea, the ascent of Akrabbim, Zin, Kadesh-barnea, Hazar-addar,
## Azmon, the brook of Egypt, the sea; the west 34:6: the great sea; the north 34:7-9: the great sea, Mount Hor, Lebo-hamath, Zedad, Ziphron, Hazar-enan;
## the east 34:10-12: Hazar-enan, Shepham, Riblah, Ain, the sea of Chinnereth, the Jordan, the Salt Sea) with their kin seats (Joshua 15:1-4, 12; Ezekiel
## 47:15-20) and the two Mount Hors (the chukat runner's two_mount_hors row cited, not rewritten); the spec of the land's extent spoken, no act on the tape
## unless the design places the spec as ONE line (the journeys' shape: a list-valued write on the people); the four promised extents (Genesis 15:18, Exodus
## 23:31, Deuteronomy 1:7, 11:24; Joshua 1:4) and Ezekiel's order DATA rows with no verdict; (b) THE LOT — 34:2's "shall fall to you as an inheritance" and
## 34:13's "you shall inherit by lot" cite the second census's cell (C2.the_land('by_lot') — VIA second_census, as at 32:18 and 33:54); (c) THE NINE AND A
## HALF — 34:13-15's "the two tribes and the half tribe have taken their inheritance" is a RUN CITATION of the Gad runner's grant on the tape (32:33's three
## holding_given transfers; the two and a half's 110,580 off the population table) — read the ledger's own lines, write nothing twice; Joshua 14:2's receipt
## "as the LORD commanded by the hand of Moses" quoting 34:13 OUTSIDE THE TORAH — THE READBACK's class (the Jabesh-gilead and the release at Joshua 22 kin);
## (d) THE COMMISSION 34:16-29 — the dividers named (Eleazar, Joshua, the ten princes): a tape line whose value is the list (as journeys_written's), or a
## DATA row; NO ENTITY for a named-but-not-written-on party (12b's lesson); the ten princes against chapter 1's twelve, the spies' twelve and Joshua 22:14's
## ten as DATA; (e) THE REGISTER GATE'S NUM 34 HEADERS SEAT — "these are the names of the men" at 34:17 and 34:19 (the register-header class), declared NONE
## with the why "chapters 34-36 NOT YET WALKED": PAID (the roster as the line's value) or HELD with the why refreshed at the gates step (10b's lesson); no
## count line, no receipt, no footer in the chapter (measured at the reading: the closer 34:29 is not the receipt form); (f) THE PARSER — no rule owed; the
## distributive doubling reads [1, 1] (right: two tokens, "each" the idiom's sense) — a class named, not a gap; the construct "two of" at 34:15 and "nine" at
## 34:13 right; (g) THE EDGES the census will demand — second_census (26:52-56), gad_reuben (32:33, 32:19), shelach (13:6 Caleb, 13:21 the spies' range,
## 14:30, 14:38), chukat (20:22-23 Mount Hor — the OTHER Hor; the two-Hors row), bamidbar (1:5-15 the roster's form, 1:10 Ammihud), naso (7:11 the
## distributive), korach (17:21 the rods' distributive), zelophehad (27:19-22 Eleazar and Joshua), journeys (33:51, 33:54), the erection runner (Exodus
## 27:9, 27:13 the court's south and east sides — REFERENCE by the side-word and "eastward, toward the sunrise"), the sotah runner (5:23 the blotting verb —
## FALSE, a homograph by sense: the border reaches, the priest blots), Genesis 14:3 (the Salt Sea's identity clause) and 15:18 (the covenant's river)
## OBSERVED; Joshua 13:7, 14:1-2, 15:1-12, 18:20, 19:49-51, 21:5-6, 22:14, Ezekiel 47:13-20, 48:1, 28, 1 Kings 8:65, 2 Kings 14:25 FORWARD — no link, or a
## labeled HYPOTHESIS; (h) THE DOCKET by the union rule — Gittin 8a (34:6's "and its border": the islands in the sea; the borders of the land for the
## commandments), Kiddushin 36b-37a (the commandments bound to the land), Mishnah Sheviit 6:1 and 9:2 (the three lands), Bava Batra 117a-122a (credited to
## the second census's docket), Sanhedrin 16a (the tribe's court and its prince), the link rows for 34:2 (Sifrei 1:2 credited), 34:6, 34:13, 34:18; the
## Tosefta of the boundaries (Sheviit 4:11) if local; (i) THE DISPLAY LAYER — done at the reading (fifty-nine rows); the store's bare "seas" gloss beyond
## the chapter (the sea and the seas one gloss) a display sitting's census; (j) THE CHECKPOINT PREFIX — grepped before naming (CZ taken at 13b; CG Genesis's);
## (k) THE TWO ORDERS — Numbers' south-west-north-east against Ezekiel's north-east-south-west, and the roster's order against the twelve, DATA rows.
'''

RESEARCH = '''
## 2026-09-12 — THE BORDERS' READING (THE NUMBERS WALK sitting 14): THE HEBREW IBID IS "THERE"; THE MARKS' ORDER ON THE INK'S ASSERTS; THE WRITTEN
## SINGULAR READ PLURAL; THE STORE'S GLOSS FAMILIES BY CENSUS; THE FLOOR OF FOUR CODE POINTS; THE BORDER'S OWN VERB AND ITS PROVERBS HOMOGRAPH

Numbers 34:1-29 read (logic/oral_triage/num_34_borders_2026-09-12.md; NUMBERS_WALK.md "Sitting 14"; the unit num_34_borders frozen, 209 units). Every
item below is computed in the sitting's scripts (bor_ink.py's asserts; bor_measure1.py / bor_measure2.py the prints).
1. THE HEBREW IBID IS "THERE". The Sifrei export's Hebrew rows cite a verse of the last-named book as שָׁם "there" followed by the chapter mark — (שם ל"ד)
   "(ibid. 34)" — where the English writes "(Ibid. 34:2)". Sitting 13's widened scan took the English "Ibid." and the Hebrew mark with the book's name
   and the gershayim; it would have missed a Hebrew row citing this chapter by "there" alone. The scan now takes FOUR forms; the one row citing 34:2
   (1:2) was found by the English form and confirmed by the Hebrew's "there"; two Hebrew "there 34" hits are Exodus 34:30 (1:7) and Exodus 34:20 (118:1,
   unparenthesized in the export), read to their verses. The class: the coverage line names four forms, and a Hebrew row's "there" is read to the row's
   last-named book like the English "Ibid.".
2. THE MARKS' ORDER ON THE INK'S ASSERTS. Eight pointed comparisons fell on the first typed pass: the DB's raw order of the vowel points differs from
   the canonical order (the dagesh written before or after the vowel; the meteg after the sheva) — בְּֽנַחֲלָה "as an inheritance" (34:2) carries a meteg, הַגָּדוֹל
   "the great" (34:6) the dagesh before the qamats in the raw and after it in the canonical. Sitting 7 met the same class on the ledger's cuts (twelve
   asserts, NFC on both sides); the ink's pointed comparisons now go through one helper that normalizes both sides (NFC) and keeps the meteg the print
   shows. Where the raw order already is canonical (וּמָחָה "and it shall reach", לָעָיִן "to Ain") the comparison passed either way — the fault is silent
   until it bites.
3. THE WRITTEN SINGULAR READ PLURAL. 34:4 וְהָיָה תוֹצְאֹתָיו "and it shall be its goings-out" is written with the singular verb and read with the plural (the
   snapshot store carries both tokens, ו/היה then וְ/הָיוּ֙; the Tanakh DB carries the written form, morphology HC/Vqq3ms) — the chapter's one
   written-and-read pair; the clause's four other seats (34:5, 8, 9, 12) are written plural. Joshua 15:4 carries the identical clause with the written
   singular (the DB's token; the store holds no Joshua, its reading unmeasured here). The class (sitting 12's): a pair is one token more in the store.
4. THE STORE'S GLOSS FAMILIES BY CENSUS. The display layer's rows are written by reference where a gloss stands at other words elsewhere and BY GLOSS
   where the store's every token of the gloss is the one word — the census FIRST, on the exact gloss strings: "cord" (19 tokens, all the border-word),
   "the-cord" (8), "and-cord" (4), "to-cord" (3), "from-cord" (1), "in-cord" (2); "the-powder" (4, all the salt); "hidden" (8, all the north); "Daniel"
   (25, all Dan); "Non" (16, all Nun); "from-pasture" (8); "front-suffix" (13); "sunrise-suffix" (9); "from-region-across" (8); "exit-him/its" (4);
   "in-pebble" (4); "the-seas" (35, all singular); "the-Jordan-suffix" (1); "to-boundary-her/its" (2); "Kadeshbarnea" (6); and the broken
   "inherit--mode-of-descent)" family (a stray parenthesis at every stem of the inheritance root, eight gloss strings). A substring census reaches
   "according" through the letters of "cord" — the assert names the six rewritten glosses, never the family. Twenty-eight by-gloss rows and thirty-one
   by-reference rows; the frozen unit untouched.
5. THE FLOOR OF FOUR CODE POINTS. A manifest check is the word's longest store-piece whole, floor four code points: וּמָחָה "and it shall reach" cuts to
   מחה (three), מִמַּטֶּה "from a tribe" to מטה (three), לְנַחֵל "to apportion" to נחל (three), שְׁנֵי "two of" to שני (three) — none can be a check; another word of the
   verse was chosen each time (Chinnereth, the plain stem's "they shall divide", Israel, "and he spoke"). Noted so the next manifest chooses first.
6. THE BORDER'S OWN VERB AND ITS PROVERBS HOMOGRAPH. תְּתָאוּ "you shall mark out" (34:7, 8) and וְהִתְאַוִּיתֶם "you shall mark out for yourselves" (34:10) are the
   verb's three Bible seats; Proverbs 23:3, 23:6 and 24:1 write תִּתְאָו "do not desire" with the same consonants — the Hitpael of the desire-root, told
   apart by the points (the tsere under the tav against the qamats under the alef) and the morphology (HVpi2mp against HVtj2ms). Joshua's borders use
   תָּאַר "was drawn" (15:9, 11; 18:14, 17) — another root. A consonantal census of the border's verb counts six; the morphology three.
7. ONKELOS'S TWO SPELLINGS OF HOR IN ADJACENT VERSES. The export's Onkelos writes הר טורא "Hor the mountain" at 34:7 and הור טורא at 34:8 — the same
   mountain (the north border's), two spellings; chapters 20-21 carry the first, chapter 33 the second. A scan of the translation for the name takes
   both (sitting 13 found five of one form; this sitting six of the other).
'''

# ---- the memory index is sized BEFORE any record is written (the 17,000-byte limit; a failure here writes nothing) ----
mi = f'{MEM}/MEMORY.md'; s_mem = open(mi, encoding='utf-8').read()
old = [l for l in s_mem.split('\n') if l.startswith('- [⚠ NUMBERS IN ORDER FROM 1:1](numbers-in-order-ruling.md)')]
assert len(old) == 1
new = ('- [⚠ NUMBERS IN ORDER FROM 1:1](numbers-in-order-ruling.md) — OWNER-RULED 2026-09-09: the chapter walk from 1:1 at the parashah grain (map World/step9/NUMBERS_WALK.md; chapters 9, 15:32-41, 27, 36 frozen at THE TENT and SKIPPED); ⚠ OWNER-RULED 2026-09-10 READ THEN COMPILE PER PORTION, never read ahead; CHAPTER NUMBERS, not portion names. NUMBERS 1:1-33:56 READ, FROZEN, COMPILED AND ON THE TAPE (sittings 1-13b; 55 runners, 60 daemons, RUN (1274, 66, 52, 0, 12, 1522, 31, 318, four pairs, 121); THE CLOSE LINE built 2026-09-12; 13b: THE FORTY-TWO A DATA ROW, the run of Exodus 12:12 told at 33:4 alone, the command\'s two debits OPEN BY DESIGN to Joshua, M-30 THE RETREAT); NUMBERS 34:1-29 READ AND FROZEN (sitting 14, 2026-09-12, #155: 209 units, standing 2149, hash 8b8fff1fa28953af unmoved; the border\'s own verb three Bible seats all here; the goings-out the Torah\'s five all here; Judah\'s south border in Joshua 15 the land\'s; the spies walked the border\'s length; one tribe-noun; the intensive stem\'s three other seats Joshua\'s runs; Caleb\'s five words from 13:6; the roster\'s order matching no other; the Hebrew "ibid." is "there" — a fourth citation form). COMMITTED a42f518 (2026-09-11); sittings 8-14 UNCOMMITTED. THE REGISTER GATE (register_census.py --strict) AT EVERY COMPILE SITTING\'S GATES STEP. NEXT: 14b — THE COMPILE OF THE BORDERS (COMPILE_DEBT\'s sitting-14 box (a)-(k)), THEN CHAPTER 35 — the refuge cities\' reading (35:1-34; THE SIFREI RETURNS at 35:9, piskaot 159-161).')
s_mem = s_mem.replace(old[0], new)
assert len(s_mem.encode()) < 17000, ('MEMORY.md would be %d bytes' % len(s_mem.encode()))
# the walk's memory file: the description's NEXT replaced (the running record's body appended below)
nr = f'{MEM}/numbers-in-order-ruling.md'; s_nr = open(nr, encoding='utf-8').read()
old_desc = "NEXT chapter 34's reading (the borders), then its compile."
assert s_nr.count(old_desc) == 1
s_nr = s_nr.replace(old_desc, "NUMBERS 34:1-29 READ AND FROZEN (sitting 14; 209 units, standing 2149, hash unmoved); NEXT 14b the borders' compile, then chapter 35's reading (the refuge cities; the Sifrei returns at 35:9).")

# ---- the recovery file's section 14 ----
RECOVERY = '''
## 14. ADDENDUM (2026-09-12, at sitting 14's close — the state doc's COMPACTION POINT #155; this supersedes section 13's NEXT, which is kept as written)

SITTING 14 DONE: CHAPTER 34 (the borders) READ AND FROZEN — 209 units, standing 2149, hash 8b8fff1fa28953af unmoved; NUMBERS_WALK.md "Sitting 14" the record
(the shelf's silence proved by position — it ends at 35:9; the cross-citing scan in FOUR forms, the Hebrew "ibid." (the word "there" before the chapter
mark) the fourth; one row credited — 1:2, the one "command" without expense, the ink's five seats the row's five; the parser's three number verses every one
read, the distributive doubling as two ones; the border's own verb three Bible seats all here; the goings-out the Torah's five all here; Judah's south border
in Joshua 15 the land's; the spies walked the border's length; one tribe-noun; the intensive stem's three other seats Joshua's runs; Caleb's five words from
13:6; the roster's order matching no other; eight pointed comparisons met by NFC on both sides); COMPILE_DEBT.md's sitting-14 box (a)-(k) the compile's
checklist. The engine, the tape, the sweep (55/55 at 6271) and every gate stand as at 13b's close. THE FORMS of sitting 14 are in
World/step9/forms_numbers_walk/ (bor_dump.py, bor_measure1.py, bor_measure2.py, bor_ink.py, bor_legs.py, bor_rows_onkelos_a.py / _b.py,
write_bor_ledger.py, write_bor_manifest.py, seat_bor.py, bor_chain.sh, patch_overrides_bor.py, write_bor_records.py, assert_driver.py): copy the latest to the
scratchpad and adapt. Still UNCOMMITTED since a42f518; commit only on "commit push".

NEXT: SITTING 14b — THE COMPILE OF THE BORDERS (34:1-29) on the compile shape of section 5, with the register gate at the gates step: the measurements (the
tape's state; the callees live — second_census, gad_reuben, shelach, chukat, bamidbar, naso, korach, zelophehad, journeys, the erection runner, the sotah
runner; the register gate's Num 34 headers seat at 34:17 and 34:19), THE DESIGN in NUMBERS_WALK.md before any code — THE FOUR SIDES AS A DATA ROW of named
points with their kin seats (Joshua 15, Ezekiel 47) and the two Mount Hors, THE LOT by CALL into the second census's cell (VIA second_census), THE NINE AND A
HALF as a run citation of the Gad runner's grant on the tape (Joshua 14:2's receipt outside the Torah — THE READBACK's), THE COMMISSION's shape (a list-valued
line, no entity for a named party), the checkpoints (the prefix grepped first), THE PREDICTION'S ARITHMETIC; then the probes to FAIL (measured — likely
zero), the docket by the union rule (Gittin 8a, Kiddushin 36b-37a, Mishnah Sheviit 6:1 and 9:2, Bava Batra 117a-122a credited, Sanhedrin 16a, the link rows),
the types, the gates to FAIL, the runner, the recorder, the stitcher, the literals, the tape, the probe gates, the daemon and dependency gates, the journal
gate, THE REGISTER GATE --strict, the sweep, the records — THEN CHAPTER 35 (the refuge cities' reading, 35:1-34; THE SIFREI RETURNS at 35:9, piskaot
159-161 by position) — NEVER THE NEXT READING FIRST. Before the compile: reread NUMBERS_WALK.md "Sitting 13b — AS BUILT" (the compile's form) and "Sitting
14" (the reading and the owed list), THE_STEPS Step 2 + Step 5 + the compiler block, memory's STANDING LESSONS head, THE_LOOP.md "Step 1's amendment — THE
CLOSE LINE".
'''

append(f'{ROOT}/logic/findings/STAMP_LEDGER.md', STAMP)
append(f'{ROOT}/World/step9/NUMBERS_WALK.md', WALK)
append(f'{ROOT}/logic/pre_logic_methods_2026-07-28/PROMPT_continue_solo_era_2026-08-06.md', STATE)
append('<world-link>/RESUME.md', RESUME)
insert_before(f'{ROOT}/THE_STEPS.md', '## THE FINDINGS LOOP + THE STAMP LAW (owner-approved 2026-08-31)', STEPS)
insert_after(f'{ROOT}/THE_BRIEFING.md', '## SCOREBOARD (as of 2026-09-12, latest)\n', BRIEF)
append(f'{ROOT}/World/step9/COMPILE_DEBT.md', DEBT)
append(f'{ROOT}/RESEARCH_LOG.md', RESEARCH)
append(f'{ROOT}/logic/pre_logic_methods_2026-07-28/RECOVERY_new_thread_2026-09-12.md', RECOVERY)

# ---- the forms: sitting 14's scripts into the walk's forms folder (the latest forms live in the repo, not the scratchpad) ----
FORMS = f'{ROOT}/World/step9/forms_numbers_walk'
copied = 0
for pat in ('bor_*.py', 'bor_*.sh', 'write_bor_*.py', 'seat_bor.py', 'patch_overrides_bor.py', 'assert_driver.py'):
    for f in glob.glob(f'{SP}/{pat}'):
        shutil.copy2(f, f'{FORMS}/{os.path.basename(f)}'); copied += 1
print(f'forms copied: {copied} -> {FORMS}')

# ---- memory ----
open(nr, 'w', encoding='utf-8').write(s_nr); append(nr, RESUME)
open(mi, 'w', encoding='utf-8').write(s_mem); print('MEMORY.md: the numbers line %d -> %d bytes; file %d bytes' % (len(old[0].encode()), len(new.encode()), len(s_mem.encode())))
LESSON = ('⚠ THE NUMBERS WALK sitting 14 — THE BORDERS\' READING (2026-09-12): THE HEBREW IBID IS "THERE" — the export\'s Hebrew rows cite a verse of the last-named book as "there" plus the chapter mark where the English says "Ibid."; the citation scan takes FOUR forms now ("(Bamidbar n:m)", "(Ibid. n:m)", the gershayim mark with the book\'s name, "there" with the mark), and the coverage line names all four. THE MARKS\' ORDER MET BY NFC ON BOTH SIDES — eight pointed comparisons fell because the DB\'s raw order of the vowel points differs from the canonical at the dagesh and the meteg (sitting 7\'s lesson on the ledger\'s cuts, now on the ink\'s asserts): one helper normalizes both sides, the meteg kept where the print shows it; a comparison that passes on a canonical token hides the fault until the next token. THE SLICE INDEX FROM THE PRINT, A SIXTH INSTANCE — six slices one off (Onkelos 34:4, Exodus 23:31, Joshua 21:1, 21:6, Numbers 17:21, Onkelos 17:21): print the verse, then slice. THE SCOPE OF A PRINT IS PART OF THE NUMBER, AGAIN — a Joshua-filtered list typed as the whole-Bible census (the shoulder\'s 28 seats). A SET COUNTS VERSES, A LIST COUNTS TOKENS — Samuel\'s 125 tokens are 120 verses. THE HAND\'S TALLY AGAINST THE MACHINE\'S COLUMN — fourteen typed fifteen; a roster fact read off half the print (Genesis 46 also puts Manasseh before Ephraim). A BY-GLOSS ROW IS CENSUSED FIRST, ON THE EXACT GLOSSES — "according" carries the letters of "cord": assert the rewritten glosses\' tokens, never a substring family; the article\'s forms belong in the stem tuple. THE FLOOR OF FOUR CODE POINTS — a check word whose longest store-piece is three letters cannot be a manifest check; choose another word of the verse first. THE READING SITTING\'S SHAPE HELD (dump → measure in three passes → asserts 18 → 1 → 0 → rows → writer 0 misses, lint 0 first write → manifest 13/13 → seat → ritual 13 PASS → the fold predicted and matched); MIDDOT, MOVE_CATALOG and MISHNAH_TOPICS untouched when the spine is silent.\n')
insert_after(f'{MEM}/step9-exam-era.md', '## STANDING LESSONS AND WATCHES (moved verbatim from the MEMORY.md index line on 2026-09-07 to keep the index under its size limit; the W4/W3/W2/W1/D9/G/E lesson tail as it stood)\n', LESSON)
print('records written')
