#!/usr/bin/env python3
# THE NUMBERS WALK, sitting 9 — THE OFFERINGS CALENDAR, Numbers 28:1-29:39 (2026-09-11; the owner: "I agree continue" after the register
# gate, on the ruling READ THEN COMPILE): THE INK of the two chapters, computed from the Tanakh DB, the snapshot store and the shelf's own
# bytes — never typed. Sitting 8's form (census_ink.py): the heads found BY POSITION and asserted; coverage computed; every cut by consonants
# (the misses collected, asserted empty); the engine's numeral parser MEASURED against every number of the two chapters; the hand's facts as
# asserts, run all at once by assert_driver.py after the measurement pass (offerings_measure1.py) printed them; every gloss of a narrative
# verb the STORE'S OWN (words.gloss); NFC on both sides of every pointed comparison. Shared by offerings_rows_onkelos.py,
# offerings_rows_sifrei.py and write_offerings_ledgers.py.
# THE SPAN: THREE drafts — num_28_daily_shabbat_rosh 28:1-15, num_28_pesach_shavuot 28:16-31, num_29_fall_festivals 29:1-39 — the remainder
# of the portion Pinchas (25:10-30:1; 25:10-19 read with Balak's draft, 26 at sitting 8, 27 FROZEN at THE TENT and skipped); the portion's
# last verse 30:1 opens the next draft (num_30_vows) and is read with it — the draft's-grain rule.
import json, os, re, html, sqlite3, sys, io, contextlib, unicodedata
from collections import Counter
from fractions import Fraction
ROOT = '<repo-old>'
DATE = '2026-09-11'
UNITS3 = [('num_28_daily_shabbat_rosh', 28, 1, 15, [142, 143, 144, 145]), ('num_28_pesach_shavuot', 28, 16, 31, [146, 147, 148, 149]), ('num_29_fall_festivals', 29, 1, 39, [150, 151, 152])]
TITLES = {'num_28_daily_shabbat_rosh': 'the offerings calendar opens — My offering, My bread, in its appointed time; the daily lambs, one in the morning and the second at dusk, the tenth of the ephah and the quarter hin, the burnt offering made at Mount Sinai; the Sabbath\'s two lambs; the new moon\'s two bulls, a ram, seven lambs, the master table of tenths and hins, and the one goat "a sin offering to the LORD"',
          'num_28_pesach_shavuot': 'the fourteenth day is Pesach, the fifteenth a festival of seven days of unleavened bread; the first and seventh days holy convocations, no laborious work; the festival offering two bulls, a ram, seven lambs, a goat, "as these" each day beside the continual; the day of the firstfruits, a new meal offering, in your weeks — the same table',
          'num_29_fall_festivals': 'the seventh month: the first day a day of blowing, the tenth the affliction with the sin offering of the atonements, the fifteenth the festival of seven days with thirteen bulls falling to seven, two rams, fourteen lambs and a goat each day, the libations spelled in three deviant letters, the eighth day an assembly; these you shall do besides your vows'}
OUTS = {uid: f'{ROOT}/logic/oral_triage/{uid}_{DATE}.md' for uid, *_ in UNITS3}

def clean(s): return re.sub(r'<[^>]+>', '', html.unescape(s))
sif = json.load(open(f'{ROOT}/Data/sefaria_export/Sifrei_Bamidbar/en.json'))['text']
sif_he = json.load(open(f'{ROOT}/Data/sefaria_export/Sifrei_Bamidbar/he.json'))['text']
onk = json.load(open(f'{ROOT}/Data/sefaria_export/Onkelos_Numbers/en.json'))['text']
onk_he = json.load(open(f'{ROOT}/Data/sefaria_export/Onkelos_Numbers/he.json'))['text']
heads = {}
for p, rows in enumerate(sif, 1):
    if not rows: continue
    m = re.search(r'\((Bamidbar|Devarim)\.? (\d+):(\d+)', clean(rows[0])[:60])
    heads[p] = (m.group(1), int(m.group(2)), int(m.group(3))) if m else None
