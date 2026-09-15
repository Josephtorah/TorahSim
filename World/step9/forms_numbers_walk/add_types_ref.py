import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE NUMBERS WALK sitting 15b — THE COMPILE OF THE REFUGE CITIES (2026-09-13; World/step9/NUMBERS_WALK.md "Sitting 15b"): THE TYPES FIRST — TWO
# tape kinds (the Levite cities commanded 35:1-8, the refuge law given 35:9-34), FOUR case-form kinds for the exam's scene (the Levite cities' rows,
# the killer's rows, the statute's rows, and THE OFFICE-HOLDER'S DEATH — the term's closer, its tape seat outside the Torah), THREE new effects
# (dwells_in_refuge — a BODY entry, the term; returns_to_his_possession and land_polluted_by_blood — statuses; the ink's own words at 35:25, 35:28,
# 35:33), NO registry row (the chapter writes on israel_people and the_land_of_canaan, both standing; the exam's persons scene-local), the 62nd
# daemon's block (law_refuge, given_at Num 35:1, installed_by BOOT with the class named — a law in the divine voice in the plains of Moab, 33:50's
# class), the functions block, the dependency span and edges (the pointers after the gate's print), the installation probe's count.
# The `he` is cut from the pointed DB text by FINDING the phrase's tokens (never a typed index); the witnesses the plain consonantal verses.
# Idempotent (add_types_bor.py's form).
import re, sqlite3, yaml
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
CORPUS = "num_35_refuge_cities (STEP_Nm_35_1 through STEP_Nm_35_34; claims MS35A-01 through MS35A-14)"
SUB = "submitted by cold_run_refuge.py [subjects: %s] (the narrative scene, THE NUMBERS WALK 15b); re-submitted on the sequential tape by cold_run_sequence.py; consumed by law_refuge (cold_run_refuge.py) -> %s"
CASE = "submitted by cold_run_refuge.py [subjects: the exam's persons] (the wrap's scene); consumed by law_refuge (cold_run_refuge.py) -> %s"
INK_ALL = "Num 35:1-34; Onkelos Num 35:1-34 ('their needs of life' at 35:3; 'two thousand' supplied four times at 35:5 — the dual read; one word for the refuge at eleven seats and for the deliverance at 35:25; one word for the killer at eighteen; 'when he has been found guilty by the court' supplied at 35:19, 21; the border the Sabbath limit's word at 35:26-27; 'money' for the ransom at 35:31-32; 'innocent' supplied at 35:33; 'my Presence dwells' at 35:34); Sifrei Bamidbar 159:1, 160:1-10, 161:1-5 (the shelf's Hebrew duplicating 161:1-4 at 160:11-14); Sifrei Bamidbar 1:2, 1:7 (credited); the exam docket num_35_refuge_cities_exam_2026-09-13.md (666 rows — Makkot 7a-13a whole, Sanhedrin 2a-2b, 76b-79a, 27b, 45b, Bava Kamma 40a-41a, Ketubot 37b, Eruvin 51a, Sotah 27b, Arakhin 33b, Yoma 23a, Megillah 29a, Yevamot 46b, the twenty-two Mishnah rows, 104 link rows in 25 works)"
KINDS = [
 ("levite_cities_commanded", "speech",
  "the Levite cities commanded — 'and the LORD spoke to Moses in the plains of Moab by the Jordan at Jericho, saying: command the children of Israel that they give to the Levites from the inheritance of their possession CITIES TO DWELL IN, and pasture-land for the cities round about them you shall give to the Levites … from the wall of the city outward A THOUSAND CUBITS round about; and you shall measure from outside the city the east side TWO THOUSAND BY THE CUBIT, and the south side two thousand … and the city in the midst … and the cities that you shall give to the Levites: the six cities of refuge which you shall give for the manslayer to flee there, and beside them you shall give FORTY-TWO cities; all the cities that you shall give to the Levites: FORTY-EIGHT cities, them and their pasture-lands; … from the many you shall take more and from the few you shall take less, each according to his inheritance' (Num 35:1-8) — ONE DEBIT on the people (commanded, the value give_the_levites_cities_and_pasture_lands, counterparty the Levites) OPEN BY DESIGN to its run at Joshua 21:1-42 (21:2 the request quoting 'cities to dwell in'; 21:41 the tally forty-eight; the four lots 13 + 10 + 13 + 12 by the parser); the table DATA (48 = 6 + 42; the measures with the exam's settings; the four sides in the camp's order; 26:54's rule by CALL); the Levites' block inheritance_barred (18:20-24) standing — the cities are the people's, given",
  HE(35, 1, 8, "and the LORD spoke to Moses in the plains of Moab by the Jordan at Jericho, saying"), WIT(35, 1, 8), INK_ALL, CORPUS,
  SUB % ("israel", "commanded on israel_people (the DEBIT give_the_levites_cities_and_pasture_lands, counterparty the-levites, OPEN by design — Joshua 21 outside the Torah, THE READBACK's)"), ["cities", "refuge", "others", "thousand", "two_thousand", "sides"]),
 ("refuge_law_given", "speech",
  "the refuge law given — 'and the LORD spoke to Moses, saying: speak to the children of Israel and say to them: when you are crossing the Jordan to the land of Canaan, YOU SHALL APPOINT for yourselves cities, cities of refuge they shall be for you, and a manslayer shall flee there who smites a soul unwittingly; and the cities shall be for you a refuge from the avenger, and the manslayer shall not die until he stands before the congregation for judgment … six cities of refuge … three beyond the Jordan and three in the land of Canaan … for the children of Israel and for the stranger and for the sojourner … and if with an instrument of iron he struck him and he died, he is a murderer, the murderer shall surely die … the avenger of blood shall put the murderer to death when he meets him … and if suddenly without enmity … the congregation shall judge between the smiter and the avenger of blood … and the congregation shall deliver the manslayer … and he shall dwell in it UNTIL THE DEATH OF THE HIGH PRIEST … he has no blood … a statute of judgment for your generations in all your dwellings … by the mouth of witnesses … one witness shall not testify … you shall not take ransom … the blood, it pollutes the land … in whose midst I dwell' (Num 35:9-34) — THE STATUTE: ONE DEBIT on the people (commanded, the value appoint_six_cities_of_refuge) OPEN BY DESIGN to Deuteronomy 4:41-43 (Moses' three, inside the Torah — that book's compile) and Joshua 20:7-8 (the six); the law's cells the exam's (killer_case, refuge_statute_case); the term an open BODY entry closed by the office-holder's death (high_priest_died — outside the Torah on the tape)",
  HE(35, 9, 34, "and the LORD spoke to Moses, saying"), WIT(35, 9, 34), INK_ALL, CORPUS,
  SUB % ("israel", "commanded on israel_people (the DEBIT appoint_six_cities_of_refuge, OPEN by design — Deuteronomy 4:41 and Joshua 20:7-8 the runs, THE READBACK's)"), ["six", "beyond_the_jordan", "in_canaan", "until", "witnesses", "ransom"]),
 ("levite_cities_case", "case", "the exam's rows on the Levite cities (Num 35:1-8 — Mishnah Sotah 5:3 / Sotah 27b:8-10 R. Akiva's thousand and two thousand; Mishnah Arakhin 9:8 / Arakhin 33b:12-15 the thousand and the thousand, the field and the lot unchanged; Eruvin 51a:8-14 the Sabbath limit's measure and the square; Eruvin 56b:6, 57a:5-13 the quarter and the karpef; Makkot 10a:4 the forty-two receive too; Makkot 13a:2-3 the rent; Makkot 12b:9 the Levite exiled; Bava Batra 24b:3; Nedarim 81a:7 'their needs of life')",
  HE(35, 4, 5, "and the pasture-lands of the cities that you shall give to the Levites: from the wall of the city outward a thousand cubits round about"), WIT(35, 1, 8), INK_ALL, CORPUS, CASE % "accepted / commanded / exempt (the exam's persons)", ["person", "ask"]),
 ("killer_case", "case", "the exam's rows on the murderer and the manslayer (Num 35:11-28 — Mishnah Makkot 2:1-3 with Makkot 7b-9b the downward motion, the permission, the office, the father and the son, the blind, the enemy; Mishnah Sanhedrin 9:1-2 with Sanhedrin 76b-79a the instruments, the water and the fire, the causation, the intent's table, the ten sticks, the tereifa; Makkot 12a:8-15 the border and the doubled verb; Bava Kamma 86b-87a the blind; Sanhedrin 29a:6 the enemy; the Sifrei 160:3-8 the induction from three, Issi ben Akiva's uncertainty)",
  HE(35, 16, 18, "and if with an instrument of iron he struck him and he died, he is a murderer; the murderer shall surely die"), WIT(35, 9, 28), INK_ALL, CORPUS, CASE % "put_to_death / flees_to_refuge / dwells_in_refuge / has_blood / exempt / accepted (the exam's persons)", ["person", "ask"]),
 ("refuge_statute_case", "case", "the exam's rows on the statute's clauses (Num 35:29-34 — Mishnah Sanhedrin 1:4 with 2a:14-2b:1 the twenty-three; Mishnah Sanhedrin 3:4 with 27b the kin and the haters; Sanhedrin 33b:15 the one witness for acquittal; Mishnah Shevuot 4:1; Ketubot 37b:3-14 and Bava Kamma 83b:9-19, 40a:5-12, 41a:5 the ransom refused and the ox's; Arakhin 16a:22, Zevachim 88b:13, Keritot 26a:17, Mishnah Sotah 9:7 / Sotah 47b:2, Yoma 23a:11-16 the land's atonement and the heifer; Shabbat 33a:4, Yoma 85a:14, Shevuot 7b:7, Megillah 29a:4 the Presence; Makkot 7a:7, Sanhedrin 35b:10, Yevamot 6b:10 'in all your dwellings')",
  HE(35, 30, 31, "whoever smites a soul, by the mouth of witnesses the murderer shall be slain; and one witness shall not testify against a soul to die"), WIT(35, 29, 34), INK_ALL, CORPUS, CASE % "accepted / exempt / put_to_death / land_polluted_by_blood (the exam's persons)", ["person", "ask"]),
 ("high_priest_died", "case", "the high priest's death — THE TERM'S CLOSER: 'and he shall dwell in it until the death of the high priest who was anointed with the holy oil' (35:25), 'for in his city of refuge he shall dwell until the death of the high priest, and after the death of the high priest the manslayer shall return to the land of his possession' (35:28), 'until the death of the priest' (35:32 bare) — the act that closes every open dwells_in_refuge entry by value (the office-holder named at the sentence) and writes returns_to_his_possession; on the tape its seat is OUTSIDE THE TORAH (Eleazar's death, Joshua 24:33 — the term OPEN BY DESIGN, THE READBACK's); in the exam's scene the act is submitted and the close graded (Mishnah Makkot 2:6-7 with Makkot 11a:12-11b:13 — the three high priests, the second's death, the priesthood found void, 'never leaves')",
  PHRASE(35, 25, ['וישב', 'בה', 'עד', 'מות', 'הכהן', 'הגדל']) + " (and he shall dwell in it until the death of the high priest — Num 35:25)", WIT(35, 25, 28), INK_ALL, CORPUS, CASE % "returns_to_his_possession (the exiles' close by value — the daemon's own close)", ["priest", "office"]),
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
# ---- THREE new effects, the ink's own words, the `he` FOUND in the verse ----
path = f"{ROOT}/World/step9/effect_vocabulary.yaml"
text = open(path, encoding='utf-8').read()
fx = yaml.safe_load(text)['effects']
for e in ('commanded', 'accepted', 'exempt', 'flees_to_refuge', 'has_blood', 'put_to_death', 'beheaded', 'ransom_imposed', 'presence_dwells', 'in_custody'):
    assert e in fx, e
print('  35:25 plain:', LV('Num', 35, 25)); print('  35:28 plain:', LV('Num', 35, 28)); print('  35:33 plain:', LV('Num', 35, 33))
HE_DWELL = PHRASE(35, 25, ['וישב', 'בה', 'עד', 'מות', 'הכהן', 'הגדל', 'אשר', 'משח', 'אתו', 'בשמן', 'הקדש'])
HE_RETURN = PHRASE(35, 28, ['ואחרי', 'מות', 'הכהן', 'הגדל', 'ישוב', 'הרצח', 'אל', 'ארץ', 'אחזתו'])
HE_POLLUTE = PHRASE(35, 33, ['כי', 'הדם', 'הוא', 'יחניף', 'את', 'הארץ'])
NEW = [
 ('dwells_in_refuge', 'body',
  "dwells in refuge — THE TERM: the BODY entry the court's deliverance writes on the manslayer, OPEN until the office-holder's death: 'and the congregation shall deliver the manslayer from the hand of the avenger of blood, and the congregation shall return him to his city of refuge where he fled, and he shall dwell in it UNTIL THE DEATH OF THE HIGH PRIEST who was anointed with the holy oil' (Num 35:25), 'for in his city of refuge he shall dwell until the death of the high priest' (35:28), 'to return to dwell in the land until the death of the priest' (35:32) — the value the office-holder at the sentence (Eleazar since Num 20:28 — the chukat runner's succession by CALL; the anointing Leviticus 21:10's, the priesthood runner's), the entry CLOSED BY VALUE when the daemon consumes high_priest_died (an EVENT-keyed term: the engine's timers are day-dues, a death is no date — the design's decision (e)); on the tape the closer is outside the Torah (Joshua 24:33) and the entry would stand OPEN BY DESIGN — no manslayer stands on the tape; in the exam's scene the act closes it (Mishnah Makkot 2:6-7: the three high priests whose deaths return him; the second's death; no high priest at the verdict — never leaves; the high priest who killed or was killed — never; Makkot 11b:7 there his dwelling, his death, his burial)",
  HE_DWELL + " (and he shall dwell in it until the death of the high priest who was anointed with the holy oil — Num 35:25)",
  "Num 35:25 ('and he shall dwell in it until the death of the high priest who was anointed with the holy oil' — the phrase 'until the death of the high priest' two seats, 35:25 and 35:28; 'the high priest' written DEFECTIVE only here, three tokens; Joshua 20:6 plene), 35:28 ('for in his city of refuge he shall dwell until the death of the high priest, and after the death of the high priest the manslayer shall return'), 35:32 ('until the death of the priest' — bare); Onkelos 35:25 'and the congregation shall DELIVER' with the refuge-root; the Sifrei 161:1-3; Babylonian Talmud Makkot 11a:12-13, 11b:7-13, 12a:5-6, Horayot 11b:6, Sanhedrin 18a:14",
  "num_35_refuge_cities (STEP_Nm_35_25, STEP_Nm_35_28, STEP_Nm_35_32; the claims MS35A-05, MS35A-13)",
  "cold_run_refuge.py (F4 the_manslayer — the_deliverance and the_term cells; the exam kind killer_case; the act high_priest_died closes it by value)"),
 ('returns_to_his_possession', 'status',
  "returns to the land of his possession — the STATUS the office-holder's death writes on the manslayer at the term's close: 'and after the death of the high priest the manslayer shall return to the land of his possession' (Num 35:28), 'to return to dwell in the land' (35:32) — written by the daemon consuming high_priest_died beside the close of dwells_in_refuge (the exile's release the death's, not a day's); the shelf: to his land, not his fathers' honor (R. Yehuda) or even to it (R. Meir) — Makkot 13a:6; his bones carried after the death (11b:12); Joshua 20:6 'and come to his city and to his house'",
  HE_RETURN + " (and after the death of the high priest the manslayer shall return to the land of his possession — Num 35:28)",
  "Num 35:28 ('and after the death of the high priest the manslayer shall return to the land of his possession' — 'the land of his possession' one seat), 35:32 ('to return to dwell in the land'); Joshua 20:6; Babylonian Talmud Makkot 11b:12, 13a:4-6; the Sifrei 161:5 (the stem read — 'he will return', not 'bring back')",
  "num_35_refuge_cities (STEP_Nm_35_28, STEP_Nm_35_32; the claim MS35A-05)",
  "cold_run_refuge.py (F4 the_manslayer — the_return cell; the act high_priest_died)"),
 ('land_polluted_by_blood', 'status',
  "the land polluted by blood — the STATUS shed blood writes ON THE LAND while the shedder stands unexecuted: 'you shall not pollute the land in which you are, for the blood, it pollutes the land, and for the land no atonement can be made for the blood shed in it except by the blood of him who shed it' (Num 35:33) — the pollute-root's only Torah seat (Psalm 106:38 'and the land was polluted with blood' its echo); the entry on the_land_of_canaan (the standing place entity) opened by a murder unatoned and closed by the shedder's execution (Arakhin 16a:22, Zevachim 88b:13 — no atonement for the community until he is put to death; where the court cannot, the tunic; the heifer where the killer is unknown — Deuteronomy 21 FORWARD; Mishnah Sotah 9:7 / Sotah 47b:2 the heifer broken and then the killer found — he dies); Shabbat 33a:4 — for bloodshed the Temple is destroyed and the Presence departs, 35:33-34 read whole (the inclusio's guard: presence_dwells OPEN on the people since Exodus 40:34)",
  HE_POLLUTE + " (for the blood, it pollutes the land — Num 35:33)",
  "Num 35:33 ('you shall not pollute the land … for the blood, it pollutes the land, and for the land no atonement can be made for the blood shed in it except by the blood of him who shed it' — the pollute-root two tokens, the Torah's only seat; the ransom's root a third time in the passive), 35:34 ('you shall not defile the land in which you dwell, in whose midst I dwell'); Psalm 106:38; Genesis 9:6 (the shedder's blood — the primeval runner by CALL); Leviticus 18:25-28 (the land that vomits — the sanctions runner by CALL); Onkelos 35:33 'innocent blood' supplied; the Sifrei 161:3 (the notarikon), 161:4 (Deuteronomy 21:1's story); Babylonian Talmud Arakhin 16a:22, Zevachim 88b:13, Keritot 26a:17, Ketubot 37b:5-6, Sotah 47b:2, Shabbat 33a:4, Yoma 85a:14, Shevuot 7b:7",
  "num_35_refuge_cities (STEP_Nm_35_33, STEP_Nm_35_34; the claims MS35A-08, MS35A-13)",
  "cold_run_refuge.py (F5 the_statute — the_land_polluted cell; the exam kind refuge_statute_case)"),
]
added = 0
for name, op, en, he, ink, corpus, exam in NEW:
    if name in fx: continue
    text = text.rstrip('\n') + '\n' + f"  {name}:\n    en: {q(en)}\n    he: {q(he)}\n    ledger_op: {op}   # THE NUMBERS WALK 15b (2026-09-13): the refuge cities' compile — {name}\n    ink: {q(ink)}\n    corpus: {q(corpus)}\n    exam: {q(exam)}\n"
    added += 1
open(path, 'w', encoding='utf-8').write(text)
fx = yaml.safe_load(open(path, encoding='utf-8'))['effects']
assert all(n in fx for n, *_ in NEW) and fx['dwells_in_refuge']['ledger_op'] == 'body' and fx['returns_to_his_possession']['ledger_op'] == 'status' and fx['land_polluted_by_blood']['ledger_op'] == 'status'
print('effects: %d added (registry %d); the he found in the verses: %s | %s | %s' % (added, len(fx), HE_DWELL, HE_RETURN, HE_POLLUTE))
# ---- NO registry row (measured: no party written on for the first time — israel_people and the land of Canaan standing) ----
reg = yaml.safe_load(open(f"{ROOT}/logic/corpus/entity_registry.yaml", encoding='utf-8'))
ids = {e['id'] for e in reg['entities']}
assert all(x in ids for x in ('moses', 'israel_people', 'the_land_of_canaan', 'the_levites', 'eleazar_son_of_aaron', 'the_priesthood', 'the_court')), 'the written-on and the named parties must stand'
print('entities: 0 added (registry %d) — israel_people and the_land_of_canaan standing' % len(reg['entities']))
# ---- the daemon block + the functions block (daemon_dispositions.yaml) ----
path = f"{ROOT}/World/step9/daemon_dispositions.yaml"
text = open(path, encoding='utf-8').read()
if '  law_refuge:' not in text:
    block = '''  law_refuge:
    file: cold_run_refuge.py
    wraps: refuge
    given_at: Num 35:1
    installed_by: boot   # THE NUMBERS WALK 15b (2026-09-13): A LAW IN THE DIVINE VOICE IN THE PLAINS OF MOAB — 'and the LORD spoke to Moses in the plains of Moab by the Jordan at Jericho, saying' at 35:1 (the place-stamp's six seats: 26:3, 26:63, 33:48, 33:50, 35:1, 36:13 — 33:50's class, law_journeys's) and 'and the LORD spoke to Moses, saying' bare at 35:9; no installing act, no relay, no tent — the walk's standing setting (D2: the mechanism built, the setting deferred to the second pass after Deuteronomy); the class named here so the second pass finds it
    watches:
      levite_cities_commanded: [commanded]                                        # 35:1-8: ONE debit on the people — give_the_levites_cities_and_pasture_lands, OPEN by design (Joshua 21 outside the Torah); the table DATA
      refuge_law_given: [commanded]                                               # 35:9-34: ONE debit on the people — appoint_six_cities_of_refuge, OPEN by design (Deuteronomy 4:41; Joshua 20:7-8); the statute's cells the exam's
      levite_cities_case: [accepted, commanded, exempt]                            # the exam's rows on the Levite cities — the measures' three settings, the forty-eight, the rule, the rent, the Levite exiled
      killer_case: [put_to_death, flees_to_refuge, dwells_in_refuge, has_blood, exempt, accepted]   # the exam's rows on the murderer (the sword by CALL) and the manslayer (the flight, the term OPEN, the border's no-blood, the neither row 'unresolved')
      refuge_statute_case: [accepted, exempt, put_to_death, land_polluted_by_blood]   # the exam's rows on the statute — the twenty-three, the witnesses, the ransom refused (the death stands), the land polluted, the Presence read
      high_priest_died: [returns_to_his_possession]                               # the office-holder's death — every open dwells_in_refuge CLOSED BY VALUE (the daemon's own close) and the return written; on the tape outside the Torah
'''
    i = text.index('  law_census:')
    text = text[:i] + block + text[i:]
if '\n  refuge:   # THE NUMBERS WALK 15b' not in text:
    fb = '''  refuge:   # THE NUMBERS WALK 15b (2026-09-13)
    the_levite_cities: {status: WRAPPED, by: law_refuge}
    the_refuge_law: {status: WRAPPED, by: law_refuge}
    the_murderer: {status: WRAPPED, by: law_refuge}
    the_manslayer: {status: WRAPPED, by: law_refuge}
    the_statute: {status: WRAPPED, by: law_refuge}
'''
    i = text.index('  borders:   # THE NUMBERS WALK 14b (2026-09-13)')
    j = text.index('\n  pre_sinai:', i)
    text = text[:j + 1] + fb + text[j + 1:]
open(path, 'w', encoding='utf-8').write(text)
dd = yaml.safe_load(open(path, encoding='utf-8'))
assert 'law_refuge' in dd['daemons'] and 'refuge' in dd['functions'], (list(dd)[:5])
print('daemons: %d (law_refuge %s); functions blocks: %d' % (len(dd['daemons']), 'law_refuge' in dd['daemons'], len(dd['functions'])))
# ---- the dependency span + edges (the POINTERS after the gate's print) ----
path = f"{ROOT}/World/step9/dependency_dispositions.yaml"
text = open(path, encoding='utf-8').read()
if '\n  refuge:' not in text.split('\nedges:')[0]:
    a = "  borders:     [[Num, 34, 1, 29]]"
    i = text.index(a); j = text.index('\n', i)
    text = text[:j + 1] + "  refuge:      [[Num, 35, 1, 34]]   # THE NUMBERS WALK 15b (2026-09-13; NUMBERS_WALK.md \"Sitting 15b\"): the refuge cities — the Levite cities as one debit on the people and a table, the six cities a data row and a debit, the murderer's and the manslayer's case table (the size clause a parameter), the term an open entry closed by the office-holder's death, the border, the witnesses, no ransom, the land polluted\n" + text[j + 1:]
    W = "THE NUMBERS WALK 15b (2026-09-13) | "
    edges = f'''  - {{from: refuge, to: mishpatim_3, disposition: CALL, link: reference, carries: verdict,
     why: "{W}35:11's 'and a manslayer shall flee there' is Exodus 21:13's 'I will appoint you a PLACE where he shall flee' — the place become cities (M3.killer('the_place') CALLED: the Levites' cities for the generations, the camps for the hour — Makkot 12b:8); 35:23's 'and he dropped it on him' the downward motion (M3.killer('refuge_by_descent') CALLED: Mishnah Makkot 2:1's rows at their second seat); 35:16-21's murderer put to death BY THE SWORD (M3.killer('mode') CALLED: Sanhedrin 9:1; 52b:13); 35:27's 'he has no blood' is Exodus 22:1's clause at its second seat (the effect has_blood REUSED; M3.burglar('judged_by_his_end')); the father and the son (M3.killer('father_and_son')); the office's exemptions (M3.killer('guile_excludes'))"}}
  - {{from: refuge, to: mishpatim, disposition: CALL, link: reference, carries: verdict,
     why: "{W}35:31's 'you shall not take RANSOM for the life of a murderer' refuses the noun Exodus 21:30 grants the goring ox's owner ('if a ransom be laid on him') — the ransom's four Torah seats named at the reading: the mishpatim runner's STONE+RANSOM cell and its effect ransom_imposed CALLED as the contrast (Ketubot 37b:12: Heaven's death commuted to money, the court's never; Bava Kamma 40a:5-12, 41a:5)"}}
  - {{from: refuge, to: lev24, disposition: CALL, link: reference, carries: verdict,
     why: "{W}35:30's 'whoever smites a soul' is Leviticus 24:17's 'a man who strikes any soul of man shall surely be put to death' (Sanhedrin 84b:6 — the two clauses both needed; 78a:3 R. Yochanan on 'any soul'); Bava Kamma 83b:9-19 derives the talion's MONEY from 35:31's 'no ransom for the LIFE of a murderer' through Leviticus 24:18-21 (L24.talion('kill') CALLED — PAY-MONEY)"}}
  - {{from: refuge, to: shelach, disposition: CALL, link: reference, carries: verdict,
     why: "{W}35:11's and 35:15's 'unwittingly' is the sin offering's word (Numbers 15:22-29 — 'in error' thrice at 15:27-29, SL.error('thrice_unwitting') CALLED; the thirteen seats measured at the reading: Leviticus 4-5, 22:14; Numbers 15; 35:11, 15); Makkot 7b:3 — 'unwittingly' excludes the intentional from exile"}}
  - {{from: refuge, to: naso, disposition: CALL, link: reference, carries: verdict,
     why: "{W}35:34's 'in whose midst I dwell' is 5:3's 'that they not defile their camps in whose midst I dwell' — THE BOOK'S INCLUSIO (the Torah's two seats of the phrase, computed): NS.camp_purity('three_camps' / 'classes') CALLED at the second seat; 35:22's 'suddenly' is 6:9's (the nazirite's — the word's two Bible seats; Keritot 9a:19)"}}
  - {{from: refuge, to: second_census, disposition: CALL, link: reference, carries: verdict,
     why: "{W}35:8's 'from the many you shall take more and from the few you shall take less' is 26:54's rule at its third seat (33:54 the second): C2.the_land('by_number_of_names') CALLED; 26:62's Levites 'no inheritance among the children of Israel' (C2.the_levites('no_inheritance')) the block the cities answer"}}
  - {{from: refuge, to: journeys, disposition: CALL, link: reference, carries: verdict,
     why: "{W}35:10's 'when you are crossing the Jordan to the land of Canaan' is 33:51's clause (the journeys runner's own row names 35:10 as the kin): JO.the_command('when_you_pass') CALLED; 35:8's rule 33:54's restatement"}}
  - {{from: refuge, to: borders, disposition: CALL, link: reference, carries: verdict,
     why: "{W}35:2's 'command the children of Israel' is the five seats' fifth (BO.the_land_and_its_fall('the_command') CALLED — Sifrei 1:2's one without expense); 35:5's four sides against 34's order (BO.the_four_sides('the_south') CALLED; the side-word's bare token at 34:3 and 35:5); the land of Canaan the standing party the pollution is written on (borders_declared at 34)"}}
  - {{from: refuge, to: zelophehad, disposition: CALL, link: reference, carries: verdict,
     why: "{W}35:29's 'a statute of judgment' is 27:11's phrase — the two Bible seats (ZL.inheritance_order('source_of_rule') CALLED; Onkelos 'a decree of judgment' at both); the daughters' court the Numbers 27 form"}}
  - {{from: refuge, to: gad_reuben, disposition: CALL, link: reference, carries: verdict,
     why: "{W}35:14's 'three cities beyond the Jordan' lie in the tribes' holdings 32:33 granted (Bezer for the Reubenites, Ramoth in Gilead for the Gadites, Golan in Bashan for the Manassites — Deuteronomy 4:43): GR.the_grant('three_parties' / 'land_held') CALLED; GR.the_cities the east's fourteen"}}
  - {{from: refuge, to: chukat, disposition: CALL, link: reference, carries: verdict,
     why: "{W}35:25's 'until the death of the high priest who was anointed with the holy oil' names the OFFICE'S HOLDER — Eleazar since 20:28 (the garments transferred, Aaron died: CK.edom_and_hor('succession') CALLED — the term's value at the sentence; his death Joshua 24:33 outside the Torah, the term OPEN by design)"}}
  - {{from: refuge, to: bamidbar, disposition: CALL, link: reference, carries: verdict,
     why: "{W}35:5's four sides run east, south, west, north — THE CAMP'S ORDER (Numbers 2:3, 10, 18, 25): CB.camp('sides') CALLED ('east judah, south reuben, west ephraim, north dan'); the bamidbar runner's own row CB.camp('distance') names 35:5 as the measure's seat"}}
  - {{from: refuge, to: primeval, disposition: CALL, link: reference, carries: verdict,
     why: "{W}35:33's 'except by the blood of him who shed it' is Genesis 9:6's clause ('who sheds the blood of man, by man shall his blood be shed') run as law — PR.cain('bloods_seats') CALLED and the blood_required HEAVEN entry on Noah read; 35:21-22's 'enmity' is Genesis 3:15's word (the serpent's — the noun's three Torah seats) FALSE by sense for the rule, a shared token only"}}
  - {{from: refuge, to: sanctions, disposition: CALL, link: reference, carries: verdict,
     why: "{W}35:34's 'you shall not defile the land in which you dwell' against Leviticus 18:25-28's land that was defiled and vomits its inhabitants (the sanctions runner's cell the_land_vomits_its_inhabitants — 18:25, 18:28, 20:22 — CALLED); Shevuot 7b:7 names bloodshed an impurity by 35:34 beside the unions (18:30) and Molech (20:3); SA.severity('orders') the four deaths' two orders"}}
  - {{from: refuge, to: priesthood, disposition: CALL, link: reference, carries: verdict,
     why: "{W}35:25's 'the high priest who was anointed with the holy oil' is Leviticus 21:10's definition ('the priest greater than his brothers, on whose head the anointing oil was poured'): PH.family('greatness' / 'nezer') CALLED — the anointed against the many-garmented (Mishnah Horayot 3:4; Makkot 11a:12's three high priests)"}}
  - {{from: refuge, to: balak, disposition: FALSE, link: none,
     why: "{W}35:11's 'you shall APPOINT for yourselves cities' (the causative of the meet-root) shares its root with Balaam's 'perhaps the LORD will MEET me' (23:4, 16) and Abraham's servant's 'cause it to happen' (Genesis 24:12; 27:20) — a homograph by sense: the designation of cities is no meeting; declared FALSE for the rule"}}
  - {{from: sequence, to: refuge, disposition: CALL, link: none,
     why: "{W}the sequential run's REGISTRATION edge — ('cold_run_refuge', 'law_refuge') in DAEMON_ORDER (the runner compiles no verse: link none, O4's license)"}}
'''
    a = "  - {from: sequence, to: borders, disposition: CALL, link: none,"
    i = text.index(a); j = text.index('\n', text.index('why:', i)) + 1
    text = text[:j] + edges + text[j:]
    open(path, 'w', encoding='utf-8').write(text)
dep = yaml.safe_load(open(path, encoding='utf-8'))
n_ref = sum(1 for e in dep['edges'] if e['from'] == 'refuge')
assert 'refuge' in dep['spans'] and n_ref == 16, n_ref
print('dependency: span + 17 edges (refuge 16 — fifteen CALL + one FALSE — and the registration); the pointers after the gate\'s print')
# ---- the installation probe's count ----
path = f"{ROOT}/World/step9/installation_probes.py"
text = open(path, encoding='utf-8').read()
if "len(real) == 61 and all(" in text:
    text = text.replace("len(real) == 61 and all('given_at' in d and 'installed_by' in d for d in real.values())   # THE NUMBERS WALK 14b (2026-09-13): 60 -> 61, law_borders",
                        "len(real) == 62 and all('given_at' in d and 'installed_by' in d for d in real.values())   # THE NUMBERS WALK 15b (2026-09-13): 61 -> 62, law_refuge (installed_by boot — a law in the divine voice in the plains of Moab, the class named); 14b: 60 -> 61, law_borders")
    open(path, 'w', encoding='utf-8').write(text)
assert "len(real) == 62" in open(path, encoding='utf-8').read()
print('installation_probes I5: 62')
