import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE NUMBERS WALK 14b (2026-09-13): THE RECORDS at the compile's close — NUMBERS_WALK.md "Sitting 14b — AS BUILT" (from bor_asbuilt.md with the sweep's,
# the journal gate's and the cursor probes' lines filled from their own prints), COMPILE_DEBT.md's sitting-14b box (the sitting-14 box PAID + the new
# debts), MIDDOT.md's docket entries, RESEARCH_LOG.md's entry, THE_STEPS' paragraph, THE_BRIEFING's bullet, World/RESUME.md's line, memory (three files),
# the state doc's #157, the recovery file's section 15. Every append anchored; every file linted after by the caller. Idempotent on the markers.
# write_jou_compile_records.py's form. MOVE_CATALOG untouched (no new move this sitting — the shelf's forms known; exemplars in MIDDOT's case law).
import re, os, sys
ROOT = _ROOT; SP = os.path.dirname(os.path.abspath(__file__)); MEM = '<memory>'
sweep = open(f'{SP}/sweep_bor.out', encoding='utf-8').read()
m = re.search(r'(\d+)/(\d+) runners? green.*?([\d,]+) graded cells', sweep, re.S) or re.search(r'(\d+)/(\d+).*?([\d,]+) graded', sweep, re.S)
assert m and m.group(1) == m.group(2), 'the sweep\'s print has no green line: read it'
NR, CELLS = m.group(1), m.group(3)
SWEEP_LINE = '%s/%s runners green, %s graded cells (13b\'s 6271 + the borders runner\'s 56; cold_run_borders.py 56/56); the dependency and daemon gates inside it GREEN' % (NR, NR, CELLS)
jg = open(f'{SP}/bor_journal_gate.out', encoding='utf-8').read()
mi = re.search(r'the index over all (\d+) segments: ([\d,]+) rows', jg)
assert 'GATE GREEN' in jg and mi, 'the journal gate\'s print has no green line or no index count: read it'
JOURNAL_LINE = 'THE JOURNAL GATE GREEN (four segments byte-identical across two processes — 3,358 lines each, THE REST 3,340; chains verified; the index %s rows over %s segments; the running world\'s counts MATCH the RUN tuple — ledger 1537 = writes, timers 66 = sets, pending 14, markers 157; population 148 = rows 148 on the three seed worlds and 136 = 136 on THE REST; closed 121 = closes 121, foreign 0);' % (mi.group(2), mi.group(1))
cp_ = open(f'{SP}/bor_cursor_probes.out', encoding='utf-8').read()
assert '6/6 probes' in cp_, 'the cursor probes did not pass 6/6: read the print'
CURSOR_LINE = 'cursor_probes 6/6 against the base this tape run regenerated (no engine change this sitting);'
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

# 1. NUMBERS_WALK — the as-built
asb = rd(f'{SP}/bor_asbuilt.md').replace('{SWEEP_LINE}', SWEEP_LINE).replace('{JOURNAL_LINE}', JOURNAL_LINE).replace('{CURSOR_LINE}', CURSOR_LINE)
assert '{SWEEP_LINE}' not in asb and '{JOURNAL_LINE}' not in asb and '{CURSOR_LINE}' not in asb
append(f'{ROOT}/World/step9/NUMBERS_WALK.md', asb if asb.startswith('\n') else '\n' + asb, '## Sitting 14b — AS BUILT')

