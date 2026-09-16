import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE DEUTERONOMY WALK sitting 1 — THE OPENING SPEECH (2026-09-15): the records — the stamp row, the NEW map World/step9/DEUTERONOMY_WALK.md
# ("Sitting 1"), the state doc's #182, World/RESUME.md, THE_STEPS' paragraph, THE_BRIEFING's bullet and entry, COMPILE_DEBT's box, RESEARCH_LOG's
# entry, MIDDOT's case-law block (the Sifrei's rows on the three chapters), the memory (a new file + the index), the recovery file's section 31, and
# the forms copied into World/step9/forms_deuteronomy_walk/ (copy_deu_forms.py). The counts below are the tools' own prints (the rituals' PASS lines
# and completion lines, the truth's units, the ledger writer's Counter, the manifest script's totals), typed from them; the corpus tripwire and the
# ritual prints are read back before a byte is written. Every insert lands on a unique anchor asserted present once. The gloss override rows were
# written by patch_overrides_deu.py at the ink step (asserted present by deu_ink.py) — verified here, not rewritten. MOVE_CATALOG.md and
# MISHNAH_TOPICS.md UNCHANGED (the rows' moves are known forms — exemplars entered in MIDDOT's case law; no Mishnah opened at a reading sitting; the
# AL TIKREI (13:6) is filed for MOVE_CATALOG at the compile). Sitting 15's form (write_ref_records.py).
import os, re, yaml, subprocess
ROOT = _ROOT
SP = os.path.dirname(os.path.abspath(__file__))
MEM = os.path.expanduser('~/.claude/projects/' + os.path.abspath(ROOT).replace('/', '-') + '/memory')
DATE = '2026-09-15'
UIDS = ['deu_01_frame_officers', 'deu_01_spies_refuse', 'deu_02_bypass_nations', 'deu_02_sihon', 'deu_03_og_gilead', 'deu_03_moses_barred']
truth = open(f'{ROOT}/logic/corpus/CORPUS_TRUTH.py', encoding='utf-8').read()
assert 'assert len(W["units"]) == 216' in truth and 'assert len(W["standing"]) == 2184' in truth and "== '8b8fff1fa28953af'" in truth, 'the fold is not the predicted one'
for n, u in enumerate(UIDS, 211):
    rit = open(f'{SP}/deu_ritual_{u}.out', encoding='utf-8').read()
    assert f'RITUAL COMPLETE for {u} ({n} frozen units)' in rit and rit.count('PASS ') >= 13, (u, n)
    assert os.path.exists(f'{ROOT}/logic/oral_audit/manifests/{u}_claims.json') and '  status: frozen' in open(f'{ROOT}/logic/units/{u}.yaml', encoding='utf-8').read() and os.path.exists(f'{ROOT}/logic/py_units/{u}.py'), u
assert os.path.exists(f'{ROOT}/logic/oral_triage/deu_01_03_devarim_{DATE}.md') and 'ALL_DONE' in open(f'{SP}/deu_chain.log', encoding='utf-8').read()
d_ov = yaml.safe_load(open(f'{ROOT}/logic/glosses/word_gloss_overrides.yaml', encoding='utf-8'))
assert len([k for k in d_ov['by_ref'] if k.startswith('Deut.')]) == 149 and d_ov['by_gloss']['the-pasture'] == 'the-wilderness' and d_ov['by_gloss']['leanness'] == 'only' and d_ov['by_gloss']['Red-Sea'] == 'Suph', 'the override rows are not the ink\'s'
assert os.path.isdir(f'{ROOT}/World/step9/forms_deuteronomy_walk')
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

STAMP = ('| 2026-09-15 | deu_01_frame_officers, deu_01_spies_refuse, deu_02_bypass_nations, deu_02_sihon, deu_03_og_gilead, deu_03_moses_barred | DELEGATED | FULL RULE | Deuteronomy 1:1-3:29 derivation 2026-09-15 (THE DEUTERONOMY WALK sitting 1 — THE OPENING SPEECH; the owner: "start with deuteronomy", on the rulings READ THEN COMPILE PER PORTION and CHAPTER NUMBERS NOT PORTION NAMES; the book\'s FIRST reading — the portion Devarim\'s three chapters as six drafts, the 211th to 216th frozen units): declared reading COMPLETE — Onkelos Deuteronomy 1:1-3:29 whole, 112 verses fresh; THE SIFREI ON DEUTERONOMY found BY POSITION — piskaot 1-25 on 1:1-1:28 and 26-30 on 3:23-3:29 (147 rows; the two files\' row grains EQUAL everywhere in the 357-piska export; NO piska on 1:29-3:22; heads 14 and 27 without a citation, continuing 1:14 and 3:24; every head asserted between its neighbors and against its rows\' own citations), each row read in BOTH files; the whole export scanned for rows of other piskaot citing the chapters — SEVEN Hebrew rows (37:9, 37:11, 52:1, 54:2, 82:5, 199:5, 314:2) and NINE English (36:10 and 37:2 added on 1:4; 199:5\'s English mis-citing 2:25 for 2:26), all seven CREDITED with a quick look; the one "ibid" candidate (355:27) resolving to Song of Songs 2:2, not Deuteronomy — the measurement pass\'s hit corrected by the ink; SIX rows of the thirty piskaot read before by topic in Genesis ledgers named at their rows (1:13, 6:1, 8:1, 11:1, 25:4, 27:3). Ledger logic/oral_triage/deu_01_03_devarim_2026-09-15.md (259 sources; coverage computed — missing 0, extra 0; the ink facts computed from the Tanakh DB and the snapshot store, every fact an assert — eight fell on the first typed pass of the shelf blocks, twenty-two on chapter 1\'s, eleven on chapter 2\'s, twelve on chapter 3\'s, each retyped from the leg print, none on the last; every quotation cut by consonants in glossed pieces, no cut miss on any rows file\'s first load; the lint 1 → 0 inside the writing step). 21 claims DV01A-01..05, DV01B-01..04, DV02A-01..04, DV02B-01..02, DV03A-01..04, DV03B-01..02 verified 21/21 by verify_claims, labeled (the strict census GREEN), seated as WITNESS_READ operators at their first verses; verify_text GREEN six times (18, 28, 25, 12, 22, 7 steps; 7 scenarios each); six freeze rituals 13 PASS each, RITUAL COMPLETE (211-216); the corpus rebaked to the prediction — units 216, standing 2184 (2163 + 21), hash 8b8fff1fa28953af UNMOVED; CORPUS TRUTH GREEN; build_world ALL GREEN; the journal gate GREEN; the register gate GREEN. THE PARSER: eleven number verses read, NO GAP (the fraction class — half Gilead, the half-tribe — named for the compile). The finds: the Sifrei\'s two islands (1:1-1:28, 3:23-3:29) and its silence over the oath, the defeat, the bypass, Sihon and Og; Onkelos writing the Sifrei\'s reading of the places as sins into 1:1; the receipt that receives the rules (1:3, Sifrei 2:8); one clock, two readers (1:3 [40, 11, 1] against Numbers 33:38 [40, 5]); the officers\' arithmetic (1:15\'s vavs; the rounding rule; 78,600); the judges\' charge as Avot 1:1 and Sanhedrin 4:1; the hard matter THE TENT\'s daughters; the spies\' words retold (Joshua and Caleb\'s "good is the land", Numbers 14:31 verbatim, Eden\'s "good and evil"); the spy-verb against the tour-verb; "enough for you" plural and singular; the retellings\' disagreement on Edom (2:29); the written and the read at 2:33; Numbers 21:33-35 quoted and turned; Og\'s bed by the cubit of a man; Joshua plene once in the Torah; the plea\'s names; Lebanon the Temple written at 3:25; the four directions in three orders; the run against the spec at Ai; the valley Peor\'s and Moses\' grave\'s. Stamp delegated under the AUTO-SEAT ruling; the owner may overrule. |\n')

WALK_HEAD = '''# THE DEUTERONOMY WALK — the fifth book in order from 1:1 (the owner: "start with deuteronomy", 2026-09-15, after NUMBERS CLOSED)

The owner's words (2026-09-15): "lets plan for deut next. where do we start" (the plan given: commit, the rereads, the measurement, the reading of
chapters 1-3, the compile; the readback's design his decision), "commit push" (29d477a), "I don't need to compact. read what you need to get ready",
"start with deuteronomy". This file is the walk's map: one section per sitting, the coverage computed at each close, the owed items named where
they are found. The rulings that govern it are the Numbers walk's (World/step9/NUMBERS_WALK.md; the memory numbers-in-order-ruling.md): READ THEN
COMPILE PER PORTION, never read ahead; CHAPTER NUMBERS, never portion names; the parashah grain; the spine Onkelos whole + the Sifrei on
Deuteronomy where it has a piska BY POSITION (logic/CORE_SHELF.md's spine default of 2026-08-27).

THE WALK'S FORM (the derivation era's, THE_STEPS Steps 2-5): each portion is one READING SITTING — the measurement passes first (the shelf by
position, both files' row counts, every row's first citation, the four-form scan for rows outside the span, the parser on every verse, the frames
and the register, the prior reads, the drafts' spans, the store's token counts and glosses), then the ink as asserts run all at once, then the rows
(Onkelos per verse; the Sifrei per row in both files, the middah named), then ONE ledger written by one script with coverage computed, the
display layer's override rows patched from the ink's own literals, the manifests with every check cut from the store's bytes, the seat script,
the rituals in sequence, the fold predicted and matched, the stamp row, the records — then a COMPILE SITTING (the design in this file before code;
probes to fail; the docket; the runner; the tape; every gate with the register gate --strict; the sweep). THE READBACK (THE_LOOP.md's STEP 6) is
designed at this book on the owner's word — Deuteronomy is the tape read back, the speech retelling what the tape holds.

THE SHELF ON DEUTERONOMY, MEASURED (sitting 1): the Sifrei on Deuteronomy's export holds 357 piskaot and 2,357 rows in BOTH files, and NO
row-count mismatch anywhere (the Numbers walk's duplicated-block class absent); piska 1 opens on 1:1 (twenty rows); 1-25 cover 1:1-1:28, 26-30
cover 3:23-3:29, 31 opens at 6:4; the Hebrew citation form "(דברים א א)" ("Deuteronomy 1:1" in Hebrew letters), the English "(Dt.1:1)" with no
space — and the English rows carry the translator's apparatus (page notes, inline footnotes), a defect class read past, never a row; heads 14 and
27 carry no citation (they continue 1:14 and 3:24). Onkelos Deuteronomy: 34 chapters, 956 verses in the export (the DB's 959), chapters 1-3 at 46,
37, 29 — the DB's division. The other 26 works on Deuteronomy stay enumerated outside declared scope (the ledger names them). THE OWED SEATS
filed at Numbers (the register gate's "the book not read" rows: 1:1 an EMPTY footer, 1:3, 1:19, 1:41 NONE; and the owed seats in chapters 4, 12,
17, 19, 21, 25) are paid by the compile sittings as the walk reaches them.
'''

