import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# DEUTERONOMY CHAPTER 10, THE READING (THE DEUTERONOMY WALK sitting 8, 2026-09-19; the owner: "Go"; ONE RUN under the two-run rule) — THE FIRST
# MEASUREMENT PASS, nothing typed (RUN 1 of four): (A0) THE TWO DIVISIONS — the export's chapter 6 aligned to the DB's by the same monotone
# alignment over token counts and negation counts, never by a typed table; the map EXP2DB used by every later section; (A) the shelf BY
# POSITION (the Sifrei on Deuteronomy's heads around chapter 5; the whole export scanned in both files for rows citing chapter 5 — the
# citation's verse number is the EXPORT'S and is mapped to the DB's); (B) the Onkelos dump per DB verse; (C) THE PARSER on every verse; (D) the
# case tokens, the frames and the register; (E) the register gate; (F) the prior reads; (G) the drafts; (H) the store's glosses.
# Chapter 9's form (ch9_dump0.py) derived by asserted substitutions (derive_ch10_dump0.py); section I (the spine ON the chapter) stays dropped — no piska
# head on chapter 10 either (the A print: 36 on 6:9, 37 on 11:10); the outside rows are the spine's whole contribution, as at chapters 4, 7, 8 and 9.
import json, re, html, os, sqlite3, subprocess, sys, io, contextlib, glob, unicodedata
from collections import Counter
ROOT = _ROOT
SP = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, f'{ROOT}/World/step9')
def clean(s): return re.sub(r'<[^>]+>', '', html.unescape(s))
def plain(w): return ''.join(c for c in w if c != '/' and not (0x0591 <= ord(c) <= 0x05C7))
CH = 10
print('==== A0. THE TWO DIVISIONS — the export\'s chapter', CH, 'against the DB\'s')
db = sqlite3.connect(f'file:{ROOT}/Data/tanakh.sqlite?mode=ro', uri=True)
VC = dict(db.execute("SELECT chapter, COUNT(*) FROM verses WHERE book='Deut' GROUP BY chapter").fetchall())
onk = json.load(open(f'{ROOT}/Data/sefaria_export/Onkelos_Deuteronomy/en.json', encoding='utf-8'))['text']
onk_he = json.load(open(f'{ROOT}/Data/sefaria_export/Onkelos_Deuteronomy/he.json', encoding='utf-8'))['text']
rows = db.execute("SELECT v.chapter, v.verse, w.he, w.morph, w.lemma FROM words w JOIN verses v ON w.verse_id=v.id WHERE v.book='Deut' AND v.chapter=? ORDER BY v.id, w.idx", (CH,)).fetchall()
by = {}
for c, v, h, m, lem in rows: by.setdefault((c, v), []).append((plain(h), m, h, lem))
NEG = ('לא', 'ולא')
D = [(len(by[(CH, v)]), sum(1 for x, _, _, _ in by[(CH, v)] if x in NEG)) for v in range(1, VC[CH] + 1)]
E = [(len(plain(clean(r)).split()), sum(1 for x in plain(clean(r)).split() if x.strip('.:') in NEG)) for r in onk_he[CH - 1]]
print('  DB verses', len(D), '| export verses HE', len(E), 'EN', len(onk[CH - 1]), '| per-chapter export lengths vs DB, chapters 1-10:', [(c, len(onk_he[c - 1]), VC[c]) for c in range(1, 11) if len(onk_he[c - 1]) != VC[c]])
INF = 10 ** 9
def cost(e, ds): return abs(e[0] - sum(d[0] for d in ds)) + 3 * abs(e[1] - sum(d[1] for d in ds))
best = {(0, 0): (0, None)}
for i in range(1, len(E) + 1):
    for j in range(i, len(D) + 1):
        cands = [(best[(i - 1, k)][0] + cost(E[i - 1], D[k:j]), k) for k in range(i - 1, j) if (i - 1, k) in best]
        if cands: best[(i, j)] = min(cands)
i, j, EXP2DB = len(E), len(D), {}
while i > 0:
    k = best[(i, j)][1]; EXP2DB[i] = list(range(k + 1, j + 1)); i, j = i - 1, k