# 2. COMPILE_DEBT — the sitting-14 box PAID + the sitting-14b box
DEBT = '''## SITTING 14b — THE COMPILE OF THE BORDERS (2026-09-13; NUMBERS_WALK.md "Sitting 14b" design + as-built; the owner: "Go" after the #155 rereads; the
## sitting-14 box (a)-(k) PAID — (a) the four sides a DATA ROW built from the DB and ONE STATUS on the land of Canaan (the standing place entity), the
## points by side with their Joshua 15 and Ezekiel 47 kin, the two Mount Hors READ from the chukat runner, the promised extents and Ezekiel's order DATA
## rows with no verdict; (b) the lot by CALL — VIA second_census at 34:2 and 34:13, the open debit cited a third time, CW3; (c) the nine and a half a RUN
## CITATION of 32:33's three transfers, 110,580 by CALL, CW4 — the restatement writes nothing; Joshua 14:2's receipt outside the Torah; (d) the commission
## a STATUS and a DEBIT on the standing party the_dividers_of_the_land (12b's row; no entity for the ten princes) and TWELVE NAMED ROWS in the population
## table; (e) THE REGISTER GATE'S NUM 34 HEADERS SEAT PAID — the roll's persons as rows (as_of Num 34:17-29), the NONE declaration deleted, the gate's D
## section ROWS 12; (f) the parser — no rule owed, the doubling [1, 1]; (g) the edges declared — nine CALL by reference, the census's two demands read
## (family VIA at six seats with 34:5's brook a homograph by sense; offerings FALSE at 34:27 — Shelomi against the peace offerings); the erection runner's
## court sides corrected to the sanctuary_build runner's span, no demand made; (h) the docket 171 rows by the union rule with the Tosefta found local;
## (i) the display layer as filed; (j) the checkpoint prefix CW grepped free; (k) the two orders DATA rows): cold_run_borders.py 56/56 (five cells, nine
## engines CALLED — second_census, gad_reuben, shelach, chukat, bamidbar, naso, korach, zelophehad, journeys), law_borders the 61st daemon (given_at Num
## 34:1; installed_by boot with the class named — a law in the divine voice relayed at 34:13 in 36:5's form), the tape's THREE lines page_order at
## (40, 6, 1) with NO close, 3 writes and 12 rows; RUN (1277, 66, 52, 0, 12, 1525, 32, 318, four pairs, 121) predicted and matched first tape run; THE
## REST 13b's exactly; CW1-CW9 MATCH; CP1 retyped 136 -> 148 (the one global count moved); THE REGISTER GATE --strict GREEN with the seat paid; every gate
## green. THE NEW DEBTS: (i) THE DIVIDERS' DEBIT OPEN BY DESIGN — the_dividers_of_the_land's commanded divide_the_inheritance_to_the_children_of_israel_in_
## canaan stands OPEN beside its Gilead charge (32:28-30): the runs Joshua 14:1 (the triad divides), 17:14-18 (Joseph's claim answered), 19:51 (the lot
## before the LORD at Shiloh — "they finished dividing the land"), and Caleb's Hebron (14:13) and the daughters' holding (17:4) paid before the same
## court: STEP 6 THE READBACK's items beside the crossing's debit of 32 and the dispossession of 33; (ii) THE RELAY'S FORM (D2, the second pass): 34:13's
## "and Moses commanded the children of Israel" is 36:5's form, and 36:5's is the installing act command_relayed (THE TENT sitting 4) — law_borders stands
## boot with the class named; whether a relay in this form installs is D2's question, the DATA row the_relay_form its record; (iii) NUMBERS 27:12-23
## UNCOMPILED (8b's owed line, met again): Sanhedrin 16a:16-17 reads Joshua's commission verse (27:21 — "he shall stand before Eleazar the priest and ask
## counsel of the Urim") for the king's war; the same pair the chapter's dividers repeat; its first exam rows filed here; (iv) DEUTERONOMY — 12:1-2's
## classing of the land-bound commandments (Kiddushin 37a:4-6; the DATA row the_land_bound_rule carries the rule, no cell classes the commandments), 34:4's
## "this is the land" from Nebo (the phrase's Torah seats 34:2, 34:13, Deuteronomy 34:4), 1:7 and 11:24's extents (DATA, no verdict), 3:17's Chinnereth
## — the book's own compile later; (v) JOSHUA 13-19, 21 — the runs of the four sides (15:1-12 Judah's border, 18:20 and 19:49 "by its borders" the closers,
## 13:7 and 14:2 the nine and a half, 21:5-8 the Levite cities by lot) and 22:14's ten princes (the embassy's doubling) — THE READBACK's; Ezekiel 47-48
## (the four sides from the north; Ginnosar's kin at 19:35) and 1 Kings 8:65 / 2 Kings 14:25 (the kingdom's measure by the chapter's two ends) forward;
## (vi) THE SHELF'S OWN BORDER LINES (Mishnah Gittin 1:2 — Rekem, Ashkelon, Akko; Sheviit 6:1 — the two holdings' lines; the Tosefta 4:4's "two lands";
## Gittin 8a:4-6's string from Turei Amnon to the River of Egypt) are DATA rows with no cell: a border for a commandment (the bills, the sabbatical
## produce) is a legal reach the readback measures against the ink's one border, not a line the tape draws; (vii) THE HOMOGRAPHS FILED FROM THE RUNS —
## the bare side-word's Leviticus seats (the field's corner 19:9, 23:22; the beard's 19:27), the Gadite = the kid (Genesis 38:23; Judges 14:6), Ephod the
## person against the vestment, Shelomi against the peace offerings (the gate's own catch), the brook's consonants against the inheritance's (34:5 — the
## gate's catch at the reading's own seat), Ain against "the eye" (Ezekiel 12:12), the Reubenite's six and the Gadite's six by token: every one a token
## census against a lemma census — the two censuses typed apart; (viii) THE DISPLAY LAYER — as the sitting-14 box's (i). Filed this sitting for the walk's
## watches (memory): TWO CENSUSES OF ONE LABEL (the bare pair against the exact pair; the token against the lemma; the family against the token) — type
## the census the print made, not the label's; A MIXED MEASURE IS NO MEASURE (the reading's "eight names" took one name by lemma and two by token — the
## compile computes both clean censuses and files the delta); THE ROW'S SHAPE FOLLOWS THE FIRST WRITER'S (the optional column present as None — the
## view reads it by key); A REGISTER SEAT IS PAID BY ROWS (the gate's green class; the declaration deleted, key and body); THE FOURTH INSTANCE OF THE
## HAND'S TALLY (the side-word's eighteen typed from the reading's family count against the token's five).
'''
append(f'{ROOT}/World/step9/COMPILE_DEBT.md', DEBT, '## SITTING 14b — THE COMPILE OF THE BORDERS')

