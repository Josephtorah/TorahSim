import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE NUMBERS WALK sitting 15 — THE REFUGE CITIES (2026-09-13): the records — the stamp row, NUMBERS_WALK.md "Sitting 15", the state doc's #158,
# World/RESUME.md, THE_STEPS' paragraph, THE_BRIEFING's bullet, COMPILE_DEBT's box, RESEARCH_LOG's entry, MIDDOT's case-law entries (the Sifrei's rows
# on the chapter), the three memory files, the recovery file's section 16, and the forms copied into World/step9/forms_numbers_walk/. The counts below
# are the tools' own prints (the ritual's PASS lines, the bake's hash, the truth's units), typed from them; the corpus tripwire and the ritual's print
# are read back before a byte is written. Every insert lands on a unique anchor asserted present once. The gloss override rows were written by
# patch_overrides_ref.py at the ink step (asserted present by ref_ink.py) — verified here, not rewritten. MOVE_CATALOG.md and MISHNAH_TOPICS.md
# UNCHANGED (the rows' moves are known forms — exemplars entered in MIDDOT's case law; no Mishnah opened at a reading sitting). Sitting 14's form.
import os, re, yaml, shutil, glob
ROOT = _ROOT
SP = os.path.dirname(os.path.abspath(__file__))
MEM = '<memory>'
truth = open(f'{ROOT}/logic/corpus/CORPUS_TRUTH.py', encoding='utf-8').read()
assert 'assert len(W["units"]) == 210' in truth and 'assert len(W["standing"]) == 2163' in truth and "== '8b8fff1fa28953af'" in truth, 'the fold is not the predicted one'
rit = open(f'{SP}/ref_ritual_num_35_refuge_cities.out', encoding='utf-8').read()
assert 'RITUAL COMPLETE for num_35_refuge_cities (210 frozen units)' in rit and rit.count('PASS ') >= 13, 'the ritual is not complete'
assert os.path.exists(f'{ROOT}/logic/oral_triage/num_35_refuge_cities_2026-09-13.md') and os.path.exists(f'{ROOT}/logic/oral_audit/manifests/num_35_refuge_cities_claims.json') and '  status: frozen' in open(f'{ROOT}/logic/units/num_35_refuge_cities.yaml', encoding='utf-8').read()
d_ov = yaml.safe_load(open(f'{ROOT}/logic/glosses/word_gloss_overrides.yaml', encoding='utf-8'))
assert len([k for k in d_ov['by_ref'] if k.startswith('Num.35.')]) == 102 and d_ov['by_gloss']['the-dash-in-pieces'] == 'the-slayer' and d_ov['by_gloss']['concretely'] == 'witness' and d_ov['by_gloss']['in-mother'] == 'by-the-cubit', 'the override rows are not the ink\'s'
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

STAMP = ('| 2026-09-13 | num_35_refuge_cities | DELEGATED | FULL RULE | Numbers 35:1-34 derivation 2026-09-13 (THE NUMBERS WALK sitting 15 — THE REFUGE CITIES; the owner: "Go" after the #157 rereads, on the ruling READ THEN COMPILE; the FORTY-SEVENTH NUMBERS UNIT and the walk\'s LAST reading in the book — the portion Masei\'s third chapter as one draft, the next unit 36:1-13 frozen at THE TENT): declared reading COMPLETE — Onkelos Numbers 35:1-34 whole, 34 verses fresh; THE SIFREI ON NUMBERS RETURNS at 35:9 — piskaot 159-161 found BY POSITION (the export\'s last three; 158 on 31:22 before them; NO piska on 35:1-8), SIXTEEN rows at the English file\'s row grain, each read in BOTH files — the Hebrew file\'s 160 carrying FOURTEEN rows where the English carries TEN, its last four being 161:1-4 DUPLICATED (a defect class new to the walk), read as their twins; every head asserted between its neighbors and against its rows\' own citations; the rows\' defects read to their verses (the English 160:5 not the Hebrew 160:5 — the induction from three transposed; "thirty" for twenty-three; the rule "we do not punish by inference" dropped a second time; the mistyped and inserted citations; the Hebrew\'s misquoted Joshua 20:7; the colophon dropped); the whole export scanned in four forms for rows of other piskaot citing the chapter — 1:2 (on 35:2) and 1:7 (on 35:34), both CREDITED with a quick look. Ledger logic/oral_triage/num_35_refuge_cities_2026-09-13.md (50 sources; coverage computed — missing 0, extra 0 on both row grains; the ink facts computed from the Tanakh DB and the snapshot store, every fact an assert — five fell on the first typed pass, none on the second; every quotation cut by consonants in glossed pieces, no cut miss; the lint 18 → 2 → 0 inside the writing step — the shelf\'s own punctuation stripped from the cuts). 14 claims MS35A-01..14 verified 14/14 by verify_claims, labeled, seated as WITNESS_READ operators at their first verses; verify_text GREEN (34 steps, 7 scenarios); freeze ritual 13 PASS, RITUAL COMPLETE (the 210th frozen unit); the corpus rebaked to the prediction — units 210, standing 2163 (2149 + 14), hash 8b8fff1fa28953af UNMOVED; CORPUS TRUTH GREEN. THE PARSER: seven number verses read, ONE GAP — 35:5\'s bare dual "two thousand" four times unread (the class named for the compile; Onkelos reads it, supplying "two"). The finds: the four sides in the camp\'s order; the measure-verb\'s three Torah seats (the omer, the pasture-lands, the elders to the slain man); the refuge-word Numbers\', Joshua\'s and Chronicles\' — never Deuteronomy\'s; Joshua 21 summing the forty-eight; the second census\'s proportional rule at its third seat; "shall surely die" five times, the Torah\'s densest; the murder-root twenty times, one root for four agents, written defective at every Numbers seat; the serpent\'s "enmity"; the high priest written defective only here; "he has no blood" the burglar\'s clause; a statute of judgment the daughters\' phrase; the sixth and the ninth commandments\' verbs in one verse; the ransom\'s root three times; the pollute-root\'s only Torah seat and Psalm 106\'s echo; the book\'s inclusio "in whose midst I dwell" (5:3, 35:34). Stamp delegated under the AUTO-SEAT ruling; the owner may overrule. |\n')

