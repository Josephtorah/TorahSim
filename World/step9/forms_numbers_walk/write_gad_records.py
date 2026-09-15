import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
_MEMORY = _os.path.expanduser('~/.claude/projects/' + _os.path.abspath(_ROOT).replace('/', '-') + '/memory')   # THE PORTABLE REPO (2026-09-15): the memory folder as Claude Code names it, from the root
#!/usr/bin/env python3
# THE NUMBERS WALK sitting 12 — GAD AND REUBEN (2026-09-12): the records — the stamp row, NUMBERS_WALK.md "Sitting 12", the state doc's #149,
# World/RESUME.md, THE_STEPS' paragraph, THE_BRIEFING's bullet, COMPILE_DEBT's box, RESEARCH_LOG's entry, the gloss override rows, the three memory
# files, and the forms copied into World/step9/forms_numbers_walk/. The counts below are the tools' own prints (the ritual's PASS lines, the bake's
# hash, the truth's units), typed from them; the corpus tripwire and the ritual's print are read back before a byte is written. Every insert lands on
# a unique anchor asserted present once. MIDDOT.md and MOVE_CATALOG.md UNCHANGED (no Sifrei row on the chapter — no case law read; no move).
import os, re, yaml, sqlite3, shutil, glob
ROOT = _ROOT
SP = os.path.dirname(os.path.abspath(__file__))
MEM = _MEMORY
truth = open(f'{ROOT}/logic/corpus/CORPUS_TRUTH.py', encoding='utf-8').read()
assert 'assert len(W["units"]) == 207' in truth and 'assert len(W["standing"]) == 2124' in truth and "== '8b8fff1fa28953af'" in truth, 'the fold is not the predicted one'
rit = open(f'{SP}/gad_ritual_num_32_gad_reuben.out', encoding='utf-8').read()
assert 'RITUAL COMPLETE for num_32_gad_reuben (207 frozen units)' in rit and rit.count('PASS ') >= 13, 'the ritual is not complete'
assert os.path.exists(f'{ROOT}/logic/oral_triage/num_32_gad_reuben_2026-09-12.md') and os.path.exists(f'{ROOT}/logic/oral_audit/manifests/num_32_gad_reuben_claims.json') and 'status: frozen' in open(f'{ROOT}/logic/units/num_32_gad_reuben.yaml', encoding='utf-8').read()
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

STAMP = ('| 2026-09-12 | num_32_gad_reuben | DELEGATED | FULL RULE | Numbers 32:1-42 derivation 2026-09-12 (THE NUMBERS WALK sitting 12 — GAD AND REUBEN; the owner: "Go" after the #148 rereads, on the ruling READ THEN COMPILE; the FORTY-FOURTH NUMBERS UNIT — the portion Matot\'s third and last chapter as one draft, the next draft opening at 33:1): declared reading COMPLETE — Onkelos Numbers 32:1-42 whole, 42 verses fresh; the Sifrei on Numbers found BY POSITION to have NO piska on the chapter (158 on 31:22 followed by 159 on 35:9 — the shelf silent from 31:25 to 35:8, 165 verses computed at sitting 11), the whole export scanned in both files for a row citing chapter 32 — three rows of other chapters (86:1, 95:1 on 32:1; 106:1 on 32:37-38) CREDITED with a quick look, read whole at sitting 3; no prior ledger had read a row of the chapter — grepped); coverage COMPUTED by script against the shelf\'s own counts (missing 0, extra 0); every quotation cut from the DB\'s and the shelf\'s bytes by consonants in glossed pieces of at most seven tokens (no cut miss on the writer\'s first run; gloss_lint 0 flags on the first write); the ink facts computed and asserted (ten failures on the first typed pass and one on the second — six slice indices, a substring census that caught the hated wife and the barking dogs, a morph prefix after the conjunction, the vowel points\' code points — each retyped from the leg print); the engine\'s parser measured on the chapter (two numbers, 32:11 twenty and 32:13 forty, both read; no gap); 10 claims VERIFIED 0 FAILED (verify_claims from the repo root on the manifest\'s path; every check the word\'s longest store-piece whole), claim_labels_census --strict GREEN (Numbers 346 labeled, debt 0), 10 WITNESS_READ operators seated by script on steps 1, 6, 10, 14, 16, 20, 25, 28, 33, 39 with every cite checked against the ledger\'s cite index, verify_text GREEN (42 steps, 7 scenarios), freeze_ritual PASS on every gate (13 PASS — RITUAL COMPLETE, the forty-fourth frozen unit of the walk\'s count: 207 in all), the corpus rebaked once (207 units, standing 2124 = 2114 + 10 as predicted, hash 8b8fff1fa28953af unmoved), the Python rendering layer written and self-proved. Machine-administered under the 2026-09-01 delegation; labeled DELEGATED; the owner may overrule. |\n')

