import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE NUMBERS WALK sitting 11 — MIDIAN (2026-09-12): the records — the stamp row, NUMBERS_WALK.md "Sitting 11", the state doc's #145, World/RESUME.md,
# THE_STEPS' paragraph, THE_BRIEFING's bullet, COMPILE_DEBT's box, RESEARCH_LOG's entry, MIDDOT's case-law block, the gloss override rows, the three
# memory files. The counts below are the tools' own prints (the ritual's PASS lines, the bake's hash, the truth's units), typed from them; the corpus
# tripwire and the ritual's print are read back before a byte is written. Every insert lands on a unique anchor asserted present once.
import os, re, yaml
ROOT = _ROOT
SP = os.path.dirname(os.path.abspath(__file__))
MEM = '<memory>'
truth = open(f'{ROOT}/logic/corpus/CORPUS_TRUTH.py', encoding='utf-8').read()
assert 'assert len(W["units"]) == 206' in truth and 'assert len(W["standing"]) == 2114' in truth and "== '8b8fff1fa28953af'" in truth, 'the fold is not the predicted one'
rit = open(f'{SP}/midian_ritual_num_31_midian.out', encoding='utf-8').read()
assert 'RITUAL COMPLETE for num_31_midian (206 frozen units)' in rit and rit.count('PASS ') >= 13, 'the ritual is not complete'
assert os.path.exists(f'{ROOT}/logic/oral_triage/num_31_midian_2026-09-12.md') and os.path.exists(f'{ROOT}/logic/oral_audit/manifests/num_31_midian_claims.json')
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

STAMP = ('| 2026-09-12 | num_31_midian | DELEGATED | FULL RULE | Numbers 31:1-54 derivation 2026-09-12 (THE NUMBERS WALK sitting 11 — MIDIAN; the owner: "ok go" after the recovery-file rereads in a new thread, on the ruling READ THEN COMPILE; the FORTY-THIRD NUMBERS UNIT — the portion Matot\'s second chapter as one draft, the next draft opening at 32:1): declared reading COMPLETE — Onkelos Numbers 31:1-54 whole, 54 verses fresh, and the Sifrei on Numbers piskaot 157-158 FOUND BY POSITION (12 rows at the shelf\'s row grain; every head checked against its rows\' own citations by script — no mistyped head; NO row from 31:25 to 35:8 — the shelf silent on 165 verses, computed; the rows\' own defects read to their verses in BOTH files — an attribution dropped three times, R. Akiva\'s arm reversed, an ancestor inserted against the row\'s own proof, the Talmud and the Mishnah supplied, a rule about rules dropped, a name garbled, a citation and a book wrong, a lemma misquoted, an identity\'s leg run backward; no prior ledger had read a row of the chapter — grepped); coverage COMPUTED by script against the shelf\'s own counts (missing 0, extra 0); every quotation cut from the DB\'s and the shelf\'s bytes by consonants in glossed pieces of at most seven tokens (no cut miss on the writer\'s first run; gloss_lint 1 flag on the first write — a hyphenated gloss — reworded and the ledger regenerated inside its writing step, then 0); the ink facts computed and asserted (fourteen failures on the first typed pass and one on the second — slice indices, token forms, a seat outside the Torah — each retyped from the leg print); the engine\'s parser measured on the chapter (right on the muster, the five kings, the schedule, the spoil\'s census, the halves, the tributes and the shekels; silent on the ratio\'s denominator at 31:28, 31:30, 31:47 — the fraction class "one of the N", six Bible seats measured, named and left for the compile); 11 claims VERIFIED 0 FAILED (verify_claims from the repo root on the manifest\'s path; every check the word\'s longest store-piece whole, the three-letter tribute-word refused as a check), claim_labels_census --strict GREEN (Numbers 336 labeled, debt 0), 11 WITNESS_READ operators seated by script on steps 1, 3, 7, 9, 13, 17, 19, 25, 32, 42, 48 with every cite checked against the ledger\'s cite index, verify_text GREEN (54 steps, 7 scenarios), freeze_ritual PASS on every gate (13 PASS — RITUAL COMPLETE, the forty-third frozen unit of the walk\'s count: 206 in all), the corpus rebaked once (206 units, standing 2114 = 2103 + 11 as predicted, hash 8b8fff1fa28953af unmoved), the Python rendering layer written and self-proved. Machine-administered under the 2026-09-01 delegation; labeled DELEGATED; the owner may overrule. |\n')