# THE SHELF'S ROWS ON CHAPTERS 28-29, BY POSITION: ELEVEN piskaot 142-152, twenty-three rows — 142 on 28:1 (five rows: the king's parable,
# My offering / My bread / My fires / My savor, "in its appointed time" the identity with the Pesach, "two per day" ben Azzai's opposite-the-day,
# "the one lamb" not more, the tenth and the wheat and the beaten oil), 143 on 28:6 (three: the Sinai olah likened to the tamid, the libation
# unmixed and the water, the second lamb — the order of the day, the inauguration, the Name on the offerings), 144 on 28:9 (two: the Sabbath's
# musaf and the service overriding the Sabbath; "on its Sabbath"), 145 on 28:11 (three: the new moon's own number; the hin's marks; "in its
# month"; the goat for the grave of the deep), 146 on 28:16 (one: mandatory; the five grains), 147 on 28:18 (two: the holy convocation and the
# food-work; "as these" — Pesach does not decrease as Sukkot does), 148 on 28:26 (one: the fiftieth day; the new meal offering; R. Tarfon and
# Yehudah b. Nachman), 149 on 28:27 (two: these besides Leviticus's; the libations likened to the animal), 150 on 29:12 (one: mandatory;
# "even one"; THE WATER LIBATION — three derivations), 151 on 29:35 (two: the atzeret as withholding; "even one"), 152 on 29:39 (one: the vows
# of the festival; "and Moses said" closes the matter). NO piska on 29:1-11 (the day of blowing and the day of atonement — computed on every
# head: 149 heads 28:27, 150 heads 29:12) nor on 29:13-34 (the seven days' table — 150's one row covers 29:12-13 and reaches 29:19-33 for
# the letters). The next head, 153, is 30:2 (the vows — the next draft).
assert heads[141] == ('Bamidbar', 27, 21) and heads[142] == ('Bamidbar', 28, 1) and heads[149] == ('Bamidbar', 28, 27) and heads[150] == ('Bamidbar', 29, 12) and heads[152] == ('Bamidbar', 29, 39) and heads[153] == ('Bamidbar', 30, 2), [heads[p] for p in (141, 142, 149, 150, 152, 153)]
assert {p: heads[p][1:] for p in range(142, 153)} == {142: (28, 1), 143: (28, 6), 144: (28, 9), 145: (28, 11), 146: (28, 16), 147: (28, 18), 148: (28, 26), 149: (28, 27), 150: (29, 12), 151: (29, 35), 152: (29, 39)}
assert sorted(p for p, h in heads.items() if h and h[0] == 'Bamidbar' and h[1] in (28, 29)) == list(range(142, 153)) and [p for p in range(138, 156) if heads.get(p) is None] == []
PISKAOT = list(range(142, 153))
SIF_ROWS = {p: len(sif[p - 1]) for p in PISKAOT}
assert SIF_ROWS == {142: 5, 143: 3, 144: 2, 145: 3, 146: 1, 147: 2, 148: 1, 149: 2, 150: 1, 151: 2, 152: 1} and {p: len(sif_he[p - 1]) for p in PISKAOT} == SIF_ROWS, SIF_ROWS
assert sum(SIF_ROWS.values()) == 23
def head(p): return heads[p][1:]
# THE ROWS' OWN DEFECTS, read to their verses (RESEARCH_LOG.md): (a) 149:1's HEBREW proof-text reads "bulls, sons of the herd, TWELVE, rams two"
# — Sukkot's second day (29:17) — where the row expounds 28:27's "two bulls, one ram" (the English has it right): the Hebrew row's quotation
# garbled; (b) 142:2's English DROPS A SPEAKER — the Hebrew has R. Yoshiyah answering R. Yonatan's objection ("said R. Yoshiyah to him") with the
# identity of "in its appointed time"; the English runs the answer into R. Yonatan's speech; (c) 147:1, 149:1, 150:1, 151:2's "even one" is
# derived in the Hebrew from LEVITICUS 23's "seven days you shall offer a fire-offering" (23:8, 23:36) — the English rewrites the citation as
# the Numbers verse at 147:1 and 149:1 ("It is, therefore, written 'And you shall present a fire-offering'"), keeps Leviticus at 150:1; (d)
# 150:1's "R. Yehudah" is R. YEHUDAH BEN BETEIRA in the Hebrew (the water-libation letters); (e) 143:3's Hebrew "and not that of the FESTIVAL
# except with the showbread on the Sabbath" reads של חג where the sense (and the English) is the TABLE (השלחן) — a garbled word; and the
# English inserts "When is this so? When the altar had not been inaugurated..." — a clause the Hebrew row does not carry (the Mishnah's answer
# supplied by the translator); (f) 147:1's Hebrew derives the food-work permission by the IDENTITY "holy convocation" (here and Exodus 12:16) —
# the English cites Exodus 12:16 without the middah.
assert 'שנים עשר אילים שנים' in clean(sif_he[148][0]) and 'two young bullocks, and one ram' in clean(sif[148][0])
assert 'נאם לו ר\' יאשיה' in clean(sif_he[141][1]) and 'R. Yonathan said: In this sense' in clean(sif[141][1]) and 'R. Yoshiyah said' not in clean(sif[141][1])
assert all('שבעת ימים תקריבו אשה' in clean(sif_he[p - 1][r - 1]) or 'ז\' ימים תקריבו אשה' in clean(sif_he[p - 1][r - 1]) for p, r in ((147, 1), (149, 1), (150, 1), (151, 2)))
assert 'Vayikra 23:36' in clean(sif[149][0]) and '"And you shall present a fire-offering," implying even one' in clean(sif[146][0])
assert 'ר\' יהודה בן בתירה' in clean(sif_he[149][0]) and 'R. Yehudah says' in clean(sif[149][0]) and 'Beteira' not in clean(sif[149][0])
assert 'ולא את של חג' in clean(sif_he[142][2]) and 'When the altar had not been inaugurated' in clean(sif[142][2]) and 'נתחנך' not in clean(sif_he[142][2])
assert 'נאמר כאן מקרא קודש' in clean(sif_he[146][0]) and 'Shemot 12:16' in clean(sif[146][0])
def plain(w): return ''.join(c for c in w if c != '/' and not (0x0591 <= ord(c) <= 0x05C7))
def pointed(w): return ''.join(c for c in w if c != '/' and not (0x0591 <= ord(c) <= 0x05AF))
ONK_LEN = {c: len(onk[c - 1]) for c in (27, 28, 29, 30)}
assert ONK_LEN == {27: 23, 28: 31, 29: 39, 30: 17} and {c: len(onk_he[c - 1]) for c in (27, 28, 29, 30)} == ONK_LEN, ONK_LEN
def onk_ev(c, v): return clean(onk[c - 1][v - 1]), clean(onk_he[c - 1][v - 1])
shelf_numbers = sorted(d for d in os.listdir(f'{ROOT}/Data/sefaria_export') if re.search(r'Numbers|Bamidbar', d))
outside = [d for d in shelf_numbers if d not in ('Sifrei_Bamidbar', 'Onkelos_Numbers')]
assert len(outside) == 23, len(outside)
# THE PRIOR READS: no ledger has read an Onkelos row of 28 or 29, none a Sifrei row of 142-152 (the moadim, the shekel, the naso and the
# shelach dockets NAME verses of 28-29 as cross-references — a name is not a read); FRESH
TRI = f'{ROOT}/logic/oral_triage'
LED = {f: open(f'{TRI}/{f}', encoding='utf-8').read() for f in os.listdir(TRI) if f.endswith('.md') and os.path.isfile(f'{TRI}/{f}') and f'{TRI}/{f}' not in OUTS.values()}
assert sorted(f for f, t in LED.items() if re.search(r'^- Onkelos Num 2[89]:\d', t, re.M)) == [] and sorted(f for f, t in LED.items() if re.search(r'Sifrei (?:Bamidbar )?1(4[2-9]|5[0-2]):\d', t)) == []
NAMING = sorted(f for f, t in LED.items() if re.search(r'Num(?:bers)? 2[89]:\d+', t))
assert len(NAMING) == 23 and 'lev_23_festivals_2026-09-05.md' in NAMING and 'num_15_offerings_laws_2026-09-10.md' in NAMING, (len(NAMING), NAMING[:5])