WALK = '''
## Sitting 1 — THE OPENING SPEECH, Deuteronomy 1:1-3:29 (2026-09-15; the owner: "start with deuteronomy" after the rereads, on the rulings READ THEN COMPILE and CHAPTER NUMBERS): the reading and the units

THE DRAFTS: six cover the portion exactly — computed from the Tanakh DB's verse table: 112 of 112 verses, missing 0 — deu_01_frame_officers 1:1-18,
deu_01_spies_refuse 1:19-46, deu_02_bypass_nations 2:1-25, deu_02_sihon 2:26-37, deu_03_og_gilead 3:1-22, deu_03_moses_barred 3:23-29 (the step ids
STEP_Dt_<chapter>_<verse>; the scenarios in the tree form before the seat). Read in ONE pass, one ledger. The forms copied from the Numbers walk's
sitting 15 (World/step9/forms_numbers_walk/) and edited, then copied at the close into World/step9/forms_deuteronomy_walk/ (deu_dump0.py,
deu_parser0.py, deu_measure0.py, deu_measure1.py, deu_measure2.py, deu_ink.py with assert_driver.py and deu_legs.py, deu_rows_onkelos_a/b/c.py,
deu_rows_sifrei_a/b/c/d.py, write_deu_ledger.py, patch_overrides_deu.py, write_deu_manifest.py, seat_deu.py, deu_chain.sh, copy_deu_forms.py,
write_deu_records.py; the legs files).

THE SHELF, BY POSITION (deu_ink.py's asserts): piskaot 1-25 head on 1:1 through 1:28 in order (1 on 1:1 with twenty rows; 7 and 8 both on 1:8; 14
without a citation, continuing 1:14; 15 headed "1:15-16"), 26-30 on 3:23 through 3:29 (27 without a citation, continuing 3:24) — 116 + 31 = 147 rows,
the two files' grains EQUAL; NO PISKA ON 1:29-3:22 (the shelf's silence over the oath, the defeat at Hormah, the bypass, Sihon and Og); 31 opens at
6:4. THE CITATION FORMS: the Hebrew "(דברים א א)" ("Deuteronomy 1:1"), the English "(Dt.1:1)" WITH NO SPACE (3,292 such parens over the export,
one "Deut."), and the English rows' translator's apparatus (page notes "H:23-27; JN1:15-23", inline footnotes — 38 digit-before-capital markers in
piska 1's twenty rows) read past: a defect class, not a row (RESEARCH_LOG.md). THE "FOUND BY POSITION" CLAUSE on the whole export: SEVEN Hebrew
rows outside 1-30 cite chapters 1-3 — 37:9 (Hermon's names, 3:9), 37:11 (Pisgah among Nebo's three names, 3:27), 52:1 ("no man" — even Og, 3:11),
54:2 (the rebuke near death — "after he had smitten Sihon", 1:4), 82:5 (the priestly blessing not lengthened by 1:11), 199:5 (Moses loved peace —
2:26's messengers), 314:2 (the eagle — "as a man carries his son", 1:31); NINE English rows — the seven and 36:10 and 37:2 (both citing 1:4 where
the Hebrew rows carry Song of Songs 6:4 and Numbers 13:22 alone), and 199:5's English cites 2:25 for the Hebrew's 2:26 (a mistyped verse). THE
ONE "IBID" CANDIDATE, 355:27's "ibid. 2:2", follows Song of Songs 2:3 — Song 2:2, NOT Deuteronomy 2:2 (the measurement pass's hit CORRECTED by the
ink: the ibid resolves to the nearest book named, not the nearest Deuteronomy). All seven credited with a quick look. THE PRIOR READS: no ledger
had read an Onkelos row of Deuteronomy; SIX rows of the thirty piskaot were read by topic in the Genesis ledgers — 1:13 (the complaint template:
gen_09, gen_10), 6:1 (the 1:7 geography: gen_24, material), 8:1 (the Land given as-is: gen_29, material), 11:1 (the guardian parable: gen_29), 25:4
(the hyperbole: gen_29, material), 27:3 (the servant census: gen_27) — named at their rows, never counted fresh (a strict row-form census, "Sifrei
Devarim p:r" — the loose form had matched num_32's "Sifrei Devarim on 3:12-20", a naming); that deferral closes EMPTY (no piska on 3:12-20);
forty-four ledgers name a verse of the three chapters.

THE READING (the modules): deu_dump0.py the shelf by position (both files' row counts, every row's first citation, the outside-row scan, the
dumps); deu_parser0.py the parser, the case tokens, the frames, the "saying" seats, the narrative verbs, the names per verse; deu_measure0.py the
register gate's lines, the prior reads, the shelf's works, the drafts, the store's token counts; deu_measure1.py sections A-J (the outside rows
whole, the retellings DIFFED against Numbers token by token, the phrase censuses over the whole DB, Onkelos's renderings); deu_measure2.py
Onkelos's tokens' seats over the whole book, the store's gloss families censused (every candidate rewrite's family printed before a row was
decided); deu_ink.py the ink with every fact an assert (assert_driver.py: EIGHT fell on the first typed pass of the shelf blocks — the English
apparatus prefixing rows 14:1 and 27:1, the heads' None at 14 and 27, a Counter's first-word split (דברים "Deuteronomy" begins with the letters of
דברי "the words of"), the English "Dt." count measured on the parens not the words, a meteg (a stress mark) in Numbers 33:38's pointed form, the
dispositions' quoted why; TWENTY-TWO on chapter 1's block, ELEVEN on chapter 2's, TWELVE on chapter 3's — nearly every one a count typed from
the measurement pass's looser regex (the bare token against the family: "well" 38 not 43, "except" 9 not 15, Hermon 11 not 14, Chinnereth 6 not 9,
Aroer 11 not 16, the armed-word 3 not 18, Joshua 177 not 197, Rephaim 19 not 28, the Avvim 4 not 6, the Perizzite family 27 not 15), a lemma with
a letter ("2603 a", "5674 b", "6696 b", "3739 a"), a sort order (LEMT's verse order against the sorted literal), the LEMV of the dig-root (twenty-one
seats, one lemma — no separate spy sense), the fill-after phrase's five forms, the hitpael filtered by "Vt" on the morph; each retyped from the
leg print (deu_legs.py), none on the last pass; the gloss block's two — my own lists' counts (149 and 126 typed as 147 and 134) and TEN families
already rewritten by earlier sittings (the patch's guard caught them; their rows stand); the ink's written-once guards fired THREE times on the same
sitting's reruns (the manifests' existence, the units' draft state, the prefixes' absence) — scoped to the first pass, a lesson); the piece-wise
cutters HP / AP / SP_ (no cut miss on any rows file's first load); deu_rows_onkelos_a/b/c.py the 112 rows; deu_rows_sifrei_a/b/c/d.py the 147 rows
(each read in both files, the middah named; the six prior-read rows marked); write_deu_ledger.py the writer → ONE ledger
logic/oral_triage/deu_01_03_devarim_2026-09-15.md (259 sources: Onkelos MATERIAL 91 / CONTEXT 21; the Sifrei MATERIAL 99 / CONTEXT 48; seven rows
credited; coverage computed, missing 0, extra 0; gloss_lint 1 → 0 inside the writing step — "notarikon" glossed; the same-sitting rewrites swapped in
whole by a temp path); the display layer's rows written at the ink step by patch_overrides_deu.py (ONE HUNDRED AND FORTY-NINE by reference with
the token named beside each, ONE HUNDRED AND TWENTY-SIX by gloss — the families censused first; the rows read from the ink module's own literals).

THE INK, COMPUTED (the measurement passes FIRST, the asserts typed from the print):
- THE PARSER MEASURED FIRST: ELEVEN number verses in 112 read, NO GAP — 1:2 [11]; 1:3 [40, 11, 1] by the NUMBER reader where Numbers 33:38's
  ordinal date read [40, 5] by the ORDINAL reader (ONE CLOCK, TWO READERS: "in forty years" against "in the year of the forty" — Aaron's death in
  the fifth month and Moses' speech in the eleventh, six months apart; the Sifrei 2:3 counts thirty-three days from the date to the Jordan); 1:11
  [1000]; 1:15 [100, 50, 10] with THE THOUSANDS A PLURAL NOUN (rule 29, as at Exodus 18:21, 25); 1:23 [12, 1]; 2:7 [40]; 2:14 [38]; 3:4 [60]; 3:8 [2]
  with the construct mark; 3:11 [9, 4]; 3:21 [2]; no ordinals. THE FRACTION CLASS UNREAD — "half the hill country of Gilead" (3:12), "the half-tribe"
  (3:13): named for the compile. The tokens 654 + 532 + 461 = 1,647.
- THE FRAMES AND THE REGISTER: SEVEN divine frames, ALL IN MOSES' VOICE — "and the LORD said to me" at 1:42, 2:2, 2:9, 2:31, 3:2, 3:26 and "AND THE
  LORD SPOKE TO ME" at 2:17, THE BIBLE'S ONLY SEAT of that form; "saying" at fourteen seats (the Sifrei 26:9 reads the superfluous one as "tell me
  whether"); the narrative verbs in the FIRST PERSON — the story retold by its actor; 3:1-3 against Numbers 21:33-35 diffed token by token ("they
  turned" → "we turned", "to meet them" → "to meet us", "to Moses" → "to me", "and they smote him and his sons" → "and the LORD our God gave into our
  hand also Og"); 1:40 against 14:25, 1:42 against 14:42, 2:27 against 21:22 (nine tokens for seventeen — the field, the vineyard, the well and the
  king's road become "by the road, by the road"), 2:32 against 21:23 (eight for twenty), 3:14 against 32:41 (twenty-three for eleven). THE CASE
  TOKENS: "for" fifteen, "if" once (1:35's oath), no "and if", no "or" — NO CASE in the three chapters: the compiler law's structure absent, the span
  narrative. "AT THAT TIME" ten times (the refrain). THE REGISTER GATE: 1:1 EMPTY footer, 1:3, 1:19, 1:41 NONE — "the book not read", the seats
  waiting for the compile; 1:3's receipt form the two-seat clause with Exodus 40:16 that the Sifrei 2:8 reads as the receipt of the hermeneutic
  rules themselves.
- THE CROWNS (twenty, the ledger's finds): the Sifrei's TWO ISLANDS (1:1-1:28, 3:23-3:29) and its silence between; the translation writing the
  Sifrei into 1:1 (thirty-three tokens for twenty-two — "he rebuked them for that they sinned in the wilderness ... scorned the manna ... the calf
  of gold": the book's one "rebuked"; the dispute the Sifrei holds open at 1:18 — R. Judah's ten trials against R. Yose ben Dormaskit's plain places
  named for events — decided by the translator for R. Judah); THE RECEIPT THAT RECEIVES THE RULES (1:3); ONE CLOCK, TWO READERS (1:3 / Numbers
  33:38); THE OFFICERS' ARITHMETIC (1:15's vavs one seat against Exodus 18:21, 25 without; the Sifrei 15:4's rounding rule — 1,999 yields one
  captain of a thousand; 14:1's "eighty thousand less a few" = 78,600 by the count; 1:13's three qualities against Jethro's four and 1:15's two —
  seven asked, three found); THE JUDGES' CHARGE IS THE TESTING SHELF'S OWN (Avot 1:1 on 1:16, Sanhedrin 4:1 on 1:18 — the Sifrei citing the Mishnah
  as the verse's reading; the judge liable in his person; the appointer of judges; the compromise dispute; R. Ishmael and the gentile litigant; the AL
  TIKREI "their guilt on your heads"); THE HARD MATTER IS THE TENT'S (1:17 — Zelophehad's daughters, Numbers 27, a reference taught); THE SPIES'
  WORDS RETOLD ("good is the land" JOSHUA AND CALEB'S — Numbers 14:7 and this, the two seats, the Sifrei 23:3 asking who said it; "some of the fruit"
  Moses' charge 13:20; "your little ones a prey" Numbers 14:31 VERBATIM; "good and evil" EDEN'S phrase — the tree's four seats and this; "turn and
  journey" 14:25's; "I am not among you" 14:42's with the person changed; "beat you down to Hormah" 14:45's with Seir added); THE SPY-VERB AGAINST
  THE TOUR-VERB (1:24's piel where Numbers 13-14 tour twelve times; 1:22's dig-root in its spy sense here and Joshua 2:2-3 alone); ENOUGH FOR YOU,
  PLURAL AND SINGULAR (Korah's cry 16:3, 7; 1:6, 2:3, 3:19; Jeroboam's; and the singular once, 3:26 on Moses); THE RETELLINGS DISAGREE ON EDOM (2:29
  against Numbers 20:18-21 and Judges 11:17 — the Sifrei silent: THE COMPILE'S OWED QUESTION); THE WRITTEN AND THE READ AT 2:33 (the store's twelve
  tokens for the DB's eleven; Onkelos reads the plural); NUMBERS 21:33-35 QUOTED AND TURNED; OG'S BED BY THE CUBIT OF A MAN (nine by four; the hapax
  phrase; Onkelos "the cubit of a king"; the outside row 52:1); JOSHUA SPELLED PLENE ONCE IN THE TORAH (3:21; Judges 2:7 the Bible's other);
  3:20 quoted whole at Joshua 1:15, 3:16's Jabbok clause at Joshua 12:2, 3:22's fight-clause at Joshua 23:3, 10; THE PLEA'S NAMES ("O LORD GOD"
  Abraham's two seats and Moses' two; "your greatness" the Sifrei 27:4's binyan av named; "your strong hand" Solomon's prayer; Onkelos turning "what
  god" into "God whose Shekhinah is in the heavens above and rules on earth"); LEBANON THE TEMPLE WRITTEN AT 3:25 (the Sifrei 6:2 and 28:3 at both
  seats; Onkelos keeps Lebanon at 1:7, writes the sanctuary at 3:25); THE FOUR DIRECTIONS IN THREE ORDERS (3:27 west-north-south-east; Genesis 13:14
  north-south-east-west; Genesis 28:14 west-east-north-south — the Sifrei 29:5's compass of prayer); THE RUN AGAINST THE SPEC AT AI (3:28 read by the
  Sifrei 29:8-9 as the condition Joshua broke — "you sent them and did not go after them"); THE VALLEY PEOR'S AND MOSES' GRAVE'S (3:29 with 4:46 and
  34:6). ONKELOS OVER THE BOOK: the Memra eleven bare seats, five "by the Memra", ten "his Memra" (3:22 "his Memra fights for you"); "my Shekhinah"
  five (1:42 "my Shekhinah does not dwell among you"); "from before the LORD" fourteen (1:37, 3:26 "there was anger from before the LORD"); "the fear
  of the LORD" supplied at twelve; "did not accept" 1:45 and 3:26 — the people's weeping and Moses' plea in one phrase; Kadesh-barnea REKAM GEYAH,
  Bashan MATHNAN, Ar LEHAYATH, the Emim THE TERRIBLE ONES, the Zamzummim THE SCHEMERS, the Caphtorim CAPPADOCIANS, Argob TRACHONA, Senir THE SNOW
  MOUNTAIN, Chinnereth GENNESAR, Pisgah THE HEIGHT, the Maacathite APKEROS.

THE SIFREI'S OWN CASE LAW (the block in MIDDOT.md): the genre from the redundancy (1:1 — "these words" against the whole Torah, I5, proved on
Amos, Jeremiah, David, Solomon); the places read as charges (1:9-17 — the aggadic name-reading; 1:18's dispute held open); the receipt of the rules
(2:8); the twelve months from the date (2:3); the rebuke near death and its four reasons (2:4-7); king and province (3:3-4, I1); "undertook" fixed
from its seats — a dispute (4:1, E7); "enough" as much (5:2); Lebanon from its seats (6:2, 28:3, E7); the judge's liability in his person (9:2);
the AL TIKREI (13:6); the two money-changers (13:3); the count and the rounding (14:1, 15:4); Avot 1:1 and Sanhedrin 4:1 seated (16:1, 18:1); the
appointer of judges (17:1); silence before hearing, the compromise dispute (17:4); the hard matter (17:7); "all of you" against 5:20 (20:1, E7);
named for its end (22:2); who said "good is the land" (23:3); the hyperbole rule (25:4); the ten names of prayer (26:7); the superfluous "saying"
(26:9, I5); the two Names (26:10); the binyan av named (27:4, I3); "enough" three readings (29:2-4); the directions of prayer (29:5); the rope of
fifty cubits (29:6 — the shelf's measure, not the ink's); if he crosses they cross — Ai (29:8-9). MOVE_CATALOG unchanged (the AL TIKREI filed for the
compile); MISHNAH_TOPICS unchanged (no Mishnah opened at a reading sitting — the tractates routed to the docket).

THE CLAIMS (write_deu_manifest.py → six manifests, 21 claims — DV01A-01..05, DV01B-01..04, DV02A-01..04, DV02B-01..02, DV03A-01..04, DV03B-01..02 —
every check the word's LONGEST STORE-PIECE WHOLE; the ID prefixes asserted absent; every cite checked against the ledger's CITE INDEX and EVERY
name of the index used by a claim, asserted; the middah labels ink with the forms named — I1, I2, I3, I5, E7, the aggadic name-reading, the AL
TIKREI, LR1 where the Sifrei teaches a link, and the open question at 2:29 named a HYPOTHESIS): verify_claims 21 VERIFIED / 0 FAILED; claim_labels_census
--strict GREEN (the labels' codes read from MIDDOT's own list after a wrong code — E4 for the narrative verbal analogy E7 — was caught and relabeled
before the seat). THE SEATS (seat_deu.py, the Numbers form with STEP_Dt_ ids): 21 WITNESS_READ operators at the claims' first verses (5 on
1, 6, 9, 14, 16; 4 on 19, 26, 34, 41; 4 on 2:1, 9, 16, 24; 2 on 2:26, 31; 4 on 3:1, 8, 12, 18; 2 on 3:23, 26), step E in each, the scenarios in the
anchor form; verify_text GREEN six times (18, 28, 25, 12, 22, 7 steps; 7 scenarios each). THE RITUALS (deu_chain.sh): every gate PASS (13 PASS
each) — RITUAL COMPLETE for the 211th through 216th frozen units; the Python rendering layer written and self-proved six times. THE CORPUS REBAKED
(predicted before the fold: units 216, standing 2163 + 21 = 2184, hash unmoved — the tripwire's literals set to the prediction before the bake):
units 216, standing 2184, hash 8b8fff1fa28953af — the prediction matched; CORPUS TRUTH GREEN; build_world ALL GREEN (the fold layer of the one
database); the journal gate GREEN (12 kinds, 9,628 rows); the register gate GREEN (the four Deuteronomy seats standing as filed until the compile).
THE STAMP: one delegated FULL RULE row naming the six units (logic/findings/STAMP_LEDGER.md). No engine file changed at this sitting — the sweep as
at Numbers' close.

OWED TO THE COMPILE (sitting 1b; the box in COMPILE_DEBT.md, items (a)-(l)): THE READBACK'S DESIGN on the owner's word (the speech as the tape read
back: 1:19-46 against the tape's Numbers 13-14 acts, 2:1-3:22 against Numbers 20-21 and 32 — the diffs measured here are the readback's first
specimens); THE REGISTER GATE'S FOUR SEATS PAID (1:1 the footer, 1:3 the receipt of the rules, 1:19 and 1:41 the receipt forms); THE OFFICERS'
TABLE (1:15's four grains with the rounding rule and the 78,600 as DATA; the seven qualities as a checklist; the Levites with the strap); THE
JUDGES' CHARGE as the law's spec (hear, judge righteously, no faces, small and great, no fear, the hard matter up — with Avot 1:1 and Sanhedrin
4:1 as the exam's rows; the compromise dispute two verdict tables; R. Ishmael's two rulings); THE FRACTION CLASS taught to the parser (3:12's half,
3:13's half-tribe — probes to FAIL); THE ONE CLOCK (1:3's date joined to Numbers 33:38's on the tape's clock; the Sifrei 2:3's thirty-three days);
THE RETELLINGS AS THE TAPE'S MEMORY (1:39 verbatim, 3:1-3 turned, 2:27 and 2:32 shortened — each a REFERENCE to the compiled act; 2:29's Edom
disagreement an OPEN question, a HYPOTHESIS row, no link of our own); THE EAST'S GRANTS by REFERENCE to gad_reuben's cells (3:12-17 the grant read
back; Jair's, Machir's; Havvoth-jair to this day); THE ARMED PASSAGE by REFERENCE to Numbers 32's condition (3:18-20; Joshua 1:15 the run outside the
Torah — THE READBACK's); JOSHUA'S CHARGE (3:21-22, 28 — Numbers 27:19-23 by REFERENCE; Joshua 1:6 and Ai the run); THE PLEA (3:23-29 — the ten
names of prayer as the effects registry's candidates; the directions of prayer as DATA; the four directions' three orders); THE DOCKET by the union
rule — Sanhedrin 1:1-6 and 4:1 with 2a-b, 32a-b, Sanhedrin 3:1-8 with 23a-31b (6b-7a the compromise), 1:6 with 16b-17a, Avot 1:1, Sheviit 9:2, Rosh
Hashanah 1:1 with 2b-3a, Sotah 7:5 and 34a-35a, Berakhot 4:5-6 with 30a, Makkot 2:4-8 and 9b-10a, Kelim 17:9-10 and Eruvin 4:8 (the cubit of a man),
Sanhedrin 90b-91a; the store's mixed families a display sitting's; the AL TIKREI for MOVE_CATALOG.

⚠ LESSONS (9): THE IBID RESOLVES TO THE NEAREST BOOK NAMED, NOT THE NEAREST DEUTERONOMY — a scan that keys "ibid" to the last Deuteronomy citation
finds a false row (355:27); walk the parens in order. THE ENGLISH ROWS CARRY THE APPARATUS — page notes and footnote numerals glued to the words;
read past them, count the markers, never a row. THE PRIOR-READ CENSUS TAKES THE ROW FORM STRICTLY — "Sifrei Devarim p:r", never "on c:v" (a naming
matched as a read). A COUNT TYPED FROM A LOOSER REGEX IS A DIFFERENT NUMBER — the measurement pass's family counts against the ink's bare-token
counts fell twenty times; type the count from the ink's own leg. THE LEMMA CARRIES A LETTER — "2603 a", "5674 b": read the lemma from the print.
THE LABEL CODES ARE MIDDOT'S OWN — read the list before labeling (E7 is the narrative verbal analogy; E4 is a particle rule). A WRITTEN-ONCE GUARD
FIRES ON THE SAME SITTING'S RERUN — scope the guards (the manifests' absence, the units' draft state, the prefixes' absence) to the first pass, and
swap a rewritten ledger in whole by a temp path while a chain runs. TEN FAMILIES WERE ALREADY REWRITTEN — grep the override file's keys before
typing a by-gloss list. THE READING SITTING'S SHAPE HELD ON A NEW BOOK: dump → parser → measure (three passes) → asserts (8, 22, 11, 12 → 0) →
rows (112 + 147) → writer (0 misses; lint 1 → 0) → patch → manifests (21/21) → seat → six rituals (13 PASS each) → the fold predicted and matched.

NEXT on the ruling: THE COMPILE OF DEUTERONOMY 1-3 (sitting 1b) on the Numbers walk's order — the measurements (the tape's state at Numbers 36:13;
the callees live: the shelach and rejection runners, chukat, the conquest, gad_reuben, journeys, zelophehad and joshua's commissioning; the register
gate's four seats), THE DESIGN in this file before any code (THE READBACK's first design on the owner's word; the fraction's probes; the officers'
table; the judges' spec; the one clock; the retellings by reference; the docket), the probes to FAIL, the runner, the tape, every gate with THE
REGISTER GATE --strict at the gates step, the sweep — then chapter 4 (the reading), and on in order.
'''

