import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE NUMBERS WALK, sitting 10 — THE VOWS, Numbers 30:1-17 (2026-09-12; the owner: "Go" after the #141 rereads, on the ruling READ THEN
# COMPILE): THE INK of the chapter, computed from the Tanakh DB, the snapshot store and the shelf's own bytes — never typed. Sitting 9's form
# (offerings_ink.py): the heads found BY POSITION and asserted; coverage computed; every cut by consonants (the misses collected, asserted
# empty); the engine's numeral parser MEASURED on every verse of the chapter (no cardinal expected — measured); the hand's facts as asserts, run
# all at once by assert_driver.py after the measurement pass (vows_measure1.py) printed them; every gloss of a narrative verb the STORE'S OWN
# (words.gloss); the piece-wise cutters HP / AP. Shared by vows_rows_onkelos.py, vows_rows_sifrei.py and write_vows_ledger.py.
# THE SPAN: ONE draft — num_30_vows 30:1-17: 30:1 is the portion Pinchas's last verse (the calendar's closer, read with this draft — the
# draft's-grain rule); 30:2-17 open the portion Matot; the next draft (num_31_midian) opens at 31:1.
import json, os, re, html, sqlite3, sys, io, contextlib, unicodedata
from collections import Counter
ROOT = _ROOT
DATE = '2026-09-12'
UID = 'num_30_vows'
PISKAOT = [153, 154, 155, 156]
TITLE = 'the vows — a man binds himself by a vow or an oath and shall not profane his word; a daughter in her father\'s house and a wife in her husband\'s: silence on the day of hearing confirms, restraint on that day annuls and the LORD forgives her; the widow and the divorcee bound by their own word; every oath of self-affliction her husband confirms or annuls; silence from day to day confirms, annulment after the hearing bears her iniquity; these are the statutes between a man and his wife, a father and his daughter'
OUT = f'{ROOT}/logic/oral_triage/{UID}_{DATE}.md'

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
# THE SHELF'S ROWS ON CHAPTER 30, BY POSITION: FOUR piskaot 153-156, SEVENTEEN rows — 153 on 30:2 (ten rows: the heads of the tribes first and
# the experts; "this is the thing" — the husband annuls, the sage permits; the minor excluded by the identity with the nazirite's vow; the vow's
# support and "in any event"; vows against oaths — the king's life against the King; upon his soul not others; bind the permitted, not permit the
# forbidden; the inward acceptance; the sage not for himself; bal yachel and bal te'acher; the woman likened to the man; "in her youth"; the deaf;
# "to her" — intending her; confirmed one hour; constraint = annulment; the hearing day = the vow day by the hekkesh of 30:17; the forgiveness of
# the annulled vow broken willfully; the caretaker and the messenger; the betrothed; the vows that came with her; only the unconfirmed; utterance
# = oath), 154 on 30:10 (three: the widow and the divorcee from marriage, the orphan in her father's lifetime; silence to confirm against silence
# to vex; the caretaker excluded, "her husband annulled them"), 155 on 30:14 (one: vows of affliction and vows between him and her; "I reasoned
# and reversed"; R. Yishmael and R. Akiva on the partial annulment), 156 on 30:15-17 (three: silence to vex, "from day to day" — to the day's end
# or twenty-four hours; "after his hearing" = after confirmation, "he shall bear her iniquity"; the father and the husband likened both ways).
# NO piska on 30:1 — 152:1 (read at sitting 9) carries it as the calendar's closer; the next head, 157, is 31:1 (the next draft).
assert heads[152] == ('Bamidbar', 29, 39) and heads[153] == ('Bamidbar', 30, 2) and heads[154] == ('Bamidbar', 30, 10) and heads[155] == ('Bamidbar', 30, 14) and heads[156] == ('Bamidbar', 30, 14) and heads[157] == ('Bamidbar', 31, 1), [heads[p] for p in (152, 153, 154, 155, 156, 157)]
assert sorted(p for p, h in heads.items() if h and h[0] == 'Bamidbar' and h[1] == 30) == PISKAOT and [p for p in range(150, 160) if heads.get(p) is None] == []
SIF_ROWS = {p: len(sif[p - 1]) for p in PISKAOT}
assert SIF_ROWS == {153: 10, 154: 3, 155: 1, 156: 3} and {p: len(sif_he[p - 1]) for p in PISKAOT} == SIF_ROWS, SIF_ROWS
assert sum(SIF_ROWS.values()) == 17
def head(p): return heads[p][1:]
# THE ROWS' OWN DEFECTS, read to their verses (RESEARCH_LOG.md): (a) 156's head reads "30:14" while its first row quotes "and if her husband be
# silent, silent to her from day to day" — 30:15's words (the phrase's one Torah seat): THE SEVENTH MISTYPED HEAD of the export; (b) 153:3's
# English cites "II Kings 4:20" and glosses the speaker "(King David)" for the Hebrew's "מלכים ב ב" (2 Kings 2) — the words "as the LORD lives
# and as your soul lives, I will not leave you" stand at 2 Kings 2:2, 2:4, 2:6 (Elisha to Elijah) and 4:30 (the Shunammite to Elisha), never at
# 4:20 and never in David's mouth; (c) 153:3's and 153:4's ENGLISH SUPPLIES THE MISHNAH — "if he were twelve years and one day old, his vows are
# examined" / "those of a girl of eleven are examined", and the identity's content "ki yafli" (the nazirite verse's own verb, 6:2) — where the
# Hebrew row of 153:3 reads the identity as "a vow with a freewill offering beside it" and carries no "examined" clause, and the Hebrew of 153:4
# carries no identity at all for the woman (the inserted-clause class, as 143:3's); (d) 153:7's Hebrew names the disputant "R. Yochanan" where
# the English (and the Sifrei's standing pair) has R. Yonatan, and its conclusion reads "so THE FATHER annuls only the unconfirmed" where the
# argument's target (and the English) is the HUSBAND — a garbled word; (e) 154:1's Hebrew closes "these are the words of R. Yishmael" and the
# English DROPS THE ATTRIBUTION (the sixth defect class again); (f) 154:2's Hebrew ends "Scripture tells that permission was given to annul ALL
# THE DAY" — the English stops at "shall stand" (a conclusion dropped); (g) 154:3's Hebrew opens on 30:13's "all that proceeds from her lips ...
# shall not stand — to exclude the caretaker" and the English opens at "her husband has annulled them" (a lemma dropped); (h) 155:1's Hebrew
# breaks off "so the father can" (אף האב יכול) — a clipped clause.
assert 'Bamidbar 30:14' in clean(sif[155][0])[:40] and 'מיום אל יום' in clean(sif_he[155][0]) and 'from day to day' in clean(sif[155][0])
assert 'II Kings 4:20' in clean(sif[152][2]) and '(King David)' in clean(sif[152][2]) and 'מלכים ב ב חי' in clean(sif_he[152][2])
assert 'his vows are examined' in clean(sif[152][2]) and 'yafli' in clean(sif[152][2]) and 'נבדק' not in clean(sif_he[152][2]) and 'נדר ונדבה עמו' in clean(sif_he[152][2])
assert 'hafla' in clean(sif[152][3]) and 'girl of eleven' in clean(sif[152][3]) and 'הפלאה' not in clean(sif_he[152][3]) and 'נאמר כאן נדר' not in clean(sif_he[152][3]) and 'נאמר כאן נדר' in clean(sif_he[152][2])
assert "ר' יוחנן אומר" in clean(sif_he[152][6]) and 'R. Yonathan says' in clean(sif[152][6]) and 'אף האב אין מיפר אלא שלא הוקמו' in clean(sif_he[152][6]) and 'so, the husband' in clean(sif[152][6])
assert "דברי ר' ישמעאל" in clean(sif_he[153][0]) and 'Yishmael' not in clean(sif[153][0]) and 'R. Akiva says' in clean(sif[153][0])
assert 'להפר כל היום' in clean(sif_he[153][1]) and 'all the day' not in clean(sif[153][1]) and 'all day' not in clean(sif[153][1])
assert 'להוציא את אפוטרופוס' in clean(sif_he[153][2]) and clean(sif[153][2]).strip().startswith('(Bamidbar 30:13) "Her husband has annulled them"')
assert 'אף האב יכול:' in clean(sif_he[154][0])
def plain(w): return ''.join(c for c in w if c != '/' and not (0x0591 <= ord(c) <= 0x05C7))
def pointed(w): return ''.join(c for c in w if c != '/' and not (0x0591 <= ord(c) <= 0x05AF))
ONK_LEN = {c: len(onk[c - 1]) for c in (29, 30, 31)}
assert ONK_LEN == {29: 39, 30: 17, 31: 54} and {c: len(onk_he[c - 1]) for c in (29, 30, 31)} == ONK_LEN, ONK_LEN
def onk_ev(c, v): return clean(onk[c - 1][v - 1]), clean(onk_he[c - 1][v - 1])
shelf_numbers = sorted(d for d in os.listdir(f'{ROOT}/Data/sefaria_export') if re.search(r'Numbers|Bamidbar', d))
outside = [d for d in shelf_numbers if d not in ('Sifrei_Bamidbar', 'Onkelos_Numbers')]
assert len(outside) == 23, len(outside)
# THE PRIOR READS: no ledger has read an Onkelos row of 30, none a Sifrei row of 153-156 (nine ledgers NAME verses of chapter 30 as
# cross-references — a name is not a read); the Sifrei's 152:1 (read whole at sitting 9 in the fall-festivals ledger) carries 30:1 as the
# calendar's closer — CREDITED here with a quick look (credit guard 1: its standing row speaks of 30:1 exactly); FRESH otherwise
TRI = f'{ROOT}/logic/oral_triage'
LED = {f: open(f'{TRI}/{f}', encoding='utf-8').read() for f in os.listdir(TRI) if f.endswith('.md') and os.path.isfile(f'{TRI}/{f}') and f'{TRI}/{f}' != OUT}
assert sorted(f for f, t in LED.items() if re.search(r'^- Onkelos Num 30:\d', t, re.M)) == [] and sorted(f for f, t in LED.items() if re.search(r'Sifrei (?:Bamidbar )?15[3-6]:\d', t)) == []
NAMING = sorted(f for f, t in LED.items() if re.search(r'Num(?:bers)? 30:\d+', t))
assert len(NAMING) == 9 and 'num_04_07_naso_exam_2026-09-10.md' in NAMING and 'num_06_nazir_2026-09-09.md' in NAMING, (len(NAMING), NAMING)
assert 'and Moses said to the children of Israel' in LED['num_29_fall_festivals_2026-09-11.md'] and '- Sifrei Bamidbar 152:1 — MATERIAL' in LED['num_29_fall_festivals_2026-09-11.md']

# ---- THE DRAFT'S SPAN, COMPUTED ----
db = sqlite3.connect(f'file:{ROOT}/Data/tanakh.sqlite?mode=ro', uri=True)
VC = dict(db.execute("SELECT chapter, COUNT(*) FROM verses WHERE book='Num' GROUP BY chapter").fetchall())
assert VC[30] == 17 and VC[31] == 54
def unit_text(uid): return open(f'{ROOT}/logic/units/{uid}.yaml', encoding='utf-8').read()
def steps(uid): return sorted({(int(a), int(b)) for a, b in re.findall(r'STEP_Nm_(\d+)_(\d+)', unit_text(uid))})
assert steps(UID) == [(30, v) for v in range(1, 18)] and 'status: draft' in unit_text(UID) and 'operators:' not in unit_text(UID)
assert steps('num_31_midian')[0] == (31, 1) and 'status: frozen' in unit_text('num_29_fall_festivals')
SPAN = [(30, v) for v in range(1, 18)]
DT_ROWS = re.findall(r'- id: ROW_Num_30_(\d+)', unit_text(UID))
assert DT_ROWS == ['3', '4', '6', '7', '9', '11', '13', '15', '16'], DT_ROWS   # the draft's decision table: the two "when" cases and the seven "if" branches

# ---- THE INK, computed from the Tanakh DB and the snapshot store ----
def accents(w): return [unicodedata.name(c).replace('HEBREW ACCENT ', '') for c in w if 0x0591 <= ord(c) <= 0x05AE]
rows = db.execute("SELECT v.book, v.chapter, v.verse, w.he, w.morph FROM words w JOIN verses v ON w.verse_id=v.id ORDER BY v.id, w.idx").fetchall()
by, byp, byraw = {}, {}, {}
for b, c, v, he, m in rows:
    by.setdefault((b, c, v), []).append((plain(he), m)); byp.setdefault((b, c, v), []).append(pointed(he)); byraw.setdefault((b, c, v), []).append(he)
T = ('Gen', 'Exod', 'Lev', 'Num', 'Deut')
def words(b, c, v): return [x for x, _ in by[(b, c, v)]]
def morphs(b, c, v): return [m for _, m in by[(b, c, v)]]
def hits(sub, books=None, exact=False): return sorted({f'{b} {c}:{v}' for (b, c, v), ws in by.items() if (books is None or b in books) and any((x == sub) if exact else (sub in x) for x, _ in ws)})
def count_tok(tok, books=None): return sum(1 for (b, c, v), ws in by.items() if (books is None or b in books) for x, _ in ws if x == tok)
def phrase(seq, books=T):
    out = []
    for (b, c, v), ws in by.items():
        if books is not None and b not in books: continue
        w = [x for x, _ in ws]
        if any(w[i:i + len(seq)] == list(seq) for i in range(len(w) - len(seq) + 1)): out.append(f'{b} {c}:{v}')
    return sorted(out)
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
for c, v, hp, g in store.execute("SELECT v.chapter, v.verse, w.he_plain, w.gloss FROM words w JOIN verses v ON w.verse_id=v.id WHERE v.book='Num' AND v.chapter = 30 ORDER BY v.id, w.idx"):
    SG.setdefault((c, v), []).append((hp.replace('/', ''), g))
def sg(c, v, tok):
    for hp, g in SG[(c, v)]:
        if hp == tok: return g
    raise KeyError((c, v, tok))

# THE ENGINE'S PARSER on every verse of the chapter — MEASURED before the compile is asked (the standing rule): NO cardinal and NO ordinal in
# seventeen verses, and the three OATH-tokens (the seven-stem's homograph — "an oath" is spelled with the letters of "seven") STARRED as refused
# homographs at 30:3, 30:11, 30:14 — 3b's rule on the seven-stem's four homographs holding at three new seats: silent-and-right, NO GAP
sys.path.insert(0, f'{ROOT}/World/step9')
with contextlib.redirect_stdout(io.StringIO()):
    import cold_run_sequence as CS
def N(b, c, v): return CS.ink_numbers(CS.verse_words(b, c, v))
def O(b, c, v): return CS.ink_ordinals(CS.verse_words(b, c, v))
assert all(N('Num', 30, v) == [] and O('Num', 30, v) == [] for v in range(1, 18)) and N('Num', 31, 1) == []
STARRED = [(v, t) for v in range(1, 18) for t in CS.verse_words('Num', 30, v) if t.endswith('*')]
assert STARRED == [(3, 'שבעה*'), (11, 'בשבעה*'), (14, 'שבעת*')], STARRED
assert [(x, m) for x, m in by[('Num', 30, 3)] if x == 'שבעה'] == [('שבעה', 'HNcfsa')] and sg(30, 3, 'שבעה') == 'something-sworn' and morphs('Num', 30, 14)[3] == 'HNcfsc' and words('Num', 30, 14)[3] == 'שבעת'
OATH_TOKENS = [(v, x) for (c, v) in SPAN for x, m in by[('Num', 30, v)] if x in ('השבע', 'שבעה', 'בשבעה', 'שבעת')]
assert OATH_TOKENS == [(3, 'השבע'), (3, 'שבעה'), (11, 'בשבעה'), (14, 'שבעת')]

# THE FRAMES AND THE REGISTER: TWO narrative verbs in seventeen verses, both Moses' — 30:1 "and Moses SAID to the children of Israel according
# to all that the LORD commanded Moses" (the calendar's closer; the Sifrei 152:1 — R. Yishmael's frame-as-punctuation) and 30:2 "and Moses SPOKE
# to the heads of the tribes ... this is the thing which the LORD commanded" — and NO divine speech-frame: the law of the vows is the one law
# chapter of Numbers given in Moses' voice alone, opened by the formula "this is the thing which the LORD commanded" (eight Bible seats — the manna's
# two, the tabernacle's gifts, Aaron's investiture, the eighth day, the slaughter ban, the vows, the daughters' marriage: the two Numbers seats, 30
# and 36, are exactly the two law chapters of the book with the formula and without "the LORD spoke to Moses"); "the heads of the tribes" three
# Bible seats — here and Solomon's assembly (1 Kings 8:1, 2 Chronicles 5:2), "TO the heads" one; the receipt formula "according to all that the
# LORD commanded Moses" seven seats — six close ACTS (the tabernacle finished, the census, the camp, the Levites' cleansing, the Passover) and 30:1
# alone closes a SPEECH ("and Moses SAID"); "and Moses said to the children of Israel" two seats (Bezalel's calling, Exodus 35:30, and this)
REG = {(c, v): [(x, m) for x, m in by[('Num', c, v)] if m and re.search(r'V.w', m)] for (c, v) in SPAN}
assert {k: v for k, v in REG.items() if v} == {(30, 1): [('ויאמר', 'HC/Vqw3ms')], (30, 2): [('וידבר', 'HC/Vpw3ms')]} and sg(30, 1, 'ויאמר') == 'and-say' and sg(30, 2, 'וידבר') == 'and-speak'
FORMULA = phrase(['זה', 'הדבר', 'אשר', 'צוה', 'יהוה'], None)
assert FORMULA == ['Exod 16:16', 'Exod 16:32', 'Exod 35:4', 'Lev 17:2', 'Lev 8:5', 'Lev 9:6', 'Num 30:2', 'Num 36:6']
DIVINE_FRAME = sorted({c for (b, c, v), ws in by.items() if b == 'Num' and any(ws[i][0] in ('וידבר', 'ויאמר') and i + 1 < len(ws) and ws[i + 1][0] == 'יהוה' for i in range(len(ws)))})
assert DIVINE_FRAME == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 25, 26, 27, 28, 31, 33, 34, 35] and 30 not in DIVINE_FRAME and 36 not in DIVINE_FRAME
assert phrase(['ראשי', 'המטות'], None) == ['1Kgs 8:1', '2Chr 5:2', 'Num 30:2'] and phrase(['אל', 'ראשי'], None) == ['Num 30:2'] and aramaic(30, 2)[3:5] == ['רישי', 'שבטיא']
RECEIPT = phrase(['ככל', 'אשר', 'צוה', 'יהוה', 'את', 'משה'], None)
assert RECEIPT == ['Exod 39:32', 'Exod 39:42', 'Num 1:54', 'Num 2:34', 'Num 30:1', 'Num 8:20', 'Num 9:5']
def key(s):
    b, cv = s.split(' '); c, v = cv.split(':'); return (b, int(c), int(v))
