import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# THE NUMBERS WALK, sitting 5 — KORACH (2026-09-10; the owner: "Go" after the #124 rereads, on the ruling READ THEN COMPILE): THE FIRST
# MEASUREMENT PASS over Numbers 16:1-18:32 — the shelf's heads by position, the drafts' spans, the prior-read scan, the engine's parser
# on the portion's numbers, and the DUMPS the reading runs on (Onkelos EN + HE per verse; the Sifrei's rows on chapter 18; the pointed
# Hebrew with the store's own glosses). Nothing typed — everything printed from the DB, the store and the shelf's bytes.
import json, os, re, html, sqlite3, sys, io, contextlib, unicodedata
from collections import Counter
ROOT = _ROOT
SP = os.path.dirname(os.path.abspath(__file__))
def clean(s): return re.sub(r'<[^>]+>', '', html.unescape(s))
sif = json.load(open(f'{ROOT}/Data/sefaria_export/Sifrei_Bamidbar/en.json'))['text']
onk = json.load(open(f'{ROOT}/Data/sefaria_export/Onkelos_Numbers/en.json'))['text']
onk_he = json.load(open(f'{ROOT}/Data/sefaria_export/Onkelos_Numbers/he.json'))['text']
heads = {}
for p, rows in enumerate(sif, 1):
    if not rows: continue
    m = re.search(r'\((Bamidbar|Devarim)\.? (\d+):(\d+)', clean(rows[0])[:60])
    heads[p] = (m.group(1), int(m.group(2)), int(m.group(3))) if m else None
print('HEADS 112-126:', {p: heads.get(p) for p in range(112, 127)})
print('HEADS naming 16 or 17:', sorted(p for p, h in heads.items() if h and h[0] == 'Bamidbar' and h[1] in (16, 17)))
print('HEADS naming 18:', sorted(p for p, h in heads.items() if h and h[0] == 'Bamidbar' and h[1] == 18))
print('HEADS naming 19:', sorted(p for p, h in heads.items() if h and h[0] == 'Bamidbar' and h[1] == 19))
print('HEADLESS 113-126:', [p for p in range(113, 127) if heads.get(p) is None])
for p in range(116, 124):
    print(f'  piska {p}: rows {len(sif[p-1])}; opens: {clean(sif[p-1][0])[:160]!r}')
print('ONK_LEN:', {c: (len(onk[c - 1]), len(onk_he[c - 1])) for c in range(15, 20)})
shelf_numbers = sorted(d for d in os.listdir(f'{ROOT}/Data/sefaria_export') if re.search(r'Numbers|Bamidbar', d))
outside = [d for d in shelf_numbers if d not in ('Sifrei_Bamidbar', 'Onkelos_Numbers')]
print('OUTSIDE:', len(outside), outside)
# the drafts
def unit_text(uid): return open(f'{ROOT}/logic/units/{uid}.yaml', encoding='utf-8').read()
def steps(uid): return sorted({(int(a), int(b)) for a, b in re.findall(r'STEP_Nm_(\d+)_(\d+)', unit_text(uid))})
for uid in ('num_16_korach', 'num_17_plague_staff', 'num_18_priest_levite_dues', 'num_19_parah'):
    st = steps(uid); print(uid, 'status draft' if 'status: draft' in unit_text(uid) else 'NOT DRAFT', st[0], st[-1], len(st), 'operators:' in unit_text(uid))
db = sqlite3.connect(f'file:{ROOT}/Data/tanakh.sqlite?mode=ro', uri=True)
VC = dict(db.execute("SELECT chapter, COUNT(*) FROM verses WHERE book='Num' GROUP BY chapter").fetchall())
print('VC 16-19:', {c: VC[c] for c in (16, 17, 18, 19)})
# the prior reads
TRI = f'{ROOT}/logic/oral_triage'
LED = {f: open(f'{TRI}/{f}', encoding='utf-8').read() for f in os.listdir(TRI) if f.endswith('.md')}
print('PRIOR sifrei 116-122:', sorted(f for f, t in LED.items() if re.search(r'Sifrei Bamidbar (11[6-9]|12[0-2]):\d', t)))
print('PRIOR onkelos 16-18:', sorted(f for f, t in LED.items() if re.search(r'Onkelos Num (16|17|18):\d', t)))
# the ink
def plain(w): return ''.join(c for c in w if c != '/' and not (0x0591 <= ord(c) <= 0x05C7))
def pointed(w): return ''.join(c for c in w if c != '/' and not (0x0591 <= ord(c) <= 0x05AF))
rows = db.execute("SELECT v.book, v.chapter, v.verse, w.he, w.morph FROM words w JOIN verses v ON w.verse_id=v.id ORDER BY v.id, w.idx").fetchall()
by, byp = {}, {}
for b, c, v, he, m in rows:
    by.setdefault((b, c, v), []).append((plain(he), m)); byp.setdefault((b, c, v), []).append(pointed(he))
