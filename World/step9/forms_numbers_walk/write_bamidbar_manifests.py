import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE NUMBERS WALK sitting 1 — BAMIDBAR (2026-09-09): THE CLAIMS of Numbers 1:1-4:20, nine manifests (one per draft unit), read off
# the nine ledgers of this sitting, every claim LABELED (World/step9/CLAIM_LABELS.md's vocabulary), a machine check where the ink
# allows — every he_contains substring CUT FROM THE SNAPSHOT STORE'S OWN BYTES by the word's CONSONANTS (THE TENT sitting 4's
# form, write_num27_36_manifests.py). Claim IDs per unit: NM01A (census command), NM01B (tribe counts), NM01C (Levites exempt),
# NM02A/NM02B (the camp), NM03A/NM03B/NM03C (chapter 3), NM04A (Kohath). Written once (the files must not exist).
import json, os, re, sqlite3
ROOT = _ROOT
DATE = '2026-09-09'
UNITS = {'num_01_census_command': 'NM01A', 'num_01_tribe_counts': 'NM01B', 'num_01_levites_exempt': 'NM01C', 'num_02_camp_east_south': 'NM02A',
         'num_02_camp_west_north': 'NM02B', 'num_03_aaron_levi_replace': 'NM03A', 'num_03_levite_clans_count': 'NM03B', 'num_03_firstborn_redeem': 'NM03C', 'num_04_kehat': 'NM04A'}
OUT = {u: f'{ROOT}/logic/oral_audit/manifests/{u}_claims.json' for u in UNITS}
for o in OUT.values(): assert not os.path.exists(o), o
CI = {}
for u in UNITS:
    led = open(f'{ROOT}/logic/oral_triage/{u}_{DATE}.md', encoding='utf-8').read().split('## CITE INDEX')[1]
    CI[u] = set(re.findall(r'^(Sifrei Bamidbar \d+:\d+|Onkelos Num \d+:\d+)$', led, re.M))
assert sum(len(v) for v in CI.values()) == 160, {u: len(v) for u, v in CI.items()}
db = sqlite3.connect(f'file:{ROOT}/torah_grok.SNAPSHOT-main-51801ca.sqlite?mode=ro', uri=True)
def cut(book, ch, v, word, n, nth=0):
    rows = db.execute("SELECT w.idx, w.he FROM words w JOIN verses v ON w.verse_id=v.id WHERE v.book=? AND v.chapter=? AND v.verse=? ORDER BY w.idx", (book, ch, v)).fetchall()
    plain = lambda h: ''.join(c for c in h if c != '/' and not (0x0591 <= ord(c) <= 0x05C7))
    hit = [(i, h) for i, h in rows if plain(h) == word]
    assert len(hit) > nth and (len(hit) == 1 or nth is not None), (book, ch, v, word, hit)   # a doubled word: the nth occurrence, named
    idx, he = hit[nth]
    piece = max(he.split('/'), key=len)
    n = min(len(piece), max(n, 6))   # at least six code points of the pointed stem (two consonants with their points), never past the stem
    return idx, piece[:n]
def hc(ref, word, n, note, nth=0):
    b, cv = ref.split(' '); c, v = map(int, cv.split(':'))
    idx, sub = cut(b, c, v, word, n, nth)
    return {"type": "he_contains", "ref": ref, "idx": idx, "contains": sub, "note": note}
def tc(word, total, refs, note): return {"type": "token_count", "where": {"he_plain_joined": word}, "expect_total": total, "expect_refs": refs, "note": note}
def onk(c, lo, hi): return '; '.join(f'Onkelos Num {c}:{v}' for v in range(lo, hi + 1))

