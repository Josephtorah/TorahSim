#!/usr/bin/env python3
# THE NUMBERS WALK sitting 13b — THE COMPILE OF THE JOURNEYS (2026-09-12; World/step9/NUMBERS_WALK.md "Sitting 13b"): THE TYPES FIRST — THREE
# tape kinds (the writing 33:1-2, the departure with the judgments on the gods 33:3-4, the command 33:50-56), TWO case-form kinds for the exam's
# scene, TWO new effects (journeys_recorded, judgments_executed_on_their_gods — status, the ink's own words at 33:2 and 33:4), NO registry row
# (the chapter writes on moses, israel_people and egypt_people, all standing; the inhabitants of the land a counterparty), the 60th daemon's block
# (law_journeys, given_at Num 33:50, installed_by BOOT with the class named — a law in the divine voice spoken in the plains of Moab), the
# functions block, the dependency span and edges (the pointers after the gate's print), the installation probe's count. The `he` is cut from the
# pointed DB text by FINDING the phrase's tokens (never a typed index); the witnesses the plain consonantal verses. Idempotent (add_types_gad.py's form).
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
    assert len(hits) == 1, (ch, vs, toks, hits, plain)
    return PV('Num', ch, vs, hits[0] + 1, hits[0] + n)
q = lambda s: '"' + s.replace('\\', '\\\\').replace('"', '\\"') + '"'
N = 'Num'
def HE(ch, lo, hi, en, cap=6):
    vv = list(range(lo, min(hi, lo + cap - 1) + 1))
    s = ' · '.join(PV(N, ch, v) + ' (%s — Num %d:%d)' % (en if v == lo else 'the verse continues', ch, v) for v in vv)
    return s + (' · … (through Num %d:%d)' % (ch, hi) if hi > vv[-1] else '')
def WIT(ch, lo, hi):
    return ['Num %d:%d | %s' % (ch, v, LV(N, ch, v)) for v in range(lo, hi + 1)]