DB2EXP = {d: e for e, ds in EXP2DB.items() for d in ds}
print('  the alignment cost', best[(len(E), len(D))][0], '| export verses mapped to MORE THAN ONE DB verse:', {e: ds for e, ds in EXP2DB.items() if len(ds) > 1})
print('  the offset per export verse (DB minus export, the first DB verse of each):', Counter(ds[0] - e for e, ds in EXP2DB.items()), '| the runs:', [(e, ds[0], ds[-1]) for e, ds in sorted(EXP2DB.items()) if e in (1, 16, 17, 18, 19, 30)])
print('  the shared export verse against its DB verses (tokens, negations):', [(e, E[e - 1], [(d, D[d - 1]) for d in ds]) for e, ds in EXP2DB.items() if len(ds) > 1])
print('==== A. THE SHELF BY POSITION — the Sifrei on Deuteronomy around chapter', CH)
he = json.load(open(f'{ROOT}/Data/sefaria_export/Sifrei_Devarim/he.json', encoding='utf-8'))['text']
en = json.load(open(f'{ROOT}/Data/sefaria_export/Sifrei_Devarim/en.json', encoding='utf-8'))['text']
print('  piskaot', len(he), len(en), 'rows', sum(len(s) for s in he), sum(len(s) for s in en))
HEB = {'א': 1, 'ב': 2, 'ג': 3, 'ד': 4, 'ה': 5, 'ו': 6, 'ז': 7, 'ח': 8, 'ט': 9, 'י': 10, 'כ': 20, 'ל': 30, 'מ': 40, 'נ': 50, 'ס': 60, 'ע': 70, 'פ': 80, 'צ': 90, 'ק': 100}
def gem(s): return sum(HEB.get(ch, 0) for ch in s)
heads = {}
for p in range(1, len(he) + 1):
    m = re.match(r'\(דברים ([א-ת]+) ([א-ת]+)(?:-[א-ת]+)?\)', clean(he[p-1][0]) if he[p-1] else '')
    heads[p] = (gem(m.group(1)), gem(m.group(2))) if m else None
print('  heads 34-39 (HE first citation | rows | EN first quote):')
for p in range(34, 40):
    e = clean(en[p-1][0]) if en[p-1] else ''; eq = re.search(r'“([^”]{0,70})', e)
    print(f'   {p:3d} head {heads[p]} | HE rows {len(he[p-1]):2d} EN rows {len(en[p-1]):2d} | {eq.group(1)[:60] if eq else e[:60]!r}')
print('  heads whose chapter is', CH, ':', [(p, h) for p, h in heads.items() if h and h[0] == CH], '| heads by chapter 1-10:', sorted(Counter(h[0] for h in heads.values() if h).items())[:10])
def he_cites(t): return [(b, gem(c), gem(v)) for b, c, v in re.findall(r'\(([א-ת]+(?: [א-ת])?) ([א-ת]{1,3}) ([א-ת]{1,3})\)', t)]
outside_he = [(p, r+1, c[2]) for p in range(1, len(he)+1) for r, row in enumerate(he[p-1]) for c in he_cites(clean(row)) if c[0] == 'דברים' and c[1] == CH]
print('  HE rows citing Deut', CH, '(the export\'s verse → the DB\'s):', len(outside_he), [(p, r, v, EXP2DB.get(v)) for p, r, v in outside_he])
en_forms = re.compile(r'\((?:Deut(?:eronomy)?\.?|Dt\.?|Devarim) ?(10):(\d+)')
outside_en = [(p, r+1, int(m.group(2))) for p in range(1, len(en)+1) for r, row in enumerate(en[p-1]) for m in en_forms.finditer(clean(row))]
print('  EN rows citing Deut', CH, ':', len(outside_en), [(p, r, v, EXP2DB.get(v)) for p, r, v in outside_en])
ibid = [(p, r+1, m.group(0), clean(row)[max(0, m.start()-120):m.start()]) for p in range(1, len(en)+1) for r, row in enumerate(en[p-1]) for m in re.finditer(r'\((?:Ibid|ibid)\.? ?10:(\d+)\)', clean(row))]
print('  EN "ibid 10:n" candidates:', len(ibid)); [print('    ', p, r, f, '<<', ctx[-100:].replace('\n', ' ')) for p, r, f, ctx in ibid[:40]]
allrows = sorted(set((p, r) for p, r, _ in outside_he) | set((p, r) for p, r, _ in outside_en))
print('  the union of rows (both files):', len(allrows), allrows)
with open(f'{SP}/ch10_sifrei_outside.txt', 'w', encoding='utf-8') as f:
    for p, r in allrows:
        f.write(f'\n## Sifrei {p}:{r} (head {heads[p]}) HE\n{clean(he[p-1][r-1])}\n\n## Sifrei {p}:{r} EN\n{clean(en[p-1][r-1]) if r <= len(en[p-1]) else "(no EN row)"}\n')