WALK = '''
## Sitting 11 — MIDIAN, Numbers 31:1-54 (2026-09-12; the owner: "ok go" after the recovery-file rereads in a new thread, on the ruling READ THEN COMPILE): the reading and the unit

THE DRAFT: one — num_31_midian 31:1-54 (54 of 54 verses, computed): the portion Matot's second chapter whole; the next draft, num_32_gad_reuben, opens at
32:1 (asserted). Read in ONE pass, one ledger. The first sitting of the new thread: the forms copied from World/step9/forms_numbers_walk/ into the scratchpad
and edited there (midian_dump.py, midian_measure1.py, midian_ink.py, midian_legs.py, midian_rows_onkelos_a.py / _b.py, midian_rows_sifrei.py,
write_midian_ledger.py, write_midian_manifest.py, seat_midian.py, midian_chain.sh, write_midian_records.py).

THE SHELF, BY POSITION (midian_ink.py's asserts): the Sifrei on Numbers has TWO piskaot on the chapter — 157 (31:1, nine rows) and 158 (31:22, three rows)
— TWELVE rows; every row's first citation is its own verse in order (ROW_CITES — the mistyped-head check is an assert now, and this chapter has none); the
next head, 159, is 35:9: THE SHELF IS SILENT FROM 31:25 TO 35:8 — the division, the tribute, the census of the spoil, the officers' gold, then chapters 32,
33, 34 whole and 35:1-8 (165 verses, computed) — the reading form holding on the translation alone for the fifth stretch of the walk. THE ROWS' OWN DEFECTS,
read to their verses in BOTH files (RESEARCH_LOG.md's entry, thirteen): 157:3's English drops "the words of R. Yishmael", REVERSES R. Akiva's arm ("to
exclude the tribe of Levi" for the Hebrew's "to include") and swaps his proof phrase; 157:4's English inserts "(Yithro, viz. Shemot 2:16)" as Phinehas's
mother's father where the Hebrew's own proof is Genesis 37:36 — Joseph, sold by "the MEDANITES" (Keturah's other son's name, 25:2; 37:28 has the
Midianites); 157:5's English supplies the Talmud's "four judicial death penalties" for the Hebrew's "by a court" (R. Natan), names "R. Eliezer" for the
Hebrew's R. Elazar, and puts the idolatry on the castles (Onkelos's assignment) where the Hebrew puts it on the cities; 157:6's English cites "(31:7)" for
31:17's second "kill" and DROPS THE HEBREW'S SECOND READING — "we do not punish by inference" — with R. Yishmael's name; 157:7's English replaces the
conclusion with "(see Chukath #126)"; 157:8's Hebrew runs the freed-word identity's first leg backward; 157:9's English drops R. Yoshiyah's name; 158:2's
English supplies the Mishnah's whitening-and-boiling split (Avodah Zarah 5:12) for the Hebrew's one list and one a-fortiori for the Hebrew's two; 158:3's
Hebrew misquotes 31:24 in the Levites' form (8:7) and cites 19:16's "slain by the sword" as 19:19, the English citing "Vayikra 19:19" for Bamidbar. Onkelos
31 whole: 54. No prior ledger had read a row of the chapter (eight name verses of it as cross-references; the Chukat ledger's rows 126:1, 127:1, 130:1 speak
of the Midian vessels and the sword from chapter 19's side — quick-looked, credit guard 1); FRESH.

THE READING (nine modules — midian_dump.py the first measurement pass; midian_measure1.py the second, printing every candidate fact; midian_ink.py the ink
with every fact an assert (assert_driver.py: FOURTEEN failures on the first typed pass, ONE on the second — midian_legs.py printing every failing leg, each
retyped from the print: five slice indices, the plural forms of bracelet and earring the measure had printed and the assert had not, tin only with its
article, the final-tsadi forms of "armed" in chapter 32 — the letter's end-form is its own code point, a wrath-verb nine words from the verse's end, "your
loins" at Kings and Chronicles beside Genesis — then 0) and the piece-wise cutters HP / AP; midian_rows_onkelos_a.py and _b.py the 54 rows;
midian_rows_sifrei.py the 12 rows; write_midian_ledger.py the writer → ONE ledger logic/oral_triage/num_31_midian_2026-09-12.md (66 sources: Onkelos
MATERIAL 52 / CONTEXT 2; the Sifrei 12 / 0; coverage computed, missing 0, extra 0; NO cut miss on the writer's first run; gloss_lint ONE flag on the first
write — a hyphenated English gloss, "wailing-blast" — reworded and the ledger regenerated ONCE inside its writing step, then 0).

THE INK, COMPUTED (the measurement pass FIRST, the asserts typed from the print):
- THE PARSER MEASURED FIRST (the standing rule): RIGHT on the muster (31:4 the doubled "a thousand to a tribe" read as two thousands — the distributive;
  31:5 [1000, 12000]; 31:6 [1000]), the five kings (31:8 [5]), the schedule (31:19 [7], the ordinals [3, 7]; 31:24 [7]), THE SPOIL'S CENSUS (675,000 /
  72,000 / 61,000 / 32,000), THE HALVES (337,500 / 36,000 / 30,500 / 16,000 at both seats), THE TRIBUTES (675 / 72 / 61 / 32), THE SHEKELS (16,750); the
  captains of "the thousands and the hundreds" rightly no number (census_probes G3); no starred homograph in fifty-four verses; SILENT on the ratio's
  denominator — THE FRACTION CLASS "one of the N" at 31:28 ("one soul of the five hundred" [1]), 31:30 and 31:47 ("one held of the fifty" [1]): the class
  named and left at census_probes R29; its Bible seats SIX, measured corpus-wide (the three here; Ecclesiastes 7:28 "one of a thousand"; Ezekiel 45:15
  "one of the flock of the two hundred"; Nehemiah 11:1 "one of the ten", read [1, 9]); the zaqef (the mid-verse accent) closes "one soul" and the
  denominator stands in the next phrase — the compile's probe list.
- THE FRAMES AND THE REGISTER: THIRTY narrative verbs in twenty-seven verses — a RUN chapter: two divine frames (31:1 spoke-saying; 31:25 said-saying, the
  form's five Torah seats), Moses' relay (31:3 "and Moses spoke to the people" — one Bible seat), Eleazar's law (31:21 — one seat), the officers' first
  person (31:50), and FOUR RECEIPTS "as the LORD commanded Moses" (31:7, 31, 41, 47) — the most of any Numbers chapter (Exodus 39 and 40 seven each,
  Leviticus 8 five; 41 seats of the form) — the register gate's four seats, with the four count lines (31:35, 36, 40, 46), declared NONE now and paid by
  the compile; "and Moses was wroth" — the wrath-verb with Moses as subject at three Torah seats (Exodus 16:20, Leviticus 10:16, 31:14), the Sifrei 157:9's
  three anger-and-error places sharing two (Meribah's verse carries no wrath-verb).
- THE COMMAND AND ITS RUN SHARE THE WORD: "the Midianites" with the article at TWO Bible seats — 25:17 "harass the Midianites" and 31:2; "avenge the
  vengeance" one seat; Moses' relay turns Israel's vengeance into "the vengeance of the LORD" (31:3 — the phrase's three other seats Babylon's); "afterward
  you shall be gathered to your people" one seat — 27:13's death sequenced after the war; "arm yourselves" one seat, the root's Torah seats all in 31-32 and
  Deuteronomy 3:18; "a thousand to a tribe" three seats all here, the doubled phrase one — 1,000 × 12 = 31:5's twelve thousand, the ink's own product;
  "were delivered" and "to commit" the deliver-root's two Torah seats, both here; THE TRUMPETS' ONE NARRATIVE SEAT IN THE TORAH (31:6; 10:8-10 the law;
  2 Chronicles 13:12 the phrase's other seat) — 10:9's war clause run, the beha runner's open trumpets debit.
- THE WAR: "they warred" one seat; "and they killed every male" — Shechem's the only other seat (Genesis 34:25); "the kings of Midian" four Bible seats,
  Gideon's two the others; the five names retold at Joshua 13:21 as "the princes of Sihon, dwelling in the land", 13:22 adding "the soothsayer" and "to
  their slain" for "upon their slain"; Zur Cozbi's father (25:15); "they killed by the sword" with Elijah's; the sword in Balak's chapter thrice — 22:29's
  "would there were a sword in my hand" the clause the compile closes at 31:8; THE BOOTY'S FOUR NOUNS (the prey's six Bible seats five here) and THE
  TRIBUTE-WORD'S SIX BIBLE SEATS ALL HERE; "their castles" four seats — Onkelos "their houses of worship"; "the plains of Moab by the Jordan of Jericho".
- THE WRATH AND THE WOMEN: "the officers of thousands and of hundreds" — Jethro's grades (Exodus 18:21, 25; Deuteronomy 1:15) as the army's ranks, both
  seats here; "have you let every female live" the midwives' verb; "by the word of Balaam" one seat (Onkelos "by the counsel"); "treachery against the
  LORD" the guilt offering's and the suspected wife's phrase; Peor's plague named five times; "in the congregation of the LORD" here and Joshua 22:17 —
  PHINEHAS HIMSELF retelling the clause; 31:17 opens and closes on "kill"; "lying with a male" — this chapter's three seats and JABESH-GILEAD'S TWO
  (Judges 21:11-12): twelve thousand sent, every male and every woman who knew a man devoted, four hundred virgins kept — the sentence RUN in Judges with
  its number and its phrase; Deuteronomy 20:13-14 spares "the women and the little ones" — this chapter stricter on both.
- THE PURIFICATION: "on the third day and on the seventh day" three seats (19:12, 19, 31:19); the purify-verb's six Torah tokens all in 19 and 31 (the
  store glosses it "sin"); 19:16's "slain by the sword" the Sifrei 158:3's sword unclean seven days; THE FOUR MATERIALS against Leviticus 11:32's four —
  SACK there against GOAT-WORK here (the freed-word identity of 157:8); THE SIX METALS in one verse — tin's one Torah seat, lead's two; "the water of
  sprinkling" four seats all in 19 and 31; "wash your garments on the seventh day... afterward come into the camp" against 19:19's "clean at evening"
  (158:3's two-way likening); Onkelos makes the purifying the SPRINKLING.
- THE DIVISION AND THE TRIBUTE: "take the sum" the census formula's singular imperative, one seat (Exodus 30:12 the ransom's verse); THE HALF-ROOT EIGHT
  TOKENS IN FIVE SPELLINGS — "half" at 31:29 and 31:42 in THE HALF-SHEKEL's spelling; "the LORD's heave-offering" eleven seats — the half-shekel's two, the
  donation's three, the tithe's tithe's three, this chapter's two, Hezekiah's; "the Levites who keep the charge of the tabernacle" 1:53's charge; the
  priest's one in five hundred, the Levites' one in fifty — ten times; 31:30 adds "of all the beasts"; the equal halves — David's statute at Ziklag
  (1 Samuel 30:24-25) and Joshua 22:8's "divide the spoil with your brothers" the ink's kin which NO ROW OF THE DECLARED SHELF LINKS to 31:27: observed, not
  linked (THE LINK REVIEW LAW).
- THE ARITHMETIC IS EXACT: the four totals (840,000 heads, every one a multiple of a thousand) ÷ 2 = the halves; the halves ÷ 500 = the tributes (840
  heads to the priest); the congregation's half the same four numbers; THE LEVITES' SHARE STATED AS A RATE AND NEVER AS A NUMBER — 6,750 / 720 / 610 /
  320 = 8,400 heads, ten times the priest's, computed and never written; the soldiers' private plunder (31:53) outside the count; 16,750 shekels
  (Onkelos: selas, the coin — the conversion layer); Gideon's 1,700 of Midianite gold the word's second count.
- THE OFFICERS' GOLD RUNS THE RANSOM OF EXODUS 30 AT A COUNT: "not one man of us is missing" (Nabal's shepherds' word); "the LORD's offering" the second
  Passover's phrase; THE FIVE ORNAMENTS (Saul's armlet, Rebekah's bracelet — the heifer chapter's "bound cover" its homograph — Ezekiel's earring, the
  donation's kumaz, the clasp, and its ring: the two gold lists share the ring, the kumaz and "articles of gold"); "to atone for our souls" one seat — the
  half-shekel's "to atone for your souls" (Exodus 30:15, 16); "a memorial for the children of Israel before the LORD" one seat — EXODUS 30:16'S SIX WORDS
  in another order; the trumpets' "be REMEMBERED before the LORD" (10:9) at the war's opening the same root: a REFERENCE by the shared words — the
  compile's CALL into the half-shekel engine.
- ONKELOS' MOVES: "the vengeance of the JUDGMENT of the people of the LORD" (the buffer); "were chosen"; "the trumpets of the wailing blast"; "their houses
  of worship"; "by the counsel of Balaam"; "you shall sprinkle on him"; "receive the account"; "a levy", "a separation"; "one that is held"; "strayed" for
  "missing"; the ornaments in Aramaic; "selas"; "the tabernacle of time".
- THE STORE'S GLOSSES READ BACK: the sword "in-drought", the prey "the-jaws", the wrath "and-crack-off", the purifying "sin", the washing "and-trample", the
  tent of meeting "seasons" — Strong's homonyms at six words: rows added to the display layer's override file (logic/glosses/word_gloss_overrides.yaml —
  by_gloss where every Torah seat of the gloss is the same word, by_ref where it is not); the frozen unit untouched; the next render picks them up.

THE SIFREI'S OWN CASE LAW (twelve entries appended to MIDDOT.md "The middot's own case law"): the leaders' praise and the name read twice (157:1); "arm" by the
lexical identity with Deuteronomy 3:18 (157:2); THE DOUBLED NUMERAL DISPUTE — R. Yishmael's 24,000 against R. Akiva's 12,000, and "all" including Levi
(157:3); "the holy" and "his hand" by two identities (157:4); the second naming of the kings, the retelling read for the mode, the frame read for a cause
(157:5); THE REFUSED A-FORTIORI ON A PENALTY — "we do not punish by inference" — beside R. Yishmael's structural "to close the subject" (157:6); the tent's
straw excluded, the captives likened (157:7); THE FREED-WORD IDENTITY "garment"-"garment" run two ways (157:8); anger begets error at three places, "in the
name of its sayer" (157:9); "only" divides, the analogy on a shared feature (158:1); the lists as specification, the immersion by a-fortiori (158:2); the
two-way likening of the camp and the evening (158:3). No new move (MOVE_CATALOG unchanged: the run-teaches-spec candidates — the officers' gold on Exodus
30's words, Jabesh-gilead on 31:17-18, Joshua 13:21-22's deltas — await a teacher at the compile's docket; M-22 is a generalization, never a license).

THE CLAIMS (write_midian_manifest.py → one manifest, 11 claims MT31A-01..11, every check the word's LONGEST STORE-PIECE WHOLE — the three-letter tribute-word
refused as a check by the four-code-point floor; the ID prefix asserted absent; every cite checked against the ledger's CITE INDEX): verify_claims 11
VERIFIED / 0 FAILED (from the repo root on the manifest's path); claim_labels_census --strict GREEN (Numbers 336 labeled 336, debt 0; every label ink — the
Sifrei's I2 the exam's). THE SEATS (seat_midian.py num_31_midian): 11 WITNESS_READ operators at the claims' first verses (steps 1, 3, 7, 9, 13, 17, 19, 25,
32, 42, 48), step E, the scenarios in the anchor form; verify_text GREEN (54 steps, 7 scenarios). THE RITUAL (midian_chain.sh): every gate PASS (13 PASS) —
RITUAL COMPLETE for the 206th frozen unit; the Python rendering layer written and self-proved. THE CORPUS REBAKED (predicted before the fold: units 206,
standing 2103 + 11 = 2114, hash unmoved — the tripwire's literals set to the prediction before the bake): units 206, facts 1809, demands 341 (191 open),
standing 2114, hash 8b8fff1fa28953af — the prediction matched; CORPUS TRUTH GREEN. THE STAMP: one delegated FULL RULE row (logic/findings/STAMP_LEDGER.md).
No engine file changed at this sitting — the sweep, the journal gate and the register gate stand as at 10b's close.

OWED TO THE COMPILE (sitting 11b; the box in COMPILE_DEBT.md, items (a)-(n)): the Midian debit closed at 31:7 by the receipt, by value; Balaam's death
closing the ass's sword clause and the five kings' deaths (Zur Cozbi's father); the trumpets' debit run at 31:6 with its class declared (the ink narrates
no sounding); the muster as a count with R. Yishmael's 24,000 a data setting; the sentence's case kinds against Deuteronomy 20:13-14 (not compiled) with
Judges 21:10-12 as a run citation; the purification by CALL into the heifer runner (the water, the third and seventh day, the sword's seven days), the
seven days a timer on the warriors, the captives' sprinkling; the four materials by CALL into the carcass runner; THE KASHERING RULE a new cell (the six
metals, the fire, the water of sprinkling, the water) with Avodah Zarah 5:12 and 75b-76b its docket; THE FRACTION CLASS taught to the parser FIRST (R29
retyped to FAIL; the six seats the probes); the halving, the tribute and the Levites' cells with the arithmetic as CHECK cells and the unwritten share
computed; the register gate's eight seats paid from the print; the officers' gold by CALL into the half-shekel engine (the count, none missing, the
atonement, the memorial) with Shabbat 64a-b its docket; the entities (the five kings, the captives as a party); the tape's lines undated, page_order after
chapter 30's, no marker, Moses' death sequenced after the war (a checkpoint at Deuteronomy 34); Eleazar's statute in the priest's voice citing Moses — a
THIRD installed_by form beside boot and the verse; the docket by the union rule; the edges the census will demand (balak, beha, chukat, lev_11,
incense_shekel, bamidbar's charge; Deuteronomy 20-21 forward; 1 Samuel 30 observed, no link); the store's four "sin" glosses at chapter 19's seats (the
display layer, not the compile's).

⚠ LESSONS (12): THE FINAL LETTER IS ITS OWN CODE POINT — a regex on the root's plain letters missed the end-form of "armed" (the final tsadi, the
letter's end-form) in chapter 32: a root census names its final forms (Balak's gentilic lesson, now on a verb). THE TOKEN SET IS THE PRINT'S — the assert
typed two spellings where the measure had printed four (bracelet, earring): copy the print's set, never a subset. THE ARTICLE IS PART OF THE TOKEN — tin
stands in the Torah only as "the tin"; a bare-stem census returns nothing, and the look-alikes are a verb. THE LEG DIAGNOSTIC, AGAIN — fourteen asserts fell
on the first typed pass and one on the second, every one a slice index, a token form or a seat outside the Torah: print every leg, retype from the print,
scope to the Torah when the claim is the Torah's. A HYPHENATED ENGLISH COMPOUND IS FLAGGED BY THE LINT — reword and regenerate inside the writing step. THE
HEADS ARE CHECKED AGAINST THE ROWS' OWN CITATIONS BY SCRIPT — an assert (ROW_CITES), not a reading. THE TWO FILES ARE READ AGAINST EACH OTHER AT EVERY ROW
— the English reversed an arm, inserted an ancestor, supplied the Talmud and the Mishnah, dropped a rule about rules and three attributions; the Hebrew
misquoted a lemma and ran an identity's leg backward: the Hebrew row is the shelf, the English a witness with its own defects. THE SHELF'S SILENCE IS
COMPUTED (165 verses). THE FRACTION CLASS MEASURED CORPUS-WIDE BEFORE THE COMPILE (six seats; the class named and left at R29 holds until the compile teaches
it). THE ARITHMETIC IS THE INK'S OWN CHECKSUM, AND THE UNWRITTEN NUMBER IS COMPUTED (the Levites' 8,400). THE STORE'S GLOSSES ARE STRONG'S HOMONYMS — the
override file, never the frozen unit. THE READING SITTING'S SHAPE HELD IN A NEW THREAD FROM THE COPIED FORMS: dump → measure → asserts (14 → 1 → 0) → rows →
writer (0 misses; lint 1 → 0 inside the step) → manifest (11/11) → seat → ritual (13 PASS) → the fold predicted and matched.

NEXT on the ruling: THE COMPILE OF MIDIAN (11b) on 1b's order — the measurements (the tape's state, the callees live: balak, beha, chukat, lev_11,
incense_shekel; the register gate's eight seats), THE DESIGN in this file before any code, the fraction class's probes to FAIL, the docket by the union
rule (Avodah Zarah 5:12 and 75b-76b, Shabbat 64a-b, Nazir 53b-54b, Yevamot 60b, Sanhedrin 106a-b + the link rows), the types, the runner, the tape, every
gate with THE REGISTER GATE --strict at the gates step, the sweep — before chapter 32, never the next reading first.
'''

