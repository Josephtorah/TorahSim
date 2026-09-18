import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE DEUTERONOMY WALK sitting 4b — THE COMPILE OF CHAPTER 6 (2026-09-17; World/step9/DEUTERONOMY_WALK.md "Sitting 4b"): THE TYPES FIRST — TWO tape
# kinds (shema_declared 6:4-9 — the creed and the four duties, the chapter's own day, NO marker; testing_barred 6:16-19 — Massah the tape's named line),
# (both STATUTE by form — the own-day giving of a law, as chapter 4's three lines), ONE case kind (shema_case), TWO new effects (shema_commanded a STATUS on Israel; test_barred a BLOCK on Israel), NO registry row (Israel the written-on
# party), the 66th daemon's block (law_hear_o_israel, given_at Deut 6:4 — the Shema's first and only giving, installed_by boot — the two Deuteronomy
# daemons' form), the functions block (six cells WRAPPED), the dependency span and the ten CALL edges by the ink with the registration edge, the
# installation probe's count 65 -> 66. The `he` is cut from the pointed DB text by FINDING the phrase's tokens (never a typed index); the claim ids and
# the step ids READ from the frozen unit. Idempotent (add_types_ch5.py's form, derived by hand where it differs).
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
unit = open(f'{ROOT}/logic/units/deu_06_shema.yaml', encoding='utf-8').read()
CL = sorted(set(re.findall(r'DV06-\d+', unit))); ST = sorted({int(x) for x in re.findall(r'STEP_Dt_6_(\d+)', unit)})
assert len(CL) == 6 and ST[0] == 1 and ST[-1] == 25, (CL, ST[:3], ST[-1])
CORPUS = f"deu_06_shema (STEP_Dt_6_1 through STEP_Dt_6_25; claims {CL[0]} through {CL[-1]})"
SUB = "submitted by cold_run_hear_o_israel.py [subjects: %s] (the narrative scene, THE DEUTERONOMY WALK 4b); re-submitted on the sequential tape by cold_run_sequence.py; consumed by law_hear_o_israel (cold_run_hear_o_israel.py) -> %s"
CASE = "submitted by cold_run_hear_o_israel.py [subjects: the exam's persons] (the wrap's scene); consumed by law_hear_o_israel (cold_run_hear_o_israel.py) -> %s"
INK = "Deut 6:1-25; Onkelos Deut 6:1-25 (the export's division the DB's; 'your property' at 6:5, 'before him' at 6:13); the Sifrei on Deuteronomy piskaot 31-36 heading on 6:4-9 (67 rows read whole in both files; eight rows citing the chapter from elsewhere; the two files diverge at 36:10); the reading ledger deu_06_vaetchanan_2026-09-17.md (97 sources, 6 claims); the exam docket deu_06_vaetchanan_exam_2026-09-17.md (747 rows, REREAD WHOLE: LAW 346 / DERIVATION 57 / DISPUTE 83 / CONTEXT 261)"
D, X = 'Deut', 'Exod'
KINDS = [
 ("shema_declared", "statute",   # STATUTE — the own-day giving of a law passes the stitcher's register test BY FORM (chapter 4's three lines the form; a speech needs a narrated verb within ten verses; retyped 2026-09-17 after the stitcher's first print dropped both lines as register-off)
  "the Shema declared — 'HEAR, O ISRAEL: THE LORD OUR GOD, THE LORD IS ONE; and you shall love the LORD your God with all your heart and with all your soul and with all your might; and these words which I command you this day shall be upon your heart; and you shall teach them diligently to your sons and speak of them when you sit in your house and when you walk by the way and when you lie down and when you rise up; and you shall bind them for a sign upon your hand and they shall be for frontlets between your eyes; and you shall write them upon the doorposts of your house and upon your gates' (Deut 6:4-9) — THE CHAPTER'S OWN LINE, spoken on the counter's day (40, 11, 1) in Moses' speech, NO marker (the retrograde stretch of 5:23 ended at 5:32's forward marker): the creed's word the numeral (the parser's [1] at 6:4 — the reading's one number verse), the four duties given here for the first time (no runner held a cell for the recitation, the teaching, the tefillin or the mezuzah — the recon's regex over all sixty runners); shema_commanded on Israel (a STATUS: the four duties standing); the answer sheet Mishnah Berakhot 1:1-3:6 with 2:2, 9:5, Menachot 3:7, Sotah 7:1 (the exam's case kind); the creed's first saying Jacob's sons' answer at his bed (the Sifrei 31:1, 31:6; Pesachim 56a)",
  HE(D, 6, 4, 9, "hear, O Israel: the LORD our God, the LORD is one"), WIT(D, 6, 4, 9), INK, CORPUS,
  SUB % ("israel", "shema_commanded on israel_people (a STATUS on the counter's day (40, 11, 1) — the four duties: the recitation, the teaching, the tefillin, the mezuzah)"), ["creed", "duties"]),
 ("testing_barred", "statute",
  "testing barred — 'YOU SHALL NOT TEST THE LORD YOUR GOD, AS YOU TESTED HIM AT MASSAH; you shall surely keep the commandments of the LORD your God and his testimonies and his statutes which he commanded you; and you shall do the right and the good in the eyes of the LORD, that it may be well with you and that you may go in and possess the good land which the LORD swore to your fathers, to thrust out all your enemies from before you, as the LORD has spoken' (Deut 6:16-19) — THE CHAPTER'S SECOND LINE on the counter's day (40, 11, 1), NO marker; Massah A RUN CITATION BY NAME: the tape's own named line at Exodus 17:7 ('Massah and Meribah' — murmured 17:2-3 'give us water', rock_struck 17:6) FOUND by kind and first verse; the trials counted ten (Arakhin 15a — 'two at the water', Marah and Rephidim; exodus_story.trials by CALL); test_barred on Israel (a BLOCK); 'surely keep' the infinitive absolute (6:17 — the testimonies' three seats 4:45, 6:17, 6:20); 'the right and the good' Bava Metzia 108a's abutter (the rule beyond the letter seated in the ink's own words)",
  HE(D, 6, 16, 19, "you shall not test the LORD your God, as you tested him at Massah"), WIT(D, 6, 16, 19) + WIT(X, 17, 2, 7), INK, CORPUS,
  SUB % ("israel", "test_barred on israel_people (a BLOCK on the counter's day (40, 11, 1); the first telling Exod 17:2-7 named in the row — Massah)"), ["first_telling", "massah"]),
 ("shema_case", "case", "the exam's rows on chapter 6 (Deut 6:1-25 — the recitation's times, postures, intention, audibility, language and exemptions: Mishnah Berakhot 1:1-3:6, Sotah 7:1, Berakhot 2a-2b, 10b-11a, 13a-13b, 15a-15b, 16a; the three passages' order: 2:2, the Sifrei 34:2-3; the three terms of the love: 9:5, 61b (R. Akiva), Sanhedrin 74a (the martyr); the tefillin's four passages and compartments, arm, order and head: Menachot 3:7, 34b-37b, Sanhedrin 4b:12-14, the Sifrei 35:3-12; the mezuzah's scroll, post, side and gates: Menachot 31b-34a, Shabbat 103b, Yoma 11a, Maaser Sheni 3:8, the Sifrei 36:1-8; the seven: Menachot 43b; the father's duties: Kiddushin 29a-30b; the creed at Jacob's bed: Pesachim 56a; the oath by the Name: Temurah 3b-4a; the abutter: Bava Metzia 108a; the four sons: Pesachim 116a-b, Mishnah Pesachim 10:4) — the exam's persons through the cells' asks: the priest entering to eat his terumah, the reader reclining by the road, the one who did not hear his own words, the mourner, the bridegroom, the woman at the recitation, the one who bound the head first, the one who wrote on a stone, the one who fixed the post on the left, the seven-blessing reciter, the true swearer, the abutter's buyer, the wise son and the one who cannot ask",
  PHRASE(D, 6, 4, ['שמע', 'ישראל']) + " (hear, O Israel — Deut 6:4)", WIT(D, 6, 1, 25), INK, CORPUS, CASE % "accepted / exempt (the exam's persons — the rule holds against him; outside the rule)", ["person", "ask"]),
]
assert len(KINDS) == 3, len(KINDS)
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
# ---- TWO new effects, the ink's own words, the `he` FOUND in the verse ----
path = f"{ROOT}/World/step9/effect_vocabulary.yaml"
text = open(path, encoding='utf-8').read()
fx = yaml.safe_load(text)['effects']
for e in ('accepted', 'exempt', 'commanded', 'other_gods_barred', 'coveting_barred', 'torah_expounded', 'tested_the_lord'):
    assert e in fx, e
