import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE NUMBERS WALK 13b (2026-09-12): THE RECORDS at the compile's close — NUMBERS_WALK.md "Sitting 13b — AS BUILT" (from jou_asbuilt.md with the sweep's
# line filled from the sweep's own print), COMPILE_DEBT.md's sitting-13b box (the sitting-13 box PAID + the new debts), MOVE_CATALOG.md M-30,
# MIDDOT.md's docket entries, MISHNAH_TOPICS' Zevachim 14 mark, RESEARCH_LOG.md's entry, THE_STEPS' paragraph, THE_BRIEFING's bullet, World/RESUME.md's
# line, memory (three files), the state doc's #154, the recovery file's section 13. Every append anchored; every file linted after by the caller.
# Idempotent on the markers. write_gad_compile_records.py's form.
import re, os, sys
ROOT = _ROOT; SP = os.path.dirname(os.path.abspath(__file__)); MEM = '<memory>'
sweep = open(f'{SP}/sweep_jou.out', encoding='utf-8').read()
m = re.search(r'(\d+)/(\d+) runners? green.*?([\d,]+) graded cells', sweep, re.S) or re.search(r'(\d+)/(\d+).*?([\d,]+) graded', sweep, re.S)
assert m and m.group(1) == m.group(2), 'the sweep\'s print has no green line: read it'
NR, CELLS = m.group(1), m.group(3)
SWEEP_LINE = '%s/%s runners green, %s graded cells (12b\'s 6218 + the journeys runner\'s 53; cold_run_journeys.py 53/53); the dependency and daemon gates inside it GREEN' % (NR, NR, CELLS)
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
asb = rd(f'{SP}/jou_asbuilt.md').replace('SWEEP_LINE', SWEEP_LINE)
assert 'SWEEP_LINE' not in asb
append(f'{ROOT}/World/step9/NUMBERS_WALK.md', asb if asb.startswith('\n') else '\n' + asb, '## Sitting 13b — AS BUILT')

# 2. COMPILE_DEBT — the sitting-13 box PAID + the sitting-13b box
DEBT = '''## SITTING 13b — THE COMPILE OF THE JOURNEYS (2026-09-12; NUMBERS_WALK.md "Sitting 13b" design + as-built; the owner: "Go" after the #152 rereads; the
## sitting-13 box (a)-(n) PAID — (a) the stations a DATA ROW built from the DB, the tape's camps read against it; (b) the writing the chapter's own act,
## the four writings a DATA row; (c) the run of Exodus 12:12 the act's FIRST telling — no debit stood open, a status on Egypt written; (d) the date
## checkpoint CZ5 — the marker's (40, 5, 1) and the ages' checksum; (e) Arad a run citation, CZ6; (f) the command's daemon with two debits OPEN BY DESIGN,
## the three objects by CALL and by OWED; (g) the lot by CALL, cited not rewritten, CZ7; (h) the negative arm a DATA row with the shelf's three runs;
## (i) the register gate's two seats measured — the mouth-phrase not a class, nothing to pay; (j) the Deuteronomy divergence a DATA row with the shelf's
## retreat; (k) the edges declared — ten CALL, one OWED, the census's three demands read; (l) the docket 196 rows by the union rule with the cut declared;
## (m) the display layer as filed; (n) no parser rule): cold_run_journeys.py 53/53 (five cells, ten engines CALLED — exodus_story, pesach, beha, shelach,
## chukat, balak, second_census, gad_reuben, erection, holiness), law_journeys the 60th daemon (given_at Num 33:50; installed_by boot with the class named
## — a law in the divine voice spoken in the plains of Moab), the tape's THREE lines page_order at (40, 6, 1) with NO close and TWO debits OPEN BY DESIGN;
## RUN (1274, 66, 52, 0, 12, 1522, 31, 318, four pairs, 121) predicted and matched first tape run; THE REST 12b's exactly; CZ1-CZ9 MATCH; THE REGISTER
## GATE --strict GREEN with nothing to pay; every gate green. THE NEW DEBTS: (i) LEVITICUS 26:1-2's OWN COMPILE — the idols, the graven image, the pillar,
## the figured stone; the sabbaths and the sanctuary: NO CELL in the tochacha runner (its span declares 26:1-46; the dependency gate's own advisory names
## 26:1-2 uncited); journeys → tochacha OWED on the figured stone and the high places' curse (26:30 — 'your high places' in the tochacha's token table
## only); Megillah 22b:11-13 (Ulla's stone floor; the outstretched limbs) the first exam rows for that sitting; (ii) THE DISPOSSESSION AND THE IMAGES —
## israel_people's commanded dispossess_the_inhabitants_and_possess_the_land and destroy_their_images stand OPEN on the tape by design: the runs Joshua's
## (Joshua 4 the crossing's purpose — Sotah 34a:5; 23:13 and Judges 2:3 the negative arm's runs; 2 Kings 23 the images' last): STEP 6 THE READBACK's
## items beside the crossing's debit of 32 and Caleb's Hebron; (iii) THE INSTALLED_BY CLASS (D2, the second pass): law_journeys installed_by boot with
## the class named — a law in the divine voice in the plains of Moab; law_musafim at 28:1 in the same plains stands called_from_the_tent (9b's choice):
## the two settings side by side, D2 to unify; (iv) DEUTERONOMY — 10:6-7's order and Moserah (the DATA row the_deuteronomy_order; the Sifrei on
## Deuteronomy not declared), 1:3's cardinal date by the number reader (a date checkpoint at Deuteronomy takes both readers), 34:7's 120 (Moses' death),
## 11:31's "when you pass over the Jordan", 7:5 and 12:2-3's iconoclasm lists (by CALL into the erection runner now; Deuteronomy's own compile later);
## (v) JOSHUA 5:10-12 — the morrow of the Passover at the run's other end and the manna's ceasing: the exodus story's manna (Exodus 16:35 'forty years')
## carries no timer to (41, 1, 16) — the provision's end fires at THE READBACK; (vi) THE HOMOGRAPHS FILED FROM THE RUNNER MEASURE — "that is Kadesh" /
## "it is holy" (three of the pair's five seats; the reading ledger's CORRECTIONS block appended) and "the wilderness of Etham" / "speaking with them"
## (Exodus 34:33): a bare pair is not a place name without its prefix — the census lesson; (vii) THE DISPLAY LAYER — as the sitting-13 box's (m). Filed
## this sitting for the walk's watches (memory): A GLOBAL COUNT IS ANY COUNT OVER A LEDGER (CV2 and CX2 moved on Israel's commanded entries — grep every
## count over one effect on one party, not the entity and close counts alone), THE VIA ROW CARRIES ITS TARGET (`via:` — the gate reads "VIA None" without
## it), THE TAPE'S VALUE HEAD IS MATCHED BY PREFIX (the plains' status runs past the head's split), A TOKEN TYPED FROM MEMORY FALLS ON ITS OWN LESSON'S
## VERSE (Joshua 23:13's lamed), THE HAND'S TALLIES AGAINST THE MACHINE'S COLUMNS (twenty / eighteen typed where the DATA row counts eighteen / seventeen).
'''
append(f'{ROOT}/World/step9/COMPILE_DEBT.md', DEBT, '## SITTING 13b — THE COMPILE OF THE JOURNEYS')