WALK = '''
## Sitting 12 — GAD AND REUBEN, Numbers 32:1-42 (2026-09-12; the owner: "Go" after the #148 rereads, on the ruling READ THEN COMPILE): the reading and the unit

THE DRAFT: one — num_32_gad_reuben 32:1-42 (42 of 42 verses, computed): the portion Matot's third and last chapter whole; the next draft, num_33_journeys,
opens at 33:1 (asserted). Read in ONE pass, one ledger. The forms copied from sitting 11's scratchpad scripts and edited (gad_dump.py, gad_measure1.py,
gad_ink.py, gad_legs.py, gad_rows_onkelos_a.py / _b.py, write_gad_ledger.py, write_gad_manifest.py, seat_gad.py, gad_chain.sh, write_gad_records.py; every
one copied into World/step9/forms_numbers_walk/ at the close, with sitting 11's).

THE SHELF, BY POSITION (gad_ink.py's asserts): the Sifrei on Numbers has NO piska on the chapter — 158 (31:22) is followed by 159 (35:9): the shelf is SILENT
from 31:25 to 35:8 (165 verses, computed at sitting 11), and this chapter is the second stretch of that silence read on the translation alone. THE "FOUND BY
POSITION" CLAUSE run on the whole export — every row of every piska scanned in BOTH files for a citation of chapter 32: THREE rows of other chapters cite
it — 86:1 (on 11:2) and 95:1 (on 11:21) quote 32:1's "much cattle" as the proof that Egypt's flocks survived the desert (the craving a PRETEXT), and the
Hebrew rows quote the verse with GAD FIRST where the ink puts Reuben first (RESEARCH_LOG.md); 106:1 (on 12:14) quotes 32:37-38 to place Moses' death in
Reuben's portion and his grave in Gad's. All three read whole at sitting 3 (the num_11_complaint_quail and num_12_miriam ledgers) — CREDITED here with a
QUICK LOOK (credit guard 1: each opened again in both files; what each says of 32 is one proof clause). Onkelos 32 whole: 42. No prior ledger had read a row
of the chapter; five NAME verses of it (the two Beha'alotcha ledgers; the vows' exam docket — 32:29-30 THE DOUBLED CONDITION as the forward edge and 32:24
the utterance rule's seat, filed at 10b; the two Exodus dockets — 32:22's clearance, Mishnah Shekalim 3:2's proof): FRESH.

THE READING (eight modules — gad_dump.py the first measurement pass; gad_measure1.py the second, printing every candidate fact; gad_ink.py the ink with every
fact an assert (assert_driver.py: TEN failures on the first typed pass, ONE on the second — gad_legs.py printing every failing leg, each retyped from the
print: six slice indices (one typed from no print at all — Joshua 14:9's leg guessed, the lesson's sharpest form), a substring census on the root's two
letters that caught "the hated wife" and "we have been foolish" and, at the place-name, Isaiah's dogs that cannot "bark" — the token set named instead, a
morph prefix after the conjunction ("HC/Vh" is not "HVh"), and the vowel points tested by a retyped string — then by code point, and both words found to
carry the i-vowel in their second syllable, so the u-vowel (the three-dot mark) and the doubling dot decide — then 0) and the piece-wise cutters HP / AP; gad_rows_onkelos_a.py and _b.py the 42
rows; write_gad_ledger.py the writer → ONE ledger logic/oral_triage/num_32_gad_reuben_2026-09-12.md (42 sources: Onkelos MATERIAL 40 / CONTEXT 2; three
Sifrei rows credited; coverage computed, missing 0, extra 0; NO cut miss on the writer's first run; gloss_lint 0 on the first write).

THE INK, COMPUTED (the measurement pass FIRST, the asserts typed from the print):
- THE PARSER MEASURED FIRST (the standing rule): TWO numbers in forty-two verses, both read — 32:11 "from twenty years old and upward" [20], 32:13 "forty
  years" [40]; no ordinal, no starred homograph, no fraction; "half the tribe of Manasseh" rightly no number (the half a noun); 33:1 empty — NO GAP. The
  retellings by the same parser: Joshua 4:13's "about forty thousand" armed against the second census's Reuben 43,730 + Gad 40,500 + half of Manasseh's
  52,700 = 110,580 (the ink's own ratio); 1 Chronicles 5:18's 44,760; Jair's twenty-three and the sixty; Deuteronomy 2:14's thirty-eight; 14:33-34's forty.
- NO DIVINE FRAME: thirty-one narrative verbs in twenty verses and nine speech verbs, and no "and the LORD spoke/said" in forty-two verses — the Numbers
  chapters without one are 22-24, 29, 30, 32 and 36 (computed): the chapter's one "the LORD swore" (32:10) is Moses QUOTING chapter 14, and the two tribes'
  "that which the LORD has spoken to your servants" (32:31) calls MOSES' stipulation the LORD's word (Joshua 22:9 reads it "by the commandment of the LORD
  by the hand of Moses"); "before the LORD" SEVEN tokens (32:20-32); "my lord" for Moses at 32:25, 27 (Joshua's, Aaron's and the Gileadite heads' address).
- THE HINDER-ROOT IS THE VOWS' VERB: "discourage the heart" (32:7, 9) and "he disallowed her" (30:6 twice, 9, 12) share one root — its six Torah tokens all
  in chapters 30 and 32, its one Torah noun 14:34's "my alienation" in the oath this chapter retells; 32:7 IS A WRITTEN-AND-READ PAIR — the store carries
  the written and the read forms side by side (fourteen tokens for the DB's thirteen; 1:16's pair the walk's first), the DB writing the written form
  unpointed; THE SPIES' VERB AT EACH TELLING — "to spy out" (13:2, 17), "to see" (32:8), "to search" (Deuteronomy 1:22), "to scout" (1:24); Kadesh Barnea
  in Numbers at 32:8 and 34:4 alone; "will your brothers go to war and you sit here" — DEBORAH'S SONG runs the question on Reuben ("why did you sit among
  the sheepfolds", Judges 5:16) — OBSERVED.
- THE OATH RETOLD WITH THE VERB SUPPLIED: chapter 14 says "as I live" (14:21, 28), never "swore"; 32:10 and Deuteronomy 1:34 supply the verb; "if they
  see" 14:23's own "if"; "from twenty years old and upward" THE CENSUS FORMULA (twenty-three seats); "which I swore to Abraham, Isaac and Jacob" — Exodus
  33:1, Deuteronomy 34:4 and this; "followed me fully" Caleb's phrase (14:24) at eight seats with Solomon's negative; Caleb "THE KENIZZITE" — Genesis
  15:19's nation as his gentilic (Joshua 14:6, 14; Othniel "son of Kenaz"); "HE MADE THEM WANDER" the causative's one Torah seat; "until all the generation
  was consumed" Deuteronomy 2:14's phrase; "WHO DID EVIL IN THE EYES OF THE LORD" — the Judges' and Kings' formula (fifty-three seats) at its FIRST seat in
  the Bible's order; "the LORD's anger burned against Israel" Peor's verse and the Judges' refrain; "brood" a hapax and "sinners" Sodom's word (Genesis
  13:13 — Lot's plain, with 13:6, 10's "substance was great", "saw all the plain" beside 32:1: OBSERVED); "to add" Isaiah 30:1's idiom; "the fierce anger of
  the LORD" Peor's (25:4) and this.
- THE OFFER AND THE ORDER OF THE TWO: "folds for our CATTLE" before "cities for our LITTLE ONES" (32:16); Moses' "cities for your LITTLE ONES" then "folds
  for your SHEEP" (32:24); the acceptance "our little ones, our wives, our cattle, our beasts" (32:26); the retellings "your wives, your little ones, your
  cattle" (Deuteronomy 3:19, Joshua 1:14) — read off the tokens, no row of the declared shelf reads it; THE ARM-ROOT SEVEN TOKENS (the final letter its own
  code point, the set typed whole); JOSHUA'S "ARMED" IN ANOTHER WORD — "chamushim" (1:14, 4:12; Exodus 13:18), the consonants of FIFTY told apart by the
  points (the u-vowel and no doubling dot in the armed; the numeral's middle letter doubled) and by the morphology; Joshua 4:13 keeps "before the LORD" and counts
  the men; Deuteronomy 3:18 "before your BROTHERS" for it; "until every man has inherited" — the retellings' "until the LORD gives REST" (Deuteronomy 3:20,
  Joshua 1:15) and the release "now the LORD has given rest... as he spoke to them" (Joshua 22:4).
- THE CONDITION DOUBLED TWICE: "if you do this thing... and if you do not do so" (32:20, 23) and "if they pass over... and if they do not pass over" (32:29,
  30), each arm one seat, the negative arm with its own outcome ("they shall have possessions among you in Canaan" — Hamor's word, Genesis 34:10) — Mishnah
  Kiddushin 3:4's exemplar, the compile's docket; ONKELOS BUFFERS THE MARTIAL "BEFORE THE LORD" TO "BEFORE THE PEOPLE OF THE LORD" at 32:20, 21, 22, 27, 29,
  32 — the buffer's six seats in Onkelos Numbers ALL THIS CHAPTER'S (computed on the whole book) — and keeps it at the three legal seats; 1 CHRONICLES 22:18
  WRITES THE DOUBLE IN ITS OWN INK ("subdued before the LORD and before his people"); "CLEAR BEFORE THE LORD AND BEFORE ISRAEL" one seat (Mishnah Shekalim
  3:2's proof; David's 2 Samuel 3:28 its kin); "KNOW YOUR SIN WHICH WILL FIND YOU" one seat — Judah's "God has found out the iniquity of your servants"
  (Genesis 44:16) the idiom's one other seat.
- THE UTTERANCE RULE'S SECOND SEAT: "that which has gone out of your mouth you shall do" (32:24) = 30:3's "all that goes out of his mouth he shall do" — the
  phrase's two Bible seats; Onkelos renders both in one Aramaic; Jephthah the Gileadite's daughter (Judges 11:36) and Deuteronomy 23:24 its kin — 10b's
  filed seat found at the reading; "so will we do" the Gileadites' word to Jephthah (Judges 11:10); "WE" in its short form at three Bible seats (Joseph's
  brothers', Lamentations', this); "the possession of our inheritance" the daughters' construct (27:7); THE COMMISSION NAMED — "Eleazar the priest, Joshua
  son of Nun and the heads of the fathers of the tribes" (32:28) are Joshua 14:1's and 21:1's dividers of the land, word for word, before 34:17.
- THE GRANT AND THE CITIES: half Manasseh first named at the grant (32:33; the half-tribe phrase's nineteen seats); "the kingdom of Sihon" one seat, "the
  kingdom of Og" Deuteronomy 3's and this; Onkelos Mathnan; GAD'S EIGHT and REUBEN'S SIX — the nine asked at 32:3 split four and five (Sebam, Nebo, Beon
  respelled Sibmah, Nebo, Baal Meon), Kiriathaim and four of Gad's new; "their names being changed" one seat; "DIBON GAD" the itinerary's witness (33:45-46);
  THE TWO CROSSED CITIES in Joshua 13 — Dibon in Reuben's list (13:17), Heshbon on Gad's border (13:26; 21:39); Beth Peor Reuben's (13:20 — Moses' grave
  "opposite Beth Peor", Deuteronomy 34:6; the Sifrei 106:1's Gad rests on 33:21 — the exam's business); THE PROPHETS name ten of the chapter's cities as
  Moab's (Isaiah 15-16, Jeremiah 48, Ezekiel 25:9); 1 Chronicles 5:8 seats Reuben "at Aroer as far as Nebo and Baal Meon"; NOBAH AND JOGBEHAH together at
  Judges 8:11 — Gideon's route against MIDIAN, the two names' only other seat; ONKELOS renders 32:3's nine by Aramaic names with NEBO AS "THE BURIAL PLACE
  OF MOSES" and keeps the names at 32:38.
- MACHIR, JAIR AND NOBAH: "the sons of Machir son of Manasseh" — Joseph's knees (Genesis 50:23) and this; "Machir begot Gilead" (26:29); Joshua 17:1 "the
  father of Gilead, for he was a man of war"; Deuteronomy 3:15; "Jair son of Manasseh" (Deuteronomy 3:14, 1 Kings 4:13) whom 1 Chronicles 2:21-22 makes
  Hezron's grandson by Machir's daughter — the ink's two accounts; Havvoth Jair (Jair's villages) six seats; "went and took" at 32:41, 42 alone; "its
  daughters" the villages of Heshbon (21:25) and Jazer (21:32).
- THE ORDER OF THE TWO TRIBES: Reuben first at 32:1, GAD FIRST six times (32:2-33) and once at 2 Kings 10:33; Reuben first everywhere else (Deuteronomy
  three, Joshua fourteen, 34:14, 1 Chronicles 5:26); the Sifrei's rows quote 32:1 with Gad first.
- ONKELOS' MOVES: "a place FIT for a house of cattle"; "whose inhabitants the LORD smote"; the nine names in Aramaic, Nebo Moses' grave; "Rekem Geah" for
  Kadesh Barnea; "the anger of the LORD grew strong"; "after my FEAR" (32:11, 12, 15); "he drove them about"; "disciples of the guilty men"; "delay them";
  "make ready, hastening"; "before the PEOPLE of the LORD" six times; "acquitted"; "what goes out of your mouth" in the vows' Aramaic; "the holding of our
  possession"; "Mathnan"; "the heights" for Jogbehah; "their names encircled"; "villages" for the daughters.
- THE STORE'S GLOSSES READ BACK: the answer-verb "and-eye", the approach-verb "and-be", the anger "and-glow", the wilderness "in-pasture", the wandering
  "and-waver", the brood "multiplication", the adding "to-scrape-together", the destroying "and-decay", Kadesh "from-?", the villages "?", the renaming
  "revolve" — rows added to the display layer's override file by reference; the frozen unit untouched.

THE SIFREI'S OWN CASE LAW: none — no row of the spine on the chapter (MIDDOT.md unchanged; MOVE_CATALOG unchanged). The three credited rows carry one
proof clause each (the flocks' survival — the pretext; Moses' grave), the exam's business.

THE CLAIMS (write_gad_manifest.py → one manifest, 10 claims MT32A-01..10, every check the word's LONGEST STORE-PIECE WHOLE; the ID prefix asserted absent;
every cite checked against the ledger's CITE INDEX): verify_claims 10 VERIFIED / 0 FAILED (from the repo root on the manifest's path); claim_labels_census
--strict GREEN (Numbers 346 labeled 346, debt 0; every label ink). THE SEATS (seat_gad.py num_32_gad_reuben): 10 WITNESS_READ operators at the claims' first
verses (steps 1, 6, 10, 14, 16, 20, 25, 28, 33, 39), step E, the scenarios in the anchor form; verify_text GREEN (42 steps, 7 scenarios). THE RITUAL
(gad_chain.sh): every gate PASS (13 PASS) — RITUAL COMPLETE for the 207th frozen unit; the Python rendering layer written and self-proved. THE CORPUS
REBAKED (predicted before the fold: units 207, standing 2114 + 10 = 2124, hash unmoved — the tripwire's literals set to the prediction before the bake):
units 207, facts 1809, demands 341 (191 open), standing 2124, hash 8b8fff1fa28953af — the prediction matched; CORPUS TRUTH GREEN. THE STAMP: one delegated
FULL RULE row (logic/findings/STAMP_LEDGER.md). No engine file changed at this sitting — the sweep, the journal gate and the register gate stand as at
11b's close.

OWED TO THE COMPILE (sitting 12b; the box in COMPILE_DEBT.md, items (a)-(o)): THE STIPULATION as a conditional grant with both arms on the ledger (the two
tribes' debit to cross armed, the possession entitled on the condition, the negative arm's outcome a data row), its release a RUN OUTSIDE THE TORAH (Joshua
22:1-9 — the Jabesh-gilead class: the entry stays open on the tape as the captives' sentence does); THE UTTERANCE RULE'S SECOND SEAT by CALL into the vows'
runner (10b's filed debt paid); the clearance "before the LORD and before Israel" a status with Mishnah Shekalim 3:2 its docket; the oath retold as
checkpoints against chapter 14's tape lines (the shelach runner's forty years and its pending thirty-eight, the doomed generation's formula); the two and a
half's count by CALL into the second census (26:7, 18, 34) with Joshua 4:13's forty thousand a run citation; the grant of Sihon's and Og's kingdoms from
the chukat runner's conquests, the three parties' possession as transfers; the cities as data rows (the nine asked, the fourteen built, the two renamed,
the two crossed); Machir, Jair and Nobah with the two lineages a data row; the registry rows (the sons of Gad, the sons of Reuben, the half tribe of
Manasseh, Machir, Jair, Nobah — the homograph traps: Jair the judge, Machir son of Ammiel, Nobah the place); no receipt and no count line in the chapter for
the register gate — its seats measured at the compile; the docket by the union rule (Kiddushin 3:4 + 61a-62a, Bava Metzia 94a, Gittin 75a-b, Nedarim 11a;
Shekalim 3:2 + Yoma 38a; Bava Batra 117a-122a; Sotah 34b-35a; Sanhedrin 111a); the edges the census will demand (vows, shelach, chukat, census2, zelophehad,
balak, bamidbar, incense_shekel; Deuteronomy 3 and Joshua 1, 4, 22 forward; Judges 5, 8, 11 observed); the tape's lines undated after chapter 31's at
(40, 6, 1), no marker; a chapter with no divine frame — the stipulation in Moses' voice, installed_by's class named as 30:2's if a law is registered.

⚠ LESSONS (9): A SUBSTRING CENSUS CATCHES HOMOGRAPH NEIGHBORS — the root's two letters matched "the hated wife" (Deuteronomy 21:15), "we have been
foolish" (12:11) and Isaiah's dogs that cannot "bark" (56:10): name the token set, never the letters. THE MORPH PREFIX FOLLOWS THE CONJUNCTION — a narrative
causative is "HC/Vh…", not "HVh…": test the stem's tag inside the string. THE VOWEL POINT IS TESTED BY CODE POINT, AND THE WHOLE WORD'S POINTS ARE READ
FIRST — "armed" and "fifty" both carry the i-vowel in their second syllable; the u-vowel (the three-dot mark) and the doubling dot decide (the marks' order lesson, now on a single mark). A LEG
TYPED FROM NO PRINT IS A GUESS — Joshua 14:9's slice was typed without a print of the verse; six slice indices fell in all: the print has the index, and a
verse not printed is printed before it is sliced. THE SHELF'S SILENCE IS PROVED BY POSITION AND ITS CROSS-CITING ROWS BY A WHOLE-EXPORT SCAN — three rows
of other chapters cite 32, credited with a quick look, never counted as rows on the chapter. THE STORE'S PAIR — a written-and-read pair shows as one token
more in the store than in the DB (32:7; 1:16 the first): the count difference per verse is the finder. A BUFFER'S "ALL THIS CHAPTER'S" IS MEASURED ON THE
WHOLE BOOK — Onkelos's "before the people of the LORD" scanned over every verse of Onkelos Numbers before the claim was typed. THE ROWS' QUOTATION IS READ
AGAINST THE VERSE — the Sifrei's Hebrew cites 32:1 with Gad first where the ink has Reuben first: the shelf's word order is its own, filed. THE READING
SITTING'S SHAPE HELD: dump → measure → asserts (10 → 1 → 0) → rows → writer (0 misses; lint 0 first write) → manifest (10/10) → seat → ritual (13 PASS) →
the fold predicted and matched.

NEXT on the ruling: THE COMPILE OF GAD AND REUBEN (12b) on 1b's order — the measurements (the tape's state, the callees live: vows, shelach, chukat,
census2, zelophehad, balak; the register gate's seats in the chapter), THE DESIGN in this file before any code (the stipulation's ledger shape, the release
outside the Torah), the probes to FAIL, the docket by the union rule (Kiddushin 3:4 + 61a-62a, Shekalim 3:2, Bava Batra 117a-122a + the link rows), the
types, the runner, the tape, every gate with THE REGISTER GATE --strict at the gates step, the sweep — before chapter 33, never the next reading first.
'''

