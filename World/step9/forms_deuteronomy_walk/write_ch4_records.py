import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE DEUTERONOMY WALK sitting 2 — CHAPTER 4 (2026-09-16; the owner: "Go" after the rereads): THE RECORDS at the close — the map's "Sitting 2"
# section, the state doc's COMPACTION POINT #185, World/RESUME.md, THE_STEPS' paragraph, THE_BRIEFING's scoreboard bullet and entry, COMPILE_DEBT's
# box (owed to the compile 2b), RESEARCH_LOG's entry, MIDDOT's block (the Sifrei's case law on the chapter), the recovery file's section 33, the
# stamp row, the memory file and the index line (under 17,000 bytes). Every number typed from a print named beside it; every insert on a unique
# anchor asserted present once; the lints before and after. Sitting 1's form (write_deu_records.py).
import os, re, subprocess, sys, yaml
ROOT = _ROOT
SP = os.path.dirname(os.path.abspath(__file__))
MEM = os.path.expanduser('~/.claude/projects/' + os.path.abspath(ROOT).replace('/', '-') + '/memory')
DATE = '2026-09-16'
UIDS = ['deu_04_obey_horeb', 'deu_04_refuge_east']
truth = open(f'{ROOT}/logic/corpus/CORPUS_TRUTH.py', encoding='utf-8').read()
assert 'assert len(W["units"]) == 218' in truth and 'assert len(W["standing"]) == 2191' in truth and "8b8fff1fa28953af" in truth
for u in UIDS:
    rit = open(f'{SP}/ch4_ritual_{u}.out', encoding='utf-8').read()
    assert 'RITUAL COMPLETE' in rit and len(re.findall(r'^PASS', rit, re.M)) == 13 and not re.search(r'^FAIL', rit, re.M), u   # the guard typed from the print: thirteen PASS lines, no FAIL line (a note may name the word)
    assert os.path.exists(f'{ROOT}/logic/oral_audit/manifests/{u}_claims.json') and '  status: frozen' in open(f'{ROOT}/logic/units/{u}.yaml', encoding='utf-8').read()
assert os.path.exists(f'{ROOT}/logic/oral_triage/deu_04_vaetchanan_{DATE}.md') and 'ALL_DONE' in open(f'{SP}/ch4_chain.log', encoding='utf-8').read()
assert 'GATE GREEN' in open(f'{SP}/journal_gate_ch4.out', encoding='utf-8').read() and 'DECLARED 100; DEBT 0; FAILS 0' in open(f'{SP}/register_gate_ch4.out', encoding='utf-8').read() and 'ALL GREEN' in open(f'{SP}/build_world_ch4.out', encoding='utf-8').read()
d_ov = yaml.safe_load(open(f'{ROOT}/logic/glosses/word_gloss_overrides.yaml', encoding='utf-8'))
assert len([k for k in d_ov['by_ref'] if k.startswith('Deut.4.')]) == 81 and len(d_ov['by_ref']) == 414 and len(d_ov['by_gloss']) == 298

def append(path, text):
    s = open(path, encoding='utf-8').read(); assert text not in s
    with open(path, 'a', encoding='utf-8') as f: f.write(text)
    print('appended %d bytes -> %s' % (len(text.encode()), path))
def insert_before(path, anchor, text):
    s = open(path, encoding='utf-8').read(); assert s.count(anchor) == 1, (path, anchor[:40], s.count(anchor))
    open(path, 'w', encoding='utf-8').write(s.replace(anchor, text + anchor)); print('inserted %d bytes before %r -> %s' % (len(text.encode()), anchor[:30], path))
def insert_after(path, anchor, text):
    s = open(path, encoding='utf-8').read(); assert s.count(anchor) == 1, (path, anchor[:40], s.count(anchor))
    open(path, 'w', encoding='utf-8').write(s.replace(anchor, anchor + text)); print('inserted %d bytes after %r -> %s' % (len(text.encode()), anchor[:30], path))

STAMP = ('| 2026-09-16 | deu_04_obey_horeb, deu_04_refuge_east | DELEGATED | FULL RULE | Deuteronomy 4:1-49 derivation 2026-09-16 (THE DEUTERONOMY WALK sitting 2 — CHAPTER 4; the owner: "Go" after the rereads, on the rulings READ THEN COMPILE PER PORTION and CHAPTER NUMBERS NOT PORTION NAMES; the book\'s second reading — chapter 4 as two drafts, the 217th and 218th frozen units): declared reading COMPLETE (one ledger logic/oral_triage/deu_04_vaetchanan_2026-09-16.md, 55 sources — Onkelos 4:1-49 whole and fresh, the Sifrei on Deuteronomy\'s SIX rows citing the chapter found by the scan of the whole export in both files and read fresh, two credited from sitting 1; NO PISKA on the chapter — 30 heads on 3:29, 31 on 6:4; coverage computed by script, missing 0 extra 0; the ink facts computed from the Tanakh DB, the snapshot store and the shelf\'s bytes — every fact an assert, six fell on the first typed pass and were retyped from the leg print, none on the second; every quotation cut by consonants, no cut miss on the ledger; gloss_lint 0), claims DV04A-01..05 and DV04B-01..02 verified 7/7 (every check the word\'s longest store-piece whole), claim_labels_census --strict GREEN (two labels re-closed with their parenthesis), seated as seven WITNESS_READ operators at the claims\' first verses (4:1, 9, 15, 25, 32; 4:41, 44), verify_text GREEN twice (40 and 9 steps, 7 scenarios each), the rituals 13 PASS each, CORPUS TRUTH GREEN (218 units, standing 2191 = 2184 + 7 as predicted, hash 8b8fff1fa28953af UNMOVED), build_world ALL GREEN, the journal gate GREEN (12 kinds, 9,646 rows), the register gate --strict GREEN (DECLARED 100, DEBT 0, FAILS 0). THE PARSER: four number verses read, NO GAP (4:13 [10, 2], 4:41 [3], 4:42 [1], 4:47 [2]). The finds: the shelf\'s silence over the whole chapter and the export\'s third citation form (301:21 unpointed); one law (4:2) and one case (4:25); learn and teach one word (4:10); the tablets plene (4:13); the third telling of the bar with an oath (4:21); the receipt in Moses\' own voice (4:5); the translation\'s fear, Memra and Shekhinah (4:4, 20, 24, 29-30, 33, 36-37, 39), "prepared" for "apportioned" (4:19), the idolaters for the idols (4:28), the miracles for the question (4:34), the Name for "God" (4:32), "see" made plural (4:5); the number switching by verse; the Decalogue\'s image recast (4:16-19); "you were shown" against "that saw" (4:35, 4:3); the creed twice (4:35, 39); the one "created" (4:32); "then Moses set apart" (4:41 — the refuge runner\'s open debit); the two frames (1:1, 4:45) and the speech\'s borders retold (4:46-49); the witnesses\' chain (Sifrei 306:1); the Haggadah\'s row (Sifrei 301:21); the export\'s chapter 5 at thirty verses. Stamp delegated under the AUTO-SEAT ruling; the owner may overrule. |\n')