CORPUS = "num_33_journeys (STEP_Nm_33_1 through STEP_Nm_33_56; claims MS33A-01 through MS33A-12)"
SUB = "submitted by cold_run_journeys.py [subjects: %s] (the narrative scene, THE NUMBERS WALK 13b); re-submitted on the sequential tape by cold_run_sequence.py; consumed by law_journeys (cold_run_journeys.py) -> %s"
CASE = "submitted by cold_run_journeys.py [subjects: the exam's persons] (the wrap's scene); consumed by law_journeys (cold_run_journeys.py) -> %s"
INK_ALL = "Num 33:1-56; Onkelos Num 33:1-56 (by the WORD of the LORD at 33:2 and 33:38; with bared head at 33:3; on their idols at 33:4; the graves of those who demanded at 33:16-17; Rekem for Kadesh at 33:36-37; the plain of Shittim; bands taking up arms and camps surrounding at 33:55); the Sifrei on Numbers SILENT (no piska from 31:25 to 35:8 — found by position; 133:3 cites 33:38 to date the daughters); Exod 12:12 (the spec 'I will execute judgments' — the run recorded at 33:4 alone), 12:29-51, 13:20, 14:2, 15:22-27, 16:1, 17:1, 19:1-2 (the nine stations' first tellings — the tape's markers and statuses); Exod 7:7 (Aaron 83, Moses 80 — the ages' checksum), 14:8 (with a high hand), 34:17 (molten gods); Lev 19:4 (molten gods), 26:1 (the figured stone's ban — UNCOMPILED), 26:30 (the high places' curse); Num 10:11-12, 11:34-35, 12:16, 13:3, 13:26 (the march, Kibroth-hattaavah, Hazeroth, Paran — Rithmah), 20:1, 20:22-29, 21:1-11 (Kadesh, Mount Hor, the death, Arad, Oboth, Iye-abarim), 22:1, 25:1 (the plains of Moab, Shittim), 26:52-56 (the lot — restated at 33:54), 27:12 (the mountain of Abarim), 32:34 (Dibon Gad); Deut 1:3 (the fortieth year's other date), 10:6-7 (the four stations in another order, Moserah), 34:7 (Moses 120); Josh 5:10-12 (the morrow of the Passover, the manna's ceasing), 23:13 (the negative arm's run); Judg 2:3; 1 Kgs 6:1 (the era's third stamp); Ps 77:21, Isa 14:24, Neh 9:11, Ezek 25:11 (observed); Babylonian Talmud Rosh Hashanah 2b-3a, Kiddushin 37b-38a, Megillah 22b, Bava Batra 17a, 117a-122a, Berakhot 9a, Eruvin 55b, Yoma 75b, Sotah 34a, Taanit 9a, Yevamot 13b, Megillah 11a; Mishnah Zevachim 14:4-8; Seder Olam Rabbah 9-10"
KINDS = [
 ("journeys_written", "act",
  "the journeys written — 'these are the journeys of the children of Israel who went out of the land of Egypt by their hosts by the hand of Moses and Aaron; and MOSES WROTE their goings out by their journeys BY THE MOUTH OF THE LORD, and these are their journeys by their goings out' (Num 33:1-2): THE CHAPTER'S OWN ACT — the writing (the four Torah seats of 'and Moses wrote': Exodus 24:4, this, Deuteronomy 31:9, 31:22); 'these are the journeys' 10:28's first four words; 'by their hosts' sixteen seats all in Numbers; 'by the hand of Moses and Aaron' 33:1 and Psalm 77:21 alone; 'by the mouth of the LORD' at 33:2 and 33:38 (Moses wrote by it, Aaron went up by it — Onkelos 'by the WORD of the LORD'); the chiasm goings-out / journeys; THE VALUE THE LIST — forty-two places (Rameses and forty-one camps, forty-two 'journeyed' and forty-two 'camped'), the DATA row the_stations built from the DB, each with its first telling and the tape's witness; a retelling never writes a camp twice — the list is the writing's value, the camps' days their first tellings'",
  HE(33, 1, 2, "these are the journeys of the children of Israel who went out of the land of Egypt by their hosts by the hand of Moses and Aaron"), WIT(33, 1, 2), INK_ALL, CORPUS,
  SUB % ("moses", "journeys_recorded on israel_people (the STATUS valued the forty-two places' count and names — the itinerary's one write for forty-eight verses); no new entity"), ["count", "by_the_mouth_of_the_lord", "first"]),
 ("gods_judged_at_the_departure", "act",
  "the judgments on the gods recorded at the departure — 'and they journeyed from Rameses in the first month, on the fifteenth day of the first month; on the morrow of the Passover the children of Israel went out with a high hand in the sight of all Egypt; and Egypt was burying those whom the LORD had struck among them, every firstborn; AND ON THEIR GODS THE LORD EXECUTED JUDGMENTS' (Num 33:3-4): THE DATE (1, 1, 15) = the tape's exodus marker at Exodus 12:41 (a retelling's date a checkpoint, never a second marker); 'the morrow of the Passover' two Bible seats (33:3, Joshua 5:11 — the run's two ends); 'with a high hand' Exodus 14:8's posture (the shelach runner's cell at 15:30); the burial the aftermath of the firstborn's plague — Egypt's plague_struck the_firstborn OPEN, a burial is not a removal (the four removals' rule); THE RUN OF EXODUS 12:12 — 'I will execute judgments' the spec, the perfect nowhere but here: Exodus narrates the firstborn and never the gods; the itinerary alone records that run, forty years on (Onkelos 'on their idols'); the departure itself already on the tape (12:37 — no second encamped_at)",
  HE(33, 3, 4, "and they journeyed from Rameses in the first month, on the fifteenth day of the first month; on the morrow of the Passover the children of Israel went out with a high hand in the sight of all Egypt"), WIT(33, 3, 4), INK_ALL, CORPUS,
  SUB % ("egypt_people", "judgments_executed_on_their_gods on egypt_people (the STATUS the record writes forty years on — the spec Exodus 12:12 cited in the law note; the firstborn's plague_struck entry OPEN, untouched); no new entity"), ["date", "morrow_of_the_passover", "high_hand", "burying"]),
 ("dispossession_commanded", "speech",
  "the dispossession commanded — 'and the LORD spoke to Moses in the plains of Moab by the Jordan at Jericho, saying: speak to the children of Israel and say to them: when you pass over the Jordan into the land of Canaan, you shall DRIVE OUT all the inhabitants of the land from before you, and DESTROY all their FIGURED STONES, and all their MOLTEN IMAGES you shall destroy, and all their HIGH PLACES you shall DEMOLISH; and you shall dispossess the land and dwell in it, for to you I have given the land to possess it; and you shall inherit the land BY LOT by your families — to the many you shall give more inheritance and to the few less; to whom the lot goes out, his it shall be; by the tribes of your fathers you shall inherit; but if you do not drive out the inhabitants of the land from before you, then those you leave of them shall be THORNS IN YOUR EYES AND PRICKS IN YOUR SIDES, and they shall harass you on the land in which you dwell; and it shall be that as I thought to do to them, I will do to you' (Num 33:50-56): THE CHAPTER'S ONE DIVINE FRAME (33:50 and 35:1 the frame's two seats); the three objects (the figured stone Leviticus 26:1's word — its ban UNCOMPILED, journeys → tochacha OWED; the molten image the calf's word — Exodus 34:17 and Leviticus 19:4 by CALL; the high places Leviticus 26:30's curse in the same verb — the Canaanites', ANOTHER SENSE than the erection's private-altar block); the other iconoclasm commands (Exodus 23:24, 34:13, Deuteronomy 7:5, 12:2-3) name altars, pillars, asherim and graven images — these three are the chapter's own; 33:53's 'to you I have given the land' the fifth expression's gift (Exodus 6:8, OPEN); 33:54 RESTATES 26:52-56 to the people with the first verb plural and the second singular (the lot's debit divide_the_land OPEN since 26:52-56 — cited, not rewritten); THE NEGATIVE ARM run back reversed by Joshua 23:13 ('scourges in your sides and thorns in your eyes') and Judges 2:3, Onkelos's armed bands and surrounding camps, 'as I thought' Isaiah 14:24's phrase; Sotah 34a:5 Joshua in the Jordan reading 33:52 as the crossing's purpose; Megillah 11a:13-14 Saul's Amalek and Haman as the thorns",
  HE(33, 50, 56, "and the LORD spoke to Moses in the plains of Moab by the Jordan at Jericho, saying"), WIT(33, 50, 56), INK_ALL, CORPUS,
  SUB % ("israel", "commanded on israel_people TWICE (the values dispossess_the_inhabitants_and_possess_the_land — OPEN BY DESIGN, its runs Joshua's, its negative arm Joshua 23:13 and Judges 2:3; destroy_their_images — OPEN BY DESIGN, the three objects the value's fields, its runs Joshua's and Judges', 2 Kings 23's the last); the lot: NO write (26:52-56's debit cited by CALL into the second census's cell); no new entity"), ["objects", "lot", "negative_arm", "frame"]),
 ("journeys_case", "case", "the exam's rows on the journeys (Num 33:1-49 — Rosh Hashanah 2b:9-3a:13; Kiddushin 37b:14-38a:7; Bava Batra 17a:3; Berakhot 9a:25; Eruvin 55b:15; Yoma 75b:14; Taanit 9a:10; Yevamot 13b:6; Seder Olam Rabbah 9:2, 10:2): the era's new year from the chapter's date (the fortieth year in Av and in Shevat one year), the era's three stamps, redeemed at evening and left by day, the morrow of the Passover at both ends and the manna's forty years less thirty days, Moses' seventh of Adar and the exact hundred and twenty, the death by the mouth of the LORD, Arad's hearing and the retreat of seven stations to Moserah, the last camp's three parasangs, the directional ending on a station's name",
  HE(33, 38, 39, "and Aaron the priest went up Mount Hor by the mouth of the LORD and died there, in the fortieth year of the going out of the children of Israel from the land of Egypt, in the fifth month, on the first of the month"), WIT(33, 1, 4) + WIT(33, 38, 40) + WIT(33, 49, 49), INK_ALL, CORPUS, CASE % "journeys_recorded / accepted / exempt (the exam's persons)", ["person", "ask"]),
 ("dispossession_case", "case", "the exam's rows on the command (Num 33:50-56 — Sotah 34a:5; Megillah 11a:13-14, 22b:11-13; Mishnah Zevachim 14:4-8; Bava Batra 117a:2-3, 117b:1-5, 119a:1, 119a:5, 119b:3, 122a:3): the crossing's purpose at the Jordan with the drowning as the negative arm, Saul's Amalek and Haman as the thorns, the figured stone at its ban (the stone floor, the outstretched limbs — the cell uncompiled, the row filed to the debt), the private altar's eras not this chapter's high places, the land divided among those who left Egypt or those who entered, held before assignment, by lot and by the Urim",
  HE(33, 52, 52, "and you shall drive out all the inhabitants of the land from before you, and destroy all their figured stones, and all their molten images you shall destroy, and all their high places you shall demolish"), WIT(33, 50, 56), INK_ALL, CORPUS, CASE % "commanded / accepted / exempt (the exam's persons)", ["person", "ask"]),
]
assert len(KINDS) == 5, len(KINDS)
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
for e in ('commanded', 'accepted', 'exempt', 'encamped_at', 'plague_struck', 'nation_to_be_judged', 'molten_image_barred', 'high_places_banned'):
    assert e in fx, e