assert [(s, words(*key(s))[0]) for s in RECEIPT if words(*key(s))[0] == 'ויאמר'] == [('Num 30:1', 'ויאמר')]
assert phrase(['ויאמר', 'משה', 'אל', 'בני', 'ישראל'], None) == ['Exod 35:30', 'Num 30:1'] and words('Num', 30, 1) == ['ויאמר', 'משה', 'אל', 'בני', 'ישראל', 'ככל', 'אשר', 'צוה', 'יהוה', 'את', 'משה']
# THE FOOTER: 30:17 "these are the statutes" — three Bible seats (Leviticus 26:46 and Deuteronomy 12:1 continue "and the judgments"; this alone
# bare), "between a man and his wife" and "between a father and his daughter" one seat each — the two authorities the chapter's two nouns:
# "her husband" NINE tokens (plus "to a man" at 30:7), "her father" SIX; "her soul" ten, "his soul" one, "a soul" one
assert phrase(['אלה', 'החקים'], None) == ['Deut 12:1', 'Lev 26:46', 'Num 30:17'] and phrase(['אלה', 'החקים', 'והמשפטים'], None) == ['Deut 12:1', 'Lev 26:46']
assert phrase(['בין', 'איש', 'לאשתו'], None) == ['Num 30:17'] and phrase(['בין', 'אב', 'לבתו'], None) == ['Num 30:17']
HUSB = [(v, x) for (c, v) in SPAN for x, m in by[('Num', 30, v)] if x in ('אישה', 'ואישה')]
assert len(HUSB) == 9 and [v for v, _ in HUSB] == [8, 9, 11, 12, 13, 13, 14, 14, 15] and words('Num', 30, 7)[3] == 'לאיש'
FATH = [(v, x) for (c, v) in SPAN for x, m in by[('Num', 30, v)] if x == 'אביה']
assert len(FATH) == 6 and [v for v, _ in FATH] == [4, 5, 5, 6, 6, 17]
SOUL = [(v, x) for (c, v) in SPAN for x, m in by[('Num', 30, v)] if x.startswith('נפש')]
assert Counter(x for _, x in SOUL) == Counter({'נפשה': 10, 'נפשו': 1, 'נפש': 1}) and SOUL[0] == (3, 'נפשו') and SOUL[-1] == (14, 'נפש')
assert sum(1 for (c, v) in SPAN for x in aramaic(30, v) if x in ('בעלה', 'ובעלה')) == 9   # ONKELOS: "her husband" rendered "her OWNER" (בעלה) at all nine seats

