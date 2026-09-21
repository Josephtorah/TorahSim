import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
import os, re, subprocess
ROOT = _ROOT   # the scratch form: ROOT from git, never typed
# THE DEUTERONOMY WALK sitting 10 — CHAPTER 12 (2026-09-20; the owner: "Monitor how long each step takes and report when the chapter is done"): THE DESIGN
# appended to the map after the measurements and the ink, before a row is typed. The guard names THE SITTING (5b's lesson).
P = ROOT + '/World/step9/DEUTERONOMY_WALK.md'
s = open(P, encoding='utf-8').read()
HDR = '## Sitting 10 — CHAPTER 12, Deuteronomy 12:1-31 (2026-09-20; the owner: "Monitor how long each step takes and report when the chapter is done" — the first sitting under THE COST RULES A-B-C): the reading and the unit — THE DESIGN, written after the measurements and the ink, before a row is typed; ONE RUN + ITS TAIL, every step timed'
assert HDR not in s and '## Sitting 10 — CHAPTER 12' not in s
D = HDR + '''

THE ONE RUN (timed step by step in the scratchpad's ch12_timing.tsv — the owner's ask; the table in the AS BUILT): the rereads (the recovery page, the map's
"THE COST AUDIT AND THE THREE RULES" with 9b's AS BUILT above it, the memory index; THE_STEPS' compiler block, Step 2 whole and Step 5's head; the map's
"Sitting 9" — the reading's newest instance), the measurements (ch12_dump0.py derived from the forms' ch11_dump0.py by twenty-six asserted substitutions;
ch12_measure1.py — chapter 11's helpers and register block by substitution, its sections chapter 12's own: THE KIN FOUND BY COMPUTATION for the first time —
every verse against every verse of the Bible by shared distinct tokens, the closest re-scored in order — beside THE LAW KIN NAMED and diffed in full; the phrase
censuses; the parser; Onkelos's renderings; the brackets; the store's gloss families; the prior reads; THE REGISTER'S FINDER run on the chapter), THE INK
(ch12_ink.py — the generic helpers COPIED from ch11_ink.py by content markers; the asserts typed from the prints; FIVE fell on the first pass, none a fact: the
English's unopened "Dt.13:29)" at 179:2, 138:1's head citation counted by the regex, the "how?" gloss caught by a '?' substring test, the computed kin asserted
before its computation, the by-gloss count sixty-nine; 0 on the second), THIS DESIGN, then the rows (the 159 spine rows in files by piska, the 31 Onkelos rows in
two, the seven outside rows in one), the ledger, THE CLEAN COMPACTION POINT (the 400k cap — chapter 11's precedent at #198), THE TAIL after the compaction: the
display patch, the manifest, the seat, the chain (the seat, verify_text, the ritual, the fold, build_world, the journal gate, the register gate --strict,
large_letter, the home gate) LAUNCHED with its readers written, the records from the sheet in one call, the forms, the commit message, the timing table, the report.

THE DRAFT: deu_12_place_name 12:1-31 — 31 of 31 verses, missing 0 (computed from the DB's verse table: THE CHAPTER IS THIRTY-ONE VERSES IN THE HEBREW NUMBERING,
the English's 12:32 the DB's 13:1 — chapter 11's ink had measured it), depends_on deu_11_bless_curse_set AND lev_17_blood_center (both frozen — asserted: the
tree-derived draft names Leviticus 17 as its kin before any reading), 38 scenarios and 35 comment lines (typed from the dump's G print), the claim prefix DV12
absent from every unit and manifest (computed). The chapter the unit, per the ruling CHAPTER NUMBERS; NO PORTION EDGE inside it (Re'eh 11:26-16:17 holds it
whole): the ledger deu_12_reeh_2026-09-20.md.

THE SPINE ON THE CHAPTER: the Sifrei on Deuteronomy heads TWENTY piskaot in chapter 12 (59 on 12:1, 60 on 12:2, 61 on 12:3, 62-63 on 12:5, 64 on 12:7, 65 on
12:8, 66 on 12:9, 67 on 12:10, 69 on 12:12, 70 on 12:13, 71 on 12:15, 72 on 12:17, 75 on 12:20, 76 on 12:23, 77 on 12:26, 78 on 12:27, 79 on 12:28, 80 on
12:29, 81 on 12:30; 58 on 11:32 before, 82 on 13:1 after) and THREE PISKAOT WITHOUT A HEAD CITATION — 68 (six rows) opening with 12:11's "your burnt
offerings", 73 (one row) with 12:17's "your herd and your flock", 74 (nine rows) with 12:17's "your vows" — folded into the spine on their consonants
(chapter 11's lesson 2 at piska 45, three times over): TWENTY-THREE PISKAOT 59-81, 159 ROWS in both files (HE = EN at every piska), split by piska for the
reading (ch12_spine_p59.txt … p81.txt). The union of both files' citations is 144 rows — 137 inside the spine, SEVEN outside: 2:2 (on 1:2 — "rest" is the Land,
12:9), 106:5 (on 14:23 — the firstling compared to the second tithe, 12:17), 138:1 (on 16:11 — the rejoicing, 12:7), 145:3 (on 16:21 — the Asherah not
planted, 12:3), 147:2 (on 17:1 — the proscriptions listed, 12:17), 179:2 (on 19:1 — build anywhere, 12:29; the English's "Dt.13:29)" a wrong chapter, the Hebrew
right), 286:16 (on 25:1 — the blood's reward, 12:23); NONE excluded, no interpolation. The spine rows without a citation in either file: eleven (63:10, 65:6,
72:8-9, 75:4, 76:2-3, 76:6, 77:2, 77:5, 79:2). THE PRIOR READS, computed: five reads of four spine rows — 61:7 at chapter 7 (the renaming of the shrines), 80:4-5
at chapter 11 (the sages weeping at the border), 75:2 at two Genesis sittings (the Kenite's land) — and 2:2 at sitting 1; every one REREAD WHOLE and marked.

THE KIN, CREDITED BY NAME (the counts computed from the ledgers): the slaughter at the tent's door and the blood — Onkelos Leviticus 17:1-16 (16 rows) at the
Leviticus 17-18 sitting; the priests' and Levites' dues — Onkelos Numbers 18:8-32 (25); the shrines and the idols' silver — Onkelos 7:5, 7:25-26 (3) at
chapter 7; Molech — Onkelos Leviticus 20:2-5 (4) and 18:21 (1); the dispossession — Numbers 33:52 (1); the angel's clause — Exodus 23:24 (1); THE ALTAR IN EVERY
PLACE (Exodus 20:21) through the Mekhilta alone (the compiler code hunt's two rows; no ledger holds an Onkelos row of Exodus 20:21, of Genesis 9:4, of Exodus
34:13 or 34:24 — asserted); NEVER READ AHEAD — no ledger holds an Onkelos row of Deuteronomy 13-16 (asserted): 14:22-29's tithe, 15:19-23's firstling, 16's
feasts are the chapter's closest kin in the book (12:18 shares thirteen tokens in order with 16:11) and wait for their own sittings.

THE MEASUREMENTS' FINDS (the design's predictions for the rows): THE HEADER'S TWIN IS THE FOLD'S FOOTER — "these are the statutes and the judgments" (12:1)
stands at Leviticus 26:46 alone beside it (the fold's closing line; 59:1-4 read its four nouns as the midrash, the laws, the mishnah, the deed); THE VERB OF
ISRAEL'S PERISHING TURNED ON THE SHRINES — 12:2's doubled "destroy, you shall destroy" is 4:26's, 8:19's and 30:18's "perish, you shall perish" in the piel (the
lemma's three seats in the chapter); THE KINGS' FORMULA — "under every leafy tree" is the Kings' and the prophets' phrase for the high places (ten seats, 12:2 the
Torah's one); THE DEMOLITION SAID IN NEW WORDS — 12:3 shares two tokens in order with 7:5 and three with Exodus 34:13, 12:2 none with 7:5 (five verbs where 7:5
had four: the name destroyed the fifth — 61:7's dispute, the renaming); THE PAIR'S TWO SEATS — "you shall not do so to the LORD your God" plural at 12:4 and
singular at 12:31 (81:5 reads the singular as the offering brought to the wrong altar); THE PLACE WHICH THE LORD WILL CHOOSE six times in the chapter, "will
choose" twenty-three seats in the book and NONE BEFORE CHAPTER 12 — the chapter installs the phrase; "to put His name there" (12:5, 21) and "to make His name
dwell" (12:11) the two forms, "His dwelling" (12:5) ONE seat in the Bible — Onkelos makes every one the SHEKHINAH ("the house of His Shekhinah" at 12:5 beside
32:40 alone); ONE VERB FOR TWO SEEKINGS — "seek" His dwelling (12:5) and "inquire" after their gods (12:30), the lemma's two seats in the chapter; THE SEVEN
OFFERINGS listed three times (12:6, 11, 17) with the list changing — "the choice of your vows" added at 12:11, the tithe of grain, wine and oil named at 12:17
(68:6 reads the two lists as Shiloh's and Jerusalem's); THE SABBATH'S HOUSEHOLD (5:14's "you and your son and your daughter, your manservant and your
maidservant") said again at 12:18 and at the feasts (16:11, 14); "EVERY MAN WHAT IS RIGHT IN HIS EYES" (12:8) Judges' refrain (17:6, 21:25 — the run's own
witness that the place was not yet chosen); "THE REST AND THE INHERITANCE" (12:9) — Numbers 10:33's ark seeking a resting place (2:2's row), 66:2's dispute
which is Shiloh and which Jerusalem; "TAKE HEED TO YOURSELF LEST" THREE TIMES IN ONE CHAPTER (13, 19, 30; nine in the Bible) — the shelf reads each as a
prohibition (70:1, 74:6-7, 81:1); "ONLY" FOUR TIMES (15, 16, 23, 26) and "BUT" once (22) — the restrictive clauses the shelf reads at 71:1, 71:5, 71:11, 75:14,
76:2, 77:9; THE SLAUGHTER LAW SAID IN NEW WORDS — Leviticus 17:3-5 (every slaughter at the tent's door) shares ONE token in order with 12:15: the release from it
is named by the shelf (75:3 R. Ishmael: the flesh of desire forbidden in the wilderness, permitted by this verse), never by Leviticus's words; THE GAZELLE'S
HOMOGRAPH — the animal's consonants are "the beauty" (2 Samuel 1:19; the DB's lemma 6643 b against 6643 a; the store glossed the animal "splendor"); "ON THE
EARTH YOU SHALL POUR IT LIKE WATER" (12:16, 24; 15:23) — Leviticus 17:13 covers the blood with dust, no token shared (71:14 reads "like water": permitted for
benefit, prepares seeds for uncleanness, exempt from covering); "YOU MAY NOT" (12:17) read by 72:1 as "you are not permitted" — Onkelos the same ("you have no
permission"); THE LEVITE'S VERSE ALONE — no verse of the Bible shares two non-stop tokens with 12:19; "AS HE HAS SPOKEN TO YOU" (12:20) the AS_WHEN form (four
seats in the book; 75:2 reads the promise as Genesis 15:19-20's three lands, Rabbi as Ezekiel 48's) — a RUN_CITATION pointer at 10b's census; "AS I HAVE
COMMANDED YOU" (12:21) — THE RECEIPT WITHOUT THE NAME, one kin in the Bible (Exodus 23:15's unleavened bread), the register's finder BLIND to it (measured: its
two forms carry the Name, no receipt found in chapter 12; the third form owed since 4b and 6b, now the fourth seat — 12:21 the shelf's seat of the slaughter's laws,
75:6 "just as holy things by slaughter, so common", 75:15 Rabbi: Moses commanded the windpipe and the gullet — Chullin 28a at 10b's docket); "BE STRONG" said to
a man about the blood (12:23) — the word said to Joshua (1:38, 31:7, 23); "THE BLOOD IS THE LIFE" — Leviticus 17:11's clause turned (three tokens shared),
Genesis 9:4's none; "SHALL BE POURED" the sin offering's verb (Leviticus 4:7, 18, 25, 30, 34) said of the sacrifices' blood at 12:27 (78:6-8 the one pouring);
"THAT IT MAY GO WELL WITH YOU AND YOUR CHILDREN AFTER YOU" 12:25 and 12:28 alone; "THE GOOD AND THE RIGHT" (12:28) 6:18's pair and Kings' measure of a king
(79:5 the good in Heaven's eyes, the right in men's); THE DB'S 13:1 IS THE ENGLISH'S 12:32 ("you shall not add nor take away" — chapter 13's reading); "LEST
YOU BE ENSNARED" (12:30) — the snare's root here (נקש) not 7:25's (יקש), the Torah's one seat of each niphal; "EVERY ABOMINATION OF THE LORD WHICH HE HATES"
(12:31) — "which He hates" 12:31 and 16:22 alone, "abomination of the LORD" eight in the book; THE CHILDREN BURNED — Jeremiah 7:31's six shared tokens, 2 Kings
17:31's four, Leviticus 18:21's three; THE KING-WORD'S HOMOGRAPH — Molech's consonants are "to the king" (the census's slip at 7:8 and 11:3), 12:31 names no
Molech. THE REGISTER: the chapter switches number at its middle — plural only in eight verses (2-4, 6, 8, 10-12), both in five (1, 5, 7, 9, 16 — the singular
inside the plural verse), singular only in eighteen (13-31), neither in none; the paragogic nun six times, all in the plural half; Moses' "I" three, "I have
commanded you" one, the eater's "let me eat" (20), the seeker's "and I will do so, I too" (30 — the chapter's one "saying"); the imperatives five (13, 19, 30 the
niphal "take heed"; 23 "be steadfast"; 28 "observe"); the infinitive absolute one (2); the consecutive perfects twenty-three in fifteen verses; NO WAYYIQTOL —
no narrative verb in the chapter; the prohibitions eight (4, 8, 16, 17, 23, 24, 25, 31); the Name twenty-three; Israel, Egypt and Moses unnamed (Moses unnamed
6-14 held). THE PARSER: ONE NUMBER VERSE (12:14 "in one of your tribes" [1]) and ONE STARRED TOKEN (12:17's "tithe" — starred at every tithe seat of the book,
the ten-word's homograph); the kin's numbers 14:28's [3] and Exodus 34:24's [3]. THE STORE = THE DB (520 tokens, 2,051 letters, no written/read pair); the four
"?" glosses the store's "I"; 241 distinct glosses, 36 already rewritten (choose, only, the-blood, the-statutes, abomination …); THE DISPLAY PATCH predicted: 69
by gloss (rejoice, the gazelle, the hart, the unclean, together, your-vows, your-tithes, their-gods, your-God …) and 124 by reference (the Shekhinah's "his-name",
"but … only" for the restrictive clause, "you-may", "is-too-far", "the-life" twice at 12:23, "I-have-commanded-you", "be-steadfast", "let-me-eat" …).

THE CLAIMS (six, DV12-01..06, one manifest; the spine's rows distributed by piska from the CITE INDEX): 01 THE HEADER AND THE DEMOLITION (12:1-4 — Onkelos 1-4,
Sifrei 59-61, 145:3; the check "you shall destroy" at 12:2); 02 THE PLACE CHOSEN (12:5-12 — Onkelos 5-12, Sifrei 62-69, 2:2, 138:1; "His dwelling" at 12:5, the
one seat); 03 THE BURNT OFFERINGS ONLY THERE (12:13-14 — Sifrei 70; "in one of" at 12:14); 04 THE PROFANE SLAUGHTER, THE BLOOD AND THE GATES (12:15-19 — Sifrei
71-74, 106:5, 147:2; "as the gazelle" at 12:15); 05 THE BORDER ENLARGED AND THE ALTAR (12:20-28 — Sifrei 75-79, 286:16; "I have commanded you" at 12:21); 06 THE
NATIONS CUT OFF AND THE ABOMINATION (12:29-31 — Sifrei 80-81, 179:2; "be ensnared" at 12:30). Seated as six WITNESS_READ operators at 12:1, 5, 13, 15, 20, 29
with step E. THE FOLD predicted: units 225 -> 226, standing 2233 -> 2239, the hash 8b8fff1fa28953af unmoved (the law layer moves no narrative fact). THE
REGISTER GATE at the reading: the header at 12:1 already on the index as a declared EMPTY seat (the seat waits for the compile) — GREEN expected, --strict.

THE TESTING SHELF routed to 10b's docket (the union rule at the compile): Mishnah Zevachim 14:4-8 and Zevachim 112b-119b (the stations of the high places — the
Dwelling, Gilgal, Shiloh, Nob and Gibeon, Jerusalem; 65:1-2, 66:1-2), Megillah 9b-10a; Mishnah Avodah Zarah 3:5, 3:7 and Avodah Zarah 45a-48b (the mountains
not forbidden, the three Asherim, the three houses — 60:4, 61:5-6); Chullin 16b-17a (the flesh of desire — 75:3), 28a (the windpipe and the gullet — 75:15),
84a-b (12:20-21's civility — 75:5), Chullin 2:9 and 6:1 (the blood like water — 71:14; Makhshirin 6:4), 8:1-4 and 113a-116a (meat in milk from "you shall not eat
it" — 76:7-8), 10:1 (the gifts — 71:9-10), 102b-103a (the limb from the living — 76:5); Mishnah Bekhorot 2:2-3, 9:3 and Bekhorot 15a-16a, 33a-b (the blemished
consecrated redeemed, the tithe's joint owners — 71:1-6, 77:7-8); Mishnah Temurah 3:5 and Temurah 3b-4a, 17b (the substitute — 77:5-6, 78:9-10); Mishnah Makkot
3:3, 3:15 and Makkot 13a-b, 17a-19b, 23b (the tithe and the firstling outside the wall, the first fruits before the confession, the blood's reward — 72:2-11,
73:1, 74:1, 76:2, 76:9); Mishnah Sotah 7:6 and Sotah 37b-38b (the Name as written — 62:4); Sanhedrin 20b (the three commandments on entering — 67:1-3);
Mishnah Zevachim 9:5-6 and Zevachim 83a-86a (the bones and the sinews, the pieces that flew off — 78:4-5, 78:10), Zevachim 37a (the one application — 78:7-8),
Tosefta Zevachim 4:1 (78:1-2); Mishnah Kiddushin 1:9 and Kiddushin 36b-37a (the commandments dependent on the Land — 59:5); Rosh Hashanah 4a-6b ("do not
delay" — 63:5); Mishnah Yoma 1:1 (his house is his wife — 64:4); Tosefta Sheqalim 2:1 (79:5); Avot 2:1 (79:4); Pesachim 8b (the Levite's pilgrimage); Tosefta
Menachot 9:2 (from the choicest — 68:4); Sanhedrin 74a-b (the persecution — 76:3); Yevamot 47b, Keritot 20b-22a (the blood's classes); the Sifra on Leviticus 17
credited from its sitting; Seder Olam 11 (the fourteen years — 65:2, 66:1).

THE ORDER (the rest of the one run): the 159 spine rows WHOLE in both files piska by piska (ch12_spine_p59.txt … p81.txt) → ch12_rows_sifrei_59_62.py, _63_67.py,
_68_71.py, _72_74.py, _75_76.py, _77_81.py (chapter 6's form; the cuts by consonants SP_), ch12_rows_onkelos_a.py (12:1-16), ch12_rows_onkelos_b.py (12:17-31),
ch12_rows_outside.py (the seven; HP / AP / SP_) → write_ch12_ledger.py (from write_ch11_ledger.py by asserted substitutions where generic — the prior reads marked
REREAD WHOLE) → lint 0, coverage computed (the Sifrei 159 + 7; Onkelos 31; the kin's credits by name) → THE CLEAN COMPACTION POINT (the state doc; the recovery
page's section 2; the reread the map's "Sitting 10 … THE DESIGN" — this section) → THE TAIL: ch12_patch_overrides.py (69 by gloss, 124 by reference; the anchors
sitting 9's last rows), the ink rerun PATCHED → write_ch12_manifest.py (six claims) → seat_ch12.py (six WITNESS_READ at 12:1, 5, 13, 15, 20, 29; step E) →
ch12_gates.sh LAUNCHED in the background (ch12_chain.sh: the seat, verify_text, the ritual; ch12_fold.sh: 226 / 2239 / the hash unmoved; build_world; the journal
gate; the register gate --strict; large_letter_probes; the home-path gate) with write_ch12_records.py and copy_ch12_forms.py written first → the summary read
once → the records from the sheet in one call → the forms copied → the commit message → the timing table → the report.
'''
s = s.rstrip('\n') + '\n\n\n' + D
assert not re.search(r'/Users/(?!Shared/)', D) and '<home>' not in D   # the username never typed, not even as a guard (9b's lesson 13)
open(P, 'w', encoding='utf-8').write(s)
print('the design appended:', len(D.encode()), 'bytes; the map', len(s.encode()))
