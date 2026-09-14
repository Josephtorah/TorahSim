#!/usr/bin/env python3
# THE NUMBERS WALK sitting 10b — THE COMPILE OF THE VOWS (2026-09-12; World/step9/NUMBERS_WALK.md "Sitting 10b"): THE TYPES FIRST — ONE new
# kind on the tape (the vows' law spoken by Moses to the heads of the tribes, Num 30:2-17 — a law in MOSES' VOICE with no divine frame), THREE
# case-form kinds for THE STATE MACHINE (vow_uttered / vow_heard / vow_restrained), SEVEN case kinds for the exam's scene, FOUR new effects
# (vow_bound debit, vow_confirmed status, vow_annulled heaven, iniquity_borne heaven — the ink's own verbs), NO registry row, the 57th daemon's
# block (law_vows, installed_by BOOT with the class NAMED — the decision of the design), the functions block, the dependency span and edges (the
# pointers after the gate's print), the installation probe's count, and THE CALENDAR ROW vow_annulment_window with its two recorded settings.
# The `he` is cut from the pointed DB text (cantillation stripped) by FINDING the phrase's tokens (never a typed index); the witnesses the plain
# consonantal verses. Idempotent (add_types_musafim.py's form).
import re, sqlite3, yaml
ROOT = "<repo-old>"
db = sqlite3.connect(f"file:{ROOT}/elijah_docket/tanakh.sqlite?mode=ro", uri=True)
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
def PHRASE(ch, vs, toks):
    """the pointed text of the phrase FOUND in the verse by its plain tokens (the index computed, never typed)"""
    plain = LV('Num', ch, vs).split(); n = len(toks)
    hits = [i for i in range(len(plain) - n + 1) if plain[i:i + n] == toks]
    assert len(hits) == 1, (ch, vs, toks, hits)
    return PV('Num', ch, vs, hits[0] + 1, hits[0] + n)
q = lambda s: '"' + s.replace('\\', '\\\\').replace('"', '\\"') + '"'
N = 'Num'
def HE(ch, lo, hi, en, cap=6):
    vv = list(range(lo, min(hi, lo + cap - 1) + 1))
    s = ' · '.join(PV(N, ch, v) + ' (%s — Num %d:%d)' % (en if v == lo else 'the verse continues', ch, v) for v in vv)
    return s + (' · … (through Num %d:%d)' % (ch, hi) if hi > vv[-1] else '')
def WIT(ch, lo, hi):
    return ['Num %d:%d | %s' % (ch, v, LV(N, ch, v)) for v in range(lo, hi + 1)]