print('  33:2 plain:', LV('Num', 33, 2)); print('  33:4 plain:', LV('Num', 33, 4))
HE_WROTE = PHRASE(33, 2, ['ויכתב', 'משה', 'את', 'מוצאיהם', 'למסעיהם'])
HE_GODS = PHRASE(33, 4, ['ובאלהיהם', 'עשה', 'יהוה', 'שפטים'])
NEW = [
 ('journeys_recorded', 'status',
  "the journeys recorded — the STATUS the writing writes on the people: 'and Moses wrote their goings out by their journeys by the mouth of the LORD, and these are their journeys by their goings out' (Num 33:2) — the value THE LIST: forty-two places (Rameses and forty-one camps; forty-two 'journeyed' and forty-two 'camped' on the ink's own count, the first departure and the last camp each told twice), each with its first telling outside the chapter or none (eighteen named nowhere else by lemma: the Red Sea camp, Dophkah, Alush, Rithmah, Rimmon-perez, Rissah, Kehelathah, Mount Shepher, Haradah, Makheloth, Mithkah, Hashmonah, Bene-jaakan, Hor-haggidgad, Abronah, Zalmonah, Punon, Almon-diblathaim) and the tape's witness (nine of Exodus's stations markers or statuses, ten of Numbers' — a retelling never writes a camp twice: the camps' days are their first tellings', the record's day the writing's, (40, 6, 1)); THE FOUR WRITINGS of Moses (Exodus 24:4, Numbers 33:2, Deuteronomy 31:9, 31:22); the shelf's reading of the thirty-eight years 'without record except the list of stations' (Seder Olam Rabbah 10:2's editor)",
  HE_WROTE + " (and Moses wrote their goings out by their journeys — Num 33:2)",
  "Num 33:2 ('and Moses wrote' — the four Torah seats: Exod 24:4, Num 33:2, Deut 31:9, 31:22; 'by the mouth of the LORD' twenty-one Bible seats, 33:2 and 33:38 the chapter's), 33:1 ('these are the journeys' — 10:28's first four words; 'by their hosts'; 'by the hand of Moses and Aaron' — Ps 77:21 the other seat), 33:5-49 (the forty-two); Onkelos 33:2 ('by the WORD of the LORD'); Exod 12:37, 13:20, 14:2, 15:22-27, 16:1, 17:1, 19:2 and Num 11:34-35, 12:16, 20:1, 20:22, 21:4, 21:10-11, 22:1, 25:1 (the first tellings on the tape); Deut 10:6-7 (four of the stations in another order); Seder Olam Rabbah 9:2 (the retreat of seven stations); Babylonian Talmud Yevamot 13b:6 (Diblathaimah's directional ending), Eruvin 55b:15, Yoma 75b:14 (the last camp's extent)",
  "num_33_journeys (STEP_Nm_33_1 through STEP_Nm_33_49; the claims MS33A-01 … MS33A-09)",
  "cold_run_journeys.py (F1 the_heading_and_the_writing — the writing's cell; F3 the_stations — the list; the exam kind journeys_case)"),
 ('judgments_executed_on_their_gods', 'status',
  "the judgments executed on their gods — the STATUS the itinerary's record writes on Egypt forty years after the night: 'and Egypt was burying those whom the LORD had struck among them, every firstborn; and on their gods the LORD executed judgments' (Num 33:4) — THE RUN OF EXODUS 12:12's 'and on all the gods of Egypt I will execute judgments, I am the LORD' (the future there and at Ezekiel 25:11 alone; the perfect nowhere but here): Exodus narrates the firstborn struck (12:29 — the tenth plague_struck on Egypt's ledger, OPEN with no removal) and never the judgments on the gods; the itinerary alone records that run, so this status is the act's FIRST TELLING, not a retelling — no entry stood open to close (the nation_to_be_judged of Genesis 15:14 closed at 12:29 with 12:12 in its note is Israel's entry, not Egypt's); Onkelos 'on their idols' (25:2's word); the burial the plague's aftermath — a burial is not a removal, the firstborn's entry stays open",
  HE_GODS + " (and on their gods the LORD executed judgments — Num 33:4)",
  "Num 33:4 ('and on their gods the LORD executed judgments' — one Bible seat of the perfect; 'Egypt was burying' the participle's two seats), 33:3 (the date and the morrow — Exod 12:41's marker); Exod 12:12 (THE SPEC — 'and on all the gods of Egypt I will execute judgments'), 12:29 (the firstborn struck — the tape's plague_struck on egypt_people), 12:37 (the departure — the tape's journeyed); Ezek 25:11 (the future's other seat); Onkelos 33:4 ('on their idols'); Babylonian Talmud Berakhot 9a:25 (redeemed at evening, left by day — 33:3)",
  "num_33_journeys (STEP_Nm_33_3, STEP_Nm_33_4; the claim MS33A-02)",
  "cold_run_journeys.py (F2 the_departure — the record's cell; the exam kind journeys_case)"),
]
added = 0
for name, op, en, he, ink, corpus, exam in NEW:
    if name in fx: continue
    text = text.rstrip('\n') + '\n' + f"  {name}:\n    en: {q(en)}\n    he: {q(he)}\n    ledger_op: {op}   # THE NUMBERS WALK 13b (2026-09-12): the journeys' compile — {name}\n    ink: {q(ink)}\n    corpus: {q(corpus)}\n    exam: {q(exam)}\n"
    added += 1
