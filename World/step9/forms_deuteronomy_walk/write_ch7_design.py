#!/usr/bin/env python3
# THE DEUTERONOMY WALK sitting 5 — CHAPTER 7, RUN 1 of four CLOSED (2026-09-17/18): the design appended to the map, THE INSTALL HYPOTHESIS recorded on the table
# (the owner: "yes record it", 2026-09-18), the state doc's COMPACTION POINT #194, the recovery page's sections 2 and 6, the memory note and the index line.
# Every text built first; the caps asserted before any file is opened. write_ch6_design.py's form.
import os, re, subprocess
ROOT = subprocess.check_output(['git', 'rev-parse', '--show-toplevel'], text=True).strip()
SP = os.path.dirname(os.path.abspath(__file__))
MEM = os.path.expanduser('~/.claude/projects/-Users-Shared-TorahSim/memory')
def read(p): return open(p, encoding='utf-8').read()
NASSERT = sum(1 for l in read(f'{SP}/ch7_ink.py').split('\n') if l.startswith('assert'))
assert read(f'{SP}/ch7_ink_run2.out').startswith('0 failing statements') and '7 failing statements' in read(f'{SP}/ch7_ink_run1.out')
DESIGN = f'''

## Sitting 5 — CHAPTER 7, Deuteronomy 7:1-26 (2026-09-17; the owner: "Go" after 4b's commit 64a8362): the reading and the unit — THE DESIGN, written at the close of RUN 1 of four

THE FOUR RUNS: RUN 1 the rereads (the recovery page, the map's "Sitting 4" design and AS BUILT as the reading's form, the tail sections — the whole-row rule and its
fix — and the memory), the measurements (ch7_dump0.py DERIVED from ch6_dump0.py by twenty-two asserted substitutions; ch7_measure1.py), the ink (ch7_ink.py —
{NASSERT} asserts, seven fell on the first pass, all forms and none facts, 0 on the second) and this design — CLOSED HERE, a clean compaction point (#194); RUN 2 the
rereads THE_STEPS Step 2 + Step 5's head + the compiler block, then the rows — the three outside rows WHOLE (ch7_sifrei_outside.txt, 4 KB) and the twenty-six Onkelos
rows WHOLE (ch7_onkelos.txt, read at run 1) under the whole-row rule — ch7_rows_onkelos_a/b.py and ch7_rows_outside.py on sitting 4's forms, write_ch7_ledger.py from
write_ch6_ledger.py by sed (lint 0; coverage computed); RUN 3 the display layer's patch (49 rewrites by gloss, 36 by reference), the manifest (six claims), the seat,
the chain (the ritual), the fold predicted and matched, build_world, the journal gate, the register gate --strict, the home-path gate; RUN 4 the records from the
sheet in one call, the forms copied, this section's AS BUILT, the compaction point.

THE DRAFT: deu_07_nations_cherem 7:1-26 — 26 of 26 verses, missing 0 (computed from the DB's verse table), depends_on deu_06_shema, 33 scenarios, 30 comment lines, no
operators, no step E; the next draft deu_08_manna_humility opens at 8:1 (8:1-20; depends_on this unit and the manna's); the step ids STEP_Dt_7_<v>. THE CHAPTER THE
UNIT, per the ruling — THE PORTION'S EDGE SITS INSIDE IT: 7:12 opens the next portion (176 tokens before the edge, 236 after); the chapter is read whole. ONE ledger:
logic/oral_triage/deu_07_vaetchanan_ekev_2026-09-17.md; the claims' prefix DV07 (absent everywhere, asserted).

THE TWO DIVISIONS AGREE: the export's chapter 7 twenty-six rows, the DB's twenty-six verses; the alignment instrument gives the identity at cost 20; chapter 5 the
book's ONE split (asserted on all thirty-four).

THE SHELF, BY POSITION — THE SPINE IS SILENT ON THE CHAPTER (chapter 4's form): no piska heads in chapter 7 — 36 on 6:9 before it, 37 on 11:10 after (the Sifrei reads
nothing between the Shema's last verse and 11:10: chapters 7, 8, 9, 10 and 11:1-9 have no section). THE OUTSIDE ROWS by the union of both files: THREE — 37:1 (the first
row of the next portion's first piska, on 11:10: the English's own "(Dt.7:12)" names the portion's opening verse and its footnote says the Sifrei does not expound it;
the Hebrew cites 11:10 alone — READ and marked an INTERPOLATION, chapter 6's 104:8 the form), 50:4 on 11:23 (citing 7:1 "seven nations greater and mightier than
you": even ONE of the seven greater and harsher than all Israel — Amos 2:9 the Amorite tall as cedars), 61:7 on 12:3 (citing 7:26 "utterly detest it, utterly abhor
it": R. Eliezer — the Asherah uprooted; R. Akiva — "destroy their name" means the shrines' names CHANGED FOR THE WORSE, never for the better; the English's note to
Tosefta Avodah Zarah 6:4 — "the Face of God" to "Dog-Face"). No slip (no cited verse beyond 26). None of the three read before; 294 strict Sifrei rows anywhere. NO
Onkelos row of chapter 7 in any ledger. THE KIN'S SPINE READ ALREADY, to be CREDITED by name at the ledger: Exodus 23:20-33 (the angel's clauses — no covenant, the
hornet, little by little, a snare; exo_23_escort_land: eight Onkelos rows on 23:21-33; the Mekhilta rows on Exodus 23 and 34 twenty-one over the ledgers), Exodus 34:11-16
(the renewed covenant — the six nations, no covenant, the altars, the daughters; exo_34_second_tablets; the erection docket's Mishnah Avodah Zarah 3:5 on 7:25's silver
and gold, and 3:6, 3:10, 4:2 — the compile's CREDITS), Numbers 33:50-56 (the dispossession, the figured stones, "thorns in your eyes"; num_33_journeys: seven Onkelos
rows). Six ledgers NAME a verse of chapter 7 (the erection docket 7:3-5 and 7:25-26; the nazirite's 7:21; the dues' 7:1; the conquest's 7:2; the journeys' 7:5; the
refuge cities' 7:12).

THE INK, COMPUTED (ch7_dump0.py, ch7_measure1.py; the asserts typed from the print — SEVEN fell on the first pass, all forms: a count typed as twelve where the print
said eleven, a token's variants summed short, a gloss already rewritten at chapter 6 ("in your midst"), the Aramaic row's length; each retyped from the print, none
after):
- THE PARSER MEASURED FIRST: TWO number verses in 26 — 7:1 "SEVEN NATIONS" [7] WITH THE VERSE'S OWN WITNESS: seven gentilic tokens (the Hittite, the Girgashite, the
  Amorite, the Canaanite, the Perizzite, the Hivite, the Jebusite) beside the numeral; the Bible's seven-name lists THREE (7:1; Joshua 3:10, 24:11 — with the Girgashite,
  whose seven seats are Genesis 10 and 15, this verse, Joshua's two, Nehemiah 9:8, 1 Chronicles 1), the six-name lists ELEVEN (Exodus 3:8, 3:17, 23:23, 33:2, 34:11;
  20:17; Joshua 9:1, 11:3, 12:8; Judges 3:5; Nehemiah 9:8) — 7:1 ALONE COUNTS ITS LIST, and the shelf reads the count (50:4); 7:9 "to a thousand generations" [1000]
  (1 Chronicles 16:15 and Psalm 105:8 the same reading; "to thousands" of the ten words — Exodus 20:6, 5:10, 34:7 — NO number, the bare plural, the 1b rule); THE
  SEVEN-STEM HOMOGRAPH "THE OATH" (7:8, the lemma 7621) STARRED — the noun's ten Torah seats (Genesis 26:3 "the oath", Exodus 22:10 "the oath of the LORD", the vows'
  chapter); "swore" (7:8, 12, 13) not a number at all; no ordinal; NO GAP. The tokens 412, the letters 1,637.
- THE STORE = THE DB at every verse but 7:9: the store carries the written מצותו ("His commandments", the ketiv — no yod) AND the read מצותיו (the qere, with the yod) —
  THE CHAPTER'S ONE WRITTEN/READ PAIR, the same written form as 5:10's (there the read form is Exodus 20:6's "MY commandments"; the DB's 1,268 ketiv tokens over the
  Bible); no large letter in the chapter; the one unglossed token "I" (7:11).
- THE KIN DIFFED (the DB's tokens): 7:1-2 against Exodus 23:23, 23:32 and 34:11-15 — SIX names there, SEVEN here; "you shall not make a covenant with them" 7:2 and
  23:32 the two seats ("lest you make" 34:12, 15); "nor show them favor" ONE; 7:3 against 34:16 — the daughters TAKEN there (one direction), BOTH directions barred
  here ("you shall not intermarry" the Torah's one seat of the verb; Shechem's offer Genesis 34:9 the kin); 7:5 against 34:13 and 12:3 — the FOUR objects (altars,
  pillars, Asherim, images; 12:3 adds "destroy their name"); 7:6 against 14:2 (a letter and a word apart) and Exodus 19:5-6 ("treasure … holy"); 7:7-8 against 4:37
  and 10:15 (the fathers loved, the seed chosen), 6:21 and Exodus 13:14 (the strong hand — the son's answer), 13:6 (the enticer's "who redeemed you"); 7:9 against
  Exodus 20:6 and 5:10 — ONE token shared with 20:6 ("and those who keep"), TWO with 5:10 (the ketiv "His commandments" in both); 7:10 against Exodus 34:7 and 20:5 —
  the fathers' iniquity VISITED there, the hater REPAID TO HIS OWN FACE here; 7:11 against 6:1 and 5:31 — the triad's third seat (5:31, 6:1, 7:11 in that order); 7:13
  against 28:4, 11, 18, 51 (the blessings' and the curses' fruit, increase and young), 11:14 (grain, wine, oil), 30:9; 7:14 against Exodus 23:26 (barren); 7:15 against
  Exodus 15:26, 23:25, 28:60 (the diseases of Egypt); 7:16 against Exodus 23:33 ("serve their gods … a snare" shared) and 13:9, 19:13 (the eye's pity); 7:17-18 against
  1:28-29, 9:1, 20:1, 20:3 (the fear of the nations — "you shall not fear them" 7:18 and 20:1); 7:19 against 4:34, 29:2 ("great which your eyes saw" shared), 26:8, 6:22
  (the trials, signs, wonders, hand, arm); 7:20 against Exodus 23:28 and Joshua 24:12 (THE HORNET'S three seats — the town Zorah the homograph); 7:21 against 6:15
  ("the LORD your God in your midst" — the two seats and Zephaniah), 10:17, 1:29, 31:6; 7:22-23 against Exodus 23:27-30 ("LITTLE BY LITTLE" — the two seats; the
  beasts of the field; the confusion); 7:24 against Joshua 1:5 ("no man shall stand" — the two seats), 9:14, 25:19, 29:19, Exodus 17:14 (the name from under heaven —
  Amalek, the calf, the curse); 7:25 against 7:5, 12:3, Exodus 20:17 and 5:21 — "YOU SHALL NOT COVET" THE TENTH WORD'S VERB on the idols' silver and gold, the phrase's
  two seats (Achan's "I coveted them and took them", Joshua 7:21, the kin), 27:15; 7:26 against 13:18 (the devoted thing), Joshua 6:18, 7:12, Leviticus 11:43 (the
  detesting verb Leviticus 11's), 23:8 ("you shall not abhor an Edomite … an Egyptian" — the abhorring verb's other seat), 27:28.
- THE PHRASE CENSUSES (the crowns): "seven nations" ONE seat; "greater and mightier than you" three, all this book's; "you shall utterly destroy" 7:2 and 20:17; "holy
  people" five, four this book's; "treasure" six (Exodus 19:5 the first); "chose you" ONE; "the fewest of all peoples" ONE; "set His love" eight (10:15 the fathers;
  21:11 the captive woman); "the oath which He swore to your fathers" ONE; "redeemed you from the house of bondage" ONE (the verb's six Deuteronomy seats); "THE
  FAITHFUL GOD" ONE; "the LORD your God, He is God" six (4:35, 39; 7:9; Solomon, Elijah, Manasseh); "keeps the covenant and the kindness" four (7:9; Solomon's prayer,
  Daniel's) and 7:12 the pair again; "to a thousand generations" three; "and repays those who hate Him to their face" ONE; "He will not delay" 7:10 and Habakkuk; the
  triad "the commandment, the statutes and the judgments" 5:31, 6:1, 7:11; "because you hear" ONE — "because" the noun "heel" read as a conjunction (7:12, 8:20,
  Genesis 22:18, 26:5, Numbers 14:24); "the fruit of your womb and the fruit of your ground" 7:13, 28:4, 28:18; "the increase of your cattle and the young of your
  flock" 7:13 and 28:51 — THE FLOCK'S "YOUNG" TAGGED A NAME in the DB's morph at its four seats (the goddess's homograph); "barren" five Torah (Sarah, Rebekah,
  Rachel; Exodus 23:26); "the diseases of Egypt" 7:15 and 28:60; "your eye shall not pity" five, all this book's; "a snare" four Torah; "if you say in your heart" ONE;
  "surely remember" ONE (the infinitive absolute 7:18 and Jeremiah 31:20); "the great trials" ONE ("trials" 4:34, 7:19; 16:10's "measure" the homograph); "the signs
  and the wonders" five; "the hornet" Exodus 23:28, 7:20, Joshua 24:12; "those who hide" ONE; "a great and awesome God" ONE; "little by little" 7:22 and Exodus 23:30;
  "great confusion" ONE; "destroy their name from under heaven" ONE; "no man shall stand before you" 7:24 and Joshua 1:5; "YOU SHALL NOT COVET" 7:25 and Exodus 20:17;
  "an abomination to the LORD your God" five and "abomination to the LORD" eight, all this book's — "abomination" thirteen Deuteronomy seats, 7:25-26 the first two;
  "you shall not bring an abomination into your house", "devoted like it", "utterly detest, utterly abhor", "for it is devoted" ONE each.
- THE FRAMES AND THE REGISTER: NO divine frame, NO "saying" — the whole chapter Moses' voice; the narrative verbs TWO, both God's past acts inside the reason (7:7 "and
  He chose", 7:8 "and He redeemed you"); NO imperative; FIVE INFINITIVE ABSOLUTES ("utterly destroy" 7:2, "surely remember" 7:18, "utterly detest … utterly abhor"
  7:26 — and "quickly" 7:4, 22 in the adverb's form); the law's form the consecutive perfect in fourteen verses; SIXTEEN PROHIBITIONS — eleven in the second person
  (7:2 two, 7:3 three, 7:16, 18, 21, 22, 25, 26), five in the third (7:10 "He will not delay", 14 "there shall not be a barren", 15 "He will not put", 16 "your eye
  shall not pity", 24 "no man shall stand"); the second person SINGULAR in nineteen verses, PLURAL in two (7:5 the altars, 7:7 the fewest), BOTH in four (7:4, 8, 12,
  25 — "you shall burn" plural inside a singular verse), NEITHER in 7:10; the first person God's (7:4 "from after Me", 7:11 "I command") and the doubter's (7:17 "than I …
  how can I"); "for/when" twelve seats, "lest" two (22, 25), "but rather" once (7:5) — no "if", no "or"; the Name twenty; "the LORD your God" fourteen, singular only;
  Moses and Israel never named; Egypt and Pharaoh at 8, 15, 18.
- ONKELOS (the renderings' seats over the book): 7:2 "utterly destroy" MADE "utterly ANNIHILATE" (7:2 and 20:17 — the ban's two seats), "nor show them favor" MADE
  "have no MERCY on them" (7:2, 13:9 the enticer); 7:4 "from after Me" MADE "from after MY SERVICE", "other gods" MADE "the IDOLS of the peoples" (eight); 7:5 "their
  altars" the idolaters' word (7:5, 12:3), "their graven images" MADE "the images of their idols" (7:5, 7:25, 12:3); 7:6 "a treasured people" MADE "a BELOVED people"
  (7:6, 14:2, 26:18); 7:7 "set His love" MADE "desired" (7:7, 10:15); 7:8 "the oath which He swore" MADE "the COVENANT which He established" — the oath's noun and verb
  both the covenant's word; 7:9 "the faithful God" (7:9, 32:4), "TO A THOUSAND GENERATIONS" MADE "TO THOUSANDS OF GENERATIONS" — the ten words' plural, at 5:10 and
  7:9 alone; 7:10 THE SUPPLIED DOCTRINE — "He repays those who hate Him THE GOOD THEY DO BEFORE HIM IN THEIR LIFETIME, to destroy them; He does not delay THE GOOD
  DEED of those who hate Him …": twelve tokens made twenty-two, the six bracketed supplements of the English (seventeen brackets over ten verses in the chapter);
  7:12 "because" MADE "IN EXCHANGE FOR" (Caleb's 1:36 the first of eight); 7:13 the cattle's increase and the flock's young MADE "the herds of your oxen and the
  flocks of your sheep" (7:13, 28:4, 18, 51); 7:15 "diseases" MADE "plagues" (7:15, 28:60, 32:23); 7:16 "consume" MADE "finish off", "a snare" MADE "a stumbling-block"
  (one); 7:19 "THE TRIALS" MADE "THE MIRACLES" (4:34, 7:19, 16:1 — the trial's word for the wonder; 6:16's Massah "the trial" another word); 7:20 "the hornet" ONE;
  7:21 "in your midst" MADE "HIS SHEKHINAH IS AMONG YOU" (6:15, 7:21 — the pair); 7:22 "little by little" ONE; 7:23 "confusion" ONE; 7:24 "no man shall stand" (7:24,
  11:25); 7:25 "an abomination to the LORD" MADE "a thing DISTANCED before the LORD" (7:25, 24:4, 27:15), 7:26 "devoted" the same word (7:26, 13:18), "detest … abhor"
  MADE "detest … keep far" — the abhorring verb the distancing's; no parenthesised variant in the chapter's Hebrew rows; the English keeps two transliterations
  ("tzir'oh" the hornet, "cheirem" the devoted thing).
- THE DISPLAY LAYER (run 3): 49 rewrites BY GLOSS ("seclude" → "ban", "try" → "choose", "wealth" → "treasure", "the-something-sworn" → "the-oath", "the-build-up" →
  "the-faithful", "fetus" → "the-increase-of", "and-'Ashtᵉrah" → "and-the-young-of", "the-wasp" → "the-hornet", "physical--a-net" → "devoted", "be-filthy" →
  "detest", "the-testing" → "the-trials" …) and 36 BY REFERENCE ("nations" and "the-peoples" for the store's singulars; "I" at 7:11; "because" for "heel"; "set-his-love"
  for "cling"; "the-fewest"; "but rather thus" at 7:5; "the-anger" for "nose" …); six of the chapter's families already rewritten at sittings 1-4 ("other", "covet",
  "like-it", "destroyed-them", "and-destroy-you", "in-your-midst").

THE CLAIMS PLANNED (write_ch7_manifest.py, run 3): SIX — DV07-01 7:1-5 the seven nations (the ban; no covenant, no favor, no marriage; the altars); DV07-02 7:6-8 the
holy people chosen for love and for the oath, not for number; DV07-03 7:9-11 the faithful God — covenant and kindness to a thousand generations, the hater repaid to
his face, keep the commandment; DV07-04 7:12-16 because you hear — love, blessing, fruit, no barrenness, no disease; consume the peoples, no pity, no serving their
gods; DV07-05 7:17-24 do not fear — remember Pharaoh, the trials, the hornet, little by little, the kings, their name; DV07-06 7:25-26 the images burned, the silver
and gold not coveted, no abomination into the house, devoted — each check the block's longest store-piece whole (7:9's "His commandments" NOT a check — the store's two
tokens). THE FOLD PREDICTED: units 221, standing 2203 + 6 = 2209, hash unmoved (the tripwire's literals set before the bake). THE SEATS: six WITNESS_READ operators at
7:1, 6, 9, 12, 17, 25, step E. THE REGISTER GATE: no seat in the chapter (no receipt form; "swore to your fathers" 7:8, 12, 13 the compile's citations) — GREEN
unchanged (DECLARED 100). THE LEDGER PREDICTED: Onkelos 26 rows; the Sifrei 3 outside rows FRESH (37:1 marked an interpolation); the kin's rows CREDITED by name (the
Exodus 23 and 34 ledgers, the Numbers 33 ledger, the erection docket); coverage COMPUTED at the writing.

OWED TO THE COMPILE (sitting 5b; the box in COMPILE_DEBT.md at run 4): THE BAN (7:2 with 20:16-18 — the seven nations' cell; the Sifrei's war sections at chapter 20),
NO COVENANT AND NO FAVOR (7:2 — Avodah Zarah 20a's readings of "show them no favor": no settlement, no gift, no praise), NO MARRIAGE (7:3-4 — "for he will turn your
son": the child of a gentile mother follows her, Kiddushin 68b; Mishnah Kiddushin 3:12 CREDITED at the erection docket; Yevamot 23a; Avodah Zarah 36b), THE ALTARS AND
THE ASHERIM (7:5 with 12:3 — Mishnah Avodah Zarah 3:5-10 CREDITED; Avodah Zarah 45b-48b), THE CHOSEN PEOPLE (7:6-8 — Chullin 89a "not because you were more … but
because you humble yourselves"), THE FAITHFUL GOD AND THE HATER REPAID (7:9-10 — Onkelos's doctrine of the wicked paid in this world; the thousand generations),
"BECAUSE YOU HEAR" (7:12), THE BLESSINGS (7:13-15 — no barrenness, the diseases of Egypt), NO PITY AND NO SERVING (7:16), DO NOT FEAR (7:17-21 — Sotah 36a's hornet on
the Jordan's bank), LITTLE BY LITTLE (7:22 — Exodus 23:29-30 the first telling, by CALL), THE IDOLS' SILVER AND GOLD (7:25 — Mishnah Avodah Zarah 3:5 CREDITED, 4:4-5
the nullification; Avodah Zarah 44b-52a; "you shall not covet" the tenth word's verb — 3b's coveting cell by CALL), THE ABOMINATION INTO THE HOUSE (7:26 — Makkot 22a
the lashes; Mishnah Avodah Zarah 3:3; the devoted like it), the docket by the union rule (the scan will name the tractates; the topic ranges expected: Avodah Zarah
20a, 36b, 42a-54b; Kiddushin 68b; Yevamot 23a; Sotah 35b-36a; Chullin 89a; Makkot 22a; Mishnah Avodah Zarah 1-4; Kiddushin 3:12). NOTHING ELSE IN CHAPTER 7 IS OWED TO
A LATER SITTING OF ITS OWN.

⚠ LESSONS (run 1): A CHAPTER WITHOUT A SPINE READS ITS KIN'S SPINE BY CREDIT — the Exodus and Numbers ledgers hold the angel's clauses and the dispossession; the three
outside rows are the Sifrei's whole voice on the chapter. THE TRANSLATOR'S PARENTHESIS AGAIN — 37:1's "(Dt.7:12)" names the portion's opening the Sifrei skips: read and
marked, never counted as the Sifrei's citation. A NUMBER VERSE CAN CARRY ITS OWN WITNESS — 7:1's seven gentilic tokens beside "seven": the count is checkable from the
ink alone, and the shelf reads the count (50:4). THE WRITTEN/READ PAIR IS THE STORE'S EXTRA TOKEN — 7:9 as 5:10: the store carries both forms, the DB the written one
marked; the mismatch census names the seat. THE FIRST TYPED PASS FELL SEVEN WAYS ON FORMS — a token's variants summed short, a count typed from memory, a gloss already
rewritten at chapter 6: the print first, then the assert. A DERIVATION BY ASSERTED SUBSTITUTIONS — ch7_dump0.py from ch6_dump0.py by twenty-two named replacements,
each asserted present; the forms copy kept the git-root line, so the derivation's header check is conditional. A PORTION'S EDGE INSIDE A CHAPTER — 7:12 opens the next
portion; the chapter is the unit per the ruling; the token split recorded.

THE ORDER (RUN 2, the first step): reread THE_STEPS Step 2 + Step 5's head + the compiler block; the three outside rows WHOLE (ch7_sifrei_outside.txt) and the twenty-six
Onkelos rows WHOLE (ch7_onkelos.txt) → ch7_rows_onkelos_a.py (7:1-13), ch7_rows_onkelos_b.py (7:14-26), ch7_rows_outside.py (sitting 4's ch6_rows_*.py the forms; the
cuts by consonants — HP / AP / SP_) → write_ch7_ledger.py (from write_ch6_ledger.py) → lint 0, coverage computed (Onkelos 26; the Sifrei 3; the kin's credits by name)
→ the state doc's checkpoint (RUN 2's close, a clean point).

## THE INSTALL HYPOTHESIS — DEUTERONOMY AS THE PROGRAM'S INSTALL (ON THE TABLE, not a ruling; recorded 2026-09-18 on the owner's "yes record it", after his question
## "do you think deuteronomy is a run instruction. why else does it alter old code then create new code?")

THE READING OFFERED: not the run itself but THE INSTALL — the program read back to the generation that will execute it, re-declared for the environment it will run in,
patched where that environment needs it, and written onto the runtime; THE RUN IS JOSHUA (the crossing). Why the book alters old code and then adds new: the target
changed — the first four books are the specification written for a camp under a cloud; Deuteronomy is the same program prepared for the land.

THE EVIDENCE ALREADY MEASURED BY THE WALK (nothing of it typed for the hypothesis; each is a record of sittings 1-5): (1) IT READS THE LOG BACK before it does anything —
the readback's first form, chapters 1-4: forty-two rows and eleven rows of the retelling graded against the tape, the acts told nowhere else written once at their own
day; (2) IT RE-DECLARES THE CODE FOR THE NEW AUDIENCE — chapter 5's ten words with receipts INSIDE them ("as the LORD your God commanded you": the code citing its own
prior giving — the register gate's CHAPTER class), the Sabbath's ground moved from the creation to Egypt (from the designer's ground to the audience's own history),
"that it may go well with you" added; (3) IT PATCHES WHAT THE LAND NEEDS — the cities of refuge east (4:41-43) with the west owed; ahead: the one place, the king, the
courts, the prophet, the war laws; (4) IT WRITES THE PROGRAM ONTO THE RUNTIME — chapter 6 as an install script: on the heart (memory), on the hand and between the eyes
(the person), on the doorposts and the gates (the house), taught to the sons (replication), recited lying down and rising (a heartbeat); the two lines given at the
chapter's own day, STATUTE by form, no marker back to Sinai; (5) THE REGISTRY ALREADY SAYS SO — the book's three daemons (law_opening_speech, law_obey_horeb,
law_hear_o_israel) are installed_by BOOT, not by an act on the tape; (6) THE RECEIPT WITHOUT THE NAME (6:25 "as He commanded us") — the install verifying itself against
the spec in the first person plural; (7) chapter 7's first measurement: the code re-declared with the target's names (SEVEN nations where Exodus had six; both
directions of marriage where Exodus 34:16 barred one; four objects where 34:13 had three; "you shall not covet" moved from the neighbor's house to the idols' silver
and gold).

WHAT WOULD TEST IT (the chapters ahead; nothing of the engine is touched now): the stones at the crossing (27:2-8 — the code copied onto the target), the blessings and
the curses (27:11-28:68 — the exit codes), the covenant at Moab (29 — the install's own covenant, distinct from Horeb's, 28:69), the reading every seven years (31:10-13 —
the reload), the song as a witness (31:19-22, 32), the handoff to Joshua (31:7-8, 23; 34:9), Moses' death outside the target (34). If those compile as install steps
rather than as law cells — writes on the world's own configuration rather than on Israel's ledger — the picture holds; if they compile as ordinary law and narrative,
it falls. THE MACHINE'S OWN CLASSES bear on it: the register gate's headers (4:45 "these are the testimonies" — DAEMONS), the daemons' installed_by field (boot / by an
act), THE LOOP's port (the run's inputs) and its second pass; a class for install steps beside the law cells would be the hypothesis's first engine change, and it is
NOT made until the owner's word after the evidence.

BESIDE IT ON THE TABLE: the Decalogue as a SCHEMA over the laws (the state doc's #185 addendum 1; ARCHITECTURE/THE_TEN_AS_A_SCHEMA.md). The two questions may be one:
a schema is what an install declares. The walk continues in order; neither is a ruling.
'''
STATE = f'''

═══ COMPACTION POINT #194 (2026-09-18 — after THE DEUTERONOMY WALK sitting 5's RUN 1 (chapter 7: the measurements, the ink, the design) and THE INSTALL HYPOTHESIS recorded on the table; the owner: "get ready to compact", then "yes record it") ═══
THE STATE: chapters 1-6 READ, FROZEN, COMPILED AND ON THE TAPE — COMMITTED 64a8362 AND PUSHED (2026-09-17; 4b whole, the whole-row rule and its fix); CHAPTER 7's READING at RUN 1 of four, CLOSED: the rereads; ch7_dump0.py (derived from ch6_dump0.py by twenty-two asserted substitutions) → ch7_dump0.out; ch7_measure1.py → ch7_measure1.out (675 lines, read whole in four pages); ch7_ink.py — {NASSERT} asserts, seven fell on the first pass (forms), 0 on the second; THE DESIGN in the map ("Sitting 5 — CHAPTER 7 … THE DESIGN"): the two divisions the identity (26 = 26, cost 20); the spine SILENT on the chapter (no piska head; 36 on 6:9, 37 on 11:10) — three outside rows (37:1 the translator's "(Dt.7:12)" an interpolation; 50:4 on 11:23; 61:7 on 12:3), none read before; the kin's spine read at the Exodus and Numbers sittings (to be credited by name); the parser TWO number verses — 7:1 "seven nations" [7] with seven gentilic tokens as the verse's own witness, 7:9 "a thousand generations" [1000]; "the oath" (7:8) starred; THE STORE'S EXTRA TOKEN at 7:9 — the chapter's one written/read pair ("His commandments" written without the yod, read with it; 5:10's kin); 412 tokens; NO divine frame, no "saying", two narrative verbs (7:7, 7:8), five infinitive absolutes, sixteen prohibitions, plural at 7:5 and 7:7 only; Onkelos's supplied doctrine at 7:10 (twelve tokens made twenty-two), "to thousands of generations" at 7:9 = 5:10; the display layer planned (49 by gloss, 36 by reference); six claims planned, the fold predicted (221 / 2209 / the hash unmoved); the register gate no seat. THE INSTALL HYPOTHESIS recorded in the map's tail (ON THE TABLE, not a ruling): Deuteronomy as the program's INSTALL, the run Joshua — the evidence the walk has measured, the tests ahead (27, 28, 29, 31, 34), no engine change until the owner's word. THE TUTORIAL: ARCHITECTURE/DEUTERONOMY_SO_FAR.md (32 KB, thirteen sections) with its epub, on the owner's "write a markdown tutorial" (2026-09-17). The corpus unmoved (220 units, standing 2203, hash 8b8fff1fa28953af); the tape unmoved since 4b (RUN (1304, 96, 88, 0, 12, 1595, 37, 319, the four pairs, 127), markers 167, closes 127). NO GATE RUN THIS RUN (no file of the engine touched; the ledger not yet written); the two probes retyped at 4b's run 4 are committed.
THE TREE (uncommitted since 64a8362): the state doc (the commit's line, this block), the recovery page, the map (the design, the hypothesis), ARCHITECTURE/DEUTERONOMY_SO_FAR.md and .epub; the memory (outside the repo). ⚠ THE SCRATCHPAD holds run 1's scripts and prints, NOT yet in the forms folder (copied at run 4): derive_ch7_dump0.py, ch7_dump0.py/.out, ch7_measure1.py/.out, ch7_ink.py, ch7_ink_run1.out, ch7_ink_run2.out, ch7_onkelos.txt (36 KB, read), ch7_sifrei_outside.txt (4 KB, read), ch7_store_glosses.txt, write_ch7_design.py; assert_driver.py (the forms' copy exists).
THE WORD FOR THE NEXT SITTING — RUN 2 OF CHAPTER 7 ON THE OWNER'S WORD, its first step: reread THE_STEPS Step 2 + Step 5's head + the compiler block (the post-compaction rule's reread before a ledger); then the rows WHOLE (the whole-row rule): the three outside rows (ch7_sifrei_outside.txt) and the twenty-six Onkelos rows (ch7_onkelos.txt) → ch7_rows_onkelos_a.py (7:1-13), ch7_rows_onkelos_b.py (7:14-26), ch7_rows_outside.py from the forms' ch6_rows_onkelos_a/b.py and ch6_rows_outside.py by sed (the cuts by consonants — HP / AP / SP_ from ch7_ink.py, which the row scripts exec; the verdicts MATERIAL / CONTEXT; the kin's rows CREDITED by name — exo_23_escort_land, exo_34_second_tablets, num_33_journeys, the erection docket), write_ch7_ledger.py from the forms' write_ch6_ledger.py by sed (OUT = logic/oral_triage/deu_07_vaetchanan_ekev_2026-09-17.md — the name in ch7_ink.py; the TITLE there; coverage computed: missing 0, extra 0 on both files' row counts; lint 0); then the checkpoint (#194 addendum 1, RUN 2's close). Run 3 and run 4 as the design's THE FOUR RUNS paragraph names them (the display layer 49 + 36 under the marker "THE DEUTERONOMY WALK sitting 5 (2026-09-17, Deuteronomy 7)"; the manifest's six claims DV07-01..06; the seat at 7:1, 6, 9, 12, 17, 25; the ritual; the fold 221 / 2209; the records; the forms; the commit message for his word).
POST-COMPACTION REREADS (the rule): the recovery page; the map's NEWEST sections — "Sitting 5 — CHAPTER 7 … THE DESIGN" (its THE ORDER paragraph names the step) and "THE INSTALL HYPOTHESIS"; MEMORY.md. Nothing else unasked; THE_STEPS' three blocks at run 2's first step.
'''
MEM_PARA = '''

SITTING 5 — CHAPTER 7 (7:1-26, the seven nations) OPENED 2026-09-17 on "Go" after 4b's commit. RUN 1 DONE 2026-09-18 (the rereads, the measurements — ch7_dump0.py derived by asserted substitutions, ch7_measure1.py — the ink 119 asserts / 0 fails on the second pass, the design in the map "Sitting 5 — … THE DESIGN"; the state doc #194 — a clean compaction point). The finds: the Sifrei has NO section on chapter 7 (three outside rows; the kin's spine — Exodus 23:20-33, 34:11-16, Numbers 33:50-56 — read at earlier sittings, credited by name); the parser reads 7:1's "seven nations" [7] with the verse's seven gentilic tokens as its own witness and 7:9's "a thousand generations" [1000]; the store carries a written AND a read form at 7:9 (the chapter's one pair, 5:10's kin); Onkelos doubles 7:10 with the doctrine of the wicked repaid in this world; "you shall not covet" (7:25) is the tenth word's verb on the idols' silver and gold. THE INSTALL HYPOTHESIS recorded ON THE TABLE (the map's tail; the owner's "yes record it" 2026-09-18): Deuteronomy as the program's INSTALL (the run Joshua) — the evidence measured, the tests at chapters 27-34, no engine change without his word. THE TUTORIAL ARCHITECTURE/DEUTERONOMY_SO_FAR.md written on his word (2026-09-17). NEXT: RUN 2 — THE_STEPS Step 2 + Step 5's head + the compiler block reread, then the three outside rows and the twenty-six Onkelos rows WHOLE, the row scripts, write_ch7_ledger.py (the scratchpad's ch7_* files; the map's THE ORDER paragraph). Uncommitted since 64a8362.
'''
plans = []
P = f'{ROOT}/World/step9/DEUTERONOMY_WALK.md'; s = read(P); assert 'Sitting 5 — CHAPTER 7' not in s and 'THE INSTALL HYPOTHESIS' not in s; plans.append((P, s.rstrip('\n') + DESIGN))
P = f'{ROOT}/logic/pre_logic_methods_2026-07-28/PROMPT_continue_solo_era_2026-08-06.md'; s = read(P); assert 'COMPACTION POINT #194' not in s; plans.append((P, s.rstrip('\n') + STATE))
P = f'{ROOT}/logic/pre_logic_methods_2026-07-28/RECOVERY_new_thread_2026-09-12.md'; s = read(P)
i = s.index('## 2. WHERE IT STANDS'); j = s.index('## 3. THE STANDING LAWS')
sec2 = '''## 2. WHERE IT STANDS (2026-09-18; the state doc #194)
- NUMBERS CLOSED. DEUTERONOMY 1:1-6:25 READ, FROZEN, COMPILED AND ON THE TAPE (sittings 1-4b; COMMITTED 64a8362 AND PUSHED).
- 220 frozen units, standing 2203, hash 8b8fff1fa28953af. 61 runners, 66 daemons, 454 functions; registries 1125 kinds / 1025 effects.
- THE TAPE at RUN (1304, 96, 88, 0, 12, 1595, 37, 319, the four pairs, 127), markers 167, closes 127, the counter (40, 11, 1); the sweep 61/61;
  every gate GREEN; the register gate DECLARED 100 / DEBT 0.
- IN FLIGHT: SITTING 5 — CHAPTER 7's reading (7:1-26): RUN 1 DONE (the measurements, the ink 119/0, the design in the map); NEXT: RUN 2 the rows
  WHOLE and the ledger. ON THE TABLE, not rulings: the Decalogue-schema question; THE INSTALL HYPOTHESIS (the map's tail).
- Uncommitted since 64a8362: run 1's records, the tutorial ARCHITECTURE/DEUTERONOMY_SO_FAR.md (+ epub).

'''
s = s[:i] + sec2 + s[j:]
old6 = "- The Decalogue-schema question: the state doc's #185 addendum 1 (ON THE TABLE)."; assert s.count(old6) == 1
s = s.replace(old6, "- ON THE TABLE: the Decalogue-schema question (the state doc's #185 addendum 1); THE INSTALL HYPOTHESIS (the map's tail section).")
n = len(s.encode('utf-8')); assert n <= 10240, ('THE RECOVERY PAGE OVER ITS CAP', n); plans.append((P, s))
P = f'{MEM}/deuteronomy-walk.md'; s = read(P)
old = 'description: "THE DEUTERONOMY WALK opened 2026-09-15'; assert s.count(old) == 1
s = s.replace(old, 'description: "THE DEUTERONOMY WALK opened 2026-09-15 — SITTING 5 (chapter 7) RUN 1 DONE 2026-09-18, THE INSTALL HYPOTHESIS on the table;', 1)
plans.append((P, s.rstrip('\n') + MEM_PARA))
P = f'{MEM}/MEMORY.md'; s = read(P)
old = "chapters 1-6 READ AND COMPILED (4b DONE 2026-09-17, four runs; COMMITTED 64a8362, PUSHED); NEXT: the commit on his word, then chapter 7's reading"
new = "chapters 1-6 COMPILED (64a8362 PUSHED); SITTING 5 (ch 7) RUN 1 DONE 2026-09-18; the INSTALL hypothesis ON THE TABLE; NEXT: RUN 2 the rows, the ledger"
assert s.count(old) == 1; s2 = s.replace(old, new); n = len(s2.encode('utf-8')); assert n < 17000, n; plans.append((P, s2))
for p, s2 in plans: assert s2 != read(p), p
for p, s2 in plans: open(p, 'w', encoding='utf-8').write(s2); print('WROTE', p.replace(ROOT, '<repo>').replace(MEM, '<memory>'), len(s2.encode('utf-8')))