# 3. MIDDOT — the docket's entries (before the Exodus block campaign section)
MID = '''- THE BORDERS' DOCKET (THE NUMBERS WALK sitting 14b, 2026-09-13; logic/oral_triage/num_34_borders_exam_2026-09-13.md — 171 rows; the rules about rules the
  docket carries, each at its row):
  · THE ADJACENT VERSE CLASSES THE COMMANDMENTS (Kiddushin 37a:4-6 — the baraita on Deuteronomy 12:1-2; the adjacency rule, the case law's own family):
    "in the land" would confine every commandment, "all the days that you live upon the earth" would extend every one — "go and learn from what is stated
    in the next verse": the idolatry's ban is an obligation of the body and applies everywhere, so every obligation of the body applies everywhere and
    every obligation of the land inside the border alone (Rav Yehuda's classing, 37a:3); the exceptions by tradition (orlah and diverse kinds, 37a:1),
    the new crop disputed (37a:7-15 — R. Eliezer's "even" read two ways, decided by Abaye's "who disagrees with R. Eliezer? R. Yishmael"). The chapter's
    border is the rule's OBJECT; the classing is Deuteronomy's and the readback's.
  · "ONLY" EXCLUDES THE TWO WHO DIVIDE (Bava Batra 122a:12 on 26:55, read whole at this docket; E2 — the restrictor as a limitation): "ONLY by lot" — Joshua
    and Caleb took not by the lot they administer but by the LORD's word (Timnath-serah, Joshua 19:50) and by Moses' oath (Hebron, Joshua 14:13); the
    two dividers of 34:17 and 34:19 the two the restrictor excepts — the exclusion read against its own administrators.
  · THE LAW OF AGENCY ASKED OF A VERSE AND REFUSED (Kiddushin 42a:6-8 on 34:18): Rav Giddel in Rav's name founds agency on "one prince from each tribe you
    shall take to divide the land" — refused, "how can you understand this as agency? minors have no agency, and the princes divided for adults and
    minors alike"; the verse kept for another rule (the court's steward for orphans, "to their disadvantage and to their benefit"): a derivation tested
    against a case it cannot cover and re-seated — the form of a refused source.
  · A VERBAL ANALOGY NOT RECEIVED IS NOT USED (Sanhedrin 16a:7-9): the false prophet before the seventy-one by "presumptuously" / "presumptuously" (Deuteronomy
    18:20; 17:12) — but the elder's presumptuousness is a death penalty by twenty-three; Reish Lakish's "word" / "word" (17:10; 18:20) instead; and why
    not return the elder to seventy-one by the first analogy? "this tanna derives by 'word' / 'word' and not by 'presumptuously' / 'presumptuously', as he
    did not receive it as a tradition" — I2's own constraint (Pesachim 66a: no verbal analogy of one's own) stated inside a sugya on the courts.
  · ONE WORD READ TWO WAYS ON A BORDER (Gittin 8a:4-7 on 34:6): "and its border" — R. Yehuda: the sea itself directly across the land is the land; the
    Rabbis: the word teaches the islands within a string from Turei Amnon to the River of Egypt (the Tosefta Terumot 2:12's picture) — the same word
    the ground of both arms, each side's reading stated with what the other does with the word ("and the Rabbis, what do they do with 'and its
    border'?").
  · ONE BORDER ROUND ABOUT AGAINST THE JORDAN CANAAN'S (Bekhorot 55a:10 on 34:12; 55a:14 on 34:15): the tithe's flocks on both banks — "this shall be your
    land by its borders round about" makes the land one border with the tribes' demarcations inside it; R. Shimon ben Yochai reads "beyond the Jordan
    AT JERICHO" — as Jericho is Canaan's, the river is Canaan's: the inclusio's closer and the "at Jericho" pair each carried as a rule.
  · THE LOTTERY'S TWO RECEPTACLES (Bava Batra 122a:3-6, credited, read whole here): "only by lot" (26:55) and "by the mouth of the lot" (26:56) reconciled by
    the picture — Eleazar with the Urim, Joshua and all Israel before him, the tribes' names in one receptacle and the twelve regions' boundaries in the
    other, the lot of each confirming the Urim's word: two verses' instruments made one procedure; the dividers of 34:17 the procedure's persons.
  · A LIKENESS REFUSED BY WHAT THE FIRST CASE NEEDED (Sanhedrin 16a:2-3): Ulla's "as the beginning was by seventy-one, so a border dispute" — refused
    because the beginning also needed the lots, the Urim and all Israel present, which a later dispute does not: a likeness tested against every
    feature of its exemplar, not the one feature named.
'''
insert_before(f'{ROOT}/logic/MIDDOT.md', '## Exodus block campaign', MID, "THE BORDERS' DOCKET (THE NUMBERS WALK sitting 14b")

# 4. RESEARCH_LOG — the findings
RL = '''
## 2026-09-13 — THE BORDERS' COMPILE (THE NUMBERS WALK sitting 14b): TWO CENSUSES OF ONE LABEL; THE EIGHT NAMES A MIXED MEASURE; THE GATE'S CATCH AT THE
## READING'S OWN SEAT; REKEM THE MISHNAH'S EAST; GINNOSAR THE LOTTERY'S NAME; THE ROW'S SHAPE

1. TWO CENSUSES OF ONE LABEL. The runner's first run fell on "the land of Canaan (with the article) — thirteen Torah seats": the measure's label sat on the
bare pair אֶרֶץ כְּנַעַן ("the land of Canaan", thirteen Torah seats) while the exact pair הָאָרֶץ כְּנָעַן ("THE land Canaan" — the article on the land, none
on the name) has Numbers 34:2 alone. The reading's claim was the exact pair's (one seat) and stands; the compile typed both censuses apart. The same
class fell twice more the same sitting — the side-word (the reading's "eighteen Torah seats" is the word's family with its prefixes; the bare token
פְּאַת has five: 34:3, 35:5, and Leviticus 19:9 and 23:22 the field's CORNER, 19:27 the beard's — homographs by sense the family count hid) and Elizaphan
(four seats by token, six by lemma — Exodus 6:22 and Leviticus 10:4 spell the same Kohathite "Elzaphan"). The lesson: type the census the print made,
not the label's; a token census and a lemma census are two instruments.
2. THE EIGHT NAMES WERE A MIXED MEASURE. The reading's "eight names stand nowhere else (Elidad, Jogli, Ephod, Shiphtan, Parnach, Azzan, Ahihud, Pedahel)"
took Ephod by lemma (his token is the vestment's at Exodus 28:15, 39:8) and Chislon and Shelomi by token (their lemmas are single-seat; Chislon's token
is Joshua 15:10's Chesalon, Shelomi's "my peace-offerings" at Leviticus 10:14) — and missed Hanniel, only-here by token (1 Chronicles 7:39 spells his
namesake otherwise) though not by lemma. The two clean censuses: EIGHT BY TOKEN (Elidad, Hanniel, Ahihud, Pedahel, Jogli, Shiphtan, Parnach, Azzan), TEN
BY LEMMA (the eight less Hanniel, plus Ephod, Chislon, Shelomi). The reading ledger's CORRECTIONS block appended; the fact set stands, the measure is named.
3. THE GATE'S CATCH AT THE READING'S OWN SEAT. The dependency gate demanded borders → family for the inheritance token at six seats — 34:2, 13, 14, 15, 17
and 34:5 — and 34:5's token is נַחְלָה מִצְרָיִם, "the BROOK of Egypt": the inheritance's consonants under another word's points, the reading's own find,
now caught by the token census as a demand and declared inside the VIA row as a homograph by sense. The gate also demanded borders → offerings at
34:27 — שְׁלֹמִי "Shelomi" (Ahihud's father) against שְׁלָמַי "my peace-offerings": FALSE, a homograph by token. Two homographs the gate found where the
reading had named one.
4. REKEM IS THE MISHNAH'S EAST. Onkelos renders Kadesh-barnea "Rekem Geah" at 34:4 (the reading's find); Mishnah Gittin 1:2 draws the borders for the bills'
law "from Rekem eastward" — the translation's name of the chapter's south-east corner is the Mishnah's east point. And Bava Batra 122a:6 has the lottery
name Naphtali's boundary GINNOSAR — Onkelos's word for 34:11's sea of Chinnereth ("the sea of Gennesar", its one seat): the shelf's lottery names a
region by the translation's word for the chapter's east point. Both DATA, no verdict; both the translation's vocabulary meeting the shelf's.
5. THE GADITE IS THE KID. The gentilic הַגָּדִי ("the Gadite", 34:14 — the pair's first seat with the Reubenite) is by token also "the kid" (Genesis 38:23,
Judges 14:6): six seats by token, a homograph the reading's "thirteen in the Bible" for the pair did not name. Filed with the walk's homograph class.
6. THE ROW'S SHAPE FOLLOWS THE FIRST WRITER'S. The borders runner's twelve named rows omitted the optional `father` column for Eleazar (34:17 names no
father); the tape's first run fell at CP7's own view of the daughters' rows, which reads r['father'] by key — the second census runner's rows carry the
column as None. The column is always present now. A table's optional column is optional in the schema and expected by the views: the first writer's
shape is the table's.
7. THE REGISTER SEAT PAID BY ROWS. The register gate's Num 34 seat (the headers "these are the names of the men" at 34:17 and 34:19) was declared NONE
since the gate's birth with the why "chapters 34-36 not yet walked"; the population table's named grain was built at 26 for "the persons the roll names",
and this is the first roll reached since. The borders runner writes the twelve as rows while consuming the dividers' line; the gate's class flips to ROWS
(green) and the declaration, now STALE, is deleted — key and body. CP1's totals moved 136 → 148, the one global count the sitting moved, grepped first.
'''
append(f'{ROOT}/RESEARCH_LOG.md', RL, "THE BORDERS' COMPILE (THE NUMBERS WALK sitting 14b)")

