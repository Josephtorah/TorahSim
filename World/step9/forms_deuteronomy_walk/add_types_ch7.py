#!/usr/bin/env python3
import os as _os, subprocess as _sp
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
# THE DEUTERONOMY WALK sitting 5b — THE COMPILE OF CHAPTER 7 (2026-09-18; World/step9/DEUTERONOMY_WALK.md "Sitting 5b"): THE TYPES FIRST — THREE tape
# kinds (nations_devoted 7:1-5 — the ban, no covenant, no favor, no marriage, the four objects; hearing_blessed 7:12-16 — the covenant kept and the
# blessings, no pity, no serving; abomination_barred 7:25-26 — the images burned, the silver and gold not coveted, the abomination not into the house,
# the devoted thing), all STATUTE by form (the own-day giving of a law — chapter 4's and 6's form), ONE case kind (seven_nations_case), FOUR new effects
# (favor_barred a BLOCK, pity_barred a BLOCK, blessings_for_hearing a conditional HEAVEN entry — the design's name blessing_promised was Abram's ladder entry, the registry decided, house_abomination_barred a BLOCK — all on Israel), NO registry
# row (Israel the written-on party; the seven nations a counterparty string), the 67th daemon's block (law_seven_nations, given_at Deut 7:1 — the ban's
# first and only giving, installed_by boot — the three Deuteronomy daemons' form), the functions block (six cells WRAPPED), the dependency span and the
# thirteen CALL edges by the ink with the registration edge, the installation probe's count 66 -> 67. The `he` is cut from the pointed DB text by FINDING
# the phrase's tokens (never a typed index); the claim ids and the step ids READ from the frozen unit. Idempotent (add_types_ch6.py's form, derived by
# hand where it differs).
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
unit = open(f'{ROOT}/logic/units/deu_07_nations_cherem.yaml', encoding='utf-8').read()
CL = sorted(set(re.findall(r'DV07-\d+', unit))); ST = sorted({int(x) for x in re.findall(r'STEP_Dt_7_(\d+)', unit)})
assert len(CL) == 6 and ST[0] == 1 and ST[-1] == 26, (CL, ST[:3], ST[-1])
CORPUS = f"deu_07_nations_cherem (STEP_Dt_7_1 through STEP_Dt_7_26; claims {CL[0]} through {CL[-1]})"
SUB = "submitted by cold_run_seven_nations.py [subjects: %s] (the narrative scene, THE DEUTERONOMY WALK 5b); re-submitted on the sequential tape by cold_run_sequence.py; consumed by law_seven_nations (cold_run_seven_nations.py) -> %s"
CASE = "submitted by cold_run_seven_nations.py [subjects: the exam's persons] (the wrap's scene); consumed by law_seven_nations (cold_run_seven_nations.py) -> %s"
INK = "Deut 7:1-26; Onkelos Deut 7:1-26 (the export's division the DB's — the identity; the supplied doctrine at 7:10, 'His Shekhinah is among you' at 7:21); the Sifrei on Deuteronomy SILENT on the chapter (37:1 on 11:10 the translator's interpolation, 50:4 on 11:23, 61:7 on 12:3 its three rows from elsewhere); the kin by CREDIT — the angel's clauses Exodus 23:20-33, the renewed covenant 34:11-16, the dispossession Numbers 33:50-56; the reading ledger deu_07_vaetchanan_ekev_2026-09-17.md (29 sources, 6 claims); the exam docket deu_07_vaetchanan_ekev_exam_2026-09-18.md (520 rows READ WHOLE FROM THE START: LAW 145 / DERIVATION 34 / DISPUTE 110 / CONTEXT 156 / OUTSIDE 75)"
D, X, N_ = 'Deut', 'Exod', 'Num'
KINDS = [
 ("nations_devoted", "statute",   # STATUTE — the own-day giving of a law passes the stitcher's register test BY FORM (chapters 4 and 6 the form)
  "the seven nations devoted — 'WHEN THE LORD YOUR GOD BRINGS YOU INTO THE LAND … and clears away many nations before you, the Hittite, the Girgashite, the Amorite, the Canaanite, the Perizzite, the Hivite and the Jebusite, SEVEN NATIONS greater and mightier than you; and the LORD your God gives them before you and you smite them: you shall UTTERLY DEVOTE them, you shall make no covenant with them and show them no favor; you shall not intermarry with them — your daughter you shall not give to his son, nor his daughter take for your son, for he will turn your son from following me; but thus you shall do to them: their altars you shall break down, their pillars shatter, their Asherim cut down and their graven images burn with fire' (Deut 7:1-5) — THE CHAPTER'S FIRST LINE, spoken on the counter's day (40, 11, 1) in Moses' speech, NO marker (the speech continuing from chapter 6's own-day lines): the parser's [7] at 7:1 with the seven gentilic tokens as its own witness (seven where every Exodus list has six — the Girgashite absent there); THE BAN the code's hole (Exodus 23 says cut off and drive out, Numbers 33 dispossess; the tape's devotings of Sihon, Og and Hormah RUNS before the spec) — commanded valued devote_the_seven_nations a DEBIT on Israel OPEN to Joshua; NO FAVOR the code's hole — favor_barred (Avodah Zarah 20a's three readings: no land, no praise, no gift); covenant_barred (Exodus 23:32's block, its first tape write) and intermarriage_barred (34:16's, valued BOTH directions — the shelf: the seven nations by Torah law, the child follows the mother); the demolition a REFERENCE row against journeys' OPEN debit destroy_their_images (no second debit; the shelf's order — fell the Asherim, conquer, then eradicate)",
  HE(D, 7, 1, 5, "when the LORD your God brings you into the land"), WIT(D, 7, 1, 5) + WIT(X, 23, 32, 33) + WIT(X, 34, 12, 16) + WIT(N_, 33, 52, 52), INK, CORPUS,
  SUB % ("israel", "commanded valued devote_the_seven_nations on israel_people (a DEBIT OPEN to the run — Joshua), covenant_barred, favor_barred, intermarriage_barred (three BLOCKS) on the counter's day (40, 11, 1)"), ["nations", "objects"]),
 ("hearing_blessed", "statute",
  "hearing blessed — 'AND IT SHALL BE, BECAUSE YOU HEAR these judgments and keep and do them, the LORD your God will keep for you the covenant and the kindness which he swore to your fathers; and he will love you and bless you and multiply you — the fruit of your womb and the fruit of your ground, your grain, your wine and your oil, the increase of your cattle and the young of your flock, on the land which he swore to your fathers to give you; blessed shall you be above all peoples: there shall not be male or female barren among you or among your cattle; and the LORD will remove from you all sickness, and none of the evil diseases of Egypt which you knew will he put upon you, but he will lay them on all who hate you; and you shall CONSUME all the peoples which the LORD your God gives you — your eye shall not PITY them, and you shall not serve their gods, for that is a snare to you' (Deut 7:12-16) — THE CHAPTER'S SECOND LINE on the counter's day (40, 11, 1), NO marker, the portion's edge at 7:12 inside the unit; 'because' the heel read as 'in consequence of' (the five seats; Onkelos 'in exchange for'); blessings_for_hearing a conditional HEAVEN entry on Israel (the form of treasured_people; NOT blessing_promised — Abram's ladder entry already in the registry — Exodus 19:5-6's condition read back); NO PITY the code's hole — pity_barred a BLOCK ('your eye shall not pity' the book's five seats, this the first; NO ROW on the shelf cites 7:16 for the pity — the write stands on the ink alone); 'consume' the war's spoil only (Bava Kamma 113b — robbing a gentile prohibited); the snare 23:33's, no serving the second word's clause (no second write)",
  HE(D, 7, 12, 16, "and it shall be, because you hear these judgments"), WIT(D, 7, 12, 16) + WIT(X, 23, 25, 26) + WIT(X, 15, 26, 26) + WIT(X, 19, 5, 6), INK, CORPUS,
  SUB % ("israel", "blessings_for_hearing on israel_people (a conditional HEAVEN entry) and pity_barred (a BLOCK) on the counter's day (40, 11, 1)"), ["condition", "blessings"]),
 ("abomination_barred", "statute",
  "the abomination barred — 'THE GRAVEN IMAGES OF THEIR GODS YOU SHALL BURN WITH FIRE; you shall not covet the silver and gold on them and take it for yourself, lest you be snared by it, for it is an abomination to the LORD your God; and you shall not bring an abomination into your house, and become devoted like it: you shall utterly detest it and utterly abhor it, for it is devoted' (Deut 7:25-26) — THE CHAPTER'S THIRD LINE on the counter's day (40, 11, 1), NO marker; 'you shall not covet' the tenth word's verb moved from the neighbor's house to the idols' silver and gold (7:25 and Exodus 20:17 the form's two seats; Achan's Joshua 7:21 the run's case) — coveting_barred stands, no second write (the readback row TURNED); THE ABOMINATION INTO THE HOUSE the code's hole — house_abomination_barred a BLOCK (Mishnah Avodah Zarah 1:8-9 the renting for a residence, 3:6 the wall; Avodah Zarah 47b:10 a house bowed to; the impurity of the idol's stones — 7:26's doubled verb in Leviticus 11:43's form); 'devoted like it' — whatever you generate from it (the exchange, the exchange's exchange disputed — Avodah Zarah 54b), the Asherah's wood flogged under 7:26 (Makkot 22a)",
  HE(D, 7, 25, 26, "the graven images of their gods you shall burn with fire"), WIT(D, 7, 25, 26) + WIT(X, 20, 17, 17), INK, CORPUS,
  SUB % ("israel", "house_abomination_barred on israel_people (a BLOCK on the counter's day (40, 11, 1))"), ["objects", "devoted"]),
 ("seven_nations_case", "case", "the exam's rows on chapter 7 (Deut 7:1-26 — the three readings of 'show them no favor': Avodah Zarah 20a-20b, Mishnah Avodah Zarah 1:8, Tosefta Avodah Zarah 3:5; the marriage bar's scope and the child that follows the mother: Avodah Zarah 36b-37a, Kiddushin 68b, Yevamot 23a, Mishnah Kiddushin 3:12; the Asherah defined, its shade, its wood, the demolition's order, the renaming: Mishnah Avodah Zarah 3:5-3:10, Avodah Zarah 44b-46b, 47b-48b, 49b; the nullification, the money and ornaments on the idol, the immediacy, the interment: Mishnah Avodah Zarah 4:4-4:6, Avodah Zarah 42a-42b, 51b-52b, 53b-54b; the abomination into the house: Mishnah Avodah Zarah 1:9, 3:6; the devoted thing and the exchange: Avodah Zarah 54b, Kiddushin 58a, Makkot 22a; 'consume' the war's spoil: Bava Kamma 113b; the ban's condition and scope and the hornet: Sotah 35b-36a) — the exam's persons through the cells' asks: the renter of a house in the Land, the praiser of the beautiful gentile, the giver of the undeserved gift, the gentile woman's betrothed, the gentile mother's son, the planter who then worshipped, the sitter in the Asherah's shade, the one without another way, the Asherah's wood-burner, the finder of the money at the idol's head, the gentile who revokes his idol, the Jew who bent the idol, the renter for a residence, the robber of a gentile, the Canaanite outside the Land who repents",
  PHRASE(D, 7, 1, ['שבעה', 'גוים']) + " (seven nations — Deut 7:1)", WIT(D, 7, 1, 26), INK, CORPUS, CASE % "accepted / exempt / lashes (the exam's persons — the rule holds against him; outside the rule; flogged)", ["person", "ask"]),
]
assert len(KINDS) == 4, len(KINDS)
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
for e in ('accepted', 'exempt', 'lashes', 'commanded', 'covenant_barred', 'intermarriage_barred', 'treasured_people', 'other_gods_barred', 'coveting_barred', 'high_places_banned', 'nations_driven_out'):
    assert e in fx, e