STATE = '''
═══ COMPACTION POINT #182 (2026-09-15 — written at THE DEUTERONOMY WALK sitting 1's close; THE OPENING SPEECH 1:1-3:29 READ AND FROZEN — the book's first six units; NOT YET COMPILED; A CLEAN COMPACTION POINT; the last commit 29d477a) ═══
STATE: 216 frozen units (210 + 6), standing 2184 (2163 + 21 as predicted), hash 8b8fff1fa28953af UNMOVED; CORPUS TRUTH GREEN; build_world ALL GREEN; the journal gate GREEN (12 kinds, 9,628 rows); the register gate GREEN (Deut 1:1 EMPTY, 1:3 / 1:19 / 1:41 NONE — "the book not read" until the compile); 57 runners, 62 daemons, the sweep as at Numbers' close (no engine file changed); RUN (1279, 66, 52, 0, 12, 1527, 33, 318, four pairs, 121) unmoved. UNCOMMITTED: the six units FROZEN (logic/units/deu_01_frame_officers.yaml, deu_01_spies_refuse.yaml, deu_02_bypass_nations.yaml, deu_02_sihon.yaml, deu_03_og_gilead.yaml, deu_03_moses_barred.yaml); logic/oral_triage/deu_01_03_devarim_2026-09-15.md NEW (one ledger, 259 sources); the six manifests logic/oral_audit/manifests/deu_*_claims.json NEW; the six logic/py_units/deu_*.py NEW and ALL_UNITS.py; the six UNIT_deu_*.html and UNIT_INDEX.html; logic/corpus/CORPUS_TRUTH.py (216 / 2184); logic/glosses/word_gloss_overrides.yaml (+149 by reference, +126 by gloss); logic/findings/STAMP_LEDGER.md; World/step9/DEUTERONOMY_WALK.md NEW ("Sitting 1"); World/step9/COMPILE_DEBT.md (the Deuteronomy sitting-1 box); logic/MIDDOT.md (the Deuteronomy block); RESEARCH_LOG.md; THE_STEPS.md; THE_BRIEFING.md; World/RESUME.md; World/step9/forms_deuteronomy_walk/ NEW (this sitting's scripts copied in); the recovery file's section 31; the memory (deuteronomy-walk.md NEW, MEMORY.md's lines); #180's addenda 3-4, #181 and this doc — commit only on "commit push" (the NEVER-COMMIT set and the staging-by-exclusion form as before).
THE SITTING (the owner: "start with deuteronomy" after "lets plan for deut next. where do we start" and the rereads; DEUTERONOMY_WALK.md "Sitting 1"): chapters 1-3 read as SIX drafts (the chapter numbers the names) from the Numbers walk's sitting-15 forms: THE SIFREI ON DEUTERONOMY found BY POSITION — piskaot 1-25 on 1:1-1:28 and 26-30 on 3:23-3:29 (147 rows, the two files' grains EQUAL everywhere in the 357-piska export; NO piska on 1:29-3:22; heads 14 and 27 without a citation), each row read in both files; seven outside rows credited (the English adding two on 1:4 and mis-citing 199:5; the one "ibid" resolving to Song of Songs, the measurement pass's hit corrected); six rows read before by topic named; Onkelos whole (112) = 259 sources in one ledger (the asserts fell 8, 22, 11, 12 on the typed passes — the looser regex's counts, the lemma letters, the sort orders, the guards — none on the last; no cut miss; the lint 1 → 0); 21 claims verified and labeled (E4 → E7 caught by MIDDOT's list), 21 operators seated on 21 steps, six rituals COMPLETE (13 PASS each) → 216 units, standing 2184, hash unmoved (predicted); the display layer's 275 rows (149 by reference, 126 by gloss; ten families already rewritten). THE PARSER: eleven number verses read, NO GAP (the fraction class named). THE FINDS: the Sifrei's two islands; Onkelos writing the Sifrei into 1:1; the receipt that receives the rules; one clock, two readers; the officers' arithmetic (the rounding rule, 78,600); the judges' charge Avot 1:1's and Sanhedrin 4:1's; the hard matter THE TENT's; the spies' words retold (Joshua and Caleb's "good is the land"; Numbers 14:31 verbatim; Eden's "good and evil"); the spy-verb against the tour-verb; "enough for you" plural and singular; the retellings' disagreement on Edom (2:29 — the compile's open question); the written and the read at 2:33; Numbers 21:33-35 quoted and turned; Og's bed by the cubit of a man; Joshua plene once; the plea's names (Abraham's "O LORD God"; the binyan av on "your greatness"); Lebanon the Temple written at 3:25; the four directions in three orders; the run against the spec at Ai; the valley Peor's and Moses' grave's.
THE RECORDS: DEUTERONOMY_WALK.md "Sitting 1" (NEW); the ledger, the six manifests and py renderings; RESEARCH_LOG.md's entry; COMPILE_DEBT.md's Deuteronomy box (a)-(l); MIDDOT.md's Deuteronomy block; STAMP_LEDGER's row; THE_STEPS' paragraph; THE_BRIEFING's scoreboard bullet and entry; the gloss override rows; World/RESUME.md; the forms copied into World/step9/forms_deuteronomy_walk/; memory (deuteronomy-walk.md NEW; MEMORY.md's index line and the numbers and loop lines' NEXT pointers); the recovery file's section 31; this entry.
NEXT on the ruling: SITTING 1b — THE COMPILE OF DEUTERONOMY 1-3 on the Numbers walk's order (DEUTERONOMY_WALK.md's owed list (a)-(l): THE READBACK's design on the owner's word first — the speech as the tape read back, the diffs against Numbers 13-14, 20-21, 32 as its specimens; the register gate's four seats paid; the officers' table; the judges' spec; the fraction's probes; the one clock; the retellings by reference and 2:29's open question; the east's grants, the armed passage and Joshua's charge by reference; the plea's vocabulary; the docket by the union rule) — the design in DEUTERONOMY_WALK.md before any code — then chapter 4's reading, and on in order.
POST-COMPACTION REREADS (mandatory, first sitting): the recovery file logic/pre_logic_methods_2026-07-28/RECOVERY_new_thread_2026-09-12.md whole (its section 5 THE COMPILE SITTING; its sections 30 and 31) + the memory deuteronomy-walk.md + numbers-in-order-ruling.md + this entry + DEUTERONOMY_WALK.md whole + NUMBERS_WALK.md "Sitting 15b — AS BUILT" (the compile's form) + THE_STEPS Step 2 + Step 5 + the compiler block + THE_LOOP.md's STEP 6 (THE READBACK, owed) — before deriving.
'''

