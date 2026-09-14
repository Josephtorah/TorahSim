#!/usr/bin/env python3
# THE NUMBERS WALK 15b (2026-09-13): THE RECORDS at the compile's close — NUMBERS_WALK.md "Sitting 15b — AS BUILT" (from ref_asbuilt.md with the sweep's,
# the journal gate's and the cursor probes' lines filled from their own prints), the reading ledger's CORRECTIONS block, COMPILE_DEBT.md's sitting-15b box
# (the sitting-15 box PAID + the new debts), MIDDOT.md's docket entries, MISHNAH_TOPICS' marks, RESEARCH_LOG.md's entry, THE_STEPS' paragraph, THE_BRIEFING's
# bullet, World/RESUME.md's line, memory (three files), the state doc's #160, the recovery file's section 17. Every append anchored; every file linted after
# by the caller. Idempotent on the markers. write_bor_compile_records.py's form. MOVE_CATALOG untouched (no new move this sitting — the shelf's forms known;
# exemplars in MIDDOT's case law).
import os, re
ROOT = '<repo-old>'; SP = os.path.dirname(os.path.abspath(__file__)); MEM = '<memory>'
sweep = open(f'{SP}/ref_sweep.out', encoding='utf-8').read()
m = re.search(r'(\d+)/(\d+) runners? green.*?([\d,]+) graded cells', sweep, re.S) or re.search(r'(\d+)/(\d+).*?([\d,]+) graded', sweep, re.S)
assert m and m.group(1) == m.group(2), 'the sweep\'s print has no green line: read it'
NR, CELLS = m.group(1), m.group(3)
SWEEP_LINE = '%s/%s runners green, %s graded cells (14b\'s 6327 + the refuge runner\'s 51; cold_run_refuge.py 51/51); the dependency and daemon gates inside it GREEN' % (NR, NR, CELLS)
jg = open(f'{SP}/ref_journal_gate.out', encoding='utf-8').read()
mi = re.search(r'the index over all (\d+) segments: ([\d,]+) rows', jg)
assert 'GATE GREEN' in jg and mi, 'the journal gate\'s print has no green line or no index count: read it'
JOURNAL_LINE = 'THE JOURNAL GATE GREEN (four segments byte-identical across two processes — 3,362 lines each, THE REST 3,358; chains verified; the index %s rows over %s segments; the running world\'s counts MATCH the RUN tuple — ledger 1539 = writes, timers 66 = sets, pending 14, markers 157; population 148 = rows 148 on every world; closed 121 = closes 121, foreign 0);' % (mi.group(2), mi.group(1))
cp_ = open(f'{SP}/ref_cursor_probes.out', encoding='utf-8').read()
assert '6/6 probes' in cp_, 'the cursor probes did not pass 6/6: read the print'
CURSOR_LINE = 'cursor_probes 6/6 against the base this tape run regenerated (no engine change this sitting — the register gate\'s test and the parser\'s rule the only instrument changes);'
def rd(p): return open(p, encoding='utf-8').read()
def wr(p, s): open(p, 'w', encoding='utf-8').write(s)
def append(p, text, marker):
    s = rd(p)
    if marker in s: print('  (already)', p); return
    assert s.endswith('\n'); wr(p, s + text); print('  appended', p)
def insert_before(p, anchor, text, marker):
    s = rd(p)
    if marker in s: print('  (already)', p); return
    assert s.count(anchor) == 1, (p, anchor[:60], s.count(anchor)); i = s.index(anchor); wr(p, s[:i] + text + s[i:]); print('  inserted', p)
def insert_after_line(p, anchor, text, marker):
    s = rd(p)
    if marker in s: print('  (already)', p); return
    assert s.count(anchor) == 1, (p, anchor[:60], s.count(anchor)); i = s.index(anchor); j = s.index('\n', i) + 1; wr(p, s[:j] + text + s[j:]); print('  inserted', p)
def mark_line(p, head, text, marker):
    s = rd(p); lines = s.split('\n')
    hits = [i for i, l in enumerate(lines) if l.startswith(head)]
    assert len(hits) == 1, (head, len(hits))
    if marker in lines[hits[0]]: print('  (already)', head[:30]); return
    lines[hits[0]] = lines[hits[0]].rstrip() + text; wr(p, '\n'.join(lines)); print('  marked', head[:40])

# 1. NUMBERS_WALK — the as-built
asb = rd(f'{SP}/ref_asbuilt.md').replace('{SWEEP_LINE}', SWEEP_LINE).replace('{JOURNAL_LINE}', JOURNAL_LINE).replace('{CURSOR_LINE}', CURSOR_LINE)
assert '{SWEEP_LINE}' not in asb and '{JOURNAL_LINE}' not in asb and '{CURSOR_LINE}' not in asb
append(f'{ROOT}/World/step9/NUMBERS_WALK.md', asb if asb.startswith('\n') else '\n' + asb, '## Sitting 15b — AS BUILT')

# 1b. the reading ledger's CORRECTIONS block
CORR = '''
## CORRECTIONS (appended at the compile, THE NUMBERS WALK sitting 15b, 2026-09-13 — append-only; the rows above stand as written)
- "THE BARE DUAL THOUSAND: … bare it misses eight Bible seats and misreads 1 Samuel 13:2 as a thousand" — the eight were the pe-patach test's count; the compile's corpus diff (every verse of the Tanakh, the parser before the rule against the parser after) found TEN bare-class verses moved right by the rule: the eight, and TWO PAUSAL DUALS (1 Chronicles 5:21, Nehemiah 7:71 — a qamats under the pe at the verse's pause, invisible to the patach test) — and one FALSE read gone (Psalm 8:8's "sheep and oxen", read [2000] since 1b). The class is 31 tokens in 28 verses (the reading's "26 seats" the patach instrument's verse count); the rule reads the dual by THE SHEVA (the vowel point) UNDER THE LAMED, which both pointings share. The claim's substance stands; the count is the widest instrument's (cold_run_sequence.py rule 29; census_probes D1-D9, R71-R72).
- THE THOUSAND THOUSANDS (1 Chronicles 21:5, 22:14, 2 Chronicles 14:8, Daniel 7:10 — אֶלֶף אֲלָפִים "a thousand thousands") read wrong before and after the rule ([103000, 470000] → [1000, 100000, 470000] at 22:14): FILED with R73 the tripwire on the present read — a rule owed to the book that reaches it, not this chapter's (no Torah seat).
'''
append(f'{ROOT}/logic/oral_triage/num_35_refuge_cities_2026-09-13.md', CORR, '## CORRECTIONS (appended at the compile, THE NUMBERS WALK sitting 15b')

