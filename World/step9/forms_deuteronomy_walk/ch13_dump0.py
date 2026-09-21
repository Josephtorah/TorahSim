import os as _os
_ROOT = _os.path.normpath(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', '..', '..'))   # THE PORTABLE REPO (2026-09-15): the repo root from this file's own place
#!/usr/bin/env python3
# DEUTERONOMY CHAPTER 13, THE READING (THE DEUTERONOMY WALK sitting 11, 2026-09-21; the owner: "Go" after the reread that followed 10b's compaction; ONE RUN + ITS TAIL under the cost rules) — THE FIRST
# MEASUREMENT PASS, nothing typed (RUN 1 of four): (A0) THE TWO DIVISIONS — the export's chapter 6 aligned to the DB's by the same monotone
# alignment over token counts and negation counts, never by a typed table; the map EXP2DB used by every later section; (A) the shelf BY
# POSITION (the Sifrei on Deuteronomy's heads around chapter 5; the whole export scanned in both files for rows citing chapter 5 — the
# citation's verse number is the EXPORT'S and is mapped to the DB's); (B) the Onkelos dump per DB verse; (C) THE PARSER on every verse; (D) the
# case tokens, the frames and the register; (E) the register gate; (F) the prior reads; (G) the drafts; (H) the store's glosses.
# Chapter 12's form (ch12_dump0.py) derived by asserted substitutions (derive_ch13_dump0.py); SECTION I in chapter 6's form — THE SPINE IS ON THE CHAPTER
# (sitting 10's print: 82 heads on 13:1): the SPINE computed from the heads, the outside rows the union less the spine's own piskaot; NO portion edge inside
# the chapter (Re'eh 11:26-16:17 holds it whole — the chapter the unit, per the ruling CHAPTER NUMBERS); NINETEEN verses in the DB's numbering (the English's
# 12:32 the DB's 13:1 — the export's chapter 13 against the DB's measured at A0, never typed).
import json, re, html, os, sqlite3, subprocess, sys, io, contextlib, glob, unicodedata
from collections import Counter
ROOT = _ROOT
SP = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, f'{ROOT}/World/step9')
def clean(s): return re.sub(r'<[^>]+>', '', html.unescape(s))
def plain(w): return ''.join(c for c in w if c != '/' and not (0x0591 <= ord(c) <= 0x05C7))
CH = 13
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
print('  DB verses', len(D), '| export verses HE', len(E), 'EN', len(onk[CH - 1]), '| per-chapter export lengths vs DB, chapters 1-13:', [(c, len(onk_he[c - 1]), VC[c]) for c in range(1, 14) if len(onk_he[c - 1]) != VC[c]])
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
print('  heads 80-100 (HE first citation | rows | EN first quote):')
for p in range(80, 101):
    e = clean(en[p-1][0]) if en[p-1] else ''; eq = re.search(r'“([^”]{0,70})', e)
    print(f'   {p:3d} head {heads[p]} | HE rows {len(he[p-1]):2d} EN rows {len(en[p-1]):2d} | {eq.group(1)[:60] if eq else e[:60]!r}')
