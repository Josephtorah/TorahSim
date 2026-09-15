import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE NUMBERS WALK sitting 13 — THE JOURNEYS (2026-09-12): the records — the stamp row, NUMBERS_WALK.md "Sitting 13", the state doc's #152,
# World/RESUME.md, THE_STEPS' paragraph, THE_BRIEFING's bullet, COMPILE_DEBT's box, RESEARCH_LOG's entry, the gloss override rows, the three memory
# files, the recovery file's section 12, and the forms copied into World/step9/forms_numbers_walk/. The counts below are the tools' own prints (the
# ritual's PASS lines, the bake's hash, the truth's units), typed from them; the corpus tripwire and the ritual's print are read back before a byte is
# written. Every insert lands on a unique anchor asserted present once. MIDDOT.md, MOVE_CATALOG.md and MISHNAH_TOPICS.md UNCHANGED (no Sifrei row on
# the chapter — no case law read; no move; no Mishnah opened at a reading sitting). Sitting 12's form (write_gad_records.py).
import os, re, yaml, sqlite3, shutil, glob
ROOT = _ROOT
SP = os.path.dirname(os.path.abspath(__file__))
MEM = '<memory>'
truth = open(f'{ROOT}/logic/corpus/CORPUS_TRUTH.py', encoding='utf-8').read()
assert 'assert len(W["units"]) == 208' in truth and 'assert len(W["standing"]) == 2136' in truth and "== '8b8fff1fa28953af'" in truth, 'the fold is not the predicted one'
rit = open(f'{SP}/jou_ritual_num_33_journeys.out', encoding='utf-8').read()
assert 'RITUAL COMPLETE for num_33_journeys (208 frozen units)' in rit and rit.count('PASS ') >= 13, 'the ritual is not complete'
assert os.path.exists(f'{ROOT}/logic/oral_triage/num_33_journeys_2026-09-12.md') and os.path.exists(f'{ROOT}/logic/oral_audit/manifests/num_33_journeys_claims.json') and 'status: frozen' in open(f'{ROOT}/logic/units/num_33_journeys.yaml', encoding='utf-8').read()
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

STAMP = ('| 2026-09-12 | num_33_journeys | DELEGATED | FULL RULE | Numbers 33:1-56 derivation 2026-09-12 (THE NUMBERS WALK sitting 13 — THE JOURNEYS; the owner: "Go" after the #151 rereads, on the ruling READ THEN COMPILE; the FORTY-FIFTH NUMBERS UNIT — the portion Masei\'s first chapter as one draft, the next draft opening at 34:1): declared reading COMPLETE — Onkelos Numbers 33:1-56 whole, 56 verses fresh; the Sifrei on Numbers found BY POSITION to have NO piska on the chapter (158 on 31:22 followed by 159 on 35:9 — the shelf silent from 31:25 to 35:8, 165 verses computed at sitting 11), the whole export scanned in both files for a row citing chapter 33 with the English "Ibid." and the Hebrew gershayim (the double-stroke mark) included — ONE row of another chapter (133:3 on 27:2, citing 33:38 to date the daughters) CREDITED with a quick look, read whole at THE TENT sitting 4; no prior ledger had read a row of the chapter — grepped); coverage COMPUTED by script against the shelf\'s own counts (missing 0, extra 0); every quotation cut from the DB\'s and the shelf\'s bytes by consonants in glossed pieces of at most seven tokens (no cut miss on the writer\'s first run; gloss_lint 0 flags on the first write); the ink facts computed and asserted (fifteen failures on the first typed pass and none on the second — ten slice indices, a piska head, the parser\'s two date readers, a heading count, a plural form, a homograph — each retyped from the leg print); the engine\'s parser measured on the chapter (five number verses, every one read — 33:3 fifteen with the ordinals, 33:8 three, 33:9 twelve and seventy, 33:38 the year and month as ordinals and the day (40, 5, 1) — the tape\'s own marker at 20:28, 33:39 a hundred and twenty-three; no gap); 12 claims VERIFIED 0 FAILED (verify_claims from the repo root on the manifest\'s path; every check the word\'s longest store-piece whole), claim_labels_census --strict GREEN (Numbers 358 labeled, debt 0), 12 WITNESS_READ operators seated by script on steps 1, 3, 5, 16, 19, 36, 38, 40, 41, 50, 54, 55 with every cite checked against the ledger\'s cite index, verify_text GREEN (56 steps, 7 scenarios), freeze_ritual PASS on every gate (13 PASS — RITUAL COMPLETE, the forty-fifth frozen unit of the walk\'s count: 208 in all), the corpus rebaked once (208 units, standing 2136 = 2124 + 12 as predicted, hash 8b8fff1fa28953af unmoved), the Python rendering layer written and self-proved. Machine-administered under the 2026-09-01 delegation; labeled DELEGATED; the owner may overrule. |\n')