WALK = '''

## Sitting 2 — CHAPTER 4, Deuteronomy 4:1-49 (2026-09-16; the owner: "Go" after the rereads, on the rulings READ THEN COMPILE PER PORTION and CHAPTER NUMBERS): the reading and the units

THE DRAFTS: two cover the chapter exactly — computed from the Tanakh DB's verse table: 49 of 49 verses, missing 0 — deu_04_obey_horeb 4:1-40,
deu_04_refuge_east 4:41-49 (the next draft, deu_05_decalogue, opens at 5:1; the step ids STEP_Dt_4_<v>; the scenarios in the tree form before the
seat; each step block carries two "comment" lines — the step's and its map's — 84 and 22, counted from the print). The portion's grain crosses at
3:23 (the second portion runs 3:23-7:11); the chapter is the sitting's unit, per the ruling. Read in ONE pass, one ledger. The forms: sitting 1's
scripts folded and edited (ch4_dump0.py — the three first-pass scripts in one; ch4_measure1.py, ch4_measure2.py; ch4_ink.py with assert_driver.py
and deu_legs.py; ch4_rows_onkelos_a/b.py; ch4_rows_sifrei.py; write_ch4_ledger.py; ch4_patch_overrides.py; write_ch4_manifest.py; seat_ch4.py;
ch4_chain.sh; copy_ch4_forms.py; write_ch4_records.py), copied at the close into World/step9/forms_deuteronomy_walk/ with their prints.

THE SHELF, BY POSITION (ch4_ink.py's asserts): THE SIFREI ON DEUTERONOMY HAS NO PISKA ON THE CHAPTER — piska 30 heads on 3:29 (two rows), piska
31 on 6:4 (ten rows); the heads by chapter: chapter 1's twenty-four, chapter 3's four (26, 28, 29, 30), chapter 4's none (computed on all 357 heads).
THE "FOUND BY POSITION" CLAUSE is therefore the whole of the spine here: the whole export scanned in both files — SEVEN Hebrew rows cite chapter 4
("(דברים ד n)" — "Deuteronomy 4:n" in Hebrew letters), EIGHT English ("(Dt.4:n)"): 30:2 (on 3:29; 4:1), 37:9 (on 11:10; 4:48), 48:2 (on 11:22;
4:9), 49:2 (on 11:22; 4:24), 148:8 (on 17:2; 4:19), 306:1 (on 32:1; 4:26), 323:1 (on 32:29; 4:44), and the English's alone 301:21 (on 26:5;
4:34) — THE EXPORT'S THIRD CITATION FORM: that row's Hebrew is UNPOINTED and abbreviated, cites nothing in parentheses, and its English cites
"(Devarim 4:34)" with a space (sitting 1 measured "Dt." 3,292 times and "Deut." once); the late piskaot are another stratum of the export. No
"ibid" candidate. THE PRIOR READS (the strict row form over every ledger, 205 prior rows): 30:2 read FRESH at sitting 1 (its last words the pointer
to 4:1 — "you are new, the past is forgiven") and 37:9 credited there — CREDITED here with a quick look; the six others FRESH in both files; no
ledger had read an Onkelos row of chapter 4; twenty ledgers NAME a verse of it (the refuge runner's two and the opening speech's docket among them).
Onkelos Deuteronomy's export: 956 verses against the DB's 959 — CHAPTER 5 IS THE ONE CHAPTER WHERE THEY DISAGREE (thirty verses in the export,
thirty-three in the DB: the Decalogue's division), measured here for the next sitting; chapter 4 at 49 in both.

THE READING (the modules): ch4_dump0.py the first pass — the shelf's heads around the chapter, the scan of both files for the chapter's citations
(the rows dumped whole), the Onkelos dump per verse (the Hebrew, the morphology, the lemmas, the store's glosses, the English, the Aramaic), the
parser on every verse, the case tokens, the frames, the narrative verbs, the imperatives, the names, the second-person number per verse, the register
gate's lines, the prior reads, the drafts, the store's token counts and glosses; ch4_measure1.py the second — fifty-four retellings DIFFED token by
token against their first tellings (Baal-peor / Numbers 25; Horeb / Exodus 19-20, 24, 31, 34 and 5:4-26; the bar / 1:37, 3:26, Numbers 20:12; the
exodus formulas / 26:8, 7:19; the cities / Numbers 35, 19:4, Joshua 20:8, 21:36; the frame / 1:1, 1:4, 6:20; the borders / 2:36, 3:8, 3:17, Joshua
12:3), a hundred and ninety phrase censuses over the whole DB, the Onkelos renderings' seats over the whole book, the English's bracketed
supplements, a hundred and thirteen store gloss families; ch4_measure2.py the third — the leftover seats, the pointed forms the rows quote, the
Aramaic forms with their prefixes, the override file's existing values; ch4_ink.py the ink with every fact an assert (assert_driver.py: SIX fell
on the first typed pass — the export's chapter 5 at thirty verses not thirty-three; the step blocks' two "comment" lines; "and lest" (4:9, 4:19)
outside the case-token list; the DB's alphabetical book order (Deuteronomy before Exodus) in a list typed canonically; a substring census reading
"and rules" inside another word at 32:14 (onk_tok, not onk_seats, for a token); a family already rewritten at sitting 1 ("and-you-came-near");
each retyped from the leg print (deu_legs.py), none on the second pass); the piece-wise cutters HP / AP / SP_ (no cut miss on any rows file's
load — the Sifrei cuts fell SEVENTEEN times at once for being typed POINTED: the cutter takes consonants, the row prints the shelf's pointed bytes);
ch4_rows_onkelos_a.py (4:1-24) and _b.py (4:25-49) the 49 rows; ch4_rows_sifrei.py the six fresh rows and the two credits; write_ch4_ledger.py →
ONE ledger logic/oral_triage/deu_04_vaetchanan_2026-09-16.md (55 sources: Onkelos MATERIAL 40 / CONTEXT 9; the Sifrei MATERIAL 6; two rows
credited; coverage computed, missing 0, extra 0; 103,547 bytes; gloss_lint 0 on the first write); ch4_patch_overrides.py the display layer's rows
(EIGHTY-ONE by reference with the token named beside each — the indices computed from the store's own rows, never typed — and SIXTY-THREE by
gloss; the families censused first; the rows read from the ink module's own lists; by_ref 414, by_gloss 298 after).

THE INK, COMPUTED (the measurement passes FIRST, the asserts typed from the print):
- THE PARSER MEASURED FIRST: FOUR number verses in 49 read, NO GAP — 4:13 "the ten words … two tablets" [10, 2] (the construct "two" marked ^),
  4:41 "three cities" [3], 4:42 "one of these cities" [1], 4:47 "the two kings" [2]; no ordinals ("the former days" the adjective, "swore" not
  "seven"); the same phrases read the same at their other seats (10:4 [10]; Exodus 34:28 [40, 40, 10]; 19:7, 19:9 [3]; 19:5, 19:11 [1]). The
  tokens 813; the store's tokens the DB's at every verse (no written-and-read pair).
- THE FRAMES AND THE REGISTER: ONE divine frame — "and the LORD spoke to you" at 4:12 (the Bible's one seat of the form); NO "saying"; the chapter
  in the SECOND PERSON, SWITCHING NUMBER BY VERSE — singular only at 10, 19, 24, 30-33, 35-40; plural only at 2, 4, 6, 8, 11-16, 20, 22, 26-28;
  both at 1, 3, 5, 9, 21, 23, 25, 29, 34; the third person at 7, 17, 18 and the frame 41-49; "the LORD your God" eleven singular, three plural;
  the Name twenty-nine tokens; the imperatives hear (4:1), see (4:5), take heed (4:9; plural 4:23), God's assemble (4:10), ask (4:32); the
  prohibitions add / diminish (4:2), lest you forget (4:9, 23), lest you corrupt (4:16), lest you lift your eyes (4:19), not prolong (4:26). THE
  CASE TOKENS: "for" fifteen (reasons), "lest" three and "and lest" two, "or" three, NO "if" — ONE LAW (4:2, without a case token) and ONE CASE
  (4:25's "when you beget sons"). Moses named at 41, 44, 45, 46 only. THE REGISTER GATE: Deut 4:5 NONE declared ("the book not read" — the receipt
  "as the LORD my God commanded me", paid at the compile), Deut 4:45 DAEMONS green (the block (Deut 1:1, Deut 4:45] since 1b).
- THE CROWNS (seventeen, the ledger's finds): THE SHELF'S SILENCE OVER THE WHOLE CHAPTER and the export's third citation form; ONE LAW, ONE CASE;
  LEARN AND TEACH ARE ONE WORD (4:10's two ילמדון "they shall learn / teach" — qal and piel, the pointing alone dividing them; the store one gloss;
  Onkelos one verb twice); THE TABLETS PLENE (4:13 — three seats in the Bible; 5:22 and every Exodus seat defective); THE THIRD TELLING OF THE BAR
  (1:37 "for your sakes", 3:26 "was wroth for your sakes", 4:21 "on your account" and an OATH — 1b's open row widened by a telling); THE RECEIPT IN
  MOSES' OWN VOICE (4:5 and 10:5 — the register's seat meets its verse); THE FEAR, THE MEMRA, THE SHEKHINAH (Onkelos supplies the fear of the LORD at
  4:4, 20, 29, 30; the Memra at 4:24 — "the LORD your God, HIS MEMRA is a consuming fire" — 4:33, 4:36, 4:37 for "with his presence"; 4:39 repeats
  3:24's confession; 4:19 "prepared" for "apportioned"; 4:28 "the peoples who serve idols"; 4:34 "the miracles the LORD did to reveal himself" for
  "has a god tried"; 4:32 the Name for "God"; 4:5 "see" made plural); THE NUMBER SWITCHES BY VERSE; THE DECALOGUE'S IMAGE RECAST ("a graven image,
  the form of any figure" — three seats, all this chapter's; the likeness-word five in 4:16-18); YOU WERE SHOWN, THAT SAW (4:35 the hophal, 4:3 the
  participle — one spelling); THE CREED TWICE (4:35, 4:39 — Elijah's and Solomon's outside; Rahab's and Solomon's "in heaven above and on the earth
  beneath"); THE ONE CREATE (4:32 — the book's one seat of Genesis 1:1's verb); THEN MOSES SET APART (4:41 in the Song's form; the refuge runner's
  debit open to this verse; 4:42 in 19:4's words with "slays" for "smites"; Joshua 20:8's Gaulon); THE TWO FRAMES (1:1 and 4:45 "which Moses spoke";
  4:44 the Sifrei 323:1's lexicon; 4:46-49 the speech's own borders in its own clauses — 1:4, 2:36, 3:8, 3:17 verbatim; Mount Sion the fourth name);
  THE WITNESSES' CHAIN (the Sifrei 306:1: 4:26 the third of eleven; 30:19's first seven words identical); THE HAGGADAH'S ROW (4:34's seven
  instruments; the Sifrei 301:21 on 26:8; the arm plene / defective); THE EXPORT'S CHAPTER 5 (thirty against thirty-three).

THE SIFREI'S OWN CASE LAW (the block in MIDDOT.md, six rows): the king's bird — the soul at stake (48:2 on 4:9, E26); the consuming fire against
the cleaving, resolved by the sages (49:2 on 4:24 and 4:4, I13); "apportioned" at its two seats — not for worship (148:8 on 4:19 with 29:25,
I2); "great terror" fixed from "great terrors" — the revelation of the Shekhinah (301:21 on 26:8 from 4:34, E7); the chain of witnesses (306:1 on
32:1 — 4:26 the heavens, the third of eleven); "this" is nothing but Torah (323:1 on 32:29 from 4:44, E7). MOVE_CATALOG unchanged; MISHNAH_TOPICS
unchanged (no Mishnah opened at a reading sitting — the tractates routed to the docket).

THE CLAIMS (write_ch4_manifest.py → two manifests, 7 claims — DV04A-01..05 (4:1-8, 9-14, 15-24, 25-31, 32-40), DV04B-01..02 (4:41-43, 44-49) —
every check the word's LONGEST STORE-PIECE WHOLE (4:2 "add", 4:10 "assemble", 4:19 "apportioned", 4:26 "I call to witness", 4:35 "you were shown",
4:41 "set apart", 4:45 "the testimonies"); the ID prefixes asserted absent; every cite checked against the ledger's CITE INDEX and EVERY name of
the index used by a claim, asserted): verify_claims 5 + 2 VERIFIED / 0 FAILED; claim_labels_census --strict GREEN after TWO labels fell — "label
outside the vocabulary": the gate's regex takes the whole label as ONE code with a parenthetical, so a tail clause after the last parenthesis is
outside it (both re-closed with a parenthesis before the seat). THE SEATS (seat_ch4.py): 7 WITNESS_READ operators at the claims' first verses (5 on
4:1, 9, 15, 25, 32; 2 on 4:41, 44), step E in each, the scenarios in the anchor form; verify_text GREEN twice (40 and 9 steps; 7 scenarios each).
THE RITUALS (ch4_chain.sh): every gate PASS (13 PASS each) — RITUAL COMPLETE for the 217th and 218th frozen units; the declared-reading gate on the
coverage tool's path (the ledger not named by the unit id — the gate's fallback reads the unit's own refs); the Python rendering layer written and
self-proved twice. THE CORPUS REBAKED (predicted before the fold: units 218, standing 2184 + 7 = 2191, hash unmoved — the tripwire's literals set to
the prediction before the bake): CORPUS TRUTH GREEN — 218 units, 1809 facts, 341 demands (191 open), hash 8b8fff1fa28953af — the prediction
matched; build_world ALL GREEN (the fold layer of the one database); the journal gate GREEN (12 kinds, 9,646 rows — 9,628 + 18); the register gate
--strict GREEN (DECLARED 100, DEBT 0, FAILS 0 — the chapter's seats standing as filed until the compile). THE STAMP: one delegated FULL RULE row
naming the two units (logic/findings/STAMP_LEDGER.md). No engine file changed at this sitting — the sweep as at 1b's close.

OWED TO THE COMPILE (sitting 2b; the box in COMPILE_DEBT.md, items (a)-(l)): THE ONE LAW (4:2's "you shall not add … nor diminish" — the cell
without a case token; 13:1 its second seat FORWARD; the docket Rosh Hashanah 28b, Eruvin 96a, Sanhedrin 88b-89a; the Sifrei 82:5 on 1:11 the
shelf's exhibit); THE ONE CASE (4:25-31's "when you beget sons … and grow old … and corrupt" — the exile and the return as the case's arms; the
witnesses; the seeking "with all your heart" the Shema's words — DATA rows, no clock item: "in the end of days" a prophecy, not a timer); THE
RECEIPT'S SEAT (Deut 4:5 NONE → its class declared from the tape — the first-person receipt "as the LORD my God commanded me", 10:5 the pair);
THE THREE CITIES (4:41-43 — Moses' ACT in the third person: the refuge runner's debit appoint_six_cities_of_refuge, OPEN BY DESIGN since Numbers
35:14, CLOSED here by Moses' three — Bezer, Ramoth, Golan — with Joshua's three FORWARD (Joshua 20:7; the six as one at Makkot 2:4's "not until all
six"); the docket's OUTSIDE rows Makkot 9b:18, 10a:9-16 credited from the refuge exam; the tape line's day the frame's question); THE READBACK
ROWS of chapter 4 on the first form (Baal-peor 4:3 → SHORTENED against Numbers 25; Horeb 4:10-13 → EXPANDED against Exodus 19-20 with the tablets'
spelling; the bar 4:21-22 → the THIRD telling, the disagreement row of 1:37 widened; the exodus formulas 4:20, 34, 37 → the exodus's acts by
reference; the two kings and the borders 4:46-49 → SHORTENED against the speech's own lines 1:4, 2:36, 3:8, 3:17; the created man 4:32 → Genesis
1 by reference; the creed 4:35, 39; 4:26 → 30:19 forward); THE TWO FRAMES' DAY (4:44-49 the book's second frame — "when they came out of Egypt"
twice: whether the frame is the speech's own day (40, 11, 1) or a stamp without a day — R6's question at its second seat; Deut 4:45 the block's
footer, the chapter's daemon inside (Deut 1:1, Deut 4:45] or the next block); THE NO-IMAGE LIST as DATA (4:16-19's forms — figure, male, female,
beast, bird, creeping thing, fish, sun, moon, stars, the host: the second word's parameter table; the dependency on the Decalogue's runner or a
pointer to Exodus 20:4 dispositioned); THE HOST "APPORTIONED" (4:19 with 29:25 — the Sifrei 148:8's pair; Onkelos "prepared": a DATA note, no
link of our own); THE CHAPTER-5 DIVISION (the export's thirty verses against the DB's thirty-three — the recorder and the stitcher address verses by
the DB; the next reading's first measurement); THE STORE'S GLOSS FAMILIES (a display sitting's: the mixed families named by reference here); THE
DOCKET by the union rule (the TESTING paragraph's tractates: bal tosif, Kiddushin 30a, Avodah Zarah 3:1-3 with Rosh Hashanah 24a-b, Avodah Zarah
55a, Ketubot 111b, Makkot 2:4-8, Pesachim 10:4 and the Haggadah, Berakhot 32b; 4:26's and 4:30's open topics); THE MEKHILTA'S QUESTION on Exodus
20:22 (4:36's heaven and earth — the reading shelf's, credited by name only).

⚠ LESSONS (9): THE CUTTER TAKES CONSONANTS — seventeen Sifrei cuts fell at once for being typed pointed; type the consonants, let the cutter
print the shelf's pointed bytes. A LABEL ENDS WITH ITS PARENTHESIS — the labels gate reads the whole label as one code with one parenthetical;
a clause after the last ")" is "outside the vocabulary". THE SCRATCH SCRIPTS RUN FROM THE REPO ROOT — git rev-parse fails inside the scratchpad
(PYTHONPATH the scratchpad, cwd the repo). THE DB'S VERSE ORDER IS ALPHABETICAL BY BOOK — Deuteronomy before Exodus: a list typed in canonical
order fell; sort, or type from the print. THE EXPORT'S CHAPTER DIVISION IS NOT THE DB'S — assert the export's lengths per chapter (chapter 5:
thirty against thirty-three). A SUBSTRING CENSUS IS NOT A TOKEN CENSUS — "and rules" found inside another word at 32:14; onk_tok for a token,
onk_seats for a phrase. A FAMILY ALREADY REWRITTEN — "and-you-came-near" from sitting 1: the ink's absence-assert caught it; keep the assert.
A STEP BLOCK CARRIES TWO "comment" LINES — count from the print, not from the step count. THE READING SITTING'S SHAPE HELD ON A CHAPTER WITH NO
PISKA: the found-by-citation scan IS the spine's reading — dump → measure (three passes) → asserts (6 → 0) → rows (49 + 6) → writer (0 misses;
lint 0) → patch → manifests (7/7; the labels re-closed) → seat → two rituals (13 PASS each) → the fold predicted and matched.

NEXT on the ruling: THE COMPILE OF CHAPTER 4 (sitting 2b) on the Numbers walk's order — the measurements (the tape's state at Deut 3:29; the
callees live: the refuge runner's debit, the opening speech's daemon, the exodus and Sinai runners; the register gate's seats 4:5 and 4:45), THE
DESIGN in this file before any code (the one law's cell; the one case's arms; the three cities' act closing the refuge debit; the readback rows
of the chapter on the first form; the two frames' day; the no-image list as DATA), the probes to FAIL, the runner, the tape, every gate with THE
REGISTER GATE --strict at the gates step, the sweep — then chapter 5 (the Decalogue's reading, the export's division measured first; the laws'
readback opens with it), and on in order.
'''