STATE = '''
═══ COMPACTION POINT #145 (2026-09-12 — written at THE NUMBERS WALK sitting 11's close, the first sitting of the new thread; MIDIAN 31:1-54 READ AND FROZEN; NUMBERS 1:1-31:54 READ, 27 BY THE TENT; 1:1-30:17 COMPILED AND ON THE TAPE; 31 NOT YET COMPILED; A CLEAN COMPACTION POINT) ═══
STATE: 206 frozen units (205 + 1), standing 2114 (2103 + 11 as predicted), hash 8b8fff1fa28953af UNMOVED; 52 runners, 57 daemons, the sweep 52/52 at 6,045 UNMOVED (no runner changed); the journal gate and the register gate GREEN as at 10b's close; RUN (1246, 60, 52, 0, 12, 1470, 28, 302, the four pairs, 114). LAST COMMIT a42f518; UNCOMMITTED: sittings 8 through 10b's paths and this sitting's (logic/units/num_31_midian.yaml frozen; logic/oral_triage/num_31_midian_2026-09-12.md NEW; logic/oral_audit/manifests/num_31_midian_claims.json NEW; logic/py_units/num_31_midian.py NEW + ALL_UNITS.py; the html page and the indexes; logic/corpus/CORPUS_TRUTH.py (206, 2114); logic/glosses/word_gloss_overrides.yaml (the chapter's rows); STAMP_LEDGER.md; NUMBERS_WALK.md; COMPILE_DEBT.md; MIDDOT.md; RESEARCH_LOG.md; THE_STEPS.md; THE_BRIEFING.md; World/RESUME.md; this doc) — commit only on "commit push" (the NEVER-COMMIT set and the staging-by-exclusion form as before; ARCHITECTURE excluded).
THE SITTING (the owner: "ok go" after the recovery-file rereads; NUMBERS_WALK.md "Sitting 11"): chapter 31 read as ONE draft (num_31_midian 31:1-54; 32:1 the next draft's) from the forms copied into the new scratchpad: the Sifrei's TWO piskaot 157-158 BY POSITION (12 rows, every head checked against its rows' own citations by script; NO row from 31:25 to 35:8 — 165 verses silent, computed; THIRTEEN defects read in both files — R. Akiva's arm REVERSED, an ancestor INSERTED against the row's own proof text, the Talmud and the Mishnah SUPPLIED, "we do not punish by inference" DROPPED, three attributions dropped, a name garbled, a citation and a book wrong, a lemma misquoted, an identity's leg backward) + Onkelos whole (54) = 66 sources in one ledger (nine modules; FOURTEEN asserts fell on the first typed pass and one on the second — each a slice index, a token form or a seat outside the Torah, retyped from the leg print; no cut miss; lint 1 → 0 inside the writing step); 11 claims MT31A verified 11/11 and labeled (Numbers 336, debt 0), 11 operators seated, the ritual COMPLETE (13 PASS; the 206th unit), the corpus rebaked once (206, 2114, hash unmoved — predicted); THE PARSER MEASURED FIRST — right on the muster, the kings, the schedule, the spoil's census, the halves, the tributes, the shekels; SILENT on the ratio's denominator at 31:28, 31:30, 31:47 (THE FRACTION CLASS "one of the N" — six Bible seats measured, R29's named-and-left holding for the compile); THE CROWNS: THE COMMAND AND ITS RUN SHARE THE WORD ("the Midianites" at 25:17 and 31:2 alone), the ink's own product (1,000 × 12; R. Yishmael's 24,000 the doubling twice), THE TRUMPETS' ONE NARRATIVE SEAT IN THE TORAH (10:9's war clause run), Joshua 13:21-22's three deltas and the ass's sword closed at Balaam's death, the tribute-word's six Bible seats all here, Phinehas retelling 31:16 at Joshua 22:17, JABESH-GILEAD RUNNING 31:17-18 with its number and its phrase, the six metals and sack-for-goat-work, Eleazar speaking the heifer's statute, THE ARITHMETIC EXACT (÷ 2, ÷ 500) AND THE LEVITES' SHARE UNWRITTEN (8,400 computed), THE OFFICERS' GOLD RUNNING EXODUS 30:16'S OWN SIX WORDS, the half-shekel's spelling and phrase in the division, the store's six Strong's homonyms overridden in the display layer; twelve case-law entries in MIDDOT.md; MOVE_CATALOG unchanged.
THE RECORDS: NUMBERS_WALK.md "Sitting 11"; the ledger, manifest and py rendering; MIDDOT.md's twelve entries; RESEARCH_LOG.md's entry; COMPILE_DEBT.md's sitting-11 box (a)-(n); STAMP_LEDGER's row; THE_STEPS' sitting-11 paragraph; THE_BRIEFING's scoreboard bullet; the gloss override rows; World/RESUME.md; memory (numbers-in-order-ruling.md, MEMORY.md, step9-exam-era.md's lessons head); this entry.
NEXT on the ruling: SITTING 11b — THE COMPILE OF MIDIAN on 1b's order (COMPILE_DEBT's sitting-11 box (a)-(n): the measurements first — the tape's state, the callees live (balak's commanded debit and balaam_death row, beha's trumpets debit, chukat's water and schedule, lev_11's vessels, incense_shekel's ransom cells, bamidbar's charge), the register gate's eight chapter-31 seats declared NONE; THE DESIGN in NUMBERS_WALK.md before any code — the cells (the vengeance and the muster, the war and the kings, the spoil, the sentence, the purification, the kashering rule, the division, the tribute and the Levites' share, the officers' gold), the DATA rows (24,000 / 12,000; Levi in or out; the court or the four penalties; the whitening and the boiling), the daemon law_midian with given_at and installed_by (Eleazar's statute a THIRD form — the priest's voice citing Moses — decided at the types step), the tape lines page_order after chapter 30's with no marker, the checkpoints CX1-CX9 (the Midian debit closed by value at 31:7; the sword clause closed at 31:8; the trumpets' debit run; the four totals, the halves and the tributes as CHECK cells; the receipts' four seats; the ransom's call), THE PREDICTION'S ARITHMETIC for RUN / CENSUS / PLACEMENT; THE FRACTION CLASS's probes to FAIL FIRST (R29 retyped; 31:28, 30, 47; Ecclesiastes 7:28, Ezekiel 45:15, Nehemiah 11:1) then the parser taught and the corpus diff read; the docket by the union rule (Avodah Zarah 5:12 + 75b-76b, Shabbat 64a-b, Nazir 53b-54b, Yevamot 60b, Sanhedrin 106a-b, Sotah 43a, Sanhedrin 54a / Makkot 5b + the link rows); the types by script; the gates to FAIL; the runner (cold_run_midian.py, the honest-pairing guard, the INK block exec'd from the sequence file, the tuples PREDICTED BY SCRIPT); the recorder; the stitcher; the literals and the checkpoints typed into cold_run_sequence.py; the tape run; the probe gates; the daemon and dependency gates; the journal gate; THE REGISTER GATE --strict (the eight seats paid: each key AND body deleted); the sweep in the background; the records), THEN CHAPTER 32 — Gad and Reuben's reading — never the next reading first.
POST-COMPACTION REREADS (mandatory, first sitting): the recovery file logic/pre_logic_methods_2026-07-28/RECOVERY_new_thread_2026-09-12.md (its section 5 THE COMPILE SITTING) + numbers-in-order-ruling.md + this entry + NUMBERS_WALK.md "Sitting 10b — AS BUILT" (the compile's form) + NUMBERS_WALK.md "Sitting 11" (this reading's record and the owed list) + THE_STEPS Step 2 + Step 5 + the compiler block; memory's STANDING LESSONS head (the sitting-11 paragraph first); before the gate's step: THE_LOOP.md "THE REGISTER GATE"; at the types step: daemon_dispositions.yaml's installed_by values. WATCHES: as #144's + THE FINAL LETTER IS ITS OWN CODE POINT + THE TOKEN SET IS THE PRINT'S + THE ARTICLE IS PART OF THE TOKEN + THE LEG DIAGNOSTIC FIRST + THE FRACTION CLASS's read form decided at the design (a Fraction(1, 500) beside the [1], or [1, 500] — the design's choice, the probes typed from it) + THE TRUMPETS' DEBIT WITH NO SOUNDING NARRATED + ELEAZAR'S installed_by FORM + THE FORMS COPIED, NEVER RETYPED FROM MEMORY.
'''