WALK = '''
## Sitting 13 — THE JOURNEYS, Numbers 33:1-56 (2026-09-12; the owner: "Go" after the #151 rereads, on the ruling READ THEN COMPILE): the reading and the unit

THE DRAFT: one — num_33_journeys 33:1-56 (56 of 56 verses, computed): the portion Masei's first chapter whole; the next draft, num_34_borders, opens
at 34:1 (asserted). Read in ONE pass, one ledger. The forms copied from sitting 12's scripts in World/step9/forms_numbers_walk/ and edited (jou_dump.py,
jou_measure1.py, jou_measure2.py, jou_ink.py, jou_legs.py, jou_rows_onkelos_a.py / _b.py, write_jou_ledger.py, write_jou_manifest.py, seat_jou.py,
jou_chain.sh, write_jou_records.py; every one copied into the forms folder at the close).

THE SHELF, BY POSITION (jou_ink.py's asserts): the Sifrei on Numbers has NO piska on the chapter — 158 (31:22) is followed by 159 (35:9): the shelf is
SILENT from 31:25 to 35:8 (165 verses, computed at sitting 11), and this chapter is the third stretch of that silence read on the translation alone. THE
"FOUND BY POSITION" CLAUSE run on the whole export in both files — and WIDENED: the first scan (jou_dump.py) looked for "(Bamidbar 33:n)" in the English
and a straight-quote chapter mark in the Hebrew and reported ZERO cross-citing rows; the second read the English's "(Ibid. 33:n)" and the Hebrew's
gershayim (the double-stroke mark) and found ONE — 133:3 (on 27:2) cites 33:38 to date the daughters' standing "in the fortieth year, the year Aaron
died" (the Hebrew row quotes 33:38 whole); the two other "Ibid. 33" hits are Genesis 33:4 (69:2, Esau's kiss) and Jeremiah 33:1 (151:1) — the
abbreviation's book is the row's last-named one, each read to its verse. The one row read whole at THE TENT sitting 4 (the daughters' ledger) and
CREDITED with a quick look. The chapter's own phrases elsewhere in the Hebrew rows: "with a high hand" at 112:2 is 15:30's own verse; "Kibroth-hattaavah"
at 86:1, 98:1, 136:2 is 11:34's naming; 82:1 (on 10:33, read at sitting 3) reads 21:1's Arad as the news of Aaron's death — the ink that reading stands
on is 33:38-40's own order, OBSERVED, not a row on the chapter. Onkelos 33 whole: 56. No prior ledger had read a row of the chapter; seven ledgers NAME
verses of it (Genesis's descent ledger 33:1; the tribe counts and the Levites 33:15; the trumpets 33:2, 33:8; the offerings-laws ledger 33:3; the chukat
exam 33:40; the Peor ledger 33:4): names, not reads — FRESH.

THE READING (nine modules — jou_dump.py the first measurement pass; jou_measure1.py and jou_measure2.py the second and third, printing every candidate
fact (the third because the second searched Onkelos's POINTED Aramaic for its renderings and found nothing at eleven seats — the instrument, not the
shelf: the plain form first); jou_ink.py the ink with every fact an assert (assert_driver.py: FIFTEEN failures on the first typed pass, NONE on the second
— jou_legs.py printing every failing leg, each retyped from the print: TEN slice indices (the itinerary's short verses made the indices look safe;
[2:5] typed where the print's index 2 was another word, four times over), a piska's HEAD taken for its row's verse (112 opens at 15:27; its second row
is on 15:30), the parser's TWO DATE READERS (Deuteronomy 1:3's "in forty year, in eleven month" is cardinal and reads [40, 11, 1] by the number reader;
33:38's year and month are the ordinal reader's), the heading count typed from a print that had excluded "these are the words" (63, not 62), a plural
form (Psalm 73:7's "figured" is another token than Leviticus 26:1's and 33:52's), a homograph ("their high places" is the consonants of "at their
death", Leviticus 11:31-32 — the morphology decides) — then 0) and the piece-wise cutters HP / AP; jou_rows_onkelos_a.py and _b.py the 56 rows (a
leg() helper for the plain station verses, each still carrying its computed note); write_jou_ledger.py the writer → ONE ledger
logic/oral_triage/num_33_journeys_2026-09-12.md (56 sources: Onkelos MATERIAL 56 / CONTEXT 0 — every verse of an itinerary a datum; one Sifrei row
credited; coverage computed, missing 0, extra 0; NO cut miss on the writer's first run; gloss_lint 0 on the first write).

THE INK, COMPUTED (the measurement passes FIRST, the asserts typed from the print):
- THE PARSER MEASURED FIRST (the standing rule): FIVE number verses in fifty-six, every one read — 33:3 "on the fifteenth day of the first month" [15]
  with the ordinals [1, 1]; 33:8 "a way of three days" [3]; 33:9 "twelve springs of water and seventy palm trees" [12, 70] (Exodus 15:27 the same);
  33:38 THE DATE — the year and the month as ORDINALS [40, 5] (the article-bearing numeral, rule 20 — the Torah's one seat of the form) and the day
  [1] = (40, 5, 1); 33:39 "a hundred and twenty-three years" [123]; no starred homograph, no marked token; 34:1 empty. NO GAP — the walk's second reading
  with none. THE TAPE'S OWN MARKER: Aaron's death at 20:28 (no number there) is dated on the tape from THIS chapter's 33:38 — cold_run_sequence.py reads
  its two ordinals and its number into day_in and CM2 checks (40, 5, 1): the reading's measurement equals the tape's marker. THE INK'S OWN CHECKSUM by
  the same parser: Aaron 83 at the exodus (Exodus 7:7 [80, 83]) + 40 = 123; Moses 80 + 40 = 120 (Deuteronomy 34:7); the brothers three years apart at
  both ends. THE TWO DATE FORMS: Deuteronomy 1:3's fortieth-year date is cardinal ([40, 11, 1] by the number reader) — a date checkpoint at Deuteronomy
  takes both readers.
- THE FRAMES AND THE REGISTER: NINETY-THREE narrative verbs in forty-seven verses — eighty-four the pair "journeyed" / "camped" (FORTY-TWO each) and
  nine others (Moses wrote; the camp turned back — singular, Exodus 14:2's jussive (the wish form, "let them turn back") fulfilled; passed and went; came; Aaron went up and died; the
  Canaanite heard; the LORD spoke); ONE divine frame (33:50) after forty-nine verses with none and ONE speech (33:51-56); the chapters of Numbers
  without a frame unchanged (22-24, 29, 30, 32, 36). "Journeyed" in forty-two verses (33:3, 33:5-48), "camped" in forty-two (33:5-49); forty-one with
  both, 33:3 the journey alone (the date line), 33:49 the camp alone (the last camp's extent); Onkelos keeps both counts.
- THE FORTY-TWO ON THE INK'S OWN COUNT: the departure from Rameses told TWICE (33:3 with its date, 33:5 as the itinerary's first line) and the camp in
  the plains of Moab TWICE (33:48 the arrival, 33:49 its extent "from Beth-jeshimoth to Abel-shittim") — the PLACES named are forty-two: Rameses and
  forty-one camps (thirty-three at 33:5-37, eight at 33:41-48); the departures' after-tokens forty distinct; 144 name-tokens, 108 distinct; Moseroth
  seven camps before Mount Hor by index.
- THE HEADING AND THE FRAME: "these are the journeys of the children of Israel" — 10:28 and 33:1, the same first four words; sixty-three verse-initial
  "these" headings in the Torah; "by their hosts" sixteen seats, every one in Numbers; "by the hand of Moses and Aaron" — 33:1 and Psalm 77:21, the
  phrase's two Bible seats; "AND MOSES WROTE" four Torah seats — the covenant's words, THE JOURNEYS, this Torah, this song (the tablets at Exodus 34:28
  and Deuteronomy 10:4 the verb's other two); 33:2's chiasm ("their goings out" two Bible seats, "their journeys" six — the cloud's stages); "by the mouth
  of the LORD" twenty-one Bible seats, eighteen Torah, fifteen in Numbers — Moses WROTE by it and Aaron WENT UP by it; 33:7's "mouth" Pi-hahiroth's, the
  homograph. ONKELOS "by the WORD of the LORD" at both.
- THE DATE LINE: "on the fifteenth day of the first month" the full phrase one seat; Leviticus 23:6 and 28:17 date the feast of unleavened bread "on
  the fifteenth day of THIS month" — the departure's date is the feast's; Exodus 12 gives the fourteenth at evening and "that selfsame day" — 33:3 alone
  writes the fifteenth of the going out; "THE MORROW OF THE PASSOVER" two Bible seats — 33:3 (out of Egypt) and Joshua 5:11 (the land's bread, the manna
  ceasing on the morrow): the run's two ends on one date-word; "WITH A HIGH HAND" three Torah seats (Exodus 14:8 the same going out; 15:30 — the Sifrei
  112:2's verse; 33:3), ONKELOS "with bared head" at 15:30 and 33:3 alone and the Sifrei's own gloss on 15:30 "one who bares his face" the same root;
  33:4 "Egypt was burying" (the participle's two Bible seats), "AND ON THEIR GODS THE LORD EXECUTED JUDGMENTS" one seat — THE RUN of Exodus 12:12's "I
  will execute judgments" (the future at Exodus 12:12 and Ezekiel 25:11 alone, the perfect nowhere else): Exodus narrates the firstborn and never the
  judgments on the gods — the itinerary alone records that run, forty years on. ONKELOS "on their idols" (25:2's word).
- THE STATIONS AGAINST THEIR FIRST TELLINGS, ON THE TOKENS: 33:5 opens as Exodus 12:37; 33:6 IS Exodus 13:20 with one word added; 33:7 fulfils Exodus
  14:2's jussive; 33:8 "passed through the midst of the sea" (Nehemiah 9:11 the other seat), "a way of three days in the wilderness of ETHAM" for
  Exodus 15:22's SHUR (each name one seat; "a way of three days" six Torah seats — Moses' request of Pharaoh walked after the sea); 33:9 Elim's twelve
  springs and seventy palms word for word with Exodus 15:27; 33:10 THE CAMP BY THE RED SEA, 33:12-13 DOPHKAH AND ALUSH — three stations Exodus never
  names; 33:14 Rephidim's water clause in another order (each order one seat; the defective spelling with Exodus 17:8's); 33:15 "camped in the wilderness
  of Sinai" (Exodus 19:2's singular verb beside it); 33:16-17 chapter 11's graves and Hazeroth (ONKELOS "the graves of those who demanded" at all four
  seats of the name); 33:18 RITHMAH for 12:16's "wilderness of Paran" — the spies' base under two names; Taberah no station.
- THE SEVENTEEN STATIONS 33:19-35: ELEVEN of the chapter's stations named NOWHERE ELSE in the Bible (Dophkah, Alush, Rithmah, Rissah, Kehelathah,
  Makheloth, Mithkah, Hashmonah, Abronah, Zalmonah, Punon — computed by every form's seats); THREE names only here whose consonants are common words
  (Mount Shepher — the ram's horn of Exodus 19:16; Haradah — "trembling"; Tahath — "under", a place by the morphology); Rimmon-perez shares Naaman's
  "house of Rimmon" (2 Kings 5:18), Terah carries Abraham's father's name (eleven seats), Libnah a Judah city's (nineteen); MOSEROTH, BENE-JAAKAN,
  HOR-HAGGIDGAD and JOTBATHAH are DEUTERONOMY 10:6-7's four in another order; Ezion-geber Deuteronomy 2:8's and Solomon's port. THE DEUTERONOMY
  DIVERGENCE, OBSERVED: Deuteronomy 10:6 runs "from Beeroth-bene-jaakan to Moserah; THERE AARON DIED" — the itinerary runs Moseroth then Bene-jaakan and
  puts the death at Mount Hor seven camps on; the declared shelf silent on the two orders (the Sifrei on Deuteronomy not declared).
- KADESH, MOUNT HOR, THE DEATH AND ARAD: "that is Kadesh" the identity idiom at five Bible seats (Genesis 14:7's "En-mishpat, that is Kadesh"); "in
  the edge of the land of Edom" one seat beside 20:23's "on the border" one seat; Mount Hor twelve Torah seats; ONKELOS Rekem for Kadesh at ten seats
  of Onkelos Numbers and the Hebrew's own Rekem, the Midianite king of 31:8, the eleventh; "Hor the mountain" at 33:37-41 and 34:8. 33:38-39: "in the
  fortieth year" (the article form) two Bible seats (1 Chronicles 26:31 David's); "of the going out of the children of Israel from the land of Egypt"
  three Bible seats — Exodus 19:1, 33:38, 1 Kings 6:1: THE ERA'S THREE STAMPS in that form; "in the fifth month" the Torah's one seat; "at his death"
  two Bible seats — Aaron's and Moses'. 33:40: "and the Canaanite king of Arad heard" — 21:1 and this; the itinerary keeps the hearing and drops the war,
  the captives, the vow and Hormah, adds "in the land of Canaan"; its place right after the death — the Sifrei's 82:1 reads 21:1 so.
- THE LAST STATIONS AGAINST CHAPTER 21: Zalmonah and Punon named here alone (21:4 names no camp before Oboth); Oboth and Iye-abarim 21:10-11's; of
  chapter 21's stations after Iye-abarim (the Zered, the Arnon, Beer, Mattanah, Nahaliel, Bamoth, the valley of Pisgah) NOT ONE is in the itinerary, and
  its Dibon-gad, Almon-diblathaim and the mountains of Abarim are not in 21 — the two lists share Oboth, Iye-abarim and Moab's name alone (the
  name-tokens intersected); DIBON-GAD — Gad built Dibon (32:34), the itinerary's witness to chapter 32; Almon-diblathaim Jeremiah 48:22's
  Beth-diblathaim; "the MOUNTAINS of Abarim before Nebo" (plural) beside 27:12's "the mountain of Abarim"; "the plains of Moab" eight Torah seats, "by
  the Jordan at Jericho" seven; Beth-jeshimoth Reuben's (Joshua 13:20) and Moab's (Ezekiel 25:9), Abel-shittim one seat, Shittim Peor's, the spies' and
  the crossing's, Micah's. ONKELOS "the plains" one word at eight seats, "the plain of Shittim", "the fords of the Abarim".
- THE COMMAND (33:50-56): the frame's two seats (33:50, 35:1); "when you pass over the Jordan" 33:51, 35:10, Deuteronomy 11:31; "drive out all the
  inhabitants of the land" one seat (Exodus 23:31's promise its kin); "their FIGURED STONES" Leviticus 26:1's word; "their MOLTEN IMAGES" one seat (the
  calf's word; "from Succoth" the consonantal look-alike); "their HIGH PLACES you shall DEMOLISH" — Leviticus 26:30's curse in the same verb on the same
  object; the other iconoclasm commands (Exodus 23:24, 34:13, Deuteronomy 7:5, 12:2-3) name altars, pillars, asherim and graven images — 33:52's three
  are its own; 33:53 "dwell in it" Deuteronomy 11:31's, "to possess it" Leviticus 20:24's, ONKELOS supplying "the inhabitants" where the Hebrew has "the
  land"; 33:54 IS 26:52-56 RESTATED TO THE PEOPLE with the first verb turned plural and the second left singular — the number switching inside the verse
  (computed on the morphology; Onkelos makes both plural); "by lot" four Torah seats; "to whom the lot goes out, his it shall be" one; "by the tribes of
  your fathers" one; 33:55 THE NEGATIVE ARM — "thorns in your eyes and pricks in your sides" run back REVERSED by Joshua 23:13 ("scourges in your sides
  and pricks in your eyes"), Judges 2:3 "for sides"; "leave over" the Passover's verb (Exodus 12:10); "harass" 25:18's Midian word; ONKELOS reads the
  figure as "bands taking up arms against you and camps surrounding you"; 33:56 "as I thought" Isaiah 14:24's, ONKELOS "as I planned".
- THE STORE'S GLOSSES READ BACK: "and-grave" (wrote), "the-pretermission" (the Passover), "be-high-actively", "sentence" (judgments), "eye" (springs),
  "in-cord" (the border), "and-wander-away" (destroy), "figure" / "pouring-over" / "elevation", "desolate" (demolish), "in-pebble" (by lot), "jut-over"
  (leave over), "to-brier", "and-cramp" (harass), "compare" (thought), and the "?" at Pi-, Baal-, Kibroth-, Beth- and Abel- — twenty-one rows added to
  the display layer's override file by reference; the frozen unit untouched.

THE SIFREI'S OWN CASE LAW: none — no row of the spine on the chapter (MIDDOT.md unchanged; MOVE_CATALOG unchanged). The one credited row carries one
dating clause.

THE CLAIMS (write_jou_manifest.py → one manifest, 12 claims MS33A-01..12, every check the word's LONGEST STORE-PIECE WHOLE; the ID prefix asserted
absent; every cite checked against the ledger's CITE INDEX; every verse of the chapter cited by some claim, asserted): verify_claims 12 VERIFIED / 0
FAILED (from the repo root on the manifest's path); claim_labels_census --strict GREEN (Numbers 358 labeled 358, debt 0; every label ink). THE SEATS
(seat_jou.py num_33_journeys): 12 WITNESS_READ operators at the claims' first verses (steps 1, 3, 5, 16, 19, 36, 38, 40, 41, 50, 54, 55), step E, the
scenarios in the anchor form; verify_text GREEN (56 steps, 7 scenarios). THE RITUAL (jou_chain.sh): every gate PASS (13 PASS) — RITUAL COMPLETE for the
208th frozen unit; the Python rendering layer written and self-proved. THE CORPUS REBAKED (predicted before the fold: units 208, standing 2124 + 12 =
2136, hash unmoved — the tripwire's literals set to the prediction before the bake): units 208, standing 2136, hash 8b8fff1fa28953af — the prediction
matched; CORPUS TRUTH GREEN. THE STAMP: one delegated FULL RULE row (logic/findings/STAMP_LEDGER.md). No engine file changed at this sitting — the
sweep, the journal gate and the register gate stand as at 12b's close.

OWED TO THE COMPILE (sitting 13b; the box in COMPILE_DEBT.md, items (a)-(n)): THE STATIONS — as a data LIST or as tape lines (the design's question: the
dated stations are already markers on the tape — Rameses, Sin, Sinai, Kibroth-hattaavah, Hazeroth, Paran, Kadesh, Mount Hor, Oboth, the plains of Moab
— and a retelling must not write an act a second time; the eleven unnamed-elsewhere stations, the Red Sea camp, Dophkah, Alush, Rithmah, Zalmonah and
Punon the itinerary's own); 33:2 Moses' writing as an act (the four writings — Exodus 24:4's on the tape?); 33:3-4 THE RUN OF EXODUS 12:12 — the
judgments on the gods closed BY VALUE at 33:4 if the exodus story's spec left a debit open (a Torah-closed debit forty years on, the crown to look for);
33:38-39 the checkpoint — the itinerary's date against the tape's marker (40, 5, 1), Aaron's 123 against Exodus 7:7's 83 on the ledger; 33:40 Arad a
RUN_CITATION of the chukat runner's line; THE COMMAND 33:50-56 in the divine voice — a daemon given_at 33:50 installed_by the verse: the dispossession a
DEBIT on Israel OPEN BY DESIGN (its runs Joshua's — THE READBACK's class), the iconoclasm's three objects (the figured stone by CALL into Leviticus 26:1's
runner; the molten image the calf's word; the high places against Leviticus 26:30's curse effect), the lot by CALL into the second census's cell (VIA),
the negative arm a DATA row with Joshua 23:13 and Judges 2:3 as run citations; the register gate's seats — "by the mouth of the LORD" at 33:2 and 33:38
(the cloud's and the census's receipt formula: measured at the compile's measurements step); the Deuteronomy divergence a DATA row (the two orders);
the edges the census will demand — exodus_story (12:37, 13:20, 14:2, 15:22-27, 16:1, 17:1, 19:2), beha (10:12, 11:34-35, 12:16), shelach, chukat (20:1,
22-29; 21:1-11), balak (22:1, 25:1), second_census (26:52-56), zelophehad (27:12), gad_reuben (32:34), tochacha (Leviticus 26:1, 30), holiness (19:4), the
calf's runner (Exodus 32:4); Deuteronomy 10:6-7, Joshua 5:10-12, 23:13, Judges 2:3 forward; the docket by the union rule (Rosh Hashanah 2b-3a — Arad
heard of Aaron's death, the first of Av; Kiddushin 37b-38a — the morrow of the Passover and the manna's ceasing; Bava Batra 117a-122a credited; Megillah
22b the figured stone; Zevachim 112b-119b the high places' eras; the local shelf scanned for the forty-two); no parser rule owed; the DATE READER'S two
forms noted for Deuteronomy's checkpoints.

⚠ LESSONS (8): THE CITATION SCANNER READS THE EXPORT'S ABBREVIATION AND ITS MARKS — "(Bamidbar 33:n)" and a straight-quote chapter mark found ZERO rows;
"(Ibid. 33:n)" and the gershayim found the one that is there (133:3): a report of zero is worth its coverage line, and the coverage line must name the
forms scanned. THE POINTED TEXT IS NOT THE PLAIN — Onkelos's renderings searched on the pointed Aramaic returned nothing at eleven seats; strip the
points, then search (the same lesson as the shelf's search, now on the translation). TEN SLICE INDICES IN FIFTEEN FALLS — the fifth instance, and the
worst: the itinerary's short verses made the indices look safe; print the verse, then slice, whatever the verse's length. A PISKA'S HEAD IS ITS FIRST
ROW'S CITATION, NOT THE ROW'S VERSE — 112 opens at 15:27 and its second row is on 15:30. THE TWO DATE FORMS HAVE TWO READERS — 33:38's article-bearing
year and month are the ordinal reader's, Deuteronomy 1:3's cardinal date the number reader's: a date checkpoint takes both. A HOMOGRAPH PLURAL IS
ANOTHER TOKEN (Psalm 73:7's "figured" is not 33:52's form); "THEIR HIGH PLACES" IS THE CONSONANTS OF "AT THEIR DEATH" — the morphology decides. THE
READING SITTING'S SHAPE HELD: dump → measure (three passes) → asserts (15 → 0) → rows → writer (0 misses; lint 0 first write) → manifest (12/12) → seat →
ritual (13 PASS) → the fold predicted and matched.

NEXT on the ruling: THE COMPILE OF THE JOURNEYS (13b) on 1b's order — the measurements (the tape's state; the callees live: exodus_story, beha, shelach,
chukat, balak, second_census, zelophehad, gad_reuben, tochacha, holiness; the register gate's seats in the chapter at 33:2 and 33:38), THE DESIGN in this
file before any code (the stations as a list or as lines; the run of Exodus 12:12 closed by value; the command's daemon and its open debit; the lot by
CALL; the negative arm as data), the probes to FAIL, the docket by the union rule, the types, the runner, the tape, every gate with THE REGISTER GATE
--strict at the gates step, the sweep — before chapter 34, never the next reading first.
'''

