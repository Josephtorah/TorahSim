import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE DEUTERONOMY WALK sitting 11 — CHAPTER 13: THE DESIGN appended to the map (World/step9/DEUTERONOMY_WALK.md) after the measurements and the ink, before a
# row is typed — the section built whole before the file is opened; the map's last section asserted to be 10b's AS BUILT; the lint run after (baseline 0).
import os, re, subprocess, sys
ROOT = _ROOT
M = f'{ROOT}/World/step9/DEUTERONOMY_WALK.md'
t = open(M, encoding='utf-8').read()
heads = re.findall(r'^## .*$', t, re.M)
assert heads[-1].startswith('## Sitting 10b — THE COMPILE OF CHAPTER 12 — AS BUILT'), heads[-1]
assert '## Sitting 11 — CHAPTER 13' not in t
SEC = '''
## Sitting 11 — CHAPTER 13, Deuteronomy 13:1-19 (2026-09-21; the owner: "Go" after the reread that followed 10b's compaction): the reading and the unit — THE DESIGN, written after the measurements and the ink, before a row is typed; ONE RUN + ITS TAIL under THE COST RULES, every step timed

THE ONE RUN (timed step by step in the scratchpad's ch13_timing.tsv; the table in the AS BUILT): the rereads (the recovery page, the map's "Sitting 10b … AS
BUILT", the memory index; THE_STEPS' compiler block, Step 2 whole and Step 5's head; the map's "Sitting 10" — the reading's newest instance), the measurements
(ch13_dump0.py derived from the forms' ch12_dump0.py by twenty-five asserted substitutions; ch13_measure1.py — chapter 12's helpers and register block by
substitution, its sections chapter 13's own: THE KIN FOUND BY COMPUTATION beside THE LAW KIN NAMED, the phrase censuses, the parser, Onkelos's renderings, the
brackets, the store's gloss families and the written/read pair, the prior reads, THE REGISTER'S FINDER), THE INK (ch13_ink.py — the generic helpers COPIED from
the forms' ch12_ink.py by content markers, the kin by computation recomputed inside it, the asserts typed from the prints: GREEN ON ITS FIRST TYPED PASS — no
form fell; the driver's first launch from the scratchpad found no git root, a launch not a fact), THIS DESIGN, then the rows (the 97 spine rows in three files
by piska, the 19 Onkelos rows in one, the six outside rows in one), the ledger, THE CLEAN COMPACTION POINT, THE TAIL after the compaction: the display patch,
the manifest, the seat, the chain LAUNCHED with its readers written, the records from the sheet in one call, the forms, the commit message, the timing table.

THE DRAFT: deu_13_seducers 13:1-19 — 19 of 19 verses, missing 0 (computed from the DB's verse table: THE CHAPTER IS NINETEEN VERSES IN THE HEBREW NUMBERING,
the English's 12:32 the DB's 13:1; the Onkelos export and the Sifrei's English both count the Hebrew way — the export's chapter 13 the DB's, the identity,
cost 10; NO row of the shelf cites "12:32"), depends_on deu_12_place_name (frozen), 26 scenarios and 23 comment lines (the dump's G print), the claim prefix
DV13 absent from every unit and manifest (computed). The chapter the unit, per the ruling CHAPTER NUMBERS; NO PORTION EDGE inside it (Re'eh 11:26-16:17
holds it whole): the ledger deu_13_reeh_2026-09-21.md.

THE SPINE ON THE CHAPTER: the Sifrei on Deuteronomy heads FOURTEEN piskaot in chapter 13 (82 on 13:1, 83 on 13:2, 84 on 13:3, 85 on 13:5, 86 on 13:6, 87
on 13:7, 89 on 13:9, 90 on 13:11, 91 on 13:12, 92 on 13:13, 93 on 13:14, 94 on 13:16, 95 and 96 on 13:17; 81 on 12:30 before, 97 on 14:2 after) and ONE
PISKA WITHOUT A HEAD CITATION — 88 (two rows) opening with 13:8's "of the gods of the peoples round about you" and "from one end of the earth" — folded into
the spine on its consonants (chapter 11's lesson 2 a fifth time): FIFTEEN PISKAOT 82-96, 101 ROWS in both files (HE = EN at every piska). PISKA 96's LAST
FOUR ROWS ARE CHAPTER 14's — 96:9 opens with the citation of 14:1 ("you are children of the LORD your God"), 96:10-12 with 14:1's own clauses ("you shall not
cut yourselves", "nor make a baldness"): NEVER READ AHEAD — they wait for chapter 14's sitting (its dump's union finds 96:9, 96:11 and 96:12 by their citations
of 14:1; 96:10 cites Amos 9:6 alone and is folded by the consonant rule — recorded in COMPILE_DEBT for chapter 14's split), so NINETY-SEVEN spine rows are read
here. The union of both files' citations is 92 rows — 86 inside the spine (88's two among them), SIX outside: 117:3 (on 15:9 — "Belial" here and at 13:14, an
analogy), 149:1-2 (on 17:4 — "diligently, diligently", the seven inquiries and the probes), 189:1 (on 19:16 — "rebellion" only a transgression, 13:6 and
Jeremiah 28:16), 190:7-8 (on 19:17-18 — the analogy a third time; the two files divide 190's rows differently, the Hebrew's 190:8 the false witness's row,
the English's the probes'); NONE excluded, no interpolation; the English's slips asserted, not corrected: "(Dt.13:4)" twice at 117:3 for 13:14, "Ezek.24:16"
at 87:3 for Deuteronomy 24:16, "Josh.6:36" at 95:6 for 6:26. The spine rows without a citation in either file: six (83:3, 91:2, 92:5, 93:8, 93:9, 95:5). THE
PRIOR READS, computed: two reads of two spine rows — 82:5 at sitting 1 (1:11's "a thousand times" not added to the priests' blessing), 83:4 at the Genesis
lights sitting (the sign "in the heavens", Genesis 1:14) — each REREAD WHOLE and marked; no outside row read before.

THE KIN, CREDITED BY NAME (the counts computed from the ledgers): the sacrifice to other gods devoted — Onkelos Exodus 22:19 (1 row) at the Exodus 22
sitting; the calf's "these are your gods" — Exodus 32:1-8 (2); the stoning by the people and by the witnesses — Leviticus 20:2, 20:27 (2) and 24:14-16, 23
(4 in each of the Leviticus 24 ledgers); the wood-gatherer stoned and the high hand — Numbers 15:35-36 (2), 15:30-31 (2); the devoted thing — Leviticus
27:28-29 (2); the ban and the devoted thing in the house — 7:2, 7:16, 7:25-26 (4) at chapter 7; the fierce anger turned — Numbers 25:4 (1); Hormah's vow —
Numbers 21:2-3 (2); the testing — 8:2, 8:16 (2) at chapter 8; "not add nor diminish" — 4:2 (1); the peoples round about — 6:14 (1); the six verbs' kin — 6:13,
10:20, 11:22 (1 each); "which you have not known" — 11:28 (1); the right in His eyes — 12:25, 12:28 (2); the dream as God's speech — Numbers 12:6 (1); the
Decalogue's preamble — 5:6 (1); the redeeming — 7:8, 9:26 (1 each); NO Onkelos row of Genesis 22:1 (the testing's first seat), of Genesis 37 (the dreamer) or of
Exodus 20:2 in any ledger — those chapters read through their spines before the Onkelos standing (asserted); NEVER READ AHEAD — no ledger holds an Onkelos
row of Deuteronomy 14-20 or of the Prophets (asserted): 17:2-7's idolater and the hand first, 17:4's inquiry, 18:20-22's false prophet, 19:16-19's plotting
witness, 24:16's fathers and sons, 28:64's exile are the chapter's closest kin in the book and wait for their own sittings.

THE MEASUREMENTS' FINDS (the design's predictions for the rows; every one asserted in the ink): THE HEADER'S TWIN IS 4:2 — "all the word that I command you"
ONE seat, 4:2's plural "you shall not add … nor take away" seven tokens in order with 13:1's singular, THE ONLY TWO SEATS of the clause; THE ROOT OF ADDING
TWICE — to the word (13:1) and to the deed (13:12 "they shall not do again"); THE SEDUCER'S ONE FORMULA — "let us go (and serve) other gods which you have
not known" at 13:3, 13:7, 13:14, each the others' closest kin by computation; "let us go" the cohortative nine in the Torah (Moses' to Pharaoh, Abraham's to
the lads, Joseph's brothers' the others); "other gods" three in the chapter, seventeen in the book, forty-six in the Bible; THE DREAMER — the noun's and the
verb's only seats in the book are the chapter's three; "a sign or a wonder" with "or" ONE; the one verse of the Bible sharing two tokens with 13:2 is the man
of God's sign at Jeroboam's altar (1 Kings 13:3); THE TESTING — the verb's eight seats in the book, the participle "is testing" here alone, Genesis 22:1 the
first; "whether you are" ONE; 11:13's plural "heart and soul" the closest kin (nine tokens in order); THE SIX VERBS OF 13:5 each ONE seat, 10:20's four the
kin; "CLEAVE" seven in the book, the chapter's two — to Him (13:5) and the devoted thing to your hand (13:18, Achan's "of the devoted thing" at Joshua 7:1);
"REBELLION" the noun's two Torah seats (13:6, 19:16) and eight in the Bible; THE EXODUS FORMULA WITH REDEEMING at 13:6 (the participle's one seat in the
Bible; the verb's six in the book), 5:6's preamble at 13:11 (six tokens); "THRUST AWAY" the chapter's verb three times, 4:19's and 30:17's the kin, ten in the
book, fifty-one in the Bible; "AND YOU SHALL PURGE THE EVIL FROM YOUR MIDST" NINE seats in the Bible, all in the book, 13:6 THE FIRST; THE INCITER — "entice"
the Torah's ONE token of eighteen (Jezebel's, 1 Kings 21:25; David's to Saul, 1 Samuel 26:19 — the shelf's two citations), "the wife of your bosom" and "your
friend as your own soul" ONE each (Jonathan's love the kin), "in secret" the curses' word; "THE GODS OF THE PEOPLES ROUND ABOUT YOU" 6:14's clause spelled
defective here; "from one end of the earth to the other" 28:64's exile and Jeremiah 25:33; THE FIVE PROHIBITIONS OF 13:9 — "your eye shall not pity" the book's
five with 7:16's defective form, "spare" the Torah's two (Pharaoh's daughter; Saul told not to spare Amalek with the chapter's word at 1 Samuel 15:3),
"consent" the book's seven, five negations in one verse; THE HAND FIRST — 17:7's "the hand of the witnesses" said here of the incited, seven tokens in order,
"afterward" the Torah's two seats both this clause; TWO VERBS OF STONING — Deuteronomy's at 13:11, 17:5, 22:21, 24 against Leviticus's and Numbers' at Molech's
giver, the necromancer, the blasphemer, the wood-gatherer, 21:21 alone holding both; "ALL ISRAEL SHALL HEAR AND FEAR" the formula's four seats, 13:12 THE
FIRST and the one with the paragogic nun; "IN ONE OF YOUR CITIES" the number verse [1] (the gates' form four seats), "to dwell there" the Torah's one seat;
SONS OF BELIAL the Torah's two (13:14, 15:9), twenty-seven in the Bible, Naboth's witnesses the closest verse; THE ONE NARRATIVE VERB of the chapter inside
the third case ("and have drawn away"); THE INQUIRY — "diligently" an infinitive absolute (the chapter's FOUR: kill, diligently, smite, devote — the design's
count of three corrected at the print), five seats in the book (the calf ground "well" among them), 17:4 the twin with nine of twelve tokens in order ("in
Israel" for "in your midst"); THE SWORD AND THE BAN — "smite, you shall smite" ONE, "with the edge of the sword" the Torah's five, the ban's verb thirteen in the
Torah (Exodus 22:19's sacrificer the first), the noun eight, Joshua's Makkedah the closest verse; THE WRITTEN/READ PAIR AT 13:16 — "that city" with the masculine
written for the feminine, the Torah's standing ketiv (the feminine pronoun never written in the Torah, "that city" six seats in the book, the Prophets write
the feminine), the chapter's one ketiv; THE STORE CARRIES BOTH FORMS (329 tokens against the DB's 328); "WHOLLY TO THE LORD" 13:17 and Samuel's lamb, the
word the priest's meal offering's; "a heap forever" Ai's (Joshua 8:28), "shall not be built again" Tyre's (Ezekiel 26:14), "its street" the Torah's one; THE
FIERCE ANGER TURNED — Achan's valley (Joshua 7:26) says the chapter's words back over the devoted thing, Peor's and the calf's the kin; "give you mercy"
Jacob's word for the brothers (Genesis 43:14); "AS HE SWORE TO YOUR FATHERS" the AS_WHEN form, 13:18 and 19:8 — a run citation of the oath for 11b's census;
THE FOOTER — "when you hearken to the voice of the LORD your God" the blessing's and the curse's opening (28:1 fourteen, 28:15 twelve tokens in order), "to do
the right in the eyes of the LORD" Jehoshaphat's measure (1 Kings 22:43), three in the Bible; THE SAME LETTERS READ TWO WAYS — "you have not known" at 13:3
tagged "you (sg.) knew THEM" and at 13:14 "you (pl.) knew", Onkelos reading each as the tagger does. THE REGISTER: singular but for the prophet's case —
13:4-5 plural and mixed ("the LORD your God is testing YOU (pl.)", the six verbs all plural), 13:1 and 13:6 both, 13:8's "round about you (pl.)", 13:14's plural
the seducers' own speech; singular only in thirteen verses; THE FIRST PERSON the seducers' — "let us go" three times, "and let us serve" three, the only "we" in
the chapter the tempter's; Moses' "I" at the header and the footer; NO IMPERATIVE; NO "IF" — the three cases open on "when" (2, 7, 13), the branches on "or"
(nine, four in the inciters' list); the consecutive perfects thirteen in seven verses; the prohibitions the second person's seven and the third person's four;
THE NAME ten bare tokens and "to the LORD" once; Israel named ONCE (13:12), Egypt twice, Moses never; NO DIVINE FRAME. THE PARSER: ONE NUMBER VERSE (13:13
"in one of your cities" [1]), no starred token; 13:18's "swore" no number (the dump's bare check matched the seven inside the oath's root — an instrument's slip,
as the dump's name test matched two niphal perfects by the letters "Np"); the kin's numbers 17:6's [2, 3, 1], 19:15's [1, 2, 3], 17:2's [1]. THE STORE: 192
distinct glosses, 27 already rewritten; the two "?" glosses the store's "I"; THE DISPLAY PATCH predicted from the ink's own lists: 34 by gloss ("apostasy" →
"rebellion", "bind-firmly" left to reference, "without-profit" → "Belial", "the-physical--a-net" → "the-devoted-thing", "speck" → "anything", "stability" →
"truth", "commiserate" → "spare", "prick-you/your" → "entices-you", "and-be-weighty-him/its" → "and-you-shall-stone-him" …) and 139 by reference ("when" for
the three cases' "that", "a-dreamer-of", "is-testing", "gods" for the three "God"s, "the-sword" twice at 13:16, "wholly", "a-heap", "His-anger", "He-swore" …).

THE CLAIMS (six, DV13-01..06, one manifest; the spine's rows distributed by piska from the CITE INDEX): 01 THE HEADER (13:1 — Onkelos 1, Sifrei 82; the check
"you shall not add" at 13:1); 02 THE PROPHET AND THE TEST (13:2-6 — Onkelos 2-6, Sifrei 83-86, 189:1; "is testing" at 13:4); 03 THE INCITER (13:7-12 —
Onkelos 7-12, Sifrei 87-91 with the headless 88, 117:3; "entices you" at 13:7); 04 THE CITY HEARD OF, THE INQUIRY AND THE SWORD (13:13-16 — Onkelos 13-16,
Sifrei 92-94, 149:1-2, 190:7-8; "diligently" at 13:15); 05 THE WHOLE OFFERING, THE HEAP AND THE MERCY (13:17-18 — Onkelos 17-18, Sifrei 95, 96:1-5; "wholly"
at 13:17); 06 THE FOOTER (13:19 — Onkelos 19, Sifrei 96:6-8; "the right in the eyes of" at 13:19). Seated as six WITNESS_READ operators at 13:1, 2, 7, 13, 17,
19 with step E. THE FOLD predicted: units 226 -> 227, standing 2239 -> 2245, the hash 8b8fff1fa28953af unmoved (the law layer moves no narrative fact). THE
REGISTER GATE at the reading: no receipt, no header, no footer in chapter 13 (the finder run — 13:18's "as He swore" the oath's form, not a receipt) — GREEN
expected, --strict, DECLARED 100 unmoved.

THE TESTING SHELF routed to 11b's docket (the union rule at the compile): Mishnah Sanhedrin 7:10 and Sanhedrin 67a (the inciter — the concealed witnesses, the
entrapment), 7:6 (the acts of honor — 91:4), 10:4-6 and Sanhedrin 111b-113b (the condemned city — the number, the border, the children, the property, the spoil,
the heap), 11:1 and 11:5-6 with Sanhedrin 89a-90a (the false prophet strangled — 86:6's R. Shimon; the sign, Elijah on Carmel a temporary measure), 5:1-2 and
Sanhedrin 40a-41a (the seven inquiries and the probes — 93:6-9, 149, 190), 1:5 (one city, not three — 92:3), 11:4 with Sanhedrin 89a (the festival's execution
— 91:1-2), 4:1 (the verdict returned — 89:6-7); Tosefta Sanhedrin 11:7, 12:6, 14:1-6 (the English's parallels); Mishnah Zevachim 8:10 with Zevachim 80a-81b and
Tosefta Zevachim 8:23 (the mixed bloods — 82:3); Mishnah Sukkah 3:4 and Sukkah 34b, Menachot 41b-42a (the four species and the fringes — 82:4); Rosh Hashanah
28b and Eruvin 96a, Sanhedrin 88b (the law of not adding — 82:4-5, the priests' blessing); Mishnah Avodah Zarah 3:9 with Avodah Zarah 49b-50a (the benefit
to the Salt Sea — 96:2); Mishnah Makkot 1:4-6 (the plotting witness — 86:3's a fortiori); Bava Metzia 59b and Yevamot 90b (the prophet's sign not decisive; the
prophet's temporary uprooting); Tosefta Bava Kamma 9:30 and Shabbat 151b (the mercy two-armed — 96:4); Avot 2:1 and 3:14; Mishnah Avot 3:9; Sifrei Numbers
103, 113, 114 (the English's parallels); the Sifra on Leviticus 20 and 24 credited from their sittings.

THE ORDER (the rest of the one run): the 97 spine rows WHOLE in both files piska by piska (ch13_spine_p82.txt … p96.txt) → ch13_rows_sifrei_82_86.py,
_87_92.py, _93_96.py (chapter 12's form; the cuts by consonants SP_), ch13_rows_onkelos.py (13:1-19), ch13_rows_outside.py (the six; HP / AP / SP_) →
write_ch13_ledger.py (from write_ch12_ledger.py's form — the prior reads marked REREAD WHOLE) → lint 0, coverage computed (the Sifrei 97 + 6; Onkelos 19; the
kin's credits by name) → THE CLEAN COMPACTION POINT (the state doc; the recovery page's section 2; the reread the map's "Sitting 11 … THE DESIGN" — this
section) → THE TAIL: ch13_patch_overrides.py (34 by gloss, 139 by reference; the anchors sitting 10's last rows), the ink rerun PATCHED → write_ch13_manifest.py
(six claims) → seat_ch13.py (six WITNESS_READ at 13:1, 2, 7, 13, 17, 19; step E) → ch13_gates.sh LAUNCHED in the background (ch13_chain.sh: the seat,
verify_text, the ritual; ch13_fold.sh: 227 / 2245 / the hash unmoved; build_world; the journal gate; the register gate --strict; large_letter_probes; the
home-path gate) with write_ch13_records.py and copy_ch13_forms.py written first → the summary read once → the records from the sheet in one call → the forms
copied → the commit message → the timing table → the report.
'''
assert not re.search(r'/Users/(?!Shared/)', SEC) and os.path.expanduser('~') not in SEC
open(M, 'a', encoding='utf-8').write(SEC)
r = subprocess.run([sys.executable, f'{ROOT}/logic/solo_tools/gloss_lint.py', M], capture_output=True, text=True)
print('design appended:', len(SEC.encode()), 'bytes; the map', len(open(M, encoding='utf-8').read().splitlines()), 'lines; lint rc', r.returncode, (r.stdout + r.stderr).strip()[-300:])
assert r.returncode == 0, 'THE LINT FLAGGED THE MAP'