STATE = '''
═══ COMPACTION POINT #149 (2026-09-12 — written at THE NUMBERS WALK sitting 12's close; GAD AND REUBEN 32:1-42 READ AND FROZEN; NUMBERS 1:1-32:42 READ, 27 BY THE TENT; 1:1-31:54 COMPILED AND ON THE TAPE; 32 NOT YET COMPILED; A CLEAN COMPACTION POINT) ═══
STATE: 207 frozen units (206 + 1), standing 2124 (2114 + 10 as predicted), hash 8b8fff1fa28953af UNMOVED; 53 runners, 58 daemons, the sweep 53/53 at 6,144 UNMOVED (no runner changed); the journal gate, the register gate and the cursor probes GREEN as at 11b's close; RUN (1259, 66, 52, 0, 12, 1505, 29, 311, the four pairs, 120). LAST COMMIT a42f518; UNCOMMITTED: sittings 8 through 11b's paths, THE CLOSE LINE's, and this sitting's (logic/units/num_32_gad_reuben.yaml frozen; logic/oral_triage/num_32_gad_reuben_2026-09-12.md NEW; logic/oral_audit/manifests/num_32_gad_reuben_claims.json NEW; logic/py_units/num_32_gad_reuben.py NEW + ALL_UNITS.py; the html page and the indexes; logic/corpus/CORPUS_TRUTH.py (207, 2124); logic/glosses/word_gloss_overrides.yaml (the chapter's rows); STAMP_LEDGER.md; NUMBERS_WALK.md; COMPILE_DEBT.md; RESEARCH_LOG.md; THE_STEPS.md; THE_BRIEFING.md; World/RESUME.md; World/step9/forms_numbers_walk/ (sittings 11, 11b and 12's scripts copied in); this doc) — commit only on "commit push" (the NEVER-COMMIT set and the staging-by-exclusion form as before; ARCHITECTURE excluded).
THE SITTING (the owner: "Go" after the #148 rereads; NUMBERS_WALK.md "Sitting 12"): chapter 32 read as ONE draft (num_32_gad_reuben 32:1-42; 33:1 the next draft's) from sitting 11's forms: the Sifrei on Numbers found BY POSITION to have NO piska on the chapter (158 on 31:22 followed by 159 on 35:9; the whole export scanned in both files — THREE rows of other chapters cite 32:1 and 32:37-38, credited with a quick look, read whole at sitting 3; the Hebrew rows quote 32:1 with GAD FIRST where the ink has Reuben first — filed) + Onkelos whole (42) = 42 sources in one ledger (eight modules; TEN asserts fell on the first typed pass and one on the second — six slice indices (one typed from no print), a substring census catching the hated wife and the barking dogs, a morph prefix after the conjunction, the vowel points by code point — retyped from the leg print; no cut miss; lint 0 on the first write); 10 claims MT32A verified 10/10 and labeled (Numbers 346, debt 0), 10 operators seated, the ritual COMPLETE (13 PASS; the 207th unit), the corpus rebaked once (207, 2124, hash unmoved — predicted); THE PARSER MEASURED FIRST — two numbers, both read (32:11 [20], 32:13 [40]); NO GAP; THE CROWNS: NO DIVINE FRAME in forty-two verses (the Numbers chapters without one: 22-24, 29, 30, 32, 36 — Moses' stipulation "that which the LORD has spoken", Joshua 22:9's "by the hand of Moses"), THE HINDER-ROOT IS THE VOWS' VERB (32:7, 9 with 30:6-12 — six Torah tokens in two chapters; 14:34's "my alienation" its noun; 32:7 a written-and-read pair the store carries side by side), THE UTTERANCE RULE'S SECOND SEAT (32:24 = 30:3's phrase, the two Bible seats; Onkelos one Aramaic; Jephthah's daughter and Deuteronomy 23:24 its kin — 10b's filed seat found), THE CONDITION DOUBLED TWICE (32:20/23, 32:29/30 — Kiddushin 3:4's exemplar, the compile's docket), ONKELOS'S BUFFER "BEFORE THE PEOPLE OF THE LORD" at six martial seats — all of Onkelos Numbers' — and 1 Chronicles 22:18's own double, "CLEAR BEFORE THE LORD AND BEFORE ISRAEL" (Shekalim 3:2's proof) and "your sin which will find you" (Judah's idiom), THE OATH RETOLD WITH THE VERB SUPPLIED ("as I live" → "he swore"; the census formula; Caleb's phrase; the Kenizzite a Canaanite nation; "he made them wander" the causative's one Torah seat; "did evil in the eyes of the LORD" the Kings' formula at its first seat), GAD FIRST six times and Reuben first everywhere else, the cattle before the children and Moses' reversal, THE COMMISSION NAMED (32:28 = Joshua 14:1, 21:1), the cities (eight and six; the nine split four and five; Dibon Gad; the two crossed in Joshua 13; ten Moab's in the prophets; Nobah and Jogbehah on Gideon's route; Onkelos's Nebo "the burial place of Moses"), Joshua's "armed" in the consonants of "fifty", Jair's two lineages, Lot's plain and Deborah's sheepfolds observed; the store's eleven glosses overridden by reference; no case law (the Sifrei silent), MOVE_CATALOG unchanged.
THE RECORDS: NUMBERS_WALK.md "Sitting 12"; the ledger, manifest and py rendering; RESEARCH_LOG.md's entry; COMPILE_DEBT.md's sitting-12 box (a)-(o); STAMP_LEDGER's row; THE_STEPS' sitting-12 paragraph; THE_BRIEFING's scoreboard bullet; the gloss override rows; World/RESUME.md; the forms copied into World/step9/forms_numbers_walk/; memory (numbers-in-order-ruling.md, MEMORY.md, step9-exam-era.md's lessons head); this entry.
NEXT on the ruling: SITTING 12b — THE COMPILE OF GAD AND REUBEN on 1b's order (COMPILE_DEBT's sitting-12 box (a)-(o): the measurements first — the tape's state, the callees live (vows' utterance cell, shelach's forty years and the doomed generation, chukat's Sihon and Og, census2's 26:7/18/34 and Machir's clan, zelophehad's Machir line, balak's Peor phrase, bamidbar's census formula), the register gate's seats in the chapter measured; THE DESIGN in NUMBERS_WALK.md before any code — THE STIPULATION'S LEDGER SHAPE (the two tribes' debit to cross armed opened at 32:20-24 and accepted at 32:25-32; the possession entitled on the condition; the negative arm's outcome a data row; the grant at 32:33 written as transfers to three parties; the release at Joshua 22:1-9 a RUN OUTSIDE THE TORAH — the entry open on the tape, declared), the cells (the request, the rebuke and the oath retold, the offer, the condition doubled, the acceptance, the commission, the grant, the cities, Machir–Jair–Nobah), the DATA rows (the doubled condition's rule; the clearance; the names changed; Jair's lineages; the Kenizzite), the daemon with given_at and installed_by (a chapter with no divine frame — the class named), the tape lines page_order after chapter 31's with no marker, the checkpoints CG1-CG9, THE PREDICTION'S ARITHMETIC for RUN / CENSUS / PLACEMENT; the probes to FAIL (census_probes for the parser if any rule; register_probes if the gate changes); the docket by the union rule (Kiddushin 3:4 + 61a-62a, Bava Metzia 94a, Gittin 75a-b, Nedarim 11a; Shekalim 3:2 + Yoma 38a; Bava Batra 117a-122a; Sotah 34b-35a; Sanhedrin 111a + the link rows); the types by script; the gates to FAIL; the runner (cold_run_gad_reuben.py, the honest-pairing guard, the INK block exec'd from the sequence file, the tuples PREDICTED BY SCRIPT); the recorder; the stitcher; the literals and the checkpoints typed into cold_run_sequence.py; the tape run; the probe gates; the daemon and dependency gates; the journal gate; THE REGISTER GATE --strict; the sweep in the background; the records), THEN CHAPTER 33 — the journeys' reading (33:1-56; the Sifrei silent to 35:8 — Onkelos alone; the forty-two stations by the parser and the tape's markers) — never the next reading first.
POST-COMPACTION REREADS (mandatory, first sitting): the recovery file logic/pre_logic_methods_2026-07-28/RECOVERY_new_thread_2026-09-12.md whole (its section 5 THE COMPILE SITTING; its section 9) + numbers-in-order-ruling.md + this entry + NUMBERS_WALK.md "Sitting 11b — AS BUILT" (the compile's form) + NUMBERS_WALK.md "Sitting 12" (this reading's record and the owed list) + THE_STEPS Step 2 + Step 5 + the compiler block; memory's STANDING LESSONS head (the sitting-12 paragraph first); THE_LOOP.md "Step 1's amendment — THE CLOSE LINE" before any journal or cursor work; at the types step: daemon_dispositions.yaml's installed_by values. WATCHES: as #148's + A SUBSTRING CENSUS CATCHES HOMOGRAPH NEIGHBORS (name the token set) + THE MORPH PREFIX FOLLOWS THE CONJUNCTION + THE VOWEL POINT BY CODE POINT AFTER THE WHOLE WORD'S POINTS ARE READ + A LEG TYPED FROM NO PRINT IS A GUESS + THE STORE'S PAIR FOUND BY THE PER-VERSE COUNT + THE STIPULATION'S RELEASE OUTSIDE THE TORAH (an entry open on the tape by design) + THE FORMS COPIED, NEVER RETYPED FROM MEMORY.
'''

