import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE DEUTERONOMY WALK sitting 7b — THE COMPILE OF CHAPTER 9 (2026-09-19; World/step9/DEUTERONOMY_WALK.md "Sitting 7b"): THE TYPES FIRST — ONE tape
# kind (prayed_for_aaron — an ACT told only in the retelling, 9:20, written ONCE at its own day by the retrograde marker at Deut 9:20: the second forty's
# day (1, 4, 18), Exod 32:30's morrow), ONE case kind (not_righteousness_case), ONE new effect (destruction_halved — a STATUS on aaron; THE NAME FROM THE
# DOCKET: Vayikra Rabbah 10:5 'half the edict was withheld — two died and two remained', superseding the design's destruction_averted), NO registry row
# (aaron the written-on party, 28 entries standing), the 69th daemon's block (law_not_righteousness, given_at Deut 9:1 — the chapter's frame; installed_by
# boot — the Deuteronomy daemons' form), the functions block (six cells WRAPPED), the dependency span and the ELEVEN CALL edges the design predicts (the
# census decides — 4b's, 5b's and 6b's lesson) with the registration edge, the installation probe's count 68 -> 69. The `he` is cut from the pointed DB
# text by FINDING the phrase's tokens (never a typed index); the claim ids and the step ids READ from the frozen unit; the reading ledger's source count
# COMPUTED. Idempotent (add_types_ch8.py's form, derived by hand where it differs).
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
unit = open(f'{ROOT}/logic/units/deu_09_not_righteousness.yaml', encoding='utf-8').read()
CL = sorted(set(re.findall(r'DV09-\d+', unit))); ST = sorted({int(x) for x in re.findall(r'STEP_Dt_9_(\d+)', unit)})
assert len(CL) == 6 and ST[0] == 1 and ST[-1] == 29, (CL, ST[:3], ST[-1])
led = open(f'{ROOT}/logic/oral_triage/deu_09_ekev_2026-09-19.md', encoding='utf-8').read()
N_SRC = len(re.findall(r'^- (?:Onkelos|Sifrei) ', led, re.M)); assert N_SRC > 0, N_SRC
CORPUS = f"deu_09_not_righteousness (STEP_Dt_9_1 through STEP_Dt_9_29; claims {CL[0]} through {CL[-1]})"
SUB = "submitted by cold_run_not_righteousness.py [subjects: %s] (the narrative scene, THE DEUTERONOMY WALK 7b); re-submitted on the sequential tape by cold_run_sequence.py; consumed by law_not_righteousness (cold_run_not_righteousness.py) -> %s"
CASE = "submitted by cold_run_not_righteousness.py [subjects: the exam's persons] (the wrap's scene); consumed by law_not_righteousness (cold_run_not_righteousness.py) -> %s"
INK = "Deut 9:1-29; Onkelos Deut 9:1-29 (the export's division the DB's — the identity; the Memra (the Word) a consuming fire at 9:3, MERIT for righteousness at 9:4-6, the anger 'from before' at 9:8 and 9:20, 'leave your prayer from before Me' supplied at 9:14, 'accepted my prayer' at 9:19, the three names TRANSLATED at 9:22, 'the inhabitants of the land' at 9:28); the Sifrei on Deuteronomy SILENT on the chapter (its seven rows from elsewhere read whole — 14:1, 25:4, 26:7, 27:2, 306:25, 342:1, 357:44); the kin by CREDIT — the calf Exodus 32-34, the ascent 24:18, the ten trials, Taberah and the quail Numbers 11, the spies 13-14; the reading ledger deu_09_ekev_2026-09-19.md (%d sources, 6 claims); the exam docket deu_09_ekev_exam_2026-09-19.md (397 rows READ WHOLE FROM THE START: LAW 46 / DERIVATION 48 / DISPUTE 10 / CONTEXT 160 / OUTSIDE 133)" % N_SRC
D, X, N_, L_ = 'Deut', 'Exod', 'Num', 'Lev'
KINDS = [
 ("prayed_for_aaron", "act",   # an ACT told only in the retelling — the register test's wayyiqtol at 9:20 ('and I prayed'); written ONCE at its own day by a RETROGRADE marker
  "Moses prayed for Aaron — 'AND WITH AARON THE LORD WAS VERY ANGRY, TO DESTROY HIM; AND I PRAYED FOR AARON ALSO AT THAT TIME' (Deut 9:20) — AARON'S PERIL, TOLD ONLY HERE: Exodus 32 has Aaron's report (32:21-24, read and not translated — Mishnah Megillah 4:10) and the plague 'because they made the calf which Aaron made' (32:35), but NO anger at Aaron and NO prayer for him — THE TAPE'S HOLE, filled by the retelling (THE READBACK'S SIXTH FORM, the T2 row); the act WRITTEN ONCE at its own day by the RETROGRADE marker at Deut 9:20 (M['aaron_told'] = M['morrow'] — 'at that time' the second forty's ascent, Exod 32:30's morrow of the breaking, (1, 4, 18); reading_placed; Sanhedrin 102a:5 reads 'at that time' as a time ordained for calamity), the stretch ENDED by a forward marker at 9:21; THE WRITE destruction_halved — a STATUS on aaron (Vayikra Rabbah 10:5: 'to destroy him' is the eradication of children (Amos 2:9); since Moses prayed HALF THE EDICT WAS WITHHELD — two died (Nadab and Abihu, Leviticus 10) and two remained (Eleazar and Ithamar — 'take Aaron and his sons with him', Leviticus 8:2); R. Yehoshua ben Levi: prayer accomplishes half); 'was very angry' the hithpael's book-four seats (1:37, 4:21, 9:8, 9:20 — Moses' twice, this chapter's twice); 'to destroy him' the one seat; the intercession's forty the marker's stretch (9:18, 9:25); Onkelos 'anger from before the LORD' and 'I prayed' — the retelling of Aaron's peril TRANSLATED where Aaron's report is not (the asymmetry, a DATA row)",
  HE(D, 9, 20, 20, "and with Aaron the LORD was very angry, to destroy him; and I prayed for Aaron also at that time"), WIT(D, 9, 20, 20) + WIT(X, 32, 21, 21) + WIT(X, 32, 35, 35) + WIT(L_, 8, 2, 2) + WIT(L_, 10, 1, 2), INK, CORPUS,
  SUB % ("moses (for aaron)", "destruction_halved on aaron (a STATUS, dated (1, 4, 18) by the retrograde marker at Deut 9:20 — the morrow of the breaking, the second forty's ascent)"), ["for", "anger", "first_telling", "dated"]),
 ("not_righteousness_case", "case", "the exam's rows on chapter 9 (Deut 9:1-29 — the hyperbole rule on 9:1: Chullin 90b:12, Tamid 29a:8; the stiff neck as the reason for the Torah: Beitzah 25b:7-8; the calf's destruction and the fourth verb: Mishnah Avodah Zarah 3:3, Avodah Zarah 43b-44a, Tosefta Avodah Zarah 4:3, 52a:4; the breaking approved at three seats: Shabbat 87a:2-5, Menachot 99b:1, Bava Batra 14b:7; the fragments in the ark: Menachot 99a:12, Bava Batra 14b:4-6; the breaking's date: Mishnah Ta'anit 4:6, Ta'anit 28b:8-10; the ascent's date's two arms: Shabbat 88a:3; the forty days as the measure of prayer: Berakhot 32b:8-9, 34a:11; the fasting's seat: Yoma 75b:11; sitting and standing: Megillah 21a:17; the intercession's rules: Berakhot 32a:14-31, 7a:5, 7a:34-36, Shabbat 55a:5; the merit of the fathers: Shabbat 55a:11-16; Aaron's peril: Vayikra Rabbah 10:5, Mishnah Megillah 4:10, Sanhedrin 102a:5; the ten trials: Avot 5:4, Arakhin 15a:6-20; the calf's day, cause and debt: Shabbat 89a:6, Berakhot 32a:8-13, Sanhedrin 102a:15-16, Berakhot 32b:15-19, Shabbat 88a:7; the confession specified: Yoma 86b:14; the ten names of prayer: Devarim Rabbah 2:1) — the exam's persons through the cells' asks: the reader of 'fortified to the heavens', the impudent people, the grinder of the idol, the one who made the calf drink, the breaker of the tablets, the prolonger of prayer, the long-winded prayer leader, the one who eats on high, the one who sat on the mount, the seizer, the annuller of the vow, the one who counts the merit of the fathers, the one who prays half, the counter of the ten trials, the confessor who specifies",
  PHRASE(D, 9, 5, ['לא', 'בצדקתך']) + " (not for your righteousness — Deut 9:5)", WIT(D, 9, 1, 29), INK, CORPUS, CASE % "accepted / exempt (the exam's persons — the rule holds against him; outside the rule)", ["person", "ask"]),
]
assert len(KINDS) == 2, len(KINDS)
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
print('kinds: %d added of %d, registry %d; the ledger sources %d' % (len(out), len(KINDS), len(after['events']), N_SRC))
# ---- ONE new effect, the shelf's own words for its name, the `he` FOUND in the verse; the kin's effects asserted present (referenced, never rewritten) ----
path = f"{ROOT}/World/step9/effect_vocabulary.yaml"
text = open(path, encoding='utf-8').read()
fx = yaml.safe_load(text)['effects']
for e in ('accepted', 'exempt', 'atoned_forgiven', 'decree_relented', 'blotted_from_the_book', 'tablets_delivered', 'fire_sank', 'garments_transferred', 'covenant_declared', 'test_barred'):
    assert e in fx, e