# 2. COMPILE_DEBT — the sitting-15 box PAID + the sitting-15b box
DEBT = '''## SITTING 15b — THE COMPILE OF THE REFUGE CITIES (2026-09-13; NUMBERS_WALK.md "Sitting 15b" design + as-built; the owner: "Go" after the #158 rereads; the
## sitting-15 box (a)-(m) PAID — (a) THE BARE DUAL THOUSAND TAUGHT as rule 29 (the sheva under the lamed marks the dual; probes D1-D9 to FAIL 9/9, then 208/208
## with R62-R73; the corpus diff read verse by verse — twelve moved, none a marker; the two pausal duals found by the diff; 4b's owed line PAID); (b) THE
## LEVITE CITIES as the law's table — 48 = 6 + 42 asserted, the measures a DATA row with three settings (R. Akiva, R. Eliezer son of R. Yosei HaGelili, the
## Mishnah in Arakhin), the four sides THE CAMP'S ORDER by CALL, 26:54's rule by CALL at its third seat, ONE debit on the people OPEN to Joshua 21 (whose four
## lots the parser sums to 48 and whose tally reads [48]), the register gate NOTHING TO PAY; (c) THE SIX CITIES a DATA row of three and three with the names
## OUTSIDE the chapter by seat, the appointment ONE debit OPEN to Deuteronomy 4:41 and Joshua 20:7-8; (d) THE MURDERER AND THE MANSLAYER — the case table from
## the tokens (the instruments, the manners, the intents), the size a PARAMETER with the iron's exemption, the sword by CALL, flees_to_refuge and has_blood
## REUSED, Issi ben Akiva's 'unresolved'; (e) THE TERM — NOT a timer: an EVENT-KEYED open BODY entry dwells_in_refuge valued the office-holder (Eleazar by
## CALL), CLOSED BY VALUE when the daemon consumes high_priest_died (the scene's three terms set and closed by two deaths; no manslayer on the tape); the three
## high priests as DATA; (f) THE BORDER CASE has_blood = no_blood reused, Onkelos' court-first clause as DATA; (g) THE WITNESSES two by the prototype, one for
## acquittal, as DATA; (h) NO RANSOM twice against the ox's ransom by the live call M1.has_lemma on Exodus 21:30 beside the EFFECTS row, the talion's money by
## CALL; (i) THE LAND polluted — a STATUS on the land of Canaan; Genesis 9:6 by CALL into the primeval runner's Cain cells; Leviticus 18:25-28 by CALL; the
## inclusio 5:3 by CALL with presence_dwells READ; (j) the edges — fifteen CALL by reference, balak FALSE, the census's three demands read (family VIA
## second_census; pre_sinai VIA primeval; yovel PARAMETER carries place); (k) the docket 666 rows by the union rule in eight parts; (l) the display layer as
## filed at the reading; (m) the kin readings filed): cold_run_refuge.py 51/51 (five cells, fifteen engines CALLED), law_refuge the 62nd daemon (given_at Num
## 35:1; installed_by boot with the class named — the divine voice in the plains of Moab), the tape's TWO lines page_order at (40, 6, 1) with NO close and 2
## writes; RUN (1279, 66, 52, 0, 12, 1527, 33, 318, four pairs, 121) predicted and matched first tape run; THE REST 14b's exactly; CR1-CR9 MATCH first run; CV2,
## CX2 and CW3 retyped (12 -> 14 commanded, 5 -> 7 open); THE REGISTER GATE --strict GREEN with nothing to pay (its tilde test taught the dual thousand);
## every gate green. AND WITH IT NUMBERS CLOSES. THE NEW DEBTS: (i) THE TWO DEBITS OPEN BY DESIGN — give_the_levites_cities_and_pasture_lands (Joshua 21:1-42:
## the request 21:2 quoting the spec, the four lots, the tally 21:41) and appoint_six_cities_of_refuge (Deuteronomy 4:41-43 Moses' three INSIDE the Torah —
## that book's compile closes nothing, 'six shall they be'; Joshua 20:7-8 the six): STEP 6 THE READBACK's items beside 32's crossing, 33's dispossession and
## 34's division; (ii) THE TERM'S CLOSER OUTSIDE THE TORAH — Joshua 24:33 Eleazar's death: no dwells_in_refuge entry stands on the tape to close, the form
## proved in the scene (three terms, two deaths); the office's succession after Eleazar (Phinehas — Judges 20:28) THE READBACK's; (iii) THE THOUSAND
## THOUSANDS (1 Chronicles 21:5, 22:14, 2 Chronicles 14:8, Daniel 7:10) — wrong before and after rule 29, R73 the tripwire: a rule owed to the book that reaches
## it; the myriad-word (Ezra 2:64, Nehemiah 7:66, 7:70) filed beside; (iv) DEUTERONOMY — 19:1-13 the refuge law's twin (the roads, the three more cities, the
## forest, 'and live' 4:42, the enemy's exile), 21:1-9 the heifer (the measure-verb's third Torah seat at 21:2; Mishnah Sotah 9 the exam), 17:6 and 19:15 the
## witnesses' spec, 25:2's 'wicked' for the lashes (Makkot 5a, Sanhedrin 10a), 24:16 the kin, 12:1-2's classing, 4:41-43 Moses' three — the book's own
## compile; JOSHUA 20-21 the runs, 20:6 quoting 35:12 — THE READBACK's; (v) THE SIZE THAT CAN KILL a PARAMETER (Sanhedrin 76b — the stab against the blow; the
## Sifrei's induction from three) with no cell reading a weight: the exam's rows DATA; (vi) THE COURT OF TWENTY-THREE built from the tokens as DATA (Sanhedrin
## 1:6; 2a-2b) — no court entity on the tape (the_court in force since Exodus 18:25 by the tent daemon; its size a later design's); (vii) THE RENT (Makkot
## 13a:2-3 — R. Yehuda / R. Meir on 35:6 and 35:11) and THE SOJOURNER'S EXILE (Makkot 9a — Rav Kahana against the baraita) parameter rows with no verdict
## fetched; (viii) THE DISPLAY LAYER as the sitting-15 box's (l) — the store's "eye" for the answer-verb and the mixed gloss families a display sitting's
## census; (ix) THE REGISTER GATE'S TILDE — the gate now tells the marked dual thousand (a count) from the dual measures (a unit inside the token); a third
## tilde class, if the parser ever marks one, must be typed into the same test. Filed this sitting for the walk's watches (memory): THE CLASS'S COUNT IS THE
## WIDEST INSTRUMENT'S (a regex on one vowel found 29, the diff over every verse 31 — measure a class on the whole corpus before typing its count); A SEAT IS
## A VERSE, A TOKEN A TOKEN (the reading's 26, the measure's 29, the diff's 31 three grains of one class — name the grain with the number); THE GATE'S PARSER
## READS EXPLICIT BRANCHES ONLY (a kind dispatched through `k in (...)` is a kind no daemon watches — one `if k ==` per kind, one literal W per branch); A
## RESERVED FIELD NAME IS THE STITCHER'S (`until` is a scene-clock day, `day` the clock — name the ink's term `term`); THE MARK IS SHARED, THE MEANING IS
## NOT (the parser's tilde on the dual thousand met the register gate's tilde test for dual measures — a new use of a mark is a new case for every reader
## of the mark); A COUNTERPARTY IS NO ENTITY (the shedder who is only a counterparty gets no ledger and no entity — count the written-on parties);
## THE VAV-FORM (the bare consonants עד are "until" at every chapter seat; "and a witness" wears the vav — a homograph claim is typed from the DB's
## tokens, never from the reading's eye).
'''
append(f'{ROOT}/World/step9/COMPILE_DEBT.md', DEBT, '## SITTING 15b — THE COMPILE OF THE REFUGE CITIES')