# THE CASE STRUCTURE (the compiler law's when/if): TWO "when" cases open at the first word — 30:3 "a man, when he vows" and 30:4 "and a woman,
# when she vows" (the other two "ki" of the chapter are "because": 30:6 "because her father restrained her", 30:15 "because he was silent") — and
# SEVEN "and if" branches (30:6, 7, 9, 11, 13, 15, 16) — the draft's decision table has exactly these nine rows; "a man, when" nine Torah seats;
# "and a woman, when" three — the zavah's two (Leviticus 15:19, 15:25) and this
KI = [(v, i) for (c, v) in SPAN for i, (x, m) in enumerate(by[('Num', 30, v)]) if x == 'כי']
assert KI == [(3, 1), (4, 1), (6, 18), (15, 20)]
VEIM = [v for (c, v) in SPAN if 'ואם' in words('Num', 30, v)]
assert VEIM == [6, 7, 9, 11, 13, 15, 16] and sum(1 for (c, v) in SPAN for x, _ in by[('Num', 30, v)] if x == 'ואם') == 7
assert [int(r) for r in DT_ROWS] == [3, 4] + VEIM
assert len(phrase(['איש', 'כי'])) == 9 and 'Num 30:3' in phrase(['איש', 'כי']) and phrase(['ואשה', 'כי'], None) == ['Lev 15:19', 'Lev 15:25', 'Num 30:4']