C = {}
C['num_01_census_command'] = [
 {"id": "NM01A-01", "source": onk(1, 1, 1), "ref": "Num 1:1",
  "claim_en": "THE DATE STAMP AND THE RETROGRADE. 'On the first of the second month, in the second year of their going out of Egypt' — the day, the month and the year named (Onkelos literal: 'on the first of the second month in the second year'); a month after the erection (Exod 40:17, the first of the FIRST month of year two) and BEFORE Num 9:1 (the first month of year two) in verse order: the tape's forward marker whose successor in the text is earlier in time — Pesachim 6b:7's own example ('there is no earlier and later in the Torah'). 1:18 repeats the date: the census runs on the command's day (computed).",
  "middah": "plain (the stamp read as it stands; the three dates compared on the ink — computed; the tradition's own example named for the exam)",
  "check": hc("Num 1:1", "השני", 4, "'the second' month — the stamp's month-word")},
 {"id": "NM01A-02", "source": onk(1, 2, 4), "ref": "Num 1:2-4",
  "claim_en": "THE COUNT OF NAMES; THE THRESHOLD; ONE MAN PER TRIBE. 'Lift the head' → Onkelos 'receive the sum' (the idiom flattened to accounting; the phrase's two Torah seats 1:2 and 26:2 — the two censuses, computed); 'by their skulls' kept — per head; 'the number of names, every male': names written, not a heap counted; 'from twenty years and upward, everyone going out to the host' → 'everyone going out in the host in Israel' — the first of the portion's three thresholds (twenty; a month at 3:15; thirty-to-fifty at 4:3 — computed); 'you and Aaron' — the count assigned to two; 'a man, a man for a tribe' — the distributive doubling kept.",
  "middah": "plain (Onkelos' renderings read as they stand; the idiom's seats and the thresholds computed)",
  "check": hc("Num 1:2", "לגלגלתם", 5, "'by their skulls' — per head")},
 {"id": "NM01A-03", "source": onk(1, 5, 16), "ref": "Num 1:5-16",
  "claim_en": "THE PRINCES, THE THREE ORDERS, ONE PRINCE TWO SPELLINGS, THE KETIV-QERE. The twelve named 'who shall stand with you' (Onkelos 'arise with you'); Joseph as two tribes (1:10) and Levi none keeps twelve. THE TRIBES' THREE ORDERS (computed): the princes' list Reuben, Simeon, Judah, Issachar, Zebulun, Ephraim, Manasseh, Benjamin, Dan, Asher, Gad, Naphtali; the count's (1:20-43) with GAD moved from eleventh to THIRD; the camp's (2:3-31) Judah first, Gad under Reuben. DEUEL (1:14, dalet — 10:20, 7:42, 7:47) against REUEL (2:14, resh — 10:29): one man, two spellings, Onkelos keeping each verse's own letter. 1:16 'the called of' WRITTEN / 'the summoned of' READ — the portion's ONE ketiv-qere pair (the only unpointed token in 1:1-4:20 on both stores; the store carries both tokens side by side), Onkelos rendering the read form; 'the heads of the thousands of Israel'.",
  "middah": "ink (the orders, the two spellings and the written/read pair computed on the ink; Onkelos' choices recorded)",
  "check": hc("Num 1:14", "דעואל", 5, "DEUEL with a dalet — against 2:14's Reuel")},
 {"id": "NM01A-04", "source": onk(1, 17, 19), "ref": "Num 1:17-19",
  "claim_en": "THE RUN: DESIGNATED, PEDIGREED, THE SAME DAY, THE FORMULA. 'Moses and Aaron took these men who were designated by names' → 'specified by names' — the designating verb is the LEMMA OF THE BLASPHEMER'S 'he pronounced' (Lev 24:11, 24:16; the DB's sub-lemma a shared by 1:17 and 24:11 — a shared word recorded, no inference drawn); 'they declared their pedigrees' — the verb's ONE seat in the Tanakh (computed) → Onkelos 'were registered by genealogy': the pedigree an act of the count (the exam: Yevamot 54b); 'on the first of the second month' repeated — the run on the command's day; 'as the LORD commanded Moses, and he counted them in the wilderness of Sinai' — the first of the portion's FIVE spec/run pairs (the formula's seats computed: 1:19, 2:33, 3:42, 3:51; 'according to all' at 1:54, 2:34).",
  "middah": "ink (the verb's one seat, the shared lemma, the repeated date and the formula's seats computed; the pairs counted)",
  "check": tc("ויתילדו", 1, ["Num 1:18"], "'and they declared their pedigrees' — the Tanakh's one seat, the Torah's one on this store")},
]
C['num_01_tribe_counts'] = [
 {"id": "NM01B-01", "source": onk(1, 20, 43), "ref": "Num 1:20-43",
  "claim_en": "THE TWELVE COUNTS, COMPUTED FROM THE INK'S NUMERALS: Reuben 46,500; Simeon 59,300; Gad 45,650; Judah 74,600; Issachar 54,400; Zebulun 57,400; Ephraim 40,500; Manasseh 32,200; Benjamin 35,400; Dan 62,700; Asher 41,500; Naphtali 53,400 — the Aramaic numerals the same. The formula twelve times ('their generations by their families by their fathers' house, by the number of names by their skulls, every male from twenty years and up, everyone going out to the host'); 'Israel's firstborn' on Reuben; 'generations' — the Genesis heading-word — twelve times as a census column (computed); GAD THIRD (the camp's companions counted together before the camp is commanded).",
  "middah": "ink (every number computed from the ink; the order and the heading-word computed)",
  "check": hc("Num 1:20", "בכר", 3, "'firstborn' — Reuben, Israel's firstborn, heads the count")},
 {"id": "NM01B-02", "source": onk(1, 44, 46), "ref": "Num 1:44-46",
  "claim_en": "THE TOTAL IS THE SUM, ON THREE SEATS. 'Twelve men, one man for his fathers' house' — the counters named; 'six hundred thousand and three thousand and five hundred and fifty' — THE TWELVE SUMMED EQUAL IT (computed: 603,550); the same number at 2:32 (the four camps summed, computed) and at Exod 38:26 (the half-shekel count at the erection, computed on that verse's own numerals): the exam's question at Bekhorot 5a — two counts months apart, one number — is a computed fact of the ink on both seats.",
  "middah": "ink (the sum and the three seats computed)",
  "check": hc("Num 1:46", "וחמשים", 6, "'and fifty' — the total's last part")},
 {"id": "NM01B-03", "source": onk(1, 21, 21), "ref": "Num 1:21",
  "claim_en": "THE CENSUS'S NUMBER GRAMMAR, MEASURED ON EVERY NUMBER OF 1:1-4:20: a unit immediately before 'hundreds' multiplies; 'thousand'/'thousands' WITHOUT the conjunction multiplies the whole group before it ('six and forty thousand' = 46,000; 'six hundred thousand'); 'AND a thousand' is an addend (3:50 = 1,365; the form's three Torah seats Exod 38:25, Num 3:50, 26:51); 'from' and 'a hundred of' are consonantal homographs told apart by their vowels (3:49-50 against 2:9-31); a doubled numeral is distributive (3:47 'five, five'). THE ENGINE'S NUMERAL PARSER CANNOT READ THE CENSUS (measured: cold_run_sequence.ink_numbers on 1:21 gives 1,546 for 46,500; on 3:39 1,020 for 22,000; on 1:46 two numbers for one) — Genesis's and Exodus's grammar has no thousands and reads 'two' as 'years': the compile sitting's item.",
  "middah": "ink (the grammar measured on the ink; the engine's parser measured against it)",
  "check": hc("Num 1:21", "אלף", 3, "'thousand' — the multiplier the engine's parser lacks")},
]
C['num_01_levites_exempt'] = [
 {"id": "NM01C-01", "source": onk(1, 47, 49), "ref": "Num 1:47-49",
  "claim_en": "THE EXCLUSION. 'And the Levites by the tribe of their fathers were not counted among them' (1:47, the narrator) BEFORE the command that excludes them (1:49 'only the tribe of Levi you shall not count, and their head you shall not lift') — the text's own order; Onkelos: 'however' for 'only', 'their sum you shall not receive' — the census idiom of 1:2 negated for one tribe. COUNT AND APPOINT ARE ONE ROOT (1:49 'you shall not count' / 1:50 'appoint'): Onkelos splits them.",
  "middah": "plain (the report before the command read as it stands; Onkelos' two verbs for the one root)",
  "check": hc("Num 1:49", "אך", 2, "'only' — the restrictive on the tribe of Levi")},
 {"id": "NM01C-02", "source": onk(1, 50, 51), "ref": "Num 1:50-51",
  "claim_en": "THE APPOINTMENT AND THE STRANGER. 'Appoint the Levites over the tabernacle of the testimony' (the name's three Torah seats computed: Exod 38:21, Num 1:50, 10:11) — carry, serve, camp around; 'when the tabernacle journeys the Levites shall take it down, and when it rests set it up'; 'AND THE STRANGER WHO APPROACHES SHALL BE PUT TO DEATH' → Onkelos 'the LAY man who approaches shall be killed' — the stranger is the OUTSIDER TO THE OFFICE, not the foreigner: the clause's four Torah seats (computed: 1:51 the non-Levite at the tabernacle, 3:10 the non-priest at the priesthood, 3:38 before the tent, 18:7 the priesthood again).",
  "middah": "plain (Onkelos' word for the stranger read as it stands; the clause's seats computed)",
  "check": hc("Num 1:51", "והזר", 4, "'and the stranger' — the lay man of Onkelos")},
 {"id": "NM01C-03", "source": onk(1, 52, 54), "ref": "Num 1:52-54",
  "claim_en": "THE BANNER, THE WRATH-SHIELD, THE RUN. 'Each man by his camp and each man by his banner' → Onkelos 'on his TAXIS' — the Greek loan for a battle-order: the camp as an army in array; 'the Levites shall camp round about the tabernacle of the testimony, THAT THERE BE NO WRATH on the congregation' → 'that there be no anger' — the guard's purpose written (the word's thirteen Torah seats computed; 18:5 'that there be no more wrath' the parallel command; 17:11 the plague's wrath): the Levite ring absorbs the wrath; 'the Levites shall keep the charge' — the portion's key-word (nine seats in 1:1-4:20, computed); 'the children of Israel did according to all that the LORD commanded Moses, so they did' — the doubled report (its second seat 2:34).",
  "middah": "plain (Onkelos' taxis and anger read as they stand; the wrath's seats and the charge's computed)",
  "check": hc("Num 1:53", "קצף", 3, "'wrath' — the guard's purpose")},
]
C['num_02_camp_east_south'] = [
 {"id": "NM02A-01", "source": onk(2, 1, 2), "ref": "Num 2:1-2",
  "claim_en": "THE BANNER, THE SIGNS, THE DISTANCE. 'To Moses AND to Aaron' — the first of three double-addressed frames (computed: 2:1, 4:1, 4:17); 'each man by his banner with the SIGNS of their fathers' house' → 'on his taxis, with the signs'; 'AT A DISTANCE, round about the tent of meeting they shall camp' → Onkelos 'OPPOSITE, round about' — the distance-word carries no number in the ink: the two thousand cubits are the Talmud's (Eruvin 51a, from Josh 3:4's 'far off' — a TRANSFER with its teacher, at the exam), not this verse's.",
  "middah": "plain (the verse and its rendering as they stand; the measure left to the exam where its teacher is)",
  "check": hc("Num 2:2", "מנגד", 4, "'at a distance' — the word without a number")},
 {"id": "NM02A-02", "source": onk(2, 3, 9), "ref": "Num 2:3-9",
  "claim_en": "EAST: JUDAH, FIRST. 'Those camping in front, eastward: the banner of the camp of Judah' → 'in front, eastward; the taxis of the camp of Judah'; Nahshon; Issachar and Zebulun 'beside him' → 'adjoining him'; the three numbers of 1:27, 29, 31 repeated verbatim (computed equal); 'all the counted of the camp of Judah: 186,400 by their hosts; FIRST they journey' → 'in the first place they journey' — THE THREE SUMMED EQUAL THE CAMP (computed: 74,600 + 54,400 + 57,400).",
  "middah": "ink (the side, the ordinal and the sum computed on the ink; Onkelos literal)",
  "check": hc("Num 2:9", "ראשנה", 5, "'first' — the march's first ordinal")},
 {"id": "NM02A-03", "source": onk(2, 10, 16), "ref": "Num 2:10-16",
  "claim_en": "SOUTH: REUBEN, SECOND; REUEL. 'The banner of the camp of Reuben southward' → 'south'; Simeon and Gad beside him — 'Eliasaph son of REUEL' (resh) against 1:14's DEUEL (dalet), computed on both seats; Onkelos keeps this verse's own letter too: one prince, two spellings, neither harmonized; 'all the counted of the camp of Reuben: 151,450; and second they journey' → 'in the second place' — the three summed equal the camp (computed: 46,500 + 59,300 + 45,650).",
  "middah": "ink (the two spellings, the side, the ordinal and the sum computed)",
  "check": hc("Num 2:14", "רעואל", 5, "REUEL with a resh — against 1:14's Deuel")},
]
C['num_02_camp_west_north'] = [
 {"id": "NM02B-01", "source": onk(2, 17, 17), "ref": "Num 2:17",
  "claim_en": "THE MARCH ORDER IS THE CAMP ORDER. 'And the tent of meeting shall journey, the camp of the Levites in the midst of the camps; AS THEY CAMP SO THEY JOURNEY, each man in his place by their banners' → Onkelos literal ('as they camp so they journey; each man on his place by their taxis') — the Levites' camp in the middle, the four banners around, the march keeping the camp's shape (the Talmud's two readings — a square as camped or a beam in file — the exam: Jerusalem Talmud Eruvin 5:1).",
  "middah": "plain (the clause read as it stands; the dispute on its shape routed to the exam)",
  "check": hc("Num 2:17", "יחנו", 4, "'they camp' — as they camp so they journey")},
 {"id": "NM02B-02", "source": onk(2, 18, 24), "ref": "Num 2:18-24",
  "claim_en": "WEST: EPHRAIM, THIRD. 'The banner of the camp of Ephraim by their hosts SEAWARD' → Onkelos 'WEST' — the sea-word rendered by the compass: the geography, not the metaphor; Manasseh and Benjamin beside him; the three numbers of 1:33, 35, 37 repeated; 'all the counted of the camp of Ephraim: 108,100; and third they journey' → 'in the third place' — the three summed equal the camp (computed: 40,500 + 32,200 + 35,400).",
  "middah": "plain (Onkelos' compass reading recorded; the side, the ordinal and the sum computed)",
  "check": hc("Num 2:18", "ימה", 3, "'seaward' — rendered west")},
 {"id": "NM02B-03", "source": onk(2, 25, 31), "ref": "Num 2:25-31",
  "claim_en": "NORTH: DAN, LAST. 'The banner of the camp of Dan northward' → 'north'; Asher and Naphtali beside him; the three numbers of 1:39, 41, 43 repeated; 'all the counted of the camp of Dan: 157,600; LAST they journey, by their banners' → 'in the last place they journey, by their taxis' — the three summed equal the camp (computed: 62,700 + 41,500 + 53,400); the march's four ordinals in the ink's own words (computed: first 2:9, second 2:16, third 2:24, last 2:31).",
  "middah": "ink (the side, the ordinals and the sum computed)",
  "check": hc("Num 2:31", "לאחרנה", 5, "'last' — the march's last ordinal")},
 {"id": "NM02B-04", "source": onk(2, 32, 34), "ref": "Num 2:32-34",
  "claim_en": "THE TOTAL'S THIRD SEAT; ONE VERSE, TWO RUNS. 'All the counted of the camps by their hosts: 603,550' — the four camps summed equal it (computed: 186,400 + 151,450 + 108,100 + 157,600) = 1:46 = Exod 38:26: the number on three seats in two books; 'the Levites were not counted, as the LORD commanded Moses' (the formula's seats computed); 'the children of Israel did according to all that the LORD commanded Moses: SO THEY CAMPED by their banners AND SO THEY JOURNEYED, each by his families, by his fathers' house' — the camp's spec (2:2) and the march's (2:17) reported done in one report formula, the doubled 'so' of 1:54 doubled again.",
  "middah": "ink (the sum and the seats computed; the two runs in one report read as they stand)",
  "check": hc("Num 2:34", "חנו", 3, "'they camped' — the first of the verse's two runs")},
]
C['num_03_aaron_levi_replace'] = [
 {"id": "NM03A-01", "source": onk(3, 1, 2), "ref": "Num 3:1-2",
  "claim_en": "THE GENESIS HEADING ON AARON AND MOSES; THE FIRSTBORN NADAB. 'And these are the generations of Aaron and Moses on the day the LORD spoke with Moses on Mount Sinai' → Onkelos literal ('on the mountain of Sinai') — the 'these are the generations' heading's ONE seat outside Genesis (computed: ten headings in the Torah, nine in Genesis), and the list that follows names AARON'S SONS ALONE — Moses in the heading, none of his in the list (the exam's Talmud fills the gap: the teacher as begetter, Sanhedrin 19b); 'on the day the LORD spoke' at Exod 6:28, Num 3:1, Deut 4:15 (computed); 'the FIRSTBORN Nadab, and Abihu, Eleazar and Ithamar' — the firstborn labeled in a chapter about firstborns; the four-name list's seven Torah seats computed.",
  "middah": "ink (the heading's seats, the dating clause's and the list's computed; the ink's own gap recorded, its filling routed to the exam)",
  "check": hc("Num 3:1", "תולדת", 5, "'the generations of' — the Genesis heading-word")},
 {"id": "NM03A-02", "source": onk(3, 3, 4), "ref": "Num 3:3-4",
  "claim_en": "THE FILLED HAND AS AN OFFERING; THE SONLESSNESS; UPON THE FACE. 'The anointed priests whose hand he filled to serve' (this form's one Torah seat, computed) → Onkelos 'the priests who were anointed, whose OFFERING was brought near, to serve' — the investiture idiom rendered by its RITE, Lev 8's ram of filling (a REFERENCE to the investiture by the translation's own word); 'Nadab and Abihu died before the LORD when they brought near strange fire' → 'foreign fire', 'in the wilderness of Sinai' (nine Torah seats computed — Lev 10 dated to this book's place); 'AND SONS THEY HAD NOT' — the phrase's one Tanakh seat (computed), Onkelos literal: the office's inheritance written in the negative — had they had sons, the sons would have stood before Eleazar; 'Eleazar and Ithamar served as priests UPON THE FACE OF Aaron their father' — Onkelos keeps the idiom ('upon the face'), the Talmud reads it 'in his lifetime' (the exam).",
  "middah": "plain (Onkelos' rite-word and kept idiom read as they stand; the one-seat phrases computed; the Talmud's reading routed to the exam)",
  "check": hc("Num 3:4", "ובנים", 5, "'and sons' — 'and sons they had not'")},
 {"id": "NM03A-03", "source": onk(3, 5, 10), "ref": "Num 3:5-10",
  "claim_en": "THE TRIBE BROUGHT NEAR; TWO CHARGES; GIVEN, GIVEN; THE PRIESTHOOD KEPT. 'Bring near the tribe of Levi and stand it before Aaron the priest, and they shall serve HIM' → 'bring near... and they shall minister to him' — THE OFFERING VERB ON A TRIBE (the phrase's one seat, computed): the Levites brought near as an offering is, the service to Aaron; 'they shall keep HIS charge and the charge of THE WHOLE CONGREGATION... to do the service of the tabernacle' — the tribe stands in for the congregation in the charge's own grammar; 'keep all the vessels of the tent of meeting'; 'GIVEN, GIVEN are they to him' → Onkelos 'HANDED OVER, GIVEN' — the doubled word (its one seat, computed; the single 'given' at 8:16, 8:19, 18:6) rendered by two verbs (the exam's Sifrei at 8:16 reads two grants); 'Aaron and his sons you shall APPOINT and they shall keep their priesthood; and the stranger who approaches shall be put to death' — the count-verb as appoint again (1:50), the death clause's second seat: here the stranger is the NON-PRIEST, a Levite too (the exam: Sanhedrin 83a).",
  "middah": "plain (Onkelos' offering verb and two verbs read as they stand; the one-seat phrases computed)",
  "check": hc("Num 3:9", "נתונם", 5, "'given' — the first of the doubled word (the store holds two; the first cut)", nth=0)},
 {"id": "NM03A-04", "source": onk(3, 11, 13), "ref": "Num 3:11-13",
  "claim_en": "THE SUBSTITUTION AS A REFERENCE TO THE FIRSTBORN LAW; ITS GROUND DATED. 'And I, behold, I have TAKEN the Levites from among the children of Israel instead of every firstborn, OPENER OF THE WOMB' → Onkelos 'I have BROUGHT NEAR the Levites' (the offering verb for the taking) and 'opener of the offspring'; 'and the Levites shall be Mine' → 'shall be ministering before Me' — possession rendered as service; 'opener of the womb' is THE FIRSTBORN ENGINE'S OWN PHRASE (computed: Exod 13:12, 13:15, 34:19, Num 3:12, 18:15 — Exod 13's sanctification clause): the substitution is a REFERENCE to the firstborn law by its own token; 'for every firstborn is Mine: ON THE DAY I SMOTE every firstborn in the land of Egypt I sanctified to Me every firstborn in Israel, from man to beast' → 'on the day that I KILLED' — the sanctification DATED to the plague's night (Exod 12:29 on the tape; 13:2's command the morning after): the ground is an event on the ledger.",
  "middah": "plain (the reference by the ink's own token, computed; Onkelos' verbs read as they stand; the date read off the clause)",
  "check": hc("Num 3:12", "פטר", 3, "'opener' — opener of the womb, Exod 13's clause")},
]
C['num_03_levite_clans_count'] = [
 {"id": "NM03B-01", "source": onk(3, 14, 17), "ref": "Num 3:14-17",
  "claim_en": "THE PLACED FRAME; THE MONTH THRESHOLD; BY THE MOUTH OF THE LORD; THE THREE HOUSES. 'And the LORD spoke to Moses IN THE WILDERNESS OF SINAI, saying' — the portion's second placed frame (computed: 1:1 and 3:14 of ten); 'count the sons of Levi by their fathers' house, by their families; every male FROM A MONTH OLD and upward' → 'from a son of a month' — the second threshold (the tribe counted from the age its firstborn are redeemable, 18:16); 'and Moses counted them BY THE MOUTH OF THE LORD, as he was commanded' → 'by the WORD of the LORD' — the phrase three times in this chapter (computed: 3:16, 3:39, 3:51: the count, the total, the money; the exam's question — how infants in tents were counted — outside scope); 'Gershon, Kohath and Merari' — the three houses.",
  "middah": "ink (the frames, the threshold and the phrase's seats computed; Onkelos' Word recorded)",
  "check": hc("Num 3:15", "חדש", 3, "'a month' — the Levite threshold")},
 {"id": "NM03B-02", "source": onk(3, 18, 26), "ref": "Num 3:18-26",
  "claim_en": "GERSHON: 7,500, WEST, THE SOFT CHARGE. The eight families under three houses (Libni, Shimei; Amram, Izhar, Hebron, Uzziel; Mahli, Mushi); Gershon's counted 7,500 (computed from the numerals; the Aramaic the same); 'behind the tabernacle, seaward' → 'behind the tabernacle they shall camp, west'; Eliasaph son of Lael (3:24 — the verse the shelf's export names as the head of its piska 62, which by position and by its own quotations is the row on 8:24: read at the Kohath ledger, the head a mislabel filed in RESEARCH_LOG.md); the charge: the tabernacle and the tent, its covering, the screen of the door, the hangings of the court, the screen of the court's gate, its cords — everything woven and roped.",
  "middah": "ink (the number, the side and the inventory computed and read; the shelf's mislabel recorded)",
  "check": hc("Num 3:23", "ימה", 3, "'seaward' — Gershon west")},
 {"id": "NM03B-03", "source": onk(3, 27, 32), "ref": "Num 3:27-32",
  "claim_en": "KOHATH: 8,600, SOUTH, THE HOLY CHARGE; THE AMARKAL; THE THREE HUNDRED. Kohath's counted 8,600, 'keepers of the charge of the holy' (Onkelos the same); THE INK'S OWN ARITHMETIC PROBLEM (computed): 7,500 + 8,600 + 6,200 = 22,300 against 3:39's 22,000 — a delta of 300 written into the verses (the exam's answer, Bekhorot 5a's three hundred firstborn Levites, is the Talmud's; the delta the ink's); 'on the side of the tabernacle southward' → 'south'; Elizaphan son of Uzziel; the charge: the ark, the table, the lampstand, THE ALTARS (plural — the golden and the bronze, both wrapped in chapter 4), the vessels of the holy, THE SCREEN (the veil, 4:5); 'AND THE PRINCE OF THE PRINCES OF LEVI: Eleazar son of Aaron the priest, the appointment of the keepers of the charge of the holy' (the phrase's one seat, computed) → Onkelos 'the AMARKAL appointed over the chiefs of the Levites, under whose hand are appointed' — the Temple treasury's office-title (Mishnah Shekalim 5:2, the exam) read onto Eleazar: the later institution's word in the translation of the earlier verse.",
  "middah": "ink (the numbers and the delta computed; Onkelos' office-title recorded as the translation's own word)",
  "check": hc("Num 3:32", "ונשיא", 5, "'and the prince of' — the prince of the princes, Onkelos' amarkal")},
 {"id": "NM03B-04", "source": onk(3, 33, 39), "ref": "Num 3:33-39",
  "claim_en": "MERARI: 6,200, NORTH, THE HARD CHARGE; EAST THE LEADERS; THE TOTAL AS WRITTEN. Merari's counted 6,200; Zuriel son of Abihail; 'on the side of the tabernacle northward' → 'north'; 'the appointed charge of the sons of Merari' → 'what is handed over to the charge': the boards, bars, pillars, sockets, the court's pillars, pegs and cords — the frame; 'those camping before the tabernacle in front, before the tent of meeting eastward: Moses and Aaron and his sons, keeping the charge of the sanctuary FOR the charge of the children of Israel; and the stranger who approaches shall be put to death' → 'keeping the charge of the sanctuary for the charge of' — the inner ring's fourth side is the LEADERS' (the ring computed: west Gershon 3:23, south Kohath 3:29, north Merari 3:35, east Moses-Aaron 3:38 — matching the outer ring's four sides), the charge kept on the people's behalf, the death clause's third seat; 'all the counted of the Levites... by the mouth of the LORD... every male from a month old and up: TWENTY-TWO THOUSAND' — the total AS WRITTEN (22,000) against the houses' computed 22,300; the ink's 'two and twenty thousand' — the unit before the ten, the thousand multiplying both.",
  "middah": "ink (the numbers, the ring and the delta computed; the clause's third seat)",
  "check": hc("Num 3:39", "ועשרים", 6, "'and twenty' — two and twenty thousand, the total as written")},
]
C['num_03_firstborn_redeem'] = [
 {"id": "NM03C-01", "source": onk(3, 40, 43), "ref": "Num 3:40-43",
  "claim_en": "THE SAID-FRAME; THE FIRSTBORN COUNTED; MAN AND BEAST. 'And the LORD SAID to Moses' — the portion's one 'said' among ten frames (computed); 'count every firstborn male of the children of Israel from a month old and up, and LIFT THE NUMBER OF THEIR NAMES' → 'RECEIVE the number of their names' — the census idiom of 1:2 on the firstborn; 'take the Levites for Me — I am the LORD — instead of every firstborn... and the cattle of the Levites instead of every firstling among the cattle' → 'BRING NEAR the Levites before Me' (the offering verb for the taking again); 'and Moses counted, as the LORD commanded him' (the formula); 'all the firstborn males... TWENTY-TWO THOUSAND, THREE AND SEVENTY AND TWO HUNDRED' — computed 22,273: the thousands first, the remainder ASCENDING (three, seventy, two hundred) — the ink's two orders in one number; the Aramaic writes the remainder descending.",
  "middah": "ink (the frame and the number computed; Onkelos' offering verb read as it stands)",
  "check": hc("Num 3:40", "ויאמר", 5, "'and He said' — the portion's one said-frame")},
 {"id": "NM03C-02", "source": onk(3, 44, 48), "ref": "Num 3:44-48",
  "claim_en": "THE EXCESS; FIVE, FIVE; THE SHEKEL AND ITS GERAH — THE CONVERSION LAYER AT ITS NUMBERS SEAT. 'Take the Levites instead of every firstborn... and the Levites shall be Mine, I am the LORD' (3:41 restated); 'the redemption of THE THREE AND THE SEVENTY AND THE TWO HUNDRED who exceed the Levites' — computed 22,273 − 22,000 = 273, the ink writing it ascending with the article on each part; 'you shall take FIVE, FIVE shekels per skull, by the shekel of the holy: TWENTY GERAH THE SHEKEL' → Onkelos 'five, five SELA'IM per skull... twenty MA'IN the sela' — the shekel is the sela, the gerah the ma'ah: the very words the Talmud cites at Bekhorot 50a ('and we translate: twenty ma'in') — the corpus's standing finding from Exod 30:13, read again at its second law seat; 'twenty gerah' at Exod 30:13, Lev 27:25, Num 3:47, 18:16 (computed: four Torah seats); the doubled five the ink's one seat — a distributive, not a sum; 'give the money to Aaron and his sons, the redemption of those who exceed'.",
  "middah": "ink (the excess computed; the conversion layer's words on the shelf's own bytes; the doubled numeral read as distributive)",
  "check": hc("Num 3:47", "גרה", 3, "'gerah' — twenty gerah the shekel: Onkelos' ma'in")},
 {"id": "NM03C-03", "source": onk(3, 49, 51), "ref": "Num 3:49-51",
  "claim_en": "THE MONEY; 'AND A THOUSAND'; THE DOUBLE FORMULA. 'Moses took the redemption money FROM those who exceeded the redeemed of the Levites' — 'from' the consonantal homograph of 'a hundred of', told apart by its vowels (computed: the tsere at 3:49-50 against the sheva-patach at 2:9, 16, 24, 31); 'FIVE AND SIXTY AND THREE HUNDRED AND A THOUSAND by the shekel of the holy' — computed 273 × 5 = 1,365: the ink writes it ASCENDING with the thousand LAST and joined by the conjunction, 'and a thousand' an ADDEND not a multiplier (the form's three Torah seats computed: Exod 38:25, Num 3:50, 26:51); the Aramaic reverses to descending; 'Moses gave the redemption money to Aaron and his sons BY THE MOUTH OF THE LORD, AS THE LORD COMMANDED MOSES' → 'by the Word of the LORD... as the LORD commanded Moses' — both formulas on one verse: the fifth commanded-and-done pair of the portion closes (the census, the camp, the Levite count, the firstborn count, the redemption).",
  "middah": "ink (the product, the homograph's vowels and the addend's seats computed; the formulas' seats computed)",
  "check": hc("Num 3:50", "ואלף", 4, "'and a thousand' — the addend by the conjunction")},
]
C['num_04_kehat'] = [
 {"id": "NM04A-01", "source": 'Sifrei Bamidbar 62:1; ' + onk(4, 1, 4), "ref": "Num 4:1-4",
  "claim_en": "THE HOUSE'S HEAD LIFTED; THE WORK'S AGES — THE SIFREI'S ROW; THE HOLY OF HOLIES. 'Lift the head of the sons of Kohath from among the sons of Levi' → 'receive the sum' — the census idiom on ONE HOUSE (computed: the infinitive at 4:2 and 4:22, the imperative at 1:2 and 26:2); 'from thirty years old and upward, and until fifty years old, everyone who comes to the HOST to do work in the tent of meeting' → 'everyone who comes to the host to do the work' — the THIRD THRESHOLD, a window (computed: thirty-to-fifty seven times in chapter 4), the army-word of 1:3 on the Levites' labor, one Aramaic word for both. THE SIFREI ON NUMBERS, PISKA 62 (found by POSITION: the export heads it '3:24', it sits between 8:4 and 8:25 and quotes 8:24 and 4:23 — the row on 8:24, the head a mislabel): 'this is what applies to the Levites' — YEARS disqualify the Levites, BLEMISHES do not, against the a-fortiori from the priests ('where years do not disqualify, blemishes do; where years disqualify, how much more') — the verse's 'this' REFUTES the inference (a stated limit beats an inferred one); and the two ages reconciled — twenty-five (8:24) to LEARN, thirty (4:23, 4:3) to SERVE: one threshold with an apprenticeship before it (the Talmud's fifty — the voice, not the years — at Chullin 24a, the exam). 'This is the service of the sons of Kohath in the tent of meeting: THE HOLY OF HOLIES' (4:4 and 4:19 in the span, computed) — Kohath's load the innermost.",
  "middah": "I1 (the Sifrei's a-fortiori from the priests' blemish-bar REFUTED by 'this is what applies' — the tradition's own refutation recorded; the two ages reconciled as learning and serving; the threshold's seats and the idiom's computed)",
  "check": hc("Num 4:3", "שלשים", 5, "'thirty' — the serving age the Sifrei reconciles with 8:24's twenty-five")},
 {"id": "NM04A-02", "source": onk(4, 5, 14), "ref": "Num 4:5-14",
  "claim_en": "THE PRIESTS COVER: THE VEIL ON THE ARK, BLUE OUTSIDE ONLY THE ARK, THE BREAD ON THE MARCH, THE ALTAR ASHED. 'Aaron and his sons shall come in when the camp journeys and take down THE VEIL OF THE SCREEN and cover with it the ark of the testimony' → 'at the journeying of the camp... the veil of the screen... cover with it the ark' — THE VEIL BECOMES THE ARK'S COVER; on it 'a covering of tachash hide' → Onkelos 'SASGONA hide' (a colored hide; the exam: Shabbat 28a) and 'a cloth WHOLLY OF BLUE' on top — the high priest's ROBE's phrase (computed: Exod 28:31, 39:22, Num 4:6): ONLY THE ARK wears blue OUTSIDE the hide; the table (4:7-8: blue, the dishes, the spoons, the jars, the jugs of libation — 'AND THE CONTINUAL BREAD SHALL BE ON IT': the bread travels on the table, the exam's Menachot 99b; crimson; hide), the lampstand with its lamps, tongs, fire-pans, oil vessels (blue, hide, ON THE BAR — no poles of its own), the golden altar (blue, hide, poles), the service vessels (blue, hide, the bar) all hide-outermost (computed: tachash at 4:6, 8, 10, 11, 12, 14); THE BRONZE ALTAR ALONE NOT BLUE: 'they shall REMOVE THE ASHES of the altar and spread on it a cloth of PURPLE' → 'clear away the ashes... a garment of purple' (the exam: the fire under the cloth, Yoma 21b), then its fire-pans, forks, shovels, basins, and the hide.",
  "middah": "ink (the layers' order computed on the ink — the robe's phrase, the tachash seats; Onkelos' hide-word recorded; the bread's clause read as it stands)",
  "check": hc("Num 4:6", "כליל", 4, "'wholly' — wholly of blue, the robe's phrase on the ark")},
 {"id": "NM04A-03", "source": onk(4, 15, 16), "ref": "Num 4:15-16",
  "claim_en": "THE ORDER IS THE LAW; ELEAZAR'S CHARGE. 'Aaron and his sons shall FINISH covering the holy and all the vessels of the holy when the camp journeys, and AFTER THAT the sons of Kohath shall come to carry; and they shall not TOUCH the holy, lest they die — these are the burden of the sons of Kohath' → Onkelos 'shall finish covering... and after that the sons of Kohath shall enter to carry; and they shall not APPROACH the holy, and they shall not die' — the touching rendered as approaching (a wider guard); the priests finish, THEN the carriers enter; the first of the span's three death clauses (computed: 4:15 touching, 4:19 approaching unassigned, 4:20 seeing); 'the appointment of Eleazar son of Aaron the priest: the oil of the light, the incense of spices, the continual meal-offering, the anointing oil; the charge of all the tabernacle' → 'what is handed over to Eleazar... the oil of lighting, the incense of spices, the continual meal-offering, the oil of greatness' — the four consumables in the priest's own hands, his charge over the whole.",
  "middah": "plain (the sequence read as it stands; Onkelos' wider verb recorded; the death clauses computed)",
  "check": hc("Num 4:15", "ומתו", 4, "'lest they die' — the first death clause")},
 {"id": "NM04A-04", "source": onk(4, 17, 20), "ref": "Num 4:17-20",
  "claim_en": "CUT NOT OFF; THE REMEDY; NOT TO SEE THE SWALLOWING. 'To Moses AND to Aaron' (the third double frame); 'DO NOT CUT OFF the tribe of the families of the Kohathite from among the Levites' → 'do not destroy' — the cutting-off verb's one seat in this form (computed): the guard laid on the LEADERS, whose negligence would cut the house off; 'this do for them, that they may LIVE AND NOT DIE when they approach the holy of holies: Aaron and his sons shall come in and set them EACH MAN, EACH MAN to his service and to his burden' → 'and they shall APPOINT them, each man, each man' — the assignment per man, the doubled 'man' kept; 'and they shall not come in to see AS THE HOLY IS SWALLOWED, lest they die' → Onkelos 'to see WHEN THEY COVER THE VESSELS of the holy' — the swallowing verb (the word's ONE seat in the Tanakh, computed) rendered as covering and its object expanded to the vessels: the moment forbidden to the eye is the packing (the exam: Sanhedrin 81b reads the swallowing as the taking-down); the third death clause — touching, approaching unassigned, seeing.",
  "middah": "ink (the one-seat words computed; Onkelos' covering read as it stands; the three clauses counted)",
  "check": tc("כבלע", 1, ["Num 4:20"], "'as it is swallowed' — the word's one seat in the Tanakh, the Torah's one on this store")},
]
LABELS = {'plain', 'ink', 'H'} | {f'I{i}' for i in range(1, 14)} | {f'E{i}' for i in range(1, 33)}
n_claims = n_checks = 0
for u, cs in C.items():
    pre = UNITS[u]
    assert [c['id'] for c in cs] == [f'{pre}-{i:02d}' for i in range(1, len(cs) + 1)], [c['id'] for c in cs]
    for c in cs:
        for s in c['source'].split('; '): assert s in CI[u], (c['id'], s)
        code = c['middah'].split(' ')[0]
        assert code in LABELS or re.fullmatch(r'M-\d\d', code), code
        assert re.fullmatch(r'^(ink|plain|H|I\d{1,2}|E\d{1,2}|M-\d\d)(?:\s*\(.*\))?\s*$', c['middah']), c['middah']
        assert '"' not in c['claim_en'], c['id']
    open(OUT[u], 'w', encoding='utf-8').write(json.dumps(cs, indent=1, ensure_ascii=False) + '\n')
    n_claims += len(cs); n_checks += sum('check' in c for c in cs)
    print(f'wrote {OUT[u]} | claims {len(cs)} | checks {sum("check" in c for c in cs)} | labels {[c["middah"].split(" ")[0] for c in cs]}')
    for c in cs:
        if c['check']['type'] == 'he_contains': print('   ', c['id'], c['check']['ref'], c['check']['idx'], repr(c['check']['contains']))
print(f'BAMIDBAR: {n_claims} claims, {n_checks} checks across {len(C)} manifests')