HE_FAVOR = PHRASE(D, 7, 2, ['ולא', 'תחנם'])
HE_PITY = PHRASE(D, 7, 16, ['לא', 'תחס', 'עינך', 'עליהם'])
HE_BLESS = PHRASE(D, 7, 12, ['ושמר', 'יהוה', 'אלהיך', 'לך', 'את', 'הברית', 'ואת', 'החסד'])
HE_HOUSE = PHRASE(D, 7, 26, ['ולא', 'תביא', 'תועבה', 'אל', 'ביתך'])
NEW = [
 ('favor_barred', 'block',
  "favor barred — the BLOCK the chapter's first line writes on Israel: 'and show them no favor' (7:2 — the verb's one seat in this form; the Torah's six seats of the root as a verb: Jacob's 'graciously given', Joseph's blessing, 'I will be gracious'): THE CODE'S HOLE compiled here — no cell in any runner held it (the recon over all sixty-one); THE THREE READINGS of the one defective verb (Avodah Zarah 20a:1-4, the baraita): no chance to ENCAMP — no house rented, nothing attached to the ground sold in the Land (Mishnah Avodah Zarah 1:8; R. Meir / R. Yosei on the Land, Syria and abroad; the sale on condition of cutting, 20b:12-15), no FAVOR by praising ('how beautiful is this gentile woman' — Rav, 20a:9; the thanks to the Creator excepted, 20a:11), no UNDESERVED GIFT (Tosefta Avodah Zarah 3:5; R. Yehuda against R. Meir on 14:21, 20a:5-8); Onkelos 'have no MERCY on them' (7:2, 13:9); written on the counter's day (40, 11, 1), no marker",
  HE_FAVOR + " (and show them no favor — Deut 7:2)",
  "Deut 7:2 ('and show them no favor' — the one seat); Deut 14:21 (the carcass given or sold — the gift reading's dispute), 13:9 (Onkelos's 'mercy' the second seat); Onkelos 7:2; Mishnah Avodah Zarah 1:8; Tosefta Avodah Zarah 3:5; Babylonian Talmud Avodah Zarah 20a:1-11, 20b:12-19",
  f"deu_07_nations_cherem (STEP_Dt_7_2; the claims {CL[0]} through {CL[-1]})",
  "cold_run_seven_nations.py (F1 the_seven_nations — no_favor; the exam kind seven_nations_case; the block written on the tape kind nations_devoted)"),
 ('pity_barred', 'block',
  "pity barred — the BLOCK the chapter's second line writes on Israel: 'your eye shall not pity them' (7:16 — the book's five seats: 7:16 the first, then 13:9 the enticer, 19:13 the murderer, 19:21 the false witness, 25:12 the woman's hand; the eye the subject, third person feminine): THE CODE'S HOLE compiled here — no cell in any runner held the pity (the recon: 'pity' nowhere); NO ROW ON THE SHELF cites 7:16 for the pity (the docket's scan: verse 16 once, Bava Kamma 113b on 'consume') — the write stands on the ink alone, its exam rows the book's later seats forward; 'and you shall consume all the peoples' the same verse — the war's spoil only, robbing a gentile prohibited (Bava Kamma 113b:7); written on the counter's day (40, 11, 1), no marker",
  HE_PITY + " (your eye shall not pity them — Deut 7:16)",
  "Deut 7:16 (the first seat of 'your eye shall not pity'); Deut 13:9, 19:13, 19:21, 25:12 (the four seats forward); Deut 7:16 'consume' — Babylonian Talmud Bava Kamma 113b:7; Onkelos 7:16 ('finish off')",
  f"deu_07_nations_cherem (STEP_Dt_7_16; the claims {CL[0]} through {CL[-1]})",
  "cold_run_seven_nations.py (F4 because_you_hear — consume_no_pity; the exam kind seven_nations_case; the block written on the tape kind hearing_blessed)"),
 ('blessings_for_hearing', 'heaven',   # NOT blessing_promised — that name is Abram's ladder entry (Genesis 12:2-3; 26:24), found in the registry at the types step: the census decides
  "the blessings for hearing — the conditional HEAVEN entry the chapter's second line writes on Israel (the form of treasured_people — Exodus 19:5-6's 'if you will hear My voice and keep My covenant' read back at 7:12): 'because you hear these judgments and keep and do them, the LORD your God will keep for you the covenant and the kindness which he swore to your fathers' (7:12 — 'because' the heel as a conjunction, the five seats; Onkelos 'in exchange for'), the blessing's list (7:13 — the fruit of the womb and of the ground, the grain, the wine and the oil, the increase of the cattle and the young of the flock: 28:4, 11, 18, 51 forward; the flock's word tagged a name in the DB's morphology), 'blessed above all peoples' (7:14 — no barren, Exodus 23:26's clause restated; Bekhorot 44b), the sickness removed (7:15 — Exodus 15:26's healer TURNED: the diseases of Egypt laid on those who hate you; 28:60 forward; Bava Metzia 107b the evil eye); the entry OPEN on the condition; written on the counter's day (40, 11, 1), no marker",
  HE_BLESS + " (the LORD your God will keep for you the covenant and the kindness — Deut 7:12)",
  "Deut 7:12-15; Exodus 19:5-6 (the offer's condition — the tape's covenant_offered), 23:25-26 (the bread and water blessed, no barren — ordinances.land by CALL), 15:26 (the healer's condition — exodus_story.marah by CALL); Deut 28:4, 11, 18, 51, 60 (forward); Onkelos 7:12-15; Babylonian Talmud Bekhorot 44b:7, Bava Metzia 107b:2, Berakhot 51b:5, Chullin 84b:1",
  f"deu_07_nations_cherem (STEP_Dt_7_12 through STEP_Dt_7_15; the claims {CL[0]} through {CL[-1]})",
  "cold_run_seven_nations.py (F4 because_you_hear — covenant_kept, the_blessing_list, no_barren, the_diseases; the exam kind seven_nations_case; the entry written on the tape kind hearing_blessed)"),
 ('house_abomination_barred', 'block',
  "the abomination barred from the house — the BLOCK the chapter's third line writes on Israel: 'and you shall not bring an abomination into your house, and become devoted like it; you shall utterly detest it and utterly abhor it, for it is devoted' (7:26 — 'you shall not bring an abomination into your house' the one seat; 'devoted like it' one; the doubled verbs two: the detesting Leviticus 11:43's, the abhorring 23:8's): THE CODE'S HOLE compiled here — no cell in any runner held the abomination into the house (the recon); THE EXAM: the renting for a residence barred everywhere — the house still a Jew's by name (Mishnah Avodah Zarah 1:8-9; Avodah Zarah 15a:7, 21a:2), the wall against the idol's house withdrawn four cubits (Mishnah 3:6; 47b:4-8), A HOUSE BOWED TO forbidden (Rav, 47b:10), the impurity of the idol's stones, wood and dust — a creeping animal (7:26's verb in Leviticus 11:43's form) or a menstruant by carrying (R. Akiva; Shabbat 82b, Tosefta Zavim 5:6), no consecration to an idol by word (44b:14); 'devoted like it' — whatever you GENERATE from it (the birds, the money of its sale, the animal exchanged: Chullin 140a, Kiddushin 58a, Temurah 30b, Avodah Zarah 54b:3), the exchange's exchange two arms (54b:4-5), THE ASHERAH'S WOOD FLOGGED under 7:26 (Makkot 22a:3; Pesachim 48a:6); the Sifrei 61:7's renaming for the worse on the doubled verbs; written on the counter's day (40, 11, 1), no marker",
  HE_HOUSE + " (and you shall not bring an abomination into your house — Deut 7:26)",
  "Deut 7:26 (the one seat); Deut 7:25 ('an abomination to the LORD your God' — the book's five; 'abomination' thirteen Deuteronomy seats, 7:25-26 the first two), 13:18 (the devoted thing's second seat — 'nothing of the devoted shall cleave to your hand'), 12:3 (forward); Leviticus 11:43 (the detesting verb — shemini.classify by CALL); Onkelos 7:26 ('detest … keep far'; the devoted word 7:26 and 13:18); the Sifrei on Deuteronomy 61:7; Mishnah Avodah Zarah 1:8-9, 3:6; Babylonian Talmud Avodah Zarah 15a:7, 21a:2, 47b:1-12, 54b:3-11, Kiddushin 58a:7-12, Chullin 140a:12, Temurah 30b:7, Makkot 22a:2-3, Pesachim 48a:6, Shabbat 82b:1; Tosefta Zavim 5:6",
  f"deu_07_nations_cherem (STEP_Dt_7_25 through STEP_Dt_7_26; the claims {CL[0]} through {CL[-1]})",
  "cold_run_seven_nations.py (F6 the_images_and_the_devoted — into_your_house, devoted_like_it, utterly_detest; the exam kind seven_nations_case; the block written on the tape kind abomination_barred)"),
]
added = 0
for name, op, en, he, ink, corpus, exam in NEW:
    if name in fx: continue
    text = text.rstrip('\n') + '\n' + f"  {name}:\n    en: {q(en)}\n    he: {q(he)}\n    ledger_op: {op}   # THE DEUTERONOMY WALK 5b (2026-09-18): chapter 7's compile — {name}\n    ink: {q(ink)}\n    corpus: {q(corpus)}\n    exam: {q(exam)}\n"
    added += 1