store = sqlite3.connect(f'file:{ROOT}/torah_grok.SNAPSHOT-main-51801ca.sqlite?mode=ro', uri=True)
SG = {}
for c, v, hp, g in store.execute("SELECT v.chapter, v.verse, w.he_plain, w.gloss FROM words w JOIN verses v ON w.verse_id=v.id WHERE v.book='Num' AND v.chapter BETWEEN 16 AND 18 ORDER BY v.id, w.idx"):
    SG.setdefault((c, v), []).append((hp.replace('/', ''), g))
SPAN = [(16, v) for v in range(1, 36)] + [(17, v) for v in range(1, 29)] + [(18, v) for v in range(1, 33)]
# the parser
sys.path.insert(0, f'{ROOT}/World/step9')
with contextlib.redirect_stdout(io.StringIO()):
    import cold_run_sequence as CS
def N(b, c, v): return CS.ink_numbers(CS.verse_words(b, c, v))
NUMTOK = re.compile(r'^(ו?ה?)(אחד|אחת|שנים|שתים|שני|שתי|שלש|שלשה|שלשת|ארבע|ארבעה|חמש|חמשה|חמשת|שש|ששה|שבע|שבעה|שמנה|שמונה|תשע|תשעה|עשר|עשרה|עשרים|שלשים|ארבעים|חמשים|ששים|שבעים|שמנים|תשעים|מאה|מאת|מאתים|אלף|אלפים|עשרון|עשרנים|מעשר|חצי|רבע|שלשית|מאות|רבבה|עשרת|שבעת|ארבעת|ששת|תשעת|חמשת|שמנת)(ים|ה|ת|י|ו|ם|ך|כם|ו)?$')
print('--- PARSER on 16-18 (verses with a number-like token) ---')
for (c, v) in SPAN:
    ws = [x for x, _ in by[('Num', c, v)]]
    cand = [x for x in ws if NUMTOK.match(x) or 'עשר' in x or 'מאה' in x or 'אלף' in x or 'מאות' in x]
    n = N('Num', c, v)
    if cand or n: print(f'  {c}:{v} tokens={cand} -> {n}')
# the frames and the register
FR = [(c, v) for (c, v) in SPAN if [x for x, _ in by[('Num', c, v)]][0] in ('וידבר', 'ויאמר') and [x for x, _ in by[('Num', c, v)]][1] == 'יהוה']
print('FRAMES:', FR, 'to whom:', [(c, v, [x for x, _ in by[('Num', c, v)]][2:5]) for c, v in FR])
REG = {}
for (c, v) in SPAN:
    vs = [(x, [q for q in m.split('/') if 'V' in q][0]) for x, m in by[('Num', c, v)] if m and re.search(r'V.w', m)]
    if vs: REG[(c, v)] = vs
print('REG count', len(REG), Counter(c for c, v in REG), 'max', max(REG.items(), key=lambda kv: len(kv[1]))[0], max(len(v) for v in REG.values()))
# THE DUMPS
with open(f'{SP}/korach_onkelos.txt', 'w', encoding='utf-8') as f:
    for (c, v) in SPAN:
        f.write(f'=== Onkelos Num {c}:{v}\nEN: {clean(onk[c-1][v-1])}\nHE: {clean(onk_he[c-1][v-1])}\n\n')
with open(f'{SP}/korach_sifrei_en.txt', 'w', encoding='utf-8') as f:
    for p in range(116, 124):
        for r, row in enumerate(sif[p - 1], 1):
            f.write(f'=== Sifrei Bamidbar {p}:{r}\n{clean(row)}\n\n')
with open(f'{SP}/korach_hebrew.txt', 'w', encoding='utf-8') as f:
    for (c, v) in SPAN:
        f.write(f'== {c}:{v}\n')
        gl = dict(SG[(c, v)])
        f.write(' | '.join(f'{x} [{gl.get(x, "?")}]' + (f' <{m}>' if m and re.search(r"V.w", m) else '') for x, m in by[('Num', c, v)]) + '\n')
print('dumped', len(SPAN), 'verses')