# ---- THE DRAFTS' SPANS, COMPUTED ----
db = sqlite3.connect(f'file:{ROOT}/elijah_docket/tanakh.sqlite?mode=ro', uri=True)
VC = dict(db.execute("SELECT chapter, COUNT(*) FROM verses WHERE book='Num' GROUP BY chapter").fetchall())
assert VC[28] == 31 and VC[29] == 39 and VC[30] == 17
def unit_text(uid): return open(f'{ROOT}/logic/units/{uid}.yaml', encoding='utf-8').read()
def steps(uid): return sorted({(int(a), int(b)) for a, b in re.findall(r'STEP_Nm_(\d+)_(\d+)', unit_text(uid))})
for uid, c, lo, hi, _ in UNITS3:
    assert steps(uid) == [(c, v) for v in range(lo, hi + 1)] and 'status: draft' in unit_text(uid) and 'operators:' not in unit_text(uid), uid
assert steps('num_30_vows')[0] == (30, 1) and 'status: frozen' in unit_text('num_27_zelophehad_joshua')
SPAN = [(28, v) for v in range(1, 32)] + [(29, v) for v in range(1, 40)]
SPAN_OF = {uid: [(c, v) for v in range(lo, hi + 1)] for uid, c, lo, hi, _ in UNITS3}

# ---- THE INK, computed from the Tanakh DB and the snapshot store ----
def accents(w): return [unicodedata.name(c).replace('HEBREW ACCENT ', '') for c in w if 0x0591 <= ord(c) <= 0x05AE]
rows = db.execute("SELECT v.book, v.chapter, v.verse, w.he, w.morph FROM words w JOIN verses v ON w.verse_id=v.id ORDER BY v.id, w.idx").fetchall()
by, byp, byraw = {}, {}, {}
for b, c, v, he, m in rows:
    by.setdefault((b, c, v), []).append((plain(he), m)); byp.setdefault((b, c, v), []).append(pointed(he)); byraw.setdefault((b, c, v), []).append(he)
T = ('Gen', 'Exod', 'Lev', 'Num', 'Deut')
def words(b, c, v): return [x for x, _ in by[(b, c, v)]]
def hits(sub, books=None, exact=False): return sorted({f'{b} {c}:{v}' for (b, c, v), ws in by.items() if (books is None or b in books) and any((x == sub) if exact else (sub in x) for x, _ in ws)})
def count_tok(tok, books=None): return sum(1 for (b, c, v), ws in by.items() if (books is None or b in books) for x, _ in ws if x == tok)
def phrase(seq, books=T):
    out = []
    for (b, c, v), ws in by.items():
        if books is not None and b not in books: continue
        w = [x for x, _ in ws]
        if any(w[i:i + len(seq)] == list(seq) for i in range(len(w) - len(seq) + 1)): out.append(f'{b} {c}:{v}')
    return sorted(out)
def key(s):
    b, cv = s.split(' '); c, v = cv.split(':'); return (b, int(c), int(v))
def pt(b, c, v, tok, nth=0):
    w, wp = words(b, c, v), byp[(b, c, v)]
    idx = [i for i, x in enumerate(w) if x == tok]
    return wp[idx[nth]] if len(idx) > nth else None
def npt(s): return unicodedata.normalize('NFC', s) if isinstance(s, str) else s
def U(*toks, books=None): return sorted(set(s for t in toks for s in hits(t, books, True)))
FAIL = []
def H(c, v, *cons):
    w, wp = words('Num', c, v), byp[('Num', c, v)]
    out, i = [], 0
    for k in cons:
        j = i
        while j < len(w) and w[j] != k: j += 1
        if j >= len(w): FAIL.append(('H', c, v, k)); out.append('⟨MISS⟩'); continue
        out.append(wp[j]); i = j + 1
    return ' '.join(out)
def A(c, v, *cons):
    ws = onk_ev(c, v)[1].rstrip(':').split()
    out, i = [], 0
    for k in cons:
        j = i
        while j < len(ws) and plain(ws[j]) != k: j += 1
        if j >= len(ws): FAIL.append(('A', c, v, k, [plain(x) for x in ws])); out.append('⟨MISS⟩'); continue
        out.append(ws[j]); i = j + 1
    return ' '.join(out)
def aramaic(c, v): return [plain(x) for x in onk_ev(c, v)[1].rstrip(':').split()]
def HP(c, v, *pieces):
    """the Hebrew cut in GLOSSED PIECES — each piece a (tokens, gloss) pair of at most six tokens, the gloss right after it (the lint's window)"""
    out = []
    for toks, gloss in pieces:
        assert len(toks) <= 7, (c, v, toks)
        out.append(f'"{H(c, v, *toks)}" ({gloss})')
    return ' '.join(out)
def AP(c, v, *pieces):
    """the Aramaic cut in glossed pieces, as HP"""
    out = []
    for toks, gloss in pieces:
        assert len(toks) <= 7, (c, v, toks)
        out.append(f'{A(c, v, *toks)} ({gloss})')
    return ' '.join(out)
store = sqlite3.connect(f'file:{ROOT}/torah_grok.SNAPSHOT-main-51801ca.sqlite?mode=ro', uri=True)
SG = {}
for c, v, hp, g in store.execute("SELECT v.chapter, v.verse, w.he_plain, w.gloss FROM words w JOIN verses v ON w.verse_id=v.id WHERE v.book='Num' AND v.chapter IN (28, 29, 30) ORDER BY v.id, w.idx"):
    SG.setdefault((c, v), []).append((hp.replace('/', ''), g))