# 5. THE_STEPS — the sitting-14b paragraph
STEPS = '''
SITTING 14b — THE COMPILE OF THE BORDERS (2026-09-13, on Brian's "Go" after the #155 rereads; World/step9/NUMBERS_WALK.md "Sitting 14b" design +
as-built; the state doc's #156 written before the docket). The measurements first: the parser reads the chapter's three numbers and no rule is owed (the
walk's third measured-zero probes step); the dividers of the land are already on the tape from chapter 32 with their Gilead charge open, the lot's debit
stands open, the grant's three transfers stand, the land of Canaan is a standing entity since Genesis's famines, and the register gate's one seat in the
chapter is a register header paid by population rows. FOUR DECISIONS: the four sides are a data row and ONE status on the land (the border is the land's
property — "the land of Canaan by its borders"), nothing on the people; the lot by call into the second census; Moses' restatement to the nine and a half
WRITES NOTHING — "have taken their inheritance" is the ledger's own three transfers read back, and Joshua 14:2's receipt lies outside the Torah; the
dividers named are a status and a debit on the standing party AND twelve named rows in the population table — the roll's persons enter the table, the
register seat is paid and its declaration deleted. The docket 171 rows by the union rule (Gittin 8a, Kiddushin 36b-37a, Sanhedrin 16a, Bava Batra
117a-122a credited, Mishnah Gittin 1:1-2, Sheviit 6:1 and 9:2, the Tosefta found local): the lottery's picture with Eleazar's Urim and two receptacles —
the dividers at work — and Naphtali's boundary named by the translation's word for this chapter's sea; the sea as a border two ways and the Jordan two
ways; the law of agency asked of "one prince from each tribe" and answered with the court's steward; the Canaanites' title claim from the heading; the
Mishnah's east at Rekem, the translation's name for Kadesh-barnea; the land-bound rule classed from Deuteronomy's adjacent verse. The types by script
(three tape kinds, two exam kinds, two effects, no registry row; the 61st daemon installed by boot with its class named — relayed at 34:13 in the form
36:5's installing act took, the second pass's question); the gates run to FAIL and read; the runner's five cells 56/56 on the sixth run — four readings
between (two censuses of one label typed apart; the eight names a mixed measure — eight by token, ten by lemma; Elizaphan's two censuses; a code
slip); the dependency census's two demands past the imports read (the inheritance's token at six seats, one of them the brook's consonants — VIA the
second census; Shelomi against the peace offerings — FALSE); THE LEDGER ON THE TAPE: one status on the land, nothing on the people, a status and a debit
on the dividers open by design to Joshua's runs, twelve rows, no close; the RUN tuple predicted in the design and matched first tape run, THE REST 13b's
exactly, the nine checkpoints all MATCH on the second run after one honest miss (a row's optional column read by key — the first writer's shape is the
table's); CP1's totals retyped, the one global count the sitting moved; the recorder once, the stitcher's census as predicted to the number; every
probe gate, the daemon, dependency, journal and register gates green; the sweep %s/%s. Numbers 1:1-34:29 read, frozen, compiled and on the tape. Next:
chapter 35 — the refuge cities' reading (the Sifrei returns at 35:9), then its compile, never the next reading first.
''' % (NR, NR)
insert_before(f'{ROOT}/THE_STEPS.md', '## THE FINDINGS LOOP + THE STAMP LAW (owner-approved 2026-08-31)', STEPS, 'SITTING 14b — THE COMPILE OF THE BORDERS')

# 6. THE_BRIEFING — the scoreboard bullet
BRIEF = '''- **THE BORDERS COMPILED — SITTING 14b DONE: THE LAND'S EXTENT IS ONE STATUS ON THE LAND (THE FOUR SIDES A DATA ROW), MOSES' RESTATEMENT WRITES NOTHING (THE GRANT READ BACK, JOSHUA 14:2'S RECEIPT OUTSIDE THE TORAH), THE DIVIDERS NAMED ARE A STATUS AND A DEBIT ON THE PARTY CHAPTER 32 CHARGED AND TWELVE NAMED ROWS IN THE POPULATION TABLE — THE FIRST REGISTER PAID BY ROWS SINCE THE TABLE WAS BUILT** (2026-09-13; NUMBERS_WALK.md "Sitting 14b"): cold_run_borders.py the 56th runner (56/56), law_borders the 61st daemon; the docket 171 rows — the lottery's two receptacles as the dividers at work, Naphtali's boundary named by the translation's word for this chapter's sea, the sea and the Jordan each a border two ways, the law of agency refused and the steward kept, Rekem the Mishnah's east; RUN (1277, 66, 52, 0, 12, 1525, 32, 318, four pairs, 121) predicted and matched first tape run; the sweep %s/%s at %s; every gate green. Numbers 1:1-34:29 read, frozen, compiled and on the tape. Next: chapter 35 (the refuge cities; the Sifrei returns at 35:9).
''' % (NR, NR, CELLS)
insert_after_line(f'{ROOT}/THE_BRIEFING.md', '## SCOREBOARD (as of 2026-09-12, latest)', BRIEF, 'THE BORDERS COMPILED — SITTING 14b DONE')