# 3. MOVE_CATALOG — M-30
M30 = '''
## M-30 — THE RETREAT (two records of one event at two places are reconciled by a movement the ink does not narrate, and the ink's own count of stations is the check: "did Aaron die in Moserah? did he not die at Mount Hor? rather, from where Aaron died they retreated seven stations until Moserah")

**The move (2026-09-12, THE NUMBERS WALK 13b — Numbers 33:30-38 against
Deuteronomy 10:6-7):** the itinerary sets Aaron's death at Mount Hor
(33:38) with Moseroth seven camps earlier (33:30) and Bene-jaakan after
it (33:31); Deuteronomy 10:6 runs "from Beeroth-bene-jaakan to Moserah;
THERE Aaron died" — the two names in the other order and the death at
the other place. The tradition does not choose a seat and drop the
other; it reads a MOVEMENT between them that neither text narrates:
after the king of Arad came against them at the news of the death, they
RETREATED seven stations back to Moserah, and the mourning was renewed
there — so Deuteronomy's "there" is the place of the second mourning,
not the death (Seder Olam Rabbah 9:2; the chukat runner's row moserah =
the_retreat_of_seven_stations, sitting 6b). THE CHECK IS THE INK'S OWN
COUNT: Moseroth is the 27th place on the list and Mount Hor the 34th —
seven camps apart by index, computed at the reading and asserted at the
compile (cold_run_journeys.py: PLACES_EN.index('Moseroth') + 7 ==
PLACES_EN.index('Mount Hor')); the shelf's seven is the itinerary's
seven. **What separates it:** from M-22 (a rule generalized across
seats) and from the proleptic name (Hormah named at 21:3, used at
14:45 — one name, two times): here two seats disagree on WHERE one
event happened, and the reconciliation is a narrated-nowhere journey
whose length the list itself supplies. Its kin on the shelf: the
"backward" count of Moses' death from the crossing's marker (Kiddushin
38a:5-6 — the tenth of Nisan less thirty-three days) — a date computed
back along a run; and Rosh Hashanah 2b:13-3a:3's ordering of the
fortieth year's events by "after he had slain Sihon". **Machine form:**
the two orders carried as one DATA row (the_deuteronomy_order — the
retreat's arm and the ink-alone arm), the count asserted on the list's
indices, the tape untouched (the death's marker stands at 20:28; no
second line for the retreat, which the ink never narrates — a
retelling never writes an act twice). **Middah correspondence:** none
named by the source; the form is a reconciliation of two seats (the
thirteenth middah's family — two verses that contradict, resolved by a
third thing — here the third thing is a walk, and the resolver is the
list's own arithmetic).
'''
append(f'{ROOT}/logic/MOVE_CATALOG.md', M30, '## M-30 — THE RETREAT')

# 4. MIDDOT — the docket's entries (before the Exodus block campaign section)
MID = '''- THE JOURNEYS' DOCKET (THE NUMBERS WALK sitting 13b, 2026-09-12; logic/oral_triage/num_33_journeys_exam_2026-09-12.md — 196 rows; the rules about rules the
  docket carries, each at its row):
  · THE VERBAL ANALOGY AT A DATE — "THE FORTIETH YEAR" / "THE FORTIETH YEAR" (Rosh Hashanah 2b:10-11; I2, the gezerah shavah — the shared word): 33:38's
    date names its epoch ("of the going out from the land of Egypt"), Deuteronomy 1:3's does not; the tradition carries the epoch across by the shared
    phrase in Rav Pappa's form ("the twentieth year" / "the twentieth year") — a TRANSFER with its teacher named; the engine's Calendar reads both dates
    in one year by its own registered epoch, so the transfer is reproduced without being assumed.
  · TWO VERSES THAT COME AS ONE TEACH NO PRECEDENT (Kiddushin 37b:6-9 — the king's "when you come … and inherit and settle" and the first fruits' the same
    form; a rule about rules, no I-code among the thirteen): when the Torah states a qualification at two seats, the pair does not generalize to a third
    — the two schools of R. Yishmael split on whether the pair was necessary (each seat needed for its own sake) or superfluous (and so teaching).
  · THE FOUR SENSES OF "KI" AND "DO NOT READ" (Rosh Hashanah 3a:2 — Reish Lakish's four: if, perhaps, but, because; R. Abbahu's "do not read 'and they
    saw' but 'and they were seen'"): a lexical rule and a vocalization rule read together on 20:29 to place the clouds' departure at Aaron's death — the
    ground of the chukat runner's row arad_heard.
  · THE HEH FOR THE LAMED (Yevamot 13b:6 — R. Nechemya and the school of R. Yishmael: a word needing a lamed at its head takes a heh at its end — Elimah,
    Mitzraimah, Diblathaimah): a grammar rule of the ink, its examples the itinerary's own tokens (33:9, 33:46); the list keeps the ending.
  · A DATE COMPUTED BACKWARD FROM A RUN'S MARKER (Kiddushin 38a:5-6; Seder Olam Rabbah 10:2): Moses' death on the seventh of Adar from the tenth of Nisan
    (Joshua 4:19) less thirty days' mourning and three days' preparation — the shelf's own retrograde marker (Pesachim 6b:7's kin), with "this day"
    (Deuteronomy 31:2) closing the count to the day (38a:7; Exodus 23:26 "the number of your days I will fill").
  · THE RETREAT (Seder Olam Rabbah 9:2 — M-30): two seats of one death reconciled by a movement the ink does not narrate, the list's own count the check.
  · THE PRIVATE ALTAR'S ERAS DECIDE A SENSE (Mishnah Zevachim 14:4-8): "high places" in the Mishnah are Israel's own altars by era — permitted, forbidden,
    permitted, forbidden, forbidden forever; 33:52's "their high places" the Canaanites' to demolish (Leviticus 26:30's curse in the same verb): one word,
    two objects, the docket's topic rows read to tell them apart and the gemara cut as another runner's.
'''
insert_before(f'{ROOT}/logic/MIDDOT.md', '## Exodus block campaign', MID, "THE JOURNEYS' DOCKET (THE NUMBERS WALK sitting 13b")