CORPUS = "num_30_vows (STEP_Nm_30_1 through STEP_Nm_30_17; claims MT30A-01 through MT30A-07)"
SUB = "submitted by cold_run_vows.py [subjects: %s] (the command scene, THE NUMBERS WALK 10b); re-submitted on the sequential tape by cold_run_sequence.py; consumed by law_vows (cold_run_vows.py) -> %s"
MACH = "submitted by cold_run_vows.py [subjects: the vower and the authority] (THE STATE MACHINE's bench — the Mishnah's rows replayed on the world engine); consumed by law_vows (cold_run_vows.py) -> %s"
CASE = "submitted by cold_run_vows.py [subjects: the exam's persons] (the wrap's scene); consumed by law_vows (cold_run_vows.py) -> %s"
INK_ALL = "Num 30:1-17; Onkelos Num 30:1-17 (the oath, the confirming and the statutes by ONE Aramaic root; 'her husband' her OWNER at nine seats; 'from day to day' with the Psalm's preposition at 30:15); Sifrei Bamidbar 153-156; Lev 5:4 (the utterance oath — the Sifrei 153:7's identity); Num 6:2 (the nazirite's vow-identity — 153:3); Num 5:31 (the suspected wife's 'bear her iniquity' — 156:2); Lev 22:13 (the priest's daughter 'a widow or a divorced woman ... as in her youth'); Deut 23:22-24 (the delay ban; 'that which has gone out of your lips'); Num 32:24 (the next portion's echo); Babylonian Talmud Nedarim 66a-91b, 64a-65b, 10a-13b; Shevuot 20a-27a; Niddah 45b-46a; Kiddushin 41b-42a; Rosh Hashanah 4a-6a; Chagigah 10a; Sanhedrin 100a; Yoma 76a; Yevamot 87a; Shabbat 157a; Mishnah Nedarim 9-11; Mishnah Niddah 5:6; Mishnah Shabbat 24:5; Mishnah Chagigah 1:8"
FIRST = "and Moses spoke to the heads of the tribes of the children of Israel, saying: this is the thing which the LORD commanded"
KINDS = [
 ("vows_law_spoken", "speech",
  "the vows' law spoken — MOSES' ONE SPEECH to the heads of the tribes, Num 30:2-17, A LAW IN MOSES' VOICE WITH NO DIVINE FRAME: 'and Moses spoke to the heads of the tribes of the children of Israel, saying: THIS IS THE THING WHICH THE LORD COMMANDED' (30:2 — the formula at eight Bible seats; its two Numbers seats, 30:2 and 36:6, are the book's two law chapters without 'the LORD spoke to Moses'); the two 'when' cases (30:3 a man; 30:4 a woman in her youth in her father's house) and the seven 'and if' branches (30:6, 7, 9, 11, 13, 15, 16) — the daughter, the betrothed, the widow and the divorcee (30:10), the married woman, the affliction oath, the silence from day to day, the annulment after the hearing; the footer 'these are the statutes which the LORD commanded Moses, between a man and his wife, between a father and his daughter, in her youth in her father's house' (30:17); the addressee THE HEADS OF THE TRIBES a field (no entity — the registry holds the princes of Israel; the Sifrei 153:1's 'by experts alone' the shelf's own addition)",
  HE(30, 2, 7, FIRST) + ' · … (through Num 30:17)', WIT(30, 2, 17), INK_ALL, CORPUS,
  SUB % ("moses", "commanded on israel_people (value 'the statutes of vows — Num 30:2-17'); NO timer, NO close, NO entity (the counter's day; no marker in the chapter)"), ["to", "heads", "close"]),
 ("vow_uttered", "case",
  "a vow uttered — THE STATE MACHINE's first event: 'a man, when he vows a vow to the LORD or swears an oath to bind a bond on his soul' (30:3) / 'and a woman, when she vows a vow to the LORD and binds a bond in her father's house in her youth' (30:4): the vower's status (a man; a daughter in her youth in her father's house; a betrothed maiden; a widow or divorcee from marriage; a married woman; a mature daughter), the kind (vow / oath), the content class (affliction / between him and her / other), the age (the DATA row vow_ages: the examined year's 'knows to Whom') and the hook (days / marital status — Nedarim 89a:4-5) — the effect vow_bound (a DEBIT on the vower toward HEAVEN) or exempt (the minor; the void vow)",
  HE(30, 3, 4, "a man, when he vows a vow to the LORD, or swears an oath to bind a bond on his soul, he shall not profane his word; according to all that proceeds out of his mouth he shall do"), WIT(30, 3, 4), INK_ALL, CORPUS,
  MACH % "vow_bound (debit) / exempt", ["vower", "kind", "status", "content_class", "age", "knows_to_whom", "hook"]),
 ("vow_heard", "case",
  "the vow heard — THE STATE MACHINE's second event, the trigger of the hearing-day clock: 'and her father hears her vow ... and her father is silent to her' (30:5), 'and her husband hears it, on the day of his hearing, and is silent to her' (30:8), 'and if her husband altogether hold his peace at her from day to day' (30:15): the authority (father / husband / both), by report or not (the Sifrei 153:5; the deaf excluded — Nedarim 73a:4), silent (the timer vow_confirmed due at the hearing day + 1 — the calendar row vow_annulment_window) or the confirming words ('you did well' — Nedarim 77b:5: confirmed at once), intending her (the wife thought the daughter — Mishnah Nedarim 11:5)",
  HE(30, 5, 5, "and her father hears her vow and her bond which she bound on her soul, and her father is silent to her, then all her vows shall stand, and every bond which she bound on her soul shall stand"), WIT(30, 5, 5) + WIT(30, 8, 8) + WIT(30, 15, 15), INK_ALL, CORPUS,
  MACH % "vow_confirmed (a TIMER on the vower, due the hearing day + 1; or at once on the confirming words) / exempt (the deaf: no hearing)", ["vower", "by", "report", "silent", "confirm_words", "intends_her"]),
 ("vow_restrained", "case",
  "the vow restrained — THE STATE MACHINE's third event, the annulment's act: 'and if her father restrain her on the day of his hearing ... the LORD will forgive her because her father restrained her' (30:6), 'and if on the day her husband hears he restrain her and annul her vow' (30:9), 'her husband has annulled them, and the LORD will forgive her' (30:13), 'and if he annul, he annuls them after his hearing, then he shall bear her iniquity' (30:16): the authority (the father over the daughter in her youth in his house; father AND husband together over the betrothed — Mishnah Nedarim 10:1; the husband alone over the married, for affliction vows and vows between him and her — 30:14 + 30:17), on the day (cancel_timers + close the debit + vow_annulled: HEAVEN forgives her) or after the day (the vow stands, iniquity_borne on the husband), partial (R. Yishmael / R. Akiva / the Rabbis — Nedarim 87b:1-2), by a messenger (R. Yoshiyah / R. Yonatan — the Sifrei 153:6)",
  HE(30, 6, 6, "and if her father restrain her on the day of his hearing, all her vows and her bonds which she bound on her soul shall not stand, and the LORD will forgive her, because her father restrained her"), WIT(30, 6, 6) + WIT(30, 9, 9) + WIT(30, 13, 13) + WIT(30, 16, 16), INK_ALL, CORPUS,
  MACH % "vow_annulled (heaven — the timer cancelled, the debit closed) / iniquity_borne (heaven, on the husband — after the confirmation); the wrong authority writes nothing (the vow stands)", ["vower", "by", "on_the_day", "after_confirmation", "partial", "via_messenger"]),
 ("mans_vow_case", "case", "the exam's rows on the man's vow and oath (Num 30:2-3 — Nedarim 2b-3b, 10a-16b, 77b-78b, 81b, 90a; Shevuot 20a-27a; Chagigah 10a; Niddah 45b-46b; Rosh Hashanah 4a-6a): the frame's two verbs, the heads of the tribes and the sage's release, the ages, the vow against the oath, the vow's support, the substitutes, 'he shall not profane his word', the two transgressions and the delay ban, the inward acceptance",
  HE(30, 3, 3, "a man, when he vows a vow to the LORD, or swears an oath to bind a bond on his soul, he shall not profane his word; according to all that proceeds out of his mouth he shall do"), WIT(30, 2, 3), INK_ALL, CORPUS, CASE % "vow_bound / accepted / commanded / exempt (the exam's persons)", ["person", "ask"]),
 ("daughters_vow_case", "case", "the exam's rows on the daughter in her father's house (Num 30:4-6 — Nedarim 67b-70b, 72b-73a, 76b, 79a; Ketubot 40b-47a; Kiddushin 81b; Nazir 23a): in her youth, the father's domain, the hearing and the report, the deaf, the silence intending her, confirmed for one hour, restraint = annulment, the forgiveness of the woman who did not know, the caretaker and the messenger",
  HE(30, 4, 4, "and a woman, when she vows a vow to the LORD, and binds a bond in her father's house in her youth"), WIT(30, 4, 6), INK_ALL, CORPUS, CASE % "vow_bound / vow_confirmed / vow_annulled / accepted / exempt (the exam's persons)", ["person", "ask"]),
 ("betrothed_vow_case", "case", "the exam's rows on the betrothed maiden (Num 30:7-9 — Nedarim 66b-72a, 74a-76b; Shevuot 20a; Gittin 73b): the father and the husband together, the two deaths and the reversion, the vows carried to the last betrothed, the same-day divorce, annulling in advance, 'what came to confirmation came to annulment', the utterance = oath, the levirate widow, the sustained betrothed",
  HE(30, 7, 7, "and if she be, she shall be to a husband, and her vows are upon her, or the utterance of her lips with which she bound her soul"), WIT(30, 7, 9), INK_ALL, CORPUS, CASE % "vow_bound / vow_confirmed / vow_annulled / accepted / exempt (the exam's persons)", ["person", "ask"]),
 ("widows_vow_case", "case", "the exam's rows on the widow and the divorcee (Num 30:10 — Nedarim 88b-89b; Ketubot 49a; Yevamot 87a): from marriage not from betrothal, the orphan in her father's lifetime, remarried she is not a widow, the vow's timing (R. Yishmael / R. Akiva), once out one hour, the priest's daughter's pair of words",
  HE(30, 10, 10, "but the vow of a widow or of a divorced woman, everything with which she bound her soul, shall stand against her"), WIT(30, 10, 10), INK_ALL, CORPUS, CASE % "vow_bound / accepted / exempt (the exam's persons)", ["person", "ask"]),
 ("wifes_vow_case", "case", "the exam's rows on the married woman (Num 30:11-13 — Nedarim 67a-67b, 69a-69b, 72b-73a, 77b, 86b-87a; Nazir 20b; Kiddushin 81b; Bava Metzia 96a): in her husband's house, the vows before the marriage, the two silences, the confirming words, the mistaken annulment, the caretaker, the sage over the confirmation, the forgiveness",
  HE(30, 11, 11, "and if she vowed in her husband's house, or bound a bond on her soul by an oath"), WIT(30, 11, 13), INK_ALL, CORPUS, CASE % "vow_bound / vow_confirmed / vow_annulled / accepted / exempt (the exam's persons)", ["person", "ask"]),
 ("affliction_oath_case", "case", "the exam's rows on the affliction oath and the day (Num 30:14-16 — Nedarim 76b-77b, 79a-83b, 87a-87b; Shabbat 157a; Shevuot 27a; Yoma 76a; Sanhedrin 100a): the filter (affliction / between him and her), R. Yosei's cases, the two reaches, the partial annulment, the deadline's two settings, the Sabbath, the silence to vex, 'after his hearing' = after confirming, 'he shall bear her iniquity', the measure of good",
  HE(30, 14, 14, "every vow and every oath of binding to afflict a soul, her husband shall confirm it, or her husband shall annul it"), WIT(30, 14, 16), INK_ALL, CORPUS, CASE % "vow_bound / vow_confirmed / vow_annulled / iniquity_borne / accepted / exempt (the exam's persons)", ["person", "ask"]),
 ("statutes_case", "case", "the exam's rows on the footer and the chapter whole (Num 30:17 and 30:1 — Nedarim 68a, 70a-70b, 79b; Ketubot 40b, 46b, 47a; Kiddushin 3b; the register gate): the likening both ways, 'in her youth in her father's house' beyond vows, the receipt of 30:1 and the finder's second form, the case structure and the clock words computed, the doubled verbs",
  HE(30, 17, 17, "these are the statutes which the LORD commanded Moses, between a man and his wife, between a father and his daughter, in her youth in her father's house"), WIT(30, 17, 17) + WIT(30, 1, 1), INK_ALL, CORPUS, CASE % "accepted / commanded / exempt (the exam's persons)", ["person", "ask"]),
]
assert len(KINDS) == 11, len(KINDS)
# ---- the kinds: append INTO the `events:` mapping (before `narrative_verbs:`) ----
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
# ---- FOUR new effects, the ink's own verbs, the `he` FOUND in the verse ----
path = f"{ROOT}/World/step9/effect_vocabulary.yaml"
text = open(path, encoding='utf-8').read()
fx = yaml.safe_load(text)['effects']
for e in ('commanded', 'accepted', 'exempt', 'atoned_forgiven', 'nazirite_vow_bound'):
    assert e in fx, e