def sg(c, v, tok):
    for hp, g in SG[(c, v)]:
        if hp == tok: return g
    raise KeyError((c, v, tok))

# THE ENGINE'S PARSER on every number of the two chapters — MEASURED before the compile is asked (the standing rule)
sys.path.insert(0, f'{ROOT}/World/step9')
with contextlib.redirect_stdout(io.StringIO()):
    import cold_run_sequence as CS
def N(b, c, v): return CS.ink_numbers(CS.verse_words(b, c, v))
def O(b, c, v): return CS.ink_ordinals(CS.verse_words(b, c, v))
Q = Fraction
RIGHT = {(c, v): N('Num', c, v) for (c, v) in SPAN if N('Num', c, v)}
EXPECT = {(28, 3): [2], (28, 4): [1], (28, 5): [Q(1, 10), Q(1, 4)], (28, 7): [Q(1, 4), 1], (28, 9): [2, 2], (28, 11): [2, 1, 7], (28, 12): [3, 1, 2, 1], (28, 13): [1, 1], (28, 14): [Q(1, 2), Q(1, 3), Q(1, 4)], (28, 15): [1], (28, 16): [14], (28, 17): [15, 7], (28, 19): [2, 8], (28, 20): [3, 2], (28, 21): [1, 1, 7], (28, 22): [1], (28, 24): [7], (28, 27): [2, 1, 7], (28, 28): [3, 1, 2, 1], (28, 29): [1, 1, 7], (28, 30): [1],
          (29, 1): [1], (29, 2): [1, 1, 7], (29, 3): [3, 2], (29, 4): [1, 1, 7], (29, 5): [1], (29, 8): [1, 1, 7], (29, 9): [3, 2, 1], (29, 10): [1, 1, 7], (29, 11): [1], (29, 12): [15, 7], (29, 13): [13, 2, 14], (29, 14): [3, 1, 13, 2, 1, 2], (29, 15): [1, 1, 14], (29, 16): [1], (29, 17): [12, 2, 14], (29, 19): [1], (29, 20): [11, 2, 14], (29, 22): [1], (29, 23): [10, 2, 14], (29, 25): [1], (29, 26): [9, 2, 14], (29, 28): [1], (29, 29): [8, 2, 14], (29, 31): [1], (29, 32): [7, 2, 14], (29, 34): [1], (29, 36): [1, 1, 7], (29, 38): [1]}
assert RIGHT == EXPECT, {k: (RIGHT.get(k), EXPECT.get(k)) for k in set(RIGHT) | set(EXPECT) if RIGHT.get(k) != EXPECT.get(k)}
ORD = {(c, v): O('Num', c, v) for (c, v) in SPAN if O('Num', c, v)}
assert ORD == {(28, 4): [2], (28, 8): [2], (28, 16): [1], (28, 18): [1], (28, 25): [7], (29, 1): [7], (29, 7): [7], (29, 12): [7], (29, 17): [2], (29, 20): [3], (29, 23): [4], (29, 26): [5], (29, 29): [6], (29, 32): [7], (29, 35): [8]}, ORD
# TWO GAPS on the chapters' own numbers, named for the compile: (23) THE DISJUNCTIVE ON "ONE" BEFORE "AND + NUMERAL" — 28:19 "and one ram
# AND SEVEN lambs" read as [2, 8]: the etnachta on אֶחָד ("one") — the verse's strongest pause — is NOT emitted as the bar, because the bar
# rule (M-26, 2b) fires only before a BARE numeral, and here the numeral carries the conjunction; the phrase joins across the pause. The
# same clause at 28:11 ("one ram; lambs sons of a year, seven") and 28:27 ("one ram, seven lambs" — the etnachta on "one" before the bare
# "seven" DOES take the bar, [2, 1, 7]) reads right by the noun between or the bare form. The ink's one seat of the adjacent pair "one
# and-seven" in the Bible. (24) THE PLENE TENTH-DAY NOUN — 29:7 בֶּעָשׂוֹר ("on the tenth [day]") spelled with the vav is SILENT; the
# defective בֶּעָשֹׂר of Exodus 12:3 reads 10 (rule 16); the plene form's Torah seats Leviticus 16:29, 23:27, 25:9, Numbers 29:7 (and six in
# Joshua, Kings, Jeremiah, Ezekiel) — every one silent; the ordinal "the seventh [month]" beside it read right.
assert [(plain(w), accents(w)) for w in byraw[('Num', 28, 19)] if plain(w) in ('אחד', 'ושבעה', 'שנים')] == [('שנים', ['TIPEHA']), ('אחד', ['ETNAHTA']), ('ושבעה', ['MAHAPAKH'])]
assert [(plain(w), accents(w)) for w in byraw[('Num', 28, 27)] if plain(w) in ('אחד', 'שבעה')] == [('אחד', ['ETNAHTA']), ('שבעה', ['MERKHA'])] and 'אחד|' in CS.verse_words('Num', 28, 27) and 'אחד|' not in CS.verse_words('Num', 28, 19)
assert phrase(['אחד', 'ושבעה'], None) == ['Num 28:19'] and words('Num', 28, 11)[8:15] == ['שנים', 'ואיל', 'אחד', 'כבשים', 'בני', 'שנה', 'שבעה']
assert U('בעשור') == ['2Kgs 25:1', 'Ezek 20:1', 'Ezek 24:1', 'Ezek 40:1', 'Jer 52:12', 'Jer 52:4', 'Josh 4:19', 'Lev 16:29', 'Lev 23:27', 'Lev 25:9'] + [] if False else sorted(U('בעשור') + ['Num 29:7'] if 'Num 29:7' not in U('בעשור') else U('בעשור')) == ['2Kgs 25:1', 'Ezek 20:1', 'Ezek 24:1', 'Ezek 40:1', 'Jer 52:12', 'Jer 52:4', 'Josh 4:19', 'Lev 16:29', 'Lev 23:27', 'Lev 25:9', 'Num 29:7']
assert U('ובעשור') == ['Num 29:7'] and U('בעשר') == ['Exod 12:3', 'Neh 10:39'] and N('Exod', 12, 3) == [10] and N('Lev', 16, 29) == [] and N('Lev', 23, 27) == [] and N('Lev', 25, 9) == [] and N('Num', 29, 7) == []
GAPS = {'(23) the disjunctive on "one" before "and + numeral"': 'Num 28:19 [2, 8] for [2, 1, 7] — the etnachta on "one" not emitted as the bar before a conjoined numeral', '(24) the plene tenth-day noun': 'Num 29:7 בעשור silent (Lev 16:29, 23:27, 25:9 the same form; Exod 12:3 defective reads 10)'}
assert phrase(['עשתי', 'עשר'], None) == ['1Chr 12:14', '1Chr 24:12', '1Chr 25:18', '1Chr 27:14', 'Num 29:20', 'Num 7:72'] and N('Num', 29, 20)[0] == 11   # 2b's "eleven" at its second Torah seat
NUMV = sorted(set(RIGHT) | set(ORD)); assert len(NUMV) == 54 and len(RIGHT) == 49 and len(ORD) == 15, (len(NUMV), len(RIGHT), len(ORD))   # fifty-four number verses: forty-nine with cardinals, fifteen with ordinals, ten with both