# THE ROOTS: "vow" fourteen tokens (noun and verb), the bond-root twenty-two, the oath four; FIVE DOUBLED VERBS (the infinitive absolute
# before its finite form) — "swear an oath" (30:3), "be, she shall be" (30:7; Jeremiah 15:18 its one kin), "annul, he annuls" (30:13, 30:16 —
# the form's two seats, both here), "be silent, he is silent" (30:15 — one seat); "bind a bond" (30:3) the cognate noun; the doubled forms
# are what the Sifrei reads ("annul, annul" — R. Akiva's part-is-whole; "silent, silent" — the silence to vex; "after his hearing")
assert sum(1 for (c, v) in SPAN for x, _ in by[('Num', 30, v)] if 'נדר' in x) == 14 and sum(1 for (c, v) in SPAN for x, _ in by[('Num', 30, v)] if 'אסר' in x) == 22
DOUBLED = [(v, by[('Num', 30, v)][i][0], by[('Num', 30, v)][i + 1][0]) for (c, v) in SPAN for i in range(len(by[('Num', 30, v)]) - 1) if by[('Num', 30, v)][i][1] in ('HVha', 'HVqa', 'HVNa')]
assert DOUBLED == [(3, 'השבע', 'שבעה'), (7, 'היו', 'תהיה'), (13, 'הפר', 'יפר'), (15, 'החרש', 'יחריש'), (16, 'הפר', 'יפר')], DOUBLED
assert phrase(['הפר', 'יפר'], None) == ['Num 30:13', 'Num 30:16'] and phrase(['החרש', 'יחריש'], None) == ['Num 30:15'] and phrase(['היו', 'תהיה'], None) == ['Jer 15:18', 'Num 30:7'] and phrase(['השבע', 'שבעה'], None) == ['Num 30:3'] and phrase(['לאסר', 'אסר'], None) == ['Num 30:3']
assert aramaic(30, 13)[1:3] == ['בטלא', 'יבטל'] and aramaic(30, 15)[1:3] == ['משתק', 'ישתוק'] and aramaic(30, 7)[1:3] == ['מהוה', 'תהוי'] and aramaic(30, 3)[7:9] == ['יקים', 'קים']   # the translation keeps every doubling
# THE STAND AND THE ANNUL: the stand-root twelve tokens (they shall stand / it shall stand / he confirmed), the annul-root six (30:13 ×3, 30:14,
# 30:16 ×2); the silence-verb four (30:5, 8, 12, 15 — "kept silent" at Genesis 34:5 its Torah kin, the craftsmen a homograph in Kings and
# Jeremiah); the restrain-verb FOUR Torah seats — three here (30:6, 9, 12) and the spies who "discouraged the heart" (32:9), the next portion's
assert len([x for (c, v) in SPAN for x, _ in by[('Num', 30, v)] if x in ('יקום', 'וקמו', 'יקמו', 'יקימנו', 'והקים', 'הקים')]) == 12
assert [(v, x) for (c, v) in SPAN for x, m in by[('Num', 30, v)] if 'פר' in x and m.startswith('HV')] == [(13, 'הפר'), (13, 'יפר'), (13, 'הפרם'), (14, 'יפרנו'), (16, 'הפר'), (16, 'יפר')]
assert U('והחריש') == ['Num 30:5', 'Num 30:8'] and U('והחרש') == ['2Kgs 24:16', 'Gen 34:5', 'Jer 29:2', 'Num 30:12'] and U('יחריש') == ['Num 30:15', 'Prov 11:12', 'Zeph 3:17']
assert sorted({f'{b} {c}:{v}' for (b, c, v), ws in by.items() if b in T for x, m in ws if x in ('הניא', 'יניא', 'ויניאו')}) == ['Num 30:12', 'Num 30:6', 'Num 30:9', 'Num 32:9'] and U('הניא') == ['Num 30:12', 'Num 30:6', 'Ps 33:10']
assert sg(30, 6, 'הניא') == 'refuse' and aramaic(30, 6)[1] == 'אעדי' and aramaic(30, 12)[5] == 'אעדי'   # ONKELOS: "restrained" rendered "turned away"

