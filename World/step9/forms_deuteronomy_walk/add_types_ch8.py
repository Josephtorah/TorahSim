import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE DEUTERONOMY WALK sitting 6b — THE COMPILE OF CHAPTER 8 (2026-09-19; World/step9/DEUTERONOMY_WALK.md "Sitting 6b"): THE TYPES FIRST — THREE tape
# kinds (grace_commanded 8:7-10 — the good land's clause and the command to eat, be satisfied and bless; forgetting_warned 8:11-18 — the warning, the
# growth, the heart, the chain, the boast, the covenant established; perishing_testified 8:19-20 — the case, the testimony, the measure for measure), all
# STATUTE by form (the own-day giving of a law — chapters 4, 6 and 7 the form), ONE case kind (good_land_case), TWO new effects (bless_after_eating_commanded
# a STATUS, forgetting_barred a BLOCK — both on Israel; the testimony REUSES heaven_and_earth_witness, law_obey_horeb's effect at 4:26, read at the design
# from the watches), NO registry row (Israel the written-on party; the manna, the rock and the serpent already rows, untouched), the 68th daemon's block
# (law_good_land, given_at Deut 8:1 — the chapter's frame; installed_by boot — the four Deuteronomy daemons' form), the functions block (six cells WRAPPED),
# the dependency span and the thirteen CALL edges by the ink with the registration edge (the design's fourteenth, decalogue, dropped at the callees' print — no cell on the second word there), the installation probe's count 67 -> 68. The `he` is cut from the
# pointed DB text by FINDING the phrase's tokens (never a typed index); the claim ids and the step ids READ from the frozen unit. Idempotent (add_types_ch7.py's
# form, derived by hand where it differs).
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
unit = open(f'{ROOT}/logic/units/deu_08_manna_humility.yaml', encoding='utf-8').read()
CL = sorted(set(re.findall(r'DV08-\d+', unit))); ST = sorted({int(x) for x in re.findall(r'STEP_Dt_8_(\d+)', unit)})
assert len(CL) == 6 and ST[0] == 1 and ST[-1] == 20, (CL, ST[:3], ST[-1])
CORPUS = f"deu_08_manna_humility (STEP_Dt_8_1 through STEP_Dt_8_20; claims {CL[0]} through {CL[-1]})"
SUB = "submitted by cold_run_good_land.py [subjects: %s] (the narrative scene, THE DEUTERONOMY WALK 6b); re-submitted on the sequential tape by cold_run_sequence.py; consumed by law_good_land (cold_run_good_land.py) -> %s"
CASE = "submitted by cold_run_good_land.py [subjects: the exam's persons] (the wrap's scene); consumed by law_good_land (cold_run_good_land.py) -> %s"
INK = "Deut 8:1-20; Onkelos Deut 8:1-20 (the export's division the DB's — the identity; the Memra (the Word) at 8:3 and 8:20, the fear supplied at 8:11, 8:14, 8:19, the shoes at 8:4, the counsel at 8:18); the Sifrei on Deuteronomy SILENT on the chapter (its sixteen rows from elsewhere read whole — 19:2, 32:10-15, 37:5, 39:4-8, 40:10, 43:7, 48:8, 48:10, 53:1, 297:4, 313:15, 318:1); the kin by CREDIT — the manna Exodus 16, the rock 17:1-7 and Numbers 20, the serpents Numbers 21:4-9, the decree 14:26-35, the craving 11; the reading ledger deu_08_ekev_2026-09-18.md (36 sources, 6 claims); the exam docket deu_08_ekev_exam_2026-09-19.md (451 rows READ WHOLE FROM THE START: LAW 80 / DERIVATION 82 / DISPUTE 36 / CONTEXT 160 / OUTSIDE 93)"
D, X, N_ = 'Deut', 'Exod', 'Num'
KINDS = [
 ("grace_commanded", "statute",   # STATUTE — the own-day giving of a law passes the stitcher's register test BY FORM (chapters 4, 6 and 7 the form)
  "the grace after the meal commanded — 'FOR THE LORD YOUR GOD BRINGS YOU TO A GOOD LAND, a land of brooks of water, of springs and deeps flowing out in the valley and in the hill; a land of wheat and barley, of vines and fig trees and pomegranates, a land of olive oil and honey; a land in which you shall eat bread without poverty, you shall not lack anything in it, a land whose stones are iron and out of whose hills you may hew copper; AND YOU SHALL EAT AND BE SATISFIED AND BLESS THE LORD YOUR GOD for the good land which he has given you' (Deut 8:7-10) — THE CHAPTER'S FIRST LINE, spoken on the counter's day (40, 11, 1) in Moses' speech, NO marker (the speech continuing from chapter 7's own-day lines); THE SEVEN SPECIES at 8:8 alone in the Bible (the first fruits' species, Mishnah Bikkurim 1:3; the order of blessings by the verse and its two 'land's, Berakhot 41a-b; the measures from the verse, Eruvin 4a); 'you shall not lack anything' 2:7's receipt; THE TORAH'S ONE COMMAND TO BLESS HIM — the code's hole (no cell in any runner held it): bless_after_eating_commanded a STATUS on Israel (the form of shema_commanded); the grace BY TORAH LAW (Berakhot 21a; Mishnah Berakhot 7:1-2 the zimmun (the invitation), 20b:16 the after by the Torah, the before by the Sages; 48b the four blessings from the verse; 49b:9 the measure of 'satisfied' a PARAMETER; 49b:4 the grace conditional on eating, not an obligation; 44a:10 'a land' concluded the matter — bread the object)",
  HE(D, 8, 7, 10, "for the LORD your God brings you to a good land"), WIT(D, 8, 7, 10) + WIT(X, 23, 25, 25) + WIT(D, 6, 10, 11) + WIT(D, 2, 7, 7), INK, CORPUS,
  SUB % ("israel", "bless_after_eating_commanded on israel_people (a STATUS, the counter's day (40, 11, 1), no marker)"), ["land", "command"]),
 ("forgetting_warned", "statute",
  "the forgetting warned — 'TAKE HEED TO YOURSELF LEST YOU FORGET THE LORD YOUR GOD, so as not to keep his commandments and his judgments and his statutes which I command you this day; lest, when you have eaten and are satisfied and have built good houses and dwelt in them, and your herds and your flocks multiply and your silver and gold multiply and all that you have multiplies, then your heart be lifted up and you forget the LORD your God who brought you out of the land of Egypt, out of the house of bondage; who led you through the great and terrible wilderness — fiery serpents and scorpions and thirsty ground where there was no water — who brought you water out of the rock of flint; who fed you manna in the wilderness which your fathers did not know, to humble you and to test you, to do you good in your end; and you say in your heart: my power and the might of my hand have gotten me this wealth — and you shall remember the LORD your God, for it is he who gives you power to get wealth, that he may establish his covenant which he swore to your fathers, as at this day' (Deut 8:11-18) — THE CHAPTER'S SECOND LINE on the counter's day (40, 11, 1), NO marker; 'take heed to yourself lest' 6:12's clause (six tokens shared) — 6:12's cell held the ask WITHOUT A WRITE: forgetting_barred a BLOCK on Israel, its first tape write ('beware, lest, not' nothing but a prohibition — Sotah 5a:3, Makkot 13b:5, Eruvin 96a:8; a prohibition without an action, no lashes — Makkot 13b:6); the growth's list 6:10-11's gift made the growth (the king's law's tokens 17:17, 17:20 forward); 'your heart be lifted up' ONE (Sotah 4b-5a arrogance as denial; 'filling his stomach' Berakhot 32a); the article + participle chain of five (who brought you out, who led you, who brought out, who fed you, who gives); the retelling's reference rows — brought_out, fiery_serpents_sent, rock_struck, manna_fell, the oath's three lines on the tape",
  HE(D, 8, 11, 18, "take heed to yourself lest you forget the LORD your God"), WIT(D, 8, 11, 18) + WIT(D, 6, 12, 12) + WIT(D, 17, 17, 17) + WIT(D, 5, 6, 6) + WIT(X, 17, 6, 6) + WIT(N_, 21, 6, 6), INK, CORPUS,
  SUB % ("israel", "forgetting_barred on israel_people (a BLOCK, the counter's day (40, 11, 1), no marker)"), ["warning", "chain"]),
 ("perishing_testified", "statute",
  "the perishing testified — 'AND IT SHALL BE, IF YOU SURELY FORGET THE LORD YOUR GOD and go after other gods and serve them and bow down to them, I TESTIFY AGAINST YOU THIS DAY THAT YOU SHALL SURELY PERISH; like the nations which the LORD makes to perish before you, so shall you perish, because you would not hearken to the voice of the LORD your God' (Deut 8:19-20) — THE CHAPTER'S THIRD LINE on the counter's day (40, 11, 1), NO marker; the two infinitive absolutes (the forgetting's the lemma's one such form in the Bible; 'surely perish' 4:26, 8:19, 30:18 alone); 'I testify against you this day' — 4:26's testimony (heaven and earth the witnesses there, 'I' here) REUSED: the effect heaven_and_earth_witness, law_obey_horeb's at witnesses_called (4:26), written here a second time at its second seat — no new effect (the watches read at the design); 'serve them and bow down to them' the second word's order reversed (serve-then-bow at 8:19, 11:16, 17:3, 29:25; bow-then-serve at 4:19, 30:17 and the ten words); 'like the nations … so shall you perish' the measure for measure against nations_devoted (7:1-5) and the heel's second seat (7:12, 8:20 — 'because' the noun; the one plural 'the LORD your God' of the chapter at 8:20)",
  HE(D, 8, 19, 20, "and it shall be, if you surely forget the LORD your God"), WIT(D, 8, 19, 20) + WIT(D, 4, 26, 26) + WIT(D, 5, 9, 9) + WIT(D, 7, 12, 12), INK, CORPUS,
  SUB % ("israel", "heaven_and_earth_witness on israel_people (REUSED — 4:26's effect at its second seat; the counter's day (40, 11, 1), no marker)"), ["case", "testimony"]),
 ("good_land_case", "case", "the exam's rows on chapter 8 (Deut 8:1-20 — the grace after meals by Torah law and its four blessings: Berakhot 21a, 48b, Tosefta Berakhot 6:1; the blessing before by inference, refuted, founded on reason: Berakhot 35a, 21a:5-6, 20b:16; the measure of 'satisfied': Berakhot 20b:14, 49b:9, Pesachim 49b, Yoma 79b, Mishnah Berakhot 7:2, Mishnah Sukkah 2:5; the grace conditional on eating, its persons, the meal's end and the reciter: Berakhot 49b:4, 20b:1-14, 42a:5-7, 43a:11-12, Arakhin 4a, Bava Metzia 114a; the order of blessings by the verse and its two 'land's, the measures: Berakhot 41a-b, Eruvin 4a, Sukkah 5b; the seven species' after-blessing and 'a land concluded the matter': Mishnah Berakhot 6:8, Berakhot 44a; the first fruits: Mishnah Bikkurim 1:3, 1:10, Menachot 84a-b; the manna's affliction and forms: Yoma 74b-76a; the afflictions of love: Berakhot 5a; arrogance: Sotah 4b-5a; 'beware, lest, not' a prohibition: Sotah 5a:3, Makkot 13b:5, Eruvin 96a:8; the grace in any language: Sotah 33a) — the exam's persons through the cells' asks: the eater of an olive-bulk, the eater of an egg-bulk, R. Tzadok with less than an egg-bulk, the priest at the atonement meal, the woman at the table, the minor who blesses for his father, the eater of consecrated food, the one who based his meal on wine, the one who forgot the New Moon in the grace, the one who forgot the Sabbath, the eater of dates before pomegranates, the eater of the seven species, the bringer of first fruits from beyond the Jordan, the one who blesses in another language, the scholar with an eighth of an eighth, the one who forgets without an act",
  PHRASE(D, 8, 7, ['ארץ', 'טובה']) + " (a good land — Deut 8:7)", WIT(D, 8, 1, 20), INK, CORPUS, CASE % "accepted / exempt / lashes (the exam's persons — the rule holds against him; outside the rule; flogged)", ["person", "ask"]),
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
# ---- TWO new effects, the ink's own words, the `he` FOUND in the verse; the testimony's effect REUSED (asserted present) ----
path = f"{ROOT}/World/step9/effect_vocabulary.yaml"
text = open(path, encoding='utf-8').read()
fx = yaml.safe_load(text)['effects']
for e in ('accepted', 'exempt', 'lashes', 'shema_commanded', 'test_barred', 'heaven_and_earth_witness', 'manna_provided', 'water_from_the_rock', 'serpents_sent', 'other_gods_barred', 'blessings_for_hearing', 'treasured_people', 'bread_and_water_blessed'):
    assert e in fx, e
assert fx['heaven_and_earth_witness']['ledger_op'] in ('status', 'heaven', 'block', 'debit'), fx['heaven_and_earth_witness']['ledger_op']
HE_BLESS = PHRASE(D, 8, 10, ['ואכלת', 'ושבעת', 'וברכת'])
HE_FORGET = PHRASE(D, 8, 11, ['השמר', 'לך', 'פן', 'תשכח'])
NEW = [
 ('bless_after_eating_commanded', 'status',
  "the blessing after the meal commanded — the STATUS the chapter's first line writes on Israel: 'and you shall eat and be satisfied and bless the LORD your God for the good land which he has given you' (8:10 — the Torah's ONE command to bless Him; 'eat and be satisfied' 6:11, 8:10, 8:12, 11:15, 14:29, 31:20; the sated verb the seven-stem homograph, starred by the parser at 8:10 and 8:12): THE CODE'S HOLE compiled here — no cell in any runner held the grace (the recon over all sixty-two: 'satisfied/grace' only the modules' strip helpers and Balak's seats); THE SHELF: the grace BY TORAH LAW (Berakhot 21a:3 Rav Yehuda; 20b:16 the mishna — the after by the Torah, the before by the Sages), THE FOUR BLESSINGS from the verse cut three ways (48b:5 the baraita — 'bless' the food's, 'the LORD your God' the zimmun (the invitation), 'for the land', 'good' Jerusalem's by 3:25, 'which he gave you' the good and beneficent; Tosefta Berakhot 6:1 the zimmun on 'bless'; 48b:6 Rabbi — the zimmun from Psalm 34:3, the fourth blessing Yavne's with no verse; 49a:5 the fourth's standing disputed), THE MEASURE OF 'SATISFIED' a PARAMETER with a Torah edge (20b:14 below satisfaction rabbinic; 49b:9, Pesachim 49b:17, Yoma 79b:9 — R. Meir 'eat' eating an olive-bulk and 'be satisfied' drinking, R. Yehuda eating that satisfies an egg-bulk; Mishnah Berakhot 7:2; Mishnah Sukkah 2:5 R. Tzadok's less than an egg-bulk), THE COMMAND'S FORM conditional on eating — 'not an obligation: if he wants he eats' (49b:4), not time-bound (20b:7 — Exodus 16:8's 'to the full'), its persons (women obligated, Torah or rabbinic OPEN 20b:11-14; the priests' atonement meal Arakhin 4a; consecrated food Bava Metzia 114a; the zimmun's persons Mishnah 7:1), its object BREAD ('a land' concluded the matter, 44a:10 — the seven species one blessing abridged from three, 44a:12; Rabban Gamliel's three rejected), the meal's end and the reciter (42a:5 the table removed; 42a:7 the three pairs — the last washing and the grace; 43a:11-12 the first to wash), the grace in any language (Sotah 33a); Onkelos 'and you shall bless' the same verb; written on the counter's day (40, 11, 1), no marker; MOSES INSTITUTED THE FIRST BLESSING WHEN THE MANNA FELL (48b:2 — the blessing before its verse, an install-order note)",
  HE_BLESS + " (and you shall eat and be satisfied and bless — Deut 8:10)",
  "Deut 8:10 (the one seat of the command); Deut 6:11, 8:12, 11:15, 14:29, 31:20 ('eat and be satisfied' — the other seats); Deut 8:8-9 (the seven species, 'a land' concluded the matter); Exodus 23:25 (the bread and water blessed — ordinances.land by CALL, the Sifrei 40:10's kin; 48b:7 read 'and YOU shall bless'); Onkelos 8:10; Mishnah Berakhot 6:1-7:5; Mishnah Sukkah 2:5; Tosefta Berakhot 6:1-2; Babylonian Talmud Berakhot 20b:1-21a:6, 35a:1-35b:23, 41a:1-44a:17, 48b:1-49b:18, Arakhin 4a:4, Bava Metzia 114a:9, Chullin 107a:12, Pesachim 49b:17, Sukkah 26b:9, Yoma 79b:9, Sotah 33a:10",
  f"deu_08_manna_humility (STEP_Dt_8_10; the claims {CL[0]} through {CL[-1]})",
  "cold_run_good_land.py (F3 the_good_land — eat_be_satisfied_bless; the exam kind good_land_case; the status written on the tape kind grace_commanded)"),
 ('forgetting_barred', 'block',
  "the forgetting barred — the BLOCK the chapter's second line writes on Israel: 'take heed to yourself lest you forget the LORD your God, so as not to keep his commandments and his judgments and his statutes which I command you this day' (8:11 — 'take heed to yourself lest' nine Bible seats, 6:12 and 8:11 the two with 'forget the LORD'; 'forget the LORD' 6:12, 8:11, 8:14, 8:19; 'forget' fourteen Deuteronomy seats, 8:19's infinitive absolute the lemma's one such form in the Bible): THE CODE'S HOLE compiled here — 6:12's cell (hear_o_israel.the_gift_and_the_warning('lest_you_forget')) held the ask WITHOUT A WRITE, the block never reached the tape: written here for the first time; THE SHELF: 'BEWARE, LEST, NOT' NOTHING BUT A PROHIBITION — R. Avin in R. Ile'a's name at three seats (Sotah 5a:3 the arrogant's warning from 8:11 with 8:14 — Rav Nachman bar Yitzchak; Makkot 13b:5 the lashes' scope from 28:58's 'if you will not observe', positive commands excluded; Eruvin 96a:8 the Paschal lamb's 'observe'), the rule's limit — 'observe' with a positive has a positive's force (Eruvin 96a:9), 8:11's 'take heed' attached to 'LEST you forget' a negative; A PROHIBITION WITHOUT AN ACTION IS NOT FLOGGED (Makkot 13b:6 'to perform') — the block carries no lashes; arrogance as denial of the core belief from 8:14 (Sotah 4b:11), as idolatry by 7:26 (4b:10), the scholar's eighth of an eighth (5a:16-17); 'filling his stomach' — Rav Nachman's source 8:14 (Berakhot 32a:12); the growth's list 6:10-11's gift made the growth (8:12-13; the king's law's tokens 17:17, 17:20 forward); Onkelos 'lest you forget THE FEAR of the LORD your God' (8:11, 8:14, 8:19 — the fear supplied at the three seats); written on the counter's day (40, 11, 1), no marker",
  HE_FORGET + " (take heed to yourself lest you forget — Deut 8:11)",
  "Deut 8:11 (the seat); Deut 6:12 (the first seat of 'lest you forget the LORD' — hear_o_israel by CALL, the cell with the ask and no write), 8:14, 8:19 (the chapter's forgetting thrice); Deut 4:9, 4:23 ('take heed to yourself lest you forget' — obey_horeb by CALL); Deut 12:13, 12:19, 12:30, 15:9 (the form forward); Deut 17:17, 17:20 (the king's law's tokens — owed forward); Onkelos 8:11, 8:14, 8:19; Babylonian Talmud Sotah 4b:8-5a:21, Makkot 13b:1-21, Eruvin 96a:8-9, Berakhot 32a:12, 43b:20",
  f"deu_08_manna_humility (STEP_Dt_8_11 through STEP_Dt_8_14; the claims {CL[0]} through {CL[-1]})",
  "cold_run_good_land.py (F4 take_heed_lest_you_forget — take_heed_lest; the exam kind good_land_case; the block written on the tape kind forgetting_warned)"),
]
added = 0
for name, op, en, he, ink, corpus, exam in NEW:
    if name in fx: continue
    text = text.rstrip('\n') + '\n' + f"  {name}:\n    en: {q(en)}\n    he: {q(he)}\n    ledger_op: {op}   # THE DEUTERONOMY WALK 6b (2026-09-19): chapter 8's compile — {name}\n    ink: {q(ink)}\n    corpus: {q(corpus)}\n    exam: {q(exam)}\n"
    added += 1
open(path, 'w', encoding='utf-8').write(text)
fx = yaml.safe_load(open(path, encoding='utf-8'))['effects']
assert all(n in fx for n, *_ in NEW) and fx['bless_after_eating_commanded']['ledger_op'] == 'status' and fx['forgetting_barred']['ledger_op'] == 'block'
print('effects: %d added (registry %d); the he found in the verses: %s | %s; the testimony REUSES heaven_and_earth_witness (%s)' % (added, len(fx), HE_BLESS, HE_FORGET, fx['heaven_and_earth_witness']['ledger_op']))
# ---- NO registry row (Israel the written-on party, standing; the manna, the rock and the serpent already rows, untouched) ----
reg = yaml.safe_load(open(f"{ROOT}/logic/corpus/entity_registry.yaml", encoding='utf-8'))
ids = {e['id'] for e in reg['entities']}
assert 'israel_people' in ids, 'the written-on party must stand'
print('entities: none added (registry %d); the-manna %s, the-rock %s, the-serpent %s (untouched — the readback references their lines)' % (len(reg['entities']), 'the-manna' in ids, 'the-rock' in ids, 'the-serpent' in ids))
# ---- the daemon block + the functions block (daemon_dispositions.yaml) ----
path = f"{ROOT}/World/step9/daemon_dispositions.yaml"
text = open(path, encoding='utf-8').read()
if '  law_good_land:' not in text:
    block = '''  law_good_land:
    file: cold_run_good_land.py
    wraps: good_land
    given_at: Deut 8:1
    installed_by: boot   # THE DEUTERONOMY WALK 6b (2026-09-19): THE GOOD LAND'S LAW GIVEN AT ITS OWN DAY — the chapter's own lines on the counter's day (40, 11, 1), no marker (the speech continuing from chapter 7's own-day lines); installed by boot like law_opening_speech, law_obey_horeb, law_hear_o_israel and law_seven_nations (the Deuteronomy daemons' form); the code's two holes compiled here (the grace after the meal, the forgetting barred) and the testimony's effect reused; THE READBACK'S FIFTH FORM — the retelling of a STATE: eighteen reference rows against the tape's lines and the kin's cells, the garment's row SUPPLIED with no retrograde write; no second write of the kin's effects
    watches:
      grace_commanded: [bless_after_eating_commanded]   # Deut 8:7-10: 'and you shall eat and be satisfied and bless the LORD your God' — the Torah's one command to bless Him: a STATUS on Israel (NEW — the code's hole; the grace by Torah law, Berakhot 21a; the measure of 'satisfied' a PARAMETER, 49b:9; the four blessings from the verse, 48b:5) on the counter's day
      forgetting_warned: [forgetting_barred]   # Deut 8:11-18: 'take heed to yourself lest you forget the LORD your God' — 6:12's clause, whose cell held the ask without a write: a BLOCK on Israel (NEW — its first tape write; 'beware, lest, not' nothing but a prohibition, Sotah 5a:3 / Makkot 13b:5 / Eruvin 96a:8; no action, no lashes, Makkot 13b:6); the chain of 8:14-18 the readback's reference rows, no second write
      perishing_testified: [heaven_and_earth_witness]   # Deut 8:19-20: 'I testify against you this day that you shall surely perish' — 4:26's testimony at its second seat: law_obey_horeb's effect REUSED (read at the design from the watches), heaven and earth the witnesses there, 'I' here; 'like the nations … so shall you perish' the measure for measure against nations_devoted
      good_land_case: [accepted, exempt, lashes]   # the exam's rows on the chapter — the persons through the cells' asks (the eater of an egg-bulk accepted, R. Tzadok with less than an egg-bulk exempt, the one who forgets without an act no lashes …)
'''
    i = text.index('  law_census:')
    text = text[:i] + block + text[i:]
if '\n  good_land:   # THE DEUTERONOMY WALK 6b' not in text:
    fb = '''  good_land:   # THE DEUTERONOMY WALK 6b (2026-09-19)
    the_frame: {status: WRAPPED, by: law_good_land}
    the_way_of_forty_years: {status: WRAPPED, by: law_good_land}
    the_good_land: {status: WRAPPED, by: law_good_land}
    take_heed_lest_you_forget: {status: WRAPPED, by: law_good_land}
    the_chain_and_the_covenant: {status: WRAPPED, by: law_good_land}
    the_testimony: {status: WRAPPED, by: law_good_land}
'''
    i = text.index('  seven_nations:   # THE DEUTERONOMY WALK 5b')
    j = text.index('\n  pre_sinai:', i)
    text = text[:j + 1] + fb + text[j + 1:]
open(path, 'w', encoding='utf-8').write(text)
dd = yaml.safe_load(open(path, encoding='utf-8'))
assert 'law_good_land' in dd['daemons'] and 'good_land' in dd['functions'], (list(dd)[:5])
print('daemons: %d (law_good_land %s); functions blocks: %d' % (len(dd['daemons']), 'law_good_land' in dd['daemons'], len(dd['functions'])))
# ---- the dependency span + the CALL edges by the ink (the token-demanded edges and the POINTERS after the gate's print) ----
path = f"{ROOT}/World/step9/dependency_dispositions.yaml"
text = open(path, encoding='utf-8').read()
if '\n  good_land:' not in text.split('\nedges:')[0]:
    a = "  seven_nations: [[Deut, 7, 1, 26]]"
    i = text.index(a); j = text.index('\n', i)
    text = text[:j + 1] + "  good_land: [[Deut, 8, 1, 20]]   # THE DEUTERONOMY WALK 6b (2026-09-19; DEUTERONOMY_WALK.md \"Sitting 6b\"): chapter 8 — THE GOOD LAND: the grace after the meal and the forgetting barred compiled for the first time (the code's holes), the testimony's effect reused; THE READBACK'S FIFTH FORM — the retelling of a STATE (the garment and the foot, 8:4 — SUPPLIED, no retrograde write): eighteen reference rows, no second write; three lines on the counter's day, no marker\n" + text[j + 1:]
    W = "THE DEUTERONOMY WALK 6b (2026-09-19) | "
    edges = f'''  - {{from: good_land, to: obey_horeb, disposition: CALL, link: reference, carries: verdict,
     why: "{W}8:1's 'that you may live and multiply and go in and possess the land' is 4:1's exhortation (OH.the_exhortation('hear_and_do') CALLED — the readback row 8:1 VERBATIM in kind); 8:11's 'take heed to yourself lest you forget' 4:9's clause (OH.horeb_retold('take_heed_lest_you_forget')); 8:19's 'I testify against you this day that you shall surely perish' 4:26's testimony (OH.the_exile_case('the_witnesses', 'perish_and_scatter') CALLED — the tape's witnesses_called found by kind and first verse; the effect heaven_and_earth_witness REUSED at 8:19, CU6); 8:1 and 8:18's 'swore to your fathers' 4:31's covenant of the fathers"}}
  - {{from: good_land, to: exodus_story, disposition: CALL, link: reference, carries: verdict,
     why: "{W}8:3 and 8:16's manna is the tape's manna_fell (Exod 16:13-15; 16:4's test clause 'whether they will walk in my law or not' — 8:2's 'whether you would keep his commandments or not' the same two closing tokens: ES.manna('forty_years', 'day_by_day') CALLED — the readback rows 8:2 VERBATIM in kind, 8:3 TURNED, 8:16 EXPANDED); 8:15's rock of flint the tape's rock_struck (17:6 — Exodus' tzur, the flint's; ES's Rephidim); 8:14's 'who brought you out of the land of Egypt' the tape's brought_out (12:51 — VERBATIM in kind); 8:2's 'to test you' the trials' direction reversed (ES.trials('ten_list', 'count_by_exodus') — Israel tested there, God testing here); 8:15's 'thirsty ground where there was no water' 17:1's; manna_provided and water_from_the_rock UNMOVED (CU5)"}}
  - {{from: good_land, to: shelach, disposition: CALL, link: reference, carries: verdict,
     why: "{W}8:2 and 8:4's 'these forty years' [40] are the decree's years (Num 14:26-35 — decree_declared with years 40, day_for_year [40, 40]: SL.decree('day_for_year') CALLED — the readback row 8:2 EXPANDED, the purpose supplied: the humbling, the test, the heart); the tape's line found by kind and first verse (CU4)"}}
  - {{from: good_land, to: beha, disposition: CALL, link: reference, carries: verdict,
     why: "{W}8:3's 'the manna which you did not know, nor did your fathers know' and 8:16's — the craving's manna described (Num 11:7-9 like coriander seed, its taste, the dew: BH.taberah_and_quail('manna_form', 'manna_taste', 'dew') CALLED); the exam's Yoma 74b-76a rows (the tastes and forms, the five foods, the sixty cubits) the Numbers 11 exam's credited rows; lust_and_weeping and quail_and_plague on the tape untouched"}}
  - {{from: good_land, to: chukat, disposition: CALL, link: reference, carries: verdict,
     why: "{W}8:15's 'fiery serpents and scorpions' is the tape's fiery_serpents_sent (Num 21:6 — 'fiery serpent' 8:15 and 21:6, 8 alone: CK.arad_and_the_serpent('bite_and_burn', 'singular_serpent') CALLED — the readback row 8:15 EXPANDED, the scorpions and the thirst named, no line for either; 21:5's 'no water' the thirst's seat); 8:15's rock the second seat's kin (Num 20:10-11 rock_struck_twice — Numbers' sela against Exodus' tzur: CK.meribah('meribah_seats') CALLED — the DATA row the_two_rocks); serpents_sent UNMOVED (CU5)"}}
  - {{from: good_land, to: hear_o_israel, disposition: CALL, link: reference, carries: verdict,
     why: "{W}8:11's 'take heed to yourself lest you forget the LORD your God' is 6:12's clause — six tokens shared (HI.the_gift_and_the_warning('lest_you_forget') CALLED: the cell holds the ask WITHOUT A WRITE — THE CODE'S HOLE, forgetting_barred written here for the first time, CU3; the readback row 8:11 VERBATIM); 8:12-13's growth 6:10-11's gift made the growth (HI.the_gift_and_the_warning('the_list') — the readback row VARIANT); 8:7-9's good land 6:3's 'flowing with milk and honey' (HI.the_header('the_land_flowing') — honey without milk, EXPANDED); 8:11's triad 'his commandments, his judgments and his statutes' 6:1's order turned (HI.the_header('the_triad')); shema_commanded and test_barred UNMOVED (CU5)"}}
  - {{from: good_land, to: opening_speech, disposition: CALL, link: reference, carries: verdict,
     why: "{W}8:9's 'you shall not lack anything in it' is 2:7's receipt 'these forty years the LORD your God has been with you; you have lacked nothing' (OS.the_bypass('forty_years_lacking_nothing') CALLED — the readback row 8:9 VERBATIM in kind; 'these forty years' 2:7, 8:2, 8:4 the three seats); 8:5's 'as a man disciplines his son' 1:31's 'as a man carries his son' (OS.the_spies_read_back('the_carrying') CALLED — the readback row 8:5 VARIANT, carried made disciplined; Berakhot 5a's afflictions of love the exam's rows); 8:15's 'the great and terrible wilderness' 1:19's phrase (OS.the_commission — the two seats)"}}
  - {{from: good_land, to: covenant_at_horeb, disposition: CALL, link: reference, carries: verdict,
     why: "{W}8:19's 'go after other gods and serve them and bow down to them' is the second word's clause with the order reversed (CH.the_second_word('no_other_gods', 'bow_and_serve') CALLED — the readback row 8:19 VARIANT; the census's ten seats, serve-then-bow four; other_gods_barred UNMOVED, CU5); 8:14's 'who brought you out of the land of Egypt, out of the house of bondage' the formula's seat 5:6 (CH.the_second_word('the_header') — the readback row 8:14 VERBATIM in kind with the tape's brought_out)"}}
  - {{from: good_land, to: seven_nations, disposition: CALL, link: reference, carries: verdict,
     why: "{W}8:1 and 8:18's 'the oath which he swore to your fathers' — 7:8's form on the oath's three tape lines (SN.the_holy_people('the_oath') CALLED — the readback row 8:18 VERBATIM in kind); 8:20's 'because' the heel's second seat (7:12 the first — SN.because_you_hear('the_heel') CALLED; 'because you would not hearken' the one plural of 'the LORD your God' in the chapter); 8:20's 'like the nations which the LORD makes to perish before you' the ban's nations (SN.the_seven_nations('the_ban') — the readback row 8:20 TURNED, the measure for measure; the tape's nations_devoted found by kind and first verse); 8:11's triad the fourth seat after 5:31, 6:1, 7:11 (SN.the_faithful_god('the_triad')); blessings_for_hearing and treasured_people UNMOVED (CU5)"}}
  - {{from: good_land, to: ordinances, disposition: CALL, link: reference, carries: verdict,
     why: "{W}8:10's 'and you shall eat and be satisfied and bless' beside 23:25's 'he shall bless your bread and your water' (OR.land('bread_water') CALLED — the Sifrei 40:10's kin; R. Yitzchak's 'read: and YOU shall bless', Berakhot 48b:7 — the before-blessing's derivation, set aside); bread_and_water_blessed in the registry and ABSENT from the world (the case kind entered_the_land is Joshua's) — the design's measurement, no write here"}}
  - {{from: good_land, to: sanctions, disposition: CALL, link: reference, carries: verdict,
     why: "{W}8:1's 'that you may live' and 8:3's 'man lives by everything that proceeds from the mouth of the LORD' beside Leviticus 18:5's 'which if a man does he shall live by them' (the sanctions runner's rows on the living — CALLED for the living clause's verdict); 'man shall live' 8:3 and Ecclesiastes 11:8; the Sifrei 48:10's 'not by bread alone' the exposition's teaching, a DATA row (not_by_bread_alone), no write"}}
  - {{from: good_land, to: mamre, disposition: CALL, link: reference, carries: verdict,
     why: "{W}8:1 and 8:18's oath — the tape's sworn_by_himself (Gen 22:16-18; MA.moriah('test_verb_seats') CALLED — 8:2 and 8:16's 'to test you' the Akedah's verb, the lemma's fifteen Torah seats) and oath_upheld (26:3-5; MA.isaac_gerar('famine_ordinal')); the readback row 8:18 found by kind and first verse (CU4); Genesis 22:18 and 26:5's 'because' the heel's Genesis seats"}}
  - {{from: good_land, to: joseph, disposition: CALL, link: reference, carries: verdict,
     why: "{W}the oath's third line — visitation_promised at Genesis 50:24 'the land which he swore to Abraham, to Isaac and to Jacob' (JS.the_oath('kindness_and_truth') CALLED — the readback row 8:18 VERBATIM in kind names the three lines)"}}
  - {{from: sequence, to: good_land, disposition: CALL, link: none,
     why: "{W}the sequential run's REGISTRATION edge — ('cold_run_good_land', 'law_good_land') in DAEMON_ORDER (the runner compiles no verse: link none, O4's license); the three tape lines this sitting's on the counter's day, NO marker; the daemon's status, block and reused entry written on its own lines"}}
'''
    a = "  - {from: seven_nations, to: sanctions, disposition: FALSE, link: none,"
    i = text.index(a); j = text.index('\n', text.index('why:', i)) + 1
    text = text[:j] + edges + text[j:]
    open(path, 'w', encoding='utf-8').write(text)
dep = yaml.safe_load(open(path, encoding='utf-8'))
n_ch = sum(1 for e in dep['edges'] if e['from'] == 'good_land')
assert 'good_land' in dep['spans'] and n_ch == 13, n_ch   # the design's decalogue edge DROPPED at the callees' print: cold_run_decalogue holds no cell on the second word (its cells altar_rules, sabbath_clauses, theft_commandment, vain_name) — the first copy's clause rides covenant_at_horeb's cell; the census decides
print('dependency: span + 14 edges (good_land 13 CALL and the registration; the decalogue edge dropped — no cell there); the token-demanded edges and the pointers after the gate\'s print')
# ---- the installation probe's count ----
path = f"{ROOT}/World/step9/installation_probes.py"
text = open(path, encoding='utf-8').read()
if "len(real) == 67 and all(" in text:
    old = "len(real) == 67 and all('given_at' in d and 'installed_by' in d for d in real.values())   # THE DEUTERONOMY WALK 5b (2026-09-18): 66 -> 67,"
    assert text.count(old) == 1, text.count(old)
    text = text.replace(old, "len(real) == 68 and all('given_at' in d and 'installed_by' in d for d in real.values())   # THE DEUTERONOMY WALK 6b (2026-09-19): 67 -> 68, law_good_land (given_at Deut 8:1 — the chapter's frame; installed_by boot); 5b: 66 -> 67,")
    open(path, 'w', encoding='utf-8').write(text)
assert "len(real) == 68" in open(path, encoding='utf-8').read()
print('installation_probes I5: 68')