RESUME = '''DEUTERONOMY SITTING 1 DONE 2026-09-15 (THE OPENING SPEECH 1:1-3:29 READ AND FROZEN — the book's first six units, the chapter numbers their names; World/step9/DEUTERONOMY_WALK.md "Sitting 1" NEW; the owner: "start with deuteronomy" after the rereads): THE SIFREI ON DEUTERONOMY found BY POSITION — piskaot 1-25 on 1:1-1:28 and 26-30 on 3:23-3:29 (147 rows; the two files' grains equal everywhere in the 357-piska export; no piska on 1:29-3:22; heads 14 and 27 without a citation; every head checked against its rows' own citations), each row read in both files; seven outside rows credited (the English adds two rows on 1:4 and mis-cites 199:5; the one "ibid" resolves to Song of Songs — the measurement's hit corrected); six rows read before by topic in Genesis ledgers named + Onkelos whole (112) = 259 sources in ONE ledger (the asserts fell 8, 22, 11, 12 on the typed passes — the looser regex's counts, the lemma letters, the sort orders, the guards — none on the last; no cut miss; the lint 1 → 0); 21 claims verified and labeled (E4 → E7 caught by MIDDOT's list), 21 operators seated, six rituals COMPLETE (13 PASS each) → 216 units, standing 2184, hash unmoved (predicted); build_world and the journal gate GREEN; THE PARSER eleven number verses read, NO GAP (the fraction class — half Gilead, the half-tribe — named for the compile); the display layer's 275 rows; THE FINDS: the Sifrei's two islands and its silence over the oath, the defeat, the bypass, Sihon and Og; Onkelos writing the Sifrei's reading of the places as sins into 1:1; the receipt that receives the rules (1:3, Sifrei 2:8); one clock, two readers (1:3 against Numbers 33:38); the officers' arithmetic (the rounding rule, 78,600); the judges' charge Avot 1:1's and Sanhedrin 4:1's; the hard matter THE TENT's daughters; the spies' words retold (Joshua and Caleb's "good is the land", Numbers 14:31 verbatim, Eden's "good and evil"); the spy-verb against the tour-verb; "enough for you" plural and singular; the retellings' disagreement on Edom (2:29 — the compile's open question); the written and the read at 2:33; Numbers 21:33-35 quoted and turned; Og's bed by the cubit of a man; Joshua plene once in the Torah; the plea's names; Lebanon the Temple written at 3:25; the four directions in three orders; the run against the spec at Ai; the valley Peor's and Moses' grave's. NEXT: 1b — THE COMPILE OF DEUTERONOMY 1-3 (DEUTERONOMY_WALK.md's owed list (a)-(l): THE READBACK's design on the owner's word first; the register gate's four seats paid; the officers' table; the judges' spec; the fraction's probes; the one clock; the retellings by reference; the docket) — then chapter 4's reading, and on in order.
'''

STEPS = '''DEUTERONOMY — SITTING 1 — THE OPENING SPEECH, Deuteronomy 1:1-3:29 (2026-09-15, on Brian's "start with deuteronomy" after the rereads; World/step9/DEUTERONOMY_WALK.md
"Sitting 1"). The book opened the way Numbers was walked: the three chapters of the first portion read as six units named by their chapters, on Onkelos
whole and the Sifrei on Deuteronomy found by its position in the export — and the shelf turned out to be two islands: twenty-five piskaot on the
first twenty-eight verses (the rebuke's places, the officers, the spies sent) and five on the last seven (the plea), with nothing at all on the
oath, the defeat at Hormah, the years of going round, Sihon and Og. Every row read in both files; the two files agree row for row here, unlike
Numbers' shelf, but the English carries its translator's page notes glued to the words, and it cites two rows the Hebrew does not and mis-cites a
third. The parser measured first: eleven number verses, every one read — the date of the speech read by the number reader where Aaron's death in
Numbers 33 was read by the ordinal reader, one year in two forms six months apart; the only thing unread is a fraction, "half" Gilead and the
"half-tribe", a class named for the compile. The finds: the translation writes the Sifrei's reading of the six place-names as six sins straight into
the first verse; the receipt "according to all the LORD commanded him" — the two-seat clause with the tabernacle's — is read by the Sifrei as the
receipt of the hermeneutic rules themselves; the officers' verse carries its vavs where Exodus 18 does not, and the Sifrei gives the compile its
arithmetic (round down at every grain; eighty thousand judges less a few); the judges' charge is the Mishnah's own first saying and its ten
distinctions; the "hard matter" is Zelophehad's daughters, the tent's case; the spies' story is retold in the spies' own words — Joshua and Caleb's
"good is the land", Numbers 14:31 verbatim, and Eden's "good and evil" on the children; "enough for you" is Korah's cry three times over and once,
singular, on Moses; the retellings disagree on Edom, and the shelf is silent there — an open question for the compile; a word is written "his
son" and read "his sons"; Og's bed is measured by the cubit of a man and Onkelos makes it a king's; Joshua's name is spelled full once in the Torah;
Lebanon becomes the Temple in the translation at the plea and not before; the four directions Moses is told to look come in an order Abraham's and
Jacob's do not share; and the Sifrei reads Joshua's charge as the rule he broke at Ai. Fifty-three typed facts fell across the passes and none on
the last. Twenty-one claims verified and seated, six rituals complete, the corpus rebaked to the predicted count with the hash unmoved, the world's
fold layer and the journal gate green. Next: the compile (1b) — and with it the readback's first design, on your word.

'''