# 7. World/RESUME.md
RES = '''SITTING 14b DONE 2026-09-13 (THE COMPILE OF THE BORDERS 34:1-29; NUMBERS_WALK.md "Sitting 14b" design + as-built; the owner: "Go" after the #155 rereads): the docket 171 rows (the lottery's two receptacles; the sea and the Jordan each a border two ways; agency refused, the steward kept; Rekem the Mishnah's east); cold_run_borders.py 56/56 the 56th runner, law_borders the 61st daemon; ONE status on the land of Canaan, NOTHING on the people (the restatement a run citation), a status and a debit on the dividers of the land and TWELVE population rows — the register gate's Num 34 seat PAID; RUN (1277, 66, 52, 0, 12, 1525, 32, 318, four pairs, 121) predicted and matched first tape run; every gate green; the sweep %s/%s at %s. NEXT: chapter 35's reading (the refuge cities; the Sifrei returns at 35:9).
''' % (NR, NR, CELLS)
append('<world-link>/RESUME.md', RES, 'SITTING 14b DONE 2026-09-13')

# 8. memory — numbers-in-order-ruling.md (a line + the description), MEMORY.md (the numbers line), step9-exam-era.md (the lessons head)
p = f'{MEM}/numbers-in-order-ruling.md'; s = rd(p)
if 'SITTING 14b DONE 2026-09-13' not in s:
    s = s.rstrip('\n') + '\nSITTING 14b DONE 2026-09-13 — THE COMPILE OF THE BORDERS 34:1-29 (NUMBERS_WALK.md "Sitting 14b" design + as-built; the owner: "Go" after the #155 rereads; the state doc\'s #156 before the docket, #157 at the close): THE PROBES STEP A MEASURED ZERO (the walk\'s third); the docket 171 rows by the union rule (6 link in 4 works + Gittin 8a, Kiddushin 36b-37a, Sanhedrin 16a, Bava Batra 117a-122a credited, Mishnah Gittin 1:1-2, Sheviit 6:1 and 9:2, the Tosefta Sheviit 4:4 and 4:12 found local; LAW 3 / DERIVATION 23 / DISPUTE 16 / CONTEXT 129) — THE LOTTERY\'S TWO RECEPTACLES the dividers at work (Bava Batra 122a:4-6) with Naphtali\'s boundary GINNOSAR the translation\'s word for 34:11\'s sea; the sea as a border two ways (Gittin 8a:4-7), the Jordan two ways (Bekhorot 55a:10, 55a:14); the law of agency asked of 34:18 and refused, the steward kept (Kiddushin 42a:6-8); the Canaanites\' title claim from the heading (Sanhedrin 91a:6); REKEM the Mishnah\'s east = the translation\'s Kadesh-barnea (Gittin 1:2); the land-bound rule from Deuteronomy 12:1-2\'s adjacent verse (Kiddushin 37a:4-6); the types by script (3 tape kinds, 2 case kinds, 2 effects — borders_declared, dividers_named; NO registry row; law_borders the 61st daemon, given_at 34:1, installed_by boot with the class named — relayed at 34:13 in 36:5\'s form, D2\'s question; nine CALL edges, the census\'s two demands read — family VIA at six seats with 34:5\'s brook a homograph by sense, offerings FALSE at 34:27 Shelomi); cold_run_borders.py 56/56 on the SIXTH run (TWO CENSUSES OF ONE LABEL typed apart — the exact pair "the land Canaan" one seat against the bare pair\'s thirteen, the side-word\'s bare token five against the family\'s eighteen; THE EIGHT NAMES A MIXED MEASURE — eight by token, ten by lemma; Elizaphan four by token, six by lemma; a dict\'s eager default); THE FOUR DECISIONS: the four sides a DATA row and ONE STATUS on the land of Canaan (nothing on the people — the lot\'s debit cited a third time), the lot by CALL, THE RESTATEMENT WRITES NOTHING (the grant\'s three transfers read back, 110,580 by CALL; Joshua 14:2\'s receipt outside the Torah), THE DIVIDERS a status and a debit on the standing party of 32:28 AND TWELVE NAMED ROWS in the population table — the register gate\'s Num 34 seat PAID, its NONE declaration deleted, CP1 retyped 136 -> 148 (the one global count moved); the recorder once; the stitcher\'s census as predicted to the number (on tape 1277, kinds 822, subjects 270); RUN (1277, 66, 52, 0, 12, 1525, 32, 318, four pairs, 121) PREDICTED AND MATCHED FIRST TAPE RUN, THE REST 13b\'s exactly; 10/10 on the SECOND run (ONE MISS READ: a row\'s optional column read by key at another chapter\'s view — the first writer\'s shape is the table\'s); every probe gate green (census 187, installation 6 with I5 61, clock, sequence 4, view 6, population 9, journal 7, cursor 6, register 7 with R3 3 -> 4 daemons and R6 ROWS 3 -> 4 retyped from the print); the daemon (422 WRAPPED), dependency (462 edges, 173 pointers), journal (population 148 = rows 148) and register (DECLARED 102; the seat ROWS) gates GREEN; the sweep %s/%s at %s. NUMBERS 1:1-34:29 READ, FROZEN, COMPILED AND ON THE TAPE (27 by THE TENT). UNCOMMITTED since a42f518. NEXT: CHAPTER 35 — the refuge cities\' reading (35:1-34; THE SIFREI RETURNS at 35:9, piskaot 159-161 by position; the parser measured first on 35:4-5\'s cubits and 35:14\'s cities), THEN its compile (15b) — never the next reading first.\n' % (NR, NR, CELLS)
    old_d = "NUMBERS 34:1-29 READ AND FROZEN (sitting 14; 209 units, standing 2149, hash unmoved); NEXT 14b the borders' compile, then chapter 35's reading (the refuge cities; the Sifrei returns at 35:9). The body holds"
    assert s.count(old_d) == 1, s.count(old_d)
    s = s.replace(old_d, "NUMBERS 1:1-34:29 READ, FROZEN, COMPILED AND ON THE TAPE (56 runners, 61 daemons; 209 units, standing 2149, hash unmoved; sitting 14b's RUN (1277, 66, 52, 0, 12, 1525, 32, 318, four pairs, 121)); NEXT chapter 35's reading (the refuge cities; the Sifrei returns at 35:9), then its compile. The body holds")
    wr(p, s); print('  memory: numbers-in-order-ruling.md')