WALK = '''
## Sitting 15 — THE REFUGE CITIES, Numbers 35:1-34 (2026-09-13; the owner: "Go" after the #157 rereads, on the ruling READ THEN COMPILE): the reading and the unit

THE DRAFT: one — num_35_refuge_cities 35:1-34 (34 of 34 verses, computed): the portion Masei's third chapter whole; the next unit, num_36_heiresses
36:1-13, is FROZEN at THE TENT (sitting 4) — this is the walk's LAST reading in Numbers. Read in ONE pass, one ledger. The forms copied from sitting 14's
scripts in World/step9/forms_numbers_walk/ and edited, with sitting 11's Sifrei block (ref_dump.py, ref_measure1.py, ref_measure2.py, ref_ink.py,
ref_rows_onkelos_a.py / _b.py, ref_rows_sifrei.py, write_ref_ledger.py, write_ref_manifest.py, seat_ref.py, ref_chain.sh, patch_overrides_ref.py,
write_ref_records.py; every one copied into the forms folder at the close).

THE SHELF, BY POSITION (ref_ink.py's asserts): THE SIFREI ON NUMBERS RETURNS AT 35:9 — piska 158 (31:22) is followed by 159 (35:9, one row), 160
(35:12) and 161 (35:29, five rows), the export's LAST THREE piskaot, all on this chapter; NO piska on 35:1-8 (the shelf's silence from 31:25 ends at
35:8 — 165 verses, computed at sitting 11); every row's first citation is its head in order (no mistyped head; 161:4 opens on Deuteronomy 21:1, the two
priests' story read at 35:33). THE ROW-GRAIN MISMATCH, MEASURED: the English file's 160 carries TEN rows, the Hebrew's FOURTEEN — the Hebrew 160:11-14
are 161:1-4 AGAIN, byte-near-identical (the dash character the one systematic difference; 160:11 drops the kaf of "whoever"; 161:4 alone parenthesizes
its Kings citation): A DUPLICATED BLOCK, a defect class new to the walk (RESEARCH_LOG.md). The ledger's grain is the English's SIXTEEN rows (1 + 10 + 5),
each read in both files; the four duplicates read as their twins, named, never counted twice; the coverage line names both grains (16 and 20). The
Hebrew 161:5 closes with the book's colophon — "the book of Numbers is completed; blessed is the man who trusts in the LORD" — which the English drops.
THE ROWS' OWN DEFECTS read to their verses in both files: 159:1's English cites Deuteronomy 12:29 where the Hebrew cites Deuteronomy 19 (the clause
"when the LORD your God cuts off the nations" stands at both — 19:1 opens the refuge chapter, the apt seat) and "Ibid. 26:3" where the Hebrew names
Numbers 36 (the stamp's seven seats); 160:2's Hebrew misquotes Joshua 20:7 ("Hebron IN THE LAND OF CANAAN" for "in the hill country of Judah") and its
a-fortiori "all the more he is not exiled" is dropped by the English; 160:3's Hebrew cites "Exodus 11" for 21:18 and carries THE RULE ABOUT RULES "we do
not punish by inference", which the English DROPS — the same drop as at 157:6 (sitting 11's finding), a second instance; 160:5 THE TWO FILES CARRY
DIFFERENT ROWS — the Hebrew the induction from the three instruments (the common feature: it can kill), the English two sentences on the court-appointed
avenger (the Hebrew's 160:7 tail), the induction carried into the English 160:6; 160:8's English "THIRTY" for the Hebrew's TWENTY-THREE, its "[27]"
for the congregation-tokens' seats (the ink: 24, 25, 25 — and 12), the Mishnah's acquittal-by-one / conviction-by-two SUPPLIED where the Hebrew says
"as witnesses are two, so the judges, and a court is not even — add one"; 160:10's "(37)" and "(38)" for verses 27 and 28; 161:1's inserted "Whence is
this derived?"; the English's "viz. Shemot 21:15" supplied at 159:1. THE "FOUND BY POSITION" CLAUSE run on the whole export in FOUR FORMS for rows
outside 159-161: TWO rows of piska 1 cite the chapter — 1:2 (on 5:2: Rabbi Shimon ben Yochai's "command" entails expense, 35:2 the third of his four; the
Hebrew "ibid. 35") and 1:7 (on 5:3 "their camp in whose midst I dwell", citing 35:34 with the chapter mark and the gershayim, the double-stroke mark —
THE BOOK'S INCLUSIO read from its first seat): both CREDITED with a quick look (read whole at sitting 2, the Naso ledger). Onkelos 35 whole: 34. No
prior ledger had read a row of the chapter or of its piskaot; fifteen ledgers NAME a verse of it (the Sabbath block's 35:4-5 — the two thousand
cubits as the Sabbath limit's measure; the exams' 35:22-27, 35:29-31): names, not reads — FRESH.

THE READING (eleven modules — ref_dump.py the first measurement pass (the heads, both files' row counts and every row's first citation, the four-form
scan, the parser, the case tokens, the law vocabulary by token, the dumps); ref_measure1.py and ref_measure2.py the second and third (the duplicated
block's deltas byte by byte, the rows' defects located, the dual by its points on the whole DB, the token families where the DB's lemma column carries
a prefix, the homographs by morph and lemma, the store's gloss families censused, the whole by-reference index of the chapter's tokens); ref_ink.py the
ink with every fact an assert (assert_driver.py: FIVE failures on the first typed pass, NONE on the second — two slice indices (the seventh instance:
Genesis 27:20's "cause it to happen", Exodus 30:12's "ransom"), a morph prefix (the consecutive perfect carries the conjunction's — a filter on the
verb tag misses "you shall measure" and "you shall appoint"), a print's scope (the plene "three" whole-Bible against the Torah's three), and a count
of my own list (103 typed for 102)) and the piece-wise cutters HP / AP with a third for the shelf's Hebrew (the shelf's own punctuation stripped from
the cut after the lint read it as the Hebrew's end); ref_rows_onkelos_a.py and _b.py the 34 rows; ref_rows_sifrei.py the 16 rows (each read in both
files, the middah named); write_ref_ledger.py the writer → ONE ledger logic/oral_triage/num_35_refuge_cities_2026-09-13.md (50 sources: Onkelos
MATERIAL 34 / CONTEXT 0; the Sifrei MATERIAL 15 / CONTEXT 1 — the two priests' story; two rows credited; coverage computed on both row grains, missing 0,
extra 0; NO cut miss on the writer's first run — two eight-token pieces caught by the cutters' cap before it; gloss_lint 18 → 2 → 0 inside the writing
step); the display layer's rows written at the ink step by patch_overrides_ref.py (ONE HUNDRED AND TWO by reference, FIFTY by gloss — the by-gloss
families censused first; the rows read from the ink module's own literals, one source of truth).

THE INK, COMPUTED (the measurement passes FIRST, the asserts typed from the print):
- THE PARSER MEASURED FIRST (the standing rule): SEVEN number verses in thirty-four read — 35:4 "a thousand cubits" [1000] (the cubit consumed as the
  unit noun); 35:6 [6, 42]; 35:7 [48]; 35:13 [6]; 35:14 [3, 3]; 35:15 [6]; 35:30 "one witness" [1] — and ONE GAP: 35:5's "TWO THOUSAND BY THE CUBIT",
  four times, reads NOTHING. THE DUAL BY THE POINTS: "two thousand" carries the patach (the vowel point) and the dagesh (the dot) in the pe with the
  sheva under the lamed, "thousands" the qamats under the lamed — the dual at 26 Bible seats, and the parser reads it ONLY when a hundreds-group
  follows (4:36's 2,750, 4:40's 2,630, 7:85's 2,400, Exodus 38:29's 2,400 — right); BARE, before a unit noun or with the approximation prefix, it reads
  nothing (35:5 ×4; 1 Kings 7:26 "two thousand baths"; 2 Kings 18:23 and Isaiah 36:8 "two thousand horses"), reads the following cubit as one (Joshua 3:4
  "about two thousand cubits" → [1]), is swallowed (Joshua 7:3, Judges 20:45) or MISREAD AS A THOUSAND (1 Samuel 13:2 "two thousand with Saul" →
  1000); the plural "thousands" (116 seats) rightly reads nothing. THE CLASS NAMED AND LEFT FOR THE COMPILE (15b): THE BARE DUAL THOUSAND — 4b's owed
  line "Num 35:5's two thousand cubits" measured at last. ONKELOS READS THE DUAL: "two thousand" with "two" supplied at all four seats. Two kin readings
  filed: Ezekiel 45:2's "five hundred by five hundred" joined to 1,000 (the preposition inside a pair of measures), Exodus 27:9's "fine twined linen"
  read as six (the linen-word's homograph, the same pointing as "six"). No line of the tape names the chapter; the parser's own two comments in
  cold_run_sequence.py (lines 437, 504) name the gap.
- THE FRAMES AND THE REGISTER: TWO divine frames — 35:1 WITH THE PLACE-STAMP "in the plains of Moab by the Jordan at Jericho" (the stamp's six seats:
  26:3, 26:63, 33:48, 33:50, 35:1, 36:13 the footer; "and the LORD spoke to Moses in the plains of Moab" 33:50 and 35:1) and 35:9 bare; twelve chapters
  of Numbers carry exactly two, this the last. NINE narrative verbs — the two frames and SEVEN INSIDE THE CASES: "and he died" six times (16, 17, 18,
  20, 21, 23) and "and he dropped it" (23) — the case's consequent told in the story's tense. THE CASE TOKENS (the compiler law's structure): "when" opens
  at 35:10; "and if" at 16, 17, 20, 22, 26; "or" at 18, 20, 21, 22, 23; "for" at 28, 31, 33 (twice, with "except") and 34. The Levite-cities paragraph in
  the second person plural — "you shall give" TEN times (2, 4, 6 ×3, 7, 8, 13, 14 ×2), "you shall measure", "you shall take more / less", "you shall
  appoint"; the cases in the third person singular; nine negations; "to you" five; "he" nine; "he is a murderer" at four seats (16, 17, 18, 21). THE
  REGISTER GATE'S SEATS: none declared and none owed — register_dispositions.yaml has no Num 35 entry; REGISTER_INDEX.md's two lines on the chapter
  (35:15's six, 35:30's one) are MEASURE-ONLY green; 35:4-7's counts are measures under the unit rule (cubit, city): nothing to pay at the compile.
- 35:1-8 THE LEVITE CITIES: "command the children of Israel" the Sifrei 1:2's FIVE seats, this the third it names; "and they shall give to the Levites",
  "from the inheritance of their possession" one seat each; "CITIES TO DWELL IN" three seats — this, Joshua 14:4 and JOSHUA 21:2, THE RUN'S REQUEST
  quoting the spec under "the LORD commanded by the hand of Moses" (Joshua 14:2's receipt form at 34:13), 21:3 the giving "at the mouth of the LORD";
  THE PASTURE-LAND WORD six Torah seats (five this chapter's, Leviticus 25:34's unsellable field), 69 verses in the Bible, 32 Joshua 21's; "their
  beasts" two Bible seats (Ezekiel 7:13), ONKELOS "their needs of life"; "FROM THE WALL OF THE CITY OUTWARD A THOUSAND CUBITS" one seat, "a thousand
  cubits" the Bible's one, "two thousand by the cubit" 35:5's four tokens, "about two thousand cubits" Joshua 3:4's; "YOU SHALL MEASURE" — the
  measure-verb's THREE Torah seats: the omer (Exodus 16:18), this, and THE ELDERS MEASURING TO THE SLAIN MAN (Deuteronomy 21:2 — the heifer whose neck is
  broken, the case the Sifrei brings to 35:33); THE FOUR SIDES IN THE CAMP'S ORDER — east, south, west, north (35:5) as Numbers 2 orders the camps (2:3,
  10, 18, 25), where the borders ran south, west, north, east (34) and the court south, north, west, east (Exodus 27:9-13); "and the city in the midst"
  one seat; "SIX CITIES OF REFUGE" with the article one seat, bare three (11, 13, 14), "the cities of refuge" four (this, Joshua 20:2, 1 Chronicles 6:42,
  52); THE REFUGE-WORD twenty tokens in twenty verses — this chapter's eleven, Joshua 20's two and 21's five, Chronicles' two — and DEUTERONOMY NEVER
  SAYS IT; "forty-two cities" one seat; "FORTY-EIGHT" four seats — this, Joshua 21:41's tally, two of Nehemiah's census — and JOSHUA 21'S FOUR LOTS SUM
  TO IT (13 + 10 + 13 + 12 by the parser); the Levites 22,000 at 3:39 and 23,000 at 26:62; "THE CITY OF REFUGE FOR THE SLAYER" at five of Joshua 21's
  six — BEZER'S ROW (21:36) LACKS THE PHRASE; "them and their pasture-lands" one seat; THE PROPORTIONAL RULE 35:8 IS THE SECOND CENSUS'S — 26:54's and
  33:54's two verbs ("you shall take more" at 33:54 and this in the Torah; "you shall take less" here alone, its singular at Leviticus 25:16, 26:54,
  33:54), "each according to his inheritance" one seat.
- 35:9-15 THE REFUGE LAW: "WHEN YOU ARE CROSSING THE JORDAN" three seats (33:51, this, Deuteronomy 11:31), 33:51 "to the land of Canaan", this
  "to Canaan-ward" — the directional form at seven Bible seats, six Genesis's and this the Torah's last; "YOU SHALL APPOINT" (cause to happen) one seat —
  the root of Balaam's meetings (23:4, 16) and Abraham's servant's prayer (Genesis 24:12; 27:20), the Sifrei "calling out connotes designation";
  "cities, cities of refuge" the apposition one seat; "SMITES A SOUL UNWITTINGLY" four seats (35:11, 15; Joshua 20:3, 9), "whoever smites a soul" three
  (35:15, 30; Joshua 20:9), "smites a soul" five, all this chapter's and Joshua 20's; "UNWITTINGLY" thirteen seats — the sin offering's word (Leviticus
  4-5, 22:14; Numbers 15:26-29) and the slayer's; DEUTERONOMY SAYS "WITHOUT KNOWLEDGE" (4:42, 19:4) AND JOSHUA 20:3 SAYS BOTH; the bare "avenger"
  without "blood" at 35:12 and Joshua 20:3 (Onkelos supplies it; Malachi's "polluted" wears the consonants, another root); "UNTIL HE STANDS BEFORE THE
  CONGREGATION FOR JUDGMENT" this and Joshua 20:6 quoting it; "the three cities" with the article here alone, bare "three cities" Deuteronomy's (4:41,
  19:7, 9) and 19:2's PLENE "three" (one of the plene form's three Torah seats, 7b's rule); "the stranger and the sojourner" Abraham's pair (Genesis
  23:4; Leviticus 25:35, 47) — JOSHUA 20:9 DROPS THE SOJOURNER; "these six cities" one seat; "TO FLEE THERE" five seats — LOT'S FIRST (Genesis 19:20),
  Deuteronomy 19:3, this, Joshua 20:3, 9; "he shall flee there" three — EXODUS 21:13 THE SPEC'S FIRST SEAT ("a PLACE to which he shall flee": the place
  become cities), Deuteronomy 19:4, 35:26.
- 35:16-21 THE INSTRUMENTS AND THE AVENGER: "instrument of iron", "a stone of the hand", "a wooden instrument" one seat each; "whereby he may die" at
  the stone (17), the wood (18) and the unseen stone (23) — never at the iron: THE IRON VERSE HAS NO "HAND" AND NO SIZE CLAUSE, ten tokens against
  thirteen and fourteen (the Sifrei: iron kills at any size, "even a needle"); ONKELOS SUPPLIES THE SIZE CLAUSE at 17 and 18; "HE IS A MURDERER, THE
  MURDERER SHALL SURELY DIE" three seats (16, 17, 18), "the smiter shall surely die" 21; "SHALL SURELY DIE" twenty-two Torah seats (twenty-four in the
  Bible), FIVE HERE — THE TORAH'S DENSEST CHAPTER; THE MURDER-ROOT twenty-eight Torah tokens, TWENTY IN THIS CHAPTER (twelve "the slayer", six "a
  slayer", "and he murders" 27, "shall slay" 30 — ONE ROOT FOR FOUR AGENTS: the murderer, the manslayer, the avenger's kill, the court's execution), the
  others the sixth commandment's two, Deuteronomy 4:42's two, 19:3, 4, 6, 22:26; forty-seven tokens in forty Bible verses; WRITTEN DEFECTIVE AT EVERY
  NUMBERS SEAT, plene at Deuteronomy 4:42, Joshua 20:3, 6 and Job 24:14 alone (the shelf's Hebrew writes him plene); "THE AVENGER OF BLOOD" ten Bible
  seats — this chapter's five verses, Deuteronomy 19:6, 12, Joshua 20:5, 9, the woman of Tekoa (2 Samuel 14:11); ONKELOS "the avenger of blood" six
  seats and A CLAUSE OF ITS OWN at 19 and 21 — "when he has been found guilty by the court": the court before the avenger's hand; "when he meets him"
  two; the thrust-root eleven Bible tokens, four the Torah's; "IN LYING-IN-WAIT" the noun's TWO Bible seats both here, its verb EXODUS 21:13'S and
  David's (1 Samuel 24:12), the provisions-word its homograph at five seats; "IN ENMITY" — THE SERPENT'S WORD: the noun's three Torah seats Genesis 3:15's
  and this chapter's two; "THE SMITER" the participle with the article — the quarrel's striker (Exodus 21:19), Hadad (Genesis 36:35), David's plea (2
  Samuel 24:17), this chapter's two; the same consonants THE SMITTEN woman at 25:14, 15, 18 (the passive by the morphology) and "the blow" in Samuel and
  Kings; "struck him" five Torah seats — this chapter's four and DEUTERONOMY 21:1's "it is not known who struck him".
- 35:22-28 THE UNWITTING, THE JUDGMENT AND THE TERM: "SUDDENLY" two Bible seats, both this book's (the nazirite's 6:9, this); "without enmity",
  "without lying-in-wait", "any stone whereby he may die", "without seeing", "and he dropped it on him", "not his enemy", "seeking his harm" one seat
  each; "the congregation shall judge between the smiter and the avenger of blood" one seat, "these judgments" here and Deuteronomy 7:12; THE
  CONGREGATION-TOKEN four times (12, 24, 25, 25) — the Sifrei's "three in the section" the judgment's; "the congregation shall deliver", "from the hand
  of the avenger", "return him", "to his city of refuge where he fled" one seat each; "UNTIL THE DEATH OF THE HIGH PRIEST" 35:25, 28 and Joshua 20:6
  PLENE — THE HIGH PRIEST WRITTEN DEFECTIVE ONLY HERE (35:25, 28 twice; plene at sixteen seats, "and the high priest" at Leviticus 21:10 and 2 Kings
  12:11); "WHO WAS ANOINTED WITH THE HOLY OIL" one seat, "the anointing oil" the tabernacle's nine, ONKELOS' anointing-verb one seat in the book; "IF THE
  SLAYER GOING OUT GOES OUT" — the doubled infinitive's two Bible seats: Jacob's from Isaac (Genesis 27:30) and this; SIX doubled infinitives in the
  chapter; "the border of his city of refuge", "outside the border", "the avenger finds him" one each; "HE HAS NO BLOOD" — THE BURGLAR'S ACQUITTAL
  (Exodus 22:1, the plural; 22:2 "he has blood") at its second seat, the singular; "the land of his possession" one seat (the family six); JOSHUA 20:6
  ADDS "and come to his city and to his house".
- 35:29-34 THE STATUTE, THE WITNESSES, THE RANSOM, THE LAND: "A STATUTE OF JUDGMENT" — the phrase's two Bible seats: THE DAUGHTERS' (27:11) and this
  (Onkelos "a decree of judgment" at both); "for your generations in all your dwellings" LEVITICUS 3:17's, THE BLOOD BAN'S formula, at its second seat;
  "in all your dwellings" six seats (Leviticus 7:26 the blood again); "by the mouth of witnesses" one seat — the bare plural without a number
  (Deuteronomy's "two or three", 17:6, 19:15); "and one witness" one seat — "ONE WITNESS" A HOMOGRAPH ("not even one" of Egypt's cattle, Exodus 9:7, and
  of the drowned, 14:28; "until one" Judges 4:16, 2 Samuel 17:22; "one witness" Deuteronomy 17:6, 19:15 — the lemmas decide); inside the chapter the
  consonants are "UNTIL" four times (12, 25, 28, 32) and "witness" twice (30); "SHALL NOT TESTIFY" THE NINTH COMMANDMENT'S VERB (Exodus 20:16;
  Deuteronomy 5:20; 19:18) beside THE SIXTH'S ROOT in one verse; "you shall not take ransom" twice — the ransom-noun's four Torah seats: THE GORING OX'S
  (Exodus 21:30), THE HALF-SHEKEL'S (30:12), this chapter's two; "wicked to die" one seat; "for he shall surely die" one; "until the death of the priest"
  at 35:32 WITHOUT "great"; ONKELOS "money" for the ransom (its two seats in the book), "guilty" for "wicked"; THE POLLUTE-ROOT'S ONLY TORAH SEAT —
  35:33's two tokens; eleven Bible tokens, PSALM 106:38 "and the land was polluted with blood" among them; "AND FOR THE LAND NO ATONEMENT CAN BE MADE"
  the passive one seat — THE RANSOM'S ROOT A THIRD TIME (31, 32 the noun; 33 the verb); "except by the blood of him who shed it" Genesis 9:6's;
  DEUTERONOMY 21:8'S heifer says the other passive, "and the blood shall be atoned for them"; ONKELOS SUPPLIES "INNOCENT" (one seat in the book); "you
  shall not defile the land" — Leviticus 18:25, 27's "and the land was defiled" the kin; "IN WHOSE MIDST I DWELL" — THE BOOK'S INCLUSIO: 5:3 (the camp,
  the first law after the census) and 35:34 (the land, the last law-chapter's close) are the Torah's two seats of "I dwell in the midst"; "for I the
  LORD dwell in the midst of the children of Israel" one seat — Exodus 29:45-46's promise, 1 Kings 6:13 and Zechariah 8:3 its runs; ONKELOS "my Presence
  dwells" at both, the word's one seat in the book at 35:34.
- THE TWIN SPECS ON THE TOKENS: of the refuge law's distinct tokens (35:9-34), Joshua 20:1-9 shares 49 of its 126 — the run quoting the spec;
  Deuteronomy 19:1-13 38 of 140; Deuteronomy 21:1-9 18; Deuteronomy 4:41-43 16; Leviticus 24:17-22 12; Exodus 21:12-14 9 of 27.
- ONKELOS OVER THE BOOK: ONE WORD FOR THE REFUGE — twelve tokens for the Hebrew's eleven, the twelfth rendering "the congregation shall DELIVER" (35:25)
  with the refuge-root; ONE WORD FOR THE KILLER — seventeen with the article and one bare (35:31) for the Hebrew's twelve and six, the murderer and
  the manslayer alike; "the smiter" two; "UNWITTINGLY" the sin offering's word (15:27-29) at 35:11, 15; THE BORDER OF THE REFUGE CITY IS THE SABBATH
  LIMIT'S WORD at 35:26, 27 (the word the translation gave the borders of 34 and Sihon's, 21:13), and 35:5's two thousand cubits the limit's measure;
  ONE WORD "SPACE" for the pasture-land (35:2, 4, 5, 7) and the SIDE (34:3, 35:5); "a decree of judgment" at both statute-seats (27:11, 35:29);
  "witnesses" and "shall testify"; "in ambush" for lying-in-wait; "suddenly" the nazirite's (6:9), Miriam's (12:4) and this; "in enmity", "in hatred";
  "when he has been found guilty by the court" supplied at 19 and 21; "innocent blood" supplied at 33; "two thousand" supplied four times at 35:5 —
  THE DUAL READ; "my Presence dwells" at 34.
- THE STORE'S GLOSSES READ BACK: "dash-in-pieces" for the murderer (Strong's rendering of the root, mixed with "scattered" — by reference),
  "the-dash-in-pieces" for THE SLAYER (fourteen, every one — by gloss), "concretely" for the WITNESS (Strong's "concretely, a witness" — seventeen,
  every one), "be-the-next-of-kin" for the avenger (by reference), "in-mother" for BY THE CUBIT (seventeen, every one a cubit), "mother" for the cubit
  at 35:4 (by reference), "flit" for FLEE, "in-wink" for SUDDENLY, "in-design" for LYING-IN-WAIT, "the-stated-assemblage" for THE CONGREGATION
  (sixty-five), "and-light-upon" for "you shall appoint" (by reference), "and-cardinal-number" for AND EIGHT (the number lost from the gloss), "eye"
  for "shall testify" (by reference; the answer-verb glossed as the eye at ten Torah tokens, filed), "suburb" for the PASTURE-LAND, "cover" for the
  RANSOM (by reference), "soil" for POLLUTE, "mouth-in-a-figurative-sense" for THE SIDE (by gloss now), "seas" for the west (by reference),
  "there-suffix" for THITHER, "in-mistake" for UNWITTINGLY, "die" for "the death of" and "shall put to death" (by reference), "the-strike" for THE
  SMITER (by reference), "?" for "I", "set" for GIVE (twelve by reference), the double-hyphen "blood--of-man" family, the "asylum" family for REFUGE,
  "earth-suffix" for TO THE LAND OF, "hating" for ENEMY, "rub-with-oil" for ANOINT, "something-seized" for POSSESSION, "spill-forth" for SHED,
  "be-foul" for DEFILE, "and-snatch-away" / "and-judge" / "and-stretch" for "deliver" / "judge" / "measure" (by reference) — ONE HUNDRED AND TWO rows
  by reference and FIFTY by gloss added to the display layer's override file (each gloss family censused: every token the one word); the frozen unit
  untouched.

THE SIFREI'S OWN CASE LAW (eleven entries in MIDDOT.md): the rule about rules "we do not punish by inference" refusing the a-fortiori on the iron
(160:3 — a second instance after 157:6); the induction from three fathers (the stone, the wood, the iron — the common feature "it can kill") to
anything, and its limit (the water, the fire, the snake — "his judgment is given to Heaven", 160:5 Hebrew / 160:6); the juxtaposition disqualifying
haters and kin from the bench, carried to witnesses by the likeness of the two "kill by" clauses and an a-fortiori (160:8); the court's number built
from the congregation-tokens (ten and ten and three, 160:8); the prototype "witness means two unless 'one' is written" (161:1); the ransom refused by
the contrast of Heaven's hand with the court's (161:1); THE NOTARIKON — the verb split into two words, "it rests wrath" (161:3, E30); the a-fortiori
from the two measures (160:10); the stem read — "he will return", not "bring back" (161:5); Issi ben Akiva's two-way uncertainty (160:8 — neither death
nor exile, the TEIKU shape); the timing clause read from the context (159:1 — after inheritance and settlement). MOVE_CATALOG unchanged (known forms,
exemplars entered in the case law); MISHNAH_TOPICS unchanged (no Mishnah opened at a reading sitting — the tractates routed to the docket).

THE CLAIMS (write_ref_manifest.py → one manifest, 14 claims MS35A-01..14, every check the word's LONGEST STORE-PIECE WHOLE — the floor of four code
points refused five words whose longest piece is three letters ("suddenly", "the great", "wicked", "when he meets him", "in whose midst"), another word
of the verse chosen each time; the ID prefix asserted absent; every cite checked against the ledger's CITE INDEX (Onkelos and Sifrei rows alike); every
verse of the chapter cited by the eight span claims, asserted; six whole-chapter claims — the parser and the frames, the Sifrei's return and its
defects, the twin specs, Onkelos, the chapter's and the book's closes, the display layer): verify_claims 14 VERIFIED / 0 FAILED (from the repo root on
the manifest's path); claim_labels_census --strict GREEN (Numbers 385 labeled 385, debt 0; the labels ink with the moves named — I1, I3, I12, E30). THE
SEATS (seat_ref.py num_35_refuge_cities): 14 WITNESS_READ operators at the claims' first verses (steps 1, 5, 9, 12, 14, 16, 19, 22, 25, 29, 31, 33, 34
— thirteen steps, one carrying two), step E, the scenarios in the anchor form; verify_text GREEN (34 steps, 7 scenarios). THE RITUAL (ref_chain.sh):
every gate PASS (13 PASS) — RITUAL COMPLETE for the 210th frozen unit; the Python rendering layer written and self-proved. THE CORPUS REBAKED (predicted
before the fold: units 210, standing 2149 + 14 = 2163, hash unmoved — the tripwire's literals set to the prediction before the bake): units 210,
standing 2163, hash 8b8fff1fa28953af — the prediction matched; CORPUS TRUTH GREEN. THE STAMP: one delegated FULL RULE row (logic/findings/STAMP_LEDGER.md).
No engine file changed at this sitting — the sweep, the journal gate and the register gate stand as at 14b's close.

OWED TO THE COMPILE (sitting 15b; the box in COMPILE_DEBT.md, items (a)-(m)): THE BARE DUAL THOUSAND taught to the parser (probes to FAIL on 35:5's
four, Joshua 3:4, 7:3, Judges 20:45, 1 Samuel 13:2, 1 Kings 7:26, 2 Kings 18:23, Isaiah 36:8; the plural's 116 seats unmoved; the corpus diff read);
THE LEVITE CITIES as the law's table (48 = 6 + 42; the measure's thousand and two thousand as DATA with the exam's settings — Eruvin 51a's square,
Sotah 27b; the proportional rule by CALL to the second census's cell; Joshua 21's run outside the Torah — THE READBACK's); THE REFUGE CITIES (the six
as a DATA row — three and three, the names from Deuteronomy 4:43 and Joshua 20:7-8 outside the chapter; the appointment a debit OPEN BY DESIGN to
Joshua 20); THE MURDERER AND THE MANSLAYER — the case table (the instruments with the size clause as a PARAMETER; the manners; the intents; the
verdicts — death by the avenger, exile, neither — Issi ben Akiva's uncertainty a row); the effects (exiled, put to death, the burglar's has_blood /
no_blood reused, the avenger's license); the court of twenty-three as DATA; THE TERM — the high priest's death as a TIMER keyed to the office's holder
(Eleazar's death at Joshua 24:33 outside the Torah — the term OPEN on the tape by design; Makkot 11a's three high priests as DATA); the border-crossing
case; THE WITNESSES (two by the prototype; one for acquittal and the oath as DATA; Deuteronomy 17:6, 19:15 uncompiled — forward); NO RANSOM against
Exodus 21:30's (the ox's cell by CALL) and the fugitive's; THE LAND — polluted by blood, atoned by the shedder's blood (a status on the land; the
heifer's other passive Deuteronomy 21's — forward); "in whose midst I dwell" by REFERENCE to 5:3's camp (the naso runner's); THE EDGES the census will
demand — exodus (21:12-14 the place, 22:1-2 the burglar's blood — the O7 head's cell), lev24 (24:17 the smiter of a soul), shelach and vayikra5
(unwittingly — the sin offering's word), naso (5:3 the camp; 6:9 suddenly), second_census (26:54's rule), journeys (33:51, 54), borders (34:2; the
sides' order), zelophehad (27:11's statute of judgment), gad_reuben (the three cities beyond the Jordan in the tribes' holdings), chukat (20:22-29
Aaron's death, Eleazar's succession — the priesthood's holder), balak (23:4, 16 "met" — FALSE by sense), the primeval runner (Genesis 9:6 the blood;
3:15's enmity — FALSE by sense), bamidbar (the camp's order of the sides — REFERENCE), the tabernacle's "any instrument" (FALSE); Deuteronomy 4, 19, 21,
Joshua 20, 21 FORWARD; THE DOCKET by the union rule — Mishnah Makkot 2:1-8 with Makkot 7a-13a, Sanhedrin 1:4 with 2a-b, 9:1-2 with 76b-79a, 3:4 with
27b, 45b, Bava Kamma 4:5 with 40a-41a, Ketubot 37b, Eruvin 4:3 and 5:1-5 with 51a, Sotah 27b and 9:7, Arakhin 9:8 with 33b, Shevuot 4:1, Yoma 23a,
Megillah 29a, Yevamot 46b, the link rows for 35:2, 11, 12, 16, 19, 24, 25, 30, 31, 33; THE DISPLAY LAYER done at the reading (152 rows); the store's
"eye" for the answer-verb at nine other tokens and the mixed families ("cover", "the-strike", "and-judge", "and-stretch", "dash-in-pieces") a display
sitting's; THE CHECKPOINT PREFIX grepped before naming; THE TWO KIN PARSER READINGS filed (Ezekiel 45:2's join across "by"; Exodus 27:9's linen — the
same pointing as "six", a homograph by context, not by points).

⚠ LESSONS (10): THE SHELF'S TWO FILES HAVE TWO ROW GRAINS — assert both counts per piska; a mismatch is read row by row (a duplicated block, read as its
twins, named, never counted twice). THE ENGLISH ROW IS NOT ALWAYS THE HEBREW ROW AT THE SAME ADDRESS (160:5) — read both files at every row, and say
which file carries what. THE SLICE INDEX FROM THE PRINT, A SEVENTH INSTANCE — two slices typed one off; print the verse, then slice. THE MORPH PREFIX
AGAIN — the consecutive perfect carries the conjunction's prefix ("HC/Vqq2mp"): a filter on the verb tag's head misses it. THE SCOPE OF A PRINT IS PART
OF THE NUMBER, AGAIN — the plene "three" has twenty-four Bible seats and three in the Torah. A COUNT OF MY OWN LIST IS A MEASUREMENT — 103 typed for
102: count the literal by script. THE SHELF'S PUNCTUATION IS NOT THE QUOTATION'S — the lint reads the gloss marker right after the Hebrew, and a row's
period glued to the last token pushes it out: strip the shelf's punctuation from the cut (18 → 2 → 0 inside the writing step). A PIECE OF EIGHT
TOKENS — the cutters' seven-token cap caught two; a scan of the rows' tuples before the load is cheaper than two loads. THE BASE LEMMA CARRIES A PREFIX
— the DB's lemma column writes "c/4054" and "1350 a": a family census by the exact string undercounts; strip the prefix, keep the letter. THE CLASS
NAMED, NOT TAUGHT, AT THE READING — the bare dual measured on 26 seats and left for the compile (the fraction class's precedent at 11). THE READING
SITTING'S SHAPE HELD: dump → measure (three passes) → asserts (5 → 0) → rows (34 + 16) → writer (0 misses; lint 18 → 2 → 0 inside the step) → manifest
(14/14) → seat → ritual (13 PASS) → the fold predicted and matched.

NEXT on the ruling: THE COMPILE OF THE REFUGE CITIES (15b) on 1b's order — the measurements (the tape's state; the callees live: exodus (the burglar and
the place), lev24, shelach, vayikra5, naso, second_census, journeys, borders, zelophehad, gad_reuben, chukat (the priesthood's holder), the primeval
runner; the register gate with nothing to pay), THE DESIGN in this file before any code (the bare dual's probes; the Levite cities' table; the six
cities as data; the murderer's and the manslayer's case table with the effects; the high priest's death as a timer on the office; the witnesses; the
ransom; the land; the checkpoint prefix grepped first), the probes to FAIL (the parser's, measured), the docket by the union rule, the types, the
runner, the tape, every gate with THE REGISTER GATE --strict at the gates step, the sweep — and with it NUMBERS CLOSES (1:1-36:13 read, frozen,
compiled and on the tape, 27 and 36 by THE TENT): the next book on the owner's word.
'''