# 3. MIDDOT — the docket's entries (before the Exodus block campaign section)
MID = '''- THE REFUGE CITIES' DOCKET (THE NUMBERS WALK sitting 15b, 2026-09-13; logic/oral_triage/num_35_refuge_cities_exam_2026-09-13.md — 666 rows; the rules about
  rules the docket carries, each at its row):
  · A CHAIN OF VERBAL ANALOGIES WITH ONE END IN THIS CHAPTER (Eruvin 51a:8 — Rav Chisda; the Sabbath block's own row, credited here): place (Exodus 16:29) /
    place (21:13) / flee (21:13) / flee (35:26) / border (35:26) / border (35:27) / outside (35:27) / OUTSIDE (35:5 — "you shall measure from outside the city
    two thousand cubits"): eight links, each pair a shared token, the Sabbath limit's measure fetched from the Levite city's; and 51a:9's refusal of the
    ninth — "outside" from "outside", not from "outward" (35:4's thousand): a chain is only as long as its exact tokens.
  · TEN AND TEN AND THREE — A COUNT BUILT FROM TWO TOKENS AND A THIRD VERSE (Sanhedrin 2a:14-2b:1; Mishnah Sanhedrin 1:6; the Sifrei 160:8): "the
    congregation shall judge" (35:24) and "the congregation shall deliver" (35:25) — a congregation is ten (14:27's ten spies); a majority of two to convict
    ("after the many to incline", Exodus 23:2, read with 23:2's "do not follow the many for evil") and one so the court is odd: twenty-three. The exemplar of
    the count of mentions joined to an arithmetic rule: the Sifrei states the sum, the Mishnah its parts, the Gemara the third verse.
  · WHERE A MEASURE IS WRITTEN AND WHERE IT IS NOT (Sanhedrin 76b:12-13 on 35:16-18): "in hand … whereby he may die" at the stone and the wood, absent at the
    iron — Shmuel: iron of any size kills; Rebbi's baraita: "revealed and known before Him who spoke and the world came to be … therefore the Torah gave it
    no measure"; the Gemara's edge: only when he stabbed. THE SILENCE READ AS A RULE, and bounded — the omitted clause teaches by its absence, but only as far
    as the reason for the absence reaches.
  · THE INDUCTION FROM THREE (the Sifrei 160:3-5; the binyan av): the stone, the wood, the iron — "what is common to the three: they can kill" — extended to
    every instrument that can kill; its limit stated in the same breath: the water, the fire, the snake, whose judgment is Heaven's. A father built from
    three verses names the feature it carries and the class it leaves.
  · A RESTRICTION AFTER A RESTRICTION AMPLIFIES (Makkot 9b:5-8; Bava Kamma 86b:17-19): "without seeing" (35:23) and "without knowledge" (Deuteronomy 19:4) —
    R. Yehuda reads the first as excluding the blind; R. Meir reads the two together as amplifying and includes him. The rule's exemplar at a case whose
    two arms are both on the shelf (the DATA row the_blind_killer).
  · TWO VERSES THAT COME AS ONE TEACH NOTHING (Sanhedrin 45b:12): the murderer ("the avenger of blood shall put him to death", 35:19-21) and the avenger —
    no principle of "the one obligated in the deed's first stage completes it" is drawn from their pair; and the court appoints an avenger where there is
    none ("when he meets him", 45b:13). The constraint on generalization stated inside the chapter's own two rows.
  · "THE TORAH SPOKE IN THE LANGUAGE OF MEN" ON A DOUBLED INFINITIVE (Makkot 12a:13-15 on 35:26 "if going out he goes out"): the doubled verb read as
    deliberate-or-unwitting exit by one baraita, refused by Abaye for the other — the end is not severer than the beginning; the same mark (Genesis 27:30's
    twin) that teaches elsewhere teaches nothing here because the rule it would yield contradicts the law's shape.
  · WE DO NOT PUNISH BY INFERENCE — A THIRD SEAT (Makkot 5b:15-16; the Sifrei 157:6 and 160:3): the lashed excluded by "wicked" / "wicked" (35:31; Deuteronomy
    25:2) and the exiled by "murderer" / "murderer" (35:21; 35:11) from an a fortiori's reach — the analogies stand in for the inference the rule refuses;
    the chapter's two halves joined by its one root at the rule's own seat.
  · THE COUNT OF MENTIONS (Makkot 11a:12; Mishnah Makkot 2:6): "the death of the high priest" three times — 35:25, 35:28 twice — the three high priests
    whose deaths return the exile (the anointed, the many-garmented, the relieved); R. Yehuda's fourth from 35:32's bare "the priest". A count of a phrase's
    seats read as a count of the law's subjects, the fourth from a variant form.
  · THE PLURAL'S MINIMUM IS TWO UNLESS "ONE" IS WRITTEN (the Sifrei 161:1 on 35:30; Sanhedrin 33b:15): "by the mouth of witnesses" — two by the prototype;
    "one witness shall not testify against a soul to die" — and R. Yosei son of R. Yehuda's "to die": not to convict, but he may answer to acquit. The
    prototype rule for a bare plural stated at its seat, the exception cut by the verse's own last word.
  · THE OFFICE THAT SHOULD HAVE PLEADED (Makkot 11a:14; 11b:11 — Rava): why does the high priest's death release the exile? the high priests should have
    pleaded for mercy that no one kill unwittingly in their days, and did not; the second high priest — he should have pleaded for the verdict. A reason
    supplied for a term the ink states without one; the reason then decides the cases the ink does not (the priest appointed after the verdict).
  · HEAVEN'S DEATH IS COMMUTED, MAN'S NEVER (Ketubot 37b:12 — R. Yishmael son of R. Yochanan ben Beroka): "you shall take no ransom for the life of a
    murderer" (35:31) against the ox's owner's ransom (Exodus 21:30) — those executed at Heaven's hand give money and are atoned; those the court executes,
    never ("dedicated of men shall not be redeemed", Leviticus 27:29). Two seats reconciled by the agent of the death, not by the deed.
  · THE HEIFER YIELDS TO THE FOUND KILLER (Mishnah Sotah 9:7; Sotah 47b:2; Ketubot 37b:6): the heifer broken and then the murderer found — he is executed:
    "except by the blood of him who shed it" (35:33); a procedure completed does not spend the atonement the verse assigns to the shedder's blood.
'''
insert_before(f'{ROOT}/logic/MIDDOT.md', '## Exodus block campaign', MID, "THE REFUGE CITIES' DOCKET (THE NUMBERS WALK sitting 15b")

# 3b. MISHNAH_TOPICS — the tractates the docket opened
T = f'{ROOT}/logic/MISHNAH_TOPICS.md'
mark_line(T, '**35. Mishnah, Lashes**', " — ch 2 READ WHOLE 2026-09-13 (THE NUMBERS WALK sitting 15b: the manslayer's chapter at the refuge cities' docket — the downward motion, the permission and the office, the father and the son, the six cities and the roads, the three high priests, the border and the tree, the Levite exiled, the honor and the rent; num_35_refuge_cities_exam_2026-09-13.md).", 'sitting 15b')
mark_line(T, '**34. Mishnah, Courts**', " — 1:6, 3:4-5, 9:1-2 read 2026-09-13 (THE NUMBERS WALK sitting 15b: the twenty-three from the congregation-tokens; the kin and the haters off the bench; the beheaded and the intent's table at the refuge cities' docket).", 'sitting 15b')
mark_line(T, '**31. Mishnah, First Gate**', " — 4:5 read 2026-09-13 (THE NUMBERS WALK sitting 15b: the ox that killed a man — the ransom the refuge cities' chapter refuses for the murderer).", 'sitting 15b')
mark_line(T, '**13. Mishnah, Merging Domains**', " — 4:3, 5:1-5 read 2026-09-13 (THE NUMBERS WALK sitting 15b: the city squared and the two thousand measured — the Levite city's measure at Numbers 35:5 the Sabbath limit's).", 'sitting 15b')
mark_line(T, '**28. Mishnah, Suspected Wife**', " — 5:3, 9:7 read 2026-09-13 (THE NUMBERS WALK sitting 15b: R. Akiva's day on the thousand and the two thousand; the heifer yielding to the found killer).", 'sitting 15b')
mark_line(T, '**45. Mishnah, Valuations**', " — 9:8 read 2026-09-13 (THE NUMBERS WALK sitting 15b: the Levite cities' fields, lots and houses unchangeable — Leviticus 25:34 at Numbers 35:2-7).", 'sitting 15b')
mark_line(T, '**36. Mishnah, Oaths**', " — 4:1 read 2026-09-13 (THE NUMBERS WALK sitting 15b: the oath of testimony's parties beside 35:30's one witness).", 'sitting 15b')
mark_line(T, '**40. Mishnah, Erroneous Rulings**', " — 3:4 read 2026-09-13 (THE NUMBERS WALK sitting 15b: the anointed against the many-garmented — the high priest whose death releases the exile).", 'sitting 15b')