STATE = '''
═══ COMPACTION POINT #185 (2026-09-16 — written at THE DEUTERONOMY WALK sitting 2's close; CHAPTER 4 READ AND FROZEN — the 217th and 218th units; NOT YET COMPILED; A CLEAN COMPACTION POINT; the last commit b8b721d, not pushed) ═══
STATE: 218 frozen units (216 + 2), standing 2191 (2184 + 7 as predicted), hash 8b8fff1fa28953af UNMOVED; CORPUS TRUTH GREEN; build_world ALL GREEN; the journal gate GREEN (12 kinds, 9,646 rows); the register gate --strict GREEN (DECLARED 100, DEBT 0, FAILS 0 — Deut 4:5 NONE "the book not read" until the compile, 4:45 DAEMONS); 58 runners, 63 daemons, the sweep as at 1b's close (no engine file changed); RUN (1295, 96, 88, 0, 12, 1583, 34, 319, four pairs, 126) unmoved. UNCOMMITTED: the two units FROZEN (logic/units/deu_04_obey_horeb.yaml, deu_04_refuge_east.yaml); logic/oral_triage/deu_04_vaetchanan_2026-09-16.md NEW (one ledger, 55 sources); the two manifests NEW; the two logic/py_units/deu_04_*.py NEW and ALL_UNITS.py; the two UNIT_deu_04_*.html and UNIT_INDEX.html; logic/corpus/CORPUS_TRUTH.py (218, 2191); logic/glosses/word_gloss_overrides.yaml (+81 by reference, +63 by gloss); the stamp row; the map, COMPILE_DEBT, RESEARCH_LOG, MIDDOT, THE_STEPS, THE_BRIEFING, RESUME, the recovery file, this entry; World/step9/forms_deuteronomy_walk/ (+ the sitting's scripts and prints); the memory; the three records that named b8b721d after the commit.
THE SITTING (the owner: "Reread what is next" → the rereads → "Go"; DEUTERONOMY_WALK.md "Sitting 2"): chapter 4 read as TWO drafts (the chapter numbers the names; the portion's grain crossed at 3:23) from sitting 1's forms folded and edited: THE SIFREI ON DEUTERONOMY HAS NO PISKA ON THE CHAPTER (30 on 3:29, 31 on 6:4 — the heads by chapter computed on all 357) — the found-by-citation scan the whole spine: eight rows of other piskaot cite chapter 4 (seven Hebrew, eight English; 301:21 the English's alone — THE EXPORT'S THIRD CITATION FORM, an unpointed abbreviated Hebrew with "(Devarim 4:34)"), six read fresh in both files, two credited from sitting 1; Onkelos whole (49) = 55 sources in one ledger (the asserts fell 6 on the first typed pass — the export's chapter 5 at thirty verses, the step blocks' two comment lines, "and lest" outside the case list, the DB's alphabetical book order, a substring census, a family already rewritten — none on the second; the Sifrei cuts fell seventeen times at once for being typed pointed); the display layer's rows 81 by reference (the indices computed from the store) + 63 by gloss; the manifests 7 claims verified 7/7, the labels gate GREEN after two labels were re-closed with their parenthesis; seated as 7 WITNESS_READ operators; verify_text GREEN twice; the rituals 13 PASS each; the corpus rebaked to the prediction; the stamp row. THE PARSER: four number verses, NO GAP. THE FINDS (seventeen crowns, the map's list): the shelf's silence and the third citation form; one law (4:2) and one case (4:25); learn and teach one word (4:10); the tablets plene (4:13); the third telling of the bar with an oath (4:21); the receipt in Moses' own voice (4:5); the translation's fear, Memra and Shekhinah (and "prepared" at 4:19, the idolaters at 4:28, the miracles at 4:34, the Name at 4:32, "see" plural at 4:5); the number switching by verse; the Decalogue's image recast; "you were shown" / "that saw"; the creed twice; the one "created"; "then Moses set apart" (the refuge debit's verse); the two frames and the speech's borders retold; the witnesses' chain; the Haggadah's row; the export's chapter 5.
THE RECORDS: DEUTERONOMY_WALK.md "Sitting 2"; the ledger, the two manifests and py renderings; RESEARCH_LOG.md's entry; COMPILE_DEBT.md's sitting-2 box (a)-(l); MIDDOT.md's block (six rows); STAMP_LEDGER's row; THE_STEPS' paragraph; THE_BRIEFING's scoreboard bullet and entry; the gloss override rows; World/RESUME.md's note; the forms copied into World/step9/forms_deuteronomy_walk/; memory (deuteronomy-walk.md's paragraph; MEMORY.md's index line); the recovery file's section 33; this entry.
THE LESSONS (the map's ⚠ list, nine): the cutter takes consonants; a label ends with its parenthesis; the scratch scripts run from the repo root; the DB's verse order is alphabetical by book; the export's chapter division is not the DB's; a substring census is not a token census; a family already rewritten is caught by the ink's assert; a step block carries two comment lines; the reading shape held on a chapter with no piska.
NEXT on the ruling: SITTING 2b — THE COMPILE OF CHAPTER 4 on the Numbers walk's order (DEUTERONOMY_WALK.md's owed list (a)-(l): the one law's cell; the one case's arms; the receipt's seat 4:5 declared; the three cities closing the refuge runner's debit; the chapter's readback rows on the first form; the two frames' day; the no-image list as DATA; the host "apportioned"; the chapter-5 division; the docket by the union rule) — the design in DEUTERONOMY_WALK.md before any code — then chapter 5's reading (the export's division measured first; the laws' readback opens with it), and on in order.
POST-COMPACTION REREADS (mandatory, first sitting): the recovery file logic/pre_logic_methods_2026-07-28/RECOVERY_new_thread_2026-09-12.md whole (its section 5 THE COMPILE SITTING; its sections 31-33) + the memory deuteronomy-walk.md + numbers-in-order-ruling.md + this entry + DEUTERONOMY_WALK.md whole ("Sitting 1b" the design and AS BUILT — the compile's form on this book; "Sitting 2") + THE_STEPS Step 2 + Step 5 + the compiler block + THE_LOOP.md's STEP 6 (THE READBACK's first form; the laws' half owed) — before deriving.
'''