STATE = '''
═══ COMPACTION POINT #158 (2026-09-13 — written at THE NUMBERS WALK sitting 15's close; THE REFUGE CITIES 35:1-34 READ AND FROZEN — THE WALK'S LAST READING IN NUMBERS; NUMBERS 1:1-36:13 READ, 27 AND 36 BY THE TENT; 1:1-34:29 COMPILED AND ON THE TAPE; 35 NOT YET COMPILED; A CLEAN COMPACTION POINT) ═══
STATE: 210 frozen units (209 + 1), standing 2163 (2149 + 14 as predicted), hash 8b8fff1fa28953af UNMOVED; 56 runners, 61 daemons, the sweep 56/56 at 6327 UNMOVED (no runner changed); the journal gate, the register gate and the cursor probes GREEN as at 14b's close; RUN (1277, 66, 52, 0, 12, 1525, 32, 318, the four pairs, 121). LAST COMMIT a42f518; UNCOMMITTED: sittings 8 through 14b's paths, THE CLOSE LINE's, and this sitting's (logic/units/num_35_refuge_cities.yaml FROZEN; logic/oral_triage/num_35_refuge_cities_2026-09-13.md NEW; logic/oral_audit/manifests/num_35_refuge_cities_claims.json NEW; logic/py_units/num_35_refuge_cities.py NEW; logic/py_units/ALL_UNITS.py; logic/pre_logic_methods_2026-07-28/UNIT_INDEX.html; logic/corpus/CORPUS_TRUTH.py (210 / 2163); corpus_world.sqlite; logic/glosses/word_gloss_overrides.yaml (+102 by reference, +50 by gloss); logic/findings/STAMP_LEDGER.md; World/step9/NUMBERS_WALK.md ("Sitting 15"); World/step9/COMPILE_DEBT.md (the sitting-15 box); logic/MIDDOT.md (eleven entries); RESEARCH_LOG.md; THE_STEPS.md; THE_BRIEFING.md; World/RESUME.md; World/step9/forms_numbers_walk/ (this sitting's scripts copied in); the recovery file's section 16; this doc) — commit only on "commit push" (the NEVER-COMMIT set and the staging-by-exclusion form as before; ARCHITECTURE excluded).
THE SITTING (the owner: "Go" after the #157 rereads; NUMBERS_WALK.md "Sitting 15"): chapter 35 read as ONE draft (num_35_refuge_cities 35:1-34; 36 frozen at THE TENT — the walk's last reading in Numbers) from sitting 14's forms with sitting 11's Sifrei block: THE SIFREI ON NUMBERS RETURNS AT 35:9 — piskaot 159-161 found BY POSITION (the export's last three; no piska on 35:1-8), SIXTEEN rows at the English file's grain each read in both files; THE ROW-GRAIN MISMATCH MEASURED — the Hebrew 160 carries fourteen rows where the English carries ten, its last four 161:1-4 DUPLICATED (byte-near-identical: the dash character, a dropped kaf, a parenthesis), a defect class new to the walk, the four read as their twins; the rows' defects read to their verses in both files (the English 160:5 not the Hebrew 160:5 — the induction from three transposed into the English 160:6; "thirty" for twenty-three with "[27]" for the tokens' seats and the Mishnah supplied; the rule "we do not punish by inference" DROPPED by the English a second time; Deuteronomy 12:29 for 19, "Ibid. 26:3" for Numbers 36, "Exodus 11" for 21:18, "(37)" and "(38)" for 27 and 28; the Hebrew misquoting Joshua 20:7; an inserted derivation; the colophon "the book of Numbers is completed" dropped by the English); the four-form scan finding two rows of piska 1 citing the chapter (1:2 on 35:2, 1:7 on 35:34 — the book's inclusio read from its first seat), both credited. Onkelos whole (34) + the Sifrei (16) = 50 sources in one ledger (FIVE asserts fell on the first typed pass, none on the second — two slice indices (the seventh instance), a morph prefix (the consecutive perfect's conjunction), a print's scope (the plene "three"), a count of my own list; no cut miss — two eight-token pieces caught by the cutters' cap; the lint 18 → 2 → 0 inside the writing step: the shelf's punctuation stripped from the cuts); 14 claims verified 14/14 and labeled (ink with the moves named), 14 operators seated on thirteen steps, the ritual COMPLETE (13 PASS) → 210 units, standing 2163, hash unmoved (predicted); THE PARSER seven number verses read — ONE GAP: 35:5's bare dual "two thousand" four times unread (THE BARE DUAL THOUSAND: the dual at 26 Bible seats read only in a compound; bare it misses eight seats and misreads 1 Samuel 13:2 as a thousand; Onkelos supplies "two" — the class named for the compile, 4b's owed line measured); the display layer's 152 rows. THE FINDS: the four sides in the camp's order (east, south, west, north); the measure-verb's three Torah seats (the omer, the pasture-lands, the elders to the slain man — the heifer the Sifrei brings to 35:33); the refuge-word Numbers', Joshua's and Chronicles' — never Deuteronomy's; "to flee there" Lot's phrase first, "he shall flee there" Exodus 21:13's — the place become cities; Joshua 21 summing the forty-eight (13 + 10 + 13 + 12) and marking five of the six (Bezer's row bare); Joshua 21:2 quoting "cities to dwell in" under "the LORD commanded by the hand of Moses"; the second census's proportional rule at its third seat; "unwittingly" the sin offering's word, Deuteronomy's "without knowledge", Joshua 20:3 both; the iron verse without "hand" and without a size clause (Onkelos supplying it at the stone and the wood); "shall surely die" five times — the Torah's densest; the murder-root twenty times, one root for four agents, defective at every Numbers seat; "in enmity" the serpent's word; "in lying-in-wait" the noun of Exodus 21:13's verb; "suddenly" the nazirite's; Onkelos putting the court before the avenger's hand; the high priest written defective only here (Joshua 20:6 plene); "he has no blood" the burglar's clause at its second seat; "a statute of judgment" the daughters' phrase; "in all your dwellings" the blood ban's formula; the sixth and the ninth commandments' verbs in one verse, "one witness" a homograph of "not even one" and "until one"; the ransom's root three times (the goring ox's ransom the contrast; the heifer's other passive); the pollute-root's only Torah seat and Psalm 106:38's echo, R. Yoshiyah's notarikon (the word split in two); "in whose midst I dwell" — THE BOOK'S INCLUSIO (5:3, 35:34), the Sifrei's first and last piskaot reading each by the other, Onkelos supplying the Presence at both; the Hebrew's colophon. THE SIFREI'S CASE LAW: eleven entries in MIDDOT.md (the rule about rules a second time; the induction from three and its Heaven-limit; the disqualification of haters and kin carried to witnesses; the court's number from the tokens; the prototype "witness means two"; the ransom's contrast; the notarikon; the a-fortiori from the measures; the stem read; Issi ben Akiva's two-way uncertainty; the timing from the context).
THE RECORDS: NUMBERS_WALK.md "Sitting 15"; the ledger, manifest and py rendering; RESEARCH_LOG.md's entry; COMPILE_DEBT.md's sitting-15 box (a)-(m); MIDDOT.md's eleven entries; STAMP_LEDGER's row; THE_STEPS' sitting-15 paragraph; THE_BRIEFING's scoreboard bullet; the gloss override rows; World/RESUME.md; the forms copied into World/step9/forms_numbers_walk/; memory (numbers-in-order-ruling.md, MEMORY.md, step9-exam-era.md's lessons head); the recovery file's section 16; this entry.
NEXT on the ruling: SITTING 15b — THE COMPILE OF THE REFUGE CITIES on 1b's order (COMPILE_DEBT's sitting-15 box (a)-(m): the measurements first — the tape's state, the callees live (the exodus runner's burglar and place; lev24's smiter of a soul; shelach's and vayikra5's unwitting; naso's camp and the nazirite's "suddenly"; the second census's proportional rule; the journeys' 33:51, 54; the borders' 34:2; zelophehad's 27:11; gad_reuben's cities beyond the Jordan; chukat's Aaron-to-Eleazar — the priesthood's holder for the term's timer; the primeval runner's blood law), the register gate with nothing to pay; THE DESIGN in NUMBERS_WALK.md before any code — THE BARE DUAL THOUSAND's probes to FAIL (35:5 ×4, Joshua 3:4, 7:3, Judges 20:45, 1 Samuel 13:2, 1 Kings 7:26, 2 Kings 18:23, Isaiah 36:8; the plural's 116 unmoved; the corpus diff read), THE LEVITE CITIES' TABLE (48 = 6 + 42; the thousand and the two thousand as DATA with the exam's settings; the proportional rule by CALL; Joshua 21 outside the Torah — THE READBACK's), THE SIX CITIES as a DATA row and the appointment a debit OPEN BY DESIGN to Joshua 20, THE MURDERER'S AND THE MANSLAYER'S CASE TABLE (the instruments with the size clause a PARAMETER, the manners, the intents; the verdicts — the avenger's death, exile, neither; the effects: exiled, put to death, the burglar's has_blood reused, the avenger's license; the court of twenty-three as DATA), THE TERM as a TIMER on the high priest's office (Eleazar's death outside the Torah — OPEN on the tape by design; the three high priests as DATA), the border case, THE WITNESSES (two by the prototype; the one for acquittal and the oath as DATA), NO RANSOM against the ox's cell by CALL, THE LAND (a status; the heifer's passive forward; "in whose midst I dwell" by REFERENCE to 5:3), the checkpoint prefix grepped first, THE PREDICTION'S ARITHMETIC; then the probes to FAIL, the state doc's checkpoint, the docket by the union rule (Makkot 2:1-8 with 7a-13a, Sanhedrin 1:4 with 2a-b, 9:1-2 with 76b-79a, 3:4 with 27b, 45b, Bava Kamma 4:5 with 40a-41a, Ketubot 37b, Eruvin 4:3 and 5:1-5 with 51a, Sotah 27b and 9:7, Arakhin 9:8 with 33b, Shevuot 4:1, Yoma 23a, Megillah 29a, Yevamot 46b, the link rows), the types, the gates to FAIL, the runner, the recorder, the stitcher, the literals, the tape, the probe gates, the daemon and dependency gates, the journal gate, THE REGISTER GATE --strict, the sweep, the records) — AND WITH IT NUMBERS CLOSES (1:1-36:13 read, frozen, compiled and on the tape; 27 and 36 by THE TENT): the next book on the owner's word. THE LOOP QUESTION (the resident world) stays under discussion with the main thread — nothing changes on the walk until Brian's word.
POST-COMPACTION REREADS (mandatory, first sitting): the recovery file logic/pre_logic_methods_2026-07-28/RECOVERY_new_thread_2026-09-12.md whole (its section 5 THE COMPILE SITTING; its sections 15 and 16) + numbers-in-order-ruling.md + this entry + NUMBERS_WALK.md "Sitting 14b — AS BUILT" (the compile's form) + NUMBERS_WALK.md "Sitting 15" (this reading's record and the owed list) + THE_STEPS Step 2 + Step 5 + the compiler block; memory's STANDING LESSONS head (the sitting-15 paragraph first); THE_LOOP.md "Step 1's amendment — THE CLOSE LINE" before any journal or cursor work; before any word on the resident-world question, memory's the-loop-ruling.md and THE_LOOP.md's step-4 row (line 78) and its "NO SAVED STATE FILE" sentence (line 671). WATCHES: as #157's + THE SHELF'S TWO FILES HAVE TWO ROW GRAINS + THE ENGLISH ROW IS NOT ALWAYS THE HEBREW ROW AT THE SAME ADDRESS + THE SLICE INDEX FROM THE PRINT (a seventh instance) + THE MORPH PREFIX AGAIN (the consecutive perfect) + THE SHELF'S PUNCTUATION IS NOT THE QUOTATION'S + THE BASE LEMMA CARRIES A PREFIX + THE CLASS NAMED, NOT TAUGHT, AT THE READING.
'''