# 5. MISHNAH_TOPICS — Zevachim 14:4-8 read
p = f'{ROOT}/logic/MISHNAH_TOPICS.md'; s = rd(p)
old = '· 14 offering outside; the altar-history eras\n'
if 'ch 14 mishnayot 4-8 READ 2026-09-12' not in s:
    assert s.count(old) == 1, s.count(old)
    s = s.replace(old, "· 14 offering outside; the altar-history eras — ch 14 mishnayot 4-8 READ 2026-09-12 (THE NUMBERS WALK 13b, the journeys' docket: the private altars' eras decide the SENSE of Numbers 33:52's high places as the Canaanites', not Israel's; the gemara 112b-119b sized at 265 segments and cut as the erection runner's docket)\n")
    wr(p, s); print('  marked', p)

# 6. RESEARCH_LOG — the findings
RL = '''
## 2026-09-12 — THE JOURNEYS' COMPILE (THE NUMBERS WALK sitting 13b): TWO HOMOGRAPHS THE RUNNER MEASURE FOUND; SEDER OLAM'S MANUSCRIPTS ON AARON'S MONTH;
## THE EXPORT'S CHAPTER HEADINGS AS ROWS; THE TAPE'S VALUE HEADS; THE GLOBAL COUNTS OVER A LEDGER

1. "THAT IS KADESH" / "IT IS HOLY". The reading's row counted "the identity clause at five Bible seats" for the pair הוּא קָדֵשׁ ("that is Kadesh" / "it is
holy"); the runner measure listed the five — Genesis 14:7 and Numbers 33:36 are the PLACE ("En-mishpat, that is Kadesh"; "the wilderness of Zin, that is
Kadesh"), Exodus 30:32, Leviticus 25:12 and 27:30 read "it is HOLY" (the anointing oil, the jubilee, the tithe). The same consonants, another word, told by
the vowel points and the sense; the reading ledger's CORRECTIONS block appended (append-only). The class: a two-token census on the consonants counts
homographs; the store's morphology (Np for the place) is the instrument.
2. "THE WILDERNESS OF ETHAM" / "SPEAKING WITH THEM". The bare pair מִדְבַּר אִתָּם has ONE seat in the Bible — Exodus 34:33, "when Moses finished SPEAKING with
them" (the participle מְדַבֵּר and the pronoun) — while the itinerary's "in the wilderness of Etham" (33:8) carries its prefix (בְּמִדְבַּר). A place-name census
that strips the prefix finds another word; the prefixed form is the seat. The reading's claim ("each name one seat") holds for the prefixed form.
3. SEDER OLAM RABBAH ON AARON'S MONTH. The export's 10:2 reads "Miriam died on the tenth of Nisan, and Aaron on the FIRST OF AV, and Moses on the seventh of
Adar"; the translator's note records that the French manuscripts have "first of Tammuz" against the Talmud's placing. The ink fixes the month — 33:38's
ordinal [40, 5], the fifth month, Av — and the tape's marker at 20:28 is built from it: a manuscript variant on a date the Torah states in full is
OBSERVED and not adjudicated; the export's own editorial line that "the remaining 38 years are without record except for the list of stations (Numbers
33)" states the design's premise for the itinerary as a data list.
4. THE SEDER OLAM EXPORT'S HEADINGS AS ROWS. Its 9:1 and 10:1 are the strings "Chapter 9" and "Chapter 10", and 10:3 an editorial line ("This is where the
chapter ends and so does part 1 of Seder Olam") — three rows verdicted OUTSIDE, owed their verdicts like any row (8b's fifth defect class, the text under an
empty key, again).
5. THE TAPE'S VALUE HEADS. The checkpoint that reads the tape's sixteen camps against the itinerary's list split each status's value at its first comma,
semicolon, parenthesis or dash and matched the head by equality; the plains' status ("the plains of Moab across the Jordan of Jericho (22:1) — …") runs
on past the name, and the head fell to unmatched: the match is by PREFIX. A value's head is the daemon's own sentence, not the registry's name.
6. THE GLOBAL COUNTS OVER A LEDGER. Two earlier checkpoints (CV2 the count of commanded entries on israel_people and the newest entry's value; CX2 Israel's
other open commanded entries) moved by the chapter's two debits though entities and closes stood unmoved — the design's "none should move" had grepped the
entity and close counts alone. Widened: a global count is any count over a ledger; grep every count over one effect on one party before the tape run.
'''
append(f'{ROOT}/RESEARCH_LOG.md', RL, "THE JOURNEYS' COMPILE (THE NUMBERS WALK sitting 13b)")