print('  heads whose chapter is', CH, ':', [(p, h) for p, h in heads.items() if h and h[0] == CH], '| heads by chapter 1-13:', sorted(Counter(h[0] for h in heads.values() if h).items())[:13])
def he_cites(t): return [(b, gem(c), gem(v)) for b, c, v in re.findall(r'\(([א-ת]+(?: [א-ת])?) ([א-ת]{1,3}) ([א-ת]{1,3})\)', t)]
outside_he = [(p, r+1, c[2]) for p in range(1, len(he)+1) for r, row in enumerate(he[p-1]) for c in he_cites(clean(row)) if c[0] == 'דברים' and c[1] == CH]
print('  HE rows citing Deut', CH, '(the export\'s verse → the DB\'s):', len(outside_he), [(p, r, v, EXP2DB.get(v)) for p, r, v in outside_he])
en_forms = re.compile(r'\((?:Deut(?:eronomy)?\.?|Dt\.?|Devarim) ?(13):(\d+)')
outside_en = [(p, r+1, int(m.group(2))) for p in range(1, len(en)+1) for r, row in enumerate(en[p-1]) for m in en_forms.finditer(clean(row))]
print('  EN rows citing Deut', CH, ':', len(outside_en), [(p, r, v, EXP2DB.get(v)) for p, r, v in outside_en])
en_1232 = [(p, r+1) for p in range(1, len(en)+1) for r, row in enumerate(en[p-1]) if re.search(r'\((?:Deut(?:eronomy)?\.?|Dt\.?|Devarim) ?12:32', clean(row))]
print('  EN rows citing Deut 12:32 (the ENGLISH\'S number for the DB\'s 13:1 — the union takes them as 13:1):', len(en_1232), en_1232)
outside_en += [(p, r, 1) for p, r in en_1232 if (p, r, 1) not in outside_en]
ibid = [(p, r+1, m.group(0), clean(row)[max(0, m.start()-120):m.start()]) for p in range(1, len(en)+1) for r, row in enumerate(en[p-1]) for m in re.finditer(r'\((?:Ibid|ibid)\.? ?13:(\d+)\)', clean(row))]
print('  EN "ibid 13:n" candidates:', len(ibid)); [print('    ', p, r, f, '<<', ctx[-100:].replace('\n', ' ')) for p, r, f, ctx in ibid[:40]]
allrows = sorted(set((p, r) for p, r, _ in outside_he) | set((p, r) for p, r, _ in outside_en))
print('  the union of rows (both files):', len(allrows), allrows)
SPINE = sorted(p for p, h in heads.items() if h and h[0] == CH)   # COMPUTED from the heads, never typed (chapter 6 typed its six from the print)
OUTSIDE = [(p, r) for p, r in allrows if p not in SPINE]
print('  the rows OUTSIDE the spine piskaot (the union less the on-chapter piskaot', SPINE[0], '-', SPINE[-1], '):', len(OUTSIDE), OUTSIDE, '| in-spine rows of the union:', len(allrows) - len(OUTSIDE))
with open(f'{SP}/ch13_sifrei_outside.txt', 'w', encoding='utf-8') as f:
    for p, r in OUTSIDE:
        f.write(f'\n## Sifrei {p}:{r} (head {heads[p]}) HE\n{clean(he[p-1][r-1])}\n\n## Sifrei {p}:{r} EN\n{clean(en[p-1][r-1]) if r <= len(en[p-1]) else "(no EN row)"}\n')
print('  outside rows file bytes', os.path.getsize(f'{SP}/ch13_sifrei_outside.txt'))
print('==== B. ONKELOS chapter', CH, 'and the DB (the dump per DB verse; a shared export row printed at its first DB verse)')
store = sqlite3.connect(f'file:{ROOT}/torah_grok.SNAPSHOT-main-51801ca.sqlite?mode=ro', uri=True)
SG = {}
for c, v, i, hp, g in store.execute("SELECT v.chapter, v.verse, w.idx, w.he_plain, w.gloss FROM words w JOIN verses v ON w.verse_id=v.id WHERE v.book='Deut' AND v.chapter=? ORDER BY v.id, w.idx", (CH,)):
    SG.setdefault((c, v), []).append((i, hp.replace('/', ''), g))
print('  the store\'s chapter', CH, 'verses', len(SG), '| verses whose store token count differs from the DB:', [(c, v, len(SG[(c, v)]), len(by[(c, v)])) for (c, v) in by if len(SG.get((c, v), [])) != len(by[(c, v)])])
print('  token count chapter', CH, ':', sum(len(by[(CH, v)]) for v in range(1, VC[CH] + 1)))
with open(f'{SP}/ch13_onkelos.txt', 'w', encoding='utf-8') as f:
    for v in range(1, VC[CH] + 1):
        e = DB2EXP[v]; shared = EXP2DB[e]
        f.write(f'\n== Deut {CH}:{v} (export {e}{" = DB " + str(shared[0]) + "-" + str(shared[-1]) if len(shared) > 1 else ""})\n  HE  {" ".join(x for x, _, _, _ in by[(CH, v)])}\n  MOR {" ".join(f"{x}:{m}" for x, m, _, _ in by[(CH, v)])}\n  LEM {" ".join(f"{x}:{(l or chr(63)).split(chr(47))[-1].strip()}" for x, _, _, l in by[(CH, v)])}\n  GL  {" | ".join(f"{hp}={g}" for _, hp, g in SG.get((CH, v), []))}\n')
        if v == shared[0]: f.write(f'  ONK {clean(onk[CH-1][e-1])}\n  ARM {plain(clean(onk_he[CH-1][e-1]))}\n')
