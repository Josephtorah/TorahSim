#!/usr/bin/env python3
# THE NUMBERS WALK, sitting 8 — THE SECOND CENSUS, Numbers 26:1-65 (2026-09-11; the owner: "Go" after the #132 rereads, on the ruling
# READ THEN COMPILE): THE FIRST MEASUREMENT PASS — the shelf's heads by position (piska 132 on 26:53; 133 on 27:1), the draft's span
# (num_26_second_census, 26:1-65 — the next draft opens at 27:1), the prior-read scan (piska 132 was QUICK-LOOKED at THE TENT's daughters,
# "outside the span, not counted" — a quick look is not a read: the rows are read whole here), the engine's parser on the census's own
# numbers against chapter 1's, the family roster against Genesis 46 and chapter 1's tribe order, and the DUMPS the reading runs on
# (Onkelos EN + HE per verse — the export's 26:1 row carries 25:19's head, already read at sitting 7; the Sifrei's rows on 26; the
# pointed Hebrew with the store's own glosses). Nothing typed.
import json, os, re, html, sqlite3, sys, io, contextlib, unicodedata
from collections import Counter
ROOT = '<repo-old>'
SP = os.path.dirname(os.path.abspath(__file__))
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
print('HEADS 130-138:', {p: heads.get(p) for p in range(130, 139)})
print('HEADS naming 26:', sorted((p, heads[p]) for p, h in heads.items() if h and h[0] == 'Bamidbar' and h[1] == 26))
P26 = sorted(p for p, h in heads.items() if h and h[0] == 'Bamidbar' and h[1] == 26)
for p in P26:
    print(f'  piska {p}: rows {len(sif[p-1])} / he {len(sif_he[p-1])}')
    for r, row in enumerate(sif[p-1], 1):
        cites = sorted(set(re.findall(r'(Bamidbar|Devarim|Bereshit|Shemot|Vayikra|Yehoshua|Ibid\.?) ?(\d+):(\d+)', clean(row))))
        print(f'    row {r}: {len(clean(row))} chars; cites {cites[:12]}; opens {clean(row)[:120]!r}')
print('ONK_LEN 25-27:', {c: (len(onk[c - 1]), len(onk_he[c - 1])) for c in (25, 26, 27)})
def plain(w): return ''.join(c for c in w if c != '/' and not (0x0591 <= ord(c) <= 0x05C7))
def pointed(w): return ''.join(c for c in w if c != '/' and not (0x0591 <= ord(c) <= 0x05AF))
print('ONK 26:1 head:', clean(onk[25][0])[:80], '|', plain(clean(onk_he[25][0]))[:40])
def unit_text(uid): return open(f'{ROOT}/logic/units/{uid}.yaml', encoding='utf-8').read()
def steps(uid): return sorted({(int(a), int(b)) for a, b in re.findall(r'STEP_Nm_(\d+)_(\d+)', unit_text(uid))})
for uid in ('num_25_peor_pinchas', 'num_26_second_census', 'num_27_zelophehad_joshua'):
    st = steps(uid); print(uid, 'status draft' if 'status: draft' in unit_text(uid) else 'NOT DRAFT', st[0], st[-1], len(st), 'operators:' in unit_text(uid))
db = sqlite3.connect(f'file:{ROOT}/elijah_docket/tanakh.sqlite?mode=ro', uri=True)
VC = dict(db.execute("SELECT chapter, COUNT(*) FROM verses WHERE book='Num' GROUP BY chapter").fetchall())
print('VC 25-27:', {c: VC[c] for c in (25, 26, 27)})
TRI = f'{ROOT}/logic/oral_triage'
LED = {f: open(f'{TRI}/{f}', encoding='utf-8').read() for f in os.listdir(TRI) if f.endswith('.md')}
print('PRIOR sifrei 132:', sorted((f, sorted(set(re.findall(r'Sifrei (?:Bamidbar )?132:\d', t)))) for f, t in LED.items() if re.search(r'Sifrei (?:Bamidbar )?132:\d', t)))
print('PRIOR onkelos 26:', sorted((f, sorted(set(re.findall(r'Onkelos Num (26:\d+)', t)))[:6]) for f, t in LED.items() if re.search(r'Onkelos Num 26:\d', t)))
rows = db.execute("SELECT v.book, v.chapter, v.verse, w.he, w.morph FROM words w JOIN verses v ON w.verse_id=v.id ORDER BY v.id, w.idx").fetchall()
by, byp = {}, {}
for b, c, v, he, m in rows:
    by.setdefault((b, c, v), []).append((plain(he), m)); byp.setdefault((b, c, v), []).append(pointed(he))
store = sqlite3.connect(f'file:{ROOT}/torah_grok.SNAPSHOT-main-51801ca.sqlite?mode=ro', uri=True)
SG = {}
for c, v, hp, g in store.execute("SELECT v.chapter, v.verse, w.he_plain, w.gloss FROM words w JOIN verses v ON w.verse_id=v.id WHERE v.book='Num' AND v.chapter = 26 ORDER BY v.id, w.idx"):
    SG.setdefault((c, v), []).append((hp.replace('/', ''), g))
SPAN = [(26, v) for v in range(1, 66)]
print('SPAN', len(SPAN), SPAN[0], SPAN[-1])
sys.path.insert(0, f'{ROOT}/World/step9')
with contextlib.redirect_stdout(io.StringIO()):
    import cold_run_sequence as CS