BRIEF = '''- **DEUTERONOMY OPENS — THE FIRST THREE CHAPTERS READ AND FROZEN: THE SHELF IS TWO ISLANDS, THE TRANSLATION WRITES THE SIFREI INTO THE FIRST VERSE, THE PARSER READS EVERY NUMBER, AND THE SPEECH RETELLS THE TAPE IN ITS OWN WORDS** (2026-09-15, on your "start with deuteronomy"; World/step9/DEUTERONOMY_WALK.md "Sitting 1"). Six units on the first portion's three chapters, 259 sources in one ledger, 21 claims, six rituals, 216 units, the hash unmoved; the Sifrei silent from the oath to Og; the readback's first specimens measured (the retellings diffed against Numbers); the compile next on your word.
'''
BRIEF_ENTRY = '''### 2026-09-15 — DEUTERONOMY OPENS: THE SPEECH RETELLS THE TAPE, AND THE SHELF IS TWO ISLANDS

You said "start with deuteronomy" after the rereads, and the fifth book was opened the way the fourth was walked: the first portion's three chapters as six units named by chapter, Onkelos whole and the Sifrei on Deuteronomy found by position, every row read in both files, every fact an assert, every quotation cut from the bytes. What the reading found:

- **The shelf is two islands.** The Sifrei's first thirty piskaot sit on 1:1-1:28 (the rebuke's places, the officers, the spies sent) and 3:23-3:29 (the plea) — and nothing between: the oath, the defeat at Hormah, the years of going round, Sihon and Og have no piska. Seven rows elsewhere in the export cite the gap and were credited. The measurement pass had found one more, an "ibid" that seemed to point at 2:2 — the ink corrected it: the "ibid" follows a Song of Songs citation and means Song 2:2.
- **The translation writes the Sifrei into the first verse.** Onkelos renders the six place-names of 1:1 as six sins — "he rebuked them for that they sinned in the wilderness ... scorned the manna ... made the calf of gold" — thirty-three words for twenty-two, exactly the Sifrei's reading, on a question the Sifrei itself leaves open (R. Judah's ten trials against R. Yose's plain places named for events). Numbers' translation never did this.
- **The speech retells the tape in its own words.** The retellings were diffed against Numbers token by token: "your little ones a prey" is Numbers 14:31 verbatim; Og's defeat is Numbers 21:33-35 with "they" turned to "we"; Sihon's embassy is cut from seventeen words to nine; "good is the land" is Joshua and Caleb's report, not the spies' — and the Sifrei asks exactly who said it. One retelling disagrees with the tape: Moses says Edom and Moab let him pass as Numbers 20 says Edom refused — the shelf is silent, and the question is filed for the compile as open. This is the readback's first material.
- **The parser reads every number.** Eleven number verses, no gap — including the date of the speech, which the number reader reads as [40, 11, 1] where Aaron's death in Numbers 33 was read by the ordinal reader as [40, 5]: one year in two grammatical forms, six months apart on one clock. Only a fraction is unread — "half" Gilead, the "half-tribe" — a class named.
- **The judges' charge is the Mishnah's.** The Sifrei seats Avot 1:1's first saying on "hear between your brothers" and Sanhedrin 4:1's ten distinctions on "all the things you shall do"; it gives the officers' verse its arithmetic (round down at every grain; eighty thousand judges less a few); and it names Zelophehad's daughters — the tent's case — as the "hard matter" Moses could not hear.

Twenty-one claims verified and seated, six rituals complete, 216 units, standing 2184, the hash unmoved; the display layer gained 275 rows for the store's odd glosses ("pasture" for the wilderness, "leanness" for "only", "Red-Sea" for the place Suph). Next on your word: the compile of these chapters — and with it the readback's design, which is yours to decide.

'''

DEBT = '''
## DEUTERONOMY SITTING 1 — THE OPENING SPEECH'S READING (2026-09-15; DEUTERONOMY_WALK.md "Sitting 1"; logic/oral_triage/deu_01_03_devarim_2026-09-15.md; the six
## units deu_01_frame_officers, deu_01_spies_refuse, deu_02_bypass_nations, deu_02_sihon, deu_03_og_gilead, deu_03_moses_barred FROZEN) — OWED TO THE
## COMPILE (1b, on the Numbers walk's order with the register gate at the gates step): (a) THE READBACK'S DESIGN on the owner's word (THE_LOOP.md's STEP 6) —
## the speech as the tape read back: 1:19-46 against the tape's Numbers 13-14 acts (the spies sent, the rejection, the oath, Hormah), 2:1-3:22 against
## Numbers 20-21 and 32 (Edom, the Zered, Sihon, Og, the east's grants), the diffs measured at the reading (1:39 VERBATIM; 3:1-3 "they" → "we"; 2:27 nine
## tokens for seventeen; 2:32 eight for twenty; 3:14 twenty-three for eleven) the readback's first specimens — each a REFERENCE to the compiled act, never a
## second act; (b) THE REGISTER GATE'S FOUR SEATS PAID — 1:1 the EMPTY footer (the block from Numbers 36:13), 1:3 the receipt of the rules (the Sifrei 2:8's
## reading as the seat's disposition), 1:19 and 1:41 the receipt forms ("as the LORD commanded us"; "all that the LORD our God commanded us"); (c) THE
## OFFICERS' TABLE — 1:15's four grains (thousands, hundreds, fifties, tens) with the Sifrei 15:4's ROUNDING RULE (integer division at every grain) and 14:1's
## "eighty thousand less a few" (78,600 by the count: 600 + 6,000 + 12,000 + 60,000) as DATA against the census's 603,550 (the exam's setting); the seven
## qualities as a checklist (Jethro's four, 1:13's three, 1:15's two); the officers the Levites with the strap (2 Chronicles 19:11 — outside the Torah, DATA);
## Exodus 18's appointment by CALL (the yitro runner's cell); (d) THE JUDGES' CHARGE as the law's spec — hear between your brothers, judge righteously, no
## faces, small and great alike, no fear, the judgment is God's, the hard matter up — with Avot 1:1 and Sanhedrin 4:1 as the exam's rows (the Sifrei's own
## citations); the compromise dispute (Sifrei 17:4) as TWO verdict tables; R. Ishmael's two rulings on the gentile litigant (16:4) as a dispute row; the
## judge liable in his person (9:2, Proverbs 22:23) an effect; the appointer of judges (17:1) the prohibition's addressee; "a man" excludes the minor
## (16:6 — orphans not judged); (e) THE FRACTION CLASS taught to the parser — 3:12's "half the hill country", 3:13's "the half-tribe" (probes to FAIL; the
## Numbers half-tribe seats — 32:33's — measured before; the corpus diff read); (f) THE ONE CLOCK — 1:3's date [40, 11, 1] joined to Numbers 33:38's [40, 5]
## on the tape's clock (Aaron's death the fifth month, the speech the eleventh — six months; the Sifrei 2:3's thirty-three days to the Jordan; Deuteronomy
## 1:3 the tape's first act in the book); (g) THE RETELLINGS' DISAGREEMENT AT 2:29 — Edom and Moab "did for me" against Numbers 20:18-21's refusal and Judges
## 11:17's double refusal: NO teacher on the seat (no piska on 2:29) — a HYPOTHESIS row under the link review law, an OPEN question, no link of our own;
## (h) THE EAST'S GRANTS by REFERENCE to gad_reuben's cells (3:12-17: Aroer and half Gilead to Reuben and Gad, the rest and Bashan to half Manasseh; Jair's
## villages, Machir's Gilead; the borders — the Arnon's middle, the Jabbok, Chinnereth to the Salt Sea under Pisgah); the half-tribe with the article
## (3:13 the Torah's one seat) as the gentilic's form; (i) THE ARMED PASSAGE by REFERENCE to Numbers 32's condition (3:18-20 — the plural "armed" at 3:18
## and 32:30, 32; "until the LORD gives rest to your brothers" quoted whole at Joshua 1:15 — the run outside the Torah, THE READBACK's; Joshua 22:4 the
## release); (j) JOSHUA'S CHARGE (3:21-22, 3:28 — Numbers 27:19-23's commissioning by REFERENCE; "he shall cause them to inherit" the effect; Joshua 1:6 and
## Ai's thirty-six (the Sifrei 29:9) the run — outside the Torah); Joshua spelled plene at 3:21 (a spelling row, no verdict); (k) THE PLEA (3:23-29) — the
## ten names of prayer (Sifrei 26:7) as the effects registry's candidates (World/step9/effect_vocabulary.yaml — a prayer effect writing the LEDGER);
## "the LORD was wroth ... would not hear" a refusal effect; "enough for you" the singular's one seat; the directions of prayer (29:5) as DATA (Berakhot
## 4:5-6); the four directions' three orders (3:27, Genesis 13:14, 28:14) a DATA row; the fifty-cubit Jordan (29:6) the shelf's measure, flagged; "opposite
## Beth-peor" by REFERENCE to peor_pinchas's place; (l) THE DOCKET by the union rule — Mishnah Sanhedrin 1:1-6 and 4:1 with Sanhedrin 2a-b, 32a-b; Sanhedrin
## 3:1-8 with 23a-31b (6b-7a the compromise); Sanhedrin 1:6 with 16b-17a; Avot 1:1; Sheviit 9:2 (the three lands, Sifrei 6:1); Rosh Hashanah 1:1 with 2b-3a
## (the fortieth year's months); Sotah 7:5 and 34a-35a (the spies' report); Berakhot 4:5-6 with 30a; Makkot 2:4-8 and 9b-10a (the eastern cities of refuge
## whose land 3:12-17 gives — chapter 4's 41-43 forward); Kelim 17:9-10 and Eruvin 4:8 (the cubit of a man against a king's); Sanhedrin 90b-91a (the giants'
## measure); the link rows for 1:3, 1:15, 1:16-17, 1:39, 2:29, 2:33, 3:11, 3:20, 3:27-28; THE DISPLAY LAYER done at the reading (275 rows); the store's mixed
## families ("set" for GIVE at every seat by reference; "stream", "bore", "grate", "cramp", "plait", "to-face", "and-eye", "feed-on") a display sitting's;
## THE AL TIKREI (Sifrei 13:6 — "read not thus but thus": the consonants revocalized) for MOVE_CATALOG; THE CHECKPOINT PREFIX grepped before naming.
'''

