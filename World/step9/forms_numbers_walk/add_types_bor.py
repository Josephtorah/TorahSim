import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE NUMBERS WALK sitting 14b — THE COMPILE OF THE BORDERS (2026-09-13; World/step9/NUMBERS_WALK.md "Sitting 14b"): THE TYPES FIRST — THREE
# tape kinds (the borders commanded 34:1-12, Moses' restatement to the nine and a half 34:13-15, the dividers named 34:16-29), TWO case-form
# kinds for the exam's scene, TWO new effects (borders_declared, dividers_named — status, the ink's own words at 34:2 and 34:17), NO registry
# row (the chapter writes on the_land_of_canaan and the_dividers_of_the_land, both standing; the ten princes rows in a table, not entities),
# the 61st daemon's block (law_borders, given_at Num 34:1, installed_by BOOT with the class named — a law in the divine voice relayed at 34:13
# in 36:5's form), the functions block, the dependency span and edges (the pointers after the gate's print), the installation probe's count.
# The `he` is cut from the pointed DB text by FINDING the phrase's tokens (never a typed index); the witnesses the plain consonantal verses.
# Idempotent (add_types_jou.py's form).
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
CORPUS = "num_34_borders (STEP_Nm_34_1 through STEP_Nm_34_29; claims MS34A-01 through MS34A-13)"
SUB = "submitted by cold_run_borders.py [subjects: %s] (the narrative scene, THE NUMBERS WALK 14b); re-submitted on the sequential tape by cold_run_sequence.py; consumed by law_borders (cold_run_borders.py) -> %s"
CASE = "submitted by cold_run_borders.py [subjects: the exam's persons] (the wrap's scene); consumed by law_borders (cold_run_borders.py) -> %s"
INK_ALL = "Num 34:1-29; Onkelos Num 34:1-29 (the lot's verb 'be divided' at 34:2 — one Aramaic verb with 26:53-56; 'Rekem Geah' at 34:4; the west split from the sea at 34:6; 'direct yourselves' at 34:7-10; Hor spelled two ways at 34:7-8; 'reach' at 34:11 against 'blot' at 5:23; 'the sea of Gennesar'; 'great' for the sea and the prince; one Aramaic tribe-word); the Sifrei on Numbers SILENT (no piska from 31:25 to 35:8 — found by position; 1:2 cites 34:2 as the one 'command' without expense); Num 26:52-56 (the lot — cited at 34:2 and 34:13, never rewritten), 32:28-33 (the commission's charge to the same triad; the grant's three transfers), 33:51-54 (the entry clause; the lot restated), 13:2, 13:6, 13:21, 14:24, 14:30, 14:38 (the spies' doubling, Caleb's five words, the spies' range, the two survivors), 1:5-15, 1:10 (the princes' roll; Ammihud), 7:11 (the dedication's doubling), 17:21 (the rods'), 20:22-28 (the first Mount Hor), 27:18-23 (Joshua's commission — uncompiled), 5:23 (the blotting verb — a homograph by sense), 36:5 (the relay's form); Exod 27:9, 27:13 (the court's south and east sides — the side-word and 'eastward toward the sunrise'); Gen 14:3 (the Salt Sea's identity clause), 15:18 (the covenant's river); Exod 23:31, Deut 1:7, 11:24, Josh 1:4 (the promised extents — none in the chapter); Josh 13:7, 13:32, 14:1-2, 15:1-12, 17:4, 17:14, 18:20, 19:49-51, 21:5-8, 22:14 (the runs); Ezek 47:13-20, 48:1, 28 (the prophet's borders — north, east, south, west); 1 Kgs 8:65; 2 Kgs 14:25; Babylonian Talmud Gittin 8a, Kiddushin 36b-37a, 42a, Bekhorot 55a, Sanhedrin 16a, 91a, Bava Batra 117a-122a; Mishnah Gittin 1:1-2, Sheviit 6:1, 9:2; Tosefta Sheviit 4:4, 4:12"
KINDS = [
 ("borders_commanded", "speech",
  "the borders commanded — 'and the LORD spoke to Moses, saying: command the children of Israel and say to them: when you are coming into the land Canaan, THIS IS THE LAND THAT SHALL FALL TO YOU AS AN INHERITANCE, the land of Canaan BY ITS BORDERS; and your south side shall be from the wilderness of Zin on the hands of Edom … and its goings-out shall be at the Salt Sea; this shall be your land by its borders round about' (Num 34:1-12): THE SPEC OF THE LAND'S EXTENT — four sides in the ink's order (south 34:3-5, west 34:6, north 34:7-9, east 34:10-12), the Salt Sea at both ends of the loop, 'by its borders' the inclusio (34:2, 34:12); the lot's verb 'shall fall' (this one Torah seat with the inheritance; Onkelos 'be divided'); the border's own verb 'you shall mark out' three Bible seats all here; the goings-out word the Torah's five all here; the second Mount Hor (34:7-8; the chukat runner's two-Hors row); Judah's south border (Joshua 15:1-4) the run of 34:3-5; Ezekiel 47:15-20 the kin in another order; THE VALUE THE FOUR SIDES — the DATA row the_four_sides built from the DB (the named points by side with their seats), written as ONE STATUS on the land of Canaan (the border the land's property — 'the land of Canaan by its borders'); nothing on the people: 'shall fall TO YOU' is the lot's debit already open (26:52-56), cited",
  HE(34, 1, 12, "and the LORD spoke to Moses, saying"), WIT(34, 1, 12), INK_ALL, CORPUS,
  SUB % ("israel", "borders_declared on the_land_of_canaan (the STATUS valued the four sides and their points — the standing place entity written on for the first time since Genesis's famines); no new entity"), ["sides", "points", "first", "last", "by_its_borders"]),
 ("moses_commanded_the_nine_and_a_half", "speech",
  "Moses' restatement to the nine and a half — 'and Moses commanded the children of Israel, saying: this is the land which you shall inherit by lot, which the LORD commanded to give to the nine tribes and the half tribe; for the tribe of the sons of the Reubenite by their fathers' house and the tribe of the sons of the Gadite by their fathers' house and the half tribe of Manasseh have taken their inheritance; the two tribes and the half tribe have taken their inheritance beyond the Jordan at Jericho, eastward toward the sunrise' (Num 34:13-15): THE RELAY of 34:1-12 to the people in the form 36:5 uses ('and Moses commanded the children of Israel' — the phrase's two Torah seats, 36:5's the installing act command_relayed at THE TENT sitting 4: the D2 question of the second pass); the nine and the two the parser's [9] and [2] with the two halves = twelve; 'nine' in the construct three Bible seats, all the nine tribes (Joshua 13:7, 14:2 and here); ONE TRIBE-NOUN — the staff-word eighteen times in the chapter, the other never (32:33's the neighbour); 'have taken their inheritance' four Bible seats, always the two and a half (34:14, 34:15, Joshua 13:8, 18:7) — A RUN CITATION of the Gad runner's grant on the tape (32:33's three holding_given transfers, 110,580 off the second census by CALL): the line WRITES NOTHING — the ledger's own lines are read at the checkpoint; the lot's debit cited (C2.the_land('by_lot') VIA second_census); Joshua 14:2's receipt 'as the LORD commanded by the hand of Moses, to the nine tribes and the half tribe' quotes 34:13's six words OUTSIDE THE TORAH — the readback's; no receipt in the chapter",
  HE(34, 13, 15, "and Moses commanded the children of Israel, saying: this is the land which you shall inherit by lot"), WIT(34, 13, 15), INK_ALL, CORPUS,
  SUB % ("moses", "NOTHING (the empty watch — the relay's own exemption: the grant's three transfers and the lot's open debit are read, not rewritten)"), ["to", "nine", "two", "halves", "by_lot"]),
 ("dividers_named", "speech",
  "the dividers named — 'and the LORD spoke to Moses, saying: these are the names of the men who shall divide the land for you: Eleazar the priest and Joshua son of Nun; and one prince, one prince from a tribe you shall take to divide the land; and these are the names of the men: for the tribe of Judah, Caleb son of Jephunneh; and for the tribe of the sons of Simeon, Shemuel son of Ammihud; … and for the tribe of the sons of Naphtali a prince, Pedahel son of Ammihud; these are they whom the LORD commanded to divide to the children of Israel in the land of Canaan' (Num 34:16-29): THE COMMISSION'S ROSTER — the party 32:28 charged as a body ('Eleazar the priest, and Joshua son of Nun, and the heads of the fathers of the tribes' — Joshua 14:1's triad word for word) gets its names: 'these are the names of the men' the rosters' heading (13:16 the spies', 34:17 and 34:19 the dividers'); 'Eleazar the priest and Joshua son of Nun' as one phrase three Bible seats (34:17; Joshua 14:1, 19:51 — the runs); THE DISTRIBUTIVE DOUBLING 'one prince, one prince from a tribe' (the parser's [1, 1] — 13:2's spies, 7:11's dedication, 17:21's rods; Joshua 3:12, 4:2, 4:4, 22:14 the runs); THE ONE ROOT IN THREE STEMS — 'inherit' the reflexive at 34:13, the plain at 34:17-18, the intensive at 34:29 (its other three Bible seats Joshua's runs: 13:32, 14:1, 19:51), the object switching from the land to the people; CALEB'S FIVE WORDS (34:19 = 13:6 — the spy's line at the dividers'); the two survivors the only persons of the spies' roster here; no prince of chapter 1 among the ten; Ammihud three tribes' fathers' name; eight names nowhere else; Shemuel the prophet's name's first seat; the title dropped for three; the order matching no other roster of the Torah (computed on sixteen lists); 34:29's closer without a receipt — the receipt Joshua 14:2's, outside the Torah; THE WRITES — dividers_named (the STATUS valued the twelve) and commanded (the DEBIT: divide the inheritance to the children of Israel in the land of Canaan — OPEN BY DESIGN to Joshua 14:1 and 19:51, the readback's) on the_dividers_of_the_land, whose Gilead charge of 32:28-30 stands OPEN beside them; AND TWELVE NAMED ROWS in the population table (grain named, as_of Num 34:17-29 — the register gate's Num 34 seat PAID: the first register reached since the table was built at 26); no entity for the ten princes (names in a value, rows in a table)",
  HE(34, 16, 29, "and the LORD spoke to Moses, saying"), WIT(34, 16, 29), INK_ALL, CORPUS,
  SUB % ("israel", "dividers_named on the_dividers_of_the_land (the STATUS valued the twelve — Eleazar the priest, Joshua son of Nun, the ten princes by tribe) and commanded on the_dividers_of_the_land (the DEBIT divide_the_inheritance_to_the_children_of_israel_in_canaan, OPEN to Joshua's runs) + twelve population rows (grain named); no new entity"), ["dividers", "per_tribe"]),
 ("borders_case", "case", "the exam's rows on the borders (Num 34:1-12 — Gittin 8a:4-7 on 34:6 the sea within the border or the islands by the string; Bekhorot 55a:10 on 34:12 one border round about; 55a:14 on 34:15 the Jordan Canaan's; Sanhedrin 91a:6 on 34:2 the Canaanites' claim; Mishnah Gittin 1:2 the bills' three points — Rekem the translation's Kadesh-barnea; Mishnah Sheviit 6:1, 9:2 and the Tosefta 4:4 the three lands; Kiddushin 36b:8-37a:6 the land-bound commandments): the sea as a border, the Jordan as a border, the heading as a title claim, the shelf's own border points, the borders' legal reach",
  HE(34, 6, 7, "and the west border: you shall have the great sea and its border; this shall be your west border"), WIT(34, 2, 12), INK_ALL, CORPUS, CASE % "borders_declared / accepted / exempt (the exam's persons)", ["person", "ask"]),
 ("dividers_case", "case", "the exam's rows on the dividers (Num 34:13-29 — Kiddushin 42a:6-8 on 34:18 the law of agency asked and the steward answered; Bava Batra 122a:4-6 the lottery's picture — Eleazar with the Urim, Joshua and all Israel, the two receptacles, Naphtali's boundary Ginnosar the translation's name of 34:11's sea; 122a:12 'only' excludes Joshua and Caleb — their own portions not by lot; 118a:4 Joshua answering Joseph's claim; 117b:2, 118b:3 the spies' portions; Sanhedrin 16a:2-3 the seventy-one at the first division, 16a:16-17 Joshua's commission verse; Bava Batra 121b:12-122a:1 by tribes): the princes as agents or stewards, the dividers at the lot, the two dividers' own portions, the court that owes the daughters' and Caleb's holdings",
  HE(34, 17, 18, "these are the names of the men who shall divide the land for you: Eleazar the priest and Joshua son of Nun"), WIT(34, 13, 29), INK_ALL, CORPUS, CASE % "commanded / dividers_named / accepted / exempt (the exam's persons)", ["person", "ask"]),
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
for e in ('commanded', 'accepted', 'exempt', 'holding_given', 'holding_owed', 'journeys_recorded'):
    assert e in fx, e
print('  34:2 plain:', LV('Num', 34, 2)); print('  34:17 plain:', LV('Num', 34, 17))
HE_FALL = PHRASE(34, 2, ['זאת', 'הארץ', 'אשר', 'תפל', 'לכם', 'בנחלה', 'ארץ', 'כנען', 'לגבלתיה'])
HE_NAMES = PHRASE(34, 17, ['אלה', 'שמות', 'האנשים', 'אשר', 'ינחלו', 'לכם', 'את', 'הארץ'])
NEW = [
 ('borders_declared', 'status',
  "the borders declared — the STATUS the spec of the land's extent writes ON THE LAND: 'this is the land that shall fall to you as an inheritance, the land of Canaan BY ITS BORDERS' (Num 34:2) … 'this shall be your land by its borders round about' (34:12) — the value THE FOUR SIDES in the ink's order (south 34:3-5 from the wilderness of Zin on the hands of Edom to the brook of Egypt and the sea; west 34:6 the great sea and its border; north 34:7-9 from the great sea by Mount Hor and Lebo-hamath to Zedad, Ziphron and Hazar-enan; east 34:10-12 from Hazar-enan by Shepham, Riblah, the shoulder of the sea of Chinnereth and the Jordan to the Salt Sea) with their named points (the DATA row the_four_sides built from the DB — Joshua 15:1-4 Judah's run of the south, Ezekiel 47:15-20 the kin) and the two Mount Hors (the chukat runner's row); the border the LAND's property — 'by its borders' the inclusio (34:2, 34:12; Joshua 18:20, 19:49 the closers), so the write is on the land of Canaan, not the people, whose lot's debit (26:52-56) stands open and is cited; the border-word sixteen times in the chapter, half of Numbers' thirty-two; the shelf's readings of the sides as rules — the sea within the border or the islands by the string (Gittin 8a:4-7), one border round about (Bekhorot 55a:10), the Jordan Canaan's (55a:14)",
  HE_FALL + " (this is the land that shall fall to you as an inheritance, the land of Canaan by its borders — Num 34:2)",
  "Num 34:2 ('this is the land that shall fall to you as an inheritance, the land of Canaan by its borders' — 'shall fall' with the inheritance one Torah seat; 'by its borders' the token's two Bible seats 34:2, 34:12), 34:3-12 (the four sides — twenty 'and it shall' verbs, 'to you' twelve times, 'its goings-out' the Torah's five seats all here, 'you shall mark out' three Bible seats all here), 34:12 ('this shall be your land by its borders round about'); Onkelos 34:2 ('be divided' — one verb with 26:53-56), 34:6 (the west and the sea split), 34:7-8 (Hor two ways), 34:11 ('reach'; 'the sea of Gennesar'); Josh 15:1-4, 15:12 (Judah's border the run), 18:20, 19:49 ('by its borders' the closers); Ezek 47:13-20, 48:1, 28 (the prophet's four sides in another order); Num 13:21 (the spies' range — 'from the wilderness of Zin' and 'Lebo-hamath' each at two seats: 13:21 and this chapter), 20:22 (the first Mount Hor); Gen 14:3 (the Salt Sea's identity clause); 1 Kgs 8:65 ('from Lebo-hamath to the brook of Egypt' — the kingdom's measure by the chapter's two ends); Babylonian Talmud Gittin 8a:4-7, Bekhorot 55a:10, 55a:14; Mishnah Gittin 1:2; Mishnah Sheviit 6:1, 9:2; Tosefta Sheviit 4:4",
  "num_34_borders (STEP_Nm_34_1 through STEP_Nm_34_12; the claims MS34A-01 … MS34A-05, MS34A-11, MS34A-12)",
  "cold_run_borders.py (F1 the_land_and_its_fall — the heading's cell; F2 the_four_sides — the sides' cell and the DATA row; the exam kind borders_case)"),
 ('dividers_named', 'status',
  "the dividers named — the STATUS the commission writes on the party 32:28 charged as a body: 'these are the names of the men who shall divide the land for you: Eleazar the priest and Joshua son of Nun; and one prince, one prince from a tribe you shall take to divide the land' (Num 34:17-18) — the value THE TWELVE (Eleazar the priest, Joshua son of Nun, and the ten princes by tribe: Judah Caleb son of Jephunneh, Simeon Shemuel son of Ammihud, Benjamin Elidad son of Chislon, Dan Bukki son of Jogli, Manasseh Hanniel son of Ephod, Ephraim Kemuel son of Shiphtan, Zebulun Elizaphan son of Parnach, Issachar Paltiel son of Azzan, Asher Ahihud son of Shelomi, Naphtali Pedahel son of Ammihud — 34:19-28) written beside the DEBIT the closer writes ('these are they whom the LORD commanded to divide to the children of Israel in the land of Canaan', 34:29 — OPEN to Joshua 14:1 and 19:51, the runs outside the Torah); the rosters' heading 'these are the names of the men' (13:16 the spies', 34:17 and 34:19 the dividers'); the triad's three seats (34:17; Joshua 14:1, 19:51); the distributive doubling of the spies, the dedication and the rods; Caleb's five words from 13:6; the two survivors the only spies here; no prince of chapter 1; the order matching no other roster; AND the roll's persons enter the population table as twelve named rows (grain named, as_of Num 34:17-29 — the register gate's Num 34 seat paid: 8b's law 'the persons the roll names enter the table'); the shelf's readings — the princes as agents or the court's steward (Kiddushin 42a:6-8), the lottery's picture (Bava Batra 122a:4-6), 'only' excludes Joshua and Caleb (122a:12), the seventy-one at the first division (Sanhedrin 16a:2-3)",
  HE_NAMES + " (these are the names of the men who shall divide the land for you — Num 34:17)",
  "Num 34:17 ('these are the names of the men who shall divide the land for you: Eleazar the priest and Joshua son of Nun' — the triad's phrase three Bible seats), 34:18 ('one prince, one prince from a tribe' — the parser's [1, 1]; 'to divide the land' the plain stem), 34:19-28 (the ten by tribe — Caleb's five words = 13:6's; eight names at one seat each; Ammihud at 34:20 and 34:28 with 1:10; the title at seven rows), 34:29 ('these are they whom the LORD commanded to divide' — the intensive stem, its other three seats Joshua 13:32, 14:1, 19:51); Num 32:28-30 (the same triad charged for Gilead — the dividers' first write), 13:2, 13:6, 13:8, 13:16 (the spies' roster and its doubling), 7:11, 17:21 (the doublings), 1:5-15 (the princes' roll — none shared), 14:24, 14:30, 14:38, 26:65 (the two survivors), 27:18-23 (Joshua's commission — uncompiled); Josh 14:1-2, 17:4, 17:14, 19:49-51, 21:1, 22:14 (the runs; Caleb's Hebron 14:13; the daughters' claim before Eleazar and Joshua 17:4; 19:50 Joshua's Timnath-serah); Babylonian Talmud Kiddushin 42a:6-8, Bava Batra 117b:2, 118a:4, 118b:3, 122a:4-6, 122a:12, Sanhedrin 16a:2-3, 16a:16-17",
  "num_34_borders (STEP_Nm_34_16 through STEP_Nm_34_29; the claims MS34A-06 … MS34A-10, MS34A-13)",
  "cold_run_borders.py (F4 the_dividers — the commission's cell; F5 the_roster — the roll and the DATA rows; the exam kind dividers_case)"),
]
added = 0
for name, op, en, he, ink, corpus, exam in NEW:
    if name in fx: continue
    text = text.rstrip('\n') + '\n' + f"  {name}:\n    en: {q(en)}\n    he: {q(he)}\n    ledger_op: {op}   # THE NUMBERS WALK 14b (2026-09-13): the borders' compile — {name}\n    ink: {q(ink)}\n    corpus: {q(corpus)}\n    exam: {q(exam)}\n"
    added += 1
open(path, 'w', encoding='utf-8').write(text)
fx = yaml.safe_load(open(path, encoding='utf-8'))['effects']
assert all(n in fx for n, *_ in NEW) and fx['borders_declared']['ledger_op'] == 'status' and fx['dividers_named']['ledger_op'] == 'status'
print('effects: %d added (registry %d); the he found in the verses: %s | %s' % (added, len(fx), HE_FALL, HE_NAMES))
# ---- NO registry row (measured: no party written on for the first time — the land of Canaan and the dividers standing) ----
reg = yaml.safe_load(open(f"{ROOT}/logic/corpus/entity_registry.yaml", encoding='utf-8'))
ids = {e['id'] for e in reg['entities']}
assert all(x in ids for x in ('moses', 'israel_people', 'the_land_of_canaan', 'the_dividers_of_the_land', 'eleazar_son_of_aaron', 'yehoshua', 'caleb')), 'the written-on and the named parties must stand'
print('entities: 0 added (registry %d) — the_land_of_canaan and the_dividers_of_the_land standing' % len(reg['entities']))
# ---- the daemon block + the functions block (daemon_dispositions.yaml) ----
path = f"{ROOT}/World/step9/daemon_dispositions.yaml"
text = open(path, encoding='utf-8').read()
if '  law_borders:' not in text:
    block = '''  law_borders:
    file: cold_run_borders.py
    wraps: borders
    given_at: Num 34:1
    installed_by: boot   # THE NUMBERS WALK 14b (2026-09-13): A LAW IN THE DIVINE VOICE — 'and the LORD spoke to Moses, saying' at 34:1 and 34:16 (the same five words, no place named; 35:1 adds the plains of Moab) — RELAYED to the people by Moses at 34:13 ('and Moses commanded the children of Israel, saying' — the phrase's two Torah seats, 34:13 and 36:5, and 36:5's is the installing act command_relayed of THE TENT sitting 4): the walk's standing setting for a law spoken at its verse (law_shelach, law_korach, law_chukat, law_balak, law_second_census, law_journeys the same), the relay's form named in the runner's DATA row the_relay_form; THE SECOND PASS (D2) decides whether a relay in this form installs (COMPILE_DEBT.md's sitting-14b box)
    watches:
      borders_commanded: [borders_declared]                                          # 34:1-12: the four sides — ONE status on the land of Canaan valued the sides and their points (the DATA row); nothing on the people (the lot's debit cited)
      moses_commanded_the_nine_and_a_half: []                                        # 34:13-15: the relay — NO write (the grant's three transfers and the lot's open debit read at the checkpoint; Joshua 14:2's receipt outside the Torah)
      dividers_named: [dividers_named, commanded]                                    # 34:16-29: the roster — the STATUS valued the twelve and the DEBIT to divide (OPEN to Joshua 14:1, 19:51) on the dividers of the land; twelve named rows in the population table (the register seat paid)
      borders_case: [borders_declared, accepted, exempt]                             # the exam's rows on the borders — the sea, the Jordan, the title claim, the shelf's points, the land-bound rule
      dividers_case: [commanded, dividers_named, accepted, exempt]                   # the exam's rows on the dividers — agency and the steward, the lottery's picture, 'only' excludes, the seventy-one, the court that owes
'''
    i = text.index('  law_census:')
    text = text[:i] + block + text[i:]
if '\n  borders:   # THE NUMBERS WALK 14b' not in text:
    fb = '''  borders:   # THE NUMBERS WALK 14b (2026-09-13)
    the_land_and_its_fall: {status: WRAPPED, by: law_borders}
    the_four_sides: {status: WRAPPED, by: law_borders}
    moses_restatement: {status: WRAPPED, by: law_borders}
    the_dividers: {status: WRAPPED, by: law_borders}
    the_roster: {status: WRAPPED, by: law_borders}
'''
    i = text.index('  journeys:   # THE NUMBERS WALK 13b (2026-09-12)')
    j = text.index('\n  pre_sinai:', i)
    text = text[:j + 1] + fb + text[j + 1:]
open(path, 'w', encoding='utf-8').write(text)
dd = yaml.safe_load(open(path, encoding='utf-8'))
assert 'law_borders' in dd['daemons'] and 'borders' in dd['functions'], (list(dd)[:5])
print('daemons: %d (law_borders %s); functions blocks: %d' % (len(dd['daemons']), 'law_borders' in dd['daemons'], len(dd['functions'])))
# ---- the dependency span + edges (the POINTERS after the gate's print) ----
path = f"{ROOT}/World/step9/dependency_dispositions.yaml"
text = open(path, encoding='utf-8').read()
if '\n  borders:' not in text.split('\nedges:')[0]:
    a = "  journeys:    [[Num, 33, 1, 56]]"
    i = text.index(a); j = text.index('\n', i)
    text = text[:j + 1] + "  borders:     [[Num, 34, 1, 29]]   # THE NUMBERS WALK 14b (2026-09-13; NUMBERS_WALK.md \"Sitting 14b\"): the borders — the land's extent as one status on the land (the four sides a data row), Moses' restatement to the nine and a half (a run citation of the grant), the dividers named (a status, a debit and twelve population rows on the standing party)\n" + text[j + 1:]
    edges = '''  - {from: borders, to: second_census, disposition: CALL, link: reference, carries: verdict,
     why: "THE NUMBERS WALK 14b (2026-09-13) | 34:2's 'shall FALL to you as an INHERITANCE' and 34:13's 'you shall INHERIT BY LOT' are 26:52-56's own words (the lot's debit divide_the_land OPEN on israel_people since 26:52-56 — cited at 33:54 and here, never rewritten; CW3 asserts ONE entry): C2.the_land('by_lot' / 'lots_mouth' / 'only_excludes' / 'thirteen_tribes' / 'possession_before_assignment') and C2.DATA['division_by'] CALLED — the lot's mouth the Urim before Eleazar (Bava Batra 122a:3-6), 'only' excluding the two dividers' own portions (122a:12): the shared words the reference"}
  - {from: borders, to: gad_reuben, disposition: CALL, link: reference, carries: verdict,
     why: "THE NUMBERS WALK 14b (2026-09-13) | 34:14-15's 'the two tribes and the half tribe HAVE TAKEN THEIR INHERITANCE beyond the Jordan at Jericho' is a RUN CITATION of 32:33's grant on the tape (holding_given on the_sons_of_gad, the_sons_of_reuben and the_half_tribe_of_manasseh — CW4 reads the three entries; the line writes nothing), and 34:17's 'Eleazar the priest and Joshua son of Nun' the triad 32:28 charged (the_dividers_of_the_land's Gilead charge OPEN beside this chapter's two writes): GR.the_grant('three_parties' / 'the_count' / 'not_by_lot' / 'land_held') and GR.the_acceptance_and_the_charge('the_commission') CALLED — the shared names the reference"}
  - {from: borders, to: shelach, disposition: CALL, link: reference, carries: verdict,
     why: "THE NUMBERS WALK 14b (2026-09-13) | 34:19's 'for the tribe of Judah, Caleb son of Jephunneh' is 13:6's five words; 34:3's 'from the wilderness of Zin' and 34:8's defective 'Lebo-hamath' are 13:21's (each at exactly two seats — the spies walked the border's length); 34:18's 'one prince, one prince from a tribe' 13:2's doubling; the two survivors (14:24, 14:30, 14:38) the only spies among the dividers: SL.spies('one_per_tribe' / 'fourth_order' / 'joshua_caleb_equal') and SL.decree('exceptions' / 'caleb_entitlement' / 'spies_portions') CALLED (Caleb's holding_owed OPEN on the tape since 14:24 — paid at Joshua 14:13 before the dividers, CW7): the shared names the reference"}
  - {from: borders, to: chukat, disposition: CALL, link: reference, carries: verdict,
     why: "THE NUMBERS WALK 14b (2026-09-13) | 34:7-8's MOUNT HOR on the north border is the SECOND Mount Hor — the chukat runner's DATA row two_mount_hors names this chapter ('Aaron's at Edom's border, the northern border's (34:7-8)'): CK.edom_and_hor('two_mount_hors') CALLED; the twelve Torah seats of the name (ten Aaron's at 20:22-33:41, two the border's) counted in the runner; the tape's marker at 20:22 and the encamped_at at Mount Hor the first Hor's (CW7): the shared name the reference, the two places the row's own"}
  - {from: borders, to: bamidbar, disposition: CALL, link: reference, carries: verdict,
     why: "THE NUMBERS WALK 14b (2026-09-13) | 34:19-28's roster against 1:5-15's roll — NO PRINCE OF CHAPTER 1 among the ten (computed on the names), one father's name shared (AMMIHUD — Ephraim's Elishama at 1:10, here Simeon's Shemuel and Naphtali's Pedahel), the tribes' order matching neither the roll's nor the count's (CB.census('orders') — 'three orders in the portion'): CB.census('orders' / 'by_names') and CB.TRIBES CALLED; the roster form 'for the tribe of X, N son of F' the roll's: the shared form the reference"}
  - {from: borders, to: naso, disposition: CALL, link: reference, carries: verdict,
     why: "THE NUMBERS WALK 14b (2026-09-13) | 34:18's 'one prince, one prince' is 7:11's 'one prince per day, one prince per day' (the distributive doubling — NS.dedication('per_day') CALLED; the twelve princes' names NS.NAMES against the ten: none shared); AND 34:11's 'and it shall REACH the shoulder of the sea of Chinnereth' is the SAME TOKEN as the sotah's 'and he shall BLOT them out into the water' (5:23) — one pointing at four Bible seats (5:23, 34:11, Deuteronomy 29:19, Isaiah 25:8): A HOMOGRAPH BY SENSE — the border reaches, the priest blots; Onkelos 'reach' here, 'blot' there — NS.sotah('scroll_erasure') READ to name the other sense, FALSE for the sotah's rule (the box (g)'s FALSE carried inside this edge, the naso runner one module)"}
  - {from: borders, to: korach, disposition: CALL, link: reference, carries: verdict,
     why: "THE NUMBERS WALK 14b (2026-09-13) | 34:18's doubling is 17:21's 'a staff for one prince, a staff for one prince … twelve staffs' (the parser's [1, 1, 12]; KR.STAFFS_21): KR.plague_and_staffs('staffs_count') CALLED — the princes' staffs by tribe the commission's princes by tribe: the shared doubling the reference"}
  - {from: borders, to: zelophehad, disposition: CALL, link: reference, carries: verdict,
     why: "THE NUMBERS WALK 14b (2026-09-13) | 34:17's 'Eleazar the priest and Joshua son of Nun' are 27:19-22's pair at Joshua's commission ('before Eleazar the priest and before all the congregation' — 27:12-23 UNCOMPILED, 8b's owed line), and the zelophehad runner's own token table already reads 34:17 ('shall apportion — Eleazar and Joshua, THE COURT THAT OWES THE HOLDING'): the daughters' holding_owed OPEN on the tape (27:1-4) is paid at Joshua 17:4 'before Eleazar the priest and before Joshua' — ZL.the_daughters('the_run' / 'reach') and ZL.inheritance_order('ten_parts' / 'land_status') CALLED (Bava Batra 118b:8's ten parts the dividers' run at Joshua 17): the shared pair the reference"}
  - {from: borders, to: journeys, disposition: CALL, link: reference, carries: verdict,
     why: "THE NUMBERS WALK 14b (2026-09-13) | 34:2's 'when you are coming into the land Canaan' is 33:51's entry clause ('when you pass over the Jordan into the land of Canaan' — the law's trigger) and 34:13's 'you shall inherit by lot' 33:54's restatement (the reflexive stem at both — 'you shall inherit' the Hitpael's Torah seats Leviticus 25:46, 32:18, 33:54, 34:13): JO.the_command('the_lot_restated' / 'when_you_pass' / 'possess_and_dwell') CALLED — the lot's debit cited at 33:54 and here the same way (no second entry): the shared words the reference"}
  - {from: sequence, to: borders, disposition: CALL, link: none,
     why: "THE NUMBERS WALK 14b (2026-09-13) | the sequential run's REGISTRATION edge — ('cold_run_borders', 'law_borders') in DAEMON_ORDER (the runner compiles no verse: link none, O4's license)"}
'''
    a = "  - {from: sequence, to: journeys, disposition: CALL, link: none,"
    i = text.index(a); j = text.index('\n', text.index('why:', i)) + 1
    text = text[:j] + edges + text[j:]
    open(path, 'w', encoding='utf-8').write(text)
dep = yaml.safe_load(open(path, encoding='utf-8'))
assert 'borders' in dep['spans'] and sum(1 for e in dep['edges'] if e['from'] == 'borders') == 9, sum(1 for e in dep['edges'] if e['from'] == 'borders')
print('dependency: span + 10 edges (borders 9 + the registration); the pointers after the gate\'s print')
# ---- the installation probe's count ----
path = f"{ROOT}/World/step9/installation_probes.py"
text = open(path, encoding='utf-8').read()
a = "len(real) == 60 and all('given_at' in d and 'installed_by' in d for d in real.values())   # THE NUMBERS WALK 13b (2026-09-12): 59 -> 60, law_journeys"
if a in text:
    text = text.replace(a, "len(real) == 61 and all('given_at' in d and 'installed_by' in d for d in real.values())   # THE NUMBERS WALK 14b (2026-09-13): 60 -> 61, law_borders (installed_by boot — a law in the divine voice relayed at 34:13 in 36:5's form, the class named); 13b: 59 -> 60, law_journeys")
    open(path, 'w', encoding='utf-8').write(text)
assert "len(real) == 61" in open(path, encoding='utf-8').read()
print('installation_probes I5: 61')