# THE FRAMES AND THE REGISTER: ONE frame in seventy verses — 28:1 "the LORD spoke to Moses, saying" — and ONE narrative verb (it); the
# whole span the LORD's speech; 30:1 "and Moses said to the children of Israel according to all that the LORD commanded Moses" closes
# the portion (the Sifrei 152:1: "to conclude the matter" — R. Yishmael), read with the next draft
FR = [(c, v) for (c, v) in SPAN if words('Num', c, v)[0] in ('וידבר', 'ויאמר')]
REG = {(c, v): [(x, m) for x, m in by[('Num', c, v)] if m and re.search(r'V.w', m)] for (c, v) in SPAN}
assert FR == [(28, 1)] and {k: v for k, v in REG.items() if v} == {(28, 1): [('וידבר', 'HC/Vpw3ms')]} and sg(28, 1, 'וידבר') == 'and-speak'
assert words('Num', 30, 1) == ['ויאמר', 'משה', 'אל', 'בני', 'ישראל', 'ככל', 'אשר', 'צוה', 'יהוה', 'את', 'משה'] and words('Num', 28, 2)[:4] == ['צו', 'את', 'בני', 'ישראל']

# THE TAMID (28:2-8): "My offering, My bread for My fire-offerings, My pleasing aroma" — four possessives, three of them one-seat forms;
# "in its appointed time" three Torah seats (the Pesach's 9:2, 9:3 and this — the Sifrei's identity, 142:2); "two per day" here and
# Exodus 29:38 (ben Azzai's "opposite the day"); the Exodus tamid restated (29:38-42) — 28:4 = 29:39 but for "the one" losing its article,
# 28:5 names "the ephah" where 29:40 says "a tenth-part", "beaten oil" at both, "strong drink" for 29:40's "wine", "made at Mount Sinai"
# added (28:6, the participle's one seat), "in the holy place" added (28:7); 28:8 = 29:41's "as the meal offering of the morning"
assert [x for x in words('Num', 28, 2) if x in ('קרבני', 'לחמי', 'לאשי', 'ניחחי')] == ['קרבני', 'לחמי', 'לאשי', 'ניחחי'] and U('קרבני') == ['Num 28:2'] and U('לאשי') == ['Num 28:2'] and U('ניחחי') == ['Num 28:2'] and 'Num 28:2' in U('לחמי') and len(U('לחמי')) == 10
assert U('במועדו') == ['Hos 2:11', 'Num 28:2', 'Num 9:2', 'Num 9:3'] and phrase(['שנים', 'ליום'], None) == ['Exod 29:38', 'Num 28:3']
assert phrase(['עלה', 'תמיד'], None) == ['Num 28:3', 'Ps 74:23'] and phrase(['עלת', 'תמיד'], None) == ['Exod 29:42', 'Ezra 3:5', 'Num 28:6'] and phrase(['עלת', 'התמיד'], None) == ['Num 28:10', 'Num 28:15', 'Num 28:31', 'Num 29:16', 'Num 29:19', 'Num 29:22', 'Num 29:25', 'Num 29:28', 'Num 29:31', 'Num 29:34', 'Num 29:38']
assert words('Num', 28, 4) == ['את', 'הכבש', 'אחד', 'תעשה', 'בבקר', 'ואת', 'הכבש', 'השני', 'תעשה', 'בין', 'הערבים'] and words('Exod', 29, 39) == ['את', 'הכבש', 'האחד', 'תעשה', 'בבקר', 'ואת', 'הכבש', 'השני', 'תעשה', 'בין', 'הערבים']
assert words('Num', 28, 5) == ['ועשירית', 'האיפה', 'סלת', 'למנחה', 'בלולה', 'בשמן', 'כתית', 'רביעת', 'ההין'] and words('Exod', 29, 40)[:7] == ['ועשרן', 'סלת', 'בלול', 'בשמן', 'כתית', 'רבע', 'ההין'] and words('Exod', 29, 40)[7:] == ['ונסך', 'רבעית', 'ההין', 'יין', 'לכבש', 'האחד']
assert phrase(['בשמן', 'כתית'], None) == ['Exod 29:40', 'Num 28:5'] and U('כתית') == ['1Kgs 5:25', 'Exod 27:20', 'Exod 29:40', 'Lev 24:2', 'Num 28:5']
assert U('העשיה') == ['Num 28:6'] and phrase(['נסך', 'שכר'], None) == ['Num 28:7'] and U('הסך') == ['Num 28:7'] and U('שכר', 'ושכר', 'לשכר', books=T) == ['Deut 15:18', 'Deut 23:5', 'Deut 29:5', 'Gen 30:16', 'Lev 10:9', 'Num 18:31', 'Num 28:7', 'Num 6:3']   # the wage-homograph at Gen 30:16, Deut 15:18, 23:5, Num 18:31
assert phrase(['כמנחת', 'הבקר'], None) == ['Exod 29:41', 'Num 28:8'] and words('Exod', 29, 41)[:9] == ['ואת', 'הכבש', 'השני', 'תעשה', 'בין', 'הערבים', 'כמנחת', 'הבקר', 'וכנסכה']
assert aramaic(28, 2)[8:10] == ['לחם', 'סדור'] and aramaic(28, 5)[:5] == ['וחד', 'מן', 'עשרא', 'בתלת', 'סאין'] and aramaic(28, 7)[7:10] == ['נסוך', 'דחמר', 'עתיק']   # ARRANGED bread; ONE OF TEN IN THREE SEAHS (the ephah converted); OLD WINE for strong drink