RESEARCH = '''
## 2026-09-15 — DEUTERONOMY 1-3 READ (THE DEUTERONOMY WALK sitting 1 — THE OPENING SPEECH): THE ENGLISH APPARATUS IN THE ROWS; TWO ENGLISH ROWS THE HEBREW
## LACKS; A MIS-CITED VERSE; THE IBID THAT RESOLVES TO SONG OF SONGS; THE WRITTEN AND THE READ AT 2:33; THE RETELLINGS DISAGREE ON EDOM; ONKELOS WRITES THE
## SIFREI INTO 1:1; THE STORE'S ODD GLOSSES ON THE THREE CHAPTERS

THE EXPORT'S ENGLISH ROWS CARRY THE TRANSLATOR'S APPARATUS. The Sifrei on Deuteronomy's English file (Data/sefaria_export/Sifrei_Devarim/en.json)
glues its page references ("Pisqa' 11H:23-27; JN1:15-23.") and its footnote numerals to the words of the row ("Select108Heb: havu ..."): piska 1's
twenty rows carry 38 digit-before-capital markers. A defect class for every reading of this export — read past, count the markers, never a row.
The Hebrew file carries none. The two files' ROW GRAINS ARE EQUAL everywhere (357 piskaot, 2,357 rows each; no mismatch) — the Numbers export's
duplicated block has no twin here.

TWO ENGLISH ROWS CITE 1:4 WHERE THE HEBREW DOES NOT, AND ONE MIS-CITES. The four-form scan for rows outside piskaot 1-30 citing chapters 1-3 found
SEVEN Hebrew rows (37:9, 37:11, 52:1, 54:2, 82:5, 199:5, 314:2) and NINE English: 36:10 and 37:2 cite "(Dt.1:4)" where the Hebrew rows carry Song of
Songs 6:4 and Numbers 13:22 alone (the translator's added references), and 199:5's English cites "(Dt.2:25)" for the Hebrew's "(דברים ב כו)"
("Deuteronomy 2:26") — the quoted words are 2:26's "I sent messengers". The English "(Dt.n:m)" form has NO SPACE (3,292 such parens over the
export; one "Deut."): a regex with a space finds nothing.

THE IBID THAT IS NOT DEUTERONOMY'S. The measurement pass's ibid scan keyed "(שם ב ב)" ("ibid. 2:2") at 355:27 to the last Deuteronomy citation and
reported one ibid row on Deuteronomy 2:2. The ink walked the row's parens in order: "(שה״ש ב ג)" ("Song of Songs 2:3") precedes it — the ibid is
Song 2:2. The English row cites Deuteronomy 33:26 and Exodus 15:11 and nothing in chapters 1-3. Filed as the scan's false class: an ibid resolves
to the nearest book NAMED, not the nearest book SOUGHT.

THE WRITTEN AND THE READ AT 2:33. The snapshot store carries TWELVE tokens for Deuteronomy 2:33 where the Tanakh DB carries ELEVEN: the store keeps
both the written בנו ("his son") and the read בניו ("his sons"); the DB keeps the written form unpointed. The span's one such pair (measured over
all 112 verses). Onkelos reads the plural. Numbers 21:35's Og has "and his sons" written.

THE RETELLINGS DISAGREE ON EDOM. Deuteronomy 2:29 has Moses tell Sihon "as the sons of Esau who dwell in Seir and the Moabites who dwell in Ar did
for me" — the passage and the selling of food and water; Numbers 20:18-21 has Edom refuse ("you shall not pass"; "and Edom refused to let Israel
pass"); Judges 11:17 has Edom and Moab BOTH refuse. The Sifrei has no piska on 2:29 (its silence runs 1:29-3:22); the outside rows do not touch it.
Filed for the compile as an OPEN question with no teacher — a hypothesis row under the link review law, never a link of our own.

ONKELOS WRITES THE SIFREI INTO 1:1. The translation renders the six place-names of 1:1 as six sins in thirty-three tokens for the Hebrew's
twenty-two ("he rebuked them for that they sinned in the wilderness, and for that they provoked in the plain opposite the Sea of Reeds; in Paran
where they scorned the manna, and at Hazeroth where they provoked over the meat, and for that they made the calf of gold") — the Sifrei 1:9-17's
readings, on a question the Sifrei holds open at 1:18 (R. Judah's ten trials against R. Yose ben Dormaskit's plain places named for events); the
book's one seat of "rebuked". The Numbers walk met no such paraphrase in Onkelos Numbers. Filed as the translation's first written reading in the
book: the compile decides which reading the code carries (the place-names as data, the sins as the Sifrei's rows).

THE STORE'S ODD GLOSSES ON THE THREE CHAPTERS (the display layer, patch_overrides_deu.py — 149 by reference, 126 by gloss; the families censused over
the whole store first): "pasture" for the WILDERNESS (the-pasture 16, in-pasture 60, the-pasture-suffix 7 — every token the wilderness, by gloss);
"leanness" for ONLY (39, by gloss); "abrupt" for OPPOSITE (15); "Red-Sea" for SUPH THE PLACE (1:1's one token); "safe" for PEACE (12); "hating-you"
for YOUR ENEMIES (14); "something-bought" for CATTLE (17); "the-precept" for THE TORAH (27); "hind-part" for AFTER (96); "in-time" for AT THE TIME
(20); "to-set" for TO GIVE (37); "from-with" for FROM (61); "meaning-accession" for ALSO (12); "heed" for BECAUSE (5); "to-meander--about" for TO
SEARCH OUT (8); the direction suffixes ("hidden-suffix" NORTHWARD, "and-south-suffix" SOUTHWARD, "the-mountain-suffix" TO THE MOUNTAIN); the names
("the-Emims", "Rapha'", "the-Chorite", "Caphtorite", "Anakite", "Tsidonian", "Jehoshua"); the hapax forms ("and-be-naught" YOU DEEMED IT EASY,
"be--lofty" TOO HIGH, "and-cross-over" WAS WROTH, "the-bee", "treading", "ravine" THE SLOPES, "couch" BEDSTEAD, "building" CITY, "yield" UNDERTOOK);
and the mixed families by reference — "set" for GIVE at all twenty-six seats of the span, "stream" for THE BROOK and the river, "in-region-across"
for BEYOND, "bore" for BEGIN beside PROFANE, "grate" for CONTEND beside the grating, "cramp" for HARASS, "turn-aside-from-the-road" for BE AFRAID
beside SOJOURN, "and-pry-into" for SEARCH OUT beside DIG, "and-be--bitter" for REBEL beside MARAH, "and-seethe" for ACT PRESUMPTUOUSLY beside Jacob's
pottage, "plait" for RECKONED beside Heshbon, "to-face" for FORMERLY, "lip" for THE EDGE, "rope" for THE REGION, "mother" for CUBITS, "strength" for
GOD, "?" for KADESH / BETH / HAVVOTH / EZION, "and-eye" for AND YOU ANSWERED, "feed-on" for FIGHT, "seas-suffix" for WESTWARD. Ten families were
already rewritten by earlier sittings (and-crack-off, from-pasture, sunrise-suffix, the-powder, and-cord, cord, in-cord, the inherit-her form,
in-hate, Non). The mixed families' other seats a display sitting's.

THE SHELF'S SILENCE, MEASURED: no piska on 1:29-3:22 — the oath (1:34-40), the defeat (1:41-46), the bypass (2:1-25), Sihon (2:26-37), Og and the
east (3:1-22) read on Onkelos alone (the Sifrei's own case law on the judges and the plea the block's whole yield). Filed with the Numbers walk's
finding that Deuteronomy never says "refuge": the book's shelf is thin where the tape is thick.
'''

