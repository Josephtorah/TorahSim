import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE DEUTERONOMY WALK sitting 2b — THE COMPILE OF CHAPTER 4 (2026-09-16; World/step9/DEUTERONOMY_WALK.md "Sitting 2b"): THE TYPES FIRST — FIVE
# tape kinds (the exhortation with the one law; the two SUPPLIED Horeb lines — the ten words declared and the tablets given, the tape's hole written
# once at its own time; the witnesses called — the one case; the three cities set apart — Moses' act), ONE case kind (horeb_case), FOUR new effects
# (adding_barred a block; covenant_declared, heaven_and_earth_witness, cities_set_apart statuses on Israel), NO registry row (Israel and Moses the
# written-on parties, both standing), the 64th daemon's block (law_obey_horeb, given_at Deut 4:2, installed_by BOOT with the class named — a law in
# Moses' voice with no divine frame), the functions block, the dependency span and the CALL edges (the token-demanded edges and the pointers after the
# gate's print), the installation probe's count 63 -> 64. The `he` is cut from the pointed DB text by FINDING the phrase's tokens (never a typed index);
# the witnesses the plain consonantal verses. Idempotent (add_types_deu.py's form).
import re, sqlite3, yaml, subprocess
ROOT = _ROOT
db = sqlite3.connect(f"file:{ROOT}/Data/tanakh.sqlite?mode=ro", uri=True)
def words(book, ch, vs):
    return [r[0] for r in db.execute("SELECT w.he FROM words w JOIN verses v ON w.verse_id=v.id WHERE v.book=? AND v.chapter=? AND v.verse=? ORDER BY w.idx", (book, ch, vs)).fetchall()]
pv = lambda w: ''.join(c for c in w if c != '/' and not (0x0591 <= ord(c) <= 0x05AF))
pl = lambda w: ''.join(c for c in w if c != '/' and not (0x0591 <= ord(c) <= 0x05C7))
def PV(book, ch, vs, lo=None, hi=None):
    ws = words(book, ch, vs); assert ws, (book, ch, vs)
    if lo is not None: ws = ws[lo - 1:hi]
    return ' '.join(pv(w) for w in ws)
def LV(book, ch, vs):
    return ' '.join(pl(w) for w in words(book, ch, vs))
def PHRASE(book, ch, vs, toks):
    plain = LV(book, ch, vs).split(); n = len(toks)
    hits = [i for i in range(len(plain) - n + 1) if plain[i:i + n] == toks]
    assert len(hits) == 1, (book, ch, vs, toks, hits, plain)
    return PV(book, ch, vs, hits[0] + 1, hits[0] + n)
q = lambda s: '"' + s.replace('\\', '\\\\').replace('"', '\\"') + '"'
def HE(book, ch, lo, hi, en, cap=6):
    vv = list(range(lo, min(hi, lo + cap - 1) + 1))
    s = ' · '.join(PV(book, ch, v) + ' (%s — %s %d:%d)' % (en if v == lo else 'the verse continues', book, ch, v) for v in vv)
    return s + (' · … (through %s %d:%d)' % (book, ch, hi) if hi > vv[-1] else '')
def WIT(book, ch, lo, hi):
    return ['%s %d:%d | %s' % (book, ch, v, LV(book, ch, v)) for v in range(lo, hi + 1)]