print('  outside rows file bytes', os.path.getsize(f'{SP}/ch10_sifrei_outside.txt'))
print('==== B. ONKELOS chapter', CH, 'and the DB (the dump per DB verse; a shared export row printed at its first DB verse)')
store = sqlite3.connect(f'file:{ROOT}/torah_grok.SNAPSHOT-main-51801ca.sqlite?mode=ro', uri=True)
SG = {}
for c, v, i, hp, g in store.execute("SELECT v.chapter, v.verse, w.idx, w.he_plain, w.gloss FROM words w JOIN verses v ON w.verse_id=v.id WHERE v.book='Deut' AND v.chapter=? ORDER BY v.id, w.idx", (CH,)):
    SG.setdefault((c, v), []).append((i, hp.replace('/', ''), g))
print('  the store\'s chapter', CH, 'verses', len(SG), '| verses whose store token count differs from the DB:', [(c, v, len(SG[(c, v)]), len(by[(c, v)])) for (c, v) in by if len(SG.get((c, v), [])) != len(by[(c, v)])])
print('  token count chapter', CH, ':', sum(len(by[(CH, v)]) for v in range(1, VC[CH] + 1)))
with open(f'{SP}/ch10_onkelos.txt', 'w', encoding='utf-8') as f:
    for v in range(1, VC[CH] + 1):
        e = DB2EXP[v]; shared = EXP2DB[e]
        f.write(f'\n== Deut {CH}:{v} (export {e}{" = DB " + str(shared[0]) + "-" + str(shared[-1]) if len(shared) > 1 else ""})\n  HE  {" ".join(x for x, _, _, _ in by[(CH, v)])}\n  MOR {" ".join(f"{x}:{m}" for x, m, _, _ in by[(CH, v)])}\n  LEM {" ".join(f"{x}:{(l or chr(63)).split(chr(47))[-1].strip()}" for x, _, _, l in by[(CH, v)])}\n  GL  {" | ".join(f"{hp}={g}" for _, hp, g in SG.get((CH, v), []))}\n')
        if v == shared[0]: f.write(f'  ONK {clean(onk[CH-1][e-1])}\n  ARM {plain(clean(onk_he[CH-1][e-1]))}\n')
print('  onkelos dump bytes', os.path.getsize(f'{SP}/ch10_onkelos.txt'))
print('==== C. THE PARSER on every verse of chapter', CH)
with contextlib.redirect_stdout(io.StringIO()):
    import cold_run_sequence as CS
hit = []
for v in range(1, VC[CH] + 1):
    vw = CS.verse_words('Deut', CH, v)
    marked = [t for t in vw if t[-1] in '#~^%@|*']
    n, o = CS.ink_numbers(vw), CS.ink_ordinals(vw)
    if n or o or marked: print(f'  {CH}:{v:<3} N {n!s:<24} O {o!s:<14} marked {marked}'); hit.append(v)
NUMW = ('אחד', 'אחת', 'שנים', 'שני', 'שתי', 'שלש', 'שלשה', 'שלשת', 'ארבע', 'ארבעה', 'ארבעים', 'חמש', 'שש', 'ששת', 'שבע', 'שביעי', 'עשר', 'עשרה', 'עשרת', 'מאה', 'אלף', 'אלפים', 'ראשון', 'שני', 'שלישי', 'רבעים', 'שלשים')
numv = {f'{CH}:{v}': [x for x, _, _, _ in by[(CH, v)] if x in NUMW or x[1:] in NUMW] for v in range(1, VC[CH] + 1) if any(x in NUMW or x[1:] in NUMW for x, _, _, _ in by[(CH, v)])}
print('  number-word tokens present per verse (the bare check against the parser):', numv)
for v in sorted(set(hit) | {int(k.split(':')[1]) for k in numv} | {1, 22}):
    print(f'  {CH}:{v} tokens:', CS.verse_words('Deut', CH, v))
