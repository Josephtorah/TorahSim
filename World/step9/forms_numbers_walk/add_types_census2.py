#!/usr/bin/env python3
# THE NUMBERS WALK sitting 8b — THE COMPILE OF THE SECOND CENSUS (2026-09-11; World/step9/NUMBERS_WALK.md "Sitting 8b"): THE TYPES FIRST —
# five new kinds on the tape (the command, the roll, the land's law, the Levites' roll, the two rolls compared), five CASE kinds for the exam's
# scene, NO new effect (commanded, counted, exempt, accepted, holding_owed, souls_counted, inheritance_barred reused), NO registry row (the
# tribes and the families are not entities; the persons the roll names enter the TABLE, not the registry), the 55th daemon's block with the
# two SHARED kinds (census_taken, levites_counted — row-only consumption), the functions block, the dependency span and edges, the
# installation probe's count, the shared kinds' tape lines appended. The `he` is the whole verse from the pointed DB text (cantillation
# stripped), the witnesses the plain consonantal verses — no anchor word typed. Idempotent (add_types_balak.py's form).
import re, sqlite3, yaml
ROOT = "<repo-old>"
db = sqlite3.connect(f"file:{ROOT}/elijah_docket/tanakh.sqlite?mode=ro", uri=True)
def words(book, ch, vs):
    return [r[0] for r in db.execute("SELECT w.he FROM words w JOIN verses v ON w.verse_id=v.id WHERE v.book=? AND v.chapter=? AND v.verse=? ORDER BY w.idx", (book, ch, vs)).fetchall()]
def PV(book, ch, vs):
    ws = words(book, ch, vs); assert ws, (book, ch, vs)
    return ' '.join(''.join(c for c in w if c != '/' and not (0x0591 <= ord(c) <= 0x05AF)) for w in ws)
def LV(book, ch, vs):
    return ' '.join(''.join(c for c in w if c != '/' and not (0x0591 <= ord(c) <= 0x05C7)) for w in words(book, ch, vs))
q = lambda s: '"' + s.replace('\\', '\\\\').replace('"', '\\"') + '"'
N = 'Num'
def HE(ch, lo, hi, en, cap=6):
    vv = list(range(lo, min(hi, lo + cap - 1) + 1))
    s = ' · '.join(PV(N, ch, v) + ' (%s — Num %d:%d)' % (en if v == lo else 'the verse continues', ch, v) for v in vv)
    return s + (' · … (through Num %d:%d)' % (ch, hi) if hi > vv[-1] else '')
def WIT(ch, lo, hi):
    return ['Num %d:%d | %s' % (ch, v, LV(N, ch, v)) for v in range(lo, hi + 1)]