def N(b, c, v): return CS.ink_numbers(CS.verse_words(b, c, v))
NUMTOK = re.compile(r'^(ו?ה?)(אחד|אחת|שנים|שתים|שני|שתי|שלש|שלשה|שלשת|ארבע|ארבעה|חמש|חמשה|חמשת|שש|ששה|שבע|שבעה|שמנה|שמונה|תשע|תשעה|עשר|עשרה|עשרים|שלשים|ארבעים|חמשים|ששים|שבעים|שמנים|תשעים|מאה|מאת|מאתים|אלף|אלפים|עשרון|עשרנים|מעשר|חצי|רבע|שלשית|מאות|רבבה|עשרת|שבעת|ארבעת|ששת|תשעת|חמשת|שמנת|שלישי|שביעי|ראשון|שני|שנית|פעמים|רגלים)(ים|ה|ת|י|ו|ם|ך|כם|ו)?$')
print('--- PARSER on 26 (verses with a number-like token) ---')
P = {}
for (c, v) in SPAN:
    ws = [x for x, _ in by[('Num', c, v)]]
    cand = [x for x in ws if NUMTOK.match(x) or 'עשר' in x or 'מאה' in x or 'אלף' in x or 'מאות' in x or 'שבע' in x or 'שלש' in x or 'רבע' in x or 'חדש' in x]
    n = N('Num', c, v); P[(c, v)] = n
    if cand or n: print(f'  {c}:{v} tokens={cand} -> {n}')
print('--- THE FIRST CENSUS (chapter 1) by the parser ---')
C1 = {v: N('Num', 1, v) for v in range(20, 47)}
print({v: n for v, n in C1.items() if n})
print('--- chapter 2 totals and 3 Levites ---', {v: N('Num', 2, v) for v in (9, 16, 24, 31, 32)}, {v: N('Num', 3, v) for v in (22, 28, 34, 39, 43)})
FR = [(c, v) for (c, v) in SPAN if [x for x, _ in by[('Num', c, v)]][0] in ('וידבר', 'ויאמר')]
print('FRAMES (spoke/said openings):', [(c, v, [x for x, _ in by[('Num', c, v)]][:7]) for c, v in FR])
REG = {}
for (c, v) in SPAN:
    vs = [(x, [q for q in m.split('/') if 'V' in q][0]) for x, m in by[('Num', c, v)] if m and re.search(r'V.w', m)]
    if vs: REG[(c, v)] = vs
print('REG count', len(REG), 'verses with a narrative verb:', sorted(v for c, v in REG), 'no-verb verses', len([k for k in SPAN if k not in REG]))
print('REG verbs:', {k[1]: [x for x, _ in vs] for k, vs in REG.items()})
# THE FAMILY ROSTER: every "family of the X" (משפחת) token in 26, in order; the tribe heads; the count of families
FAM = []
for (c, v) in SPAN:
    ws = [x for x, _ in by[('Num', c, v)]]
    for i, x in enumerate(ws):
        if x == 'משפחת' and i + 1 < len(ws): FAM.append((v, ws[i + 1]))
print('FAMILIES (משפחת + next):', len(FAM), FAM)
print('משפחת tokens by verse:', Counter(v for v, _ in FAM))
TRIBE_HEADS = [(v, [x for x, _ in by[('Num', 26, v)]][:6]) for v in range(5, 52) if [x for x, _ in by[('Num', 26, v)]][0] in ('בני', 'ראובן', 'אלה')]
print('TRIBE HEADS (verses opening בני/אלה):', TRIBE_HEADS)
# Genesis 46's roster tokens (the sons by name) for the comparison
G46 = {v: [x for x, _ in by[('Gen', 46, v)]] for v in range(8, 28)}
print('GEN 46:8-27 tokens:'); [print(f'  46:{v}', ' '.join(ws)) for v, ws in G46.items()]
print('NUM 1 tribe order (1:20-43 heads):', [(v, [x for x, _ in by[('Num', 1, v)]][:3]) for v in range(20, 44) if [x for x, _ in by[('Num', 1, v)]][0] in ('לבני', 'ויהיו', 'בני')])
print('NUM 2 camp order:', [(v, [x for x, _ in by[('Num', 2, v)]][:8]) for v in (3, 5, 7, 10, 12, 14, 18, 20, 22, 25, 27, 29)])
with open(f'{SP}/census_onkelos.txt', 'w', encoding='utf-8') as f:
    for (c, v) in SPAN:
        en, he = clean(onk[c-1][v-1]), clean(onk_he[c-1][v-1])
        f.write(f'=== Onkelos Num {c}:{v}' + (' (the row\'s HEAD is 25:19 "It was after the plague" — read at sitting 7; the rest is 26:1)' if v == 1 else '') + f'\nEN: {en}\nHE: {he}\n\n')
with open(f'{SP}/census_sifrei_en.txt', 'w', encoding='utf-8') as f:
    for p in P26:
        for r, row in enumerate(sif[p - 1], 1):
            f.write(f'=== Sifrei Bamidbar {p}:{r}\n{clean(row)}\n\n=== HE {p}:{r}\n{clean(sif_he[p - 1][r - 1])}\n\n')
with open(f'{SP}/census_hebrew.txt', 'w', encoding='utf-8') as f:
    for (c, v) in SPAN:
        f.write(f'== {c}:{v}\n')
        gl = dict(SG[(c, v)])
        f.write(' | '.join(f'{x} [{gl.get(x, "?")}]' + (f' <{m}>' if m and re.search(r"V.w", m) else '') for x, m in by[('Num', c, v)]) + '\n')
print('dumped', len(SPAN), 'verses; sifrei on 26:', P26, 'rows', [len(sif[p-1]) for p in P26], 'chars', sum(len(clean(r)) for p in P26 for r in sif[p-1]))
print('onkelos chars', sum(len(clean(onk[c-1][v-1])) + len(clean(onk_he[c-1][v-1])) for c, v in SPAN), 'hebrew chars', os.path.getsize(f'{SP}/census_hebrew.txt'))