RESUME_NOTE = '''# ⚠ THE DEUTERONOMY WALK sitting 2 (2026-09-16; step9/DEUTERONOMY_WALK.md "Sitting 2"): CHAPTER 4 READ AND FROZEN as two units (the 217th and
# 218th; standing 2191, hash unmoved) — the Sifrei has NO piska on the chapter, its eight rows found by citation; one law (4:2), one case (4:25),
# Moses' three cities at 4:41 the refuge runner's open debit; every gate GREEN. NEXT on the ruling: the compile (2b), then chapter 5.
'''
RESUME = '''DEUTERONOMY SITTING 2 DONE 2026-09-16 (CHAPTER 4 READ AND FROZEN — deu_04_obey_horeb 4:1-40 and deu_04_refuge_east 4:41-49, the 217th and 218th units; World/step9/DEUTERONOMY_WALK.md "Sitting 2"; the owner: "Go" after the rereads): THE SIFREI ON DEUTERONOMY HAS NO PISKA ON THE CHAPTER (30 on 3:29, 31 on 6:4) — its eight rows citing chapter 4 found by the scan of the whole export in both files (six fresh, two credited from sitting 1; 301:21 the export's third citation form — unpointed, "Devarim 4:34"); Onkelos whole (49) = 55 sources in one ledger (logic/oral_triage/deu_04_vaetchanan_2026-09-16.md; coverage computed; the ink asserts 6 → 0; the Sifrei cuts typed pointed fell seventeen at once); the parser four number verses, no gap; the finds — one law (4:2) and one case (4:25); learn and teach one word (4:10); the tablets plene (4:13); the third telling of the bar with an oath (4:21); the receipt in Moses' own voice (4:5); Onkelos' fear, Memra and Shekhinah, "prepared" for "apportioned" (4:19), the idolaters for the idols (4:28), the miracles for the question (4:34), the Name for "God" (4:32); the number switching by verse; the Decalogue's image recast; the creed twice; "then Moses set apart" (4:41 — the refuge runner's debit's verse); the two frames (1:1, 4:45) and the speech's borders retold; the Sifrei 306:1's witnesses; the export's chapter 5 at thirty verses; 7 claims verified and seated, two rituals 13 PASS, the corpus rebaked to the prediction (218 units, standing 2191, hash 8b8fff1fa28953af), build_world, the journal gate and the register gate GREEN; the display layer +144 rows. NEXT: the compile (2b) — the one law's cell, the one case's arms, the three cities closing the refuge debit, the receipt's seat, the chapter's readback rows; then chapter 5.
'''