STATE = '''
═══ COMPACTION POINT #152 (2026-09-12 — written at THE NUMBERS WALK sitting 13's close; THE JOURNEYS 33:1-56 READ AND FROZEN; NUMBERS 1:1-33:56 READ, 27 BY THE TENT; 1:1-32:42 COMPILED AND ON THE TAPE; 33 NOT YET COMPILED; A CLEAN COMPACTION POINT) ═══
STATE: 208 frozen units (207 + 1), standing 2136 (2124 + 12 as predicted), hash 8b8fff1fa28953af UNMOVED; 54 runners, 59 daemons, the sweep 54/54 at 6218 UNMOVED (no runner changed); the journal gate, the register gate and the cursor probes GREEN as at 12b's close; RUN (1271, 66, 52, 0, 12, 1518, 30, 318, the four pairs, 121). LAST COMMIT a42f518; UNCOMMITTED: sittings 8 through 12b's paths, THE CLOSE LINE's, and this sitting's (logic/units/num_33_journeys.yaml frozen; logic/oral_triage/num_33_journeys_2026-09-12.md NEW; logic/oral_audit/manifests/num_33_journeys_claims.json NEW; logic/py_units/num_33_journeys.py NEW + ALL_UNITS.py; the html page and the indexes; logic/corpus/CORPUS_TRUTH.py (208, 2136); logic/glosses/word_gloss_overrides.yaml (the chapter's twenty-one rows); STAMP_LEDGER.md; NUMBERS_WALK.md; COMPILE_DEBT.md; RESEARCH_LOG.md; THE_STEPS.md; THE_BRIEFING.md; World/RESUME.md; World/step9/forms_numbers_walk/ (this sitting's scripts copied in); the recovery file's section 12; this doc) — commit only on "commit push" (the NEVER-COMMIT set and the staging-by-exclusion form as before; ARCHITECTURE excluded).
THE SITTING (the owner: "Go" after the #151 rereads; NUMBERS_WALK.md "Sitting 13"): chapter 33 read as ONE draft (num_33_journeys 33:1-56; 34:1 the next draft's) from sitting 12's forms: the Sifrei on Numbers found BY POSITION to have NO piska on the chapter (158 on 31:22 followed by 159 on 35:9; the whole export scanned in both files — the first scan reported ZERO cross-citing rows and the scan WIDENED to the English "Ibid." and the Hebrew gershayim found ONE, 133:3 on 27:2 citing 33:38 to date the daughters, credited with a quick look, read whole at THE TENT sitting 4) + Onkelos whole (56) = 56 sources in one ledger (nine modules; FIFTEEN asserts fell on the first typed pass and none on the second — ten slice indices, a piska head taken for its row's verse, the parser's two date readers, a heading count, a plural form, a homograph — retyped from the leg print; no cut miss; lint 0 on the first write); 12 claims MS33A verified 12/12 and labeled (Numbers 358, debt 0), 12 operators seated, the ritual COMPLETE (13 PASS; the 208th unit), the corpus rebaked once (208, 2136, hash unmoved — predicted); THE PARSER MEASURED FIRST — five number verses, every one read (33:3 [15] with the ordinals [1, 1], 33:8 [3], 33:9 [12, 70], 33:38 the ordinals [40, 5] and the day [1] = (40, 5, 1) — THE TAPE'S OWN MARKER AT 20:28 IS BUILT FROM THIS VERSE, 33:39 [123] = Exodus 7:7's 83 + 40); NO GAP; THE CROWNS — the forty-two on the ink's own count (forty-two "journeyed" and forty-two "camped", the first departure and the last camp each told twice: forty-two places, Rameses and forty-one camps), the Torah's one full death-date and the era's three stamps in one form (Exodus 19:1, 33:38, 1 Kings 6:1), the ink's checksum on the brothers' ages, the run of Exodus 12:12's judgments on the gods recorded only here, the morrow of the Passover at both ends of the run (33:3, Joshua 5:11), eleven stations named nowhere else and three common-word names, the stations retelling their first tellings on the tokens (33:6 = Exodus 13:20 + one word; Etham for Shur; Rithmah for Paran; the Red Sea camp, Dophkah and Alush unnamed in Exodus), Deuteronomy 10:6-7's four in another order with Aaron's death placed at Moserah (OBSERVED, the shelf silent), 33:54 restating 26:52-56 with the verb's number switching inside the verse, 33:52's three objects with Leviticus 26:30's curse on the third, the negative arm run back reversed by Joshua 23:13 and read by Onkelos as armed bands, Onkelos's Rekem at ten seats and the Midianite king Rekem the Hebrew's own; the store's twenty-one glosses overridden by reference.
THE RECORDS: NUMBERS_WALK.md "Sitting 13"; the ledger, manifest and py rendering; RESEARCH_LOG.md's entry; COMPILE_DEBT.md's sitting-13 box (a)-(n); STAMP_LEDGER's row; THE_STEPS' sitting-13 paragraph; THE_BRIEFING's scoreboard bullet; the gloss override rows; World/RESUME.md; the forms copied into World/step9/forms_numbers_walk/; memory (numbers-in-order-ruling.md, MEMORY.md, step9-exam-era.md's lessons head); the recovery file's section 12; this entry. MIDDOT, MOVE_CATALOG and MISHNAH_TOPICS unchanged.
NEXT on the ruling: SITTING 13b — THE COMPILE OF THE JOURNEYS on 1b's order (COMPILE_DEBT's sitting-13 box (a)-(n): the measurements first — the tape's state and its markers at the dated stations, the callees live (the exodus story's 12:12 spec and 12:37, 13:20, 14:2, 15:22-27, 16:1, 17:1, 19:2 lines; beha's 10:12, 11:34-35, 12:16; shelach's; chukat's 20:1, 20:22-29, 21:1-11; balak's 22:1, 25:1; the second census's 26:52-56 by_lot cell; zelophehad's 27:12; gad_reuben's 32:34; the tochacha's Leviticus 26:1 and 26:30 effects; the calf's molten word), the register gate's seats in the chapter measured (33:2, 33:38 "by the mouth of the LORD"); THE DESIGN in NUMBERS_WALK.md before any code — THE STATIONS' SHAPE (a data list of forty-two places with their first tellings and run citations, or tape lines for the itinerary's own stations, the dated ones already markers — a retelling never writes an act twice), THE RUN OF EXODUS 12:12 closed by value at 33:4 if a debit stands open, THE DATE CHECKPOINT (33:38 against the marker at 20:28; 33:39 against Exodus 7:7 on the ledger), THE COMMAND'S DAEMON (given_at 33:50, installed_by the verse — the divine voice: the dispossession a debit on Israel OPEN BY DESIGN to Joshua's runs, the three objects' bans, the lot by CALL, the negative arm as data), the checkpoints CZ1-CZ9 (the prefix grepped first), THE PREDICTION'S ARITHMETIC; then the probes to FAIL (a measured zero if no rule is owed), the docket by the union rule (Rosh Hashanah 2b-3a, Kiddushin 37b-38a, Megillah 22b, Zevachim 112b-119b, Bava Batra 117a-122a credited, the link rows), the types, the gates to FAIL, the runner (the runner measure first), the recorder, the stitcher, the literals, the tape (10/10), the probe gates, the daemon and dependency gates, the journal gate, THE REGISTER GATE --strict, the sweep, the records — THEN CHAPTER 34 (the borders' reading, 34:1-29; the Sifrei silent to 35:8; the parser measured on 34:13's nine and 34:15's two) — NEVER THE NEXT READING FIRST.
POST-COMPACTION REREADS (mandatory, first sitting): the recovery file logic/pre_logic_methods_2026-07-28/RECOVERY_new_thread_2026-09-12.md whole (its section 5 THE COMPILE SITTING; its sections 11 and 12) + numbers-in-order-ruling.md + this entry + NUMBERS_WALK.md "Sitting 12b — AS BUILT" (the compile's form) + NUMBERS_WALK.md "Sitting 13" (this reading's record and the owed list) + THE_STEPS Step 2 + Step 5 + the compiler block; memory's STANDING LESSONS head (the sitting-13 paragraph first); THE_LOOP.md "Step 1's amendment — THE CLOSE LINE" before any journal or cursor work; at the types step: daemon_dispositions.yaml's installed_by values. WATCHES: as #151's + THE CITATION SCANNER READS THE ABBREVIATION AND THE MARKS (a zero is worth its coverage line) + THE POINTED TEXT IS NOT THE PLAIN (strip, then search) + THE SLICE INDEX FROM THE PRINT, A FIFTH INSTANCE + A PISKA'S HEAD IS ITS FIRST ROW'S CITATION + THE TWO DATE FORMS HAVE TWO READERS + THE FORMS COPIED, NEVER RETYPED FROM MEMORY.
'''