open(path, 'w', encoding='utf-8').write(text)
fx = yaml.safe_load(open(path, encoding='utf-8'))['effects']
assert all(n in fx for n, *_ in NEW) and fx['favor_barred']['ledger_op'] == 'block' and fx['pity_barred']['ledger_op'] == 'block' and fx['blessings_for_hearing']['ledger_op'] == 'heaven' and fx['house_abomination_barred']['ledger_op'] == 'block'
print('effects: %d added (registry %d); the he found in the verses: %s | %s | %s | %s' % (added, len(fx), HE_FAVOR, HE_PITY, HE_BLESS, HE_HOUSE))
# ---- NO registry row (Israel the written-on party, standing; the seven nations a counterparty string) ----
reg = yaml.safe_load(open(f"{ROOT}/logic/corpus/entity_registry.yaml", encoding='utf-8'))
ids = {e['id'] for e in reg['entities']}
assert 'israel_people' in ids, 'the written-on party must stand'
assert not any(i in ids for i in ('the-nations', 'the-hittite', 'the-girgashite', 'the-canaanite', 'the-perizzite', 'the-hivite', 'the-jebusite', 'the-seven-nations')), 'the seven nations have no entity — a counterparty string'
print('entities: none added (registry %d); the-amorite present: %s (Sihon\'s, untouched)' % (len(reg['entities']), 'the-amorite' in ids))
# ---- the daemon block + the functions block (daemon_dispositions.yaml) ----
path = f"{ROOT}/World/step9/daemon_dispositions.yaml"
text = open(path, encoding='utf-8').read()
if '  law_seven_nations:' not in text:
    block = '''  law_seven_nations:
    file: cold_run_seven_nations.py
    wraps: seven_nations
    given_at: Deut 7:1
    installed_by: boot   # THE DEUTERONOMY WALK 5b (2026-09-18): THE BAN'S FIRST AND ONLY GIVING — the chapter's own line on the counter's day (40, 11, 1), no marker (the speech continuing from chapter 6's own-day lines); installed by boot like law_opening_speech, law_obey_horeb and law_hear_o_israel (the Deuteronomy daemons' form); the code's four holes compiled here (the ban, no favor, no pity, the abomination into the house); the debit and the blocks written at the chapter's own lines; the readback on the kin (Exodus 23, 34, Numbers 33, the two words) a REFERENCE table, no second write
    watches:
      nations_devoted: [commanded, covenant_barred, favor_barred, intermarriage_barred]   # Deut 7:1-5: the ban a DEBIT on Israel valued devote_the_seven_nations, OPEN to Joshua; no covenant (23:32's block, its first tape write), no favor (NEW — the three readings), no marriage (34:16's block valued both directions, its first tape write) — four writes on Israel on the counter's day
      hearing_blessed: [blessings_for_hearing, pity_barred]   # Deut 7:12-16: the covenant kept and the blessings — a conditional HEAVEN entry (NEW, the form of treasured_people); 'your eye shall not pity' a BLOCK (NEW — no row on the shelf; the ink alone); 'consume' the war's spoil (Bava Kamma 113b); no serving the second word's clause, no second write
      abomination_barred: [house_abomination_barred]   # Deut 7:25-26: 'you shall not bring an abomination into your house' a BLOCK (NEW); 'you shall not covet' the tenth word's — coveting_barred stands, no second write; the images burned the demolition's reference row
      seven_nations_case: [accepted, exempt, lashes]   # the exam's rows on the chapter — the persons through the cells' asks (the renter of a house in the Land accepted, the thanks-giver exempt, the Asherah's wood-burner flogged …)
'''
    i = text.index('  law_census:')
    text = text[:i] + block + text[i:]