# THE SABBATH AND THE NEW MOON (28:9-15): Leviticus 23:3's Sabbath has NO offering — 28:9-10 gives it two lambs and two tenths, "the burnt
# offering of the Sabbath on its Sabbath" (one seat); the new moon is ABSENT from Leviticus 23 — 28:11-15 gives it two bulls, a ram, seven
# lambs, the MASTER TABLE of tenths (3 / 2 / 1) and hins (1/2 / 1/3 / 1/4) that every later day cites "according to the ordinance", and "the
# burnt offering of the month in its month" (one seat); the two "X in its X" forms stand together elsewhere in ONE verse, Isaiah 66:23;
# "at the beginnings of your months" here and at the trumpets (10:10); "for the months of the year" here and Exodus 12:2; the goat "a sin
# offering TO THE LORD" — the new moon's alone of the thirteen goats of the two chapters (the exam's Shevuot 9a)
assert phrase(['עלת', 'שבת', 'בשבתו'], None) == ['Num 28:10'] and phrase(['עלת', 'חדש', 'בחדשו'], None) == ['Num 28:14'] and U('בשבתו') == ['Isa 66:23', 'Num 28:10', 'Prov 31:23'] and U('בחדשו') == ['Isa 66:23', 'Num 28:14']
assert phrase(['ובראשי', 'חדשיכם'], None) == ['Num 10:10', 'Num 28:11'] and phrase(['לחדשי', 'השנה'], None) == ['Exod 12:2', 'Num 28:14'] and [v for v in range(1, 45) if any(x in ('חדש', 'החדש', 'חדשיכם', 'ובראשי') for x in words('Lev', 23, v))] == []
assert N('Num', 28, 12) == [3, 1, 2, 1] and N('Num', 28, 13) == [1, 1] and N('Num', 28, 14) == [Q(1, 2), Q(1, 3), Q(1, 4)] and [(v, N('Num', 15, v)) for v in (4, 6, 9)] == [(4, [1, Q(1, 4)]), (6, [2, Q(1, 3)]), (9, [3, Q(1, 2)])]   # the table of 15:4-10 restated per animal
assert phrase(['חצי', 'ההין'], None) == ['Num 15:10', 'Num 15:9', 'Num 28:14'] and phrase(['שלישת', 'ההין'], None) == [] and U('ושלישת') == ['Num 28:14'] and phrase(['רביעת', 'ההין'], None) == ['Lev 23:13', 'Num 28:5', 'Num 28:7']
GOATS = [(c, v, words('Num', c, v)[:6]) for (c, v) in SPAN if any(x in ('ושעיר', 'שעיר') for x in words('Num', c, v))]
assert len(GOATS) == 13 and [(c, v) for c, v, w in GOATS if 'ליהוה' in w] == [(28, 15)] and phrase(['לחטאת', 'ליהוה'], None) == ['Num 28:15']
assert [(c, v) for c, v, w in GOATS if 'לכפר' in w] == [(28, 22), (28, 30), (29, 5)] and [(c, v) for c, v, w in GOATS if w[:4] == ['ושעיר', 'חטאת', 'אחד', 'מלבד'] or w[:3] == ['ושעיר', 'חטאת', 'אחד']] == [(28, 22), (29, 22), (29, 28), (29, 31), (29, 34), (29, 38)]
assert aramaic(28, 14)[15:17] == ['ירחא', 'באתחדתותיה'] and aramaic(28, 15)[:4] == ['וצפיר', 'בר', 'עזי', 'חד']