SUB = "submitted by cold_run_second_census.py [subjects: %s] (the narrative scene, THE NUMBERS WALK 8b); re-submitted on the sequential tape by cold_run_sequence.py; consumed by law_second_census (cold_run_second_census.py) -> %s"
CASE = "submitted by cold_run_second_census.py [subjects: the exam's persons] (the wrap's scene); consumed by law_second_census (cold_run_second_census.py) -> %s"
U26 = "num_26_second_census (STEP_Nm_26_1 through STEP_Nm_26_65; claims PN26A-01 through PN26A-12)"
L = [
 ("second_census_commanded", "speech", "the second census commanded — 'and it was after the plague; and the LORD said to Moses and to Eleazar son of Aaron the priest, saying: lift the head of all the congregation of the children of Israel from twenty years old and upward by their fathers' houses, everyone going out to the host in Israel; and Moses and Eleazar the priest spoke [them] in the plains of Moab by the Jordan of Jericho, saying: from twenty years old and upward, as the LORD commanded Moses and the children of Israel who came out of the land of Egypt' (Num 25:19-26:4) — the son for the father; 1:2-3's formula with five clauses dropped; the object without its verb (the translation supplies 'to count'); the exodus generation named at the second roll's head", 26, 1, 4, "and the LORD said to Moses and to Eleazar son of Aaron the priest, saying", "Num 25:19, 26:1-4; Onkelos Num 26:1-4; Num 1:2-3, 20:28; Sifrei Bamidbar 132:1; Seder Olam Rabbah 9:2", U26, "israel", "commanded (the DEBIT on Israel — value the_second_census: the count owed; CLOSED at 26:51)", ["addressees", "threshold", "after"]),
 ("second_census_taken", "act", "the second census taken — the roll by families with its twelve counts: 'Reuben the firstborn of Israel: the sons of Reuben — of Hanoch, the family of the Hanochite …' through 'these are the counted of the children of Israel: six hundred thousand and a thousand seven hundred and thirty' (Num 26:5-51) — the twelve summing to 601,730 by the parser at both seats; the deltas against chapter 1 declared; fifty-seven families with their gentilics ('family of' seventy-eight times, chapter 1 none); the roll's named persons — Dathan, Abiram and Korach recalled with both deaths (26:9-10) and the sons who did not die (26:11), Er and Onan dead in Canaan (26:19), the line Machir-Gilead-Hepher-Zelophehad and the five daughters (26:29-33), Serah (26:46)", 26, 5, 51, "Reuben the firstborn of Israel: the sons of Reuben — of Hanoch, the family of the Hanochite", "Num 26:5-51; Onkelos Num 26:5-51; Num 1:20-46, 16:32, 16:35, 17:14, 25:9; Gen 46:8-25; Bava Batra 117a-119a, 143b:6; Sanhedrin 110a:13-17; Megillah 11a:17", U26, "israel", "the debit CLOSED (26:51); counted (the STATUS on Israel with THE NUMBER 601,730); THE POPULATION TABLE's rows — the twelve tribes, the fifty-seven families (no count: the ink gives none), the twelve deltas declared from the table's chapter-1 rows with the tape's explanations and the labeled remainder, the roll's named persons — no ledger write for a row", ["counts", "total", "families", "named"]),
 ("land_division_commanded", "speech", "the land's division commanded — 'and the LORD spoke to Moses, saying: to these the land shall be divided for an inheritance by the number of names; to the many you shall increase their inheritance and to the few you shall diminish their inheritance, to each according to his counted shall his inheritance be given; only by lot shall the land be divided, by the names of the tribes of their fathers they shall inherit; by the mouth of the lot shall its inheritance be divided between the many and the few' (Num 26:52-56) — the SIZE by count and the PLACE by lot as two functions; 'to these' the four-way dispute (the Zelophehad runner's row); 'only' excludes Joshua and Caleb; the lot's mouth the Urim", 26, 52, 56, "and the LORD spoke to Moses, saying: to these the land shall be divided for an inheritance by the number of names", "Num 26:52-56; Onkelos Num 26:52-56; Num 1:2, 33:54, 35:8, 27:21; Sifrei Bamidbar 132:1-4; Bava Batra 117a-118a, 121b:12-122b:2; Yoma 73b:3; Sanhedrin 43b:6; Josh 14-19", U26, "israel", "commanded (the DEBIT on Israel — value divide_the_land; OPEN on this tape: Joshua 14-19 the run)", ["by_names", "by_lot", "lots_mouth"]),
 ("levites_counted_second", "act", "the Levites counted the second time — 'and these are the counted of the Levites by their families: of Gershon the family of the Gershonite, of Kohath the family of the Kohathite, of Merari the family of the Merarite; these are the families of Levi: the Libnite, the Hebronite, the Mahlite, the Mushite, the Korahite; and Kohath begot Amram; and the name of Amram's wife was Jochebed the daughter of Levi, whom she bore to Levi in Egypt; and she bore to Amram Aaron and Moses and Miriam their sister; and to Aaron were born Nadab and Abihu, Eleazar and Ithamar; and Nadab and Abihu died when they brought near strange fire before the LORD; and their counted were twenty-three thousand, every male from a month old and upward, for they were not counted among the children of Israel, for no inheritance was given them among the children of Israel' (Num 26:57-62) — five families for chapter 3's eight; 23,000 for 22,000; the subjectless 'bore her'; the block of 18:23-24 read", 26, 57, 62, "and these are the counted of the Levites by their families: of Gershon the family of the Gershonite", "Num 26:57-62; Onkelos Num 26:57-62; Num 3:4, 3:17-20, 3:39, 18:20-24; Exod 2:1, 6:20; Lev 10:1; Gen 46:11, 46:15; Bava Batra 120a:1-3, 123b:1; Sotah 12a:14-15", U26, "the-levites", "counted (the STATUS on the Levites with THE NUMBER 23,000); THE POPULATION TABLE's rows — the Levites' tribe row, the three houses, the five families, the delta (+1,000 unexplained), the named persons (Amram, Jochebed, Aaron, Moses, Miriam, Nadab, Abihu, Eleazar, Ithamar); the inheritance_barred block on the Levites' ledger since 18:23-24 READ, not rewritten", ["families", "total", "threshold", "named"]),
 ("rolls_compared", "act", "the two rolls compared — 'these are the counted by Moses and Eleazar the priest, who counted the children of Israel in the plains of Moab by the Jordan of Jericho; and among these there was not a man of those counted by Moses and Aaron the priest, who counted the children of Israel in the wilderness of Sinai; for the LORD had said of them: they shall surely die in the wilderness; and there was not left a man of them except Caleb son of Jephunneh and Joshua son of Nun' (Num 26:63-65) — one sentence twice, the priest and the place the deltas; THE MEMBERSHIP PREDICATE; the decree's words (14:35) and 14:30's seven words verbatim", 26, 63, 65, "these are the counted by Moses and Eleazar the priest, who counted the children of Israel in the plains of Moab by the Jordan of Jericho", "Num 26:63-65; Onkelos Num 26:63-65; Num 1:19, 14:29-35, 14:38; Deut 2:14-16; Exod 10:15; Bava Batra 118b:3, 121a:9-121b:11; Seder Olam Rabbah 9:2", U26, "israel", "nothing written — the named rows Caleb and Joshua ('excepted — remained'); the membership predicate the checkpoint's (the table's named dead against the ledger's death entries; the decree's timer fired before the census's day)", ["priest", "place", "exceptions"]),
]
assert len(L) == 5, len(L)
KINDS = [(name, form, en, HE(ch, lo, hi, first), WIT(ch, lo, hi), ink, corpus, SUB % (subj, tape), fields) for name, form, en, ch, lo, hi, first, ink, corpus, subj, tape, fields in L]
KINDS += [
 ("census_command_case", "case", "the exam's rows on the second census's command (Num 25:19-26:4 — Seder Olam 9:2's order; Sifrei 132:1; the succession by the Chukat runner): the addressees, the shortened formula, the supplied verb, the marker after the plague, the exodus generation named",
  HE(26, 1, 1, "and the LORD said to Moses and to Eleazar son of Aaron the priest, saying"), WIT(26, 1, 1), "Num 25:19, 26:1-4; Seder Olam Rabbah 9:2; Sifrei Bamidbar 132:1; Num 20:28", U26, CASE % "accepted / commanded / counted / exempt (the exam's persons)", ["person", "ask"]),
 ("census_roll_case", "case", "the exam's rows on the roll (Num 26:5-51 — Bava Batra 143b:6, 123a:4-10; Sanhedrin 110a:9-17; Megillah 11a:17; Mishnah Bava Batra 8:1-2): the twelve counts and the total at both seats, the declared deltas, Simeon's gap, Korach's dead, the families and Genesis 46, the plural for one son, Dathan and Abiram 'this is', Korach's two deaths, the sons who did not die, the daughters' row, Serah, Reuben the firstborn, Joseph's two",
  HE(26, 9, 9, "and the sons of Eliab: Nemuel and Dathan and Abiram — this is Dathan and Abiram, the called of the congregation, who strove against Moses and against Aaron in the company of Korach when they strove against the LORD"), WIT(26, 9, 9), "Num 26:5-51; Bava Batra 143b:5-7, 123a:4-10; Sanhedrin 110a:9-17; Megillah 11a:17; Mishnah Bava Batra 8:1-2; Gen 46:8-25; 1 Chr 5:1-2", U26, CASE % "accepted / counted / holding_owed / souls_counted (the exam's persons)", ["person", "ask"]),
 ("land_division_case", "case", "the exam's rows on the land's division (Num 26:52-56 — Bava Batra 117a-119b, 121b:12-122b:2; Yoma 73b:3; Sanhedrin 43b:6; Sifrei 132:1-4; Mishnah Bava Batra 7:1-4): by the number of names and by lot, the lot's mouth, the four-way dispute, 'only', tribes or skulls, the compensation, the spies' portions, the children, the estimate, Joseph's protest, the ten parts, the possession before assignment, morasha, the thirteen tribes",
  HE(26, 55, 55, "only by lot shall the land be divided; by the names of the tribes of their fathers they shall inherit"), WIT(26, 55, 55), "Num 26:52-56; Bava Batra 117a:1-119b:4, 121b:12-122b:2; Yoma 73b:3; Sanhedrin 43b:6; Sifrei Bamidbar 132:1-4; Mishnah Bava Batra 7:1-4; Josh 14-19, 17:5, 17:14; Exod 6:8", U26, CASE % "accepted / commanded / exempt / holding_owed (the exam's persons)", ["person", "ask"]),
 ("levite_roll_case", "case", "the exam's rows on the Levites' roll (Num 26:57-62 — Bava Batra 120a:1-3, 123b:1; Sotah 12a:2-15; Num 3:4, 3:17-20, 18:20-24; Lev 10:1): five families for eight, 23,000 for 22,000, no inheritance, Jochebed between the walls and her age, Amram's remarriage, Miriam, Nadab and Abihu's strange fire, Kohath begot",
  HE(26, 59, 59, "and the name of Amram's wife was Jochebed the daughter of Levi, whom she bore to Levi in Egypt; and she bore to Amram Aaron and Moses and Miriam their sister"), WIT(26, 59, 59), "Num 26:57-62; Bava Batra 120a:1-3, 123a:21, 123b:1; Sotah 12a:2-15; Num 3:4, 3:17-20, 3:39, 18:20-24; Lev 10:1; Gen 46:11, 46:15; Exod 2:1, 6:20", U26, CASE % "accepted / counted / inheritance_barred / souls_counted (the exam's persons)", ["person", "ask"]),
 ("two_rolls_case", "case", "the exam's rows on the two rolls (Num 26:63-65 — Bava Batra 118b:3, 121a:9-121b:11; Seder Olam 9:2; Sotah 13a:14; Deut 2:14-16): one sentence twice, the membership predicate, Caleb and Joshua, the decree consumed, Levi outside, the age edges, the seven who spanned, Serah and Jochebed on both rolls, the ark's roster as a labeled hypothesis",
  HE(26, 64, 64, "and among these there was not a man of those counted by Moses and Aaron the priest, who counted the children of Israel in the wilderness of Sinai"), WIT(26, 64, 64), "Num 26:63-65; Bava Batra 118b:3, 121a:9-121b:11; Seder Olam Rabbah 9:2; Sotah 13a:14; Deut 2:14-16; Num 14:29-38; Gen 9:10", U26, CASE % "accepted / exempt (the exam's persons)", ["person", "ask"]),
]
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
# the SHARED kinds' tape lines: the second consumer named (census_taken, levites_counted)
text = open(path, encoding='utf-8').read()
n_sh = 0
for k, add in (('census_taken', "; ALSO consumed by law_second_census (cold_run_second_census.py) -> THE POPULATION TABLE's twelve tribe rows as of Num 1:17-19, no effect (THE NUMBERS WALK 8b, 2026-09-11 — a shared kind at its second consumer)"),
               ('levites_counted', "; ALSO consumed by law_second_census (cold_run_second_census.py) -> THE POPULATION TABLE's three house rows and the Levites' total row as of Num 3:16, no effect (THE NUMBERS WALK 8b, 2026-09-11 — a shared kind at its second consumer)")):
    m = re.search(r'(^  %s:\n(?:(?!^  \S).*\n)*?^    tape: ")([^"\n]*)("\n)' % re.escape(k), text, re.M)
    assert m, k
    if 'law_second_census' not in m.group(2):
        text = text[:m.start(2)] + m.group(2) + add + text[m.end(2):]; n_sh += 1