assert 'destruction_averted' not in fx, "the design's provisional name must not be on file — the docket named the effect"
HE_HALVED = PHRASE(D, 9, 20, ['התאנף', 'יהוה', 'מאד', 'להשמידו'])
NEW = [
 ('destruction_halved', 'status',
  "the destruction halved — the STATUS the retrograde line prayed_for_aaron writes on aaron: 'and with Aaron the LORD was very angry, TO DESTROY HIM; and I prayed for Aaron also at that time' (9:20 — Aaron's peril TOLD ONLY HERE; 'to destroy him' the one seat; 'was very angry' 1:37, 4:21, 9:8, 9:20): THE NAME FROM THE SHELF — Vayikra Rabbah 10:5 (read whole at the docket): R. Yehoshua of Sikhnin in R. Levi's name — DESTRUCTION IS NOTHING OTHER THAN THE ERADICATION OF CHILDREN ('I destroyed his fruit from above and his roots from below', Amos 2:9); since Moses prayed, HALF THE EDICT WAS WITHHELD — TWO DIED AND TWO REMAINED ('take Aaron and his sons with him', Leviticus 8:2); R. Yehoshua ben Levi: repentance accomplishes all and PRAYER HALF — from Aaron (R. Yehuda's arm the reverse: prayer all, repentance half — Cain's 'in the land of Nod'); THE TWO HALVES ALREADY ON THE TAPE — Nadab and Abihu's fire (Leviticus 10:1-2, shemini_day's line) and the succession's garments_transferred on aaron at Hor (Numbers 20:26-28); the status dated (1, 4, 18) with its line — the second forty's ascent, Exod 32:30's morrow; 'at that time' a time ordained for calamity (Sanhedrin 102a:5 — Exodus 32:34's 'day of visiting' among R. Yosei's seats); Mishnah Megillah 4:10's ASYMMETRY — Aaron's report (Exodus 32:21-24) read and NOT translated, the retelling of his peril TRANSLATED (Onkelos 9:20 'anger from before the LORD … and I prayed'); aaron's atoned_forgiven entry (the milluim's re-acceptance, Leviticus 9:7's 'approach' by CALL) STANDS beside the new status, no second write; the design's provisional name destruction_averted SUPERSEDED by the docket's row before the types were typed",
  HE_HALVED + " (the LORD was very angry, to destroy him — Deut 9:20)",
  "Deut 9:20 (the one seat — Aaron's peril told only here); Deut 1:37, 4:21, 9:8 ('was very angry' — the hithpael's other book seats); Exodus 32:21-24 (Aaron's report — no anger, no prayer: the tape's hole), 32:35 (the plague 'which Aaron made'); Leviticus 8:2 ('take Aaron and his sons with him' — the milluim's row, lev_08_milluim_2026-09-03.md), 9:7 (the re-acceptance — shemini_day.day('aaron_chatat_run') by CALL), 10:1-2 (the two who died); Numbers 20:26-28 (the two who remained — garments_transferred on aaron); Amos 2:9 (the destruction's definition — the run outside the Torah); Onkelos 9:20; Vayikra Rabbah 10:5; Mishnah Megillah 4:10; Babylonian Talmud Sanhedrin 102a:5, Megillah 25b (the reading law's seat)",
  f"deu_09_not_righteousness (STEP_Dt_9_20; the claims {CL[0]} through {CL[-1]})",
  "cold_run_not_righteousness.py (F4 aarons_peril — the_peril, half_the_edict; the exam kind not_righteousness_case; the status written on the tape kind prayed_for_aaron under the retrograde marker at Deut 9:20)"),
]
added = 0
for name, op, en, he, ink, corpus, exam in NEW:
    if name in fx: continue
    text = text.rstrip('\n') + '\n' + f"  {name}:\n    en: {q(en)}\n    he: {q(he)}\n    ledger_op: {op}   # THE DEUTERONOMY WALK 7b (2026-09-19): chapter 9's compile — {name}, the name from the docket's row Vayikra Rabbah 10:5\n    ink: {q(ink)}\n    corpus: {q(corpus)}\n    exam: {q(exam)}\n"
    added += 1