# PESACH AND SHAVUOT (28:16-31): the dates of Leviticus 23:5-6 with "at dusk" dropped and "the festival of unleavened bread to the LORD"
# shortened to "a festival"; 28:18 = 23:7 word for word; "no laborious work" at 28:18, 25, 26 and 29:1, 12, 35 — the six festival days —
# against Yom Kippur's "no work" at 29:7 (Leviticus 23:3's Sabbath and 23:31's atonement the other seats of the bare form); "besides"
# twelve times in the two chapters of the Torah's twenty — the musaf STACKS on the tamid; "as these you shall do each day" one seat (the
# Sifrei 147:2: Pesach does not decrease as Sukkot does); "the day of the firstfruits ... a new meal offering ... in your weeks" — "in
# your weeks" one seat, and ONKELOS RENDERS IT "IN YOUR ASSEMBLIES" (עצרת — the Mishnah's own name for Shavuot in the translation's mouth);
# the three musaf tables of 28 identical (2, 1, 7; the parser's [2, 8] at 28:19 the gap)
assert words('Num', 28, 16) == ['ובחדש', 'הראשון', 'בארבעה', 'עשר', 'יום', 'לחדש', 'פסח', 'ליהוה'] and [x for x in words('Lev', 23, 5) if x not in words('Num', 28, 16)] == ['בחדש', 'בין', 'הערבים'] and [x for x in words('Lev', 23, 6) if x not in words('Num', 28, 17)] == ['המצות', 'ליהוה', 'תאכלו']
assert words('Num', 28, 18) == ['ביום', 'הראשון', 'מקרא', 'קדש', 'כל', 'מלאכת', 'עבדה', 'לא', 'תעשו'] and [x for x in words('Lev', 23, 7) if x not in words('Num', 28, 18)] == ['יהיה', 'לכם'] and all(x in words('Lev', 23, 7) for x in words('Num', 28, 18)) and words('Lev', 23, 7)[4:6] == ['יהיה', 'לכם']   # 23:7's "shall be to you" sits after "holy convocation"; 28:18 drops it and keeps the nine
assert phrase(['כל', 'מלאכת', 'עבדה', 'לא', 'תעשו'], None) == ['Lev 23:21', 'Lev 23:25', 'Lev 23:35', 'Lev 23:36', 'Lev 23:7', 'Lev 23:8', 'Num 28:18', 'Num 28:25', 'Num 28:26', 'Num 29:1', 'Num 29:12', 'Num 29:35'] and phrase(['כל', 'מלאכה', 'לא', 'תעשו'], None) == ['Lev 23:3', 'Lev 23:31', 'Num 29:7']
assert phrase(['מקרא', 'קדש'], ('Num',)) == ['Num 28:18', 'Num 28:25', 'Num 28:26', 'Num 29:1', 'Num 29:12', 'Num 29:7'] and len(phrase(['מקרא', 'קדש'], None)) == 15
assert [(c, v) for (c, v) in SPAN if 'מלבד' in words('Num', c, v)] == [(28, 23), (28, 31), (29, 6), (29, 11), (29, 16), (29, 19), (29, 22), (29, 25), (29, 28), (29, 31), (29, 34), (29, 38)] and len(U('מלבד', books=T)) == 20
assert phrase(['כאלה', 'תעשו', 'ליום'], None) == ['Num 28:24'] and phrase(['לחם', 'אשה'], None) == ['Lev 3:11', 'Lev 3:16', 'Num 28:24'] and phrase(['מצות', 'יאכל'], None) == ['Exod 13:7', 'Ezek 45:21', 'Num 28:17']
assert phrase(['מנחה', 'חדשה'], None) == ['Lev 23:16', 'Num 28:26'] and U('בשבעתיכם') == ['Num 28:26'] and phrase(['יום', 'הבכורים'], None) == [] and words('Num', 28, 26)[:2] == ['וביום', 'הבכורים'] and aramaic(28, 26)[7] == 'בעצרתיכון'
assert N('Num', 28, 11) == N('Num', 28, 27) == [2, 1, 7] and N('Num', 28, 19) == [2, 8] and phrase(['תמימם', 'יהיו', 'לכם'], None) == ['Num 28:19', 'Num 28:31', 'Num 29:8']