HE_SHEMA = PHRASE(D, 6, 4, ['שמע', 'ישראל', 'יהוה', 'אלהינו', 'יהוה', 'אחד'])
HE_TEST = PHRASE(D, 6, 16, ['לא', 'תנסו', 'את', 'יהוה', 'אלהיכם'])
NEW = [
 ('shema_commanded', 'status',
  "the Shema commanded — the STATUS the chapter's own line writes on Israel: the creed 'hear, O Israel: the LORD our God, the LORD is one' (6:4) and THE FOUR DUTIES standing from its giving — the love with all the heart, the soul and the might (6:5 — the two inclinations, the martyr's soul, the money: Mishnah Berakhot 9:5, 61b, Sanhedrin 74a), the words upon the heart (6:6), THE TEACHING and THE RECITATION ('teach them diligently to your sons and speak of them … when you lie down and when you rise up', 6:7 — the evening from 'lie down', the morning from 'rise': Mishnah Berakhot 1:1-2; the postures 1:3; the intention 2:1; the audibility 2:3; any language Sotah 7:1; the exemptions 3:1-6; the three passages in order 2:2), THE TEFILLIN ('bind them for a sign upon your hand, and they shall be for frontlets between your eyes', 6:8 — the four passages Menachot 3:7; the compartments FOUR a PARAMETER taught by the shelf — the Sifrei 35:3-4, Menachot 34b-35a, Sanhedrin 4b:12-14 — whose derivation reads 11:18 'frontlets' defective where the ink is plene: THE OPEN ROW the_spellings; the arm, the order, the head 35:5-12), THE MEZUZAH ('write them upon the doorposts of your house and upon your gates', 6:9 — a scroll in ink, the right post, the dwelling's gates: the Sifrei 36:1-8, Menachot 31b-34a, Yoma 11a); given on the counter's day (40, 11, 1), no marker — the four duties compiled here for the first time",
  HE_SHEMA + " (hear, O Israel: the LORD our God, the LORD is one — Deut 6:4)",
  "Deut 6:4-9 (the creed and the four duties), 6:5 ('with all your heart, soul and might'), 11:13-21 (the second passage — the tefillin and the mezuzah restated, forward), Exodus 13:9, 13:16 (the sign upon the hand — the first passages), Numbers 15:37-41 (the third passage recited — the fringes, mekoshesh's span); Onkelos 6:5 ('your property'); the Sifrei on Deuteronomy 31-36; Mishnah Berakhot 1:1-3:6, 2:2, 9:5, Menachot 3:7, Sotah 7:1; Babylonian Talmud Berakhot 2a-2b, 10b-11a, 13a-13b, 15a-15b, 61b, Menachot 34b-37b, 43b, Sanhedrin 4b:12-14, Kiddushin 29a-30b, Shabbat 103b, Yoma 11a, Pesachim 56a",
  f"deu_06_shema (STEP_Dt_6_4 through STEP_Dt_6_9; the claims {CL[0]} through {CL[-1]})",
  "cold_run_hear_o_israel.py (F2 the_creed — hear_o_israel, the_lord_is_one, with_all_your_heart, with_all_your_soul, with_all_your_might, love_and_fear; F3 the_four_duties — recite_when, recite_how, recite_who, the_passages, teach_your_sons, tefillin_passages, tefillin_compartments, tefillin_arm, tefillin_order, tefillin_head, mezuzah_writing, mezuzah_doorpost, mezuzah_gates, the_seven, the_write; the exam kind shema_case; the status written on the tape kind shema_declared)"),
 ('test_barred', 'block',
  "testing barred — the BLOCK the chapter's second line writes on Israel: 'you shall not test the LORD your God, as you tested him at Massah' (6:16) — Massah the tape's own named line (Exodus 17:7 'Massah and Meribah'; 17:2-3 the murmuring 'give us water … why do you test the LORD', 17:6 the rock struck): a RUN CITATION by name; the wilderness trials counted ten (Arakhin 15a — 'two at the water', Marah and Rephidim; Numbers 14:22 'tested me these ten times'; exodus_story.trials by CALL); with it 'you shall surely keep the commandments … his testimonies and his statutes' (6:17 — the infinitive absolute; the testimonies' three seats 4:45, 6:17, 6:20) and 'the right and the good' (6:18 — Bava Metzia 108a's abutter: the buyer of the adjoining field yields to the neighbor, a rule beyond the letter seated in the ink's own words); written on the counter's day (40, 11, 1), no marker",
  HE_TEST + " (you shall not test the LORD your God — Deut 6:16)",
  "Deut 6:16-19; Exodus 17:1-7 (Massah — the first telling on the tape: murmured, rock_struck, named), 17:2 ('why do you test the LORD'); Numbers 14:22 ('these ten times'); Deut 4:45 and 6:20 (the testimonies' seats); Psalm 95:8-9; Babylonian Talmud Arakhin 15a:8-13 (the ten trials), Bava Metzia 108a:1-4 (the abutter)",
  f"deu_06_shema (STEP_Dt_6_16 through STEP_Dt_6_19; the claims {CL[0]} through {CL[-1]})",
  "cold_run_hear_o_israel.py (F5 the_test_and_the_right — you_shall_not_test, surely_keep, the_right_and_the_good, thrust_out_enemies; the exam kind shema_case; the block written on the tape kind testing_barred)"),
]
added = 0
for name, op, en, he, ink, corpus, exam in NEW:
    if name in fx: continue
    text = text.rstrip('\n') + '\n' + f"  {name}:\n    en: {q(en)}\n    he: {q(he)}\n    ledger_op: {op}   # THE DEUTERONOMY WALK 4b (2026-09-17): chapter 6's compile — {name}\n    ink: {q(ink)}\n    corpus: {q(corpus)}\n    exam: {q(exam)}\n"
    added += 1