# 7. THE_STEPS — the sitting-13b paragraph
STEPS = '''
SITTING 13b — THE COMPILE OF THE JOURNEYS (2026-09-12, on Brian's "Go" after the #152 rereads; World/step9/NUMBERS_WALK.md "Sitting 13b" design +
as-built; the state doc's #153 written before the docket). The measurements first: the parser reads the chapter's five numbers and no rule is owed (the
walk's second measured-zero probes step); the tape already carries the dated stations as thirteen markers and sixteen camps as statuses, Aaron's death
at 20:28 with the date and the age THIS chapter states, and no entry anywhere for the judgments on Egypt's gods; the tochacha runner has no cell on
Leviticus 26:1 or 26:30; the register gate has nothing to pay. THE DESIGN'S DECISION: the forty-two stations are a DATA ROW, not tape lines — a retelling
never writes an act twice, a year-one camp cannot carry the record's day, and the ink's own verb for the chapter is "wrote" — so the writing is the act
and the list its value. The docket 196 rows by the union rule (Rosh Hashanah 2b-3a, Kiddushin 37b-38a, Megillah 22b, Bava Batra 117a-122a credited,
Mishnah Zevachim 14:4-8, Seder Olam Rabbah 9-10; Zevachim's gemara SIZED at 265 segments and CUT as the private altar's docket — the five Mishnah rows
read whole to decide that sense): the fortieth year's walk in the shelf's own order with THE RETREAT OF SEVEN STATIONS reconciling Deuteronomy 10:6 and
the itinerary's own count agreeing (M-30 registered); the era's New Year proved from the chapter's date by the shelf's own chain of the three stamps;
the morrow of the Passover at both ends and the manna's forty years less thirty days from the tape's own marker; Moses' seventh of Adar computed
backward from a run's marker; "by the mouth of the LORD" as the kiss; the command's run at the crossing and the negative arm's runs on the shelf; the
figured stone at its ban with the cell uncompiled, filed. The types by script (three tape kinds, two exam kinds, two effects, no registry row; the 60th
daemon installed by boot with its class named — a law in the divine voice in the plains of Moab; ten edges by CALL and one OWED); the gates run to FAIL
and read; the runner's five cells 53/53 on the third run — two readings between (a token typed from memory on the lesson's own verse; two hand tallies
against the machine's columns); the dependency census's three demands past the imports read (the land's inheritance VIA the second census; king against
Molech a third time; the arm's own comparison INTERNAL); THE LEDGER ON THE TAPE: one status on the people valued the forty-two, one status on Egypt for
the run of Exodus 12:12 told here alone (the firstborn's plague left open — a burial is no removal), two debits on the people OPEN BY DESIGN to Joshua's
runs, the lot's debit cited and not rewritten, no close; the RUN tuple predicted in the design and matched first tape run, THE REST 12b's exactly, the
nine checkpoints all MATCH on the second run after three honest misses (two global counts over Israel's commanded entries the design had not grepped; a
value head matched by prefix); the recorder once, the stitcher's census as predicted to the number; every probe gate, the daemon, dependency, journal and
register gates green; the sweep 55/55. Numbers 1:1-33:56 read, frozen, compiled and on the tape. Next: chapter 34 — the borders' reading, then its
compile, never the next reading first.
'''
insert_before(f'{ROOT}/THE_STEPS.md', '## THE FINDINGS LOOP + THE STAMP LAW (owner-approved 2026-08-31)', STEPS, 'SITTING 13b — THE COMPILE OF THE JOURNEYS')

# 8. THE_BRIEFING — the scoreboard bullet
BRIEF = '''- **THE JOURNEYS COMPILED — SITTING 13b DONE: THE ITINERARY IS A RECORD WRITTEN AT THE RUN'S END — THE FORTY-TWO STATIONS A DATA LIST (NO CAMP WRITTEN TWICE), THE RUN OF EXODUS 12:12 TOLD HERE ALONE AS A STATUS ON EGYPT, THE COMMAND'S TWO DEBITS OPEN BY DESIGN TO JOSHUA, AND THE SHELF'S RETREAT OF SEVEN STATIONS EQUAL TO THE LIST'S OWN COUNT (2026-09-12).** Chapter 33 compiled on the walk's compile shape: cold_run_journeys.py 53/53 (five cells, ten engines called), law_journeys the 60th daemon; three lines on the tape at the counter's day — the writing (its value the forty-two, built from the ink), the departure retold with the judgments on the gods (Exodus narrates the firstborn and never the gods; the itinerary alone records that run, forty years on; the firstborn's plague stays open, a burial is no removal), the command in the divine voice (dispossess and possess; destroy the figured stones, the molten images and the high places — the figured stone's own ban at Leviticus 26:1 found UNCOMPILED and filed; the lot's debit of chapter 26 cited, not rewritten). The dates checkpointed against the tape's own markers (the departure the exodus marker's; Aaron's death the marker at 20:28 built from this chapter, 123 = 83 + 40). The docket 196 rows: Seder Olam's fortieth-year walk with THE RETREAT OF SEVEN STATIONS to Moserah — and Moseroth stands seven camps before Mount Hor on the list (M-30); Rosh Hashanah's proof of the era's New Year from this chapter's date, reproduced by the engine's Calendar; the morrow of the Passover at both ends; Moses' seventh of Adar computed backward; the private altar's eras read to decide the sense of "high places" and the gemara cut as another runner's. RUN (1274, 66, 52, 0, 12, 1522, 31, 318, four pairs, 121) predicted and matched first run; every gate green; the sweep %s/%s at %s. Numbers 1:1-33:56 read, frozen, compiled and on the tape. Next: chapter 34, the borders.
''' % (NR, NR, CELLS)
insert_after_line(f'{ROOT}/THE_BRIEFING.md', '## SCOREBOARD (as of 2026-09-12, latest)', BRIEF, 'THE JOURNEYS COMPILED — SITTING 13b DONE')