RESUME = '''SITTING 15 DONE 2026-09-13 (THE REFUGE CITIES 35:1-34 READ AND FROZEN — the walk's last reading in Numbers, 36 frozen at THE TENT; NUMBERS_WALK.md "Sitting 15"; the owner: "Go" after the #157 rereads): THE SIFREI ON NUMBERS RETURNS AT 35:9 — piskaot 159-161 found BY POSITION (the export's last three; no piska on 35:1-8; every head checked against its rows' own citations), sixteen rows at the English file's grain each read in both files — THE HEBREW FILE DUPLICATES A BLOCK (160:11-14 are 161:1-4 again, byte-near-identical; a defect class new to the walk), the English 160:5 is not the Hebrew 160:5 (the induction from three transposed), "thirty" for twenty-three, the rule "we do not punish by inference" dropped a second time, mistyped and inserted citations, the colophon dropped; two rows of piska 1 citing the chapter credited (1:2 on 35:2; 1:7 on 35:34 — the book's inclusio) + Onkelos whole (34) = 50 sources in one ledger (five asserts fell on the first typed pass, none on the second — two slice indices, a morph prefix, a print's scope, a count of my own list; no cut miss; the lint 18 → 2 → 0 inside the writing step — the shelf's punctuation stripped from the cuts); 14 claims verified and labeled, 14 operators seated, the ritual COMPLETE → 210 units, standing 2163, hash unmoved (predicted); THE PARSER seven number verses read, ONE GAP — THE BARE DUAL THOUSAND (35:5's "two thousand" four times unread; the dual at 26 Bible seats read only in a compound; Onkelos supplies "two"; the class named for the compile); the four sides in the camp's order; the measure-verb's three Torah seats (the omer, the pasture-lands, the elders to the slain man); the refuge-word never Deuteronomy's; Lot's "to flee there", Exodus 21:13's "he shall flee there"; Joshua 21 summing the forty-eight, Bezer's row bare; the second census's rule at its third seat; the iron verse without "hand" and without the size clause; "shall surely die" five times, the murder-root twenty — one root for four agents, defective at every Numbers seat; the serpent's "enmity"; Onkelos putting the court before the avenger; the high priest defective only here; "he has no blood" the burglar's clause; "a statute of judgment" the daughters'; the sixth and the ninth commandments' verbs in one verse; the ransom's root three times; the pollute-root's only Torah seat, Psalm 106's echo, the notarikon (the word split in two); "in whose midst I dwell" the book's inclusio (5:3, 35:34); eleven entries in MIDDOT.md; the display layer's 152 rows. NEXT: 15b — THE COMPILE OF THE REFUGE CITIES (COMPILE_DEBT's sitting-15 box (a)-(m): the bare dual taught; the Levite cities' table; the six cities as data; the murderer's and the manslayer's case table; the high priest's death as a timer on the office; the witnesses; the ransom; the land; the register gate with nothing to pay) — and with it NUMBERS CLOSES; the next book on the owner's word.
'''