# 4. RESEARCH_LOG — the findings
RL = '''
## 2026-09-13 — THE REFUGE CITIES' COMPILE (THE NUMBERS WALK sitting 15b — AND WITH IT NUMBERS CLOSES): THE PAUSAL DUAL; THE THOUSAND THOUSANDS; THE MYRIAD-WORD;
## A SEAT AND A TOKEN; THE REGISTER GATE'S TILDE; THE STITCHER'S RESERVED FIELD; THE GATE'S EXPLICIT BRANCHES; THE VAV-FORM WITNESS; THE COUNTERPARTY'S ENTITY

1. THE PAUSAL DUAL. The measurement pass found the bare dual thousand (אַלְפַּיִם, "two thousand") by the patach under the pe: 29 tokens. The rule was written on
the SHEVA UNDER THE LAMED instead (the same instrument as 1b's "two" — the dual ending's own mark), and the corpus diff over every verse found two more:
1 Chronicles 5:21 and Nehemiah 7:71, where the dual stands at the verse's pause with a QAMATS under the pe (אֲלָפָיִם, "two thousand" at the pause). The patach test cannot see a pausal
form; the sheva test reads both. The class is 31 tokens in 28 verses; both pausal seats read right the first time and are R71-R72. Lesson: measure a class
with the widest instrument (the diff over every verse) before typing its count; a regex on one vowel is a narrower instrument than the rule it measures for.
2. THE THOUSAND THOUSANDS. אֶלֶף אֲלָפִים ("a thousand thousands" = 1,000,000; 1 Chronicles 21:5, 22:14, 2 Chronicles 14:8, Daniel 7:10) reads wrong before and
after rule 29 (22:14: [103000, 470000] → [1000, 100000, 470000]): the plural "thousands" after a unit "thousand" is a MULTIPLIER the parser's grouping does not
know. No Torah seat; filed with R73 holding the present read as a tripwire — the rule is owed to the book that reaches it. The myriad-word (רִבּוֹא,
Ezra 2:64, Nehemiah 7:66, 7:70 — "two myriads" the same dual form on another noun) filed beside as the class's cousin.
3. A SEAT IS A VERSE, A TOKEN A TOKEN. The reading said "26 seats", the measure "29 tokens", the diff "31 tokens in 28 verses", and the design typed
"twenty-one compound seats" for eighteen compound TOKENS — four numbers of one class at three grains, one of them a hand's slip. The runner asserts the
grain with the number everywhere (MURDER_TOK_35 twenty tokens against MURDER_T twenty-one verses). Name the grain.
4. THE REGISTER GATE'S TILDE. The parser marks the dual measures ("two cubits", "two days", "twice") with a tilde, and the register gate's numeral-run test
reads any tilde as "a unit inside the token" — a MEASURE. Rule 29 marks the bare dual thousand with the same tilde. The strict gate fired the same hour:
Num 4:36's 2,750 Kohathites and 4:40's 2,630 Gershonites — count lines declared NONE with a why — came back "MEASURE-ONLY … STALE". The gate's test now
excepts the dual thousand (a NUMBER's dual, a count). Lesson: a mark is shared, a meaning is not — a new use of a mark is a new case for every reader of
the mark; grep the mark's readers before reusing it.
5. THE STITCHER'S RESERVED FIELD. The narrative's second line carried `'until': 'the death of the high priest'` and the stitcher fell re-basing it: `until` is
a scene-clock DAY the stitcher re-bases, `day` the clock (a42f518's banked lesson "a count field is named days, never until", met now at a TERM). The field
is `term`. The recorder ran twice.
6. THE GATE'S PARSER READS EXPLICIT BRANCHES ONLY (O3's lesson met at a new form). The daemon dispatched three exam kinds through one `if k in (...)` with one
shared effects dict; the daemon gate parsed none of them — two kinds "watched by NO daemon", one kind's effects wider than declared. One `if k == ...` per
kind with its own literal W dict; the yaml's watches retyped from the gate's print (killer_case carries commanded and returns_to_his_possession;
refuge_statute_case carries flees_to_refuge and no exempt).
7. THE VAV-FORM WITNESS. The runner's assert typed "the bare consonants עד are 'until' at 12, 25, 28, 32 and 'witness' at 30 — the lemmas decide". The DB:
35:30's witness is וְעֵד ("and a witness") — the vav on it; the bare token עד inside the chapter is the preposition at every seat (5704). The homograph
claim is typed from the DB's tokens (the vav-form carries the witness), never from the reading's eye.
8. THE COUNTERPARTY'S ENTITY. The scene's prediction counted 25 exam persons + the land = 26 entities; the engine made 25: the unexecuted shedder's row
writes land_polluted_by_blood ON THE LAND with the shedder as COUNTERPARTY (the design's own decision), so nothing is written on him and no entity is
made. Count the written-on parties, never the submitted subjects — the borders' narrative had taught it for the tape (moses and israel subjects, no
write, no entity); the scene met it at a case.
9. "THE PRIEST" BARE INSIDE THE PLENE PHRASE. "until the death of the priest" typed at three seats missed Joshua 20:6, whose "until the death of the high
priest" contains the bare phrase — a prefix phrase's census includes every longer phrase it opens. Four seats.
10. DEUTERONOMY NEVER SAYS "REFUGE". The refuge-word (מִקְלָט, lemma 4733) has twenty Bible verses; the Torah's eleven are all in this chapter; Deuteronomy
4:41-43 and 19:1-13 name the cities and the flight without the word. Joshua 20-21 and Chronicles 6 carry it. Filed for that book's compile.
'''
append(f'{ROOT}/RESEARCH_LOG.md', RL, "THE REFUGE CITIES' COMPILE (THE NUMBERS WALK sitting 15b")