CORPUS = "deu_04_obey_horeb (STEP_Dt_4_1 through STEP_Dt_4_40; claims DV04A-01 through DV04A-05), deu_04_refuge_east (STEP_Dt_4_41 through STEP_Dt_4_49; claims DV04B-01, DV04B-02)"
SUB = "submitted by cold_run_obey_horeb.py [subjects: %s] (the narrative scene, THE DEUTERONOMY WALK 2b); re-submitted on the sequential tape by cold_run_sequence.py; consumed by law_obey_horeb (cold_run_obey_horeb.py) -> %s"
CASE = "submitted by cold_run_obey_horeb.py [subjects: the exam's persons] (the wrap's scene); consumed by law_obey_horeb (cold_run_obey_horeb.py) -> %s"
INK = "Deut 4:1-49; Onkelos Deut 4:1-49 (the fear supplied at 4:4, 20, 29-30; the Memra at 4:24, 33, 36-37; 'prepared' for 'apportioned' at 4:19; the idolaters for the idols at 4:28; the Name for 'God' at 4:32); the Sifrei on Deuteronomy's eight rows citing the chapter (30:2, 37:9, 48:2, 49:2, 148:8, 301:21, 306:1, 323:1 — NO piska on the chapter); the reading ledger deu_04_vaetchanan_2026-09-16.md (55 sources, 7 claims); the exam docket deu_04_vaetchanan_exam_2026-09-16.md (327 rows: LAW 76 / DERIVATION 70 / DISPUTE 12 / CONTEXT 169)"
D, X = 'Deut', 'Exod'
KINDS = [
 ("add_nothing_commanded", "speech",
  "the exhortation with the one law — 'and now, Israel, hear the statutes and the judgments which I teach you, to do them, that you may live and go in and possess the land; YOU SHALL NOT ADD to the word which I command you, NOR DIMINISH from it, to keep the commandments of the LORD your God which I command you … behold, I have taught you statutes and judgments AS THE LORD MY GOD COMMANDED ME … for what great nation has God so near … what great nation has statutes and judgments so righteous as all this Torah which I set before you this day' (Deut 4:1-8) — adding_barred on Israel (a BLOCK: THE CHAPTER'S ONE LAW, 4:2 the plural's one seat, 13:1 the singular's forward — bal tosif's rows Rosh Hashanah 28b, Eruvin 95b-96a, Sanhedrin 88b-89a); the receipt 4:5 the register seat ACT — the teaching's run (Exodus 24:12's 'to teach them'; 4:14 'the LORD commanded me at that time to teach you'; Bekhorot 29a — as I learned for free, you learned for free); page_order at the speech's day (40, 11, 1)",
  HE(D, 4, 1, 8, "and now, Israel, hear the statutes and the judgments which I teach you"), WIT(D, 4, 1, 8), INK, CORPUS,
  SUB % ("israel", "adding_barred on israel_people (a BLOCK — the law's own write; the register seat Deut 4:5 ACT by the line's source)"), ["law", "receipt"]),
 ("ten_words_declared", "speech",
  "the ten words declared — 'the day you stood before the LORD your God at Horeb … and you came near and stood under the mountain, and the mountain burned with fire to the heart of heaven … and the LORD spoke to you from the midst of the fire: a voice of words you heard, but no form, only a voice; and he declared to you his covenant which he commanded you to do, THE TEN WORDS' (Deut 4:10-13) — Exodus 20:1's 'and God spoke all these words' THE FIRST TELLING, absent from the tape (the tape runs from Exod 19:20 to 24:1 — THE TAPE'S HOLE, the readback's finding): A SUPPLIED ACT written ONCE at its own time, DATED (1, 3, 7) by the RETROGRADE marker at Deut 4:10 (the giving's day — Rabbi Yose's seventh of Sivan, Shabbat 86b:5, the tape's own marker at Exod 19:16; the ink's dating word 'the day you stood'); covenant_declared on Israel (a STATUS valued the ten words on two tablets)",
  HE(D, 4, 10, 13, "the day you stood before the LORD your God at Horeb, when the LORD said to me: assemble the people to me"), WIT(D, 4, 10, 13) + WIT(X, 20, 1, 1), INK, CORPUS,
  SUB % ("israel", "covenant_declared on israel_people (a STATUS dated (1, 3, 7) — the ten words declared at Horeb; the first telling Exod 20:1-17 named in the row)"), ["first_telling", "dated"]),
 ("tablets_given", "act",
  "the tablets given — 'and he wrote them on two tablets of stone' (Deut 4:13, the tablets PLENE — 4:13, 9:11, 1 Kings 8:9 against every Exodus seat defective); 'and He gave to Moses, when He finished speaking with him on Mount Sinai, two tablets of the testimony, tablets of stone written with the finger of God' (Exodus 31:18 — THE FIRST TELLING, absent from the tape: the erection runner folded the tablets into the ascent's line at W7 — THE TAPE'S HOLE): A SUPPLIED ACT written ONCE at its own time, DATED (1, 4, 17) by the RETROGRADE marker at Deut 4:13 (the fortieth day of 24:18's forty — Taanit 28b:9: the seventh of Sivan plus forty = the seventeenth of Tammuz; the tablets GIVEN and BROKEN on one day, 32:15 'Moses went down with the two tablets', the tape's own marker at Exod 32:19); tablets_delivered on Moses (the erection's registered effect at its FIRST tape seat)",
  HE(D, 4, 13, 13, "and he declared to you his covenant which he commanded you to do, the ten words, and he wrote them on two tablets of stone"), WIT(D, 4, 13, 13) + WIT(X, 31, 18, 18), INK, CORPUS,
  SUB % ("moses", "tablets_delivered on moses (the TRANSFER — the erection's effect, dated (1, 4, 17); the first telling Exod 31:18 named in the row)"), ["first_telling", "dated", "plene"]),
 ("witnesses_called", "speech",
  "heaven and earth called to witness — 'WHEN you beget sons and sons' sons and have grown old in the land and deal corruptly and make a graven image … I CALL HEAVEN AND EARTH TO WITNESS AGAINST YOU THIS DAY that you shall surely perish quickly from the land … the LORD will scatter you among the peoples and you shall be left few in number … there you shall serve gods the work of men's hands, wood and stone … you will seek the LORD your God from there and find him … in your distress, in the end of days, you will return to the LORD your God and hearken; for the LORD your God is a merciful God, he will not fail you nor destroy you nor forget the covenant of your fathers which he swore to them' (Deut 4:25-31) — THE CHAPTER'S ONE CASE ('when', 4:25): heaven_and_earth_witness on Israel (a STATUS — the Sifrei 306:1's chain of witnesses, the third of eleven; 30:19 and 31:28 forward, 30:19's first seven words identical); the arms DATA (the tochacha's scattered_among_nations and covenant_remembered by CALL — Leviticus 26:33, 26:42 the first tellings; 28:36, 28:64 forward), 'in the end of days' a prophecy, NO timer; page_order at (40, 11, 1)",
  HE(D, 4, 25, 31, "when you beget sons and sons' sons and have grown old in the land and deal corruptly"), WIT(D, 4, 25, 31), INK, CORPUS,
  SUB % ("israel", "heaven_and_earth_witness on israel_people (a STATUS — the witnesses named against the case's arms)"), ["case", "witnesses"]),
 ("three_cities_set_apart", "act",
  "three cities set apart — 'THEN Moses set apart three cities beyond the Jordan toward the sunrise, that the manslayer might flee there, who slays his neighbor unawares and hated him not in time past, and that fleeing to one of these cities he might live: Bezer in the wilderness in the plain for the Reubenites, and Ramoth in Gilead for the Gadites, and Golan in Bashan for the Manassites' (Deut 4:41-43) — Moses' own ACT in the third person ('then' with the imperfect — the Song's form, the six Torah seats; the chapter's only narrative act of its own day): cities_set_apart on Israel (a STATUS valued the three — the refuge runner's DATA row the_six_cities by CALL, computed by seat); THE REFUGE DEBIT appoint_six_cities_of_refuge READ OPEN, not closed — Mishnah Makkot 2:4 / Makkot 9b:14: the three east admitted no one until Joshua's three were selected, 'six cities of refuge SHALL THEY BE' (Numbers 35:13); R. Simlai: 'a mitzva that came my way' (Makkot 10a:15-16); Joshua 20:7-8 the close, OUTSIDE THE TORAH, the readback's; 4:42 the manslayer in 19:4's words with 'slays' for 'smites' (computed); page_order at (40, 11, 1)",
  HE(D, 4, 41, 43, "then Moses set apart three cities beyond the Jordan toward the sunrise"), WIT(D, 4, 41, 43), INK, CORPUS,
  SUB % ("israel", "cities_set_apart on israel_people (a STATUS valued the three cities; the refuge debit on israel_people read OPEN, unmoved)"), ["cities", "manslayer"]),
 ("horeb_case", "case", "the exam's rows on chapter 4 (Deut 4:1-49 — bal tosif: Rosh Hashanah 28b:8-24, Eruvin 95b:19-96a:11, Sanhedrin 88b:14-89a:2; the teaching and the forgetting: Kiddushin 30a, Berakhot 21b-22a, Menachot 99b, Avot 3:8, Bekhorot 29a, Nedarim 37a-38a; the images: Mishnah Avodah Zarah 3:1-3, Mishnah Rosh Hashanah 2:8, Rosh Hashanah 24a-24b; the host: Avodah Zarah 55a; the cleaving and the fire: Ketubot 111b, Sanhedrin 64a, 90b, Sotah 14a, Avodah Zarah 54b-55a; the inquiry: Chagigah 11b-12a, Sanhedrin 38b; the creed: Chullin 7b, Sanhedrin 67b, Rosh Hashanah 32b; the exile: Gittin 88a, Sanhedrin 38a, Megillah 31b; God near: Sanhedrin 38b, Rosh Hashanah 18a, Yevamot 105a; the cities: Mishnah Makkot 2:4-8, Makkot 9b-10a, Gittin 12a, Sotah 49a; the Haggadah: Mishnah Pesachim 10:4; the frame: Yoma 72b) — the exam's persons through the cells' asks: the priest who adds a blessing, the sleeper in the sukkah on the eighth, the second pair of tefillin, the elder's fifth compartment, the grandfather, the forgetter, the paid teacher, the moon's forms for study, the vessels with the sun, the cleaver, the inquirer, the teacher exiled, the manslayer in Moses' three, the Haggadah's expounder, the community's sentence",
  PHRASE(D, 4, 2, ['לא', 'תספו', 'על', 'הדבר']) + " (you shall not add to the word — Deut 4:2)", WIT(D, 4, 1, 8) + WIT(D, 4, 41, 43), INK, CORPUS, CASE % "accepted / exempt (the exam's persons — the rule holds against him / outside the rule)", ["person", "ask"]),
]
assert len(KINDS) == 6, len(KINDS)
path = f"{ROOT}/World/step9/event_vocabulary.yaml"
text = open(path, encoding='utf-8').read()
have = yaml.safe_load(text)['events']
out = []
for name, form, en, he, wit, ink, corpus, tape, fields in KINDS:
    if name in have: continue
    out.append(f"  {name}:\n    en: {q(en)}\n    he: {q(he)}\n    form: {form}\n    witness: [{', '.join(q(w) for w in wit)}]\n    ink: {q(ink)}\n    corpus: {q(corpus)}\n    tape: {q(tape)}\n    fields: [{', '.join(q(f) for f in fields)}]\n")