# THE CLOCK WORDS: "on the day of his hearing" FOUR seats, all here (30:6, 8, 13, 15) with 30:9's "on the day her husband hears" and 30:16's
# "AFTER his hearing" (one seat — the Sifrei: after his confirmation); the hearing-infinitive six tokens — the clock's trigger; "from day to
# day" (30:15) two Bible seats — this and 1 Chronicles 16:23, whose Psalm parallel (96:2) writes the same words with the other preposition
# (Esther 3:7 the Psalm's form): the Chronicler's form is the Torah's; ONKELOS renders 30:15 with the Psalm's form (מיום ליום)
assert phrase(['ביום', 'שמעו'], None) == ['Num 30:13', 'Num 30:15', 'Num 30:6', 'Num 30:8'] and phrase(['ביום', 'שמע'], None) == ['Num 30:9'] and phrase(['אחרי', 'שמעו'], None) == ['Num 30:16']
assert [(v, x, m) for (c, v) in SPAN for x, m in by[('Num', 30, v)] if x.startswith('שמע')] == [(6, 'שמעו', 'HVqc/Sp3ms'), (8, 'שמעו', 'HVqc/Sp3ms'), (9, 'שמע', 'HVqc'), (13, 'שמעו', 'HVqc/Sp3ms'), (15, 'שמעו', 'HVqc/Sp3ms'), (16, 'שמעו', 'HVqc/Sp3ms')]
assert phrase(['מיום', 'אל', 'יום'], None) == ['1Chr 16:23', 'Num 30:15'] and phrase(['מיום', 'ליום'], None) == ['Esth 3:7', 'Ps 96:2'] and aramaic(30, 15)[5:7] == ['מיום', 'ליום']
assert words('1Chr', 16, 23)[4:9] == ['בשרו', 'מיום', 'אל', 'יום', 'ישועתו'] and words('Ps', 96, 2)[4:8] == ['בשרו', 'מיום', 'ליום', 'ישועתו'], (words('1Chr', 16, 23), words('Ps', 96, 2))   # retyped from the print: the index was typed from memory