p = f'{MEM}/MEMORY.md'; s = rd(p)
old = [l for l in s.split('\n') if l.startswith('- [⚠ NUMBERS IN ORDER FROM 1:1]')]
assert len(old) == 1, len(old)
new = "- [⚠ NUMBERS IN ORDER FROM 1:1](numbers-in-order-ruling.md) — OWNER-RULED 2026-09-09: the chapter walk from 1:1 at the parashah grain (map World/step9/NUMBERS_WALK.md; chapters 9, 15:32-41, 27, 36 frozen at THE TENT and SKIPPED); ⚠ OWNER-RULED 2026-09-10 READ THEN COMPILE PER PORTION, never read ahead; CHAPTER NUMBERS, not portion names. NUMBERS 1:1-34:29 READ, FROZEN, COMPILED AND ON THE TAPE (sittings 1-14b; 56 runners, 61 daemons, RUN (1277, 66, 52, 0, 12, 1525, 32, 318, four pairs, 121); 209 units, standing 2149, hash 8b8fff1fa28953af unmoved; THE CLOSE LINE built 2026-09-12; 14b (2026-09-13): the four sides ONE STATUS ON THE LAND, the restatement WRITES NOTHING, the dividers a status and a debit on the party of 32:28 and TWELVE POPULATION ROWS — the first register PAID BY ROWS since the table was built; the lottery's two receptacles the dividers at work; the eight names a MIXED MEASURE — eight by token, ten by lemma; the two-censuses lesson). COMMITTED a42f518 (2026-09-11); sittings 8-14b UNCOMMITTED. THE REGISTER GATE (register_census.py --strict) AT EVERY COMPILE SITTING'S GATES STEP. NEXT: CHAPTER 35 — the refuge cities' reading (35:1-34; THE SIFREI RETURNS at 35:9, piskaot 159-161; the parser on 35:4-5's cubits first), THEN its compile (15b)."
if old[0] != new:
    s = s.replace(old[0], new); wr(p, s)
size = len(rd(p).encode('utf-8')); assert size < 17000, size; print('  memory: MEMORY.md', size, 'bytes')
p = f'{MEM}/step9-exam-era.md'; s = rd(p)
LESSON = "⚠ THE NUMBERS WALK sitting 14b — THE BORDERS' COMPILE (2026-09-13): TWO CENSUSES OF ONE LABEL — the runner fell three times on a number typed from a label, not from the census the print made: the exact pair \"THE land Canaan\" has one seat where the bare pair has thirteen; the side-word's bare token has five Torah seats (Leviticus's field-corner and beard-corner among them, homographs by sense) where the reading's eighteen counted the family; Elizaphan has four seats by token and six by lemma. Type the census the print made; a token census and a lemma census are two instruments, and a family count a third. A MIXED MEASURE IS NO MEASURE — the reading's \"eight names nowhere else\" took Ephod by lemma and Chislon and Shelomi by token and missed Hanniel (only-here by token): the compile computes both clean censuses (eight by token, ten by lemma) and files the delta in the ledger's CORRECTIONS block. THE ROW'S SHAPE FOLLOWS THE FIRST WRITER'S — an optional column omitted on one runner's rows fell at another chapter's view (r['father'] by key): carry every column the first writer carries, None where the ink is silent. A REGISTER SEAT IS PAID BY ROWS — the gate's green class for a register is ROWS (rows in the population table whose as_of begins with the chapter), the daemon writes them while consuming the roll's line, and the NONE declaration is then STALE: delete the key and its body before the strict run. THE GATE CATCHES THE READING'S HOMOGRAPH AT ITS OWN SEAT — the dependency census demanded the inheritance token at 34:5 (the brook's consonants) and Shelomi at 34:27 (the peace offerings' token): declare the sense inside the row (VIA with the homograph named; FALSE). THE DICT'S EAGER DEFAULT — d.get(k, e[k]) evaluates e[k] first: one map, every key. THE COMPILE SITTING'S SHAPE HELD with a measured-zero probes step: measurements → design → (no probe) → the state doc → docket (four parts) → types → gates to FAIL → runner (56/56 sixth run) → recorder (once) → stitcher → literals + CW1-CW9 + CP1's retype → tape (10/10 second run; the RUN tuple first run) → probe gates → journal gate → register gate (the seat paid; R3 and R6 retyped) → sweep → records.\n"
if "sitting 14b — THE BORDERS' COMPILE" not in s:
    a = '## STANDING LESSONS AND WATCHES (moved verbatim from the MEMORY.md index line on 2026-09-07 to keep the index under its size limit; the W4/W3/W2/W1/D9/G/E lesson tail as it stood)\n'
    assert s.count(a) == 1; i = s.index(a) + len(a); s = s[:i] + LESSON + s[i:]; wr(p, s); print('  memory: step9-exam-era.md')