STEPS = '''DEUTERONOMY — SITTING 2 — CHAPTER 4, Deuteronomy 4:1-49 (2026-09-16, on Brian's "Go" after the rereads; World/step9/DEUTERONOMY_WALK.md "Sitting 2").
The chapter read as two units the way the book was opened: Onkelos whole and the Sifrei on Deuteronomy by its position in the export — and the shelf
has nothing on this chapter at all: its thirtieth piska ends at 3:29 and its thirty-first opens at 6:4. So the reading of the spine here is the scan
of the whole export for any row that cites chapter 4 — eight rows do, six of them fresh, and one of the eight is another stratum of the export
altogether, an unpointed Hebrew with abbreviations and an English that cites "Devarim 4:34" with a space, the third citation form the book has shown.
The parser measured first: four number verses, every one read. The finds: the chapter has one law — add nothing, take nothing away — and one case,
"when you beget sons and grow old"; "they shall learn" and "they shall teach" in the Horeb verse are the same letters, told apart by the vowels alone;
the two tablets of stone are spelled full here where the same chapter's own retelling in chapter 5 and every Exodus seat spell them short; the bar on
Moses is told a third time, now with an oath and a new ground; the receipt "as the LORD commanded" is given by Moses for his own teaching; the
translation writes "the fear of the LORD" where the verse says the LORD, the Word where the verse says fire or presence, and turns "has a god tried"
into "the miracles the LORD did"; the chapter speaks to Israel in the singular and the plural by turns, verse by verse; "you were shown" and "your
eyes that saw" are one spelling; "the LORD is God" is said twice, in Elijah's and Solomon's words; the one "created" of the book is here; then Moses
sets apart three cities in the Song's grammar — the refuge law's open debt since Numbers 35, to be closed at the compile; and the chapter's last
verses frame the laws with the speech's own border clauses word for word. Six typed facts fell on the first pass and none on the second; seventeen
Sifrei cuts fell at once for being typed with their vowels. Seven claims verified and seated, two rituals complete, the corpus rebaked to the predicted
count with the hash unmoved, the world's fold layer, the journal gate and the register gate green. Next: the compile (2b), on your word.

'''

BRIEF = '''- **CHAPTER 4 READ AND FROZEN — THE SHELF IS SILENT ON THE WHOLE CHAPTER, ONE LAW AND ONE CASE, LEARN AND TEACH ARE ONE WORD, AND MOSES SETS APART THE THREE CITIES THE REFUGE LAW LEFT OPEN** (2026-09-16, on your "Go" after the rereads; World/step9/DEUTERONOMY_WALK.md "Sitting 2"). Two units on the chapter, 55 sources in one ledger, seven claims seated, the 217th and 218th frozen units (standing 2191, hash unmoved). The Sifrei on Deuteronomy has no piska on 4:1-49; its eight rows citing the chapter were found by scanning the whole export, and one of them is a third citation form. The finds: the chapter's one law (add nothing, take nothing away) and one case (when you beget sons); "they shall learn" and "they shall teach" the same letters; the tablets spelled full; the bar on Moses told a third time with an oath; the receipt in Moses' own voice; the translation's fear, Word and Shekhinah; the creed twice; "then Moses set apart" — the refuge runner's open debt, closed at the compile. Every gate green.
'''
BRIEF_ENTRY = '''### 2026-09-16 — CHAPTER 4 READ: THE SHELF IS SILENT, THE CHAPTER HAS ONE LAW, AND MOSES' THREE CITIES WAIT FOR THE COMPILE

Chapter 4 was read the way the first three were — Onkelos whole, the Sifrei by its position — and the Sifrei turned out to have no position here at
all: nothing between its row on 3:29 and its row on 6:4. So the shelf's reading of this chapter is whatever the shelf says about it elsewhere: eight
rows in other piskaot cite chapter 4, and those were read (six fresh, two already read). The parser read every number. The chapter itself has one law
(you shall not add to the word, nor take from it) and one case (when you beget sons and grow old in the land) — everything else is the rebuke retold:
Horeb, the calf's lesson without the calf, the bar on Moses now with an oath, the exile and the return, the creed. Two things were measured that
matter to the machine: the same letters mean "they shall learn" and "they shall teach" in one verse, told apart by vowels alone; and the export's
chapter 5 has thirty verses where the database has thirty-three — the Decalogue's division — so the next reading measures that first. And the
chapter's one act — Moses setting apart three cities of refuge beyond the Jordan — is the very act the refuge law's runner left open since Numbers
35; the compile closes it. Seven claims, two rituals, the corpus at its predicted count, every gate green. Next: the compile, on your word.

'''

DEBT = '''
## DEUTERONOMY SITTING 2 — CHAPTER 4'S READING (2026-09-16; DEUTERONOMY_WALK.md "Sitting 2"; logic/oral_triage/deu_04_vaetchanan_2026-09-16.md; the two
## units deu_04_obey_horeb, deu_04_refuge_east FROZEN) — OWED TO THE COMPILE (sitting 2b), each item named at its verse: (a) THE ONE LAW — 4:2's "you
## shall not add … nor diminish" (the cell without a case token; 13:1 its second seat FORWARD; the docket Rosh Hashanah 28b, Eruvin 96a, Sanhedrin
## 88b-89a; the Sifrei 82:5 on 1:11 the exhibit); (b) THE ONE CASE — 4:25-31's "when you beget sons … grow old … corrupt" (the exile and the return as
## the case's arms; DATA rows — "in the end of days" a prophecy, no timer); (c) THE RECEIPT'S SEAT — Deut 4:5 NONE ("the book not read") declared from
## the tape: the first-person receipt "as the LORD my God commanded me" (10:5 the pair); (d) THE THREE CITIES — 4:41-43 Moses' ACT in the third
## person: the refuge runner's debit appoint_six_cities_of_refuge OPEN BY DESIGN since Numbers 35:14, CLOSED by Moses' three (Bezer, Ramoth, Golan),
## Joshua's three FORWARD (Joshua 20:7; Makkot 2:4 "not until all six"); the docket's OUTSIDE rows Makkot 9b:18, 10a:9-16 credited from the refuge
## exam docket; (e) THE READBACK ROWS of chapter 4 on the first form (4:3 SHORTENED / Numbers 25; 4:10-13 EXPANDED / Exodus 19-20, the tablets' spelling;
## 4:21-22 the THIRD telling — the 1:37 disagreement row widened; 4:20, 34, 37 the exodus's acts by reference; 4:46-49 SHORTENED / the speech's own 1:4,
## 2:36, 3:8, 3:17; 4:32 Genesis 1 by reference; 4:35, 39 the creed; 4:26 → 30:19 forward); (f) THE TWO FRAMES' DAY — 4:44-49 the book's second frame,
## "when they came out of Egypt" twice: the frame's day (40, 11, 1) or a stamp without a day (R6's question at its second seat); Deut 4:45 the block's
## footer — the chapter's daemon inside (Deut 1:1, Deut 4:45] or the next block; (g) THE NO-IMAGE LIST as DATA — 4:16-19's forms (figure, male, female,
## beast, bird, creeping thing, fish, sun, moon, stars, the host): the second word's parameter table, the pointer to Exodus 20:4 dispositioned; (h) THE
## HOST "APPORTIONED" — 4:19 with 29:25 (the Sifrei 148:8's pair), Onkelos "prepared": a DATA note, no link of our own; (i) THE CHAPTER-5 DIVISION —
## the export's thirty verses against the DB's thirty-three: the recorder and the stitcher address by the DB; the next reading's first measurement;
## (j) THE STORE'S GLOSS FAMILIES — the mixed families named by reference (a display sitting's); (k) THE DOCKET by the union rule — bal tosif,
## Kiddushin 30a, Avodah Zarah 3:1-3 with Rosh Hashanah 24a-b, Avodah Zarah 55a, Ketubot 111b, Makkot 2:4-8, Pesachim 10:4 and the Haggadah, Berakhot
## 32b; 4:26's "not prolong days" and 4:30's "in your distress … return" open topics; (l) THE MEKHILTA'S QUESTION on Exodus 20:22 (4:36 — the reading
## shelf's, credited by name only). THE 1b BOX'S ITEM (ii) — 4:41-43 — is this sitting's (d).
'''

