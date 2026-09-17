import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE DEUTERONOMY WALK sitting 3b — THE COMPILE OF CHAPTER 5 (2026-09-16; World/step9/DEUTERONOMY_WALK.md "Sitting 3b"): THE TYPES FIRST — TWO
# tape kinds (the request for a mediator — the tape's second hole, Exodus 20:18-19 the first telling; the answer — stand here with me, told only here),
# ONE case kind (horeb_covenant_case), FOUR new effects (other_gods_barred and coveting_barred BLOCKS on Israel — the code's hole filled at the giving's
# line; torah_through_moses and returned_to_tents STATUSES on Israel), NO registry row (Israel and Moses the written-on parties, both standing), the
# 65th daemon's block (law_covenant_at_horeb, given_at Exod 20:3 — the second word's first giving, installed_by covenant_blood_thrown — law_decalogue's
# own installer), the functions block, the dependency span and the CALL edges (the token-demanded edges and the pointers after the gate's print),
# the obey_horeb → decalogue edge's why amended (the second word PAID), the installation probe's count 64 -> 65. The `he` is cut from the pointed DB
# text by FINDING the phrase's tokens (never a typed index); the witnesses the plain consonantal verses. Idempotent (add_types_ch4.py's form).
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
CORPUS = "deu_05_decalogue (STEP_Dt_5_1 through STEP_Dt_5_33; claims DV05-01 through DV05-06)"
SUB = "submitted by cold_run_covenant_at_horeb.py [subjects: %s] (the narrative scene, THE DEUTERONOMY WALK 3b); re-submitted on the sequential tape by cold_run_sequence.py; consumed by law_covenant_at_horeb (cold_run_covenant_at_horeb.py) -> %s"
CASE = "submitted by cold_run_covenant_at_horeb.py [subjects: the exam's persons] (the wrap's scene); consumed by law_covenant_at_horeb (cold_run_covenant_at_horeb.py) -> %s"
INK = "Deut 5:1-33; Exodus 20:2-17 (the first copy, diffed token by token at the reading); Onkelos Deut 5:1-33 (the export's thirty verses mapped to the DB's thirty-three; 'speech with speech' at 5:4, the Memra at 5:5, 'except me' at 5:7, 'did not cease' at 5:22, 'accept and do' at 5:27); the Sifrei on Deuteronomy's six rows citing the chapter (20:1, 41:1, 41:4, 233:1, 306:16, 357:40 — NO piska on the chapter); the reading ledger deu_05_vaetchanan_2026-09-16.md (38 sources, 6 claims); the exam docket deu_05_vaetchanan_exam_2026-09-16.md (275 rows: LAW 77 / DERIVATION 19 / DISPUTE 14 / CONTEXT 165)"
D, X = 'Deut', 'Exod'
KINDS = [
 ("mediator_requested", "speech",
  "the request for a mediator — 'and it came to pass, when you heard the voice out of the midst of the darkness, while the mountain burned with fire, that you came near to me, all the heads of your tribes and your elders, and you said: behold, the LORD our God has shown us his glory and his greatness, and his voice we have heard out of the midst of the fire; this day we have seen that God speaks with man and he lives; now therefore why should we die? for this great fire will consume us; if we hear the voice of the LORD our God any more, we shall die; for who is there of all flesh that has heard the voice of the living God speaking out of the midst of the fire, as we have, and lived? GO YOU NEAR AND HEAR all that the LORD our God shall say, and YOU SPEAK TO US all that the LORD our God speaks to you, AND WE WILL HEAR AND DO' (Deut 5:23-27) — Exodus 20:18-19's 'and all the people saw the thunders … and they stood afar off, and said to Moses: speak you with us and we will hear, but let not God speak with us lest we die' THE FIRST TELLING, absent from the tape (Exodus 20:18 sits in no runner's span; 20:19-21 are the ordinances' law cells; the tape runs from Exod 19:20 to 24:1 — THE TAPE'S SECOND HOLE, the laws' readback's finding): A SUPPLIED ACT written ONCE at its own time, DATED (1, 3, 7) by the RETROGRADE marker at Deut 5:23 (the giving's day — the request came when they heard the voice; Rabbi Yose's seventh of Sivan, the tape's own marker at Exod 19:16); torah_through_moses on Israel (a STATUS: the rest of the code through the mediator — Makkot 24a's two words from the Almighty's mouth); 'we will hear and do' against 24:7's 'we will do and hear' the TURNED row (Shabbat 88a)",
  HE(D, 5, 23, 27, "and it came to pass, when you heard the voice out of the midst of the darkness, while the mountain burned with fire, that you came near to me"), WIT(D, 5, 23, 27) + WIT(X, 20, 18, 19), INK, CORPUS,
  SUB % ("israel", "torah_through_moses on israel_people (a STATUS dated (1, 3, 7) — the mediator asked for at Horeb; the first telling Exod 20:18-19 named in the row)"), ["first_telling", "dated", "request"]),
 ("stand_here_commanded", "speech",
  "stand here with me — 'and the LORD heard the voice of your words when you spoke to me; and the LORD said to me: I have heard the voice of the words of this people which they have spoken to you; THEY HAVE DONE WELL in all that they have spoken; who would give that they had such a heart as this always, to fear me and keep all my commandments, that it might be well with them and with their children forever; go say to them: RETURN TO YOUR TENTS; but as for you, STAND HERE WITH ME, and I will speak to you all the commandment and the statutes and the judgments which you shall teach them, that they may do them in the land which I give them to possess' (Deut 5:28-31) — TOLD ONLY IN THE RETELLING (Exodus 20:22's answer another speech; Deuteronomy 18:16-17 cites this one forward: 'according to all that you desired of the LORD your God in Horeb on the day of the assembly … they have well said'): A SUPPLIED ACT written ONCE at its own time, DATED (1, 3, 7) inside the retrograde stretch of Deut 5:23's marker; TWO writes — THE CHARGE TO TEACH a DEBIT on Moses (commanded, valued teach_the_commandment — Exodus 24:12's 'to teach them' and 4:14's 'commanded me at that time to teach you') CLOSED AT ONCE BY THE PRIOR RUN (the closer the tape's EARLIER line, speech_opened at Deut 1:1-5 — 'Moses undertook to expound this Torah'; 4:5's receipt the same run: the book itself the charge's run), and RETURN TO YOUR TENTS a STATUS on Israel (returned_to_tents — the separation of Exodus 19:15 released: Beitzah 5a-b, Shabbat 87a, Yevamot 62a); 'stand here with me' the Torah received standing (Megillah 21a; the Sifrei 357:40)",
  HE(D, 5, 28, 31, "and the LORD heard the voice of your words when you spoke to me"), WIT(D, 5, 28, 31) + WIT(D, 18, 16, 17), INK, CORPUS,
  SUB % ("moses", "commanded on moses valued teach_the_commandment (a DEBIT written and CLOSED inside the daemon — the close by the prior run, Deut 1:5), returned_to_tents on israel_people (a STATUS dated (1, 3, 7))"), ["first_telling", "dated", "answer"]),
 ("horeb_covenant_case", "case", "the exam's rows on chapter 5 (Deut 5:1-33 — the second word: Mishnah Sanhedrin 7:6, Sanhedrin 60b; the tenth word: Bava Metzia 5b; the vain oath: Mishnah Shevuot 3:8-9; keep and remember in one utterance: Shevuot 20b, Rosh Hashanah 27a, Berakhot 20b; the ox and the ass, the servants' rest: Bava Kamma 54b, Yevamot 48b; the reward clause: Bava Kamma 55a, Kiddushin 39b-40a, Chullin 142a; the honor's measures: Kiddushin 30b-31b; the theft of persons: Sanhedrin 86a; 'we will do' before 'we will hear': Shabbat 88a; the first two words from the Almighty's mouth: Makkot 24a; return to your tents: Beitzah 5a-b; the receipts at Marah: Sanhedrin 56b, Shabbat 87b; the day: Yoma 4b; the covenants counted: Sotah 37b) — the exam's persons through the cells' asks: the bower, the embracer, the server in its way, the one who says 'you are my god', the coveter who pays, the woman at kiddush, the laden beast's driver, the circumcised slave at rest, the son who feeds pheasant, the father who abducts his son, the one who put 'we will do' first, the men returned to their tents",
  PHRASE(D, 5, 7, ['לא', 'יהיה', 'לך', 'אלהים', 'אחרים']) + " (you shall have no other gods — Deut 5:7)", WIT(D, 5, 6, 21) + WIT(D, 5, 23, 31), INK, CORPUS, CASE % "put_to_death / exempt / accepted (the exam's persons — stoned by the second word's answer sheet; outside the rule; the rule holds against him)", ["person", "ask"]),
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
# ---- FOUR new effects, the ink's own words, the `he` FOUND in the verse ----
path = f"{ROOT}/World/step9/effect_vocabulary.yaml"
text = open(path, encoding='utf-8').read()
fx = yaml.safe_load(text)['effects']
for e in ('commanded', 'put_to_death', 'exempt', 'accepted', 'covenant_declared', 'tablets_delivered', 'torah_expounded', 'sanctified_for_the_third_day', 'lashes', 'labor_barred', 'sanctify_day'):
    assert e in fx, e
HE_GODS = PHRASE(D, 5, 7, ['לא', 'יהיה', 'לך', 'אלהים', 'אחרים', 'על', 'פני'])
HE_COVET = PHRASE(D, 5, 21, ['ולא', 'תחמד', 'אשת', 'רעך'])
HE_HEAR = PHRASE(D, 5, 27, ['ואת', 'תדבר', 'אלינו', 'את', 'כל', 'אשר', 'ידבר', 'יהוה', 'אלהינו', 'אליך', 'ושמענו', 'ועשינו'])
HE_TENTS = PHRASE(D, 5, 30, ['לך', 'אמר', 'להם', 'שובו', 'לכם', 'לאהליכם'])
NEW = [
 ('other_gods_barred', 'block',
  "other gods barred — the BLOCK the second word writes on Israel: 'you shall have no other gods before me; you shall not make for yourself a graven image, any form of what is in the heavens above or on the earth beneath or in the waters under the earth; you shall not bow down to them nor serve them, for I the LORD your God am a jealous God, visiting the iniquity of the fathers upon the sons to the third and the fourth generation of those who hate me, and doing mercy to thousands of those who love me and keep my commandments' (Deut 5:7-10; Exodus 20:3-6 the first copy — 5:8 'any form' for 'and any form', 5:9 'fathers' plene and 'and upon the third', 5:10 the written 'his' for 'my', computed at the reading) — THE CODE'S HOLE FILLED FROM THE RETELLING'S SEAT (no runner compiled the second word until THE DEUTERONOMY WALK 3b): the block written at the giving's own line (ten_words_declared, dated (1, 3, 7)), never at the retelling's; the answer sheet Mishnah Sanhedrin 7:6 with Sanhedrin 60b — the idolater STONED for worship in its way, for slaughter, incense, libation and BOWING even not in its way (the Temple's rites emptied to the Name, Exodus 22:19; bowing's death by the juxtaposition of Deuteronomy 17:3 to 17:5, its prohibition from 34:14), the hugger and kisser a prohibition without death; the visiting's arms (Berakhot 7a — when they hold their fathers' deeds; Makkot 24a:30 — revoked by Ezekiel 18:4) DATA; the images for study (Rosh Hashanah 24a-24b) and the no-image list of 4:16-19 (the obey_horeb runner's DATA row) the parameter table",
  HE_GODS + " (you shall have no other gods before me — Deut 5:7)",
  "Deut 5:7-10 ('you shall have no other gods before me … you shall not bow down to them nor serve them … a jealous God'), Exodus 20:3-6 (the first copy), 4:15-19 (the no-image list), 4:24 ('a jealous God'), 6:14-15, 17:2-7 (the sanction's procedure, forward), 34:14 (Exodus — 'you shall bow to no other god'), 22:19 (Exodus — 'he who sacrifices to the gods shall be devoted'); Onkelos 5:7 ('except me'); Mishnah Sanhedrin 7:6; Babylonian Talmud Sanhedrin 60b:1-19, Makkot 24a:1, 24a:30, Berakhot 7a:27, Kiddushin 31a:6-7; Mishnah Avodah Zarah 3:1-3, Rosh Hashanah 24a-24b (2b's docket)",
  "deu_05_decalogue (STEP_Dt_5_7 through STEP_Dt_5_10; the claim DV05-02)",
  "cold_run_covenant_at_horeb.py (F2 the_second_word — no_other_gods, no_image, bow_and_serve, the_visiting, the_ketiv, the_write; the exam kind horeb_covenant_case; the block written on the tape kind ten_words_declared)"),
 ('coveting_barred', 'block',
  "coveting barred — the BLOCK the tenth word writes on Israel: 'and you shall not covet your neighbor's wife; and you shall not desire your neighbor's house, his field, or his servant or his maidservant, his ox or his ass, or anything that is your neighbor's' (Deut 5:21; Exodus 20:17 the first copy — 'you shall not covet your neighbor's house; you shall not covet your neighbor's wife …': the house first there, the wife first here, DESIRE for the second covet, 'his field' added — computed at the reading) — THE CODE'S HOLE FILLED FROM THE RETELLING'S SEAT (no runner compiled the tenth word until THE DEUTERONOMY WALK 3b): the block written at the giving's own line (ten_words_declared, dated (1, 3, 7)); the answer sheet Bava Metzia 5b:19-20 — Rav Acha of Difti: taking by force or deceit violates 'you shall not covet' EVEN WITH PAYMENT; most people read it as taking without payment, so the bailee who pays is not disqualified as a robber; the two verbs (covet in deed, desire in the heart — the Mekhilta's distinction, the first copy's spine, credited by name) DATA",
  HE_COVET + " (and you shall not covet your neighbor's wife — Deut 5:21)",
  "Deut 5:21 ('and you shall not covet … and you shall not desire'), Exodus 20:17 (the first copy — 'you shall not covet' twice), 7:25 ('you shall not covet the silver and gold on them'); Onkelos 5:21; Babylonian Talmud Bava Metzia 5b:18-20; the Mekhilta d'Rabbi Yishmael Bahodesh 8 (named, unopened)",
  "deu_05_decalogue (STEP_Dt_5_21; the claim DV05-04)",
  "cold_run_covenant_at_horeb.py (F5 the_tenth_word — covet_and_desire, the_wife_first, the_coveter_who_pays, the_write; the exam kind horeb_covenant_case; the block written on the tape kind ten_words_declared)"),
 ('torah_through_moses', 'status',
  "the Torah through Moses — the STATUS the request for a mediator writes on Israel: 'go you near and hear all that the LORD our God shall say, and you speak to us all that the LORD our God speaks to you, and we will hear and do' (Deut 5:27; 5:5 'I stood between the LORD and you at that time to declare to you the word of the LORD'; 5:31 'stand here with me and I will speak to you all the commandment … which you shall teach them'); Exodus 20:19's 'speak you with us and we will hear, but let not God speak with us lest we die' THE FIRST TELLING (no line on the tape — the second hole); the tradition's own reading: 'I am' and 'you shall have no other gods' heard from the Almighty's mouth, the rest through Moses (Makkot 24a:1 — 611 and 2 = 613); 'Moses received the Torah from Sinai and handed it on' (Mishnah Avot 1:1 — the vocabulary); dated (1, 3, 7) by the retrograde marker at Deut 5:23",
  HE_HEAR + " (and you speak to us all that the LORD our God speaks to you, and we will hear and do — Deut 5:27)",
  "Deut 5:23-27 (the request), 5:5 (the mediator), 5:31 (the charge), 18:16-17 (the citation forward); Exodus 20:18-21 (the first telling), 24:3, 24:7 ('we will do and hear' — the order turned at 5:27), 19:8; Onkelos 5:27 ('accept and do'); Babylonian Talmud Makkot 24a:1, Shabbat 88a:5-9, Yoma 4b:7-8; Mishnah Avot 1:1",
  "deu_05_decalogue (STEP_Dt_5_23 through STEP_Dt_5_27; the claim DV05-05)",
  "cold_run_covenant_at_horeb.py (F6 the_voice_and_the_request — you_came_near, the_request, hear_and_do, the_write; the tape kind mediator_requested, SUPPLIED, dated by the retrograde marker at Deut 5:23)"),
 ('returned_to_tents', 'status',
  "returned to your tents — the STATUS the answer writes on Israel: 'go say to them: return to your tents' (Deut 5:30) — the separation of Exodus 19:15 ('be ready for the third day; do not come near a woman') RELEASED by an explicit word: Rav Yosef — a matter forbidden by a count needs a count to permit (Beitzah 5a:7-5b:3); 'his tent' is his wife (Moed Katan 7b:5, 15b:13); procreation repeated at Sinai (Sanhedrin 59b:3-4); Moses' own separation agreed by 'and you, stand here with me' (Shabbat 87a:4; Yevamot 62a:2); told only in the retelling, dated (1, 3, 7) inside Deut 5:23's stretch",
  HE_TENTS + " (go say to them: return to your tents — Deut 5:30)",
  "Deut 5:30 ('go say to them: return to your tents'), 5:31 ('and you, stand here with me'); Exodus 19:15 ('do not come near a woman' — the separation), 19:10-11 (the timer sanctified_for_the_third_day on the tape); Babylonian Talmud Beitzah 5a:7, 5b:3, Shabbat 87a:4, Yevamot 62a:2, Moed Katan 7b:5, 15b:13, Sanhedrin 59b:3-4, Avodah Zarah 5a:7",
  "deu_05_decalogue (STEP_Dt_5_28 through STEP_Dt_5_31; the claim DV05-06)",
  "cold_run_covenant_at_horeb.py (F7 the_answer_and_the_charge — return_to_your_tents, stand_here_with_me; the tape kind stand_here_commanded, SUPPLIED, dated inside the retrograde stretch of Deut 5:23)"),
]
added = 0
for name, op, en, he, ink, corpus, exam in NEW:
    if name in fx: continue
    text = text.rstrip('\n') + '\n' + f"  {name}:\n    en: {q(en)}\n    he: {q(he)}\n    ledger_op: {op}   # THE DEUTERONOMY WALK 3b (2026-09-16): chapter 5's compile — {name}\n    ink: {q(ink)}\n    corpus: {q(corpus)}\n    exam: {q(exam)}\n"
    added += 1
open(path, 'w', encoding='utf-8').write(text)
fx = yaml.safe_load(open(path, encoding='utf-8'))['effects']
assert all(n in fx for n, *_ in NEW) and fx['other_gods_barred']['ledger_op'] == 'block' and fx['coveting_barred']['ledger_op'] == 'block' and fx['torah_through_moses']['ledger_op'] == 'status' and fx['returned_to_tents']['ledger_op'] == 'status'
print('effects: %d added (registry %d); the he found in the verses: %s | %s | %s | %s' % (added, len(fx), HE_GODS, HE_COVET, HE_HEAR, HE_TENTS))
# ---- NO registry row (Israel and Moses the written-on parties, both standing) ----
reg = yaml.safe_load(open(f"{ROOT}/logic/corpus/entity_registry.yaml", encoding='utf-8'))
ids = {e['id'] for e in reg['entities']}
assert 'israel_people' in ids and 'moses' in ids, 'the written-on parties must stand'
print('entities: none added (registry %d)' % len(reg['entities']))
# ---- the daemon block + the functions block (daemon_dispositions.yaml) ----
path = f"{ROOT}/World/step9/daemon_dispositions.yaml"
text = open(path, encoding='utf-8').read()
if '  law_covenant_at_horeb:' not in text:
    block = '''  law_covenant_at_horeb:
    file: cold_run_covenant_at_horeb.py
    wraps: covenant_at_horeb
    given_at: Exod 20:3
    installed_by: covenant_blood_thrown   # THE DEUTERONOMY WALK 3b (2026-09-16): THE SECOND WORD'S FIRST GIVING (Exodus 20:3) — its code compiled from the second copy (Deut 5:7-10) with the first, and the tenth word's (5:21 with 20:17): THE CODE'S HOLE FILLED FROM THE RETELLING'S SEAT; installed by the covenant's blood like law_decalogue (Exod 24:8; the D2 candidate ten_words_declared standing filed); the blocks written at the giving's own line
    watches:
      ten_words_declared: [other_gods_barred, coveting_barred]   # Deut 4:10-13 (2b's supplied line, dated (1, 3, 7)): the second and the tenth words' BLOCKS on Israel — the code's hole filled at the code's own line (THE REST's one declared delta)
      mediator_requested: [torah_through_moses]                  # Deut 5:23-27 (Exod 20:18-19 the first telling — the tape's second hole): SUPPLIED, dated (1, 3, 7) by the retrograde marker at 5:23 — a STATUS on Israel
      stand_here_commanded: [commanded, returned_to_tents]       # Deut 5:28-31 (told only here; 18:16-17 forward): SUPPLIED, dated (1, 3, 7) — the charge to teach a DEBIT on Moses CLOSED AT ONCE BY THE PRIOR RUN (Deut 1:5); return to your tents a STATUS on Israel
      horeb_covenant_case: [put_to_death, exempt, accepted]      # the exam's rows on the chapter — the persons through the cells' asks (the second word's stoning by 17:5's reference; the embracer exempt; the rule holds)
'''
    i = text.index('  law_census:')
    text = text[:i] + block + text[i:]
if '\n  covenant_at_horeb:   # THE DEUTERONOMY WALK 3b' not in text:
    fb = '''  covenant_at_horeb:   # THE DEUTERONOMY WALK 3b (2026-09-16)
    the_assembly_called: {status: WRAPPED, by: law_covenant_at_horeb}
    the_second_word: {status: WRAPPED, by: law_covenant_at_horeb}
    the_first_tablet: {status: WRAPPED, by: law_covenant_at_horeb}
    the_second_tablet: {status: WRAPPED, by: law_covenant_at_horeb}
    the_tenth_word: {status: WRAPPED, by: law_covenant_at_horeb}
    the_voice_and_the_request: {status: WRAPPED, by: law_covenant_at_horeb}
    the_answer_and_the_charge: {status: WRAPPED, by: law_covenant_at_horeb}
'''
    i = text.index('  obey_horeb:   # THE DEUTERONOMY WALK 2b')
    j = text.index('\n  pre_sinai:', i)
    text = text[:j + 1] + fb + text[j + 1:]
open(path, 'w', encoding='utf-8').write(text)
dd = yaml.safe_load(open(path, encoding='utf-8'))
assert 'law_covenant_at_horeb' in dd['daemons'] and 'covenant_at_horeb' in dd['functions'], (list(dd)[:5])
print('daemons: %d (law_covenant_at_horeb %s); functions blocks: %d' % (len(dd['daemons']), 'law_covenant_at_horeb' in dd['daemons'], len(dd['functions'])))
# ---- the dependency span + the CALL edges (the token-demanded edges and the POINTERS after the gate's print); the 2b OWED why amended ----
path = f"{ROOT}/World/step9/dependency_dispositions.yaml"
text = open(path, encoding='utf-8').read()
if '\n  covenant_at_horeb:' not in text.split('\nedges:')[0]:
    a = "  obey_horeb: [[Deut, 4, 1, 49]]"
    i = text.index(a); j = text.index('\n', i)
    text = text[:j + 1] + "  covenant_at_horeb: [[Deut, 5, 1, 33]]   # THE DEUTERONOMY WALK 3b (2026-09-16; DEUTERONOMY_WALK.md \"Sitting 3b\"): chapter 5 — the covenant at Horeb retold, THE SECOND COPY OF THE TEN WORDS (the laws' readback, code against code; the second and the tenth words compiled here), the voice and the tablets FOUND, the request for a mediator and the answer (the tape's second hole — two supplied lines)\n" + text[j + 1:]
    W = "THE DEUTERONOMY WALK 3b (2026-09-16) | "
    edges = f'''  - {{from: covenant_at_horeb, to: decalogue, disposition: CALL, link: reference, carries: verdict,
     why: "{W}THE LAWS' READBACK — the second copy's words graded against the decalogue runner's cells: 5:11's vain name (DC.vain_name('vain_oath', 'false_future_oath', 'vain_and_false_utterance') CALLED — the last the one-utterance teaching the 5:12 row reads), 5:12-15's Sabbath (DC.sabbath_clauses('remember', 'labor_scope', 'causing', 'laden_beast') CALLED), 5:19's theft of persons (DC.theft_commandment('kidnapper', 'money_theft_here') CALLED — Sanhedrin 86a:15-16 the cell's own move); the second and the tenth words have NO cell there: compiled in THIS runner (F2, F5), their blocks written at the giving's line"}}
  - {{from: covenant_at_horeb, to: obey_horeb, disposition: CALL, link: reference, carries: verdict,
     why: "{W}5:22's 'these words the LORD spoke … and he wrote them on two tablets of stone and gave them to me' are 2b's SUPPLIED lines ten_words_declared and tablets_given READ BACK — FOUND on the tape, no second write (OH.horeb_retold('the_voice_and_no_form', 'the_ten_words_and_the_tablets') CALLED; OH.READBACK the second chapter's eleven rows the laws' rows join); 5:8's 'any form' the no-image list's head (OH.DATA the_no_image_list CALLED — the second word's parameter table, 4:16-19); the giving's line the seat of this runner's two blocks"}}
  - {{from: covenant_at_horeb, to: erection, disposition: CALL, link: reference, carries: verdict,
     why: "{W}5:2-3's 'the LORD our God made a covenant with us in Horeb' is the covenant's book and blood (ER.blood_covenant('book_of_covenant') CALLED — Exodus 24:3-8); 5:4's 'face in face' Onkelos renders 'speech with speech' as at Exodus 33:11 (ER.presence('speech_with_speech') CALLED); 5:22's 'two tablets of stone' the ten words' seats (ER.tablets('ten_words') CALLED); 5:31's 'which you shall teach them' Exodus 24:12's 'to teach them' (ER.ascent('torah_mitzvah') CALLED — the charge's debit)"}}
  - {{from: covenant_at_horeb, to: exodus_story, disposition: CALL, link: reference, carries: verdict,
     why: "{W}5:23's 'when you heard the voice' dates the request at the giving's day — Rabbi Yose's seventh (ES.sinai('days_r_yose') CALLED; the retrograde marker at 5:23); 5:27's 'we will hear and do' against 24:7's 'we will do and hear' (ES.sinai('we_will_do_seats') CALLED — the TURNED row; Shabbat 88a:7); the mountain overturned like a tub (ES.sinai('tub') CALLED — Shabbat 88a:5); 5:12 and 5:16's receipt read as Marah by the teacher (ES.marah('statute_list') CALLED — Sanhedrin 56b:16: the Sabbath and honoring parents among Marah's statutes)"}}
  - {{from: covenant_at_horeb, to: opening_speech, disposition: CALL, link: reference, carries: verdict,
     why: "{W}5:23's 'you came near to me, all the heads of your tribes and your elders' is 1:22's phrase at its second seat (OS.the_spies_read_back('the_asking') CALLED — the mob and the elders); 5:28's 'the LORD heard the voice of your words' is 1:34's (OS.the_spies_read_back('the_oath') CALLED); the charge's debit CLOSED BY THE PRIOR RUN — speech_opened at 1:1-5 the closer (OS.the_frame('the_write') CALLED — torah_expounded); OS.READBACK the first form's forty-two rows; the _closed_by_prior_run form reused"}}
  - {{from: covenant_at_horeb, to: holiness, disposition: CALL, link: reference, carries: verdict,
     why: "{W}5:16's 'honor your father and your mother' has NO cell at the Decalogue's seat — the fifth word compiled at its kin's, Leviticus 19:3's 'a man shall fear his mother and his father' (HO.frame('honor_defined', 'fear_defined', 'parents_order', 'three_partners', 'woman_included') CALLED — Kiddushin 30b-31b's measures: what is fear, what is honor, the three equations, the order, the woman): the readback row 5:16 EXPANDED names it"}}
  - {{from: covenant_at_horeb, to: mishpatim_3, disposition: CALL, link: reference, carries: verdict,
     why: "{W}5:17's 'you shall not murder' has its code at Exodus 21:12-14 (M3.killer('mode') CALLED — the killer's cells; the readback row 5:17 VERBATIM); 5:16's parents at their sanctions' seats — the striker (21:15) and the curser (21:17) (M3.parent_striker('mode'), M3.parent_curser('the_woman') CALLED; Kiddushin 30b:20's equation of cursing)"}}
  - {{from: covenant_at_horeb, to: sanctions, disposition: CALL, link: reference, carries: verdict,
     why: "{W}5:18's 'you shall not commit adultery' has its code at Leviticus 20:10 (SA.adultery('mode', 'both') CALLED — the readback row 5:18 VARIANT); 5:16's curser at Leviticus 20:9 (SA.curser('mode') CALLED)"}}
  - {{from: covenant_at_horeb, to: refuge, disposition: CALL, link: reference, carries: verdict,
     why: "{W}5:17's 'you shall not murder' — the murderer's definition at Numbers 35 (RF.the_murderer('he_is_a_murderer') CALLED — the sixth word's kin cell; the murder-verb the refuge runner's own census)"}}
  - {{from: covenant_at_horeb, to: ordinances, disposition: CALL, link: reference, carries: verdict,
     why: "{W}5:20's 'a VAIN witness' (20:16's 'false') has NO cell at the Decalogue's seat — the ninth word's kin at Exodus 23:1's 'you shall not take up a false report … a witness of violence' (OR.courts('false_report', 'witness_of_violence') CALLED; Deuteronomy 19:16-21 forward); the second word's sanction source 'he who sacrifices to the gods shall be devoted' (22:19 — Sanhedrin 60b:8, the ordinances' capital clause by REFERENCE)"}}
  - {{from: covenant_at_horeb, to: pre_sinai, disposition: CALL, link: reference, carries: verdict,
     why: "{W}5:15's ground — the exodus for the creation: the first copy's creation ground at 20:11 is the pre-Sinai runner's (PS.sabbath('delta_20_11') CALLED — the fourth word's two grounds a DATA row); 5:30's 'return to your tents' repeats procreation at Sinai (PS.noahide('repeated_at_sinai', 'procreation_israel') CALLED — Sanhedrin 59b:3-4)"}}
  - {{from: sequence, to: covenant_at_horeb, disposition: CALL, link: none,
     why: "{W}the sequential run's REGISTRATION edge — ('cold_run_covenant_at_horeb', 'law_covenant_at_horeb') in DAEMON_ORDER (the runner compiles no verse: link none, O4's license); the two tape lines and the two markers (Deut 5:23 retrograde, 5:32 forward) this sitting's; the daemon's two blocks written on 2b's giving line"}}
'''
    a = "  - {from: sequence, to: obey_horeb, disposition: CALL, link: none,"
    i = text.index(a); j = text.index('\n', text.index('why:', i)) + 1
    text = text[:j] + edges + text[j:]
    OLD_OWED = "no cell for the image law: OWED to chapter 5's sitting (COMPILE_DEBT); 4:24's 'jealous God' 20:5's by REFERENCE"
    assert text.count(OLD_OWED) == 1, text.count(OLD_OWED)
    text = text.replace(OLD_OWED, "no cell for the image law: OWED to chapter 5's sitting (COMPILE_DEBT) — PAID at THE DEUTERONOMY WALK 3b (2026-09-16): cold_run_covenant_at_horeb.py F2 the_second_word compiles the second word from both copies, its block other_gods_barred written at this runner's giving line; 4:24's 'jealous God' 20:5's by REFERENCE")
    open(path, 'w', encoding='utf-8').write(text)
dep = yaml.safe_load(open(path, encoding='utf-8'))
n_ch = sum(1 for e in dep['edges'] if e['from'] == 'covenant_at_horeb')
assert 'covenant_at_horeb' in dep['spans'] and n_ch == 11, n_ch
assert any('PAID at THE DEUTERONOMY WALK 3b' in str(e.get('why', '')) for e in dep['edges'] if e['from'] == 'obey_horeb' and e['to'] == 'decalogue')
print('dependency: span + 12 edges (covenant_at_horeb 11 CALL and the registration); the 2b OWED why amended PAID; the token-demanded edges and the pointers after the gate\'s print')
# ---- the installation probe's count ----
path = f"{ROOT}/World/step9/installation_probes.py"
text = open(path, encoding='utf-8').read()
if "len(real) == 64 and all(" in text:
    text = text.replace("len(real) == 64 and all('given_at' in d and 'installed_by' in d for d in real.values())   # THE DEUTERONOMY WALK 2b (2026-09-16): 63 -> 64, law_obey_horeb",
                        "len(real) == 65 and all('given_at' in d and 'installed_by' in d for d in real.values())   # THE DEUTERONOMY WALK 3b (2026-09-16): 64 -> 65, law_covenant_at_horeb (given_at Exod 20:3 — the second word's first giving, compiled from its second copy; installed_by covenant_blood_thrown); 2b: 63 -> 64, law_obey_horeb")
    open(path, 'w', encoding='utf-8').write(text)
assert "len(real) == 65" in open(path, encoding='utf-8').read()
print('installation_probes I5: 65')