RESUME = '''SITTING 13 DONE 2026-09-12 (THE JOURNEYS 33:1-56 READ AND FROZEN; NUMBERS_WALK.md "Sitting 13"; the owner: "Go" after the #151 rereads): the Sifrei on Numbers found BY POSITION to have no piska on the chapter (the shelf silent 31:25-35:8; the cross-citing scan WIDENED to the English "Ibid." and the Hebrew gershayim after a first scan reported zero — one row of another chapter, 133:3 citing 33:38, credited with a quick look) + Onkelos whole (56) = 56 sources in one ledger (fifteen asserts fell on the first typed pass, none on the second — ten slice indices, a piska head, the two date readers, a heading count, a plural form, a homograph; no cut miss; lint 0 first write); 12 claims verified and labeled, 12 operators seated, the ritual COMPLETE → 208 units, standing 2136, hash unmoved (predicted); THE PARSER five number verses, every one read — 33:38's date (40, 5, 1) THE TAPE'S OWN MARKER AT 20:28, 33:39's 123 = Exodus 7:7's 83 + 40; NO GAP; THE FORTY-TWO ON THE INK'S OWN COUNT (forty-two "journeyed", forty-two "camped", Rameses and the plains of Moab each told twice — forty-two places); the Torah's one full death-date and the era's three stamps (Exodus 19:1, 33:38, 1 Kings 6:1); the run of Exodus 12:12's judgments on the gods recorded only here; the morrow of the Passover at both ends (33:3, Joshua 5:11); eleven stations named nowhere else; the stations retelling Exodus on the tokens (33:6 = Exodus 13:20 + one word; Etham for Shur; Rithmah for Paran); Deuteronomy 10:6-7's order and Moserah OBSERVED; 33:54 restating 26:52-56 with the verb's number switching; 33:52's three objects and Leviticus 26:30's curse; the negative arm reversed by Joshua 23:13, Onkelos's armed bands; Rekem at ten seats and the Midianite king. NEXT: 13b — THE COMPILE OF THE JOURNEYS (COMPILE_DEBT's sitting-13 box (a)-(n); the stations as a list or as lines; the run of Exodus 12:12 closed by value; the command's daemon and its open debit; the register gate at the gates step), THEN chapter 34 — never the next reading first.
'''