RESUME = '''SITTING 12 DONE 2026-09-12 (GAD AND REUBEN 32:1-42 READ AND FROZEN; NUMBERS_WALK.md "Sitting 12"; the owner: "Go" after the #148 rereads): the Sifrei on Numbers found BY POSITION to have no piska on the chapter (the shelf silent 31:25-35:8; three rows of other chapters citing 32:1 and 32:37-38 credited with a quick look — the Hebrew rows quoting 32:1 with Gad first, filed) + Onkelos whole (42) = 42 sources in one ledger (ten asserts fell on the first typed pass, one on the second — six slice indices, a substring census, a morph prefix, the vowel points by code point; no cut miss; lint 0 first write); 10 claims verified and labeled, 10 operators seated, the ritual COMPLETE → 207 units, standing 2124, hash unmoved (predicted); THE PARSER two numbers, both read — no gap; NO DIVINE FRAME in the chapter (Moses' stipulation "that which the LORD has spoken"); THE HINDER-ROOT THE VOWS' VERB (32:7, 9 with 30:6-12; 32:7 a written-and-read pair); THE UTTERANCE RULE'S SECOND SEAT (32:24 = 30:3 — 10b's filed seat found); THE CONDITION DOUBLED TWICE (Kiddushin 3:4's exemplar); Onkelos's "before the people of the LORD" at six martial seats, 1 Chronicles 22:18's own double; the clearance before the LORD and Israel; the oath retold with "swore" supplied and the Kings' formula at its first seat; Gad first six times; the cattle before the children reversed by Moses; the commission of Joshua 14:1 named; the cities eight and six, two crossed in Joshua 13, ten Moab's in the prophets, Nobah and Jogbehah on Gideon's route; Joshua's "armed" in the consonants of "fifty"; Jair's two lineages; the store's eleven glosses overridden by reference. NEXT: 12b — THE COMPILE OF GAD AND REUBEN (COMPILE_DEBT's sitting-12 box (a)-(o); the stipulation's ledger shape with its release outside the Torah; the utterance rule by CALL; the register gate at the gates step), THEN chapter 33 — never the next reading first.
'''