RESUME = '''SITTING 11 DONE 2026-09-12 (MIDIAN 31:1-54 READ AND FROZEN; NUMBERS_WALK.md "Sitting 11"; the owner: "ok go" after the recovery-file rereads in a new thread): the Sifrei's two piskaot 157-158 by position (12 rows, every head checked against its rows' own citations; NO row from 31:25 to 35:8 — 165 verses silent; thirteen defects read in both files — an arm reversed, an ancestor inserted, a rule about rules dropped) + Onkelos whole (54) = 66 sources in one ledger (fourteen asserts fell on the first typed pass, one on the second — retyped from the leg print; no cut miss; lint 1 → 0 inside the step); 11 claims verified and labeled, 11 operators seated, the ritual COMPLETE → 206 units, standing 2114, hash unmoved (predicted); THE PARSER right on the spoil's census, the halves, the tributes and the shekels, silent on "one of the five hundred / fifty" (the fraction class, six Bible seats, named for the compile); the command and its run sharing "the Midianites"; the trumpets' one narrative seat; Joshua 13's retelling; Jabesh-gilead running the sentence; the arithmetic exact and the Levites' share unwritten (8,400 computed); the officers' gold running Exodus 30:16's six words; the store's six homonym glosses overridden in the display layer. NEXT: 11b — THE COMPILE OF MIDIAN (COMPILE_DEBT's sitting-11 box; the fraction class taught first; the register gate's eight seats paid), THEN chapter 32 — never the next reading first.
'''