# 5. THE_STEPS — the sitting-15b paragraph
STEPS = '''
SITTING 15b — THE COMPILE OF THE REFUGE CITIES (2026-09-13, on Brian's "Go" after the #158 rereads; World/step9/NUMBERS_WALK.md "Sitting 15b" design +
as-built; the state doc's #159 written before the parser was taught) — AND WITH IT NUMBERS CLOSES. The measurements first: the parser wrong at one verse of
the chapter (35:5's four "two thousand" reading nothing — the bare dual thousand named at the reading), the callees' cells live with their values typed from
the print, the tape's grounds (the people's twelve debits with five open, the Levites' block standing, Eleazar in office since Aaron's death with no close
inside the Torah, the Presence dwelling since Exodus 40:34), the register gate with nothing to pay. THE DESIGN'S DECISIONS: the bare dual taught as RULE 29
by the sheva under the lamed (nine probes to FAIL, then the corpus diff read verse by verse — twelve moved, two of them pausal duals the measure had not
seen, one the thousand thousands filed); the Levite cities ONE debit on the people with the Levites as counterparty, the measures and the forty-eight as
DATA (the three settings — the Sabbath limit's two thousand R. Akiva's), the four sides in THE CAMP'S ORDER by call; the six cities a DATA row with the
names outside the chapter and ONE debit open to Joshua 20; the murderer's and the manslayer's case table from the tokens with the size a PARAMETER; THE
TERM NOT A TIMER — an event-keyed open entry on the manslayer valued the office-holder, closed by value when the daemon consumes the high priest's death
(the engine's timers are day-dues; a death is no date); the border's no-blood the burglar's clause reused; the witnesses two by the prototype; no ransom
twice against the ox's ransom by a live call; the land polluted a STATUS on the land, Genesis 9:6 and Leviticus 18 by call, "in whose midst I dwell" the
book's inclusio with 5:3 read, not rewritten. The docket 666 rows by the union rule in eight parts (Makkot 7a-13a whole, Sanhedrin 2a-b / 76b-79a / 27b /
45b, Bava Kamma 40a-41a, Ketubot 37b, Eruvin 51a, Sotah 27b, Arakhin 33b, Yoma 23a, Megillah 29a, Yevamot 46b; Mishnah Makkot 2 whole): the Sabbath limit
is this chapter's measure by Rav Chisda's chain; the court of twenty-three from the congregation-tokens; the iron needs no measure; the downward motion;
the term's reason and its three priests; the avenger after the court; no ransom and why the ox has one; the land's atonement and the heifer; the
inclusio's two readings; the rule about rules a third time. The types by script (two tape kinds, four exam kinds, three effects, no registry row; the 62nd
daemon boot with its class named); the gates run to FAIL and read; the runner's five cells 51/51 on the third run (the guard refusing a name for an
expectation; four print-corrected retypes and one model miss — the counterparty who gets no entity); the daemon gate's honest fire read (explicit
branches only — the daemon rewritten, the watches retyped from the print); the dependency census's three demands past the imports read (family VIA the
second census; pre-Sinai VIA the primeval story; the holding a PARAMETER carrying a place); the recorder twice (the stitcher's reserved field `until`);
THE LEDGER ON THE TAPE: two debits on the people open by design to Joshua 20 and 21, nothing else — no close, no timer, no row; the RUN tuple predicted in
the design and matched first tape run, THE REST 14b's exactly, the nine checkpoints and the three retypes all MATCH first run; every probe gate, the daemon,
dependency, journal and register gates green — the register gate after one honest fire on its own tilde test (the parser's new mark on the dual thousand
read as a dual measure; the test taught the difference); the sweep %s/%s. NUMBERS 1:1-36:13 READ, FROZEN, COMPILED AND ON THE TAPE (27 and 36 by THE
TENT). Next on the owner's word: the next book.
''' % (NR, NR)
insert_before(f'{ROOT}/THE_STEPS.md', '## THE FINDINGS LOOP + THE STAMP LAW (owner-approved 2026-08-31)', STEPS, 'SITTING 15b — THE COMPILE OF THE REFUGE CITIES')

# 6. THE_BRIEFING — the scoreboard bullet
BRIEF = '''- **THE REFUGE CITIES COMPILED — SITTING 15b DONE, AND WITH IT NUMBERS CLOSES: THE BARE DUAL THOUSAND TAUGHT (RULE 29 — 35:5'S FOUR "TWO THOUSAND" READ AT LAST, THE CORPUS DIFF FINDING TWO PAUSAL DUALS THE MEASURE HAD MISSED), THE LEVITE CITIES AND THE SIX CITIES TWO DEBITS ON THE PEOPLE OPEN TO JOSHUA, THE TERM "UNTIL THE DEATH OF THE HIGH PRIEST" AN EVENT-KEYED ENTRY CLOSED BY THE DEATH ACT — NOT A TIMER, THE LAND POLLUTED A STATUS ON THE LAND, "IN WHOSE MIDST I DWELL" THE BOOK'S INCLUSIO READ BACK TO 5:3** (2026-09-13; NUMBERS_WALK.md "Sitting 15b"): cold_run_refuge.py the 57th runner (51/51), law_refuge the 62nd daemon; the docket 666 rows — the Sabbath limit is this chapter's measure (Rav Chisda's chain of eight verbal analogies), the court of twenty-three from the congregation-tokens, the iron needs no measure, the three high priests, no ransom and why the ox has one; RUN (1279, 66, 52, 0, 12, 1527, 33, 318, four pairs, 121) predicted and matched first tape run; the sweep %s/%s at %s; every gate green (the register gate after teaching its tilde test the dual thousand). NUMBERS 1:1-36:13 READ, FROZEN, COMPILED AND ON THE TAPE. Next on the owner's word: the next book.
''' % (NR, NR, CELLS)
insert_after_line(f'{ROOT}/THE_BRIEFING.md', '## SCOREBOARD (as of 2026-09-12, latest)', BRIEF, 'THE REFUGE CITIES COMPILED — SITTING 15b DONE')

# 7. World/RESUME.md
RES = '''SITTING 15b DONE 2026-09-13 (THE COMPILE OF THE REFUGE CITIES 35:1-34 — AND WITH IT NUMBERS CLOSES; NUMBERS_WALK.md "Sitting 15b" design + as-built; the owner: "Go" after the #158 rereads): RULE 29 THE BARE DUAL THOUSAND taught (the sheva under the lamed; probes 9/9 to FAIL then 208/208; the corpus diff twelve moved — two pausal duals found, the thousand thousands filed); the docket 666 rows (the Sabbath limit this chapter's measure; the twenty-three from the tokens; the iron needs no measure; the three high priests; no ransom and why the ox has one); cold_run_refuge.py 51/51 the 57th runner, law_refuge the 62nd daemon; TWO debits on the people OPEN by design to Joshua 20 and 21, THE TERM an event-keyed entry closed by the death act (three terms set and closed in the scene), the land polluted a status on the land, the inclusio read back to 5:3; RUN (1279, 66, 52, 0, 12, 1527, 33, 318, four pairs, 121) predicted and matched first tape run; every gate green; the sweep %s/%s at %s. NUMBERS 1:1-36:13 READ, FROZEN, COMPILED AND ON THE TAPE. NEXT on the owner's word: the next book.
''' % (NR, NR, CELLS)
append('<world-link>/RESUME.md', RES, 'SITTING 15b DONE 2026-09-13')