# 9. the state doc #157
SD = '''
═══ COMPACTION POINT #157 (2026-09-13 — written at THE NUMBERS WALK sitting 14b's close; THE BORDERS 34:1-29 COMPILED AND ON THE TAPE; NUMBERS 1:1-34:29 READ, FROZEN, COMPILED AND ON THE TAPE, 27 BY THE TENT; EVERY GATE GREEN; A CLEAN COMPACTION POINT) ═══
STATE: 209 frozen units, standing 2149, hash 8b8fff1fa28953af UNMOVED (no unit touched this sitting); 56 runners (cold_run_borders.py the 56th, 56/56), 61 daemons (law_borders the 61st), the sweep %s/%s at %s graded cells; RUN (1277, 66, 52, 0, 12, 1525, 32, 318, the four pairs, 121); the tape 10/10 with THE REST; the journal gate GREEN (population 148 = rows 148); THE REGISTER GATE --strict GREEN (DECLARED 102, DEBT 0 — the Num 34 seat PAID by rows, its declaration deleted; the footer Num 36:13 DAEMONS 4); the daemon (422 WRAPPED) and dependency (462 edges, 173 pointers) gates GREEN; every probe file green (census 187, installation 6 with I5 61, clock, sequence 4, view 6, population 9, journal 7, cursor 6, register 7). LAST COMMIT a42f518; UNCOMMITTED: sittings 8 through 14's paths, THE CLOSE LINE's, and this sitting's (World/step9/cold_run_borders.py NEW; cold_run_sequence.py — the import, DAEMON_ORDER, the tape's three lines, the literals, CW1-CW9, CP1 retyped; event_vocabulary.yaml +5, effect_vocabulary.yaml +2, daemon_dispositions.yaml (law_borders, the functions block), dependency_dispositions.yaml (the span, eleven edges), installation_probes.py (I5 61), register_probes.py (R3, R6), register_dispositions.yaml (the Num 34 seat deleted), DAEMON_INDEX.md / DEPENDENCY_INDEX.md / REGISTER_INDEX.md (gate-written); logic/oral_triage/num_34_borders_exam_2026-09-13.md NEW; the reading ledger's CORRECTIONS block; World/step9/NUMBERS_WALK.md ("Sitting 14b" design + AS BUILT); COMPILE_DEBT.md; logic/MIDDOT.md; logic/MISHNAH_TOPICS.md; RESEARCH_LOG.md; THE_STEPS.md; THE_BRIEFING.md; World/RESUME.md; World/step9/forms_numbers_walk/ (this sitting's scripts copied in); the recovery file's section 15; this doc) — commit only on "commit push" (the NEVER-COMMIT set and the staging-by-exclusion form as before; ARCHITECTURE excluded).
THE SITTING (the owner: "Go" after the #155 rereads; NUMBERS_WALK.md "Sitting 14b" design + as-built; 1b's order held with a measured-zero probes step): THE MEASUREMENTS (the parser's three numbers read, no rule owed; the dividers of the land ALREADY on the tape from 32:28 with their Gilead charge open; the lot's debit one and open; the grant's three transfers; the land of Canaan a standing entity; Caleb's and the daughters' holdings open; the chukat runner's two_mount_hors row naming 34:7-8; the register gate's Num 34 seat a REGISTER HEADER paid by rows; THE GLOBAL COUNTS grepped — CP1 the one that moves; the prefix CW free; the docket sized 171) → THE DESIGN in NUMBERS_WALK.md before any code — FOUR DECISIONS: the four sides ONE STATUS ON THE LAND (a DATA row; nothing on the people), the lot by CALL, THE RESTATEMENT WRITES NOTHING (a run citation of the grant; Joshua 14:2's receipt outside the Torah), the dividers a STATUS and a DEBIT on the standing party AND TWELVE NAMED ROWS (the register seat paid) → the docket by the union rule (171 rows; the crowns: the lottery's two receptacles the dividers at work with Naphtali's boundary Ginnosar the translation's word for 34:11's sea; the sea as a border two ways; the Jordan two ways; agency asked of 34:18 and refused, the steward kept; the Canaanites' title claim from the heading; Rekem the Mishnah's east = the translation's Kadesh-barnea; the land-bound rule from Deuteronomy 12:1-2's adjacent verse — a fifteenth DATA row added) → the types by script (3 tape kinds, 2 case kinds, 2 effects, no registry row, the 61st daemon boot with the class named — relayed at 34:13 in 36:5's form, D2's question; nine CALL edges) → the gates to FAIL (2 + 10) → the runner 56/56 on the SIXTH run (four readings: TWO CENSUSES OF ONE LABEL — the exact pair "the land Canaan" one seat, the side-word's bare token five, Elizaphan's lemma six; THE EIGHT NAMES A MIXED MEASURE — eight by token, ten by lemma; and a dict's eager default) with the scene (18 persons) and the narrative (3 writes, 2 entities, 12 rows) matched first run → the daemon gate GREEN first run; the dependency gate's TWO demands read (family VIA at six seats — 34:5's brook the inheritance's consonants, a homograph by sense; offerings FALSE at 34:27 — Shelomi) → the recorder once → the stitcher's census as predicted to the number → the literals, CW1-CW9, CP1 retyped 136 → 148 → THE TAPE: RUN PREDICTED AND MATCHED FIRST RUN, THE REST 13b's exactly, 10/10 on the SECOND run (one miss read — a row's optional column by key at CP7's view: the first writer's shape is the table's) → the probe gates (register_probes R3 3 → 4 and R6 ROWS 3 → 4 retyped from the gate's print) → the journal gate GREEN → THE REGISTER GATE --strict GREEN with the Num 34 seat PAID (the declaration deleted, key and body) → the cursor probes 6/6 → the sweep → the records.
THE RECORDS: NUMBERS_WALK.md "Sitting 14b — AS BUILT"; the docket; the reading ledger's CORRECTIONS block (the eight names; Elizaphan; the side-word; the article's one seat confirmed); COMPILE_DEBT.md's sitting-14 box PAID and the 14b box (i)-(viii); MIDDOT's docket entries (the adjacent verse classing the commandments; "only" excludes the two who divide; agency refused; a verbal analogy not received; one word read two ways on a border; one border against the Jordan Canaan's; the lottery's two receptacles; a likeness refused by what the first case needed); MISHNAH_TOPICS (Gittin 1:1-2; Sheviit 6:1, 9:2); RESEARCH_LOG.md's seven findings; THE_STEPS' sitting-14b paragraph; THE_BRIEFING's scoreboard bullet; World/RESUME.md; the forms copied; memory (numbers-in-order-ruling.md, MEMORY.md, step9-exam-era.md's lessons head); the recovery file's section 15; this entry.
NEXT on the ruling: CHAPTER 35 — THE REFUGE CITIES' READING (35:1-34) on the reading shape (the recovery file's section 5; NUMBERS_WALK "Sitting 14" the form; the forms in World/step9/forms_numbers_walk/ — bor_dump.py, bor_measure1.py, bor_measure2.py, bor_ink.py, bor_legs.py, bor_rows_onkelos_a/b.py, write_bor_ledger.py, write_bor_manifest.py, seat_bor.py, bor_chain.sh, patch_overrides_bor.py, write_bor_records.py, assert_driver.py — copied to the scratchpad and adapted): THE SIFREI RETURNS at 35:9 — piskaot 159-161 BY POSITION (the heads checked against the rows' own citations; the export scanned in the four citation forms for rows citing 35 — the Levite cities 35:1-8 may be silent); Onkelos whole (34 verses); THE PARSER measured first on 35:4-5's cubits (a thousand, two thousand — 4b's owed line "Num 35:5's two thousand cubits"; the dual noun), 35:6's forty-two and six, 35:7's forty-eight, 35:14's three and three; the crowns to look for: the Levite cities' measure (the Talmud's square at Eruvin 51a; Sotah 27b), the six refuge cities (the three beyond the Jordan — 32's grant), the murderer and the manslayer (35:16-24 the instruments; the blood-avenger; the congregation's judgment), the high priest's death as the term (35:25, 28 — a timer keyed to an office's holder: the priesthood engine's hour), the two witnesses (35:30), no ransom (35:31-32), the land polluted by blood (35:33-34); the register gate's seats in the chapter (35:6-8's counts) declared NONE at the reading, paid or held at the compile — THEN its compile (15b) on the compile shape with the register gate at the gates step — NEVER THE NEXT READING FIRST.
POST-COMPACTION REREADS (mandatory, first sitting): the recovery file logic/pre_logic_methods_2026-07-28/RECOVERY_new_thread_2026-09-12.md whole (its section 5 THE READING SITTING; its sections 14 and 15) + numbers-in-order-ruling.md + this entry + NUMBERS_WALK.md "Sitting 14" (the reading's form) + "Sitting 14b — AS BUILT" (the compile's) + THE_STEPS Step 2 + Step 5 + the compiler block; memory's STANDING LESSONS head (the sitting-14b paragraph first). WATCHES: as #155's + TWO CENSUSES OF ONE LABEL + A MIXED MEASURE IS NO MEASURE + THE ROW'S SHAPE FOLLOWS THE FIRST WRITER'S + A REGISTER SEAT IS PAID BY ROWS + THE GATE CATCHES THE READING'S HOMOGRAPH AT ITS OWN SEAT + THE DICT'S EAGER DEFAULT.
''' % (NR, NR, CELLS)
append(f'{ROOT}/logic/pre_logic_methods_2026-07-28/PROMPT_continue_solo_era_2026-08-06.md', SD, 'COMPACTION POINT #157')