STEPS = '''SITTING 13 — THE JOURNEYS, Numbers 33:1-56 (2026-09-12, on Brian's "Go" after the #151 rereads; World/step9/NUMBERS_WALK.md "Sitting 13"). The
chapter read as one draft (34:1 the next draft's) on Onkelos whole — the Sifrei on Numbers has no piska on it, found by position, and the whole export
was scanned for any row citing the chapter: a first scan reported zero, and a scan widened to the English "Ibid." and the Hebrew double-stroke mark found
the one that is there (133:3 dating the daughters by 33:38), credited with a quick look — a report of zero is worth its coverage line, and the line must
name the forms scanned. Every quotation cut from the bytes by consonants in glossed pieces, no cut miss, the lint clean on the first write. The parser
measured first: five number verses, every one read, no gap — and 33:38's date, read as the fortieth year, the fifth month, the first of the month, is
the very verse the tape already reads to place Aaron's death at 20:28: the reading's measurement equals the tape's marker. The finds: the chapter counts
forty-two "journeyed" and forty-two "camped" because the first departure and the last camp are each told twice, so the places are forty-two — Rameses and
forty-one camps; Aaron's hundred and twenty-three is Exodus 7:7's eighty-three plus forty, Moses' hundred and twenty is eighty plus forty, the brothers
three years apart at both ends; "on their gods the LORD executed judgments" (33:4) is the only place the Torah records the run of Exodus 12:12's promise;
"the morrow of the Passover" stands twice in the Bible — out of Egypt here, into the land's bread at Joshua 5:11; eleven stations are named nowhere else;
the stations retell Exodus word for word with small changes (33:6 is Exodus 13:20 plus one word; Etham for Shur; Rithmah for Paran); Deuteronomy 10:6-7
runs two stations in the other order and puts Aaron's death at Moserah — observed, the shelf silent; 33:54 restates the lot's rule of chapter 26 with the
verb's number switching inside the verse; 33:52's "you shall demolish their high places" is Leviticus 26:30's curse in the same verb; and 33:55's thorns
and pricks come back reversed at Joshua 23:13, which Onkelos reads as armed bands and surrounding camps. Fifteen typed facts fell on the first pass (ten
of them slice indices — the fifth instance of the lesson) and none on the second. Twelve claims verified, seated, the ritual complete, the corpus rebaked
to the predicted count with the hash unmoved. Next: the compile (13b), then chapter 34 — never the next reading first.

'''

BRIEF = '''- **THE JOURNEYS READ AND FROZEN — SITTING 13 DONE: THE CHAPTER COUNTS ITS FORTY-TWO ON ITS OWN VERBS, AARON'S DEATH-DATE IS THE VERSE THE TAPE ALREADY READS, THE JUDGMENTS ON EGYPT'S GODS ARE RECORDED ONLY HERE, AND THE STATIONS RETELL EXODUS WORD FOR WORD WITH SMALL CHANGES** (2026-09-12, on your "Go"; World/step9/NUMBERS_WALK.md "Sitting 13"). Chapter 33 read as one unit on Onkelos whole — the Sifrei has no row on it, proved by position; the scan for rows citing it was widened after a first pass reported zero, and found the one row that dates the daughters by Aaron's death (56 sources, one ledger, no cut miss, the lint clean first write). The parser: five number verses, every one read, no gap — 33:38's date is (40, 5, 1), the tape's own marker for 20:28. The finds: forty-two "journeyed" and forty-two "camped" — the first departure and the last camp each told twice, so forty-two places; Aaron's 123 = 83 + 40 and Moses' 120 = 80 + 40; "on their gods the LORD executed judgments" the run of Exodus 12:12 nowhere else; "the morrow of the Passover" out of Egypt here and into the land's bread at Joshua 5:11; eleven stations named nowhere else; 33:6 is Exodus 13:20 plus one word, Etham for Shur, Rithmah for Paran; Deuteronomy 10 runs two stations the other way and puts the death at Moserah (observed); 33:54 restates the lot's rule with the verb's number switching; the high places' demolition is Leviticus 26:30's curse in the same verb; the thorns and pricks come back reversed in Joshua 23:13. Twelve claims verified and seated, the ritual complete, 208 units, standing 2136, the hash unmoved. Next: the compile, then chapter 34.
'''