# 8. memory — numbers-in-order-ruling.md (a line + the description), MEMORY.md (the numbers line), step9-exam-era.md (the lessons head)
p = f'{MEM}/numbers-in-order-ruling.md'; s = rd(p)
if 'SITTING 15b DONE 2026-09-13' not in s:
    s = s.rstrip('\n') + '\nSITTING 15b DONE 2026-09-13 — THE COMPILE OF THE REFUGE CITIES 35:1-34, AND WITH IT NUMBERS CLOSES (NUMBERS_WALK.md "Sitting 15b" design + as-built; the owner: "Go" after the #158 rereads; the state doc\'s #159 before the parser was taught, #160 at the close): RULE 29 THE BARE DUAL THOUSAND — verse_words marks the dual אַלְפַּיִם ("two thousand") by THE SHEVA UNDER THE LAMED with the tilde, UNITS gains it at 1000, ink_numbers reads the marked dual as 2,000 wherever it stands and the unmarked plural as a noun; census_probes D1-D9 written to FAIL 9/9 (35:5 ×4 reading nothing; Joshua 3:4\'s cubit read as one; 1 Samuel 13:2\'s dual read as a thousand; Psalm 8:8\'s "sheep and oxen" reading [2000] since 1b), R62-R73 the regressions and the finds; 208/208; THE CORPUS DIFF over every verse read verse by verse — TWELVE moved: the nine predicted, TWO PAUSAL DUALS the measure\'s patach test had missed (1 Chronicles 5:21, Nehemiah 7:71 — right now), ONE the thousand thousands (1 Chronicles 22:14 — wrong before and after, R73 the tripwire; the class\'s four seats filed), eighteen marked only, none a marker; the docket 666 rows by the union rule in eight parts (104 link in 25 works + 562 topic; Makkot 7a-13a whole, Sanhedrin 2a-b / 76b-79a / 27b / 45b, Bava Kamma 40a-41a, Ketubot 37b, Eruvin 51a, Sotah 27b, Arakhin 33b, Yoma 23a, Megillah 29a, Yevamot 46b; Mishnah Makkot 2 whole; LAW 97 / DERIVATION 112 / DISPUTE 105 / CONTEXT 352) — THE SABBATH LIMIT IS THIS CHAPTER\'S MEASURE (Eruvin 51a:8, Rav Chisda\'s chain of eight verbal analogies to 35:5\'s "from outside the city"; R. Akiva\'s, R. Eliezer\'s and the Mishnah in Arakhin\'s three settings on two verses), THE COURT OF TWENTY-THREE FROM THE CONGREGATION-TOKENS (Sanhedrin 2a-2b — ten and ten and three), THE IRON NEEDS NO MEASURE (Sanhedrin 76b:12-13), THE DOWNWARD MOTION (Makkot 7b:2), THE TERM\'S REASON AND ITS THREE PRIESTS (Makkot 11a-11b), THE AVENGER AFTER THE COURT (Makkot 12a; Sanhedrin 45b), NO RANSOM AND WHY THE OX HAS ONE (Ketubot 37b; Bava Kamma 83b), THE LAND\'S ATONEMENT AND THE HEIFER, THE INCLUSIO\'S TWO READINGS (Shabbat 33a; Megillah 29a), the rule about rules a third time (Makkot 5b); the types by script (2 tape kinds, 4 case kinds incl. high_priest_died, 3 effects — dwells_in_refuge BODY, returns_to_his_possession, land_polluted_by_blood; NO registry row; law_refuge the 62nd daemon, given_at 35:1, boot with the class named; fifteen CALL edges + balak FALSE; the census\'s three demands read — family VIA second_census, pre_sinai VIA primeval, yovel PARAMETER carries place); cold_run_refuge.py 51/51 on the THIRD run (the guard refusing a NAME for an expectation; FOUR print-corrected retypes — the bare "until the death of the priest" inside Joshua 20:6\'s plene, THE VAV-FORM WITNESS (the bare עד "until" at every chapter seat, וְעֵד "and a witness" at 30), three twin sizes, the borders runner\'s side-word row naming the court not 35:5 — and ONE MODEL MISS: the shedder who is only a COUNTERPARTY gets no entity, 26 → 25); THE DESIGN\'S DECISIONS: the Levite cities ONE debit on the people with the Levites as counterparty + the measures and the forty-eight as DATA (Joshua 21\'s four lots 13 + 10 + 13 + 12 = 48 by the parser) + the four sides THE CAMP\'S ORDER by CALL; the six cities a DATA row + ONE debit OPEN to Deuteronomy 4:41 and Joshua 20:7-8; the case table from the tokens with the size a PARAMETER; THE TERM AN EVENT-KEYED OPEN BODY ENTRY valued the office-holder (Eleazar by CALL), CLOSED BY VALUE when the daemon consumes high_priest_died — NOT a timer (the scene\'s three terms set and closed by two deaths); the border has_blood = no_blood reused; the witnesses two by the prototype; no ransom by the live call M1.has_lemma; the land polluted a STATUS on the land of Canaan; Genesis 9:6 and Leviticus 18:25-28 by CALL; "in whose midst I dwell" 5:3\'s inclusio by CALL with presence_dwells READ; THE DAEMON GATE\'S HONEST FIRE READ (the parser reads explicit branches only — the daemon rewritten as three `if k ==` branches, the watches retyped from the print); THE STITCHER\'S RESERVED FIELD (`until` a scene-clock day — the term\'s field named `term`; the recorder twice); THE REGISTER GATE\'S TILDE (the marked dual thousand read as a dual measure — Num 4:36 and 4:40 STALE; the test taught the difference); the stitcher\'s census as predicted to the number (on tape 1279, kinds 824, subjects 270); RUN (1279, 66, 52, 0, 12, 1527, 33, 318, four pairs, 121) PREDICTED AND MATCHED FIRST TAPE RUN, THE REST 14b\'s exactly; CR1-CR9 MATCH first run; CV2 / CX2 / CW3 retyped (12 → 14 commanded, 5 → 7 open, the newest appoint_six_cities_of_refuge); every probe gate green (census 208, installation 6 with I5 62, clock, sequence 4, view 6, population 9, journal 7, cursor 6, register 7 with R3 4 → 5 retyped); the daemon (427 WRAPPED), dependency (482 edges, 173 pointers), journal (population 148 = rows 148) and register (DECLARED 102, DEBT 0, nothing to pay) gates GREEN; the sweep %s/%s at %s. NUMBERS 1:1-36:13 READ, FROZEN, COMPILED AND ON THE TAPE (27 and 36 by THE TENT). UNCOMMITTED since a42f518. NEXT on the owner\'s word: THE NEXT BOOK (the owed forward seats filed across the walk — Deuteronomy 4:41-43, 19:1-13, 21:1-9, 17:6 / 19:15, 25:2, 12:1-2; the thousand-thousands rule at its first seat).\n' % (NR, NR, CELLS)
    old_d = "NUMBERS 35:1-34 READ AND FROZEN (sitting 15, 2026-09-13 — the walk's last reading in Numbers; 210 units, standing 2163, hash unmoved; the bare dual thousand named for the compile); NEXT 15b the refuge cities' compile — and with it Numbers closes; the next book on the owner's word. The body holds"
    assert s.count(old_d) == 1, s.count(old_d)
    s = s.replace(old_d, "NUMBERS 1:1-36:13 READ, FROZEN, COMPILED AND ON THE TAPE (sittings 1-15b; 57 runners, 62 daemons; 210 units, standing 2163, hash unmoved; sitting 15b's RUN (1279, 66, 52, 0, 12, 1527, 33, 318, four pairs, 121)) — NUMBERS CLOSED 2026-09-13; NEXT on the owner's word: the next book. The body holds")
    wr(p, s); print('  memory: numbers-in-order-ruling.md')
p = f'{MEM}/MEMORY.md'; s = rd(p)
old = [l for l in s.split('\n') if l.startswith('- [⚠ NUMBERS IN ORDER FROM 1:1]')]
assert len(old) == 1, len(old)
new = "- [⚠ NUMBERS IN ORDER FROM 1:1](numbers-in-order-ruling.md) — OWNER-RULED 2026-09-09: the chapter walk from 1:1 at the parashah grain (map World/step9/NUMBERS_WALK.md; chapters 9, 15:32-41, 27, 36 frozen at THE TENT and SKIPPED); ⚠ OWNER-RULED 2026-09-10 READ THEN COMPILE PER PORTION, never read ahead; CHAPTER NUMBERS, not portion names. NUMBERS 1:1-36:13 READ, FROZEN, COMPILED AND ON THE TAPE — NUMBERS CLOSED 2026-09-13 (sittings 1-15b; 57 runners, 62 daemons, RUN (1279, 66, 52, 0, 12, 1527, 33, 318, four pairs, 121); 210 units, standing 2163, hash 8b8fff1fa28953af unmoved; 15b: RULE 29 THE BARE DUAL THOUSAND taught by the sheva under the lamed — 35:5's four 'two thousand' read at last, the corpus diff finding two pausal duals and the thousand thousands (filed, R73); the Levite cities and the six cities TWO debits on the people OPEN to Joshua 20-21; THE TERM an event-keyed open entry closed by the death act, NOT a timer; the land polluted a status on the land; the inclusio 5:3 / 35:34 read back; the docket 666 rows — the Sabbath limit this chapter's measure, the twenty-three from the tokens; lessons: the widest instrument counts the class, the gate's parser reads explicit branches only, a mark is shared but its meaning is not, a counterparty is no entity). COMMITTED a42f518 (2026-09-11); sittings 8-15b UNCOMMITTED. THE REGISTER GATE (register_census.py --strict) AT EVERY COMPILE SITTING'S GATES STEP. NEXT on the owner's word: THE NEXT BOOK (the owed forward seats filed — Deuteronomy 4:41-43, 19:1-13, 21:1-9, 17:6 / 19:15, 25:2, 12:1-2)."
if old[0] != new:
    s = s.replace(old[0], new); wr(p, s)