# 10. the recovery file — section 15
REC = '''
## 15. ADDENDUM (2026-09-13, at sitting 14b's close — the state doc's COMPACTION POINT #157; this supersedes section 14's NEXT, which is kept as written)

SITTING 14b DONE: CHAPTER 34 (the borders) COMPILED AND ON THE TAPE — NUMBERS 1:1-34:29 READ, FROZEN, COMPILED AND ON THE TAPE (27 by THE TENT); 56 runners
(cold_run_borders.py the 56th, 56/56), 61 daemons (law_borders the 61st, given_at 34:1, installed_by boot with the class named — a law in the divine voice
relayed at 34:13 in 36:5's form, D2's question); RUN (1277, 66, 52, 0, 12, 1525, 32, 318, the four pairs, 121); the sweep %s/%s at %s; EVERY GATE GREEN
(the tape 10/10, the journal gate with population 148 = rows 148, the register gate --strict with THE NUM 34 SEAT PAID BY ROWS and its declaration
deleted, the daemon and dependency gates, every probe file, vocab_lint 0). NUMBERS_WALK.md "Sitting 14b" (design + as-built) the record; COMPILE_DEBT.md's
sitting-14b box (i)-(viii) the owed items (the dividers' debit OPEN to Joshua 14:1, 17:14, 19:51 — THE READBACK's; the relay's form D2's; Numbers 27:12-23
uncompiled met again; Deuteronomy's and Joshua's seats; the shelf's own border lines as DATA; the homographs filed; the display layer). THE DESIGN'S FOUR
DECISIONS: the four sides ONE STATUS ON THE LAND (a DATA row, nothing on the people); the lot by CALL; THE RESTATEMENT WRITES NOTHING (a run citation of
the grant on the tape); the dividers a status and a debit on the standing party of 32:28 AND TWELVE NAMED ROWS in the population table — the first register
paid by rows since the table was built at 26. THE FORMS of 14b are in World/step9/forms_numbers_walk/ (bor_compile_recon.py, bor_compile_measure.py,
bor_docket_scan.py, bor_docket_A-D.py, write_bor_docket.py, add_types_bor.py, bor_runner_measure.py, bor_part1-4.py — the runner assembled by cat,
patch_seq_literals_bor.py, bor_design.md, bor_asbuilt.md, write_bor_compile_records.py, seq_record.py, seq_stitch.py). Still UNCOMMITTED since a42f518;
commit only on "commit push".

NEXT: CHAPTER 35 — THE REFUGE CITIES' READING (35:1-34) on section 5's reading shape (the measurement pass first: the parser on 35:4-5's cubits — 4b's
owed line — and the cities' counts at 35:6-7 and 35:14; THE SIFREI RETURNS at 35:9, piskaot 159-161 by position with the heads checked against the rows'
own citations, the export scanned in the four citation forms for rows on 35:1-8; Onkelos whole; one ledger script with coverage computed, one manifest
script with checks cut from the store's bytes, one seat script, the ritual, the corpus rebaked, the stamp row), THEN its compile (15b) on section 5's
compile shape with the register gate at the gates step (the chapter's count lines declared at the reading, paid or held at the compile) — NEVER THE NEXT
READING FIRST. Before the reading: reread NUMBERS_WALK.md "Sitting 14" (the reading's form) and "Sitting 14b — AS BUILT" (the compile's), THE_STEPS Step 2
+ Step 5 + the compiler block, memory's STANDING LESSONS head.
''' % (NR, NR, CELLS)
append(f'{ROOT}/logic/pre_logic_methods_2026-07-28/RECOVERY_new_thread_2026-09-12.md', REC, '## 15. ADDENDUM (2026-09-13, at sitting 14b')
print('records written')