# TISHRI (29:1-39): "a day of blowing" one seat (Leviticus 23:24 says "a memorial of blowing"), ONKELOS "A DAY OF WAILING" — the teruah
# rendered a wail (sitting 3's finding at 10:5-6, at its third seat); 29:6 the triple stack "besides the burnt offering of the month and
# the continual" — "according to their ordinance" (כמשפטם) here and at the seventh day of Sukkot alone in the two chapters; 29:7 "you shall
# afflict your souls" (Leviticus 16:31, 23:27, 23:32 the kin; 16:29 "you shall afflict"), ONKELOS "YOU SHALL FAST"; "the sin offering of the
# atonements" (29:11) here and Exodus 30:10 (the incense altar's yearly blood) — the pointer to Leviticus 16's goat; 29:12 "you shall
# celebrate a festival to the LORD seven days" one seat (Leviticus 23:41's "celebrate it"); THE SEVEN DAYS: bulls 13, 12, 11, 10, 9, 8, 7 —
# SEVENTY (computed), rams two and lambs fourteen every day, a goat every day — the per-day tenths and hins by the master table computed:
# 21 ephahs for the bulls, 2 4/5 for the rams, 9 4/5 for the lambs; 64 1/6 hins; the eighth day (29:35-38) one bull, one ram, seven lambs,
# one goat — the new moon's number without the second bull; "assembly" (עצרת) three Torah seats — Leviticus 23:36 and this for the eighth
# day, Deuteronomy 16:8 for PESACH'S SEVENTH; ONKELOS "A GATHERING"; 29:39 "these you shall do to the LORD in your appointed times besides
# your vows and your freewill offerings" — Leviticus 23:37-38's close ("besides the Sabbaths of the LORD and besides your gifts... vows...
# freewill offerings") at its second seat, the four offering-kinds listed; ONKELOS "the sacrifices of your holy things" for peace offerings
assert phrase(['יום', 'תרועה'], None) == ['Num 29:1'] and phrase(['זכרון', 'תרועה'], None) == ['Lev 23:24'] and U('תרועה', books=T) == ['Lev 23:24', 'Lev 25:9', 'Num 10:5', 'Num 10:6', 'Num 29:1'] and aramaic(29, 1)[13:15] == ['יום', 'יבבא']
assert words('Num', 29, 6)[:7] == ['מלבד', 'עלת', 'החדש', 'ומנחתה', 'ועלת', 'התמיד', 'ומנחתה'] and U('כמשפטם', books=T) == ['Num 29:33', 'Num 29:6'] and U('כמשפט', books=('Num',)) == ['Num 15:24', 'Num 29:18', 'Num 29:21', 'Num 29:24', 'Num 29:27', 'Num 29:30', 'Num 29:37']
assert phrase(['ועניתם', 'את', 'נפשתיכם'], None) == ['Lev 16:31', 'Lev 23:27', 'Lev 23:32', 'Num 29:7'] and phrase(['תענו', 'את', 'נפשתיכם'], None) == ['Lev 16:29'] and aramaic(29, 7)[8] == 'ותענון'
assert phrase(['חטאת', 'הכפרים'], None) == ['Exod 30:10', 'Num 29:11'] and phrase(['וחגתם', 'חג', 'ליהוה'], None) == ['Num 29:12'] and phrase(['תחגו', 'אתו'], None) == ['Lev 23:41']
BULLS = {v: N('Num', 29, v) for v in (13, 17, 20, 23, 26, 29, 32)}
assert [BULLS[v][0] for v in (13, 17, 20, 23, 26, 29, 32)] == [13, 12, 11, 10, 9, 8, 7] and sum(BULLS[v][0] for v in BULLS) == 70 and all(BULLS[v][1:] == [2, 14] for v in BULLS)
assert [N('Num', 29, v) for v in (16, 19, 22, 25, 28, 31, 34, 38)] == [[1]] * 8 and N('Num', 29, 36) == [1, 1, 7]
TENTHS = (Q(3, 10) * 70, Q(2, 10) * 14, Q(1, 10) * 98); HINS = Q(1, 2) * 70 + Q(1, 3) * 14 + Q(1, 4) * 98
assert TENTHS == (21, Q(14, 5), Q(49, 5)) and HINS == Q(385, 6)
assert U('עצרת', books=T) == ['Deut 16:8', 'Lev 23:36', 'Num 29:35'] and U('עצרת') == ['2Chr 7:9', 'Deut 16:8', 'Jer 9:1', 'Lev 23:36', 'Neh 8:18', 'Num 29:35'] and aramaic(29, 35)[2] == 'כנישו'
assert words('Num', 29, 39) == ['אלה', 'תעשו', 'ליהוה', 'במועדיכם', 'לבד', 'מנדריכם', 'ונדבתיכם', 'לעלתיכם', 'ולמנחתיכם', 'ולנסכיכם', 'ולשלמיכם'] and words('Lev', 23, 38)[:2] == ['מלבד', 'שבתת'] and U('ונדבתיכם') == ['Deut 12:6', 'Num 29:39'] and aramaic(29, 39)[-2:] == ['ולנכסת', 'קודשיכון']
# THE WATER LIBATION SPELLED IN THREE LETTERS (the Sifrei 150:1, R. Yehudah ben Beteira; Taanit 2b, Shabbat 103b the exam): the goat-verses of
# the seven days close "the continual burnt offering, its meal offering and ITS LIBATION" (ונסכה) — except the SECOND day's "and THEIR
# libations" (ונסכיהם, 29:19: an extra mem), the SIXTH day's "and its libations" (ונסכיה, 29:31: an extra yod — the form's ONE seat in the
# Bible), and the SEVENTH day's "according to THEIR ordinance" (כמשפטם, 29:33: an extra mem where the other days say "according to the
# ordinance") — mem, yod, mem: מים ("water"); computed on the tokens of all eight goat-verses and seven ordinance-verses
LIB = {v: [x for x in words('Num', 29, v) if x.startswith('ונסכ')] for v in (16, 19, 22, 25, 28, 31, 34, 38)}
assert LIB == {16: ['ונסכה'], 19: ['ונסכיהם'], 22: ['ונסכה'], 25: ['ונסכה'], 28: ['ונסכה'], 31: ['ונסכיה'], 34: ['ונסכה'], 38: ['ונסכה']}, LIB
MISH = {v: [x for x in words('Num', 29, v) if x.startswith('כמשפט')] for v in (18, 21, 24, 27, 30, 33, 37)}
assert MISH == {18: ['כמשפט'], 21: ['כמשפט'], 24: ['כמשפט'], 27: ['כמשפט'], 30: ['כמשפט'], 33: ['כמשפטם'], 37: ['כמשפט']}, MISH
assert U('ונסכיה') == ['Num 29:31'] and 'Num 29:19' in U('ונסכיהם') and ''.join(('ונסכיהם'[-1], 'ונסכיה'[-1], 'כמשפטם'[-1])) == 'םהם' and ('ם', 'י', 'ם') == ('ונסכיהם'[-1], 'ונסכיה'[-2], 'כמשפטם'[-1])
assert phrase(['במספרם', 'כמשפט'], None) == ['Num 29:18', 'Num 29:21', 'Num 29:24', 'Num 29:27', 'Num 29:30', 'Num 29:37'] and phrase(['במספרם', 'כמשפטם'], None) == ['Num 29:33']
# LEVITICUS 23 AT ITS SECOND SEAT (M-23): the shared tokens per festival verse pair computed — 28:18 = 23:7 whole (9 of 9), 28:17 nine of ten
# of 23:6, 28:16 six of eight of 23:5; 29:1 ten of seventeen with 23:24 ("a memorial of blowing" → "a day of blowing"); 29:7 ten of fifteen
# with 23:27 ("the day of atonements" dropped, the affliction kept); 29:35 nine of ten with 23:36; 29:39 two of eleven with 23:37 — the
# close rewritten; the Sabbath's offering and the new moon's whole register NEW here
def overlap(a, b):
    A_, B_ = words('Num', *a), words('Lev', *b); return len([x for x in A_ if x in B_]), len(A_)
assert [overlap(a, b) for a, b in (((28, 16), (23, 5)), ((28, 17), (23, 6)), ((28, 18), (23, 7)), ((28, 25), (23, 8)), ((28, 26), (23, 21)), ((29, 1), (23, 24)), ((29, 7), (23, 27)), ((29, 12), (23, 34)), ((29, 35), (23, 36)), ((29, 39), (23, 37)))] == [(6, 8), (9, 10), (9, 9), (8, 11), (9, 16), (10, 17), (10, 15), (8, 19), (9, 10), (2, 11)]
# THE TRANSLATION'S WORDS: "to be accepted with favor" for "a pleasing aroma" at every seat (eleven of eleven); the counts tens-first
assert sum(1 for (c, v) in SPAN if 'לאתקבלא' in aramaic(c, v) or 'דמתקבל' in aramaic(c, v)) == 11 == sum(1 for (c, v) in SPAN if 'ניחח' in words('Num', c, v) or 'ניחחי' in words('Num', c, v))
assert aramaic(29, 13)[10:12] == ['תלת', 'עשר'] and aramaic(29, 18)[-1] == 'כדחזי' and aramaic(29, 33)[-2:] == ['כדחזי', 'להון'], (aramaic(29, 13)[8:13], aramaic(29, 18)[-1], aramaic(29, 33)[-2:])