STEPS = '''SITTING 11 — MIDIAN, Numbers 31:1-54 (2026-09-12, on Brian's "ok go" after the recovery-file rereads in a new thread; World/step9/NUMBERS_WALK.md
"Sitting 11"). The chapter read as one draft (32:1 the next draft's) on Onkelos whole and the Sifrei's two piskaot by position — 66 sources, one
ledger, coverage computed, no cut miss, the lint clean after one reworded gloss; every head checked against its rows' own citations by script (no
mistyped head here), and the shelf found SILENT from 31:25 to 35:8 — 165 verses with no row, the division, the tribute, the census of the spoil and
the officers' gold read on the translation alone; the two files read against each other at every row — the English reversed R. Akiva's arm on the
tribe of Levi, inserted Jethro where the Hebrew's own proof text is Joseph's sale, supplied the Talmud's four death penalties for "by a court" and the
Mishnah's whitening-and-boiling for one list, dropped the rule "we do not punish by inference" and three attributions; the Hebrew misquoted a lemma
and ran an identity's leg backward. The parser measured first: right on the muster, the five kings, the schedule, the spoil's four totals, the two
halves, the four tributes and the 16,750 shekels; silent on the ratio's denominator — "one soul of the five hundred", "one held of the fifty" — the
fraction class "one of the N", six seats in the Bible measured, named for the compile. The finds, computed: THE COMMAND AND ITS RUN SHARE ONE WORD —
"the Midianites" with the article stands twice in the Bible, at the command to harass them and at the vengeance; a thousand to a tribe twice over is
1,000 × 12 = 31:5's own twelve thousand (R. Yishmael reads the doubling twice, 24,000); the trumpets of alarm in Phinehas's hand are the trumpets'
ONE narrative seat in the Torah — the war clause of chapter 10 run; Joshua 13 retells the five kings as Sihon's princes and Balaam as the soothsayer,
and the sword Balaam wished against his ass is the sword he dies by; the tribute-word's six Bible seats are all this chapter's; Phinehas himself
retells "the plague in the congregation of the LORD" at Joshua 22:17; JABESH-GILEAD runs the sentence of 31:17-18 with its number and its phrase;
Eleazar speaks the heifer's statute in the priest's mouth, and the six metals stand in one verse; THE ARITHMETIC IS EXACT — the totals halve, the
halves divide by five hundred to the tributes — and the Levites' one-of-fifty is never given as a number (8,400 heads, computed); THE OFFICERS' GOLD
RUNS THE HALF-SHEKEL'S OWN WORDS — the sum taken, none missing, "to atone for our souls", "a memorial for the children of Israel before the LORD" —
Exodus 30:16's six words in another order. Eleven claims verified and seated, the ritual complete: 206 units, standing 2114, hash unmoved, the fold
predicted and matched; the store's six homonym glosses (the sword "drought", the prey "jaws", the wrath "crack-off") overridden in the display layer,
never in the frozen unit. Honest catches: fourteen asserts fell on the first typed pass and one on the second — slice indices, token forms, the final
letter of "armed" that a regex on plain letters missed, a phrase's seats outside the Torah — each retyped from the leg print. Next: the compile (11b)
— the Midian debit closed by value, Balaam's death closing the sword clause, the trumpets' debit run, the heifer's water by call, the kashering rule a
new cell, the fraction class taught to the parser first, the division and the tribute as computed cells with the arithmetic as checks, the officers'
gold by call into the half-shekel engine, the register gate's eight seats paid — then chapter 32, never the next reading first.

'''

BRIEF = '''- **MIDIAN READ AND FROZEN — SITTING 11 DONE: THE COMMAND AND ITS RUN SHARE ONE WORD, THE SPOIL'S ARITHMETIC IS EXACT AND THE LEVITES' SHARE IS NEVER WRITTEN, THE OFFICERS' GOLD RUNS THE HALF-SHEKEL'S OWN WORDS, AND THE SHELF FALLS SILENT FOR 165 VERSES** (2026-09-12, on your "ok go" in the new thread; World/step9/NUMBERS_WALK.md "Sitting 11"). Chapter 31 read as one unit on Onkelos whole and the Sifrei's two piskaot by position (66 sources, one ledger, no cut miss); every head checked against its rows' own citations by script; the two files read against each other at every row — the English reversed an arm, inserted an ancestor, supplied the Talmud and the Mishnah, dropped the rule "we do not punish by inference". The parser: right on the muster, the kings, the schedule, the four totals, the halves, the tributes and the shekels; silent on "one of the five hundred" — the fraction class, six seats in the Bible, named for the compile. The finds: "the Midianites" stands twice in the Bible — the command and the vengeance; the trumpets' one narrative seat in the Torah; Joshua 13's retelling of the kings and Balaam; Jabesh-gilead running the sentence; the totals halve and the halves divide by five hundred exactly, and the Levites' 8,400 is computed, never written; the officers' gold speaks Exodus 30:16's six words. Eleven claims verified and seated, the ritual complete, 206 units, standing 2114, hash unmoved; the compile next.
'''

DEBT = '''
## SITTING 11 — MIDIAN'S READING (2026-09-12; NUMBERS_WALK.md "Sitting 11"; logic/oral_triage/num_31_midian_2026-09-12.md; the unit num_31_midian FROZEN) — OWED
## TO THE COMPILE (11b, on 1b's order with the register gate at the gates step): (a) THE MIDIAN DEBIT CLOSED — the Balak runner's commanded
## 'harass_the_midianites' on israel_people (25:17) closed BY VALUE at 31:7's receipt "as the LORD commanded Moses" (the first of the chapter's four; the
## 7b lesson: a close without a value takes another runner's entry); (b) BALAAM'S DEATH — 31:8 closes the ass's sword clause (the balak runner's
## balaam_death row, two settings: by the sword at Midian / Rav's four modes); the five kings' deaths (Zur Cozbi's father — the registry's zur; the other
## four new or a party); Joshua 13:21-22's retelling a RUN_CITATION with its three deltas; (c) THE TRUMPETS' DEBIT — the beha runner's open trumpets debit
## (10:9's war clause) RUN at 31:6 "the trumpets of alarm in his hand" with NO SOUNDING NARRATED: the debit's class declared from the print (a run by
## carrying, or left open — the design decides, 2 Chronicles 13:12 the phrase's other seat); (d) THE MUSTER — a count cell: 1,000 × 12 = 12,000 (31:5),
## R. Yishmael's 24,000 a DATA setting (the doubling twice), Levi in or out a data row (the Hebrew "include", the English "exclude"); "were delivered" the
## three readings as data; (e) THE SENTENCE — the case kinds from 31:17-18 (every male among the little ones; every woman who has known a man; the little
## ones among the women kept) against Deuteronomy 20:13-14's war law (NOT COMPILED — OWED or PARAMETER at the census) and 21:10-14's captive woman (forward);
## Judges 21:10-12 the RUN_CITATION (12,000 sent; the phrase; 400 kept); the Sifrei's "fit for intercourse" and R. Shimon ben Yochai's proselyte under three
## as data rows; the a-fortiori refused on a penalty a rules-about-rules row (Sanhedrin 54a, Makkot 5b); (f) THE PURIFICATION BY CALL into the heifer runner
## (chukat: the water of separation, the third-and-seventh-day timers, the sword's seven days at 19:16, the camp entry vs 19:19's evening) — the seven days
## outside the camp a TIMER on the warriors; "you and your captives" the captives' sprinkling; the four materials by CALL into the carcass runner (lev_11:
## Leviticus 11:32's list, sack for goat-work the delta — spun and woven the Sifrei's data); (g) THE KASHERING RULE a NEW CELL — the six metals (tin's one
## Torah seat, lead's two), "everything that comes into the fire through the fire, and with the water of sprinkling; what does not, through water" — Mishnah
## Avodah Zarah 5:12 and Avodah Zarah 75b-76b (the vessels of Midian — the whole sugya's seat) its docket; the whitening / boiling / rinsing / immersion as
## data rows (the English's split is the Mishnah's, the Hebrew's one list the Sifrei's); Eleazar's statute "which the LORD commanded Moses" (31:21) —
## installed_by a THIRD FORM beside boot and the verse: the priest's voice citing Moses (decided at the types step; the Sifrei's three readings data);
## (h) THE FRACTION CLASS TAUGHT FIRST — census_probes R29 ("one held of the fifty" UNMOVED [1]) retyped to FAIL with 31:28, 31:47, Ecclesiastes 7:28,
## Ezekiel 45:15 and Nehemiah 11:1 (read [1, 9] — the nine parts read, the ten not) beside it; the read form decided at the design (Fraction(1, 500) beside
## the one, or the pair); the corpus diff read verse by verse after the rule; (i) THE DIVISION — the halving cell (31:27; "those who took the war" vs the
## congregation), THE TRIBUTE cell (one of five hundred of the warriors' half to the priest — "the LORD's heave-offering", the half-shekel's phrase), THE
## LEVITES' cell (one of fifty of the congregation's half — "who keep the charge of the tabernacle", 1:53's charge by CALL into bamidbar; Jerusalem Talmud
## Terumot 4:3's "one of fifty" a data row if on the local shelf); THE ARITHMETIC AS CHECK CELLS — the four totals ÷ 2 = the halves (both seats), the halves
## ÷ 500 = the tributes (675 / 72 / 61 / 32 = 840), the Levites' UNWRITTEN shares computed (6,750 / 720 / 610 / 320 = 8,400, ten times the priest's), every
## total a multiple of a thousand; the soldiers' private plunder (31:53) outside the count; (j) THE REGISTER GATE'S EIGHT SEATS PAID from the print — the
## receipts 31:7 (CLOSE — the Midian debit), 31:31 / 31:41 / 31:47 (the division's command 31:26-30 and its runs: a spec/run pair), the count lines 31:35,
## 31:36, 31:40, 31:46 (the spoil's persons are captives, not Israel's population — the class the print gives; each paid seat's KEY AND BODY deleted);
## (k) THE OFFICERS' GOLD BY CALL into the half-shekel engine (incense_shekel: the count taken with none missing, "to atone for our souls" — Exodus 30:15-16's
## words; "a memorial before the LORD" — 30:16's; no_plague_at_counting / half_shekel_owed the cells to read) — a REFERENCE by the shared words; the five
## ornaments and the 16,750 shekels a ledger value on the tent; Shabbat 64a-b the docket (the kumaz, the clasp; the atonement "for our souls"); (l) THE TAPE —
## the chapter undated: its lines page_order after chapter 30's line at (40, 6, 1), no marker; "afterward you shall be gathered to your people" a SEQUENCE
## constraint — Moses' death after the war (a checkpoint at Deuteronomy 34); the events: the command (speech), the muster and the sending (acts), the war
## (act — closes the debit), the kings and Balaam killed (act), the spoil brought (act), the wrath (speech), the sentence (speech), Eleazar's statute (speech —
## a law), the division (speech), the runs (acts with receipts), the gold (act); the entities midian, balaam, zur, eleazar, pinchas existing; (m) THE EDGES
## the census will demand — balak (the debit, Balaam, Zur, the plague, "the matter of Peor"), beha (the trumpets), chukat (the heifer's water, the schedule,
## the sword), lev_11 (the vessels), incense_shekel (the ransom), bamidbar (the charge), naso? (the sotah's "treachery against the LORD" — 5:6), Deuteronomy
## 20:13-14 and 21:10-14 (not compiled — forward), Judges 21 and Joshua 13 (run citations), 1 Samuel 30:24-25 and Joshua 22:8 (OBSERVED at the reading — no
## teacher on the declared shelf: no link, or a labeled HYPOTHESIS); (n) THE DISPLAY LAYER, NOT THE COMPILE'S — chapter 19's four "sin" glosses of the
## purify-verb (19:12 ×2, 13, 20) carry the same Strong's homonym as 31:19-23's: override rows owed at a display sitting.
'''