HE_BOUND = PHRASE(30, 3, ['לא', 'יחל', 'דברו', 'ככל', 'היצא', 'מפיו', 'יעשה'])
HE_CONF = PHRASE(30, 5, ['וקמו', 'כל', 'נדריה'])
HE_ANN = PHRASE(30, 6, ['ויהוה', 'יסלח', 'לה', 'כי', 'הניא', 'אביה', 'אתה'])
HE_INIQ = PHRASE(30, 16, ['ונשא', 'את', 'עונה'])
NEW = [
 ('vow_bound', 'debit',
  "the vow bound — the DEBIT the vow writes on the vower toward HEAVEN, its value the vow's kind and content: 'a man, when he vows a vow to the LORD, or swears an oath to bind a bond on his soul, HE SHALL NOT PROFANE HIS WORD; according to all that proceeds out of his mouth he shall do' (Num 30:3) — the tradition's own words 'his vows STAND' (30:5 'then all her vows shall stand'), the vow leaning on a vowed thing (Nedarim 14a:5), the two transgressions on the unpaid vow — 'he shall not profane' and 'you shall not delay' (Deut 23:22; Nedarim 3a:7); closed by the vow's payment (the offering brought, the abstention kept to its term) or by its ANNULMENT (vow_annulled) — the annulled entry closed_by the restraining verse; the man's, the widow's and the mature daughter's vows have no annuller",
  HE_BOUND + " (he shall not profane his word; according to all that proceeds out of his mouth he shall do — Num 30:3)",
  "Num 30:3 ('he shall not profane his word' one Bible seat in this sense; 'according to all that proceeds out of his mouth' one seat, its echoes 32:24 and Judg 11:36), 30:4-5 ('shall stand' — the stand-root twelve tokens in the chapter), 30:10 ('shall stand against her' — the widow's), 30:11-12 (the married woman's stand); Deut 23:22-24 (the delay ban; 'that which has gone out of your lips you shall keep and do' — a positive mitzva, a prohibition, the court's warrant: Rosh Hashanah 6a:5); Lev 27:2, Num 6:2 ('clearly utter' — the identity of the vow's age); Onkelos 30:3 ('he shall not VOID his word'); Sifrei Bamidbar 153:3-4; Babylonian Talmud Nedarim 2b:2, 3a:7, 13a:2-14a:5, 16b:3-4, 81b:5; Shevuot 20b:3, 21a:4; Rosh Hashanah 4a:13, 5b:2-5, 6a:12",
  CORPUS + "; num_06_nazir (the nazirite's vow the cousin, nazirite_vow_bound)",
  "cold_run_vows.py (F1 the_man; the state machine's vow_uttered); Mishnah Nedarim 1:1-2:5 (the substitutes, the support), 9:1-10 (the sage's release), 11:10 (the nine whose vows stand); Mishnah Niddah 5:6 (the ages); Rosh Hashanah 1:1 (the festivals' new year for the delay)"),
 ('vow_confirmed', 'status',
  "the vow confirmed — the STATUS the authority's silence or words write on the vower's vow at the hearing day's end: 'and her father hears her vow ... and her father is silent to her, THEN ALL HER VOWS SHALL STAND' (Num 30:5), 'he has confirmed them, because he was silent to her on the day of his hearing' (30:15), 'her husband shall confirm it' (30:14) — the tradition's קִיּוּם (confirmation): CONFIRMED FOR ONE HOUR, NEVER ANNULLED (Sifrei 153:5; Nedarim 69a:1-2, 79a:1 — silence confirms, silence does not annul; the heart confirms), the TIMER's fire at the hearing day + 1 (the calendar row vow_annulment_window: to nightfall, the pair's twenty-four hours recorded), or at once on the confirming words ('you did well' — Nedarim 77b:5); a confirmation may be dissolved by a sage, an annulment may not (Nedarim 69a:4, 79a:3)",
  HE_CONF + " (then all her vows shall stand — Num 30:5)",
  "Num 30:5, 30:8, 30:12 ('and is silent to her' — the silence-verb's single form at three seats), 30:14 ('her husband shall confirm it'), 30:15 ('silent, he is silent ... from day to day' — the doubled verb; 'he has confirmed them, because he was silent to her on the day of his hearing'); Onkelos 30:5-15 (the confirming by the stand-root — the oath's and the statutes' one root); Sifrei Bamidbar 153:5, 153:8, 154:2, 156:1; Babylonian Talmud Nedarim 69a:1-6, 70a:4, 76b:4-8, 77b:5, 79a:1-9; Shabbat 157a:11",
  CORPUS,
  "cold_run_vows.py (the state machine's vow_heard; F2 the_daughter, F3 the_betrothed, F5 the_wife, F6 the_affliction_oath); Mishnah Nedarim 10:1-8 (the day; the confirmation), 11:5-7"),
 ('vow_annulled', 'heaven',
  "the vow annulled — HEAVEN's entry the authority's restraint on the hearing day writes on the vower: 'and if her father restrain her on the day of his hearing, all her vows ... shall not stand, AND THE LORD WILL FORGIVE HER, because her father restrained her' (Num 30:6; 'and the LORD will forgive her' at 30:9 and 30:13 — the clause's three Bible seats all in this chapter) — the tradition's הֲפָרָה (annulment): RESTRAINT IS ANNULMENT (the pair at 30:9 — Sifrei 153:6, 153:9); the pending confirmation's timer cancelled and the vow_bound debit closed by the restraining verse; the forgiveness for the woman who broke the vow not knowing it was annulled (Sifrei 153:6; Kiddushin 81b:5; Nazir 23a:3); the annulment an ACT — the heart alone does not annul (Nedarim 79a:1; Beit Hillel otherwise, 77b:7); by the right authority alone (the father in her youth in his house; father and husband together over the betrothed; the husband over the married for affliction vows and vows between them — 30:14, 30:17); annulled for himself and for others (affliction) or for himself only (between them) — Nedarim 79b:5",
  HE_ANN + " (and the LORD will forgive her, because her father restrained her — Num 30:6)",
  "Num 30:6, 30:9, 30:13 ('and the LORD will forgive her' — three seats; the forgive-verb's fourth Bible token 2 Kgs 5:18), 30:9 ('he restrains her and annuls her vow' — the two verbs adjacent here alone), 30:13 ('annul, he annuls' — the form's two Bible seats 30:13 and 30:16), 30:14 ('her husband shall annul it'); Onkelos 30:6 ('from before the LORD it shall be forgiven her' — the passive behind the buffer; 'restrained' turned away, 'annul' void); Sifrei Bamidbar 153:6, 153:9-10, 154:3, 155:1, 156:3; Babylonian Talmud Nedarim 67a:5, 68a:1-2, 71b:1, 73a:4, 75a:6, 79a:1, 79b:2-5, 82a:1, 83a:1, 86b:5, 87a:3, 87b:1-2; Nazir 23a:3; Kiddushin 81b:5; Bava Metzia 96a:20",
  CORPUS,
  "cold_run_vows.py (the state machine's vow_restrained; F2, F3, F5, F6); Mishnah Nedarim 10:1-8, 11:1-12; Mishnah Shabbat 24:5 (the Sabbath's annulment); Mishnah Nazir 4:1 (the wife's 'and I')"),
 ('iniquity_borne', 'heaven',
  "her iniquity borne — HEAVEN's entry the annulment AFTER the confirmation writes on THE HUSBAND: 'and if he annul, he annuls them after his hearing, THEN HE SHALL BEAR HER INIQUITY' (Num 30:16) — 'after his hearing' = after his confirming (Sifrei 156:2, the phrase freed by 30:15's neighbor); 'he enters in her place for the sin' — the woman who broke the confirmed vow relying on his void annulment is clear, the iniquity his (Sifrei 156:2; Nedarim 79a:4-5; Mishnah Nedarim 10:7); the phrase's first seat the suspected wife's 'that woman shall bear her iniquity' (5:31 — the Naso runner's cell by CALL); Onkelos 'he shall receive her guilt' (the debt-word); the a-fortiori from the two measures (the measure of good five hundred times the measure of punishment — Sanhedrin 100a:18; Yoma 76a:7)",
  HE_INIQ + " (then he shall bear her iniquity — Num 30:16)",
  "Num 30:16 ('and if he annul, he annuls them after his hearing' — 'after his hearing' one seat; 'he shall bear her iniquity' one seat — 'her iniquity' five Torah seats: Lev 7:18, 18:25, Num 5:31, 15:31, 30:16), 5:31 ('that woman shall bear her iniquity' — the suspected wife's); Onkelos 30:16 ('and he shall receive her guilt'); Sifrei Bamidbar 156:2; Babylonian Talmud Nedarim 79a:4-5; Sanhedrin 100a:17-18; Yoma 76a:7; Sifrei Bamidbar 21:3 (5:31 at the sotah's seat)",
  CORPUS + "; num_05_sotah (the phrase's first seat, NS05B-11)",
  "cold_run_vows.py (the state machine's vow_restrained after the fire; F6 the_affliction_oath); Mishnah Nedarim 10:7 (the annulment after the day — the exam's 'after his hearing' rows); cold_run_naso.py sotah('husband_clean') by CALL"),
]
added = 0
for name, op, en, he, ink, corpus, exam in NEW:
    if name in fx: continue
    text = text.rstrip('\n') + '\n' + f"  {name}:\n    en: {q(en)}\n    he: {q(he)}\n    ledger_op: {op}   # THE NUMBERS WALK 10b (2026-09-12): the vows' state machine — {name}\n    ink: {q(ink)}\n    corpus: {q(corpus)}\n    exam: {q(exam)}\n"
    added += 1