# 9. World/RESUME.md
RES = '''SITTING 13b DONE 2026-09-12 (THE COMPILE OF THE JOURNEYS 33:1-56; NUMBERS_WALK.md "Sitting 13b" design + as-built; the owner: "Go" after the #152 rereads): the docket 196 rows (Zevachim's gemara sized and cut; the retreat of seven stations — M-30; the era's New Year from the chapter's date; the morrow at both ends; the figured stone's ban uncompiled and filed); the types (three tape kinds, two exam kinds, two effects, no registry row; law_journeys the 60th daemon, installed by boot with the class named); cold_run_journeys.py 53/53 on the third run; THE FORTY-TWO A DATA ROW built from the DB (eighteen only here; Moseroth seven before Mount Hor); the tape's three lines — the writing, the judgments on the gods (Exodus 12:12's run told here alone), the command's two debits OPEN BY DESIGN; RUN (1274, 66, 52, 0, 12, 1522, 31, 318, four pairs, 121) predicted and matched first tape run, 10/10 on the second; every gate green; the sweep %s/%s at %s. NUMBERS 1:1-33:56 READ, FROZEN, COMPILED AND ON THE TAPE. NEXT: chapter 34 — the borders' reading, then its compile.
''' % (NR, NR, CELLS)
append('<world-link>/RESUME.md', RES, 'SITTING 13b DONE 2026-09-12')

# 10. memory — numbers-in-order-ruling.md (a line + the description), MEMORY.md (the numbers line), step9-exam-era.md (the lessons head)
p = f'{MEM}/numbers-in-order-ruling.md'; s = rd(p)
if 'SITTING 13b DONE 2026-09-12' not in s:
    s = s.rstrip('\n') + '\nSITTING 13b DONE 2026-09-12 — THE COMPILE OF THE JOURNEYS 33:1-56 (NUMBERS_WALK.md "Sitting 13b" design + as-built; the owner: "Go" after the #152 rereads; the state doc\'s #153 before the docket, #154 at the close): THE PROBES STEP A MEASURED ZERO (the walk\'s second); the docket 196 rows by the union rule (12 link in 9 works + Rosh Hashanah 2b-3a, Kiddushin 37b-38a, Megillah 22b, Bava Batra 117a-122a credited, Mishnah Zevachim 14:4-8, Seder Olam 9-10; Zevachim 112b-119b SIZED at 265 and CUT as the private altar\'s docket; LAW 7 / DERIVATION 31 / DISPUTE 6 / CONTEXT 149 / OUTSIDE 3) — THE RETREAT OF SEVEN STATIONS (Seder Olam 9:2) equal to the list\'s own count, M-30; the era\'s New Year from 33:38 with Deuteronomy 1:3 (Rosh Hashanah 2b:9-11, the verbal analogy taught); the morrow at both ends (Kiddushin 37b-38a); Moses\' seventh of Adar backward from Joshua 4:19; the kiss (Bava Batra 17a:3); the figured stone\'s ban UNCOMPILED (Megillah 22b:11-13 filed); the types by script (3 tape kinds, 2 case kinds, 2 effects — journeys_recorded, judgments_executed_on_their_gods; NO registry row; law_journeys the 60th daemon, given_at 33:50, installed_by boot with the class named — the divine voice in the plains of Moab; ten CALL edges, tochacha OWED — Leviticus 26:1-2\'s own compile a debt); cold_run_journeys.py 53/53 on the THIRD run (a Joshua token typed from memory — the lamed; two hand tallies against the machine\'s columns); THE FORTY-TWO A DATA ROW built from the DB (Rameses + forty-one camps; eighteen only here — seventeen by lemma + the Red Sea; Moseroth seven before Mount Hor by index; eighteen first tellings, seventeen tape witnesses); the dependency census\'s three demands read (family VIA second_census — the `via:` target the gate reads; sanctions FALSE — king against Molech a third time; the AS_WHEN pointer 33:56 INTERNAL); THE LEDGER SHAPE: journeys_recorded on the people (the list its value), judgments_executed_on_their_gods on Egypt (Exodus 12:12\'s run told here alone — the firstborn\'s plague OPEN, a burial no removal), commanded ×2 on the people OPEN BY DESIGN to Joshua\'s runs, the lot\'s debit CITED not rewritten, NO close, no line for 33:38-40 (the tape\'s 20:28 and 21:1 checkpointed — the marker (40, 5, 1) built from 33:38, 123 = 83 + 40); the recorder once; the stitcher\'s census as predicted to the number (on tape 1274, kinds 819, subjects 270); RUN (1274, 66, 52, 0, 12, 1522, 31, 318, four pairs, 121) PREDICTED AND MATCHED FIRST TAPE RUN, THE REST 12b\'s exactly; 10/10 on the SECOND run (THREE MISSES READ: CV2 and CX2 — global counts over Israel\'s commanded entries moved by the two debits, retyped AS OF the sitting; CZ2\'s value head matched by prefix); every probe gate green (census 187, installation 6 with I5 60, clock 22, sequence 4, view 6, population 9, journal 7, cursor 6, register 7 with R3 retyped 2 → 3 daemons); the daemon (417 WRAPPED), dependency (450 edges, 173 pointers), journal (13,353 rows) and register (nothing to pay; the Num 34 why refreshed) gates GREEN; the sweep %s/%s at %s. NUMBERS 1:1-33:56 READ, FROZEN, COMPILED AND ON THE TAPE (27 by THE TENT). UNCOMMITTED since a42f518. NEXT: CHAPTER 34 — the borders\' reading (34:1-29; the Sifrei silent to 35:8; the parser measured on 34:13\'s nine and 34:15\'s two), THEN its compile (14b) — never the next reading first.\n' % (NR, NR, CELLS)
    old_d = "NEXT chapter 33's reading, then its compile. The body holds"
    assert s.count(old_d) == 1, s.count(old_d)
    s = s.replace(old_d, "NUMBERS 1:1-33:56 READ, FROZEN, COMPILED AND ON THE TAPE (55 runners, 60 daemons; 208 units, standing 2136, hash unmoved; sitting 13b's RUN (1274, 66, 52, 0, 12, 1522, 31, 318, four pairs, 121)); NEXT chapter 34's reading (the borders), then its compile. The body holds")
    wr(p, s); print('  memory: numbers-in-order-ruling.md')