# THE FORGIVENESS AND THE INIQUITY: "and the LORD will forgive her" THREE seats — all in this chapter (30:6, 9, 13: the father's restraint, the
# husband's day-of-hearing annulment, the husband's annulment in her husband's house); the verb "will forgive" four Bible tokens — the three and
# Naaman's plea (2 Kings 5:18); ONKELOS makes it passive with the buffer: "from before the LORD it shall be forgiven her"; "and he shall bear
# HER iniquity" (30:16) one seat — the feminine "her iniquity" five Torah seats: the peace offering eaten late (Leviticus 7:18), the land
# (18:25), THE SOTAH ("that woman shall bear her iniquity", 5:31), the blasphemer (15:31) and this — the husband who annuls after confirming
# steps into her place (the Sifrei 156:2); ONKELOS: "he shall RECEIVE her guilt" (the debt-word)
assert phrase(['ויהוה', 'יסלח', 'לה'], None) == ['Num 30:13', 'Num 30:6', 'Num 30:9'] and U('יסלח') == ['2Kgs 5:18', 'Num 30:13', 'Num 30:6', 'Num 30:9']
assert aramaic(30, 6)[15:20] == ['ומן', 'קדם', 'יי', 'ישתבק', 'לה'] and aramaic(30, 9)[-5:] == ['ומן', 'קדם', 'יי', 'ישתביק', 'לה']
assert phrase(['ונשא', 'את', 'עונה'], None) == ['Num 30:16'] and U('עונה', books=T) == ['Lev 18:25', 'Lev 7:18', 'Num 15:31', 'Num 30:16', 'Num 5:31'] and phrase(['תשא', 'את', 'עונה'], None) == ['Num 5:31']
assert phrase(['ונשא', 'עונו'], None) == ['Lev 17:16', 'Lev 5:1', 'Lev 5:17'] and aramaic(30, 16)[-3:] == ['ויקבל', 'ית', 'חובה'] and sg(30, 16, 'עונה') == 'perversity-her/its'