open(path, 'w', encoding='utf-8').write(text)
after = yaml.safe_load(open(path, encoding='utf-8'))
assert all(k[0] in after['events'] for k in KINDS)
print('kinds: %d added of %d, registry %d; shared tape lines appended %d' % (len(out), len(KINDS), len(after['events']), n_sh))
# ---- no new effect: the reused effects asserted on file ----
fx = yaml.safe_load(open(f"{ROOT}/World/step9/effect_vocabulary.yaml", encoding='utf-8'))['effects']
for e in ('commanded', 'counted', 'exempt', 'accepted', 'holding_owed', 'souls_counted', 'inheritance_barred'):
    assert e in fx, e
print('effects: none added — commanded, counted, exempt, accepted, holding_owed, souls_counted, inheritance_barred reused (registry %d)' % len(fx))
# ---- the daemon block + the functions block (daemon_dispositions.yaml) ----
path = f"{ROOT}/World/step9/daemon_dispositions.yaml"
text = open(path, encoding='utf-8').read()
if '  law_second_census:' not in text:
    block = '''  law_second_census:
    file: cold_run_second_census.py
    wraps: second_census
    given_at: Num 26:1
    installed_by: boot   # THE NUMBERS WALK 8b (2026-09-11): the census is a command executed at its verse — law_census's own form (Num 1:1); THE POPULATION TABLE's writer: rows (World.row) are not effects and do not appear in these watch lists — the two SHARED kinds below are row-only consumptions (an empty watch)
    watches:
      second_census_commanded: [commanded]                            # 25:19-26:4: the DEBIT on Israel — the count owed (value the_second_census)
      second_census_taken: [counted]                                  # 26:5-51: the debit CLOSED; the STATUS with 601,730; the table's rows (tribes, families, deltas, the roll's named)
      land_division_commanded: [commanded]                            # 26:52-56: the DEBIT on Israel — divide_the_land; OPEN (Joshua 14-19 the run)
      levites_counted_second: [counted]                               # 26:57-62: the STATUS on the Levites with 23,000; the table's rows; the 18:23-24 block READ
      rolls_compared: []                                              # 26:63-65: nothing written — the named rows Caleb and Joshua; the predicate the checkpoint's
      census_taken: []                                                # Num 1:17-19 (SHARED with law_census): the twelve tribe rows as of the first census — rows only
      levites_counted: []                                             # Num 3:16 (SHARED with law_census): the three houses and the Levites' total — rows only
      census_command_case: [accepted, commanded, counted, exempt]     # the exam's rows on 25:19-26:4
      census_roll_case: [accepted, counted, holding_owed, souls_counted]   # the exam's rows on 26:5-51
      land_division_case: [accepted, commanded, exempt, holding_owed] # the exam's rows on 26:52-56
      levite_roll_case: [accepted, counted, inheritance_barred, souls_counted]   # the exam's rows on 26:57-62
      two_rolls_case: [accepted, exempt]                              # the exam's rows on 26:63-65
'''
    i = text.index('  law_zelophehad:')
    text = text[:i] + block + text[i:]