STEPS = '''SITTING 15 — THE REFUGE CITIES, Numbers 35:1-34 (2026-09-13, on Brian's "Go" after the #157 rereads; World/step9/NUMBERS_WALK.md "Sitting 15"). The
chapter read as one draft — the walk's last reading in Numbers, chapter 36 already frozen at THE TENT — on Onkelos whole and THE SIFREI, WHICH RETURNS
AT 35:9 with its last three piskaot after its long silence: sixteen rows at the English file's grain, every one read in both files, and the two
files found to disagree in ways the reading had to measure — the Hebrew file repeats a block of four rows at the end of one piska before opening the
next with it, the English gives a different row at one address (the induction from three instruments moved a row down), the English says "thirty"
where the Hebrew says twenty-three, and the rule "we do not punish by inference" is dropped by the English for the second time on this walk. Every
quotation cut from the bytes by consonants in glossed pieces, no cut miss; the shelf's own punctuation had to be stripped from the cuts for the lint
to see the glosses. The parser measured first: seven number verses read, and ONE GAP — "two thousand by the cubit" four times reads nothing, because
the parser reads the dual "two thousand" only when hundreds follow; bare, before a cubit or a horse, it misses it across the Bible and once misreads
it as a thousand; Onkelos reads it, supplying "two" — the class named for the compile, an owed line from the first compile of Numbers paid by a
measurement. The finds: the Levite city's four sides run in the camp's order; the verb "you shall measure" has three Torah seats — the omer, these
pasture-lands, and the elders measuring to the slain man of the heifer rite the Sifrei brings to this chapter's last law; the refuge-word belongs to
Numbers, Joshua and Chronicles and never to Deuteronomy; "to flee there" is Lot's phrase first and "he shall flee there" is Exodus 21:13's — the
promised place become cities; Joshua 21's four lots sum to the forty-eight; the proportional rule of the second census stands here a third time;
"unwittingly" is the sin offering's word where Deuteronomy says "without knowledge" and Joshua 20 says both; the iron verse alone has no "hand" and no
size clause, which the Sifrei reads and Onkelos supplies elsewhere; "shall surely die" stands five times, the Torah's densest chapter, and the
murder-root twenty times for the murderer, the manslayer, the avenger and the court alike; "in enmity" is the serpent's word; Onkelos puts the court
before the avenger's hand; the high priest is written defective only here; "he has no blood" is the burglar's acquittal at its second seat; "a statute
of judgment" is the daughters' phrase and "in all your dwellings" the blood ban's; one verse carries the sixth and the ninth commandments' verbs; the
ransom's root stands three times — no ransom for the murderer, none for the fugitive, no atonement for the land; the pollute-root has its only Torah
seat here and Psalm 106 echoes it with the blood; and "in whose midst I dwell" closes the book's law as it opened it at 5:3 — the Sifrei's first and
last piskaot reading each by the other. Five typed facts fell on the first pass and none on the second. Fourteen claims verified, seated, the ritual
complete, the corpus rebaked to the predicted count with the hash unmoved. Next: the compile (15b) — and with it Numbers closes.

'''