size = len(rd(p).encode('utf-8')); assert size < 17000, size; print('  memory: MEMORY.md', size, 'bytes')
p = f'{MEM}/step9-exam-era.md'; s = rd(p)
LESSON = "⚠ THE NUMBERS WALK sitting 15b — THE REFUGE CITIES' COMPILE (2026-09-13; NUMBERS CLOSED): THE CLASS'S COUNT IS THE WIDEST INSTRUMENT'S — the measure's regex on the patach found 29 dual thousands, the corpus diff over every verse found 31 (two PAUSAL forms with a qamats): measure a class with the diff before typing its count; a regex on one vowel is narrower than the rule it measures for. A SEAT IS A VERSE, A TOKEN A TOKEN — 26 / 29 / 31 / \"twenty-one\" were four numbers of one class at three grains and a slip: name the grain with every count. THE GATE'S PARSER READS EXPLICIT BRANCHES ONLY (O3's lesson at a new form) — a kind dispatched through `if k in (...)` with a shared dict is a kind NO daemon watches: one `if k == '...'` per kind, one literal W per branch, the yaml's watches typed from the gate's print. A RESERVED FIELD NAME IS THE STITCHER'S — `until` is a scene-clock day it re-bases, `day` the clock: the ink's term goes in `term`; the recorder runs again after any runner change. THE MARK IS SHARED, THE MEANING IS NOT — rule 29 put the dual measures' tilde on the dual thousand and the register gate read every tilde as a measure (Num 4:36 and 4:40 STALE the same hour): before reusing a mark, grep its readers; teach each one the new case. A COUNTERPARTY IS NO ENTITY — the scene predicted 26 entities and the engine made 25: the shedder written on only as the land's counterparty has no ledger; count the written-on parties. THE VAV-FORM — a homograph claim is typed from the DB's tokens (35:30's witness is וְעֵד with the vav; the bare עד is \"until\" at every seat), never from the reading's eye. A PREFIX PHRASE'S CENSUS INCLUDES EVERY LONGER PHRASE IT OPENS (\"until the death of the priest\" at Joshua 20:6 inside the plene). THE GUARD REFUSES A NAME — the scene's and the narrative's tuples are tripwire asserts beside CASES, never CASES rows. THE COMPILE SITTING'S SHAPE HELD with a taught rule: measurements → design → probes to FAIL (9/9) → the state doc → the rule → the diff read → docket (eight parts) → types → gates to FAIL → runner (51/51 third run) → recorder (twice) → stitcher → literals + CR1-CR9 + three retypes → tape (10/10 first run) → probe gates → daemon gate (one honest fire) → dependency gate (three demands) → journal gate → register gate (one honest fire on its tilde) → cursor → sweep → records.\n"
if "sitting 15b — THE REFUGE CITIES' COMPILE" not in s:
    a = '## STANDING LESSONS AND WATCHES (moved verbatim from the MEMORY.md index line on 2026-09-07 to keep the index under its size limit; the W4/W3/W2/W1/D9/G/E lesson tail as it stood)\n'
    assert s.count(a) == 1; i = s.index(a) + len(a); s = s[:i] + LESSON + s[i:]; wr(p, s); print('  memory: step9-exam-era.md')

# 9. the state doc #160
SD = '''
═══ COMPACTION POINT #160 (2026-09-13 — written at THE NUMBERS WALK sitting 15b's close; THE REFUGE CITIES 35:1-34 COMPILED AND ON THE TAPE; NUMBERS 1:1-36:13 READ, FROZEN, COMPILED AND ON THE TAPE — NUMBERS CLOSED; EVERY GATE GREEN; A CLEAN COMPACTION POINT) ═══
STATE: 210 frozen units, standing 2163, hash 8b8fff1fa28953af UNMOVED (no unit touched this sitting); 57 runners (cold_run_refuge.py the 57th, 51/51), 62 daemons (law_refuge the 62nd), the sweep %s/%s at %s graded cells; RUN (1279, 66, 52, 0, 12, 1527, 33, 318, the four pairs, 121); the tape 10/10 with THE REST; the journal gate GREEN (population 148 = rows 148); THE REGISTER GATE --strict GREEN (DECLARED 102, DEBT 0, FAILS 0 — nothing to pay in 35; the footer Num 36:13 DAEMONS 5; its numeral-run test taught the marked dual thousand is a count); the daemon (427 WRAPPED, unconsumed 0) and dependency (482 edges, 173 pointers) gates GREEN; every probe file green (census 208, installation 6 with I5 62, clock, sequence 4, view 6, population 9, journal 7, cursor 6, register 7). LAST COMMIT a42f518; UNCOMMITTED: sittings 8 through 15's paths, THE CLOSE LINE's, and this sitting's (World/step9/cold_run_refuge.py NEW; cold_run_sequence.py — RULE 29 in the INK block, the import, DAEMON_ORDER, the tape's two lines, the literals, CR1-CR9, CV2/CX2/CW3 retyped; census_probes.py +21 (D1-D9, R62-R73); register_census.py (the tilde test); event_vocabulary.yaml +6, effect_vocabulary.yaml +3, daemon_dispositions.yaml (law_refuge, the functions block, the watches retyped), dependency_dispositions.yaml (the span, twenty edges), installation_probes.py (I5 62), register_probes.py (R3), DAEMON_INDEX.md / DEPENDENCY_INDEX.md / REGISTER_INDEX.md (gate-written); logic/oral_triage/num_35_refuge_cities_exam_2026-09-13.md NEW; the reading ledger's CORRECTIONS block; World/step9/NUMBERS_WALK.md ("Sitting 15b" design + AS BUILT); COMPILE_DEBT.md; logic/MIDDOT.md; logic/MISHNAH_TOPICS.md; RESEARCH_LOG.md; THE_STEPS.md; THE_BRIEFING.md; World/RESUME.md; World/step9/forms_numbers_walk/ (this sitting's scripts copied in); the recovery file's section 17; this doc) — commit only on "commit push" (the NEVER-COMMIT set and the staging-by-exclusion form as before; ARCHITECTURE excluded).
THE SITTING (the owner: "Go" after the #158 rereads; NUMBERS_WALK.md "Sitting 15b" design + as-built; 1b's order held with a taught rule): THE MEASUREMENTS (the parser wrong at 35:5 alone; the dual class 29 tokens by the patach — 31 by the diff; the callees' values typed from the print; the tape's grounds; the register gate nothing to pay; THE GLOBAL COUNTS grepped — CV2, CX2, CW3 the three that move; the prefix CR free; the docket sized 666) → THE DESIGN in NUMBERS_WALK.md before any code (rule 29; the Levite cities one debit + DATA; the six cities DATA + one debit; the case table; THE TERM an event-keyed entry, not a timer; the border; the witnesses; the ransom by the live call; the land a status; the inclusio read) → THE PROBES TO FAIL (D1-D9 9/9 FELL; R62-R70 regressions) → #159 → RULE 29 TAUGHT (the sheva under the lamed) → 205/205 → THE CORPUS DIFF READ (twelve moved: nine predicted, two pausal duals, the thousand thousands filed; R71-R73; 208/208) → the docket by the union rule (eight parts; 666 rows; the crowns) → the types by script → the gates to FAIL (2 + 16) → the runner 51/51 on the THIRD run (the guard's refusal of a name; four print-corrected retypes — the bare phrase inside the plene, THE VAV-FORM WITNESS, three twin sizes, the side-word row's seats; ONE MODEL MISS — the counterparty's entity) with the scene's thirty-three slots and the narrative matched first run → the recorder (twice — the stitcher's reserved field `until`) → the stitcher's census as predicted to the number → the literals, CR1-CR9, the three retypes → THE TAPE: RUN PREDICTED AND MATCHED FIRST RUN, THE REST 14b's exactly, 10/10 FIRST RUN → the probe gates (register_probes R3 4 → 5 retyped) → THE DAEMON GATE'S HONEST FIRE (explicit branches only — the daemon rewritten, the watches retyped) → THE DEPENDENCY GATE'S THREE DEMANDS READ (family VIA second_census; pre_sinai VIA primeval; yovel PARAMETER carries place) → the journal gate GREEN → THE REGISTER GATE'S HONEST FIRE (the tilde on the dual thousand read as a dual measure — Num 4:36 and 4:40 STALE; the test taught) → --strict GREEN → the cursor probes 6/6 → the sweep → the records.
THE RECORDS: NUMBERS_WALK.md "Sitting 15b — AS BUILT"; the docket; the reading ledger's CORRECTIONS block (the pausal duals; the thousand thousands); COMPILE_DEBT.md's sitting-15 box PAID and the 15b box (i)-(ix); MIDDOT's docket entries (the chain of verbal analogies; ten and ten and three; the measure written and not written; the induction from three; a restriction after a restriction; two verses as one; the language of men on a doubled infinitive; we do not punish by inference a third time; the count of mentions; the plural's minimum; the office that should have pleaded; Heaven's death commuted; the heifer yields); MISHNAH_TOPICS (Makkot 2 WHOLE; Sanhedrin, Bava Kamma, Eruvin, Sotah, Arakhin, Shevuot, Horayot marked); RESEARCH_LOG.md's ten findings; THE_STEPS' sitting-15b paragraph; THE_BRIEFING's scoreboard bullet; World/RESUME.md; the forms copied; memory (numbers-in-order-ruling.md, MEMORY.md, step9-exam-era.md's lessons head); the recovery file's section 17; this entry.
NEXT on the owner's word: THE NEXT BOOK. Nothing opens before the word. When it comes: the walk's shape as NUMBERS_WALK.md holds it (READ THEN COMPILE PER PORTION; the reading shape and the compile shape in the recovery file's section 5; the forms in World/step9/forms_numbers_walk/ — the ref_* set the newest); the spine for Deuteronomy Sifrei Devarim (memory spine-default); the owed forward seats filed across the walk — 4:41-43 Moses' three cities (the appointment's debit stands OPEN, 'six shall they be'), 19:1-13 the refuge law's twin, 21:1-9 the heifer, 17:6 and 19:15 the witnesses, 25:2 the lashes' "wicked", 12:1-2 the land-bound classing, 4:42's "and live"; the thousand-thousands rule (R73) at its first seat; THE READBACK (Joshua's runs — 14:1, 17:14-18, 19:51, 20:1-9, 21:1-42, 24:33) its own design at step 6.
POST-COMPACTION REREADS (mandatory, first sitting): the recovery file logic/pre_logic_methods_2026-07-28/RECOVERY_new_thread_2026-09-12.md whole (its section 5; its sections 16 and 17) + numbers-in-order-ruling.md + this entry + NUMBERS_WALK.md "Sitting 15" (the reading's form) + "Sitting 15b — AS BUILT" (the compile's) + THE_STEPS Step 2 + Step 5 + the compiler block; memory's STANDING LESSONS head (the sitting-15b paragraph first). WATCHES: as #158's + THE CLASS'S COUNT IS THE WIDEST INSTRUMENT'S + A SEAT IS A VERSE, A TOKEN A TOKEN + THE GATE'S PARSER READS EXPLICIT BRANCHES ONLY + A RESERVED FIELD NAME IS THE STITCHER'S + THE MARK IS SHARED, THE MEANING IS NOT + A COUNTERPARTY IS NO ENTITY + THE VAV-FORM.
''' % (NR, NR, CELLS)
append(f'{ROOT}/logic/pre_logic_methods_2026-07-28/PROMPT_continue_solo_era_2026-08-06.md', SD, 'COMPACTION POINT #160')