MIDDOT = '''- **THE SIFREI ON DEUTERONOMY'S OWN CASE LAW ON THE OPENING SPEECH (Deuteronomy 1:1-3:29; THE DEUTERONOMY WALK sitting 1, 2026-09-15;
  logic/oral_triage/deu_01_03_devarim_2026-09-15.md — piskaot 1-30 read whole in both files; the aggadic rows, E-codes by the claim's conclusion):
  · THE GENRE FROM THE REDUNDANCY (Sifrei Devarim 1:1-5 on 1:1): "these are the words Moses spoke" — did he prophesy only these? he wrote the whole
    Torah (31:9); so "these" are WORDS OF REBUKE ("Jeshurun grew fat and kicked", 32:15) — proved again on Amos, Jeremiah, David and Solomon, each
    book's "words" a rebuke: the particular against the whole resolved as a genre (I5), and the translation writes the genre into the verse (Onkelos
    1:1 "he rebuked them").
  · THE PLACES READ AS CHARGES, AND THE DISPUTE HELD OPEN (Sifrei 1:9-18 on 1:1): "beyond the Jordan" — for Shittim; "in the wilderness" — the manna;
    "in the Arabah" — Peor; "opposite Suph" — the sea; "between Paran and Tophel" — "words of folly against the manna" (the name read by its sound);
    "Hazeroth" — Miriam (an a-fortiori from the righteous to the rest, 1:14-16); "Di-zahab" — the gold of the calf (the tabernacle's gold to atone).
    Then R. Judah's TEN TRIALS ("two at the sea, two at the waters, two at the manna, two at the quail, the calf, the spies") and R. Yose ben
    Dormaskit's refusal — "Judah, why do you twist the Scriptures? we have gone over all the places and they are places, named for events" (the
    wells of Genesis 26 the proof) — the aggadic name-reading STATED AND DENIED in one piska, the dispute carried to Zechariah 9:1 and Genesis 41:43:
    a move with its own dissent on the shelf.
  · THE RECEIPT THAT RECEIVES THE RULES (Sifrei 2:8 on 1:3): "Moses spoke according to ALL that the LORD commanded him" — whence the light and the
    weighty, the equal decrees, the generals and the particulars, the bodies and the details? from "ALL": the hermeneutic rules themselves (I1, I2,
    I4 named by the row) received inside the receipt form — the register gate's seat at 1:3 meeting its reading.
  · THE CALENDAR FROM A DATE (Sifrei 2:3 on 1:3): "in the fortieth year, in the eleventh month" teaches that the year has twelve months — Esther's
    twelfth month, Solomon's twelve officers and the one "in the land" (the intercalated month), Moses' "today my days are full" and Joshua 4:19's
    tenth of the first month — thirty-three days counted back: a number in a date read as a rule of the calendar.
  · THE REBUKE NEAR DEATH AND ITS FOUR REASONS (Sifrei 2:4-7 on 1:3): "in the fortieth year" — he rebuked them only near death, as Jacob ("Reuben, my
    firstborn" — why not before: lest you cleave to Esau), Joshua, Samuel, David; FOUR reasons — not to rebuke twice, not to shame before a witness,
    no grudge, to part in peace ("rebuke brings peace": Abraham and Abimelech, Isaac and the Philistines) — the timing of an act derived from its
    date (I12's kin), the reasons a list.
  · KING AND PROVINCE (Sifrei 3:3-4 on 1:4): had Sihon not been hard but dwelt in Heshbon he was hard, for the province was hard; had the province
    not been hard but Sihon in it, it was hard, for the king was hard; how much more both — the a-fortiori (I1) on two joined difficulties, repeated
    for Og and Ashtaroth.
  · A VERB'S SENSE FIXED FROM ITS SEATS, DISPUTED (Sifrei 4:1 on 1:5; 27:1 on 3:24): "Moses undertook (הואיל) to explain" — R. Judah: a BEGINNING
    (Judges 19:6, 1 Chronicles 17:27); the sages: an OATH (Exodus 2:21 "Moses swore to dwell with the man", 1 Samuel 14:24) — E7 both ways; the
    translation takes R. Judah's ("Moses began"), the plea's row (27:1) takes the sages' ("you released my vow to Jethro").
  · THE HOMONYM READ (Sifrei 5:2-4 on 1:6-7): "enough (רב, 'much') for you at this mountain" — it was MUCH reward (the tabernacle, the table, the
    lampstand), MUCH benefit (the Torah, the seventy elders, the captains of 1:15), then HARM — idleness ("turn and journey"): one word read three
    ways, the last as the command's reason.
  · LEBANON FROM ITS SEATS (Sifrei 6:2-3 on 1:7; 28:3 on 3:25): "and Lebanon" — a KING (Ezekiel 17:3, 2 Kings 14:9) and THE TEMPLE (Jeremiah 22:6,
    Isaiah 10:34), named Lebanon because it whitens sins (Isaiah 1:18) — E7 on the word and the name read by its sound; ONKELOS WRITES THE TEMPLE at
    3:25 ("the house of the sanctuary", three seats in the book) and keeps Lebanon at 1:7.
  · THE JUDGE LIABLE IN HIS PERSON (Sifrei 9:2 on 1:9): "I cannot bear you alone" — not incapacity: a king of flesh and blood judges to death and it is
    nothing to him, takes two selas for one; "I, if I wrongly charge money, am claimed in my SOUL" (Proverbs 22:22-23 "he will despoil of soul those
    who despoil them") — the judge's error a debt on his life, the verse's ground.
  · THE COUNT AND THE ROUNDING (Sifrei 14:1 and 15:4 on 1:14-15): the judges "eighty thousand less a few" (the captains of thousands 600, of hundreds
    6,000, of fifties 12,000, of tens 60,000 — 78,600); "captains of thousands" — if there were 1,999 only one captain of a thousand is taken, 199
    one of a hundred, 99 one of fifty, 19 one of ten — INTEGER DIVISION at four grains stated as a rule: the compile's table for the officers, the
    remainder unled.
  · THE TWO MONEY-CHANGERS (Sifrei 13:3 on 1:13): "wise" against "understanding" — the wise like a rich money-changer (when no coins are brought
    he brings out his own and examines), the understanding like a poor one (when none are brought he sits and wonders): two competences
    distinguished by a parable (E26), the judges' second and third qualities.
  · READ NOT THUS BUT THUS — THE AL TIKREI (Sifrei 13:6 on 1:13): "and I will set them as your heads" (וַאֲשִׂימֵם) — read "THEIR GUILT on your heads"
    (וַאֲשָׁמָם): Israel's guilt hangs on the heads of their judges (Ezekiel 33:7-9's watchman) — the consonants revocalized to another word, an
    aggadic move on the pointing (filed for MOVE_CATALOG at the compile; the store's "and-put/set-them" the plain reading).
  · THE MISHNAH CITED BY THE SIFREI (Sifrei 16:1 on 1:16; 18:1 on 1:18): "hear between your brothers" — "be deliberate in judgment", AVOT 1:1's first
    saying with its two companions (raise many disciples, make a fence); "all the things you shall do" — the TEN DISTINCTIONS between money cases and
    capital cases (Sanhedrin 4:1): the testing shelf named as the verse's reading — the bridge stated from the reading side.
  · THE GENTILE LITIGANT, TWO RULINGS (Sifrei 16:4 on 1:16): R. Ishmael — by Israel's law or the nations', acquit the Israelite ("what do I care?
    'hear between your BROTHERS'"); Rabban Shimon ben Gamliel — no need: by the law they came under. A dispute on the addressee of "your brothers",
    flagged for the compile as two verdict tables.
  · THE HOLDER HOLDS (Sifrei 16:5 on 1:16): "judge righteously" — the righteous claimant claims and brings proofs: this one wrapped in his cloak, that
    one says "it is mine"; plowing with his cow, holding his field, sitting in his house — possession against the claim, the burden on the claimant.
  · "A MAN" EXCLUDES THE MINOR; "HIS BROTHER" INCLUDES EVERY PAIR (Sifrei 16:6-7 on 1:16): orphans are not judged; man and woman, nation and family,
    family and family — "in every case": I2's exclusion and inclusion on the same verse.
  · THE APPOINTER OF JUDGES (Sifrei 17:1 on 1:17): "you shall not recognize faces in judgment" — said to the one who SEATS judges: handsome, strong,
    my kinsman, he lent me money, he knows languages — he acquits the guilty from ignorance, and it is counted as favoring faces: the prohibition
    moved from the bench to the appointment.
  · SILENCE BEFORE HEARING, AND THE COMPROMISE DISPUTE (Sifrei 17:4 on 1:17): before you hear the two you may be silent, once heard you may not
    (Proverbs 17:14); if you cannot decide, you may be silent — "truth and the judgment of peace" (Zechariah 8:16) is compromise; Rabban Shimon ben
    Gamliel: raising the small and lowering the great is compromise; the sages: whoever compromises SINS (Psalm 10:3 "he who blesses a compromiser
    spurns the LORD") — the timing of the judge's silence as a rule, and the standing dispute on arbitration (Sanhedrin 6b the bridge).
  · THE HARD MATTER IS THE TENT'S (Sifrei 17:7 on 1:17): "the matter too hard for you" — the Holy One to Moses: you judge a hard case? I will bring one
    your disciple's disciple can hear and you cannot — THE DAUGHTERS OF ZELOPHEHAD ("Moses brought their case before the LORD", Numbers 27:5); so
    Samuel the seer (1 Samuel 9:19, 16:7): the link from 1:17 to Numbers 27 a REFERENCE the Sifrei itself teaches (LR1) — THE TENT's fourth sitting
    named from Deuteronomy.
  · THE SAME VERB AT TWO SEATS READ BY THEIR DIFFERENCE (Sifrei 20:1 on 1:22): "you came near to me, ALL OF YOU" — a mob (the young shoving the
    elders), against 5:20's "all the heads of your tribes and your elders came near to me" — the young honoring the elders: E7's narrative twin
    turned to contrast.
  · NAMED FOR ITS END (Sifrei 22:2 on 1:24): "the valley of Eshcol" before the cluster was cut (Numbers 13:23), "the mountain of God, Horeb" (Exodus
    3:1) before the giving — a place named in the text for what happens there later: the rule for the anachronism of names (E32's kin — the text's
    order is not the events'), the compile's naming rule.
  · WHO SAID "GOOD IS THE LAND" (Sifrei 23:3 on 1:25): "they brought us word and said: good is the land" — did they speak its good? they spoke its
    evil; who spoke its good? Joshua and Caleb — and even so "you would not go up" (1:26): the retelling's "they" narrowed to the two by the earlier
    seat's own words (Numbers 14:7 — the ink: "good is the land" two seats, theirs and this), the attribution a reading of the seats.
  · THE HYPERBOLE RULE (Sifrei 25:4 on 1:28; Rabban Shimon ben Gamliel): "cities great and fortified TO HEAVEN" — the Scriptures speak in
    exaggeration ("you cross the Jordan today", 9:1); but "as the stars of heaven", "as the dust of the earth" to Abraham are NOT exaggeration — a
    rule about which numbers the text means: the compile's docket on 9:1's "today" and the count-phrases.
  · THE TEN NAMES OF PRAYER (Sifrei 26:7 on 3:23): "and I besought" — prayer is called cry, shout, groan (Exodus 2:23-24), distress and calling (2
    Samuel 22:7), song and entreaty (Jeremiah 7:16), falling (9:25), prayer (9:26), entreating (Genesis 25:21), standing (Psalm 106:30), seeking
    (Exodus 32:11), supplication (3:23) — a census of a vocabulary from the seats (the English counts thirteen), the effects registry's candidates.
  · THE SUPERFLUOUS "SAYING" (Sifrei 26:9 on 3:23): "at that time, saying" — the word not needed: "tell me whether you will do it for me or not" —
    at Exodus 17:4, 6:12, Numbers 12:13, 27:15-16 and here, five seats where "saying" after a prayer asks for an answer: I5 on the register's word.
  · THE TWO NAMES (Sifrei 26:10 on 3:24): "O LORD" — wherever "the LORD", the measure of mercy (Exodus 34:6); wherever "God", the measure of
    judgment (Exodus 22:8, 27 — the judges) — a rule for the Names stated at the plea's seat (the Torah's four "O LORD God": Abraham's two, Moses'
    two), THE EFFECTS LAW's register for the divine actor.
  · THE BINYAN AV NAMED ON ONE WORD (Sifrei 27:4 on 3:24): "your greatness" — "this is a prototype (בנין אב, 'building a father') for every 'your
    greatness' in the Torah" — the middah named by the row itself on a word (I3); the ink: 3:24 the Torah's one seat, Joshua 3:7 the Bible's other — the
    prototype of itself.
  · "ENOUGH" THREE WAYS (Sifrei 29:2-4 on 3:26): "the LORD said to me: enough for you (רב לך)" — go to your MASTER (רב) to release your vow; you are an
    EXAMPLE to the judges (if Moses was shown no favor for "hear now, rebels", how much more the perverters of judgment; if Moses told "no more" did not
    cease to ask, how much more the rest — Hezekiah's sword on the neck); MUCH (רב) is kept for you in the world to come; "so-and-so has crossed the
    line" — the word read by its sound, by its sense and by its sound again, with two a-fortioris inside (I1).
  · THE DIRECTIONS OF PRAYER (Sifrei 29:5 on 3:26-27): "speak no more ... go up to the top of Pisgah" — R. Eliezer ben Jacob: one prayer is better than a
    hundred good deeds (for all his deeds Moses was never told "go up"; for the prayer he was); hence those outside the Land face the Land, in the Land
    face Jerusalem, in Jerusalem the Temple, in the Temple the Holy of Holies (Solomon's prayer, 1 Kings 8:48, 2 Chronicles 6) — north faces south, east
    faces west: all Israel toward one place. The verse's four directions (the ink: west, north, south, east — an order Genesis 13:14 and 28:14 do not
    share) become a compass of prayer: a rule of conduct from an aggadic seat (Berakhot 4:5-6 the bridge).
  · THE SHELF'S OWN MEASURE (Sifrei 29:6 on 3:27): "and see with your eyes" — the son kept from the bedroom; Moses: I am kept from the Land only the
    width of this Jordan, "a rope of FIFTY CUBITS" — a number the text does not carry: the compile takes it as the shelf's measure, not the ink's.
  · IF HE CROSSES THEY CROSS, IF HE GIVES THEY INHERIT — AI (Sifrei 29:8-9 on 3:28): "for he shall cross before this people" — if Joshua crosses before
    them they cross, if not, not; "he shall cause them to inherit" — if he gives, they inherit; so at Ai thirty-six fell and the LORD said "did I not say
    to Moses your master: ... you SENT them and did not go after them" (Joshua 7:5-10) — the run's failure traced to the spec's condition by the
    Sifrei itself: THE RUN AGAINST THE SPEC, taught (LR1), the readback's first teacher.
'''

RECOVERY = '''
## 31. ADDENDUM (2026-09-15, THE DEUTERONOMY WALK sitting 1 — THE OPENING SPEECH, Deuteronomy 1:1-3:29 READ AND FROZEN; the owner: "lets plan for deut next. where do we start" → "commit push" (29d477a) → "I don't need to compact. read what you need to get ready" → "start with deuteronomy"; the state doc's COMPACTION POINT #182)

THE BOOK OPENED. The map is World/step9/DEUTERONOMY_WALK.md (NEW — the head carries the walk's form and the shelf measured; "Sitting 1" the
reading's record and the owed list (a)-(l)). The rulings are the Numbers walk's (section 13-14 above; the memory numbers-in-order-ruling.md):
READ THEN COMPILE PER PORTION, CHAPTER NUMBERS, the parashah grain, the spine Onkelos + the Sifrei on Deuteronomy BY POSITION. The forms are the
Numbers walk's sitting-15 forms edited (World/step9/forms_deuteronomy_walk/ — deu_dump0 / parser0 / measure0-2, deu_ink with the driver and the
legs, the rows files, write_deu_ledger, patch_overrides_deu, write_deu_manifest, seat_deu (STEP_Dt_ ids), deu_chain.sh, copy_deu_forms,
write_deu_records). THE STATE: 216 frozen units (210 + 6), standing 2184 (2163 + 21), hash 8b8fff1fa28953af UNMOVED; CORPUS TRUTH, build_world,
the journal gate, the register gate GREEN; no engine file changed; the ledger logic/oral_triage/deu_01_03_devarim_2026-09-15.md (259 sources);
the six manifests (21 claims DV01A..DV03B); the display layer +275 rows. THE READING'S SHAPE HELD on the new book (the section-5 shape): dump →
parser → measure (three passes) → asserts (8, 22, 11, 12 fell on the typed passes → 0) → rows (112 + 147) → the writer (0 misses; the lint 1 → 0)
→ the patch → the manifests (21/21, the strict census GREEN) → the seat → six rituals (13 PASS each) → the fold predicted and matched. THE
SHELF: the Sifrei on Deuteronomy's 357 piskaot / 2,357 rows in BOTH files, equal grains; piskaot 1-25 on 1:1-1:28 and 26-30 on 3:23-3:29, NO piska
on 1:29-3:22; the English rows carry the translator's apparatus and the "(Dt.1:1)" form with no space; seven outside Hebrew rows (nine English:
36:10 and 37:2 added on 1:4, 199:5 mis-cited) credited; the one "ibid" resolving to Song of Songs (the measurement's hit corrected); six rows read
before by topic in Genesis ledgers (1:13, 6:1, 8:1, 11:1, 25:4, 27:3) named. THE FINDS (the ledger's twenty crowns; the map's THE INK): the two
islands; Onkelos writing the Sifrei into 1:1; the receipt of the rules (1:3); one clock, two readers; the officers' arithmetic; the judges' charge as
Avot 1:1 and Sanhedrin 4:1; the hard matter THE TENT's; the spies' words retold; the spy-verb against the tour-verb; "enough" plural and singular;
the retellings' disagreement on Edom (2:29 — the compile's open question, a hypothesis row); 2:33's written and read; Numbers 21:33-35 turned; Og's
bed; Joshua plene once; the plea's names; Lebanon the Temple at 3:25; the four directions in three orders; the run against the spec at Ai; the
valley Peor's. THE LESSONS (nine, the map's ⚠ list): the ibid to the nearest book named; the English apparatus; the prior-read census's strict
row form; a count from a looser regex is a different number; the lemma's letter; MIDDOT's own label codes (E4 → E7); a written-once guard fires on
the rerun — scope it to the first pass and swap a rewritten ledger in whole by a temp path; grep the override file's keys before a by-gloss list;
the shape held. NEXT on the ruling: SITTING 1b — THE COMPILE OF DEUTERONOMY 1-3 (the owed list (a)-(l) in DEUTERONOMY_WALK.md; THE READBACK's design
on the owner's word FIRST — the speech as the tape read back, the diffs against Numbers 13-14, 20-21, 32 its specimens; the register gate's four
seats paid; the officers' table; the judges' spec; the fraction's probes; the one clock; the retellings by reference; the docket by the union rule)
— the design in the map before any code; then chapter 4's reading. UNCOMMITTED at this writing: everything of this sitting (the state doc's #182
names every path) and #180's addenda 3-4 and #181 — the owner's next "commit push" carries them.
'''