BRIEF = '''- **THE REFUGE CITIES READ AND FROZEN — SITTING 15 DONE, THE WALK'S LAST READING IN NUMBERS: THE SIFREI RETURNS AND ITS TWO FILES DISAGREE, THE PARSER'S GAP ON "TWO THOUSAND" IS MEASURED AT LAST, AND THE BOOK'S LAW CLOSES ON THE WORDS IT OPENED WITH** (2026-09-13, on your "Go"; World/step9/NUMBERS_WALK.md "Sitting 15"). Chapter 35 read as one unit on Onkelos and the Sifrei's last three piskaot — sixteen rows read in both files, the Hebrew found to repeat a block and the English to swap a row and miscount a court. The parser read seven number verses and missed the bare "two thousand" four times — the dual it reads only in a compound; Onkelos reads it. "In whose midst I dwell" at 5:3 and 35:34 is the book's inclusio. Fourteen claims, the 210th frozen unit, the corpus at 2163 with the hash unmoved. Next: the compile (15b), and with it Numbers closes.
'''

DEBT = '''
## SITTING 15 — THE REFUGE CITIES' READING (2026-09-13; NUMBERS_WALK.md "Sitting 15"; logic/oral_triage/num_35_refuge_cities_2026-09-13.md; the unit
## num_35_refuge_cities FROZEN — the walk's last reading in Numbers) — OWED TO THE COMPILE (15b, on 1b's order with the register gate at the gates step):
## (a) THE BARE DUAL THOUSAND — the parser reads the dual "two thousand" (the patach, the vowel point, and the dagesh, the dot, in the pe) only when a hundreds-group follows; bare,
## before a unit noun or with the approximation prefix, it reads nothing (35:5 ×4; 1 Kings 7:26; 2 Kings 18:23; Isaiah 36:8), reads the following cubit
## as one (Joshua 3:4), is swallowed (Joshua 7:3; Judges 20:45) or misread as a thousand (1 Samuel 13:2): probes to FAIL on every one, the plural's 116
## seats unmoved, the corpus diff read verse by verse (4b's owed line "Num 35:5's two thousand cubits" PAID by the teaching); (b) THE LEVITE CITIES as
## the law's table — forty-eight = six + forty-two; the measure's thousand (35:4) and two thousand (35:5) as DATA with the exam's settings (Eruvin 51a's
## square, Sotah 27b — the Sabbath limit's measure, the Sabbath block's ledger naming the seats); the four sides in the camp's order a DATA row; the
## proportional rule by CALL to the second census's cell (26:54's rule at its third seat); Joshua 21's run outside the Torah — THE READBACK's (the
## request 21:2 quoting the spec under "by the hand of Moses"; the tally 21:41; the four lots summing to 48; Bezer's row bare); the register gate NOTHING
## TO PAY (no Num 35 seat declared; the index's two lines MEASURE-ONLY green); (c) THE SIX CITIES — a DATA row of three and three (the names from
## Deuteronomy 4:43 and Joshua 20:7-8 outside the chapter, no verdict); the appointment a debit OPEN BY DESIGN to Joshua 20 (Deuteronomy 4:41's three by
## Moses inside the Torah, uncompiled — forward); the Sifrei's "no refuge until all six are set apart" as DATA; (d) THE MURDERER AND THE MANSLAYER — the
## case table from the ink's own tokens: the instruments (iron at any size; the stone and the wood with the size clause "whereby he may die" — the size a
## PARAMETER, the Sifrei's "fills the hand" / "can kill"), the manners (thrust, threw, struck with the hand), the intents (hatred, lying-in-wait, enmity
## against suddenly, without enmity, without lying-in-wait, unseen, not his enemy nor seeking his harm); the verdicts — a murderer (death by the avenger
## after the court), a manslayer (exile), neither (Issi ben Akiva's two-way uncertainty — a TEIKU-shaped row); the effects — exiled_to_refuge, put_to_death,
## the burglar's has_blood / no_blood reused (O7's effect at its second seat), the avenger's license; the water, the fire and the snake "to Heaven" as the
## heaven entry; the court of twenty-three from the tokens as DATA (Sanhedrin 1:4); (e) THE TERM — "until the death of the high priest" a TIMER keyed to
## the office's holder (Eleazar since 20:28 — the chukat runner's succession; his death at Joshua 24:33 OUTSIDE the Torah: the term OPEN on the tape by
## design, THE READBACK's); Makkot 11a's three high priests as DATA; the anointing clause the definition (Leviticus 21:10); (f) THE BORDER CASE — the
## fugitive outside the limit, the avenger's no-blood (the burglar's clause); Onkelos's court-first clause as the exam's reading (DATA); (g) THE WITNESSES
## — "by the mouth of witnesses" two by the prototype (the Sifrei's rule — the rule itself the shelf's, Deuteronomy 17:6 and 19:15 the spec, uncompiled —
## forward); "one witness" for acquittal and for the oath as DATA (Shevuot 4:1); (h) NO RANSOM — against Exodus 21:30's ransom (the ox runner's cell by
## CALL — the Mishpatim head's kofer) for the murderer, and for the fugitive; the condemned man's liabilities as DATA (Sanhedrin 71b); (i) THE LAND —
## polluted by blood (a status on the land of Canaan), atoned only by the shedder's blood (Genesis 9:6 by REFERENCE to the primeval runner's blood law);
## the heifer's other passive (Deuteronomy 21:8 — forward, the book's own compile); "you shall not defile the land" against Leviticus 18:25-28 (the
## arayot runner — REFERENCE); "in whose midst I dwell" by REFERENCE to 5:3's camp (the naso runner's effect) — the book's inclusio a checkpoint; (j) THE
## EDGES the census will demand — exodus (21:12-14 the place to flee; 22:1-2 the burglar's blood), lev24 (24:17 the smiter of a soul), shelach / vayikra5
## (unwittingly — the sin offering's word), naso (5:3; 6:9 suddenly), second_census (26:54), journeys (33:51, 33:54), borders (34:2 the land; the sides'
## order), zelophehad (27:11 a statute of judgment), gad_reuben (32's cities beyond the Jordan), chukat (20:22-29 Aaron's death and Eleazar's robes),
## balak (23:4, 16 "met" — FALSE by sense), the primeval runner (9:6 the blood; 3:15 enmity — FALSE by sense), bamidbar (the camp's order of the sides —
## REFERENCE), the tabernacle's "any instrument" (FALSE), the erection's sides (REFERENCE); Deuteronomy 4:41-43, 19:1-13, 21:1-9, Joshua 20, 21 FORWARD —
## no link, or a labeled HYPOTHESIS; (k) THE DOCKET by the union rule — Mishnah Makkot 2:1-8 with Makkot 7a-13a (the manslayer's tractate whole),
## Sanhedrin 1:4 with 2a-b, 9:1-2 with 76b-79a, 3:4 with 27b, 45b, Bava Kamma 4:5 with 40a-41a, Ketubot 37b, Eruvin 4:3 and 5:1-5 with 51a, Sotah 27b and
## 9:7, Arakhin 9:8 with 33b, Shevuot 4:1, Yoma 23a, Megillah 29a, Yevamot 46b, the link rows for 35:2, 11, 12, 16, 19, 24, 25, 30, 31, 33; (l) THE
## DISPLAY LAYER — done at the reading (152 rows); the store's "eye" for the answer-verb at nine other Torah tokens and the mixed gloss families ("cover",
## "the-strike", "and-judge", "and-stretch", "dash-in-pieces") a display sitting's census; (m) THE TWO KIN PARSER READINGS FILED — Ezekiel 45:2's "five
## hundred by five hundred" joined to 1,000 (the preposition inside a pair of measures), Exodus 27:9's "fine twined linen" read as six (the same pointing
## as "six" — a homograph by context, the next teaching's); THE CHECKPOINT PREFIX grepped before naming (CW taken at 14b).
'''