print('==== D. CASE TOKENS, FRAMES, REGISTER, NAMES')
print('  case tokens (כי "when/for" / אם "if" / ואם / או "or" / פן "lest"):', {f'{CH}:{v}': [x for x, m, _, _ in by[(CH, v)] if x in ('כי', 'אם', 'ואם', 'או', 'פן', 'ופן')] for v in range(1, VC[CH] + 1) if any(x in ('כי', 'אם', 'ואם', 'או', 'פן', 'ופן') for x, m, _, _ in by[(CH, v)])})
print('  divine frames (ויאמר/וידבר + יהוה):', [f'{CH}:{v}' for v in range(1, VC[CH] + 1) for i, (x, _, _, _) in enumerate(by[(CH, v)][:-1]) if x in ('ויאמר', 'וידבר') and by[(CH, v)][i + 1][0] == 'יהוה'])
print('  לאמר "saying" seats:', [f'{CH}:{v}' for v in range(1, VC[CH] + 1) if any(x == 'לאמר' for x, _, _, _ in by[(CH, v)])])
print('  narrative-form verbs (V.w) per verse:', {v: [x for x, m, _, _ in by[(CH, v)] if m and re.search(r'V.w', m)] for v in range(1, VC[CH] + 1) if any(m and re.search(r'V.w', m) for _, m, _, _ in by[(CH, v)])})
print('  first-person verb forms (1cs / 1cp) per verse:', {v: [(x, m) for x, m, _, _ in by[(CH, v)] if m and re.search(r'1c[sp]', m) and m.startswith('HV')] for v in range(1, VC[CH] + 1) if any(m and re.search(r'1c[sp]', m) and m.startswith('HV') for _, m, _, _ in by[(CH, v)])})
print('  imperatives (Vq.v / Vp.v / Vh.v) per verse:', {v: [(x, m) for x, m, _, _ in by[(CH, v)] if m and re.search(r'^HV..v', m)] for v in range(1, VC[CH] + 1) if any(m and re.search(r'^HV..v', m) for _, m, _, _ in by[(CH, v)])})
print('  prohibitions לא + imperfect (the ten\'s form) per verse:', {v: [(by[(CH, v)][i + 1][0], by[(CH, v)][i + 1][1]) for i, (x, _, _, _) in enumerate(by[(CH, v)][:-1]) if x in NEG and by[(CH, v)][i + 1][1] and by[(CH, v)][i + 1][1].startswith('HV') and 'i' in by[(CH, v)][i + 1][1][3:5]] for v in range(1, VC[CH] + 1) if any(x in NEG for x, _, _, _ in by[(CH, v)])})
print('  name tokens (Np):', {v: [x for x, m, _, _ in by[(CH, v)] if m and 'Np' in m] for v in range(1, VC[CH] + 1) if any(m and 'Np' in m for _, m, _, _ in by[(CH, v)])})
print('  second-person plural vs singular (2mp / 2ms tokens per verse):', {v: (sum(1 for _, m, _, _ in by[(CH, v)] if m and '2mp' in m), sum(1 for _, m, _, _ in by[(CH, v)] if m and '2ms' in m)) for v in range(1, VC[CH] + 1)})
print('==== E. THE REGISTER GATE on Deut', CH)
RD = open(f'{ROOT}/World/step9/register_dispositions.yaml', encoding='utf-8').read()
print('  dispositions naming Deut 10:', re.findall(r'^([^\n]*Deut 10:[^\n]*)$', RD, re.M)[:20])
RI = open(f'{ROOT}/World/step9/REGISTER_INDEX.md', encoding='utf-8').read()
print('  REGISTER_INDEX lines on Deut 10:'); [print('   ', l[:220]) for l in RI.split('\n') if re.search(r'Deut 10:', l)]
print('==== F. THE PRIOR READS')
TRI = f'{ROOT}/logic/oral_triage'
LED = {f: open(f'{TRI}/{f}', encoding='utf-8').read() for f in os.listdir(TRI) if f.endswith('.md') and os.path.isfile(f'{TRI}/{f}')}
print('  ledgers with an Onkelos Deut 10 row:', sorted(f for f, t in LED.items() if re.search(r'^- Onkelos Deut 10:', t, re.M)))
PRIOR = sorted({(f, int(a), int(b)) for f, t in LED.items() for a, b in re.findall(r'Sifrei Devarim (\d+):(\d+)', t)})
print('  prior Sifrei Devarim rows anywhere (strict form), those among the outside rows:', [(f, p, r) for f, p, r in PRIOR if (p, r) in allrows], '| all prior rows count', len(PRIOR))
NAMING = sorted((f, len(re.findall(r'Deut(?:eronomy)? 10:\d+', t)), sorted(set(re.findall(r'Deut(?:eronomy)? 10:\d+(?:-\d+)?', t)))[:14]) for f, t in LED.items() if re.search(r'Deut(?:eronomy)? 10:\d+', t))
print('  ledgers NAMING a verse of Deut 10:', len(NAMING)); [print('   ', n) for n in NAMING]
print('  ledgers with an Onkelos Exod 25, 34 or 37 row (the kin\'s reading — the ark 25:10-22, the second tablets 34:1-4 and 28-29, the ark made 37:1-9):', sorted(f for f, t in LED.items() if re.search(r'^- Onkelos Exod (25|34|37):', t, re.M)), '| Tanchuma rows on Exod 25/34/37 anywhere:', sum(len(re.findall(r'Tanchuma[^\n]{0,40}(?:25|34|37):\d+', t)) for t in LED.values()), '| ledgers with an Onkelos Num 3, 8, 18, 20 or 33 row (the Levites 3:5-13, 8:5-26, 18:20-24; Aaron\'s death 20:22-29; the journeys 33:30-39):', sorted(f for f, t in LED.items() if re.search(r'^- Onkelos Num (3|8|18|20|33):', t, re.M)))
print('==== G. THE DRAFTS')
for uid in sorted(os.path.basename(f)[:-5] for f in glob.glob(f'{ROOT}/logic/units/deu_09*.yaml') + glob.glob(f'{ROOT}/logic/units/deu_10*.yaml')):
    t = open(f'{ROOT}/logic/units/{uid}.yaml', encoding='utf-8').read()
    st = sorted({(int(a), int(b)) for a, b in re.findall(r'id: STEP_Dt_(\d+)_(\d+)', t)})
    refs = re.search(r'refs: "([^"]+)"', t).group(1)
    print(f'  {uid}: refs {refs}; steps {st[0]}..{st[-1]} n={len(st)}; draft {"status: draft" in t}; operators {"operators:" in t}; depends_on {re.findall(r"depends_on:\n((?:    - \"[^\"]+\"\n)+)", t)[:1]}; scenarios {t.count(chr(10) + "  - id: S")}; binary_trees {chr(10) + "binary_trees:" in t}; step E {"- step: E" in t}; comment lines {t.count(chr(10) + "    comment:") + t.count(chr(10) + "      comment:")}')
    if uid.startswith('deu_10'): print('    the step verses:', [b for a, b in st], '| covers DB', VC[CH], '?', [b for a, b in st] == list(range(1, VC[CH] + 1)))