open(path, 'w', encoding='utf-8').write(text)
fx = yaml.safe_load(open(path, encoding='utf-8'))['effects']
assert all(n in fx for n, *_ in NEW) and fx['vow_bound']['ledger_op'] == 'debit' and fx['vow_annulled']['ledger_op'] == 'heaven'
print('effects: %d added (registry %d); the he found in the verses: %s | %s | %s | %s' % (added, len(fx), HE_BOUND, HE_CONF, HE_ANN, HE_INIQ))
# ---- the daemon block + the functions block (daemon_dispositions.yaml) ----
path = f"{ROOT}/World/step9/daemon_dispositions.yaml"
text = open(path, encoding='utf-8').read()
if '  law_vows:' not in text:
    block = '''  law_vows:
    file: cold_run_vows.py
    wraps: vows
    given_at: Num 30:2
    installed_by: boot   # THE NUMBERS WALK 10b (2026-09-12): THE FORM FOR A LAW IN MOSES' VOICE — the chapter has NO divine frame ('and Moses spoke to the heads of the tribes ... this is the thing which the LORD commanded', 30:2; the book's other such chapter 36, whose relayed command IS a case-born output on the tent, command_relayed); Moses' relay to the heads of the tribes erects no institution (the installing acts are institution-erecting events on a `kind: institution` entity) and the chapter has no case — so the walk's standing setting for a statute spoken at its verse, with the CLASS named here: 'relayed in Moses' voice, no divine frame'; THE SECOND PASS (D2) decides whether a relayed statute needs the tent standing (COMPILE_DEBT.md's sitting-10b box)
    watches:
      vows_law_spoken: [commanded]                                                      # 30:2-17: the one line — the statutes commanded on israel_people; no timer, no close
      vow_uttered: [vow_bound, exempt]                                                   # THE STATE MACHINE (1): the vow's debit toward HEAVEN, or no vow (the minor; the void vow)
      vow_heard: [vow_confirmed, exempt]                                                 # THE STATE MACHINE (2): the TIMER vow_confirmed due the hearing day + 1 (the calendar row vow_annulment_window), or at once on the confirming words; the deaf hear nothing
      vow_restrained: [vow_annulled, iniquity_borne]                                     # THE STATE MACHINE (3): on the day by the right authority — the timer cancelled, the debit closed, HEAVEN forgives; after the fire — the husband bears her iniquity; the wrong authority writes nothing
      mans_vow_case: [vow_bound, accepted, commanded, exempt]                            # the exam's rows on 30:2-3
      daughters_vow_case: [vow_bound, vow_confirmed, vow_annulled, accepted, exempt]     # the exam's rows on 30:4-6
      betrothed_vow_case: [vow_bound, vow_confirmed, vow_annulled, accepted, exempt]     # the exam's rows on 30:7-9
      widows_vow_case: [vow_bound, accepted, exempt]                                     # the exam's rows on 30:10
      wifes_vow_case: [vow_bound, vow_confirmed, vow_annulled, accepted, exempt]         # the exam's rows on 30:11-13
      affliction_oath_case: [vow_bound, vow_confirmed, vow_annulled, iniquity_borne, accepted, exempt]   # the exam's rows on 30:14-16
      statutes_case: [accepted, commanded, exempt]                                       # the exam's rows on 30:17 and 30:1
'''
    i = text.index('  law_zelophehad:')
    text = text[:i] + block + text[i:]