RESEARCH = '''

## 2026-09-16 — DEUTERONOMY 4 READ (THE DEUTERONOMY WALK sitting 2 — CHAPTER 4): THE SHELF'S SILENCE OVER A WHOLE CHAPTER; THE EXPORT'S THIRD
## CITATION FORM; THE EXPORT'S CHAPTER 5 AT THIRTY VERSES; LEARN AND TEACH ONE WORD; THE TABLETS PLENE; THE NAME FOR "GOD" IN THE TRANSLATION;
## THE THIRD TELLING OF THE BAR; THE STORE'S ODD GLOSSES ON THE CHAPTER

THE SIFREI ON DEUTERONOMY HAS NO PISKA ON CHAPTER 4. Its thirtieth piska heads on 3:29 (two rows) and its thirty-first on 6:4 (ten rows); no head
of the 357 falls in the chapter (the heads by chapter computed: chapter 1's twenty-four, chapter 3's four, chapter 4's none). Sitting 1 found the
shelf two islands (1:1-1:28 and 3:23-3:29); the silence of 1:29-3:22 continues through 4:49 and ends at the Shema. The reading of the spine on such
a chapter is the scan of the whole export for rows that CITE the chapter: eight do (seven in the Hebrew file, eight in the English), and those
rows — on 3:29, 11:10, 11:22 (two), 17:2, 26:5, 32:1, 32:29 — were read in both files, six fresh, two credited from sitting 1.

THE EXPORT'S THIRD CITATION FORM. Row 301:21 (on 26:8) is cited in the scan by its English alone: its Hebrew is UNPOINTED, abbreviated ("as it is
written" in two letters) and cites nothing in parentheses, while its English cites "(Devarim 4:34)" WITH a space. The rows of piskaot 1-30 cite
"(דברים א א)" ("Deuteronomy 1:1" in Hebrew letters) and "(Dt.1:1)" without a space (sitting 1 measured 3,292 "Dt." parens and one "Deut."); the
late piskaot of the export are another stratum, with another translation. A scan of this export must carry all three forms; a Hebrew-only scan
misses the row.

THE EXPORT'S CHAPTER 5 HAS THIRTY VERSES. Onkelos Deuteronomy's export gives 956 verses to the DB's 959, and the whole difference is chapter 5 —
thirty verses in the export against thirty-three in the DB (the Decalogue's division): the one chapter of the book where the export and the DB
disagree (every other chapter's count equal, computed). The recorder and the stitcher address verses by the DB; the next reading measures the
mapping first.

LEARN AND TEACH ARE ONE WORD. 4:10 writes ילמדון ("they shall learn / they shall teach") twice: "that they may LEARN to fear me" (the qal, the
morphology HVqi3mp) and "and their sons they shall TEACH" (the piel, HVpi3mp) — one spelling, two stems, the pointing alone dividing them; the store
glosses both "goad-suffix", and Onkelos writes one Aramaic verb twice (the Aramaic cannot show the stem either). The display layer names each by
reference ("they-may-learn", "they-shall-teach"); the parser's morphology carries what the consonants do not.

THE TABLETS PLENE. 4:13's "two tablets of stone" spells "tablets" with the vav — three seats in the Bible (4:13, 9:11, 1 Kings 8:9) — where 5:22, the
same chapter's own retelling, and every Exodus seat write it defective (twelve seats). The diff of 4:13 against 5:22 keeps "and wrote them on two"
and changes the spelling.

THE NAME FOR "GOD" IN THE TRANSLATION. 4:32 "since the day God created man on the earth" — Onkelos writes the Tetragrammaton's two letters where the
verse writes Elohim: Genesis 1:1's verb given Genesis 2:4's Name. The chapter's other moves of the translation: "the fear of the LORD" supplied at
4:4, 20, 29, 30; the Memra at 4:24 ("the LORD your God — his Memra is a consuming fire", the form's two seats 4:24 and 20:1), 4:33, 4:36, 4:37 (for
"with his presence"); 4:39's "God whose Shekhinah is in the heavens above and who rules on the earth beneath" (3:24's confession again); 4:19
"prepared" for "apportioned"; 4:28 "the peoples who serve idols" for "gods of wood and stone" (4:28, 28:36, 28:64); 4:34 "the miracles which the
LORD did to reveal himself" for "has a god tried"; 4:5 "see" made plural.

THE THIRD TELLING OF THE BAR. 1:37 "the LORD was angry with me FOR YOUR SAKES", 3:26 "the LORD was WROTH with me for your sakes", 4:21 "the LORD was
ANGRY with me ON YOUR ACCOUNT and SWORE that I should not cross" — three grounds, one oath: 4:21 takes 1:37's verb (the hitpael of anger; the four
Torah seats 1:37, 4:21, 9:8, 9:20) and its own phrase ("on your account" one seat, against "for your sakes" at 1:37 and Micah 3:12). The disagreement
row 1b left open (1:37 against Numbers 20:12's "because you did not believe") widens by a telling.

THE STORE'S ODD GLOSSES ON THE CHAPTER (the display layer, read back by ch4_patch_overrides.py — eighty-one by reference, sixty-three by gloss; the
families censused over the whole store first): "goad" for TEACH (the whole family the teach-root), "the-enactment" for THE STATUTES, "mislay" for
FORGET, "living-being-you/your" for YOUR SOUL, "meaning-to-glisten" for TABLETS, "to-failure-of" for SO AS NOT, "associate-him/its" for HIS
NEIGHBOR, "the-Emorite" for THE AMORITE, "in-region-across" for BEYOND, "at-that-time" for THEN, "from-nearest-part" for FROM THE MIDST OF, "kindle"
for BURN, "and-gloom" for AND THICK DARKNESS, "convoke" for ASSEMBLE, "decay-suffix" for YOU ACT CORRUPTLY, "the-heavens-suffix" for HEAVENWARD,
"from-pot" for FROM THE FURNACE OF, "wander-away-suffix" for YOU SHALL PERISH, "trebly" for THE DAY BEFORE, "the-test" for HAS TRIED, "in-testing" for
BY TRIALS; and by reference the mixed families — "the-see" for THAT SAW (4:3) against "see" for WERE SHOWN (4:35), "structure" for THE LIKENESS OF,
"idol" for A GRAVEN IMAGE, "be-smooth" for APPORTIONED, "duplicate" for I CALL TO WITNESS, "and-dash-in-pieces" for AND WILL SCATTER, "dash-in-pieces"
for A MANSLAYER and SLAYS, "the-testimony" for THE TESTIMONIES, "?" for I (six seats), Baal, Beth. Sixteen families the chapter shares with sitting 1
were already rewritten and stand.
'''