if '\n  second_census:   # THE NUMBERS WALK 8b' not in text:
    fb = '''  second_census:   # THE NUMBERS WALK 8b (2026-09-11)
    the_command: {status: WRAPPED, by: law_second_census}
    the_roll: {status: WRAPPED, by: law_second_census}
    the_land: {status: WRAPPED, by: law_second_census}
    the_levites: {status: WRAPPED, by: law_second_census}
    the_rolls: {status: WRAPPED, by: law_second_census}
'''
    i = text.index('  balak:   # THE NUMBERS WALK 7b (2026-09-11)')
    j = text.index('\n  pre_sinai:', i)
    text = text[:j + 1] + fb + text[j + 1:]
open(path, 'w', encoding='utf-8').write(text)
dd = yaml.safe_load(open(path, encoding='utf-8'))
assert 'law_second_census' in dd['daemons'] and 'second_census' in dd['functions'], (list(dd)[:5])
print('daemons: %d (law_second_census %s); functions blocks: %d' % (len(dd['daemons']), 'law_second_census' in dd['daemons'], len(dd['functions'])))
# ---- the dependency span + edges ----
path = f"{ROOT}/World/step9/dependency_dispositions.yaml"
text = open(path, encoding='utf-8').read()
if '  second_census:' not in text:
    a = "  balak:       [[Num, 22, 1, 41], [Num, 23, 1, 30], [Num, 24, 1, 25], [Num, 25, 1, 19]]"
    i = text.index(a); j = text.index('\n', i)
    text = text[:j + 1] + "  second_census: [[Num, 25, 19, 19], [Num, 26, 1, 65]]   # THE NUMBERS WALK 8b (2026-09-11; NUMBERS_WALK.md \"Sitting 8b\"): the second census — the command, the roll, the land's law, the Levites' roll, the two rolls; 25:19's half-verse the marker\n" + text[j + 1:]
    edges = '''  - {from: second_census, to: bamidbar, disposition: CALL, link: reference, carries: count,
     why: "THE NUMBERS WALK 8b (2026-09-11) | 26:1-2 'lift the head... from twenty years old and upward' is 1:2-3's formula at its second seat and 26:63-64 sets the second roll against the first ('those counted by Moses and Aaron in the wilderness of Sinai'): cold_run_bamidbar.TWELVE / TOTAL / HOUSES / LEV_WRITTEN and census('total'), census('lineage'), levites('delta') CALLED — the first census's numbers the deltas are declared against"}
  - {from: second_census, to: balak, disposition: CALL, link: reference, carries: count,
     why: "THE NUMBERS WALK 8b (2026-09-11) | 25:19 'and it was after THE PLAGUE' names the plague of 25:3-9 and Simeon's fall 59,300 -> 22,200 (26:14) is measured against its 24,000: cold_run_balak.COUNT CALLED — the delta row's explanation, the tribe the shelf's claim (the row plague_tribe), 13,100 labeled unexplained"}
  - {from: second_census, to: korach, disposition: CALL, link: reference, carries: verdict,
     why: "THE NUMBERS WALK 8b (2026-09-11) | 26:9-11 recalls Korach's company — 'the earth opened its mouth and swallowed them with Korach when that company died, when the fire consumed the two hundred and fifty men' (16:32, 16:35 restated) and 'the sons of Korach did not die': cold_run_korach.plague_and_staffs('plague_count'), rebellion('two_hundred_fifty') and the rows korach_death_mode (CK4 OPEN — Sanhedrin 110a:13-14's two arms on 26:10's ink), maintaining_a_dispute, earth_mouth, sons_of_korach CALLED"}
  - {from: second_census, to: shelach, disposition: CALL, link: reference, carries: verdict,
     why: "THE NUMBERS WALK 8b (2026-09-11) | 26:65 'for the LORD had said of them: they shall surely die in the wilderness' cites the decree of 14:29-35 and 26:64's 'not a man of those counted... in the wilderness of Sinai' is its consumption: cold_run_shelach.decree('set') (the census set by CALL), ('exceptions') (Caleb and Joshua — 14:30's seven words verbatim at 26:65), ('deaths_ceased') (the fifteenth of Av, Bava Batra 121a:9) and DATA deaths_ceased CALLED — the timer's fire before the census's day the checkpoint"}
  - {from: second_census, to: zelophehad, disposition: CALL, link: reference, carries: verdict,
     why: "THE NUMBERS WALK 8b (2026-09-11) | 26:33 'and Zelophehad son of Hepher had no sons, only daughters; and the names of the daughters of Zelophehad: Mahlah, Noah, Hoglah, Milcah and Tirzah' is the daughters' row BEFORE their plea (27:1) and 26:53-56 'to these the land shall be divided' is the verse the Zelophehad runner's row land_divided_among was read from: cold_run_zelophehad.the_daughters('plea', 'names_order', 'the_run', 'three_portions', 'uncertainty', 'levirate_dilemma', 'reach', 'lapse', 'second_output'), heir_of, inheritance_order('firstborn_double') and DATA land_divided_among with its forks D_ENTERED / D_BOTH CALLED — the row READ, never re-declared"}
  - {from: second_census, to: joseph, disposition: CALL, link: reference, carries: count,
     why: "THE NUMBERS WALK 8b (2026-09-11) | 26:59 'whom she bore to Levi IN EGYPT' is the ink witness the Joseph runner's seventy (Gen 46:8-27; CJ3b — Leah's thirty-three against thirty-two living named) waited on, and the roll's families are keyed to Genesis 46's names (five absent, nine renamed, two moved a generation): cold_run_joseph.seventy('jochebed', 'diverge', 'leah_living_named', 'names_by_register', 'subtotals_parsed') and ROSTERS CALLED"}
  - {from: second_census, to: chukat, disposition: CALL, link: reference, carries: verdict,
     why: "THE NUMBERS WALK 8b (2026-09-11) | 26:1 'to Moses and to ELEAZAR son of Aaron the priest' — the son for the father since 20:28's succession ('Moses and Eleazar' seven seats from there): cold_run_chukat.edom_and_hor('succession') CALLED"}
  - {from: second_census, to: shemini_day, disposition: CALL, link: reference, carries: verdict,
     why: "THE NUMBERS WALK 8b (2026-09-11) | 26:61 'and Nadab and Abihu died when they brought near strange fire before the LORD' is Lev 10:1's clause restated (3:4's shortened by four): cold_run_shemini_day.fire('fire_status') CALLED — the eighth day's fire; no entity on the tape for the two (the gap the predicate names)"}
  - {from: sequence, to: second_census, disposition: CALL, link: none,
     why: "THE NUMBERS WALK 8b (2026-09-11) | the sequential run's REGISTRATION edge — ('cold_run_second_census', 'law_second_census') in DAEMON_ORDER (the runner compiles no verse: link none, O4's license)"}
'''
    a = "  - {from: sequence, to: balak, disposition: CALL, link: none,"
    i = text.index(a); j = text.index('\n', text.index('why:', i)) + 1
    text = text[:j] + edges + text[j:]
    open(path, 'w', encoding='utf-8').write(text)
dep = yaml.safe_load(open(path, encoding='utf-8'))
assert 'second_census' in dep['spans']
print('dependency: span + 9 edges (second_census)')
# ---- the installation probe's count ----
path = f"{ROOT}/World/step9/installation_probes.py"
text = open(path, encoding='utf-8').read()
a = "len(real) == 54 and all('given_at' in d and 'installed_by' in d for d in real.values())   # THE NUMBERS WALK 7b (2026-09-11): 53 -> 54, law_balak;"
if a in text:
    text = text.replace(a, "len(real) == 55 and all('given_at' in d and 'installed_by' in d for d in real.values())   # THE NUMBERS WALK 8b (2026-09-11): 54 -> 55, law_second_census; 7b: 53 -> 54, law_balak;")
    open(path, 'w', encoding='utf-8').write(text)
print('installation_probes I5: 55')