STEPS = '''SITTING 12 — GAD AND REUBEN, Numbers 32:1-42 (2026-09-12, on Brian's "Go" after the #148 rereads; World/step9/NUMBERS_WALK.md "Sitting 12"). The
chapter read as one draft (33:1 the next draft's) on Onkelos whole — the Sifrei on Numbers has no piska on it, found by position (158 on 31:22 is
followed by 159 on 35:9), and the whole export was scanned for any row citing the chapter: three rows of other chapters do, credited with a quick look
(and their Hebrew quotes 32:1 with Gad first where the verse has Reuben first — filed); 42 sources, one ledger, coverage computed, no cut miss, the lint
clean on the first write. The parser measured first: two numbers in forty-two verses, twenty and forty, both read — no gap. The finds, computed: NO
DIVINE FRAME IN THE CHAPTER — the LORD never speaks in it (the Numbers chapters without a frame are 22-24, 29, 30, 32 and 36), and the two tribes call
Moses' stipulation "that which the LORD has spoken to your servants", as Joshua 22:9 calls the grant "by the commandment of the LORD by the hand of
Moses"; THE VERB OF THE VOWS IS THE VERB OF THE DISCOURAGING — "why do you discourage the heart" (32:7) and "he disallowed her" (30:6-12) share one root,
its six Torah tokens all in chapters 30 and 32, and 32:7 is a written-and-read pair the store carries side by side; THE UTTERANCE RULE'S SECOND SEAT —
"that which has gone out of your mouth you shall do" (32:24) is the vows' "all that goes out of his mouth he shall do" (30:3), the phrase's two seats in
the Bible, Onkelos rendering both in one Aramaic, Jephthah the Gileadite's daughter and Deuteronomy 23:24 its kin — the seat the vows' compile filed to
this chapter, found; THE CONDITION DOUBLED TWICE — "if you do this thing... and if you do not" (32:20, 23), "if they pass over... and if they do not"
(32:29, 30), the negative arm with its own outcome — the Mishnah's exemplar of a stipulation (Kiddushin 3:4), the compile's docket; ONKELOS BUFFERS "before
the LORD" to "before the PEOPLE of the LORD" at the six martial seats — all six of Onkelos Numbers' — and keeps it at the three legal ones, and 1
Chronicles 22:18 writes the double in its own ink ("subdued before the LORD and before his people"); "clear before the LORD and before Israel" (Mishnah
Shekalim 3:2's proof) and "your sin which will find you" (Judah's "God has found out the iniquity of your servants"); the oath of chapter 14 retold with
the verb "swore" supplied (chapter 14 says "as I live"), the census formula "from twenty years old and upward" naming the doomed, Caleb "the Kenizzite"
by a Canaanite nation's name, "he made them wander" the causative's one Torah seat, "who did evil in the eyes of the LORD" — the Judges' and Kings'
formula at its first seat in the Bible; Gad named before Reuben six times in this chapter and once more in all the Bible; the tribes put the cattle
before the children and Moses reverses it; the commission Moses charges (Eleazar, Joshua, the heads of the fathers) is Joshua 14:1's dividers of the
land word for word; Gad's eight cities and Reuben's six, the nine asked split four and five, Dibon Gad the itinerary's own witness, Dibon and Heshbon
crossed between the tribes in Joshua 13, ten of the cities Moab's in the prophets, Nobah and Jogbehah on Gideon's route against Midian, Onkelos calling
Nebo "the burial place of Moses"; Joshua's "armed" in the consonants of "fifty", told apart by the points; Jair son of Manasseh and Jair grandson of
Hezron of Judah — the ink's two lineages. Ten claims verified and seated, the ritual complete: 207 units, standing 2124, hash unmoved, the fold
predicted and matched; the store's eleven glosses ("and-eye" for the answer, "and-be" for the drawing near, "revolve" for the renaming) overridden in
the display layer, never in the frozen unit. Honest catches: ten asserts fell on the first typed pass and one on the second — six slice indices (one
typed from no print at all), a two-letter census that caught the hated wife and the barking dogs, a morph tag read from the wrong end, a vowel point
retyped instead of tested by code point — each retyped from the leg print. Next: the compile (12b) — the stipulation as a conditional grant with both
arms on the ledger and its release at Joshua 22 a run outside the Torah, the utterance rule by call into the vows' runner, the oath's retelling
checked against chapter 14's tape, the two and a half's count from the second census, the cities and the three parties, the register gate at the gates
step — then chapter 33, never the next reading first.

'''

BRIEF = '''- **GAD AND REUBEN READ AND FROZEN — SITTING 12 DONE: THE LORD NEVER SPEAKS IN THE CHAPTER, THE VOWS' VERB IS THE DISCOURAGING VERB, THE UTTERANCE RULE HAS ITS SECOND SEAT, AND THE CONDITION IS DOUBLED TWICE** (2026-09-12, on your "Go"; World/step9/NUMBERS_WALK.md "Sitting 12"). Chapter 32 read as one unit on Onkelos whole — the Sifrei has no row on it, proved by position, and the three rows of other chapters that cite it credited (42 sources, one ledger, no cut miss, the lint clean first write). The parser: two numbers, both read, no gap. The finds: no divine frame in forty-two verses, so Moses' stipulation is "that which the LORD has spoken" (Joshua 22:9 agrees); "discourage the heart" and "he disallowed her" (chapter 30) share one root, all its Torah tokens in these two chapters; "that which has gone out of your mouth you shall do" (32:24) is the vows' own rule (30:3) — the seat the last compile filed forward, found; the condition doubled twice — the Mishnah's exemplar of a stipulation (Kiddushin 3:4); Onkelos softens "before the LORD" to "before the people of the LORD" at every martial seat, and the Chronicler writes the double himself (1 Chronicles 22:18); "clear before the LORD and before Israel"; the oath of chapter 14 retold with "swore" supplied and the Kings' formula "did evil in the eyes of the LORD" at its first seat; Gad before Reuben six times; the cattle before the children, reversed by Moses; the commission of Joshua 14:1 named; the cities eight and six, two crossed between the tribes in Joshua, ten Moab's in the prophets, Nobah and Jogbehah on Gideon's route against Midian; Jair's two lineages. Ten claims verified and seated, the ritual complete, 207 units, standing 2124, hash unmoved; the compile next.
'''