DEBT = '''
## SITTING 13 — THE JOURNEYS' READING (2026-09-12; NUMBERS_WALK.md "Sitting 13"; logic/oral_triage/num_33_journeys_2026-09-12.md; the unit
## num_33_journeys FROZEN) — OWED TO THE COMPILE (13b, on 1b's order with the register gate at the gates step): (a) THE STATIONS' SHAPE — the design's
## question: a DATA LIST of the forty-two places (Rameses and forty-one camps, each with its first telling's verse and its run citations — the dated
## stations are ALREADY MARKERS on the tape: Rameses / Succoth (Exodus 12:37), Sin (16:1), Sinai (19:1), Kibroth-hattaavah and Hazeroth (11:34-35), Paran
## (12:16), Kadesh (20:1), Mount Hor (20:22), Oboth and Iye-abarim (21:10-11), the plains of Moab (22:1)), or tape lines for the itinerary's OWN stations
## (the eleven named nowhere else, the Red Sea camp, Dophkah, Alush, Rithmah, Zalmonah, Punon) — a RETELLING NEVER WRITES AN ACT TWICE (the tape's lines
## for chapter 33 page_order at (40, 6, 1) after chapter 32's twelve, no new marker unless the design places one); (b) 33:2 MOSES WROTE — an act (the
## four writings: Exodus 24:4's on the tape at the covenant? measured); (c) THE RUN OF EXODUS 12:12 — "on their gods the LORD executed judgments" (33:4):
## if the exodus story's spec (12:12 "I will execute judgments") left a DEBIT open on Heaven's docket, 33:4 closes it BY VALUE forty years on (the crown to
## look for at the measurements); 33:3's date a dated retelling of the exodus marker (the fifteenth of the first month — the tape's own day, checked);
## (d) 33:38-39 THE DATE CHECKPOINT — the itinerary's (40, 5, 1) against the tape's marker at 20:28 (built from this verse — the compile asserts the
## identity from the tape's side); Aaron's 123 against Exodus 7:7's 83 on the ledger (+ 40 by the era) and Moses' 120; (e) 33:40 ARAD a RUN_CITATION of
## the chukat runner's line at (40, 5, 1) (taken_captive) — the hearing alone; Rosh Hashanah 2b-3a's reading (the news of Aaron's death) the docket's;
## (f) THE COMMAND 33:50-56 — a law in the DIVINE voice (given_at 33:50, installed_by the verse — the first daemon of the walk since 30:2's class that is
## NOT in Moses' voice): the dispossession a DEBIT on israel_people (commanded: drive out the inhabitants) OPEN BY DESIGN — its runs Joshua's (the
## Jabesh-gilead class again, THE READBACK's item), Joshua 23:13 and Judges 2:3 the negative arm's runs; the iconoclasm's THREE OBJECTS — the figured stone
## by CALL into the runner that compiled Leviticus 26:1 (the tochacha's or the behar's — measured), the molten image the calf's word (Exodus 32:4's runner),
## the high places against Leviticus 26:30's curse EFFECT (the same verb — a spec/curse pair on one object); "possess the land and dwell in it" a status;
## (g) THE LOT by CALL into the second census's cell (C2.the_land('by_lot') — VIA second_census as at 32:18) — 33:54's restatement with the verb's number
## switching a DATA row; (h) THE NEGATIVE ARM (33:55-56) a DATA row (the outcome "thorns in your eyes and pricks in your sides"; "as I thought to do to
## them" — Isaiah 14:24's phrase) with no verdict on the tape; (i) THE REGISTER GATE — "by the mouth of the LORD" at 33:2 and 33:38 (the cloud's and the
## census's receipt class of chapters 3-4 and 9): the gate's seats in 33 measured at the compile's measurements step, declared from the print; no count
## line, no "as the LORD commanded"; (j) THE DEUTERONOMY DIVERGENCE a DATA row — Deuteronomy 10:6-7's order (Bene-jaakan then Moserah) and its place for
## Aaron's death against 33:30-31 and 33:37-38 (the local Talmud scanned for the eight backward journeys; the Jerusalem Talmud's rows if local);
## (k) THE EDGES the census will demand — exodus_story (12:37, 13:20, 14:2, 15:22-27, 16:1, 17:1, 19:2; 12:12's spec), beha (10:12, 11:34-35, 12:16),
## shelach (13:3, 26), chukat (20:1, 20:22-29, 21:1-11), balak (22:1, 25:1), second_census (26:52-56), zelophehad (27:12), gad_reuben (32:34 Dibon),
## tochacha (Leviticus 26:1, 26:30), holiness (19:4), the calf's runner (Exodus 32:4); Deuteronomy 10:6-7, 1:2-3, 34:7; Joshua 5:10-12, 23:13; Judges
## 2:3; 1 Kings 6:1 forward; Genesis 14:7, Psalm 77:21, Isaiah 14:24, Nehemiah 9:11 OBSERVED — no link, or a labeled HYPOTHESIS; (l) THE DOCKET by the
## union rule — Rosh Hashanah 2b-3a (the first of Av; Arad's hearing), Kiddushin 37b-38a (the morrow of the Passover, the manna's ceasing — Joshua 5:11),
## Seder Olam 9-10 if local, Bava Batra 117a-122a (credited to the second census's docket), Megillah 22b (the figured stone, Leviticus 26:1), Zevachim
## 112b-119b (the high places' eras), the link rows for 33:4, 33:38, 33:52-55; the Tanchuma on the forty-two OUTSIDE the declared spine; (m) THE DISPLAY
## LAYER, NOT THE COMPILE'S — the store's "the-pretermission" for the Passover, "in-pebble" for the lot and "and-grave" for wrote stand at seats beyond
## this chapter (a display sitting's census); the chapter's twenty-one seats overridden by reference at the reading; (n) THE PARSER — no rule owed; THE
## DATE READER'S TWO FORMS (33:38's article-bearing ordinals against Deuteronomy 1:3's cardinals) noted for Deuteronomy's date checkpoints, not a gap here.
'''