print('  the units\' claim prefixes present anywhere?', {p: sum(1 for f in glob.glob(f'{ROOT}/logic/oral_audit/manifests/*_claims.json') + glob.glob(f'{ROOT}/logic/units/*.yaml') if f'{p}-' in open(f, encoding='utf-8').read()) for p in ('DV10', 'DV10A', 'DV10B', 'DV09', 'DV11')})
print('  existing manifests deu_10*:', sorted(os.path.basename(f) for f in glob.glob(f'{ROOT}/logic/oral_audit/manifests/deu_10*')), '| ledgers deu_*:', sorted(f for f in LED if f.startswith('deu_')))
print('  unit count and standing (CORPUS_TRUTH literals):', re.findall(r'^(?:N_UNITS|UNITS_FROZEN|STANDING|N_STANDING|WORLD_HASH)[^\n]*', open(f'{ROOT}/logic/corpus/CORPUS_TRUTH.py', encoding='utf-8').read(), re.M)[:6])
print('==== H. THE STORE\'S GLOSSES on chapter', CH)
print('  gloss Counter (the 50 commonest):', Counter(g for k in SG for _, _, g in SG[k]).most_common(50))
with open(f'{SP}/ch10_store_glosses.txt', 'w', encoding='utf-8') as f:
    for (c, v) in sorted(SG): f.write(f'{c}:{v}: ' + str([(i, t, g) for i, t, g in SG[(c, v)]]) + '\n')
print('  gloss file bytes', os.path.getsize(f'{SP}/ch10_store_glosses.txt'))
OV = open(f'{ROOT}/logic/glosses/word_gloss_overrides.yaml', encoding='utf-8').read()
print('  overrides already for Deut.10:', re.findall(r'"Deut\.10\.[^"]+": "[^"]+"', OV)[:20], '| by_ref last Deut.9 line:', [l for l in OV.split('\n') if l.startswith('  "Deut.9.')][-1:])
print('==== I. THE SPINE ON THE CHAPTER — none: no piska head in chapter', CH, '(the heads by chapter above); the outside rows are the spine here')
print('  the heads whose chapter is', CH, ':', [(p, h) for p, h in heads.items() if h and h[0] == CH], '| the nearest heads:', {p: heads[p] for p in (36, 37)})