open(path, 'w', encoding='utf-8').write(text)
fx = yaml.safe_load(open(path, encoding='utf-8'))['effects']
assert all(n in fx for n, *_ in NEW) and fx['destruction_halved']['ledger_op'] == 'status'
print('effects: %d added (registry %d); the he found in the verse: %s' % (added, len(fx), HE_HALVED))
# ---- NO registry row (aaron the written-on party, standing with his 28 entries; the-calf and the-tablets tape subjects without a row, as at the erection) ----
reg = yaml.safe_load(open(f"{ROOT}/logic/corpus/entity_registry.yaml", encoding='utf-8'))
ids = {e['id'] for e in reg['entities']}
assert 'aaron' in ids and 'moses' in ids and 'israel_people' in ids, 'the written-on party must stand'
print('entities: none added (registry %d); aaron %s, the-calf %s, the-tablets %s (tape subjects without a row — the erection\'s form)' % (len(reg['entities']), 'aaron' in ids, 'the-calf' in ids, 'the-tablets' in ids))
# ---- the daemon block + the functions block (daemon_dispositions.yaml) ----
path = f"{ROOT}/World/step9/daemon_dispositions.yaml"
text = open(path, encoding='utf-8').read()
if '  law_not_righteousness:' not in text:
    block = '''  law_not_righteousness:
    file: cold_run_not_righteousness.py
    wraps: not_righteousness
    given_at: Deut 9:1
    installed_by: boot   # THE DEUTERONOMY WALK 7b (2026-09-19): "NOT FOR YOUR RIGHTEOUSNESS" — the chapter's frame given at the counter's day (40, 11, 1); installed by boot like law_opening_speech, law_obey_horeb, law_hear_o_israel, law_seven_nations and law_good_land (the Deuteronomy daemons' form); THE READBACK'S SIXTH FORM — the retelling of a STRETCH: Moses telling the calf in his own voice, thirty-odd reference rows against the tape's Exodus 24-34 and Numbers 11-14 lines and the kin's cells, the three forties graded against THE CLOCK's own arithmetic (the markers' days — Ta'anit 28b:9's 24 + 16 reproduced), and ONE hole filled with a write: Aaron's peril (9:20), an act told only here, written ONCE at its own day by the RETROGRADE marker at Deut 9:20 (the morrow of the breaking, (1, 4, 18)) and ended by a forward marker at 9:21; no second write of the kin's effects (decree_relented, blotted_from_the_book, tablets_delivered, fire_sank, atoned_forgiven stand)
    watches:
      prayed_for_aaron: [destruction_halved]   # Deut 9:20: 'and with Aaron the LORD was very angry, to destroy him; and I prayed for Aaron also at that time' — a STATUS on aaron (NEW — the tape's hole; THE NAME FROM THE DOCKET: half the edict withheld, two died and two remained, Vayikra Rabbah 10:5), dated (1, 4, 18) by the retrograde marker
      not_righteousness_case: [accepted, exempt]   # the exam's rows on the chapter — the persons through the cells' asks (the grinder of the idol accepted, the one who counts the merit of the fathers exempt on Shmuel's arm …); no lashes person — the chapter holds no prohibition
'''
    i = text.index('  law_census:')
    text = text[:i] + block + text[i:]