open(path, 'w', encoding='utf-8').write(text)
fx = yaml.safe_load(open(path, encoding='utf-8'))['effects']
assert all(n in fx for n, *_ in NEW) and fx['journeys_recorded']['ledger_op'] == 'status' and fx['judgments_executed_on_their_gods']['ledger_op'] == 'status'
print('effects: %d added (registry %d); the he found in the verses: %s | %s' % (added, len(fx), HE_WROTE, HE_GODS))
# ---- NO registry row (measured: no party written on for the first time) ----
reg = yaml.safe_load(open(f"{ROOT}/logic/corpus/entity_registry.yaml", encoding='utf-8'))
assert all(x in {e['id'] for e in reg['entities']} for x in ('moses', 'israel_people', 'egypt_people')), 'the three written-on parties must stand'
print('entities: 0 added (registry %d) — moses, israel_people, egypt_people standing' % len(reg['entities']))
# ---- the daemon block + the functions block (daemon_dispositions.yaml) ----
path = f"{ROOT}/World/step9/daemon_dispositions.yaml"
text = open(path, encoding='utf-8').read()
if '  law_journeys:' not in text:
    block = '''  law_journeys:
    file: cold_run_journeys.py
    wraps: journeys
    given_at: Num 33:50
    installed_by: boot   # THE NUMBERS WALK 13b (2026-09-12): A LAW IN THE DIVINE VOICE SPOKEN IN THE PLAINS OF MOAB — 'and the LORD spoke to Moses in the plains of Moab by the Jordan at Jericho, saying' (33:50; 35:1 the frame's second seat) — the chapter's ONE divine frame after forty-nine verses without one; the walk's standing setting for a law spoken at its verse (law_shelach, law_korach, law_chukat, law_balak, law_second_census the same), beside law_musafim's called_from_the_tent at 28:1 in the same plains; the measured registry (jou_compile_recon.out) carries no verse as an installed_by and no installing act for the plains' speeches, and the state doc's sketch 'installed_by the verse' (#152) gives way to the measured form; THE SECOND PASS (D2) decides whether the plains' speeches take the tent's act (COMPILE_DEBT.md's sitting-13b box)
    watches:
      journeys_written: [journeys_recorded]                                          # 33:1-2: Moses wrote — the STATUS on the people valued the forty-two (the list the writing's value; no camp written twice)
      gods_judged_at_the_departure: [judgments_executed_on_their_gods]               # 33:3-4: the run of Exodus 12:12 recorded on Egypt — the act's first telling; the firstborn's plague OPEN (a burial is no removal)
      dispossession_commanded: [commanded]                                           # 33:50-56: TWO DEBITS on israel_people — dispossess and possess (OPEN to Joshua's runs; the negative arm Joshua 23:13, Judges 2:3), destroy the three objects (OPEN); the lot's debit of 26:52-56 cited, not rewritten
      journeys_case: [journeys_recorded, accepted, exempt]                           # the exam's rows on the journeys — the era's new year, the morrow, Moses' seventh of Adar, the retreat of seven stations, the last camp's extent
      dispossession_case: [commanded, accepted, exempt]                              # the exam's rows on the command — the crossing's purpose, the thorns, the figured stone at its ban, the private altar's eras, the lot's arms
'''
    i = text.index('  law_zelophehad:')
    text = text[:i] + block + text[i:]