MEMFILE = '''---
name: deuteronomy-walk
description: "THE DEUTERONOMY WALK opened 2026-09-15 on the owner's 'start with deuteronomy' — the fifth book in order from 1:1 at the parashah grain, chapter numbers not portion names, READ THEN COMPILE PER PORTION; map World/step9/DEUTERONOMY_WALK.md; SITTING 1 DONE 2026-09-15 — 1:1-3:29 read and frozen as six units (216 units, standing 2184, hash unmoved); NEXT: the compile of 1-3 (1b) with THE READBACK's design on his word, then chapter 4"
metadata:
  type: project
---

THE RULING APPLIED (the owner, 2026-09-15): "lets plan for deut next. where do we start" (the plan: commit, the rereads, the measurement, the
reading of chapters 1-3, the compile — the readback's design his decision), "commit push" (29d477a), "I don't need to compact. read what you need
to get ready", "start with deuteronomy". The Numbers walk's rulings govern ([[numbers-in-order-ruling]]): READ THEN COMPILE PER PORTION, never
read ahead; CHAPTER NUMBERS, never portion names; the parashah grain; the spine Onkelos whole + the Sifrei on Deuteronomy BY POSITION
([[spine-default]]).

**Why:** Numbers closed 2026-09-13 (1:1-36:13 read, frozen, compiled, on the tape); the next book in order is Deuteronomy, whose owed seats the
register gate had filed at Numbers ("the book not read": 1:1, 1:3, 1:19, 1:41; and chapters 4, 12, 17, 19, 21, 25).

**How to apply:** the map is World/step9/DEUTERONOMY_WALK.md (one section per sitting; the owed list per sitting; the forms in
World/step9/forms_deuteronomy_walk/ — the Numbers walk's sitting-15 forms edited, the step ids STEP_Dt_<c>_<v>). SITTING 1 DONE 2026-09-15 — THE
OPENING SPEECH 1:1-3:29 read and frozen as SIX units (deu_01_frame_officers, deu_01_spies_refuse, deu_02_bypass_nations, deu_02_sihon,
deu_03_og_gilead, deu_03_moses_barred): the Sifrei's piskaot 1-30 by position (147 rows, both files' grains equal; NO piska on 1:29-3:22 — the
shelf two islands), Onkelos whole (112) = 259 sources in ONE ledger logic/oral_triage/deu_01_03_devarim_2026-09-15.md; 21 claims (DV01A..DV03B)
verified, labeled, seated; six rituals 13 PASS each → 216 units, standing 2184, hash 8b8fff1fa28953af unmoved (predicted); the display layer
+275 rows; the parser eleven number verses read, NO GAP (the fraction class named). THE FINDS: Onkelos writes the Sifrei's reading of 1:1's places
as sins into the verse; the receipt "according to all" (1:3) received as the hermeneutic rules (Sifrei 2:8); one clock, two readers (1:3 against
Numbers 33:38); the officers' arithmetic (the rounding rule, 78,600); the judges' charge Avot 1:1's and Sanhedrin 4:1's; the hard matter
Zelophehad's daughters (THE TENT); the spies' words retold (Joshua and Caleb's "good is the land"; Numbers 14:31 verbatim; Eden's "good and evil");
the retellings disagree on Edom at 2:29 (no teacher — a HYPOTHESIS row, the compile's open question); 2:33 written "his son" read "his sons"; Og's
bed by the cubit of a man; Joshua plene once in the Torah; Lebanon the Temple written at 3:25; the four directions in three orders; the run against
the spec at Ai (Sifrei 29:9). ⚠ LESSONS: the ibid resolves to the nearest book named; the English rows carry the apparatus and the "(Dt.1:1)" form
with no space; the prior-read census takes the row form strictly; a count typed from a looser regex is a different number; MIDDOT's own label
codes (E7 the narrative verbal analogy, not E4); a written-once guard fires on the same sitting's rerun — scope it to the first pass; grep the
override keys before a by-gloss list. NEXT on the ruling: SITTING 1b — THE COMPILE OF DEUTERONOMY 1-3 (DEUTERONOMY_WALK.md's owed list (a)-(l):
THE READBACK's design on the owner's word FIRST — the speech as the tape read back, the diffs against Numbers 13-14, 20-21, 32 its specimens; the
register gate's four seats paid; the officers' table; the judges' spec; the fraction's probes; the one clock; the retellings by reference; the docket
by the union rule), the design in the map before any code; then chapter 4's reading, and on in order. See also [[the-loop-ruling]] (STEP 6 THE
READBACK, owed) and [[step9-exam-era]] (the standing lessons).
'''

# ---- THE WRITES (every insert on a unique anchor asserted present once) ----
LINT = f'{ROOT}/logic/solo_tools/gloss_lint.py'
def lint(path):
    out = subprocess.run(['python3', LINT, path], capture_output=True, text=True).stdout
    m = re.search(r'gloss_lint: (\d+) flag', out); return int(m.group(1)) if m else -1
TOUCH = [f'{ROOT}/logic/findings/STAMP_LEDGER.md', f'{ROOT}/logic/pre_logic_methods_2026-07-28/PROMPT_continue_solo_era_2026-08-06.md', f'{ROOT}/World/RESUME.md', f'{ROOT}/THE_STEPS.md', f'{ROOT}/THE_BRIEFING.md', f'{ROOT}/World/step9/COMPILE_DEBT.md', f'{ROOT}/RESEARCH_LOG.md', f'{ROOT}/logic/MIDDOT.md', f'{ROOT}/logic/pre_logic_methods_2026-07-28/RECOVERY_new_thread_2026-09-12.md', f'{MEM}/MEMORY.md']
BEFORE = {p: lint(p) for p in TOUCH}
print('lint before:', {os.path.basename(p): n for p, n in BEFORE.items()})

append(f'{ROOT}/logic/findings/STAMP_LEDGER.md', STAMP)
WALKP = f'{ROOT}/World/step9/DEUTERONOMY_WALK.md'
assert not os.path.exists(WALKP), WALKP
open(WALKP, 'w', encoding='utf-8').write(WALK_HEAD + WALK); print('wrote', WALKP, len((WALK_HEAD + WALK).encode()), 'bytes')
append(f'{ROOT}/logic/pre_logic_methods_2026-07-28/PROMPT_continue_solo_era_2026-08-06.md', STATE)
insert_after(f'{ROOT}/World/RESUME.md', 'NUMBERS 1:1-36:13 READ, FROZEN, COMPILED AND ON THE TAPE. NEXT on the owner\'s word: the next book.\n', RESUME)
# THE_STEPS: the paragraph goes after the SITTING 15b paragraph (its end found by the blank line that follows it)
sp = f'{ROOT}/THE_STEPS.md'; s = open(sp, encoding='utf-8').read()
i = s.index('SITTING 15b — THE COMPILE OF THE REFUGE CITIES'); j = s.index('\n\n', i) + 2
open(sp, 'w', encoding='utf-8').write(s[:j] + STEPS + s[j:]); print('inserted THE_STEPS paragraph after the 15b paragraph at', j)
insert_before(f'{ROOT}/THE_BRIEFING.md', '- **THE BUTTONS DRIVE THE ENGINE — THE ENGINE WAITS;', BRIEF)
insert_before(f'{ROOT}/THE_BRIEFING.md', '### 2026-09-15 — THE BUTTONS DRIVE THE ENGINE\n', BRIEF_ENTRY)
append(f'{ROOT}/World/step9/COMPILE_DEBT.md', DEBT)
append(f'{ROOT}/RESEARCH_LOG.md', RESEARCH)
insert_before(f'{ROOT}/logic/MIDDOT.md', '## Exodus block campaign — owner\'s word "Do 3")', MIDDOT + '\n')
append(f'{ROOT}/logic/pre_logic_methods_2026-07-28/RECOVERY_new_thread_2026-09-12.md', RECOVERY)
# the memory: a new file + the index (under 17,000 bytes — two NEXT pointers shortened to pay for the new line)
mp = f'{MEM}/deuteronomy-walk.md'; assert not os.path.exists(mp); open(mp, 'w', encoding='utf-8').write(MEMFILE); print('wrote', mp)
ip = f'{MEM}/MEMORY.md'; m = open(ip, encoding='utf-8').read()
a1 = "NEXT on the owner's word: DEUTERONOMY, chapters 1-3 first (the owed seats filed in chapters 4, 12, 17, 19, 21, 25)."
b1 = "NEXT: [[deuteronomy-walk]] (the owed seats filed in chapters 1, 4, 12, 17, 19, 21, 25)."
a2 = "#180 the current tail (2026-09-15, everything committed at 29d477a and pushed; NEXT: DEUTERONOMY chapters 1-3, the reading, on his word)"
b2 = "#182 the current tail (2026-09-15; the last commit 29d477a; NEXT: the compile of Deuteronomy 1-3 on his word)"
a3 = "- [User identity](user_identity.md)"
b3 = "- [⚠ THE DEUTERONOMY WALK](deuteronomy-walk.md) — opened 2026-09-15 on \"start with deuteronomy\"; map World/step9/DEUTERONOMY_WALK.md; SITTING 1 DONE 2026-09-15 (1:1-3:29 read and frozen as six units; 216 units, standing 2184, hash unmoved; the Sifrei two islands, no piska on 1:29-3:22; the retellings diffed against Numbers — the readback's specimens; 2:29's Edom question OPEN); NEXT: the compile (1b) with THE READBACK's design on his word, then chapter 4\n- [User identity](user_identity.md)"
assert m.count(a1) == 1 and m.count(a2) == 1 and m.count(a3) == 1
m = m.replace(a1, b1).replace(a2, b2).replace(a3, b3)
assert len(m.encode()) < 17000, len(m.encode())
open(ip, 'w', encoding='utf-8').write(m); print('MEMORY.md', len(m.encode()), 'bytes')
AFTER = {p: lint(p) for p in TOUCH}
print('lint after: ', {os.path.basename(p): n for p, n in AFTER.items()})
assert all(AFTER[p] <= BEFORE[p] for p in TOUCH), [(os.path.basename(p), BEFORE[p], AFTER[p]) for p in TOUCH if AFTER[p] > BEFORE[p]]
for p in (WALKP, mp): assert lint(p) == 0, p
print('records written; the lints unchanged; the map and the memory file lint 0')
