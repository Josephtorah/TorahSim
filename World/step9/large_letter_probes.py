#!/usr/bin/env python3
"""THE LARGE LETTERS AS A MARKER LAYER — A HYPOTHESIS (owner-ruled 2026-09-17 at THE DEUTERONOMY WALK sitting 4, run 1: "yes lets put it in as hypothesis").

The scroll writes a few letters oversized (the Masorah's majuscules). The Bible's XML carries FOUR such segments, all in the Torah: the ayin and the dalet of
"hear … one" (Deuteronomy 6:4 — together עד, "witness"), the vav of "belly" (Leviticus 11:42 — Kiddushin 30a: the middle letter of the Torah), the nun of
"their case" (Numbers 27:5 — the daughters' plea Moses brought near). THE HYPOTHESIS: the large letter is a SECOND CHANNEL in the program's text, a mark beside
the words like the parser's own marks (the star, the caret), and its three seats land on three classes the engine already has — a COUNT CHECK, a HALT, an
ATTESTATION. The shelf teaches the first two (Kiddushin 30a; Sifrei Bamidbar 133:4 / Bava Batra 119a); the third ("witness") is later than the core shelf and
stays a HYPOTHESIS until a teacher on the shelf is found. This probe measures the exhibits; it changes no engine file. Owed on the owner's word: the parser's
mark (the Tanakh DB rebuilt carrying the XML's segment type — the store's rebuild the same), and the compile's edge at 6:4 filed `link: hypothesis`.
The values typed from the measurement prints of 2026-09-17 (the scratchpad's ch6_* and the middle-count print).
"""
import os as _os, re, sqlite3, sys
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
def plain(w): return ''.join(c for c in w if c != '/' and not (0x0591 <= ord(c) <= 0x05C7))
ORD = {'Gen': 1, 'Exod': 2, 'Lev': 3, 'Num': 4, 'Deut': 5}
RESULTS = []
def H(name, ok, detail): RESULTS.append((name, bool(ok), detail)); print(f"  {'PASS' if ok else 'FAIL'} {name}: {detail}")

def h1_the_xml():
    """H1 — the XML carries exactly four large-letter segments in the whole Bible, all in the Torah, and these four letters"""
    segs = {}
    for f in sorted(_os.listdir(f'{_ROOT}/Data')):
        if f.endswith('.xml'):
            t = open(f'{_ROOT}/Data/{f}', encoding='utf-8').read()
            found = re.findall(r'<seg type="x-large">([^<]+)</seg>', t)
            if found: segs[f] = found
    H('H1 the XML segments', segs == {'Deut.xml': ['ע', 'ד'], 'Lev.xml': ['וֹ'], 'Num.xml': ['ן']}, segs)

def h2_the_store_and_the_db():
    """H2 — the snapshot store drops the four letters (four tokens differ over the Torah at equal counts); the Tanakh DB carries them whole"""
    store = sqlite3.connect(f'file:{_ROOT}/torah_grok.SNAPSHOT-main-51801ca.sqlite?mode=ro', uri=True)
    db = sqlite3.connect(f'file:{_ROOT}/Data/tanakh.sqlite?mode=ro', uri=True)
    S = {}
    for b, c, v, hp, idx in store.execute("SELECT v.book, v.chapter, v.verse, REPLACE(w.he_plain,'/',''), w.idx FROM words w JOIN verses v ON w.verse_id=v.id WHERE v.book IN ('Gen','Exod','Lev','Num','Deut')"):
        S.setdefault((b, c, v), {})[idx] = hp
    D = {}
    for b, c, v, he, idx in db.execute("SELECT v.book, v.chapter, v.verse, w.he, w.idx FROM words w JOIN verses v ON w.verse_id=v.id WHERE v.book IN ('Gen','Exod','Lev','Num','Deut')"):
        D.setdefault((b, c, v), {})[idx] = plain(he)
    mism = sorted((k, i, S[k][i], D[k][i]) for k in D if k in S and len(S[k]) == len(D[k]) for i in sorted(D[k]) if S[k][i] != D[k][i])
    want = [(('Deut', 6, 4), 0, 'שמ', 'שמע'), (('Deut', 6, 4), 5, 'אח', 'אחד'), (('Lev', 11, 42), 3, 'גח', 'גחון'), (('Num', 27, 5), 3, 'משפט', 'משפטן')]
    H('H2 the store drops the four letters, the DB keeps them', sorted(mism) == sorted(want) and len(mism) == 4, mism)
    return db