open(path, 'w', encoding='utf-8').write(text)
fx = yaml.safe_load(open(path, encoding='utf-8'))['effects']
assert all(n in fx for n, *_ in NEW) and fx['shema_commanded']['ledger_op'] == 'status' and fx['test_barred']['ledger_op'] == 'block'
print('effects: %d added (registry %d); the he found in the verses: %s | %s' % (added, len(fx), HE_SHEMA, HE_TEST))
# ---- NO registry row (Israel the written-on party, standing) ----
reg = yaml.safe_load(open(f"{ROOT}/logic/corpus/entity_registry.yaml", encoding='utf-8'))
assert 'israel_people' in {e['id'] for e in reg['entities']}, 'the written-on party must stand'
print('entities: none added (registry %d)' % len(reg['entities']))
# ---- the daemon block + the functions block (daemon_dispositions.yaml) ----
path = f"{ROOT}/World/step9/daemon_dispositions.yaml"
text = open(path, encoding='utf-8').read()
if '  law_hear_o_israel:' not in text:
    block = '''  law_hear_o_israel:
    file: cold_run_hear_o_israel.py
    wraps: hear_o_israel
    given_at: Deut 6:4
    installed_by: boot   # THE DEUTERONOMY WALK 4b (2026-09-17): THE SHEMA'S FIRST AND ONLY GIVING — the chapter's own line on the counter's day (40, 11, 1), no marker (the retrograde stretch of 5:23 ended at 5:32); installed by boot like law_opening_speech and law_obey_horeb (the two Deuteronomy daemons' form); the four duties compiled here for the first time; the status and the block written at the chapter's own lines
    watches:
      shema_declared: [shema_commanded]   # Deut 6:4-9: the creed and the four duties (the recitation, the teaching, the tefillin, the mezuzah) — a STATUS on Israel on the counter's day
      testing_barred: [test_barred]       # Deut 6:16-19: 'you shall not test … as you tested at Massah' — a BLOCK on Israel; Massah the tape's named line (Exod 17:7), a run citation by name
      shema_case: [accepted, exempt]      # the exam's rows on the chapter — the persons through the cells' asks (the priest at evening accepted, the bridegroom exempt, the abutter's buyer accepted …)
'''
    i = text.index('  law_census:')
    text = text[:i] + block + text[i:]