RESEARCH = '''
## 2026-09-12 — MIDIAN'S READING (THE NUMBERS WALK sitting 11): THE EXPORT'S TWO FILES AGAINST EACH OTHER AT TWELVE ROWS — AN ARM REVERSED, AN ANCESTOR
## INSERTED, THE TALMUD AND THE MISHNAH SUPPLIED, A RULE ABOUT RULES DROPPED; THE SHELF SILENT ON 165 VERSES; THE FRACTION CLASS'S SIX SEATS; THE STORE'S
## SIX STRONG'S HOMONYMS; AND THE INK'S OWN CHECKSUMS ON THE SPOIL

Numbers 31:1-54 read (logic/oral_triage/num_31_midian_2026-09-12.md; NUMBERS_WALK.md "Sitting 11"; the unit num_31_midian frozen, 206 units). Every finding
computed on the bytes (midian_ink.py's asserts; midian_measure1.py's print).
1. THE SIFREI'S HEADS CHECKED AGAINST THE ROWS' OWN CITATIONS BY SCRIPT: piskaot 157 (31:1) and 158 (31:22), twelve rows, each row's first citation its own
   verse in order — no mistyped head in this chapter (ROW_CITES); the next head 159 is 35:9: NO ROW FROM 31:25 TO 35:8 — 165 verses (31:25-54 thirty, 32 forty-two,
   33 fifty-six, 34 twenty-nine, 35:1-8 eight) with no row of the spine: the fifth silent stretch of the walk.
2. 157:3 — THE ENGLISH REVERSES AN ARM: the Hebrew reads "24,000 — the words of R. Yishmael; R. Akiva says 12,000; why 'for all the tribes of Israel'? TO INCLUDE
   the tribe of Levi"; the English drops R. Yishmael's name, gives R. Akiva "to EXCLUDE the tribe of Levi", and cites "and there were handed over" as his proof
   where the Hebrew cites "for all the tribes you shall send". A new defect class beside the reversed frame of 123:1 (Chukat): the arm itself reversed.
3. 157:4 — THE ENGLISH INSERTS AN ANCESTOR AGAINST THE ROW'S OWN PROOF: "his mother's father" is proved in the Hebrew by Genesis 37:36 "and the Medanites sold
   him to Egypt" — Joseph (Phinehas's mother of Putiel's daughters, Exodus 6:25); the English inserts "(Yithro, viz. Shemot 2:16)", a citation the Hebrew lacks;
   and the proof text's own word is "the MEDANITES" — Keturah's other son (Genesis 25:2 names Medan and Midian as brothers), where 37:28 has "Midianite men,
   merchants": the Sifrei reads the brothers as one, the ink keeps them two.
4. 157:5 — THE ENGLISH SUPPLIES THE TALMUD: R. Natan's Hebrew "by a COURT they killed him" (Joshua 13:22's "among their slain") becomes "with the four judicial
   death penalties" (Sanhedrin 106b's Rav); "Abba Chanin in the name of R. ELAZAR" becomes "R. Eliezer"; the Hebrew assigns the idolatry to "their cities in their
   dwellings" and two readings to "their castles" — the English puts the idolatry on the castles, Onkelos's assignment ("their houses of worship").
5. 157:6 — A RULE ABOUT RULES DROPPED: the Hebrew reads 31:17's second "kill" two ways — R. Yishmael's "to close the subject", and "the one fit for intercourse is
   killed — the one who has lain all the more? If you say so you punish by inference; therefore 'kill' is written, to teach that WE DO NOT PUNISH BY INFERENCE";
   the English keeps the first, drops the second whole with R. Yishmael's name, and cites "(31:7)" for 31:17.
6. 157:7 — the English replaces the Hebrew's conclusion ("they do not come into the category of uncleanness") with "(see Chukath #126)". 157:9 — the English drops
   R. Yoshiyah's name on "in the name of its sayer" (Esther 2:22). 158:2 — the English supplies Mishnah Avodah Zarah 5:12's split (knives, spits and grills
   whitened; pots and kettles boiled) where the Hebrew lists five vessels under "comes into the fire" with no split, and gives one a-fortiori for the Hebrew's two.
7. 157:8 — THE IDENTITY'S LEG RUN BACKWARD IN THE HEBREW: "as the garment said THERE (Leviticus 11:32) has every goat-work like sack, so the garment HERE" — but
   "work of goats" is 31:20's word, not Leviticus's; the English runs "as here, so there", the direction the ink allows.
8. 158:3 — THE HEBREW MISQUOTES A LEMMA AND A CITATION: "therefore it says 'and they shall wash their garments'" is 8:7's form (the Levites), not 31:24's "and you
   shall wash your garments"; "(19:19) 'slain by the sword'" names 19:16's phrase (19:19 is the row's second proof, "until the evening"); the English cites
   "Vayikra 19:19" for Bamidbar — a book wrong, as sitting 8's Judges for Joshua.
9. THE PARSER'S FRACTION CLASS "ONE OF THE N" — six Bible seats measured before any claim: Num 31:28 "one soul of the five hundred" [1]; 31:30 and 31:47 "one held
   of the fifty" [1]; Ecclesiastes 7:28 "one of a thousand" [1]; Ezekiel 45:15 "one of the flock, of the two hundred" [1]; Nehemiah 11:1 "one of the ten" [1, 9]
   (the nine parts read, the ten not). Named and left at census_probes R29; the compile's probes.
10. THE INK'S OWN CHECKSUMS: 675,000 / 72,000 / 61,000 / 32,000 (840,000, every total a multiple of a thousand); ÷ 2 = 337,500 / 36,000 / 30,500 / 16,000 at both
    seats; ÷ 500 = 675 / 72 / 61 / 32 (840) — exact; the Levites' one-of-fifty NEVER STATED AS A NUMBER — 6,750 / 720 / 610 / 320 (8,400, ten times the priest's)
    computed; 16,750 shekels; the receipt "as the LORD commanded Moses" at four seats in the chapter — the most of any Numbers chapter (41 seats in the Bible;
    Exodus 39 and 40 seven each, Leviticus 8 five).
11. THE STORE'S GLOSSES ARE STRONG'S HOMONYMS AT SIX WORDS: "in-drought" for the sword (31:8 — the gloss's six Torah seats all "by the sword"), "the-transitively-
    -the-jaws" for the prey (the word's Torah seats all Numbers 31's), "and-crack-off" for the wrath-verb (five Torah seats), "sin" for the reflexive purify-verb
    (31:19, 20, 23 — and chapter 19's four seats, owed), "and-trample" for the washing of garments (twenty Torah seats), "seasons" for the tent of MEETING (31:54 —
    the appointed-times homograph at 142 seats, so by reference only). Rows added to logic/glosses/word_gloss_overrides.yaml (by_gloss where every Torah seat is
    the one word, by_ref where not); the frozen unit and the machine truth untouched (the display layer's law).
12. THE RETELLINGS MEASURED: Joshua 13:21-22 (the five kings "the princes of Midian... the princes of Sihon, dwelling in the land"; Balaam "the SOOTHSAYER"; "to
    their slain" for 31:8's "upon their slain" — the word's three Bible seats); Joshua 22:17 (Phinehas: "the plague in the congregation of the LORD" — the clause's
    only other seat); Judges 21:10-12 (twelve thousand sent; "every male and every woman who has known lying with a male you shall devote"; four hundred virgins —
    "lying with a male" at this chapter's three seats and Jabesh-gilead's two alone in the Bible); Judges 8:5, 12, 26 ("the kings of Midian" — Gideon's two;
    1,700 shekels of Midianite gold); Exodus 30:16 ("for the children of Israel for a memorial before the LORD, to atone for your souls" — 31:54's six words in
    another order, 31:50's "to atone for our souls"); Exodus 35:22 (the donation's gold list sharing the ring and the kumaz — the clasp); 1 Samuel 30:24-25 and
    Joshua 22:8 (the equal shares — the ink's kin, no row of the declared shelf linking them: observed, not linked).
13. THE TRUMPETS' ONE NARRATIVE SEAT IN THE TORAH: the trumpet-word's Torah seats are 10:8, 9, 10 (the law) and 31:6 (the run) — "the trumpets of alarm" with
    2 Chronicles 13:12 alone; "the Midianites" with the article at 25:17 and 31:2 alone (the command and its run); "the deliver-root" at 31:5 and 31:16 alone in
    the Torah; the tribute-word's six Bible seats all here; the prey-word's six, five here; tin's one Torah seat (31:22), lead's two (Exodus 15:10, 31:22).
'''