DEBT = '''
## SITTING 12 — GAD AND REUBEN'S READING (2026-09-12; NUMBERS_WALK.md "Sitting 12"; logic/oral_triage/num_32_gad_reuben_2026-09-12.md; the unit
## num_32_gad_reuben FROZEN) — OWED TO THE COMPILE (12b, on 1b's order with the register gate at the gates step): (a) THE STIPULATION'S LEDGER SHAPE —
## the two tribes' request (32:1-5) a plea; Moses' condition (32:20-24) opens a DEBIT on the two tribes (to cross armed before the LORD until the land is
## subdued) with the possession ENTITLED on it (32:22 "this land shall be yours for a possession") and the negative arm's outcome a DATA row (32:23 "you
## have sinned... your sin will find you"; 32:30 "they shall have possessions among you in Canaan"); the acceptance (32:25-27, 31-32) the commitment; the
## grant (32:33) written as TRANSFERS to three parties (the kingdoms of Sihon and Og from the chukat runner's conquests, 21:24, 35); the RELEASE a RUN
## OUTSIDE THE TORAH — Joshua 22:1-9 ("you have kept all that Moses commanded you... return to your tents") — the Jabesh-gilead class: the debit stays OPEN
## on the tape by design (as the captives' sentence does), declared in the design, Joshua 22:2-4, 9 the RUN_CITATION; (b) THE DOUBLED CONDITION as the
## exam's rule — Mishnah Kiddushin 3:4 (the stipulation doubled, the positive before the negative, the condition before the act: R. Meir against R.
## Chanina ben Gamliel) with Kiddushin 61a-62a, Bava Metzia 94a, Gittin 75a-b, Nedarim 11a its docket; the second doubling (32:29-30) to the commission —
## the vows' docket's forward edge (10b) PAID here; (c) THE UTTERANCE RULE'S SECOND SEAT — 32:24 "that which has gone out of your mouth you shall do" by
## CALL into the vows' runner (cold_run_vows's 30:3 cell): 10b's filed debt (Deuteronomy 23:22-24 and 32:24) paid at 12b; Jephthah's daughter (Judges
## 11:36) a RUN_CITATION; (d) THE CLEARANCE — 32:22 "clear before the LORD and before Israel" a STATUS effect (registered first) with Mishnah Shekalim 3:2 +
## Yoma 38a its docket (the two Exodus dockets' rows re-read); (e) THE OATH RETOLD — checkpoints against chapter 14's tape lines (the shelach runner's
## forty years and its pending thirty-eight, the doomed generation "from twenty years old and upward" — the census formula by CALL into bamidbar / census2;
## "until all the generation was consumed" against Deuteronomy 2:14's thirty-eight years at the tape's counter; the verb "swore" supplied — a data note);
## Caleb "the Kenizzite" (Genesis 15:19's nation) a DATA row (Sotah 11b-12a's Caleb if on the shelf); (f) THE TWO AND A HALF'S COUNT — 26:7 + 26:18 + 26:34
## ÷ 2 = 110,580 by CALL into the second census, Joshua 4:13's "about forty thousand" a RUN_CITATION (the ink's own ratio, no shelf row); 1 Chronicles
## 5:18's 44,760; (g) THE CITIES as DATA rows — the nine asked (32:3), Gad's eight and Reuben's six built (32:34-38), the two renamed (Nebo, Baal Meon —
## the exam's idol-names if a row is found), the two crossed in Joshua 13 (Dibon, Heshbon), Dibon Gad (33:45-46 — the next chapter's own witness, a
## forward pointer), the prophets' ten (Isaiah 15-16, Jeremiah 48, Ezekiel 25:9 — run citations of Moab's later hold); (h) MACHIR, JAIR AND NOBAH — three
## acts (took Gilead, took the villages, took Kenath) with the grant to Machir (32:40) a transfer; Jair's TWO LINEAGES a DATA row (32:41's "son of
## Manasseh" against 1 Chronicles 2:21-22's grandson of Hezron); Havvoth Jair's six seats; (i) THE REGISTRY ROWS — the sons of Gad, the sons of Reuben,
## the half tribe of Manasseh (34:14-15's next seats), Machir, Jair, Nobah; THE HOMOGRAPH TRAPS: Jair the judge (Judges 10), Jair Mordecai's father (Esther
## 2:5), Machir son of Ammiel (2 Samuel 9), Nobah the place (Judges 8:11); (j) THE REGISTER GATE — no receipt "as the LORD commanded" and no count line in
## the chapter (32:11's twenty and 32:13's forty are the oath's, not a census): the gate's seats in 32 measured at the compile's measurements step, declared
## from the print; (k) THE TAPE — the chapter undated: its lines page_order after chapter 31's thirteen at (40, 6, 1), no marker; the events: the request
## (speech), the rebuke (speech — the oath quoted, no divine frame), the offer (speech), the condition (speech — a law-like stipulation in Moses' voice),
## the acceptance (speech), the commission (speech), the grant (act — three transfers), the building (acts), Machir–Jair–Nobah (acts); the entities moses,
## eleazar, joshua, caleb existing; (l) THE DAEMON — a chapter with NO DIVINE FRAME: if a law is registered (the stipulation's rule), installed_by BOOT with
## the class NAMED as 30:2's (a law in Moses' voice) — the second pass's D2 to decide; the alternative: no daemon, the stipulation a case on the tent's
## form (a plea brought to Moses, Eleazar and the princes — 27:2's triad) — decided at the design; (m) THE EDGES the census will demand — vows (the
## utterance, the hinder-root), shelach (the spies, Eshcol, Kadesh Barnea, Caleb, the forty years), chukat (Sihon, Og, Jazer, "its daughters"), census2
## (26:7, 18, 29-34), zelophehad (Machir's line 27:1, 36:1), balak (25:3-4's anger phrases), bamidbar (the census formula), incense_shekel (Exodus 30:14's
## formula seat); Deuteronomy 3:12-20 and Joshua 1:12-18, 4:12-13, 22:1-9 forward run citations; Judges 5:16, 8:11, 11:10, 36, Genesis 13, 44:16, 1
## Chronicles 22:18 OBSERVED — no link, or a labeled HYPOTHESIS; (n) THE DOCKET by the union rule — Kiddushin 3:4 + 61a-62a, Bava Metzia 94a, Gittin
## 75a-b, Nedarim 11a, Shevuot 36a; Shekalim 3:2 + Yoma 38a, Pesachim 13a; Bava Batra 117a-122a (the division of the land — the two and a half); Sotah
## 34b-35a; Sanhedrin 111a; the Tanchuma on the cattle before the children OUTSIDE the declared spine; (o) THE DISPLAY LAYER, NOT THE COMPILE'S — the
## store's "and-eye" for the answer-verb and "and-be" for the approach-verb stand at many seats beyond this chapter (37 and 544 tokens of the two glosses,
## most of the second the verb "to be"): a display sitting's census, the chapter's eleven seats overridden by reference at the reading.
'''

