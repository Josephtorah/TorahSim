import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE DEUTERONOMY WALK sitting 13 — CHAPTER 15: THE DESIGN appended to the map (World/step9/DEUTERONOMY_WALK.md) after the measurements and the ink, before a
# row is typed — the section built whole before the file is opened; the map's last section asserted to be 12b's AS BUILT; the lint run after (baseline 0);
# every count in the section READ from the prints and the files (the asserts counted in the ink, the timing rows parsed). Sitting 12's form
# (write_ch14_design.py). RUN FROM THE REPO ROOT.
import os, re, subprocess, sys
ROOT = _ROOT
SP = os.path.dirname(os.path.abspath(__file__))
M = f'{ROOT}/World/step9/DEUTERONOMY_WALK.md'
t = open(M, encoding='utf-8').read()
heads = re.findall(r'^## .*$', t, re.M)
assert heads[-1].startswith('## Sitting 12b — THE COMPILE OF CHAPTER 14 — AS BUILT'), heads[-1]
assert '## Sitting 13 — CHAPTER 15' not in t
ink = open(f'{SP}/ch15_ink.py', encoding='utf-8').read(); NA = len(re.findall(r'^assert ', ink, re.M))
run1 = open(f'{SP}/ch15_ink_run1.out', encoding='utf-8').read(); run2 = open(f'{SP}/ch15_ink_run2.out', encoding='utf-8').read()
F1 = int(re.search(r'^(\d+) failing statements', run1, re.M).group(1)); F2 = int(re.search(r'^(\d+) failing statements', run2, re.M).group(1)); assert F2 == 0
MB = os.path.getsize(f'{SP}/ch15_measure1.out'); DB_ = os.path.getsize(f'{SP}/ch15_dump0.out')
SEC = f'''

## Sitting 13 — CHAPTER 15, Deuteronomy 15:1-23 (2026-09-22; the owner: "Go" after the compaction at #205 addendum 5 — chapters 1-14 pushed through 049f55c): the reading and the unit — THE DESIGN, written after the measurements and the ink, before a row is typed; TWO RUNS + THE TAIL under THE COST RULES (the #204 NOTE — sitting 12's lesson 1), every step timed; THE ROWS IN TWO HALVES WITH THE CLEAN POINT BETWEEN THEM UNCONDITIONALLY

THE RUNS (timed step by step in the scratchpad's ch15_timing.tsv; the table in the AS BUILT): RUN A — the rereads (the recovery page, the map's "Sitting 12b …
AS BUILT", the memory index; the state doc's #205 addendum 5; THE_STEPS' compiler block, Step 2 whole and Step 5's head; the map's "Sitting 12" — the reading's
newest instance, its design and AS BUILT), the measurements (ch15_dump0.py derived from the forms' ch14_dump0.py by twenty-seven asserted substitutions — the
derive's own guard tripped twice on legitimate text (the file names printed twice; a slice the form's own) and was relaxed to the form's; the spine split by piska
with NO tail folded in — piska 110's five rows were read whole at chapter 14 and 126's rows stop before 16:1's words, both checked on the consonants;
ch15_measure1.py — chapter 14's helpers and register block by substitution, its sections chapter 15's own in two files: THE KIN FOUND BY COMPUTATION beside THE
LAW KIN NAMED and THE TWIN LAWS diffed verse by verse (Exodus 21:2-7 at 15:12-18; Exodus 23:10-11 and Leviticus 25 at 15:1-11; the firstling's and the blemish's
seats at 15:19-21; chapter 12's clauses at 15:20-23; the formulas at 15:5, 6, 9, 11, 15), the phrase censuses, the parser, Onkelos's renderings, the brackets, the
store's gloss families, the prior reads, THE REGISTER'S FINDER — {MB:,} bytes of print, read in four pages; its first run fell on its own instrument (a list inside a
set), retyped), THE INK (ch15_ink.py — the generic helpers COPIED from the forms' ch14_ink.py by content markers, the kin by computation recomputed inside it,
{NA} asserts typed from the prints: {F1} fell on the FIRST typed pass — every one the INSTRUMENT'S SHAPE, not a fact: a ledger's whole-row count typed where the
Onkelos-row count was measured, a verse range typed one verse too wide (Exodus 22:24-29 where the ledger holds one row of 22:27-28), the firstling's short form
בְּכֹר ("firstling", 15:19) typed without its preposition — retyped from the print; {F2} on the second), THIS DESIGN, THE CLEAN COMPACTION POINT (#206). RUN B1 —
THE FIRST HALF of the rows: piskaot 111-118 (63 rows — the release, the needy, the blessing, the hand opened and shut, the base thought, the giving) WHOLE in
both files, Onkelos 15:1-11, the four outside rows on the first half (109:3 on "the end" — REREAD WHOLE from chapter 14; 41:3 on the commandments before the
conquest — REREAD WHOLE from chapter 11; 279:4 on the hireling's cry; 355:9 on Moses' righteousness) → the import check → THE CLEAN COMPACTION POINT
UNCONDITIONALLY. RUN B2 — THE SECOND HALF: piskaot 119-126 (36 rows — the slave's gift, the slave remembered, the awl, the double hire, the firstling, the year,
the blemish, the blood), Onkelos 15:12-23, the six outside rows on the second half (106:5 the firstling whose year passed — REREAD WHOLE from chapters 12 and 14;
71:6-8 the blemished consecrated and the unclean and the clean — REREAD WHOLE from chapter 12; 147:3-4 the blemishes) → the import check → the ledger with
coverage COMPUTED → lint 0 → THE CLEAN COMPACTION POINT. THE TAIL after the compaction: the display patch, the manifest, the seat, the chain LAUNCHED with its
readers written, the records from the sheet in one call, the forms, the commit message, the timing table.

THE DRAFT: deu_15_release_firstborn 15:1-23 — 23 of 23 verses, missing 0 (computed from the DB's verse table: the export's chapter 15 = the DB's, the identity,
cost 20; NO fold of the English's numbering), depends_on deu_14_food_tithe (frozen), lev_25_shemittah (frozen — the sabbatical year and the sold brother) and
exo_21_slave_person (frozen — THE TWIN LAW of the Hebrew slave, the draft's own edge; its reading the law era's, no Onkelos row in any ledger), 30 scenarios and
27 comment lines (the dump's G print), the claim prefix DV15 absent from every unit and manifest (computed). The chapter the unit, per the ruling CHAPTER
NUMBERS; NO PORTION EDGE inside it (Re'eh 11:26-16:17 holds it whole): the ledger deu_15_reeh_2026-09-22.md.

THE SPINE ON THE CHAPTER: the Sifrei on Deuteronomy heads SIXTEEN piskaot in chapter 15 (111 on 15:1, 112 on 15:2, 113 on 15:3, 114 on 15:4, 115 on 15:5, 116
on 15:6, 117 on 15:9, 118 on 15:11, 119 on 15:13, 120 on 15:15, 121 on 15:16, 122 on 15:17, 123 on 15:18, 124 on 15:19, 125 on 15:20, 126 on 15:21; 110 on
14:29 before, 127 on 16:1 after) — THE HEADS IN VERSE ORDER this chapter (chapter 14's were not); seven verses carry no head (7, 8, 10, 12, 14, 22, 23); 99
rows in both files (HE = EN at every piska); NO TAIL FOLDED IN (piska 110's rows all on 14:29, read at chapter 14; 126's on 15:21-23 — 126:2 cites 15:23), so
NINETY-NINE spine rows are read here. The union of both files' citations is 99 rows — 89 inside the spine, TEN outside: 41:3 (on 11:13 — the commandments
observed only after the conquest; the English cites 15:9) READ BEFORE at chapter 11's sitting; 71:6, 71:7, 71:8 (on 12:15 — the blemished consecrated
slaughtered only for a permanent blemish, "the unclean and the clean"; the Hebrew and the English cite 15:22) READ BEFORE at chapter 12's; 106:5 (on 14:23 —
the firstling whose year passed; the Hebrew cites 15:20) READ BEFORE at chapters 12 and 14 — its THIRD read; 109:3 (on 14:28 — "the end" here and at 15:1; the
English cites 15:1 twice) READ BEFORE at chapter 14's; 147:3 and 147:4 (on 17:1 — the blemishes: scabs, warts, tumors; the English cites 15:21); 279:4 (on
24:15 — the hireling's cry; the Hebrew cites 15:9); 355:9 (on 33:20 — Moses' righteousness; the Hebrew cites 15:7) — the SIX read before REREAD WHOLE and marked,
the FOUR fresh; NONE excluded, no interpolation, no "ibid.". The spine rows without a citation in either file: five (111:4, 111:6, 112:2, 116:17, 122:5). THE
PRIOR READS, computed: two spine rows read before — 117:3 at chapter 13's sitting ("take care" — the row cites 13:4), 116:18 at the Genesis 2 sitting ("a
helper" — the row cites Genesis 2:18) — each REREAD WHOLE and marked; 884 prior Sifrei rows in the ledgers.

THE KIN, CREDITED BY NAME (the counts computed from the ledgers): THE SABBATICAL AND THE SOLD BROTHER — Leviticus 25 in three ledgers (25:1-7 (7 Onkelos
rows), 25:35-38 (4), 25:39-55 (17)); THE BLEMISH — Leviticus 22:17-27 (11), the priests' 21:16-23 (8); THE FIRSTLING — Leviticus 27:26 (1), Numbers 18:15-18
(4); THE PLACE, THE GAZELLE AND THE HART, THE BLOOD — 12:6, 15-18, 22-24 (8) at chapter 12; THE POOR AT THE GATE — 14:28-29 (2) at chapter 14; THE SLAVE
REMEMBERED — 5:15 (1) at chapter 5; AND NO ONKELOS ROW OF EXODUS 21:2-11, 23:10-11, 22:24-26, 22:29, 13:2-16 OR 34:19-20, NOR OF GENESIS 4:4, IN ANY LEDGER
(asserted) — Exodus 21's slave, 23's seventh year and 13's firstborn were read in the law era through their spines before the Onkelos standing (the units
exo_21_slave_person, exo_23_justice_calendar, exo_13_* frozen); NEVER READ AHEAD — no ledger holds an Onkelos row of Deuteronomy 16-26 or of the Prophets
(asserted): 16:5's "one of your gates", 16:12's slave remembered, 17:1's blemish, 23:17's escaped slave, 23:20-21's interest, 24:10-15's pledge and the
hireling's cry, 24:18-22's sojourner, 28:12's lending, 31:10's release-year assembly wait for their sittings; Jeremiah 34 (the release of the slaves broken)
the run's case, never a row.

THE MEASUREMENTS' FINDS (the design's predictions for the rows; every one asserted in the ink): "AT THE END OF SEVEN YEARS" THREE in the Bible — the release,
the assembly (31:10), JEREMIAH 34:14 (the run's case — the verse that quotes this chapter: 15:12's closest kin in the whole Bible by computation, seven of
fifteen tokens in order, closer than Exodus 21:2's three); "release" the noun FIVE tokens, all in this book (15:1, 2, 2, 9; 31:10), the verb's nine (Exodus
23:11's land "let rest"; Uzzah's oxen; Jezebel thrown down); "AND THIS IS THE MANNER OF" — 19:4's manslayer and Solomon's levy the kin; THE CREDITOR'S VERB
thirteen in the Bible (Exodus 22:24 "as a creditor", 24:10-11's pledge, Elisha's widow, Nehemiah's usurers); "proclaim" with liberty — the jubilee's, Isaiah's,
Jeremiah's; "THE FOREIGNER" the book's five (14:21's carcass, this exaction, 17:15's king, 23:21's interest, 29:21's visitor); "your brother" seven tokens;
"THERE SHALL BE NO NEEDY" (15:4) AGAINST "THE NEEDY SHALL NEVER CEASE" (15:11) — three tokens shared in order, the two piskaot 114 and 118 each citing BOTH
verses (the contradiction the shelf reads); "needy" the Torah's nine tokens, six here; "BLESS, HE WILL BLESS YOU" ONE seat (Abraham's "bless, I will bless you"
the form's first); "for an inheritance to possess it" 25:19's twin; "IF YOU DILIGENTLY HEARKEN" — 28:1's blessing header (fourteen of seventeen in order),
Marah's (Exodus 15:26); "which I command you this day" eighteen in the book; "AS HE SPOKE TO YOU" FOUR in the book — 12:20's border, this blessing, 26:18-19,
29:12: THE RECEIPT'S SHAPE WITHOUT THE NAME, and the finder finds NO receipt here (as at 12:20); "YOU SHALL LEND TO MANY NATIONS" — 28:12 THE TWIN with "lend"
(לוה) for "pledge" (עבט), 28:44 the curse's reversal, the pledge-verb SIX in the Bible (this chapter's four); "WITHIN ONE OF YOUR GATES" the formula's first
seat of four (16:5, 17:2, 23:17 ahead) — the parser reads its "one" as [1]; "shut your hand" the verb's ONE seat in the Torah of seven; "harden your heart" —
Sihon's (2:30) the book's other, Zedekiah's the run's; "OPEN, YOU SHALL OPEN YOUR HAND" TWICE (15:8, 15:11), the Psalm's "You open Your hand" the form's other;
"sufficient for his need" — "need" the Torah's ONE seat of thirteen (the Levite's host at Gibeah the run's, Judges 19:20; Proverbs' eight); "BEWARE LEST" at
its sixth seat in the book of nine; "base" the Torah's TWO — 13:14's sons of Belial and this thought; "the year of release" 31:10's twin; "AND IT BE SIN IN
YOU" THREE in the book — the needy's cry, the vow (23:22), THE HIRELING'S CRY (24:15 — seven tokens in order; 279:4 reads them together); "give, you shall
give" — Jephthah's vow the form's other; "your heart grieved" — Elkanah's; "because of this thing" ONE seat; "all that you put your hand to" the book's six,
14:29's blessing the twin; "THEREFORE I COMMAND YOU" FIVE in the book — twice in this chapter ("saying" at 15:11, "this thing today" at 15:15), the refuge, the
sojourner's justice twice; "your poor" — Hagar's "your affliction" the homograph (Genesis 16:11). THE HEBREW SLAVE: "A HEBREW MAN OR A HEBREW WOMAN" —
"Hebrew" Abram's first (Genesis 14:13), Exodus 21:2's slave; "the Hebrew woman" bare ONE seat (Jeremiah's with the vav); "be sold" the Torah's seven niphals
(Leviticus 25's five); "six years" the Torah's four; "FREE" seventeen in the Bible (Exodus 21's four, Jeremiah 34's six, Job's, the Psalm's); "EMPTY" sixteen —
the exodus's spoil "you shall not go out empty" (Exodus 3:21 — 119:4-5's kin), the festivals' "not empty", Jacob's wage, Ruth; "FURNISH, YOU SHALL FURNISH"
— the verb's ONE seat in the Torah (the Psalm's "chain" the homograph), and 15:14 has NO KIN BY COMPUTATION (no verse of the Bible shares two of its tokens);
"your floor and your press" 16:13's Sukkot; "REMEMBER THAT YOU WERE A SLAVE" FIVE in the book — the Sabbath's (5:15 "brought you out", eleven in order), this
("redeemed you" — the chapter's ONE narrative form, a wayyiqtol; the compile's T1 row), 16:12, 24:18 (the closest, fourteen of seventeen), 24:22; "I WILL NOT
GO OUT" — Exodus 21:5's slave loves his master, his wife and his children; THIS ONE LOVES YOU AND YOUR HOUSE because it is well with him (23:17's escaped slave
"where it is good for him" the kin); the first person FOUR — Moses' "I command you" thrice and THE SLAVE'S ONE WORD; "THE AWL" the Bible's TWO seats, the
boring verb Exodus's alone — HERE NO JUDGES, NO DOORPOST, "into the door", ONE token shared in order with Exodus 21:6; "the door" the Torah's four, "the
doorpost" the Passover's and the frontlets' — absent here; "servant for ever" in this form ONE seat; "AND ALSO TO YOUR MAIDSERVANT YOU SHALL DO LIKEWISE" against
Exodus 21:7's "she shall not go out as the menservants do" — what "likewise" reaches the shelf decides (122:8-9); "DOUBLE" the Torah's seven — the manna's,
Joseph's, 17:18's COPY of this law (the same word); "the hire of a hireling" — Malachi's the other seat; Leviticus 25:40-53's sold brother "as a hireling …
YEAR BY YEAR". THE FIRSTLING: "firstling" three tokens here of the book's eight; "YOU SHALL SANCTIFY" against Leviticus 27:26's "NO MAN SHALL SANCTIFY IT" —
the shelf's reconciliation at 124:4; Exodus 13:2's "sanctify to Me", 22:29's seven days with the mother, 34:19's opener of the womb, Numbers 18:17's "you
shall not redeem, they are holy" — the kin by name, none close by computation; "you shall do no work with the firstling of your ox" — 21:3's heifer the twin;
"shear" the Torah's one verb seat outside Genesis (Jacob's and Judah's shearings); "YEAR BY YEAR" (שנה בשנה) the Torah's TWO — the firstling eaten and the
hireling reckoned (Leviticus 25:53; 106:5 the shelf's reading, its third read); THE PLACE FORMULA at its fourth seat in this form, 12:18's clause the closest
(nine of twelve), "you and your household" 14:26's twin, NO Shekhinah in the Aramaic here (the Hebrew has no "to cause His name to dwell"); Numbers 18:18
gives the firstling's flesh to the priest — 125:1's question; "LAME OR BLIND, ANY ILL BLEMISH" — 17:1's "any evil thing" the twin ahead (six in order; 147:3-4
cite them together), the priests' "blind or lame" reversed, Malachi's "lame and sick" the run's; 15:22 IS CHAPTER 12'S CLAUSE — "the unclean and the clean
alike, as the gazelle and as the hart" at its third seat (12:15, 12:22); "pour it on the earth as water" the third seat of chapter 12's formula (12:16 six of
nine), Leviticus 17:13's hunted blood COVERED with dust the contrast (126:5-6). THE REGISTER: THE CHAPTER IS SINGULAR FROM END TO END — no plural "you" in
any verse (chapter 14's food laws were plural), 104 singular morphs, 15:2's creditor-law addressing no one; ONE imperative ("beware", 15:9); EIGHT INFINITIVE
ABSOLUTES (release, bless, hearken, open, lend, give, open, furnish — the shelf's doublings); the consecutive perfects in seven verses; eight verses open on
"when/for", ONE "if" (15:5), one "lest", two "or"; sixteen negations in thirteen verses; no divine frame, "saying" twice, no "so that"; the Name thirteen bare
and three with "to", "the LORD your God" in nine verses, Egypt the one other name — Moses, Israel never named. THE PARSER: FOUR NUMBER VERSES (15:1 [7], 15:12
[6], 15:18 [6] — the starred "years" tokens; 15:7 [1] "one of your brothers … one of your gates") and ONE ORDINAL (15:9 "the seventh" [7]); the kin's numbers
Exodus 21:2's six, 23:10's six, Leviticus 25:8's sevens and forty-nine, Jeremiah's seven and six, the firstling's seven days; NO count line by the finder.
ONKELOS: "the creditor" rendered "THE MASTER OF THE CLAIM", "exact" "claim"; "the foreigner" "a son of the nations" at its four seats; "hearken to the voice"
"receive THE MEMRA" — the Memra's THREE seats in the chapter (15:5, 9, 11); "lend to many nations" the same Aramaic verb at 28:12 (the twin read as one);
"base" "in wickedness" (13:14's sons of Belial rendered by the same word); "sin in you" "guilt" at its four; "A HEBREW MAN OR A HEBREW WOMAN" RENDERED "A SON OF
ISRAEL OR A DAUGHTER OF ISRAEL" (ONE seat in the book); "free" "a son of freedom"; "furnish" "SET APART"; "your house" "the PEOPLE of your house" (the English's
bracket "[the members of]" at 15:16 and 15:20); "servant for ever" "a SERVING servant"; "double" "TWO FOR ONE"; the floor's Aramaic a homograph of Edrei; "as
the gazelle and as the hart" "AS THE FLESH OF"; "blemish" at 15:21 and 17:1 alone; no parenthesis; the English's brackets sixteen in eleven verses. THE STORE
= THE DB (354 = 354; NO KETIV); 189 distinct glosses, 25 already rewritten ("leanness" "only", "and-sever-you" "and-redeemed-you", "like-splendor"
"as-the-gazelle"); THREE "?" GLOSSES — Moses' "I" (אנכי, "I") at 15:5, 11, 15; THE DISPLAY PATCH predicted from the G print at the tail — "remission" (the
release), "fling-down" (release), "debt" (the creditor), "drive" (exact), "the-strange" (the foreigner), "destitute" (needy), "cessation" (howbeit), "pawn"
(lend), "draw-together" (shut), "collar" (furnish), "the-Eberite" (the Hebrew), "exempt" (free), "emptily" (empty), "and-in-something-swinging" (the door),
"repetition" (double), "man-at-wages" (hireling), "cut-off" (shear), "stain" (blemish), "spill-forth" (pour).

THE CLAIMS (seven, DV15-01..07, one manifest; the spine's rows distributed by piska from the CITE INDEX): 01 THE RELEASE (15:1-3 — Onkelos 1-3, Sifrei 111,
112, 113, 109:3; the check "a release" at 15:1); 02 THE NEEDY AND THE BLESSING (15:4-6 — Onkelos 4-6, Sifrei 114, 115, 116:1-3; "no needy" at 15:4); 03 THE
HAND OPENED (15:7-11 — Onkelos 7-11, Sifrei 116:4-18, 117, 118:1-3, 41:3, 279:4, 355:9; "open your hand" at 15:8); 04 THE HEBREW SLAVE (15:12-15 — Onkelos
12-15, Sifrei 118:4-7, 119, 120; "the Hebrew" at 15:12); 05 THE AWL AND THE DOUBLE HIRE (15:16-18 — Onkelos 16-18, Sifrei 121, 122, 123; "the awl" at 15:17);
06 THE FIRSTLING (15:19-20 — Onkelos 19-20, Sifrei 124, 125, 106:5; "the firstling" at 15:19); 07 THE BLEMISH AND THE BLOOD (15:21-23 — Onkelos 21-23, Sifrei
126, 71:6-8, 147:3-4; "a blemish" at 15:21). Seated as seven WITNESS_READ operators at 15:1, 4, 7, 12, 16, 19, 21 with step E. THE FOLD predicted: units 228
-> 229, standing 2252 -> 2259, the hash 8b8fff1fa28953af unmoved (the law layer moves no narrative fact). THE REGISTER GATE at the reading: no receipt, no
header, no footer, no count line in chapter 15 (the finder run — 15:6's "as He spoke to you" not a receipt by its forms, 15:2's "this is the manner" not a
header; the number verses no count lines) — GREEN expected, --strict, DECLARED 98 unmoved.

THE TESTING SHELF routed to 13b's docket (the union rule at the compile): Mishnah Sheviit 10:1-9 with Gittin 36a-37b (the release of debts, Hillel's prozbul,
the release by decree when the jubilee is not; the loan of the seventh year) and Arakhin 32b-33a (the jubilee's link); Makkot 3b (the witnesses in the release);
Rosh Hashanah 8b-9a ("the year of release" and the year's start); Mishnah Kiddushin 1:2-3 with Kiddushin 14b-22b (the Hebrew slave and the Hebrew woman — the
acquisition, the six years, "double the hire of a hireling" 15a, the gift 16b-17b, the awl and the ear that heard at Sinai 22a-b, the maidservant's exemption);
Bava Metzia 31b (the doubled words — "lend, you shall lend", "give, you shall give", "furnish, you shall furnish") and 71a (Exodus 22:24 — the poor of your city
first); Mishnah Peah 8:7-9 with Ketubot 67b (the poor's "sufficient for his need" — even a horse and a servant; the giving with a good heart); Mishnah Bekhorot
1:1-2, 2:6-9, 3:3-4, 4:1-2, 5:1-6, 6:1-12 with Bekhorot 25a-28b (the shearing and the work), 26b-27b (the year "year by year"), 33a-37b (the blemish eaten,
the expert), 53b (the year); Mishnah Temurah 3:5 (the firstling's offspring); Mishnah Arakhin 8:7 (the sanctifying of the firstling — Leviticus 27:26); Sifra
Behar credited from its sitting; the Sifrei's own Mishnah citations read at the rows; every row whole; a docket past ~700 rows its own run.

THE ORDER (RUN B1, B2 and the tail): the 99 spine rows WHOLE in both files piska by piska (ch15_spine_p111.txt … p126.txt) — THE FIRST HALF 111-118 (63 rows)
with Onkelos 15:1-11 and the outside rows 109:3, 41:3, 279:4, 355:9 → ch15_rows_sifrei_111_116.py, ch15_rows_sifrei_117_118.py, ch15_rows_onkelos_a.py
(15:1-11 typed), ch15_rows_outside_a.py → the import check → THE CLEAN COMPACTION POINT UNCONDITIONALLY (the state doc's #206 addendum 1); THE SECOND HALF
119-126 (36 rows) with Onkelos 15:12-23 and the outside rows 106:5, 71:6-8, 147:3-4 → ch15_rows_sifrei_119_123.py, ch15_rows_sifrei_124_126.py,
ch15_rows_onkelos_b.py, ch15_rows_outside_b.py (chapter 14's form; the cuts by consonants SP_) → write_ch15_ledger.py (from the forms' write_ch14_ledger.py — the
prior reads marked REREAD WHOLE: 117:3, 116:18, 41:3, 71:6-8, 106:5, 109:3) → lint 0, coverage computed (the Sifrei 99 + 10; Onkelos 23; the kin's credits by
name) → THE CLEAN COMPACTION POINT (#206 addendum 2) → THE TAIL: ch15_patch_overrides.py (by gloss and by reference from the G print; the anchors sitting 12's
last rows), the ink rerun PATCHED with ch15_ink_body_d.py → write_ch15_manifest.py (seven claims; the check words probed in the store first) → seat_ch15.py
(seven WITNESS_READ at 15:1, 4, 7, 12, 16, 19, 21; step E) → ch15_gates.sh LAUNCHED in the background (ch15_chain.sh: the seat, verify_text, the ritual;
ch15_fold.sh: 229 / 2259 / the hash unmoved; build_world; the journal gate; the register gate --strict; large_letter_probes; the home-path gate) with
write_ch15_records.py and copy_ch15_forms.py written first → the summary read once → the records from the sheet in one call → the forms copied → the commit
message → the timing table → the report.
'''
assert SEC.count('\n## ') == 1 and 'DV15' in SEC
open(M, 'a', encoding='utf-8').write(SEC)
t2 = open(M, encoding='utf-8').read(); assert t2.endswith(SEC) and t2.count('## Sitting 13 — CHAPTER 15') == 1
print('THE DESIGN appended:', len(SEC), 'bytes; the map', len(t2), 'bytes; asserts', NA, 'first pass fails', F1, 'second', F2)
r = subprocess.run(['python3', f'{ROOT}/logic/solo_tools/gloss_lint.py', M], capture_output=True, text=True); print('lint:', r.stdout.strip().split('\n')[-1]); assert r.returncode == 0, r.stdout[-800:]