if '\n  vows:   # THE NUMBERS WALK 10b' not in text:
    fb = '''  vows:   # THE NUMBERS WALK 10b (2026-09-12)
    the_man: {status: WRAPPED, by: law_vows}
    the_daughter: {status: WRAPPED, by: law_vows}
    the_betrothed: {status: WRAPPED, by: law_vows}
    the_widow: {status: WRAPPED, by: law_vows}
    the_wife: {status: WRAPPED, by: law_vows}
    the_affliction_oath: {status: WRAPPED, by: law_vows}
    the_statutes: {status: WRAPPED, by: law_vows}
'''
    i = text.index('  musafim:   # THE NUMBERS WALK 9b (2026-09-11)')
    j = text.index('\n  pre_sinai:', i)
    text = text[:j + 1] + fb + text[j + 1:]
open(path, 'w', encoding='utf-8').write(text)
dd = yaml.safe_load(open(path, encoding='utf-8'))
assert 'law_vows' in dd['daemons'] and 'vows' in dd['functions'], (list(dd)[:5])
print('daemons: %d (law_vows %s); functions blocks: %d' % (len(dd['daemons']), 'law_vows' in dd['daemons'], len(dd['functions'])))
# ---- the dependency span + edges (the POINTERS after the gate's print) ----
path = f"{ROOT}/World/step9/dependency_dispositions.yaml"
text = open(path, encoding='utf-8').read()
if '\n  vows:' not in text.split('\nedges:')[0]:
    a = "  musafim:     [[Num, 28, 1, 31], [Num, 29, 1, 39]]"
    i = text.index(a); j = text.index('\n', i)
    text = text[:j + 1] + "  vows:        [[Num, 30, 1, 17]]   # THE NUMBERS WALK 10b (2026-09-12; NUMBERS_WALK.md \"Sitting 10b\"): the vows — the man, the daughter, the betrothed, the widow, the married woman, the affliction oath, the statutes; 30:1 the calendar's receipt-closer read with it\n" + text[j + 1:]
    edges = '''  - {from: vows, to: naso, disposition: CALL, link: reference, carries: verdict,
     why: "THE NUMBERS WALK 10b (2026-09-12) | 30:3's 'a man, when he vows a vow' takes its AGE from the nazirite's 'when a man or woman shall clearly utter a vow' (6:2 — the Sifrei 153:3's identity, Niddah 46a:2) and 30:16's 'he shall bear her iniquity' is the suspected wife's phrase at its first seat (5:31 — the Sifrei 156:2): cold_run_naso.nazirite('vow_form') and sotah('husband_clean') CALLED — the shared tokens the reference"}
  - {from: vows, to: vayikra5, disposition: CALL, link: reference, carries: verdict,
     why: "THE NUMBERS WALK 10b (2026-09-12) | 30:7's 'the utterance of her lips' (the noun at 30:7 and 30:9 alone) is the oath of Leviticus 5:4 'to utter with the lips' (the Sifrei 153:7's identity; Shevuot 20a:4-9): cold_run_vayikra5.graded_offering(utterance_oath) CALLED — the option template 'to do evil or to do good' the affliction oath's own class (Shevuot 27a:6)"}
  - {from: vows, to: priesthood, disposition: CALL, link: reference, carries: verdict,
     why: "THE NUMBERS WALK 10b (2026-09-12) | 30:10's 'a widow or a divorced woman' and 30:4's 'in her youth' share the priest's daughter's words at Leviticus 22:13 ('a widow or divorced ... she returns to her father's house AS IN HER YOUTH' — the three Torah seats of the pair): cold_run_priesthood.holy_food('return') and holy_food('eating_table', after='fathers_house') CALLED — Yevamot 87a:6-7 reads the two verses against each other"}
  - {from: vows, to: musafim, disposition: CALL, link: reference, carries: value,
     why: "THE NUMBERS WALK 10b (2026-09-12) | 29:39 'besides your VOWS and your freewill offerings' names the vows at the calendar's close and the delay ban's clock ('you shall not delay', Deut 23:22 — Rosh Hashanah 4a:13-4b:10) sits in the musafim runner's DATA row vow_deadline: cold_run_musafim.the_calendar(vow_deadline) and DATA['vow_deadline'] READ by CALL — never re-declared (the 9b debt (iv) paid)"}
  - {from: vows, to: moadim, disposition: CALL, link: reference, carries: value,
     why: "THE NUMBERS WALK 10b (2026-09-12) | 30:14's 'to afflict a soul' shares the affliction-root with Leviticus 23:27's 'you shall afflict your souls' (the five afflictions — Yoma 76a:11; Rava's two senses of one root, Nedarim 80b:6): cold_run_moadim.yom_kippur()['affliction_list'] CALLED — the contrast's other seat"}
  - {from: sequence, to: vows, disposition: CALL, link: none,
     why: "THE NUMBERS WALK 10b (2026-09-12) | the sequential run's REGISTRATION edge — ('cold_run_vows', 'law_vows') in DAEMON_ORDER (the runner compiles no verse: link none, O4's license)"}
'''
    a = "  - {from: sequence, to: musafim, disposition: CALL, link: none,"
    i = text.index(a); j = text.index('\n', text.index('why:', i)) + 1
    text = text[:j] + edges + text[j:]
    open(path, 'w', encoding='utf-8').write(text)