# THE PERSONS: "in her youth" TWO seats, both here (30:4, 30:17) — the priest's daughter returns to her father's house "AS in her youth"
# (Leviticus 22:13, the kin form); "her father's house" seven Bible seats — Tamar's widowhood (Genesis 38:11), the priest's daughter, this, the
# slandered bride (Deuteronomy 22:21), Rahab's, the concubine's two — and "IN her father's house" (30:4) one; "her husband's house" (30:11)
# here and Ruth 1:9; "a widow or a divorced woman" THREE Torah seats — the high priest's forbidden wives (Leviticus 21:14), the priest's
# daughter sent home (22:13) and this — the vower's widow and the priest's the same pair of words
assert U('בנעריה') == ['Num 30:17', 'Num 30:4'] and U('כנעוריה') == ['Lev 22:13'] and aramaic(30, 4)[-1] == 'ברביותהא' and aramaic(30, 17)[-3] == 'ברביותהא'
assert phrase(['בית', 'אביה'], None) == ['Deut 22:21', 'Gen 38:11', 'Josh 6:25', 'Judg 19:2', 'Judg 19:3', 'Lev 22:13', 'Num 30:17'] and phrase(['בבית', 'אביה'], None) == ['Num 30:4'] and phrase(['בית', 'אישה'], None) == ['Num 30:11', 'Ruth 1:9']
assert phrase(['אלמנה', 'וגרושה'], None) == ['Lev 21:14', 'Lev 22:13', 'Num 30:10'] and words('Lev', 22, 13)[:6] == ['ובת', 'כהן', 'כי', 'תהיה', 'אלמנה', 'וגרושה'] and words('Lev', 22, 13)[10:14] == ['אל', 'בית', 'אביה', 'כנעוריה']
assert aramaic(30, 10)[1:3] == ['ארמלא', 'ומתרכא'] and aramaic(30, 11)[1:3] == ['בית', 'בעלה']

# THE UTTERANCE: "the utterance of her lips" (מבטא) TWO seats, both here (30:7, 30:9) — the noun's kin the oath-verb "to utter with the lips"
# of Leviticus 5:4 (one seat; the Sifrei's identity: utterance = oath); "all that proceeds from her lips" (30:13) one seat and its pair "what
# proceeds from your lips you shall keep" (Deuteronomy 23:24) one; "he shall not profane his word" one seat (the profane-verb's one seat in
# this sense; five homographs "wait / begin" in Judges, Isaiah, Psalms); "according to all that proceeds from his mouth he shall do" one seat —
# and its two echoes: Moses to Gad and Reuben "what has gone out of your mouth you shall do" (32:24, the next portion) and Jephthah's daughter
# "do to me as went out of your mouth" (Judges 11:36); "to afflict a soul" (30:14) — the afflict-infinitive two Bible seats, Pharaoh's "to humble
# yourself" (Exodus 10:3) and this; ONKELOS: the utterance "the EXPLICIT [word] of her lips", "he shall not VOID his word", "to MORTIFY a soul"
assert U('מבטא') == ['Num 30:7', 'Num 30:9'] and U('לבטא') == ['Lev 5:4'] and words('Lev', 5, 4)[:6] == ['או', 'נפש', 'כי', 'תשבע', 'לבטא', 'בשפתים'] and aramaic(30, 7)[7:9] == ['פרוש', 'ספותהא']
assert phrase(['מוצא', 'שפתיה'], None) == ['Num 30:13'] and phrase(['מוצא', 'שפתיך'], None) == ['Deut 23:24'] and words('Deut', 23, 24)[:4] == ['מוצא', 'שפתיך', 'תשמר', 'ועשית']
assert phrase(['לא', 'יחל', 'דברו'], None) == ['Num 30:3'] and U('יחל') == ['Isa 48:11', 'Judg 10:18', 'Judg 13:5', 'Num 30:3', 'Ps 130:7', 'Ps 131:3'] and morphs('Num', 30, 3)[13] == 'HVhi3ms' and aramaic(30, 3)[13:16] == ['לא', 'יבטל', 'פתגמיה']
assert phrase(['ככל', 'היצא', 'מפיו'], None) == ['Num 30:3'] and phrase(['והיצא', 'מפיכם'], None) == ['Num 32:24'] and phrase(['יצא', 'מפיך'], None) == ['Judg 11:36']
assert phrase(['לענת', 'נפש'], None) == ['Num 30:14'] and U('לענת') == ['Exod 10:3', 'Num 30:14'] and aramaic(30, 14)[5:7] == ['לסגפא', 'נפש'] and sg(30, 14, 'לענת') == 'to-depress-literally'
# ONKELOS' ONE ROOT: the translation renders the OATH by the root "stand/establish" (יקים קים at 30:3 "swears an oath", בקיום 30:11, קיומת 30:14),
# the CONFIRMING by the same root (יקומון, ויקים, קים 30:5-15), and "the statutes" of 30:17 by it too (קימיא) — the chapter's stand-verb, its
# oath-noun and its statute-noun one Aramaic root; the Hebrew keeps three (קום / שבע / חק)
QY = [(v, x) for (c, v) in SPAN for x in aramaic(30, v) if x.startswith('קי') or x.startswith('יקי') or x in ('קים', 'בקיום')]
assert [(v, x) for v, x in QY if x in ('קים', 'בקיום', 'קיומת', 'קימיא')] == [(3, 'קים'), (11, 'בקיום'), (14, 'קיומת'), (15, 'קים'), (17, 'קימיא')] and aramaic(30, 3)[7] == 'יקים' and aramaic(30, 14)[8] == 'יקימנון'
assert aramaic(30, 3)[:6] == ['גבר', 'ארי', 'ידר', 'נדר', 'קדם', 'יי'] and aramaic(30, 1)[:4] == ['ואמר', 'משה', 'לבני', 'ישראל'] and aramaic(30, 2)[8:13] == ['דין', 'פתגמא', 'די', 'פקיד', 'יי']