if '\n  not_righteousness:   # THE DEUTERONOMY WALK 7b' not in text:
    fb = '''  not_righteousness:   # THE DEUTERONOMY WALK 7b (2026-09-19)
    the_frame: {status: WRAPPED, by: law_not_righteousness}
    the_calf_retold: {status: WRAPPED, by: law_not_righteousness}
    the_forty_days: {status: WRAPPED, by: law_not_righteousness}
    aarons_peril: {status: WRAPPED, by: law_not_righteousness}
    the_four_provocations: {status: WRAPPED, by: law_not_righteousness}
    the_intercession: {status: WRAPPED, by: law_not_righteousness}
'''
    i = text.index('  good_land:   # THE DEUTERONOMY WALK 6b')
    j = text.index('\n  pre_sinai:', i)
    text = text[:j + 1] + fb + text[j + 1:]
open(path, 'w', encoding='utf-8').write(text)
dd = yaml.safe_load(open(path, encoding='utf-8'))
assert 'law_not_righteousness' in dd['daemons'] and 'not_righteousness' in dd['functions'], (list(dd)[:5])
print('daemons: %d (law_not_righteousness %s); functions blocks: %d' % (len(dd['daemons']), 'law_not_righteousness' in dd['daemons'], len(dd['functions'])))
# ---- the dependency span + the CALL edges by the ink (the token-demanded edges and the POINTERS after the gate's print) ----
path = f"{ROOT}/World/step9/dependency_dispositions.yaml"
text = open(path, encoding='utf-8').read()
if '\n  not_righteousness:' not in text.split('\nedges:')[0]:
    a = "  good_land: [[Deut, 8, 1, 20]]"
    i = text.index(a); j = text.index('\n', i)
    text = text[:j + 1] + "  not_righteousness: [[Deut, 9, 1, 29]]   # THE DEUTERONOMY WALK 7b (2026-09-19; DEUTERONOMY_WALK.md \"Sitting 7b\"): chapter 9 — NOT FOR YOUR RIGHTEOUSNESS: the calf retold in Moses' own voice; THE READBACK'S SIXTH FORM — the retelling of a STRETCH (the three forties graded against the clock's own arithmetic); Aaron's peril (9:20) an act told only here, written ONCE at its own day by the retrograde marker at Deut 9:20 with the write destruction_halved on aaron; ONE line, TWO markers, no second write of the kin's effects\n" + text[j + 1:]
    W = "THE DEUTERONOMY WALK 7b (2026-09-19) | "
    edges = f'''  - {{from: not_righteousness, to: erection, disposition: CALL, link: reference, carries: verdict,
     why: "{W}the calf retold (9:8-21) is the erection runner's Exodus 24-34 stretch on the tape — moses_ascended 'first' (24:18), calf_made (32:4), moses_interceded 'relent' (32:11-14) and 'blot_me' (32:31-33), tablets_broken (32:19), calf_destroyed (32:20), moses_ascended 'second' (34:2-4): the readback rows found by kind and first verse; the kin's cells CALLED — ER.ascent('seventeenth_tammuz', 'sheet_taanit_4_6') the clock's compile rules (Ta'anit 28b:9, Mishnah Ta'anit 4:6 — the readback's stretch rows 9:9, 9:11 graded MATCH), ER.calf('saru_stiff') the stiff neck's six seats (9:6, 9:13 — no write, the state in the first telling), ER.calf('seized', 'three_legged', 'vayechal', 'vow_annulled', 'oath_endures') the intercession's rules (9:14, 9:26-27), ER.calf('four_verbs', 'fourth_verb_decides', 'nullification_dispute') the calf's destruction (9:21 — THE FOURTH VERB DROPPED by the retelling, the dispute's hinge), ER.calf('surcharge', 'boshesh', 'confess_specify', 'reading_law') the calf's debt, its own day (the OPEN row), the confession specified (9:18, 9:21), Aaron's report untranslated (the asymmetry with 9:20); ER.tablets('breaking_ratified', 'fragments_by_call') the breaking approved at three seats (9:17) and the fragments owed to chapter 10"}}
  - {{from: not_righteousness, to: exodus_story, disposition: CALL, link: reference, carries: verdict,
     why: "{W}9:7 and 9:24's 'from the day you came out of Egypt until you came to this place you have been rebellious' is the TEN TRIALS' span (ES.trials('ten_list', 'count_by_exodus') CALLED — Avot 5:4 and Arakhin 15a:14 the answer sheet: Massah the second water, Kibroth the second quail, the calf at Horeb, Kadesh = Paran among the ten; TABERAH (9:22) NOT among them — a DATA row the design did not predict); 9:22's Massah the tape's named line at Exod 17:7 (rock_struck 17:6 beside it); Shabbat 88a:3's two arms of the giving's day (ES.sinai) the ascent's date's parameter"}}
  - {{from: not_righteousness, to: beha, disposition: CALL, link: reference, carries: verdict,
     why: "{W}9:22's Taberah and Kibroth-hattaavah are the tape's fire_of_the_lord_burned (Num 11:1-3 — fire_sank a STATUS on Israel UNMOVED) and quail_and_plague (11:31-35 — the graves) found by kind and first verse; BH.taberah_and_quail('fire_at_edge', 'fire_sank', 'graves') CALLED; the marker at Num 11:1 (Ta'anit 29a:3 — the three days) the day the line carries; Berakhot 32a:5's al-tikrei ('do not read') on Taberah's prayer a DATA note"}}
  - {{from: not_righteousness, to: shelach, disposition: CALL, link: reference, carries: verdict,
     why: "{W}9:23's Kadesh-barnea — 'you rebelled … you did not believe Him nor hearken' — is the rejection's block on the tape (congregation_wept Num 14:1-4 found by kind and first verse; decree_declared 14:26-35 the sentence UNMOVED); 9:2's 'a people great and tall, the sons of the Anakim' the spies' giants (SL.spies('giants') CALLED); 9:28's taunt 'because the LORD was not able' is Numbers 14:16's feminine noun kept (SL.decree('ability', 'egypt_will_hear') CALLED — the tape's moses_pleaded_on_the_attributes 14:13-19 the intercession's second telling; THE TAUNT'S FOUR FORMS a DATA row: Exodus 32:12, Numbers 14:16, Deuteronomy 1:27, 9:28); the marker at Num 13:25 (Ta'anit 29a:5) the Ninth of Av"}}
  - {{from: not_righteousness, to: opening_speech, disposition: CALL, link: reference, carries: verdict,
     why: "{W}9:1's 'cities great and fortified to the heavens' is 1:28's phrase with the spelling changed (the readback row VARIANT — the hyperbole rule, Chullin 90b:12, the Sifrei 25:4); 9:2's Anakim 1:28's; 9:23's 'you rebelled against the commandment of the LORD' 1:26's clause (five tokens shared) — OS.the_spies_read_back('the_murmuring', 'the_presumption') CALLED; 9:28's 'because He hated them' 1:27's 'in His hatred' (the taunt's third form); the kin's readback (the first form) the row these rows reference twice"}}
  - {{from: not_righteousness, to: obey_horeb, disposition: CALL, link: reference, carries: verdict,
     why: "{W}9:1's 'nations greater and mightier than you' is 4:38's clause (OH.the_one_god('to_dispossess_nations') CALLED — the readback row VERBATIM in kind); 9:3's 'a consuming fire' 4:24's (OH.no_image('consuming_fire_jealous_god') CALLED); 9:10's tablets 4:13's retrograde line tablets_given on the tape (OH.horeb_retold('the_ten_words_and_the_tablets') CALLED — the line found by kind and first verse Deut 4:13, first_telling Exodus 31:18; dated at the breaking (1, 4, 17) — the same day the stretch row 9:11 ends); 9:26 and 9:29's 'Your great power' 4:37's (OH.the_one_god CALLED); 9:19's 'the LORD hearkened' the merciful God of 4:31 (OH.the_exile_case('the_merciful_god'))"}}
  - {{from: not_righteousness, to: covenant_at_horeb, disposition: CALL, link: reference, carries: verdict,
     why: "{W}9:10's 'the LORD gave me the two tablets of stone written with the finger of God, and on them all the words which the LORD spoke with you in the mountain out of the midst of the fire on the day of the assembly' is 5:22's 'and he wrote them on two tablets of stone and gave them to me' (CH.the_voice_and_the_request('the_tablets_given_to_me') CALLED — the readback row VERBATIM in kind with the tape's tablets_given); Shabbat 88b:8-89a:1's answer to the angels FROM THE TEN WORDS (CH.the_first_tablet / the_second_tablet — the tablets' content, a DATA note on 9:10's 'according to all the words')"}}
  - {{from: not_righteousness, to: hear_o_israel, disposition: CALL, link: reference, carries: verdict,
     why: "{W}9:22's Massah is 6:16's 'as you tested at Massah' (HI.the_test_and_the_right('you_shall_not_test') CALLED — the tape's named line at Exod 17:7 the seat both reference; test_barred on Israel UNMOVED); the readback row 9:22 VERBATIM in kind (the three names, three lines, out of the tape's order)"}}
  - {{from: not_righteousness, to: seven_nations, disposition: CALL, link: reference, carries: verdict,
     why: "{W}9:1's 'nations greater and mightier than you' is 7:1's 'seven nations greater and mightier than you' said again without the count (SN.the_seven_nations('the_seven') CALLED — the seven's list the census's, the readback row 9:1 VERBATIM in kind with 4:38 and 7:1); 9:4-5's 'the wickedness of these nations' the ban's reason (7:1-5's nations_devoted UNMOVED, the debit OPEN to Joshua)"}}
  - {{from: not_righteousness, to: shemini_day, disposition: CALL, link: reference, carries: verdict,
     why: "{W}9:20's Aaron's peril reaches the tape's eighth day — Leviticus 9:2's 'take a calf for a sin offering' the calf for the calf, 9:7's 'approach the altar' the public re-acceptance after the calf (SD.day('aaron_chatat_run') CALLED — the milluim and investiture ledgers read Aaron's re-acceptance from 9:20 at their own sittings); THE TWO HALVES of destruction_halved on the tape: Nadab and Abihu's fire (Leviticus 10:1-2 — SD.fire) and the succession at Hor (Numbers 20:26-28 — garments_transferred on aaron); atoned_forgiven on aaron STANDS beside the new status"}}
  - {{from: not_righteousness, to: good_land, disposition: CALL, link: reference, carries: verdict,
     why: "{W}9:7's 'from the day you came out of Egypt until you came to this place' spans 8:2's 'these forty years' (GL.the_way_of_forty_years('forty_years') CALLED — [40] the parser's at 8:2 and 8:4; the readback's fifth form the sixth's nearest kin: a STATE there, a STRETCH here — the forty years of the wilderness against the forty days of the mountain, both the parser's [40]); 9:26's 'which You redeemed' 7:8's and 15:15's redemption (the readback row VARIANT with Exodus 32:11's 'brought out')"}}
  - {{from: sequence, to: not_righteousness, disposition: CALL, link: none,
     why: "{W}the sequential run's REGISTRATION edge — ('cold_run_not_righteousness', 'law_not_righteousness') in DAEMON_ORDER (the runner compiles no verse: link none, O4's license); ONE tape line this sitting (prayed_for_aaron, dated (1, 4, 18) by the RETROGRADE marker at Deut 9:20, reading_placed; the FORWARD marker at 9:21 ends the stretch at the counter's day (40, 11, 1)); the daemon's one status written on its own line — THE REST drops it, no declared delta"}}
'''
    a = "  - {from: sequence, to: good_land, disposition: CALL, link: none,"
    i = text.index(a); j = text.index('\n', text.index('why:', i)) + 1
    text = text[:j] + edges + text[j:]
    open(path, 'w', encoding='utf-8').write(text)