print('  onkelos dump bytes', os.path.getsize(f'{SP}/ch13_onkelos.txt'))
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
for v in sorted(set(hit) | {int(k.split(':')[1]) for k in numv} | {1, 19}):
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
print('  dispositions naming Deut 13:', re.findall(r'^([^\n]*Deut 13:[^\n]*)$', RD, re.M)[:20])
RI = open(f'{ROOT}/World/step9/REGISTER_INDEX.md', encoding='utf-8').read()
print('  REGISTER_INDEX lines on Deut 13:'); [print('   ', l[:220]) for l in RI.split('\n') if re.search(r'Deut 13:', l)]
print('==== F. THE PRIOR READS')
TRI = f'{ROOT}/logic/oral_triage'
LED = {f: open(f'{TRI}/{f}', encoding='utf-8').read() for f in os.listdir(TRI) if f.endswith('.md') and os.path.isfile(f'{TRI}/{f}')}
print('  ledgers with an Onkelos Deut 13 row:', sorted(f for f, t in LED.items() if re.search(r'^- Onkelos Deut 13:', t, re.M)))
PRIOR = sorted({(f, int(a), int(b)) for f, t in LED.items() for a, b in re.findall(r'Sifrei Devarim (\d+):(\d+)', t)})
print('  prior Sifrei Devarim rows anywhere (strict form), those among the outside rows:', [(f, p, r) for f, p, r in PRIOR if (p, r) in allrows], '| all prior rows count', len(PRIOR))
NAMING = sorted((f, len(re.findall(r'Deut(?:eronomy)? 13:\d+', t)), sorted(set(re.findall(r'Deut(?:eronomy)? 13:\d+(?:-\d+)?', t)))[:14]) for f, t in LED.items() if re.search(r'Deut(?:eronomy)? 13:\d+', t))
print('  ledgers NAMING a verse of Deut 13:', len(NAMING)); [print('   ', n) for n in NAMING]
print('  ledgers with an Onkelos Exod 22 row (the kin\'s reading — the sacrifice to other gods 22:19 for 13:2-12) or an Exod 32 row (the calf\'s "these are your gods" for 13:3, 13:7, 13:14):', sorted(f for f, t in LED.items() if re.search(r'^- Onkelos Exod (?:22|32):', t, re.M)), '| ledgers with an Onkelos Lev 20 or Lev 24 row (the stoning by the people 20:2 and by the witnesses 24:14-16 for 13:10-11) or a Lev 27 row (the devoted thing 27:28-29 for 13:16-18):', sorted(f for f, t in LED.items() if re.search(r'^- Onkelos Lev (?:20|24|27):', t, re.M)), '| ledgers with an Onkelos Num 15 row (the high hand 15:30-31) or a Num 25 row (the fierce anger 25:4 for 13:18) or a Deut 4 / Deut 7 / Deut 8 row (the signs and wonders 4:34, the ban and the devoted thing 7:2, 7:25-26, the testing 8:2, 8:16 — 13:2-4\'s and 13:16-18\'s kin):', sorted(f for f, t in LED.items() if re.search(r'^- Onkelos (?:Num 15|Num 25|Deut 4|Deut 7|Deut 8):', t, re.M)), '| ledgers with an Onkelos Gen 22 row (the test 22:1 for 13:4):', sorted(f for f, t in LED.items() if re.search(r'^- Onkelos Gen 22:', t, re.M)))
print('==== G. THE DRAFTS')
for uid in sorted(os.path.basename(f)[:-5] for f in glob.glob(f'{ROOT}/logic/units/deu_12*.yaml') + glob.glob(f'{ROOT}/logic/units/deu_13*.yaml')):
    t = open(f'{ROOT}/logic/units/{uid}.yaml', encoding='utf-8').read()
    st = sorted({(int(a), int(b)) for a, b in re.findall(r'id: STEP_Dt_(\d+)_(\d+)', t)})
    refs = re.search(r'refs: "([^"]+)"', t).group(1)
    print(f'  {uid}: refs {refs}; steps {st[0]}..{st[-1]} n={len(st)}; draft {"status: draft" in t}; operators {"operators:" in t}; depends_on {re.findall(r"depends_on:\n((?:    - \"[^\"]+\"\n)+)", t)[:1]}; scenarios {t.count(chr(10) + "  - id: S")}; binary_trees {chr(10) + "binary_trees:" in t}; step E {"- step: E" in t}; comment lines {t.count(chr(10) + "    comment:") + t.count(chr(10) + "      comment:")}')
    if uid.startswith('deu_13'): print('    the step verses:', [b for a, b in st], '| covers DB', VC[CH], '?', [b for a, b in st] == list(range(1, VC[CH] + 1)))