RESEARCH = '''
## 2026-09-13 — THE REFUGE CITIES' READING (THE NUMBERS WALK sitting 15): THE SIFREI'S HEBREW FILE DUPLICATES A BLOCK; THE ENGLISH ROW IS NOT THE
## HEBREW ROW AT ONE ADDRESS; "THIRTY" FOR TWENTY-THREE; THE RULE ABOUT RULES DROPPED A SECOND TIME; THE BARE DUAL THOUSAND; THE BASE LEMMA'S PREFIX;
## THE STORE'S "EYE" FOR THE ANSWER-VERB

Numbers 35:1-34 read (logic/oral_triage/num_35_refuge_cities_2026-09-13.md; NUMBERS_WALK.md "Sitting 15"; the unit num_35_refuge_cities frozen, 210
units). Every item below is computed in the sitting's scripts (ref_ink.py's asserts; ref_measure1.py / ref_measure2.py the prints).
1. THE HEBREW FILE DUPLICATES A BLOCK. The Sifrei on Numbers export's Hebrew piska 160 carries fourteen rows where the English carries ten: its rows
   11-14 are 161:1-4 again, byte-near-identical — the dash character (U+2013 against the hyphen) the one systematic difference, 160:11 dropping the
   kaf of "whoever smites" ל מכה ("smites") for כל מכה ("whoever smites"), 161:4 alone parenthesizing its Kings citation. The English file has no such block. A new defect class
   for the export (after the mistyped heads, the translator's gaps, the verse division, the reversed frame, the dropped speaker, the supplied
   Mishnah): A DUPLICATED BLOCK across two piskaot in one file. The ledger's grain is the English's sixteen rows; the four duplicates are read as their
   twins and named; the coverage line carries both counts (16 and 20). The Hebrew 161:5 ends with the export's colophon — "the book of Numbers is
   completed; blessed is the man who trusts in the LORD" (Jeremiah 17:7's words) — absent from the English.
2. THE ENGLISH ROW IS NOT THE HEBREW ROW AT 160:5. The Hebrew 160:5 is the induction from the three instruments ("stone is not like wood, wood not like
   stone, neither like iron — the common feature: it can kill; the commandment is in the avenger's hand"); the English 160:5 is two sentences on the
   court-appointed avenger (the Hebrew's 160:7 tail, which the English 160:7 also carries), and the English 160:6 opens with the Hebrew 160:5's
   induction before its own. The address is the same, the content transposed. The class: the two files are read at every row and the ledger says
   which carries what.
3. "THIRTY" FOR TWENTY-THREE, AND "[27]". The Hebrew 160:8 closes "the expounders of the marked words said: the three 'congregations' written in the
   section teach that capital cases are by TWENTY-THREE" (בעשרים ושלשה "by twenty-three"); the English writes "adjudicated by thirty" and cites the
   tokens as "one in [24] and two in [27]" — the ink's congregation-tokens stand at 35:24, 35:25 (twice) and 35:12. The English also supplies the
   Mishnah's "acquittal is with a majority of one, and incrimination by a majority of two" where the Hebrew says "as witnesses are two, so the judges,
   and a court is not evenly balanced — add one" (the supplied-Mishnah class, Sanhedrin 1:6).
4. THE RULE ABOUT RULES DROPPED A SECOND TIME. The Hebrew 160:3: "but I can derive iron a fortiori — except that we do not punish by inference; therefore
   it says 'if with an instrument of iron ... he is a murderer', to teach that WE DO NOT PUNISH BY INFERENCE" — שאין עונשים מן הדין ("we do not punish by inference"). The English carries
   the a-fortiori and replaces the refusal with a different objection ("just as a stone must fill the hand, so iron"). Sitting 11 found the same rule
   dropped at 157:6; the class recurs — the export's English drops the meta-rule and keeps the case.
5. THE CITATIONS. 159:1's English "(Devarim 12:29)" where the Hebrew says "Deuteronomy 19" — the clause "when the LORD your God cuts off the nations"
   stands at both 12:29 and 19:1, and 19:1 opens the refuge chapter (the Hebrew's is the apt seat); its "(Ibid. 26:3)" for "at the Jordan, Jericho" where
   the Hebrew names Numbers 36 (36:13; the phrase's seven seats); 160:3's Hebrew "Exodus 11" for 21:18; 160:10's English "(37)" and "(38)" for verses 27
   and 28; 161:1's English "Whence is this derived? From 'And you shall not take ransom'" with no Hebrew counterpart; 159:1's English "viz. Shemot 21:15"
   supplied; 160:2's Hebrew misquoting Joshua 20:7 — "Kiriath-arba, that is Hebron, IN THE LAND OF CANAAN" for the ink's "in the hill country of Judah" —
   and its a-fortiori "all the more he is not exiled" dropped by the English.
6. THE BARE DUAL THOUSAND. אַלְפַּיִם "two thousand" (the patach and the dagesh in the pe, the sheva under the lamed) against אֲלָפִים "thousands" (the qamats
   under the lamed): the dual stands at 26 Bible seats, the plural at 116. The parser (cold_run_sequence.ink_numbers) reads the dual only when a
   hundreds-group follows — 4:36's 2,750, 4:40's 2,630, 7:85's 2,400, Exodus 38:29's 2,400, Ezra's and Nehemiah's rows — and misses it bare: 35:5's four
   "two thousand by the cubit" read nothing; 1 Kings 7:26's "two thousand baths", 2 Kings 18:23's and Isaiah 36:8's "two thousand horses" nothing; Joshua
   3:4's "about two thousand cubits" reads [1] (the cubit as one after the unread numeral); Joshua 7:3's and Judges 20:45's are swallowed; 1 Samuel
   13:2's "two thousand with Saul" reads 1000. The parser's own comments name the seat ("the dual, Num 35:5" at line 437; "Num 35:5's 'two thousand
   cubits'" at line 504) — the gap was known and left; sitting 1b's owed line "Num 35:5's two thousand cubits". Onkelos reads the dual, supplying תרין ("two") at all four seats. The class named for the compile (15b): the bare dual before a unit noun, with the approximation prefix, or alone.
7. TWO KIN READINGS BEYOND THE CHAPTER. Ezekiel 45:2 "five hundred by five hundred" reads [1000, 50] — the parser joins the pair across the preposition
   "by" (בְּ); Exodus 27:9 "fine twined linen" reads six — שֵׁשׁ "linen" and שֵׁשׁ "six" carry the same pointing, a homograph by context only (the
   following "twined" decides). Both filed for the parser's next teaching; neither this chapter's.
8. THE BASE LEMMA CARRIES A PREFIX. The Tanakh DB's lemma column writes the prefix with the number — "c/4054" (and-pasture-land), "l/…", "d/…" — and a
   letter for homonyms ("1350 a", "3724 a"): a census by the exact string undercounts a family (the pasture-land word's Torah seats came out three of
   six; the refuge word four of twenty). The base lemma is the string after the last slash, letter kept; the token family by substring overcounts the
   other way (Leviticus 2:16's "its grits" under the pasture-land's consonants). Both instruments printed, the base lemma the assert's.
9. THE STORE'S "EYE" FOR THE ANSWER-VERB. The snapshot store glosses the root "answer / testify" as "eye" at ten Torah tokens — Genesis 41:16 "God shall
   answer", Exodus 20:16 and Deuteronomy 5:20 "you shall not answer [as a false witness]", Exodus 23:2, 32:18's "the sound of answering", Numbers 21:17
   "sing", 35:30 "shall testify", Deuteronomy 19:18 — Strong's homonym עין ("eye") assigned to the verb ענה ("answer"). 35:30's rewritten by reference; the
   other nine filed for a display sitting. The mixed families found the same way — "cover" (the screen, the sparing, the ransom), "the-strike" (the
   smiter and the smitten woman), "and-judge" (the judging and the praying), "and-stretch" (the stretching and the measuring), "dash-in-pieces" (the
   murder-root and the scattering) — every one rewritten by reference, never by gloss.
10. THE SHELF WRITES THE MURDERER PLENE. The Sifrei's Hebrew rows write רוצח / הרוצח ("a murderer" / "the murderer") with the vav at every quotation; the ink writes רצח / הרצח ("a slayer" / "the slayer") defective at all twenty seats of the chapter, plene only at Deuteronomy 4:42, Joshua 20:3, 6 and Job 24:14 — the shelf's spelling is its own, as
   sitting 12 found for the word order.
'''

MIDDOT = '''  · WE DO NOT PUNISH BY INFERENCE, A SECOND INSTANCE (Sifrei Bamidbar 160:3 on 35:16): "if the stone and the wood make him liable, iron the more —
    except that one does not punish from an inference; therefore 'iron' is written": the a-fortiori (I1) refused on a penalty, the verse supplying what
    the inference may not — sitting 11's rule (157:6) at a second seat; the export's English drops the sentence both times.
  · THE INDUCTION FROM THREE FATHERS AND ITS LIMIT (Sifrei Bamidbar 160:5 Hebrew, 160:6 on 35:16-20): "stone is not like wood, wood not like stone,
    neither like iron, iron not like the two — the common feature: it can kill, and if he killed, the commandment is in the avenger's hand — so
    anything that can kill" (the building-block prototype from three verses, I3's form); and the same induction used to EXCLUDE — pushed into water
    or fire, a dog or a snake set on him: the three kill by the killing things themselves, so the indirect killing is not in the class, "his judgment
    is given to Heaven" — the heaven entry's own case; the English carries the induction one row down from the Hebrew.
  · THE JUXTAPOSITION THAT DISQUALIFIES, CARRIED BY A LIKENESS AND AN A-FORTIORI (Sifrei Bamidbar 160:8 on 35:23-24): "he was not his enemy" beside "the
    congregation shall judge" — haters unfit to judge (I12, the adjacent clause); kin from "between the smiter and the avenger"; and witnesses by the
    likeness of the two "kill by" clauses (kill by judges, kill by witnesses) and by I1 — judges do not decide the facts and are unfit, witnesses decide
    them, all the more.
  · THE COURT'S NUMBER FROM THE TOKENS (Sifrei Bamidbar 160:8 on 35:24-25): "the congregation shall judge", "the congregation shall deliver" — ten and
    ten (Numbers 14:27's ten spies the congregation, the exam's Sanhedrin 2a); and three more from Exodus 23:2's inclining, "as witnesses are two, so
    the judges, and a court is not even — add one": twenty-three; the Hebrew's number, the English's "thirty" a defect.
  · THE PROTOTYPE "WITNESS MEANS TWO" (Sifrei Bamidbar 161:1 on 35:30): "and one witness — this builds a father: wherever 'witness' is written, two are
    meant, unless Scripture specifies 'one'" (I3 from the specified case to the bare word); the ink's bare plural "witnesses" at 35:30 the seat.
  · THE RANSOM REFUSED BY A CONTRAST OF HANDS (Sifrei Bamidbar 161:1 on 35:31): Exodus 21:30's ransom is for a death at Heaven's hand (the ox's owner);
    "I might think the same for a death by man's hand — 'you shall not take ransom'": the verse read against its kin, the kin's setting named.
  · THE NOTARIKON ON A VERB (Sifrei Bamidbar 161:3 on 35:33): "for the blood, it pollutes (יַחֲנִיף) the land" — R. Yoshiyah splits the verb into two words,
    "it rests wrath (יחון אף) on the land": E30 (the word read as an abbreviation of two) on a verb of the ink — the exemplar beside the compile
    debt's noun (MIDDOT's sitting L4b entry).
  · THE A-FORTIORI ACROSS THE TWO MEASURES (Sifrei Bamidbar 160:10 on 35:26): R. Elazar ben Azariah — "if under the lesser measure, punishment, one step
    beyond the border forfeits the soul, how much more under the greater measure, reward": I1 with the tradition's own premise that the measure of good
    exceeds the measure of punishment (the exam's Sanhedrin 100b), the doubled infinitive "going out he goes out" the seat.
  · THE STEM READ (Sifrei Bamidbar 161:5 on 35:34): Deuteronomy 30:3 "the LORD will RETURN (וְשָׁב) with your captivity" — "'and he will bring back' is not
    written but 'and he will return'": the simple stem against the causative (the ink's form the simple, computed), the Presence read as one of the
    returning captives; the grammar of the stem as the ground of a reading (M-27's kin — the form decides).
  · THE TWO-WAY UNCERTAINTY (Sifrei Bamidbar 160:8 on 35:23): Issi ben Akiva on "without seeing ... not his enemy" — "his stringency is his leniency and
    his leniency his stringency: you cannot make him liable to death — perhaps unwitting; you cannot make him liable to exile — perhaps wilful": a
    case that no verdict reaches from the facts, carried as a row with neither (the TEIKU shape without the word).
  · THE TIMING READ FROM THE CONTEXT (Sifrei Bamidbar 159:1 on 35:10-11): "you shall appoint cities" — after inheritance and settlement, not at the entry,
    by Deuteronomy 19:1's "when the LORD your God cuts off the nations" (the refuge chapter's own opening; the English cites 12:29, the clause's other
    seat): I12, the adjacent law's timing clause read into this one; and the Jordan's status a dispute of two readings of one phrase (R. Yonatan: not
    of Canaan; R. Shimon ben Yochai: as Jericho, so the Jordan — 36:13).
'''