dep = yaml.safe_load(open(path, encoding='utf-8'))
n_ch = sum(1 for e in dep['edges'] if e['from'] == 'not_righteousness')
assert 'not_righteousness' in dep['spans'] and n_ch == 11, n_ch   # the design's eleven CALL edges — the census decides (the callees' print first; the dependency gate's demands after)
print('dependency: span + 12 edges (not_righteousness 11 CALL and the registration); the token-demanded edges and the pointers after the gate\'s print')
# ---- the installation probe's count ----
path = f"{ROOT}/World/step9/installation_probes.py"
text = open(path, encoding='utf-8').read()
if "len(real) == 68 and all(" in text:
    old = "len(real) == 68 and all('given_at' in d and 'installed_by' in d for d in real.values())   # THE DEUTERONOMY WALK 6b (2026-09-19): 67 -> 68,"
    assert text.count(old) == 1, text.count(old)
    text = text.replace(old, "len(real) == 69 and all('given_at' in d and 'installed_by' in d for d in real.values())   # THE DEUTERONOMY WALK 7b (2026-09-19): 68 -> 69, law_not_righteousness (given_at Deut 9:1 — the chapter's frame; installed_by boot); 6b: 67 -> 68,")
    open(path, 'w', encoding='utf-8').write(text)
assert "len(real) == 69" in open(path, encoding='utf-8').read()
print('installation_probes I5: 69')