print('  the units\' claim prefixes present anywhere?', {p: sum(1 for f in glob.glob(f'{ROOT}/logic/oral_audit/manifests/*_claims.json') + glob.glob(f'{ROOT}/logic/units/*.yaml') if f'{p}-' in open(f, encoding='utf-8').read()) for p in ('DV13', 'DV13A', 'DV13B', 'DV12', 'DV14')})
print('  existing manifests deu_13*:', sorted(os.path.basename(f) for f in glob.glob(f'{ROOT}/logic/oral_audit/manifests/deu_13*')), '| ledgers deu_*:', sorted(f for f in LED if f.startswith('deu_')))
print('  unit count and standing (CORPUS_TRUTH literals):', re.findall(r'^(?:N_UNITS|UNITS_FROZEN|STANDING|N_STANDING|WORLD_HASH)[^\n]*', open(f'{ROOT}/logic/corpus/CORPUS_TRUTH.py', encoding='utf-8').read(), re.M)[:6])
print('==== H. THE STORE\'S GLOSSES on chapter', CH)
print('  gloss Counter (the 50 commonest):', Counter(g for k in SG for _, _, g in SG[k]).most_common(50))
with open(f'{SP}/ch13_store_glosses.txt', 'w', encoding='utf-8') as f:
    for (c, v) in sorted(SG): f.write(f'{c}:{v}: ' + str([(i, t, g) for i, t, g in SG[(c, v)]]) + '\n')
print('  gloss file bytes', os.path.getsize(f'{SP}/ch13_store_glosses.txt'))
OV = open(f'{ROOT}/logic/glosses/word_gloss_overrides.yaml', encoding='utf-8').read()
print('  overrides already for Deut.13:', re.findall(r'"Deut\.13\.[^"]+": "[^"]+"', OV)[:20], '| by_ref last Deut.12 line:', [l for l in OV.split('\n') if l.startswith('  "Deut.12.')][-1:])
print('==== I. THE SPINE ON THE CHAPTER — the Sifrei piskaot whose head is in chapter', CH, '(the first on-chapter piskaot since chapter 6), whole')
print('  SPINE (computed from the heads):', SPINE, '| contiguous?', SPINE == list(range(SPINE[0], SPINE[-1] + 1)), '| the heads by verse:', [(p, heads[p][1]) for p in SPINE], '| the heads before and after:', {p: heads[p] for p in (SPINE[0] - 1, SPINE[-1] + 1)})
rows_ps = {p: (len(he[p - 1]), len(en[p - 1])) for p in SPINE}
print('  rows per piska (HE, EN):', rows_ps, '| total HE rows', sum(a for a, _ in rows_ps.values()), '| HE == EN everywhere?', all(a == b for a, b in rows_ps.values()))
with open(f'{SP}/ch13_sifrei_spine.txt', 'w', encoding='utf-8') as f:
    for p in SPINE:
        for r in range(len(he[p - 1])): f.write(f'--- {p}:{r + 1} (head {heads[p]})\nHE: {clean(he[p - 1][r])}\nEN: {clean(en[p - 1][r]) if r < len(en[p - 1]) else "(no EN row)"}\n')
print('  spine file bytes', os.path.getsize(f'{SP}/ch13_sifrei_spine.txt'), '| bytes per piska HE+EN:', {p: sum(len(clean(he[p - 1][r])) + (len(clean(en[p - 1][r])) if r < len(en[p - 1]) else 0) for r in range(len(he[p - 1]))) for p in SPINE})
print('  prior reads among the spine rows (any ledger):', [(f, p, r) for f, p, r in PRIOR if p in SPINE])
print('  the spine rows citing a verse of chapter', CH, 'in the Hebrew (p, r, the export verses):', [(p, r + 1, sorted({c[2] for c in he_cites(clean(he[p - 1][r])) if c[0] == 'דברים' and c[1] == CH})) for p in SPINE for r in range(len(he[p - 1])) if any(c[0] == 'דברים' and c[1] == CH for c in he_cites(clean(he[p - 1][r])))])
print('  the spine rows\' own Hebrew citations (book, chapter, verse) by row:', [(p, r + 1, he_cites(clean(he[p - 1][r]))) for p in SPINE for r in range(len(he[p - 1])) if he_cites(clean(he[p - 1][r]))])
print('  the spine rows\' English citations by row:', [(p, r + 1, re.findall(r'\(([A-Z][a-z]+\.? ?\d+:\d+(?:-\d+)?)\)', clean(en[p - 1][r]))) for p in SPINE for r in range(len(en[p - 1])) if re.findall(r'\(([A-Z][a-z]+\.? ?\d+:\d+(?:-\d+)?)\)', clean(en[p - 1][r]))])
print('  the spine rows with NO citation in either file:', [(p, r + 1) for p in SPINE for r in range(len(he[p - 1])) if not he_cites(clean(he[p - 1][r])) and not re.findall(r'\([A-Z][a-z]+\.? ?\d+:\d+', clean(en[p - 1][r]))])
print('  NO portion edge inside the chapter (Re\'eh 11:26-16:17 holds it whole) — the heads by verse, and the verses of the chapter with no head:', sorted({heads[p][1] for p in SPINE}), [v for v in range(1, VC[CH] + 1) if v not in {heads[p][1] for p in SPINE}])