p = f'{MEM}/MEMORY.md'; s = rd(p)
old = [l for l in s.split('\n') if l.startswith('- [⚠ NUMBERS IN ORDER FROM 1:1]')]
assert len(old) == 1, len(old)
new = "- [⚠ NUMBERS IN ORDER FROM 1:1](numbers-in-order-ruling.md) — OWNER-RULED 2026-09-09: the chapter walk from 1:1 at the parashah grain (map World/step9/NUMBERS_WALK.md; chapters 9, 15:32-41, 27, 36 frozen at THE TENT and SKIPPED); ⚠ OWNER-RULED 2026-09-10 READ THEN COMPILE PER PORTION, never read ahead; CHAPTER NUMBERS, not portion names. NUMBERS 1:1-33:56 READ, FROZEN, COMPILED AND ON THE TAPE (sittings 1-13b; 55 runners, 60 daemons, RUN (1274, 66, 52, 0, 12, 1522, 31, 318, four pairs, 121); 208 units, standing 2136, hash 8b8fff1fa28953af unmoved; THE CLOSE LINE built 2026-09-12); 13b (2026-09-12, #154): THE FORTY-TWO A DATA ROW built from the DB (no camp written twice), the run of Exodus 12:12 told at 33:4 alone as a status on Egypt, the command's two debits OPEN BY DESIGN to Joshua, the figured stone's ban at Leviticus 26:1 found UNCOMPILED and filed, THE RETREAT OF SEVEN STATIONS (Seder Olam 9:2) equal to the list's own count — M-30. COMMITTED a42f518 (2026-09-11); sittings 8-13b UNCOMMITTED. THE REGISTER GATE (register_census.py --strict) AT EVERY COMPILE SITTING'S GATES STEP. NEXT: CHAPTER 34 — the borders' reading (34:1-29; the Sifrei silent to 35:8; the parser measured on 34:13's nine and 34:15's two), then its compile."
if old[0] != new:
    s = s.replace(old[0], new); wr(p, s)
size = len(rd(p).encode('utf-8')); assert size < 17000, size; print('  memory: MEMORY.md', size, 'bytes')
p = f'{MEM}/step9-exam-era.md'; s = rd(p)
LESSON = "⚠ THE NUMBERS WALK sitting 13b — THE JOURNEYS' COMPILE (2026-09-12): A GLOBAL COUNT IS ANY COUNT OVER A LEDGER — CV2 (the commanded entries on israel_people and the newest one's value) and CX2 (Israel's other open commanded entries) moved by the chapter's two debits while entities and closes stood unmoved: the design's \"none should move\" had grepped the entity and close counts alone; grep every `len(cmd_v)` and `sum(1 for e in isr_cmd` kin — a count over one effect on one party — before the tape run. THE VIA ROW CARRIES ITS TARGET — a VIA edge typed without `via: second_census` reads \"VIA None\" at the gate: copy the form's row whole. THE TAPE'S VALUE HEAD IS MATCHED BY PREFIX — the plains' status runs on past the head's split (\"the plains of Moab across the Jordan of Jericho (22:1) — …\"): a value's head is the daemon's own sentence, not the registry's name. A TOKEN TYPED FROM MEMORY FALLS ON ITS OWN LESSON'S VERSE — Joshua 23:13's \"from before you\" carries the lamed where 33:52's does not; the print had it. THE HAND'S TALLIES AGAINST THE MACHINE'S COLUMNS — the DATA row's first tellings and witnesses typed twenty / eighteen where the row counts eighteen / seventeen: assert the row's own sums, then read them. THE FOOTER'S DAEMON COUNT MOVES BY given_at ALONE (R3 2 → 3 at law_journeys's registration — retyped from the gate's print, a second time). A TWO-TOKEN CENSUS ON THE CONSONANTS COUNTS HOMOGRAPHS — \"that is Kadesh\" / \"it is holy\" (three of five seats), \"the wilderness of Etham\" / \"speaking with them\" (Exodus 34:33): the morphology and the prefix decide; the reading ledger's correction APPENDED. THE FORTY-TWO AS A DATA ROW — a retelling never writes an act twice; the record's day is the writing's, the camps' days their first tellings'; the list built from the verbs' after-tokens (the subject skipped, the next verb the stop) and checked against the tape's statuses by prefix. THE SIZED-AND-CUT RANGE — a topic range whose sense the Mishnah rows decide against the chapter is sized at the scan, cut, and the sizing kept on file (Zevachim 112b-119b, 265 segments). THE COMPILE SITTING'S SHAPE HELD with a measured-zero probes step: measurements → design → (no probe) → the state doc → docket (four parts) → types → gates to FAIL → runner (53/53 third run) → recorder (once) → stitcher → literals + CZ1-CZ9 → tape (10/10 second run; the RUN tuple first run) → probe gates → journal gate → register gate (nothing to pay; a stale why refreshed) → sweep → records.\n"
if "sitting 13b — THE JOURNEYS' COMPILE" not in s:
    a = '## STANDING LESSONS AND WATCHES (moved verbatim from the MEMORY.md index line on 2026-09-07 to keep the index under its size limit; the W4/W3/W2/W1/D9/G/E lesson tail as it stood)\n'
    assert s.count(a) == 1; i = s.index(a) + len(a); s = s[:i] + LESSON + s[i:]; wr(p, s); print('  memory: step9-exam-era.md')