if '\n  hear_o_israel:   # THE DEUTERONOMY WALK 4b' not in text:
    fb = '''  hear_o_israel:   # THE DEUTERONOMY WALK 4b (2026-09-17)
    the_header: {status: WRAPPED, by: law_hear_o_israel}
    the_creed: {status: WRAPPED, by: law_hear_o_israel}
    the_four_duties: {status: WRAPPED, by: law_hear_o_israel}
    the_gift_and_the_warning: {status: WRAPPED, by: law_hear_o_israel}
    the_test_and_the_right: {status: WRAPPED, by: law_hear_o_israel}
    the_sons_question: {status: WRAPPED, by: law_hear_o_israel}
'''
    i = text.index('  covenant_at_horeb:   # THE DEUTERONOMY WALK 3b')
    j = text.index('\n  pre_sinai:', i)
    text = text[:j + 1] + fb + text[j + 1:]
open(path, 'w', encoding='utf-8').write(text)
dd = yaml.safe_load(open(path, encoding='utf-8'))
assert 'law_hear_o_israel' in dd['daemons'] and 'hear_o_israel' in dd['functions'], (list(dd)[:5])
print('daemons: %d (law_hear_o_israel %s); functions blocks: %d' % (len(dd['daemons']), 'law_hear_o_israel' in dd['daemons'], len(dd['functions'])))
# ---- the dependency span + the CALL edges by the ink (the token-demanded edges and the POINTERS after the gate's print) ----
path = f"{ROOT}/World/step9/dependency_dispositions.yaml"
text = open(path, encoding='utf-8').read()
if '\n  hear_o_israel:' not in text.split('\nedges:')[0]:
    a = "  covenant_at_horeb: [[Deut, 5, 1, 33]]"
    i = text.index(a); j = text.index('\n', i)
    text = text[:j + 1] + "  hear_o_israel: [[Deut, 6, 1, 25]]   # THE DEUTERONOMY WALK 4b (2026-09-17; DEUTERONOMY_WALK.md \"Sitting 4b\"): chapter 6 — THE SHEMA: the creed and the four duties compiled for the first time (the recitation, the teaching, the tefillin, the mezuzah), the test at Massah a run citation by name, the right and the good, the son's question — THE READBACK'S THIRD FORM (a retelling inside a law); two lines on the counter's day, no marker\n" + text[j + 1:]
    W = "THE DEUTERONOMY WALK 4b (2026-09-17) | "
    edges = f'''  - {{from: hear_o_israel, to: covenant_at_horeb, disposition: CALL, link: reference, carries: verdict,
     why: "{W}6:14's 'you shall not go after other gods' and 6:15's 'a jealous God in your midst … lest he destroy you' are the second word's clauses (CH.the_second_word('no_other_gods', 'the_visiting') CALLED — other_gods_barred stands from 3b, NO second write, CO5); 6:1's 'this is the commandment … which the LORD your God commanded to teach you' is the charge's line stand_here_commanded (CH.the_answer_and_the_charge('stand_here_with_me', 'the_charge') CALLED — 5:28-31, the debit CLOSED by the prior run, CO7); the readback's rows 6:1, 6:24 and 6:25 graded against 3b's lines"}}
  - {{from: hear_o_israel, to: obey_horeb, disposition: CALL, link: reference, carries: verdict,
     why: "{W}6:12's 'take heed to yourself lest you forget the LORD' is obey_horeb's FORGET census (OH.horeb_retold('take_heed_lest_you_forget') CALLED — the thirteen seats, 6:12 among them); 6:17 and 6:20's 'testimonies' are the 4:45 header's three seats (OH.the_cities_and_the_frame('the_second_frame') CALLED); 6:5's 'with all your heart and with all your soul' 4:29's kin (OH.the_exile_case('seek_and_find') CALLED); OH.READBACK the second chapter's rows the third form joins"}}
  - {{from: hear_o_israel, to: decalogue, disposition: CALL, link: reference, carries: verdict,
     why: "{W}6:13's 'and by his name you shall swear' is a POSITIVE clause whose prohibition is the third word's (DC.vain_name('vain_oath', 'false_future_oath') CALLED — the vain and the false oath; Temurah 3b-4a: the true oath commanded from 6:13, Shevuot 35a the Name in an oath); the ten words excluded from the daily recitation (Berakhot 12a — the passages' order, DC's seat by REFERENCE)"}}
  - {{from: hear_o_israel, to: exodus_story, disposition: CALL, link: reference, carries: verdict,
     why: "{W}6:16's 'as you tested him at Massah' is the wilderness trials' census (ES.trials('ten_list', 'count_by_exodus') CALLED — 'two at the water', Marah and Rephidim; the tape's murmured / rock_struck / named at Exodus 17:2-7 FOUND by kind and first verse, CO3); 6:21-22's 'the LORD brought us out of Egypt with a strong hand … signs and wonders great and grievous upon Egypt' the ten plague_struck lines and brought_out READ BACK (found on the tape by kind — CO4, CO8; ES.plagues the plagues' cell by REFERENCE)"}}
  - {{from: hear_o_israel, to: pesach, disposition: CALL, link: reference, carries: verdict,
     why: "{W}6:20's 'when your son asks you tomorrow, saying' is Exodus 13:14 VERBATIM (the four sons — Pesachim 116a-b; Mishnah Pesachim 10:4 'according to the son's understanding'): the passover runner's firstborn cell holds 13:8's 'you shall tell your son' and 13:14's question (PE.firstborn CALLED for the ink's seat — the DATA row the_four_sons; the answer's rows the third form's reference rows); 13:9 and 13:16's 'a sign upon your hand' the tefillin's first passages (PE by REFERENCE — no tefillin cell there)"}}
  - {{from: hear_o_israel, to: opening_speech, disposition: CALL, link: reference, carries: verdict,
     why: "{W}6:10, 6:18 and 6:23's 'the land which the LORD swore to your fathers' are 1:8's seats at the book's opening (OS.the_frame CALLED — the oath's seats and the frame's write torah_expounded; OS.READBACK the first form the third joins); 6:24's 'the LORD commanded us to do all these statutes' the book's own charge, 1:5's expounding the charge's run (CO7)"}}
  - {{from: hear_o_israel, to: mamre, disposition: CALL, link: reference, carries: verdict,
     why: "{W}6:10, 6:18 and 6:23's 'which he swore to your fathers, to Abraham, to Isaac and to Jacob' — the oath's lines on the tape: sworn_by_himself at Genesis 22:16-18 ('by myself I have sworn' — MA.moriah CALLED), oath_upheld at 26:3-5 (MA.isaac_gerar CALLED); the RUN_CITATION pointers at Deut 6:10 / 6:18 / 6:23 name them; the readback row 6:23 FOUND on the running world (CO4)"}}
  - {{from: hear_o_israel, to: joseph, disposition: CALL, link: reference, carries: verdict,
     why: "{W}the oath's third line — visitation_promised at Genesis 50:24 'the land which he swore to Abraham, to Isaac and to Jacob' (JS.the_oath CALLED — Joseph's words the first telling of the three names together on the tape; the readback row 6:23 FOUND, CO4)"}}
  - {{from: hear_o_israel, to: mekoshesh, disposition: CALL, link: reference, carries: verdict,
     why: "{W}6:6-7's 'these words … you shall speak of them' are recited with the THIRD passage, the fringes of Numbers 15:37-41 (Mishnah Berakhot 2:2 the order; the Sifrei 34:2-3: the fringes recited, not bound; Menachot 43b the seven): the fringes' verses sit in mekoshesh's span and its cell the_gatherer compiles the wood-gatherer alone — the recitation's third passage a REFERENCE into that span (MK.the_gatherer('the_case') CALLED for the span's own seat); the fringes' own law, read on the docket, has no cell: the 4b box's owed line"}}
  - {{from: hear_o_israel, to: erection, disposition: CALL, link: reference, carries: verdict,
     why: "{W}6:1-3's 'the commandment, the statutes and the judgments which the LORD your God commanded to teach you' executes Exodus 24:12's 'the law and the commandment … to teach them' (ER.ascent('torah_mitzvah') CALLED — the charge's debit, CO7); 6:22-23's 'to give us the land which he swore' the covenant's book (ER.blood_covenant('book_of_covenant') CALLED where the cell asks)"}}
  - {{from: sequence, to: hear_o_israel, disposition: CALL, link: none,
     why: "{W}the sequential run's REGISTRATION edge — ('cold_run_hear_o_israel', 'law_hear_o_israel') in DAEMON_ORDER (the runner compiles no verse: link none, O4's license); the two tape lines this sitting's on the counter's day, NO marker; the daemon's status and block written on its own lines"}}
'''
    a = "  - {from: sequence, to: covenant_at_horeb, disposition: CALL, link: none,"
    i = text.index(a); j = text.index('\n', text.index('why:', i)) + 1
    text = text[:j] + edges + text[j:]
    open(path, 'w', encoding='utf-8').write(text)