if '\n  seven_nations:   # THE DEUTERONOMY WALK 5b' not in text:
    fb = '''  seven_nations:   # THE DEUTERONOMY WALK 5b (2026-09-18)
    the_seven_nations: {status: WRAPPED, by: law_seven_nations}
    the_holy_people: {status: WRAPPED, by: law_seven_nations}
    the_faithful_god: {status: WRAPPED, by: law_seven_nations}
    because_you_hear: {status: WRAPPED, by: law_seven_nations}
    do_not_fear: {status: WRAPPED, by: law_seven_nations}
    the_images_and_the_devoted: {status: WRAPPED, by: law_seven_nations}
'''
    i = text.index('  hear_o_israel:   # THE DEUTERONOMY WALK 4b')
    j = text.index('\n  pre_sinai:', i)
    text = text[:j + 1] + fb + text[j + 1:]
open(path, 'w', encoding='utf-8').write(text)
dd = yaml.safe_load(open(path, encoding='utf-8'))
assert 'law_seven_nations' in dd['daemons'] and 'seven_nations' in dd['functions'], (list(dd)[:5])
print('daemons: %d (law_seven_nations %s); functions blocks: %d' % (len(dd['daemons']), 'law_seven_nations' in dd['daemons'], len(dd['functions'])))
# ---- the dependency span + the CALL edges by the ink (the token-demanded edges and the POINTERS after the gate's print) ----
path = f"{ROOT}/World/step9/dependency_dispositions.yaml"
text = open(path, encoding='utf-8').read()
if '\n  seven_nations:' not in text.split('\nedges:')[0]:
    a = "  hear_o_israel: [[Deut, 6, 1, 25]]"
    i = text.index(a); j = text.index('\n', i)
    text = text[:j + 1] + "  seven_nations: [[Deut, 7, 1, 26]]   # THE DEUTERONOMY WALK 5b (2026-09-18; DEUTERONOMY_WALK.md \"Sitting 5b\"): chapter 7 — THE SEVEN NATIONS: the ban, no favor, no pity and the abomination into the house compiled for the first time (the code's four holes); the old code said again for the new place — THE READBACK ON THE KIN (the laws' form on Exodus 23, 34, Numbers 33 and the two words: twenty-one reference rows, no second write); three lines on the counter's day, no marker\n" + text[j + 1:]
    W = "THE DEUTERONOMY WALK 5b (2026-09-18) | "
    edges = f'''  - {{from: seven_nations, to: ordinances, disposition: CALL, link: reference, carries: verdict,
     why: "{W}7:2's 'you shall make no covenant with them' is 23:32's ban (OR.land('no_covenant') CALLED — covenant_barred its effect, written here for the first time on the tape at nations_devoted, CQ3); 7:16's snare 23:33's (OR.land('not_dwell')); 7:13-15's blessing 23:25-26's bread and water and no barren (OR.land('bread_water', 'no_barren')); 7:20's hornet 23:28's (OR.land('hornet')); 7:22's little by little 23:29-30's (OR.land('little_by_little')); 7:23-24's confusion and the inhabitants into your hand 23:27, 23:31's (OR.land('borders')); 7:5's demolition beside 23:24's (OR.land('break_pillars')) — the readback's rows 7:2, 7:13-15, 7:14, 7:16, 7:20, 7:22, 7:23-24 graded against the angel's clauses BY CALL"}}
  - {{from: seven_nations, to: erection, disposition: CALL, link: reference, carries: verdict,
     why: "{W}7:1's six-name kin 34:11's (ER.covenant('nations_seven_orders') CALLED — seven orders, only Deuteronomy the seventh name); 7:2's no covenant 34:12, 15's (ER.covenant('no_covenant_by_call')); 7:3's marriage bar BOTH WAYS against 34:16's one direction (ER.covenant('daughters_two_seats', 'intermarriage_channels', 'child_follows_mother') — intermarriage_barred its effect, written here for the first time on the tape valued both directions, CQ3; Kiddushin 68b's rule already in that cell); 7:5's four objects against 34:13's three (ER.covenant('cut_four', 'pillars_exod', 'demolition_grows')); the exam's Mishnah Avodah Zarah rows CREDITED from the erection docket (ER.covenant('sheet_az_3_5', 'sheet_az_4_2', 'sheet_az_4_4'))"}}
  - {{from: seven_nations, to: journeys, disposition: CALL, link: reference, carries: verdict,
     why: "{W}7:1's 'clears away' and 7:17's 'to dispossess them' are 33:52-53's dispossession (JO.the_command('drive_out') CALLED — the debit commanded valued dispossess_the_inhabitants_and_possess_the_land OPEN on the world, CQ5); 7:5's demolition a REFERENCE ROW against journeys' OPEN debit destroy_their_images (JO.the_command('figured_stones', 'molten_images', 'high_places', 'three_objects_own') — the three objects there, the four here; NO second debit, R1)"}}
  - {{from: seven_nations, to: covenant_at_horeb, disposition: CALL, link: reference, carries: verdict,
     why: "{W}7:9's 'to a thousand generations, those who love him and keep his commandments' and 7:10's 'repays those who hate him to his face' are the second word's visiting clause (CH.the_second_word('the_visiting') CALLED — 5:9-10; the readback rows 7:9 VARIANT, 7:10 TURNED); 7:16's 'you shall not serve their gods' the second word's head (CH.the_second_word('no_other_gods') — other_gods_barred stands, NO second write, CQ5); 7:25's 'you shall not covet' the tenth word's verb (CH.the_tenth_word('covet_and_desire') — coveting_barred stands, NO second write, CQ7; the readback row 7:25 TURNED: the object moved from the neighbor's house to the idols' silver and gold); 7:11's triad the charge's line stand_here_commanded (5:31 — the row 7:11 VERBATIM in kind)"}}
  - {{from: seven_nations, to: decalogue, disposition: CALL, link: reference, carries: verdict,
     why: "{W}7:9's clause and 7:25's verb have their FIRST copies at Exodus 20:5-6 and 20:17 (the readback names both copies — 5:9-10 / 20:5-6, 5:21 / 20:17); 7:8's 'the oath which he swore' — the oath's noun starred by the parser (the seven-stem homograph) — beside the third word's cell (DC.vain_name('vain_oath', 'false_future_oath') CALLED for the oath's prohibition side, 4b's form at 6:13)"}}
  - {{from: seven_nations, to: exodus_story, disposition: CALL, link: reference, carries: verdict,
     why: "{W}7:6's 'a treasured people' is 19:5-6's offer (ES.sinai('treasure_seats') CALLED — treasured_people on the world a heaven entry, CQ5; the readback row 7:6 EXPANDED against the tape's covenant_offered, FOUND by kind and first verse); 7:12's 'because you hear' 19:5's condition (VARIANT); 7:8's 'brought you out with a strong hand' the tape's brought_out (12:51 — EXPANDED); 7:15's diseases 15:26's healer (ES.marah('healer_condition') — TURNED, the diseases redirected); 7:18-19's plagues, trials, signs and wonders, the hand and the arm the ten plague_struck lines and the sea (ES.plagues('ten'), ES.sea('saved_seat'), ES.trials('ten_list', 'count_by_exodus') — SHORTENED); 7:24's 'destroy their name from under heaven' Amalek's phrase (ES.amalek('blotting') — blotting_sworn's 17:14)"}}
  - {{from: seven_nations, to: obey_horeb, disposition: CALL, link: reference, carries: verdict,
     why: "{W}7:7-8's 'the LORD set his love on you and chose you … because of the LORD's love for you' is 4:37's 'because he loved your fathers' (OH.the_one_god('because_he_loved_your_fathers') CALLED — the readback row 7:6 names 4:37's 'chose'); 7:9's 'he is God' 4:35, 39's creed (OH.the_one_god('you_were_shown')); 7:17's 'to dispossess them' and 7:1's 'greater and mightier than you' 4:38's (OH.the_one_god('to_dispossess_nations')); 7:19's 'the great trials which your eyes saw' 4:34's list"}}
  - {{from: seven_nations, to: hear_o_israel, disposition: CALL, link: reference, carries: verdict,
     why: "{W}7:11's 'the commandment, the statutes and the judgments' is the triad's third seat (5:31, 6:1, 7:11 — HI.the_header('the_triad') CALLED, its verdict names 7:11 forward); 7:21's 'the LORD your God is in your midst, a great and awesome God' 6:15's pair (HI.the_gift_and_the_warning('the_jealous_god') — Onkelos 'his Shekhinah is among you' at both); 7:4's 'and the anger of the LORD will burn against you' 6:15's; chapter 6's own-day lines the tape's last before this chapter's three"}}
  - {{from: seven_nations, to: opening_speech, disposition: CALL, link: reference, carries: verdict,
     why: "{W}7:17's 'these nations are more than I; how can I dispossess them' is the spies' fear read back at 1:28 (OS.the_spies_read_back('the_murmuring') CALLED — 'our brothers have melted our heart: a people greater and taller than we'); 7:1's 'greater and mightier than you' 1:28's and 4:38's; the tape's own DEVOTINGS the east's — sihons_cities_devoted (2:34) and ogs_cities_devoted (3:6), RUNS before the ban's spec (the DATA row the_devotings; OS.READBACK the first form); the oath's seats 1:8's"}}
  - {{from: seven_nations, to: mamre, disposition: CALL, link: reference, carries: verdict,
     why: "{W}7:8, 7:12 and 7:13's 'the oath which he swore to your fathers' — the oath's lines on the tape: sworn_by_himself at Genesis 22:16-18 (MA.moriah('test_verb_seats') CALLED), oath_upheld at 26:3-5 (MA.isaac_gerar('famine_ordinal')); the RUN_CITATION pointers at Deut 7:8 / 7:12 / 7:13 name them (6:10's form)"}}
  - {{from: seven_nations, to: joseph, disposition: CALL, link: reference, carries: verdict,
     why: "{W}the oath's third line — visitation_promised at Genesis 50:24 'the land which he swore to Abraham, to Isaac and to Jacob' (JS.the_oath('kindness_and_truth') CALLED — the three names' first joint telling on the tape; 7:8's 'the oath' the noun's one Deuteronomy seat, starred by the parser)"}}
  - {{from: seven_nations, to: balak, disposition: CALL, link: reference, carries: verdict,
     why: "{W}7:4's reason 'for he will turn your son from following me' has its exhibit on the tape at Shittim — the whoring after the daughters of Moab and the yoke to Baal Peor (Numbers 25:1-3; BK.peor('spec_run') CALLED — Exodus 34:15-16's spec RUN there): the DATA row the_shittim_exhibit; the marriage bar's reason the shelf's chain wine → daughters → idolatry (Avodah Zarah 36b:4); the offering to the dead's tent-impurity from the Shittim verse (48b:6)"}}
  - {{from: seven_nations, to: shemini, disposition: CALL, link: reference, carries: verdict,
     why: "{W}7:26's 'you shall utterly DETEST it' is Leviticus 11:43's verb (the detesting root's six Torah seats — Leviticus 11:11, 13, 43, 20:25 and 7:26's two): the shelf reads the idol's impurity from the creeping animal's form (Avodah Zarah 47b:2; Tosefta Zavim 5:6 'idol worship is like a creeping thing') — SH.classify CALLED for the classifier's own verdict on a creeping thing (the live edge), the verb by REFERENCE"}}
  - {{from: sequence, to: seven_nations, disposition: CALL, link: none,
     why: "{W}the sequential run's REGISTRATION edge — ('cold_run_seven_nations', 'law_seven_nations') in DAEMON_ORDER (the runner compiles no verse: link none, O4's license); the three tape lines this sitting's on the counter's day, NO marker; the daemon's debit, blocks and heaven entry written on its own lines"}}
'''
    a = "  - {from: sequence, to: hear_o_israel, disposition: CALL, link: none,"
    i = text.index(a); j = text.index('\n', text.index('why:', i)) + 1
    text = text[:j] + edges + text[j:]
    open(path, 'w', encoding='utf-8').write(text)