MIDDOT = '''- MIDIAN'S CHAPTER (THE NUMBERS WALK sitting 11, 2026-09-12; the Sifrei on Numbers 157-158 on 31:1-24 — no row from 31:25 to 35:8;
  logic/oral_triage/num_31_midian_2026-09-12.md): the Sifrei's own case law read on the chapter's rows —
  · THE NAME READ TWICE AND THE PRIORITY ASKED (157:1): "from the Midianites" — but Moab began (22:4, 22:7)? the old feud read off Genesis 36:35 and the
    parable of the two dogs; the gentilic's letters read as "contended" and "counseled" — the narrative middot's name-reading; the ink's own fact beside it:
    "the Midianites" with the article at the command (25:17) and the run (31:2) alone in the Bible.
  · "ARM" BY THE LEXICAL IDENTITY (157:2): the imperative's one seat fixed by Deuteronomy 3:18's "armed shall you pass over" — I2's lexical form (a word's
    sense from its other seat); "afterward you shall be gathered" read as the plain sequence: Moses' death contingent on the war.
  · THE DOUBLED NUMERAL DISPUTE (157:3): "a thousand to a tribe, a thousand to a tribe" — R. Yishmael reads the doubling twice (24,000), R. Akiva once (12,000,
    the ink of 31:5's own sum; the parser's distributive [1000, 1000]); "for ALL the tribes" the E-class amplifier — to include the tribe of Levi (the Hebrew;
    the English reversed); the passive "were delivered" read for its agent three ways (the men, others, conscription). The export's defects at this row
    (RESEARCH_LOG).
  · "THE HOLY" AND "HIS HAND" BY IDENTITY (157:4): the holy vessels = the ark from 4:20; "in his hand" = his domain from 21:26 and Genesis 24:10 — I2 on a
    common word at two seats; the ancestor by descent (the Hebrew's Joseph, the English's Jethro inserted).
  · THE SECOND NAMING, THE RETELLING FOR THE MODE, THE FRAME FOR A CAUSE (157:5): "the five kings" named again — as one in counsel, one in punishment (the
    "why repeated" form); Balaam's mode read off Joshua 13:22 (R. Natan: by a court — the Hebrew); "Moses and Eleazar went out" read for its cause (the
    youths snatching); "Moses was wroth" — the stigma hangs on the great; "by the word of Balaam" — the counsel spelled out.
  · THE REFUSED A-FORTIORI ON A PENALTY (157:6): "every woman who has known a man" — fit for intercourse, by the "uphold both verses" form on 31:18; the
    second "kill" read two ways: R. Yishmael — a repeated verb CLOSES THE SUBJECT (a structural rule: the paragraph's boundary); the other reading — the
    a-fortiori (the fit one killed, the one who has lain all the more) is barred, for WE DO NOT PUNISH BY INFERENCE (ain onshin min ha-din, the rule about
    rules at Sanhedrin 54a and Makkot 5b): the penalty must be written — the English drops it whole; R. Shimon ben Yochai's proselyte under three from "keep
    alive for yourselves".
  · THE TENT'S STRAW EXCLUDED, THE CAPTIVES LIKENED (157:7): 19:14's "all that is in the tent" — straw and twigs do not enter the category (piska 126's
    exclusion repeated); "you and your captives" — as you are children of the covenant, so your captives, for the sprinkling (an analogy on the pronoun pair).
  · THE FREED-WORD IDENTITY RUN TWO WAYS (157:8): Leviticus 11:32's "skin or sack" against 31:20's "garment, skin, goat-work, wood" — the a-fortiori refused
    both ways ("do we derive from the stringent to be lenient and stringent with it?"), "garment" declared FREED (mufneh — unneeded in its own verse) to form
    the gezerah shavah (the verbal identity): goat-work like sack carried to the creeping thing's law, "spun and woven" carried to the dead's — the band, the
    belt and the ass's girth in, cords and ropes out. The Hebrew's first leg runs backward (goat-work is 31:20's word); the English the way the ink allows.
    The identity's license: the freed word (MIDDOT.md under I2 — Pesachim 66a: no identity of one's own).
  · ANGER BEGETS ERROR AT THREE PLACES, AND "IN THE NAME OF ITS SAYER" (157:9): why Eleazar speaks the heifer's statute — Moses came to anger and to error
    (Leviticus 10:16, Numbers 20:10, 31:14 — R. Elazar; the wrath-verb with Moses as subject stands at Exodus 16:20, Leviticus 10:16, 31:14: two shared),
    or Moses gave him leave, or R. Yoshiyah's attribution rule from Esther 2:22 (the English drops the name) — rules about the lawgiver and the teacher.
  · "ONLY" DIVIDES, AND THE ANALOGY ON A SHARED FEATURE (158:1): the metals as vessels not lumps — Israel's dead and Midian's slain both defile, so both
    defile vessels only (the "you reason" form on a common feature); R. Yose HaGelili: the E-class limiter "only".
  · THE LISTS AS SPECIFICATION, THE IMMERSION BY A-FORTIORI (158:2): the vessels of fire and of water listed (the Sifrei's data channel — "because of the
    gentiles' absorptions"); if what needs no sprinkling needs immersion, what needs sprinkling all the more — I1; the English supplying the Mishnah's
    whitening / boiling.
  · THE TWO-WAY LIKENING OF THE CAMP AND THE EVENING (158:3): the sword unclean seven days from "slain by the sword" (19:16); vessels-man-vessels from the
    garments' washing; 31:24 and 19:19 likened BOTH WAYS (the camp's bar exported, the evening imported) — the likening (hekkesh, no I-code) as the vows'
    footer used it; the Hebrew's misquoted lemma and the English's wrong book (RESEARCH_LOG).

'''