RESEARCH = '''
## 2026-09-12 — THE JOURNEYS' READING (THE NUMBERS WALK sitting 13): THE CITATION SCAN'S TWO BLIND SPOTS (THE ABBREVIATION AND THE MARK); THE ITINERARY
## AGAINST DEUTERONOMY 10:6-7; THE PARSER'S TWO DATE READERS ON THE TWO FULL DATES; REKEM IN TWO LANGUAGES; THE STORE'S GLOSSES AT TWENTY-ONE WORDS

Numbers 33:1-56 read (logic/oral_triage/num_33_journeys_2026-09-12.md; NUMBERS_WALK.md "Sitting 13"; the unit num_33_journeys frozen, 208 units). Every
item below is computed in the sitting's scripts (jou_ink.py's asserts; jou_measure1.py / jou_measure2.py the prints).
1. THE CITATION SCAN'S TWO BLIND SPOTS. The "found by position" clause scans the whole Sifrei export for rows citing the chapter. The first scan looked for
   "(Bamidbar 33:n)" in the English and for the chapter mark with a straight quote in the Hebrew, and reported ZERO cross-citing rows. The export cites
   a verse of the same book as "(Ibid. 33:38)" and the Hebrew row writes the chapter with the GERSHAYIM (the double-stroke mark, ״) — the widened scan
   found ONE row (133:3 on 27:2, dating the daughters by 33:38), and two false "Ibid. 33" hits whose book is another (Genesis 33:4 at 69:2, Jeremiah
   33:1 at 151:1 — the abbreviation's referent is the row's last-named book, read to its verse). The class: a citation scanner must read the export's
   abbreviation AND its punctuation marks, and a report of zero is worth only the coverage line that names the forms scanned (THE_STEPS Step 2's rule,
   met on the shelf's own citations).
2. THE ITINERARY AGAINST DEUTERONOMY 10:6-7. Deuteronomy runs "from Beeroth-bene-jaakan to Moserah; THERE AARON DIED and was buried" and then "to
   Gudgodah, and from Gudgodah to Jotbathah"; the itinerary runs Moseroth (33:30) THEN Bene-jaakan (33:31) then Hor-haggidgad and Jotbathah, and puts
   Aaron's death at Mount Hor (33:38), seven camps after Moseroth by index. Two orders and two places in the ink itself; the declared shelf (the Sifrei on
   Numbers, Onkelos) is silent on both; filed as an OBSERVED divergence for the compile's docket (the eight backward journeys of the tradition if the local
   Talmud carries them) and for Deuteronomy's own reading. No adjudication.
3. THE PARSER'S TWO DATE READERS. The Torah writes the fortieth year twice in full: 33:38 בִּשְׁנַת הָאַרְבָּעִים "in the year of THE forty" with בַּחֹדֶשׁ הַחֲמִישִׁי "in the fifth month" — the
   article-bearing ORDINAL forms, read by ink_ordinals as [40, 5] with the day [1] by ink_numbers — and Deuteronomy 1:3 בְּאַרְבָּעִים שָׁנָה "in forty year" with
   בְּעַשְׁתֵּי עָשָׂר חֹדֶשׁ "in eleven month", the CARDINAL forms, read by ink_numbers as [40, 11, 1] with ink_ordinals empty. Both read right; a date checkpoint
   that takes one reader misses the other form. Noted for the compile's checkpoints at Deuteronomy.
4. REKEM IN TWO LANGUAGES. Onkelos renders Kadesh as רְקַם "Rekem" at ten seats of Onkelos Numbers (13:26; 20:1, 14, 16, 22; 27:14; 32:8's "Rekem Geah" for
   Kadesh-barnea; 33:36, 37; 34:4); the Hebrew's own רֶקֶם "Rekem" is a Midianite king at 31:8, rendered by the same consonants in the Aramaic — a scan of
   the translation for the place-name counts the king unless it reads the Hebrew beside it. Likewise "the graves of those who demanded" for
   Kibroth-hattaavah at all four seats of the name (11:34, 35; 33:16, 17), "Hor the mountain" at 33:37-41 and 34:8, "the fords of the Abarim" at 21:11
   (plene) and 33:44-45, "with bared head" for the high hand at 15:30 and 33:3 alone. The second measurement pass searched the POINTED Aramaic for these
   and found nothing at eleven seats — the points strip first (the shelf-search lesson, now on the translation).
5. A PISKA'S HEAD AND ITS ROWS. Piska 112's head row cites 15:27 and its second row is on 15:30 (the high hand); an assert typed "112 is on 15:30" from
   the row's verse fell. The head is the first row's citation; the rows walk on.
6. THE STORE'S GLOSSES AT TWENTY-ONE WORDS (the display layer, logic/glosses/word_gloss_overrides.yaml, by reference): "and-grave" for וַיִּכְתֹּב "and he
   wrote" (33:2), "the-pretermission" for הַפֶּסַח "the Passover" (33:3), "be-high-actively" for רָמָה "high" (33:3), "sentence" for שְׁפָטִים "judgments" (33:4),
   "eye" for עֵינֹת "springs" (33:9), "in-cord" for בִּגְבוּל "in the border" (33:44), "and-wander-away" for וְאִבַּדְתֶּם "and you shall destroy" (33:52),
   "figure" / "pouring-over" / "elevation" for the figured stones, the molten images and the high places (33:52), "desolate" for תַּשְׁמִידוּ "you shall
   demolish" (33:52), "in-pebble" for בְּגוֹרָל "by lot" (33:54), "jut-over" for תּוֹתִירוּ "you leave over" (33:55), "to-brier" for לְשִׂכִּים "as thorns" (33:55),
   "and-cramp" for וְצָרְרוּ "and they shall harass" (33:55), "compare" for דִּמִּיתִי "I thought" (33:56), and the "?" at the halves of Pi-hahiroth, Baal-zephon,
   Kibroth-hattaavah, Beth-jeshimoth and Abel-shittim. The frozen unit untouched.
7. TWO HOMOGRAPHS TOLD BY THE MORPHOLOGY. בָּמֹתָם "their high places" (33:52) is the consonants of בְּמֹתָם "at their death" (Leviticus 11:31-32, 6:7) — a
   plural noun with a suffix here, a preposition and a noun there; and מַשְׂכִּיּוֹת "figured" at Psalm 73:7 is another token than מַשְׂכִּית "figured" at
   Leviticus 26:1 and מַשְׂכִּיֹּתָם "their figured stones" at 33:52 — an exact-token census counts two Torah seats, not three.
'''

# ---- the gloss override rows (the display layer; by reference — the glosses stand at other words elsewhere) ----
OV = f'{ROOT}/logic/glosses/word_gloss_overrides.yaml'
store = sqlite3.connect(f'file:{ROOT}/torah_grok.SNAPSHOT-main-51801ca.sqlite?mode=ro', uri=True)
def idx_of(v, he_plain, nth=0):
    rows = store.execute("SELECT w.idx, w.gloss FROM words w JOIN verses v ON w.verse_id=v.id WHERE v.book='Num' AND v.chapter=33 AND v.verse=? AND w.he_plain=? ORDER BY w.idx", (v, he_plain)).fetchall()
    assert len(rows) > nth, (v, he_plain, rows)
    return rows[nth]
WANT = [(2, 'ו/יכתב', 'and-grave', 'and-he-wrote'), (3, 'ה/פסח', 'the-pretermission', 'the-Passover'), (3, 'רמה', 'be-high-actively', 'high'), (4, 'שפטים', 'sentence', 'judgments'),
        (9, 'עינת', 'eye', 'springs-of'), (44, 'ב/גבול', 'in-cord', 'in-the-border-of'), (52, 'ו/אבדתם', 'and-wander-away', 'and-you-shall-destroy'), (52, 'משכית/ם', 'figure-them/their', 'their-figured-stones'),
        (52, 'מסכת/ם', 'pouring-over-them/their', 'their-molten-images'), (52, 'במת/ם', 'elevation-them/their', 'their-high-places'), (52, 'תשמידו', 'desolate', 'you-shall-demolish'), (54, 'ב/גורל', 'in-pebble', 'by-lot'),
        (55, 'תותירו', 'jut-over', 'you-leave-over'), (55, 'ל/שכים', 'to-brier', 'as-thorns'), (55, 'ו/צררו', 'and-cramp', 'and-they-shall-harass'), (56, 'דמיתי', 'compare', 'I-thought'),
        (7, 'פי', '?', 'Pi-'), (7, 'בעל', '?', 'Baal-'), (16, 'ב/קברת', 'in-?', 'in-Kibroth-'), (49, 'מ/בית', 'from-?', 'from-Beth-'), (49, 'אבל', '?', 'Abel-')]
BYREF = '  # THE NUMBERS WALK sitting 13 (2026-09-12, Numbers 33): the store\'s glosses at the chapter\'s seats, by reference — RESEARCH_LOG.md\n'
for v, hp, bad, good in WANT:
    idx, g = idx_of(v, hp)
    assert g == bad, (v, hp, idx, g, bad)
    BYREF += f'  "Num.33.{v}:{idx}": "{good}"\n'
s = open(OV, encoding='utf-8').read()
assert s.count('\nby_ref:\n') == 1
if 'Num.33.' not in s:
    s = s.replace('\nby_ref:\n', '\nby_ref:\n' + BYREF)
    open(OV, 'w', encoding='utf-8').write(s)
else:
    print('override rows already present — verified below, not rewritten')
d = yaml.safe_load(open(OV, encoding='utf-8'))
K33 = [k for k in d['by_ref'] if k.startswith('Num.33.')]
assert len(K33) == 21 and d['by_ref'][f'Num.33.3:{idx_of(3, "ה/פסח")[0]}'] == 'the-Passover', 'the yaml is parsed before it is trusted'
print('overrides: by_gloss %d, by_ref %d (+21 for chapter 33), parsed' % (len(d['by_gloss']), len(d['by_ref'])))