# 11. the state doc #154
SD = '''
═══ COMPACTION POINT #154 (2026-09-12 — written at THE NUMBERS WALK sitting 13b's close; THE JOURNEYS 33:1-56 COMPILED AND ON THE TAPE; NUMBERS 1:1-33:56 READ, FROZEN, COMPILED AND ON THE TAPE, 27 BY THE TENT; EVERY GATE GREEN; A CLEAN COMPACTION POINT) ═══
STATE: 208 frozen units, standing 2136, hash 8b8fff1fa28953af UNMOVED (no unit touched this sitting); 55 runners (cold_run_journeys.py the 55th, 53/53), 60 daemons (law_journeys the 60th), the sweep %s/%s at %s graded cells; RUN (1274, 66, 52, 0, 12, 1522, 31, 318, the four pairs, 121) predicted and matched first tape run; THE REST 12b's exactly; the tape 10/10; every probe gate green (census 187, installation 6 with I5 60, clock 22, sequence 4, view 6, population 9, journal 7, cursor 6, register 7); the daemon gate (60 daemons, 417 WRAPPED), the dependency gate (450 edges, 173 pointers), the journal gate (13,353 rows; closed 121 = closes 121) and THE REGISTER GATE --strict (nothing to pay; the footer 36:13 DAEMONS with law_journeys; the Num 34 why refreshed) GREEN; vocab_lint 0. LAST COMMIT a42f518; UNCOMMITTED: sittings 8 through 13's paths, THE CLOSE LINE's, and this sitting's (World/step9/cold_run_journeys.py NEW; cold_run_sequence.py — the import, DAEMON_ORDER, RUN, PREVIOUS_RUN, NEWEST_RUNNER, PLACEMENT, CENSUS, the VERDICTS' CZ entries, CV2/CX2 retyped, the CZ1-CZ9 block, the three tape lines; event_vocabulary.yaml (+5), effect_vocabulary.yaml (+2), daemon_dispositions.yaml (law_journeys + the functions block), dependency_dispositions.yaml (the span, 13 edges, 1 pointer), installation_probes.py (I5 60), register_probes.py (R3), register_dispositions.yaml (the Num 34 why), DAEMON_INDEX.md, DEPENDENCY_INDEX.md, REGISTER_INDEX.md; logic/oral_triage/num_33_journeys_exam_2026-09-12.md NEW; logic/oral_triage/num_33_journeys_2026-09-12.md (the CORRECTIONS block appended); NUMBERS_WALK.md ("Sitting 13b" design + as-built); COMPILE_DEBT.md; MOVE_CATALOG.md (M-30); MIDDOT.md; MISHNAH_TOPICS.md; RESEARCH_LOG.md; THE_STEPS.md; THE_BRIEFING.md; World/RESUME.md; World/step9/forms_numbers_walk/ (this sitting's scripts copied in); the recovery file's section 13; this doc) — commit only on "commit push" (the NEVER-COMMIT set and the staging-by-exclusion form as before; ARCHITECTURE excluded).
THE SITTING (the owner: "Go" after the #152 rereads; NUMBERS_WALK.md "Sitting 13b" design + as-built; 1b's order held with a measured-zero probes step): THE MEASUREMENTS (the parser's five numbers read again, no rule owed; the tape's grounds — the dated stations thirteen markers, sixteen camps as statuses, NO entry for the judgments on the gods, the 20:28 event carrying this chapter's date and age; the tochacha runner without a cell on 26:1 or 26:30; the installed_by forms — no verse, boot the standing setting; the register gate on 33 empty; CZ free; the stations by lemma; the docket sized 461 and cut to 196 with the sizing on file); THE DESIGN — THE FORTY-TWO A DATA ROW, NOT TAPE LINES (a retelling never writes an act twice; the record's day the writing's; the ink's verb "wrote"); three lines, two debits OPEN BY DESIGN, the lot cited; CZ1-CZ9; the arithmetic; THE DOCKET 196 rows (four parts on disk; the crowns — the retreat of seven stations, the era's New Year from the chapter's date, the morrow at both ends, Moses' seventh of Adar backward, the kiss, the crossing's purpose and the thorns' runs, the figured stone at its ban, the private altar's eras deciding a sense, the last camp's three parasangs, Arad's identity, the directional ending, Seder Olam's manuscripts); THE TYPES by script; THE GATES TO FAIL (2 + 11) then GREEN with three demands read (family VIA second_census, sanctions FALSE, the pointer INTERNAL); THE RUNNER 53/53 on the third run (a token from memory, two hand tallies); THE RECORDER once; THE STITCHER as predicted to the number; THE TAPE 10/10 on the second run (CV2, CX2 the global counts over Israel's commanded entries retyped AS OF the sitting; CZ2 by prefix); every gate green; the sweep %s/%s.
THE RECORDS: NUMBERS_WALK.md "Sitting 13b — AS BUILT"; the docket; the reading ledger's CORRECTIONS; COMPILE_DEBT.md's sitting-13 box PAID and the 13b box (i)-(vii); MOVE_CATALOG M-30 THE RETREAT; MIDDOT's docket entries; MISHNAH_TOPICS (Zevachim 14:4-8 read); RESEARCH_LOG's six findings; THE_STEPS' paragraph; THE_BRIEFING's bullet; World/RESUME.md; the forms copied into World/step9/forms_numbers_walk/; memory (numbers-in-order-ruling.md, MEMORY.md, step9-exam-era.md's lessons head); the recovery file's section 13; this entry.
NEXT on the ruling: CHAPTER 34 — THE BORDERS' READING (34:1-29) on the reading shape (the recovery file's section 5; NUMBERS_WALK "Sitting 13" the form; the forms in World/step9/forms_numbers_walk/ — jou_dump.py, jou_measure1.py, jou_measure2.py, jou_ink.py, jou_legs.py, jou_rows_onkelos_a/b.py, write_jou_ledger.py, write_jou_manifest.py, seat_jou.py, jou_chain.sh, write_jou_records.py copied to the scratchpad and adapted): the measurement pass FIRST — the parser on 34:13's nine ("nine tribes and the half tribe") and 34:15's two ("the two tribes and the half tribe"), the Sifrei silent to 35:8 (found by position again, the whole export scanned for rows citing 34 with the "Ibid." and gershayim forms), Onkelos whole (29 verses); the crowns to look for: the border's four sides on the tokens (34:3-12 against Ezekiel 47-48 and Joshua 15's south border), the two and a half named again (34:14-15 with the OTHER tribe-noun — 12b's finding), the princes by name (34:17-29 — the register gate's Num 34 headers seat declared NONE, paid or held at the compile; the tribes' order against 1:5-15, 13:4-15, 26:5-50), Caleb among the princes; THEN its compile (14b) on the compile shape — NEVER THE NEXT READING FIRST.
POST-COMPACTION REREADS (mandatory, first sitting): the recovery file logic/pre_logic_methods_2026-07-28/RECOVERY_new_thread_2026-09-12.md whole (its section 5 THE READING SITTING; its sections 12 and 13) + numbers-in-order-ruling.md + this entry + NUMBERS_WALK.md "Sitting 13" (the reading's form) and "Sitting 13b — AS BUILT" (the compile's) + THE_STEPS Step 2 + Step 5 + the compiler block; memory's STANDING LESSONS head (the sitting-13b paragraph first); THE_LOOP.md "Step 1's amendment — THE CLOSE LINE" before any journal or cursor work. WATCHES: as #152's + A GLOBAL COUNT IS ANY COUNT OVER A LEDGER + THE VIA ROW CARRIES ITS TARGET + THE TAPE'S VALUE HEAD IS MATCHED BY PREFIX + A TOKEN TYPED FROM MEMORY FALLS ON ITS OWN LESSON'S VERSE + THE HAND'S TALLIES AGAINST THE MACHINE'S COLUMNS + A TWO-TOKEN CENSUS ON THE CONSONANTS COUNTS HOMOGRAPHS.
''' % (NR, NR, CELLS, NR, NR)
append(f'{ROOT}/logic/pre_logic_methods_2026-07-28/PROMPT_continue_solo_era_2026-08-06.md', SD, 'COMPACTION POINT #154')