dep = yaml.safe_load(open(path, encoding='utf-8'))
assert 'vows' in dep['spans']
print('dependency: span + 6 edges (vows); the pointers after the gate\'s print')
# ---- the installation probe's count ----
path = f"{ROOT}/World/step9/installation_probes.py"
text = open(path, encoding='utf-8').read()
a = "len(real) == 56 and all('given_at' in d and 'installed_by' in d for d in real.values())   # THE NUMBERS WALK 9b (2026-09-11): 55 -> 56, law_musafim;"
if a in text:
    text = text.replace(a, "len(real) == 57 and all('given_at' in d and 'installed_by' in d for d in real.values())   # THE NUMBERS WALK 10b (2026-09-12): 56 -> 57, law_vows (installed_by boot — the form for a law in Moses' voice, the class named); 9b: 55 -> 56, law_musafim;")
    open(path, 'w', encoding='utf-8').write(text)
assert "len(real) == 57" in open(path, encoding='utf-8').read()
print('installation_probes I5: 57')
# ---- THE CALENDAR ROW vow_annulment_window (the third registry; read by the runner as DATA) ----
path = f"{ROOT}/World/step9/calendar_parameters.yaml"
text = open(path, encoding='utf-8').read()
if '  vow_annulment_window:' not in text:
    row = '''  vow_annulment_window:
    value: to_nightfall
    channel: received
    source: "Num 30:6, 30:9, 30:13, 30:15 — 'on the day of his hearing' at four seats (all in this chapter) and 'from day to day' at 30:15 (two Bible seats, 1 Chr 16:23 the other): Mishnah Nedarim 10:8 (Nedarim 76b:2-3) — the annulment ALL THE DAY of the hearing, a leniency (vowed Friday night — annulled through the Sabbath till dark) and a stringency (vowed near dark — till dark only); the baraita at 76b:4 — the first tanna from 'on the day that he hears them' (30:13): till the day's end; R. Yosei b. R. Yehuda and R. Elazar b. R. Shimon: TWENTY-FOUR HOURS from the hearing, from 'from day to day' (76b:5); each arm reads both clauses (76b:6-7 — the night inside the day; not a week); Sifrei Bamidbar 156:1 — R. Shimon ben Yochai's twenty-four hours against the verse's own 'on the DAY of his hearing'; R. Yehoshua b. Levi: THE HALAKHA (the ruling) IS NOT AS THAT PAIR (76b:8; Rav's uncle R. Chiyya the same); Shabbat 157a:9-11 the same pair on the Sabbath's annulment"
    teacher: "Nedarim 76b:4-8; Sifrei Bamidbar 156:1; Mishnah Nedarim 10:8"
    settings: {to_nightfall: "the first tanna (the Mishnah's ruling): the hearing day ends at dark — the timer vow_confirmed due = the hearing day + 1 on the engine's EVENING boundary (the day_boundary row's 'until the evening' convention); a vow heard on Friday night is annullable through the Sabbath day", twenty_four_hours: "R. Yosei b. R. Yehuda and R. Elazar b. R. Shimon (the Sifrei's R. Shimon ben Yochai): from the hearing's hour to the same hour of the next day — at the DAY grain the fire would land inside the next day after its boundary (sub-day is out — the clock consensus); recorded, UNEXERCISED"}
    open: "THE NUMBERS WALK 10b (2026-09-12): the vows' state machine reads this row's value for its timer; the twenty-four-hour arm's day-grain rendering is named, never run; the day of LEARNING that annulment exists is a second hearing day (Mishnah Nedarim 11:7 — a DATA row of the runner, not this clock's)"
    exercised_by: [vows]
'''
    i = text.index('\neras:\n')
    text = text[:i] + '\n' + row.rstrip('\n') + text[i:]
    open(path, 'w', encoding='utf-8').write(text)
cal = yaml.safe_load(open(path, encoding='utf-8'))
assert cal['parameters']['vow_annulment_window']['value'] == 'to_nightfall' and 'twenty_four_hours' in cal['parameters']['vow_annulment_window']['settings']
print('calendar_parameters: vow_annulment_window (rows %d)' % len(cal['parameters']))