MIDDOT = '''- **THE SIFREI ON DEUTERONOMY'S OWN CASE LAW ON CHAPTER 4 (Deuteronomy 4:1-49; THE DEUTERONOMY WALK sitting 2, 2026-09-16;
  logic/oral_triage/deu_04_vaetchanan_2026-09-16.md — no piska on the chapter; the six rows citing it, read whole in both files; E-codes by the row's conclusion):
  · THE KING'S BIRD — THE SOUL AT STAKE (Sifrei Devarim 48:2 on 4:9, in the row on 11:22): "only take heed to yourself and keep your soul diligently" —
    R. Ishmael's king who trapped a bird and gave it to his servant for his son: lose it and you have lost not a penny's bird but your life; "it is no
    empty word for you — it is your life" (32:47) joined by its own word. The parable of the king (E26) on a verse whose "soul" is read whole; the
    second verse a REFERENCE the Sifrei itself makes (LR1).
  · THE CONSUMING FIRE AGAINST THE CLEAVING (49:2 on 11:22 with 4:24 and 4:4): "and to cleave to him" — how can a man go up on high and cleave to
    fire, when "the LORD your God is a consuming fire" (4:24) and "his throne was flames of fire" (Daniel 7:9)? Cleave to the sages and their
    disciples, and it is counted as if you went up and took it — by war. Two verses that contradict until a third reading decides (I13); Onkelos at
    4:4 decides by translation ("cleave to the FEAR of the LORD") and at 4:24 moves the fire to the Memra.
  · "APPORTIONED" AT ITS TWO SEATS — NOT FOR WORSHIP (148:8 on 17:2-3 with 4:19 and 29:25): R. Yose the Galilean — from "which the LORD your God
    apportioned to all the peoples" (4:19), might it be for worship? "gods which they knew not and which he had NOT apportioned to them" (29:25).
    The doubt raised and closed by the second seat of the one verb (the qal perfect's two Torah seats exactly these — computed; I2's form on a shared
    verb, a REFERENCE the Sifrei draws, LR1); Onkelos answers the same doubt at 4:19 with "prepared".
  · "GREAT TERROR" FIXED FROM "GREAT TERRORS" — THE REVELATION OF THE SHEKHINAH (301:21 on 26:8 from 4:34): the first-fruits' "and with great terror"
    glossed by 4:34's seven instruments; the term fixed from its fuller seat (E7). The export's unpointed stratum; the Haggadah's row (Mishnah
    Pesachim 10:4 — the testing shelf).
  · THE CHAIN OF WITNESSES (306:1 on 32:1 with 4:26): R. Meir — Israel testified against themselves (Joshua 24:22); corrupted, Judah and Benjamin
    testified; then the prophets; then THE HEAVENS — "I call heaven and earth to witness against you this day" (4:26); then the earth, the roads,
    the nations, the mountains, the beasts, the birds, the fish, the ant. Eleven summonses in the Hebrew row, ten in the English (computed); the
    verses ordered as a history, each rung a citation (E32's kin — the sequence read as a ladder).
  · "THIS" IS NOTHING BUT TORAH (323:1 on 32:29 from 4:44): "if they were wise they would understand THIS" — had Israel looked into the Torah no
    nation would have ruled them; "this" defined from "and this is the Torah which Moses set before the children of Israel" (4:44) — the word fixed
    from its defining seat (E7), in the row's own formula "nothing but" (the exclusive gloss).
  THE TWO CREDITED ROWS (30:2 — "and now, Israel, hear" the forgiveness after the rebuke, read at sitting 1; 37:9 — Hermon's four names with 4:48's
  Sion, an a-fortiori on the Land, I1) stand in sitting 1's block.
'''

RECOVERY = '''

## 33. ADDENDUM (2026-09-16, THE DEUTERONOMY WALK sitting 2 — CHAPTER 4, Deuteronomy 4:1-49 READ AND FROZEN; the owner: "Reread what is next" → the rereads → "Go"; the state doc's COMPACTION POINT #185)

THE SITTING RAN IN THE READING SHAPE (section 5) on a chapter WITH NO PISKA: World/step9/DEUTERONOMY_WALK.md "Sitting 2". THE STATE: 218 frozen
units (216 + 2 — deu_04_obey_horeb 4:1-40, deu_04_refuge_east 4:41-49), standing 2191 (2184 + 7 as predicted), hash 8b8fff1fa28953af UNMOVED;
CORPUS TRUTH, build_world, the journal gate (12 kinds, 9,646 rows), the register gate --strict (DECLARED 100, DEBT 0, FAILS 0) GREEN; no engine file
changed; the ledger logic/oral_triage/deu_04_vaetchanan_2026-09-16.md (55 sources — Onkelos 49 fresh, the Sifrei's six rows citing the chapter fresh,
two credited from sitting 1); the two manifests (7 claims DV04A-01..05, DV04B-01..02); the display layer +144 rows. THE SHELF: the Sifrei on
Deuteronomy has NO piska on chapter 4 (30 on 3:29, 31 on 6:4; the heads by chapter computed on all 357) — the found-by-citation scan the whole spine:
eight rows (seven Hebrew, eight English; 301:21 the English's alone — THE EXPORT'S THIRD CITATION FORM, an unpointed abbreviated Hebrew, "(Devarim
4:34)" with a space); Onkelos Deuteronomy's export gives CHAPTER 5 THIRTY VERSES against the DB's thirty-three (the one disagreeing chapter — the
next reading measures the mapping first). THE READING'S SHAPE HELD: dump (one script for the three first-pass scripts) → measure (three passes: the
retellings diffed, the phrase censuses, the Onkelos seats, the gloss families) → asserts (6 fell on the first typed pass → 0) → rows (49 + 6; the
Sifrei cuts fell seventeen at once for being typed pointed) → the writer (0 misses; lint 0 on the first write) → the patch (81 by reference with the
indices computed from the store, 63 by gloss) → the manifests (7/7; the labels gate after two labels re-closed with their parenthesis) → the seat
→ two rituals (13 PASS each) → the fold predicted and matched. THE FINDS (seventeen crowns): the shelf's silence and the third citation form; ONE LAW
(4:2 add / diminish, no case token) and ONE CASE (4:25 "when you beget sons"); LEARN AND TEACH ONE WORD (4:10's two ילמדון "they shall learn /
teach" — qal and piel by the pointing alone); the TABLETS PLENE (4:13); the THIRD TELLING OF THE BAR (4:21 "on your account" with an oath — 1b's open
row widened); the RECEIPT IN MOSES' OWN VOICE (4:5, the register's seat); the translation's FEAR, MEMRA AND SHEKHINAH (4:4, 20, 24, 29-30, 33, 36-37,
39), "prepared" for "apportioned" (4:19), the idolaters for the idols (4:28), the miracles for the question (4:34), the Name for "God" (4:32), "see"
plural (4:5); the number switching by verse; the Decalogue's image recast (4:16-19); "you were shown" / "that saw" one spelling; the creed twice
(4:35, 39); the one "created" (4:32); THEN MOSES SET APART (4:41 — the refuge runner's debit appoint_six_cities_of_refuge OPEN since Numbers 35:14,
the compile's to close); the two frames (1:1, 4:45) and the speech's borders retold verbatim (1:4, 2:36, 3:8, 3:17); the Sifrei 306:1's witnesses;
the Haggadah's row (301:21). THE LESSONS (nine, the map's ⚠ list): the cutter takes consonants; a label ends with its parenthesis; the scratch
scripts run from the repo root; the DB's verse order is alphabetical by book; the export's chapter division is not the DB's; a substring census is
not a token census; a family already rewritten is caught by the ink's assert; a step block carries two comment lines; the reading shape held on a
chapter with no piska. THE FORMS: World/step9/forms_deuteronomy_walk/ (+ the sitting's scripts and prints). THE RECORDS current: the map, COMPILE_DEBT
(the sitting-2 box (a)-(l); the 1b box's item (ii) is its (d)), RESEARCH_LOG, MIDDOT (six rows), STAMP_LEDGER, THE_STEPS, THE_BRIEFING, RESUME, the
memory, the state doc's #185. NEXT on the ruling: SITTING 2b — THE COMPILE OF CHAPTER 4 (the design in the map before any code: the one law's cell,
the one case's arms, the receipt's seat 4:5, the three cities closing the refuge debit, the chapter's readback rows on the first form, the two frames'
day, the no-image list as DATA, the docket by the union rule), then chapter 5's reading (the Decalogue; the export's division measured first; the
laws' readback opens with it). UNCOMMITTED at this writing: everything of this sitting and the three records that named b8b721d — the owner's next
commit word carries them (the last commit b8b721d, not pushed).
'''