if out:
    i = text.index('\nnarrative_verbs:\n')
    text = text[:i] + '\n' + ''.join(out).rstrip('\n') + text[i:]
    open(path, 'w', encoding='utf-8').write(text)
after = yaml.safe_load(open(path, encoding='utf-8'))
assert all(k[0] in after['events'] for k in KINDS)
print('kinds: %d added of %d, registry %d' % (len(out), len(KINDS), len(after['events'])))
# ---- FOUR new effects, the ink's own words, the `he` FOUND in the verse ----
path = f"{ROOT}/World/step9/effect_vocabulary.yaml"
text = open(path, encoding='utf-8').read()
fx = yaml.safe_load(text)['effects']
for e in ('tablets_delivered', 'accepted', 'exempt', 'commanded', 'scattered_among_nations', 'covenant_remembered', 'torah_expounded', 'yoked_to_baal_peor', 'barred_from_the_land', 'brought_out' if 'brought_out' in fx else 'commanded'):
    assert e in fx, e
HE_ADD = PHRASE(D, 4, 2, ['לא', 'תספו', 'על', 'הדבר', 'אשר', 'אנכי', 'מצוה', 'אתכם', 'ולא', 'תגרעו', 'ממנו'])
HE_DECL = PHRASE(D, 4, 13, ['ויגד', 'לכם', 'את', 'בריתו', 'אשר', 'צוה', 'אתכם', 'לעשות', 'עשרת', 'הדברים'])
HE_WIT = PHRASE(D, 4, 26, ['העידתי', 'בכם', 'היום', 'את', 'השמים', 'ואת', 'הארץ'])
HE_SET = PHRASE(D, 4, 41, ['אז', 'יבדיל', 'משה', 'שלש', 'ערים'])
NEW = [
 ('adding_barred', 'block',
  "adding barred — the BLOCK the chapter's one law writes on Israel: 'you shall not add to the word which I command you, nor diminish from it, to keep the commandments of the LORD your God which I command you' (Deut 4:2 — the plural's one seat; 13:1 the singular's, forward); the exam's two parameters — IN THE MITZVA'S TIME the addition transgresses without intent, OUT OF ITS TIME only with intent (Rava, Rosh Hashanah 28b:24; the sleeper in the sukkah on the eighth day, the second pair of tefillin on the Sabbath — Eruvin 95b:19-96a:5, the priest who adds a blessing — 28b:10-13, the whole day his time); the third — AN ADDITION THAT SPOILS (the elder's fifth compartment made as one against a fifth placed beside; the lulav's species by the binding, the fringes' thread by the upper knot — Sanhedrin 88b:14-89a:2); 'do not diminish' the pair's other arm — an OMISSION where adding is an ACT (R. Yehoshua, 28b:18; the mixed bloods 28b:15-17); the Sifrei 82:5's fifth species and fifth fringe the shelf's exhibit; the block's reach the law's own: every mitzva's measure",
  HE_ADD + " (you shall not add to the word which I command you, nor diminish from it — Deut 4:2)",
  "Deut 4:2 ('you shall not add to the word which I command you, nor diminish from it'), 13:1 ('you shall not add to it nor diminish from it' — the singular), 4:1 ('hear the statutes and the judgments which I teach you'), 4:5-8 (the receipt and the wisdom); Exodus 5:8 (the bricks' diminish-root), Numbers 27:4, 36:3-4 (the daughters' — the root's kin); Onkelos 4:2; the Sifrei 82:5 on 13:1 (credited); Babylonian Talmud Rosh Hashanah 28b:8-24, Eruvin 95b:19-96a:11, Sanhedrin 88b:14-89a:2; Mishnah Sanhedrin 11:3",
  "deu_04_obey_horeb (STEP_Dt_4_1, STEP_Dt_4_2; the claim DV04A-01)",
  "cold_run_obey_horeb.py (F1 the_exhortation — add_nothing, diminish_nothing; the tape kind add_nothing_commanded; the exam kind horeb_case)"),
 ('covenant_declared', 'status',
  "the covenant declared — the STATUS the ten words' speaking writes on Israel: 'and he declared to you his covenant which he commanded you to do, the ten words, and he wrote them on two tablets of stone' (Deut 4:13); 'and God spoke all these words, saying' (Exodus 20:1 — THE FIRST TELLING, absent from the tape until this line: the readback's finding); the value the ten words on two tablets; dated (1, 3, 7) — the giving's day by Rabbi Yose (Shabbat 86b:5; the calendar row sinai_days), the tape's own marker at Exodus 19:16; 'the ten words' three Bible seats (Exodus 34:28, Deuteronomy 4:13, 10:4 — the erection's tablets cell by CALL); the second pass's D2 candidate: law_decalogue's installing act (now covenant_blood_thrown, 24:8) may turn to this line",
  HE_DECL + " (and he declared to you his covenant which he commanded you to do, the ten words — Deut 4:13)",
  "Deut 4:13 ('and he declared to you his covenant … the ten words'), 4:10-12 ('the day you stood before the LORD your God at Horeb … a voice of words you heard, but no form'), 4:15, 4:33, 4:36 (the voice from the fire), 5:22 forward ('these words the LORD spoke to all your assembly … and he wrote them on two tablets of stone and gave them to me'), 9:10, 10:4; Exodus 20:1 ('and God spoke all these words'), 19:16-20 (the assembly's day — thunder_and_horn, lord_descended on the tape), 34:28; Onkelos 4:13; Babylonian Talmud Shabbat 86b:5-87a:3 (the days of Sivan), Berakhot 22a:4, Kiddushin 30a:7 (the juxtaposition to 4:9)",
  "deu_04_obey_horeb (STEP_Dt_4_10 through STEP_Dt_4_13; the claim DV04A-02)",
  "cold_run_obey_horeb.py (F2 horeb_retold — the_voice_and_no_form, the_ten_words_and_the_tablets; the tape kind ten_words_declared, SUPPLIED, dated by the retrograde marker at Deut 4:10)"),
 ('heaven_and_earth_witness', 'status',
  "heaven and earth called to witness — the STATUS the case's evidence clause writes on Israel: 'I call heaven and earth to witness against you this day that you shall surely perish quickly from the land … you shall not prolong your days upon it but shall be utterly destroyed' (Deut 4:26) — the witnesses of the exile case (4:25-31: corrupt → perish, scatter, few, serve wood and stone; seek → find; return → mercy); the Sifrei 306:1's CHAIN OF WITNESSES — 4:26 the third of eleven (30:19 'I call heaven and earth to witness against you this day', 31:28 'that I may call heaven and earth to witness against them', 32:1 'give ear, O heavens'; 30:19's first seven words identical, computed); 'the end of days' (4:30) a prophecy — no timer, no exile written; Gittin 88a:15-17 and Sanhedrin 38a:6 (the exile hastened by two years of 'grown old'); Megillah 31b:2 (the Ninth of Av's reading)",
  HE_WIT + " (I call heaven and earth to witness against you this day — Deut 4:26)",
  "Deut 4:26 ('I call heaven and earth to witness against you this day'), 4:25 ('when you beget sons and sons' sons and have grown old in the land and deal corruptly'), 4:27-31 (the arms), 30:19, 31:28, 32:1 (the chain — forward); Leviticus 26:33, 26:42 (the tochacha's scatter and remember — the first tellings, by CALL), 28:36, 28:64 (forward); Onkelos 4:26; the Sifrei 306:1 on 32:1 (read at the reading); Babylonian Talmud Gittin 88a:15-17, Sanhedrin 38a:6, Megillah 31b:2",
  "deu_04_obey_horeb (STEP_Dt_4_25 through STEP_Dt_4_31; the claim DV04A-04)",
  "cold_run_obey_horeb.py (F4 the_exile_case — the_case_head, the_witnesses, perish_and_scatter, seek_and_find, in_your_distress_return, the_merciful_god; the tape kind witnesses_called)"),
 ('cities_set_apart', 'status',
  "cities set apart — the STATUS Moses' act writes on Israel: 'then Moses set apart three cities beyond the Jordan toward the sunrise … Bezer in the wilderness in the plain for the Reubenites, and Ramoth in Gilead for the Gadites, and Golan in Bashan for the Manassites' (Deut 4:41, 4:43) — the value the three; THE REFUGE DEBIT appoint_six_cities_of_refuge (Numbers 35:11-14, on Israel since (40, 6, 1)) READ OPEN AND NOT CLOSED: the appointment is ONE of six — Mishnah Makkot 2:4 / Makkot 9b:14 'until the three in the land of Canaan were selected, the three beyond the Jordan did not admit', 'six cities of refuge SHALL THEY BE' (35:13); R. Simlai: Moses knew and said 'a mitzva that came my way, I will fulfill it' (Makkot 10a:15-16); the two rows of vines — Hebron against Bezer, Shechem against Ramoth, Kadesh against Golan (9b:18); Reuben first (10a:14); Joshua 20:7-8 the six's run and the debit's close, OUTSIDE THE TORAH — the readback's; 'then' with the imperfect the Song's form (Exodus 15:1, Numbers 21:17 — the six Torah seats computed); the names outside Numbers 35 (the refuge runner's DATA row the_six_cities by CALL)",
  HE_SET + " (then Moses set apart three cities — Deut 4:41)",
  "Deut 4:41 ('then Moses set apart three cities beyond the Jordan toward the sunrise'), 4:42 ('that the manslayer might flee there, who slays his neighbor unawares and hated him not in time past' — 19:4's words with 'slays' for 'smites', computed; the murder-verb plene), 4:43 (the three names); Numbers 35:11-14 (the debit's spec — 'three cities beyond the Jordan and three in the land of Canaan'), 35:6; Deuteronomy 19:1-13 forward; Joshua 20:7-8 (Gaulon), 21:36; Onkelos 4:41-43; Babylonian Talmud Makkot 9b:14-10a:16; Mishnah Makkot 2:4-8; Avodah Zarah 58b:8 (Bezer not Bozrah)",
  "deu_04_refuge_east (STEP_Dt_4_41 through STEP_Dt_4_43; the claim DV04B-01)",
  "cold_run_obey_horeb.py (F6 the_cities_and_the_frame — then_moses_set_apart, not_until_all_six, the_manslayer_defined, the_three_names; the tape kind three_cities_set_apart)"),
]
added = 0
for name, op, en, he, ink, corpus, exam in NEW:
    if name in fx: continue
    text = text.rstrip('\n') + '\n' + f"  {name}:\n    en: {q(en)}\n    he: {q(he)}\n    ledger_op: {op}   # THE DEUTERONOMY WALK 2b (2026-09-16): chapter 4's compile — {name}\n    ink: {q(ink)}\n    corpus: {q(corpus)}\n    exam: {q(exam)}\n"
    added += 1