# ---- the memory index is sized BEFORE any record is written (the 17,000-byte limit; a failure here writes nothing) ----
mi = f'{MEM}/MEMORY.md'; s_mem = open(mi, encoding='utf-8').read()
old = [l for l in s_mem.split('\n') if l.startswith('- [⚠ NUMBERS IN ORDER FROM 1:1](numbers-in-order-ruling.md)')]
assert len(old) == 1
new = ('- [⚠ NUMBERS IN ORDER FROM 1:1](numbers-in-order-ruling.md) — OWNER-RULED 2026-09-09: the chapter walk from 1:1 at the parashah grain (map World/step9/NUMBERS_WALK.md; chapters 9, 15:32-41, 27, 36 frozen at THE TENT and SKIPPED); ⚠ OWNER-RULED 2026-09-10 READ THEN COMPILE PER PORTION, never read ahead; CHAPTER NUMBERS, not portion names. NUMBERS 1:1-34:29 READ, FROZEN, COMPILED AND ON THE TAPE (sittings 1-14b; 56 runners, 61 daemons, RUN (1277, 66, 52, 0, 12, 1525, 32, 318, four pairs, 121); THE CLOSE LINE built 2026-09-12; 14b: the four sides ONE STATUS ON THE LAND, the restatement WRITES NOTHING, the dividers a status and a debit and TWELVE POPULATION ROWS — the first register PAID BY ROWS); NUMBERS 35:1-34 READ AND FROZEN (sitting 15, 2026-09-13, #158 — THE WALK\'S LAST READING IN NUMBERS, 36 frozen at THE TENT: 210 units, standing 2163, hash 8b8fff1fa28953af unmoved; THE SIFREI RETURNS at 35:9 — its Hebrew file DUPLICATES A BLOCK (160:11-14 = 161:1-4), the English 160:5 not the Hebrew\'s, "thirty" for twenty-three, the rule "we do not punish by inference" dropped a second time; THE BARE DUAL THOUSAND — 35:5\'s "two thousand" unread four times, the class named for the compile; the book\'s inclusio "in whose midst I dwell" 5:3 / 35:34; eleven MIDDOT entries). COMMITTED a42f518 (2026-09-11); sittings 8-15 UNCOMMITTED. THE REGISTER GATE (register_census.py --strict) AT EVERY COMPILE SITTING\'S GATES STEP. NEXT: 15b — THE COMPILE OF THE REFUGE CITIES (COMPILE_DEBT\'s sitting-15 box (a)-(m): the bare dual taught; the Levite cities\' table; the six cities as data; the murderer\'s and the manslayer\'s case table; the high priest\'s death a timer on the office; the witnesses; the ransom; the land) — AND WITH IT NUMBERS CLOSES; the next book on the owner\'s word.')
s_mem = s_mem.replace(old[0], new)
assert len(s_mem.encode()) < 17000, ('MEMORY.md would be %d bytes' % len(s_mem.encode()))
nr = f'{MEM}/numbers-in-order-ruling.md'; s_nr = open(nr, encoding='utf-8').read()
old_desc = "NEXT chapter 35's reading (the refuge cities; the Sifrei returns at 35:9), then its compile."
assert s_nr.count(old_desc) == 1
s_nr = s_nr.replace(old_desc, "NUMBERS 35:1-34 READ AND FROZEN (sitting 15, 2026-09-13 — the walk's last reading in Numbers; 210 units, standing 2163, hash unmoved; the bare dual thousand named for the compile); NEXT 15b the refuge cities' compile — and with it Numbers closes; the next book on the owner's word.")

RECOVERY = '''
## 16. ADDENDUM (2026-09-13, at sitting 15's close — the state doc's COMPACTION POINT #158; this supersedes section 15's NEXT, which is kept as written)

SITTING 15 DONE: CHAPTER 35 (the refuge cities) READ AND FROZEN — THE WALK'S LAST READING IN NUMBERS (36 frozen at THE TENT) — 210 units, standing 2163,
hash 8b8fff1fa28953af unmoved; NUMBERS_WALK.md "Sitting 15" the record (THE SIFREI RETURNS at 35:9 — piskaot 159-161 by position, sixteen rows at the
English file's grain each read in both files; the Hebrew file DUPLICATES A BLOCK (160:11-14 = 161:1-4), the English 160:5 is not the Hebrew 160:5, "thirty"
for twenty-three, the rule "we do not punish by inference" dropped a second time, the citations and the colophon; two rows of piska 1 credited; the parser's
seven number verses read and ONE GAP — THE BARE DUAL THOUSAND at 35:5, the class named for the compile; the four sides in the camp's order; the measure-verb's
three Torah seats; the refuge-word never Deuteronomy's; Joshua 21 summing the forty-eight; "shall surely die" five times; the murder-root twenty, one root
for four agents; the high priest defective only here; "he has no blood" the burglar's; the sixth and the ninth commandments' verbs in one verse; the
ransom's root three times; the pollute-root's only Torah seat; the book's inclusio 5:3 / 35:34; eleven MIDDOT entries; the display layer's 152 rows);
COMPILE_DEBT.md's sitting-15 box (a)-(m) the compile's checklist. The engine, the tape, the sweep (56/56 at 6327) and every gate stand as at 14b's close.
THE FORMS of sitting 15 are in World/step9/forms_numbers_walk/ (ref_dump.py, ref_measure1.py, ref_measure2.py, ref_ink.py, ref_rows_onkelos_a.py / _b.py,
ref_rows_sifrei.py, write_ref_ledger.py, write_ref_manifest.py, seat_ref.py, ref_chain.sh, patch_overrides_ref.py, write_ref_records.py,
assert_driver.py — the reading shape WITH the Sifrei block): copy the latest to the scratchpad and adapt. Still UNCOMMITTED since a42f518; commit only on
"commit push". The loop question (a resident world against the replayed journal) stays under discussion with the main thread — nothing on the walk moves
until Brian's word.

NEXT: SITTING 15b — THE COMPILE OF THE REFUGE CITIES (35:1-34) on the compile shape of section 5, with the register gate at the gates step: the
measurements (the tape's state; the callees live — exodus (the burglar's blood, the place to flee), lev24, shelach, vayikra5, naso, second_census,
journeys, borders, zelophehad, gad_reuben, chukat (the priesthood's holder), the primeval runner; the register gate with nothing to pay), THE DESIGN in
NUMBERS_WALK.md before any code — THE BARE DUAL THOUSAND's probes to FAIL (35:5 ×4, Joshua 3:4, 7:3, Judges 20:45, 1 Samuel 13:2, 1 Kings 7:26, 2 Kings
18:23, Isaiah 36:8; the plural unmoved; the corpus diff read), THE LEVITE CITIES' TABLE (48 = 6 + 42; the measures as DATA with the exam's settings; the
proportional rule by CALL; Joshua 21 outside the Torah — THE READBACK's), THE SIX CITIES as a DATA row and the appointment a debit OPEN BY DESIGN to Joshua
20, THE MURDERER'S AND THE MANSLAYER'S CASE TABLE (the size clause a PARAMETER; the verdicts and the effects — exiled, put to death, the burglar's
has_blood reused; the court of twenty-three as DATA), THE TERM as a TIMER on the high priest's office (Eleazar's death outside the Torah — OPEN by design),
the border case, THE WITNESSES (two by the prototype), NO RANSOM against the ox's cell by CALL, THE LAND (a status; "in whose midst I dwell" by REFERENCE to
5:3), the checkpoints (the prefix grepped first), THE PREDICTION'S ARITHMETIC; then the probes to FAIL, the docket by the union rule (Makkot 2:1-8 with
7a-13a, Sanhedrin 1:4 with 2a-b, 9:1-2 with 76b-79a, 3:4 with 27b, 45b, Bava Kamma 4:5 with 40a-41a, Ketubot 37b, Eruvin 4:3 and 5:1-5 with 51a, Sotah 27b
and 9:7, Arakhin 9:8 with 33b, Shevuot 4:1, Yoma 23a, Megillah 29a, Yevamot 46b, the link rows), the types, the gates to FAIL, the runner, the recorder,
the stitcher, the literals, the tape, the probe gates, the daemon and dependency gates, the journal gate, THE REGISTER GATE --strict, the sweep, the
records — AND WITH IT NUMBERS CLOSES (1:1-36:13 read, frozen, compiled and on the tape; 27 and 36 by THE TENT): the next book on the owner's word. Before
the compile: reread NUMBERS_WALK.md "Sitting 14b — AS BUILT" (the compile's form) and "Sitting 15" (the reading and the owed list), THE_STEPS Step 2 +
Step 5 + the compiler block, memory's STANDING LESSONS head, THE_LOOP.md "Step 1's amendment — THE CLOSE LINE".
'''

append(f'{ROOT}/logic/findings/STAMP_LEDGER.md', STAMP)
append(f'{ROOT}/World/step9/NUMBERS_WALK.md', WALK)
append(f'{ROOT}/logic/pre_logic_methods_2026-07-28/PROMPT_continue_solo_era_2026-08-06.md', STATE)
append('<world-link>/RESUME.md', RESUME)
insert_before(f'{ROOT}/THE_STEPS.md', '## THE FINDINGS LOOP + THE STAMP LAW (owner-approved 2026-08-31)', STEPS)
insert_after(f'{ROOT}/THE_BRIEFING.md', '## SCOREBOARD (as of 2026-09-12, latest)\n', BRIEF)
append(f'{ROOT}/World/step9/COMPILE_DEBT.md', DEBT)
append(f'{ROOT}/RESEARCH_LOG.md', RESEARCH)
insert_before(f'{ROOT}/logic/MIDDOT.md', '## Exodus block campaign', MIDDOT)
append(f'{ROOT}/logic/pre_logic_methods_2026-07-28/RECOVERY_new_thread_2026-09-12.md', RECOVERY)

FORMS = f'{ROOT}/World/step9/forms_numbers_walk'
copied = 0
for pat in ('ref_*.py', 'ref_*.sh', 'write_ref_*.py', 'seat_ref.py', 'patch_overrides_ref.py', 'assert_driver.py'):
    for f in glob.glob(f'{SP}/{pat}'):
        shutil.copy2(f, f'{FORMS}/{os.path.basename(f)}'); copied += 1
print(f'forms copied: {copied} -> {FORMS}')

open(nr, 'w', encoding='utf-8').write(s_nr); append(nr, RESUME)
open(mi, 'w', encoding='utf-8').write(s_mem); print('MEMORY.md: the numbers line %d -> %d bytes; file %d bytes' % (len(old[0].encode()), len(new.encode()), len(s_mem.encode())))
LESSON = ('⚠ THE NUMBERS WALK sitting 15 — THE REFUGE CITIES\' READING (2026-09-13; the walk\'s last reading in Numbers): THE SHELF\'S TWO FILES HAVE TWO ROW GRAINS — assert both files\' row counts per piska; a mismatch is read row by row (the Hebrew 160 carried four rows more — 161:1-4 duplicated, read as their twins, named, never counted twice; the coverage line names both grains). THE ENGLISH ROW IS NOT ALWAYS THE HEBREW ROW AT THE SAME ADDRESS (160:5 — the induction from three transposed one row down): read both files at every row and say which carries what; "thirty" for twenty-three and the dropped rule about rules are the same reading\'s catches. THE SLICE INDEX FROM THE PRINT, A SEVENTH INSTANCE — two slices one off (Genesis 27:20, Exodus 30:12): print the verse, then slice. THE MORPH PREFIX AGAIN — the consecutive perfect carries the conjunction\'s prefix ("HC/Vqq2mp"): a filter on the verb tag\'s head ("HV") misses "you shall measure" and "you shall appoint". THE SCOPE OF A PRINT IS PART OF THE NUMBER, AGAIN — the plene "three" has twenty-four Bible seats and three in the Torah. A COUNT OF MY OWN LIST IS A MEASUREMENT — 103 typed for 102 rows: count the literal by script. THE SHELF\'S PUNCTUATION IS NOT THE QUOTATION\'S — the lint reads the gloss marker right after the Hebrew, and a row\'s period glued to the cut\'s last token pushes the marker out: strip the shelf\'s punctuation in the cutter (the lint 18 → 2 → 0 inside the writing step). A PIECE OF EIGHT TOKENS — the cutters\' seven-token cap caught two; scan the rows\' tuples by script before the load. THE BASE LEMMA CARRIES A PREFIX — the DB\'s lemma column writes "c/4054" and "1350 a": a census by the exact string undercounts a family; strip the prefix, keep the letter; the substring family overcounts the other way. THE CLASS NAMED, NOT TAUGHT, AT THE READING — the bare dual "two thousand" measured on its 26 seats and left for the compile (the fraction class\'s precedent at sitting 11). THE READING SITTING\'S SHAPE HELD WITH THE SIFREI BLOCK (dump → measure in three passes → asserts 5 → 0 → rows 34 + 16 → writer 0 misses, lint 18 → 2 → 0 inside the step → manifest 14/14 → seat → ritual 13 PASS → the fold predicted and matched); MIDDOT\'s case law entered (eleven), MOVE_CATALOG and MISHNAH_TOPICS untouched.\n')
insert_after(f'{MEM}/step9-exam-era.md', '## STANDING LESSONS AND WATCHES (moved verbatim from the MEMORY.md index line on 2026-09-07 to keep the index under its size limit; the W4/W3/W2/W1/D9/G/E lesson tail as it stood)\n', LESSON)
print('records written')