# THE SHELF'S CITATIONS, READ TO THEIR VERSES: the vow-identity's partner 6:2 "when he clearly utters to vow a vow" ("when he clearly utters"
# four Bible seats — Leviticus 27:2, Numbers 6:2, Deuteronomy 17:8, Zechariah 8:6); Deuteronomy 23:22 "when you vow a vow to the LORD your God
# you shall not DELAY to pay it" (the second transgression, 153:4); Leviticus 5:4's "to utter with the lips" (153:7); the trumpets' two verses
# (10:3-4, 153:1); Moses' "thus said the LORD" (Exodus 11:4, 153:2); the princes returning first (Exodus 34:31-32, 153:1); the king's-life oath
# at 2 Kings 2:2 (153:3 — the English's "4:20" and "King David" wrong twice)
assert words('Num', 6, 2)[6:13] == ['איש', 'או', 'אשה', 'כי', 'יפלא', 'לנדר', 'נדר'] and phrase(['כי', 'יפלא'], None) == ['Deut 17:8', 'Lev 27:2', 'Num 6:2', 'Zech 8:6']
assert words('Deut', 23, 22)[:8] == ['כי', 'תדר', 'נדר', 'ליהוה', 'אלהיך', 'לא', 'תאחר', 'לשלמו'] and phrase(['תדר', 'נדר'], None) == ['Deut 23:22', 'Eccl 5:3', 'Num 30:4'] and phrase(['ידר', 'נדר'], None) == ['Num 30:3']
assert words('Num', 10, 3)[:6] == ['ותקעו', 'בהן', 'ונועדו', 'אליך', 'כל', 'העדה'] and words('Num', 10, 4)[:6] == ['ואם', 'באחת', 'יתקעו', 'ונועדו', 'אליך', 'הנשיאים']
assert words('Exod', 11, 4)[:5] == ['ויאמר', 'משה', 'כה', 'אמר', 'יהוה'] and words('Exod', 34, 31)[3:9] == ['וישבו', 'אליו', 'אהרן', 'וכל', 'הנשאים', 'בעדה'] and words('Exod', 34, 32)[:5] == ['ואחרי', 'כן', 'נגשו', 'כל', 'בני']
assert phrase(['חי', 'יהוה', 'וחי', 'נפשך', 'אם', 'אעזבך'], None) == ['2Kgs 2:2', '2Kgs 2:4', '2Kgs 2:6', '2Kgs 4:30']
assert words('Lev', 21, 14)[:2] == ['אלמנה', 'וגרושה'] and words('Gen', 38, 11)[4:8] == ['שבי', 'אלמנה', 'בית', 'אביך']
NEDER_BOOKS = Counter(b for (b, c, v), ws in by.items() if b in T for x, m in ws if re.match(r'^(ו|ל|ה|מ)?נדר', x))
assert NEDER_BOOKS == Counter({'Num': 22, 'Deut': 8, 'Lev': 6, 'Gen': 4}) and NEDER_BOOKS['Num'] == 22 and 14 <= NEDER_BOOKS['Num']   # Numbers holds the Torah's vow-word most, and this chapter fourteen of its twenty-two