if '\n  journeys:   # THE NUMBERS WALK 13b' not in text:
    fb = '''  journeys:   # THE NUMBERS WALK 13b (2026-09-12)
    the_heading_and_the_writing: {status: WRAPPED, by: law_journeys}
    the_departure: {status: WRAPPED, by: law_journeys}
    the_stations: {status: WRAPPED, by: law_journeys}
    aarons_death_retold: {status: WRAPPED, by: law_journeys}
    the_command: {status: WRAPPED, by: law_journeys}
'''
    i = text.index('  gad_reuben:   # THE NUMBERS WALK 12b (2026-09-12)')
    j = text.index('\n  pre_sinai:', i)
    text = text[:j + 1] + fb + text[j + 1:]
open(path, 'w', encoding='utf-8').write(text)
dd = yaml.safe_load(open(path, encoding='utf-8'))
assert 'law_journeys' in dd['daemons'] and 'journeys' in dd['functions'], (list(dd)[:5])
print('daemons: %d (law_journeys %s); functions blocks: %d' % (len(dd['daemons']), 'law_journeys' in dd['daemons'], len(dd['functions'])))
# ---- the dependency span + edges (the POINTERS after the gate's print) ----
path = f"{ROOT}/World/step9/dependency_dispositions.yaml"
text = open(path, encoding='utf-8').read()
if '\n  journeys:' not in text.split('\nedges:')[0]:
    a = "  gad_reuben:  [[Num, 32, 1, 42]]"
    i = text.index(a); j = text.index('\n', i)
    text = text[:j + 1] + "  journeys:    [[Num, 33, 1, 56]]   # THE NUMBERS WALK 13b (2026-09-12; NUMBERS_WALK.md \"Sitting 13b\"): the journeys — the writing, the departure with the judgments on the gods, the forty-two stations as a data list, Aaron's death retold, Arad, the command in the plains of Moab\n" + text[j + 1:]
    edges = '''  - {from: journeys, to: exodus_story, disposition: CALL, link: reference, carries: verdict,
     why: "THE NUMBERS WALK 13b (2026-09-12) | 33:5-15's stations are Exodus 12:37-19:2's own names (Rameses, Succoth, Etham, Pi-hahiroth, Marah, Elim, Sin, Rephidim, Sinai — 33:6 IS Exodus 13:20 with one word added; 33:9 word for word with 15:27): ES.night('stations') = 9 (its why names Numbers 33's list as the run's citation), ES.night('by_day'), ES.plagues('ten' / 'removed'), ES.sinai('new_moon'), ES.marah('three_days'), ES.manna('forty_years') CALLED — the shared names the reference; 33:4's burial reads Egypt's plague_struck the_firstborn entry (12:29) off the running world (CZ4)"}
  - {from: journeys, to: pesach, disposition: CALL, link: reference, carries: verdict,
     why: "THE NUMBERS WALK 13b (2026-09-12) | 33:3's 'on the morrow of THE PASSOVER' and 33:4's 'every FIRSTBORN' are the Passover's own names (Exodus 12:11, 12:12's 'every firstborn'); PS.firstborn({'kind': 'human'}) CALLED (the firstborn cell — 13:15's 'on the day I struck every firstborn in the land of Egypt'); Exodus 12:12's SPEC 'on all the gods of Egypt I will execute judgments' lies inside the pesach runner's span with NO CELL on the gods (measured: jou_compile_measure.out (4)) — the record at 33:4 cites the spec verse in its law note and writes the status itself: the reference by the shared names"}
  - {from: journeys, to: beha, disposition: CALL, link: reference, carries: verdict,
     why: "THE NUMBERS WALK 13b (2026-09-12) | 33:16-17's Kibroth-hattaavah and Hazeroth are 11:34-35's names (the naming 11:34 — BH.taberah_and_quail('graves') CALLED, 'the graves of lust'), 33:18's departure from Hazeroth 12:16's (BH.march('day_stack') CALLED — Hazeroth (2, 3, 22), Paran (2, 3, 29) the tape's markers; BH.march('year_turns') — the second year's Nisan and Iyar one year, Rosh Hashanah 3a:5): the shared names the reference"}
  - {from: journeys, to: shelach, disposition: CALL, link: reference, carries: verdict,
     why: "THE NUMBERS WALK 13b (2026-09-12) | 33:3's 'WITH A HIGH HAND' is the shelach runner's own seat — SL.high_hand('high_hand_posture') returns 'the exodus's posture — with a high hand (Exodus 14:8; Numbers 33:3)': the callee names this verse; 33:18's Rithmah is 12:16's Paran under another name (the spies' base — 13:3 'from the wilderness of Paran', 13:26 'to the wilderness of Paran, to Kadesh'): SL.spies('forty_days'), SL.decree('count_from' / 'deaths_ceased') CALLED — the shared names the reference"}
  - {from: journeys, to: chukat, disposition: CALL, link: reference, carries: verdict,
     why: "THE NUMBERS WALK 13b (2026-09-12) | 33:36-40 retell 20:1-21:4 in their own names (Kadesh in the wilderness of Zin, Mount Hor at the edge of Edom, Aaron went up and died, the Canaanite king of Arad heard) and 33:38-39 carry THE DATE AND THE AGE the tape's 20:28 line already reads from this chapter: CK.AARON_DATE (40, 5, 1), CK.AARON_AGE [123], CK.edom_and_hor('death_dates' / 'aaron_age' / 'arad_heard' / 'moserah' / 'two_mount_hors' / 'thirty_days' / 'succession'), CK.DATA['moserah'] (the retreat of seven stations — Seder Olam Rabbah 9:2) and CK.DATA['arad_heard'] CALLED; 33:43-44's Oboth and Iye-abarim 21:10-11's; 33:40's hearing a RUN_CITATION of the tape's arad_fought_and_took_captives at 21:1 — the shared names the reference"}
  - {from: journeys, to: balak, disposition: CALL, link: reference, carries: verdict,
     why: "THE NUMBERS WALK 13b (2026-09-12) | 33:48-50's 'the plains of Moab by the Jordan at Jericho' is 22:1's last camp (BK.the_call('last_camp') CALLED — 'the book never moves again') and 33:49's Abel-shittim 25:1's Shittim (BK.peor('shittim_name') CALLED — the place's name or an allusion, Bekhorot 5b): the shared names the reference; 33:55's 'harass' 25:18's Midian word (the same lemma, OBSERVED)"}
  - {from: journeys, to: second_census, disposition: CALL, link: reference, carries: verdict,
     why: "THE NUMBERS WALK 13b (2026-09-12) | 33:54 RESTATES 26:52-56 TO THE PEOPLE word for word ('by lot', 'to the many you shall give more inheritance and to the few less', 'by the tribes of your fathers') with the first verb turned plural and the second left singular: C2.the_land('by_lot' / 'lots_mouth' / 'by_number_of_names' / 'land_divided_among' / 'possession_before_assignment') and C2.DATA['division_by'] CALLED; THE OPEN divide_the_land DEBIT on israel_people (26:52-56) is CITED, NOT REWRITTEN — a restatement of a command is a retelling (CZ7 asserts ONE entry)"}
  - {from: journeys, to: gad_reuben, disposition: CALL, link: reference, carries: verdict,
     why: "THE NUMBERS WALK 13b (2026-09-12) | 33:45-46's DIBON GAD is 32:34's city under its tribe's name — the Gad runner's own cell names these verses ('the itinerary's own witness to the city's tribe'): GR.the_cities('dibon_gad') CALLED, GR.the_grant('not_by_lot') (the east not by 26:55's lot — 33:54's lot is Canaan's) and GR.DATA['negative_arm_outcome'] (the chapter's negative arm 33:55-56 beside 32:23's) READ: the shared name the reference"}
  - {from: journeys, to: erection, disposition: CALL, link: reference, carries: verdict,
     why: "THE NUMBERS WALK 13b (2026-09-12) | 33:52's 'all their MOLTEN IMAGES' is the calf's word (Exodus 32:4 'a molten calf'; 34:17 'molten gods you shall not make for yourself' — the ban the covenant restates): ER.covenant('molten_two_seats') = ([('Exod', 34, 17)], [('Lev', 19, 4)]), ER.calf('molten_calf') = 4 seats, ER.covenant('demolition_grows') = [3, 4, 5] (the other iconoclasm commands' lists — altars, pillars, asherim, graven images: 33:52's three objects are its own) CALLED; aaron's molten_image_barred block (Exodus 32:4) READ off the running world; the erection's high_places_banned is the PRIVATE ALTAR's block on the land's era — ANOTHER SENSE than 33:52's Canaanite high places (Mishnah Zevachim 14:4-8 read at the docket: the sense decided) — FALSE for that effect, the shared word named"}
  - {from: journeys, to: holiness, disposition: CALL, link: reference, carries: verdict,
     why: "THE NUMBERS WALK 13b (2026-09-12) | 33:52's 'molten images' with Leviticus 19:4's 'molten gods you shall not make for you' (the vav-form's one seat): HL.frame('molten_warnings') (the Sifra's two warnings, R. Yosei's third) and HL.frame('idols_look') CALLED — the shared word the reference"}
  - {from: journeys, to: tochacha, disposition: OWED, link: reference,
     why: "THE NUMBERS WALK 13b (2026-09-12) | 33:52's 'all their FIGURED STONES' is Leviticus 26:1's word ('a figured stone you shall not install in your land to bow upon it' — the same lemma; Megillah 22b:11-13's ban on the stone floor) and 'all their HIGH PLACES you shall DEMOLISH' Leviticus 26:30's curse in the same verb on the same object ('I will destroy your high places') — both seats lie inside the tochacha runner's declared span [[Lev, 26, 1, 46]] with NO CELL: its cells are the covenant's arms, 'your high places' stands in its token table only, and no runner's cell compiles 26:1-2 (measured at this sitting, jou_compile_measure.out (4)); THE COMPILE DEBT 'Leviticus 26:1-2's own compile — the idols, the graven image, the pillar, the figured stone; the sabbaths and the sanctuary' filed in COMPILE_DEBT.md's sitting-13b box with Megillah 22b:11-13 as its first exam rows; the reference by the shared lemmas; the CALL owed to that sitting"}
  - {from: sequence, to: journeys, disposition: CALL, link: none,
     why: "THE NUMBERS WALK 13b (2026-09-12) | the sequential run's REGISTRATION edge — ('cold_run_journeys', 'law_journeys') in DAEMON_ORDER (the runner compiles no verse: link none, O4's license)"}
'''
    a = "  - {from: sequence, to: gad_reuben, disposition: CALL, link: none,"
    i = text.index(a); j = text.index('\n', text.index('why:', i)) + 1
    text = text[:j] + edges + text[j:]
    open(path, 'w', encoding='utf-8').write(text)
dep = yaml.safe_load(open(path, encoding='utf-8'))
assert 'journeys' in dep['spans'] and sum(1 for e in dep['edges'] if e['from'] == 'journeys') == 11
print('dependency: span + 12 edges (journeys 11 + the registration); the pointers after the gate\'s print')
# ---- the installation probe's count ----
path = f"{ROOT}/World/step9/installation_probes.py"
text = open(path, encoding='utf-8').read()
a = "len(real) == 59 and all('given_at' in d and 'installed_by' in d for d in real.values())   # THE NUMBERS WALK 12b (2026-09-12): 58 -> 59, law_gad_reuben"
if a in text:
    text = text.replace(a, "len(real) == 60 and all('given_at' in d and 'installed_by' in d for d in real.values())   # THE NUMBERS WALK 13b (2026-09-12): 59 -> 60, law_journeys (installed_by boot — a law in the divine voice spoken in the plains of Moab, the class named); 12b: 58 -> 59, law_gad_reuben")
    open(path, 'w', encoding='utf-8').write(text)
assert "len(real) == 60" in open(path, encoding='utf-8').read()
print('installation_probes I5: 60')