MEMPAR = '''
SITTING 2 DONE 2026-09-16 (the owner: "Reread what is next" → the rereads → "Go"; "Sitting 2" in the map): CHAPTER 4 READ AND FROZEN as TWO units —
deu_04_obey_horeb 4:1-40, deu_04_refuge_east 4:41-49 (218 units, standing 2191, hash 8b8fff1fa28953af unmoved); the ledger
logic/oral_triage/deu_04_vaetchanan_2026-09-16.md (55 sources). THE SIFREI HAS NO PISKA ON CHAPTER 4 (30 on 3:29, 31 on 6:4) — its eight rows
citing the chapter found by scanning the whole export in both files (six fresh, two credited); 301:21 the export's THIRD citation form (an unpointed
abbreviated Hebrew; "Devarim 4:34" with a space). ⚠ THE EXPORT'S CHAPTER 5 HAS THIRTY VERSES against the DB's thirty-three (the Decalogue's division)
— chapter 5's reading measures the mapping FIRST. The finds: one law (4:2 add / diminish) and one case (4:25); learn and teach ONE WORD (4:10's two
ילמדון "they shall learn / teach", qal and piel by the pointing alone); the tablets plene (4:13); the bar told a THIRD time with an oath (4:21 —
1b's open row widened); the receipt in Moses' own voice (4:5 — the register's seat NONE, paid at the compile); Onkelos' fear, Memra and Shekhinah,
"prepared" for "apportioned" (4:19), the idolaters for the idols (4:28), the miracles for "has a god tried" (4:34), the Name for "God" (4:32); the
number switching by verse; "then Moses set apart" (4:41) — THE REFUGE RUNNER'S DEBIT appoint_six_cities_of_refuge OPEN since Numbers 35:14, the
compile closes it; the two frames (1:1, 4:45) and the speech's borders retold verbatim. Every gate GREEN (CORPUS TRUTH, build_world, the journal
gate, the register gate --strict). ⚠ THE LESSONS OF 2 (nine, in the map): the cutter takes CONSONANTS (seventeen Sifrei cuts fell at once for being
typed pointed); a label ENDS WITH ITS PARENTHESIS (the labels gate reads one code + one parenthetical); the scratch scripts run from the repo ROOT
(PYTHONPATH the scratchpad); the DB's verse order is ALPHABETICAL by book; the export's chapter division is not the DB's; onk_tok for a token,
onk_seats for a phrase; a family already rewritten is caught by the ink's assert; a step block carries two "comment" lines. OWED (the sitting-2
box (a)-(l)): the compile 2b — the one law's cell, the one case's arms, the receipt's seat, the three cities closing the refuge debit, the readback
rows of the chapter, the two frames' day, the no-image list as DATA, the docket. NEXT on the ruling: SITTING 2b — the compile of chapter 4 (the
design in the map before any code), then chapter 5's reading.
'''

# ---- THE WRITES (every insert on a unique anchor asserted present once) ----
LINT = f'{ROOT}/logic/solo_tools/gloss_lint.py'
def lint(path):
    out = subprocess.run(['python3', LINT, path], capture_output=True, text=True).stdout
    m = re.search(r'gloss_lint: (\d+) flag', out); return int(m.group(1)) if m else -1
WALKP = f'{ROOT}/World/step9/DEUTERONOMY_WALK.md'
TOUCH = [f'{ROOT}/logic/findings/STAMP_LEDGER.md', f'{ROOT}/logic/pre_logic_methods_2026-07-28/PROMPT_continue_solo_era_2026-08-06.md', f'{ROOT}/World/RESUME.md', f'{ROOT}/THE_STEPS.md', f'{ROOT}/THE_BRIEFING.md', f'{ROOT}/World/step9/COMPILE_DEBT.md', f'{ROOT}/RESEARCH_LOG.md', f'{ROOT}/logic/MIDDOT.md', f'{ROOT}/logic/pre_logic_methods_2026-07-28/RECOVERY_new_thread_2026-09-12.md', f'{MEM}/MEMORY.md', WALKP, f'{MEM}/deuteronomy-walk.md']
BEFORE = {p: lint(p) for p in TOUCH}
print('lint before:', {os.path.basename(p): n for p, n in BEFORE.items()})

append(f'{ROOT}/logic/findings/STAMP_LEDGER.md', STAMP)
assert '## Sitting 2 — CHAPTER 4' not in open(WALKP, encoding='utf-8').read()
append(WALKP, WALK)
append(f'{ROOT}/logic/pre_logic_methods_2026-07-28/PROMPT_continue_solo_era_2026-08-06.md', STATE)
insert_before(f'{ROOT}/World/RESUME.md', '# ⚠ THE DEUTERONOMY WALK 1b (2026-09-15/16; step9/DEUTERONOMY_WALK.md "Sitting 1b — AS BUILT")', RESUME_NOTE)
rp = f'{ROOT}/World/RESUME.md'; s = open(rp, encoding='utf-8').read()
i = s.index('DEUTERONOMY SITTING 1 DONE 2026-09-15 (THE OPENING SPEECH 1:1-3:29 READ AND FROZEN'); j = s.index('\n', i) + 1
open(rp, 'w', encoding='utf-8').write(s[:j] + RESUME + s[j:]); print('inserted the RESUME line after sitting 1\'s at', j)
sp = f'{ROOT}/THE_STEPS.md'; s = open(sp, encoding='utf-8').read()
i = s.index('DEUTERONOMY — SITTING 1b — THE OPENING SPEECH COMPILED'); j = s.index('\n\n', i) + 2
open(sp, 'w', encoding='utf-8').write(s[:j] + STEPS + s[j:]); print('inserted THE_STEPS paragraph after the 1b paragraph at', j)
insert_before(f'{ROOT}/THE_BRIEFING.md', '- **THE OPENING SPEECH COMPILED — THE READBACK\'S FIRST FORM BUILT:', BRIEF)
insert_before(f'{ROOT}/THE_BRIEFING.md', '### 2026-09-15/16 — THE OPENING SPEECH COMPILED: THE TAPE IS READ BACK', BRIEF_ENTRY)
append(f'{ROOT}/World/step9/COMPILE_DEBT.md', DEBT)
append(f'{ROOT}/RESEARCH_LOG.md', RESEARCH)
insert_before(f'{ROOT}/logic/MIDDOT.md', '## Exodus block campaign — owner\'s word "Do 3")', MIDDOT + '\n')
append(f'{ROOT}/logic/pre_logic_methods_2026-07-28/RECOVERY_new_thread_2026-09-12.md', RECOVERY)
# the memory: the walk file's paragraph + the index line (under 17,000 bytes)
append(f'{MEM}/deuteronomy-walk.md', MEMPAR)
ip = f'{MEM}/MEMORY.md'; m = open(ip, encoding='utf-8').read()
a1 = "- [⚠ THE DEUTERONOMY WALK](deuteronomy-walk.md) — opened 2026-09-15; map World/step9/DEUTERONOMY_WALK.md; SITTINGS 1 (1:1-3:29 read, six units) and 1b (the compile; THE READBACK's first form BUILT — 42 rows; every gate GREEN; twelve ⚠ lessons) DONE 2026-09-16; NEXT: chapter 4's reading"
b1 = "- [⚠ THE DEUTERONOMY WALK](deuteronomy-walk.md) — opened 2026-09-15; map World/step9/DEUTERONOMY_WALK.md; SITTINGS 1 (1:1-3:29 read), 1b (the compile; THE READBACK's first form BUILT) and 2 (chapter 4 read; 218 units; the Sifrei silent on it) DONE 2026-09-16; NEXT: the compile of chapter 4 (2b)"
assert m.count(a1) == 1
m = m.replace(a1, b1)
assert len(m.encode()) < 17000, len(m.encode())
open(ip, 'w', encoding='utf-8').write(m); print('MEMORY.md', len(m.encode()), 'bytes')
AFTER = {p: lint(p) for p in TOUCH}
print('lint after: ', {os.path.basename(p): n for p, n in AFTER.items()})
assert all(AFTER[p] <= BEFORE[p] for p in TOUCH), [(os.path.basename(p), BEFORE[p], AFTER[p]) for p in TOUCH if AFTER[p] > BEFORE[p]]
assert lint(WALKP) == 0 and lint(f'{MEM}/deuteronomy-walk.md') == 0
print('records written; the lints at or under their baselines; the map and the memory file lint 0')