open(path, 'w', encoding='utf-8').write(text)
fx = yaml.safe_load(open(path, encoding='utf-8'))['effects']
assert all(n in fx for n, *_ in NEW) and fx['adding_barred']['ledger_op'] == 'block' and fx['covenant_declared']['ledger_op'] == 'status' and fx['heaven_and_earth_witness']['ledger_op'] == 'status' and fx['cities_set_apart']['ledger_op'] == 'status'
print('effects: %d added (registry %d); the he found in the verses: %s | %s | %s | %s' % (added, len(fx), HE_ADD, HE_DECL, HE_WIT, HE_SET))
# ---- NO registry row (Israel and Moses the written-on parties, both standing) ----
reg = yaml.safe_load(open(f"{ROOT}/logic/corpus/entity_registry.yaml", encoding='utf-8'))
ids = {e['id'] for e in reg['entities']}
assert 'israel_people' in ids and 'moses' in ids, 'the written-on parties must stand'
print('entities: none added (registry %d)' % len(reg['entities']))
# ---- the daemon block + the functions block (daemon_dispositions.yaml) ----
path = f"{ROOT}/World/step9/daemon_dispositions.yaml"
text = open(path, encoding='utf-8').read()
if '  law_obey_horeb:' not in text:
    block = '''  law_obey_horeb:
    file: cold_run_obey_horeb.py
    wraps: obey_horeb
    given_at: Deut 4:2
    installed_by: boot   # THE DEUTERONOMY WALK 2b (2026-09-16): A LAW IN MOSES' VOICE WITH NO DIVINE FRAME — 'you shall not add to the word which I command you' (4:2): the vows' class (the opening speech's 1:16 the same), the second pass's D2 question; no installing act, no in_force write
    watches:
      add_nothing_commanded: [adding_barred]                    # Deut 4:1-8: THE ONE LAW — a BLOCK on Israel (bal tosif); the receipt 4:5 inside the line's source (the register seat ACT)
      ten_words_declared: [covenant_declared]                   # Deut 4:10-13 (Exod 20:1 the first telling): SUPPLIED, dated (1, 3, 7) by the retrograde marker at 4:10 — a STATUS on Israel
      tablets_given: [tablets_delivered]                        # Deut 4:13 (Exod 31:18 the first telling): SUPPLIED, dated (1, 4, 17) by the retrograde marker at 4:13 — the erection's TRANSFER on Moses at its first tape seat
      witnesses_called: [heaven_and_earth_witness]              # Deut 4:25-31: THE ONE CASE — a STATUS on Israel; the arms DATA, no timer
      three_cities_set_apart: [cities_set_apart]                # Deut 4:41-43: Moses' ACT — a STATUS on Israel valued the three; the refuge debit READ OPEN (Makkot 2:4)
      horeb_case: [accepted, exempt]                            # the exam's rows on the chapter — the persons through the cells' asks
'''
    i = text.index('  law_census:')
    text = text[:i] + block + text[i:]