RESEARCH = '''
## 2026-09-12 — GAD AND REUBEN'S READING (THE NUMBERS WALK sitting 12): THE SHELF SILENT, PROVED BY POSITION, AND ITS THREE CROSS-CITING ROWS — ONE QUOTING
## THE VERSE'S PAIR IN THE OTHER ORDER; A WRITTEN-AND-READ PAIR AT 32:7; THE STORE'S GLOSSES AT ELEVEN WORDS; ONKELOS'S BUFFER MEASURED ON THE WHOLE BOOK;
## AND THE RETELLINGS MEASURED

Numbers 32:1-42 read (logic/oral_triage/num_32_gad_reuben_2026-09-12.md; NUMBERS_WALK.md "Sitting 12"; the unit num_32_gad_reuben frozen, 207 units). Every
finding computed on the bytes (gad_ink.py's asserts; gad_measure1.py's print).
1. THE SHELF'S SILENCE PROVED BY POSITION AND SCANNED WHOLE: no piska of the Sifrei on Numbers stands between 158 (31:22) and 159 (35:9); the whole export
   (161 piskaot, both files) scanned for any row citing chapter 32 — three rows of OTHER chapters: 86:1 (on 11:2) and 95:1 (on 11:21) cite 32:1, 106:1 (on
   12:14) cites 32:37-38. Credited with a quick look (read whole at sitting 3), never counted as rows on the chapter.
2. THE ROWS' QUOTATION REORDERS THE VERSE'S PAIR: both 86:1 and 95:1 quote 32:1 in Hebrew as "and much cattle had the sons of GAD and the sons of REUBEN"
   (ומקנה רב היה לבני גד ולבני ראובן — "much cattle... Gad... Reuben"), where the verse reads "the sons of REUBEN and the sons of GAD" — the chapter's own
   order of 32:2-33 (Gad first six times) carried by the citing rows into the one verse that has Reuben first; the English rows keep Reuben first at 95:1 and
   Gad first at 86:1. A shelf word-order variant, filed beside the mistyped heads and the misquoted lemmas.
3. 32:7 A WRITTEN-AND-READ PAIR: the store carries the written form and the read form of "you discourage" side by side (תנואו/ן "you discourage", written;
   תניאו/ן, read) — fourteen tokens for the DB's thirteen, the one verse of the chapter whose counts differ (the per-verse count the finder; 1:16's pair the
   walk's first); the DB writes the written form WITHOUT ITS POINTS (the raw token unpointed among pointed neighbors) — the DB's convention for the written
   form, read off the bytes.
4. THE HINDER-ROOT'S TOKENS AND THE SUBSTRING TRAP: the root of "discourage" (32:7, 9) and "disallow" (30:6, 9, 12) — six Torah tokens in chapters 30 and 32,
   the noun at 14:34 ("my alienation") and Job 33:10; a census on the root's two letters catches "the hated wife" (Deuteronomy 21:15-17), "we have been
   foolish" (12:11) and "I will provoke them" (Deuteronomy 32:21): the token set named, the letters refused (the lesson banked).
5. "ARMED" AND "FIFTY" ONE SPELLING: Joshua's "chamushim" (1:14; 4:12; Exodus 13:18; Judges 7:11) and the numeral "fifty" share their consonants; the DB's
   morphology reads each (a participle / a cardinal), and the points differ — the u-vowel under the second letter and no doubling dot in the armed; the
   i-vowel and the doubled third letter in the numeral; both carry the i-vowel in their second syllable (a discriminating mark is chosen after the whole
   word's points are read).
6. ONKELOS'S BUFFER MEASURED ON THE WHOLE BOOK: "before the LORD" rendered "before the PEOPLE of the LORD" (קדם עמא דיי "before the people of the LORD") at
   32:20, 21, 22, 27, 29, 32 — every seat of the phrase in Onkelos Numbers is this chapter's, all six martial (the arming, the crossing, the subduing, the
   war); the three legal seats keep "before the LORD" (32:22 twice, 32:23). 1 Chronicles 22:18 has the double in the ink: "and the land is subdued before the
   LORD and before his people".
7. THE STORE'S GLOSSES AT ELEVEN WORDS: "and-eye" for the answer-verb (32:31 — the gloss's 37 tokens mix the answer-verb's forms with "and-the-eyes-of"),
   "and-be" for the approach-verb (32:16 — 544 tokens, nearly all "to be"; the approach-verb's two forms among them), "and-glow" for the anger (32:10, 13),
   "in-pasture" for the wilderness (32:13, 15), "and-waver" for "he made them wander", "multiplication" for "brood", "to-scrape-together" for "to add",
   "and-decay" for "you will destroy", "from-?" for "from Kadesh" (19 tokens of the gloss — every one a place name with the prefix), "?" for the pieces of
   Atroth Shophan, Beth Nimrah, Beth Haran, Baal Meon and "villages of", "revolve" for "their names being changed": overridden BY REFERENCE at the chapter's
   seats (logic/glosses/word_gloss_overrides.yaml); the frozen unit and the machine truth untouched.
8. THE PARSER: two numbers in the chapter (32:11 [20], 32:13 [40]), no gap; the retellings' numbers by the same parser — Joshua 4:13's 40,000 against 26:7 +
   26:18 + 26:34 ÷ 2 = 110,580; 1 Chronicles 5:18's 44,760; 1 Chronicles 2:22-23's 23 and 60; Judges 10:4's three thirties; Deuteronomy 3:4's 60; 2:14's 38.
9. THE RETELLINGS MEASURED: Deuteronomy 3:12-20 ("armed before your BROTHERS" for "before the LORD"; "I know that you have much cattle" quoting 32:1;
   "until the LORD gives rest to your brothers" for 32:18's "until every man has inherited"); Joshua 1:12-18 ("remember the word which Moses commanded";
   "all that you have commanded us we will do"); 4:12-13 ("armed before the children of Israel as Moses spoke to them"; "about forty thousand armed for the
   host before the LORD"); 22:1-9 ("you have kept all that Moses commanded you"; "divide the spoil of your enemies with your brothers"; "by the commandment
   of the LORD by the hand of Moses"); Judges 5:16-17 (Reuben "sat among the sheepfolds", Gilead "abode beyond the Jordan"); 8:11 (Nobah and Jogbehah on
   Gideon's route); 11:10, 36 (the Gileadites' "so will we do"; Jephthah's daughter's "as has gone out of your mouth"); Joshua 13:15-31 (Dibon in Reuben's
   allotment, Heshbon on Gad's border, Beth Peor in Reuben's — Moses' grave "opposite Beth Peor", Deuteronomy 34:6, against the Sifrei 106:1's Gad from
   33:21); Isaiah 15-16, Jeremiah 48, Ezekiel 25:9 (ten of the chapter's cities as Moab's); 1 Chronicles 2:21-23 (Jair the grandson of Hezron of Judah by
   Machir's daughter — against 32:41's "son of Manasseh"), 5:8-9, 18, 25-26 (Reuben "at Aroer as far as Nebo and Baal Meon"; the two and a half exiled
   first); 2 Kings 10:33 (Hazael's Gilead — the one other seat with Gad before Reuben).
10. THE TRIBES' ORDER: Reuben before Gad at 32:1 and at every seat of the pair outside the chapter but 2 Kings 10:33 (Deuteronomy 3:12, 16, 29:7; Joshua's
    fourteen; 34:14; 1 Chronicles 5:26); Gad before Reuben at 32:2, 6, 25, 29, 31, 33 and in the building (32:34 before 32:37).
11. THE KINGS' FORMULA'S FIRST SEAT: "did evil in the eyes of the LORD" (הרע בעיני יהוה "the evil in the eyes of the LORD") stands fifty-three times in the
    Bible; its first seat in the canonical order is 32:13, the Torah's other four Deuteronomy's (4:25, 9:18, 17:2, 31:29).
'''

# ---- the gloss override rows (the display layer; by reference — the glosses stand at other words elsewhere) ----
OV = f'{ROOT}/logic/glosses/word_gloss_overrides.yaml'
store = sqlite3.connect(f'file:{ROOT}/torah_grok.SNAPSHOT-main-51801ca.sqlite?mode=ro', uri=True)
def idx_of(v, he_plain, nth=0):
    rows = store.execute("SELECT w.idx, w.gloss FROM words w JOIN verses v ON w.verse_id=v.id WHERE v.book='Num' AND v.chapter=32 AND v.verse=? AND w.he_plain=? ORDER BY w.idx", (v, he_plain)).fetchall()
    assert len(rows) > nth, (v, he_plain, rows)
    return rows[nth]
WANT = [(31, 'ו/יענו', 'and-eye', 'and-they-answered'), (16, 'ו/יגשו', 'and-be', 'and-they-drew-near'), (8, 'מ/קדש', 'from-?', 'from-Kadesh'),
        (13, 'ו/ינע/ם', 'and-waver-them/their', 'and-he-made-them-wander'), (14, 'תרבות', 'multiplication', 'a-brood-of'), (14, 'ל/ספות', 'to-scrape--together', 'to-add'),
        (15, 'ו/שחתם', 'and-decay', 'and-you-will-destroy'), (38, 'מוסבת', 'revolve', 'changed'), (41, 'חות', '?', 'villages-of'),
        (35, 'עטרת', '?', 'Atroth'), (36, 'בית', '?', 'Beth'), (38, 'בעל', '?', 'Baal'), (10, 'ו/יחר', 'and-glow', 'and-burned'), (13, 'ו/יחר', 'and-glow', 'and-burned')]
BYREF = '  # THE NUMBERS WALK sitting 12 (2026-09-12, Numbers 32): the store\'s glosses at the chapter\'s seats, by reference — RESEARCH_LOG.md\n'
seen = {}
for v, hp, bad, good in WANT:
    n = seen.get((v, hp), 0); seen[(v, hp)] = n + 1
    idx, g = idx_of(v, hp, n)
    assert g == bad, (v, hp, idx, g, bad)
    BYREF += f'  "Num.32.{v}:{idx}": "{good}"\n'
idx2, g2 = idx_of(36, 'בית', 1); assert g2 == '?'
BYREF += f'  "Num.32.36:{idx2}": "Beth"\n'
s = open(OV, encoding='utf-8').read()
assert s.count('\nby_ref:\n') == 1
if 'Num.32.' not in s:
    s = s.replace('\nby_ref:\n', '\nby_ref:\n' + BYREF)
    open(OV, 'w', encoding='utf-8').write(s)
else:
    print('override rows already present (the first run wrote them before the memory-size check fell) — verified below, not rewritten')
d = yaml.safe_load(open(OV, encoding='utf-8'))
K32 = [k for k in d['by_ref'] if k.startswith('Num.32.')]
assert len(K32) == 15 and d['by_ref'][f'Num.32.31:{idx_of(31, "ו/יענו")[0]}'] == 'and-they-answered', 'the yaml is parsed before it is trusted'
print('overrides: by_gloss %d, by_ref %d (+15 for chapter 32), parsed' % (len(d['by_gloss']), len(d['by_ref'])))

