#!/usr/bin/env python3
# THE DEUTERONOMY WALK sitting 4 — CHAPTER 6, RUN 1 of four CLOSED (2026-09-17): the design appended to the map, the state doc's checkpoint, the memory note and the
# index line. Every text built first; the caps asserted before any file is opened. write_ch5b_design.py's form.
import os, subprocess
ROOT = subprocess.check_output(['git', 'rev-parse', '--show-toplevel'], text=True).strip()
MEM = os.path.expanduser('~/.claude/projects/-Users-Shared-TorahSim/memory')
def read(p): return open(p, encoding='utf-8').read()
DESIGN = '''

## Sitting 4 — CHAPTER 6, Deuteronomy 6:1-25 (2026-09-17; the owner: "ok lets start the next chapter"): the reading and the unit — THE DESIGN, written at the close of RUN 1 of four

THE FOUR RUNS (the rule of 2026-09-16, its first application): RUN 1 the rereads (the recovery page, the map's "Sitting 3b — AS BUILT" and "THE FOUR-RUN RULE", the
memory; the map's "Sitting 3" as the reading's form), the measurements (ch6_dump0.py, ch6_measure1.py), the ink (ch6_ink.py — 113 asserts, 0 fails on the second
pass) and this design — CLOSED HERE, a clean compaction point; RUN 2 the rereads THE_STEPS Step 2 + Step 5's head + the compiler block, then the rows (the spine's
67 rows piska by piska from ch6_sifrei_spine.txt, the eight outside rows, the twenty-five Onkelos rows from ch6_onkelos.txt) and the ledger (write_ch6_ledger.py from
write_ch5_ledger.py by sed; lint 0; coverage computed); RUN 3 the display layer's patch (33 rewrites by gloss, 24 by reference), the manifest (six claims), the seat,
the chain (the ritual), the fold predicted and matched, build_world, the journal gate, the register gate --strict, the home-path gate; RUN 4 the records from the
sheet in one call, the forms copied, this section's AS BUILT, the compaction point.

THE DRAFT: deu_06_shema 6:1-25 — 25 of 25 verses, missing 0 (computed from the DB's verse table), depends_on deu_05_decalogue, 32 scenarios, 54 comment lines (two
per step and four of the log); the next draft deu_07_nations_cherem opens at 7:1; the step ids STEP_Dt_6_<v>. The chapter the unit, per the ruling; ONE pass, one
ledger: logic/oral_triage/deu_06_vaetchanan_2026-09-17.md; the claims' prefix DV06 (absent everywhere, asserted).

THE TWO DIVISIONS AGREE: the export's chapter 6 twenty-five rows, the DB's twenty-five verses; sitting 3's alignment instrument rerun gives the identity at cost 12;
chapter 5 the book's ONE split (every other chapter's export length equals the DB's — asserted on all thirty-four).

THE SHELF, BY POSITION — THE SPINE LANDS ON THE CHAPTER: piskaot 31-36 head on 6:4, 6:5, 6:6, 6:7, 6:8, 6:9, ONE PER VERSE OF THE SHEMA (the first on-chapter piskaot
since piska 30 on 3:29; piska 37 heads on 11:10 — chapters 7 to 10 have none): 67 rows (10, 21, 4, 10, 12, 10; the two files equal), 100 KB in both languages;
6:1-3 and 6:10-25 carry no piska — the Sifrei reads the Shema alone. THREE spine rows read at Genesis sittings are CREDITED (32:2 at gen_27 as a duplicate row; 36:10
at gen_29 and 33:4 at gen_30 material). THE OUTSIDE ROWS by the union of both files: nine rows beyond the spine cite chapter 6 — EIGHT READ (38:10 on 11:10 citing
6:11 three times; 41:14 and 41:20 on 11:13 citing 6:4 and 6:5; 104:8 on 14:21 — the English translator's own "(Dt.6:1ff.)" for "once at Horeb", marked an
interpolation; 201:3 on 20:15 citing 6:11; 258:1 on 23:15 — the Shema named as a text, its recitation barred beside the launderers' vat, Mishnah Berakhot 3:5;
306:37 on 32:1; 355:27 on 33:26 — Israel says "Hear, O Israel" and the Holy Spirit answers with 1 Chronicles 17:21) and ONE EXCLUDED (62:4's "(Dt.6:27)" is the
English's slip for Numbers 6:27 — the Hebrew names Numbers; no verse 6:27 exists). TWO CITATION FORMS NEW TO THE SCAN: the Hebrew's "ibid." (the word "there" after a
Deuteronomy citation in the same row — 355:27; the book-name regex misses it, the English catches it) and the translator's parenthesis (104:8). None of the eight
read before. THE PRIOR READS: 219 strict rows anywhere; no ledger holds an Onkelos row of chapter 6 or of Exodus 13 (the frontlets' and the son's kin — the Exodus
blocks were read exam-first, never spine-by-position); five ledgers NAME a verse of chapter 6.

THE INK, COMPUTED (ch6_dump0.py, ch6_measure1.py; the asserts typed from the print — SIX fell on the first pass, all forms and none facts: the Genesis ledgers' TABLE
row form; the store's 6:4 (below); the register yaml holds no 4:45 key (that seat green by computation, undeclared); a seat list unsorted; "to-goad" already
rewritten at sitting 2; each retyped from the print, none after):
- THE PARSER MEASURED FIRST: ONE number verse in 25 — 6:4 "the LORD is one" [1]: THE CREED'S WORD READ AS THE NUMERAL (Zechariah 14:9's "the LORD one and His
  name one" reads [1, 1]; "one witness" at 17:6 and 19:15 the same word); the seven-stem homographs REFUSED — "swore" (6:10, 18, 23) and "you shall swear" (6:13)
  not numbers at all (the lemma 7650), "and you shall be satisfied" (6:11, the lemma 7646) STARRED; no ordinal; NO GAP. The tokens 318, the letters 1,295; the six
  piskaot's verses 6:4-9 forty-eight tokens.
- THE STORE = THE DB in count at every verse; FOUR TOKENS DIFFER OVER THE WHOLE TORAH, all LARGE LETTERS the store drops (RESEARCH_LOG 2026-09-09's defect report,
  which named this seat in advance): 6:4's "hear" and "one" (the ayin and the dalet), Leviticus 11:42's "belly" (the vav), Numbers 27:5's "their case" (the nun) —
  the census computed, the second and third instances met; the ink asserts the exact miss. The two unglossed tokens both "I" (6:2, 6:6).
- THE KIN DIFFED (the DB's tokens): 6:1 against 5:31 — the triad "the commandment, the statutes and the judgments" at 5:31, 6:1, 7:11 in that order, the three
  seats: 6:1 OPENS THE TEACHING 5:31 COMMANDED ("which you shall teach them" → "commanded to teach you"); 6:8 against Exodus 13:9, 13:16 and 11:18 — the sign on the
  hand FOUR SEATS in four spellings of "your hand", the FRONTLETS THREE SEATS in THREE SPELLINGS (Exodus 13:16 plene with the vav, 6:8 DEFECTIVE, 11:18 plene — the
  Talmud's four compartments from the spellings, Sanhedrin 4b and Menachot 34b, the docket's); 6:9 against 11:20 (one letter — "doorposts" defective here); 6:13
  against 10:20 (10:20 adds "and to Him you shall cleave"); 6:20 against Exodus 13:14 — "WHEN YOUR SON ASKS YOU TOMORROW, SAYING" VERBATIM, the Bible's two seats;
  the four askings (Exodus 12:26, 13:8, 13:14, 6:20 — the four sons of the Mekhilta and the Haggadah; Mishnah Pesachim 10:4 "according to the son's understanding" —
  the docket's); 6:21-23 against Exodus 13:3, 13:8, 13:14 and 4:34-38 — THE ANSWER A RETELLING OF THE EXODUS IN THE FIRST PERSON PLURAL ("we were slaves to
  Pharaoh" the one seat; "He brought us out … gave signs and wonders … before our eyes … to bring us in") — THE READBACK'S NEXT FORM at the compile: a story told to
  a son graded against the tape's own lines; 6:16 against Exodus 17:2, 7 and 33:8 (Massah's four seats; "you shall not test" plural — the testers addressed); 6:15
  against 4:24 and 5:9 (the jealous God, five seats); 6:12 against 8:11, 5:6 and Exodus 13:3.
- THE PHRASE CENSUSES (the crowns): "Hear, O Israel" four seats, all this book's; "THE LORD IS ONE" 6:4 and Zechariah 14:9 — the two seats; "with all your heart
  and with all your soul" seven, all Deuteronomy's (4:29 the first); "AND WITH ALL YOUR MIGHT" THE BIBLE'S ONE SEAT of the noun with a suffix; "teach them
  diligently" the ONE seat of the word (the root's nine — whetting arrows, swords, the tongue); "when you sit … when you rise" 6:7 and 11:19; "and you shall eat and
  be satisfied" 6:11, 8:10, 11:15; "you shall fear, serve, swear by His name" 6:13 = 10:20; "swore to your fathers" 6:10 the book's first of four, "to our
  fathers" 6:23 the one; "a land flowing with milk and honey" 6:3 THE BOOK'S FIRST (eleven in the Torah); "the testimonies, the statutes and the judgments" 6:20 =
  4:45's footer — THE SON ASKS ABOUT THE REGISTER GATE'S OWN HEADER; "and it shall be righteousness for us" one — "righteousness" eight Torah seats, Abraham's
  Genesis 15:6 the first; "AS HE COMMANDED US" (6:25, Ezra 4:3) A RECEIPT WITHOUT THE NAME — THE REGISTER GATE'S CENSUS DOES NOT SEE IT (the gate reads "as the LORD
  commanded"; chapter 6 has NO SEAT, computed: no index line, no yaml key).
- THE FRAMES AND THE REGISTER: NO divine frame — the whole chapter Moses' voice; ONE "saying" — the son's (6:20); the narrative verbs only inside the answer
  (6:21, 22, 24); TWO IMPERATIVES "hear" (6:4) and "take heed" (6:12); ONE INFINITIVE ABSOLUTE "keep" (6:17 — with 5:12 and 16:1 the book's three); the law's form
  the consecutive perfect in eleven verses; TWO PROHIBITIONS, BOTH PLURAL (6:14 other gods, 6:16 the test) in a SINGULAR chapter (singular-only fifteen verses;
  plural-only 1, 14, 16, 17; both 3, 20; the answer's 22-25 in the FIRST PERSON PLURAL — "we"); "the LORD your God" six singular, three plural, "our God" four;
  the Name twenty-two; Moses never named; "for/when" at 10, 15, 20, 25 and "lest" at 12, 15 — no "if", no "or".
- ONKELOS (the renderings' seats over the book): 6:4 "one" one seat of the pair; 6:5 "AND WITH ALL YOUR MIGHT" MADE "WITH ALL YOUR PROPERTY" (the one seat —
  Mishnah Berakhot 9:5's "with all your money" the docket's); 6:8 "FRONTLETS" MADE "TEFILLIN" — the object named (the English's bracket); 6:9 "write them on
  MEZUZOT AND FIX THEM in the doorposts" — the fixing SUPPLIED (6:9, 11:20); 6:12 "lest you forget (THE FEAR OF) the LORD" — THE EXPORT'S PARENTHESISED VARIANT, the
  chapter's one of the book's ten; 6:13 "serve BEFORE Him" (6:13, 10:20, 13:5); 6:14 "the IDOLS of the peoples" (eighteen); 6:15 "in your midst" MADE "HIS SHEKHINAH
  IS AMONG YOU" (6:15, 7:21); 6:16 "MASSAH" MADE "THE TRIAL" — the name translated (one seat); 6:18 "what is fit and what is proper" (one); 6:22 "all the MEN OF his
  house" (supplied); 6:25 "RIGHTEOUSNESS" MADE "MERIT" (6:25 and 24:13 — the two seats of the word in the book); the reverential "before" at 6:2, 13, 16, 18, 25
  (101 seats in the book); the English's eleven bracketed supplements.
- THE DISPLAY LAYER (run 3): 33 rewrites BY GLOSS ("to-fillet-for-the-forehead" → "for-frontlets", "very-you/your" → "your-might", "and-point-them/their" →
  "and-you-shall-teach-them-diligently", "deferred" → "tomorrow", "and-rightness" → "and-righteousness" …) and 24 BY REFERENCE (the two "I"; "God" for "strength"
  and "anger" for "nose" at 6:15; "hewn", "vineyards", "cisterns"; "slaves" and "bondage" …); eleven of the chapter's families already rewritten at sittings 1-3.

THE CLAIMS PLANNED (write_ch6_manifest.py, run 3): SIX — DV06-01 6:1-3 the header (the charge's teaching opens; the land; the days prolonged); DV06-02 6:4-5 the
creed and the love; DV06-03 6:6-9 the words' four duties (on the heart, taught, bound, written); DV06-04 6:10-15 the gift and the warning (the cities not built;
lest you forget; fear, serve, swear; no other gods; the jealous God); DV06-05 6:16-19 Massah, keep, the right and the good; DV06-06 6:20-25 the son's question and
the answer — each check the block's longest store-piece whole (6:4's "hear" and "one" NOT checks — the store's dropped letters). THE FOLD PREDICTED: units 220,
standing 2197 + 6 = 2203, hash unmoved (the tripwire's literals set before the bake). THE SEATS: six WITNESS_READ operators at 6:1, 4, 6, 10, 16, 20, step E. THE
REGISTER GATE: no seat in the chapter — GREEN unchanged (DECLARED 100). THE LEDGER PREDICTED: Onkelos 25 rows; the Sifrei 67 spine rows (3 CREDITED, 64 FRESH) and
8 outside rows FRESH; coverage COMPUTED at the writing.

OWED TO THE COMPILE (sitting 4b; the box in COMPILE_DEBT.md at run 4): the Shema's four duties (6:6-9) as law cells — the words on the heart (the recitation:
Mishnah Berakhot 1-3), the teaching, the tefillin (the spellings' four compartments; Menachot 34b-37b), the mezuzah (Menachot 31b-34a); 6:13's fear-serve-swear (the
oath by the Name — Shevuot; Temurah 4a); 6:14's other gods — a CALL into 3b's second-word cell; 6:16's test; 6:18's the right and the good (Bava Metzia 108a the
abutter — the docket); 6:20-25 THE SON'S ANSWER AS THE READBACK'S THIRD FORM — a retelling told to a son, graded against the tape's exodus lines; 6:1's edge (the
charge's teaching opens — a REFERENCE to the debit closed at 3b); 6:10-11's list a DATA row; "swore to your fathers" three times — the oath's tape entries (Genesis
22:16, 26:3, 50:24; Exodus 13:5, 33:1); THE RECEIPT WITHOUT THE NAME (6:25) — the register gate's finder taught the form, or the seat declared by hand; the docket by
the union rule (Berakhot 2a-16a whole; Menachot 28b-44a; Pesachim 116a-b the four sons; Mishnah Berakhot 1:1-3:5 and 9:5; Sotah 7:1; Sanhedrin 74a the martyr's
"with all your soul"; Kiddushin 30a-b "teach them diligently" — sharpened answers).

⚠ LESSONS (run 1): THE HEBREW'S "IBID." FORM — a Sifrei row cites "there" after a Deuteronomy citation in the same row; the book-name regex misses it, the English's
catches it: the union of both files remains the finder. THE ENGLISH EXPORT CAN MIS-CITE A BOOK — 62:4's "(Dt.6:27)" for Numbers 6:27: a cited verse beyond the
chapter's length is checked against the DB before it is counted. A TRANSLATOR'S PARENTHESIS IS NOT THE SIFREI'S CITATION (104:8). THE STORE'S LARGE LETTERS — the
defect report of 2026-09-09 named 6:4 in advance; the whole-Torah census is four tokens; the ink asserts the exact miss and no claim's check uses those words. THE
FIRST TYPED PASS FELL SIX WAYS ON FORMS, NOT FACTS — the asserts typed from the print still need the FORM of the prior record read (a ledger's table row, a yaml's
keys, a sorted list). A RUN'S EDGE IS A RECORD: the design written before the rows, the checkpoint naming run 2's first step.

THE ORDER (RUN 2, the first step): reread THE_STEPS Step 2 + Step 5's head + the compiler block; the spine's rows piska by piska (ch6_sifrei_spine.txt, 100 KB —
31; 32 the long one; 33-36), the eight outside rows (ch6_sifrei_outside.txt), the Onkelos rows (ch6_onkelos.txt, read at run 1) → ch6_rows_onkelos_a/b.py,
ch6_rows_sifrei_31.py, ch6_rows_sifrei_32.py, ch6_rows_sifrei_33_36.py, ch6_rows_outside.py (the cuts by consonants; SP_ for the Sifrei) → write_ch6_ledger.py →
lint 0, coverage computed → the state doc's checkpoint (RUN 2's close, a clean point).
'''
STATE = '''

#189 ADDENDUM 2 (2026-09-17 — THE DEUTERONOMY WALK SITTING 4, CHAPTER 6: RUN 1 OF FOUR CLOSED — A CLEAN COMPACTION POINT; the owner: "ok lets start the next chapter"): THE STATE — the rereads done (the recovery page, the map's 3b sections and the four-run rule, the memory index; the map's "Sitting 3" as the reading's form); THE MEASUREMENTS (ch6_dump0.py → ch6_dump0.out 81 lines; ch6_measure1.py → ch6_measure1.out 377 lines): the two divisions agree (25 = 25, the identity at cost 12); THE SPINE LANDS ON THE CHAPTER — Sifrei piskaot 31-36 on 6:4-9, 67 rows, three CREDITED from Genesis sittings; eight outside rows FRESH (38:10, 41:14, 41:20, 104:8 the translator's note, 201:3, 258:1, 306:37, 355:27 the Hebrew's "ibid."), 62:4 EXCLUDED (the English's "(Dt.6:27)" for Numbers 6:27); the parser ONE number verse, 6:4 "one" [1], the seven-stem homographs refused, NO GAP; the store's 6:4 drops the two large letters (the 2026-09-09 defect, the Torah census four tokens); no register seat in the chapter; 6:25's receipt without the Name unseen by the gate; THE INK ch6_ink.py — 113 asserts, six fell on the first pass (forms, not facts), 0 on the second; THE DESIGN in the map ("Sitting 4 — … THE DESIGN"): the six claims planned, the fold predicted (220 units, standing 2203, hash unmoved), the display layer's 33 + 24, the owed items, the lessons. THE SCRATCHPAD: ch6_dump0.py/.out, ch6_measure1.py/.out, ch6_ink.py, ch6_ink_run2.out, ch6_onkelos.txt (27 KB, read), ch6_sifrei_spine.txt (100 KB, unread), ch6_sifrei_outside.txt (92 KB — the eight rows unread), ch6_store_glosses.txt, write_ch6_design.py. THE GATES: none run this run (no file of the engine touched; the ledger not yet written). THE RECORDS: the map, this addendum, the memory. NOT COMMITTED (since 7c8554e). NEXT — RUN 2, THE FIRST STEP: reread THE_STEPS Step 2 + Step 5's head + the compiler block (the post-compaction rule's reread before a ledger); then the spine's rows piska by piska at a short cut, the outside rows, the row scripts (ch6_rows_*.py — sitting 3's ch5_rows_*.py the form, the cuts by consonants), write_ch6_ledger.py from write_ch5_ledger.py by sed, lint 0, coverage computed; then the checkpoint (#189 addendum 3, RUN 2's close). IF THIS COMPACTS HERE: reread the recovery page, the map's "Sitting 4 — … THE DESIGN" (its THE ORDER paragraph names the step), MEMORY.md; then RUN 2's first step.
'''
plans = []
P = f'{ROOT}/World/step9/DEUTERONOMY_WALK.md'; s = read(P); assert 'Sitting 4 — CHAPTER 6' not in s; plans.append((P, s.rstrip('\n') + DESIGN))
P = f'{ROOT}/logic/pre_logic_methods_2026-07-28/PROMPT_continue_solo_era_2026-08-06.md'; s = read(P); assert '#189 ADDENDUM 2' not in s; plans.append((P, s.rstrip('\n') + STATE))
P = f'{MEM}/deuteronomy-walk.md'; s = read(P)
plans.append((P, s.rstrip('\n') + "\n\nSITTING 4 — CHAPTER 6 (6:1-25, the Shema) OPENED 2026-09-17 on \"ok lets start the next chapter\" — THE FIRST SITTING UNDER THE FOUR-RUN RULE. RUN 1 DONE (the rereads, the measurements, the ink 113/0, the design in the map \"Sitting 4 — … THE DESIGN\"; the state doc #189 addendum 2 — a clean compaction point). The finds: the Sifrei's piskaot 31-36 sit ON the chapter (6:4-9, one per verse of the Shema, 67 rows); the parser reads 6:4's \"one\" as the numeral 1; the store drops 6:4's two large letters (the known defect, four tokens in the Torah); 6:25's \"as He commanded us\" is a receipt WITHOUT the Name — unseen by the register gate (owed to the compile); the Hebrew's \"ibid.\" citation form and the English export's mis-cited book (62:4) — two forms new to the scan. NEXT: RUN 2 — THE_STEPS Step 2 + Step 5's head + the compiler block reread, then the rows and the ledger (the scratchpad's ch6_* files; the map's THE ORDER paragraph). Not committed since 7c8554e.\n"))
P = f'{MEM}/MEMORY.md'; s = read(P)
old = "SITTINGS 1-3b DONE 2026-09-16 (chapters 1-5 COMPILED; 7c8554e not pushed); NEXT: chapter 6 or the schema, on his word"
new = "chapters 1-5 COMPILED (7c8554e not pushed); SITTING 4 (ch 6) RUN 1 DONE 2026-09-17; NEXT: RUN 2 the rows, the ledger"
assert s.count(old) == 1; s2 = s.replace(old, new); n = len(s2.encode('utf-8')); assert n < 17000, n; plans.append((P, s2))
for p, s2 in plans: assert s2 != read(p), p
for p, s2 in plans: open(p, 'w', encoding='utf-8').write(s2); print('WROTE', p.replace(ROOT, '<repo>').replace(MEM, '<memory>'), len(s2.encode('utf-8')))