dep = yaml.safe_load(open(path, encoding='utf-8'))
n_ch = sum(1 for e in dep['edges'] if e['from'] == 'seven_nations')
assert 'seven_nations' in dep['spans'] and n_ch == 13, n_ch
print('dependency: span + 14 edges (seven_nations 13 CALL and the registration); the token-demanded edges and the pointers after the gate\'s print')
# ---- the installation probe's count ----
path = f"{ROOT}/World/step9/installation_probes.py"
text = open(path, encoding='utf-8').read()
if "len(real) == 66 and all(" in text:
    old = "len(real) == 66 and all('given_at' in d and 'installed_by' in d for d in real.values())   # THE DEUTERONOMY WALK 4b (2026-09-17): 65 -> 66,"
    assert text.count(old) == 1, text.count(old)
    text = text.replace(old, "len(real) == 67 and all('given_at' in d and 'installed_by' in d for d in real.values())   # THE DEUTERONOMY WALK 5b (2026-09-18): 66 -> 67, law_seven_nations (given_at Deut 7:1 — the ban's own giving; installed_by boot); 4b: 65 -> 66,")
    open(path, 'w', encoding='utf-8').write(text)
assert "len(real) == 67" in open(path, encoding='utf-8').read()
print('installation_probes I5: 67')