if '\n  obey_horeb:   # THE DEUTERONOMY WALK 2b' not in text:
    fb = '''  obey_horeb:   # THE DEUTERONOMY WALK 2b (2026-09-16)
    the_exhortation: {status: WRAPPED, by: law_obey_horeb}
    horeb_retold: {status: WRAPPED, by: law_obey_horeb}
    no_image: {status: WRAPPED, by: law_obey_horeb}
    the_exile_case: {status: WRAPPED, by: law_obey_horeb}
    the_one_god: {status: WRAPPED, by: law_obey_horeb}
    the_cities_and_the_frame: {status: WRAPPED, by: law_obey_horeb}
'''
    i = text.index('  opening_speech:   # THE DEUTERONOMY WALK 1b')
    j = text.index('\n  pre_sinai:', i)
    text = text[:j + 1] + fb + text[j + 1:]
open(path, 'w', encoding='utf-8').write(text)
dd = yaml.safe_load(open(path, encoding='utf-8'))
assert 'law_obey_horeb' in dd['daemons'] and 'obey_horeb' in dd['functions'], (list(dd)[:5])
print('daemons: %d (law_obey_horeb %s); functions blocks: %d' % (len(dd['daemons']), 'law_obey_horeb' in dd['daemons'], len(dd['functions'])))
# ---- the dependency span + the CALL edges (the token-demanded edges and the POINTERS after the gate's print) ----
path = f"{ROOT}/World/step9/dependency_dispositions.yaml"
text = open(path, encoding='utf-8').read()
if '\n  obey_horeb:' not in text.split('\nedges:')[0]:
    a = "  opening_speech: [[Num, 27, 12, 23], [Deut, 1, 1, 46], [Deut, 2, 1, 37], [Deut, 3, 1, 29]]"
    i = text.index(a); j = text.index('\n', i)
    text = text[:j + 1] + "  obey_horeb: [[Deut, 4, 1, 49]]   # THE DEUTERONOMY WALK 2b (2026-09-16; DEUTERONOMY_WALK.md \"Sitting 2b\"): chapter 4 — the one law (4:2), the one case (4:25-31), Horeb retold with the two supplied lines (the ten words, the tablets — the tape's hole), the three cities' act, the second frame\n" + text[j + 1:]
    W = "THE DEUTERONOMY WALK 2b (2026-09-16) | "
    edges = f'''  - {{from: obey_horeb, to: balak, disposition: CALL, link: reference, carries: verdict,
     why: "{W}4:3's 'your eyes have seen what the LORD did at Baal-peor: every man who followed Baal-peor the LORD your God destroyed from your midst' is Numbers 25:3-9 READ BACK (BK.peor('plague_count') CALLED — the twenty-four thousand; 'peor_service' the worship's definition; 'judges_count' the slayers' arithmetic): the readback row SHORTENED against the tape's israel_yoked_to_baal_peor; 4:46's 'the valley over against Beth-peor' the last camp (BK.the_call('last_camp') CALLED)"}}
  - {{from: obey_horeb, to: refuge, disposition: CALL, link: reference, carries: verdict,
     why: "{W}4:41-43's three cities are Numbers 35:11-14's 'three cities beyond the Jordan' (RF.the_refuge_law('six_cities') and ('the_debit') CALLED — the DATA row the_six_cities naming Bezer, Ramoth, Golan by seat; the debit appoint_six_cities_of_refuge READ OPEN and left open on Mishnah Makkot 2:4's row); 4:42's 'who slays his neighbor unawares and hated him not in time past' the manslayer's clauses (RF.the_manslayer('not_his_enemy') and ('without_seeing') CALLED — 19:4's words with 'slays' for 'smites')"}}
  - {{from: obey_horeb, to: opening_speech, disposition: CALL, link: reference, carries: verdict,
     why: "{W}4:21-22's 'the LORD was angry with me on your account and swore' is the bar's THIRD telling (OS.the_spies_read_back('the_bars_ground') and OS.the_plea('the_refusal') CALLED — 1:37's and 3:26's tellings, the DISAGREES row widened, OPEN); 4:44-49's second frame and borders quote the speech's own 1:1, 1:4, 2:36, 3:8, 3:17 (OS.the_frame('after_sihon') and OS.sihon_and_og('hermon') CALLED; OS.READBACK the first form's forty-two rows the chapter's eleven join)"}}
  - {{from: obey_horeb, to: erection, disposition: CALL, link: reference, carries: verdict,
     why: "{W}4:13's 'the ten words … on two tablets of stone' — 'the ten words' at three seats (ER.tablets('ten_words') CALLED — Exodus 34:28, Deuteronomy 4:13, 10:4) and the tablets' forms (ER.tablets('finger_and_forms') CALLED — the plene/defective census); 4:13's tablets_given dated the fortieth day (ER.ascent('seventeenth_tammuz') CALLED — Taanit 28b: the seventh of Sivan plus forty); 4:5 and 4:14's teaching Exodus 24:12's 'to teach them' (ER.tablets('torah_mitzvah') CALLED); 4:10's Horeb (ER.presence('horev_plene') CALLED — plene at Exodus 33:6 alone)"}}
  - {{from: obey_horeb, to: exodus_story, disposition: CALL, link: reference, carries: verdict,
     why: "{W}4:10's 'the day you stood before the LORD your God at Horeb' is Exodus 19:16-20's assembly (ES.sinai('days_r_yose') CALLED — Rabbi Yose's seventh of Sivan the giving's day, the retrograde marker's day at 4:10; ES.sinai('descents')); 4:34's instruments are the exodus's (ES.plagues('ten') and ES.sea('ten_at_sea') CALLED — the plagues and the sea's miracles; ES.night('sent_formula') the sending); 4:20's 'brought you out of the iron furnace' and 4:37's 'brought you out with his presence' the tape's brought_out (12:51) READ BACK"}}
  - {{from: obey_horeb, to: tochacha, disposition: CALL, link: reference, carries: verdict,
     why: "{W}4:27's 'the LORD will scatter you among the peoples' and 4:31's 'nor forget the covenant of your fathers' are Leviticus 26:33's scattering and 26:42's remembering (TC.recovery(True, True) CALLED — covenant_remembered; TC.NOT_BROKEN the covenant never broken in the enemies' land): the exile case's arms as DATA, no entry written (no exile on the tape)"}}
  - {{from: obey_horeb, to: pre_sinai, disposition: CALL, link: reference, carries: verdict,
     why: "{W}4:32's 'since the day God created man upon the earth' is Genesis 1:27's 'created' (PS.creation('created_made') CALLED — 'created' six, 'made' ten; the book's one seat of the verb; the sixth day's marker on the tape, the era life:the_human)"}}
  - {{from: obey_horeb, to: primeval, disposition: CALL, link: reference, carries: verdict,
     why: "{W}4:20's 'the iron furnace' the furnace-word's first seat Genesis 15:17 (PR.pieces('furnace') CALLED — Bereshit Rabbah 44:13's furnace of fire at 15:7); 4:37's 'because he loved your fathers he chose their seed' and 4:38's 'to give you their land' Genesis 15:18's land (PR.call('land_seats') CALLED)"}}
  - {{from: obey_horeb, to: decalogue, disposition: CALL, link: reference, carries: verdict,
     why: "{W}4:36's 'from heaven he made you hear his voice' is Exodus 20:22's 'from heaven I spoke with you' (DC.altar_rules('steps') CALLED — the altar rule's seat, 20:22-26; the Mekhilta credited by name); 4:16-19's no-image list restates the Decalogue's SECOND WORD (Exodus 20:3-6 — 'any likeness of what is in heaven above') — UNCOMPILED: cold_run_decalogue.py wraps vain_name, sabbath_clauses, theft_commandment (altar_rules by the ordinances), no cell for the image law: OWED to chapter 5's sitting (COMPILE_DEBT); 4:24's 'jealous God' 20:5's by REFERENCE"}}
  - {{from: obey_horeb, to: chukat, disposition: CALL, link: reference, carries: verdict,
     why: "{W}4:46-47's 'Sihon king of the Amorites … and the land of Og king of Bashan, the two kings of the Amorites' are Numbers 21:24-25 and 21:35 READ BACK a second time (CK.well_and_kings('deut3_delta') CALLED — the two kings' lines; sihon_smitten_land_possessed and og_smitten the tape's kinds): the readback row SHORTENED against the speech's own 1:4 and 3:8"}}
  - {{from: obey_horeb, to: borders, disposition: CALL, link: reference, carries: verdict,
     why: "{W}4:48-49's 'from Aroer on the bank of the brook Arnon to Mount Sion which is Hermon, and all the Arabah beyond the Jordan eastward to the sea of the Arabah under the slopes of Pisgah' are the east's extents (BO.the_four_sides('the_promised_extents') CALLED; 2:36, 3:8-9, 3:17 the speech's own lines quoted verbatim — computed diffs)"}}
  - {{from: sequence, to: obey_horeb, disposition: CALL, link: none,
     why: "{W}the sequential run's REGISTRATION edge — ('cold_run_obey_horeb', 'law_obey_horeb') in DAEMON_ORDER (the runner compiles no verse: link none, O4's license); the five tape lines and the two retrograde markers (Deut 4:10, 4:13) this sitting's"}}
'''
    a = "  - {from: sequence, to: opening_speech, disposition: CALL, link: none,"
    i = text.index(a); j = text.index('\n', text.index('why:', i)) + 1
    text = text[:j] + edges + text[j:]
    open(path, 'w', encoding='utf-8').write(text)
dep = yaml.safe_load(open(path, encoding='utf-8'))
n_oh = sum(1 for e in dep['edges'] if e['from'] == 'obey_horeb')
assert 'obey_horeb' in dep['spans'] and n_oh == 11, n_oh
print('dependency: span + 12 edges (obey_horeb 11 CALL and the registration); the token-demanded edges and the pointers after the gate\'s print')
# ---- the installation probe's count ----
path = f"{ROOT}/World/step9/installation_probes.py"
text = open(path, encoding='utf-8').read()
if "len(real) == 63 and all(" in text:
    text = text.replace("len(real) == 63 and all('given_at' in d and 'installed_by' in d for d in real.values())   # THE DEUTERONOMY WALK 1b (2026-09-15): 62 -> 63, law_opening_speech",
                        "len(real) == 64 and all('given_at' in d and 'installed_by' in d for d in real.values())   # THE DEUTERONOMY WALK 2b (2026-09-16): 63 -> 64, law_obey_horeb (installed_by boot — a law in Moses' voice with no divine frame, the class named); 1b: 62 -> 63, law_opening_speech")
    open(path, 'w', encoding='utf-8').write(text)
assert "len(real) == 64" in open(path, encoding='utf-8').read()
print('installation_probes I5: 64')