# ---- the gloss override rows (the display layer; by_gloss where every Torah seat of the gloss is the one word, by_ref where it is not) ----
OV = f'{ROOT}/logic/glosses/word_gloss_overrides.yaml'
BYGLOSS = '''  # THE NUMBERS WALK sitting 11 (2026-09-12, Numbers 31): six Strong's homonyms read back off the store — RESEARCH_LOG.md
  "in-drought": "with-the-sword"            # the sword-word: the gloss's six Torah seats are all "by the sword" (Exod 5:3, 22:23; Num 14:3, 14:43, 20:18, 31:8)
  "the-transitively--the-jaws": "the-prey"  # the prey-word's Torah seats are all Numbers 31's
  "transitively--the-jaws": "prey"
  "and-crack-off": "and-was-wroth"          # the wrath-verb at five Torah seats
  "and-trample": "and-wash"                 # the washing of garments at twenty Torah seats

'''
BYREF = '''  "Num.31.54:14": "meeting"          # the tent of MEETING — the seasons-gloss is the appointed-times homograph (142 seats), so by reference only
  "Num.31.19:12": "purify-yourselves"  # the reflexive of the sin-root: to purify oneself (Num 31:19, 20, 23; chapter 19's four seats owed)
  "Num.31.20:11": "purify-yourselves"
  "Num.31.23:11": "shall-be-purified"
  "Num.31.10:6": "castles-their"       # tirotam — the encampment/castle word, not "wall"
  "Num.31.12:11": "the-captives"       # ha-shevi — the captives, not "the exiled"
  "Num.31.26:4": "the-captives"
  "Num.31.19:18": "and-your-captives"
  "Num.31.3:5": "arm-yourselves"       # hechaltzu — not "pull-off"
  "Num.31.5:0": "and-were-delivered"   # va-yimmaseru — not "and-sunder"
  "Num.31.7:0": "and-they-warred"      # va-yitzbe'u — not "and-mass"
  "Num.31.50:9": "armlet"              # etz'adah — Saul's armlet (2 Sam 1:10), not "step-chain"
  "Num.31.50:12": "earring"            # agil — Ezekiel 16:12's earring, not "something-round"
'''
s = open(OV, encoding='utf-8').read()
assert s.count('\nreplace:\n') == 1 and s.count('\nby_ref:\n') == 1 and 'in-drought' not in s and 'Num.31.' not in s
s = s.replace('\nreplace:\n', '\n' + BYGLOSS + 'replace:\n').replace('\nby_ref:\n', '\nby_ref:\n' + BYREF)
open(OV, 'w', encoding='utf-8').write(s)
d = yaml.safe_load(open(OV, encoding='utf-8'))
assert d['by_gloss']['in-drought'] == 'with-the-sword' and d['by_ref']['Num.31.54:14'] == 'meeting' and len([k for k in d['by_ref'] if k.startswith('Num.31.')]) == 13, 'the yaml is parsed before it is trusted'
print('overrides: by_gloss %d, by_ref %d, parsed' % (len(d['by_gloss']), len(d['by_ref'])))

append(f'{ROOT}/logic/findings/STAMP_LEDGER.md', STAMP)
append(f'{ROOT}/World/step9/NUMBERS_WALK.md', WALK)
append(f'{ROOT}/logic/pre_logic_methods_2026-07-28/PROMPT_continue_solo_era_2026-08-06.md', STATE)
append('<world-link>/RESUME.md', RESUME)
insert_before(f'{ROOT}/THE_STEPS.md', '## THE FINDINGS LOOP + THE STAMP LAW (owner-approved 2026-08-31)', STEPS)
insert_after(f'{ROOT}/THE_BRIEFING.md', '## SCOREBOARD (as of 2026-09-12, latest)\n', BRIEF)
append(f'{ROOT}/World/step9/COMPILE_DEBT.md', DEBT)
append(f'{ROOT}/RESEARCH_LOG.md', RESEARCH)
insert_before(f'{ROOT}/logic/MIDDOT.md', '## Exodus block campaign — owner\'s word "Do 3")', MIDDOT)

# ---- memory ----
append(f'{MEM}/numbers-in-order-ruling.md', RESUME.replace('SITTING 11 DONE 2026-09-12 (', 'SITTING 11 DONE 2026-09-12 — THE FIRST SITTING OF THE NEW THREAD, from the recovery file and the copied forms ('))
mi = f'{MEM}/MEMORY.md'; s = open(mi, encoding='utf-8').read()
old = [l for l in s.split('\n') if l.startswith('- [⚠ NUMBERS IN ORDER FROM 1:1](numbers-in-order-ruling.md)')]
assert len(old) == 1
new = ('- [⚠ NUMBERS IN ORDER FROM 1:1](numbers-in-order-ruling.md) — OWNER-RULED 2026-09-09: the chapter walk from 1:1 at the parashah grain (map World/step9/NUMBERS_WALK.md; chapters 9, 15:32-41, 27, 36 frozen at THE TENT and SKIPPED); ⚠ OWNER-RULED 2026-09-10 READ THEN COMPILE PER PORTION, never read ahead; CHAPTER NUMBERS, not portion names. NUMBERS 1:1-30:17 READ, FROZEN, COMPILED AND ON THE TAPE (sittings 1-10b); 31 READ AND FROZEN (sitting 11, 2026-09-12, #145: 206 units, standing 2114, hash unmoved; the Sifrei silent 31:25-35:8; the parser\'s fraction class "one of the N" named for the compile; the register gate\'s eight chapter-31 seats declared NONE). COMMITTED a42f518 (2026-09-11); sittings 8-11 UNCOMMITTED. THE REGISTER GATE (register_census.py --strict) RUNS AT EVERY COMPILE SITTING\'S GATES STEP. NEXT: SITTING 11b — CHAPTER 31\'S COMPILE (COMPILE_DEBT\'s sitting-11 box (a)-(n); the fraction class taught first), then chapter 32\'s reading.')
s = s.replace(old[0], new); open(mi, 'w', encoding='utf-8').write(s); print('MEMORY.md line rewritten: %d -> %d bytes; file %d bytes' % (len(old[0].encode()), len(new.encode()), len(s.encode())))
assert len(s.encode()) < 17000
LESSON = ('⚠ THE NUMBERS WALK sitting 11 — MIDIAN\'S READING (2026-09-12, the first sitting of the new thread, from the recovery file and the copied forms): THE FINAL LETTER IS ITS OWN CODE POINT — a regex on the root\'s plain letters misses the end-form (the final tsadi, the letter\'s end-form, of "armed" in chapter 32): a root census names its final forms (Balak\'s gentilic lesson, now on a verb). THE TOKEN SET IS THE PRINT\'S — the assert typed two spellings where the measure had printed four (bracelet, earring): copy the print\'s token set, never a subset. THE ARTICLE IS PART OF THE TOKEN — tin stands in the Torah only as "the tin"; a bare-stem census returns nothing, and the look-alikes are a verb. THE LEG DIAGNOSTIC, AGAIN — fourteen asserts fell on the first typed pass and one on the second, every one a slice index, a token form or a seat outside the Torah (a phrase in Kings and Chronicles beside Genesis): print every leg (midian_legs.py), retype from the print, scope to the Torah when the claim is the Torah\'s. A HYPHENATED ENGLISH COMPOUND IS FLAGGED BY THE LINT (a gloss "wailing-blast") — reword and regenerate inside the writing step. THE HEADS ARE CHECKED AGAINST THE ROWS\' OWN CITATIONS BY SCRIPT (ROW_CITES — an assert, not a reading). THE TWO FILES ARE READ AGAINST EACH OTHER AT EVERY ROW — the English REVERSED an arm (include/exclude on Levi), INSERTED an ancestor against the row\'s own proof text, SUPPLIED the Talmud and the Mishnah, DROPPED a rule about rules ("we do not punish by inference") and three attributions; the Hebrew misquoted a lemma and ran an identity\'s leg backward: the Hebrew row is the shelf, the English a witness with its own defects. THE SHELF\'S SILENCE IS COMPUTED (31:25-35:8 — 165 verses with no row). THE FRACTION CLASS "ONE OF THE N" MEASURED CORPUS-WIDE BEFORE THE COMPILE (six Bible seats; Nehemiah 11:1 read [1, 9]); the class named and left at R29 holds until the compile teaches it. THE ARITHMETIC IS THE INK\'S OWN CHECKSUM (the totals ÷ 2, the halves ÷ 500, exact) AND THE UNWRITTEN NUMBER IS COMPUTED (the Levites\' one-of-fifty never given: 8,400 heads). THE STORE\'S GLOSSES ARE STRONG\'S HOMONYMS — the sword "drought", the prey "the jaws", the wrath "crack-off", the purifying "sin", the washing "trample", the meeting "seasons": the display override file (by_gloss where every Torah seat is the one word, by_ref where not), never the frozen unit. THE READING SITTING\'S SHAPE HELD FROM THE COPIED FORMS (dump → measure → asserts 14 → 1 → 0 → rows → writer 0 misses, lint 1 → 0 inside the step → manifest 11/11 → seat → ritual 13 PASS → the fold predicted and matched).\n')
insert_after(f'{MEM}/step9-exam-era.md', '## STANDING LESSONS AND WATCHES (moved verbatim from the MEMORY.md index line on 2026-09-07 to keep the index under its size limit; the W4/W3/W2/W1/D9/G/E lesson tail as it stood)\n', LESSON)
print('records written')