# ---- the memory index is sized BEFORE any record is written (the 17,000-byte limit; a failure here writes nothing) ----
mi = f'{MEM}/MEMORY.md'; s_mem = open(mi, encoding='utf-8').read()
old = [l for l in s_mem.split('\n') if l.startswith('- [⚠ NUMBERS IN ORDER FROM 1:1](numbers-in-order-ruling.md)')]
assert len(old) == 1
new = ('- [⚠ NUMBERS IN ORDER FROM 1:1](numbers-in-order-ruling.md) — OWNER-RULED 2026-09-09: the chapter walk from 1:1 at the parashah grain (map World/step9/NUMBERS_WALK.md; chapters 9, 15:32-41, 27, 36 frozen at THE TENT and SKIPPED); ⚠ OWNER-RULED 2026-09-10 READ THEN COMPILE PER PORTION, never read ahead; CHAPTER NUMBERS, not portion names. NUMBERS 1:1-31:54 READ, FROZEN, COMPILED AND ON THE TAPE (sittings 1-11b; 53 runners, 58 daemons, RUN (1259, 66, 52, 0, 12, 1505, 29, 311, four pairs, 120); THE CLOSE LINE built 2026-09-12 on "I accept your recommendation" — run.close the tenth log class); 32 READ AND FROZEN (sitting 12, 2026-09-12, #149: 207 units, standing 2124, hash unmoved; the Sifrei silent by position; the utterance rule\'s second seat 32:24 = 30:3; the condition doubled twice, Kiddushin 3:4\'s exemplar). COMMITTED a42f518 (2026-09-11); sittings 8-12 UNCOMMITTED. THE REGISTER GATE (register_census.py --strict) AT EVERY COMPILE SITTING\'S GATES STEP. NEXT: SITTING 12b — CHAPTER 32\'S COMPILE (COMPILE_DEBT\'s sitting-12 box (a)-(o)), then chapter 33\'s reading.')
# the step-9 index line has grown past its hook (the loop's steps, THE TENT's four sittings and the walk's first three, with their lessons): MOVED VERBATIM
# into step9-exam-era.md as the 2026-09-08 line was, the index keeping a one-line hook — the established form when the index passes its size limit
s9 = [l for l in s_mem.split('\n') if l.startswith('- [Step 9 exam era](step9-exam-era.md)')]
assert len(s9) == 1 and len(s9[0]) > 3000, len(s9[0]) if s9 else 0
S9_NEW = ('- [Step 9 exam era](step9-exam-era.md) — ⚠ THE FULL MARQUEE, EVERY ⚠ LESSON, THE CAMPAIGNS AND THE CURRENT STATE LIVE IN THE FILE — read its head blocks and its "## STANDING LESSONS" section before any step-9 sitting; the index lines as they stood on 2026-09-08 and on 2026-09-12 were moved into the file verbatim (the two "## THE MEMORY.md INDEX LINE AS IT STOOD" sections — the open-items campaign, THE LOOP\'s steps 1-5, THE TENT\'s four sittings, the walk\'s sittings 1-3); the current state is in [[numbers-in-order-ruling]] and [[the-loop-ruling]].')
s_mem = s_mem.replace(old[0], new).replace(s9[0], S9_NEW)
assert len(s_mem.encode()) < 17000, ('MEMORY.md would be %d bytes' % len(s_mem.encode()))
S9_MOVED = ('## THE MEMORY.md INDEX LINE AS IT STOOD ON 2026-09-12 (moved verbatim from MEMORY.md at THE NUMBERS WALK sitting 12 when the index passed its size limit; the tail from THE LOOP\'s first step through the walk\'s sitting 3 as it stood — the later state in numbers-in-order-ruling.md and the-loop-ruling.md)\n' + s9[0] + '\n\n')

append(f'{ROOT}/logic/findings/STAMP_LEDGER.md', STAMP)
append(f'{ROOT}/World/step9/NUMBERS_WALK.md', WALK)
append(f'{ROOT}/logic/pre_logic_methods_2026-07-28/PROMPT_continue_solo_era_2026-08-06.md', STATE)
append(((_ROOT + '/World') + '/RESUME.md'), RESUME)
insert_before(f'{ROOT}/THE_STEPS.md', '## THE FINDINGS LOOP + THE STAMP LAW (owner-approved 2026-08-31)', STEPS)
insert_after(f'{ROOT}/THE_BRIEFING.md', '## SCOREBOARD (as of 2026-09-12, latest)\n', BRIEF)
append(f'{ROOT}/World/step9/COMPILE_DEBT.md', DEBT)
append(f'{ROOT}/RESEARCH_LOG.md', RESEARCH)

# ---- the forms: sittings 11, 11b and 12's scripts into the walk's forms folder (the latest forms live in the repo, not the scratchpad) ----
FORMS = f'{ROOT}/World/step9/forms_numbers_walk'
copied = 0
for pat in ('midian_*.py', 'midian_*.sh', 'midian_design.md', 'write_midian_*.py', 'seat_midian.py', 'add_types_midian.py', 'seq_record.py', 'seq_stitch.py', 'gad_*.py', 'gad_*.sh', 'write_gad_*.py', 'seat_gad.py', 'assert_driver.py'):
    for f in glob.glob(f'{SP}/{pat}'):
        shutil.copy2(f, f'{FORMS}/{os.path.basename(f)}'); copied += 1
print(f'forms copied: {copied} -> {FORMS}')

# ---- memory ----
append(f'{MEM}/numbers-in-order-ruling.md', RESUME)
insert_before(f'{MEM}/step9-exam-era.md', '## THE MEMORY.md INDEX LINE AS IT STOOD (moved verbatim from MEMORY.md on 2026-09-08', S9_MOVED)
open(mi, 'w', encoding='utf-8').write(s_mem); print('MEMORY.md: the numbers line %d -> %d bytes, the step-9 line %d -> %d bytes (moved into the file); file %d bytes' % (len(old[0].encode()), len(new.encode()), len(s9[0].encode()), len(S9_NEW.encode()), len(s_mem.encode())))
LESSON = ('⚠ THE NUMBERS WALK sitting 12 — GAD AND REUBEN\'S READING (2026-09-12): A SUBSTRING CENSUS CATCHES HOMOGRAPH NEIGHBORS — the root\'s two letters matched "the hated wife" (Deuteronomy 21:15), "we have been foolish" (12:11) and Isaiah\'s dogs that cannot "bark" (56:10): name the token set, never the letters. THE MORPH PREFIX FOLLOWS THE CONJUNCTION — a narrative causative is "HC/Vh…", not "HVh…": test the stem\'s tag inside the string. THE VOWEL POINT IS TESTED BY CODE POINT, AND THE WHOLE WORD\'S POINTS ARE READ FIRST — "armed" and "fifty" both carry the i-vowel in their second syllable; the u-vowel (the three-dot mark) and the doubling dot decide. A LEG TYPED FROM NO PRINT IS A GUESS — Joshua 14:9\'s slice was typed without a print of the verse; six slice indices fell in all: print the verse, then slice. THE SHELF\'S SILENCE IS PROVED BY POSITION AND ITS CROSS-CITING ROWS BY A WHOLE-EXPORT SCAN — three rows of other chapters cite 32, credited with a quick look, never counted as rows on the chapter. THE STORE\'S PAIR IS FOUND BY THE PER-VERSE COUNT — a written-and-read pair is one token more in the store than in the DB (32:7; 1:16 the first); the DB writes the written form unpointed. A BUFFER\'S "ALL THIS CHAPTER\'S" IS MEASURED ON THE WHOLE BOOK — Onkelos\'s "before the people of the LORD" scanned over every verse of Onkelos Numbers before the claim was typed (six seats, all 32\'s). THE ROWS\' QUOTATION IS READ AGAINST THE VERSE — the Sifrei\'s Hebrew cites 32:1 with Gad first where the ink has Reuben first: the shelf\'s word order is its own, filed. THE READING SITTING\'S SHAPE HELD (dump → measure → asserts 10 → 1 → 0 → rows → writer 0 misses, lint 0 first write → manifest 10/10 → seat → ritual 13 PASS → the fold predicted and matched); MIDDOT and MOVE_CATALOG untouched when the spine is silent.\n')
insert_after(f'{MEM}/step9-exam-era.md', '## STANDING LESSONS AND WATCHES (moved verbatim from the MEMORY.md index line on 2026-09-07 to keep the index under its size limit; the W4/W3/W2/W1/D9/G/E lesson tail as it stood)\n', LESSON)
print('records written')