# 12. the recovery file — section 13
REC = '''
## 13. ADDENDUM (2026-09-12, at sitting 13b's close — the state doc's COMPACTION POINT #154; this supersedes section 12's NEXT, which is kept as written)

SITTING 13b DONE: CHAPTER 33 (the journeys) COMPILED AND ON THE TAPE — NUMBERS 1:1-33:56 READ, FROZEN, COMPILED AND ON THE TAPE (27 by THE TENT); 55 runners
(cold_run_journeys.py the 55th, 53/53), 60 daemons (law_journeys the 60th, given_at 33:50, installed_by boot with the class named — the divine voice in the
plains of Moab); RUN (1274, 66, 52, 0, 12, 1522, 31, 318, the four pairs, 121); the sweep %s/%s at %s; EVERY GATE GREEN (the tape 10/10, the journal gate,
the register gate --strict with nothing to pay, the daemon and dependency gates, every probe file, vocab_lint 0). NUMBERS_WALK.md "Sitting 13b" (design +
as-built) the record; COMPILE_DEBT.md's sitting-13b box (i)-(vii) the owed items (Leviticus 26:1-2's own compile — the figured stone's ban, the edge
OWED; the dispossession and the images OPEN to Joshua's runs — THE READBACK's; D2's class beside law_musafim's setting; Deuteronomy's seats; Joshua 5's
morrow and the manna's end; the two homographs; the display layer). THE DESIGN'S DECISION: THE FORTY-TWO STATIONS ARE A DATA ROW built from the DB, not
tape lines — a retelling never writes an act twice. THE FORMS of 13b are in World/step9/forms_numbers_walk/ (jou_compile_recon.py, jou_compile_measure.py,
jou_docket_scan.py, jou_docket_A-D.py, write_jou_docket.py, add_types_jou.py, jou_runner_measure.py, jou_part1-4.py — the runner assembled by cat,
patch_seq_literals_jou.py, jou_asbuilt.md, write_jou_compile_records.py, seq_record.py, seq_stitch.py). Still UNCOMMITTED since a42f518; commit only on
"commit push".

NEXT: CHAPTER 34 — THE BORDERS' READING (34:1-29) on section 5's reading shape (the measurement pass first: the parser on 34:13's nine and 34:15's two;
the Sifrei silent to 35:8 — found by position again, the whole export scanned for rows citing 34 with the "Ibid." and gershayim forms; Onkelos whole; one
ledger script with coverage computed, one manifest script with checks cut from the store's bytes, one seat script, the ritual, the corpus rebaked, the
stamp row), THEN its compile (14b) on section 5's compile shape with the register gate at the gates step (the Num 34 headers seat, the land's princes by
name, declared NONE — paid or held) — NEVER THE NEXT READING FIRST. Before the reading: reread NUMBERS_WALK.md "Sitting 13" (the reading's form) and
"Sitting 13b — AS BUILT" (the compile's), THE_STEPS Step 2 + Step 5 + the compiler block, memory's STANDING LESSONS head.
''' % (NR, NR, CELLS)
append(f'{ROOT}/logic/pre_logic_methods_2026-07-28/RECOVERY_new_thread_2026-09-12.md', REC, '## 13. ADDENDUM (2026-09-12, at sitting 13b')
print('records written')