# ---- the memory index is sized BEFORE any record is written (the 17,000-byte limit; a failure here writes nothing) ----
mi = f'{MEM}/MEMORY.md'; s_mem = open(mi, encoding='utf-8').read()
old = [l for l in s_mem.split('\n') if l.startswith('- [⚠ NUMBERS IN ORDER FROM 1:1](numbers-in-order-ruling.md)')]
assert len(old) == 1
new = ('- [⚠ NUMBERS IN ORDER FROM 1:1](numbers-in-order-ruling.md) — OWNER-RULED 2026-09-09: the chapter walk from 1:1 at the parashah grain (map World/step9/NUMBERS_WALK.md; chapters 9, 15:32-41, 27, 36 frozen at THE TENT and SKIPPED); ⚠ OWNER-RULED 2026-09-10 READ THEN COMPILE PER PORTION, never read ahead; CHAPTER NUMBERS, not portion names. NUMBERS 1:1-32:42 READ, FROZEN, COMPILED AND ON THE TAPE (sittings 1-12b; 54 runners, 59 daemons, RUN (1271, 66, 52, 0, 12, 1518, 30, 318, four pairs, 121); THE CLOSE LINE built 2026-09-12); 33 READ AND FROZEN (sitting 13, 2026-09-12, #152: 208 units, standing 2136, hash unmoved; the Sifrei silent by position, the cross-citing scan widened to "Ibid." and the gershayim; the forty-two on the ink\'s own verbs; 33:38\'s date the tape\'s own marker at 20:28; the run of Exodus 12:12 recorded only at 33:4). COMMITTED a42f518 (2026-09-11); sittings 8-13 UNCOMMITTED. THE REGISTER GATE (register_census.py --strict) AT EVERY COMPILE SITTING\'S GATES STEP. NEXT: SITTING 13b — THE COMPILE OF THE JOURNEYS (the stations as a list or as lines; the run of Exodus 12:12 closed by value; the command\'s daemon given_at 33:50 with the dispossession a debit open by design; the lot by CALL), then chapter 34\'s reading (the borders).')
s_mem = s_mem.replace(old[0], new)
assert len(s_mem.encode()) < 17000, ('MEMORY.md would be %d bytes' % len(s_mem.encode()))

# ---- the recovery file's section 12 ----
RECOVERY = '''
## 12. ADDENDUM (2026-09-12, at sitting 13's close — the state doc's COMPACTION POINT #152; this supersedes section 11's NEXT, which is kept as written)

SITTING 13 DONE: CHAPTER 33 (the journeys) READ AND FROZEN — 208 units, standing 2136, hash 8b8fff1fa28953af unmoved; NUMBERS_WALK.md "Sitting 13" the record
(the shelf's silence proved by position and the cross-citing scan WIDENED to the English "Ibid." and the Hebrew gershayim after a first scan reported zero —
one row credited; the parser's five number verses every one read, 33:38's date (40, 5, 1) THE TAPE'S OWN MARKER at 20:28; the forty-two on the ink's own
verbs; the run of Exodus 12:12 recorded only at 33:4; Deuteronomy 10:6-7's order observed); COMPILE_DEBT.md's sitting-13 box (a)-(n) the compile's checklist.
The engine, the tape, the sweep (54/54 at 6218) and every gate stand as at 12b's close. THE FORMS of sitting 13 are in World/step9/forms_numbers_walk/
(jou_dump.py, jou_measure1.py, jou_measure2.py, jou_ink.py, jou_legs.py, jou_rows_onkelos_a.py / _b.py, write_jou_ledger.py, write_jou_manifest.py,
seat_jou.py, jou_chain.sh, write_jou_records.py, assert_driver.py): copy the latest to the scratchpad and adapt. Still UNCOMMITTED since a42f518; commit only
on "commit push".

NEXT: SITTING 13b — THE COMPILE OF THE JOURNEYS (33:1-56) on the compile shape of section 5, with the register gate at the gates step: the measurements (the
tape's state and its markers at the dated stations; the callees live — exodus_story, beha, shelach, chukat, balak, second_census, zelophehad, gad_reuben,
tochacha, holiness, the calf's runner; the register gate's seats in the chapter at 33:2 and 33:38), THE DESIGN in NUMBERS_WALK.md before any code — THE
STATIONS' SHAPE (a data list of forty-two places with their first tellings, or lines for the itinerary's own stations; a retelling never writes an act
twice), THE RUN OF EXODUS 12:12 closed by value at 33:4 if a debit stands open, THE DATE CHECKPOINT (33:38 against the marker; 33:39 against Exodus 7:7),
THE COMMAND'S DAEMON (given_at 33:50, installed_by the verse — the divine voice; the dispossession a debit OPEN BY DESIGN to Joshua's runs; the three
objects' bans; the lot by CALL; the negative arm as data), the checkpoints (the prefix grepped first), THE PREDICTION'S ARITHMETIC; then the probes to FAIL,
the docket by the union rule (Rosh Hashanah 2b-3a, Kiddushin 37b-38a, Megillah 22b, Zevachim 112b-119b, Bava Batra 117a-122a credited, the link rows), the
types, the gates to FAIL, the runner, the recorder, the stitcher, the literals, the tape, the probe gates, the daemon and dependency gates, the journal gate,
THE REGISTER GATE --strict, the sweep, the records — THEN CHAPTER 34 (the borders' reading, 34:1-29; the Sifrei silent to 35:8) — NEVER THE NEXT READING
FIRST. Before the compile: reread NUMBERS_WALK.md "Sitting 12b — AS BUILT" (the compile's form) and "Sitting 13" (the reading and the owed list), THE_STEPS
Step 2 + Step 5 + the compiler block, memory's STANDING LESSONS head, THE_LOOP.md "Step 1's amendment — THE CLOSE LINE".
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

# ---- the forms: sitting 13's scripts into the walk's forms folder (the latest forms live in the repo, not the scratchpad) ----
FORMS = f'{ROOT}/World/step9/forms_numbers_walk'
copied = 0
for pat in ('jou_*.py', 'jou_*.sh', 'write_jou_*.py', 'seat_jou.py', 'assert_driver.py'):
    for f in glob.glob(f'{SP}/{pat}'):
        shutil.copy2(f, f'{FORMS}/{os.path.basename(f)}'); copied += 1
print(f'forms copied: {copied} -> {FORMS}')

# ---- memory ----
append(f'{MEM}/numbers-in-order-ruling.md', RESUME)
open(mi, 'w', encoding='utf-8').write(s_mem); print('MEMORY.md: the numbers line %d -> %d bytes; file %d bytes' % (len(old[0].encode()), len(new.encode()), len(s_mem.encode())))
LESSON = ('⚠ THE NUMBERS WALK sitting 13 — THE JOURNEYS\' READING (2026-09-12): THE CITATION SCANNER READS THE EXPORT\'S ABBREVIATION AND ITS MARKS — "(Bamidbar 33:n)" and a straight-quote chapter mark found ZERO cross-citing rows; "(Ibid. 33:n)" and the gershayim (the double-stroke mark) found the one that is there (133:3, dating the daughters by 33:38); the "Ibid." book is the row\'s last-named one (Genesis 33:4 and Jeremiah 33:1 the false hits): a report of zero is worth its coverage line, and the line names the forms scanned. THE POINTED TEXT IS NOT THE PLAIN — Onkelos\'s renderings searched on the pointed Aramaic returned nothing at eleven seats: strip the points, then search (the shelf-search lesson on the translation). TEN SLICE INDICES IN FIFTEEN FALLS, THE FIFTH INSTANCE — the itinerary\'s short verses made the indices look safe: print the verse, then slice, whatever its length. A PISKA\'S HEAD IS ITS FIRST ROW\'S CITATION, NOT THE ROW\'S VERSE (112 opens at 15:27; its second row is on 15:30). THE TWO DATE FORMS HAVE TWO READERS — 33:38\'s article-bearing year and month are the ordinal reader\'s [40, 5], Deuteronomy 1:3\'s cardinal date the number reader\'s [40, 11, 1]: a date checkpoint takes both. A HOMOGRAPH PLURAL IS ANOTHER TOKEN (Psalm 73:7\'s "figured" is not 33:52\'s form); "THEIR HIGH PLACES" IS THE CONSONANTS OF "AT THEIR DEATH" — the morphology decides. A HEADING COUNT EXCLUDES NOTHING THE PRINT DID NOT EXCLUDE (63 with "these are the words"). THE READING SITTING\'S SHAPE HELD (dump → measure in three passes → asserts 15 → 0 → rows → writer 0 misses, lint 0 first write → manifest 12/12 → seat → ritual 13 PASS → the fold predicted and matched); MIDDOT, MOVE_CATALOG and MISHNAH_TOPICS untouched when the spine is silent.\n')
insert_after(f'{MEM}/step9-exam-era.md', '## STANDING LESSONS AND WATCHES (moved verbatim from the MEMORY.md index line on 2026-09-07 to keep the index under its size limit; the W4/W3/W2/W1/D9/G/E lesson tail as it stood)\n', LESSON)
print('records written')