def h3_kiddushin_30a(db):
    """H3 — Kiddushin 30a's three middles (the vav of belly the middle LETTER, darosh darash the middle WORD, vehitgalach the middle VERSE) against the text's count:
    the text's middles all fall in Leviticus 8; the Talmud's seats lie past them — DIVERGE, as the gemara's own "we are not expert" admits"""
    rows = db.execute("SELECT v.book, v.chapter, v.verse, w.he, w.idx FROM words w JOIN verses v ON w.verse_id=v.id WHERE v.book IN ('Gen','Exod','Lev','Num','Deut')").fetchall()
    rows.sort(key=lambda r: (ORD[r[0]], r[1], r[2], r[4]))
    letters, words, verses = [], [], []
    for b, c, v, he, idx in rows:
        p = plain(he); words.append((b, c, v, idx, p)); letters.extend((b, c, v, idx, ch) for ch in p)
        if not verses or verses[-1] != (b, c, v): verses.append((b, c, v))
    NL, NW, NV = len(letters), len(words), len(verses)
    midL = (letters[NL // 2 - 1][:3], letters[NL // 2][:3]); midW = (words[NW // 2 - 1][:3], words[NW // 2][:3]); midV = verses[NV // 2]
    vav = [k for k, (b, c, v, i, ch) in enumerate(letters) if (b, c, v) == ('Lev', 11, 42) and ch == 'ו' and next(w for w in words if w[:4] == (b, c, v, i))[4] == 'גחון']
    dd = [k for k, w in enumerate(words) if w[:3] == ('Lev', 10, 16) and w[4] == 'דרש']
    vg = [k for k, x in enumerate(verses) if x == ('Lev', 13, 33)]
    facts = (NL, NW, NV, midL, midW, midV, vav, dd, vg)
    want = (304850, 79982, 5853, (('Lev', 8, 29), ('Lev', 8, 29)), (('Lev', 8, 15), ('Lev', 8, 15)), ('Lev', 8, 9), [157238], [40920, 40921], [3085])
    H('H3 Kiddushin 30a DIVERGES from the count', facts == want, f'letters {NL} (half {NL // 2}; the vav of belly at {vav[0]}, {vav[0] - NL // 2} past), words {NW} (half {NW // 2}; darosh darash at {dd}, {dd[0] - NW // 2} past), verses {NV} (the middle {midV}; vehitgalach at {vg[0]}, {vg[0] - NV // 2} past); the text\'s middles {midL[0]}, {midW[0]}, {midV}')

def _lines_at(prefix):
    """the journal's event rows whose verse column starts with the prefix (any of the verse-bearing columns), the prefix followed by no digit"""
    j = sqlite3.connect(f'file:{_ROOT}/World/journal/data/world.sqlite?mode=ro', uri=True)
    cols = [c[1] for c in j.execute('PRAGMA table_info(events)')]
    out = []
    for col in [c for c in cols if c in ('source', 'verse', 'at', 'ref', 'case_source', 'first_verse')]:
        for kind, s_, data in j.execute(f"SELECT kind, {col}, data FROM events WHERE {col} LIKE ?", (prefix + '%',)):
            if s_ and not s_[len(prefix):len(prefix) + 1].isdigit(): out.append((col, kind, data or ''))
    return out

def h4_the_halt():
    """H4 — the tape's line at Numbers 27:5 is the halt's third form (judgment_brought_near): the large nun sits on the halt"""
    rows = _lines_at('Num 27:5'); classes = sorted({k for _, k, _ in rows})
    H('H4 the nun on the halt', any('judgment_brought_near' in d for _, _, d in rows) and 'run.event' in classes, f'{len(rows)} lines, classes {classes}, the halt kind present: {any("judgment_brought_near" in d for _, _, d in rows)}')

def h5_the_creed():
    """H5 — Deuteronomy 6:4 has NO machine class yet (no tape line, no register seat): the "witness" reading is the hypothesis, OPEN until the compile files its edge"""
    n = len(_lines_at('Deut 6:4'))
    RI = open(f'{_ROOT}/World/step9/REGISTER_INDEX.md', encoding='utf-8').read()
    H('H5 the creed unclassed (OPEN)', n == 0 and not re.search(r'Deut 6:4\b', RI), f'tape lines at 6:4: {n}; register lines: {bool(re.search(r"Deut 6:4", RI))}')

def h6_the_count_check(db):
    """H6 — the count check the vav stands for is the machine's own: the Torah's letters, words and verses counted twice (by book order, by id order) agree"""
    a = db.execute("SELECT COUNT(*) FROM words w JOIN verses v ON w.verse_id=v.id WHERE v.book IN ('Gen','Exod','Lev','Num','Deut')").fetchone()[0]
    b = sum(db.execute("SELECT COUNT(*) FROM words w JOIN verses v ON w.verse_id=v.id WHERE v.book=?", (bk,)).fetchone()[0] for bk in ORD)
    H('H6 the count agrees both ways', a == b == 79982, (a, b))

if __name__ == '__main__':
    print('THE LARGE LETTERS — the hypothesis\'s exhibits')
    h1_the_xml(); db = h2_the_store_and_the_db(); h3_kiddushin_30a(db); h4_the_halt(); h5_the_creed(); h6_the_count_check(db)
    ok = sum(1 for _, o, _ in RESULTS if o); print(f'{ok}/{len(RESULTS)}')
    sys.exit(0 if ok == len(RESULTS) else 1)