# 10. the recovery file — section 17
REC = '''
## 17. ADDENDUM (2026-09-13, at sitting 15b's close — the state doc's COMPACTION POINT #160; this supersedes section 16's NEXT, which is kept as written)

SITTING 15b DONE: CHAPTER 35 (the refuge cities) COMPILED AND ON THE TAPE — NUMBERS 1:1-36:13 READ, FROZEN, COMPILED AND ON THE TAPE (27 and 36 by THE TENT):
NUMBERS IS CLOSED. 57 runners (cold_run_refuge.py the 57th, 51/51), 62 daemons (law_refuge the 62nd, given_at 35:1, installed_by boot with the class named —
the divine voice in the plains of Moab); RUN (1279, 66, 52, 0, 12, 1527, 33, 318, the four pairs, 121); the sweep %s/%s at %s; EVERY GATE GREEN (the tape
10/10 first run, the journal gate with population 148 = rows 148, the register gate --strict with nothing to pay and its tilde test taught, the daemon and
dependency gates after one honest fire each read and repaired at the runner and the yaml, every probe file, vocab_lint 0). NUMBERS_WALK.md "Sitting 15b"
(design + as-built) the record; COMPILE_DEBT.md's sitting-15b box (i)-(ix) the owed items (the two debits OPEN to Joshua 20-21 and Deuteronomy 4:41 — THE
READBACK's; the term's closer Joshua 24:33 outside the Torah; the thousand thousands R73; Deuteronomy's seats; the size that can kill a parameter; the
twenty-three as DATA; the rent and the sojourner's exile; the display layer; the register gate's tilde). THE DESIGN'S DECISIONS: RULE 29 THE BARE DUAL
THOUSAND (the sheva under the lamed); the Levite cities ONE debit + DATA (the four sides THE CAMP'S ORDER); the six cities DATA + ONE debit; the case table
from the tokens (the size a PARAMETER); THE TERM AN EVENT-KEYED OPEN ENTRY closed by the death act — NOT a timer; the border's no-blood reused; the
witnesses by the prototype; no ransom by the live call; the land polluted a STATUS on the land; the inclusio 5:3 / 35:34 READ. THE FORMS of 15b are in
World/step9/forms_numbers_walk/ (ref_compile_recon.py, ref_runner_measure.py, ref_docket_scan.py, ref_compile_measure.py, ref_design.md, patch_probes_ref.py,
ref_parser_diff.py, ref_docket_A-H.py, write_ref_docket.py, add_types_ref.py, ref_part1-4.py — the runner assembled by cat, patch_seq_literals_ref.py,
ref_asbuilt.md, write_ref_compile_records.py, seq_record.py, seq_stitch.py). Still UNCOMMITTED since a42f518; commit only on "commit push".

NEXT on the owner's word: THE NEXT BOOK — nothing opens before the word. When it comes, the walk's shape holds: READ THEN COMPILE PER PORTION at the
parashah grain; the reading shape and the compile shape in section 5 (the forms the ref_* set); the spine Sifrei Devarim (memory spine-default) with
Onkelos whole; the register gate at every compile sitting's gates step; the owed forward seats filed across Numbers' walk (Deuteronomy 4:41-43, 19:1-13,
21:1-9, 17:6 and 19:15, 25:2, 12:1-2, 4:42) met at their chapters; THE READBACK (step 6) its own design when Joshua's runs are reached. Before the first
sitting: reread NUMBERS_WALK.md "Sitting 15" (the reading's form) and "Sitting 15b — AS BUILT" (the compile's), THE_STEPS Step 2 + Step 5 + the compiler
block, memory's STANDING LESSONS head.
''' % (NR, NR, CELLS)
append(f'{ROOT}/logic/pre_logic_methods_2026-07-28/RECOVERY_new_thread_2026-09-12.md', REC, '## 17. ADDENDUM (2026-09-13, at sitting 15b')
print('records written')