dep = yaml.safe_load(open(path, encoding='utf-8'))
n_ch = sum(1 for e in dep['edges'] if e['from'] == 'hear_o_israel')
assert 'hear_o_israel' in dep['spans'] and n_ch == 10, n_ch
print('dependency: span + 11 edges (hear_o_israel 10 CALL and the registration); the token-demanded edges and the pointers after the gate\'s print')
# ---- the installation probe's count ----
path = f"{ROOT}/World/step9/installation_probes.py"
text = open(path, encoding='utf-8').read()
if "len(real) == 65 and all(" in text:
    old = "len(real) == 65 and all('given_at' in d and 'installed_by' in d for d in real.values())   # THE DEUTERONOMY WALK 3b (2026-09-16): 64 -> 65,"
    assert text.count(old) == 1, text.count(old)
    text = text.replace(old, "len(real) == 66 and all('given_at' in d and 'installed_by' in d for d in real.values())   # THE DEUTERONOMY WALK 4b (2026-09-17): 65 -> 66, law_hear_o_israel (given_at Deut 6:4 — the Shema's own giving; installed_by boot); 3b: 64 -> 65,")
    open(path, 'w', encoding='utf-8').write(text)
assert "len(real) == 66" in open(path, encoding='utf-8').read()
print('installation_probes I5: 66')
